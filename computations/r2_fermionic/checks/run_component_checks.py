#!/usr/bin/env python3
"""Replay the current R² component construction in a temporary directory.

The restored kernels check the current source equations and collected action.
Archived revisions and the earlier numerical AdS reconstruction are not inputs.
No repository input, expected record or output is rewritten.
"""
from pathlib import Path
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
STAGES = (
    ("verify_step1_primed_bf", "step1_primed_bf_verification.json"),
    ("verify_step2_mixed_linear", "step2_mixed_linear_verification.json"),
    ("verify_step3_bf_insertion", "step3_bf_insertion_verification.json"),
    ("verify_step4_gold_gauge", "step4_gold_gauge_verification.json"),
    ("build_step6_supercovariant", None),
    ("verify_step6_supercovariant", "step6_supercovariant_verification.json"),
    ("verify_step6_supercovariant_tensors", "step6_supercovariant_tensor_verification.json"),
    ("verify_step6_supercovariant_collections", "step6_supercovariant_collection_verification.json"),
    ("verify_step6_collections_majorana", "step6_collection_majorana_verification.json"),
)


def checked_report(path):
    report = json.loads(path.read_text())
    if report.get("status") == "FAIL" or report.get("failed") or report.get("failures"):
        raise AssertionError(f"Failed component checks: {path.name}")
    for name in ("checks", "details", "results"):
        items = report.get(name, [])
        if isinstance(items, list) and any(item.get("pass") is False for item in items):
            raise AssertionError(f"Failed {name}: {path.name}")
    return report


def compare_ledger(work, name, keys):
    actual = json.loads((work / "build" / name).read_text())
    expected = json.loads((ROOT / "expected" / name).read_text())
    for key in keys:
        if actual[key] != expected[key]:
            raise AssertionError(f"Regenerated {name}: {key} differs from current expected action")
    # Hashes identify the current supplied notes, not removed presentation revisions.
    sources = {
        "source_sha256": "06_step4_Gold_unprimed_vector_and_gauge.md",
        "map_sha256": "08_step5_primed_composite_vector_insertion.md",
        "prior_step6_sha256": "10_step6_gauged_action_through_two_fermions.md",
    }
    for key, filename in sources.items():
        digest = hashlib.sha256((work / "notes" / filename).read_bytes()).hexdigest()
        if actual[key] != digest:
            raise AssertionError(f"Current source hash mismatch: {filename}")
    print(f"PASS regenerated {name}: {actual['terms']} terms match current expected data", flush=True)


def main():
    if sys.flags.optimize:
        raise RuntimeError("Run without -O; the component kernels use assertions.")
    with tempfile.TemporaryDirectory(prefix="r2-component-checks-") as directory:
        work = Path(directory) / "r2"
        shutil.copytree(ROOT / "inputs/reference/r2/notes", work / "notes")
        # Legacy kernels read dollar delimiters; only the temporary wrappers change.
        for document in (work / "notes").rglob("*.md"):
            text = re.sub(
                r"^ {0,3}```math[ \t]*\n(.*?)^ {0,3}```[ \t]*$",
                lambda m: "$$\n" + m[1] + "$$", document.read_text(), flags=re.M | re.S,
            )
            text = re.sub(r"\$`(.*?)`\$", lambda m: "$" + m[1] + "$", text, flags=re.S)
            document.write_text(text)
        shutil.copytree(ROOT / "src/kernels", work / "scripts")
        (work / "build").mkdir()
        for program, report in STAGES:
            result = subprocess.run(
                [sys.executable, "-B", str(work / "scripts" / f"{program}.py")],
                cwd=work, env=dict(os.environ, PYTHONDONTWRITEBYTECODE="1"),
                text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
            )
            if result.returncode:
                print(result.stdout)
                raise RuntimeError(f"{program} failed with exit status {result.returncode}")
            if report:
                value = checked_report(work / "build" / report)
                count = value.get("passed", value.get("checks"))
                if isinstance(count, list):
                    count = len(count)
                print(f"PASS {program}: {count} checks", flush=True)
        compare_ledger(work, "step6_supercovariant_ledger.json",
                       ("rows", "groups", "operators", "terms", "degrees"))
        compare_ledger(work, "step6_supercovariant_collected_ledger.json",
                       ("rows", "groups", "terms", "degrees"))
        sys.path.insert(0, str(ROOT))
        from calculations.action import collect_rows, check_canonical_display
        ledger = json.loads((work / "build/step6_supercovariant_collected_ledger.json").read_text())
        rows = collect_rows(ledger["rows"])
        check_canonical_display(rows)
        if rows != json.loads((ROOT / "outputs/r2_action.json").read_text())["rows"]:
            raise AssertionError("Regenerated canonical action differs from current output")
        print(f"PASS regenerated canonical action: {len(rows)} terms and displayed expression", flush=True)
    print("PASS current R² component checks; repository files unchanged")


if __name__ == "__main__":
    main()
