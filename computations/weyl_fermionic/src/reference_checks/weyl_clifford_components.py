import numpy as np,itertools as it,json,re,time
from pathlib import Path
rg=range(5);eta=np.array([-1,1,1,1,1]);I=np.eye(4);s1=np.array([[0,1],[1,0]]);s2=np.array([[0,-1j],[1j,0]]);s3=np.diag([1,-1]);I2=np.eye(2)
gu=np.array([-1j*np.kron(s3,I2),np.kron(s1,s1),np.kron(s1,s2),np.kron(s1,s3),np.kron(s2,I2)])
gl=eta[:,None,None]*gu;charge=gu[2]@gu[4];su=np.array([[0,1],[-1,0]])
def sign(p):return (-1)**sum(p[a]>p[b] for a in range(len(p)) for b in range(a+1,len(p)))
G={0:I}
for n in range(1,6):
 a=np.zeros((5,)*n+(4,4),complex)
 for ix in it.combinations(rg,n):
  mat=I
  for i in ix:mat=mat@gl[i]
  for p in it.permutations(range(n)):a[tuple(ix[k] for k in p)]=sign(p)*mat
 G[n]=a
E=np.zeros((5,)*5)
for p in it.permutations(rg):E[p]=-sign(p)
pairs=list(it.combinations(rg,2))
cb=np.zeros((100,5,5,5,5))
for n,((a,b),(c,d)) in enumerate(it.product(pairs,pairs)):
 for i,j,s in [(a,b,1),(b,a,-1)]:
  for k,l,t in [(c,d,1),(d,c,-1)]:cb[n,i,j,k,l]=s*t
trace=np.einsum('nabcb,b->nac',cb,eta).reshape(100,25).T
proj=np.eye(100)-np.linalg.pinv(trace)@trace

def gen(seed):
 rng=np.random.default_rng(seed);rand=lambda shape:rng.integers(-3,4,size=shape).astype(complex)
 anti=lambda a:a-np.swapaxes(a,-1,-2)
 fields={'T':anti(rand((5,5))),'Td1':anti(rand((5,5,5))),'Td2':anti(rand((5,5,5,5))),'D':rand(()),'Dd1':rand((5,)),'V':anti(rand((5,5))),'E':E}
 fields['D2']=fields['D']**2;fields['m']=np.diag(eta)
 fields['C']=np.einsum('n,nabcd->abcd',proj@rand((100,)),cb)
 fields['Cd1']=np.einsum('xn,nabcd->xabcd',rand((5,100))@proj,cb)
 ferm={}
 for name,d in [('R',0),('R',1),('X',0),('X',1)]:
  shape=(2,)+(5,)*d+((5,5) if name=='R' else ())+ (2,4)
  q=rand(shape)
  if name=='R':
   # Each odd mode, derivative jet and SU(2) component is projected separately.
   q=np.swapaxes(q,-1,-3) if False else q
   q=q-np.swapaxes(q,-4,-3)
   for pre in it.product(*[range(n) for n in q.shape[:-4]]):
    for u in range(2):
     raw=q[pre+(slice(None),slice(None),u,slice(None))].copy()
     ph=np.zeros((5,4),complex)
     for a in rg:
      ph[a]=sum(1j/3*gu[b]@raw[a,b] for b in rg)-sum(1j/24*gl[a]@(eta[b]*eta[c]*G[2][b,c])@raw[b,c] for b,c in it.product(rg,repeat=2))
     r=np.array([[raw[a,b]-1j*gl[a]@ph[b]+1j*gl[b]@ph[a] for b in rg] for a in rg])
     assert np.max(np.abs(sum(np.einsum('uv,bv->bu',gu[a],r[a]) for a in rg)))<1e-11
     q[pre+(slice(None),slice(None),u,slice(None))]=r
  ferm[(name,d)]=q
 return fields,ferm

def valcoef(s):return complex(eval(s,{'__builtins__':{}},{'I':1j}))
def evaluate(term,fields,ferm):
 c,f,go,gi,fr=term;args=[];labs={};counts={};nextlab=0
 def label(x):
  nonlocal nextlab
  if x not in labs:labs[x]=nextlab;nextlab+=1
  counts[x]=counts.get(x,0)+1
  return labs[x]
 def fresh():
  nonlocal nextlab
  n=nextlab;nextlab+=1;return n
 # all fields/gamma matrices carry lower Lorentz slots; eta at each contraction.
 for n,ix in f:args.extend([fields[n],[label(x) for x in ix]])
 o1,o2=fresh(),fresh()
 def word(chain,left,right):
  if not chain:args.extend([I,[left,right]]);return
  prev=left
  for k,ix in enumerate(chain):
   end=right if k==len(chain)-1 else fresh();args.extend([G[len(ix)],[label(x) for x in ix]+[prev,end]]);prev=end
 word(go,o1,o2)
 if fr:
  (n,d,ix),(m,e,jx)=fr;fl,fc,fmid,fright,sul,sur=[fresh() for _ in range(6)]
  args.extend([charge,[fl,fc],su,[sul,sur]])
  word(gi,fc,fmid)
  leftix=[label(x) for x in ix]+[sul,fl];rightix=[label(x) for x in jx]+[sur,fmid]
  ia=len(args);args.extend([None,leftix,None,rightix])
 else:assert not gi
 for x,l in labs.items():
  assert counts[x]==2,(x,counts,term)
  args.extend([eta,[l]])
 if fr:
  ans=0
  for u,v,sgn in [(0,1,1),(1,0,-1)]:
   args[ia]=ferm[(n,d)][u];args[ia+2]=ferm[(m,e)][v]
   ans=ans+sgn*np.einsum(*args,[o1,o2],optimize='greedy')
 else:ans=np.einsum(*args,[o1,o2],optimize='greedy')
 return valcoef(c)*ans

def canonical_to_term(row):
 f=[];go=[];gi=[];fr=[]
 for n,ix in row['factors']:
  if n.startswith('G'):go=[ix]
  elif n.startswith('B'):
   na,da,nb,db,gr=re.fullmatch(r'B([RX])(\d)([RX])(\d)g(\d)',n).groups();da,db,gr=map(int,[da,db,gr]);left=da+(2 if na=='R' else 0)
   fr=[(na,da,ix[:left]),(nb,db,ix[left+gr:])];gi=[ix[left:left+gr]] if gr else []
  else:f.append((n,ix))
 return [row['coefficient'],f,go,gi,fr]
if __name__=='__main__':
 import sys
 j=json.loads(Path(sys.argv[1]).read_text());report={};out=[]
 # A complete finite Clifford basis includes ranks 0,...,5 before duality.
 for row in j['basis_products']:
  a=tuple(row['left']);b=tuple(row['right']);lhs=G[len(a)][a]@G[len(b)][b];rhs=np.zeros((4,4),complex)
  for c,blade,metrics in row['terms']:
   factor=valcoef(c)
   for u,v in metrics:factor*=eta[u] if u==v else 0
   rhs+=factor*G[len(blade)][tuple(blade)]
  assert np.max(np.abs(lhs-rhs))==0
 report['Clifford_basis_products']={'status':'PASS','cases':len(j['basis_products']),'max_error':0}
 assert np.max(np.abs(gu[0]@gu[1]@gu[2]@gu[3]@gu[4]-1j*I))==0
 for n,fac in [(3,-.5j),(4,1j),(5,1j)]:
  for ix in it.combinations(rg,n):
   rhs=np.zeros((4,4),complex)
   for rest in it.product(rg,repeat=5-n):
    rhs+=fac*E[ix+rest]*np.prod([eta[a] for a in rest])*G[5-n][rest]
   assert np.max(np.abs(G[n][ix]-rhs))==0
 report['duality_and_orientation']={'status':'PASS','all_upper_gamma_01234':'i','volume_lower_01234':-1}
 # Repeated random component checks test all original 586 entries against all85 final terms.
 for seed in [42,53,67,79,83,97,101,109,113,127]:
  fields,ferm=gen(seed)
  orig=sum(evaluate(r,fields,ferm) for r in j['original'])
  red=sum(evaluate(canonical_to_term(r),fields,ferm) for r in j['reduced'])
  err=float(np.max(np.abs(orig-red)));scale=float(max(np.max(np.abs(orig)),1))
  out.append({'seed':seed,'absolute_error':err,'relative_error':err/scale});assert err/scale<1e-11
 report['full_original_to_collected']={'status':'PASS','two_Grassmann_generators':True,'samples':out}
 # Check every displayed middle line and endpoint, not only a sum that might hide errors.
 fields,ferm=gen(42);errs=[]
 for r in j['rows']:
  lhs=sum(evaluate(x,fields,ferm) for x in r['projected_input'])
  mid=sum(evaluate(canonical_to_term(x),fields,ferm) for x in r['gamma_products_expanded'])
  end=sum(evaluate(canonical_to_term(x),fields,ferm) for x in r['terms'])
  scale=float(max(np.max(np.abs(lhs)),np.max(np.abs(mid)),np.max(np.abs(end)),1))
  err=float(max(np.max(np.abs(lhs-mid)),np.max(np.abs(lhs-end))))/scale
  errs.append(err);assert err<1e-10,(r['equation'],err)
 report['displayed_intermediate_reductions']={'status':'PASS','equations':len(errs),'maximum_relative_error':max(errs)}
 # Algebraic restrictions of the polynomial; these are not asserted to be backgrounds.
 lim=[]
 fields,ferm=gen(42)
 for kept in [[],['D','D2'],['C'],['V'],['T']]:
  fs={n:(v if n in kept or n in ['m','E'] else np.zeros_like(v)) for n,v in fields.items()}
  fr={n:np.zeros_like(v) for n,v in ferm.items()}
  lhs=sum(evaluate(x,fs,fr) for x in j['original']);rhs=sum(evaluate(canonical_to_term(x),fs,fr) for x in j['reduced'])
  err=float(np.max(np.abs(lhs-rhs)));scale=float(max(np.max(np.abs(lhs)),1));assert err/scale<1e-11
  lim.append({'retained':kept,'relative_error':err/scale})
 report['zero_and_single_sector_limits']={'status':'PASS','cases':lim}
 serr=[]
 for seed in range(10):
  f,fr=gen(seed);T=f['T'];U=f['Td1']
  A=np.einsum('abcde,ab,cf,fde,a,b,c,d,e,f',E,T,T,U,eta,eta,eta,eta,eta,eta)
  B=np.einsum('abcde,ab,cf,def,a,b,c,d,e,f',E,T,T,U,eta,eta,eta,eta,eta,eta)
  C=np.einsum('abcde,ab,cd,fef,a,b,c,d,e,f',E,T,T,U,eta,eta,eta,eta,eta,eta)
  Q=np.einsum('acdef,cd,ef,gh,gh,c,d,e,f,g,h',E,T,T,T,T,eta,eta,eta,eta,eta,eta)
  W=np.einsum('acdef,cd,eg,fh,gh,c,d,e,f,g,h',E,T,T,T,T,eta,eta,eta,eta,eta,eta)
  err=float(max(abs(A+C/2),abs(B-C/4),np.max(np.abs(W-Q/4))));assert err==0;serr.append(err)
 report['Schouten_component_crosschecks']={'status':'PASS','tensor_samples':10,'identities_per_sample':3,'maximum_error':max(serr),'proof':'notebook G14-G20, six-index antisymmetrization'}
 Path(sys.argv[2]).write_text(json.dumps(report,indent=2)+'\n');print('Independent matrix, component and Grassmann checks: PASS')
