"""Once-only bar projection and transport of the existing LOG polynomials.

This module does not differentiate a prematurely truncated spinor.  Its
inputs are the completed superspace expressions in steps 2--5.  No Fierz,
integration by parts, EOM, or ordinary-derivative replacement is performed.
"""
from collections import Counter
from pathlib import Path
import pickle
import log_step4_covariant_rules as b

BASE = Path(__file__).resolve().parents[2] / 'outputs' / 'kernel'
Q, I, P = b.Q, b.I, b.P
for name, definition in {
    'rho': ('', Q(1), 0), 'lam': ('su', Q(3, 2), 1),
    'aux': ('uu', Q(2), 0), 'hatF': ('ll', Q(2), 0),
    'ten': ('ll', Q(1), 0), 'chi': ('su', Q(3, 2), 1),
    'auxD': ('', Q(2), 0), 'RQ': ('llsu', Q(3, 2), 1),
    'RV': ('lluu', Q(2), 0), 'RMB': ('llll', Q(2), 0),
    'g1': ('lss', Q(0), 0), 'g2': ('llss', Q(0), 0),
    'suB': ('uu', Q(0), 0), 'volB': ('lllll', Q(0), 0),
}.items():
    b.spec[name] = definition
b.const.update({'g1', 'g2', 'suB', 'volB'})
b.symbols.update({'rho': r'\rho', 'lam': r'\lambda', 'aux': 'Y',
    'hatF': r'\widehat F', 'ten': 'T', 'chi': r'\chi', 'auxD': 'D',
    'RQ': 'R(Q)', 'RV': 'R(V)', 'RMB': 'R(M)',
    'g1': r'\gamma', 'g2': r'\gamma', 'suB': r'\varepsilon',
    'volB': r'\epsilon'})


def retained(p, limit):
    return P.terms([(c, fs) for c, fs in p.ts
                    if sum(f.parity for f in fs) <= limit])


def elementary(f):
    """Source tensor -> project tensor; retain every index in its position."""
    if f.oddD:
        raise ValueError('Projection requires completed spinor differentiation')
    if f.ds:
        p = elementary(b.replace(f, ds=()))
        for d in reversed(f.ds):
            p = b.vec(d, p)
        return p
    n, ix = f.name, f.ix
    if n == 'pow':
        return P(f)  # rho^{-n} is supplied by the renderer, not a new field.
    simple = {'W': ('rho', 1), 'L': ('lam', -1), 'X': ('aux', 2),
        'F': ('hatF', -1), 'w': ('ten', Q(16, 3)),
        'x': ('chi', -I * Q(32, 3)), 'Y': ('auxD', Q(-128, 3)),
        'za': ('RV', -I * Q(4, 3)), 'w3a': ('RQ', I),
        'G': ('g1', I), 'S': ('g2', Q(1, 2)), 'eps5': ('volB', -1)}
    if n in simple:
        target, c = simple[n]
        return c * b.replace(f, name=target)
    if n == 'eps' and ix[0][1] == 'u':
        # Gold lowers on the left with -E; B lowers on the right with E.
        # Already-lowered fields have equal arrays. A naked lower metric
        # changes sign, whereas a naked upper metric does not.
        return (-1 if ix[0][0] == '-' else 1) * b.replace(f, name='suB')
    if n in {'eps', 'eta', 'del'}:
        return P(f)
    a, c = b.fresh('l'), b.fresh('l')
    gam = lambda s, t: b.field('g2', b.up(a), b.up(c), s, t)
    if n in {'Fs', 'ws', 'z', 'w3'}:
        target, fac = {'Fs': ('hatF', Q(-1, 4)),
            'ws': ('ten', Q(4, 3)), 'z': ('RV', -I * Q(1, 3)),
            'w3': ('RQ', I * Q(1, 4))}[n]
        return fac * gam(*ix[:2]) * b.field(target, b.dn(a), b.dn(c), *ix[2:])
    if n == 'w4':
        d, e = b.fresh('l'), b.fresh('l')
        alpha, beta, gamma, delta = ix
        p = -I * Q(1, 4) * gam(alpha, beta) * b.field(
            'g2', b.up(d), b.up(e), gamma, delta) * b.field(
            'RMB', b.dn(a), b.dn(c), b.dn(d), b.dn(e))
        # 3 W_(ab W_cd) = W_ab W_cd + W_ac W_bd + W_ad W_bc.
        for s, t, u, v in [(alpha, beta, gamma, delta),
                           (alpha, gamma, beta, delta),
                           (alpha, delta, beta, gamma)]:
            p += I * Q(16, 9) * gam(s, t) * b.field(
                'g2', b.up(d), b.up(e), u, v) * b.field(
                'ten', b.dn(a), b.dn(c)) * b.field('ten', b.dn(d), b.dn(e))
        return p
    raise ValueError(('unprojected field', f))


def project(p):
    # Eliminate mixed superspace geometric objects using their explicit
    # source equations *before* transporting generators or metrics.
    expanded = P()
    for c, fs in p.ts:
        q = P(c)
        for f in fs:
            q *= b.geometry(f)
        expanded.ts.extend(q.ts)
    p = b.normalize(expanded, True)
    out = P()
    for c, fs in p.ts:
        q = P(c)
        for f in fs:
            q *= elementary(f)
        out.ts.extend(q.ts)
    # Do not run the source metric contractor on B's lower SU(2) epsilon.
    return b.normalize(out, False)


def input_polynomials():
    raise RuntimeError("Use calculations.descendants: fresh differentiation replaces temporary caches.")


WEIGHTS = {'L': Q(3), 'phi': Q(7, 2), 'N': Q(4), 'E': Q(4)}
FREE = {'L': {'uI': '+', 'uJ': '+'},
        'phi': {'sE': '-', 'uI': '+'}, 'N': {}, 'E': {'lV': '+'}}


def texatom(f, mp):
    def indices(ix):
        return ''.join(('{}^{' if x[0] == '+' else '{}_{') + mp[x[1:]] + '}'
                       for x in ix)
    if f.name == 'pow':
        body = r'\rho' if f.power == 1 else r'\rho^{' + str(f.power) + '}'
    elif f.name in {'g1', 'g2'}:
        cut = 1 if f.name == 'g1' else 2
        body = r'(\gamma' + indices(f.ix[:cut]) + ')' + indices(f.ix[cut:])
    elif f.name == 'eps' and f.ix[0][1] == 's':
        body = r'\mathsf C' + indices(f.ix)
    else:
        body = b.symbols[f.name] + indices(f.ix)
    for d in reversed(f.ds):
        body = (r'\mathcal D_{' if d[0] == '-' else r'\mathcal D^{') + mp[d[1:]] + '}' + body
    return r'\big(' + body + r'\big)' if f.ds else body


def labels(slot):
    b.a.fixed.clear()
    b.a.names['s'] = [r'\alpha', r'\beta', r'\gamma', r'\delta', r'\rho',
        r'\sigma', r'\tau', r'\xi', r'\kappa', r'\mu', r'\nu', r'\omega', r'\upsilon']
    b.a.names['s'] += [r'\alpha_{'+str(j)+'}' for j in range(1,30)]
    b.a.names['u'] = list('ijklmn') + ['i_{'+str(j)+'}' for j in range(1,30)]
    b.a.names['l'] = list('abcdefgh') + ['a_{'+str(j)+'}' for j in range(1,30)]
    if slot == 'L':
        b.a.fixed.update({'uI': 'i', 'uJ': 'j'})
        b.a.names['u'] = b.a.names['u'][2:]
    elif slot == 'phi':
        b.a.fixed.update({'sE': r'\alpha', 'uI': 'i'})
        b.a.names['s'] = b.a.names['s'][1:]
        b.a.names['u'] = b.a.names['u'][1:]
    elif slot == 'E':
        b.a.fixed['lV'] = 'a'
        b.a.names['l'] = b.a.names['l'][1:]


def term(c, fs):
    mp = b.a.namemap(fs)
    used = {x[1:] for f in fs for x in b.allix(f)}
    vals = [mp[k] for k in used]
    assert len(set(vals)) == len(vals), 'Dummy labels overlap'
    return b.texcoef(c) + ''.join(texatom(f, mp) for f in fs)


def texcoef(c):
    if c.r and c.i:
        return '+\\left(' + b.texcoef(b.C(c.r, Q(0))).lstrip('+') + b.texcoef(b.C(Q(0), c.i)) + '\\right)'
    return b.texcoef(c)


def collect(p, slot):
    """Collect literally identical monomials after even-factor moves only.

    All odd factors keep their original mutual order. No gamma symmetry,
    antisymmetric-index canonicalization, Fierz identity or trace is assumed.
    The output key is the complete displayed field expression, so unrelated
    contraction graphs cannot become equal because of a truncated hash.
    """
    labels(slot)
    answer, multiplicities = {}, Counter()
    for c, fs in p.ts:
        even = [f for f in fs if not f.parity]
        odd = [f for f in fs if f.parity]
        even.sort(key=lambda f: (f.name != 'pow', f.name,
                   len(f.ds), tuple(x[:2] for x in f.ds + f.ix)))
        ordered = tuple(even + odd)
        body = term(b.coef(1), ordered)[1:]
        answer[body] = answer.get(body, b.coef(0)) + c
        multiplicities[body] += 1
    return [(c, body) for body, c in answer.items() if c], multiplicities


if __name__ == '__main__':
    for slot, ps in input_polynomials().items():
        count = 0
        for key, p in ps.items():
            q = project(p)
            b.check(q, WEIGHTS[slot], FREE[slot])
            count += len(q.ts)
        print(slot, count, flush=True)
