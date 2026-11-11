"""Quadratic fermion operator of the lambda_GB block (milestone 2b/3): evaluate every parsed term.

Bilinear terms (two odd factors): spinor chain  bar(X) Gamma_1 ... Gamma_n Y  with the background values of all
bosonic factors (evalbg semantics), K = X_B^T C Gamma Y_A - (X_A^T C Gamma Y_B)^T.
Bosonic-form terms: sum over factors of (factor)^(2) x (other factors)^0, derivatives of single-product groups
expanded by the Leibniz rule first.  The two odd D(group) terms C_a D_b(bilinear^{ab}) (term 17) use the full
supercovariant derivative of the bilinear by the Leibniz rule, with the linear-order D R^(Q) and D chi: its Q/S
connection terms -delta_Q(psi_b), -delta_S(phi_b) are of second order in the fermions and are kept (the first version
used nabla_b of the bilinear and called these terms cubic, which is wrong; that rule is behind LEGACY_NABLA).
Usage: K = KGB(ctx) -> (Nb, Na) array."""
import itertools
import numpy as np
from fractions import Fraction
import evalbg
from evalbg import Evaluator, Ten, has_odd, unwrap, canon_idx
from ferm2 import Lin, ETA, ETAI, EPS2, EPS_LOW, CC, GL, I, s2, bl, ein, kb
from objects2 import even_objects
from deriv2 import Var, fermion_derivatives
from second2 import Second
from bderiv2 import CurvVar, sym_ij
from ferm2 import base_objects

SU2 = set('ijkl')

def chain_sig(f):
    """('D', chain, tgt) -> (signature string, derivative letters with positions)"""
    sig = ''; lets = []
    for c_ in f[1]:
        if c_ == 'box': sig += 'B'
        else: sig += 'd'; lets.append(c_)
    return sig, lets

def leibniz(terms):
    """expand derivatives of single-product groups (bosonic and odd) into derivatives of atoms"""
    out = []
    for t in terms:
        stack = [(t['coef'], [])]
        for f in t['factors']:
            g = unwrap(f)
            if g[0] == 'D' and unwrap(g[2])[0] == 'grp' and not has_odd(g):
                grp = unwrap(g[2])[1]; assert len(grp) == 1
                sub = grp[0]; fl = [unwrap(x) for x in sub['factors']]
                alts = []
                for k in range(len(fl)):
                    fk = fl[k]
                    if fk[0] == 'T': dk = ('D', list(g[1]), fk)
                    elif fk[0] == 'D': dk = ('D', list(g[1]) + list(fk[1]), fk[2])
                    else: raise ValueError(fk)
                    alts.append((sub['coef'], fl[:k] + [dk] + fl[k + 1:]))
                stack = [(evalbg._mul_coef(c0, c1), fl0 + fl1) for c0, fl0 in stack for c1, fl1 in alts]
            else:
                stack = [(c0, fl0 + [g]) for c0, fl0 in stack]
        out += [dict(coef=c0, factors=fl0) for c0, fl0 in stack]
    return out

LEGACY_NABLA = False

class Engine:
    def __init__(s, c):
        s.c = c
        o = base_objects(c); v = Var(c, o); fermion_derivatives(c, o, v); e = even_objects(c, o)
        s.o, s.v, s.e = o, v, e
        S = Second(c, o, e, v); s.S = S; br = S.br; bv = S.bv; s.br, s.bv = br, bv
        s.ev = Evaluator(c.B)
        d1 = S.d1
        # ---- odd objects: name/signature -> Lin (frame axes: derivative letters, then target letters)
        zero0 = Lin(np.zeros((2, 4, c.Na), complex), np.zeros((2, 4, c.Nb), complex))
        s.odd = {('', 'grav'): o['psi'], ('', 'dil'): zero0, ('d', 'dil'): o['Dpsi'], ('dd', 'dil'): o['DDpsi'],
                 ('B', 'dil'): o['boxpsi'], ('', 'RQ'): o['RQ'], ('d', 'RQ'): o['DRQ'], ('', 'varphi'): o['varphi'],
                 ('d', 'varphi'): o['Dvarphi'], ('B', 'varphi'): o['boxvarphi'], ('', 'chi'): o['chi'], ('d', 'chi'): o['Dchi']}
        # ---- even two-fermion parts
        G0, H0, T0 = c.G, c.H, c.T
        up2 = lambda X: np.einsum('ab,ax,by->xy', X, ETAI, ETAI)
        ev = {}
        ev[('', 'G^')] = e['G']; ev[('', 'H^')] = e['H']; ev[('', 'T')] = e['T']; ev[('', 'C^')] = e['C']
        ev[('', 'D')] = e['D']; ev[('', 'RV')] = e['RV']
        ev[('', 'G2')] = 2 * np.einsum('ab,abmn->mn', up2(G0), e['G']); ev[('', 'T2')] = 2 * np.einsum('ab,abmn->mn', up2(T0), e['T'])
        ev[('d', 'G^')] = d1['DG']; ev[('d', 'H^')] = d1['DHd']; ev[('d', 'T')] = d1['DT']; ev[('d', 'L')] = d1['DL']
        ev[('d', 'N')] = d1['DN']
        ev[('d', 'D')] = bv.first(e['D'], np.array(c.B.Dscal), 0, bv.XiQ_D, bv.XiS_D)
        cv = S.cv
        # (parameter letters renamed: CurvVar uses c, d, a, b, e internally; only the axis order matters)
        XiC = lambda E, ef: CurvVar.ricci_f_C(cv.dRp_Q(E, 'zwv'[:len(ef)]))[2]
        SgC = lambda E, ef: CurvVar.ricci_f_C(cv.dRp_S(E, 'zwv'[:len(ef)]))[2]
        ev[('d', 'C^')] = bv.first(e['C'], c.Cw, 4, XiC, SgC)
        ev[('d', 'RV')] = s.DRV()
        DDG = S.DDG(); DDH = S.DDHd()
        ev[('dd', 'G^')] = DDG; ev[('dd', 'H^')] = DDH
        ev[('B', 'G^')] = np.einsum('xyabmn,xy->abmn', DDG, ETAI); ev[('B', 'H^')] = np.einsum('xyabmn,xy->abmn', DDH, ETAI)
        def Xi_T(E, ef, F, xb=''):
            return bl(E, ef, F['chi'], xb, G=GL[2], gf='pq', out=ef + xb + 'pq') * (I / 2) - bl(E, ef, F['RQ'], xb + 'pq', out=ef + xb + 'pq') * (3j / 32)
        ev[('dd', 'T')] = S._second(d1['DT'], 2, Xi_T, None, T0, e['T'], 1)
        DDL = S.DDL(); DDN = S.DDN()
        ev[('B', 'L')] = np.einsum('xyijmn,xy->ijmn', DDL, ETAI); ev[('B', 'N')] = np.einsum('xymn,xy->mn', DDN, ETAI)
        ev[('dd', 'sigma')] = e['DDsigma']; ev[('B', 'sigma')] = e['boxsigma']
        DDDs = S.DDDs()
        ev[('dB', 'sigma')] = np.einsum('zxymn,xy->zmn', DDDs, ETAI)
        ev[('Bd', 'sigma')] = np.einsum('zxymn,zx->ymn', DDDs, ETAI)
        # Box D^c H^_ac = Box V_a, V = -(1/16) eps G^ G^ + (g/2) E^
        first, boxE, div, E2 = S.DE_box()
        BG = ev[('B', 'G^')]
        boxGu0 = up2(s.ev.deriv(['box'], ('T', 'G^', [('d', 'a'), ('d', 'b')])).a)
        Gu = up2(G0); BGu = np.einsum('abmn,ax,by->xymn', BG, ETAI, ETAI); G2u = np.einsum('abmn,ax,by->xymn', e['G'], ETAI, ETAI)
        eps2 = lambda A, B: np.einsum('abcde,bc,demn->amn', EPS_LOW, A, B)
        boxV = -(2 * eps2(Gu, BGu) + 2 * eps2(boxGu0, G2u)) / 16 + (c.g / 2) * boxE
        ev[('Bd', 'H^')] = boxV
        for nm in ('L', 'N', 'C', 'sigma', 'eps'): ev[('', nm)] = None
        ev[('d', 'sigma')] = None
        s.even = ev

    def DRV(s):
        """(D_c R^_ab^{ij}(V))^(2): axes c, a, b, i, j"""
        c, o, e, bv = s.c, s.o, s.e, s.bv
        RV0 = 0.5 * np.einsum('ab,ij->abij', c.dV, np.eye(2))
        t = c.nabK(e['RV'], 3) if False else None
        # nabla on the frame indices of a K-array with trailing SU(2) axes
        K = e['RV']                                            # [a, b, i, j, m, n]
        Km = np.moveaxis(K, (2, 3), (-4, -3))                  # keep as is: frame first
        out = np.einsum('c,abijmn->cabijmn', c.mAB, K)
        out = out - np.einsum('eca,ebijmn->cabijmn', c.Gam, K) - np.einsum('ecb,aeijmn->cabijmn', c.Gam, K)
        # U(1)_R on the SU(2) indices: + 2 V^(i_k X^j)k
        u = 0.5 * np.einsum('c,ik,abjkmn->cabijmn', c.V, EPS2, K); out = out + u + np.swapaxes(u, 3, 4)
        omm = np.einsum('cdxmn,xe->cdemn', e['omega'], ETAI)
        out = out + np.einsum('caemn,ebij->cabijmn', omm, RV0) + np.einsum('cbemn,aeij->cabijmn', omm, RV0)
        psi, ph, RQ, chi, RS = o['psi'], o['phi_mu'], o['RQ'], o['chi'], o['RS']
        Dchi = o['Dchi']
        def XiQ(E, ef):
            t = -1.5 * I * sym_ij(E, ef, RS, 'ab', out=ef + 'ab')
            x = sym_ij(E, ef, Dchi, 'b', G=GL[1], gf='a', out=ef + 'ab'); t = t - 4 * (x - np.swapaxes(x, -6, -5))
            t = t + I * sym_ij(E, ef, RQ, 'ab', G=c.gT, out=ef + 'ab')
            gaTgb = bv.gaTgb
            t = t + 8 * I * sym_ij(E, ef, chi, '', G=gaTgb, gf='ab', out=ef + 'ab')
            return t
        def XiS(E, ef):
            return 1.5 * I * sym_ij(E, ef, RQ, 'ab', out=ef + 'ab') + 8 * I * sym_ij(E, ef, chi, '', G=GL[2], gf='ab', out=ef + 'ab')
        return out - XiQ(psi, 'c') - XiS(ph, 'c')

    # ------------------------------------------------------------------ factor values
    def odd_value(s, f):
        """Lin + list of (letter, kind, pos) for its frame axes and its SU(2) axis"""
        f = unwrap(f)
        if f[0] == 'T':
            name, idx = f[1], f[2]; sig, dl = '', []
        else:
            sig, dl = chain_sig(f); tgt = unwrap(f[2]); name, idx = tgt[1], tgt[2]
        fr = [(l, 'fr', p[0]) for p, l in idx if l[0] not in SU2]
        su = [(l, 'su2', p[0]) for p, l in idx if l[0] in SU2]
        if name == 'psi': name = 'grav' if fr else 'dil'
        X = s.odd[(sig, name)]
        labels = [(l, 'fr', p[0]) for p, l in dl] + fr
        assert X.A.ndim - 3 == len(labels), (f, X.A.shape, labels)
        return X, labels, su

    def bos_value(s, f):
        """background value (numpy array, labels)"""
        t = s.ev.factor(f)
        return t.a, [(x[0], x[1], x[2]) for x in t.idx]

    def even_value(s, f):
        """two-fermion part (array with trailing modes, labels) or None"""
        f = unwrap(f)
        if f[0] == 'T':
            name, idx = f[1], f[2]; sig, dl = '', []
        elif f[0] == 'pow':
            base = unwrap(f[1]); assert base[0] == 'T' and f[2] == 2 and not base[2], f
            name = base[1]; K = s.even[('', name)]
            if K is None: return None
            b0 = s.bos_value(base)[0]
            return 2 * b0 * K, []
        elif f[0] == 'D':
            sig, dl = chain_sig(f); tgt = unwrap(f[2]); name, idx = tgt[1], tgt[2]
        else:
            raise KeyError(f)
        key = (sig, name)
        if key not in s.even: raise KeyError('no two-fermion part for %s' % (key,))
        K = s.even[key]
        if K is None: return None
        lab_d = [(l, 'fr', p[0]) for p, l in dl]
        lab_t = [(l, 'fr' if l[0] not in SU2 else 'su2', p[0]) for p, l in idx]
        if key == ('Bd', 'H^'):
            # Box D^c H_ac : free index = the target index not contracted with the derivative
            dlet = dl[0][1]; free = [x for x in lab_t if x[0] != dlet]; assert len(free) == 1 and lab_t[1][0] == dlet, (f,)
            return K, free
        if key in (('dB', 'sigma'), ('Bd', 'sigma')): return K, lab_d
        return K, lab_d + lab_t

    # ------------------------------------------------------------------ contraction
    def contract(s, coef, items, odd=None, out=()):
        """items: list of (array, labels); an array with two more axes than labels is a K-array (modes last).
        odd: None or (X, xlabels, Y, ylabels, gammas) for the chain bar(X) gamma_1 ... gamma_n Y, labels incl. SU(2);
        gammas = list of (array (..,4,4), labels).  out: free labels (letters) kept in the output (in this order).
        Returns array out + (Nb, Na)."""
        num, ip, gp = coef
        cf = complex(float(num)) * (1j ** ip) * (s.c.g ** gp)
        pool = iter([ch for ch in 'abcdefghijklopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'])
        ops = [[a, list(lb), None] for a, lb in items]
        if odd is not None:
            X, xl, Y, yl, gams = odd
            if not any(x[1] == 'su2' for x in xl) and not any(y[1] == 'su2' for y in yl):
                xl = xl + [('I*', 'su2', 'u')]; yl = yl + [('I*', 'su2', 'd')]
            gops = [[g, list(gl), None] for g, gl in gams]
            ops_all = ops + gops + [['X', xl, None], ['Y', yl, None]]
        else:
            gops = []; ops_all = ops
        occ = {}
        for k_, op in enumerate(ops_all):
            for (l, kind, pos) in op[1]: occ.setdefault(l, []).append((k_, kind, pos))
        let = {}
        for k_, op in enumerate(ops_all):
            op[2] = ''.join(let.setdefault((l, k_), next(pool)) for (l, kind, pos) in op[1])
        extra = []
        outspec = ''
        for l, oc in occ.items():
            if len(oc) == 1:
                if l in out: continue
                raise ValueError('free index %s' % l)
            if len(oc) > 2: raise ValueError('letter %s occurs %d times' % (l, len(oc)))
            (k1, kind1, p1), (k2, kind2, p2) = oc
            l1 = let[(l, k1)]; l2 = let[(l, k2)]
            if kind1 == 'fr': extra.append((ETAI, l1 + l2))
            else:
                p1, p2 = p1[0], p2[0]
                if (p1, p2) == ('u', 'd'): extra.append((EPS2.T.astype(complex), l1 + l2))
                elif (p1, p2) == ('d', 'u'): extra.append((EPS2.astype(complex), l1 + l2))
                else: raise ValueError('SU(2) pairing %s %s %s' % (l, p1, p2))
        for l in out:
            (k1, kind1, p1), = occ[l]; outspec += let[(l, k1)]
        specs = []; arrs = []
        for op in ops:
            sp_ = op[2] + ('mn' if op[0].ndim == len(op[2]) + 2 else '')
            specs.append(sp_); arrs.append(op[0])
        if odd is None:
            expr = ','.join(specs + [e_[1] for e_ in extra]) + '->' + outspec + 'mn'
            return cf * np.einsum(expr, *(arrs + [e_[0] for e_ in extra]), optimize=True)
        ng = len(gops)
        sl = [next(pool) for _ in range(ng + 2)]
        gspecs = [gops[k_][2] + sl[k_ + 1] + sl[k_ + 2] for k_ in range(ng)]
        xs = ops_all[-2][2] + sl[0]; ys = ops_all[-1][2] + sl[-1]
        cspec = sl[0] + sl[1]
        rest = specs + gspecs + [cspec] + [e_[1] for e_ in extra]
        rarrs = arrs + [g[0] for g in gops] + [CC] + [e_[0] for e_ in extra]
        e1 = ','.join([xs + 'm', ys + 'n'] + rest) + '->' + outspec + 'mn'
        e2 = ','.join([xs + 'n', ys + 'm'] + rest) + '->' + outspec + 'mn'
        return cf * (np.einsum(e1, X.B, Y.A, *rarrs, optimize=True) - np.einsum(e2, X.A, Y.B, *rarrs, optimize=True))

    def gamma_value(s, f):
        idx = f[2]
        return GL[len(idx)], [(l, 'fr', p[0]) for p, l in idx]

    def bilinear(s, coef, fs, out=()):
        ib = [k for k, f in enumerate(fs) if f[0] == 'bar']; assert len(ib) == 1, fs
        ib = ib[0]
        iy = [k for k, f in enumerate(fs) if k != ib and has_odd(f)]; assert len(iy) == 1, fs
        iy = iy[0]
        ig = [k for k, f in enumerate(fs) if f[0] == 'T' and f[1] == 'gamma']
        assert all(ib < k < iy for k in ig), ('gamma outside the chain', fs)
        X, xl, xs = s.odd_value(fs[ib][1]); Y, yl, ys = s.odd_value(fs[iy])
        gams = [s.gamma_value(fs[k]) for k in ig]
        items = [s.bos_value(f) for k, f in enumerate(fs) if k not in ig and k != ib and k != iy]
        return s.contract(coef, items, (X, xl + xs, Y, yl + ys, gams), out=out)

    def term_K(s, t):
        fs = [unwrap(f) for f in t['factors']]
        odd = [f for f in fs if has_odd(f)]
        if len(odd) == 2: return s.bilinear(t['coef'], fs)
        if len(odd) == 1:
            # C_a D_b (bilinear group).  D_b is the FULL supercovariant derivative: at two fermions
            # D_b(Xbar G Y) = (D_b X)bar G Y + Xbar G (D_b Y) with the linear-order supercovariant derivatives (they contain
            # -delta_Q(psi_b) and -delta_S(phi_b) of X, Y).  [Before 6 Nov: nabla_b of the bilinear (nabK), which omits the
            # gravitino terms -delta(psi_b)(Xbar G Y) -- wrong at two fermions; kept as LEGACY_NABLA for comparison.]
            kd = [k for k, f in enumerate(fs) if has_odd(f)][0]; g = fs[kd]
            assert g[0] == 'D' and len(g[1]) == 1 and unwrap(g[2])[0] == 'grp', g
            sub = unwrap(g[2])[1]; assert len(sub) == 1
            dl = g[1][0]
            inner = [unwrap(x) for x in sub[0]['factors']]
            if LEGACY_NABLA:
                cnt = {}
                for x in inner:
                    for p, l in (x[1][2] if x[0] == 'bar' else (x[2] if x[0] == 'T' else [])):
                        cnt[l] = cnt.get(l, 0) + 1
                free = [l for l, n in cnt.items() if n == 1 and l[0] not in SU2]
                J = s.bilinear(sub[0]['coef'], inner, out=tuple(free))       # axes free..., m, n
                DJ = s.c.nabK(J, len(free))                                   # axes d, free...
                items = [s.bos_value(f) for k, f in enumerate(fs) if k != kd]
                items.append((DJ, [(dl[1], 'fr', dl[0][0])] + [(l, 'fr', 'u') for l in free]))
                return s.contract(t['coef'], items)
            (n1, i1, g1), (n2, i2, g2) = t['coef'], sub[0]['coef']
            cf = (n1 * n2, i1 + i2, g1 + g2)
            outer = [f for k, f in enumerate(fs) if k != kd]
            assert all(not has_odd(x) or x[0] == 'bar' or x[0] == 'T' for x in inner)
            assert all(has_odd(x) or (x[0] == 'T' and x[1] == 'gamma') for x in inner), inner
            tot = 0
            for k, x in enumerate(inner):
                if not has_odd(x): continue
                if x[0] == 'bar': y = ('bar', ('D', [dl], x[1]))
                else: y = ('D', [dl], x)
                tot = tot + s.bilinear(cf, outer + inner[:k] + [y] + inner[k + 1:])
            return tot
        # bosonic form: sum over factors of (factor)^(2) x others^0
        tot = 0
        for k, f in enumerate(fs):
            ev = s.even_value(f)
            if ev is None: continue
            items = [ev] + [s.bos_value(g) for j, g in enumerate(fs) if j != k]
            tot = tot + s.contract(t['coef'], items)
        return tot

def KGB(c, terms=None, verbose=False, split=False, trace=False):
    eng = Engine(c)
    if terms is None:
        from sources import terms as source_terms
        terms = source_terms()
    parts = {lab: np.zeros((c.Nb, c.Na), complex) for lab in ('W', 'LOG')}
    eng.source_terms = []
    for index, source in enumerate(terms):
        lab = 'W' if index < 52 else 'LOG'
        value = np.zeros((c.Nb, c.Na), complex)
        for term in leibniz(evalbg.expand_terms([source])):
            value += eng.term_K(term)
        if not np.isfinite(value).all():
            raise ArithmeticError(('Nonfinite source contribution', index))
        parts[lab] += value
        if trace:
            eng.source_terms.append(value)
    if split: return parts, eng
    return parts['W'] + parts['LOG'], eng
