# Generic AdS5 central charges and massless-vector kinetic terms

[Generic combination](../README.md) · [Reproduce this calculation](../../computations/generic_ads5_massless/README.md)

This result supplies citation-map item 23: equation (3.63) (`eq:acgen`) and equation (3.64) (`eq:uvgen`) of
draft v109. It uses the [common action](../../common/generic_action.md) with
the two-derivative coefficient one and all three coefficients
$`\alpha,\beta,\zeta`$ symbolic. The component action's $`R^2`$ coefficient $`\lambda`$
is $`\zeta`$ here. The overall factor is $`1/(2\kappa_5^2)`$.

## Background and domain

The [supersymmetric AdS5 background](../../computations/generic_ads5_massless/SOURCE_MAP.md#background-and-retained-fields)
has zero form strengths and

```math
\begin{aligned}
N_0&=-\frac32gL_0^2,&\ell^{-2}&=\frac12g^2L_0^2,\\
\tau&=(\beta+6\zeta)g^2,&Q&=\tau L_0^2-8L_0+8=0.
\end{aligned}
```

The couplings are real, $`g\ne0`$ and $`L_0>0`$. The paper selects
the Einstein-connected root $`L_0=2/(1+\sqrt{1-\tau/2})`$, for $`\tau\le2`$. The
algebraic identities below hold on $`Q=0`$ with $`L_0>0`$; choosing this root is
separate from the symbolic reduction. There is no small-coupling expansion.

## Central charges

Let the curvature terms of the constant-scalar action be
$`b_1R+b_2R^2+b_3R_{ab}R^{ab}+b_4R_{abcd}R^{abcd}`$. Their explicit
coefficients and source terms are in the
[source derivation](../../computations/generic_ads5_massless/SOURCE_MAP.md).
The holographic type-A coefficient follows from the AdS value of the
density, using [Myers--Sinha, equation (88)](https://arxiv.org/html/1011.5819#S5.SS3)
with $`d=4`$ and their Lagrangian equal to $`\mathcal F/(2\kappa_5^2)`$.
It is normalized to $`a=c=\pi^2\ell^3/\kappa_5^2`$ in the two-derivative vacuum.
The type-B coefficient is obtained from the massless
TT Einstein factor. Constant-background scalar mixing is in the trace sector;
the TT variation of $`R`$ vanishes. The curvature linearization uses
[Bueno--Cano--Min--Visser, section 2](https://arxiv.org/html/1610.08519v2#S2).

Writing $`P=\pi^2\ell^3/\kappa_5^2`$, the intermediate results are

```math
\begin{aligned}
a&=-\frac{\pi^2\ell^5}{8\kappa_5^2}\,\mathcal F_{\mathrm{AdS}},
&\frac{c}{P}&=b_1-2\ell^{-2}(20b_2+4b_3-2b_4),\\
\frac{a}{P}\Big|_{\text{before }Q=0}
&=-\frac14(3\tau L_0^2-12L_0+8),\\
\frac{c}{P}\Big|_{\text{before }Q=0}
&=L_0+\left(\frac\alpha2-\frac\beta2-3\zeta\right)g^2L_0^2.
\end{aligned}
```

These expressions impose the supersymmetric configuration, with $`b_1`$
evaluated at $`N=N_0`$, while leaving $`Q`$ unevaluated. Imposing $`Q=0`$ gives

```math
\begin{aligned}
a&=\frac{\pi^2\ell^3}{\kappa_5^2}(4-3L_0),
&c&=\frac{\pi^2\ell^3}{\kappa_5^2}
\left(4-3L_0+\frac12\alpha g^2L_0^2\right).
\end{aligned}
```

This is equation (3.63) (`eq:acgen`). In particular, $`c-a=\pi^2\alpha\ell/\kappa_5^2`$.
The background density alone cannot determine $`c`$: the Weyl invariant vanishes there but contributes to the TT
quadratic operator.

## Massless vectors

The fields $`c_\mu`$ and $`v_\mu`$ are the fluctuations of $`C_\mu`$ and the singlet $`V_\mu`$.
The [source derivation](../../computations/generic_ads5_massless/SOURCE_MAP.md)
retains the vector--form constraint, including the $`g`$-dependent $`E_3`$ contribution.
It projects the current action term by term before imposing the vacuum equation.
Define

```math
\begin{aligned}
B_0&=2-L_0,& C_0&=4-3L_0+\frac12\alpha g^2L_0^2,\\
Z_u&=6B_0,& Z_v&=\frac{2C_0}{3g^2L_0^2},\\
u_\mu&=c_\mu+\frac{\sqrt2}{3gL_0}v_\mu.
\end{aligned}
```

The massless kinetic density, inside the common gravitational prefactor, is

```math
\begin{aligned}
e^{-1}\mathcal L_{0,V}^{(2)}
&=-\frac14Z_u(du)^2-\frac14Z_v(dv)^2\\
&=-\frac32(2-L_0)(du)^2
-\frac{4-3L_0+\frac12\alpha g^2L_0^2}{6g^2L_0^2}(dv)^2.
\end{aligned}
```

There is no du.dv term. This is equation (3.64) (`eq:uvgen`), obtained with all three couplings
retained in the input action. Beta and zeta enter the displayed light
coefficients through Q and L0; their separate dependence remains in the full
vector--form matrix.

## An identity without division by critical coefficients

Use the exact-two-form potential h and spectral variable x defined in the
source derivation. After imposing the Bianchi constraint, write the density
as $`x\,\mathbf w^TK(x)\mathbf w`$, where $`\mathbf w=(c,v,h)^T`$, and set
$`K_0=K(0)`$. With

```math
\begin{aligned}
\Delta_H&=\alpha g^2L_0^2+12\zeta g^2L_0^2+2L_0-8,\\
\begin{pmatrix}c\\v\\h\end{pmatrix}
&=T\begin{pmatrix}u\\v\\\eta\end{pmatrix},
\qquad
T=\begin{pmatrix}
1&-\sqrt2/(3gL_0)&0\\
0&1&0\\
1/2&\sqrt2/(12gL_0)&1
\end{pmatrix},\\
T^T K_0 T&=\mathop{\mathrm{diag}}\nolimits
\left(3B_0,\frac{C_0}{3g^2L_0^2},\frac43\Delta_H\right),
\qquad \det T=1.
\end{aligned}
```

This congruence is checked as an exact symbolic identity modulo $`Q`$. Its
denominators contain only $`g`$ and $`L_0`$. The $`h`$ variable parametrizes a two-form
strength: its third entry is a form pivot, not a third physical massless
Maxwell field. For the ordinary isolated-pole interpretation require
$`B_0C_0\Delta_H\ne0`$. At their zeros the displayed polynomial coefficients and
congruence still apply, but the inverse-pole argument cannot classify the
additional degeneracies. No complete critical spectrum is claimed here.

## Verification record

The [36-check log](../../computations/generic_ads5_massless/outputs/verification.log)
records exact symbolic zero residuals. It includes the existing MS5 density
and tadpole checks, current versus rewritten vector representatives, a second
five-field calculation retaining a Lagrange multiplier, agreement at symbolic
x, the congruence above, and the Einstein, Weyl, LOG, R2 and common-GB limits.
The remaining coupling and g stay symbolic in the single-invariant limits.
The [machine-readable results](../../computations/generic_ads5_massless/outputs/results.json)
contain the full K(x), the coefficients before Q, and the input/producer hashes.

The common GB limit uses beta=2alpha and zeta=0. Conversion to the separate
GB spectrum action must use the [existing normalization map](../action_inputs.md);
this check does not establish an additional full fermionic equivalence.
The result covers the two cited equations and local kinetic coefficients,
not a full generic spectrum, boundary-norm analysis or product background.
