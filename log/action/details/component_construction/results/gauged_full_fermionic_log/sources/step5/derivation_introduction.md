---
title: "Step 5 — LOG vector through two explicit fermions"
date: 2026-09-23
status: "Explicit covariant descent through two fermions; retained multiplet and current/BF interface certified separately"
procedure: GAUGED-LOG-G25-S23-PROCEDURE-v1
fermion_order: "zero and two explicit fermions; higher orders represented by + high fermi term"
---

# Step 5 — deriving the LOG vector

<!-- LOG_CURRENT_CERTIFICATION_20260925 -->

**Current scope:** [the 2026-09-25 certificate](../../CERTIFICATION_LOG_TWO_FERMI_2026-09-25.md) verifies the full primary and the component action through two physical fermions. The source comparisons and restricted tests below retain their stated mathematical scope.

**Source-algebra repair, 2026-09-25.** This rebuilt result includes the two factors of $`i`$ required in the K-generator part of C24 (A.1l). The printed source is preserved, and the correction is established by the independent SDD super-Jacobi certificate. See [the full certification record](../../../../../../../../references/source_evidence/README.md).

**Derivative notation.** This stage uses the full Gold superspace $`\nabla_A`$. Step 6 transports it to the full project $`\mathcal D_a`$ and $`\Box^c=\mathcal D^a\mathcal D_a`$, including Q/S/K connections, as in the fermionic Weyl-squared calculation. No connection-only derivative replaces it.

## 1. Problem and Target

We calculate the vector by differentiating the **calculated spinor**, retaining the zero- and two-explicit-fermion contributions. Its input is [STEP_03_LOG_SPINOR.md](../../STEP_03_LOG_SPINOR.md), derived from the 58-term primary in [STEP_02_LOG_PRIMARY.md](../../STEP_02_LOG_PRIMARY.md), Eq. (S2-193). The coefficient of primary term H3.9 remains the derived $`+i/4`$, not the printed $`-i/4`$. The scalar in [STEP_04_LOG_SCALAR.md](../../STEP_04_LOG_SCALAR.md) supplies an independent trace check; taking a derivative of that scalar would not recover the vector.

S23 (3.26a,c), [On curvature-squared invariants of minimal five-dimensional supergravity from superspace — PDF22](https://arxiv.org/abs/2302.14295), give

```math
\varphi_{\log W\,\beta}^{i}=\frac13\nabla_{\beta j}H_{\log W}^{ij},\qquad
\mathcal H_{\log W}^{a}=\frac{i}{12}(\Gamma^a)^{\alpha\beta}\nabla_{\alpha i}\nabla_{\beta j}H_{\log W}^{ij}
=\frac i4(\Gamma^a)^{\alpha\beta}\nabla_{\alpha i}\varphi_{\log W\,\beta}^{i}.
\tag{S5-V01}
```

This is the vector **superfield** in Gold's traceless Standard-Weyl superspace, at the same stage as our primary, spinor and scalar. Component projection and the Gold-to-project conversion are performed together in the [Step 6 component projection](../../STEP_06_LOG_PROJECTED_MULTIPLET_AND_BOSONIC_ACTION.md). The component constraint is displayed separately in §5 to explain what the vector must satisfy after projection; it does not change the frame of the final expression.

**A1.** The calculation is classical, five dimensional and off shell. **A2.** We work on the scalar patch $`W>0`$. **A3.** We impose no field equation, gauge fixing, auxiliary elimination or background restriction. **A4.** All equalities are local; no integration by parts or total-derivative equivalence is used. **A5.** The specified truncation counts the explicitly written odd fields after descent. It is an algebraic fermion-degree expansion, not a small-coupling approximation or a numerical error estimate. **A6.** Restricted field assignments occur only in checks, after differentiation.

The endpoint contains every retained contribution with its indices, coefficients and ordered vector derivatives. It is a nonminimal tensor expression: Clifford/Fierz reductions and cancellations into Gold's shorter published basis are not claimed. There are no unevaluated **spinor** derivatives or generator actions in the endpoint. The conventional superspace torsion and curvatures retain the definitions displayed below. Consecutive blocks at the end continue one equality, with two summands per row and the final remainder written exactly as $`+\text{high fermi term}`$.

## 2. Convention Ledger

<!-- ASSERT_CONVENTION: source_frame=Gold traceless Standard-Weyl superspace, metric_signature=(-,+,+,+,+), natural_units=hbar=c=1, derivative_parity=odd left, fermions=explicit degree zero and two after descent, regularization_scheme=Not applicable for initial classical analysis, renormalization_scheme=Not applicable for initial classical analysis -->

The controlling files are [CONVENTIONS.md](../../CONVENTIONS.md) and [LOG_CONVENTIONS.md](../../LOG_CONVENTIONS.md).

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

