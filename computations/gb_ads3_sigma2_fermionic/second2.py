"""Two-fermion parts of second and third derivatives of bosonic covariants (milestone 2b).

(D_x D_y Phi)^(2) = nabla_x (D_y Phi)^(2) - XiQ_{D_y Phi}(psi_x) - XiS_{D_y Phi}(phi_x) + K[f, Phi]^(2)
with the brute-force variations of Brute.vary_first.  Third derivatives of sigma use the Hessian variation
(Xi_{D sigma} with delta f: + 2 delta f_xy, tested by test_D.py); D_c X with X = D D sigma has the torsion term on
X^0 = 2 f^0.  Box D^c H^_ac = Box V_a with V_a = -(1/16)(eps G^ G^)_a + (g/2) E^_a (H03 gauged); E^ is the
supercovariant constrained vector, primary of weight 4 with delta E_a = -(i/2) epsbar g_ab D^b varphi
- 2 epsbar g^b varphi T_ba - 2 etabar g_a varphi (L01)."""
import numpy as np
from ferm2 import Lin, ein, bl, GL, GUP, ETA, ETAI, EPS_LOW, EPS2, I, s2
from bderiv2 import BVar, CurvVar, Brute, first_derivatives, antisym

class Second:
    def __init__(s, c, o, e, v):
        s.c, s.o, s.e, s.v = c, o, e, v
        s.bv = BVar(c, o, e, v); s.cv = CurvVar(s.bv); s.br = Brute(s.bv, s.cv)
        s.d1 = first_derivatives(s.bv)
    def _second(s, first, nown, Xi, Sg, Phi0, X2, w):
        c, o, bv, br = s.c, s.o, s.bv, s.br
        t = c.nabK(first, 1 + nown)
        t = t - br.vary_first(Xi, Sg, Phi0, w, nown, o['psi'], 'x', 'Q')
        t = t - br.vary_first(Xi, Sg, Phi0, w, nown, o['phi_mu'], 'x', 'S')
        t = t + bv.Kterm(Phi0, X2, w, nown)
        return t
    def DDG(s):
        c, e, br = s.c, s.e, s.br
        return s._second(s.d1['DG'], 2, br.Xi_G, br.Sg_G, c.G, e['G'], 2)
    def DDHd(s):
        c, e, br = s.c, s.e, s.br
        return s._second(s.d1['DHd'], 2, br.Xi_Hd, br.Sg_Hd, c.H, e['H'], 3)
    def DDN(s):
        c, br = s.c, s.br
        zero = np.zeros((c.Nb, c.Na), complex)
        return s._second(s.d1['DN'], 0, br.Xi_N, br.Sg_N, np.array(c.N, dtype=complex), zero, 4)
    def DDL(s):
        """(D_x D_y L^{ij})^(2): axes x, y, i, j (SU(2) upper).  L weight 3, U(1)_R charged."""
        c, o, bv, br, v = s.c, s.o, s.bv, s.br, s.v
        first = s.d1['DL']                                                     # [y, i, j, m, n]
        t = c.nabK(first, 1)
        # U(1)_R connection on the SU(2) indices: D_mu X^{ij} contains + 2 V_mu^(i_k X^j)k, V^i_k = (1/2) V eps_ik
        Vt = 0.5 * np.einsum('x,ik,yjkmn->xyijmn', c.V, EPS2, first)
        t = t + Vt + np.swapaxes(Vt, 2, 3)
        L0 = c.Lij
        for kind, E in (('Q', o['psi']), ('S', o['phi_mu'])):
            if kind == 'Q':
                tt = br.Xi_L(E, 'x', br.Fnab, 'y')
                tt = tt - br.Xi_L(v.soft(E), 'x' + 'y', br.F0)
                FQ = br.FQ(E)
                tt = tt - np.transpose(br.Xi_L(o['psi'], 'y', FQ, 'x'), (1, 0, 2, 3, 4, 5))
                db = bv.db_Q(E, 'x'); dV = s.dV_Q(E, 'x')
            else:
                tt = -br.Xi_L(ein('bst,...itn->...bisn', -I * GL[1], E), 'x' + 'y', br.F0)
                FS = br.FS(E)
                tt = tt - np.transpose(br.Xi_L(o['psi'], 'y', FS, 'x'), (1, 0, 2, 3, 4, 5))
                db = bv.db_S(E, 'x'); dV = s.dV_S(E, 'x')
            tt = tt - 3 * np.einsum('xymn,ij->xyijmn', db, L0)
            # + 2 delta V^(i_k L^j)k with delta V^i_k = delta V^{il} eps_lk
            dVm = np.einsum('xyilmn,lk->xyikmn', dV, EPS2)
            u = np.einsum('xyikmn,jk->xyijmn', dVm, L0)
            tt = tt + u + np.swapaxes(u, 2, 3)
            t = t - tt
        t = t + 2 * 3 * np.einsum('xymn,ij->xyijmn', s.e['f'], L0)
        return t
    def dV_Q(s, E, ef):
        o = s.o
        from bderiv2 import sym_ij
        t = -1.5 * I * sym_ij(E, ef, o['phi_mu'], 'b', out=ef + 'b') + 4 * sym_ij(E, ef, o['chi'], '', G=GL[1], gf='b', out=ef + 'b')
        return t + I * sym_ij(E, ef, o['psi'], 'b', G=s.c.gT, out=ef + 'b')
    def dV_S(s, E, ef):
        from bderiv2 import sym_ij
        return 1.5 * I * sym_ij(E, ef, s.o['psi'], 'b', out=ef + 'b')
    # ---- sigma: Hessian and third derivatives
    def _Kf(s, E, ef, kind):
        dR = s.cv.dRp_Q(E, ef) if kind == 'Q' else s.cv.dRp_S(E, ef)
        return 2 * CurvVar.ricci_f_C(dR)[1]
    def DDDs(s):
        """(D_z D_x D_y sigma)^(2): axes z, x, y"""
        c, o, e, br = s.c, s.o, s.e, s.br
        X2 = e['DDsigma']; X0 = 2 * c.f
        t = c.nabK(X2, 2)
        omm = np.einsum('cdxmn,xe->cdemn', e['omega'], ETAI)
        t = t + np.einsum('zxemn,ey->zxymn', omm, X0) + np.einsum('zyemn,xe->zxymn', omm, X0)
        # variations of X = D_x D_y sigma, parameter psi_z / phi_z: Brute.vary_first on Phi = D_y sigma with outer x
        def XiX(kind, E, ef):
            return br.vary_first(br.Xi_Ds, br.Sg_Ds, None, 0, 1, E, ef, kind, Kterm=s._Kf)
        t = t - XiX('Q', o['psi'], 'z') - XiX('S', o['phi_mu'], 'z')
        return t
    # ---- E^ and Box V
    def Ehat2(s):
        c, e, d = s.c, s.e, s.d1
        V2 = np.einsum('cabmn,cb->amn', d['DHd'], ETAI)                       # D^c H^_ac  (index order: D_c H_ab, b=c)
        Gu = np.einsum('ab,ax,by->xy', c.G, ETAI, ETAI)
        G2u = np.einsum('abmn,ax,by->xymn', e['G'], ETAI, ETAI)
        eGG2 = 2 * np.einsum('abcde,bc,demn->amn', EPS_LOW, Gu, G2u)
        return (V2 + eGG2 / 16) * (2 / c.g), V2
    def Xi_E(s, E, ef, F, xb=''):
        c = s.c
        Tl = c.T
        t = bl(E, ef, F['Dvarphi'], xb + 'b', G=np.einsum('abst,bx->axst', GL[2], ETAI), gf='pb', out=ef + xb + 'p') * (-I / 2)
        Mb = np.einsum('bst,bx,xa->ast', GL[1], ETAI, Tl)                      # gamma^b T_ba
        return t - 2 * bl(E, ef, F['varphi'], xb, G=Mb, gf='p', out=ef + xb + 'p')
    def Sg_E(s, E, ef, F, xb=''):
        return -2 * bl(E, ef, F['varphi'], xb, G=GL[1], gf='p', out=ef + xb + 'p')
    def DE_box(s):
        """(D_y E^_p)^(2) and (Box E^_p)^(2)"""
        c, o, br, bv = s.c, s.o, s.br, s.bv
        E2, V2 = s.Ehat2()
        first = c.nabK(E2, 1) - s.Xi_E(o['psi'], 'c', br.F0) - s.Sg_E(o['phi_mu'], 'c', br.F0)     # [c, p]
        sec = c.nabK(first, 2)
        sec = sec - br.vary_first(s.Xi_E, s.Sg_E, None, 4, 1, o['psi'], 'x', 'Q')
        sec = sec - br.vary_first(s.Xi_E, s.Sg_E, None, 4, 1, o['phi_mu'], 'x', 'S')
        sec = sec + bv.Kterm(np.zeros(5, complex), E2, 4, 1)
        box = np.einsum('xypmn,xy->pmn', sec, ETAI)
        div = np.einsum('cpmn,cp->mn', first, ETAI)
        return first, box, div, E2
