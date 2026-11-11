exec(open('__RESULTS_CHECK_WORKDIR__/results_weyl_scalar_q_check.py').read().split('rawQ={}')[0])
dcsub={}
Rsymbols=set().union(*(v.free_symbols for v in subc.values()))
for m in range(5):
 ds={r:s.Symbol('d'+str(m)+'_'+str(r)) for r in Rsymbols}
 for a,b in pairs:
  for c,d in pairs:dcsub[dc[m,a,b,c,d]]=subc[C[a,b,c,d]].xreplace(ds)
for a in range(5):
 with open('__RESULTS_CHECK_WORKDIR__/results_weyl_Eres'+str(a)+'.pkl','rb') as f0:res=pickle.load(f0)
 res=s.expand(res.xreplace(dcsub))
 assert res==0, (a,res)
 print('Differentiated Weyl algebraic identities, component',a,':',len(s.Add.make_args(res)) if res!=0 else 0,flush=True)
 if res!=0:print(s.Add.make_args(res)[:6],flush=True)
