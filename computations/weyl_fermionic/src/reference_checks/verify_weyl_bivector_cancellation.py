"""Independent component checks of the hand proof B01--B36; no EOM.

Run with NumPy available. Two odd generators retain the antisymmetric
polarization of every fermion bilinear; coefficients are not commuting
spinors. Random tensor tests are cross-checks, not the analytic proof.
"""
from weyl_clifford_components import *
ROOT=Path(__file__).resolve().parents[1]
PH=ROOT/'.gpd/phases/02-ozkan-map-and-variation-completion'
ledger=json.loads((PH/'CLIFFORD-COLLECTION-LEDGER.json').read_text())
rows=[r for r in ledger['terms'] if any(n=='G2' for n,ix in r['factors'])]
assert len(rows)==29
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

def dc_contractions(B,T):
 p=np.einsum('abcfg,de,cfgde,c,f,g,d,e->ab',E,T,B,eta,eta,eta,eta,eta,optimize=True)/3
 q=np.einsum('abefg,dg,cefcd,e,f,g,d,c->ab',E,T,B,eta,eta,eta,eta,eta,optimize=True)
 return p,q

def matrix(k):return sum(eta[a]*eta[b]*k[a,b]*G[2][a,b] for a,b in it.product(rg,repeat=2))
report={'status':'PASS','input_terms':29,'source_lock':'UNG-WEYL2-OP58-CONVENTIONS-v5','samples':[]}
for seed in [42,53,67,79,83,97]:
 fields,ferm=gen(seed);fields['C']=weyl(seed);fields['Cd1']*=0
 R=ferm[('R',0)];X=ferm[('X',0)];T=fields['T'];C=fields['C']
 def bil(u,g,v):return sum(su[i,k]*(u[0,i]@charge@g@v[1,k]-u[1,i]@charge@g@v[0,k]) for i,k in it.product(range(2),repeat=2))
 comm=np.zeros((5,)*4,complex)
 for a,b,c,d in it.product(rg,repeat=4):
  comm[a,b,c,d]=sum(eta[e]*(C[a,b,c,e]*T[e,d]+C[a,b,d,e]*T[c,e]) for e in rg)-.5j*bil(R[:,a,b],G[2][c,d],X)+3j/32*bil(R[:,a,b],I,R[:,c,d])
 # Keep arbitrary symmetric second derivative jets in addition to the
 # curvature-fixed antisymmetric derivatives.
 fields['Td2']=(fields['Td2']+fields['Td2'].swapaxes(0,1))/2+comm/2
 BR=np.zeros((5,)*5,complex);BX=BR.copy();BK=BR.copy()
 F=np.random.default_rng(seed+1000).integers(-3,4,(5,5,5)).astype(complex)
 F-=F.swapaxes(0,1).copy();ft=np.einsum('abb,b->a',F,eta)
 for a,b,c in it.product(rg,repeat=3):F[a,b,c]-=(metric[b,c]*ft[a]-metric[a,c]*ft[b])/4
 for a,b,c,d,e in it.product(rg,repeat=5):
  for u,v,w in [(a,b,c),(b,c,a),(c,a,b)]:
   BR[a,b,c,d,e]+=(bil(R[:,u,v],gl[d],R[:,w,e])-bil(R[:,u,v],gl[e],R[:,w,d])+bil(R[:,u,v],gl[w],R[:,d,e]))/4
   BX[a,b,c,d,e]+=2*(metric[w,d]*bil(R[:,u,v],gl[e],X)-metric[w,e]*bil(R[:,u,v],gl[d],X))
   BK[a,b,c,d,e]+=2*(F[u,v,d]*metric[w,e]-F[u,v,e]*metric[w,d])
 parts={key:dc_contractions(B,T) for key,B in [('RR',BR),('Rchi',BX),('RK',BK)]}
 # Independent spinor identities B05 and B19--B24.
 dualerr=0
 for mode,sui in it.product(range(2),repeat=2):
  r=R[mode,:,:,sui,:]
  lhs=np.einsum('abcde,des,d,e->abcs',E,r,eta,eta)
  rhs=np.array([[[2j*(gl[a]@r[b,c]+gl[b]@r[c,a]+gl[c]@r[a,b]) for c in rg] for b in rg] for a in rg])
  dualerr=max(dualerr,float(np.max(abs(lhs-rhs))))
 A=np.zeros((5,5),complex);Q=A.copy();U=A.copy();chi=A.copy();RR2=A.copy()
 for a,b,c,d in it.product(rg,repeat=4):
  A[a,b]+=eta[c]*eta[d]*T[c,d]*bil(R[:,a,b],I,R[:,c,d])
  Q[a,b]+=eta[c]*eta[d]*(bil(R[:,c,a],I,R[:,c,d])*T[d,b]-bil(R[:,c,b],I,R[:,c,d])*T[d,a])/2
  RR2[a,b]+=eta[c]*eta[d]*bil(R[:,c,d],G[2][a,b],R[:,c,d])
  chi[a,b]+=eta[c]*eta[d]*T[c,d]*(bil(R[:,a,b],G[2][c,d],X)-2*bil(R[:,a,c],G[2][b,d],X)+2*bil(R[:,b,c],G[2][a,d],X)+bil(R[:,c,d],G[2][a,b],X))
  for e in rg:U[a,b]+=eta[c]*eta[d]*eta[e]*T[d,e]*(bil(R[:,c,a],G[2][b,d],R[:,c,e])-bil(R[:,c,b],G[2][a,d],R[:,c,e]))/2
 q2=np.array([[sum(eta[c]*bil(R[:,c,a],I,R[:,c,b]) for c in rg) for b in rg] for a in rg])
 evaluated=[evaluate(canonical_to_term(r),fields,ferm) for r in rows]
 rest=sum(evaluated);dc=sum(matrix(p+q) for p,q in parts.values());scale=max(1,float(sum(np.max(abs(x)) for x in evaluated)))
 L=np.zeros((5,)*4,complex)
 for a,b,c,d in it.product(rg,repeat=4):L[a,b,c,d]=sum(eta[e]*(C[a,b,c,e]*T[e,d]+C[a,b,d,e]*T[c,e]) for e in rg)
 AA=np.zeros((5,5),complex);vs=[AA.copy() for _ in range(5)]
 for a,b,c,d in it.product(rg,repeat=4):
  z=eta[c]*eta[d]
  vs[0][a,b]+=z*(T[a,c]*L[b,d,c,d]-T[b,c]*L[a,d,c,d])/2
  vs[1][a,b]+=z*(T[a,c]*L[d,c,b,d]-T[b,c]*L[d,c,a,d])/2
  vs[2][a,b]+=z*T[c,d]*(L[c,a,b,d]-L[c,b,a,d])/2
  vs[3][a,b]+=z*T[c,d]*L[c,d,a,b]
  vs[4][a,b]+=z*T[c,d]*L[a,b,c,d]
  for e in rg:AA[a,b]+=eta[c]*eta[d]*eta[e]*(C[a,c,d,e]*T[c,b]-C[b,c,d,e]*T[c,a])*T[d,e]/2
 b16errors=[float(np.max(abs(v-z*AA))) for v,z in zip(vs,[-.5,-.5,-.5,2,0])]
 Ffirst=np.zeros((5,5),complex);Xfirst=Ffirst.copy()
 for a,b,c,d,e in it.product(rg,repeat=5):
  for ff in rg:
   Ffirst[a,b]+=-4*E[a,b,c,d,e]*eta[c]*eta[d]*eta[e]*eta[ff]*F[c,d,ff]*T[e,ff]
   Xfirst[a,b]+=-4*E[c,d,a,b,e]*eta[c]*eta[d]*eta[e]*eta[ff]*T[ff,e]*bil(R[:,c,d],gl[ff],X)
 intermediate_errors={"B16_each_row_absolute":max(b16errors),"B29_RK_first_absolute":float(np.max(abs(Ffirst-parts["RK"][0]))),"B29_Rchi_first_absolute":float(np.max(abs(Xfirst-parts["Rchi"][0])))}
 errors={
  **intermediate_errors,
  'full_29_terms_relative':float(np.max(abs(rest+dc)))/scale,
  'B05_absolute':dualerr,
  'B20_absolute':float(np.max(abs(chi))),
  'B22_absolute':float(np.max(abs(RR2-4*q2))),
  'B24_absolute':float(np.max(abs(A+2*U))),
  'B30_absolute':float(np.max(abs(parts['RR'][0]-(1.5j*A-2j*Q)))),
  'B35_absolute':float(np.max(abs(parts['RR'][1]-(-1.5j*A+2j*Q)))),
  'B27_double_trace_absolute':float(np.max(abs(np.einsum('abcde,bd,ce->a',BR+BX,metric,metric)))),
  **{f'B29_{key}_absolute':float(np.max(abs(p+q))) for key,(p,q) in parts.items()}}
 assert errors['full_29_terms_relative']<1e-11,errors
 assert max(v for k,v in errors.items() if k!='full_29_terms_relative')<1e-8,errors
 report['samples'].append({'seed':seed,**errors})
report['scope']='Independent component checks; analytic proof is DERIVATION-bivector-cancellation.md B01--B36. No EOM or fermion truncation.'
(PH/'BIVECTOR-CANCELLATION-CHECKS.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'status':report['status'],'samples':len(report['samples']),'max_relative_error':max(r['full_29_terms_relative'] for r in report['samples']),'max_absolute_identity_error':max(v for r in report['samples'] for k,v in r.items() if k not in ['seed','full_29_terms_relative'])},indent=2))
