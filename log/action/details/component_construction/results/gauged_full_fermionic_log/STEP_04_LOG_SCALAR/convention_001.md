# LOG scalar superfield — S4-01 – S4-H0.1-product

<a id="step-4--deriving-the-log-scalar-superfield--definitions-and-conventions"></a>

[Component index](../STEP_04_LOG_SCALAR.md).

---
title: "Step 4 — LOG scalar from the calculated primary and spinor"
date: 2026-09-23
status: "Source-frame scalar descent; retained project-frame projection/reality and full-primary constraints certified separately"
procedure: GAUGED-LOG-G25-S23-PROCEDURE-v1
fermion_order: all
---

## Step 4 — deriving the LOG scalar superfield

<!-- LOG_CURRENT_CERTIFICATION_20260925 -->

**Current scope:** [the 2026-09-25 certificate](../CERTIFICATION_LOG_TWO_FERMI_2026-09-25.md) verifies the full primary and the component action through two physical fermions. The source comparisons and restricted tests below retain their stated mathematical scope.

**Source-algebra repair, 2026-09-25.** This rebuilt result includes the two factors of $`i`$ required in the K-generator part of C24 (A.1l). The printed source is preserved, and the correction is established by the independent SDD super-Jacobi certificate. See [the full certification record](../../../../../../../references/source_evidence/README.md).

**Derivative notation.** This stage uses the full Gold superspace $`\nabla_A`$. Step 6 transports it to the full project $`\mathcal D_a`$ and $`\Box^c=\mathcal D^a\mathcal D_a`$, including Q/S/K connections, as in the fermionic Weyl-squared calculation. No connection-only derivative replaces it.

## 1. Target, inputs and scope

We use the **calculated** primary in [STEP_02_LOG_PRIMARY.md](../STEP_02_LOG_PRIMARY.md), Eq. (S2-193), and its spinor descendant in [STEP_03_LOG_SPINOR.md](../STEP_03_LOG_SPINOR.md), Eq. (S3-200). In particular, the primary input H3.9 has the derived coefficient $`+i/4`$. The unchanged printed S23 primary is not substituted for this input.

The definition is S23 (3.26b), [On curvature-squared invariants of minimal five-dimensional supergravity from superspace — PDF22](https://arxiv.org/abs/2302.14295). The equivalent spinor trace is given explicitly in C24 (2.42b), [Components of curvature-squared invariants of minimal supergravity in five dimensions — PDF20](https://arxiv.org/abs/2311.00679):

```math
F_{\log W}=\frac{i}{12}\nabla^{\alpha i}\nabla_\alpha^jH_{ij}
=-\frac{i}{4}\nabla^{\alpha i}\varphi_{\alpha i},\qquad
\varphi_\alpha^i=\frac13\nabla_{\alpha j}H^{ij}.
\tag{S4-01}
```

All equations, including the collected result in §8, remain **superfield equations** in the Gold traceless Standard-Weyl superspace frame. This is the same stage as the calculated $`H^{ij}`$ and LOG spinor. The Weyl descendants retain their source names $`W_{ab}`$, $`X_\alpha^i`$, $`X_{\alpha\beta}^{ij}`$ and $`Y`$. The vector derivative and geometric curvatures are superspace objects. This endpoint deliberately remains in the source frame; its component projection and conversion are carried out in Step 6 and certified at the retained order. The unreduced expression is stated in the source frame; its component projection and conversion are given by Step 6.

**A1.** Five-dimensional classical conformal superspace, exact and off shell. **A2.** The scalar patch is $`W>0`$. **A3.** All fermion orders are retained; no field equation, auxiliary elimination, gauge fixing, background restriction, or field redefinition is used in the derivation. **A4.** All equalities are local. No integration by parts or boundary identification is made. **A5.** Restricted field assignments are used only for coefficient checks, after differentiation; they are not backgrounds imposed on the invariant.

The formula is long because explicit epsilon and gamma contractions are retained. No spinor derivative or generator action remains in its endpoint. Terms which could cancel after further tensor or Fierz identities are still written. The complete result is at the end, with two summands per row. Consecutive display blocks there are typographical continuations of **one sum**, not separately defined component fields.

## 2. Convention ledger and the trace sign

<!-- ASSERT_CONVENTION: source_frame=Gold traceless Standard-Weyl superspace, metric_signature=(-,+,+,+,+), natural_units=hbar=c=1, derivative_parity=odd left, fermions=all degrees retained, regularization_scheme=Not applicable for initial classical analysis, renormalization_scheme=Not applicable for initial classical analysis -->

The [main source conventions](../CONVENTIONS.md) and [LOG working conventions](../LOG_CONVENTIONS.md) control this calculation. We use the scoped Gold superspace conventions.

| Item | Convention |
|---|---|
| Indices | $`a,b=0,\ldots,4`$; $`\alpha,\beta=1,\ldots,4`$; $`i,j=1,2`$ |
| Metric, gamma matrices | $`\eta=(-,+,+,+,+)`$; $`\{\Gamma^a,\Gamma^b\}=-2\eta^{ab}`$; $`\Sigma^{ab}=-[\Gamma^a,\Gamma^b]/4`$ |
| Orientation | $`\varepsilon^{01234}=-1`$, $`\varepsilon_{01234}=+1`$ |
| Spinor metrics | $`\zeta^\alpha=\varepsilon^{\alpha\beta}\zeta_\beta`$; $`\varepsilon^{\alpha\gamma}\varepsilon_{\gamma\beta}=\delta^\alpha{}_{\beta}`$ |
| SU(2) metrics | $`\zeta_i=\varepsilon_{ij}\zeta^j`$; $`\varepsilon^{12}=\varepsilon_{21}=1`$ |
| Symmetrization | Unit weight; the actual averages are expanded in the calculations below |
| Odd quantities | $`\lambda_\alpha^i`$, $`X_\alpha^i`$, $`W_{\alpha\beta\gamma}{}^i`$, spinor derivatives and supersymmetry parameters |
| Ordering | Left odd derivatives; no unrecorded exchange of odd factors |
| Curvature sign | $`[\nabla_A,\nabla_B\}=-\mathcal T_{AB}{}^C\nabla_C-\frac12\mathcal R(M)_{AB}{}^{cd}M_{cd}-\mathcal R(J)_{AB}{}^{kl}J_{kl}-\mathcal R(\mathbb D)_{AB}\mathbb D-\mathcal R(S)_{AB}{}^{\gamma k}S_{\gamma k}-\mathcal R(K)_{AB}{}^cK_c`$ |
| Reality | Gold symplectic reality; no conjugation or bilinear flip is used as an algebraic shortcut |
| Couplings | This is a local multiplet component; no action coefficient, Fourier convention, quantum-state normalization or renormalization expansion enters |

The scalar $`W`$ is distinct from the Weyl tensor $`W_{ab}`$. The vector auxiliary $`X^{ij}`$ is distinct from the Weyl descendants $`X_\alpha^i`$, $`X_{\alpha\beta}^{ij}`$ and $`Y`$. All covariant derivatives are the full superconformal derivatives. In particular, $`\Box=\nabla^a\nabla_a`$.

Lower the spinor descendant's SU(2) index, substitute its definition, and raise only the derivative's spinor index:

```math
\begin{aligned}
\varphi_{\eta t}&=\varepsilon_{ti}\varphi_\eta^i
=\frac13\varepsilon_{ti}\varepsilon_{jr}\nabla_\eta^rH^{ij},\\
\nabla^{\eta t}\varphi_{\eta t}
&=\frac13\varepsilon^{\eta\zeta}\varepsilon_{ti}\varepsilon_{jr}
\nabla_\zeta^t\nabla_\eta^rH^{ij},\\
F_{\log W}&=-\frac{i}{12}\varepsilon^{\eta\zeta}\varepsilon_{ti}\varepsilon_{jr}
\nabla_\zeta^t\nabla_\eta^rH^{ij}.
\end{aligned}
\tag{S4-02}
```

No two derivatives were interchanged. Starting instead with the first expression in (S4-01), the second lowering factor is $`\varepsilon_{rj}=-\varepsilon_{jr}`$; this produces precisely the minus sign in (S4-02). Thus the plus sign in the two-derivative definition and the minus sign in the spinor trace are consistent.

As a normalization check, use C24 (2.41b):

```math
\begin{aligned}
\nabla_\beta^i\varphi_\alpha^j
&=-\frac i2\varepsilon^{ij}\varepsilon_{\beta\alpha}F
+\frac i2\varepsilon^{ij}\mathcal H_{\beta\alpha}
+i(\Gamma^a)_{\beta\alpha}\nabla_aH^{ij},\\
\varepsilon^{\alpha\beta}\varepsilon_{ij}\nabla_\beta^i\varphi_\alpha^j
&=-\frac i2(-2)(4)F+0+0=4iF,\\
-\frac i4(4iF)&=F.
\end{aligned}
\tag{S4-03}
```

The second term has zero spinor trace because $`\mathcal H_{\alpha\beta}=(\Gamma^a)_{\alpha\beta}\mathcal H_a`$ is symplectic-traceless; the third has zero SU(2) trace because $`H^{ij}`$ is symmetric. Here $`\varepsilon_{ij}\varepsilon^{ij}=-2`$ and $`\varepsilon^{\alpha\beta}\varepsilon_{\beta\alpha}=4`$.

## 3. Identities used in the second descent

The source identities below are the same ones used for the spinor, now supplemented by the action on higher vector descendants. They are cited and displayed before their use. Source images were checked for their index positions: S23 (2.6a–f), (2.8), [On curvature-squared invariants of minimal five-dimensional supergravity from superspace — PDF9](https://arxiv.org/abs/2302.14295); S23 (2.13), [On curvature-squared invariants of minimal five-dimensional supergravity from superspace — PDF10](https://arxiv.org/abs/2302.14295)–[On curvature-squared invariants of minimal five-dimensional supergravity from superspace — PDF11](https://arxiv.org/abs/2302.14295); C24 (A.1), (A.3), [Components of curvature-squared invariants of minimal supergravity in five dimensions — PDF81](https://arxiv.org/abs/2311.00679)–[Components of curvature-squared invariants of minimal supergravity in five dimensions — PDF83](https://arxiv.org/abs/2311.00679).

### 3.1 Elementary derivative and curvature identities

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
\tag{S4-I-WEYL}
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
\tag{S4-I-VECTOR}
```

For example, expansion of the weighted SU(2) average in the vector rule gives

```math
\begin{aligned}
\nabla_\eta^rX^{ij}={}&i\varepsilon^{ri}(\Gamma^a)_\eta{}^\beta\nabla_a\lambda_\beta^j+i\varepsilon^{rj}(\Gamma^a)_\eta{}^\beta\nabla_a\lambda_\beta^i\\
&-\tfrac i2\varepsilon^{ri}W_{\eta\beta}\lambda^{\beta j}-\tfrac i2\varepsilon^{rj}W_{\eta\beta}\lambda^{\beta i}-\tfrac34\varepsilon^{ri}X_\eta^jW-\tfrac34\varepsilon^{rj}X_\eta^iW.
\end{aligned}
\tag{S4-I-04}
```

The $`-3/4`$ is $`(2i)(1/2)(3i/4)`$. No SU(2) factor is suppressed. Spinor and SU(2) raising/lowering commute with $`\nabla`$ because their metrics are covariantly constant. The same statement applies to the gamma matrices and $`\eta_{ab}`$.

### 3.2 The geometric tensors retained in the result

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
\tag{S4-I-05}
```

The entire $`K`$ curvature, including the three terms continued onto PDF83, is

```math
\begin{aligned}
\mathcal R(K)_{a\eta}{}^{rb}={}&\tfrac16(\Gamma^b)_\eta{}^\beta\nabla^cW_{ca\beta}{}^r+\tfrac1{12}(\Gamma_a)_\eta{}^\beta\nabla^cW_c{}^b{}_{\beta}{}^r+\tfrac16\nabla_\eta{}^\beta W_a{}^b{}_{\beta}{}^r-\tfrac1{24}\varepsilon_a{}^{bcde}\nabla_cW_{de\eta}{}^r\\
&+\tfrac18(\Gamma^b)_\eta{}^\beta\nabla_aX_\beta^r+\tfrac1{64}W^{cd}(3\Gamma_a\Sigma_{cd}\Gamma^b-\Sigma_{cd}\Gamma_a\Gamma^b)_\eta{}^\beta X_\beta^r-\tfrac1{48}\widetilde W_{acd}(\Gamma^b)_\eta{}^\beta W^{cd}{}_{\beta}{}^r\\
&+\tfrac18\delta_a{}^bW^{cd}W_{cd\eta}{}^r+\tfrac1{12}(\Sigma_a{}^b)_\eta{}^\beta W_{cd\beta}{}^rW^{cd}-\tfrac1{12}W^{cd}(\Sigma_{cd})_\eta{}^\beta W_a{}^b{}_{\beta}{}^r\\
&+\tfrac{13}{48}W_{ac}W^{cb}{}_{\eta}{}^r+\tfrac{11}{48}W_{ac\eta}{}^rW^{cb}-\tfrac{13}{96}(\Gamma_a)_\eta{}^\beta W_{cd\beta}{}^r\widetilde W^{cdb}.
\end{aligned}
\tag{S4-I-06}
```

Thus retaining $`\mathcal R(K)`$ does not mean setting its fermions to zero or using an unspecified remainder. It denotes this exact source tensor. Its vector derivatives in the scalar formula are full covariant derivatives of this tensor. The geometric composites and their derivatives retain these exact covariant definitions.

### 3.3 Generator actions, with the SU(2) sign derived

The needed source actions are C24 (A.1), S23 (2.8), (2.15). For a lower spinor $`U_\beta`$, a lower vector $`U_a`$ and a doublet $`U^i`$,

```math
\begin{aligned}
M_{ab}U_\beta&=(\Sigma_{ab})_\beta{}^\gamma U_\gamma,\qquad M_{ab}U_c=\eta_{ca}U_b-\eta_{cb}U_a,\\
J^{kl}U^i&=\tfrac12(\varepsilon^{ik}U^l+\varepsilon^{il}U^k),\\
J_{kl}U^i&=\varepsilon_{km}\varepsilon_{ln}J^{mn}U^i
=-\tfrac12(\delta_k{}^i\varepsilon_{ln}+\delta_l{}^i\varepsilon_{kn})U^n.
\end{aligned}
\tag{S4-I-07}
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
\tag{S4-I-08}
```

The last identity applies to each elementary vector/Weyl descendant in this calculation, not to its vector derivatives. The weights are $`w(W)=w(W_{ab})=1`$, $`w(\lambda)=w(X_\alpha)=w(W_{\alpha\beta\gamma})=3/2`$, $`w(X^{ij})=w(F_{ab})=w(X_{ab}^{ij})=w(Y)=2`$; $`w(\nabla_a)=1`$, $`w(\nabla_\alpha^i)=1/2`$.

### 3.4 Higher descendants and the commutator on a derivative

The remaining elementary S actions follow from S23 (2.8); the full scalar descent uses them when differentiating the spinor's Weyl descendants:

```math
\begin{aligned}
S_{\gamma k}W_{\alpha\beta\delta}{}^i&=2\delta_k{}^i(\varepsilon_{\gamma\alpha}W_{\beta\delta}+\varepsilon_{\gamma\beta}W_{\delta\alpha}+\varepsilon_{\gamma\delta}W_{\alpha\beta}),\\
S_{\gamma k}Y&=8iX_{\gamma k},\qquad
S_{\gamma k}W_{\alpha\beta\delta\rho}=24\varepsilon_{\gamma(\alpha}W_{\beta\delta\rho)k},\\
S_{\gamma k}X_{\alpha\beta}^{ij}
&=-2\delta_k{}^iW_{\gamma\alpha\beta}{}^j-2\delta_k{}^jW_{\gamma\alpha\beta}{}^i
+\delta_k{}^i(\varepsilon_{\gamma\alpha}X_\beta^j+\varepsilon_{\gamma\beta}X_\alpha^j)
+\delta_k{}^j(\varepsilon_{\gamma\alpha}X_\beta^i+\varepsilon_{\gamma\beta}X_\alpha^i).
\end{aligned}
\tag{S4-04}
```

All these elementary fields are K-primary. Their vector derivatives are not. For any homogeneous tensor $`U`$ of weight $`w_U`$, C24 (A.1) gives

```math
\begin{aligned}
K_c\nabla_aU&=\nabla_a(K_cU)+2\eta_{ca}w_UU+2M_{ca}U,\\
K_c\nabla_a\nabla_bU
&=\nabla_a\nabla_b(K_cU)+2w_U\eta_{cb}\nabla_aU+2\nabla_a(M_{cb}U)
+2(w_U+1)\eta_{ca}\nabla_bU+2M_{ca}(\nabla_bU),\\
M_{cd}(\nabla_aU)&=\eta_{ac}\nabla_dU-\eta_{ad}\nabla_cU+\nabla_a(M_{cd}U),\\
S_{\gamma k}\nabla_aU
&=\nabla_a(S_{\gamma k}U)+i(\Gamma_a)_\gamma{}^\delta\varepsilon_{kl}\nabla_\delta^lU
-\frac14W_a{}^b(\Gamma_b)_\gamma{}^\delta S_{\delta k}U\\
&\quad+\frac i8(\Gamma_a)_\gamma{}^\delta(\Gamma^b)_\delta{}^\rho X_{\rho k}K_bU
-\frac i4W_{ab\gamma k}K^bU.
\end{aligned}
\tag{S4-05}
```

The last two coefficients include the Jacobi-required factors of $`i`$ missing from literal C24 (A.1l); see [the source-algebra certificate](../../../../../../../references/source_evidence/log/results/gauged_full_fermionic_log/sources/certification_20260925/curved/jacobi-SDD-checks.json). The literal source is preserved in the convention ledger. The last two terms cannot be removed when $`U`$ already contains a vector derivative. In the second line the weight has increased to $`w_U+1`$ on $`\nabla_bU`$. These facts are needed, for example, for the two descendants of the $`\Box X^{ij}`$ and $`\lambda\Box\lambda`$ inputs.

Reversing the vector–spinor commutator sign in the convention ledger gives the explicit rule

```math
\begin{aligned}
\nabla_\zeta^t\nabla_aU
={}&\nabla_a\nabla_\zeta^tU+\mathcal T_{a\zeta}{}^\beta\nabla_\beta^tU
+\frac12\mathcal R(M)_{a\zeta}{}^{tbc}M_{bc}U
+w_U\mathcal R(\mathbb D)_{a\zeta}{}^tU\\
&+\mathcal R(J)_{a\zeta}{}^{tkl}J_{kl}U
+\mathcal R(S)_{a\zeta}{}^{t\beta k}S_{\beta k}U
+\mathcal R(K)_{a\zeta}{}^{tb}K_bU,\\
\nabla_\zeta^t\Box U
={}&\Box\nabla_\zeta^tU+\nabla^a([\nabla_\zeta^t,\nabla_a]U)
+[\nabla_\zeta^t,\nabla^a]\nabla_aU.
\end{aligned}
\tag{S4-06}
```

For more ordered vector derivatives this equation is applied to the outermost one, then the next one. The generator acts on **all** tensor indices, including derivative indices. Its actions are those displayed in (S4-I-07), (S4-I-08), (S4-04), and (S4-05). There is no replacement of a covariant derivative by a partial derivative.

### 3.5 Differentiating the geometric tensors

The spinor contains $`\mathcal T`$ and $`\mathcal R`$. Their derivatives must be included. For example, differentiating their actual defining fields gives

```math
\begin{aligned}
\nabla_\zeta^t\mathcal T_{a\eta}{}^\beta
={}&\frac34(\Gamma_a)_\eta{}^\gamma\varepsilon^{\beta\delta}
\big(W_{\gamma\delta\zeta}{}^t+\tfrac12\varepsilon_{\zeta\gamma}X_\delta^t+\tfrac12\varepsilon_{\zeta\delta}X_\gamma^t\big)\\
&-\frac14\varepsilon^{\gamma\delta}
\big(W_{\eta\delta\zeta}{}^t+\tfrac12\varepsilon_{\zeta\eta}X_\delta^t+\tfrac12\varepsilon_{\zeta\delta}X_\eta^t\big)(\Gamma_a)_\gamma{}^\beta,\\
\nabla_\zeta^t\mathcal R(\mathbb D)_{a\eta}{}^r
={}&-\frac14(\Gamma_a)_\eta{}^\beta\Big[
X_{\zeta\beta}^{tr}+\frac i8\varepsilon^{tr}\varepsilon_{\zeta\beta}Y
-\frac{3i}{2}\varepsilon^{tr}(\Gamma^b)_\zeta{}^\gamma\nabla_bW_{\beta\gamma}
-2i\varepsilon^{tr}W_\zeta{}^\gamma W_{\beta\gamma}\\
&\hspace{33mm}+\frac i2\varepsilon^{tr}\varepsilon_{\zeta\beta}W^{\gamma\delta}W_{\gamma\delta}
-\frac i2\varepsilon^{tr}(\Gamma^b)_\beta{}^\gamma\nabla_bW_{\zeta\gamma}\Big].
\end{aligned}
\tag{S4-07}
```

The following evaluated rows supply the full substitutions for all six geometric tensors, including the longer Lorentz, S and K curvatures. Their free indices are the ones on the left. A prime, unnamed response tensor, or unevaluated spinor derivative is not introduced.

#### Spinor derivative of torsion

```math
\begin{aligned}
\nabla_\eta^r \mathcal T{}_{a \beta}{}^{\gamma}={}&\frac{3}{4}(\Gamma{}_{a}){}_{\beta}{}^{\alpha}W{}_{\eta \alpha}{}^{\gamma r} +\frac{3}{8}(\Gamma{}_{a}){}_{\beta \eta}X{}^{\gamma r}\\
&+\frac{3}{8}(\Gamma{}_{a}){}_{\beta}{}^{\alpha}\varepsilon{}^{\gamma \delta}\varepsilon{}_{\eta \delta}X{}_{\alpha}{}^{r} -\frac{1}{4}W{}_{\eta \beta}{}^{\alpha r}(\Gamma{}_{a}){}_{\alpha}{}^{\gamma}\\
&-\frac{1}{8}\varepsilon{}_{\eta \beta}X{}^{\alpha r}(\Gamma{}_{a}){}_{\alpha}{}^{\gamma} +\frac{1}{8}X{}_{\beta}{}^{r}(\Gamma{}_{a}){}_{\eta}{}^{\gamma}
\end{aligned}
\tag{S4-D-T}
```

#### Spinor derivative of dilatation curvature

```math
\begin{aligned}
\nabla_\eta^r \mathcal R(\mathbb D){}_{a \beta}{}^{i}={}&-\frac{1}{4}(\Gamma{}_{a}){}_{\beta}{}^{\alpha}X{}_{\eta \alpha}{}^{r i} -\frac{i}{32}(\Gamma{}_{a}){}_{\beta \eta}\varepsilon{}^{r i}Y\\
&+\frac{3i}{8}(\Gamma{}_{a}){}_{\beta}{}^{\alpha}\varepsilon{}^{r i}(\Gamma{}^{d}){}_{\eta}{}^{\delta}\big(\nabla_{d}W{}_{\alpha \delta}\big) +\frac{i}{2}(\Gamma{}_{a}){}_{\beta}{}^{\alpha}\varepsilon{}^{r i}W{}_{\eta}{}^{\delta}W{}_{\alpha \delta}\\
&-\frac{i}{8}(\Gamma{}_{a}){}_{\beta \eta}\varepsilon{}^{r i}W{}^{\alpha \delta}W{}_{\alpha \delta} +\frac{i}{8}(\Gamma{}_{a}){}_{\beta}{}^{\alpha}\varepsilon{}^{r i}(\Gamma{}^{d}){}_{\alpha}{}^{\delta}\big(\nabla_{d}W{}_{\eta \delta}\big)
\end{aligned}
\tag{S4-D-RD}
```

#### Spinor derivative of SU(2) curvature

```math
\begin{aligned}
\nabla_\eta^r \mathcal R(J){}_{a \beta}{}^{i j k}={}&-\frac{3}{8}(\Gamma{}_{a}){}_{\beta}{}^{\alpha}\varepsilon{}^{i j}X{}_{\eta \alpha}{}^{r k} -\frac{3i}{64}(\Gamma{}_{a}){}_{\beta \eta}\varepsilon{}^{i j}\varepsilon{}^{r k}Y\\
&+\frac{9i}{16}(\Gamma{}_{a}){}_{\beta}{}^{\alpha}\varepsilon{}^{i j}\varepsilon{}^{r k}(\Gamma{}^{d}){}_{\eta}{}^{\delta}\big(\nabla_{d}W{}_{\alpha \delta}\big) +\frac{3i}{4}(\Gamma{}_{a}){}_{\beta}{}^{\alpha}\varepsilon{}^{i j}\varepsilon{}^{r k}W{}_{\eta}{}^{\delta}W{}_{\alpha \delta}\\
&-\frac{3i}{16}(\Gamma{}_{a}){}_{\beta \eta}\varepsilon{}^{i j}\varepsilon{}^{r k}W{}^{\alpha \delta}W{}_{\alpha \delta} +\frac{3i}{16}(\Gamma{}_{a}){}_{\beta}{}^{\alpha}\varepsilon{}^{i j}\varepsilon{}^{r k}(\Gamma{}^{d}){}_{\alpha}{}^{\delta}\big(\nabla_{d}W{}_{\eta \delta}\big)\\
&-\frac{3}{8}(\Gamma{}_{a}){}_{\beta}{}^{\alpha}\varepsilon{}^{i k}X{}_{\eta \alpha}{}^{r j} -\frac{3i}{64}(\Gamma{}_{a}){}_{\beta \eta}\varepsilon{}^{i k}\varepsilon{}^{r j}Y\\
&+\frac{9i}{16}(\Gamma{}_{a}){}_{\beta}{}^{\alpha}\varepsilon{}^{i k}\varepsilon{}^{r j}(\Gamma{}^{d}){}_{\eta}{}^{\delta}\big(\nabla_{d}W{}_{\alpha \delta}\big) +\frac{3i}{4}(\Gamma{}_{a}){}_{\beta}{}^{\alpha}\varepsilon{}^{i k}\varepsilon{}^{r j}W{}_{\eta}{}^{\delta}W{}_{\alpha \delta}\\
&-\frac{3i}{16}(\Gamma{}_{a}){}_{\beta \eta}\varepsilon{}^{i k}\varepsilon{}^{r j}W{}^{\alpha \delta}W{}_{\alpha \delta} +\frac{3i}{16}(\Gamma{}_{a}){}_{\beta}{}^{\alpha}\varepsilon{}^{i k}\varepsilon{}^{r j}(\Gamma{}^{d}){}_{\alpha}{}^{\delta}\big(\nabla_{d}W{}_{\eta \delta}\big)
\end{aligned}
\tag{S4-D-RJ}
```

#### Spinor derivative of Lorentz curvature

```math
\begin{aligned}
\nabla_\eta^r \mathcal R(M){}_{a \beta}{}^{i b c}={}&\frac{1}{2}(\Gamma{}_{a}){}_{\beta}{}^{\alpha}(\Sigma{}^{b c}){}^{\delta \rho}\varepsilon{}^{r i}W{}_{\eta \delta \rho \alpha} +\frac{i}{2}(\Gamma{}_{a}){}_{\beta}{}^{\alpha}(\Sigma{}^{b c}){}^{\delta \rho}\varepsilon{}^{r i}(\Gamma{}^{d}){}_{\eta \delta}\big(\nabla_{d}W{}_{\rho \alpha}\big)\\
&+\frac{1}{2}(\Gamma{}_{a}){}_{\beta}{}^{\alpha}(\Sigma{}^{b c}){}_{\eta}{}^{\delta}X{}_{\delta \alpha}{}^{r i} +\frac{i}{2}(\Gamma{}_{a}){}_{\beta}{}^{\alpha}(\Sigma{}^{b c}){}^{\delta \rho}\varepsilon{}^{r i}(\Gamma{}^{d}){}_{\eta \rho}\big(\nabla_{d}W{}_{\delta \alpha}\big)\\
&+\frac{1}{2}(\Gamma{}_{a}){}_{\beta}{}^{\alpha}(\Sigma{}^{b c}){}^{\delta}{}_{\eta}X{}_{\delta \alpha}{}^{r i} +\frac{i}{2}(\Gamma{}_{a}){}_{\beta}{}^{\alpha}(\Sigma{}^{b c}){}^{\delta \rho}\varepsilon{}^{r i}(\Gamma{}^{d}){}_{\eta \alpha}\big(\nabla_{d}W{}_{\delta \rho}\big)\\
&+\frac{1}{2}(\Gamma{}_{a}){}_{\beta \eta}(\Sigma{}^{b c}){}^{\alpha \delta}X{}_{\alpha \delta}{}^{r i} +\frac{i}{4}(\Gamma{}_{a}){}_{\beta}{}^{\alpha}(\Sigma{}^{b c}){}_{\eta}{}^{\delta}\varepsilon{}^{r i}(\Gamma{}^{d}){}_{\delta}{}^{\rho}\big(\nabla_{d}W{}_{\alpha \rho}\big)\\
&+\frac{i}{4}(\Gamma{}_{a}){}_{\beta}{}^{\alpha}(\Sigma{}^{b c}){}_{\eta}{}^{\delta}\varepsilon{}^{r i}(\Gamma{}^{d}){}_{\alpha}{}^{\rho}\big(\nabla_{d}W{}_{\delta \rho}\big) +\frac{i}{4}(\Gamma{}_{a}){}_{\beta}{}^{\alpha}(\Sigma{}^{b c}){}^{\delta}{}_{\eta}\varepsilon{}^{r i}(\Gamma{}^{d}){}_{\delta}{}^{\rho}\big(\nabla_{d}W{}_{\alpha \rho}\big)\\
&+\frac{i}{4}(\Gamma{}_{a}){}_{\beta}{}^{\alpha}(\Sigma{}^{b c}){}^{\delta}{}_{\eta}\varepsilon{}^{r i}(\Gamma{}^{d}){}_{\alpha}{}^{\rho}\big(\nabla_{d}W{}_{\delta \rho}\big) +\frac{i}{4}(\Gamma{}_{a}){}_{\beta \eta}(\Sigma{}^{b c}){}^{\alpha \delta}\varepsilon{}^{r i}(\Gamma{}^{d}){}_{\alpha}{}^{\rho}\big(\nabla_{d}W{}_{\delta \rho}\big)\\
&+\frac{i}{4}(\Gamma{}_{a}){}_{\beta \eta}(\Sigma{}^{b c}){}^{\alpha \delta}\varepsilon{}^{r i}(\Gamma{}^{d}){}_{\delta}{}^{\rho}\big(\nabla_{d}W{}_{\alpha \rho}\big) +\frac{1}{8}\varepsilon{}_{a}{}^{b c d e}(\Sigma{}_{d e}){}^{\alpha \delta}\varepsilon{}^{r i}W{}_{\eta \alpha \delta \beta}\\
&+\frac{i}{8}\varepsilon{}_{a}{}^{b c d e}(\Sigma{}_{d e}){}^{\alpha \delta}\varepsilon{}^{r i}(\Gamma{}^{f}){}_{\eta \alpha}\big(\nabla_{f}W{}_{\delta \beta}\big) +\frac{1}{8}\varepsilon{}_{a}{}^{b c d e}(\Sigma{}_{d e}){}_{\eta}{}^{\alpha}X{}_{\alpha \beta}{}^{r i}\\
&+\frac{i}{8}\varepsilon{}_{a}{}^{b c d e}(\Sigma{}_{d e}){}^{\alpha \delta}\varepsilon{}^{r i}(\Gamma{}^{f}){}_{\eta \delta}\big(\nabla_{f}W{}_{\alpha \beta}\big) +\frac{1}{8}\varepsilon{}_{a}{}^{b c d e}(\Sigma{}_{d e}){}^{\alpha}{}_{\eta}X{}_{\alpha \beta}{}^{r i}\\
&+\frac{i}{8}\varepsilon{}_{a}{}^{b c d e}(\Sigma{}_{d e}){}^{\alpha \delta}\varepsilon{}^{r i}(\Gamma{}^{f}){}_{\eta \beta}\big(\nabla_{f}W{}_{\alpha \delta}\big) +\frac{1}{8}\varepsilon{}_{a}{}^{b c d e}(\Sigma{}_{d e}){}^{\alpha \delta}\varepsilon{}_{\eta \beta}X{}_{\alpha \delta}{}^{r i}\\
&+\frac{i}{16}\varepsilon{}_{a}{}^{b c d e}(\Sigma{}_{d e}){}_{\eta}{}^{\alpha}\varepsilon{}^{r i}(\Gamma{}^{f}){}_{\alpha}{}^{\delta}\big(\nabla_{f}W{}_{\beta \delta}\big) +\frac{i}{16}\varepsilon{}_{a}{}^{b c d e}(\Sigma{}_{d e}){}_{\eta}{}^{\alpha}\varepsilon{}^{r i}(\Gamma{}^{f}){}_{\beta}{}^{\delta}\big(\nabla_{f}W{}_{\alpha \delta}\big)\\
&+\frac{i}{16}\varepsilon{}_{a}{}^{b c d e}(\Sigma{}_{d e}){}^{\alpha}{}_{\eta}\varepsilon{}^{r i}(\Gamma{}^{f}){}_{\alpha}{}^{\delta}\big(\nabla_{f}W{}_{\beta \delta}\big) +\frac{i}{16}\varepsilon{}_{a}{}^{b c d e}(\Sigma{}_{d e}){}^{\alpha}{}_{\eta}\varepsilon{}^{r i}(\Gamma{}^{f}){}_{\beta}{}^{\delta}\big(\nabla_{f}W{}_{\alpha \delta}\big)\\
&+\frac{i}{16}\varepsilon{}_{a}{}^{b c d e}(\Sigma{}_{d e}){}^{\alpha \delta}\varepsilon{}^{r i}\varepsilon{}_{\eta \beta}(\Gamma{}^{f}){}_{\alpha}{}^{\rho}\big(\nabla_{f}W{}_{\delta \rho}\big) +\frac{i}{16}\varepsilon{}_{a}{}^{b c d e}(\Sigma{}_{d e}){}^{\alpha \delta}\varepsilon{}^{r i}\varepsilon{}_{\eta \beta}(\Gamma{}^{f}){}_{\delta}{}^{\rho}\big(\nabla_{f}W{}_{\alpha \rho}\big)\\
&+\frac{1}{4}\delta{}_{a}{}^{b}(\Gamma{}^{c}){}_{\beta}{}^{\alpha}X{}_{\eta \alpha}{}^{r i} +\frac{i}{32}\delta{}_{a}{}^{b}(\Gamma{}^{c}){}_{\beta \eta}\varepsilon{}^{r i}Y\\
&-\frac{3i}{8}\delta{}_{a}{}^{b}(\Gamma{}^{c}){}_{\beta}{}^{\alpha}\varepsilon{}^{r i}(\Gamma{}^{d}){}_{\eta}{}^{\delta}\big(\nabla_{d}W{}_{\alpha \delta}\big) -\frac{i}{2}\delta{}_{a}{}^{b}(\Gamma{}^{c}){}_{\beta}{}^{\alpha}\varepsilon{}^{r i}W{}_{\eta}{}^{\delta}W{}_{\alpha \delta}\\
&+\frac{i}{8}\delta{}_{a}{}^{b}(\Gamma{}^{c}){}_{\beta \eta}\varepsilon{}^{r i}W{}^{\alpha \delta}W{}_{\alpha \delta} -\frac{i}{8}\delta{}_{a}{}^{b}(\Gamma{}^{c}){}_{\beta}{}^{\alpha}\varepsilon{}^{r i}(\Gamma{}^{d}){}_{\alpha}{}^{\delta}\big(\nabla_{d}W{}_{\eta \delta}\big)\\
&-\frac{1}{4}\delta{}_{a}{}^{c}(\Gamma{}^{b}){}_{\beta}{}^{\alpha}X{}_{\eta \alpha}{}^{r i} -\frac{i}{32}\delta{}_{a}{}^{c}(\Gamma{}^{b}){}_{\beta \eta}\varepsilon{}^{r i}Y\\
&+\frac{3i}{8}\delta{}_{a}{}^{c}(\Gamma{}^{b}){}_{\beta}{}^{\alpha}\varepsilon{}^{r i}(\Gamma{}^{d}){}_{\eta}{}^{\delta}\big(\nabla_{d}W{}_{\alpha \delta}\big) +\frac{i}{2}\delta{}_{a}{}^{c}(\Gamma{}^{b}){}_{\beta}{}^{\alpha}\varepsilon{}^{r i}W{}_{\eta}{}^{\delta}W{}_{\alpha \delta}\\
&-\frac{i}{8}\delta{}_{a}{}^{c}(\Gamma{}^{b}){}_{\beta \eta}\varepsilon{}^{r i}W{}^{\alpha \delta}W{}_{\alpha \delta} +\frac{i}{8}\delta{}_{a}{}^{c}(\Gamma{}^{b}){}_{\beta}{}^{\alpha}\varepsilon{}^{r i}(\Gamma{}^{d}){}_{\alpha}{}^{\delta}\big(\nabla_{d}W{}_{\eta \delta}\big)
\end{aligned}
\tag{S4-D-RM}
```

#### Spinor derivative of S curvature

```math
\begin{aligned}
\nabla_\eta^r \mathcal R(S){}_{a \beta}{}^{i \gamma j}={}&-\frac{i}{32}(\Sigma{}_{d e}){}^{\alpha \delta}\varepsilon{}^{r i}W{}_{\eta \rho}W{}_{\alpha \delta}{}^{\rho j}(\Sigma{}^{d e}){}_{\beta}{}^{\sigma}(\Gamma{}_{a}){}_{\sigma}{}^{\gamma} -\frac{3i}{64}(\Sigma{}_{d e}){}^{\alpha \delta}\varepsilon{}^{r i}W{}_{\alpha \delta}X{}_{\eta}{}^{j}(\Sigma{}^{d e}){}_{\beta}{}^{\rho}(\Gamma{}_{a}){}_{\rho}{}^{\gamma}\\
&+\frac{i}{16}(\Sigma{}_{d e}){}^{\alpha \delta}\varepsilon{}^{r i}(\Gamma{}^{f}){}_{\eta}{}^{\rho}\big(\nabla_{f}W{}_{\alpha \delta \rho}{}^{j}\big)(\Sigma{}^{d e}){}_{\beta}{}^{\sigma}(\Gamma{}_{a}){}_{\sigma}{}^{\gamma} -\frac{3i}{64}(\Sigma{}_{d e}){}^{\alpha \delta}\varepsilon{}^{r i}W{}_{\alpha}{}^{\rho}W{}_{\delta \eta \rho}{}^{j}(\Sigma{}^{d e}){}_{\beta}{}^{\sigma}(\Gamma{}_{a}){}_{\sigma}{}^{\gamma}\\
&-\frac{i}{64}(\Sigma{}_{d e}){}_{\eta}{}^{\alpha}\varepsilon{}^{r i}W{}^{\delta \rho}W{}_{\alpha \delta \rho}{}^{j}(\Sigma{}^{d e}){}_{\beta}{}^{\sigma}(\Gamma{}_{a}){}_{\sigma}{}^{\gamma} +\frac{i}{128}(\Sigma{}_{d e}){}^{\alpha \delta}\varepsilon{}^{r i}W{}_{\eta \alpha}X{}_{\delta}{}^{j}(\Sigma{}^{d e}){}_{\beta}{}^{\rho}(\Gamma{}_{a}){}_{\rho}{}^{\gamma}\\
&+\frac{3i}{128}(\Sigma{}_{d e}){}_{\eta}{}^{\alpha}\varepsilon{}^{r i}W{}_{\alpha \delta}X{}^{\delta j}(\Sigma{}^{d e}){}_{\beta}{}^{\rho}(\Gamma{}_{a}){}_{\rho}{}^{\gamma} +\frac{i}{32}(\Sigma{}_{d e}){}^{\alpha \delta}\varepsilon{}^{r i}(\Gamma{}^{f}){}_{\alpha}{}^{\rho}\big(\nabla_{f}W{}_{\delta \eta \rho}{}^{j}\big)(\Sigma{}^{d e}){}_{\beta}{}^{\sigma}(\Gamma{}_{a}){}_{\sigma}{}^{\gamma}\\
&-\frac{i}{64}(\Sigma{}_{d e}){}^{\alpha \delta}\varepsilon{}^{r i}(\Gamma{}^{f}){}_{\eta \alpha}\big(\nabla_{f}X{}_{\delta}{}^{j}\big)(\Sigma{}^{d e}){}_{\beta}{}^{\rho}(\Gamma{}_{a}){}_{\rho}{}^{\gamma} +\frac{i}{64}(\Sigma{}_{d e}){}_{\eta}{}^{\alpha}\varepsilon{}^{r i}(\Gamma{}^{f}){}_{\alpha \delta}\big(\nabla_{f}X{}^{\delta j}\big)(\Sigma{}^{d e}){}_{\beta}{}^{\rho}(\Gamma{}_{a}){}_{\rho}{}^{\gamma}\\
&-\frac{3i}{64}(\Sigma{}_{d e}){}^{\alpha \delta}\varepsilon{}^{r i}W{}_{\delta}{}^{\rho}W{}_{\alpha \eta \rho}{}^{j}(\Sigma{}^{d e}){}_{\beta}{}^{\sigma}(\Gamma{}_{a}){}_{\sigma}{}^{\gamma} -\frac{i}{64}(\Sigma{}_{d e}){}^{\alpha}{}_{\eta}\varepsilon{}^{r i}W{}^{\delta \rho}W{}_{\alpha \delta \rho}{}^{j}(\Sigma{}^{d e}){}_{\beta}{}^{\sigma}(\Gamma{}_{a}){}_{\sigma}{}^{\gamma}\\
&+\frac{i}{128}(\Sigma{}_{d e}){}^{\alpha \delta}\varepsilon{}^{r i}W{}_{\eta \delta}X{}_{\alpha}{}^{j}(\Sigma{}^{d e}){}_{\beta}{}^{\rho}(\Gamma{}_{a}){}_{\rho}{}^{\gamma} +\frac{3i}{128}(\Sigma{}_{d e}){}^{\alpha}{}_{\eta}\varepsilon{}^{r i}W{}_{\alpha \delta}X{}^{\delta j}(\Sigma{}^{d e}){}_{\beta}{}^{\rho}(\Gamma{}_{a}){}_{\rho}{}^{\gamma}\\
&+\frac{i}{32}(\Sigma{}_{d e}){}^{\alpha \delta}\varepsilon{}^{r i}(\Gamma{}^{f}){}_{\delta}{}^{\rho}\big(\nabla_{f}W{}_{\alpha \eta \rho}{}^{j}\big)(\Sigma{}^{d e}){}_{\beta}{}^{\sigma}(\Gamma{}_{a}){}_{\sigma}{}^{\gamma} -\frac{i}{64}(\Sigma{}_{d e}){}^{\alpha \delta}\varepsilon{}^{r i}(\Gamma{}^{f}){}_{\eta \delta}\big(\nabla_{f}X{}_{\alpha}{}^{j}\big)(\Sigma{}^{d e}){}_{\beta}{}^{\rho}(\Gamma{}_{a}){}_{\rho}{}^{\gamma}\\
&+\frac{i}{64}(\Sigma{}_{d e}){}^{\alpha}{}_{\eta}\varepsilon{}^{r i}(\Gamma{}^{f}){}_{\alpha \delta}\big(\nabla_{f}X{}^{\delta j}\big)(\Sigma{}^{d e}){}_{\beta}{}^{\rho}(\Gamma{}_{a}){}_{\rho}{}^{\gamma} -\frac{i}{32}(\Sigma{}_{d e}){}^{\alpha \delta}\varepsilon{}^{r j}W{}_{\eta \rho}W{}_{\alpha \delta}{}^{\rho i}(\Sigma{}^{d e}){}_{\beta}{}^{\sigma}(\Gamma{}_{a}){}_{\sigma}{}^{\gamma}\\
&-\frac{3i}{64}(\Sigma{}_{d e}){}^{\alpha \delta}\varepsilon{}^{r j}W{}_{\alpha \delta}X{}_{\eta}{}^{i}(\Sigma{}^{d e}){}_{\beta}{}^{\rho}(\Gamma{}_{a}){}_{\rho}{}^{\gamma} +\frac{i}{16}(\Sigma{}_{d e}){}^{\alpha \delta}\varepsilon{}^{r j}(\Gamma{}^{f}){}_{\eta}{}^{\rho}\big(\nabla_{f}W{}_{\alpha \delta \rho}{}^{i}\big)(\Sigma{}^{d e}){}_{\beta}{}^{\sigma}(\Gamma{}_{a}){}_{\sigma}{}^{\gamma}\\
&-\frac{3i}{64}(\Sigma{}_{d e}){}^{\alpha \delta}\varepsilon{}^{r j}W{}_{\alpha}{}^{\rho}W{}_{\delta \eta \rho}{}^{i}(\Sigma{}^{d e}){}_{\beta}{}^{\sigma}(\Gamma{}_{a}){}_{\sigma}{}^{\gamma} -\frac{i}{64}(\Sigma{}_{d e}){}_{\eta}{}^{\alpha}\varepsilon{}^{r j}W{}^{\delta \rho}W{}_{\alpha \delta \rho}{}^{i}(\Sigma{}^{d e}){}_{\beta}{}^{\sigma}(\Gamma{}_{a}){}_{\sigma}{}^{\gamma}\\
&+\frac{i}{128}(\Sigma{}_{d e}){}^{\alpha \delta}\varepsilon{}^{r j}W{}_{\eta \alpha}X{}_{\delta}{}^{i}(\Sigma{}^{d e}){}_{\beta}{}^{\rho}(\Gamma{}_{a}){}_{\rho}{}^{\gamma} +\frac{3i}{128}(\Sigma{}_{d e}){}_{\eta}{}^{\alpha}\varepsilon{}^{r j}W{}_{\alpha \delta}X{}^{\delta i}(\Sigma{}^{d e}){}_{\beta}{}^{\rho}(\Gamma{}_{a}){}_{\rho}{}^{\gamma}\\
&+\frac{i}{32}(\Sigma{}_{d e}){}^{\alpha \delta}\varepsilon{}^{r j}(\Gamma{}^{f}){}_{\alpha}{}^{\rho}\big(\nabla_{f}W{}_{\delta \eta \rho}{}^{i}\big)(\Sigma{}^{d e}){}_{\beta}{}^{\sigma}(\Gamma{}_{a}){}_{\sigma}{}^{\gamma} -\frac{i}{64}(\Sigma{}_{d e}){}^{\alpha \delta}\varepsilon{}^{r j}(\Gamma{}^{f}){}_{\eta \alpha}\big(\nabla_{f}X{}_{\delta}{}^{i}\big)(\Sigma{}^{d e}){}_{\beta}{}^{\rho}(\Gamma{}_{a}){}_{\rho}{}^{\gamma}\\
&+\frac{i}{64}(\Sigma{}_{d e}){}_{\eta}{}^{\alpha}\varepsilon{}^{r j}(\Gamma{}^{f}){}_{\alpha \delta}\big(\nabla_{f}X{}^{\delta i}\big)(\Sigma{}^{d e}){}_{\beta}{}^{\rho}(\Gamma{}_{a}){}_{\rho}{}^{\gamma} -\frac{3i}{64}(\Sigma{}_{d e}){}^{\alpha \delta}\varepsilon{}^{r j}W{}_{\delta}{}^{\rho}W{}_{\alpha \eta \rho}{}^{i}(\Sigma{}^{d e}){}_{\beta}{}^{\sigma}(\Gamma{}_{a}){}_{\sigma}{}^{\gamma}\\
&-\frac{i}{64}(\Sigma{}_{d e}){}^{\alpha}{}_{\eta}\varepsilon{}^{r j}W{}^{\delta \rho}W{}_{\alpha \delta \rho}{}^{i}(\Sigma{}^{d e}){}_{\beta}{}^{\sigma}(\Gamma{}_{a}){}_{\sigma}{}^{\gamma} +\frac{i}{128}(\Sigma{}_{d e}){}^{\alpha \delta}\varepsilon{}^{r j}W{}_{\eta \delta}X{}_{\alpha}{}^{i}(\Sigma{}^{d e}){}_{\beta}{}^{\rho}(\Gamma{}_{a}){}_{\rho}{}^{\gamma}\\
&+\frac{3i}{128}(\Sigma{}_{d e}){}^{\alpha}{}_{\eta}\varepsilon{}^{r j}W{}_{\alpha \delta}X{}^{\delta i}(\Sigma{}^{d e}){}_{\beta}{}^{\rho}(\Gamma{}_{a}){}_{\rho}{}^{\gamma} +\frac{i}{32}(\Sigma{}_{d e}){}^{\alpha \delta}\varepsilon{}^{r j}(\Gamma{}^{f}){}_{\delta}{}^{\rho}\big(\nabla_{f}W{}_{\alpha \eta \rho}{}^{i}\big)(\Sigma{}^{d e}){}_{\beta}{}^{\sigma}(\Gamma{}_{a}){}_{\sigma}{}^{\gamma}\\
&-\frac{i}{64}(\Sigma{}_{d e}){}^{\alpha \delta}\varepsilon{}^{r j}(\Gamma{}^{f}){}_{\eta \delta}\big(\nabla_{f}X{}_{\alpha}{}^{i}\big)(\Sigma{}^{d e}){}_{\beta}{}^{\rho}(\Gamma{}_{a}){}_{\rho}{}^{\gamma} +\frac{i}{64}(\Sigma{}_{d e}){}^{\alpha}{}_{\eta}\varepsilon{}^{r j}(\Gamma{}^{f}){}_{\alpha \delta}\big(\nabla_{f}X{}^{\delta i}\big)(\Sigma{}^{d e}){}_{\beta}{}^{\rho}(\Gamma{}_{a}){}_{\rho}{}^{\gamma}\\
&+\frac{i}{16}(\Sigma{}_{d e}){}^{\alpha \delta}\varepsilon{}^{r i}W{}_{\eta \rho}W{}_{\alpha \delta}{}^{\rho j}(\Gamma{}_{a}){}_{\beta}{}^{\sigma}(\Sigma{}^{d e}){}_{\sigma}{}^{\gamma} +\frac{3i}{32}(\Sigma{}_{d e}){}^{\alpha \delta}\varepsilon{}^{r i}W{}_{\alpha \delta}X{}_{\eta}{}^{j}(\Gamma{}_{a}){}_{\beta}{}^{\rho}(\Sigma{}^{d e}){}_{\rho}{}^{\gamma}\\
&-\frac{i}{8}(\Sigma{}_{d e}){}^{\alpha \delta}\varepsilon{}^{r i}(\Gamma{}^{f}){}_{\eta}{}^{\rho}\big(\nabla_{f}W{}_{\alpha \delta \rho}{}^{j}\big)(\Gamma{}_{a}){}_{\beta}{}^{\sigma}(\Sigma{}^{d e}){}_{\sigma}{}^{\gamma} +\frac{3i}{32}(\Sigma{}_{d e}){}^{\alpha \delta}\varepsilon{}^{r i}W{}_{\alpha}{}^{\rho}W{}_{\delta \eta \rho}{}^{j}(\Gamma{}_{a}){}_{\beta}{}^{\sigma}(\Sigma{}^{d e}){}_{\sigma}{}^{\gamma}\\
&+\frac{i}{32}(\Sigma{}_{d e}){}_{\eta}{}^{\alpha}\varepsilon{}^{r i}W{}^{\delta \rho}W{}_{\alpha \delta \rho}{}^{j}(\Gamma{}_{a}){}_{\beta}{}^{\sigma}(\Sigma{}^{d e}){}_{\sigma}{}^{\gamma} -\frac{i}{64}(\Sigma{}_{d e}){}^{\alpha \delta}\varepsilon{}^{r i}W{}_{\eta \alpha}X{}_{\delta}{}^{j}(\Gamma{}_{a}){}_{\beta}{}^{\rho}(\Sigma{}^{d e}){}_{\rho}{}^{\gamma}\\
&-\frac{3i}{64}(\Sigma{}_{d e}){}_{\eta}{}^{\alpha}\varepsilon{}^{r i}W{}_{\alpha \delta}X{}^{\delta j}(\Gamma{}_{a}){}_{\beta}{}^{\rho}(\Sigma{}^{d e}){}_{\rho}{}^{\gamma} -\frac{i}{16}(\Sigma{}_{d e}){}^{\alpha \delta}\varepsilon{}^{r i}(\Gamma{}^{f}){}_{\alpha}{}^{\rho}\big(\nabla_{f}W{}_{\delta \eta \rho}{}^{j}\big)(\Gamma{}_{a}){}_{\beta}{}^{\sigma}(\Sigma{}^{d e}){}_{\sigma}{}^{\gamma}\\
&+\frac{i}{32}(\Sigma{}_{d e}){}^{\alpha \delta}\varepsilon{}^{r i}(\Gamma{}^{f}){}_{\eta \alpha}\big(\nabla_{f}X{}_{\delta}{}^{j}\big)(\Gamma{}_{a}){}_{\beta}{}^{\rho}(\Sigma{}^{d e}){}_{\rho}{}^{\gamma} -\frac{i}{32}(\Sigma{}_{d e}){}_{\eta}{}^{\alpha}\varepsilon{}^{r i}(\Gamma{}^{f}){}_{\alpha \delta}\big(\nabla_{f}X{}^{\delta j}\big)(\Gamma{}_{a}){}_{\beta}{}^{\rho}(\Sigma{}^{d e}){}_{\rho}{}^{\gamma}\\
&+\frac{3i}{32}(\Sigma{}_{d e}){}^{\alpha \delta}\varepsilon{}^{r i}W{}_{\delta}{}^{\rho}W{}_{\alpha \eta \rho}{}^{j}(\Gamma{}_{a}){}_{\beta}{}^{\sigma}(\Sigma{}^{d e}){}_{\sigma}{}^{\gamma} +\frac{i}{32}(\Sigma{}_{d e}){}^{\alpha}{}_{\eta}\varepsilon{}^{r i}W{}^{\delta \rho}W{}_{\alpha \delta \rho}{}^{j}(\Gamma{}_{a}){}_{\beta}{}^{\sigma}(\Sigma{}^{d e}){}_{\sigma}{}^{\gamma}\\
&-\frac{i}{64}(\Sigma{}_{d e}){}^{\alpha \delta}\varepsilon{}^{r i}W{}_{\eta \delta}X{}_{\alpha}{}^{j}(\Gamma{}_{a}){}_{\beta}{}^{\rho}(\Sigma{}^{d e}){}_{\rho}{}^{\gamma} -\frac{3i}{64}(\Sigma{}_{d e}){}^{\alpha}{}_{\eta}\varepsilon{}^{r i}W{}_{\alpha \delta}X{}^{\delta j}(\Gamma{}_{a}){}_{\beta}{}^{\rho}(\Sigma{}^{d e}){}_{\rho}{}^{\gamma}\\
&-\frac{i}{16}(\Sigma{}_{d e}){}^{\alpha \delta}\varepsilon{}^{r i}(\Gamma{}^{f}){}_{\delta}{}^{\rho}\big(\nabla_{f}W{}_{\alpha \eta \rho}{}^{j}\big)(\Gamma{}_{a}){}_{\beta}{}^{\sigma}(\Sigma{}^{d e}){}_{\sigma}{}^{\gamma} +\frac{i}{32}(\Sigma{}_{d e}){}^{\alpha \delta}\varepsilon{}^{r i}(\Gamma{}^{f}){}_{\eta \delta}\big(\nabla_{f}X{}_{\alpha}{}^{j}\big)(\Gamma{}_{a}){}_{\beta}{}^{\rho}(\Sigma{}^{d e}){}_{\rho}{}^{\gamma}\\
&-\frac{i}{32}(\Sigma{}_{d e}){}^{\alpha}{}_{\eta}\varepsilon{}^{r i}(\Gamma{}^{f}){}_{\alpha \delta}\big(\nabla_{f}X{}^{\delta j}\big)(\Gamma{}_{a}){}_{\beta}{}^{\rho}(\Sigma{}^{d e}){}_{\rho}{}^{\gamma} +\frac{i}{16}(\Sigma{}_{d e}){}^{\alpha \delta}\varepsilon{}^{r j}W{}_{\eta \rho}W{}_{\alpha \delta}{}^{\rho i}(\Gamma{}_{a}){}_{\beta}{}^{\sigma}(\Sigma{}^{d e}){}_{\sigma}{}^{\gamma}\\
&+\frac{3i}{32}(\Sigma{}_{d e}){}^{\alpha \delta}\varepsilon{}^{r j}W{}_{\alpha \delta}X{}_{\eta}{}^{i}(\Gamma{}_{a}){}_{\beta}{}^{\rho}(\Sigma{}^{d e}){}_{\rho}{}^{\gamma} -\frac{i}{8}(\Sigma{}_{d e}){}^{\alpha \delta}\varepsilon{}^{r j}(\Gamma{}^{f}){}_{\eta}{}^{\rho}\big(\nabla_{f}W{}_{\alpha \delta \rho}{}^{i}\big)(\Gamma{}_{a}){}_{\beta}{}^{\sigma}(\Sigma{}^{d e}){}_{\sigma}{}^{\gamma}\\
&+\frac{3i}{32}(\Sigma{}_{d e}){}^{\alpha \delta}\varepsilon{}^{r j}W{}_{\alpha}{}^{\rho}W{}_{\delta \eta \rho}{}^{i}(\Gamma{}_{a}){}_{\beta}{}^{\sigma}(\Sigma{}^{d e}){}_{\sigma}{}^{\gamma} +\frac{i}{32}(\Sigma{}_{d e}){}_{\eta}{}^{\alpha}\varepsilon{}^{r j}W{}^{\delta \rho}W{}_{\alpha \delta \rho}{}^{i}(\Gamma{}_{a}){}_{\beta}{}^{\sigma}(\Sigma{}^{d e}){}_{\sigma}{}^{\gamma}\\
&-\frac{i}{64}(\Sigma{}_{d e}){}^{\alpha \delta}\varepsilon{}^{r j}W{}_{\eta \alpha}X{}_{\delta}{}^{i}(\Gamma{}_{a}){}_{\beta}{}^{\rho}(\Sigma{}^{d e}){}_{\rho}{}^{\gamma} -\frac{3i}{64}(\Sigma{}_{d e}){}_{\eta}{}^{\alpha}\varepsilon{}^{r j}W{}_{\alpha \delta}X{}^{\delta i}(\Gamma{}_{a}){}_{\beta}{}^{\rho}(\Sigma{}^{d e}){}_{\rho}{}^{\gamma}\\
&-\frac{i}{16}(\Sigma{}_{d e}){}^{\alpha \delta}\varepsilon{}^{r j}(\Gamma{}^{f}){}_{\alpha}{}^{\rho}\big(\nabla_{f}W{}_{\delta \eta \rho}{}^{i}\big)(\Gamma{}_{a}){}_{\beta}{}^{\sigma}(\Sigma{}^{d e}){}_{\sigma}{}^{\gamma} +\frac{i}{32}(\Sigma{}_{d e}){}^{\alpha \delta}\varepsilon{}^{r j}(\Gamma{}^{f}){}_{\eta \alpha}\big(\nabla_{f}X{}_{\delta}{}^{i}\big)(\Gamma{}_{a}){}_{\beta}{}^{\rho}(\Sigma{}^{d e}){}_{\rho}{}^{\gamma}\\
&-\frac{i}{32}(\Sigma{}_{d e}){}_{\eta}{}^{\alpha}\varepsilon{}^{r j}(\Gamma{}^{f}){}_{\alpha \delta}\big(\nabla_{f}X{}^{\delta i}\big)(\Gamma{}_{a}){}_{\beta}{}^{\rho}(\Sigma{}^{d e}){}_{\rho}{}^{\gamma} +\frac{3i}{32}(\Sigma{}_{d e}){}^{\alpha \delta}\varepsilon{}^{r j}W{}_{\delta}{}^{\rho}W{}_{\alpha \eta \rho}{}^{i}(\Gamma{}_{a}){}_{\beta}{}^{\sigma}(\Sigma{}^{d e}){}_{\sigma}{}^{\gamma}\\
&+\frac{i}{32}(\Sigma{}_{d e}){}^{\alpha}{}_{\eta}\varepsilon{}^{r j}W{}^{\delta \rho}W{}_{\alpha \delta \rho}{}^{i}(\Gamma{}_{a}){}_{\beta}{}^{\sigma}(\Sigma{}^{d e}){}_{\sigma}{}^{\gamma} -\frac{i}{64}(\Sigma{}_{d e}){}^{\alpha \delta}\varepsilon{}^{r j}W{}_{\eta \delta}X{}_{\alpha}{}^{i}(\Gamma{}_{a}){}_{\beta}{}^{\rho}(\Sigma{}^{d e}){}_{\rho}{}^{\gamma}\\
&-\frac{3i}{64}(\Sigma{}_{d e}){}^{\alpha}{}_{\eta}\varepsilon{}^{r j}W{}_{\alpha \delta}X{}^{\delta i}(\Gamma{}_{a}){}_{\beta}{}^{\rho}(\Sigma{}^{d e}){}_{\rho}{}^{\gamma} -\frac{i}{16}(\Sigma{}_{d e}){}^{\alpha \delta}\varepsilon{}^{r j}(\Gamma{}^{f}){}_{\delta}{}^{\rho}\big(\nabla_{f}W{}_{\alpha \eta \rho}{}^{i}\big)(\Gamma{}_{a}){}_{\beta}{}^{\sigma}(\Sigma{}^{d e}){}_{\sigma}{}^{\gamma}\\
&+\frac{i}{32}(\Sigma{}_{d e}){}^{\alpha \delta}\varepsilon{}^{r j}(\Gamma{}^{f}){}_{\eta \delta}\big(\nabla_{f}X{}_{\alpha}{}^{i}\big)(\Gamma{}_{a}){}_{\beta}{}^{\rho}(\Sigma{}^{d e}){}_{\rho}{}^{\gamma} -\frac{i}{32}(\Sigma{}_{d e}){}^{\alpha}{}_{\eta}\varepsilon{}^{r j}(\Gamma{}^{f}){}_{\alpha \delta}\big(\nabla_{f}X{}^{\delta i}\big)(\Gamma{}_{a}){}_{\beta}{}^{\rho}(\Sigma{}^{d e}){}_{\rho}{}^{\gamma}\\
&-\frac{i}{8}\varepsilon{}^{i j}(\Sigma{}_{d e}){}^{\alpha \delta}\big(\nabla_{a}W{}_{\eta \alpha \delta}{}^{r}\big)(\Sigma{}^{d e}){}_{\beta}{}^{\gamma} -\frac{i}{16}\varepsilon{}^{i j}(\Sigma{}_{d e}){}_{\eta}{}^{\alpha}\big(\nabla_{a}X{}_{\alpha}{}^{r}\big)(\Sigma{}^{d e}){}_{\beta}{}^{\gamma}\\
&-\frac{i}{16}\varepsilon{}^{i j}(\Sigma{}_{d e}){}^{\alpha}{}_{\eta}\big(\nabla_{a}X{}_{\alpha}{}^{r}\big)(\Sigma{}^{d e}){}_{\beta}{}^{\gamma} -\frac{i}{8}\varepsilon{}^{i j}\mathcal T{}_{a \eta}{}^{\alpha}(\Sigma{}_{d e}){}^{\delta \rho}W{}_{\alpha \delta \rho}{}^{r}(\Sigma{}^{d e}){}_{\beta}{}^{\gamma}\\
&-\frac{i}{16}\varepsilon{}^{i j}\mathcal T{}_{a \eta}{}^{\alpha}(\Sigma{}_{d e}){}_{\alpha}{}^{\delta}X{}_{\delta}{}^{r}(\Sigma{}^{d e}){}_{\beta}{}^{\gamma} -\frac{i}{16}\varepsilon{}^{i j}\mathcal T{}_{a \eta}{}^{\alpha}(\Sigma{}_{d e}){}^{\delta}{}_{\alpha}X{}_{\delta}{}^{r}(\Sigma{}^{d e}){}_{\beta}{}^{\gamma}\\
&-\frac{i}{16}\varepsilon{}^{i j}\mathcal R(M){}_{a \eta}{}^{r}{}_{d}{}^{e}W{}_{e f}(\Sigma{}^{d f}){}_{\beta}{}^{\gamma} +\frac{i}{16}\varepsilon{}^{i j}\mathcal R(M){}_{a \eta}{}^{r d}{}_{e}W{}_{d f}(\Sigma{}^{e f}){}_{\beta}{}^{\gamma}\\
&-\frac{i}{16}\varepsilon{}^{i j}\mathcal R(M){}_{a \eta}{}^{r}{}_{d}{}^{e}W{}_{f e}(\Sigma{}^{f d}){}_{\beta}{}^{\gamma} +\frac{i}{16}\varepsilon{}^{i j}\mathcal R(M){}_{a \eta}{}^{r d}{}_{e}W{}_{f d}(\Sigma{}^{f e}){}_{\beta}{}^{\gamma}\\
&-\frac{i}{8}\varepsilon{}^{i j}\mathcal R(\mathbb D){}_{a \eta}{}^{r}W{}_{d e}(\Sigma{}^{d e}){}_{\beta}{}^{\gamma} -\frac{i}{8}\varepsilon{}^{i j}(\Sigma{}_{d a}){}^{\alpha \delta}\big(\nabla_{e}W{}_{\eta \alpha \delta}{}^{r}\big)(\Sigma{}^{e d}){}_{\beta}{}^{\gamma}\\
&-\frac{i}{16}\varepsilon{}^{i j}(\Sigma{}_{d a}){}_{\eta}{}^{\alpha}\big(\nabla_{e}X{}_{\alpha}{}^{r}\big)(\Sigma{}^{e d}){}_{\beta}{}^{\gamma} -\frac{i}{16}\varepsilon{}^{i j}(\Sigma{}_{d a}){}^{\alpha}{}_{\eta}\big(\nabla_{e}X{}_{\alpha}{}^{r}\big)(\Sigma{}^{e d}){}_{\beta}{}^{\gamma}\\
&-\frac{i}{8}\varepsilon{}^{i j}\mathcal T{}_{d \eta}{}^{\alpha}(\Sigma{}_{e a}){}^{\delta \rho}W{}_{\alpha \delta \rho}{}^{r}(\Sigma{}^{d e}){}_{\beta}{}^{\gamma} -\frac{i}{16}\varepsilon{}^{i j}\mathcal T{}_{d \eta}{}^{\alpha}(\Sigma{}_{e a}){}_{\alpha}{}^{\delta}X{}_{\delta}{}^{r}(\Sigma{}^{d e}){}_{\beta}{}^{\gamma}\\
&-\frac{i}{16}\varepsilon{}^{i j}\mathcal T{}_{d \eta}{}^{\alpha}(\Sigma{}_{e a}){}^{\delta}{}_{\alpha}X{}_{\delta}{}^{r}(\Sigma{}^{d e}){}_{\beta}{}^{\gamma} -\frac{i}{16}\varepsilon{}^{i j}\mathcal R(M){}_{d \eta}{}^{r}{}_{e}{}^{f}W{}_{f a}(\Sigma{}^{d e}){}_{\beta}{}^{\gamma}\\
&+\frac{i}{16}\varepsilon{}^{i j}\mathcal R(M){}_{d \eta}{}^{r e}{}_{f}W{}_{e a}(\Sigma{}^{d f}){}_{\beta}{}^{\gamma} -\frac{i}{16}\varepsilon{}^{i j}\mathcal R(M){}_{d \eta}{}^{r}{}_{a}{}^{e}W{}_{f e}(\Sigma{}^{d f}){}_{\beta}{}^{\gamma}\\
&+\frac{i}{16}\varepsilon{}^{i j}\mathcal R(M){}_{d \eta}{}^{r e}{}_{a}W{}_{f e}(\Sigma{}^{d f}){}_{\beta}{}^{\gamma} -\frac{i}{8}\varepsilon{}^{i j}\mathcal R(\mathbb D){}_{d \eta}{}^{r}W{}_{e a}(\Sigma{}^{d e}){}_{\beta}{}^{\gamma}\\
&-\frac{i}{8}\varepsilon{}^{i j}(\Sigma{}_{a d}){}^{\alpha \delta}\big(\nabla_{e}W{}_{\eta \alpha \delta}{}^{r}\big)(\Sigma{}^{d e}){}_{\beta}{}^{\gamma} -\frac{i}{16}\varepsilon{}^{i j}(\Sigma{}_{a d}){}_{\eta}{}^{\alpha}\big(\nabla_{e}X{}_{\alpha}{}^{r}\big)(\Sigma{}^{d e}){}_{\beta}{}^{\gamma}\\
&-\frac{i}{16}\varepsilon{}^{i j}(\Sigma{}_{a d}){}^{\alpha}{}_{\eta}\big(\nabla_{e}X{}_{\alpha}{}^{r}\big)(\Sigma{}^{d e}){}_{\beta}{}^{\gamma} -\frac{i}{8}\varepsilon{}^{i j}\mathcal T{}_{d \eta}{}^{\alpha}(\Sigma{}_{a e}){}^{\delta \rho}W{}_{\alpha \delta \rho}{}^{r}(\Sigma{}^{e d}){}_{\beta}{}^{\gamma}\\
&-\frac{i}{16}\varepsilon{}^{i j}\mathcal T{}_{d \eta}{}^{\alpha}(\Sigma{}_{a e}){}_{\alpha}{}^{\delta}X{}_{\delta}{}^{r}(\Sigma{}^{e d}){}_{\beta}{}^{\gamma} -\frac{i}{16}\varepsilon{}^{i j}\mathcal T{}_{d \eta}{}^{\alpha}(\Sigma{}_{a e}){}^{\delta}{}_{\alpha}X{}_{\delta}{}^{r}(\Sigma{}^{e d}){}_{\beta}{}^{\gamma}\\
&-\frac{i}{16}\varepsilon{}^{i j}\mathcal R(M){}_{d \eta}{}^{r}{}_{a}{}^{e}W{}_{e f}(\Sigma{}^{f d}){}_{\beta}{}^{\gamma} +\frac{i}{16}\varepsilon{}^{i j}\mathcal R(M){}_{d \eta}{}^{r e}{}_{a}W{}_{e f}(\Sigma{}^{f d}){}_{\beta}{}^{\gamma}\\
&-\frac{i}{16}\varepsilon{}^{i j}\mathcal R(M){}_{d \eta}{}^{r}{}_{e}{}^{f}W{}_{a f}(\Sigma{}^{e d}){}_{\beta}{}^{\gamma} +\frac{i}{16}\varepsilon{}^{i j}\mathcal R(M){}_{d \eta}{}^{r e}{}_{f}W{}_{a e}(\Sigma{}^{f d}){}_{\beta}{}^{\gamma}
\end{aligned}
\tag{S4-D-RS-1}
```

```math
\begin{aligned}
&-\frac{i}{8}\varepsilon{}^{i j}\mathcal R(\mathbb D){}_{d \eta}{}^{r}W{}_{a e}(\Sigma{}^{e d}){}_{\beta}{}^{\gamma} -\frac{i}{8}\varepsilon{}^{i j}(\Sigma{}^{d e}){}^{\alpha \delta}\big(\nabla_{d}W{}_{\eta \alpha \delta}{}^{r}\big)(\Sigma{}_{e a}){}_{\beta}{}^{\gamma}\\
&-\frac{i}{16}\varepsilon{}^{i j}(\Sigma{}^{d e}){}_{\eta}{}^{\alpha}\big(\nabla_{d}X{}_{\alpha}{}^{r}\big)(\Sigma{}_{e a}){}_{\beta}{}^{\gamma} -\frac{i}{16}\varepsilon{}^{i j}(\Sigma{}^{d e}){}^{\alpha}{}_{\eta}\big(\nabla_{d}X{}_{\alpha}{}^{r}\big)(\Sigma{}_{e a}){}_{\beta}{}^{\gamma}\\
&-\frac{i}{8}\varepsilon{}^{i j}\mathcal T{}_{d \eta}{}^{\alpha}(\Sigma{}^{d e}){}^{\delta \rho}W{}_{\alpha \delta \rho}{}^{r}(\Sigma{}_{e a}){}_{\beta}{}^{\gamma} -\frac{i}{16}\varepsilon{}^{i j}\mathcal T{}_{d \eta}{}^{\alpha}(\Sigma{}^{d e}){}_{\alpha}{}^{\delta}X{}_{\delta}{}^{r}(\Sigma{}_{e a}){}_{\beta}{}^{\gamma}\\
&-\frac{i}{16}\varepsilon{}^{i j}\mathcal T{}_{d \eta}{}^{\alpha}(\Sigma{}^{d e}){}^{\delta}{}_{\alpha}X{}_{\delta}{}^{r}(\Sigma{}_{e a}){}_{\beta}{}^{\gamma} -\frac{i}{16}\varepsilon{}^{i j}\mathcal R(M){}^{d}{}_{\eta}{}^{r}{}_{d}{}^{e}W{}_{e}{}^{f}(\Sigma{}_{f a}){}_{\beta}{}^{\gamma}\\
&+\frac{i}{16}\varepsilon{}^{i j}\mathcal R(M){}^{d}{}_{\eta}{}^{r e}{}_{d}W{}_{e}{}^{f}(\Sigma{}_{f a}){}_{\beta}{}^{\gamma} -\frac{i}{16}\varepsilon{}^{i j}\mathcal R(M){}_{d \eta}{}^{r}{}_{e}{}^{f}W{}^{d}{}_{f}(\Sigma{}^{e}{}_{a}){}_{\beta}{}^{\gamma}\\
&+\frac{i}{16}\varepsilon{}^{i j}\mathcal R(M){}_{d \eta}{}^{r e}{}_{f}W{}^{d}{}_{e}(\Sigma{}^{f}{}_{a}){}_{\beta}{}^{\gamma} -\frac{i}{8}\varepsilon{}^{i j}\mathcal R(\mathbb D){}_{d \eta}{}^{r}W{}^{d e}(\Sigma{}_{e a}){}_{\beta}{}^{\gamma}\\
&+\frac{3i}{16}\varepsilon{}^{i j}(\Sigma{}_{d a}){}^{\alpha \delta}\big(\nabla^{d}W{}_{\eta \alpha \delta}{}^{r}\big)\delta{}_{\beta}{}^{\gamma} +\frac{3i}{32}\varepsilon{}^{i j}(\Sigma{}_{d a}){}_{\eta}{}^{\alpha}\big(\nabla^{d}X{}_{\alpha}{}^{r}\big)\delta{}_{\beta}{}^{\gamma}\\
&+\frac{3i}{32}\varepsilon{}^{i j}(\Sigma{}_{d a}){}^{\alpha}{}_{\eta}\big(\nabla^{d}X{}_{\alpha}{}^{r}\big)\delta{}_{\beta}{}^{\gamma} +\frac{3i}{16}\varepsilon{}^{i j}\mathcal T{}^{d}{}_{\eta}{}^{\alpha}(\Sigma{}_{d a}){}^{\delta \rho}W{}_{\alpha \delta \rho}{}^{r}\delta{}_{\beta}{}^{\gamma}\\
&+\frac{3i}{32}\varepsilon{}^{i j}\mathcal T{}^{d}{}_{\eta}{}^{\alpha}(\Sigma{}_{d a}){}_{\alpha}{}^{\delta}X{}_{\delta}{}^{r}\delta{}_{\beta}{}^{\gamma} +\frac{3i}{32}\varepsilon{}^{i j}\mathcal T{}^{d}{}_{\eta}{}^{\alpha}(\Sigma{}_{d a}){}^{\delta}{}_{\alpha}X{}_{\delta}{}^{r}\delta{}_{\beta}{}^{\gamma}\\
&+\frac{3i}{32}\varepsilon{}^{i j}\mathcal R(M){}^{d}{}_{\eta}{}^{r}{}_{d}{}^{e}W{}_{e a}\delta{}_{\beta}{}^{\gamma} -\frac{3i}{32}\varepsilon{}^{i j}\mathcal R(M){}^{d}{}_{\eta}{}^{r e}{}_{d}W{}_{e a}\delta{}_{\beta}{}^{\gamma}\\
&+\frac{3i}{32}\varepsilon{}^{i j}\mathcal R(M){}^{d}{}_{\eta}{}^{r}{}_{a}{}^{e}W{}_{d e}\delta{}_{\beta}{}^{\gamma} -\frac{3i}{32}\varepsilon{}^{i j}\mathcal R(M){}^{d}{}_{\eta}{}^{r e}{}_{a}W{}_{d e}\delta{}_{\beta}{}^{\gamma}\\
&+\frac{3i}{16}\varepsilon{}^{i j}\mathcal R(\mathbb D){}^{d}{}_{\eta}{}^{r}W{}_{d a}\delta{}_{\beta}{}^{\gamma} -\frac{i}{16}\varepsilon{}^{i j}\varepsilon{}_{d a}{}^{e}{}_{f g}(\Sigma{}^{f g}){}^{\alpha \delta}\big(\nabla^{d}W{}_{\eta \alpha \delta}{}^{r}\big)(\Gamma{}_{e}){}_{\beta}{}^{\gamma}\\
&-\frac{i}{32}\varepsilon{}^{i j}\varepsilon{}_{d a}{}^{e}{}_{f g}(\Sigma{}^{f g}){}_{\eta}{}^{\alpha}\big(\nabla^{d}X{}_{\alpha}{}^{r}\big)(\Gamma{}_{e}){}_{\beta}{}^{\gamma} -\frac{i}{32}\varepsilon{}^{i j}\varepsilon{}_{d a}{}^{e}{}_{f g}(\Sigma{}^{f g}){}^{\alpha}{}_{\eta}\big(\nabla^{d}X{}_{\alpha}{}^{r}\big)(\Gamma{}_{e}){}_{\beta}{}^{\gamma}\\
&-\frac{i}{16}\varepsilon{}^{i j}\varepsilon{}_{d a}{}^{e}{}_{f g}\mathcal T{}^{d}{}_{\eta}{}^{\alpha}(\Sigma{}^{f g}){}^{\delta \rho}W{}_{\alpha \delta \rho}{}^{r}(\Gamma{}_{e}){}_{\beta}{}^{\gamma} -\frac{i}{32}\varepsilon{}^{i j}\varepsilon{}_{d a}{}^{e}{}_{f g}\mathcal T{}^{d}{}_{\eta}{}^{\alpha}(\Sigma{}^{f g}){}_{\alpha}{}^{\delta}X{}_{\delta}{}^{r}(\Gamma{}_{e}){}_{\beta}{}^{\gamma}\\
&-\frac{i}{32}\varepsilon{}^{i j}\varepsilon{}_{d a}{}^{e}{}_{f g}\mathcal T{}^{d}{}_{\eta}{}^{\alpha}(\Sigma{}^{f g}){}^{\delta}{}_{\alpha}X{}_{\delta}{}^{r}(\Gamma{}_{e}){}_{\beta}{}^{\gamma} -\frac{i}{32}\varepsilon{}^{i j}\varepsilon{}_{d a}{}^{e f}{}_{g}\mathcal R(M){}^{d}{}_{\eta}{}^{r}{}_{f}{}^{h}W{}_{h}{}^{g}(\Gamma{}_{e}){}_{\beta}{}^{\gamma}\\
&+\frac{i}{32}\varepsilon{}^{i j}\varepsilon{}_{d a}{}^{e f}{}_{g}\mathcal R(M){}^{d}{}_{\eta}{}^{r h}{}_{f}W{}_{h}{}^{g}(\Gamma{}_{e}){}_{\beta}{}^{\gamma} -\frac{i}{32}\varepsilon{}^{i j}\varepsilon{}_{d a}{}^{e}{}_{f}{}^{g}\mathcal R(M){}^{d}{}_{\eta}{}^{r}{}_{g}{}^{h}W{}^{f}{}_{h}(\Gamma{}_{e}){}_{\beta}{}^{\gamma}\\
&+\frac{i}{32}\varepsilon{}^{i j}\varepsilon{}_{d a}{}^{e}{}_{f}{}^{g}\mathcal R(M){}^{d}{}_{\eta}{}^{r h}{}_{g}W{}^{f}{}_{h}(\Gamma{}_{e}){}_{\beta}{}^{\gamma} -\frac{i}{16}\varepsilon{}^{i j}\varepsilon{}_{d a}{}^{e}{}_{f g}\mathcal R(\mathbb D){}^{d}{}_{\eta}{}^{r}W{}^{f g}(\Gamma{}_{e}){}_{\beta}{}^{\gamma}\\
&+\frac{i}{32}\varepsilon{}^{i j}\varepsilon{}^{d e f}{}_{g h}(\Sigma{}^{g h}){}^{\alpha \delta}W{}_{\eta \alpha \delta}{}^{r}W{}_{e f}(\Sigma{}_{d a}){}_{\beta}{}^{\gamma} +\frac{i}{64}\varepsilon{}^{i j}\varepsilon{}^{d e f}{}_{g h}(\Sigma{}^{g h}){}_{\eta}{}^{\alpha}X{}_{\alpha}{}^{r}W{}_{e f}(\Sigma{}_{d a}){}_{\beta}{}^{\gamma}\\
&+\frac{i}{64}\varepsilon{}^{i j}\varepsilon{}^{d e f}{}_{g h}(\Sigma{}^{g h}){}^{\alpha}{}_{\eta}X{}_{\alpha}{}^{r}W{}_{e f}(\Sigma{}_{d a}){}_{\beta}{}^{\gamma} +\frac{i}{32}\varepsilon{}^{i j}\varepsilon{}^{d e f}{}_{g h}W{}^{g h}(\Sigma{}_{e f}){}^{\alpha \delta}W{}_{\eta \alpha \delta}{}^{r}(\Sigma{}_{d a}){}_{\beta}{}^{\gamma}\\
&+\frac{i}{64}\varepsilon{}^{i j}\varepsilon{}^{d e f}{}_{g h}W{}^{g h}(\Sigma{}_{e f}){}_{\eta}{}^{\alpha}X{}_{\alpha}{}^{r}(\Sigma{}_{d a}){}_{\beta}{}^{\gamma} +\frac{i}{64}\varepsilon{}^{i j}\varepsilon{}^{d e f}{}_{g h}W{}^{g h}(\Sigma{}_{e f}){}^{\alpha}{}_{\eta}X{}_{\alpha}{}^{r}(\Sigma{}_{d a}){}_{\beta}{}^{\gamma}\\
&-\frac{3i}{64}\varepsilon{}^{i j}\varepsilon{}_{a d e f g}(\Sigma{}^{f g}){}^{\alpha \delta}W{}_{\eta \alpha \delta}{}^{r}W{}^{d e}\delta{}_{\beta}{}^{\gamma} -\frac{3i}{128}\varepsilon{}^{i j}\varepsilon{}_{a d e f g}(\Sigma{}^{f g}){}_{\eta}{}^{\alpha}X{}_{\alpha}{}^{r}W{}^{d e}\delta{}_{\beta}{}^{\gamma}\\
&-\frac{3i}{128}\varepsilon{}^{i j}\varepsilon{}_{a d e f g}(\Sigma{}^{f g}){}^{\alpha}{}_{\eta}X{}_{\alpha}{}^{r}W{}^{d e}\delta{}_{\beta}{}^{\gamma} -\frac{3i}{64}\varepsilon{}^{i j}\varepsilon{}_{a d e f g}W{}^{f g}(\Sigma{}^{d e}){}^{\alpha \delta}W{}_{\eta \alpha \delta}{}^{r}\delta{}_{\beta}{}^{\gamma}\\
&-\frac{3i}{128}\varepsilon{}^{i j}\varepsilon{}_{a d e f g}W{}^{f g}(\Sigma{}^{d e}){}_{\eta}{}^{\alpha}X{}_{\alpha}{}^{r}\delta{}_{\beta}{}^{\gamma} -\frac{3i}{128}\varepsilon{}^{i j}\varepsilon{}_{a d e f g}W{}^{f g}(\Sigma{}^{d e}){}^{\alpha}{}_{\eta}X{}_{\alpha}{}^{r}\delta{}_{\beta}{}^{\gamma}\\
&+\frac{i}{4}\varepsilon{}^{i j}(\Sigma{}_{a d}){}^{\alpha \delta}W{}_{\eta \alpha \delta}{}^{r}W{}^{e d}(\Gamma{}_{e}){}_{\beta}{}^{\gamma} +\frac{i}{8}\varepsilon{}^{i j}(\Sigma{}_{a d}){}_{\eta}{}^{\alpha}X{}_{\alpha}{}^{r}W{}^{e d}(\Gamma{}_{e}){}_{\beta}{}^{\gamma}\\
&+\frac{i}{8}\varepsilon{}^{i j}(\Sigma{}_{a d}){}^{\alpha}{}_{\eta}X{}_{\alpha}{}^{r}W{}^{e d}(\Gamma{}_{e}){}_{\beta}{}^{\gamma} +\frac{i}{4}\varepsilon{}^{i j}W{}_{a d}(\Sigma{}^{e d}){}^{\alpha \delta}W{}_{\eta \alpha \delta}{}^{r}(\Gamma{}_{e}){}_{\beta}{}^{\gamma}\\
&+\frac{i}{8}\varepsilon{}^{i j}W{}_{a d}(\Sigma{}^{e d}){}_{\eta}{}^{\alpha}X{}_{\alpha}{}^{r}(\Gamma{}_{e}){}_{\beta}{}^{\gamma} +\frac{i}{8}\varepsilon{}^{i j}W{}_{a d}(\Sigma{}^{e d}){}^{\alpha}{}_{\eta}X{}_{\alpha}{}^{r}(\Gamma{}_{e}){}_{\beta}{}^{\gamma}\\
&-\frac{3i}{64}\varepsilon{}^{i j}(\Sigma{}^{d e}){}^{\alpha \delta}W{}_{\eta \alpha \delta}{}^{r}W{}_{d e}(\Gamma{}_{a}){}_{\beta}{}^{\gamma} -\frac{3i}{128}\varepsilon{}^{i j}(\Sigma{}^{d e}){}_{\eta}{}^{\alpha}X{}_{\alpha}{}^{r}W{}_{d e}(\Gamma{}_{a}){}_{\beta}{}^{\gamma}\\
&-\frac{3i}{128}\varepsilon{}^{i j}(\Sigma{}^{d e}){}^{\alpha}{}_{\eta}X{}_{\alpha}{}^{r}W{}_{d e}(\Gamma{}_{a}){}_{\beta}{}^{\gamma} -\frac{3i}{64}\varepsilon{}^{i j}W{}^{d e}(\Sigma{}_{d e}){}^{\alpha \delta}W{}_{\eta \alpha \delta}{}^{r}(\Gamma{}_{a}){}_{\beta}{}^{\gamma}\\
&-\frac{3i}{128}\varepsilon{}^{i j}W{}^{d e}(\Sigma{}_{d e}){}_{\eta}{}^{\alpha}X{}_{\alpha}{}^{r}(\Gamma{}_{a}){}_{\beta}{}^{\gamma} -\frac{3i}{128}\varepsilon{}^{i j}W{}^{d e}(\Sigma{}_{d e}){}^{\alpha}{}_{\eta}X{}_{\alpha}{}^{r}(\Gamma{}_{a}){}_{\beta}{}^{\gamma}
\end{aligned}
\tag{S4-D-RS-2}
```

#### Spinor derivative of K curvature

```math
\begin{aligned}
\nabla_\eta^r \mathcal R(K){}_{a \beta}{}^{i b}={}&-\frac{1}{12}(\Gamma{}^{b}){}_{\beta}{}^{\alpha}(\Sigma{}_{d a}){}^{\delta \rho}\varepsilon{}^{r i}\big(\nabla^{d}W{}_{\eta \delta \rho \alpha}\big) -\frac{i}{12}(\Gamma{}^{b}){}_{\beta}{}^{\alpha}(\Sigma{}_{d a}){}^{\delta \rho}\varepsilon{}^{r i}(\Gamma{}^{e}){}_{\eta \delta}\big(\nabla^{d}\nabla_{e}W{}_{\rho \alpha}\big)\\
&-\frac{1}{12}(\Gamma{}^{b}){}_{\beta}{}^{\alpha}(\Sigma{}_{d a}){}_{\eta}{}^{\delta}\big(\nabla^{d}X{}_{\delta \alpha}{}^{r i}\big) -\frac{i}{12}(\Gamma{}^{b}){}_{\beta}{}^{\alpha}(\Sigma{}_{d a}){}^{\delta \rho}\varepsilon{}^{r i}(\Gamma{}^{e}){}_{\eta \rho}\big(\nabla^{d}\nabla_{e}W{}_{\delta \alpha}\big)\\
&-\frac{1}{12}(\Gamma{}^{b}){}_{\beta}{}^{\alpha}(\Sigma{}_{d a}){}^{\delta}{}_{\eta}\big(\nabla^{d}X{}_{\delta \alpha}{}^{r i}\big) -\frac{i}{12}(\Gamma{}^{b}){}_{\beta}{}^{\alpha}(\Sigma{}_{d a}){}^{\delta \rho}\varepsilon{}^{r i}(\Gamma{}^{e}){}_{\eta \alpha}\big(\nabla^{d}\nabla_{e}W{}_{\delta \rho}\big)\\
&-\frac{1}{12}(\Gamma{}^{b}){}_{\beta \eta}(\Sigma{}_{d a}){}^{\alpha \delta}\big(\nabla^{d}X{}_{\alpha \delta}{}^{r i}\big) -\frac{i}{24}(\Gamma{}^{b}){}_{\beta}{}^{\alpha}(\Sigma{}_{d a}){}_{\eta}{}^{\delta}\varepsilon{}^{r i}(\Gamma{}^{e}){}_{\delta}{}^{\rho}\big(\nabla^{d}\nabla_{e}W{}_{\alpha \rho}\big)\\
&-\frac{i}{24}(\Gamma{}^{b}){}_{\beta}{}^{\alpha}(\Sigma{}_{d a}){}_{\eta}{}^{\delta}\varepsilon{}^{r i}(\Gamma{}^{e}){}_{\alpha}{}^{\rho}\big(\nabla^{d}\nabla_{e}W{}_{\delta \rho}\big) -\frac{i}{24}(\Gamma{}^{b}){}_{\beta}{}^{\alpha}(\Sigma{}_{d a}){}^{\delta}{}_{\eta}\varepsilon{}^{r i}(\Gamma{}^{e}){}_{\delta}{}^{\rho}\big(\nabla^{d}\nabla_{e}W{}_{\alpha \rho}\big)\\
&-\frac{i}{24}(\Gamma{}^{b}){}_{\beta}{}^{\alpha}(\Sigma{}_{d a}){}^{\delta}{}_{\eta}\varepsilon{}^{r i}(\Gamma{}^{e}){}_{\alpha}{}^{\rho}\big(\nabla^{d}\nabla_{e}W{}_{\delta \rho}\big) -\frac{i}{24}(\Gamma{}^{b}){}_{\beta \eta}(\Sigma{}_{d a}){}^{\alpha \delta}\varepsilon{}^{r i}(\Gamma{}^{e}){}_{\alpha}{}^{\rho}\big(\nabla^{d}\nabla_{e}W{}_{\delta \rho}\big)\\
&-\frac{i}{24}(\Gamma{}^{b}){}_{\beta \eta}(\Sigma{}_{d a}){}^{\alpha \delta}\varepsilon{}^{r i}(\Gamma{}^{e}){}_{\delta}{}^{\rho}\big(\nabla^{d}\nabla_{e}W{}_{\alpha \rho}\big) -\frac{1}{12}(\Gamma{}^{b}){}_{\beta}{}^{\alpha}\mathcal T{}^{d}{}_{\eta}{}^{\delta}(\Sigma{}_{d a}){}^{\rho \sigma}\varepsilon{}^{r i}W{}_{\delta \rho \sigma \alpha}\\
&-\frac{i}{12}(\Gamma{}^{b}){}_{\beta}{}^{\alpha}\mathcal T{}^{d}{}_{\eta}{}^{\delta}(\Sigma{}_{d a}){}^{\rho \sigma}\varepsilon{}^{r i}(\Gamma{}^{e}){}_{\delta \rho}\big(\nabla_{e}W{}_{\sigma \alpha}\big) -\frac{1}{12}(\Gamma{}^{b}){}_{\beta}{}^{\alpha}\mathcal T{}^{d}{}_{\eta}{}^{\delta}(\Sigma{}_{d a}){}_{\delta}{}^{\rho}X{}_{\rho \alpha}{}^{r i}\\
&-\frac{i}{12}(\Gamma{}^{b}){}_{\beta}{}^{\alpha}\mathcal T{}^{d}{}_{\eta}{}^{\delta}(\Sigma{}_{d a}){}^{\rho \sigma}\varepsilon{}^{r i}(\Gamma{}^{e}){}_{\delta \sigma}\big(\nabla_{e}W{}_{\rho \alpha}\big) -\frac{1}{12}(\Gamma{}^{b}){}_{\beta}{}^{\alpha}\mathcal T{}^{d}{}_{\eta}{}^{\delta}(\Sigma{}_{d a}){}^{\rho}{}_{\delta}X{}_{\rho \alpha}{}^{r i}\\
&-\frac{i}{12}(\Gamma{}^{b}){}_{\beta}{}^{\alpha}\mathcal T{}^{d}{}_{\eta}{}^{\delta}(\Sigma{}_{d a}){}^{\rho \sigma}\varepsilon{}^{r i}(\Gamma{}^{e}){}_{\delta \alpha}\big(\nabla_{e}W{}_{\rho \sigma}\big) -\frac{1}{12}(\Gamma{}^{b}){}_{\beta \alpha}\mathcal T{}^{d}{}_{\eta}{}^{\alpha}(\Sigma{}_{d a}){}^{\delta \rho}X{}_{\delta \rho}{}^{r i}\\
&-\frac{i}{24}(\Gamma{}^{b}){}_{\beta}{}^{\alpha}\mathcal T{}^{d}{}_{\eta}{}^{\delta}(\Sigma{}_{d a}){}_{\delta}{}^{\rho}\varepsilon{}^{r i}(\Gamma{}^{e}){}_{\rho}{}^{\sigma}\big(\nabla_{e}W{}_{\alpha \sigma}\big) -\frac{i}{24}(\Gamma{}^{b}){}_{\beta}{}^{\alpha}\mathcal T{}^{d}{}_{\eta}{}^{\delta}(\Sigma{}_{d a}){}_{\delta}{}^{\rho}\varepsilon{}^{r i}(\Gamma{}^{e}){}_{\alpha}{}^{\sigma}\big(\nabla_{e}W{}_{\rho \sigma}\big)\\
&-\frac{i}{24}(\Gamma{}^{b}){}_{\beta}{}^{\alpha}\mathcal T{}^{d}{}_{\eta}{}^{\delta}(\Sigma{}_{d a}){}^{\rho}{}_{\delta}\varepsilon{}^{r i}(\Gamma{}^{e}){}_{\rho}{}^{\sigma}\big(\nabla_{e}W{}_{\alpha \sigma}\big) -\frac{i}{24}(\Gamma{}^{b}){}_{\beta}{}^{\alpha}\mathcal T{}^{d}{}_{\eta}{}^{\delta}(\Sigma{}_{d a}){}^{\rho}{}_{\delta}\varepsilon{}^{r i}(\Gamma{}^{e}){}_{\alpha}{}^{\sigma}\big(\nabla_{e}W{}_{\rho \sigma}\big)\\
&-\frac{i}{24}(\Gamma{}^{b}){}_{\beta \alpha}\mathcal T{}^{d}{}_{\eta}{}^{\alpha}(\Sigma{}_{d a}){}^{\delta \rho}\varepsilon{}^{r i}(\Gamma{}^{e}){}_{\delta}{}^{\sigma}\big(\nabla_{e}W{}_{\rho \sigma}\big) -\frac{i}{24}(\Gamma{}^{b}){}_{\beta \alpha}\mathcal T{}^{d}{}_{\eta}{}^{\alpha}(\Sigma{}_{d a}){}^{\delta \rho}\varepsilon{}^{r i}(\Gamma{}^{e}){}_{\rho}{}^{\sigma}\big(\nabla_{e}W{}_{\delta \sigma}\big)\\
&+\frac{1}{12}(\Gamma{}^{b}){}_{\beta}{}^{\alpha}\mathcal R(M){}^{d}{}_{\eta}{}^{r}{}_{d}{}^{e}W{}_{e a \alpha}{}^{i} -\frac{1}{12}(\Gamma{}^{b}){}_{\beta}{}^{\alpha}\mathcal R(M){}^{d}{}_{\eta}{}^{r e}{}_{d}W{}_{e a \alpha}{}^{i}\\
&+\frac{1}{12}(\Gamma{}^{b}){}_{\beta}{}^{\alpha}\mathcal R(M){}^{d}{}_{\eta}{}^{r}{}_{a}{}^{e}W{}_{d e \alpha}{}^{i} -\frac{1}{12}(\Gamma{}^{b}){}_{\beta}{}^{\alpha}\mathcal R(M){}^{d}{}_{\eta}{}^{r e}{}_{a}W{}_{d e \alpha}{}^{i}\\
&+\frac{1}{12}(\Gamma{}^{b}){}_{\beta}{}^{\alpha}\mathcal R(M){}^{d}{}_{\eta}{}^{r e f}(\Sigma{}_{e f}){}_{\alpha}{}^{\delta}W{}_{d a \delta}{}^{i} +\frac{1}{4}(\Gamma{}^{b}){}_{\beta}{}^{\alpha}\mathcal R(\mathbb D){}^{d}{}_{\eta}{}^{r}W{}_{d a \alpha}{}^{i}\\
&-\frac{1}{12}(\Gamma{}^{b}){}_{\beta}{}^{\alpha}\mathcal R(J){}^{d}{}_{\eta}{}^{r i l}W{}_{d a \alpha l} -\frac{1}{12}(\Gamma{}^{b}){}_{\beta}{}^{\alpha}\mathcal R(J){}^{d}{}_{\eta}{}^{r l i}W{}_{d a \alpha l}\\
&+\frac{1}{3}(\Gamma{}^{b}){}_{\beta}{}^{\alpha}\mathcal R(S){}^{d}{}_{\eta}{}^{r \delta i}(\Sigma{}_{d a}){}_{\delta}{}^{\rho}W{}_{\rho \alpha} +\frac{1}{3}(\Gamma{}^{b}){}_{\beta}{}^{\alpha}\mathcal R(S){}^{d}{}_{\eta}{}^{r \delta i}(\Sigma{}_{d a}){}^{\rho}{}_{\delta}W{}_{\rho \alpha}\\
&+\frac{1}{3}(\Gamma{}^{b}){}_{\beta \alpha}\mathcal R(S){}^{d}{}_{\eta}{}^{r \alpha i}(\Sigma{}_{d a}){}^{\delta \rho}W{}_{\delta \rho} -\frac{1}{24}(\Gamma{}_{a}){}_{\beta}{}^{\alpha}(\Sigma{}_{d}{}^{b}){}^{\delta \rho}\varepsilon{}^{r i}\big(\nabla^{d}W{}_{\eta \delta \rho \alpha}\big)\\
&-\frac{i}{24}(\Gamma{}_{a}){}_{\beta}{}^{\alpha}(\Sigma{}_{d}{}^{b}){}^{\delta \rho}\varepsilon{}^{r i}(\Gamma{}^{e}){}_{\eta \delta}\big(\nabla^{d}\nabla_{e}W{}_{\rho \alpha}\big) -\frac{1}{24}(\Gamma{}_{a}){}_{\beta}{}^{\alpha}(\Sigma{}_{d}{}^{b}){}_{\eta}{}^{\delta}\big(\nabla^{d}X{}_{\delta \alpha}{}^{r i}\big)\\
&-\frac{i}{24}(\Gamma{}_{a}){}_{\beta}{}^{\alpha}(\Sigma{}_{d}{}^{b}){}^{\delta \rho}\varepsilon{}^{r i}(\Gamma{}^{e}){}_{\eta \rho}\big(\nabla^{d}\nabla_{e}W{}_{\delta \alpha}\big) -\frac{1}{24}(\Gamma{}_{a}){}_{\beta}{}^{\alpha}(\Sigma{}_{d}{}^{b}){}^{\delta}{}_{\eta}\big(\nabla^{d}X{}_{\delta \alpha}{}^{r i}\big)\\
&-\frac{i}{24}(\Gamma{}_{a}){}_{\beta}{}^{\alpha}(\Sigma{}_{d}{}^{b}){}^{\delta \rho}\varepsilon{}^{r i}(\Gamma{}^{e}){}_{\eta \alpha}\big(\nabla^{d}\nabla_{e}W{}_{\delta \rho}\big) -\frac{1}{24}(\Gamma{}_{a}){}_{\beta \eta}(\Sigma{}_{d}{}^{b}){}^{\alpha \delta}\big(\nabla^{d}X{}_{\alpha \delta}{}^{r i}\big)\\
&-\frac{i}{48}(\Gamma{}_{a}){}_{\beta}{}^{\alpha}(\Sigma{}_{d}{}^{b}){}_{\eta}{}^{\delta}\varepsilon{}^{r i}(\Gamma{}^{e}){}_{\delta}{}^{\rho}\big(\nabla^{d}\nabla_{e}W{}_{\alpha \rho}\big) -\frac{i}{48}(\Gamma{}_{a}){}_{\beta}{}^{\alpha}(\Sigma{}_{d}{}^{b}){}_{\eta}{}^{\delta}\varepsilon{}^{r i}(\Gamma{}^{e}){}_{\alpha}{}^{\rho}\big(\nabla^{d}\nabla_{e}W{}_{\delta \rho}\big)\\
&-\frac{i}{48}(\Gamma{}_{a}){}_{\beta}{}^{\alpha}(\Sigma{}_{d}{}^{b}){}^{\delta}{}_{\eta}\varepsilon{}^{r i}(\Gamma{}^{e}){}_{\delta}{}^{\rho}\big(\nabla^{d}\nabla_{e}W{}_{\alpha \rho}\big) -\frac{i}{48}(\Gamma{}_{a}){}_{\beta}{}^{\alpha}(\Sigma{}_{d}{}^{b}){}^{\delta}{}_{\eta}\varepsilon{}^{r i}(\Gamma{}^{e}){}_{\alpha}{}^{\rho}\big(\nabla^{d}\nabla_{e}W{}_{\delta \rho}\big)\\
&-\frac{i}{48}(\Gamma{}_{a}){}_{\beta \eta}(\Sigma{}_{d}{}^{b}){}^{\alpha \delta}\varepsilon{}^{r i}(\Gamma{}^{e}){}_{\alpha}{}^{\rho}\big(\nabla^{d}\nabla_{e}W{}_{\delta \rho}\big) -\frac{i}{48}(\Gamma{}_{a}){}_{\beta \eta}(\Sigma{}_{d}{}^{b}){}^{\alpha \delta}\varepsilon{}^{r i}(\Gamma{}^{e}){}_{\delta}{}^{\rho}\big(\nabla^{d}\nabla_{e}W{}_{\alpha \rho}\big)\\
&-\frac{1}{24}(\Gamma{}_{a}){}_{\beta}{}^{\alpha}\mathcal T{}^{d}{}_{\eta}{}^{\delta}(\Sigma{}_{d}{}^{b}){}^{\rho \sigma}\varepsilon{}^{r i}W{}_{\delta \rho \sigma \alpha} -\frac{i}{24}(\Gamma{}_{a}){}_{\beta}{}^{\alpha}\mathcal T{}^{d}{}_{\eta}{}^{\delta}(\Sigma{}_{d}{}^{b}){}^{\rho \sigma}\varepsilon{}^{r i}(\Gamma{}^{e}){}_{\delta \rho}\big(\nabla_{e}W{}_{\sigma \alpha}\big)\\
&-\frac{1}{24}(\Gamma{}_{a}){}_{\beta}{}^{\alpha}\mathcal T{}^{d}{}_{\eta}{}^{\delta}(\Sigma{}_{d}{}^{b}){}_{\delta}{}^{\rho}X{}_{\rho \alpha}{}^{r i} -\frac{i}{24}(\Gamma{}_{a}){}_{\beta}{}^{\alpha}\mathcal T{}^{d}{}_{\eta}{}^{\delta}(\Sigma{}_{d}{}^{b}){}^{\rho \sigma}\varepsilon{}^{r i}(\Gamma{}^{e}){}_{\delta \sigma}\big(\nabla_{e}W{}_{\rho \alpha}\big)\\
&-\frac{1}{24}(\Gamma{}_{a}){}_{\beta}{}^{\alpha}\mathcal T{}^{d}{}_{\eta}{}^{\delta}(\Sigma{}_{d}{}^{b}){}^{\rho}{}_{\delta}X{}_{\rho \alpha}{}^{r i} -\frac{i}{24}(\Gamma{}_{a}){}_{\beta}{}^{\alpha}\mathcal T{}^{d}{}_{\eta}{}^{\delta}(\Sigma{}_{d}{}^{b}){}^{\rho \sigma}\varepsilon{}^{r i}(\Gamma{}^{e}){}_{\delta \alpha}\big(\nabla_{e}W{}_{\rho \sigma}\big)\\
&-\frac{1}{24}(\Gamma{}_{a}){}_{\beta \alpha}\mathcal T{}^{d}{}_{\eta}{}^{\alpha}(\Sigma{}_{d}{}^{b}){}^{\delta \rho}X{}_{\delta \rho}{}^{r i} -\frac{i}{48}(\Gamma{}_{a}){}_{\beta}{}^{\alpha}\mathcal T{}^{d}{}_{\eta}{}^{\delta}(\Sigma{}_{d}{}^{b}){}_{\delta}{}^{\rho}\varepsilon{}^{r i}(\Gamma{}^{e}){}_{\rho}{}^{\sigma}\big(\nabla_{e}W{}_{\alpha \sigma}\big)\\
&-\frac{i}{48}(\Gamma{}_{a}){}_{\beta}{}^{\alpha}\mathcal T{}^{d}{}_{\eta}{}^{\delta}(\Sigma{}_{d}{}^{b}){}_{\delta}{}^{\rho}\varepsilon{}^{r i}(\Gamma{}^{e}){}_{\alpha}{}^{\sigma}\big(\nabla_{e}W{}_{\rho \sigma}\big) -\frac{i}{48}(\Gamma{}_{a}){}_{\beta}{}^{\alpha}\mathcal T{}^{d}{}_{\eta}{}^{\delta}(\Sigma{}_{d}{}^{b}){}^{\rho}{}_{\delta}\varepsilon{}^{r i}(\Gamma{}^{e}){}_{\rho}{}^{\sigma}\big(\nabla_{e}W{}_{\alpha \sigma}\big)\\
&-\frac{i}{48}(\Gamma{}_{a}){}_{\beta}{}^{\alpha}\mathcal T{}^{d}{}_{\eta}{}^{\delta}(\Sigma{}_{d}{}^{b}){}^{\rho}{}_{\delta}\varepsilon{}^{r i}(\Gamma{}^{e}){}_{\alpha}{}^{\sigma}\big(\nabla_{e}W{}_{\rho \sigma}\big) -\frac{i}{48}(\Gamma{}_{a}){}_{\beta \alpha}\mathcal T{}^{d}{}_{\eta}{}^{\alpha}(\Sigma{}_{d}{}^{b}){}^{\delta \rho}\varepsilon{}^{r i}(\Gamma{}^{e}){}_{\delta}{}^{\sigma}\big(\nabla_{e}W{}_{\rho \sigma}\big)\\
&-\frac{i}{48}(\Gamma{}_{a}){}_{\beta \alpha}\mathcal T{}^{d}{}_{\eta}{}^{\alpha}(\Sigma{}_{d}{}^{b}){}^{\delta \rho}\varepsilon{}^{r i}(\Gamma{}^{e}){}_{\rho}{}^{\sigma}\big(\nabla_{e}W{}_{\delta \sigma}\big) +\frac{1}{24}(\Gamma{}_{a}){}_{\beta}{}^{\alpha}\mathcal R(M){}^{d}{}_{\eta}{}^{r}{}_{d}{}^{e}W{}_{e}{}^{b}{}_{\alpha}{}^{i}\\
&-\frac{1}{24}(\Gamma{}_{a}){}_{\beta}{}^{\alpha}\mathcal R(M){}^{d}{}_{\eta}{}^{r e}{}_{d}W{}_{e}{}^{b}{}_{\alpha}{}^{i} +\frac{1}{24}(\Gamma{}_{a}){}_{\beta}{}^{\alpha}\mathcal R(M){}^{d}{}_{\eta}{}^{r b e}W{}_{d e \alpha}{}^{i}\\
&-\frac{1}{24}(\Gamma{}_{a}){}_{\beta}{}^{\alpha}\mathcal R(M){}^{d}{}_{\eta}{}^{r e b}W{}_{d e \alpha}{}^{i} +\frac{1}{24}(\Gamma{}_{a}){}_{\beta}{}^{\alpha}\mathcal R(M){}^{d}{}_{\eta}{}^{r e f}(\Sigma{}_{e f}){}_{\alpha}{}^{\delta}W{}_{d}{}^{b}{}_{\delta}{}^{i}\\
&+\frac{1}{8}(\Gamma{}_{a}){}_{\beta}{}^{\alpha}\mathcal R(\mathbb D){}^{d}{}_{\eta}{}^{r}W{}_{d}{}^{b}{}_{\alpha}{}^{i} -\frac{1}{24}(\Gamma{}_{a}){}_{\beta}{}^{\alpha}\mathcal R(J){}^{d}{}_{\eta}{}^{r i l}W{}_{d}{}^{b}{}_{\alpha l}\\
&-\frac{1}{24}(\Gamma{}_{a}){}_{\beta}{}^{\alpha}\mathcal R(J){}^{d}{}_{\eta}{}^{r l i}W{}_{d}{}^{b}{}_{\alpha l} +\frac{1}{6}(\Gamma{}_{a}){}_{\beta}{}^{\alpha}\mathcal R(S){}^{d}{}_{\eta}{}^{r \delta i}(\Sigma{}_{d}{}^{b}){}_{\delta}{}^{\rho}W{}_{\rho \alpha}\\
&+\frac{1}{6}(\Gamma{}_{a}){}_{\beta}{}^{\alpha}\mathcal R(S){}^{d}{}_{\eta}{}^{r \delta i}(\Sigma{}_{d}{}^{b}){}^{\rho}{}_{\delta}W{}_{\rho \alpha} +\frac{1}{6}(\Gamma{}_{a}){}_{\beta \alpha}\mathcal R(S){}^{d}{}_{\eta}{}^{r \alpha i}(\Sigma{}_{d}{}^{b}){}^{\delta \rho}W{}_{\delta \rho}\\
&-\frac{1}{12}(\Gamma{}^{d}){}_{\beta}{}^{\alpha}(\Sigma{}_{a}{}^{b}){}^{\delta \rho}\varepsilon{}^{r i}\big(\nabla_{d}W{}_{\eta \delta \rho \alpha}\big) -\frac{i}{12}(\Gamma{}^{d}){}_{\beta}{}^{\alpha}(\Sigma{}_{a}{}^{b}){}^{\delta \rho}\varepsilon{}^{r i}(\Gamma{}^{e}){}_{\eta \delta}\big(\nabla_{d}\nabla_{e}W{}_{\rho \alpha}\big)\\
&-\frac{1}{12}(\Gamma{}^{d}){}_{\beta}{}^{\alpha}(\Sigma{}_{a}{}^{b}){}_{\eta}{}^{\delta}\big(\nabla_{d}X{}_{\delta \alpha}{}^{r i}\big) -\frac{i}{12}(\Gamma{}^{d}){}_{\beta}{}^{\alpha}(\Sigma{}_{a}{}^{b}){}^{\delta \rho}\varepsilon{}^{r i}(\Gamma{}^{e}){}_{\eta \rho}\big(\nabla_{d}\nabla_{e}W{}_{\delta \alpha}\big)\\
&-\frac{1}{12}(\Gamma{}^{d}){}_{\beta}{}^{\alpha}(\Sigma{}_{a}{}^{b}){}^{\delta}{}_{\eta}\big(\nabla_{d}X{}_{\delta \alpha}{}^{r i}\big) -\frac{i}{12}(\Gamma{}^{d}){}_{\beta}{}^{\alpha}(\Sigma{}_{a}{}^{b}){}^{\delta \rho}\varepsilon{}^{r i}(\Gamma{}^{e}){}_{\eta \alpha}\big(\nabla_{d}\nabla_{e}W{}_{\delta \rho}\big)\\
&-\frac{1}{12}(\Gamma{}^{d}){}_{\beta \eta}(\Sigma{}_{a}{}^{b}){}^{\alpha \delta}\big(\nabla_{d}X{}_{\alpha \delta}{}^{r i}\big) -\frac{i}{24}(\Gamma{}^{d}){}_{\beta}{}^{\alpha}(\Sigma{}_{a}{}^{b}){}_{\eta}{}^{\delta}\varepsilon{}^{r i}(\Gamma{}^{e}){}_{\delta}{}^{\rho}\big(\nabla_{d}\nabla_{e}W{}_{\alpha \rho}\big)\\
&-\frac{i}{24}(\Gamma{}^{d}){}_{\beta}{}^{\alpha}(\Sigma{}_{a}{}^{b}){}_{\eta}{}^{\delta}\varepsilon{}^{r i}(\Gamma{}^{e}){}_{\alpha}{}^{\rho}\big(\nabla_{d}\nabla_{e}W{}_{\delta \rho}\big) -\frac{i}{24}(\Gamma{}^{d}){}_{\beta}{}^{\alpha}(\Sigma{}_{a}{}^{b}){}^{\delta}{}_{\eta}\varepsilon{}^{r i}(\Gamma{}^{e}){}_{\delta}{}^{\rho}\big(\nabla_{d}\nabla_{e}W{}_{\alpha \rho}\big)\\
&-\frac{i}{24}(\Gamma{}^{d}){}_{\beta}{}^{\alpha}(\Sigma{}_{a}{}^{b}){}^{\delta}{}_{\eta}\varepsilon{}^{r i}(\Gamma{}^{e}){}_{\alpha}{}^{\rho}\big(\nabla_{d}\nabla_{e}W{}_{\delta \rho}\big) -\frac{i}{24}(\Gamma{}^{d}){}_{\beta \eta}(\Sigma{}_{a}{}^{b}){}^{\alpha \delta}\varepsilon{}^{r i}(\Gamma{}^{e}){}_{\alpha}{}^{\rho}\big(\nabla_{d}\nabla_{e}W{}_{\delta \rho}\big)\\
&-\frac{i}{24}(\Gamma{}^{d}){}_{\beta \eta}(\Sigma{}_{a}{}^{b}){}^{\alpha \delta}\varepsilon{}^{r i}(\Gamma{}^{e}){}_{\delta}{}^{\rho}\big(\nabla_{d}\nabla_{e}W{}_{\alpha \rho}\big) -\frac{1}{12}(\Gamma{}^{d}){}_{\beta}{}^{\alpha}\mathcal T{}_{d \eta}{}^{\delta}(\Sigma{}_{a}{}^{b}){}^{\rho \sigma}\varepsilon{}^{r i}W{}_{\delta \rho \sigma \alpha}\\
&-\frac{i}{12}(\Gamma{}^{d}){}_{\beta}{}^{\alpha}\mathcal T{}_{d \eta}{}^{\delta}(\Sigma{}_{a}{}^{b}){}^{\rho \sigma}\varepsilon{}^{r i}(\Gamma{}^{e}){}_{\delta \rho}\big(\nabla_{e}W{}_{\sigma \alpha}\big) -\frac{1}{12}(\Gamma{}^{d}){}_{\beta}{}^{\alpha}\mathcal T{}_{d \eta}{}^{\delta}(\Sigma{}_{a}{}^{b}){}_{\delta}{}^{\rho}X{}_{\rho \alpha}{}^{r i}\\
&-\frac{i}{12}(\Gamma{}^{d}){}_{\beta}{}^{\alpha}\mathcal T{}_{d \eta}{}^{\delta}(\Sigma{}_{a}{}^{b}){}^{\rho \sigma}\varepsilon{}^{r i}(\Gamma{}^{e}){}_{\delta \sigma}\big(\nabla_{e}W{}_{\rho \alpha}\big) -\frac{1}{12}(\Gamma{}^{d}){}_{\beta}{}^{\alpha}\mathcal T{}_{d \eta}{}^{\delta}(\Sigma{}_{a}{}^{b}){}^{\rho}{}_{\delta}X{}_{\rho \alpha}{}^{r i}\\
&-\frac{i}{12}(\Gamma{}^{d}){}_{\beta}{}^{\alpha}\mathcal T{}_{d \eta}{}^{\delta}(\Sigma{}_{a}{}^{b}){}^{\rho \sigma}\varepsilon{}^{r i}(\Gamma{}^{e}){}_{\delta \alpha}\big(\nabla_{e}W{}_{\rho \sigma}\big) -\frac{1}{12}(\Gamma{}^{d}){}_{\beta \alpha}\mathcal T{}_{d \eta}{}^{\alpha}(\Sigma{}_{a}{}^{b}){}^{\delta \rho}X{}_{\delta \rho}{}^{r i}\\
&-\frac{i}{24}(\Gamma{}^{d}){}_{\beta}{}^{\alpha}\mathcal T{}_{d \eta}{}^{\delta}(\Sigma{}_{a}{}^{b}){}_{\delta}{}^{\rho}\varepsilon{}^{r i}(\Gamma{}^{e}){}_{\rho}{}^{\sigma}\big(\nabla_{e}W{}_{\alpha \sigma}\big) -\frac{i}{24}(\Gamma{}^{d}){}_{\beta}{}^{\alpha}\mathcal T{}_{d \eta}{}^{\delta}(\Sigma{}_{a}{}^{b}){}_{\delta}{}^{\rho}\varepsilon{}^{r i}(\Gamma{}^{e}){}_{\alpha}{}^{\sigma}\big(\nabla_{e}W{}_{\rho \sigma}\big)\\
&-\frac{i}{24}(\Gamma{}^{d}){}_{\beta}{}^{\alpha}\mathcal T{}_{d \eta}{}^{\delta}(\Sigma{}_{a}{}^{b}){}^{\rho}{}_{\delta}\varepsilon{}^{r i}(\Gamma{}^{e}){}_{\rho}{}^{\sigma}\big(\nabla_{e}W{}_{\alpha \sigma}\big) -\frac{i}{24}(\Gamma{}^{d}){}_{\beta}{}^{\alpha}\mathcal T{}_{d \eta}{}^{\delta}(\Sigma{}_{a}{}^{b}){}^{\rho}{}_{\delta}\varepsilon{}^{r i}(\Gamma{}^{e}){}_{\alpha}{}^{\sigma}\big(\nabla_{e}W{}_{\rho \sigma}\big)\\
&-\frac{i}{24}(\Gamma{}^{d}){}_{\beta \alpha}\mathcal T{}_{d \eta}{}^{\alpha}(\Sigma{}_{a}{}^{b}){}^{\delta \rho}\varepsilon{}^{r i}(\Gamma{}^{e}){}_{\delta}{}^{\sigma}\big(\nabla_{e}W{}_{\rho \sigma}\big) -\frac{i}{24}(\Gamma{}^{d}){}_{\beta \alpha}\mathcal T{}_{d \eta}{}^{\alpha}(\Sigma{}_{a}{}^{b}){}^{\delta \rho}\varepsilon{}^{r i}(\Gamma{}^{e}){}_{\rho}{}^{\sigma}\big(\nabla_{e}W{}_{\delta \sigma}\big)
\end{aligned}
\tag{S4-D-RK-1}
```

```math
\begin{aligned}
&+\frac{1}{12}(\Gamma{}^{d}){}_{\beta}{}^{\alpha}\mathcal R(M){}_{d \eta}{}^{r}{}_{a}{}^{e}W{}_{e}{}^{b}{}_{\alpha}{}^{i} -\frac{1}{12}(\Gamma{}^{d}){}_{\beta}{}^{\alpha}\mathcal R(M){}_{d \eta}{}^{r e}{}_{a}W{}_{e}{}^{b}{}_{\alpha}{}^{i}\\
&+\frac{1}{12}(\Gamma{}^{d}){}_{\beta}{}^{\alpha}\mathcal R(M){}_{d \eta}{}^{r b e}W{}_{a e \alpha}{}^{i} -\frac{1}{12}(\Gamma{}^{d}){}_{\beta}{}^{\alpha}\mathcal R(M){}_{d \eta}{}^{r e b}W{}_{a e \alpha}{}^{i}\\
&+\frac{1}{12}(\Gamma{}^{d}){}_{\beta}{}^{\alpha}\mathcal R(M){}_{d \eta}{}^{r e f}(\Sigma{}_{e f}){}_{\alpha}{}^{\delta}W{}_{a}{}^{b}{}_{\delta}{}^{i} +\frac{1}{4}(\Gamma{}^{d}){}_{\beta}{}^{\alpha}\mathcal R(\mathbb D){}_{d \eta}{}^{r}W{}_{a}{}^{b}{}_{\alpha}{}^{i}\\
&-\frac{1}{12}(\Gamma{}^{d}){}_{\beta}{}^{\alpha}\mathcal R(J){}_{d \eta}{}^{r i l}W{}_{a}{}^{b}{}_{\alpha l} -\frac{1}{12}(\Gamma{}^{d}){}_{\beta}{}^{\alpha}\mathcal R(J){}_{d \eta}{}^{r l i}W{}_{a}{}^{b}{}_{\alpha l}\\
&+\frac{1}{3}(\Gamma{}^{d}){}_{\beta}{}^{\alpha}\mathcal R(S){}_{d \eta}{}^{r \delta i}(\Sigma{}_{a}{}^{b}){}_{\delta}{}^{\rho}W{}_{\rho \alpha} +\frac{1}{3}(\Gamma{}^{d}){}_{\beta}{}^{\alpha}\mathcal R(S){}_{d \eta}{}^{r \delta i}(\Sigma{}_{a}{}^{b}){}^{\rho}{}_{\delta}W{}_{\rho \alpha}\\
&+\frac{1}{3}(\Gamma{}^{d}){}_{\beta \alpha}\mathcal R(S){}_{d \eta}{}^{r \alpha i}(\Sigma{}_{a}{}^{b}){}^{\delta \rho}W{}_{\delta \rho} +\frac{1}{48}\varepsilon{}_{a}{}^{b d e f}(\Sigma{}_{e f}){}^{\alpha \delta}\varepsilon{}^{r i}\big(\nabla_{d}W{}_{\eta \alpha \delta \beta}\big)\\
&+\frac{i}{48}\varepsilon{}_{a}{}^{b d e f}(\Sigma{}_{e f}){}^{\alpha \delta}\varepsilon{}^{r i}(\Gamma{}^{g}){}_{\eta \alpha}\big(\nabla_{d}\nabla_{g}W{}_{\delta \beta}\big) +\frac{1}{48}\varepsilon{}_{a}{}^{b d e f}(\Sigma{}_{e f}){}_{\eta}{}^{\alpha}\big(\nabla_{d}X{}_{\alpha \beta}{}^{r i}\big)\\
&+\frac{i}{48}\varepsilon{}_{a}{}^{b d e f}(\Sigma{}_{e f}){}^{\alpha \delta}\varepsilon{}^{r i}(\Gamma{}^{g}){}_{\eta \delta}\big(\nabla_{d}\nabla_{g}W{}_{\alpha \beta}\big) +\frac{1}{48}\varepsilon{}_{a}{}^{b d e f}(\Sigma{}_{e f}){}^{\alpha}{}_{\eta}\big(\nabla_{d}X{}_{\alpha \beta}{}^{r i}\big)\\
&+\frac{i}{48}\varepsilon{}_{a}{}^{b d e f}(\Sigma{}_{e f}){}^{\alpha \delta}\varepsilon{}^{r i}(\Gamma{}^{g}){}_{\eta \beta}\big(\nabla_{d}\nabla_{g}W{}_{\alpha \delta}\big) +\frac{1}{48}\varepsilon{}_{a}{}^{b d e f}(\Sigma{}_{e f}){}^{\alpha \delta}\varepsilon{}_{\eta \beta}\big(\nabla_{d}X{}_{\alpha \delta}{}^{r i}\big)\\
&+\frac{i}{96}\varepsilon{}_{a}{}^{b d e f}(\Sigma{}_{e f}){}_{\eta}{}^{\alpha}\varepsilon{}^{r i}(\Gamma{}^{g}){}_{\alpha}{}^{\delta}\big(\nabla_{d}\nabla_{g}W{}_{\beta \delta}\big) +\frac{i}{96}\varepsilon{}_{a}{}^{b d e f}(\Sigma{}_{e f}){}_{\eta}{}^{\alpha}\varepsilon{}^{r i}(\Gamma{}^{g}){}_{\beta}{}^{\delta}\big(\nabla_{d}\nabla_{g}W{}_{\alpha \delta}\big)\\
&+\frac{i}{96}\varepsilon{}_{a}{}^{b d e f}(\Sigma{}_{e f}){}^{\alpha}{}_{\eta}\varepsilon{}^{r i}(\Gamma{}^{g}){}_{\alpha}{}^{\delta}\big(\nabla_{d}\nabla_{g}W{}_{\beta \delta}\big) +\frac{i}{96}\varepsilon{}_{a}{}^{b d e f}(\Sigma{}_{e f}){}^{\alpha}{}_{\eta}\varepsilon{}^{r i}(\Gamma{}^{g}){}_{\beta}{}^{\delta}\big(\nabla_{d}\nabla_{g}W{}_{\alpha \delta}\big)\\
&+\frac{i}{96}\varepsilon{}_{a}{}^{b d e f}(\Sigma{}_{e f}){}^{\alpha \delta}\varepsilon{}^{r i}\varepsilon{}_{\eta \beta}(\Gamma{}^{g}){}_{\alpha}{}^{\rho}\big(\nabla_{d}\nabla_{g}W{}_{\delta \rho}\big) +\frac{i}{96}\varepsilon{}_{a}{}^{b d e f}(\Sigma{}_{e f}){}^{\alpha \delta}\varepsilon{}^{r i}\varepsilon{}_{\eta \beta}(\Gamma{}^{g}){}_{\delta}{}^{\rho}\big(\nabla_{d}\nabla_{g}W{}_{\alpha \rho}\big)\\
&+\frac{1}{48}\varepsilon{}_{a}{}^{b d e f}\mathcal T{}_{d \eta}{}^{\alpha}(\Sigma{}_{e f}){}^{\delta \rho}\varepsilon{}^{r i}W{}_{\alpha \delta \rho \beta} +\frac{i}{48}\varepsilon{}_{a}{}^{b d e f}\mathcal T{}_{d \eta}{}^{\alpha}(\Sigma{}_{e f}){}^{\delta \rho}\varepsilon{}^{r i}(\Gamma{}^{g}){}_{\alpha \delta}\big(\nabla_{g}W{}_{\rho \beta}\big)\\
&+\frac{1}{48}\varepsilon{}_{a}{}^{b d e f}\mathcal T{}_{d \eta}{}^{\alpha}(\Sigma{}_{e f}){}_{\alpha}{}^{\delta}X{}_{\delta \beta}{}^{r i} +\frac{i}{48}\varepsilon{}_{a}{}^{b d e f}\mathcal T{}_{d \eta}{}^{\alpha}(\Sigma{}_{e f}){}^{\delta \rho}\varepsilon{}^{r i}(\Gamma{}^{g}){}_{\alpha \rho}\big(\nabla_{g}W{}_{\delta \beta}\big)\\
&+\frac{1}{48}\varepsilon{}_{a}{}^{b d e f}\mathcal T{}_{d \eta}{}^{\alpha}(\Sigma{}_{e f}){}^{\delta}{}_{\alpha}X{}_{\delta \beta}{}^{r i} +\frac{i}{48}\varepsilon{}_{a}{}^{b d e f}\mathcal T{}_{d \eta}{}^{\alpha}(\Sigma{}_{e f}){}^{\delta \rho}\varepsilon{}^{r i}(\Gamma{}^{g}){}_{\alpha \beta}\big(\nabla_{g}W{}_{\delta \rho}\big)\\
&-\frac{1}{48}\varepsilon{}_{a}{}^{b d e f}\mathcal T{}_{d \eta \beta}(\Sigma{}_{e f}){}^{\alpha \delta}X{}_{\alpha \delta}{}^{r i} +\frac{i}{96}\varepsilon{}_{a}{}^{b d e f}\mathcal T{}_{d \eta}{}^{\alpha}(\Sigma{}_{e f}){}_{\alpha}{}^{\delta}\varepsilon{}^{r i}(\Gamma{}^{g}){}_{\delta}{}^{\rho}\big(\nabla_{g}W{}_{\beta \rho}\big)\\
&+\frac{i}{96}\varepsilon{}_{a}{}^{b d e f}\mathcal T{}_{d \eta}{}^{\alpha}(\Sigma{}_{e f}){}_{\alpha}{}^{\delta}\varepsilon{}^{r i}(\Gamma{}^{g}){}_{\beta}{}^{\rho}\big(\nabla_{g}W{}_{\delta \rho}\big) +\frac{i}{96}\varepsilon{}_{a}{}^{b d e f}\mathcal T{}_{d \eta}{}^{\alpha}(\Sigma{}_{e f}){}^{\delta}{}_{\alpha}\varepsilon{}^{r i}(\Gamma{}^{g}){}_{\delta}{}^{\rho}\big(\nabla_{g}W{}_{\beta \rho}\big)\\
&+\frac{i}{96}\varepsilon{}_{a}{}^{b d e f}\mathcal T{}_{d \eta}{}^{\alpha}(\Sigma{}_{e f}){}^{\delta}{}_{\alpha}\varepsilon{}^{r i}(\Gamma{}^{g}){}_{\beta}{}^{\rho}\big(\nabla_{g}W{}_{\delta \rho}\big) -\frac{i}{96}\varepsilon{}_{a}{}^{b d e f}\mathcal T{}_{d \eta \beta}(\Sigma{}_{e f}){}^{\alpha \delta}\varepsilon{}^{r i}(\Gamma{}^{g}){}_{\alpha}{}^{\rho}\big(\nabla_{g}W{}_{\delta \rho}\big)\\
&-\frac{i}{96}\varepsilon{}_{a}{}^{b d e f}\mathcal T{}_{d \eta \beta}(\Sigma{}_{e f}){}^{\alpha \delta}\varepsilon{}^{r i}(\Gamma{}^{g}){}_{\delta}{}^{\rho}\big(\nabla_{g}W{}_{\alpha \rho}\big) -\frac{1}{48}\varepsilon{}_{a}{}^{b d e f}\mathcal R(M){}_{d \eta}{}^{r}{}_{e}{}^{g}W{}_{g f \beta}{}^{i}\\
&+\frac{1}{48}\varepsilon{}_{a}{}^{b d e f}\mathcal R(M){}_{d \eta}{}^{r g}{}_{e}W{}_{g f \beta}{}^{i} -\frac{1}{48}\varepsilon{}_{a}{}^{b d e f}\mathcal R(M){}_{d \eta}{}^{r}{}_{f}{}^{g}W{}_{e g \beta}{}^{i}\\
&+\frac{1}{48}\varepsilon{}_{a}{}^{b d e f}\mathcal R(M){}_{d \eta}{}^{r g}{}_{f}W{}_{e g \beta}{}^{i} -\frac{1}{48}\varepsilon{}_{a}{}^{b d e f}\mathcal R(M){}_{d \eta}{}^{r g h}(\Sigma{}_{g h}){}_{\beta}{}^{\alpha}W{}_{e f \alpha}{}^{i}\\
&-\frac{1}{16}\varepsilon{}_{a}{}^{b d e f}\mathcal R(\mathbb D){}_{d \eta}{}^{r}W{}_{e f \beta}{}^{i} +\frac{1}{48}\varepsilon{}_{a}{}^{b d e f}\mathcal R(J){}_{d \eta}{}^{r i l}W{}_{e f \beta l}\\
&+\frac{1}{48}\varepsilon{}_{a}{}^{b d e f}\mathcal R(J){}_{d \eta}{}^{r l i}W{}_{e f \beta l} -\frac{1}{12}\varepsilon{}_{a}{}^{b d e f}\mathcal R(S){}_{d \eta}{}^{r \alpha i}(\Sigma{}_{e f}){}_{\alpha}{}^{\delta}W{}_{\delta \beta}\\
&-\frac{1}{12}\varepsilon{}_{a}{}^{b d e f}\mathcal R(S){}_{d \eta}{}^{r \alpha i}(\Sigma{}_{e f}){}^{\delta}{}_{\alpha}W{}_{\delta \beta} +\frac{1}{12}\varepsilon{}_{a}{}^{b d e f}\mathcal R(S){}_{d \eta}{}^{r}{}_{\beta}{}^{i}(\Sigma{}_{e f}){}^{\alpha \delta}W{}_{\alpha \delta}\\
&+\frac{1}{8}(\Gamma{}^{b}){}_{\beta}{}^{\alpha}\big(\nabla_{a}X{}_{\eta \alpha}{}^{r i}\big) +\frac{i}{64}(\Gamma{}^{b}){}_{\beta \eta}\varepsilon{}^{r i}\big(\nabla_{a}Y\big)\\
&-\frac{3i}{16}(\Gamma{}^{b}){}_{\beta}{}^{\alpha}\varepsilon{}^{r i}(\Gamma{}^{d}){}_{\eta}{}^{\delta}\big(\nabla_{a}\nabla_{d}W{}_{\alpha \delta}\big) -\frac{i}{4}(\Gamma{}^{b}){}_{\beta}{}^{\alpha}\varepsilon{}^{r i}\big(\nabla_{a}W{}_{\eta}{}^{\delta}\big)W{}_{\alpha \delta}\\
&-\frac{i}{4}(\Gamma{}^{b}){}_{\beta}{}^{\alpha}\varepsilon{}^{r i}W{}_{\eta}{}^{\delta}\big(\nabla_{a}W{}_{\alpha \delta}\big) +\frac{i}{16}(\Gamma{}^{b}){}_{\beta \eta}\varepsilon{}^{r i}\big(\nabla_{a}W{}^{\alpha \delta}\big)W{}_{\alpha \delta}\\
&+\frac{i}{16}(\Gamma{}^{b}){}_{\beta \eta}\varepsilon{}^{r i}W{}^{\alpha \delta}\big(\nabla_{a}W{}_{\alpha \delta}\big) -\frac{i}{16}(\Gamma{}^{b}){}_{\beta}{}^{\alpha}\varepsilon{}^{r i}(\Gamma{}^{d}){}_{\alpha}{}^{\delta}\big(\nabla_{a}\nabla_{d}W{}_{\eta \delta}\big)\\
&+\frac{1}{8}(\Gamma{}^{b}){}_{\beta}{}^{\alpha}\mathcal T{}_{a \eta}{}^{\delta}X{}_{\delta \alpha}{}^{r i} +\frac{i}{64}(\Gamma{}^{b}){}_{\beta \alpha}\mathcal T{}_{a \eta}{}^{\alpha}\varepsilon{}^{r i}Y\\
&-\frac{3i}{16}(\Gamma{}^{b}){}_{\beta}{}^{\alpha}\mathcal T{}_{a \eta}{}^{\delta}\varepsilon{}^{r i}(\Gamma{}^{d}){}_{\delta}{}^{\rho}\big(\nabla_{d}W{}_{\alpha \rho}\big) -\frac{i}{4}(\Gamma{}^{b}){}_{\beta}{}^{\alpha}\mathcal T{}_{a \eta}{}^{\delta}\varepsilon{}^{r i}W{}_{\delta}{}^{\rho}W{}_{\alpha \rho}\\
&+\frac{i}{16}(\Gamma{}^{b}){}_{\beta \alpha}\mathcal T{}_{a \eta}{}^{\alpha}\varepsilon{}^{r i}W{}^{\delta \rho}W{}_{\delta \rho} -\frac{i}{16}(\Gamma{}^{b}){}_{\beta}{}^{\alpha}\mathcal T{}_{a \eta}{}^{\delta}\varepsilon{}^{r i}(\Gamma{}^{d}){}_{\alpha}{}^{\rho}\big(\nabla_{d}W{}_{\delta \rho}\big)\\
&+\frac{1}{16}(\Gamma{}^{b}){}_{\beta}{}^{\alpha}\mathcal R(M){}_{a \eta}{}^{r d e}(\Sigma{}_{d e}){}_{\alpha}{}^{\delta}X{}_{\delta}{}^{i} +\frac{3}{16}(\Gamma{}^{b}){}_{\beta}{}^{\alpha}\mathcal R(\mathbb D){}_{a \eta}{}^{r}X{}_{\alpha}{}^{i}\\
&-\frac{1}{16}(\Gamma{}^{b}){}_{\beta}{}^{\alpha}\mathcal R(J){}_{a \eta}{}^{r i l}X{}_{\alpha l} -\frac{1}{16}(\Gamma{}^{b}){}_{\beta}{}^{\alpha}\mathcal R(J){}_{a \eta}{}^{r l i}X{}_{\alpha l}\\
&+\frac{1}{2}(\Gamma{}^{b}){}_{\beta}{}^{\alpha}\mathcal R(S){}_{a \eta}{}^{r \delta i}W{}_{\delta \alpha} +\frac{3}{64}(\Sigma{}^{d e}){}^{\alpha \delta}W{}_{\eta \alpha \delta}{}^{r}(\Gamma{}_{a}){}_{\beta}{}^{\rho}(\Sigma{}_{d e}){}_{\rho}{}^{\sigma}(\Gamma{}^{b}){}_{\sigma}{}^{\tau}X{}_{\tau}{}^{i}\\
&+\frac{3}{128}(\Sigma{}^{d e}){}_{\eta}{}^{\alpha}X{}_{\alpha}{}^{r}(\Gamma{}_{a}){}_{\beta}{}^{\delta}(\Sigma{}_{d e}){}_{\delta}{}^{\rho}(\Gamma{}^{b}){}_{\rho}{}^{\sigma}X{}_{\sigma}{}^{i} +\frac{3}{128}(\Sigma{}^{d e}){}^{\alpha}{}_{\eta}X{}_{\alpha}{}^{r}(\Gamma{}_{a}){}_{\beta}{}^{\delta}(\Sigma{}_{d e}){}_{\delta}{}^{\rho}(\Gamma{}^{b}){}_{\rho}{}^{\sigma}X{}_{\sigma}{}^{i}\\
&+\frac{3}{64}W{}^{d e}(\Gamma{}_{a}){}_{\beta}{}^{\alpha}(\Sigma{}_{d e}){}_{\alpha}{}^{\delta}(\Gamma{}^{b}){}_{\delta}{}^{\rho}X{}_{\eta \rho}{}^{r i} +\frac{3i}{512}W{}^{d e}(\Gamma{}_{a}){}_{\beta}{}^{\alpha}(\Sigma{}_{d e}){}_{\alpha}{}^{\delta}(\Gamma{}^{b}){}_{\delta \eta}\varepsilon{}^{r i}Y\\
&-\frac{9i}{128}W{}^{d e}(\Gamma{}_{a}){}_{\beta}{}^{\alpha}(\Sigma{}_{d e}){}_{\alpha}{}^{\delta}(\Gamma{}^{b}){}_{\delta}{}^{\rho}\varepsilon{}^{r i}(\Gamma{}^{f}){}_{\eta}{}^{\sigma}\big(\nabla_{f}W{}_{\rho \sigma}\big) -\frac{3i}{32}W{}^{d e}(\Gamma{}_{a}){}_{\beta}{}^{\alpha}(\Sigma{}_{d e}){}_{\alpha}{}^{\delta}(\Gamma{}^{b}){}_{\delta}{}^{\rho}\varepsilon{}^{r i}W{}_{\eta}{}^{\sigma}W{}_{\rho \sigma}\\
&+\frac{3i}{128}W{}^{d e}(\Gamma{}_{a}){}_{\beta}{}^{\alpha}(\Sigma{}_{d e}){}_{\alpha}{}^{\delta}(\Gamma{}^{b}){}_{\delta \eta}\varepsilon{}^{r i}W{}^{\rho \sigma}W{}_{\rho \sigma} -\frac{3i}{128}W{}^{d e}(\Gamma{}_{a}){}_{\beta}{}^{\alpha}(\Sigma{}_{d e}){}_{\alpha}{}^{\delta}(\Gamma{}^{b}){}_{\delta}{}^{\rho}\varepsilon{}^{r i}(\Gamma{}^{f}){}_{\rho}{}^{\sigma}\big(\nabla_{f}W{}_{\eta \sigma}\big)\\
&-\frac{1}{64}(\Sigma{}^{d e}){}^{\alpha \delta}W{}_{\eta \alpha \delta}{}^{r}(\Sigma{}_{d e}){}_{\beta}{}^{\rho}(\Gamma{}_{a}){}_{\rho}{}^{\sigma}(\Gamma{}^{b}){}_{\sigma}{}^{\tau}X{}_{\tau}{}^{i} -\frac{1}{128}(\Sigma{}^{d e}){}_{\eta}{}^{\alpha}X{}_{\alpha}{}^{r}(\Sigma{}_{d e}){}_{\beta}{}^{\delta}(\Gamma{}_{a}){}_{\delta}{}^{\rho}(\Gamma{}^{b}){}_{\rho}{}^{\sigma}X{}_{\sigma}{}^{i}\\
&-\frac{1}{128}(\Sigma{}^{d e}){}^{\alpha}{}_{\eta}X{}_{\alpha}{}^{r}(\Sigma{}_{d e}){}_{\beta}{}^{\delta}(\Gamma{}_{a}){}_{\delta}{}^{\rho}(\Gamma{}^{b}){}_{\rho}{}^{\sigma}X{}_{\sigma}{}^{i} -\frac{1}{64}W{}^{d e}(\Sigma{}_{d e}){}_{\beta}{}^{\alpha}(\Gamma{}_{a}){}_{\alpha}{}^{\delta}(\Gamma{}^{b}){}_{\delta}{}^{\rho}X{}_{\eta \rho}{}^{r i}\\
&-\frac{i}{512}W{}^{d e}(\Sigma{}_{d e}){}_{\beta}{}^{\alpha}(\Gamma{}_{a}){}_{\alpha}{}^{\delta}(\Gamma{}^{b}){}_{\delta \eta}\varepsilon{}^{r i}Y +\frac{3i}{128}W{}^{d e}(\Sigma{}_{d e}){}_{\beta}{}^{\alpha}(\Gamma{}_{a}){}_{\alpha}{}^{\delta}(\Gamma{}^{b}){}_{\delta}{}^{\rho}\varepsilon{}^{r i}(\Gamma{}^{f}){}_{\eta}{}^{\sigma}\big(\nabla_{f}W{}_{\rho \sigma}\big)\\
&+\frac{i}{32}W{}^{d e}(\Sigma{}_{d e}){}_{\beta}{}^{\alpha}(\Gamma{}_{a}){}_{\alpha}{}^{\delta}(\Gamma{}^{b}){}_{\delta}{}^{\rho}\varepsilon{}^{r i}W{}_{\eta}{}^{\sigma}W{}_{\rho \sigma} -\frac{i}{128}W{}^{d e}(\Sigma{}_{d e}){}_{\beta}{}^{\alpha}(\Gamma{}_{a}){}_{\alpha}{}^{\delta}(\Gamma{}^{b}){}_{\delta \eta}\varepsilon{}^{r i}W{}^{\rho \sigma}W{}_{\rho \sigma}\\
&+\frac{i}{128}W{}^{d e}(\Sigma{}_{d e}){}_{\beta}{}^{\alpha}(\Gamma{}_{a}){}_{\alpha}{}^{\delta}(\Gamma{}^{b}){}_{\delta}{}^{\rho}\varepsilon{}^{r i}(\Gamma{}^{f}){}_{\rho}{}^{\sigma}\big(\nabla_{f}W{}_{\eta \sigma}\big) -\frac{1}{96}\varepsilon{}_{a d e f g}(\Sigma{}^{f g}){}^{\alpha \delta}W{}_{\eta \alpha \delta}{}^{r}(\Gamma{}^{b}){}_{\beta}{}^{\rho}W{}^{d e}{}_{\rho}{}^{i}\\
&-\frac{1}{192}\varepsilon{}_{a d e f g}(\Sigma{}^{f g}){}_{\eta}{}^{\alpha}X{}_{\alpha}{}^{r}(\Gamma{}^{b}){}_{\beta}{}^{\delta}W{}^{d e}{}_{\delta}{}^{i} -\frac{1}{192}\varepsilon{}_{a d e f g}(\Sigma{}^{f g}){}^{\alpha}{}_{\eta}X{}_{\alpha}{}^{r}(\Gamma{}^{b}){}_{\beta}{}^{\delta}W{}^{d e}{}_{\delta}{}^{i}\\
&+\frac{1}{192}\varepsilon{}_{a d e f g}W{}^{f g}(\Gamma{}^{b}){}_{\beta}{}^{\alpha}(\Sigma{}^{d e}){}^{\delta \rho}\varepsilon{}^{r i}W{}_{\eta \delta \rho \alpha} +\frac{i}{192}\varepsilon{}_{a d e f g}W{}^{f g}(\Gamma{}^{b}){}_{\beta}{}^{\alpha}(\Sigma{}^{d e}){}^{\delta \rho}\varepsilon{}^{r i}(\Gamma{}^{h}){}_{\eta \delta}\big(\nabla_{h}W{}_{\rho \alpha}\big)\\
&+\frac{1}{192}\varepsilon{}_{a d e f g}W{}^{f g}(\Gamma{}^{b}){}_{\beta}{}^{\alpha}(\Sigma{}^{d e}){}_{\eta}{}^{\delta}X{}_{\delta \alpha}{}^{r i} +\frac{i}{192}\varepsilon{}_{a d e f g}W{}^{f g}(\Gamma{}^{b}){}_{\beta}{}^{\alpha}(\Sigma{}^{d e}){}^{\delta \rho}\varepsilon{}^{r i}(\Gamma{}^{h}){}_{\eta \rho}\big(\nabla_{h}W{}_{\delta \alpha}\big)\\
&+\frac{1}{192}\varepsilon{}_{a d e f g}W{}^{f g}(\Gamma{}^{b}){}_{\beta}{}^{\alpha}(\Sigma{}^{d e}){}^{\delta}{}_{\eta}X{}_{\delta \alpha}{}^{r i} +\frac{i}{192}\varepsilon{}_{a d e f g}W{}^{f g}(\Gamma{}^{b}){}_{\beta}{}^{\alpha}(\Sigma{}^{d e}){}^{\delta \rho}\varepsilon{}^{r i}(\Gamma{}^{h}){}_{\eta \alpha}\big(\nabla_{h}W{}_{\delta \rho}\big)\\
&+\frac{1}{192}\varepsilon{}_{a d e f g}W{}^{f g}(\Gamma{}^{b}){}_{\beta \eta}(\Sigma{}^{d e}){}^{\alpha \delta}X{}_{\alpha \delta}{}^{r i} +\frac{i}{384}\varepsilon{}_{a d e f g}W{}^{f g}(\Gamma{}^{b}){}_{\beta}{}^{\alpha}(\Sigma{}^{d e}){}_{\eta}{}^{\delta}\varepsilon{}^{r i}(\Gamma{}^{h}){}_{\delta}{}^{\rho}\big(\nabla_{h}W{}_{\alpha \rho}\big)\\
&+\frac{i}{384}\varepsilon{}_{a d e f g}W{}^{f g}(\Gamma{}^{b}){}_{\beta}{}^{\alpha}(\Sigma{}^{d e}){}_{\eta}{}^{\delta}\varepsilon{}^{r i}(\Gamma{}^{h}){}_{\alpha}{}^{\rho}\big(\nabla_{h}W{}_{\delta \rho}\big) +\frac{i}{384}\varepsilon{}_{a d e f g}W{}^{f g}(\Gamma{}^{b}){}_{\beta}{}^{\alpha}(\Sigma{}^{d e}){}^{\delta}{}_{\eta}\varepsilon{}^{r i}(\Gamma{}^{h}){}_{\delta}{}^{\rho}\big(\nabla_{h}W{}_{\alpha \rho}\big)\\
&+\frac{i}{384}\varepsilon{}_{a d e f g}W{}^{f g}(\Gamma{}^{b}){}_{\beta}{}^{\alpha}(\Sigma{}^{d e}){}^{\delta}{}_{\eta}\varepsilon{}^{r i}(\Gamma{}^{h}){}_{\alpha}{}^{\rho}\big(\nabla_{h}W{}_{\delta \rho}\big) +\frac{i}{384}\varepsilon{}_{a d e f g}W{}^{f g}(\Gamma{}^{b}){}_{\beta \eta}(\Sigma{}^{d e}){}^{\alpha \delta}\varepsilon{}^{r i}(\Gamma{}^{h}){}_{\alpha}{}^{\rho}\big(\nabla_{h}W{}_{\delta \rho}\big)
\end{aligned}
\tag{S4-D-RK-2}
```

```math
\begin{aligned}
&+\frac{i}{384}\varepsilon{}_{a d e f g}W{}^{f g}(\Gamma{}^{b}){}_{\beta \eta}(\Sigma{}^{d e}){}^{\alpha \delta}\varepsilon{}^{r i}(\Gamma{}^{h}){}_{\delta}{}^{\rho}\big(\nabla_{h}W{}_{\alpha \rho}\big) +\frac{1}{8}\delta{}_{a}{}^{b}(\Sigma{}^{d e}){}^{\alpha \delta}W{}_{\eta \alpha \delta}{}^{r}W{}_{d e \beta}{}^{i}\\
&+\frac{1}{16}\delta{}_{a}{}^{b}(\Sigma{}^{d e}){}_{\eta}{}^{\alpha}X{}_{\alpha}{}^{r}W{}_{d e \beta}{}^{i} +\frac{1}{16}\delta{}_{a}{}^{b}(\Sigma{}^{d e}){}^{\alpha}{}_{\eta}X{}_{\alpha}{}^{r}W{}_{d e \beta}{}^{i}\\
&-\frac{1}{16}\delta{}_{a}{}^{b}W{}^{d e}(\Sigma{}_{d e}){}^{\alpha \delta}\varepsilon{}^{r i}W{}_{\eta \alpha \delta \beta} -\frac{i}{16}\delta{}_{a}{}^{b}W{}^{d e}(\Sigma{}_{d e}){}^{\alpha \delta}\varepsilon{}^{r i}(\Gamma{}^{f}){}_{\eta \alpha}\big(\nabla_{f}W{}_{\delta \beta}\big)\\
&-\frac{1}{16}\delta{}_{a}{}^{b}W{}^{d e}(\Sigma{}_{d e}){}_{\eta}{}^{\alpha}X{}_{\alpha \beta}{}^{r i} -\frac{i}{16}\delta{}_{a}{}^{b}W{}^{d e}(\Sigma{}_{d e}){}^{\alpha \delta}\varepsilon{}^{r i}(\Gamma{}^{f}){}_{\eta \delta}\big(\nabla_{f}W{}_{\alpha \beta}\big)\\
&-\frac{1}{16}\delta{}_{a}{}^{b}W{}^{d e}(\Sigma{}_{d e}){}^{\alpha}{}_{\eta}X{}_{\alpha \beta}{}^{r i} -\frac{i}{16}\delta{}_{a}{}^{b}W{}^{d e}(\Sigma{}_{d e}){}^{\alpha \delta}\varepsilon{}^{r i}(\Gamma{}^{f}){}_{\eta \beta}\big(\nabla_{f}W{}_{\alpha \delta}\big)\\
&-\frac{1}{16}\delta{}_{a}{}^{b}W{}^{d e}(\Sigma{}_{d e}){}^{\alpha \delta}\varepsilon{}_{\eta \beta}X{}_{\alpha \delta}{}^{r i} -\frac{i}{32}\delta{}_{a}{}^{b}W{}^{d e}(\Sigma{}_{d e}){}_{\eta}{}^{\alpha}\varepsilon{}^{r i}(\Gamma{}^{f}){}_{\alpha}{}^{\delta}\big(\nabla_{f}W{}_{\beta \delta}\big)\\
&-\frac{i}{32}\delta{}_{a}{}^{b}W{}^{d e}(\Sigma{}_{d e}){}_{\eta}{}^{\alpha}\varepsilon{}^{r i}(\Gamma{}^{f}){}_{\beta}{}^{\delta}\big(\nabla_{f}W{}_{\alpha \delta}\big) -\frac{i}{32}\delta{}_{a}{}^{b}W{}^{d e}(\Sigma{}_{d e}){}^{\alpha}{}_{\eta}\varepsilon{}^{r i}(\Gamma{}^{f}){}_{\alpha}{}^{\delta}\big(\nabla_{f}W{}_{\beta \delta}\big)\\
&-\frac{i}{32}\delta{}_{a}{}^{b}W{}^{d e}(\Sigma{}_{d e}){}^{\alpha}{}_{\eta}\varepsilon{}^{r i}(\Gamma{}^{f}){}_{\beta}{}^{\delta}\big(\nabla_{f}W{}_{\alpha \delta}\big) -\frac{i}{32}\delta{}_{a}{}^{b}W{}^{d e}(\Sigma{}_{d e}){}^{\alpha \delta}\varepsilon{}^{r i}\varepsilon{}_{\eta \beta}(\Gamma{}^{f}){}_{\alpha}{}^{\rho}\big(\nabla_{f}W{}_{\delta \rho}\big)\\
&-\frac{i}{32}\delta{}_{a}{}^{b}W{}^{d e}(\Sigma{}_{d e}){}^{\alpha \delta}\varepsilon{}^{r i}\varepsilon{}_{\eta \beta}(\Gamma{}^{f}){}_{\delta}{}^{\rho}\big(\nabla_{f}W{}_{\alpha \rho}\big) -\frac{1}{24}(\Sigma{}_{a}{}^{b}){}_{\beta}{}^{\alpha}(\Sigma{}_{d e}){}^{\delta \rho}\varepsilon{}^{r i}W{}_{\eta \delta \rho \alpha}W{}^{d e}\\
&-\frac{i}{24}(\Sigma{}_{a}{}^{b}){}_{\beta}{}^{\alpha}(\Sigma{}_{d e}){}^{\delta \rho}\varepsilon{}^{r i}(\Gamma{}^{f}){}_{\eta \delta}\big(\nabla_{f}W{}_{\rho \alpha}\big)W{}^{d e} -\frac{1}{24}(\Sigma{}_{a}{}^{b}){}_{\beta}{}^{\alpha}(\Sigma{}_{d e}){}_{\eta}{}^{\delta}X{}_{\delta \alpha}{}^{r i}W{}^{d e}\\
&-\frac{i}{24}(\Sigma{}_{a}{}^{b}){}_{\beta}{}^{\alpha}(\Sigma{}_{d e}){}^{\delta \rho}\varepsilon{}^{r i}(\Gamma{}^{f}){}_{\eta \rho}\big(\nabla_{f}W{}_{\delta \alpha}\big)W{}^{d e} -\frac{1}{24}(\Sigma{}_{a}{}^{b}){}_{\beta}{}^{\alpha}(\Sigma{}_{d e}){}^{\delta}{}_{\eta}X{}_{\delta \alpha}{}^{r i}W{}^{d e}\\
&-\frac{i}{24}(\Sigma{}_{a}{}^{b}){}_{\beta}{}^{\alpha}(\Sigma{}_{d e}){}^{\delta \rho}\varepsilon{}^{r i}(\Gamma{}^{f}){}_{\eta \alpha}\big(\nabla_{f}W{}_{\delta \rho}\big)W{}^{d e} -\frac{1}{24}(\Sigma{}_{a}{}^{b}){}_{\beta \eta}(\Sigma{}_{d e}){}^{\alpha \delta}X{}_{\alpha \delta}{}^{r i}W{}^{d e}\\
&-\frac{i}{48}(\Sigma{}_{a}{}^{b}){}_{\beta}{}^{\alpha}(\Sigma{}_{d e}){}_{\eta}{}^{\delta}\varepsilon{}^{r i}(\Gamma{}^{f}){}_{\delta}{}^{\rho}\big(\nabla_{f}W{}_{\alpha \rho}\big)W{}^{d e} -\frac{i}{48}(\Sigma{}_{a}{}^{b}){}_{\beta}{}^{\alpha}(\Sigma{}_{d e}){}_{\eta}{}^{\delta}\varepsilon{}^{r i}(\Gamma{}^{f}){}_{\alpha}{}^{\rho}\big(\nabla_{f}W{}_{\delta \rho}\big)W{}^{d e}\\
&-\frac{i}{48}(\Sigma{}_{a}{}^{b}){}_{\beta}{}^{\alpha}(\Sigma{}_{d e}){}^{\delta}{}_{\eta}\varepsilon{}^{r i}(\Gamma{}^{f}){}_{\delta}{}^{\rho}\big(\nabla_{f}W{}_{\alpha \rho}\big)W{}^{d e} -\frac{i}{48}(\Sigma{}_{a}{}^{b}){}_{\beta}{}^{\alpha}(\Sigma{}_{d e}){}^{\delta}{}_{\eta}\varepsilon{}^{r i}(\Gamma{}^{f}){}_{\alpha}{}^{\rho}\big(\nabla_{f}W{}_{\delta \rho}\big)W{}^{d e}\\
&-\frac{i}{48}(\Sigma{}_{a}{}^{b}){}_{\beta \eta}(\Sigma{}_{d e}){}^{\alpha \delta}\varepsilon{}^{r i}(\Gamma{}^{f}){}_{\alpha}{}^{\rho}\big(\nabla_{f}W{}_{\delta \rho}\big)W{}^{d e} -\frac{i}{48}(\Sigma{}_{a}{}^{b}){}_{\beta \eta}(\Sigma{}_{d e}){}^{\alpha \delta}\varepsilon{}^{r i}(\Gamma{}^{f}){}_{\delta}{}^{\rho}\big(\nabla_{f}W{}_{\alpha \rho}\big)W{}^{d e}\\
&-\frac{1}{12}(\Sigma{}_{a}{}^{b}){}_{\beta}{}^{\alpha}W{}_{d e \alpha}{}^{i}(\Sigma{}^{d e}){}^{\delta \rho}W{}_{\eta \delta \rho}{}^{r} -\frac{1}{24}(\Sigma{}_{a}{}^{b}){}_{\beta}{}^{\alpha}W{}_{d e \alpha}{}^{i}(\Sigma{}^{d e}){}_{\eta}{}^{\delta}X{}_{\delta}{}^{r}\\
&-\frac{1}{24}(\Sigma{}_{a}{}^{b}){}_{\beta}{}^{\alpha}W{}_{d e \alpha}{}^{i}(\Sigma{}^{d e}){}^{\delta}{}_{\eta}X{}_{\delta}{}^{r} -\frac{1}{12}(\Sigma{}^{d e}){}^{\alpha \delta}W{}_{\eta \alpha \delta}{}^{r}(\Sigma{}_{d e}){}_{\beta}{}^{\rho}W{}_{a}{}^{b}{}_{\rho}{}^{i}\\
&-\frac{1}{24}(\Sigma{}^{d e}){}_{\eta}{}^{\alpha}X{}_{\alpha}{}^{r}(\Sigma{}_{d e}){}_{\beta}{}^{\delta}W{}_{a}{}^{b}{}_{\delta}{}^{i} -\frac{1}{24}(\Sigma{}^{d e}){}^{\alpha}{}_{\eta}X{}_{\alpha}{}^{r}(\Sigma{}_{d e}){}_{\beta}{}^{\delta}W{}_{a}{}^{b}{}_{\delta}{}^{i}\\
&+\frac{1}{24}W{}^{d e}(\Sigma{}_{d e}){}_{\beta}{}^{\alpha}(\Sigma{}_{a}{}^{b}){}^{\delta \rho}\varepsilon{}^{r i}W{}_{\eta \delta \rho \alpha} +\frac{i}{24}W{}^{d e}(\Sigma{}_{d e}){}_{\beta}{}^{\alpha}(\Sigma{}_{a}{}^{b}){}^{\delta \rho}\varepsilon{}^{r i}(\Gamma{}^{f}){}_{\eta \delta}\big(\nabla_{f}W{}_{\rho \alpha}\big)\\
&+\frac{1}{24}W{}^{d e}(\Sigma{}_{d e}){}_{\beta}{}^{\alpha}(\Sigma{}_{a}{}^{b}){}_{\eta}{}^{\delta}X{}_{\delta \alpha}{}^{r i} +\frac{i}{24}W{}^{d e}(\Sigma{}_{d e}){}_{\beta}{}^{\alpha}(\Sigma{}_{a}{}^{b}){}^{\delta \rho}\varepsilon{}^{r i}(\Gamma{}^{f}){}_{\eta \rho}\big(\nabla_{f}W{}_{\delta \alpha}\big)\\
&+\frac{1}{24}W{}^{d e}(\Sigma{}_{d e}){}_{\beta}{}^{\alpha}(\Sigma{}_{a}{}^{b}){}^{\delta}{}_{\eta}X{}_{\delta \alpha}{}^{r i} +\frac{i}{24}W{}^{d e}(\Sigma{}_{d e}){}_{\beta}{}^{\alpha}(\Sigma{}_{a}{}^{b}){}^{\delta \rho}\varepsilon{}^{r i}(\Gamma{}^{f}){}_{\eta \alpha}\big(\nabla_{f}W{}_{\delta \rho}\big)\\
&+\frac{1}{24}W{}^{d e}(\Sigma{}_{d e}){}_{\beta \eta}(\Sigma{}_{a}{}^{b}){}^{\alpha \delta}X{}_{\alpha \delta}{}^{r i} +\frac{i}{48}W{}^{d e}(\Sigma{}_{d e}){}_{\beta}{}^{\alpha}(\Sigma{}_{a}{}^{b}){}_{\eta}{}^{\delta}\varepsilon{}^{r i}(\Gamma{}^{f}){}_{\delta}{}^{\rho}\big(\nabla_{f}W{}_{\alpha \rho}\big)\\
&+\frac{i}{48}W{}^{d e}(\Sigma{}_{d e}){}_{\beta}{}^{\alpha}(\Sigma{}_{a}{}^{b}){}_{\eta}{}^{\delta}\varepsilon{}^{r i}(\Gamma{}^{f}){}_{\alpha}{}^{\rho}\big(\nabla_{f}W{}_{\delta \rho}\big) +\frac{i}{48}W{}^{d e}(\Sigma{}_{d e}){}_{\beta}{}^{\alpha}(\Sigma{}_{a}{}^{b}){}^{\delta}{}_{\eta}\varepsilon{}^{r i}(\Gamma{}^{f}){}_{\delta}{}^{\rho}\big(\nabla_{f}W{}_{\alpha \rho}\big)\\
&+\frac{i}{48}W{}^{d e}(\Sigma{}_{d e}){}_{\beta}{}^{\alpha}(\Sigma{}_{a}{}^{b}){}^{\delta}{}_{\eta}\varepsilon{}^{r i}(\Gamma{}^{f}){}_{\alpha}{}^{\rho}\big(\nabla_{f}W{}_{\delta \rho}\big) +\frac{i}{48}W{}^{d e}(\Sigma{}_{d e}){}_{\beta \eta}(\Sigma{}_{a}{}^{b}){}^{\alpha \delta}\varepsilon{}^{r i}(\Gamma{}^{f}){}_{\alpha}{}^{\rho}\big(\nabla_{f}W{}_{\delta \rho}\big)\\
&+\frac{i}{48}W{}^{d e}(\Sigma{}_{d e}){}_{\beta \eta}(\Sigma{}_{a}{}^{b}){}^{\alpha \delta}\varepsilon{}^{r i}(\Gamma{}^{f}){}_{\delta}{}^{\rho}\big(\nabla_{f}W{}_{\alpha \rho}\big) +\frac{13}{48}(\Sigma{}_{a d}){}^{\alpha \delta}W{}_{\eta \alpha \delta}{}^{r}W{}^{d b}{}_{\beta}{}^{i}\\
&+\frac{13}{96}(\Sigma{}_{a d}){}_{\eta}{}^{\alpha}X{}_{\alpha}{}^{r}W{}^{d b}{}_{\beta}{}^{i} +\frac{13}{96}(\Sigma{}_{a d}){}^{\alpha}{}_{\eta}X{}_{\alpha}{}^{r}W{}^{d b}{}_{\beta}{}^{i}\\
&-\frac{13}{96}W{}_{a d}(\Sigma{}^{d b}){}^{\alpha \delta}\varepsilon{}^{r i}W{}_{\eta \alpha \delta \beta} -\frac{13i}{96}W{}_{a d}(\Sigma{}^{d b}){}^{\alpha \delta}\varepsilon{}^{r i}(\Gamma{}^{e}){}_{\eta \alpha}\big(\nabla_{e}W{}_{\delta \beta}\big)\\
&-\frac{13}{96}W{}_{a d}(\Sigma{}^{d b}){}_{\eta}{}^{\alpha}X{}_{\alpha \beta}{}^{r i} -\frac{13i}{96}W{}_{a d}(\Sigma{}^{d b}){}^{\alpha \delta}\varepsilon{}^{r i}(\Gamma{}^{e}){}_{\eta \delta}\big(\nabla_{e}W{}_{\alpha \beta}\big)\\
&-\frac{13}{96}W{}_{a d}(\Sigma{}^{d b}){}^{\alpha}{}_{\eta}X{}_{\alpha \beta}{}^{r i} -\frac{13i}{96}W{}_{a d}(\Sigma{}^{d b}){}^{\alpha \delta}\varepsilon{}^{r i}(\Gamma{}^{e}){}_{\eta \beta}\big(\nabla_{e}W{}_{\alpha \delta}\big)\\
&-\frac{13}{96}W{}_{a d}(\Sigma{}^{d b}){}^{\alpha \delta}\varepsilon{}_{\eta \beta}X{}_{\alpha \delta}{}^{r i} -\frac{13i}{192}W{}_{a d}(\Sigma{}^{d b}){}_{\eta}{}^{\alpha}\varepsilon{}^{r i}(\Gamma{}^{e}){}_{\alpha}{}^{\delta}\big(\nabla_{e}W{}_{\beta \delta}\big)\\
&-\frac{13i}{192}W{}_{a d}(\Sigma{}^{d b}){}_{\eta}{}^{\alpha}\varepsilon{}^{r i}(\Gamma{}^{e}){}_{\beta}{}^{\delta}\big(\nabla_{e}W{}_{\alpha \delta}\big) -\frac{13i}{192}W{}_{a d}(\Sigma{}^{d b}){}^{\alpha}{}_{\eta}\varepsilon{}^{r i}(\Gamma{}^{e}){}_{\alpha}{}^{\delta}\big(\nabla_{e}W{}_{\beta \delta}\big)\\
&-\frac{13i}{192}W{}_{a d}(\Sigma{}^{d b}){}^{\alpha}{}_{\eta}\varepsilon{}^{r i}(\Gamma{}^{e}){}_{\beta}{}^{\delta}\big(\nabla_{e}W{}_{\alpha \delta}\big) -\frac{13i}{192}W{}_{a d}(\Sigma{}^{d b}){}^{\alpha \delta}\varepsilon{}^{r i}\varepsilon{}_{\eta \beta}(\Gamma{}^{e}){}_{\alpha}{}^{\rho}\big(\nabla_{e}W{}_{\delta \rho}\big)\\
&-\frac{13i}{192}W{}_{a d}(\Sigma{}^{d b}){}^{\alpha \delta}\varepsilon{}^{r i}\varepsilon{}_{\eta \beta}(\Gamma{}^{e}){}_{\delta}{}^{\rho}\big(\nabla_{e}W{}_{\alpha \rho}\big) -\frac{11}{96}(\Sigma{}_{a d}){}^{\alpha \delta}\varepsilon{}^{r i}W{}_{\eta \alpha \delta \beta}W{}^{d b}\\
&-\frac{11i}{96}(\Sigma{}_{a d}){}^{\alpha \delta}\varepsilon{}^{r i}(\Gamma{}^{e}){}_{\eta \alpha}\big(\nabla_{e}W{}_{\delta \beta}\big)W{}^{d b} -\frac{11}{96}(\Sigma{}_{a d}){}_{\eta}{}^{\alpha}X{}_{\alpha \beta}{}^{r i}W{}^{d b}\\
&-\frac{11i}{96}(\Sigma{}_{a d}){}^{\alpha \delta}\varepsilon{}^{r i}(\Gamma{}^{e}){}_{\eta \delta}\big(\nabla_{e}W{}_{\alpha \beta}\big)W{}^{d b} -\frac{11}{96}(\Sigma{}_{a d}){}^{\alpha}{}_{\eta}X{}_{\alpha \beta}{}^{r i}W{}^{d b}\\
&-\frac{11i}{96}(\Sigma{}_{a d}){}^{\alpha \delta}\varepsilon{}^{r i}(\Gamma{}^{e}){}_{\eta \beta}\big(\nabla_{e}W{}_{\alpha \delta}\big)W{}^{d b} -\frac{11}{96}(\Sigma{}_{a d}){}^{\alpha \delta}\varepsilon{}_{\eta \beta}X{}_{\alpha \delta}{}^{r i}W{}^{d b}\\
&-\frac{11i}{192}(\Sigma{}_{a d}){}_{\eta}{}^{\alpha}\varepsilon{}^{r i}(\Gamma{}^{e}){}_{\alpha}{}^{\delta}\big(\nabla_{e}W{}_{\beta \delta}\big)W{}^{d b} -\frac{11i}{192}(\Sigma{}_{a d}){}_{\eta}{}^{\alpha}\varepsilon{}^{r i}(\Gamma{}^{e}){}_{\beta}{}^{\delta}\big(\nabla_{e}W{}_{\alpha \delta}\big)W{}^{d b}\\
&-\frac{11i}{192}(\Sigma{}_{a d}){}^{\alpha}{}_{\eta}\varepsilon{}^{r i}(\Gamma{}^{e}){}_{\alpha}{}^{\delta}\big(\nabla_{e}W{}_{\beta \delta}\big)W{}^{d b} -\frac{11i}{192}(\Sigma{}_{a d}){}^{\alpha}{}_{\eta}\varepsilon{}^{r i}(\Gamma{}^{e}){}_{\beta}{}^{\delta}\big(\nabla_{e}W{}_{\alpha \delta}\big)W{}^{d b}\\
&-\frac{11i}{192}(\Sigma{}_{a d}){}^{\alpha \delta}\varepsilon{}^{r i}\varepsilon{}_{\eta \beta}(\Gamma{}^{e}){}_{\alpha}{}^{\rho}\big(\nabla_{e}W{}_{\delta \rho}\big)W{}^{d b} -\frac{11i}{192}(\Sigma{}_{a d}){}^{\alpha \delta}\varepsilon{}^{r i}\varepsilon{}_{\eta \beta}(\Gamma{}^{e}){}_{\delta}{}^{\rho}\big(\nabla_{e}W{}_{\alpha \rho}\big)W{}^{d b}\\
&-\frac{11}{48}W{}_{a d \beta}{}^{i}(\Sigma{}^{d b}){}^{\alpha \delta}W{}_{\eta \alpha \delta}{}^{r} -\frac{11}{96}W{}_{a d \beta}{}^{i}(\Sigma{}^{d b}){}_{\eta}{}^{\alpha}X{}_{\alpha}{}^{r}\\
&-\frac{11}{96}W{}_{a d \beta}{}^{i}(\Sigma{}^{d b}){}^{\alpha}{}_{\eta}X{}_{\alpha}{}^{r} +\frac{13}{384}(\Gamma{}_{a}){}_{\beta}{}^{\alpha}(\Sigma{}_{d e}){}^{\delta \rho}\varepsilon{}^{r i}W{}_{\eta \delta \rho \alpha}\varepsilon{}^{d e b}{}_{f g}W{}^{f g}\\
&+\frac{13i}{384}(\Gamma{}_{a}){}_{\beta}{}^{\alpha}(\Sigma{}_{d e}){}^{\delta \rho}\varepsilon{}^{r i}(\Gamma{}^{f}){}_{\eta \delta}\big(\nabla_{f}W{}_{\rho \alpha}\big)\varepsilon{}^{d e b}{}_{g h}W{}^{g h} +\frac{13}{384}(\Gamma{}_{a}){}_{\beta}{}^{\alpha}(\Sigma{}_{d e}){}_{\eta}{}^{\delta}X{}_{\delta \alpha}{}^{r i}\varepsilon{}^{d e b}{}_{f g}W{}^{f g}\\
&+\frac{13i}{384}(\Gamma{}_{a}){}_{\beta}{}^{\alpha}(\Sigma{}_{d e}){}^{\delta \rho}\varepsilon{}^{r i}(\Gamma{}^{f}){}_{\eta \rho}\big(\nabla_{f}W{}_{\delta \alpha}\big)\varepsilon{}^{d e b}{}_{g h}W{}^{g h} +\frac{13}{384}(\Gamma{}_{a}){}_{\beta}{}^{\alpha}(\Sigma{}_{d e}){}^{\delta}{}_{\eta}X{}_{\delta \alpha}{}^{r i}\varepsilon{}^{d e b}{}_{f g}W{}^{f g}\\
&+\frac{13i}{384}(\Gamma{}_{a}){}_{\beta}{}^{\alpha}(\Sigma{}_{d e}){}^{\delta \rho}\varepsilon{}^{r i}(\Gamma{}^{f}){}_{\eta \alpha}\big(\nabla_{f}W{}_{\delta \rho}\big)\varepsilon{}^{d e b}{}_{g h}W{}^{g h} +\frac{13}{384}(\Gamma{}_{a}){}_{\beta \eta}(\Sigma{}_{d e}){}^{\alpha \delta}X{}_{\alpha \delta}{}^{r i}\varepsilon{}^{d e b}{}_{f g}W{}^{f g}\\
&+\frac{13i}{768}(\Gamma{}_{a}){}_{\beta}{}^{\alpha}(\Sigma{}_{d e}){}_{\eta}{}^{\delta}\varepsilon{}^{r i}(\Gamma{}^{f}){}_{\delta}{}^{\rho}\big(\nabla_{f}W{}_{\alpha \rho}\big)\varepsilon{}^{d e b}{}_{g h}W{}^{g h} +\frac{13i}{768}(\Gamma{}_{a}){}_{\beta}{}^{\alpha}(\Sigma{}_{d e}){}_{\eta}{}^{\delta}\varepsilon{}^{r i}(\Gamma{}^{f}){}_{\alpha}{}^{\rho}\big(\nabla_{f}W{}_{\delta \rho}\big)\varepsilon{}^{d e b}{}_{g h}W{}^{g h}\\
&+\frac{13i}{768}(\Gamma{}_{a}){}_{\beta}{}^{\alpha}(\Sigma{}_{d e}){}^{\delta}{}_{\eta}\varepsilon{}^{r i}(\Gamma{}^{f}){}_{\delta}{}^{\rho}\big(\nabla_{f}W{}_{\alpha \rho}\big)\varepsilon{}^{d e b}{}_{g h}W{}^{g h} +\frac{13i}{768}(\Gamma{}_{a}){}_{\beta}{}^{\alpha}(\Sigma{}_{d e}){}^{\delta}{}_{\eta}\varepsilon{}^{r i}(\Gamma{}^{f}){}_{\alpha}{}^{\rho}\big(\nabla_{f}W{}_{\delta \rho}\big)\varepsilon{}^{d e b}{}_{g h}W{}^{g h}\\
&+\frac{13i}{768}(\Gamma{}_{a}){}_{\beta \eta}(\Sigma{}_{d e}){}^{\alpha \delta}\varepsilon{}^{r i}(\Gamma{}^{f}){}_{\alpha}{}^{\rho}\big(\nabla_{f}W{}_{\delta \rho}\big)\varepsilon{}^{d e b}{}_{g h}W{}^{g h} +\frac{13i}{768}(\Gamma{}_{a}){}_{\beta \eta}(\Sigma{}_{d e}){}^{\alpha \delta}\varepsilon{}^{r i}(\Gamma{}^{f}){}_{\delta}{}^{\rho}\big(\nabla_{f}W{}_{\alpha \rho}\big)\varepsilon{}^{d e b}{}_{g h}W{}^{g h}\\
&+\frac{13}{192}(\Gamma{}_{a}){}_{\beta}{}^{\alpha}W{}_{d e \alpha}{}^{i}\varepsilon{}^{d e b}{}_{f g}(\Sigma{}^{f g}){}^{\delta \rho}W{}_{\eta \delta \rho}{}^{r} +\frac{13}{384}(\Gamma{}_{a}){}_{\beta}{}^{\alpha}W{}_{d e \alpha}{}^{i}\varepsilon{}^{d e b}{}_{f g}(\Sigma{}^{f g}){}_{\eta}{}^{\delta}X{}_{\delta}{}^{r}\\
&+\frac{13}{384}(\Gamma{}_{a}){}_{\beta}{}^{\alpha}W{}_{d e \alpha}{}^{i}\varepsilon{}^{d e b}{}_{f g}(\Sigma{}^{f g}){}^{\delta}{}_{\eta}X{}_{\delta}{}^{r}
\end{aligned}
\tag{S4-D-RK-3}
```

## 4. Explicit calculation for every input

### 4.1 The graded second product rule

The first derivative of the denominator and a product is

```math
\nabla_\eta^r(W^{-n}P)=-niW^{-n-1}\lambda_\eta^rP+W^{-n}\nabla_\eta^rP.
\tag{S4-08}
```

Acting on both written products gives, without reordering the two gaugini,

```math
\begin{aligned}
\nabla_\zeta^t\nabla_\eta^r(W^{-n}P)
={}&-n(n+1)W^{-n-2}\lambda_\zeta^t\lambda_\eta^rP
-niW^{-n-1}(\nabla_\zeta^t\lambda_\eta^r)P
+niW^{-n-1}\lambda_\eta^r\nabla_\zeta^tP\\
&-niW^{-n-1}\lambda_\zeta^t\nabla_\eta^rP
+W^{-n}\nabla_\zeta^t\nabla_\eta^rP,\\
-ni(\nabla_\zeta^t\lambda_\eta^r)P
={}&2ni\varepsilon^{tr}(F_{\zeta\eta}+W_{\zeta\eta}W)P
+ni\varepsilon_{\zeta\eta}X^{tr}P
+ni\varepsilon^{tr}(\Gamma^a)_{\zeta\eta}(\nabla_aW)P.
\end{aligned}
\tag{S4-09}
```

The third term in the first equality has a plus sign because the derivative passes the odd $`\lambda_\eta^r`$. The coefficient of the first term is $`(-ni)(-(n+1)i)=-n(n+1)`$. This rule does not presume that $`P`$ is a bosonic truncation.

For an actual ordered numerator $`A_1\cdots A_m`$, the differentiated slot $`A_q`$ acquires the sign $`(-1)^{|A_1|+\cdots+|A_{q-1}|}`$. The following subsections write every such product out for the **actual** inputs, including their symmetrization halves. Each subsection shows the input from our primary, the evaluated first derivative used in our spinor, then the fully written second product rule. Substituting the displayed elementary, geometric and vector-commutator identities gives the endpoint in §8. The endpoint contains the resulting field terms explicitly; it is not a prescription to perform those substitutions later.

In each subsection the common scalar contraction is exactly (S4-02). The first-derivative rows are the spinor before its common $`\varepsilon_{jr}/3`$ contraction, so that neither this factor nor $`-i/4`$ is inadvertently applied twice.

### Input H0.1

```math
\begin{aligned}
\left.H^{ij}\right|_{\mathrm{H0.1}}={}&-\frac{3i}{8}W{}_{a b}X{}^{a b i j}
\end{aligned}
\tag{S4-H0.1-input}
```

Insert the elementary derivative laws and, for every vector derivative, (S4-06). The evaluated first derivative is

```math
\begin{aligned}
\left.\nabla_\eta^rH^{ij}\right|_{\mathrm{H0.1}}={}&-\frac{3i}{8}(\Sigma{}_{a b}){}^{\alpha \beta}W{}_{\eta \alpha \beta}{}^{r}X{}^{a b i j} -\frac{3i}{16}(\Sigma{}_{a b}){}_{\eta}{}^{\alpha}X{}_{\alpha}{}^{r}X{}^{a b i j}\\
&-\frac{3i}{16}(\Sigma{}_{a b}){}^{\alpha}{}_{\eta}X{}_{\alpha}{}^{r}X{}^{a b i j} -\frac{3}{16}W{}_{a b}(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r i}W{}_{\eta \gamma}W{}_{\alpha \beta}{}^{\gamma j}\\
&-\frac{9}{32}W{}_{a b}(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r i}W{}_{\alpha \beta}X{}_{\eta}{}^{j} +\frac{3}{8}W{}_{a b}(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r i}(\Gamma{}^{c}){}_{\eta}{}^{\gamma}\big(\nabla_{c}W{}_{\alpha \beta \gamma}{}^{j}\big)\\
&-\frac{9}{32}W{}_{a b}(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r i}W{}_{\alpha}{}^{\gamma}W{}_{\beta \eta \gamma}{}^{j} -\frac{3}{32}W{}_{a b}(\Sigma{}^{a b}){}_{\eta}{}^{\alpha}\varepsilon{}^{r i}W{}^{\beta \gamma}W{}_{\alpha \beta \gamma}{}^{j}\\
&+\frac{3}{64}W{}_{a b}(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r i}W{}_{\eta \alpha}X{}_{\beta}{}^{j} +\frac{9}{64}W{}_{a b}(\Sigma{}^{a b}){}_{\eta}{}^{\alpha}\varepsilon{}^{r i}W{}_{\alpha \beta}X{}^{\beta j}\\
&+\frac{3}{16}W{}_{a b}(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r i}(\Gamma{}^{c}){}_{\alpha}{}^{\gamma}\big(\nabla_{c}W{}_{\beta \eta \gamma}{}^{j}\big) -\frac{3}{32}W{}_{a b}(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r i}(\Gamma{}^{c}){}_{\eta \alpha}\big(\nabla_{c}X{}_{\beta}{}^{j}\big)\\
&+\frac{3}{32}W{}_{a b}(\Sigma{}^{a b}){}_{\eta}{}^{\alpha}\varepsilon{}^{r i}(\Gamma{}^{c}){}_{\alpha \beta}\big(\nabla_{c}X{}^{\beta j}\big) -\frac{9}{32}W{}_{a b}(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r i}W{}_{\beta}{}^{\gamma}W{}_{\alpha \eta \gamma}{}^{j}\\
&-\frac{3}{32}W{}_{a b}(\Sigma{}^{a b}){}^{\alpha}{}_{\eta}\varepsilon{}^{r i}W{}^{\beta \gamma}W{}_{\alpha \beta \gamma}{}^{j} +\frac{3}{64}W{}_{a b}(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r i}W{}_{\eta \beta}X{}_{\alpha}{}^{j}\\
&+\frac{9}{64}W{}_{a b}(\Sigma{}^{a b}){}^{\alpha}{}_{\eta}\varepsilon{}^{r i}W{}_{\alpha \beta}X{}^{\beta j} +\frac{3}{16}W{}_{a b}(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r i}(\Gamma{}^{c}){}_{\beta}{}^{\gamma}\big(\nabla_{c}W{}_{\alpha \eta \gamma}{}^{j}\big)\\
&-\frac{3}{32}W{}_{a b}(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r i}(\Gamma{}^{c}){}_{\eta \beta}\big(\nabla_{c}X{}_{\alpha}{}^{j}\big) +\frac{3}{32}W{}_{a b}(\Sigma{}^{a b}){}^{\alpha}{}_{\eta}\varepsilon{}^{r i}(\Gamma{}^{c}){}_{\alpha \beta}\big(\nabla_{c}X{}^{\beta j}\big)\\
&-\frac{3}{16}W{}_{a b}(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r j}W{}_{\eta \gamma}W{}_{\alpha \beta}{}^{\gamma i} -\frac{9}{32}W{}_{a b}(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r j}W{}_{\alpha \beta}X{}_{\eta}{}^{i}\\
&+\frac{3}{8}W{}_{a b}(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r j}(\Gamma{}^{c}){}_{\eta}{}^{\gamma}\big(\nabla_{c}W{}_{\alpha \beta \gamma}{}^{i}\big) -\frac{9}{32}W{}_{a b}(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r j}W{}_{\alpha}{}^{\gamma}W{}_{\beta \eta \gamma}{}^{i}\\
&-\frac{3}{32}W{}_{a b}(\Sigma{}^{a b}){}_{\eta}{}^{\alpha}\varepsilon{}^{r j}W{}^{\beta \gamma}W{}_{\alpha \beta \gamma}{}^{i} +\frac{3}{64}W{}_{a b}(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r j}W{}_{\eta \alpha}X{}_{\beta}{}^{i}\\
&+\frac{9}{64}W{}_{a b}(\Sigma{}^{a b}){}_{\eta}{}^{\alpha}\varepsilon{}^{r j}W{}_{\alpha \beta}X{}^{\beta i} +\frac{3}{16}W{}_{a b}(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r j}(\Gamma{}^{c}){}_{\alpha}{}^{\gamma}\big(\nabla_{c}W{}_{\beta \eta \gamma}{}^{i}\big)\\
&-\frac{3}{32}W{}_{a b}(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r j}(\Gamma{}^{c}){}_{\eta \alpha}\big(\nabla_{c}X{}_{\beta}{}^{i}\big) +\frac{3}{32}W{}_{a b}(\Sigma{}^{a b}){}_{\eta}{}^{\alpha}\varepsilon{}^{r j}(\Gamma{}^{c}){}_{\alpha \beta}\big(\nabla_{c}X{}^{\beta i}\big)\\
&-\frac{9}{32}W{}_{a b}(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r j}W{}_{\beta}{}^{\gamma}W{}_{\alpha \eta \gamma}{}^{i} -\frac{3}{32}W{}_{a b}(\Sigma{}^{a b}){}^{\alpha}{}_{\eta}\varepsilon{}^{r j}W{}^{\beta \gamma}W{}_{\alpha \beta \gamma}{}^{i}\\
&+\frac{3}{64}W{}_{a b}(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r j}W{}_{\eta \beta}X{}_{\alpha}{}^{i} +\frac{9}{64}W{}_{a b}(\Sigma{}^{a b}){}^{\alpha}{}_{\eta}\varepsilon{}^{r j}W{}_{\alpha \beta}X{}^{\beta i}\\
&+\frac{3}{16}W{}_{a b}(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r j}(\Gamma{}^{c}){}_{\beta}{}^{\gamma}\big(\nabla_{c}W{}_{\alpha \eta \gamma}{}^{i}\big) -\frac{3}{32}W{}_{a b}(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r j}(\Gamma{}^{c}){}_{\eta \beta}\big(\nabla_{c}X{}_{\alpha}{}^{i}\big)\\
&+\frac{3}{32}W{}_{a b}(\Sigma{}^{a b}){}^{\alpha}{}_{\eta}\varepsilon{}^{r j}(\Gamma{}^{c}){}_{\alpha \beta}\big(\nabla_{c}X{}^{\beta i}\big)
\end{aligned}
\tag{S4-H0.1-spinor}
```

The next left derivative gives the following individual product terms. Each sign records the parity of the factors to the left of the differentiated slot.

```math
\begin{aligned}
\left.\nabla_\zeta^t\nabla_\eta^rH^{ij}\right|_{\mathrm{H0.1}}={}&-\frac{3i}{8}(\Sigma{}_{a b}){}^{\alpha \beta}\nabla_{\zeta}^{t}\big(W{}_{\eta \alpha \beta}{}^{r}\big)X{}^{a b i j} +\frac{3i}{8}(\Sigma{}_{a b}){}^{\alpha \beta}W{}_{\eta \alpha \beta}{}^{r}\nabla_{\zeta}^{t}\big(X{}^{a b i j}\big)\\
&-\frac{3i}{16}(\Sigma{}_{a b}){}_{\eta}{}^{\alpha}\nabla_{\zeta}^{t}\big(X{}_{\alpha}{}^{r}\big)X{}^{a b i j} +\frac{3i}{16}(\Sigma{}_{a b}){}_{\eta}{}^{\alpha}X{}_{\alpha}{}^{r}\nabla_{\zeta}^{t}\big(X{}^{a b i j}\big)\\
&-\frac{3i}{16}(\Sigma{}_{a b}){}^{\alpha}{}_{\eta}\nabla_{\zeta}^{t}\big(X{}_{\alpha}{}^{r}\big)X{}^{a b i j} +\frac{3i}{16}(\Sigma{}_{a b}){}^{\alpha}{}_{\eta}X{}_{\alpha}{}^{r}\nabla_{\zeta}^{t}\big(X{}^{a b i j}\big)\\
&-\frac{3}{16}\nabla_{\zeta}^{t}\big(W{}_{a b}\big)(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r i}W{}_{\eta \gamma}W{}_{\alpha \beta}{}^{\gamma j} -\frac{3}{16}W{}_{a b}(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r i}\nabla_{\zeta}^{t}\big(W{}_{\eta \gamma}\big)W{}_{\alpha \beta}{}^{\gamma j}\\
&-\frac{3}{16}W{}_{a b}(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r i}W{}_{\eta \gamma}\nabla_{\zeta}^{t}\big(W{}_{\alpha \beta}{}^{\gamma j}\big) -\frac{9}{32}\nabla_{\zeta}^{t}\big(W{}_{a b}\big)(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r i}W{}_{\alpha \beta}X{}_{\eta}{}^{j}\\
&-\frac{9}{32}W{}_{a b}(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r i}\nabla_{\zeta}^{t}\big(W{}_{\alpha \beta}\big)X{}_{\eta}{}^{j} -\frac{9}{32}W{}_{a b}(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r i}W{}_{\alpha \beta}\nabla_{\zeta}^{t}\big(X{}_{\eta}{}^{j}\big)\\
&+\frac{3}{8}\nabla_{\zeta}^{t}\big(W{}_{a b}\big)(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r i}(\Gamma{}^{c}){}_{\eta}{}^{\gamma}\big(\nabla_{c}W{}_{\alpha \beta \gamma}{}^{j}\big) +\frac{3}{8}W{}_{a b}(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r i}(\Gamma{}^{c}){}_{\eta}{}^{\gamma}\nabla_{\zeta}^{t}\big(\nabla_{c}W{}_{\alpha \beta \gamma}{}^{j}\big)\\
&-\frac{9}{32}\nabla_{\zeta}^{t}\big(W{}_{a b}\big)(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r i}W{}_{\alpha}{}^{\gamma}W{}_{\beta \eta \gamma}{}^{j} -\frac{9}{32}W{}_{a b}(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r i}\nabla_{\zeta}^{t}\big(W{}_{\alpha}{}^{\gamma}\big)W{}_{\beta \eta \gamma}{}^{j}\\
&-\frac{9}{32}W{}_{a b}(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r i}W{}_{\alpha}{}^{\gamma}\nabla_{\zeta}^{t}\big(W{}_{\beta \eta \gamma}{}^{j}\big) -\frac{3}{32}\nabla_{\zeta}^{t}\big(W{}_{a b}\big)(\Sigma{}^{a b}){}_{\eta}{}^{\alpha}\varepsilon{}^{r i}W{}^{\beta \gamma}W{}_{\alpha \beta \gamma}{}^{j}\\
&-\frac{3}{32}W{}_{a b}(\Sigma{}^{a b}){}_{\eta}{}^{\alpha}\varepsilon{}^{r i}\nabla_{\zeta}^{t}\big(W{}^{\beta \gamma}\big)W{}_{\alpha \beta \gamma}{}^{j} -\frac{3}{32}W{}_{a b}(\Sigma{}^{a b}){}_{\eta}{}^{\alpha}\varepsilon{}^{r i}W{}^{\beta \gamma}\nabla_{\zeta}^{t}\big(W{}_{\alpha \beta \gamma}{}^{j}\big)\\
&+\frac{3}{64}\nabla_{\zeta}^{t}\big(W{}_{a b}\big)(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r i}W{}_{\eta \alpha}X{}_{\beta}{}^{j} +\frac{3}{64}W{}_{a b}(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r i}\nabla_{\zeta}^{t}\big(W{}_{\eta \alpha}\big)X{}_{\beta}{}^{j}\\
&+\frac{3}{64}W{}_{a b}(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r i}W{}_{\eta \alpha}\nabla_{\zeta}^{t}\big(X{}_{\beta}{}^{j}\big) +\frac{9}{64}\nabla_{\zeta}^{t}\big(W{}_{a b}\big)(\Sigma{}^{a b}){}_{\eta}{}^{\alpha}\varepsilon{}^{r i}W{}_{\alpha \beta}X{}^{\beta j}\\
&+\frac{9}{64}W{}_{a b}(\Sigma{}^{a b}){}_{\eta}{}^{\alpha}\varepsilon{}^{r i}\nabla_{\zeta}^{t}\big(W{}_{\alpha \beta}\big)X{}^{\beta j} +\frac{9}{64}W{}_{a b}(\Sigma{}^{a b}){}_{\eta}{}^{\alpha}\varepsilon{}^{r i}W{}_{\alpha \beta}\nabla_{\zeta}^{t}\big(X{}^{\beta j}\big)\\
&+\frac{3}{16}\nabla_{\zeta}^{t}\big(W{}_{a b}\big)(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r i}(\Gamma{}^{c}){}_{\alpha}{}^{\gamma}\big(\nabla_{c}W{}_{\beta \eta \gamma}{}^{j}\big) +\frac{3}{16}W{}_{a b}(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r i}(\Gamma{}^{c}){}_{\alpha}{}^{\gamma}\nabla_{\zeta}^{t}\big(\nabla_{c}W{}_{\beta \eta \gamma}{}^{j}\big)\\
&-\frac{3}{32}\nabla_{\zeta}^{t}\big(W{}_{a b}\big)(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r i}(\Gamma{}^{c}){}_{\eta \alpha}\big(\nabla_{c}X{}_{\beta}{}^{j}\big) -\frac{3}{32}W{}_{a b}(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r i}(\Gamma{}^{c}){}_{\eta \alpha}\nabla_{\zeta}^{t}\big(\nabla_{c}X{}_{\beta}{}^{j}\big)\\
&+\frac{3}{32}\nabla_{\zeta}^{t}\big(W{}_{a b}\big)(\Sigma{}^{a b}){}_{\eta}{}^{\alpha}\varepsilon{}^{r i}(\Gamma{}^{c}){}_{\alpha \beta}\big(\nabla_{c}X{}^{\beta j}\big) +\frac{3}{32}W{}_{a b}(\Sigma{}^{a b}){}_{\eta}{}^{\alpha}\varepsilon{}^{r i}(\Gamma{}^{c}){}_{\alpha \beta}\nabla_{\zeta}^{t}\big(\nabla_{c}X{}^{\beta j}\big)\\
&-\frac{9}{32}\nabla_{\zeta}^{t}\big(W{}_{a b}\big)(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r i}W{}_{\beta}{}^{\gamma}W{}_{\alpha \eta \gamma}{}^{j} -\frac{9}{32}W{}_{a b}(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r i}\nabla_{\zeta}^{t}\big(W{}_{\beta}{}^{\gamma}\big)W{}_{\alpha \eta \gamma}{}^{j}\\
&-\frac{9}{32}W{}_{a b}(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r i}W{}_{\beta}{}^{\gamma}\nabla_{\zeta}^{t}\big(W{}_{\alpha \eta \gamma}{}^{j}\big) -\frac{3}{32}\nabla_{\zeta}^{t}\big(W{}_{a b}\big)(\Sigma{}^{a b}){}^{\alpha}{}_{\eta}\varepsilon{}^{r i}W{}^{\beta \gamma}W{}_{\alpha \beta \gamma}{}^{j}\\
&-\frac{3}{32}W{}_{a b}(\Sigma{}^{a b}){}^{\alpha}{}_{\eta}\varepsilon{}^{r i}\nabla_{\zeta}^{t}\big(W{}^{\beta \gamma}\big)W{}_{\alpha \beta \gamma}{}^{j} -\frac{3}{32}W{}_{a b}(\Sigma{}^{a b}){}^{\alpha}{}_{\eta}\varepsilon{}^{r i}W{}^{\beta \gamma}\nabla_{\zeta}^{t}\big(W{}_{\alpha \beta \gamma}{}^{j}\big)\\
&+\frac{3}{64}\nabla_{\zeta}^{t}\big(W{}_{a b}\big)(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r i}W{}_{\eta \beta}X{}_{\alpha}{}^{j} +\frac{3}{64}W{}_{a b}(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r i}\nabla_{\zeta}^{t}\big(W{}_{\eta \beta}\big)X{}_{\alpha}{}^{j}\\
&+\frac{3}{64}W{}_{a b}(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r i}W{}_{\eta \beta}\nabla_{\zeta}^{t}\big(X{}_{\alpha}{}^{j}\big) +\frac{9}{64}\nabla_{\zeta}^{t}\big(W{}_{a b}\big)(\Sigma{}^{a b}){}^{\alpha}{}_{\eta}\varepsilon{}^{r i}W{}_{\alpha \beta}X{}^{\beta j}\\
&+\frac{9}{64}W{}_{a b}(\Sigma{}^{a b}){}^{\alpha}{}_{\eta}\varepsilon{}^{r i}\nabla_{\zeta}^{t}\big(W{}_{\alpha \beta}\big)X{}^{\beta j} +\frac{9}{64}W{}_{a b}(\Sigma{}^{a b}){}^{\alpha}{}_{\eta}\varepsilon{}^{r i}W{}_{\alpha \beta}\nabla_{\zeta}^{t}\big(X{}^{\beta j}\big)\\
&+\frac{3}{16}\nabla_{\zeta}^{t}\big(W{}_{a b}\big)(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r i}(\Gamma{}^{c}){}_{\beta}{}^{\gamma}\big(\nabla_{c}W{}_{\alpha \eta \gamma}{}^{j}\big) +\frac{3}{16}W{}_{a b}(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r i}(\Gamma{}^{c}){}_{\beta}{}^{\gamma}\nabla_{\zeta}^{t}\big(\nabla_{c}W{}_{\alpha \eta \gamma}{}^{j}\big)\\
&-\frac{3}{32}\nabla_{\zeta}^{t}\big(W{}_{a b}\big)(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r i}(\Gamma{}^{c}){}_{\eta \beta}\big(\nabla_{c}X{}_{\alpha}{}^{j}\big) -\frac{3}{32}W{}_{a b}(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r i}(\Gamma{}^{c}){}_{\eta \beta}\nabla_{\zeta}^{t}\big(\nabla_{c}X{}_{\alpha}{}^{j}\big)\\
&+\frac{3}{32}\nabla_{\zeta}^{t}\big(W{}_{a b}\big)(\Sigma{}^{a b}){}^{\alpha}{}_{\eta}\varepsilon{}^{r i}(\Gamma{}^{c}){}_{\alpha \beta}\big(\nabla_{c}X{}^{\beta j}\big) +\frac{3}{32}W{}_{a b}(\Sigma{}^{a b}){}^{\alpha}{}_{\eta}\varepsilon{}^{r i}(\Gamma{}^{c}){}_{\alpha \beta}\nabla_{\zeta}^{t}\big(\nabla_{c}X{}^{\beta j}\big)\\
&-\frac{3}{16}\nabla_{\zeta}^{t}\big(W{}_{a b}\big)(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r j}W{}_{\eta \gamma}W{}_{\alpha \beta}{}^{\gamma i} -\frac{3}{16}W{}_{a b}(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r j}\nabla_{\zeta}^{t}\big(W{}_{\eta \gamma}\big)W{}_{\alpha \beta}{}^{\gamma i}\\
&-\frac{3}{16}W{}_{a b}(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r j}W{}_{\eta \gamma}\nabla_{\zeta}^{t}\big(W{}_{\alpha \beta}{}^{\gamma i}\big) -\frac{9}{32}\nabla_{\zeta}^{t}\big(W{}_{a b}\big)(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r j}W{}_{\alpha \beta}X{}_{\eta}{}^{i}\\
&-\frac{9}{32}W{}_{a b}(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r j}\nabla_{\zeta}^{t}\big(W{}_{\alpha \beta}\big)X{}_{\eta}{}^{i} -\frac{9}{32}W{}_{a b}(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r j}W{}_{\alpha \beta}\nabla_{\zeta}^{t}\big(X{}_{\eta}{}^{i}\big)\\
&+\frac{3}{8}\nabla_{\zeta}^{t}\big(W{}_{a b}\big)(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r j}(\Gamma{}^{c}){}_{\eta}{}^{\gamma}\big(\nabla_{c}W{}_{\alpha \beta \gamma}{}^{i}\big) +\frac{3}{8}W{}_{a b}(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r j}(\Gamma{}^{c}){}_{\eta}{}^{\gamma}\nabla_{\zeta}^{t}\big(\nabla_{c}W{}_{\alpha \beta \gamma}{}^{i}\big)\\
&-\frac{9}{32}\nabla_{\zeta}^{t}\big(W{}_{a b}\big)(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r j}W{}_{\alpha}{}^{\gamma}W{}_{\beta \eta \gamma}{}^{i} -\frac{9}{32}W{}_{a b}(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r j}\nabla_{\zeta}^{t}\big(W{}_{\alpha}{}^{\gamma}\big)W{}_{\beta \eta \gamma}{}^{i}\\
&-\frac{9}{32}W{}_{a b}(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r j}W{}_{\alpha}{}^{\gamma}\nabla_{\zeta}^{t}\big(W{}_{\beta \eta \gamma}{}^{i}\big) -\frac{3}{32}\nabla_{\zeta}^{t}\big(W{}_{a b}\big)(\Sigma{}^{a b}){}_{\eta}{}^{\alpha}\varepsilon{}^{r j}W{}^{\beta \gamma}W{}_{\alpha \beta \gamma}{}^{i}\\
&-\frac{3}{32}W{}_{a b}(\Sigma{}^{a b}){}_{\eta}{}^{\alpha}\varepsilon{}^{r j}\nabla_{\zeta}^{t}\big(W{}^{\beta \gamma}\big)W{}_{\alpha \beta \gamma}{}^{i} -\frac{3}{32}W{}_{a b}(\Sigma{}^{a b}){}_{\eta}{}^{\alpha}\varepsilon{}^{r j}W{}^{\beta \gamma}\nabla_{\zeta}^{t}\big(W{}_{\alpha \beta \gamma}{}^{i}\big)\\
&+\frac{3}{64}\nabla_{\zeta}^{t}\big(W{}_{a b}\big)(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r j}W{}_{\eta \alpha}X{}_{\beta}{}^{i} +\frac{3}{64}W{}_{a b}(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r j}\nabla_{\zeta}^{t}\big(W{}_{\eta \alpha}\big)X{}_{\beta}{}^{i}\\
&+\frac{3}{64}W{}_{a b}(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r j}W{}_{\eta \alpha}\nabla_{\zeta}^{t}\big(X{}_{\beta}{}^{i}\big) +\frac{9}{64}\nabla_{\zeta}^{t}\big(W{}_{a b}\big)(\Sigma{}^{a b}){}_{\eta}{}^{\alpha}\varepsilon{}^{r j}W{}_{\alpha \beta}X{}^{\beta i}\\
&+\frac{9}{64}W{}_{a b}(\Sigma{}^{a b}){}_{\eta}{}^{\alpha}\varepsilon{}^{r j}\nabla_{\zeta}^{t}\big(W{}_{\alpha \beta}\big)X{}^{\beta i} +\frac{9}{64}W{}_{a b}(\Sigma{}^{a b}){}_{\eta}{}^{\alpha}\varepsilon{}^{r j}W{}_{\alpha \beta}\nabla_{\zeta}^{t}\big(X{}^{\beta i}\big)\\
&+\frac{3}{16}\nabla_{\zeta}^{t}\big(W{}_{a b}\big)(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r j}(\Gamma{}^{c}){}_{\alpha}{}^{\gamma}\big(\nabla_{c}W{}_{\beta \eta \gamma}{}^{i}\big) +\frac{3}{16}W{}_{a b}(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r j}(\Gamma{}^{c}){}_{\alpha}{}^{\gamma}\nabla_{\zeta}^{t}\big(\nabla_{c}W{}_{\beta \eta \gamma}{}^{i}\big)\\
&-\frac{3}{32}\nabla_{\zeta}^{t}\big(W{}_{a b}\big)(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r j}(\Gamma{}^{c}){}_{\eta \alpha}\big(\nabla_{c}X{}_{\beta}{}^{i}\big) -\frac{3}{32}W{}_{a b}(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r j}(\Gamma{}^{c}){}_{\eta \alpha}\nabla_{\zeta}^{t}\big(\nabla_{c}X{}_{\beta}{}^{i}\big)\\
&+\frac{3}{32}\nabla_{\zeta}^{t}\big(W{}_{a b}\big)(\Sigma{}^{a b}){}_{\eta}{}^{\alpha}\varepsilon{}^{r j}(\Gamma{}^{c}){}_{\alpha \beta}\big(\nabla_{c}X{}^{\beta i}\big) +\frac{3}{32}W{}_{a b}(\Sigma{}^{a b}){}_{\eta}{}^{\alpha}\varepsilon{}^{r j}(\Gamma{}^{c}){}_{\alpha \beta}\nabla_{\zeta}^{t}\big(\nabla_{c}X{}^{\beta i}\big)\\
&-\frac{9}{32}\nabla_{\zeta}^{t}\big(W{}_{a b}\big)(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r j}W{}_{\beta}{}^{\gamma}W{}_{\alpha \eta \gamma}{}^{i} -\frac{9}{32}W{}_{a b}(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r j}\nabla_{\zeta}^{t}\big(W{}_{\beta}{}^{\gamma}\big)W{}_{\alpha \eta \gamma}{}^{i}\\
&-\frac{9}{32}W{}_{a b}(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r j}W{}_{\beta}{}^{\gamma}\nabla_{\zeta}^{t}\big(W{}_{\alpha \eta \gamma}{}^{i}\big) -\frac{3}{32}\nabla_{\zeta}^{t}\big(W{}_{a b}\big)(\Sigma{}^{a b}){}^{\alpha}{}_{\eta}\varepsilon{}^{r j}W{}^{\beta \gamma}W{}_{\alpha \beta \gamma}{}^{i}\\
&-\frac{3}{32}W{}_{a b}(\Sigma{}^{a b}){}^{\alpha}{}_{\eta}\varepsilon{}^{r j}\nabla_{\zeta}^{t}\big(W{}^{\beta \gamma}\big)W{}_{\alpha \beta \gamma}{}^{i} -\frac{3}{32}W{}_{a b}(\Sigma{}^{a b}){}^{\alpha}{}_{\eta}\varepsilon{}^{r j}W{}^{\beta \gamma}\nabla_{\zeta}^{t}\big(W{}_{\alpha \beta \gamma}{}^{i}\big)\\
&+\frac{3}{64}\nabla_{\zeta}^{t}\big(W{}_{a b}\big)(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r j}W{}_{\eta \beta}X{}_{\alpha}{}^{i} +\frac{3}{64}W{}_{a b}(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r j}\nabla_{\zeta}^{t}\big(W{}_{\eta \beta}\big)X{}_{\alpha}{}^{i}\\
&+\frac{3}{64}W{}_{a b}(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r j}W{}_{\eta \beta}\nabla_{\zeta}^{t}\big(X{}_{\alpha}{}^{i}\big) +\frac{9}{64}\nabla_{\zeta}^{t}\big(W{}_{a b}\big)(\Sigma{}^{a b}){}^{\alpha}{}_{\eta}\varepsilon{}^{r j}W{}_{\alpha \beta}X{}^{\beta i}\\
&+\frac{9}{64}W{}_{a b}(\Sigma{}^{a b}){}^{\alpha}{}_{\eta}\varepsilon{}^{r j}\nabla_{\zeta}^{t}\big(W{}_{\alpha \beta}\big)X{}^{\beta i} +\frac{9}{64}W{}_{a b}(\Sigma{}^{a b}){}^{\alpha}{}_{\eta}\varepsilon{}^{r j}W{}_{\alpha \beta}\nabla_{\zeta}^{t}\big(X{}^{\beta i}\big)\\
&+\frac{3}{16}\nabla_{\zeta}^{t}\big(W{}_{a b}\big)(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r j}(\Gamma{}^{c}){}_{\beta}{}^{\gamma}\big(\nabla_{c}W{}_{\alpha \eta \gamma}{}^{i}\big) +\frac{3}{16}W{}_{a b}(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r j}(\Gamma{}^{c}){}_{\beta}{}^{\gamma}\nabla_{\zeta}^{t}\big(\nabla_{c}W{}_{\alpha \eta \gamma}{}^{i}\big)\\
&-\frac{3}{32}\nabla_{\zeta}^{t}\big(W{}_{a b}\big)(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r j}(\Gamma{}^{c}){}_{\eta \beta}\big(\nabla_{c}X{}_{\alpha}{}^{i}\big) -\frac{3}{32}W{}_{a b}(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r j}(\Gamma{}^{c}){}_{\eta \beta}\nabla_{\zeta}^{t}\big(\nabla_{c}X{}_{\alpha}{}^{i}\big)\\
&+\frac{3}{32}\nabla_{\zeta}^{t}\big(W{}_{a b}\big)(\Sigma{}^{a b}){}^{\alpha}{}_{\eta}\varepsilon{}^{r j}(\Gamma{}^{c}){}_{\alpha \beta}\big(\nabla_{c}X{}^{\beta i}\big) +\frac{3}{32}W{}_{a b}(\Sigma{}^{a b}){}^{\alpha}{}_{\eta}\varepsilon{}^{r j}(\Gamma{}^{c}){}_{\alpha \beta}\nabla_{\zeta}^{t}\big(\nabla_{c}X{}^{\beta i}\big)
\end{aligned}
\tag{S4-H0.1-product}
```

[Component index](../STEP_04_LOG_SCALAR.md) · [Next component](derivation_002.md)
