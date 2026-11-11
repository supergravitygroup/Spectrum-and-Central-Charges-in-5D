---
title: "Step 4 — LOG scalar from the calculated primary and spinor"
date: 2026-09-23
status: "Source-frame scalar descent; retained project-frame projection/reality and full-primary constraints certified separately"
procedure: GAUGED-LOG-G25-S23-PROCEDURE-v1
fermion_order: all
---

# Step 4 — deriving the LOG scalar superfield

<!-- LOG_CURRENT_CERTIFICATION_20260925 -->

**Current scope:** [the 2026-09-25 certificate](../../CERTIFICATION_LOG_TWO_FERMI_2026-09-25.md) verifies the full primary and the component action through two physical fermions. The source comparisons and restricted tests below retain their stated mathematical scope.

**Source-algebra repair, 2026-09-25.** This rebuilt result includes the two factors of $`i`$ required in the K-generator part of C24 (A.1l). The printed source is preserved, and the correction is established by the independent SDD super-Jacobi certificate. See [the full certification record](../../../../../../../../references/source_evidence/README.md).

**Derivative notation.** This stage uses the full Gold superspace $`\nabla_A`$. Step 6 transports it to the full project $`\mathcal D_a`$ and $`\Box^c=\mathcal D^a\mathcal D_a`$, including Q/S/K connections, as in the fermionic Weyl-squared calculation. No connection-only derivative replaces it.

## 1. Target, inputs and scope

We use the **calculated** primary in [STEP_02_LOG_PRIMARY.md](../../STEP_02_LOG_PRIMARY.md), Eq. (S2-193), and its spinor descendant in [STEP_03_LOG_SPINOR.md](../../STEP_03_LOG_SPINOR.md), Eq. (S3-200). In particular, the primary input H3.9 has the derived coefficient $`+i/4`$. The unchanged printed S23 primary is not substituted for this input.

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

The [main source conventions](../../CONVENTIONS.md) and [LOG working conventions](../../LOG_CONVENTIONS.md) control this calculation. We use the scoped Gold superspace conventions.

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

