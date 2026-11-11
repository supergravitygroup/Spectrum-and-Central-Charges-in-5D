"""Reuse the explicit gauge-preserving Killing-spinor check E16-E22.

Existence, not just integrability: the accepted real rank-eight Killing
connection is flat, so parallel transport on a simply connected local patch
extends arbitrary initial real spinor data. No global quotient is selected.
"""

import sympy as sp

from inputs.symbols import L, N, k, g, x, m, on_branch
from src.reporting import check_zero, write_json


def calculate():
    residuals = {}
    delta_compensator = on_branch(N / 2 + 3 * g * L**2 / 4)
    killing_curvature = on_branch(k / 2 + 2 * m**2)
    composite_D = on_branch(-20 * k / 32 + g * N / 4 + g**2 * L**2 / 16)
    check_zero(residuals, "independent compensator variation E18", delta_compensator)
    check_zero(residuals, "Killing connection curvature E19-E21", killing_curvature)
    check_zero(residuals, "dependent chi variation E22", composite_D / 4)
    J = sp.Matrix([[0, -1], [1, 0]])
    if J**2 != -sp.eye(2):
        raise AssertionError("Wrong NW-SE doublet generator")
    return {
        "status": "FULL_LOCAL_KINEMATIC_SUPERSYMMETRY_IN_ACCEPTED_TRANSFORMATION_SYSTEM",
        "theory_real_parameters": 8,
        "local_preserved_parameters": 8,
        "S_compensator": "eta=-m J epsilon",
        "Killing_equation": "(nabla_mu+i*m*gamma_mu*J)epsilon=0",
        "differential_existence": "Flat real rank-eight connection; parallel transport is path independent on a simply connected local patch, with arbitrary initial spinor data.",
        "domain": "GB-S+, g!=0, 0<x<=2; kinematic statement also at x=2",
        "qualification": "Does not certify nonlinear invariance of inherited action, complete multiplet closure or global boundary solutions.",
        "source": "derivations/support/gb-splus-spectrum-method-EXPLAIN.md, E16-E22",
        "residuals": residuals,
    }


def main():
    write_json("supersymmetry.json", calculate())
    print("Supersymmetry: inherited local Killing problem admits 8/8 real solutions; global data not selected.")


if __name__ == "__main__":
    main()
