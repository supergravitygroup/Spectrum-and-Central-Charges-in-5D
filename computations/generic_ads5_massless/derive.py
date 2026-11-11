#!/usr/bin/env python3
"""Reproduce citation-map item 23 with free symbolic couplings.

Default: JSON on stdout. --write-results writes only outputs/results.json.
"""
import argparse
import hashlib
import json
from pathlib import Path

import sympy as s

from action_inputs import (
    L, N, N0, R, Ricci2, Riemann2, alpha, beta, c, couplings,
    curvature_blocks, E, factor, g, h, k, on_vacuum, r, v,
    vacuum_polynomial, vector_blocks, x, zeta,
)

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]


def derive():
    curvature = s.expand(sum(a*b for a, b in zip(couplings, curvature_blocks().values())))
    background = {R: 20*k, Ricci2: 80*k**2, Riemann2: 40*k**2}
    F = s.expand(curvature.subs(background))
    F_ads = factor(F.subs({k: -r, N: N0}))
    a_off = factor(-F_ads/(8*r))
    coefs = {
        "R": curvature.coeff(R, 1), "R2": curvature.coeff(R, 2),
        "Ricci2": curvature.coeff(Ricci2), "Riemann2": curvature.coeff(Riemann2),
    }
    # The Einstein coefficient of the massless TT factor in D=5.
    c_off = factor((coefs["R"] - 2*r*(20*coefs["R2"]
                    + 4*coefs["Ricci2"] - 2*coefs["Riemann2"])).subs(N, N0))
    density = s.expand(sum(a*b for a, b in zip(couplings, vector_blocks().values())))
    # The multiplier equation is E + 2*x*h/g = 0. This is a Bianchi identity,
    # not an auxiliary-field EOM or a two-derivative truncation of the theory.
    constrained = s.expand(density.subs(E, -2*x*h/g))
    K = (s.hessian(constrained, (c, v, h))/(2*x)).applyfunc(factor)
    K0 = K.subs(x, 0)
    # Derive the light block on the regular chart, then verify a division-free
    # congruence in checks.py, including its polynomial continuation.
    Zcv = (2*(K0[:2, :2] - K0[:2, 2:]*K0[2:, :2]/K0[2, 2])).applyfunc(on_vacuum)
    mixing = factor(Zcv[0, 1]/Zcv[0, 0])
    P = s.Matrix([[1, -mixing], [0, 1]])
    Zuv = (P.T*Zcv*P).applyfunc(factor)
    return {
        "background_density": F, "ads_density_before_Q": F_ads,
        "a_normalized_before_Q": a_off, "c_normalized_before_Q": c_off,
        "a_normalized": on_vacuum(a_off), "c_normalized": on_vacuum(c_off),
        "curvature_coefficients": coefs, "vector_K": K, "vector_K0": K0,
        "vector_Zcv": Zcv, "vector_Zuv": Zuv, "u_mixing": mixing,
        "form_pivot": on_vacuum(K0[2, 2]), "vacuum_polynomial": vacuum_polynomial,
    }


def encode(value):
    if isinstance(value, dict):
        return {key: encode(item) for key, item in value.items()}
    if isinstance(value, s.MatrixBase):
        return [[str(item) for item in row] for row in value.tolist()]
    return str(value)


def result_record():
    inputs = json.loads((HERE / "source_manifest.json").read_text())
    return {
        "claim": "Final-paper citation 23; draft_v109 eq:acgen and eq:uvgen",
        "method": "exact symbolic algebra; no numerical coupling samples",
        "normalization": "S=(1/(2*kappa5**2))*integral e*L; a,c in units pi**2*ell**3/kappa5**2",
        "domain": "real alpha,beta,zeta; g!=0; L0>0; Q=0; k=-ell**(-2)",
        "regular_pole_conditions": "(2-L0)*(4-3*L0+alpha*g**2*L0**2/2)*(alpha*g**2*L0**2+12*zeta*g**2*L0**2+2*L0-8)!=0",
        "degenerate_scope": "polynomial kinetic congruence remains valid; no complete degenerate-mode spectrum claimed",
        "source_sha256": inputs["current_inputs"],
        "producer_sha256": {name: hashlib.sha256((HERE/name).read_bytes()).hexdigest()
                            for name in ("action_inputs.py", "derive.py")},
        "results": encode(derive()),
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write-results", action="store_true")
    args = parser.parse_args()
    text = json.dumps(result_record(), indent=2, sort_keys=True) + "\n"
    if args.write_results:
        output = HERE / "outputs" / "results.json"
        output.parent.mkdir(exist_ok=True)
        output.write_text(text)
        print("Wrote computations/generic_ads5_massless/outputs/results.json")
    else:
        print(text, end="")


if __name__ == "__main__":
    main()
