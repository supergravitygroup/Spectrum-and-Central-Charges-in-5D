"""Q/S variations at bosonic order of the fermionic objects, and the fermionic derivative objects.

All parameters (eps, eta) are Lin objects with arbitrary leading frame axes (e.g. eps = psi_c); results carry those
axes first, then the object's own frame indices.  Background bosons are covariantly constant, so every D T, D G^,
D L, D N on the background vanishes.  Sources (the repository component reference plus the item-25 H02 overlay):
  dilatino  delta psi = (-g.G/4 + g.T) eps + (g/2) L^{ij} eps_j + eta                      (W02 gauged, GG05)
  varphi    delta varphi = N eps/2 - g.T L^{ij} eps_j + 3 L^{ij} eta_j                       (L01)
  chi       delta chi = eps D/4 - (1/64) g.R^{ij}(V) eps_j - (1/4) g^{abcd} T_ab T_cd eps + T^2 eps/6 + g.T eta/4   (W03)
  phi_b     SC7D-10 (bosonic part);  D_b psi: SC7D-11;  R^_ab(Q): R05 (with X11);  R^(S): R06b.
  D_c R^_ab(Q) = nabla_c R^_ab - delta_Q(psi_c) R^_ab - delta_S(phi_c) R^_ab    (R06 rule, K invariant)
  D_a D_b psi = nabla_a [D_b psi] - delta_Q(psi_a) D_b psi - delta_S(phi_a) D_b psi                        (SC7D-12)
  D_a D_b varphi = nabla_a D_b varphi - delta_Q(psi_a) D_b varphi - delta_S(phi_a) D_b varphi + 7 f_ab varphi
                   - f_a^c gamma_cb varphi                                       (K-connection, weight 7/2)
with delta(D_b Phi) = D_b(delta Phi) - delta_Q(i g.T g_b eps) Phi - delta_S(delta_Q phi_b|_0) Phi for a fermion Phi."""
import numpy as np
from ferm2 import Lin, ein, gm, su2, GL, GUP, ETA, ETAI, JM, I, s2

def _b(M, E):
    """M[b] (5,4,4) acting on E -> Lin with a new axis b after E's leading axes"""
    return ein('bst,...itn->...bisn', M, E)
def _ab(M, E):
    return ein('abst,...itn->...abisn', M, E)

class Var:
    def __init__(s, c, o):
        s.c, s.o = c, o
        g, L, T, G, H, f = c.g, c.L, c.T, c.G, c.H, c.f
        up = lambda X: np.einsum('ab,ax,by->xy', X, ETAI, ETAI)
        s.Tu = up(T); s.T2 = np.einsum('ab,ab->', T, s.Tu)
        s.gT, s.gG = c.gT, c.gG
        # phi_b variation pieces (SC7D-10)
        s.Mphi1 = I * np.einsum('bc,cst->bst', f, GUP[1])
        dVu = up(c.dV)
        gcdgb = np.einsum('cdst,btu->bsu', np.einsum('cdst,cd->cdst', GUP[2], c.dV), GL[1])     # gamma^{cd} dV_cd gamma_b
        gbgcd = np.einsum('bst,tu->bsu', GL[1], np.einsum('cdst,cd->st', GUP[2], c.dV))
        s.Mphi2 = (I / 12) * (gcdgb - 0.5 * gbgcd) * 0.5                           # acts on J eps
        TT = np.einsum('cd,ef->cdef', s.Tu, s.Tu)
        Tud = np.einsum('cd,dx->cx', T, ETAI)          # T_c^d
        m3 = -np.einsum('bcdefst,cdef->bst', GL[5], TT) + 8 * np.einsum('cst,cd,bd->bst', GUP[1], Tud, T) - 2 * s.T2 * GL[1]
        s.Mphi3 = I * m3
        s.MphiS = (I / 3) * (8 * np.einsum('cst,bc->bst', GUP[1], T) - np.einsum('bst,tu->bsu', GL[1], s.gT))
        # R05 pieces
        g4 = np.einsum('abcdst,cx,dy->abxyst', GL[4], ETAI, ETAI)                 # gamma_ab^{cd}
        t1 = np.einsum('abcdst,cd->abst', g4, c.dV)
        gcd_dV = np.einsum('cdst,cd->st', GUP[2], c.dV)
        t2 = np.einsum('st,abtu->absu', gcd_dV, GL[2]); t3 = np.einsum('abst,tu->absu', GL[2], gcd_dV)
        s.MRQv = (1 / 6) * (t1 - t2 - 0.5 * t3) * (-0.5)                            # acts on J eps
        Cwu = np.einsum('abcd,cx,dy->abxy', c.Cw, ETAI, ETAI)
        s.MRQm = 0.25 * np.einsum('abcd,cdst->abst', Cwu, GL[2])
        Tud_ = np.einsum('ac,cx->ax', T, ETAI)            # T_a^c
        x = np.einsum('ac,bcst->abst', Tud_, GL[2])        # T_a^c gamma_bc
        s.MRQs = -8 * np.einsum('ab,st->abst', T, np.eye(4)) + (16 / 3) * 0.5 * (x - np.swapaxes(x, 0, 1)) \
            + (4 / 3) * np.einsum('abcdst,cd->abst', GL[4], s.Tu)
        # chi (W03)
        s.Mchi = 0.25 * c.B.Dscal * np.eye(4) - 0.25 * np.einsum('abcdst,ab,cd->st', GUP[4], T, T) + s.T2 / 6 * np.eye(4)
        s.Mchiv = -(1 / 64) * np.einsum('abst,ab->st', GUP[2], c.dV) * 0.5          # acts on J eps
        # Dpsi (SC7D-11)
        X = s.gG / 4 - s.gT
        s.MDpsi = I * np.einsum('st,tu,buv->bsv', X, s.gT, GL[1])
        s.MDpsiJ = -(I * g / 2) * (L / s2) * np.einsum('st,btu->bsu', s.gT, GL[1])
        s.MDpsiS = -I * np.einsum('st,btu->bsu', X, GL[1])
        s.MDpsiSJ = (I * g / 2) * (L / s2) * GL[1]
        s.gTgb = np.einsum('st,btu->bsu', s.gT, GL[1])

    # ---- fermion variations, bosonic order
    def dQ_dil(s, E):
        c = s.c; return gm(-s.gG / 4 + s.gT, E) + su2(JM, E) * (c.g * c.L / (2 * s2))
    def dS_dil(s, Hh): return Hh
    def dQ_varphi(s, E):
        c = s.c; return E * (c.N / 2) - gm(s.gT, su2(JM, E)) * (c.L / s2)
    def dS_varphi(s, Hh): return su2(JM, Hh) * (3 * s.c.L / s2)
    def dQ_chi(s, E): return gm(s.Mchi, E) + gm(s.Mchiv, su2(JM, E))
    def dS_chi(s, Hh): return gm(s.gT, Hh) * 0.25
    def dQ_phi(s, E): return _b(s.Mphi1, E) + _b(s.Mphi2, su2(JM, E)) + _b(s.Mphi3, E)
    def dS_phi(s, Hh): return _b(s.MphiS, Hh)
    def dQ_RQ(s, E): return _ab(s.MRQv, su2(JM, E)) + _ab(s.MRQm, E)
    def dS_RQ(s, Hh): return _ab(s.MRQs, Hh)
    def soft(s, E):
        """i gamma.T gamma_b eps  (delta psi_b - D_b eps), new axis b"""
        return _b(I * s.gTgb, E)
    def dQ_Dpsi(s, E): return _b(s.MDpsi, E) + _b(s.MDpsiJ, su2(JM, E)) - s.dQ_phi(E)
    def dS_Dpsi(s, Hh): return _b(s.MDpsiS, Hh) + _b(s.MDpsiSJ, su2(JM, Hh)) - s.dS_phi(Hh)
    def dQ_Dvarphi(s, E):
        # -delta_Q(i g.T g_b eps) varphi - delta_S(delta_Q phi_b) varphi ; the parameter carries the new axis b
        return -s.dQ_varphi(s.soft(E)) - s.dS_varphi(s.dQ_phi(E))
    def dS_Dvarphi(s, Hh):
        return -s.dQ_varphi(_b(-I * GL[1], Hh)) - s.dS_varphi(s.dS_phi(Hh))

def fermion_derivatives(c, o, v):
    """adds D R^(Q), R^(S), D D psi, Box psi, D chi (rule and SC7-17), D D varphi, Box varphi to o"""
    psi, ph = o['psi'], o['phi_mu']
    o['DRQ'] = c.nab(o['RQ']) - v.dQ_RQ(psi) - v.dS_RQ(ph)                          # [c, a, b]
    o['DDpsi'] = c.nab(o['Dpsi']) - v.dQ_Dpsi(psi) - v.dS_Dpsi(ph)                  # [a, b]
    o['boxpsi'] = ein('ab,abisn->isn', ETAI, o['DDpsi'])
    o['Dchi'] = c.nab(o['chi']) - v.dQ_chi(psi) - v.dS_chi(ph)
    Hg = np.einsum('ab,abst->st', c.H, GUP[2])
    o['Dchi_SC717'] = ein('ast,caitn->cisn', GUP[1], o['DDpsi']) * (I / 8) - gm(Hg, o['Dpsi']) / 16 \
        - su2(JM, o['Dpsi']) * (c.g / 16 * c.L / s2) + o['Dvarphi'] * (c.g / 8)
    f = c.f
    fgam = np.einsum('ac,cx,xbst->abst', f, ETAI, GL[2])                          # f_a^c gamma_cb
    o['DDvarphi'] = c.nab(o['Dvarphi']) - v.dQ_Dvarphi(psi) - v.dS_Dvarphi(ph) \
        + ein('ab,isn->abisn', 7 * f, o['varphi']) - ein('abst,itn->abisn', fgam, o['varphi'])
    o['boxvarphi'] = ein('ab,abisn->isn', ETAI, o['DDvarphi'])
    # R^_ab(S), R06b
    DRQ, RQ, T, Tu = o['DRQ'], o['RQ'], c.T, v.Tu
    t = -I * ein('cst,cabitn->abisn', GUP[1], DRQ)
    divR = ein('cx,cbxisn->bisn', ETAI, DRQ)                                      # D^c R_bc
    x = ein('ast,bitn->abisn', GL[1], divR); t = t - (I / 2) * (x - x.ap(lambda q: np.swapaxes(q, 0, 1)))
    TR = ein('cd,cdisn->isn', Tu, RQ)
    t = t - (8 / 3) * ein('abst,itn->abisn', GL[2], TR)
    M12 = 12 * np.einsum('est,ce->cst', GL[1], Tu)                                  # 12 gamma_e T^{ce}
    y = ein('ast,bcitn->abcisn', GL[1], RQ)                                         # gamma_a R_bc
    y = ein('cst,abcitn->abisn', M12, y); t = t + 0.5 * (y - y.ap(lambda q: np.swapaxes(q, 0, 1)))
    t = t - 3 * gm(c.gT, RQ)
    Tc_a = np.einsum('xa,xc->ca', T, ETAI)                                         # T^c_a
    z = ein('ca,bcisn->abisn', Tc_a, RQ); t = t - 8 * 0.5 * (z - z.ap(lambda q: np.swapaxes(q, 0, 1)))
    o['RS'] = t
    return o
