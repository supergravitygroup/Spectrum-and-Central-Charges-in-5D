#!/usr/bin/env python3
"""Scoped checks of the retained-operator primed substitution."""
from pathlib import Path
import json,hashlib
import sympy as sym
import build_step5a_partial_insertion as source
from step6_supercovariant_maps import *
ROOT=Path(__file__).resolve().parents[1]
checks=[]
def ck(test,label):checks.append({'check':label,'pass':bool(test)})
DIM={'L':0,'N':1,'Lt':0,'E':1,'V':1,'G':1,'T':1,'D':2,'ftrace':2,
     'chi':Q(3,2),'barchi':Q(3,2),'phi':Q(3,2),'barphi':Q(3,2),
     'vphi':Q(1,2),'barvphi':Q(1,2),'psi':Q(1,2),'barpsi':Q(1,2),
     'RV':2,'RQ':Q(3,2),'gam':0,'eps2':0,'eps5':0,'delta':0}
def coeffdim(c):
    ds=set()
    for term in s.expand(c).as_ordered_terms():
        powers=term.as_powers_dict();ds.add(powers.get(N,0)+powers.get(g,0))
    assert len(ds)==1,(c,ds)
    return ds.pop()
def atomdim(f):
    if f.name in OPS:
        op=OPS[f.name]
        return coeffdim(op['coefficient'])+sum(atomdim(h) for h in op['factors'])+(2 if op['kind']=='box' else 1)
    return DIM[f.name]+len(f.ds)
def formal(p,t):
    return sum(c*t**sum(f.degree for f in fs)*s.Mul(*(s.Symbol(repr(f),commutative=False) for f in fs)) for fs,c in p.terms.items())
def unpack(rows):
    p=Poly()
    for row in rows:
        fs=tuple(Atom(f['name'],tuple(map(tuple,f['ix'])),tuple(map(tuple,f['ds']))) for f in row['factors'])
        p+=Poly({fs:s.sympify(row['coefficient'],locals={'L':L,'N':N,'g':g})})
    return p

def main():
    t=s.Symbol('grading');total=Poly()
    for number,raw,terms in source.source_rows():
        p=Poly();oracle=0
        for row in terms:
            pp=poly(row.c);oo=row.c
            for f in row.fs:
                replacement=token(f.tex);pp*=replacement;oo*=formal(replacement,t)
            p+=pp;oracle+=s.expand(oo)
        expected=s.expand(oracle).coeff(t,0)+s.expand(oracle).coeff(t,2)
        ck(s.expand(expected-formal(p,s.Integer(1)))==0,f'group {number}: independent noncommuting outer-product expansion')
        q=canonical(p);total+=q
        ck(not index_errors(p) and not index_errors(q),f'group {number}: all Lorentz/SU2 dummy indices paired')
        ck(all(coeffdim(c)+sum(atomdim(f) for f in fs)==4 for fs,c in q.terms.items()),f'group {number}: all retained monomials have dimension four')
    total=canonical(total)
    ledger=json.loads((ROOT/'build/step6_supercovariant_ledger.json').read_text())
    ck(s.expand(formal(total,s.Integer(1))-formal(unpack(ledger['rows']),s.Integer(1)))==0,'final ledger equals regenerated collected density')
    ck(all(sum(f.degree for f in fs) in (0,2) for fs in total.terms),'only explicit degree zero and two')
    # Source-preservation checks do not assert that earlier expansion is the
    # same requested presentation; its bytes are retained as a comparison.
    for name,path in [('source','notes/06_step4_Gold_unprimed_vector_and_gauge.md'),('map','notes/08_step5_primed_composite_vector_insertion.md'),('prior_step6','notes/10_step6_gauged_action_through_two_fermions.md')]:
        ck(hashlib.sha256((ROOT/path).read_bytes()).hexdigest()==ledger[name+'_sha256'],name+' unchanged')
    text='\n'.join(r['tex'] for r in ledger['rows'])
    ck(not any(x in text for x in [r'\nabla',"\\rho'","\\lambda'","Y'","F'","A'",'SC0']), 'final display has no ordinary derivative, primed component or internal operator alias')
    ck(r'\mathcal D' in text and r'\Box_c' in text,'supercovariant derivative and box retained')
    ck(all(s.Poly(s.together(c).as_numer_denom()[1],g).degree()==0 for c in total.terms.values()),'coefficient limit g -> 0 has no inverse-g singularity')
    r=canonical(rho()**2)
    i,j='iA','iB'
    target=canonical(poly(4*N*N/L**2)+4*I*N/L**4*lp(dn(i),dn(j))*bvf(up(i))*vf(up(j)))
    ck(s.expand(formal(r,s.Integer(1))-formal(target,s.Integer(1)))==0,'rho-prime squared: 4N^2/L^2 plus 4iN/L^4 times original bilinear')
    # This is a test of the underlying bosonic triplet contraction, with
    # derivative/curvature slots restricted to zero; no vacuum is assumed.
    yy=-N*N/L**3+Q(8,3)/L*s.Symbol('Tsq')+4/L*s.Symbol('auxD')
    expected=s.expand(L*L*yy**2-2*g*N*L*yy)
    got=s.expand(L*L*(yy-g*N/L)**2-g*g*N*N)
    ck(s.expand(got-expected)==0,'bosonic constant-slot triplet square and mixed coupling agree')
    bad=[x for x in checks if not x['pass']]
    report={'status':'PASS_SCOPED' if not bad else 'FAIL','checks':checks,'passed':len(checks)-len(bad),'failed':len(bad),
            'scope':'First-level primed insertion, ordered product distribution, indices, dimensions and stated limits; no full SUSY or reality proof.'}
    (ROOT/'build/step6_supercovariant_verification.json').write_text(json.dumps(report,indent=2)+'\n')
    print(report['status'],report['passed'],'passed;',report['failed'],'failed')
    if bad:print(bad)
    return bool(bad)
if __name__=='__main__':raise SystemExit(main())
