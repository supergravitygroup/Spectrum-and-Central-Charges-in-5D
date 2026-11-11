"""Independent finite tensor contractions versus original seven derivative words."""
import sys,runpy,json,time,hashlib
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parent))
import log_step3_covariant_rules as a
from pathlib import Path
import numpy as np,itertools as it
base=Path(__file__).resolve().parents[1]
n=runpy.run_path(str(base/'scripts/verify_log_step2.py'))
# Fixed source matrices are numerical only. Candidate terms are fully expanded first.
C,U,E,G,GD,GU,S,SD,SU,eta=[n[k] for k in ['C','U','E','G','GD','GU','S','SD','SU','eta']]

def arr(f,F,X,v):
 if f.oddD:raise ValueError('unevaluated spinor derivative')
 if f.name=='pow':return np.array(1)
 if f.name in ['w','ws','x','w3','w3a','z','za','Y','w4','T','RM','RD','RJ','RS','RK']:return None
 if f.ds:
  if f.name=='W' and len(f.ds)==1:return v.copy()* (eta if f.ds[0][0]=='+' else 1)
  return None
 if f.name=='W':return np.array(1)
 if f.name=='L':
  # Separate exterior generator selector in the last axis.
  t=np.eye(8).reshape(4,2,8).astype(complex)
 elif f.name=='X':t=X.copy()
 elif f.name=='F':t=F.copy()
 elif f.name=='Fs':t=sum(F[c,d]*SD[c,d]/2 for c,d in it.product(range(5),repeat=2))
 elif f.name=='eps':return (E if f.ix[0][0]=='+' else -E) if f.ix[0][1]=='u' else (U if f.ix[0][0]=='+' else C)
 elif f.name=='eta':return np.diag(eta)
 elif f.name=='del':return np.eye(2 if f.ix[0][1]=='u' else 4 if f.ix[0][1]=='s' else 5)
 elif f.name=='eps5':
  t=np.zeros((5,)*5)
  for ids in it.permutations(range(5)):t[ids]=-n['cc']['eps'](ids)
  # canonical epsilon is all upper
  for axis,x in enumerate(f.ix):
   if x[0]=='-':t=t*np.reshape(eta,[5 if q==axis else 1 for q in range(5)])
  return t
 elif f.name=='G':t=GD.copy()*eta[:,None,None] # canonical all lower
 elif f.name=='S':t=SD.copy()*eta[:,None,None,None]*eta[None,:,None,None]
 else:raise ValueError(f)
 # fields canonical: Lor/spin lower; SU2 upper. Convert each requested variance.
 for axis,x in enumerate(f.ix):
  want='+' if x[1]=='u' else '-'
  if x[0]==want:continue
  if x[1]=='l':t=t*np.reshape(eta,[5 if q==axis else 1 for q in range(t.ndim)])
  else:
   metric=-E if x[1]=='u' else U
   t=np.moveaxis(np.tensordot(metric,t,axes=(1,axis)),0,axis)
 return t

from functools import lru_cache
@lru_cache(None)
def exterior_basis(k):
 ids=[];masks=[];signs=[]
 for js in it.permutations(range(8),k):
  ids.append(js);masks.append(sum(1<<x for x in js));signs.append((-1)**sum(js[p]>js[q] for p in range(k) for q in range(p+1,k)))
 return np.array(ids,dtype=int),np.array(masks),np.array(signs)

def evaluate(pol,F,X,v,output=('sE','uR','uI','uJ')):
 out={};nonzero=0
 for c,fs in pol.ts:
  pole=-sum(f.power for f in fs if f.name=='pow');arrays=[];labels=[];nextidx=0;idx={};odd=[];skip=False
  for f in fs:
   if f.name=='pow':continue
   t=arr(f,F,X,v)
   if t is None:skip=True;break
   ix=f.ds+f.ix
   ii=[]
   for x in ix:
    if x[1:] not in idx:idx[x[1:]]=nextidx;nextidx+=1
    ii.append(idx[x[1:]])
   if f.name=='L':ii.append(nextidx);odd.append(nextidx);nextidx+=1
   arrays.append(t);labels.append(ii)
  if skip:continue
  nonzero+=1
  args=[]
  for t,ii in zip(arrays,labels):args.extend([t,ii])
  shapeout=[idx[x] for x in output]
  # Optimize each contraction, retaining free indices and the ordered generator axes.
  ten=np.einsum(*args,shapeout+odd,optimize='greedy')
  if odd:
   js,ms,sg=exterior_basis(len(odd))
   vals=ten[(slice(None),)*len(output)+tuple(js[:,z] for z in range(len(odd)))]
   vals=vals*sg
   for free in it.product(*[range(ten.shape[z]) for z in range(len(output))]):
    for mask in set(ms):
     value=vals[free][ms==mask].sum()*complex(c.r,c.i)
     if value:out[free,pole,int(mask)]=out.get((free,pole,int(mask)),0)+value
  else:
   for free in it.product(*[range(d) for d in ten.shape]):
    value=ten[free]*complex(c.r,c.i)
    if value:out[free,pole,0]=out.get((free,pole,0),0)+value
 return {k:v for k,v in out.items() if abs(v)>1e-8},nonzero

def check_case(pol,label,F,X,v):
 raw,nterms=evaluate(pol,F,X,v)
 # Contract epsilon_jr and raise eta to alpha explicitly.
 candidate={}
 for (s,r,i,j),pole,mask in raw:
  for al in range(4):
   k=(al,i,pole,mask);candidate[k]=candidate.get(k,0)+U[al,s]*(-E[j,r])*raw[(s,r,i,j),pole,mask]/3
 candidate={k:v for k,v in candidate.items() if abs(v)>1e-8}
 old=n['raw'](F,X,v);fb=sum(F[c,d]*SD[c,d]/2 for c,d in it.product(range(5),repeat=2));vb=sum(v[c]*GD[c] for c in range(5))
 QQ=np.zeros((8,8),complex)
 for s,r,b,j in it.product(range(4),range(2),range(4),range(2)):QQ[2*s+r,2*b+j]=-2*E[r,j]*fb[s,b]-C[s,b]*X[r,j]-E[r,j]*vb[s,b]
 expected={}
 for al,i,s,r,j in it.product(range(4),range(2),range(4),range(2),range(2)):
  pref=U[al,s]*(-E[j,r]);h=old[tuple(sorted((i,j)))];dh=n['deriv'](2*s+r,h,QQ)
  for (pole,mask),val in dh.items():
   k=(al,i,pole,mask);expected[k]=expected.get(k,0)+pref*val
 # old raw carries denominator 30720; 1/3 adds factor 3.
 for k in set(candidate)|set(expected):
  av=candidate.get(k,0)*92160;bv=expected.get(k,0)
  assert abs(av-bv)<1e-6,(k,av,bv)
 return {'name':label,'status':'PASS','nonzero_candidate_coefficients':len(candidate),'source_comparison_coefficients':len(set(candidate)|set(expected)),'surviving_written_terms':nterms}

if __name__=='__main__':
 inputs=a.make_inputs();pol=sum([a.deriv(p) for p in inputs.values()],a.P())
 for p in inputs.values():
  a.check(p,a.Q(3),{'uI':'+','uJ':'+'})
  for q in [a.deriv(p,True),a.deriv(p),a.normalize(a.deriv(p),True)]:
   a.check(q,a.Q(7,2),{'sE':'-','uR':'+','uI':'+','uJ':'+'})
 F=np.zeros((5,5));F[0,1]=2;F[1,0]=-2;F[2,3]=3;F[3,2]=-3
 X=np.array([[2,3],[3,5]]);v=np.array([1,2,3,4,5])
 cases=[('X_only',F*0,X,v*0),('F_only',F,X*0,v*0),('gradient_only',F*0,X*0,v),('F_X',F,X,v*0),('F_gradient',F,X*0,v),('X_gradient',F*0,X,v),('all',F,X,v)]
 rng=np.random.default_rng(230326)
 for q in range(6):
  ff=rng.integers(-3,4,(5,5));xx=rng.integers(-3,4,(2,2));vv=rng.integers(-3,4,5)
  cases.append((f'integer_probe_{q+1}',ff-ff.T,xx+xx.T,vv))
 report={'date':'2026-09-23','status':'PASS','scope':'All 58 inputs: exact weight, parity, dummy/free-index and written coverage checks; independent original seven-derivative comparison restricted to flat constant F/X/dW and all Grassmann degrees. No full curved S/K/reality or C24 component-basis certificate.','expanded_geometric_summands':len(pol.ts),'cases':[]}
 for label,ff,xx,vv in cases:
  result=check_case(pol,label,ff,xx,vv);report['cases'].append(result);print(label,'PASS',result['nonzero_candidate_coefficients'],flush=True)
 # Independent matrix contraction also checks the index-raising simplification used for typesetting.
 formatted=a.normalize(pol,True)
 test=check_case(formatted,'index-raised printed form',F,X,v);report['formatted_expression_probe']=test
 # Coverage: every derived input and both explicit intermediate formulas appear once.
 doc=(base/'STEP_03_LOG_SPINOR.md').read_text()
 source=json.loads((base/'sources/step2/primary_derived_term_ledger.json').read_text())
 for group in source['groups']:
  for item in group['terms']:
   key=item['id']
   for suffix in ['input','a','b']:assert doc.count('\\tag{S3-'+key+'-'+suffix+'}')==1
   assert item['latex'].removesuffix('.').lstrip('+') in doc
   expanded=a.display(a.deriv(inputs[key]),'S3-'+key+'-b',r'\left.\nabla_\eta^rH^{ij}\right|_{\mathrm{'+key+'}}')
   assert expanded in doc,key
 final=doc.split('<!-- FULL_SPINOR_DERIVED_BEGIN -->')[1].split('<!-- FULL_SPINOR_DERIVED_END -->')[0]
 assert doc.rstrip().endswith('<!-- FULL_SPINOR_DERIVED_END -->')
 for coefficient,fs in formatted.ts:
  numerator=a.P.terms([(coefficient,tuple(f for f in fs if f.name!='pow'))])
  term=a.texterms(numerator,False)[0]
  assert term in final or term.lstrip('+') in final
 report['input_terms']=58;report['unresolved_spinor_derivatives_in_endpoint']=0
 report['parent_primary_sha256']=hashlib.sha256((base/'STEP_02_LOG_PRIMARY.md').read_bytes()).hexdigest()
 report['input_ledger_sha256']=hashlib.sha256((base/'sources/step2/primary_derived_term_ledger.json').read_bytes()).hexdigest()
 report['derivation_sha256']=hashlib.sha256((base/'STEP_03_LOG_SPINOR.md').read_bytes()).hexdigest()
 report['scripts_sha256']={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in [Path(__file__),Path(a.__file__)]}
 (base/'sources/step3/checks.json').write_text(json.dumps(report,indent=2)+'\n')
 print('PASS: 13 independent seventh-derivative probes, printed-form probe, and 58-term coverage')
