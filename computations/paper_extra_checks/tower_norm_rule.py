"""Section 4.5: large-level spin-2 norm and positive-weight criterion.

Adapted from the supplied tower_norm_rule.py by Aksoy, Okyay, Ozkan and
Senisik (2026), MIT license. Imports the repository's cubic and coefficients.
The numerical scan checks the analytic rule; it is not its proof.
"""
from pathlib import Path
import random
import sys

import mpmath as mp
import sympy as s

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "gb_ads3_sigma2"))
from model import L, k, D, M2, P1, P2, P3, P4, P5
from closed_forms import cubic, nuf, mul, kappa


def zero(expr):
    value = s.factor(s.cancel(expr))
    assert value == 0, value


def symbolic_rule():
    zero(nuf-1 - 2*P1*P2/(k*P3))
    zero(nuf+1 - 8*(P1+k)/(k*P3))
    zero(nuf**2-1 - 16*P1*P2*(P1+k)/(k*P3)**2)
    nu, mu, eps = s.symbols("nu mu epsilon")
    polynomial = D*(D-2)*(D-1-mu)-M2*(D-1-nu)
    correction = (nu**2-1)*(nu-mu)
    near = 1+nu+correction*eps
    expanded = s.expand(polynomial.subs({D: near, M2: 1/eps}))
    zero(expanded.coeff(eps, 0))
    zero(s.limit(eps*s.diff(polynomial, D).subs({D: near, M2: 1/eps}), eps, 0)+1)
    zero(correction.subs(nu, 0)-mu)
    zero(kappa - L*k*P3*mul/(4*P2))
    # A=P1; B=P1+k. Positive weights mean A*P2*B>0. In that
    # domain sign(nu)=sign(A*P2/(k*P3)); multiplying by chi*k
    # leaves sign(A). A>0 also forces P2=A+2>0. Thus both norm
    # and weights are positive exactly when A>0 and B>0.
    zero(P2-P1-2)
    zero(P1+k-(2-k*(L-1)))
    for asign in (-1, 1):
        for bsign in (-1, 1):
            for p2sign in (-1, 1):
                if asign == 1 and p2sign == -1:
                    continue  # P2=P1+2 excludes this sign combination.
                weights = asign*p2sign*bsign > 0
                assert (weights and asign > 0) == (asign > 0 and bsign > 0)
    at = {L: 3, k: 2}
    zero(nuf.subs(at))
    assert mul.subs(at) < 0 and kappa.subs(at) < 0
    print("PASS analytic expansion and positive norm + positive weights iff kL<2, k(L-1)<2", flush=True)


def numerical_rule(samples=400):
    rng = random.Random(20261110)
    mp.mp.dps = 60
    checked = 0
    while checked < samples:
        lv, kv = s.Rational(rng.randint(1, 240), 20), s.Rational(rng.randint(-120, 120), 20)
        at = {L: lv, k: kv}
        if kv == 0 or any(p.subs(at) == 0 for p in (P1, P2, P3, P4, P5)):
            continue
        nu, mu = s.cancel(nuf.subs(at)), s.cancel(mul.subs(at))
        if nu == 0 or abs(nu) == 1:
            continue
        chi = int(s.sign((P3/P2).subs(at)))
        m2 = s.Integer(10)**8
        poly = s.Poly(cubic.subs({**at, M2: m2}), D)
        coeff = [mp.mpf(str(c.evalf(65))) for c in poly.all_coeffs()]
        roots = mp.polyroots(coeff, maxsteps=1000, extraprec=200)
        target = mp.mpf(str((1+nu).evalf(65)))
        root = min(roots, key=lambda r: abs(r-target))
        assert abs(mp.im(root)) < mp.mpf("1e-45")
        residual_scale = sum(abs(c)*max(1, abs(root))**(3-i) for i, c in enumerate(coeff))
        assert abs(mp.polyval(coeff, root))/residual_scale < mp.mpf("1e-45")
        deriv = mp.polyval([coeff[i]*(3-i) for i in range(3)], root)
        pref = -lv*kv*(P3/P2).subs(at)**3/32
        norm = int(mp.sign(mp.re(root)-1)*mp.sign(mp.mpf(str(pref.evalf(65)))*deriv))
        predicted = int(s.sign(chi*kv*nu))
        assert norm == predicted, (lv, kv, norm, predicted)
        weights = abs(nu) > 1
        assert bool(abs(root-1) > 1) == bool(weights), (lv, kv)
        condition = lv*kv < 2 and kv*(lv-1) < 2
        assert bool(norm > 0 and weights) == bool(condition), (lv, kv)
        if chi == -1:
            assert norm < 0, (lv, kv)
        checked += 1
    print(f"PASS {checked} regular rational points at M^2=10^8 (60-digit arithmetic)", flush=True)


if __name__ == "__main__":
    symbolic_rule()
    numerical_rule()
