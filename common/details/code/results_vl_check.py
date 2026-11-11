import sympy as s
from collections import defaultdict
from itertools import product
I=s.I; h=(-1,1,1,1,1); n=5; eps=s.Matrix([[0,1],[-1,0]]); one=s.eye(2)
def symmat(prefix):
 a,b,c=s.symbols(prefix+'11 '+prefix+'12 '+prefix+'22');return s.Matrix([[a,b],[b,c]])
L=symmat('L');Ld=eps.T*L*eps;Y=symmat('Y');Yd=eps.T*Y*eps
rho,N=s.symbols('rho N');E=s.symbols('E0:5');dr=s.symbols('dr0:5');dL=[symmat('dL'+str(a)+'_') for a in range(5)]
T={};F={}
for a in range(5):
 for b in range(5):
  for dic,lab in [(T,'T'),(F,'F')]:
   dic[a,b]=0 if a==b else (1 if a<b else -1)*s.Symbol(lab+str(min(a,b))+str(max(a,b)))
# Spinor matrix is {(SU2 output,SU2 input, gamma tuple):scalar}
def blade(a,b):
 x=list(a);sgn=1
 for j in b:
  sgn*=(-1)**sum(k>j for k in x)
  if j in x:sgn*=h[j];x.remove(j)
  else:x.append(j);x.sort()
 return tuple(x),sgn
def gamma(*a):
 if len(set(a))!=len(a):return {}
 return {tuple(sorted(a)):(-1)**sum(a[i]>a[j] for i in range(len(a)) for j in range(i+1,len(a)))}
def gm(A,B):
 d=defaultdict(lambda:s.S.Zero)
 for a,x in A.items():
  for b,y in B.items():
   c,sgn=blade(a,b);d[c]+=x*y*sgn
 return dict(d)
def gs(c,A):return {k:c*v for k,v in A.items()}
def ga(*A):
 d=defaultdict(lambda:s.S.Zero)
 for M in A:
  for k,v in M.items():d[k]+=v
 return dict(d)
def tau(a):return (-1)**(len(a)*(len(a)-1)//2)
def mat(C,G):return {(i,j,g):C[i,j]*v for i,j in product(range(2),repeat=2) for g,v in G.items() if C[i,j]*v!=0}
def ma(*A):
 d=defaultdict(lambda:s.S.Zero)
 for M in A:
  for k,v in M.items():d[k]+=v
 return dict(d)
Ts=ga(*(gs(T[a,b],gamma(a,b)) for a,b in product(range(5),repeat=2)))
Fs=ga(*(gs(F[a,b],gamma(a,b)) for a,b in product(range(5),repeat=2)))
rs=ga(*(gs(dr[a],gamma(a)) for a in range(5)))
Es=ga(*(gs(E[a],gamma(a)) for a in range(5)))
# Every spinor species has independent two SU(2) components.
def delta(X):
 if X=='lambda':
  return [('eps',ma(mat(one,ga(gs(-s.Rational(1,4),Fs),gs(-I/2,rs),gs(rho,Ts))),mat(Y*eps,gamma()))),('eta',mat(rho*one,gamma()))]
 if X=='varphi':
  return [('eps',ma(mat(one,ga(gs(-I/2,Es),gs(N/2,gamma()))),mat(L*eps,Ts),*(mat(I*dL[a]*eps/2,gamma(a)) for a in range(5)))),('eta',mat(-3*L*eps,gamma()))]
 if isinstance(X,tuple) and X[0]=='psi':
  a=X[1];return [(('deps',a),mat(one,gamma())),('eps',mat(I*one,gm(Ts,gs(h[a],gamma(a))))),('eta',mat(-I*one,gs(h[a],gamma(a))))]
 raise KeyError(X)
out=defaultdict(lambda:s.S.Zero)
def term(par,ferm,C,G,factor=1):
 for i,j in product(range(2),repeat=2):
  for g,v in G.items():
   if C[i,j]*v!=0:out[par,ferm,i,j,g]+=factor*C[i,j]*v

def vary_bilinear(X,Z,C,G,factor=1):
 for par,M in delta(X):
  for (i,k,m),u in M.items():
   for j in range(2):
    for g,v in G.items():
     b,sgn=blade(m,g)
     out[par,Z,k,j,b]+=factor*C[i,j]*u*v*tau(m)*sgn
 for par,M in delta(Z):
  for (j,k,m),u in M.items():
   for i in range(2):
    for g,v in G.items():
     b,sgn=blade(g,m)
     out[par,X,k,i,b]+=factor*C[i,j]*u*v*tau(b)*sgn

def Dferm(X,a):
 # Returns species, spinor matrix for D_a X.
 if X=='lambda':
  return [(('dlambda',a),mat(one,gamma())),(('psi',a),ma(mat(one,ga(gs(s.Rational(1,4),Fs),gs(I/2,rs),gs(-rho,Ts))),mat(-Y*eps,gamma()))),(('phiS',a),mat(-rho*one,gamma()))]
 if X=='varphi':
  return [(('dvarphi',a),mat(one,gamma())),(('psi',a),ma(mat(one,ga(gs(I/2,Es),gs(-N/2,gamma()))),mat(-L*eps,Ts),*(mat(-I*dL[b]*eps/2,gamma(b)) for b in range(5)))),(('phiS',a),mat(3*L*eps,gamma()))]

def termD(par,X,a,C,G,factor=1):
 for Z,M in Dferm(X,a):
  for (j,k,m),u in M.items():
   for i in range(2):
    for g,v in G.items():
     b,sgn=blade(g,m);out[par,Z,i,k,b]+=factor*C[i,j]*u*v*sgn

# Variation of e(YL+rho N) and explicit fermions, without A P.
YL=sum(Y[i,j]*Ld[i,j] for i,j in product(range(2),repeat=2))
for a in range(5):
 term('eps',('psi',a),-eps,gamma(a),(YL+rho*N)/2)
 termD('eps','lambda',a,Ld,gamma(a),-s.Rational(1,2))
 termD('eps','varphi',a,-eps,gamma(a),rho/2)
term('eps','lambda',Ld,Ts,I/2)
term('eps','chi',Ld,gamma(),-4*I*rho)
term('eta','lambda',Ld,gamma(),I/2)
term('eps','varphi',Yd,gamma(),I)
term('eps','lambda',-eps,gamma(),I*N/2)
term('eps','varphi',-eps,Ts,3*I*rho/2)
term('eps','chi',Ld,gamma(),4*I*rho)
term('eta','varphi',-eps,gamma(),3*I*rho/2)
vary_bilinear('lambda','varphi',-eps,gamma(),I)
for a in range(5):
 vary_bilinear(('psi',a),'lambda',Ld,gamma(a),-s.Rational(1,2))
 vary_bilinear(('psi',a),'varphi',-eps,gamma(a),rho/2)
 for b in range(5):
  vary_bilinear(('psi',a),('psi',b),Ld,gamma(a,b),I*rho/4)
# AP variation after exact curl identity delta(e P^mu)=partial_nu(e Q^mu nu):
# delta A_a E^a and -F_ab Q^ab/2, modulo div(A Q).
for a in range(5):
 term('eps',('psi',a),-eps,gamma(),-I*rho*h[a]*E[a]/2)
 term('eps','lambda',-eps,gamma(a),E[a]/2)
 for b in range(5):
  term('eps','varphi',-eps,gamma(a,b),-I*F[a,b]/4)
  for c in range(5):
   term('eps',('psi',c),Ld,gamma(a,b,c),F[a,b]/4)
# Subtract divergence K^a = -1/2 L_ij bareps^i gamma^a lambda^j
#                       +rho/2 bareps gamma^a varphi.
for a in range(5):
 term(('deps',a),'lambda',Ld,gamma(a),s.Rational(1,2))
 term('eps',('dlambda',a),Ld,gamma(a),s.Rational(1,2))
 term('eps','lambda',eps.T*dL[a]*eps,gamma(a),s.Rational(1,2))
 term(('deps',a),'varphi',-eps,gamma(a),-rho/2)
 term('eps',('dvarphi',a),-eps,gamma(a),-rho/2)
 term('eps','varphi',-eps,gamma(a),-dr[a]/2)
# Remaining density current generated by varying the psi psi term.
# Kpsi^a=i rho L_ij bareps^i gamma^{ab} psi_b^j /2.
for a in range(5):
 for b in range(5):
  term(('deps',a),('psi',b),Ld,gamma(a,b),-I*rho/2)
  term('eps',('psi',b),Ld,gamma(a,b),-I*dr[a]/2)
  term('eps',('psi',b),eps.T*dL[a]*eps,gamma(a,b),-I*rho/2)
  # gamma^{ab} D_a psi_b=-4i gamma^a phi_a-i gamma^{ab} Tslash gamma_a psi_b.
  term('eps',('psi',b),Ld,gm(gamma(a,b),gm(Ts,gs(h[a],gamma(a)))),-rho/2)
 term('eps',('phiS',a),Ld,gamma(a),-2*rho)
res={k:s.expand(v) for k,v in out.items() if s.expand(v)!=0}
print('VL residual nonzero blocks:',len(res))
for k,v in list(res.items())[:35]:print(k,':',s.factor(v))

assert not res, res
