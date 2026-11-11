"""Two-fermion parts of the bosonic supercovariant objects at the background (K-arrays, frame indices lower).

From the component reference (the repository component reference plus the item-25 H02 overlay), at the gauge sigma=1, psi^i=0, b=0:
  G^_ab   = G_ab + (i/2) psibar_[a psi_b]                                  (SC7-05)
  H^_abc  = H_abc - (3/4) psibar_[a gamma_b psi_c],  H^_ab = -(1/12) eps_abcde H^^cde
  T       = (G^ - 2 H^)/8                                                    (SC7-08)
  omega   = omega(e) + (1/2) psibar^[a gamma^b] psi_mu + (1/4) psibar^a gamma_mu psi^b           (R01)
  R'(M)   = R(omega) + i phibar_[mu g^ab psi_nu] + i psibar_[mu g^[a g.T g^b] psi_nu] + psibar_[mu g^[a R_nu]^b](Q)
            + (1/2) psibar_[mu g_nu] R^ab(Q) + 8 psibar_[mu e_nu]^[a g^b] chi                     (R03)
  Ric_cd  = R'_{cb d}^b (ordered), f_cd = -Ric_cd/6 + eta_cd Ric/48, C^ = R'(M) + 8 f_[c^[a delta_d]^b]
  Box sigma = -Ric/8 - (i/2) psibar_a D^a psi - (i/4) psibar_a g^a g^b D_b psi - (g/4) psibar_a g^a varphi   (SC7D-07)
  D_a D_b sigma = 2 f_ab - (i/2) psibar_a D_b psi - 2 psibar_a g_b chi                                    (SC7D-06)
  D       = Box sigma/4 + (5/96) G^2 + (1/24) G.H - (13/24) H^2 + (g/4) N + (g^2/16) L^2                  (SC7-10)
  R^(V)_ab^ij = (1/2) delta^ij (dV)_ab - 3i phibar_[a^(i psi_b]^j) - 8 psibar_[a^(i g_b] chi^j) - i psibar_[a^(i g.T psi_b]^j)  (R02)"""
import numpy as np
from ferm2 import Lin, ein, gm, su2, kb, bl, GL, GUP, ETA, ETAI, EPS_LOW, NW, DL, JM, CC, I, s2

def asym2(K, a=0, b=1):
    """unit-weight antisymmetrisation of two axes of an array"""
    return 0.5 * (K - np.swapaxes(K, a, b))

def even_objects(c, o):
    """two-fermion parts; o = base_objects(c).  Returns dict of K-arrays."""
    e = {}
    psi, ph, RQ, d, chi, vphi = o['psi'], o['phi_mu'], o['RQ'], o['Dpsi'], o['chi'], o['varphi']
    g = c.g
    # G^ and H^
    e['G'] = asym2(bl(psi, 'a', psi, 'b', out='ab')) * (I / 2)
    H3 = bl(psi, 'a', psi, 'c', G=GL[1], gf='b', out='abc') * (-0.75)
    H3 = sum(np.sign(np.linalg.det(np.eye(3)[list(p)])) * np.transpose(H3, tuple(p) + (3, 4))
             for p in __import__('itertools').permutations(range(3))) / 6
    e['H3'] = H3
    H3u = np.einsum('cdemn,cx,dy,ez->xyzmn', H3, ETAI, ETAI, ETAI)
    e['H'] = -np.einsum('abcde,cdemn->abmn', EPS_LOW, H3u) / 12
    e['T'] = (e['G'] - 2 * e['H']) / 8
    # torsion of omega: omega^(2)_{d ab} (lower)
    om = (bl(psi, 'a', psi, 'd', G=GL[1], gf='b', out='dab') - bl(psi, 'b', psi, 'd', G=GL[1], gf='a', out='dab')) * 0.25 \
        + bl(psi, 'a', psi, 'b', G=GL[1], gf='d', out='dab') * 0.25
    e['omega'] = om
    # R(omega)^(2)_{cd ab} = nabla_c om_d - nabla_d om_c (tangent, torsion free frame)
    nom = c.nabK(om, 3)                                          # [c, d, a, b]
    Rom = nom - np.swapaxes(nom, 0, 1)
    # B^(2)
    gTm = c.gT
    gaTgb = np.einsum('ast,tu,buv->absv', GUP[1], gTm, GUP[1])   # gamma^a gamma.T gamma^b
    gaTgb = 0.5 * (gaTgb - np.swapaxes(gaTgb, 0, 1))
    gaTgb_l = np.einsum('abst,ax,by->xyst', gaTgb, ETA, ETA)     # lower a,b
    RQu = RQ                                                     # R^_{d b} lower; R_d^b raised below with eta
    Bm = bl(ph, 'c', psi, 'd', G=GL[2], gf='ab', out='cdab') * I
    Bm = Bm + bl(psi, 'c', psi, 'd', G=gaTgb_l, gf='ab', out='cdab') * I
    Bm = Bm + bl(psi, 'c', RQ, 'db', G=GL[1], gf='a', out='cdab')
    Bm = Bm + bl(psi, 'c', RQ, 'ab', G=GL[1], gf='d', out='cdab') * 0.5
    # 8 psibar_[c e_d]^[a gamma^b] chi : delta_d^a  -> lower: eta_da
    t = bl(psi, 'c', chi, '', G=GL[1], gf='b', out='cb')
    Bm = Bm + 8 * np.einsum('cbmn,da->cdabmn', t, ETA)
    # antisymmetrise in [ab] then in [cd]
    Bm = asym2(asym2(Bm, 2, 3), 0, 1)
    # note: the first two terms are already antisymmetric in ab (gamma^{ab}, g^[a T g^b]); asym2 is harmless
    e['B'] = Bm
    Rp = Rom + Bm
    e["R'M"] = Rp
    Ric = np.einsum('cbdxmn,bx->cdmn', Rp, ETAI)                # Ric_cd = R'_{cb d}^b (ordered)
    e['Ric'] = Ric
    Rs = np.einsum('cdmn,cd->mn', Ric, ETAI)
    e['Rs'] = Rs
    f = -Ric / 6 + np.einsum('cd,mn->cdmn', ETA, Rs) / 48
    e['f'] = f
    add = 2 * (np.einsum('camn,db->cdabmn', f, ETA) - np.einsum('cbmn,da->cdabmn', f, ETA)
               - np.einsum('damn,cb->cdabmn', f, ETA) + np.einsum('dbmn,ca->cdabmn', f, ETA))
    e['C'] = Rp + add
    # sigma derivatives
    trf = np.einsum('cdmn,cd->mn', f, ETAI)
    DDs = 2 * f - bl(psi, 'a', d, 'b', out='ab') * (I / 2) - 2 * bl(psi, 'a', chi, '', G=GL[1], gf='b', out='ab')
    e['DDsigma'] = DDs
    e['boxsigma'] = np.einsum('abmn,ab->mn', DDs, ETAI)
    # D
    up2 = lambda X: np.einsum('ab,ax,by->xy', X, ETAI, ETAI)
    dot = lambda X0, K: np.einsum('ab,abmn->mn', up2(X0), K)
    e['D'] = e['boxsigma'] / 4 + 5 / 48 * dot(c.G, e['G']) + (dot(c.H, e['G']) + dot(c.G, e['H'])) / 24 - 13 / 12 * dot(c.H, e['H'])
    # R^(V)^(2)_{ab}^{ij} (free SU(2) indices, symmetrised)
    def sym_ij(X, xf, Y, yf, G=None, gf='', out=''):
        ops = [(CC, 'su'), (G, gf + 'ut') if G is not None else (np.eye(4, dtype=complex), 'ut')]
        K = kb(X, xf + 'is', Y, yf + 'jt', ops, out + 'ij')
        return 0.5 * (K + np.swapaxes(K, -4, -3))
    RV = -3 * I * sym_ij(ph, 'a', psi, 'b', out='ab') - 8 * sym_ij(psi, 'a', chi, '', G=GL[1], gf='b', out='ab') \
        - I * sym_ij(psi, 'a', psi, 'b', G=c.gT, out='ab')
    e['RV'] = asym2(RV, 0, 1)
    return e
