"""Linear Q/S variations of bosonic covariants, gauge-field variations, and two-fermion parts of their derivatives.

Q-variation of a bosonic covariant Phi: delta_Q(eps) Phi = epsbar Xi_Phi (linear in the fluctuations).  As a function
of a parameter Lin E with leading-axis letters ef, XiQ_*(E, ef) returns the K-array of  Ebar Xi  with axes ef + own.
Sources: H02 with the revision-3 overlay (G^, H^), L01 (L, N), W03 (T, D), R06a (R^(V)), R04a/W01 (omega, b, V).

Derivative rule (G01 chain rule; D eps terms cancel and are dropped):
  (D_c Phi)^(2) = nabla_c Phi^(2) + omega^(2)_{c a}^e Phi^0_{..e..} - Xi_Phi(psi_c) - Sigma_Phi(phi_c)      [K-inert Phi]
  delta_Q(E) D_b Phi = Ebar D_b Xi_Phi - Xi_Phi(i g.T g_b E) + delta omega_{b a}^e Phi^0_{..e..} - w delta b_b Phi^0
                       - Sigma_Phi(delta_Q phi_b(E))            [Phi^0 SU(2)-neutral, first derivatives of Phi^0 vanish]
  delta_S(E) D_b Phi = - Xi_Phi(-i g_b E) + delta_S omega_{b a}^e Phi^0_{..e..} - w delta_S b_b Phi^0 - Sigma_Phi(delta_S phi_b(E))
  (D_a D_b Phi)^(2) = nabla_a (D_b Phi)^(2) - XiQ_{D_b Phi}(psi_a) - XiS_{D_b Phi}(phi_a) + K[f, Phi]^(2),
  K[f, X]_{ab..} = 2w f_ab X_.. + sum_k [2 f_{a x_k} X_{..b..} - 2 eta_{b x_k} f_a^e X_{..e..}]  (f's first index = outer derivative)."""
import itertools
import numpy as np
from ferm2 import Lin, ein, gm, su2, kb, bl, GL, GUP, ETA, ETAI, EPS_LOW, NW, DL, JM, CC, I, s2
from objects2 import asym2

LET = 'abcdefgh'
# Revision-3 H02; alternate values are used only by explicit negative controls.
H02_G_SIGN = 1.0
H02_GAUGED_FACTOR = 1.0

def perm_sign(p):
    s = 1
    for i in range(len(p)):
        for j in range(i + 1, len(p)):
            if p[i] > p[j]: s = -s
    return s
def antisym(K, axes):
    """unit-weight antisymmetrisation over the given axes"""
    out = 0
    for p in itertools.permutations(range(len(axes))):
        perm = list(range(K.ndim))
        for k, ax in enumerate(axes): perm[ax] = axes[p[k]]
        out = out + perm_sign(p) * np.transpose(K, perm)
    return out / len(list(itertools.permutations(range(len(axes)))))
def raise_all(K, nfr):
    for k in range(nfr): K = np.moveaxis(np.einsum('x...,xy->y...', np.moveaxis(K, k, 0), ETAI), 0, k)
    return K
def sym_ij(X, xf, Y, yf, G=None, gf='', out=''):
    """Xbar^(i G Y^j) with free upper SU(2) indices appended (i, j) before the modes"""
    ops = [(CC, 'su'), (G, gf + 'ut') if G is not None else (np.eye(4, dtype=complex), 'ut')]
    K = kb(X, xf + 'is', Y, yf + 'jt', ops, out + 'ij')
    return 0.5 * (K + np.swapaxes(K, -4, -3))

class BVar:
    def __init__(s, c, o, e, v):
        s.c, s.o, s.e, s.v = c, o, e, v
        s.gaTgb = 0.5 * (np.einsum('ast,tu,buv->absv', GL[1], c.gT, GL[1]) - np.einsum('bst,tu,auv->absv', GL[1], c.gT, GL[1]))

    # ---------------------------------------------------------- Xi functions (F: dict of fermion objects; xb: extra
    # leading letter carried by those objects, for the derivative versions)
    def XiQ_G(s, E, ef, F=None, xb=''):
        F = F or s.o
        t = bl(E, ef, F['RQ'], xb + 'pq', out=ef + xb + 'pq') * (-I / 2)
        u = bl(E, ef, F['Dpsi'], xb + 'q', G=GL[1], gf='p', out=ef + xb + 'pq')
        return t - 0.5 * (u - np.swapaxes(u, -3, -4))
    def XiQ_H3(s, E, ef, F=None, xb=''):
        F = F or s.o
        n = len(ef) + len(xb)
        t = bl(E, ef, F['RQ'], xb + 'qr', G=GL[1], gf='p', out=ef + xb + 'pqr') * (-0.75)
        u = bl(E, ef, F['Dpsi'], xb + 'r', G=GL[2], gf='pq', out=ef + xb + 'pqr') * (1.5 * I)
        # Correction C2 of the item-25 fermionic_action_inputs.md, correction C2.
        # gauged theory: H^ contains (g/2) E_c (GG04a); the covariant part of delta E_c,abc is + epsbar gamma_abc varphi
        # (fixed by delta T(composite) = W03, test_bos.py B3; the literal L04 sign is quarantined by X10)
        w_ = bl(E, ef, F['varphi'], xb, G=GL[3], gf='pqr', out=ef + xb + 'pqr') * (H02_GAUGED_FACTOR * s.c.g / 2)
        return antisym(t + u, [n, n + 1, n + 2]) + w_
    def XiQ_Hd(s, E, ef, F=None, xb=''):
        X3 = s.XiQ_H3(E, ef, F, xb); n = len(ef) + len(xb)
        X3u = X3
        for k in range(3): X3u = np.moveaxis(np.einsum('x...,xy->y...', np.moveaxis(X3u, n + k, 0), ETAI), 0, n + k)
        return -np.einsum('abcde,...cdemn->...abmn', EPS_LOW, X3u) / 12
    def XiQ_T(s, E, ef, F=None, xb=''):
        return (s.XiQ_G(E, ef, F, xb) - 2 * s.XiQ_Hd(E, ef, F, xb)) / 8
    def XiQ_T_W03(s, E, ef):
        return bl(E, ef, s.o['chi'], '', G=GL[2], gf='pq', out=ef + 'pq') * (I / 2) - bl(E, ef, s.o['RQ'], 'pq', out=ef + 'pq') * (3j / 32)
    def XiQ_L(s, E, ef, F=None, xb=''):
        F = F or s.o
        return sym_ij(E, ef, F['varphi'], xb, out=ef + xb) * I
    def XiQ_N(s, E, ef, F=None, xb=''):
        F = F or s.o; c = s.c
        t = bl(E, ef, F['Dvarphi'], xb + 'p', G=GUP[1], gf='p', out=ef + xb) * 0.5
        t = t + bl(E, ef, F['varphi'], xb, G=c.gT, out=ef + xb) * (1.5 * I)
        t = t + bl(E, ef, F['chi'], xb, P=DL, out=ef + xb) * (4 * I * c.L / s2)
        return t
    def XiS_N(s, E, ef, F=None, xb=''):
        F = F or s.o
        return bl(E, ef, F['varphi'], xb, out=ef + xb) * (1.5 * I)
    def XiQ_D(s, E, ef, F=None, xb=''):
        F = F or s.o
        return bl(E, ef, F['Dchi'], xb + 'p', G=GUP[1], gf='p', out=ef + xb) - bl(E, ef, F['chi'], xb, G=s.c.gT, out=ef + xb) * (5j / 3)
    def XiS_D(s, E, ef, F=None, xb=''):
        F = F or s.o
        return bl(E, ef, F['chi'], xb, out=ef + xb) * (-I)

    # ---------------------------------------------------------- gauge-field variations (tangent index b first)
    def dw_Q(s, E, ef):
        """delta omega_{b cd} (lower), R04a Q part: axes ef + 'bcd'"""
        o = s.o; out = ef + 'bcd'
        t = bl(E, ef, o['phi_mu'], 'b', G=GL[2], gf='cd', out=out) * (I / 2)
        t = t - bl(E, ef, o['psi'], 'b', G=s.gaTgb, gf='cd', out=out) * I
        x = bl(E, ef, o['RQ'], 'bd', G=GL[1], gf='c', out=out); t = t - 0.25 * (x - np.swapaxes(x, -3, -4))
        t = t - bl(E, ef, o['RQ'], 'cd', G=GL[1], gf='b', out=out) * 0.25
        y = bl(E, ef, o['chi'], '', G=GL[1], gf='d', out=ef + 'd')
        y = np.einsum('...dmn,bc->...bcdmn', y, ETA); t = t - 2 * (y - np.swapaxes(y, -3, -4))
        return t
    def dw_S(s, E, ef):
        return bl(E, ef, s.o['psi'], 'b', G=GL[2], gf='cd', out=ef + 'bcd') * (-I / 2)
    def db_Q(s, E, ef):
        return bl(E, ef, s.o['phi_mu'], 'b', out=ef + 'b') * (I / 2) - 2 * bl(E, ef, s.o['chi'], '', G=GL[1], gf='b', out=ef + 'b')
    def db_S(s, E, ef):
        return bl(E, ef, s.o['psi'], 'b', out=ef + 'b') * (I / 2)

    # ---------------------------------------------------------- helpers
    def om_act(s, dw, X0, nX):
        """+ dw_{b x_k}^e X0_{..e..} for each lower index of the background tensor X0 (nX indices); dw axes (...,b,c,d,m,n)"""
        dwm = np.einsum('...bcxmn,xe->...bcemn', dw, ETAI)                      # dw_{b c}^e
        lead = dw.ndim - 5
        out = 0
        letters = 'pqrs'[:nX]
        for k in range(nX):
            src = letters[:k] + 'e' + letters[k + 1:]
            spec = '...b' + letters[k] + 'emn,' + src + '->...b' + letters + 'mn'
            out = out + np.einsum(spec, dwm, X0)
        return out
    def Kterm(s, X0, X2, w, nX):
        """K[f, X]^(2) for (D_a D_b X)^(2): axes a, b, X-indices, m, n"""
        c, e = s.c, s.e
        f0 = c.f; f2 = e['f']
        out = 2 * w * (np.einsum('abmn,...->ab...mn', f2, X0) if nX == 0 else np.einsum('abmn,' + 'pqrs'[:nX] + '->ab' + 'pqrs'[:nX] + 'mn', f2, X0))
        out = out + 2 * w * np.einsum('ab,' + 'pqrs'[:nX] + 'mn->ab' + 'pqrs'[:nX] + 'mn', f0, X2)
        L = 'pqrs'[:nX]
        for k in range(nX):
            # 2 f_{a x_k} X_{..b..} - 2 eta_{b x_k} f_a^e X_{..e..}
            srcb = L[:k] + 'b' + L[k + 1:]; srce = L[:k] + 'e' + L[k + 1:]
            out = out + 2 * np.einsum('a' + L[k] + 'mn,' + srcb + '->ab' + L + 'mn', f2, X0)
            out = out + 2 * np.einsum('a' + L[k] + ',' + srcb + 'mn->ab' + L + 'mn', f0, X2)
            f2u = np.einsum('axmn,xe->aemn', f2, ETAI); f0u = np.einsum('ax,xe->ae', f0, ETAI)
            out = out - 2 * np.einsum('b' + L[k] + ',aemn,' + srce + '->ab' + L + 'mn', ETA, f2u, X0)
            out = out - 2 * np.einsum('b' + L[k] + ',ae,' + srce + 'mn->ab' + L + 'mn', ETA, f0u, X2)
        return out

    # ---------------------------------------------------------- first derivatives, (2)-parts
    def first(s, X2, X0, nX, XiQ, XiS=None):
        """(D_c X)^(2) for a K-inert covariant with nX lower frame indices: axes c, X-indices, m, n"""
        c, o, e = s.c, s.o, s.e
        out = c.nabK(X2, nX)
        if nX:
            omm = np.einsum('cdxmn,xe->cdemn', e['omega'], ETAI)              # omega^(2)_{c d}^e
            L = 'pqrs'[:nX]
            for k in range(nX):
                src = L[:k] + 'e' + L[k + 1:]
                out = out + np.einsum('c' + L[k] + 'emn,' + src + '->c' + L + 'mn', omm, X0)
        out = out - XiQ(o['psi'], 'c')
        if XiS is not None: out = out - XiS(o['phi_mu'], 'c')
        return out

def first_derivatives(bv):
    c, o, e = bv.c, bv.o, bv.e
    d = {}
    d['DG'] = bv.first(e['G'], c.G, 2, bv.XiQ_G)
    d['DHd'] = bv.first(e['H'], c.H, 2, bv.XiQ_Hd)
    d['DT'] = (d['DG'] - 2 * d['DHd']) / 8
    d['DL'] = -bv.XiQ_L(o['psi'], 'c')                                          # [c, i, j]
    d['DN'] = bv.first(np.zeros((c.Nb, c.Na), complex), np.array(c.N), 0, bv.XiQ_N, bv.XiS_N)
    d['DH3'] = bv.first(e['H3'], H3_bg(c), 3, bv.XiQ_H3)
    return d

def H3_bg(c):
    H3 = np.zeros((5, 5, 5), complex)
    for q in itertools.permutations((0, 1, 2)): H3[q] = perm_sign(q) * (-2 * c.h)
    return H3

# ------------------------------------------------------------------ curvature variations (R07, R04d), linear order
class CurvVar:
    """delta R'(M)_{cd ab} (tangent, all lower), delta f_cd, delta C^_abcd for a parameter E (Q) or H (S).
    R07: delta R' = 2 D_[mu delta omega_nu] + delta B, then the tangent frame variation; D E terms are dropped
    (they cancel: R'(M) has no derivative of the parameter in its variation)."""
    def __init__(s, bv):
        s.bv = bv; c = bv.c; s.c = c; o = bv.o; v = bv.v
        s.W = {}
        # nabla of the fermion objects entering delta omega (ordinary covariant derivative)
        s.n_phi = c.nab(o['phi_mu'])            # [c, d]
        s.n_psi = c.nab(o['psi'])
        s.n_RQ = c.nab(o['RQ'])                 # [c, d, b]
        s.n_chi = c.nab(o['chi'])               # [c]
        s.R0 = c.Riem                           # R'(M)^0_{cd ab} = Riemann (form pair first)
    def _domega_der(s, E, ef):
        """Ebar (nabla_c W_d - nabla_d W_c)^{ab} with delta omega_d = Ebar W_d (R04a, Q): axes ef + c d a b"""
        bv = s.bv; o = bv.o; out = ef + 'cdab'
        t = bl(E, ef, s.n_phi, 'cd', G=GL[2], gf='ab', out=out) * (I / 2)
        t = t - bl(E, ef, s.n_psi, 'cd', G=bv.gaTgb, gf='ab', out=out) * I
        x = bl(E, ef, s.n_RQ, 'cdb', G=GL[1], gf='a', out=out); t = t - 0.25 * (x - np.swapaxes(x, -3, -4))
        t = t - bl(E, ef, s.n_RQ, 'cab', G=GL[1], gf='d', out=out) * 0.25
        y = bl(E, ef, s.n_chi, 'c', G=GL[1], gf='b', out=ef + 'cb')
        y = np.einsum('...cbmn,da->...cdabmn', y, ETA); t = t - 2 * (y - np.swapaxes(y, -3, -4))
        return t - np.swapaxes(t, len(ef), len(ef) + 1)
    def _dB(s, E, ef, dpsi, dphi, dRQ, dchi):
        """variation of B: one fermion replaced by its variation (Lin with axes ef + own)"""
        bv = s.bv; o = bv.o; out = ef + 'cdab'
        psi, ph, RQ, chi = o['psi'], o['phi_mu'], o['RQ'], o['chi']
        def pair(X, xf, Y, yf, G, gf):
            return bl(X, xf, Y, yf, G=G, gf=gf, out=out)
        t = 0
        if dphi is not None: t = t + I * pair(dphi, ef + 'c', psi, 'd', GL[2], 'ab')
        t = t + I * pair(ph, 'c', dpsi, ef + 'd', GL[2], 'ab')
        t = t + I * (pair(dpsi, ef + 'c', psi, 'd', bv.gaTgb, 'ab') + pair(psi, 'c', dpsi, ef + 'd', bv.gaTgb, 'ab'))
        x = pair(dpsi, ef + 'c', RQ, 'db', GL[1], 'a') + pair(psi, 'c', dRQ, ef + 'db', GL[1], 'a')
        t = t + 0.5 * (x - np.swapaxes(x, -3, -4))
        t = t + 0.5 * (pair(dpsi, ef + 'c', RQ, 'ab', GL[1], 'd') + pair(psi, 'c', dRQ, ef + 'ab', GL[1], 'd'))
        y = bl(dpsi, ef + 'c', chi, '', G=GL[1], gf='b', out=ef + 'cb') + bl(psi, 'c', dchi, ef, G=GL[1], gf='b', out=ef + 'cb')
        y = np.einsum('...cbmn,da->...cdabmn', y, ETA); t = t + 4 * (y - np.swapaxes(y, -3, -4))
        n = len(ef)
        return 0.5 * (t - np.swapaxes(t, n, n + 1))
    def dRp_Q(s, E, ef):
        bv = s.bv; v = bv.v; o = bv.o; n = len(ef)
        t = s._domega_der(E, ef)
        t = t + s._dB(E, ef, v.soft(E), v.dQ_phi(E), v.dQ_RQ(E), v.dQ_chi(E))
        # tangent frame variation: delta e_c^mu = -(1/2) Ebar gamma^e psi_c e_e^mu
        u = bl(E, ef, o['psi'], 'c', G=GUP[1], gf='e', out=ef + 'ce')            # Ebar gamma^e psi_c
        t = t - 0.5 * np.einsum('...cemn,edab->...cdabmn', u, s.R0) - 0.5 * np.einsum('...demn,ceab->...cdabmn', u, s.R0)
        return t
    def dRp_S(s, Hh, ef):
        bv = s.bv; v = bv.v; o = bv.o
        out = ef + 'cdab'
        t = bl(Hh, ef, s.n_psi, 'cd', G=GL[2], gf='ab', out=out) * (-I / 2)
        t = t - np.swapaxes(t, len(ef), len(ef) + 1)
        dpsi = ein('bst,...itn->...bisn', -I * GL[1], Hh)
        t = t + s._dB(Hh, ef, dpsi, v.dS_phi(Hh), v.dS_RQ(Hh), v.dS_chi(Hh))
        return t
    @staticmethod
    def ricci_f_C(dRp):
        """from a variation of R'_{cdab}: (delta Ric_cd, delta f_cd, delta C_cdab), leading axes kept"""
        Ric = np.einsum('...cbdxmn,bx->...cdmn', dRp, ETAI)
        Rs = np.einsum('...cdmn,cd->...mn', Ric, ETAI)
        f = -Ric / 6 + np.einsum('cd,...mn->...cdmn', ETA, Rs) / 48
        add = 2 * (np.einsum('...camn,db->...cdabmn', f, ETA) - np.einsum('...cbmn,da->...cdabmn', f, ETA)
                   - np.einsum('...damn,cb->...cdabmn', f, ETA) + np.einsum('...dbmn,ca->...cdabmn', f, ETA))
        return Ric, f, dRp + add

def sigma_hessian_vars(bv, cv):
    """delta_Q and delta_S of D_a D_c sigma (linear order), as functions of a parameter (axes ef + a c).
    delta(D_a D_c sigma) = Ebar D_a Xi_c - Xi_c(soft_a) + 2 delta f_{ac} - (1/2) Ebar g^b psi_a (2 f_bc)
    with Xi_c(E) = (i/2) Ebar D_c psi + 2 Ebar g_c chi (SC7D-05)."""
    c, o, v = bv.c, bv.o, bv.v
    def XiDs(E, ef, F=None, xb=''):
        F = F or o
        return bl(E, ef, F['Dpsi'], xb + 'q', out=ef + xb + 'q') * (I / 2) + 2 * bl(E, ef, F['chi'], xb, G=GL[1], gf='q', out=ef + xb + 'q')
    Fd = {'Dpsi': o['DDpsi'], 'chi': o['Dchi']}          # derivative versions, extra leading letter
    def XiQ(E, ef):
        n = len(ef)
        t = XiDs(E, ef, Fd, 'a')                                          # Ebar D_a Xi_c  -> ef a q
        t = t - XiDs(v.soft(E), ef + 'a')                                 # - Xi_c(i g.T g_a E)
        _, df, _ = CurvVar.ricci_f_C(cv.dRp_Q(E, ef))
        t = t + 2 * df
        u = bl(E, ef, o['psi'], 'a', G=GUP[1], gf='b', out=ef + 'ab')     # Ebar gamma^b psi_a
        t = t - np.einsum('...abmn,bq->...aqmn', u, c.f)
        return t
    def XiS(Hh, ef):
        t = -XiDs(ein('bst,...itn->...bisn', -I * GL[1], Hh), ef + 'a')
        _, df, _ = CurvVar.ricci_f_C(cv.dRp_S(Hh, ef))
        return t + 2 * df
    return XiDs, XiQ, XiS

# ------------------------------------------------------------------ brute-force variations of first derivatives
def _tr(K, n1, n2):
    """move the first n1 axes behind the next n2 axes (keeps the rest)"""
    perm = list(range(n1, n1 + n2)) + list(range(n1)) + list(range(n1 + n2, K.ndim))
    return np.transpose(K, perm)

class Brute:
    """Full transformation coefficients (incl. undifferentiated-dilatino terms) and the brute-force variation of a
    first derivative:
      delta_eps(D_y Phi) = epsbar nab_y(Xi^full) - Xi(soft_y eps) - psibar_y Xi(F -> delta_eps F)
                           - phibar_y Sigma(F -> delta_eps F) - Sigma(delta_Q phi_y) + delta omega_y.Phi^0
                           - w delta b_y Phi^0 - delta V_y.Phi^0 - delta f_y . delta_K Phi^0 .
    F: dict of fermion constituents; xb: letters of the extra leading axes they carry."""
    def __init__(s, bv, cv):
        s.bv, s.cv = bv, cv; c, o, v = bv.c, bv.o, bv.v; s.c, s.o, s.v = c, o, v
        zero = Lin(np.zeros((2, 4, c.Na), complex), np.zeros((2, 4, c.Nb), complex))
        s.F0 = dict(o); s.F0['dil'] = zero
        zero5 = Lin(np.zeros((5, 2, 4, c.Na), complex), np.zeros((5, 2, 4, c.Nb), complex))
        s.Fnab = {'RQ': c.nab(o['RQ']), 'Dpsi': c.nab(o['Dpsi']), 'chi': c.nab(o['chi']), 'varphi': c.nab(o['varphi']),
                  'Dvarphi': c.nab(o['Dvarphi']), 'dil': zero5, 'Dchi': c.nab(o['Dchi'])}
        g3 = np.einsum('ast,tu,bcuv->abcsv', GL[1], c.gT, GL[2])                 # gamma_a g.T gamma_bc
        s.gTg3 = antisym(g3, [0, 1, 2])
        s.gG3 = antisym(np.einsum('ast,bc->abcst', GL[1], c.G), [0, 1, 2])         # gamma_[a G_bc]
    def FQ(s, E):
        v = s.v
        return {'RQ': v.dQ_RQ(E), 'Dpsi': v.dQ_Dpsi(E), 'dil': v.dQ_dil(E), 'chi': v.dQ_chi(E), 'varphi': v.dQ_varphi(E),
                'Dvarphi': v.dQ_Dvarphi(E)}
    def FS(s, Hh):
        v = s.v
        return {'RQ': v.dS_RQ(Hh), 'Dpsi': v.dS_Dpsi(Hh), 'dil': v.dS_dil(Hh), 'chi': v.dS_chi(Hh), 'varphi': v.dS_varphi(Hh),
                'Dvarphi': v.dS_Dvarphi(Hh)}
    # ---- full coefficients (E barred; F constituents)
    def Xi_G(s, E, ef, F, xb=''):
        bv = s.bv
        t = bv.XiQ_G(E, ef, F, xb)
        return t + bl(E, ef, F['dil'], xb, G=bv.gaTgb, gf='pq', out=ef + xb + 'pq') * I
    def Sg_G(s, E, ef, F, xb=''):
        return bl(E, ef, F['dil'], xb, G=GL[2], gf='pq', out=ef + xb + 'pq') * I
    def Xi_H3(s, E, ef, F, xb=''):
        t = s.bv.XiQ_H3(E, ef, F, xb)
        t = t - 1.5 * bl(E, ef, F['dil'], xb, G=s.gTg3, gf='pqr', out=ef + xb + 'pqr')
        # Correction C1 in the item-25 fermionic_action_inputs.md.
        # H02 of reference revision 2 printed -(3/2) epsbar g_[a G^_bc] psi (revision 3, X12, has +); the supercovariant commutator [D_x, D_y] H^ (test_second.py S2H,
        # coefficient fit in dbg_H.py) and D D T (S3) require +(3/2) in our conventions.  Only derivatives of this
        # undifferentiated-dilatino term enter (second derivatives of H^).
        t = t + H02_G_SIGN * 1.5 * bl(E, ef, F['dil'], xb, G=s.gG3, gf='pqr', out=ef + xb + 'pqr')
        return t
    def Sg_H3(s, E, ef, F, xb=''):
        return -1.5 * bl(E, ef, F['dil'], xb, G=GL[3], gf='pqr', out=ef + xb + 'pqr')
    @staticmethod
    def dual(X3, n):
        for k in range(3): X3 = np.moveaxis(np.einsum('x...,xy->y...', np.moveaxis(X3, n + k, 0), ETAI), 0, n + k)
        return -np.einsum('abcde,...cdemn->...abmn', EPS_LOW, X3) / 12
    def Xi_Hd(s, E, ef, F, xb=''): return s.dual(s.Xi_H3(E, ef, F, xb), len(ef) + len(xb))
    def Sg_Hd(s, E, ef, F, xb=''): return s.dual(s.Sg_H3(E, ef, F, xb), len(ef) + len(xb))
    def Xi_Ds(s, E, ef, F, xb=''):
        t = bl(E, ef, F['Dpsi'], xb + 'q', out=ef + xb + 'q') * (I / 2) + 2 * bl(E, ef, F['chi'], xb, G=GL[1], gf='q', out=ef + xb + 'q')
        return t - 0.5 * bl(E, ef, F['dil'], xb, G=np.einsum('qst,tu->qsu', GL[1], s.c.gT), gf='q', out=ef + xb + 'q')
    def Sg_Ds(s, E, ef, F, xb=''):
        return -0.5 * bl(E, ef, F['dil'], xb, G=GL[1], gf='q', out=ef + xb + 'q')
    def Xi_N(s, E, ef, F, xb=''): return s.bv.XiQ_N(E, ef, F, xb)
    def Sg_N(s, E, ef, F, xb=''): return s.bv.XiS_N(E, ef, F, xb)
    def Xi_L(s, E, ef, F, xb=''): return s.bv.XiQ_L(E, ef, F, xb)
    # ---- brute-force variation of D_y Phi
    def vary_first(s, Xi, Sg, Phi0, w, nown, E, ef, kind='Q', lorentz=True, Kterm=None):
        """returns K-array with axes ef + 'y' + own (nown own indices)"""
        c, o, v, bv = s.c, s.o, s.v, s.bv
        n = len(ef)
        if kind == 'Q':
            t = Xi(E, ef, s.Fnab, 'y')
            t = t - Xi(v.soft(E), ef + 'y', s.F0)
            FQ = s.FQ(E)
            t = t - _tr(Xi(o['psi'], 'y', FQ, ef), 1, n)
            if Sg is not None:
                t = t - _tr(Sg(o['phi_mu'], 'y', FQ, ef), 1, n)
                t = t - Sg(v.dQ_phi(E), ef + 'y', s.F0)
            dw = bv.dw_Q(E, ef); db = bv.db_Q(E, ef)
        else:
            t = 0
            if Sg is not None: t = Sg(E, ef, s.Fnab, 'y')
            t = t - Xi(ein('bst,...itn->...bisn', -I * GL[1], E), ef + 'y', s.F0)
            FS = s.FS(E)
            t = t - _tr(Xi(o['psi'], 'y', FS, ef), 1, n)
            if Sg is not None:
                t = t - _tr(Sg(o['phi_mu'], 'y', FS, ef), 1, n)
                t = t - Sg(v.dS_phi(E), ef + 'y', s.F0)
            dw = bv.dw_S(E, ef); db = bv.db_S(E, ef)
        if Phi0 is not None and np.any(Phi0 != 0):
            if lorentz and nown:
                dwm = np.einsum('...bcxmn,xe->...bcemn', dw, ETAI)
                Lt = 'pqrs'[:nown]
                for k in range(nown):
                    src = Lt[:k] + 'e' + Lt[k + 1:]
                    t = t + np.einsum('...y' + Lt[k] + 'emn,' + src + '->...y' + Lt + 'mn', dwm, Phi0)
            t = t - w * np.einsum('...ymn,' + 'pqrs'[:nown] + '->...y' + 'pqrs'[:nown] + 'mn', db, Phi0)
        if Kterm is not None: t = t + Kterm(E, ef, kind)
        return t
