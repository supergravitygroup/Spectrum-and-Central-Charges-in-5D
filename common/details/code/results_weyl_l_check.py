exec(open('__RESULTS_CHECK_WORKDIR__/results_vl_check.py').read().split('# Variation of e(YL+rho N)')[0])
D=s.Symbol('D')
RV={};dt={};C={}
for a,b in product(range(5),repeat=2):
 RV[a,b]=s.zeros(2) if a==b else (1 if a<b else -1)*symmat('RV'+str(min(a,b))+str(max(a,b))+'_')
 for c in range(5):dt[c,a,b]=0 if a==b else (1 if a<b else -1)*s.Symbol('dT'+str(c)+'_'+str(min(a,b))+str(max(a,b)))
 for c,d in product(range(5),repeat=2):
  C[a,b,c,d]=0 if a==b or c==d else (1 if a<b else -1)*(1 if c<d else -1)*s.Symbol('C'+str(min(a,b))+str(max(a,b))+'_'+str(min(c,d))+str(max(c,d)))
DT=[ga(*(gs(dt[a,c,d],gamma(c,d)) for c,d in product(range(5),repeat=2))) for a in range(5)]
# Q-curvature and chi variations. All are independently indexed coefficients.
def dq(a,b):
 bos=ga(*(gs(s.Rational(1,4)*C[a,b,c,d],gamma(c,d)) for c,d in product(range(5),repeat=2)),
  gs(I*h[b],gm(DT[a],gamma(b))),gs(-I*h[a],gm(DT[b],gamma(a))),
  gs(-I*h[b]/3,gm(gamma(b),DT[a])),gs(I*h[a]/3,gm(gamma(a),DT[b])),
  *(gs(-I*h[a]*h[b]/3,gm(gamma(a),gm(gamma(c),gm(DT[c],gamma(b))))) for c in range(5)),
  *(gs(I*h[a]*h[b]/3,gm(gamma(b),gm(gamma(c),gm(DT[c],gamma(a))))) for c in range(5)),
  *(gs(-2*I*h[a]*h[b]*h[c]*dt[c,c,d]/3,gm(gamma(a,b),gamma(d))) for c,d in product(range(5),repeat=2)))
 rv=[]
 for c,d in product(range(5),repeat=2):
  G=ga(gs(h[a]*h[b],gamma(a,b,c,d)),gs(-h[a]*h[b],gm(gamma(c,d),gamma(a,b))),gs(-h[a]*h[b]/s.Integer(2),gm(gamma(a,b),gamma(c,d))))
  rv.append(mat(RV[c,d]*eps/6,G))
 return [('eps',ma(mat(one,bos),*rv)),('eta',mat(one,ga(gs(-8*T[a,b],gamma()),*(gs(s.Rational(8,3)*h[b]*T[a,c],gamma(b,c)) for c in range(5)),*(gs(-s.Rational(8,3)*h[a]*T[b,c],gamma(a,c)) for c in range(5)),*(gs(s.Rational(4,3)*h[a]*h[b]*T[c,d],gamma(a,b,c,d)) for c,d in product(range(5),repeat=2)))))]
def dchi():
 G=ga(gs(D/4,gamma()),*(gs(I*dt[c,a,b]/8,gm(gamma(a,b),gamma(c))) for a,b,c in product(range(5),repeat=3)),*(gs(-I*h[b]*dt[b,a,b]/8,gamma(a)) for a,b in product(range(5),repeat=2)),*(gs(-T[a,b]*T[c,d]/4,gamma(a,b,c,d)) for a,b,c,d in product(range(5),repeat=4)),*(gs(h[a]*h[b]*T[a,b]**2/6,gamma()) for a,b in product(range(5),repeat=2)))
 return [('eps',ma(mat(one,G),*(mat(RV[a,b]*eps/64,gamma(a,b)) for a,b in product(range(5),repeat=2)))),('eta',mat(one,gs(s.Rational(1,4),Ts)))]
def delta(X):
 if X=='chi':return dchi()
 if isinstance(X,tuple) and X[0]=='q':return dq(X[1],X[2])
 raise KeyError(X)

def rs(a,b):
 # species and gamma matrices, all fermionic coefficients retained
 terms=[]
 for c in range(5):
  terms += [(('dq',c,a,b),gs(-I,gamma(c))), (('dq',c,b,c),gs(-I*h[a]*h[c]/2,gamma(a))), (('dq',c,a,c),gs(I*h[b]*h[c]/2,gamma(b)))]
 for c,d in product(range(5),repeat=2):
  terms += [(('q',c,d),gs(-s.Rational(8,3)*h[a]*h[b]*h[c]*h[d]*T[c,d],gamma(a,b)))]
 for r,d in product(range(5),repeat=2):
  terms += [(('q',b,r),gs(6*h[r]*T[r,d]*h[a],gm(gamma(d),gamma(a)))),(('q',a,r),gs(-6*h[r]*T[r,d]*h[b],gm(gamma(d),gamma(b))))]
 terms +=[(('q',a,b),gs(-3,Ts))]
 for r in range(5):terms += [(('q',b,r),gs(-4*h[r]*T[r,a],gamma())),(('q',a,r),gs(4*h[r]*T[r,b],gamma()))]
 return terms

def wphi():
 terms=[]
 for a,b in product(range(5),repeat=2):
  for c,d in product(range(5),repeat=2):
   terms += [(('q',a,b),mat(one,gs(-h[a]*h[b]*C[a,b,c,d]/8,gamma(c,d))))]
  for c in range(5):
   terms += [(('q',a,b),mat(one,gs(-4*I*h[a]*h[b]*dt[a,b,c],gamma(c)))),(('dq',c,a,b),mat(one,gs(8*I*h[a]*h[b]*T[a,b],gamma(c)))),(('dq',c,b,c),mat(one,gs(8*I*h[b]*h[c]*T[a,b],gamma(a))))]
  terms += [(('q',a,b),mat(one,gs(s.Rational(8,3)*h[a]*h[b]*T[a,b],Ts))),(('q',a,b),mat(h[a]*h[b]*RV[a,b]*eps/2,gamma())),('chi',mat(-s.Rational(8,3)*RV[a,b]*eps,gamma(a,b)))]
  for c in range(5):terms += [('chi',mat(one,gs(-64*I*dt[a,b,c]/3,gm(gamma(a,b),gamma(c)))))]
  terms += [('chi',mat(one,gs(s.Rational(1024,9)*h[a]*h[b]*T[a,b]**2,gamma()))),(('dchi',b),mat(one,gs(128*I*h[b]*T[a,b]/3,gamma(a))))]
 terms += [('chi',mat(one,gs(s.Rational(128,3)*D,gamma())))]
 return terms

def insert_spinor(par,Cpair,Z,M,factor=1):
 for (j,k,m),u in M.items():
  for i in range(2):out[par,Z,i,k,m]+=factor*Cpair[i,j]*u

def projector_mats():
 result={}
 for j in range(5):
  for k in range(j+1,5):
   co=lambda a,b:int((a,b)==(j,k))-int((a,b)==(k,j))
   tr=ga(*(gs(co(a,b),gamma(a,b)) for a,b in product(range(5),repeat=2)))
   ph=[ga(*(gs(I*co(a,c)/3,gamma(c)) for c in range(5)),gs(-I*h[a]/24,gm(gamma(a),tr))) for a in range(5)]
   for a,b in product(range(5),repeat=2):
    result[a,b,j,k]=ga(gs(co(a,b),gamma()),gs(-I*h[a],gm(gamma(a),ph[b])),gs(I*h[b],gm(gamma(b),ph[a])))
 return result
P=projector_mats()
for oi,oj in [(0,0),(0,1),(1,1)]:
 out.clear();pair=s.zeros(2);pair[oi,oj]+=s.Rational(1,2);pair[oj,oi]+=s.Rational(1,2)
 for a,b in product(range(5),repeat=2):
  vary_bilinear(('q',a,b),('q',a,b),pair,gamma(),I*h[a]*h[b]/4)
  # (16/3) T^ab delta RV_ab^ij
  for Z,G in rs(a,b):term('eps',Z,pair,G,-8*I*h[a]*h[b]*T[a,b])
  term('eps',('q',a,b),pair,Ts,16*I*h[a]*h[b]*T[a,b]/3)
  for c in range(5):
   term('eps',('dchi',b),pair,gamma(a),-s.Rational(64,3)*h[a]*h[b]*T[a,b]*h[a])
   term('eps',('dchi',a),pair,gamma(b),s.Rational(64,3)*h[a]*h[b]*T[a,b]*h[b])
   break
  term('eps','chi',pair,ga(gm(gs(h[a],gamma(a)),gm(Ts,gs(h[b],gamma(b)))),gs(-1,gm(gs(h[b],gamma(b)),gm(Ts,gs(h[a],gamma(a)))))),64*I*h[a]*h[b]*T[a,b]/3)
  term('eta',('q',a,b),pair,gamma(),8*I*h[a]*h[b]*T[a,b])
  term('eta','chi',pair,gamma(a,b),s.Rational(128,3)*I*T[a,b])
  # (16/3) RV_ab^ij delta T^ab
  term('eps','chi',-eps,gamma(a,b),s.Rational(8,3)*I*RV[a,b][oi,oj])
  term('eps',('q',a,b),-eps,gamma(),-I*h[a]*h[b]*RV[a,b][oi,oj]/2)
 vary_bilinear('chi','chi',pair,gamma(),s.Rational(256,3)*I)
 for Z,M in wphi():insert_spinor('eps',pair,Z,M,-I)
 # reduce independent Q-curvature coefficients to gamma-traceless ones
 red=defaultdict(lambda:s.S.Zero)
 for (par,Z,i,j,g),v in out.items():
  v=s.expand(v)
  if v==0:continue
  if isinstance(Z,tuple) and Z[0] in ('q','dq'):
   a,b=Z[-2:]
   for c in range(5):
    for d in range(c+1,5):
     W=('qp',c,d) if Z[0]=='q' else ('dqp',Z[1],c,d)
     for m,u in P[a,b,c,d].items():
      bladeout,sgn=blade(g,m);red[par,W,i,j,bladeout]+=v*u*sgn
  else:red[par,Z,i,j,g]+=v
 res={key:s.expand(val) for key,val in red.items() if s.expand(val)!=0}
 assert not res, (oi,oj,res)
 print('Weyl L variation residual',oi,oj,':',len(res),flush=True)
 from collections import Counter
 print(Counter((key[0],key[1][0] if isinstance(key[1],tuple) else key[1]) for key in res),flush=True)
 for key,val in list(res.items())[:15]:print(key,s.factor(val))
