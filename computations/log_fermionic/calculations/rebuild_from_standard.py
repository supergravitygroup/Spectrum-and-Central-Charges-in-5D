"""Replay the gauged multiplet and BF density from declared component inputs.

By default, adopt the distributed expected/*_standard.json polynomials. This
is a downstream replay, not reconstruction of the missing historical run or
an independent verification of the Standard-Weyl primary descent.
"""
import argparse
from collections import Counter
from pathlib import Path
import hashlib
import json
import sys
from src.algebra import ROOT, prepare_outputs
from src.polynomials import load, save
from calculations.descendants import SLOTS
from calculations.gauged_components import substitute_and_collect
from calculations.density import density_blocks, write_density
from checks.regression import compare_standard, compare_gauged, check_ordered_connection
from checks.algebra_identities import main as check_algebra_identities


def compare_density(actual, reference):
    """Ignore additive ordering only; keep every coefficient and ordered factor."""
    if len(actual) != 7 or len(reference) != 7:
        raise AssertionError("Expected seven complete BF contraction blocks")
    for index, (new, old) in enumerate(zip(actual, reference)):
        key = "terms_with_density_coefficient"
        if {k: v for k, v in new.items() if k != key} != {k: v for k, v in old.items() if k != key}:
            raise AssertionError(("BF contraction changed", index))
        records = lambda rows: Counter(json.dumps(row, sort_keys=True) for row in rows)
        if records(new[key]) != records(old[key]):
            raise AssertionError(("BF coefficient/term records changed", index))
    return [len(block["terms_with_density_coefficient"]) for block in actual]


def main(argv=None):
    if sys.flags.optimize:
        raise RuntimeError("Run without -O.")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--historical-input-dir", type=Path,
                        help="explicit alternative containing L.json, phi.json, N.json, E.json")
    args = parser.parse_args(argv)
    adopted = args.historical_input_dir is None
    paths = {slot: (ROOT / "expected" / f"{slot}_standard.json" if adopted
                    else args.historical_input_dir / f"{slot}.json") for slot in SLOTS}
    missing = [str(path) for path in paths.values() if not path.is_file()]
    if missing:
        raise FileNotFoundError("Missing replay input(s); outputs preserved: " + ", ".join(missing))
    report_path = ROOT / "outputs/downstream_summary.json"
    density_path = ROOT / "outputs/bf_density.json"
    retained_density = json.loads(density_path.read_text())["blocks"] if density_path.is_file() else None
    standard = {slot: load(path) for slot, path in paths.items()}
    for slot, polynomial in standard.items():
        compare_standard(polynomial, slot)
    prepare_outputs()
    report_path.unlink(missing_ok=True)
    report = {
        "scope": "downstream replay from adopted canonical components" if adopted else "downstream replay from explicitly supplied components",
        "input_policy": "distributed canonical components" if adopted else "explicit alternative inputs; historical identity not certified",
        "standard_comparison_is_independent": False if adopted else None,
        "input_files": {slot: str(path.relative_to(ROOT)) if path.is_relative_to(ROOT) else str(path)
                        for slot, path in paths.items()},
        "fresh_primary_derivation": False,
        "input_sha256": {
            slot: hashlib.sha256(path.read_bytes()).hexdigest() for slot, path in paths.items()
        },
        "gauged": {},
    }
    multiplet = {}
    for slot in SLOTS:
        multiplet[slot], detail = substitute_and_collect(standard[slot], slot)
        detail["accepted_residual"] = compare_gauged(multiplet[slot], slot)
        report["gauged"][slot] = detail
        save(ROOT / "outputs/gauged" / f"{slot}.json", multiplet[slot])
    check_ordered_connection()
    check_algebra_identities()
    report["matched_BF_term_counts"] = (compare_density(density_blocks(multiplet), retained_density)
                                      if retained_density is not None else None)
    report["retained_BF_comparison"] = "PASS" if retained_density is not None else "NOT RUN: no retained density supplied"
    write_density(multiplet)
    report["status"] = "PASS"
    report_path.write_text(json.dumps(report, indent=2) + "\n")
    print("PASS: downstream replay; source primary was not recomputed.")
    print("Retained seven-block comparison:", report["retained_BF_comparison"])


if __name__ == "__main__":
    main()
