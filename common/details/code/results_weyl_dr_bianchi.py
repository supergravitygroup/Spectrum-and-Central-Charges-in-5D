exec(open('__RESULTS_CHECK_WORKDIR__/results_weyl_scalar_q_check.py').read().split('rawQ={}')[0])
from itertools import combinations,combinations_with_replacement
# Formal Young-symmetry parametrization; H is an auxiliary symbolic tensor,
# not a gauge choice or a numerical assignment to any field.
def hh(a,b,c,d,e):return s.Symbol('H'+''.join(map(str,sorted((a,b))))+'_'+''.join(map(str,sorted((c,d,e)))))
def drr(m,a,b,c,d):return (hh(c,b,a,d,m)+hh(a,d,b,c,m)-hh(b,d,a,c,m)-hh(a,c,b,d,m))/2
subdR={}
for m in range(5):
 for r,P0 in enumerate(pairs):
  for q,Q0 in enumerate(pairs):
   if r<=q:subdR[s.Symbol('d'+str(m)+'_R'+str(r)+'_'+str(q))]=drr(m,*P0,*Q0)
with open('__RESULTS_CHECK_WORKDIR__/results_weyl_spinorQres.pkl','rb') as f0:res=pickle.load(f0)
red={key:s.expand(val.xreplace(subdR)) for key,val in res.items()}
red={key:val for key,val in red.items() if val!=0}
assert not red, red
print('Full Q-spinor residual after differential Bianchi:',len(red),flush=True)
if red:
 for k,v in list(red.items())[:4]:print(k,s.Add.make_args(v)[:5],flush=True)
# Verify that the parametrization covers every tensor obeying the symmetries.
rows=[(m,r,q) for m in range(5) for r in range(10) for q in range(r,10)]
rindex={row:i for i,row in enumerate(rows)}
Hvars=sorted(set().union(*(v.free_symbols for v in subdR.values())),key=str)
hindex={v:i for i,v in enumerate(Hvars)}
entries={}
for row,i in rindex.items():
 m,r,q=row
 for h0,coeff in s.Poly(drr(m,*pairs[r],*pairs[q]),*Hvars).terms():
  j=next((j for j,n0 in enumerate(h0) if n0),None)
  if j is not None:entries[i,j]=coeff
A=s.MutableSparseMatrix(len(rows),len(Hvars),entries)
def component(m,a,b,c,d):
 if a==b or c==d:return {}
 rr0=pairs.index(tuple(sorted((a,b))));qq0=pairs.index(tuple(sorted((c,d))))
 sg=(1 if a<b else -1)*(1 if c<d else -1)
 return {rindex[m,min(rr0,qq0),max(rr0,qq0)]:sg}
def plus(*x):
 d=defaultdict(int)
 for dd in x:
  for k,v in dd.items():d[k]+=v
 return {k:v for k,v in d.items() if v}
constraints=[]
for m in range(5):
 for a,b,c,d in combinations(range(5),4):constraints.append(plus(component(m,a,b,c,d),component(m,a,c,d,b),component(m,a,d,b,c)))
for a,b,c in combinations(range(5),3):
 for d,e in pairs:constraints.append(plus(component(a,b,c,d,e),component(b,c,a,d,e),component(c,a,b,d,e)))
B=s.MutableSparseMatrix(len(constraints),len(rows),{(i,j):v for i,row in enumerate(constraints) for j,v in row.items()})
assert B*A==s.zeros(B.rows,A.cols)
from sympy.polys.matrices import DomainMatrix
rankA=DomainMatrix.from_Matrix(A).convert_to(s.QQ).rank()
rankB=DomainMatrix.from_Matrix(B).convert_to(s.QQ).rank()
print('Exact fixed-index ranks:',rankA,rankB,'ambient coefficient space',len(rows),flush=True)
assert rankA+rankB==len(rows)
print('Young parametrization equals the full Bianchi kernel.',flush=True)
