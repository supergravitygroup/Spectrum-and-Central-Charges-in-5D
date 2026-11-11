#!/usr/bin/env python3
"""Exact checks of four supplied algebraic identities; no parameter sampling.

This module uses the displayed formulas directly, construct a
new action, or derive a Hessian. The inputs are the displayed formulas cited in
each check. All free couplings, curvature monomials and tensor entries remain
symbolic. The only numerical SU(2) entries define epsilon_12 = epsilon^12 = 1.
Output is JSON on stdout; no files are written.
"""
import json
import sys

import sympy as sp


def require_zero(expression):
    residual = sp.factor(sp.cancel(expression))
    if residual != 0:
        raise AssertionError(f"Nonzero symbolic residual: {residual}")
    return "0"


def weyl_vector_determinant():
    alpha, g, t = sp.symbols("alpha g t")
    a0 = 1 - alpha * g**2 / 6
    nu2 = g**2 / 2 - 3 / alpha
    matrix = sp.Matrix([
        [-2 * a0 + (alpha / 3 - 2 / g**2) * t, 2 * t / g**2,
         -sp.sqrt(2) * a0 / g],
        [2 * t / g**2, 3 - 2 * t / g**2, sp.sqrt(2) / g],
        [-sp.sqrt(2) * a0 / g, sp.sqrt(2) / g, alpha / 3],
    ])
    stated = -2 * alpha**2 / (9 * g**2) * (
        (t - nu2)**2 - 2 * g**2 * nu2
    )
    return {
        "name": "weyl_vector_displayed_determinant",
        "source": "weyl2/ads5/details/physical_operators.md",
        "residual": require_zero(matrix.det() - stated),
        "conditions": ["g != 0", "alpha != 0 for the stated nu^2 form"],
        "scope": "Determinant of the displayed 3 by 3 matrix, before multiplying by t^2.",
        "exclusions": "Does not derive the matrix or the t^2 constraint factor from the action.",
    }



def triplet_lowering():
    # The two triplets have fully independent symbolic entries.
    l11, l12, l22, v11, v12, v22 = sp.symbols("L11 L12 L22 V11 V12 V22")
    epsilon = sp.Matrix([[0, 1], [-1, 0]])
    lower_l = sp.Matrix([[l11, l12], [l12, l22]])
    lower_v = sp.Matrix([[v11, v12], [v12, v22]])
    upper_l = epsilon * lower_l * epsilon.T
    upper_mixed_v = epsilon * lower_v
    lower_mixed_v = lower_v * epsilon.T
    upper_connection = upper_mixed_v * upper_l + upper_l * upper_mixed_v.T
    lowered_connection = epsilon.T * upper_connection * epsilon
    stated = -(lower_mixed_v * lower_l + lower_l * lower_mixed_v.T)
    residuals = [require_zero(entry) for entry in lowered_connection - stated]
    return {
        "name": "nw_se_triplet_connection_lowering",
        "source": "common/two_derivative_action/details/construction.md, equation (4.27a)",
        "convention_source": "CONVENTIONS.md: NW-SE raising and lowering",
        "component_residuals": residuals,
        "conditions": ["L_ij and V_ij are symmetric SU(2) triplets"],
        "scope": "epsilon_ki epsilon_lj (2 V^(k)_m L^(l)m) = -2 V_(i)^k L_(j)k.",
        "exclusions": "Does not assign field values or impose the compensator gauge.",
    }


def gauss_bonnet_curvature_coefficients():
    riem2, ricci2, scalar2, coupling, coupling_gb = sp.symbols(
        "Riemann_squared Ricci_squared R_squared lambda lambda_GB"
    )
    # These are formal curvature monomials, not a field truncation.
    c2 = riem2 - sp.Rational(4, 3) * ricci2 + scalar2 / 6
    weyl = c2 / 8 + scalar2 / 48
    log = -ricci2 / 6 + scalar2 / 24
    gb = riem2 - 4 * ricci2 + scalar2
    basis_residual = require_zero(weyl + 2 * log - gb / 8)
    spectrum_residual = require_zero(-2 * weyl - 4 * log + gb / 4)
    # lambda = -2 lambda_GB is the stated symbolic coefficient map.
    map_residual = require_zero(
        (coupling * gb / 8).subs(coupling, -2 * coupling_gb) + coupling_gb * gb / 4
    )
    return {
        "name": "gauss_bonnet_curvature_coefficient_map",
        "source": "common/details/action_normalizations.md; gauss_bonnet/ads5/action_inputs.md",
        "residuals": [basis_residual, spectrum_residual, map_residual],
        "conditions": ["D = 5", "The cited curvature monomials and density definitions"],
        "scope": "ell_W + 2 ell_LOG has GB/8; -2 ell_W -4 ell_LOG has -GB/4.",
        "coupling_map": "lambda = -2 lambda_GB",
        "exclusions": "Pure-curvature matching does not establish complete fermionic action equivalence.",
    }


def gauss_bonnet_fermion_coefficients():
    g, x = sp.symbols("g x")
    return {
        "name": "gauss_bonnet_F25_spinor_coefficients",
        "source": "gauss_bonnet/ads5/code/derivations/support/gb-splus-fermionic-expansion-EXPLAIN.md, F25 coefficient check",
        "residuals": [
            require_zero(sp.Rational(512, 3) * (g**2 / 64) - 8 * g**2 / 3),
            require_zero(
                (256 * sp.I * g * x / (3 * sp.sqrt(2))) * (g**2 / 64)
                - 4 * sp.I * g**3 * x / (3 * sp.sqrt(2))
            ),
        ],
        "conditions": [],
        "scope": "Two coefficient products in the displayed F25 reduction, with g and x symbolic.",
        "exclusions": "Does not perform a field truncation or establish the other quadratic-action entries.",
    }


def main():
    try:
        checks = [
            weyl_vector_determinant(),
            triplet_lowering(),
            gauss_bonnet_curvature_coefficients(),
            gauss_bonnet_fermion_coefficients(),
        ]
    except AssertionError as error:
        print(json.dumps({"status": "FAIL", "error": str(error)}, indent=2))
        return 1
    print(json.dumps({
        "status": "PASS_SCOPED_SYMBOLIC",
        "arithmetic": "Exact SymPy algebra; no free-parameter or field specialization",
        "sympy_version": sp.__version__,
        "checks": checks,
        "scope": "Four supplied algebraic identities; not a full action, Hessian, SUSY or spectrum verification.",
    }, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
