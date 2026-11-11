#!/usr/bin/env python3
"""Exact R2 AdS5 checks for the final paper; default execution is read-only."""
import argparse
import hashlib
import json
from pathlib import Path
import platform

import sympy as s

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]


def reduced(expr):
    return s.factor(s.cancel(expr))


def matrix_record(matrix):
    return [[str(reduced(x)) for x in matrix.row(i)] for i in range(matrix.rows)]


def source_check():
    manifest = json.loads((HERE / "source_manifest.json").read_text())
    for base, key in ((ROOT, "repository_inputs"), (HERE, "implementation_hashes")):
        for name, expected in manifest[key].items():
            if hashlib.sha256((base / name).read_bytes()).hexdigest() != expected:
                raise AssertionError(("source fingerprint changed", name))
    return {key: len(manifest[key]) for key in ("repository_inputs", "implementation_hashes")}


def calculate():
    L, g, nu, mu, y, t = s.symbols("L g nu mu y t", nonzero=True, real=True)
    lam = 4*(L-1)/(3*g**2*L**2)
    A, B = 4-3*L, 2-L
    ell2, m = 2/(g**2*L**2), g*L/(2*s.sqrt(2))
    nu2 = (4-L)/(2*(L-1))
    records = []

    def check(name, expression):
        entries = list(expression) if isinstance(expression, s.MatrixBase) else [expression]
        residuals = [reduced(x) for x in entries]
        if any(x != 0 for x in residuals):
            raise AssertionError((name, residuals))
        records.append(dict(name=name, components=len(entries), residuals=[str(x) for x in residuals]))

    def claim(name, condition, evidence):
        if not condition:
            raise AssertionError((name, evidence))
        records.append(dict(name=name, evidence=evidence, status="PASS"))

    # eq:R2vec: first-order form constraint, then algebraic elimination.
    # For transverse vectors, (dX).(dY) = -2 t X.Y modulo a boundary term.
    c, v, E, u, w, z, Enew, chat = s.symbols("c v E u w z Enew chat")
    W = s.sqrt(2)*v+2*E/L
    J = 6*lam*g*L*W+9*lam*g**2*L**2*c-u/g
    parent = (A*t*c**2 + lam*t*W**2/2 + 3*lam*g*L*t*W*c
              + s.Rational(9, 2)*lam*g**2*L**2*t*c**2 + t*J**2/(8*A)
              - 2*(1/L+3*lam*g**2)*E**2 - 2*s.sqrt(2)*E*v-4*g*E*c+u*E)
    # w=W and z=J are independent; E is then algebraic.
    reexpressed = s.expand(parent.subs({v: (w-2*E/L)/s.sqrt(2),
                                      u: g*(6*lam*g*L*w+9*lam*g**2*L**2*c-z)}))
    check("vector/algebraic E coefficient", s.diff(reexpressed, E, 2)/2-2*A/L**2)
    check("vector/E equation has no spectral derivative", s.diff(reexpressed, E, t))
    Esolution = s.solve(s.diff(reexpressed, E), E)[0]
    zsolution = s.solve(Esolution-Enew, z)[0]
    from_parent = reexpressed.subs(E, Esolution).subs(z, zsolution)
    from_parent = from_parent.subs(w, s.sqrt(2)*v+2*Enew/L).subs(Enew, E)
    vector = (A*t*c**2 + A*t*(s.sqrt(2)*v+2*g*L*c)**2/(2*g**2*L**2)
              + lam*t*(s.sqrt(2)*v+2*E/L+3*g*L*c)**2/2 - 2*A*E**2/L**2)
    check("eq:R2vec2/from constrained original action", from_parent-vector)
    expected = (3*B*t*chat**2 + A*t*v**2/(3*g**2*L**2)
                + 2*A*lam*(t-B/lam)*E**2/(L**2*B))
    check("eq:R2vec3/kinetic and mass congruence",
          vector.subs(c, chat-s.sqrt(2)*v/(3*g*L)-g*lam*E/B)-expected)
    check("eq:R2MV/mass", B*ell2/lam-(nu2-1))

    # The scalar kinetic form and inverse eigenfields are independent inputs.
    Ks = s.Matrix([[8/(3*A), -2/L, 0], [-2/L, 2/L+3*lam*g**2, 6*lam*g/L],
                   [0, 6*lam*g/L, 4*lam/L**2]])
    check("scalar/kinetic determinant", Ks.det()-16*lam/(3*L**4))
    a0, ap, am = s.symbols("a0 ap am")
    U = g*A*ell2*(ap-am)/(2*nu)
    Z = (ap+am)/2-(ap-am)/nu
    scalar = a0-L*U/B+3*lam*g*L*Z/B
    aux = Z-2*g*L*scalar
    X = U+A*scalar/L
    T = s.Matrix([X, scalar, aux]).jacobian([a0, ap, am])
    norms = s.diag(2*B/(3*L**2), 4*A/(g**2*L**4*nu*(nu+1)),
                   4*A/(g**2*L**4*nu*(nu-1)))
    Lnu = 2*(nu**2+2)/(2*nu**2+1)
    check("scalar/all eigenfield norms", (T.T*Ks*T-norms).subs(L, Lnu))

    # Gauge invariance of Lambda on the supersymmetric AdS5 background.
    check("fermion/SUSY shift of varphi", (-3*g*L**2/2)/2+3*g*L**2/4)
    check("fermion/flat Killing connection", -1/(2*ell2)+2*m**2)
    check("fermion/Lambda RS coefficient with J=i sqrt(2) I",
          -2*s.I/L*(L/(3*s.sqrt(2)))*(s.I*s.sqrt(2))-s.Rational(2, 3))
    check("fermion/Lambda spinor mass coefficient", -2*s.I/L*5*m*(s.I*s.sqrt(2))-5*g)
    check("eq:R2fermop/factorization", lam*(y+5*m)*(y-3*m)-A-lam*((y+m)**2-nu2/ell2))
    af, bf = lam*L*(mu+5*m)/(2*A), lam*(mu-m)
    pulled = 4*A*af**2/(3*L**2)+lam-4*af*bf/(3*L)+4*bf**2/(3*A)
    defining = s.together(lam*(mu+5*m)*(mu-3*m)-A).as_numer_denom()[0]
    numerator = s.together(pulled-2*lam**2*(mu**2-m**2)/A).as_numer_denom()[0]
    check("fermion/heavy norm modulo original root", s.rem(numerator, defining, mu))
    check("fermion/light norm", A**2/B**2*(4*A/(3*L**2)+2*lam*g**2)-4*A**2/(3*B*L**2))
    # These rational identities also fix the sign on 1<nu<2 without sampling.
    check("range/A in nu", A.subs(L, Lnu)-2*(nu**2-4)/(2*nu**2+1))
    check("range/B in nu", B.subs(L, Lnu)-2*(nu**2-1)/(2*nu**2+1))

    # tau=3/2: no division by A, and no inference from a generic eigenbasis.
    r, q, rho = s.symbols("r q rho")
    lc, ic = 1/(4*g**2), 8*g**2/9
    Xc = r/(8*g**2)-3*t*q/(16*g**2)+5*q/6-rho/(2*g)
    raw = ((r-s.Rational(3, 2)*t*q)**2/(16*g**2)+(5*q/6-rho/(2*g))*r
           + 25*g**2*q**2/9-10*g*q*rho/3+13*rho**2/9-s.Rational(5, 4)*q*t*q
           + 3*q*t*rho/(4*g)+rho*t*rho/(8*g**2))
    check("tau=3/2/scalar critical square modulo IBP", raw-Xc**2/lc-lc*rho*(t+4*ic)*rho/2)
    fv, fE, G, Esq, Q = s.symbols("fv fE G Esq Q")
    F = s.sqrt(2)*fv+s.Rational(3, 2)*fE
    remainder = s.expand(-4*lc*g*(F+2*g*G)*Q-3*Esq+(s.sqrt(2)*fv/g+2*G)*Q)
    check("tau=3/2/vector critical square modulo form IBP", remainder.subs(fE*Q, -2*g*Esq))
    check("tau=3/2/critical spinor norm", (4*B/(3*L**2)).subs(L, s.Rational(4, 3))/(2*g**2)-lc)

    # tau=2: finite matrices from eq:R2vec2, with the fields kept independent.
    fields = (c, v, E)
    Kv = s.hessian(s.diff(vector, t), fields)
    Mv = -s.hessian(vector.subs(t, 0), fields)
    Ke, Me = Kv.subs(L, 2), Mv.subs(L, 2)
    Nv = (Ke.inv()*Me).applyfunc(reduced)
    check("tau=2/vector determinant", Ke.det()-4/(3*g**4))
    check("tau=2/vector field equations", Nv-s.Matrix([[0, 0, -g], [0, 0, 0], [0, 0, 0]]))
    check("tau=2/vector nilpotency", Nv*Nv)
    claim("tau=2/vector Jordan block sizes", Nv.rank()==1,
          dict(rank=int(Nv.rank()), zero_root_algebraic_multiplicity=3, zero_root_kernel_dimension=2))
    C, V = s.symbols("C V")
    check("tau=2/regular vector field change",
          vector.subs(L, 2).subs({c: C-E/(4*g), v: V+s.sqrt(2)*E})
          -(2*t*C*E/g-t*V**2/(6*g**2)+E**2))

    # Use the original (X,s,n) equations; no fractional power of negative A.
    Ksc = s.Matrix([[-4, 3*A/L, 0], [-2/L, 2/L+3*lam*g**2, 6*lam*g/L],
                    [0, 6*lam*g/L, 4*lam/L**2]])
    Msc = s.Matrix([[3*A/lam+10*g**2*L**2, -3*A/lam+15*A*g**2*L, 9*A*g],
                    [2/lam-10*g**2*L, -2/lam+g**2*(4+8*L)+3*lam*g**4*L**2,
                     -2*g+18*lam*g**3*L], [-6*g, -2*g+18*lam*g**3*L, -4/L+20*lam*g**2]])
    Js = (-ell2*Ksc.inv()*Msc).subs(L, 2).applyfunc(reduced)
    check("tau=2/scalar characteristic polynomial", (y*s.eye(3)-Js).det()-y*(y+4)**2)
    check("tau=2/scalar minimal polynomial has simple BF factor", Js*(Js+4*s.eye(3)))
    claim("tau=2/two independent BF scalars", len((Js+4*s.eye(3)).nullspace())==2,
          dict(BF_kernel_dimension=2, mass_squared_times_ell_squared=[-4, -4, 0]))

    # Coupled spinor equations follow from the recorded original Euler operators.
    # The J=+1 component has I=-i/sqrt(2); the other component is Majorana paired.
    H, KF, PF = y-m, y+5*m, y-3*m
    check("tau=2/undivided spinor identity", lam*KF*PF-A-(lam*H*(y+3*m)-B))
    spinor = s.Matrix([[H, 0], [2*s.I*g*A/s.sqrt(2), lam*KF*PF-A]])
    Pe, me, le = spinor.subs(L, 2), m.subs(L, 2), lam.subs(L, 2)
    check("tau=2/spinor determinant", Pe.det()-le*(y-me)**2*(y+3*me))
    claim("tau=2/spinor Jordan pair", len(Pe.subs(y, me).nullspace())==1,
          dict(light_root_algebraic_multiplicity=2, light_root_kernel_dimension=1))
    check("tau=2/spinor Jordan source coefficient", (2*g*A/lam).subs(L, 2)+12*g**3)

    return dict(checks=records, results=dict(
        vector_endpoint=dict(K=matrix_record(Ke), M=matrix_record(Me), K_inverse_M=matrix_record(Nv)),
        scalar_endpoint=dict(dimensionless_mass_matrix=matrix_record(Js), characteristic="y*(y + 4)**2"),
        fermion_endpoint=dict(coupled_polynomial=matrix_record(Pe), light_root=str(me),
                              Jordan_source_coefficient="-12*g**3"),
        regular_region="g != 0; L > 0; lambda*A*B != 0; lambda=4*(L-1)/(3*g^2*L^2)",
        real_positive_coupling_region="0 < tau < 2, tau != 3/2; nu > 1",
        upper_interval="3/2 < tau < 2: massless vector multiplet positive; graviton and long vector multiplets negative",
        scope="Final-paper local quadratic claims only; inherited Hessian, no nonlinear SUSY or logarithmic boundary-domain proof"))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write-log", action="store_true", help="write only this package's verification records")
    args = parser.parse_args()
    sources = source_check()
    payload = calculate()
    report = dict(status="PASS", count=len(payload["checks"]), source_checks=sources,
                  versions=dict(python=platform.python_version(), sympy=s.__version__), **payload)
    out = HERE / "outputs"
    if args.write_log:
        out.mkdir(exist_ok=True)
        (out / "verification.json").write_text(json.dumps(report, indent=2)+"\n")
        (out / "verification.log").write_text(
            "Command: python3 -B computations/r2_ads5_paper_checks/checks.py --write-log\n"
            + "\n".join("PASS "+r["name"] for r in payload["checks"])
            + f"\nPASS {len(payload['checks'])} exact checks; source fingerprints verified\n")
    else:
        stored = json.loads((out / "verification.json").read_text())
        if any(stored[key] != payload[key] for key in ("checks", "results")):
            raise AssertionError("Stored results differ from fresh exact calculation")
    print(f"PASS {len(payload['checks'])} exact R2 checks; source fingerprints and stored results verified")


if __name__ == "__main__":
    main()
