"""Use the accepted item-25 action and item-24 prediction as separate inputs."""
from pathlib import Path
import sys
import importlib.util
import numpy as np
import sympy as sp

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
ACTION_DIR = ROOT / "computations/gb_ads3_sigma2_fermionic"
BOSON_DIR = ROOT / "computations/gb_ads3_sigma2"
sys.path.append(str(ACTION_DIR))
from action import evaluate, gauge_columns, pack, unpack, basis_record, SECTORS, lr_polynomial
from background import background
_spec=importlib.util.spec_from_file_location("_item24_sample_definitions",ACTION_DIR/"derive.py")
_samples=importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_samples)
SAMPLES=_samples.SAMPLES
import action2
sys.path.append(str(BOSON_DIR))
import model as bosonic_model
import closed_forms as bosonic_forms

def complex_pair(z):
    return [float(complex(z).real), float(complex(z).imag)]

def from_pair(x):
    return complex(*x)

def lr_matrix(L, g, n, q, D, S):
    fn,K,a,b,_=lr_polynomial(str(L),"0",str(g),str(n),q,str(S))
    return np.asarray(fn(D),complex),a,b

def gauge_at(L,k,g,n,q,D,S):
    from ferm2 import Ctx,base_objects
    from deriv2 import Var
    from gauge_modes import eps_basis,gauge_modes
    c=Ctx(sp.Rational(L),sp.Rational(k),sp.Rational(n),q,D=D,S=complex(sp.sympify(S)),
          g=sp.sympify(g),bgdict=background(sp.Rational(L),sp.Rational(k),sp.sympify(g)))
    c.eps_comps=eps_basis(sp.Rational(n),q)
    return gauge_modes(c,Var(c,base_objects(c)))

def total(L, k, g, n, q, D, S):
    if sp.sympify(k) == 0:
        return lr_matrix(L, g, n, q, D, S)[0]
    return evaluate(L, k, g, n, q, D, S)["K"]

def mode(n, D, q, origin=None):
    """The shadow operation applies to the fermion, after its SUSY shift."""
    n, D = float(n), complex(D)
    if D.real < 1:
        n, D, q = -n, 2-D, -q
    return dict(spin=n, energy=complex_pair(D), q_R=int(q), origin=origin)

def numerical_roots(poly, variable, digits=50):
    # Factor first, preserving repeated exact factors and their multiplicity.
    result = []
    for factor, multiplicity in sp.factor_list(poly, variable)[1]:
        if sp.degree(factor, variable) > 0:
            for root in sp.Poly(factor, variable).nroots(n=digits, maxsteps=500):
                result.extend([complex(root)] * multiplicity)
    return result

def prediction(L, k, S):
    """Bosonic closed forms already checked independently by item 24.

    They never enter action interpolation, root selection or rank tests.
    The torus constant level has its separate short-multiplet content.
    """
    m, f = bosonic_model, bosonic_forms
    lv, kv, sv = map(sp.sympify, (L, k, S))
    bg = background(lv, kv, 1)
    level = sp.simplify(-bg["v"]*bg["l"]**2*sv*(1-sv))
    chi = bg["chi"]
    substitution = {m.L:lv, m.k:kv, m.M2:level}
    if kv == 0:
        cubic = sp.limit(m.k*f.cubic, m.k, 0).subs(substitution)
        quintic = sp.limit(m.k*f.F, m.k, 0).subs(substitution)
    else:
        cubic, quintic = f.cubic.subs(substitution), f.F.subs(substitution)
    out = []
    if bg["v"] == 0 and kv == 0 and sv == 0:
        massive = sp.cancel(quintic/(m.D*(m.D-2)))
        for d in numerical_roots(massive, m.D):
            for q in (1,-1):
                out.append(mode(.5, d+.5, q, "T2 massive boson-primary"))
        for q in (1,-1):
            for n,d in [(1.5,1.5),(.5,2.5),(.5,2.5),(-1.5,2.5),(-.5,1.5)]:
                out.append(mode(n,d,q,"T2 massless/short multiplet"))
    else:
        for d in numerical_roots(cubic, m.D):
            for q in (1,-1):
                out.append(mode(1.5,1+chi*(d-1.5),q,"spin2 multiplet"))
        for d in numerical_roots(quintic, m.D):
            for q in (1,-1):
                out.append(mode(.5,1+chi*(d-.5),q,"scalar-vector multiplet"))
        if kv != 0:
            nu = complex(f.nuf.subs(substitution))
            nu_chi = 1+chi*(nu-1)
            for q in (1,-1):
                out += [mode(1-chi/2,nu_chi-.5,q,"flat lower"),
                        mode(1+chi/2,nu_chi+.5,q,"flat upper")]
    return out, dict(chi=chi, M2=complex_pair(complex(level)))
