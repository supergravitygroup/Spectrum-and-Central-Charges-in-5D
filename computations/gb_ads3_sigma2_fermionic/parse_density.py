"""Parser of the lambda_GB block of GB-FINAL-DENSITY (inputs/gb_splus_action.md, Final Result).

Output: a list of terms, each a dict {coef: (rational, ipow, gpow), factors: [Factor ...]}, where the coefficient is
rational * i**ipow * g**gpow, and a Factor is one of
  ('T', name, idx)                tensor atom; idx = list of (pos, letter) with pos in 'u','d'; name in
                                  C^ (Weyl tensor), G^, H^, RV (R(V)), RQ (R(Q)), T, D, N, L, C (bare potential),
                                  chi, psi, varphi, sigma, eps, gamma, G2 (G^2), T2 (T^2)
  ('D', [(pos,letter) | 'box' | 'slash'], Factor)   ordered derivative chain applied to a factor or a group
  ('grp', [terms])                parenthesised sum (a nested expression)
  ('bar', Factor)                 Majorana bar of an odd factor
  ('pow', Factor, n)              integer power of a bosonic factor
  ('sym', ...)                    is not produced: symmetrisation (i j) is recorded on the index as pos+'(' / pos+')'
The parser does not interpret physics; it only reproduces the source structure.  Usage: python3 parse_density.py"""
import re
from fractions import Fraction

def load_block(path):
    s = open(path).read().splitlines()
    a = next(i for i, l in enumerate(s) if l.startswith('## Final Result'))
    fin = s[a:]
    st = next(i for i, l in enumerate(fin) if '\\lambda_{\\mathrm{GB}}\\Bigg(' in l)
    en = next(i for i, l in enumerate(fin) if '\\tag{GB-FINAL-DENSITY}' in l)
    txt = '\n'.join(fin[st:en])
    txt = txt.split('\\lambda_{\\mathrm{GB}}\\Bigg(', 1)[1]
    # strip the closing  \Bigg)\Bigg]_{\le2}.  \end{aligned}}
    k = txt.rfind('\\Bigg)\\Bigg]_{\\le2}')
    txt = txt[:k]
    txt = txt.replace('&', ' ').replace('\\\\[3pt]', ' ').replace('\\\\', ' ')
    txt = txt.replace('\\,', '').replace('\n', ' ')
    return txt

# ---------------------------------------------------------------- tokenizer
TOK = re.compile(r"""
 (?P<frac>\\frac\{(?P<fn>[0-9]*i?)\}\{(?P<fd>[0-9]+)\})
|(?P<frac2>\\frac(?P<f2n>[0-9])(?P<f2d>[0-9]))
|(?P<num>[0-9]+)
|(?P<cmd>\\[A-Za-z]+)
|(?P<sym>[{}()\[\]^_+\-])
|(?P<let>[A-Za-z])
|(?P<ws>\s+)
""", re.X)

def tokenize(t):
    out = []; pos = 0
    while pos < len(t):
        m = TOK.match(t, pos)
        if not m: raise SyntaxError('cannot tokenize at %r' % t[pos:pos+40])
        pos = m.end()
        if m.group('ws'): continue
        if m.group('frac'): out.append(('frac', m.group('fn'), m.group('fd')))
        elif m.group('frac2'): out.append(('frac', m.group('f2n'), m.group('f2d')))
        elif m.group('num'): out.append(('num', m.group('num')))
        elif m.group('cmd'): out.append(('cmd', m.group('cmd')))
        elif m.group('sym'): out.append(('sym', m.group('sym')))
        else: out.append(('let', m.group('let')))
    return out

class P:
    def __init__(s, toks): s.t = toks; s.i = 0
    def peek(s, k=0): return s.t[s.i+k] if s.i+k < len(s.t) else ('eof',)
    def take(s): x = s.t[s.i]; s.i += 1; return x
    def expect(s, kind, val=None):
        x = s.take()
        if x[0] != kind or (val is not None and x[1] != val): raise SyntaxError('expected %s %s, got %s at token %d' % (kind, val, x, s.i))
        return x
    def at(s, kind, val=None):
        x = s.peek(); return x[0] == kind and (val is None or x[1] == val)

    # ---- index blocks: {}^{a}{}^{b} ... , ^{ab}, _a, _{(i}, ^c (single), {}_{b}
    def indices(s):
        idx = []
        while True:
            if s.at('sym', '{') and s.peek(1) == ('sym', '}') and s.peek(2)[0] == 'sym' and s.peek(2)[1] in '^_':
                s.take(); s.take(); continue
            if s.at('sym', '^') or s.at('sym', '_'):
                # power?  ^{2} or ^2 after an atom is handled by the caller
                nxt = s.peek(1)
                if s.peek()[1] == '^' and (nxt[0] == 'num' or (nxt == ('sym', '{') and s.peek(2)[0] == 'num')): break
                if s.peek()[1] == '^' and nxt == ('let', 'c') and s._box_context: break
                pos = 'u' if s.take()[1] == '^' else 'd'
                if s.at('sym', '{'):
                    s.take(); sym = ''
                    while not s.at('sym', '}'):
                        x = s.take()
                        if x == ('sym', '('): sym = '('; continue
                        if x == ('sym', ')'): idx[-1] = (idx[-1][0] + ')', idx[-1][1]); continue
                        if x[0] != 'let': raise SyntaxError('bad index token %s at %d' % (x, s.i))
                        idx.append((pos + sym, x[1])); sym = ''
                    s.take()
                else:
                    x = s.take()
                    if x[0] != 'let': raise SyntaxError('bad index %s at %d' % (x, s.i))
                    idx.append((pos, x[1]))
                continue
            break
        return idx
    _box_context = False

    def power(s):
        if s.at('sym', '^'):
            nxt = s.peek(1)
            if nxt[0] == 'num': s.take(); return int(s.take()[1])
            if nxt == ('sym', '{') and s.peek(2)[0] == 'num' and s.peek(3) == ('sym', '}'):
                s.take(); s.take(); n = int(s.take()[1]); s.take(); return n
        return None

    # ---- expression
    def expr(s, closers):
        terms = []; sign = 1
        if s.at('sym', '+'): s.take()
        elif s.at('sym', '-'): s.take(); sign = -1
        while True:
            t = s.term(closers); t['coef'] = (t['coef'][0]*sign, t['coef'][1], t['coef'][2]); terms.append(t)
            if s.at('sym', '+'): s.take(); sign = 1
            elif s.at('sym', '-'): s.take(); sign = -1
            else: break
        return terms

    def is_closer(s, closers):
        x = s.peek()
        if x[0] == 'eof': return True
        for c in closers:
            if x == c: return True
        return False

    def term(s, closers):
        num = Fraction(1); ip = 0; gp = 0; facs = []
        while not s.is_closer(closers) and not s.at('sym', '+') and not s.at('sym', '-'):
            x = s.peek()
            if x[0] == 'frac':
                s.take(); n = x[1]
                if n.endswith('i'): ip += 1; n = n[:-1]
                num *= Fraction(int(n) if n else 1, int(x[2])); continue
            if x[0] == 'num': s.take(); num *= int(x[1]); continue
            if x == ('let', 'i'): s.take(); ip += 1; continue
            if x == ('let', 'g'):
                s.take(); p = s.power(); gp += p if p else 1; continue
            facs.append(s.factor())
        return dict(coef=(num, ip, gp), factors=facs)

    def group(s, open_tok, close_tok):
        s.take()
        inner = s.expr([close_tok])
        s.expect(*close_tok)
        return ('grp', inner)

    def factor(s):
        x = s.peek()
        f = None
        if x == ('cmd', '\\big') and s.peek(1) == ('sym', '('):
            s.take(); f = s.group(('sym', '('), ('cmd', '\\big')); s.expect('sym', ')')
        elif x == ('cmd', '\\Big') and s.peek(1) == ('sym', '['):
            s.take(); s.take(); inner = s.expr([('cmd', '\\Big')]); s.expect('cmd', '\\Big'); s.expect('sym', ']'); f = ('grp', inner)
        elif x == ('sym', '('):
            s.take(); inner = s.expr([('sym', ')')]); s.expect('sym', ')'); f = ('grp', inner)
        elif x == ('cmd', '\\mathcal'):
            s.take(); s.expect('let', 'D'); idx = s.indices()
            chain = [idx[0]] if idx else []
            if len(idx) != 1: raise SyntaxError('derivative index %s at %d' % (idx, s.i))
            tgt = s.factor()
            if tgt[0] == 'D': return ('D', chain + tgt[1], tgt[2])
            return ('D', chain, tgt)
        elif x == ('cmd', '\\Box'):
            s.take(); s.expect('sym', '^'); s.expect('let', 'c')
            tgt = s.factor()
            if tgt[0] == 'D': return ('D', ['box'] + tgt[1], tgt[2])
            return ('D', ['box'], tgt)
        elif x == ('cmd', '\\overline'):
            s.take(); s.expect('sym', '{'); inner = s.expr([('sym', '}')]); s.expect('sym', '}')
            if len(inner) != 1 or inner[0]['coef'] != (1, 0, 0) or len(inner[0]['factors']) != 1:
                raise SyntaxError('overline content %s' % inner)
            g0 = inner[0]['factors'][0]
            if g0[0] == 'T' and g0[1] == 'R?':
                idx = g0[2] + s.indices(); s.expect('sym', '('); kind = s.take()[1]; s.expect('sym', ')'); idx += s.indices()
                g0 = ('T', 'R' + kind, idx)
            f = ('bar', g0)
        elif x == ('cmd', '\\bar'):
            s.take(); f = ('bar', s.atom())
        else:
            f = s.atom()
        p = s.power()
        if p: f = ('pow', f, p)
        return f

    def atom(s):
        x = s.take()
        if x == ('cmd', '\\widehat'):
            y = s.take()
            if y[0] != 'let': raise SyntaxError('widehat %s' % (y,))
            if y[1] == 'R':
                idx = s.indices(); kind = None
                if s.at('sym', '('):
                    s.take(); kind = s.take()[1]; s.expect('sym', ')')
                idx += s.indices()
                if kind is None and s.at('sym', '}'): return ('T', 'R?', idx)   # \overline{\widehat R}_{..}(Q)
                if kind not in ('Q', 'V'): raise SyntaxError('R kind %s' % kind)
                return ('T', 'R' + kind, idx)
            name = y[1] + '^'
            if s.at('sym', '^') and s.peek(1) == ('num', '2'):
                s.take(); s.take(); return ('T', y[1] + '2', [])
            return ('T', name, s.indices())
        if x[0] == 'cmd':
            nm = {'\\chi': 'chi', '\\psi': 'psi', '\\varphi': 'varphi', '\\sigma': 'sigma', '\\varepsilon': 'eps',
                  '\\gamma': 'gamma', '\\phi': 'phi'}.get(x[1])
            if nm is None: raise SyntaxError('unknown command %s at %d' % (x[1], s.i))
            return ('T', nm, s.indices())
        if x[0] == 'let' and x[1] in 'CTDNL':
            if x[1] == 'T' and s.at('sym', '^') and s.peek(1) == ('num', '2'):
                s.take(); s.take(); return ('T', 'T2', [])
            if x[1] == 'D' and s.at('sym', '^') and s.peek(1) == ('num', '2'):
                s.take(); s.take(); return ('pow', ('T', 'D', []), 2)
            return ('T', x[1], s.indices())
        raise SyntaxError('unexpected token %s at %d' % (x, s.i))

def parse(path):
    txt = load_block(path)
    p = P(tokenize(txt))
    terms = p.expr([])
    if p.peek()[0] != 'eof': raise SyntaxError('trailing tokens at %d: %s' % (p.i, p.t[p.i:p.i+10]))
    return terms

def show(f):
    if f[0] == 'T':
        return f[1] + ''.join(('^' if p[0] == 'u' else '_') + ('(' if '(' in p else '') + l + (')' if ')' in p else '') for p, l in f[2])
    if f[0] == 'D':
        ch = ''.join('Box' if c == 'box' else ('D^' if c[0] == 'u' else 'D_') + c[1] for c in f[1])
        return '[' + ch + ' ' + show(f[2]) + ']'
    if f[0] == 'bar': return 'bar(' + show(f[1]) + ')'
    if f[0] == 'pow': return '(' + show(f[1]) + ')^%d' % f[2]
    if f[0] == 'grp': return '{' + ' + '.join(showterm(t) for t in f[1]) + '}'
def showterm(t):
    c, ip, gp = t['coef']
    return '%s%s%s ' % (c, ' i^%d' % ip if ip else '', ' g^%d' % gp if gp else '') + ' '.join(show(f) for f in t['factors'])

