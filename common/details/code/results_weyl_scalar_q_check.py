# Exact bosonic scalar descendant derived from the full linear spinor variation.
exec(open('__RESULTS_CHECK_WORKDIR__/results_weyl_spinor_s_check.py').read().split('result={}')[0])
exec('pairs=[(a,b)'+open('__RESULTS_CHECK_WORKDIR__/results_weyl_spinor_s_check.py').read().split('pairs=[(a,b)')[1].split('res={')[0])
from functools import lru_cache
import pickle
# R_abcd includes all 55 input components and algebraic Bianchi projection.
rawQ={}
for a,b in product(range(5),repeat=2):
 G=ga(*(gs(rr(a,b,c,d)/4,gamma(c,d)) for c,d in product(range(5),repeat=2)),gs(I*h[b],gm(DT[a],gamma(b))),gs(-I*h[a],gm(DT[b],gamma(a))),gs(-h[a]*h[b],gm(Ts,gm(gamma(a),gm(Ts,gamma(b))))),gs(h[a]*h[b],gm(Ts,gm(gamma(b),gm(Ts,gamma(a))))))
 rawQ[a,b]=ma(mat(one,G),mat(RV[a,b]*eps,gamma()))
trQ={}
for a,b in product(range(5),repeat=2):trQ=ma(trQ,mm(mat(one,gamma(a,b)),rawQ[a,b]))
Qphi=[]
for a in range(5):
 X={}
 for b in range(5):X=ma(X,ms(I/3,mm(mat(one,gamma(b)),rawQ[a,b])))
 X=ma(X,ms(-I*h[a]/24,mm(mat(one,gamma(a)),trQ)))
 Qphi.append(clean(X))
@lru_cache(None)
def QDferm(X):
 if X=='chi':return Mchi
 if isinstance(X,tuple):
  if X[0]=='q':return MQ[X[1],X[2]]
  if X[0]=='dchi':
   a=X[1];return clean(ma(md(Mchi,a),mm(Mchi,mat(-I*one,gm(Ts,gs(h[a],gamma(a))))),ms(-1,mm(Nchi,Qphi[a]))))
  if X[0]=='dq':
   a,b,c=X[1:];return clean(ma(md(MQ[b,c],a),mm(MQ[b,c],mat(-I*one,gm(Ts,gs(h[a],gamma(a))))),ms(-1,mm(NQ[b,c],Qphi[a]))))
 raise KeyError(X)
byx={}
for X,M in wphi():byx[X]=ma(byx.get(X,{}),M)
byx={X:clean(M) for X,M in byx.items() if clean(M)}
# Scalar trace in Clifford and SU(2); no physical field restriction is imposed.
orientation=s.Symbol('epsilon01234')
Ncalc=s.S.Zero
fullcalc={}
for ix,(X,M) in enumerate(byx.items()):
 A=mm(M,QDferm(X))
 fullcalc=ma(fullcalc,A)
 Ncalc+=sum(A.get((i,i,()),0)+I*orientation*A.get((i,i,(0,1,2,3,4)),0) for i in range(2))
fullcalc=clean(fullcalc)
with open('__RESULTS_CHECK_WORKDIR__/results_weyl_spinor_Qfull.pkl','wb') as f0:pickle.dump(fullcalc,f0)
Ncalc=s.expand(Ncalc)
with open('__RESULTS_CHECK_WORKDIR__/results_weyl_Ncalc.pkl','wb') as f:pickle.dump(Ncalc,f)
print('Derived scalar descendant monomials:',len(s.Add.make_args(Ncalc)),flush=True)
# Exact full conformal D_b D_c T_de at zero physical fermion order.
f={(a,b):-Ric[a,b]/6+met(a,b)*Rsc/48 for a,b in product(range(5),repeat=2)}
def kDT(m,c,d,e):
 # coefficient of Lambda^m in delta_K D_c T_de, from delta b and delta omega.
 return -2*met(m,c)*T[d,e]-2*met(c,d)*T[e,m]+2*met(m,d)*T[e,c]+2*met(c,e)*T[d,m]-2*met(m,e)*T[d,c]
def d2T(b,c,d,e):
 return ddt[b,c,d,e]-sum(h[m]*f[b,m]*kDT(m,c,d,e) for m in range(5))
def alt(indices):
 if len(set(indices))<len(indices):return 0
 return (-1)**sum(indices[i]>indices[j] for i in range(len(indices)) for j in range(i+1,len(indices)))
T2=sum(h[a]*h[b]*T[a,b]**2 for a,b in product(range(5),repeat=2))
Nexpected=s.Rational(64,3)*D**2+s.Rational(1024,9)*T2*D-s.Rational(2816,27)*T2**2
Nexpected+=sum(h[a]*h[b]*h[c]*h[d]*C[a,b,c,d]**2/8 for a,b,c,d in product(range(5),repeat=4))
Nexpected-=sum(s.Rational(16,3)*h[a]*h[b]*h[c]*h[d]*C[a,b,c,d]*T[a,b]*T[c,d] for a,b,c,d in product(range(5),repeat=4))
Nexpected-=sum(h[a]*h[b]*(RV[a,b].multiply_elementwise(eps.T*RV[a,b]*eps)).sum() if False else s.Rational(1,3)*h[a]*h[b]*sum(RV[a,b][i,j]*(eps.T*RV[a,b]*eps)[i,j] for i,j in product(range(2),repeat=2)) for a,b in product(range(5),repeat=2))
Nexpected+=sum(-s.Rational(64,3)*h[a]*h[b]*h[c]*dt[a,b,c]**2+s.Rational(64,3)*h[a]*h[b]*h[c]*dt[b,a,c]*dt[a,b,c]-s.Rational(128,3)*h[a]*h[b]*h[c]*T[a,b]*d2T(b,c,a,c) for a,b,c in product(range(5),repeat=3))
Nexpected+=sum(1024*h[a]*h[b]*h[c]*h[d]*T[a,b]*T[b,c]*T[c,d]*T[d,a] for a,b,c,d in product(range(5),repeat=4))
Nexpected+=sum(s.Rational(128,3)*orientation*alt((a,b,c,d,e))*h[a]*h[b]*h[c]*h[d]*h[e]*h[f0]*T[a,b]*T[c,d]*dt[f0,e,f0] for a,b,c,d,e,f0 in product(range(5),repeat=6) if alt((a,b,c,d,e)))
res=s.expand(Ncalc-Nexpected)
print('Scalar residual before curvature and derivative reductions:',len(s.Add.make_args(res)),flush=True)
# Ordered second derivatives: preserve the symmetric part, replace only the
# antisymmetric commutator by its defining curvature action.
ddsub={}
for a in range(5):
 for b in range(5):
  for c,d in pairs:
   symmetric=s.Symbol('sddT'+str(min(a,b))+str(max(a,b))+'_'+str(c)+str(d))
   comm=sum(h[e]*(rr(a,b,c,e)*T[e,d]+rr(a,b,d,e)*T[c,e]) for e in range(5))
   ddsub[ddt[a,b,c,d]]=symmetric+comm/2
res=s.expand(res.xreplace(subc).xreplace(ddsub))
with open('__RESULTS_CHECK_WORKDIR__/results_weyl_Nres.pkl','wb') as f:pickle.dump(res,f)
print('Scalar residual after exact identities monomial count:',len(s.Add.make_args(res)) if res!=0 else 0,flush=True)
if res!=0:
 print('Representative coefficient terms (not field samples):',s.Add.make_args(res)[:12],flush=True)

assert res==0, res
