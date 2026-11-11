"""Raw fermion coefficients, field shift, signed equations and reconstruction.

Sources: FC13-FC15; Step 7 (7.11)-(7.13); Step 10 (10.6)-(10.10);
Step 11 (11.9)-(11.15). The Clifford factors are independently checked in
checks.reference_reduction and the unprojected component operator stage.
"""

import sympy as sp

from inputs.symbols import g, x, c, k, m, lam, on_branch
from inputs.fermionic_coefficients import two_derivative_terms, gauss_bonnet_terms
from src.reporting import check_zero, write_json


def calculate():
    two_derivative = two_derivative_terms()
    higher_derivative = gauss_bonnet_terms()
    total = {term: two_derivative[term] + lam * higher_derivative[term] for term in two_derivative}
    raw = {term: on_branch(value) for term, value in total.items()}
    residuals = {}

    # We divide by c only for the interior reduction. Endpoint testing below
    # evaluates the original raw coefficients before any such division.
    normalized = {term: sp.cancel(value / c) for term, value in raw.items()}
    beta = sp.Symbol("beta")
    derivative_J = -normalized["derivative_mixing_delta"]  # delta pairing = -bar A J B.
    shift = sp.solve(-6 * beta + derivative_J, beta)[0]
    check_zero(residuals, "derivative mixing removed", -6 * shift + derivative_J)
    check_zero(residuals, "algebraic mixing removed", -24 * sp.I * m * shift + normalized["algebraic_mixing"])

    spinor_gradient = sp.factor(c * (
        -12 * shift**2 + 4 * derivative_J * shift + normalized["spinor_kinetic"]
    ))
    spinor_mass_J = sp.factor(c * (
        60 * sp.I * m * shift**2
        -5 * normalized["algebraic_mixing"] * shift
        -normalized["spinor_mass_delta"]
    ))
    spinor_parameter = sp.factor(spinor_mass_J / (sp.I * spinor_gradient))
    # gamma^{ab} Upsilon_b=-Upsilon^a on the gamma-traceless representative.
    gravitino_parameter = sp.factor(raw["gravitino_mass_delta"] / (sp.I * raw["gravitino_kinetic"]))
    check_zero(residuals, "spinor signed operator parameter", spinor_parameter - m)
    check_zero(residuals, "gravitino gauge parameter", gravitino_parameter - 3 * m)

    # Reconstruct both original equations (7.13), not just a determinant root.
    reconstruction = {
        "derivative gamma trace": 3 * shift - sp.I * sp.sqrt(2) / x,
        "algebraic gamma trace": 12 * sp.I * m * shift + 2 * g,
        "spinor derivative": 4 * sp.I * sp.sqrt(2) * shift / x + 2 / (3 * x**2) + 2 / x**2,
        "spinor mass": 10 * g * shift + 2 * sp.I * m / (3 * x**2) - 7 * sp.I * g / (sp.sqrt(2) * x),
        "Noether identity": on_branch(-3 * k - 12 * m**2),
        "residual gauge divergence": on_branch(25 * m**2 + 5 * k - 5 * m**2),
    }
    for name, expression in reconstruction.items():
        check_zero(residuals, name, expression)
    for term, expression in raw.items():
        check_zero(residuals, f"endpoint: {term}", expression.subs(x, 2))

    return {
        "scope": "coefficient reduction of the documented full quadratic block; local bulk; 0<x<2 for elimination",
        "two_derivative_coefficients": two_derivative,
        "GB_coefficients_before_lambda": higher_derivative,
        "raw_quadratic_coefficients": raw,
        "shift_Psi_equals_Upsilon_plus_beta_gamma_J_zeta": shift,
        "diagonal_gravitino_gradient": raw["gravitino_kinetic"],
        "diagonal_spinor_gradient": spinor_gradient,
        "diagonal_spinor_mass_J": spinor_mass_J,
        "signed_gravitino_parameters": {"s=+1": gravitino_parameter, "s=-1": -gravitino_parameter},
        "signed_spinor_parameters": {"s=+1": spinor_parameter, "s=-1": -spinor_parameter},
        "constraints": "gamma.Upsilon=0 by local gauge; divergence.Upsilon=0 follows from its equation",
        "residual_gauge": "(slash_nabla+5*i*m*J) epsilon=0",
        "reality": "s=+1 and s=-1 are paired by symplectic Majorana reality, not extra doublets",
        "residuals": residuals,
    }


def main():
    result = calculate()
    write_json("fermionic_reduction.json", result)
    print(f"Fermions: six raw coefficients and diagonal operators; {len(result['residuals'])} exact checks.")


if __name__ == "__main__":
    main()
