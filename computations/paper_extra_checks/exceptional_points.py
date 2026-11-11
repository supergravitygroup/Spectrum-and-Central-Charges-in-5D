"""Checks of the exceptional backgrounds in Sections 4.1 and 4.3.

Adapted from the supplied exceptional_points.py by Aksoy, Okyay, Ozkan and
Senisik (2026), MIT license. Uses this repository's action for the independent
linear-variation check. It does not compute the exceptional family's spectrum.
"""
from pathlib import Path
import sys

import sympy as s

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "gb_ads3_sigma2"))
from model import L, k, g, D, M2, P1, P2, P3, P4, P5, branch, v as regular_v
from closed_forms import Y, mul, nuf, cubic


def zero(expr):
    value = s.factor(s.cancel(expr))
    assert value == 0, value


def reduced_equations():
    """Product-background equations before division by any P_i."""
    u, v, p, q, r, N, lam = s.symbols("u v p q r N lam")
    f2 = (L * (6*u + 2*v - p**2 + 8*q**2) - 2*N**2/L
          - 2*g*L*N - 4*g*N + 2*g**2*L**2 - g**2*L**3/2)
    fgb = (3*u*v + 6*u*p*q - 4*v*q**2 + 8*p*q**3
           + 2*s.sqrt(2)*g*L*r*q - 4*g*N*p*q
           + g**2*L**2 * (-(3*u + v)/2 + p**2/2 - p*q - 6*q**2)
           + g**2*N**2 + 2*g**3*N*L**2 + g**4*L**4/2)
    f = f2 + lam*fgb
    fq = s.diff(f, q)
    equations = {
        "L": s.diff(f, L), "N": s.diff(f, N),
        "three-form": -g*fq/4 + 2*g*p + s.sqrt(2)*r,
        "AdS3": 3*f/2 - u*s.diff(f, u) - 3*q*fq/2,
        "surface": f - v*s.diff(f, v) - p*s.diff(f, p) - r*s.diff(f, r),
    }
    bg = branch()
    regular = {p: bg["p"], q: bg["h"], N: bg["N"], u: -1/bg["l"]**2,
               v: regular_v, r: regular_v, lam: bg["lam"]}
    for eq in equations.values():
        zero(eq.subs(regular, simultaneous=True))
    assert [p.subs({L: 2, k: 2}) for p in (P2, P3, P4, P5)] == [0]*4

    bps = {L: 2, lam: 2/g**2, p: s.sqrt(2)*g, r: v,
           N: -4*g + 4*s.sqrt(2)*q, u: -4*(q-g/s.sqrt(2))**2}
    common = (g - 2*s.sqrt(2)*q)*v - 2*g**2*(g + 2*s.sqrt(2)*q)
    ratios = {"L": -2/g, "N": 0, "three-form": -s.sqrt(2)/g,
              "AdS3": -6/g, "surface": 0}
    vsol = 2*g**2*(g + 2*s.sqrt(2)*q)/(g - 2*s.sqrt(2)*q)
    for name, eq in equations.items():
        residual = eq.subs(bps, simultaneous=True)
        zero(residual - ratios[name]*common)
        zero(residual.subs(v, vsol))
    zero(common.subs(q, g/(2*s.sqrt(2))) + 4*g**3)
    zero(bps[u].subs(q, g/s.sqrt(2)))
    qt = -g/(2*s.sqrt(2))
    for expr in (vsol.subs(q, qt), bps[u].subs(q, qt) + 9*g**2/2,
                 bps[N].subs(q, qt) + 6*g):
        zero(expr)
    t = s.Symbol("t")
    zero(vsol.subs(q, g*t/(2*s.sqrt(2)))/g**2 - 2*(1+t)/(1-t))
    zero(-bps[u].subs(q, g*t/(2*s.sqrt(2)))/g**2 - (t-2)**2/2)

    a, b, eps = s.symbols("a b epsilon")
    approach = {L: 2+a*eps, k: 2+b*eps}
    qlim = s.limit(regular[q].subs(approach), eps, 0)
    vlim = s.limit(regular[v].subs(approach), eps, 0)
    zero(qlim + s.sqrt(2)*a*g/(4*(a+b)))
    zero(vlim - 2*b*g**2/(2*a+b))
    zero(vsol.subs(q, qlim) - vlim)
    # Two regular directions give different finite family members.
    assert s.simplify(vlim.subs({a: 1, b: 0}) - vlim.subs({a: 1, b: 1})) != 0
    print("PASS exceptional family: five undivided equations, SUSY substitution, limits", flush=True)


def action_variations():
    """Independent first variations of the complete existing GB action."""
    import symengine as se
    from sectors import sector
    ds, ss = se.symbols("D S")

    def member(t):
        t = se.sympify(t)
        vv = 2*(1+t)/(1-t)
        uu = -(t-2)**2/2
        return dict(L=se.Integer(2), N=2*(t-2), p=se.sqrt(2), h=t/(2*se.sqrt(2)),
                    r=vv, v=vv, u=uu, l=se.sqrt(-1/uu), w=se.sqrt(-vv),
                    g=se.Integer(1), lam=se.Integer(2))

    def nonzero(bg, fs=False):
        result = sector(bg, 0, ds, ss, verbose=False, fs=fs)
        linear = se.expand(result["lin_a"].subs({ds: 2, ss: 1}))
        return [value for amp in result["avars"]
                if (value := s.simplify(s.sympify(str(se.expand(se.diff(linear, amp)))))) != 0]

    for t in (3, s.Rational(-5, 2), 5, 0, s.Rational(1, 2), -1):
        assert not nonzero(member(t), fs=t == -1), t
    shifted = member(3)
    shifted["N"] += se.Rational(1, 7)
    assert nonzero(shifted)
    shifted = member(3)
    shifted["v"] -= 1
    shifted["r"], shifted["w"] = shifted["v"], se.sqrt(-shifted["v"])
    assert nonzero(shifted)
    shifted = member(-1)
    shifted["N"] += se.Rational(1, 7)
    assert nonzero(shifted, fs=True)
    print("PASS full-action first variations: six family members, three negative controls", flush=True)


def isolated_points():
    numerator = s.fraction(s.cancel(nuf))[0]
    zero(s.resultant(Y, numerator, L)
         - 256*k**8*(k-2)**2*(49*k**2 - 138*k + 64))
    for sign in (-1, 1):
        at = {L: (25+sign*s.sqrt(65))/8, k: (69-sign*5*s.sqrt(65))/49}
        assert all(s.simplify(p.subs(at)) != 0 for p in (P1, P2, P3, P4, P5))
        zero(mul.subs(at))
        zero(nuf.subs(at))
        zero(cubic.subs(at) - (D-1)*(D*(D-2)-M2))
    print("PASS two regular isolated points: mu ell_s = nu_f = 0 and cubic factorization", flush=True)


if __name__ == "__main__":
    reduced_equations()
    isolated_points()
    action_variations()
