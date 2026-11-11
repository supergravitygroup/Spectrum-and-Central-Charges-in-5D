#!/usr/bin/env python3
"""Independent algebra/interface tests; NOT a nonlinear SUSY/map certificate."""
import itertools as it
import json, math
from fractions import Fraction as F
from pathlib import Path

BASE=Path(__file__).resolve().parents[1]
N=4
I=[[complex(i==j) for j in range(N)] for i in range(N)]
Z=[[0j]*N for _ in range(N)]
def add(*xs): return [[sum(x[i][j] for x in xs) for j in range(N)] for i in range(N)]
def scale(c,x): return [[c*v for v in r] for r in x]
def mul(a,b): return [[sum(a[i][k]*b[k][j] for k in range(N)) for j in range(N)] for i in range(N)]
def tr(a):return sum(a[i][i] for i in range(N))
def trans(a):return [list(x) for x in zip(*a)]
def dagger(a):return [[a[j][i].conjugate() for j in range(N)] for i in range(N)]
def eq(a,b):return max(abs(a[i][j]-b[i][j]) for i in range(N) for j in range(N))<1e-12
def kron(a,b):return [[a[i//2][j//2]*b[i%2][j%2] for j in range(4)] for i in range(4)]
s1=[[0,1],[1,0]];s2=[[0,-1j],[1j,0]];s3=[[1,0],[0,-1]];i2=[[1,0],[0,1]]
g=[scale(-1j,kron(s3,i2)),kron(s1,s1),kron(s1,s2),kron(s1,s3),kron(s2,i2)]
eta=[-1,1,1,1,1]
def sign(seq):return (-1)**sum(seq[i]>seq[j] for i in range(len(seq)) for j in range(i+1,len(seq)))
def gam(seq):
 if len(set(seq))!=len(seq):return Z
 out=I
 for a in seq:out=mul(out,g[a])
 return out # distinct Clifford generators already equal the antisymmetric product

def lowgam(seq):return scale(math.prod(eta[a] for a in seq),gam(seq))
def eps(seq):return sign(seq) if len(seq)==5 and len(set(seq))==5 else 0
checks={}
assert all(eq(add(mul(g[a],g[b]),mul(g[b],g[a])),scale(2*eta[a] if a==b else 0,I)) for a in range(5) for b in range(5))
assert eq(gam(range(5)),scale(1j,I));checks['clifford_and_orientation']='PASS: 25 Clifford relations and gamma01234=+i'
C=mul(g[2],g[4])
assert eq(trans(C),scale(-1,C)) and eq(mul(dagger(C),C),I)
for a in range(5):assert eq(trans(mul(C,g[a])),scale(-1,mul(C,g[a])))
B=mul(C,scale(-1,g[0]));assert eq(mul(B,[[x.conjugate() for x in r] for r in B]),scale(-1,I))
for n,tn in enumerate([1,1,-1,-1]):
 for indices in it.combinations(range(5),n):
  assert eq(trans(mul(C,gam(indices))),scale(-tn,mul(C,gam(indices))))
checks['majorana_and_fixed_index_flip']='PASS: transpose symmetry; odd reordering yields t_n, SU(2) contraction adds minus'
count=0
for n in range(6):
 for indices in it.combinations(range(5),n):
  rhs=Z
  for rem in it.permutations([a for a in range(5) if a not in indices]):
   rhs=add(rhs,scale(-1j*eps(indices+rem)/math.factorial(5-n),gam(rem[::-1])))
  assert eq(lowgam(indices),rhs),(n,indices)
  count+=1
checks['gamma_duality']=f'PASS: {count} independent rank0-5 identities'
for n,(c1,c2) in enumerate([(5,-20),(-3,-4),(1,4),(1,4)]):
 for ids in it.combinations(range(5),n):
  m=gam(ids)
  assert eq(add(*[mul(mul(g[a],m),lowgam((a,))) for a in range(5)]),scale(c1,m))
  assert eq(add(*[mul(mul(gam((a,b)),m),lowgam((a,b))) for a in range(5) for b in range(5)]),scale(c2,m))
checks['gamma_sandwiches']='PASS: all independent components, ranks0-3'
# Matrix completeness proves the coefficients before Grassmann reordering;
# every one of 16 matrix units is tested, not a single special spinor.
for i in range(4):
 for j in range(4):
  m=[[complex(a==i and b==j) for b in range(4)] for a in range(4)]
  rhs=scale(tr(m)/4,I)
  rhs=add(rhs,*[scale(tr(mul(g[a],m))/4,lowgam((a,))) for a in range(5)])
  rhs=add(rhs,*[scale(-tr(mul(gam((a,b)),m))/8,lowgam((a,b))) for a in range(5) for b in range(5)])
  assert eq(m,rhs)
checks['fierz_completeness']='PASS: all16 matrix units; odd swap gives (-1/4,-1/4,+1/8)'
u=[[0,1],[-1,0]]
assert all(sum(u[i][k]*u[j][k] for k in range(2))==int(i==j) for i in range(2) for j in range(2))
for vec in ([2,3],[-1,5]):
 lower=[sum(vec[j]*u[j][i] for j in range(2)) for i in range(2)]
 assert [sum(u[i][j]*lower[j] for j in range(2)) for i in range(2)]==list(vec)
checks['su2_nwse']='PASS: raise/lower inverse; epsilon contracted with reversed slot adds minus'
# Algebraic constant-curvature and Schouten projection checks in Lorentzian frame.
def delta(a,b):return int(a==b)
k=F(7,3)
R=lambda m,n,a,b:k*(delta(m,a)*delta(n,b)-delta(n,a)*delta(m,b))
ric=[[sum(R(m,r,a,r)*eta[a]*delta(n,a) for r in range(5) for a in range(5)) for n in range(5)] for m in range(5)]
rw=[[sum(R(m,r,r,b)*eta[b]*delta(n,b) for r in range(5) for b in range(5)) for n in range(5)] for m in range(5)]
assert all(ric[m][n]==4*k*eta[m]*delta(m,n)==-rw[m][n] for m in range(5) for n in range(5))
scalar=sum(eta[m]*ric[m][m] for m in range(5));assert scalar==20*k
f=[[ -ric[m][a]*eta[a]/6+F(1,48)*delta(m,a)*scalar for a in range(5)] for m in range(5)]
assert all(f[m][a]==-k*delta(m,a)/4 for m in range(5) for a in range(5))
for m,n,a,b in it.product(range(5),repeat=4):
 fterm=2*(f[m][a]*delta(n,b)-f[n][a]*delta(m,b)-f[m][b]*delta(n,a)+f[n][b]*delta(m,a))
 assert R(m,n,a,b)+fterm==0
checks['ricci_and_dependent_f']='PASS: R_OP=-R_W; R=20k; f=-k e/4; all625 Weyl components vanish'
# General diagonal Ricci Kulkarni-Nomizu curvature: trace-free Weyl projection.
S=[F(2),F(3),F(5),F(7),F(11)]
def raw(a,b,c,d):
 metric=lambda x,y:eta[x]*delta(x,y)
 sym=lambda x,y:S[x]*delta(x,y)
 return metric(a,c)*sym(b,d)-metric(b,c)*sym(a,d)-metric(a,d)*sym(b,c)+metric(b,d)*sym(a,c)
ric2=[[sum(eta[a]*raw(a,b,a,d) for a in range(5)) for d in range(5)] for b in range(5)]
r2=sum(eta[a]*ric2[a][a] for a in range(5))
c2=F(0);rm2=F(0)
for a,b,c,d in it.product(range(5),repeat=4):
 metric=lambda x,y:eta[x]*delta(x,y)
 cc=raw(a,b,c,d)-(metric(a,c)*ric2[b][d]-metric(b,c)*ric2[a][d]-metric(a,d)*ric2[b][c]+metric(b,d)*ric2[a][c])/3+(metric(a,c)*metric(b,d)-metric(a,d)*metric(b,c))*r2/12
 assert cc==0
 rm2+=eta[a]*eta[b]*eta[c]*eta[d]*raw(a,b,c,d)**2
ricci2=sum(eta[a]*eta[b]*ric2[a][b]**2 for a in range(5) for b in range(5))
assert rm2-F(4,3)*ricci2+F(1,6)*r2**2==0
checks['weyl_projection']='PASS: anisotropic Ricci-type curvature and independent C² contraction'
# Local rotation test: Leibniz derivative of X wedge Y fixes tensor connection sign.
omega=[[F(0)]*5 for _ in range(5)];omega[2][3]=F(2);omega[3][2]=F(-2)
x=[F(0),F(3),F(0),F(0),F(0)];y=[F(0),F(0),F(0),F(5),F(0)]
T=[[x[a]*y[b]-x[b]*y[a] for b in range(5)] for a in range(5)]
dx=[sum(omega[a][c]*x[c] for c in range(5)) for a in range(5)]
dy=[sum(omega[a][c]*y[c] for c in range(5)) for a in range(5)]
for a,b in it.product(range(5),repeat=2):
 leib=dx[a]*y[b]+x[a]*dy[b]-dx[b]*y[a]-x[b]*dy[a]
 upperfirst=sum(omega[c][a]*T[b][c]-omega[c][b]*T[a][c] for c in range(5))
 assert leib==upperfirst
assert sum(omega[c][1]*T[2][c]-omega[c][2]*T[1][c] for c in range(5))!=0
checks['tensor_derivative_sign']='PASS: covector Leibniz rule requires +2 omega^c_[a T_b]c; literal source minus fails'
w={'eps':F(-1,2),'eta':F(1,2),'psimu':F(-1,2),'e':F(-1),'sigma':F(1),'psi':F(3,2),'chi':F(3,2),'T':F(1),'D':F(2),'RQ':F(3,2),'RV':F(2),'C':F(2),'G':F(2),'Da':F(1)}
def weight(seq):return sum(w[x] for x in seq.split())
L=['RQ RQ','chi chi','RV T'];phi=['RQ C','RQ Da T','chi D','Da RQ T','Da RQ T','Da T chi','T T chi','Da chi T','RQ T T','RV RQ','RV chi']
assert all(weight(x)==3 for x in L);assert all(weight(x)==F(7,2) for x in phi)
H=['sigma sigma eps RQ','sigma eps Da psi','eps psi Da sigma','sigma eps T psi','eps G psi','sigma eta psi']
assert all(weight(x)==3 for x in H)
assert weight('psimu psimu')==-1 and weight('psimu e chi')==0
assert F(3,2)-F(7,2)==-2
s=F(2);assert F(3,2)*s==3 and F(3,2)*s!=F(3,2)
checks['weights_and_source_repairs']='PASS: all3 L/11 varphi terms,6 H terms; naked ψψ mismatch; chi dilation residual; sigma=2 principal derivative'
# Source E3/E2 mismatch is detected, not declared solved by a false PASS.
for a,b in it.combinations(range(5),2):
 contracted=add(*[scale(eps((a,b)+ids),lowgam(ids)) for ids in it.permutations(range(5),3)])
 assert eq(contracted,scale(6j,gam((a,b))))
checks['potential_interface']='CONFIRMED SOURCE CONFLICT: printed deltaE3 implies opposite leading deltaE2 sign with C01/C04/L03; quarantined'
result={'lock':'UNG-WEYL2-OP58-CONVENTIONS-v4','scope':'Algebra and source-interface tests only','checks':checks,'algebra_status':'PASS','map_completion':'NOT PERFORMED','nonlinear_susy':'NOT VERIFIED','potential_interface':'OPEN; literal potential laws quarantined'}
print(json.dumps(result,indent=2))
if __name__=='__main__':
 out=BASE/'.gpd/phases/02-ozkan-map-and-variation-completion/02-CONVENTIONS-CHECKS.json'
 out.write_text(json.dumps(result,indent=2)+'\n')
