"""Compare the derived spectrum with short AdS multiplets only at the end.

Source: derivations/spectrum/REPRESENTATION_CHECK.md, R1-R15.
Representation compatibility is distinct from nonlinear SUSY closure.
"""

import sympy as sp

from inputs.symbols import x, g, c, k, on_branch
from calculations.spectrum import calculate as calculate_spectrum
from calculations.fermionic_reduction import calculate as calculate_fermions
from src.reporting import check_zero, write_json


def calculate():
    spectrum = calculate_spectrum()
    fermions = calculate_fermions()
    residuals = {}
    radius_squared = -1 / on_branch(k)
    spinor_energy = 2 + sp.sqrt(sp.factor(fermions["signed_spinor_parameters"]["s=+1"]**2 * radius_squared))
    gravitino_energy = 2 + sp.sqrt(sp.factor(fermions["signed_gravitino_parameters"]["s=+1"]**2 * radius_squared))
    check_zero(residuals, "spinor energy from calculated mass", spinor_energy - sp.Rational(5, 2))
    check_zero(residuals, "gravitino energy from calculated gauge mass", gravitino_energy - sp.Rational(7, 2))
    for energy, left_spin, right_spin in [(2, 0, 0), (3, 1, 1)]:
        check_zero(residuals, f"left shortening at E={energy}", energy - (2 + left_spin))
        check_zero(residuals, f"right shortening at E={energy}", energy - (2 + right_spin))

    G, H, F_matter, F_gravity = sp.symbols("G H F_matter F_gravity")
    T = G / 8 - H / 4
    shift = fermions["shift_Psi_equals_Upsilon_plus_beta_gamma_J_zeta"]
    check_zero(residuals, "matter spinor flux selects A+4Q", -T + 3 * (G / 4 - T) - (G + 4 * H) / 4)
    check_zero(residuals, "shift flux coefficient", shift * x / sp.sqrt(2) - sp.I / 3)
    check_zero(residuals, "gravitino rank-three flux selects A-2Q", 2 * sp.I * T - sp.I * (G - 2 * H) / 4)
    check_zero(residuals, "gravitino remaining gamma flux", -sp.I * G / 4 + sp.I * (G / 4 + H) / 3 + sp.I * (G - 2 * H) / 6)
    rotated = sp.expand(-c * ((F_matter + 2 * F_gravity) / 3)**2 / 2 - 4 * c * ((F_matter - F_gravity) / 6)**2)
    check_zero(residuals, "vector rotation removes mixed kinetic term", rotated.coeff(F_matter * F_gravity))
    check_zero(residuals, "R connection selects gravity vector", sp.sqrt(2) * g * x * (2 * (F_matter - F_gravity) / 6 - (F_matter + 2 * F_gravity) / 3) + sp.sqrt(2) * g * x * F_gravity)
    return {
        "status": "REPRESENTATION_COMPATIBILITY_ONLY",
        "source_spectrum_counts": {"bosons": spectrum["bosonic_dof"], "fermions": spectrum["fermionic_dof"]},
        "energies": {"scalar": 2, "vectors": 3, "graviton": 4, "spinor": spinor_energy, "gravitino": gravitino_energy},
        "multiplets": {"gravity": "A1 Abar1 [1;1]_3^(0), 8+8", "vector": "A2 Abar2 [0;0]_2^(0), 4+4"},
        "vector_assignments": {"gravity": "A-2Q", "matter": "A+4Q"},
        "vector_kinetic_weights": {"matter": -4 * rotated.coeff(F_matter, 2), "gravity": -4 * rotated.coeff(F_gravity, 2)},
        "domain": "0<x<2; positive-energy representation comparison; global boundary conditions and full SUSY intertwining not certified",
        "residuals": residuals,
    }


def main():
    write_json("representations.json", calculate())
    print("Representation comparison: gravity 8+8 and vector 4+4; closure not inferred.")


if __name__ == "__main__":
    main()
