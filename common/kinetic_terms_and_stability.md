# Kinetic signs and stability

Mass roots, kinetic coefficients, and boundary-admissible solutions are separate data. This section uses coefficients from earlier coupled quadratic calculations; it introduces no independent Hermitian inner product for formal fermionic transpose norms.

## AdS₅ comparison

For R², using the [R² spectrum definitions](../r2/ads5/spectrum.md) $`A_R=4-3L_0,B_R=2-L_0,\nu_R`$, the bosonic coefficients are

| Channel | Kinetic coefficient |
|---|---|
| Graviton | $`A_R/2`$ |
| Two Maxwell channels | $`6B_R,\ 2A_R/(3g^2L_0^2)`$ |
| Proca | $`4A_R\zeta/(L_0^2B_R)`$ |
| Light scalar | $`2B_R/(3L_0^2)`$ |
| Additional neutral scalars | $`4A_R/[g^2L_0^4\nu_R(\nu_R\pm1)]`$ |
| Internal scalars | $`4\zeta^2/A_R`$ |

On the regular real branch used, positive ζ is decisive for the kinetic signs. These divided normalizations do not apply at $`A_R=0`$ or ζ=0. [R² kinetic norms](../r2/ads5/details/kinetic_norms.md).

In the Weyl² AdS₅ calculation, the two simple spin-2 channels have coefficients $`1+\alpha g^2/2`$ and $`-(1+\alpha g^2/2)`$, and the additional scalar has $`-128\alpha^2/9`$. For LOG, the spin-2 coefficients are $`(4-3L_0)/2`$ and $`-(4-3L_0)/2`$, and the additional scalar coefficient is $`-2(2-L_0)/L_0^4`$. These belong to the specified source field normalizations; magnitudes in different channels are not compared as normalization-independent observables. [Weyl² kinetic norms](../weyl2/ads5/details/kinetic_norms.md), [LOG kinetic norms](../log/ads5/details/kinetic_norms.md).

Opposite signs of distinct physical spin-2 poles obstruct positivity in the generic theory retaining all modes. At a critical point, the original operator and symplectic form replace simple-pole formulas. Signs of higher-spin longitudinal polarizations also belong to the relevant source analysis.

## Gauss–Bonnet on AdS₅

The [local spectrum table](../gauss_bonnet/ads5/spectrum.md) records positive kinetic weights on its regular branch `0<x<2`. The graviton and gravitino weights are `c=2-x`; the scalar and spinor weights are `2c/(3x^2)`; the two Maxwell weights are `2c` and `16c`. These are transcriptions in the source field normalization, relative to its positive two-derivative reference. See [Step 12](../gauss_bonnet/ads5/details/kinetic_norms.md).

At `x=2`, the raw quadratic action vanishes. The regular norm formulas and constraint reduction do not define a spectrum there. The [calculation guide](../gauss_bonnet/ads5/source_notes.md) states the scope of the analytic and numerical results.

## Boundary conditions versus norms

The scalar BF bounds $`M^2\ell_5^2\ge-4`$ in AdS₅ and $`M^2\ell_3^2\ge-1`$ in AdS₃ do not establish positive kinetic coefficients. Where both falloffs are normalizable, the boundary domain must be specified separately. The fixed-source/reflecting prescription in the AdS₅ sources is not generalized to other branches. Local B/F root matching does not replace a common global supersymmetric boundary domain.
