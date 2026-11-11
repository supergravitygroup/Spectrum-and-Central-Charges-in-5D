#!/usr/bin/env python3
"""Zero-pole LOG coefficient from source descendants, with fixed-table checks.

Inputs: S23 (2.6), (2.8a), (2.13), (2.15); C24 (A.1l), (A.3).
The source 51/64 and -3/8 enter only in the final comparison.
All Weyl spinor/three-spinor components are independent exterior generators.
Arrays w,z,dz carry lower vector indices. No EOM, IBP or field gauge is used.
"""
import runpy
from pathlib import Path
HERE=Path(__file__).resolve().parent
ns=runpy.run_path(str(HERE/'verify_log_step2_w1.py'));globals().update({k:v for k,v in ns.items() if not k.startswith('__')})
YY=add(*[prod(yu[r][0],y[r][0]) for r in range(4)])
WWW=add(*[scale(U[a,d]*U[b,e]*U[c,f],prod(w3[d,e,f,0],w3[a,b,c,0])) for a,b,c,d,e,f in it.product(range(4),repeat=6)])
def w0raw(w,z,dz=None):
 if dz is None:dz=np.zeros((5,5,5))
 ws=twoform(w);wu=U@ws@U.T;wm=-ws@U;zs=twoform(z)
 rs=RSkernel(zero(),np.zeros((5,5,5)),z)
 drs=[RSkernel(zero(),np.zeros((5,5,5)),dz[a])[a] for a in range(5)]
 T=np.array([(3*eta[a]*G[a]@wm-wm@G[a]*eta[a])/4 for a in range(5)])
 d3={(a,b,c,d):-.5*(C[a,b]*zs[c,d]+C[a,c]*zs[b,d]+C[a,d]*zs[b,c]) for a,b,c,d in it.product(range(4),repeat=4)}
 ddw={(a,b,r,s):d3[a,b,r,s]+.5*C[b,r]*zs[a,s]+.5*C[b,s]*zs[a,r] for a,b,r,s in it.product(range(4),repeat=4)}
 dm={(al,b,t):add(*[scale(-U[r,t],DW(al,b,r)) for r in range(4)]) for al,b,t in it.product(range(4),repeat=3)}
 dl1={(al,a,b):-2j*sum(rs[a,al,t]*C[t,b] for t in range(4)) for al,a,b in it.product(range(4),range(5),range(4))}
 dxjet={}
 for al,a,r in it.product(range(4),range(5),range(4)):
  dxjet[al,a,r]=add({0:twoform(dz[a])[al,r]+sum(T[a,al,t]*zs[t,r]+4*rs[a,al,t]*ws[t,r] for t in range(4))},*[scale(.5*eta[c]*eta[d]*S[c,d,r,t],prod(RM(a,al,c,d),y[t][0])) for c,d,t in it.product(range(5),range(5),range(4))])
 Yrows=[[],[],[]]
 for al,be in it.product(range(4),repeat=2):
  e=-U[al,be]
  Yrows[0].extend(scale(e*8*G[a,be,r],dxjet[al,a,r]) for a,r in it.product(range(5),range(4)))
  Yrows[1].extend(scale(e*8,prod(dm[al,be,r],y[r][0])) for r in range(4))
  Yrows[2].append({0:e*8*sum(wm[be,r]*zs[al,r] for r in range(4))})
 Yrows=[add(*r) for r in Yrows];DppY=add(*Yrows)
 W2rows=[add(*[scale(-4*U[al,be]*U[r,t]*U[s,u],prod(DW(al,t,u),DW(be,r,s))) for al,be,r,s,t,u in it.product(range(4),repeat=6)]),{0:-4*sum(U[al,be]*wu[r,s]*ddw[al,be,r,s] for al,be,r,s in it.product(range(4),repeat=4))}]
 DppW2=add(*W2rows)
 Boxrows=[[],[],[],[],[]]
 for al,be in it.product(range(4),repeat=2):
  e=-U[al,be]
  # D Box lambda at scalar degree one, all S terms retained.
  val=-2j*sum(eta[a]*drs[a][al,t]*C[t,be] for a,t in it.product(range(5),range(4)))
  val+=-2j*sum(eta[a]*T[a,al,t]*rs[a,t,r]*C[r,be] for a,t,r in it.product(range(5),range(4),range(4)))
  val+=sum(eta[a]*rs[a,al,t]*(-2j*eta[a]*G[a,t,r]*ws[r,be]+.5j*sum(w[a,c]*G[c,t,r]*C[r,be] for c in range(5))) for a,t,r in it.product(range(5),range(4),range(4)))
  Boxrows[0].append({0:e*1j*val})
  Boxrows[1].append({0:e*2j*sum(eta[a]*T[a,be,r]*dl1[al,a,r] for a,r in it.product(range(5),range(4)))})
  Boxrows[2].append({0:e*(-.75)*sum(zs[be,r]*U[r,t]*ws[al,t] for r,t in it.product(range(4),repeat=2))})
  Boxrows[3].extend(scale(e/16*G[a,be,r]*eta[a]*G[a,al,t],prod(y[r][0],y[t][0])) for a,r,t in it.product(range(5),range(4),range(4)))
  Boxrows[4].extend(scale(e*(-1/16)*eta[a]*eta[b]*SU[a,b,r,s],prod(DW(al,r,s),wab(a,b,be))) for a,b,r,s in it.product(range(5),range(5),range(4),range(4)))
  Boxrows[4].append({0:e*(-1/16)*sum(w[a,b]*SU[a,b,r,s]*d3[al,r,s,be] for a,b,r,s in it.product(range(5),range(5),range(4),range(4)))})
 Boxrows=[add(*r) for r in Boxrows];DppBox=add(*Boxrows)
 WFrows=[[],[]]
 for al,be,r,s in it.product(range(4),repeat=4):
  ddf=sum(-.5j*(GD[a,be,r]*int(t==s)+GD[a,be,s]*int(t==r)+C[be,r]*G[a,s,t]+C[be,s]*G[a,r,t])*dl1[al,a,t] for a,t in it.product(range(5),range(4)))-d3[al,be,r,s]
  WFrows[0].append({0:-2*U[al,be]*wu[r,s]*ddf})
  WFrows[1].extend(scale(4*U[al,be]*U[r,t]*U[s,u],prod(DW(al,t,u),w3[be,r,s,0])) for t,u in it.product(range(4),repeat=2))
 WFrows=[add(*r) for r in WFrows];DppWF=add(*WFrows)
 YpLmRows=[scale(-7,YY),{0:-4*sum(U[a,b]*U[r,s]*zs[a,s]*ws[b,r] for a,b,r,s in it.product(range(4),repeat=4))}]
 DppYpLm=add(*YpLmRows);DppWA=add(scale(-3j/4,DppY),scale(31j/4,DppW2))
 DXpieces=[scale(1j/4,DppBox),scale(-1j/4,DppWF),scale(-5j/32,DppYpLm),{},scale(-1/32,DppWA)];DX=add(*DXpieces)
 rw={(a,b,r):add(scale(-1.5*C[a,b],y[r][0]),scale(-.5*C[a,r],y[b][0]),scale(.5*C[b,r],y[a][0])) for a,b,r in it.product(range(4),repeat=3)}
 DBpieces=[{0:-2*sum(U[d,a]*U[r,s]*zs[a,r]*ws[d,s] for d,a,r,s in it.product(range(4),repeat=4))},add(*[scale(eps4(a,b,c,d)*U[r,s]/16,prod(rw[a,b,r],rw[c,d,s])) for a,b,c,d in it.permutations(range(4)) for r,s in it.product(range(4),repeat=2)])]
 DB=add(*DBpieces);H=add(scale(-.5,DX),scale(-1j/8,DB));return locals()

# Columns: W_ab X^{ab++}, X^{alpha+}X_alpha^+, W^{alpha beta gamma+}W_{alpha beta gamma}^+.
TABLES={
 'Yrows':[[4,-20,0],[0,20,0],[-4,0,0]],
 'W2rows':[[0,10,4],[-8,0,0]],
 'Boxrows':[[-3/16,0,0],[15/8,0,0],[-3/8,0,0],[0,5/16,0],[3/16,0,-1/8]],
 'WFrows':[[6,0,0],[0,0,-4]],
 'YpLmRows':[[0,-7,0],[2,0,0]],
 'DXpieces':[[3j/8,5j/64,-1j/32],[-3j/2,0,1j],[-5j/16,35j/32,0],[0,0,0],[31j/16,-155j/64,-31j/32]],
 'DBpieces':[[1,0,0],[0,-11/8,0]]}
def fixed(bs,cs):return add(*[scale(c,b) for c,b in zip(cs,bs)])
def check_extra(w,z,d):
 ws,wu,rs,T,dl1,d3=[d[k] for k in ['ws','wu','rs','T','dl1','d3']]
 wz=sum(eta[a]*eta[b]*w[a,b]*z[a,b] for a,b in it.product(range(5),repeat=2))
 rows=[0j]*4
 for a,al,be,t,r in it.product(range(5),range(4),range(4),range(4),range(4)):
  e=-U[al,be]*1j
  rows[1]+=e*(-2j)*eta[a]*T[a,al,t]*rs[a,t,r]*C[r,be]
  rows[2]+=e*eta[a]*rs[a,al,t]*(-2j*eta[a]*G[a,t,r]*ws[r,be])
  rows[3]+=e*eta[a]*rs[a,al,t]*(.5j*sum(w[a,c]*G[c,t,r]*C[r,be] for c in range(5)))
 assert rows==[0,9*wz/16,-3*wz/8,-3*wz/8]
 frows=[0j,0j]
 for al,be,r,s in it.product(range(4),repeat=4):
  common=-2*U[al,be]*wu[r,s]
  frows[0]+=common*sum(-.5j*(GD[a,be,r]*int(t==s)+GD[a,be,s]*int(t==r)+C[be,r]*G[a,s,t]+C[be,s]*G[a,r,t])*dl1[al,a,t] for a,t in it.product(range(5),range(4)))
  frows[1]+=common*(-d3[al,be,r,s])
 assert frows==[3*wz,3*wz]
 return 6

def main():
 import json,hashlib,time
 start=time.monotonic();counts={'zero even fields, all Weyl fermions':0,'W times Weyl two-form descendant':0,'uncontracted derivative of Weyl two-form descendant':0,'combined nonzero even fields':0};rows=0;extra=0
 def check(w,z,dz,name):
  nonlocal rows,extra
  d=w0raw(w,z,dz);wz=sum(eta[a]*eta[b]*w[a,b]*z[a,b] for a,b in it.product(range(5),repeat=2));bs=[scale(wz,{0:1}),YY,WWW]
  for k,tab in TABLES.items():
   for n,cs in enumerate(tab):assert add(d[k][n])==fixed(bs,cs),(name,k,n)
   rows+=len(tab)
  assert d['DX']==fixed(bs,[1j/2,-5j/4,0]);assert d['DB']==fixed(bs,[1,-11/8,0]);assert d['H']==fixed(bs,[-3j/8,51j/64,0])
  extra+=check_extra(w,z,d);counts[name]+=1
 check(zero(),zero(),None,'zero even fields, all Weyl fermions')
 for ab,cd in it.product(pairs5,repeat=2):
  w=zero();z=zero();w[ab]=1;w[ab[::-1]]=-1;z[cd]=1;z[cd[::-1]]=-1
  check(w,z,None,'W times Weyl two-form descendant')
 for a,ab in it.product(range(5),pairs5):
  dz=np.zeros((5,5,5));dz[a,*ab]=1;dz[a,*ab[::-1]]=-1
  check(zero(),zero(),dz,'uncontracted derivative of Weyl two-form descendant')
 w=zero();z=zero()
 for n,ab in enumerate(pairs5):w[ab]=n%3-1;w[ab[::-1]]=-w[ab];z[ab]=n%5-2;z[ab[::-1]]=-z[ab]
 check(w,z,np.arange(125).reshape(5,5,5)-np.arange(125).reshape(5,5,5).transpose(0,2,1),'combined nonzero even fields')
 # Nine separate entries of the R1 R1 contraction, with its actual odd order.
 rw={(a,b,r):[scale(-1.5*C[a,b],y[r][0]),scale(-.5*C[a,r],y[b][0]),scale(.5*C[b,r],y[a][0])] for a,b,r in it.product(range(4),repeat=3)}
 rr=[[-9/8,-3/32,-3/32],[-3/32,1/32,1/32],[-3/32,1/32,1/32]]
 for j,k in it.product(range(3),repeat=2):
  raw=add(*[scale(eps4(a,b,c,d)*U[r,s]/16,prod(rw[a,b,r][j],rw[c,d,s][k])) for a,b,c,d in it.permutations(range(4)) for r,s in it.product(range(4),repeat=2)])
  assert raw==scale(rr[j][k],YY)
 # Analyticity: five anticommuting plus derivatives on four spinor slots vanish.
 words=0
 for a in range(4):
  for rest in it.permutations(range(4)):
   word=(a,*rest);assert len(set(word))<len(word);words+=1
 report={'date':'2026-09-23','status':'PASS','scope':'Both W^0 terms, each intermediate descendant and table; full S/K/reality certificate not claimed','source_agreement':'Both W^0 terms agree with S23 (3.25)','basis_probes':counts,'total_probes':sum(counts.values()),'fixed_table_rows':rows,'additional_Box_lambda_and_WF_subrows':extra,'bilinear_product_rows':9,'five_plus_derivative_words':words,'arithmetic':'Exactly representable Gaussian dyadic coefficients; equality is exact and no coefficients are fitted','elapsed_seconds':round(time.monotonic()-start,2),'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
 (HERE.parent/'sources/step2/w0_checks.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))
if __name__=='__main__':main()
