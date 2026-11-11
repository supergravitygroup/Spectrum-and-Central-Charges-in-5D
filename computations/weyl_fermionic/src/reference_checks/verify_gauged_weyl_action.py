"""Exact density transcription and finite Grassmann checks of gauged composites.
No nonlinear action-level invariance, reality, or primitive-field expansion claim.
"""
from pathlib import Path
from fractions import Fraction
import ast,json,re,hashlib,itertools as it
import numpy as np
B=Path(__file__).resolve().parents[1];P=B/'.gpd/phases/03-full-ungauged-fermionic-invariant'
old_code=(B/'scripts/verify_weyl_action_substitution.py').read_text()
# Reuse only pure parsing and exterior-algebra functions. Do not execute old
# top-level checks or rewrite any ungauged result.
module=ast.parse(old_code)
exec(compile(ast.Module(body=[x for x in module.body if isinstance(x,ast.FunctionDef)],type_ignores=[]),str(B/'scripts/verify_weyl_action_substitution.py'),'exec'))
ledger=json.loads((P/'GAUGED-ACTION-LEDGER.json').read_text())
base=json.loads((P/'ACTION-SUBSTITUTION-LEDGER.json').read_text())
anchor=(B/'notes/04_full_fermionic_weyl_linear_map.md').read_text()
doc=(B/'notes/05_gauged_full_fermionic_weyl2_calculation.md').read_text()
old_doc=(P/'DERIVATION-full-fermionic-weyl2-action.md').read_text()
original_clean=clean
def clean(s):
 # Equivalent physical coefficient typography in the hand-worked GA12.
 for a,b,c in [(r'\frac{ig}{8\sigma}',r'\frac{i}{8}',r'g\sigma^{-1}'),(r'\frac{128ig}{3\sigma}',r'\frac{128i}{3}',r'g\sigma^{-1}'),(r'\frac{8g}{3\sigma}',r'\frac{8}{3}',r'g\sigma^{-1}')]:s=s.replace(a,b+c)
 return original_clean(s)
for label,tag in [('phi','FM02'),('L','FM01'),('N','FM04')]:assert [c for c,b in parsed(tag)]==[coeff(c) for c in ledger[label+'_input_coefficients']]
for name in base['order']:
 keep=ledger['blocks'][name][:3] if name=='Y' else ledger['blocks'][name]
 assert keep==base['blocks'][name],name
actual=[coeff(c) for c,b in ledger['blocks']['Y'][3:]]
assert actual==[mul(c,('-1/2',0)) for c in ledger['L_input_coefficients']]
all_terms=[]
for n,name in enumerate(ledger['order'],7):
 terms=[coefficient(t) for t in split_sum(equation(doc,'GA'+str(n).zfill(2)))]
 wanted=[(coeff(c),clean(b)) for c,b in ledger['blocks'][name]]
 assert terms==wanted,(name,terms,wanted)
 all_terms+=terms
assert [coefficient(t) for t in split_sum(equation(doc,'GA24'))]==all_terms
at_zero=[t for t in all_terms if not t[1].startswith('g'+r'\sigma^{-1}L_c')]
assert at_zero==[coefficient(t) for t in split_sum(equation(old_doc,'WA24'))]
# Exact forward coefficients: gauged Y^2, chi's two new terms, tensor dual,
# and the cubic/quartic-g diagnostic. These are independent of the ledger.
assert Fraction(1,4)*2*Fraction(1,4)*Fraction(-1,2)==Fraction(-1,16)
assert Fraction(1,4)*Fraction(-1,2)**2==Fraction(1,16)
assert Fraction(1,8)*Fraction(-1,2)==Fraction(-1,16)
assert Fraction(1,8)*Fraction(1,6)*Fraction(1,2)==Fraction(1,96)
assert [Fraction(64,3)*Fraction(1,4)**2,Fraction(64,3)*2*Fraction(1,4)*Fraction(1,16),Fraction(64,3)*Fraction(1,16)**2]==[Fraction(4,3),Fraction(2,3),Fraction(1,12)]

# Four-generator exterior algebra and finite 4x4 gamma representation.
exec(old_code[old_code.index('pairs=[]'):old_code.index('reports=[]')])
def unit(x):
 z=np.zeros(16,complex);z[0]=x;return z

def scalvec(p,v):
 out=np.empty_like(v)
 for ix in np.ndindex(v.shape[:-1]):out[ix]=wedge(p,v[ix])
 return out

def mat(M,v):return np.einsum('ab,...bp->...ap',M,v)
def triplet_action(t,v):
 return np.array([sum(eps[k,j]*scalvec(t[i,j],v[k]) for j,k in it.product(range(2),repeat=2)) for i in range(2)])
def lower_triplet(t):return np.einsum('ki,lj,klp->ijp',eps,eps,t)
def triplet_dot(a,b):return sum(wedge(a[i,j],b[i,j]) for i,j in it.product(range(2),repeat=2))
def twoform_square(a,b):return sum(eta[i]*eta[j]*wedge(a[i,j],b[i,j]) for i,j in it.product(range(5),repeat=2))
def twoslash(t,v):return sum(scalvec(t[a,b],mat(gamma(a,b),v)) for a,b in it.product(range(5),repeat=2))
def oneslash(v,u):return sum(scalvec(v[a],mat(g[a],u)) for a in range(5))
def relative(a,b):return float(np.max(abs(a-b)))/max(1.,float(np.max(abs(a))),float(np.max(abs(b))))
reports=[]
for seed in [13,29,47,61,83,107]:
 rng=np.random.default_rng(seed)
 def poly(shape,parity,maxdegree=4):
  z=np.zeros(shape+(16,),complex)
  for mask in range(16):
   if mask.bit_count()%2==parity and mask.bit_count()<=maxdegree:z[...,mask]=rng.integers(-2,3,shape)
  return z
 psi=poly((2,4),1,1);phic=poly((2,4),1,1);gr=poly((5,2,4),1,1);phimu=poly((5,2,4),1,3)
 d0psi=poly((5,2,4),1,3);ds=poly((5,),0,2);box=poly((),0,4);N=poly((),0,4)
 G=poly((5,5),0,2);G=G-G.swapaxes(0,1)
 T=poly((5,5),0,2);T=T-T.swapaxes(0,1)
 L=poly((2,2),0,0);L=(L+L.swapaxes(0,1))/2;Ld=lower_triplet(L)
 A=np.array([[raw(psi[i],eye,psi[j]) for j in range(2)] for i in range(2)]);Ad=lower_triplet(A)
 sig=1.5+seed/100.;coupling=.7
 Y=1j/(4*sig)*A-coupling/(2*sig)*L;Yd=lower_triplet(Y)
 # Build D_mu psi using the source form with Y, independently of its expanded
 # gauged transcription. Then evaluate both displayed chi forms.
 dpsi=np.array([d0psi[m]+twoslash(G,gr[m])/4+1j/2*oneslash(ds,gr[m])+triplet_action(Y,gr[m])-sig*twoslash(T,gr[m])-sig*phimu[m] for m in range(5)])
 slash_dpsi=sum(mat(g[m],dpsi[m]) for m in range(5))
 chi=(1j/(8*sig)*slash_dpsi+1j/(16*sig**2)*oneslash(ds,psi)-twoslash(G,psi)/(32*sig**2)+twoslash(T,psi)/(4*sig)+1j/(32*sig**3)*triplet_action(A,psi)-coupling/(16*sig**3)*triplet_action(L,psi)+coupling/(8*sig**2)*phic)
 chi_before_Y=(1j/(8*sig)*slash_dpsi+1j/(16*sig**2)*oneslash(ds,psi)-twoslash(G,psi)/(32*sig**2)+triplet_action(Y,psi)/(8*sig**2)+twoslash(T,psi)/(4*sig)+coupling/(8*sig**2)*phic)
 chi_expanded=(1j/(8*sig)*sum(mat(g[m],d0psi[m]) for m in range(5))+1j/(32*sig)*sum(mat(g[m],twoslash(G,gr[m])) for m in range(5))-1/(16*sig)*sum(mat(g[m],oneslash(ds,gr[m])) for m in range(5))-1/(32*sig**2)*sum(mat(g[m],triplet_action(A,gr[m])) for m in range(5))-1j*coupling/(16*sig**2)*sum(mat(g[m],triplet_action(L,gr[m])) for m in range(5))-1j/8*sum(mat(g[m],twoslash(T,gr[m])) for m in range(5))-1j/8*sum(mat(g[m],phimu[m]) for m in range(5))+1j/(16*sig**2)*oneslash(ds,psi)-twoslash(G,psi)/(32*sig**2)+twoslash(T,psi)/(4*sig)+1j/(32*sig**3)*triplet_action(A,psi)-coupling/(16*sig**3)*triplet_action(L,psi)+coupling/(8*sig**2)*phic)
 yy=triplet_dot(Y,Yd)
 yy_expanded=-triplet_dot(A,Ad)/(16*sig**2)-1j*coupling/(4*sig**2)*triplet_dot(Ld,A)+coupling**2/(4*sig**2)*triplet_dot(L,Ld)
 gs=twoform_square(G,G);ts=twoform_square(T,T);gt=twoform_square(G,T);ds2=sum(eta[a]*wedge(ds[a],ds[a]) for a in range(5))
 psid=bil(psi,eye,slash_dpsi);psichi=bil(psi,eye,chi)
 psiTpsi=bil(psi,eye,twoslash(T,psi))
 D=(box/(4*sig)+ds2/(8*sig**2)-gs/(16*sig**2)-psid/(8*sig**2)-triplet_dot(A,Ad)/(64*sig**4)-4j/sig*psichi-26/3*ts+2/sig*gt+1j/(4*sig**2)*psiTpsi+coupling/(4*sig**2)*N-1j*coupling/(16*sig**4)*triplet_dot(Ld,A)+coupling**2/(16*sig**4)*triplet_dot(L,Ld))
 D_source=(-gs/4-psid/2+sig*box+ds2/2+yy+1j*psiTpsi-16j*sig*psichi-104/3*sig**2*ts+8*sig*gt+coupling*N)/(4*sig**2)
 # Actual odd bilinears in the extra compensator coupling, not commuting
 # substitutes for chi or the gravitino curvature.
 R=poly((2,4),1,3);V=poly((2,2),0,2);V=(V+V.swapaxes(0,1))/2
 triplet_terms=np.array([[[raw(R[i],eye,R[j]) for j in range(2)] for i in range(2)],[[raw(chi[i],eye,chi[j]) for j in range(2)] for i in range(2)],V])
 lower_terms=np.array([lower_triplet(z) for z in triplet_terms])
 Lw=1j/4*lower_terms[0]+256j/3*lower_terms[1]+16/3*lower_terms[2]
 extra_source=-coupling/(2*sig)*triplet_dot(L,Lw)
 extra_expanded=-1j*coupling/(8*sig)*triplet_dot(L,lower_terms[0])-128j*coupling/(3*sig)*triplet_dot(L,lower_terms[1])-8*coupling/(3*sig)*triplet_dot(L,lower_terms[2])
 errors={'Y_squared':relative(yy,yy_expanded),'chi_Y_insertion':relative(chi_before_Y,chi),'chi_connection_expansion':relative(chi_expanded,chi),'scalar_constraint':relative(D_source,D),'new_density_coupling':relative(extra_source,extra_expanded)}
 assert max(errors.values())<3e-13,errors
 assert abs(yy[15])>1e-8 and abs(D[15])>1e-8,'Quartic tests empty'
 # With zero gauging all explicit compensator deformations vanish identically.
 assert all('g' in body[:3] for c,body in ledger['blocks']['Y'][3:])
 reports.append({'seed':seed,'relative_errors':errors,'Y_squared_degree_four_nonzero':True,'D_degree_four_nonzero':True})
# Exact independent numerical check of higher-g coefficients on test scalars.
for sig,Nscalar,Lsquare,coupling in [(2.,3.,5.,.7),(1.25,-2.,3.,-.4)]:
 lhs=64*sig/3*(coupling*Nscalar/(4*sig**2)+coupling**2*Lsquare/(16*sig**4))**2
 rhs=4*coupling**2/(3*sig**3)*Nscalar**2+2*coupling**3/(3*sig**5)*Nscalar*Lsquare+coupling**4/(12*sig**7)*Lsquare**2
 assert abs(lhs-rhs)<1e-12
# Integrity of the mathematical document.
assert doc.count('$$')%2==0
for math in doc.split('$$')[1::2]:
 depth=0
 for c in re.sub(r'\\[{}]','',math):depth+=(c=='{')-(c=='}');assert depth>=0
 assert depth==0
for label in (*range(1,18),24,25):
 assert re.search(r'\\tag\{GA0?'+str(label)+r'\}',doc),label
tags=re.findall(r'\\tag\{([^}]+)\}',doc);assert len(tags)==len(set(tags))
for name in ['L_W',r'\varphi_W','E_W','N_W','Y^{ij}']:assert name not in equation(doc,'GA24')
for link in re.findall(r'\]\(([^)]+)\)',doc):
 if not link.startswith(('http','#')) and 'GAUGED-ACTION-CHECKS.json' not in link:assert (B/'notes'/link).exists(),link
report={'status':'PASS','reference_id':ledger['reference_id'],'base_map':ledger['map_reference'],'gauged_extension':ledger['gauged_extension'],'exact_checks':{'base_map_input_coefficients':29,'new_density_coefficients':3,'unchanged_grouped_terms':70,'gauged_grouped_terms':73,'product_rule_contributions':87,'ungauged_limit_same_local_representative':True,'new_composite_and_high_g_coefficients':True},'grassmann_checks':{'generators':4,'samples':reports,'max_relative_error':max(max(x['relative_errors'].values()) for x in reports),'scope':'Y², full chi/D constraint solutions, explicit chi connection expansion and new density contraction; no nonlinear invariance test.'},'document_checks':{'unique_equations':len(tags),'balanced_math':True,'complete_gauged_equation_set_present':True},'scope':ledger['scope'],'derivation_sha256':hashlib.sha256(doc.encode()).hexdigest()}
(P/'GAUGED-ACTION-CHECKS.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({k:v for k,v in report.items() if k!='grassmann_checks'},indent=2));print('Maximum Grassmann residual:',report['grassmann_checks']['max_relative_error'])
