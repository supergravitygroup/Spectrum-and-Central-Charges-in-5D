# LOG vector descent — S5-V01 – S5-I-D-RK-3

<a id="step-5--deriving-the-log-vector--definitions-and-conventions"></a>

[Component index](../STEP_05_LOG_VECTOR.md).

---
title: "Step 5 — LOG vector through two explicit fermions"
date: 2026-09-23
status: "Explicit covariant descent through two fermions; retained multiplet and current/BF interface certified separately"
procedure: GAUGED-LOG-G25-S23-PROCEDURE-v1
fermion_order: "zero and two explicit fermions; higher orders represented by + high fermi term"
---

## Step 5 — deriving the LOG vector

<!-- LOG_CURRENT_CERTIFICATION_20260925 -->

**Current scope:** [the 2026-09-25 certificate](../CERTIFICATION_LOG_TWO_FERMI_2026-09-25.md) verifies the full primary and the component action through two physical fermions. The source comparisons and restricted tests below retain their stated mathematical scope.

**Source-algebra repair, 2026-09-25.** This rebuilt result includes the two factors of $`i`$ required in the K-generator part of C24 (A.1l). The printed source is preserved, and the correction is established by the independent SDD super-Jacobi certificate. See [the full certification record](../../../../../../../references/source_evidence/README.md).

**Derivative notation.** This stage uses the full Gold superspace $`\nabla_A`$. Step 6 transports it to the full project $`\mathcal D_a`$ and $`\Box^c=\mathcal D^a\mathcal D_a`$, including Q/S/K connections, as in the fermionic Weyl-squared calculation. No connection-only derivative replaces it.

## 1. Problem and Target

We calculate the vector by differentiating the **calculated spinor**, retaining the zero- and two-explicit-fermion contributions. Its input is [STEP_03_LOG_SPINOR.md](../STEP_03_LOG_SPINOR.md), derived from the 58-term primary in [STEP_02_LOG_PRIMARY.md](../STEP_02_LOG_PRIMARY.md), Eq. (S2-193). The coefficient of primary term H3.9 remains the derived $`+i/4`$, not the printed $`-i/4`$. The scalar in [STEP_04_LOG_SCALAR.md](../STEP_04_LOG_SCALAR.md) supplies an independent trace check; taking a derivative of that scalar would not recover the vector.

S23 (3.26a,c), [On curvature-squared invariants of minimal five-dimensional supergravity from superspace — PDF22](https://arxiv.org/abs/2302.14295), give

```math
\varphi_{\log W\,\beta}^{i}=\frac13\nabla_{\beta j}H_{\log W}^{ij},\qquad
\mathcal H_{\log W}^{a}=\frac{i}{12}(\Gamma^a)^{\alpha\beta}\nabla_{\alpha i}\nabla_{\beta j}H_{\log W}^{ij}
=\frac i4(\Gamma^a)^{\alpha\beta}\nabla_{\alpha i}\varphi_{\log W\,\beta}^{i}.
\tag{S5-V01}
```

This is the vector **superfield** in Gold's traceless Standard-Weyl superspace, at the same stage as our primary, spinor and scalar. Component projection and the Gold-to-project conversion are performed together in the [Step 6 component projection](../STEP_06_LOG_PROJECTED_MULTIPLET_AND_BOSONIC_ACTION.md). The component constraint is displayed separately in §5 to explain what the vector must satisfy after projection; it does not change the frame of the final expression.

**A1.** The calculation is classical, five dimensional and off shell. **A2.** We work on the scalar patch $`W>0`$. **A3.** We impose no field equation, gauge fixing, auxiliary elimination or background restriction. **A4.** All equalities are local; no integration by parts or total-derivative equivalence is used. **A5.** The specified truncation counts the explicitly written odd fields after descent. It is an algebraic fermion-degree expansion, not a small-coupling approximation or a numerical error estimate. **A6.** Restricted field assignments occur only in checks, after differentiation.

The endpoint contains every retained contribution with its indices, coefficients and ordered vector derivatives. It is a nonminimal tensor expression: Clifford/Fierz reductions and cancellations into Gold's shorter published basis are not claimed. There are no unevaluated **spinor** derivatives or generator actions in the endpoint. The conventional superspace torsion and curvatures retain the definitions displayed below. Consecutive blocks at the end continue one equality, with two summands per row and the final remainder written exactly as $`+\text{high fermi term}`$.

## 2. Convention Ledger

<!-- ASSERT_CONVENTION: source_frame=Gold traceless Standard-Weyl superspace, metric_signature=(-,+,+,+,+), natural_units=hbar=c=1, derivative_parity=odd left, fermions=explicit degree zero and two after descent, regularization_scheme=Not applicable for initial classical analysis, renormalization_scheme=Not applicable for initial classical analysis -->

The controlling files are [CONVENTIONS.md](../CONVENTIONS.md) and [LOG_CONVENTIONS.md](../LOG_CONVENTIONS.md).

| Item | Convention used here |
|---|---|
| Indices | $`a,b=0,\ldots,4`$; $`\alpha,\beta=1,\ldots,4`$; $`i,j=1,2`$ |
| Metric and orientation | $`\eta=(-,+,+,+,+)`$; $`\varepsilon^{01234}=-1`$, $`\varepsilon_{01234}=+1`$ |
| Clifford algebra | $`\{\Gamma^a,\Gamma^b\}=-2\eta^{ab}`$; $`\Sigma^{ab}=-[\Gamma^a,\Gamma^b]/4`$ |
| Spinor metric | $`\zeta^\alpha=\varepsilon^{\alpha\beta}\zeta_\beta`$, $`\varepsilon^{\alpha\gamma}\varepsilon_{\gamma\beta}=\delta^\alpha{}_{\beta}`$ |
| Doublet metric | $`\zeta_i=\varepsilon_{ij}\zeta^j`$, $`\varepsilon^{12}=\varepsilon_{21}=1`$ |
| Symmetrization | Unit weight; the actual $`i,j`$ averages are displayed as separate terms below |
| Odd fields | $`\lambda_\alpha^i`$, $`X_\alpha^i`$, $`W_{\alpha\beta\gamma}{}^i`$, their vector derivatives, and the spinorial components of $`\mathcal R(M),\mathcal R(J),\mathcal R(\mathbb D),\mathcal R(K)`$ |
| Even fields | $`W`$, $`X^{ij}`$, $`F_{ab}`$, $`W_{ab}`$, $`Y`$, $`X_{\alpha\beta}^{ij}`$, $`W_{\alpha\beta\gamma\delta}`$, $`\mathcal T_{a\alpha}{}^\beta`$, $`\mathcal R(S)_{a\alpha}{}^{i\beta j}`$ |
| Grassmann rule | Left odd derivatives; written odd-factor order retained; no implicit spinor flip |
| Reality | Gold's symplectic reality. No complex conjugation or Majorana flip is used to shorten the endpoint; retained-component reality is certified in the later audit |
| Curvature sign | $`[\nabla_A,\nabla_B\}=-\mathcal T_{AB}{}^C\nabla_C-\tfrac12\mathcal R(M)_{AB}{}^{cd}M_{cd}-\mathcal R(J)_{AB}{}^{kl}J_{kl}-\mathcal R(\mathbb D)_{AB}\mathbb D-\mathcal R(S)_{AB}{}^{\gamma k}S_{\gamma k}-\mathcal R(K)_{AB}{}^cK_c`$ |
| Derivatives | Full superconformal $`\nabla_A`$; $`\Box=\nabla^a\nabla_a`$; vector derivative order is never silently commuted |
| Couplings | No action coefficient or gauging substitution enters this descendant. The later action retains $`[\lambda_{\rm LOG}]=-2`$ |

The scalar $`W`$ is different from the Weyl two-form $`W_{ab}`$. The vector auxiliary $`X^{ij}`$ is different from the Weyl descendants $`X_\alpha^i`$ and $`X_{\alpha\beta}^{ij}`$. No Ricci scalar or Levi–Civita curvature is introduced here; the curvature convention is specified by the commutator in the table. No Fourier transform, quantum-state normalization, boundary condition, chirality projection or renormalization scheme is needed for this local classical calculation.

### 2.1 The trace sign, with every raising/lowering factor

First lower the derivative's doublet index, then substitute the spinor:

```math
\begin{aligned}
\nabla_{\zeta i}\varphi_\eta^i
&=\varepsilon_{it}\nabla_\zeta^t\varphi_\eta^i
=\frac13\varepsilon_{it}\varepsilon_{jr}\nabla_\zeta^t\nabla_\eta^rH^{ij},\\
\mathcal H^a_{\log W}
&=\frac i{12}(\Gamma^a)^{\zeta\eta}\varepsilon_{it}\varepsilon_{jr}\nabla_\zeta^t\nabla_\eta^rH^{ij}
=-\frac i{12}(\Gamma^a)^{\zeta\eta}\varepsilon_{ti}\varepsilon_{jr}\nabla_\zeta^t\nabla_\eta^rH^{ij}.
\end{aligned}
\tag{S5-V02}
```

The last sign uses only $`\varepsilon_{it}=-\varepsilon_{ti}`$, with **no interchange of odd derivatives**. In particular, the order of the spinor indices on the gamma matrix is $`\zeta,\eta`$. For comparison, our scalar trace uses $`-i\varepsilon^{\eta\zeta}/12`$ with the same $`\varepsilon_{ti}\varepsilon_{jr}`$; replacing it without accounting for this order would be a sign error.

The generic linear-multiplet identity is C24 (2.41b), [Components of curvature-squared invariants of minimal supergravity in five dimensions — PDF20](https://arxiv.org/abs/2311.00679):

```math
\nabla_\zeta^t\varphi_\eta^i
=-\frac i2\varepsilon^{ti}\varepsilon_{\zeta\eta}F
+\frac i2\varepsilon^{ti}(\Gamma^b)_{\zeta\eta}\mathcal H_b
+i(\Gamma^b)_{\zeta\eta}\nabla_bH^{ti}.
\tag{S5-V03}
```

With the locked metrics, the contractions are

```math
\varepsilon_{it}\varepsilon^{ti}=2,\qquad
(\Gamma^a)^{\zeta\eta}\varepsilon_{\zeta\eta}=0,\qquad
(\Gamma^a)^{\zeta\eta}(\Gamma^b)_{\zeta\eta}=-4\eta^{ab},\qquad
\varepsilon_{it}H^{ti}=0.
\tag{S5-V04}
```

The last equality contracts an antisymmetric doublet metric with a symmetric triplet. The gamma trace follows from the Clifford algebra and spinor raising: its same-slot contraction equals $`\mathop{\mathrm{tr}}\nolimits(\Gamma^a\Gamma^b)=-4\eta^{ab}`$. This is also checked with the explicit four-by-four Clifford matrices used in the preceding scalar calculation, for all 25 pairs $`a,b`$.

Insert (S5-V03) into (S5-V01). The scalar term vanishes by the second identity in (S5-V04), the triplet term vanishes by the last identity, and the remaining coefficient is

```math
\frac i4\frac i2\,(2)(-4)\eta^{ab}\mathcal H_b=\mathcal H^a.
\tag{S5-V05}
```

### 2.2 Why the cubic spinor and quartic primary are needed

An odd derivative can replace an odd field by an even one, reducing explicit fermion degree by one; it can also replace an even field by an odd one, increasing it by one. The derivative identities below show those possibilities directly. The geometric tensors used here have homogeneous explicit degree: $`\mathcal T`$ and $`\mathcal R(S)`$ have degree zero, and the other displayed mixed curvatures have degree one.

Consequently a term of degree $`q`$ in the primary can first contribute to degree $`q-2`$ in the vector. The required bookkeeping is

```math
\begin{aligned}
H^{ij}:&\quad q=0,2,4\ \longrightarrow\ \mathcal H^a:\ q=0,2,\ldots,\\
H^{ij}:&\quad q\ge6\ \longrightarrow\ \mathcal H^a:\ q\ge4,\\
\varphi_\alpha^i:&\quad q=1,3\ \longrightarrow\ \mathcal H^a:\ q=0,2,4.
\end{aligned}
\tag{S5-V06}
```

We therefore differentiate the full primary and retain the complete linear and cubic spinor contributions. Only **after the next derivative is evaluated** do we select degree zero and two. The verification independently compares this with differentiating the full spinor first and truncating last, input by input. The two sextic primary inputs H6.1 and H6.2 have zero retained contribution, by the second line of (S5-V06).

This degree counts explicit covariant fermion fields. Full covariant derivatives and their connections are retained; it is not a claim to have expanded every gravitino hidden inside all component supercovariant objects. The specified $`\text{high fermi term}`$ means terms with at least four such explicit fermions. It does not represent omitted bosonic or bilinear terms and does not have a numerical norm bound.

## 3. Definitions and Required Identities

The following identities are the same source equations already used for the spinor and scalar descents, displayed here so the second derivative can be followed in this file. Source anchors: S23 (2.5)–(2.6), (2.8), (2.12)–(2.13); C24 (2.29)–(2.30), Appendix A (A.1) and (A.3). Their cached pages are [S23 PDF9](https://arxiv.org/abs/2302.14295), [On curvature-squared invariants of minimal five-dimensional supergravity from superspace — PDF10](https://arxiv.org/abs/2302.14295), [On curvature-squared invariants of minimal five-dimensional supergravity from superspace — PDF11](https://arxiv.org/abs/2302.14295), and [C24 PDF81](https://arxiv.org/abs/2311.00679), [Components of curvature-squared invariants of minimal supergravity in five dimensions — PDF82](https://arxiv.org/abs/2311.00679), [Components of curvature-squared invariants of minimal supergravity in five dimensions — PDF83](https://arxiv.org/abs/2311.00679).

The full derivative, including the inhomogeneous dilatation action on the original logarithm, is

```math
\nabla_A=E_A-\frac12\Omega_A{}^{ab}M_{ab}-\Phi_A{}^{ij}J_{ij}-B_A\mathbb D-\mathfrak F_A{}^{\alpha i}S_{\alpha i}-\mathfrak F_A{}^aK_a,\qquad
\mathbb DW=W,\qquad \mathbb D\log W=1.
\tag{S5-V07}
```

No new logarithm differentiation is needed after the already calculated primary. Its exact homogeneous weight three is preserved by the two descents to weight four.

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
\tag{S5-I-I-WEYL}
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
\tag{S5-I-I-VECTOR}
```

For example, expansion of the weighted SU(2) average in the vector rule gives

```math
\begin{aligned}
\nabla_\eta^rX^{ij}={}&i\varepsilon^{ri}(\Gamma^a)_\eta{}^\beta\nabla_a\lambda_\beta^j+i\varepsilon^{rj}(\Gamma^a)_\eta{}^\beta\nabla_a\lambda_\beta^i\\
&-\tfrac i2\varepsilon^{ri}W_{\eta\beta}\lambda^{\beta j}-\tfrac i2\varepsilon^{rj}W_{\eta\beta}\lambda^{\beta i}-\tfrac34\varepsilon^{ri}X_\eta^jW-\tfrac34\varepsilon^{rj}X_\eta^iW.
\end{aligned}
\tag{S5-I-I-04}
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
\tag{S5-I-I-05}
```

The entire $`K`$ curvature, including the three terms continued onto PDF83, is

```math
\begin{aligned}
\mathcal R(K)_{a\eta}{}^{rb}={}&\tfrac16(\Gamma^b)_\eta{}^\beta\nabla^cW_{ca\beta}{}^r+\tfrac1{12}(\Gamma_a)_\eta{}^\beta\nabla^cW_c{}^b{}_{\beta}{}^r+\tfrac16\nabla_\eta{}^\beta W_a{}^b{}_{\beta}{}^r-\tfrac1{24}\varepsilon_a{}^{bcde}\nabla_cW_{de\eta}{}^r\\
&+\tfrac18(\Gamma^b)_\eta{}^\beta\nabla_aX_\beta^r+\tfrac1{64}W^{cd}(3\Gamma_a\Sigma_{cd}\Gamma^b-\Sigma_{cd}\Gamma_a\Gamma^b)_\eta{}^\beta X_\beta^r-\tfrac1{48}\widetilde W_{acd}(\Gamma^b)_\eta{}^\beta W^{cd}{}_{\beta}{}^r\\
&+\tfrac18\delta_a{}^bW^{cd}W_{cd\eta}{}^r+\tfrac1{12}(\Sigma_a{}^b)_\eta{}^\beta W_{cd\beta}{}^rW^{cd}-\tfrac1{12}W^{cd}(\Sigma_{cd})_\eta{}^\beta W_a{}^b{}_{\beta}{}^r\\
&+\tfrac{13}{48}W_{ac}W^{cb}{}_{\eta}{}^r+\tfrac{11}{48}W_{ac\eta}{}^rW^{cb}-\tfrac{13}{96}(\Gamma_a)_\eta{}^\beta W_{cd\beta}{}^r\widetilde W^{cdb}.
\end{aligned}
\tag{S5-I-I-06}
```

Thus retaining $`\mathcal R(K)`$ does not mean setting its fermions to zero or using an unspecified remainder. It denotes this exact source tensor. Its vector derivatives in the vector formula are full covariant derivatives of this tensor. The geometric composites and their derivatives retain these exact covariant definitions.

### 3.3 Generator actions, with the SU(2) sign derived

The needed source actions are C24 (A.1), S23 (2.8), (2.15). For a lower spinor $`U_\beta`$, a lower vector $`U_a`$ and a doublet $`U^i`$,

```math
\begin{aligned}
M_{ab}U_\beta&=(\Sigma_{ab})_\beta{}^\gamma U_\gamma,\qquad M_{ab}U_c=\eta_{ca}U_b-\eta_{cb}U_a,\\
J^{kl}U^i&=\tfrac12(\varepsilon^{ik}U^l+\varepsilon^{il}U^k),\\
J_{kl}U^i&=\varepsilon_{km}\varepsilon_{ln}J^{mn}U^i
=-\tfrac12(\delta_k{}^i\varepsilon_{ln}+\delta_l{}^i\varepsilon_{kn})U^n.
\end{aligned}
\tag{S5-I-I-07}
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
\tag{S5-I-I-08}
```

The last identity applies to each elementary vector/Weyl descendant in this calculation, not to its vector derivatives. The weights are $`w(W)=w(W_{ab})=1`$, $`w(\lambda)=w(X_\alpha)=w(W_{\alpha\beta\gamma})=3/2`$, $`w(X^{ij})=w(F_{ab})=w(X_{ab}^{ij})=w(Y)=2`$; $`w(\nabla_a)=1`$, $`w(\nabla_\alpha^i)=1/2`$.

### 3.4 Higher descendants and the commutator on a derivative

The remaining elementary S actions follow from S23 (2.8); the full vector descent uses them when differentiating the spinor's Weyl descendants:

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
\tag{S5-I-04}
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
\tag{S5-I-05}
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
\tag{S5-I-06}
```

For more ordered vector derivatives this equation is applied to the outermost one, then the next one. The generator acts on **all** tensor indices, including derivative indices. Its actions are those displayed in (S5-I-I-07), (S5-I-I-08), (S5-I-04), and (S5-I-05). There is no replacement of a covariant derivative by a partial derivative.

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
\tag{S5-I-07}
```

The following evaluated rows supply the full substitutions for all six geometric tensors, including the longer Lorentz, S and K curvatures. Their free indices are the ones on the left. A prime, unnamed response tensor, or unevaluated spinor derivative is not introduced.

#### Spinor derivative of torsion

```math
\begin{aligned}
\nabla_\eta^r \mathcal T{}_{a \beta}{}^{\gamma}={}&\frac{3}{4}(\Gamma{}_{a}){}_{\beta}{}^{\alpha}W{}_{\eta \alpha}{}^{\gamma r} +\frac{3}{8}(\Gamma{}_{a}){}_{\beta \eta}X{}^{\gamma r}\\
&+\frac{3}{8}(\Gamma{}_{a}){}_{\beta}{}^{\alpha}\varepsilon{}^{\gamma \delta}\varepsilon{}_{\eta \delta}X{}_{\alpha}{}^{r} -\frac{1}{4}W{}_{\eta \beta}{}^{\alpha r}(\Gamma{}_{a}){}_{\alpha}{}^{\gamma}\\
&-\frac{1}{8}\varepsilon{}_{\eta \beta}X{}^{\alpha r}(\Gamma{}_{a}){}_{\alpha}{}^{\gamma} +\frac{1}{8}X{}_{\beta}{}^{r}(\Gamma{}_{a}){}_{\eta}{}^{\gamma}
\end{aligned}
\tag{S5-I-D-T}
```

#### Spinor derivative of dilatation curvature

```math
\begin{aligned}
\nabla_\eta^r \mathcal R(\mathbb D){}_{a \beta}{}^{i}={}&-\frac{1}{4}(\Gamma{}_{a}){}_{\beta}{}^{\alpha}X{}_{\eta \alpha}{}^{r i} -\frac{i}{32}(\Gamma{}_{a}){}_{\beta \eta}\varepsilon{}^{r i}Y\\
&+\frac{3i}{8}(\Gamma{}_{a}){}_{\beta}{}^{\alpha}\varepsilon{}^{r i}(\Gamma{}^{d}){}_{\eta}{}^{\delta}\big(\nabla_{d}W{}_{\alpha \delta}\big) +\frac{i}{2}(\Gamma{}_{a}){}_{\beta}{}^{\alpha}\varepsilon{}^{r i}W{}_{\eta}{}^{\delta}W{}_{\alpha \delta}\\
&-\frac{i}{8}(\Gamma{}_{a}){}_{\beta \eta}\varepsilon{}^{r i}W{}^{\alpha \delta}W{}_{\alpha \delta} +\frac{i}{8}(\Gamma{}_{a}){}_{\beta}{}^{\alpha}\varepsilon{}^{r i}(\Gamma{}^{d}){}_{\alpha}{}^{\delta}\big(\nabla_{d}W{}_{\eta \delta}\big)
\end{aligned}
\tag{S5-I-D-RD}
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
\tag{S5-I-D-RJ}
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
\tag{S5-I-D-RM}
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
\tag{S5-I-D-RS-1}
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
\tag{S5-I-D-RS-2}
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
\tag{S5-I-D-RK-1}
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
\tag{S5-I-D-RK-2}
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
\tag{S5-I-D-RK-3}
```

[Component index](../STEP_05_LOG_VECTOR.md) · [Next component](derivation_002.md)
