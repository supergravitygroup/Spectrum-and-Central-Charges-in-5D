"""03. Rebuild ordered action ledgers and collect identical tensor words.

Collection combines scalar coefficients only. Factor order, derivative arguments,
Majorana bars and index variance are retained. No EOM or integration by parts.
"""
from collections import OrderedDict
import json
import re
import sympy as sp
from src.runtime import ROOT, OUTPUT, WORK, read_json, write_json


def collect_rows(rows):
    buckets = OrderedDict()
    symbols = {name: sp.Symbol(name, real=True) for name in ("L", "N", "g")}
    for index, row in enumerate(rows, 1):
        if row["degree"] not in (0, 2):
            raise ValueError("Unexpected fermion degree.")
        key = json.dumps(row["factors"], sort_keys=True)
        bucket = buckets.setdefault(key, {"row": row, "coefficient": sp.S.Zero, "source_rows": []})
        bucket["coefficient"] += sp.sympify(row["coefficient"], locals=symbols)
        bucket["source_rows"].append(index)
    collected = []
    for bucket in buckets.values():
        coefficient = sp.factor(bucket["coefficient"])
        if coefficient == 0:
            continue
        row = dict(bucket["row"])
        old_coefficient = sp.sympify(row["coefficient"], locals=symbols)
        prefix = "" if old_coefficient == 1 else "-" if old_coefficient == -1 else sp.latex(old_coefficient)
        if len(bucket["source_rows"]) > 1:
            if not row["tex"].startswith(prefix):
                raise ValueError("Coefficient and displayed tensor word disagree.")
            word = row["tex"][len(prefix):].strip()
            absolute = -coefficient if coefficient.could_extract_minus_sign() else coefficient
            tex_coefficient = "" if absolute == 1 else sp.latex(absolute)
            row["tex"] = ("- " if coefficient.could_extract_minus_sign() else "") + tex_coefficient + " " + word
        row.update(coefficient=str(coefficient), source_rows=bucket["source_rows"])
        collected.append(row)
    return collected


def write_action(rows):
    write_json(OUTPUT / "r2_action.json", {
        "presentation_lock": "R2-BF-CANONICAL-EXPLICIT2-20260921-v2",
        "definition_revision": "COOMANS-GAUGED-DEFINITIONS-20260922-v1",
        "scope": "Retained supercovariant expression through explicit degree two; see CLAIMS.md.",
        "rows": rows,
    })
    text = [
        "# Rebuilt R² action\n",
        "Full definitions and the physical-order interpretation: "
        "[canonical derivation](../../../r2/action/details/construction.md).\n",
        "The integrand is the sum of the following ordered terms. "
        "Multiply by $`\\lambda_{R^2}\\int d^5x\\,e`$; retain the declared $`\\leq2`$ scope.\n",
    ]
    for index, row in enumerate(rows, 1):
        text.append(f"Term {index}; source rows {row['source_rows']}; explicit degree {row['degree']}.\n\n"
                    "```math\n" + row["tex"] + "\n```\n")
    (OUTPUT / "r2_action.md").write_text("\n".join(text))


def check_canonical_display(rows):
    """Compare every displayed factor/sign with the independent source document."""
    document = (ROOT.parents[1] / "r2/action/details/construction.md").read_text()
    document = re.sub(
        r"^ {0,3}```math[ \t]*\n(.*?)^ {0,3}```[ \t]*$",
        lambda m: "$$\n" + m[1] + "$$", document, flags=re.M | re.S,
    )
    equations = dict((tag, body) for body, tag in re.findall(
        r"\$\$\s*\n(.*?)\\tag\{([^}]+)\}\s*\n\$\$", document, re.S
    ))
    integrand = equations["R2"].split(r"\Bigg\{", 1)[1].split(r"\Bigg\}_{\leq2}", 1)[0]
    words = [row["tex"] if index == 0 or row["tex"].startswith("-") else "+" + row["tex"]
             for index, row in enumerate(rows)]
    normalize = lambda text: re.sub(r"\s+", "", text.replace("\\\\", "").replace("&", ""))
    if normalize(integrand) != normalize("".join(words)):
        raise AssertionError("Rebuilt canonical display differs in coefficient, sign or tensor word.")


def run():
    """Collect the supplied current tensor ledger and check its displayed action.

    This is exact coefficient collection; it does not rederive the input map.
    """
    rows = collect_rows(read_json(ROOT / "expected/step6_supercovariant_collected_ledger.json")["rows"])
    check_canonical_display(rows)
    write_action(rows)
    return rows
