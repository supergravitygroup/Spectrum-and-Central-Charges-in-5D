"""Complete item-25 quadratic action, evaluated at caller-supplied parameters.

The LR summand uses exact algebra. The GB tensor contractions use complex128;
their samples are numerical results, not symbolic identities in L,k,g,D,S.
No roots, physical-minor reductions or bosonic multiplet predictions enter.
"""
from functools import lru_cache
from fractions import Fraction
import numpy as np
import sympy as sp
from background import background
from ferm2 import Ctx
from eval2 import KGB
from gauge_modes import eps_basis, gauge_modes
import action2

DSYM = sp.Symbol('D')
SECTORS = tuple((sp.Rational(n, 2), q) for n in (1, -1, 3, -3) for q in (1, -1))


def exact(value):
    return sp.sympify(str(value))


def basis_record(basis):
    return [dict(field='varphi' if field == 'phi' else field, frame=a,
                 spinor=[str(x) for x in u], doublet=[str(x) for x in v])
            for field, a, u, v in basis]


@lru_cache(maxsize=128)
def lr_polynomial(L, k, g, n, q, S):
    bg = background(exact(L), exact(k), exact(g))
    K, a, b, parts = action2.K2(bg, exact(n), q, DSYM, exact(S), parts=True)
    arrays = {name: sp.lambdify(DSYM, sp.Matrix(value.tolist()), 'numpy')
              for name, value in parts.items()}
    return sp.lambdify(DSYM, K, 'numpy'), K, a, b, arrays


def evaluate(L, k, g, n, q_R, D, S, *, trace=False):
    """Return LR, raw -2W, raw -4LOG, total matrices and their live context.

The bare-potential chart requires v!=0. Nonzero-k T2 and excluded loci
are deliberately rejected, as they were not analyzed in v109's fermion section.
"""
    L, k, g, n, S = map(exact, (L, k, g, n, S))
    if (n, q_R) not in SECTORS:
        raise ValueError('Allowed sectors: n=+/-1/2,+/-3/2 and q_R=+/-1')
    bg = background(L, k, g)
    if bg['v'] == 0:
        raise ValueError('The GB bare-potential chart does not cover T2')
    if any(x.free_symbols for x in (L, k, g, S)):
        raise ValueError('GB evaluation is numerical: supply L,k,g,S explicitly')
    c = Ctx(Fraction(L), Fraction(k), Fraction(n), q_R,
            D=complex(D), S=complex(S), g=g, bgdict=bg)
    parts, engine = KGB(c, split=True, trace=trace)
    fn, _, a, b, lrparts = lr_polynomial(*map(str, (L, k, g, n)), q_R, str(S))
    LR = np.asarray(fn(complex(D)), complex)
    coefficient = -float(k)/(2*float(g)**2)
    K = LR + coefficient*(parts['W']+parts['LOG'])
    if not np.isfinite(K).all():
        raise ArithmeticError('Nonfinite total quadratic matrix')
    return dict(K=K, LR=LR, W=parts['W'], LOG=parts['LOG'],
                lambda_GB=coefficient, background=bg, a=a, b=b, n=n, q_R=q_R,
                context=c, engine=engine,
                lr_parts={name: np.asarray(f(complex(D)), complex) for name, f in lrparts.items()})


def gauge_columns(result):
    c, eng = result['context'], result['engine']
    # Construct transformations from the SUSY rules, never from a fitted kernel.
    c.eps_comps = eps_basis(result['n'], result['q_R'])
    return gauge_modes(c, eng.v)


def pack(matrix):
    A = np.asarray(matrix, complex)
    return dict(real=A.real.tolist(), imag=A.imag.tolist())


def unpack(record):
    return np.asarray(record['real']) + 1j*np.asarray(record['imag'])
