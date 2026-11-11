#!/usr/bin/env python3
"""Independent source six-derivative check of every gradient-X coefficient.

Only flat vector rules (2.13), the definition (3.24), and exterior algebra
are used on the operator side; no higher descendant reduction is imported.
Terms are retained symbolically through six differentiations, then the
coefficient linear in dX is extracted. All denominators are cleared.
"""
import runpy
from pathlib import Path
HERE=Path(__file__).resolve().parent
ns=runpy.run_path(str(HERE/'verify_log_step2_w3.py'))
globals().update({k:v for k,v in ns.items() if not k.startswith('__')})
# Polynomial monomial (pole, sorted even variable names, odd-generator mask).
# D X, D F and D v generate d lambda. D(d lambda) generates d X.
# Variables: F spinor symmetric, X symmetric, v[5], dx[5,2,2].
def even(kind,*ids):return ((kind,*ids),)
def mulbasis(ev1,m1,ev2,m2):
 if m1&m2:return None
 sg=(-1)**sum((m2&((1<<j)-1)).bit_count() for j in range(m1.bit_length()) if m1&(1<<j))
 return tuple(sorted(ev1+ev2)),m1|m2,sg
def Dvar(A,var):
 a,i=divmod(A,2);kind,*ids=var;out=[]
 if kind=='X':
  j,k=ids
  for n,t in it.product(range(5),range(4)):
   for c,h in [(1j*E[i,j]*G[n,a,t],k),(1j*E[i,k]*G[n,a,t],j)]:
    if c:out.append(((),1<<(8+8*n+2*t+h),c))
 if kind=='F':
  b,c=ids
  for n,t in it.product(range(5),range(4)):
   z=-.5j*(GD[n,a,b]*int(t==c)+GD[n,a,c]*int(t==b)+C[a,b]*G[n,c,t]+C[a,c]*G[n,b,t])
   if z:out.append(((),1<<(8+8*n+2*t+i),z))
 if kind=='v':
  n=ids[0];out.append(((),1<<(8+8*n+2*a+i),1j))
 return out
def Dodd(A,B):
 a,i=divmod(A,2);out=[]
 if B<8:
  b,j=divmod(B,2)
  out.append((even('F',*sorted((a,b))),0,-2*E[i,j]))
  out.append((even('X',*sorted((i,j))),0,-C[a,b]))
  out.extend((even('v',n),0,-E[i,j]*GD[n,a,b]) for n in range(5))
 else:
  n,r=divmod(B-8,8);b,j=divmod(r,2)
  out.append((even('dx',n,*sorted((i,j))),0,-C[a,b]))
 return [(e,m,c) for e,m,c in out if c]
def DP(A,P):
 out=defaultdict(complex)
 for (n,ev,m),z in P.items():
  # pole derivative
  t=mulbasis((),1<<A,ev,m)
  if t and n:out[n+1,t[0],t[1]]+=-n*1j*z*t[2] # Derivative of the even coefficient inserts lambda on the left.
  for idx,var in enumerate(ev):
   eleft=ev[:idx]+ev[idx+1:]
   for en,mn,c in Dvar(A,var):
    t=mulbasis(en,mn,eleft,m)
    if t:out[n,t[0],t[1]]+=z*c*t[2]
  for idx,B in enumerate([b for b in range(m.bit_length()) if m&(1<<b)]):
   for en,mn,c in Dodd(A,B):
    t=mulbasis(ev,m^(1<<B),en,mn)
    if t:out[n,t[0],t[1]]+=z*c*((-1)**idx)*t[2]
 return {k:v for k,v in out.items() if v}
from functools import lru_cache
@lru_cache(None)
def word_eval(word):
 if len(word)==1:return {(1,(),1<<word[0]):1j}
 return DP(word[0],word_eval(word[1:]))
pairs=[(a,b,U[a,b]) for a,b in it.product(range(4),repeat=2) if U[a,b]]
words=defaultdict(complex)
for k,l,p,q in it.product(range(2),repeat=4):
 if not E[p,k]*E[q,l]:continue
 for ss in it.permutations((0,0,k,l)):
  for (a,b,uv),(c,d,uw),(e,f,ux) in it.product(pairs,repeat=3):
   word=(2*b+ss[0],2*a+ss[1],2*d+ss[2],2*c+ss[3],2*f+p,2*e+q)
   words[word]+=E[p,k]*E[q,l]*uv*uw*ux
out=defaultdict(complex)
for word,z in words.items():
 if not z:continue
 for key,vv in word_eval(word).items():
  n,ev,m=key
  if n==3 and len(ev)==1 and ev[0][0]=='dx':out[key]+=3j*z*vv

for nn,i,j in it.product(range(5),range(2),range(2)):
 if j<i:continue
 p=inputs();p['dx'][nn,i,j]=p['dx'][nn,j,i]=1
 actual={m:z for (n,ev,m),z in out.items() if ev==even('dx',nn,i,j) and z}
 expected=scale(30720,add(*rawparts(**p)))
 assert_poly_equal(actual,expected,'six source derivatives, dx '+str((nn,i,j)))
report={'status':'PASS: definition-derived sign; printed sign fails', 'scope':'all 15 independent flat dX components and every surviving Grassmann monomial; complete six-derivative SU(2) symmetrization', 'unique_ordered_words':len(words), 'cached_ordered_prefixes':word_eval.cache_info().currsize, 'operator_normalization_denominator_cleared':30720, 'printed_gradient_X_coefficient':'-i/4', 'derived_gradient_X_coefficient':'+i/4', 'IBP_or_EOM_used':False, 'full_primary_verified':False}
report['input_sha256']={str(p.relative_to(BASE)):hashlib.sha256(p.read_bytes()).hexdigest() for p in [Path(__file__),HERE/'verify_log_step2_w3.py']}
(BASE/'sources/step2/w3_flat_gradient_x_checks.json').write_text(json.dumps(report,indent=2)+'\n')
print('PASS: all 15 dX jets under the original six derivatives. The printed S23 gradient-X sign is opposite.')
