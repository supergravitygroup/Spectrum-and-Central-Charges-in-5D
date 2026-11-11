#!/usr/bin/env python3
"""Exact checks for item 23. Default is read-only; --write-log updates its log."""
import argparse
import hashlib
import json
from pathlib import Path
import runpy
import sys

import sympy as s

from action_inputs import (
    L, N, N0, R, Ricci2, Riemann2, alpha, beta, block_names, c,
    couplings, curvature_blocks, E, expanded_vector_blocks, factor, g, h, k,
    multiplier, on_vacuum, r, v, vacuum_polynomial, vector_blocks, x, zeta,
)
from derive import HERE, ROOT, derive, result_record


def run_checks():
    lines = [
        "Item 23: exact symbolic verification",
        "Command: python3 -B computations/generic_ads5_massless/checks.py --write-log",
        "Working directory: repository root",
        f"Python: {sys.version.split()[0]}; SymPy: {s.__version__}",
        "Parameters: real alpha,beta,zeta; g!=0; L0>0; no numerical samples.",
        "Q=0 is imposed algebraically; named single-invariant limits are separate checks.",
    ]
    count = 0

    def check(name, residual):
        nonlocal count
        entries = list(residual) if isinstance(residual, s.MatrixBase) else [residual]
        reduced = [factor(item) for item in entries]
        if any(item != 0 for item in reduced):
            raise AssertionError(f"{name}: residuals {reduced}")
        count += 1
        lines.append(f"PASS {name}: exact zero ({len(entries)} component(s))")

    manifest = json.loads((HERE / "source_manifest.json").read_text())
    for name, expected in manifest["current_inputs"].items():
        actual = hashlib.sha256((ROOT/name).read_bytes()).hexdigest()
        if actual != expected:
            raise AssertionError(f"Source changed: {name}; re-audit its term mapping.")
    lines.append(f"PASS source lock: {len(manifest['current_inputs'])} current input files")

    data = derive()
    old = runpy.run_path(str(HERE / "background_blocks.py"))
    translation = {old["L"]: L, old["N"]: N, old["k"]: k, old["g"]: g}
    ms5 = {R: 20*k, Ricci2: 80*k**2, Riemann2: 40*k**2}
    for name, block, existing in zip(block_names, curvature_blocks().values(), old["blocks"]):
        check(f"background/{name}", block.subs(ms5) - existing.subs(translation, simultaneous=True))

    F = data["background_density"]
    subs = {N: N0, k: -r}
    # Differentiate before restricting to the supersymmetric configuration.
    check("background/N tadpole", s.diff(F, N).subs(subs) + g*vacuum_polynomial/2)
    check("background/L tadpole", s.diff(F, L).subs(subs) - g**2*L*vacuum_polynomial/2)
    check("background/metric tadpole", (F/2-k*s.diff(F, k)/5).subs(subs)
          - g**2*L**2*vacuum_polynomial/2)
    curvature = data["curvature_coefficients"]
    check("curvature/Riemann2", curvature["Riemann2"] - alpha/8)
    check("curvature/Ricci2", curvature["Ricci2"] + (alpha+beta)/6)
    check("curvature/R2", curvature["R2"] - (alpha+beta)/24 - zeta/4)
    C0 = 4 - 3*L + alpha*g**2*L**2/2
    B0 = 2 - L
    Delta = alpha*g**2*L**2 + 12*zeta*g**2*L**2 + 2*L - 8
    check("eq:acgen/a", data["a_normalized"] - (4-3*L))
    check("eq:acgen/c", data["c_normalized"] - C0)
    check("central charges/c-a", data["c_normalized"]-data["a_normalized"]-alpha*r)

    direct, alternate = vector_blocks(), expanded_vector_blocks()
    constraint = {E: -2*x*h/g}
    for name in block_names:
        check(f"vector source representatives/{name}", (direct[name]-alternate[name]).subs(constraint))
    # Non-cyclic vs cyclic LOG H derivatives: do not drop its source E^2 term.
    check("LOG Bianchi completion", direct["log"]-alternate["log"]
          - (g**2*E**2-4*x**2*h**2)/3)

    # Keep the form constraint by a multiplier, using the alternate action.
    S5 = s.expand(sum(a*b for a, b in zip(couplings, alternate.values()))
                  + multiplier*(E+2*x*h/g))
    check("multiplier/Bianchi equation", s.diff(S5, multiplier) - E - 2*x*h/g)
    M = (s.hessian(S5, (c, v, E, multiplier, h))/2).applyfunc(on_vacuum)
    A, B, H = M[:2, :2], M[:2, 2:], M[2:, 2:]
    light5 = (A-B*H.inv()*B.T).applyfunc(factor)
    K = data["vector_K"]
    light3 = K[:2, :2] - K[:2, 2:]*K[2:, :2]/K[2, 2]
    check("vector/two routes at symbolic x", (light5/x-light3).applyfunc(on_vacuum))
    leading5 = light5.applyfunc(lambda a: factor(a/x).subs(x, 0))
    check("vector/exact massless coefficient", 2*leading5-data["vector_Zcv"])
    # M is half the Hessian, so x*M_light^{-1}=2*Z^{-1} at the pole.
    check("vector/pole inverse normalization", leading5.inv()-2*data["vector_Zcv"].inv())

    # This identity has denominators only in g and L, not in B0, C0 or Delta.
    # It therefore also records the polynomial coefficients at degeneracies.
    q = s.sqrt(2)/(3*g*L)
    T = s.Matrix([[1, -q, 0], [0, 1, 0], [s.S.Half, s.sqrt(2)/(12*g*L), 1]])
    diagonal = s.diag(3*B0, C0/(3*g**2*L**2), 4*Delta/3)
    check("vector/undivided congruence", (T.T*data["vector_K0"]*T-diagonal).applyfunc(on_vacuum))
    check("vector/congruence invertible", T.det()-1)
    check("eq:uvgen/mixing", data["u_mixing"]-q)
    check("eq:uvgen/kinetic matrix", data["vector_Zuv"]-s.diag(6*B0, 2*C0/(3*g**2*L**2)))

    # Named theory limits: remaining couplings and g stay symbolic.
    aoff, coff = data["a_normalized_before_Q"], data["c_normalized_before_Q"]
    for name, sub, expected_a, expected_c in (
        ("Einstein", {alpha: 0, beta: 0, zeta: 0, L: 1}, 1, 1),
        ("Weyl", {beta: 0, zeta: 0, L: 1}, 1, 1+alpha*g**2/2),
        ("LOG", {alpha: 0, zeta: 0, beta: 8*(L-1)/(g**2*L**2)}, 4-3*L, 4-3*L),
        ("R2", {alpha: 0, beta: 0, zeta: 4*(L-1)/(3*g**2*L**2)}, 4-3*L, 4-3*L),
        ("common GB", {alpha: 4*(L-1)/(g**2*L**2), beta: 8*(L-1)/(g**2*L**2), zeta: 0}, 4-3*L, 2-L),
    ):
        check(f"limits/{name}/a,c", s.Matrix([aoff.subs(sub, simultaneous=True)-expected_a,
                                              coff.subs(sub, simultaneous=True)-expected_c]))
        # Derive the vector reduction from its unrestricted K0 in this theory,
        # rather than merely substituting in the already-diagonal answer.
        Kcase = data["vector_K0"].subs(sub, simultaneous=True)
        Tcase = T.subs(sub, simultaneous=True)
        caseL = sub.get(L, L)
        expected = s.diag(3*(2-caseL), expected_c/(3*g**2*caseL**2),
                          data["vector_K0"][2, 2].subs(sub, simultaneous=True))
        check(f"limits/{name}/vectors", Tcase.T*Kcase*Tcase-expected)

    stored = json.loads((HERE / "outputs/results.json").read_text())
    if stored != result_record():
        raise AssertionError("Stored results differ; rerun derive.py --write-results.")
    lines += [
        "PASS stored results: exact match to fresh derivation and producer hashes",
        f"PASS: {count} exact algebraic checks, source lock and output reproduction.",
        "Regular pole interpretation: B0*C0*Delta != 0. Undivided congruence covers their zeros.",
        "Scope: eq:acgen, eq:uvgen; no full generic spectrum or degenerate-mode classification.",
    ]
    return "\n".join(lines) + "\n"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write-log", action="store_true")
    args = parser.parse_args()
    result = run_checks()  # A failed check raises before any success log is written.
    if args.write_log:
        (HERE / "outputs/verification.log").write_text(result)
    print(result, end="")


if __name__ == "__main__":
    main()
