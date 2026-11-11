"""Validate per-root evidence without equating platform-dependent SVD errors.

This checks saved evidence and its recomputed polynomial diagnostics. It does
not replace fresh action holdouts or the physical tests in polynomial.py.
"""
import math
import numbers

import numpy as np


FIELDS = {
    "root", "singular_values", "action_interpolant_disagreement",
    "coefficient_scaled_disagreement", "polynomial_rank_defect_residual",
    "coefficient_scaled_root_solve_residual", "coefficient_evaluation_scale",
    "rank_threshold_absolute", "retained_gap_over_error_budget",
    "resolved_extra_nullity",
}
# Comparison allowance only: eight times the 128-epsilon rounding term in
# the physical error budget. It is expressed in coefficient-scale units,
# far below the unchanged 2e-9 / 2e-8 physical residual limits. This is a
# conservative float64 replay policy, not a theorem for arbitrary platforms.
ROUND_OFF = 1024 * np.finfo(float).eps


def finite_number(value):
    return (isinstance(value, numbers.Real) and not isinstance(value, (bool, np.bool_))
            and math.isfinite(value))


def certificate_structure(check, path="certificate", dimension=None):
    if not isinstance(check, dict) or set(check) != FIELDS:
        raise AssertionError(("certificate schema", path))
    for field in ("root", "singular_values"):
        values = check[field]
        if (not isinstance(values, list) or not values
                or not all(finite_number(x) for x in values)):
            raise AssertionError(("nonfinite or malformed certificate", path, field))
    if len(check["root"]) != 2:
        raise AssertionError(("complex root must have two components", path))
    sv = check["singular_values"]
    if dimension is not None and len(sv) != dimension:
        raise AssertionError(("singular-value count", path))
    if any(x < 0 for x in sv) or any(a < b for a, b in zip(sv, sv[1:])):
        raise AssertionError(("invalid singular values", path))
    if type(check["resolved_extra_nullity"]) is not int:
        raise AssertionError(("noninteger nullity", path))
    for field in FIELDS - {"root", "singular_values", "resolved_extra_nullity"}:
        x = check[field]
        if field == "retained_gap_over_error_budget" and x is None:
            continue
        if not finite_number(x) or x < 0:
            raise AssertionError(("nonfinite or negative certificate field", path, field))
    if check["coefficient_evaluation_scale"] <= 0 or check["rank_threshold_absolute"] <= 0:
        raise AssertionError(("nonpositive certificate scale", path))


def validate_root_certificates(data, path="sector", dimension=None):
    roots, certificates = data.get("roots"), data.get("direct_root_checks")
    if not isinstance(roots, list) or not isinstance(certificates, list):
        raise AssertionError(("root certificate lists", path))
    if len(roots) != len(certificates):
        raise AssertionError(("root certificate count", path, len(roots), len(certificates)))
    for index, (root, check) in enumerate(zip(roots, certificates)):
        location = f"{path}.root[{index}]"
        certificate_structure(check, location, dimension)
        if not isinstance(root, dict) or root.get("root") != check["root"]:
            raise AssertionError(("root certificate association", location))
        multiplicity = root.get("multiplicity")
        if type(multiplicity) is not int or multiplicity < 1:
            raise AssertionError(("invalid root multiplicity", location))
        if check["resolved_extra_nullity"] != multiplicity:
            raise AssertionError(("direct action multiplicity", location))


def assert_certificate_close(actual, expected, path="certificate"):
    """Compare dimensionful diagnostics using B=sum ||C_j||_F |D|^j.

    Root coordinates and supplied source-action evidence are inputs, so must
    agree exactly. Derived residuals/budgets may differ by ROUND_OFF * B.
    The inverse-budget gap is checked by reconstructing its singular value;
    relative differences of this ill-conditioned ratio are not accuracy tests.
    Fresh physical acceptance must still be enforced by the caller.
    """
    certificate_structure(actual, path)
    certificate_structure(expected, path)
    for field in ("root", "singular_values", "action_interpolant_disagreement",
                  "resolved_extra_nullity"):
        if actual[field] != expected[field]:
            raise AssertionError(("certificate input or rank changed", path, field))
    scale = max(actual["coefficient_evaluation_scale"], expected["coefficient_evaluation_scale"])
    for field in ("polynomial_rank_defect_residual", "rank_threshold_absolute",
                  "coefficient_evaluation_scale"):
        if abs(actual[field] - expected[field]) > ROUND_OFF * scale:
            raise AssertionError(("certificate change exceeds roundoff scale", path, field))
    for field in ("coefficient_scaled_disagreement", "coefficient_scaled_root_solve_residual"):
        if abs(actual[field] - expected[field]) > ROUND_OFF:
            raise AssertionError(("scaled certificate change exceeds roundoff", path, field))
    a_gap, e_gap = actual["retained_gap_over_error_budget"], expected["retained_gap_over_error_budget"]
    if (a_gap is None) != (e_gap is None):
        raise AssertionError(("retained gap structure changed", path))
    if a_gap is not None:
        a_sv = a_gap * actual["rank_threshold_absolute"]
        e_sv = e_gap * expected["rank_threshold_absolute"]
        if not math.isfinite(a_sv) or not math.isfinite(e_sv) or abs(a_sv - e_sv) > ROUND_OFF * scale:
            raise AssertionError(("retained singular-value evidence changed", path))
        if min(a_gap, e_gap) < 20:
            raise AssertionError(("unresolved direct-action gap", path))
