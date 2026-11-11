# Two-derivative supergravity on AdS₅

The reference theory is the gauged two-derivative action obtained from the
2016 single-linear-multiplet map. Its component density is given in the
[common action](../../common/two_derivative_action/README.md).
The [fermionic input correspondence](../../references/fermionic_input_correspondence.md)
identifies its component input and reduction.

The fluxless background is the solution

```math
L_0=1,\qquad N_0=-\frac32g,\qquad
k=-\frac12g^2=-\ell^{-2},\qquad g\ne0.
```

Here $`L_0=1`$ is fixed by the two-derivative background equations, not a
normalization of the free compensator in a higher-derivative theory.
The [background and raw quadratic derivation](../../computations/two_derivative_fermionic/inputs/reference/results/gauged_two_derivative_fermionic_action/06_fluxless_ads5_zeroth_first_second_order_actions_from_1608_action.md)
retains arbitrary independent fluctuations and the implicit fermionic terms.

## Quadratic reduction and local modes

The [constraint and diagonalization derivation](../../computations/two_derivative_fermionic/inputs/reference/results/gauged_two_derivative_fermionic_action/07_fluxless_ads5_gauge_decomposition_diagonalization_and_spectrum_from_1608_action.md)
varies the raw action before fixing fluctuation gauges. Its sections 5–9
give the bosonic equations, algebraic and form constraints, metric–scalar
diagonalization and physical form channels. Sections 10–13 give the fermionic
field transformation, signed charge branches and reconstruction in the
original equations.

| Field or channel | Mass data | Real local polarizations |
|---|---|---:|
| Graviton | Massless AdS spin 2 | 5 |
| Maxwell field | $`M^2=0`$ | 3 |
| Massless two-form | Locally dual to a Maxwell field | 3 |
| Compensator scalar | $`M^2\ell^2=-4`$ | 1 |
| Gauge gravitino | $`\lvert m_{3/2}\ell\rvert=3/2`$ | 8 |
| Spinor | $`\lvert m_{1/2}\ell\rvert=1/2`$ | 4 |

Thus the local bosonic and fermionic totals are each twelve. The absolute
fermion masses in this table summarize the signed equations in the detailed
derivation; the two internal signs are related by symplectic Majorana reality
and are not additional independent doublets.

The scalar saturates the AdS₅ BF bound. Its logarithmic falloff is a boundary
choice, not an additional local polarization. Boundary counterterms,
renormalized norms and the relation to a particular boundary multiplet require
their own stated boundary data.

## Source and computational scope

The [component construction package](../../computations/two_derivative_fermionic/README.md)
contains the map, BF insertion and coefficient records. The
[source qualifications](../../computations/two_derivative_fermionic/CLAIMS.md)
identify the action inputs and the domains of its checks.

[Higher-derivative studies](../../README.md) ·
[Convention corrections](../../CONVENTIONS.md) ·
[Reproduction](../../README.md#reproduction)
