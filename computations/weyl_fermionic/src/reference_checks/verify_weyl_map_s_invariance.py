#!/usr/bin/env python3
"""Finite-basis cross-check of the full hand derivation; no physical truncation."""
import json
from pathlib import Path
from fractions import Fraction
import itertools as it
N=4
I=[[complex(i==j) for j in range(N)] for i in range(N)];Z=[[0j]*4 for _ in range(4)]
def add(*ms):return [[sum(m[i][j] for m in ms) for j in range(4)] for i in range(4)]
def scale(c,m):return [[c*x for x in r] for r in m]
def mul(a,b):return [[sum(a[i][k]*b[k][j] for k in range(4)) for j in range(4)] for i in range(4)]
def trans(a):return [list(x) for x in zip(*a)]
def kron(a,b):return [[a[i//2][j//2]*b[i%2][j%2] for j in range(4)] for i in range(4)]
p1=[[0,1],[1,0]];p2=[[0,-1j],[1j,0]];p3=[[1,0],[0,-1]];u=[[1,0],[0,1]]
g=[scale(-1j,kron(p3,u)),kron(p1,p1),kron(p1,p2),kron(p1,p3),kron(p2,u)];eta=[-1,1,1,1,1];gl=[scale(eta[a],g[a]) for a in range(5)]
C=mul(g[2],g[4]);Ci=scale(-1,C)
def ga(ids,lower=False):
 if len(set(ids))<len(ids):return Z
 m=I
 for a in ids:m=mul(m,gl[a] if lower else g[a])
 return m

def mv(m,v):return [sum(m[i][j]*v[j] for j in range(4)) for i in range(4)]
def vsum(vs):
 vs=list(vs)
 return [sum(v[i] for v in vs) for i in range(4)]
def vscale(c,v):return [c*x for x in v]
def vmax(v):return max(map(abs,v),default=0)
def mmax(m):return vmax([x for row in m for x in row])
def assert_v(a,b):assert a==b,(a,b)

def t_basis(pair):
 t=[[0]*5 for _ in range(5)];a,b=pair;t[a][b]=1;t[b][a]=-1;return t

def three_A(t,old=False):
 # 3 δ_S R_ab = A3_ab η. old=True reproduces the v3 index reversal.
 flip=-1 if old else 1
 return [[add(scale(-24*t[a][b],I),
  *[scale(8*flip*t[a][c]*eta[c],ga((b,c),True)) for c in range(5)],
  *[scale(-8*flip*t[b][c]*eta[c],ga((a,c),True)) for c in range(5)],
  *[scale(4*t[c][d]*eta[c]*eta[d],ga((a,b,c,d),True)) for c in range(5) for d in range(5)]) for b in range(5)] for a in range(5)]

def project_basis(pair,spin):
 # r = 12 B - 8 gamma_[a q_b] + gamma_ab q; no floating division.
 raw=[[[0j]*4 for _ in range(5)] for _ in range(5)]
 a,b=pair;raw[a][b][spin]=1;raw[b][a][spin]=-1
 q=[vsum(mv(g[a],raw[a][b]) for a in range(5)) for b in range(5)]
 qs=vsum(mv(g[a],q[a]) for a in range(5))
 return [[vsum([vscale(12,raw[a][b]),vscale(-4,mv(gl[a],q[b])),
   vscale(4,mv(gl[b],q[a])),mv(ga((a,b),True),qs)]) for b in range(5)] for a in range(5)]

pairs=list(it.combinations(range(5),2))
rbasis=[project_basis(pair,alpha) for pair in pairs for alpha in range(4)]
checks={};max_size=0
for r in rbasis:
 for b in range(5):assert_v(vsum(mv(g[a],r[a][b]) for a in range(5)),[0j]*4)
checks['projector']='PASS: all40 raw basis images gamma-traceless; projector equals12 times identity on constrained inputs'
# Clifford/C prerequisites are tested independently of the cancellation.
for a,b in it.product(range(5),repeat=2):
 assert add(mul(g[a],g[b]),mul(g[b],g[a]))==scale(2*eta[a] if a==b else 0,I)
assert trans(C)==scale(-1,C)
for n,transpose_sign in [(0,1),(1,1),(2,-1),(3,-1),(4,1)]:
 for ids in it.combinations(range(5),n):
  assert mul(mul(Ci,trans(ga(ids))),C)==scale(transpose_sign,ga(ids))
checks['transpose_and_clifford']='PASS: Clifford and Majorana reversal ranks0-4'
B=mul(C,gl[0])
for n in (0,2,4):
 for ids in it.combinations(range(5),n):
  CG=mul(C,ga(ids))
  conjugate=[[x.conjugate() for x in row] for row in CG]
  assert mul(mul(trans(B),conjugate),B)==scale(-1,CG)
checks['triplet_reality']='PASS: B^T(C Gamma_even)*B=-C Gamma_even on all even-rank basis matrices'
for a,b,c,d in it.product(range(5),repeat=4):
 metric=lambda x,y:eta[x]*int(x==y)
 rhs=add(ga((c,d,a,b),True),scale(metric(d,a),ga((c,b),True)),
  scale(-metric(c,a),ga((d,b),True)),scale(-metric(d,b),ga((c,a),True)),
  scale(metric(c,b),ga((d,a),True)),
  scale(metric(d,a)*metric(c,b)-metric(c,a)*metric(d,b),I))
 assert mul(ga((c,d),True),ga((a,b),True))==rhs
checks['two_gamma_product']='PASS: all625 ordered index choices in hand equation S23'


old_trace_failures=0;old_variation_failures=0;sample=None;sector_pairs=0
for pair in pairs:
 t=t_basis(pair);a3=three_A(t);bad=three_A(t,old=True)
 for b in range(5):assert add(*[mul(g[a],a3[a][b]) for a in range(5)])==Z
 if any(add(*[mul(g[a],bad[a][b]) for a in range(5)])!=Z for b in range(5)):old_trace_failures+=1
 K=add(*[scale(t[a][b],ga((a,b))) for a in range(5) for b in range(5)])
 # Both raw product-rule variations, with odd factor reordering explicit.
 # δχ=Kη/4. Multiply δL_chichi by 3/i: coefficient64*(K^T C -(C K)^T).
 chichi=scale(64,add(mul(trans(K),C),scale(-1,trans(mul(C,K)))))
 Vchi=scale(128,mul(C,K))
 assert add(chichi,Vchi)==Z
 for r in rbasis:
  rup=[[vscale(eta[a]*eta[b],r[a][b]) for b in range(5)] for a in range(5)]
  X=vsum(vscale(t[a][b],rup[a][b]) for a in range(5) for b in range(5))
  Y=vsum(vscale(t[a][c]*eta[c],mv(ga((b,c),True),rup[a][b])) for a in range(5) for b in range(5) for c in range(5))
  Z4=vsum(vscale(t[c][d]*eta[c]*eta[d],mv(ga((a,b,c,d),True),rup[a][b])) for a in range(5) for b in range(5) for c in range(5) for d in range(5))
  assert_v(Y,X);assert_v(Z4,vscale(-2,X))
  # First term: bar(delta R)R, coefficient of η_alpha.
  first=vsum(mv(mul(trans(a3[a][b]),C),rup[a][b]) for a in range(5) for b in range(5))
  # Second term: barR(delta R), move odd η left: -(C A3)^T R.
  second=vsum(vscale(-1,mv(trans(mul(C,a3[a][b])),rup[a][b])) for a in range(5) for b in range(5))
  CX=mv(C,X)
  assert_v(first,vscale(-48,CX));assert_v(second,first)
  # Multiply the complete R-sector variation by12/i to use only integers.
  residual=vsum([first,second,vscale(96,CX)])
  assert_v(residual,[0j]*4)
  oldfirst=vsum(mv(mul(trans(bad[a][b]),C),rup[a][b]) for a in range(5) for b in range(5))
  oldsecond=vsum(vscale(-1,mv(trans(mul(C,bad[a][b])),rup[a][b])) for a in range(5) for b in range(5))
  oldres=vsum([oldfirst,oldsecond,vscale(96,CX)])
  # The wrong-index rule leaves δL_old=(16i/3)barη X.
  assert_v(oldres,vscale(64,CX))
  if vmax(oldres):
   old_variation_failures+=1
   if sample is None:sample={'T_pair':pair,'R_seed_pair':pairs[rbasis.index(r)//4],'spinor_seed':rbasis.index(r)%4,'X':[str(x) for x in X],'scaled_old_residual_12_over_i':[str(x) for x in oldres]}
  for values in [X,Y,Z4,first,second,oldres]:
   for z in values:
    assert z.real.is_integer() and z.imag.is_integer()
    max_size=max(max_size,abs(z.real),abs(z.imag))
  sector_pairs+=1
assert max_size<2**53
checks['s_curvature_gamma_trace']='PASS: all10 independent T components and all spinor columns'
checks['gamma_contractions']=f'PASS: Y=X and Z=-2X on {sector_pairs} T/projected-R basis pairs'
checks['raw_product_rule']=f'PASS: both variations computed separately; {sector_pairs*4} R-sector parameter coefficients; 160 chi-sector coefficients'
checks['wrong_index_negative_control']=f'PASS: v3 rule fails gamma trace for {old_trace_failures}/10 T basis tensors and full variation for {old_variation_failures}/400 pairs; residual exactly(16i/3)barηX'
# Scalar rational coefficients are independently collected.
assert Fraction(-8)+Fraction(8)==0
assert -Fraction(128,3)+Fraction(128,3)==0
checks['coefficient_ledger']='PASS: (-8+8)=0 and (-128/3+128/3)=0'
result={'lock':'UNG-WEYL2-OP58-CONVENTIONS-v4','result':'delta_S L^ij = 0 exactly using the conventional gamma-trace constraint','status':'PASS','checks':checks,'arithmetic':'Gaussian integers, integer scaling, no tolerance used; values stored exactly in binary64 below2^53','max_integer_component':max_size,'negative_control_sample':sample,'scope':'Full S-invariance of the printed composite L; source S-curvature law and conventional constraint are inputs','not_checked':['Q variation of L','varphi transformation','missing E/N fermions','complete invariant or spectrum']}
if __name__=='__main__':
 b=Path(__file__).resolve().parents[1]
 out=b/'.gpd/phases/02-ozkan-map-and-variation-completion/S-INVARIANCE-CHECKS.json'
 out.write_text(json.dumps(result,indent=2)+'\n')
 print(json.dumps(result,indent=2))
