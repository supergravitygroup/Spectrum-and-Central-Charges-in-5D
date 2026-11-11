import ast,itertools as it,json
from pathlib import Path
#!/usr/bin/env python3
"""Check H50 hand completion: finite Clifford identities, Fierz coefficients,
index bookkeeping and addition. Not a nonlinear closure or action check."""
from fractions import Fraction as F
from collections import Counter,defaultdict
import hashlib,re
BASE=Path(__file__).resolve().parents[1]
PHASE=BASE/'.gpd/phases/02-ozkan-map-and-variation-completion'
NOTE=PHASE/'DERIVATION-fermionic-map.md'
checks={}
p=Path(__file__).resolve().parent/'verify_weyl_spinor_q_variation.py'
ns={};exec('from itertools import product',ns)
for n in ast.parse(p.read_text()).body:
 if isinstance(n,ast.FunctionDef) and n.name in {'eye','zero','add','scale','mm','tr','transpose','kron','gm','metric','eps'}:exec(compile(ast.Module(body=[n],type_ignores=[]),str(p),'exec'),ns)
exec('I=eye(4); Z=zero(4); I2=eye(2)\ns1=[[0,1],[1,0]];s2=[[0,-1j],[1j,0]];s3=[[1,0],[0,-1]]\ngamma=[scale(-1j,kron(s3,I2)),kron(s1,s1),kron(s1,s2),kron(s1,s3),kron(s2,I2)]\neta=[-1,1,1,1,1]',ns)
mm,add,sc,gm,Z,eta=[ns[k] for k in ['mm','add','scale','gm','Z','eta']]
g=lambda a:sc(eta[a],gm((a,)))
rg=range(5);pairs=list(it.combinations(rg,2))
def norm(m):return max(abs(z) for row in m for z in row)
def dif(a,b):return norm(add(a,sc(-1,b)))
def run(T,U):
 K=add(*[sc(T[a][b],gm((a,b))) for a,b in it.product(rg,repeat=2)])
 DK=[add(*[sc(U[c][a][b],gm((a,b))) for a,b in it.product(rg,repeat=2)]) for c in rg]
 q=[[add(sc(1j,mm(DK[a],g(b))),sc(-1j,mm(DK[b],g(a))),sc(-1,mm(mm(mm(K,g(a)),K),g(b))),mm(mm(mm(K,g(b)),K),g(a))) for b in rg] for a in rg]
 err=[]
 for a in rg:
  lhs=add(*[sc(1j/3,mm(gm((b,)),q[a][b])) for b in rg],*[sc(-1j/24,mm(mm(g(a),gm((b,c))),q[b][c])) for b,c in it.product(rg,repeat=2)])
  rhs=add(*[sc(1/3,mm(mm(gm((b,)),DK[b]),g(a))) for b in rg],sc(-1/3,DK[a]),*[sc(eta[b]*U[b][b][c]/3,mm(g(a),gm((c,)))) for b,c in it.product(rg,repeat=2)],*[sc(-1j*eta[a]*T[b][c]*T[d][e],gm((a,b,c,d,e))) for b,c,d,e in it.product(rg,repeat=4)],*[sc(8j*eta[c]*T[b][c]*T[a][c],gm((b,))) for b,c in it.product(rg,repeat=2)],sc(-2j*sum(eta[b]*eta[c]*T[b][c]**2 for b,c in it.product(rg,repeat=2)),g(a)))
  err.append(dif(lhs,rhs))
 return max(err)
zeroT=lambda:[[0]*5 for _ in rg]
zeroU=lambda:[zeroT() for _ in rg]
errs=[]
for c in rg:
 for a,b in pairs:
  U=zeroU();U[c][a][b]=1;U[c][b][a]=-1
  errs.append(run(zeroT(),U))
assert max(errs)<1e-12
checks['S_connection_derivative_terms']={'status':'PASS','independent_DT_jets':50,'components_per_jet':5,'max_error':max(errs)}
errs=[]
for config in [(p,) for p in pairs]+list(it.combinations(pairs,2)):
 T=zeroT()
 for a,b in config:T[a][b]=1;T[b][a]=-1
 errs.append(run(T,zeroU()))
assert max(errs)<1e-12
checks['S_connection_quadratic_terms']={'status':'PASS','two_form_basis_and_polarizations':55,'components_per_configuration':5,'max_error':max(errs)}

maxerr=[0,0,0]
for cfg in [(p,) for p in pairs]+list(it.combinations(pairs,2)):
 T=zeroT()
 for a,b in cfg:T[a][b]=1;T[b][a]=-1
 K=add(*[sc(T[a][b],gm((a,b))) for a,b in it.product(rg,repeat=2)])
 t2=sum(eta[b]*eta[c]*T[b][c]**2 for b,c in it.product(rg,repeat=2))
 for a in rg:
  Q=add(*[sc(eta[a]*T[b][c]*T[d][e],gm((a,b,c,d,e))) for b,c,d,e in it.product(rg,repeat=4)])
  V=add(*[sc(eta[c]*T[b][c]*T[a][c],gm((b,))) for b,c in it.product(rg,repeat=2)])
  W=add(*[sc(T[a][b]*T[c][d],gm((b,c,d))) for b,c,d in it.product(rg,repeat=3)])
  A=add(*[mm(mm(mm(mm(gm((b,)),K),g(a)),K),g(b)) for b in rg])
  B=mm(mm(K,K),g(a))
  CC=add(*[mm(mm(mm(mm(mm(g(a),gm((b,c))),K),g(b)),K),g(c)) for b,c in it.product(rg,repeat=2)])
  for k,(lhs,rhs) in enumerate([(A,add(sc(5,Q),sc(-24,V),sc(6*t2,g(a)))),(B,add(Q,sc(-4,W),sc(-2*t2,g(a)))),(CC,add(sc(4,Q),sc(16,W),sc(8*t2,g(a))))]):maxerr[k]=max(maxerr[k],dif(lhs,rhs))
assert max(maxerr)<1e-12
checks['three_H59a_gamma_products']={'status':'PASS','basis_polarizations':55,'vector_indices':5,'products':3,'max_errors':maxerr}

# Every new transpose pattern, including the antisymmetrized three-factor product.
charge=mm(gm((2,)),gm((4,)));ci=sc(-1,charge)
trans=ns['transpose']
tilde=lambda m:mm(mm(ci,trans(m)),charge)
n=0
for (c,d),a,e in it.product(pairs,rg,rg):
 K=gm((c,d))
 tests=[(mm(K,gm((e,))),sc(-1,mm(gm((e,)),K))),
        (mm(K,gm((a,e))),mm(gm((a,e)),K)),
        (mm(mm(K,gm((e,))),gm((a,))),sc(-1,mm(mm(gm((a,)),gm((e,))),K))),
        (mm(mm(gm((a,)),K),gm((c,d))),mm(mm(gm((c,d)),K),gm((a,)))),
        (mm(gm((a,)),K),sc(-1,mm(K,gm((a,))))),
        (mm(mm(gm((a,)),K),gm((e,))),sc(-1,mm(mm(gm((e,)),K),gm((a,)))))]
 for lhs,rhs in tests:assert dif(tilde(lhs),rhs)==0;n+=1
 anti=add(mm(mm(gm((a,)),K),gm((e,))),sc(-1,mm(mm(gm((e,)),K),gm((a,)))))
 assert dif(tilde(anti),anti)==0;n+=1
checks['Majorana_transposes']={'status':'PASS','matrix_cases':n}

# H65: prove the entire Schouten contraction on a basis of gamma-traceless
# spinor two-forms and arbitrary f_ab. No Ricci-symmetry assumption is used.
def mv(m,v):return [sum(m[i][j]*v[j] for j in range(4)) for i in range(4)]
def va(*v):return [sum(x[i] for x in v) for i in range(4)]
def vs(c,v):return [c*x for x in v]
count=0;maxerror=0
for (u,v),alpha in it.product(pairs,range(4)):
 raw=[[[0j]*4 for _ in rg] for _ in rg];raw[u][v][alpha]=1;raw[v][u][alpha]=-1
 ph=[va(*[vs(1j/3,mv(gm((b,)),raw[a][b])) for b in rg],*[vs(-1j/24,mv(mm(g(a),gm((b,c))),raw[b][c])) for b,c in it.product(rg,repeat=2)]) for a in rg]
 rq=[[va(raw[a][b],vs(-1j,mv(g(a),ph[b])),vs(1j,mv(g(b),ph[a]))) for b in rg] for a in rg]
 for b in rg:assert max(map(abs,va(*[mv(gm((a,)),rq[a][b]) for a in rg])))<1e-12
 for k,l in it.product(rg,repeat=2):
  lhs=[0j]*4
  for a,b,c,d in it.product(rg,repeat=4):
   # 8 f_[a[c eta_b]d] = 2*(four terms); choose f_kl=1.
   f=lambda x,y:int(x==k and y==l)
   met=lambda x,y:eta[x]*int(x==y)
   factor=2*(f(a,c)*met(b,d)-f(b,c)*met(a,d)-f(a,d)*met(b,c)+f(b,d)*met(a,c))
   if factor:lhs=va(lhs,vs(factor*eta[a]*eta[b],mv(gm((c,d)),rq[a][b])))
  rhs=vs(-8*eta[k]*eta[l],rq[k][l]);err=max(abs(x-y) for x,y in zip(lhs,rhs))
  maxerror=max(maxerror,err);assert err<1e-12;count+=1
checks['dependent_f_contraction_H65']={'status':'PASS','gamma_traceless_spinor_basis_times_f_basis':count,'max_error':maxerror}

errT=0;errD=0
for kind in ['T','DT']:
 configs=[(p,) for p in pairs]+list(it.combinations(pairs,2)) if kind=='T' else list(it.product(rg,pairs))
 for cfg in configs:
  T=zeroT();U=zeroU()
  if kind=='T':
   for a,b in cfg:T[a][b]=1;T[b][a]=-1
  else:
   c,(a,b)=cfg;U[c][a][b]=1;U[c][b][a]=-1
  K=add(*[sc(T[a][b],gm((a,b))) for a,b in it.product(rg,repeat=2)])
  DK=[add(*[sc(U[c][a][b],gm((a,b))) for a,b in it.product(rg,repeat=2)]) for c in rg]
  q=[[add(sc(1j,mm(DK[a],g(b))),sc(-1j,mm(DK[b],g(a))),sc(-1,mm(mm(mm(K,g(a)),K),g(b))),mm(mm(mm(K,g(b)),K),g(a))) for b in rg] for a in rg]
  ph=[add(*[sc(1j/3,mm(gm((b,)),q[a][b])) for b in rg],*[sc(-1j/24,mm(mm(g(a),gm((b,c))),q[b][c])) for b,c in it.product(rg,repeat=2)]) for a in rg]
  for a,b in pairs:
   lhs=add(q[a][b],sc(-1j,mm(g(a),ph[b])),sc(1j,mm(g(b),ph[a])))
   rhs=add(sc(1j,mm(DK[a],g(b))),sc(-1j,mm(DK[b],g(a))),sc(-1j/3,mm(g(b),DK[a])),sc(1j/3,mm(g(a),DK[b])),*[sc(-1j/3,mm(mm(g(a),gm((c,))),mm(DK[c],g(b)))) for c in rg],*[sc(1j/3,mm(mm(g(b),gm((c,))),mm(DK[c],g(a)))) for c in rg],*[sc(-2j/3*eta[a]*eta[b]*eta[c]*U[c][c][d],mm(gm((a,b)),gm((d,)))) for c,d in it.product(rg,repeat=2)])
   if kind=='T':errT=max(errT,dif(lhs,rhs))
   else:errD=max(errD,dif(lhs,rhs))
assert errD<1e-12 and errT<1e-12
checks['normal_frame_R01_to_R05_crosscheck']={'status':'PASS','DT_jets':50,'T_basis_polarizations':55,'curvature_index_pairs':10,'DT_max_error':errD,'T_squared_residual':errT}

j=json.loads((PHASE/'H50-COMPLETION-LEDGER.json').read_text())
text=NOTE.read_text()
# This check audits Part IV (H50), not later canonicalization chapters that
# legitimately introduce their own notation.
part=text.split('# Part IV',1)[1].split('# Part V',1)[0]
new=text.split('### 27.3 ',1)[1]
origins={1:'C',2:'U',4:'Y',5:'Y',6:'U',8:'Z'}
raw=json.loads((PHASE/'VARPHI-Q-TERM-LEDGER.json').read_text())
outer={n:tuple(map(F,next(t for t in raw['terms'][str(n)] if t['label']==s)['coefficient'])) for n,s in origins.items()}
assert outer=={1:(F(-1,8),F(0)),2:(F(0),F(-4)),4:(F(0),F(8)),5:(F(0),F(8)),6:(F(0),F(-64,3)),8:(F(0),F(128,3))}
def cmul(a,b):return a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0]
# Weighted antisymmetrization is expanded before the three Fierz ranks are displayed.
for f in j['fierz_inputs']:
 facts=[F(3,16),F(3,16),F(-3,32)] if f['triplet'] else [F(1,8),F(1,8),F(-1,16)]
 assert len(f['rows'])==3*2**len(f['antisym_pairs'])
 for row in f['rows']:
  expected=cmul(tuple(map(F,f['coefficient'])),(f['transpose_sign']*facts[row['rank']]*F(row['antisym_factor']),F(0)))
  assert expected==tuple(map(F,row['coefficient'])),f['origin']
  assert abs(F(row['antisym_factor']))==F(1,2**len(f['antisym_pairs']))
  assert '[' not in row['latex'] and ']' not in row['latex']
  assert row['latex'] in new
checks['explicit_Fierz_coefficients']={'status':'PASS','physical_products':len(j['fierz_inputs']),'weighted_antisymmetry_expanded':True,'basis_ranks':'0,1,2; full-pair rank-two sum'}

# All Lorentz dummy indices occur exactly twice. epsilon has the sole free i.
number=0
for block,rows in j['blocks'].items():
 for row in rows:
  s=row['latex'];counts=Counter()
  for m in re.finditer(r'[_^](?:\{([^{}]*)\}|([a-z]))',s):
   chars=re.sub(r'\\[A-Za-z]+','',m[1] or m[2]);counts.update(re.sub('[^a-z]','',chars))
  assert counts['i']==1 and all(n==2 for a,n in counts.items() if a!='i'),(row['origin'],counts)
  assert s.endswith(r'\epsilon^i') and r'\epsilon^j' not in s
  assert s in new;number+=1
assert number==472
checks['dummy_indices_and_display_coverage']={'status':'PASS','new_terms':number,'six_original_origins':list(j['blocks'])}

hand=json.loads((PHASE/'HUMAN-NOTATION-LEDGER.json').read_text());total=defaultdict(lambda:(F(0),F(0)));before=0
for block in range(1,12):
 for row in hand['blocks'][str(block)]+j['blocks'].get(str(block),[]):
  key=re.sub(r'\s+',' ',row['latex']).strip()
  total[key]=tuple(a+F(b) for a,b in zip(total[key],row['coefficient']));before+=1
total={k:v for k,v in total.items() if any(v)}
actual={r['latex']:tuple(map(F,r['coefficient'])) for r in j['summation']['rows']}
assert total==actual and before==602 and len(total)==586
final=text.split('## 28. Final Result:',1)[1].split('## 29.',1)[0]
for r in j['summation']['rows']:assert r['latex'] in final
# A printed coefficient and its physical expression must be together, not just separately present.
def coeff(c):
 r,i=map(F,c);v=r or i;sgn='-' if v<0 else '+';v=abs(v)
 n='' if v.numerator==1 else str(v.numerator)
 if i:n+='i'
 elif not n:n='1'
 if v.denominator!=1:n=r'\frac{'+n+'}{'+str(v.denominator)+'}'
 elif n=='1':n=''
 return sgn+n
for row in j['summation']['rows']:
 expected=coeff(row['coefficient'])+row['latex']
 assert expected in final or (expected.startswith('+') and expected[1:] in final)
checks['complete_explicit_addition']={'status':'PASS','before_literal_collection':before,'after_literal_collection':len(total),'original_origins':94,'zero_trace_origins':22}

# Archived-draft preservation is outside the final-paper calculation.
for token in [r'\star',r'\mathbf',r'\mathscr',r'\boldsymbol']:assert token not in part
for math in re.findall(r'\$\$([\s\S]*?)\$\$',part):
 level=0
 for char in math:level+=(char=='{')-(char=='}');assert level>=0
 assert level==0
 assert math.count(r'\begin{aligned}')==math.count(r'\end{aligned}')
 assert not re.search(r'\^\{[^{}]*\}\^',math),'Double superscript'
tags=re.findall(r'\\tag\{(H\d+[a-z]?)\}',part);assert len(tags)==len(set(tags))
checks['presentation']={'status':'PASS','no_custom_operations_or_response_fields':True,'equation_tags':len(tags)}
result={'status':'PASS_FOR_H50_AND_EXPLICIT_SUM','date':'2026-09-18','source_lock':'UNG-WEYL2-OP58-CONVENTIONS-v5','scope':'All six H50 normal-frame covariant coefficients, displayed Fierz algebra and full epsilon-right singlet addition. Covariance restoration is the hand argument H54-H55. Not independent full nonlinear SUSY closure, minimal E/N, invariant or spectrum.','checks':checks,'proof_sha256':hashlib.sha256(NOTE.read_bytes()).hexdigest(),'ledger_sha256':hashlib.sha256((PHASE/'H50-COMPLETION-LEDGER.json').read_bytes()).hexdigest()}
(PHASE/'H50-COMPLETION-CHECKS.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
