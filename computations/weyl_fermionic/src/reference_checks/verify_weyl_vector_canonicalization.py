"""Independent checks of the vector-coefficient derivation VC01--VC44.
Finite gamma matrices and independent odd generators cross-check the hand proof.
No field equation or fermion truncation is imposed.
"""
from weyl_clifford_components import *
from fractions import Fraction
from collections import Counter
BASE=Path(__file__).resolve().parents[1]
PH=BASE/'.gpd/phases/02-ozkan-map-and-variation-completion'
j=json.loads((PH/'CLIFFORD-COLLECTION-LEDGER.json').read_text())
old=[r for r in j['terms'] if any(n=='G1' for n,ix in r['factors'])]
metric=np.diag(eta)
def term(coef,fields,gi=(),ferm=()):return [str(coef),fields,['a'],list(gi),list(ferm)]
def weyl(seed):
 rng=np.random.default_rng(seed)
 r=np.einsum('n,nabcd->abcd',rng.integers(-3,4,100),cb)
 r=(r+r.transpose(2,3,0,1))/2
 r=r-(r+r.transpose(0,2,3,1)+r.transpose(0,3,1,2))/3
 ric=np.einsum('abcd,b,d,bd->ac',r,eta,eta,metric)
 scalar=np.einsum('aa,a',ric,eta)
 for a,b,c,d in it.product(rg,repeat=4):
  r[a,b,c,d]-=(metric[a,c]*ric[b,d]-metric[b,c]*ric[a,d]-metric[a,d]*ric[b,c]+metric[b,d]*ric[a,c])/3
  r[a,b,c,d]+=scalar*(metric[a,c]*metric[b,d]-metric[a,d]*metric[b,c])/12
 assert np.max(abs(np.einsum('abcd,bd->ac',r,metric)))<1e-12
 assert np.max(abs(r-r.transpose(2,3,0,1)))<1e-12
 assert np.max(abs(r+r.transpose(0,2,3,1)+r.transpose(0,3,1,2)))<1e-12
 return r



# Product-rule expansion of the independently written final t^a.
new=[canonical_to_term(old[0]),canonical_to_term(old[24])]
for coef,fields in [
 ('-2j',[('Cd1','babcd'),('T','cd')]),('-2j',[('C','abcd'),('Td1','bcd')]),
 ('32j/3',[('Dd1','b'),('T','ab')]),('32j/3',[('D',''),('Td1','bab')]),
 ('64j/9',[('Td1','bab'),('T','cd'),('T','cd')]),('128j/9',[('T','ab'),('T','cd'),('Td1','bcd')]),
 ('256j/3',[('Td1','bac'),('T','cd'),('T','bd')]),('256j/3',[('T','ac'),('Td1','bcd'),('T','bd')]),('256j/3',[('T','ac'),('T','cd'),('Td1','bbd')]),
 ('32j/3',[('E','abcde'),('Td1','bcf'),('Td1','fde')]),('32j/3',[('E','abcde'),('T','cf'),('Td2','bfde')]),
 ('16j',[('E','abcde'),('Td1','bcf'),('Td1','def')]),('16j',[('E','abcde'),('T','cf'),('Td2','bdef')])]:new.append(term(coef,fields))
new+= [
 term('1j/2',[('T','cd')],['a'],[('R',0,'ec'),('R',0,'ed')]),
 term('-3j/2',[('T','cd')],['c'],[('R',0,'ea'),('R',0,'ed')]),
 term('-8j',[('T','cd')],['d'],[('R',0,'ac'),('X',0,'')]),
 term('-8j/3',[('T','cd')],['a'],[('R',0,'cd'),('X',0,'')]),
 term('1/4',[],[],[('R',0,'cd'),('R',1,'acd')]),
 term('3/4',[],[],[('R',0,'cd'),('R',1,'cda')]),
 term('4',[],[],[('R',1,'bab'),('X',0,'')]),
 term('4',[],[],[('R',0,'ab'),('X',1,'b')]),
 term('-64/3',[],['ab'],[('X',0,''),('X',1,'b')])]

# Additional physical contractions used only inside these verification routines.
basis={
 'A':term(1,[('T','cd')],['c'],[('R',0,'ea'),('R',0,'ed')]),
 'Q':term(1,[('T','cd')],['a'],[('R',0,'ec'),('R',0,'ed')]),
 'B':term(1,[('E','acdef'),('T','cd')],[],[('R',0,'eg'),('R',0,'fg')]),
 'C':term(1,[('E','acdef'),('T','dg')],[],[('R',0,'ce'),('R',0,'fg')]),
 'X':term(1,[('T','cd')],['d'],[('R',0,'ac'),('X',0,'')]),
 'W':term(1,[('T','cd')],['a'],[('R',0,'cd'),('X',0,'')]),
 'U':term(1,[('E','acdef'),('T','cd')],['fg'],[('R',0,'eg'),('X',0,'')]),
 'V':term(1,[('E','acdef'),('T','dg')],['fg'],[('R',0,'ce'),('X',0,'')]),
 'Y':term(1,[('T','cd')],['acd'],[('R',0,'ef'),('R',0,'ef')])}
curv={f'C{n+1}':canonical_to_term(old[n]) for n in range(1,6)}
for v in curv.values():v[0]='1'
curv['L1']=term(1,[('E','acdef'),('T','cd'),('C','egfh'),('T','hg')])
curv['L2']=term(1,[('E','acdef'),('T','dg'),('C','cefh'),('T','hg')])
curv['L3']=term(1,[('E','acdef'),('T','dg'),('C','cegh'),('T','fh')])
def vector_part(m):
 if isinstance(m,int):return np.zeros((4,4),complex)
 return sum(gl[a]*np.trace(gu[a]@m)/4 for a in rg)
report={'status':'PASS','input_terms':34,'expanded_final_terms':len(new),'samples':[]}
# Exact arithmetic for each nontrivial coefficient addition.
assert 4*Fraction(1,2)+8*Fraction(1,4)-Fraction(22,3)+4*Fraction(1,2)==-Fraction(4,3)
assert Fraction(32,3)*(-Fraction(1,2))-Fraction(40,3)*(-Fraction(1,2))==Fraction(4,3)
assert -2+Fraction(5,4)*2==Fraction(1,2)
assert -3+4-Fraction(5,4)*2==-Fraction(3,2)
assert -16+Fraction(16,3)*4-Fraction(20,3)*2==-8
assert Fraction(16,3)*2-Fraction(20,3)*2==-Fraction(8,3)
assert Fraction(1,4)+Fraction(1,2)==Fraction(3,4)
report['coefficient_additions']={'status':'PASS','exact_rational_checks':7}
# Matrix products used in the bilinear reductions and dualizations.
me=0.
for a,b,c in it.product(rg,repeat=3):
 rhs=G[3][a,b,c]+metric[a,b]*gl[c]-metric[a,c]*gl[b]
 me=max(me,float(np.max(abs(gl[a]@G[2][b,c]-rhs))))
for a in rg:
 me=max(me,float(np.max(abs(sum(eta[b]*gl[b]@G[2][b,a] for b in rg)-4*gl[a]))))
for a,b,c in it.product(rg,repeat=3):
 rhs=-.5j*sum(E[a,b,c,d,e]*eta[d]*eta[e]*G[2][d,e] for d,e in it.product(rg,repeat=2))
 me=max(me,float(np.max(abs(G[3][a,b,c]-rhs))))
assert me==0
report['finite_matrix_identities']={'status':'PASS','max_error':me,'checks':'125 gamma1*gamma2 products,5 contracted products,125 rank3 dualities'}
for seed in [42,53,67,79,83,97]:
 fields,ferm=gen(seed);fields['C']=weyl(seed)
 fields['Cd1']=np.array([weyl(seed+100+k) for k in range(5)])
 C=fields['C'];T=fields['T'];R=ferm[('R',0)];X=ferm[('X',0)]
 def bil(u,g,v):
  return sum(su[i,k]*(u[0,i]@charge@g@v[1,k]-u[1,i]@charge@g@v[0,k]) for i,k in it.product(range(2),repeat=2))
 comm=np.zeros((5,)*4,complex)
 for a,b,c,d in it.product(rg,repeat=4):
  comm[a,b,c,d]=sum(eta[e]*(C[a,b,c,e]*T[e,d]+C[a,b,d,e]*T[c,e]) for e in rg)-.5j*bil(R[:,a,b],G[2][c,d],X)+3j/32*bil(R[:,a,b],I,R[:,c,d])
 fields['Td2']=(fields['Td2']+fields['Td2'].swapaxes(0,1))/2+comm/2
 os=[evaluate(canonical_to_term(r),fields,ferm) for r in old]
 ns=[evaluate(r,fields,ferm) for r in new]
 scale=max(1,sum(np.max(abs(v)) for v in os))
 errs={'all34_to_final_relative':float(np.max(abs(sum(os)-sum(ns))))/scale}
 assert errs['all34_to_final_relative']<1e-11
 for label,ii,jj in [('C_DT',range(6,11),range(2,4)),('DD',range(11,13),range(4,6)),('cubic',range(13,18),range(6,11)),('RDR',range(26,30),range(19,21)),('Dferm',range(31,34),range(21,24))]:
  lhs=sum(os[k] for k in ii);rhs=sum(ns[k] for k in jj)
  errs[label+'_relative']=float(np.max(abs(lhs-rhs)))/max(1,float(np.max(abs(lhs))),float(np.max(abs(rhs))))
 bb={k:evaluate(v,fields,ferm) for k,v in basis.items()}
 identity_errors=[bb['B']-2j*bb['Q']+4j*bb['A'],bb['C']-2j*bb['Q']+2j*bb['A'],bb['U']-2j*bb['W']-4j*bb['X'],bb['V']-2j*bb['W']-2j*bb['X'],bb['B']-.5j*bb['Y']]
 errs['five_spinor_identities_relative']=max(float(np.max(abs(e))) for e in identity_errors)/max(1,max(float(np.max(abs(b))) for b in bb.values()))
 cc={k:evaluate(v,fields,ferm) for k,v in curv.items()}
 ratios={'C2':.5,'C3':.25,'C4':0,'C5':1,'C6':.5,'L1':-.5,'L2':0,'L3':-.5}
 errs['eight_curvature_identities_relative']=max(float(np.max(abs(cc[k]-z*cc['C5']))) for k,z in ratios.items())/max(1,max(float(np.max(abs(b))) for b in cc.values()))
 assert max(errs.values())<1e-10,errs
 # Independently form the vector of each original ordered gamma word.
 if seed in [42,53]:
  raw=[];miderrs=[]
  for row in j['rows']:
   if row['rank'] in [0,2]:continue
   lhs=sum(evaluate(t,fields,ferm) for t in row['projected_input'])
   rhs=sum(evaluate(canonical_to_term(t),fields,ferm) for t in row['terms'])
   lv=vector_part(lhs);rv=vector_part(rhs)
   miderrs.append(float(np.max(abs(lv-rv)))/max(1,float(np.max(abs(lhs))),float(np.max(abs(rhs)))))
   raw.append(lv)
  errs['original_matrix_contributions']=len(raw)
  errs['largest_individual_vector_reduction_relative']=max(miderrs)
  errs['original_matrices_to_final_relative']=float(np.max(abs(sum(raw)-sum(ns))))/scale
  assert max(miderrs)<1e-10 and errs['original_matrices_to_final_relative']<1e-11
 report['samples'].append({'seed':seed,**errs})
# Explicitly check the sign and factorial in the epsilon-epsilon Schouten proof.
eeerr=0.
for a,e,f,c,d,k in it.product(rg,repeat=6):
 lhs=sum(E[a,e,f,g,h]*eta[a]*eta[e]*eta[f]*eta[g]*eta[h]*E[c,d,g,h,k] for g,h in it.product(rg,repeat=2))
 det=sum(sign(p)*int((a,e,f)[0]==(c,d,k)[p[0]])*int((a,e,f)[1]==(c,d,k)[p[1]])*int((a,e,f)[2]==(c,d,k)[p[2]]) for p in it.permutations(range(3)))
 eeerr=max(eeerr,abs(lhs+2*det))
assert eeerr==0
report['six_index_schouten_contraction']={'status':'PASS','epsilon_epsilon_cases':5**6,'max_error':eeerr}
# Paired index and Weyl-weight audit includes every product-rule summand.
for c,f,go,gi,fr in new:
 count=Counter(x for n,ix in f for x in ix)
 count.update(x for chain in go+gi for x in chain)
 count.update(x for n,d,ix in fr for x in ix)
 assert all(n==2 for n in count.values()),(c,count)
 weights={'C':2,'Cd1':3,'T':1,'D':2,'Dd1':3,'V':2,'Td1':2,'Td2':3,'E':0}
 assert sum(weights[n] for n,ix in f)+sum(1.5+d for n,d,ix in fr)==4
report['weights_and_indices']={'status':'PASS','expanded_monomials':len(new),'weight':4}
# Majorana reality matrices, as in the locked C03/SC28 convention.
B=charge@gl[0];re=0.
for n in range(3):
 for ix in it.combinations(rg,n):
  M=charge@(G[n][ix] if n else I)
  re=max(re,float(np.max(abs(B.T@M.conj()@B-(-1)**(n+1)*M))))
assert re==0
report['reality_matrices']={'status':'PASS','ranks':[0,1,2],'max_error':re}
# Source M03: strip the common i from t; multiply by 2i to compare.
tcoeff=[-Fraction(1,32),Fraction(1,24),-2,Fraction(32,3),Fraction(64,9),Fraction(256,3),Fraction(32,3),16]
source=[Fraction(1,16),-Fraction(1,12),4,-Fraction(64,3),-Fraction(128,9),-Fraction(512,3),-Fraction(64,3),-32]
assert [-2*c for c in tcoeff]==source
report['bosonic_M03_comparison']={'status':'PASS','coefficients':8,'same_derivative_order':True}
# Algebraic restrictions of VC41b, not assumed solutions.
f,fr=gen(42);f['C']=weyl(42)
fr={k:np.zeros_like(v) for k,v in fr.items()};limits=[]
for kept in [['C','V'],['T','D']]:
 fs={n:(v if n in kept or n in ['E','m'] else np.zeros_like(v)) for n,v in f.items()}
 lhs=sum(evaluate(canonical_to_term(r),fs,fr) for r in old)
 rhs=sum(evaluate(r,fs,fr) for r in new)
 expected=sum(evaluate(r,fs,fr) for r in new[:2]) if 'C' in kept else np.zeros((4,4),complex)
 err=float(max(np.max(abs(lhs-expected)),np.max(abs(rhs-expected))))/max(1,float(np.max(abs(lhs))))
 assert err<1e-11
 limits.append({'retained':kept,'relative_error':err})
report['algebraic_limits']={'status':'PASS','cases':limits}
# Extra traceful test of VC23: its RHS is Einstein-curvature times dual(T wedge T).
f,fr=gen(53)
f['C']=weyl(53)+np.einsum('ac,bd->abcd',metric,metric)-np.einsum('ad,bc->abcd',metric,metric)
f['Ric']=np.einsum('cacb,c->ab',f['C'],eta);f['scal']=np.einsum('aa,a',f['Ric'],eta)
lhs=evaluate(curv['C5'],f,fr)-2*evaluate(curv['C6'],f,fr)
rhs=evaluate(term(-1,[('Ric','ak'),('E','klmnp'),('T','lm'),('T','np')]),f,fr)+evaluate(term('1/2',[('scal',''),('E','almnp'),('T','lm'),('T','np')]),f,fr)
e=float(np.max(abs(lhs-rhs)))/max(1,float(np.max(abs(lhs))))
assert e<1e-11
report['traceful_Schouten_sign_check']={'status':'PASS','relative_error':e}
report['scope']='Exact canonicalization relative to v5/M08/M12. Full ordered derivatives and fermionic commutator retained; no EOM, IBP, physical-fermion truncation or nonlinear closure claim.'
(PH/'VECTOR-CANONICALIZATION-CHECKS.json').write_text(json.dumps(report,indent=2)+'\n')
(PH/'VECTOR-CANONICALIZATION-LEDGER.json').write_text(json.dumps({'original_terms':old,'expanded_final_terms':new,'scope':report['scope']},indent=2)+'\n')
print(json.dumps(report,indent=2))
