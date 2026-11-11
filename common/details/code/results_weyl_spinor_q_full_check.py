exec(open('__RESULTS_CHECK_WORKDIR__/results_weyl_scalar_q_check.py').read().split('rawQ={}')[0])
orientation=s.Symbol('epsilon01234')
with open('__RESULTS_CHECK_WORKDIR__/results_weyl_spinor_Qfull.pkl','rb') as f0:fullcalc=pickle.load(f0)
with open('__RESULTS_CHECK_WORKDIR__/results_weyl_Ncalc.pkl','rb') as f0:Ncalc=pickle.load(f0)
with open('__RESULTS_CHECK_WORKDIR__/results_weyl_Ecalc.pkl','rb') as f0:Ecalc=pickle.load(f0)
Lw=s.zeros(2)
for a,b in product(range(5),repeat=2):Lw+=s.Rational(16,3)*h[a]*h[b]*T[a,b]*RV[a,b]
expected=ma(mat(Ncalc*one/2,gamma()),*(mat(-I*Ecalc[a]*one/2,gamma(a)) for a in range(5)),mat(Lw*eps,Ts),*(mat(I*Lw.applyfunc(lambda z:deriv(z,a))*eps/2,gamma(a)) for a in range(5)))
res=ma(fullcalc,ms(-1,expected))
def alt(ind):return 0 if len(set(ind))<len(ind) else (-1)**sum(ind[i]>ind[j] for i in range(len(ind)) for j in range(i+1,len(ind)))
red=defaultdict(lambda:s.S.Zero)
for (i,j,g),v in res.items():
 if len(g)<=2:red[i,j,g]+=v
 else:
  comp=tuple(k for k in range(5) if k not in g)
  factor=I*orientation*alt(g+comp)*(-1)**(len(comp)*(len(comp)-1)//2)
  for k in comp:factor*=h[k]
  red[i,j,comp]+=factor*v
red={k:s.rem(s.expand(v),orientation**2-1,orientation) for k,v in red.items()}
red={k:s.expand(v) for k,v in red.items() if s.expand(v)!=0}
print('Full Q-spinor residual before tensor identities:',len(red),flush=True)
# Full algebraic curvature/derivative relations, with undetermined tensors symbolic.
ddsub={};dcsub={};drvsub={}
for a in range(5):
 for b in range(5):
  for c,d in pairs:
   symmetric=s.Symbol('sddT'+str(min(a,b))+str(max(a,b))+'_'+str(c)+str(d))
   comm=sum(h[e]*(rr(a,b,c,e)*T[e,d]+rr(a,b,d,e)*T[c,e]) for e in range(5))
   ddsub[ddt[a,b,c,d]]=symmetric+comm/2
Rsymbols=set().union(*(v.free_symbols for v in subc.values()))
for m in range(5):
 ds={r:s.Symbol('d'+str(m)+'_'+str(r)) for r in Rsymbols}
 for a,b in pairs:
  for c,d in pairs:dcsub[dc[m,a,b,c,d]]=subc[C[a,b,c,d]].xreplace(ds)
 for a,b in pairs:
  cyc=drv[m,a,b]+drv[a,b,m]+drv[b,m,a]
  for i,j in [(0,0),(0,1),(1,1)]:drvsub[drv[m,a,b][i,j]]=drv[m,a,b][i,j]-cyc[i,j]/3
red={k:s.expand(v.xreplace(subc).xreplace(ddsub).xreplace(dcsub).xreplace(drvsub)) for k,v in red.items()}
red={k:v for k,v in red.items() if v!=0}
print('After algebraic curvature and SU(2) Bianchi identities:',len(red),flush=True)
for k,v in list(red.items())[:3]:print(k,len(s.Add.make_args(v)),s.Add.make_args(v)[:6],flush=True)
with open('__RESULTS_CHECK_WORKDIR__/results_weyl_spinorQres.pkl','wb') as f0:pickle.dump(red,f0)
