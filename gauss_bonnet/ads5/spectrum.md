# Physical spectrum and degrees of freedom for Gauss–Bonnet on AdS₅

<a id="step-14--physical-spectrum-and-degrees-of-freedom-on-gb-s"></a>

[Notation dictionary](../notation.md).

<!-- ASSERT_CONVENTION: natural_units=true, metric_signature=(-,+,+,+,+), curvature=GB04, action_lock=GB-FERMION-ACTION-0+2-v1, convention_lock=GB-FERMION-SPECTRUM-CONVENTIONS-v1, coupling_dimension=-2, fermion_bar=linear_Majorana -->

The spectrum follows the [quadratic action](quadratic_action.md), [constraint reduction](code/derivations/spectrum/STEP_09_FIELD_STATUS_AND_CONSTRAINTS.md), [eigenfields](details/masses_and_eigenfields.md) and [kinetic norms](details/kinetic_norms.md), using the component action through two physical fermions.

<a id="141-independent-local-counts"></a>

## Independent local counts

For the massless graviton the five diffeomorphisms and their associated constraints leave $`D(D-3)/2=5`$ polarizations in $`D=5`$. For a massless one-form the transverse little-group vector has $`D-2=3`$ components. For a massless two-form the physical little-group two-form has $`\binom{D-2}{2}=3`$ components. The scalar contributes one. The algebraic $`n`$, multiplier pair $`(v,e_3)`$ and $`v'`$ contribute none after the explicitly derived constraints and local gauges. Thus

```math
N_B=5+3+3+1=12.
\tag{14.1}
```

For fermions, the transverse little group is $`\mathrm{Spin}(3)`$. Its vector-spinor has $`3\times2`$ complex components; its gamma trace removes two, leaving four complex spin-$`3/2`$ components. A symplectic Majorana doublet gives the corresponding eight real physical gravitino components. The spin-$`1/2`$ little-group spinor has two complex, or four real, physical components for one symplectic Majorana doublet. The two eigenvalues of $`iJ`$ in (11.14) are related by the imposed reality condition and must not be counted as additional doublets. Therefore

```math
N_F=8+4=12.
\tag{14.2}
```

This count uses the gauge identity and spinor equations already derived. The subsequent [representation check](details/multiplets.md) verifies the energies, R-charge pairs and shortening of a massless gravity multiplet of $`8+8`$ and a vector multiplet of $`4+4`$. Its explicit flux transformations identify $`A-2Q`$ as the gravity vector and $`A+4Q`$ as the matter vector, and their kinetic cross term vanishes. Complete supersymmetry intertwining and closure on all fields are not claimed.

<a id="142-spectrum-table"></a>

## Spectrum table

The branch is $`x=2/(1+\sqrt{1+2a})`$, $`a=\lambda_{\rm GB}g^2>-1/2`$, $`g\ne0`$, $`c=2-x>0`$, $`k=-g^2x^2/2=-\mathcal L^{-2}`$, $`m=gx/(2\sqrt2)`$. The signed convention is $`(\not\nabla+\mu_s)q_s=0`$.

### Modes and local polarizations

| Mode | Original-field eigenmode | Spin | Operator or physical mass | Real DoF |
|---|---|---|---|---|
| Graviton | $`h=H`$, $`\ell=n=0`$; $`H`$ TT modulo residual diffeomorphisms | 2 | $`(\Box-2k)H=0`$; massless | 5 |
| Scalar | $`h_{\mu\nu}=-2\bar g_{\mu\nu}\ell/(3x)`$, $`n=-2gx\ell`$ | 0 | $`(\Box-4k)\ell=0`$; $`m_0^2\mathcal L^2=-4`$ | 1 |
| Maxwell field | $`A`$ Maxwell; $`H_2=0`$, $`v=-\sqrt2gxA`$ | 1 | $`(\Box-4k)A=0`$ in Lorenz gauge; massless | 3 |
| Dual form field | $`H_2=dQ`$, $`db=2*dQ`$, $`A=0`$, $`v=2\sqrt2gxQ`$ | 1, dual of a 2-form | $`(\Box-4k)Q=0`$; massless | 3 |
| Gravitino | $`\Psi=\Upsilon`$, $`\zeta=0`$; $`\Upsilon`$ transverse gamma-traceless modulo residual supersymmetry | $`3/2`$ | $`\mu_{3/2,s}=3sm`$; gauge-invariant AdS massless gravitino | 8 |
| Spinor | $`\Psi_a=i\sqrt2\gamma_aJ\zeta/(3x)`$, $`\Upsilon=0`$ | $`1/2`$ | $`\mu_{1/2,s}=sm`$ | 4 |

### Kinetic weights and local stability

| Mode | Kinetic weight | Local stability test |
|---|---|---|
| Graviton | $`c>0`$, Einstein reference | massless gauge operator |
| Scalar | $`2c/(3x^2)>0`$ | scalar BF saturation |
| Maxwell field | $`2c>0`$ | massless gauge operator |
| Dual form field | $`16c>0`$ after Legendre dualization | massless gauge operator |
| Gravitino | $`c>0`$, two-derivative reference | $`\lvert\mu\rvert\mathcal L=3/2`$, massless gauge identity |
| Spinor | $`2c/(3x^2)>0`$, two-derivative reference | real $`\mu`$, $`\lvert\mu\rvert\mathcal L=1/2`$ |

### Boundary data

| Mode | Global boundary admissibility |
|---|---|
| Graviton | not selected |
| Scalar | $`z^2`$ and $`z^2\log z`$ data not selected |
| Maxwell field | not selected |
| Dual form field | not selected; no global duality asserted |
| Gravitino | not selected |
| Spinor | local exponents $`3/2,5/2`$; data not selected |

Unlisted fields are reconstructed by the common constraints: $`e_3=0`$ locally, $`p=0`$, $`v'=0`$, with residual gauge gradients retained. Scalar and form eigenmodes have vanishing fermions; fermion eigenmodes have vanishing bosonic fluctuations. The equal numbers $`4k`$ in the scalar and Lorenz-Maxwell operators have different meanings: the former is a scalar mass squared, the latter a vector Ricci shift.

<a id="143-endpoint-limits-and-claim-boundary"></a>

## Endpoint, limits and claim boundary

At $`a=-1/2`$, $`x=2`$, $`c=0`$, the **entire raw quadratic action vanishes**. The generic constraints and count do not apply. This calculation establishes loss of quadratic control, not zero nonlinear degrees of freedom. Determining a spectrum there requires going beyond this linear approximation.

There is no additional finite interior kinetic zero or higher-derivative pole. The $`\lambda\to0`$ limit reproduces the direct two-derivative quadratic action; the fixed-$`\lambda`$, $`g\to0`$ limit is the flat massless $`12+12`$ spectrum. The $`a\to+\infty`$ compensator-patch boundary is a singular field-normalization limit, not an extra regular background.

The [verification report](code/CLAIMS.md) gives the reproducible local physics checks and their scope. Global AdS boundary conditions, normal-mode frequencies, topological sectors and renormalized boundary norms are outside this analysis.

## Norms, special branches and interpretation

| Question | Derivation |
|---|---|
| Kinetic signs and norm convention | [Reduced norms](details/kinetic_norms.md) |
| Singular kinetic coefficients and coincident roots | [Special branches](details/critical_branches.md) |
| Local masses versus boundary-admissible states | [Common stability definitions](../../common/kinetic_terms_and_stability.md) |
| Action and fermion conventions used in this table | [Component inputs](action_inputs.md) and [source definitions](source_notes.md) |
