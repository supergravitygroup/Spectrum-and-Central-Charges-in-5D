# GB-S+ local spectrum

a>-1/2, 0<x<2, real g!=0; local bulk

| Mode | Spin | Local equation | Kinetic weight | Real DoF | Reconstruction |
|---|---|---|---|---:|---|
| graviton | 2 | (Box-2k)H=0; massless | $`2 - x`$ | 5 | h=H; ell=n=0 |
| scalar | 0 | (Box-4k)ell=0; M^2 L_AdS^2=-4 | $`- \frac{2 \left(x - 2\right)}{3 x^{2}}`$ | 1 | h=-2*gbar*ell/(3x); n=-2gx*ell |
| vector_A | 1 | Maxwell; physical mass 0 | $`- 2 \left(x - 2\right)`$ | 3 | H2=0; v=-sqrt(2)gx*A |
| vector_Q | 1 (dual two-form) | Maxwell; physical mass 0 | $`- 16 \left(x - 2\right)`$ | 3 | H2=dQ; db=2 star(dQ); v=2sqrt(2)gx*Q |
| gravitino | 3/2 | (slash_nabla+3imJ)Upsilon=0; gauge massless | $`2 - x`$ | 8 | Psi=Upsilon; zeta=0; gamma.Upsilon=div.Upsilon=0 |
| spinor | 1/2 | (slash_nabla+imJ)zeta=0 | $`- \frac{2 \left(x - 2\right)}{3 x^{2}}`$ | 4 | Psi=i*sqrt(2)*gamma*J*zeta/(3x); Upsilon=0 |

Bosons: 12. Fermions: 12.

a=-1/2: x=2, every raw quadratic coefficient vanishes; generic constraints and DoF count not assigned

global boundary data, global frequencies, topology and renormalized boundary norms are not selected

Detailed equations, gauge quotients, signed roots and norms: [calculation notes](../../spectrum.md).
