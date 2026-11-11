---
title: From the full BF density to one canonical R² action through two fermions
date: 2026-09-21
status: verified_algebraic_consolidation_through_two_fermions
presentation_lock: R2-BF-CANONICAL-EXPLICIT2-20260921-v2
parent_action_lock: R2-PRIMED-SUPERCOVARIANT-COLLECTED-EXPLICIT2-v2
definition_revision: COOMANS-GAUGED-DEFINITIONS-20260922-v1
---

# From BF to the complete collected R² density through two fermions

**[Go directly to the full canonicalized action, Eq. (R2)](construction.md#6-final-result).** The individual substitutions below are its derivation; the final expression contains the whole action in one integral.

<a id="1-problem-and-target"></a>

## Problem and Target

Starting from the full fermionic vector–linear (BF) density, carry out the mixed vector-to-linear substitution, apply the defining-vector map and the established gauges, insert every primed-vector component, and collect the answer. Section 4 contains the replacements and intermediate products. Section 6 writes the whole action in **one displayed integral**, with every term directly inside its braces and no primed component on its right-hand side. It combines the zero- and two-fermion terms rather than introducing separate bosonic and fermionic fields.

The density below is obtained by insertion of the component maps into the BF action. Gold's Eq. (4) supplies the defining-vector identification and Eqs. (7), (25) specify the already chosen gauge; Gold's final R² action is a comparison reference rather than an input density. The intermediate expression (C.1) keeps the primed maps closed. Equation (R2) inserts them all. Canonicalization means equal-contraction collection with fixed index and Clifford ordering; it is not a kinetic-field diagonalization or a claim of a minimal Fierz basis.

**A1 — order.** Retain physical fermion orders zero and two. The written expressions have at most two *explicit* odd factors. All retained supercovariant objects carry their full inherited completions. Thus the final equation is an equality **through two physical fermions**, and any implicit four-fermion or higher completion in its closed objects lies outside its accuracy. No even composite is replaced by its bosonic part and no odd composite is set to zero. An explicit four-fermion product cannot generate a term of physical order two.

**A2 — formulation.** Work off shell, in five dimensions, with the same original linear multiplet $`(L_{ij},\varphi_i,E_a,N)`$ in both maps. The two vector roles remain distinct until their own definitions have been inserted.

**A3 — gauge and patch.** Use $`\sigma=1`$, $`b_\mu=0`$, the defining dilatino $`\psi^i=0`$, and the already established local alignment $`L_{ij}=\delta_{ij}L/\sqrt2`$, with $`L>0`$. The gravitino $`\psi_\mu{}^i`$, original linear fermion $`\varphi_i`$, and dynamical scalar $`L`$ remain. A covariant derivative of an aligned or fixed field is not set to zero.

**A4 — operations.** Keep the full $`\mathcal D`$ and representation-appropriate $`\Box_c`$. Use linearity, the covariant product rule, index symmetry, the declared Majorana flips, and closed Clifford contractions. No field equation, integration by parts, boundary discard, auxiliary elimination, background condition, or field redefinition is applied. Equalities before truncation are local on the declared gauge patch.

**A5 — closed background.** The common $`T_{ab},\chi^i,D`$, dependent connections, $`E_a`$, and hatted curvatures remain the full gauged Coomans–Özkan composites. Their definitions and the inherited source qualifications are fixed below. The final result is fully explicit in the primed-vector replacements, not an elementary-field expansion of every dependent supergravity object.

The source chain is:

| Input | Exact anchor used here |
|---|---|
| Full BF density | Özkan–Pang 2013, Eq. (3.1), [Supersymmetric Completion of Gauss-Bonnet Combination in Five Dimensions — page 10](https://arxiv.org/abs/1301.6622); [BF density derivation](../../../computations/r2_fermionic/inputs/reference/r2/notes/03_step1_full_primed_BF_density.md) |
| Mixed vector-to-linear map | Özkan 2016, Eq. (3.20), [Off-Shell N=2 Linear Multiplets in Five Dimensions — PDF 10](https://arxiv.org/abs/1608.00349), [Off-Shell N=2 Linear Multiplets in Five Dimensions — PDF 11](https://arxiv.org/abs/1608.00349); [corrected mixed-map derivation](../../../computations/r2_fermionic/inputs/reference/r2/notes/04_step2_mixed_primed_linear_multiplet.md) |
| Full three-form bridge | Özkan 2016, Eqs. (3.12)–(3.13), [Off-Shell N=2 Linear Multiplets in Five Dimensions — PDF 9](https://arxiv.org/abs/1608.00349) |
| Defining-vector map | Gold 2025, Eq. (4), [On five-dimensional curvature squared supergravity and holography — page 5](https://arxiv.org/abs/2504.10856) and [On five-dimensional curvature squared supergravity and holography — page 6](https://arxiv.org/abs/2504.10856) |
| Primed composite | The [locked single-linear map](../../../computations/two_derivative_fermionic/inputs/reference/results/gauged_two_derivative_fermionic_action/02_single_linear_multiplet_mapping_construction.md), §§7.9, 8.7/8.11, 9.7, Eqs. (10.11), (10.15), descended from Özkan Eq. (3.14) |
| Local primed potential | [Primed-composite insertion](../../../computations/r2_fermionic/inputs/reference/r2/notes/08_step5_primed_composite_vector_insertion.md), §4.5; lock `R2-COMPOSITE-POTENTIAL-GOLD25-v1` |
| Gauged background | Coomans–Özkan 2013, Eqs. (5.2)–(5.8), [An off-shell formulation for internally gauged D=5, N=2 supergravity from superconformal methods — page 16](https://arxiv.org/abs/1210.4704), [An off-shell formulation for internally gauged D=5, N=2 supergravity from superconformal methods — page 17](https://arxiv.org/abs/1210.4704) |
| Existing action and reductions | [Defining-vector insertion](../../../computations/r2_fermionic/inputs/reference/r2/notes/06_step4_Gold_unprimed_vector_and_gauge.md), Eq. (47); [Step 5](../../../computations/r2_fermionic/inputs/reference/r2/notes/08_step5_primed_composite_vector_insertion.md); [collected action](../../../computations/r2_fermionic/inputs/reference/r2/notes/11_primed_insertion_supercovariant_two_fermions.md), (SC21)–(SC35) |


<a id="2-convention-ledger"></a>

## Convention Ledger

| Item | Convention |
|---|---|
| Indices | $`a,b,c,d,e,\mu,\nu=0,\ldots,4`$; $`i,j,k,l,m,n=1,2`$; vector labels $`B,C=1,2`$ are different from $`SU(2)`$ indices |
| Metric and curvature | $`\eta=(-++++)`$; $`R^\rho{}_{\sigma\mu\nu}=2\partial_{[\mu}\Gamma^\rho_{\nu]\sigma}+2\Gamma^\rho_{[\mu\vert \lambda\vert }\Gamma^\lambda_{\nu]\sigma}`$, $`R_{\mu\nu}=R^\rho{}_{\mu\rho\nu}`$ |
| Orientation | Tangent $`\varepsilon^{01234}=+1`$, $`\varepsilon_{01234}=-1`$; the BF formula uses its source coordinate epsilon convention with the frame conversion explicitly shown below |
| Symmetry brackets | Unit weight: $`X_{(ij)}=(X_{ij}+X_{ji})/2`$, $`X_{[ab]}=(X_{ab}-X_{ba})/2`$ |
| $`SU(2)`$ | $`X^i=\varepsilon^{ij}X_j`$, $`X_i=X^j\varepsilon_{ji}`$, $`\varepsilon^{12}=\varepsilon_{12}=1`$; no delta replacement for lowering |
| Clifford algebra | $`\{\gamma_a,\gamma_b\}=2\eta_{ab}`$, $`\gamma^{a_1\cdots a_p}=\gamma^{[a_1}\cdots\gamma^{a_p]}`$, $`\gamma^{abcde}=i\varepsilon^{abcde}`$ |
| Dots and slashes | $`\gamma\!\cdot\!T=\gamma^{ab}T_{ab}`$, $`T^2=T_{ab}T^{ab}`$; $`\not E=\gamma^aE_a`$, $`\not{\mathcal D}=\gamma^a\mathcal D_a`$; no hidden factorial |
| Fermions | Grassmann-odd symplectic Majorana; $`\bar\zeta=\zeta^TC`$, $`C^T=-C`$; operational transpose preserves scalar $`i`$ |
| Flips | Fixed-index $`t_0=t_1=+1`$, $`t_2=t_3=-1`$; a contracted NW–SE pair carries the additional epsilon sign |
| Operators | Full source supercovariant derivatives, torsionful dependent spin connection, and $`SU(2)`$, $`S`$, $`K`$ connections; $`\phi_\mu{}^i`$ is the $`S`$ connection, distinct from $`\varphi^i`$ |
| Normalization | Unit BF density; the eventual coupling is $`S_{R^2}=\lambda_{R^2}\int d^5x\,e\,(e^{-1}\mathcal L_{R^2})`$, with $`[\lambda_{R^2}]=-2`$ relative to the two-derivative density |
| Unused choices | No Fourier transform, functional derivative, boundary condition or vacuum is needed for this algebraic calculation |

The inherited source repairs remain explicit: the working mixed-map scalar-gradient coefficient is $`+i/2`$ before $`C_{1BC}`$ weighting, while the printed 2016 coefficient is $`+1/2`$. The gauged endpoint is insensitive to this particular repair because both repaired structures vanish on the defining-vector gauge. The prior 2016 dangling-label repair and project $`R'(M)|_\chi`$ correction are not published errata. These corrections apply on the stated gauge patch; they do not constitute a nonlinear SUSY or reality proof.

<a id="3-definitions-and-required-identities"></a>

## Definitions and Required Identities

<a id="31-multiplet-roles-and-mixed-coefficients"></a>

### Multiplet roles and mixed coefficients

```math
\begin{aligned}
(\rho^1,\lambda_i^1,Y_{ij}^1,A_\mu^1,\widehat F_{ab}^1)
&=(\rho',\lambda'_i,Y'_{ij},A'_\mu,\widehat F'_{ab}),\\
(\rho^2,\lambda_i^2,Y_{ij}^2,A_\mu^2,\widehat F_{ab}^2)
&=(\rho,\lambda_i,Y_{ij},A_\mu,\widehat F_{ab}),\\
(L_{ij,1},\varphi_{i,1},E_1^a,N_1)&=(L'_{ij},\varphi'_i,E'^a,N'),\\
C_{111}=C_{122}&=0,\qquad C_{112}=C_{121}=\frac12.
\end{aligned}
\tag{M.1}
```

The common *input* linear multiplet is unprimed. The *output* linear multiplet carries a prime. For any displayed two-vector structure, the coefficient sum is just its ordered $`(1,2)`$ value with weight $`1/2`$ plus its ordered $`(2,1)`$ value with weight $`1/2`$. This rule is applied once:

```math
\begin{aligned}
\sum_{B,C=1}^2 C_{1BC}X^B Z^C
&=\tfrac12X'Z+\tfrac12XZ',\\
\sum_{B,C} C_{1BC}\,2\rho^B Y^C_{ij}
&=\tfrac12(2\rho'Y_{ij})+\tfrac12(2\rho Y'_{ij})
=\rho'Y_{ij}+\rho Y'_{ij},\\
-\frac i4\bar\lambda'_{(i}\lambda_{j)}-\frac i4\bar\lambda_{(i}\lambda'_{j)}
&=-\frac i4\bar\lambda'_{(i}\lambda_{j)}-\frac i4\bar\lambda'_{(i}\lambda_{j)}
=-\frac i2\bar\lambda'_{(i}\lambda_{j)}.
\end{aligned}
\tag{M.2}
```

The last equality uses the fixed-index scalar Majorana flip and the displayed unit-weight symmetrization; no contracted-index flip is substituted for it. The full source map, with the stated working phase, is:

```math
L_{ij,A}=\sum_{B,C}C_{ABC}
\left(2\rho^B Y_{ij}^C-\frac i2\bar\lambda^B_{(i}\lambda^C_{j)}\right).
\tag{M.3}
```

```math
\begin{aligned}
\varphi_{i,A}=\sum_{B,C}C_{ABC}\bigg(&i\rho^B\not{\mathcal D}\lambda_i^C
+2\rho^B\gamma\!\cdot\!T\lambda_i^C-8\rho^B\rho^C\chi_i\\
&-\frac14\gamma\!\cdot\!\widehat F^B\lambda_i^C
+\frac i2(\not{\mathcal D}\rho^B)\lambda_i^C-Y_{ij}^B\lambda^{jC}\bigg).
\end{aligned}
\tag{M.4}
```

```math
\begin{aligned}
E_A^a=\sum_{B,C}C_{ABC}\bigg[\mathcal D_b\bigg(&-\rho^B\widehat F^{abC}
+8\rho^B\rho^C T^{ab}-\frac i4\bar\lambda^B\gamma^{ab}\lambda^C\bigg)\\
&-\frac18\varepsilon^{abcde}\widehat F_{bc}^B\widehat F_{de}^C\bigg].
\end{aligned}
\tag{M.5}
```

```math
\begin{aligned}
N_A=\sum_{B,C}C_{ABC}\bigg[&\rho^B\Box_c\rho^C
+\frac12\mathcal D_a\rho^B\mathcal D^a\rho^C
-\frac14\widehat F_{ab}^B\widehat F^{abC}+Y_{ij}^B Y^{ijC}\\
&+8\rho^B\widehat F_{ab}^C T^{ab}
-4\rho^B\rho^C\left(D+\frac{26}{3}T^2\right)\\
&-\frac12\bar\lambda^B\not{\mathcal D}\lambda^C
+i\bar\lambda^B\gamma\!\cdot\!T\lambda^C
+16i\rho^B\bar\chi\lambda^C\bigg].
\end{aligned}
\tag{M.6}
```

Applying the two weights to each source term gives the four components used in BF. In $`E'^a`$ the two two-form factors in the epsilon contraction exchange with sign $`(-1)^{2\cdot2}=+1`$; its two $`-1/16`$ contributions therefore make $`-1/8`$. In $`N'`$, $`\bar\lambda'\not{\mathcal D}\lambda`$ and $`\bar\lambda\not{\mathcal D}\lambda'`$ retain their separate orderings. No integration by parts identifies them.

```math
L'_{ij}=\rho'Y_{ij}+\rho Y'_{ij}-\frac i2\bar\lambda'_{(i}\lambda_{j)}.
\tag{B.2}
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
\tag{B.3}
```

```math
\begin{aligned}
E'^a={}&\mathcal D_b\left[-\frac12(\rho'\widehat F^{ab}+\rho\widehat F'^{ab})
+8\rho'\rho T^{ab}-\frac i4\bar\lambda'\gamma^{ab}\lambda\right]
-\frac18\varepsilon^{abcde}\widehat F'_{bc}\widehat F_{de}.
\end{aligned}
\tag{B.4}
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
\tag{B.5}
```

For example, the scalar kinetic and Pauli coefficients follow directly from the same two ordered entries:

```math
\begin{aligned}
\tfrac12\!\left(\tfrac12\mathcal D_a\rho'\mathcal D^a\rho\right)
+\tfrac12\!\left(\tfrac12\mathcal D_a\rho\mathcal D^a\rho'\right)
&=\tfrac12\mathcal D_a\rho'\mathcal D^a\rho,\\
\tfrac12(8\rho'\widehat F_{ab}T^{ab})+\tfrac12(8\rho\widehat F'_{ab}T^{ab})
&=4\rho'\widehat F_{ab}T^{ab}+4\rho\widehat F'_{ab}T^{ab},\\
\tfrac12(16i\rho'\bar\chi\lambda)+\tfrac12(16i\rho\bar\chi\lambda')
&=8i\rho'\bar\chi\lambda+8i\rho\bar\chi\lambda'.
\end{aligned}
\tag{M.7}
```

<a id="32-full-supercovariant-definitions-and-the-form-bridge"></a>

### Full supercovariant definitions and the form bridge

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
\tag{B.6}
```

```math
E'^a+\frac i2\bar\psi_b{}^i\gamma^{ba}\varphi'_i
+\frac14\bar\psi_b{}^i\gamma^{abc}\psi_c{}^jL'_{ij}
=-\frac1{12}e_\mu{}^a\varepsilon^{\mu\nu\rho\sigma\tau}\partial_\nu E'_{\rho\sigma\tau}.
\tag{B.7}
```

The primed definitions replace only $`(A,\rho,\lambda,Y)`$ by $`(A',\rho',\lambda',Y')`$ in (B.6). The background objects are common. In particular $`F'=2\partial A'`$ is an ordinary strength, whereas $`\widehat F'`$ includes the two gravitino terms in (B.6). The hatted epsilon term in the mixed map is retained as written; it is not converted in isolation to an ordinary Chern–Simons term.

<a id="33-meaning-of-the-closed-gauged-objects"></a>

### Meaning of the closed gauged objects

$`e=\det e_\mu{}^a`$; tangent components use the inverse vielbein. $`C_\mu`$ and $`B_{\mu\nu}`$ are the defining vector and two-form. $`E_{\mu\nu\rho}`$ is the original linear-multiplet three-form; the mixed output has its distinct $`E'_{\mu\nu\rho}`$. $`E_a`$ is the full constrained original linear vector. $`V_\mu{}^{ij}`$ is the $`SU(2)`$ connection with $`V_\mu{}^{ij}=V_\mu^{\prime ij}+\delta^{ij}V_\mu/2`$; the trace $`V_\mu`$ is not a new vector multiplet. The dependent $`\omega_\mu{}^{ab},\phi_\mu{}^i,f_\mu{}^a`$ and curvatures $`\widehat R(Q),\widehat R(V)`$ retain the project convention lock.

For clarity, the Coomans defining relations are kept in their source form before the gauge restriction. Their label $`g`$ means the gauged composite, not a second independent field:

```math
\begin{aligned}
Y^{ij}&=\frac{i}{4\sigma}\bar\psi^i\psi^j-\frac{g}{2\sigma}L^{ij},\\
\chi^i&=\frac{i}{8\sigma}\not{\mathcal D}\psi^i
+\frac{i}{16\sigma^2}(\not{\mathcal D}\sigma)\psi^i
-\frac1{32\sigma^2}\gamma\!\cdot\!G\psi^i
+\frac1{4\sigma}\gamma\!\cdot\!T\psi^i
+\frac1{8\sigma^2}Y^{ij}\psi_j+\frac{g}{8\sigma^2}\varphi^i,\\
D&=\frac1{4\sigma}\Box_c\sigma
+\frac1{8\sigma^2}(\mathcal D_a\sigma)(\mathcal D^a\sigma)
-\frac1{16\sigma^2}G_{\mu\nu}G^{\mu\nu}
-\frac1{8\sigma^2}\bar\psi\not{\mathcal D}\psi
+\frac1{4\sigma^2}Y^{ij}Y_{ij}-\frac{4i}{\sigma}\bar\psi\chi\\
&\quad+\frac1{8\sigma^2}\bar\psi_\mu\gamma_\nu\psi\,G^{\mu\nu}
-\frac{i}{16\sigma}\bar\psi_\mu\psi_\nu\,G^{\mu\nu}
+\left(-\frac{26}{3}T_{ab}+\frac2\sigma\widehat G_{ab}
+\frac{i}{4\sigma^2}\bar\psi\gamma_{ab}\psi\right)T^{ab}
+\frac{g}{4\sigma^2}N,\\
-\frac16\varepsilon_{abcde}\widehat H^{edc}
&=8\sigma^2T_{ab}-\sigma\widehat G_{ab}-\frac i4\bar\psi\gamma_{ab}\psi,\\
\widehat H_{\mu\nu\rho}
&=3\partial_{[\mu}B_{\nu\rho]}+\frac32C_{[\mu}G_{\nu\rho]}
+\frac g2E_{\mu\nu\rho}
-\frac34\sigma^2\bar\psi_{[\mu}\gamma_\nu\psi_{\rho]}
-\frac{3i}{2}\sigma\bar\psi_{[\mu}\gamma_{\nu\rho]}\psi.
\end{aligned}
\tag{D.1}
```

Here $`G_{\mu\nu}=2\partial_{[\mu}C_{\nu]}`$ is ordinary, whereas $`\widehat G`$ is the full supercovariant strength. Equation (D.1) is the displayed-order content of Coomans (5.2)–(5.7); the source qualifies the omitted higher orders of $`\chi,D`$. This is sufficient at the specified physical order and is not an assertion that the source gives an all-orders closure. In the action, $`\psi`$ without a spacetime index in these defining relations is set to zero only after evaluating its source derivative. No such restriction is made on $`\psi_\mu`$.

In particular, the source's last explicit $`G`$ bilinear contains two **gravitini**, not two defining dilatini. On $`\sigma=1`$, $`\psi^i=0`$, its combination with the ordinary square is

```math
-\frac1{16}G^2-\frac i{16}G^{ab}\bar\psi_a\psi_b
=-\frac1{16}\widehat G^2+O(\mathrm{fermion}^4),\qquad
\widehat G_{ab}=G_{ab}+\frac i2\bar\psi_{[a}\psi_{b]}.
\tag{D.2}
```

Using the full scalar box from (B.6) before gauge restriction gives the actual common composites used in the component calculation:

```math
\begin{aligned}
\chi^i&=\frac i8\not{\mathcal D}\psi^i+\frac g8\varphi^i+O(\mathrm{fermion}^3),\\
D&=\frac12f_a{}^a-\frac1{16}\widehat G^2-\frac{26}{3}T^2
+2\widehat G^{ab}T_{ab}+\frac g4N+\frac{g^2}{16}L^2\\
&\quad-\frac i8\bar\psi_a{}^i\mathcal D^a\psi_i
-\frac12\bar\psi_a{}^i\gamma^a\chi_i+O(\mathrm{fermion}^4).
\end{aligned}
\tag{D.3}
```

The differentiated $`\psi_i`$ in (D.3) is the defining dilatino, evaluated with the full supercovariant derivative even though its field value vanishes. These are the same expressions already used in note 10 (B14), (B23) and note 12 (4.24), (4.33); the correction does not change their quadratic action coefficients.

<a id="4-detailed-derivation"></a>

## Detailed Derivation

<a id="41-start-from-all-seven-bf-terms"></a>

### Start from all seven BF terms

```math
\begin{aligned}
e^{-1}\mathcal L_{VL}={}&Y'^{ij}L'_{ij}+i\bar\lambda'{}^i\varphi'_i
-\frac12\bar\psi_a{}^i\gamma^a\lambda'{}^jL'_{ij}
-\frac1{12}\varepsilon^{\mu\nu\rho\sigma\tau}A'_\mu\partial_\nu E'_{\rho\sigma\tau}\\
&+\rho'N'+\frac{\rho'}2\bar\psi_a{}^i\gamma^a\varphi'_i
+\frac{i\rho'}4\bar\psi_a{}^i\gamma^{ab}\psi_b{}^jL'_{ij}.
\end{aligned}
\tag{B.1}
```

<a id="42-replace-the-mixed-linear-components-retaining-the-complete-form-bridge"></a>

### Replace the mixed-linear components, retaining the complete form bridge

<a id="421-convert-the-bf-curl-by-the-full-identity-without-integration-by-parts"></a>

#### Convert the BF curl by the full identity, without integration by parts

Use the inverse frame definition of the existing primed potential:

```math
A'_a=e_a{}^\mu A'_\mu,\qquad
A'_ae_\mu{}^a=e_a{}^\nu e_\mu{}^aA'_\nu
=\delta_\mu{}^\nu A'_\nu=A'_\mu.
\tag{B.8}
```

Multiply (B.7) by the even $`A'_a`$ and use (B.8). The result is the pointwise equality

```math
\begin{aligned}
-\frac1{12}\varepsilon^{\mu\nu\rho\sigma\tau}A'_\mu\partial_\nu E'_{\rho\sigma\tau}
={}&A'_aE'^a+\frac i2 A'_a\bar\psi_b{}^i\gamma^{ba}\varphi'_i
+\frac14 A'_a\bar\psi_b{}^i\gamma^{abc}\psi_c{}^jL'_{ij}.
\end{aligned}
\tag{B.9}
```

The gamma order in the second term is $`\gamma^{ba}`$, exactly as in (B.7). There is no replacement by $`\gamma^{ab}`$ and no associated hidden minus sign. No derivative was moved from $`E'_3`$ to $`A'`$.

Inserting (B.9) in (B.1) produces the nine groups to be expanded:

```math
\begin{aligned}
e^{-1}\mathcal L_{VL}={}&Y'^{ij}L'_{ij}+i\bar\lambda'{}^i\varphi'_i
-\frac12\bar\psi_a{}^i\gamma^a\lambda'{}^jL'_{ij}\\
&+A'_aE'^a+\frac i2A'_a\bar\psi_b{}^i\gamma^{ba}\varphi'_i
+\frac14A'_a\bar\psi_b{}^i\gamma^{abc}\psi_c{}^jL'_{ij}\\
&+\rho'N'+\frac{\rho'}2\bar\psi_a{}^i\gamma^a\varphi'_i
+\frac{i\rho'}4\bar\psi_a{}^i\gamma^{ab}\psi_b{}^jL'_{ij}.
\end{aligned}
\tag{B.10}
```

These extra two groups are required even though the original BF density has seven terms.

<a id="422-insert-l_ij-in-yijl_ij"></a>

#### Insert $`L'_{ij}`$ in $`Y'^{ij}L'_{ij}`$

Substitute (B.2) and distribute the even $`Y'^{ij}`$ across its three summands:

```math
\begin{aligned}
Y'^{ij}L'_{ij}
&=Y'^{ij}\left(\rho'Y_{ij}+\rho Y'_{ij}-\frac i2\bar\lambda'_{(i}\lambda_{j)}\right)\\
&=\rho'Y'^{ij}Y_{ij}+\rho Y'^{ij}Y'_{ij}
-\frac i2Y'^{ij}\bar\lambda'_{(i}\lambda_{j)}.
\end{aligned}
\tag{B.11}
```
The first coefficient is $`1\cdot1=1`$, not $`1/2`$. The symmetrization in the last term is retained. If it is written without parentheses, its two contributions are explicitly

```math
-\frac i2Y'^{ij}\bar\lambda'_{(i}\lambda_{j)}
=-\frac i4Y'^{ij}\bar\lambda'_i\lambda_j
-\frac i4Y'^{ij}\bar\lambda'_j\lambda_i.
\tag{B.12}
```

No spinor interchange was used in this expansion. Each term has weight $`2+3=5`$.

<a id="423-insert-varphi_i-in-ibarlambdaivarphi_i"></a>

#### Insert $`\varphi'_i`$ in $`i\bar\lambda'{}^i\varphi'_i`$

Multiply each of the six coefficient types in (B.3) by the explicit BF factor $`i`$:

```math
i\frac i2=-\frac12,\quad i\cdot1=i,\quad i(-8)=-8i,\quad
i\left(-\frac18\right)=-\frac i8,\quad i\frac i4=\frac{i^2}4=-\frac14,\quad
i\left(-\frac12\right)=-\frac i2.
\tag{B.13}
```

Left-multiply every spinor term in (B.3) by $`\bar\lambda'{}^i`$, retaining the gamma and derivative order. The eleven products are

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
\tag{B.14}
```
Both derivative terms remain. The second scalar-gradient row is retained as a literal distributed product; no rank-one spinor-bilinear reduction is being made. Each row has weight $`3/2+7/2=5`$ and even parity.

<a id="424-insert-l_ij-in-the-gravitinovector-fermion-term"></a>

#### Insert $`L'_{ij}`$ in the gravitino–vector-fermion term

The coefficient products are

```math
-\frac12\cdot1=-\frac12,\qquad
\left(-\frac12\right)\left(-\frac i2\right)=+\frac i4.
\tag{B.15}
```

Distributing (B.2) gives

```math
\begin{aligned}
-\frac12\bar\psi_a{}^i\gamma^a\lambda'{}^jL'_{ij}={}&
-\frac{\rho'}2\bar\psi_a{}^i\gamma^a\lambda'{}^jY_{ij}
-\frac\rho2\bar\psi_a{}^i\gamma^a\lambda'{}^jY'_{ij}\\
&+\frac i4\left(\bar\psi_a{}^i\gamma^a\lambda'{}^j\right)
\left(\bar\lambda'_{(i}\lambda_{j)}\right).
\end{aligned}
\tag{B.16}
```
The quartic term has the source order $`(\bar\psi\lambda')(\bar\lambda'\lambda)`$. Its plus sign comes only from (B.15); there is no Grassmann interchange. The weight is $`1/2+3/2+3=5`$.

<a id="425-insert-ea-and-display-every-outer-derivative-product"></a>

#### Insert $`E'^a`$ and display every outer derivative product

First substitute (B.4) into the first term of (B.9):

```math
\begin{aligned}
A'_aE'^a={}&A'_a\mathcal D_b\left[-\frac12\rho'\widehat F^{ab}
-\frac12\rho\widehat F'^{ab}+8\rho'\rho T^{ab}
-\frac i4\bar\lambda'\gamma^{ab}\lambda\right]
-\frac18A'_a\varepsilon^{abcde}\widehat F'_{bc}\widehat F_{de}.
\end{aligned}
\tag{B.17}
```

The even derivative obeys a product rule without an odd-derivative sign. The source covariant gamma matrix is constant under the connection acting on its indices. Thus the four derivative terms expand separately as

```math
\mathcal D_b(\rho'\widehat F^{ab})
=(\mathcal D_b\rho')\widehat F^{ab}+\rho'\mathcal D_b\widehat F^{ab},\qquad
\mathcal D_b(\rho\widehat F'^{ab})
=(\mathcal D_b\rho)\widehat F'^{ab}+\rho\mathcal D_b\widehat F'^{ab}.
\tag{B.18}
```

```math
\mathcal D_b(\rho'\rho T^{ab})
=(\mathcal D_b\rho')\rho T^{ab}
+\rho'(\mathcal D_b\rho)T^{ab}+\rho'\rho\mathcal D_bT^{ab}.
\tag{B.19}
```

```math
\mathcal D_b(\bar\lambda'\gamma^{ab}\lambda)
=(\mathcal D_b\bar\lambda')\gamma^{ab}\lambda
+\bar\lambda'\gamma^{ab}\mathcal D_b\lambda.
\tag{B.20}
```

Substitute (B.18)–(B.20) into (B.17), with no differentiation of the external $`A'_a`$:

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
\tag{B.21}
```
The $`1/8`$ epsilon coefficient is already the mixed result. The repeated indices are exactly $`(a,b)`$ in the derivative terms and $`(a,b,c,d,e)`$ in the last term. The weight is $`w(A'_a)+w(E'^a)=1+4=5`$; both differentiated fermion products keep their original order.

<a id="426-insert-varphi_i-in-the-first-additional-form-coupling"></a>

#### Insert $`\varphi'_i`$ in the first additional form coupling

For the second term in (B.9), the coefficient products are

```math
\frac i2\frac i2=-\frac14,\quad \frac i2\cdot1=\frac i2,\quad
\frac i2(-8)=-4i,\quad \frac i2\left(-\frac18\right)=-\frac i{16},\quad
\frac i2\frac i4=\frac{i^2}8=-\frac18,\quad \frac i2\left(-\frac12\right)=-\frac i4.
\tag{B.22}
```

Left multiplication of every term of (B.3) by $`A'_a\bar\psi_b{}^i\gamma^{ba}`$ yields

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
\tag{B.23}
```
Here, for example, $`\gamma^{ba}\not{\mathcal D}\lambda_i=\gamma^{ba}\gamma^c\mathcal D_c\lambda_i`$, with $`c`$ distinct from $`a,b`$. The corresponding dot uses $`\gamma^{ba}\gamma^{cd}T_{cd}`$. No gamma matrices have been commuted. Each row has weight $`1+1/2+7/2=5`$.

<a id="427-insert-l_ij-in-the-second-additional-form-coupling"></a>

#### Insert $`L'_{ij}`$ in the second additional form coupling

Use $`\tfrac14\cdot1=\tfrac14`$ and $`\tfrac14(-\tfrac i2)=-\tfrac i8`$. Distributing (B.2) gives

```math
\begin{aligned}
\frac14A'_a\bar\psi_b{}^i\gamma^{abc}\psi_c{}^jL'_{ij}={}&
+\frac{\rho'}4A'_a\bar\psi_b{}^i\gamma^{abc}\psi_c{}^jY_{ij}
+\frac\rho4A'_a\bar\psi_b{}^i\gamma^{abc}\psi_c{}^jY'_{ij}\\
&-\frac i8A'_a\left(\bar\psi_b{}^i\gamma^{abc}\psi_c{}^j\right)
\left(\bar\lambda'_{(i}\lambda_{j)}\right).
\end{aligned}
\tag{B.24}
```
The quartic sign is negative. Its two bilinears retain their source order. The weight is $`1+1/2+1/2+3=5`$.

<a id="428-insert-n-in-rhon"></a>

#### Insert $`N'`$ in $`\rho'N'`$

Multiplication by the external $`\rho'`$ is ordinary scalar multiplication. In the $`D,T^2`$ block the numerical operation is

```math
\rho'\left[-4\rho'\rho\left(D+\frac{26}{3}T^2\right)\right]
=-4(\rho')^2\rho D-\frac{104}{3}(\rho')^2\rho T^2.
\tag{B.25}
```

For the box and fermion terms, the derivative never acts on this external scalar:

```math
\rho'\left(\frac12\rho\Box_c\rho'\right)=\frac12\rho'\rho\Box_c\rho',\qquad
\rho'\left(-\frac14\bar\lambda\not{\mathcal D}\lambda'\right)
=-\frac14\rho'\bar\lambda\not{\mathcal D}\lambda'.
\tag{B.26}
```

Applying that multiplication to every summand of (B.5) yields the fourteen rows

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
\tag{B.27}
```
In particular $`\bar\chi\lambda`$ has not been changed to $`\bar\lambda\chi`$. Nor is either derivative bilinear combined with the other by an unrecorded integration by parts. Each row has weight $`1+4=5`$.

<a id="429-insert-varphi_i-in-the-scalargravitino-coupling"></a>

#### Insert $`\varphi'_i`$ in the scalar–gravitino coupling

Factor out the external $`\rho'`$. The remaining coefficient multiplications are

```math
\frac12\frac i2=\frac i4,\quad \frac12\cdot1=\frac12,\quad
\frac12(-8)=-4,\quad \frac12\left(-\frac18\right)=-\frac1{16},\quad
\frac12\frac i4=\frac i8,\quad \frac12\left(-\frac12\right)=-\frac14.
\tag{B.28}
```

Left multiplication of (B.3) by $`\rho'\bar\psi_a{}^i\gamma^a/2`$ therefore gives

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
\tag{B.29}
```
For instance the $`\chi_i`$ coefficient is $`\rho'/2`$ times $`-8\rho'\rho`$, hence $`-4(\rho')^2\rho`$. Its weight is $`2+1+1/2+3/2=5`$, as is the common group weight $`1+1/2+7/2=5`$.

<a id="4210-insert-l_ij-in-the-final-two-gravitino-coupling"></a>

#### Insert $`L'_{ij}`$ in the final two-gravitino coupling

The bilinear part of (B.2) gives a real positive quartic coefficient:

```math
\frac{i\rho'}4\left(-\frac i2\right)
=-\frac{i^2\rho'}8=+\frac{\rho'}8.
\tag{B.30}
```

Distributing all three terms produces

```math
\begin{aligned}
\frac{i\rho'}4\bar\psi_a{}^i\gamma^{ab}\psi_b{}^jL'_{ij}={}&
+\frac i4(\rho')^2\bar\psi_a{}^i\gamma^{ab}\psi_b{}^jY_{ij}
+\frac i4\rho'\rho\bar\psi_a{}^i\gamma^{ab}\psi_b{}^jY'_{ij}\\
&+\frac{\rho'}8\left(\bar\psi_a{}^i\gamma^{ab}\psi_b{}^j\right)
\left(\bar\lambda'_{(i}\lambda_{j)}\right).
\end{aligned}
\tag{B.31}
```
The weight is $`1+1/2+1/2+3=5`$. Together (B.11), (B.14), (B.16), (B.21), (B.23), (B.24), (B.27), (B.29), and (B.31) exhaust every group of (B.10).

The preceding nine products are the complete BF replacement. The three explicit quartic BF products are shown at this intermediate stage to make their origin and coefficients visible; each contains the defining gaugino after Gold's map and vanishes on the gauge slice below. Thus none is silently omitted before its substitution.

In the following reused source derivation, references to “Step 3 Eq. (n)” point to (B.n) above. Source equation labels (G.n) preserve the earlier Step-4 ordering.

<a id="43-replace-the-unprimed-vector-and-impose-the-established-gauge"></a>

### Replace the unprimed vector and impose the established gauge

```math
\begin{aligned}
\rho&\longmapsto\sigma, & A_\mu&\longmapsto C_\mu, & \lambda^i&\longmapsto\psi^i,\\
Y^{ij}&\longmapsto\frac{i}{4\sigma}\bar\psi^i\psi^j-\frac{g}{2\sigma}L^{ij},
&\widehat F_{ab}&\longmapsto\widehat G_{ab}.
\end{aligned}
\tag{G.1}
```

```math
\begin{aligned}
Y_{ij}&=Y^{k\ell}\varepsilon_{ki}\varepsilon_{\ell j}\\
&\longmapsto \frac{i}{4\sigma}(\bar\psi^k\varepsilon_{ki})(\psi^\ell\varepsilon_{\ell j})
-\frac{g}{2\sigma}L^{k\ell}\varepsilon_{ki}\varepsilon_{\ell j}\\
&=\frac{i}{4\sigma}\bar\psi_i\psi_j-\frac{g}{2\sigma}L_{ij}.
\end{aligned}
\tag{G.2}
```

<a id="431-impose-gold-7-on-the-correctly-mapped-components"></a>

#### Impose Gold (7) on the correctly mapped components

```math
\left.\sigma\right|_{\rm gf}=1,\qquad
\left.b_\mu\right|_{\rm gf}=0,\qquad
\left.\psi^i\right|_{\rm gf}=0,\qquad
\left.\rho\right|_{\rm Gold,gf}=1,\qquad
\left.\lambda^i\right|_{\rm Gold,gf}=0.
\tag{G.6}
```

```math
\left.Y_{ij}\right|_{\rm Gold,gf}
=\frac i4\,0\cdot0-\frac g2L_{ij}=-\frac g2L_{ij},\qquad
\left.Y^{ij}\right|_{\rm Gold,gf}=-\frac g2L^{ij}.
\tag{G.7}
```

Apply the gauge to each term of the strength definition. The term with the gaugino vanishes, while the term with two gravitini remains:

```math
\begin{aligned}
\left.\widehat G_{\mu\nu}\right|_{\rm gf}
&=G_{\mu\nu}-\bar\psi_{[\mu}{}^i\gamma_{\nu]}\,0
+\frac i2(1)\bar\psi_{[\mu}{}^i\psi_{\nu]i}\\
&=G_{\mu\nu}+\frac i2\bar\psi_{[\mu}{}^i\psi_{\nu]i}.
\end{aligned}
\tag{G.8}
```

Thus $`\widehat G`$ in the following restricted expressions includes this bilinear. It is not set equal to $`G`$ in a fermionic calculation. From the scalar derivative,

```math
\left.\mathcal D_\mu\sigma\right|_{\rm gf}
=(\partial_\mu-0)1-\frac i2\bar\psi_\mu\,0=0,
\qquad \left.\not{\mathcal D}\sigma\right|_{\rm gf}=0.
\tag{G.9}
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
\tag{G.10}
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
\tag{G.11}
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
\tag{G.12}
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
\tag{G.13}
```

This identifies the needed S compensation; it is not an auxiliary equation or a proof of the full action variation. Dilatations fix the nonzero $`\sigma`$, and special conformal transformations fix $`b_\mu`$. Lorentz, diffeomorphism, Abelian and $`SU(2)`$ gauge freedom have not been removed by (G.7).

<a id="432-restrict-derivative-products-including-those-containing-a-zero-gaugino"></a>

#### Restrict derivative products, including those containing a zero gaugino

```math
\begin{aligned}
\left.\mathcal D_b(\bar\lambda'\gamma^{ab}\psi)\right|_{\rm gf}
&=\left.(\mathcal D_b\bar\lambda')\gamma^{ab}\psi\right|_{\rm gf}
+\left.\bar\lambda'\gamma^{ab}\mathcal D_b\psi\right|_{\rm gf}\\
&=0+\bar\lambda'{}^i\gamma^{ab}
\left(\frac14\gamma\!\cdot\!\widehat G\psi_{bi}
-\gamma\!\cdot\!T\psi_{bi}+\frac g2L_{ij}\psi_b{}^j-\phi_{bi}\right).
\end{aligned}
\tag{G.14}
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
\tag{G.15}
```

All quantities on the right are understood as restricted parent quantities. In particular $`\mathcal D_b\widehat G^{ab}`$ is the restricted supercovariant derivative of the mapped strength, not $`\partial_bG^{ab}`$. Its gauge-fixed field-value definition does not remove its superconformal connection terms.

<a id="433-apply-the-map-and-gauge-to-every-bf-group"></a>

#### Apply the map and gauge to every BF group

Each subsection first shows the full Gold substitution **before** the gauge is imposed, followed by all surviving terms in the gauge. The ordering and external primed BF arguments are exactly those of Step 3. All hatted quantities and derivatives in a gauge-restricted equation are restricted parent quantities. Only the explicit gaugino zeros and the proven $`\mathcal D\sigma=0`$ are used to remove rows.

##### Triplet product — Step 3 Eq. (B.11)

```math
\begin{aligned}\left.Y'^{ij}L'_{ij}\right|_{\rm Gold}={}&\rho'Y'^{ij}\left(\frac{i}{4\sigma}\bar\psi_i\psi_j-\frac{g}{2\sigma}L_{ij}\right)+\sigma Y'^{ij}Y'_{ij}
-\frac i2Y'^{ij}\bar\lambda'_{(i}\psi_{j)}.
\end{aligned}
\tag{G.16}
```

Insert the gauge values into each displayed factor. The surviving Step 3 row numbers are 1, 2. Rows 3 vanish; their zero factors are listed explicitly after these nine substitutions. The surviving density contribution is

```math
\begin{aligned}\left.Y'^{ij}L'_{ij}\right|_{\rm Gold,gf}={}&Y'^{ij}Y'_{ij}-\frac g2\rho'Y'^{ij}L_{ij}.
\end{aligned}
\tag{G.17}
```

##### External primed gaugino — Step 3 Eq. (B.14)

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
\tag{G.18}
```

Insert the gauge values into each displayed factor. The surviving Step 3 row numbers are 1, 2, 4, 5, 7, 11. Rows 3, 6, 8, 9, 10 vanish; their zero factors are listed explicitly after these nine substitutions. The surviving density contribution is

```math
\begin{aligned}\left.i\bar\lambda'{}^i\varphi'_i\right|_{\rm Gold,gf}={}&-\frac{\rho'}2\bar\lambda'{}^i\not{\mathcal D}\psi_i
-\frac12\bar\lambda'{}^i\not{\mathcal D}\lambda'_i
+i\bar\lambda'{}^i\gamma\!\cdot\!T\lambda'_i
-8i\rho'\bar\lambda'{}^i\chi_i\\
&-\frac i8\bar\lambda'{}^i\gamma\!\cdot\!\widehat G\lambda'_i
+\frac{ig}4\bar\lambda'{}^iL_{ij}\lambda'{}^j.
\end{aligned}
\tag{G.19}
```

##### Gravitino–primed-gaugino product — Step 3 Eq. (B.16)

```math
\begin{aligned}\left.-\frac12\bar\psi_a{}^i\gamma^a\lambda'{}^jL'_{ij}\right|_{\rm Gold}={}&
-\frac{\rho'}2\bar\psi_a{}^i\gamma^a\lambda'{}^j\left(\frac{i}{4\sigma}\bar\psi_i\psi_j-\frac{g}{2\sigma}L_{ij}\right)
-\frac\sigma2\bar\psi_a{}^i\gamma^a\lambda'{}^jY'_{ij}\\
&+\frac i4\left(\bar\psi_a{}^i\gamma^a\lambda'{}^j\right)
\left(\bar\lambda'_{(i}\psi_{j)}\right).
\end{aligned}
\tag{G.20}
```

Insert the gauge values into each displayed factor. The surviving Step 3 row numbers are 1, 2. Rows 3 vanish; their zero factors are listed explicitly after these nine substitutions. The surviving density contribution is

```math
\begin{aligned}\left.-\frac12\bar\psi_a{}^i\gamma^a\lambda'{}^jL'_{ij}\right|_{\rm Gold,gf}={}&+\frac g4\rho'\bar\psi_a{}^i\gamma^a\lambda'{}^jL_{ij}
-\frac12\bar\psi_a{}^i\gamma^a\lambda'{}^jY'_{ij}.
\end{aligned}
\tag{G.21}
```

##### Constrained-vector contribution — Step 3 Eq. (B.21)

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
\tag{G.22}
```

Insert the gauge values into each displayed factor. The surviving Step 3 row numbers are 1, 2, 4, 5, 7, 9, 10. Rows 3, 6, 8 vanish; their zero factors are listed explicitly after these nine substitutions. The surviving density contribution is

```math
\begin{aligned}\left.A'_aE'^a\right|_{\rm Gold,gf}={}&-\frac12A'_a(\mathcal D_b\rho')\widehat G^{ab}
-\frac12A'_a\rho'\mathcal D_b\widehat G^{ab}
-\frac12A'_a\mathcal D_b\widehat F'^{ab}\\
&+8A'_a(\mathcal D_b\rho')T^{ab}+8A'_a\rho'\mathcal D_bT^{ab}
-\frac i4A'_a\bar\lambda'{}^i\gamma^{ab}\mathcal D_b\psi_i
-\frac18A'_a\varepsilon^{abcde}\widehat F'_{bc}\widehat G_{de}.
\end{aligned}
\tag{G.23}
```

##### First fermionic form-bridge term — Step 3 Eq. (B.23)

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
\tag{G.24}
```

Insert the gauge values into each displayed factor. The surviving Step 3 row numbers are 1, 2, 4, 5, 7, 11. Rows 3, 6, 8, 9, 10 vanish; their zero factors are listed explicitly after these nine substitutions. The surviving density contribution is

```math
\begin{aligned}\left.\frac i2A'_a\bar\psi_b{}^i\gamma^{ba}\varphi'_i\right|_{\rm Gold,gf}={}&-\frac14A'_a\rho'\bar\psi_b{}^i\gamma^{ba}\not{\mathcal D}\psi_i
-\frac14A'_a\bar\psi_b{}^i\gamma^{ba}\not{\mathcal D}\lambda'_i\\
&+\frac i2A'_a\bar\psi_b{}^i\gamma^{ba}\gamma\!\cdot\!T\lambda'_i
-4iA'_a\rho'\bar\psi_b{}^i\gamma^{ba}\chi_i\\
&-\frac i{16}A'_a\bar\psi_b{}^i\gamma^{ba}\gamma\!\cdot\!\widehat G\lambda'_i
+\frac{ig}8A'_a\bar\psi_b{}^i\gamma^{ba}L_{ij}\lambda'{}^j.
\end{aligned}
\tag{G.25}
```

##### Second fermionic form-bridge term — Step 3 Eq. (B.24)

```math
\begin{aligned}\left.\frac14A'_a\bar\psi_b{}^i\gamma^{abc}\psi_c{}^jL'_{ij}\right|_{\rm Gold}={}&
+\frac{\rho'}4A'_a\bar\psi_b{}^i\gamma^{abc}\psi_c{}^j\left(\frac{i}{4\sigma}\bar\psi_i\psi_j-\frac{g}{2\sigma}L_{ij}\right)
+\frac\sigma4A'_a\bar\psi_b{}^i\gamma^{abc}\psi_c{}^jY'_{ij}\\
&-\frac i8A'_a\left(\bar\psi_b{}^i\gamma^{abc}\psi_c{}^j\right)
\left(\bar\lambda'_{(i}\psi_{j)}\right).
\end{aligned}
\tag{G.26}
```

Insert the gauge values into each displayed factor. The surviving Step 3 row numbers are 1, 2. Rows 3 vanish; their zero factors are listed explicitly after these nine substitutions. The surviving density contribution is

```math
\begin{aligned}\left.\frac14A'_a\bar\psi_b{}^i\gamma^{abc}\psi_c{}^jL'_{ij}\right|_{\rm Gold,gf}={}&-\frac g8A'_a\rho'\bar\psi_b{}^i\gamma^{abc}\psi_c{}^jL_{ij}
+\frac14A'_a\bar\psi_b{}^i\gamma^{abc}\psi_c{}^jY'_{ij}.
\end{aligned}
\tag{G.27}
```

##### Scalar–top-component product — Step 3 Eq. (B.27)

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
\tag{G.28}
```

Insert the gauge values into each displayed factor. The surviving Step 3 row numbers are 1, 2, 4, 5, 6, 7, 8, 9, 10, 14. Rows 3, 11, 12, 13 vanish; their zero factors are listed explicitly after these nine substitutions. The surviving density contribution is

```math
\begin{aligned}\left.\rho'N'\right|_{\rm Gold,gf}={}&+\frac12(\rho')^2\Box_c\sigma+\frac12\rho'\Box_c\rho'
-\frac14\rho'\widehat F'_{ab}\widehat G^{ab}-\frac g2\rho'Y'_{ij}L^{ij}\\
&+4(\rho')^2\widehat G_{ab}T^{ab}+4\rho'\widehat F'_{ab}T^{ab}
-4(\rho')^2D-\frac{104}{3}(\rho')^2T^2\\
&-\frac14\rho'\bar\lambda'{}^i\not{\mathcal D}\psi_i+8i\rho'\bar\chi\lambda' .
\end{aligned}
\tag{G.29}
```

##### Scalar–gravitino–linear-fermion product — Step 3 Eq. (B.29)

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
\tag{G.30}
```

Insert the gauge values into each displayed factor. The surviving Step 3 row numbers are 1, 2, 4, 5, 7, 11. Rows 3, 6, 8, 9, 10 vanish; their zero factors are listed explicitly after these nine substitutions. The surviving density contribution is

```math
\begin{aligned}\left.\frac{\rho'}2\bar\psi_a{}^i\gamma^a\varphi'_i\right|_{\rm Gold,gf}={}&+\frac i4(\rho')^2\bar\psi_a{}^i\gamma^a\not{\mathcal D}\psi_i
+\frac i4\rho'\bar\psi_a{}^i\gamma^a\not{\mathcal D}\lambda'_i\\
&+\frac12\rho'\bar\psi_a{}^i\gamma^a\gamma\!\cdot\!T\lambda'_i
-4(\rho')^2\bar\psi_a{}^i\gamma^a\chi_i\\
&-\frac1{16}\rho'\bar\psi_a{}^i\gamma^a\gamma\!\cdot\!\widehat G\lambda'_i
+\frac g8\rho'\bar\psi_a{}^i\gamma^aL_{ij}\lambda'{}^j.
\end{aligned}
\tag{G.31}
```

##### Final two-gravitino product — Step 3 Eq. (B.31)

```math
\begin{aligned}\left.\frac{i\rho'}4\bar\psi_a{}^i\gamma^{ab}\psi_b{}^jL'_{ij}\right|_{\rm Gold}={}&
+\frac i4(\rho')^2\bar\psi_a{}^i\gamma^{ab}\psi_b{}^j\left(\frac{i}{4\sigma}\bar\psi_i\psi_j-\frac{g}{2\sigma}L_{ij}\right)
+\frac i4\rho'\sigma\bar\psi_a{}^i\gamma^{ab}\psi_b{}^jY'_{ij}\\
&+\frac{\rho'}8\left(\bar\psi_a{}^i\gamma^{ab}\psi_b{}^j\right)
\left(\bar\lambda'_{(i}\psi_{j)}\right).
\end{aligned}
\tag{G.32}
```

Insert the gauge values into each displayed factor. The surviving Step 3 row numbers are 1, 2. Rows 3 vanish; their zero factors are listed explicitly after these nine substitutions. The surviving density contribution is

```math
\begin{aligned}\left.\frac{i\rho'}4\bar\psi_a{}^i\gamma^{ab}\psi_b{}^jL'_{ij}\right|_{\rm Gold,gf}={}&-\frac{ig}8(\rho')^2\bar\psi_a{}^i\gamma^{ab}\psi_b{}^jL_{ij}
+\frac i4\rho'\bar\psi_a{}^i\gamma^{ab}\psi_b{}^jY'_{ij}.
\end{aligned}
\tag{G.33}
```

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

<a id="434-collect-equal-terms-without-any-integration-by-parts"></a>

#### Collect equal terms without any integration by parts

```math
\begin{aligned}
Y'_{ij}L^{ij}&=Y'_{ij}\varepsilon^{ik}\varepsilon^{j\ell}L_{k\ell}
=L_{k\ell}\varepsilon^{ki}\varepsilon^{\ell j}Y'_{ij}
=Y'^{ij}L_{ij},\\
-\frac g2\rho'Y'^{ij}L_{ij}-\frac g2\rho'Y'_{ij}L^{ij}
&=-g\rho'Y'^{ij}L_{ij}.
\end{aligned}
\tag{G.34}
```

Two epsilon reversals give two minus signs, hence a plus in the triplet exchange; the dummy pairs are then relabeled. The $`\mathcal D\psi`$ terms with the external primed gaugino have exactly the same order and coefficient sum:

```math
-\frac{\rho'}2\bar\lambda'{}^i\not{\mathcal D}\psi_i
-\frac{\rho'}4\bar\lambda'{}^i\not{\mathcal D}\psi_i
=-\frac{3\rho'}4\bar\lambda'{}^i\not{\mathcal D}\psi_i.
\tag{G.35}
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
\tag{G.36}
```

At this intermediate stage the ordering $`\bar\chi\lambda'`$ from $`N'`$ is left as supplied. It is combined with $`\bar\lambda'\chi`$ below only after the contracted Majorana flip is displayed. Nor is $`\bar\lambda'\not{\mathcal D}\lambda'`$ integrated by parts. These collections concern literal equal local products only.

<a id="435-expand-all-five-surviving-differentiated-gaugino-contractions"></a>

#### Expand all five surviving differentiated-gaugino contractions

Use the lower-index derivative derived above. Each line below substitutes its four summands into one of the five remaining contractions. Gamma matrices are multiplied in their original order. Dummy indices in dots are independent of the external $`a,b,c`$.

```math
\begin{aligned}-\frac{3\rho'}4\bar\lambda'{}^i\not{\mathcal D}\psi_i
={}&-\frac{3\rho'}{16}\bar\lambda'{}^i\gamma^a\gamma\!\cdot\!\widehat G\psi_{ai}
+\frac{3\rho'}4\bar\lambda'{}^i\gamma^a\gamma\!\cdot\!T\psi_{ai}\\
&-\frac{3g\rho'}8\bar\lambda'{}^i\gamma^aL_{ij}\psi_a{}^j
+\frac{3\rho'}4\bar\lambda'{}^i\gamma^a\phi_{ai}.
\end{aligned}
\tag{G.37}
```

```math
\begin{aligned}-\frac i4A'_a\bar\lambda'{}^i\gamma^{ab}\mathcal D_b\psi_i
={}&-\frac i{16}A'_a\bar\lambda'{}^i\gamma^{ab}\gamma\!\cdot\!\widehat G\psi_{bi}
+\frac i4A'_a\bar\lambda'{}^i\gamma^{ab}\gamma\!\cdot\!T\psi_{bi}\\
&-\frac{ig}8A'_a\bar\lambda'{}^i\gamma^{ab}L_{ij}\psi_b{}^j
+\frac i4A'_a\bar\lambda'{}^i\gamma^{ab}\phi_{bi}.
\end{aligned}
\tag{G.38}
```

```math
\begin{aligned}-\frac14A'_a\rho'\bar\psi_b{}^i\gamma^{ba}\not{\mathcal D}\psi_i
={}&-\frac1{16}A'_a\rho'\bar\psi_b{}^i\gamma^{ba}\gamma^c\gamma\!\cdot\!\widehat G\psi_{ci}
+\frac14A'_a\rho'\bar\psi_b{}^i\gamma^{ba}\gamma^c\gamma\!\cdot\!T\psi_{ci}\\
&-\frac g8A'_a\rho'\bar\psi_b{}^i\gamma^{ba}\gamma^cL_{ij}\psi_c{}^j
+\frac14A'_a\rho'\bar\psi_b{}^i\gamma^{ba}\gamma^c\phi_{ci}.
\end{aligned}
\tag{G.39}
```

```math
\begin{aligned}+\frac i4(\rho')^2\bar\psi_a{}^i\gamma^a\not{\mathcal D}\psi_i
={}&+\frac i{16}(\rho')^2\bar\psi_a{}^i\gamma^a\gamma^b\gamma\!\cdot\!\widehat G\psi_{bi}
-\frac i4(\rho')^2\bar\psi_a{}^i\gamma^a\gamma^b\gamma\!\cdot\!T\psi_{bi}\\
&+\frac{ig}8(\rho')^2\bar\psi_a{}^i\gamma^a\gamma^bL_{ij}\psi_b{}^j
-\frac i4(\rho')^2\bar\psi_a{}^i\gamma^a\gamma^b\phi_{bi}.
\end{aligned}
\tag{G.40}
```

```math
\begin{aligned}-\frac i4(\rho')^2\bar\psi_a{}^i\mathcal D^a\psi_i
={}&-\frac i{16}(\rho')^2\bar\psi_a{}^i\gamma\!\cdot\!\widehat G\psi^a_i
+\frac i4(\rho')^2\bar\psi_a{}^i\gamma\!\cdot\!T\psi^a_i\\
&-\frac{ig}8(\rho')^2\bar\psi_a{}^iL_{ij}\psi^{aj}
+\frac i4(\rho')^2\bar\psi_a{}^i\phi^a_i.
\end{aligned}
\tag{G.41}
```

For example the first line uses $`(-3/4)(1/4)=-3/16`$, $`(-3/4)(-1)=+3/4`$, $`(-3/4)(g/2)=-3g/8`$, $`(-3/4)(-1)=+3/4`$. The other four prefactors multiply the same four derivative coefficients in their written order. All twenty products are displayed, so no differentiated gauge-fixed gaugino remains unspecified in the final expression.

<a id="436-keep-the-full-primed-supercovariant-objects-on-this-gauge-slice"></a>

#### Keep the full primed supercovariant objects on this gauge slice

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
\tag{G.42}
```

There is no unprimed vector $`Y`$ in these definitions: the $`Y'`$ slot stays primed. Connections and background composites are shared. No claim is made that $`\Box_c\rho'`$ or $`\mathcal D\lambda'`$ is an ordinary derivative. Expanding those composite arguments into their original linear fields belongs to Step 5.

<a id="44-collect-the-shared-derivative-and-majorana-terms"></a>

### Collect the shared derivative and Majorana terms

The source-gradient repair does not change this gauge endpoint: $`(\not{\mathcal D}\rho')\lambda_i=0`$ because $`\lambda_i=\psi_i=0`$, and $`(\not{\mathcal D}\rho)\lambda'_i=0`$ because $`\mathcal D\sigma=0`$ from its full scalar definition. This argument does **not** set $`\mathcal D_a\psi_i`$ to zero.

```math
\begin{aligned}
&-\tfrac12A'_a(\mathcal D_b\rho')\widehat G^{ab}
-\tfrac12A'_a\rho'\mathcal D_b\widehat G^{ab}
-\tfrac12A'_a\mathcal D_b\widehat F'^{ab}\\
&\qquad+8A'_a(\mathcal D_b\rho')T^{ab}+8A'_a\rho'\mathcal D_bT^{ab}\\
&=-\tfrac12A'_a\left\{\mathcal D_b\widehat F'^{ab}
+(\mathcal D_b\rho')(\widehat G^{ab}-16T^{ab})
+\rho'\mathcal D_b(\widehat G^{ab}-16T^{ab})\right\}\\
&=-\tfrac12A'_a\mathcal D_b\!\left[\widehat F'^{ab}
+\rho'(\widehat G^{ab}-16T^{ab})\right].
\end{aligned}
\tag{SC32}
```

```math
\begin{aligned}
-\tfrac14\rho'\widehat F'_{ab}\widehat G^{ab}+4\rho'\widehat F'_{ab}T^{ab}
&=-\tfrac14\rho'\widehat F'_{ab}(\widehat G^{ab}-16T^{ab}),\\
\bar\chi^i\lambda'_i
&=\varepsilon^{ij}\bar\chi_j\lambda'_i
=\varepsilon^{ij}\bar\lambda'_i\chi_j=-\bar\lambda'^i\chi_i,\\
-8i\rho'\bar\lambda'^i\chi_i+8i\rho'\bar\chi^i\lambda'_i
&=-16i\rho'\bar\lambda'^i\chi_i,\\
\gamma^a\gamma^b&=\gamma^{ab}+\eta^{ab},\\
\frac{i(\rho')^2}{4}\bar\psi_a^i\gamma^a\gamma^b\mathcal D_b\psi_i
-\frac{i(\rho')^2}{4}\bar\psi_a^i\mathcal D^a\psi_i
&=\frac{i(\rho')^2}{4}\bar\psi_a^i\gamma^{ab}\mathcal D_b\psi_i.
\end{aligned}
\tag{SC34}
```

```math
\mathcal D_a\psi_i
=\left(\tfrac14\gamma\!\cdot\!\widehat G-\gamma\!\cdot\!T\right)\psi_{ai}
+\tfrac g2L_{ij}\psi_a{}^j-\phi_{ai}.
\tag{SC35}
```

The first identity applies the inverse supercovariant product rule on the inherited representations. The scalar bilinear flip in (SC34) follows from the fixed-index flip followed by interchanging the two contracted epsilon indices. The final identity uses $`\gamma^a\gamma^b=\gamma^{ab}+\eta^{ab}`$; its $`\eta^{ab}`$ piece cancels the second term. No gamma matrix is commuted through a retained operator argument.

The entire action with closed primed maps is now the following one equation. It still has the gauge-fixed derivative brackets written out, including the $`S`$ connection:

```math
\boxed{\begin{aligned}
e^{-1}\mathcal L_{R^2}={}&Y'^{ij}Y'_{ij} -g\rho'Y'^{ij}L_{ij} -\frac12\bar\lambda'{}^i\not{\mathcal D}\lambda'_i +i\bar\lambda'{}^i\gamma\!\cdot\!T\lambda'_i\\
&-16i\rho'\bar\lambda'{}^i\chi_i -\frac i8\bar\lambda'{}^i\gamma\!\cdot\!\widehat G\lambda'_i +\frac{ig}4\bar\lambda'{}^iL_{ij}\lambda'{}^j +\frac g4\rho'\bar\psi_a{}^i\gamma^a\lambda'{}^jL_{ij}\\
&-\frac12\bar\psi_a{}^i\gamma^a\lambda'{}^jY'_{ij} -\frac{3\rho'}4\bar\lambda'{}^i\gamma^a [\frac14\gamma\!\cdot\!\widehat G\psi_{ai} -\gamma\!\cdot\!T\psi_{ai}+\frac g2L_{ij}\psi_a{}^j-\phi_{ai}] -\frac12A'_a\mathcal D_b\!\left[\widehat F'^{ab}+\rho'(\widehat G^{ab}-16T^{ab})\right] -\frac18A'_a\varepsilon^{abcde}\widehat F'_{bc}\widehat G_{de}\\
&-\frac i4A'_a\bar\lambda'{}^i\gamma^{ab} [\frac14\gamma\!\cdot\!\widehat G\psi_{bi} -\gamma\!\cdot\!T\psi_{bi}+\frac g2L_{ij}\psi_b{}^j-\phi_{bi}] -\frac14A'_a\rho'\bar\psi_b{}^i\gamma^{ba}\gamma^c [\frac14\gamma\!\cdot\!\widehat G\psi_{ci} -\gamma\!\cdot\!T\psi_{ci}+\frac g2L_{ij}\psi_c{}^j-\phi_{ci}] -\frac14A'_a\bar\psi_b{}^i\gamma^{ba}\not{\mathcal D}\lambda'_i +\frac i2A'_a\bar\psi_b{}^i\gamma^{ba}\gamma\!\cdot\!T\lambda'_i\\
&-4iA'_a\rho'\bar\psi_b{}^i\gamma^{ba}\chi_i -\frac i{16}A'_a\bar\psi_b{}^i\gamma^{ba}\gamma\!\cdot\!\widehat G\lambda'_i +\frac{ig}8A'_a\bar\psi_b{}^i\gamma^{ba}L_{ij}\lambda'{}^j -\frac g8A'_a\rho'\bar\psi_b{}^i\gamma^{abc}\psi_c{}^jL_{ij}\\
&+\frac14A'_a\bar\psi_b{}^i\gamma^{abc}\psi_c{}^jY'_{ij} +\frac12\rho'\Box_c\rho' +(\rho')^2 f_a{}^a -\frac14\rho'\widehat F'_{ab}(\widehat G^{ab}-16T^{ab})\\
&+4(\rho')^2\widehat G_{ab}T^{ab} -4(\rho')^2D -\frac{104}{3}(\rho')^2T^2 -5(\rho')^2\bar\psi_a{}^i\gamma^a\chi_i\\
&+\frac i4\rho'\bar\psi_a{}^i\gamma^a\not{\mathcal D}\lambda'_i +\frac12\rho'\bar\psi_a{}^i\gamma^a\gamma\!\cdot\!T\lambda'_i -\frac1{16}\rho'\bar\psi_a{}^i\gamma^a\gamma\!\cdot\!\widehat G\lambda'_i +\frac g8\rho'\bar\psi_a{}^i\gamma^aL_{ij}\lambda'{}^j\\
&+\frac i4(\rho')^2\bar\psi_a{}^i\gamma^{ab} [\frac14\gamma\!\cdot\!\widehat G\psi_{bi} -\gamma\!\cdot\!T\psi_{bi}+\frac g2L_{ij}\psi_b{}^j-\phi_{bi}] -\frac{ig}8(\rho')^2\bar\psi_a{}^i\gamma^{ab}\psi_b{}^jL_{ij} +\frac i4\rho'\bar\psi_a{}^i\gamma^{ab}\psi_b{}^jY'_{ij}
\end{aligned}}
\tag{C.1}
```

For a further cancellation that will occur automatically in the fully collected endpoint, insert just the $`gL_{ij}\psi_b{}^j/2`$ part of (SC35) into the last Clifford contraction:

```math
\begin{aligned}
\frac{i(\rho')^2}{4}\bar\psi_a^i\gamma^{ab}
\left(\frac g2L_{ij}\psi_b{}^j\right)
-\frac{ig(\rho')^2}{8}\bar\psi_a^i\gamma^{ab}\psi_b{}^jL_{ij}
&=\left(\frac{ig}{8}-\frac{ig}{8}\right)(\rho')^2L_{ij}\bar\psi_a^i\gamma^{ab}\psi_b{}^j=0.
\end{aligned}
\tag{C.2}
```

<a id="45-insert-the-primed-scalar-spinor-triplet-strength-and-potential"></a>

### Insert the primed scalar, spinor, triplet, strength and potential

These are the inherited single-linear-to-vector formulas through the needed order. The scalar is needed through two fermions; the gaugino through one, because every occurrence has an additional odd factor; the triplet through two. Its omitted explicit quartic terms and the gaugino's omitted explicit cubic terms can only contribute four or more to the action. A supercovariant derivative preserves the minimum physical fermion order of these omitted products.

```math
\rho'=\left[\begin{aligned}
&2L^{-1}N\\
&+iL^{-3}L_{ij}\bar\varphi^i\varphi^j
\end{aligned}\right]
\tag{SC1}
```

```math
\lambda'_i=\left[\begin{aligned}
&-2iL^{-1}\not{\mathcal D}\varphi_i\\
&+16L^{-1}L_{ij}\chi^j\\
&+4L^{-1}\gamma\!\cdot\!T\varphi_i\\
&-2NL^{-3}L_{ij}\varphi^j\\
&+2iL^{-3}(\not{\mathcal D}L_{ij})L^{jk}\varphi_k\\
&-2iL^{-3}\not E L_{ij}\varphi^j
\end{aligned}\right]+O_{\rm explicit}(\mathrm{fermion}^3)
\tag{SC2}
```

```math
Y'_{ij}=\left[\begin{aligned}
&L^{-1}\square^c L_{ij}\\
&-L^{-3}L^{km}\mathcal D_aL_{k(i}\mathcal D^aL_{j)m}\\
&-L^{-3}L_{ij}N^2\\
&-L^{-3}L_{ij}E_aE^a\\
&+2L^{-3}E_aL_{k(i}\mathcal D^aL_{j)}{}^k\\
&+\frac83L^{-1}L_{ij}T^2\\
&+4L^{-1}L_{ij}D\\
&+iNL^{-3}\bar\varphi_{(i}\varphi_{j)}\\
&-3iNL^{-5}L_{ij}L^{kl}\bar\varphi_k\varphi_l\\
&+3L^{-5}L_{ij}L^{kl}\bar\varphi_k\not E\varphi_l\\
&-L^{-3}\bar\varphi_{(i}\not E\varphi_{j)}\\
&-16iL^{-1}\bar\chi_{(i}\varphi_{j)}\\
&+16iL^{-3}L_{ij}L_{kl}\bar\chi^k\varphi^l\\
&+2L^{-3}L_{k(i}\bar\varphi^k\not{\mathcal D}\varphi_{j)}\\
&-3L^{-5}L_{k(i}L^{lm}\bar\varphi^k(\not{\mathcal D}L_{j)l})\varphi_m\\
&+\frac12L^{-3}\bar\varphi^l(\not{\mathcal D}L_{l(i})\varphi_{j)}\\
&+\frac12L^{-3}\bar\varphi^m(\not{\mathcal D}L_{ij})\varphi_m\\
&+2iL^{-3}L_{ij}\bar\varphi\gamma\!\cdot\!T\varphi
\end{aligned}\right]+O_{\rm explicit}(\mathrm{fermion}^4)
\tag{SC3}
```

```math
\widehat F'_{\mu\nu}=\left[\begin{aligned}
&4\mathcal D_{[\mu}(L^{-1}E_{\nu]})\\
&+2L^{-1}\widehat R_{\mu\nu}^{ij}(V)L_{ij}\\
&-2L^{-3}L_k{}^l\mathcal D_{[\mu}L^{kp}\mathcal D_{\nu]}L_{lp}\\
&-2\mathcal D_{[\mu}(L^{-3}L_{ij}\bar\varphi^i\gamma_{\nu]}\varphi^j)\\
&-iL^{-1}\bar\varphi^i\widehat R_{\mu\nu i}(Q)
\end{aligned}\right]
\tag{SC4}
```

```math
A'_a=\frac{2}{L}E_a+\sqrt2V_a-\frac{1}{L^3}L_{ij}\bar\varphi^i\gamma_a\varphi^j-\frac{i}{L}\bar\varphi^i\psi_{ai}.
\tag{SC5}
```

```math
\begin{aligned}
\overline{-2iL^{-1}\gamma^a\mathcal D_a\varphi_i}
&=-2iL^{-1}(\mathcal D_a\bar\varphi_i)\gamma^a,\\
\overline{4L^{-1}\gamma^{ab}T_{ab}\varphi_i}
&=-4L^{-1}\bar\varphi_i\gamma^{ab}T_{ab}.
\end{aligned}
\tag{SC6}
```

```math
\bar\lambda'_i=\left[\begin{aligned}
&-2iL^{-1}(\mathcal D_a\bar\varphi_i)\gamma^a\\
&+16L^{-1}L_{ij}\bar\chi^j\\
&-4L^{-1}\bar\varphi_i\gamma\!\cdot\!T\\
&-2NL^{-3}L_{ij}\bar\varphi^j\\
&+2iL^{-3}L^{jk}\bar\varphi_k(\not{\mathcal D}L_{ij})\\
&-2iL^{-3}L_{ij}\bar\varphi^j\not E
\end{aligned}\right]+O_{\rm explicit}(\mathrm{fermion}^3).
\tag{SC7}
```

```math
\bar\lambda'{}^i=\varepsilon^{ir}\bar\lambda'_r,\qquad \lambda'{}^j=\varepsilon^{js}\lambda'_s,\qquad Y'^{ij}=\varepsilon^{ir}\varepsilon^{js}Y'_{rs}.
\tag{SC8}
```

The potential (SC5) is a local aligned representative derived from the hatted strength and its supercovariant-to-ordinary bridge in Step 5. Its two fermionic terms must both be retained. $`A'_a`$ is replaced by (SC5) in every explicit BF occurrence, while $`\widehat F'`$ is replaced by (SC4), not by the curl of only the first two terms of $`A'_a`$.

<a id="46-distribute-the-scalar-and-differentiated-spinor-products"></a>

### Distribute the scalar and differentiated-spinor products

<!-- ASSERT_CONVENTION: metric_signature=mostly_plus (-++++); spinor_bar=NW-SE-transpose; derivative=source-supercovariant; fermion_order=explicit-0-and-2 -->

Multiplication of the two scalar summands gives

```math
\begin{aligned}
(\rho')^2
&=\frac{4N^2}{L^2}+\frac{2iN}{L^4}L_{ij}\bar\varphi^i\varphi^j
+\frac{2iN}{L^4}L_{ij}\bar\varphi^i\varphi^j
-\frac{1}{L^6}(L_{ij}\bar\varphi^i\varphi^j)(L_{kl}\bar\varphi^k\varphi^l)\\
&=\frac{4N^2}{L^2}+\frac{4iN}{L^4}L_{ij}\bar\varphi^i\varphi^j
+O_{\rm explicit}(\mathrm{fermion}^4).
\end{aligned}
\tag{SC9}
```

The two cross terms have equal signs because each scalar bilinear is even. The omitted coefficient is $`i^2=-1`$, with four displayed fermions. Applying only linearity, then distributing the *outer* scalar product, gives

```math
\begin{aligned}
\frac12\rho'\Box_c\rho'
={}&\frac{2N}{L}\Box_c\!\left(\frac NL\right)
+\frac{iN}{L}\Box_c\!\left(L^{-3}L_{ij}\bar\varphi^i\varphi^j\right)\\
&+iL^{-3}L_{ij}\bar\varphi^i\varphi^j\Box_c\!\left(\frac NL\right)
+O_{\rm explicit}(\mathrm{fermion}^4).
\end{aligned}
\tag{SC10}
```

The factor $`\Box_c`$ has not been replaced or expanded. Its action on the entire indicated composite argument is retained. The same treatment of first derivatives gives

```math
\mathcal D_a\rho'=2\mathcal D_a\!\left(\frac NL\right)
+i\mathcal D_a\!\left(L^{-3}L_{ij}\bar\varphi^i\varphi^j\right).
\tag{SC11}
```

```math
\begin{aligned}
\mathcal D_a\lambda'_i={}&-2i\mathcal D_a\!\left(L^{-1}\not{\mathcal D}\varphi_i\right)
+16\mathcal D_a\!\left(L^{-1}L_{ij}\chi^j\right)\\
&+4\mathcal D_a\!\left(L^{-1}\gamma\!\cdot\!T\varphi_i\right)
-2\mathcal D_a\!\left(NL^{-3}L_{ij}\varphi^j\right)\\
&+2i\mathcal D_a\!\left(L^{-3}(\not{\mathcal D}L_{ij})L^{jk}\varphi_k\right)
-2i\mathcal D_a\!\left(L^{-3}\not E L_{ij}\varphi^j\right)
+O_{\rm explicit}(\mathrm{fermion}^3).
\end{aligned}
\tag{SC12}
```

Each derivative retains its argument, including all products and the inner derivative. For instance, multiplying the first term of (SC7) by the derivative of the first term of (SC2) in the kinetic coupling produces

```math
\begin{aligned}
&-\frac12\varepsilon^{ij}
\left[-\frac{2i}{L}(\mathcal D_a\bar\varphi_j)\gamma^a\right]
\gamma^b\left[-2i\mathcal D_b(L^{-1}\not{\mathcal D}\varphi_i)\right]\\
&\qquad=\frac{2}{L}\varepsilon^{ij}(\mathcal D_a\bar\varphi_j)
\gamma^a\gamma^b\mathcal D_b\!\left(L^{-1}\not{\mathcal D}\varphi_i\right).
\end{aligned}
\tag{SC13}
```

Here $`(-1/2)(-2i)(-2i)=2`$. No spinors interchange and the gamma order is unchanged. The literal kinetic product has $`6\times6=36`$ pairings. After the $`N+i\not E`$ collection below it has $`5\times5=25`$ displayed products; all are written in group 3 in Section 4.8.

The unit-weight parentheses in (SC3) and brackets in (SC4) are expanded before their products. For example,

```math
\begin{aligned}
-L^{-3}L^{km}\mathcal D_aL_{k(i}\mathcal D^aL_{j)m}
={}&-\frac{L^{km}}{2L^3}(\mathcal D_aL_{ki})(\mathcal D^aL_{jm})
-\frac{L^{km}}{2L^3}(\mathcal D_aL_{kj})(\mathcal D^aL_{im}),\\
4\mathcal D_{[a}(L^{-1}E_{b]})
={}&2\mathcal D_a(L^{-1}E_b)-2\mathcal D_b(L^{-1}E_a).
\end{aligned}
\tag{SC14}
```

This distributes the index symmetrizations, not the operator's connection terms or argument products. Undifferentiated triplet contractions use

```math
L_{ij}L^{jk}=\frac{L^2}{2}\delta_i{}^k,\qquad
L_{ij}L^{ij}=L^2,\qquad L_i{}^i=0.
\tag{SC15}
```

To verify the norm factors, write a general symmetric two-by-two matrix only for this algebra check:

```math
\begin{aligned}
L_{ij}&=\begin{pmatrix}p&q\\q&r\end{pmatrix},&
L^{ij}&=\begin{pmatrix}r&-q\\-q&p\end{pmatrix},\\
L_{ij}L^{jk}&=(pr-q^2)\delta_i{}^k,&
L^2&=2(pr-q^2).
\end{aligned}
\tag{SC16}
```

The matrix entries in (SC16) are not fields in the action. Equations (SC15)–(SC16) do not act through a differential operator. As an example of the resulting coefficient simplification,

```math
\left(-\frac{N^2}{L^3}L^{ij}\right)
\left(-\frac{N^2}{L^3}L_{ij}\right)
=\frac{N^4}{L^6}L^2=\frac{N^4}{L^4}.
\tag{SC17}
```

Dummy indices are renamed without moving odd factors. Transferring a contracted Lorentz index between two factors has sign $`+1`$; transferring an $`SU(2)`$ index obeys $`X^iY_i=-X_iY^i`$ in the locked NW–SE convention. Epsilon raising/lowering is applied before equivalent scalar contractions are collected. Closed gamma contractions use

```math
\begin{aligned}
\gamma^a\gamma_a&=5,&
\gamma^a\gamma_{ab}&=4\gamma_b,&
\gamma_{ab}\gamma^a&=-4\gamma_b,\\
\gamma^a\gamma^{b_1\ldots b_p}\gamma_a
&=(-1)^p(5-2p)\gamma^{b_1\ldots b_p},\\
\gamma^{a_1\ldots a_p}\gamma_{a_1\ldots a_p}
&=(-1)^{p(p-1)/2}\frac{5!}{(5-p)!}.
\end{aligned}
\tag{SC18}
```

The sandwich coefficient follows by moving the first gamma past the $`p`$ antisymmetrized entries: the crossed term contributes $`(-1)^p5`$, and the $`p`$ anticommutators contribute $`-2p(-1)^p`$. Their sum is $`(-1)^p(5-2p)`$. Iterating a vector contraction gives $`5(5-1)\cdots(5-p+1)`$, with reversal sign $`(-1)^{p(p-1)/2}`$. These operations apply only to closed gamma contractions outside retained derivative arguments. No Fierz reduction or derivative commutation is performed.

<a id="47-reduce-the-su2-derivative-products-and-restore-index-symmetry"></a>

### Reduce the $`SU(2)`$ derivative products and restore index symmetry

The following matrix calculations are proofs about the existing $`L_{ij}`$ and its derivatives; their temporary letters do not define new fields. They justify every nontrivial triplet reduction used in the action.

First restore the unit-weight index operations by reversing (SC14):

```math
\begin{aligned}
&-\frac{L^{kl}}{2L^3}\left[(\mathcal D_aL_{ki})(\mathcal D^aL_{jl})+(\mathcal D_aL_{kj})(\mathcal D^aL_{il})\right]
=-\frac{L^{kl}}{L^3}\mathcal D_aL_{k(i}\mathcal D^aL_{j)l},\\
&2\mathcal D_a(L^{-1}E_b)-2\mathcal D_b(L^{-1}E_a)
=4\mathcal D_{[a}(L^{-1}E_{b]}).
\end{aligned}
\tag{SC21}
```

The fixed-index Majorana vector flip is symmetric. Raising the first SU(2) index contracts that symmetric tensor with epsilon:

```math
\begin{aligned}
\bar\varphi_i\gamma^a\varphi_j&=\bar\varphi_j\gamma^a\varphi_i,\\
\bar\varphi^i\gamma^a\varphi_i
&=\varepsilon^{ij}\bar\varphi_j\gamma^a\varphi_i
=\tfrac12\varepsilon^{ij}\left(\bar\varphi_j\gamma^a\varphi_i-\bar\varphi_i\gamma^a\varphi_j\right)=0,\\
\frac1{2L^3}\bar\varphi^m(\not{\mathcal D}L_{ij})\varphi_m
&=\frac{\mathcal D_aL_{ij}}{2L^3}\bar\varphi^m\gamma^a\varphi_m=0.
\end{aligned}
\tag{SC22}
```

Thus the last derivative-of-triplet singlet in (SC3) contributes zero in every descendant action product. This statement concerns the full identical spinors, not independent barred and unbarred test arrays.

For the remaining derivative terms, differentiate the defining norm algebraically with the covariant product rule:

```math
\begin{aligned}
L^2&=L_{ij}L^{ij},\\
2L\mathcal D_aL&=(\mathcal D_aL_{ij})L^{ij}+L_{ij}\mathcal D_aL^{ij}
=2L^{ij}\mathcal D_aL_{ij},\\
L\mathcal D_aL&=L^{ij}\mathcal D_aL_{ij}.
\end{aligned}
\tag{SC23}
```

Here metric/epsilon compatibility is used. This norm identity does not set a triplet derivative to zero in the aligned gauge. A general symmetric two-by-two matrix identity supplies the required tensor reduction. For this proof only let $`S`$ denote the matrix of entries $`L_{ij}`$, $`P`$ the matrix of entries $`\mathcal D_aL_{ij}`$ for a fixed tangent direction, and $`J=(\varepsilon^{ij})`$. These are temporary proof matrices, not additional fields. With $`S=\left(\begin{smallmatrix}u&v\\v&w\end{smallmatrix}\right)`$ and $`P=\left(\begin{smallmatrix}p&q\\q&r\end{smallmatrix}\right)`$, the three independent entries on both sides are

```math
\begin{aligned}
\mathop{\mathrm{adj}}\nolimits S&=\begin{pmatrix}w&-v\\-v&u\end{pmatrix},\\
(P\mathop{\mathrm{adj}}\nolimits S P)_{11}&=wp^2-2vpq+uq^2,\\
(P\mathop{\mathrm{adj}}\nolimits S P)_{12}&=wpq-v(pr+q^2)+uqr,\\
(P\mathop{\mathrm{adj}}\nolimits S P)_{22}&=wq^2-2vqr+ur^2,\\
P\mathop{\mathrm{adj}}\nolimits S P&=\mathop{\mathrm{tr}}\nolimits(\mathop{\mathrm{adj}}\nolimits S P)P-\det(P)S.
\end{aligned}
\tag{SC24}
```

Use $`\mathop{\mathrm{tr}}\nolimits(\mathop{\mathrm{adj}}\nolimits S P)=L\mathcal D_aL`$ and $`2\det P=\mathcal D_aL_{kl}\mathcal D_aL^{kl}`$; sum with $`\eta^{aa}`$, without changing derivative order. Multiplication by $`-L^{-3}`$ gives

```math
\begin{aligned}
L^{kl}\mathcal D_aL_{k(i}\mathcal D^aL_{j)l}
&=L(\mathcal D_aL)\mathcal D^aL_{ij}
-\tfrac12 L_{ij}\mathcal D_aL_{kl}\mathcal D^aL^{kl},\\
-L^{-3}L^{kl}\mathcal D_aL_{k(i}\mathcal D^aL_{j)l}
&=-L^{-2}(\mathcal D_aL)\mathcal D^aL_{ij}
+\frac{L_{ij}}{2L^3}\mathcal D_aL_{kl}\mathcal D^aL^{kl}.
\end{aligned}
\tag{SC25}
```

The second SU(2) identity involves the symmetric matrix with entries $`\bar\varphi_i\gamma_a\varphi_j`$. For this proof denote those entries by $`B=\left(\begin{smallmatrix}b&d\\d&e\end{smallmatrix}\right)`$. With $`\mathop{\mathrm{sym}}\nolimits M=(M+M^T)/2`$, direct multiplication gives

```math
\begin{aligned}
\mathop{\mathrm{tr}}\nolimits(\mathop{\mathrm{adj}}\nolimits B S)&=eu-2dv+bw,\\
\mathop{\mathrm{sym}}\nolimits(SJP)_{11}&=uq-vp,\\
\mathop{\mathrm{sym}}\nolimits(SJP)_{12}&=\tfrac12(ur-wp),\\
\mathop{\mathrm{sym}}\nolimits(SJP)_{22}&=vr-wq,\\
\mathop{\mathrm{sym}}\nolimits(PJB)_{11}&=pd-qb,\\
\mathop{\mathrm{sym}}\nolimits(PJB)_{12}&=\tfrac12(pe-rb),\\
\mathop{\mathrm{sym}}\nolimits(PJB)_{22}&=qe-rd,\\
\mathop{\mathrm{sym}}\nolimits(SJB\mathop{\mathrm{adj}}\nolimits S P)
&=(eu-2dv+bw)\mathop{\mathrm{sym}}\nolimits(SJP)
+(uw-v^2)\mathop{\mathrm{sym}}\nolimits(PJB).
\end{aligned}
\tag{SC26}
```

The three entries in the last line are, respectively,

```math
\begin{aligned}
& (eu-2dv+bw)(uq-vp)+(uw-v^2)(pd-qb),\\
& \tfrac12(eu-2dv+bw)(ur-wp)+\tfrac12(uw-v^2)(pe-rb),\\
& (eu-2dv+bw)(vr-wq)+(uw-v^2)(qe-rd).
\end{aligned}
\tag{SC27}
```

Restoring indices and $`\det S=L^2/2`$ yields the identity, followed by its substitution into the two original terms:

```math
\begin{aligned}
L_{k(i}L^{lm}\bar\varphi^k(\not{\mathcal D}L_{j)l})\varphi_m
={}&L^{mn}\bar\varphi_m\gamma_a\varphi_n\,L_{k(i}\mathcal D^aL_{j)}{}^k
+\frac{L^2}{2}\bar\varphi^k(\not{\mathcal D}L_{k(i})\varphi_{j)},\\
&-\frac3{L^5}L_{k(i}L^{lm}\bar\varphi^k(\not{\mathcal D}L_{j)l})\varphi_m
+\frac1{2L^3}\bar\varphi^k(\not{\mathcal D}L_{k(i})\varphi_{j)}\\
={}&-\frac3{L^5}L^{mn}\bar\varphi_m\gamma_a\varphi_n\,L_{k(i}\mathcal D^aL_{j)}{}^k
+\frac{-3/2+1/2}{L^3}\bar\varphi^k(\not{\mathcal D}L_{k(i})\varphi_{j)}\\
={}&-\frac3{L^5}L^{mn}\bar\varphi_m\gamma_a\varphi_n\,L_{k(i}\mathcal D^aL_{j)}{}^k
-\frac1{L^3}\bar\varphi^k(\not{\mathcal D}L_{k(i})\varphi_{j)}.
\end{aligned}
\tag{SC28}
```

Now collect the $`N`$ and $`E`$ bilinears without changing spinor order. Collect the two $`\chi`$ terms using $`L_{kl}\bar\chi^k\varphi^l=L^{kl}\bar\chi_k\varphi_l`$; the two epsilon transfers give a positive sign:

```math
\begin{aligned}
&\frac{iN}{L^3}\bar\varphi_{(i}\varphi_{j)}-\frac1{L^3}\bar\varphi_{(i}\not E\varphi_{j)}
=\frac1{L^3}\bar\varphi_{(i}(iN-\not E)\varphi_{j)},\\
&-\frac{3iN}{L^5}L_{ij}L^{kl}\bar\varphi_k\varphi_l
+\frac3{L^5}L_{ij}L^{kl}\bar\varphi_k\not E\varphi_l
=-\frac3{L^5}L_{ij}L^{kl}\bar\varphi_k(iN-\not E)\varphi_l,\\
&-\frac{16i}{L}\bar\chi_{(i}\varphi_{j)}+\frac{16i}{L^3}L_{ij}L^{kl}\bar\chi_k\varphi_l
=-\frac{16i}{L}\left(\delta_{(i}{}^k\delta_{j)}{}^l-\frac{L_{ij}L^{kl}}{L^2}\right)\bar\chi_k\varphi_l.
\end{aligned}
\tag{SC29}
```

Equations (SC22), (SC25), (SC28) and (SC29) turn the literal input (SC3) into the following collected map:

```math
\begin{aligned}
Y'_{ij}={}&\frac1L\Box_cL_{ij}-\frac1{L^2}(\mathcal D_aL)\mathcal D^aL_{ij}\\
&+\frac{L_{ij}}L\left(4D+\frac83T^2-\frac{N^2+E_aE^a}{L^2}
+\frac{\mathcal D_aL_{kl}\mathcal D^aL^{kl}}{2L^2}\right)\\
&+\frac2{L^3}L_{k(i}\mathcal D^aL_{j)}{}^k
\left(E_a-\frac3{2L^2}L^{mn}\bar\varphi_m\gamma_a\varphi_n\right)\\
&+\frac1{L^3}\bar\varphi_{(i}(iN-\not E)\varphi_{j)}
-\frac3{L^5}L_{ij}L^{kl}\bar\varphi_k(iN-\not E)\varphi_l\\
&-\frac{16i}{L}\left(\delta_{(i}{}^k\delta_{j)}{}^l-\frac{L_{ij}L^{kl}}{L^2}\right)\bar\chi_k\varphi_l\\
&+\frac2{L^3}L_{k(i}\bar\varphi^k\not{\mathcal D}\varphi_{j)}
-\frac1{L^3}\bar\varphi^k(\not{\mathcal D}L_{k(i})\varphi_{j)}\\
&+\frac{2i}{L^3}L_{ij}\bar\varphi^k\gamma\!\cdot\!T\varphi_k
+O_{\rm explicit}(\mathrm{fermion}^4).
\end{aligned}
\tag{SC30}
```

The $`-2NL^{-3}`$ and $`-2iL^{-3}\not E`$ terms in (SC2) have the common coefficient $`-2L^{-3}L_{ij}`$. The two antisymmetric derivatives in (SC4) combine by linearity. Hence

```math
\begin{aligned}
\lambda'_i={}&-\frac{2i}{L}\not{\mathcal D}\varphi_i+\frac{16}{L}L_{ij}\chi^j
+\frac4L\gamma\!\cdot\!T\varphi_i
-\frac2{L^3}L_{ij}(N+i\not E)\varphi^j\\
&+\frac{2i}{L^3}(\not{\mathcal D}L_{ij})L^{jk}\varphi_k
+O_{\rm explicit}(\mathrm{fermion}^3),\\
\widehat F'_{ab}={}&2\mathcal D_{[a}\!\left(\frac{2E_{b]}}L
-\frac{L_{ij}}{L^3}\bar\varphi^i\gamma_{b]}\varphi^j\right)
+\frac2L L_{ij}\widehat R_{ab}{}^{ij}(V)\\
&-\frac2{L^3}L_k{}^l\mathcal D_{[a}L^{kp}\mathcal D_{b]}L_{lp}
-\frac iL\bar\varphi^i\widehat R_{ab,i}(Q).
\end{aligned}
\tag{SC31}
```

No new map name is assigned to the combinations $`N+i\not E`$, $`iN-\not E`$ or $`\widehat G^{ab}-16T^{ab}`$. They are written in full wherever they occur. The barred version of the collected spinor is obtained by (SC6)–(SC8), reversing the Clifford order and the rank-two sign while keeping scalar $`i`$.

<a id="48-every-collected-source-contribution-with-its-primed-maps-inserted"></a>

### Every collected source contribution with its primed maps inserted

Each left-hand side below identifies one contribution in (C.1). Its right-hand side distributes the outer products using (SC1)–(SC8) and the reductions (SC21)–(SC31), with only zero or two explicit odd factors. The labels are the original Step-4 source-group numbers, retained for traceability; they are not additional fields. A displayed product of already written scalar or Clifford brackets is left factored when that exposes a common coefficient. Derivative arguments and full gauged background composites remain closed.

All these equalities are understood through physical fermion order two under A1. In particular a closed even bracket is not a declaration of a bosonic projection. The derivative acting on the full argument always remains supercovariant.

**Source contribution 1.**

```math
\begin{aligned}
Y'^{ij}Y'_{ij}={}&\frac{1}{L^{2}} \Box_c\!\left(L_{ij}\right) \Box_c\!\left(L^{ij}\right) - \frac{2}{L^{3}} \Box_c\!\left(L_{ij}\right) \mathcal D_{a}\!\left(L\right) \mathcal D^{a}\!\left(L^{ij}\right) +\frac{2}{L^{2}} \left(4 D +\frac{8}{3} T_{ab} T^{ab} - \frac{1}{L^{2}} E_{a} E^{a} - \frac{N^{2}}{L^{2}} +\frac{1}{2 L^{2}} \mathcal D_{a}\!\left(L_{kl}\right) \mathcal D^{a}\!\left(L^{kl}\right)\right) L_{ij} \Box_c\!\left(L^{ij}\right) +\frac{2}{L^{4}} \Box_c\!\left(L^{ij}\right) \left(\bar\varphi_{(i} \left(i N - \gamma^{b} E_{b}\right) \varphi_{j)}\right)\\
&+\frac{6}{L^{6}} L_{i}{}^{j} L_{kl} \Box_c\!\left(L^{kl}\right) \bar\varphi^{i} \left(i N - \gamma^{a} E_{a}\right) \varphi_{j} +\frac{4}{L^{4}} E_{a} \left(L_{k(i} \mathcal D^{a}\!\left(L_{j)}{}^{k}\right)\right) \Box_c\!\left(L^{ij}\right) +\frac{6}{L^{6}} \left(L_{m(k} \mathcal D_{a}\!\left(L_{l)}{}^{m}\right)\right) L_{i}{}^{j} \Box_c\!\left(L^{kl}\right) \bar\varphi^{i} \gamma^{a} \varphi_{j} - \frac{32 i}{L^{2}} \Box_c\!\left(L^{ij}\right) \left(\bar\chi_{(i} \varphi_{j)}\right)\\
&- \frac{32 i}{L^{4}} L_{i}{}^{j} L_{kl} \Box_c\!\left(L^{kl}\right) \bar\chi^{i} \varphi_{j} +\frac{4}{L^{4}} \Box_c\!\left(L^{ij}\right) \left(L_{k(i} \bar\varphi^{k} \gamma^{a} \mathcal D_{a}\!\left(\varphi_{j)}\right)\right) - \frac{2}{L^{4}} \Box_c\!\left(L^{ij}\right) \left(\bar\varphi^{k} \gamma^{a} \mathcal D_{a}\!\left(L_{k(i}\right) \varphi_{j)}\right) +\frac{4 i}{L^{4}} L_{jk} \Box_c\!\left(L^{jk}\right) T_{ab} \bar\varphi^{i} \gamma^{ab} \varphi_{i}\\
&+\frac{1}{L^{4}} \mathcal D_{a}\!\left(L\right) \mathcal D_{b}\!\left(L\right) \mathcal D^{a}\!\left(L_{ij}\right) \mathcal D^{b}\!\left(L^{ij}\right) - \frac{2}{L^{3}} \left(4 D +\frac{8}{3} T_{bc} T^{bc} - \frac{1}{L^{2}} E_{b} E^{b} - \frac{N^{2}}{L^{2}} +\frac{1}{2 L^{2}} \mathcal D_{b}\!\left(L_{kl}\right) \mathcal D^{b}\!\left(L^{kl}\right)\right) L_{ij} \mathcal D_{a}\!\left(L\right) \mathcal D^{a}\!\left(L^{ij}\right) - \frac{2}{L^{5}} \mathcal D_{a}\!\left(L\right) \mathcal D^{a}\!\left(L^{ij}\right) \left(\bar\varphi_{(i} \left(i N - \gamma^{c} E_{c}\right) \varphi_{j)}\right) - \frac{6}{L^{7}} L_{i}{}^{j} L_{kl} \mathcal D_{a}\!\left(L\right) \mathcal D^{a}\!\left(L^{kl}\right) \bar\varphi^{i} \left(i N - \gamma^{b} E_{b}\right) \varphi_{j}\\
&- \frac{4}{L^{5}} E_{a} \left(L_{k(i} \mathcal D^{a}\!\left(L_{j)}{}^{k}\right)\right) \mathcal D_{b}\!\left(L\right) \mathcal D^{b}\!\left(L^{ij}\right) - \frac{6}{L^{7}} \left(L_{m(k} \mathcal D_{a}\!\left(L_{l)}{}^{m}\right)\right) L_{i}{}^{j} \mathcal D_{b}\!\left(L\right) \mathcal D^{b}\!\left(L^{kl}\right) \bar\varphi^{i} \gamma^{a} \varphi_{j} +\frac{32 i}{L^{3}} \mathcal D_{a}\!\left(L\right) \mathcal D^{a}\!\left(L^{ij}\right) \left(\bar\chi_{(i} \varphi_{j)}\right) +\frac{32 i}{L^{5}} L_{i}{}^{j} L_{kl} \mathcal D_{a}\!\left(L\right) \mathcal D^{a}\!\left(L^{kl}\right) \bar\chi^{i} \varphi_{j}\\
&- \frac{4}{L^{5}} \mathcal D_{a}\!\left(L\right) \mathcal D^{a}\!\left(L^{ij}\right) \left(L_{k(i} \bar\varphi^{k} \gamma^{b} \mathcal D_{b}\!\left(\varphi_{j)}\right)\right) +\frac{2}{L^{5}} \mathcal D_{a}\!\left(L\right) \mathcal D^{a}\!\left(L^{ij}\right) \left(\bar\varphi^{k} \gamma^{b} \mathcal D_{b}\!\left(L_{k(i}\right) \varphi_{j)}\right) - \frac{4 i}{L^{5}} L_{jk} \mathcal D_{c}\!\left(L\right) \mathcal D^{c}\!\left(L^{jk}\right) T_{ab} \bar\varphi^{i} \gamma^{ab} \varphi_{i} +\left(4 D +\frac{8}{3} T_{ab} T^{ab} - \frac{1}{L^{2}} E_{a} E^{a} - \frac{N^{2}}{L^{2}} +\frac{1}{2 L^{2}} \mathcal D_{a}\!\left(L_{ij}\right) \mathcal D^{a}\!\left(L^{ij}\right)\right) \left(4 D +\frac{8}{3} T_{cd} T^{cd} - \frac{1}{L^{2}} E_{c} E^{c} - \frac{N^{2}}{L^{2}} +\frac{1}{2 L^{2}} \mathcal D_{c}\!\left(L_{kl}\right) \mathcal D^{c}\!\left(L^{kl}\right)\right)\\
&+\frac{2}{L^{4}} \left(4 D +\frac{8}{3} T_{ab} T^{ab} - \frac{1}{L^{2}} E_{a} E^{a} - \frac{N^{2}}{L^{2}} +\frac{1}{2 L^{2}} \mathcal D_{a}\!\left(L_{kl}\right) \mathcal D^{a}\!\left(L^{kl}\right)\right) L^{ij} \left(\bar\varphi_{(i} \left(i N - \gamma^{d} E_{d}\right) \varphi_{j)}\right) +\frac{6}{L^{4}} \left(4 D +\frac{8}{3} T_{ab} T^{ab} - \frac{1}{L^{2}} E_{a} E^{a} - \frac{N^{2}}{L^{2}} +\frac{1}{2 L^{2}} \mathcal D_{a}\!\left(L_{kl}\right) \mathcal D^{a}\!\left(L^{kl}\right)\right) L_{i}{}^{j} \bar\varphi^{i} \left(i N - \gamma^{c} E_{c}\right) \varphi_{j} +\frac{4}{L^{4}} E_{a} \left(4 D +\frac{8}{3} T_{bc} T^{bc} - \frac{1}{L^{2}} E_{b} E^{b} - \frac{N^{2}}{L^{2}} +\frac{1}{2 L^{2}} \mathcal D_{b}\!\left(L_{kl}\right) \mathcal D^{b}\!\left(L^{kl}\right)\right) \left(L_{m(i} \mathcal D^{a}\!\left(L_{j)}{}^{m}\right)\right) L^{ij} +\frac{6}{L^{6}} \left(4 D +\frac{8}{3} T_{bc} T^{bc} - \frac{1}{L^{2}} E_{b} E^{b} - \frac{N^{2}}{L^{2}} +\frac{1}{2 L^{2}} \mathcal D_{b}\!\left(L_{mn}\right) \mathcal D^{b}\!\left(L^{mn}\right)\right) \left(L_{o(k} \mathcal D_{a}\!\left(L_{l)}{}^{o}\right)\right) L_{i}{}^{j} L^{kl} \bar\varphi^{i} \gamma^{a} \varphi_{j}\\
&- \frac{32 i}{L^{2}} \left(4 D +\frac{8}{3} T_{ab} T^{ab} - \frac{1}{L^{2}} E_{a} E^{a} - \frac{N^{2}}{L^{2}} +\frac{1}{2 L^{2}} \mathcal D_{a}\!\left(L_{kl}\right) \mathcal D^{a}\!\left(L^{kl}\right)\right) L^{ij} \left(\bar\chi_{(i} \varphi_{j)}\right) - \frac{32 i}{L^{2}} \left(4 D +\frac{8}{3} T_{ab} T^{ab} - \frac{1}{L^{2}} E_{a} E^{a} - \frac{N^{2}}{L^{2}} +\frac{1}{2 L^{2}} \mathcal D_{a}\!\left(L_{kl}\right) \mathcal D^{a}\!\left(L^{kl}\right)\right) L_{i}{}^{j} \bar\chi^{i} \varphi_{j} +\frac{4}{L^{4}} \left(4 D +\frac{8}{3} T_{ab} T^{ab} - \frac{1}{L^{2}} E_{a} E^{a} - \frac{N^{2}}{L^{2}} +\frac{1}{2 L^{2}} \mathcal D_{a}\!\left(L_{kl}\right) \mathcal D^{a}\!\left(L^{kl}\right)\right) L^{ij} \left(L_{m(i} \bar\varphi^{m} \gamma^{c} \mathcal D_{c}\!\left(\varphi_{j)}\right)\right) - \frac{2}{L^{4}} \left(4 D +\frac{8}{3} T_{ab} T^{ab} - \frac{1}{L^{2}} E_{a} E^{a} - \frac{N^{2}}{L^{2}} +\frac{1}{2 L^{2}} \mathcal D_{a}\!\left(L_{kl}\right) \mathcal D^{a}\!\left(L^{kl}\right)\right) L^{ij} \left(\bar\varphi^{m} \gamma^{c} \mathcal D_{c}\!\left(L_{m(i}\right) \varphi_{j)}\right)\\
&+\frac{4 i}{L^{2}} \left(4 D +\frac{8}{3} T_{cd} T^{cd} - \frac{1}{L^{2}} E_{c} E^{c} - \frac{N^{2}}{L^{2}} +\frac{1}{2 L^{2}} \mathcal D_{c}\!\left(L_{jk}\right) \mathcal D^{c}\!\left(L^{jk}\right)\right) T_{ab} \bar\varphi^{i} \gamma^{ab} \varphi_{i} +\frac{4}{L^{6}} E_{a} \left(L_{k}{}^{(i} \mathcal D^{a}\!\left(L^{j)k}\right)\right) \left(\bar\varphi_{(i} \left(i N - \gamma^{c} E_{c}\right) \varphi_{j)}\right) +\frac{12}{L^{8}} E_{a} \left(L_{m(k} \mathcal D^{a}\!\left(L_{l)}{}^{m}\right)\right) L_{i}{}^{j} L^{kl} \bar\varphi^{i} \left(i N - \gamma^{b} E_{b}\right) \varphi_{j} +\frac{4}{L^{6}} E_{a} E_{b} \left(L_{k(i} \mathcal D^{a}\!\left(L_{j)}{}^{k}\right)\right) \left(L_{l}{}^{(i} \mathcal D^{b}\!\left(L^{j)l}\right)\right)\\
&+\frac{6}{L^{8}} E_{b} \left(L_{m(k} \mathcal D^{b}\!\left(L_{l)}{}^{m}\right)\right) \left(L_{n}{}^{(k} \mathcal D_{a}\!\left(L^{l)n}\right)\right) L_{i}{}^{j} \bar\varphi^{i} \gamma^{a} \varphi_{j} - \frac{64 i}{L^{4}} E_{a} \left(L_{k}{}^{(i} \mathcal D^{a}\!\left(L^{j)k}\right)\right) \left(\bar\chi_{(i} \varphi_{j)}\right) - \frac{64 i}{L^{6}} E_{a} \left(L_{m(k} \mathcal D^{a}\!\left(L_{l)}{}^{m}\right)\right) L_{i}{}^{j} L^{kl} \bar\chi^{i} \varphi_{j} +\frac{8}{L^{6}} E_{a} \left(L_{k}{}^{(i} \mathcal D^{a}\!\left(L^{j)k}\right)\right) \left(L_{l(i} \bar\varphi^{l} \gamma^{b} \mathcal D_{b}\!\left(\varphi_{j)}\right)\right)\\
&- \frac{4}{L^{6}} E_{a} \left(L_{k}{}^{(i} \mathcal D^{a}\!\left(L^{j)k}\right)\right) \left(\bar\varphi^{l} \gamma^{b} \mathcal D_{b}\!\left(L_{l(i}\right) \varphi_{j)}\right) +\frac{8 i}{L^{6}} E_{c} \left(L_{l(j} \mathcal D^{c}\!\left(L_{k)}{}^{l}\right)\right) L^{jk} T_{ab} \bar\varphi^{i} \gamma^{ab} \varphi_{i} +\frac{6}{L^{8}} E_{b} \left(L_{m(k} \mathcal D_{a}\!\left(L_{l)}{}^{m}\right)\right) \left(L_{n}{}^{(k} \mathcal D^{b}\!\left(L^{l)n}\right)\right) L_{i}{}^{j} \bar\varphi^{i} \gamma^{a} \varphi_{j}
\end{aligned}
\tag{I.1}
```

**Source contribution 2.**

```math
\begin{aligned}
-g\rho'Y'^{ij}L_{ij}={}&- \frac{2 N g}{L^{2}} L_{ij} \Box_c\!\left(L^{ij}\right) +\frac{2 N g}{L^{3}} L_{ij} \mathcal D_{a}\!\left(L\right) \mathcal D^{a}\!\left(L^{ij}\right) - 2 N g \left(4 D +\frac{8}{3} T_{ab} T^{ab} - \frac{1}{L^{2}} E_{a} E^{a} - \frac{N^{2}}{L^{2}} +\frac{1}{2 L^{2}} \mathcal D_{a}\!\left(L_{ij}\right) \mathcal D^{a}\!\left(L^{ij}\right)\right) - \frac{2 N g}{L^{4}} L^{ij} \left(\bar\varphi_{(i} \left(i N - \gamma^{b} E_{b}\right) \varphi_{j)}\right)\\
&- \frac{6 N g}{L^{4}} L_{i}{}^{j} \bar\varphi^{i} \left(i N - \gamma^{a} E_{a}\right) \varphi_{j} - \frac{4 N g}{L^{4}} E_{a} \left(L_{k(i} \mathcal D^{a}\!\left(L_{j)}{}^{k}\right)\right) L^{ij} - \frac{6 N g}{L^{6}} \left(L_{m(k} \mathcal D_{a}\!\left(L_{l)}{}^{m}\right)\right) L_{i}{}^{j} L^{kl} \bar\varphi^{i} \gamma^{a} \varphi_{j} +\frac{32 i N g}{L^{2}} L^{ij} \left(\bar\chi_{(i} \varphi_{j)}\right)\\
&+\frac{32 i N g}{L^{2}} L_{i}{}^{j} \bar\chi^{i} \varphi_{j} - \frac{4 N g}{L^{4}} L^{ij} \left(L_{k(i} \bar\varphi^{k} \gamma^{a} \mathcal D_{a}\!\left(\varphi_{j)}\right)\right) +\frac{2 N g}{L^{4}} L^{ij} \left(\bar\varphi^{k} \gamma^{a} \mathcal D_{a}\!\left(L_{k(i}\right) \varphi_{j)}\right) - \frac{4 i N g}{L^{2}} T_{ab} \bar\varphi^{i} \gamma^{ab} \varphi_{i}\\
&+\frac{i g}{L^{4}} L_{i}{}^{j} L_{kl} \Box_c\!\left(L^{kl}\right) \bar\varphi^{i} \varphi_{j} - \frac{i g}{L^{5}} L_{i}{}^{j} L_{kl} \mathcal D_{a}\!\left(L\right) \mathcal D^{a}\!\left(L^{kl}\right) \bar\varphi^{i} \varphi_{j} +\frac{i g}{L^{2}} \left(4 D +\frac{8}{3} T_{ab} T^{ab} - \frac{1}{L^{2}} E_{a} E^{a} - \frac{N^{2}}{L^{2}} +\frac{1}{2 L^{2}} \mathcal D_{a}\!\left(L_{kl}\right) \mathcal D^{a}\!\left(L^{kl}\right)\right) L_{i}{}^{j} \bar\varphi^{i} \varphi_{j} +\frac{2 i g}{L^{6}} E_{a} \left(L_{m(k} \mathcal D^{a}\!\left(L_{l)}{}^{m}\right)\right) L_{i}{}^{j} L^{kl} \bar\varphi^{i} \varphi_{j}
\end{aligned}
\tag{I.2}
```

**Source contribution 3.**

```math
\begin{aligned}
-\frac12\bar\lambda'{}^i\not{\mathcal D}\lambda'_i={}&- \frac{2}{L} \mathcal D_{a}\!\left(\bar\varphi_{i}\right) \gamma^{a} \gamma^{b} \mathcal D_{b}\!\left(\frac{1}{L} \gamma^{c} \mathcal D_{c}\!\left(\varphi^{i}\right)\right) - \frac{16 i}{L} \mathcal D_{a}\!\left(\bar\varphi_{i}\right) \gamma^{a} \gamma^{b} \mathcal D_{b}\!\left(\frac{1}{L} L^{i}{}_{j} \chi^{j}\right) - \frac{4 i}{L} \mathcal D_{a}\!\left(\bar\varphi_{i}\right) \gamma^{a} \gamma^{b} \mathcal D_{b}\!\left(\frac{1}{L} \gamma^{cd} T_{cd} \varphi^{i}\right) +\frac{2 i}{L} \mathcal D_{a}\!\left(\bar\varphi_{i}\right) \gamma^{a} \gamma^{b} \mathcal D_{b}\!\left(\frac{1}{L^{3}} L^{i}{}_{j} \left(i \gamma^{c} E_{c} +N\right) \varphi^{j}\right)\\
&+\frac{2}{L} \mathcal D_{a}\!\left(\bar\varphi_{i}\right) \gamma^{a} \gamma^{b} \mathcal D_{b}\!\left(\frac{1}{L^{3}} \gamma^{c} \mathcal D_{c}\!\left(L^{i}{}_{j}\right) L^{jk} \varphi_{k}\right) +\frac{16 i}{L} L_{i}{}^{j} \bar\chi^{i} \gamma^{a} \mathcal D_{a}\!\left(\frac{1}{L} \gamma^{b} \mathcal D_{b}\!\left(\varphi_{j}\right)\right) - \frac{128}{L} L_{i}{}^{j} \bar\chi^{i} \gamma^{a} \mathcal D_{a}\!\left(\frac{1}{L} L_{jk} \chi^{k}\right) - \frac{32}{L} L_{i}{}^{j} \bar\chi^{i} \gamma^{a} \mathcal D_{a}\!\left(\frac{1}{L} \gamma^{bc} T_{bc} \varphi_{j}\right)\\
&+\frac{16}{L} L_{i}{}^{j} \bar\chi^{i} \gamma^{a} \mathcal D_{a}\!\left(\frac{1}{L^{3}} L_{jk} \left(i \gamma^{b} E_{b} +N\right) \varphi^{k}\right) - \frac{16 i}{L} L_{i}{}^{j} \bar\chi^{i} \gamma^{a} \mathcal D_{a}\!\left(\frac{1}{L^{3}} \gamma^{b} \mathcal D_{b}\!\left(L_{jk}\right) L^{kl} \varphi_{l}\right) - \frac{4 i}{L} T_{ab} \bar\varphi^{i} \gamma^{ab} \gamma^{c} \mathcal D_{c}\!\left(\frac{1}{L} \gamma^{d} \mathcal D_{d}\!\left(\varphi_{i}\right)\right) +\frac{32}{L} T_{ab} \bar\varphi^{i} \gamma^{ab} \gamma^{c} \mathcal D_{c}\!\left(\frac{1}{L} L_{ij} \chi^{j}\right)\\
&+\frac{8}{L} T_{ab} \bar\varphi^{i} \gamma^{ab} \gamma^{c} \mathcal D_{c}\!\left(\frac{1}{L} \gamma^{de} T_{de} \varphi_{i}\right) - \frac{4}{L} T_{ab} \bar\varphi^{i} \gamma^{ab} \gamma^{c} \mathcal D_{c}\!\left(\frac{1}{L^{3}} L_{ij} \left(i \gamma^{d} E_{d} +N\right) \varphi^{j}\right) +\frac{4 i}{L} T_{ab} \bar\varphi^{i} \gamma^{ab} \gamma^{c} \mathcal D_{c}\!\left(\frac{1}{L^{3}} \gamma^{d} \mathcal D_{d}\!\left(L_{ij}\right) L^{jk} \varphi_{k}\right) - \frac{2 i}{L^{3}} L_{i}{}^{j} \bar\varphi^{i} \left(i E_{b} \gamma^{b} +N\right) \gamma^{a} \mathcal D_{a}\!\left(\frac{1}{L} \gamma^{c} \mathcal D_{c}\!\left(\varphi_{j}\right)\right)\\
&+\frac{16}{L^{3}} L_{i}{}^{j} \bar\varphi^{i} \left(i E_{b} \gamma^{b} +N\right) \gamma^{a} \mathcal D_{a}\!\left(\frac{1}{L} L_{jk} \chi^{k}\right) +\frac{4}{L^{3}} L_{i}{}^{j} \bar\varphi^{i} \left(i E_{b} \gamma^{b} +N\right) \gamma^{a} \mathcal D_{a}\!\left(\frac{1}{L} \gamma^{cd} T_{cd} \varphi_{j}\right) - \frac{2}{L^{3}} L_{i}{}^{j} \bar\varphi^{i} \left(i E_{b} \gamma^{b} +N\right) \gamma^{a} \mathcal D_{a}\!\left(\frac{1}{L^{3}} L_{jk} \left(i \gamma^{c} E_{c} +N\right) \varphi^{k}\right) +\frac{2 i}{L^{3}} L_{i}{}^{j} \bar\varphi^{i} \left(i E_{b} \gamma^{b} +N\right) \gamma^{a} \mathcal D_{a}\!\left(\frac{1}{L^{3}} \gamma^{c} \mathcal D_{c}\!\left(L_{jk}\right) L^{kl} \varphi_{l}\right)\\
&- \frac{2}{L^{3}} L_{ik} \mathcal D_{a}\!\left(L^{jk}\right) \bar\varphi^{i} \gamma^{a} \gamma^{b} \mathcal D_{b}\!\left(\frac{1}{L} \gamma^{c} \mathcal D_{c}\!\left(\varphi_{j}\right)\right) - \frac{16 i}{L^{3}} L_{ik} \mathcal D_{a}\!\left(L^{jk}\right) \bar\varphi^{i} \gamma^{a} \gamma^{b} \mathcal D_{b}\!\left(\frac{1}{L} L_{jl} \chi^{l}\right) - \frac{4 i}{L^{3}} L_{ik} \mathcal D_{a}\!\left(L^{jk}\right) \bar\varphi^{i} \gamma^{a} \gamma^{b} \mathcal D_{b}\!\left(\frac{1}{L} \gamma^{cd} T_{cd} \varphi_{j}\right) +\frac{2 i}{L^{3}} L_{ik} \mathcal D_{a}\!\left(L^{jk}\right) \bar\varphi^{i} \gamma^{a} \gamma^{b} \mathcal D_{b}\!\left(\frac{1}{L^{3}} L_{jl} \left(i \gamma^{c} E_{c} +N\right) \varphi^{l}\right)\\
&+\frac{2}{L^{3}} L_{ik} \mathcal D_{a}\!\left(L^{jk}\right) \bar\varphi^{i} \gamma^{a} \gamma^{b} \mathcal D_{b}\!\left(\frac{1}{L^{3}} \gamma^{c} \mathcal D_{c}\!\left(L_{jl}\right) L^{lm} \varphi_{m}\right)
\end{aligned}
\tag{I.3}
```

**Source contribution 4.**

```math
\begin{aligned}
i\bar\lambda'{}^i\gamma\!\cdot\!T\lambda'_i={}&\frac{4 i}{L^{2}} T_{bc} \mathcal D_{a}\!\left(\bar\varphi_{i}\right) \gamma^{a} \gamma^{bc} \gamma^{d} \mathcal D_{d}\!\left(\varphi^{i}\right) +\frac{32}{L^{2}} L^{ij} T_{bc} \mathcal D_{a}\!\left(\bar\varphi_{i}\right) \gamma^{a} \gamma^{bc} \chi_{j} - \frac{8}{L^{2}} T_{bc} T_{de} \mathcal D_{a}\!\left(\bar\varphi_{i}\right) \gamma^{a} \gamma^{bc} \gamma^{de} \varphi^{i} - \frac{4}{L^{4}} L^{ij} T_{bc} \mathcal D_{a}\!\left(\bar\varphi_{i}\right) \gamma^{a} \gamma^{bc} \left(i \gamma^{d} E_{d} +N\right) \varphi_{j}\\
&+\frac{4 i}{L^{4}} L^{j}{}_{k} \mathcal D_{d}\!\left(L^{ik}\right) T_{bc} \mathcal D_{a}\!\left(\bar\varphi_{i}\right) \gamma^{a} \gamma^{bc} \gamma^{d} \varphi_{j} +\frac{32}{L^{2}} L_{i}{}^{j} T_{ab} \bar\chi^{i} \gamma^{ab} \gamma^{c} \mathcal D_{c}\!\left(\varphi_{j}\right) +128 i T_{ab} \bar\chi^{i} \gamma^{ab} \chi_{i} +\frac{64 i}{L^{2}} L_{i}{}^{j} T_{ab} T_{cd} \bar\chi^{i} \gamma^{ab} \gamma^{cd} \varphi_{j}\\
&- \frac{16 i}{L^{2}} T_{ab} \bar\chi^{i} \gamma^{ab} \left(i \gamma^{c} E_{c} +N\right) \varphi_{i} - \frac{32}{L^{4}} L_{ik} L^{j}{}_{l} \mathcal D_{c}\!\left(L^{kl}\right) T_{ab} \bar\chi^{i} \gamma^{ab} \gamma^{c} \varphi_{j} - \frac{8}{L^{2}} T_{ab} T_{cd} \bar\varphi^{i} \gamma^{ab} \gamma^{cd} \gamma^{e} \mathcal D_{e}\!\left(\varphi_{i}\right) +\frac{64 i}{L^{2}} L_{i}{}^{j} T_{ab} T_{cd} \bar\varphi^{i} \gamma^{ab} \gamma^{cd} \chi_{j}\\
&- \frac{16 i}{L^{2}} T_{ab} T_{cd} T_{ef} \bar\varphi^{i} \gamma^{ab} \gamma^{cd} \gamma^{ef} \varphi_{i} - \frac{8 i}{L^{4}} L_{i}{}^{j} T_{ab} T_{cd} \bar\varphi^{i} \gamma^{ab} \gamma^{cd} \left(i \gamma^{e} E_{e} +N\right) \varphi_{j} - \frac{8}{L^{4}} L^{j}{}_{k} \mathcal D_{e}\!\left(L_{i}{}^{k}\right) T_{ab} T_{cd} \bar\varphi^{i} \gamma^{ab} \gamma^{cd} \gamma^{e} \varphi_{j} - \frac{4}{L^{4}} L_{i}{}^{j} T_{ab} \bar\varphi^{i} \left(i E_{d} \gamma^{d} +N\right) \gamma^{ab} \gamma^{c} \mathcal D_{c}\!\left(\varphi_{j}\right)\\
&- \frac{16 i}{L^{2}} T_{ab} \bar\varphi^{i} \left(i E_{c} \gamma^{c} +N\right) \gamma^{ab} \chi_{i} - \frac{8 i}{L^{4}} L_{i}{}^{j} T_{ab} T_{cd} \bar\varphi^{i} \left(i E_{e} \gamma^{e} +N\right) \gamma^{ab} \gamma^{cd} \varphi_{j} +\frac{2 i}{L^{4}} T_{ab} \bar\varphi^{i} \left(i E_{c} \gamma^{c} +N\right) \gamma^{ab} \left(i \gamma^{d} E_{d} +N\right) \varphi_{i} +\frac{4}{L^{6}} L_{ik} L^{j}{}_{l} \mathcal D_{c}\!\left(L^{kl}\right) T_{ab} \bar\varphi^{i} \left(i E_{d} \gamma^{d} +N\right) \gamma^{ab} \gamma^{c} \varphi_{j}\\
&+\frac{4 i}{L^{4}} L_{ik} \mathcal D_{a}\!\left(L^{jk}\right) T_{bc} \bar\varphi^{i} \gamma^{a} \gamma^{bc} \gamma^{d} \mathcal D_{d}\!\left(\varphi_{j}\right) +\frac{32}{L^{4}} L_{ik} L^{j}{}_{l} \mathcal D_{a}\!\left(L^{lk}\right) T_{bc} \bar\varphi^{i} \gamma^{a} \gamma^{bc} \chi_{j} - \frac{8}{L^{4}} L_{ik} \mathcal D_{a}\!\left(L^{jk}\right) T_{bc} T_{de} \bar\varphi^{i} \gamma^{a} \gamma^{bc} \gamma^{de} \varphi_{j} - \frac{4}{L^{6}} L_{ik} L^{j}{}_{l} \mathcal D_{a}\!\left(L^{lk}\right) T_{bc} \bar\varphi^{i} \gamma^{a} \gamma^{bc} \left(i \gamma^{d} E_{d} +N\right) \varphi_{j}\\
&- \frac{4 i}{L^{6}} L_{ik} L^{j}{}_{l} \mathcal D_{a}\!\left(L_{m}{}^{k}\right) \mathcal D_{d}\!\left(L^{ml}\right) T_{bc} \bar\varphi^{i} \gamma^{a} \gamma^{bc} \gamma^{d} \varphi_{j}
\end{aligned}
\tag{I.4}
```

**Source contribution 5,33.**

```math
\begin{aligned}
-16i\rho'\bar\lambda'{}^i\chi_i={}&\frac{64 N}{L^{2}} \mathcal D_{a}\!\left(\bar\varphi_{i}\right) \gamma^{a} \chi^{i} - \frac{512 i N}{L^{2}} L_{i}{}^{j} \bar\chi^{i} \chi_{j} +\frac{128 i N}{L^{2}} T_{ab} \bar\varphi^{i} \gamma^{ab} \chi_{i} +\frac{64 i N}{L^{4}} L_{i}{}^{j} \bar\varphi^{i} \left(i E_{a} \gamma^{a} +N\right) \chi_{j}\\
&+\frac{64 N}{L^{4}} L_{ik} \mathcal D_{a}\!\left(L^{jk}\right) \bar\varphi^{i} \gamma^{a} \chi_{j}
\end{aligned}
\tag{I.5}
```

**Source contribution 6.**

```math
\begin{aligned}
-\frac i8\bar\lambda'{}^i\gamma\!\cdot\!\widehat G\lambda'_i={}&- \frac{i}{2 L^{2}} \widehat G_{bc} \mathcal D_{a}\!\left(\bar\varphi_{i}\right) \gamma^{a} \gamma^{bc} \gamma^{d} \mathcal D_{d}\!\left(\varphi^{i}\right) - \frac{4}{L^{2}} \widehat G_{bc} L^{ij} \mathcal D_{a}\!\left(\bar\varphi_{i}\right) \gamma^{a} \gamma^{bc} \chi_{j} +\frac{1}{L^{2}} \widehat G_{bc} T_{de} \mathcal D_{a}\!\left(\bar\varphi_{i}\right) \gamma^{a} \gamma^{bc} \gamma^{de} \varphi^{i} +\frac{1}{2 L^{4}} \widehat G_{bc} L^{ij} \mathcal D_{a}\!\left(\bar\varphi_{i}\right) \gamma^{a} \gamma^{bc} \left(i \gamma^{d} E_{d} +N\right) \varphi_{j}\\
&- \frac{i}{2 L^{4}} \widehat G_{bc} L^{j}{}_{k} \mathcal D_{d}\!\left(L^{ik}\right) \mathcal D_{a}\!\left(\bar\varphi_{i}\right) \gamma^{a} \gamma^{bc} \gamma^{d} \varphi_{j} - \frac{4}{L^{2}} \widehat G_{ab} L_{i}{}^{j} \bar\chi^{i} \gamma^{ab} \gamma^{c} \mathcal D_{c}\!\left(\varphi_{j}\right) - 16 i \widehat G_{ab} \bar\chi^{i} \gamma^{ab} \chi_{i} - \frac{8 i}{L^{2}} \widehat G_{ab} L_{i}{}^{j} T_{cd} \bar\chi^{i} \gamma^{ab} \gamma^{cd} \varphi_{j}\\
&+\frac{2 i}{L^{2}} \widehat G_{ab} \bar\chi^{i} \gamma^{ab} \left(i \gamma^{c} E_{c} +N\right) \varphi_{i} +\frac{4}{L^{4}} \widehat G_{ab} L_{ik} L^{j}{}_{l} \mathcal D_{c}\!\left(L^{kl}\right) \bar\chi^{i} \gamma^{ab} \gamma^{c} \varphi_{j} +\frac{1}{L^{2}} \widehat G_{cd} T_{ab} \bar\varphi^{i} \gamma^{ab} \gamma^{cd} \gamma^{e} \mathcal D_{e}\!\left(\varphi_{i}\right) - \frac{8 i}{L^{2}} \widehat G_{cd} L_{i}{}^{j} T_{ab} \bar\varphi^{i} \gamma^{ab} \gamma^{cd} \chi_{j}\\
&+\frac{2 i}{L^{2}} \widehat G_{cd} T_{ab} T_{ef} \bar\varphi^{i} \gamma^{ab} \gamma^{cd} \gamma^{ef} \varphi_{i} +\frac{i}{L^{4}} \widehat G_{cd} L_{i}{}^{j} T_{ab} \bar\varphi^{i} \gamma^{ab} \gamma^{cd} \left(i \gamma^{e} E_{e} +N\right) \varphi_{j} +\frac{1}{L^{4}} \widehat G_{cd} L^{j}{}_{k} \mathcal D_{e}\!\left(L_{i}{}^{k}\right) T_{ab} \bar\varphi^{i} \gamma^{ab} \gamma^{cd} \gamma^{e} \varphi_{j} +\frac{1}{2 L^{4}} \widehat G_{ab} L_{i}{}^{j} \bar\varphi^{i} \left(i E_{d} \gamma^{d} +N\right) \gamma^{ab} \gamma^{c} \mathcal D_{c}\!\left(\varphi_{j}\right)\\
&+\frac{2 i}{L^{2}} \widehat G_{ab} \bar\varphi^{i} \left(i E_{c} \gamma^{c} +N\right) \gamma^{ab} \chi_{i} +\frac{i}{L^{4}} \widehat G_{ab} L_{i}{}^{j} T_{cd} \bar\varphi^{i} \left(i E_{e} \gamma^{e} +N\right) \gamma^{ab} \gamma^{cd} \varphi_{j} - \frac{i}{4 L^{4}} \widehat G_{ab} \bar\varphi^{i} \left(i E_{c} \gamma^{c} +N\right) \gamma^{ab} \left(i \gamma^{d} E_{d} +N\right) \varphi_{i} - \frac{1}{2 L^{6}} \widehat G_{ab} L_{ik} L^{j}{}_{l} \mathcal D_{c}\!\left(L^{kl}\right) \bar\varphi^{i} \left(i E_{d} \gamma^{d} +N\right) \gamma^{ab} \gamma^{c} \varphi_{j}\\
&- \frac{i}{2 L^{4}} \widehat G_{bc} L_{ik} \mathcal D_{a}\!\left(L^{jk}\right) \bar\varphi^{i} \gamma^{a} \gamma^{bc} \gamma^{d} \mathcal D_{d}\!\left(\varphi_{j}\right) - \frac{4}{L^{4}} \widehat G_{bc} L_{ik} L^{j}{}_{l} \mathcal D_{a}\!\left(L^{lk}\right) \bar\varphi^{i} \gamma^{a} \gamma^{bc} \chi_{j} +\frac{1}{L^{4}} \widehat G_{bc} L_{ik} \mathcal D_{a}\!\left(L^{jk}\right) T_{de} \bar\varphi^{i} \gamma^{a} \gamma^{bc} \gamma^{de} \varphi_{j} +\frac{1}{2 L^{6}} \widehat G_{bc} L_{ik} L^{j}{}_{l} \mathcal D_{a}\!\left(L^{lk}\right) \bar\varphi^{i} \gamma^{a} \gamma^{bc} \left(i \gamma^{d} E_{d} +N\right) \varphi_{j}\\
&+\frac{i}{2 L^{6}} \widehat G_{bc} L_{ik} L^{j}{}_{l} \mathcal D_{a}\!\left(L_{m}{}^{k}\right) \mathcal D_{d}\!\left(L^{ml}\right) \bar\varphi^{i} \gamma^{a} \gamma^{bc} \gamma^{d} \varphi_{j}
\end{aligned}
\tag{I.6}
```

**Source contribution 7.**

```math
\begin{aligned}
\frac{ig}4\bar\lambda'{}^iL_{ij}\lambda'{}^j={}&- \frac{i g}{L^{2}} L^{ij} \mathcal D_{a}\!\left(\bar\varphi_{i}\right) \gamma^{a} \gamma^{b} \mathcal D_{b}\!\left(\varphi_{j}\right) +4 g \mathcal D_{a}\!\left(\bar\varphi_{i}\right) \gamma^{a} \chi^{i} +\frac{2 g}{L^{2}} L^{ij} T_{bc} \mathcal D_{a}\!\left(\bar\varphi_{i}\right) \gamma^{a} \gamma^{bc} \varphi_{j} - \frac{g}{2 L^{2}} \mathcal D_{a}\!\left(\bar\varphi_{i}\right) \gamma^{a} \left(i \gamma^{b} E_{b} +N\right) \varphi^{i}\\
&+\frac{i g}{L^{4}} L^{i}{}_{k} L^{j}{}_{l} \mathcal D_{b}\!\left(L^{kl}\right) \mathcal D_{a}\!\left(\bar\varphi_{i}\right) \gamma^{a} \gamma^{b} \varphi_{j} +4 g \bar\chi^{i} \gamma^{a} \mathcal D_{a}\!\left(\varphi_{i}\right) - 32 i g L_{i}{}^{j} \bar\chi^{i} \chi_{j} +8 i g T_{ab} \bar\chi^{i} \gamma^{ab} \varphi_{i}\\
&+\frac{4 i g}{L^{2}} L_{i}{}^{j} \bar\chi^{i} \left(i \gamma^{a} E_{a} +N\right) \varphi_{j} +\frac{4 g}{L^{2}} L^{j}{}_{k} \mathcal D_{a}\!\left(L_{i}{}^{k}\right) \bar\chi^{i} \gamma^{a} \varphi_{j} +\frac{2 g}{L^{2}} L_{i}{}^{j} T_{ab} \bar\varphi^{i} \gamma^{ab} \gamma^{c} \mathcal D_{c}\!\left(\varphi_{j}\right) +8 i g T_{ab} \bar\varphi^{i} \gamma^{ab} \chi_{i}\\
&+\frac{4 i g}{L^{2}} L_{i}{}^{j} T_{ab} T_{cd} \bar\varphi^{i} \gamma^{ab} \gamma^{cd} \varphi_{j} - \frac{i g}{L^{2}} T_{ab} \bar\varphi^{i} \gamma^{ab} \left(i \gamma^{c} E_{c} +N\right) \varphi_{i} - \frac{2 g}{L^{4}} L_{ik} L^{j}{}_{l} \mathcal D_{c}\!\left(L^{kl}\right) T_{ab} \bar\varphi^{i} \gamma^{ab} \gamma^{c} \varphi_{j} - \frac{g}{2 L^{2}} \bar\varphi^{i} \left(i E_{b} \gamma^{b} +N\right) \gamma^{a} \mathcal D_{a}\!\left(\varphi_{i}\right)\\
&+\frac{4 i g}{L^{2}} L_{i}{}^{j} \bar\varphi^{i} \left(i E_{a} \gamma^{a} +N\right) \chi_{j} - \frac{i g}{L^{2}} T_{ab} \bar\varphi^{i} \left(i E_{c} \gamma^{c} +N\right) \gamma^{ab} \varphi_{i} - \frac{i g}{2 L^{4}} L_{i}{}^{j} \bar\varphi^{i} \left(i E_{a} \gamma^{a} +N\right) \left(i \gamma^{b} E_{b} +N\right) \varphi_{j} - \frac{g}{2 L^{4}} L^{j}{}_{k} \mathcal D_{a}\!\left(L_{i}{}^{k}\right) \bar\varphi^{i} \left(i E_{b} \gamma^{b} +N\right) \gamma^{a} \varphi_{j}\\
&- \frac{i g}{L^{4}} L_{ik} L^{j}{}_{l} \mathcal D_{a}\!\left(L^{lk}\right) \bar\varphi^{i} \gamma^{a} \gamma^{b} \mathcal D_{b}\!\left(\varphi_{j}\right) +\frac{4 g}{L^{2}} L_{ik} \mathcal D_{a}\!\left(L^{jk}\right) \bar\varphi^{i} \gamma^{a} \chi_{j} +\frac{2 g}{L^{4}} L_{ik} L^{j}{}_{l} \mathcal D_{a}\!\left(L^{lk}\right) T_{bc} \bar\varphi^{i} \gamma^{a} \gamma^{bc} \varphi_{j} - \frac{g}{2 L^{4}} L_{ik} \mathcal D_{a}\!\left(L^{jk}\right) \bar\varphi^{i} \gamma^{a} \left(i \gamma^{b} E_{b} +N\right) \varphi_{j}\\
&+\frac{i g}{L^{6}} L_{ik} L^{j}{}_{l} L_{mn} \mathcal D_{a}\!\left(L^{mk}\right) \mathcal D_{b}\!\left(L^{nl}\right) \bar\varphi^{i} \gamma^{a} \gamma^{b} \varphi_{j}
\end{aligned}
\tag{I.7}
```

**Source contribution 8.**

```math
\begin{aligned}
\frac g4\rho'\bar\psi_a{}^i\gamma^a\lambda'{}^jL_{ij}={}&\frac{i N g}{L^{2}} L_{i}{}^{j} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{b} \mathcal D_{b}\!\left(\varphi_{j}\right) - 4 N g \bar\psi_{a}{}^{i} \gamma^{a} \chi_{i} - \frac{2 N g}{L^{2}} L_{i}{}^{j} T_{bc} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{bc} \varphi_{j} +\frac{N g}{2 L^{2}} \bar\psi_{a}{}^{i} \gamma^{a} \left(i \gamma^{b} E_{b} +N\right) \varphi_{i}\\
&- \frac{i N g}{L^{4}} L_{ik} L^{j}{}_{l} \mathcal D_{b}\!\left(L^{kl}\right) \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{b} \varphi_{j}
\end{aligned}
\tag{I.8}
```

**Source contribution 9.**

```math
\begin{aligned}
-\frac12\bar\psi_a{}^i\gamma^a\lambda'{}^jY'_{ij}={}&- \frac{i}{L^{2}} \Box_c\!\left(L_{i}{}^{j}\right) \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{b} \mathcal D_{b}\!\left(\varphi_{j}\right) +\frac{i}{L^{3}} \mathcal D_{c}\!\left(L\right) \mathcal D^{c}\!\left(L_{i}{}^{j}\right) \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{b} \mathcal D_{b}\!\left(\varphi_{j}\right) - \frac{i}{L^{2}} \left(4 D +\frac{8}{3} T_{cd} T^{cd} - \frac{1}{L^{2}} E_{c} E^{c} - \frac{N^{2}}{L^{2}} +\frac{1}{2 L^{2}} \mathcal D_{c}\!\left(L_{kl}\right) \mathcal D^{c}\!\left(L^{kl}\right)\right) L_{i}{}^{j} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{b} \mathcal D_{b}\!\left(\varphi_{j}\right) - \frac{2 i}{L^{4}} E_{c} \varepsilon^{jk}\left(L_{l(i} \mathcal D^{c}\!\left(L_{k)}{}^{l}\right)\right) \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{b} \mathcal D_{b}\!\left(\varphi_{j}\right)\\
&- \frac{8}{L^{2}} L^{j}{}_{k} \Box_c\!\left(L_{i}{}^{k}\right) \bar\psi_{a}{}^{i} \gamma^{a} \chi_{j} +\frac{8}{L^{3}} L^{j}{}_{k} \mathcal D_{b}\!\left(L\right) \mathcal D^{b}\!\left(L_{i}{}^{k}\right) \bar\psi_{a}{}^{i} \gamma^{a} \chi_{j} +4 \left(4 D +\frac{8}{3} T_{bc} T^{bc} - \frac{1}{L^{2}} E_{b} E^{b} - \frac{N^{2}}{L^{2}} +\frac{1}{2 L^{2}} \mathcal D_{b}\!\left(L_{jk}\right) \mathcal D^{b}\!\left(L^{jk}\right)\right) \bar\psi_{a}{}^{i} \gamma^{a} \chi_{i} +\frac{16}{L^{4}} E_{b} \left(L_{l(i} \mathcal D^{b}\!\left(L_{k)}{}^{l}\right)\right) L^{jk} \bar\psi_{a}{}^{i} \gamma^{a} \chi_{j}\\
&+\frac{2}{L^{2}} \Box_c\!\left(L_{i}{}^{j}\right) T_{bc} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{bc} \varphi_{j} - \frac{2}{L^{3}} \mathcal D_{d}\!\left(L\right) \mathcal D^{d}\!\left(L_{i}{}^{j}\right) T_{bc} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{bc} \varphi_{j} +\frac{2}{L^{2}} \left(4 D +\frac{8}{3} T_{de} T^{de} - \frac{1}{L^{2}} E_{d} E^{d} - \frac{N^{2}}{L^{2}} +\frac{1}{2 L^{2}} \mathcal D_{d}\!\left(L_{kl}\right) \mathcal D^{d}\!\left(L^{kl}\right)\right) L_{i}{}^{j} T_{bc} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{bc} \varphi_{j} +\frac{4}{L^{4}} E_{d} \varepsilon^{jk}\left(L_{l(i} \mathcal D^{d}\!\left(L_{k)}{}^{l}\right)\right) T_{bc} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{bc} \varphi_{j}\\
&+\frac{1}{L^{4}} L^{j}{}_{k} \Box_c\!\left(L_{i}{}^{k}\right) \bar\psi_{a}{}^{i} \gamma^{a} \left(i \gamma^{b} E_{b} +N\right) \varphi_{j} - \frac{1}{L^{5}} L^{j}{}_{k} \mathcal D_{b}\!\left(L\right) \mathcal D^{b}\!\left(L_{i}{}^{k}\right) \bar\psi_{a}{}^{i} \gamma^{a} \left(i \gamma^{c} E_{c} +N\right) \varphi_{j} - \frac{1}{2 L^{2}} \left(4 D +\frac{8}{3} T_{bc} T^{bc} - \frac{1}{L^{2}} E_{b} E^{b} - \frac{N^{2}}{L^{2}} +\frac{1}{2 L^{2}} \mathcal D_{b}\!\left(L_{jk}\right) \mathcal D^{b}\!\left(L^{jk}\right)\right) \bar\psi_{a}{}^{i} \gamma^{a} \left(i \gamma^{d} E_{d} +N\right) \varphi_{i} - \frac{2}{L^{6}} E_{b} \left(L_{l(i} \mathcal D^{b}\!\left(L_{k)}{}^{l}\right)\right) L^{jk} \bar\psi_{a}{}^{i} \gamma^{a} \left(i \gamma^{c} E_{c} +N\right) \varphi_{j}\\
&+\frac{i}{L^{4}} L^{j}{}_{k} \Box_c\!\left(L_{il}\right) \mathcal D_{b}\!\left(L^{lk}\right) \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{b} \varphi_{j} +\frac{i}{L^{5}} L^{j}{}_{k} \mathcal D_{c}\!\left(L\right) \mathcal D_{b}\!\left(L_{l}{}^{k}\right) \mathcal D^{c}\!\left(L_{i}{}^{l}\right) \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{b} \varphi_{j} +\frac{i}{L^{4}} \left(4 D +\frac{8}{3} T_{cd} T^{cd} - \frac{1}{L^{2}} E_{c} E^{c} - \frac{N^{2}}{L^{2}} +\frac{1}{2 L^{2}} \mathcal D_{c}\!\left(L_{mn}\right) \mathcal D^{c}\!\left(L^{mn}\right)\right) L_{ik} L^{j}{}_{l} \mathcal D_{b}\!\left(L^{kl}\right) \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{b} \varphi_{j} +\frac{2 i}{L^{6}} E_{c} \left(L_{m(i} \mathcal D^{c}\!\left(L_{k)}{}^{m}\right)\right) L^{j}{}_{l} \mathcal D_{b}\!\left(L^{kl}\right) \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{b} \varphi_{j}
\end{aligned}
\tag{I.9}
```

**Source contribution 10.**

```math
\begin{aligned}
-\frac{3\rho'}4\bar\lambda'{}^i\gamma^a [\frac14\gamma\!\cdot\!\widehat G\psi_{ai} -\gamma\!\cdot\!T\psi_{ai}+\frac g2L_{ij}\psi_a{}^j-\phi_{ai}]={}&- \frac{3 i N}{4 L^{2}} \widehat G_{cd} \mathcal D_{a}\!\left(\bar\varphi_{i}\right) \gamma^{a} \gamma^{b} \gamma^{cd} \psi_{b}{}^{i} - \frac{6 N}{L^{2}} \widehat G_{bc} L_{i}{}^{j} \bar\chi^{i} \gamma^{a} \gamma^{bc} \psi_{aj} +\frac{3 N}{2 L^{2}} \widehat G_{de} T_{ab} \bar\varphi^{i} \gamma^{ab} \gamma^{c} \gamma^{de} \psi_{ci} +\frac{3 N}{4 L^{4}} \widehat G_{bc} L_{i}{}^{j} \bar\varphi^{i} \left(i E_{d} \gamma^{d} +N\right) \gamma^{a} \gamma^{bc} \psi_{aj}\\
&- \frac{3 i N}{4 L^{4}} \widehat G_{cd} L_{ik} \mathcal D_{a}\!\left(L^{jk}\right) \bar\varphi^{i} \gamma^{a} \gamma^{b} \gamma^{cd} \psi_{bj} +\frac{3 i N}{L^{2}} T_{cd} \mathcal D_{a}\!\left(\bar\varphi_{i}\right) \gamma^{a} \gamma^{b} \gamma^{cd} \psi_{b}{}^{i} +\frac{24 N}{L^{2}} L_{i}{}^{j} T_{bc} \bar\chi^{i} \gamma^{a} \gamma^{bc} \psi_{aj} - \frac{6 N}{L^{2}} T_{ab} T_{de} \bar\varphi^{i} \gamma^{ab} \gamma^{c} \gamma^{de} \psi_{ci}\\
&- \frac{3 N}{L^{4}} L_{i}{}^{j} T_{bc} \bar\varphi^{i} \left(i E_{d} \gamma^{d} +N\right) \gamma^{a} \gamma^{bc} \psi_{aj} +\frac{3 i N}{L^{4}} L_{ik} \mathcal D_{a}\!\left(L^{jk}\right) T_{cd} \bar\varphi^{i} \gamma^{a} \gamma^{b} \gamma^{cd} \psi_{bj} +\frac{3 i N g}{2 L^{2}} L^{ij} \mathcal D_{a}\!\left(\bar\varphi_{i}\right) \gamma^{a} \gamma^{b} \psi_{bj} - 6 N g \bar\chi^{i} \gamma^{a} \psi_{ai}\\
&- \frac{3 N g}{L^{2}} L_{i}{}^{j} T_{ab} \bar\varphi^{i} \gamma^{ab} \gamma^{c} \psi_{cj} +\frac{3 N g}{4 L^{2}} \bar\varphi^{i} \left(i E_{b} \gamma^{b} +N\right) \gamma^{a} \psi_{ai} +\frac{3 i N g}{2 L^{4}} L_{ik} L^{j}{}_{l} \mathcal D_{a}\!\left(L^{lk}\right) \bar\varphi^{i} \gamma^{a} \gamma^{b} \psi_{bj} +\frac{3 i N}{L^{2}} \mathcal D_{a}\!\left(\bar\varphi_{i}\right) \gamma^{a} \gamma^{b} \phi_{b}{}^{i}\\
&+\frac{24 N}{L^{2}} L_{i}{}^{j} \bar\chi^{i} \gamma^{a} \phi_{aj} - \frac{6 N}{L^{2}} T_{ab} \bar\varphi^{i} \gamma^{ab} \gamma^{c} \phi_{ci} - \frac{3 N}{L^{4}} L_{i}{}^{j} \bar\varphi^{i} \left(i E_{b} \gamma^{b} +N\right) \gamma^{a} \phi_{aj} +\frac{3 i N}{L^{4}} L_{ik} \mathcal D_{a}\!\left(L^{jk}\right) \bar\varphi^{i} \gamma^{a} \gamma^{b} \phi_{bj}
\end{aligned}
\tag{I.10}
```

**Source contribution 11,12,13,14,15.**

```math
\begin{aligned}
-\frac12A'_a\mathcal D_b\!\left[\widehat F'^{ab}+\rho'(\widehat G^{ab}-16T^{ab})\right]={}&- \frac{1}{L} E_{a} \mathcal D_{b}\!\left(\left(4 \left(\mathcal D^{[a}\!\left(\frac{1}{L} E^{b]}\right)\right) +\frac{2}{L} L_{ij} \widehat R(V)^{abij} - \frac{2}{L^{3}} L_{i}{}^{j} \left(\mathcal D^{[a}\!\left(L^{ik}\right) \mathcal D^{b]}\!\left(L_{jk}\right)\right) +\frac{2 N}{L} \left(\widehat G^{ab} -16 T^{ab}\right)\right)\right) - \frac{1}{L} E^{b} \mathcal D_{a}\!\left(\left(-2 \eta^{ac}\left(\mathcal D_{[b}\!\left(\frac{1}{L^{3}} L_{mn} \bar\varphi^{m} \gamma_{c]} \varphi^{n}\right)\right) - \frac{i}{L} \bar\varphi^{i} \widehat R(Q)_{b}{}^{a}{}_{i} +\frac{i}{L^{3}} L_{ij} \bar\varphi^{i} \varphi^{j} \left(\widehat G_{b}{}^{a} -16 T_{b}{}^{a}\right)\right)\right) - \frac{\sqrt{2}}{2} \mathcal D_{a}\!\left(\left(4 \eta^{ac}\left(\mathcal D_{[b}\!\left(\frac{1}{L} E_{c]}\right)\right) +\frac{2}{L} L_{ij} \widehat R(V)_{b}{}^{aij} - \frac{2}{L^{3}} L_{i}{}^{j} \eta^{ad}\left(\mathcal D_{[b}\!\left(L^{ik}\right) \mathcal D_{d]}\!\left(L_{jk}\right)\right) +\frac{2 N}{L} \left(\widehat G_{b}{}^{a} -16 T_{b}{}^{a}\right)\right)\right) V^{b} - \frac{\sqrt{2}}{2} V^{b} \mathcal D_{a}\!\left(\left(-2 \eta^{ac}\left(\mathcal D_{[b}\!\left(\frac{1}{L^{3}} L_{mn} \bar\varphi^{m} \gamma_{c]} \varphi^{n}\right)\right) - \frac{i}{L} \bar\varphi^{i} \widehat R(Q)_{b}{}^{a}{}_{i} +\frac{i}{L^{3}} L_{ij} \bar\varphi^{i} \varphi^{j} \left(\widehat G_{b}{}^{a} -16 T_{b}{}^{a}\right)\right)\right)\\
&- \frac{1}{2 L^{3}} L_{i}{}^{j} \mathcal D_{b}\!\left(\left(4 \eta^{bc}\left(\mathcal D_{[a}\!\left(\frac{1}{L} E_{c]}\right)\right) +\frac{2}{L} L_{kl} \widehat R(V)_{a}{}^{bkl} - \frac{2}{L^{3}} L_{k}{}^{l} \eta^{bd}\left(\mathcal D_{[a}\!\left(L^{km}\right) \mathcal D_{d]}\!\left(L_{lm}\right)\right) +\frac{2 N}{L} \left(\widehat G_{a}{}^{b} -16 T_{a}{}^{b}\right)\right)\right) \bar\varphi^{i} \gamma^{a} \varphi_{j} +\frac{i}{2 L} \mathcal D_{b}\!\left(\left(4 \left(\mathcal D^{[a}\!\left(\frac{1}{L} E^{b]}\right)\right) +\frac{2}{L} L_{jk} \widehat R(V)^{abjk} - \frac{2}{L^{3}} L_{j}{}^{k} \left(\mathcal D^{[a}\!\left(L^{jl}\right) \mathcal D^{b]}\!\left(L_{kl}\right)\right) +\frac{2 N}{L} \left(\widehat G^{ab} -16 T^{ab}\right)\right)\right) \bar\varphi^{i} \psi_{ai}
\end{aligned}
\tag{I.11}
```

**Source contribution 16.**

```math
\begin{aligned}
-\frac18A'_a\varepsilon^{abcde}\widehat F'_{bc}\widehat G_{de}={}&- \frac{1}{L} E_{a} \widehat G_{bc} \left(\mathcal D_{[d}\!\left(\frac{1}{L} E_{e]}\right)\right) \varepsilon^{abcde} - \frac{1}{2 L^{2}} E_{a} \widehat G_{bc} L_{ij} \widehat R(V)_{de}{}^{ij} \varepsilon^{abcde} - \frac{1}{2 L^{4}} E_{a} \widehat G_{bc} \left(\mathcal D_{[d}\!\left(L_{i}{}^{k}\right) \mathcal D_{e]}\!\left(L_{jk}\right)\right) L^{ij} \varepsilon^{abcde} +\frac{1}{2 L} E_{c} \widehat G_{de} \varepsilon^{abcde} \left(\mathcal D_{[a}\!\left(\frac{1}{L^{3}} L_{kl} \bar\varphi^{k} \gamma_{b]} \varphi^{l}\right)\right)\\
&+\frac{i}{4 L^{2}} E_{c} \widehat G_{de} \varepsilon^{abcde} \bar\varphi^{i} \widehat R(Q)_{abi} - \frac{\sqrt{2}}{2} \widehat G_{ab} \left(\mathcal D_{[c}\!\left(\frac{1}{L} E_{d]}\right)\right) V_{e} \varepsilon^{abcde} - \frac{\sqrt{2}}{4 L} \widehat G_{ab} L_{ij} \widehat R(V)_{cd}{}^{ij} V_{e} \varepsilon^{abcde} - \frac{\sqrt{2}}{4 L^{3}} \widehat G_{ab} \left(\mathcal D_{[c}\!\left(L_{i}{}^{k}\right) \mathcal D_{d]}\!\left(L_{jk}\right)\right) L^{ij} V_{e} \varepsilon^{abcde}\\
&+\frac{\sqrt{2}}{4} \widehat G_{cd} V_{e} \varepsilon^{abcde} \left(\mathcal D_{[a}\!\left(\frac{1}{L^{3}} L_{kl} \bar\varphi^{k} \gamma_{b]} \varphi^{l}\right)\right) +\frac{\sqrt{2} i}{8 L} \widehat G_{cd} V_{e} \varepsilon^{abcde} \bar\varphi^{i} \widehat R(Q)_{abi} - \frac{1}{2 L^{3}} \widehat G_{bc} \left(\mathcal D_{[d}\!\left(\frac{1}{L} E_{e]}\right)\right) L_{i}{}^{j} \varepsilon_{a}{}^{bcde} \bar\varphi^{i} \gamma^{a} \varphi_{j} - \frac{1}{4 L^{4}} \widehat G_{bc} L_{i}{}^{j} L_{kl} \widehat R(V)_{de}{}^{kl} \varepsilon_{a}{}^{bcde} \bar\varphi^{i} \gamma^{a} \varphi_{j}\\
&- \frac{1}{4 L^{6}} \widehat G_{bc} \left(\mathcal D_{[d}\!\left(L_{k}{}^{m}\right) \mathcal D_{e]}\!\left(L_{lm}\right)\right) L_{i}{}^{j} L^{kl} \varepsilon_{a}{}^{bcde} \bar\varphi^{i} \gamma^{a} \varphi_{j} +\frac{i}{2 L} \widehat G_{bc} \left(\mathcal D_{[d}\!\left(\frac{1}{L} E_{e]}\right)\right) \varepsilon^{abcde} \bar\varphi^{i} \psi_{ai} +\frac{i}{4 L^{2}} \widehat G_{bc} L_{jk} \widehat R(V)_{de}{}^{jk} \varepsilon^{abcde} \bar\varphi^{i} \psi_{ai} +\frac{i}{4 L^{4}} \widehat G_{bc} \left(\mathcal D_{[d}\!\left(L_{j}{}^{l}\right) \mathcal D_{e]}\!\left(L_{kl}\right)\right) L^{jk} \varepsilon^{abcde} \bar\varphi^{i} \psi_{ai}
\end{aligned}
\tag{I.16}
```

**Source contribution 17.**

```math
\begin{aligned}
-\frac i4A'_a\bar\lambda'{}^i\gamma^{ab} [\frac14\gamma\!\cdot\!\widehat G\psi_{bi} -\gamma\!\cdot\!T\psi_{bi}+\frac g2L_{ij}\psi_b{}^j-\phi_{bi}]={}&\frac{1}{4 L^{2}} E_{b} \widehat G_{de} \mathcal D_{a}\!\left(\bar\varphi_{i}\right) \gamma^{a} \gamma^{bc} \gamma^{de} \psi_{c}{}^{i} - \frac{2 i}{L^{2}} E_{a} \widehat G_{cd} L_{i}{}^{j} \bar\chi^{i} \gamma^{ab} \gamma^{cd} \psi_{bj} +\frac{i}{2 L^{2}} E_{c} \widehat G_{ef} T_{ab} \bar\varphi^{i} \gamma^{ab} \gamma^{cd} \gamma^{ef} \psi_{di} +\frac{i}{4 L^{4}} E_{a} \widehat G_{cd} L_{i}{}^{j} \bar\varphi^{i} \left(i E_{e} \gamma^{e} +N\right) \gamma^{ab} \gamma^{cd} \psi_{bj}\\
&+\frac{1}{4 L^{4}} E_{b} \widehat G_{de} L_{ik} \mathcal D_{a}\!\left(L^{jk}\right) \bar\varphi^{i} \gamma^{a} \gamma^{bc} \gamma^{de} \psi_{cj} +\frac{\sqrt{2}}{8 L} \widehat G_{de} V_{b} \mathcal D_{a}\!\left(\bar\varphi_{i}\right) \gamma^{a} \gamma^{bc} \gamma^{de} \psi_{c}{}^{i} - \frac{\sqrt{2} i}{L} \widehat G_{cd} L_{i}{}^{j} V_{a} \bar\chi^{i} \gamma^{ab} \gamma^{cd} \psi_{bj} +\frac{\sqrt{2} i}{4 L} \widehat G_{ef} T_{ab} V_{c} \bar\varphi^{i} \gamma^{ab} \gamma^{cd} \gamma^{ef} \psi_{di}\\
&+\frac{\sqrt{2} i}{8 L^{3}} \widehat G_{cd} L_{i}{}^{j} V_{a} \bar\varphi^{i} \left(i E_{e} \gamma^{e} +N\right) \gamma^{ab} \gamma^{cd} \psi_{bj} +\frac{\sqrt{2}}{8 L^{3}} \widehat G_{de} L_{ik} \mathcal D_{a}\!\left(L^{jk}\right) V_{b} \bar\varphi^{i} \gamma^{a} \gamma^{bc} \gamma^{de} \psi_{cj} - \frac{1}{L^{2}} E_{b} T_{de} \mathcal D_{a}\!\left(\bar\varphi_{i}\right) \gamma^{a} \gamma^{bc} \gamma^{de} \psi_{c}{}^{i} +\frac{8 i}{L^{2}} E_{a} L_{i}{}^{j} T_{cd} \bar\chi^{i} \gamma^{ab} \gamma^{cd} \psi_{bj}\\
&- \frac{2 i}{L^{2}} E_{c} T_{ab} T_{ef} \bar\varphi^{i} \gamma^{ab} \gamma^{cd} \gamma^{ef} \psi_{di} - \frac{i}{L^{4}} E_{a} L_{i}{}^{j} T_{cd} \bar\varphi^{i} \left(i E_{e} \gamma^{e} +N\right) \gamma^{ab} \gamma^{cd} \psi_{bj} - \frac{1}{L^{4}} E_{b} L_{ik} \mathcal D_{a}\!\left(L^{jk}\right) T_{de} \bar\varphi^{i} \gamma^{a} \gamma^{bc} \gamma^{de} \psi_{cj} - \frac{\sqrt{2}}{2 L} T_{de} V_{b} \mathcal D_{a}\!\left(\bar\varphi_{i}\right) \gamma^{a} \gamma^{bc} \gamma^{de} \psi_{c}{}^{i}\\
&+\frac{4 \sqrt{2} i}{L} L_{i}{}^{j} T_{cd} V_{a} \bar\chi^{i} \gamma^{ab} \gamma^{cd} \psi_{bj} - \frac{\sqrt{2} i}{L} T_{ab} T_{ef} V_{c} \bar\varphi^{i} \gamma^{ab} \gamma^{cd} \gamma^{ef} \psi_{di} - \frac{\sqrt{2} i}{2 L^{3}} L_{i}{}^{j} T_{cd} V_{a} \bar\varphi^{i} \left(i E_{e} \gamma^{e} +N\right) \gamma^{ab} \gamma^{cd} \psi_{bj} - \frac{\sqrt{2}}{2 L^{3}} L_{ik} \mathcal D_{a}\!\left(L^{jk}\right) T_{de} V_{b} \bar\varphi^{i} \gamma^{a} \gamma^{bc} \gamma^{de} \psi_{cj}\\
&- \frac{g}{2 L^{2}} E_{b} L^{ij} \mathcal D_{a}\!\left(\bar\varphi_{i}\right) \gamma^{a} \gamma^{bc} \psi_{cj} - 2 i g E_{a} \bar\chi^{i} \gamma^{ab} \psi_{bi} - \frac{i g}{L^{2}} E_{c} L_{i}{}^{j} T_{ab} \bar\varphi^{i} \gamma^{ab} \gamma^{cd} \psi_{dj} +\frac{i g}{4 L^{2}} E_{a} \bar\varphi^{i} \left(i E_{c} \gamma^{c} +N\right) \gamma^{ab} \psi_{bi}\\
&- \frac{g}{2 L^{4}} E_{b} L_{ik} L^{j}{}_{l} \mathcal D_{a}\!\left(L^{lk}\right) \bar\varphi^{i} \gamma^{a} \gamma^{bc} \psi_{cj} - \frac{\sqrt{2} g}{4 L} L^{ij} V_{b} \mathcal D_{a}\!\left(\bar\varphi_{i}\right) \gamma^{a} \gamma^{bc} \psi_{cj} - \sqrt{2} i L g V_{a} \bar\chi^{i} \gamma^{ab} \psi_{bi} - \frac{\sqrt{2} i g}{2 L} L_{i}{}^{j} T_{ab} V_{c} \bar\varphi^{i} \gamma^{ab} \gamma^{cd} \psi_{dj}\\
&+\frac{\sqrt{2} i g}{8 L} V_{a} \bar\varphi^{i} \left(i E_{c} \gamma^{c} +N\right) \gamma^{ab} \psi_{bi} - \frac{\sqrt{2} g}{4 L^{3}} L_{ik} L^{j}{}_{l} \mathcal D_{a}\!\left(L^{lk}\right) V_{b} \bar\varphi^{i} \gamma^{a} \gamma^{bc} \psi_{cj} - \frac{1}{L^{2}} E_{b} \mathcal D_{a}\!\left(\bar\varphi_{i}\right) \gamma^{a} \gamma^{bc} \phi_{c}{}^{i} +\frac{8 i}{L^{2}} E_{a} L_{i}{}^{j} \bar\chi^{i} \gamma^{ab} \phi_{bj}\\
&- \frac{2 i}{L^{2}} E_{c} T_{ab} \bar\varphi^{i} \gamma^{ab} \gamma^{cd} \phi_{di} - \frac{i}{L^{4}} E_{a} L_{i}{}^{j} \bar\varphi^{i} \left(i E_{c} \gamma^{c} +N\right) \gamma^{ab} \phi_{bj} - \frac{1}{L^{4}} E_{b} L_{ik} \mathcal D_{a}\!\left(L^{jk}\right) \bar\varphi^{i} \gamma^{a} \gamma^{bc} \phi_{cj} - \frac{\sqrt{2}}{2 L} V_{b} \mathcal D_{a}\!\left(\bar\varphi_{i}\right) \gamma^{a} \gamma^{bc} \phi_{c}{}^{i}\\
&+\frac{4 \sqrt{2} i}{L} L_{i}{}^{j} V_{a} \bar\chi^{i} \gamma^{ab} \phi_{bj} - \frac{\sqrt{2} i}{L} T_{ab} V_{c} \bar\varphi^{i} \gamma^{ab} \gamma^{cd} \phi_{di} - \frac{\sqrt{2} i}{2 L^{3}} L_{i}{}^{j} V_{a} \bar\varphi^{i} \left(i E_{c} \gamma^{c} +N\right) \gamma^{ab} \phi_{bj} - \frac{\sqrt{2}}{2 L^{3}} L_{ik} \mathcal D_{a}\!\left(L^{jk}\right) V_{b} \bar\varphi^{i} \gamma^{a} \gamma^{bc} \phi_{cj}
\end{aligned}
\tag{I.17}
```

**Source contribution 18.**

```math
\begin{aligned}
-\frac14A'_a\rho'\bar\psi_b{}^i\gamma^{ba}\gamma^c [\frac14\gamma\!\cdot\!\widehat G\psi_{ci} -\gamma\!\cdot\!T\psi_{ci}+\frac g2L_{ij}\psi_c{}^j-\phi_{ci}]={}&- \frac{N}{4 L^{2}} E_{b} \widehat G_{de} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{c} \gamma^{de} \psi_{ci} - \frac{\sqrt{2} N}{8 L} \widehat G_{de} V_{b} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{c} \gamma^{de} \psi_{ci} +\frac{N}{L^{2}} E_{b} T_{de} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{c} \gamma^{de} \psi_{ci} +\frac{\sqrt{2} N}{2 L} T_{de} V_{b} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{c} \gamma^{de} \psi_{ci}\\
&+\frac{N g}{2 L^{2}} E_{b} L_{i}{}^{j} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{c} \psi_{cj} +\frac{\sqrt{2} N g}{4 L} L_{i}{}^{j} V_{b} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{c} \psi_{cj} +\frac{N}{L^{2}} E_{b} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{c} \phi_{ci} +\frac{\sqrt{2} N}{2 L} V_{b} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{c} \phi_{ci}
\end{aligned}
\tag{I.18}
```

**Source contribution 19.**

```math
\begin{aligned}
-\frac14A'_a\bar\psi_b{}^i\gamma^{ba}\not{\mathcal D}\lambda'_i={}&\frac{i}{L} E_{b} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{c} \mathcal D_{c}\!\left(\frac{1}{L} \gamma^{d} \mathcal D_{d}\!\left(\varphi_{i}\right)\right) - \frac{8}{L} E_{b} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{c} \mathcal D_{c}\!\left(\frac{1}{L} L_{ij} \chi^{j}\right) - \frac{2}{L} E_{b} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{c} \mathcal D_{c}\!\left(\frac{1}{L} \gamma^{de} T_{de} \varphi_{i}\right) +\frac{1}{L} E_{b} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{c} \mathcal D_{c}\!\left(\frac{1}{L^{3}} L_{ij} \left(i \gamma^{d} E_{d} +N\right) \varphi^{j}\right)\\
&- \frac{i}{L} E_{b} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{c} \mathcal D_{c}\!\left(\frac{1}{L^{3}} \gamma^{d} \mathcal D_{d}\!\left(L_{ij}\right) L^{jk} \varphi_{k}\right) +\frac{\sqrt{2} i}{2} V_{b} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{c} \mathcal D_{c}\!\left(\frac{1}{L} \gamma^{d} \mathcal D_{d}\!\left(\varphi_{i}\right)\right) - 4 \sqrt{2} V_{b} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{c} \mathcal D_{c}\!\left(\frac{1}{L} L_{ij} \chi^{j}\right) - \sqrt{2} V_{b} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{c} \mathcal D_{c}\!\left(\frac{1}{L} \gamma^{de} T_{de} \varphi_{i}\right)\\
&+\frac{\sqrt{2}}{2} V_{b} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{c} \mathcal D_{c}\!\left(\frac{1}{L^{3}} L_{ij} \left(i \gamma^{d} E_{d} +N\right) \varphi^{j}\right) - \frac{\sqrt{2} i}{2} V_{b} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{c} \mathcal D_{c}\!\left(\frac{1}{L^{3}} \gamma^{d} \mathcal D_{d}\!\left(L_{ij}\right) L^{jk} \varphi_{k}\right)
\end{aligned}
\tag{I.19}
```

**Source contribution 20.**

```math
\begin{aligned}
\frac i2A'_a\bar\psi_b{}^i\gamma^{ba}\gamma\!\cdot\!T\lambda'_i={}&\frac{2}{L^{2}} E_{b} T_{cd} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{cd} \gamma^{e} \mathcal D_{e}\!\left(\varphi_{i}\right) - \frac{16 i}{L^{2}} E_{b} L_{i}{}^{j} T_{cd} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{cd} \chi_{j} +\frac{4 i}{L^{2}} E_{b} T_{cd} T_{ef} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{cd} \gamma^{ef} \varphi_{i} +\frac{2 i}{L^{4}} E_{b} L_{i}{}^{j} T_{cd} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{cd} \left(i \gamma^{e} E_{e} +N\right) \varphi_{j}\\
&+\frac{2}{L^{4}} E_{b} L^{j}{}_{k} \mathcal D_{e}\!\left(L_{i}{}^{k}\right) T_{cd} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{cd} \gamma^{e} \varphi_{j} +\frac{\sqrt{2}}{L} T_{cd} V_{b} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{cd} \gamma^{e} \mathcal D_{e}\!\left(\varphi_{i}\right) - \frac{8 \sqrt{2} i}{L} L_{i}{}^{j} T_{cd} V_{b} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{cd} \chi_{j} +\frac{2 \sqrt{2} i}{L} T_{cd} T_{ef} V_{b} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{cd} \gamma^{ef} \varphi_{i}\\
&+\frac{\sqrt{2} i}{L^{3}} L_{i}{}^{j} T_{cd} V_{b} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{cd} \left(i \gamma^{e} E_{e} +N\right) \varphi_{j} +\frac{\sqrt{2}}{L^{3}} L^{j}{}_{k} \mathcal D_{e}\!\left(L_{i}{}^{k}\right) T_{cd} V_{b} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{cd} \gamma^{e} \varphi_{j}
\end{aligned}
\tag{I.20}
```

**Source contribution 21.**

```math
\begin{aligned}
-4iA'_a\rho'\bar\psi_b{}^i\gamma^{ba}\chi_i={}&- \frac{16 i N}{L^{2}} E_{b} \bar\psi_{a}{}^{i} \gamma^{ab} \chi_{i} - \frac{8 \sqrt{2} i N}{L} V_{b} \bar\psi_{a}{}^{i} \gamma^{ab} \chi_{i}
\end{aligned}
\tag{I.21}
```

**Source contribution 22.**

```math
\begin{aligned}
-\frac i{16}A'_a\bar\psi_b{}^i\gamma^{ba}\gamma\!\cdot\!\widehat G\lambda'_i={}&- \frac{1}{4 L^{2}} E_{b} \widehat G_{cd} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{cd} \gamma^{e} \mathcal D_{e}\!\left(\varphi_{i}\right) +\frac{2 i}{L^{2}} E_{b} \widehat G_{cd} L_{i}{}^{j} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{cd} \chi_{j} - \frac{i}{2 L^{2}} E_{b} \widehat G_{cd} T_{ef} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{cd} \gamma^{ef} \varphi_{i} - \frac{i}{4 L^{4}} E_{b} \widehat G_{cd} L_{i}{}^{j} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{cd} \left(i \gamma^{e} E_{e} +N\right) \varphi_{j}\\
&- \frac{1}{4 L^{4}} E_{b} \widehat G_{cd} L^{j}{}_{k} \mathcal D_{e}\!\left(L_{i}{}^{k}\right) \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{cd} \gamma^{e} \varphi_{j} - \frac{\sqrt{2}}{8 L} \widehat G_{cd} V_{b} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{cd} \gamma^{e} \mathcal D_{e}\!\left(\varphi_{i}\right) +\frac{\sqrt{2} i}{L} \widehat G_{cd} L_{i}{}^{j} V_{b} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{cd} \chi_{j} - \frac{\sqrt{2} i}{4 L} \widehat G_{cd} T_{ef} V_{b} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{cd} \gamma^{ef} \varphi_{i}\\
&- \frac{\sqrt{2} i}{8 L^{3}} \widehat G_{cd} L_{i}{}^{j} V_{b} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{cd} \left(i \gamma^{e} E_{e} +N\right) \varphi_{j} - \frac{\sqrt{2}}{8 L^{3}} \widehat G_{cd} L^{j}{}_{k} \mathcal D_{e}\!\left(L_{i}{}^{k}\right) V_{b} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{cd} \gamma^{e} \varphi_{j}
\end{aligned}
\tag{I.22}
```

**Source contribution 23.**

```math
\begin{aligned}
\frac{ig}8A'_a\bar\psi_b{}^i\gamma^{ba}L_{ij}\lambda'{}^j={}&- \frac{g}{2 L^{2}} E_{b} L_{i}{}^{j} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{c} \mathcal D_{c}\!\left(\varphi_{j}\right) - 2 i g E_{b} \bar\psi_{a}{}^{i} \gamma^{ab} \chi_{i} - \frac{i g}{L^{2}} E_{b} L_{i}{}^{j} T_{cd} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{cd} \varphi_{j} +\frac{i g}{4 L^{2}} E_{b} \bar\psi_{a}{}^{i} \gamma^{ab} \left(i \gamma^{c} E_{c} +N\right) \varphi_{i}\\
&+\frac{g}{2 L^{4}} E_{b} L_{ik} L^{j}{}_{l} \mathcal D_{c}\!\left(L^{kl}\right) \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{c} \varphi_{j} - \frac{\sqrt{2} g}{4 L} L_{i}{}^{j} V_{b} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{c} \mathcal D_{c}\!\left(\varphi_{j}\right) - \sqrt{2} i L g V_{b} \bar\psi_{a}{}^{i} \gamma^{ab} \chi_{i} - \frac{\sqrt{2} i g}{2 L} L_{i}{}^{j} T_{cd} V_{b} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{cd} \varphi_{j}\\
&+\frac{\sqrt{2} i g}{8 L} V_{b} \bar\psi_{a}{}^{i} \gamma^{ab} \left(i \gamma^{c} E_{c} +N\right) \varphi_{i} +\frac{\sqrt{2} g}{4 L^{3}} L_{ik} L^{j}{}_{l} \mathcal D_{c}\!\left(L^{kl}\right) V_{b} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{c} \varphi_{j}
\end{aligned}
\tag{I.23}
```

**Source contribution 24.**

```math
\begin{aligned}
-\frac g8A'_a\rho'\bar\psi_b{}^i\gamma^{abc}\psi_c{}^jL_{ij}={}&- \frac{N g}{2 L^{2}} E_{b} L_{i}{}^{j} \bar\psi_{a}{}^{i} \gamma^{abc} \psi_{cj} - \frac{\sqrt{2} N g}{4 L} L_{i}{}^{j} V_{b} \bar\psi_{a}{}^{i} \gamma^{abc} \psi_{cj}
\end{aligned}
\tag{I.24}
```

**Source contribution 25.**

```math
\begin{aligned}
\frac14A'_a\bar\psi_b{}^i\gamma^{abc}\psi_c{}^jY'_{ij}={}&\frac{1}{2 L^{2}} E_{b} \Box_c\!\left(L_{i}{}^{j}\right) \bar\psi_{a}{}^{i} \gamma^{abc} \psi_{cj} - \frac{1}{2 L^{3}} E_{b} \mathcal D_{d}\!\left(L\right) \mathcal D^{d}\!\left(L_{i}{}^{j}\right) \bar\psi_{a}{}^{i} \gamma^{abc} \psi_{cj} +\frac{1}{2 L^{2}} E_{b} \left(4 D +\frac{8}{3} T_{de} T^{de} - \frac{1}{L^{2}} E_{d} E^{d} - \frac{N^{2}}{L^{2}} +\frac{1}{2 L^{2}} \mathcal D_{d}\!\left(L_{kl}\right) \mathcal D^{d}\!\left(L^{kl}\right)\right) L_{i}{}^{j} \bar\psi_{a}{}^{i} \gamma^{abc} \psi_{cj} +\frac{1}{L^{4}} E_{b} E_{d} \varepsilon^{jk}\left(L_{l(i} \mathcal D^{d}\!\left(L_{k)}{}^{l}\right)\right) \bar\psi_{a}{}^{i} \gamma^{abc} \psi_{cj}\\
&+\frac{\sqrt{2}}{4 L} \Box_c\!\left(L_{i}{}^{j}\right) V_{b} \bar\psi_{a}{}^{i} \gamma^{abc} \psi_{cj} - \frac{\sqrt{2}}{4 L^{2}} \mathcal D_{d}\!\left(L\right) \mathcal D^{d}\!\left(L_{i}{}^{j}\right) V_{b} \bar\psi_{a}{}^{i} \gamma^{abc} \psi_{cj} +\frac{\sqrt{2}}{4 L} \left(4 D +\frac{8}{3} T_{de} T^{de} - \frac{1}{L^{2}} E_{d} E^{d} - \frac{N^{2}}{L^{2}} +\frac{1}{2 L^{2}} \mathcal D_{d}\!\left(L_{kl}\right) \mathcal D^{d}\!\left(L^{kl}\right)\right) L_{i}{}^{j} V_{b} \bar\psi_{a}{}^{i} \gamma^{abc} \psi_{cj} +\frac{\sqrt{2}}{2 L^{3}} E_{d} \varepsilon^{jk}\left(L_{l(i} \mathcal D^{d}\!\left(L_{k)}{}^{l}\right)\right) V_{b} \bar\psi_{a}{}^{i} \gamma^{abc} \psi_{cj}
\end{aligned}
\tag{I.25}
```

**Source contribution 26.**

```math
\begin{aligned}
\frac12\rho'\Box_c\rho'={}&\frac{2 N}{L} \Box_c\!\left(\frac{N}{L}\right) +\frac{i N}{L} \Box_c\!\left(\frac{1}{L^{3}} L_{ij} \bar\varphi^{i} \varphi^{j}\right) - \frac{i}{L^{3}} L_{i}{}^{j} \Box_c\!\left(\frac{N}{L}\right) \bar\varphi^{i} \varphi_{j}
\end{aligned}
\tag{I.26}
```

**Source contribution 27.**

```math
\begin{aligned}
(\rho')^2 f_a{}^a={}&\frac{4 N^{2}}{L^{2}} f_{a}{}^{a} - \frac{4 i N}{L^{4}} L_{i}{}^{j} f_{a}{}^{a} \bar\varphi^{i} \varphi_{j}
\end{aligned}
\tag{I.27}
```

**Source contribution 28,30.**

```math
\begin{aligned}
-\frac14\rho'\widehat F'_{ab}(\widehat G^{ab}-16T^{ab})={}&- \frac{2 N}{L} \left(\widehat G_{ab} -16 T_{ab}\right) \left(\mathcal D^{[a}\!\left(\frac{1}{L} E^{b]}\right)\right) - \frac{N}{L^{2}} \left(\widehat G_{ab} -16 T_{ab}\right) L_{ij} \widehat R(V)^{abij} - \frac{N}{L^{4}} \left(\widehat G_{ab} -16 T_{ab}\right) \left(\mathcal D^{[a}\!\left(L_{i}{}^{k}\right) \mathcal D^{b]}\!\left(L_{jk}\right)\right) L^{ij} +\frac{N}{L} \left(\widehat G^{ab} -16 T^{ab}\right) \left(\mathcal D_{[a}\!\left(\frac{1}{L^{3}} L_{kl} \bar\varphi^{k} \gamma_{b]} \varphi^{l}\right)\right)\\
&+\frac{i N}{2 L^{2}} \left(\widehat G^{ab} -16 T^{ab}\right) \bar\varphi^{i} \widehat R(Q)_{abi} +\frac{i}{L^{3}} \left(\widehat G_{ab} -16 T_{ab}\right) \left(\mathcal D^{[a}\!\left(\frac{1}{L} E^{b]}\right)\right) L_{i}{}^{j} \bar\varphi^{i} \varphi_{j} +\frac{i}{2 L^{4}} \left(\widehat G_{ab} -16 T_{ab}\right) L_{i}{}^{j} L_{kl} \widehat R(V)^{abkl} \bar\varphi^{i} \varphi_{j} +\frac{i}{2 L^{6}} \left(\widehat G_{ab} -16 T_{ab}\right) \left(\mathcal D^{[a}\!\left(L_{k}{}^{m}\right) \mathcal D^{b]}\!\left(L_{lm}\right)\right) L_{i}{}^{j} L^{kl} \bar\varphi^{i} \varphi_{j}
\end{aligned}
\tag{I.28}
```

**Source contribution 29.**

```math
\begin{aligned}
4(\rho')^2\widehat G_{ab}T^{ab}={}&\frac{16 N^{2}}{L^{2}} \widehat G_{ab} T^{ab} - \frac{16 i N}{L^{4}} \widehat G_{ab} L_{i}{}^{j} T^{ab} \bar\varphi^{i} \varphi_{j}
\end{aligned}
\tag{I.29}
```

**Source contribution 31.**

```math
\begin{aligned}
-4(\rho')^2D={}&- \frac{16 N^{2}}{L^{2}} D +\frac{16 i N}{L^{4}} D L_{i}{}^{j} \bar\varphi^{i} \varphi_{j}
\end{aligned}
\tag{I.31}
```

**Source contribution 32.**

```math
\begin{aligned}
-\frac{104}{3}(\rho')^2T^2={}&- \frac{416 N^{2}}{3 L^{2}} T_{ab} T^{ab} +\frac{416 i N}{3 L^{4}} L_{i}{}^{j} T_{ab} T^{ab} \bar\varphi^{i} \varphi_{j}
\end{aligned}
\tag{I.32}
```

**Source contribution 34.**

```math
\begin{aligned}
-5(\rho')^2\bar\psi_a{}^i\gamma^a\chi_i={}&- \frac{20 N^{2}}{L^{2}} \bar\psi_{a}{}^{i} \gamma^{a} \chi_{i}
\end{aligned}
\tag{I.34}
```

**Source contribution 35.**

```math
\begin{aligned}
\frac i4\rho'\bar\psi_a{}^i\gamma^a\not{\mathcal D}\lambda'_i={}&\frac{N}{L} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{b} \mathcal D_{b}\!\left(\frac{1}{L} \gamma^{c} \mathcal D_{c}\!\left(\varphi_{i}\right)\right) +\frac{8 i N}{L} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{b} \mathcal D_{b}\!\left(\frac{1}{L} L_{ij} \chi^{j}\right) +\frac{2 i N}{L} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{b} \mathcal D_{b}\!\left(\frac{1}{L} \gamma^{cd} T_{cd} \varphi_{i}\right) - \frac{i N}{L} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{b} \mathcal D_{b}\!\left(\frac{1}{L^{3}} L_{ij} \left(i \gamma^{c} E_{c} +N\right) \varphi^{j}\right)\\
&- \frac{N}{L} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{b} \mathcal D_{b}\!\left(\frac{1}{L^{3}} \gamma^{c} \mathcal D_{c}\!\left(L_{ij}\right) L^{jk} \varphi_{k}\right)
\end{aligned}
\tag{I.35}
```

**Source contribution 36.**

```math
\begin{aligned}
\frac12\rho'\bar\psi_a{}^i\gamma^a\gamma\!\cdot\!T\lambda'_i={}&- \frac{2 i N}{L^{2}} T_{bc} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{bc} \gamma^{d} \mathcal D_{d}\!\left(\varphi_{i}\right) - \frac{16 N}{L^{2}} L_{i}{}^{j} T_{bc} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{bc} \chi_{j} +\frac{4 N}{L^{2}} T_{bc} T_{de} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{bc} \gamma^{de} \varphi_{i} +\frac{2 N}{L^{4}} L_{i}{}^{j} T_{bc} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{bc} \left(i \gamma^{d} E_{d} +N\right) \varphi_{j}\\
&- \frac{2 i N}{L^{4}} L^{j}{}_{k} \mathcal D_{d}\!\left(L_{i}{}^{k}\right) T_{bc} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{bc} \gamma^{d} \varphi_{j}
\end{aligned}
\tag{I.36}
```

**Source contribution 37.**

```math
\begin{aligned}
-\frac1{16}\rho'\bar\psi_a{}^i\gamma^a\gamma\!\cdot\!\widehat G\lambda'_i={}&\frac{i N}{4 L^{2}} \widehat G_{bc} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{bc} \gamma^{d} \mathcal D_{d}\!\left(\varphi_{i}\right) +\frac{2 N}{L^{2}} \widehat G_{bc} L_{i}{}^{j} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{bc} \chi_{j} - \frac{N}{2 L^{2}} \widehat G_{bc} T_{de} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{bc} \gamma^{de} \varphi_{i} - \frac{N}{4 L^{4}} \widehat G_{bc} L_{i}{}^{j} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{bc} \left(i \gamma^{d} E_{d} +N\right) \varphi_{j}\\
&+\frac{i N}{4 L^{4}} \widehat G_{bc} L^{j}{}_{k} \mathcal D_{d}\!\left(L_{i}{}^{k}\right) \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{bc} \gamma^{d} \varphi_{j}
\end{aligned}
\tag{I.37}
```

**Source contribution 38.**

```math
\begin{aligned}
\frac g8\rho'\bar\psi_a{}^i\gamma^aL_{ij}\lambda'{}^j={}&\frac{i N g}{2 L^{2}} L_{i}{}^{j} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{b} \mathcal D_{b}\!\left(\varphi_{j}\right) - 2 N g \bar\psi_{a}{}^{i} \gamma^{a} \chi_{i} - \frac{N g}{L^{2}} L_{i}{}^{j} T_{bc} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{bc} \varphi_{j} +\frac{N g}{4 L^{2}} \bar\psi_{a}{}^{i} \gamma^{a} \left(i \gamma^{b} E_{b} +N\right) \varphi_{i}\\
&- \frac{i N g}{2 L^{4}} L_{ik} L^{j}{}_{l} \mathcal D_{b}\!\left(L^{kl}\right) \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{b} \varphi_{j}
\end{aligned}
\tag{I.38}
```

**Source contribution 39,40.**

```math
\begin{aligned}
\frac i4(\rho')^2\bar\psi_a{}^i\gamma^{ab} [\frac14\gamma\!\cdot\!\widehat G\psi_{bi} -\gamma\!\cdot\!T\psi_{bi}+\frac g2L_{ij}\psi_b{}^j-\phi_{bi}]={}&\frac{i N^{2}}{4 L^{2}} \widehat G_{cd} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{cd} \psi_{bi} - \frac{i N^{2}}{L^{2}} T_{cd} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{cd} \psi_{bi} - \frac{i N^{2} g}{2 L^{2}} L_{i}{}^{j} \bar\psi_{a}{}^{i} \gamma^{ab} \psi_{bj} - \frac{i N^{2}}{L^{2}} \bar\psi_{a}{}^{i} \gamma^{ab} \phi_{bi}
\end{aligned}
\tag{I.39}
```

**Source contribution 41.**

```math
\begin{aligned}
-\frac{ig}8(\rho')^2\bar\psi_a{}^i\gamma^{ab}\psi_b{}^jL_{ij}={}&\frac{i N^{2} g}{2 L^{2}} L_{i}{}^{j} \bar\psi_{a}{}^{i} \gamma^{ab} \psi_{bj}
\end{aligned}
\tag{I.41}
```

**Source contribution 42.**

```math
\begin{aligned}
\frac i4\rho'\bar\psi_a{}^i\gamma^{ab}\psi_b{}^jY'_{ij}={}&- \frac{i N}{2 L^{2}} \Box_c\!\left(L_{i}{}^{j}\right) \bar\psi_{a}{}^{i} \gamma^{ab} \psi_{bj} +\frac{i N}{2 L^{3}} \mathcal D_{c}\!\left(L\right) \mathcal D^{c}\!\left(L_{i}{}^{j}\right) \bar\psi_{a}{}^{i} \gamma^{ab} \psi_{bj} - \frac{i N}{2 L^{2}} \left(4 D +\frac{8}{3} T_{cd} T^{cd} - \frac{1}{L^{2}} E_{c} E^{c} - \frac{N^{2}}{L^{2}} +\frac{1}{2 L^{2}} \mathcal D_{c}\!\left(L_{kl}\right) \mathcal D^{c}\!\left(L^{kl}\right)\right) L_{i}{}^{j} \bar\psi_{a}{}^{i} \gamma^{ab} \psi_{bj} - \frac{i N}{L^{4}} E_{c} \varepsilon^{jk}\left(L_{l(i} \mathcal D^{c}\!\left(L_{k)}{}^{l}\right)\right) \bar\psi_{a}{}^{i} \gamma^{ab} \psi_{bj}
\end{aligned}
\tag{I.42}
```

<a id="49-add-the-contributions-and-collect-identical-ordered-words"></a>

### Add the contributions and collect identical ordered words

All 42 source groups occur once in Section 4.8; four mergers reduce their presentation to 35 contributions. Their 380 written summands first reduce to the inherited 373 summands by exact contraction collection and the cancellation (C.2). Eight pairs still carry the same ordered tensor word with different scalar coefficients. The following explicit sums merge those pairs, leaving 365 written summands. These are presentation counts, not a count of independent local operators.

```math
\begin{aligned}\left(4 g+\frac{64 N}{L^{2}}\right) \mathcal D_{a}\!\left(\bar\varphi_{i}\right) \gamma^{a} \chi^{i}\
&=\frac{4 \left(L^{2} g + 16 N\right)}{L^{2}} \mathcal D_{a}\!\left(\bar\varphi_{i}\right) \gamma^{a} \chi^{i}\end{aligned}
\tag{K.1}
```

```math
\begin{aligned}\left(- 32 i g- \frac{512 i N}{L^{2}}\right) L_{i}{}^{j} \bar\chi^{i} \chi_{j}\
&=- \frac{32 i \left(L^{2} g + 16 N\right)}{L^{2}} L_{i}{}^{j} \bar\chi^{i} \chi_{j}\end{aligned}
\tag{K.2}
```

```math
\begin{aligned}\left(8 i g+\frac{128 i N}{L^{2}}\right) T_{ab} \bar\varphi^{i} \gamma^{ab} \chi_{i}\
&=\frac{8 i \left(L^{2} g + 16 N\right)}{L^{2}} T_{ab} \bar\varphi^{i} \gamma^{ab} \chi_{i}\end{aligned}
\tag{K.3}
```

```math
\begin{aligned}\left(\frac{4 i g}{L^{2}}+\frac{64 i N}{L^{4}}\right) L_{i}{}^{j} \bar\varphi^{i} \left(i E_{a} \gamma^{a} +N\right) \chi_{j}\
&=\frac{4 i \left(L^{2} g + 16 N\right)}{L^{4}} L_{i}{}^{j} \bar\varphi^{i} \left(i E_{a} \gamma^{a} +N\right) \chi_{j}\end{aligned}
\tag{K.4}
```

```math
\begin{aligned}\left(\frac{4 g}{L^{2}}+\frac{64 N}{L^{4}}\right) L_{ik} \mathcal D_{a}\!\left(L^{jk}\right) \bar\varphi^{i} \gamma^{a} \chi_{j}\
&=\frac{4 \left(L^{2} g + 16 N\right)}{L^{4}} L_{ik} \mathcal D_{a}\!\left(L^{jk}\right) \bar\varphi^{i} \gamma^{a} \chi_{j}\end{aligned}
\tag{K.5}
```

```math
\begin{aligned}\left(- 6 N g- \frac{20 N^{2}}{L^{2}}\right) \bar\psi_{a}{}^{i} \gamma^{a} \chi_{i}\
&=- \frac{2 N \left(3 L^{2} g + 10 N\right)}{L^{2}} \bar\psi_{a}{}^{i} \gamma^{a} \chi_{i}\end{aligned}
\tag{K.6}
```

```math
\begin{aligned}\left(- 2 i g- \frac{16 i N}{L^{2}}\right) E_{b} \bar\psi_{a}{}^{i} \gamma^{ab} \chi_{i}\
&=- \frac{2 i \left(L^{2} g + 8 N\right)}{L^{2}} E_{b} \bar\psi_{a}{}^{i} \gamma^{ab} \chi_{i}\end{aligned}
\tag{K.7}
```

```math
\begin{aligned}\left(- \sqrt{2} i L g- \frac{8 \sqrt{2} i N}{L}\right) V_{b} \bar\psi_{a}{}^{i} \gamma^{ab} \chi_{i}\
&=- \frac{\sqrt{2} i \left(L^{2} g + 8 N\right)}{L} V_{b} \bar\psi_{a}{}^{i} \gamma^{ab} \chi_{i}\end{aligned}
\tag{K.8}
```

For every other word, its coefficient is unchanged. No odd factor or Clifford matrix is moved in these eight sums. The two terms multiplying a given word have the same engineering dimension, so their sum is an allowed coefficient. Replacing the pairs by (K.1)–(K.8) yields the single action in Section 6.

<a id="5-consistency-checks"></a>

## Consistency Checks

<a id="51-dimensions-indices-and-truncation"></a>

### Dimensions, indices and truncation

Before fixing the scale, the conformal weights are $`w(\rho,A_a)=1`$, $`w(\lambda)=3/2`$, $`w(Y,\widehat F,T\rho)=2`$, $`w(L_{ij},\varphi,E_a,N)=(3,7/2,4,4)`$. Thus each BF term has weight five; for example $`w(Y'L')=2+3=5`$, $`w(\rho'N')=1+4=5`$, and $`w(\bar\lambda'\varphi')=3/2+7/2=5`$. The fixed compensator supplies the omitted conformal weight in the gauge-fixed action.

For gauge-fixed engineering counting in compensator units, $`[L]=[L_{ij}]=0`$, $`[N]=[E]=[g]=[T]=[\widehat G]=[V]=1`$, $`[\varphi]=[\psi_a]=1/2`$, $`[\chi]=[\phi_a]=[\widehat R(Q)]=3/2`$, $`[D]=[f]=[\widehat R(V)]=2`$ and $`[\mathcal D]=1`$. Therefore $`[\rho']=1`$, $`[\lambda']=3/2`$, $`[Y']=[\widehat F']=2`$ and each final density term has dimension four. For instance:

```math
\begin{aligned}
[L^{-2}(\Box_cL_{ij})(\Box_cL^{ij})]&=2+2=4,\\
[L^{-1}(\mathcal D_a\bar\varphi_i)\gamma^a\gamma^b
\mathcal D_b(L^{-1}\not{\mathcal D}\varphi^i)]
&=\left(1+\tfrac12\right)+\left(1+1+\tfrac12\right)=4,\\
[(g+16N/L^2)(\mathcal D_a\bar\varphi_i)\gamma^a\chi^i]
&=1+\tfrac32+\tfrac32=4.
\end{aligned}
\tag{V.1}
```

All free vector or triplet indices in a map match its left-hand side. All indices in the action are paired with opposite variance, including those inside held derivatives and symmetry brackets. Explicit $`\varepsilon^{ij}`$ is shown where a symmetric pair would otherwise be printed with mixed variance. The factor order is preserved in every fermion bilinear.

An even composite begins at physical order zero and an odd composite at order one. Hence every omitted outer product of explicit degree four has minimum physical degree four; none can feed the retained action. Conversely, a displayed term with no explicit fermion may contain physical quadratic pieces in $`T,D,E,\widehat G,\Box_c,\mathcal D,\widehat R(V)`$ and the dependent connections. Those pieces are retained by using the full definitions, not discarded by a component projection.

<a id="52-independent-limiting-coefficient-test"></a>

### Independent limiting coefficient test

For an algebraic coefficient test only, set the formal derivative/background slots and fermions to zero, keeping $`L,N,g`$. This is not an assignment solving the gauged composite relations. The two surviving contributions provide a direct check independent of the large distribution:

```math
\begin{aligned}
\rho'&=\frac{2N}{L},&Y'_{ij}&=-\frac{N^2}{\sqrt2L^2}\delta_{ij},&
\lambda'_i&=\widehat F'_{ab}=A'_a=0,\\
Y'^{ij}Y'_{ij}
&=\frac{N^4}{2L^4}\delta^{ij}\delta_{ij}=\frac{N^4}{L^4},\\
-g\rho'Y'^{ij}L_{ij}
&=-g\frac{2N}{L}\left(-\frac{N^2}{2L}\delta^{ij}\delta_{ij}\right)
=\frac{2gN^3}{L^2},\\
e^{-1}\mathcal L_{VL}\big|_{\rm coefficient\ test}
&=\frac{N^4}{L^4}+\frac{2gN^3}{L^2}
\ \xrightarrow{g\to0}\ \frac{N^4}{L^4}.
\end{aligned}
\tag{V.2}
```

The regular $`g\to0`$ limit is also checked at fixed source slots: none of the scalar coefficients has an inverse power of $`g`$. A physical ungauged limit additionally specializes every Coomans composite. No auxiliary equation or vacuum restriction is used as a shortcut.

<a id="53-curvature-square-normalization-without-using-golds-action"></a>

### Curvature-square normalization without using Gold's action

To isolate only the curvature-square coefficient, take the zero-fermion, zero-flux constant-compensator sector and suppress the non-curvature algebraic slots. The source dependent-$`K`$ constraint gives $`f_a{}^a=-R/16`$ in this sector; the scalar and triplet conformal boxes have $`2f_a{}^a\sigma`$ and $`6f_a{}^aL_{ij}`$, respectively. These are the same source definitions used in [gauged-density derivation](../../../computations/r2_fermionic/inputs/reference/r2/notes/10_step6_gauged_action_through_two_fermions.md), (B20), (E6). Therefore

```math
\begin{aligned}
\left.\Box_c\sigma\right|_R&=2f_a{}^a=-\frac18R,
&\left.D\right|_R&=\frac14\left.\Box_c\sigma\right|_R=-\frac1{32}R,\\
\left.\Box_cL_{ij}\right|_R&=6f_a{}^aL_{ij}=-\frac38R L_{ij},\\
\left.Y'_{ij}\right|_R
&=\frac1L\left(-\frac38R L_{ij}\right)+\frac4L L_{ij}\left(-\frac1{32}R\right)
=-\frac{R}{2L}L_{ij},\\
\left.e^{-1}\mathcal L_{R^2}\right|_{R^2}
&=\left(-\frac{R}{2L}L^{ij}\right)\left(-\frac{R}{2L}L_{ij}\right)
=\frac{R^2}{4L^2}L^{ij}L_{ij}=\frac14R^2.
\end{aligned}
\tag{V.3}
```

This is a coefficient extraction, not a vacuum condition or a replacement of the full gauged backgrounds. Thus the unit BF density has the inherited positive $`R^2/4`$ coefficient. No rescaling to a unit $`R^2`$ coefficient is made.

<a id="6-final-result"></a>

## Final Result

**The full canonicalized action through two fermions is written below in one integral.** Every primed map has been inserted and the identical contractions collected across the entire action. All terms appear directly inside the braces; no contribution labels or sums over earlier equations are used. Several terms share each line.

The subscript $`\leq2`$ applies to the complete integrand, including the implicit completions of the retained supercovariant objects. The closed gauged background objects are those defined in Section 3.3. There is no separation into bosonic and fermionic actions.

<!-- BEGIN SINGLE CANONICAL R2 ACTION -->

```math
\begin{aligned}
S_{R^2}^{\leq2}=\lambda_{R^2}\int d^5x\,e\,\Bigg\{&\frac{1}{L^{2}} \Box_c\!\left(L_{ij}\right) \Box_c\!\left(L^{ij}\right) - \frac{2}{L^{3}} \Box_c\!\left(L_{ij}\right) \mathcal D_{a}\!\left(L\right) \mathcal D^{a}\!\left(L^{ij}\right) +\frac{2}{L^{2}} \left(4 D +\frac{8}{3} T_{ab} T^{ab} - \frac{1}{L^{2}} E_{a} E^{a} - \frac{N^{2}}{L^{2}} +\frac{1}{2 L^{2}} \mathcal D_{a}\!\left(L_{kl}\right) \mathcal D^{a}\!\left(L^{kl}\right)\right) L_{ij} \Box_c\!\left(L^{ij}\right) +\frac{2}{L^{4}} \Box_c\!\left(L^{ij}\right) \left(\bar\varphi_{(i} \left(i N - \gamma^{b} E_{b}\right) \varphi_{j)}\right)\\
&+\frac{6}{L^{6}} L_{i}{}^{j} L_{kl} \Box_c\!\left(L^{kl}\right) \bar\varphi^{i} \left(i N - \gamma^{a} E_{a}\right) \varphi_{j} +\frac{4}{L^{4}} E_{a} \left(L_{k(i} \mathcal D^{a}\!\left(L_{j)}{}^{k}\right)\right) \Box_c\!\left(L^{ij}\right) +\frac{6}{L^{6}} \left(L_{m(k} \mathcal D_{a}\!\left(L_{l)}{}^{m}\right)\right) L_{i}{}^{j} \Box_c\!\left(L^{kl}\right) \bar\varphi^{i} \gamma^{a} \varphi_{j} - \frac{32 i}{L^{2}} \Box_c\!\left(L^{ij}\right) \left(\bar\chi_{(i} \varphi_{j)}\right)\\
&- \frac{32 i}{L^{4}} L_{i}{}^{j} L_{kl} \Box_c\!\left(L^{kl}\right) \bar\chi^{i} \varphi_{j} +\frac{4}{L^{4}} \Box_c\!\left(L^{ij}\right) \left(L_{k(i} \bar\varphi^{k} \gamma^{a} \mathcal D_{a}\!\left(\varphi_{j)}\right)\right) - \frac{2}{L^{4}} \Box_c\!\left(L^{ij}\right) \left(\bar\varphi^{k} \gamma^{a} \mathcal D_{a}\!\left(L_{k(i}\right) \varphi_{j)}\right) +\frac{4 i}{L^{4}} L_{jk} \Box_c\!\left(L^{jk}\right) T_{ab} \bar\varphi^{i} \gamma^{ab} \varphi_{i}\\
&+\frac{1}{L^{4}} \mathcal D_{a}\!\left(L\right) \mathcal D_{b}\!\left(L\right) \mathcal D^{a}\!\left(L_{ij}\right) \mathcal D^{b}\!\left(L^{ij}\right) - \frac{2}{L^{3}} \left(4 D +\frac{8}{3} T_{bc} T^{bc} - \frac{1}{L^{2}} E_{b} E^{b} - \frac{N^{2}}{L^{2}} +\frac{1}{2 L^{2}} \mathcal D_{b}\!\left(L_{kl}\right) \mathcal D^{b}\!\left(L^{kl}\right)\right) L_{ij} \mathcal D_{a}\!\left(L\right) \mathcal D^{a}\!\left(L^{ij}\right) - \frac{2}{L^{5}} \mathcal D_{a}\!\left(L\right) \mathcal D^{a}\!\left(L^{ij}\right) \left(\bar\varphi_{(i} \left(i N - \gamma^{c} E_{c}\right) \varphi_{j)}\right) - \frac{6}{L^{7}} L_{i}{}^{j} L_{kl} \mathcal D_{a}\!\left(L\right) \mathcal D^{a}\!\left(L^{kl}\right) \bar\varphi^{i} \left(i N - \gamma^{b} E_{b}\right) \varphi_{j}\\
&- \frac{4}{L^{5}} E_{a} \left(L_{k(i} \mathcal D^{a}\!\left(L_{j)}{}^{k}\right)\right) \mathcal D_{b}\!\left(L\right) \mathcal D^{b}\!\left(L^{ij}\right) - \frac{6}{L^{7}} \left(L_{m(k} \mathcal D_{a}\!\left(L_{l)}{}^{m}\right)\right) L_{i}{}^{j} \mathcal D_{b}\!\left(L\right) \mathcal D^{b}\!\left(L^{kl}\right) \bar\varphi^{i} \gamma^{a} \varphi_{j} +\frac{32 i}{L^{3}} \mathcal D_{a}\!\left(L\right) \mathcal D^{a}\!\left(L^{ij}\right) \left(\bar\chi_{(i} \varphi_{j)}\right) +\frac{32 i}{L^{5}} L_{i}{}^{j} L_{kl} \mathcal D_{a}\!\left(L\right) \mathcal D^{a}\!\left(L^{kl}\right) \bar\chi^{i} \varphi_{j}\\
&- \frac{4}{L^{5}} \mathcal D_{a}\!\left(L\right) \mathcal D^{a}\!\left(L^{ij}\right) \left(L_{k(i} \bar\varphi^{k} \gamma^{b} \mathcal D_{b}\!\left(\varphi_{j)}\right)\right) +\frac{2}{L^{5}} \mathcal D_{a}\!\left(L\right) \mathcal D^{a}\!\left(L^{ij}\right) \left(\bar\varphi^{k} \gamma^{b} \mathcal D_{b}\!\left(L_{k(i}\right) \varphi_{j)}\right) - \frac{4 i}{L^{5}} L_{jk} \mathcal D_{c}\!\left(L\right) \mathcal D^{c}\!\left(L^{jk}\right) T_{ab} \bar\varphi^{i} \gamma^{ab} \varphi_{i} +\left(4 D +\frac{8}{3} T_{ab} T^{ab} - \frac{1}{L^{2}} E_{a} E^{a} - \frac{N^{2}}{L^{2}} +\frac{1}{2 L^{2}} \mathcal D_{a}\!\left(L_{ij}\right) \mathcal D^{a}\!\left(L^{ij}\right)\right) \left(4 D +\frac{8}{3} T_{cd} T^{cd} - \frac{1}{L^{2}} E_{c} E^{c} - \frac{N^{2}}{L^{2}} +\frac{1}{2 L^{2}} \mathcal D_{c}\!\left(L_{kl}\right) \mathcal D^{c}\!\left(L^{kl}\right)\right)\\
&+\frac{2}{L^{4}} \left(4 D +\frac{8}{3} T_{ab} T^{ab} - \frac{1}{L^{2}} E_{a} E^{a} - \frac{N^{2}}{L^{2}} +\frac{1}{2 L^{2}} \mathcal D_{a}\!\left(L_{kl}\right) \mathcal D^{a}\!\left(L^{kl}\right)\right) L^{ij} \left(\bar\varphi_{(i} \left(i N - \gamma^{d} E_{d}\right) \varphi_{j)}\right) +\frac{6}{L^{4}} \left(4 D +\frac{8}{3} T_{ab} T^{ab} - \frac{1}{L^{2}} E_{a} E^{a} - \frac{N^{2}}{L^{2}} +\frac{1}{2 L^{2}} \mathcal D_{a}\!\left(L_{kl}\right) \mathcal D^{a}\!\left(L^{kl}\right)\right) L_{i}{}^{j} \bar\varphi^{i} \left(i N - \gamma^{c} E_{c}\right) \varphi_{j} +\frac{4}{L^{4}} E_{a} \left(4 D +\frac{8}{3} T_{bc} T^{bc} - \frac{1}{L^{2}} E_{b} E^{b} - \frac{N^{2}}{L^{2}} +\frac{1}{2 L^{2}} \mathcal D_{b}\!\left(L_{kl}\right) \mathcal D^{b}\!\left(L^{kl}\right)\right) \left(L_{m(i} \mathcal D^{a}\!\left(L_{j)}{}^{m}\right)\right) L^{ij} +\frac{6}{L^{6}} \left(4 D +\frac{8}{3} T_{bc} T^{bc} - \frac{1}{L^{2}} E_{b} E^{b} - \frac{N^{2}}{L^{2}} +\frac{1}{2 L^{2}} \mathcal D_{b}\!\left(L_{mn}\right) \mathcal D^{b}\!\left(L^{mn}\right)\right) \left(L_{o(k} \mathcal D_{a}\!\left(L_{l)}{}^{o}\right)\right) L_{i}{}^{j} L^{kl} \bar\varphi^{i} \gamma^{a} \varphi_{j}\\
&- \frac{32 i}{L^{2}} \left(4 D +\frac{8}{3} T_{ab} T^{ab} - \frac{1}{L^{2}} E_{a} E^{a} - \frac{N^{2}}{L^{2}} +\frac{1}{2 L^{2}} \mathcal D_{a}\!\left(L_{kl}\right) \mathcal D^{a}\!\left(L^{kl}\right)\right) L^{ij} \left(\bar\chi_{(i} \varphi_{j)}\right) - \frac{32 i}{L^{2}} \left(4 D +\frac{8}{3} T_{ab} T^{ab} - \frac{1}{L^{2}} E_{a} E^{a} - \frac{N^{2}}{L^{2}} +\frac{1}{2 L^{2}} \mathcal D_{a}\!\left(L_{kl}\right) \mathcal D^{a}\!\left(L^{kl}\right)\right) L_{i}{}^{j} \bar\chi^{i} \varphi_{j} +\frac{4}{L^{4}} \left(4 D +\frac{8}{3} T_{ab} T^{ab} - \frac{1}{L^{2}} E_{a} E^{a} - \frac{N^{2}}{L^{2}} +\frac{1}{2 L^{2}} \mathcal D_{a}\!\left(L_{kl}\right) \mathcal D^{a}\!\left(L^{kl}\right)\right) L^{ij} \left(L_{m(i} \bar\varphi^{m} \gamma^{c} \mathcal D_{c}\!\left(\varphi_{j)}\right)\right) - \frac{2}{L^{4}} \left(4 D +\frac{8}{3} T_{ab} T^{ab} - \frac{1}{L^{2}} E_{a} E^{a} - \frac{N^{2}}{L^{2}} +\frac{1}{2 L^{2}} \mathcal D_{a}\!\left(L_{kl}\right) \mathcal D^{a}\!\left(L^{kl}\right)\right) L^{ij} \left(\bar\varphi^{m} \gamma^{c} \mathcal D_{c}\!\left(L_{m(i}\right) \varphi_{j)}\right)\\
&+\frac{4 i}{L^{2}} \left(4 D +\frac{8}{3} T_{cd} T^{cd} - \frac{1}{L^{2}} E_{c} E^{c} - \frac{N^{2}}{L^{2}} +\frac{1}{2 L^{2}} \mathcal D_{c}\!\left(L_{jk}\right) \mathcal D^{c}\!\left(L^{jk}\right)\right) T_{ab} \bar\varphi^{i} \gamma^{ab} \varphi_{i} +\frac{4}{L^{6}} E_{a} \left(L_{k}{}^{(i} \mathcal D^{a}\!\left(L^{j)k}\right)\right) \left(\bar\varphi_{(i} \left(i N - \gamma^{c} E_{c}\right) \varphi_{j)}\right) +\frac{12}{L^{8}} E_{a} \left(L_{m(k} \mathcal D^{a}\!\left(L_{l)}{}^{m}\right)\right) L_{i}{}^{j} L^{kl} \bar\varphi^{i} \left(i N - \gamma^{b} E_{b}\right) \varphi_{j} +\frac{4}{L^{6}} E_{a} E_{b} \left(L_{k(i} \mathcal D^{a}\!\left(L_{j)}{}^{k}\right)\right) \left(L_{l}{}^{(i} \mathcal D^{b}\!\left(L^{j)l}\right)\right)\\
&+\frac{6}{L^{8}} E_{b} \left(L_{m(k} \mathcal D^{b}\!\left(L_{l)}{}^{m}\right)\right) \left(L_{n}{}^{(k} \mathcal D_{a}\!\left(L^{l)n}\right)\right) L_{i}{}^{j} \bar\varphi^{i} \gamma^{a} \varphi_{j} - \frac{64 i}{L^{4}} E_{a} \left(L_{k}{}^{(i} \mathcal D^{a}\!\left(L^{j)k}\right)\right) \left(\bar\chi_{(i} \varphi_{j)}\right) - \frac{64 i}{L^{6}} E_{a} \left(L_{m(k} \mathcal D^{a}\!\left(L_{l)}{}^{m}\right)\right) L_{i}{}^{j} L^{kl} \bar\chi^{i} \varphi_{j} +\frac{8}{L^{6}} E_{a} \left(L_{k}{}^{(i} \mathcal D^{a}\!\left(L^{j)k}\right)\right) \left(L_{l(i} \bar\varphi^{l} \gamma^{b} \mathcal D_{b}\!\left(\varphi_{j)}\right)\right)\\
&- \frac{4}{L^{6}} E_{a} \left(L_{k}{}^{(i} \mathcal D^{a}\!\left(L^{j)k}\right)\right) \left(\bar\varphi^{l} \gamma^{b} \mathcal D_{b}\!\left(L_{l(i}\right) \varphi_{j)}\right) +\frac{8 i}{L^{6}} E_{c} \left(L_{l(j} \mathcal D^{c}\!\left(L_{k)}{}^{l}\right)\right) L^{jk} T_{ab} \bar\varphi^{i} \gamma^{ab} \varphi_{i} +\frac{6}{L^{8}} E_{b} \left(L_{m(k} \mathcal D_{a}\!\left(L_{l)}{}^{m}\right)\right) \left(L_{n}{}^{(k} \mathcal D^{b}\!\left(L^{l)n}\right)\right) L_{i}{}^{j} \bar\varphi^{i} \gamma^{a} \varphi_{j} - \frac{2 N g}{L^{2}} L_{ij} \Box_c\!\left(L^{ij}\right)\\
&+\frac{2 N g}{L^{3}} L_{ij} \mathcal D_{a}\!\left(L\right) \mathcal D^{a}\!\left(L^{ij}\right) - 2 N g \left(4 D +\frac{8}{3} T_{ab} T^{ab} - \frac{1}{L^{2}} E_{a} E^{a} - \frac{N^{2}}{L^{2}} +\frac{1}{2 L^{2}} \mathcal D_{a}\!\left(L_{ij}\right) \mathcal D^{a}\!\left(L^{ij}\right)\right) - \frac{2 N g}{L^{4}} L^{ij} \left(\bar\varphi_{(i} \left(i N - \gamma^{b} E_{b}\right) \varphi_{j)}\right) - \frac{6 N g}{L^{4}} L_{i}{}^{j} \bar\varphi^{i} \left(i N - \gamma^{a} E_{a}\right) \varphi_{j}\\
&- \frac{4 N g}{L^{4}} E_{a} \left(L_{k(i} \mathcal D^{a}\!\left(L_{j)}{}^{k}\right)\right) L^{ij} - \frac{6 N g}{L^{6}} \left(L_{m(k} \mathcal D_{a}\!\left(L_{l)}{}^{m}\right)\right) L_{i}{}^{j} L^{kl} \bar\varphi^{i} \gamma^{a} \varphi_{j} +\frac{32 i N g}{L^{2}} L^{ij} \left(\bar\chi_{(i} \varphi_{j)}\right) +\frac{32 i N g}{L^{2}} L_{i}{}^{j} \bar\chi^{i} \varphi_{j}\\
&- \frac{4 N g}{L^{4}} L^{ij} \left(L_{k(i} \bar\varphi^{k} \gamma^{a} \mathcal D_{a}\!\left(\varphi_{j)}\right)\right) +\frac{2 N g}{L^{4}} L^{ij} \left(\bar\varphi^{k} \gamma^{a} \mathcal D_{a}\!\left(L_{k(i}\right) \varphi_{j)}\right) - \frac{4 i N g}{L^{2}} T_{ab} \bar\varphi^{i} \gamma^{ab} \varphi_{i} +\frac{i g}{L^{4}} L_{i}{}^{j} L_{kl} \Box_c\!\left(L^{kl}\right) \bar\varphi^{i} \varphi_{j}\\
&- \frac{i g}{L^{5}} L_{i}{}^{j} L_{kl} \mathcal D_{a}\!\left(L\right) \mathcal D^{a}\!\left(L^{kl}\right) \bar\varphi^{i} \varphi_{j} +\frac{i g}{L^{2}} \left(4 D +\frac{8}{3} T_{ab} T^{ab} - \frac{1}{L^{2}} E_{a} E^{a} - \frac{N^{2}}{L^{2}} +\frac{1}{2 L^{2}} \mathcal D_{a}\!\left(L_{kl}\right) \mathcal D^{a}\!\left(L^{kl}\right)\right) L_{i}{}^{j} \bar\varphi^{i} \varphi_{j} +\frac{2 i g}{L^{6}} E_{a} \left(L_{m(k} \mathcal D^{a}\!\left(L_{l)}{}^{m}\right)\right) L_{i}{}^{j} L^{kl} \bar\varphi^{i} \varphi_{j} - \frac{2}{L} \mathcal D_{a}\!\left(\bar\varphi_{i}\right) \gamma^{a} \gamma^{b} \mathcal D_{b}\!\left(\frac{1}{L} \gamma^{c} \mathcal D_{c}\!\left(\varphi^{i}\right)\right)\\
&- \frac{16 i}{L} \mathcal D_{a}\!\left(\bar\varphi_{i}\right) \gamma^{a} \gamma^{b} \mathcal D_{b}\!\left(\frac{1}{L} L^{i}{}_{j} \chi^{j}\right) - \frac{4 i}{L} \mathcal D_{a}\!\left(\bar\varphi_{i}\right) \gamma^{a} \gamma^{b} \mathcal D_{b}\!\left(\frac{1}{L} \gamma^{cd} T_{cd} \varphi^{i}\right) +\frac{2 i}{L} \mathcal D_{a}\!\left(\bar\varphi_{i}\right) \gamma^{a} \gamma^{b} \mathcal D_{b}\!\left(\frac{1}{L^{3}} L^{i}{}_{j} \left(i \gamma^{c} E_{c} +N\right) \varphi^{j}\right) +\frac{2}{L} \mathcal D_{a}\!\left(\bar\varphi_{i}\right) \gamma^{a} \gamma^{b} \mathcal D_{b}\!\left(\frac{1}{L^{3}} \gamma^{c} \mathcal D_{c}\!\left(L^{i}{}_{j}\right) L^{jk} \varphi_{k}\right)\\
&+\frac{16 i}{L} L_{i}{}^{j} \bar\chi^{i} \gamma^{a} \mathcal D_{a}\!\left(\frac{1}{L} \gamma^{b} \mathcal D_{b}\!\left(\varphi_{j}\right)\right) - \frac{128}{L} L_{i}{}^{j} \bar\chi^{i} \gamma^{a} \mathcal D_{a}\!\left(\frac{1}{L} L_{jk} \chi^{k}\right) - \frac{32}{L} L_{i}{}^{j} \bar\chi^{i} \gamma^{a} \mathcal D_{a}\!\left(\frac{1}{L} \gamma^{bc} T_{bc} \varphi_{j}\right) +\frac{16}{L} L_{i}{}^{j} \bar\chi^{i} \gamma^{a} \mathcal D_{a}\!\left(\frac{1}{L^{3}} L_{jk} \left(i \gamma^{b} E_{b} +N\right) \varphi^{k}\right)\\
&- \frac{16 i}{L} L_{i}{}^{j} \bar\chi^{i} \gamma^{a} \mathcal D_{a}\!\left(\frac{1}{L^{3}} \gamma^{b} \mathcal D_{b}\!\left(L_{jk}\right) L^{kl} \varphi_{l}\right) - \frac{4 i}{L} T_{ab} \bar\varphi^{i} \gamma^{ab} \gamma^{c} \mathcal D_{c}\!\left(\frac{1}{L} \gamma^{d} \mathcal D_{d}\!\left(\varphi_{i}\right)\right) +\frac{32}{L} T_{ab} \bar\varphi^{i} \gamma^{ab} \gamma^{c} \mathcal D_{c}\!\left(\frac{1}{L} L_{ij} \chi^{j}\right) +\frac{8}{L} T_{ab} \bar\varphi^{i} \gamma^{ab} \gamma^{c} \mathcal D_{c}\!\left(\frac{1}{L} \gamma^{de} T_{de} \varphi_{i}\right)\\
&- \frac{4}{L} T_{ab} \bar\varphi^{i} \gamma^{ab} \gamma^{c} \mathcal D_{c}\!\left(\frac{1}{L^{3}} L_{ij} \left(i \gamma^{d} E_{d} +N\right) \varphi^{j}\right) +\frac{4 i}{L} T_{ab} \bar\varphi^{i} \gamma^{ab} \gamma^{c} \mathcal D_{c}\!\left(\frac{1}{L^{3}} \gamma^{d} \mathcal D_{d}\!\left(L_{ij}\right) L^{jk} \varphi_{k}\right) - \frac{2 i}{L^{3}} L_{i}{}^{j} \bar\varphi^{i} \left(i E_{b} \gamma^{b} +N\right) \gamma^{a} \mathcal D_{a}\!\left(\frac{1}{L} \gamma^{c} \mathcal D_{c}\!\left(\varphi_{j}\right)\right) +\frac{16}{L^{3}} L_{i}{}^{j} \bar\varphi^{i} \left(i E_{b} \gamma^{b} +N\right) \gamma^{a} \mathcal D_{a}\!\left(\frac{1}{L} L_{jk} \chi^{k}\right)\\
&+\frac{4}{L^{3}} L_{i}{}^{j} \bar\varphi^{i} \left(i E_{b} \gamma^{b} +N\right) \gamma^{a} \mathcal D_{a}\!\left(\frac{1}{L} \gamma^{cd} T_{cd} \varphi_{j}\right) - \frac{2}{L^{3}} L_{i}{}^{j} \bar\varphi^{i} \left(i E_{b} \gamma^{b} +N\right) \gamma^{a} \mathcal D_{a}\!\left(\frac{1}{L^{3}} L_{jk} \left(i \gamma^{c} E_{c} +N\right) \varphi^{k}\right) +\frac{2 i}{L^{3}} L_{i}{}^{j} \bar\varphi^{i} \left(i E_{b} \gamma^{b} +N\right) \gamma^{a} \mathcal D_{a}\!\left(\frac{1}{L^{3}} \gamma^{c} \mathcal D_{c}\!\left(L_{jk}\right) L^{kl} \varphi_{l}\right) - \frac{2}{L^{3}} L_{ik} \mathcal D_{a}\!\left(L^{jk}\right) \bar\varphi^{i} \gamma^{a} \gamma^{b} \mathcal D_{b}\!\left(\frac{1}{L} \gamma^{c} \mathcal D_{c}\!\left(\varphi_{j}\right)\right)\\
&- \frac{16 i}{L^{3}} L_{ik} \mathcal D_{a}\!\left(L^{jk}\right) \bar\varphi^{i} \gamma^{a} \gamma^{b} \mathcal D_{b}\!\left(\frac{1}{L} L_{jl} \chi^{l}\right) - \frac{4 i}{L^{3}} L_{ik} \mathcal D_{a}\!\left(L^{jk}\right) \bar\varphi^{i} \gamma^{a} \gamma^{b} \mathcal D_{b}\!\left(\frac{1}{L} \gamma^{cd} T_{cd} \varphi_{j}\right) +\frac{2 i}{L^{3}} L_{ik} \mathcal D_{a}\!\left(L^{jk}\right) \bar\varphi^{i} \gamma^{a} \gamma^{b} \mathcal D_{b}\!\left(\frac{1}{L^{3}} L_{jl} \left(i \gamma^{c} E_{c} +N\right) \varphi^{l}\right) +\frac{2}{L^{3}} L_{ik} \mathcal D_{a}\!\left(L^{jk}\right) \bar\varphi^{i} \gamma^{a} \gamma^{b} \mathcal D_{b}\!\left(\frac{1}{L^{3}} \gamma^{c} \mathcal D_{c}\!\left(L_{jl}\right) L^{lm} \varphi_{m}\right)\\
&+\frac{4 i}{L^{2}} T_{bc} \mathcal D_{a}\!\left(\bar\varphi_{i}\right) \gamma^{a} \gamma^{bc} \gamma^{d} \mathcal D_{d}\!\left(\varphi^{i}\right) +\frac{32}{L^{2}} L^{ij} T_{bc} \mathcal D_{a}\!\left(\bar\varphi_{i}\right) \gamma^{a} \gamma^{bc} \chi_{j} - \frac{8}{L^{2}} T_{bc} T_{de} \mathcal D_{a}\!\left(\bar\varphi_{i}\right) \gamma^{a} \gamma^{bc} \gamma^{de} \varphi^{i} - \frac{4}{L^{4}} L^{ij} T_{bc} \mathcal D_{a}\!\left(\bar\varphi_{i}\right) \gamma^{a} \gamma^{bc} \left(i \gamma^{d} E_{d} +N\right) \varphi_{j}\\
&+\frac{4 i}{L^{4}} L^{j}{}_{k} \mathcal D_{d}\!\left(L^{ik}\right) T_{bc} \mathcal D_{a}\!\left(\bar\varphi_{i}\right) \gamma^{a} \gamma^{bc} \gamma^{d} \varphi_{j} +\frac{32}{L^{2}} L_{i}{}^{j} T_{ab} \bar\chi^{i} \gamma^{ab} \gamma^{c} \mathcal D_{c}\!\left(\varphi_{j}\right) +128 i T_{ab} \bar\chi^{i} \gamma^{ab} \chi_{i} +\frac{64 i}{L^{2}} L_{i}{}^{j} T_{ab} T_{cd} \bar\chi^{i} \gamma^{ab} \gamma^{cd} \varphi_{j}\\
&- \frac{16 i}{L^{2}} T_{ab} \bar\chi^{i} \gamma^{ab} \left(i \gamma^{c} E_{c} +N\right) \varphi_{i} - \frac{32}{L^{4}} L_{ik} L^{j}{}_{l} \mathcal D_{c}\!\left(L^{kl}\right) T_{ab} \bar\chi^{i} \gamma^{ab} \gamma^{c} \varphi_{j} - \frac{8}{L^{2}} T_{ab} T_{cd} \bar\varphi^{i} \gamma^{ab} \gamma^{cd} \gamma^{e} \mathcal D_{e}\!\left(\varphi_{i}\right) +\frac{64 i}{L^{2}} L_{i}{}^{j} T_{ab} T_{cd} \bar\varphi^{i} \gamma^{ab} \gamma^{cd} \chi_{j}\\
&- \frac{16 i}{L^{2}} T_{ab} T_{cd} T_{ef} \bar\varphi^{i} \gamma^{ab} \gamma^{cd} \gamma^{ef} \varphi_{i} - \frac{8 i}{L^{4}} L_{i}{}^{j} T_{ab} T_{cd} \bar\varphi^{i} \gamma^{ab} \gamma^{cd} \left(i \gamma^{e} E_{e} +N\right) \varphi_{j} - \frac{8}{L^{4}} L^{j}{}_{k} \mathcal D_{e}\!\left(L_{i}{}^{k}\right) T_{ab} T_{cd} \bar\varphi^{i} \gamma^{ab} \gamma^{cd} \gamma^{e} \varphi_{j} - \frac{4}{L^{4}} L_{i}{}^{j} T_{ab} \bar\varphi^{i} \left(i E_{d} \gamma^{d} +N\right) \gamma^{ab} \gamma^{c} \mathcal D_{c}\!\left(\varphi_{j}\right)\\
&- \frac{16 i}{L^{2}} T_{ab} \bar\varphi^{i} \left(i E_{c} \gamma^{c} +N\right) \gamma^{ab} \chi_{i} - \frac{8 i}{L^{4}} L_{i}{}^{j} T_{ab} T_{cd} \bar\varphi^{i} \left(i E_{e} \gamma^{e} +N\right) \gamma^{ab} \gamma^{cd} \varphi_{j} +\frac{2 i}{L^{4}} T_{ab} \bar\varphi^{i} \left(i E_{c} \gamma^{c} +N\right) \gamma^{ab} \left(i \gamma^{d} E_{d} +N\right) \varphi_{i} +\frac{4}{L^{6}} L_{ik} L^{j}{}_{l} \mathcal D_{c}\!\left(L^{kl}\right) T_{ab} \bar\varphi^{i} \left(i E_{d} \gamma^{d} +N\right) \gamma^{ab} \gamma^{c} \varphi_{j}\\
&+\frac{4 i}{L^{4}} L_{ik} \mathcal D_{a}\!\left(L^{jk}\right) T_{bc} \bar\varphi^{i} \gamma^{a} \gamma^{bc} \gamma^{d} \mathcal D_{d}\!\left(\varphi_{j}\right) +\frac{32}{L^{4}} L_{ik} L^{j}{}_{l} \mathcal D_{a}\!\left(L^{lk}\right) T_{bc} \bar\varphi^{i} \gamma^{a} \gamma^{bc} \chi_{j} - \frac{8}{L^{4}} L_{ik} \mathcal D_{a}\!\left(L^{jk}\right) T_{bc} T_{de} \bar\varphi^{i} \gamma^{a} \gamma^{bc} \gamma^{de} \varphi_{j} - \frac{4}{L^{6}} L_{ik} L^{j}{}_{l} \mathcal D_{a}\!\left(L^{lk}\right) T_{bc} \bar\varphi^{i} \gamma^{a} \gamma^{bc} \left(i \gamma^{d} E_{d} +N\right) \varphi_{j}\\
&- \frac{4 i}{L^{6}} L_{ik} L^{j}{}_{l} \mathcal D_{a}\!\left(L_{m}{}^{k}\right) \mathcal D_{d}\!\left(L^{ml}\right) T_{bc} \bar\varphi^{i} \gamma^{a} \gamma^{bc} \gamma^{d} \varphi_{j} +\frac{4 \left(L^{2} g + 16 N\right)}{L^{2}} \mathcal D_{a}\!\left(\bar\varphi_{i}\right) \gamma^{a} \chi^{i} - \frac{32 i \left(L^{2} g + 16 N\right)}{L^{2}} L_{i}{}^{j} \bar\chi^{i} \chi_{j} +\frac{8 i \left(L^{2} g + 16 N\right)}{L^{2}} T_{ab} \bar\varphi^{i} \gamma^{ab} \chi_{i}\\
&+\frac{4 i \left(L^{2} g + 16 N\right)}{L^{4}} L_{i}{}^{j} \bar\varphi^{i} \left(i E_{a} \gamma^{a} +N\right) \chi_{j} +\frac{4 \left(L^{2} g + 16 N\right)}{L^{4}} L_{ik} \mathcal D_{a}\!\left(L^{jk}\right) \bar\varphi^{i} \gamma^{a} \chi_{j} - \frac{i}{2 L^{2}} \widehat G_{bc} \mathcal D_{a}\!\left(\bar\varphi_{i}\right) \gamma^{a} \gamma^{bc} \gamma^{d} \mathcal D_{d}\!\left(\varphi^{i}\right) - \frac{4}{L^{2}} \widehat G_{bc} L^{ij} \mathcal D_{a}\!\left(\bar\varphi_{i}\right) \gamma^{a} \gamma^{bc} \chi_{j}\\
&+\frac{1}{L^{2}} \widehat G_{bc} T_{de} \mathcal D_{a}\!\left(\bar\varphi_{i}\right) \gamma^{a} \gamma^{bc} \gamma^{de} \varphi^{i} +\frac{1}{2 L^{4}} \widehat G_{bc} L^{ij} \mathcal D_{a}\!\left(\bar\varphi_{i}\right) \gamma^{a} \gamma^{bc} \left(i \gamma^{d} E_{d} +N\right) \varphi_{j} - \frac{i}{2 L^{4}} \widehat G_{bc} L^{j}{}_{k} \mathcal D_{d}\!\left(L^{ik}\right) \mathcal D_{a}\!\left(\bar\varphi_{i}\right) \gamma^{a} \gamma^{bc} \gamma^{d} \varphi_{j} - \frac{4}{L^{2}} \widehat G_{ab} L_{i}{}^{j} \bar\chi^{i} \gamma^{ab} \gamma^{c} \mathcal D_{c}\!\left(\varphi_{j}\right)\\
&- 16 i \widehat G_{ab} \bar\chi^{i} \gamma^{ab} \chi_{i} - \frac{8 i}{L^{2}} \widehat G_{ab} L_{i}{}^{j} T_{cd} \bar\chi^{i} \gamma^{ab} \gamma^{cd} \varphi_{j} +\frac{2 i}{L^{2}} \widehat G_{ab} \bar\chi^{i} \gamma^{ab} \left(i \gamma^{c} E_{c} +N\right) \varphi_{i} +\frac{4}{L^{4}} \widehat G_{ab} L_{ik} L^{j}{}_{l} \mathcal D_{c}\!\left(L^{kl}\right) \bar\chi^{i} \gamma^{ab} \gamma^{c} \varphi_{j}\\
&+\frac{1}{L^{2}} \widehat G_{cd} T_{ab} \bar\varphi^{i} \gamma^{ab} \gamma^{cd} \gamma^{e} \mathcal D_{e}\!\left(\varphi_{i}\right) - \frac{8 i}{L^{2}} \widehat G_{cd} L_{i}{}^{j} T_{ab} \bar\varphi^{i} \gamma^{ab} \gamma^{cd} \chi_{j} +\frac{2 i}{L^{2}} \widehat G_{cd} T_{ab} T_{ef} \bar\varphi^{i} \gamma^{ab} \gamma^{cd} \gamma^{ef} \varphi_{i} +\frac{i}{L^{4}} \widehat G_{cd} L_{i}{}^{j} T_{ab} \bar\varphi^{i} \gamma^{ab} \gamma^{cd} \left(i \gamma^{e} E_{e} +N\right) \varphi_{j}\\
&+\frac{1}{L^{4}} \widehat G_{cd} L^{j}{}_{k} \mathcal D_{e}\!\left(L_{i}{}^{k}\right) T_{ab} \bar\varphi^{i} \gamma^{ab} \gamma^{cd} \gamma^{e} \varphi_{j} +\frac{1}{2 L^{4}} \widehat G_{ab} L_{i}{}^{j} \bar\varphi^{i} \left(i E_{d} \gamma^{d} +N\right) \gamma^{ab} \gamma^{c} \mathcal D_{c}\!\left(\varphi_{j}\right) +\frac{2 i}{L^{2}} \widehat G_{ab} \bar\varphi^{i} \left(i E_{c} \gamma^{c} +N\right) \gamma^{ab} \chi_{i} +\frac{i}{L^{4}} \widehat G_{ab} L_{i}{}^{j} T_{cd} \bar\varphi^{i} \left(i E_{e} \gamma^{e} +N\right) \gamma^{ab} \gamma^{cd} \varphi_{j}\\
&- \frac{i}{4 L^{4}} \widehat G_{ab} \bar\varphi^{i} \left(i E_{c} \gamma^{c} +N\right) \gamma^{ab} \left(i \gamma^{d} E_{d} +N\right) \varphi_{i} - \frac{1}{2 L^{6}} \widehat G_{ab} L_{ik} L^{j}{}_{l} \mathcal D_{c}\!\left(L^{kl}\right) \bar\varphi^{i} \left(i E_{d} \gamma^{d} +N\right) \gamma^{ab} \gamma^{c} \varphi_{j} - \frac{i}{2 L^{4}} \widehat G_{bc} L_{ik} \mathcal D_{a}\!\left(L^{jk}\right) \bar\varphi^{i} \gamma^{a} \gamma^{bc} \gamma^{d} \mathcal D_{d}\!\left(\varphi_{j}\right) - \frac{4}{L^{4}} \widehat G_{bc} L_{ik} L^{j}{}_{l} \mathcal D_{a}\!\left(L^{lk}\right) \bar\varphi^{i} \gamma^{a} \gamma^{bc} \chi_{j}\\
&+\frac{1}{L^{4}} \widehat G_{bc} L_{ik} \mathcal D_{a}\!\left(L^{jk}\right) T_{de} \bar\varphi^{i} \gamma^{a} \gamma^{bc} \gamma^{de} \varphi_{j} +\frac{1}{2 L^{6}} \widehat G_{bc} L_{ik} L^{j}{}_{l} \mathcal D_{a}\!\left(L^{lk}\right) \bar\varphi^{i} \gamma^{a} \gamma^{bc} \left(i \gamma^{d} E_{d} +N\right) \varphi_{j} +\frac{i}{2 L^{6}} \widehat G_{bc} L_{ik} L^{j}{}_{l} \mathcal D_{a}\!\left(L_{m}{}^{k}\right) \mathcal D_{d}\!\left(L^{ml}\right) \bar\varphi^{i} \gamma^{a} \gamma^{bc} \gamma^{d} \varphi_{j} - \frac{i g}{L^{2}} L^{ij} \mathcal D_{a}\!\left(\bar\varphi_{i}\right) \gamma^{a} \gamma^{b} \mathcal D_{b}\!\left(\varphi_{j}\right)\\
&+\frac{2 g}{L^{2}} L^{ij} T_{bc} \mathcal D_{a}\!\left(\bar\varphi_{i}\right) \gamma^{a} \gamma^{bc} \varphi_{j} - \frac{g}{2 L^{2}} \mathcal D_{a}\!\left(\bar\varphi_{i}\right) \gamma^{a} \left(i \gamma^{b} E_{b} +N\right) \varphi^{i} +\frac{i g}{L^{4}} L^{i}{}_{k} L^{j}{}_{l} \mathcal D_{b}\!\left(L^{kl}\right) \mathcal D_{a}\!\left(\bar\varphi_{i}\right) \gamma^{a} \gamma^{b} \varphi_{j} +4 g \bar\chi^{i} \gamma^{a} \mathcal D_{a}\!\left(\varphi_{i}\right)\\
&+8 i g T_{ab} \bar\chi^{i} \gamma^{ab} \varphi_{i} +\frac{4 i g}{L^{2}} L_{i}{}^{j} \bar\chi^{i} \left(i \gamma^{a} E_{a} +N\right) \varphi_{j} +\frac{4 g}{L^{2}} L^{j}{}_{k} \mathcal D_{a}\!\left(L_{i}{}^{k}\right) \bar\chi^{i} \gamma^{a} \varphi_{j} +\frac{2 g}{L^{2}} L_{i}{}^{j} T_{ab} \bar\varphi^{i} \gamma^{ab} \gamma^{c} \mathcal D_{c}\!\left(\varphi_{j}\right)\\
&+\frac{4 i g}{L^{2}} L_{i}{}^{j} T_{ab} T_{cd} \bar\varphi^{i} \gamma^{ab} \gamma^{cd} \varphi_{j} - \frac{i g}{L^{2}} T_{ab} \bar\varphi^{i} \gamma^{ab} \left(i \gamma^{c} E_{c} +N\right) \varphi_{i} - \frac{2 g}{L^{4}} L_{ik} L^{j}{}_{l} \mathcal D_{c}\!\left(L^{kl}\right) T_{ab} \bar\varphi^{i} \gamma^{ab} \gamma^{c} \varphi_{j} - \frac{g}{2 L^{2}} \bar\varphi^{i} \left(i E_{b} \gamma^{b} +N\right) \gamma^{a} \mathcal D_{a}\!\left(\varphi_{i}\right)\\
&- \frac{i g}{L^{2}} T_{ab} \bar\varphi^{i} \left(i E_{c} \gamma^{c} +N\right) \gamma^{ab} \varphi_{i} - \frac{i g}{2 L^{4}} L_{i}{}^{j} \bar\varphi^{i} \left(i E_{a} \gamma^{a} +N\right) \left(i \gamma^{b} E_{b} +N\right) \varphi_{j} - \frac{g}{2 L^{4}} L^{j}{}_{k} \mathcal D_{a}\!\left(L_{i}{}^{k}\right) \bar\varphi^{i} \left(i E_{b} \gamma^{b} +N\right) \gamma^{a} \varphi_{j} - \frac{i g}{L^{4}} L_{ik} L^{j}{}_{l} \mathcal D_{a}\!\left(L^{lk}\right) \bar\varphi^{i} \gamma^{a} \gamma^{b} \mathcal D_{b}\!\left(\varphi_{j}\right)\\
&+\frac{2 g}{L^{4}} L_{ik} L^{j}{}_{l} \mathcal D_{a}\!\left(L^{lk}\right) T_{bc} \bar\varphi^{i} \gamma^{a} \gamma^{bc} \varphi_{j} - \frac{g}{2 L^{4}} L_{ik} \mathcal D_{a}\!\left(L^{jk}\right) \bar\varphi^{i} \gamma^{a} \left(i \gamma^{b} E_{b} +N\right) \varphi_{j} +\frac{i g}{L^{6}} L_{ik} L^{j}{}_{l} L_{mn} \mathcal D_{a}\!\left(L^{mk}\right) \mathcal D_{b}\!\left(L^{nl}\right) \bar\varphi^{i} \gamma^{a} \gamma^{b} \varphi_{j} +\frac{3 i N g}{2 L^{2}} L_{i}{}^{j} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{b} \mathcal D_{b}\!\left(\varphi_{j}\right)\\
&- \frac{2 N \left(3 L^{2} g + 10 N\right)}{L^{2}} \bar\psi_{a}{}^{i} \gamma^{a} \chi_{i} - \frac{3 N g}{L^{2}} L_{i}{}^{j} T_{bc} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{bc} \varphi_{j} +\frac{3 N g}{4 L^{2}} \bar\psi_{a}{}^{i} \gamma^{a} \left(i \gamma^{b} E_{b} +N\right) \varphi_{i} - \frac{3 i N g}{2 L^{4}} L_{ik} L^{j}{}_{l} \mathcal D_{b}\!\left(L^{kl}\right) \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{b} \varphi_{j}\\
&- \frac{i}{L^{2}} \Box_c\!\left(L_{i}{}^{j}\right) \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{b} \mathcal D_{b}\!\left(\varphi_{j}\right) +\frac{i}{L^{3}} \mathcal D_{c}\!\left(L\right) \mathcal D^{c}\!\left(L_{i}{}^{j}\right) \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{b} \mathcal D_{b}\!\left(\varphi_{j}\right) - \frac{i}{L^{2}} \left(4 D +\frac{8}{3} T_{cd} T^{cd} - \frac{1}{L^{2}} E_{c} E^{c} - \frac{N^{2}}{L^{2}} +\frac{1}{2 L^{2}} \mathcal D_{c}\!\left(L_{kl}\right) \mathcal D^{c}\!\left(L^{kl}\right)\right) L_{i}{}^{j} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{b} \mathcal D_{b}\!\left(\varphi_{j}\right) - \frac{2 i}{L^{4}} E_{c} \varepsilon^{jk}\left(L_{l(i} \mathcal D^{c}\!\left(L_{k)}{}^{l}\right)\right) \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{b} \mathcal D_{b}\!\left(\varphi_{j}\right)\\
&- \frac{8}{L^{2}} L^{j}{}_{k} \Box_c\!\left(L_{i}{}^{k}\right) \bar\psi_{a}{}^{i} \gamma^{a} \chi_{j} +\frac{8}{L^{3}} L^{j}{}_{k} \mathcal D_{b}\!\left(L\right) \mathcal D^{b}\!\left(L_{i}{}^{k}\right) \bar\psi_{a}{}^{i} \gamma^{a} \chi_{j} +4 \left(4 D +\frac{8}{3} T_{bc} T^{bc} - \frac{1}{L^{2}} E_{b} E^{b} - \frac{N^{2}}{L^{2}} +\frac{1}{2 L^{2}} \mathcal D_{b}\!\left(L_{jk}\right) \mathcal D^{b}\!\left(L^{jk}\right)\right) \bar\psi_{a}{}^{i} \gamma^{a} \chi_{i} +\frac{16}{L^{4}} E_{b} \left(L_{l(i} \mathcal D^{b}\!\left(L_{k)}{}^{l}\right)\right) L^{jk} \bar\psi_{a}{}^{i} \gamma^{a} \chi_{j}\\
&+\frac{2}{L^{2}} \Box_c\!\left(L_{i}{}^{j}\right) T_{bc} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{bc} \varphi_{j} - \frac{2}{L^{3}} \mathcal D_{d}\!\left(L\right) \mathcal D^{d}\!\left(L_{i}{}^{j}\right) T_{bc} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{bc} \varphi_{j} +\frac{2}{L^{2}} \left(4 D +\frac{8}{3} T_{de} T^{de} - \frac{1}{L^{2}} E_{d} E^{d} - \frac{N^{2}}{L^{2}} +\frac{1}{2 L^{2}} \mathcal D_{d}\!\left(L_{kl}\right) \mathcal D^{d}\!\left(L^{kl}\right)\right) L_{i}{}^{j} T_{bc} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{bc} \varphi_{j} +\frac{4}{L^{4}} E_{d} \varepsilon^{jk}\left(L_{l(i} \mathcal D^{d}\!\left(L_{k)}{}^{l}\right)\right) T_{bc} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{bc} \varphi_{j}\\
&+\frac{1}{L^{4}} L^{j}{}_{k} \Box_c\!\left(L_{i}{}^{k}\right) \bar\psi_{a}{}^{i} \gamma^{a} \left(i \gamma^{b} E_{b} +N\right) \varphi_{j} - \frac{1}{L^{5}} L^{j}{}_{k} \mathcal D_{b}\!\left(L\right) \mathcal D^{b}\!\left(L_{i}{}^{k}\right) \bar\psi_{a}{}^{i} \gamma^{a} \left(i \gamma^{c} E_{c} +N\right) \varphi_{j} - \frac{1}{2 L^{2}} \left(4 D +\frac{8}{3} T_{bc} T^{bc} - \frac{1}{L^{2}} E_{b} E^{b} - \frac{N^{2}}{L^{2}} +\frac{1}{2 L^{2}} \mathcal D_{b}\!\left(L_{jk}\right) \mathcal D^{b}\!\left(L^{jk}\right)\right) \bar\psi_{a}{}^{i} \gamma^{a} \left(i \gamma^{d} E_{d} +N\right) \varphi_{i} - \frac{2}{L^{6}} E_{b} \left(L_{l(i} \mathcal D^{b}\!\left(L_{k)}{}^{l}\right)\right) L^{jk} \bar\psi_{a}{}^{i} \gamma^{a} \left(i \gamma^{c} E_{c} +N\right) \varphi_{j}\\
&+\frac{i}{L^{4}} L^{j}{}_{k} \Box_c\!\left(L_{il}\right) \mathcal D_{b}\!\left(L^{lk}\right) \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{b} \varphi_{j} +\frac{i}{L^{5}} L^{j}{}_{k} \mathcal D_{c}\!\left(L\right) \mathcal D_{b}\!\left(L_{l}{}^{k}\right) \mathcal D^{c}\!\left(L_{i}{}^{l}\right) \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{b} \varphi_{j} +\frac{i}{L^{4}} \left(4 D +\frac{8}{3} T_{cd} T^{cd} - \frac{1}{L^{2}} E_{c} E^{c} - \frac{N^{2}}{L^{2}} +\frac{1}{2 L^{2}} \mathcal D_{c}\!\left(L_{mn}\right) \mathcal D^{c}\!\left(L^{mn}\right)\right) L_{ik} L^{j}{}_{l} \mathcal D_{b}\!\left(L^{kl}\right) \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{b} \varphi_{j} +\frac{2 i}{L^{6}} E_{c} \left(L_{m(i} \mathcal D^{c}\!\left(L_{k)}{}^{m}\right)\right) L^{j}{}_{l} \mathcal D_{b}\!\left(L^{kl}\right) \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{b} \varphi_{j}\\
&- \frac{3 i N}{4 L^{2}} \widehat G_{cd} \mathcal D_{a}\!\left(\bar\varphi_{i}\right) \gamma^{a} \gamma^{b} \gamma^{cd} \psi_{b}{}^{i} - \frac{6 N}{L^{2}} \widehat G_{bc} L_{i}{}^{j} \bar\chi^{i} \gamma^{a} \gamma^{bc} \psi_{aj} +\frac{3 N}{2 L^{2}} \widehat G_{de} T_{ab} \bar\varphi^{i} \gamma^{ab} \gamma^{c} \gamma^{de} \psi_{ci} +\frac{3 N}{4 L^{4}} \widehat G_{bc} L_{i}{}^{j} \bar\varphi^{i} \left(i E_{d} \gamma^{d} +N\right) \gamma^{a} \gamma^{bc} \psi_{aj}\\
&- \frac{3 i N}{4 L^{4}} \widehat G_{cd} L_{ik} \mathcal D_{a}\!\left(L^{jk}\right) \bar\varphi^{i} \gamma^{a} \gamma^{b} \gamma^{cd} \psi_{bj} +\frac{3 i N}{L^{2}} T_{cd} \mathcal D_{a}\!\left(\bar\varphi_{i}\right) \gamma^{a} \gamma^{b} \gamma^{cd} \psi_{b}{}^{i} +\frac{24 N}{L^{2}} L_{i}{}^{j} T_{bc} \bar\chi^{i} \gamma^{a} \gamma^{bc} \psi_{aj} - \frac{6 N}{L^{2}} T_{ab} T_{de} \bar\varphi^{i} \gamma^{ab} \gamma^{c} \gamma^{de} \psi_{ci}\\
&- \frac{3 N}{L^{4}} L_{i}{}^{j} T_{bc} \bar\varphi^{i} \left(i E_{d} \gamma^{d} +N\right) \gamma^{a} \gamma^{bc} \psi_{aj} +\frac{3 i N}{L^{4}} L_{ik} \mathcal D_{a}\!\left(L^{jk}\right) T_{cd} \bar\varphi^{i} \gamma^{a} \gamma^{b} \gamma^{cd} \psi_{bj} +\frac{3 i N g}{2 L^{2}} L^{ij} \mathcal D_{a}\!\left(\bar\varphi_{i}\right) \gamma^{a} \gamma^{b} \psi_{bj} - 6 N g \bar\chi^{i} \gamma^{a} \psi_{ai}\\
&- \frac{3 N g}{L^{2}} L_{i}{}^{j} T_{ab} \bar\varphi^{i} \gamma^{ab} \gamma^{c} \psi_{cj} +\frac{3 N g}{4 L^{2}} \bar\varphi^{i} \left(i E_{b} \gamma^{b} +N\right) \gamma^{a} \psi_{ai} +\frac{3 i N g}{2 L^{4}} L_{ik} L^{j}{}_{l} \mathcal D_{a}\!\left(L^{lk}\right) \bar\varphi^{i} \gamma^{a} \gamma^{b} \psi_{bj} +\frac{3 i N}{L^{2}} \mathcal D_{a}\!\left(\bar\varphi_{i}\right) \gamma^{a} \gamma^{b} \phi_{b}{}^{i}\\
&+\frac{24 N}{L^{2}} L_{i}{}^{j} \bar\chi^{i} \gamma^{a} \phi_{aj} - \frac{6 N}{L^{2}} T_{ab} \bar\varphi^{i} \gamma^{ab} \gamma^{c} \phi_{ci} - \frac{3 N}{L^{4}} L_{i}{}^{j} \bar\varphi^{i} \left(i E_{b} \gamma^{b} +N\right) \gamma^{a} \phi_{aj} +\frac{3 i N}{L^{4}} L_{ik} \mathcal D_{a}\!\left(L^{jk}\right) \bar\varphi^{i} \gamma^{a} \gamma^{b} \phi_{bj}\\
&- \frac{1}{L} E_{a} \mathcal D_{b}\!\left(\left(4 \left(\mathcal D^{[a}\!\left(\frac{1}{L} E^{b]}\right)\right) +\frac{2}{L} L_{ij} \widehat R(V)^{abij} - \frac{2}{L^{3}} L_{i}{}^{j} \left(\mathcal D^{[a}\!\left(L^{ik}\right) \mathcal D^{b]}\!\left(L_{jk}\right)\right) +\frac{2 N}{L} \left(\widehat G^{ab} -16 T^{ab}\right)\right)\right) - \frac{1}{L} E^{b} \mathcal D_{a}\!\left(\left(-2 \eta^{ac}\left(\mathcal D_{[b}\!\left(\frac{1}{L^{3}} L_{mn} \bar\varphi^{m} \gamma_{c]} \varphi^{n}\right)\right) - \frac{i}{L} \bar\varphi^{i} \widehat R(Q)_{b}{}^{a}{}_{i} +\frac{i}{L^{3}} L_{ij} \bar\varphi^{i} \varphi^{j} \left(\widehat G_{b}{}^{a} -16 T_{b}{}^{a}\right)\right)\right) - \frac{\sqrt{2}}{2} \mathcal D_{a}\!\left(\left(4 \eta^{ac}\left(\mathcal D_{[b}\!\left(\frac{1}{L} E_{c]}\right)\right) +\frac{2}{L} L_{ij} \widehat R(V)_{b}{}^{aij} - \frac{2}{L^{3}} L_{i}{}^{j} \eta^{ad}\left(\mathcal D_{[b}\!\left(L^{ik}\right) \mathcal D_{d]}\!\left(L_{jk}\right)\right) +\frac{2 N}{L} \left(\widehat G_{b}{}^{a} -16 T_{b}{}^{a}\right)\right)\right) V^{b} - \frac{\sqrt{2}}{2} V^{b} \mathcal D_{a}\!\left(\left(-2 \eta^{ac}\left(\mathcal D_{[b}\!\left(\frac{1}{L^{3}} L_{mn} \bar\varphi^{m} \gamma_{c]} \varphi^{n}\right)\right) - \frac{i}{L} \bar\varphi^{i} \widehat R(Q)_{b}{}^{a}{}_{i} +\frac{i}{L^{3}} L_{ij} \bar\varphi^{i} \varphi^{j} \left(\widehat G_{b}{}^{a} -16 T_{b}{}^{a}\right)\right)\right)\\
&- \frac{1}{2 L^{3}} L_{i}{}^{j} \mathcal D_{b}\!\left(\left(4 \eta^{bc}\left(\mathcal D_{[a}\!\left(\frac{1}{L} E_{c]}\right)\right) +\frac{2}{L} L_{kl} \widehat R(V)_{a}{}^{bkl} - \frac{2}{L^{3}} L_{k}{}^{l} \eta^{bd}\left(\mathcal D_{[a}\!\left(L^{km}\right) \mathcal D_{d]}\!\left(L_{lm}\right)\right) +\frac{2 N}{L} \left(\widehat G_{a}{}^{b} -16 T_{a}{}^{b}\right)\right)\right) \bar\varphi^{i} \gamma^{a} \varphi_{j} +\frac{i}{2 L} \mathcal D_{b}\!\left(\left(4 \left(\mathcal D^{[a}\!\left(\frac{1}{L} E^{b]}\right)\right) +\frac{2}{L} L_{jk} \widehat R(V)^{abjk} - \frac{2}{L^{3}} L_{j}{}^{k} \left(\mathcal D^{[a}\!\left(L^{jl}\right) \mathcal D^{b]}\!\left(L_{kl}\right)\right) +\frac{2 N}{L} \left(\widehat G^{ab} -16 T^{ab}\right)\right)\right) \bar\varphi^{i} \psi_{ai} - \frac{1}{L} E_{a} \widehat G_{bc} \left(\mathcal D_{[d}\!\left(\frac{1}{L} E_{e]}\right)\right) \varepsilon^{abcde} - \frac{1}{2 L^{2}} E_{a} \widehat G_{bc} L_{ij} \widehat R(V)_{de}{}^{ij} \varepsilon^{abcde}\\
&- \frac{1}{2 L^{4}} E_{a} \widehat G_{bc} \left(\mathcal D_{[d}\!\left(L_{i}{}^{k}\right) \mathcal D_{e]}\!\left(L_{jk}\right)\right) L^{ij} \varepsilon^{abcde} +\frac{1}{2 L} E_{c} \widehat G_{de} \varepsilon^{abcde} \left(\mathcal D_{[a}\!\left(\frac{1}{L^{3}} L_{kl} \bar\varphi^{k} \gamma_{b]} \varphi^{l}\right)\right) +\frac{i}{4 L^{2}} E_{c} \widehat G_{de} \varepsilon^{abcde} \bar\varphi^{i} \widehat R(Q)_{abi} - \frac{\sqrt{2}}{2} \widehat G_{ab} \left(\mathcal D_{[c}\!\left(\frac{1}{L} E_{d]}\right)\right) V_{e} \varepsilon^{abcde}\\
&- \frac{\sqrt{2}}{4 L} \widehat G_{ab} L_{ij} \widehat R(V)_{cd}{}^{ij} V_{e} \varepsilon^{abcde} - \frac{\sqrt{2}}{4 L^{3}} \widehat G_{ab} \left(\mathcal D_{[c}\!\left(L_{i}{}^{k}\right) \mathcal D_{d]}\!\left(L_{jk}\right)\right) L^{ij} V_{e} \varepsilon^{abcde} +\frac{\sqrt{2}}{4} \widehat G_{cd} V_{e} \varepsilon^{abcde} \left(\mathcal D_{[a}\!\left(\frac{1}{L^{3}} L_{kl} \bar\varphi^{k} \gamma_{b]} \varphi^{l}\right)\right) +\frac{\sqrt{2} i}{8 L} \widehat G_{cd} V_{e} \varepsilon^{abcde} \bar\varphi^{i} \widehat R(Q)_{abi}\\
&- \frac{1}{2 L^{3}} \widehat G_{bc} \left(\mathcal D_{[d}\!\left(\frac{1}{L} E_{e]}\right)\right) L_{i}{}^{j} \varepsilon_{a}{}^{bcde} \bar\varphi^{i} \gamma^{a} \varphi_{j} - \frac{1}{4 L^{4}} \widehat G_{bc} L_{i}{}^{j} L_{kl} \widehat R(V)_{de}{}^{kl} \varepsilon_{a}{}^{bcde} \bar\varphi^{i} \gamma^{a} \varphi_{j} - \frac{1}{4 L^{6}} \widehat G_{bc} \left(\mathcal D_{[d}\!\left(L_{k}{}^{m}\right) \mathcal D_{e]}\!\left(L_{lm}\right)\right) L_{i}{}^{j} L^{kl} \varepsilon_{a}{}^{bcde} \bar\varphi^{i} \gamma^{a} \varphi_{j} +\frac{i}{2 L} \widehat G_{bc} \left(\mathcal D_{[d}\!\left(\frac{1}{L} E_{e]}\right)\right) \varepsilon^{abcde} \bar\varphi^{i} \psi_{ai}\\
&+\frac{i}{4 L^{2}} \widehat G_{bc} L_{jk} \widehat R(V)_{de}{}^{jk} \varepsilon^{abcde} \bar\varphi^{i} \psi_{ai} +\frac{i}{4 L^{4}} \widehat G_{bc} \left(\mathcal D_{[d}\!\left(L_{j}{}^{l}\right) \mathcal D_{e]}\!\left(L_{kl}\right)\right) L^{jk} \varepsilon^{abcde} \bar\varphi^{i} \psi_{ai} +\frac{1}{4 L^{2}} E_{b} \widehat G_{de} \mathcal D_{a}\!\left(\bar\varphi_{i}\right) \gamma^{a} \gamma^{bc} \gamma^{de} \psi_{c}{}^{i} - \frac{2 i}{L^{2}} E_{a} \widehat G_{cd} L_{i}{}^{j} \bar\chi^{i} \gamma^{ab} \gamma^{cd} \psi_{bj}\\
&+\frac{i}{2 L^{2}} E_{c} \widehat G_{ef} T_{ab} \bar\varphi^{i} \gamma^{ab} \gamma^{cd} \gamma^{ef} \psi_{di} +\frac{i}{4 L^{4}} E_{a} \widehat G_{cd} L_{i}{}^{j} \bar\varphi^{i} \left(i E_{e} \gamma^{e} +N\right) \gamma^{ab} \gamma^{cd} \psi_{bj} +\frac{1}{4 L^{4}} E_{b} \widehat G_{de} L_{ik} \mathcal D_{a}\!\left(L^{jk}\right) \bar\varphi^{i} \gamma^{a} \gamma^{bc} \gamma^{de} \psi_{cj} +\frac{\sqrt{2}}{8 L} \widehat G_{de} V_{b} \mathcal D_{a}\!\left(\bar\varphi_{i}\right) \gamma^{a} \gamma^{bc} \gamma^{de} \psi_{c}{}^{i}\\
&- \frac{\sqrt{2} i}{L} \widehat G_{cd} L_{i}{}^{j} V_{a} \bar\chi^{i} \gamma^{ab} \gamma^{cd} \psi_{bj} +\frac{\sqrt{2} i}{4 L} \widehat G_{ef} T_{ab} V_{c} \bar\varphi^{i} \gamma^{ab} \gamma^{cd} \gamma^{ef} \psi_{di} +\frac{\sqrt{2} i}{8 L^{3}} \widehat G_{cd} L_{i}{}^{j} V_{a} \bar\varphi^{i} \left(i E_{e} \gamma^{e} +N\right) \gamma^{ab} \gamma^{cd} \psi_{bj} +\frac{\sqrt{2}}{8 L^{3}} \widehat G_{de} L_{ik} \mathcal D_{a}\!\left(L^{jk}\right) V_{b} \bar\varphi^{i} \gamma^{a} \gamma^{bc} \gamma^{de} \psi_{cj}\\
&- \frac{1}{L^{2}} E_{b} T_{de} \mathcal D_{a}\!\left(\bar\varphi_{i}\right) \gamma^{a} \gamma^{bc} \gamma^{de} \psi_{c}{}^{i} +\frac{8 i}{L^{2}} E_{a} L_{i}{}^{j} T_{cd} \bar\chi^{i} \gamma^{ab} \gamma^{cd} \psi_{bj} - \frac{2 i}{L^{2}} E_{c} T_{ab} T_{ef} \bar\varphi^{i} \gamma^{ab} \gamma^{cd} \gamma^{ef} \psi_{di} - \frac{i}{L^{4}} E_{a} L_{i}{}^{j} T_{cd} \bar\varphi^{i} \left(i E_{e} \gamma^{e} +N\right) \gamma^{ab} \gamma^{cd} \psi_{bj}\\
&- \frac{1}{L^{4}} E_{b} L_{ik} \mathcal D_{a}\!\left(L^{jk}\right) T_{de} \bar\varphi^{i} \gamma^{a} \gamma^{bc} \gamma^{de} \psi_{cj} - \frac{\sqrt{2}}{2 L} T_{de} V_{b} \mathcal D_{a}\!\left(\bar\varphi_{i}\right) \gamma^{a} \gamma^{bc} \gamma^{de} \psi_{c}{}^{i} +\frac{4 \sqrt{2} i}{L} L_{i}{}^{j} T_{cd} V_{a} \bar\chi^{i} \gamma^{ab} \gamma^{cd} \psi_{bj} - \frac{\sqrt{2} i}{L} T_{ab} T_{ef} V_{c} \bar\varphi^{i} \gamma^{ab} \gamma^{cd} \gamma^{ef} \psi_{di}\\
&- \frac{\sqrt{2} i}{2 L^{3}} L_{i}{}^{j} T_{cd} V_{a} \bar\varphi^{i} \left(i E_{e} \gamma^{e} +N\right) \gamma^{ab} \gamma^{cd} \psi_{bj} - \frac{\sqrt{2}}{2 L^{3}} L_{ik} \mathcal D_{a}\!\left(L^{jk}\right) T_{de} V_{b} \bar\varphi^{i} \gamma^{a} \gamma^{bc} \gamma^{de} \psi_{cj} - \frac{g}{2 L^{2}} E_{b} L^{ij} \mathcal D_{a}\!\left(\bar\varphi_{i}\right) \gamma^{a} \gamma^{bc} \psi_{cj} - 2 i g E_{a} \bar\chi^{i} \gamma^{ab} \psi_{bi}\\
&- \frac{i g}{L^{2}} E_{c} L_{i}{}^{j} T_{ab} \bar\varphi^{i} \gamma^{ab} \gamma^{cd} \psi_{dj} +\frac{i g}{4 L^{2}} E_{a} \bar\varphi^{i} \left(i E_{c} \gamma^{c} +N\right) \gamma^{ab} \psi_{bi} - \frac{g}{2 L^{4}} E_{b} L_{ik} L^{j}{}_{l} \mathcal D_{a}\!\left(L^{lk}\right) \bar\varphi^{i} \gamma^{a} \gamma^{bc} \psi_{cj} - \frac{\sqrt{2} g}{4 L} L^{ij} V_{b} \mathcal D_{a}\!\left(\bar\varphi_{i}\right) \gamma^{a} \gamma^{bc} \psi_{cj}\\
&- \sqrt{2} i L g V_{a} \bar\chi^{i} \gamma^{ab} \psi_{bi} - \frac{\sqrt{2} i g}{2 L} L_{i}{}^{j} T_{ab} V_{c} \bar\varphi^{i} \gamma^{ab} \gamma^{cd} \psi_{dj} +\frac{\sqrt{2} i g}{8 L} V_{a} \bar\varphi^{i} \left(i E_{c} \gamma^{c} +N\right) \gamma^{ab} \psi_{bi} - \frac{\sqrt{2} g}{4 L^{3}} L_{ik} L^{j}{}_{l} \mathcal D_{a}\!\left(L^{lk}\right) V_{b} \bar\varphi^{i} \gamma^{a} \gamma^{bc} \psi_{cj}\\
&- \frac{1}{L^{2}} E_{b} \mathcal D_{a}\!\left(\bar\varphi_{i}\right) \gamma^{a} \gamma^{bc} \phi_{c}{}^{i} +\frac{8 i}{L^{2}} E_{a} L_{i}{}^{j} \bar\chi^{i} \gamma^{ab} \phi_{bj} - \frac{2 i}{L^{2}} E_{c} T_{ab} \bar\varphi^{i} \gamma^{ab} \gamma^{cd} \phi_{di} - \frac{i}{L^{4}} E_{a} L_{i}{}^{j} \bar\varphi^{i} \left(i E_{c} \gamma^{c} +N\right) \gamma^{ab} \phi_{bj}\\
&- \frac{1}{L^{4}} E_{b} L_{ik} \mathcal D_{a}\!\left(L^{jk}\right) \bar\varphi^{i} \gamma^{a} \gamma^{bc} \phi_{cj} - \frac{\sqrt{2}}{2 L} V_{b} \mathcal D_{a}\!\left(\bar\varphi_{i}\right) \gamma^{a} \gamma^{bc} \phi_{c}{}^{i} +\frac{4 \sqrt{2} i}{L} L_{i}{}^{j} V_{a} \bar\chi^{i} \gamma^{ab} \phi_{bj} - \frac{\sqrt{2} i}{L} T_{ab} V_{c} \bar\varphi^{i} \gamma^{ab} \gamma^{cd} \phi_{di}\\
&- \frac{\sqrt{2} i}{2 L^{3}} L_{i}{}^{j} V_{a} \bar\varphi^{i} \left(i E_{c} \gamma^{c} +N\right) \gamma^{ab} \phi_{bj} - \frac{\sqrt{2}}{2 L^{3}} L_{ik} \mathcal D_{a}\!\left(L^{jk}\right) V_{b} \bar\varphi^{i} \gamma^{a} \gamma^{bc} \phi_{cj} - \frac{N}{4 L^{2}} E_{b} \widehat G_{de} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{c} \gamma^{de} \psi_{ci} - \frac{\sqrt{2} N}{8 L} \widehat G_{de} V_{b} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{c} \gamma^{de} \psi_{ci}\\
&+\frac{N}{L^{2}} E_{b} T_{de} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{c} \gamma^{de} \psi_{ci} +\frac{\sqrt{2} N}{2 L} T_{de} V_{b} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{c} \gamma^{de} \psi_{ci} +\frac{N g}{2 L^{2}} E_{b} L_{i}{}^{j} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{c} \psi_{cj} +\frac{\sqrt{2} N g}{4 L} L_{i}{}^{j} V_{b} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{c} \psi_{cj}\\
&+\frac{N}{L^{2}} E_{b} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{c} \phi_{ci} +\frac{\sqrt{2} N}{2 L} V_{b} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{c} \phi_{ci} +\frac{i}{L} E_{b} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{c} \mathcal D_{c}\!\left(\frac{1}{L} \gamma^{d} \mathcal D_{d}\!\left(\varphi_{i}\right)\right) - \frac{8}{L} E_{b} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{c} \mathcal D_{c}\!\left(\frac{1}{L} L_{ij} \chi^{j}\right)\\
&- \frac{2}{L} E_{b} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{c} \mathcal D_{c}\!\left(\frac{1}{L} \gamma^{de} T_{de} \varphi_{i}\right) +\frac{1}{L} E_{b} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{c} \mathcal D_{c}\!\left(\frac{1}{L^{3}} L_{ij} \left(i \gamma^{d} E_{d} +N\right) \varphi^{j}\right) - \frac{i}{L} E_{b} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{c} \mathcal D_{c}\!\left(\frac{1}{L^{3}} \gamma^{d} \mathcal D_{d}\!\left(L_{ij}\right) L^{jk} \varphi_{k}\right) +\frac{\sqrt{2} i}{2} V_{b} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{c} \mathcal D_{c}\!\left(\frac{1}{L} \gamma^{d} \mathcal D_{d}\!\left(\varphi_{i}\right)\right)\\
&- 4 \sqrt{2} V_{b} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{c} \mathcal D_{c}\!\left(\frac{1}{L} L_{ij} \chi^{j}\right) - \sqrt{2} V_{b} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{c} \mathcal D_{c}\!\left(\frac{1}{L} \gamma^{de} T_{de} \varphi_{i}\right) +\frac{\sqrt{2}}{2} V_{b} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{c} \mathcal D_{c}\!\left(\frac{1}{L^{3}} L_{ij} \left(i \gamma^{d} E_{d} +N\right) \varphi^{j}\right) - \frac{\sqrt{2} i}{2} V_{b} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{c} \mathcal D_{c}\!\left(\frac{1}{L^{3}} \gamma^{d} \mathcal D_{d}\!\left(L_{ij}\right) L^{jk} \varphi_{k}\right)\\
&+\frac{2}{L^{2}} E_{b} T_{cd} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{cd} \gamma^{e} \mathcal D_{e}\!\left(\varphi_{i}\right) - \frac{16 i}{L^{2}} E_{b} L_{i}{}^{j} T_{cd} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{cd} \chi_{j} +\frac{4 i}{L^{2}} E_{b} T_{cd} T_{ef} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{cd} \gamma^{ef} \varphi_{i} +\frac{2 i}{L^{4}} E_{b} L_{i}{}^{j} T_{cd} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{cd} \left(i \gamma^{e} E_{e} +N\right) \varphi_{j}\\
&+\frac{2}{L^{4}} E_{b} L^{j}{}_{k} \mathcal D_{e}\!\left(L_{i}{}^{k}\right) T_{cd} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{cd} \gamma^{e} \varphi_{j} +\frac{\sqrt{2}}{L} T_{cd} V_{b} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{cd} \gamma^{e} \mathcal D_{e}\!\left(\varphi_{i}\right) - \frac{8 \sqrt{2} i}{L} L_{i}{}^{j} T_{cd} V_{b} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{cd} \chi_{j} +\frac{2 \sqrt{2} i}{L} T_{cd} T_{ef} V_{b} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{cd} \gamma^{ef} \varphi_{i}\\
&+\frac{\sqrt{2} i}{L^{3}} L_{i}{}^{j} T_{cd} V_{b} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{cd} \left(i \gamma^{e} E_{e} +N\right) \varphi_{j} +\frac{\sqrt{2}}{L^{3}} L^{j}{}_{k} \mathcal D_{e}\!\left(L_{i}{}^{k}\right) T_{cd} V_{b} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{cd} \gamma^{e} \varphi_{j} - \frac{2 i \left(L^{2} g + 8 N\right)}{L^{2}} E_{b} \bar\psi_{a}{}^{i} \gamma^{ab} \chi_{i} - \frac{\sqrt{2} i \left(L^{2} g + 8 N\right)}{L} V_{b} \bar\psi_{a}{}^{i} \gamma^{ab} \chi_{i}\\
&- \frac{1}{4 L^{2}} E_{b} \widehat G_{cd} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{cd} \gamma^{e} \mathcal D_{e}\!\left(\varphi_{i}\right) +\frac{2 i}{L^{2}} E_{b} \widehat G_{cd} L_{i}{}^{j} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{cd} \chi_{j} - \frac{i}{2 L^{2}} E_{b} \widehat G_{cd} T_{ef} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{cd} \gamma^{ef} \varphi_{i} - \frac{i}{4 L^{4}} E_{b} \widehat G_{cd} L_{i}{}^{j} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{cd} \left(i \gamma^{e} E_{e} +N\right) \varphi_{j}\\
&- \frac{1}{4 L^{4}} E_{b} \widehat G_{cd} L^{j}{}_{k} \mathcal D_{e}\!\left(L_{i}{}^{k}\right) \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{cd} \gamma^{e} \varphi_{j} - \frac{\sqrt{2}}{8 L} \widehat G_{cd} V_{b} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{cd} \gamma^{e} \mathcal D_{e}\!\left(\varphi_{i}\right) +\frac{\sqrt{2} i}{L} \widehat G_{cd} L_{i}{}^{j} V_{b} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{cd} \chi_{j} - \frac{\sqrt{2} i}{4 L} \widehat G_{cd} T_{ef} V_{b} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{cd} \gamma^{ef} \varphi_{i}\\
&- \frac{\sqrt{2} i}{8 L^{3}} \widehat G_{cd} L_{i}{}^{j} V_{b} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{cd} \left(i \gamma^{e} E_{e} +N\right) \varphi_{j} - \frac{\sqrt{2}}{8 L^{3}} \widehat G_{cd} L^{j}{}_{k} \mathcal D_{e}\!\left(L_{i}{}^{k}\right) V_{b} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{cd} \gamma^{e} \varphi_{j} - \frac{g}{2 L^{2}} E_{b} L_{i}{}^{j} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{c} \mathcal D_{c}\!\left(\varphi_{j}\right) - \frac{i g}{L^{2}} E_{b} L_{i}{}^{j} T_{cd} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{cd} \varphi_{j}\\
&+\frac{i g}{4 L^{2}} E_{b} \bar\psi_{a}{}^{i} \gamma^{ab} \left(i \gamma^{c} E_{c} +N\right) \varphi_{i} +\frac{g}{2 L^{4}} E_{b} L_{ik} L^{j}{}_{l} \mathcal D_{c}\!\left(L^{kl}\right) \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{c} \varphi_{j} - \frac{\sqrt{2} g}{4 L} L_{i}{}^{j} V_{b} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{c} \mathcal D_{c}\!\left(\varphi_{j}\right) - \frac{\sqrt{2} i g}{2 L} L_{i}{}^{j} T_{cd} V_{b} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{cd} \varphi_{j}\\
&+\frac{\sqrt{2} i g}{8 L} V_{b} \bar\psi_{a}{}^{i} \gamma^{ab} \left(i \gamma^{c} E_{c} +N\right) \varphi_{i} +\frac{\sqrt{2} g}{4 L^{3}} L_{ik} L^{j}{}_{l} \mathcal D_{c}\!\left(L^{kl}\right) V_{b} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{c} \varphi_{j} - \frac{N g}{2 L^{2}} E_{b} L_{i}{}^{j} \bar\psi_{a}{}^{i} \gamma^{abc} \psi_{cj} - \frac{\sqrt{2} N g}{4 L} L_{i}{}^{j} V_{b} \bar\psi_{a}{}^{i} \gamma^{abc} \psi_{cj}\\
&+\frac{1}{2 L^{2}} E_{b} \Box_c\!\left(L_{i}{}^{j}\right) \bar\psi_{a}{}^{i} \gamma^{abc} \psi_{cj} - \frac{1}{2 L^{3}} E_{b} \mathcal D_{d}\!\left(L\right) \mathcal D^{d}\!\left(L_{i}{}^{j}\right) \bar\psi_{a}{}^{i} \gamma^{abc} \psi_{cj} +\frac{1}{2 L^{2}} E_{b} \left(4 D +\frac{8}{3} T_{de} T^{de} - \frac{1}{L^{2}} E_{d} E^{d} - \frac{N^{2}}{L^{2}} +\frac{1}{2 L^{2}} \mathcal D_{d}\!\left(L_{kl}\right) \mathcal D^{d}\!\left(L^{kl}\right)\right) L_{i}{}^{j} \bar\psi_{a}{}^{i} \gamma^{abc} \psi_{cj} +\frac{1}{L^{4}} E_{b} E_{d} \varepsilon^{jk}\left(L_{l(i} \mathcal D^{d}\!\left(L_{k)}{}^{l}\right)\right) \bar\psi_{a}{}^{i} \gamma^{abc} \psi_{cj}\\
&+\frac{\sqrt{2}}{4 L} \Box_c\!\left(L_{i}{}^{j}\right) V_{b} \bar\psi_{a}{}^{i} \gamma^{abc} \psi_{cj} - \frac{\sqrt{2}}{4 L^{2}} \mathcal D_{d}\!\left(L\right) \mathcal D^{d}\!\left(L_{i}{}^{j}\right) V_{b} \bar\psi_{a}{}^{i} \gamma^{abc} \psi_{cj} +\frac{\sqrt{2}}{4 L} \left(4 D +\frac{8}{3} T_{de} T^{de} - \frac{1}{L^{2}} E_{d} E^{d} - \frac{N^{2}}{L^{2}} +\frac{1}{2 L^{2}} \mathcal D_{d}\!\left(L_{kl}\right) \mathcal D^{d}\!\left(L^{kl}\right)\right) L_{i}{}^{j} V_{b} \bar\psi_{a}{}^{i} \gamma^{abc} \psi_{cj} +\frac{\sqrt{2}}{2 L^{3}} E_{d} \varepsilon^{jk}\left(L_{l(i} \mathcal D^{d}\!\left(L_{k)}{}^{l}\right)\right) V_{b} \bar\psi_{a}{}^{i} \gamma^{abc} \psi_{cj}\\
&+\frac{2 N}{L} \Box_c\!\left(\frac{N}{L}\right) +\frac{i N}{L} \Box_c\!\left(\frac{1}{L^{3}} L_{ij} \bar\varphi^{i} \varphi^{j}\right) - \frac{i}{L^{3}} L_{i}{}^{j} \Box_c\!\left(\frac{N}{L}\right) \bar\varphi^{i} \varphi_{j} +\frac{4 N^{2}}{L^{2}} f_{a}{}^{a}\\
&- \frac{4 i N}{L^{4}} L_{i}{}^{j} f_{a}{}^{a} \bar\varphi^{i} \varphi_{j} - \frac{2 N}{L} \left(\widehat G_{ab} -16 T_{ab}\right) \left(\mathcal D^{[a}\!\left(\frac{1}{L} E^{b]}\right)\right) - \frac{N}{L^{2}} \left(\widehat G_{ab} -16 T_{ab}\right) L_{ij} \widehat R(V)^{abij} - \frac{N}{L^{4}} \left(\widehat G_{ab} -16 T_{ab}\right) \left(\mathcal D^{[a}\!\left(L_{i}{}^{k}\right) \mathcal D^{b]}\!\left(L_{jk}\right)\right) L^{ij}\\
&+\frac{N}{L} \left(\widehat G^{ab} -16 T^{ab}\right) \left(\mathcal D_{[a}\!\left(\frac{1}{L^{3}} L_{kl} \bar\varphi^{k} \gamma_{b]} \varphi^{l}\right)\right) +\frac{i N}{2 L^{2}} \left(\widehat G^{ab} -16 T^{ab}\right) \bar\varphi^{i} \widehat R(Q)_{abi} +\frac{i}{L^{3}} \left(\widehat G_{ab} -16 T_{ab}\right) \left(\mathcal D^{[a}\!\left(\frac{1}{L} E^{b]}\right)\right) L_{i}{}^{j} \bar\varphi^{i} \varphi_{j} +\frac{i}{2 L^{4}} \left(\widehat G_{ab} -16 T_{ab}\right) L_{i}{}^{j} L_{kl} \widehat R(V)^{abkl} \bar\varphi^{i} \varphi_{j}\\
&+\frac{i}{2 L^{6}} \left(\widehat G_{ab} -16 T_{ab}\right) \left(\mathcal D^{[a}\!\left(L_{k}{}^{m}\right) \mathcal D^{b]}\!\left(L_{lm}\right)\right) L_{i}{}^{j} L^{kl} \bar\varphi^{i} \varphi_{j} +\frac{16 N^{2}}{L^{2}} \widehat G_{ab} T^{ab} - \frac{16 i N}{L^{4}} \widehat G_{ab} L_{i}{}^{j} T^{ab} \bar\varphi^{i} \varphi_{j} - \frac{16 N^{2}}{L^{2}} D\\
&+\frac{16 i N}{L^{4}} D L_{i}{}^{j} \bar\varphi^{i} \varphi_{j} - \frac{416 N^{2}}{3 L^{2}} T_{ab} T^{ab} +\frac{416 i N}{3 L^{4}} L_{i}{}^{j} T_{ab} T^{ab} \bar\varphi^{i} \varphi_{j} +\frac{N}{L} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{b} \mathcal D_{b}\!\left(\frac{1}{L} \gamma^{c} \mathcal D_{c}\!\left(\varphi_{i}\right)\right)\\
&+\frac{8 i N}{L} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{b} \mathcal D_{b}\!\left(\frac{1}{L} L_{ij} \chi^{j}\right) +\frac{2 i N}{L} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{b} \mathcal D_{b}\!\left(\frac{1}{L} \gamma^{cd} T_{cd} \varphi_{i}\right) - \frac{i N}{L} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{b} \mathcal D_{b}\!\left(\frac{1}{L^{3}} L_{ij} \left(i \gamma^{c} E_{c} +N\right) \varphi^{j}\right) - \frac{N}{L} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{b} \mathcal D_{b}\!\left(\frac{1}{L^{3}} \gamma^{c} \mathcal D_{c}\!\left(L_{ij}\right) L^{jk} \varphi_{k}\right)\\
&- \frac{2 i N}{L^{2}} T_{bc} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{bc} \gamma^{d} \mathcal D_{d}\!\left(\varphi_{i}\right) - \frac{16 N}{L^{2}} L_{i}{}^{j} T_{bc} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{bc} \chi_{j} +\frac{4 N}{L^{2}} T_{bc} T_{de} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{bc} \gamma^{de} \varphi_{i} +\frac{2 N}{L^{4}} L_{i}{}^{j} T_{bc} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{bc} \left(i \gamma^{d} E_{d} +N\right) \varphi_{j}\\
&- \frac{2 i N}{L^{4}} L^{j}{}_{k} \mathcal D_{d}\!\left(L_{i}{}^{k}\right) T_{bc} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{bc} \gamma^{d} \varphi_{j} +\frac{i N}{4 L^{2}} \widehat G_{bc} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{bc} \gamma^{d} \mathcal D_{d}\!\left(\varphi_{i}\right) +\frac{2 N}{L^{2}} \widehat G_{bc} L_{i}{}^{j} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{bc} \chi_{j} - \frac{N}{2 L^{2}} \widehat G_{bc} T_{de} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{bc} \gamma^{de} \varphi_{i}\\
&- \frac{N}{4 L^{4}} \widehat G_{bc} L_{i}{}^{j} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{bc} \left(i \gamma^{d} E_{d} +N\right) \varphi_{j} +\frac{i N}{4 L^{4}} \widehat G_{bc} L^{j}{}_{k} \mathcal D_{d}\!\left(L_{i}{}^{k}\right) \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{bc} \gamma^{d} \varphi_{j} +\frac{i N^{2}}{4 L^{2}} \widehat G_{cd} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{cd} \psi_{bi} - \frac{i N^{2}}{L^{2}} T_{cd} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{cd} \psi_{bi}\\
&- \frac{i N^{2}}{L^{2}} \bar\psi_{a}{}^{i} \gamma^{ab} \phi_{bi} - \frac{i N}{2 L^{2}} \Box_c\!\left(L_{i}{}^{j}\right) \bar\psi_{a}{}^{i} \gamma^{ab} \psi_{bj} +\frac{i N}{2 L^{3}} \mathcal D_{c}\!\left(L\right) \mathcal D^{c}\!\left(L_{i}{}^{j}\right) \bar\psi_{a}{}^{i} \gamma^{ab} \psi_{bj} - \frac{i N}{2 L^{2}} \left(4 D +\frac{8}{3} T_{cd} T^{cd} - \frac{1}{L^{2}} E_{c} E^{c} - \frac{N^{2}}{L^{2}} +\frac{1}{2 L^{2}} \mathcal D_{c}\!\left(L_{kl}\right) \mathcal D^{c}\!\left(L^{kl}\right)\right) L_{i}{}^{j} \bar\psi_{a}{}^{i} \gamma^{ab} \psi_{bj}\\
&- \frac{i N}{L^{4}} E_{c} \varepsilon^{jk}\left(L_{l(i} \mathcal D^{c}\!\left(L_{k)}{}^{l}\right)\right) \bar\psi_{a}{}^{i} \gamma^{ab} \psi_{bj}\Bigg\}_{\leq2}.
\end{aligned}
\tag{R2}
```

<!-- END SINGLE CANONICAL R2 ACTION -->

The braces contain the entire canonicalized integrand; $`\leq2`$ applies to the full expression, including its closed supercovariant objects. It is pointwise on the chosen gauge slice; no boundary term was dropped. Retained full supercovariant definitions supply their quadratic completions, and any higher-order completions inside them are outside the declared truncation. The expression uses the original BF normalization throughout.

<a id="7-convention-dependence-and-remaining-uncertainties"></a>

## Convention Dependence and Scope

The local potential requires $`L>0`$ and the aligned-triplet patch. Its use does not license setting $`\mathcal D_aL_{ij}=0`$. Restoring an unaligned triplet requires the orientation contribution in the original potential derivation. Restoring the defining dilatino or dilatation gauge requires the unrestrained BF parent, not a replacement of fixed constants by independent fields in (R2).

The mixed-map gradient-phase repair, inherited 2016 label repair, and project-dependent curvature convention remain the same as in the source action. The first disappears from the gauge endpoint as explicitly proved in Section 4.4; the other source qualifications are carried forward rather than hidden. An all-orders fermionic completion or fully independent SUSY/reality certification is not asserted.

The final action contains all terms of the inherited construction needed through two fermions, in the stated closed-supercovariant presentation. The gauged maps retain their defined covariant form, with the auxiliary fields included.
