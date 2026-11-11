"""Background tensors of the supersymmetric AdS3 x Sigma2 solution (tau = +1 branch) in the frame of the product-background
engine, in the conventions of GB-FINAL-DENSITY (GB02-GB04, SC7-05/06/10, R03).

Frame: E_0=(z/l)d_t, E_1=(z/l)d_x, E_2=(z/l)d_z, E_3=w y d_y1, E_4=w y d_y2, with [E_2,E_0]=E_0/l, [E_2,E_1]=E_1/l,
[E_4,E_3]=w E_3.  eta = diag(-1,1,1,1,1), epsilon^{01234} = +1, epsilon_{01234} = -1.
Everything is numeric (numpy complex128); tensors are stored with ALL FRAME INDICES LOWER and SU(2) indices UPPER.
Usage: from bgfields import Background; B = Background(L, k, g=1)."""
import itertools
import numpy as np
import sympy as sp
from background import background as bg_exact

ETA = np.diag([-1., 1, 1, 1, 1])
EPS2 = np.array([[0., 1], [-1, 0]])          # epsilon_{ij} = epsilon^{ij}, eps_12 = 1

def perm_sign(p):
    p = list(p); s = 1
    for i in range(len(p)):
        for j in range(i + 1, len(p)):
            if p[i] > p[j]: s = -s
    return s

EPS_LOW = np.zeros((5,) * 5)                  # epsilon_{abcde}, epsilon_{01234} = -1
for p in itertools.permutations(range(5)): EPS_LOW[p] = -perm_sign(p)

class Background:
    def __init__(s, L, k, g=1, geom=None, bgdict=None):
        b = bg_exact(sp.Rational(L), sp.Rational(k), g) if bgdict is None else dict(bgdict)
        if geom is not None:                       # override the geometry (l, w) for off-shell tests
            b = dict(b); b['l'], b['w'] = geom; b['v'] = -geom[1] ** 2
        f = lambda x: complex(sp.N(sp.sympify(str(x)), 30))
        s.exact = b
        s.L, s.N, s.p, s.h, s.r, s.v = [f(b[x]) for x in ('L', 'N', 'p', 'h', 'r', 'v')]
        s.l, s.w, s.g = f(b['l']), f(b['w']), f(g)
        s.k = complex(sp.Rational(k)); s.chi = b['chi']
        l, w = s.l, s.w
        # structure constants C[c,a,b]: [E_a,E_b] = C^c_ab E_c
        C = np.zeros((5, 5, 5), complex)
        C[0, 2, 0] = 1 / l; C[0, 0, 2] = -1 / l; C[1, 2, 1] = 1 / l; C[1, 1, 2] = -1 / l; C[3, 4, 3] = w; C[3, 3, 4] = -w
        s.C = C
        Cl = np.einsum('cd,dab->cab', ETA, C)                                   # C_{c ab}
        Gl = (Cl - np.einsum('bac->cab', Cl) - np.einsum('abc->cab', Cl)) / 2      # Gamma_{c a b}
        s.Gam = np.einsum('cd,dab->cab', ETA, Gl)                                  # Gamma^c_{ab}: nabla_a E_b = Gam^c_ab E_c
        # spin connection omega_a^{cd} = Gamma^c_{a e} eta^{ed}
        s.om = np.einsum('cae,ed->acd', s.Gam, ETA)
        # Riemann R_ab^{cd} = -C^e_ab om_e^{cd} + om_a^{ce} om_b,e^{d} - (a<->b)   (constant frame components)
        omL = np.einsum('ace,ef->acf', s.om, ETA)                                  # om_a^c_f (second index lowered)
        R = -np.einsum('eab,ecd->abcd', C, s.om) + np.einsum('ace,bed->abcd', omL, s.om) - np.einsum('bce,aed->abcd', omL, s.om)
        s.Riem_ud = R                                                              # R_ab^{cd}
        s.Riem = np.einsum('abcd,ce,df->abef', R, ETA, ETA)                        # R_abcd
        s.Ric = np.einsum('abcb->ac', np.einsum('abcd,df->abcf', np.einsum('abcd,ce->abed', R, ETA), np.eye(5)))  # R_{a b c}^{b}
        s.Ric = np.einsum('abcd,db->ac', np.einsum('abcd,ce->abed', R, ETA), np.eye(5))
        s.Rs = np.einsum('ab,ab->', np.linalg.inv(ETA), s.Ric)
        s.f = -s.Ric / 6 + ETA * s.Rs / 48                                         # f_ab (SC7-06)
        fu = np.einsum('ab,bc->ac', s.f, np.linalg.inv(ETA))                       # f_a^c
        I5 = np.eye(5)
        add = 2 * (np.einsum('ac,bd->abcd', fu, I5) - np.einsum('ad,bc->abcd', fu, I5)
                   - np.einsum('bc,ad->abcd', fu, I5) + np.einsum('bd,ac->abcd', fu, I5))   # 8 f_[a^[c delta_b]^d]
        s.Cw = np.einsum('abcd,ce,df->abef', R + add, ETA, ETA)                    # C^_abcd (all lower)
        # forms
        G = np.zeros((5, 5), complex); G[3, 4] = s.p; G[4, 3] = -s.p
        H3 = np.zeros((5, 5, 5), complex)
        for p_ in itertools.permutations((0, 1, 2)): H3[p_] = perm_sign(p_) * (-2 * s.h)      # H_{abc}, H_012 = -2h
        H3u = np.einsum('abc,ad,be,cf->def', H3, ETA, ETA, ETA)
        Hd = -np.einsum('abcde,cde->ab', EPS_LOW, H3u) / 12                         # H_ab = -(1/12) eps_abcde H^cde
        s.G, s.H = G, Hd
        s.T = (G - 2 * Hd) / 8
        Ginv = np.linalg.inv(ETA)
        up2 = lambda X: np.einsum('ab,ac,bd->cd', X, Ginv, Ginv)
        s.G2 = np.einsum('ab,ab->', s.G, up2(s.G)); s.H2 = np.einsum('ab,ab->', s.H, up2(s.H)); s.GH = np.einsum('ab,ab->', s.G, up2(s.H))
        s.T2 = np.einsum('ab,ab->', s.T, up2(s.T))
        # R(V)_ab^{ij} = (1/2) delta^{ij} (dV)_ab,  (dV)_34 = r
        dV = np.zeros((5, 5), complex); dV[3, 4] = s.r; dV[4, 3] = -s.r
        s.RV = 0.5 * np.einsum('ab,ij->abij', dV, np.eye(2))
        s.Lij = s.L / np.sqrt(2) * np.eye(2)                                       # L^{ij}
        Ca = np.zeros(5, complex); Ca[3] = s.p / w if w != 0 else np.nan; s.Ca = Ca
        s.boxsigma = 2 * np.trace(np.einsum('ab,bc->ac', s.f, Ginv))               # 2 f_a^a
        LL = np.einsum('ij,kl,ki,lj->', s.Lij, s.Lij, EPS2, EPS2)                  # L^{ij} L_{ij}
        s.LL = LL
        s.Dscal = s.boxsigma / 4 + 5 / 96 * s.G2 + s.GH / 24 - 13 / 24 * s.H2 + s.g / 4 * s.N + s.g ** 2 / 16 * LL
        s._checks()

    def _checks(s):
        Ginv = np.linalg.inv(ETA)
        # torsion free and metric
        assert np.allclose(s.Gam - np.einsum('cba->cab', s.Gam), s.C)
        # Weyl tensor traceless: C_{a b c}^{b} = 0 -> C_abcd eta^{bd}
        assert np.allclose(np.einsum('abcd,bd->ac', s.Cw, Ginv), 0), 'Weyl tensor not traceless'
        # curvature of the factors: R_{01}^{01} = -1/l^2 (AdS3), R_{34}^{34} = v (Sigma2)
        assert np.isclose(s.Riem_ud[0, 1, 0, 1], -1 / s.l ** 2), s.Riem_ud[0, 1, 0, 1]
        assert np.isclose(s.Riem_ud[3, 4, 3, 4], s.v), (s.Riem_ud[3, 4, 3, 4], s.v)
        assert np.isclose(s.Rs, -6 / s.l ** 2 + 2 * s.v)
        assert np.isclose(s.Riem_ud[3, 4, 3, 4], -s.w ** 2)

