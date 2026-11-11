#!/usr/bin/env python3
"""Check W^-2 from the graded projector and source descendant rules.

Raw p2parts is the twelve-way expansion in STEP_02_LOG_PRIMARY.md.
The independent comparison target2 is the twelve printed S23 (3.25) terms.
No coefficients are solved for or fitted. Fermions are exterior generators.
All comparisons use exact Gaussian dyadic equality, not a numerical tolerance.
The analytic R(S) and D X_Weyl inputs are C24 A.3e and S23 2.6b.
"""
import runpy
from pathlib import Path
HERE=Path(__file__).resolve().parent
ns=runpy.run_path(str(HERE/'verify_log_step2_w3.py'));globals().update({k:v for k,v in ns.items() if not k.startswith('__')})
I=np.eye(4);eps5=lambda ids: -cc['eps'](ids) if len(set(ids))==5 else 0
pairs5=list(it.combinations(range(5),2))
def twoform(f):return sum(f[a,b]*SD[a,b]/2 for a,b in it.product(range(5),repeat=2))
def dual(f):return np.array([[[sum(eta[a]*eta[b]*eta[c]*eps5((a,b,c,d,e))*f[d,e]/2 for d,e in it.product(range(5),repeat=2)) for c in range(5)] for b in range(5)] for a in range(5)])
def RSkernel(w,dw,z):
 tw=dual(w);dtw=np.array([dual(dw[a]) for a in range(5)]);w2=sum(eta[c]*eta[d]*w[c,d]**2 for c,d in it.product(range(5),repeat=2));RS=[]
 for b in range(5):
  gb=eta[b]*G[b];rs=sum(z[c,d]*(S[c,d]@gb-2*gb@S[c,d])/16 for c,d in it.product(range(5),repeat=2))
  rs+=sum(-1j/8*(dw[b,c,d]+dw[c,d,b]+dw[d,b,c])*S[c,d] for c,d in it.product(range(5),repeat=2))
  rs+=sum(-1j/8*eta[d]*eta[b]*dw[d,d,c]*S[c,b] for c,d in it.product(range(5),repeat=2))
  rs+=sum(3j/16*eta[d]*dw[d,d,b]*I for d in range(5))
  rs+=sum(-1j/8*eta[c]*dtw[c,c,b,d]*G[d] for c,d in it.product(range(5),repeat=2))
  rs+=sum(1j/16*eta[d]*eta[e]*eta[b]*tw[c,d,e]*w[d,e]*S[c,b] for c,d,e in it.product(range(5),repeat=3))
  rs+=sum(-3j/32*eta[d]*eta[e]*tw[b,d,e]*w[d,e]*I for d,e in it.product(range(5),repeat=2))
  rs+=sum(1j/4*eta[d]*w[b,d]*w[c,d]*G[c] for c,d in it.product(range(5),repeat=2))
  rs+=-3j/64*w2*gb
  RS.append(rs)
 return np.array(RS)
def dxweyl(w,dw,z,Y):
 ws=twoform(w);wm=-ws@U;dws=np.array([twoform(dw[a]) for a in range(5)]);wss=np.sum((U@ws@U.T)*ws)
 return twoform(z)+1j/8*C*Y-1.5j*sum(G[a]@dws[a].T for a in range(5))-2j*wm@ws.T+.5j*C*wss-.5j*sum(dws[a]@G[a].T for a in range(5))
def ddx1(w,dw,z,Y):
 ws=twoform(w);wm=-ws@U;dws=np.array([twoform(dw[a]) for a in range(5)]);rs=RSkernel(w,dw,z);dx=dxweyl(w,dw,z,Y);T=np.array([(3*eta[a]*G[a]@wm-wm@(eta[a]*G[a]))/4 for a in range(5)])
 out=np.zeros((4,4),complex)
 for al,be in it.product(range(4),repeat=2):
  out[al,be]=-4j*sum(G[a,be,r]*dws[a,al,r] for a,r in it.product(range(5),range(4)))
  out[al,be]+=-4j*sum(G[a,be,r]*(T[a]@ws)[al,r] for a,r in it.product(range(5),range(4)))
  out[al,be]+=4*sum(G[a,be,r]*(rs[a]@C)[al,r] for a,r in it.product(range(5),range(4)))
  out[al,be]+=2j*sum(ws[be,r]*U[r,s]*ws[al,s] for r,s in it.product(range(4),repeat=2))
  out[al,be]+=-1.5*dx[al,be]
 return out
boxl=[[{1<<(96+2*a+i):1} for i in range(2)] for a in range(4)]
def input2():
 p=inputs();p.update(dw=np.zeros((5,5,5)),z=np.zeros((2,2,5,5)),Y=0,box=False);return p

def p2parts(F,X,v,W,dx,df,h,der,wy,ww,dw,z,Y,box=False,detail=False):
 ws=twoform(W);wm=-ws@U;fs=twoform(F);fu=U@fs@U.T;wu=U@ws@U.T;dws=np.array([twoform(dw[a]) for a in range(5)])
 d0=dl if der else [[[{} for i in range(2)] for r in range(4)] for a in range(5)]
 yy=y if wy else [[{} for i in range(2)] for r in range(4)];uy=yu if wy else [[{} for i in range(2)] for r in range(4)]
 www=w3 if ww else {k:{} for k in w3};Q0=-2*fs-C*X[0,1]-sum(v[a]*GD[a] for a in range(5));Q1=-2*ws;R0=Rplus(ws,der)
 RW={(a,b,r):add(scale(-1.5*C[a,b],yy[r][0]),scale(-.5*C[a,r],yy[b][0]),scale(.5*C[b,r],yy[a][0])) for a,b,r in it.product(range(4),repeat=3)}
 RS=RSkernel(W,dw,z[0,1]);RSpp=RSkernel(zero(),dw*0,z[0,0]);DXw=dxweyl(W,dw,z[0,1],Y);DXp=twoform(z[0,0]);T=np.array([(3*eta[a]*G[a]@wm-wm@(eta[a]*G[a]))/4 for a in range(5)])
 dbx=[];dwf=[];dtx=[]
 for al in range(4):
  # D+ Box W at coefficient of explicit scalar W^0.
  dbox=add(scale(1j,boxl[al][0]) if box else {},*[scale(2j*eta[a]*T[a,al,t],d0[a][t][0]) for a,t in it.product(range(5),range(4))],*[scale(1j*eta[a]*((3*eta[a]*G[a]@(-dws[a]@U)-(-dws[a]@U)@(eta[a]*G[a]))/4)[al,t],ll[t][0]) for a,t in it.product(range(5),range(4))],*[scale(1j*eta[a]*(T[a]@T[a])[al,t],ll[t][0]) for a,t in it.product(range(5),range(4))],*[scale(.25*G[a,al,t]*v[a],yy[t][0]) for a,t in it.product(range(5),range(4))],*[scale(eta[a]*(RSpp[a]@(eta[a]*G[a]))[al,t],ll[t][1]) for a,t in it.product(range(5),range(4))],*[scale(-eta[a]*(RS[a]@(eta[a]*G[a]))[al,t],ll[t][0]) for a,t in it.product(range(5),range(4))])
  dbx.append(dbox)
  DWsp={(b,c):add(www[al,b,c,0],scale(.5*C[al,b],yy[c][0]),scale(.5*C[al,c],yy[b][0])) for b,c in it.product(range(4),repeat=2)}
  DFsp={}
  for b,c in it.product(range(4),repeat=2):
   DFsp[b,c]=add(*[scale(-.5j*(GD[a,al,b]*int(t==c)+GD[a,al,c]*int(t==b)+C[al,b]*G[a,c,t]+C[al,c]*G[a,b,t]),d0[a][t][0]) for a,t in it.product(range(5),range(4))],scale(-1.5j*ws[b,c],ll[al][0]),scale(.25j*ws[al,b],ll[c][0]),scale(.25j*ws[al,c],ll[b][0]),*[scale(-.75j*(C[al,b]*wm[c,t]+C[al,c]*wm[b,t]),ll[t][0]) for t in range(4)])
  dwf.append(add(*[scale(2*fu[b,c],DWsp[b,c]) for b,c in it.product(range(4),repeat=2)],*[scale(2*wu[b,c],DFsp[b,c]) for b,c in it.product(range(4),repeat=2)]))
  w2=sum(eta[a]*eta[b]*W[a,b]**2 for a,b in it.product(range(5),repeat=2))
  dtx.append(add(scale(-8j,dbox),scale(8j,dwf[-1]),*[scale(5j*(DXp@U.T)[al,r],ll[r][1]) for r in range(4)],*[scale(-5j*Q0[al,r],uy[r][0]) for r in range(4)],*[scale(-9j*(DXw@U.T)[al,r],ll[r][0]) for r in range(4)],scale(-9j*X[0,0],yy[al][1]),scale(.75*Y-31/4*w2,ll[al][0])))
 # D++ X-- at scalar degree zero from S2-73/S2-74.
 dpx=add({0:-8j*sum(eta[a]*h[a,a] for a in range(5))+8j*sum(eta[a]*eta[b]*W[a,b]*F[a,b] for a,b in it.product(range(5),repeat=2))},*[scale(5j,prod(uy[a][0],ll[a][1])) for a in range(4)],*[scale(-9j,prod(uy[a][1],ll[a][0])) for a in range(4)])
 # D+ D++ lambda^- coefficient from S2-72.
 TP={}
 for al,r in it.product(range(4),repeat=2):
  TP[al,r]=add({0:4j*sum(GD[a,al,r]*dx[a,0,0] for a in range(5))-8j*ws[al,r]*X[0,0]},*[scale(-8j,prod(www[al,r,t,0],lu[t][0])) for t in range(4)],*[scale(1j*C[al,r],prod(uy[t][0],ll[t][0])) for t in range(4)],scale(2j,prod(yy[al][0],ll[r][0])),scale(-2j,prod(yy[r][0],ll[al][0])))
 DL=[add(scale(1j*X[0,0],yy[r][0]),*[scale(-1j*DXp[r,t],lu[t][0]) for t in range(4)]) for r in range(4)]
 dd1=ddx1(W,dw,z[0,1],Y)
 parts=[add(*[scale(-3/8*X[0,0],prod(lu[a][0],yy[a][1])) for a in range(4)]),add(*[scale(-eps4(a,b,c,d)*dd1[c,d]/16,prod(ll[a][0],ll[b][0])) for a,b,c,d in it.product(range(4),repeat=4)]),scale(1j*X[0,0]/16,dpx),add(*[scale(-1j/16,prod(lu[a][0],dtx[a])) for a in range(4)])]
 b22a=[];b22b=[];b13a=[];b13b=[];b13c=[];DB1=[];DB2=[];DB3=[]
 for a,b,c,d in it.product(range(4),repeat=4):
  e=eps4(a,b,c,d)
  if not e:continue
  ddb1=add(*[scale(-2,prod(RW[c,d,r],lu[r][1])) for r in range(4)],{0:-2*sum(Q1[d,r]*U[r,s]*Q0[c,s]+Q0[d,r]*U[r,s]*Q1[c,s] for r,s in it.product(range(4),repeat=2))})
  ddb2=-2*sum(Q1[d,r]*U[r,s]*Q1[c,s] for r,s in it.product(range(4),repeat=2))
  b22a.append(scale(-X[0,0]*e*C[a,b]/64,ddb1));b22b.append(scale(-3j*e*ddb2/64,prod(ll[a][0],ll[b][0])))
  b13b.extend(scale(e*U[r,s]*Q1[d,s]/16,prod(ll[a][0],R0[b,c,r])) for r,s in it.product(range(4),repeat=2))
  b13c.extend(scale(e*U[r,s]*Q0[d,s]/16,prod(ll[a][0],RW[b,c,r])) for r,s in it.product(range(4),repeat=2))
  DB3.extend(scale(e*U[r,s]/16,prod(R0[a,b,r],R0[c,d,s])) for r,s in it.product(range(4),repeat=2))
 b13a=[scale(DXp[a,r]/4,prod(lu[a][0],lu[r][1])) for a,r in it.product(range(4),repeat=2)]
 DB1=[scale(-2,prod(DL[r],lu[r][1])) for r in range(4)]
 DB2=[scale(-U[d,a]*U[r,s]*Q0[d,s]/4,TP[a,r]) for a,d,r,s in it.product(range(4),repeat=4)]
 parts.extend([add(*b22a),add(*b22b),add(*b13a),add(*b13b),add(*b13c),scale(-1j/8,add(*DB1)),scale(-1j/8,add(*DB2)),scale(-1j/8,add(*DB3))])
 if detail:return {'DDX1':dd1,'D++X0':dpx,'DBox0':dbx,'DWF0':dwf,'TX0':dtx,'DeltaB0':add(*DB1,*DB2,*DB3)}
 return parts

def target2(F,X,v,W,dx,df,h,der,wy,ww,dw,z,Y,box=False):
 ws=twoform(W);w2=sum(eta[a]*eta[b]*W[a,b]**2 for a,b in it.product(range(5),repeat=2));out=[{0:.5*X[0,0]*sum(eta[a]*h[a,a] for a in range(5))+.5*sum(eta[a]*v[a]*dx[a,0,0] for a in range(5))}]
 if box:out.extend(scale(-.5j,prod(lu[a][0],boxl[a][0])) for a in range(4))
 if der:
  out.extend(scale(-.25j*eta[a],prod(dlu[a][r][0],dl[a][r][0])) for a,r in it.product(range(5),range(4)))
  for a,b,c,d,e in it.permutations(range(5)):
   out.extend(scale(3j/16*cc['eps']((a,b,c,d,e))*eta[a]*eta[b]*SU[a,b,al,be]*W[d,e],prod(ll[al][0],dl[c][be][0])) for al,be in it.product(range(4),repeat=2))
 out.extend(scale(-3j/8*GU[a,al,be]*eta[c]*dw[c,a,c],prod(ll[al][0],ll[be][0])) for a,c,al,be in it.product(range(5),range(5),range(4),range(4)))
 out.append(scale(3j/64*Y+3j/128*w2,bil(0,0)))
 for a,b,c,d,e in it.permutations(range(5)):
  out.extend(scale(-9j/256*cc['eps']((a,b,c,d,e))*eta[a]*GU[a,al,be]*W[b,c]*W[d,e],prod(ll[al][0],ll[be][0])) for al,be in it.product(range(4),repeat=2))
 if wy:
  out.extend(scale(3/8*SU[a,b,al,be]*F[a,b],prod(y[al][0],ll[be][0])) for a,b,al,be in it.product(range(5),range(5),range(4),range(4)))
  out.extend(scale(-3/8*X[0,0],prod(yu[a][k],ld[a][k])) for a,k in it.product(range(4),range(2)))
 if ww:
  # W_ab^{alpha} = epsilon^{alpha beta} (Sigma_ab)^{gamma delta} W_gamma delta beta.
  out.extend(scale(F[a,b]*SU[a,b,c,d]*U[r,t]/4,prod(w3[c,d,t,0],ll[r][0])) for a,b,c,d,r,t in it.product(range(5),range(5),range(4),range(4),range(4),range(4)))
 return add(*out)

def check_ddx1(p):
 w,dw,Y=p['W'],p['dw'],p['Y'];w2=sum(eta[a]*eta[b]*w[a,b]**2 for a,b in it.product(range(5),repeat=2))
 rhs=(-3j*Y/16+31j*w2/16)*C
 rhs+=sum(-3j*GD[a]*eta[c]*dw[c,a,c] for a,c in it.product(range(5),repeat=2))
 rhs+=sum(1j/4*eps5((a,b,c,d,e))*eta[a]*GD[a]*w[b,c]*w[d,e] for a,b,c,d,e in it.permutations(range(5)))
 assert np.array_equal(ddx1(w,dw,p['z'][0,1],Y),rhs),'D D X explicit-W coefficient'

def check_delta_lambda():
 counts=0
 for mode in ['X','Z']:
  for pair in (pairs5 if mode=='Z' else [None]):
   z=zero()
   if pair is not None:z[pair]=1;z[pair[::-1]]=-1
   zs=twoform(z);rs=RSkernel(zero(),np.zeros((5,5,5)),z)
   expected=[-5,-20,0,0,-1,2,-8] if mode=='X' else [9,0,-4,24,1,0,2]
   for rho in range(4):
    rows=[[] for _ in range(7)]
    for be,al in it.product(range(4),repeat=2):
     u=-U[be,al]
     if not u:continue
     if mode=='X':
      rows[0]+=[scale(u*1j*GD[a,al,rho]*eta[a]*G[a,be,t],y[t][0]) for a,t in it.product(range(5),range(4))]
      rows[1]+=[scale(u*(-4j)*C[be,al],y[rho][0]),scale(u*(-4j)*C[be,rho],y[al][0])]
      rows[4]+=[scale(u*1j*C[al,rho],y[be][0])]
      rows[5]+=[scale(u*2j*C[be,rho],y[al][0])]
      rows[6]+=[scale(u*(-2j)*C[be,al],y[rho][0])]
     else:
      rows[0]+=[scale(u*(-8j)*GD[a,al,rho]*rs[a,be,t],ll[t][0]) for a,t in it.product(range(5),range(4))]
      rows[2]+=[scale(u*(-4j)*zs[al,rho],ll[be][0])]
      rows[3]+=[scale(u*4j*(C[be,al]*zs[rho,t]+C[be,rho]*zs[al,t]+C[be,t]*zs[al,rho]),lu[t][0]) for t in range(4)]
      rows[4]+=[scale(u*(-1j)*C[al,rho]*zs[be,t],lu[t][0]) for t in range(4)]
      rows[5]+=[scale(u*2j*zs[be,al],ll[rho][0])]
      rows[6]+=[scale(u*(-2j)*zs[be,rho],ll[al][0])]
    basis=scale(1j,y[rho][0]) if mode=='X' else add(*[scale(1j*zs[rho,t],lu[t][0]) for t in range(4)])
    for n,row in enumerate(rows):assert add(*row)==scale(expected[n],basis),(mode,pair,rho,n)
    counts+=7
 return counts

def main():
 import json,hashlib,time
 start=time.monotonic();counts={}
 def check(p,group):
  assert add(*p2parts(**p))==target2(**p),group
  check_ddx1(p);counts[group]=counts.get(group,0)+1
 def putform(p,key,pair):p[key][pair]=1;p[key][pair[::-1]]=-1
 for field in ['box','der','wy','ww']:
  p=input2();p[field]=True;check(p,'single odd channels')
 p=input2();p['Y']=1;check(p,'Y')
 for a,b in it.product(range(5),repeat=2):
  p=input2();p['X'][0,0]=1;p['h'][a,b]=1;check(p,'ordered Hessian')
 for a,b,(i,j) in it.product(range(5),range(5),[(0,0),(0,1),(1,1)]):
  p=input2();p['v'][a]=1;p['dx'][b,i,j]=p['dx'][b,j,i]=1;check(p,'gradient W times gradient X')
 for n,ab in enumerate(pairs5):
  for cd in pairs5[n:]:
   p=input2();putform(p,'W',ab);putform(p,'W',cd);check(p,'W quadratic polarization')
  for odd in ['der','wy','ww']:
   p=input2();putform(p,'W',ab);p[odd]=True;check(p,'W and odd channels')
  for odd in ['wy','ww']:
   p=input2();putform(p,'F',ab);p[odd]=True;check(p,'F and Weyl fermions')
  for a in range(5):
   p=input2();p['dw'][(a,*ab)]=1;p['dw'][(a,*ab[::-1])]=-1;check(p,'uncontracted derivative W')
  for i,j in [(0,0),(0,1),(1,1)]:
   p=input2();p['z'][(i,j,*ab)]=p['z'][(j,i,*ab)]=1;p['z'][(i,j,*ab[::-1])]=p['z'][(j,i,*ab[::-1])]=-1;check(p,'Weyl tensor descendant cancellation')
  for cd in pairs5:
   p=input2();putform(p,'W',ab);putform(p,'F',cd);p['X'][0,0]=1;check(p,'X W F cancellation')
 for i,j in [(0,0),(0,1),(1,1)]:
  p=input2();p['X'][i,j]=p['X'][j,i]=1;p['wy']=True;check(p,'X and Weyl spinor')
 for a in range(5):
  p=input2();p['v'][a]=1;p['wy']=True;check(p,'gradient W and Weyl spinor cancellation')
 p=input2();p.update(der=True,wy=True,ww=True,box=True,Y=3)
 for n,ab in enumerate(pairs5):
  p['W'][ab]=(n%3)-1;p['W'][ab[::-1]]=-p['W'][ab];p['F'][ab]=(n%5)-2;p['F'][ab[::-1]]=-p['F'][ab]
 p['X']=np.array([[2,3],[3,-1]]);p['v']=np.arange(5)-2;p['h']=np.arange(25).reshape(5,5);p['dx'][:,0,0]=np.arange(5)
 check(p,'combined nonzero fields')
 report={'status':'PASS','date':'2026-09-23','scope':'Complete W^-2 projected coefficient; no claim for full-primary S/K/linearity or reality',
 'source_agreement':'12 of 12 printed W^-2 terms agree; W^-3 discrepancy unchanged',
 'arithmetic':'Exact equality of Gaussian dyadic exterior-polynomial coefficients; no fitting',
 'basis_probes':counts,'total_basis_probes':sum(counts.values()),'delta_lambda_row_checks':check_delta_lambda(),
 'uncontracted_DDX_explicit_W_checks':sum(counts.values()),'elapsed_seconds':round(time.monotonic()-start,2),
 'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
 out=HERE.parent/'sources/step2/w2_checks.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))
if __name__=='__main__':main()
