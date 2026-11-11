"""Background (fermion-free) value of the parsed lambda_GB block on AdS3 x Sigma2, and comparison with the paper's
L_GB from the stage-2 engine.

Semantics.  Each factor is evaluated as a numeric tensor with frame indices LOWER and SU(2) indices UPPER (canonical
form).  A repeated frame letter is contracted with eta^{ab}; a repeated SU(2) letter X^i ... Y_i is contracted with
eps_{ji} (Y_i = Y^j eps_ji), the lower one being the second.  Background values of derivatives:
  * first derivatives of K-inert covariants (G, H, T, C^, D, N, L, groups) and of sigma: 0 (homogeneous, covariantly
    constant, D_a sigma = 0 at the gauge);
  * D_a D_b sigma = 2 f_ab, Box sigma = 2 f_a^a (SC7D-06/07);
  * D_e D_b X of a K-inert X of weight w with lower indices: the K-connection term
      2w f_eb X_{a..} + sum_k [2 f_{e a_k} X_{..b..} - 2 eta_{b a_k} f_e^c X_{..c..}]   (W01, R04a)
    (derivation in fermionic_action_inputs.md); weights: G 2, H 3, T 1, L 3, N 4;
  * third derivatives: 0 at the background (their K-variations are proportional to D sigma or D X, which vanish).
Terms with an odd factor (psi, varphi, chi, R(Q)) have no background value.  Usage: python3 evalbg.py L k [g]"""
import itertools
import numpy as np
from fractions import Fraction
from bgfields import Background, ETA, EPS2, EPS_LOW
ETAI = np.linalg.inv(ETA)
SU2 = set('ijkl')
ODD = {'psi', 'varphi', 'chi', 'RQ', 'phi'}
LOR = 1
WEIGHT = {'G^': 2, 'H^': 3, 'T': 1, 'L': 3, 'N': 4}

class Ten:
    """numeric tensor with an ordered list of (letter, kind, pos) for its free indices (canonical storage)"""
    def __init__(s, arr, idx): s.a = np.asarray(arr, complex); s.idx = idx

def has_odd(f):
    if f[0] == 'T': return f[1] in ODD
    if f[0] in ('D', 'bar'): return has_odd(f[2] if f[0] == 'D' else f[1])
    if f[0] == 'pow': return has_odd(f[1])
    if f[0] == 'grp': return any(any(has_odd(g) for g in t['factors']) for t in f[1])
    return False

def canon_idx(idx):
    out = []
    for pos, l in idx:
        out.append((l, 'su2' if l[0] in SU2 else 'fr', pos[0], pos[1:]))
    return out

class Evaluator:
    def __init__(s, B): s.B = B

    # ---------------- atoms
    def atom(s, name, idx):
        B = s.B
        ci = canon_idx(idx)
        if name == 'C^': return Ten(B.Cw, ci)
        if name == 'G^': return Ten(B.G, ci)
        if name == 'H^': return Ten(B.H, ci)
        if name == 'T': return Ten(B.T, ci)
        if name == 'G2': return Ten(B.G2, [])
        if name == 'T2': return Ten(B.T2, [])
        if name == 'D': return Ten(B.Dscal, [])
        if name == 'N': return Ten(B.N, [])
        if name == 'L': return Ten(B.Lij, ci)
        if name == 'C': return Ten(B.Ca, ci)
        if name == 'RV': return Ten(B.RV, ci)
        if name == 'eps': return Ten(EPS_LOW, ci)
        if name == 'sigma': return Ten(np.array(1.0 + 0j), [])
        raise KeyError('no background value for atom %s' % name)

    def deriv(s, chain, tgt):
        B = s.B
        n = sum(2 if c == 'box' else 1 for c in chain)
        if n == 1:
            # value of the target only fixes the shape: result is zero with the derivative index prepended
            t = s.factor(tgt)
            dl = chain[0]
            return Ten(np.zeros((5,) + t.a.shape, complex), [(dl[1], 'fr', dl[0][0], '')] + t.idx)
        if n >= 3:
            t = s.factor(tgt)
            extra = [] if chain[0] == 'box' and len(chain) == 2 else None
            letters = [c for c in chain if c != 'box']
            return Ten(np.zeros((5,) * len(letters) + t.a.shape, complex), [(c[1], 'fr', c[0][0], '') for c in letters] + t.idx)
        # second derivative: chain = [d_e, d_b] or ['box']
        if tgt[0] == 'T' and tgt[1] == 'sigma':
            val = 2 * B.f                              # D_e D_b sigma
            X = Ten(np.ones(()), [])
        else:
            X = s.factor(tgt)
            name = tgt[1] if tgt[0] == 'T' else None
            if name not in WEIGHT: raise KeyError('second derivative of %s' % (tgt,))
            w = WEIGHT[name]
            val = None
        # build K-term tensor  K[e,b,(X indices)]
        if tgt[0] == 'T' and tgt[1] == 'sigma':
            K = 2 * B.f
        else:
            frpos = [k for k, t in enumerate(X.idx) if t[1] == 'fr']
            K = 2 * w * np.einsum('eb,...->eb...', B.f, X.a)
            fu = np.einsum('ec,cd->ed', B.f, ETAI)        # f_e^c ... f_e^c with c up
            for k in frpos:
                # 2 f_{e a_k} X_{..b..}: move X's k-th axis to the b slot
                Xm = np.moveaxis(X.a, k, 0)                          # X[b, rest...]
                t1 = 2 * np.einsum('ea,b...->eba...', B.f, Xm)        # indices e,b,a_k,rest
                t1 = np.moveaxis(t1, 2, 2 + k)
                # -2 eta_{b a_k} f_e^c X_{..c..}
                Xc = np.einsum('ec,c...->e...', fu, Xm)              # f_e^c X_{c,rest}
                t2 = -2 * np.einsum('ba,e...->eba...', ETA, Xc)
                t2 = np.moveaxis(t2, 2, 2 + k)
                K = K + LOR * (t1 + t2)
        if chain == ['box']:
            return Ten(np.einsum('eb...,eb->...', K, ETAI), X.idx)
        e, b = chain
        return Ten(K, [(e[1], 'fr', e[0][0], ''), (b[1], 'fr', b[0][0], '')] + X.idx)

    def factor(s, f):
        if f[0] == 'T': return s.atom(f[1], f[2])
        if f[0] == 'D': return s.deriv(f[1], f[2])
        if f[0] == 'pow':
            t = s.factor(f[1]); assert not t.idx, 'power of a tensor'
            return Ten(t.a ** f[2], [])
        if f[0] == 'grp':
            parts = [s.term(t) for t in f[1]]
            ref = parts[0]
            tot = ref.a.copy()
            for q in parts[1:]:
                # align index order by letters
                order = [ [x[0] for x in q.idx].index(l[0]) for l in ref.idx ]
                tot = tot + np.transpose(q.a, order)
            return Ten(tot, ref.idx)
        raise KeyError(f[0])

    def term(s, t):
        num, ip, gp = t['coef']
        c = complex(float(num)) * (1j ** ip) * (s.B.g ** gp)
        tens = [s.factor(f) for f in t['factors']]
        # contraction
        letters = {}
        for ti, T_ in enumerate(tens):
            for ax, (l, kind, pos, sym) in enumerate(T_.idx):
                letters.setdefault(l, []).append((ti, ax, kind, pos))
        ops = []; subs = []; free = []
        sym = iter('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz')
        names = {}
        for l, occ in letters.items():
            if len(occ) == 1: free.append(l)
            elif len(occ) != 2: raise ValueError('letter %s occurs %d times' % (l, len(occ)))
        axname = {}
        for l, occ in letters.items():
            if len(occ) == 1: axname[(occ[0][0], occ[0][1])] = names.setdefault(l, next(sym))
            else:
                n1, n2 = next(sym), next(sym)
                axname[(occ[0][0], occ[0][1])] = n1; axname[(occ[1][0], occ[1][1])] = n2
                kind = occ[0][2]
                if kind == 'fr':
                    ops.append(ETAI); subs.append(n1 + n2)
                else:
                    p1, p2 = occ[0][3], occ[1][3]
                    if p1 == 'u' and p2 == 'd': ops.append(EPS2.T); subs.append(n1 + n2)     # X^i Y_i -> eps_{j i} -> M[i,j]=eps_ji
                    elif p1 == 'd' and p2 == 'u': ops.append(EPS2); subs.append(n1 + n2)     # X_i Y^i = X^j eps_ji Y^i -> M[j,i] = eps_ji
                    else: raise ValueError('SU(2) letter %s with positions %s %s' % (l, p1, p2))
        ins = []
        for ti, T_ in enumerate(tens):
            ins.append(T_.a); subs.insert(len(ins) - 1, ''.join(axname[(ti, ax)] for ax in range(len(T_.idx))))
        # rebuild subs in the right order: tensors first, then metrics
        tsubs = [''.join(axname[(ti, ax)] for ax in range(len(T_.idx))) for ti, T_ in enumerate(tens)]
        msubs = []
        for l, occ in letters.items():
            if len(occ) == 2: msubs.append(axname[(occ[0][0], occ[0][1])] + axname[(occ[1][0], occ[1][1])])
        outsub = ''.join(names[l] for l in free)
        expr = ','.join(tsubs + msubs) + '->' + outsub
        val = np.einsum(expr, *([T_.a for T_ in tens] + ops), optimize=True) if tens else np.array(1.0)
        idx = [next(x for x in [(l, tens[letters[l][0][0]].idx[letters[l][0][1]][1], tens[letters[l][0][0]].idx[letters[l][0][1]][2], '')]) for l in free]
        return Ten(c * val, idx)

def block_value(B, terms, verbose=False):
    ev = Evaluator(B); tot = 0; nb = 0; skipped = []
    for k, t in enumerate(terms):
        if any(has_odd(f) for f in t['factors']): continue
        r = ev.term(t)
        assert not r.idx, 'free indices in term %d' % k
        tot += complex(r.a); nb += 1
        if verbose and abs(r.a) > 1e-12: print('%4d %+.6e' % (k, complex(r.a).real))
    return tot, nb

def unwrap(f):
    while f[0] == 'grp' and len(f[1]) == 1 and len(f[1][0]['factors']) == 1 and f[1][0]['coef'] == (1, 0, 0):
        f = f[1][0]['factors'][0]
    return f

# ------------------------------------------------------------------ distribute sums
def _mul_coef(c1, c2):
    return (c1[0] * c2[0], c1[1] + c2[1], c1[2] + c2[2])

def expand_terms(terms):
    """Distribute every group factor (and every derivative of a group) over its sum, so that each returned term is a
    product of atoms, derivatives of atoms, derivatives of single-product groups, bars and powers."""
    out = []
    for t in terms:
        stack = [(t['coef'], [])]
        for f in t['factors']:
            alts = _alternatives(f)                    # list of (coef, factor list)
            stack = [(_mul_coef(c, c2), fl + fl2) for c, fl in stack for c2, fl2 in alts]
        out += [dict(coef=c, factors=fl) for c, fl in stack]
    return out

_ctr = [0]
def _letters(f, acc):
    if f[0] == 'T':
        for p, l in f[2]: acc[l] = acc.get(l, 0) + 1
    elif f[0] == 'D':
        for c in f[1]:
            if c != 'box': acc[c[1]] = acc.get(c[1], 0) + 1
        _letters(f[2], acc)
    elif f[0] in ('bar',): _letters(f[1], acc)
    elif f[0] == 'pow': _letters(f[1], acc)
    elif f[0] == 'grp':
        for t in f[1]:
            sub = {}
            for g in t['factors']: _letters(g, sub)
            for l, n in sub.items():
                if n == 1: acc[l] = acc.get(l, 0) + 1
    return acc
def _rename(f, m):
    if f[0] == 'T': return ('T', f[1], [(p, m.get(l, l)) for p, l in f[2]])
    if f[0] == 'D': return ('D', [c if c == 'box' else (c[0], m.get(c[1], c[1])) for c in f[1]], _rename(f[2], m))
    if f[0] == 'bar': return ('bar', _rename(f[1], m))
    if f[0] == 'pow': return ('pow', _rename(f[1], m), f[2])
    if f[0] == 'grp': return ('grp', [dict(coef=t['coef'], factors=[_rename(g, m) for g in t['factors']]) for t in f[1]])
def _fresh_dummies(fl):
    acc = {}
    for g in fl: _letters(g, acc)
    m = {}
    for l, n in acc.items():
        if n >= 2: _ctr[0] += 1; m[l] = l + '#%d' % _ctr[0]
    return [_rename(g, m) for g in fl]
def _alternatives(f):
    if f[0] == 'grp':
        res = []
        for sub in expand_terms(f[1]): res.append((sub['coef'], _fresh_dummies(sub['factors'])))
        return res
    if f[0] == 'D' and f[2][0] == 'grp':
        res = []
        for sub in expand_terms(f[2][1]):
            fl = _fresh_dummies(sub['factors'])
            inner = fl[0] if len(fl) == 1 else ('grp', [dict(coef=(Fraction(1), 0, 0), factors=fl)])
            res.append((sub['coef'], [('D', f[1], inner)]))
        return res
    if f[0] == 'pow' and f[1][0] == 'grp':
        alts = _alternatives(f[1]); res = [((Fraction(1), 0, 0), [])]
        for _ in range(f[2]): res = [(_mul_coef(c, c2), a + _fresh_dummies(b)) for c, a in res for c2, b in alts]
        return res
    return [((Fraction(1), 0, 0), [f])]
