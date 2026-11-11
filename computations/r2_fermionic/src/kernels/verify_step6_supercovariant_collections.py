"""Exact collection identities, coverage, dimensions, and expanded contractions."""
import json,hashlib
from pathlib import Path
import step6_supercovariant_collections as c
from step6_supercovariant_collections import *
import verify_step6_supercovariant as baseline

checks=[]
def ck(x,label):checks.append({'check':label,'pass':bool(x)})
def zero(p):return not canonical(p).terms
def dim(f):
    if f.name in HELD:
        values={baseline.coeffdim(cc)+sum(dim(a) for a in fs) for fs,cc in HELD[f.name]['p'].terms.items()}
        assert len(values)==1,(f,values)
        return values.pop()
    if f.name in OPS:
        op=OPS[f.name]
        return baseline.coeffdim(op['coefficient'])+sum(dim(a) for a in op['factors'])+(2 if op['kind']=='box' else 1)
    return baseline.DIM[f.name]+len(f.ds)

def main():
    # General triplets and the symmetric fixed-index vector bilinear.
    u,v,w,p,q,r,b,d,e=s.symbols('u v w p q r b d e')
    S=s.Matrix([[u,v],[v,w]]);P=s.Matrix([[p,q],[q,r]]);B=s.Matrix([[b,d],[d,e]])
    J=s.Matrix([[0,1],[-1,0]])
    adj=lambda x:J*x*J.T
    sym=lambda x:(x+x.T)/2
    ck(all(s.expand(x)==0 for x in P*adj(S)*P-s.trace(adj(S)*P)*P+P.det()*S),'general triplet derivative identity, every matrix entry')
    ck(all(s.expand(x)==0 for x in sym(S*J*B*adj(S)*P)-s.trace(adj(B)*S)*sym(S*J*P)-S.det()*sym(P*J*B)),'general triplet/bilinear derivative identity, every matrix entry')
    ck(s.trace(J*B)==0,'identical-spinor vector singlet vanishes against epsilon')
    ck(s.simplify(-3*Q(1,2)+Q(1,2))==-1,'derivative-bilinear coefficient -3/2+1/2=-1')
    rr,dr,GG,dGG,TT,dTT,FF,dFF,AA=s.symbols('rho Dr G DG T DT F DF A')
    before=-AA*dr*GG/2-AA*rr*dGG/2-AA*dFF/2+8*AA*dr*TT+8*AA*rr*dTT
    after=-AA*(dFF+dr*(GG-16*TT)+rr*(dGG-16*dTT))/2
    ck(s.expand(before-after)==0,'groups 11–15: inverse covariant product rule')
    ck(s.expand(-rr*FF*GG/4+4*rr*FF*TT+rr*FF*(GG-16*TT)/4)==0,'groups 28,30: strength collection')
    ck(-8*I-8*I==-16*I,'groups 5,33: contracted scalar Majorana flip coefficient')
    X,Z=s.symbols('gamma_antisymmetric metric')
    ck(s.expand(I*(X+Z)/4-I*Z/4-I*X/4)==0,'groups 39,40: Clifford metric part cancels')
    i,j='i','j';a,b='a','b'
    ck(zero(bch(up(i))*(expanded(lam(dn(i)))-original_lam(dn(i)))),'compact gaugino expands to all original linear terms')
    ck(zero((expanded(Fh(dn(a),dn(b)))-original_Fh(dn(a),dn(b)))*Gh(up(a),up(b))),'antisymmetric strength expands to original hatted map')
    result,total=build()
    coverage=[k for gr in result['groups'] for k in gr['sources']]
    ck(sorted(coverage)==list(range(1,43)) and len(set(coverage))==42,'each source group occurs exactly once')
    ck(not index_errors(total),'all final scalar contractions have paired opposite-variance indices')
    ck(all(baseline.coeffdim(cc)+sum(dim(a) for a in fs)==4 for fs,cc in total.terms.items()),'all final terms have engineering dimension four, recursively through held sums')
    ck(all(sum(a.degree for a in fs) in (0,2) for fs in total.terms),'all final terms contain zero or two explicit fermions')
    # Checking every final word after expanding its held tensor nodes catches
    # false Clifford contractions across a protected matrix or index block.
    for k,(fs,cc) in enumerate(total.terms.items(),1):
        expanded_word=expanded(Poly({fs:cc}))
        ck(not index_errors(expanded_word),f'final word {k}: held-node expansion has valid indices')
    # Source maps and the earlier bosonic report must retain their exact bytes.
    old=json.loads((ROOT/'build/step6_supercovariant_ledger.json').read_text())
    for key in ['source_sha256','map_sha256','prior_step6_sha256']:
        ck(result[key]==old[key],key+' preserved')
    txt='\n'.join(r['tex'] for r in result['rows'])
    ck(not any(a in txt for a in ['HC','SC0',"\\rho'","\\lambda'","Y'","F'","A'",r'\nabla']), 'no internal aliases, primed component, or ordinary derivative in delivered rows')
    ck('^{[' in txt or '_{[' in txt,'antisymmetric index pairs are printed')
    ck('_{(' in txt or '^{(' in txt,'symmetric index pairs are printed')
    ck(all(s.Poly(s.together(cc).as_numer_denom()[1],g).degree()==0 for cc in total.terms.values()),'coefficient ungauged limit has no inverse-g singularity')
    failed=[x for x in checks if not x['pass']]
    report={'status':'PASS_SCOPED' if not failed else 'FAIL','passed':len(checks)-len(failed),'failed':len(failed),'checks':checks,
      'ledger_sha256':hashlib.sha256((ROOT/'build/step6_supercovariant_collected_ledger.json').read_bytes()).hexdigest(),
      'scope':'Exact triplet, coefficient and derivative identities; complete source-group coverage; dimensions, indices and explicit grading. Majorana-aware numerical map check is separate. No full SUSY or reality proof.'}
    (ROOT/'build/step6_supercovariant_collection_verification.json').write_text(json.dumps(report,indent=2)+'\n')
    print(report['status'],report['passed'],'passed;',len(failed),'failed',failed[:3])
    return bool(failed)
if __name__=='__main__':raise SystemExit(main())
