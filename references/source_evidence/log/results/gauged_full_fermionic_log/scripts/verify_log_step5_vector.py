"""LOG vector descent, with explicit degree <=2 selected after both derivatives.

Exact rational coefficients for the covariant algebra; independent original
eight-derivative, exterior-algebra comparisons on flat constant jets. This is
not a certificate of the full curved multiplet or the potential bridge.
"""
import json,pickle,itertools as it,hashlib
from pathlib import Path
from collections import Counter
import numpy as np
import log_step4_covariant_rules as b
import verify_log_step3_spinor as v
BASE=Path(__file__).resolve().parents[1]
OUT=BASE/'sources/step5'

def degree(fs):return sum(f.parity for f in fs)
def keep(p,n=2):return b.P.terms([(c,fs) for c,fs in p.ts if degree(fs)<=n])
def vector_trace(p):
    return b.I*b.Q(1,12)*b.field('G','+lV','+sZ','+sE')*b.eps('-uI','-uT')*b.eps('-uJ','-uR')*p

def build():
    polys={};coverage=[]
    for key,p in b.make_inputs().items():
        spin=b.a.deriv(p)
        second=b.dpoly(spin,'sZ','uT')
        vector=keep(vector_trace(second))
        b.check(vector,b.Q(4),{'lV':'+'})
        b.check(b.normalize(vector,True),b.Q(4),{'lV':'+'})
        assert all(not f.oddD for c,fs in vector.ts for f in fs)
        # Check the safe early truncation against late truncation, including
        # every cubic spinor term, not just the linear spinor.
        safe=keep(vector_trace(b.dpoly(keep(spin,3),'sZ','uT')))
        # Fresh dummy names differ; displayed alpha-renaming is the comparison.
        assert b.texterms(vector)==b.texterms(safe),key
        polys[key]=vector
        coverage.append({'input':key,'primary_degree':sorted({degree(fs) for c,fs in p.ts}),
            'spinor_terms':len(spin.ts),'retained_spinor_terms':len(keep(spin,3).ts),
            'second_derivative_degrees':dict(sorted(Counter(degree(fs) for c,fs in second.ts).items())),
            'retained_vector_contributions':len(vector.ts)})
    return polys,coverage

def expected(F,X,grad):
    raw=v.n['raw'](F,X,grad)
    fb=sum(F[c,d]*v.SD[c,d]/2 for c,d in it.product(range(5),repeat=2))
    vb=sum(grad[c]*v.GD[c] for c in range(5));qq=np.zeros((8,8),complex)
    for s,r,t,k in it.product(range(4),range(2),range(4),range(2)):
        qq[2*s+r,2*t+k]=-2*v.E[r,k]*fb[s,t]-v.C[s,t]*X[r,k]-v.E[r,k]*vb[s,t]
    out={};uncontracted={}
    for zeta,t,eta,r,i,j in it.product(range(4),range(2),range(4),range(2),range(2),range(2)):
        first=v.n['deriv'](2*eta+r,raw[tuple(sorted((i,j)))],qq)
        last=v.n['deriv'](2*zeta+t,first,qq)
        pref=(-v.E[i,t])*(-v.E[j,r])*1j/12
        for (pole,mask),val in last.items():
            if mask.bit_count()>2:continue
            for a in range(5):
                key=((a,),pole,mask)
                out[key]=out.get(key,0)+pref*v.GU[a,zeta,eta]*val/30720
    return {key:val for key,val in out.items() if abs(val)>1e-8}

def case(pol,label,F,X,grad):
    got,nterms=v.evaluate(pol,F,X,grad,output=('lV',))
    exp=expected(F,X,grad)
    worst=max([abs(got.get(k,0)-exp.get(k,0)) for k in set(got)|set(exp)]+[0])
    assert worst<1e-7,(label,worst)
    # Constant-jet divergence: only W varies. The covector grad contracts H^a.
    div={}
    for (a,),pole,mask in got:
        key=(pole+1,mask);div[key]=div.get(key,0)-pole*grad[a]*got[((a,),pole,mask)]
    worstdiv=max([abs(x) for x in div.values()]+[0])
    assert worstdiv<1e-7,(label,'divergence',worstdiv)
    return {'case':label,'status':'PASS','compared_coefficients':len(set(got)|set(exp)),
        'nonzero_vector_coefficients':len(got),'retained_written_terms_in_probe':nterms,
        'max_absolute_difference':float(worst),'constant_jet_divergence_residual':float(worstdiv)}

if __name__=='__main__':
    OUT.mkdir(exist_ok=True)
    polys,coverage=build();pol=sum(polys.values(),b.P())
    with open('/private/tmp/log-vector-two-fermi.pkl','wb') as f:pickle.dump(polys,f)
    (OUT/'derivation_coverage.json').write_text(json.dumps({'inputs':coverage},indent=2)+'\n')
    print('Built',len(pol.ts),'retained contributions',flush=True)
    # Independent gamma trace normalization in all 25 Lorentz components.
    norm=np.einsum('aij,bij->ab',v.GU,v.GD)
    assert np.max(abs(norm+4*np.diag(v.eta)))<1e-12,norm
    assert np.max(abs(np.einsum('aij,ij->a',v.GU,v.C)))<1e-12
    F=np.zeros((5,5));F[0,1]=2;F[1,0]=-2;F[2,3]=3;F[3,2]=-3
    X=np.array([[2,3],[3,5]]);grad=np.array([1,2,3,4,5]);rng=np.random.default_rng(230526)
    cases=[('X only',F*0,X,grad*0),('F only',F,X*0,grad*0),('gradient only',F*0,X*0,grad),('F X gradient',F,X,grad)]
    for j in range(3):
        ff=rng.integers(-2,3,(5,5));xx=rng.integers(-2,3,(2,2));gg=rng.integers(-2,3,5)
        cases.append((f'integer probe {j+1}',ff-ff.T,xx+xx.T,gg))
    report={'status':'PASS','scope':'Unreduced Gold-superspace vector through two explicit fermions. Flat constant-jet checks, gamma normalization, index/weight/parity and truncation audit; full curved transformation and reality checks not certified.',
       'retained_contributions':len(pol.ts),'degrees':dict(Counter(degree(fs) for c,fs in pol.ts)),
       'gamma_trace':norm.real.tolist(),'checks':[]}
    for label,ff,xx,gg in cases:
        row=case(pol,label,ff,xx,gg);report['checks'].append(row);print(row,flush=True)
    row=case(b.normalize(pol,True),'index-raised displayed form',ff,xx,gg)
    report['checks'].append(row);print(row,flush=True)
    report['source_hashes']={f:hashlib.sha256((BASE/f).read_bytes()).hexdigest() for f in ['STEP_02_LOG_PRIMARY.md','STEP_03_LOG_SPINOR.md','STEP_04_LOG_SCALAR.md','scripts/log_step3_covariant_rules.py','scripts/log_step4_covariant_rules.py']}
    (OUT/'checks.json').write_text(json.dumps(report,indent=2)+'\n')
