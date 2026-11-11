exec(open('__RESULTS_CHECK_WORKDIR__/results_weyl_l_check.py').read().split('for oi,oj in [(0,0)')[0])
# Infer exact proportionality by symbolic coefficient equations, not samples.
z=s.Symbol('z')
equations=[]
for c,d in [(c,d) for c in range(5) for d in range(c+1,5)]:
 for j in range(5):
  for k in range(j+1,5):
   outg={}
   for a,b in product(range(5),repeat=2):
    G=ga(gamma(a,b,c,d),gs(-1,gm(gamma(a,b),gamma(c,d))),gs(-s.Rational(1,2),gm(gamma(c,d),gamma(a,b))))
    outg=ga(outg,gm(G,P[a,b,j,k]))
   outg=ga(outg,gs(-z*h[c]*h[d],P[c,d,j,k]))
   equations.extend(s.expand(v) for v in outg.values() if s.expand(v)!=0)
print('Projected curvature gamma identity coefficient:',s.solve(equations,[z]),flush=True)

assert s.solve(equations,[z])=={z:s.Integer(6)}
