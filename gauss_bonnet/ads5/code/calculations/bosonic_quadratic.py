"""Rebuild the bosonic quadratic coefficients and expose the reduction steps.

Scalar/metric input: Step 6, (6.7)-(6.18). Form input: FD1-FD10 and
(6.20)-(6.30). Covariant variation and boundary currents are supplied as
analytic derivations, not silently replaced by a reduced-potential variation.
"""

import sympy as sp

from inputs.symbols import L, N, k, g, lam, x, c, on_branch
from src.reporting import action_coefficients, check_zero, write_json


def scalar_metric_restriction():
    """Evaluate source tensor bodies and integrate the displayed box terms."""
    coefficients = action_coefficients()
    R, ricci_squared, riemann_squared = sp.symbols("R Ricci_squared Riemann_squared")
    gradient, box_L, box_N = sp.symbols("gradient_L_squared box_L box_N")
    D = -R / 32 + g * N / 4 + g**2 * L**2 / 16
    source_bodies = {
        "Weyl_sigma_N:1": riemann_squared - sp.Rational(4, 3) * ricci_squared + R**2 / 6,
        "Weyl_sigma_N:2": D**2,
        "LOG_seed:46": R**2 / 64,
        "LOG_seed:47": -g**2 * L**2 * R / 8,
        "LOG_seed:48": -g * N * R / 8,
        "LOG_seed:49": g**4 * L**4,
        "LOG_seed:50": g**3 * N * L**2,
        "LOG_seed:51": g**2 * N**2,
        "LOG_seed:71": g**2 * L * (box_L - 3 * R * L / 8),
        "LOG_seed:74": ricci_squared / 9 - 11 * R**2 / 576,
        "LOG_seed:75": g**2 * gradient,
        "LOG_seed:76": g * (box_N - R * N / 2),
        "LOG_seed:80": g**4 * L**4 / 2,
    }
    two_derivative = (
        -2 * (box_L - 3 * R * L / 8) - 8 * L * D + gradient / L
        -2 * N**2 / L - 4 * g * N + 2 * g**2 * L**2
    )
    total = sp.expand(two_derivative + lam * sum(
        coefficients[source_id] * body for source_id, body in source_bodies.items()
    ))
    # A(L) Box L = div(A grad L) - A'(L) (grad L)^2.
    boundary_L = total.coeff(box_L)
    boundary_N = total.coeff(box_N)
    integrated = total.subs({box_L: 0, box_N: 0}) - sp.diff(boundary_L, L) * gradient
    gauss_bonnet = riemann_squared - 4 * ricci_squared + R**2
    scalar_part = sp.expand(integrated + lam * gauss_bonnet / 4)
    F = scalar_part.coeff(R)
    K = scalar_part.coeff(gradient)
    V = scalar_part.subs({R: 0, gradient: 0})
    residuals = {}
    check_zero(residuals, "complete scalar restriction", scalar_part - F * R - K * gradient - V)
    return F, K, V, {"grad_L": boundary_L, "grad_N": boundary_N}, residuals


def form_derivative_collection():
    """FD3-FD7: retain H nonclosed and use the Bianchi identity only for G."""
    coefficients = action_coefficients()
    AG, AM, AH = sp.symbols("A_GG A_GH A_HH")
    JG, JM, JH = sp.symbols("J_GG J_GH J_HH")
    KG, KM, KH = sp.symbols("k_G_squared k_GH k_H_squared")
    A_TT = (AG - 4 * AM + 4 * AH) / 64
    J_TT = (JG - 4 * JM + 4 * JH) / 64
    k_TT = (KG - 4 * KM + 4 * KH) / 64
    source_bodies = {
        "Weyl_sigma_N:6": A_TT,
        "Weyl_sigma_N:7": J_TT - 3 * k_TT,
        "Weyl_sigma_N:8": -J_TT + k_TT,
    }
    log_bodies = {
        33: JG - KG / 2, 35: -JM, 37: JM - KM / 2, 39: JH,
        40: -AG - 5 * KG, 41: -AM - 5 * KM, 42: JG - KG / 2,
        43: -JM, 44: JM - KM / 2, 45: JH,
        52: JG - 3 * KG, 53: JM - 3 * KM, 54: JH - 3 * KH,
        55: AG, 56: AM, 57: AH, 58: -JM, 59: -JH,
    }
    source_bodies.update({f"LOG_seed:{index}": body for index, body in log_bodies.items()})
    terms = {key: coefficients[key] * body for key, body in source_bodies.items()}
    summed = sp.expand(sum(terms.values()))
    closed_G = sp.expand(summed.subs({AG: 2 * JG - 6 * KG, AM: 2 * JM - 6 * KM}))

    # These three blocks are the separately displayed analytic reductions of
    # Step 6.7 / FD8-FD10. Their individual source IDs are in the companion.
    algebraic = -sp.Rational(17, 3) * KG - sp.Rational(112, 3) * KH
    ordered_current = -8 * JM + 2 * KG - 22 * KM  # LOG_seed 287 and companions.
    remaining_currents = 4 * KG + 10 * KM       # LOG_seed 246 and companions.
    total = sp.expand(closed_G + algebraic + ordered_current + remaining_currents)
    residuals = {}
    check_zero(residuals, "form derivative and current cancellation", total - (-8 * JH + KG + 4 * KM - 8 * KH))
    return {"source_terms": terms, "derivative_sum": summed, "closed_G_sum": closed_G,
            "algebraic": algebraic, "ordered_current": ordered_current,
            "remaining_currents": remaining_currents, "total": total, "residuals": residuals}


def calculate():
    F, K, V, boundary, residuals = scalar_metric_restriction()
    # The Lovelock metric variation in Step 6.4 gives F0-lambda*k.
    # Scalar Taylor entries are differentiated here, before background insertion.
    raw = {
        "h_Einstein_h": -on_branch(F - lam * k) / 2,
        "ell_r": on_branch(sp.diff(F, L)),
        "gradient_ell_squared": on_branch(K),
        "ell_squared": on_branch((20 * k * sp.diff(F, L, 2) + sp.diff(V, L, 2)) / 2),
        "ell_n": on_branch(sp.diff(V, L, N)),
        "n_squared": on_branch(sp.diff(V, N, 2) / 2),
        "G_squared": on_branch(-L / 2 + lam * k),
        "H_squared": on_branch(4 * L - 8 * lam * k),
        "p_squared": on_branch(-2 / L - 2 * lam * g**2),
        "p_v": on_branch(-2 * sp.sqrt(2) * (1 + lam * g**2 * L)),
        "p_A": on_branch(-4 * g + 4 * lam * k * g),
        "vprime_squared": on_branch(2 * L + 2 * lam * g**2 * L**2),
    }
    ell, n = sp.symbols("ell n")
    scalar_potential = raw["ell_squared"] * ell**2 + raw["ell_n"] * ell * n + raw["n_squared"] * n**2
    auxiliary_equation = sp.diff(scalar_potential, n)
    auxiliary_solution = sp.solve(auxiliary_equation, n)[0]
    remaining_potential = sp.factor(scalar_potential.subs(n, auxiliary_solution))
    metric_shift = sp.solve(sp.Rational(3, 2) * c * sp.Symbol("beta") + raw["ell_r"], sp.Symbol("beta"))[0]
    diagonal_gradient = sp.factor(3 * c * metric_shift**2 + 4 * c * metric_shift / x + raw["gradient_ell_squared"])
    diagonal_potential = on_branch(-15 * c * k * metric_shift**2 - 20 * c * k * metric_shift / x + remaining_potential.coeff(ell, 2))
    scalar_mass_squared = sp.factor(diagonal_potential / diagonal_gradient)
    check_zero(residuals, "scalar mass from diagonal action", scalar_mass_squared - on_branch(4 * k))

    # Check reconstruction in the original scalar equation; Box is an operator label.
    box = sp.Symbol("Box")
    reconstructed_r = 8 * box / (3 * x) + 40 * k / (3 * x)
    scalar_equation = on_branch(c * reconstructed_r / x - 2 * c * box / x**2 + 8 * c * g**2)
    check_zero(residuals, "scalar reconstructed original equation", scalar_equation - 2 * c * (box - scalar_mass_squared) / (3 * x**2))
    G, H = sp.symbols("G H")
    connection_curl = sp.sqrt(2) * g * x * (2 * H - G)
    check_zero(residuals, "original three-form equation", 4 * g * H - sp.sqrt(2) * connection_curl / x - 2 * g * G)

    # Legendre elimination; substituting H=dQ in +4c H^2 alone has the wrong sign.
    Y, FQ = sp.symbols("Y F_Q")
    first_order_dual = raw["H_squared"] * Y**2 - 8 * c * Y * FQ
    dual_solution = sp.solve(sp.diff(first_order_dual, Y), Y)[0]
    dual_coefficient = sp.expand(first_order_dual.subs(Y, dual_solution)).coeff(FQ, 2)
    form_collection = form_derivative_collection()
    residuals.update(form_collection.pop("residuals"))
    return {
        "scope": "source-coefficient scalar restriction and documented analytic form/metric reductions; no unrestricted nonlinear EOM solver",
        "scalar_restriction": {"F": F, "K": K, "V": V, "boundary_current": boundary},
        "form_collection": form_collection,
        "raw_quadratic_coefficients": raw,
        "auxiliary_equation": auxiliary_equation,
        "auxiliary_solution_n": auxiliary_solution,
        "constraint_domain": "0<x<2, c!=0; do not use the solutions at x=2",
        "metric_shift_beta": metric_shift,
        "scalar_gradient_coefficient": diagonal_gradient,
        "scalar_potential_coefficient": diagonal_potential,
        "scalar_mass_squared": scalar_mass_squared,
        "connection_curl_Fv": connection_curl,
        "dual_vector_coefficient": dual_coefficient,
        "residuals": residuals,
    }


def main():
    result = calculate()
    write_json("bosonic_quadratic.json", result)
    print(f"Bosons: 12 raw coefficients, constraints and diagonal scalar/form blocks; {len(result['residuals'])} exact checks.")


if __name__ == "__main__":
    main()
