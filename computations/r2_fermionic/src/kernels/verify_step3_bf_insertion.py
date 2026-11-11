#!/usr/bin/env python3
"""Exact Step 3 distribution audit; not a SUSY, Fierz or source-reality proof.

Historical archive comparisons are omitted; the current equations are checked.
Input polynomials below are authored from Step 2. The other side is parsed
from the actual nine expanded equations in the new note. Noncommuting words
preserve spinor/gamma order. Only even scalar factors commute. Tensor index
contractions are checked in the hand note, not proved by this word algebra.
"""
from collections import defaultdict
from pathlib import Path
import hashlib
import json
import re
import sympy as S

ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / 'notes/05_step3_mixed_linear_inserted_in_BF.md'
I = S.I
Q = S.Rational
checks = []

def check(ok, label):
    checks.append({'pass': bool(ok), 'check': label})

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def clean(tex):
    tex = re.sub(r'\\tag\{\d+\}', '', tex)
    tex = tex.replace(r'\left.', '').replace(r'\right.', '')
    for token in [r'\begin{aligned}', r'\end{aligned}', r'\left', r'\right',
                  r'\!', r'\,', r'\quad', r'\qquad', r'\\', '&', '$$']:
        tex = tex.replace(token, '')
    tex = re.sub(r'\\hspace\{[^}]+\}', '', tex)
    return re.sub(r'\s+', '', tex).replace('{}', '')

# Atomic entries: (weight, explicit odd-factor count, primed degree, unprimed degree).
# SL is exactly the retained symmetric bilinear, not a new physical field.
meta = {}
def atom(name, w, odd=0, prime=0, unprime=0):
    meta[name] = (Q(w), odd, prime, unprime)

for name in ['r', 'rp']:
    atom(name, 1, prime=int(name == 'rp'), unprime=int(name == 'r'))
for name in ['Y', 'Yp', 'F', 'Fp']:
    atom(name, 2, prime=int(name.endswith('p')), unprime=int(not name.endswith('p')))
for name in ['l', 'lp', 'bl', 'blp']:
    atom(name, Q(3,2), 1, prime=int(name.endswith('p')), unprime=int(not name.endswith('p')))
for name in ['dl', 'dlp', 'dblp']:
    atom(name, Q(5,2), 1, prime=int(name.endswith('p')), unprime=int(not name.endswith('p')))
for name in ['dr', 'drp', 'sr', 'srp']:
    atom(name, 2, prime=int(name.endswith('p')), unprime=int(not name.endswith('p')))
for name in ['boxr', 'boxrp', 'dF', 'dFp']:
    atom(name, 3, prime=int(name.endswith('p')), unprime=int(not name.endswith('p')))
atom('Ap', 1, prime=1)
atom('T', 1)
atom('dT', 2)
atom('D', 2)
atom('chi', Q(3,2), 1)
atom('bchi', Q(3,2), 1)
atom('ps', Q(1,2), 1)
atom('bps', Q(1,2), 1)
atom('SL', 3, 2, 1, 1)
for name in ['g1', 'g2', 'g3', 'eps']:
    atom(name, 0)

# Only these even scalar/tensor factors can move through an ordered spinor word.
# gamma matrices, slashed gradients and all fermions stay in sequence.
commuting = {'r','rp','Y','Yp','F','Fp','dr','drp','boxr','boxrp','dF','dFp',
             'Ap','T','dT','D','eps'}

def canon(word):
    return tuple(sorted(x for x in word if x in commuting)) + tuple(x for x in word if x not in commuting)

def polynomial(rows):
    out = defaultdict(lambda: S.Integer(0))
    for c, word in rows:
        out[canon(word)] += c
    return {w: S.simplify(c) for w,c in out.items() if c != 0}

def row(c, *word):
    return S.sympify(c), tuple(word)

# Independent compact component transcription, from corrected Step 2 (56)-(59).
# Both scalar-gradient coefficients use project repair R2-VL-GRADIENT-PHASE-v1;
# no other component coefficient is changed by that repair.
L = [row(1,'rp','Y'), row(1,'r','Yp'), row(-I/2,'SL')]
P = [row(I/2,'rp','dl'), row(I/2,'r','dlp'),
     row(1,'rp','g2','T','l'), row(1,'r','g2','T','lp'), row(-8,'rp','r','chi'),
     row(-Q(1,8),'g2','Fp','l'), row(-Q(1,8),'g2','F','lp'),
     row(I/4,'srp','l'), row(I/4,'sr','lp'),
     row(-Q(1,2),'Yp','l'), row(-Q(1,2),'Y','lp')]
N = [row(Q(1,2),'rp','boxr'), row(Q(1,2),'r','boxrp'),
     row(Q(1,2),'drp','dr'), row(-Q(1,4),'Fp','F'), row(1,'Yp','Y'),
     row(4,'rp','F','T'), row(4,'r','Fp','T'), row(-4,'rp','r','D'),
     row(-Q(104,3),'rp','r','T','T'), row(-Q(1,4),'blp','g1','dl'),
     row(-Q(1,4),'bl','g1','dlp'), row(I,'blp','g2','T','l'),
     row(8*I,'rp','bchi','l'), row(8*I,'r','bchi','lp')]

# A slash on a fermionic derivative has the explicit leading gamma.
P[0] = row(I/2,'rp','g1','dl')
P[1] = row(I/2,'r','g1','dlp')

E_inside = [row(-Q(1,2),'rp','F'), row(-Q(1,2),'r','Fp'),
            row(8,'rp','r','T'), row(-I/4,'blp','g2','l')]
derivative = {'rp':'drp','r':'dr','F':'dF','Fp':'dFp','T':'dT','blp':'dblp','l':'dl'}
E = []
for c, word in E_inside:
    # Even Leibniz rule: no parity-dependent sign.
    for k,x in enumerate(word):
        if x in derivative:
            E.append((c, word[:k] + (derivative[x],) + word[k+1:]))
E.append(row(-Q(1,8),'eps','Fp','F'))

# Source seven terms, with the source form term expanded into its three exact
# component terms. External prefactors are independent of the components.
groups = {
    'YL': (1, ('Yp',), L),
    'LP': (I, ('blp',), P),
    'PSL': (-Q(1,2), ('bps','g1','lp'), L),
    'AE': (1, ('Ap',), E),
    'APP': (I/2, ('Ap','bps','g2'), P),
    'APL': (Q(1,4), ('Ap','bps','g3','ps'), L),
    'RN': (1, ('rp',), N),
    'RPP': (Q(1,2), ('rp','bps','g1'), P),
    'RPL': (I/4, ('rp','bps','g2','ps'), L),
}

# Strict, finite lexer for the actual distributed TeX. Each token consumes its
# full printed indices; index equivalences here are explicitly enumerated.
tokens = {}
def tex(names, *word):
    for name in names:
        tokens[clean(name)] = tuple(word)

tex([r"(\rho')^2"], 'rp','rp')
tex([r"\rho'"], 'rp'); tex([r'\rho'], 'r')
tex([r"Y'^{ij}",r"Y'_{ij}"], 'Yp'); tex([r'Y^{ij}',r'Y_{ij}'], 'Y')
tex([r"\bar\lambda'_{(i}\lambda_{j)}"], 'SL')
tex([r"\bar\lambda'{}^i",r"\bar\lambda'"], 'blp')
tex([r'\bar\lambda'], 'bl')
tex([r"\lambda'{}^j",r"\lambda'_i",r"\lambda'"], 'lp')
tex([r'\lambda_i',r'\lambda^j',r'\lambda'], 'l')
tex([r"\not{\mathcal D}\lambda'_i",r"\not{\mathcal D}\lambda'"], 'g1','dlp')
tex([r'\not{\mathcal D}\lambda_i',r'\not{\mathcal D}\lambda'], 'g1','dl')
tex([r"(\not{\mathcal D}\rho')"], 'srp'); tex([r'(\not{\mathcal D}\rho)'], 'sr')
tex([r'\gamma\!\cdot\!T'], 'g2','T')
tex([r"\gamma\!\cdot\!\widehat F'"], 'g2','Fp')
tex([r'\gamma\!\cdot\!\widehat F'], 'g2','F')
tex([r'\bar\psi_a{}^i',r'\bar\psi_b{}^i'], 'bps')
tex([r'\psi_b{}^j',r'\psi_c{}^j'], 'ps')
tex([r'\gamma^a'], 'g1')
tex([r'\gamma^{ab}',r'\gamma^{ba}'], 'g2')
tex([r'\gamma^{abc}'], 'g3')
tex([r'\chi_i'], 'chi'); tex([r'\bar\chi'], 'bchi')
tex([r"A'_a"], 'Ap')
tex([r"(\mathcal D_b\rho')",r"\mathcal D_a\rho'"], 'drp')
tex([r'(\mathcal D_b\rho)',r'\mathcal D^a\rho'], 'dr')
tex([r'\widehat F^{ab}',r'\widehat F_{ab}',r'\widehat F_{de}'], 'F')
tex([r"\widehat F'^{ab}",r"\widehat F'_{ab}",r"\widehat F'_{bc}"], 'Fp')
tex([r'\mathcal D_b\widehat F^{ab}'], 'dF')
tex([r"\mathcal D_b\widehat F'^{ab}"], 'dFp')
tex([r'T^{ab}'], 'T'); tex([r'T^2'], 'T','T')
tex([r'\mathcal D_bT^{ab}'], 'dT')
tex([r"(\mathcal D_b\bar\lambda')"], 'dblp')
tex([r'\mathcal D_b\lambda'], 'dl')
tex([r'\varepsilon^{abcde}'], 'eps')
tex([r'\Box_c\rho'], 'boxr'); tex([r"\Box_c\rho'"], 'boxrp')
tex(['D'], 'D')

prefixes = {}
for den in [2,4,8,16]:
    for frac in [rf'\frac1{den}', rf'\frac1{{{den}}}', rf'\frac{{1}}{{{den}}}']:
        prefixes[frac] = (Q(1,den), ())
    for frac in [rf'\frac i{den}', rf'\frac i{{{den}}}', rf'\frac{{i}}{{{den}}}']:
        prefixes[clean(frac)] = (I/den, ())
for den in [2,4,8]:
    prefixes[rf"\frac{{\rho'}}{den}"] = (Q(1,den), ('rp',))
    prefixes[rf'\frac\rho{den}'] = (Q(1,den), ('r',))
prefixes[r'\frac{104}{3}'] = (Q(104,3), ())
for n in [8,4]:
    prefixes[f'{n}i'] = (n*I, ())
    prefixes[str(n)] = (S.Integer(n), ())
prefixes['i'] = (I, ())

def parse_terms(rhs):
    # All +/- within these distributed RHSs are top-level addition signs;
    # the finite token grammar contains no internal addition/subtraction.
    rhs = clean(rhs)
    parts = re.findall(r'([+-]?)([^+-]+)', rhs)
    out = []
    for sign, body in parts:
        c = S.Integer(-1 if sign == '-' else 1)
        word = ()
        for p in sorted(prefixes, key=len, reverse=True):
            if body.startswith(p):
                cc, ww = prefixes[p]
                c *= cc; word += ww; body = body[len(p):]
                break
        while body:
            for token in sorted(tokens, key=len, reverse=True):
                if body.startswith(token):
                    word += tokens[token]; body = body[len(token):]
                    break
            else:
                if body[0] in '().':
                    body = body[1:]
                else:
                    raise ValueError('Unparsed TeX suffix: '+body)
        out.append((c, word))
    return out

def main():
    text = DOC.read_text()
    parsed = {}
    ledger = []
    for name, (external_c, prefix, component) in groups.items():
        block = re.search(r'<!-- BEGIN EXPANSION '+name+r' -->(.*?)<!-- END EXPANSION '+name+r' -->', text, re.S)[1]
        rhs = block.rsplit('=', 1)[1]
        got = parse_terms(rhs)
        expected = [(external_c*c, prefix+w) for c,w in component]
        check(len(got) == len(expected), name+' complete row count')
        check(polynomial(got) == polynomial(expected), name+' exact ordered distribution matches compact BF substitution')
        parsed[name] = got
        for k,(c,w) in enumerate(got,1):
            weights = [meta[x][0] for x in w]
            odd = sum(meta[x][1] for x in w)
            degrees = [sum(meta[x][i] for x in w) for i in [2,3]]
            check(sum(weights) == 5, f'{name}-{k:02d} weight 5')
            check(odd % 2 == 0, f'{name}-{k:02d} even Grassmann parity')
            check(degrees == [2,1], f'{name}-{k:02d} primed/unprimed degrees (2,1), hence both zero-vector limits')
            ledger.append({'row':f'{name}-{k:02d}', 'coefficient':str(c),
                           'ordered_factors':list(w), 'factor_weights':[str(v) for v in weights],
                           'explicit_odd_factors':odd, 'vector_degrees':degrees})
    actual = [r for rows in parsed.values() for r in rows]
    expected_all = [(cc*c,prefix+w) for cc,prefix,comp in groups.values() for c,w in comp]
    check(len(actual) == 69, 'all 69 distributed rows present')
    check(polynomial(actual) == polynomial(expected_all), 'full seven-source-term density after complete bridge equals nine expanded groups')
    bos = [(c,w) for c,w in actual if not any(meta[x][1] for x in w)]
    bos_source = [(c,w) for c,w in expected_all if not any(meta[x][1] for x in w)]
    check(len(bos) == 19, 'bosonic restriction retains 19 distributed rows')
    check(polynomial(bos) == polynomial(bos_source), 'bosonic restriction agrees with compact BF substitution')
    check([c for c,w in parsed['PSL'] if 'SL' in w] == [I/4], 'first explicit quartic coefficient +i/4')
    check([c for c,w in parsed['APL'] if 'SL' in w] == [-I/8], 'form explicit quartic coefficient -i/8')
    check([c for c,w in parsed['RPL'] if 'SL' in w] == [Q(1,8)], 'last explicit quartic coefficient +1/8')

    # Final formula: audit each literal bracket against the input definitions.
    final = clean(re.search(r'<!-- BEGIN FINAL INSERTION -->(.*?)<!-- END FINAL INSERTION -->', text, re.S)[1])
    eqs = {int(tag):body for body,tag in re.findall(r'^\$\$\s*\n(.*?)\\tag\{(\d+)\}\s*\n\$\$', text, re.M|re.S)}
    Ltex = clean(eqs[2]).split('=',1)[1].rstrip('.')
    Ptex = clean(eqs[3]).split('=',1)[1].rstrip('.')
    Ntex = clean(eqs[5]).split('=',1)[1].rstrip('.')
    check(final.count('('+Ltex+')') == 4, 'final density contains all four literal L substitutions')
    check(final.count('['+Ptex+']') == 3, 'final density contains all three literal varphi substitutions')
    check(final.count('['+Ntex+']') == 1, 'final density contains the literal N substitution')
    for term in [r"L'_{ij}",r"\varphi'_i",r"E'^a",r"N'",r"E'_{\rho\sigma\tau}"]:
        check(term not in final, 'final formula eliminates output '+term)
    for prefix in [r"Y'^{ij}(", r"i\bar\lambda'{}^i[",
                   r"-\frac12\bar\psi_a{}^i\gamma^a\lambda'{}^j(",
                   r"+\frac i2A'_a\bar\psi_b{}^i\gamma^{ba}[",
                   r"+\frac14A'_a\bar\psi_b{}^i\gamma^{abc}\psi_c{}^j(",
                   r"+\rho'[", r"+\frac{\rho'}2\bar\psi_a{}^i\gamma^a[",
                   r"+\frac{i\rho'}4\bar\psi_a{}^i\gamma^{ab}\psi_b{}^j("]:
        check(clean(prefix) in final, 'final external BF factor '+prefix)
    expected_E = clean(r"+A'_a\mathcal D_b[-\frac12(\rho'\widehat F^{ab}+\rho\widehat F'^{ab})+8\rho'\rho T^{ab}-\frac i4\bar\lambda'\gamma^{ab}\lambda]-\frac18A'_a\varepsilon^{abcde}\widehat F'_{bc}\widehat F_{de}")
    check(expected_E in final, 'final E insertion retains full compact derivative and epsilon term')
    assembled_final = ''.join([
        clean(r"\boxed{e^{-1}\mathcal L_{VL}=Y'^{ij}("), Ltex, ')',
        clean(r"+i\bar\lambda'{}^i["), Ptex, ']',
        clean(r"-\frac12\bar\psi_a{}^i\gamma^a\lambda'{}^j("), Ltex, ')',
        expected_E,
        clean(r"+\frac i2A'_a\bar\psi_b{}^i\gamma^{ba}["), Ptex, ']',
        clean(r"+\frac14A'_a\bar\psi_b{}^i\gamma^{abc}\psi_c{}^j("), Ltex, ')',
        clean(r"+\rho'["), Ntex, ']',
        clean(r"+\frac{\rho'}2\bar\psi_a{}^i\gamma^a["), Ptex, ']',
        clean(r"+\frac{i\rho'}4\bar\psi_a{}^i\gamma^{ab}\psi_b{}^j("), Ltex, ').}'])
    check(final == assembled_final, 'entire boxed endpoint equals reconstructed nine substitutions, with no extra terms')
    # Independently test frame conversion with a nondiagonal exact frame.
    frame = S.Matrix([[2,1,0,0,0],[0,1,1,0,0],[0,0,3,1,0],[1,0,0,1,1],[0,0,1,0,2]])
    inv = frame.inv()
    A = S.Matrix([2,-3,5,7,-11])
    curl_world = S.Matrix([13,17,-19,23,-29])
    A_tangent = inv*A
    curl_tangent = frame.T*curl_world
    check(S.expand((A_tangent.T*curl_tangent)[0] - (A.T*curl_world)[0]) == 0,
          'exact nondiagonal inverse-frame contraction for the full three-form curl bridge')
    check([int(n) for n in re.findall(r'\\tag\{(\d+)\}',text)] == list(range(1,36)), '35 sequential numbered equations')
    check(not any(delim in text for delim in [r'\[',r'\]',r'\(',r'\)']), 'dollar equation delimiters only')
    for heading in ['Problem and Target','Convention Ledger','Definitions and Required Identities',
                    'Detailed Derivation','Consistency Checks','Final Result','Convention Dependence and Remaining Uncertainties']:
        check(bool(re.search(r'^## \d\. '+re.escape(heading)+r'$',text,re.M)), 'required section '+heading)
    assertions = re.findall(r'<!-- ASSERT_CONVENTION: (.*?) -->',text)
    check(len(assertions) == 11 and all('metric_signature=mostly_plus (-++++)' in a and
          'procedure_lock=R2-PRIMED-BF-CONSTRUCTION-FRAMEWORK-v1' in a for a in assertions),
          'ledger and all ten derivation steps retain convention lock')
    check(P[7][0]==I/4 and P[8][0]==I/4, 'both compact input gradients use corrected i/4')
    check(parse_terms(clean(eqs[3]).split('=',1)[1])==P,
          'entire displayed mixed fermion input matches independently authored corrected coefficients')
    # Inputs remain the currently verified corrected earlier steps.

    inputs = ['notes/03_step1_full_primed_BF_density.md','notes/04_step2_mixed_primed_linear_multiplet.md']
    failures = [c['check'] for c in checks if not c['pass']]
    report = {'status':'FAIL' if failures else 'PASS', 'checks':len(checks),
        'scope':'exact_locked_input_BF_insertion_ordered_distribution_and_stated_limits_only',
        'limitations':['No full local SUSY or source-reality proof','No Fierz reduction',
                       'No explicit gauged-composite completion','Tensor index audit is in the hand derivation'],
        'result_lock':'R2-MIXED-BF-INSERTION-v2','repair_lock':'R2-VL-GRADIENT-PHASE-v1','document':str(DOC.relative_to(ROOT)),
        'document_sha256':sha(DOC),'input_sha256':{p:sha(ROOT/p) for p in inputs},
        'distributed_rows':69,'bosonic_rows':len(bos),
        'failures':failures,'details':checks,'row_ledger':ledger}
    (ROOT/'build/step3_bf_insertion_verification.json').write_text(json.dumps(report,indent=2)+'\n')
    print(f"{report['status']}: {len(checks)} scoped checks; {len(actual)} distributed rows; {len(bos)} bosonic rows.")
    for failure in failures:
        print('FAIL:',failure)
    return bool(failures)

if __name__ == '__main__':
    raise SystemExit(main())
