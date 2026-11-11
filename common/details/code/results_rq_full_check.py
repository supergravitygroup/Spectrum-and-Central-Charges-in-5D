exec(open('__RESULTS_CHECK_WORKDIR__/results_weyl_scalar_q_check.py').read().split('byx={}')[0])
residuals={}
for a,b in pairs:
 proj=ma(rawQ[a,b],mm(mat(-I*one,gs(h[a],gamma(a))),Qphi[b]),mm(mat(I*one,gs(h[b],gamma(b))),Qphi[a]))
 res=clean(ma(proj,ms(-1,MQ[a,b])))
 res={k:s.expand(v.xreplace(subc)) for k,v in res.items() if s.expand(v.xreplace(subc))!=0}
 if res:residuals[a,b]=res
print('Definition-derived Q-curvature variation minus R05:',len(residuals),'nonzero tensor blocks',flush=True)
assert not residuals
