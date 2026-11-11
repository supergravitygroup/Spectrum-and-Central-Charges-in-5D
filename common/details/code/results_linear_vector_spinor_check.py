exec(open('__RESULTS_CHECK_WORKDIR__/results_weyl_scalar_q_check.py').read().split('byx={}')[0])
from functools import lru_cache
ell=s.Symbol('Lnorm',positive=True);dN=s.symbols('dN0:5');dE={(a,b):s.Symbol('dE'+str(a)+str(b)) for a,b in product(range(5),repeat=2)}
d2L={}
for a,b in product(range(5),repeat=2):d2L[a,b]=symmat('ddL'+str(a)+str(b)+'_')
# Extend the formal derivative registry for the independent linear multiplet.
for a in range(5):
 jet[a][N]=dN[a]
 for b in range(5):jet[a][E[b]]=dE[a,b]
 for i,j in [(0,0),(0,1),(1,1)]:
  jet[a][L[i,j]]=dL[a][i,j]
  for b in range(5):jet[a][dL[b][i,j]]=d2L[a,b][i,j]
Mvar=ma(mat(one,ga(gs(-I/2,Es),gs(N/2,gamma()))),mat(L*eps,Ts),*(mat(I*dL[a]*eps/2,gamma(a)) for a in range(5)))
Nvar=mat(-3*L*eps,gamma())
def dvar(a,par):
 if par=='eps':return clean(ma(md(Mvar,a),mm(Mvar,mat(-I*one,gm(Ts,gs(h[a],gamma(a))))),ms(-1,mm(Nvar,Qphi[a]))))
 return clean(ma(md(Nvar,a),mm(Mvar,mat(I*one,gs(h[a],gamma(a)))),ms(-1,mm(Nvar,Sphi[a]))))
# Upper composite gaugino, with original order of gamma factors preserved.
lam1=[]
for a in range(5):lam1.append((('dvarphi',a),mat(-2*I*one/ell,gamma(a))))
lam1 += [('varphi',mat(-2*N*L*eps/ell**3,gamma())),('varphi',mat(-2*I*L*eps/ell**3,Es)),('chi',mat(16*L*eps/ell,gamma())),('varphi',mat(4*one/ell,Ts))]
for a in range(5):lam1.append(('varphi',mat(-2*I*dL[a]*eps*L*eps/ell**3,gamma(a))))
# Bosonic target rho1,Y1,F1.
rho1=2*N/ell
Y1d=sum((h[a]*eps.T*d2L[a,a]*eps for a in range(5)),s.zeros(2))/ell-3*Rsc*Ld/(8*ell)
E2=sum(h[a]*E[a]**2 for a in range(5))
Y1d-=Ld*(N**2+E2)/ell**3
for a in range(5):
 dld=eps.T*dL[a]*eps
 Y1d-=h[a]*(dld*L*dld)/ell**3
 # L_(i^k dL_j)k = sym(Ldown eps^T dLdown^T)
 X=Ld*eps.T*dld
 Y1d-=h[a]*E[a]*(X+X.T)/ell**3
T2=sum(h[a]*h[b]*T[a,b]**2 for a,b in product(range(5),repeat=2))
Y1d+=4*Ld*(D+s.Rational(2,3)*T2)/ell
Y1u=eps*Y1d*eps.T
F1={}
for a,b in product(range(5),repeat=2):
 val=2*(dE[a,b]-dE[b,a])/ell
 val-=2*sum(L[i,j]*((eps.T*dL[a]*eps)[i,j]*E[b]-(eps.T*dL[b]*eps)[i,j]*E[a]) for i,j in product(range(2),repeat=2))/ell**3
 val+=2*sum(RV[a,b][i,j]*Ld[i,j] for i,j in product(range(2),repeat=2))/ell
 val-=2*sum((Ld*eps.T)[k,l]*dL[a][k,p]*(eps.T*dL[b]*eps)[l,p] for k,l,p in product(range(2),repeat=3))/ell**3
 F1[a,b]=val
Dnorm=[sum(Ld[i,j]*dL[a][i,j] for i,j in product(range(2),repeat=2))/ell for a in range(5)]
dr1=[2*dN[a]/ell-2*N*Dnorm[a]/ell**2 for a in range(5)]
targetQ=ma(mat(one,ga(*(gs(-F1[a,b]/4,gamma(a,b)) for a,b in product(range(5),repeat=2)),*(gs(-I*dr1[a]/2,gamma(a)) for a in range(5)),gs(rho1,Ts))),mat(Y1u*eps,gamma()))
targetS=mat(rho1*one,gamma())
# Required exact commutator for a weight-three triplet; preserve all symmetric jets.
subL={}
for a,b in product(range(5),repeat=2):
 sy=symmat('symddL'+str(min(a,b))+str(max(a,b))+'_')
 Umat=RV[a,b]*eps;comm=Umat*L+L*Umat.T
 for i,j in [(0,0),(0,1),(1,1)]:subL[d2L[a,b][i,j]]=sy[i,j]+comm[i,j]/2
# E constraint is a symbolic trace projection, not a field background.
trE=sum(h[a]*dE[a,a] for a in range(5))
subE={dE[a,a]:dE[a,a]-h[a]*trE/5 for a in range(5)}
for par,target in [('eps',targetQ),('eta',targetS)]:
 result={}
 for X,M in lam1:
  if X=='varphi':DX=Mvar if par=='eps' else Nvar
  elif X=='chi':DX=Mchi if par=='eps' else Nchi
  else:DX=dvar(X[1],par)
  result=ma(result,mm(M,DX))
 result=clean(ma(result,ms(-1,target)))
 result={k:s.expand((ell**3*v).xreplace(subc).xreplace(subL).xreplace(subE)) for k,v in result.items()}
 result={k:s.rem(v,ell**2-2*(L[0,0]*L[1,1]-L[0,1]**2),ell) for k,v in result.items()}
 res={k:s.factor(v) for k,v in result.items() if s.expand(v)!=0}
 assert not res, (par,res)
 print('Linear-to-vector composite gaugino',par,'residual blocks',len(res),flush=True)
 for k,v in list(res.items())[:10]:print(k,v,flush=True)
