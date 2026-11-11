"""C24 A.4c: full Lorentz curvature is the image of a symmetric rank-four spinor.
Verify cyclic, trace and pair symmetry on every independent symmetric-spinor basis.
"""
import sys,runpy,json,itertools as it,contextlib,io
from pathlib import Path
import numpy as np
OUT=Path(__file__).resolve().parent;BASE=OUT.parents[2]
with contextlib.redirect_stdout(io.StringIO()):m=runpy.run_path(str(BASE/'scripts/verify_log_step2.py'))
eta,SU=m['eta'],m['SU'];sig=SU*eta[:,None,None,None]*eta[None,:,None,None]
rows=[]
for ids in it.combinations_with_replacement(range(4),4):
 T=np.zeros((4,)*4,complex)
 for perm in set(it.permutations(ids)):T[perm]=1
 R=-.25*np.einsum('abst,cdvw,stvw->abcd',sig,sig,T)
 tests={'cyclic':R+R.transpose(1,2,0,3)+R.transpose(2,0,1,3),'pair_exchange':R-R.transpose(2,3,0,1),'trace':np.einsum('a,abad->bd',eta,R)}
 assert all(np.all(z==0) for z in tests.values()),ids
 rows.append({'basis':ids,'cyclic':0,'pair_exchange':0,'trace':0})
report={'status':'PASS','symmetric_spinor_basis_vectors':len(rows),'source':'C24 A.4c; i W_abcd + 3W_(ab W_cd) is fully symmetric','scope':'Exact full superspace curvature algebra, not a bosonic approximation','rows':rows}
(OUT/'curvature-algebraic-bianchi.json').write_text(json.dumps(report,indent=2)+'\n');print(report['status'],len(rows))
