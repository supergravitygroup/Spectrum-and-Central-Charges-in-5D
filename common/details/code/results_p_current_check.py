exec(open('__RESULTS_CHECK_WORKDIR__/results_vl_check.py').read().split('# Variation of e(YL+rho N)')[0])
for a in range(5):
 out.clear()
 for b in range(5):
  term('eps',('psi',b),-eps,gamma(b),h[a]*E[a]/2)
  term('eps',('psi',b),-eps,gamma(a),-h[b]*E[b]/2)
  termD('eps','varphi',b,-eps,gamma(a,b),-I/2)
  term('eps','varphi',-eps,gamma(b),-2*h[a]*T[b,a])
  vary_bilinear(('psi',b),'varphi',-eps,gamma(b,a),I/2)
  for c in range(5):
   vary_bilinear(('psi',b),('psi',c),Ld,gamma(a,b,c),s.Rational(1,4))
 term('eta','varphi',-eps,gamma(a),-2)
 # Subtract covariant divergence of Q^{ab}.
 for b in range(5):
  term(('deps',b),'varphi',-eps,gamma(a,b),I/2)
  term('eps',('dvarphi',b),-eps,gamma(a,b),I/2)
  for c in range(5):
   term('eps',('psi',c),eps.T*dL[b]*eps,gamma(a,b,c),-s.Rational(1,2))
   term(('deps',b),('psi',c),Ld,gamma(a,b,c),-s.Rational(1,2))
   term('eps',('psi',c),Ld,gm(gamma(a,b,c),gm(Ts,gs(h[b],gamma(b)))) ,I/2)
  term('eps',('phiS',b),Ld,gamma(a,b),3*I/2)
 res={k:s.expand(v) for k,v in out.items() if s.expand(v)!=0}
 assert not res, (a,res)
 print('P current residual',a,':',len(res))
 for k,v in list(res.items())[:10]:print(k,s.factor(v))
