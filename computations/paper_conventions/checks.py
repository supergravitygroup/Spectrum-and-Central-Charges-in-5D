#!/usr/bin/env python3
"""Exact, bounded checks for citation-map items 27 and 29.

Default execution is read-only. --write-log writes this package's reports.
The MS5 action projection is imported from the accepted item-23 source.
This does not rederive a full invariant or rerun the donor's audit suite.
"""
import argparse
import hashlib
import importlib.util
import itertools
import json
from pathlib import Path
import platform

import sympy as s

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_lock():
    record = json.loads((HERE / "source_manifest.json").read_text())
    for path, expected in record["current_inputs"].items():
        if digest(ROOT / path) != expected:
            raise AssertionError("Input changed; review the formula correspondence: " + path)
    for path, expected in record["implementation_hashes"].items():
        if digest(HERE / path) != expected:
            raise AssertionError("Implementation changed; review the scoped checks: " + path)
    return record["current_inputs"]


def run_checks():
    hashes = source_lock()
    records = []

    def zero(name, residual, group):
        residual = s.factor(s.cancel(residual))
        if residual != 0:
            raise AssertionError((name, residual))
        records.append(dict(name=name, group=group, method="exact", residual="0"))

    def negative(name, residual):
        residual = s.expand(residual)
        if residual == 0:
            raise AssertionError("Negative control did not detect error: " + name)
        records.append(dict(name=name, group="negative control", method="exact",
                            detected=True, nonzero_residual=str(residual)))

    # B(a,c,b)=bar(psi_a) gamma_c psi_b. The paper's contracted NW-SE
    # rank-one flip gives antisymmetry in a,b; every surviving B is free.
    def B(a, c, b, wrong_flip=False):
        if a == b:
            return s.S.Zero
        sign = 1 if wrong_flip or a < b else -1
        return sign * s.Symbol(f"B_{min(a,b)}_{c}_{max(a,b)}")

    def K(m, a, b, *, last=s.Rational(1, 4), wrong_flip=False):
        bil = lambda x, y, z: B(x, y, z, wrong_flip)
        return (bil(a, b, m) - bil(b, a, m))/4 + last*bil(a, m, b)

    for m, a, b in itertools.product(range(5), repeat=3):
        zero(f"metric compatibility K[{m},{a},{b}]", K(m,a,b)+K(m,b,a),
             "contorsion antisymmetry")
    for a, b, c in itertools.product(range(5), repeat=3):
        zero(f"R(P) fermion coefficient [{a},{b},{c}]",
             K(a,c,b)-K(b,c,a)-B(a,c,b)/2, "torsion constraint")
    negative("incorrect contracted rank-one flip breaks metric compatibility",
             K(0,1,2,wrong_flip=True)+K(0,2,1,wrong_flip=True))
    negative("omitted last contorsion term breaks R(P)=0",
             K(0,2,1,last=0)-K(1,2,0,last=0)-B(0,2,1)/2)

    # Import only the source definitions; no output-producing entry point.
    path = ROOT / "computations/generic_ads5_massless/action_inputs.py"
    spec = importlib.util.spec_from_file_location("paper_vacuum_inputs", path)
    inputs = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(inputs)
    L,N,k,g = inputs.L,inputs.N,inputs.k,inputs.g
    ms5 = {inputs.R:20*k, inputs.Ricci2:80*k**2, inputs.Riemann2:40*k**2}
    blocks = {name:s.expand(value.subs(ms5))
              for name,value in inputs.curvature_blocks().items()}
    F = sum(coefficient*block for coefficient,block in
            zip(inputs.couplings,blocks.values()))
    bps = {N:-3*g*L**2/2, k:-g**2*L**2/2}
    Dbar = -5*k/8+g*N/4+g**2*L**2/16
    W = blocks["weyl"]
    Q = (inputs.beta+6*inputs.zeta)*g**2*L**2-8*L+8
    zero("auxiliary D vanishes on the SUSY configuration",
         Dbar.subs(bps), "vacuum")
    zero("Weyl density equals 64 Dbar^2/3 on MS5",
         W-64*Dbar**2/3, "vacuum")
    zero("Weyl density vanishes for arbitrary positive L",
         W.subs(bps), "vacuum")
    for field in (L,N,k):
        zero("Weyl first derivative before BPS substitution: "+str(field),
             s.diff(W,field).subs(bps), "vacuum")
    zero("N equation = -g Q/2",
         s.diff(F,N).subs(bps)+g*Q/2, "vacuum")
    zero("L equation = g^2 L Q/2",
         s.diff(F,L).subs(bps)-g**2*L*Q/2, "vacuum")
    zero("metric trace = g^2 L^2 Q/2",
         (F/2-k*s.diff(F,k)/5).subs(bps)-g**2*L**2*Q/2, "vacuum")
    # The second derivative survives. Treating the invariant as identically
    # absent after its background value vanishes would miss this coefficient.
    zero("nonzero Weyl second derivative coefficient",
         s.diff(W,N,2)-8*g**2/3, "vacuum")
    negative("wrong SUSY coefficient N=-g L^2 is detected by dW/dN",
             s.diff(W,N).subs({N:-g*L**2,k:-g**2*L**2/2}))

    return dict(
        scope="Items 27/29 only: MS5 vacuum coefficients and fermion contorsion. No full spectrum or nonlinear SUSY proof.",
        command="python3 -B computations/paper_conventions/checks.py",
        working_directory="repository root",
        versions=dict(python=platform.python_version(), sympy=s.__version__),
        assumptions=["L>0, g!=0; real alpha,beta,zeta remain symbolic",
                     "Zero form strengths, constant scalars, maximally symmetric five-dimensional geometry",
                     "Differentiate the off-shell MS5 density before imposing N=-3gL^2/2, k=-g^2L^2/2",
                     "NW-SE contracted rank-one Majorana flip B(a,c,b)=-B(b,c,a)",
                     "Poincare gauge b_mu=0; no sampled field or coupling values"],
        source_hashes=hashes,
        results=dict(vacuum_polynomial=str(Q),
                     N_tadpole=str(-g*Q/2),
                     L_tadpole=str(g**2*L*Q/2),
                     metric_tadpole=str(g**2*L**2*Q/2),
                     Weyl_second_N_derivative=str(8*g**2/3)),
        checks=records,
        counts={group:sum(r["group"]==group for r in records)
                for group in ("contorsion antisymmetry","torsion constraint","vacuum","negative control")},
        status="PASS")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write-log", action="store_true")
    args = parser.parse_args()
    report = run_checks()
    lines = [
        "Items 27 and 29: exact symbolic checks",
        report["command"] + (" --write-log" if args.write_log else ""),
        "Python: "+report["versions"]["python"]+"; SymPy: "+report["versions"]["sympy"],
        "No field or coupling samples; no small-coupling expansion.",
        *(f"PASS {group}: {count}" for group,count in report["counts"].items()),
        f"PASS input fingerprints: {len(report['source_hashes'])}",
        "PASS total: "+str(len(report["checks"]))+" exact checks.",
        "The donor's 241-check summary was not rerun by this command.",
    ]
    text = "\n".join(lines)+"\n"
    if args.write_log:
        out = HERE/"outputs"
        out.mkdir(exist_ok=True)
        (out/"verification.json").write_text(json.dumps(report,indent=2)+"\n")
        (out/"verification.log").write_text(text)
    print(text,end="")


if __name__ == "__main__":
    main()
