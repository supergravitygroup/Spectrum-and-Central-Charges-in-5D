#!/usr/bin/env python3
"""Verify the individual contraction tables in the W^-2 hand derivation.

All expected rational coefficients are written in STEP_02_LOG_PRIMARY.md.
No fitting or least-squares operations are used in this check.
"""
import runpy,json,hashlib
from pathlib import Path
HERE=Path(__file__).resolve().parent
ns=runpy.run_path(str(HERE/'verify_log_step2_w2.py'))
globals().update({k:v for k,v in ns.items() if not k.startswith('__')})
def build(w):
 ws=twoform(w)
 rd=[{} for n in range(6)];rw=[{} for n in range(3)]
 for a,b,r in it.product(range(4),repeat=3):
  rd[0][a,b,r]=add(*[scale(1j*GD[m,a,b],dl[m][r][0]) for m in range(5)])
  rd[1][a,b,r]=add(*[scale(1j*GD[m,a,r],dl[m][b][0]) for m in range(5)])
  rd[2][a,b,r]=add(*[scale(1j*C[a,b]*G[m,r,t],dl[m][t][0]) for m,t in it.product(range(5),range(4))])
  rd[3][a,b,r]=add(*[scale(1j*C[a,r]*G[m,b,t],dl[m][t][0]) for m,t in it.product(range(5),range(4))])
  rd[4][a,b,r]=add(*[scale(-1j*C[b,r]*G[m,a,t],dl[m][t][0]) for m,t in it.product(range(5),range(4))])
  rd[5][a,b,r]=add(*[scale(-1j*GD[m,b,r],dl[m][a][0]) for m in range(5)])
  rw[0][a,b,r]=scale(1j*ws[b,r],ll[a][0]);rw[1][a,b,r]=scale(-1j*ws[a,r],ll[b][0]);rw[2][a,b,r]=add(*[scale(-3j*C[a,b]*ws[r,t],lu[t][0]) for t in range(4)])
 def plus(R):return {k:add(*[r[k] for r in R]) for k in R[0]}
 def contract(A,B):return add(*[scale(-1j/128*eps4(a,b,c,d)*U[r,s],prod(A[a,b,r],B[c,d,s])) for a,b,c,d in it.permutations(range(4)) for r,s in it.product(range(4),repeat=2)])
 kin=add(*[scale(1j*eta[a],prod(dlu[a][r][0],dl[a][r][0])) for a,r in it.product(range(5),range(4))]);sig=add(*[scale(1j*SU[a,b,r,s],prod(dl[a][r][0],dl[b][s][0])) for a,b,r,s in it.product(range(5),range(5),range(4),range(4))])
 epsdl=add(*[scale(1j*eps5((a,b,c,d,e))*eta[a]*eta[b]*SU[a,b,r,s]*w[d,e],prod(ll[r][0],dl[c][s][0])) for a,b,c,d,e in it.permutations(range(5)) for r,s in it.product(range(4),repeat=2)])
 vecdl=add(*[scale(1j*GU[a,r,s]*w[a,b]*eta[b],prod(ll[r][0],dl[b][s][0])) for a,b,r,s in it.product(range(5),range(5),range(4),range(4))])
 w2=sum(eta[a]*eta[b]*w[a,b]**2 for a,b in it.product(range(5),repeat=2));sc=scale(1j*w2,bil(0,0));ev=add(*[scale(1j*eps5((a,b,c,d,e))*eta[a]*GU[a,r,s]*w[b,c]*w[d,e],prod(ll[r][0],ll[s][0])) for a,b,c,d,e in it.permutations(range(5)) for r,s in it.product(range(4),repeat=2)])
 return rd,rw,kin,sig,epsdl,vecdl,sc,ev,contract,plus
def ddrows(w,dw,z,Y):
 ws=twoform(w);wm=-ws@U;dws=np.array([twoform(dw[a]) for a in range(5)]);rs=RSkernel(w,dw,z);dx=dxweyl(w,dw,z,Y);T=np.array([(3*eta[a]*G[a]@wm-wm@(eta[a]*G[a]))/4 for a in range(5)])
 out=np.zeros((5,4,4),complex)
 for al,be in it.product(range(4),repeat=2):
  out[0,al,be]=-4j*sum(G[a,be,r]*dws[a,al,r] for a,r in it.product(range(5),range(4)))
  out[1,al,be]=-4j*sum(G[a,be,r]*(T[a]@ws)[al,r] for a,r in it.product(range(5),range(4)))
  out[2,al,be]=4*sum(G[a,be,r]*(rs[a]@C)[al,r] for a,r in it.product(range(5),range(4)))
  out[3,al,be]=2j*sum(ws[be,r]*U[r,s]*ws[al,s] for r,s in it.product(range(4),repeat=2))
  out[4,al,be]=-1.5*dx[al,be]
 return out

def main():
 count=0
 for n,ab in enumerate(pairs5):
  for cd in pairs5[n:]:
   w=zero();w[ab]=w[cd]=1;w[ab[::-1]]=w[cd[::-1]]=-1
   rd,rw,kin,sig,epsdl,vecdl,sc,ev,contract,plus=build(w)
   for r,(a,b) in zip(rd,[(-1/16,-1/8),(-3/32,1/16),(1/16,-1/8),(-1/32,1/16),(-1/32,1/16),(-3/32,1/16)]):
    assert contract(r,plus(rd))==add(scale(a,kin),scale(b,sig));count+=1
   for r,(a,b) in zip(rd,[(-1/64,-1/32),(-3/128,1/64),(5/64,-5/32),(3/128,-3/64),(3/128,-3/64),(-3/128,1/64)]):
    assert add(contract(r,plus(rw)),contract(plus(rw),r))==add(scale(a,epsdl),scale(b,vecdl));count+=1
   for r,(a,b) in zip(rw,[(5/512,-1/1024),(5/512,-1/1024),(-15/256,15/512)]):
    assert contract(r,plus(rw))==add(scale(a,sc),scale(b,ev));count+=1
 dc=0
 tests=[]
 for n,ab in enumerate(pairs5):
  for cd in pairs5[n:]:
   p=input2();p['W'][ab]=p['W'][cd]=1;p['W'][ab[::-1]]=p['W'][cd[::-1]]=-1;tests.append(p)
  for a in range(5):
   p=input2();p['dw'][(a,*ab)]=1;p['dw'][(a,*ab[::-1])]=-1;tests.append(p)
  p=input2();p['z'][(0,1,*ab)]=1;p['z'][(0,1,*ab[::-1])]=-1;tests.append(p)
 p=input2();p['Y']=1;tests.append(p)
 coeffs=[(0,0,-2,0),(0,7/4,0,5/8),(0,-1/16,-1/4,-1/16),(0,1/4,0,-1/8),(-3/16,0,-3/4,-3/16)]
 for p in tests:
  w,dw=p['W'],p['dw'];w2=sum(eta[a]*eta[b]*w[a,b]**2 for a,b in it.product(range(5),repeat=2))
  div=sum(GD[a]*eta[c]*dw[c,a,c] for a,c in it.product(range(5),repeat=2))
  ev=sum(eps5((a,b,c,d,e))*eta[a]*GD[a]*w[b,c]*w[d,e] for a,b,c,d,e in it.permutations(range(5)))
  rows=ddrows(w,dw,p['z'][0,1],p['Y'])
  for row,(a,b,c,d) in zip(rows,coeffs):
   assert np.array_equal((row-row.T)/2,1j*(a*C*p['Y']+b*C*w2+c*div+d*ev));dc+=1
  assert np.array_equal(sum(rows),sum(rows).T*-1),'full DDX is antisymmetric'
 report={'status':'PASS','date':'2026-09-23','scope':'Individual derivative-product and explicit-W DDX contraction tables',
 'RR_table_row_comparisons':count,'DDX_table_row_comparisons':dc,
 'arithmetic':'Exact Gaussian dyadic exterior coefficients; fixed expected fractions, no fitting',
 'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
 (HERE.parent/'sources/step2/w2_contraction_checks.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))
if __name__=='__main__':main()
