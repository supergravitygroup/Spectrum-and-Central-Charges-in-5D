#!/usr/bin/env python3
"""Step 4 exact substitution/restriction audit, not full action certification.

Historical archive comparisons are omitted. Compare actual printed Step 4 equations with a direct restriction of the
Step 3 ordered rows; evaluate the zero-gaugino connections before dropping
fields. Keep spinor/gamma order. No Fierz or gamma-rank reduction is used.
"""
from pathlib import Path
from collections import defaultdict
import importlib.util
import hashlib
import json
import re
import sympy as S

ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT/'notes/06_step4_Gold_unprimed_vector_and_gauge.md'
spec = importlib.util.spec_from_file_location('step3_input', ROOT/'scripts/verify_step3_bf_insertion.py')
prior = importlib.util.module_from_spec(spec)
spec.loader.exec_module(prior)
Q, I = S.Rational, S.I
g = S.Symbol('g', real=True)
checks = []
def check(ok, label): checks.append({'pass':bool(ok),'check':label})
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def row(c,*w): return S.sympify(c),tuple(w)

commute = prior.commuting | {'L','Gh','dGh','ft','boxsigma'}
def canon(w):
    return tuple(sorted(x for x in w if x in commute))+tuple(x for x in w if x not in commute)
def poly(rows):
    out=defaultdict(lambda:S.Integer(0))
    for c,w in rows: out[canon(w)]+=c
    return {w:S.expand(c) for w,c in out.items() if S.expand(c)!=0}
def mul(a,b): return [(c*d,w+v) for c,w in a for d,v in b]
def replace(rows,rules):
    out=[]
    for c,w in rows:
        accum=[(c,())]
        for x in w: accum=mul(accum,rules.get(x,[(S.Integer(1),(x,))]))
        out+=accum
    return out

# Full restriction of source atoms. A derivative of the gaugino is NOT zero.
rules={'r':[row(1)], 'l':[], 'bl':[], 'SL':[], 'dr':[], 'sr':[],
       'Y':[row(-g/2,'L')], 'F':[row(1,'Gh')], 'dF':[row(1,'dGh')],
       'dl':[row(1,'du')], 'boxr':[row(1,'boxsigma')]}
du=[row(Q(1,4),'g2','Gh','ps'),row(-1,'g2','T','ps'),
    row(g/2,'L','ps'),row(-1,'phi')]
boxsigma=[row(2,'ft'),row(-I/2,'bps','du'),row(-2,'bps','g1','chi')]

# Copy only the previous strict TeX lexer, then extend for the new printed
# quantities. Every printed index pattern here is explicit; the separate
# epsilon-matrix check handles the nontrivial lowering sign.
tokens=dict(prior.tokens)
def tex(strings,*w):
    for t in strings: tokens[prior.clean(t)]=tuple(w)
tex([r'L_{ij}',r'L^{ij}'],'L')
tex([r'\widehat G^{ab}',r'\widehat G_{ab}',r'\widehat G_{de}'],'Gh')
tex([r'\mathcal D_b\widehat G^{ab}'],'dGh')
tex([r'\gamma\!\cdot\!\widehat G'],'g2','Gh')
tex([r'\not{\mathcal D}\psi_i'],'g1','du')
tex([r'\mathcal D_b\psi_i',r'\mathcal D^a\psi_i'],'du')
tex([r'\Box_c\sigma'],'boxsigma')
tex([r'f_a{}^a'],'ft')
tex([r'\psi_{ai}',r'\psi_{bi}',r'\psi_{ci}',r'\psi^a_i',
     r'\psi_a{}^j',r'\psi_b{}^j',r'\psi_c{}^j',r'\psi^{aj}'],'ps')
tex([r'\phi_{ai}',r'\phi_{bi}',r'\phi_{ci}',r'\phi^a_i'],'phi')
tex([r'\gamma^a',r'\gamma^b',r'\gamma^c'],'g1')
tex([r'\chi_i'],'chi')
tex([r'\rho\prime'],'rp') # no such spelling is generated; primes in the note use apostrophes
tokens.pop(prior.clean(r'\rho\prime'))

def argument(s):
    """Consume one TeX fraction argument (brace group, macro or character)."""
    if s[0]=='{':
        depth=1
        for k in range(1,len(s)):
            depth += (s[k]=='{')-(s[k]=='}')
            if depth==0:return s[1:k],s[k+1:]
        raise ValueError('unclosed argument '+s)
    if s[0]=='\\':
        m=re.match(r"\\[A-Za-z]+\'?",s)
        return m[0],s[len(m[0]):]
    return s[0],s[1:]

def top_terms(s):
    start=0;depth=0
    for k,ch in enumerate(s):
        if ch=='[':depth+=1
        elif ch==']':depth-=1
        elif ch in '+-' and depth==0 and k>start:
            yield s[start:k];start=k
    yield s[start:]

def parse_sum(s):
    s=prior.clean(s)
    return [r for part in top_terms(s) for r in parse_product(part)]

def parse_product(s):
    out=[row(1)]
    if s.startswith(('+','-')):
        out=[row(-1 if s[0]=='-' else 1)];s=s[1:]
    while s:
        if s.startswith(r'\frac'):
            num,s=argument(s[len(r'\frac'):]);den,s=argument(s)
            if not den.isdigit():raise ValueError('non-numeric denominator '+den)
            out=mul(out,[(c/Q(den),w) for c,w in parse_product(num)])
            continue
        if s[0]=='[':
            depth=1
            for k in range(1,len(s)):
                depth+=(s[k]=='[')-(s[k]==']')
                if depth==0:break
            out=mul(out,parse_sum(s[1:k]));s=s[k+1:];continue
        for t in sorted(tokens,key=len,reverse=True):
            if s.startswith(t):
                out=mul(out,[row(1,*tokens[t])]);s=s[len(t):];break
        else:
            if s[0].isdigit():
                m=re.match(r'\d+',s);out=mul(out,[row(int(m[0]))]);s=s[len(m[0]):]
            elif s[0]=='i':out=mul(out,[row(I)]);s=s[1:]
            elif s[0]=='g':out=mul(out,[row(g)]);s=s[1:]
            elif s[0] in '().':s=s[1:]
            else:raise ValueError('unparsed suffix: '+s)
    return out

def block(text,typ,name):
    return re.search('<!-- BEGIN '+typ+' '+name+' -->(.*?)<!-- END '+typ+' '+name+' -->',text,re.S)[1]
def rhs(b):return prior.clean(b.rsplit('=',1)[1])

def main():
    text=DOC.read_text();old=prior.DOC.read_text()
    fixed={};ledger=[];zero=[]
    for name in prior.groups:
        source=prior.parse_terms(block(old,'EXPANSION',name).rsplit('=',1)[1])
        expected=replace(source,rules)
        actual=parse_sum(rhs(block(text,'GAUGE',name)))
        fixed[name]=actual
        check(poly(actual)==poly(expected),name+' printed gauge result equals direct restriction of prior rows')
        check(len(actual)==len(expected),name+' surviving source-row count')
        # Explicit source-to-Gold transcription audit of all pre-gauge rows.
        parent_body=block(old,'EXPANSION',name).rsplit('=',1)[1]
        wanted=re.sub(r"\\rho(?!')",r'\\sigma',parent_body)
        wanted=re.sub(r"\\lambda(?!')",r'\\psi',wanted)
        wanted=re.sub(r"\\widehat F(?!')",r'\\widehat G',wanted)
        wanted=wanted.replace('Y_{ij}',r'\left(\frac{i}{4\sigma}\bar\psi_i\psi_j-\frac{g}{2\sigma}L_{ij}\right)')
        wanted=wanted.replace('Y^{ij}',r'\left(\frac{i}{4\sigma}\bar\psi^i\psi^j-\frac{g}{2\sigma}L^{ij}\right)')
        got=rhs(block(text,'GOLD',name))
        # Both sides end in the same equation-environment and tag, removed by clean.
        check(got==prior.clean(wanted),name+' complete printed pre-gauge Gold substitution')
        for k,(c,w) in enumerate(source,1):
            mapped=replace([(c,w)],rules)
            removed=[x for x in w if x in rules and rules[x]==[]]
            if not mapped:zero.append(f'{name}-{k:02d}')
            check(bool(mapped)==(not removed),f'{name}-{k:02d} vanishes iff a proven zero factor is present')
            check(sum(prior.meta[x][0] for x in w)==5,f'{name}-{k:02d} parent Weyl weight 5 before weight-preserving Gold map')
            ledger.append({'source_row':f'{name}-{k:02d}','vanishes':not bool(mapped),'zero_factors':removed,
                           'restricted_terms':[{'coefficient':str(d),'word':list(v)} for d,v in mapped]})
    all_fixed=[r for rows in fixed.values() for r in rows]
    check(len(zero)==26,'26 vanished rows explicitly accounted for')
    check(len(all_fixed)==43,'43 surviving rows before collections and derivative expansion')
    # The new derivative groups are independently supplied by their external
    # prefactors, not obtained by parsing their own output.
    prefixes={
        'X1':(-Q(3,4),('rp','blp','g1')),
        'X2':(-I/4,('Ap','blp','g2')),
        'X3':(-Q(1,4),('Ap','rp','bps','g2','g1')),
        'X4':(I/4,('rp','rp','bps','g1','g1')),
        'X5':(-I/4,('rp','rp','bps'))}
    for name,(c,w) in prefixes.items():
        got=parse_sum(rhs(block(text,'DERIVATIVE',name)))
        check(len(got)==4,name+' all four derivative contributions present')
        check(poly(got)==poly(mul([(c,w)],du)),name+' exact coefficients and spinor/gamma ordering')
    # Independent route: restrict each prior row, then expand Box sigma and D psi.
    expected_final=replace(replace(all_fixed,{'boxsigma':boxsigma}),{'du':du})
    final_block=re.search(r'<!-- BEGIN FINAL GOLD GAUGE -->(.*?)<!-- END FINAL GOLD GAUGE -->',text,re.S)[1]
    final_rhs=rhs(final_block)
    assert final_rhs.endswith('}')
    final_rhs=final_rhs[:-1] # outer boxed environment only
    actual_final=parse_sum(final_rhs)
    check(len(actual_final)==57,'57 distributed rows in final expression before Clifford/Fierz reduction')
    check(poly(actual_final)==poly(expected_final),'entire printed boxed endpoint equals independent restriction and derivative expansion')
    forbidden=[r'\not{\mathcal D}\psi_i',r'\mathcal D_b\psi_i',r'\mathcal D^a\psi_i',
               r'\Box_c\sigma',r'L\prime',r'\varphi\prime']
    for f in forbidden:check(prior.clean(f) not in final_rhs,'endpoint has no residual '+f)
    for f in [r"\\rho(?!')",r"\\lambda(?!')",r"\\widehat F(?!')",r"(?<![A-Za-z'])Y(?:_|\^)"]:
        check(not re.search(f,final_block),'no unprimed vector token matching '+f)
    check('du' not in {x for c,w in actual_final for x in w},'all zero-gaugino derivatives evaluated')
    check('boxsigma' not in {x for c,w in actual_final for x in w},'constant compensator box evaluated')

    odd={k:v[1] for k,v in prior.meta.items()}
    odd.update(L=0,Gh=0,dGh=0,ft=0,boxsigma=0,du=1,phi=1)
    for k,(c,w) in enumerate(actual_final,1):
        check(sum(odd[x] for x in w)%2==0,f'final row {k:02d} is Grassmann even')
    bos_actual=[(c,w) for c,w in actual_final if not any(odd[x] for x in w)]
    bos_expected=[(c,w) for c,w in expected_final if not any(odd[x] for x in w)]
    check(len(bos_actual)==15,'15 displayed bosonic rows after collection')
    check(poly(bos_actual)==poly(bos_expected),'bosonic restriction commutes with complete insertion')
    # Independent source bosonic equation route: prior source rows, discard
    # odd factors first, substitute map and evaluate Box sigma = 2 f.
    old_rows=[r for n in prior.groups for r in prior.parse_terms(block(old,'EXPANSION',n).rsplit('=',1)[1])]
    old_bos=[(c,w) for c,w in old_rows if not any(prior.meta[x][1] for x in w)]
    old_bos_fixed=replace(replace(old_bos,rules),{'boxsigma':[row(2,'ft')]})
    check(poly(bos_actual)==poly(old_bos_fixed),'independent Step 3 bosonic restriction gives final bosonic expression')
    check(poly([(c.subs(g,0),w) for c,w in actual_final])==
          poly([(c.subs(g,0),w) for c,w in expected_final]),'explicit g=0 restriction, common background held fixed')
    # NW-SE index test: no spinor products or flips, only a linear index map.
    eps=S.Matrix([[0,1],[-1,0]])
    L=S.Matrix([[2,3],[3,5]])
    pu=S.Matrix([7,11])
    Lu=eps*L*eps.T;pl=eps.T*pu
    check(eps.T*Lu*pl == -L*pu,'nontrivial exact SU(2) lower-index sign L^{kj} psi_j epsilon_ki = -L_ij psi^j')
    check((-g/2)*(eps.T*Lu*pl)==(g/2)*L*pu,'lowered gauging coefficient is +g/2')
    check(eps.T*Lu*eps==L,'double lowering of a triplet has no extra sign')
    check(-1+Q(3,2)+Q(3,2)==2,'Gold fermion bilinear has triplet weight 2')
    check(0-1+3==2,'Gold g sigma^{-1} L has triplet weight 2')
    check(-Q(1,4)*I/2 == -I/8,'mixed hatted strength retains gravitino coefficient -i/8')
    # Simple exact evaluations of scalar coefficients, with noncommuting words
    # still distinct; this is not a replacement of Grassmann fields by numbers.
    for gv in [Q(0),Q(2,3),Q(-5,7)]:
        check(poly([(c.subs(g,gv),w) for c,w in actual_final])==poly([(c.subs(g,gv),w) for c,w in expected_final]),f'exact coefficient spot check g={gv}')
    tags=[int(n) for n in re.findall(r'\\tag\{(\d+)\}',text)]
    check(tags==list(range(1,49)),'48 sequential numbered equations')
    check(not any(d in text for d in [r'\[',r'\]',r'\(',r'\)']),'dollar delimiters only')
    for h in ['Problem and Target','Convention Ledger','Definitions and Required Identities','Detailed Derivation','Consistency Checks','Final Result','Convention Dependence and Remaining Uncertainties']:
        check(bool(re.search(r'^## \d\. '+re.escape(h)+'$',text,re.M)),'required section '+h)
    assertions=re.findall(r'<!-- ASSERT_CONVENTION: (.*?) -->',text)
    check(len(assertions)>=15 and all('metric_signature=mostly_plus (-++++)' in a and 'gauge_slice=R2-GOLD7-GAUGE-v1' in a for a in assertions),'all current convention assertions retain gauge and signature lock')
    step3report=json.loads((ROOT/'build/step3_bf_insertion_verification.json').read_text())
    check(sha(prior.DOC)==step3report['document_sha256'],'corrected gauge-unfixed Step 3 parent matches current verification hash')
    failures=[c['check'] for c in checks if not c['pass']]
    report={'status':'FAIL' if failures else 'PASS','checks':len(checks),
        'scope':'Gold4_substitution_Gold7_restriction_derivative_connections_ordered_algebra_only',
        'result_lock':'R2-GOLD4-UNPRIMED-SUBSTITUTION-v2','gauge_lock':'R2-GOLD7-GAUGE-v1','repair_lock':'R2-VL-GRADIENT-PHASE-v1',
        'document':str(DOC.relative_to(ROOT)),'document_sha256':sha(DOC),
        'parent_document_sha256':sha(prior.DOC),'vanished_rows':zero,
        'surviving_rows_before_collection':len(all_fixed),'final_distributed_rows':len(actual_final),
        'final_bosonic_rows':len(bos_actual),
        'failures':failures,'details':checks,'source_row_ledger':ledger,
        'limitations':['No complete source-reality or local SUSY proof','No Fierz/gamma reduction',
                       'Tensor contractions audited in the hand note','Common gauged composites and primed map remain unexpanded']}
    (ROOT/'build/step4_gold_gauge_verification.json').write_text(json.dumps(report,indent=2)+'\n')
    print(f"{report['status']}: {len(checks)} scoped checks; {len(zero)} zero rows, {len(all_fixed)} survivors, {len(actual_final)} final distributed rows.")
    for f in failures:print('FAIL:',f)
    return bool(failures)

if __name__=='__main__':raise SystemExit(main())
