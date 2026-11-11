# LOG spinor descent — S3-01 – S3-H2.12-b

<a id="step-3--deriving-the-log-spinor--definitions-and-conventions"></a>

[Component index](../STEP_03_LOG_SPINOR.md).

---

<!-- LOG_FULL_SUPERCOVARIANT_DERIVATIVES_20260925 -->

**Derivative notation.** This is a Gold superspace calculation: its $`\nabla_A`$ remains the full source covariant derivative. Component projection at [Step 6](../STEP_06_LOG_PROJECTED_MULTIPLET_AND_BOSONIC_ACTION.md) transports it to the full project $`\mathcal D_a`$, with $`\Box^c=\mathcal D^a\mathcal D_a`$, as in the fermionic Weyl-squared calculation. The [active gauged LOG result](../../../../construction.md) retains that full derivative. No Lorentz/SU(2)-only replacement is intended here.
title: "Step 3 — LOG spinor from the calculated primary"
date: 2026-09-23
status: "Source-frame derivation; full-primary and retained-order component certification complete; see current certificate"
procedure: GAUGED-LOG-G25-S23-PROCEDURE-v1
source_frame: Gold traceless Standard-Weyl superspace
fermion_order: all orders
---

## Step 3 — deriving the LOG spinor

<!-- LOG_CURRENT_CERTIFICATION_20260925 -->

**Current scope:** [the 2026-09-25 certificate](../CERTIFICATION_LOG_TWO_FERMI_2026-09-25.md) verifies the full primary and the component action through two physical fermions. The source comparisons and restricted tests below retain their stated mathematical scope.

## 1. Problem and Target

We differentiate **our calculated primary**, Eq. (S2-193) of [STEP_02_LOG_PRIMARY.md](../STEP_02_LOG_PRIMARY.md), using the definition

```math
\varphi_{\log W}^{\alpha i}=\frac13\nabla_j^\alpha H_{\log W}^{ij}
=\frac13\varepsilon^{\alpha\eta}\varepsilon_{jr}\nabla_\eta^r H_{\log W}^{ij}.
\tag{S3-01}
```

This is S23 (3.26a), directly inspected on [On curvature-squared invariants of minimal five-dimensional supergravity from superspace — PDF22](https://arxiv.org/abs/2302.14295), and C24 (2.42a), [Components of curvature-squared invariants of minimal supergravity in five dimensions — PDF20](https://arxiv.org/abs/2311.00679). In the component calculation the same formula is bar-projected. Here we first obtain the covariant superfield; no component connection is deleted. The ordinary component spinor is its value at $`\theta=0`$.

The input is the **derived** [58-term ledger](../../../../../../../references/source_evidence/log/results/gauged_full_fermionic_log/sources/step2/primary_derived_term_ledger.json), including the $`+i/4`$ gradient-$`X^{ij}`$ coefficient H3.9. It is not the unchanged printed S23 (3.25) ledger. The derivation below assigns a separate subsection to each of the 58 input terms. Each subsection displays the input, its graded product rule, and the expression after substitution. The complete collected formula is the last display in this file.

The final expression uses the **covariant geometric basis**: the original vector/Weyl fields, their ordered vector derivatives, and the standard torsion and curvatures $`\mathcal T`$, $`\mathcal R(M)`$, $`\mathcal R(J)`$, $`\mathcal R(\mathbb D)`$, $`\mathcal R(S)`$, $`\mathcal R(K)`$ defined in §3. It contains no unevaluated spinor derivative, generator action, unnamed remainder, or coefficient function. These geometric tensors are retained explicitly instead of performing a further Clifford/Fierz reduction into the different basis of C24 supplement §2.2.1. The formula is consequently longer than that supplement. A termwise comparison in its reduced basis is **not** claimed.

**Assumptions.** A1: classical five-dimensional conformal superspace, off shell. A2: $`W>0`$ locally. A3: all fermion orders are retained, with no auxiliary equation, field equation, gauge fixing, background restriction or field redefinition. A4: equalities are local; no integration by parts or boundary identification is used. A5: flat constant-field specializations occur only in the independently reported verification probes. The full-primary S/K checks and retained-order component reality are now certified separately; §5 records the identities and the original local checks.

## 2. Convention Ledger

<!-- ASSERT_CONVENTION: source_frame=Gold traceless Standard-Weyl superspace, metric_signature=(-,+,+,+,+), natural_units=hbar=c=1, fermions=all degrees retained, derivative_parity=odd left, regularization_scheme=Not applicable for initial classical analysis, renormalization_scheme=Not applicable for initial classical analysis -->

The [main reference](../CONVENTIONS.md) and [LOG working ledger](../LOG_CONVENTIONS.md) remain controlling. The calculation uses the scoped Gold superspace conventions.

| Item | Convention used here |
|---|---|
| Dimension and indices | $`a,b=0,\ldots,4`$; $`\alpha,\beta=1,\ldots,4`$; $`i,j=1,2`$ |
| Metric and Clifford algebra | $`\eta_{ab}=\mathop{\mathrm{diag}}\nolimits(-,+,+,+,+)`$; $`\{\Gamma^a,\Gamma^b\}=-2\eta^{ab}`$; $`\Sigma^{ab}=-[\Gamma^a,\Gamma^b]/4`$ |
| Orientation | Gold $`\varepsilon^{01234}=-1`$, $`\varepsilon_{01234}=+1`$ |
| Spinor metric | $`\zeta^\alpha=\varepsilon^{\alpha\beta}\zeta_\beta`$, $`\varepsilon^{\alpha\gamma}\varepsilon_{\gamma\beta}=\delta^\alpha{}_{\beta}`$; both spinor metrics antisymmetric |
| SU(2) | $`\zeta_i=\varepsilon_{ij}\zeta^j`$; $`\varepsilon^{12}=\varepsilon_{21}=1`$ |
| Symmetrization | Parentheses and brackets have unit weight; every input $`(ij)`$ average is explicitly expanded below |
| Odd objects | $`\lambda_\alpha^i`$, $`X_\alpha^i`$, $`W_{\alpha\beta\gamma}{}^i`$, spinor derivatives and SUSY parameters |
| Curvature parity | $`\mathcal T`$ and $`\mathcal R(S)`$ are even; spinor–vector $`\mathcal R(M,J,\mathbb D,K)`$ are odd |
| Operator order | Odd derivatives act from the left; the rightmost derivative acts first; written odd-factor order is preserved |
| Curvature sign | Defined by the minus-sign commutator (S3-03); no component-frame Riemann sign is substituted |
| Reality | Gold symplectic reality is inherited; no complex conjugation or bilinear flip is used to alter the calculation |
| Coupling and quantum conventions | This is a local composite, with no action coupling, Fourier transform, state normalization or renormalization expansion |

The two-form/bispinor conversion is

```math
T_{ab}=(\Sigma_{ab})^{\beta\gamma}T_{\beta\gamma},\qquad
T_{\beta\gamma}=\frac12(\Sigma^{ab})_{\beta\gamma}T_{ab}.
\tag{S3-02}
```

It applies to $`W_{ab}`$, $`F_{ab}`$ and $`X_{ab}^{ij}`$. Also $`W_{ab\alpha}{}^i=(\Sigma_{ab})^{\beta\gamma}W_{\beta\gamma\alpha}{}^i`$. The scalar $`W`$ remains distinct from either Weyl tensor. $`X^{ij}`$ is the vector auxiliary; $`X_\alpha^i`$, $`X_{\alpha\beta}^{ij}`$ and $`Y`$ are Weyl descendants. The two meanings of $`X`$ are distinguished by their indices in every display.

## 3. Definitions and Required Identities

### 3.1 Full connection and derivative order

<!-- ASSERT_CONVENTION: source_frame=Gold traceless Standard-Weyl superspace, derivative_parity=odd left, metric_signature=(-,+,+,+,+) -->

S23 (2.1)–(2.2), C24 Appendix A, give

```math
\begin{aligned}
\nabla_A&=E_A-\tfrac12\Omega_A{}^{ab}M_{ab}-\Phi_A{}^{ij}J_{ij}-B_A\mathbb D-\mathfrak F_A{}^{\beta i}S_{\beta i}-\mathfrak F_A{}^aK_a,\\
[\nabla_A,\nabla_B\}&=-\mathcal T_{AB}{}^C\nabla_C-\tfrac12\mathcal R(M)_{AB}{}^{cd}M_{cd}-\mathcal R(J)_{AB}{}^{kl}J_{kl}-\mathcal R(\mathbb D)_{AB}\mathbb D-\mathcal R(S)_{AB}{}^{\gamma k}S_{\gamma k}-\mathcal R(K)_{AB}{}^cK_c,\\
\nabla_{\beta\gamma}&=(\Gamma^a)_{\beta\gamma}\nabla_a,\qquad \Box=\nabla^a\nabla_a.
\end{aligned}
\tag{S3-03}
```

In particular $`[\nabla_\eta^r,\nabla_a]`$ has the **opposite sign** to the coefficient expansion of $`[\nabla_a,\nabla_\eta^r]`$. Every commutator contribution below therefore carries a plus sign before the relevant generator action. Neither derivative is a partial derivative.

### 3.2 Elementary spinor derivatives

The following source identities are used before any commutator reduction. Their source images were inspected: S23 (2.6a–f), [On curvature-squared invariants of minimal five-dimensional supergravity from superspace — PDF9](https://arxiv.org/abs/2302.14295); S23 (2.12)–(2.13), [On curvature-squared invariants of minimal five-dimensional supergravity from superspace — PDF10](https://arxiv.org/abs/2302.14295), [On curvature-squared invariants of minimal five-dimensional supergravity from superspace — PDF11](https://arxiv.org/abs/2302.14295). They are also C24 (2.6), (2.29)–(2.30). In applying them, the derivative index is relabeled $`\eta,r`$ and the elementary-field indices are relabeled independently.

```math
\begin{aligned}
\nabla_\gamma^kW_{\alpha\beta}
&=W_{\alpha\beta\gamma}{}^k+\varepsilon_{\gamma(\alpha}X_{\beta)}{}^k,\qquad\text{(S23-2.6a)}\\
\nabla_\alpha^iX_\beta^j
&=X_{\alpha\beta}{}^{ij}+\tfrac i8\varepsilon^{ij}\varepsilon_{\alpha\beta}Y
-\tfrac{3i}{2}\varepsilon^{ij}(\Gamma^a)_\alpha{}^\rho\nabla_aW_{\beta\rho}
-2i\varepsilon^{ij}W_\alpha{}^\rho W_{\beta\rho}\\
&\quad+\tfrac i2\varepsilon^{ij}\varepsilon_{\alpha\beta}W^{\gamma\delta}W_{\gamma\delta}
-\tfrac i2\varepsilon^{ij}(\Gamma^a)_\beta{}^\rho\nabla_aW_{\alpha\rho},\qquad\text{(S23-2.6b)}\\
\nabla_\alpha^iW_{\beta\gamma\lambda}{}^j
&=-\tfrac12\varepsilon^{ij}\left(W_{\alpha\beta\gamma\lambda}
+3i(\Gamma^a)_{\alpha(\beta}\nabla_aW_{\gamma\lambda)}
+3i\varepsilon_{\alpha(\beta}(\Gamma^a)_\gamma{}^\tau\nabla_aW_{\lambda)\tau}\right)
-\tfrac32\varepsilon_{\alpha(\beta}X_{\gamma\lambda)}{}^{ij},\qquad\text{(S23-2.6c)}\\
\nabla_\alpha^iW_{\beta\gamma\lambda\rho}
&=-4i(\Gamma^a)_{\alpha(\beta}\nabla_aW_{\gamma\lambda\rho)}{}^i
-6iW_{\alpha(\beta\gamma}{}^iW_{\lambda\rho)}
+6iW_{\alpha(\beta}W_{\gamma\lambda\rho)}{}^i\\
&\quad+6i\varepsilon_{\alpha(\beta}\left(W_{\gamma\lambda}X_{\rho)}{}^i
-2(\Gamma^a)_\gamma{}^\tau\nabla_aW_{\lambda\rho)\tau}{}^i
-W_\gamma{}^\tau W_{\lambda\rho)\tau}{}^i\right),\qquad\text{(S23-2.6d)}\\
\nabla_\alpha^iX_{\beta\gamma}{}^{jk}
&=i\varepsilon^{i(j}\Big(-3W_{(\beta}{}^\lambda W_{\gamma)\alpha\lambda}{}^{k)}
-\varepsilon_{\alpha(\beta}W^{\rho\tau}W_{\gamma)\rho\tau}{}^{k)}
-W_{\alpha\lambda}W_{\beta\gamma}{}^{\lambda k)}-\tfrac32W_{\beta\gamma}X_\alpha{}^{k)}\\
&\qquad+\tfrac12W_{\alpha(\beta}X_{\gamma)}{}^{k)}
+\tfrac32\varepsilon_{\alpha(\beta}W_{\gamma)\lambda}X^{k)\lambda}
+2(\Gamma^a)_\alpha{}^\rho\nabla_aW_{\beta\gamma\rho}{}^{k)}\\
&\qquad+2(\Gamma^a)_{(\beta}{}^\rho\nabla_aW_{\gamma)\alpha\rho}{}^{k)}
-(\Gamma^a)_{\alpha(\beta}\nabla_aX_{\gamma)}{}^{k)}
+\varepsilon_{\alpha(\beta}(\Gamma^a)_{\gamma)\lambda}\nabla_aX^{k)\lambda}\Big),\qquad\text{(S23-2.6e)}\\
\nabla_\alpha^iY&=8(\Gamma^a)_\alpha{}^\beta\nabla_aX_\beta{}^i+8W_\alpha{}^\beta X_\beta{}^i.\qquad\text{(S23-2.6f)}
\end{aligned}
\tag{S3-WEYL}
```

```math
\begin{gathered}
W^*=W,\quad K_AW=0,\quad\mathbb DW=W,\qquad
\nabla_\alpha^{(i}\nabla_\beta^{j)}W=\tfrac14\varepsilon_{\alpha\beta}\nabla^{\gamma(i}\nabla_\gamma^{j)}W,\\
\lambda_\alpha^i=-i\nabla_\alpha^iW,\qquad
X^{ij}=\tfrac i4\nabla^{\alpha(i}\nabla_\alpha^{j)}W
=-\tfrac14\nabla^{\alpha(i}\lambda_\alpha^{j)},\\
F_{\alpha\beta}=-\tfrac i4\nabla_{(\alpha}^k\nabla_{\beta)k}W-W_{\alpha\beta}W
=\tfrac14\nabla_{(\alpha}^k\lambda_{\beta)k}-W_{\alpha\beta}W,\\
\nabla_\alpha^i\lambda_\beta^j
=-2\varepsilon^{ij}(F_{\alpha\beta}+W_{\alpha\beta}W)
-\varepsilon_{\alpha\beta}X^{ij}-\varepsilon^{ij}\nabla_{\alpha\beta}W,\qquad\text{(S23-2.13a)}\\
\begin{aligned}
\nabla_\alpha^iF_{\beta\gamma}
&=-i\nabla_{\alpha(\beta}\lambda_{\gamma)}^i-i\varepsilon_{\alpha(\beta}\nabla_{\gamma)}{}^\delta\lambda_\delta^i
-\tfrac{3i}{2}W_{\beta\gamma}\lambda_\alpha^i-W_{\alpha\beta\gamma}{}^iW\\
&\quad+\tfrac i2W_{\alpha(\beta}\lambda_{\gamma)}^i
-\tfrac{3i}{2}\varepsilon_{\alpha(\beta}W_{\gamma)}{}^\delta\lambda_\delta^i,
\end{aligned}\qquad\text{(S23-2.13b)}\\
\nabla_\alpha^iX^{jk}
=2i\varepsilon^{i(j}\left(\nabla_\alpha{}^\beta\lambda_\beta^{k)}
-\tfrac12W_{\alpha\beta}\lambda^{\beta k)}+\tfrac{3i}{4}X_\alpha{}^{k)}W\right),\qquad\text{(S23-2.13c)}\\
\nabla_{(\alpha}{}^\gamma F_{\beta)\gamma}=\tfrac12\lambda^{\gamma k}W_{\alpha\beta\gamma k},\qquad\text{(S23-2.14)}\\
S_\alpha^i\lambda_\beta^j=-2i\varepsilon_{\alpha\beta}\varepsilon^{ij}W,
\quad S_\alpha^iF_{\beta\gamma}=4\varepsilon_{\alpha(\beta}\lambda_{\gamma)}^i,
\quad S_\alpha^iX^{jk}=-2\varepsilon^{i(j}\lambda_\alpha^{k)},\qquad\text{(S23-2.15)}\\
\nabla^{ij}:=\nabla^{\alpha(i}\nabla_\alpha^{j)},\qquad
\Delta^{ijkl}:=-\tfrac1{96}\varepsilon^{\alpha\beta\gamma\delta}
\nabla_\alpha^{(i}\nabla_\beta^j\nabla_\gamma^k\nabla_\delta^{l)}
=-\tfrac1{32}\nabla^{(ij}\nabla^{kl)}.
\end{gathered}
\tag{S3-VECTOR}
```

For example, expansion of the weighted SU(2) average in the vector rule gives

```math
\begin{aligned}
\nabla_\eta^rX^{ij}={}&i\varepsilon^{ri}(\Gamma^a)_\eta{}^\beta\nabla_a\lambda_\beta^j+i\varepsilon^{rj}(\Gamma^a)_\eta{}^\beta\nabla_a\lambda_\beta^i\\
&-\tfrac i2\varepsilon^{ri}W_{\eta\beta}\lambda^{\beta j}-\tfrac i2\varepsilon^{rj}W_{\eta\beta}\lambda^{\beta i}-\tfrac34\varepsilon^{ri}X_\eta^jW-\tfrac34\varepsilon^{rj}X_\eta^iW.
\end{aligned}
\tag{S3-04}
```

The $`-3/4`$ is $`(2i)(1/2)(3i/4)`$. No SU(2) factor is suppressed. Spinor and SU(2) raising/lowering commute with $`\nabla`$ because their metrics are covariantly constant. The same statement applies to the gamma matrices and $`\eta_{ab}`$.

### 3.3 The geometric tensors retained in the result

C24 (A.3a–f), [Components of curvature-squared invariants of minimal supergravity in five dimensions — PDF82](https://arxiv.org/abs/2311.00679) and its continuation [Components of curvature-squared invariants of minimal supergravity in five dimensions — PDF83](https://arxiv.org/abs/2311.00679), defines every tensor below. The two-form dual is $`\widetilde W_{abc}=\varepsilon_{abcde}W^{de}/2`$. We write $`\mathcal T_{a\eta}{}^\beta`$ for the SU(2)-diagonal coefficient $`\mathcal T_{a\eta}^{r,\beta}{}_s=\delta_s{}^r\mathcal T_{a\eta}{}^\beta`$; this removes only an identity matrix, not a field.

```math
\begin{aligned}
\mathcal T_{a\eta}{}^\beta&=\tfrac14\big(3(\Gamma_a)_\eta{}^\gamma W_\gamma{}^\beta-W_\eta{}^\gamma(\Gamma_a)_\gamma{}^\beta\big),\\
\mathcal R(\mathbb D)_{a\eta}{}^r&=-\tfrac14(\Gamma_a)_\eta{}^\gamma X_\gamma^r,\qquad
\mathcal R(J)_{a\eta}{}^{rkl}=-\tfrac34(\Gamma_a)_\eta{}^\gamma\varepsilon^{r(k}X_\gamma^{l)},\\
\mathcal R(M)_{a\eta}{}^{rbc}&=-(\Gamma_a)_\eta{}^\gamma W^{bc}{}_{\gamma}{}^r-\tfrac14\varepsilon_a{}^{bcde}W_{de\eta}{}^r+\tfrac12\delta_a{}^{[b}(\Gamma^{c]})_\eta{}^\gamma X_\gamma^r,\\
\mathcal R(S)_{a\eta}{}^{r\gamma k}&=\tfrac1{16}X_{bc}^{rk}(\Sigma^{bc}\Gamma_a-2\Gamma_a\Sigma^{bc})_\eta{}^\gamma-\tfrac{3i}{8}\varepsilon^{rk}\nabla_{[a}W_{bc]}(\Sigma^{bc})_\eta{}^\gamma-\tfrac i8\varepsilon^{rk}\nabla_bW^{bc}(\Sigma_{ca})_\eta{}^\gamma\\
&\quad+\tfrac{3i}{16}\varepsilon^{rk}\nabla^bW_{ba}\delta_\eta{}^\gamma-\tfrac i8\varepsilon^{rk}\nabla^b\widetilde W_{ba}{}^c(\Gamma_c)_\eta{}^\gamma+\tfrac i{16}\varepsilon^{rk}\widetilde W^{bcd}W_{cd}(\Sigma_{ba})_\eta{}^\gamma-\tfrac{3i}{32}\varepsilon^{rk}\widetilde W_{abc}W^{bc}\delta_\eta{}^\gamma\\
&\quad+\tfrac i4\varepsilon^{rk}W_{ab}W^{cb}(\Gamma_c)_\eta{}^\gamma-\tfrac{3i}{64}\varepsilon^{rk}W^{bc}W_{bc}(\Gamma_a)_\eta{}^\gamma.
\end{aligned}
\tag{S3-05}
```

The entire $`K`$ curvature, including the three terms continued onto PDF83, is

```math
\begin{aligned}
\mathcal R(K)_{a\eta}{}^{rb}={}&\tfrac16(\Gamma^b)_\eta{}^\beta\nabla^cW_{ca\beta}{}^r+\tfrac1{12}(\Gamma_a)_\eta{}^\beta\nabla^cW_c{}^b{}_{\beta}{}^r+\tfrac16\nabla_\eta{}^\beta W_a{}^b{}_{\beta}{}^r-\tfrac1{24}\varepsilon_a{}^{bcde}\nabla_cW_{de\eta}{}^r\\
&+\tfrac18(\Gamma^b)_\eta{}^\beta\nabla_aX_\beta^r+\tfrac1{64}W^{cd}(3\Gamma_a\Sigma_{cd}\Gamma^b-\Sigma_{cd}\Gamma_a\Gamma^b)_\eta{}^\beta X_\beta^r-\tfrac1{48}\widetilde W_{acd}(\Gamma^b)_\eta{}^\beta W^{cd}{}_{\beta}{}^r\\
&+\tfrac18\delta_a{}^bW^{cd}W_{cd\eta}{}^r+\tfrac1{12}(\Sigma_a{}^b)_\eta{}^\beta W_{cd\beta}{}^rW^{cd}-\tfrac1{12}W^{cd}(\Sigma_{cd})_\eta{}^\beta W_a{}^b{}_{\beta}{}^r\\
&+\tfrac{13}{48}W_{ac}W^{cb}{}_{\eta}{}^r+\tfrac{11}{48}W_{ac\eta}{}^rW^{cb}-\tfrac{13}{96}(\Gamma_a)_\eta{}^\beta W_{cd\beta}{}^r\widetilde W^{cdb}.
\end{aligned}
\tag{S3-06}
```

Thus retaining $`\mathcal R(K)`$ does not mean setting its fermions to zero or using an unspecified remainder. It denotes this exact source tensor. Its vector derivatives in the final formula are full covariant derivatives of this tensor. The geometric composites and their derivatives retain these exact covariant definitions.

### 3.4 Generator actions, with the SU(2) sign derived

The needed source actions are C24 (A.1), S23 (2.8), (2.15). For a lower spinor $`U_\beta`$, a lower vector $`U_a`$ and a doublet $`U^i`$,

```math
\begin{aligned}
M_{ab}U_\beta&=(\Sigma_{ab})_\beta{}^\gamma U_\gamma,\qquad M_{ab}U_c=\eta_{ca}U_b-\eta_{cb}U_a,\\
J^{kl}U^i&=\tfrac12(\varepsilon^{ik}U^l+\varepsilon^{il}U^k),\\
J_{kl}U^i&=\varepsilon_{km}\varepsilon_{ln}J^{mn}U^i
=-\tfrac12(\delta_k{}^i\varepsilon_{ln}+\delta_l{}^i\varepsilon_{kn})U^n.
\end{aligned}
\tag{S3-07}
```

The minus sign uses $`\varepsilon_{km}\varepsilon^{im}=-\delta_k{}^i`$, with the summed index in the **second slot of both epsilons**. Generator actions on a tensor act separately on every index. In particular $`J_{kl}X^{ij}`$ is the sum of its action on $`i`$ and on $`j`$; this gives four half-weight contributions in each relevant subsection below.

```math
\begin{aligned}
S_{\gamma k}W&=0,\qquad S_{\gamma k}W_{\beta\rho}=0,\qquad
S_{\gamma k}\lambda_\beta^i=-2i\delta_k{}^i\varepsilon_{\gamma\beta}W,\\
S_{\gamma k}X^{ij}&=-\delta_k{}^i\lambda_\gamma^j-\delta_k{}^j\lambda_\gamma^i,\qquad
S_{\gamma k}X_\beta^i=4\delta_k{}^iW_{\gamma\beta},\\
S_{\gamma k}F_{\beta\rho}&=2\varepsilon_{\gamma\beta}\lambda_{\rho k}+2\varepsilon_{\gamma\rho}\lambda_{\beta k},\qquad K_aU=0.
\end{aligned}
\tag{S3-08}
```

The last identity applies to each elementary vector/Weyl descendant in this calculation, not to its vector derivatives. The weights are $`w(W)=w(W_{ab})=1`$, $`w(\lambda)=w(X_\alpha)=w(W_{\alpha\beta\gamma})=3/2`$, $`w(X^{ij})=w(F_{ab})=w(X_{ab}^{ij})=w(Y)=2`$; $`w(\nabla_a)=1`$, $`w(\nabla_\alpha^i)=1/2`$.

## 4. Detailed Derivation

### 4.1 Denominators, graded signs and the normalization

<!-- ASSERT_CONVENTION: source_frame=Gold traceless Standard-Weyl superspace, derivative_parity=odd left, fermions=all degrees retained -->

For one term with even numerical/tensor coefficient $`c`$ and ordered factors $`A_1\cdots A_m`$, differentiation gives

```math
\begin{aligned}
\nabla_\eta^rW^{-n}&=-niW^{-n-1}\lambda_\eta^r,\\
\nabla_\eta^r(cW^{-n}A_1\cdots A_m)
&=-nicW^{-n-1}\lambda_\eta^rA_1\cdots A_m\\
&\quad+cW^{-n}\sum_{q=1}^m(-1)^{|A_1|+\cdots+|A_{q-1}|}A_1\cdots A_{q-1}(\nabla_\eta^rA_q)A_{q+1}\cdots A_m.
\end{aligned}
\tag{S3-09}
```

This equation is used only to explain the operation. In §§4.4–4.10 **every sum is written out** for the actual input. No odd factor is moved past another odd factor. For example, $`\nabla(\lambda\,\nabla_aX\,\lambda)`$ has the signs $`+,-,-`$: the middle factor is even and the last factor has one odd factor to its left. Differentiating $`W^{-n}`$ inserts its gaugino to the far left; it is not silently moved through the original fermions.

The contraction in (S3-01) is the source normalization, not a convention guess. The first linear identity gives

```math
\begin{aligned}
\nabla_\eta^rH^{ij}&=\varepsilon^{ri}\varphi_\eta^j+\varepsilon^{rj}\varphi_\eta^i,\\
\varepsilon_{jr}\nabla_\eta^rH^{ij}
&=\underbrace{\varepsilon_{jr}\varepsilon^{ri}}_{\delta_j{}^i}\varphi_\eta^j+\underbrace{\varepsilon_{jr}\varepsilon^{rj}}_{2}\varphi_\eta^i=3\varphi_\eta^i.
\end{aligned}
\tag{S3-10}
```

The inverse relation is valid because the linear constraint of the input follows from its projector, (S2-191). The definition (S3-01) itself can still be differentiated before invoking that constraint.

### 4.2 Move one spinor derivative past one vector derivative

<!-- ASSERT_CONVENTION: source_frame=Gold traceless Standard-Weyl superspace, derivative_parity=odd left, commutator_order=spinor then vector -->

For an elementary tensor $`U`$ of weight $`w_U`$, insert the reversed commutator from (S3-03):

```math
\begin{aligned}
\nabla_\eta^r\nabla_aU={}&\nabla_a(\nabla_\eta^rU)+\mathcal T_{a\eta}{}^\beta\nabla_\beta^rU+\tfrac12\mathcal R(M)_{a\eta}{}^{rbc}M_{bc}U\\
&+w_U\mathcal R(\mathbb D)_{a\eta}{}^rU+\mathcal R(J)_{a\eta}{}^{rkl}J_{kl}U+\mathcal R(S)_{a\eta}{}^{r\beta k}S_{\beta k}U.
\end{aligned}
\tag{S3-11}
```

There is no $`K`$ term on this elementary $`U`$ because (S3-08) gives $`K_aU=0`$. The $`S`$ term is zero only when its displayed elementary action vanishes. It is retained, for example, on $`\lambda`$, $`X^{ij}`$, $`F_{ab}`$ and $`X_\alpha^i`$.

For the scalar this substitution is short enough to show in one equality:

```math
\nabla_\eta^r\nabla_aW=i\nabla_a\lambda_\eta^r+i\mathcal T_{a\eta}{}^\beta\lambda_\beta^r+\mathcal R(\mathbb D)_{a\eta}{}^rW.
\tag{S3-12}
```

The scalar is primary but has weight one. Its dilatation term cannot be deleted. All three terms have weight $`5/2`$.

### 4.3 Two vector derivatives: why the K curvature survives

<!-- ASSERT_CONVENTION: source_frame=Gold traceless Standard-Weyl superspace, derivative_parity=odd left, metric_signature=(-,+,+,+,+) -->

Keep vector derivatives in their original order:

```math
\begin{aligned}
\nabla_\eta^r\Box U
&=\nabla^a\nabla_a(\nabla_\eta^rU)+\nabla^a([\nabla_\eta^r,\nabla_a]U)+[\nabla_\eta^r,\nabla^a]\nabla_aU,\\
\mathbb D\nabla_aU&=(w_U+1)\nabla_aU,\qquad
M_{bc}\nabla_aU=\eta_{ab}\nabla_cU-\eta_{ac}\nabla_bU+\nabla_a(M_{bc}U),\\
J_{kl}\nabla_aU&=\nabla_a(J_{kl}U),\qquad
K_b\nabla_aU=2\eta_{ba}w_UU+2M_{ba}U,\\
S_{\beta k}\nabla_aU&=\nabla_a(S_{\beta k}U)+i(\Gamma_a)_\beta{}^\gamma\varepsilon_{kl}\nabla_\gamma^lU-\tfrac14W_a{}^b(\Gamma_b)_\beta{}^\gamma S_{\gamma k}U.
\end{aligned}
\tag{S3-13}
```

The two K terms in $`[S,\nabla_a]`$ from C24 (A.1l) annihilate the elementary $`U`$ in the last line; the displayed $`W\Gamma S`$ term generally does not. The K action on the **first vector descendant**, third line, does not vanish. In particular,

```math
\begin{aligned}
K_b\nabla_aW&=2\eta_{ba}W,\qquad K_b\nabla_aX^{ij}=4\eta_{ba}X^{ij},\\
K_b\nabla_a\lambda_\gamma^i&=3\eta_{ba}\lambda_\gamma^i+2(\Sigma_{ba})_\gamma{}^\delta\lambda_\delta^i,\\
S_{\beta k}\nabla_a\lambda_\gamma^i
&=-2i\delta_k{}^i\varepsilon_{\beta\gamma}\nabla_aW
+i(\Gamma_a)_\beta{}^\delta\varepsilon_{kl}\big[-2\varepsilon^{li}F_{\delta\gamma}-2\varepsilon^{li}W_{\delta\gamma}W-\varepsilon_{\delta\gamma}X^{li}-\varepsilon^{li}(\Gamma^b)_{\delta\gamma}\nabla_bW\big]\\
&\quad+\tfrac i2\delta_k{}^iW_a{}^b(\Gamma_b)_\beta{}^\delta\varepsilon_{\delta\gamma}W.
\end{aligned}
\tag{S3-14}
```

Each coefficient follows directly from the source generator algebra: the $`3`$ is $`2w_\lambda`$, and $`+i/2=(-1/4)(-2i)`$. The K-curvature contribution to the final spinor from $`\Box\lambda`$ therefore contains both displayed Lorentz structures. No scalar-commutator shortcut is used.

In the term calculations below, the first line of (S3-13) is expanded by the ordinary vector product rule and (S3-11). All generator actions in its last commutator are replaced by the last four lines of (S3-13). This produces explicit $`\nabla\mathcal T`$, $`\mathcal T^2`$, $`\nabla\mathcal R`$, $`\mathcal R\nabla U`$, and $`\mathcal R(K)U`$ contributions. They remain visible in the expanded endpoints for H1.3, H2.1, H2.4 and H3.10.

The weight check is local: a first-derivative commutator term has weight $`w_U+3/2`$, and a second-derivative term has $`w_U+5/2`$. For example $`w(\mathcal R(K)\lambda)=5/2+3/2=4=w(\nabla_\eta^r\Box\lambda)`$. This is also the parity check: its odd K-curvature times odd gaugino is even, matching the spinor derivative of the odd gaugino.

### Reading the 58 term calculations

The labels H0.1 through H6.2 are **input provenance IDs**, not new physical fields. A label on the left of a display means “the contribution obtained by differentiating this one displayed input”. None appears in the collected result. The original $`\alpha,\beta,\ldots`$ dummy labels may be renamed separately in each summand; free derivative labels are always $`\eta,r`$, and the original triplet indices are $`i,j`$.

Each subsection first displays the original term with its $`W`$ power and coefficient. The next display writes every product-rule derivative and its Grassmann sign. The third display inserts (S3-02), the elementary source rules, and (S3-11)–(S3-14), with all product rules distributed. Index raising/lowering is carried through explicitly; no Fierz identity or permutation of odd factors is used. The endpoints retain the source's ordered vector derivatives. Each has weight $`7/2`$, odd parity, and exactly the free indices $`(\eta;r,i,j)`$ before the final contraction.

### 4.4 Differentiate every input in the $`W^0`$ sector

<!-- ASSERT_CONVENTION: source_frame=Gold traceless Standard-Weyl superspace, derivative_parity=odd left, fermions=all degrees retained -->

#### Input H0.1

The calculated input is

```math
\left.H^{ij}\right|_{\mathrm{H0.1}}=\big(-\frac{3i}{8}W_{ab}X^{abij}\big).
\tag{S3-H0.1-input}
```

Apply the product rule (S3-09), in the displayed factor order:

```math
\begin{aligned}
\left.\nabla_\eta^rH^{ij}\right|_{\mathrm{H0.1}}=&-\frac{3i}{8}\nabla_{\eta}^{r}\big(W{}_{a b}\big)X{}^{a b i j} -\frac{3i}{8}W{}_{a b}\nabla_{\eta}^{r}\big(X{}^{a b i j}\big)
\end{aligned}
\tag{S3-H0.1-a}
```

Insert the elementary source identities and the applicable commutators (S3-11)–(S3-14), distribute the vector product rules, and contract only index-raising metrics. The resulting contribution is

```math
\begin{aligned}
\left.\nabla_\eta^rH^{ij}\right|_{\mathrm{H0.1}}=&-\frac{3i}{8}(\Sigma{}_{a b}){}^{\beta \gamma}W{}_{\eta \beta \gamma}{}^{r}X{}^{a b i j} -\frac{3i}{16}(\Sigma{}_{a b}){}_{\eta}{}^{\beta}X{}_{\beta}{}^{r}X{}^{a b i j}\\
&-\frac{3i}{16}(\Sigma{}_{a b}){}^{\beta}{}_{\eta}X{}_{\beta}{}^{r}X{}^{a b i j} -\frac{3}{16}W{}_{a b}(\Sigma{}^{a b}){}^{\beta \gamma}\varepsilon{}^{r i}W{}_{\eta \delta}W{}_{\beta \gamma}{}^{\delta j}\\
&-\frac{9}{32}W{}_{a b}(\Sigma{}^{a b}){}^{\beta \gamma}\varepsilon{}^{r i}W{}_{\beta \gamma}X{}_{\eta}{}^{j} +\frac{3}{8}W{}_{a b}(\Sigma{}^{a b}){}^{\beta \gamma}\varepsilon{}^{r i}(\Gamma{}^{c}){}_{\eta}{}^{\delta}\big(\nabla_{c}W{}_{\beta \gamma \delta}{}^{j}\big)\\
&-\frac{9}{32}W{}_{a b}(\Sigma{}^{a b}){}^{\beta \gamma}\varepsilon{}^{r i}W{}_{\beta}{}^{\delta}W{}_{\gamma \eta \delta}{}^{j} -\frac{3}{32}W{}_{a b}(\Sigma{}^{a b}){}_{\eta}{}^{\beta}\varepsilon{}^{r i}W{}^{\gamma \delta}W{}_{\beta \gamma \delta}{}^{j}\\
&+\frac{3}{64}W{}_{a b}(\Sigma{}^{a b}){}^{\beta \gamma}\varepsilon{}^{r i}W{}_{\eta \beta}X{}_{\gamma}{}^{j} +\frac{9}{64}W{}_{a b}(\Sigma{}^{a b}){}_{\eta}{}^{\beta}\varepsilon{}^{r i}W{}_{\beta \gamma}X{}^{\gamma j}\\
&+\frac{3}{16}W{}_{a b}(\Sigma{}^{a b}){}^{\beta \gamma}\varepsilon{}^{r i}(\Gamma{}^{c}){}_{\beta}{}^{\delta}\big(\nabla_{c}W{}_{\gamma \eta \delta}{}^{j}\big) -\frac{3}{32}W{}_{a b}(\Sigma{}^{a b}){}^{\beta \gamma}\varepsilon{}^{r i}(\Gamma{}^{c}){}_{\eta \beta}\big(\nabla_{c}X{}_{\gamma}{}^{j}\big)\\
&+\frac{3}{32}W{}_{a b}(\Sigma{}^{a b}){}_{\eta}{}^{\beta}\varepsilon{}^{r i}(\Gamma{}^{c}){}_{\beta \gamma}\big(\nabla_{c}X{}^{\gamma j}\big) -\frac{9}{32}W{}_{a b}(\Sigma{}^{a b}){}^{\beta \gamma}\varepsilon{}^{r i}W{}_{\gamma}{}^{\delta}W{}_{\beta \eta \delta}{}^{j}\\
&-\frac{3}{32}W{}_{a b}(\Sigma{}^{a b}){}^{\beta}{}_{\eta}\varepsilon{}^{r i}W{}^{\gamma \delta}W{}_{\beta \gamma \delta}{}^{j} +\frac{3}{64}W{}_{a b}(\Sigma{}^{a b}){}^{\beta \gamma}\varepsilon{}^{r i}W{}_{\eta \gamma}X{}_{\beta}{}^{j}\\
&+\frac{9}{64}W{}_{a b}(\Sigma{}^{a b}){}^{\beta}{}_{\eta}\varepsilon{}^{r i}W{}_{\beta \gamma}X{}^{\gamma j} +\frac{3}{16}W{}_{a b}(\Sigma{}^{a b}){}^{\beta \gamma}\varepsilon{}^{r i}(\Gamma{}^{c}){}_{\gamma}{}^{\delta}\big(\nabla_{c}W{}_{\beta \eta \delta}{}^{j}\big)\\
&-\frac{3}{32}W{}_{a b}(\Sigma{}^{a b}){}^{\beta \gamma}\varepsilon{}^{r i}(\Gamma{}^{c}){}_{\eta \gamma}\big(\nabla_{c}X{}_{\beta}{}^{j}\big) +\frac{3}{32}W{}_{a b}(\Sigma{}^{a b}){}^{\beta}{}_{\eta}\varepsilon{}^{r i}(\Gamma{}^{c}){}_{\beta \gamma}\big(\nabla_{c}X{}^{\gamma j}\big)\\
&-\frac{3}{16}W{}_{a b}(\Sigma{}^{a b}){}^{\beta \gamma}\varepsilon{}^{r j}W{}_{\eta \delta}W{}_{\beta \gamma}{}^{\delta i} -\frac{9}{32}W{}_{a b}(\Sigma{}^{a b}){}^{\beta \gamma}\varepsilon{}^{r j}W{}_{\beta \gamma}X{}_{\eta}{}^{i}\\
&+\frac{3}{8}W{}_{a b}(\Sigma{}^{a b}){}^{\beta \gamma}\varepsilon{}^{r j}(\Gamma{}^{c}){}_{\eta}{}^{\delta}\big(\nabla_{c}W{}_{\beta \gamma \delta}{}^{i}\big) -\frac{9}{32}W{}_{a b}(\Sigma{}^{a b}){}^{\beta \gamma}\varepsilon{}^{r j}W{}_{\beta}{}^{\delta}W{}_{\gamma \eta \delta}{}^{i}\\
&-\frac{3}{32}W{}_{a b}(\Sigma{}^{a b}){}_{\eta}{}^{\beta}\varepsilon{}^{r j}W{}^{\gamma \delta}W{}_{\beta \gamma \delta}{}^{i} +\frac{3}{64}W{}_{a b}(\Sigma{}^{a b}){}^{\beta \gamma}\varepsilon{}^{r j}W{}_{\eta \beta}X{}_{\gamma}{}^{i}\\
&+\frac{9}{64}W{}_{a b}(\Sigma{}^{a b}){}_{\eta}{}^{\beta}\varepsilon{}^{r j}W{}_{\beta \gamma}X{}^{\gamma i} +\frac{3}{16}W{}_{a b}(\Sigma{}^{a b}){}^{\beta \gamma}\varepsilon{}^{r j}(\Gamma{}^{c}){}_{\beta}{}^{\delta}\big(\nabla_{c}W{}_{\gamma \eta \delta}{}^{i}\big)\\
&-\frac{3}{32}W{}_{a b}(\Sigma{}^{a b}){}^{\beta \gamma}\varepsilon{}^{r j}(\Gamma{}^{c}){}_{\eta \beta}\big(\nabla_{c}X{}_{\gamma}{}^{i}\big) +\frac{3}{32}W{}_{a b}(\Sigma{}^{a b}){}_{\eta}{}^{\beta}\varepsilon{}^{r j}(\Gamma{}^{c}){}_{\beta \gamma}\big(\nabla_{c}X{}^{\gamma i}\big)\\
&-\frac{9}{32}W{}_{a b}(\Sigma{}^{a b}){}^{\beta \gamma}\varepsilon{}^{r j}W{}_{\gamma}{}^{\delta}W{}_{\beta \eta \delta}{}^{i} -\frac{3}{32}W{}_{a b}(\Sigma{}^{a b}){}^{\beta}{}_{\eta}\varepsilon{}^{r j}W{}^{\gamma \delta}W{}_{\beta \gamma \delta}{}^{i}\\
&+\frac{3}{64}W{}_{a b}(\Sigma{}^{a b}){}^{\beta \gamma}\varepsilon{}^{r j}W{}_{\eta \gamma}X{}_{\beta}{}^{i} +\frac{9}{64}W{}_{a b}(\Sigma{}^{a b}){}^{\beta}{}_{\eta}\varepsilon{}^{r j}W{}_{\beta \gamma}X{}^{\gamma i}\\
&+\frac{3}{16}W{}_{a b}(\Sigma{}^{a b}){}^{\beta \gamma}\varepsilon{}^{r j}(\Gamma{}^{c}){}_{\gamma}{}^{\delta}\big(\nabla_{c}W{}_{\beta \eta \delta}{}^{i}\big) -\frac{3}{32}W{}_{a b}(\Sigma{}^{a b}){}^{\beta \gamma}\varepsilon{}^{r j}(\Gamma{}^{c}){}_{\eta \gamma}\big(\nabla_{c}X{}_{\beta}{}^{i}\big)\\
&+\frac{3}{32}W{}_{a b}(\Sigma{}^{a b}){}^{\beta}{}_{\eta}\varepsilon{}^{r j}(\Gamma{}^{c}){}_{\beta \gamma}\big(\nabla_{c}X{}^{\gamma i}\big)
\end{aligned}
\tag{S3-H0.1-b}
```

**Check for H0.1:** all 37 written summands have weight $`7/2`$, odd parity and the same free indices $`\eta;r,i,j`$. Dummy labels are paired. The coefficient $`1/3`$ and the two external epsilons are applied once, when collecting the spinor.

#### Input H0.2

The calculated input is

```math
\left.H^{ij}\right|_{\mathrm{H0.2}}=\big(\frac{51i}{64}X^{\alpha i}X_\alpha^j\big).
\tag{S3-H0.2-input}
```

Apply the product rule (S3-09), in the displayed factor order:

```math
\begin{aligned}
\left.\nabla_\eta^rH^{ij}\right|_{\mathrm{H0.2}}=&\frac{51i}{64}\nabla_{\eta}^{r}\big(X{}^{\beta i}\big)X{}_{\beta}{}^{j} -\frac{51i}{64}X{}^{\beta i}\nabla_{\eta}^{r}\big(X{}_{\beta}{}^{j}\big)
\end{aligned}
\tag{S3-H0.2-a}
```

Insert the elementary source identities and the applicable commutators (S3-11)–(S3-14), distribute the vector product rules, and contract only index-raising metrics. The resulting contribution is

```math
\begin{aligned}
\left.\nabla_\eta^rH^{ij}\right|_{\mathrm{H0.2}}=&\frac{51i}{64}X{}_{\eta}{}^{\beta r i}X{}_{\beta}{}^{j} +\frac{51}{512}\varepsilon{}^{r i}YX{}_{\eta}{}^{j}\\
&+\frac{153}{128}\varepsilon{}^{r i}(\Gamma{}^{a}){}_{\eta}{}^{\beta}\big(\nabla_{a}W{}^{\gamma}{}_{\beta}\big)X{}_{\gamma}{}^{j} +\frac{51}{32}\varepsilon{}^{r i}W{}_{\eta}{}^{\beta}W{}^{\gamma}{}_{\beta}X{}_{\gamma}{}^{j}\\
&+\frac{51}{128}\varepsilon{}^{r i}W{}^{\beta \gamma}W{}_{\beta \gamma}X{}_{\eta}{}^{j} +\frac{51}{128}\varepsilon{}^{r i}(\Gamma{}^{a}){}^{\beta \gamma}\big(\nabla_{a}W{}_{\eta \gamma}\big)X{}_{\beta}{}^{j}\\
&-\frac{51i}{64}X{}^{\beta i}X{}_{\eta \beta}{}^{r j} +\frac{51}{512}X{}_{\eta}{}^{i}\varepsilon{}^{r j}Y\\
&-\frac{153}{128}X{}^{\beta i}\varepsilon{}^{r j}(\Gamma{}^{a}){}_{\eta}{}^{\gamma}\big(\nabla_{a}W{}_{\beta \gamma}\big) -\frac{51}{32}X{}^{\beta i}\varepsilon{}^{r j}W{}_{\eta}{}^{\gamma}W{}_{\beta \gamma}\\
&+\frac{51}{128}X{}_{\eta}{}^{i}\varepsilon{}^{r j}W{}^{\beta \gamma}W{}_{\beta \gamma} -\frac{51}{128}X{}^{\beta i}\varepsilon{}^{r j}(\Gamma{}^{a}){}_{\beta}{}^{\gamma}\big(\nabla_{a}W{}_{\eta \gamma}\big)
\end{aligned}
\tag{S3-H0.2-b}
```

**Check for H0.2:** all 12 written summands have weight $`7/2`$, odd parity and the same free indices $`\eta;r,i,j`$. Dummy labels are paired. The coefficient $`1/3`$ and the two external epsilons are applied once, when collecting the spinor.

### 4.5 Differentiate every input in the $`W^{-1}`$ sector

<!-- ASSERT_CONVENTION: source_frame=Gold traceless Standard-Weyl superspace, derivative_parity=odd left, fermions=all degrees retained -->

#### Input H1.1

The calculated input is

```math
\left.H^{ij}\right|_{\mathrm{H1.1}}=W^{-1}\big(\frac9{64}X^{ij}Y\big).
\tag{S3-H1.1-input}
```

Apply the product rule (S3-09), in the displayed factor order:

```math
\begin{aligned}
\left.\nabla_\eta^rH^{ij}\right|_{\mathrm{H1.1}}=&\frac{9}{64}\nabla_{\eta}^{r}\big(W^{-1}\big)X{}^{i j}Y +\frac{9}{64}W^{-1}\nabla_{\eta}^{r}\big(X{}^{i j}\big)Y\\
&+\frac{9}{64}W^{-1}X{}^{i j}\nabla_{\eta}^{r}\big(Y\big)
\end{aligned}
\tag{S3-H1.1-a}
```

Insert the elementary source identities and the applicable commutators (S3-11)–(S3-14), distribute the vector product rules, and contract only index-raising metrics. The resulting contribution is

```math
\begin{aligned}
\left.\nabla_\eta^rH^{ij}\right|_{\mathrm{H1.1}}=&-\frac{9i}{64}W^{-2}\lambda{}_{\eta}{}^{r}X{}^{i j}Y +\frac{9i}{64}W^{-1}\varepsilon{}^{r i}(\Gamma{}^{a}){}_{\eta}{}^{\beta}\big(\nabla_{a}\lambda{}_{\beta}{}^{j}\big)Y\\
&-\frac{9i}{128}W^{-1}\varepsilon{}^{r i}W{}_{\eta \beta}\lambda{}^{\beta j}Y -\frac{27}{256}\varepsilon{}^{r i}X{}_{\eta}{}^{j}Y\\
&+\frac{9i}{64}W^{-1}\varepsilon{}^{r j}(\Gamma{}^{a}){}_{\eta}{}^{\beta}\big(\nabla_{a}\lambda{}_{\beta}{}^{i}\big)Y -\frac{9i}{128}W^{-1}\varepsilon{}^{r j}W{}_{\eta \beta}\lambda{}^{\beta i}Y\\
&-\frac{27}{256}\varepsilon{}^{r j}X{}_{\eta}{}^{i}Y +\frac{9}{8}W^{-1}X{}^{i j}(\Gamma{}^{a}){}_{\eta}{}^{\beta}\big(\nabla_{a}X{}_{\beta}{}^{r}\big)\\
&+\frac{9}{8}W^{-1}X{}^{i j}W{}_{\eta}{}^{\beta}X{}_{\beta}{}^{r}
\end{aligned}
\tag{S3-H1.1-b}
```

**Check for H1.1:** all 9 written summands have weight $`7/2`$, odd parity and the same free indices $`\eta;r,i,j`$. Dummy labels are paired. The coefficient $`1/3`$ and the two external epsilons are applied once, when collecting the spinor.

#### Input H1.2

The calculated input is

```math
\left.H^{ij}\right|_{\mathrm{H1.2}}=W^{-1}\big(-\frac{3i}{8}F_{ab}X^{abij}\big).
\tag{S3-H1.2-input}
```

Apply the product rule (S3-09), in the displayed factor order:

```math
\begin{aligned}
\left.\nabla_\eta^rH^{ij}\right|_{\mathrm{H1.2}}=&-\frac{3i}{8}\nabla_{\eta}^{r}\big(W^{-1}\big)F{}_{a b}X{}^{a b i j} -\frac{3i}{8}W^{-1}\nabla_{\eta}^{r}\big(F{}_{a b}\big)X{}^{a b i j}\\
&-\frac{3i}{8}W^{-1}F{}_{a b}\nabla_{\eta}^{r}\big(X{}^{a b i j}\big)
\end{aligned}
\tag{S3-H1.2-a}
```

Insert the elementary source identities and the applicable commutators (S3-11)–(S3-14), distribute the vector product rules, and contract only index-raising metrics. The resulting contribution is

```math
\begin{aligned}
\left.\nabla_\eta^rH^{ij}\right|_{\mathrm{H1.2}}=&-\frac{3}{8}W^{-2}\lambda{}_{\eta}{}^{r}F{}_{a b}X{}^{a b i j} -\frac{3}{16}W^{-1}(\Sigma{}_{a b}){}^{\beta \gamma}(\Gamma{}^{c}){}_{\eta \beta}\big(\nabla_{c}\lambda{}_{\gamma}{}^{r}\big)X{}^{a b i j}\\
&-\frac{3}{16}W^{-1}(\Sigma{}_{a b}){}_{\eta}{}^{\beta}(\Gamma{}^{c}){}_{\beta}{}^{\gamma}\big(\nabla_{c}\lambda{}_{\gamma}{}^{r}\big)X{}^{a b i j} +\frac{3}{32}W^{-1}(\Sigma{}_{a b}){}^{\beta \gamma}W{}_{\eta \beta}\lambda{}_{\gamma}{}^{r}X{}^{a b i j}\\
&-\frac{9}{32}W^{-1}(\Sigma{}_{a b}){}_{\eta}{}^{\beta}W{}_{\beta}{}^{\gamma}\lambda{}_{\gamma}{}^{r}X{}^{a b i j} -\frac{3}{16}W^{-1}(\Sigma{}_{a b}){}^{\beta \gamma}(\Gamma{}^{c}){}_{\eta \gamma}\big(\nabla_{c}\lambda{}_{\beta}{}^{r}\big)X{}^{a b i j}\\
&-\frac{3}{16}W^{-1}(\Sigma{}_{a b}){}^{\beta}{}_{\eta}(\Gamma{}^{c}){}_{\beta}{}^{\gamma}\big(\nabla_{c}\lambda{}_{\gamma}{}^{r}\big)X{}^{a b i j} +\frac{3}{32}W^{-1}(\Sigma{}_{a b}){}^{\beta \gamma}W{}_{\eta \gamma}\lambda{}_{\beta}{}^{r}X{}^{a b i j}\\
&-\frac{9}{32}W^{-1}(\Sigma{}_{a b}){}^{\beta}{}_{\eta}W{}_{\beta}{}^{\gamma}\lambda{}_{\gamma}{}^{r}X{}^{a b i j} -\frac{9}{16}W^{-1}(\Sigma{}_{a b}){}^{\beta \gamma}W{}_{\beta \gamma}\lambda{}_{\eta}{}^{r}X{}^{a b i j}\\
&+\frac{3i}{8}(\Sigma{}_{a b}){}^{\beta \gamma}W{}_{\eta \beta \gamma}{}^{r}X{}^{a b i j} -\frac{3}{16}W^{-1}F{}_{a b}(\Sigma{}^{a b}){}^{\beta \gamma}\varepsilon{}^{r i}W{}_{\eta \delta}W{}_{\beta \gamma}{}^{\delta j}\\
&-\frac{9}{32}W^{-1}F{}_{a b}(\Sigma{}^{a b}){}^{\beta \gamma}\varepsilon{}^{r i}W{}_{\beta \gamma}X{}_{\eta}{}^{j} +\frac{3}{8}W^{-1}F{}_{a b}(\Sigma{}^{a b}){}^{\beta \gamma}\varepsilon{}^{r i}(\Gamma{}^{c}){}_{\eta}{}^{\delta}\big(\nabla_{c}W{}_{\beta \gamma \delta}{}^{j}\big)\\
&-\frac{9}{32}W^{-1}F{}_{a b}(\Sigma{}^{a b}){}^{\beta \gamma}\varepsilon{}^{r i}W{}_{\beta}{}^{\delta}W{}_{\gamma \eta \delta}{}^{j} -\frac{3}{32}W^{-1}F{}_{a b}(\Sigma{}^{a b}){}_{\eta}{}^{\beta}\varepsilon{}^{r i}W{}^{\gamma \delta}W{}_{\beta \gamma \delta}{}^{j}\\
&+\frac{3}{64}W^{-1}F{}_{a b}(\Sigma{}^{a b}){}^{\beta \gamma}\varepsilon{}^{r i}W{}_{\eta \beta}X{}_{\gamma}{}^{j} +\frac{9}{64}W^{-1}F{}_{a b}(\Sigma{}^{a b}){}_{\eta}{}^{\beta}\varepsilon{}^{r i}W{}_{\beta \gamma}X{}^{\gamma j}\\
&+\frac{3}{16}W^{-1}F{}_{a b}(\Sigma{}^{a b}){}^{\beta \gamma}\varepsilon{}^{r i}(\Gamma{}^{c}){}_{\beta}{}^{\delta}\big(\nabla_{c}W{}_{\gamma \eta \delta}{}^{j}\big) -\frac{3}{32}W^{-1}F{}_{a b}(\Sigma{}^{a b}){}^{\beta \gamma}\varepsilon{}^{r i}(\Gamma{}^{c}){}_{\eta \beta}\big(\nabla_{c}X{}_{\gamma}{}^{j}\big)\\
&+\frac{3}{32}W^{-1}F{}_{a b}(\Sigma{}^{a b}){}_{\eta}{}^{\beta}\varepsilon{}^{r i}(\Gamma{}^{c}){}_{\beta \gamma}\big(\nabla_{c}X{}^{\gamma j}\big) -\frac{9}{32}W^{-1}F{}_{a b}(\Sigma{}^{a b}){}^{\beta \gamma}\varepsilon{}^{r i}W{}_{\gamma}{}^{\delta}W{}_{\beta \eta \delta}{}^{j}\\
&-\frac{3}{32}W^{-1}F{}_{a b}(\Sigma{}^{a b}){}^{\beta}{}_{\eta}\varepsilon{}^{r i}W{}^{\gamma \delta}W{}_{\beta \gamma \delta}{}^{j} +\frac{3}{64}W^{-1}F{}_{a b}(\Sigma{}^{a b}){}^{\beta \gamma}\varepsilon{}^{r i}W{}_{\eta \gamma}X{}_{\beta}{}^{j}\\
&+\frac{9}{64}W^{-1}F{}_{a b}(\Sigma{}^{a b}){}^{\beta}{}_{\eta}\varepsilon{}^{r i}W{}_{\beta \gamma}X{}^{\gamma j} +\frac{3}{16}W^{-1}F{}_{a b}(\Sigma{}^{a b}){}^{\beta \gamma}\varepsilon{}^{r i}(\Gamma{}^{c}){}_{\gamma}{}^{\delta}\big(\nabla_{c}W{}_{\beta \eta \delta}{}^{j}\big)\\
&-\frac{3}{32}W^{-1}F{}_{a b}(\Sigma{}^{a b}){}^{\beta \gamma}\varepsilon{}^{r i}(\Gamma{}^{c}){}_{\eta \gamma}\big(\nabla_{c}X{}_{\beta}{}^{j}\big) +\frac{3}{32}W^{-1}F{}_{a b}(\Sigma{}^{a b}){}^{\beta}{}_{\eta}\varepsilon{}^{r i}(\Gamma{}^{c}){}_{\beta \gamma}\big(\nabla_{c}X{}^{\gamma j}\big)\\
&-\frac{3}{16}W^{-1}F{}_{a b}(\Sigma{}^{a b}){}^{\beta \gamma}\varepsilon{}^{r j}W{}_{\eta \delta}W{}_{\beta \gamma}{}^{\delta i} -\frac{9}{32}W^{-1}F{}_{a b}(\Sigma{}^{a b}){}^{\beta \gamma}\varepsilon{}^{r j}W{}_{\beta \gamma}X{}_{\eta}{}^{i}\\
&+\frac{3}{8}W^{-1}F{}_{a b}(\Sigma{}^{a b}){}^{\beta \gamma}\varepsilon{}^{r j}(\Gamma{}^{c}){}_{\eta}{}^{\delta}\big(\nabla_{c}W{}_{\beta \gamma \delta}{}^{i}\big) -\frac{9}{32}W^{-1}F{}_{a b}(\Sigma{}^{a b}){}^{\beta \gamma}\varepsilon{}^{r j}W{}_{\beta}{}^{\delta}W{}_{\gamma \eta \delta}{}^{i}\\
&-\frac{3}{32}W^{-1}F{}_{a b}(\Sigma{}^{a b}){}_{\eta}{}^{\beta}\varepsilon{}^{r j}W{}^{\gamma \delta}W{}_{\beta \gamma \delta}{}^{i} +\frac{3}{64}W^{-1}F{}_{a b}(\Sigma{}^{a b}){}^{\beta \gamma}\varepsilon{}^{r j}W{}_{\eta \beta}X{}_{\gamma}{}^{i}\\
&+\frac{9}{64}W^{-1}F{}_{a b}(\Sigma{}^{a b}){}_{\eta}{}^{\beta}\varepsilon{}^{r j}W{}_{\beta \gamma}X{}^{\gamma i} +\frac{3}{16}W^{-1}F{}_{a b}(\Sigma{}^{a b}){}^{\beta \gamma}\varepsilon{}^{r j}(\Gamma{}^{c}){}_{\beta}{}^{\delta}\big(\nabla_{c}W{}_{\gamma \eta \delta}{}^{i}\big)\\
&-\frac{3}{32}W^{-1}F{}_{a b}(\Sigma{}^{a b}){}^{\beta \gamma}\varepsilon{}^{r j}(\Gamma{}^{c}){}_{\eta \beta}\big(\nabla_{c}X{}_{\gamma}{}^{i}\big) +\frac{3}{32}W^{-1}F{}_{a b}(\Sigma{}^{a b}){}_{\eta}{}^{\beta}\varepsilon{}^{r j}(\Gamma{}^{c}){}_{\beta \gamma}\big(\nabla_{c}X{}^{\gamma i}\big)\\
&-\frac{9}{32}W^{-1}F{}_{a b}(\Sigma{}^{a b}){}^{\beta \gamma}\varepsilon{}^{r j}W{}_{\gamma}{}^{\delta}W{}_{\beta \eta \delta}{}^{i} -\frac{3}{32}W^{-1}F{}_{a b}(\Sigma{}^{a b}){}^{\beta}{}_{\eta}\varepsilon{}^{r j}W{}^{\gamma \delta}W{}_{\beta \gamma \delta}{}^{i}\\
&+\frac{3}{64}W^{-1}F{}_{a b}(\Sigma{}^{a b}){}^{\beta \gamma}\varepsilon{}^{r j}W{}_{\eta \gamma}X{}_{\beta}{}^{i} +\frac{9}{64}W^{-1}F{}_{a b}(\Sigma{}^{a b}){}^{\beta}{}_{\eta}\varepsilon{}^{r j}W{}_{\beta \gamma}X{}^{\gamma i}\\
&+\frac{3}{16}W^{-1}F{}_{a b}(\Sigma{}^{a b}){}^{\beta \gamma}\varepsilon{}^{r j}(\Gamma{}^{c}){}_{\gamma}{}^{\delta}\big(\nabla_{c}W{}_{\beta \eta \delta}{}^{i}\big) -\frac{3}{32}W^{-1}F{}_{a b}(\Sigma{}^{a b}){}^{\beta \gamma}\varepsilon{}^{r j}(\Gamma{}^{c}){}_{\eta \gamma}\big(\nabla_{c}X{}_{\beta}{}^{i}\big)\\
&+\frac{3}{32}W^{-1}F{}_{a b}(\Sigma{}^{a b}){}^{\beta}{}_{\eta}\varepsilon{}^{r j}(\Gamma{}^{c}){}_{\beta \gamma}\big(\nabla_{c}X{}^{\gamma i}\big)
\end{aligned}
\tag{S3-H1.2-b}
```

**Check for H1.2:** all 45 written summands have weight $`7/2`$, odd parity and the same free indices $`\eta;r,i,j`$. Dummy labels are paired. The coefficient $`1/3`$ and the two external epsilons are applied once, when collecting the spinor.

#### Input H1.3

The calculated input is

```math
\left.H^{ij}\right|_{\mathrm{H1.3}}=W^{-1}\big(-\frac12\Box X^{ij}\big).
\tag{S3-H1.3-input}
```

Apply the product rule (S3-09), in the displayed factor order:

```math
\begin{aligned}
\left.\nabla_\eta^rH^{ij}\right|_{\mathrm{H1.3}}=&-\frac{1}{2}\nabla_{\eta}^{r}\big(W^{-1}\big)\big(\nabla^{a}\nabla_{a}X{}^{i j}\big) -\frac{1}{2}W^{-1}\nabla_{\eta}^{r}\big(\nabla^{a}\nabla_{a}X{}^{i j}\big)
\end{aligned}
\tag{S3-H1.3-a}
```

Insert the elementary source identities and the applicable commutators (S3-11)–(S3-14), distribute the vector product rules, and contract only index-raising metrics. The resulting contribution is

```math
\begin{aligned}
\left.\nabla_\eta^rH^{ij}\right|_{\mathrm{H1.3}}=&\frac{i}{2}W^{-2}\lambda{}_{\eta}{}^{r}\big(\nabla^{a}\nabla_{a}X{}^{i j}\big) -\frac{i}{2}W^{-1}\varepsilon{}^{r i}(\Gamma{}^{a}){}_{\eta}{}^{\beta}\big(\nabla^{b}\nabla_{b}\nabla_{a}\lambda{}_{\beta}{}^{j}\big)\\
&+\frac{i}{4}W^{-1}\varepsilon{}^{r i}\big(\nabla^{a}\nabla_{a}W{}_{\eta \beta}\big)\lambda{}^{\beta j} +\frac{i}{4}W^{-1}\varepsilon{}^{r i}\big(\nabla_{a}W{}_{\eta \beta}\big)\big(\nabla^{a}\lambda{}^{\beta j}\big)\\
&+\frac{i}{4}W^{-1}\varepsilon{}^{r i}\big(\nabla^{a}W{}_{\eta \beta}\big)\big(\nabla_{a}\lambda{}^{\beta j}\big) +\frac{i}{4}W^{-1}\varepsilon{}^{r i}W{}_{\eta \beta}\big(\nabla^{a}\nabla_{a}\lambda{}^{\beta j}\big)\\
&+\frac{3}{8}\varepsilon{}^{r i}\big(\nabla^{a}\nabla_{a}X{}_{\eta}{}^{j}\big) +\frac{3}{8}W^{-1}\varepsilon{}^{r i}\big(\nabla_{a}X{}_{\eta}{}^{j}\big)\big(\nabla^{a}W\big)\\
&+\frac{3}{8}W^{-1}\varepsilon{}^{r i}\big(\nabla^{a}X{}_{\eta}{}^{j}\big)\big(\nabla_{a}W\big) +\frac{3}{8}W^{-1}\varepsilon{}^{r i}X{}_{\eta}{}^{j}\big(\nabla^{a}\nabla_{a}W\big)\\
&-\frac{i}{2}W^{-1}\varepsilon{}^{r j}(\Gamma{}^{a}){}_{\eta}{}^{\beta}\big(\nabla^{b}\nabla_{b}\nabla_{a}\lambda{}_{\beta}{}^{i}\big) +\frac{i}{4}W^{-1}\varepsilon{}^{r j}\big(\nabla^{a}\nabla_{a}W{}_{\eta \beta}\big)\lambda{}^{\beta i}\\
&+\frac{i}{4}W^{-1}\varepsilon{}^{r j}\big(\nabla_{a}W{}_{\eta \beta}\big)\big(\nabla^{a}\lambda{}^{\beta i}\big) +\frac{i}{4}W^{-1}\varepsilon{}^{r j}\big(\nabla^{a}W{}_{\eta \beta}\big)\big(\nabla_{a}\lambda{}^{\beta i}\big)\\
&+\frac{i}{4}W^{-1}\varepsilon{}^{r j}W{}_{\eta \beta}\big(\nabla^{a}\nabla_{a}\lambda{}^{\beta i}\big) +\frac{3}{8}\varepsilon{}^{r j}\big(\nabla^{a}\nabla_{a}X{}_{\eta}{}^{i}\big)\\
&+\frac{3}{8}W^{-1}\varepsilon{}^{r j}\big(\nabla_{a}X{}_{\eta}{}^{i}\big)\big(\nabla^{a}W\big) +\frac{3}{8}W^{-1}\varepsilon{}^{r j}\big(\nabla^{a}X{}_{\eta}{}^{i}\big)\big(\nabla_{a}W\big)\\
&+\frac{3}{8}W^{-1}\varepsilon{}^{r j}X{}_{\eta}{}^{i}\big(\nabla^{a}\nabla_{a}W\big) -\frac{i}{2}W^{-1}\big(\nabla^{a}\mathcal T{}_{a \eta}{}^{\beta}\big)\varepsilon{}^{r i}(\Gamma{}^{b}){}_{\beta}{}^{\gamma}\big(\nabla_{b}\lambda{}_{\gamma}{}^{j}\big)\\
&-\frac{i}{2}W^{-1}\mathcal T{}_{a \eta}{}^{\beta}\varepsilon{}^{r i}(\Gamma{}^{b}){}_{\beta}{}^{\gamma}\big(\nabla^{a}\nabla_{b}\lambda{}_{\gamma}{}^{j}\big) +\frac{i}{4}W^{-1}\big(\nabla^{a}\mathcal T{}_{a \eta}{}^{\beta}\big)\varepsilon{}^{r i}W{}_{\beta \gamma}\lambda{}^{\gamma j}\\
&+\frac{i}{4}W^{-1}\mathcal T{}_{a \eta}{}^{\beta}\varepsilon{}^{r i}\big(\nabla^{a}W{}_{\beta \gamma}\big)\lambda{}^{\gamma j} +\frac{i}{4}W^{-1}\mathcal T{}_{a \eta}{}^{\beta}\varepsilon{}^{r i}W{}_{\beta \gamma}\big(\nabla^{a}\lambda{}^{\gamma j}\big)\\
&+\frac{3}{8}\big(\nabla^{a}\mathcal T{}_{a \eta}{}^{\beta}\big)\varepsilon{}^{r i}X{}_{\beta}{}^{j} +\frac{3}{8}\mathcal T{}_{a \eta}{}^{\beta}\varepsilon{}^{r i}\big(\nabla^{a}X{}_{\beta}{}^{j}\big)\\
&+\frac{3}{8}W^{-1}\mathcal T{}_{a \eta}{}^{\beta}\varepsilon{}^{r i}X{}_{\beta}{}^{j}\big(\nabla^{a}W\big) -\frac{i}{2}W^{-1}\big(\nabla^{a}\mathcal T{}_{a \eta}{}^{\beta}\big)\varepsilon{}^{r j}(\Gamma{}^{b}){}_{\beta}{}^{\gamma}\big(\nabla_{b}\lambda{}_{\gamma}{}^{i}\big)\\
&-\frac{i}{2}W^{-1}\mathcal T{}_{a \eta}{}^{\beta}\varepsilon{}^{r j}(\Gamma{}^{b}){}_{\beta}{}^{\gamma}\big(\nabla^{a}\nabla_{b}\lambda{}_{\gamma}{}^{i}\big) +\frac{i}{4}W^{-1}\big(\nabla^{a}\mathcal T{}_{a \eta}{}^{\beta}\big)\varepsilon{}^{r j}W{}_{\beta \gamma}\lambda{}^{\gamma i}\\
&+\frac{i}{4}W^{-1}\mathcal T{}_{a \eta}{}^{\beta}\varepsilon{}^{r j}\big(\nabla^{a}W{}_{\beta \gamma}\big)\lambda{}^{\gamma i} +\frac{i}{4}W^{-1}\mathcal T{}_{a \eta}{}^{\beta}\varepsilon{}^{r j}W{}_{\beta \gamma}\big(\nabla^{a}\lambda{}^{\gamma i}\big)\\
&+\frac{3}{8}\big(\nabla^{a}\mathcal T{}_{a \eta}{}^{\beta}\big)\varepsilon{}^{r j}X{}_{\beta}{}^{i} +\frac{3}{8}\mathcal T{}_{a \eta}{}^{\beta}\varepsilon{}^{r j}\big(\nabla^{a}X{}_{\beta}{}^{i}\big)\\
&+\frac{3}{8}W^{-1}\mathcal T{}_{a \eta}{}^{\beta}\varepsilon{}^{r j}X{}_{\beta}{}^{i}\big(\nabla^{a}W\big) -W^{-1}\big(\nabla^{a}\mathcal R(\mathbb D){}_{a \eta}{}^{r}\big)X{}^{i j}\\
&-W^{-1}\mathcal R(\mathbb D){}_{a \eta}{}^{r}\big(\nabla^{a}X{}^{i j}\big) +\frac{1}{4}W^{-1}\big(\nabla^{a}\mathcal R(J){}_{a \eta}{}^{r i k}\big)X{}_{k}{}^{j}\\
&+\frac{1}{4}W^{-1}\mathcal R(J){}_{a \eta}{}^{r i k}\big(\nabla^{a}X{}_{k}{}^{j}\big) +\frac{1}{4}W^{-1}\big(\nabla^{a}\mathcal R(J){}_{a \eta}{}^{r k i}\big)X{}_{k}{}^{j}\\
&+\frac{1}{4}W^{-1}\mathcal R(J){}_{a \eta}{}^{r k i}\big(\nabla^{a}X{}_{k}{}^{j}\big) +\frac{1}{4}W^{-1}\big(\nabla^{a}\mathcal R(J){}_{a \eta}{}^{r j k}\big)X{}^{i}{}_{k}\\
&+\frac{1}{4}W^{-1}\mathcal R(J){}_{a \eta}{}^{r j k}\big(\nabla^{a}X{}^{i}{}_{k}\big) +\frac{1}{4}W^{-1}\big(\nabla^{a}\mathcal R(J){}_{a \eta}{}^{r k j}\big)X{}^{i}{}_{k}\\
&+\frac{1}{4}W^{-1}\mathcal R(J){}_{a \eta}{}^{r k j}\big(\nabla^{a}X{}^{i}{}_{k}\big) +\frac{1}{2}W^{-1}\big(\nabla^{a}\mathcal R(S){}_{a \eta}{}^{r \beta i}\big)\lambda{}_{\beta}{}^{j}\\
&+\frac{1}{2}W^{-1}\mathcal R(S){}_{a \eta}{}^{r \beta i}\big(\nabla^{a}\lambda{}_{\beta}{}^{j}\big) +\frac{1}{2}W^{-1}\big(\nabla^{a}\mathcal R(S){}_{a \eta}{}^{r \beta j}\big)\lambda{}_{\beta}{}^{i}\\
&+\frac{1}{2}W^{-1}\mathcal R(S){}_{a \eta}{}^{r \beta j}\big(\nabla^{a}\lambda{}_{\beta}{}^{i}\big) -\frac{i}{2}W^{-1}\mathcal T{}^{a}{}_{\eta}{}^{\beta}\varepsilon{}^{r i}(\Gamma{}^{b}){}_{\beta}{}^{\gamma}\big(\nabla_{a}\nabla_{b}\lambda{}_{\gamma}{}^{j}\big)\\
&+\frac{i}{4}W^{-1}\mathcal T{}^{a}{}_{\eta}{}^{\beta}\varepsilon{}^{r i}\big(\nabla_{a}W{}_{\beta \gamma}\big)\lambda{}^{\gamma j} +\frac{i}{4}W^{-1}\mathcal T{}^{a}{}_{\eta}{}^{\beta}\varepsilon{}^{r i}W{}_{\beta \gamma}\big(\nabla_{a}\lambda{}^{\gamma j}\big)\\
&+\frac{3}{8}\mathcal T{}^{a}{}_{\eta}{}^{\beta}\varepsilon{}^{r i}\big(\nabla_{a}X{}_{\beta}{}^{j}\big) +\frac{3}{8}W^{-1}\mathcal T{}^{a}{}_{\eta}{}^{\beta}\varepsilon{}^{r i}X{}_{\beta}{}^{j}\big(\nabla_{a}W\big)\\
&-\frac{i}{2}W^{-1}\mathcal T{}^{a}{}_{\eta}{}^{\beta}\varepsilon{}^{r j}(\Gamma{}^{b}){}_{\beta}{}^{\gamma}\big(\nabla_{a}\nabla_{b}\lambda{}_{\gamma}{}^{i}\big) +\frac{i}{4}W^{-1}\mathcal T{}^{a}{}_{\eta}{}^{\beta}\varepsilon{}^{r j}\big(\nabla_{a}W{}_{\beta \gamma}\big)\lambda{}^{\gamma i}\\
&+\frac{i}{4}W^{-1}\mathcal T{}^{a}{}_{\eta}{}^{\beta}\varepsilon{}^{r j}W{}_{\beta \gamma}\big(\nabla_{a}\lambda{}^{\gamma i}\big) +\frac{3}{8}\mathcal T{}^{a}{}_{\eta}{}^{\beta}\varepsilon{}^{r j}\big(\nabla_{a}X{}_{\beta}{}^{i}\big)\\
&+\frac{3}{8}W^{-1}\mathcal T{}^{a}{}_{\eta}{}^{\beta}\varepsilon{}^{r j}X{}_{\beta}{}^{i}\big(\nabla_{a}W\big) -\frac{i}{2}W^{-1}\mathcal T{}^{a}{}_{\eta}{}^{\beta}\mathcal T{}_{a \beta}{}^{\gamma}\varepsilon{}^{r i}(\Gamma{}^{b}){}_{\gamma}{}^{\delta}\big(\nabla_{b}\lambda{}_{\delta}{}^{j}\big)\\
&+\frac{i}{4}W^{-1}\mathcal T{}^{a}{}_{\eta}{}^{\beta}\mathcal T{}_{a \beta}{}^{\gamma}\varepsilon{}^{r i}W{}_{\gamma \delta}\lambda{}^{\delta j} +\frac{3}{8}\mathcal T{}^{a}{}_{\eta}{}^{\beta}\mathcal T{}_{a \beta}{}^{\gamma}\varepsilon{}^{r i}X{}_{\gamma}{}^{j}\\
&-\frac{i}{2}W^{-1}\mathcal T{}^{a}{}_{\eta}{}^{\beta}\mathcal T{}_{a \beta}{}^{\gamma}\varepsilon{}^{r j}(\Gamma{}^{b}){}_{\gamma}{}^{\delta}\big(\nabla_{b}\lambda{}_{\delta}{}^{i}\big) +\frac{i}{4}W^{-1}\mathcal T{}^{a}{}_{\eta}{}^{\beta}\mathcal T{}_{a \beta}{}^{\gamma}\varepsilon{}^{r j}W{}_{\gamma \delta}\lambda{}^{\delta i}\\
&+\frac{3}{8}\mathcal T{}^{a}{}_{\eta}{}^{\beta}\mathcal T{}_{a \beta}{}^{\gamma}\varepsilon{}^{r j}X{}_{\gamma}{}^{i} -W^{-1}\mathcal T{}^{a}{}_{\eta}{}^{\beta}\mathcal R(\mathbb D){}_{a \beta}{}^{r}X{}^{i j}\\
&+\frac{1}{4}W^{-1}\mathcal T{}^{a}{}_{\eta}{}^{\beta}\mathcal R(J){}_{a \beta}{}^{r i k}X{}_{k}{}^{j} +\frac{1}{4}W^{-1}\mathcal T{}^{a}{}_{\eta}{}^{\beta}\mathcal R(J){}_{a \beta}{}^{r k i}X{}_{k}{}^{j}\\
&+\frac{1}{4}W^{-1}\mathcal T{}^{a}{}_{\eta}{}^{\beta}\mathcal R(J){}_{a \beta}{}^{r j k}X{}^{i}{}_{k} +\frac{1}{4}W^{-1}\mathcal T{}^{a}{}_{\eta}{}^{\beta}\mathcal R(J){}_{a \beta}{}^{r k j}X{}^{i}{}_{k}\\
&+\frac{1}{2}W^{-1}\mathcal T{}^{a}{}_{\eta}{}^{\beta}\mathcal R(S){}_{a \beta}{}^{r \gamma i}\lambda{}_{\gamma}{}^{j} +\frac{1}{2}W^{-1}\mathcal T{}^{a}{}_{\eta}{}^{\beta}\mathcal R(S){}_{a \beta}{}^{r \gamma j}\lambda{}_{\gamma}{}^{i}\\
&-\frac{1}{4}W^{-1}\mathcal R(M){}^{a}{}_{\eta}{}^{r}{}_{a}{}^{b}\big(\nabla_{b}X{}^{i j}\big) +\frac{1}{4}W^{-1}\mathcal R(M){}^{a}{}_{\eta}{}^{r b}{}_{a}\big(\nabla_{b}X{}^{i j}\big)\\
&-\frac{3}{2}W^{-1}\mathcal R(\mathbb D){}^{a}{}_{\eta}{}^{r}\big(\nabla_{a}X{}^{i j}\big) +\frac{1}{4}W^{-1}\mathcal R(J){}^{a}{}_{\eta}{}^{r i k}\big(\nabla_{a}X{}_{k}{}^{j}\big)\\
&+\frac{1}{4}W^{-1}\mathcal R(J){}^{a}{}_{\eta}{}^{r k i}\big(\nabla_{a}X{}_{k}{}^{j}\big) +\frac{1}{4}W^{-1}\mathcal R(J){}^{a}{}_{\eta}{}^{r j k}\big(\nabla_{a}X{}^{i}{}_{k}\big)\\
&+\frac{1}{4}W^{-1}\mathcal R(J){}^{a}{}_{\eta}{}^{r k j}\big(\nabla_{a}X{}^{i}{}_{k}\big) +\frac{1}{2}W^{-1}\mathcal R(S){}^{a}{}_{\eta}{}^{r \beta i}\big(\nabla_{a}\lambda{}_{\beta}{}^{j}\big)\\
&+\frac{1}{2}W^{-1}\mathcal R(S){}^{a}{}_{\eta}{}^{r \beta j}\big(\nabla_{a}\lambda{}_{\beta}{}^{i}\big) +\frac{1}{2}W^{-1}\mathcal R(S){}^{a}{}_{\eta}{}^{r \beta i}(\Gamma{}_{a}){}_{\beta}{}^{\gamma}(\Gamma{}^{b}){}_{\gamma}{}^{\delta}\big(\nabla_{b}\lambda{}_{\delta}{}^{j}\big)\\
&-\frac{1}{4}W^{-1}\mathcal R(S){}^{a}{}_{\eta}{}^{r \beta i}(\Gamma{}_{a}){}_{\beta}{}^{\gamma}W{}_{\gamma \delta}\lambda{}^{\delta j} +\frac{3i}{8}\mathcal R(S){}^{a}{}_{\eta}{}^{r \beta i}(\Gamma{}_{a}){}_{\beta}{}^{\gamma}X{}_{\gamma}{}^{j}\\
&+\frac{1}{2}W^{-1}\mathcal R(S){}^{a}{}_{\eta}{}^{r \beta j}(\Gamma{}_{a}){}_{\beta}{}^{\gamma}(\Gamma{}^{b}){}_{\gamma}{}^{\delta}\big(\nabla_{b}\lambda{}_{\delta}{}^{i}\big) -\frac{1}{4}W^{-1}\mathcal R(S){}^{a}{}_{\eta}{}^{r \beta j}(\Gamma{}_{a}){}_{\beta}{}^{\gamma}W{}_{\gamma \delta}\lambda{}^{\delta i}\\
&+\frac{3i}{8}\mathcal R(S){}^{a}{}_{\eta}{}^{r \beta j}(\Gamma{}_{a}){}_{\beta}{}^{\gamma}X{}_{\gamma}{}^{i} -\frac{1}{8}W^{-1}\mathcal R(S){}^{a}{}_{\eta}{}^{r \beta i}W{}_{a}{}^{b}(\Gamma{}_{b}){}_{\beta}{}^{\gamma}\lambda{}_{\gamma}{}^{j}\\
&-\frac{1}{8}W^{-1}\mathcal R(S){}^{a}{}_{\eta}{}^{r \beta j}W{}_{a}{}^{b}(\Gamma{}_{b}){}_{\beta}{}^{\gamma}\lambda{}_{\gamma}{}^{i} -2W^{-1}\mathcal R(K){}_{a \eta}{}^{r a}X{}^{i j}
\end{aligned}
\tag{S3-H1.3-b}
```

**Check for H1.3:** all 90 written summands have weight $`7/2`$, odd parity and the same free indices $`\eta;r,i,j`$. Dummy labels are paired. The coefficient $`1/3`$ and the two external epsilons are applied once, when collecting the spinor.

#### Input H1.4

The calculated input is

```math
\left.H^{ij}\right|_{\mathrm{H1.4}}=W^{-1}\big(-\frac9{64}X^{ij}W^{ab}W_{ab}\big).
\tag{S3-H1.4-input}
```

Apply the product rule (S3-09), in the displayed factor order:

```math
\begin{aligned}
\left.\nabla_\eta^rH^{ij}\right|_{\mathrm{H1.4}}=&-\frac{9}{64}\nabla_{\eta}^{r}\big(W^{-1}\big)X{}^{i j}W{}^{a b}W{}_{a b} -\frac{9}{64}W^{-1}\nabla_{\eta}^{r}\big(X{}^{i j}\big)W{}^{a b}W{}_{a b}\\
&-\frac{9}{64}W^{-1}X{}^{i j}\nabla_{\eta}^{r}\big(W{}^{a b}\big)W{}_{a b} -\frac{9}{64}W^{-1}X{}^{i j}W{}^{a b}\nabla_{\eta}^{r}\big(W{}_{a b}\big)
\end{aligned}
\tag{S3-H1.4-a}
```

Insert the elementary source identities and the applicable commutators (S3-11)–(S3-14), distribute the vector product rules, and contract only index-raising metrics. The resulting contribution is

```math
\begin{aligned}
\left.\nabla_\eta^rH^{ij}\right|_{\mathrm{H1.4}}=&\frac{9i}{64}W^{-2}\lambda{}_{\eta}{}^{r}X{}^{i j}W{}^{a b}W{}_{a b} -\frac{9i}{64}W^{-1}\varepsilon{}^{r i}(\Gamma{}^{a}){}_{\eta}{}^{\beta}\big(\nabla_{a}\lambda{}_{\beta}{}^{j}\big)W{}^{b c}W{}_{b c}\\
&+\frac{9i}{128}W^{-1}\varepsilon{}^{r i}W{}_{\eta \beta}\lambda{}^{\beta j}W{}^{a b}W{}_{a b} +\frac{27}{256}\varepsilon{}^{r i}X{}_{\eta}{}^{j}W{}^{a b}W{}_{a b}\\
&-\frac{9i}{64}W^{-1}\varepsilon{}^{r j}(\Gamma{}^{a}){}_{\eta}{}^{\beta}\big(\nabla_{a}\lambda{}_{\beta}{}^{i}\big)W{}^{b c}W{}_{b c} +\frac{9i}{128}W^{-1}\varepsilon{}^{r j}W{}_{\eta \beta}\lambda{}^{\beta i}W{}^{a b}W{}_{a b}\\
&+\frac{27}{256}\varepsilon{}^{r j}X{}_{\eta}{}^{i}W{}^{a b}W{}_{a b} -\frac{9}{64}W^{-1}X{}^{i j}(\Sigma{}^{a b}){}^{\beta \gamma}W{}_{\eta \beta \gamma}{}^{r}W{}_{a b}\\
&-\frac{9}{128}W^{-1}X{}^{i j}(\Sigma{}^{a b}){}_{\eta}{}^{\beta}X{}_{\beta}{}^{r}W{}_{a b} -\frac{9}{128}W^{-1}X{}^{i j}(\Sigma{}^{a b}){}^{\beta}{}_{\eta}X{}_{\beta}{}^{r}W{}_{a b}\\
&-\frac{9}{64}W^{-1}X{}^{i j}W{}^{a b}(\Sigma{}_{a b}){}^{\beta \gamma}W{}_{\eta \beta \gamma}{}^{r} -\frac{9}{128}W^{-1}X{}^{i j}W{}^{a b}(\Sigma{}_{a b}){}_{\eta}{}^{\beta}X{}_{\beta}{}^{r}\\
&-\frac{9}{128}W^{-1}X{}^{i j}W{}^{a b}(\Sigma{}_{a b}){}^{\beta}{}_{\eta}X{}_{\beta}{}^{r}
\end{aligned}
\tag{S3-H1.4-b}
```

**Check for H1.4:** all 13 written summands have weight $`7/2`$, odd parity and the same free indices $`\eta;r,i,j`$. Dummy labels are paired. The coefficient $`1/3`$ and the two external epsilons are applied once, when collecting the spinor.

#### Input H1.5

The calculated input is

```math
\left.H^{ij}\right|_{\mathrm{H1.5}}=W^{-1}\big(\frac14W^{ab}W_{ab}^{\alpha(i}\lambda_\alpha^{j)}\big).
\tag{S3-H1.5-input}
```

Expand each written SU(2) average with weight $`1/2`$ before applying the left derivative.

Apply the product rule (S3-09), in the displayed factor order:

```math
\begin{aligned}
\left.\nabla_\eta^rH^{ij}\right|_{\mathrm{H1.5}}=&\frac{1}{8}\nabla_{\eta}^{r}\big(W^{-1}\big)W{}^{a b}W{}_{a b}{}^{\beta i}\lambda{}_{\beta}{}^{j} +\frac{1}{8}W^{-1}\nabla_{\eta}^{r}\big(W{}^{a b}\big)W{}_{a b}{}^{\beta i}\lambda{}_{\beta}{}^{j}\\
&+\frac{1}{8}W^{-1}W{}^{a b}\nabla_{\eta}^{r}\big(W{}_{a b}{}^{\beta i}\big)\lambda{}_{\beta}{}^{j} -\frac{1}{8}W^{-1}W{}^{a b}W{}_{a b}{}^{\beta i}\nabla_{\eta}^{r}\big(\lambda{}_{\beta}{}^{j}\big)\\
&+\frac{1}{8}\nabla_{\eta}^{r}\big(W^{-1}\big)W{}^{a b}W{}_{a b}{}^{\beta j}\lambda{}_{\beta}{}^{i} +\frac{1}{8}W^{-1}\nabla_{\eta}^{r}\big(W{}^{a b}\big)W{}_{a b}{}^{\beta j}\lambda{}_{\beta}{}^{i}\\
&+\frac{1}{8}W^{-1}W{}^{a b}\nabla_{\eta}^{r}\big(W{}_{a b}{}^{\beta j}\big)\lambda{}_{\beta}{}^{i} -\frac{1}{8}W^{-1}W{}^{a b}W{}_{a b}{}^{\beta j}\nabla_{\eta}^{r}\big(\lambda{}_{\beta}{}^{i}\big)
\end{aligned}
\tag{S3-H1.5-a}
```

Insert the elementary source identities and the applicable commutators (S3-11)–(S3-14), distribute the vector product rules, and contract only index-raising metrics. The resulting contribution is

```math
\begin{aligned}
\left.\nabla_\eta^rH^{ij}\right|_{\mathrm{H1.5}}=&-\frac{i}{8}W^{-2}\lambda{}_{\eta}{}^{r}W{}^{a b}W{}_{a b}{}^{\beta i}\lambda{}_{\beta}{}^{j} +\frac{1}{8}W^{-1}(\Sigma{}^{a b}){}^{\beta \gamma}W{}_{\eta \beta \gamma}{}^{r}W{}_{a b}{}^{\delta i}\lambda{}_{\delta}{}^{j}\\
&+\frac{1}{16}W^{-1}(\Sigma{}^{a b}){}_{\eta}{}^{\beta}X{}_{\beta}{}^{r}W{}_{a b}{}^{\gamma i}\lambda{}_{\gamma}{}^{j} +\frac{1}{16}W^{-1}(\Sigma{}^{a b}){}^{\beta}{}_{\eta}X{}_{\beta}{}^{r}W{}_{a b}{}^{\gamma i}\lambda{}_{\gamma}{}^{j}\\
&-\frac{1}{16}W^{-1}W{}^{a b}(\Sigma{}_{a b}){}^{\beta \gamma}\varepsilon{}^{r i}W{}_{\eta \beta \gamma}{}^{\delta}\lambda{}_{\delta}{}^{j} -\frac{i}{16}W^{-1}W{}^{a b}(\Sigma{}_{a b}){}^{\beta \gamma}\varepsilon{}^{r i}(\Gamma{}^{c}){}_{\eta \beta}\big(\nabla_{c}W{}_{\gamma}{}^{\delta}\big)\lambda{}_{\delta}{}^{j}\\
&-\frac{1}{16}W^{-1}W{}^{a b}(\Sigma{}_{a b}){}_{\eta}{}^{\beta}X{}_{\beta}{}^{\gamma r i}\lambda{}_{\gamma}{}^{j} -\frac{i}{16}W^{-1}W{}^{a b}(\Sigma{}_{a b}){}^{\beta \gamma}\varepsilon{}^{r i}(\Gamma{}^{c}){}_{\eta \gamma}\big(\nabla_{c}W{}_{\beta}{}^{\delta}\big)\lambda{}_{\delta}{}^{j}\\
&-\frac{1}{16}W^{-1}W{}^{a b}(\Sigma{}_{a b}){}^{\beta}{}_{\eta}X{}_{\beta}{}^{\gamma r i}\lambda{}_{\gamma}{}^{j} -\frac{i}{16}W^{-1}W{}^{a b}(\Sigma{}_{a b}){}^{\beta \gamma}\varepsilon{}^{r i}(\Gamma{}^{c}){}_{\eta}{}^{\delta}\big(\nabla_{c}W{}_{\beta \gamma}\big)\lambda{}_{\delta}{}^{j}\\
&+\frac{1}{16}W^{-1}W{}^{a b}(\Sigma{}_{a b}){}^{\beta \gamma}X{}_{\beta \gamma}{}^{r i}\lambda{}_{\eta}{}^{j} -\frac{i}{32}W^{-1}W{}^{a b}(\Sigma{}_{a b}){}_{\eta}{}^{\beta}\varepsilon{}^{r i}(\Gamma{}^{c}){}_{\beta}{}^{\gamma}\big(\nabla_{c}W{}^{\delta}{}_{\gamma}\big)\lambda{}_{\delta}{}^{j}\\
&-\frac{i}{32}W^{-1}W{}^{a b}(\Sigma{}_{a b}){}_{\eta}{}^{\beta}\varepsilon{}^{r i}(\Gamma{}^{c}){}^{\gamma \delta}\big(\nabla_{c}W{}_{\beta \delta}\big)\lambda{}_{\gamma}{}^{j} -\frac{i}{32}W^{-1}W{}^{a b}(\Sigma{}_{a b}){}^{\beta}{}_{\eta}\varepsilon{}^{r i}(\Gamma{}^{c}){}_{\beta}{}^{\gamma}\big(\nabla_{c}W{}^{\delta}{}_{\gamma}\big)\lambda{}_{\delta}{}^{j}\\
&-\frac{i}{32}W^{-1}W{}^{a b}(\Sigma{}_{a b}){}^{\beta}{}_{\eta}\varepsilon{}^{r i}(\Gamma{}^{c}){}^{\gamma \delta}\big(\nabla_{c}W{}_{\beta \delta}\big)\lambda{}_{\gamma}{}^{j} +\frac{i}{32}W^{-1}W{}^{a b}(\Sigma{}_{a b}){}^{\beta \gamma}\varepsilon{}^{r i}(\Gamma{}^{c}){}_{\beta}{}^{\delta}\big(\nabla_{c}W{}_{\gamma \delta}\big)\lambda{}_{\eta}{}^{j}\\
&+\frac{i}{32}W^{-1}W{}^{a b}(\Sigma{}_{a b}){}^{\beta \gamma}\varepsilon{}^{r i}(\Gamma{}^{c}){}_{\gamma}{}^{\delta}\big(\nabla_{c}W{}_{\beta \delta}\big)\lambda{}_{\eta}{}^{j} +\frac{1}{4}W^{-1}W{}^{a b}W{}_{a b}{}^{\beta i}\varepsilon{}^{r j}F{}_{\eta \beta}\\
&+\frac{1}{4}W{}^{a b}W{}_{a b}{}^{\beta i}\varepsilon{}^{r j}W{}_{\eta \beta} +\frac{1}{8}W^{-1}W{}^{a b}W{}_{a b \eta}{}^{i}X{}^{r j}\\
&+\frac{1}{8}W^{-1}W{}^{a b}W{}_{a b}{}^{\beta i}\varepsilon{}^{r j}(\Gamma{}^{c}){}_{\eta \beta}\big(\nabla_{c}W\big) -\frac{i}{8}W^{-2}\lambda{}_{\eta}{}^{r}W{}^{a b}W{}_{a b}{}^{\beta j}\lambda{}_{\beta}{}^{i}\\
&+\frac{1}{8}W^{-1}(\Sigma{}^{a b}){}^{\beta \gamma}W{}_{\eta \beta \gamma}{}^{r}W{}_{a b}{}^{\delta j}\lambda{}_{\delta}{}^{i} +\frac{1}{16}W^{-1}(\Sigma{}^{a b}){}_{\eta}{}^{\beta}X{}_{\beta}{}^{r}W{}_{a b}{}^{\gamma j}\lambda{}_{\gamma}{}^{i}\\
&+\frac{1}{16}W^{-1}(\Sigma{}^{a b}){}^{\beta}{}_{\eta}X{}_{\beta}{}^{r}W{}_{a b}{}^{\gamma j}\lambda{}_{\gamma}{}^{i} -\frac{1}{16}W^{-1}W{}^{a b}(\Sigma{}_{a b}){}^{\beta \gamma}\varepsilon{}^{r j}W{}_{\eta \beta \gamma}{}^{\delta}\lambda{}_{\delta}{}^{i}\\
&-\frac{i}{16}W^{-1}W{}^{a b}(\Sigma{}_{a b}){}^{\beta \gamma}\varepsilon{}^{r j}(\Gamma{}^{c}){}_{\eta \beta}\big(\nabla_{c}W{}_{\gamma}{}^{\delta}\big)\lambda{}_{\delta}{}^{i} -\frac{1}{16}W^{-1}W{}^{a b}(\Sigma{}_{a b}){}_{\eta}{}^{\beta}X{}_{\beta}{}^{\gamma r j}\lambda{}_{\gamma}{}^{i}\\
&-\frac{i}{16}W^{-1}W{}^{a b}(\Sigma{}_{a b}){}^{\beta \gamma}\varepsilon{}^{r j}(\Gamma{}^{c}){}_{\eta \gamma}\big(\nabla_{c}W{}_{\beta}{}^{\delta}\big)\lambda{}_{\delta}{}^{i} -\frac{1}{16}W^{-1}W{}^{a b}(\Sigma{}_{a b}){}^{\beta}{}_{\eta}X{}_{\beta}{}^{\gamma r j}\lambda{}_{\gamma}{}^{i}\\
&-\frac{i}{16}W^{-1}W{}^{a b}(\Sigma{}_{a b}){}^{\beta \gamma}\varepsilon{}^{r j}(\Gamma{}^{c}){}_{\eta}{}^{\delta}\big(\nabla_{c}W{}_{\beta \gamma}\big)\lambda{}_{\delta}{}^{i} +\frac{1}{16}W^{-1}W{}^{a b}(\Sigma{}_{a b}){}^{\beta \gamma}X{}_{\beta \gamma}{}^{r j}\lambda{}_{\eta}{}^{i}\\
&-\frac{i}{32}W^{-1}W{}^{a b}(\Sigma{}_{a b}){}_{\eta}{}^{\beta}\varepsilon{}^{r j}(\Gamma{}^{c}){}_{\beta}{}^{\gamma}\big(\nabla_{c}W{}^{\delta}{}_{\gamma}\big)\lambda{}_{\delta}{}^{i} -\frac{i}{32}W^{-1}W{}^{a b}(\Sigma{}_{a b}){}_{\eta}{}^{\beta}\varepsilon{}^{r j}(\Gamma{}^{c}){}^{\gamma \delta}\big(\nabla_{c}W{}_{\beta \delta}\big)\lambda{}_{\gamma}{}^{i}\\
&-\frac{i}{32}W^{-1}W{}^{a b}(\Sigma{}_{a b}){}^{\beta}{}_{\eta}\varepsilon{}^{r j}(\Gamma{}^{c}){}_{\beta}{}^{\gamma}\big(\nabla_{c}W{}^{\delta}{}_{\gamma}\big)\lambda{}_{\delta}{}^{i} -\frac{i}{32}W^{-1}W{}^{a b}(\Sigma{}_{a b}){}^{\beta}{}_{\eta}\varepsilon{}^{r j}(\Gamma{}^{c}){}^{\gamma \delta}\big(\nabla_{c}W{}_{\beta \delta}\big)\lambda{}_{\gamma}{}^{i}\\
&+\frac{i}{32}W^{-1}W{}^{a b}(\Sigma{}_{a b}){}^{\beta \gamma}\varepsilon{}^{r j}(\Gamma{}^{c}){}_{\beta}{}^{\delta}\big(\nabla_{c}W{}_{\gamma \delta}\big)\lambda{}_{\eta}{}^{i} +\frac{i}{32}W^{-1}W{}^{a b}(\Sigma{}_{a b}){}^{\beta \gamma}\varepsilon{}^{r j}(\Gamma{}^{c}){}_{\gamma}{}^{\delta}\big(\nabla_{c}W{}_{\beta \delta}\big)\lambda{}_{\eta}{}^{i}\\
&+\frac{1}{4}W^{-1}W{}^{a b}W{}_{a b}{}^{\beta j}\varepsilon{}^{r i}F{}_{\eta \beta} +\frac{1}{4}W{}^{a b}W{}_{a b}{}^{\beta j}\varepsilon{}^{r i}W{}_{\eta \beta}\\
&+\frac{1}{8}W^{-1}W{}^{a b}W{}_{a b \eta}{}^{j}X{}^{r i} +\frac{1}{8}W^{-1}W{}^{a b}W{}_{a b}{}^{\beta j}\varepsilon{}^{r i}(\Gamma{}^{c}){}_{\eta \beta}\big(\nabla_{c}W\big)
\end{aligned}
\tag{S3-H1.5-b}
```

**Check for H1.5:** all 42 written summands have weight $`7/2`$, odd parity and the same free indices $`\eta;r,i,j`$. Dummy labels are paired. The coefficient $`1/3`$ and the two external epsilons are applied once, when collecting the spinor.

#### Input H1.6

The calculated input is

```math
\left.H^{ij}\right|_{\mathrm{H1.6}}=W^{-1}\big(-\frac34(\Gamma^a)^{\alpha\beta}X_\alpha^{(i}\nabla_a\lambda_\beta^{j)}\big).
\tag{S3-H1.6-input}
```

Expand each written SU(2) average with weight $`1/2`$ before applying the left derivative.

Apply the product rule (S3-09), in the displayed factor order:

```math
\begin{aligned}
\left.\nabla_\eta^rH^{ij}\right|_{\mathrm{H1.6}}=&-\frac{3}{8}\nabla_{\eta}^{r}\big(W^{-1}\big)(\Gamma{}^{a}){}^{\beta \gamma}X{}_{\beta}{}^{i}\big(\nabla_{a}\lambda{}_{\gamma}{}^{j}\big) -\frac{3}{8}W^{-1}(\Gamma{}^{a}){}^{\beta \gamma}\nabla_{\eta}^{r}\big(X{}_{\beta}{}^{i}\big)\big(\nabla_{a}\lambda{}_{\gamma}{}^{j}\big)\\
&+\frac{3}{8}W^{-1}(\Gamma{}^{a}){}^{\beta \gamma}X{}_{\beta}{}^{i}\nabla_{\eta}^{r}\big(\nabla_{a}\lambda{}_{\gamma}{}^{j}\big) -\frac{3}{8}\nabla_{\eta}^{r}\big(W^{-1}\big)(\Gamma{}^{a}){}^{\beta \gamma}X{}_{\beta}{}^{j}\big(\nabla_{a}\lambda{}_{\gamma}{}^{i}\big)\\
&-\frac{3}{8}W^{-1}(\Gamma{}^{a}){}^{\beta \gamma}\nabla_{\eta}^{r}\big(X{}_{\beta}{}^{j}\big)\big(\nabla_{a}\lambda{}_{\gamma}{}^{i}\big) +\frac{3}{8}W^{-1}(\Gamma{}^{a}){}^{\beta \gamma}X{}_{\beta}{}^{j}\nabla_{\eta}^{r}\big(\nabla_{a}\lambda{}_{\gamma}{}^{i}\big)
\end{aligned}
\tag{S3-H1.6-a}
```

Insert the elementary source identities and the applicable commutators (S3-11)–(S3-14), distribute the vector product rules, and contract only index-raising metrics. The resulting contribution is

```math
\begin{aligned}
\left.\nabla_\eta^rH^{ij}\right|_{\mathrm{H1.6}}=&\frac{3i}{8}W^{-2}\lambda{}_{\eta}{}^{r}(\Gamma{}^{a}){}^{\beta \gamma}X{}_{\beta}{}^{i}\big(\nabla_{a}\lambda{}_{\gamma}{}^{j}\big) -\frac{3}{8}W^{-1}(\Gamma{}^{a}){}^{\beta \gamma}X{}_{\eta \beta}{}^{r i}\big(\nabla_{a}\lambda{}_{\gamma}{}^{j}\big)\\
&-\frac{3i}{64}W^{-1}(\Gamma{}^{a}){}_{\eta}{}^{\beta}\varepsilon{}^{r i}Y\big(\nabla_{a}\lambda{}_{\beta}{}^{j}\big) +\frac{9i}{16}W^{-1}(\Gamma{}^{a}){}^{\beta \gamma}\varepsilon{}^{r i}(\Gamma{}^{b}){}_{\eta}{}^{\delta}\big(\nabla_{b}W{}_{\beta \delta}\big)\big(\nabla_{a}\lambda{}_{\gamma}{}^{j}\big)\\
&+\frac{3i}{4}W^{-1}(\Gamma{}^{a}){}^{\beta \gamma}\varepsilon{}^{r i}W{}_{\eta}{}^{\delta}W{}_{\beta \delta}\big(\nabla_{a}\lambda{}_{\gamma}{}^{j}\big) -\frac{3i}{16}W^{-1}(\Gamma{}^{a}){}_{\eta}{}^{\beta}\varepsilon{}^{r i}W{}^{\gamma \delta}W{}_{\gamma \delta}\big(\nabla_{a}\lambda{}_{\beta}{}^{j}\big)\\
&+\frac{3i}{16}W^{-1}(\Gamma{}^{a}){}^{\beta \gamma}\varepsilon{}^{r i}(\Gamma{}^{b}){}_{\beta}{}^{\delta}\big(\nabla_{b}W{}_{\eta \delta}\big)\big(\nabla_{a}\lambda{}_{\gamma}{}^{j}\big) -\frac{3}{4}W^{-1}(\Gamma{}^{a}){}^{\beta \gamma}X{}_{\beta}{}^{i}\varepsilon{}^{r j}\big(\nabla_{a}F{}_{\eta \gamma}\big)\\
&-\frac{3}{4}(\Gamma{}^{a}){}^{\beta \gamma}X{}_{\beta}{}^{i}\varepsilon{}^{r j}\big(\nabla_{a}W{}_{\eta \gamma}\big) -\frac{3}{4}W^{-1}(\Gamma{}^{a}){}^{\beta \gamma}X{}_{\beta}{}^{i}\varepsilon{}^{r j}W{}_{\eta \gamma}\big(\nabla_{a}W\big)\\
&-\frac{3}{8}W^{-1}(\Gamma{}^{a}){}^{\beta}{}_{\eta}X{}_{\beta}{}^{i}\big(\nabla_{a}X{}^{r j}\big) -\frac{3}{8}W^{-1}(\Gamma{}^{a}){}^{\beta \gamma}X{}_{\beta}{}^{i}\varepsilon{}^{r j}(\Gamma{}^{b}){}_{\eta \gamma}\big(\nabla_{a}\nabla_{b}W\big)\\
&-\frac{3}{4}W^{-1}(\Gamma{}^{a}){}^{\beta \gamma}X{}_{\beta}{}^{i}\mathcal T{}_{a \eta}{}^{\delta}\varepsilon{}^{r j}F{}_{\delta \gamma} -\frac{3}{4}(\Gamma{}^{a}){}^{\beta \gamma}X{}_{\beta}{}^{i}\mathcal T{}_{a \eta}{}^{\delta}\varepsilon{}^{r j}W{}_{\delta \gamma}\\
&-\frac{3}{8}W^{-1}(\Gamma{}^{a}){}^{\beta}{}_{\gamma}X{}_{\beta}{}^{i}\mathcal T{}_{a \eta}{}^{\gamma}X{}^{r j} -\frac{3}{8}W^{-1}(\Gamma{}^{a}){}^{\beta \gamma}X{}_{\beta}{}^{i}\mathcal T{}_{a \eta}{}^{\delta}\varepsilon{}^{r j}(\Gamma{}^{b}){}_{\delta \gamma}\big(\nabla_{b}W\big)\\
&+\frac{3}{16}W^{-1}(\Gamma{}^{a}){}^{\beta \gamma}X{}_{\beta}{}^{i}\mathcal R(M){}_{a \eta}{}^{r b c}(\Sigma{}_{b c}){}_{\gamma}{}^{\delta}\lambda{}_{\delta}{}^{j} +\frac{9}{16}W^{-1}(\Gamma{}^{a}){}^{\beta \gamma}X{}_{\beta}{}^{i}\mathcal R(\mathbb D){}_{a \eta}{}^{r}\lambda{}_{\gamma}{}^{j}\\
&-\frac{3}{16}W^{-1}(\Gamma{}^{a}){}^{\beta \gamma}X{}_{\beta}{}^{i}\mathcal R(J){}_{a \eta}{}^{r j k}\lambda{}_{\gamma k} -\frac{3}{16}W^{-1}(\Gamma{}^{a}){}^{\beta \gamma}X{}_{\beta}{}^{i}\mathcal R(J){}_{a \eta}{}^{r k j}\lambda{}_{\gamma k}\\
&-\frac{3i}{4}(\Gamma{}^{a}){}^{\beta}{}_{\gamma}X{}_{\beta}{}^{i}\mathcal R(S){}_{a \eta}{}^{r \gamma j} +\frac{3i}{8}W^{-2}\lambda{}_{\eta}{}^{r}(\Gamma{}^{a}){}^{\beta \gamma}X{}_{\beta}{}^{j}\big(\nabla_{a}\lambda{}_{\gamma}{}^{i}\big)\\
&-\frac{3}{8}W^{-1}(\Gamma{}^{a}){}^{\beta \gamma}X{}_{\eta \beta}{}^{r j}\big(\nabla_{a}\lambda{}_{\gamma}{}^{i}\big) -\frac{3i}{64}W^{-1}(\Gamma{}^{a}){}_{\eta}{}^{\beta}\varepsilon{}^{r j}Y\big(\nabla_{a}\lambda{}_{\beta}{}^{i}\big)\\
&+\frac{9i}{16}W^{-1}(\Gamma{}^{a}){}^{\beta \gamma}\varepsilon{}^{r j}(\Gamma{}^{b}){}_{\eta}{}^{\delta}\big(\nabla_{b}W{}_{\beta \delta}\big)\big(\nabla_{a}\lambda{}_{\gamma}{}^{i}\big) +\frac{3i}{4}W^{-1}(\Gamma{}^{a}){}^{\beta \gamma}\varepsilon{}^{r j}W{}_{\eta}{}^{\delta}W{}_{\beta \delta}\big(\nabla_{a}\lambda{}_{\gamma}{}^{i}\big)\\
&-\frac{3i}{16}W^{-1}(\Gamma{}^{a}){}_{\eta}{}^{\beta}\varepsilon{}^{r j}W{}^{\gamma \delta}W{}_{\gamma \delta}\big(\nabla_{a}\lambda{}_{\beta}{}^{i}\big) +\frac{3i}{16}W^{-1}(\Gamma{}^{a}){}^{\beta \gamma}\varepsilon{}^{r j}(\Gamma{}^{b}){}_{\beta}{}^{\delta}\big(\nabla_{b}W{}_{\eta \delta}\big)\big(\nabla_{a}\lambda{}_{\gamma}{}^{i}\big)\\
&-\frac{3}{4}W^{-1}(\Gamma{}^{a}){}^{\beta \gamma}X{}_{\beta}{}^{j}\varepsilon{}^{r i}\big(\nabla_{a}F{}_{\eta \gamma}\big) -\frac{3}{4}(\Gamma{}^{a}){}^{\beta \gamma}X{}_{\beta}{}^{j}\varepsilon{}^{r i}\big(\nabla_{a}W{}_{\eta \gamma}\big)\\
&-\frac{3}{4}W^{-1}(\Gamma{}^{a}){}^{\beta \gamma}X{}_{\beta}{}^{j}\varepsilon{}^{r i}W{}_{\eta \gamma}\big(\nabla_{a}W\big) -\frac{3}{8}W^{-1}(\Gamma{}^{a}){}^{\beta}{}_{\eta}X{}_{\beta}{}^{j}\big(\nabla_{a}X{}^{r i}\big)\\
&-\frac{3}{8}W^{-1}(\Gamma{}^{a}){}^{\beta \gamma}X{}_{\beta}{}^{j}\varepsilon{}^{r i}(\Gamma{}^{b}){}_{\eta \gamma}\big(\nabla_{a}\nabla_{b}W\big) -\frac{3}{4}W^{-1}(\Gamma{}^{a}){}^{\beta \gamma}X{}_{\beta}{}^{j}\mathcal T{}_{a \eta}{}^{\delta}\varepsilon{}^{r i}F{}_{\delta \gamma}\\
&-\frac{3}{4}(\Gamma{}^{a}){}^{\beta \gamma}X{}_{\beta}{}^{j}\mathcal T{}_{a \eta}{}^{\delta}\varepsilon{}^{r i}W{}_{\delta \gamma} -\frac{3}{8}W^{-1}(\Gamma{}^{a}){}^{\beta}{}_{\gamma}X{}_{\beta}{}^{j}\mathcal T{}_{a \eta}{}^{\gamma}X{}^{r i}\\
&-\frac{3}{8}W^{-1}(\Gamma{}^{a}){}^{\beta \gamma}X{}_{\beta}{}^{j}\mathcal T{}_{a \eta}{}^{\delta}\varepsilon{}^{r i}(\Gamma{}^{b}){}_{\delta \gamma}\big(\nabla_{b}W\big) +\frac{3}{16}W^{-1}(\Gamma{}^{a}){}^{\beta \gamma}X{}_{\beta}{}^{j}\mathcal R(M){}_{a \eta}{}^{r b c}(\Sigma{}_{b c}){}_{\gamma}{}^{\delta}\lambda{}_{\delta}{}^{i}\\
&+\frac{9}{16}W^{-1}(\Gamma{}^{a}){}^{\beta \gamma}X{}_{\beta}{}^{j}\mathcal R(\mathbb D){}_{a \eta}{}^{r}\lambda{}_{\gamma}{}^{i} -\frac{3}{16}W^{-1}(\Gamma{}^{a}){}^{\beta \gamma}X{}_{\beta}{}^{j}\mathcal R(J){}_{a \eta}{}^{r i k}\lambda{}_{\gamma k}\\
&-\frac{3}{16}W^{-1}(\Gamma{}^{a}){}^{\beta \gamma}X{}_{\beta}{}^{j}\mathcal R(J){}_{a \eta}{}^{r k i}\lambda{}_{\gamma k} -\frac{3i}{4}(\Gamma{}^{a}){}^{\beta}{}_{\gamma}X{}_{\beta}{}^{j}\mathcal R(S){}_{a \eta}{}^{r \gamma i}
\end{aligned}
\tag{S3-H1.6-b}
```

**Check for H1.6:** all 42 written summands have weight $`7/2`$, odd parity and the same free indices $`\eta;r,i,j`$. Dummy labels are paired. The coefficient $`1/3`$ and the two external epsilons are applied once, when collecting the spinor.

#### Input H1.7

The calculated input is

```math
\left.H^{ij}\right|_{\mathrm{H1.7}}=W^{-1}\big(\frac34(\Gamma^a)^{\alpha\beta}\lambda_\alpha^{(i}\nabla_aX_\beta^{j)}\big).
\tag{S3-H1.7-input}
```

Expand each written SU(2) average with weight $`1/2`$ before applying the left derivative.

Apply the product rule (S3-09), in the displayed factor order:

```math
\begin{aligned}
\left.\nabla_\eta^rH^{ij}\right|_{\mathrm{H1.7}}=&\frac{3}{8}\nabla_{\eta}^{r}\big(W^{-1}\big)(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{i}\big(\nabla_{a}X{}_{\gamma}{}^{j}\big) +\frac{3}{8}W^{-1}(\Gamma{}^{a}){}^{\beta \gamma}\nabla_{\eta}^{r}\big(\lambda{}_{\beta}{}^{i}\big)\big(\nabla_{a}X{}_{\gamma}{}^{j}\big)\\
&-\frac{3}{8}W^{-1}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{i}\nabla_{\eta}^{r}\big(\nabla_{a}X{}_{\gamma}{}^{j}\big) +\frac{3}{8}\nabla_{\eta}^{r}\big(W^{-1}\big)(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{j}\big(\nabla_{a}X{}_{\gamma}{}^{i}\big)\\
&+\frac{3}{8}W^{-1}(\Gamma{}^{a}){}^{\beta \gamma}\nabla_{\eta}^{r}\big(\lambda{}_{\beta}{}^{j}\big)\big(\nabla_{a}X{}_{\gamma}{}^{i}\big) -\frac{3}{8}W^{-1}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{j}\nabla_{\eta}^{r}\big(\nabla_{a}X{}_{\gamma}{}^{i}\big)
\end{aligned}
\tag{S3-H1.7-a}
```

Insert the elementary source identities and the applicable commutators (S3-11)–(S3-14), distribute the vector product rules, and contract only index-raising metrics. The resulting contribution is

```math
\begin{aligned}
\left.\nabla_\eta^rH^{ij}\right|_{\mathrm{H1.7}}=&-\frac{3i}{8}W^{-2}\lambda{}_{\eta}{}^{r}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{i}\big(\nabla_{a}X{}_{\gamma}{}^{j}\big) -\frac{3}{4}W^{-1}(\Gamma{}^{a}){}^{\beta \gamma}\varepsilon{}^{r i}F{}_{\eta \beta}\big(\nabla_{a}X{}_{\gamma}{}^{j}\big)\\
&-\frac{3}{4}(\Gamma{}^{a}){}^{\beta \gamma}\varepsilon{}^{r i}W{}_{\eta \beta}\big(\nabla_{a}X{}_{\gamma}{}^{j}\big) -\frac{3}{8}W^{-1}(\Gamma{}^{a}){}_{\eta}{}^{\beta}X{}^{r i}\big(\nabla_{a}X{}_{\beta}{}^{j}\big)\\
&-\frac{3}{8}W^{-1}(\Gamma{}^{a}){}^{\beta \gamma}\varepsilon{}^{r i}(\Gamma{}^{b}){}_{\eta \beta}\big(\nabla_{b}W\big)\big(\nabla_{a}X{}_{\gamma}{}^{j}\big) -\frac{3}{8}W^{-1}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{i}\big(\nabla_{a}X{}_{\eta \gamma}{}^{r j}\big)\\
&-\frac{3i}{64}W^{-1}(\Gamma{}^{a}){}^{\beta}{}_{\eta}\lambda{}_{\beta}{}^{i}\varepsilon{}^{r j}\big(\nabla_{a}Y\big) +\frac{9i}{16}W^{-1}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{i}\varepsilon{}^{r j}(\Gamma{}^{b}){}_{\eta}{}^{\delta}\big(\nabla_{a}\nabla_{b}W{}_{\gamma \delta}\big)\\
&+\frac{3i}{4}W^{-1}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{i}\varepsilon{}^{r j}\big(\nabla_{a}W{}_{\eta}{}^{\delta}\big)W{}_{\gamma \delta} +\frac{3i}{4}W^{-1}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{i}\varepsilon{}^{r j}W{}_{\eta}{}^{\delta}\big(\nabla_{a}W{}_{\gamma \delta}\big)\\
&-\frac{3i}{16}W^{-1}(\Gamma{}^{a}){}^{\beta}{}_{\eta}\lambda{}_{\beta}{}^{i}\varepsilon{}^{r j}\big(\nabla_{a}W{}^{\gamma \delta}\big)W{}_{\gamma \delta} -\frac{3i}{16}W^{-1}(\Gamma{}^{a}){}^{\beta}{}_{\eta}\lambda{}_{\beta}{}^{i}\varepsilon{}^{r j}W{}^{\gamma \delta}\big(\nabla_{a}W{}_{\gamma \delta}\big)\\
&+\frac{3i}{16}W^{-1}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{i}\varepsilon{}^{r j}(\Gamma{}^{b}){}_{\gamma}{}^{\delta}\big(\nabla_{a}\nabla_{b}W{}_{\eta \delta}\big) -\frac{3}{8}W^{-1}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{i}\mathcal T{}_{a \eta}{}^{\delta}X{}_{\delta \gamma}{}^{r j}\\
&-\frac{3i}{64}W^{-1}(\Gamma{}^{a}){}^{\beta}{}_{\gamma}\lambda{}_{\beta}{}^{i}\mathcal T{}_{a \eta}{}^{\gamma}\varepsilon{}^{r j}Y +\frac{9i}{16}W^{-1}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{i}\mathcal T{}_{a \eta}{}^{\delta}\varepsilon{}^{r j}(\Gamma{}^{b}){}_{\delta}{}^{\rho}\big(\nabla_{b}W{}_{\gamma \rho}\big)\\
&+\frac{3i}{4}W^{-1}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{i}\mathcal T{}_{a \eta}{}^{\delta}\varepsilon{}^{r j}W{}_{\delta}{}^{\rho}W{}_{\gamma \rho} -\frac{3i}{16}W^{-1}(\Gamma{}^{a}){}^{\beta}{}_{\gamma}\lambda{}_{\beta}{}^{i}\mathcal T{}_{a \eta}{}^{\gamma}\varepsilon{}^{r j}W{}^{\delta \rho}W{}_{\delta \rho}\\
&+\frac{3i}{16}W^{-1}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{i}\mathcal T{}_{a \eta}{}^{\delta}\varepsilon{}^{r j}(\Gamma{}^{b}){}_{\gamma}{}^{\rho}\big(\nabla_{b}W{}_{\delta \rho}\big) -\frac{3}{16}W^{-1}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{i}\mathcal R(M){}_{a \eta}{}^{r b c}(\Sigma{}_{b c}){}_{\gamma}{}^{\delta}X{}_{\delta}{}^{j}\\
&-\frac{9}{16}W^{-1}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{i}\mathcal R(\mathbb D){}_{a \eta}{}^{r}X{}_{\gamma}{}^{j} +\frac{3}{16}W^{-1}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{i}\mathcal R(J){}_{a \eta}{}^{r j k}X{}_{\gamma k}\\
&+\frac{3}{16}W^{-1}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{i}\mathcal R(J){}_{a \eta}{}^{r k j}X{}_{\gamma k} -\frac{3}{2}W^{-1}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{i}\mathcal R(S){}_{a \eta}{}^{r \delta j}W{}_{\delta \gamma}\\
&-\frac{3i}{8}W^{-2}\lambda{}_{\eta}{}^{r}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{j}\big(\nabla_{a}X{}_{\gamma}{}^{i}\big) -\frac{3}{4}W^{-1}(\Gamma{}^{a}){}^{\beta \gamma}\varepsilon{}^{r j}F{}_{\eta \beta}\big(\nabla_{a}X{}_{\gamma}{}^{i}\big)\\
&-\frac{3}{4}(\Gamma{}^{a}){}^{\beta \gamma}\varepsilon{}^{r j}W{}_{\eta \beta}\big(\nabla_{a}X{}_{\gamma}{}^{i}\big) -\frac{3}{8}W^{-1}(\Gamma{}^{a}){}_{\eta}{}^{\beta}X{}^{r j}\big(\nabla_{a}X{}_{\beta}{}^{i}\big)\\
&-\frac{3}{8}W^{-1}(\Gamma{}^{a}){}^{\beta \gamma}\varepsilon{}^{r j}(\Gamma{}^{b}){}_{\eta \beta}\big(\nabla_{b}W\big)\big(\nabla_{a}X{}_{\gamma}{}^{i}\big) -\frac{3}{8}W^{-1}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{j}\big(\nabla_{a}X{}_{\eta \gamma}{}^{r i}\big)\\
&-\frac{3i}{64}W^{-1}(\Gamma{}^{a}){}^{\beta}{}_{\eta}\lambda{}_{\beta}{}^{j}\varepsilon{}^{r i}\big(\nabla_{a}Y\big) +\frac{9i}{16}W^{-1}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{j}\varepsilon{}^{r i}(\Gamma{}^{b}){}_{\eta}{}^{\delta}\big(\nabla_{a}\nabla_{b}W{}_{\gamma \delta}\big)\\
&+\frac{3i}{4}W^{-1}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{j}\varepsilon{}^{r i}\big(\nabla_{a}W{}_{\eta}{}^{\delta}\big)W{}_{\gamma \delta} +\frac{3i}{4}W^{-1}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{j}\varepsilon{}^{r i}W{}_{\eta}{}^{\delta}\big(\nabla_{a}W{}_{\gamma \delta}\big)\\
&-\frac{3i}{16}W^{-1}(\Gamma{}^{a}){}^{\beta}{}_{\eta}\lambda{}_{\beta}{}^{j}\varepsilon{}^{r i}\big(\nabla_{a}W{}^{\gamma \delta}\big)W{}_{\gamma \delta} -\frac{3i}{16}W^{-1}(\Gamma{}^{a}){}^{\beta}{}_{\eta}\lambda{}_{\beta}{}^{j}\varepsilon{}^{r i}W{}^{\gamma \delta}\big(\nabla_{a}W{}_{\gamma \delta}\big)\\
&+\frac{3i}{16}W^{-1}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{j}\varepsilon{}^{r i}(\Gamma{}^{b}){}_{\gamma}{}^{\delta}\big(\nabla_{a}\nabla_{b}W{}_{\eta \delta}\big) -\frac{3}{8}W^{-1}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{j}\mathcal T{}_{a \eta}{}^{\delta}X{}_{\delta \gamma}{}^{r i}\\
&-\frac{3i}{64}W^{-1}(\Gamma{}^{a}){}^{\beta}{}_{\gamma}\lambda{}_{\beta}{}^{j}\mathcal T{}_{a \eta}{}^{\gamma}\varepsilon{}^{r i}Y +\frac{9i}{16}W^{-1}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{j}\mathcal T{}_{a \eta}{}^{\delta}\varepsilon{}^{r i}(\Gamma{}^{b}){}_{\delta}{}^{\rho}\big(\nabla_{b}W{}_{\gamma \rho}\big)\\
&+\frac{3i}{4}W^{-1}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{j}\mathcal T{}_{a \eta}{}^{\delta}\varepsilon{}^{r i}W{}_{\delta}{}^{\rho}W{}_{\gamma \rho} -\frac{3i}{16}W^{-1}(\Gamma{}^{a}){}^{\beta}{}_{\gamma}\lambda{}_{\beta}{}^{j}\mathcal T{}_{a \eta}{}^{\gamma}\varepsilon{}^{r i}W{}^{\delta \rho}W{}_{\delta \rho}\\
&+\frac{3i}{16}W^{-1}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{j}\mathcal T{}_{a \eta}{}^{\delta}\varepsilon{}^{r i}(\Gamma{}^{b}){}_{\gamma}{}^{\rho}\big(\nabla_{b}W{}_{\delta \rho}\big) -\frac{3}{16}W^{-1}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{j}\mathcal R(M){}_{a \eta}{}^{r b c}(\Sigma{}_{b c}){}_{\gamma}{}^{\delta}X{}_{\delta}{}^{i}\\
&-\frac{9}{16}W^{-1}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{j}\mathcal R(\mathbb D){}_{a \eta}{}^{r}X{}_{\gamma}{}^{i} +\frac{3}{16}W^{-1}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{j}\mathcal R(J){}_{a \eta}{}^{r i k}X{}_{\gamma k}\\
&+\frac{3}{16}W^{-1}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{j}\mathcal R(J){}_{a \eta}{}^{r k i}X{}_{\gamma k} -\frac{3}{2}W^{-1}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{j}\mathcal R(S){}_{a \eta}{}^{r \delta i}W{}_{\delta \gamma}
\end{aligned}
\tag{S3-H1.7-b}
```

**Check for H1.7:** all 48 written summands have weight $`7/2`$, odd parity and the same free indices $`\eta;r,i,j`$. Dummy labels are paired. The coefficient $`1/3`$ and the two external epsilons are applied once, when collecting the spinor.

### 4.6 Differentiate every input in the $`W^{-2}`$ sector

<!-- ASSERT_CONVENTION: source_frame=Gold traceless Standard-Weyl superspace, derivative_parity=odd left, fermions=all degrees retained -->

#### Input H2.1

The calculated input is

```math
\left.H^{ij}\right|_{\mathrm{H2.1}}=W^{-2}\big(\frac12X^{ij}\Box W\big).
\tag{S3-H2.1-input}
```

Apply the product rule (S3-09), in the displayed factor order:

```math
\begin{aligned}
\left.\nabla_\eta^rH^{ij}\right|_{\mathrm{H2.1}}=&\frac{1}{2}\nabla_{\eta}^{r}\big(W^{-2}\big)X{}^{i j}\big(\nabla^{a}\nabla_{a}W\big) +\frac{1}{2}W^{-2}\nabla_{\eta}^{r}\big(X{}^{i j}\big)\big(\nabla^{a}\nabla_{a}W\big)\\
&+\frac{1}{2}W^{-2}X{}^{i j}\nabla_{\eta}^{r}\big(\nabla^{a}\nabla_{a}W\big)
\end{aligned}
\tag{S3-H2.1-a}
```

Insert the elementary source identities and the applicable commutators (S3-11)–(S3-14), distribute the vector product rules, and contract only index-raising metrics. The resulting contribution is

```math
\begin{aligned}
\left.\nabla_\eta^rH^{ij}\right|_{\mathrm{H2.1}}=&-iW^{-3}\lambda{}_{\eta}{}^{r}X{}^{i j}\big(\nabla^{a}\nabla_{a}W\big) +\frac{i}{2}W^{-2}\varepsilon{}^{r i}(\Gamma{}^{a}){}_{\eta}{}^{\beta}\big(\nabla_{a}\lambda{}_{\beta}{}^{j}\big)\big(\nabla^{b}\nabla_{b}W\big)\\
&-\frac{i}{4}W^{-2}\varepsilon{}^{r i}W{}_{\eta \beta}\lambda{}^{\beta j}\big(\nabla^{a}\nabla_{a}W\big) -\frac{3}{8}W^{-1}\varepsilon{}^{r i}X{}_{\eta}{}^{j}\big(\nabla^{a}\nabla_{a}W\big)\\
&+\frac{i}{2}W^{-2}\varepsilon{}^{r j}(\Gamma{}^{a}){}_{\eta}{}^{\beta}\big(\nabla_{a}\lambda{}_{\beta}{}^{i}\big)\big(\nabla^{b}\nabla_{b}W\big) -\frac{i}{4}W^{-2}\varepsilon{}^{r j}W{}_{\eta \beta}\lambda{}^{\beta i}\big(\nabla^{a}\nabla_{a}W\big)\\
&-\frac{3}{8}W^{-1}\varepsilon{}^{r j}X{}_{\eta}{}^{i}\big(\nabla^{a}\nabla_{a}W\big) +\frac{i}{2}W^{-2}X{}^{i j}\big(\nabla^{a}\nabla_{a}\lambda{}_{\eta}{}^{r}\big)\\
&+\frac{i}{2}W^{-2}X{}^{i j}\big(\nabla^{a}\mathcal T{}_{a \eta}{}^{\beta}\big)\lambda{}_{\beta}{}^{r} +\frac{i}{2}W^{-2}X{}^{i j}\mathcal T{}_{a \eta}{}^{\beta}\big(\nabla^{a}\lambda{}_{\beta}{}^{r}\big)\\
&+\frac{1}{2}W^{-1}X{}^{i j}\big(\nabla^{a}\mathcal R(\mathbb D){}_{a \eta}{}^{r}\big) +\frac{1}{2}W^{-2}X{}^{i j}\mathcal R(\mathbb D){}_{a \eta}{}^{r}\big(\nabla^{a}W\big)\\
&+\frac{i}{2}W^{-2}X{}^{i j}\mathcal T{}^{a}{}_{\eta}{}^{\beta}\big(\nabla_{a}\lambda{}_{\beta}{}^{r}\big) +\frac{i}{2}W^{-2}X{}^{i j}\mathcal T{}^{a}{}_{\eta}{}^{\beta}\mathcal T{}_{a \beta}{}^{\gamma}\lambda{}_{\gamma}{}^{r}\\
&+\frac{1}{2}W^{-1}X{}^{i j}\mathcal T{}^{a}{}_{\eta}{}^{\beta}\mathcal R(\mathbb D){}_{a \beta}{}^{r} +\frac{1}{4}W^{-2}X{}^{i j}\mathcal R(M){}^{a}{}_{\eta}{}^{r}{}_{a}{}^{b}\big(\nabla_{b}W\big)\\
&-\frac{1}{4}W^{-2}X{}^{i j}\mathcal R(M){}^{a}{}_{\eta}{}^{r b}{}_{a}\big(\nabla_{b}W\big) +W^{-2}X{}^{i j}\mathcal R(\mathbb D){}^{a}{}_{\eta}{}^{r}\big(\nabla_{a}W\big)\\
&-\frac{1}{2}W^{-2}X{}^{i j}\mathcal R(S){}^{a}{}_{\eta}{}^{r \beta k}(\Gamma{}_{a}){}_{\beta}{}^{\gamma}\lambda{}_{\gamma k} +W^{-1}X{}^{i j}\mathcal R(K){}_{a \eta}{}^{r a}
\end{aligned}
\tag{S3-H2.1-b}
```

**Check for H2.1:** all 20 written summands have weight $`7/2`$, odd parity and the same free indices $`\eta;r,i,j`$. Dummy labels are paired. The coefficient $`1/3`$ and the two external epsilons are applied once, when collecting the spinor.

#### Input H2.2

The calculated input is

```math
\left.H^{ij}\right|_{\mathrm{H2.2}}=W^{-2}\big(\frac12(\nabla^aW)\nabla_aX^{ij}\big).
\tag{S3-H2.2-input}
```

Expand each written SU(2) average with weight $`1/2`$ before applying the left derivative.

Apply the product rule (S3-09), in the displayed factor order:

```math
\begin{aligned}
\left.\nabla_\eta^rH^{ij}\right|_{\mathrm{H2.2}}=&\frac{1}{2}\nabla_{\eta}^{r}\big(W^{-2}\big)\big(\nabla^{a}W\big)\big(\nabla_{a}X{}^{i j}\big) +\frac{1}{2}W^{-2}\nabla_{\eta}^{r}\big(\nabla^{a}W\big)\big(\nabla_{a}X{}^{i j}\big)\\
&+\frac{1}{2}W^{-2}\big(\nabla^{a}W\big)\nabla_{\eta}^{r}\big(\nabla_{a}X{}^{i j}\big)
\end{aligned}
\tag{S3-H2.2-a}
```

Insert the elementary source identities and the applicable commutators (S3-11)–(S3-14), distribute the vector product rules, and contract only index-raising metrics. The resulting contribution is

```math
\begin{aligned}
\left.\nabla_\eta^rH^{ij}\right|_{\mathrm{H2.2}}=&-iW^{-3}\lambda{}_{\eta}{}^{r}\big(\nabla^{a}W\big)\big(\nabla_{a}X{}^{i j}\big) +\frac{i}{2}W^{-2}\big(\nabla^{a}\lambda{}_{\eta}{}^{r}\big)\big(\nabla_{a}X{}^{i j}\big)\\
&+\frac{i}{2}W^{-2}\mathcal T{}^{a}{}_{\eta}{}^{\beta}\lambda{}_{\beta}{}^{r}\big(\nabla_{a}X{}^{i j}\big) +\frac{1}{2}W^{-1}\mathcal R(\mathbb D){}^{a}{}_{\eta}{}^{r}\big(\nabla_{a}X{}^{i j}\big)\\
&+\frac{i}{2}W^{-2}\big(\nabla^{a}W\big)\varepsilon{}^{r i}(\Gamma{}^{b}){}_{\eta}{}^{\beta}\big(\nabla_{a}\nabla_{b}\lambda{}_{\beta}{}^{j}\big) -\frac{i}{4}W^{-2}\big(\nabla^{a}W\big)\varepsilon{}^{r i}\big(\nabla_{a}W{}_{\eta \beta}\big)\lambda{}^{\beta j}\\
&-\frac{i}{4}W^{-2}\big(\nabla^{a}W\big)\varepsilon{}^{r i}W{}_{\eta \beta}\big(\nabla_{a}\lambda{}^{\beta j}\big) -\frac{3}{8}W^{-1}\big(\nabla^{a}W\big)\varepsilon{}^{r i}\big(\nabla_{a}X{}_{\eta}{}^{j}\big)\\
&-\frac{3}{8}W^{-2}\big(\nabla^{a}W\big)\varepsilon{}^{r i}X{}_{\eta}{}^{j}\big(\nabla_{a}W\big) +\frac{i}{2}W^{-2}\big(\nabla^{a}W\big)\varepsilon{}^{r j}(\Gamma{}^{b}){}_{\eta}{}^{\beta}\big(\nabla_{a}\nabla_{b}\lambda{}_{\beta}{}^{i}\big)\\
&-\frac{i}{4}W^{-2}\big(\nabla^{a}W\big)\varepsilon{}^{r j}\big(\nabla_{a}W{}_{\eta \beta}\big)\lambda{}^{\beta i} -\frac{i}{4}W^{-2}\big(\nabla^{a}W\big)\varepsilon{}^{r j}W{}_{\eta \beta}\big(\nabla_{a}\lambda{}^{\beta i}\big)\\
&-\frac{3}{8}W^{-1}\big(\nabla^{a}W\big)\varepsilon{}^{r j}\big(\nabla_{a}X{}_{\eta}{}^{i}\big) -\frac{3}{8}W^{-2}\big(\nabla^{a}W\big)\varepsilon{}^{r j}X{}_{\eta}{}^{i}\big(\nabla_{a}W\big)\\
&+\frac{i}{2}W^{-2}\big(\nabla^{a}W\big)\mathcal T{}_{a \eta}{}^{\beta}\varepsilon{}^{r i}(\Gamma{}^{b}){}_{\beta}{}^{\gamma}\big(\nabla_{b}\lambda{}_{\gamma}{}^{j}\big) -\frac{i}{4}W^{-2}\big(\nabla^{a}W\big)\mathcal T{}_{a \eta}{}^{\beta}\varepsilon{}^{r i}W{}_{\beta \gamma}\lambda{}^{\gamma j}\\
&-\frac{3}{8}W^{-1}\big(\nabla^{a}W\big)\mathcal T{}_{a \eta}{}^{\beta}\varepsilon{}^{r i}X{}_{\beta}{}^{j} +\frac{i}{2}W^{-2}\big(\nabla^{a}W\big)\mathcal T{}_{a \eta}{}^{\beta}\varepsilon{}^{r j}(\Gamma{}^{b}){}_{\beta}{}^{\gamma}\big(\nabla_{b}\lambda{}_{\gamma}{}^{i}\big)\\
&-\frac{i}{4}W^{-2}\big(\nabla^{a}W\big)\mathcal T{}_{a \eta}{}^{\beta}\varepsilon{}^{r j}W{}_{\beta \gamma}\lambda{}^{\gamma i} -\frac{3}{8}W^{-1}\big(\nabla^{a}W\big)\mathcal T{}_{a \eta}{}^{\beta}\varepsilon{}^{r j}X{}_{\beta}{}^{i}\\
&+W^{-2}\big(\nabla^{a}W\big)\mathcal R(\mathbb D){}_{a \eta}{}^{r}X{}^{i j} -\frac{1}{4}W^{-2}\big(\nabla^{a}W\big)\mathcal R(J){}_{a \eta}{}^{r i k}X{}_{k}{}^{j}\\
&-\frac{1}{4}W^{-2}\big(\nabla^{a}W\big)\mathcal R(J){}_{a \eta}{}^{r k i}X{}_{k}{}^{j} -\frac{1}{4}W^{-2}\big(\nabla^{a}W\big)\mathcal R(J){}_{a \eta}{}^{r j k}X{}^{i}{}_{k}\\
&-\frac{1}{4}W^{-2}\big(\nabla^{a}W\big)\mathcal R(J){}_{a \eta}{}^{r k j}X{}^{i}{}_{k} -\frac{1}{2}W^{-2}\big(\nabla^{a}W\big)\mathcal R(S){}_{a \eta}{}^{r \beta i}\lambda{}_{\beta}{}^{j}\\
&-\frac{1}{2}W^{-2}\big(\nabla^{a}W\big)\mathcal R(S){}_{a \eta}{}^{r \beta j}\lambda{}_{\beta}{}^{i}
\end{aligned}
\tag{S3-H2.2-b}
```

**Check for H2.2:** all 27 written summands have weight $`7/2`$, odd parity and the same free indices $`\eta;r,i,j`$. Dummy labels are paired. The coefficient $`1/3`$ and the two external epsilons are applied once, when collecting the spinor.

#### Input H2.3

The calculated input is

```math
\left.H^{ij}\right|_{\mathrm{H2.3}}=W^{-2}\big(\frac14F^{ab}W_{ab}^{\alpha(i}\lambda_\alpha^{j)}\big).
\tag{S3-H2.3-input}
```

Expand each written SU(2) average with weight $`1/2`$ before applying the left derivative.

Apply the product rule (S3-09), in the displayed factor order:

```math
\begin{aligned}
\left.\nabla_\eta^rH^{ij}\right|_{\mathrm{H2.3}}=&\frac{1}{8}\nabla_{\eta}^{r}\big(W^{-2}\big)F{}^{a b}W{}_{a b}{}^{\beta i}\lambda{}_{\beta}{}^{j} +\frac{1}{8}W^{-2}\nabla_{\eta}^{r}\big(F{}^{a b}\big)W{}_{a b}{}^{\beta i}\lambda{}_{\beta}{}^{j}\\
&+\frac{1}{8}W^{-2}F{}^{a b}\nabla_{\eta}^{r}\big(W{}_{a b}{}^{\beta i}\big)\lambda{}_{\beta}{}^{j} -\frac{1}{8}W^{-2}F{}^{a b}W{}_{a b}{}^{\beta i}\nabla_{\eta}^{r}\big(\lambda{}_{\beta}{}^{j}\big)\\
&+\frac{1}{8}\nabla_{\eta}^{r}\big(W^{-2}\big)F{}^{a b}W{}_{a b}{}^{\beta j}\lambda{}_{\beta}{}^{i} +\frac{1}{8}W^{-2}\nabla_{\eta}^{r}\big(F{}^{a b}\big)W{}_{a b}{}^{\beta j}\lambda{}_{\beta}{}^{i}\\
&+\frac{1}{8}W^{-2}F{}^{a b}\nabla_{\eta}^{r}\big(W{}_{a b}{}^{\beta j}\big)\lambda{}_{\beta}{}^{i} -\frac{1}{8}W^{-2}F{}^{a b}W{}_{a b}{}^{\beta j}\nabla_{\eta}^{r}\big(\lambda{}_{\beta}{}^{i}\big)
\end{aligned}
\tag{S3-H2.3-a}
```

Insert the elementary source identities and the applicable commutators (S3-11)–(S3-14), distribute the vector product rules, and contract only index-raising metrics. The resulting contribution is

```math
\begin{aligned}
\left.\nabla_\eta^rH^{ij}\right|_{\mathrm{H2.3}}=&-\frac{i}{4}W^{-3}\lambda{}_{\eta}{}^{r}F{}^{a b}W{}_{a b}{}^{\beta i}\lambda{}_{\beta}{}^{j} -\frac{i}{16}W^{-2}(\Sigma{}^{a b}){}^{\beta \gamma}(\Gamma{}^{c}){}_{\eta \beta}\big(\nabla_{c}\lambda{}_{\gamma}{}^{r}\big)W{}_{a b}{}^{\delta i}\lambda{}_{\delta}{}^{j}\\
&-\frac{i}{16}W^{-2}(\Sigma{}^{a b}){}_{\eta}{}^{\beta}(\Gamma{}^{c}){}_{\beta}{}^{\gamma}\big(\nabla_{c}\lambda{}_{\gamma}{}^{r}\big)W{}_{a b}{}^{\delta i}\lambda{}_{\delta}{}^{j} +\frac{i}{32}W^{-2}(\Sigma{}^{a b}){}^{\beta \gamma}W{}_{\eta \beta}\lambda{}_{\gamma}{}^{r}W{}_{a b}{}^{\delta i}\lambda{}_{\delta}{}^{j}\\
&-\frac{3i}{32}W^{-2}(\Sigma{}^{a b}){}_{\eta}{}^{\beta}W{}_{\beta}{}^{\gamma}\lambda{}_{\gamma}{}^{r}W{}_{a b}{}^{\delta i}\lambda{}_{\delta}{}^{j} -\frac{i}{16}W^{-2}(\Sigma{}^{a b}){}^{\beta \gamma}(\Gamma{}^{c}){}_{\eta \gamma}\big(\nabla_{c}\lambda{}_{\beta}{}^{r}\big)W{}_{a b}{}^{\delta i}\lambda{}_{\delta}{}^{j}\\
&-\frac{i}{16}W^{-2}(\Sigma{}^{a b}){}^{\beta}{}_{\eta}(\Gamma{}^{c}){}_{\beta}{}^{\gamma}\big(\nabla_{c}\lambda{}_{\gamma}{}^{r}\big)W{}_{a b}{}^{\delta i}\lambda{}_{\delta}{}^{j} +\frac{i}{32}W^{-2}(\Sigma{}^{a b}){}^{\beta \gamma}W{}_{\eta \gamma}\lambda{}_{\beta}{}^{r}W{}_{a b}{}^{\delta i}\lambda{}_{\delta}{}^{j}\\
&-\frac{3i}{32}W^{-2}(\Sigma{}^{a b}){}^{\beta}{}_{\eta}W{}_{\beta}{}^{\gamma}\lambda{}_{\gamma}{}^{r}W{}_{a b}{}^{\delta i}\lambda{}_{\delta}{}^{j} -\frac{3i}{16}W^{-2}(\Sigma{}^{a b}){}^{\beta \gamma}W{}_{\beta \gamma}\lambda{}_{\eta}{}^{r}W{}_{a b}{}^{\delta i}\lambda{}_{\delta}{}^{j}\\
&-\frac{1}{8}W^{-1}(\Sigma{}^{a b}){}^{\beta \gamma}W{}_{\eta \beta \gamma}{}^{r}W{}_{a b}{}^{\delta i}\lambda{}_{\delta}{}^{j} -\frac{1}{16}W^{-2}F{}^{a b}(\Sigma{}_{a b}){}^{\beta \gamma}\varepsilon{}^{r i}W{}_{\eta \beta \gamma}{}^{\delta}\lambda{}_{\delta}{}^{j}\\
&-\frac{i}{16}W^{-2}F{}^{a b}(\Sigma{}_{a b}){}^{\beta \gamma}\varepsilon{}^{r i}(\Gamma{}^{c}){}_{\eta \beta}\big(\nabla_{c}W{}_{\gamma}{}^{\delta}\big)\lambda{}_{\delta}{}^{j} -\frac{1}{16}W^{-2}F{}^{a b}(\Sigma{}_{a b}){}_{\eta}{}^{\beta}X{}_{\beta}{}^{\gamma r i}\lambda{}_{\gamma}{}^{j}\\
&-\frac{i}{16}W^{-2}F{}^{a b}(\Sigma{}_{a b}){}^{\beta \gamma}\varepsilon{}^{r i}(\Gamma{}^{c}){}_{\eta \gamma}\big(\nabla_{c}W{}_{\beta}{}^{\delta}\big)\lambda{}_{\delta}{}^{j} -\frac{1}{16}W^{-2}F{}^{a b}(\Sigma{}_{a b}){}^{\beta}{}_{\eta}X{}_{\beta}{}^{\gamma r i}\lambda{}_{\gamma}{}^{j}\\
&-\frac{i}{16}W^{-2}F{}^{a b}(\Sigma{}_{a b}){}^{\beta \gamma}\varepsilon{}^{r i}(\Gamma{}^{c}){}_{\eta}{}^{\delta}\big(\nabla_{c}W{}_{\beta \gamma}\big)\lambda{}_{\delta}{}^{j} +\frac{1}{16}W^{-2}F{}^{a b}(\Sigma{}_{a b}){}^{\beta \gamma}X{}_{\beta \gamma}{}^{r i}\lambda{}_{\eta}{}^{j}\\
&-\frac{i}{32}W^{-2}F{}^{a b}(\Sigma{}_{a b}){}_{\eta}{}^{\beta}\varepsilon{}^{r i}(\Gamma{}^{c}){}_{\beta}{}^{\gamma}\big(\nabla_{c}W{}^{\delta}{}_{\gamma}\big)\lambda{}_{\delta}{}^{j} -\frac{i}{32}W^{-2}F{}^{a b}(\Sigma{}_{a b}){}_{\eta}{}^{\beta}\varepsilon{}^{r i}(\Gamma{}^{c}){}^{\gamma \delta}\big(\nabla_{c}W{}_{\beta \delta}\big)\lambda{}_{\gamma}{}^{j}\\
&-\frac{i}{32}W^{-2}F{}^{a b}(\Sigma{}_{a b}){}^{\beta}{}_{\eta}\varepsilon{}^{r i}(\Gamma{}^{c}){}_{\beta}{}^{\gamma}\big(\nabla_{c}W{}^{\delta}{}_{\gamma}\big)\lambda{}_{\delta}{}^{j} -\frac{i}{32}W^{-2}F{}^{a b}(\Sigma{}_{a b}){}^{\beta}{}_{\eta}\varepsilon{}^{r i}(\Gamma{}^{c}){}^{\gamma \delta}\big(\nabla_{c}W{}_{\beta \delta}\big)\lambda{}_{\gamma}{}^{j}\\
&+\frac{i}{32}W^{-2}F{}^{a b}(\Sigma{}_{a b}){}^{\beta \gamma}\varepsilon{}^{r i}(\Gamma{}^{c}){}_{\beta}{}^{\delta}\big(\nabla_{c}W{}_{\gamma \delta}\big)\lambda{}_{\eta}{}^{j} +\frac{i}{32}W^{-2}F{}^{a b}(\Sigma{}_{a b}){}^{\beta \gamma}\varepsilon{}^{r i}(\Gamma{}^{c}){}_{\gamma}{}^{\delta}\big(\nabla_{c}W{}_{\beta \delta}\big)\lambda{}_{\eta}{}^{j}\\
&+\frac{1}{4}W^{-2}F{}^{a b}W{}_{a b}{}^{\beta i}\varepsilon{}^{r j}F{}_{\eta \beta} +\frac{1}{4}W^{-1}F{}^{a b}W{}_{a b}{}^{\beta i}\varepsilon{}^{r j}W{}_{\eta \beta}\\
&+\frac{1}{8}W^{-2}F{}^{a b}W{}_{a b \eta}{}^{i}X{}^{r j} +\frac{1}{8}W^{-2}F{}^{a b}W{}_{a b}{}^{\beta i}\varepsilon{}^{r j}(\Gamma{}^{c}){}_{\eta \beta}\big(\nabla_{c}W\big)\\
&-\frac{i}{4}W^{-3}\lambda{}_{\eta}{}^{r}F{}^{a b}W{}_{a b}{}^{\beta j}\lambda{}_{\beta}{}^{i} -\frac{i}{16}W^{-2}(\Sigma{}^{a b}){}^{\beta \gamma}(\Gamma{}^{c}){}_{\eta \beta}\big(\nabla_{c}\lambda{}_{\gamma}{}^{r}\big)W{}_{a b}{}^{\delta j}\lambda{}_{\delta}{}^{i}\\
&-\frac{i}{16}W^{-2}(\Sigma{}^{a b}){}_{\eta}{}^{\beta}(\Gamma{}^{c}){}_{\beta}{}^{\gamma}\big(\nabla_{c}\lambda{}_{\gamma}{}^{r}\big)W{}_{a b}{}^{\delta j}\lambda{}_{\delta}{}^{i} +\frac{i}{32}W^{-2}(\Sigma{}^{a b}){}^{\beta \gamma}W{}_{\eta \beta}\lambda{}_{\gamma}{}^{r}W{}_{a b}{}^{\delta j}\lambda{}_{\delta}{}^{i}\\
&-\frac{3i}{32}W^{-2}(\Sigma{}^{a b}){}_{\eta}{}^{\beta}W{}_{\beta}{}^{\gamma}\lambda{}_{\gamma}{}^{r}W{}_{a b}{}^{\delta j}\lambda{}_{\delta}{}^{i} -\frac{i}{16}W^{-2}(\Sigma{}^{a b}){}^{\beta \gamma}(\Gamma{}^{c}){}_{\eta \gamma}\big(\nabla_{c}\lambda{}_{\beta}{}^{r}\big)W{}_{a b}{}^{\delta j}\lambda{}_{\delta}{}^{i}\\
&-\frac{i}{16}W^{-2}(\Sigma{}^{a b}){}^{\beta}{}_{\eta}(\Gamma{}^{c}){}_{\beta}{}^{\gamma}\big(\nabla_{c}\lambda{}_{\gamma}{}^{r}\big)W{}_{a b}{}^{\delta j}\lambda{}_{\delta}{}^{i} +\frac{i}{32}W^{-2}(\Sigma{}^{a b}){}^{\beta \gamma}W{}_{\eta \gamma}\lambda{}_{\beta}{}^{r}W{}_{a b}{}^{\delta j}\lambda{}_{\delta}{}^{i}\\
&-\frac{3i}{32}W^{-2}(\Sigma{}^{a b}){}^{\beta}{}_{\eta}W{}_{\beta}{}^{\gamma}\lambda{}_{\gamma}{}^{r}W{}_{a b}{}^{\delta j}\lambda{}_{\delta}{}^{i} -\frac{3i}{16}W^{-2}(\Sigma{}^{a b}){}^{\beta \gamma}W{}_{\beta \gamma}\lambda{}_{\eta}{}^{r}W{}_{a b}{}^{\delta j}\lambda{}_{\delta}{}^{i}\\
&-\frac{1}{8}W^{-1}(\Sigma{}^{a b}){}^{\beta \gamma}W{}_{\eta \beta \gamma}{}^{r}W{}_{a b}{}^{\delta j}\lambda{}_{\delta}{}^{i} -\frac{1}{16}W^{-2}F{}^{a b}(\Sigma{}_{a b}){}^{\beta \gamma}\varepsilon{}^{r j}W{}_{\eta \beta \gamma}{}^{\delta}\lambda{}_{\delta}{}^{i}\\
&-\frac{i}{16}W^{-2}F{}^{a b}(\Sigma{}_{a b}){}^{\beta \gamma}\varepsilon{}^{r j}(\Gamma{}^{c}){}_{\eta \beta}\big(\nabla_{c}W{}_{\gamma}{}^{\delta}\big)\lambda{}_{\delta}{}^{i} -\frac{1}{16}W^{-2}F{}^{a b}(\Sigma{}_{a b}){}_{\eta}{}^{\beta}X{}_{\beta}{}^{\gamma r j}\lambda{}_{\gamma}{}^{i}\\
&-\frac{i}{16}W^{-2}F{}^{a b}(\Sigma{}_{a b}){}^{\beta \gamma}\varepsilon{}^{r j}(\Gamma{}^{c}){}_{\eta \gamma}\big(\nabla_{c}W{}_{\beta}{}^{\delta}\big)\lambda{}_{\delta}{}^{i} -\frac{1}{16}W^{-2}F{}^{a b}(\Sigma{}_{a b}){}^{\beta}{}_{\eta}X{}_{\beta}{}^{\gamma r j}\lambda{}_{\gamma}{}^{i}\\
&-\frac{i}{16}W^{-2}F{}^{a b}(\Sigma{}_{a b}){}^{\beta \gamma}\varepsilon{}^{r j}(\Gamma{}^{c}){}_{\eta}{}^{\delta}\big(\nabla_{c}W{}_{\beta \gamma}\big)\lambda{}_{\delta}{}^{i} +\frac{1}{16}W^{-2}F{}^{a b}(\Sigma{}_{a b}){}^{\beta \gamma}X{}_{\beta \gamma}{}^{r j}\lambda{}_{\eta}{}^{i}\\
&-\frac{i}{32}W^{-2}F{}^{a b}(\Sigma{}_{a b}){}_{\eta}{}^{\beta}\varepsilon{}^{r j}(\Gamma{}^{c}){}_{\beta}{}^{\gamma}\big(\nabla_{c}W{}^{\delta}{}_{\gamma}\big)\lambda{}_{\delta}{}^{i} -\frac{i}{32}W^{-2}F{}^{a b}(\Sigma{}_{a b}){}_{\eta}{}^{\beta}\varepsilon{}^{r j}(\Gamma{}^{c}){}^{\gamma \delta}\big(\nabla_{c}W{}_{\beta \delta}\big)\lambda{}_{\gamma}{}^{i}\\
&-\frac{i}{32}W^{-2}F{}^{a b}(\Sigma{}_{a b}){}^{\beta}{}_{\eta}\varepsilon{}^{r j}(\Gamma{}^{c}){}_{\beta}{}^{\gamma}\big(\nabla_{c}W{}^{\delta}{}_{\gamma}\big)\lambda{}_{\delta}{}^{i} -\frac{i}{32}W^{-2}F{}^{a b}(\Sigma{}_{a b}){}^{\beta}{}_{\eta}\varepsilon{}^{r j}(\Gamma{}^{c}){}^{\gamma \delta}\big(\nabla_{c}W{}_{\beta \delta}\big)\lambda{}_{\gamma}{}^{i}\\
&+\frac{i}{32}W^{-2}F{}^{a b}(\Sigma{}_{a b}){}^{\beta \gamma}\varepsilon{}^{r j}(\Gamma{}^{c}){}_{\beta}{}^{\delta}\big(\nabla_{c}W{}_{\gamma \delta}\big)\lambda{}_{\eta}{}^{i} +\frac{i}{32}W^{-2}F{}^{a b}(\Sigma{}_{a b}){}^{\beta \gamma}\varepsilon{}^{r j}(\Gamma{}^{c}){}_{\gamma}{}^{\delta}\big(\nabla_{c}W{}_{\beta \delta}\big)\lambda{}_{\eta}{}^{i}\\
&+\frac{1}{4}W^{-2}F{}^{a b}W{}_{a b}{}^{\beta j}\varepsilon{}^{r i}F{}_{\eta \beta} +\frac{1}{4}W^{-1}F{}^{a b}W{}_{a b}{}^{\beta j}\varepsilon{}^{r i}W{}_{\eta \beta}\\
&+\frac{1}{8}W^{-2}F{}^{a b}W{}_{a b \eta}{}^{j}X{}^{r i} +\frac{1}{8}W^{-2}F{}^{a b}W{}_{a b}{}^{\beta j}\varepsilon{}^{r i}(\Gamma{}^{c}){}_{\eta \beta}\big(\nabla_{c}W\big)
\end{aligned}
\tag{S3-H2.3-b}
```

**Check for H2.3:** all 56 written summands have weight $`7/2`$, odd parity and the same free indices $`\eta;r,i,j`$. Dummy labels are paired. The coefficient $`1/3`$ and the two external epsilons are applied once, when collecting the spinor.

#### Input H2.4

The calculated input is

```math
\left.H^{ij}\right|_{\mathrm{H2.4}}=W^{-2}\big(-\frac i2\lambda^{\alpha(j}\Box\lambda_\alpha^{i)}\big).
\tag{S3-H2.4-input}
```

Expand each written SU(2) average with weight $`1/2`$ before applying the left derivative.

Apply the product rule (S3-09), in the displayed factor order:

```math
\begin{aligned}
\left.\nabla_\eta^rH^{ij}\right|_{\mathrm{H2.4}}=&-\frac{i}{4}\nabla_{\eta}^{r}\big(W^{-2}\big)\lambda{}^{\beta j}\big(\nabla^{a}\nabla_{a}\lambda{}_{\beta}{}^{i}\big) -\frac{i}{4}W^{-2}\nabla_{\eta}^{r}\big(\lambda{}^{\beta j}\big)\big(\nabla^{a}\nabla_{a}\lambda{}_{\beta}{}^{i}\big)\\
&+\frac{i}{4}W^{-2}\lambda{}^{\beta j}\nabla_{\eta}^{r}\big(\nabla^{a}\nabla_{a}\lambda{}_{\beta}{}^{i}\big) -\frac{i}{4}\nabla_{\eta}^{r}\big(W^{-2}\big)\lambda{}^{\beta i}\big(\nabla^{a}\nabla_{a}\lambda{}_{\beta}{}^{j}\big)\\
&-\frac{i}{4}W^{-2}\nabla_{\eta}^{r}\big(\lambda{}^{\beta i}\big)\big(\nabla^{a}\nabla_{a}\lambda{}_{\beta}{}^{j}\big) +\frac{i}{4}W^{-2}\lambda{}^{\beta i}\nabla_{\eta}^{r}\big(\nabla^{a}\nabla_{a}\lambda{}_{\beta}{}^{j}\big)
\end{aligned}
\tag{S3-H2.4-a}
```

Insert the elementary source identities and the applicable commutators (S3-11)–(S3-14), distribute the vector product rules, and contract only index-raising metrics. The resulting contribution is

```math
\begin{aligned}
\left.\nabla_\eta^rH^{ij}\right|_{\mathrm{H2.4}}=&-\frac{1}{2}W^{-3}\lambda{}_{\eta}{}^{r}\lambda{}^{\beta j}\big(\nabla^{a}\nabla_{a}\lambda{}_{\beta}{}^{i}\big) +\frac{i}{2}W^{-2}\varepsilon{}^{r j}F{}_{\eta}{}^{\beta}\big(\nabla^{a}\nabla_{a}\lambda{}_{\beta}{}^{i}\big)\\
&+\frac{i}{2}W^{-1}\varepsilon{}^{r j}W{}_{\eta}{}^{\beta}\big(\nabla^{a}\nabla_{a}\lambda{}_{\beta}{}^{i}\big) -\frac{i}{4}W^{-2}X{}^{r j}\big(\nabla^{a}\nabla_{a}\lambda{}_{\eta}{}^{i}\big)\\
&+\frac{i}{4}W^{-2}\varepsilon{}^{r j}(\Gamma{}^{a}){}_{\eta}{}^{\beta}\big(\nabla_{a}W\big)\big(\nabla^{b}\nabla_{b}\lambda{}_{\beta}{}^{i}\big) -\frac{i}{2}W^{-2}\lambda{}^{\beta j}\varepsilon{}^{r i}\big(\nabla^{a}\nabla_{a}F{}_{\eta \beta}\big)\\
&-\frac{i}{2}W^{-1}\lambda{}^{\beta j}\varepsilon{}^{r i}\big(\nabla^{a}\nabla_{a}W{}_{\eta \beta}\big) -\frac{i}{2}W^{-2}\lambda{}^{\beta j}\varepsilon{}^{r i}\big(\nabla_{a}W{}_{\eta \beta}\big)\big(\nabla^{a}W\big)\\
&-\frac{i}{2}W^{-2}\lambda{}^{\beta j}\varepsilon{}^{r i}\big(\nabla^{a}W{}_{\eta \beta}\big)\big(\nabla_{a}W\big) -\frac{i}{2}W^{-2}\lambda{}^{\beta j}\varepsilon{}^{r i}W{}_{\eta \beta}\big(\nabla^{a}\nabla_{a}W\big)\\
&-\frac{i}{4}W^{-2}\lambda{}_{\eta}{}^{j}\big(\nabla^{a}\nabla_{a}X{}^{r i}\big) -\frac{i}{4}W^{-2}\lambda{}^{\beta j}\varepsilon{}^{r i}(\Gamma{}^{a}){}_{\eta \beta}\big(\nabla^{b}\nabla_{b}\nabla_{a}W\big)\\
&-\frac{i}{2}W^{-2}\lambda{}^{\beta j}\big(\nabla^{a}\mathcal T{}_{a \eta}{}^{\gamma}\big)\varepsilon{}^{r i}F{}_{\gamma \beta} -\frac{i}{2}W^{-2}\lambda{}^{\beta j}\mathcal T{}_{a \eta}{}^{\gamma}\varepsilon{}^{r i}\big(\nabla^{a}F{}_{\gamma \beta}\big)\\
&-\frac{i}{2}W^{-1}\lambda{}^{\beta j}\big(\nabla^{a}\mathcal T{}_{a \eta}{}^{\gamma}\big)\varepsilon{}^{r i}W{}_{\gamma \beta} -\frac{i}{2}W^{-1}\lambda{}^{\beta j}\mathcal T{}_{a \eta}{}^{\gamma}\varepsilon{}^{r i}\big(\nabla^{a}W{}_{\gamma \beta}\big)\\
&-\frac{i}{2}W^{-2}\lambda{}^{\beta j}\mathcal T{}_{a \eta}{}^{\gamma}\varepsilon{}^{r i}W{}_{\gamma \beta}\big(\nabla^{a}W\big) -\frac{i}{4}W^{-2}\lambda{}_{\beta}{}^{j}\big(\nabla^{a}\mathcal T{}_{a \eta}{}^{\beta}\big)X{}^{r i}\\
&-\frac{i}{4}W^{-2}\lambda{}_{\beta}{}^{j}\mathcal T{}_{a \eta}{}^{\beta}\big(\nabla^{a}X{}^{r i}\big) -\frac{i}{4}W^{-2}\lambda{}^{\beta j}\big(\nabla^{a}\mathcal T{}_{a \eta}{}^{\gamma}\big)\varepsilon{}^{r i}(\Gamma{}^{b}){}_{\gamma \beta}\big(\nabla_{b}W\big)\\
&-\frac{i}{4}W^{-2}\lambda{}^{\beta j}\mathcal T{}_{a \eta}{}^{\gamma}\varepsilon{}^{r i}(\Gamma{}^{b}){}_{\gamma \beta}\big(\nabla^{a}\nabla_{b}W\big) +\frac{i}{8}W^{-2}\lambda{}^{\beta j}\big(\nabla^{a}\mathcal R(M){}_{a \eta}{}^{r b c}\big)(\Sigma{}_{b c}){}_{\beta}{}^{\gamma}\lambda{}_{\gamma}{}^{i}\\
&+\frac{i}{8}W^{-2}\lambda{}^{\beta j}\mathcal R(M){}_{a \eta}{}^{r b c}(\Sigma{}_{b c}){}_{\beta}{}^{\gamma}\big(\nabla^{a}\lambda{}_{\gamma}{}^{i}\big) +\frac{3i}{8}W^{-2}\lambda{}^{\beta j}\big(\nabla^{a}\mathcal R(\mathbb D){}_{a \eta}{}^{r}\big)\lambda{}_{\beta}{}^{i}\\
&+\frac{3i}{8}W^{-2}\lambda{}^{\beta j}\mathcal R(\mathbb D){}_{a \eta}{}^{r}\big(\nabla^{a}\lambda{}_{\beta}{}^{i}\big) -\frac{i}{8}W^{-2}\lambda{}^{\beta j}\big(\nabla^{a}\mathcal R(J){}_{a \eta}{}^{r i k}\big)\lambda{}_{\beta k}\\
&-\frac{i}{8}W^{-2}\lambda{}^{\beta j}\mathcal R(J){}_{a \eta}{}^{r i k}\big(\nabla^{a}\lambda{}_{\beta k}\big) -\frac{i}{8}W^{-2}\lambda{}^{\beta j}\big(\nabla^{a}\mathcal R(J){}_{a \eta}{}^{r k i}\big)\lambda{}_{\beta k}\\
&-\frac{i}{8}W^{-2}\lambda{}^{\beta j}\mathcal R(J){}_{a \eta}{}^{r k i}\big(\nabla^{a}\lambda{}_{\beta k}\big) +\frac{1}{2}W^{-1}\lambda{}_{\beta}{}^{j}\big(\nabla^{a}\mathcal R(S){}_{a \eta}{}^{r \beta i}\big)\\
&+\frac{1}{2}W^{-2}\lambda{}_{\beta}{}^{j}\mathcal R(S){}_{a \eta}{}^{r \beta i}\big(\nabla^{a}W\big) -\frac{i}{2}W^{-2}\lambda{}^{\beta j}\mathcal T{}^{a}{}_{\eta}{}^{\gamma}\varepsilon{}^{r i}\big(\nabla_{a}F{}_{\gamma \beta}\big)\\
&-\frac{i}{2}W^{-1}\lambda{}^{\beta j}\mathcal T{}^{a}{}_{\eta}{}^{\gamma}\varepsilon{}^{r i}\big(\nabla_{a}W{}_{\gamma \beta}\big) -\frac{i}{2}W^{-2}\lambda{}^{\beta j}\mathcal T{}^{a}{}_{\eta}{}^{\gamma}\varepsilon{}^{r i}W{}_{\gamma \beta}\big(\nabla_{a}W\big)\\
&-\frac{i}{4}W^{-2}\lambda{}_{\beta}{}^{j}\mathcal T{}^{a}{}_{\eta}{}^{\beta}\big(\nabla_{a}X{}^{r i}\big) -\frac{i}{4}W^{-2}\lambda{}^{\beta j}\mathcal T{}^{a}{}_{\eta}{}^{\gamma}\varepsilon{}^{r i}(\Gamma{}^{b}){}_{\gamma \beta}\big(\nabla_{a}\nabla_{b}W\big)\\
&-\frac{i}{2}W^{-2}\lambda{}^{\beta j}\mathcal T{}^{a}{}_{\eta}{}^{\gamma}\mathcal T{}_{a \gamma}{}^{\delta}\varepsilon{}^{r i}F{}_{\delta \beta} -\frac{i}{2}W^{-1}\lambda{}^{\beta j}\mathcal T{}^{a}{}_{\eta}{}^{\gamma}\mathcal T{}_{a \gamma}{}^{\delta}\varepsilon{}^{r i}W{}_{\delta \beta}\\
&-\frac{i}{4}W^{-2}\lambda{}_{\beta}{}^{j}\mathcal T{}^{a}{}_{\eta}{}^{\gamma}\mathcal T{}_{a \gamma}{}^{\beta}X{}^{r i} -\frac{i}{4}W^{-2}\lambda{}^{\beta j}\mathcal T{}^{a}{}_{\eta}{}^{\gamma}\mathcal T{}_{a \gamma}{}^{\delta}\varepsilon{}^{r i}(\Gamma{}^{b}){}_{\delta \beta}\big(\nabla_{b}W\big)\\
&+\frac{i}{8}W^{-2}\lambda{}^{\beta j}\mathcal T{}^{a}{}_{\eta}{}^{\gamma}\mathcal R(M){}_{a \gamma}{}^{r b c}(\Sigma{}_{b c}){}_{\beta}{}^{\delta}\lambda{}_{\delta}{}^{i} +\frac{3i}{8}W^{-2}\lambda{}^{\beta j}\mathcal T{}^{a}{}_{\eta}{}^{\gamma}\mathcal R(\mathbb D){}_{a \gamma}{}^{r}\lambda{}_{\beta}{}^{i}\\
&-\frac{i}{8}W^{-2}\lambda{}^{\beta j}\mathcal T{}^{a}{}_{\eta}{}^{\gamma}\mathcal R(J){}_{a \gamma}{}^{r i k}\lambda{}_{\beta k} -\frac{i}{8}W^{-2}\lambda{}^{\beta j}\mathcal T{}^{a}{}_{\eta}{}^{\gamma}\mathcal R(J){}_{a \gamma}{}^{r k i}\lambda{}_{\beta k}\\
&+\frac{1}{2}W^{-1}\lambda{}_{\beta}{}^{j}\mathcal T{}^{a}{}_{\eta}{}^{\gamma}\mathcal R(S){}_{a \gamma}{}^{r \beta i} +\frac{i}{8}W^{-2}\lambda{}^{\beta j}\mathcal R(M){}^{a}{}_{\eta}{}^{r}{}_{a}{}^{b}\big(\nabla_{b}\lambda{}_{\beta}{}^{i}\big)\\
&-\frac{i}{8}W^{-2}\lambda{}^{\beta j}\mathcal R(M){}^{a}{}_{\eta}{}^{r b}{}_{a}\big(\nabla_{b}\lambda{}_{\beta}{}^{i}\big) +\frac{i}{8}W^{-2}\lambda{}^{\beta j}\mathcal R(M){}^{a}{}_{\eta}{}^{r b c}(\Sigma{}_{b c}){}_{\beta}{}^{\gamma}\big(\nabla_{a}\lambda{}_{\gamma}{}^{i}\big)\\
&+\frac{5i}{8}W^{-2}\lambda{}^{\beta j}\mathcal R(\mathbb D){}^{a}{}_{\eta}{}^{r}\big(\nabla_{a}\lambda{}_{\beta}{}^{i}\big) -\frac{i}{8}W^{-2}\lambda{}^{\beta j}\mathcal R(J){}^{a}{}_{\eta}{}^{r i k}\big(\nabla_{a}\lambda{}_{\beta k}\big)\\
&-\frac{i}{8}W^{-2}\lambda{}^{\beta j}\mathcal R(J){}^{a}{}_{\eta}{}^{r k i}\big(\nabla_{a}\lambda{}_{\beta k}\big) +\frac{1}{2}W^{-2}\lambda{}_{\beta}{}^{j}\mathcal R(S){}^{a}{}_{\eta}{}^{r \beta i}\big(\nabla_{a}W\big)\\
&+\frac{1}{2}W^{-2}\lambda{}^{\beta j}\mathcal R(S){}^{a}{}_{\eta}{}^{r \gamma i}(\Gamma{}_{a}){}_{\gamma}{}^{\delta}F{}_{\delta \beta} +\frac{1}{2}W^{-1}\lambda{}^{\beta j}\mathcal R(S){}^{a}{}_{\eta}{}^{r \gamma i}(\Gamma{}_{a}){}_{\gamma}{}^{\delta}W{}_{\delta \beta}\\
&+\frac{1}{4}W^{-2}\lambda{}_{\beta}{}^{j}\mathcal R(S){}^{a}{}_{\eta}{}^{r \gamma k}(\Gamma{}_{a}){}_{\gamma}{}^{\beta}X{}_{k}{}^{i} +\frac{1}{4}W^{-2}\lambda{}^{\beta j}\mathcal R(S){}^{a}{}_{\eta}{}^{r \gamma i}(\Gamma{}_{a}){}_{\gamma}{}^{\delta}(\Gamma{}^{b}){}_{\delta \beta}\big(\nabla_{b}W\big)\\
&-\frac{1}{8}W^{-1}\lambda{}_{\beta}{}^{j}\mathcal R(S){}^{a}{}_{\eta}{}^{r \gamma i}W{}_{a}{}^{b}(\Gamma{}_{b}){}_{\gamma}{}^{\beta} +\frac{3i}{4}W^{-2}\lambda{}^{\beta j}\mathcal R(K){}_{a \eta}{}^{r a}\lambda{}_{\beta}{}^{i}\\
&+\frac{i}{2}W^{-2}\lambda{}^{\beta j}\mathcal R(K){}^{a}{}_{\eta}{}^{r b}(\Sigma{}_{b a}){}_{\beta}{}^{\gamma}\lambda{}_{\gamma}{}^{i} -\frac{1}{2}W^{-3}\lambda{}_{\eta}{}^{r}\lambda{}^{\beta i}\big(\nabla^{a}\nabla_{a}\lambda{}_{\beta}{}^{j}\big)\\
&+\frac{i}{2}W^{-2}\varepsilon{}^{r i}F{}_{\eta}{}^{\beta}\big(\nabla^{a}\nabla_{a}\lambda{}_{\beta}{}^{j}\big) +\frac{i}{2}W^{-1}\varepsilon{}^{r i}W{}_{\eta}{}^{\beta}\big(\nabla^{a}\nabla_{a}\lambda{}_{\beta}{}^{j}\big)\\
&-\frac{i}{4}W^{-2}X{}^{r i}\big(\nabla^{a}\nabla_{a}\lambda{}_{\eta}{}^{j}\big) +\frac{i}{4}W^{-2}\varepsilon{}^{r i}(\Gamma{}^{a}){}_{\eta}{}^{\beta}\big(\nabla_{a}W\big)\big(\nabla^{b}\nabla_{b}\lambda{}_{\beta}{}^{j}\big)\\
&-\frac{i}{2}W^{-2}\lambda{}^{\beta i}\varepsilon{}^{r j}\big(\nabla^{a}\nabla_{a}F{}_{\eta \beta}\big) -\frac{i}{2}W^{-1}\lambda{}^{\beta i}\varepsilon{}^{r j}\big(\nabla^{a}\nabla_{a}W{}_{\eta \beta}\big)\\
&-\frac{i}{2}W^{-2}\lambda{}^{\beta i}\varepsilon{}^{r j}\big(\nabla_{a}W{}_{\eta \beta}\big)\big(\nabla^{a}W\big) -\frac{i}{2}W^{-2}\lambda{}^{\beta i}\varepsilon{}^{r j}\big(\nabla^{a}W{}_{\eta \beta}\big)\big(\nabla_{a}W\big)\\
&-\frac{i}{2}W^{-2}\lambda{}^{\beta i}\varepsilon{}^{r j}W{}_{\eta \beta}\big(\nabla^{a}\nabla_{a}W\big) -\frac{i}{4}W^{-2}\lambda{}_{\eta}{}^{i}\big(\nabla^{a}\nabla_{a}X{}^{r j}\big)\\
&-\frac{i}{4}W^{-2}\lambda{}^{\beta i}\varepsilon{}^{r j}(\Gamma{}^{a}){}_{\eta \beta}\big(\nabla^{b}\nabla_{b}\nabla_{a}W\big) -\frac{i}{2}W^{-2}\lambda{}^{\beta i}\big(\nabla^{a}\mathcal T{}_{a \eta}{}^{\gamma}\big)\varepsilon{}^{r j}F{}_{\gamma \beta}\\
&-\frac{i}{2}W^{-2}\lambda{}^{\beta i}\mathcal T{}_{a \eta}{}^{\gamma}\varepsilon{}^{r j}\big(\nabla^{a}F{}_{\gamma \beta}\big) -\frac{i}{2}W^{-1}\lambda{}^{\beta i}\big(\nabla^{a}\mathcal T{}_{a \eta}{}^{\gamma}\big)\varepsilon{}^{r j}W{}_{\gamma \beta}\\
&-\frac{i}{2}W^{-1}\lambda{}^{\beta i}\mathcal T{}_{a \eta}{}^{\gamma}\varepsilon{}^{r j}\big(\nabla^{a}W{}_{\gamma \beta}\big) -\frac{i}{2}W^{-2}\lambda{}^{\beta i}\mathcal T{}_{a \eta}{}^{\gamma}\varepsilon{}^{r j}W{}_{\gamma \beta}\big(\nabla^{a}W\big)\\
&-\frac{i}{4}W^{-2}\lambda{}_{\beta}{}^{i}\big(\nabla^{a}\mathcal T{}_{a \eta}{}^{\beta}\big)X{}^{r j} -\frac{i}{4}W^{-2}\lambda{}_{\beta}{}^{i}\mathcal T{}_{a \eta}{}^{\beta}\big(\nabla^{a}X{}^{r j}\big)\\
&-\frac{i}{4}W^{-2}\lambda{}^{\beta i}\big(\nabla^{a}\mathcal T{}_{a \eta}{}^{\gamma}\big)\varepsilon{}^{r j}(\Gamma{}^{b}){}_{\gamma \beta}\big(\nabla_{b}W\big) -\frac{i}{4}W^{-2}\lambda{}^{\beta i}\mathcal T{}_{a \eta}{}^{\gamma}\varepsilon{}^{r j}(\Gamma{}^{b}){}_{\gamma \beta}\big(\nabla^{a}\nabla_{b}W\big)\\
&+\frac{i}{8}W^{-2}\lambda{}^{\beta i}\big(\nabla^{a}\mathcal R(M){}_{a \eta}{}^{r b c}\big)(\Sigma{}_{b c}){}_{\beta}{}^{\gamma}\lambda{}_{\gamma}{}^{j} +\frac{i}{8}W^{-2}\lambda{}^{\beta i}\mathcal R(M){}_{a \eta}{}^{r b c}(\Sigma{}_{b c}){}_{\beta}{}^{\gamma}\big(\nabla^{a}\lambda{}_{\gamma}{}^{j}\big)\\
&+\frac{3i}{8}W^{-2}\lambda{}^{\beta i}\big(\nabla^{a}\mathcal R(\mathbb D){}_{a \eta}{}^{r}\big)\lambda{}_{\beta}{}^{j} +\frac{3i}{8}W^{-2}\lambda{}^{\beta i}\mathcal R(\mathbb D){}_{a \eta}{}^{r}\big(\nabla^{a}\lambda{}_{\beta}{}^{j}\big)\\
&-\frac{i}{8}W^{-2}\lambda{}^{\beta i}\big(\nabla^{a}\mathcal R(J){}_{a \eta}{}^{r j k}\big)\lambda{}_{\beta k} -\frac{i}{8}W^{-2}\lambda{}^{\beta i}\mathcal R(J){}_{a \eta}{}^{r j k}\big(\nabla^{a}\lambda{}_{\beta k}\big)\\
&-\frac{i}{8}W^{-2}\lambda{}^{\beta i}\big(\nabla^{a}\mathcal R(J){}_{a \eta}{}^{r k j}\big)\lambda{}_{\beta k} -\frac{i}{8}W^{-2}\lambda{}^{\beta i}\mathcal R(J){}_{a \eta}{}^{r k j}\big(\nabla^{a}\lambda{}_{\beta k}\big)\\
&+\frac{1}{2}W^{-1}\lambda{}_{\beta}{}^{i}\big(\nabla^{a}\mathcal R(S){}_{a \eta}{}^{r \beta j}\big) +\frac{1}{2}W^{-2}\lambda{}_{\beta}{}^{i}\mathcal R(S){}_{a \eta}{}^{r \beta j}\big(\nabla^{a}W\big)\\
&-\frac{i}{2}W^{-2}\lambda{}^{\beta i}\mathcal T{}^{a}{}_{\eta}{}^{\gamma}\varepsilon{}^{r j}\big(\nabla_{a}F{}_{\gamma \beta}\big) -\frac{i}{2}W^{-1}\lambda{}^{\beta i}\mathcal T{}^{a}{}_{\eta}{}^{\gamma}\varepsilon{}^{r j}\big(\nabla_{a}W{}_{\gamma \beta}\big)\\
&-\frac{i}{2}W^{-2}\lambda{}^{\beta i}\mathcal T{}^{a}{}_{\eta}{}^{\gamma}\varepsilon{}^{r j}W{}_{\gamma \beta}\big(\nabla_{a}W\big) -\frac{i}{4}W^{-2}\lambda{}_{\beta}{}^{i}\mathcal T{}^{a}{}_{\eta}{}^{\beta}\big(\nabla_{a}X{}^{r j}\big)\\
&-\frac{i}{4}W^{-2}\lambda{}^{\beta i}\mathcal T{}^{a}{}_{\eta}{}^{\gamma}\varepsilon{}^{r j}(\Gamma{}^{b}){}_{\gamma \beta}\big(\nabla_{a}\nabla_{b}W\big) -\frac{i}{2}W^{-2}\lambda{}^{\beta i}\mathcal T{}^{a}{}_{\eta}{}^{\gamma}\mathcal T{}_{a \gamma}{}^{\delta}\varepsilon{}^{r j}F{}_{\delta \beta}\\
&-\frac{i}{2}W^{-1}\lambda{}^{\beta i}\mathcal T{}^{a}{}_{\eta}{}^{\gamma}\mathcal T{}_{a \gamma}{}^{\delta}\varepsilon{}^{r j}W{}_{\delta \beta} -\frac{i}{4}W^{-2}\lambda{}_{\beta}{}^{i}\mathcal T{}^{a}{}_{\eta}{}^{\gamma}\mathcal T{}_{a \gamma}{}^{\beta}X{}^{r j}\\
&-\frac{i}{4}W^{-2}\lambda{}^{\beta i}\mathcal T{}^{a}{}_{\eta}{}^{\gamma}\mathcal T{}_{a \gamma}{}^{\delta}\varepsilon{}^{r j}(\Gamma{}^{b}){}_{\delta \beta}\big(\nabla_{b}W\big) +\frac{i}{8}W^{-2}\lambda{}^{\beta i}\mathcal T{}^{a}{}_{\eta}{}^{\gamma}\mathcal R(M){}_{a \gamma}{}^{r b c}(\Sigma{}_{b c}){}_{\beta}{}^{\delta}\lambda{}_{\delta}{}^{j}\\
&+\frac{3i}{8}W^{-2}\lambda{}^{\beta i}\mathcal T{}^{a}{}_{\eta}{}^{\gamma}\mathcal R(\mathbb D){}_{a \gamma}{}^{r}\lambda{}_{\beta}{}^{j} -\frac{i}{8}W^{-2}\lambda{}^{\beta i}\mathcal T{}^{a}{}_{\eta}{}^{\gamma}\mathcal R(J){}_{a \gamma}{}^{r j k}\lambda{}_{\beta k}\\
&-\frac{i}{8}W^{-2}\lambda{}^{\beta i}\mathcal T{}^{a}{}_{\eta}{}^{\gamma}\mathcal R(J){}_{a \gamma}{}^{r k j}\lambda{}_{\beta k} +\frac{1}{2}W^{-1}\lambda{}_{\beta}{}^{i}\mathcal T{}^{a}{}_{\eta}{}^{\gamma}\mathcal R(S){}_{a \gamma}{}^{r \beta j}\\
&+\frac{i}{8}W^{-2}\lambda{}^{\beta i}\mathcal R(M){}^{a}{}_{\eta}{}^{r}{}_{a}{}^{b}\big(\nabla_{b}\lambda{}_{\beta}{}^{j}\big) -\frac{i}{8}W^{-2}\lambda{}^{\beta i}\mathcal R(M){}^{a}{}_{\eta}{}^{r b}{}_{a}\big(\nabla_{b}\lambda{}_{\beta}{}^{j}\big)\\
&+\frac{i}{8}W^{-2}\lambda{}^{\beta i}\mathcal R(M){}^{a}{}_{\eta}{}^{r b c}(\Sigma{}_{b c}){}_{\beta}{}^{\gamma}\big(\nabla_{a}\lambda{}_{\gamma}{}^{j}\big) +\frac{5i}{8}W^{-2}\lambda{}^{\beta i}\mathcal R(\mathbb D){}^{a}{}_{\eta}{}^{r}\big(\nabla_{a}\lambda{}_{\beta}{}^{j}\big)\\
&-\frac{i}{8}W^{-2}\lambda{}^{\beta i}\mathcal R(J){}^{a}{}_{\eta}{}^{r j k}\big(\nabla_{a}\lambda{}_{\beta k}\big) -\frac{i}{8}W^{-2}\lambda{}^{\beta i}\mathcal R(J){}^{a}{}_{\eta}{}^{r k j}\big(\nabla_{a}\lambda{}_{\beta k}\big)\\
&+\frac{1}{2}W^{-2}\lambda{}_{\beta}{}^{i}\mathcal R(S){}^{a}{}_{\eta}{}^{r \beta j}\big(\nabla_{a}W\big) +\frac{1}{2}W^{-2}\lambda{}^{\beta i}\mathcal R(S){}^{a}{}_{\eta}{}^{r \gamma j}(\Gamma{}_{a}){}_{\gamma}{}^{\delta}F{}_{\delta \beta}\\
&+\frac{1}{2}W^{-1}\lambda{}^{\beta i}\mathcal R(S){}^{a}{}_{\eta}{}^{r \gamma j}(\Gamma{}_{a}){}_{\gamma}{}^{\delta}W{}_{\delta \beta} +\frac{1}{4}W^{-2}\lambda{}_{\beta}{}^{i}\mathcal R(S){}^{a}{}_{\eta}{}^{r \gamma k}(\Gamma{}_{a}){}_{\gamma}{}^{\beta}X{}_{k}{}^{j}\\
&+\frac{1}{4}W^{-2}\lambda{}^{\beta i}\mathcal R(S){}^{a}{}_{\eta}{}^{r \gamma j}(\Gamma{}_{a}){}_{\gamma}{}^{\delta}(\Gamma{}^{b}){}_{\delta \beta}\big(\nabla_{b}W\big) -\frac{1}{8}W^{-1}\lambda{}_{\beta}{}^{i}\mathcal R(S){}^{a}{}_{\eta}{}^{r \gamma j}W{}_{a}{}^{b}(\Gamma{}_{b}){}_{\gamma}{}^{\beta}\\
&+\frac{3i}{4}W^{-2}\lambda{}^{\beta i}\mathcal R(K){}_{a \eta}{}^{r a}\lambda{}_{\beta}{}^{j} +\frac{i}{2}W^{-2}\lambda{}^{\beta i}\mathcal R(K){}^{a}{}_{\eta}{}^{r b}(\Sigma{}_{b a}){}_{\beta}{}^{\gamma}\lambda{}_{\gamma}{}^{j}
\end{aligned}
\tag{S3-H2.4-b}
```

**Check for H2.4:** all 118 written summands have weight $`7/2`$, odd parity and the same free indices $`\eta;r,i,j`$. Dummy labels are paired. The coefficient $`1/3`$ and the two external epsilons are applied once, when collecting the spinor.

#### Input H2.5

The calculated input is

```math
\left.H^{ij}\right|_{\mathrm{H2.5}}=W^{-2}\big(-\frac i4(\nabla^a\lambda^{\alpha i})\nabla_a\lambda_\alpha^j\big).
\tag{S3-H2.5-input}
```

Expand each written SU(2) average with weight $`1/2`$ before applying the left derivative.

Apply the product rule (S3-09), in the displayed factor order:

```math
\begin{aligned}
\left.\nabla_\eta^rH^{ij}\right|_{\mathrm{H2.5}}=&-\frac{i}{4}\nabla_{\eta}^{r}\big(W^{-2}\big)\big(\nabla^{a}\lambda{}^{\beta i}\big)\big(\nabla_{a}\lambda{}_{\beta}{}^{j}\big) -\frac{i}{4}W^{-2}\nabla_{\eta}^{r}\big(\nabla^{a}\lambda{}^{\beta i}\big)\big(\nabla_{a}\lambda{}_{\beta}{}^{j}\big)\\
&+\frac{i}{4}W^{-2}\big(\nabla^{a}\lambda{}^{\beta i}\big)\nabla_{\eta}^{r}\big(\nabla_{a}\lambda{}_{\beta}{}^{j}\big)
\end{aligned}
\tag{S3-H2.5-a}
```

Insert the elementary source identities and the applicable commutators (S3-11)–(S3-14), distribute the vector product rules, and contract only index-raising metrics. The resulting contribution is

```math
\begin{aligned}
\left.\nabla_\eta^rH^{ij}\right|_{\mathrm{H2.5}}=&-\frac{1}{2}W^{-3}\lambda{}_{\eta}{}^{r}\big(\nabla^{a}\lambda{}^{\beta i}\big)\big(\nabla_{a}\lambda{}_{\beta}{}^{j}\big) +\frac{i}{2}W^{-2}\varepsilon{}^{r i}\big(\nabla^{a}F{}_{\eta}{}^{\beta}\big)\big(\nabla_{a}\lambda{}_{\beta}{}^{j}\big)\\
&+\frac{i}{2}W^{-1}\varepsilon{}^{r i}\big(\nabla^{a}W{}_{\eta}{}^{\beta}\big)\big(\nabla_{a}\lambda{}_{\beta}{}^{j}\big) +\frac{i}{2}W^{-2}\varepsilon{}^{r i}W{}_{\eta}{}^{\beta}\big(\nabla^{a}W\big)\big(\nabla_{a}\lambda{}_{\beta}{}^{j}\big)\\
&-\frac{i}{4}W^{-2}\big(\nabla^{a}X{}^{r i}\big)\big(\nabla_{a}\lambda{}_{\eta}{}^{j}\big) +\frac{i}{4}W^{-2}\varepsilon{}^{r i}(\Gamma{}^{a}){}_{\eta}{}^{\beta}\big(\nabla^{b}\nabla_{a}W\big)\big(\nabla_{b}\lambda{}_{\beta}{}^{j}\big)\\
&+\frac{i}{2}W^{-2}\mathcal T{}^{a}{}_{\eta}{}^{\beta}\varepsilon{}^{r i}F{}_{\beta}{}^{\gamma}\big(\nabla_{a}\lambda{}_{\gamma}{}^{j}\big) +\frac{i}{2}W^{-1}\mathcal T{}^{a}{}_{\eta}{}^{\beta}\varepsilon{}^{r i}W{}_{\beta}{}^{\gamma}\big(\nabla_{a}\lambda{}_{\gamma}{}^{j}\big)\\
&-\frac{i}{4}W^{-2}\mathcal T{}^{a}{}_{\eta}{}^{\beta}X{}^{r i}\big(\nabla_{a}\lambda{}_{\beta}{}^{j}\big) +\frac{i}{4}W^{-2}\mathcal T{}^{a}{}_{\eta}{}^{\beta}\varepsilon{}^{r i}(\Gamma{}^{b}){}_{\beta}{}^{\gamma}\big(\nabla_{b}W\big)\big(\nabla_{a}\lambda{}_{\gamma}{}^{j}\big)\\
&-\frac{i}{8}W^{-2}\mathcal R(M){}^{a}{}_{\eta}{}^{r b c}(\Sigma{}_{b c}){}^{\beta \gamma}\lambda{}_{\gamma}{}^{i}\big(\nabla_{a}\lambda{}_{\beta}{}^{j}\big) -\frac{3i}{8}W^{-2}\mathcal R(\mathbb D){}^{a}{}_{\eta}{}^{r}\lambda{}^{\beta i}\big(\nabla_{a}\lambda{}_{\beta}{}^{j}\big)\\
&+\frac{i}{8}W^{-2}\mathcal R(J){}^{a}{}_{\eta}{}^{r i k}\lambda{}^{\beta}{}_{k}\big(\nabla_{a}\lambda{}_{\beta}{}^{j}\big) +\frac{i}{8}W^{-2}\mathcal R(J){}^{a}{}_{\eta}{}^{r k i}\lambda{}^{\beta}{}_{k}\big(\nabla_{a}\lambda{}_{\beta}{}^{j}\big)\\
&+\frac{1}{2}W^{-1}\mathcal R(S){}^{a}{}_{\eta}{}^{r \beta i}\big(\nabla_{a}\lambda{}_{\beta}{}^{j}\big) -\frac{i}{2}W^{-2}\big(\nabla^{a}\lambda{}^{\beta i}\big)\varepsilon{}^{r j}\big(\nabla_{a}F{}_{\eta \beta}\big)\\
&-\frac{i}{2}W^{-1}\big(\nabla^{a}\lambda{}^{\beta i}\big)\varepsilon{}^{r j}\big(\nabla_{a}W{}_{\eta \beta}\big) -\frac{i}{2}W^{-2}\big(\nabla^{a}\lambda{}^{\beta i}\big)\varepsilon{}^{r j}W{}_{\eta \beta}\big(\nabla_{a}W\big)\\
&-\frac{i}{4}W^{-2}\big(\nabla^{a}\lambda{}_{\eta}{}^{i}\big)\big(\nabla_{a}X{}^{r j}\big) -\frac{i}{4}W^{-2}\big(\nabla^{a}\lambda{}^{\beta i}\big)\varepsilon{}^{r j}(\Gamma{}^{b}){}_{\eta \beta}\big(\nabla_{a}\nabla_{b}W\big)\\
&-\frac{i}{2}W^{-2}\big(\nabla^{a}\lambda{}^{\beta i}\big)\mathcal T{}_{a \eta}{}^{\gamma}\varepsilon{}^{r j}F{}_{\gamma \beta} -\frac{i}{2}W^{-1}\big(\nabla^{a}\lambda{}^{\beta i}\big)\mathcal T{}_{a \eta}{}^{\gamma}\varepsilon{}^{r j}W{}_{\gamma \beta}\\
&-\frac{i}{4}W^{-2}\big(\nabla^{a}\lambda{}_{\beta}{}^{i}\big)\mathcal T{}_{a \eta}{}^{\beta}X{}^{r j} -\frac{i}{4}W^{-2}\big(\nabla^{a}\lambda{}^{\beta i}\big)\mathcal T{}_{a \eta}{}^{\gamma}\varepsilon{}^{r j}(\Gamma{}^{b}){}_{\gamma \beta}\big(\nabla_{b}W\big)\\
&+\frac{i}{8}W^{-2}\big(\nabla^{a}\lambda{}^{\beta i}\big)\mathcal R(M){}_{a \eta}{}^{r b c}(\Sigma{}_{b c}){}_{\beta}{}^{\gamma}\lambda{}_{\gamma}{}^{j} +\frac{3i}{8}W^{-2}\big(\nabla^{a}\lambda{}^{\beta i}\big)\mathcal R(\mathbb D){}_{a \eta}{}^{r}\lambda{}_{\beta}{}^{j}\\
&-\frac{i}{8}W^{-2}\big(\nabla^{a}\lambda{}^{\beta i}\big)\mathcal R(J){}_{a \eta}{}^{r j k}\lambda{}_{\beta k} -\frac{i}{8}W^{-2}\big(\nabla^{a}\lambda{}^{\beta i}\big)\mathcal R(J){}_{a \eta}{}^{r k j}\lambda{}_{\beta k}\\
&+\frac{1}{2}W^{-1}\big(\nabla^{a}\lambda{}_{\beta}{}^{i}\big)\mathcal R(S){}_{a \eta}{}^{r \beta j}
\end{aligned}
\tag{S3-H2.5-b}
```

**Check for H2.5:** all 29 written summands have weight $`7/2`$, odd parity and the same free indices $`\eta;r,i,j`$. Dummy labels are paired. The coefficient $`1/3`$ and the two external epsilons are applied once, when collecting the spinor.

#### Input H2.6

The calculated input is

```math
\left.H^{ij}\right|_{\mathrm{H2.6}}=W^{-2}\big(-\frac{3i}{16}\varepsilon^{abcde}(\Sigma_{ab})^{\alpha\beta}W_{de}\lambda_\alpha^{(i}\nabla_c\lambda_\beta^{j)}\big).
\tag{S3-H2.6-input}
```

Expand each written SU(2) average with weight $`1/2`$ before applying the left derivative.

Apply the product rule (S3-09), in the displayed factor order:

```math
\begin{aligned}
\left.\nabla_\eta^rH^{ij}\right|_{\mathrm{H2.6}}=&-\frac{3i}{32}\nabla_{\eta}^{r}\big(W^{-2}\big)\varepsilon{}^{a b c d e}(\Sigma{}_{a b}){}^{\beta \gamma}W{}_{d e}\lambda{}_{\beta}{}^{i}\big(\nabla_{c}\lambda{}_{\gamma}{}^{j}\big) -\frac{3i}{32}W^{-2}\varepsilon{}^{a b c d e}(\Sigma{}_{a b}){}^{\beta \gamma}\nabla_{\eta}^{r}\big(W{}_{d e}\big)\lambda{}_{\beta}{}^{i}\big(\nabla_{c}\lambda{}_{\gamma}{}^{j}\big)\\
&-\frac{3i}{32}W^{-2}\varepsilon{}^{a b c d e}(\Sigma{}_{a b}){}^{\beta \gamma}W{}_{d e}\nabla_{\eta}^{r}\big(\lambda{}_{\beta}{}^{i}\big)\big(\nabla_{c}\lambda{}_{\gamma}{}^{j}\big) +\frac{3i}{32}W^{-2}\varepsilon{}^{a b c d e}(\Sigma{}_{a b}){}^{\beta \gamma}W{}_{d e}\lambda{}_{\beta}{}^{i}\nabla_{\eta}^{r}\big(\nabla_{c}\lambda{}_{\gamma}{}^{j}\big)\\
&-\frac{3i}{32}\nabla_{\eta}^{r}\big(W^{-2}\big)\varepsilon{}^{a b c d e}(\Sigma{}_{a b}){}^{\beta \gamma}W{}_{d e}\lambda{}_{\beta}{}^{j}\big(\nabla_{c}\lambda{}_{\gamma}{}^{i}\big) -\frac{3i}{32}W^{-2}\varepsilon{}^{a b c d e}(\Sigma{}_{a b}){}^{\beta \gamma}\nabla_{\eta}^{r}\big(W{}_{d e}\big)\lambda{}_{\beta}{}^{j}\big(\nabla_{c}\lambda{}_{\gamma}{}^{i}\big)\\
&-\frac{3i}{32}W^{-2}\varepsilon{}^{a b c d e}(\Sigma{}_{a b}){}^{\beta \gamma}W{}_{d e}\nabla_{\eta}^{r}\big(\lambda{}_{\beta}{}^{j}\big)\big(\nabla_{c}\lambda{}_{\gamma}{}^{i}\big) +\frac{3i}{32}W^{-2}\varepsilon{}^{a b c d e}(\Sigma{}_{a b}){}^{\beta \gamma}W{}_{d e}\lambda{}_{\beta}{}^{j}\nabla_{\eta}^{r}\big(\nabla_{c}\lambda{}_{\gamma}{}^{i}\big)
\end{aligned}
\tag{S3-H2.6-a}
```

Insert the elementary source identities and the applicable commutators (S3-11)–(S3-14), distribute the vector product rules, and contract only index-raising metrics. The resulting contribution is

```math
\begin{aligned}
\left.\nabla_\eta^rH^{ij}\right|_{\mathrm{H2.6}}=&-\frac{3}{16}W^{-3}\lambda{}_{\eta}{}^{r}\varepsilon{}^{a b c d e}(\Sigma{}_{a b}){}^{\beta \gamma}W{}_{d e}\lambda{}_{\beta}{}^{i}\big(\nabla_{c}\lambda{}_{\gamma}{}^{j}\big) -\frac{3i}{32}W^{-2}\varepsilon{}^{a b c d e}(\Sigma{}_{a b}){}^{\beta \gamma}(\Sigma{}_{d e}){}^{\delta \rho}W{}_{\eta \delta \rho}{}^{r}\lambda{}_{\beta}{}^{i}\big(\nabla_{c}\lambda{}_{\gamma}{}^{j}\big)\\
&-\frac{3i}{64}W^{-2}\varepsilon{}^{a b c d e}(\Sigma{}_{a b}){}^{\beta \gamma}(\Sigma{}_{d e}){}_{\eta}{}^{\delta}X{}_{\delta}{}^{r}\lambda{}_{\beta}{}^{i}\big(\nabla_{c}\lambda{}_{\gamma}{}^{j}\big) -\frac{3i}{64}W^{-2}\varepsilon{}^{a b c d e}(\Sigma{}_{a b}){}^{\beta \gamma}(\Sigma{}_{d e}){}^{\delta}{}_{\eta}X{}_{\delta}{}^{r}\lambda{}_{\beta}{}^{i}\big(\nabla_{c}\lambda{}_{\gamma}{}^{j}\big)\\
&+\frac{3i}{16}W^{-2}\varepsilon{}^{a b c d e}(\Sigma{}_{a b}){}^{\beta \gamma}W{}_{d e}\varepsilon{}^{r i}F{}_{\eta \beta}\big(\nabla_{c}\lambda{}_{\gamma}{}^{j}\big) +\frac{3i}{16}W^{-1}\varepsilon{}^{a b c d e}(\Sigma{}_{a b}){}^{\beta \gamma}W{}_{d e}\varepsilon{}^{r i}W{}_{\eta \beta}\big(\nabla_{c}\lambda{}_{\gamma}{}^{j}\big)\\
&+\frac{3i}{32}W^{-2}\varepsilon{}^{a b c d e}(\Sigma{}_{a b}){}_{\eta}{}^{\beta}W{}_{d e}X{}^{r i}\big(\nabla_{c}\lambda{}_{\beta}{}^{j}\big) +\frac{3i}{32}W^{-2}\varepsilon{}^{a b c d e}(\Sigma{}_{a b}){}^{\beta \gamma}W{}_{d e}\varepsilon{}^{r i}(\Gamma{}^{f}){}_{\eta \beta}\big(\nabla_{f}W\big)\big(\nabla_{c}\lambda{}_{\gamma}{}^{j}\big)\\
&-\frac{3i}{16}W^{-2}\varepsilon{}^{a b c d e}(\Sigma{}_{a b}){}^{\beta \gamma}W{}_{d e}\lambda{}_{\beta}{}^{i}\varepsilon{}^{r j}\big(\nabla_{c}F{}_{\eta \gamma}\big) -\frac{3i}{16}W^{-1}\varepsilon{}^{a b c d e}(\Sigma{}_{a b}){}^{\beta \gamma}W{}_{d e}\lambda{}_{\beta}{}^{i}\varepsilon{}^{r j}\big(\nabla_{c}W{}_{\eta \gamma}\big)\\
&-\frac{3i}{16}W^{-2}\varepsilon{}^{a b c d e}(\Sigma{}_{a b}){}^{\beta \gamma}W{}_{d e}\lambda{}_{\beta}{}^{i}\varepsilon{}^{r j}W{}_{\eta \gamma}\big(\nabla_{c}W\big) -\frac{3i}{32}W^{-2}\varepsilon{}^{a b c d e}(\Sigma{}_{a b}){}^{\beta}{}_{\eta}W{}_{d e}\lambda{}_{\beta}{}^{i}\big(\nabla_{c}X{}^{r j}\big)\\
&-\frac{3i}{32}W^{-2}\varepsilon{}^{a b c d e}(\Sigma{}_{a b}){}^{\beta \gamma}W{}_{d e}\lambda{}_{\beta}{}^{i}\varepsilon{}^{r j}(\Gamma{}^{f}){}_{\eta \gamma}\big(\nabla_{c}\nabla_{f}W\big) -\frac{3i}{16}W^{-2}\varepsilon{}^{a b c d e}(\Sigma{}_{a b}){}^{\beta \gamma}W{}_{d e}\lambda{}_{\beta}{}^{i}\mathcal T{}_{c \eta}{}^{\delta}\varepsilon{}^{r j}F{}_{\delta \gamma}\\
&-\frac{3i}{16}W^{-1}\varepsilon{}^{a b c d e}(\Sigma{}_{a b}){}^{\beta \gamma}W{}_{d e}\lambda{}_{\beta}{}^{i}\mathcal T{}_{c \eta}{}^{\delta}\varepsilon{}^{r j}W{}_{\delta \gamma} -\frac{3i}{32}W^{-2}\varepsilon{}^{a b c d e}(\Sigma{}_{a b}){}^{\beta}{}_{\gamma}W{}_{d e}\lambda{}_{\beta}{}^{i}\mathcal T{}_{c \eta}{}^{\gamma}X{}^{r j}\\
&-\frac{3i}{32}W^{-2}\varepsilon{}^{a b c d e}(\Sigma{}_{a b}){}^{\beta \gamma}W{}_{d e}\lambda{}_{\beta}{}^{i}\mathcal T{}_{c \eta}{}^{\delta}\varepsilon{}^{r j}(\Gamma{}^{f}){}_{\delta \gamma}\big(\nabla_{f}W\big) +\frac{3i}{64}W^{-2}\varepsilon{}^{a b c d e}(\Sigma{}_{a b}){}^{\beta \gamma}W{}_{d e}\lambda{}_{\beta}{}^{i}\mathcal R(M){}_{c \eta}{}^{r f g}(\Sigma{}_{f g}){}_{\gamma}{}^{\delta}\lambda{}_{\delta}{}^{j}\\
&+\frac{9i}{64}W^{-2}\varepsilon{}^{a b c d e}(\Sigma{}_{a b}){}^{\beta \gamma}W{}_{d e}\lambda{}_{\beta}{}^{i}\mathcal R(\mathbb D){}_{c \eta}{}^{r}\lambda{}_{\gamma}{}^{j} -\frac{3i}{64}W^{-2}\varepsilon{}^{a b c d e}(\Sigma{}_{a b}){}^{\beta \gamma}W{}_{d e}\lambda{}_{\beta}{}^{i}\mathcal R(J){}_{c \eta}{}^{r j k}\lambda{}_{\gamma k}\\
&-\frac{3i}{64}W^{-2}\varepsilon{}^{a b c d e}(\Sigma{}_{a b}){}^{\beta \gamma}W{}_{d e}\lambda{}_{\beta}{}^{i}\mathcal R(J){}_{c \eta}{}^{r k j}\lambda{}_{\gamma k} +\frac{3}{16}W^{-1}\varepsilon{}^{a b c d e}(\Sigma{}_{a b}){}^{\beta}{}_{\gamma}W{}_{d e}\lambda{}_{\beta}{}^{i}\mathcal R(S){}_{c \eta}{}^{r \gamma j}\\
&-\frac{3}{16}W^{-3}\lambda{}_{\eta}{}^{r}\varepsilon{}^{a b c d e}(\Sigma{}_{a b}){}^{\beta \gamma}W{}_{d e}\lambda{}_{\beta}{}^{j}\big(\nabla_{c}\lambda{}_{\gamma}{}^{i}\big) -\frac{3i}{32}W^{-2}\varepsilon{}^{a b c d e}(\Sigma{}_{a b}){}^{\beta \gamma}(\Sigma{}_{d e}){}^{\delta \rho}W{}_{\eta \delta \rho}{}^{r}\lambda{}_{\beta}{}^{j}\big(\nabla_{c}\lambda{}_{\gamma}{}^{i}\big)\\
&-\frac{3i}{64}W^{-2}\varepsilon{}^{a b c d e}(\Sigma{}_{a b}){}^{\beta \gamma}(\Sigma{}_{d e}){}_{\eta}{}^{\delta}X{}_{\delta}{}^{r}\lambda{}_{\beta}{}^{j}\big(\nabla_{c}\lambda{}_{\gamma}{}^{i}\big) -\frac{3i}{64}W^{-2}\varepsilon{}^{a b c d e}(\Sigma{}_{a b}){}^{\beta \gamma}(\Sigma{}_{d e}){}^{\delta}{}_{\eta}X{}_{\delta}{}^{r}\lambda{}_{\beta}{}^{j}\big(\nabla_{c}\lambda{}_{\gamma}{}^{i}\big)\\
&+\frac{3i}{16}W^{-2}\varepsilon{}^{a b c d e}(\Sigma{}_{a b}){}^{\beta \gamma}W{}_{d e}\varepsilon{}^{r j}F{}_{\eta \beta}\big(\nabla_{c}\lambda{}_{\gamma}{}^{i}\big) +\frac{3i}{16}W^{-1}\varepsilon{}^{a b c d e}(\Sigma{}_{a b}){}^{\beta \gamma}W{}_{d e}\varepsilon{}^{r j}W{}_{\eta \beta}\big(\nabla_{c}\lambda{}_{\gamma}{}^{i}\big)\\
&+\frac{3i}{32}W^{-2}\varepsilon{}^{a b c d e}(\Sigma{}_{a b}){}_{\eta}{}^{\beta}W{}_{d e}X{}^{r j}\big(\nabla_{c}\lambda{}_{\beta}{}^{i}\big) +\frac{3i}{32}W^{-2}\varepsilon{}^{a b c d e}(\Sigma{}_{a b}){}^{\beta \gamma}W{}_{d e}\varepsilon{}^{r j}(\Gamma{}^{f}){}_{\eta \beta}\big(\nabla_{f}W\big)\big(\nabla_{c}\lambda{}_{\gamma}{}^{i}\big)\\
&-\frac{3i}{16}W^{-2}\varepsilon{}^{a b c d e}(\Sigma{}_{a b}){}^{\beta \gamma}W{}_{d e}\lambda{}_{\beta}{}^{j}\varepsilon{}^{r i}\big(\nabla_{c}F{}_{\eta \gamma}\big) -\frac{3i}{16}W^{-1}\varepsilon{}^{a b c d e}(\Sigma{}_{a b}){}^{\beta \gamma}W{}_{d e}\lambda{}_{\beta}{}^{j}\varepsilon{}^{r i}\big(\nabla_{c}W{}_{\eta \gamma}\big)\\
&-\frac{3i}{16}W^{-2}\varepsilon{}^{a b c d e}(\Sigma{}_{a b}){}^{\beta \gamma}W{}_{d e}\lambda{}_{\beta}{}^{j}\varepsilon{}^{r i}W{}_{\eta \gamma}\big(\nabla_{c}W\big) -\frac{3i}{32}W^{-2}\varepsilon{}^{a b c d e}(\Sigma{}_{a b}){}^{\beta}{}_{\eta}W{}_{d e}\lambda{}_{\beta}{}^{j}\big(\nabla_{c}X{}^{r i}\big)\\
&-\frac{3i}{32}W^{-2}\varepsilon{}^{a b c d e}(\Sigma{}_{a b}){}^{\beta \gamma}W{}_{d e}\lambda{}_{\beta}{}^{j}\varepsilon{}^{r i}(\Gamma{}^{f}){}_{\eta \gamma}\big(\nabla_{c}\nabla_{f}W\big) -\frac{3i}{16}W^{-2}\varepsilon{}^{a b c d e}(\Sigma{}_{a b}){}^{\beta \gamma}W{}_{d e}\lambda{}_{\beta}{}^{j}\mathcal T{}_{c \eta}{}^{\delta}\varepsilon{}^{r i}F{}_{\delta \gamma}\\
&-\frac{3i}{16}W^{-1}\varepsilon{}^{a b c d e}(\Sigma{}_{a b}){}^{\beta \gamma}W{}_{d e}\lambda{}_{\beta}{}^{j}\mathcal T{}_{c \eta}{}^{\delta}\varepsilon{}^{r i}W{}_{\delta \gamma} -\frac{3i}{32}W^{-2}\varepsilon{}^{a b c d e}(\Sigma{}_{a b}){}^{\beta}{}_{\gamma}W{}_{d e}\lambda{}_{\beta}{}^{j}\mathcal T{}_{c \eta}{}^{\gamma}X{}^{r i}\\
&-\frac{3i}{32}W^{-2}\varepsilon{}^{a b c d e}(\Sigma{}_{a b}){}^{\beta \gamma}W{}_{d e}\lambda{}_{\beta}{}^{j}\mathcal T{}_{c \eta}{}^{\delta}\varepsilon{}^{r i}(\Gamma{}^{f}){}_{\delta \gamma}\big(\nabla_{f}W\big) +\frac{3i}{64}W^{-2}\varepsilon{}^{a b c d e}(\Sigma{}_{a b}){}^{\beta \gamma}W{}_{d e}\lambda{}_{\beta}{}^{j}\mathcal R(M){}_{c \eta}{}^{r f g}(\Sigma{}_{f g}){}_{\gamma}{}^{\delta}\lambda{}_{\delta}{}^{i}\\
&+\frac{9i}{64}W^{-2}\varepsilon{}^{a b c d e}(\Sigma{}_{a b}){}^{\beta \gamma}W{}_{d e}\lambda{}_{\beta}{}^{j}\mathcal R(\mathbb D){}_{c \eta}{}^{r}\lambda{}_{\gamma}{}^{i} -\frac{3i}{64}W^{-2}\varepsilon{}^{a b c d e}(\Sigma{}_{a b}){}^{\beta \gamma}W{}_{d e}\lambda{}_{\beta}{}^{j}\mathcal R(J){}_{c \eta}{}^{r i k}\lambda{}_{\gamma k}\\
&-\frac{3i}{64}W^{-2}\varepsilon{}^{a b c d e}(\Sigma{}_{a b}){}^{\beta \gamma}W{}_{d e}\lambda{}_{\beta}{}^{j}\mathcal R(J){}_{c \eta}{}^{r k i}\lambda{}_{\gamma k} +\frac{3}{16}W^{-1}\varepsilon{}^{a b c d e}(\Sigma{}_{a b}){}^{\beta}{}_{\gamma}W{}_{d e}\lambda{}_{\beta}{}^{j}\mathcal R(S){}_{c \eta}{}^{r \gamma i}
\end{aligned}
\tag{S3-H2.6-b}
```

**Check for H2.6:** all 44 written summands have weight $`7/2`$, odd parity and the same free indices $`\eta;r,i,j`$. Dummy labels are paired. The coefficient $`1/3`$ and the two external epsilons are applied once, when collecting the spinor.

#### Input H2.7

The calculated input is

```math
\left.H^{ij}\right|_{\mathrm{H2.7}}=W^{-2}\big(-\frac{3i}{8}(\Gamma^a)^{\alpha\beta}\lambda_\alpha^i\lambda_\beta^j\nabla^cW_{ac}\big).
\tag{S3-H2.7-input}
```

Expand each written SU(2) average with weight $`1/2`$ before applying the left derivative.

Apply the product rule (S3-09), in the displayed factor order:

```math
\begin{aligned}
\left.\nabla_\eta^rH^{ij}\right|_{\mathrm{H2.7}}=&-\frac{3i}{8}\nabla_{\eta}^{r}\big(W^{-2}\big)(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{i}\lambda{}_{\gamma}{}^{j}\big(\nabla^{b}W{}_{a b}\big) -\frac{3i}{8}W^{-2}(\Gamma{}^{a}){}^{\beta \gamma}\nabla_{\eta}^{r}\big(\lambda{}_{\beta}{}^{i}\big)\lambda{}_{\gamma}{}^{j}\big(\nabla^{b}W{}_{a b}\big)\\
&+\frac{3i}{8}W^{-2}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{i}\nabla_{\eta}^{r}\big(\lambda{}_{\gamma}{}^{j}\big)\big(\nabla^{b}W{}_{a b}\big) -\frac{3i}{8}W^{-2}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{i}\lambda{}_{\gamma}{}^{j}\nabla_{\eta}^{r}\big(\nabla^{b}W{}_{a b}\big)
\end{aligned}
\tag{S3-H2.7-a}
```

Insert the elementary source identities and the applicable commutators (S3-11)–(S3-14), distribute the vector product rules, and contract only index-raising metrics. The resulting contribution is

```math
\begin{aligned}
\left.\nabla_\eta^rH^{ij}\right|_{\mathrm{H2.7}}=&-\frac{3}{4}W^{-3}\lambda{}_{\eta}{}^{r}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{i}\lambda{}_{\gamma}{}^{j}\big(\nabla^{b}W{}_{a b}\big) +\frac{3i}{4}W^{-2}(\Gamma{}^{a}){}^{\beta \gamma}\varepsilon{}^{r i}F{}_{\eta \beta}\lambda{}_{\gamma}{}^{j}\big(\nabla^{b}W{}_{a b}\big)\\
&+\frac{3i}{4}W^{-1}(\Gamma{}^{a}){}^{\beta \gamma}\varepsilon{}^{r i}W{}_{\eta \beta}\lambda{}_{\gamma}{}^{j}\big(\nabla^{b}W{}_{a b}\big) +\frac{3i}{8}W^{-2}(\Gamma{}^{a}){}_{\eta}{}^{\beta}X{}^{r i}\lambda{}_{\beta}{}^{j}\big(\nabla^{b}W{}_{a b}\big)\\
&+\frac{3i}{8}W^{-2}(\Gamma{}^{a}){}^{\beta \gamma}\varepsilon{}^{r i}(\Gamma{}^{b}){}_{\eta \beta}\big(\nabla_{b}W\big)\lambda{}_{\gamma}{}^{j}\big(\nabla^{c}W{}_{a c}\big) -\frac{3i}{4}W^{-2}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{i}\varepsilon{}^{r j}F{}_{\eta \gamma}\big(\nabla^{b}W{}_{a b}\big)\\
&-\frac{3i}{4}W^{-1}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{i}\varepsilon{}^{r j}W{}_{\eta \gamma}\big(\nabla^{b}W{}_{a b}\big) -\frac{3i}{8}W^{-2}(\Gamma{}^{a}){}^{\beta}{}_{\eta}\lambda{}_{\beta}{}^{i}X{}^{r j}\big(\nabla^{b}W{}_{a b}\big)\\
&-\frac{3i}{8}W^{-2}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{i}\varepsilon{}^{r j}(\Gamma{}^{b}){}_{\eta \gamma}\big(\nabla_{b}W\big)\big(\nabla^{c}W{}_{a c}\big) -\frac{3i}{8}W^{-2}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{i}\lambda{}_{\gamma}{}^{j}(\Sigma{}_{a b}){}^{\delta \rho}\big(\nabla^{b}W{}_{\eta \delta \rho}{}^{r}\big)\\
&-\frac{3i}{16}W^{-2}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{i}\lambda{}_{\gamma}{}^{j}(\Sigma{}_{a b}){}_{\eta}{}^{\delta}\big(\nabla^{b}X{}_{\delta}{}^{r}\big) -\frac{3i}{16}W^{-2}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{i}\lambda{}_{\gamma}{}^{j}(\Sigma{}_{a b}){}^{\delta}{}_{\eta}\big(\nabla^{b}X{}_{\delta}{}^{r}\big)\\
&-\frac{3i}{8}W^{-2}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{i}\lambda{}_{\gamma}{}^{j}\mathcal T{}^{b}{}_{\eta}{}^{\delta}(\Sigma{}_{a b}){}^{\rho \sigma}W{}_{\delta \rho \sigma}{}^{r} -\frac{3i}{16}W^{-2}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{i}\lambda{}_{\gamma}{}^{j}\mathcal T{}^{b}{}_{\eta}{}^{\delta}(\Sigma{}_{a b}){}_{\delta}{}^{\rho}X{}_{\rho}{}^{r}\\
&-\frac{3i}{16}W^{-2}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{i}\lambda{}_{\gamma}{}^{j}\mathcal T{}^{b}{}_{\eta}{}^{\delta}(\Sigma{}_{a b}){}^{\rho}{}_{\delta}X{}_{\rho}{}^{r} -\frac{3i}{16}W^{-2}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{i}\lambda{}_{\gamma}{}^{j}\mathcal R(M){}^{b}{}_{\eta}{}^{r}{}_{a}{}^{c}W{}_{c b}\\
&+\frac{3i}{16}W^{-2}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{i}\lambda{}_{\gamma}{}^{j}\mathcal R(M){}^{b}{}_{\eta}{}^{r c}{}_{a}W{}_{c b} -\frac{3i}{16}W^{-2}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{i}\lambda{}_{\gamma}{}^{j}\mathcal R(M){}^{b}{}_{\eta}{}^{r}{}_{b}{}^{c}W{}_{a c}\\
&+\frac{3i}{16}W^{-2}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{i}\lambda{}_{\gamma}{}^{j}\mathcal R(M){}^{b}{}_{\eta}{}^{r c}{}_{b}W{}_{a c} -\frac{3i}{8}W^{-2}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{i}\lambda{}_{\gamma}{}^{j}\mathcal R(\mathbb D){}^{b}{}_{\eta}{}^{r}W{}_{a b}
\end{aligned}
\tag{S3-H2.7-b}
```

**Check for H2.7:** all 20 written summands have weight $`7/2`$, odd parity and the same free indices $`\eta;r,i,j`$. Dummy labels are paired. The coefficient $`1/3`$ and the two external epsilons are applied once, when collecting the spinor.

#### Input H2.8

The calculated input is

```math
\left.H^{ij}\right|_{\mathrm{H2.8}}=W^{-2}\big(\frac{3i}{64}Y\lambda^{\alpha i}\lambda_\alpha^j\big).
\tag{S3-H2.8-input}
```

Apply the product rule (S3-09), in the displayed factor order:

```math
\begin{aligned}
\left.\nabla_\eta^rH^{ij}\right|_{\mathrm{H2.8}}=&\frac{3i}{64}\nabla_{\eta}^{r}\big(W^{-2}\big)Y\lambda{}^{\beta i}\lambda{}_{\beta}{}^{j} +\frac{3i}{64}W^{-2}\nabla_{\eta}^{r}\big(Y\big)\lambda{}^{\beta i}\lambda{}_{\beta}{}^{j}\\
&+\frac{3i}{64}W^{-2}Y\nabla_{\eta}^{r}\big(\lambda{}^{\beta i}\big)\lambda{}_{\beta}{}^{j} -\frac{3i}{64}W^{-2}Y\lambda{}^{\beta i}\nabla_{\eta}^{r}\big(\lambda{}_{\beta}{}^{j}\big)
\end{aligned}
\tag{S3-H2.8-a}
```

Insert the elementary source identities and the applicable commutators (S3-11)–(S3-14), distribute the vector product rules, and contract only index-raising metrics. The resulting contribution is

```math
\begin{aligned}
\left.\nabla_\eta^rH^{ij}\right|_{\mathrm{H2.8}}=&\frac{3}{32}W^{-3}\lambda{}_{\eta}{}^{r}Y\lambda{}^{\beta i}\lambda{}_{\beta}{}^{j} +\frac{3i}{8}W^{-2}(\Gamma{}^{a}){}_{\eta}{}^{\beta}\big(\nabla_{a}X{}_{\beta}{}^{r}\big)\lambda{}^{\gamma i}\lambda{}_{\gamma}{}^{j}\\
&+\frac{3i}{8}W^{-2}W{}_{\eta}{}^{\beta}X{}_{\beta}{}^{r}\lambda{}^{\gamma i}\lambda{}_{\gamma}{}^{j} -\frac{3i}{32}W^{-2}Y\varepsilon{}^{r i}F{}_{\eta}{}^{\beta}\lambda{}_{\beta}{}^{j}\\
&-\frac{3i}{32}W^{-1}Y\varepsilon{}^{r i}W{}_{\eta}{}^{\beta}\lambda{}_{\beta}{}^{j} +\frac{3i}{64}W^{-2}YX{}^{r i}\lambda{}_{\eta}{}^{j}\\
&-\frac{3i}{64}W^{-2}Y\varepsilon{}^{r i}(\Gamma{}^{a}){}_{\eta}{}^{\beta}\big(\nabla_{a}W\big)\lambda{}_{\beta}{}^{j} +\frac{3i}{32}W^{-2}Y\lambda{}^{\beta i}\varepsilon{}^{r j}F{}_{\eta \beta}\\
&+\frac{3i}{32}W^{-1}Y\lambda{}^{\beta i}\varepsilon{}^{r j}W{}_{\eta \beta} +\frac{3i}{64}W^{-2}Y\lambda{}_{\eta}{}^{i}X{}^{r j}\\
&+\frac{3i}{64}W^{-2}Y\lambda{}^{\beta i}\varepsilon{}^{r j}(\Gamma{}^{a}){}_{\eta \beta}\big(\nabla_{a}W\big)
\end{aligned}
\tag{S3-H2.8-b}
```

**Check for H2.8:** all 11 written summands have weight $`7/2`$, odd parity and the same free indices $`\eta;r,i,j`$. Dummy labels are paired. The coefficient $`1/3`$ and the two external epsilons are applied once, when collecting the spinor.

#### Input H2.9

The calculated input is

```math
\left.H^{ij}\right|_{\mathrm{H2.9}}=W^{-2}\big(\frac38(\Sigma_{ab})^{\alpha\beta}F^{ab}X_\alpha^{(i}\lambda_\beta^{j)}\big).
\tag{S3-H2.9-input}
```

Expand each written SU(2) average with weight $`1/2`$ before applying the left derivative.

Apply the product rule (S3-09), in the displayed factor order:

```math
\begin{aligned}
\left.\nabla_\eta^rH^{ij}\right|_{\mathrm{H2.9}}=&\frac{3}{16}\nabla_{\eta}^{r}\big(W^{-2}\big)(\Sigma{}_{a b}){}^{\beta \gamma}F{}^{a b}X{}_{\beta}{}^{i}\lambda{}_{\gamma}{}^{j} +\frac{3}{16}W^{-2}(\Sigma{}_{a b}){}^{\beta \gamma}\nabla_{\eta}^{r}\big(F{}^{a b}\big)X{}_{\beta}{}^{i}\lambda{}_{\gamma}{}^{j}\\
&+\frac{3}{16}W^{-2}(\Sigma{}_{a b}){}^{\beta \gamma}F{}^{a b}\nabla_{\eta}^{r}\big(X{}_{\beta}{}^{i}\big)\lambda{}_{\gamma}{}^{j} -\frac{3}{16}W^{-2}(\Sigma{}_{a b}){}^{\beta \gamma}F{}^{a b}X{}_{\beta}{}^{i}\nabla_{\eta}^{r}\big(\lambda{}_{\gamma}{}^{j}\big)\\
&+\frac{3}{16}\nabla_{\eta}^{r}\big(W^{-2}\big)(\Sigma{}_{a b}){}^{\beta \gamma}F{}^{a b}X{}_{\beta}{}^{j}\lambda{}_{\gamma}{}^{i} +\frac{3}{16}W^{-2}(\Sigma{}_{a b}){}^{\beta \gamma}\nabla_{\eta}^{r}\big(F{}^{a b}\big)X{}_{\beta}{}^{j}\lambda{}_{\gamma}{}^{i}\\
&+\frac{3}{16}W^{-2}(\Sigma{}_{a b}){}^{\beta \gamma}F{}^{a b}\nabla_{\eta}^{r}\big(X{}_{\beta}{}^{j}\big)\lambda{}_{\gamma}{}^{i} -\frac{3}{16}W^{-2}(\Sigma{}_{a b}){}^{\beta \gamma}F{}^{a b}X{}_{\beta}{}^{j}\nabla_{\eta}^{r}\big(\lambda{}_{\gamma}{}^{i}\big)
\end{aligned}
\tag{S3-H2.9-a}
```

Insert the elementary source identities and the applicable commutators (S3-11)–(S3-14), distribute the vector product rules, and contract only index-raising metrics. The resulting contribution is

```math
\begin{aligned}
\left.\nabla_\eta^rH^{ij}\right|_{\mathrm{H2.9}}=&-\frac{3i}{8}W^{-3}\lambda{}_{\eta}{}^{r}(\Sigma{}_{a b}){}^{\beta \gamma}F{}^{a b}X{}_{\beta}{}^{i}\lambda{}_{\gamma}{}^{j} -\frac{3i}{32}W^{-2}(\Sigma{}_{a b}){}^{\beta \gamma}(\Sigma{}^{a b}){}^{\delta \rho}(\Gamma{}^{c}){}_{\eta \delta}\big(\nabla_{c}\lambda{}_{\rho}{}^{r}\big)X{}_{\beta}{}^{i}\lambda{}_{\gamma}{}^{j}\\
&-\frac{3i}{32}W^{-2}(\Sigma{}_{a b}){}^{\beta \gamma}(\Sigma{}^{a b}){}_{\eta}{}^{\delta}(\Gamma{}^{c}){}_{\delta}{}^{\rho}\big(\nabla_{c}\lambda{}_{\rho}{}^{r}\big)X{}_{\beta}{}^{i}\lambda{}_{\gamma}{}^{j} +\frac{3i}{64}W^{-2}(\Sigma{}_{a b}){}^{\beta \gamma}(\Sigma{}^{a b}){}^{\delta \rho}W{}_{\eta \delta}\lambda{}_{\rho}{}^{r}X{}_{\beta}{}^{i}\lambda{}_{\gamma}{}^{j}\\
&-\frac{9i}{64}W^{-2}(\Sigma{}_{a b}){}^{\beta \gamma}(\Sigma{}^{a b}){}_{\eta}{}^{\delta}W{}_{\delta}{}^{\rho}\lambda{}_{\rho}{}^{r}X{}_{\beta}{}^{i}\lambda{}_{\gamma}{}^{j} -\frac{3i}{32}W^{-2}(\Sigma{}_{a b}){}^{\beta \gamma}(\Sigma{}^{a b}){}^{\delta \rho}(\Gamma{}^{c}){}_{\eta \rho}\big(\nabla_{c}\lambda{}_{\delta}{}^{r}\big)X{}_{\beta}{}^{i}\lambda{}_{\gamma}{}^{j}\\
&-\frac{3i}{32}W^{-2}(\Sigma{}_{a b}){}^{\beta \gamma}(\Sigma{}^{a b}){}^{\delta}{}_{\eta}(\Gamma{}^{c}){}_{\delta}{}^{\rho}\big(\nabla_{c}\lambda{}_{\rho}{}^{r}\big)X{}_{\beta}{}^{i}\lambda{}_{\gamma}{}^{j} +\frac{3i}{64}W^{-2}(\Sigma{}_{a b}){}^{\beta \gamma}(\Sigma{}^{a b}){}^{\delta \rho}W{}_{\eta \rho}\lambda{}_{\delta}{}^{r}X{}_{\beta}{}^{i}\lambda{}_{\gamma}{}^{j}\\
&-\frac{9i}{64}W^{-2}(\Sigma{}_{a b}){}^{\beta \gamma}(\Sigma{}^{a b}){}^{\delta}{}_{\eta}W{}_{\delta}{}^{\rho}\lambda{}_{\rho}{}^{r}X{}_{\beta}{}^{i}\lambda{}_{\gamma}{}^{j} -\frac{9i}{32}W^{-2}(\Sigma{}_{a b}){}^{\beta \gamma}(\Sigma{}^{a b}){}^{\delta \rho}W{}_{\delta \rho}\lambda{}_{\eta}{}^{r}X{}_{\beta}{}^{i}\lambda{}_{\gamma}{}^{j}\\
&-\frac{3}{16}W^{-1}(\Sigma{}_{a b}){}^{\beta \gamma}(\Sigma{}^{a b}){}^{\delta \rho}W{}_{\eta \delta \rho}{}^{r}X{}_{\beta}{}^{i}\lambda{}_{\gamma}{}^{j} +\frac{3}{16}W^{-2}(\Sigma{}_{a b}){}^{\beta \gamma}F{}^{a b}X{}_{\eta \beta}{}^{r i}\lambda{}_{\gamma}{}^{j}\\
&+\frac{3i}{128}W^{-2}(\Sigma{}_{a b}){}_{\eta}{}^{\beta}F{}^{a b}\varepsilon{}^{r i}Y\lambda{}_{\beta}{}^{j} -\frac{9i}{32}W^{-2}(\Sigma{}_{a b}){}^{\beta \gamma}F{}^{a b}\varepsilon{}^{r i}(\Gamma{}^{c}){}_{\eta}{}^{\delta}\big(\nabla_{c}W{}_{\beta \delta}\big)\lambda{}_{\gamma}{}^{j}\\
&-\frac{3i}{8}W^{-2}(\Sigma{}_{a b}){}^{\beta \gamma}F{}^{a b}\varepsilon{}^{r i}W{}_{\eta}{}^{\delta}W{}_{\beta \delta}\lambda{}_{\gamma}{}^{j} +\frac{3i}{32}W^{-2}(\Sigma{}_{a b}){}_{\eta}{}^{\beta}F{}^{a b}\varepsilon{}^{r i}W{}^{\gamma \delta}W{}_{\gamma \delta}\lambda{}_{\beta}{}^{j}\\
&-\frac{3i}{32}W^{-2}(\Sigma{}_{a b}){}^{\beta \gamma}F{}^{a b}\varepsilon{}^{r i}(\Gamma{}^{c}){}_{\beta}{}^{\delta}\big(\nabla_{c}W{}_{\eta \delta}\big)\lambda{}_{\gamma}{}^{j} +\frac{3}{8}W^{-2}(\Sigma{}_{a b}){}^{\beta \gamma}F{}^{a b}X{}_{\beta}{}^{i}\varepsilon{}^{r j}F{}_{\eta \gamma}\\
&+\frac{3}{8}W^{-1}(\Sigma{}_{a b}){}^{\beta \gamma}F{}^{a b}X{}_{\beta}{}^{i}\varepsilon{}^{r j}W{}_{\eta \gamma} +\frac{3}{16}W^{-2}(\Sigma{}_{a b}){}^{\beta}{}_{\eta}F{}^{a b}X{}_{\beta}{}^{i}X{}^{r j}\\
&+\frac{3}{16}W^{-2}(\Sigma{}_{a b}){}^{\beta \gamma}F{}^{a b}X{}_{\beta}{}^{i}\varepsilon{}^{r j}(\Gamma{}^{c}){}_{\eta \gamma}\big(\nabla_{c}W\big) -\frac{3i}{8}W^{-3}\lambda{}_{\eta}{}^{r}(\Sigma{}_{a b}){}^{\beta \gamma}F{}^{a b}X{}_{\beta}{}^{j}\lambda{}_{\gamma}{}^{i}\\
&-\frac{3i}{32}W^{-2}(\Sigma{}_{a b}){}^{\beta \gamma}(\Sigma{}^{a b}){}^{\delta \rho}(\Gamma{}^{c}){}_{\eta \delta}\big(\nabla_{c}\lambda{}_{\rho}{}^{r}\big)X{}_{\beta}{}^{j}\lambda{}_{\gamma}{}^{i} -\frac{3i}{32}W^{-2}(\Sigma{}_{a b}){}^{\beta \gamma}(\Sigma{}^{a b}){}_{\eta}{}^{\delta}(\Gamma{}^{c}){}_{\delta}{}^{\rho}\big(\nabla_{c}\lambda{}_{\rho}{}^{r}\big)X{}_{\beta}{}^{j}\lambda{}_{\gamma}{}^{i}\\
&+\frac{3i}{64}W^{-2}(\Sigma{}_{a b}){}^{\beta \gamma}(\Sigma{}^{a b}){}^{\delta \rho}W{}_{\eta \delta}\lambda{}_{\rho}{}^{r}X{}_{\beta}{}^{j}\lambda{}_{\gamma}{}^{i} -\frac{9i}{64}W^{-2}(\Sigma{}_{a b}){}^{\beta \gamma}(\Sigma{}^{a b}){}_{\eta}{}^{\delta}W{}_{\delta}{}^{\rho}\lambda{}_{\rho}{}^{r}X{}_{\beta}{}^{j}\lambda{}_{\gamma}{}^{i}\\
&-\frac{3i}{32}W^{-2}(\Sigma{}_{a b}){}^{\beta \gamma}(\Sigma{}^{a b}){}^{\delta \rho}(\Gamma{}^{c}){}_{\eta \rho}\big(\nabla_{c}\lambda{}_{\delta}{}^{r}\big)X{}_{\beta}{}^{j}\lambda{}_{\gamma}{}^{i} -\frac{3i}{32}W^{-2}(\Sigma{}_{a b}){}^{\beta \gamma}(\Sigma{}^{a b}){}^{\delta}{}_{\eta}(\Gamma{}^{c}){}_{\delta}{}^{\rho}\big(\nabla_{c}\lambda{}_{\rho}{}^{r}\big)X{}_{\beta}{}^{j}\lambda{}_{\gamma}{}^{i}\\
&+\frac{3i}{64}W^{-2}(\Sigma{}_{a b}){}^{\beta \gamma}(\Sigma{}^{a b}){}^{\delta \rho}W{}_{\eta \rho}\lambda{}_{\delta}{}^{r}X{}_{\beta}{}^{j}\lambda{}_{\gamma}{}^{i} -\frac{9i}{64}W^{-2}(\Sigma{}_{a b}){}^{\beta \gamma}(\Sigma{}^{a b}){}^{\delta}{}_{\eta}W{}_{\delta}{}^{\rho}\lambda{}_{\rho}{}^{r}X{}_{\beta}{}^{j}\lambda{}_{\gamma}{}^{i}\\
&-\frac{9i}{32}W^{-2}(\Sigma{}_{a b}){}^{\beta \gamma}(\Sigma{}^{a b}){}^{\delta \rho}W{}_{\delta \rho}\lambda{}_{\eta}{}^{r}X{}_{\beta}{}^{j}\lambda{}_{\gamma}{}^{i} -\frac{3}{16}W^{-1}(\Sigma{}_{a b}){}^{\beta \gamma}(\Sigma{}^{a b}){}^{\delta \rho}W{}_{\eta \delta \rho}{}^{r}X{}_{\beta}{}^{j}\lambda{}_{\gamma}{}^{i}\\
&+\frac{3}{16}W^{-2}(\Sigma{}_{a b}){}^{\beta \gamma}F{}^{a b}X{}_{\eta \beta}{}^{r j}\lambda{}_{\gamma}{}^{i} +\frac{3i}{128}W^{-2}(\Sigma{}_{a b}){}_{\eta}{}^{\beta}F{}^{a b}\varepsilon{}^{r j}Y\lambda{}_{\beta}{}^{i}\\
&-\frac{9i}{32}W^{-2}(\Sigma{}_{a b}){}^{\beta \gamma}F{}^{a b}\varepsilon{}^{r j}(\Gamma{}^{c}){}_{\eta}{}^{\delta}\big(\nabla_{c}W{}_{\beta \delta}\big)\lambda{}_{\gamma}{}^{i} -\frac{3i}{8}W^{-2}(\Sigma{}_{a b}){}^{\beta \gamma}F{}^{a b}\varepsilon{}^{r j}W{}_{\eta}{}^{\delta}W{}_{\beta \delta}\lambda{}_{\gamma}{}^{i}\\
&+\frac{3i}{32}W^{-2}(\Sigma{}_{a b}){}_{\eta}{}^{\beta}F{}^{a b}\varepsilon{}^{r j}W{}^{\gamma \delta}W{}_{\gamma \delta}\lambda{}_{\beta}{}^{i} -\frac{3i}{32}W^{-2}(\Sigma{}_{a b}){}^{\beta \gamma}F{}^{a b}\varepsilon{}^{r j}(\Gamma{}^{c}){}_{\beta}{}^{\delta}\big(\nabla_{c}W{}_{\eta \delta}\big)\lambda{}_{\gamma}{}^{i}\\
&+\frac{3}{8}W^{-2}(\Sigma{}_{a b}){}^{\beta \gamma}F{}^{a b}X{}_{\beta}{}^{j}\varepsilon{}^{r i}F{}_{\eta \gamma} +\frac{3}{8}W^{-1}(\Sigma{}_{a b}){}^{\beta \gamma}F{}^{a b}X{}_{\beta}{}^{j}\varepsilon{}^{r i}W{}_{\eta \gamma}\\
&+\frac{3}{16}W^{-2}(\Sigma{}_{a b}){}^{\beta}{}_{\eta}F{}^{a b}X{}_{\beta}{}^{j}X{}^{r i} +\frac{3}{16}W^{-2}(\Sigma{}_{a b}){}^{\beta \gamma}F{}^{a b}X{}_{\beta}{}^{j}\varepsilon{}^{r i}(\Gamma{}^{c}){}_{\eta \gamma}\big(\nabla_{c}W\big)
\end{aligned}
\tag{S3-H2.9-b}
```

**Check for H2.9:** all 42 written summands have weight $`7/2`$, odd parity and the same free indices $`\eta;r,i,j`$. Dummy labels are paired. The coefficient $`1/3`$ and the two external epsilons are applied once, when collecting the spinor.

#### Input H2.10

The calculated input is

```math
\left.H^{ij}\right|_{\mathrm{H2.10}}=W^{-2}\big(\frac{3i}{128}W^{ab}W_{ab}\lambda^{\alpha i}\lambda_\alpha^j\big).
\tag{S3-H2.10-input}
```

Apply the product rule (S3-09), in the displayed factor order:

```math
\begin{aligned}
\left.\nabla_\eta^rH^{ij}\right|_{\mathrm{H2.10}}=&\frac{3i}{128}\nabla_{\eta}^{r}\big(W^{-2}\big)W{}^{a b}W{}_{a b}\lambda{}^{\beta i}\lambda{}_{\beta}{}^{j} +\frac{3i}{128}W^{-2}\nabla_{\eta}^{r}\big(W{}^{a b}\big)W{}_{a b}\lambda{}^{\beta i}\lambda{}_{\beta}{}^{j}\\
&+\frac{3i}{128}W^{-2}W{}^{a b}\nabla_{\eta}^{r}\big(W{}_{a b}\big)\lambda{}^{\beta i}\lambda{}_{\beta}{}^{j} +\frac{3i}{128}W^{-2}W{}^{a b}W{}_{a b}\nabla_{\eta}^{r}\big(\lambda{}^{\beta i}\big)\lambda{}_{\beta}{}^{j}\\
&-\frac{3i}{128}W^{-2}W{}^{a b}W{}_{a b}\lambda{}^{\beta i}\nabla_{\eta}^{r}\big(\lambda{}_{\beta}{}^{j}\big)
\end{aligned}
\tag{S3-H2.10-a}
```

Insert the elementary source identities and the applicable commutators (S3-11)–(S3-14), distribute the vector product rules, and contract only index-raising metrics. The resulting contribution is

```math
\begin{aligned}
\left.\nabla_\eta^rH^{ij}\right|_{\mathrm{H2.10}}=&\frac{3}{64}W^{-3}\lambda{}_{\eta}{}^{r}W{}^{a b}W{}_{a b}\lambda{}^{\beta i}\lambda{}_{\beta}{}^{j} +\frac{3i}{128}W^{-2}(\Sigma{}^{a b}){}^{\beta \gamma}W{}_{\eta \beta \gamma}{}^{r}W{}_{a b}\lambda{}^{\delta i}\lambda{}_{\delta}{}^{j}\\
&+\frac{3i}{256}W^{-2}(\Sigma{}^{a b}){}_{\eta}{}^{\beta}X{}_{\beta}{}^{r}W{}_{a b}\lambda{}^{\gamma i}\lambda{}_{\gamma}{}^{j} +\frac{3i}{256}W^{-2}(\Sigma{}^{a b}){}^{\beta}{}_{\eta}X{}_{\beta}{}^{r}W{}_{a b}\lambda{}^{\gamma i}\lambda{}_{\gamma}{}^{j}\\
&+\frac{3i}{128}W^{-2}W{}^{a b}(\Sigma{}_{a b}){}^{\beta \gamma}W{}_{\eta \beta \gamma}{}^{r}\lambda{}^{\delta i}\lambda{}_{\delta}{}^{j} +\frac{3i}{256}W^{-2}W{}^{a b}(\Sigma{}_{a b}){}_{\eta}{}^{\beta}X{}_{\beta}{}^{r}\lambda{}^{\gamma i}\lambda{}_{\gamma}{}^{j}\\
&+\frac{3i}{256}W^{-2}W{}^{a b}(\Sigma{}_{a b}){}^{\beta}{}_{\eta}X{}_{\beta}{}^{r}\lambda{}^{\gamma i}\lambda{}_{\gamma}{}^{j} -\frac{3i}{64}W^{-2}W{}^{a b}W{}_{a b}\varepsilon{}^{r i}F{}_{\eta}{}^{\beta}\lambda{}_{\beta}{}^{j}\\
&-\frac{3i}{64}W^{-1}W{}^{a b}W{}_{a b}\varepsilon{}^{r i}W{}_{\eta}{}^{\beta}\lambda{}_{\beta}{}^{j} +\frac{3i}{128}W^{-2}W{}^{a b}W{}_{a b}X{}^{r i}\lambda{}_{\eta}{}^{j}\\
&-\frac{3i}{128}W^{-2}W{}^{a b}W{}_{a b}\varepsilon{}^{r i}(\Gamma{}^{c}){}_{\eta}{}^{\beta}\big(\nabla_{c}W\big)\lambda{}_{\beta}{}^{j} +\frac{3i}{64}W^{-2}W{}^{a b}W{}_{a b}\lambda{}^{\beta i}\varepsilon{}^{r j}F{}_{\eta \beta}\\
&+\frac{3i}{64}W^{-1}W{}^{a b}W{}_{a b}\lambda{}^{\beta i}\varepsilon{}^{r j}W{}_{\eta \beta} +\frac{3i}{128}W^{-2}W{}^{a b}W{}_{a b}\lambda{}_{\eta}{}^{i}X{}^{r j}\\
&+\frac{3i}{128}W^{-2}W{}^{a b}W{}_{a b}\lambda{}^{\beta i}\varepsilon{}^{r j}(\Gamma{}^{c}){}_{\eta \beta}\big(\nabla_{c}W\big)
\end{aligned}
\tag{S3-H2.10-b}
```

**Check for H2.10:** all 15 written summands have weight $`7/2`$, odd parity and the same free indices $`\eta;r,i,j`$. Dummy labels are paired. The coefficient $`1/3`$ and the two external epsilons are applied once, when collecting the spinor.

#### Input H2.11

The calculated input is

```math
\left.H^{ij}\right|_{\mathrm{H2.11}}=W^{-2}\big(\frac{9i}{256}\varepsilon^{abcde}(\Gamma_a)^{\alpha\beta}W_{bc}W_{de}\lambda_\alpha^i\lambda_\beta^j\big).
\tag{S3-H2.11-input}
```

Expand each written SU(2) average with weight $`1/2`$ before applying the left derivative.

Apply the product rule (S3-09), in the displayed factor order:

```math
\begin{aligned}
\left.\nabla_\eta^rH^{ij}\right|_{\mathrm{H2.11}}=&\frac{9i}{256}\nabla_{\eta}^{r}\big(W^{-2}\big)\varepsilon{}^{a b c d e}(\Gamma{}_{a}){}^{\beta \gamma}W{}_{b c}W{}_{d e}\lambda{}_{\beta}{}^{i}\lambda{}_{\gamma}{}^{j} +\frac{9i}{256}W^{-2}\varepsilon{}^{a b c d e}(\Gamma{}_{a}){}^{\beta \gamma}\nabla_{\eta}^{r}\big(W{}_{b c}\big)W{}_{d e}\lambda{}_{\beta}{}^{i}\lambda{}_{\gamma}{}^{j}\\
&+\frac{9i}{256}W^{-2}\varepsilon{}^{a b c d e}(\Gamma{}_{a}){}^{\beta \gamma}W{}_{b c}\nabla_{\eta}^{r}\big(W{}_{d e}\big)\lambda{}_{\beta}{}^{i}\lambda{}_{\gamma}{}^{j} +\frac{9i}{256}W^{-2}\varepsilon{}^{a b c d e}(\Gamma{}_{a}){}^{\beta \gamma}W{}_{b c}W{}_{d e}\nabla_{\eta}^{r}\big(\lambda{}_{\beta}{}^{i}\big)\lambda{}_{\gamma}{}^{j}\\
&-\frac{9i}{256}W^{-2}\varepsilon{}^{a b c d e}(\Gamma{}_{a}){}^{\beta \gamma}W{}_{b c}W{}_{d e}\lambda{}_{\beta}{}^{i}\nabla_{\eta}^{r}\big(\lambda{}_{\gamma}{}^{j}\big)
\end{aligned}
\tag{S3-H2.11-a}
```

Insert the elementary source identities and the applicable commutators (S3-11)–(S3-14), distribute the vector product rules, and contract only index-raising metrics. The resulting contribution is

```math
\begin{aligned}
\left.\nabla_\eta^rH^{ij}\right|_{\mathrm{H2.11}}=&\frac{9}{128}W^{-3}\lambda{}_{\eta}{}^{r}\varepsilon{}^{a b c d e}(\Gamma{}_{a}){}^{\beta \gamma}W{}_{b c}W{}_{d e}\lambda{}_{\beta}{}^{i}\lambda{}_{\gamma}{}^{j} +\frac{9i}{256}W^{-2}\varepsilon{}^{a b c d e}(\Gamma{}_{a}){}^{\beta \gamma}(\Sigma{}_{b c}){}^{\delta \rho}W{}_{\eta \delta \rho}{}^{r}W{}_{d e}\lambda{}_{\beta}{}^{i}\lambda{}_{\gamma}{}^{j}\\
&+\frac{9i}{512}W^{-2}\varepsilon{}^{a b c d e}(\Gamma{}_{a}){}^{\beta \gamma}(\Sigma{}_{b c}){}_{\eta}{}^{\delta}X{}_{\delta}{}^{r}W{}_{d e}\lambda{}_{\beta}{}^{i}\lambda{}_{\gamma}{}^{j} +\frac{9i}{512}W^{-2}\varepsilon{}^{a b c d e}(\Gamma{}_{a}){}^{\beta \gamma}(\Sigma{}_{b c}){}^{\delta}{}_{\eta}X{}_{\delta}{}^{r}W{}_{d e}\lambda{}_{\beta}{}^{i}\lambda{}_{\gamma}{}^{j}\\
&+\frac{9i}{256}W^{-2}\varepsilon{}^{a b c d e}(\Gamma{}_{a}){}^{\beta \gamma}W{}_{b c}(\Sigma{}_{d e}){}^{\delta \rho}W{}_{\eta \delta \rho}{}^{r}\lambda{}_{\beta}{}^{i}\lambda{}_{\gamma}{}^{j} +\frac{9i}{512}W^{-2}\varepsilon{}^{a b c d e}(\Gamma{}_{a}){}^{\beta \gamma}W{}_{b c}(\Sigma{}_{d e}){}_{\eta}{}^{\delta}X{}_{\delta}{}^{r}\lambda{}_{\beta}{}^{i}\lambda{}_{\gamma}{}^{j}\\
&+\frac{9i}{512}W^{-2}\varepsilon{}^{a b c d e}(\Gamma{}_{a}){}^{\beta \gamma}W{}_{b c}(\Sigma{}_{d e}){}^{\delta}{}_{\eta}X{}_{\delta}{}^{r}\lambda{}_{\beta}{}^{i}\lambda{}_{\gamma}{}^{j} -\frac{9i}{128}W^{-2}\varepsilon{}^{a b c d e}(\Gamma{}_{a}){}^{\beta \gamma}W{}_{b c}W{}_{d e}\varepsilon{}^{r i}F{}_{\eta \beta}\lambda{}_{\gamma}{}^{j}\\
&-\frac{9i}{128}W^{-1}\varepsilon{}^{a b c d e}(\Gamma{}_{a}){}^{\beta \gamma}W{}_{b c}W{}_{d e}\varepsilon{}^{r i}W{}_{\eta \beta}\lambda{}_{\gamma}{}^{j} -\frac{9i}{256}W^{-2}\varepsilon{}^{a b c d e}(\Gamma{}_{a}){}_{\eta}{}^{\beta}W{}_{b c}W{}_{d e}X{}^{r i}\lambda{}_{\beta}{}^{j}\\
&-\frac{9i}{256}W^{-2}\varepsilon{}^{a b c d e}(\Gamma{}_{a}){}^{\beta \gamma}W{}_{b c}W{}_{d e}\varepsilon{}^{r i}(\Gamma{}^{f}){}_{\eta \beta}\big(\nabla_{f}W\big)\lambda{}_{\gamma}{}^{j} +\frac{9i}{128}W^{-2}\varepsilon{}^{a b c d e}(\Gamma{}_{a}){}^{\beta \gamma}W{}_{b c}W{}_{d e}\lambda{}_{\beta}{}^{i}\varepsilon{}^{r j}F{}_{\eta \gamma}\\
&+\frac{9i}{128}W^{-1}\varepsilon{}^{a b c d e}(\Gamma{}_{a}){}^{\beta \gamma}W{}_{b c}W{}_{d e}\lambda{}_{\beta}{}^{i}\varepsilon{}^{r j}W{}_{\eta \gamma} +\frac{9i}{256}W^{-2}\varepsilon{}^{a b c d e}(\Gamma{}_{a}){}^{\beta}{}_{\eta}W{}_{b c}W{}_{d e}\lambda{}_{\beta}{}^{i}X{}^{r j}\\
&+\frac{9i}{256}W^{-2}\varepsilon{}^{a b c d e}(\Gamma{}_{a}){}^{\beta \gamma}W{}_{b c}W{}_{d e}\lambda{}_{\beta}{}^{i}\varepsilon{}^{r j}(\Gamma{}^{f}){}_{\eta \gamma}\big(\nabla_{f}W\big)
\end{aligned}
\tag{S3-H2.11-b}
```

**Check for H2.11:** all 15 written summands have weight $`7/2`$, odd parity and the same free indices $`\eta;r,i,j`$. Dummy labels are paired. The coefficient $`1/3`$ and the two external epsilons are applied once, when collecting the spinor.

#### Input H2.12

The calculated input is

```math
\left.H^{ij}\right|_{\mathrm{H2.12}}=W^{-2}\big(-\frac38X^{ij}X^{\alpha k}\lambda_{\alpha k}\big).
\tag{S3-H2.12-input}
```

Apply the product rule (S3-09), in the displayed factor order:

```math
\begin{aligned}
\left.\nabla_\eta^rH^{ij}\right|_{\mathrm{H2.12}}=&-\frac{3}{8}\nabla_{\eta}^{r}\big(W^{-2}\big)X{}^{i j}X{}^{\beta k}\lambda{}_{\beta k} -\frac{3}{8}W^{-2}\nabla_{\eta}^{r}\big(X{}^{i j}\big)X{}^{\beta k}\lambda{}_{\beta k}\\
&-\frac{3}{8}W^{-2}X{}^{i j}\nabla_{\eta}^{r}\big(X{}^{\beta k}\big)\lambda{}_{\beta k} +\frac{3}{8}W^{-2}X{}^{i j}X{}^{\beta k}\nabla_{\eta}^{r}\big(\lambda{}_{\beta k}\big)
\end{aligned}
\tag{S3-H2.12-a}
```

Insert the elementary source identities and the applicable commutators (S3-11)–(S3-14), distribute the vector product rules, and contract only index-raising metrics. The resulting contribution is

```math
\begin{aligned}
\left.\nabla_\eta^rH^{ij}\right|_{\mathrm{H2.12}}=&\frac{3i}{4}W^{-3}\lambda{}_{\eta}{}^{r}X{}^{i j}X{}^{\beta k}\lambda{}_{\beta k} -\frac{3i}{8}W^{-2}\varepsilon{}^{r i}(\Gamma{}^{a}){}_{\eta}{}^{\beta}\big(\nabla_{a}\lambda{}_{\beta}{}^{j}\big)X{}^{\gamma k}\lambda{}_{\gamma k}\\
&+\frac{3i}{16}W^{-2}\varepsilon{}^{r i}W{}_{\eta \beta}\lambda{}^{\beta j}X{}^{\gamma k}\lambda{}_{\gamma k} +\frac{9}{32}W^{-1}\varepsilon{}^{r i}X{}_{\eta}{}^{j}X{}^{\beta k}\lambda{}_{\beta k}\\
&-\frac{3i}{8}W^{-2}\varepsilon{}^{r j}(\Gamma{}^{a}){}_{\eta}{}^{\beta}\big(\nabla_{a}\lambda{}_{\beta}{}^{i}\big)X{}^{\gamma k}\lambda{}_{\gamma k} +\frac{3i}{16}W^{-2}\varepsilon{}^{r j}W{}_{\eta \beta}\lambda{}^{\beta i}X{}^{\gamma k}\lambda{}_{\gamma k}\\
&+\frac{9}{32}W^{-1}\varepsilon{}^{r j}X{}_{\eta}{}^{i}X{}^{\beta k}\lambda{}_{\beta k} -\frac{3}{8}W^{-2}X{}^{i j}X{}_{\eta}{}^{\beta r k}\lambda{}_{\beta k}\\
&+\frac{3i}{64}W^{-2}X{}^{i j}Y\lambda{}_{\eta}{}^{r} +\frac{9i}{16}W^{-2}X{}^{i j}(\Gamma{}^{a}){}_{\eta}{}^{\beta}\big(\nabla_{a}W{}^{\gamma}{}_{\beta}\big)\lambda{}_{\gamma}{}^{r}\\
&+\frac{3i}{4}W^{-2}X{}^{i j}W{}_{\eta}{}^{\beta}W{}^{\gamma}{}_{\beta}\lambda{}_{\gamma}{}^{r} +\frac{3i}{16}W^{-2}X{}^{i j}W{}^{\beta \gamma}W{}_{\beta \gamma}\lambda{}_{\eta}{}^{r}\\
&+\frac{3i}{16}W^{-2}X{}^{i j}(\Gamma{}^{a}){}^{\beta \gamma}\big(\nabla_{a}W{}_{\eta \gamma}\big)\lambda{}_{\beta}{}^{r} +\frac{3}{4}W^{-2}X{}^{i j}X{}^{\beta r}F{}_{\eta \beta}\\
&+\frac{3}{4}W^{-1}X{}^{i j}X{}^{\beta r}W{}_{\eta \beta} -\frac{3}{8}W^{-2}X{}^{i j}X{}_{\eta}{}^{k}X{}^{r}{}_{k}\\
&+\frac{3}{8}W^{-2}X{}^{i j}X{}^{\beta r}(\Gamma{}^{a}){}_{\eta \beta}\big(\nabla_{a}W\big)
\end{aligned}
\tag{S3-H2.12-b}
```

**Check for H2.12:** all 17 written summands have weight $`7/2`$, odd parity and the same free indices $`\eta;r,i,j`$. Dummy labels are paired. The coefficient $`1/3`$ and the two external epsilons are applied once, when collecting the spinor.

[Component index](../STEP_03_LOG_SPINOR.md) · [Next component](derivation_002.md)
