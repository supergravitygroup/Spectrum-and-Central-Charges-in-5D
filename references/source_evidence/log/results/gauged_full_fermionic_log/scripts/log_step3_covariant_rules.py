"""Transcription/formatting of the displayed source rules; no Fierz or EOM reduction."""
from dataclasses import dataclass,replace
from fractions import Fraction as Q
from collections import defaultdict,Counter
from pathlib import Path
import itertools,json,hashlib,re
@dataclass(frozen=True)
class C:
 r:Q=Q(0); i:Q=Q(0)
 def __add__(self,o):
  o=coef(o);return C(self.r+o.r,self.i+o.i)
 __radd__=__add__
 def __mul__(self,o):
  if isinstance(o,(P,A)):return P(self)*o
  o=coef(o);return C(self.r*o.r-self.i*o.i,self.r*o.i+self.i*o.r)
 __rmul__=__mul__
 def __neg__(self):return C(-self.r,-self.i)
 def __sub__(self,o):return self+-coef(o)
 def __bool__(self):return bool(self.r or self.i)
def coef(x):return x if isinstance(x,C) else C(Q(x))
I=C(Q(0),Q(1))
# Signed index strings: +s.../-s... spinor, +u.../-u... SU2, +l.../-l... Lorentz.
def up(x):return '+'+x.lstrip('+-')
def dn(x):return '-'+x.lstrip('+-')
def fresh(k):
 global counter
 counter+=1;return k+str(counter)
counter=0
spec={
 'W':('',Q(1),0),'L':('su',Q(3,2),1),'X':('uu',Q(2),0),
 'F':('ll',Q(2),0),'Fs':('ss',Q(2),0),'w':('ll',Q(1),0),'ws':('ss',Q(1),0),
 'x':('su',Q(3,2),1),'w3':('sssu',Q(3,2),1),'w3a':('llsu',Q(3,2),1),
 'z':('ssuu',Q(2),0),'za':('lluu',Q(2),0),'Y':('',Q(2),0),'w4':('ssss',Q(2),0),
 'T':('lss',Q(1),0),'RM':('lsull',Q(3,2),1),'RD':('lsu',Q(3,2),1),
 'RJ':('lsuuu',Q(3,2),1),'RS':('lsusu',Q(2),0),'RK':('lsul',Q(5,2),1),
 'eps':('',Q(0),0),'eta':('',Q(0),0),'del':('',Q(0),0),'G':('lss',Q(0),0),'S':('llss',Q(0),0),'eps5':('lllll',Q(0),0),
 'pow':('',Q(0),0),
}
const={'eps','eta','del','G','S','eps5'}
@dataclass(frozen=True)
class A:
 name:str; ix:tuple=(); ds:tuple=(); power:int=0; oddD:tuple=()
 def __mul__(self,o):return P(self)*o
 def __rmul__(self,o):return P(o)*self
 def __add__(self,o):return P(self)+o
 def __radd__(self,o):return P(o)+self
 def __neg__(self):return -P(self)
 def __sub__(self,o):return P(self)-o
 @property
 def parity(self):return (spec[self.name][2]+bool(self.oddD))%2
 @property
 def weight(self):return (Q(self.power) if self.name=='pow' else spec[self.name][1])+len(self.ds)+Q(int(bool(self.oddD)),2)
class P:
 def __init__(self,x=0):
  self.ts=x.ts.copy() if isinstance(x,P) else ([(C(Q(1)),(x,))] if isinstance(x,A) else ([(coef(x),())] if coef(x) else []))
 @classmethod
 def terms(cls,ts):
  p=cls();p.ts=[(coef(c),tuple(f)) for c,f in ts if coef(c)];return p
 def __add__(self,o):return P.terms(self.ts+P(o).ts)
 def __radd__(self,o):return P(o)+self
 def __neg__(self):return P.terms([(-c,f) for c,f in self.ts])
 def __sub__(self,o):return self+-P(o)
 def __mul__(self,o):return P.terms([(c*d,a+b) for c,a in self.ts for d,b in P(o).ts])
 def __rmul__(self,o):return P(o)*self

def atom(n,*ix):return A(n,tuple(ix))
def eps(a,b):assert a[0]==b[0] and a[1]==b[1];return atom('eps',a,b)
def met(a,b):return atom('eta',a,b)
def delta(a,b):return atom('del',a,b)
def field(n,*ix):return atom(n,*ix)
def pw(n):return A('pow',power=n) if n else P(1)
def vec(a,p):
 out=P()
 for c,fs in P(p).ts:
  for n,f in enumerate(fs):
   if f.name in const:continue
   if f.name=='pow':
    if f.power:out+=P.terms([(c*f.power,fs[:n]+(A('pow',power=f.power-1),A('W',ds=(a,)))+fs[n+1:])])
   else:out+=P.terms([(c,fs[:n]+(replace(f,ds=(a,)+f.ds),)+fs[n+1:])])
 return out

def variance_lower(f):
 """Return covariant spinor/Lorentz, contravariant SU2 field and explicit metrics."""
 pre=P(1);ix=list(f.ix)
 for n,x in enumerate(ix):
  want='+' if x[1]=='u' else '-'
  if x[0]==want:continue
  y=fresh(x[1]);ix[n]=want+y
  pre*=eps(x,up(y) if x[0]=='+' else dn(y)) if x[1] in 'su' else met(x,up(y) if x[0]=='+' else dn(y))
 return pre,replace(f,ix=tuple(ix))

def D0(f,s,r):
 """S23 2.6 and 2.13 with every weighted symmetrization expanded."""
 pre,f=variance_lower(f)
 n=f.name;q=[z[1:] for z in f.ix]
 a,b,c,d=[fresh('l') for _ in range(4)];t,v,h=[fresh('s') for _ in range(3)]
 ep=lambda i,j:eps(up(i),up(j))
 ee=lambda i,j:eps(dn(i),dn(j))
 W=field('W');G=lambda a,b,c:field('G',up(a),dn(b),up(c))
 L=lambda a,i:field('L',dn(a),up(i))
 w=lambda a,b:field('ws',dn(a),dn(b))
 x=lambda a,i:field('x',dn(a),up(i))
 F=lambda a,b:field('Fs',dn(a),dn(b))
 Z=lambda a,b,i,j:field('z',dn(a),dn(b),up(i),up(j))
 W3=lambda a,b,c,i:field('w3',dn(a),dn(b),dn(c),up(i))
 wm=lambda a,b:field('ws',dn(a),up(b))
 out=P()
 if n=='W':out=I*L(s,r)
 elif n=='L':
  b,j=q
  out=-2*ep(r,j)*F(s,b)-2*ep(r,j)*w(s,b)*W-ee(s,b)*field('X',up(r),up(j))-ep(r,j)*field('G',up(a),dn(s),dn(b))*vec(dn(a),W)
 elif n=='X':
  j,k=q
  for jj,kk in [(j,k),(k,j)]:
   out+=I*ep(r,jj)*G(a,s,t)*vec(dn(a),L(t,kk))-I*Q(1,2)*ep(r,jj)*w(s,t)*field('L',up(t),up(kk))-Q(3,4)*ep(r,jj)*x(s,kk)*W
 elif n=='ws':
  b,c=q;out=W3(s,b,c,r)+Q(1,2)*ee(s,b)*x(c,r)+Q(1,2)*ee(s,c)*x(b,r)
 elif n=='Fs':
  b,c=q
  for b,c in [(b,c),(c,b)]:
   out+=-I*Q(1,2)*field('G',up(a),dn(s),dn(b))*vec(dn(a),L(c,r))-I*Q(1,2)*ee(s,b)*G(a,c,t)*vec(dn(a),L(t,r))+I*Q(1,4)*w(s,b)*L(c,r)-I*Q(3,4)*ee(s,b)*wm(c,t)*L(t,r)
  b,c=q;out+=-I*Q(3,2)*w(b,c)*L(s,r)-W3(s,b,c,r)*W
 elif n=='x':
  b,j=q
  out=Z(s,b,r,j)+I*Q(1,8)*ep(r,j)*ee(s,b)*field('Y')-I*Q(3,2)*ep(r,j)*G(a,s,t)*vec(dn(a),w(b,t))-2*I*ep(r,j)*wm(s,t)*w(b,t)+I*Q(1,2)*ep(r,j)*ee(s,b)*field('ws',up(t),up(v))*w(t,v)-I*Q(1,2)*ep(r,j)*G(a,b,t)*vec(dn(a),w(s,t))
 elif n=='Y':out=8*G(a,s,t)*vec(dn(a),x(t,r))+8*wm(s,t)*x(t,r)
 elif n=='w3':
  b,c,d,j=q
  out=-Q(1,2)*ep(r,j)*field('w4',dn(s),dn(b),dn(c),dn(d))
  for bb,cc,dd in [(b,c,d),(c,b,d),(d,b,c)]:
   out+=-I*Q(1,2)*ep(r,j)*field('G',up(a),dn(s),dn(bb))*vec(dn(a),w(cc,dd))-Q(1,2)*ee(s,bb)*Z(cc,dd,r,j)
  for bb,cc,dd in itertools.permutations((b,c,d)):
   out+=-I*Q(1,4)*ep(r,j)*ee(s,bb)*G(a,cc,t)*vec(dn(a),w(dd,t))
 elif n=='z':
  b,c,j,k=q
  for jj,kk in [(j,k),(k,j)]:
   preu=I*Q(1,2)*ep(r,jj)
   sub=-w(s,t)*field('w3',dn(b),dn(c),up(t),up(kk))-Q(3,2)*w(b,c)*x(s,kk)+2*G(a,s,t)*vec(dn(a),W3(b,c,t,kk))
   for bb,cc in [(b,c),(c,b)]:
    sub+=-Q(3,2)*wm(bb,t)*W3(cc,s,t,kk)-Q(1,2)*ee(s,bb)*field('ws',up(t),up(v))*W3(cc,t,v,kk)+Q(1,4)*w(s,bb)*x(cc,kk)+Q(3,4)*ee(s,bb)*w(cc,t)*field('x',up(t),up(kk))+G(a,bb,t)*vec(dn(a),W3(cc,s,t,kk))-Q(1,2)*field('G',up(a),dn(s),dn(bb))*vec(dn(a),x(cc,kk))+Q(1,2)*ee(s,bb)*field('G',up(a),dn(cc),dn(t))*vec(dn(a),field('x',up(t),up(kk)))
   out+=preu*sub
 elif n in ['F','w','w3a','za']:
  b,c,*rest=q
  target={'F':'Fs','w':'ws','w3a':'w3','za':'z'}[n]
  fx=field(target,dn(t),dn(v),*f.ix[2:])
  out=field('S',dn(b),dn(c),up(t),up(v))*D0(fx,s,r)
 else:raise ValueError(('D0',f))
 return pre*out

# Generator actions on elementary fields, with geometric indices kept explicit.
def M(f,c,d):
 if f.ds:
  a,*rest=f.ds;b=a[1:];u=replace(f,ds=tuple(rest))
  if a[0]=='+':
   z=fresh('l');return met(a,up(z))*M(replace(f,ds=(dn(z),)+tuple(rest)),c,d)
  return met(dn(b),dn(c))*vec(dn(d),u)-met(dn(b),dn(d))*vec(dn(c),u)+vec(a,M(u,c,d))
 pre,f=variance_lower(f);out=P()
 for n,b in enumerate(f.ix):
  if b[1]=='s':
   t=fresh('s');out+=field('S',dn(c),dn(d),b,up(t))*replace(f,ix=f.ix[:n]+(dn(t),)+f.ix[n+1:])
  elif b[1]=='l':
   out+=met(b,dn(c))*replace(f,ix=f.ix[:n]+(dn(d),)+f.ix[n+1:])-met(b,dn(d))*replace(f,ix=f.ix[:n]+(dn(c),)+f.ix[n+1:])
 return pre*out

def J(f,k,l):
 if f.ds:return vec(f.ds[0],J(replace(f,ds=f.ds[1:]),k,l))
 pre,f=variance_lower(f);out=P()
 # J_kl U^i=-1/2(delta_k^i eps_lm+delta_l^i eps_km) U^m.
 for n,b in enumerate(f.ix):
  if b[1]=='u':
   t=fresh('u');fu=replace(f,ix=f.ix[:n]+(up(t),)+f.ix[n+1:])
   out+=-Q(1,2)*(delta(b,dn(k))*eps(dn(l),dn(t))+delta(b,dn(l))*eps(dn(k),dn(t)))*fu
 return pre*out

def Sgen(f,s,k):
 if f.ds:
  a,*rest=f.ds;u=replace(f,ds=tuple(rest));t=fresh('s');l=fresh('u');b=fresh('l')
  # Only first vector descendants of elementary K-primary fields are needed.
  assert not rest
  return vec(a,Sgen(u,s,k))+I*field('G',a,dn(s),up(t))*eps(dn(k),dn(l))*D(u,t,l)-Q(1,4)*field('w',a,up(b))*field('G',dn(b),dn(s),up(t))*Sgen(u,t,k)
 pre,f=variance_lower(f);n=f.name;q=[x[1:] for x in f.ix];out=P()
 de=lambda j:delta(up(j),dn(k))
 if n in ['W','ws','w']:return out
 if n=='L':b,j=q;out=-2*I*de(j)*eps(dn(s),dn(b))*field('W')
 elif n=='X':j,l=q;out=-de(j)*field('L',dn(s),up(l))-de(l)*field('L',dn(s),up(j))
 elif n=='x':b,j=q;out=4*de(j)*field('ws',dn(s),dn(b))
 elif n=='Fs':
  b,c=q;out=2*eps(dn(s),dn(b))*field('L',dn(c),up(k))+2*eps(dn(s),dn(c))*field('L',dn(b),up(k))
  # Source S_lower k on F uses lambda_lower k, not upper k.
  t=fresh('u');out=eps(dn(k),dn(t))*(2*eps(dn(s),dn(b))*field('L',dn(c),up(t))+2*eps(dn(s),dn(c))*field('L',dn(b),up(t)))
 elif n=='F':
  b,c=q;t,v=fresh('s'),fresh('s');out=field('S',dn(b),dn(c),up(t),up(v))*Sgen(field('Fs',dn(t),dn(v)),s,k)
 else:raise ValueError(('Sgen',f))
 return pre*out

def K(f,c):
 if not f.ds:return P()
 a,*rest=f.ds;assert not rest
 u=replace(f,ds=())
 # K_c nabla_a=2 eta_ca D+2 M_ca, raising a if needed.
 if a[0]=='+':
  b=fresh('l');return met(a,up(b))*K(replace(f,ds=(dn(b),)),c)
 return 2*u.weight*met(dn(c),a)*u+2*M(u,c,a[1:])

def comm(f,a,s,r):
 """[nabla_s^r,nabla_a] on f, including every generator action."""
 t=fresh('s');c,d=fresh('l'),fresh('l');k,l=fresh('u'),fresh('u')
 return (field('T',a,dn(s),up(t))*D(f,t,r)
  +Q(1,2)*field('RM',a,dn(s),up(r),up(c),up(d))*M(f,c,d)
  +f.weight*field('RD',a,dn(s),up(r))*f
  +field('RJ',a,dn(s),up(r),up(k),up(l))*J(f,k,l)
  +field('RS',a,dn(s),up(r),up(t),up(k))*Sgen(f,t,k)
  +field('RK',a,dn(s),up(r),up(c))*K(f,c))

def D(f,s='sE',r='uR'):
 if f.oddD:raise ValueError('no unresolved spinor derivative may enter')
 if f.name in const:return P()
 if f.name=='pow':return f.power*I*pw(f.power-1)*field('L',dn(s),up(r))
 if not f.ds:return D0(f,s,r)
 a,*rest=f.ds;u=replace(f,ds=tuple(rest))
 return vec(a,D(u,s,r))+comm(u,a,s,r)

def deriv(p,raw=False):
 out=P()
 for c,fs in P(p).ts:
  parity=0
  for n,f in enumerate(fs):
   if f.name in const:continue
   df=P(replace(f,oddD=(dn('sE'),up('uR')))) if raw else D(f)
   out+=P.terms([(c*((-1)**parity),fs[:n])])*df*P.terms([(C(Q(1)),fs[n+1:])])
   parity+=f.parity
 return out

# Human transcribed 58 monomials, with (ij) written as its two weighted terms.
def make_inputs():
 a,b,c,d,e=['l'+x for x in 'abcde'];al,be,ro,ga=['s'+x for x in ['A','B','R','G']];i,j,k,l=['u'+x for x in 'IJKL']
 L=lambda s,u:field('L',s,u)
 X=lambda u,v:field('X',u,v)
 w=lambda a,b:field('w',a,b)
 F=lambda a,b:field('F',a,b)
 x=lambda s,u:field('x',s,u)
 za=lambda a,b,u,v:field('za',a,b,u,v)
 wa=lambda a,b,s,u:field('w3a',a,b,s,u)
 G=lambda a,s,t:field('G',a,s,t)
 S=lambda a,b,s,t:field('S',a,b,s,t)
 W=field('W');Y=field('Y')
 box=lambda p:vec(up(a),vec(dn(a),p))
 def sy(f):return Q(1,2)*(f(i,j)+f(j,i))
 inputs={}
 def put(n,num,c,p):inputs[f'H{n}.{num}']=c*pw(-n)*p
 put(0,1,-I*Q(3,8),w(dn(a),dn(b))*za(up(a),up(b),up(i),up(j)))
 put(0,2,I*Q(51,64),x(up(al),up(i))*x(dn(al),up(j)))
 put(1,1,Q(9,64),X(up(i),up(j))*Y)
 put(1,2,-I*Q(3,8),F(dn(a),dn(b))*za(up(a),up(b),up(i),up(j)))
 put(1,3,-Q(1,2),box(X(up(i),up(j))))
 put(1,4,-Q(9,64),X(up(i),up(j))*w(up(a),up(b))*w(dn(a),dn(b)))
 put(1,5,Q(1,4),sy(lambda i,j:w(up(a),up(b))*wa(dn(a),dn(b),up(al),up(i))*L(dn(al),up(j))))
 put(1,6,-Q(3,4),G(up(a),up(al),up(be))*sy(lambda i,j:x(dn(al),up(i))*vec(dn(a),L(dn(be),up(j)))))
 put(1,7,Q(3,4),G(up(a),up(al),up(be))*sy(lambda i,j:L(dn(al),up(i))*vec(dn(a),x(dn(be),up(j)))))
 put(2,1,Q(1,2),X(up(i),up(j))*box(W))
 put(2,2,Q(1,2),vec(up(a),W)*vec(dn(a),X(up(i),up(j))))
 put(2,3,Q(1,4),sy(lambda i,j:F(up(a),up(b))*wa(dn(a),dn(b),up(al),up(i))*L(dn(al),up(j))))
 put(2,4,-I*Q(1,2),sy(lambda i,j:L(up(al),up(j))*box(L(dn(al),up(i)))))
 put(2,5,-I*Q(1,4),vec(up(a),L(up(al),up(i)))*vec(dn(a),L(dn(al),up(j))))
 ee=field('eps5',up(a),up(b),up(c),up(d),up(e))
 put(2,6,-I*Q(3,16),ee*S(dn(a),dn(b),up(al),up(be))*w(dn(d),dn(e))*sy(lambda i,j:L(dn(al),up(i))*vec(dn(c),L(dn(be),up(j)))))
 put(2,7,-I*Q(3,8),G(up(a),up(al),up(be))*L(dn(al),up(i))*L(dn(be),up(j))*vec(up(c),w(dn(a),dn(c))))
 put(2,8,I*Q(3,64),Y*L(up(al),up(i))*L(dn(al),up(j)))
 put(2,9,Q(3,8),S(dn(a),dn(b),up(al),up(be))*F(up(a),up(b))*sy(lambda i,j:x(dn(al),up(i))*L(dn(be),up(j))))
 put(2,10,I*Q(3,128),w(up(a),up(b))*w(dn(a),dn(b))*L(up(al),up(i))*L(dn(al),up(j)))
 put(2,11,I*Q(9,256),ee*G(dn(a),up(al),up(be))*w(dn(b),dn(c))*w(dn(d),dn(e))*L(dn(al),up(i))*L(dn(be),up(j)))
 put(2,12,-Q(3,8),X(up(i),up(j))*x(up(al),up(k))*L(dn(al),dn(k)))
 put(3,1,Q(1,8),X(up(i),up(j))*F(up(a),up(b))*F(dn(a),dn(b)))
 put(3,2,-Q(1,8),X(up(i),up(j))*X(up(k),up(l))*X(dn(k),dn(l)))
 put(3,3,-Q(1,4),X(up(i),up(j))*vec(up(a),W)*vec(dn(a),W))
 put(3,4,-I*Q(1,8),ee*S(dn(a),dn(b),up(al),up(be))*F(dn(d),dn(e))*sy(lambda i,j:L(dn(al),up(i))*vec(dn(c),L(dn(be),up(j)))))
 put(3,5,-I*Q(1,4),G(up(a),up(al),up(be))*F(dn(a),dn(b))*sy(lambda i,j:L(dn(al),up(i))*vec(up(b),L(dn(be),up(j)))))
 put(3,6,-I*Q(1,4),G(up(a),up(al),up(be))*L(dn(al),up(i))*L(dn(be),up(j))*vec(up(c),F(dn(a),dn(c))))
 put(3,7,I*Q(1,4),G(up(a),up(al),up(be))*X(up(i),up(j))*L(dn(al),up(k))*vec(dn(a),L(dn(be),dn(k))))
 put(3,8,I*Q(1,4),G(up(a),up(al),up(be))*sy(lambda i,j:X(up(k),up(i))*L(dn(al),up(j)))*vec(dn(a),L(dn(be),dn(k))))
 put(3,9,I*Q(1,4),G(up(a),up(al),up(be))*sy(lambda i,j:L(dn(al),up(i))*vec(dn(a),X(up(j),up(l))))*L(dn(be),dn(l)))
 put(3,10,I*Q(1,4),L(up(al),up(i))*L(dn(al),up(j))*box(W))
 put(3,11,I*Q(3,4),vec(up(a),W)*sy(lambda i,j:L(up(al),up(i))*vec(dn(a),L(dn(al),up(j)))))
 put(3,12,-I*Q(1,2),S(dn(a),dn(b),up(al),up(be))*vec(up(a),W)*sy(lambda i,j:L(dn(al),up(i))*vec(up(b),L(dn(be),up(j)))))
 put(3,13,-I*Q(3,16),G(up(a),up(al),up(be))*w(dn(a),dn(b))*L(dn(al),up(i))*L(dn(be),up(j))*vec(up(b),W))
 put(3,14,I*Q(3,32),w(dn(a),dn(b))*F(up(a),up(b))*L(up(al),up(i))*L(dn(al),up(j)))
 put(3,15,I*Q(9,64),ee*G(dn(a),up(al),up(be))*w(dn(b),dn(c))*F(dn(d),dn(e))*L(dn(al),up(i))*L(dn(be),up(j)))
 put(3,16,-I*Q(3,32),S(dn(a),dn(b),up(al),up(be))*X(up(i),up(j))*w(up(a),up(b))*L(dn(al),up(k))*L(dn(be),dn(k)))
 put(3,17,-I*Q(3,8),x(up(al),up(k))*sy(lambda i,j:L(dn(al),up(i))*L(up(be),up(j)))*L(dn(be),dn(k)))
 put(3,18,-I*Q(3,8),x(up(al),up(k))*L(up(be),up(i))*L(dn(be),up(j))*L(dn(al),dn(k)))
 put(4,1,-I*Q(3,16),L(up(al),up(i))*L(dn(al),up(j))*vec(up(a),W)*vec(dn(a),W))
 put(4,2,-I*Q(3,8),G(up(a),up(al),up(be))*sy(lambda i,j:X(up(k),up(i))*L(dn(al),up(j)))*L(dn(be),dn(k))*vec(dn(a),W))
 put(4,3,I*Q(3,8),G(up(a),up(al),up(be))*F(dn(a),dn(b))*L(dn(al),up(i))*L(dn(be),up(j))*vec(up(b),W))
 put(4,4,I*Q(3,32),F(up(a),up(b))*F(dn(a),dn(b))*L(up(al),up(i))*L(dn(al),up(j)))
 put(4,5,I*Q(3,64),ee*G(dn(a),up(al),up(be))*F(dn(b),dn(c))*F(dn(d),dn(e))*L(dn(al),up(i))*L(dn(be),up(j)))
 put(4,6,-I*Q(3,16),S(dn(a),dn(b),up(al),up(be))*X(up(i),up(j))*F(up(a),up(b))*L(dn(al),up(k))*L(dn(be),dn(k)))
 put(4,7,-I*Q(3,16),X(up(i),up(j))*X(up(k),up(l))*L(up(al),dn(k))*L(dn(al),dn(l)))
 put(4,8,-I*Q(3,32),X(up(k),up(l))*X(dn(k),dn(l))*L(up(al),up(i))*L(dn(al),up(j)))
 put(4,9,-Q(15,64),G(up(a),up(al),up(be))*L(dn(al),up(i))*L(dn(be),up(j))*L(up(ga),up(k))*vec(dn(a),L(dn(ga),dn(k))))
 put(4,10,-Q(9,32),G(up(a),up(al),up(be))*sy(lambda i,j:L(dn(al),up(i))*L(up(ro),up(j)))*L(dn(be),up(k))*vec(dn(a),L(dn(ro),dn(k))))
 put(4,11,-Q(15,32),G(up(a),up(al),up(be))*sy(lambda i,j:L(dn(al),up(i))*L(up(ro),up(j)))*L(dn(ro),up(k))*vec(dn(a),L(dn(be),dn(k))))
 put(4,12,-Q(15,64),G(up(a),up(al),up(be))*L(up(ro),up(i))*L(dn(ro),up(j))*L(dn(al),up(k))*vec(dn(a),L(dn(be),dn(k))))
 put(4,13,Q(9,32),S(dn(a),dn(b),up(al),up(be))*w(up(a),up(b))*sy(lambda i,j:L(dn(al),up(i))*L(up(ro),up(j)))*L(dn(be),up(k))*L(dn(ro),dn(k)))
 put(4,14,Q(9,64),S(dn(a),dn(b),up(al),up(be))*w(up(a),up(b))*L(up(ro),up(i))*L(dn(ro),up(j))*L(dn(al),up(k))*L(dn(be),dn(k)))
 put(5,1,Q(3,8),G(up(a),up(al),up(be))*sy(lambda i,j:L(dn(al),up(i))*L(up(ro),up(j)))*L(dn(be),up(k))*L(dn(ro),dn(k))*vec(dn(a),W))
 put(5,2,Q(3,8),S(dn(a),dn(b),up(al),up(be))*F(up(a),up(b))*L(up(ro),up(i))*L(dn(ro),up(j))*L(dn(al),up(k))*L(dn(be),dn(k)))
 put(5,3,Q(3,8),X(up(k),up(l))*L(up(al),up(i))*L(dn(al),up(j))*L(up(be),dn(k))*L(dn(be),dn(l)))
 put(6,1,I*Q(3,32),L(up(al),up(i))*L(dn(al),up(j))*L(up(be),up(k))*L(dn(be),up(l))*L(up(ga),dn(k))*L(dn(ga),dn(l)))
 put(6,2,I*Q(3,16),L(up(al),up(i))*L(dn(al),up(k))*L(up(be),up(j))*L(dn(be),up(l))*L(up(ga),dn(k))*L(dn(ga),dn(l)))
 return inputs

def allix(f):return f.ds+f.ix+f.oddD

def check(p,weight,free):
 for c,fs in p.ts:
  w=sum((f.weight for f in fs),Q(0));assert w==weight,('weight',w,fs)
  par=sum(f.parity for f in fs)%2;assert par==(int(2*weight)%2),('parity',par,fs)
  ix=defaultdict(list)
  for f in fs:
   for x in allix(f):ix[x[1:]].append(x[0])
  for name,positions in ix.items():
   if name in free:assert positions==[free[name]],('free',name,positions,fs)
   else:assert sorted(positions)==['+','-'],('dummy',name,positions,fs)
  assert set(free)<=set(ix),('missing',set(free)-set(ix),fs)

def normalize(p,metrics=False):
 out=[]
 for c,fs0 in p.ts:
  fs=list(fs0);power=sum(f.power if f.name=='pow' else 1 for f in fs if (f.name=='pow' and not f.oddD) or (f.name=='W' and not f.ds and not f.oddD))
  fs=[f for f in fs if not((f.name=='pow' and not f.oddD) or (f.name=='W' and not f.ds and not f.oddD))]
  if power:fs=[A('pow',power=power)]+fs
  if metrics:
   while True:
    done=False
    for n,f in enumerate(fs):
     if f.ds or f.oddD or f.name not in ['eps','eta','del']:continue
     # First try contracting second metric slot, then the first (epsilon sign).
     for pos in [1,0]:
      x=f.ix[pos];y=f.ix[1-pos]
      for m,g in enumerate(fs):
       if m==n or g.name in ['eps','eta','del']:continue
       if any(z[1:]==x[1:] and z[0]!=x[0] for z in allix(g)):
        if f.name=='eps' and pos==0:c=-c
        def sub(z):return y if z[1:]==x[1:] else z
        fs[m]=replace(g,ix=tuple(map(sub,g.ix)),ds=tuple(map(sub,g.ds)),oddD=tuple(map(sub,g.oddD)))
        fs.pop(n);done=True;break
      if done:break
     if done:break
    if not done:break
  out.append((c,tuple(fs)))
 return P.terms(out)

# Human-readable conventional dummy labels, reset independently in each summand.
names={'s':[r'\beta',r'\gamma',r'\delta',r'\rho',r'\sigma',r'\tau',r'\xi',r'\zeta',r'\kappa',r'\mu',r'\nu',r'\omega',r'\upsilon'],
       'u':list('klmnpqstuvxyz'),'l':list('abcdefghpqstuvxyz')}
fixed={'sE':r'\eta','uI':'i','uJ':'j','uR':'r'}
def namemap(fs):
 mapping=fixed.copy();count=defaultdict(int)
 for f in fs:
  for x in allix(f):
   x=x[1:]
   if x not in mapping:
    k=x[0];num=count[k];count[k]+=1
    mapping[x]=names[k][num] if num<len(names[k]) else ('q_{'+str(num)+'}')
 return mapping
symbols={'L':r'\lambda','X':'X','F':'F','Fs':'F','w':'W','ws':'W','x':'X','w3':'W','w3a':'W','z':'X','za':'X','Y':'Y','W':'W','w4':'W','eps':r'\varepsilon','eta':r'\eta','del':r'\delta','G':r'\Gamma','S':r'\Sigma','eps5':r'\varepsilon','T':r'\mathcal T','RM':r'\mathcal R(M)','RD':r'\mathcal R(\mathbb D)','RJ':r'\mathcal R(J)','RS':r'\mathcal R(S)','RK':r'\mathcal R(K)'}
def texatom(f,mp):
 if f.name=='pow':body='W' if f.power==1 else 'W^{'+str(f.power)+'}'
 else:
  def indices(ix):
   result='';groups=[]
   for x in ix:
    if groups and groups[-1][0]==x[0]:groups[-1][1].append(mp[x[1:]])
    else:groups.append((x[0],[mp[x[1:]]]))
   for sign,labels in groups:result+='{}'+('^' if sign=='+' else '_')+'{'+' '.join(labels)+'}'
   return result
  if f.name in ['G','S']:
   cut=1 if f.name=='G' else 2
   body='('+symbols[f.name]+indices(f.ix[:cut])+')'+indices(f.ix[cut:])
  else:body=symbols[f.name]+indices(f.ix)

 for a in reversed(f.ds):body=(r'\nabla_{' if a[0]=='-' else r'\nabla^{')+mp[a[1:]]+'}'+body
 if f.oddD:
  s,r=f.oddD;body=r'\nabla_{'+mp[s[1:]]+'}^{'+mp[r[1:]]+r'}\big('+body+r'\big)'
 elif f.ds:body=r'\big('+body+r'\big)'
 return body

def texcoef(c):
 assert not(c.r and c.i)
 a=c.i or c.r;sg='-' if a<0 else '+';a=abs(a)
 numerator=('' if a.numerator==1 else str(a.numerator))+('i' if c.i else '')
 if not numerator:numerator='1'
 if a.denominator==1:v='' if numerator=='1' else numerator
 else:v=r'\frac{'+numerator+'}{'+str(a.denominator)+'}'
 return sg+v

def texterms(p,metrics=True):
 out=[]
 for c,fs in normalize(p,metrics=metrics).ts:
  mp=namemap(fs);out.append(texcoef(c)+''.join(texatom(f,mp) for f in fs))
 return out

def mathjax_display(tex):
 """Expand boxed in long display payloads before MathJax macro expansion."""
 if len(tex)<=5120:return tex
 while (match:=re.search(r'\\boxed(?![A-Za-z])\s*\{',tex)):
  start=match.end();end=start;depth=1
  while end<len(tex) and depth:
   if tex[end]=='\\':
    end+=2  # Escaped braces and control sequences do not open a brace group.
    continue
   if tex[end]=='{':depth+=1
   elif tex[end]=='}':depth-=1
   end+=1
  if depth:raise ValueError('Unbalanced boxed expression in Markdown output')
  body=tex[start:end-1]
  tex=tex[:match.start()]+r'\fbox{$\displaystyle{'+body+r'}$}'+tex[end:]
 return tex

def display(p,label=None,left=None,perrow=2,metrics=True):
 ts=texterms(p,metrics=metrics);lines=[]
 for n in range(0,len(ts),perrow):
  row=' '.join(ts[n:n+perrow])
  if n==0 and row.startswith('+'):row=row[1:]
  lines.append(('{}={}&'.format(left,'') if n==0 and left else '&')+row)
 tex=r'\begin{aligned}'+'\n'+('\\\\\n'.join(lines) if lines else '0')+'\n'+r'\end{aligned}'+ ('\n'+r'\tag{'+label+'}' if label else '')
 return '```math\n'+mathjax_display(tex)+'\n```\n'

if __name__=='__main__':
 inputs=make_inputs();print('inputs',len(inputs));check(P.terms([t for p in inputs.values() for t in p.ts]),Q(3),{'uI':'+','uJ':'+'})
 for key,p in inputs.items():
  z=deriv(p);check(z,Q(7,2),{'sE':'-','uR':'+','uI':'+','uJ':'+'});check(normalize(z,True),Q(7,2),{'sE':'-','uR':'+','uI':'+','uJ':'+'})
  print(key,len(z.ts))
