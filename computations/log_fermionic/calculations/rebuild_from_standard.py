"""Fast downstream rebuild from this package's previously computed components.

This deliberately does not claim a fresh primary derivation. It reads only
outputs/standard_weyl/*.json, records their hashes, rechecks them, and rebuilds
the gauged multiplet and BF action. The primary descent is documented in
calculations/descendants.py and the package derivations.
"""
import hashlib
import json
import sys
from src.algebra import ROOT, prepare_outputs
from src.polynomials import load, save
from calculations.descendants import SLOTS
from calculations.gauged_components import substitute_and_collect
from calculations.density import write_density
from checks.regression import compare_standard, compare_gauged, check_ordered_connection
from checks.algebra_identities import main as check_algebra_identities


def main():
    if sys.flags.optimize:
        raise RuntimeError("Run without -O.")
    prepare_outputs()
    report_path = ROOT / "outputs/downstream_summary.json"
    report_path.unlink(missing_ok=True)
    paths = {slot: ROOT / "outputs/standard_weyl" / f"{slot}.json" for slot in SLOTS}
    if not all(path.is_file() for path in paths.values()):
        raise FileNotFoundError("This downstream command requires all four outputs/standard_weyl component files; see README.md for the retained inputs and scope.")
    standard = {slot: load(path) for slot, path in paths.items()}
    for slot, polynomial in standard.items():
        compare_standard(polynomial, slot)
    report = {
        "scope": "downstream rebuild from previously computed Standard-Weyl components",
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
    write_density(multiplet)
    report["status"] = "PASS"
    report_path.write_text(json.dumps(report, indent=2) + "\n")
    print("PASS: downstream rebuild; source primary was not recomputed in this run.")


if __name__ == "__main__":
    main()
