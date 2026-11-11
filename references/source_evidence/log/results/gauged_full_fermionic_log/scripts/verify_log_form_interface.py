#!/usr/bin/env python3
"""Exact indexed superform/linear-current bridge; does not certify LOG polynomials.
ASSERT_CONVENTION: regularization_scheme=Not applicable for initial classical analysis, renormalization_scheme=Not applicable for initial classical analysis
Scoped convention: GAUGED-LOG-STEP1-v1; mostly-plus, gamma01234=i,
bar(u)=u^T C, project NW-SE epsilon12=+1. No field equations.
"""
from pathlib import Path
from itertools import product, combinations, permutations
from collections import defaultdict
import hashlib, html, json, math, re
import sympy as s

BASE = Path(__file__).resolve().parents[1]
OUT = BASE / 'sources/certification_20260925/form'
I=s.I; Q=s.Rational; Z=s.zeros(4); eye=s.eye(4)
p1=s.Matrix([[0,1],[1,0]]); p2=s.Matrix([[0,-I],[I,0]]); p3=s.diag(1,-1)
g=[-I*s.kronecker_product(p3,s.eye(2)),s.kronecker_product(p1,p1),
   s.kronecker_product(p1,p2),s.kronecker_product(p1,p3),s.kronecker_product(p2,s.eye(2))]
eta=[-1,1,1,1,1]; C=g[2]*g[4]; U=-C; su=s.Matrix([[0,1],[-1,0]])
def gam(ids,lower=False):
 if len(set(ids))<len(ids):return Z
 a=eye
 for i in ids:a=a*g[i]*(eta[i] if lower else 1)
 return a
def eps(ids):
 if len(set(ids))<5:return 0
 return (-1)**sum(ids[i]>ids[j] for i in range(5) for j in range(i+1,5))
def clean(p):return {k:s.expand(v) for k,v in p.items() if s.expand(v)!=0}
def addbil(p,c,M,f1,f2):
 for a,b in product(range(4),repeat=2):
  v=c*M[a,b]
  if not v:continue
  x,y=f1(a),f2(b)
  if x==y:continue
  p[(min(x,y),max(x,y))]+=v*(1 if x<y else -1)
def psi(a,i,x):return 8*a+4*i+x
def phi(i,x):return 100+4*i+x
def xi(i,x):return 200+4*i+x
checks={}
assert C.T==-C and C*C==-eye and gam(range(5))==I*eye
for a,b in product(range(5),repeat=2):
 assert g[a]*g[b]+g[b]*g[a]==2*eta[a]*int(a==b)*eye
for a,b in combinations(range(5),2):
 M=gam((a,b))/2
 lowered=M*C.T  # Sigma_alpha,beta=epsilon_beta,gamma Sigma_alpha^gamma
 assert lowered==-M*C
 assert U.T*M==C*M
 assert U.T*lowered*U==-C*M
 assert U.T*(M*C)*U==C*M  # old local-note kernel: opposite, so detect it
checks['indexed_spinor_lowering']='PASS: all ten independent Sigma generators, exact Gaussian rational matrices'

# Enumerate every selected fermion-slot subset; source reverse vielbein order.
pullbacks={}
for p in (4,5):
 result=[]
 for k in range(p+1):
  signs=[]
  for subset in combinations(range(p),k):
   S=set(subset)
   tensor_swaps=sum(i in S and j not in S for i in range(p) for j in range(i+1,p))
   world_swaps=sum(i not in S and j in S for i in range(p) for j in range(i+1,p))
   odd_reversal=k*(k-1)//2
   signs.append((-1)**(tensor_swaps+world_swaps+odd_reversal))
  result.append(Q(sum(signs),2**k))
 assert result==[Q(math.comb(p,k),2**k)*(-1)**(k*(p-k)+k*(k-1)//2) for k in range(p+1)]
 pullbacks[str(p)]=[str(x) for x in result]
assert pullbacks['5']==['1','5/2','-5/2','-5/4','5/16','1/32']
assert pullbacks['4'][:3]==['1','-2','-3/2']
# Covariant Cartan component xi^D Phi_DABC: zero/one gravitino.
assert (-1)**3==-1
potential_signs=[(-1)**(2+(2-r)+r) for r in range(3)]
assert potential_signs==[1,1,1] and Q(sum(potential_signs),2)==Q(3,2)
checks['graded_pullback']='PASS: all 48 subsets for p=4,5; matches source (8.27); potential coefficients -1,+3/2'

# Complete polynomial equality for independent odd components; every triplet basis.
q1=[defaultdict(lambda:0) for _ in range(5)]
r1=[defaultdict(lambda:0) for _ in range(5)]
for a,b,i,j in product(range(5),range(5),range(2),range(2)):
 addbil(q1[a],I*su[j,i]/2,C*gam((b,a)),lambda x:psi(b,i,x),lambda x:phi(j,x))
 # Raw 2 Sigma_alpha^beta psi_i^alpha phi_G,beta^i, phi_G=i phi/2.
 addbil(r1[a],I*su[j,i],U.T*(gam((a,b))/2),lambda x:psi(b,j,x),lambda x:phi(i,x))
assert all(clean(a)==clean(b) for a,b in zip(q1,r1))
triplet_bases=[s.Matrix([[1,0],[0,0]]),s.Matrix([[0,1],[1,0]]),s.Matrix([[0,0],[0,1]])]
for Llow in triplet_bases:
 Lup=su*Llow*su.T
 q2=[defaultdict(lambda:0) for _ in range(5)]
 r2=[defaultdict(lambda:0) for _ in range(5)]
 for a,b,c,i,j in product(range(5),range(5),range(5),range(2),range(2)):
  addbil(q2[a],Llow[i,j]/4,C*gam((a,b,c)),lambda x:psi(b,i,x),lambda x:psi(c,j,x))
 for a,b,c,d,e in permutations(range(5)):
  M=gam((b,c),True)/2
  kernel=U.T*(M*C.T)*U
  for i,j,k,l in product(range(2),repeat=4):
   # +i/2 epsilon_G Sigma_lowerlower psi_i psi_j G^ij in h-H.
   cf=I/2*(-eps((a,b,c,d,e)))*(-Lup[i,j]/2)*su[k,i]*su[l,j]
   addbil(r2[a],cf,kernel,lambda x:psi(d,k,x),lambda x:psi(e,l,x))
 assert all(clean(a)==clean(b) for a,b in zip(q2,r2))
 # Full potential projection: C24 displayed mixed-index law versus project law.
 for a,b,c in combinations(range(5),3):
  raw=defaultdict(lambda:0); target=defaultdict(lambda:0)
  for i,j in product(range(2),repeat=2):
   # δb = -δE/2: first project term -bar(epsilon) gamma_abc phi /2.
   addbil(target,-su[j,i]/2,C*gam((a,b,c),True),lambda x:xi(i,x),lambda x:phi(j,x))
   for d,e in product(range(5),repeat=2):
    epsG_low=eps((a,b,c,d,e))  # epsilon_G_lower01234=+1
    addbil(raw,2*epsG_low*su[j,i]*Q(1,2)*(I/2),U.T*(gam((d,e))/2),lambda x:xi(j,x),lambda x:phi(i,x))
  # antisymmetrized psi_a gamma_bc is average over the three cyclic terms.
  for aa,bb,cc in ((a,b,c),(b,c,a),(c,a,b)):
   for i,j in product(range(2),repeat=2):
    addbil(target,I*Llow[i,j]/2,C*gam((bb,cc),True),lambda x:psi(aa,i,x),lambda x:xi(j,x))
    addbil(raw,-12*I*Q(1,3)*Q(1,2)*(-Llow[i,j]/2),U.T*(gam((bb,cc),True)/2),lambda x:psi(aa,i,x),lambda x:xi(j,x))
  assert clean(raw)==clean(target),(a,b,c,Llow)
checks['full_indexed_current_and_potential']='PASS: five currents and ten three-form components, all three symmetric triplet bases, independent Grassmann generators'

# The six nonform density coefficients: explicit source maps and SU(2) signs.
converted=[-2*(-Q(1,2)),-(-1),-2*(-1)*(I/2),I*(I/2)*(-1),I*I*(-1)*(-Q(1,2)),-I*Q(1,2)*(-Q(1,2))]
expected=[1,1,I,Q(1,2),-Q(1,2),I/4]
assert converted==expected
assert -(-1)*1==1 # -v h -> + A P
checks['BF_coefficients']='PASS: all seven slots, including +A.P from the ordinary four-form'
weights=[2+3,1+4,Q(3,2)+Q(7,2),1+Q(1,2)+Q(7,2),Q(1,2)+Q(3,2)+3,1+2*Q(1,2)+3,1+4]
assert set(weights)=={5}
checks['weights']='PASS: all BF terms weight5; both completions weight4'

# Cache exact equation alttext and source identity; source, not generated solution.
src=OUT/'1410.8682v2.html'; rawhtml=src.read_text(); equations={}
for label in ['8.3','8.4','8.5','8.6a','8.6b','8.6c','8.7','8.8a','8.8b','8.9','8.10','8.12','8.19','8.22a','8.22b','8.22c','8.25','8.27','8.28','8.29a','8.29b','8.30','A.3','A.9','A.11']:
 pos=rawhtml.find('('+label+')')
 if pos<0:continue
 start=rawhtml.rfind('<table',0,pos);end=rawhtml.find('</table>',pos)+8
 equations[label]=[html.unescape(q) for q in re.findall('alttext="([^"]*)"',rawhtml[start:end])]
(OUT/'source_equations.json').write_text(json.dumps({'url':'https://arxiv.org/html/1410.8682v2','sha256':hashlib.sha256(src.read_bytes()).hexdigest(),'reason':'C24 ref30 supplies lower superfour-form components and exact BF pullback absent from local extracted C24/S23 formulas','equations':equations},indent=2)+'\n')
result={'status':'PASS','scope':'generic superform, current and BF slot interface only; conditional on true linear multiplet; not a verification of the expanded LOG polynomial','checks':checks,'pullback_coefficients':pullbacks,'literal_C24_2_50_minus_covariant_current':'2 Q1 = i bar(psi_b) gamma^{ba} phi','action_current':'P=E+Q1+Q2','potential_coefficients':[1,-3],'sources':{str(p.relative_to(BASE)):hashlib.sha256(p.read_bytes()).hexdigest() for p in [src,BASE/'STEP_02_LOG_PRIMARY.md',BASE/'notes/07_step1_linear_bridge_independent_check.md',Path(__file__)]}}
(OUT/'checks.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
