exec(open('__RESULTS_CHECK_WORKDIR__/results_weyl_l_check.py').read().split('for oi,oj in [(0,0)')[0])
from itertools import combinations
checks=0
for m in range(5):
 for j,k in pairs if 'pairs' in globals() else combinations(range(5),2):
  # Dictionary entry is the coefficient of the independent derivative jet d_m q'_{jk}.
  q=lambda a,b:P[a,b,j,k]
  rsd={}
  for a,b in product(range(5),repeat=2):
   rsd[a,b]=ga(gs(-I,gm(gamma(m),q(a,b))),gs(-I*h[a]*h[m]/2,gm(gamma(a),q(b,m))),gs(I*h[b]*h[m]/2,gm(gamma(b),q(a,m))))
  for a,b,c in combinations(range(5),3):
   lhs=ga(gs(int(a==m),q(b,c)),gs(int(b==m),q(c,a)),gs(int(c==m),q(a,b)))
   rhs=ga(gs(I*h[a],gm(gamma(a),rsd[b,c])),gs(I*h[b],gm(gamma(b),rsd[c,a])),gs(I*h[c],gm(gamma(c),rsd[a,b])))
   residual={g:s.expand(v) for g,v in ga(lhs,gs(-1,rhs)).items() if s.expand(v)!=0}
   assert not residual,(m,j,k,a,b,c,residual)
   checks+=1
print('S-curvature derivative Bianchi coefficients:',checks,'exact zero residuals',flush=True)
# T terms: DQ term is separate; retain every T component symbolically.
checks=0
for j,k in combinations(range(5),2):
 q=lambda a,b:P[a,b,j,k]
 U=ga(*(gs(h[a]*h[b]*T[a,b],q(a,b)) for a,b in product(range(5),repeat=2)))
 rst={}
 for a,b in product(range(5),repeat=2):
  rst[a,b]=ga(gs(-s.Rational(8,3)*h[a]*h[b],gm(gamma(a,b),U)),gs(-3,gm(Ts,q(a,b))),*(gs(6*h[r]*T[r,d]*h[a],gm(gamma(d),gm(gamma(a),q(b,r)))) for r,d in product(range(5),repeat=2)),*(gs(-6*h[r]*T[r,d]*h[b],gm(gamma(d),gm(gamma(b),q(a,r)))) for r,d in product(range(5),repeat=2)),*(gs(-4*h[r]*T[r,a],q(b,r)) for r in range(5)),*(gs(4*h[r]*T[r,b],q(a,r)) for r in range(5)))
 for a,b,c in combinations(range(5),3):
  residual=ga(gs(h[a],gm(gamma(a),rst[b,c])),gs(h[b],gm(gamma(b),rst[c,a])),gs(h[c],gm(gamma(c),rst[a,b])),gs(-h[a],gm(Ts,gm(gamma(a),q(b,c)))),gs(-h[b],gm(Ts,gm(gamma(b),q(c,a)))),gs(-h[c],gm(Ts,gm(gamma(c),q(a,b)))))
  residual={g:s.expand(v) for g,v in residual.items() if s.expand(v)!=0}
  assert not residual,(j,k,a,b,c,residual)
  checks+=1
print('S-curvature T Bianchi coefficients:',checks,'exact zero residuals',flush=True)
