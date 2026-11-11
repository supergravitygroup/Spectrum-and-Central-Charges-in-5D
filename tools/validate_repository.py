#!/usr/bin/env python3
"""Check local links and anchors, images, tables, Python syntax and file hashes.

This is a structural check. It neither executes archived calculations nor
certifies equations, spectrum claims or the targets of external URLs.
"""
import argparse
import ast
import hashlib
import html
import json
import re
import unicodedata
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "references" / "artifact_hashes.json"
IMAGE_SUFFIXES = {".png", ".jpg", ".jpeg", ".gif", ".webp", ".svg", ".avif",
                  ".bmp", ".ico", ".apng", ".tif", ".tiff"}


def files():
    return sorted(
        p for p in ROOT.rglob("*")
        if p.is_file() and not any(
            part in {".git", "__pycache__", ".DS_Store"} for part in p.parts
        ) and p.suffix != ".pyc"
    )


def without_fenced_code(text):
    """Mask fenced blocks while preserving source line numbers."""
    marker = None
    lines = []
    for line in text.splitlines(keepends=True):
        fence = re.match(r"^ {0,3}(`{3,}|~{3,})(.*)$", line.rstrip("\r\n"))
        if marker is None:
            if fence:
                marker = fence.group(1)
                lines.append("\n" if line.endswith("\n") else "")
            else:
                lines.append(line)
        else:
            if (fence and fence.group(1)[0] == marker[0]
                    and len(fence.group(1)) >= len(marker)
                    and not fence.group(2).strip()):
                marker = None
            lines.append("\n" if line.endswith("\n") else "")
    return "".join(lines)


def markdown_targets(text):
    """Yield (destination, is_image) outside code and mathematics.

    Reference-style links are checked by their definition. Balanced parentheses
    are allowed in inline destinations. Anchor existence is checked separately.
    """
    text = without_fenced_code(text)
    text = re.sub(r"\$\$.*?\$\$|\\\[.*?\\\]", "", text, flags=re.S)
    text = re.sub(r"(?<!\\)\$[^\n$]*?(?<!\\)\$|\\\(.*?\\\)", "", text)
    text = re.sub(r"`+[^`\n]*`+", "", text)
    for match in re.finditer(r"(!?)\[[^\]\n]*\]\(", text):
        is_image = bool(match.group(1))
        start = match.end()
        if start < len(text) and text[start] == "<":
            end = text.find(">", start)
            if end >= 0:
                yield text[start + 1:end], is_image
            continue
        depth, end = 1, start
        while end < len(text) and text[end] != "\n":
            if text[end] == "\\":
                end += 2
                continue
            if text[end] == "(":
                depth += 1
            elif text[end] == ")":
                depth -= 1
                if depth == 0:
                    break
            end += 1
        if depth == 0:
            destination = text[start:end].split(' "')[0].strip()
            if not any(c.isspace() for c in destination):
                yield destination, is_image
    normalize = lambda label: " ".join(label.split()).casefold()
    image_labels = set()
    for match in re.finditer(r"!\[([^\]\n]*)\](?:\[([^\]\n]*)\])?(?!\()", text):
        image_labels.add(normalize(match.group(2) or match.group(1)))
    for match in re.finditer(
            r"(?m)^ {0,3}\[([^\]\n]+)\]:\s*(?:<([^>\n]+)>|(\S+))", text):
        yield match.group(2) or match.group(3), normalize(match.group(1)) in image_labels


def markdown_links(text):
    """Yield all destinations, including embedded images."""
    for target, _ in markdown_targets(text):
        yield target


def heading_slug(heading):
    """Return the GitHub-style anchor for rendered inline heading text.

    Formatting delimiters and link destinations do not belong to the heading
    text. Unicode letters, numbers and combining marks are retained; punctuation
    and symbols are removed, except for the hyphens and underscores accepted by
    GitHub anchors. Consecutive spaces intentionally produce consecutive dashes.
    """
    code = []

    def keep_code(match):
        code.append(match.group(2).strip())
        return f"\x00{len(code)-1}\x00"

    heading = re.sub(r"(`+)(.*?)\1", keep_code, heading)
    heading = re.sub(r"!?\[([^\]]*)\]\([^)]*\)", r"\1", heading)
    heading = re.sub(r"!?\[([^\]]*)\]\[[^\]]*\]", r"\1", heading)
    heading = re.sub(r"<[^>]+>", "", heading)
    heading = re.sub(r"\\([!\"#$%&'()*+,\-./:;<=>?@\[\]\\^_`{|}~])", r"\1", heading)
    heading = heading.replace("*", "").replace("~", "")
    heading = re.sub(r"(?<!\w)_+|_+(?!\w)", "", heading)
    heading = re.sub(r"\x00(\d+)\x00", lambda match: code[int(match[1])], heading)
    heading = html.unescape(heading).strip().lower()
    return "".join(
        "-" if char.isspace() else char
        for char in heading
        if char.isspace() or char in "-_"
        or unicodedata.category(char)[0] in "LNM"
    )


def markdown_anchors(text):
    """Collect explicit HTML IDs/names and generated ATX/setext heading IDs."""
    text = without_fenced_code(text)
    text = re.sub(r"<!--.*?-->", "", text, flags=re.S)
    text = re.sub(r"\A---\s*\n.*?\n---\s*(?:\n|\Z)", "", text, count=1, flags=re.S)
    anchors = set()
    tag_text = re.sub(r"(`+).*?\1", "", text)
    for tag in re.findall(r"<[A-Za-z][^>]*>", tag_text):
        for match in re.finditer(
                r"\s(?:id|name)\s*=\s*(?:\"([^\"]*)\"|'([^']*)'|([^\s>]+))", tag, re.I):
            anchors.add(html.unescape(next(value for value in match.groups() if value is not None)))
    used = set()
    lines = text.splitlines()
    for index, line in enumerate(lines):
        atx = re.match(r"^ {0,3}#{1,6}(?:[ \t]+(.*?)|[ \t]*)$", line)
        if atx:
            heading = re.sub(r"[ \t]+#+[ \t]*$", "", atx[1] or "")
        elif (index and re.fullmatch(r" {0,3}(?:=+|-+)[ \t]*", line)
              and lines[index - 1].strip()
              and not re.match(r"\s*(?:[#>|]|[-*+]\s|\d+[.)]\s)", lines[index - 1])):
            heading = lines[index - 1].strip()
        else:
            continue
        base = heading_slug(heading)
        slug, suffix = base, 0
        while slug in used:
            suffix += 1
            slug = f"{base}-{suffix}"
        used.add(slug)
        anchors.add(slug)
    return anchors


def table_cells(line):
    """Split pipe-table cells; escaped pipes remain inside their cell."""
    cells, start = [], 0
    for match in re.finditer(r"\|", line):
        backslashes = len(line[:match.start()]) - len(line[:match.start()].rstrip("\\"))
        if backslashes % 2 == 0:
            cells.append(line[start:match.start()].strip())
            start = match.end()
    cells.append(line[start:].strip())
    if line.lstrip().startswith("|"):
        cells = cells[1:]
    if cells and cells[-1] == "" and line.rstrip().endswith("|"):
        cells = cells[:-1]
    return cells


def markdown_table_errors(text):
    """Find column-count mismatches in pipe tables outside fenced code."""
    lines = without_fenced_code(text).splitlines()
    for index in range(1, len(lines)):
        separator = table_cells(lines[index])
        if ("|" not in lines[index] or not separator
                or not all(re.fullmatch(r":?-+:?", cell) for cell in separator)
                or "|" not in lines[index - 1]):
            continue
        columns = len(separator)
        row_indices = [index - 1]
        end = index + 1
        while end < len(lines) and lines[end].strip() and "|" in lines[end]:
            row_indices.append(end)
            end += 1
        for row in row_indices:
            actual = len(table_cells(lines[row]))
            if actual != columns:
                yield {"line": row + 1, "expected_columns": columns,
                       "actual_columns": actual}


def local_target(path, target):
    if not target:
        return None
    parsed = urlsplit(target)
    if parsed.scheme or parsed.netloc:
        return None
    value = unquote(parsed.path)
    if not value:
        return path.resolve() if parsed.fragment else None
    # TeX expressions can have Markdown-like brackets; they are not links.
    if "\\" in value or value.startswith(("$", "{")):
        return None
    return (path.parent / value).resolve()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--details", action="store_true")
    args = parser.parse_args()
    paths = files()
    errors = []
    links = 0
    images = 0
    py_count = 0
    md_count = 0
    fragments = 0
    anchor_cache = {}
    for path in paths:
        relative = str(path.relative_to(ROOT))
        if path.suffix == ".py":
            py_count += 1
            try:
                ast.parse(path.read_text(encoding="utf-8-sig"), filename=relative)
            except (SyntaxError, UnicodeError) as error:
                errors.append({"file": relative, "kind": "python_syntax", "error": str(error)})
        if path.suffix.lower() == ".md":
            md_count += 1
            content = path.read_text(encoding="utf-8")
            for error in markdown_table_errors(content):
                errors.append({"file": relative, "kind": "table_columns", **error})
            for link, is_image in markdown_targets(content):
                target = local_target(path, link)
                if target is None:
                    continue
                links += 1
                images += is_image
                if not target.is_relative_to(ROOT):
                    errors.append({"file": relative, "kind": "nonportable_link", "target": link})
                elif not target.exists():
                    errors.append({"file": relative, "kind": "missing_file", "target": link})
                elif is_image and (not target.is_file() or target.suffix.lower() not in IMAGE_SUFFIXES):
                    errors.append({"file": relative, "kind": "non_image_embed", "target": link})
                elif not is_image and target.is_file() and target.suffix.lower() == ".md":
                    fragment = unquote(urlsplit(link).fragment)
                    if fragment:
                        fragments += 1
                        if target not in anchor_cache:
                            anchor_cache[target] = markdown_anchors(target.read_text(encoding="utf-8"))
                        if fragment not in anchor_cache[target]:
                            errors.append({"file": relative, "kind": "missing_fragment", "target": link})
    hash_count = 0
    if MANIFEST.exists():
        record = json.loads(MANIFEST.read_text())
        expected = record["sha256"]
        current = {str(p.relative_to(ROOT)): p for p in paths if p != MANIFEST}
        for name, expected_digest in expected.items():
            hash_count += 1
            if name not in current:
                errors.append({"file": name, "kind": "manifest_missing_file"})
            elif hashlib.sha256(current[name].read_bytes()).hexdigest() != expected_digest:
                errors.append({"file": name, "kind": "hash_mismatch"})
        for name in sorted(set(current) - set(expected)):
            errors.append({"file": name, "kind": "not_in_manifest"})
    else:
        errors.append({"file": str(MANIFEST.relative_to(ROOT)), "kind": "manifest_absent"})
    result = {
        "status": "PASS" if not errors else "FAIL",
        "scope": "Local file and Markdown anchor targets, images, pipe-table columns, Python parsing and current artifact hashes only; no scientific calculation executed.",
        "markdown_files": md_count,
        "local_file_links": links,
        "local_image_targets": images,
        "pipe_table_columns_checked": True,
        "python_files_parsed": py_count,
        "hashes_checked": hash_count,
        "fragment_anchors_checked": True,
        "markdown_fragment_links": fragments,
        "external_urls_checked": False,
        "errors_count": len(errors),
    }
    if args.details:
        result["errors"] = errors
    print(json.dumps(result, indent=2, ensure_ascii=False))
    raise SystemExit(1 if errors else 0)


if __name__ == "__main__":
    main()
