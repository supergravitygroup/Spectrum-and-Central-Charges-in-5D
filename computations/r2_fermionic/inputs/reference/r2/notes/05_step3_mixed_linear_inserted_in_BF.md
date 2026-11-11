# Step 3 — Mixed linear multiplet inserted into primed BF

## 1. Problem and Target

Insert all four mixed components from [Step 2, Eqs. (56)–(59)](04_step2_mixed_primed_linear_multiplet.md) into [Step 1, Eq. (25)](03_step1_full_primed_BF_density.md). The result is an intermediate action density in **primed and unprimed vector components**, following Step 3 of [the confirmed framework](00_action_construction_framework.md). No vector component is renamed.

**Assumptions and scope**

- **A1.** Start from the locked Step 1 BF density and locked Step 2 mixed components, off shell and gauge unfixed. No field equation, field redefinition, integration by parts, boundary discard, dualization, or truncation is permitted in this insertion.
- **A2.** Vector label 1 is primed; label 2 is unprimed in either $`B`$ or $`C`$. The output linear multiplet is primed. The coefficients $`C_{112}=C_{121}=1/2`$, $`C_{111}=C_{122}=0`$ have **already** been applied in Step 2. They are not applied again to BF.
- **A3.** Keep both vector maps unexpanded. The original unprimed linear multiplet $`(L_{ij},\varphi_i,E^a,N)`$ remains the common input to those later maps. It is distinct from the mixed primed output being inserted here.
- **A4.** Every $`T_{ab},\chi^i,D`$ slot, explicit or implicit, is the same gauged Coomans–Özkan background. The [framework](00_action_construction_framework.md) anchors its Eqs. (5.2)–(5.8), including its source-omitted fermion orders. Those composites are retained without expansion or replacement by an ungauged expression.
- **A5.** All equalities in the derivation are pointwise equalities conditional on the locked source inputs. Retain all their fermion terms and implicit supercovariant completions. The displayed rows are a distribution of products, not a claim that all rows form an independent basis of nonzero operators.

## 2. Convention Ledger

<!-- ASSERT_CONVENTION: natural_units=hbar=c=1, metric_signature=mostly_plus (-++++), procedure_lock=R2-PRIMED-BF-CONSTRUCTION-FRAMEWORK-v1 -->

The [branch conventions](../../../../derivations/component_conventions.md) and Step 1–2 convention ledgers agree. No conversion is introduced.

| Item | Convention used here |
|---|---|
| Dimension, signature, units | $`d=5`$, $`\eta_{ab}=\mathrm{diag}(-,+,+,+,+)`$, $`\hbar=c=1`$ |
| Indices and frames | $`a,b,\ldots`$ and $`\mu,\nu,\ldots=0,\ldots,4`$; $`i,j=1,2`$; $`e=\det(e_\mu{}^a)`$; tangent indices use $`\eta`$, world indices use $`g_{\mu\nu}`$ |
| $`SU(2)`$ | $`X^i=\varepsilon^{ij}X_j`$, $`X_i=X^j\varepsilon_{ji}`$, $`\varepsilon_{12}=\varepsilon^{12}=1`$; no single-index replacement by $`\delta_{ij}`$ |
| Symmetrization | Unit weight: $`\bar\lambda'_{(i}\lambda_{j)}=(\bar\lambda'_i\lambda_j+\bar\lambda'_j\lambda_i)/2`$; gamma antisymmetrization includes $`1/p!`$ |
| Orientation | Frame $`\varepsilon^{01234}=+1`$, $`\varepsilon_{01234}=-1`$; world $`\varepsilon^{\mu\nu\rho\sigma\tau}=e^{-1}\epsilon^{\mu\nu\rho\sigma\tau}`$ with coordinate symbol $`\epsilon^{01234}=+1`$ |
| Clifford algebra | $`\{\gamma_a,\gamma_b\}=2\eta_{ab}`$, $`\gamma^{abcde}=i\varepsilon^{abcde}\mathbf1`$; gamma dots have no factorial |
| Spinors | Odd symplectic Majorana; operational bar $`(\lambda^i)^TC`$; $`C^T=-C`$, $`(C\gamma_a)^T=-C\gamma_a`$, $`(C\gamma_{ab})^T=C\gamma_{ab}`$ |
| Ordering | Fixed-index flips have $`t_0=t_1=+1`$, $`t_2=t_3=-1`$; a NW–SE-contracted flip adds a minus. No flip, Hermitian conjugation, Fierz identity or chirality projection is performed here |
| Derivatives | Source supercovariant $`\mathcal D`$ is even; $`\not{\mathcal D}=\gamma^a\mathcal D_a`$; $`\Box_c`$ is Özkan (3.21), not an ordinary Laplacian |
| Connections | Dependent $`\omega_\mu{}^{ab},\phi_\mu^i,f_\mu{}^a`$ and gravitino contorsion retained. $`\phi_\mu^i`$ is the S connection, distinct from $`\varphi'_i`$ |
| Curvature | $`R^\rho{}_{\sigma\mu\nu}=2\partial_{[\mu}\Gamma^\rho_{\nu]\sigma}+2\Gamma^\rho_{[\mu\vert\alpha\vert}\Gamma^\alpha_{\nu]\sigma}`$, $`R_{\mu\nu}=R^\rho{}_{\mu\rho\nu}`$; no commutator is used |
| Gauging | Abelian vector strengths in the source convention; gauged Coomans background throughout; no new Yang–Mills term |
| Normalization | Exactly one primed BF pairing with unit overall coefficient. $`\lambda_{R^2}`$ has mass dimension $`-2`$ and multiplies this source-normalized invariant in the [total action](12_total_action_zeroth_first_second_orders.md) |
| Variations and boundaries | No functional derivative, no choice of left/right variation, no integration by parts and no boundary condition used |

The gravitino $`\psi_\mu^i`$ is unprimed in every term. Scalars, potentials, triplets and hatted strengths are even; the spinors and their derivatives are odd. Bilinears are even. Moving an even scalar past a spinor creates no sign. The order inside every spinor string and between the two bilinears of every quartic term is retained.

This calculation makes no approximation. The conformal weights below, rather than gauge-fixed canonical field dimensions, provide the dimensional check. Fourier transforms, state normalization and renormalization do not enter the BF insertion.

## 3. Definitions and Required Identities

### 3.1 The full primed BF starting expression

Write Step 1's seven terms with the contracted spinor indices made explicit:

```math
\begin{aligned}
e^{-1}\mathcal L_{VL}={}&Y'^{ij}L'_{ij}+i\bar\lambda'{}^i\varphi'_i
-\frac12\bar\psi_a{}^i\gamma^a\lambda'{}^jL'_{ij}
-\frac1{12}\varepsilon^{\mu\nu\rho\sigma\tau}A'_\mu\partial_\nu E'_{\rho\sigma\tau}\\
&+\rho'N'+\frac{\rho'}2\bar\psi_a{}^i\gamma^a\varphi'_i
+\frac{i\rho'}4\bar\psi_a{}^i\gamma^{ab}\psi_b{}^jL'_{ij}.
\end{aligned}
\tag{1}
```

The order of the scalar terms has only been arranged for the calculation below. No fermion has been interchanged. The world epsilon in $`e^{-1}\mathcal L`$ is the tensor; multiplication by $`e`$ returns the coordinate-symbol form of the source density.

### 3.2 The four mixed components to insert

The Step 2 results, with their already-applied coefficient weights, are

```math
L'_{ij}=\rho'Y_{ij}+\rho Y'_{ij}-\frac i2\bar\lambda'_{(i}\lambda_{j)}.
\tag{2}
```

```math
\begin{aligned}
\varphi'_i={}&\frac i2\rho'\not{\mathcal D}\lambda_i
+\frac i2\rho\not{\mathcal D}\lambda'_i
+\rho'\gamma\!\cdot\!T\lambda_i+\rho\gamma\!\cdot\!T\lambda'_i-8\rho'\rho\chi_i\\
&-\frac18\gamma\!\cdot\!\widehat F'\lambda_i
-\frac18\gamma\!\cdot\!\widehat F\lambda'_i
+\frac i4(\not{\mathcal D}\rho')\lambda_i+\frac i4(\not{\mathcal D}\rho)\lambda'_i\\
&-\frac12Y'_{ij}\lambda^j-\frac12Y_{ij}\lambda'{}^j.
\end{aligned}
\tag{3}
```

The working coefficient of each scalar-gradient term is $`+i/4`$. The printed $`+1/4`$ is the printed source coefficient, while the fixed Coomans transformation $`\delta L'_{ij}=i\bar\epsilon_{(i}\varphi'_{j)}`$ requires $`ic=-1/4`$, hence $`c=i/4`$, as derived in [the correction note](../../../../derivations/README.md). Only that source-phase correction enters (3); the $`C_{1BC}`$ weights, $`E'`$ and $`N'`$ coefficients are unchanged.

```math
\begin{aligned}
E'^a={}&\mathcal D_b\left[-\frac12(\rho'\widehat F^{ab}+\rho\widehat F'^{ab})
+8\rho'\rho T^{ab}-\frac i4\bar\lambda'\gamma^{ab}\lambda\right]
-\frac18\varepsilon^{abcde}\widehat F'_{bc}\widehat F_{de}.
\end{aligned}
\tag{4}
```

```math
\begin{aligned}
N'={}&\frac12\rho'\Box_c\rho+\frac12\rho\Box_c\rho'
+\frac12\mathcal D_a\rho'\mathcal D^a\rho
-\frac14\widehat F'_{ab}\widehat F^{ab}+Y'_{ij}Y^{ij}\\
&+4\rho'\widehat F_{ab}T^{ab}+4\rho\widehat F'_{ab}T^{ab}
-4\rho'\rho D-\frac{104}{3}\rho'\rho T^2\\
&-\frac14\bar\lambda'\not{\mathcal D}\lambda
-\frac14\bar\lambda\not{\mathcal D}\lambda'
+i\bar\lambda'\gamma\!\cdot\!T\lambda
+8i\rho'\bar\chi\lambda+8i\rho\bar\chi\lambda'.
\end{aligned}
\tag{5}
```

Here $`\gamma\!\cdot\!T=\gamma^{ab}T_{ab}`$, $`\gamma\!\cdot\!\widehat F=\gamma^{ab}\widehat F_{ab}`$ and $`T^2=T_{ab}T^{ab}`$. Unwritten $`SU(2)`$ contractions use the declared NW–SE order. A slash on a scalar acts on that scalar only, before multiplying the following spinor.

For completeness the retained source derivative and strength definitions are exactly [Step 2, Eqs. (7)–(9)](04_step2_mixed_primed_linear_multiplet.md):

```math
\begin{aligned}
\widehat F_{\mu\nu}&=2\partial_{[\mu}A_{\nu]}-\bar\psi_{[\mu}\gamma_{\nu]}\lambda
+\frac i2\rho\bar\psi_{[\mu}\psi_{\nu]},\\
\mathcal D_\mu\rho&=(\partial_\mu-b_\mu)\rho-\frac i2\bar\psi_\mu\lambda,\\
\mathcal D_\mu\lambda^i&=(\partial_\mu-\tfrac32b_\mu)\lambda^i
+\frac14\omega_\mu{}^{ab}\gamma_{ab}\lambda^i-V_\mu{}^{ij}\lambda_j
+\frac14\gamma\!\cdot\!\widehat F\psi_\mu^i\\
&\quad+\frac i2(\not{\mathcal D}\rho)\psi_\mu^i+Y^{ij}\psi_{\mu j}
-\rho\gamma\!\cdot\!T\psi_\mu^i-\rho\phi_\mu^i,\\
\Box_c\rho&=(\partial^a-2b^a+\omega_b{}^{ba})\mathcal D_a\rho
-\frac i2\bar\psi_a\mathcal D^a\lambda-2\rho\bar\psi_a\gamma^a\chi\\
&\quad+\frac12\bar\psi_a\gamma^a\gamma\!\cdot\!T\lambda
+\frac12\bar\phi_a\gamma^a\lambda+2f_a{}^a\rho.
\end{aligned}
\tag{6}
```

For the primed definitions replace only $`(A,\rho,\lambda,Y)`$ in (6) by $`(A',\rho',\lambda',Y')`$. The gravitino, connections and $`T,\chi,D`$ remain the same background. This is a definition of the primed derivative arguments, not either of the later composite-vector maps. Tangent strengths are $`\widehat F_{ab}=e_a{}^\mu e_b{}^\nu\widehat F_{\mu\nu}`$, with the same relation for primes.

### 3.3 The constrained-form identity

The primed version of Özkan (3.12)–(3.13), already derived as Step 2 Eq. (47), is

```math
E'^a+\frac i2\bar\psi_b{}^i\gamma^{ba}\varphi'_i
+\frac14\bar\psi_b{}^i\gamma^{abc}\psi_c{}^jL'_{ij}
=-\frac1{12}e_\mu{}^a\varepsilon^{\mu\nu\rho\sigma\tau}\partial_\nu E'_{\rho\sigma\tau}.
\tag{7}
```

The potential $`E'_{\rho\sigma\tau}`$ belongs to the new primed linear output. It is not the original unprimed linear potential. We need only its curl identity; no local potential formula is guessed.

## 4. Detailed Derivation

### 4.1 Convert the BF curl by the full identity, without integration by parts

<!-- ASSERT_CONVENTION: metric_signature=mostly_plus (-++++), procedure_lock=R2-PRIMED-BF-CONSTRUCTION-FRAMEWORK-v1 -->

Use the inverse frame definition of the existing primed potential:

```math
A'_a=e_a{}^\mu A'_\mu,\qquad
A'_ae_\mu{}^a=e_a{}^\nu e_\mu{}^aA'_\nu
=\delta_\mu{}^\nu A'_\nu=A'_\mu.
\tag{8}
```

Multiply (7) by the even $`A'_a`$ and use (8). The result is the pointwise equality

```math
\begin{aligned}
-\frac1{12}\varepsilon^{\mu\nu\rho\sigma\tau}A'_\mu\partial_\nu E'_{\rho\sigma\tau}
={}&A'_aE'^a+\frac i2 A'_a\bar\psi_b{}^i\gamma^{ba}\varphi'_i
+\frac14 A'_a\bar\psi_b{}^i\gamma^{abc}\psi_c{}^jL'_{ij}.
\end{aligned}
\tag{9}
```

The gamma order in the second term is $`\gamma^{ba}`$, exactly as in (7). There is no replacement by $`\gamma^{ab}`$ and no associated hidden minus sign. No derivative was moved from $`E'_3`$ to $`A'`$.

Inserting (9) in (1) produces the nine groups to be expanded:

```math
\begin{aligned}
e^{-1}\mathcal L_{VL}={}&Y'^{ij}L'_{ij}+i\bar\lambda'{}^i\varphi'_i
-\frac12\bar\psi_a{}^i\gamma^a\lambda'{}^jL'_{ij}\\
&+A'_aE'^a+\frac i2A'_a\bar\psi_b{}^i\gamma^{ba}\varphi'_i
+\frac14A'_a\bar\psi_b{}^i\gamma^{abc}\psi_c{}^jL'_{ij}\\
&+\rho'N'+\frac{\rho'}2\bar\psi_a{}^i\gamma^a\varphi'_i
+\frac{i\rho'}4\bar\psi_a{}^i\gamma^{ab}\psi_b{}^jL'_{ij}.
\end{aligned}
\tag{10}
```

These extra two groups are required even though the original BF density has seven terms.

### 4.2 Insert $`L'_{ij}`$ in $`Y'^{ij}L'_{ij}`$

<!-- ASSERT_CONVENTION: metric_signature=mostly_plus (-++++), procedure_lock=R2-PRIMED-BF-CONSTRUCTION-FRAMEWORK-v1 -->

Substitute (2) and distribute the even $`Y'^{ij}`$ across its three summands:

<!-- BEGIN EXPANSION YL -->
```math
\begin{aligned}
Y'^{ij}L'_{ij}
&=Y'^{ij}\left(\rho'Y_{ij}+\rho Y'_{ij}-\frac i2\bar\lambda'_{(i}\lambda_{j)}\right)\\
&=\rho'Y'^{ij}Y_{ij}+\rho Y'^{ij}Y'_{ij}
-\frac i2Y'^{ij}\bar\lambda'_{(i}\lambda_{j)}.
\end{aligned}
\tag{11}
```
<!-- END EXPANSION YL -->

The first coefficient is $`1\cdot1=1`$, not $`1/2`$. The symmetrization in the last term is retained. If it is written without parentheses, its two contributions are explicitly

```math
-\frac i2Y'^{ij}\bar\lambda'_{(i}\lambda_{j)}
=-\frac i4Y'^{ij}\bar\lambda'_i\lambda_j
-\frac i4Y'^{ij}\bar\lambda'_j\lambda_i.
\tag{12}
```

No spinor interchange was used in this expansion. Each term has weight $`2+3=5`$.

### 4.3 Insert $`\varphi'_i`$ in $`i\bar\lambda'{}^i\varphi'_i`$

<!-- ASSERT_CONVENTION: metric_signature=mostly_plus (-++++), procedure_lock=R2-PRIMED-BF-CONSTRUCTION-FRAMEWORK-v1 -->

Multiply each of the six coefficient types in (3) by the explicit BF factor $`i`$:

```math
i\frac i2=-\frac12,\quad i\cdot1=i,\quad i(-8)=-8i,\quad
i\left(-\frac18\right)=-\frac i8,\quad i\frac i4=\frac{i^2}4=-\frac14,\quad
i\left(-\frac12\right)=-\frac i2.
\tag{13}
```

Left-multiply every spinor term in (3) by $`\bar\lambda'{}^i`$, retaining the gamma and derivative order. The eleven products are

<!-- BEGIN EXPANSION LP -->
```math
\begin{aligned}
i\bar\lambda'{}^i\varphi'_i={}&
-\frac{\rho'}2\bar\lambda'{}^i\not{\mathcal D}\lambda_i
-\frac\rho2\bar\lambda'{}^i\not{\mathcal D}\lambda'_i\\
&+i\rho'\bar\lambda'{}^i\gamma\!\cdot\!T\lambda_i
+i\rho\bar\lambda'{}^i\gamma\!\cdot\!T\lambda'_i
-8i\rho'\rho\bar\lambda'{}^i\chi_i\\
&-\frac i8\bar\lambda'{}^i\gamma\!\cdot\!\widehat F'\lambda_i
-\frac i8\bar\lambda'{}^i\gamma\!\cdot\!\widehat F\lambda'_i\\
&-\frac14\bar\lambda'{}^i(\not{\mathcal D}\rho')\lambda_i
-\frac14\bar\lambda'{}^i(\not{\mathcal D}\rho)\lambda'_i\\
&-\frac i2\bar\lambda'{}^iY'_{ij}\lambda^j
-\frac i2\bar\lambda'{}^iY_{ij}\lambda'{}^j.
\end{aligned}
\tag{14}
```
<!-- END EXPANSION LP -->

Both derivative terms remain. The second scalar-gradient row is retained as a literal distributed product; no rank-one spinor-bilinear reduction is being made. Each row has weight $`3/2+7/2=5`$ and even parity.

### 4.4 Insert $`L'_{ij}`$ in the gravitino–vector-fermion term

<!-- ASSERT_CONVENTION: metric_signature=mostly_plus (-++++), procedure_lock=R2-PRIMED-BF-CONSTRUCTION-FRAMEWORK-v1 -->

The coefficient products are

```math
-\frac12\cdot1=-\frac12,\qquad
\left(-\frac12\right)\left(-\frac i2\right)=+\frac i4.
\tag{15}
```

Distributing (2) gives

<!-- BEGIN EXPANSION PSL -->
```math
\begin{aligned}
-\frac12\bar\psi_a{}^i\gamma^a\lambda'{}^jL'_{ij}={}&
-\frac{\rho'}2\bar\psi_a{}^i\gamma^a\lambda'{}^jY_{ij}
-\frac\rho2\bar\psi_a{}^i\gamma^a\lambda'{}^jY'_{ij}\\
&+\frac i4\left(\bar\psi_a{}^i\gamma^a\lambda'{}^j\right)
\left(\bar\lambda'_{(i}\lambda_{j)}\right).
\end{aligned}
\tag{16}
```
<!-- END EXPANSION PSL -->

The quartic term has the source order $`(\bar\psi\lambda')(\bar\lambda'\lambda)`$. Its plus sign comes only from (15); there is no Grassmann interchange. The weight is $`1/2+3/2+3=5`$.

### 4.5 Insert $`E'^a`$ and display every outer derivative product

<!-- ASSERT_CONVENTION: metric_signature=mostly_plus (-++++), procedure_lock=R2-PRIMED-BF-CONSTRUCTION-FRAMEWORK-v1 -->

First substitute (4) into the first term of (9):

```math
\begin{aligned}
A'_aE'^a={}&A'_a\mathcal D_b\left[-\frac12\rho'\widehat F^{ab}
-\frac12\rho\widehat F'^{ab}+8\rho'\rho T^{ab}
-\frac i4\bar\lambda'\gamma^{ab}\lambda\right]
-\frac18A'_a\varepsilon^{abcde}\widehat F'_{bc}\widehat F_{de}.
\end{aligned}
\tag{17}
```

The even derivative obeys a product rule without an odd-derivative sign. The source covariant gamma matrix is constant under the connection acting on its indices. Thus the four derivative terms expand separately as

```math
\mathcal D_b(\rho'\widehat F^{ab})
=(\mathcal D_b\rho')\widehat F^{ab}+\rho'\mathcal D_b\widehat F^{ab},\qquad
\mathcal D_b(\rho\widehat F'^{ab})
=(\mathcal D_b\rho)\widehat F'^{ab}+\rho\mathcal D_b\widehat F'^{ab}.
\tag{18}
```

```math
\mathcal D_b(\rho'\rho T^{ab})
=(\mathcal D_b\rho')\rho T^{ab}
+\rho'(\mathcal D_b\rho)T^{ab}+\rho'\rho\mathcal D_bT^{ab}.
\tag{19}
```

```math
\mathcal D_b(\bar\lambda'\gamma^{ab}\lambda)
=(\mathcal D_b\bar\lambda')\gamma^{ab}\lambda
+\bar\lambda'\gamma^{ab}\mathcal D_b\lambda.
\tag{20}
```

Substitute (18)–(20) into (17), with no differentiation of the external $`A'_a`$:

<!-- BEGIN EXPANSION AE -->
```math
\begin{aligned}
A'_aE'^a={}&-\frac12A'_a(\mathcal D_b\rho')\widehat F^{ab}
-\frac12A'_a\rho'\mathcal D_b\widehat F^{ab}\\
&-\frac12A'_a(\mathcal D_b\rho)\widehat F'^{ab}
-\frac12A'_a\rho\mathcal D_b\widehat F'^{ab}\\
&+8A'_a(\mathcal D_b\rho')\rho T^{ab}
+8A'_a\rho'(\mathcal D_b\rho)T^{ab}
+8A'_a\rho'\rho\mathcal D_bT^{ab}\\
&-\frac i4A'_a(\mathcal D_b\bar\lambda')\gamma^{ab}\lambda
-\frac i4A'_a\bar\lambda'\gamma^{ab}\mathcal D_b\lambda
-\frac18A'_a\varepsilon^{abcde}\widehat F'_{bc}\widehat F_{de}.
\end{aligned}
\tag{21}
```
<!-- END EXPANSION AE -->

The $`1/8`$ epsilon coefficient is already the mixed result. The repeated indices are exactly $`(a,b)`$ in the derivative terms and $`(a,b,c,d,e)`$ in the last term. The weight is $`w(A'_a)+w(E'^a)=1+4=5`$; both differentiated fermion products keep their original order.

### 4.6 Insert $`\varphi'_i`$ in the first additional form coupling

<!-- ASSERT_CONVENTION: metric_signature=mostly_plus (-++++), procedure_lock=R2-PRIMED-BF-CONSTRUCTION-FRAMEWORK-v1 -->

For the second term in (9), the coefficient products are

```math
\frac i2\frac i2=-\frac14,\quad \frac i2\cdot1=\frac i2,\quad
\frac i2(-8)=-4i,\quad \frac i2\left(-\frac18\right)=-\frac i{16},\quad
\frac i2\frac i4=\frac{i^2}8=-\frac18,\quad \frac i2\left(-\frac12\right)=-\frac i4.
\tag{22}
```

Left multiplication of every term of (3) by $`A'_a\bar\psi_b{}^i\gamma^{ba}`$ yields

<!-- BEGIN EXPANSION APP -->
```math
\begin{aligned}
\frac i2A'_a\bar\psi_b{}^i\gamma^{ba}\varphi'_i={}&
-\frac14A'_a\rho'\bar\psi_b{}^i\gamma^{ba}\not{\mathcal D}\lambda_i
-\frac14A'_a\rho\bar\psi_b{}^i\gamma^{ba}\not{\mathcal D}\lambda'_i\\
&+\frac i2A'_a\rho'\bar\psi_b{}^i\gamma^{ba}\gamma\!\cdot\!T\lambda_i
+\frac i2A'_a\rho\bar\psi_b{}^i\gamma^{ba}\gamma\!\cdot\!T\lambda'_i\\
&-4iA'_a\rho'\rho\bar\psi_b{}^i\gamma^{ba}\chi_i\\
&-\frac i{16}A'_a\bar\psi_b{}^i\gamma^{ba}\gamma\!\cdot\!\widehat F'\lambda_i
-\frac i{16}A'_a\bar\psi_b{}^i\gamma^{ba}\gamma\!\cdot\!\widehat F\lambda'_i\\
&-\frac18A'_a\bar\psi_b{}^i\gamma^{ba}(\not{\mathcal D}\rho')\lambda_i
-\frac18A'_a\bar\psi_b{}^i\gamma^{ba}(\not{\mathcal D}\rho)\lambda'_i\\
&-\frac i4A'_a\bar\psi_b{}^i\gamma^{ba}Y'_{ij}\lambda^j
-\frac i4A'_a\bar\psi_b{}^i\gamma^{ba}Y_{ij}\lambda'{}^j.
\end{aligned}
\tag{23}
```
<!-- END EXPANSION APP -->

Here, for example, $`\gamma^{ba}\not{\mathcal D}\lambda_i=\gamma^{ba}\gamma^c\mathcal D_c\lambda_i`$, with $`c`$ distinct from $`a,b`$. The corresponding dot uses $`\gamma^{ba}\gamma^{cd}T_{cd}`$. No gamma matrices have been commuted. Each row has weight $`1+1/2+7/2=5`$.

### 4.7 Insert $`L'_{ij}`$ in the second additional form coupling

<!-- ASSERT_CONVENTION: metric_signature=mostly_plus (-++++), procedure_lock=R2-PRIMED-BF-CONSTRUCTION-FRAMEWORK-v1 -->

Use $`\tfrac14\cdot1=\tfrac14`$ and $`\tfrac14(-\tfrac i2)=-\tfrac i8`$. Distributing (2) gives

<!-- BEGIN EXPANSION APL -->
```math
\begin{aligned}
\frac14A'_a\bar\psi_b{}^i\gamma^{abc}\psi_c{}^jL'_{ij}={}&
+\frac{\rho'}4A'_a\bar\psi_b{}^i\gamma^{abc}\psi_c{}^jY_{ij}
+\frac\rho4A'_a\bar\psi_b{}^i\gamma^{abc}\psi_c{}^jY'_{ij}\\
&-\frac i8A'_a\left(\bar\psi_b{}^i\gamma^{abc}\psi_c{}^j\right)
\left(\bar\lambda'_{(i}\lambda_{j)}\right).
\end{aligned}
\tag{24}
```
<!-- END EXPANSION APL -->

The quartic sign is negative. Its two bilinears retain their source order. The weight is $`1+1/2+1/2+3=5`$.

### 4.8 Insert $`N'`$ in $`\rho'N'`$

<!-- ASSERT_CONVENTION: metric_signature=mostly_plus (-++++), procedure_lock=R2-PRIMED-BF-CONSTRUCTION-FRAMEWORK-v1 -->

Multiplication by the external $`\rho'`$ is ordinary scalar multiplication. In the $`D,T^2`$ block the numerical operation is

```math
\rho'\left[-4\rho'\rho\left(D+\frac{26}{3}T^2\right)\right]
=-4(\rho')^2\rho D-\frac{104}{3}(\rho')^2\rho T^2.
\tag{25}
```

For the box and fermion terms, the derivative never acts on this external scalar:

```math
\rho'\left(\frac12\rho\Box_c\rho'\right)=\frac12\rho'\rho\Box_c\rho',\qquad
\rho'\left(-\frac14\bar\lambda\not{\mathcal D}\lambda'\right)
=-\frac14\rho'\bar\lambda\not{\mathcal D}\lambda'.
\tag{26}
```

Applying that multiplication to every summand of (5) yields the fourteen rows

<!-- BEGIN EXPANSION RN -->
```math
\begin{aligned}
\rho'N'={}&\frac12(\rho')^2\Box_c\rho+\frac12\rho'\rho\Box_c\rho'
+\frac12\rho'\mathcal D_a\rho'\mathcal D^a\rho\\
&-\frac14\rho'\widehat F'_{ab}\widehat F^{ab}+\rho'Y'_{ij}Y^{ij}
+4(\rho')^2\widehat F_{ab}T^{ab}+4\rho'\rho\widehat F'_{ab}T^{ab}\\
&-4(\rho')^2\rho D-\frac{104}{3}(\rho')^2\rho T^2\\
&-\frac14\rho'\bar\lambda'\not{\mathcal D}\lambda
-\frac14\rho'\bar\lambda\not{\mathcal D}\lambda'
+i\rho'\bar\lambda'\gamma\!\cdot\!T\lambda\\
&+8i(\rho')^2\bar\chi\lambda+8i\rho'\rho\bar\chi\lambda'.
\end{aligned}
\tag{27}
```
<!-- END EXPANSION RN -->

In particular $`\bar\chi\lambda`$ has not been changed to $`\bar\lambda\chi`$. Nor is either derivative bilinear combined with the other by an unrecorded integration by parts. Each row has weight $`1+4=5`$.

### 4.9 Insert $`\varphi'_i`$ in the scalar–gravitino coupling

<!-- ASSERT_CONVENTION: metric_signature=mostly_plus (-++++), procedure_lock=R2-PRIMED-BF-CONSTRUCTION-FRAMEWORK-v1 -->

Factor out the external $`\rho'`$. The remaining coefficient multiplications are

```math
\frac12\frac i2=\frac i4,\quad \frac12\cdot1=\frac12,\quad
\frac12(-8)=-4,\quad \frac12\left(-\frac18\right)=-\frac1{16},\quad
\frac12\frac i4=\frac i8,\quad \frac12\left(-\frac12\right)=-\frac14.
\tag{28}
```

Left multiplication of (3) by $`\rho'\bar\psi_a{}^i\gamma^a/2`$ therefore gives

<!-- BEGIN EXPANSION RPP -->
```math
\begin{aligned}
\frac{\rho'}2\bar\psi_a{}^i\gamma^a\varphi'_i={}&
+\frac i4(\rho')^2\bar\psi_a{}^i\gamma^a\not{\mathcal D}\lambda_i
+\frac i4\rho'\rho\bar\psi_a{}^i\gamma^a\not{\mathcal D}\lambda'_i\\
&+\frac12(\rho')^2\bar\psi_a{}^i\gamma^a\gamma\!\cdot\!T\lambda_i
+\frac12\rho'\rho\bar\psi_a{}^i\gamma^a\gamma\!\cdot\!T\lambda'_i\\
&-4(\rho')^2\rho\bar\psi_a{}^i\gamma^a\chi_i\\
&-\frac1{16}\rho'\bar\psi_a{}^i\gamma^a\gamma\!\cdot\!\widehat F'\lambda_i
-\frac1{16}\rho'\bar\psi_a{}^i\gamma^a\gamma\!\cdot\!\widehat F\lambda'_i\\
&+\frac i8\rho'\bar\psi_a{}^i\gamma^a(\not{\mathcal D}\rho')\lambda_i
+\frac i8\rho'\bar\psi_a{}^i\gamma^a(\not{\mathcal D}\rho)\lambda'_i\\
&-\frac14\rho'\bar\psi_a{}^i\gamma^aY'_{ij}\lambda^j
-\frac14\rho'\bar\psi_a{}^i\gamma^aY_{ij}\lambda'{}^j.
\end{aligned}
\tag{29}
```
<!-- END EXPANSION RPP -->

For instance the $`\chi_i`$ coefficient is $`\rho'/2`$ times $`-8\rho'\rho`$, hence $`-4(\rho')^2\rho`$. Its weight is $`2+1+1/2+3/2=5`$, as is the common group weight $`1+1/2+7/2=5`$.

### 4.10 Insert $`L'_{ij}`$ in the final two-gravitino coupling

<!-- ASSERT_CONVENTION: metric_signature=mostly_plus (-++++), procedure_lock=R2-PRIMED-BF-CONSTRUCTION-FRAMEWORK-v1 -->

The bilinear part of (2) gives a real positive quartic coefficient:

```math
\frac{i\rho'}4\left(-\frac i2\right)
=-\frac{i^2\rho'}8=+\frac{\rho'}8.
\tag{30}
```

Distributing all three terms produces

<!-- BEGIN EXPANSION RPL -->
```math
\begin{aligned}
\frac{i\rho'}4\bar\psi_a{}^i\gamma^{ab}\psi_b{}^jL'_{ij}={}&
+\frac i4(\rho')^2\bar\psi_a{}^i\gamma^{ab}\psi_b{}^jY_{ij}
+\frac i4\rho'\rho\bar\psi_a{}^i\gamma^{ab}\psi_b{}^jY'_{ij}\\
&+\frac{\rho'}8\left(\bar\psi_a{}^i\gamma^{ab}\psi_b{}^j\right)
\left(\bar\lambda'_{(i}\lambda_{j)}\right).
\end{aligned}
\tag{31}
```
<!-- END EXPANSION RPL -->

The weight is $`1+1/2+1/2+3=5`$. Together (11), (14), (16), (21), (23), (24), (27), (29), and (31) exhaust every group of (10).

## 5. Consistency Checks

### 5.1 Exhaustive insertion and weights

There are $`3+11+3+10+11+3+14+11+3=69`$ distributed rows. The count treats each symmetrized bilinear as one structure; it splits the outer derivative and the $`D,T^2`$ terms. It does not count 69 independent nonzero interactions. No Fierz reduction or collection across different BF groups is included in this number.

| BF group | Expanded equation | Distributed rows | Weight of every row |
|---|---|---:|---|
| $`Y'^{ij}L'_{ij}`$ | (11) | 3 | $`2+3=5`$ |
| $`i\bar\lambda'\varphi'`$ | (14) | 11 | $`3/2+7/2=5`$ |
| $`-\bar\psi\gamma\lambda'L'/2`$ | (16) | 3 | $`1/2+3/2+3=5`$ |
| $`A'_aE'^a`$ | (21) | 10 | $`1+4=5`$ |
| $`iA'\bar\psi\gamma\varphi'/2`$ | (23) | 11 | $`1+1/2+7/2=5`$ |
| $`A'\bar\psi\gamma\psi L'/4`$ | (24) | 3 | $`1+1/2+1/2+3=5`$ |
| $`\rho'N'`$ | (27) | 14 | $`1+4=5`$ |
| $`\rho'\bar\psi\gamma\varphi'/2`$ | (29) | 11 | $`1+1/2+7/2=5`$ |
| $`i\rho'\bar\psi\gamma\psi L'/4`$ | (31) | 3 | $`1+1/2+1/2+3=5`$ |

These use $`w(\rho)=1`$, $`w(\lambda)=3/2`$, $`w(Y)=w(\widehat F)=2`$, $`w(T)=1`$, $`w(\chi)=3/2`$, $`w(D)=2`$, $`w(\mathcal D_a)=1`$ and $`w(\psi_a)=1/2`$, with the same weights for primes. Thus $`w(e^{-1}\mathcal L)=5`$ and $`w(e)=-5`$; the coordinate density has weight zero. The verifier checks the sum of factor weights in each of the 69 rows, not only these nine group sums.

### 5.2 Indices, Grassmann order and gamma order

The $`Y'L'`$ contractions have the upper/lower symmetric pair $`ij`$. In all $`\varphi'`$ insertions the lower free $`i`$ contracts the upper $`i`$ of the external bar; $`Y_{ij}\lambda^j`$ leaves precisely that lower $`i`$. Every $`L'`$ insertion with two spinors has the external upper pair $`ij`$ contracted against $`L'_{ij}`$. The epsilon term in (21) contracts $`A'_a`$, the pair $`bc`$ and the pair $`de`$. All other Lorentz indices occur in a slash, a dot, a two-form contraction, or a displayed external gamma string.

Dummy indices inside a slash or a dot must be chosen independently of external indices, for example

```math
A'_a\bar\psi_b{}^i\gamma^{ba}\gamma\!\cdot\!\widehat F'\lambda_i
=A'_a\bar\psi_b{}^i\gamma^{ba}\gamma^{cd}\widehat F'_{cd}\lambda_i,
\qquad
\bar\psi_a{}^i\gamma^a\not{\mathcal D}\lambda_i
=\bar\psi_a{}^i\gamma^a\gamma^b\mathcal D_b\lambda_i.
\tag{32}
```

No gamma transpose or odd-factor interchange occurs in these equalities. Each distributed row is even. The explicitly quartic products from the three $`L'`$ insertions have, respectively, the coefficients $`+i/4`$, $`-iA'_a/8`$, and $`+\rho'/8`$, with the displayed external tensors understood. Equations (15), (24), (30) show the origin of all three signs. Hatted strengths, derivatives and background slots retain their additional implicit fermions.

### 5.3 Bosonic and zero-vector limits

For a check only, set all fermions to zero, including the gravitino and the background fermions; retain bosonic conformal connections. Then the three $`\varphi'`$ groups and the three explicit gravitino-$`L'`$ groups vanish. Remove the bilinear from $`L'`$ and the differentiated bilinear from $`E'`$; remove the last five fermionic rows of $`N'`$. The remaining density is explicitly

```math
\begin{aligned}
e^{-1}\mathcal L_{VL}\big|_{\rm bos}={}&
\rho'Y'^{ij}Y_{ij}+\rho Y'^{ij}Y'_{ij}\\
&+\rho'\left[\frac12\rho'\Box_c\rho+\frac12\rho\Box_c\rho'
+\frac12\mathcal D_a\rho'\mathcal D^a\rho-\frac14F'_{ab}F^{ab}+Y'_{ij}Y^{ij}\right.\\
&\hspace{16mm}\left.+4\rho'F_{ab}T^{ab}+4\rho F'_{ab}T^{ab}
-4\rho'\rho D-\frac{104}{3}\rho'\rho T^2\right]\\
&+A'_a\mathcal D_b\left[-\frac12(\rho'F^{ab}+\rho F'^{ab})+8\rho'\rho T^{ab}\right]
-\frac18A'_a\varepsilon^{abcde}F'_{bc}F_{de}.
\end{aligned}
\tag{33}
```

Here $`F_{\mu\nu}=2\partial_{[\mu}A_{\nu]}`$ and its primed counterpart are the bosonic limits of the already defined strengths. This is exactly the bosonic restriction of (1) after (2)–(5), (9): $`2+9+8=19`$ distributed rows survive. No conformal connection is discarded by the bosonic test.

At fixed common background, each mixed linear component is linear in each vector argument separately. For constant test numbers $`s,t`$, scaling every primed vector slot and its derivatives by $`s`$, and every unprimed slot and its derivatives by $`t`$, gives

```math
(L',\varphi',E',N')\longmapsto st(L',\varphi',E',N'),\qquad
e^{-1}\mathcal L_{VL}\longmapsto s^2t\,e^{-1}\mathcal L_{VL}.
\tag{34}
```

The extra $`s`$ comes from the explicit BF vector, which is primed in every group. For example $`\rho'Y'^{ij}Y_{ij}`$ has degrees $`(2,1)`$, $`A'_a(\mathcal D_b\rho')\rho T^{ab}`$ has degrees $`(2,1)`$, and $`(\rho')^2\rho\bar\psi\gamma\chi`$ has degrees $`(2,1)`$. The script checks those degrees for every row. Setting $`s=0`$ or $`t=0`$ makes every row vanish. This test sets an entire vector and its derivatives to zero, not just its scalar.

The final density is not required to be invariant under exchanging the two vector roles: BF contains the additional primed vector. The mixed linear map has the exchange property established in Step 2; the density has the degree $`s^2t`$ derived here.

### 5.4 Independent algebra check and its scope

[The Step 3 verifier](../../../../src/kernels/verify_step3_bf_insertion.py) independently constructs the ordered products of the seven-term BF input with the compact mixed linear formulas, uses the full form bridge and the even derivative product rule, and compares them with a separately entered list of the 69 distributed rows. It uses exact complex rational coefficients and formal ordered factor strings: spinor and gamma factors are not treated as commuting numerical spinors. Its report, generated as `build/step3_bf_insertion_verification.json` in the [component-check runner](../../../../checks/run_component_checks.py)'s temporary directory, records the checked document hash, group transcription checks, row weights/parities/degrees, the bosonic restriction, and a nontrivial inverse-frame contraction test for (8).

The script cross-checks the displayed multiplication; it does not replace the hand calculation in Section 4. The form identity itself is source-anchored, not derived by the script. Lorentz/$`SU(2)`$ index types and the original source gauge/boundary representative are preserved by (8)–(10) and the explicit contractions above. A full local supersymmetry variation, a full reality proof of the density, and a component expansion of the gauged background are not claimed by this check. No approximation or truncation has been introduced.

## 6. Final Result

The fully inserted density is the sum of the **nine expanded right-hand sides** (11), (14), (16), (21), (23), (24), (27), (29), (31). The following single formula collects exactly that sum, factoring only the external BF prefactors and undoing the outer product rule in (21) for legibility. Every new primed linear component has been replaced; all fields shown are the existing vector components and common background:

<!-- BEGIN FINAL INSERTION -->
```math
\boxed{\begin{aligned}
e^{-1}\mathcal L_{VL}={}&
Y'^{ij}\left(\rho'Y_{ij}+\rho Y'_{ij}-\frac i2\bar\lambda'_{(i}\lambda_{j)}\right)\\
&+i\bar\lambda'{}^i\left[\frac i2\rho'\not{\mathcal D}\lambda_i+\frac i2\rho\not{\mathcal D}\lambda'_i
+\rho'\gamma\!\cdot\!T\lambda_i+\rho\gamma\!\cdot\!T\lambda'_i-8\rho'\rho\chi_i\right.\\
&\hspace{12mm}\left.-\frac18\gamma\!\cdot\!\widehat F'\lambda_i-\frac18\gamma\!\cdot\!\widehat F\lambda'_i
+\frac i4(\not{\mathcal D}\rho')\lambda_i+\frac i4(\not{\mathcal D}\rho)\lambda'_i
-\frac12Y'_{ij}\lambda^j-\frac12Y_{ij}\lambda'{}^j\right]\\
&-\frac12\bar\psi_a{}^i\gamma^a\lambda'{}^j
\left(\rho'Y_{ij}+\rho Y'_{ij}-\frac i2\bar\lambda'_{(i}\lambda_{j)}\right)\\
&+A'_a\mathcal D_b\left[-\frac12(\rho'\widehat F^{ab}+\rho\widehat F'^{ab})+8\rho'\rho T^{ab}
-\frac i4\bar\lambda'\gamma^{ab}\lambda\right]-\frac18A'_a\varepsilon^{abcde}\widehat F'_{bc}\widehat F_{de}\\
&+\frac i2 A'_a\bar\psi_b{}^i\gamma^{ba}
\left[\frac i2\rho'\not{\mathcal D}\lambda_i+\frac i2\rho\not{\mathcal D}\lambda'_i
+\rho'\gamma\!\cdot\!T\lambda_i+\rho\gamma\!\cdot\!T\lambda'_i-8\rho'\rho\chi_i\right.\\
&\hspace{12mm}\left.-\frac18\gamma\!\cdot\!\widehat F'\lambda_i-\frac18\gamma\!\cdot\!\widehat F\lambda'_i
+\frac i4(\not{\mathcal D}\rho')\lambda_i+\frac i4(\not{\mathcal D}\rho)\lambda'_i
-\frac12Y'_{ij}\lambda^j-\frac12Y_{ij}\lambda'{}^j\right]\\
&+\frac14A'_a\bar\psi_b{}^i\gamma^{abc}\psi_c{}^j
\left(\rho'Y_{ij}+\rho Y'_{ij}-\frac i2\bar\lambda'_{(i}\lambda_{j)}\right)\\
&+\rho'\left[\frac12\rho'\Box_c\rho+\frac12\rho\Box_c\rho'
+\frac12\mathcal D_a\rho'\mathcal D^a\rho-\frac14\widehat F'_{ab}\widehat F^{ab}+Y'_{ij}Y^{ij}\right.\\
&\hspace{12mm}+4\rho'\widehat F_{ab}T^{ab}+4\rho\widehat F'_{ab}T^{ab}
-4\rho'\rho D-\frac{104}{3}\rho'\rho T^2\\
&\hspace{12mm}\left.-\frac14\bar\lambda'\not{\mathcal D}\lambda-\frac14\bar\lambda\not{\mathcal D}\lambda'
+i\bar\lambda'\gamma\!\cdot\!T\lambda+8i\rho'\bar\chi\lambda+8i\rho\bar\chi\lambda'\right]\\
&+\frac{\rho'}2\bar\psi_a{}^i\gamma^a
\left[\frac i2\rho'\not{\mathcal D}\lambda_i+\frac i2\rho\not{\mathcal D}\lambda'_i
+\rho'\gamma\!\cdot\!T\lambda_i+\rho\gamma\!\cdot\!T\lambda'_i-8\rho'\rho\chi_i\right.\\
&\hspace{12mm}\left.-\frac18\gamma\!\cdot\!\widehat F'\lambda_i-\frac18\gamma\!\cdot\!\widehat F\lambda'_i
+\frac i4(\not{\mathcal D}\rho')\lambda_i+\frac i4(\not{\mathcal D}\rho)\lambda'_i
-\frac12Y'_{ij}\lambda^j-\frac12Y_{ij}\lambda'{}^j\right]\\
&+\frac{i\rho'}4\bar\psi_a{}^i\gamma^{ab}\psi_b{}^j
\left(\rho'Y_{ij}+\rho Y'_{ij}-\frac i2\bar\lambda'_{(i}\lambda_{j)}\right).
\end{aligned}}
\tag{35}
```
<!-- END FINAL INSERTION -->

Equation (35), with the fully distributed expressions above it, is the Step 3 endpoint, lock **R2-MIXED-BF-INSERTION-v2**. It contains the complete supplied BF and mixed-map terms in the intermediate vector notation. Its cubic vector degree is two primed arguments and one unprimed argument. It is not yet the action written in the original linear and gauged Dilaton-Weyl fields.

## 7. Convention Dependence and Remaining Uncertainties

- **Step 3 is complete as an exact insertion of the locked Steps 1–2 inputs.** The new primed linear fields and their potential curl have all been replaced, using the full fermionic identity (9). No three-form potential representative was invented and no boundary term was discarded.
- The scalar-gradient phase in (3) is the documented project correction $`+i/4`$, and every occurrence in (13), (14), (22), (23), (28), (29), and (35) uses it. All other source coefficients are retained. The ordered-algebra check certifies propagation of that corrected input; it does not establish full source reality or all-order local supersymmetry.
- $`\rho',\lambda',Y',A',\widehat F'`$ retain the earlier composite-vector role; unprimed vector entries retain Gold (4)'s role. Their derivatives have not been identified. The same original unprimed linear input enters both maps in [Step 4](06_step4_Gold_unprimed_vector_and_gauge.md) and [Step 5](08_step5_primed_composite_vector_insertion.md).
- The background slots remain **gauged Coomans composites**, including those in derivatives, strengths and dependent connections. Their explicit expansion through two physical fermions is given in [Step 6](10_step6_gauged_action_through_two_fermions.md); source-omitted higher orders are outside that calculation.
- [Step 4](06_step4_Gold_unprimed_vector_and_gauge.md) applies Gold (4) to every unprimed vector occurrence in (35). [Step 5](08_step5_primed_composite_vector_insertion.md) applies the earlier map to every primed occurrence, including the local $`A'_a`$ potential representative. [Step 6](10_step6_gauged_action_through_two_fermions.md) gives the gauged action through two physical fermions. These linked calculations supply the substitutions and gauge restriction beyond the intermediate density derived here.
