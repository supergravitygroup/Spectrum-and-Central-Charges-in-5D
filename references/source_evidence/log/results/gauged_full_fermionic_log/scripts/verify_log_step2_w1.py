#!/usr/bin/env python3
"""W^-1 LOG primary from four spinor derivatives and full source curvatures.

Source inputs: S23 2.6a-f, 2.13a-c, 2.15; C24 A.1, A.3a-f.
calculate evaluates Delta X-- via D++ of the previously derived D++ X--.
finalparts constructs the pole from the graded projector, not the benchmark.
target1 is used only for the final comparison. No coefficient fitting.
Spinors and their first derivatives are independent exterior generators.
"""
import runpy
from pathlib import Path
HERE=Path(__file__).resolve().parent
m=runpy.run_path(str(HERE/'verify_log_step2_w2.py'));globals().update({k:v for k,v in m.items() if not k.startswith('__')})
dy=[[[{1<<(104+8*a+2*r+i):1} for i in range(2)] for r in range(4)] for a in range(5)]
dw3={}
for n,ids in enumerate(it.combinations_with_replacement(range(4),3)):
 for perm in set(it.permutations(ids)):
  for a,i in it.product(range(5),range(2)):dw3[a,*perm,i]={1<<(144+10*n+2*a+i):1}
from functools import lru_cache
@lru_cache(None)
def wab(a,b,r,i=0,grad=None):
 return add(*[scale(SU[a,b,t,u],w3[t,u,r,i] if grad is None else dw3[grad,t,u,r,i]) for t,u in it.product(range(4),repeat=2)])
@lru_cache(None)
def DW(al,r,s,grad=None):
 yy=y if grad is None else dy[grad];www=w3[al,r,s,0] if grad is None else dw3[grad,al,r,s,0]
 return add(www,scale(.5*C[al,r],yy[s][0]),scale(.5*C[al,s],yy[r][0]))
@lru_cache(None)
def RM(a,al,c,d,grad=None):
 yy=y if grad is None else dy[grad]
 return add(*[scale(-eta[a]*G[a,al,t],wab(c,d,t,grad=grad)) for t in range(4)],*[scale(-.25*eta[a]*eps5((a,c,d,e,f))*eta[e]*eta[f],wab(e,f,al,grad=grad)) for e,f in it.product(range(5),repeat=2)],*[scale(.25*(int(a==c)*G[d,al,t]-int(a==d)*G[c,al,t]),yy[t][0]) for t in range(4)])
def RK(w):
 tw=dual(w);out={};rows={}
 for b,al,c in it.product(range(5),range(4),range(5)):
  ts=[[] for _ in range(13)]
  ts[0]=[scale(eta[b]*G[c,al,t]*16,wab(d,b,t,grad=d)) for d,t in it.product(range(5),range(4))]
  ts[1]=[scale(eta[b]*G[b,al,t]*8,wab(d,c,t,grad=d)) for d,t in it.product(range(5),range(4))]
  ts[2]=[scale(eta[b]*G[a,al,t]*16,wab(b,c,t,grad=a)) for a,t in it.product(range(5),range(4))]
  ts[3]=[scale(-eta[b]*eps5((b,c,d,e,f))*eta[e]*eta[f]*4,wab(e,f,al,grad=d)) for d,e,f in it.product(range(5),repeat=3)]
  ts[4]=[scale(G[c,al,t]*12,dy[b][t][0]) for t in range(4)]
  ts[5]=[scale(w[d,e]*eta[b]*(3*G[b]@S[d,e]@G[c]-S[d,e]@G[b]@G[c])[al,t]*1.5,y[t][0]) for d,e,t in it.product(range(5),range(5),range(4))]
  ts[6]=[scale(-tw[b,d,e]*G[c,al,t]*2,wab(d,e,t)) for d,e,t in it.product(range(5),range(5),range(4))]
  ts[7]=[scale(int(b==c)*w[d,e]*12,wab(d,e,al)) for d,e in it.product(range(5),repeat=2)]
  ts[8]=[scale(eta[b]*S[b,c,al,t]*w[d,e]*8,wab(d,e,t)) for d,e,t in it.product(range(5),range(5),range(4))]
  ts[9]=[scale(-w[d,e]*S[d,e,al,t]*eta[b]*8,wab(b,c,t)) for d,e,t in it.product(range(5),range(5),range(4))]
  ts[10]=[scale(13*w[b,d]*2,wab(d,c,al)) for d in range(5)]
  ts[11]=[scale(11*eta[b]*eta[c]*w[d,c]*2,wab(b,d,al)) for d in range(5)]
  ts[12]=[scale(-13*eta[b]*G[b,al,t]*eta[c]*tw[d,e,c]*1,wab(d,e,t)) for d,e,t in it.product(range(5),range(5),range(4))]
  rows[b,al,c]=[add(*t) for t in ts];out[b,al,c]=add(*rows[b,al,c])
 return out,rows

def prepare(w,dw,z,Y,X,F,v):
 ws=twoform(w);wm=-ws@U;fs=twoform(F);T=np.array([(3*eta[a]*G[a]@wm-wm@G[a]*eta[a])/4 for a in range(5)])
 rS=RSkernel(w,dw,z[0,1]);rSp=RSkernel(zero(),dw*0,z[0,0]);rm={(a,al,c,d):RM(a,al,c,d) for a,al,c,d in it.product(range(5),range(4),range(5),range(5))};rk,rkrows=RK(w)
 dxm=dxweyl(w,dw,z[0,1],Y);dxp=twoform(z[0,0]);qm=-2*fs-C*X[0,1]-sum(GD[a]*v[a] for a in range(5));qp=-C*X[0,0]
 # Spinor derivative of a vector derivative of the primary super-Weyl tensor.
 ddw={}
 for al,a,r,s in it.product(range(4),range(5),range(4),range(4)):
  ddw[al,a,r,s]=add(DW(al,r,s,grad=a),*[scale(T[a,al,t],DW(t,r,s)) for t in range(4)],*[scale(.5*eta[c]*eta[d]*(S[c,d,r,t]*ws[t,s]+S[c,d,s,t]*ws[r,t]),rm[a,al,c,d]) for c,d,t in it.product(range(5),range(5),range(4))],*[scale(-.25*eta[a]*G[a,al,t]*ws[r,s],y[t][0]) for t in range(4)])
 # D+ X_{rs}^{+-}, with the symmetrizations expanded from S23 2.6e.
 dz={}
 for al,b,c in it.product(range(4),repeat=3):
  ts=[]
  for l in range(4):
   ts.extend([scale(-1.5j*wm[b,l],w3[c,al,l,0]),scale(-1.5j*wm[c,l],w3[b,al,l,0]),scale(.75j*(C[al,b]*ws[c,l]+C[al,c]*ws[b,l]),yu[l][0])])
   ts.extend([scale(-1j*ws[al,l]*U[l,t],w3[b,c,t,0]) for t in range(4)])
  for r,t in it.product(range(4),repeat=2):
   ts.extend([scale(-.5j*C[al,b]*(U@ws@U.T)[r,t],w3[c,r,t,0]),scale(-.5j*C[al,c]*(U@ws@U.T)[r,t],w3[b,r,t,0])])
  ts.extend([scale(-1.5j*ws[b,c],y[al][0]),scale(.25j*ws[al,b],y[c][0]),scale(.25j*ws[al,c],y[b][0])])
  for a,r in it.product(range(5),range(4)):
   ts.extend([scale(2j*G[a,al,r],dw3[a,b,c,r,0]),scale(1j*G[a,b,r],dw3[a,c,al,r,0]),scale(1j*G[a,c,r],dw3[a,b,al,r,0])])
   ts.extend([scale(.5j*(C[al,b]*GD[a,c,l]+C[al,c]*GD[a,b,l])*U[l,r],dy[a][r][0]) for l in range(4)])
  for a in range(5):
   ts.extend([scale(-.5j*GD[a,al,b],dy[a][c][0]),scale(-.5j*GD[a,al,c],dy[a][b][0])])
  dz[al,b,c]=scale(.5,add(*ts))
 # Spinor derivatives of X_Weyl^- and W^2/Y building blocks.
 dyd={};dw2={}
 for al in range(4):
  dyd[al]=add(*[scale(8*G[a,al,t],dy[a][t][0]) for a,t in it.product(range(5),range(4))],*[scale(8*wm[al,t],y[t][0]) for t in range(4)])
  dw2[al]=add(*[scale(4*(U@ws@U.T)[r,s],DW(al,r,s)) for r,s in it.product(range(4),repeat=2)])
 d_dxm={}
 for al,b,c in it.product(range(4),repeat=3):
  ts=[dz[al,b,c],scale(1j*C[b,c]/8,dyd[al])]
  ts.extend(scale(-1.5j*G[a,b,r],ddw[al,a,c,r]) for a,r in it.product(range(5),range(4)))
  ts.extend(scale(-.5j*G[a,c,r],ddw[al,a,b,r]) for a,r in it.product(range(5),range(4)))
  for r,t in it.product(range(4),repeat=2):
   ts.append(scale(2j*U[t,r]*ws[c,r],DW(al,b,t)))
   ts.append(scale(-2j*wm[b,r]*int(t==0),DW(al,c,r))) if t==0 else None
  ts.extend(scale(.25j*C[b,c],dw2[al]) for _ in [0])
  d_dxm[al,b,c]=add(*ts)
 # D+ nabla_a lambda_beta^+ including its scalar-W^0 part.
 d_dl={};km={}
 for al,a,b in it.product(range(4),range(5),range(4)):
  km[al,a,b]=add({0:-sum(T[a,al,t]*C[t,b]*X[0,0] for t in range(4))},*[scale(.5*eta[c]*eta[d]*S[c,d,b,t],prod(rm[a,al,c,d],ll[t][0])) for c,d,t in it.product(range(5),range(5),range(4))])
 # The caller adds -C_ab nabla_a X++ to km for D nabla lambda.
 return locals()
def divide96(poly):
 from fractions import Fraction
 out={}
 for k,v in poly.items():
  real=Fraction(float(v.real))/96;imag=Fraction(float(v.imag))/96
  assert real.denominator & (real.denominator-1)==0 and imag.denominator & (imag.denominator-1)==0, (k,real,imag)
  out[k]=complex(real,imag)
 return out

def calculate(p,detail=False):
 w,dw,z,Y,X,F,v=[p[k] for k in ['W','dw','z','Y','X','F','v']];dx=p['dx'];boxX=p.get('boxX',0)
 c=prepare(w,dw,z,Y,X,F,v);ws,wm,T,rS,rSp,rm,rk,dxm,dxp,qm,qp,ddw,dz,dyd,dw2,d_dxm,km=[c[k] for k in ['ws','wm','T','rS','rSp','rm','rk','dxm','dxp','qm','qp','ddw','dz','dyd','dw2','d_dxm','km']]
 w2=sum(eta[a]*eta[b]*w[a,b]**2 for a,b in it.product(range(5),repeat=2));dws=np.array([twoform(dw[a]) for a in range(5)])
 d_dl={(al,a,b):add({0:-C[al,b]*dx[a,0,0]},km[al,a,b]) for al,a,b in it.product(range(4),range(5),range(4))}
 DT={}
 for al,a,b,t in it.product(range(4),range(5),range(4),range(4)):
  DT[al,a,b,t]=add(*[scale(-.75*eta[a]*G[a,b,r]*U[s,t],DW(al,r,s)) for r,s in it.product(range(4),repeat=2)],*[scale(.25*eta[a]*U[s,r]*G[a,r,t],DW(al,b,s)) for r,s in it.product(range(4),repeat=2)])
 div=sum(G[a]*eta[b]*dw[b,a,b] for a,b in it.product(range(5),repeat=2));curl=sum(eps5((a,b,c,d,e))*eta[a]*eta[b]*S[a,b]*dw[c,d,e] for a,b,c,d,e in it.permutations(range(5)))
 O=-3/8*twoform(z[0,1])@U-9j*w2*I/64-9j*div/16-3j*curl/16
 ZpM=-dxp@U
 DO={};DOrows={}
 for al,b,t in it.product(range(4),repeat=3):
  ts=[scale(-3/8*U[r,t],dz[al,b,r]) for r in range(4)];ts.append(scale(-9j/64*I[b,t],dw2[al]))
  for a,c0,r,s in it.product(range(5),range(5),range(4),range(4)):
   # divergence: nabla^c W_ac, lower W_ac = eta_a eta_c SU_ac Wspin
   ts.append(scale(-9j/16*G[a,b,t]*eta[a]*SU[a,c0,r,s],ddw[al,c0,r,s]))
  for a,c0,e,f,g in it.permutations(range(5)):
   for r,s in it.product(range(4),repeat=2):
    ts.append(scale(-3j/16*eps5((a,c0,e,f,g))*eta[a]*eta[c0]*S[a,c0,b,t]*eta[f]*eta[g]*SU[f,g,r,s],ddw[al,e,r,s]))
  DO[al,b,t]=add(*ts)
  DOrows[al,b,t]=[add(*ts[:4]),ts[4],add(*ts[5:405]),add(*ts[405:])]
 # source covariant commutator on Box lambda^+.
 dboxl={}
 for al,b in it.product(range(4),repeat=2):
  ts=[{0:-C[al,b]*boxX}];kts=[]
  for a in range(5):
   for t in range(4):
    dta=sum((3*eta[a]*G[a]@(-dws[a]@U)-(-dws[a]@U)@G[a]*eta[a])[al,t]/4 for _ in [0])
    ts.append({0:-eta[a]*(dta*C[t,b]*X[0,0]+2*T[a,al,t]*C[t,b]*dx[a,0,0])})
    ts.append(scale(eta[a]*T[a,al,t],km[t,a,b]))
    ts.append(scale(.75*G[a,al,t],prod(y[t][0],dl[a][b][0])))
    for e,f in it.product(range(5),repeat=2):
     ts.append(scale(.5*eta[a]*eta[e]*eta[f]*S[e,f,b,t],prod(RM(a,al,e,f,grad=a),ll[t][0])))
     ts.append(scale(eta[a]*eta[e]*eta[f]*S[e,f,b,t],prod(rm[a,al,e,f],dl[a][t][0])))
   ts.append({0:-2j*eta[a]*v[a]*sum(rSp[a,al,t]*C[t,b] for t in range(4))})
   for gam in range(4):
    slowplus=-2*c['fs']+C*X[0,1]-sum(GD[q]*v[q] for q in range(5));slowminus=qp
    sjetp=1j*sum(eta[a]*G[a,gam,t]*slowplus[t,b] for t in range(4))-2j*C[gam,b]*v[a]
    sjetm=1j*sum(eta[a]*G[a,gam,t]*slowminus[t,b] for t in range(4))
    ts.append({0:eta[a]*(rSp[a,al,gam]*sjetp+rS[a,al,gam]*sjetm)})
   for e in range(5):
    kts.append(scale(3*int(a==e),prod(rk[a,al,e],ll[b][0])))
    kts.extend(scale(2*eta[e]*S[e,a,b,t],prod(rk[a,al,e],ll[t][0])) for t in range(4))
  dboxl[al,b]=add(scale(96,add(*ts)),add(*kts)) # numerator of 96 D Box lambda
 dbbox={};boxrows={}
 for al,b in it.product(range(4),repeat=2):
  ts=[scale(1j,dboxl[al,b])];br=[[ts[0]],[],[],[],[],[],[],[],[]]
  for a,t in it.product(range(5),range(4)):
   ts.extend([scale(2j*eta[a],prod(DT[al,a,b,t],dl[a][t][0])),scale(2j*eta[a]*T[a,b,t],d_dl[al,a,t])])
  br[1]=ts[1:].copy()
  Os=[-3/8*twoform(z[0,1])@U,-9j*w2*I/64,-9j*div/16,-3j*curl/16]
  for t in range(4):
   ts.extend([prod(DO[al,b,t],ll[t][0]),{0:O[b,t]*qp[al,t]-3/8*ZpM[b,t]*qm[al,t]}])
   for n in range(4):br[[2,4,5,6][n]].extend([prod(DOrows[al,b,t][n],ll[t][0]),{0:Os[n][b,t]*qp[al,t]}])
   br[3].append({0:-3/8*ZpM[b,t]*qm[al,t]})
  for a,t in it.product(range(5),range(4)):
   dV=add(scale(1j,dl[a][al][0]),*[scale(1j*T[a,al,r],ll[r][0]) for r in range(4)])
   ts.append({0:.25*G[a,b,t]*dxp[al,t]*v[a]})
   ts.append(scale(-.25*G[a,b,t],prod(y[t][0],dV)));br[7].extend(ts[-2:])
  # D (W * (D Box W)_1): the factor W is differentiated.
  ts.extend(scale(-1j*w[e,f]/16,prod(ll[al][0],wab(e,f,b))) for e,f in it.product(range(5),repeat=2))
  br[8]=ts[-25:];boxrows[al,b]=[add(*x) for x in br]
  dbbox[al,b]=add(ts[0],scale(96,add(*ts[1:])))
  boxrows[al,b]=[boxrows[al,b][0]]+[scale(96,t) for t in boxrows[al,b][1:]]
  assert dbbox[al,b]==add(*boxrows[al,b])
 DppBoxRows=[divide96(add(*[scale(-U[a,b],boxrows[a,b][n]) for a,b in it.product(range(4),repeat=2)])) for n in range(9)]
 DppBox=divide96(add(*[scale(-U[a,b],dbbox[a,b]) for a,b in it.product(range(4),repeat=2)]))
 # D++ F_beta gamma from the source first derivative, never from benchmark.
 DF={};DDF={};DDW={}
 for be,r,s in it.product(range(4),repeat=3):
  DF[be,r,s]=add(*[scale(-.5j*(GD[a,be,r]*int(t==s)+GD[a,be,s]*int(t==r)+C[be,r]*G[a,s,t]+C[be,s]*G[a,r,t]),dl[a][t][0]) for a,t in it.product(range(5),range(4))],scale(-1.5j*ws[r,s],ll[be][0]),scale(.25j*ws[be,r],ll[s][0]),scale(.25j*ws[be,s],ll[r][0]),*[scale(-.75j*(C[be,r]*wm[s,t]+C[be,s]*wm[r,t]),ll[t][0]) for t in range(4)])
  for al in range(4):
   DDW[al,be,r,s]=-.5*(C[al,r]*dxp[s,be]+C[al,s]*dxp[r,be]+C[al,be]*dxp[r,s])+.5*C[be,r]*dxp[al,s]+.5*C[be,s]*dxp[al,r]
   ts=[scale(-.5j*(GD[a,be,r]*int(t==s)+GD[a,be,s]*int(t==r)+C[be,r]*G[a,s,t]+C[be,s]*G[a,r,t]),d_dl[al,a,t]) for a,t in it.product(range(5),range(4))]
   ts.extend([scale(-1.5j,prod(DW(al,r,s),ll[be][0])),{0:-1.5j*ws[r,s]*qp[al,be]},scale(.25j,prod(DW(al,be,r),ll[s][0])),{0:.25j*ws[be,r]*qp[al,s]},scale(.25j,prod(DW(al,be,s),ll[r][0])),{0:.25j*ws[be,s]*qp[al,r]},scale(1j,prod(w3[be,r,s,0],ll[al][0]))])
   for t in range(4):
    ts.extend([scale(.75j*C[be,r]*U[q,t],prod(DW(al,s,q),ll[t][0])) for q in range(4)])
    ts.extend([scale(.75j*C[be,s]*U[q,t],prod(DW(al,r,q),ll[t][0])) for q in range(4)])
    ts.append({0:-.75j*(C[be,r]*wm[s,t]+C[be,s]*wm[r,t])*qp[al,t]})
   DDF[al,be,r,s]=add(*ts)
 DppWF=add(*[scale(-2*U[a,b]*(U@c['fs']@U.T)[r,s],{0:DDW[a,b,r,s]}) for a,b,r,s in it.product(range(4),repeat=4)],*[scale(-2*U[a,b]*(U@ws@U.T)[r,s],DDF[a,b,r,s]) for a,b,r,s in it.product(range(4),repeat=4)],*[scale(-4*U[a,b]*U[r,t]*U[s,u],prod(DW(a,t,u),DF[b,r,s])) for a,b,r,s,t,u in it.product(range(4),repeat=6)])
 DppYminus=[add(*[scale(-U[a,b],d_dxm[a,b,r]) for a,b in it.product(range(4),repeat=2)]) for r in range(4)]
 DppLminus=[add(*[scale(4j*G[a,r,t],dl[a][t][0]) for a,t in it.product(range(5),range(4))],*[scale(-10j*ws[r,t],lu[t][0]) for t in range(4)]) for r in range(4)]
 DppYpLm=add(*[prod(yu[r][0],DppLminus[r]) for r in range(4)],{0:2*sum(U[a,b]*(dxp@U.T)[a,r]*qm[b,r] for a,b,r in it.product(range(4),repeat=3))})
 DppYmLp=add(*[scale(U[r,t],prod(DppYminus[t],ll[r][0])) for r,t in it.product(range(4),repeat=2)],{0:2*sum(U[a,b]*(dxm@U.T)[a,r]*qp[b,r] for a,b,r in it.product(range(4),repeat=3))})
 AA=-3j*Y/4+31j*w2/4
 DA=[add(scale(-3j/4,dyd[a]),scale(31j/4,dw2[a])) for a in range(4)]
 DppWA=add({0:-4j*X[0,0]*AA},*[scale(-2j*U[a,b],prod(ll[a][0],DA[b])) for a,b in it.product(range(4),repeat=2)])
 pieces=[scale(1j/4,DppBox),scale(-1j/4,DppWF),scale(-5j/32,DppYpLm),scale(9j/32,DppYmLp),scale(-1/32,DppWA)]
 if detail:return locals()
 return add(*pieces)

def finalparts(p):
 w,F,X,v,z,Y=[p[k] for k in ['W','F','X','v','z','Y']];ws=twoform(w);wm=-ws@U;fs=twoform(F);zs=twoform(z[0,0]);w2=sum(eta[a]*eta[b]*w[a,b]**2 for a,b in it.product(range(5),repeat=2));qm=-2*fs-C*X[0,1]-sum(GD[a]*v[a] for a in range(5));q1=-2*ws
 out=[scale(-.5,calculate(p)),{0:3/64*X[0,0]*Y-31/64*X[0,0]*w2}]
 tx=[add(*[scale(-6j*G[a,al,t],dy[a][t][0]) for a,t in it.product(range(5),range(4))],*[scale(15j*wm[al,t],y[t][0]) for t in range(4)],*[scale(8j*w[a,b],wab(a,b,al)) for a,b in it.product(range(5),repeat=2)]) for al in range(4)]
 out.append(add(*[scale(-1j/16,prod(lu[al][0],tx[al])) for al in range(4)]));out.append({0:X[0,0]*w2/8})
 rw={(a,b,r):add(scale(-1.5*C[a,b],y[r][0]),scale(-.5*C[a,r],y[b][0]),scale(.5*C[b,r],y[a][0])) for a,b,r in it.product(range(4),repeat=3)};rr=Rplus(ws,True)
 out.append(add(*[scale(-eps4(a,b,c,d)*U[r,s]*ws[d,s]/8,prod(ll[a][0],rw[b,c,r])) for a,b,c,d in it.permutations(range(4)) for r,s in it.product(range(4),repeat=2)]))
 tp={}
 for al,r in it.product(range(4),repeat=2):
  tp[al,r]=add({0:4j*sum(GD[a,al,r]*p['dx'][a,0,0] for a in range(5))-8j*ws[al,r]*X[0,0]},*[scale(-8j,prod(w3[al,r,t,0],lu[t][0])) for t in range(4)],*[scale(1j*C[al,r],prod(yu[t][0],ll[t][0])) for t in range(4)],scale(2j,prod(y[al][0],ll[r][0])),scale(-2j,prod(y[r][0],ll[al][0])))
 out.append(add(*[scale(1j*U[d,a]*U[r,s]/32,add({0:-4*zs[a,r]*qm[d,s]},scale(q1[d,s],tp[a,r]))) for a,d,r,s in it.product(range(4),repeat=4)]))
 out.append(add(*[scale(-1j*eps4(a,b,c,d)*U[r,s]/128,add(prod(rr[a,b,r],rw[c,d,s]),prod(rw[a,b,r],rr[c,d,s]))) for a,b,c,d in it.permutations(range(4)) for r,s in it.product(range(4),repeat=2)]))
 return out

def target1(p):
 w,F,X,z,Y=[p[k] for k in ['W','F','X','z','Y']];w2=sum(eta[a]*eta[b]*w[a,b]**2 for a,b in it.product(range(5),repeat=2))
 return add({0:9/64*X[0,0]*(Y-w2)-.5*p.get('boxX',0)-3j/8*sum(eta[a]*eta[b]*F[a,b]*z[0,0,a,b] for a,b in it.product(range(5),repeat=2))},*[scale(w[a,b]*U[r,t]/4,prod(wab(a,b,t),ll[r][0])) for a,b,r,t in it.product(range(5),range(5),range(4),range(4))],*[scale(-.75*GU[a,r,t],prod(y[r][0],dl[a][t][0])) for a,r,t in it.product(range(5),range(4),range(4))],*[scale(.75*GU[a,r,t],prod(ll[r][0],dy[a][t][0])) for a,r,t in it.product(range(5),range(4),range(4))])

def reduced_delta(p):
 w,F,X,z,Y=[p[k] for k in ['W','F','X','z','Y']];w2=sum(eta[a]*eta[b]*w[a,b]**2 for a,b in it.product(range(5),repeat=2))
 return add({0:p.get('boxX',0)-3*X[0,0]*Y/16+X[0,0]*w2/16+1j/2*sum(eta[a]*eta[b]*F[a,b]*z[0,0,a,b] for a,b in it.product(range(5),repeat=2))},*[scale(1.25*GU[a,r,t],prod(y[r][0],dl[a][t][0])) for a,r,t in it.product(range(5),range(4),range(4))],*[scale(-.75*GU[a,r,t],prod(ll[r][0],dy[a][t][0])) for a,r,t in it.product(range(5),range(4),range(4))],*[scale(.75*SU[a,b,r,t]*w[a,b],prod(y[r][0],ll[t][0])) for a,b,r,t in it.product(range(5),range(5),range(4),range(4))])

def main():
 import json,time,hashlib
 counts={};start=time.monotonic()
 def check(p,name):
  parts=finalparts(p)
  assert add(*parts)==target1(p),(name,'primary')
  assert scale(-2,parts[0])==reduced_delta(p),(name,'Delta X')
  counts[name]=counts.get(name,0)+1
 def form(p,key,ab):p[key][ab]=1;p[key][ab[::-1]]=-1
 check(input2(),'all independent odd components')
 p=input2();p['boxX']=1;check(p,'Box X')
 for i,j in [(0,0),(0,1),(1,1)]:
  p=input2();p['X'][i,j]=p['X'][j,i]=1;p['Y']=1;check(p,'X Y')
 for n,ab in enumerate(pairs5):
  p=input2();form(p,'W',ab);check(p,'W with all odd components')
  for cd in pairs5[n:]:
   p=input2();form(p,'W',ab);form(p,'W',cd);p['X'][0,0]=1;check(p,'X W squared polarization')
  for cd in pairs5:
   p=input2();form(p,'F',ab);p['z'][0,0,*cd]=1;p['z'][0,0,*cd[::-1]]=-1;check(p,'F times Weyl tensor descendant')
  for a in range(5):
   p=input2();p['dw'][a,*ab]=1;p['dw'][a,*ab[::-1]]=-1;p['F'][(a+1)%5,(a+2)%5]=1;p['F'][(a+2)%5,(a+1)%5]=-1;p['v'][a]=1;check(p,'uncontracted derivative W cancellation')
 for a in range(5):
  p=input2();p['v'][a]=1;check(p,'scalar gradient cancellation')
  for i,j in [(0,0),(0,1),(1,1)]:
   p=input2();p['dx'][a,i,j]=p['dx'][a,j,i]=1;check(p,'auxiliary gradient cancellation')
 p=input2();p['boxX']=2;p['Y']=3;p['X']=np.array([[2,1],[1,-1]]);p['v']=np.arange(5)-2
 for n,ab in enumerate(pairs5):
  p['W'][ab]=n%3-1;p['W'][ab[::-1]]=-p['W'][ab];p['F'][ab]=n%5-2;p['F'][ab[::-1]]=-p['F'][ab]
  p['z'][0,0,*ab]=n%4-1;p['z'][0,0,*ab[::-1]]=-p['z'][0,0,*ab]
 check(p,'combined nonzero fields')
 report={'date':'2026-09-23','status':'PASS','scope':'Complete W^-1 coefficient and intermediate Delta X-- at explicit scalar W^0; no full-primary certification',
 'source_agreement':'All seven W^-1 terms agree with S23 (3.25)',
 'arithmetic':'Exact Gaussian dyadic exterior polynomial equality, no tolerance or fitted coefficient',
 'basis_probes':counts,'total_probes':sum(counts.values()),
 'odd_components':'8 lambda, 40 nabla lambda, 8 Weyl X, 40 nabla Weyl X, 40 symmetric W3, 200 nabla W3',
 'elapsed_seconds':round(time.monotonic()-start,2),'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
 (HERE.parent/'sources/step2/w1_checks.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))
if __name__=='__main__':main()
