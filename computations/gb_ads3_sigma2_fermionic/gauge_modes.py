"""Explicit local-supersymmetry gauge modes in a sector (n,q) and their residuals K v.
delta psi_a = nabla_a eps + i g.T g_a eps - i g_a eta,  eta = -delta_Q(eps) psi_dil (dilatino gauge),
delta varphi = delta_Q varphi + delta_S varphi;  eps ~ z^D y^S, spinor weight n, J-charge q (phi side)."""
import numpy as np, sympy as sp
from ferm2 import Lin, ein, gm, su2, GL, GUP, JM, I
from clifford import SIGMA01, J as Jsym

def eps_basis(n, q):
    sig = SIGMA01.eigenvects(); jev = Jsym.eigenvects()
    us = [sp.Matrix(v) for val, m, vs in sig if sp.simplify(val - sp.Rational(n)) == 0 for v in vs]
    vq = [sp.Matrix(vs[0]) for val, m, vs in jev if sp.simplify(val - sp.I * q) == 0][0]
    out = []
    for u in us:
        comp = np.array((u * vq.T).T.tolist(), dtype=complex)          # [i, alpha]
        out.append(comp)
    return out

def gauge_modes(c, v):
    """columns: coefficients of the gauge modes in the phi-side sector basis; also the LSQ residuals"""
    from fractions import Fraction
    n = Fraction(c.basis[0][0][2].shape[0]) if False else None
    modes = []; res = []
    psiA = c.psi.A; phA = c.varphi.A
    Bmat = np.concatenate([psiA.reshape(-1, c.Na), phA.reshape(-1, c.Na)], axis=0)
    for comp in c.eps_comps:
        E = Lin(comp[:, :, None], np.zeros((2, 4, 0), complex))
        nabE = c.nab(E)                                           # [a]
        soft = v.soft(E)
        eta = -v.dQ_dil(E)
        geta = ein('ast,itn->aisn', GL[1], eta) * (-I)
        dpsi = nabE + soft + geta
        dphi = v.dQ_varphi(E) + v.dS_varphi(eta)
        rhs = np.concatenate([dpsi.A.reshape(-1), dphi.A.reshape(-1)])
        coef, *_ = np.linalg.lstsq(Bmat, rhs, rcond=None)
        res.append(np.linalg.norm(Bmat @ coef - rhs) / max(np.linalg.norm(rhs), 1e-300))
        modes.append(coef)
    return np.array(modes).T, res
