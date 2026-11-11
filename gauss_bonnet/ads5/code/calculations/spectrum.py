"""Assemble the spectrum from the calculated diagonal blocks, not multiplets."""

import sympy as sp

from inputs.symbols import g, k, x, a, c, m, on_branch
from calculations.bosonic_quadratic import calculate as bosonic_calculation
from calculations.fermionic_reduction import calculate as fermionic_calculation
from src.reporting import OUTPUTS, check_zero, write_json


def calculate():
    bosons = bosonic_calculation()
    fermions = fermionic_calculation()
    raw_bosons = bosons["raw_quadratic_coefficients"]
    radius_squared = -1 / on_branch(k)
    weights = {
        "graviton": -2 * raw_bosons["h_Einstein_h"],
        "scalar": -2 * bosons["scalar_gradient_coefficient"],
        "vector_A": -4 * raw_bosons["G_squared"],
        "vector_Q": -4 * bosons["dual_vector_coefficient"],
        "gravitino": -fermions["diagonal_gravitino_gradient"],
        "spinor": -fermions["diagonal_spinor_gradient"],
    }
    residuals = {}
    positive_parameter = sp.Symbol("t", positive=True)
    positivity = {}
    for mode, weight in weights.items():
        positive_form = sp.factor(weight.subs(x, 2 * positive_parameter / (1 + positive_parameter)))
        if positive_form.is_positive is not True:
            raise AssertionError((mode, positive_form))
        positivity[mode] = positive_form
        check_zero(residuals, f"zero kinetic weight at endpoint: {mode}", weight.subs(x, 2))

    scalar_mass_radius = sp.factor(bosons["scalar_mass_squared"] * radius_squared)
    spinor_parameter = fermions["signed_spinor_parameters"]["s=+1"]
    gravitino_parameter = fermions["signed_gravitino_parameters"]["s=+1"]
    check_zero(residuals, "scalar BF saturation", scalar_mass_radius + 4)
    check_zero(residuals, "spinor AdS magnitude squared", spinor_parameter**2 * radius_squared - sp.Rational(1, 4))
    check_zero(residuals, "gravitino AdS gauge magnitude squared", gravitino_parameter**2 * radius_squared - sp.Rational(9, 4))

    dimension = 5
    little_group_spinor_complex_dimension = 2
    dof = {
        "graviton": dimension * (dimension - 3) // 2,
        "scalar": 1,
        "vector_A": dimension - 2,
        "vector_Q": int(sp.binomial(dimension - 2, 2)),
        "gravitino": 2 * ((dimension - 2) * little_group_spinor_complex_dimension - little_group_spinor_complex_dimension),
        "spinor": 2 * little_group_spinor_complex_dimension,
    }
    scalar_exponent = sp.Symbol("Delta")
    scalar_indicial = sp.factor(scalar_exponent * (scalar_exponent - 4) - scalar_mass_radius)
    branch_x = 2 / (1 + sp.sqrt(1 + 2 * a))
    small_coupling = sp.series(branch_x, a, 0, 3)
    rows = [
        ("graviton", "2", "(Box-2k)H=0; massless", "h=H; ell=n=0"),
        ("scalar", "0", "(Box-4k)ell=0; M^2 L_AdS^2=-4", "h=-2*gbar*ell/(3x); n=-2gx*ell"),
        ("vector_A", "1", "Maxwell; physical mass 0", "H2=0; v=-sqrt(2)gx*A"),
        ("vector_Q", "1 (dual two-form)", "Maxwell; physical mass 0", "H2=dQ; db=2 star(dQ); v=2sqrt(2)gx*Q"),
        ("gravitino", "3/2", "(slash_nabla+3imJ)Upsilon=0; gauge massless", "Psi=Upsilon; zeta=0; gamma.Upsilon=div.Upsilon=0"),
        ("spinor", "1/2", "(slash_nabla+imJ)zeta=0", "Psi=i*sqrt(2)*gamma*J*zeta/(3x); Upsilon=0"),
    ]
    spectrum = [
        {"mode": mode, "spin": spin, "equation": equation, "reconstruction": reconstruction,
         "kinetic_weight": sp.factor(weights[mode]), "real_dof": dof[mode]}
        for mode, spin, equation, reconstruction in rows
    ]
    # The fixed-lambda ungauged limit follows a=lambda*g^2, not fixed a.
    fixed_lambda = sp.Symbol("fixed_lambda", real=True)
    x_in_limit = branch_x.subs(a, fixed_lambda * g**2)
    limits = {"x": sp.limit(x_in_limit, g, 0), "curvature": sp.limit(-g**2 * x_in_limit**2 / 2, g, 0),
              "fermion_parameter": sp.limit(g * x_in_limit / (2 * sp.sqrt(2)), g, 0)}
    return {
        "branch": "GB-S+", "domain": "a>-1/2, 0<x<2, real g!=0; local bulk",
        "spectrum": spectrum,
        "bosonic_dof": sum(dof[name] for name in ["graviton", "scalar", "vector_A", "vector_Q"]),
        "fermionic_dof": dof["gravitino"] + dof["spinor"],
        "positivity_proof_x_equals_2t_over_1_plus_t": positivity,
        "scalar_indicial_equation": scalar_indicial,
        "scalar_falloffs": "z^2 and z^2 log(z); no second bulk scalar",
        "small_a_expansion": small_coupling,
        "fixed_lambda_ungauged_limit": limits,
        "endpoint": "a=-1/2: x=2, every raw quadratic coefficient vanishes; generic constraints and DoF count not assigned",
        "boundary_scope": "global boundary data, global frequencies, topology and renormalized boundary norms are not selected",
        "residuals": residuals,
    }


def main():
    result = calculate()
    write_json("spectrum.json", result)
    lines = ["# GB-S+ local spectrum", "", result["domain"], "",
             "| Mode | Spin | Local equation | Kinetic weight | Real DoF | Reconstruction |",
             "|---|---|---|---|---:|---|"]
    for row in result["spectrum"]:
        lines.append(f"| {row['mode']} | {row['spin']} | {row['equation']} | $`{sp.latex(row['kinetic_weight'])}`$ | {row['real_dof']} | {row['reconstruction']} |")
    lines.extend(["", "Bosons: 12. Fermions: 12.", "", result["endpoint"], "", result["boundary_scope"], "",
                  "Detailed equations, gauge quotients, signed roots and norms: [calculation notes](../../spectrum.md).", ""])
    (OUTPUTS / "spectrum.md").write_text("\n".join(lines), encoding="utf-8")
    print("Spectrum: 12 bosonic + 12 fermionic local degrees of freedom; endpoint recorded separately.")


if __name__ == "__main__":
    main()
