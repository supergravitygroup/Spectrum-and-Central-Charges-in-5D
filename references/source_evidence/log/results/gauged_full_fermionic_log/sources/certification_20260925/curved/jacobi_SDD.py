"""Independent finite-index S,D,D K-generator Jacobi certificate.
All numbers are Gaussian dyadic rationals: complex binary storage is exact here;
assert residual==0, no tolerance. 48 independent Weyl-fermion input basis vectors.
ASSERT_CONVENTION: metric_signature=mostly-plus, source_frame=Gold-S23-C24
"""
import sys,runpy,itertools as it,json,contextlib,io
from pathlib import Path
import numpy as np
OUT=Path(__file__).resolve().parent; BASE=OUT.parents[2]
with contextlib.redirect_stdout(io.StringIO()):n=runpy.run_path(str(BASE/'scripts/verify_log_step2.py'))
C,U,E,G,GD,SU,eta=[n[k] for k in ['C','U','E','G','GD','SU','eta']]
eps5=np.zeros((5,)*5)
for ids in it.permutations(range(5)):eps5[ids]=n['cc']['eps'](ids) # all lower
sig=SU*eta[:,None,None,None]*eta[None,:,None,None]
glo=G*eta[:,None,None]

def check(x,w3,phase=1j):
 # D_t^r W_uv = W_uvt^r + eps_t(u X_v)^r, S23(2.6a).
 dw=np.zeros((4,2,5,5),complex)
 for t,r in it.product(range(4),range(2)):
  dws=w3[:,:,t,r]+(np.outer(C[t],x[:,r])+np.outer(x[:,r],C[t]))/2
  dw[t,r]=np.einsum('abuv,uv->ab',sig,dws)
 # S_sl nabla_a W_bc = i Gamma_a_s^t eps_lr D_t^r W_bc.
 sdw=1j*np.einsum('ast,lr,trbc->slabc',glo,-E,dw)
 stilde=np.einsum('defgh,g,h,slagh->sladef',eps5,eta,eta,sdw)/2
 sddiv=np.einsum('b,c,slbbc->slc',eta,eta,sdw)
 stdiv=np.einsum('d,c,slddac->slac',eta,eta,stilde)
 sy=8j*np.einsum('lr,sr->sl',-E,x)
 # RK_{alpha beta}^{ij c} : C24(A.2d); W² terms S-primary, vanish under S.
 srk=(-.5j*np.einsum('ij,AB,slc->ABijslc',E,C,sddiv)
      +.5j*np.einsum('ij,aAB,slac->ABijslc',E,GD,stdiv)
      -1j/32*np.einsum('ij,cAB,sl->ABijslc',E,GD,sy))
 xu=U@x
 rs=.75j*np.einsum('ij,AB,tk->ABijtk',E,C,xu)
 rs+=.5j*(np.einsum('ij,At,Bk->ABijtk',E,np.eye(4),x)-np.einsum('ij,Bt,Ak->ABijtk',E,np.eye(4),x))
 # {S_sl,S_tk}=-2i eps^{lk} Gamma^c_st after lowering both SU(2) indices.
 rsss=-2j*np.einsum('ABijtk,lk,cst->ABijslc',rs,E,GD)
 xlow=np.einsum('lr,vr->vl',-E,x)
 w3a=np.einsum('abuv,uvsr,lr->absl',sig,w3,-E)
 # Candidate [S_sl,nabla_a]_K^c.
 vecK=phase*(np.einsum('ast,ctv,vl->slac',glo,G,xlow)/8-np.einsum('c,acsl->slac',eta,w3a)/4)
 tor=-2j*np.einsum('ij,aAB,slac->ABijslc',E,GD,vecK)
 residual=tor-srk+rsss
 return residual,tor,srk,rsss
rows=[]; failures=[]; support=0
bases=[('x',(s,r)) for s,r in it.product(range(4),range(2))]+[('w3',(a,b,c,r)) for a,b,c in it.combinations_with_replacement(range(4),3) for r in range(2)]
for name,ids in bases:
 x=np.zeros((4,2),complex);w3=np.zeros((4,4,4,2),complex)
 if name=='x':x[ids]=1
 else:
  for abc in set(it.permutations(ids[:3])):w3[abc+(ids[3],)]=1
 rr,tor,srk,rsss=check(x,w3)
 old,*_=check(x,w3,1)
 row={'basis':name+str(ids),'new_nonzero':int(np.count_nonzero(rr)),'new_max':float(np.max(abs(rr))),'printed_nonzero':int(np.count_nonzero(old)),'printed_max':float(np.max(abs(old)))}
 rows.append(row);support+=np.count_nonzero(tor)+np.count_nonzero(srk)+np.count_nonzero(rsss)
 if np.any(rr):failures.append(row)
report={'status':'PASS' if not failures else 'FAIL','basis_vectors':len(bases),'jacobi_components_per_basis':int(rr.size),'exact_arithmetic':'Gaussian dyadic rationals; comparisons use exact equality; all entries products/sums/divisions by powers of 2','support_terms':int(support),'rows':rows,'failures':failures}
(OUT/'jacobi-SDD-checks.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({k:v for k,v in report.items() if k not in ['rows','failures']},indent=2));print('failures',failures[:3])
