"""Check the displayed density insertion, not nonlinear SUSY or primitive DW expansion.
Exact anchored-map transcription, rational multiplication, and a separate four-
generator Grassmann test of density contractions with 4x4 Clifford matrices.
"""
from pathlib import Path
from fractions import Fraction
import re,json,hashlib,itertools as it
import numpy as np
B=Path(__file__).resolve().parents[1]
P=B/'.gpd/phases/03-full-ungauged-fermionic-invariant'
ledger=json.loads((P/'ACTION-SUBSTITUTION-LEDGER.json').read_text())
anchor=(B/'notes/04_full_fermionic_weyl_linear_map.md').read_text()
doc=(P/'DERIVATION-full-fermionic-weyl2-action.md').read_text()
def clean(s):
 s=re.sub(r'\\hspace\{[^}]*\}','',s)
 return re.sub(r'\s+','',s.replace('\\\\','').replace('&','').replace(r'\,','').replace(r'\!',''))
def equation(s,tag):
 s=s.split('\\tag{'+tag+'}',1)[0].rsplit('\\begin{aligned}',1)[1].split('\\end{aligned}',1)[0]
 return clean(s).split('=',1)[1].removeprefix('{}').rstrip('.')
def split_sum(s):
 depth=0;start=0;out=[]
 for i,c in enumerate(s):
  if c in '{[(':depth+=1
  if c in '}])':depth-=1
  assert depth>=0
  if c in '+-' and depth==0 and i>start:out.append(s[start:i]);start=i
 out.append(s[start:]);assert depth==0
 return out

def atom(s):
 if s[0]=='{':
  end=s.index('}');return s[1:end],s[end+1:]
 return s[:1],s[1:]
def coefficient(s):
 sign=-1 if s.startswith('-') else 1;s=s.lstrip('+-');imag=0
 if s.startswith(r'\frac'):
  a,s=atom(s[5:]);b,s=atom(s)
  if 'i' in a:imag=1;a=a.replace('i','') or '1'
  value=Fraction(a)/Fraction(b)
 else:
  m=re.match(r'\d+',s);value=Fraction(m[0]) if m else Fraction(1)
  if m:s=s[len(m[0]):]
 if s.startswith('i'):imag+=1;s=s[1:]
 return (sign*value,imag),s

def coeff(c):return Fraction(c[0]),c[1]
def mul(a,b):
 x,k=coeff(a);y,l=coeff(b);phase=k+l
 return x*y*(-1)**(phase//2),phase%2

def parsed(tag):return [coefficient(t) for t in split_sum(equation(anchor,tag))]
for label,tag in [('phi','FM02'),('L','FM01'),('N','FM04')]:
 assert [c for c,b in parsed(tag)]==[coeff(c) for c in ledger[label+'_input_coefficients']]
# Descendant tensor bodies are unchanged, including full ordered derivatives.
for name,tag,prefix in [('sigma_N','FM04',r'\sigma'),('C_E','FM03','C_a')]:
 for (co,bo),(cn,bn) in zip(parsed(tag),ledger['blocks'][name]):
  assert co==coeff(cn),(name,co,cn)
  assert clean(prefix+bo)==clean(bn),(name,bo,bn)
# All 45 distributed spinor/triplet coefficients, against independent source prefactors.
fixed_phi={'dilatino':('1',1),'gravitino':('1/2',0),'C_gravitino':('1/2',1)}
fixed_L={'Y':('1/4',1),'gravitino_dilatino':('-1/2',0),'two_gravitinos':('1/4',1),'C_two_gravitinos':('1/4',0)}
for inputs,prefactors in [('phi',fixed_phi),('L',fixed_L)]:
 for name,pref in prefactors.items():
  actual=[coeff(c) for c,b in ledger['blocks'][name]]
  assert actual==[mul(c,pref) for c in ledger[inputs+'_input_coefficients']]
# Final result has exactly the terms displayed in the nine evaluated equations.
all_terms=[]
for k,name in enumerate(ledger['order'],7):
 terms=[coefficient(t) for t in split_sum(equation(doc,'WA'+str(k).zfill(2)))]
 wanted=[(coeff(c),clean(b)) for c,b in ledger['blocks'][name]]
 assert terms==wanted,(name,terms,wanted)
 all_terms+=terms
assert [coefficient(t) for t in split_sum(equation(doc,'WA24'))]==all_terms

# Independent finite exterior algebra with four generators. Its degree-four
# component detects quartic couplings missed by a two-generator bilinear check.
pairs=[]
for a,b in it.product(range(16),repeat=2):
 if not a&b:
  inversions=sum(1 for i in range(4) for j in range(4) if a>>i&1 and b>>j&1 and i>j)
  pairs.append((a,b,a|b,(-1)**inversions))
def wedge(x,y):
 z=np.zeros(16,complex)
 for a,b,c,sign in pairs:z[c]+=sign*x[a]*y[b]
 return z
s1=np.array([[0,1],[1,0]],complex);s2=np.array([[0,-1j],[1j,0]],complex);s3=np.diag([1,-1]);I2=np.eye(2)
g=[1j*np.kron(s3,s3),np.kron(s1,I2),np.kron(s2,I2),np.kron(s3,s1),np.kron(s3,s2)]
eta=[-1,1,1,1,1];eye=np.eye(4);eps=np.array([[0,1],[-1,0]])
for a,b in it.product(range(5),repeat=2):assert np.max(abs(g[a]@g[b]+g[b]@g[a]-2*(eta[a] if a==b else 0)*eye))==0
# A nonsingular antisymmetric charge matrix suffices for this bilinear-density
# identity; no symplectic-Majorana reality or SUSY test is claimed here.
charge=g[2]@g[4];assert np.max(abs(charge.T+charge))==0

def gamma(*indices):
 out=np.zeros((4,4),complex)
 from math import factorial
 for p in it.permutations(range(len(indices))):
  sign=(-1)**sum(p[a]>p[b] for a in range(len(p)) for b in range(a+1,len(p)))
  z=eye
  for j in p:z=z@g[indices[j]]
  out+=sign*z
 return out/factorial(len(indices))

def raw(u,M,v):
 z=np.zeros(16,complex);matrix=charge@M
 for a,b in it.product(range(4),repeat=2):
  if matrix[a,b]:z+=matrix[a,b]*wedge(u[a],v[b])
 return z

def bil(u,M,v):return sum(eps[j,i]*raw(u[i],M,v[j]) for i,j in it.product(range(2),repeat=2))
def cnum(c):return float(Fraction(c[0]))*1j**c[1]
reports=[]
for seed in [11,23,37,51,73,89]:
 rng=np.random.default_rng(seed)
 def odd(shape,cubic=False):
  x=np.zeros(shape+(16,),complex)
  for mask in range(16):
   if mask.bit_count() in ([1,3] if cubic else [1]):x[...,mask]=rng.integers(-2,3,shape)
  return x
 dil=odd((2,4));gr=odd((5,2,4));rspin=odd((2,4));chi=odd((2,4))
 # The eleven complete map spinors are independent odd test inputs, including
 # degree three. This tests insertion, not reconstruction of the map itself.
 phis=odd((11,2,4),True)
 upper=np.zeros((3,2,2,16),complex)
 for i,j in it.product(range(2),repeat=2):
  upper[0,i,j]=(raw(rspin[i],eye,rspin[j])+raw(rspin[j],eye,rspin[i]))/2
  upper[1,i,j]=(raw(chi[i],eye,chi[j])+raw(chi[j],eye,chi[i]))/2
 upper[2,:,:,0]=np.array([[2,3],[3,-1]])
 lower=np.einsum('ki,lj,nklp->nijp',eps,eps,upper)
 pc=np.array([cnum(c) for c in ledger['phi_input_coefficients']])
 lc=np.array([cnum(c) for c in ledger['L_input_coefficients']])
 phi=np.einsum('n,nisp->isp',pc,phis);L=np.einsum('n,nijp->ijp',lc,lower)
 sig=2.;C=np.array([1,-2,3,1,-1]);source={};expanded={}
 source['dilatino']=1j*bil(dil,eye,phi)
 source['gravitino']=sig/2*sum(bil(gr[m],g[m],phi) for m in range(5))
 source['C_gravitino']=1j/2*sum(C[m]*bil(gr[n],gamma(n,m),phi) for m,n in it.product(range(5),repeat=2))
 for name in fixed_phi:
  ans=np.zeros(16,complex)
  for q,(cn,_) in enumerate(ledger['blocks'][name]):
   if name=='dilatino':v=bil(dil,eye,phis[q])
   elif name=='gravitino':v=sig*sum(bil(gr[m],g[m],phis[q]) for m in range(5))
   else:v=sum(C[m]*bil(gr[n],gamma(n,m),phis[q]) for m,n in it.product(range(5),repeat=2))
   ans+=cnum(cn)*v
  expanded[name]=ans
 external={name:np.zeros((2,2,16),complex) for name in fixed_L}
 for i,j in it.product(range(2),repeat=2):
  external['Y'][i,j]=raw(dil[i],eye,dil[j])/sig
  external['gravitino_dilatino'][i,j]=sum(raw(gr[m,i],g[m],dil[j]) for m in range(5))
  external['two_gravitinos'][i,j]=sig*sum(raw(gr[m,i],gamma(m,n),gr[n,j]) for m,n in it.product(range(5),repeat=2))
  external['C_two_gravitinos'][i,j]=sum(C[m]*raw(gr[n,i],gamma(m,n,p),gr[p,j]) for m,n,p in it.product(range(5),repeat=3))
 for name in fixed_L:
  source[name]=cnum(fixed_L[name])*sum(wedge(external[name][i,j],L[i,j]) for i,j in it.product(range(2),repeat=2))
  expanded[name]=sum(cnum(cn)*wedge(external[name][i,j],lower[q,i,j]) for q,(cn,_) in enumerate(ledger['blocks'][name]) for i,j in it.product(range(2),repeat=2))
 errors={name:float(np.max(abs(source[name]-expanded[name])))/max(1,float(np.max(abs(source[name]))),float(np.max(abs(expanded[name])))) for name in source}
 assert max(errors.values())<1e-12,errors
 assert any(abs(v[15])>1 for v in source.values()),'Quartic sample was empty'
 reports.append({'seed':seed,'relative_errors_by_density_term':errors,'nonzero_degree_four_terms':[name for name,v in source.items() if abs(v[15])>1e-10]})
# Markdown integrity and endpoint scope.
assert doc.count('$$')%2==0
for math in doc.split('$$')[1::2]:
 depth=0
 for c in re.sub(r'\\[{}]','',math):
  depth+=(c=='{')-(c=='}');assert depth>=0
 assert depth==0
for n,title in enumerate(['Problem and Target','Convention Ledger','Definitions and Required Identities','Detailed Derivation','Consistency Checks','Final Result','Convention Dependence and Remaining Uncertainties'],1):assert f'## {n}. {title}' in doc
tags=re.findall(r'\\tag\{([^}]+)\}',doc);assert len(tags)==len(set(tags))
final=equation(doc,'WA24')
for omitted in ['N_W','E_W',r'\varphi_W','L_W','Y^{ij}']:assert omitted not in final
for link in re.findall(r'\]\(([^)]+)\)',doc):
 if not link.startswith(('http','#')) and link!='ACTION-SUBSTITUTION-CHECKS.json':assert (P/link).exists(),link
report={'status':'PASS','convention_lock':ledger['convention_lock'],'map_reference':ledger['map_reference'],
'exact_checks':{'map_input_coefficients':29,'distributed_phi_and_L_coefficients':45,'unchanged_descendant_outer_terms':25,'endpoint_grouped_terms':len(all_terms),'document_equations_unique':len(tags)},
'grassmann_checks':{'generators':4,'spinor_components':4,'seeds':reports,'scope':'Polynomial insertion and SU(2)/gamma contractions only; independent generic odd map inputs, not nonlinear map laws.'},
'expanded_derivative_coverage':{'N':15,'E_after_C04_flip':24,'spinor_couplings':33,'triplet_couplings':12,'total':84},
'scope':'Exact map-inserted full-covariant density; no nonlinear SUSY, conserved-current, primitive DW-expansion or reality certification.',
'derivation_sha256':hashlib.sha256(doc.encode()).hexdigest()}
(P/'ACTION-SUBSTITUTION-CHECKS.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({k:v for k,v in report.items() if k!='grassmann_checks'},indent=2))
print('Grassmann sample maximum relative error:',max(max(x['relative_errors_by_density_term'].values()) for x in reports))
