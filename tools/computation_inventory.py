#!/usr/bin/env python3
"""List computational sources and static numerical-specialization indicators.

This script reads text only: it never imports or executes a source program.
Indicators locate code for review; they are neither an exhaustive audit nor a
proof that each matching line substitutes a free parameter.
"""
import argparse
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
INDICATORS = {
    "random_sampling": re.compile(r"\b(?:default_rng|random|randint|integers)\b"),
    "floating_evaluation": re.compile(r"\b(?:float|evalf|allclose|isclose)\s*\("),
    "rational_reconstruction": re.compile(r"\b(?:limit_denominator|interpolate|nsimplify)\s*\("),
    "fixed_scale_note": re.compile(r"\b(?:g|ell|k|valueL)\s*=\s*(?:-?1\b|np\.sqrt\(2\))"),
}
KNOWN_LIMITATIONS = {
    "two_derivative_fermionic": [
    ],
    "weyl_fermionic": [
        "src/reference_checks/weyl_clifford_components.py: randomized tensor components",
        "src/reference_checks/verify_weyl_scalar_canonicalization.py: sampled component comparisons",
        "src/reference_checks/verify_weyl_vector_canonicalization.py: sampled component comparisons",
    ],
    "r2_fermionic": [
        "src/kernels/verify_step6_supercovariant_tensors.py: random tensor components",
    ],
    "log_fermionic": [
        "Exact rational descendant kernels are supplied, but the complete imported pipeline has not been audited for unrestricted symbolic execution.",
        "Component Clifford/epsilon checks use a concrete representation; they do not establish an orientation-independent covariant spectrum.",
    ],
    "gauss_bonnet": [
        "Component checks in gauss_bonnet/ads5/code use a fixed AdS scale and g=1, k=-1, x=sqrt(2).",
    ],
}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--details", action="store_true", help="Include matched file paths and line numbers.")
    args = parser.parse_args()
    packages = []
    for directory in sorted((ROOT / "computations").iterdir()):
        if not directory.is_dir():
            continue
        files = sorted(directory.rglob("*.py"))
        hits = []
        for path in files:
            for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
                names = [name for name, pattern in INDICATORS.items() if pattern.search(line)]
                if names:
                    hits.append({"path": str(path.relative_to(ROOT)), "line": number, "indicators": names})
        package = {
            "package": directory.name,
            "python_sources": len(files),
            "indicator_lines": len(hits),
            "known_limitations": KNOWN_LIMITATIONS.get(directory.name, []),
            "execution": "Not imported or executed by this inventory",
        }
        if args.details:
            package["indicators"] = hits
        packages.append(package)
    print(json.dumps({
        "status": "INVENTORY_ONLY",
        "packages": packages,
        "gauss_bonnet_component_limitations": KNOWN_LIMITATIONS["gauss_bonnet"],
        "scope": "Static source inventory. Absence of a match does not certify a program.",
    }, indent=2))


if __name__ == "__main__":
    main()
