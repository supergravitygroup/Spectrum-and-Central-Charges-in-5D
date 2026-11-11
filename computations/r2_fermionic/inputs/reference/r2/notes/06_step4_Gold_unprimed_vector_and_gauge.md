# Step 4 — Gold map and gauge simplification

## 1. Problem and Target

Apply **Gold et al. Eq. (4) to every unprimed vector occurrence** in [Step 3, Eq. (35)](05_step3_mixed_linear_inserted_in_BF.md), then evaluate the result in the gauge specified below. Show the ungauge-fixed substitution first, all surviving and vanishing terms next, and the collected gauge-restricted density last.

**Sources inspected for this calculation**

| Input | Local source and exact location |
|---|---|
| Unprimed vector map | Gold 2025 ([arXiv:2504.10856v1](../../../../../../references/bibliography.md#GoldEtAl2025)), Eq. (4), PDF pp. 5–6 |
| Gauge used in the main result | Gold Eq. (7), PDF p. 6: $`\sigma=1`$, $`b_\mu=0`$, $`\psi^i=0`$ |
| Derivatives and hatted strength | Coomans–Özkan 2013 ([publication](../../../../../../references/bibliography.md#CoomansOzkan2013)), Eqs. (2.16)–(2.18), PDF p. 8  |
| Gaugino transformation | Coomans (2.15), PDF p. 7; used only to identify the compensating S parameter |
| Conformal scalar box | Özkan 2016 ([arXiv:1608.00349v2](../../../../../../references/bibliography.md#Ozkan2016)), Eq. (3.21), PDF p. 11 |
| Full BF input | [Step 3](05_step3_mixed_linear_inserted_in_BF.md), distributed Eqs. (11),(14),(16),(21),(23),(24),(27),(29),(31); their exact source locks are retained |
| Reusable gauge/index audit | [Earlier defining-vector anchor, Sections 5.2–5.5](../../../../../two_derivative_fermionic/inputs/reference/results/gauged_two_derivative_fermionic_action/04_defining_vector_component_anchor.md); only its component definitions are used, not its two-derivative vector sum or normalization |

**Assumptions**

- **A1.** Off-shell substitution of the corrected locked Step 3 expression. Both mixed scalar-gradient coefficients are $`+i/4`$ under `R2-VL-GRADIENT-PHASE-v1`; other Özkan (3.20) coefficients are retained. This is a necessary correction under the locked Coomans rules, not a claim of a published erratum or complete local SUSY proof.
- **A2.** Gold's map acts on label 2 only: $`(\rho,\lambda^i,Y^{ij},A_\mu)`$. All label-1 vector entries retain their primes and their earlier-map role.
- **A3.** The main gauge slice, denoted $`|_{\rm gf}`$, is exactly Gold (7), with lock `R2-GOLD7-GAUGE-v1`. Work on a nonvanishing compensator patch admitting $`\sigma=1`$. The original triplet $`L_{ij}`$ is retained as a triplet in the main result. Its optional Gold (25) alignment is stated separately; no additional gauge is needed for the simplifications below.
- **A4.** The gaugino $`\psi^i`$ is set to zero; the gravitino $`\psi_\mu{}^i`$, original linear fermion $`\varphi^i`$, and primed vector fermion $`\lambda'^i`$ are retained. Full source fermion content is kept, including inside supercovariant quantities. This is not a bosonic or quadratic-fermion truncation.
- **A5.** All $`T,\chi,D`$ and dependent connections remain the common gauged Coomans composites. Their general higher-fermion completion and the primed vector map remain Steps 5–6 work. No source-omitted term is declared zero by this calculation.
- **A6.** No integration by parts, field equation, auxiliary elimination, dualization, or boundary discard. Equalities after gauge restriction mean equality of the parent densities evaluated on that slice, not equality to the unrestricted density for arbitrary fields.

## 2. Convention Ledger

<!-- ASSERT_CONVENTION: natural_units=hbar=c=1, metric_signature=mostly_plus (-++++), procedure_lock=R2-PRIMED-BF-CONSTRUCTION-FRAMEWORK-v1, gauge_slice=R2-GOLD7-GAUGE-v1 -->

The [branch conventions](../../../../derivations/component_conventions.md), Step 3 ledger, and [inherited convention handoff](../../../../../../common/README.md) are used without changing their geometric or spinor signs. The new gauge restriction is explicitly recorded, with the unrestrained parent preserved.

| Item | Convention |
|---|---|
| Dimension and indices | $`d=5`$, $`a,b,\ldots`$ and $`\mu,\nu,\ldots=0,\ldots,4`$; $`i,j=1,2`$ |
| Metric and orientation | $`\eta_{ab}=\mathrm{diag}(-,+,+,+,+)`$; frame $`\varepsilon^{01234}=+1`$, lower $`\varepsilon_{01234}=-1`$; world epsilon tensor is $`e^{-1}`$ times the coordinate symbol |
| Symmetrization | Unit weight, including $`1/2`$ for pairs and $`1/p!`$ in $`\gamma^{a_1\cdots a_p}`$ |
| Clifford rules | $`\{\gamma_a,\gamma_b\}=2\eta_{ab}`$, $`\gamma^{abcde}=i\varepsilon^{abcde}\mathbf1`$; gamma dots have no extra $`1/2`$ |
| $`SU(2)`$ | $`X^i=\varepsilon^{ij}X_j`$, $`X_i=X^j\varepsilon_{ji}`$, $`\varepsilon^{12}=\varepsilon_{12}=1`$ |
| Spinors and bar | Odd symplectic Majorana, $`\bar\lambda^i=(\lambda^i)^TC`$; $`C^T=-C`$; $`(C\gamma_a)^T=-C\gamma_a`$, $`(C\gamma_{ab})^T=C\gamma_{ab}`$ |
| Ordering and flips | Fixed-index $`t_0=t_1=+1`$, $`t_2=t_3=-1`$; a contracted NW–SE flip adds a minus. No spinor interchange or Fierz transformation is used below |
| Derivatives | The source $`\mathcal D`$ is an even supercovariant derivation. Gauge restriction follows evaluation of its component definition; it does not replace it by an ordinary derivative |
| Connections | Second-order dependent $`\omega,\phi,f`$, with gravitino contorsion, retained; $`\phi_\mu^i`$ denotes the S connection, not a linear-multiplet spinor |
| Curvature | $`R^\rho{}_{\sigma\mu\nu}=2\partial_{[\mu}\Gamma^\rho_{\nu]\sigma}+2\Gamma^\rho_{[\mu\vert\alpha\vert}\Gamma^\alpha_{\nu]\sigma}`$; $`R_{\mu\nu}=R^\rho{}_{\mu\rho\nu}`$; no curvature commutator is used |
| Gauging and normalization | $`g`$ is Gold's gauging parameter with pre-gauge Weyl weight zero. Keep the unit BF normalization and already-applied $`C_{1BC}`$ weights; $`\lambda_{R^2}`$ multiplies this source-normalized invariant in the [total action](12_total_action_zeroth_first_second_orders.md) |
| Functional variations | None; no left/right fermion functional derivative is invoked |

The metric, units, spinor ordering and coupling conventions are those in the table above. No perturbative approximation is made. A weight comparison after setting a weight-one compensator to the number 1 must restore that compensator power; gauge-fixed canonical dimensions are not substituted for the pre-gauge Weyl weights.

## 3. Definitions and Required Identities

### 3.1 Apply exactly Gold (4), with no new field names

```math
\begin{aligned}
\rho&\longmapsto\sigma, & A_\mu&\longmapsto C_\mu, & \lambda^i&\longmapsto\psi^i,\\
Y^{ij}&\longmapsto\frac{i}{4\sigma}\bar\psi^i\psi^j-\frac{g}{2\sigma}L^{ij},
&\widehat F_{ab}&\longmapsto\widehat G_{ab}.
\end{aligned}
\tag{1}
```

The lower triplet follows by lowering both indices, not by changing the sign by inspection:

```math
\begin{aligned}
Y_{ij}&=Y^{k\ell}\varepsilon_{ki}\varepsilon_{\ell j}\\
&\longmapsto \frac{i}{4\sigma}(\bar\psi^k\varepsilon_{ki})(\psi^\ell\varepsilon_{\ell j})
-\frac{g}{2\sigma}L^{k\ell}\varepsilon_{ki}\varepsilon_{\ell j}\\
&=\frac{i}{4\sigma}\bar\psi_i\psi_j-\frac{g}{2\sigma}L_{ij}.
\end{aligned}
\tag{2}
```

The two epsilons are even, so their movement causes no Grassmann sign. The scalar bilinear is the symmetric triplet already source-verified in the earlier anchor. This $`L_{ij}`$ is the **original unprimed linear input**, not the mixed output $`L'_{ij}`$.

### 3.2 Strength and derivative definitions before restricting the gauge

```math
\begin{aligned}
G_{\mu\nu}&=2\partial_{[\mu}C_{\nu]},\\
\widehat G_{\mu\nu}&=G_{\mu\nu}-\bar\psi_{[\mu}{}^i\gamma_{\nu]}\psi_i
+\frac i2\sigma\bar\psi_{[\mu}{}^i\psi_{\nu]i},\\
\widehat G_{ab}&=e_a{}^\mu e_b{}^\nu\widehat G_{\mu\nu},\qquad
\gamma\!\cdot\!\widehat G=\gamma^{ab}\widehat G_{ab},\qquad T^2=T_{ab}T^{ab}.
\end{aligned}
\tag{3}
```

```math
\begin{aligned}
\mathcal D_\mu\sigma&=(\partial_\mu-b_\mu)\sigma-\frac i2\bar\psi_\mu\psi,\\
\mathcal D_\mu\psi^i&=(\partial_\mu-\tfrac32b_\mu)\psi^i
+\frac14\omega_\mu{}^{ab}\gamma_{ab}\psi^i-V_\mu{}^{ij}\psi_j
+\frac14\gamma\!\cdot\!\widehat G\psi_\mu{}^i
+\frac i2(\not{\mathcal D}\sigma)\psi_\mu{}^i\\
&\quad+\left(\frac{i}{4\sigma}\bar\psi^i\psi^j-\frac{g}{2\sigma}L^{ij}\right)\psi_{\mu j}
-\sigma\gamma\!\cdot\!T\psi_\mu{}^i-\sigma\phi_\mu{}^i,\\
\Box_c\sigma&=(\partial^a-2b^a+\omega_b{}^{ba})\mathcal D_a\sigma
-\frac i2\bar\psi_a\mathcal D^a\psi-2\sigma\bar\psi_a\gamma^a\chi\\
&\quad+\frac12\bar\psi_a\gamma^a\gamma\!\cdot\!T\psi
+\frac12\bar\phi_a\gamma^a\psi+2f_a{}^a\sigma.
\end{aligned}
\tag{4}
```

These are the unprimed derivative occurrences in Step 3 after Gold substitution. The $`Y\psi_\mu`$ contribution has itself received Gold's map. A slash always means $`\gamma^a\mathcal D_a`$ acting on the immediately following field. A gauge restriction on a hatted tensor or its derivative always means restriction of its **parent supercovariant expression**.

### 3.3 Complete BF expression to be evaluated

The exact fermionic form bridge from Step 3 gives the nine insertion groups:

```math
\begin{aligned}
e^{-1}\mathcal L_{VL}={}&Y'^{ij}L'_{ij}+i\bar\lambda'{}^i\varphi'_i
-\frac12\bar\psi_a{}^i\gamma^a\lambda'{}^jL'_{ij}\\
&+A'_aE'^a+\frac i2A'_a\bar\psi_b{}^i\gamma^{ba}\varphi'_i
+\frac14A'_a\bar\psi_b{}^i\gamma^{abc}\psi_c{}^jL'_{ij}\\
&+\rho'N'+\frac{\rho'}2\bar\psi_a{}^i\gamma^a\varphi'_i
+\frac{i\rho'}4\bar\psi_a{}^i\gamma^{ab}\psi_b{}^jL'_{ij}.
\end{aligned}
\tag{5}
```

In Section 4.3 every right-hand side is already the Step 3 distributed expression with Gold applied. The $`L',\varphi',E',N'`$ on the left are only labels for their existing BF insertion group, not fields left in the final action. The potential term's two additional fermion couplings are retained.

## 4. Detailed Derivation

### 4.1 Impose Gold (7) on the correctly mapped components

<!-- ASSERT_CONVENTION: natural_units=hbar=c=1, metric_signature=mostly_plus (-++++), procedure_lock=R2-PRIMED-BF-CONSTRUCTION-FRAMEWORK-v1, gauge_slice=R2-GOLD7-GAUGE-v1 -->

```math
\left.\sigma\right|_{\rm gf}=1,\qquad
\left.b_\mu\right|_{\rm gf}=0,\qquad
\left.\psi^i\right|_{\rm gf}=0,\qquad
\left.\rho\right|_{\rm Gold,gf}=1,\qquad
\left.\lambda^i\right|_{\rm Gold,gf}=0.
\tag{6}
```

```math
\left.Y_{ij}\right|_{\rm Gold,gf}
=\frac i4\,0\cdot0-\frac g2L_{ij}=-\frac g2L_{ij},\qquad
\left.Y^{ij}\right|_{\rm Gold,gf}=-\frac g2L^{ij}.
\tag{7}
```

Apply the gauge to each term of the strength definition. The term with the gaugino vanishes, while the term with two gravitini remains:

```math
\begin{aligned}
\left.\widehat G_{\mu\nu}\right|_{\rm gf}
&=G_{\mu\nu}-\bar\psi_{[\mu}{}^i\gamma_{\nu]}\,0
+\frac i2(1)\bar\psi_{[\mu}{}^i\psi_{\nu]i}\\
&=G_{\mu\nu}+\frac i2\bar\psi_{[\mu}{}^i\psi_{\nu]i}.
\end{aligned}
\tag{8}
```

Thus $`\widehat G`$ in the following restricted expressions includes this bilinear. It is not set equal to $`G`$ in a fermionic calculation. From the scalar derivative,

```math
\left.\mathcal D_\mu\sigma\right|_{\rm gf}
=(\partial_\mu-0)1-\frac i2\bar\psi_\mu\,0=0,
\qquad \left.\not{\mathcal D}\sigma\right|_{\rm gf}=0.
\tag{9}
```

Now evaluate each term of the gaugino derivative **before** discarding the gauge-fixed gaugino:

```math
\begin{aligned}
\left.\mathcal D_\mu\psi^i\right|_{\rm gf}
&=(\partial_\mu+\tfrac14\omega_\mu{}^{ab}\gamma_{ab})0-V_\mu{}^{ij}0
+\frac14\gamma\!\cdot\!\widehat G\psi_\mu{}^i+\frac i2(0)\psi_\mu{}^i\\
&\quad-\frac g2L^{ij}\psi_{\mu j}-\gamma\!\cdot\!T\psi_\mu{}^i-\phi_\mu{}^i\\
&=\frac14\gamma\!\cdot\!\widehat G\psi_\mu{}^i
-\gamma\!\cdot\!T\psi_\mu{}^i-\frac g2L^{ij}\psi_{\mu j}-\phi_\mu{}^i.
\end{aligned}
\tag{10}
```

For the lower free index used in Step 3, insert the NW–SE epsilons explicitly:

```math
\begin{aligned}
L^{kj}\psi_{\mu j}\varepsilon_{ki}
&=\varepsilon^{km}\varepsilon^{jn}L_{mn}\psi_\mu{}^\ell\varepsilon_{\ell j}\varepsilon_{ki}\\
&=\delta_i{}^m(-\delta_\ell{}^n)L_{mn}\psi_\mu{}^\ell
=-L_{ij}\psi_\mu{}^j,\\
\left.\mathcal D_a\psi_i\right|_{\rm gf}
&=\frac14\gamma\!\cdot\!\widehat G\psi_{ai}
-\gamma\!\cdot\!T\psi_{ai}+\frac g2L_{ij}\psi_a{}^j-\phi_{ai}.
\end{aligned}
\tag{11}
```

The $`+g/2`$ sign in the last line is consequently fixed. No odd spinors were interchanged. The fact that $`\psi_i=0`$ does not annihilate this covariant derivative.

For the scalar box, the first term vanishes by the displayed zero of $`\mathcal D_a\sigma`$, and the two terms with an undifferentiated gaugino vanish. The remaining terms are

```math
\begin{aligned}
\left.\Box_c\sigma\right|_{\rm gf}
&=(\partial^a+\omega_b{}^{ba})0
-\frac i2\bar\psi_a{}^i\left.\mathcal D^a\psi_i\right|_{\rm gf}
-2\bar\psi_a\gamma^a\chi+0+0+2f_a{}^a\\
&=2f_a{}^a-\frac i2\bar\psi_a{}^i\left(
\frac14\gamma\!\cdot\!\widehat G\psi^a_i
-\gamma\!\cdot\!T\psi^a_i+\frac g2L_{ij}\psi^{aj}-\phi^a_i\right)
-2\bar\psi_a\gamma^a\chi.
\end{aligned}
\tag{12}
```

This nonzero box is the restriction of a weight-one conformal scalar, not the ordinary Laplacian of the constant number 1. It retains the dependent K connection $`f_a{}^a`$.

The gauge is compatible with retaining local supersymmetry through compensating transformations. For example source Coomans (2.15) gives, on this slice,

```math
\begin{aligned}
0=\left.\delta\psi^i\right|_{\rm gf}
&=-\frac14\gamma\!\cdot\!\widehat G\epsilon^i
+\gamma\!\cdot\!T\epsilon^i+\frac g2L^{ij}\epsilon_j+\eta^i,\\
\eta^i&=\left(\frac14\gamma\!\cdot\!\widehat G-\gamma\!\cdot\!T\right)\epsilon^i
-\frac g2L^{ij}\epsilon_j.
\end{aligned}
\tag{13}
```

This identifies the needed S compensation; it is not an auxiliary equation or a proof of the full action variation. Dilatations fix the nonzero $`\sigma`$, and special conformal transformations fix $`b_\mu`$. Lorentz, diffeomorphism, Abelian and $`SU(2)`$ gauge freedom have not been removed by (7).

### 4.2 Restrict derivative products, including those containing a zero gaugino

<!-- ASSERT_CONVENTION: natural_units=hbar=c=1, metric_signature=mostly_plus (-++++), procedure_lock=R2-PRIMED-BF-CONSTRUCTION-FRAMEWORK-v1, gauge_slice=R2-GOLD7-GAUGE-v1 -->

```math
\begin{aligned}
\left.\mathcal D_b(\bar\lambda'\gamma^{ab}\psi)\right|_{\rm gf}
&=\left.(\mathcal D_b\bar\lambda')\gamma^{ab}\psi\right|_{\rm gf}
+\left.\bar\lambda'\gamma^{ab}\mathcal D_b\psi\right|_{\rm gf}\\
&=0+\bar\lambda'{}^i\gamma^{ab}
\left(\frac14\gamma\!\cdot\!\widehat G\psi_{bi}
-\gamma\!\cdot\!T\psi_{bi}+\frac g2L_{ij}\psi_b{}^j-\phi_{bi}\right).
\end{aligned}
\tag{14}
```

The plus sign in the product rule follows because $`\mathcal D_b`$ is even. No source spinor order is reversed. Dropping the bilinear before taking its source covariant derivative would incorrectly remove the second term.

The scalar products in the constrained-vector part give

```math
\begin{aligned}
\left.\mathcal D_b(\rho'\widehat G^{ab})\right|_{\rm gf}
&=(\mathcal D_b\rho')\widehat G^{ab}+\rho'\mathcal D_b\widehat G^{ab},\\
\left.\mathcal D_b(\sigma\widehat F'^{ab})\right|_{\rm gf}
&=0\cdot\widehat F'^{ab}+\mathcal D_b\widehat F'^{ab},\\
\left.\mathcal D_b(\rho'\sigma T^{ab})\right|_{\rm gf}
&=(\mathcal D_b\rho')T^{ab}+\rho'(0)T^{ab}+\rho'\mathcal D_bT^{ab}.
\end{aligned}
\tag{15}
```

All quantities on the right are understood as restricted parent quantities. In particular $`\mathcal D_b\widehat G^{ab}`$ is the restricted supercovariant derivative of the mapped strength, not $`\partial_bG^{ab}`$. Its gauge-fixed field-value definition does not remove its superconformal connection terms.

### 4.3 Apply the map and gauge to every BF group

Each subsection first shows the full Gold substitution **before** the gauge is imposed, followed by all surviving terms in the gauge. The ordering and external primed BF arguments are exactly those of Step 3. All hatted quantities and derivatives in a gauge-restricted equation are restricted parent quantities. Only the explicit gaugino zeros and the proven $`\mathcal D\sigma=0`$ are used to remove rows.

#### Triplet product — Step 3 Eq. (11)

<!-- ASSERT_CONVENTION: natural_units=hbar=c=1, metric_signature=mostly_plus (-++++), procedure_lock=R2-PRIMED-BF-CONSTRUCTION-FRAMEWORK-v1, gauge_slice=R2-GOLD7-GAUGE-v1 -->

<!-- BEGIN GOLD YL -->

```math
\begin{aligned}\left.Y'^{ij}L'_{ij}\right|_{\rm Gold}={}&\rho'Y'^{ij}\left(\frac{i}{4\sigma}\bar\psi_i\psi_j-\frac{g}{2\sigma}L_{ij}\right)+\sigma Y'^{ij}Y'_{ij}
-\frac i2Y'^{ij}\bar\lambda'_{(i}\psi_{j)}.
\end{aligned}
\tag{16}
```

<!-- END GOLD YL -->

Insert the gauge values into each displayed factor. The surviving Step 3 row numbers are 1, 2. Rows 3 vanish; their zero factors are listed explicitly after these nine substitutions. The surviving density contribution is

<!-- BEGIN GAUGE YL -->

```math
\begin{aligned}\left.Y'^{ij}L'_{ij}\right|_{\rm Gold,gf}={}&Y'^{ij}Y'_{ij}-\frac g2\rho'Y'^{ij}L_{ij}.
\end{aligned}
\tag{17}
```

<!-- END GAUGE YL -->

#### External primed gaugino — Step 3 Eq. (14)

<!-- ASSERT_CONVENTION: natural_units=hbar=c=1, metric_signature=mostly_plus (-++++), procedure_lock=R2-PRIMED-BF-CONSTRUCTION-FRAMEWORK-v1, gauge_slice=R2-GOLD7-GAUGE-v1 -->

<!-- BEGIN GOLD LP -->

```math
\begin{aligned}\left.i\bar\lambda'{}^i\varphi'_i\right|_{\rm Gold}={}&
-\frac{\rho'}2\bar\lambda'{}^i\not{\mathcal D}\psi_i
-\frac\sigma2\bar\lambda'{}^i\not{\mathcal D}\lambda'_i\\
&+i\rho'\bar\lambda'{}^i\gamma\!\cdot\!T\psi_i
+i\sigma\bar\lambda'{}^i\gamma\!\cdot\!T\lambda'_i
-8i\rho'\sigma\bar\lambda'{}^i\chi_i\\
&-\frac i8\bar\lambda'{}^i\gamma\!\cdot\!\widehat F'\psi_i
-\frac i8\bar\lambda'{}^i\gamma\!\cdot\!\widehat G\lambda'_i\\
&-\frac14\bar\lambda'{}^i(\not{\mathcal D}\rho')\psi_i
-\frac14\bar\lambda'{}^i(\not{\mathcal D}\sigma)\lambda'_i\\
&-\frac i2\bar\lambda'{}^iY'_{ij}\psi^j
-\frac i2\bar\lambda'{}^i\left(\frac{i}{4\sigma}\bar\psi_i\psi_j-\frac{g}{2\sigma}L_{ij}\right)\lambda'{}^j.
\end{aligned}
\tag{18}
```

<!-- END GOLD LP -->

Insert the gauge values into each displayed factor. The surviving Step 3 row numbers are 1, 2, 4, 5, 7, 11. Rows 3, 6, 8, 9, 10 vanish; their zero factors are listed explicitly after these nine substitutions. The surviving density contribution is

<!-- BEGIN GAUGE LP -->

```math
\begin{aligned}\left.i\bar\lambda'{}^i\varphi'_i\right|_{\rm Gold,gf}={}&-\frac{\rho'}2\bar\lambda'{}^i\not{\mathcal D}\psi_i
-\frac12\bar\lambda'{}^i\not{\mathcal D}\lambda'_i
+i\bar\lambda'{}^i\gamma\!\cdot\!T\lambda'_i
-8i\rho'\bar\lambda'{}^i\chi_i\\
&-\frac i8\bar\lambda'{}^i\gamma\!\cdot\!\widehat G\lambda'_i
+\frac{ig}4\bar\lambda'{}^iL_{ij}\lambda'{}^j.
\end{aligned}
\tag{19}
```

<!-- END GAUGE LP -->

#### Gravitino–primed-gaugino product — Step 3 Eq. (16)

<!-- ASSERT_CONVENTION: natural_units=hbar=c=1, metric_signature=mostly_plus (-++++), procedure_lock=R2-PRIMED-BF-CONSTRUCTION-FRAMEWORK-v1, gauge_slice=R2-GOLD7-GAUGE-v1 -->

<!-- BEGIN GOLD PSL -->

```math
\begin{aligned}\left.-\frac12\bar\psi_a{}^i\gamma^a\lambda'{}^jL'_{ij}\right|_{\rm Gold}={}&
-\frac{\rho'}2\bar\psi_a{}^i\gamma^a\lambda'{}^j\left(\frac{i}{4\sigma}\bar\psi_i\psi_j-\frac{g}{2\sigma}L_{ij}\right)
-\frac\sigma2\bar\psi_a{}^i\gamma^a\lambda'{}^jY'_{ij}\\
&+\frac i4\left(\bar\psi_a{}^i\gamma^a\lambda'{}^j\right)
\left(\bar\lambda'_{(i}\psi_{j)}\right).
\end{aligned}
\tag{20}
```

<!-- END GOLD PSL -->

Insert the gauge values into each displayed factor. The surviving Step 3 row numbers are 1, 2. Rows 3 vanish; their zero factors are listed explicitly after these nine substitutions. The surviving density contribution is

<!-- BEGIN GAUGE PSL -->

```math
\begin{aligned}\left.-\frac12\bar\psi_a{}^i\gamma^a\lambda'{}^jL'_{ij}\right|_{\rm Gold,gf}={}&+\frac g4\rho'\bar\psi_a{}^i\gamma^a\lambda'{}^jL_{ij}
-\frac12\bar\psi_a{}^i\gamma^a\lambda'{}^jY'_{ij}.
\end{aligned}
\tag{21}
```

<!-- END GAUGE PSL -->

#### Constrained-vector contribution — Step 3 Eq. (21)

<!-- ASSERT_CONVENTION: natural_units=hbar=c=1, metric_signature=mostly_plus (-++++), procedure_lock=R2-PRIMED-BF-CONSTRUCTION-FRAMEWORK-v1, gauge_slice=R2-GOLD7-GAUGE-v1 -->

<!-- BEGIN GOLD AE -->

```math
\begin{aligned}\left.A'_aE'^a\right|_{\rm Gold}={}&-\frac12A'_a(\mathcal D_b\rho')\widehat G^{ab}
-\frac12A'_a\rho'\mathcal D_b\widehat G^{ab}\\
&-\frac12A'_a(\mathcal D_b\sigma)\widehat F'^{ab}
-\frac12A'_a\sigma\mathcal D_b\widehat F'^{ab}\\
&+8A'_a(\mathcal D_b\rho')\sigma T^{ab}
+8A'_a\rho'(\mathcal D_b\sigma)T^{ab}
+8A'_a\rho'\sigma\mathcal D_bT^{ab}\\
&-\frac i4A'_a(\mathcal D_b\bar\lambda')\gamma^{ab}\psi
-\frac i4A'_a\bar\lambda'\gamma^{ab}\mathcal D_b\psi
-\frac18A'_a\varepsilon^{abcde}\widehat F'_{bc}\widehat G_{de}.
\end{aligned}
\tag{22}
```

<!-- END GOLD AE -->

Insert the gauge values into each displayed factor. The surviving Step 3 row numbers are 1, 2, 4, 5, 7, 9, 10. Rows 3, 6, 8 vanish; their zero factors are listed explicitly after these nine substitutions. The surviving density contribution is

<!-- BEGIN GAUGE AE -->

```math
\begin{aligned}\left.A'_aE'^a\right|_{\rm Gold,gf}={}&-\frac12A'_a(\mathcal D_b\rho')\widehat G^{ab}
-\frac12A'_a\rho'\mathcal D_b\widehat G^{ab}
-\frac12A'_a\mathcal D_b\widehat F'^{ab}\\
&+8A'_a(\mathcal D_b\rho')T^{ab}+8A'_a\rho'\mathcal D_bT^{ab}
-\frac i4A'_a\bar\lambda'{}^i\gamma^{ab}\mathcal D_b\psi_i
-\frac18A'_a\varepsilon^{abcde}\widehat F'_{bc}\widehat G_{de}.
\end{aligned}
\tag{23}
```

<!-- END GAUGE AE -->

#### First fermionic form-bridge term — Step 3 Eq. (23)

<!-- ASSERT_CONVENTION: natural_units=hbar=c=1, metric_signature=mostly_plus (-++++), procedure_lock=R2-PRIMED-BF-CONSTRUCTION-FRAMEWORK-v1, gauge_slice=R2-GOLD7-GAUGE-v1 -->

<!-- BEGIN GOLD APP -->

```math
\begin{aligned}\left.\frac i2A'_a\bar\psi_b{}^i\gamma^{ba}\varphi'_i\right|_{\rm Gold}={}&
-\frac14A'_a\rho'\bar\psi_b{}^i\gamma^{ba}\not{\mathcal D}\psi_i
-\frac14A'_a\sigma\bar\psi_b{}^i\gamma^{ba}\not{\mathcal D}\lambda'_i\\
&+\frac i2A'_a\rho'\bar\psi_b{}^i\gamma^{ba}\gamma\!\cdot\!T\psi_i
+\frac i2A'_a\sigma\bar\psi_b{}^i\gamma^{ba}\gamma\!\cdot\!T\lambda'_i\\
&-4iA'_a\rho'\sigma\bar\psi_b{}^i\gamma^{ba}\chi_i\\
&-\frac i{16}A'_a\bar\psi_b{}^i\gamma^{ba}\gamma\!\cdot\!\widehat F'\psi_i
-\frac i{16}A'_a\bar\psi_b{}^i\gamma^{ba}\gamma\!\cdot\!\widehat G\lambda'_i\\
&-\frac18A'_a\bar\psi_b{}^i\gamma^{ba}(\not{\mathcal D}\rho')\psi_i
-\frac18A'_a\bar\psi_b{}^i\gamma^{ba}(\not{\mathcal D}\sigma)\lambda'_i\\
&-\frac i4A'_a\bar\psi_b{}^i\gamma^{ba}Y'_{ij}\psi^j
-\frac i4A'_a\bar\psi_b{}^i\gamma^{ba}\left(\frac{i}{4\sigma}\bar\psi_i\psi_j-\frac{g}{2\sigma}L_{ij}\right)\lambda'{}^j.
\end{aligned}
\tag{24}
```

<!-- END GOLD APP -->

Insert the gauge values into each displayed factor. The surviving Step 3 row numbers are 1, 2, 4, 5, 7, 11. Rows 3, 6, 8, 9, 10 vanish; their zero factors are listed explicitly after these nine substitutions. The surviving density contribution is

<!-- BEGIN GAUGE APP -->

```math
\begin{aligned}\left.\frac i2A'_a\bar\psi_b{}^i\gamma^{ba}\varphi'_i\right|_{\rm Gold,gf}={}&-\frac14A'_a\rho'\bar\psi_b{}^i\gamma^{ba}\not{\mathcal D}\psi_i
-\frac14A'_a\bar\psi_b{}^i\gamma^{ba}\not{\mathcal D}\lambda'_i\\
&+\frac i2A'_a\bar\psi_b{}^i\gamma^{ba}\gamma\!\cdot\!T\lambda'_i
-4iA'_a\rho'\bar\psi_b{}^i\gamma^{ba}\chi_i\\
&-\frac i{16}A'_a\bar\psi_b{}^i\gamma^{ba}\gamma\!\cdot\!\widehat G\lambda'_i
+\frac{ig}8A'_a\bar\psi_b{}^i\gamma^{ba}L_{ij}\lambda'{}^j.
\end{aligned}
\tag{25}
```

<!-- END GAUGE APP -->

#### Second fermionic form-bridge term — Step 3 Eq. (24)

<!-- ASSERT_CONVENTION: natural_units=hbar=c=1, metric_signature=mostly_plus (-++++), procedure_lock=R2-PRIMED-BF-CONSTRUCTION-FRAMEWORK-v1, gauge_slice=R2-GOLD7-GAUGE-v1 -->

<!-- BEGIN GOLD APL -->

```math
\begin{aligned}\left.\frac14A'_a\bar\psi_b{}^i\gamma^{abc}\psi_c{}^jL'_{ij}\right|_{\rm Gold}={}&
+\frac{\rho'}4A'_a\bar\psi_b{}^i\gamma^{abc}\psi_c{}^j\left(\frac{i}{4\sigma}\bar\psi_i\psi_j-\frac{g}{2\sigma}L_{ij}\right)
+\frac\sigma4A'_a\bar\psi_b{}^i\gamma^{abc}\psi_c{}^jY'_{ij}\\
&-\frac i8A'_a\left(\bar\psi_b{}^i\gamma^{abc}\psi_c{}^j\right)
\left(\bar\lambda'_{(i}\psi_{j)}\right).
\end{aligned}
\tag{26}
```

<!-- END GOLD APL -->

Insert the gauge values into each displayed factor. The surviving Step 3 row numbers are 1, 2. Rows 3 vanish; their zero factors are listed explicitly after these nine substitutions. The surviving density contribution is

<!-- BEGIN GAUGE APL -->

```math
\begin{aligned}\left.\frac14A'_a\bar\psi_b{}^i\gamma^{abc}\psi_c{}^jL'_{ij}\right|_{\rm Gold,gf}={}&-\frac g8A'_a\rho'\bar\psi_b{}^i\gamma^{abc}\psi_c{}^jL_{ij}
+\frac14A'_a\bar\psi_b{}^i\gamma^{abc}\psi_c{}^jY'_{ij}.
\end{aligned}
\tag{27}
```

<!-- END GAUGE APL -->

#### Scalar–top-component product — Step 3 Eq. (27)

<!-- ASSERT_CONVENTION: natural_units=hbar=c=1, metric_signature=mostly_plus (-++++), procedure_lock=R2-PRIMED-BF-CONSTRUCTION-FRAMEWORK-v1, gauge_slice=R2-GOLD7-GAUGE-v1 -->

<!-- BEGIN GOLD RN -->

```math
\begin{aligned}\left.\rho'N'\right|_{\rm Gold}={}&\frac12(\rho')^2\Box_c\sigma+\frac12\rho'\sigma\Box_c\rho'
+\frac12\rho'\mathcal D_a\rho'\mathcal D^a\sigma\\
&-\frac14\rho'\widehat F'_{ab}\widehat G^{ab}+\rho'Y'_{ij}\left(\frac{i}{4\sigma}\bar\psi^i\psi^j-\frac{g}{2\sigma}L^{ij}\right)
+4(\rho')^2\widehat G_{ab}T^{ab}+4\rho'\sigma\widehat F'_{ab}T^{ab}\\
&-4(\rho')^2\sigma D-\frac{104}{3}(\rho')^2\sigma T^2\\
&-\frac14\rho'\bar\lambda'\not{\mathcal D}\psi
-\frac14\rho'\bar\psi\not{\mathcal D}\lambda'
+i\rho'\bar\lambda'\gamma\!\cdot\!T\psi\\
&+8i(\rho')^2\bar\chi\psi+8i\rho'\sigma\bar\chi\lambda'.
\end{aligned}
\tag{28}
```

<!-- END GOLD RN -->

Insert the gauge values into each displayed factor. The surviving Step 3 row numbers are 1, 2, 4, 5, 6, 7, 8, 9, 10, 14. Rows 3, 11, 12, 13 vanish; their zero factors are listed explicitly after these nine substitutions. The surviving density contribution is

<!-- BEGIN GAUGE RN -->

```math
\begin{aligned}\left.\rho'N'\right|_{\rm Gold,gf}={}&+\frac12(\rho')^2\Box_c\sigma+\frac12\rho'\Box_c\rho'
-\frac14\rho'\widehat F'_{ab}\widehat G^{ab}-\frac g2\rho'Y'_{ij}L^{ij}\\
&+4(\rho')^2\widehat G_{ab}T^{ab}+4\rho'\widehat F'_{ab}T^{ab}
-4(\rho')^2D-\frac{104}{3}(\rho')^2T^2\\
&-\frac14\rho'\bar\lambda'{}^i\not{\mathcal D}\psi_i+8i\rho'\bar\chi\lambda' .
\end{aligned}
\tag{29}
```

<!-- END GAUGE RN -->

#### Scalar–gravitino–linear-fermion product — Step 3 Eq. (29)

<!-- ASSERT_CONVENTION: natural_units=hbar=c=1, metric_signature=mostly_plus (-++++), procedure_lock=R2-PRIMED-BF-CONSTRUCTION-FRAMEWORK-v1, gauge_slice=R2-GOLD7-GAUGE-v1 -->

<!-- BEGIN GOLD RPP -->

```math
\begin{aligned}\left.\frac{\rho'}2\bar\psi_a{}^i\gamma^a\varphi'_i\right|_{\rm Gold}={}&
+\frac i4(\rho')^2\bar\psi_a{}^i\gamma^a\not{\mathcal D}\psi_i
+\frac i4\rho'\sigma\bar\psi_a{}^i\gamma^a\not{\mathcal D}\lambda'_i\\
&+\frac12(\rho')^2\bar\psi_a{}^i\gamma^a\gamma\!\cdot\!T\psi_i
+\frac12\rho'\sigma\bar\psi_a{}^i\gamma^a\gamma\!\cdot\!T\lambda'_i\\
&-4(\rho')^2\sigma\bar\psi_a{}^i\gamma^a\chi_i\\
&-\frac1{16}\rho'\bar\psi_a{}^i\gamma^a\gamma\!\cdot\!\widehat F'\psi_i
-\frac1{16}\rho'\bar\psi_a{}^i\gamma^a\gamma\!\cdot\!\widehat G\lambda'_i\\
&+\frac i8\rho'\bar\psi_a{}^i\gamma^a(\not{\mathcal D}\rho')\psi_i
+\frac i8\rho'\bar\psi_a{}^i\gamma^a(\not{\mathcal D}\sigma)\lambda'_i\\
&-\frac14\rho'\bar\psi_a{}^i\gamma^aY'_{ij}\psi^j
-\frac14\rho'\bar\psi_a{}^i\gamma^a\left(\frac{i}{4\sigma}\bar\psi_i\psi_j-\frac{g}{2\sigma}L_{ij}\right)\lambda'{}^j.
\end{aligned}
\tag{30}
```

<!-- END GOLD RPP -->

Insert the gauge values into each displayed factor. The surviving Step 3 row numbers are 1, 2, 4, 5, 7, 11. Rows 3, 6, 8, 9, 10 vanish; their zero factors are listed explicitly after these nine substitutions. The surviving density contribution is

<!-- BEGIN GAUGE RPP -->

```math
\begin{aligned}\left.\frac{\rho'}2\bar\psi_a{}^i\gamma^a\varphi'_i\right|_{\rm Gold,gf}={}&+\frac i4(\rho')^2\bar\psi_a{}^i\gamma^a\not{\mathcal D}\psi_i
+\frac i4\rho'\bar\psi_a{}^i\gamma^a\not{\mathcal D}\lambda'_i\\
&+\frac12\rho'\bar\psi_a{}^i\gamma^a\gamma\!\cdot\!T\lambda'_i
-4(\rho')^2\bar\psi_a{}^i\gamma^a\chi_i\\
&-\frac1{16}\rho'\bar\psi_a{}^i\gamma^a\gamma\!\cdot\!\widehat G\lambda'_i
+\frac g8\rho'\bar\psi_a{}^i\gamma^aL_{ij}\lambda'{}^j.
\end{aligned}
\tag{31}
```

<!-- END GAUGE RPP -->

#### Final two-gravitino product — Step 3 Eq. (31)

<!-- ASSERT_CONVENTION: natural_units=hbar=c=1, metric_signature=mostly_plus (-++++), procedure_lock=R2-PRIMED-BF-CONSTRUCTION-FRAMEWORK-v1, gauge_slice=R2-GOLD7-GAUGE-v1 -->

<!-- BEGIN GOLD RPL -->

```math
\begin{aligned}\left.\frac{i\rho'}4\bar\psi_a{}^i\gamma^{ab}\psi_b{}^jL'_{ij}\right|_{\rm Gold}={}&
+\frac i4(\rho')^2\bar\psi_a{}^i\gamma^{ab}\psi_b{}^j\left(\frac{i}{4\sigma}\bar\psi_i\psi_j-\frac{g}{2\sigma}L_{ij}\right)
+\frac i4\rho'\sigma\bar\psi_a{}^i\gamma^{ab}\psi_b{}^jY'_{ij}\\
&+\frac{\rho'}8\left(\bar\psi_a{}^i\gamma^{ab}\psi_b{}^j\right)
\left(\bar\lambda'_{(i}\psi_{j)}\right).
\end{aligned}
\tag{32}
```

<!-- END GOLD RPL -->

Insert the gauge values into each displayed factor. The surviving Step 3 row numbers are 1, 2. Rows 3 vanish; their zero factors are listed explicitly after these nine substitutions. The surviving density contribution is

<!-- BEGIN GAUGE RPL -->

```math
\begin{aligned}\left.\frac{i\rho'}4\bar\psi_a{}^i\gamma^{ab}\psi_b{}^jL'_{ij}\right|_{\rm Gold,gf}={}&-\frac{ig}8(\rho')^2\bar\psi_a{}^i\gamma^{ab}\psi_b{}^jL_{ij}
+\frac i4\rho'\bar\psi_a{}^i\gamma^{ab}\psi_b{}^jY'_{ij}.
\end{aligned}
\tag{33}
```

<!-- END GAUGE RPL -->

For the triplet coefficients, the common multiplications are $`1(-g/2)=-g/2`$, $`(-1/2)(-g/2)=+g/4`$, $`(1/4)(-g/2)=-g/8`$, and $`(i/4)(-g/2)=-ig/8`$. In the three linear-spinor insertions, $`(-i/2)(-g/2)=+ig/4`$, $`(-i/4)(-g/2)=+ig/8`$ and $`(-1/4)(-g/2)=+g/8`$. These are the coefficients shown above; no additional $`C_{1BC}`$ factor is inserted.

The following table accounts for **every vanished row** of Step 3. Row numbers refer to summands in each previously distributed equation, in their written order. A zero is used only where the relevant factor is not under an unevaluated covariant derivative.

| Step 3 group | Row(s) | Explicit zero after Gold and gauge |
|---|---|---|
| $`Y'L'`$ | 3 | $`\bar\lambda'_{(i}\psi_{j)}=\bar\lambda'_{(i}0=0`$ |
| $`i\bar\lambda'\varphi'`$ | 3, 6, 10 | $`\gamma\!\cdot\!T\psi_i=0`$, $`\gamma\!\cdot\!\widehat F'\psi_i=0`$, $`Y'_{ij}\psi^j=0`$ |
| Same | 8, 9 | $`(\not{\mathcal D}\rho')\psi_i=0`$, $`(\not{\mathcal D}\sigma)\lambda'_i=0`$ |
| $`-\bar\psi\gamma\lambda'L'/2`$ | 3 | $`(\bar\psi\gamma\lambda')\bar\lambda'_{(i}\psi_{j)}=0`$ |
| $`A'E'`$ | 3, 6 | $`(\mathcal D_b\sigma)\widehat F'^{ab}=0`$, $`\rho'(\mathcal D_b\sigma)T^{ab}=0`$ |
| Same | 8 | $`(\mathcal D_b\bar\lambda')\gamma^{ab}\psi=0`$; row 9 with $`\mathcal D_b\psi`$ survives |
| First form-bridge fermion term | 3, 6, 10 | $`\gamma\!\cdot\!T\psi_i=0`$, $`\gamma\!\cdot\!\widehat F'\psi_i=0`$, $`Y'_{ij}\psi^j=0`$ |
| Same | 8, 9 | $`(\not{\mathcal D}\rho')\psi_i=0`$, $`(\not{\mathcal D}\sigma)\lambda'_i=0`$ |
| Second form-bridge fermion term | 3 | $`(\bar\psi\gamma^{abc}\psi)\bar\lambda'_{(i}\psi_{j)}=0`$; the last spinor is the gaugino |
| $`\rho'N'`$ | 3 | $`\mathcal D_a\rho'\mathcal D^a\sigma=0`$ |
| Same | 11, 12, 13 | $`\bar\psi\not{\mathcal D}\lambda'=0`$, $`\bar\lambda'\gamma\!\cdot\!T\psi=0`$, $`\bar\chi\psi=0`$; these $`\psi`$'s have no vector index |
| $`\rho'\bar\psi\gamma\varphi'/2`$ | 3, 6, 10 | $`\gamma\!\cdot\!T\psi_i=0`$, $`\gamma\!\cdot\!\widehat F'\psi_i=0`$, $`Y'_{ij}\psi^j=0`$ |
| Same | 8, 9 | $`(\not{\mathcal D}\rho')\psi_i=0`$, $`(\not{\mathcal D}\sigma)\lambda'_i=0`$ |
| $`i\rho'\bar\psi\gamma\psi L'/4`$ | 3 | $`(\bar\psi\gamma^{ab}\psi)\bar\lambda'_{(i}\psi_{j)}=0`$; the last spinor is the gaugino |

There are $`26`$ vanished rows and $`43`$ surviving rows at this stage. The explicitly quartic products inherited from the $`L'`$ bilinear vanish because they contain the gauge-fixed gaugino. Other quartic contributions remain inside $`\widehat G`$, the primed hatted strength, derivatives, and background composites.

### 4.4 Collect equal terms without any integration by parts

<!-- ASSERT_CONVENTION: natural_units=hbar=c=1, metric_signature=mostly_plus (-++++), procedure_lock=R2-PRIMED-BF-CONSTRUCTION-FRAMEWORK-v1, gauge_slice=R2-GOLD7-GAUGE-v1 -->

```math
\begin{aligned}
Y'_{ij}L^{ij}&=Y'_{ij}\varepsilon^{ik}\varepsilon^{j\ell}L_{k\ell}
=L_{k\ell}\varepsilon^{ki}\varepsilon^{\ell j}Y'_{ij}
=Y'^{ij}L_{ij},\\
-\frac g2\rho'Y'^{ij}L_{ij}-\frac g2\rho'Y'_{ij}L^{ij}
&=-g\rho'Y'^{ij}L_{ij}.
\end{aligned}
\tag{34}
```

Two epsilon reversals give two minus signs, hence a plus in the triplet exchange; the dummy pairs are then relabeled. The $`\mathcal D\psi`$ terms with the external primed gaugino have exactly the same order and coefficient sum:

```math
-\frac{\rho'}2\bar\lambda'{}^i\not{\mathcal D}\psi_i
-\frac{\rho'}4\bar\lambda'{}^i\not{\mathcal D}\psi_i
=-\frac{3\rho'}4\bar\lambda'{}^i\not{\mathcal D}\psi_i.
\tag{35}
```

The scalar box contribution becomes three terms. Its $`\chi`$ term combines with the one in the scalar–gravitino group:

```math
\begin{aligned}
\frac12(\rho')^2\left.\Box_c\sigma\right|_{\rm gf}
&=(\rho')^2 f_a{}^a-\frac i4(\rho')^2\bar\psi_a{}^i\mathcal D^a\psi_i
-(\rho')^2\bar\psi_a{}^i\gamma^a\chi_i,\\
-(\rho')^2\bar\psi_a{}^i\gamma^a\chi_i
-4(\rho')^2\bar\psi_a{}^i\gamma^a\chi_i
&=-5(\rho')^2\bar\psi_a{}^i\gamma^a\chi_i.
\end{aligned}
\tag{36}
```

The ordering $`\bar\chi\lambda'`$ from $`N'`$ remains distinct from $`\bar\lambda'\chi`$; they are not combined. Nor is $`\bar\lambda'\not{\mathcal D}\lambda'`$ integrated by parts. These collections concern literal equal local products only.

### 4.5 Expand all five surviving differentiated-gaugino contractions

<!-- ASSERT_CONVENTION: natural_units=hbar=c=1, metric_signature=mostly_plus (-++++), procedure_lock=R2-PRIMED-BF-CONSTRUCTION-FRAMEWORK-v1, gauge_slice=R2-GOLD7-GAUGE-v1 -->

Use the lower-index derivative derived above. Each line below substitutes its four summands into one of the five remaining contractions. Gamma matrices are multiplied in their original order. Dummy indices in dots are independent of the external $`a,b,c`$.

<!-- BEGIN DERIVATIVE X1 -->

```math
\begin{aligned}-\frac{3\rho'}4\bar\lambda'{}^i\not{\mathcal D}\psi_i
={}&-\frac{3\rho'}{16}\bar\lambda'{}^i\gamma^a\gamma\!\cdot\!\widehat G\psi_{ai}
+\frac{3\rho'}4\bar\lambda'{}^i\gamma^a\gamma\!\cdot\!T\psi_{ai}\\
&-\frac{3g\rho'}8\bar\lambda'{}^i\gamma^aL_{ij}\psi_a{}^j
+\frac{3\rho'}4\bar\lambda'{}^i\gamma^a\phi_{ai}.
\end{aligned}
\tag{37}
```

<!-- END DERIVATIVE X1 -->

<!-- BEGIN DERIVATIVE X2 -->

```math
\begin{aligned}-\frac i4A'_a\bar\lambda'{}^i\gamma^{ab}\mathcal D_b\psi_i
={}&-\frac i{16}A'_a\bar\lambda'{}^i\gamma^{ab}\gamma\!\cdot\!\widehat G\psi_{bi}
+\frac i4A'_a\bar\lambda'{}^i\gamma^{ab}\gamma\!\cdot\!T\psi_{bi}\\
&-\frac{ig}8A'_a\bar\lambda'{}^i\gamma^{ab}L_{ij}\psi_b{}^j
+\frac i4A'_a\bar\lambda'{}^i\gamma^{ab}\phi_{bi}.
\end{aligned}
\tag{38}
```

<!-- END DERIVATIVE X2 -->

<!-- BEGIN DERIVATIVE X3 -->

```math
\begin{aligned}-\frac14A'_a\rho'\bar\psi_b{}^i\gamma^{ba}\not{\mathcal D}\psi_i
={}&-\frac1{16}A'_a\rho'\bar\psi_b{}^i\gamma^{ba}\gamma^c\gamma\!\cdot\!\widehat G\psi_{ci}
+\frac14A'_a\rho'\bar\psi_b{}^i\gamma^{ba}\gamma^c\gamma\!\cdot\!T\psi_{ci}\\
&-\frac g8A'_a\rho'\bar\psi_b{}^i\gamma^{ba}\gamma^cL_{ij}\psi_c{}^j
+\frac14A'_a\rho'\bar\psi_b{}^i\gamma^{ba}\gamma^c\phi_{ci}.
\end{aligned}
\tag{39}
```

<!-- END DERIVATIVE X3 -->

<!-- BEGIN DERIVATIVE X4 -->

```math
\begin{aligned}+\frac i4(\rho')^2\bar\psi_a{}^i\gamma^a\not{\mathcal D}\psi_i
={}&+\frac i{16}(\rho')^2\bar\psi_a{}^i\gamma^a\gamma^b\gamma\!\cdot\!\widehat G\psi_{bi}
-\frac i4(\rho')^2\bar\psi_a{}^i\gamma^a\gamma^b\gamma\!\cdot\!T\psi_{bi}\\
&+\frac{ig}8(\rho')^2\bar\psi_a{}^i\gamma^a\gamma^bL_{ij}\psi_b{}^j
-\frac i4(\rho')^2\bar\psi_a{}^i\gamma^a\gamma^b\phi_{bi}.
\end{aligned}
\tag{40}
```

<!-- END DERIVATIVE X4 -->

<!-- BEGIN DERIVATIVE X5 -->

```math
\begin{aligned}-\frac i4(\rho')^2\bar\psi_a{}^i\mathcal D^a\psi_i
={}&-\frac i{16}(\rho')^2\bar\psi_a{}^i\gamma\!\cdot\!\widehat G\psi^a_i
+\frac i4(\rho')^2\bar\psi_a{}^i\gamma\!\cdot\!T\psi^a_i\\
&-\frac{ig}8(\rho')^2\bar\psi_a{}^iL_{ij}\psi^{aj}
+\frac i4(\rho')^2\bar\psi_a{}^i\phi^a_i.
\end{aligned}
\tag{41}
```

<!-- END DERIVATIVE X5 -->

For example the first line uses $`(-3/4)(1/4)=-3/16`$, $`(-3/4)(-1)=+3/4`$, $`(-3/4)(g/2)=-3g/8`$, $`(-3/4)(-1)=+3/4`$. The other four prefactors multiply the same four derivative coefficients in their written order. All twenty products are displayed, so no differentiated gauge-fixed gaugino remains unspecified in the final expression.

### 4.6 Keep the full primed supercovariant objects on this gauge slice

<!-- ASSERT_CONVENTION: natural_units=hbar=c=1, metric_signature=mostly_plus (-++++), procedure_lock=R2-PRIMED-BF-CONSTRUCTION-FRAMEWORK-v1, gauge_slice=R2-GOLD7-GAUGE-v1 -->

The gauge does not set the primed gaugino or the gravitino to zero. In particular, the retained primed objects have the following explicit definitions; they remain the inputs for the earlier composite map in Step 5:

```math
\begin{aligned}
\widehat F'_{\mu\nu}&=2\partial_{[\mu}A'_{\nu]}-\bar\psi_{[\mu}\gamma_{\nu]}\lambda'
+\frac i2\rho'\bar\psi_{[\mu}\psi_{\nu]},\\
\mathcal D_\mu\rho'&=\partial_\mu\rho'-\frac i2\bar\psi_\mu\lambda',\\
\mathcal D_\mu\lambda'^i&=(\partial_\mu+\tfrac14\omega_\mu{}^{ab}\gamma_{ab})\lambda'^i
-V_\mu{}^{ij}\lambda'_j+\frac14\gamma\!\cdot\!\widehat F'\psi_\mu{}^i
+\frac i2(\not{\mathcal D}\rho')\psi_\mu{}^i\\
&\quad+Y'^{ij}\psi_{\mu j}-\rho'\gamma\!\cdot\!T\psi_\mu{}^i-\rho'\phi_\mu{}^i,\\
\Box_c\rho'&=(\partial^a+\omega_b{}^{ba})\mathcal D_a\rho'
-\frac i2\bar\psi_a\mathcal D^a\lambda'-2\rho'\bar\psi_a\gamma^a\chi\\
&\quad+\frac12\bar\psi_a\gamma^a\gamma\!\cdot\!T\lambda'
+\frac12\bar\phi_a\gamma^a\lambda'+2f_a{}^a\rho'.
\end{aligned}
\tag{42}
```

There is no unprimed vector $`Y`$ in these definitions: the $`Y'`$ slot stays primed. Connections and background composites are shared. No claim is made that $`\Box_c\rho'`$ or $`\mathcal D\lambda'`$ is an ordinary derivative. Expanding those composite arguments into their original linear fields belongs to Step 5.

## 5. Consistency Checks

### 5.1 Source coverage, parity and weights

The nine ungauge-fixed equations in Section 4.3 explicitly apply Gold to every Step 3 row. The nine gauge-restricted equations retain $`2+6+2+7+6+2+10+6+2=43`$ rows and the table accounts for the other $`26`$. The two equal-term collections remove two repeated rows. Expanding the scalar box adds two rows and collecting its $`\chi`$ term removes one, giving $`42`$ rows before expanding the five differentiated-gaugino contractions. Each of those five becomes four rows, giving $`42+5(4-1)=57`$ distributed rows in the final collected representation. This is a bookkeeping count before Fierz/gamma reduction and expansion of hatted/background objects, not an independent-operator count.

Gold's map preserves pre-gauge weights term by term:

```math
\begin{aligned}
w(\sigma)&=1=w(\rho),\qquad w(\psi)=\tfrac32=w(\lambda),\\
w(\sigma^{-1}\bar\psi^i\psi^j)&=-1+\tfrac32+\tfrac32=2,\\
w(g\sigma^{-1}L^{ij})&=0-1+3=2=w(Y),\\
w(\widehat G_{ab})&=2=w(\widehat F_{ab}),\qquad
w(\mathcal D_a\psi)=\tfrac52,\qquad w(\Box_c\sigma)=3.
\end{aligned}
\tag{43}
```

Consequently every mapped ungauge-fixed row inherits weight five from Step 3. The gauge-fixed constant 1 represents the fixed value of a weight-one compensator. Its missing powers must be restored to make a conformal weight comparison. For example $`\sigma Y'^{ij}Y'_{ij}`$ had weight $`1+2+2=5`$ before becoming $`Y'^{ij}Y'_{ij}`$. No inconsistent gauge-fixed weight assignment to $`g`$ is made.

Every action row is Grassmann even. $`\mathcal D_a\psi_i|_{\rm gf}`$ is odd, and its four replacement terms are odd, so the derivative expansion preserves parity. All open $`i,j`$ in $`L_{ij}`$ contract the original upper spinor or triplet indices. Free tangent indices of $`\mathcal D_b\psi_i`$ are supplied by the original derivative and are contracted before insertion into the action. For instance,

```math
A'_a\bar\psi_b{}^i\gamma^{ba}\gamma^c\gamma\!\cdot\!\widehat G\psi_{ci}
=A'_a\bar\psi_b{}^i\gamma^{ba}\gamma^c\gamma^{de}\widehat G_{de}\psi_{ci}.
\tag{44}
```

The gamma order is $`\gamma^{ba}\gamma^c\gamma^{de}`$ on both sides. Each of $`a,b,c,d,e`$ is paired; the NW–SE spinor contraction is unchanged.

### 5.2 Explicit bosonic restriction

For this test only, set the gravitino, primed gaugino, background fermions and original linear fermion to zero. Then $`\mathcal D\psi|_{\rm gf}=0`$ and $`\Box_c\sigma|_{\rm gf}=2f_a{}^a`$, while the bosonic conformal connections are retained. The final density becomes

```math
\begin{aligned}
\left.e^{-1}\mathcal L_{VL}\right|_{\rm Gold,gf,bos}={}&Y'^{ij}Y'_{ij}-g\rho'Y'^{ij}L_{ij}
+\frac12\rho'\Box_c\rho'+(\rho')^2f_a{}^a
-\frac14\rho'F'_{ab}G^{ab}\\
&+4(\rho')^2G_{ab}T^{ab}+4\rho'F'_{ab}T^{ab}
-4(\rho')^2D-\frac{104}{3}(\rho')^2T^2\\
&-\frac12 A'_a(\mathcal D_b\rho')G^{ab}
-\frac12 A'_a\rho'\mathcal D_bG^{ab}
-\frac12 A'_a\mathcal D_bF'^{ab}\\
&+8A'_a(\mathcal D_b\rho')T^{ab}+8A'_a\rho'\mathcal D_bT^{ab}
-\frac18A'_a\varepsilon^{abcde}F'_{bc}G_{de}.
\end{aligned}
\tag{45}
```

This has 15 displayed bosonic rows after the stated collection. Inserting $`\rho=1`$, $`Y_{ij}=-gL_{ij}/2`$, $`F=G`$, $`\mathcal D\rho=0`$ and $`\Box_c\rho=2f_a{}^a`$ into the Step 3 bosonic Eq. (33) gives exactly these rows: the two triplet terms sum to $`-g\rho'Y'L`$ and the box term supplies $`(\rho')^2f_a{}^a`$. The verifier performs this independent restriction and comparison.

For the explicit ungauged test, set $`g=0`$. Both Gold's $`-gL/(2\sigma)`$ triplet entry and the $`+gL\psi_a/2`$ part of the lower derivative disappear in the two routes. Every remaining term is the same ungauged substitution into the parent BF expression. This check holds background slots fixed while testing explicit map coefficients; a full ungauged action limit additionally replaces the common gauged background by its $`g=0`$ composite expressions.

### 5.3 Hatted-strength and connection checks

For example, the mixed strength term explicitly contains the surviving gravitino bilinear:

```math
-\frac14\rho'\widehat F'_{ab}\widehat G^{ab}
=-\frac14\rho'\widehat F'_{ab}G^{ab}
-\frac i8\rho'\widehat F'_{ab}\bar\psi^{[a i}\psi^{b]}{}_i.
\tag{46}
```

The same hatted definition is retained in every dot, $`T`$ contraction, epsilon term and parent derivative. Terms proportional to $`\mathcal D\psi|_{\rm gf}`$ were expanded in Section 4.5, rather than erased. Terms proportional to $`\mathcal D\sigma|_{\rm gf}`$ vanish by their component definition, not by replacing all covariant derivatives with partial derivatives.

### 5.4 Reproducible checks and qualifications

[verify_step4_gold_gauge.py](../../../../src/kernels/verify_step4_gold_gauge.py) compares the gauge restriction of all 69 prior rows with the nine equations parsed from this document; checks every vanished-row reason; tests the lower-index $`SU(2)`$ sign with explicit epsilon matrices; and compares the five derivative expansions and final collected expression with an independently assembled ordered polynomial. It also checks parity, pre-gauge map weights, the bosonic and explicit $`g=0`$ restrictions, and document coverage. The report, generated as `build/step4_gold_gauge_verification.json` in the [component-check runner](../../../../checks/run_component_checks.py)'s temporary directory, records the exact scope and document hash.

The word algebra keeps spinor/gamma order. It is not a commuting-numerical-spinor test. Contractions and dummy indices are displayed and audited in the hand derivation. Full local supersymmetry, reality of the complete corrected density, expansion of the common gauged background, and source-to-Gold action normalization remain separate requirements. No truncation error is assigned because this step makes no perturbative truncation.

## 6. Final Result

The collected gauge-restricted density is displayed below. The five four-term brackets are the fully evaluated derivatives from Section 4.5, with no new shorthand field defined. All entries are evaluated on Gold (7); the hatted strength is the full fermionic expression above. The primed map remains unexpanded.

<!-- BEGIN FINAL GOLD GAUGE -->

```math
\boxed{\begin{aligned}
\left.e^{-1}\mathcal L_{VL}\right|_{\rm Gold,gf}={}&
Y'^{ij}Y'_{ij}-g\rho'Y'^{ij}L_{ij}
-\frac12\bar\lambda'{}^i\not{\mathcal D}\lambda'_i
+i\bar\lambda'{}^i\gamma\!\cdot\!T\lambda'_i\\
&-8i\rho'\bar\lambda'{}^i\chi_i
-\frac i8\bar\lambda'{}^i\gamma\!\cdot\!\widehat G\lambda'_i
+\frac{ig}4\bar\lambda'{}^iL_{ij}\lambda'{}^j\\
&+\frac g4\rho'\bar\psi_a{}^i\gamma^a\lambda'{}^jL_{ij}
-\frac12\bar\psi_a{}^i\gamma^a\lambda'{}^jY'_{ij}\\
&-\frac{3\rho'}4\bar\lambda'{}^i\gamma^a
\left[\frac14\gamma\!\cdot\!\widehat G\psi_{ai}
-\gamma\!\cdot\!T\psi_{ai}+\frac g2L_{ij}\psi_a{}^j-\phi_{ai}\right]\\
&-\frac12A'_a(\mathcal D_b\rho')\widehat G^{ab}
-\frac12A'_a\rho'\mathcal D_b\widehat G^{ab}
-\frac12A'_a\mathcal D_b\widehat F'^{ab}\\
&+8A'_a(\mathcal D_b\rho')T^{ab}+8A'_a\rho'\mathcal D_bT^{ab}
-\frac18A'_a\varepsilon^{abcde}\widehat F'_{bc}\widehat G_{de}\\
&-\frac i4A'_a\bar\lambda'{}^i\gamma^{ab}
\left[\frac14\gamma\!\cdot\!\widehat G\psi_{bi}
-\gamma\!\cdot\!T\psi_{bi}+\frac g2L_{ij}\psi_b{}^j-\phi_{bi}\right]\\
&-\frac14A'_a\rho'\bar\psi_b{}^i\gamma^{ba}\gamma^c
\left[\frac14\gamma\!\cdot\!\widehat G\psi_{ci}
-\gamma\!\cdot\!T\psi_{ci}+\frac g2L_{ij}\psi_c{}^j-\phi_{ci}\right]\\
&-\frac14A'_a\bar\psi_b{}^i\gamma^{ba}\not{\mathcal D}\lambda'_i
+\frac i2A'_a\bar\psi_b{}^i\gamma^{ba}\gamma\!\cdot\!T\lambda'_i
-4iA'_a\rho'\bar\psi_b{}^i\gamma^{ba}\chi_i\\
&-\frac i{16}A'_a\bar\psi_b{}^i\gamma^{ba}\gamma\!\cdot\!\widehat G\lambda'_i
+\frac{ig}8A'_a\bar\psi_b{}^i\gamma^{ba}L_{ij}\lambda'{}^j\\
&-\frac g8A'_a\rho'\bar\psi_b{}^i\gamma^{abc}\psi_c{}^jL_{ij}
+\frac14A'_a\bar\psi_b{}^i\gamma^{abc}\psi_c{}^jY'_{ij}\\
&+\frac12\rho'\Box_c\rho'+(\rho')^2 f_a{}^a
-\frac14\rho'\widehat F'_{ab}\widehat G^{ab}
+4(\rho')^2\widehat G_{ab}T^{ab}+4\rho'\widehat F'_{ab}T^{ab}\\
&-4(\rho')^2D-\frac{104}{3}(\rho')^2T^2+8i\rho'\bar\chi\lambda'
-5(\rho')^2\bar\psi_a{}^i\gamma^a\chi_i\\
&+\frac i4\rho'\bar\psi_a{}^i\gamma^a\not{\mathcal D}\lambda'_i
+\frac12\rho'\bar\psi_a{}^i\gamma^a\gamma\!\cdot\!T\lambda'_i
-\frac1{16}\rho'\bar\psi_a{}^i\gamma^a\gamma\!\cdot\!\widehat G\lambda'_i
+\frac g8\rho'\bar\psi_a{}^i\gamma^aL_{ij}\lambda'{}^j\\
&+\frac i4(\rho')^2\bar\psi_a{}^i\gamma^a\gamma^b
\left[\frac14\gamma\!\cdot\!\widehat G\psi_{bi}
-\gamma\!\cdot\!T\psi_{bi}+\frac g2L_{ij}\psi_b{}^j-\phi_{bi}\right]\\
&-\frac i4(\rho')^2\bar\psi_a{}^i
\left[\frac14\gamma\!\cdot\!\widehat G\psi^a_i
-\gamma\!\cdot\!T\psi^a_i+\frac g2L_{ij}\psi^{aj}-\phi^a_i\right]\\
&-\frac{ig}8(\rho')^2\bar\psi_a{}^i\gamma^{ab}\psi_b{}^jL_{ij}
+\frac i4\rho'\bar\psi_a{}^i\gamma^{ab}\psi_b{}^jY'_{ij}.
\end{aligned}}
\tag{47}
```

<!-- END FINAL GOLD GAUGE -->

Equation (47) has no unprimed vector $`\rho,\lambda,Y,A`$ left, no unevaluated $`\mathcal D\psi`$ of the zero gaugino, and no $`\Box_c\sigma`$. The $`\psi_{ai}`$, $`\psi_a{}^j`$ and $`\psi^{aj}`$ in its brackets are **gravitini**, not the gauge-fixed spinor. Every occurrence of $`\widehat G`$ uses

```math
\widehat G_{ab}\big|_{\rm gf}
=e_a{}^\mu e_b{}^\nu\left(2\partial_{[\mu}C_{\nu]}
+\frac i2\bar\psi_{[\mu}{}^i\psi_{\nu]i}\right).
\tag{48}
```

This is the Step 4 endpoint, lock **R2-GOLD4-UNPRIMED-SUBSTITUTION-v2**, with gauge lock **R2-GOLD7-GAUGE-v1**. Its primed vector is substituted in [Step 5](08_step5_primed_composite_vector_insertion.md). Its primed strength, derivatives and scalar box retain the complete definitions in Section 4.6; the common gauged background is still implicit.

## 7. Convention Dependence and Remaining Uncertainties

- **Completed here:** all unprimed Gold substitutions, Gold (7) gauge restriction, the complete vanished/surviving-row ledger, explicit evaluation of the zero gaugino's derivatives and constant compensator's box, and local collections leading to (47). The earlier gauge-unfixed Step 3 artifact is corrected in parallel; its non-gradient rows are unchanged.
- This stage imposes the Gold gauge without identifying primed and unprimed vectors, setting the gravitino or $`\varphi^i`$ to zero, or eliminating an auxiliary field.
- The main result leaves the original $`L_{ij}`$ as an $`SU(2)`$ triplet. The optional alignment $`L_{ij}=\delta_{ij}L/\sqrt2`$ from Gold (25) can subsequently be applied with its connection split. It is not imposed in (47); no triplet covariant derivative is assumed to vanish. These simplifications follow from Gold (7).
- The equality to the source action is a **gauge-restricted, off-shell equality**, with no boundary term discarded. Restoring the gauge-unfixed expression means using the nine Gold-substituted equations in Section 4.3, not treating the fixed number 1 as an unconstrained field.
- The mixed scalar-gradient phase is corrected before restriction. It drops out on this slice by the explicit two-factor argument in Section 5.5. All other source phases are retained. No full source-reality or all-order supersymmetry proof is implied by the ordered algebra checks. The gauged Coomans background's source-omitted fermion orders are outside the retained action; $`T,\chi,D`$ have not been replaced by bosonic approximations.
- **Primed substitution:** [Step 5](08_step5_primed_composite_vector_insertion.md) substitutes the full linear-to-vector map into the primed occurrences in (47), with the same original unprimed linear input and the gauge restriction applied to full derivative expressions. It gives the potential representative for $`A'_a`$ and its curl. The complete retained-order density is in [Step 6](10_step6_gauged_action_through_two_fermions.md). This Step 4 calculation uses no normalization fit or auxiliary equation and does not compute a vacuum or spectrum.
