# Reuse the symbolic input definitions and read the calculated full Q variation.
exec(open('__RESULTS_CHECK_WORKDIR__/results_weyl_scalar_q_check.py').read().split('byx={}')[0])
exec('f={(a,b)'+open('__RESULTS_CHECK_WORKDIR__/results_weyl_scalar_q_check.py').read().split('f={(a,b)')[1].split('T2=sum')[0])
with open('__RESULTS_CHECK_WORKDIR__/results_weyl_spinor_Qfull.pkl','rb') as file:fullcalc=pickle.load(file)
orientation=s.Symbol('epsilon01234')
T2=sum(h[a]*h[b]*T[a,b]**2 for a,b in product(range(5),repeat=2))
Ecalc={}
for a in range(5):
 comp=tuple(b for b in range(5) if b!=a)
 Ecalc[a]=s.expand(I*sum(fullcalc.get((i,i,(a,)),0)+I*orientation*alt(comp+(a,))*h[a]*fullcalc.get((i,i,comp),0) for i in range(2)))
Eexpected={}
for a in range(5):
 val=s.S.Zero
 for b,c,d,e in product(range(5),repeat=4):
  if not alt((a,b,c,d,e)):continue
  epsilon=-orientation*alt((a,b,c,d,e))
  val+=epsilon*h[b]*h[c]*h[d]*h[e]*sum(h[f0]*h[g]*C[b,c,f0,g]*C[d,e,f0,g]/16 for f0,g in product(range(5),repeat=2))
  val-=epsilon*h[b]*h[c]*h[d]*h[e]*sum(RV[b,c][i,j]*(eps.T*RV[d,e]*eps)[i,j]/12 for i,j in product(range(2),repeat=2))
  for f0 in range(5):
   val-=32*epsilon*h[b]*h[c]*h[f0]*h[d]*h[e]*(s.Rational(2,3)*(dt[b,c,f0]*dt[f0,d,e]+T[c,f0]*d2T(b,f0,d,e))+dt[b,c,f0]*dt[d,e,f0]+T[c,f0]*d2T(b,d,e,f0))
 for b in range(5):
  inside=4*sum(h[c]*h[d]*C[a,b,c,d]*T[c,d] for c,d in product(range(5),repeat=2))-s.Rational(64,3)*D*T[a,b]-s.Rational(128,9)*T[a,b]*T2-s.Rational(512,3)*sum(h[c]*h[d]*T[a,c]*T[c,d]*T[b,d] for c,d in product(range(5),repeat=2))
  val+=h[b]*deriv(inside,b)
 Eexpected[a]=s.expand(val)
# Curvature and ordered-second-derivative identities used for the scalar check.
ddsub={}
for a in range(5):
 for b in range(5):
  for c,d in pairs:
   symmetric=s.Symbol('sddT'+str(min(a,b))+str(max(a,b))+'_'+str(c)+str(d))
   comm=sum(h[e]*(rr(a,b,c,e)*T[e,d]+rr(a,b,d,e)*T[c,e]) for e in range(5))
   ddsub[ddt[a,b,c,d]]=symmetric+comm/2
for a in range(5):
 residual=s.expand((Ecalc[a]-Eexpected[a]).xreplace(subc).xreplace(ddsub))
 with open('__RESULTS_CHECK_WORKDIR__/results_weyl_Eres'+str(a)+'.pkl','wb') as file:pickle.dump(residual,file)
 print('Vector component',a,'residual monomials:',len(s.Add.make_args(residual)) if residual!=0 else 0,flush=True)
 if residual!=0:print(s.Add.make_args(residual)[:8],flush=True)
with open('__RESULTS_CHECK_WORKDIR__/results_weyl_Ecalc.pkl','wb') as file:pickle.dump(Ecalc,file)
