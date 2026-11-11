"""Scalar descent source-rule extension. Exact rational graded algebra; no EOM/IBP."""
import log_step3_covariant_rules as a
from log_step3_covariant_rules import *
old_D0=a.D0
old_S=a.Sgen
GEOM={'T','RM','RD','RJ','RS','RK'}

def dpoly(p,s,r,raw=False):
 out=P()
 for c,fs in P(p).ts:
  parity=0
  for n,f in enumerate(fs):
   if f.name in const:continue
   df=P(replace(f,oddD=(dn(s),up(r)))) if raw else D(f,s,r)
   out+=P.terms([(c*((-1)**parity),fs[:n])])*df*P.terms([(C(Q(1)),fs[n+1:])])
   parity+=f.parity
 return out

def natural(f,signs):
 pre=P(1);ix=list(f.ix)
 for n,(x,sg) in enumerate(zip(ix,signs)):
  if x[0]==sg:continue
  y=fresh(x[1]);ix[n]=sg+y
  pre*=eps(x,x[0]+y) if x[1] in 'su' else met(x,x[0]+y)
 return pre,replace(f,ix=tuple(ix))

def geometry(f):
 """C24 A.3. All ordered vector derivatives are distributed explicitly."""
 if f.name not in GEOM:return P(f)
 if f.ds:
  out=geometry(replace(f,ds=()))
  for d in reversed(f.ds):out=vec(d,out)
  return out
 pre,f=natural(f,{'T':'--+','RD':'--+','RJ':'--+++','RM':'--+++','RS':'--+++','RK':'--++'}[f.name])
 ix=[x[1:] for x in f.ix];b,s=ix[:2]
 c,d,e,h=[fresh('l') for _ in range(4)];t,v,z=[fresh('s') for _ in range(3)]
 G=lambda b,s,t:field('G',b,s,t)
 S=lambda b,c,s,t:field('S',b,c,s,t)
 w=lambda b,c:field('w',b,c)
 ws=lambda b,c:field('ws',b,c)
 W3=lambda b,c,s,r:field('w3a',b,c,s,r)
 x=lambda s,r:field('x',s,r)
 def tw(b,c,d):
  e,h=fresh('l'),fresh('l')
  return Q(1,2)*field('eps5',b,c,d,dn(e),dn(h))*w(up(e),up(h))
 out=P()
 if f.name=='T':
  u=ix[2];out=Q(3,4)*G(dn(b),dn(s),up(t))*ws(dn(t),up(u))-Q(1,4)*ws(dn(s),up(t))*G(dn(b),dn(t),up(u))
 else:
  r=ix[2]
  if f.name=='RD':out=-Q(1,4)*G(dn(b),dn(s),up(t))*x(dn(t),up(r))
  elif f.name=='RJ':
   k,l=ix[3:];out=-Q(3,8)*G(dn(b),dn(s),up(t))*(eps(up(r),up(k))*x(dn(t),up(l))+eps(up(r),up(l))*x(dn(t),up(k)))
  elif f.name=='RM':
   c,d=ix[3:]
   out=-G(dn(b),dn(s),up(t))*W3(up(c),up(d),dn(t),up(r))-Q(1,4)*field('eps5',dn(b),up(c),up(d),up(e),up(h))*W3(dn(e),dn(h),dn(s),up(r))
   out+=Q(1,4)*(delta(dn(b),up(c))*G(up(d),dn(s),up(t))-delta(dn(b),up(d))*G(up(c),dn(s),up(t)))*x(dn(t),up(r))
  elif f.name=='RS':
   u,k=ix[3:];ep=eps(up(r),up(k))
   out=Q(1,16)*field('za',dn(c),dn(d),up(r),up(k))*(S(up(c),up(d),dn(s),up(t))*G(dn(b),dn(t),up(u))-2*G(dn(b),dn(s),up(t))*S(up(c),up(d),dn(t),up(u)))
   # Antisymmetrization nabla_[b W_cd] has three cyclic terms, each 1/3.
   out+=-I*Q(1,8)*ep*(vec(dn(b),w(dn(c),dn(d)))+vec(dn(c),w(dn(d),dn(b)))+vec(dn(d),w(dn(b),dn(c))))*S(up(c),up(d),dn(s),up(u))
   out+=-I*Q(1,8)*ep*vec(dn(d),w(up(d),up(c)))*S(dn(c),dn(b),dn(s),up(u))
   out+=I*Q(3,16)*ep*vec(up(d),w(dn(d),dn(b)))*delta(dn(s),up(u))
   out+=-I*Q(1,8)*ep*vec(up(c),tw(dn(c),dn(b),up(d)))*G(dn(d),dn(s),up(u))
   out+=I*Q(1,16)*ep*tw(up(c),up(d),up(e))*w(dn(d),dn(e))*S(dn(c),dn(b),dn(s),up(u))
   out+=-I*Q(3,32)*ep*tw(dn(b),dn(d),dn(e))*w(up(d),up(e))*delta(dn(s),up(u))
   out+=I*Q(1,4)*ep*w(dn(b),dn(d))*w(up(c),up(d))*G(dn(c),dn(s),up(u))
   out+=-I*Q(3,64)*ep*w(up(c),up(d))*w(dn(c),dn(d))*G(dn(b),dn(s),up(u))
  elif f.name=='RK':
   c=ix[3]
   out=Q(1,6)*G(up(c),dn(s),up(t))*vec(up(d),W3(dn(d),dn(b),dn(t),up(r)))+Q(1,12)*G(dn(b),dn(s),up(t))*vec(up(d),W3(dn(d),up(c),dn(t),up(r)))
   out+=Q(1,6)*G(up(d),dn(s),up(t))*vec(dn(d),W3(dn(b),up(c),dn(t),up(r)))-Q(1,24)*field('eps5',dn(b),up(c),up(d),up(e),up(h))*vec(dn(d),W3(dn(e),dn(h),dn(s),up(r)))
   out+=Q(1,8)*G(up(c),dn(s),up(t))*vec(dn(b),x(dn(t),up(r)))
   out+=Q(1,64)*w(up(d),up(e))*(3*G(dn(b),dn(s),up(v))*S(dn(d),dn(e),dn(v),up(z))*G(up(c),dn(z),up(t))-S(dn(d),dn(e),dn(s),up(v))*G(dn(b),dn(v),up(z))*G(up(c),dn(z),up(t)))*x(dn(t),up(r))
   out+=-Q(1,48)*tw(dn(b),dn(d),dn(e))*G(up(c),dn(s),up(t))*W3(up(d),up(e),dn(t),up(r))
   out+=Q(1,8)*delta(dn(b),up(c))*w(up(d),up(e))*W3(dn(d),dn(e),dn(s),up(r))
   out+=Q(1,12)*S(dn(b),up(c),dn(s),up(t))*W3(dn(d),dn(e),dn(t),up(r))*w(up(d),up(e))
   out+=-Q(1,12)*w(up(d),up(e))*S(dn(d),dn(e),dn(s),up(t))*W3(dn(b),up(c),dn(t),up(r))
   out+=Q(13,48)*w(dn(b),dn(d))*W3(up(d),up(c),dn(s),up(r))+Q(11,48)*W3(dn(b),dn(d),dn(s),up(r))*w(up(d),up(c))
   out+=-Q(13,96)*G(dn(b),dn(s),up(t))*W3(dn(d),dn(e),dn(t),up(r))*tw(up(d),up(e),up(c))
 return pre*out

def expand_geometry(p):
 out=P()
 for c,fs in P(p).ts:
  q=P(c)
  for f in fs:q*=geometry(f)
  out+=q
 return out

def D0(f,s,r):
 if f.name in GEOM:return dpoly(geometry(f),s,r)
 if f.name!='w4':return old_D0(f,s,r)
 pre,f=variance_lower(f);qs=[x[1:] for x in f.ix]
 b=fresh('l');t=fresh('s');out=P()
 for j,k,l,m in itertools.permutations(qs):
  out+=-I*Q(1,6)*field('G',up(b),dn(s),dn(j))*vec(dn(b),field('w3',dn(k),dn(l),dn(m),up(r)))
  out+=-I*Q(1,4)*field('w3',dn(s),dn(j),dn(k),up(r))*field('ws',dn(l),dn(m))
  out+=I*Q(1,4)*field('ws',dn(s),dn(j))*field('w3',dn(k),dn(l),dn(m),up(r))
  out+=I*Q(1,4)*eps(dn(s),dn(j))*field('ws',dn(k),dn(l))*field('x',dn(m),up(r))
  out+=-I*Q(1,2)*eps(dn(s),dn(j))*field('G',up(b),dn(k),up(t))*vec(dn(b),field('w3',dn(l),dn(m),dn(t),up(r)))
  out+=-I*Q(1,4)*eps(dn(s),dn(j))*field('ws',dn(k),up(t))*field('w3',dn(l),dn(m),dn(t),up(r))
 return pre*out

def Sgen(f,s,k):
 if f.ds:
  b,*rest=f.ds;u=replace(f,ds=tuple(rest));t,l,c,v=fresh('s'),fresh('u'),fresh('l'),fresh('s')
  # C24 A.1l source repair, 2026-09-25: both K coefficients carry i.
  # Exact source-local SDD Jacobi proof: certification_20260925/curved/
  # jacobi-SDD-checks.json (48 complete basis inputs, 122880 components).
  # The cached printed source is preserved; do not import its real factors.
  return vec(b,Sgen(u,s,k))+I*field('G',b,dn(s),up(t))*eps(dn(k),dn(l))*D(u,t,l)-Q(1,4)*field('w',b,up(c))*field('G',dn(c),dn(s),up(t))*Sgen(u,t,k)+I*Q(1,8)*field('G',b,dn(s),up(t))*field('G',up(c),dn(t),up(v))*field('x',dn(v),dn(k))*K(u,c)-I*Q(1,4)*field('w3a',b,up(c),dn(s),dn(k))*K(u,c)
 if f.name not in ['w3','w3a','z','za','Y','w4']:return old_S(f,s,k)
 pre,f=variance_lower(f);qs=[x[1:] for x in f.ix];out=P()
 if f.name=='Y':out=8*I*field('x',dn(s),dn(k))
 elif f.name=='w3':
  b,c,d,j=qs
  for bb,cc,dd in [(b,c,d),(c,b,d),(d,b,c)]:out+=2*delta(up(j),dn(k))*eps(dn(s),dn(bb))*field('ws',dn(cc),dn(dd))
 elif f.name=='w4':
  for n,b in enumerate(qs):out+=6*eps(dn(s),dn(b))*field('w3',*(dn(c) for c in qs[:n]+qs[n+1:]),dn(k))
 elif f.name=='z':
  b,c,j,l=qs
  for jj,ll in [(j,l),(l,j)]:
   out+=-2*delta(up(jj),dn(k))*field('w3',dn(s),dn(b),dn(c),up(ll))
   out+=delta(up(jj),dn(k))*(eps(dn(s),dn(b))*field('x',dn(c),up(ll))+eps(dn(s),dn(c))*field('x',dn(b),up(ll)))
 elif f.name in ['w3a','za']:
  b,c,*_=qs;t,v=fresh('s'),fresh('s')
  out=field('S',dn(b),dn(c),up(t),up(v))*Sgen(field({'w3a':'w3','za':'z'}[f.name],dn(t),dn(v),*f.ix[2:]),s,k)
 return pre*out

def K(f,c):
 if not f.ds:return P()
 b,*rest=f.ds
 if b[0]=='+':
  h=fresh('l');return met(b,up(h))*K(replace(f,ds=(dn(h),)+tuple(rest)),c)
 u=replace(f,ds=tuple(rest))
 return vec(b,K(u,c))+2*u.weight*met(dn(c),b)*u+2*M(u,c,b[1:])

def comm(f,b,s,r):
 t=fresh('s');c,d=fresh('l'),fresh('l');k,l=fresh('u'),fresh('u')
 return (field('T',b,dn(s),up(t))*D(f,t,r)+Q(1,2)*field('RM',b,dn(s),up(r),up(c),up(d))*M(f,c,d)+f.weight*field('RD',b,dn(s),up(r))*f+field('RJ',b,dn(s),up(r),up(k),up(l))*J(f,k,l)+field('RS',b,dn(s),up(r),up(t),up(k))*Sgen(f,t,k)+field('RK',b,dn(s),up(r),up(c))*K(f,c))

def D(f,s='sZ',r='uT'):
 if f.oddD:raise ValueError('unresolved spinor derivative')
 if f.name in GEOM:return dpoly(geometry(f),s,r)
 if f.name in const:return P()
 if f.name=='pow':return f.power*I*pw(f.power-1)*field('L',dn(s),up(r))
 if not f.ds:return D0(f,s,r)
 b,*rest=f.ds;u=replace(f,ds=tuple(rest))
 return vec(b,D(u,s,r))+comm(u,b,s,r)

def trace(p):
 # F=-i/12 eps^{eta zeta} eps_{ti} eps_{jr} D_zeta^t D_eta^r H^{ij}
 return -I*Q(1,12)*eps(up('sE'),up('sZ'))*eps(dn('uT'),dn('uI'))*eps(dn('uJ'),dn('uR'))*p

if __name__=='__main__':
 inputs=make_inputs();count=0
 for key,p in inputs.items():
  spin=a.deriv(p);expanded=expand_geometry(spin)
  check(expanded,Q(7,2),{'sE':'-','uR':'+','uI':'+','uJ':'+'})
  scalar=trace(dpoly(expanded,'sZ','uT'))
  check(scalar,Q(4),{});check(normalize(scalar,True),Q(4),{})
  count+=len(scalar.ts);print(key,len(spin.ts),len(expanded.ts),len(scalar.ts),flush=True)
 print('TOTAL',count)
