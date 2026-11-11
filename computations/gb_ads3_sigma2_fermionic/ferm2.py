"""Numeric zero-momentum fermion engine for phase 2 (complex128 at fixed D, S).

Same frame and modes as phase 1 (fengine.py): E_0=(z/l)d_t, E_1=(z/l)d_x, E_2=(z/l)d_z, E_3=w y d_y1,
E_4=w y d_y2.  Fermions: phi-side ~ z^D y^S (amplitudes eta_k, k < Na), chi-side ~ z^(2-D) y^(1-S) (xi_m, m < Nb).

Lin: a fermionic tensor linear in the fluctuations.  Arrays A (..., 2, 4, Na) and B (..., 2, 4, Nb); leading axes are
frame indices (all LOWER), then the SU(2) index (UPPER), the spinor index and the mode.
K-array: two-fermion part of a bosonic tensor, array (..., Nb, Na) with frame indices lower: the quadratic action is
sum_{m,k} xi_m K_mk eta_k.  A Majorana bilinear Xbar Gamma Y contributes  X_B^T C Gamma Y_A - (X_A^T C Gamma Y_B)^T.

Conventions: those of the density (GB02-GB04) and of clifford.py: gamma^{01234} = i, C = gamma^2 gamma^4,
X_i = X^j eps_ji, eps_12 = 1, (J X)^i = delta^{ij} X_j."""
import itertools
import numpy as np
import sympy as sp
from clifford import GU as _GU, gam as _gam, CC as _CC, J as _J
from bgfields import Background, ETA, EPS2, EPS_LOW
ETAI = np.linalg.inv(ETA)
R5 = range(5)
c2n = lambda M: np.array(M.tolist(), dtype=complex)
CC = c2n(_CC); JM = c2n(_J); NW = EPS2.T.astype(complex); DL = np.eye(2, dtype=complex)
I = 1j; s2 = np.sqrt(2)

def _gamma_array(r, lower):
    if r == 0: return np.eye(4, dtype=complex)
    out = np.zeros((5,) * r + (4, 4), complex)
    for idx in itertools.product(R5, repeat=r):
        if len(set(idx)) == r: out[idx] = c2n(_gam(*idx, lower=lower))
    return out
# Pure in-memory Clifford arrays: importing this module never writes a cache.
GL = [_gamma_array(r, True) for r in range(6)]
GUP = [_gamma_array(r, False) for r in range(6)]

# ------------------------------------------------------------------ linear fermionic objects
class Lin:
    __slots__ = ('A', 'B')
    def __init__(s, A, B): s.A, s.B = A, B
    def __add__(s, o): return Lin(s.A + o.A, s.B + o.B)
    def __sub__(s, o): return Lin(s.A - o.A, s.B - o.B)
    def __neg__(s): return Lin(-s.A, -s.B)
    def __mul__(s, c): return Lin(s.A * c, s.B * c)
    __rmul__ = __mul__
    def __truediv__(s, c): return Lin(s.A / c, s.B / c)
    def ap(s, f): return Lin(f(s.A), f(s.B))
    @property
    def nfr(s): return s.A.ndim - 3
    def __getitem__(s, k): return Lin(s.A[k], s.B[k])

def lin_zero(Na, Nb, shape=()): return Lin(np.zeros(shape + (2, 4, Na), complex), np.zeros(shape + (2, 4, Nb), complex))
def gm(M, X):
    """left-multiply the spinor index by a 4x4 matrix M (M may carry leading frame axes that broadcast like X's)"""
    if M.ndim == 2: return X.ap(lambda a: np.einsum('st,...itn->...isn', M, a))
    raise ValueError
def su2(M, X): return X.ap(lambda a: np.einsum('ij,...jsn->...isn', M, a))
def ein(expr, *ops):
    """einsum on a Lin operand (exactly one) and arrays; the Lin operand's spec must end with 'isn' style letters
    for (su2, spinor, mode) given explicitly by the caller"""
    k = [j for j, o in enumerate(ops) if isinstance(o, Lin)]; assert len(k) == 1
    k = k[0]
    fa = lambda arr: np.einsum(expr, *[arr if j == k else o for j, o in enumerate(ops)], optimize=True)
    return Lin(fa(ops[k].A), fa(ops[k].B))

def kb(X, xs, Y, ys, ops, out):
    """K-array of the bilinear  Xbar Gamma Y  (X barred): xs, ys index strings of X, Y without the mode letter
    (frame..., su2, spinor); ops = list of (array, spec) including the charge conjugation C and the SU(2) pairing;
    out = output frame/su2 letters.  Returns array out + (Nb, Na)."""
    arrs = [a for a, _ in ops]; specs = [sp_ for _, sp_ in ops]
    e1 = ','.join([xs + 'm', ys + 'n'] + specs) + '->' + out + 'mn'
    e2 = ','.join([xs + 'n', ys + 'm'] + specs) + '->' + out + 'mn'
    return np.einsum(e1, X.B, Y.A, *arrs, optimize=True) - np.einsum(e2, X.A, Y.B, *arrs, optimize=True)

def bl(X, xf, Y, yf, G=None, gf='', P=NW, out='', pre=None, prespec=''):
    """K-array of  sum P_ij Xbar^i_{xf} G_{gf} Y^j_{yf}  with frame letters xf, yf, gf; out = output frame letters.
    P = NW gives the default contraction Xbar^i Y_i; P = DL gives delta_ij Xbar^i Y^j.  Optional pre = extra array
    (e.g. a background tensor or eta^{-1}) with spec prespec."""
    ops = [(CC, 'su')]
    ops.append((G, gf + 'ut') if G is not None else (np.eye(4, dtype=complex), 'ut'))
    if P is not None: ops.append((P, 'ij'))
    if pre is not None: ops.append((pre, prespec))
    return kb(X, xf + ('i' if P is not None else '') + 's', Y, yf + ('j' if P is not None else '') + 't', ops, out)

# ------------------------------------------------------------------ context: background, frame, modes
class Ctx:
    def __init__(s, L, k, n, q, D, S, g=1, lamGB=None, bgdict=None):
        s.B = B = Background(L, k, g, bgdict=bgdict)
        s.l, s.w, s.g = B.l, B.w, B.g
        s.D, s.S = complex(D), complex(S)
        s.Gam = B.Gam                                    # Gamma^c_{ab}
        s.om = B.om                                      # omega_a^{cd}
        s.Om = np.einsum('acd,cdst->ast', s.om, GL[2]) / 4  # (1/4) omega_a^{cd} gamma_cd
        l, w = s.l, s.w
        s.mA = np.zeros(5, complex); s.mA[2] = s.D / l; s.mA[4] = w * s.S
        s.mB = np.zeros(5, complex); s.mB[2] = (2 - s.D) / l; s.mB[4] = w * (1 - s.S)
        s.mAB = s.mA + s.mB
        # background tensors (lower)
        s.G, s.H, s.T, s.f, s.Cw, s.Riem = B.G, B.H, B.T, B.f, B.Cw, B.Riem
        s.N, s.L, s.p, s.h, s.r = B.N, B.L, B.p, B.h, B.r
        s.V = np.zeros(5, complex); s.V[3] = B.r / w if w != 0 else 0     # U(1) potential, V_a^{ij} = delta^{ij} V_a / 2
        s.dV = np.zeros((5, 5), complex); s.dV[3, 4] = B.r; s.dV[4, 3] = -B.r
        s.Lij = B.Lij
        s.gT = np.einsum('ab,abst->st', s.T, GUP[2])     # gamma.T = gamma^{ab} T_ab
        s.gG = np.einsum('ab,abst->st', s.G, GUP[2])
        s.gH = np.einsum('ab,abst->st', s.H, GUP[2])
        s.fields(n, q)
        s._checks()

    def fields(s, n, q):
        from fengine import build_fields
        psi, phi, ba, bb = build_fields(sp.Rational(n), q)
        tonum = lambda arr: np.array(arr.tolist(), dtype=complex)
        s.Na, s.Nb = len(ba), len(bb)
        s.psi = Lin(np.array([tonum(psi[a].A) for a in R5]), np.array([tonum(psi[a].B) for a in R5]))
        s.varphi = Lin(tonum(phi.A), tonum(phi.B))
        s.basis = (ba, bb)

    def _checks(s):
        # spin connection compatible with the frame connection: [Om_a, gamma^b] = -Gam^b_{ae} gamma^e
        for a in R5:
            for b in R5:
                lhs = s.Om[a] @ GUP[1][b] - GUP[1][b] @ s.Om[a]
                rhs = -np.einsum('e,est->st', s.Gam[b, a], GUP[1])
                assert np.allclose(lhs, rhs)
        # total derivatives of bilinears vanish: mAB[e] + Gam^a_{ae} = 0
        assert np.allclose(s.mAB + np.einsum('aae->e', s.Gam), 0)

    # -------------------------------------------------------------- ordinary covariant derivatives
    def nab(s, X):
        """nabla_c X_{a1..an}: weight factor, spin connection, Levi-Civita on frame indices, U(1)_R connection.
        Returns a Lin with the derivative index c prepended."""
        n = X.nfr
        def side(arr, m):
            out = np.einsum('c,...->c...', m, arr)
            out = out + np.einsum('cst,...itm->c...ism', s.Om, arr)
            for k in range(n):
                # - Gam^e_{c a_k} X_{..e..}
                Xm = np.moveaxis(arr, k, 0)
                t = -np.einsum('eca,e...->ca...', s.Gam, Xm)
                out = out + np.moveaxis(t, 1, 1 + k)
            out = out - 0.5 * np.einsum('c,ij,...jsm->c...ism', s.V, JM, arr)
            return out
        return Lin(side(X.A, s.mA), side(X.B, s.mB))

    def nabK(s, K, nfr):
        """nabla_c of a K-array whose first nfr axes are frame indices (no SU(2) axes)"""
        out = np.einsum('c,...->c...', s.mAB, K)
        for k in range(nfr):
            Km = np.moveaxis(K, k, 0)
            t = -np.einsum('eca,e...->ca...', s.Gam, Km)
            out = out + np.moveaxis(t, 1, 1 + k)
        return out

# ------------------------------------------------------------------ phase-1 objects (gauge sigma=1, psi^i=0, b=0)
def base_objects(c):
    """psi_a, R'(Q), phi_a, R^(Q), D_a psi (dilatino), chi, varphi, D_a varphi -- linear in the fluctuations"""
    o = {}
    psi = c.psi; o['psi'] = psi
    npsi = c.nab(psi)                                            # [c, a]: nabla_c psi_a
    gpsi = psi.ap(lambda a: np.einsum('bst,aitn->abisn', GL[1], a))   # gamma_b psi_a  [a, b]
    Rp = npsi - npsi.ap(lambda a: np.swapaxes(a, 0, 1))
    # + i gamma.T (gamma_a psi_b - gamma_b psi_a)
    x = gpsi.ap(lambda a: np.swapaxes(a, 0, 1)) - gpsi           # [a,b]: gamma_a psi_b - gamma_b psi_a
    Rp = Rp + gm(c.gT, x) * I
    o["R'Q"] = Rp
    t1 = ein('bst,abitn->aisn', GUP[1], Rp)                         # gamma^b R'_ab
    t2 = ein('bcst,bcitn->isn', GUP[2], Rp)                         # gamma^{bc} R'_bc
    ph = t1 * (I / 3) - ein('ast,itn->aisn', GL[1], t2) * (I / 24)
    o['phi_mu'] = ph
    gph = ein('bst,aitn->abisn', GL[1], ph)                         # [a,b] gamma_b phi_a
    o['RQ'] = Rp - (gph.ap(lambda a: np.swapaxes(a, 0, 1)) - gph) * I    # R'_ab - i (gamma_a phi_b - gamma_b phi_a)
    gG4T = np.einsum('ab,abst->st', c.G / 4 - c.T, GUP[2])
    d = gm(gG4T, psi) - ph - su2(JM, psi) * (c.g * c.L / (2 * s2))
    o['Dpsi'] = d
    o['chi'] = ein('ast,aitn->isn', GUP[1], d) * (I / 8) + c.varphi * (c.g / 8)
    o['varphi'] = c.varphi
    Dphi = c.nab(c.varphi) - psi * (c.N / 2) + gm(c.gT, su2(JM, psi)) * (c.L / s2) - su2(JM, ph) * (3 * c.L / s2)
    o['Dvarphi'] = Dphi
    return o

