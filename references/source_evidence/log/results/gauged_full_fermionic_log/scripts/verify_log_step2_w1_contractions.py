#!/usr/bin/env python3
"""Check the individual W^-1 hand tables against raw source contractions.

Fixed rational entries are checked, never solved for. Coordinates of W_ab,
F_ab and their derivatives in the arrays are lower Lorentz indices.
"""
import runpy
from pathlib import Path
HERE=Path(__file__).resolve().parent
ns=runpy.run_path(str(HERE/'verify_log_step2_w1.py'))
globals().update({k:v for k,v in ns.items() if not k.startswith('__')})
# All inputs below have exactly representable Gaussian dyadic coefficients.
A=add(*[scale(GU[a,r,t],prod(y[r][0],dl[a][t][0])) for a,r,t in it.product(range(5),range(4),range(4))])
B=add(*[scale(GU[a,r,t],prod(ll[r][0],dy[a][t][0])) for a,r,t in it.product(range(5),range(4),range(4))])
def basis(p):
 w=p['W'];w2=sum(eta[a]*eta[b]*w[a,b]**2 for a,b in it.product(range(5),repeat=2))
 WW=add(*[scale(w[a,b]*U[r,t],prod(wab(a,b,t),ll[r][0])) for a,b,r,t in it.product(range(5),range(5),range(4),range(4))])
 SY=add(*[scale(SU[a,b,r,t]*w[a,b],prod(y[r][0],ll[t][0])) for a,b,r,t in it.product(range(5),range(5),range(4),range(4))])
 return [A,B,WW,SY,scale(p['X'][0,0]*w2,{0:1}),scale(sum(eta[a]*eta[b]*p['F'][a,b]*p['z'][0,0,a,b] for a,b in it.product(range(5),repeat=2)),{0:1}),scale(p.get('boxX',0),{0:1}),scale(p['Y']*p['X'][0,0],{0:1})]
# Columns A, B, W W3 lambda, Sigma W X lambda, X W^2, F Z, Box X, X Y.
BOX=[
 [1/4,-3/8,-27/32,3/32,9/16,3j/8,-4,0],
 [1/2,0,-7/2,-1/2,11/4,0,0,0],
 [0,3/8,0,-3/16,0,0,0,0],
 [0,0,0,0,0,3j/8,0,0],
 [0,0,-9/32,-9/32,9/16,0,0,0],
 [0,9/8,9/16,9/8,0,0,0,0],
 [0,-9/8,0,9/16,0,0,0,0],
 [-1/4,0,0,7/16,0,0,0,0],
 [0,0,-1/16,0,0,0,0,0]] # each row is multiplied by i
DELTA=[[-1/8,0,33/32,-5/16,-31/32,-3j/16,1,0],[2,0,-2,1/2,2,1j,0,0],[-5/8,0,0,-25/32,0,-5j/16,0,0],[0,-9/8,0,9/16,0,0,0,-9/32],[0,3/8,31/32,25/32,-31/32,0,0,3/32]]
PRIMARY=[[-5/8,3/8,0,-3/8,-1/32,-1j/4,-1/2,3/32],[0,0,0,0,-31/64,0,0,3/64],[0,3/8,1/2,15/32,0,0,0,0],[0,0,0,0,1/8,0,0,0],[0,0,0,3/16,0,0,0,0],[0,0,-1/4,0,1/4,-1j/8,0,0],[-1/8,0,0,-9/32,0,0,0,0]]
WF=[[0,0,0,0,0,-4,0,0],[0,0,-6j,-2j,8j,0,0,0],[8j,0,-2j,4j,0,0,0,0]]
def checkrows(raw,table,bs,label,factor=1):
 for n,(r,cs) in enumerate(zip(raw,table)):
  assert add(r)==add(*[scale(factor*c,b) for c,b in zip(cs,bs)]),(label,n)
 assert len(raw)==len(table)
 return len(raw)
def wfrows(d):
 fs=d['c']['fs'];ws=d['ws'];DF,DDF,DDW=[d[k] for k in ['DF','DDF','DDW']]
 return [add(*[scale(-2*U[a,b]*(U@fs@U.T)[r,s],{0:DDW[a,b,r,s]}) for a,b,r,s in it.product(range(4),repeat=4)]),add(*[scale(-2*U[a,b]*(U@ws@U.T)[r,s],DDF[a,b,r,s]) for a,b,r,s in it.product(range(4),repeat=4)]),add(*[scale(-4*U[a,b]*U[r,t]*U[s,u],prod(DW(a,t,u),DF[b,r,s])) for a,b,r,s,t,u in it.product(range(4),repeat=6)])]
def extra_rows(p,c):
 w=p['W'];ws=c['ws'];wm=c['wm']
 rw={(a,b,r):add(scale(-1.5*C[a,b],y[r][0]),scale(-.5*C[a,r],y[b][0]),scale(.5*C[b,r],y[a][0])) for a,b,r in it.product(range(4),repeat=3)}
 r0={}
 for a,b,r in it.product(range(4),repeat=3):
  ts=[[],[],[],[],[],[],[scale(1j*ws[b,r],ll[a][0])],[scale(-1j*ws[a,r],ll[b][0])],[scale(-3j*C[a,b]*ws[r,t],lu[t][0]) for t in range(4)]]
  for v,t in it.product(range(5),range(4)):
   for j,q in enumerate([GD[v,a,b]*int(t==r),GD[v,a,r]*int(t==b),C[a,b]*G[v,r,t],C[a,r]*G[v,b,t],-C[b,r]*G[v,a,t],-GD[v,b,r]*int(t==a)]):ts[j].append(scale(1j*q,dl[v][t][0]))
  r0[a,b,r]=[add(*v) for v in ts]
 rr=[add(*[scale(-1j*eps4(a,b,c0,d)*U[r,s]/128,add(prod(r0[a,b,r][n],rw[c0,d,s]),prod(rw[a,b,r],r0[c0,d,s][n]))) for a,b,c0,d in it.permutations(range(4)) for r,s in it.product(range(4),repeat=2)]) for n in range(9)]
 bs=basis(p);n=checkrows(rr,[[-1/32,0],[5/64,0],[-7/32,0],[-1/64,0],[-1/64,0],[5/64,0],[0,3/128],[0,3/128],[0,-21/64]],[bs[0],bs[3]],'RR')
 tab=[]
 for rho in range(4):
  rows=[[] for _ in range(7)]
  for a,b in it.product(range(4),repeat=2):
   e=-U[a,b];rows[0].append(scale(e,c['dz'][a,b,rho]));rows[1].append(scale(e*1j*C[b,rho]/8,c['dyd'][a]));rows[6].append(scale(e*.25j*C[b,rho],c['dw2'][a]))
   for v,t in it.product(range(5),range(4)):
    rows[2].append(scale(e*-1.5j*G[v,b,t],c['ddw'][a,v,rho,t]));rows[3].append(scale(e*-.5j*G[v,rho,t],c['ddw'][a,v,b,t]))
   for t,s in it.product(range(4),repeat=2):rows[4].append(scale(e*2j*U[s,t]*ws[rho,t],DW(a,b,s)))
   for t in range(4):rows[5].append(scale(e*-2j*wm[b,t],DW(a,rho,t)))
  bases=[add(*[scale(1j*G[v,rho,t],dy[v][t][0]) for v,t in it.product(range(5),range(4))]),add(*[scale(1j*wm[rho,t],y[t][0]) for t in range(4)]),add(*[scale(1j*w[v,z0],wab(v,z0,rho)) for v,z0 in it.product(range(5),repeat=2)])]
  n+=checkrows([add(*r) for r in rows],[[-1,-1,0],[-1,-1,0],[-3/4,-21/4,-3/4],[-5/4,1/4,1/4],[0,5,0],[0,-1,1],[0,-1,-1/2]],bases,'trace X Weyl')
  raw=add(*[c['rk'][a,rho,a] for a in range(5)])
  expected=add(*[scale(12*G[a,rho,t],dy[a][t][0]) for a,t in it.product(range(5),range(4))],*[scale(3*w[a,b]*S[a,b,rho,t],y[t][0]) for a,b,t in it.product(range(5),range(5),range(4))],*[scale(-3*w[a,b],wab(a,b,rho)) for a,b in it.product(range(5),repeat=2)])
  assert raw==expected,('96 RK trace',rho)
  n+=1
 return n

def main():
 import json,hashlib,time
 start=time.monotonic();counts={'DppBox_rows':0,'DeltaX_rows':0,'primary_rows':0,'WF_rows':0,'RR_Weyl_trace_K_rows':0,'matrix_identities':0}
 ps=[input2()]
 for ab in pairs5:
  p=input2();p['W'][ab]=1;p['W'][ab[::-1]]=-1;ps.append(p)
 for label in ['XY','XWW','FZ','box']:
  p=input2()
  if label in ['XY','XWW']:p['X'][0,0]=1
  if label=='XY':p['Y']=1
  if label=='XWW':p['W'][0,1]=1;p['W'][1,0]=-1
  if label=='FZ':p['F'][0,1]=1;p['F'][1,0]=-1;p['z'][0,0,0,1]=1;p['z'][0,0,1,0]=-1
  if label=='box':p['boxX']=1
  ps.append(p)
 for p in ps:
  d=calculate(p,True);bs=basis(p)
  counts['DppBox_rows']+=checkrows(d['DppBoxRows'],BOX,bs,'box',1j)
  counts['DeltaX_rows']+=checkrows(d['pieces'],DELTA,bs,'Delta')
  counts['primary_rows']+=checkrows(finalparts(p),PRIMARY,bs,'primary')
  counts['WF_rows']+=checkrows(wfrows(d),WF,bs,'WF')
  counts['RR_Weyl_trace_K_rows']+=extra_rows(p,d['c'])
 for n,ab in enumerate(pairs5):
  for cd in pairs5[n:]:
   w=zero();w[ab]=1;w[ab[::-1]]=-1;w[cd]=1;w[cd[::-1]]=-1
   wm=-twoform(w)@U;T=np.array([(3*eta[a]*G[a]@wm-wm@G[a]*eta[a])/4 for a in range(5)])
   w2=sum(eta[a]*eta[b]*w[a,b]**2 for a,b in it.product(range(5),repeat=2))
   ep=sum(eps5((a,b,c,d,e))*eta[a]*G[a]*w[b,c]*w[d,e] for a,b,c,d,e in it.permutations(range(5)))
   assert np.array_equal(sum(1j*eta[a]*T[a]@T[a] for a in range(5)),-5j*w2*I/32+1j*ep/64)
   rs=RSkernel(w,np.zeros((5,5,5)),zero());sm=-sum(eta[a]*rs[a]@(eta[a]*G[a]) for a in range(5))
   assert np.array_equal(sm,1j*w2*I/64-1j*ep/64)
   counts['matrix_identities']+=2
 for a,ab in it.product(range(5),pairs5):
  dw=np.zeros((5,5,5));dw[a,*ab]=1;dw[a,*ab[::-1]]=-1;dws=np.array([-twoform(dw[b])@U for b in range(5)])
  div=sum(G[b]*eta[c]*dw[c,b,c] for b,c in it.product(range(5),repeat=2));curl=sum(eps5((b,c,d,e,f))*eta[b]*eta[c]*S[b,c]*dw[d,e,f] for b,c,d,e,f in it.permutations(range(5)))
  raw=sum(1j*(3*G[b]@dws[b]-dws[b]@G[b])/4 for b in range(5))
  assert np.array_equal(raw,-.5j*div-.125j*curl)
  rs=RSkernel(zero(),dw,zero());sm=-sum(rs[b]@G[b] for b in range(5))
  assert np.array_equal(sm,-1j*div/16-1j*curl/16)
  counts['matrix_identities']+=2
 for ab in pairs5:
  z=zero();z[ab]=1;z[ab[::-1]]=-1;rs=RSkernel(zero(),np.zeros((5,5,5)),z)
  assert np.array_equal(-sum(rs[a]@G[a] for a in range(5)),3*(-twoform(z)@U)/8)
  counts['matrix_identities']+=1
 report={'date':'2026-09-23','status':'PASS','scope':'Individual W^-1 hand tables, uncontracted matrix identities, and full K-curvature trace; no full-primary certification','table_probes':len(ps),'checks':counts,'total_rows_and_matrix_identities':sum(counts.values()),'arithmetic':'Fixed Gaussian dyadic coefficients and exact polynomial equality; no fitting','elapsed_seconds':round(time.monotonic()-start,2),'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
 (HERE.parent/'sources/step2/w1_contraction_checks.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))
if __name__=='__main__':main()
