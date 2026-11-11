# From the action to a-maximization and c-extremization

This guide follows Sections 3.6 and 4.4 of the final paper. It connects the
Lagrangian inputs to equations (3.63)–(3.67) and (4.14)–(4.16), using the existing
calculations. The [citation index](paper_citation_map.md) gives the corresponding
paper references. Run the two read-only checks from the repository root:

```bash
python -B computations/generic_ads5_massless/checks.py
python -B computations/central_charge_extremization/checks.py
```

The first checks 36 identities in the action and massless-vector reduction;
the second checks 33 anomaly and extremization identities. Both keep the
couplings symbolic. Names in backticks below are identifiers in their reports.

## 1. Fix the action and the supersymmetric vacuum

Use the [four-invariant action](../generic_combination/action.md) with the
[normalization dictionary](../generic_combination/action_inputs.md): the
coefficient of the two-derivative density is one, and the three higher-derivative
coefficients are alpha, beta and zeta. The component action's R² coefficient
lambda is zeta in the paper's general-combination notation.

The [source projection](../computations/generic_ads5_massless/SOURCE_MAP.md)
retains constant scalars and the curvature invariants before imposing the
supersymmetric AdS₅ conditions. With the paper's positive g convention,

```math
\begin{aligned}
\tau&=(\beta+6\zeta)g^2,&
Q&=\tau L_0^2-8L_0+8=0,\\
N_0&=-\frac32gL_0^2,&
\ell^{-2}&=\frac12g^2L_0^2.
\end{aligned}
```

The paper selects the root connected to the two-derivative vacuum. The
massless-sector check verifies the action projection and the vacuum tadpoles;
its [source map](../computations/generic_ads5_massless/SOURCE_MAP.md) explains
which component terms enter. This fixes the normalization before computing a
central charge.

## 2. Read a and c from different parts of the same action

The AdS value of the Lagrangian determines a. The transverse traceless metric
operator determines c. With the common factor
$`\mathcal N=\pi^2\ell^3/\kappa^2`$, equation (3.63) is

```math
\begin{aligned}
a&=\mathcal N(4-3L_0),&
c&=\mathcal N\left(4-3L_0+\frac12\alpha g^2L_0^2\right).
\end{aligned}
```

See [central charges](../generic_combination/ads5/central_charges_and_massless_vectors.md#central-charges)
for the curvature coefficients before imposing Q = 0 and the adopted
holographic normalization. The massless-sector report's `eq:acgen/*` checks
compare these expressions with that action projection. The on-shell value
alone is insufficient for c: the Weyl invariant has zero value on this vacuum
but contributes to the metric quadratic action.

## 3. Identify the R-current and flavor-current directions

Equation (3.64) diagonalizes the two massless vectors by
$`u_\mu=c_\mu+\sqrt2v_\mu/(3gL_0)`$. Their kinetic coefficients are

```math
Z_u=6(2-L_0),\qquad
Z_v=\frac{2}{3g^2L_0^2}
\left(4-3L_0+\frac12\alpha g^2L_0^2\right),
```

in the convention $`-Z_u(du)^2/4-Z_v(dv)^2/4`$. The
[vector derivation](../generic_combination/ads5/central_charges_and_massless_vectors.md#massless-vectors)
keeps the form constraint. The `eq:uvgen/*` checks use both a constrained
reduction and a Lagrange multiplier, and verify the kinetic congruence without
dividing by the critical coefficients. The ordinary inverse-pole
interpretation still requires the regularity conditions stated there.

The charge-one R source is v = −2A_R with u = 0; the flavor source is u = A_F
with v = 0. The `normalized flavor coefficient` check fixes
$`C_F=24\pi^2\ell(2-L_0)/\kappa^2`$ using $`C_R=16c/3`$.

## 4. Obtain anomalies and the trial a-function

Follow the [Chern–Simons reduction](../generic_combination/ads5/anomalies_and_extremization.md#five-dimensional-source-and-anomaly-normalization).
The E-field Bianchi identity supplies part of the gauge Chern–Simons terms;
the higher-derivative invariants supply the remaining gauge and mixed
curvature terms. These are equation (3.66). Symmetrizing their cubic tensor
and choosing $`(C,V)=(\varepsilon,-2)A_R`$ gives the anomalies in (3.67).
The checks `CS reduction / matrix entry ...` and `eq:TrR cubic` verify these
coefficients with the stated anomaly-inflow normalization.

Insert the anomalies into
$`a(\varepsilon)=3(3\mathop{\mathrm{Tr}}\nolimits R^3-\mathop{\mathrm{Tr}}\nolimits R)/32`$.
For $`\varepsilon=2\sqrt2y/(3g)`$, equation (3.65) becomes

```math
\widehat a(y)=\frac{2\sqrt2\pi^2}{g^3\kappa^2}
\left(3y^2-2y^3-\frac34\tau y\right).
```

The checks `eq:atrial from anomalies` and
`trial a from current scalar-curvature action` compare the two routes.
`stationarity is vacuum polynomial` verifies that its stationary points
satisfy Q = 0. The `a maximum / current action a` and corresponding c check
recover (3.63). Finally, `R direction equals graviphoton` identifies the
extremizing current with u = 0, while
`a-maximization / flavor two-point coefficient` verifies
$`a''(\varepsilon_*)=-9C_F/16`$.

## 5. Reduce on the supersymmetric product family

Set $`(\alpha,\beta,\zeta)=(k/g^2,2k/g^2,0)`$ for Gauss–Bonnet. Insert the
[regular BPS background](../gauss_bonnet/product_backgrounds/supersymmetric_ads3_sigma2/action_inputs.md)
into the gauge Chern–Simons tensor, with fluxes p and r on Σ₂. The reduced
matrix determines the quadratic trial central charge. Its extremum yields
c_L of (4.14); the mixed gravitational term gives c_R − c_L.

The checks `eq:cLcR / extremized trial` and
`eq:cLcR / gravitational anomaly` verify these statements symbolically in L
and k. They use the chirality convention chi = +1 and the regular domain
specified in the [derivation](../generic_combination/ads5/anomalies_and_extremization.md#the-ads3-family).
The independent constant-level current matrix is compared entry by entry,
then `R-current level cL=3kR` checks its normalization. At k = 2/3 the trial
function is independent of mixing; the three `k=2/3 / ...` checks evaluate
that locus before division by the flavor anomaly.

## 6. Keep the flavor-mixing correction in the universal twist

For the universal twist the flux is aligned with the four-dimensional
superconformal R direction. Extremizing the two-dimensional mixing gives

```math
\begin{aligned}
c_L&=\frac{16}{3}(\mathsf g-1)(5a-3c)+\delta c,\\
c_R&=\frac{32}{3}(\mathsf g-1)a+\delta c,&
\delta c&=\frac{8(\mathsf g-1)(c-a)^2}{3c}.
\end{aligned}
```

These are (4.15)–(4.16) for a hyperbolic surface of genus greater than one, on the stated c ≠ 0 domain. The checks `eq:deltac`,
`eq:UTc left` and `eq:UTc right` verify the exact expressions; the final
first-order check confirms that the correction starts beyond linear order
in k. See the [full anomaly derivation](../generic_combination/ads5/anomalies_and_extremization.md)
for flux and genus conventions. The guide does not extend the paper's
boundary-condition or unitarity claims.
