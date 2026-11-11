#!/usr/bin/env python3
"""Bounded exact replay of the final paper's Weyl/LOG AdS5 claims.

The inputs are the cited quadratic densities and reduced equations, not a
new component-action engine. Default execution writes only to stdout.
--write-log explicitly records this package's results.
"""
import argparse
import hashlib
import itertools
import json
from pathlib import Path
import platform

import sympy as s
from sympy.matrices.normalforms import smith_normal_form

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_lock():
    manifest = json.loads((HERE / "source_manifest.json").read_text())
    for path, expected in manifest["current_inputs"].items():
        if digest(ROOT / path) != expected:
            raise AssertionError("Review changed formula source: " + path)
    for path, expected in manifest["implementation_hashes"].items():
        if digest(HERE / path) != expected:
            raise AssertionError("Review changed implementation: " + path)
    return manifest


def run_checks():
    manifest = source_lock()
    records = []

    def zero(name, expression, group):
        entries = list(expression) if isinstance(expression, s.MatrixBase) else [expression]
        residuals = [s.simplify(s.cancel(x)) for x in entries]
        if any(x != 0 for x in residuals):
            raise AssertionError((name, residuals))
        records.append(dict(name=name, group=group, method="exact", residual="0"))

    def nonzero(name, expression, group):
        residual = s.factor(expression)
        if residual == 0:
            raise AssertionError("Negative control failed: " + name)
        records.append(dict(name=name, group=group, method="exact",
                            nonzero_residual=str(residual)))

    a, g, t, r, z, m = s.symbols("alpha g t rho z m", nonzero=True, real=True)
    a0 = 1-a*g**2/6
    nu2 = g**2/2-3/a
    M = s.Matrix([
        [-2*a0+(a/3-2/g**2)*t, 2*t/g**2, -s.sqrt(2)*a0/g],
        [2*t/g**2, 3-2*t/g**2, s.sqrt(2)/g],
        [-s.sqrt(2)*a0/g, s.sqrt(2)/g, a/3],
    ])
    w, c, v = s.symbols("w c v")
    Y = s.Matrix([w,c,v])
    # Paper WV after dX.dY = -2 X tY, E = t(w-c)/g.
    WV = (3*c*t*c+2*s.sqrt(2)*c*t*v/g+a*v*t*v/3
          -2*a0*w*t*w-2*s.sqrt(2)*a0*w*t*v/g
          +a*w*t**2*w/3-2*t**2*(c-w)**2/g**2)
    zero("WV quadratic form gives t M", WV-(Y.T*t*M*Y)[0], "Weyl vectors")
    det_expected = -2*a**2/(9*g**2)*((t-nu2)**2-2*g**2*nu2)
    zero("constrained vector determinant", M.det()-det_expected, "Weyl vectors")
    for sig in (-1,1):
        root = g**2*(r**2+2*sig*r)/2
        direction = s.Matrix([1-sig*r, -sig*r, -g*(r**2-sig*r)/s.sqrt(2)])
        Mr = M.subs(a,6/(g**2*(1-r**2)))
        zero(f"vector {sig}: all null-vector rows", Mr.subs(t,root)*direction, "Weyl vectors")
        coefficient = 2*(direction.T*s.diff(t*Mr,t).subs(t,root)*direction)[0]
        zero(f"vector {sig}: normalized kinetic coefficient",
             coefficient+4*r**2*(r+2*sig)/(r+sig), "Weyl vectors")
    u, v0 = s.symbols("u v0")
    Y0 = s.Matrix([-v0/(s.sqrt(2)*g),u-s.sqrt(2)*v0/(3*g),v0])
    zero("two Maxwell kinetic coefficients",
         (Y0.T*M.subs(t,0)*Y0)[0]-3*u**2-(a*g**2+2)*v0**2/(6*g**2), "Weyl vectors")
    dT2,jT2,T2 = s.symbols("dT2 jT2 T2")
    cross = jT2+s.Rational(3,2)*g**2*T2
    W21 = (-s.Rational(64,3)*(dT2/3+2*cross)+s.Rational(64,3)*cross
           +s.Rational(128,3)*jT2+s.Rational(64,3)*g**2*T2)
    zero("W21 derivative terms give paper Wquad after AdS IBP",
         W21+s.Rational(64,9)*dT2-s.Rational(64,3)*jT2+s.Rational(32,3)*g**2*T2,
         "Weyl quadratic action")

    x, mass = s.symbols("x mass")
    current_poly = mass**2-2*x*mass+x*(x-4)
    normalized = {t:mass*g**2/2,a:6/(g**2*(1-x))}
    zero("current determinant in dimensionless mass",
         M.det().subs(normalized)+2*current_poly/(g**2*(x-1)**2), "Weyl vectors")

    # Explicit realization of the final paper's Appendix A, not an extra
    # convention imposed on the component conventions.
    I2 = s.eye(2)
    sx = s.Matrix([[0,1],[1,0]])
    sy = s.Matrix([[0,-s.I],[s.I,0]])
    sz = s.diag(1,-1)
    G = [s.I*s.kronecker_product(sx,I2), s.kronecker_product(sy,I2),
         s.kronecker_product(sz,sx), s.kronecker_product(sz,sy),
         -s.kronecker_product(sz,sz)]
    eta = [-1,1,1,1,1]
    C = G[1]*G[3]
    B = C*(-G[0])
    I4 = s.eye(4)
    zero("Majorana C antisymmetry", C.T+C, "paper reality convention")
    zero("Majorana C unitary normalization", C.H*C-I4, "paper reality convention")
    zero("symplectic Majorana B star B", B.conjugate()*B+I4, "paper reality convention")
    volume = I4
    for ga in G:
        volume *= ga
    zero("paper epsilon orientation", volume-s.I*I4, "paper reality convention")
    for i in range(5):
        zero(f"gamma {i} Majorana adjoint", G[i].T*C-C*G[i], "paper reality convention")
        for j in range(i,5):
            zero(f"Clifford {i},{j}", G[i]*G[j]+G[j]*G[i]-(2*eta[i]*I4 if i==j else s.zeros(4)), "paper reality convention")
    eps = s.Matrix([[0,1],[-1,0]])
    Js = -eps
    Jpaper = -s.I*Js
    zero("paper J squared", Jpaper**2-s.eye(2), "paper reality convention")
    zero("internal mass convention", s.I*g*Js/(2*s.sqrt(2))+g*Jpaper/(2*s.sqrt(2)), "paper reality convention")
    zero("NW-SE internal mass formal adjoint", Js.T*(-eps)+(-eps)*Js, "paper reality convention")

    # Complexified Euclidean Clifford representation suffices for these
    # signature-independent covariant projector identities.
    E = [s.kronecker_product(sx,I2), s.kronecker_product(sy,I2),
         s.kronecker_product(sz,sx),s.kronecker_product(sz,sy),s.kronecker_product(sz,sz)]
    Z = s.zeros(4)
    def gab(i,j):
        return (E[i]*E[j]-E[j]*E[i])/2
    def project(Q):
        tr = sum((gab(i,j)*Q[i][j] for i in range(5) for j in range(5)),Z)
        return [[Q[i][j]+sum((E[i]*E[h]*Q[j][h]-E[j]*E[h]*Q[i][h] for h in range(5)),Z)/3-gab(i,j)*tr/12
                 for j in range(5)] for i in range(5)]
    for i,j in itertools.combinations(range(5),2):
        Q = [[s.zeros(4) for _ in range(5)] for _ in range(5)]
        Q[i][j],Q[j][i] = I4,-I4
        projected = project(Q)
        zero(f"Q gamma trace, free bivector {i},{j}",
             s.Matrix.vstack(*(sum((E[h]*projected[h][b] for h in range(5)),Z) for b in range(5))), "fermion projector")
    for h in range(5):
        Q = [[E[j]*int(i==h)-E[i]*int(j==h) for j in range(5)] for i in range(5)]
        zero(f"Q annihilates gamma wedge derivative {h}",s.Matrix.vstack(*(q for row in project(Q) for q in row)), "fermion projector")
    zero("Q annihilates AdS SUSY curvature term",s.Matrix.vstack(*(q for row in project([[gab(i,j) for j in range(5)] for i in range(5)]) for q in row)), "fermion projector")
    zero("X gauge curvature identity",sum((gab(i,j)*gab(i,j) for i in range(5) for j in range(5)),Z)+20*I4, "fermion projector")
    for i in range(5):
        zero(f"X gauge derivative identity {i}",sum((gab(i,j)*E[j] for j in range(5)),Z)-4*E[i], "fermion projector")

    mval = g/(2*s.sqrt(2))
    zero("X linearized SUSY shift",4*m*z+20*m**2-4*m*(z+5*m),"fermion projector")
    trace_X = 32*a*(z-5*m)*(z-m)/3-96
    spinor_X = -128*m/g-32*a*g*(z-m)/3
    zero("mixed fermion trace equations give X polynomial",
         (trace_X-8*m*spinor_X/g-32*(1+a*(z+3*m)*(z-m)/3)).subs(m,mval),
         "Weyl fermions")
    P = -a*(z+3*m)*((z-m)**2-nu2)/3
    paper = (1+a*g**2/2)*(z-3*mval)+a*(z-3*mval)**2*(z+5*mval)/3
    zero("paper gravitino two equivalent factors",paper-a*(z-3*mval)*((z+mval)**2-nu2)/3, "Weyl fermions")
    zero("paper/repo gravitino signed operator",P.subs(m,mval)-paper.subs(z,-z), "Weyl fermions")
    zero("massless gravitino coefficient",-s.diff(P,z).subs(z,-3*m).subs(m,mval)-(1+a*g**2/2), "Weyl fermions")
    for sig in (-1,1):
        relation = {m:mval,a:6/(g**2*(1-r**2))}
        zero(f"gravitino {sig} residue",(-s.diff(P,z).subs(z,(1+2*sig*r)*m)-a*g**2*r*(r+2*sig)/3).subs(relation), "Weyl fermions")
        aa,bb = 16*a*g*(1+sig*r)/3,16*a*m*(1+sig*r)/3
        mu = -(1+2*sig*r)*m
        h = (bb*(z-5*m)+g*aa)/8
        L2 = ((12*bb**2+2*aa**2-32*aa*bb*m/g)*z
              -60*bb**2*m-14*aa**2*m+20*g*aa*bb)
        zero(f"X {sig}: two-derivative action pullback",(L2+aa**2*(z+3*m)/2).subs(m,mval), "Weyl X norm")
        L = -aa**2*(z+3*m)/2-256*a*h**2*(z-m)/3
        zero(f"X {sig}: composite embedding",(h.subs(z,mu)-1).subs(relation), "Weyl X norm")
        zero(f"X {sig}: full action root",L.subs(z,mu).subs(relation), "Weyl X norm")
        zero(f"X {sig}: kinetic coefficient",(-s.diff(L,z).subs(z,mu)+256*a**2*g**2*r*(r+sig)/9).subs(relation), "Weyl X norm")

    # Exact endpoints are evaluated in the undivided polynomials.
    for q in (-2,6):
        Pr = P.subs({a:q/g**2,m:mval})
        target = (-a*(z+3*m)**2*(z-5*m)/3 if q==-2 else -a*(z+3*m)*(z-m)**2/3)
        zero(f"critical q={q} gravitino",Pr-target.subs({a:q/g**2,m:mval}), "critical operators")
        vector_target = -8*t**3*(t-4*g**2)/(9*g**6) if q==-2 else -8*t**4/g**6
        zero(f"critical q={q} constrained vector determinant",(t**2*M.det()).subs(a,q/g**2)-vector_target, "critical operators")
    zero("q=6 X double factor",((z+mval)**2-nu2).subs(a,6/g**2)-(z+mval)**2, "critical operators")
    # t below is dimensionless t/g^2; g=1 fixes units, not the free coupling.
    SM = smith_normal_form(s.diag(1,t,t)*M.subs({g:1,a:-2}),domain=s.QQ.algebraic_field(s.sqrt(2)).poly_ring(t))
    zero("q=-2 vector Smith form",SM-s.diag(1,t,s.Rational(8,9)*t**2*(t-4)), "critical operators")
    K = s.Matrix([[s.Rational(1,3),16*a/9],[16*a/9,64*a**2/27]])
    scalar_map = s.Matrix([[1,16*a/3],[0,-1]])
    zero("scalar kinetic pullback",scalar_map.T*K*scalar_map-s.diag(s.Rational(1,3),-64*a**2/9), "critical operators")
    zero("q=6 two separate nonzero BF scalar coefficients",s.diag(s.Rational(2,3),-128*a**2/9).subs(a,6/g**2)-s.diag(s.Rational(2,3),-512/g**4), "critical operators")

    # LOG: source-local alpha is the paper's beta. These are checks of the
    # displayed coupled equations, not a new full LOG Hessian derivation.
    L, beta, tt, D = s.symbols("L beta t_internal D", nonzero=True,real=True)
    beta_bps = 8*(L-1)/(g**2*L**2)
    nv = (4-L)/(2*(L-1))
    qhat = -4*(L-1)/(2-L)
    zero("LOG parameter map",1-6/qhat-nv,"LOG displayed operators")
    zero("LOG massless kinetic coefficient",(2-L)*(1+qhat/2)-(4-3*L),"LOG displayed operators")
    AA = 4*(L-1)*z**2-12*(L-1)*z+31-13*L
    BB = 4*(L-1)*z+4*L-10
    CC = 16*(L-1)*z**2-24*L*z+100-40*L
    HH = (10*L-4)*z+13*L-34
    chi, rh = s.symbols("chi rho_spinor")
    e1,e2 = AA*(rh-chi)+BB*(4*rh-3*chi),CC*(rh-chi)+HH*(4*rh-3*chi)
    half = 4*(L-1)*(z*z+z)+3*L-9
    zero("LOG coupled row subtraction",e2-4*e1+3*(L-2)*(2*z+1)*chi,"LOG displayed operators")
    zero("LOG coupled spin-half separation",e1-half*rh+(L-1)*(2*z-1)*(2*z+1)*chi,"LOG displayed operators")
    zero("LOG spin-half factorization",half-4*(L-1)*((z+s.Rational(1,2))**2-nv),"LOG displayed operators")
    P32 = beta*D**3/3+beta*tt*D**2/6+(L-3-beta*tt**2/2)*D+3*(L-3)*tt/2
    zero("LOG TT cubic factorization",P32-(D+3*tt/2)*(beta*(D**2-tt*D)/3+L-3),"LOG displayed operators")
    ttval = g*L/s.sqrt(2)
    zero("LOG TT masses equal paper nu",(P32-beta*(D+3*tt/2)*((D-tt/2)**2-tt**2*nv)/3).subs({beta:beta_bps,tt:ttval}),"LOG displayed operators")
    zero("LOG critical tau=3/2 massless merger",nv.subs(L,s.Rational(4,3))-4,"LOG displayed operators")
    return dict(status="PASS_SCOPED_EXACT", count=len(records), checks=records,
                python=platform.python_version(), sympy=s.__version__,
                current_inputs=manifest["current_inputs"],
                paper_sources=manifest["external_source_records"],
                scope="Displayed Weyl quadratic densities, formal/physical convention bridge, local operators and LOG reduced equations; no new invariant construction or global boundary-norm calculation.")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write-log",action="store_true")
    args = parser.parse_args()
    report = run_checks()
    text = json.dumps(report,indent=2,ensure_ascii=False)+"\n"
    if args.write_log:
        out = HERE / "outputs"
        out.mkdir(exist_ok=True)
        (out / "verification.json").write_text(text)
        (out / "verification.log").write_text(
            f"{report['status']}: {report['count']} bounded exact checks\n"
            f"Python {report['python']}; SymPy {report['sympy']}\n"
            "\n".join(f"PASS [{r['group']}] {r['name']}" for r in report["checks"])+"\n")
    print(text,end="")


if __name__ == "__main__":
    main()
