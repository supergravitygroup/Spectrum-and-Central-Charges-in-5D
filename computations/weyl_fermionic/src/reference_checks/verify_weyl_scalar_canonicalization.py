"""Independent finite gamma/Grassmann checks of scalar canonicalization SC01--SC36.
Run with NumPy available. These checks support the displayed hand derivation.
"""
from weyl_clifford_components import *
from fractions import Fraction
BASE=Path(__file__).resolve().parents[1]
PH=BASE/'.gpd/phases/02-ozkan-map-and-variation-completion'
j=json.loads((PH/'CLIFFORD-COLLECTION-LEDGER.json').read_text())
old=[r for r in j['terms'] if not any(n.startswith('G') for n,ix in r['factors'])]
metric=np.diag(eta)
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


# Explicit independent canonical expression. Spinor suffix 1 is one full derivative.
new=[
 ['1/16',[('C','abcd'),('C','abcd')],[],[],[]],
 ['32/3',[('D2','')],[],[],[]],
 ['512/9',[('D',''),('T','ab'),('T','ab')],[],[],[]],
 ['-8/3',[('C','abcd'),('T','ab'),('T','cd')],[],[],[]],
 ['-1/6',[('V','ab'),('V','ab')],[],[],[]],
 ['-32/3',[('Td1','abc'),('Td1','abc')],[],[],[]],
 ['32/3',[('Td1','bac'),('Td1','abc')],[],[],[]],
 ['-64/3',[('T','ab'),('Td2','bcac')],[],[],[]],
 ['-64/3',[('E','abcde'),('T','ab'),('T','cd'),('Td1','fef')],[],[],[]],
 ['512',[('T','ab'),('T','bc'),('T','cd'),('T','da')],[],[],[]],
 ['-1408/27',[('T','ab'),('T','ab'),('T','cd'),('T','cd')],[],[],[]],
 ['3/8',[],[],['c'],[('R',0,'ab'),('R',1,'cab')]],
 ['-1j',[('T','ab')],[],[],[('R',0,'ca'),('R',0,'cb')]],
 ['-80j/3',[('T','ab')],[],[],[('R',0,'ab'),('X',0,'')]],
 ['-128/3',[],[],['a'],[('X',0,''),('X',1,'a')]]]
report={'status':'PASS','input_terms':22,'canonical_terms':15,'samples':[]}
# All contributions to the22 starting coefficients must add exactly.
def rational(z):
 z=z.replace('*I','').replace('I','1')
 return Fraction(z)
for row in old:
 assert sum((rational(c[-1]) for c in row['contributions']),Fraction())==rational(row['coefficient'])
assert Fraction(-52,3)+8*Fraction(1,2)+Fraction(64,3)*Fraction(1,2)==Fraction(-8,3)
assert Fraction(113,16)-Fraction(97,64)*4-Fraction(64,3)*Fraction(3,32)==-1
assert Fraction(-112,3)+Fraction(64,3)*Fraction(1,2)==Fraction(-80,3)
report['exact_coefficient_additions']={'status':'PASS','starting_coefficients':22,'modified_coefficients':3}
# Finite4x4 matrix checks: Clifford products, scalar traces and SM reality.
B=charge@gl[0];gammaerr=0.;realityerr=0.
for a,b,c,d in it.product(rg,repeat=4):
 rhs=G[4][a,b,c,d]+metric[b,c]*G[2][a,d]-metric[a,c]*G[2][b,d]-metric[b,d]*G[2][a,c]+metric[a,d]*G[2][b,c]+(metric[a,d]*metric[b,c]-metric[a,c]*metric[b,d])*I
 gammaerr=max(gammaerr,float(np.max(abs(G[2][a,b]@G[2][c,d]-rhs))))
 assert abs(np.trace(G[2][a,b]@G[2][c,d])/4-(metric[a,d]*metric[b,c]-metric[a,c]*metric[b,d]))==0
for n in range(3):
 for ix in it.combinations(rg,n):
  M=charge@(G[n][ix] if n else I)
  realityerr=max(realityerr,float(np.max(abs(B.T@M.conj()@B-(-1)**(n+1)*M))))
assert gammaerr==realityerr==0
report['finite_matrix_identities']={'status':'PASS','two_bivector_products':625,'max_error':gammaerr,'reality_basis_ranks':[0,1,2],'reality_max_error':realityerr}
for seed in [42,53,67,79,83,97]:
 fields,ferm=gen(seed);fields['C']=weyl(seed);C=fields['C'];T=fields['T'];R=ferm[('R',0)];X=ferm[('X',0)]
 def bil(u,g,v):return sum(su[i,k]*(u[0,i]@charge@g@v[1,k]-u[1,i]@charge@g@v[0,k]) for i,k in it.product(range(2),repeat=2))
 comm=np.zeros((5,)*4,complex)
 for a,b,c,d in it.product(rg,repeat=4):
  comm[a,b,c,d]=sum(eta[e]*(C[a,b,c,e]*T[e,d]+C[a,b,d,e]*T[c,e]) for e in rg)-.5j*bil(R[:,a,b],G[2][c,d],X)+3j/32*bil(R[:,a,b],I,R[:,c,d])
 fields['Td2']=(fields['Td2']+fields['Td2'].swapaxes(0,1))/2+comm/2
 os=[evaluate(canonical_to_term(r),fields,ferm) for r in old];ns=[evaluate(r,fields,ferm) for r in new]
 scale=max(1,sum(np.max(abs(v)) for v in os))

 residual=float(np.max(abs(sum(os)-sum(ns))))/scale
 assert residual<1e-11
 # Check the intermediate identities separately; cancellation of mistakes
 # in the total is insufficient.
 ce=np.einsum('abcd,ab,cd,a,b,c,d',C,T,T,eta,eta,eta,eta)
 cx=np.einsum('abcd,ac,bd,a,b,c,d',C,T,T,eta,eta,eta,eta)
 rr=sum(eta[a]*eta[b]*eta[c]*T[a,b]*bil(R[:,c,a],I,R[:,c,b]) for a,b,c in it.product(rg,repeat=3))
 rx=sum(eta[a]*eta[b]*T[a,b]*bil(R[:,a,b],I,X) for a,b in it.product(rg,repeat=2))
 rg2=sum(eta[a]*eta[b]*eta[c]*eta[d]*T[a,b]*bil(R[:,c,d],G[2][a,b],R[:,c,d]) for a,b,c,d in it.product(rg,repeat=4))
 rcgamma=sum(eta[c]*eta[d]*eta[e]*T[c,d]*bil(R[:,e,c],G[2][d,e],X) for c,d,e in it.product(rg,repeat=3))
 cm=sum(eta[c]*eta[d]*eta[e]*T[c,d]*comm[e,c,d,e] for c,d,e in it.product(rg,repeat=3))
 errs={
  'C_cross_absolute':float(abs(cx-ce/2)),
  'RR_gamma_absolute':float(abs(rg2-4*rr)),
  'Rchi_gamma_absolute':float(abs(rcgamma+rx)),
  'contracted_commutator_absolute':float(abs(cm-(ce/2+.5j*rx-3j/32*rr))),
  'five_C_epsilon_absolute':float(max(np.max(abs(os[n])) for n in range(3,8))),
  'quartic_trace_absolute':float(np.max(abs(os[11]-ns[9]))),
  'all22_to15_relative':residual}
 assert max(v for k,v in errs.items() if 'relative' not in k)<1e-8,errs
 # Every scalar contribution before gamma multiplication is tested against
 # its displayed Part-V endpoint, and their sum against the new result.
 # This includes ordered higher-rank products, not only the22 collected terms.
 if seed in [42,53]:
  raw=[];miderrors=[];tested=0
  for row in j['rows']:
   if row['rank'] in [1,2]:continue
   lhs=sum(evaluate(t,fields,ferm) for t in row['projected_input'])
   rhs=sum(evaluate(canonical_to_term(t),fields,ferm) for t in row['terms'])
   lscalar=np.trace(lhs)/4
   rscalar=np.trace(rhs)/4 if not isinstance(rhs,int) else rhs
   mids=max(1,float(np.max(abs(lhs))),float(np.max(abs(rhs))))
   miderrors.append(float(abs(lscalar-rscalar))/mids);raw.append(lscalar);tested+=1
  assert max(miderrors)<1e-10
  rawerr=float(abs(sum(raw)-np.trace(sum(ns))/4))/scale
  assert rawerr<1e-11
  errs.update(original_matrix_trace_relative=rawerr,original_matrix_contributions=tested,largest_individual_scalar_reduction_relative=max(miderrors))
 report['samples'].append({'seed':seed,**errs})
# All15 monomials are Lorentz scalars of weight4.
for c,f,go,gi,fr in new:
 from collections import Counter
 count=Counter(x for n,ix in f for x in ix)
 count.update(x for chain in go+gi for x in chain)
 count.update(x for n,d,ix in fr for x in ix)
 assert all(n==2 for n in count.values()),(c,count)
 weights={'C':2,'T':1,'D':2,'D2':4,'V':2,'Td1':2,'Td2':3,'E':0}
 assert sum(weights[n] for n,ix in f)+sum(1.5+d for n,d,ix in fr)==4
report['weights_and_indices']={'status':'PASS','monomials':15,'weight':4}
report['scope']='Canonicalization of M11b relative to v5/M08 and M12; no EOM, IBP or fermion truncation. Not a nonlinear multiplet-closure test.'
(PH/'SCALAR-CANONICALIZATION-CHECKS.json').write_text(json.dumps(report,indent=2)+'\n')
(PH/'SCALAR-CANONICALIZATION-LEDGER.json').write_text(json.dumps({'original_terms':old,'canonical_terms':new,'scope':report['scope']},indent=2)+'\n')
print(json.dumps({'status':'PASS','input_terms':22,'canonical_terms':15,'samples':len(report['samples']),'max_relative_error':max(r['all22_to15_relative'] for r in report['samples']),'raw_matrix_samples':[r for r in report['samples'] if 'original_matrix_trace_relative' in r]},indent=2))
