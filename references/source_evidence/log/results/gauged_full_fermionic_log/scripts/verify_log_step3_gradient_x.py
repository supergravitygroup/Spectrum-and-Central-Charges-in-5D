import sys,runpy,time,json,hashlib
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parent))
import verify_log_step3_spinor as v
import log_step3_covariant_rules as a
import numpy as np,itertools as it
from collections import defaultdict
B=Path(__file__).resolve().parents[1]
t=time.time();ns=runpy.run_path(str(B/'scripts/verify_log_step2_w3_flat_gradient_x.py'))
# H++ = -2 derivative relation: varphi_alpha^+ = -D_alpha^- H++/2.
actual=defaultdict(complex)
for s in range(4):
 for word,z in ns['words'].items():
  if not z:continue
  for (pole,ev,mask),c in ns['DP'](2*s+1,ns['word_eval'](word)).items():
   if pole==4 and len(ev)==1 and ev[0][0]=='dx':actual[s,ev[0],mask]+=-3j*z*c
print('Raw seventh-derivative gradient sector ready',round(time.time()-t,1),flush=True)
original=v.arr
DX=np.zeros((5,2,2))
def arr(f,F,X,grad):
 if f.name=='X' and len(f.ds)==1:
  tensor=DX.copy()
  if f.ds[0][0]=='+':tensor=tensor*v.eta[:,None,None]
  for axis,x in enumerate(f.ix,1):
   if x[0]=='-':tensor=np.moveaxis(np.tensordot(-v.E,tensor,axes=(1,axis)),0,axis)
  return tensor
 return original(f,F,X,grad)
v.arr=arr
inputs=a.make_inputs();pol=sum([a.deriv(p) for p in inputs.values()],a.P())
# Restrict only after complete descent; tensors with other bosonic data vanish.
F=np.zeros((5,5));X=np.zeros((2,2));grad=np.zeros(5)
checks=[]
for plane in [(n,i,j) for n in range(5) for i,j in [(0,0),(0,1),(1,1)]]:
 DX[:]=0;nn,i,j=plane;DX[nn,i,j]=DX[nn,j,i]=1
 raw,_=v.evaluate(pol,F,X,grad)
 # direct defining trace, lower free spinor, SU2 +
 candidate=defaultdict(complex)
 for (s,r,ii,jj),pole,mask in raw:
  if ii==0 and pole==4:candidate[s,mask]+=(-v.E[jj,r])*raw[(s,r,ii,jj),pole,mask]/3
 keys={(s,mask) for s,ev,mask in actual if ev==('dx',nn,i,j)}|set(candidate)
 for s,mask in keys:
  lhs=candidate[s,mask]*61440;rhs=actual[s,('dx',nn,i,j),mask]
  assert abs(lhs-rhs)<1e-6,(plane,s,mask,lhs,rhs)
 checks.append({'gradient_component':list(plane),'coefficients':len(keys),'status':'PASS'})
 print('PASS gradient',plane,len(keys),flush=True)
report={'date':'2026-09-23','status':'PASS','scope':'Independent original seven-spinor definition versus the new direct trace; all 15 first gradients of the auxiliary triplet, coefficient linear in gradient X and cubic in gauginos at W^-4. Flat Weyl geometry; F/X/dW and other independent jets zero at the comparison point. No full curved Ward identity.','comparison_denominator':61440,'checks':checks,'scripts_sha256':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in [Path(__file__),Path(v.__file__),Path(a.__file__),B/'scripts/verify_log_step2_w3_flat_gradient_x.py']}}
(B/'sources/step3/gradient_x_checks.json').write_text(json.dumps(report,indent=2)+'\n')
print('PASS all 15 gradient-X components; elapsed',round(time.time()-t,1),'seconds')
