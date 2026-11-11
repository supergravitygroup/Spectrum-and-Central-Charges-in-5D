"""S0 and S1 from the twelve surviving source terms; selected GB-S+ only.

Sources: derivations/background/STEP_04_ZEROTH_ORDER_ACTION.md, (4.1)-(4.8),
and STEP_05_BRANCH_CATALOGUE.md. The zero routes of all other terms are
documented in the first-order source ledger. We do not enumerate other branches.
"""

import sympy as sp

from inputs.symbols import L, N, k, g, lam, x, a, branch_values, on_branch
from src.reporting import action_coefficients, check_zero, write_json


def background_substitutions():
    """Each value is the tensor body evaluated before its source coefficient."""
    composite_D = -5 * k / 8 + g * N / 4 + g**2 * L**2 / 16
    dilaton_box = -5 * k / 2
    return {
        "Weyl_sigma_N:2": composite_D**2,
        "LOG_seed:46": dilaton_box**2,
        "LOG_seed:47": g**2 * L**2 * dilaton_box,
        "LOG_seed:48": g * N * dilaton_box,
        "LOG_seed:49": g**4 * L**4,
        "LOG_seed:50": g**3 * N * L**2,
        "LOG_seed:51": g**2 * N**2,
        "LOG_seed:71": g**2 * L * (-15 * k * L / 2),
        "LOG_seed:74": 5 * k**2 / 4,
        "LOG_seed:75": sp.Integer(0),
        "LOG_seed:76": g * (-10 * k * N),
        "LOG_seed:80": g**4 * L**4 / 2,
    }


def first_order_substitutions():
    """Explicit product-rule variations; ordered covariant boxes are retained."""
    ell, n, r, box_ell, box_n = sp.symbols("ell n r box_ell box_n")
    composite_D = -5 * k / 8 + g * N / 4 + g**2 * L**2 / 16
    delta_D = -r / 32 + g * n / 4 + g**2 * L * ell / 8
    dilaton_box = -5 * k / 2
    variations = {
        "Weyl_sigma_N:2": 2 * composite_D * delta_D,
        "LOG_seed:46": 2 * dilaton_box * (-r / 8),
        "LOG_seed:47": g**2 * (2 * L * ell * dilaton_box - L**2 * r / 8),
        "LOG_seed:48": g * (n * dilaton_box - N * r / 8),
        "LOG_seed:49": 4 * g**4 * L**3 * ell,
        "LOG_seed:50": g**3 * (L**2 * n + 2 * N * L * ell),
        "LOG_seed:51": 2 * g**2 * N * n,
        "LOG_seed:71": g**2 * (
            ell * (-15 * k * L / 2)
            + L * (box_ell - 15 * k * ell / 2 - 3 * L * r / 8)
        ),
        "LOG_seed:74": k * r / 8,
        "LOG_seed:75": sp.Integer(0),
        "LOG_seed:76": g * (box_n - 10 * k * n - N * r / 2),
        "LOG_seed:80": 2 * g**4 * L**3 * ell,
    }
    two_derivative = (
        -2 * (box_ell - 15 * k * ell / 2 - 3 * L * r / 8)
        -8 * (ell * composite_D + L * delta_D)
        -4 * N * n / L + 2 * N**2 * ell / L**2 - 4 * g * n
        + 4 * g**2 * L * ell
    )
    return (ell, n, r, box_ell, box_n), variations, two_derivative


def calculate():
    coefficients = action_coefficients()
    terms = {
        source_id: sp.expand(coefficients[source_id] * body)
        for source_id, body in background_substitutions().items()
    }
    higher_density = sp.expand(sum(terms.values()))
    two_density = (
        20 * L * k - 2 * N**2 / L - 2 * g * L * N - 4 * g * N
        + 2 * g**2 * L**2 - g**2 * L**3 / 2
    )
    density = two_density + lam * higher_density

    variables, variations, two_first = first_order_substitutions()
    first_order = sp.expand(two_first + lam * sum(
        coefficients[source_id] * body for source_id, body in variations.items()
    ))
    ell, n, r, box_ell, box_n = variables
    curvature_coefficient = first_order.coeff(r)
    tadpoles = {
        "L": first_order.coeff(ell),
        "N": first_order.coeff(n),
        "metric_trace": density / 2 - 4 * k * curvature_coefficient,
    }
    residuals = {}
    check_zero(residuals, "scalar L variation", tadpoles["L"] - sp.diff(density, L))
    check_zero(residuals, "scalar N variation", tadpoles["N"] - sp.diff(density, N))
    check_zero(residuals, "metric scaling cross-check", sp.diff(density, k) - 20 * curvature_coefficient)
    for field, tadpole in tadpoles.items():
        check_zero(residuals, f"GB-S+ tadpole: {field}", on_branch(tadpole))

    # The selected positive root is solved without borrowing the spectrum.
    positive_root = 2 / (1 + sp.sqrt(1 + 2 * a))
    check_zero(residuals, "selected root equation", a * positive_root**2 + 2 * positive_root - 2)
    for term in sp.Add.make_args(sp.expand(density)):
        powers = term.as_powers_dict()
        dimension = powers.get(g, 0) + powers.get(N, 0) + 2 * powers.get(k, 0) - 2 * powers.get(lam, 0)
        if dimension != 2:
            raise AssertionError(f"Wrong density dimension: {term}")

    return {
        "scope": "selected-branch S0/S1 calculation with source coefficients; other-field zeros use the supplied analytic ledger",
        "higher_derivative_source_terms": terms,
        "S0_density": sp.factor(density),
        "S1_before_boundary_transfers": first_order,
        "total_divergence_coefficients": {"box_ell": first_order.coeff(box_ell), "box_n": first_order.coeff(box_n)},
        "tadpoles": {key: sp.factor(value) for key, value in tadpoles.items()},
        "background": {str(key): value for key, value in branch_values().items()},
        "positive_root_x": positive_root,
        "domain": "g != 0; a >= -1/2; 0 < x <= 2; scalar patch L > 0",
        "residuals": residuals,
    }


def main():
    result = calculate()
    write_json("background.json", result)
    print(f"Background: {len(result['residuals'])} exact checks passed.")


if __name__ == "__main__":
    main()
