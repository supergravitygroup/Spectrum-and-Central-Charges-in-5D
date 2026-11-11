# Definitions only; do not rerun the first component calculation.
exec(open('__RESULTS_CHECK_WORKDIR__/results_weyl_l_check.py').read().split('for oi,oj in [(0,0)')[0])
# Dictionary-valued Clifford/SU(2) matrix algebra.
def mm(A,B):
 out=defaultdict(lambda:s.S.Zero)
 for (i,j,a),u in A.items():
  for (k,l,b),v in B.items():
   if j==k:
    c,sgn=blade(a,b);out[i,l,c]+=u*v*sgn
 return dict(out)
def ms(c,A):return {k:c*v for k,v in A.items()}
def clean(A):return {k:s.expand(v) for k,v in A.items() if s.expand(v)!=0}
# formal tensor jets, all bosonic fields symbolic
DD=s.symbols('dD0:5')
drv={}
for m,a,b in product(range(5),repeat=3):drv[m,a,b]=s.zeros(2) if a==b else (1 if a<b else -1)*symmat('dRV'+str(m)+'_'+str(min(a,b))+str(max(a,b))+'_')
dc={}
for m,a,b,c,d in product(range(5),repeat=5):
 dc[m,a,b,c,d]=0 if a==b or c==d else (1 if a<b else -1)*(1 if c<d else -1)*s.Symbol('dC'+str(m)+'_'+str(min(a,b))+str(max(a,b))+'_'+str(min(c,d))+str(max(c,d)))
ddt={}
for m,n,a,b in product(range(5),repeat=4):ddt[m,n,a,b]=0 if a==b else (1 if a<b else -1)*s.Symbol('ddT'+str(m)+str(n)+'_'+str(min(a,b))+str(max(a,b)))
jet={m:{D:DD[m]} for m in range(5)}
for m in range(5):
 for a in range(5):
  for b in range(a+1,5):
   jet[m][T[a,b]]=dt[m,a,b]
   for i,j in [(0,0),(0,1),(1,1)]:jet[m][RV[a,b][i,j]]=drv[m,a,b][i,j]
   for n in range(5):jet[m][dt[n,a,b]]=ddt[m,n,a,b]
   for c in range(5):
    for d in range(c+1,5):jet[m][C[a,b,c,d]]=dc[m,a,b,c,d]
def deriv(x,m):
 x=s.expand(x)
 return s.Add(*(s.diff(x,z)*jet[m][z] for z in x.free_symbols if z in jet[m]))
def md(A,m):return {k:deriv(v,m) for k,v in A.items()}
# δ_S phi_a = nabla_a eta + Sphi_a eta, obtained directly from R'Q definition.
raw={(a,b):gs(2*h[a]*h[b],gm(Ts,gamma(a,b))) for a,b in product(range(5),repeat=2)}
tr=ga(*(gm(gamma(a,b),raw[a,b]) for a,b in product(range(5),repeat=2)))
Sphi=[mat(one,ga(*(gs(I/3,gm(gamma(b),raw[a,b])) for b in range(5)),gs(-I*h[a]/24,gm(gamma(a),tr)))) for a in range(5)]
Mchi=dict(dchi())['eps'];Nchi=dict(dchi())['eta']
MQ={(a,b):dict(dq(a,b))['eps'] for a,b in product(range(5),repeat=2)}
NQ={(a,b):dict(dq(a,b))['eta'] for a,b in product(range(5),repeat=2)}
def SDferm(X):
 if X=='chi':return Nchi
 if isinstance(X,tuple):
  if X[0]=='q':return NQ[X[1],X[2]]
  if X[0]=='dchi':
   a=X[1];return ma(md(Nchi,a),mm(Mchi,mat(I*one,gs(h[a],gamma(a)))),ms(-1,mm(Nchi,Sphi[a])))
  if X[0]=='dq':
   a,b,c=X[1:];return ma(md(NQ[b,c],a),mm(MQ[b,c],mat(I*one,gs(h[a],gamma(a)))),ms(-1,mm(NQ[b,c],Sphi[a])))
 raise KeyError(X)
result={}
for X,M in wphi():result=ma(result,mm(M,SDferm(X)))
# subtract 3 LW^{ij} eta_j = -16 RV^{ij}_{ab} T^{ab} eps_jk eta^k
result=ma(result,*(mat(16*h[a]*h[b]*T[a,b]*RV[a,b]*eps,gamma()) for a,b in product(range(5),repeat=2)))
result=clean(result)
print('Unreduced S-spinor residual blocks:',len(result),flush=True)

# Curvature Weyl identities are linear. Substitute a full symbolic Riemann
# curvature projected to the Weyl representation, with no physical component sampling.
pairs=[(a,b) for a in range(5) for b in range(a+1,5)]
base={}
for r,P in enumerate(pairs):
 for q,Q in enumerate(pairs):base[P,Q]=s.Symbol('R'+str(min(r,q))+'_'+str(max(r,q)))
def rb(a,b,c,d):
 if a==b or c==d:return s.S.Zero
 return (1 if a<b else -1)*(1 if c<d else -1)*base[tuple(sorted((a,b))),tuple(sorted((c,d)))]
def rr(a,b,c,d):return s.expand((2*rb(a,b,c,d)-rb(a,c,d,b)-rb(a,d,b,c))/3)
Ric={(b,d):s.Add(*(h[a]*rr(a,b,a,d) for a in range(5))) for b,d in product(range(5),repeat=2)}
Rsc=s.Add(*(h[a]*Ric[a,a] for a in range(5)))
met=lambda a,b:h[a] if a==b else 0
subc={}
for a,b in pairs:
 for c,d in pairs:
  subc[C[a,b,c,d]]=rr(a,b,c,d)-(met(a,c)*Ric[b,d]-met(b,c)*Ric[a,d]-met(a,d)*Ric[b,c]+met(b,d)*Ric[a,c])/3+(met(a,c)*met(b,d)-met(a,d)*met(b,c))*Rsc/12
res={key:s.expand(val.xreplace(subc)) for key,val in result.items() if s.expand(val.xreplace(subc))!=0}
print('Weyl spinor S residual after exact Weyl identities:',len(res),flush=True)
for k,v in list(res.items())[:4]:print(k,s.factor(v),flush=True)

assert not res, res
