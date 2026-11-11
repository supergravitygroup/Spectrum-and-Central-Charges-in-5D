"""Exact v109 BPS background; numerical evaluation is a separate operation.

g and k are caller inputs. Symbolic L,k require an explicit chirality.
The formulas agree with item 24; no bosonic output files are consumed.
"""
import sympy as sp


def background(L, k, g, chi=None):
    L, k, g = map(sp.sympify, (L, k, g))
    P1, P2, P3 = 2-k*L, 4-k*L, 2*L+4-k*L**2
    P4, P5 = 8-4*k-4*k*L+k**2*L**2, 8+4*k-8*k*L+k**2*L**2
    if any(x == 0 for x in (L, g, P1, P2, P3, P4, P5)):
        raise ValueError('Excluded or singular v109 background')
    if not (L.free_symbols or g.free_symbols) and (L <= 0 or g <= 0):
        raise ValueError('The physical convention requires L > 0 and g > 0')
    ratio = P3/P2
    if chi is None:
        if ratio.free_symbols:
            raise ValueError('Specify chi=+1 or -1 for a symbolic background')
        chi = 1 if ratio > 0 else -1
    if chi not in (-1, 1):
        raise ValueError('chi must be +1 or -1')
    if not ratio.free_symbols and chi*ratio <= 0:
        raise ValueError('chi is inconsistent with the positive AdS radius')
    ell_s = sp.sqrt(2)*P2/(g*P3)
    v = 2*g**2*L*(2*L-8+3*k*L-k*L**2)/P4
    return dict(L=L, N=-g*L*P3/P2, p=g*L/sp.sqrt(2),
                h=g*(L-2)/(sp.sqrt(2)*P2), r=v, v=v,
                u=-1/ell_s**2, l=chi*ell_s, w=sp.sqrt(-v),
                g=g, lam=k/g**2, chi=chi)
