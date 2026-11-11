# LOG component multiplet and bosonic action — S6-01 – S6-phi-010

<a id="step-6--the-log-multiplet-in-our-conventions--definitions-and-conventions"></a>

[Component index](../STEP_06_LOG_PROJECTED_MULTIPLET_AND_BOSONIC_ACTION.md).

---
title: "Step 6 — projected LOG multiplet and bosonic BF action"
date: 2026-09-24
status: "Explicit component transport; complete calculated bosonic comparison certified 2026-09-25; fermionic gates scoped separately"
procedure: GAUGED-LOG-G25-S23-PROCEDURE-v1
fermion_order: "zero/two explicit fermions in even slots; one in the spinor; higher remainder displayed"
---

## Step 6 — the LOG multiplet in our conventions

<!-- LOG_CURRENT_CERTIFICATION_20260925 -->

**Current scope:** [the 2026-09-25 certificate](../CERTIFICATION_LOG_TWO_FERMI_2026-09-25.md) verifies the full primary and the component action through two physical fermions. The source comparisons and restricted tests below retain their stated mathematical scope.

## Contents

1. [Problem and Target](convention_001.md#1-problem-and-target)
2. [Convention Ledger](convention_001.md#2-convention-ledger)
3. [Definitions and Required Identities](convention_001.md#3-definitions-and-required-identities)
4. [Detailed Derivation](convention_001.md#4-detailed-derivation)
5. [Consistency Checks](convention_001.md#5-consistency-checks)
6. [Convention Dependence and Remaining Uncertainties](convention_001.md#6-convention-dependence-and-remaining-uncertainties)
7. [Final Result](convention_001.md#7-final-result): [triplet](convention_001.md#71-the-triplet), [spinor](convention_001.md#72-the-spinor), [scalar](scalar_003.md#73-the-scalar), [vector](scalar_125.md#74-the-vector), [bosonic action and comparison](bosonic_266.md#75-bosonic-action-and-comparison).

**Source-algebra repair, 2026-09-25.** The scalar and vector below have been rebuilt using the Jacobi-required $`i`$ factors in C24 (A.1l). Their source inputs H1.3 and H2.4 are propagated before the once-only component projection. The full $`\mathcal D_a`$ and $`\Box^c`$ convention is unchanged. Exact propagation and independent complete-polynomial checks are recorded in [the certification evidence](../CERTIFICATION_LOG_TWO_FERMI_2026-09-25.md).

## 1. Problem and Target

Project the four **calculated** superfields in [step 2](../STEP_02_LOG_PRIMARY.md), [step 3](../STEP_03_LOG_SPINOR.md), [step 4](../STEP_04_LOG_SCALAR.md), and [step 5](../STEP_05_LOG_VECTOR.md), then transport them to the component conventions of [LOG_CONVENTIONS.md](../LOG_CONVENTIONS.md). The output consists of $`L_{\log}^{ij},\varphi_{\log\alpha}^{i},N_{\log},E_{\log}^{a}`$. The complete retained expressions are collected in §7. The BF density is kept compact; its bosonic specialization and the earlier project action are compared separately.

All retained terms of the existing covariant polynomials are transported below, including their mixed-curvature terms. A separate [complete calculated bosonic certificate](../../../../../../../references/source_evidence/log/derivations/bosonic.md) now reduces the **entire calculated zero-fermion scalar/vector/BF polynomial** to the corrected prior action, including every flux/derivative term, the independent compensator vector, and explicit boundary currents. This comparison is an equality of the bosonic densities with the displayed boundary currents.

Assumptions:

1. **A1:** five-dimensional classical, off-shell Standard-Weyl supergravity; no field equation or auxiliary elimination.
2. **A2:** the defining vector scalar obeys $`\rho>0`$. The four projected components remain gauge unfixed.
3. **A3:** retain explicit fermion degree $`0,2`$ in $`L_{\log},N_{\log},E_{\log}`$ and degree $`1`$ in $`\varphi_{\log}`$. The omitted degree starts at $`4`$ in even slots and $`3`$ in the spinor. This is a formal Grassmann-degree truncation, not a small numerical parameter.
4. **A4:** retain full supercovariant strengths, curvatures and ordered $`\mathcal D_a`$. Their implicit connection fermions are retained; a subsequent expansion must again discard actual degree above two. Thus “two explicit fermions” does not mean setting gravitino terms inside a supercovariant tensor to zero.
5. **A5:** only the final bosonic comparison uses $`\rho=1`$, vanishing fermions and $`b_\mu=0`$, and then the gauged dilaton-Weyl substitutions. It uses the independent compensator $`L^{ij},N,E^a`$, which is different from the LOG composite.
6. **A6:** equality modulo a divergence, denoted $`\simeq_{\partial}`$, is used only for actions. Dropping an integrated divergence requires a compact manifold without boundary or vanishing flux of the stated boundary current.

| Input | Located relation | Evidence |
|---|---|---|
| Descendant definitions | S23 (3.26a–c) | [S23 PDF22](https://arxiv.org/abs/2302.14295) |
| Bar projection and full component derivative | C24 (2.15)–(2.17) | [Components of curvature-squared invariants of minimal supergravity in five dimensions — PDF12](https://arxiv.org/abs/2311.00679), [Components of curvature-squared invariants of minimal supergravity in five dimensions — PDF13](https://arxiv.org/abs/2311.00679) |
| Inverse two-form/spinor map | C24 footnote 4 | [Components of curvature-squared invariants of minimal supergravity in five dimensions — PDF9](https://arxiv.org/abs/2311.00679) |
| Mixed superspace curvatures; vector–vector curvatures | C24 (A.3), (A.4a–c) | [Components of curvature-squared invariants of minimal supergravity in five dimensions — PDF82](https://arxiv.org/abs/2311.00679), [Components of curvature-squared invariants of minimal supergravity in five dimensions — PDF83](https://arxiv.org/abs/2311.00679) |
| Field, curvature, parameter and connection bridge | C24 Appendix C, Tables 4–6 | [Components of curvature-squared invariants of minimal supergravity in five dimensions — PDF90](https://arxiv.org/abs/2311.00679), [Components of curvature-squared invariants of minimal supergravity in five dimensions — PDF91](https://arxiv.org/abs/2311.00679), [Components of curvature-squared invariants of minimal supergravity in five dimensions — PDF92](https://arxiv.org/abs/2311.00679) |
| BF principle | S23 (3.2), (3.27); C24 (5.9b) | [S23 PDF14](https://arxiv.org/abs/2302.14295); [working seven-term audit](../LOG_CONVENTIONS.md#43-seven-bf-terms-and-the-form-residual) |
| Existing corrected bosonic reduction | Project L1–L13 and final LOG formula | [editable derivation](../../../../../../../gauss_bonnet/ads5/code/inputs/action_sources/10_weyl_log_from_definitions.tex), [LOG-CORR01–05](../CONVENTIONS.md) |

## 2. Convention Ledger

<!-- ASSERT_CONVENTION: metric_signature=(-,+,+,+,+), natural_units=hbar=c=1, source_frame=Gold traceless Standard-Weyl, target_frame=Bergshoeff/Ozkan project-corrected components, component_projection=exactly once, regularization_scheme=Not applicable for initial classical analysis, renormalization_scheme=Not applicable for initial classical analysis -->

Use $`a,b=0,\ldots,4`$, $`\alpha,\beta=1,\ldots,4`$, $`i,j=1,2`$, weighted (anti)symmetrization, $`\epsilon^{01234}=1`$, and

```math
\eta_{ab}=\mathop{\mathrm{diag}}\nolimits(-,+,+,+,+),\qquad \{\gamma^a,\gamma^b\}=2\eta^{ab},\qquad
\gamma^{ab}=\tfrac12[\gamma^a,\gamma^b],\qquad \gamma^{01234}=i.
\tag{S6-01}
```

Our spacetime convention is $`R_{\mu\nu}{}^{ab}=2\partial_{[\mu}\omega_{\nu]}{}^{ab}+2\omega_{[\mu}{}^{ac}\omega_{\nu]c}{}^b`$ and $`R_{\mu\nu}=R_{\mu\rho}{}^{ab}e_b{}^\rho e_{\nu a}`$. Supercovariant $`R(M)`$ below is the traceless curvature of master R03, not the ordinary Riemann tensor. A hat on $`R(Q),R(V),R(M)`$ is suppressed in the long expressions; all three are supercovariant. In §7.5, $`R_{abcd}`$ without a parenthetical generator is the ordinary bosonic Riemann tensor.

The doublet and Majorana rules are

```math
u_i=u^j\varepsilon_{ji},\qquad u^i=\varepsilon^{ij}u_j,\qquad
\varepsilon^{12}=\varepsilon_{12}=1,\qquad \bar\zeta=\zeta^T\mathsf C.
\tag{S6-02}
```

The bar is linear, so $`\overline{i\zeta}=i\bar\zeta`$. All physical fermions and supersymmetry parameters are odd. No odd factors are exchanged in the projection. Collecting repeated monomials moves only even factors; their interchange sign is $`+1`$.

The explicit spinor-index realization continues step 2 (S2-02). In a basis with $`\mathsf C^T=-\mathsf C`$, $`\mathsf C^2=-1`$, use $`\mathsf C^{\alpha\beta}=(-\mathsf C)^{\alpha\beta}`$ and

```math
\zeta^\alpha=\mathsf C^{\alpha\beta}\zeta_\beta,\qquad
(\gamma^a)_{\alpha\beta}=\mathsf C_{\beta\delta}(\gamma^a)_\alpha{}^\delta,
\qquad (\gamma^{ab})_{\alpha\beta}=\mathsf C_{\beta\delta}(\gamma^{ab})_\alpha{}^\delta.
\tag{S6-03}
```

Thus the arrays with two lower indices are $`-\gamma^a\mathsf C`$ and $`-\gamma^{ab}\mathsf C`$. This is an index-placement statement; a Majorana bilinear kernel is instead $`\mathsf C\gamma^{ab}`$. They must not be identified. The former $`M\mathsf C`$ step in note 07 (LB42) was a second-index-lowering error and is now corrected there to $`M\mathsf C^T=-M\mathsf C`$. This calculation already used the correct indexed rule, which is unchanged. The [full superform proof](../../../../../../../references/source_evidence/log/derivations/form-interface.md) resolves FORM-01 for genuine multiplets and shows that the literal current discrepancy is only $`2Q_1`$.

The defining vector is $`(\rho,A_\mu,\lambda^i,Y^{ij})`$, while the independent compensator is $`(L^{ij},\varphi^i,N,E^a)`$. The LOG composite carries a subscript throughout. Conformal weights are

```math
w(\rho,\lambda,Y,\widehat F,T,\chi,D)=(1,\tfrac32,2,2,1,\tfrac32,2),\qquad
w(L_{\log},\varphi_{\log},N_{\log},E_{\log})=(3,\tfrac72,4,4).
\tag{S6-04}
```

The later gauge-fixed coupling remains $`S=(2\kappa_5^2)^{-1}\int d^5x\,e(\ell_{2\partial}+\lambda_{\rm LOG}\ell_{\rm LOG})`$, with $`[\kappa_5^2]=-3`$ and $`[\lambda_{\rm LOG}]=-2`$. No Fourier convention, quantum-state normalization or renormalization prescription is used.

## 3. Definitions and Required Identities

### 3.1 Projection, slot normalization and derivative order

The source definitions are

```math
\varphi_G^{\alpha i}=\tfrac13\nabla_j^\alpha H^{ij},\qquad
F_G=\tfrac i{12}\nabla_i^\alpha\nabla_{\alpha j}H^{ij},\qquad
\mathcal H_G^a=\tfrac i{12}(\Gamma^a)^{\alpha\beta}\nabla_{\alpha i}\nabla_{\beta j}H^{ij}.
\tag{S6-05}
```

The previously matched four-slot normalization gives

```math
L_{\log}^{ij}=-2H^{ij}|,\qquad \varphi_{\log\alpha}^{i}=-2i\varphi_{G\alpha}^{i}|,
\qquad N_{\log}=-F_G|,\qquad E_{\log}^a=\mathcal H_G^a|.
\tag{S6-06}
```

Here $`|`$ is applied once, after the superspace differentiations. The right sides must also receive the complete field/Clifford bridge. Adding a vertical bar alone does not perform that bridge.

C24 (2.16) reads

```math
e_\mu{}^a\nabla_a=\partial_\mu-\tfrac12\psi_{G\mu}^{\alpha i}Q_{\alpha i}
-\tfrac12\omega_{G\mu}^{ab}M_{ab}-b_\mu\mathbb D-\phi_{G\mu}^{ij}J_{ij}
-\tfrac12\phi_{G\mu}^{\alpha i}S_{\alpha i}-f_{G\mu}{}^aK_a.
\tag{S6-07}
```

The target derivative is the full project $`\mathcal D_a`$. The source connection shifts are

```math
\omega_G=-\omega,\qquad \mathcal V_G{}^i{}_j=-V{}^i{}_j,\qquad
i\phi_{G\mu}^i=-\phi_\mu^i+\tfrac13T_{ab}\gamma^{ab}\psi_\mu^i,
\qquad f_{G\mu}{}^a=-f_\mu{}^a+\tfrac13\bar\psi_\mu^i\gamma^a\chi_i.
\tag{S6-08}
```

Together with $`\epsilon=2\xi`$, $`\eta_B=-2i\eta_G+2T_{ab}\gamma^{ab}\xi/3`$ and the corresponding $`K`$ shift, these identify the **whole** vector derivative (C24 Appendix C, paragraph before Table 4). Consequently every ordered derivative is transported in the same order. As concrete target definitions, master V02 gives

```math
\begin{aligned}
\mathcal D_\mu\rho&=(\partial_\mu-b_\mu)\rho-\tfrac i2\bar\psi_\mu\lambda,\qquad
\widehat F_{\mu\nu}=2\partial_{[\mu}A_{\nu]}-\bar\psi_{[\mu}\gamma_{\nu]}\lambda+\tfrac i2\rho\bar\psi_{[\mu}\psi_{\nu]},\\
\mathcal D_\mu\lambda^i&=\left(\partial_\mu-\frac32b_\mu+\frac14\omega_\mu{}^{ab}\gamma_{ab}\right)\lambda^i-V_\mu{}^{ij}\lambda_j+\tfrac14\gamma\!\cdot\!\widehat F\psi_\mu^i
+\tfrac i2\not{\mathcal D}\rho\psi_\mu^i+Y^{ij}\psi_{\mu j}-\rho\gamma\!\cdot\!T\psi_\mu^i-\rho\phi_\mu^i.
\end{aligned}
\tag{S6-09}
```

The first bracket displays the Lorentz, dilatation and SU(2) part only to define the full derivative on the left; no second derivative operator is used in the component result. The remaining $`\mathcal D`$ derivatives and supercovariant curvatures are fixed by master G02, R01–R03, V01–V02. In particular $`R(Q)=R'(Q)-2i\gamma_{[\mu}\phi_{\nu]}`$, and $`R(M)=R'(M)+8f_{[\mu}{}^{[a}e_{\nu]}{}^{b]}`$, using the project-corrected explicit $`\psi\chi`$ term in R03.

### 3.2 Elementary component bridge

Combine C24 (2.15), supplement (1.2), and Tables 4–6:

```math
\begin{aligned}
W|&=\rho,\quad v_G=-A,\quad \lambda_{G\alpha}^i|=-\lambda_\alpha^i,\quad X_G^{ij}|=2Y^{ij},\quad F_{Gab}|=-\widehat F_{ab},\\
W_{ab}|&=\tfrac{16}{3}T_{ab},\quad X_\alpha^i|=-\tfrac{32i}{3}\chi_\alpha^i,\quad Y_G|=-\tfrac{128}{3}D,\quad X_{ab}^{ij}|=-\tfrac{4i}{3}R(V)_{ab}^{ij},\\
\Gamma_G^a&=i\gamma^a,\quad\Sigma_G^{ab}=\tfrac12\gamma^{ab},\quad\epsilon_G^{abcde}=-\epsilon^{abcde},\quad R_G(Q)=\tfrac12R(Q),\quad R_G(M)=-R(M).
\end{aligned}
\tag{S6-10}
```

For example $`\Phi_{ab}^{ij}=-3iX_{ab}^{ij}|/4=-R(V)_{ab}^{ij}`$ implies $`X_{ab}^{ij}|=(-4/3i)\Phi_{ab}^{ij}=-4iR(V)_{ab}^{ij}/3`$. The $`Y_G`$ on the second line is the Weyl scalar descendant, not $`Y^{ij}`$.

The source and target lower doublet metrics have opposite numerical entries but lower a field on opposite sides:

```math
\varepsilon_{Gij}=-\varepsilon_{Bij},\qquad
\varepsilon_{Gij}u^j=-\varepsilon_{Bij}u^j=u^j\varepsilon_{Bji}=u_i.
\tag{S6-11}
```

Thus a **naked** lower epsilon receives a minus sign. An already lowered physical field does not receive another minus. Upper doublet epsilon is unchanged. This distinction is implemented before displaying the results.

## 4. Detailed Derivation

### 4.1 Eliminate the higher Weyl tensors

<!-- ASSERT_CONVENTION: source_frame=Gold traceless Standard-Weyl, target_frame=Bergshoeff/Ozkan project-corrected components, component_projection=exactly once -->

The two-form/spinor maps in C24 footnote 4 are $`U_{ab}=(\Sigma_{Gab})^{\alpha\beta}U_{\alpha\beta}`$ and $`U_{\alpha\beta}=\tfrac12(\Sigma_G^{ab})_{\alpha\beta}U_{ab}`$. Substituting the factors in (S6-10) gives

```math
\begin{aligned}
F_{G\alpha\beta}|&=\tfrac12\cdot\tfrac12\cdot(-1)(\gamma^{ab})_{\alpha\beta}\widehat F_{ab}
=-\tfrac14(\gamma^{ab})_{\alpha\beta}\widehat F_{ab},\\
W_{\alpha\beta}|&=\tfrac12\cdot\tfrac12\cdot\tfrac{16}{3}(\gamma^{ab})_{\alpha\beta}T_{ab}
=\tfrac43(\gamma^{ab})_{\alpha\beta}T_{ab},\\
X_{\alpha\beta}^{ij}|&=\tfrac12\cdot\tfrac12\cdot(-\tfrac{4i}{3})(\gamma^{ab})_{\alpha\beta}R(V)_{ab}^{ij}
=-\tfrac i3(\gamma^{ab})_{\alpha\beta}R(V)_{ab}^{ij}.
\end{aligned}
\tag{S6-12}
```

For the three-spinor Weyl descendant, C24 (2.17), (A.4a) give

```math
R_G(Q)_{ab\alpha}^i=-\tfrac i2W_{ab\alpha}^i|,
\qquad W_{ab\alpha}^i|=2iR_G(Q)_{ab\alpha}^i=iR(Q)_{ab\alpha}^i,
\qquad W_{\alpha\beta\gamma}^i|=\tfrac i4(\gamma^{ab})_{\alpha\beta}R(Q)_{ab\gamma}^i.
\tag{S6-13}
```

For the four-spinor descendant, start with C24 (A.4c), lower the Lorentz pair, and multiply by the two inverse Sigma maps:

```math
\begin{aligned}
R_G(M)_{ab,cd}&=-\tfrac14(\Sigma_{Gab})^{\mu\nu}(\Sigma_{Gcd})^{\rho\sigma}
\left(iW_{\mu\nu\rho\sigma}|+3W_{(\mu\nu}|W_{\rho\sigma)}|\right),\\
(\Sigma_G^{ab})_{\alpha\beta}(\Sigma_G^{cd})_{\gamma\delta}R_G(M)_{ab,cd}
&=-\left(iW_{\alpha\beta\gamma\delta}|+3W_{(\alpha\beta}|W_{\gamma\delta)}|\right),\\
W_{\alpha\beta\gamma\delta}|&=i(\Sigma_G^{ab})_{\alpha\beta}(\Sigma_G^{cd})_{\gamma\delta}R_G(M)_{ab,cd}
+3iW_{(\alpha\beta}|W_{\gamma\delta)}|.
\end{aligned}
\tag{S6-14}
```

In the second line each contracted Sigma pair gives $`2\delta_{(\alpha}^{\mu}\delta_{\beta)}^{\nu}`$; $`(-1/4)2\cdot2=-1`$. Dividing the third line uses $`1/i=-i`$, fixing both signs. There are three distinct pairings in the symmetrized product, each with weight $`1/3`$. Thus

```math
\begin{aligned}
W_{\alpha\beta\gamma\delta}|={}&-\tfrac i4(\gamma^{ab})_{\alpha\beta}(\gamma^{cd})_{\gamma\delta}R(M)_{ab,cd}\\
&+\tfrac{16i}{9}\left[(\gamma^{ab})_{\alpha\beta}(\gamma^{cd})_{\gamma\delta}
+(\gamma^{ab})_{\alpha\gamma}(\gamma^{cd})_{\beta\delta}
+(\gamma^{ab})_{\alpha\delta}(\gamma^{cd})_{\beta\gamma}\right]T_{ab}T_{cd}.
\end{aligned}
\tag{S6-15}
```

This removes every higher super-Weyl component in favor of project curvatures and fields. For a differentiated four-spinor tensor, the product rule is required, for example

```math
\begin{aligned}
\mathcal D_e(T_{ab}T_{cd})&=(\mathcal D_eT_{ab})T_{cd}+T_{ab}\mathcal D_eT_{cd},\\
\mathcal D_f\mathcal D_e(T_{ab}T_{cd})&=(\mathcal D_f\mathcal D_eT_{ab})T_{cd}
+(\mathcal D_eT_{ab})(\mathcal D_fT_{cd})
+(\mathcal D_fT_{ab})(\mathcal D_eT_{cd})+T_{ab}\mathcal D_f\mathcal D_eT_{cd}.
\end{aligned}
\tag{S6-16}
```

No two derivatives are commuted here. The same order is retained on $`R(M)`$.

### 4.2 Mixed superspace curvatures are expanded before transport

The earlier descendants contain $`\mathcal T_{a\alpha}{}^\beta`$ and $`\mathcal R(M),\mathcal R(J),\mathcal R(\mathbb D),\mathcal R(S),\mathcal R(K)`$ with one spinor leg. They are **not** independent target component fields. Insert their complete C24 (A.3a–f) expressions, already displayed in step 4, §3, and step 5, §3; then apply (S6-10)–(S6-15) to every factor.

For example the source torsion and dilatation curvature reduce as

```math
\begin{aligned}
\mathcal T_{b\alpha}{}^\beta|&=\left[\tfrac34(\Gamma_b)_\alpha{}^\gamma W_\gamma{}^\beta
-\tfrac14W_\alpha{}^\gamma(\Gamma_b)_\gamma{}^\beta\right]|\\
&=i(\gamma_b)_\alpha{}^\gamma(\gamma^{cd})_\gamma{}^\beta T_{cd}
-\tfrac i3(\gamma^{cd})_\alpha{}^\gamma(\gamma_b)_\gamma{}^\beta T_{cd},\\
\mathcal R(\mathbb D)_{b\alpha}{}^i|&=-\tfrac14(i\gamma_b)_\alpha{}^\beta(-\tfrac{32i}{3}\chi_\beta^i)
=-\tfrac83(\gamma_b)_\alpha{}^\beta\chi_\beta^i.
\end{aligned}
\tag{S6-17}
```

The factors $`3/4\times i\times4/3=i`$, $`-1/4\times4/3\times i=-i/3`$, and $`-1/4\times i\times(-32i/3)=-8/3`$ account for all three coefficients. The source Lorentz curvature illustrates the additional orientation sign:

```math
\begin{aligned}
\mathcal R(M)_{b\alpha}{}^{i cd}|={}&
(\gamma_b)_\alpha{}^\beta R(Q)^{cd}{}_{\beta}{}^i
+\tfrac i4\epsilon_b{}^{cdef}R(Q)_{ef\alpha}^i\\
&+\tfrac83\left(\delta_b^c(\gamma^d)_\alpha{}^\beta-\delta_b^d(\gamma^c)_\alpha{}^\beta\right)\chi_\beta^i.
\end{aligned}
\tag{S6-18}
```

The first coefficient is $`-(i)(i)=1`$; the second is $`-(1/4)(-1)i=i/4`$; the third is $`(1/4)i(-32i/3)=8/3`$. The long S and K expressions are expanded by those same **displayed** source equations before collection. The endpoint contains no mixed superspace torsion or curvature symbol. The retained contribution table below records each of the 58 parent terms separately.

### 4.3 Apply the slot factors and preserve Grassmann order

For the primary's first terms, write the substitutions before multiplying constants:

```math
\begin{aligned}
-2\left(-\tfrac{3i}{8}W_{ab}X^{abij}\right)|
&=(-2)(-\tfrac{3i}{8})(\tfrac{16}{3})(-\tfrac{4i}{3})T_{ab}R(V)^{abij}
=\tfrac{16}{3}T_{ab}R(V)^{abij},\\
-2\left(\tfrac{51i}{64}X^{\alpha i}X_\alpha^j\right)|
&=(-2)(\tfrac{51i}{64})(-\tfrac{32i}{3})^2\chi^{\alpha i}\chi_\alpha^j
=\tfrac{544i}{3}\chi^{\alpha i}\chi_\alpha^j,\\
-2\left(\tfrac9{64}W^{-1}X^{ij}Y_G\right)|
&=(-2)(\tfrac9{64})(2)(-\tfrac{128}{3})\rho^{-1}Y^{ij}D
=24\rho^{-1}Y^{ij}D,\\
-2\left(-\tfrac12W^{-1}\nabla^a\nabla_aX^{ij}\right)|
&=2\rho^{-1}\mathcal D^a\mathcal D_aY^{ij}.
\end{aligned}
\tag{S6-19}
```

For the spinor trace one can lower its free spinor index before transporting, since $`\mathsf C_{\alpha\beta}\mathsf C^{\beta\gamma}=\delta_\alpha{}^\gamma`$:

```math
\varphi_{\log\alpha}^i=-\tfrac{2i}{3}\left.\nabla_{\alpha j}H^{ij}\right|.
\tag{S6-20}
```

The $`H^{ij}`$ on this right side is the full primary used in step 3. For example differentiating $`H0.1`$ gives, before any truncation,

```math
\nabla_\alpha^rH0.1^{ij}
=-\tfrac{3i}{8}\left[(\nabla_\alpha^rW_{ab})X^{abij}+W_{ab}\nabla_\alpha^rX^{abij}\right].
\tag{S6-21}
```

There is a plus product-rule sign because $`W_{ab}`$ is even. Step 3 (S3-H0.1-b) has already inserted both Weyl derivative identities into this equation. Multiply its expanded terms by $`-2i\varepsilon_{Gjr}/3`$, use (S6-11), and project the elementary fields. This carries the **calculated** spinor into the new file; no replacement by a published spinor expression is made.

For the two scalar terms independently reconstructed in step 4, the scalar slot's additional minus yields

```math
\begin{aligned}
-\left(\tfrac3{2048}Y_G^2\right)|&=-\tfrac3{2048}\left(-\tfrac{128}{3}\right)^2D^2=-\tfrac83D^2,\\
-\left(\tfrac{69}{1024}W^{ab}W_{ab}Y_G\right)|
&=-\tfrac{69}{1024}\left(\tfrac{16}{3}\right)^2\left(-\tfrac{128}{3}\right)T^{ab}T_{ab}D
=\tfrac{736}{9}T^{ab}T_{ab}D.
\end{aligned}
\tag{S6-22}
```

The derivative-of-$`Y_G`$ vector terms checked in step 5 give

```math
\begin{aligned}
\left(\tfrac3{32}W^{ab}\nabla_bY_G+\tfrac3{32}Y_G\nabla_bW^{ab}\right)|
&=\tfrac3{32}\cdot\tfrac{16}{3}\cdot(-\tfrac{128}{3})
\left(T^{ab}\mathcal D_bD+D\mathcal D_bT^{ab}\right)\\
&=-\tfrac{64}{3}\left(T^{ab}\mathcal D_bD+D\mathcal D_bT^{ab}\right).
\end{aligned}
\tag{S6-23}
```

No extra scalar-slot minus is applied to this vector. All remaining coefficients are ordinary products of the explicitly tabulated constant factors and, for (S6-15), its four displayed summands. The final expressions show the resulting ordinary fields, not an instruction to substitute later.

Truncation is performed **after** the differentiations producing each slot. In particular,

```math
\nabla(\lambda\lambda\lambda)=(\nabla\lambda)\lambda\lambda-\lambda(\nabla\lambda)\lambda+\lambda\lambda(\nabla\lambda)
\tag{S6-24}
```

has degree-two terms because $`\nabla\lambda`$ is even. Consequently the degree-one spinor displayed here must not be differentiated alone to recompute $`N_{\log}^{(2)}`$ or $`E_{\log}^{(2)}`$. Those slots use the full earlier descent, which retained the required cubic spinor terms. There are no EOM substitutions or Fierz rearrangements in this projection.

| Parent primary term | Triplet | Spinor | Scalar | Vector |
|---|---:|---:|---:|---:|
| H0.1 | 1 | 37 | 1464 | 1464 |
| H0.2 | 1 | 12 | 240 | 240 |
| H1.1 | 1 | 9 | 191 | 191 |
| H1.2 | 1 | 45 | 2193 | 2193 |
| H1.3 | 1 | 386 | 25116 | 25116 |
| H1.4 | 1 | 13 | 271 | 271 |
| H1.5 | 2 | 40 | 1504 | 1504 |
| H1.6 | 2 | 62 | 2400 | 2400 |
| H1.7 | 2 | 72 | 3374 | 3374 |
| H2.1 | 1 | 57 | 2453 | 2453 |
| H2.2 | 1 | 60 | 2280 | 2280 |
| H2.3 | 2 | 40 | 2280 | 2280 |
| H2.4 | 2 | 358 | 25458 | 25458 |
| H2.5 | 1 | 50 | 3538 | 3538 |
| H2.6 | 2 | 58 | 2404 | 2404 |
| H2.7 | 1 | 8 | 905 | 905 |
| H2.8 | 1 | 8 | 170 | 170 |
| H2.9 | 2 | 20 | 1032 | 1032 |
| H2.10 | 1 | 8 | 252 | 252 |
| H2.11 | 1 | 8 | 252 | 252 |
| H2.12 | 1 | 10 | 370 | 370 |
| H3.1 | 1 | 27 | 969 | 969 |
| H3.2 | 1 | 19 | 545 | 545 |
| H3.3 | 1 | 15 | 367 | 367 |
| H3.4 | 2 | 58 | 3432 | 3432 |
| H3.5 | 2 | 58 | 3432 | 3432 |
| H3.6 | 1 | 8 | 2830 | 2830 |
| H3.7 | 1 | 29 | 1418 | 1418 |
| H3.8 | 2 | 58 | 2836 | 2836 |
| H3.9 | 2 | 16 | 3508 | 3508 |
| H3.10 | 1 | 8 | 1895 | 1895 |
| H3.11 | 2 | 58 | 2542 | 2542 |
| H3.12 | 2 | 58 | 2542 | 2542 |
| H3.13 | 1 | 8 | 279 | 279 |
| H3.14 | 1 | 8 | 472 | 472 |
| H3.15 | 1 | 8 | 472 | 472 |
| H3.16 | 1 | 8 | 342 | 342 |
| H3.17 | 0 | 0 | 480 | 480 |
| H3.18 | 0 | 0 | 240 | 240 |
| H4.1 | 1 | 8 | 306 | 306 |
| H4.2 | 2 | 16 | 738 | 738 |
| H4.3 | 1 | 8 | 499 | 499 |
| H4.4 | 1 | 8 | 692 | 692 |
| H4.5 | 1 | 8 | 692 | 692 |
| H4.6 | 1 | 8 | 562 | 562 |
| H4.7 | 1 | 8 | 432 | 432 |
| H4.8 | 1 | 8 | 432 | 432 |
| H4.9 | 0 | 0 | 696 | 696 |
| H4.10 | 0 | 0 | 1392 | 1392 |
| H4.11 | 0 | 0 | 1392 | 1392 |
| H4.12 | 0 | 0 | 696 | 696 |
| H4.13 | 0 | 0 | 384 | 384 |
| H4.14 | 0 | 0 | 192 | 192 |
| H5.1 | 0 | 0 | 384 | 384 |
| H5.2 | 0 | 0 | 192 | 192 |
| H5.3 | 0 | 0 | 192 | 192 |
| H6.1 | 0 | 0 | 0 | 0 |
| H6.2 | 0 | 0 | 0 | 0 |

Counts are unreduced algebraic contributions, not independent invariant structures. A zero means the term contributes only above the selected fermion degree to that slot.

### 4.4 Compact BF assembly

Substitute (S6-06) into the seven source terms, retaining their overall minus sign. The nonform products are

```math
\begin{aligned}
-W_GF_G&=\rho N_{\log},\qquad -X_{Gij}H^{ij}=Y^{ij}L_{\log ij},\qquad
-2\lambda_G^i\varphi_{Gi}=i\bar\lambda\varphi_{\log},\\
W_G\psi_{ai}\Gamma_G^a\varphi_G^i&=\tfrac12\rho\bar\psi_a\gamma^a\varphi_{\log},\qquad
i\psi_{ai}\Gamma_G^a\lambda_{Gj}H^{ij}=-\tfrac12\bar\psi_a^i\gamma^a\lambda^jL_{\log ij},\\
-iW_G\psi_{ai}\Sigma_G^{ab}\psi_{bj}H^{ij}&=\tfrac i4\rho\bar\psi_a^i\gamma^{ab}\psi_b^jL_{\log ij}.
\end{aligned}
\tag{S6-25}
```

Their normalization and ordered Majorana contractions are the prior step-1 matching. The separate completed superform certificate supplies the current/potential interface proof. The operational component density is

```math
\begin{aligned}
\ell_{\log}={}&Y^{ij}L_{\log ij}+i\bar\lambda\varphi_{\log}
-\tfrac12\bar\psi_a^i\gamma^a\lambda^jL_{\log ij}+A_aP_{\log}^a\\
&+\rho\left(N_{\log}+\tfrac12\bar\psi_a\gamma^a\varphi_{\log}
+\tfrac i4\bar\psi_a^i\gamma^{ab}\psi_b^jL_{\log ij}\right),\\
P_{\log}^a={}&E_{\log}^a+\tfrac i2\bar\psi_b\gamma^{ba}\varphi_{\log}
+\tfrac14\bar\psi_b^i\gamma^{abc}\psi_c^jL_{\log ij}.
\end{aligned}
\tag{S6-26}
```

At the specified order, the first, fourth and scalar terms need the even slots through degree two; the other terms need only the linear spinor or bosonic triplet. No full expansion of (S6-26) is required. The literal Gold printed vector term instead maps to $`A_aE_{\log}^a`$. The difference literal Gold minus the operational density is $`-A_a(P_{\log}^a-E_{\log}^a)`$. The [closed-superform derivation](../../../../../../../references/source_evidence/log/derivations/form-interface.md), (FI25)–(FI31), proves that the ordinary current $`P`$ is required; it agrees with the original source action (8.28)–(8.29). This resolves the generic FORM-01 interface while preserving the incompatible printed expression as a source record.

Setting all fermions to zero eliminates that residual and gives the exact bosonic insertion

```math
\ell_{\log}^{\rm bos}=A_aE_{\log}^{a(0)}+\rho N_{\log}^{(0)}+Y^{ij}L_{\log ij}^{(0)}.
\tag{S6-27}
```

The degree-zero triplet can already be collected in a short local expression directly from the calculated primary:

```math
\begin{aligned}
L_{\log}^{ij(0)}={}&\tfrac{16}{3}T_{ab}R(V)^{abij}-\rho^{-1}F_{ab}R(V)^{abij}
+\rho^{-1}\left(24Y^{ij}D+2\mathcal D^a\mathcal D_aY^{ij}+16Y^{ij}T^{ab}T_{ab}\right)\\
&-2\rho^{-2}\left[Y^{ij}\mathcal D^a\mathcal D_a\rho+(\mathcal D^a\rho)\mathcal D_aY^{ij}\right]
+\rho^{-3}Y^{ij}\left[-\tfrac12F^{ab}F_{ab}+2Y^{kl}Y_{kl}+(\mathcal D^a\rho)\mathcal D_a\rho\right].
\end{aligned}
\tag{S6-27a}
```

Its last three coefficients come from $`(-2)(1/8)(2)(-1)^2=-1/2`$, $`(-2)(-1/8)2^3=2`$, and $`(-2)(-1/4)2=1`$ in H3.1–H3.3. Together with (S6-19), these account for every bosonic primary input.

The curvature term generated by degauging this triplet can also be checked without importing a reduced action. In Gold's bosonic frame C24 (2.24c) gives $`f_{Ga}{}^a=(-1/6+5/48)R_G=-R_G/16`$. The commutator $`[K_a,\nabla_b]U=2\eta_{ab}w(U)U`$ on a primary scalar gives, at $`W=1,b_a=0`$,

```math
\nabla^a\nabla_aW=-2f_{Ga}{}^a=\tfrac18R_G,\qquad
\nabla^a\nabla_aX^{ij}=D_G^aD_{Ga}X^{ij}-4f_{Ga}{}^aX^{ij}
=D_G^aD_{Ga}X^{ij}+\tfrac14R_GX^{ij}.
\tag{S6-27b}
```

Consequently $`-\tfrac12\Box X^{ij}+\tfrac12X^{ij}\Box W`$ contributes $`(-1/8+1/16)R_GX^{ij}=-R_GX^{ij}/16`$ to $`H^{ij}`$. Multiplying by $`-2`$, substituting $`X=2Y`$ and $`R_G=-R`$ gives $`-RY^{ij}/4`$. The complete bosonic triplet on this gauge slice is therefore

```math
L_{\log}^{ij(0)}=\left(\tfrac{16}{3}T^{ab}-F^{ab}\right)R(V)_{ab}^{ij}
+2D^aD_aY^{ij}+Y^{ij}\left(24D-\tfrac14R+16T^2-\tfrac12F^2+2Y^{kl}Y_{kl}\right).
\tag{S6-27c}
```

This agrees with the previous `eq:L-lowest` after its full bridge. Unlike the full scalar/vector reduction, this entire bosonic triplet comparison has been performed above.

### 4.5 Bosonic reduction and comparison: equality status

The full projected expressions in §7 define (S6-27) locally, with its ordered superconformal derivatives. To compare it to the prior **gauge-fixed** project action, one also has to degauge the derivatives and fix $`\rho=1,b_\mu=0`$. In particular $`\mathcal D_a\mathcal D_b\rho`$ cannot be replaced by zero just because $`\rho`$ is constant: it contains the K connection. The old derivation performs that reduction from the raw C24 supplement §3.1. The separate 2026-09-25 calculated bosonic certificate now performs the full degauging and exact boundary matching directly on the newly generated component polynomials; it reproduces the entire corrected action.

The direct primary-based check (S6-22) gives the previously disputed $`T^2D`$ coefficient. In Gold's intermediate fields this is $`+23w^2D/8`$ in the BF action. C24 (5.20) already has that coefficient; only the earlier printed scalar projection (4.8b) has the recorded mismatch. Do not add another copy of this term to the action.

The second inherited correction concerns the curvature/derivative representative. The explicit calculation in the earlier source audit is

```math
\begin{aligned}
\ell^G_{w,\rm curv}&=\tfrac13R_{abcd}w^{ab}w^{cd}+\tfrac13R_{acbd}w^{ab}w^{cd}
-R_{ab}w^{ac}w^b{}_c-\tfrac{27}{256}Rw^2,\\
R_{acbd}w^{ab}w^{cd}&=\tfrac12R_{abcd}w^{ab}w^{cd},\\
\ell^G_{w,\rm der}&\simeq_{\partial}\tfrac38(D_aw_{bc})^2
+\tfrac14\left[(D^cw^a{}_b)(D^bw_{ac})-(D^bw^a{}_b)(D^cw_{ac})\right],\\
(D^cw^a{}_b)(D^bw_{ac})&\simeq_{\partial}(D^bw^a{}_b)(D^cw_{ac})
+R_{ab}w^{ac}w^b{}_c-\tfrac12R_{abcd}w^{ab}w^{cd},\\
\ell^G_{w,\rm curv}+\ell^G_{w,\rm der}&\simeq_{\partial}
\tfrac38(D_aw_{bc})^2+\left(\tfrac12-\tfrac18\right)R_{abcd}w^{ab}w^{cd}
+\left(-1+\tfrac14\right)R_{ab}w^{ac}w^b{}_c-\tfrac{27}{256}Rw^2.
\end{aligned}
\tag{S6-28}
```

This raw-source reduction gives $`3/8`$, rather than the $`1/4`$ in printed C24 (5.20). The [complete calculated bosonic certificate](../../../../../../../references/source_evidence/log/derivations/bosonic.md) independently obtains the same complete corrected Standard-Weyl ledger from the newly calculated scalar/vector/BF polynomials. The earlier source audit and this new calculation are separate checks.

The bosonic boundary operations use, before dropping the divergence,

```math
\begin{aligned}
-v_aD_bQ^{ab}&=-D_b(v_aQ^{ab})-\tfrac12F_{ab}Q^{ab},\qquad
-w^{cd}D^2w_{cd}=(D_aw^{cd})(D^aw_{cd})-D_a(w^{cd}D^aw_{cd}),\\
G^{ac}\nabla_c\nabla^d(G_{ad}-2H_{ad})
&=-(\nabla_cG^{ac})\nabla^d(G_{ad}-2H_{ad})
+\nabla_c\left[G^{ac}\nabla^d(G_{ad}-2H_{ad})\right].
\end{aligned}
\tag{S6-29}
```

Here $`Q^{ab}`$ denotes the antisymmetric two-index potential of the already given bosonic LOG current; it is used only to state its boundary integration. For two-form derivative canonicalization in the final project frame the earlier identity is

```math
(\nabla^aX^{ce})(\nabla_cY_{ae})\simeq_{\partial}
(\nabla_bX^{ab})(\nabla^cY_{ac})-R_{ab}X^{ac}Y^b{}_c+\tfrac12R_{abcd}X^{ab}Y^{cd},
\qquad J^m=(\nabla^aX^{me})Y_{ae}+Y^m{}_e\nabla_bX^{eb}.
\tag{S6-30}
```

$`X,Y`$ here are just the two arguments of this displayed identity, used with the explicit pairs $`G,G`$, $`G,H`$, and $`H,H`$. This line is in the project Riemann convention; (S6-28) was explicitly in Gold's intermediate convention. The sign bridge is included before applying (S6-30).

### 4.6 Gauged bosonic comparison without eliminating the independent compensator

Use the prior source-locked gauged map, only in this comparison:

```math
\begin{aligned}
\rho&=1,\quad A=C,\quad F_{Gab}=-G_{ab},\quad X_G^{ij}=2Y^{ij}=-gL^{ij},\quad
\Phi_{Gab}^{ij}=-V_{ab}^{ij},\quad R_{Gabcd}=-R_{abcd},\\
T_{ab}&=\tfrac18G_{ab}-\tfrac14H_{ab},\qquad
D=-\tfrac1{32}R+\tfrac5{96}G^2+\tfrac1{24}G\!\cdot H-\tfrac{13}{24}H^2+\tfrac g4N+\tfrac{g^2}{16}L^{ij}L_{ij}.
\end{aligned}
\tag{S6-31}
```

For example $`T^2=G^2/64-(G\!\cdot H)/16+H^2/16`$ and $`G\!\cdot T=G^2/8-(G\!\cdot H)/4`$. Inserting these two equalities into $`D=-R/32-G^2/16-(26T/3-2G)\!\cdot T+gN/4+g^2L^2/16`$ gives each coefficient in (S6-31). The $`V_{ab}^{ij}`$ here is the bosonic SU(2) curvature, not its connection.

The independent three-form and its dual satisfy

```math
\mathcal H_3=dB+\tfrac12C\wedge G+\tfrac g2E_3,\qquad
H^{ab}=-\tfrac1{12}\epsilon^{abcde}\mathcal H_{cde},\qquad
E^a=-\tfrac1{12}\epsilon^{abcde}\nabla_bE_{cde}.
\tag{S6-32}
```

Differentiate the dual. The $`dB`$ term vanishes by $`d^2=0`$, the three cyclic $`C_{[c}G_{de]}`$ terms give equal epsilon contractions, and $`\epsilon^{abcde}\nabla_bC_c=\epsilon^{abcde}G_{bc}/2`$. Therefore

```math
\nabla_bH^{ab}=-\tfrac18\epsilon^{abcde}\nabla_b(C_cG_{de})
-\tfrac g{24}\epsilon^{abcde}\nabla_bE_{cde}
=-\tfrac1{16}\epsilon^{abcde}G_{bc}G_{de}+\tfrac g2E^a.
\tag{S6-33}
```

The relevant bosonic derivative block before this substitution is

```math
\begin{aligned}
&\tfrac23(\nabla_bG^{ab})(\nabla^cH_{ac})+\tfrac43(\nabla_bH^{ab})(\nabla^cH_{ac})
+\tfrac1{12}(\nabla^bH_{ab})\epsilon^{acdef}G_{cd}G_{ef}
-\tfrac43(\nabla^bH_{ab})\epsilon^{acdef}H_{cd}H_{ef}.
\end{aligned}
\tag{S6-34}
```

Its terms containing $`E`$ arise separately as

```math
\begin{aligned}
\tfrac23\mathop{\mathrm{div}}\nolimits G\!\cdot\mathop{\mathrm{div}}\nolimits H&\supset\tfrac g3E_a\nabla_bG^{ab},\qquad
\tfrac43(\mathop{\mathrm{div}}\nolimits H)^2\supset\tfrac{g^2}{3}E_aE^a-\tfrac g{12}E_a\epsilon^{abcde}G_{bc}G_{de},\\
\tfrac1{12}\mathop{\mathrm{div}}\nolimits H\!\cdot(\epsilon GG)&\supset\tfrac g{24}E_a\epsilon^{abcde}G_{bc}G_{de},\qquad
-\tfrac43\mathop{\mathrm{div}}\nolimits H\!\cdot(\epsilon HH)\supset-\tfrac{2g}{3}E_a\epsilon^{abcde}H_{bc}H_{de}.
\end{aligned}
\tag{S6-35}
```

Here $`\mathop{\mathrm{div}}\nolimits H`$ denotes only the displayed contraction $`\nabla_bH^{ab}`$ in this four-line arithmetic. The sum $`-g/12+g/24=-g/24`$ reproduces all four previously missing explicit-$`E`$ terms. They are included once in the final density.

The curvature conversion is also explicit:

```math
\begin{aligned}
\tfrac14R_GFF+\tfrac38R_Gww
&=-\tfrac14R_{abcd}G^{ab}G^{cd}-\tfrac16R_{abcd}(G^{ab}-2H^{ab})(G^{cd}-2H^{cd})\\
&=-\tfrac5{12}R_{abcd}G^{ab}G^{cd}+\tfrac23R_{abcd}G^{ab}H^{cd}-\tfrac23R_{abcd}H^{ab}H^{cd}.
\end{aligned}
\tag{S6-36}
```

The derivative commutator contribution in the existing reduction has coefficients $`(5/12,-2/3,2/3)`$ for those same three contractions. Adding the two rows gives $`(0,0,0)`$. Retaining the printed $`1/4`$ instead of $`3/8`$ would leave $`(1/18,-2/9,2/9)`$, the already identified discrepancy. The 2026-09-25 complete calculated bosonic certificate independently establishes the full new-polynomial equality, including this curvature cancellation.

The scalar terms are checked by expanding (S6-31) in the polynomial given by the full Standard-Weyl action in §7.5. For example the fluxless curvature coefficient is

```math
\tfrac{23}{384}R^2+\tfrac12R(-\tfrac R{32})-\tfrac83(-\tfrac R{32})^2
=\left(\tfrac{23}{384}-\tfrac1{64}-\tfrac1{384}\right)R^2=\tfrac1{24}R^2.
\tag{S6-37}
```

The complete scalar polynomial, ordered two-form quartics, parity-odd terms and boundary reductions are displayed in the earlier derivation L1–L13 and its [source verification script](../../../../../../../references/source_evidence/log/scripts/verify_weyl_log_definition_map.py). The [complete calculated bosonic certificate](../../../../../../../references/source_evidence/log/derivations/bosonic.md) now also tests the actual newly calculated polynomials: the complete vector equality and both Standard-Weyl and gauged density comparisons have exactly zero residual, with the final boundary current rechecked using pointwise identities only.

## 5. Consistency Checks

The exact scope and concrete outputs of the checks accompanying this file are saved in [sources/step6/checks.json](../../../../../../../references/source_evidence/log/results/gauged_full_fermionic_log/sources/step6/checks.json) and [sources/step6/coverage.json](../../../../../../../references/source_evidence/log/results/gauged_full_fermionic_log/sources/step6/coverage.json). The original checks distinguish algebraic projection, input coverage and numerical tensor probes. The complete calculated bosonic comparison is now certified separately in [the exact proof folder](../sources/certification_20260925/bosonic/EXACT_BOSONIC_COMPARISON.md).

- **Indices and weights:** every retained projected monomial is checked for one occurrence of each stated free index and a matched up/down pair for every dummy index. Its weight is respectively $`3,7/2,4,4`$. For example $`w(\rho^{-1}Y^{ij}D)=-1+2+2=3`$ and $`w(\rho^{-1}\widehat F\,\mathcal D\lambda)=-1+2+1+3/2=7/2`$. All BF terms have weight five, e.g. $`w(\rho N_{\log})=1+4`$ and $`w(\bar\lambda\varphi_{\log})=3/2+7/2`$.
- **Clifford/projector factors:** the two-form inverse map and the four-spinor inversion (S6-14) are tested with the fixed project matrices, including all Lorentz and spinor index values. The check does not fit any action coefficient.
- **Fermion counting:** degree $`0,2`$ and $`1`$ are selected from the completed prior slots; no cubic spinor needed for the scalar/vector calculation is dropped before differentiating. Written order of odd factors is unchanged.
- **Projection coefficients:** (S6-19), (S6-22), (S6-23) show their exact rational products; the independent step-4 and step-5 curved tests remain linked from those files. No scalar $`Y_G\to D`$ projection is applied twice.
- **Bosonic/ungauged limit:** setting fermions to zero reduces the compact density to (S6-27). Setting $`g=0`$ in the final gauged comparison removes every explicit compensator-$`E`$ term. Setting all forms and compensator fields to zero leaves $`-R_{ab}R^{ab}/6+R^2/24`$, as in (S6-37).
- **Derivative and boundary status:** no derivatives are interchanged in the component projection. The comparison uses only the boundary operations stated in (S6-29)–(S6-30) and the old scalar divergence $`\nabla^2[R/8-5G^2/24-(G\!\cdot H)/6+13H^2/6-gN-g^2L^2/4]`$. Its ordinary divergence may be dropped; its original conformal curvature-weight contribution is retained.
- **Scope of the projection check:** the displayed component comparison. The complete zero-fermion polynomial equality is established by the separate 2026-09-25 bosonic certificate. The linked superform proof establishes the generic FORM-01 interface under its vector/linear-multiplet hypotheses; a finite numerical projection check has only its stated sample scope.

**Superseding bosonic verification, 2026-09-25:** the [complete calculated comparison](../../../../../../../references/source_evidence/log/derivations/bosonic.md) freshly rebuilds the actual bosonic triplet/scalar/vector, proves the full vector divergence relation, and matches every term of LOG-CORR05. Its 11-term Standard-Weyl and nine-term gauged currents combine into a displayed 16-term current. Subtracting that divergence from the original full difference leaves exactly zero by pointwise identities alone. The comparison establishes this bosonic density equality with the displayed boundary current.

## 6. Convention Dependence and Remaining Uncertainties

The source/target curvature and Clifford signs in (S6-10), the spinor metric order in (S6-03), and the distinction between a naked epsilon and a lowered field in (S6-11) are essential. Changing one requires changing the entire bridge. No convention-independent claim is made for an isolated sign.

The existing primary has the reconstructed positive $`H3.9`$ coefficient, unlike the printed S23 comparison. That reconstructed input is used here unchanged. Its transport does not resolve its source discrepancy. The unrestricted curved fermionic component-reduction and supersymmetry gates are separate from the now-certified complete bosonic comparison. The older bosonic action was an independently encoded comparison target; no action coefficient was fitted to it.

The final components are explicit, but deliberately retain full supercovariant derivatives and gamma contractions rather than a minimal Fierz basis. Duplicate literal monomials are collected using only even-factor moves and dummy relabeling. Gamma traces or equivalent tensor structures can therefore remain unreduced. Keeping them is not evidence of a new physical term.

The displayed action retains the specified explicit fermion degrees and labels the higher-order remainder. The result is a two-fermion component action; it does not specify all higher-fermion interactions.

## 7. Final Result

Every field and derivative in the following four expressions is in the declared project component convention. No superspace spinor derivative, unprojected higher Weyl tensor, mixed superspace curvature or vertical bar remains. Consecutive numbered displays continue the same sum. There are two monomials per row, and each slot ends with the specified **$`+\text{ high fermi terms}`$**. The scalar and vector are the previously computed full descents projected at the specified order, not derivatives of the truncated spinor printed here.

<!-- STEP6_COMPONENT_RESULTS_BEGIN -->

### 7.1 The triplet

59 displayed monomials after collecting identical contractions. All consecutive displays below continue the same sum.

<!-- PROJECTED_L_BEGIN -->

```math
\begin{aligned}
\fbox{$\displaystyle{L_{\log}^{ij}}$}={}&\frac{16}{3}R(V){}^{a}{}^{b}{}^{i}{}^{j}T{}_{a}{}_{b} +\frac{544i}{3}\chi{}^{\alpha}{}^{i}\chi{}_{\alpha}{}^{j}\\
&+24\rho^{-1}Y{}^{i}{}^{j}D -\rho^{-1}R(V){}^{a}{}^{b}{}^{i}{}^{j}\widehat F{}_{a}{}_{b}\\
&+2\rho^{-1}\big(\mathcal D^{a}\mathcal D_{a}Y{}^{i}{}^{j}\big) +16\rho^{-1}Y{}^{i}{}^{j}T{}^{a}{}^{b}T{}_{a}{}_{b}\\
&+\frac{4i}{3}\rho^{-1}T{}^{a}{}^{b}R(Q){}_{a}{}_{b}{}^{\alpha}{}^{i}\lambda{}_{\alpha}{}^{j} +\frac{4i}{3}\rho^{-1}T{}^{a}{}^{b}R(Q){}_{a}{}_{b}{}^{\alpha}{}^{j}\lambda{}_{\alpha}{}^{i}\\
&-8\rho^{-1}(\gamma{}^{a}){}^{\alpha}{}^{\beta}\chi{}_{\alpha}{}^{i}\big(\mathcal D_{a}\lambda{}_{\beta}{}^{j}\big) -8\rho^{-1}(\gamma{}^{a}){}^{\alpha}{}^{\beta}\chi{}_{\alpha}{}^{j}\big(\mathcal D_{a}\lambda{}_{\beta}{}^{i}\big)\\
&+8\rho^{-1}(\gamma{}^{a}){}^{\alpha}{}^{\beta}\lambda{}_{\alpha}{}^{i}\big(\mathcal D_{a}\chi{}_{\beta}{}^{j}\big) +8\rho^{-1}(\gamma{}^{a}){}^{\alpha}{}^{\beta}\lambda{}_{\alpha}{}^{j}\big(\mathcal D_{a}\chi{}_{\beta}{}^{i}\big)\\
&-2\rho^{-2}Y{}^{i}{}^{j}\big(\mathcal D^{a}\mathcal D_{a}\rho\big) -2\rho^{-2}\big(\mathcal D_{a}Y{}^{i}{}^{j}\big)\big(\mathcal D^{a}\rho\big)\\
&-\frac{i}{4}\rho^{-2}\widehat F{}^{a}{}^{b}R(Q){}_{a}{}_{b}{}^{\alpha}{}^{i}\lambda{}_{\alpha}{}^{j} -\frac{i}{4}\rho^{-2}\widehat F{}^{a}{}^{b}R(Q){}_{a}{}_{b}{}^{\alpha}{}^{j}\lambda{}_{\alpha}{}^{i}\\
&+\frac{i}{2}\rho^{-2}\lambda{}^{\alpha}{}^{j}\big(\mathcal D^{a}\mathcal D_{a}\lambda{}_{\alpha}{}^{i}\big) +\frac{i}{2}\rho^{-2}\lambda{}^{\alpha}{}^{i}\big(\mathcal D^{a}\mathcal D_{a}\lambda{}_{\alpha}{}^{j}\big)\\
&+\frac{i}{2}\rho^{-2}\big(\mathcal D^{a}\lambda{}^{\alpha}{}^{i}\big)\big(\mathcal D_{a}\lambda{}_{\alpha}{}^{j}\big) -\frac{i}{2}\rho^{-2}(\gamma{}_{a}{}_{b}){}^{\alpha}{}^{\beta}T{}_{c}{}_{d}\epsilon{}^{a}{}^{b}{}^{e}{}^{c}{}^{d}\lambda{}_{\alpha}{}^{i}\big(\mathcal D_{e}\lambda{}_{\beta}{}^{j}\big)\\
&-\frac{i}{2}\rho^{-2}(\gamma{}_{a}{}_{b}){}^{\alpha}{}^{\beta}T{}_{c}{}_{d}\epsilon{}^{a}{}^{b}{}^{e}{}^{c}{}^{d}\lambda{}_{\alpha}{}^{j}\big(\mathcal D_{e}\lambda{}_{\beta}{}^{i}\big) -4\rho^{-2}(\gamma{}^{a}){}^{\alpha}{}^{\beta}\big(\mathcal D^{b}T{}_{a}{}_{b}\big)\lambda{}_{\alpha}{}^{i}\lambda{}_{\beta}{}^{j}\\
&+4i\rho^{-2}D\lambda{}^{\alpha}{}^{i}\lambda{}_{\alpha}{}^{j} +2i\rho^{-2}(\gamma{}_{a}{}_{b}){}^{\alpha}{}^{\beta}\widehat F{}^{a}{}^{b}\chi{}_{\alpha}{}^{i}\lambda{}_{\beta}{}^{j}\\
&+2i\rho^{-2}(\gamma{}_{a}{}_{b}){}^{\alpha}{}^{\beta}\widehat F{}^{a}{}^{b}\chi{}_{\alpha}{}^{j}\lambda{}_{\beta}{}^{i} -\frac{4i}{3}\rho^{-2}T{}^{a}{}^{b}T{}_{a}{}_{b}\lambda{}^{\alpha}{}^{i}\lambda{}_{\alpha}{}^{j}\\
&-2\rho^{-2}(\gamma{}_{a}){}^{\alpha}{}^{\beta}T{}_{b}{}_{c}T{}_{d}{}_{e}\epsilon{}^{a}{}^{b}{}^{c}{}^{d}{}^{e}\lambda{}_{\alpha}{}^{i}\lambda{}_{\beta}{}^{j} +16i\rho^{-2}Y{}^{i}{}^{j}\chi{}^{\alpha}{}^{k}\lambda{}_{\alpha}{}_{k}\\
&-\frac{1}{2}\rho^{-3}Y{}^{i}{}^{j}\widehat F{}^{a}{}^{b}\widehat F{}_{a}{}_{b} +2\rho^{-3}Y{}^{i}{}^{j}Y{}^{k}{}^{l}Y{}_{k}{}_{l}\\
&+\rho^{-3}Y{}^{i}{}^{j}\big(\mathcal D^{a}\rho\big)\big(\mathcal D_{a}\rho\big) +\frac{i}{16}\rho^{-3}(\gamma{}_{a}{}_{b}){}^{\alpha}{}^{\beta}\widehat F{}_{c}{}_{d}\epsilon{}^{a}{}^{b}{}^{e}{}^{c}{}^{d}\lambda{}_{\alpha}{}^{i}\big(\mathcal D_{e}\lambda{}_{\beta}{}^{j}\big)\\
&+\frac{i}{16}\rho^{-3}(\gamma{}_{a}{}_{b}){}^{\alpha}{}^{\beta}\widehat F{}_{c}{}_{d}\epsilon{}^{a}{}^{b}{}^{e}{}^{c}{}^{d}\lambda{}_{\alpha}{}^{j}\big(\mathcal D_{e}\lambda{}_{\beta}{}^{i}\big) +\frac{1}{4}\rho^{-3}(\gamma{}^{a}){}^{\alpha}{}^{\beta}\widehat F{}_{a}{}_{b}\lambda{}_{\alpha}{}^{i}\big(\mathcal D^{b}\lambda{}_{\beta}{}^{j}\big)\\
&+\frac{1}{4}\rho^{-3}(\gamma{}^{a}){}^{\alpha}{}^{\beta}\widehat F{}_{a}{}_{b}\lambda{}_{\alpha}{}^{j}\big(\mathcal D^{b}\lambda{}_{\beta}{}^{i}\big) +\frac{1}{2}\rho^{-3}(\gamma{}^{a}){}^{\alpha}{}^{\beta}\big(\mathcal D^{b}\widehat F{}_{a}{}_{b}\big)\lambda{}_{\alpha}{}^{i}\lambda{}_{\beta}{}^{j}\\
&+\rho^{-3}Y{}^{i}{}^{j}(\gamma{}^{a}){}^{\alpha}{}^{\beta}\lambda{}_{\alpha}{}^{k}\big(\mathcal D_{a}\lambda{}_{\beta}{}_{k}\big) +\frac{1}{2}\rho^{-3}Y{}^{k}{}^{i}(\gamma{}^{a}){}^{\alpha}{}^{\beta}\lambda{}_{\alpha}{}^{j}\big(\mathcal D_{a}\lambda{}_{\beta}{}_{k}\big)\\
&+\frac{1}{2}\rho^{-3}Y{}^{k}{}^{j}(\gamma{}^{a}){}^{\alpha}{}^{\beta}\lambda{}_{\alpha}{}^{i}\big(\mathcal D_{a}\lambda{}_{\beta}{}_{k}\big) +\frac{1}{2}\rho^{-3}\big(\mathcal D_{a}Y{}^{j}{}^{k}\big)(\gamma{}^{a}){}^{\alpha}{}^{\beta}\lambda{}_{\alpha}{}^{i}\lambda{}_{\beta}{}_{k}\\
&+\frac{1}{2}\rho^{-3}\big(\mathcal D_{a}Y{}^{i}{}^{k}\big)(\gamma{}^{a}){}^{\alpha}{}^{\beta}\lambda{}_{\alpha}{}^{j}\lambda{}_{\beta}{}_{k} -\frac{i}{2}\rho^{-3}\big(\mathcal D^{a}\mathcal D_{a}\rho\big)\lambda{}^{\alpha}{}^{i}\lambda{}_{\alpha}{}^{j}\\
&-\frac{3i}{4}\rho^{-3}\big(\mathcal D^{a}\rho\big)\lambda{}^{\alpha}{}^{i}\big(\mathcal D_{a}\lambda{}_{\alpha}{}^{j}\big) -\frac{3i}{4}\rho^{-3}\big(\mathcal D^{a}\rho\big)\lambda{}^{\alpha}{}^{j}\big(\mathcal D_{a}\lambda{}_{\alpha}{}^{i}\big)\\
&+\frac{i}{4}\rho^{-3}(\gamma{}_{a}{}_{b}){}^{\alpha}{}^{\beta}\big(\mathcal D^{a}\rho\big)\lambda{}_{\alpha}{}^{i}\big(\mathcal D^{b}\lambda{}_{\beta}{}^{j}\big) +\frac{i}{4}\rho^{-3}(\gamma{}_{a}{}_{b}){}^{\alpha}{}^{\beta}\big(\mathcal D^{a}\rho\big)\lambda{}_{\alpha}{}^{j}\big(\mathcal D^{b}\lambda{}_{\beta}{}^{i}\big)\\
&-2\rho^{-3}(\gamma{}^{a}){}^{\alpha}{}^{\beta}\big(\mathcal D^{b}\rho\big)T{}_{a}{}_{b}\lambda{}_{\alpha}{}^{i}\lambda{}_{\beta}{}^{j} +i\rho^{-3}\widehat F{}^{a}{}^{b}T{}_{a}{}_{b}\lambda{}^{\alpha}{}^{i}\lambda{}_{\alpha}{}^{j}\\
&+\frac{3}{2}\rho^{-3}(\gamma{}_{a}){}^{\alpha}{}^{\beta}\widehat F{}_{b}{}_{c}T{}_{d}{}_{e}\epsilon{}^{a}{}^{d}{}^{e}{}^{b}{}^{c}\lambda{}_{\alpha}{}^{i}\lambda{}_{\beta}{}^{j} +i\rho^{-3}Y{}^{i}{}^{j}(\gamma{}_{a}{}_{b}){}^{\alpha}{}^{\beta}T{}^{a}{}^{b}\lambda{}_{\alpha}{}^{k}\lambda{}_{\beta}{}_{k}\\
&+\frac{3i}{8}\rho^{-4}\big(\mathcal D^{a}\rho\big)\big(\mathcal D_{a}\rho\big)\lambda{}^{\alpha}{}^{i}\lambda{}_{\alpha}{}^{j} -\frac{3}{4}\rho^{-4}Y{}^{k}{}^{i}(\gamma{}^{a}){}^{\alpha}{}^{\beta}\big(\mathcal D_{a}\rho\big)\lambda{}_{\alpha}{}^{j}\lambda{}_{\beta}{}_{k}\\
&-\frac{3}{4}\rho^{-4}Y{}^{k}{}^{j}(\gamma{}^{a}){}^{\alpha}{}^{\beta}\big(\mathcal D_{a}\rho\big)\lambda{}_{\alpha}{}^{i}\lambda{}_{\beta}{}_{k} -\frac{3}{4}\rho^{-4}(\gamma{}^{a}){}^{\alpha}{}^{\beta}\widehat F{}_{a}{}_{b}\big(\mathcal D^{b}\rho\big)\lambda{}_{\alpha}{}^{i}\lambda{}_{\beta}{}^{j}\\
&-\frac{3i}{16}\rho^{-4}\widehat F{}^{a}{}^{b}\widehat F{}_{a}{}_{b}\lambda{}^{\alpha}{}^{i}\lambda{}_{\alpha}{}^{j} -\frac{3}{32}\rho^{-4}(\gamma{}_{a}){}^{\alpha}{}^{\beta}\widehat F{}_{b}{}_{c}\widehat F{}_{d}{}_{e}\epsilon{}^{a}{}^{b}{}^{c}{}^{d}{}^{e}\lambda{}_{\alpha}{}^{i}\lambda{}_{\beta}{}^{j}\\
&-\frac{3i}{8}\rho^{-4}Y{}^{i}{}^{j}(\gamma{}_{a}{}_{b}){}^{\alpha}{}^{\beta}\widehat F{}^{a}{}^{b}\lambda{}_{\alpha}{}^{k}\lambda{}_{\beta}{}_{k} +\frac{3i}{2}\rho^{-4}Y{}^{i}{}^{j}Y{}^{k}{}^{l}\lambda{}^{\alpha}{}_{k}\lambda{}_{\alpha}{}_{l}\\
&+\frac{3i}{4}\rho^{-4}Y{}^{k}{}^{l}Y{}_{k}{}_{l}\lambda{}^{\alpha}{}^{i}\lambda{}_{\alpha}{}^{j} +\text{ high fermi terms}
\end{aligned}
\tag{S6-L-001}
```

<!-- PROJECTED_L_END -->

### 7.2 The spinor

1,520 displayed monomials after collecting identical contractions. All consecutive displays below continue the same sum.

<!-- PROJECTED_phi_BEGIN -->

```math
\begin{aligned}
\fbox{$\displaystyle{\varphi_{\log\alpha}^i}$}={}&\frac{8}{9}R(V){}^{a}{}^{b}{}^{i}{}^{j}(\gamma{}_{a}{}_{b}){}_{\alpha}{}^{\beta}\chi{}_{\beta}{}_{j} +\frac{8}{9}R(V){}^{a}{}^{b}{}^{i}{}^{j}(\gamma{}_{a}{}_{b}){}^{\beta}{}_{\alpha}\chi{}_{\beta}{}_{j}\\
&-\frac{1}{9}(\gamma{}^{a}{}^{b}){}^{\beta}{}^{\gamma}(\gamma{}^{c}{}^{d}){}_{\alpha}{}_{\delta}(\gamma{}^{e}{}^{f}){}_{\beta}{}_{\gamma}T{}_{a}{}_{b}T{}_{c}{}_{d}R(Q){}_{e}{}_{f}{}^{\delta}{}^{i} +\frac{56}{27}(\gamma{}^{a}{}^{b}){}^{\beta}{}^{\gamma}(\gamma{}^{c}{}^{d}){}_{\beta}{}_{\gamma}T{}_{a}{}_{b}T{}_{c}{}_{d}\chi{}_{\alpha}{}^{i}\\
&+\frac{i}{6}(\gamma{}^{a}){}_{\alpha}{}^{\beta}(\gamma{}^{b}{}^{c}){}^{\gamma}{}^{\delta}(\gamma{}^{d}{}^{e}){}_{\gamma}{}_{\delta}T{}_{b}{}_{c}\big(\mathcal D_{a}R(Q){}_{d}{}_{e}{}_{\beta}{}^{i}\big) -\frac{1}{6}(\gamma{}^{a}{}^{b}){}^{\beta}{}^{\gamma}(\gamma{}^{c}{}^{d}){}_{\beta}{}^{\delta}(\gamma{}^{e}{}^{f}){}_{\gamma}{}_{\alpha}T{}_{a}{}_{b}T{}_{c}{}_{d}R(Q){}_{e}{}_{f}{}_{\delta}{}^{i}\\
&-\frac{1}{18}(\gamma{}^{a}{}^{b}){}^{\beta}{}^{\gamma}(\gamma{}^{c}{}^{d}){}_{\alpha}{}^{\delta}(\gamma{}^{e}{}^{f}){}_{\delta}{}_{\beta}T{}_{c}{}_{d}T{}_{a}{}_{b}R(Q){}_{e}{}_{f}{}_{\gamma}{}^{i} -\frac{32}{27}(\gamma{}^{a}{}^{b}){}^{\beta}{}^{\gamma}(\gamma{}^{c}{}^{d}){}_{\alpha}{}_{\beta}T{}_{a}{}_{b}T{}_{c}{}_{d}\chi{}_{\gamma}{}^{i}\\
&-\frac{32}{9}(\gamma{}^{a}{}^{b}){}_{\alpha}{}^{\beta}(\gamma{}^{c}{}^{d}){}_{\beta}{}_{\gamma}T{}_{a}{}_{b}T{}_{c}{}_{d}\chi{}^{\gamma}{}^{i} +\frac{i}{12}(\gamma{}^{a}){}_{\beta}{}^{\gamma}(\gamma{}^{b}{}^{c}){}^{\beta}{}^{\delta}(\gamma{}^{d}{}^{e}){}_{\delta}{}_{\alpha}T{}_{b}{}_{c}\big(\mathcal D_{a}R(Q){}_{d}{}_{e}{}_{\gamma}{}^{i}\big)\\
&+\frac{16i}{9}(\gamma{}^{a}){}_{\alpha}{}_{\beta}(\gamma{}^{b}{}^{c}){}^{\beta}{}^{\gamma}T{}_{b}{}_{c}\big(\mathcal D_{a}\chi{}_{\gamma}{}^{i}\big) -\frac{16i}{9}(\gamma{}^{a}){}_{\beta}{}_{\gamma}(\gamma{}^{b}{}^{c}){}_{\alpha}{}^{\beta}T{}_{b}{}_{c}\big(\mathcal D_{a}\chi{}^{\gamma}{}^{i}\big)\\
&-\frac{1}{6}(\gamma{}^{a}{}^{b}){}^{\beta}{}^{\gamma}(\gamma{}^{c}{}^{d}){}_{\gamma}{}^{\delta}(\gamma{}^{e}{}^{f}){}_{\beta}{}_{\alpha}T{}_{a}{}_{b}T{}_{c}{}_{d}R(Q){}_{e}{}_{f}{}_{\delta}{}^{i} -\frac{1}{18}(\gamma{}^{a}{}^{b}){}^{\beta}{}^{\gamma}(\gamma{}^{c}{}^{d}){}^{\delta}{}_{\alpha}(\gamma{}^{e}{}^{f}){}_{\delta}{}_{\beta}T{}_{c}{}_{d}T{}_{a}{}_{b}R(Q){}_{e}{}_{f}{}_{\gamma}{}^{i}\\
&-\frac{32}{27}(\gamma{}^{a}{}^{b}){}^{\beta}{}^{\gamma}(\gamma{}^{c}{}^{d}){}_{\alpha}{}_{\gamma}T{}_{a}{}_{b}T{}_{c}{}_{d}\chi{}_{\beta}{}^{i} -\frac{32}{9}(\gamma{}^{a}{}^{b}){}^{\beta}{}_{\alpha}(\gamma{}^{c}{}^{d}){}_{\beta}{}_{\gamma}T{}_{a}{}_{b}T{}_{c}{}_{d}\chi{}^{\gamma}{}^{i}\\
&+\frac{i}{12}(\gamma{}^{a}){}_{\beta}{}^{\gamma}(\gamma{}^{b}{}^{c}){}^{\delta}{}^{\beta}(\gamma{}^{d}{}^{e}){}_{\delta}{}_{\alpha}T{}_{b}{}_{c}\big(\mathcal D_{a}R(Q){}_{d}{}_{e}{}_{\gamma}{}^{i}\big) +\frac{16i}{9}(\gamma{}^{a}){}_{\alpha}{}_{\beta}(\gamma{}^{b}{}^{c}){}^{\gamma}{}^{\beta}T{}_{b}{}_{c}\big(\mathcal D_{a}\chi{}_{\gamma}{}^{i}\big)\\
&-\frac{16i}{9}(\gamma{}^{a}){}_{\beta}{}_{\gamma}(\gamma{}^{b}{}^{c}){}^{\beta}{}_{\alpha}T{}_{b}{}_{c}\big(\mathcal D_{a}\chi{}^{\gamma}{}^{i}\big) +\frac{1}{9}(\gamma{}^{a}{}^{b}){}^{\beta}{}^{\gamma}(\gamma{}^{c}{}^{d}){}_{\alpha}{}_{\delta}(\gamma{}^{e}{}^{f}){}_{\beta}{}_{\gamma}\varepsilon{}^{j}{}^{k}\varepsilon{}_{k}{}_{j}T{}_{a}{}_{b}T{}_{c}{}_{d}R(Q){}_{e}{}_{f}{}^{\delta}{}^{i}\\
&-\frac{56}{27}(\gamma{}^{a}{}^{b}){}^{\beta}{}^{\gamma}(\gamma{}^{c}{}^{d}){}_{\beta}{}_{\gamma}\varepsilon{}^{j}{}^{k}\varepsilon{}_{k}{}_{j}T{}_{a}{}_{b}T{}_{c}{}_{d}\chi{}_{\alpha}{}^{i} -\frac{i}{6}(\gamma{}^{a}){}_{\alpha}{}^{\beta}(\gamma{}^{b}{}^{c}){}^{\gamma}{}^{\delta}(\gamma{}^{d}{}^{e}){}_{\gamma}{}_{\delta}\varepsilon{}^{j}{}^{k}\varepsilon{}_{k}{}_{j}T{}_{b}{}_{c}\big(\mathcal D_{a}R(Q){}_{d}{}_{e}{}_{\beta}{}^{i}\big)\\
&+\frac{1}{6}(\gamma{}^{a}{}^{b}){}^{\beta}{}^{\gamma}(\gamma{}^{c}{}^{d}){}_{\beta}{}^{\delta}(\gamma{}^{e}{}^{f}){}_{\gamma}{}_{\alpha}\varepsilon{}^{j}{}^{k}\varepsilon{}_{k}{}_{j}T{}_{a}{}_{b}T{}_{c}{}_{d}R(Q){}_{e}{}_{f}{}_{\delta}{}^{i} +\frac{1}{18}(\gamma{}^{a}{}^{b}){}^{\beta}{}^{\gamma}(\gamma{}^{c}{}^{d}){}_{\alpha}{}^{\delta}(\gamma{}^{e}{}^{f}){}_{\delta}{}_{\beta}\varepsilon{}^{j}{}^{k}\varepsilon{}_{k}{}_{j}T{}_{c}{}_{d}T{}_{a}{}_{b}R(Q){}_{e}{}_{f}{}_{\gamma}{}^{i}\\
&+\frac{32}{27}(\gamma{}^{a}{}^{b}){}^{\beta}{}^{\gamma}(\gamma{}^{c}{}^{d}){}_{\alpha}{}_{\beta}\varepsilon{}^{j}{}^{k}\varepsilon{}_{k}{}_{j}T{}_{a}{}_{b}T{}_{c}{}_{d}\chi{}_{\gamma}{}^{i} +\frac{32}{9}(\gamma{}^{a}{}^{b}){}_{\alpha}{}^{\beta}(\gamma{}^{c}{}^{d}){}_{\beta}{}_{\gamma}\varepsilon{}^{j}{}^{k}\varepsilon{}_{k}{}_{j}T{}_{a}{}_{b}T{}_{c}{}_{d}\chi{}^{\gamma}{}^{i}\\
&-\frac{i}{12}(\gamma{}^{a}){}_{\beta}{}^{\gamma}(\gamma{}^{b}{}^{c}){}^{\beta}{}^{\delta}(\gamma{}^{d}{}^{e}){}_{\delta}{}_{\alpha}\varepsilon{}^{j}{}^{k}\varepsilon{}_{k}{}_{j}T{}_{b}{}_{c}\big(\mathcal D_{a}R(Q){}_{d}{}_{e}{}_{\gamma}{}^{i}\big) -\frac{16i}{9}(\gamma{}^{a}){}_{\alpha}{}_{\beta}(\gamma{}^{b}{}^{c}){}^{\beta}{}^{\gamma}\varepsilon{}^{j}{}^{k}\varepsilon{}_{k}{}_{j}T{}_{b}{}_{c}\big(\mathcal D_{a}\chi{}_{\gamma}{}^{i}\big)\\
&+\frac{16i}{9}(\gamma{}^{a}){}_{\beta}{}_{\gamma}(\gamma{}^{b}{}^{c}){}_{\alpha}{}^{\beta}\varepsilon{}^{j}{}^{k}\varepsilon{}_{k}{}_{j}T{}_{b}{}_{c}\big(\mathcal D_{a}\chi{}^{\gamma}{}^{i}\big) +\frac{1}{6}(\gamma{}^{a}{}^{b}){}^{\beta}{}^{\gamma}(\gamma{}^{c}{}^{d}){}_{\gamma}{}^{\delta}(\gamma{}^{e}{}^{f}){}_{\beta}{}_{\alpha}\varepsilon{}^{j}{}^{k}\varepsilon{}_{k}{}_{j}T{}_{a}{}_{b}T{}_{c}{}_{d}R(Q){}_{e}{}_{f}{}_{\delta}{}^{i}\\
&+\frac{1}{18}(\gamma{}^{a}{}^{b}){}^{\beta}{}^{\gamma}(\gamma{}^{c}{}^{d}){}^{\delta}{}_{\alpha}(\gamma{}^{e}{}^{f}){}_{\delta}{}_{\beta}\varepsilon{}^{j}{}^{k}\varepsilon{}_{k}{}_{j}T{}_{c}{}_{d}T{}_{a}{}_{b}R(Q){}_{e}{}_{f}{}_{\gamma}{}^{i} +\frac{32}{27}(\gamma{}^{a}{}^{b}){}^{\beta}{}^{\gamma}(\gamma{}^{c}{}^{d}){}_{\alpha}{}_{\gamma}\varepsilon{}^{j}{}^{k}\varepsilon{}_{k}{}_{j}T{}_{a}{}_{b}T{}_{c}{}_{d}\chi{}_{\beta}{}^{i}\\
&+\frac{32}{9}(\gamma{}^{a}{}^{b}){}^{\beta}{}_{\alpha}(\gamma{}^{c}{}^{d}){}_{\beta}{}_{\gamma}\varepsilon{}^{j}{}^{k}\varepsilon{}_{k}{}_{j}T{}_{a}{}_{b}T{}_{c}{}_{d}\chi{}^{\gamma}{}^{i} -\frac{i}{12}(\gamma{}^{a}){}_{\beta}{}^{\gamma}(\gamma{}^{b}{}^{c}){}^{\delta}{}^{\beta}(\gamma{}^{d}{}^{e}){}_{\delta}{}_{\alpha}\varepsilon{}^{j}{}^{k}\varepsilon{}_{k}{}_{j}T{}_{b}{}_{c}\big(\mathcal D_{a}R(Q){}_{d}{}_{e}{}_{\gamma}{}^{i}\big)\\
&-\frac{16i}{9}(\gamma{}^{a}){}_{\alpha}{}_{\beta}(\gamma{}^{b}{}^{c}){}^{\gamma}{}^{\beta}\varepsilon{}^{j}{}^{k}\varepsilon{}_{k}{}_{j}T{}_{b}{}_{c}\big(\mathcal D_{a}\chi{}_{\gamma}{}^{i}\big) +\frac{16i}{9}(\gamma{}^{a}){}_{\beta}{}_{\gamma}(\gamma{}^{b}{}^{c}){}^{\beta}{}_{\alpha}\varepsilon{}^{j}{}^{k}\varepsilon{}_{k}{}_{j}T{}_{b}{}_{c}\big(\mathcal D_{a}\chi{}^{\gamma}{}^{i}\big)\\
&-\frac{17}{9}R(V){}_{a}{}_{b}{}_{j}{}^{i}(\gamma{}^{a}{}^{b}){}_{\alpha}{}^{\beta}\chi{}_{\beta}{}^{j} -\frac{16}{9}D\chi{}_{\alpha}{}^{i}\\
&-\frac{34i}{3}(\gamma{}^{a}){}_{\alpha}{}^{\beta}(\gamma{}^{b}{}^{c}){}^{\gamma}{}_{\beta}\big(\mathcal D_{a}T{}_{b}{}_{c}\big)\chi{}_{\gamma}{}^{i} -\frac{544}{27}(\gamma{}^{a}{}^{b}){}^{\beta}{}_{\gamma}(\gamma{}^{c}{}^{d}){}_{\alpha}{}^{\gamma}T{}_{c}{}_{d}T{}_{a}{}_{b}\chi{}_{\beta}{}^{i}\\
&+\frac{10i}{3}(\gamma{}^{a}){}^{\beta}{}^{\gamma}(\gamma{}^{b}{}^{c}){}_{\alpha}{}_{\gamma}\big(\mathcal D_{a}T{}_{b}{}_{c}\big)\chi{}_{\beta}{}^{i} +\frac{17}{9}R(V){}_{a}{}_{b}{}_{j}{}^{j}(\gamma{}^{a}{}^{b}){}_{\alpha}{}_{\beta}\chi{}^{\beta}{}^{i}\\
&+\frac{16}{9}D\varepsilon{}^{j}{}^{k}\varepsilon{}_{k}{}_{j}\chi{}_{\alpha}{}^{i} -\frac{34i}{3}(\gamma{}^{a}){}_{\alpha}{}^{\beta}(\gamma{}^{b}{}^{c}){}_{\gamma}{}_{\beta}\varepsilon{}^{j}{}^{k}\varepsilon{}_{k}{}_{j}\big(\mathcal D_{a}T{}_{b}{}_{c}\big)\chi{}^{\gamma}{}^{i}\\
&-\frac{544}{27}(\gamma{}^{a}{}^{b}){}_{\alpha}{}^{\beta}(\gamma{}^{c}{}^{d}){}_{\gamma}{}_{\beta}\varepsilon{}^{j}{}^{k}\varepsilon{}_{k}{}_{j}T{}_{a}{}_{b}T{}_{c}{}_{d}\chi{}^{\gamma}{}^{i} -\frac{34i}{9}(\gamma{}^{a}){}_{\beta}{}^{\gamma}(\gamma{}^{b}{}^{c}){}_{\alpha}{}_{\gamma}\varepsilon{}^{j}{}^{k}\varepsilon{}_{k}{}_{j}\big(\mathcal D_{a}T{}_{b}{}_{c}\big)\chi{}^{\beta}{}^{i}\\
&-8\rho^{-2}Y{}^{i}{}^{j}D\lambda{}_{\alpha}{}_{j} +\frac{8i}{3}\rho^{-1}D(\gamma{}^{a}){}_{\alpha}{}^{\beta}\big(\mathcal D_{a}\lambda{}_{\beta}{}^{i}\big)\\
&-\frac{8}{3}\rho^{-1}D(\gamma{}^{a}{}^{b}){}_{\alpha}{}_{\beta}T{}_{a}{}_{b}\lambda{}^{\beta}{}^{i} -\frac{8i}{3}\rho^{-1}D(\gamma{}^{a}){}_{\alpha}{}^{\beta}\varepsilon{}^{j}{}^{k}\varepsilon{}_{k}{}_{j}\big(\mathcal D_{a}\lambda{}_{\beta}{}^{i}\big)\\
&-\frac{8}{9}\rho^{-1}D(\gamma{}^{a}{}^{b}){}_{\alpha}{}_{\beta}\varepsilon{}^{j}{}^{k}\varepsilon{}_{k}{}_{j}T{}_{a}{}_{b}\lambda{}^{\beta}{}^{i} -\frac{128i}{9}\rho^{-1}Y{}^{i}{}^{j}(\gamma{}^{a}){}_{\alpha}{}^{\beta}\big(\mathcal D_{a}\chi{}_{\beta}{}_{j}\big)\\
&-\frac{56}{3}\rho^{-1}Y{}^{i}{}^{j}(\gamma{}^{a}{}^{b}){}_{\alpha}{}^{\beta}T{}_{a}{}_{b}\chi{}_{\beta}{}_{j} +\frac{1}{3}\rho^{-2}R(V){}^{a}{}^{b}{}^{i}{}^{j}\widehat F{}_{a}{}_{b}\lambda{}_{\alpha}{}_{j}\\
&-\frac{i}{12}\rho^{-1}R(V){}^{a}{}^{b}{}^{i}{}^{j}(\gamma{}^{c}){}_{\alpha}{}_{\beta}(\gamma{}_{a}{}_{b}){}^{\beta}{}^{\gamma}\big(\mathcal D_{c}\lambda{}_{\gamma}{}_{j}\big) -\frac{i}{12}\rho^{-1}R(V){}^{a}{}^{b}{}^{i}{}^{j}(\gamma{}^{c}){}_{\beta}{}^{\gamma}(\gamma{}_{a}{}_{b}){}_{\alpha}{}^{\beta}\big(\mathcal D_{c}\lambda{}_{\gamma}{}_{j}\big)\\
&+\frac{1}{18}\rho^{-1}R(V){}^{a}{}^{b}{}^{i}{}^{j}(\gamma{}^{c}{}^{d}){}_{\alpha}{}_{\beta}(\gamma{}_{a}{}_{b}){}^{\beta}{}^{\gamma}T{}_{c}{}_{d}\lambda{}_{\gamma}{}_{j} -\frac{1}{6}\rho^{-1}R(V){}^{a}{}^{b}{}^{i}{}^{j}(\gamma{}^{c}{}^{d}){}_{\beta}{}^{\gamma}(\gamma{}_{a}{}_{b}){}_{\alpha}{}^{\beta}T{}_{c}{}_{d}\lambda{}_{\gamma}{}_{j}\\
&-\frac{i}{12}\rho^{-1}R(V){}^{a}{}^{b}{}^{i}{}^{j}(\gamma{}^{c}){}_{\alpha}{}_{\beta}(\gamma{}_{a}{}_{b}){}^{\gamma}{}^{\beta}\big(\mathcal D_{c}\lambda{}_{\gamma}{}_{j}\big) -\frac{i}{12}\rho^{-1}R(V){}^{a}{}^{b}{}^{i}{}^{j}(\gamma{}^{c}){}_{\beta}{}^{\gamma}(\gamma{}_{a}{}_{b}){}^{\beta}{}_{\alpha}\big(\mathcal D_{c}\lambda{}_{\gamma}{}_{j}\big)\\
&+\frac{1}{18}\rho^{-1}R(V){}^{a}{}^{b}{}^{i}{}^{j}(\gamma{}^{c}{}^{d}){}_{\alpha}{}_{\beta}(\gamma{}_{a}{}_{b}){}^{\gamma}{}^{\beta}T{}_{c}{}_{d}\lambda{}_{\gamma}{}_{j} -\frac{1}{6}\rho^{-1}R(V){}^{a}{}^{b}{}^{i}{}^{j}(\gamma{}^{c}{}^{d}){}_{\beta}{}^{\gamma}(\gamma{}_{a}{}_{b}){}^{\beta}{}_{\alpha}T{}_{c}{}_{d}\lambda{}_{\gamma}{}_{j}\\
&-\frac{1}{3}\rho^{-1}R(V){}^{a}{}^{b}{}^{i}{}^{j}(\gamma{}^{c}{}^{d}){}_{\beta}{}_{\gamma}(\gamma{}_{a}{}_{b}){}^{\beta}{}^{\gamma}T{}_{c}{}_{d}\lambda{}_{\alpha}{}_{j} +\frac{1}{48}\rho^{-1}(\gamma{}^{a}{}^{b}){}^{\beta}{}^{\gamma}(\gamma{}^{c}{}^{d}){}_{\alpha}{}_{\delta}(\gamma{}^{e}{}^{f}){}_{\beta}{}_{\gamma}\widehat F{}_{a}{}_{b}T{}_{c}{}_{d}R(Q){}_{e}{}_{f}{}^{\delta}{}^{i}\\
&-\frac{4}{3}\rho^{-1}(\gamma{}^{a}{}^{b}){}^{\beta}{}^{\gamma}(\gamma{}^{c}{}^{d}){}_{\beta}{}_{\gamma}\widehat F{}_{a}{}_{b}T{}_{c}{}_{d}\chi{}_{\alpha}{}^{i} -\frac{i}{32}\rho^{-1}(\gamma{}^{a}){}_{\alpha}{}^{\beta}(\gamma{}^{b}{}^{c}){}^{\gamma}{}^{\delta}(\gamma{}^{d}{}^{e}){}_{\gamma}{}_{\delta}\widehat F{}_{b}{}_{c}\big(\mathcal D_{a}R(Q){}_{d}{}_{e}{}_{\beta}{}^{i}\big)\\
&+\frac{1}{32}\rho^{-1}(\gamma{}^{a}{}^{b}){}^{\beta}{}^{\gamma}(\gamma{}^{c}{}^{d}){}_{\beta}{}^{\delta}(\gamma{}^{e}{}^{f}){}_{\gamma}{}_{\alpha}\widehat F{}_{a}{}_{b}T{}_{c}{}_{d}R(Q){}_{e}{}_{f}{}_{\delta}{}^{i} +\frac{1}{96}\rho^{-1}(\gamma{}^{a}{}^{b}){}^{\beta}{}^{\gamma}(\gamma{}^{c}{}^{d}){}_{\alpha}{}^{\delta}(\gamma{}^{e}{}^{f}){}_{\delta}{}_{\beta}\widehat F{}_{c}{}_{d}T{}_{a}{}_{b}R(Q){}_{e}{}_{f}{}_{\gamma}{}^{i}\\
&+\frac{2}{9}\rho^{-1}(\gamma{}^{a}{}^{b}){}^{\beta}{}^{\gamma}(\gamma{}^{c}{}^{d}){}_{\alpha}{}_{\beta}\widehat F{}_{a}{}_{b}T{}_{c}{}_{d}\chi{}_{\gamma}{}^{i} +\frac{2}{3}\rho^{-1}(\gamma{}^{a}{}^{b}){}_{\alpha}{}^{\beta}(\gamma{}^{c}{}^{d}){}_{\beta}{}_{\gamma}\widehat F{}_{a}{}_{b}T{}_{c}{}_{d}\chi{}^{\gamma}{}^{i}\\
&-\frac{i}{64}\rho^{-1}(\gamma{}^{a}){}_{\beta}{}^{\gamma}(\gamma{}^{b}{}^{c}){}^{\beta}{}^{\delta}(\gamma{}^{d}{}^{e}){}_{\delta}{}_{\alpha}\widehat F{}_{b}{}_{c}\big(\mathcal D_{a}R(Q){}_{d}{}_{e}{}_{\gamma}{}^{i}\big) -\frac{i}{3}\rho^{-1}(\gamma{}^{a}){}_{\alpha}{}_{\beta}(\gamma{}^{b}{}^{c}){}^{\beta}{}^{\gamma}\widehat F{}_{b}{}_{c}\big(\mathcal D_{a}\chi{}_{\gamma}{}^{i}\big)\\
&+\frac{i}{3}\rho^{-1}(\gamma{}^{a}){}_{\beta}{}_{\gamma}(\gamma{}^{b}{}^{c}){}_{\alpha}{}^{\beta}\widehat F{}_{b}{}_{c}\big(\mathcal D_{a}\chi{}^{\gamma}{}^{i}\big) +\frac{1}{32}\rho^{-1}(\gamma{}^{a}{}^{b}){}^{\beta}{}^{\gamma}(\gamma{}^{c}{}^{d}){}_{\gamma}{}^{\delta}(\gamma{}^{e}{}^{f}){}_{\beta}{}_{\alpha}\widehat F{}_{a}{}_{b}T{}_{c}{}_{d}R(Q){}_{e}{}_{f}{}_{\delta}{}^{i}\\
&+\frac{1}{96}\rho^{-1}(\gamma{}^{a}{}^{b}){}^{\beta}{}^{\gamma}(\gamma{}^{c}{}^{d}){}^{\delta}{}_{\alpha}(\gamma{}^{e}{}^{f}){}_{\delta}{}_{\beta}\widehat F{}_{c}{}_{d}T{}_{a}{}_{b}R(Q){}_{e}{}_{f}{}_{\gamma}{}^{i} +\frac{2}{9}\rho^{-1}(\gamma{}^{a}{}^{b}){}^{\beta}{}^{\gamma}(\gamma{}^{c}{}^{d}){}_{\alpha}{}_{\gamma}\widehat F{}_{a}{}_{b}T{}_{c}{}_{d}\chi{}_{\beta}{}^{i}\\
&+\frac{2}{3}\rho^{-1}(\gamma{}^{a}{}^{b}){}^{\beta}{}_{\alpha}(\gamma{}^{c}{}^{d}){}_{\beta}{}_{\gamma}\widehat F{}_{a}{}_{b}T{}_{c}{}_{d}\chi{}^{\gamma}{}^{i} -\frac{i}{64}\rho^{-1}(\gamma{}^{a}){}_{\beta}{}^{\gamma}(\gamma{}^{b}{}^{c}){}^{\delta}{}^{\beta}(\gamma{}^{d}{}^{e}){}_{\delta}{}_{\alpha}\widehat F{}_{b}{}_{c}\big(\mathcal D_{a}R(Q){}_{d}{}_{e}{}_{\gamma}{}^{i}\big)\\
&-\frac{i}{3}\rho^{-1}(\gamma{}^{a}){}_{\alpha}{}_{\beta}(\gamma{}^{b}{}^{c}){}^{\gamma}{}^{\beta}\widehat F{}_{b}{}_{c}\big(\mathcal D_{a}\chi{}_{\gamma}{}^{i}\big) +\frac{i}{3}\rho^{-1}(\gamma{}^{a}){}_{\beta}{}_{\gamma}(\gamma{}^{b}{}^{c}){}^{\beta}{}_{\alpha}\widehat F{}_{b}{}_{c}\big(\mathcal D_{a}\chi{}^{\gamma}{}^{i}\big)
\end{aligned}
\tag{S6-phi-001}
```

```math
\begin{aligned}
&-\frac{1}{48}\rho^{-1}(\gamma{}^{a}{}^{b}){}^{\beta}{}^{\gamma}(\gamma{}^{c}{}^{d}){}_{\alpha}{}_{\delta}(\gamma{}^{e}{}^{f}){}_{\beta}{}_{\gamma}\widehat F{}_{a}{}_{b}\varepsilon{}^{j}{}^{k}\varepsilon{}_{k}{}_{j}T{}_{c}{}_{d}R(Q){}_{e}{}_{f}{}^{\delta}{}^{i} +\frac{4}{3}\rho^{-1}(\gamma{}^{a}{}^{b}){}^{\beta}{}^{\gamma}(\gamma{}^{c}{}^{d}){}_{\beta}{}_{\gamma}\widehat F{}_{a}{}_{b}\varepsilon{}^{j}{}^{k}\varepsilon{}_{k}{}_{j}T{}_{c}{}_{d}\chi{}_{\alpha}{}^{i}\\
&+\frac{i}{32}\rho^{-1}(\gamma{}^{a}){}_{\alpha}{}^{\beta}(\gamma{}^{b}{}^{c}){}^{\gamma}{}^{\delta}(\gamma{}^{d}{}^{e}){}_{\gamma}{}_{\delta}\widehat F{}_{b}{}_{c}\varepsilon{}^{j}{}^{k}\varepsilon{}_{k}{}_{j}\big(\mathcal D_{a}R(Q){}_{d}{}_{e}{}_{\beta}{}^{i}\big) -\frac{1}{32}\rho^{-1}(\gamma{}^{a}{}^{b}){}^{\beta}{}^{\gamma}(\gamma{}^{c}{}^{d}){}_{\beta}{}^{\delta}(\gamma{}^{e}{}^{f}){}_{\gamma}{}_{\alpha}\widehat F{}_{a}{}_{b}\varepsilon{}^{j}{}^{k}\varepsilon{}_{k}{}_{j}T{}_{c}{}_{d}R(Q){}_{e}{}_{f}{}_{\delta}{}^{i}\\
&-\frac{1}{96}\rho^{-1}(\gamma{}^{a}{}^{b}){}^{\beta}{}^{\gamma}(\gamma{}^{c}{}^{d}){}_{\alpha}{}^{\delta}(\gamma{}^{e}{}^{f}){}_{\delta}{}_{\beta}\widehat F{}_{c}{}_{d}\varepsilon{}^{j}{}^{k}\varepsilon{}_{k}{}_{j}T{}_{a}{}_{b}R(Q){}_{e}{}_{f}{}_{\gamma}{}^{i} -\frac{2}{9}\rho^{-1}(\gamma{}^{a}{}^{b}){}^{\beta}{}^{\gamma}(\gamma{}^{c}{}^{d}){}_{\alpha}{}_{\beta}\widehat F{}_{a}{}_{b}\varepsilon{}^{j}{}^{k}\varepsilon{}_{k}{}_{j}T{}_{c}{}_{d}\chi{}_{\gamma}{}^{i}\\
&-\frac{2}{3}\rho^{-1}(\gamma{}^{a}{}^{b}){}_{\alpha}{}^{\beta}(\gamma{}^{c}{}^{d}){}_{\beta}{}_{\gamma}\widehat F{}_{a}{}_{b}\varepsilon{}^{j}{}^{k}\varepsilon{}_{k}{}_{j}T{}_{c}{}_{d}\chi{}^{\gamma}{}^{i} +\frac{i}{64}\rho^{-1}(\gamma{}^{a}){}_{\beta}{}^{\gamma}(\gamma{}^{b}{}^{c}){}^{\beta}{}^{\delta}(\gamma{}^{d}{}^{e}){}_{\delta}{}_{\alpha}\widehat F{}_{b}{}_{c}\varepsilon{}^{j}{}^{k}\varepsilon{}_{k}{}_{j}\big(\mathcal D_{a}R(Q){}_{d}{}_{e}{}_{\gamma}{}^{i}\big)\\
&+\frac{i}{3}\rho^{-1}(\gamma{}^{a}){}_{\alpha}{}_{\beta}(\gamma{}^{b}{}^{c}){}^{\beta}{}^{\gamma}\widehat F{}_{b}{}_{c}\varepsilon{}^{j}{}^{k}\varepsilon{}_{k}{}_{j}\big(\mathcal D_{a}\chi{}_{\gamma}{}^{i}\big) -\frac{i}{3}\rho^{-1}(\gamma{}^{a}){}_{\beta}{}_{\gamma}(\gamma{}^{b}{}^{c}){}_{\alpha}{}^{\beta}\widehat F{}_{b}{}_{c}\varepsilon{}^{j}{}^{k}\varepsilon{}_{k}{}_{j}\big(\mathcal D_{a}\chi{}^{\gamma}{}^{i}\big)\\
&-\frac{1}{32}\rho^{-1}(\gamma{}^{a}{}^{b}){}^{\beta}{}^{\gamma}(\gamma{}^{c}{}^{d}){}_{\gamma}{}^{\delta}(\gamma{}^{e}{}^{f}){}_{\beta}{}_{\alpha}\widehat F{}_{a}{}_{b}\varepsilon{}^{j}{}^{k}\varepsilon{}_{k}{}_{j}T{}_{c}{}_{d}R(Q){}_{e}{}_{f}{}_{\delta}{}^{i} -\frac{1}{96}\rho^{-1}(\gamma{}^{a}{}^{b}){}^{\beta}{}^{\gamma}(\gamma{}^{c}{}^{d}){}^{\delta}{}_{\alpha}(\gamma{}^{e}{}^{f}){}_{\delta}{}_{\beta}\widehat F{}_{c}{}_{d}\varepsilon{}^{j}{}^{k}\varepsilon{}_{k}{}_{j}T{}_{a}{}_{b}R(Q){}_{e}{}_{f}{}_{\gamma}{}^{i}\\
&-\frac{2}{9}\rho^{-1}(\gamma{}^{a}{}^{b}){}^{\beta}{}^{\gamma}(\gamma{}^{c}{}^{d}){}_{\alpha}{}_{\gamma}\widehat F{}_{a}{}_{b}\varepsilon{}^{j}{}^{k}\varepsilon{}_{k}{}_{j}T{}_{c}{}_{d}\chi{}_{\beta}{}^{i} -\frac{2}{3}\rho^{-1}(\gamma{}^{a}{}^{b}){}^{\beta}{}_{\alpha}(\gamma{}^{c}{}^{d}){}_{\beta}{}_{\gamma}\widehat F{}_{a}{}_{b}\varepsilon{}^{j}{}^{k}\varepsilon{}_{k}{}_{j}T{}_{c}{}_{d}\chi{}^{\gamma}{}^{i}\\
&+\frac{i}{64}\rho^{-1}(\gamma{}^{a}){}_{\beta}{}^{\gamma}(\gamma{}^{b}{}^{c}){}^{\delta}{}^{\beta}(\gamma{}^{d}{}^{e}){}_{\delta}{}_{\alpha}\widehat F{}_{b}{}_{c}\varepsilon{}^{j}{}^{k}\varepsilon{}_{k}{}_{j}\big(\mathcal D_{a}R(Q){}_{d}{}_{e}{}_{\gamma}{}^{i}\big) +\frac{i}{3}\rho^{-1}(\gamma{}^{a}){}_{\alpha}{}_{\beta}(\gamma{}^{b}{}^{c}){}^{\gamma}{}^{\beta}\widehat F{}_{b}{}_{c}\varepsilon{}^{j}{}^{k}\varepsilon{}_{k}{}_{j}\big(\mathcal D_{a}\chi{}_{\gamma}{}^{i}\big)\\
&-\frac{i}{3}\rho^{-1}(\gamma{}^{a}){}_{\beta}{}_{\gamma}(\gamma{}^{b}{}^{c}){}^{\beta}{}_{\alpha}\widehat F{}_{b}{}_{c}\varepsilon{}^{j}{}^{k}\varepsilon{}_{k}{}_{j}\big(\mathcal D_{a}\chi{}^{\gamma}{}^{i}\big) -\frac{2}{3}\rho^{-2}\big(\mathcal D^{a}\mathcal D_{a}Y{}^{i}{}^{j}\big)\lambda{}_{\alpha}{}_{j}\\
&+\frac{i}{3}\rho^{-1}(\gamma{}^{a}){}_{\alpha}{}^{\beta}\big(\mathcal D^{b}\mathcal D_{b}\mathcal D_{a}\lambda{}_{\beta}{}^{i}\big) +\frac{2}{9}\rho^{-1}(\gamma{}^{a}{}^{b}){}_{\alpha}{}_{\beta}\big(\mathcal D^{c}\mathcal D_{c}T{}_{a}{}_{b}\big)\lambda{}^{\beta}{}^{i}\\
&-\frac{2}{9}\rho^{-1}(\gamma{}^{a}{}^{b}){}_{\alpha}{}_{\beta}\big(\mathcal D_{c}T{}_{a}{}_{b}\big)\big(\mathcal D^{c}\lambda{}^{\beta}{}^{i}\big) -\frac{2}{9}\rho^{-1}(\gamma{}^{a}{}^{b}){}_{\alpha}{}_{\beta}\big(\mathcal D^{c}T{}_{a}{}_{b}\big)\big(\mathcal D_{c}\lambda{}^{\beta}{}^{i}\big)\\
&-\frac{2}{9}\rho^{-1}(\gamma{}^{a}{}^{b}){}_{\alpha}{}_{\beta}T{}_{a}{}_{b}\big(\mathcal D^{c}\mathcal D_{c}\lambda{}^{\beta}{}^{i}\big) -\frac{8}{3}\big(\mathcal D^{a}\mathcal D_{a}\chi{}_{\alpha}{}^{i}\big)\\
&-\frac{8}{3}\rho^{-1}\big(\mathcal D_{a}\rho\big)\big(\mathcal D^{a}\chi{}_{\alpha}{}^{i}\big) -\frac{i}{3}\rho^{-1}(\gamma{}^{a}){}_{\alpha}{}^{\beta}\varepsilon{}^{j}{}^{k}\varepsilon{}_{k}{}_{j}\big(\mathcal D^{b}\mathcal D_{b}\mathcal D_{a}\lambda{}_{\beta}{}^{i}\big)\\
&-\frac{2}{9}\rho^{-1}(\gamma{}^{a}{}^{b}){}_{\alpha}{}_{\beta}\varepsilon{}^{j}{}^{k}\varepsilon{}_{k}{}_{j}\big(\mathcal D^{c}\mathcal D_{c}T{}_{a}{}_{b}\big)\lambda{}^{\beta}{}^{i} -\frac{2}{9}\rho^{-1}(\gamma{}^{a}{}^{b}){}_{\alpha}{}_{\beta}\varepsilon{}^{j}{}^{k}\varepsilon{}_{k}{}_{j}\big(\mathcal D_{c}T{}_{a}{}_{b}\big)\big(\mathcal D^{c}\lambda{}^{\beta}{}^{i}\big)\\
&+\frac{2}{9}\rho^{-1}(\gamma{}^{a}{}^{b}){}_{\alpha}{}_{\beta}\varepsilon{}^{j}{}^{k}\varepsilon{}_{k}{}_{j}\big(\mathcal D^{c}T{}_{a}{}_{b}\big)\big(\mathcal D_{c}\lambda{}^{\beta}{}^{i}\big) +\frac{2}{9}\rho^{-1}(\gamma{}^{a}{}^{b}){}_{\alpha}{}_{\beta}\varepsilon{}^{j}{}^{k}\varepsilon{}_{k}{}_{j}T{}_{a}{}_{b}\big(\mathcal D^{c}\mathcal D_{c}\lambda{}^{\beta}{}^{i}\big)\\
&+\frac{8}{3}\varepsilon{}^{j}{}^{k}\varepsilon{}_{k}{}_{j}\big(\mathcal D^{a}\mathcal D_{a}\chi{}_{\alpha}{}^{i}\big) +\frac{8}{3}\rho^{-1}\big(\mathcal D_{a}\rho\big)\varepsilon{}^{j}{}^{k}\varepsilon{}_{k}{}_{j}\big(\mathcal D^{a}\chi{}_{\alpha}{}^{i}\big)\\
&-\frac{1}{3}\rho^{-1}(\gamma{}^{a}){}_{\beta}{}^{\gamma}(\gamma{}_{b}){}_{\alpha}{}^{\delta}(\gamma{}^{c}{}^{d}){}_{\delta}{}^{\beta}\big(\mathcal D^{b}T{}_{c}{}_{d}\big)\big(\mathcal D_{a}\lambda{}_{\gamma}{}^{i}\big) -\frac{1}{3}\rho^{-1}(\gamma{}^{a}){}_{\beta}{}^{\gamma}(\gamma{}_{b}){}_{\alpha}{}^{\delta}(\gamma{}^{c}{}^{d}){}_{\delta}{}^{\beta}T{}_{c}{}_{d}\big(\mathcal D^{b}\mathcal D_{a}\lambda{}_{\gamma}{}^{i}\big)\\
&+\frac{1}{9}\rho^{-1}(\gamma{}^{a}){}_{\beta}{}^{\gamma}(\gamma{}_{b}){}_{\delta}{}^{\beta}(\gamma{}^{c}{}^{d}){}_{\alpha}{}^{\delta}T{}_{c}{}_{d}\big(\mathcal D^{b}\mathcal D_{a}\lambda{}_{\gamma}{}^{i}\big) +\frac{2i}{9}\rho^{-1}(\gamma{}_{a}){}_{\alpha}{}^{\beta}(\gamma{}^{b}{}^{c}){}_{\beta}{}^{\gamma}(\gamma{}^{d}{}^{e}){}_{\gamma}{}_{\delta}T{}_{d}{}_{e}\big(\mathcal D^{a}T{}_{b}{}_{c}\big)\lambda{}^{\delta}{}^{i}\\
&+\frac{2i}{9}\rho^{-1}(\gamma{}_{a}){}_{\alpha}{}^{\beta}(\gamma{}^{b}{}^{c}){}_{\beta}{}^{\gamma}(\gamma{}^{d}{}^{e}){}_{\gamma}{}_{\delta}T{}_{b}{}_{c}\big(\mathcal D^{a}T{}_{d}{}_{e}\big)\lambda{}^{\delta}{}^{i} -\frac{2i}{27}\rho^{-1}(\gamma{}_{a}){}_{\beta}{}^{\gamma}(\gamma{}^{b}{}^{c}){}_{\alpha}{}^{\beta}(\gamma{}^{d}{}^{e}){}_{\gamma}{}_{\delta}T{}_{b}{}_{c}\big(\mathcal D^{a}T{}_{d}{}_{e}\big)\lambda{}^{\delta}{}^{i}\\
&-\frac{2i}{9}\rho^{-1}(\gamma{}_{a}){}_{\alpha}{}^{\beta}(\gamma{}^{b}{}^{c}){}_{\beta}{}^{\gamma}(\gamma{}^{d}{}^{e}){}_{\gamma}{}_{\delta}T{}_{b}{}_{c}T{}_{d}{}_{e}\big(\mathcal D^{a}\lambda{}^{\delta}{}^{i}\big) +\frac{2i}{27}\rho^{-1}(\gamma{}_{a}){}_{\beta}{}^{\gamma}(\gamma{}^{b}{}^{c}){}_{\alpha}{}^{\beta}(\gamma{}^{d}{}^{e}){}_{\gamma}{}_{\delta}T{}_{b}{}_{c}T{}_{d}{}_{e}\big(\mathcal D^{a}\lambda{}^{\delta}{}^{i}\big)\\
&-\frac{8i}{3}(\gamma{}_{a}){}_{\alpha}{}^{\beta}(\gamma{}^{b}{}^{c}){}_{\beta}{}^{\gamma}\big(\mathcal D^{a}T{}_{b}{}_{c}\big)\chi{}_{\gamma}{}^{i} -\frac{8i}{3}(\gamma{}_{a}){}_{\alpha}{}^{\beta}(\gamma{}^{b}{}^{c}){}_{\beta}{}^{\gamma}T{}_{b}{}_{c}\big(\mathcal D^{a}\chi{}_{\gamma}{}^{i}\big)\\
&+\frac{8i}{9}(\gamma{}_{a}){}_{\beta}{}^{\gamma}(\gamma{}^{b}{}^{c}){}_{\alpha}{}^{\beta}T{}_{b}{}_{c}\big(\mathcal D^{a}\chi{}_{\gamma}{}^{i}\big) +\frac{1}{3}\rho^{-1}(\gamma{}^{a}){}_{\beta}{}^{\gamma}(\gamma{}_{b}){}_{\alpha}{}^{\delta}(\gamma{}^{c}{}^{d}){}_{\delta}{}^{\beta}\varepsilon{}^{j}{}^{k}\varepsilon{}_{k}{}_{j}\big(\mathcal D^{b}T{}_{c}{}_{d}\big)\big(\mathcal D_{a}\lambda{}_{\gamma}{}^{i}\big)\\
&-\frac{1}{9}\rho^{-1}(\gamma{}^{a}){}_{\beta}{}^{\gamma}(\gamma{}_{b}){}_{\delta}{}^{\beta}(\gamma{}^{c}{}^{d}){}_{\alpha}{}^{\delta}\varepsilon{}^{j}{}^{k}\varepsilon{}_{k}{}_{j}\big(\mathcal D^{b}T{}_{c}{}_{d}\big)\big(\mathcal D_{a}\lambda{}_{\gamma}{}^{i}\big) +\frac{1}{3}\rho^{-1}(\gamma{}^{a}){}_{\beta}{}^{\gamma}(\gamma{}_{b}){}_{\alpha}{}^{\delta}(\gamma{}^{c}{}^{d}){}_{\delta}{}^{\beta}\varepsilon{}^{j}{}^{k}\varepsilon{}_{k}{}_{j}T{}_{c}{}_{d}\big(\mathcal D^{b}\mathcal D_{a}\lambda{}_{\gamma}{}^{i}\big)\\
&-\frac{1}{9}\rho^{-1}(\gamma{}^{a}){}_{\beta}{}^{\gamma}(\gamma{}_{b}){}_{\delta}{}^{\beta}(\gamma{}^{c}{}^{d}){}_{\alpha}{}^{\delta}\varepsilon{}^{j}{}^{k}\varepsilon{}_{k}{}_{j}T{}_{c}{}_{d}\big(\mathcal D^{b}\mathcal D_{a}\lambda{}_{\gamma}{}^{i}\big) -\frac{2i}{9}\rho^{-1}(\gamma{}_{a}){}_{\alpha}{}^{\beta}(\gamma{}^{b}{}^{c}){}_{\beta}{}^{\gamma}(\gamma{}^{d}{}^{e}){}_{\gamma}{}_{\delta}\varepsilon{}^{j}{}^{k}\varepsilon{}_{k}{}_{j}T{}_{d}{}_{e}\big(\mathcal D^{a}T{}_{b}{}_{c}\big)\lambda{}^{\delta}{}^{i}\\
&+\frac{2i}{27}\rho^{-1}(\gamma{}_{a}){}_{\beta}{}^{\gamma}(\gamma{}^{b}{}^{c}){}_{\alpha}{}^{\beta}(\gamma{}^{d}{}^{e}){}_{\gamma}{}_{\delta}\varepsilon{}^{j}{}^{k}\varepsilon{}_{k}{}_{j}T{}_{d}{}_{e}\big(\mathcal D^{a}T{}_{b}{}_{c}\big)\lambda{}^{\delta}{}^{i} -\frac{2i}{9}\rho^{-1}(\gamma{}_{a}){}_{\alpha}{}^{\beta}(\gamma{}^{b}{}^{c}){}_{\beta}{}^{\gamma}(\gamma{}^{d}{}^{e}){}_{\gamma}{}_{\delta}\varepsilon{}^{j}{}^{k}\varepsilon{}_{k}{}_{j}T{}_{b}{}_{c}\big(\mathcal D^{a}T{}_{d}{}_{e}\big)\lambda{}^{\delta}{}^{i}\\
&+\frac{2i}{27}\rho^{-1}(\gamma{}_{a}){}_{\beta}{}^{\gamma}(\gamma{}^{b}{}^{c}){}_{\alpha}{}^{\beta}(\gamma{}^{d}{}^{e}){}_{\gamma}{}_{\delta}\varepsilon{}^{j}{}^{k}\varepsilon{}_{k}{}_{j}T{}_{b}{}_{c}\big(\mathcal D^{a}T{}_{d}{}_{e}\big)\lambda{}^{\delta}{}^{i} -\frac{2i}{9}\rho^{-1}(\gamma{}_{a}){}_{\alpha}{}^{\beta}(\gamma{}^{b}{}^{c}){}_{\beta}{}^{\gamma}(\gamma{}^{d}{}^{e}){}_{\gamma}{}_{\delta}\varepsilon{}^{j}{}^{k}\varepsilon{}_{k}{}_{j}T{}_{b}{}_{c}T{}_{d}{}_{e}\big(\mathcal D^{a}\lambda{}^{\delta}{}^{i}\big)\\
&+\frac{2i}{27}\rho^{-1}(\gamma{}_{a}){}_{\beta}{}^{\gamma}(\gamma{}^{b}{}^{c}){}_{\alpha}{}^{\beta}(\gamma{}^{d}{}^{e}){}_{\gamma}{}_{\delta}\varepsilon{}^{j}{}^{k}\varepsilon{}_{k}{}_{j}T{}_{b}{}_{c}T{}_{d}{}_{e}\big(\mathcal D^{a}\lambda{}^{\delta}{}^{i}\big) +\frac{8i}{3}(\gamma{}_{a}){}_{\alpha}{}^{\beta}(\gamma{}^{b}{}^{c}){}_{\beta}{}^{\gamma}\varepsilon{}^{j}{}^{k}\varepsilon{}_{k}{}_{j}\big(\mathcal D^{a}T{}_{b}{}_{c}\big)\chi{}_{\gamma}{}^{i}\\
&-\frac{8i}{9}(\gamma{}_{a}){}_{\beta}{}^{\gamma}(\gamma{}^{b}{}^{c}){}_{\alpha}{}^{\beta}\varepsilon{}^{j}{}^{k}\varepsilon{}_{k}{}_{j}\big(\mathcal D^{a}T{}_{b}{}_{c}\big)\chi{}_{\gamma}{}^{i} +\frac{8i}{3}(\gamma{}_{a}){}_{\alpha}{}^{\beta}(\gamma{}^{b}{}^{c}){}_{\beta}{}^{\gamma}\varepsilon{}^{j}{}^{k}\varepsilon{}_{k}{}_{j}T{}_{b}{}_{c}\big(\mathcal D^{a}\chi{}_{\gamma}{}^{i}\big)\\
&-\frac{8i}{9}(\gamma{}_{a}){}_{\beta}{}^{\gamma}(\gamma{}^{b}{}^{c}){}_{\alpha}{}^{\beta}\varepsilon{}^{j}{}^{k}\varepsilon{}_{k}{}_{j}T{}_{b}{}_{c}\big(\mathcal D^{a}\chi{}_{\gamma}{}^{i}\big) -\frac{16i}{9}\rho^{-1}Y{}^{i}{}^{j}(\gamma{}_{a}){}_{\alpha}{}^{\beta}\big(\mathcal D^{a}\chi{}_{\beta}{}_{j}\big)\\
&-\frac{16i}{3}\rho^{-1}\big(\mathcal D^{a}Y{}^{i}{}^{j}\big)(\gamma{}_{a}){}_{\alpha}{}^{\beta}\chi{}_{\beta}{}_{j} +\frac{8i}{3}\rho^{-1}Y{}_{j}{}^{i}(\gamma{}_{a}){}_{\alpha}{}^{\beta}\big(\mathcal D^{a}\chi{}_{\beta}{}^{j}\big)\\
&+\frac{8i}{3}\rho^{-1}Y{}_{j}{}^{j}(\gamma{}_{a}){}_{\alpha}{}^{\beta}\big(\mathcal D^{a}\chi{}_{\beta}{}^{i}\big) +\frac{8i}{3}\rho^{-1}\big(\mathcal D^{a}Y{}_{j}{}^{i}\big)(\gamma{}_{a}){}_{\alpha}{}^{\beta}\chi{}_{\beta}{}^{j}\\
&+\frac{8i}{3}\rho^{-1}\big(\mathcal D^{a}Y{}_{j}{}^{j}\big)(\gamma{}_{a}){}_{\alpha}{}^{\beta}\chi{}_{\beta}{}^{i} -\frac{8i}{3}\rho^{-1}Y{}^{i}{}_{j}\delta{}^{k}{}_{l}(\gamma{}_{a}){}_{\alpha}{}^{\beta}\varepsilon{}^{m}{}^{l}\varepsilon{}_{k}{}_{m}\big(\mathcal D^{a}\chi{}_{\beta}{}^{j}\big)\\
&+\frac{8i}{3}\rho^{-1}Y{}^{i}{}_{j}(\gamma{}_{a}){}_{\alpha}{}^{\beta}\big(\mathcal D^{a}\chi{}_{\beta}{}^{j}\big) -\frac{8i}{3}\rho^{-1}\big(\mathcal D^{a}Y{}^{i}{}_{j}\big)\delta{}^{k}{}_{l}(\gamma{}_{a}){}_{\alpha}{}^{\beta}\varepsilon{}^{m}{}^{l}\varepsilon{}_{k}{}_{m}\chi{}_{\beta}{}^{j}\\
&+\frac{8i}{3}\rho^{-1}\big(\mathcal D^{a}Y{}^{i}{}_{j}\big)(\gamma{}_{a}){}_{\alpha}{}^{\beta}\chi{}_{\beta}{}^{j} +\frac{i}{36}\rho^{-1}\big(\mathcal D^{a}R(V){}_{b}{}_{c}{}_{j}{}^{i}\big)(\gamma{}_{a}){}_{\beta}{}^{\gamma}(\gamma{}^{b}{}^{c}){}_{\alpha}{}^{\beta}\lambda{}_{\gamma}{}^{j}\\
&-\frac{i}{18}\rho^{-1}\big(\mathcal D^{a}R(V){}_{b}{}_{c}{}_{j}{}^{i}\big)(\gamma{}_{a}){}_{\alpha}{}^{\beta}(\gamma{}^{b}{}^{c}){}_{\beta}{}^{\gamma}\lambda{}_{\gamma}{}^{j} +\frac{2}{9}\rho^{-1}(\gamma{}^{a}{}^{b}){}_{\alpha}{}^{\beta}\big(\mathcal D^{c}\mathcal D_{c}T{}_{a}{}_{b}\big)\lambda{}_{\beta}{}^{i}\\
&+\frac{2}{9}\rho^{-1}(\gamma{}^{a}{}^{b}){}_{\alpha}{}^{\beta}\big(\mathcal D^{c}\mathcal D_{a}T{}_{b}{}_{c}\big)\lambda{}_{\beta}{}^{i} +\frac{2}{9}\rho^{-1}(\gamma{}^{a}{}^{b}){}_{\alpha}{}^{\beta}\big(\mathcal D^{c}\mathcal D_{b}T{}_{c}{}_{a}\big)\lambda{}_{\beta}{}^{i}\\
&+\frac{2}{9}\rho^{-1}(\gamma{}_{a}{}_{b}){}_{\alpha}{}^{\beta}\big(\mathcal D^{b}\mathcal D_{c}T{}^{c}{}^{a}\big)\lambda{}_{\beta}{}^{i} -\frac{2}{3}\rho^{-1}\big(\mathcal D^{a}\mathcal D^{b}T{}_{b}{}_{a}\big)\lambda{}_{\alpha}{}^{i}\\
&-\frac{2i}{9}\rho^{-1}(\gamma{}_{a}){}_{\alpha}{}^{\beta}\big(\mathcal D^{b}\mathcal D^{c}T{}^{d}{}^{e}\big)\epsilon{}_{c}{}_{b}{}^{a}{}_{d}{}_{e}\lambda{}_{\beta}{}^{i} +\frac{8}{27}\rho^{-1}(\gamma{}_{a}{}_{b}){}_{\alpha}{}^{\beta}T{}_{c}{}_{d}\big(\mathcal D^{b}T{}^{e}{}^{f}\big)\epsilon{}^{a}{}^{c}{}^{d}{}_{e}{}_{f}\lambda{}_{\beta}{}^{i}\\
&+\frac{8}{27}\rho^{-1}(\gamma{}_{a}{}_{b}){}_{\alpha}{}^{\beta}T{}^{c}{}^{d}\big(\mathcal D^{b}T{}_{e}{}_{f}\big)\epsilon{}^{a}{}^{e}{}^{f}{}_{c}{}_{d}\lambda{}_{\beta}{}^{i} -\frac{8}{9}\rho^{-1}T{}^{a}{}^{b}\big(\mathcal D^{c}T{}^{d}{}^{e}\big)\epsilon{}_{c}{}_{a}{}_{b}{}_{d}{}_{e}\lambda{}_{\alpha}{}^{i}\\
&-\frac{8}{9}\rho^{-1}T{}^{a}{}^{b}\big(\mathcal D^{c}T{}^{d}{}^{e}\big)\epsilon{}_{c}{}_{d}{}_{e}{}_{a}{}_{b}\lambda{}_{\alpha}{}^{i} -\frac{128i}{27}\rho^{-1}(\gamma{}_{a}){}_{\alpha}{}^{\beta}T{}^{a}{}^{b}\big(\mathcal D^{c}T{}_{c}{}_{b}\big)\lambda{}_{\beta}{}^{i}
\end{aligned}
\tag{S6-phi-002}
```

```math
\begin{aligned}
&-\frac{128i}{27}\rho^{-1}(\gamma{}_{a}){}_{\alpha}{}^{\beta}T{}_{b}{}_{c}\big(\mathcal D^{b}T{}^{a}{}^{c}\big)\lambda{}_{\beta}{}^{i} +\frac{8i}{9}\rho^{-1}(\gamma{}_{a}){}_{\alpha}{}^{\beta}T{}_{b}{}_{c}\big(\mathcal D^{a}T{}^{b}{}^{c}\big)\lambda{}_{\beta}{}^{i}\\
&+\frac{8i}{9}\rho^{-1}(\gamma{}_{a}){}_{\alpha}{}^{\beta}T{}^{b}{}^{c}\big(\mathcal D^{a}T{}_{b}{}_{c}\big)\lambda{}_{\beta}{}^{i} +\frac{i}{72}\rho^{-1}R(V){}_{a}{}_{b}{}_{j}{}^{i}(\gamma{}_{c}){}_{\beta}{}^{\gamma}(\gamma{}^{a}{}^{b}){}_{\alpha}{}^{\beta}\big(\mathcal D^{c}\lambda{}_{\gamma}{}^{j}\big)\\
&-\frac{i}{36}\rho^{-1}R(V){}_{a}{}_{b}{}_{j}{}^{i}(\gamma{}_{c}){}_{\alpha}{}^{\beta}(\gamma{}^{a}{}^{b}){}_{\beta}{}^{\gamma}\big(\mathcal D^{c}\lambda{}_{\gamma}{}^{j}\big) +\frac{1}{9}\rho^{-1}(\gamma{}^{a}{}^{b}){}_{\alpha}{}^{\beta}\big(\mathcal D_{c}T{}_{a}{}_{b}\big)\big(\mathcal D^{c}\lambda{}_{\beta}{}^{i}\big)\\
&+\frac{1}{9}\rho^{-1}(\gamma{}^{a}{}^{b}){}_{\alpha}{}^{\beta}\big(\mathcal D_{a}T{}_{b}{}_{c}\big)\big(\mathcal D^{c}\lambda{}_{\beta}{}^{i}\big) +\frac{1}{9}\rho^{-1}(\gamma{}^{a}{}^{b}){}_{\alpha}{}^{\beta}\big(\mathcal D_{b}T{}_{c}{}_{a}\big)\big(\mathcal D^{c}\lambda{}_{\beta}{}^{i}\big)\\
&+\frac{1}{9}\rho^{-1}(\gamma{}_{a}{}_{b}){}_{\alpha}{}^{\beta}\big(\mathcal D_{c}T{}^{c}{}^{a}\big)\big(\mathcal D^{b}\lambda{}_{\beta}{}^{i}\big) -\frac{1}{3}\rho^{-1}\big(\mathcal D^{a}T{}_{a}{}_{b}\big)\big(\mathcal D^{b}\lambda{}_{\alpha}{}^{i}\big)\\
&-\frac{i}{9}\rho^{-1}(\gamma{}_{a}){}_{\alpha}{}^{\beta}\big(\mathcal D^{b}T{}^{c}{}^{d}\big)\epsilon{}_{b}{}_{e}{}^{a}{}_{c}{}_{d}\big(\mathcal D^{e}\lambda{}_{\beta}{}^{i}\big) +\frac{4}{27}\rho^{-1}(\gamma{}_{a}{}_{b}){}_{\alpha}{}^{\beta}T{}^{c}{}^{d}T{}_{e}{}_{f}\epsilon{}^{a}{}^{e}{}^{f}{}_{c}{}_{d}\big(\mathcal D^{b}\lambda{}_{\beta}{}^{i}\big)\\
&-\frac{4}{9}\rho^{-1}T{}^{a}{}^{b}T{}^{c}{}^{d}\epsilon{}_{e}{}_{c}{}_{d}{}_{a}{}_{b}\big(\mathcal D^{e}\lambda{}_{\alpha}{}^{i}\big) -\frac{64i}{27}\rho^{-1}(\gamma{}_{a}){}_{\alpha}{}^{\beta}T{}^{a}{}^{b}T{}_{c}{}_{b}\big(\mathcal D^{c}\lambda{}_{\beta}{}^{i}\big)\\
&+\frac{4i}{9}\rho^{-1}(\gamma{}_{a}){}_{\alpha}{}^{\beta}T{}^{b}{}^{c}T{}_{b}{}_{c}\big(\mathcal D^{a}\lambda{}_{\beta}{}^{i}\big) +\frac{i}{36}\rho^{-1}\big(\mathcal D^{a}R(V){}_{b}{}_{c}{}_{j}{}^{j}\big)(\gamma{}_{a}){}_{\beta}{}^{\gamma}(\gamma{}^{b}{}^{c}){}_{\alpha}{}^{\beta}\lambda{}_{\gamma}{}^{i}\\
&-\frac{i}{18}\rho^{-1}\big(\mathcal D^{a}R(V){}_{b}{}_{c}{}_{j}{}^{j}\big)(\gamma{}_{a}){}_{\alpha}{}^{\beta}(\gamma{}^{b}{}^{c}){}_{\beta}{}^{\gamma}\lambda{}_{\gamma}{}^{i} -\frac{2}{9}\rho^{-1}\delta{}^{j}{}_{k}(\gamma{}^{a}{}^{b}){}_{\alpha}{}^{\beta}\varepsilon{}^{l}{}^{k}\varepsilon{}_{j}{}_{l}\big(\mathcal D^{c}\mathcal D_{c}T{}_{a}{}_{b}\big)\lambda{}_{\beta}{}^{i}\\
&-\frac{2}{9}\rho^{-1}\delta{}^{j}{}_{k}(\gamma{}^{a}{}^{b}){}_{\alpha}{}^{\beta}\varepsilon{}^{l}{}^{k}\varepsilon{}_{j}{}_{l}\big(\mathcal D^{c}\mathcal D_{a}T{}_{b}{}_{c}\big)\lambda{}_{\beta}{}^{i} -\frac{2}{9}\rho^{-1}\delta{}^{j}{}_{k}(\gamma{}^{a}{}^{b}){}_{\alpha}{}^{\beta}\varepsilon{}^{l}{}^{k}\varepsilon{}_{j}{}_{l}\big(\mathcal D^{c}\mathcal D_{b}T{}_{c}{}_{a}\big)\lambda{}_{\beta}{}^{i}\\
&-\frac{2}{9}\rho^{-1}\delta{}^{j}{}_{k}(\gamma{}_{a}{}_{b}){}_{\alpha}{}^{\beta}\varepsilon{}^{l}{}^{k}\varepsilon{}_{j}{}_{l}\big(\mathcal D^{b}\mathcal D_{c}T{}^{c}{}^{a}\big)\lambda{}_{\beta}{}^{i} +\frac{2}{3}\rho^{-1}\delta{}^{j}{}_{k}\varepsilon{}^{l}{}^{k}\varepsilon{}_{j}{}_{l}\big(\mathcal D^{a}\mathcal D^{b}T{}_{b}{}_{a}\big)\lambda{}_{\alpha}{}^{i}\\
&+\frac{2i}{9}\rho^{-1}\delta{}^{j}{}_{k}(\gamma{}_{a}){}_{\alpha}{}^{\beta}\varepsilon{}^{l}{}^{k}\varepsilon{}_{j}{}_{l}\big(\mathcal D^{b}\mathcal D^{c}T{}^{d}{}^{e}\big)\epsilon{}_{c}{}_{b}{}^{a}{}_{d}{}_{e}\lambda{}_{\beta}{}^{i} -\frac{8}{27}\rho^{-1}\delta{}^{j}{}_{k}(\gamma{}_{a}{}_{b}){}_{\alpha}{}^{\beta}\varepsilon{}^{l}{}^{k}\varepsilon{}_{j}{}_{l}T{}_{c}{}_{d}\big(\mathcal D^{b}T{}^{e}{}^{f}\big)\epsilon{}^{a}{}^{c}{}^{d}{}_{e}{}_{f}\lambda{}_{\beta}{}^{i}\\
&-\frac{8}{27}\rho^{-1}\delta{}^{j}{}_{k}(\gamma{}_{a}{}_{b}){}_{\alpha}{}^{\beta}\varepsilon{}^{l}{}^{k}\varepsilon{}_{j}{}_{l}T{}^{c}{}^{d}\big(\mathcal D^{b}T{}_{e}{}_{f}\big)\epsilon{}^{a}{}^{e}{}^{f}{}_{c}{}_{d}\lambda{}_{\beta}{}^{i} +\frac{8}{9}\rho^{-1}\delta{}^{j}{}_{k}\varepsilon{}^{l}{}^{k}\varepsilon{}_{j}{}_{l}T{}^{a}{}^{b}\big(\mathcal D^{c}T{}^{d}{}^{e}\big)\epsilon{}_{c}{}_{a}{}_{b}{}_{d}{}_{e}\lambda{}_{\alpha}{}^{i}\\
&+\frac{8}{9}\rho^{-1}\delta{}^{j}{}_{k}\varepsilon{}^{l}{}^{k}\varepsilon{}_{j}{}_{l}T{}^{a}{}^{b}\big(\mathcal D^{c}T{}^{d}{}^{e}\big)\epsilon{}_{c}{}_{d}{}_{e}{}_{a}{}_{b}\lambda{}_{\alpha}{}^{i} +\frac{128i}{27}\rho^{-1}\delta{}^{j}{}_{k}(\gamma{}_{a}){}_{\alpha}{}^{\beta}\varepsilon{}^{l}{}^{k}\varepsilon{}_{j}{}_{l}T{}^{a}{}^{b}\big(\mathcal D^{c}T{}_{c}{}_{b}\big)\lambda{}_{\beta}{}^{i}\\
&+\frac{128i}{27}\rho^{-1}\delta{}^{j}{}_{k}(\gamma{}_{a}){}_{\alpha}{}^{\beta}\varepsilon{}^{l}{}^{k}\varepsilon{}_{j}{}_{l}T{}_{b}{}_{c}\big(\mathcal D^{b}T{}^{a}{}^{c}\big)\lambda{}_{\beta}{}^{i} -\frac{8i}{9}\rho^{-1}\delta{}^{j}{}_{k}(\gamma{}_{a}){}_{\alpha}{}^{\beta}\varepsilon{}^{l}{}^{k}\varepsilon{}_{j}{}_{l}T{}_{b}{}_{c}\big(\mathcal D^{a}T{}^{b}{}^{c}\big)\lambda{}_{\beta}{}^{i}\\
&-\frac{8i}{9}\rho^{-1}\delta{}^{j}{}_{k}(\gamma{}_{a}){}_{\alpha}{}^{\beta}\varepsilon{}^{l}{}^{k}\varepsilon{}_{j}{}_{l}T{}^{b}{}^{c}\big(\mathcal D^{a}T{}_{b}{}_{c}\big)\lambda{}_{\beta}{}^{i} +\frac{i}{36}\rho^{-1}R(V){}_{a}{}_{b}{}_{j}{}^{j}(\gamma{}_{c}){}_{\beta}{}^{\gamma}(\gamma{}^{a}{}^{b}){}_{\alpha}{}^{\beta}\big(\mathcal D^{c}\lambda{}_{\gamma}{}^{i}\big)\\
&-\frac{i}{18}\rho^{-1}R(V){}_{a}{}_{b}{}_{j}{}^{j}(\gamma{}_{c}){}_{\alpha}{}^{\beta}(\gamma{}^{a}{}^{b}){}_{\beta}{}^{\gamma}\big(\mathcal D^{c}\lambda{}_{\gamma}{}^{i}\big) -\frac{2}{9}\rho^{-1}\delta{}^{j}{}_{k}(\gamma{}^{a}{}^{b}){}_{\alpha}{}^{\beta}\varepsilon{}^{l}{}^{k}\varepsilon{}_{j}{}_{l}\big(\mathcal D_{c}T{}_{a}{}_{b}\big)\big(\mathcal D^{c}\lambda{}_{\beta}{}^{i}\big)\\
&-\frac{2}{9}\rho^{-1}\delta{}^{j}{}_{k}(\gamma{}^{a}{}^{b}){}_{\alpha}{}^{\beta}\varepsilon{}^{l}{}^{k}\varepsilon{}_{j}{}_{l}\big(\mathcal D_{a}T{}_{b}{}_{c}\big)\big(\mathcal D^{c}\lambda{}_{\beta}{}^{i}\big) -\frac{2}{9}\rho^{-1}\delta{}^{j}{}_{k}(\gamma{}^{a}{}^{b}){}_{\alpha}{}^{\beta}\varepsilon{}^{l}{}^{k}\varepsilon{}_{j}{}_{l}\big(\mathcal D_{b}T{}_{c}{}_{a}\big)\big(\mathcal D^{c}\lambda{}_{\beta}{}^{i}\big)\\
&-\frac{2}{9}\rho^{-1}\delta{}^{j}{}_{k}(\gamma{}_{a}{}_{b}){}_{\alpha}{}^{\beta}\varepsilon{}^{l}{}^{k}\varepsilon{}_{j}{}_{l}\big(\mathcal D_{c}T{}^{c}{}^{a}\big)\big(\mathcal D^{b}\lambda{}_{\beta}{}^{i}\big) +\frac{2}{3}\rho^{-1}\delta{}^{j}{}_{k}\varepsilon{}^{l}{}^{k}\varepsilon{}_{j}{}_{l}\big(\mathcal D^{a}T{}_{a}{}_{b}\big)\big(\mathcal D^{b}\lambda{}_{\alpha}{}^{i}\big)\\
&+\frac{2i}{9}\rho^{-1}\delta{}^{j}{}_{k}(\gamma{}_{a}){}_{\alpha}{}^{\beta}\varepsilon{}^{l}{}^{k}\varepsilon{}_{j}{}_{l}\big(\mathcal D^{b}T{}^{c}{}^{d}\big)\epsilon{}_{b}{}_{e}{}^{a}{}_{c}{}_{d}\big(\mathcal D^{e}\lambda{}_{\beta}{}^{i}\big) -\frac{8}{27}\rho^{-1}\delta{}^{j}{}_{k}(\gamma{}_{a}{}_{b}){}_{\alpha}{}^{\beta}\varepsilon{}^{l}{}^{k}\varepsilon{}_{j}{}_{l}T{}^{c}{}^{d}T{}_{e}{}_{f}\epsilon{}^{a}{}^{e}{}^{f}{}_{c}{}_{d}\big(\mathcal D^{b}\lambda{}_{\beta}{}^{i}\big)\\
&+\frac{8}{9}\rho^{-1}\delta{}^{j}{}_{k}\varepsilon{}^{l}{}^{k}\varepsilon{}_{j}{}_{l}T{}^{a}{}^{b}T{}^{c}{}^{d}\epsilon{}_{e}{}_{c}{}_{d}{}_{a}{}_{b}\big(\mathcal D^{e}\lambda{}_{\alpha}{}^{i}\big) +\frac{128i}{27}\rho^{-1}\delta{}^{j}{}_{k}(\gamma{}_{a}){}_{\alpha}{}^{\beta}\varepsilon{}^{l}{}^{k}\varepsilon{}_{j}{}_{l}T{}^{a}{}^{b}T{}_{c}{}_{b}\big(\mathcal D^{c}\lambda{}_{\beta}{}^{i}\big)\\
&-\frac{8i}{9}\rho^{-1}\delta{}^{j}{}_{k}(\gamma{}_{a}){}_{\alpha}{}^{\beta}\varepsilon{}^{l}{}^{k}\varepsilon{}_{j}{}_{l}T{}^{b}{}^{c}T{}_{b}{}_{c}\big(\mathcal D^{a}\lambda{}_{\beta}{}^{i}\big) -\frac{1}{3}\rho^{-1}(\gamma{}^{a}){}_{\alpha}{}^{\beta}(\gamma{}^{b}){}_{\gamma}{}^{\delta}(\gamma{}^{c}{}^{d}){}_{\beta}{}^{\gamma}T{}_{c}{}_{d}\big(\mathcal D_{a}\mathcal D_{b}\lambda{}_{\delta}{}^{i}\big)\\
&+\frac{1}{9}\rho^{-1}(\gamma{}^{a}){}_{\beta}{}^{\gamma}(\gamma{}^{b}){}_{\gamma}{}^{\delta}(\gamma{}^{c}{}^{d}){}_{\alpha}{}^{\beta}T{}_{c}{}_{d}\big(\mathcal D_{a}\mathcal D_{b}\lambda{}_{\delta}{}^{i}\big) +\frac{2i}{9}\rho^{-1}(\gamma{}^{a}){}_{\alpha}{}^{\beta}(\gamma{}^{b}{}^{c}){}_{\beta}{}^{\gamma}(\gamma{}^{d}{}^{e}){}_{\gamma}{}_{\delta}T{}_{b}{}_{c}\big(\mathcal D_{a}T{}_{d}{}_{e}\big)\lambda{}^{\delta}{}^{i}\\
&-\frac{2i}{27}\rho^{-1}(\gamma{}^{a}){}_{\beta}{}^{\gamma}(\gamma{}^{b}{}^{c}){}_{\alpha}{}^{\beta}(\gamma{}^{d}{}^{e}){}_{\gamma}{}_{\delta}T{}_{b}{}_{c}\big(\mathcal D_{a}T{}_{d}{}_{e}\big)\lambda{}^{\delta}{}^{i} -\frac{2i}{9}\rho^{-1}(\gamma{}^{a}){}_{\alpha}{}^{\beta}(\gamma{}^{b}{}^{c}){}_{\beta}{}^{\gamma}(\gamma{}^{d}{}^{e}){}_{\gamma}{}_{\delta}T{}_{b}{}_{c}T{}_{d}{}_{e}\big(\mathcal D_{a}\lambda{}^{\delta}{}^{i}\big)\\
&+\frac{2i}{27}\rho^{-1}(\gamma{}^{a}){}_{\beta}{}^{\gamma}(\gamma{}^{b}{}^{c}){}_{\alpha}{}^{\beta}(\gamma{}^{d}{}^{e}){}_{\gamma}{}_{\delta}T{}_{b}{}_{c}T{}_{d}{}_{e}\big(\mathcal D_{a}\lambda{}^{\delta}{}^{i}\big) -\frac{8i}{3}(\gamma{}^{a}){}_{\alpha}{}^{\beta}(\gamma{}^{b}{}^{c}){}_{\beta}{}^{\gamma}T{}_{b}{}_{c}\big(\mathcal D_{a}\chi{}_{\gamma}{}^{i}\big)\\
&+\frac{8i}{9}(\gamma{}^{a}){}_{\beta}{}^{\gamma}(\gamma{}^{b}{}^{c}){}_{\alpha}{}^{\beta}T{}_{b}{}_{c}\big(\mathcal D_{a}\chi{}_{\gamma}{}^{i}\big) -\frac{8i}{3}\rho^{-1}(\gamma{}^{a}){}_{\alpha}{}^{\beta}(\gamma{}^{b}{}^{c}){}_{\beta}{}^{\gamma}\big(\mathcal D_{a}\rho\big)T{}_{b}{}_{c}\chi{}_{\gamma}{}^{i}\\
&+\frac{8i}{9}\rho^{-1}(\gamma{}^{a}){}_{\beta}{}^{\gamma}(\gamma{}^{b}{}^{c}){}_{\alpha}{}^{\beta}\big(\mathcal D_{a}\rho\big)T{}_{b}{}_{c}\chi{}_{\gamma}{}^{i} +\frac{1}{3}\rho^{-1}(\gamma{}^{a}){}_{\alpha}{}^{\beta}(\gamma{}^{b}){}_{\gamma}{}^{\delta}(\gamma{}^{c}{}^{d}){}_{\beta}{}^{\gamma}\varepsilon{}^{j}{}^{k}\varepsilon{}_{k}{}_{j}T{}_{c}{}_{d}\big(\mathcal D_{a}\mathcal D_{b}\lambda{}_{\delta}{}^{i}\big)\\
&-\frac{1}{9}\rho^{-1}(\gamma{}^{a}){}_{\beta}{}^{\gamma}(\gamma{}^{b}){}_{\gamma}{}^{\delta}(\gamma{}^{c}{}^{d}){}_{\alpha}{}^{\beta}\varepsilon{}^{j}{}^{k}\varepsilon{}_{k}{}_{j}T{}_{c}{}_{d}\big(\mathcal D_{a}\mathcal D_{b}\lambda{}_{\delta}{}^{i}\big) -\frac{2i}{9}\rho^{-1}(\gamma{}^{a}){}_{\alpha}{}^{\beta}(\gamma{}^{b}{}^{c}){}_{\beta}{}^{\gamma}(\gamma{}^{d}{}^{e}){}_{\gamma}{}_{\delta}\varepsilon{}^{j}{}^{k}\varepsilon{}_{k}{}_{j}T{}_{b}{}_{c}\big(\mathcal D_{a}T{}_{d}{}_{e}\big)\lambda{}^{\delta}{}^{i}\\
&+\frac{2i}{27}\rho^{-1}(\gamma{}^{a}){}_{\beta}{}^{\gamma}(\gamma{}^{b}{}^{c}){}_{\alpha}{}^{\beta}(\gamma{}^{d}{}^{e}){}_{\gamma}{}_{\delta}\varepsilon{}^{j}{}^{k}\varepsilon{}_{k}{}_{j}T{}_{b}{}_{c}\big(\mathcal D_{a}T{}_{d}{}_{e}\big)\lambda{}^{\delta}{}^{i} +\frac{2i}{9}\rho^{-1}(\gamma{}^{a}){}_{\alpha}{}^{\beta}(\gamma{}^{b}{}^{c}){}_{\beta}{}^{\gamma}(\gamma{}^{d}{}^{e}){}_{\gamma}{}_{\delta}\varepsilon{}^{j}{}^{k}\varepsilon{}_{k}{}_{j}T{}_{b}{}_{c}T{}_{d}{}_{e}\big(\mathcal D_{a}\lambda{}^{\delta}{}^{i}\big)\\
&-\frac{2i}{27}\rho^{-1}(\gamma{}^{a}){}_{\beta}{}^{\gamma}(\gamma{}^{b}{}^{c}){}_{\alpha}{}^{\beta}(\gamma{}^{d}{}^{e}){}_{\gamma}{}_{\delta}\varepsilon{}^{j}{}^{k}\varepsilon{}_{k}{}_{j}T{}_{b}{}_{c}T{}_{d}{}_{e}\big(\mathcal D_{a}\lambda{}^{\delta}{}^{i}\big) +\frac{8i}{3}(\gamma{}^{a}){}_{\alpha}{}^{\beta}(\gamma{}^{b}{}^{c}){}_{\beta}{}^{\gamma}\varepsilon{}^{j}{}^{k}\varepsilon{}_{k}{}_{j}T{}_{b}{}_{c}\big(\mathcal D_{a}\chi{}_{\gamma}{}^{i}\big)\\
&-\frac{8i}{9}(\gamma{}^{a}){}_{\beta}{}^{\gamma}(\gamma{}^{b}{}^{c}){}_{\alpha}{}^{\beta}\varepsilon{}^{j}{}^{k}\varepsilon{}_{k}{}_{j}T{}_{b}{}_{c}\big(\mathcal D_{a}\chi{}_{\gamma}{}^{i}\big) +\frac{8i}{3}\rho^{-1}(\gamma{}^{a}){}_{\alpha}{}^{\beta}(\gamma{}^{b}{}^{c}){}_{\beta}{}^{\gamma}\big(\mathcal D_{a}\rho\big)\varepsilon{}^{j}{}^{k}\varepsilon{}_{k}{}_{j}T{}_{b}{}_{c}\chi{}_{\gamma}{}^{i}\\
&-\frac{8i}{9}\rho^{-1}(\gamma{}^{a}){}_{\beta}{}^{\gamma}(\gamma{}^{b}{}^{c}){}_{\alpha}{}^{\beta}\big(\mathcal D_{a}\rho\big)\varepsilon{}^{j}{}^{k}\varepsilon{}_{k}{}_{j}T{}_{b}{}_{c}\chi{}_{\gamma}{}^{i} -\frac{i}{3}\rho^{-1}(\gamma{}^{a}){}_{\alpha}{}^{\beta}(\gamma{}^{b}){}_{\gamma}{}^{\delta}(\gamma{}_{a}){}_{\rho}{}^{\sigma}(\gamma{}^{c}{}^{d}){}_{\beta}{}^{\rho}(\gamma{}^{e}{}^{f}){}_{\sigma}{}^{\gamma}T{}_{c}{}_{d}T{}_{e}{}_{f}\big(\mathcal D_{b}\lambda{}_{\delta}{}^{i}\big)\\
&+\frac{i}{9}\rho^{-1}(\gamma{}^{a}){}_{\alpha}{}^{\beta}(\gamma{}^{b}){}_{\gamma}{}^{\delta}(\gamma{}_{a}){}_{\rho}{}^{\gamma}(\gamma{}^{c}{}^{d}){}_{\beta}{}^{\sigma}(\gamma{}^{e}{}^{f}){}_{\sigma}{}^{\rho}T{}_{c}{}_{d}T{}_{e}{}_{f}\big(\mathcal D_{b}\lambda{}_{\delta}{}^{i}\big) +\frac{i}{9}\rho^{-1}(\gamma{}^{a}){}_{\beta}{}^{\gamma}(\gamma{}^{b}){}_{\delta}{}^{\rho}(\gamma{}_{a}){}_{\gamma}{}^{\sigma}(\gamma{}^{c}{}^{d}){}_{\alpha}{}^{\beta}(\gamma{}^{e}{}^{f}){}_{\sigma}{}^{\delta}T{}_{c}{}_{d}T{}_{e}{}_{f}\big(\mathcal D_{b}\lambda{}_{\rho}{}^{i}\big)\\
&-\frac{i}{27}\rho^{-1}(\gamma{}^{a}){}_{\beta}{}^{\gamma}(\gamma{}^{b}){}_{\delta}{}^{\rho}(\gamma{}_{a}){}_{\sigma}{}^{\delta}(\gamma{}^{c}{}^{d}){}_{\alpha}{}^{\beta}(\gamma{}^{e}{}^{f}){}_{\gamma}{}^{\sigma}T{}_{c}{}_{d}T{}_{e}{}_{f}\big(\mathcal D_{b}\lambda{}_{\rho}{}^{i}\big) -\frac{2}{9}\rho^{-1}(\gamma{}^{a}){}_{\alpha}{}^{\beta}(\gamma{}_{a}){}_{\gamma}{}^{\delta}(\gamma{}^{b}{}^{c}){}_{\beta}{}^{\gamma}(\gamma{}^{d}{}^{e}){}_{\delta}{}^{\rho}(\gamma{}^{f}{}^{g}){}_{\rho}{}_{\sigma}T{}_{b}{}_{c}T{}_{d}{}_{e}T{}_{f}{}_{g}\lambda{}^{\sigma}{}^{i}\\
&+\frac{2}{27}\rho^{-1}(\gamma{}^{a}){}_{\alpha}{}^{\beta}(\gamma{}_{a}){}_{\gamma}{}^{\delta}(\gamma{}^{b}{}^{c}){}_{\beta}{}^{\rho}(\gamma{}^{d}{}^{e}){}_{\rho}{}^{\gamma}(\gamma{}^{f}{}^{g}){}_{\delta}{}_{\sigma}T{}_{b}{}_{c}T{}_{d}{}_{e}T{}_{f}{}_{g}\lambda{}^{\sigma}{}^{i} +\frac{2}{27}\rho^{-1}(\gamma{}^{a}){}_{\beta}{}^{\gamma}(\gamma{}_{a}){}_{\gamma}{}^{\delta}(\gamma{}^{b}{}^{c}){}_{\alpha}{}^{\beta}(\gamma{}^{d}{}^{e}){}_{\delta}{}^{\rho}(\gamma{}^{f}{}^{g}){}_{\rho}{}_{\sigma}T{}_{b}{}_{c}T{}_{d}{}_{e}T{}_{f}{}_{g}\lambda{}^{\sigma}{}^{i}\\
&-\frac{2}{81}\rho^{-1}(\gamma{}^{a}){}_{\beta}{}^{\gamma}(\gamma{}_{a}){}_{\delta}{}^{\rho}(\gamma{}^{b}{}^{c}){}_{\alpha}{}^{\beta}(\gamma{}^{d}{}^{e}){}_{\gamma}{}^{\delta}(\gamma{}^{f}{}^{g}){}_{\rho}{}_{\sigma}T{}_{b}{}_{c}T{}_{d}{}_{e}T{}_{f}{}_{g}\lambda{}^{\sigma}{}^{i} +\frac{8}{3}(\gamma{}^{a}){}_{\alpha}{}^{\beta}(\gamma{}_{a}){}_{\gamma}{}^{\delta}(\gamma{}^{b}{}^{c}){}_{\beta}{}^{\gamma}(\gamma{}^{d}{}^{e}){}_{\delta}{}^{\rho}T{}_{b}{}_{c}T{}_{d}{}_{e}\chi{}_{\rho}{}^{i}\\
&-\frac{8}{9}(\gamma{}^{a}){}_{\alpha}{}^{\beta}(\gamma{}_{a}){}_{\gamma}{}^{\delta}(\gamma{}^{b}{}^{c}){}_{\beta}{}^{\rho}(\gamma{}^{d}{}^{e}){}_{\rho}{}^{\gamma}T{}_{b}{}_{c}T{}_{d}{}_{e}\chi{}_{\delta}{}^{i} -\frac{8}{9}(\gamma{}^{a}){}_{\beta}{}^{\gamma}(\gamma{}_{a}){}_{\gamma}{}^{\delta}(\gamma{}^{b}{}^{c}){}_{\alpha}{}^{\beta}(\gamma{}^{d}{}^{e}){}_{\delta}{}^{\rho}T{}_{b}{}_{c}T{}_{d}{}_{e}\chi{}_{\rho}{}^{i}\\
&+\frac{8}{27}(\gamma{}^{a}){}_{\beta}{}^{\gamma}(\gamma{}_{a}){}_{\delta}{}^{\rho}(\gamma{}^{b}{}^{c}){}_{\alpha}{}^{\beta}(\gamma{}^{d}{}^{e}){}_{\gamma}{}^{\delta}T{}_{b}{}_{c}T{}_{d}{}_{e}\chi{}_{\rho}{}^{i} +\frac{i}{3}\rho^{-1}(\gamma{}^{a}){}_{\alpha}{}^{\beta}(\gamma{}^{b}){}_{\gamma}{}^{\delta}(\gamma{}_{a}){}_{\rho}{}^{\sigma}(\gamma{}^{c}{}^{d}){}_{\beta}{}^{\rho}(\gamma{}^{e}{}^{f}){}_{\sigma}{}^{\gamma}\varepsilon{}^{j}{}^{k}\varepsilon{}_{k}{}_{j}T{}_{c}{}_{d}T{}_{e}{}_{f}\big(\mathcal D_{b}\lambda{}_{\delta}{}^{i}\big)\\
&-\frac{i}{9}\rho^{-1}(\gamma{}^{a}){}_{\alpha}{}^{\beta}(\gamma{}^{b}){}_{\gamma}{}^{\delta}(\gamma{}_{a}){}_{\rho}{}^{\gamma}(\gamma{}^{c}{}^{d}){}_{\beta}{}^{\sigma}(\gamma{}^{e}{}^{f}){}_{\sigma}{}^{\rho}\varepsilon{}^{j}{}^{k}\varepsilon{}_{k}{}_{j}T{}_{c}{}_{d}T{}_{e}{}_{f}\big(\mathcal D_{b}\lambda{}_{\delta}{}^{i}\big) -\frac{i}{9}\rho^{-1}(\gamma{}^{a}){}_{\beta}{}^{\gamma}(\gamma{}^{b}){}_{\delta}{}^{\rho}(\gamma{}_{a}){}_{\gamma}{}^{\sigma}(\gamma{}^{c}{}^{d}){}_{\alpha}{}^{\beta}(\gamma{}^{e}{}^{f}){}_{\sigma}{}^{\delta}\varepsilon{}^{j}{}^{k}\varepsilon{}_{k}{}_{j}T{}_{c}{}_{d}T{}_{e}{}_{f}\big(\mathcal D_{b}\lambda{}_{\rho}{}^{i}\big)\\
&+\frac{i}{27}\rho^{-1}(\gamma{}^{a}){}_{\beta}{}^{\gamma}(\gamma{}^{b}){}_{\delta}{}^{\rho}(\gamma{}_{a}){}_{\sigma}{}^{\delta}(\gamma{}^{c}{}^{d}){}_{\alpha}{}^{\beta}(\gamma{}^{e}{}^{f}){}_{\gamma}{}^{\sigma}\varepsilon{}^{j}{}^{k}\varepsilon{}_{k}{}_{j}T{}_{c}{}_{d}T{}_{e}{}_{f}\big(\mathcal D_{b}\lambda{}_{\rho}{}^{i}\big) +\frac{2}{9}\rho^{-1}(\gamma{}^{a}){}_{\alpha}{}^{\beta}(\gamma{}_{a}){}_{\gamma}{}^{\delta}(\gamma{}^{b}{}^{c}){}_{\beta}{}^{\gamma}(\gamma{}^{d}{}^{e}){}_{\delta}{}^{\rho}(\gamma{}^{f}{}^{g}){}_{\rho}{}_{\sigma}\varepsilon{}^{j}{}^{k}\varepsilon{}_{k}{}_{j}T{}_{b}{}_{c}T{}_{d}{}_{e}T{}_{f}{}_{g}\lambda{}^{\sigma}{}^{i}
\end{aligned}
\tag{S6-phi-003}
```

```math
\begin{aligned}
&-\frac{2}{27}\rho^{-1}(\gamma{}^{a}){}_{\alpha}{}^{\beta}(\gamma{}_{a}){}_{\gamma}{}^{\delta}(\gamma{}^{b}{}^{c}){}_{\beta}{}^{\rho}(\gamma{}^{d}{}^{e}){}_{\rho}{}^{\gamma}(\gamma{}^{f}{}^{g}){}_{\delta}{}_{\sigma}\varepsilon{}^{j}{}^{k}\varepsilon{}_{k}{}_{j}T{}_{b}{}_{c}T{}_{d}{}_{e}T{}_{f}{}_{g}\lambda{}^{\sigma}{}^{i} -\frac{2}{27}\rho^{-1}(\gamma{}^{a}){}_{\beta}{}^{\gamma}(\gamma{}_{a}){}_{\gamma}{}^{\delta}(\gamma{}^{b}{}^{c}){}_{\alpha}{}^{\beta}(\gamma{}^{d}{}^{e}){}_{\delta}{}^{\rho}(\gamma{}^{f}{}^{g}){}_{\rho}{}_{\sigma}\varepsilon{}^{j}{}^{k}\varepsilon{}_{k}{}_{j}T{}_{b}{}_{c}T{}_{d}{}_{e}T{}_{f}{}_{g}\lambda{}^{\sigma}{}^{i}\\
&+\frac{2}{81}\rho^{-1}(\gamma{}^{a}){}_{\beta}{}^{\gamma}(\gamma{}_{a}){}_{\delta}{}^{\rho}(\gamma{}^{b}{}^{c}){}_{\alpha}{}^{\beta}(\gamma{}^{d}{}^{e}){}_{\gamma}{}^{\delta}(\gamma{}^{f}{}^{g}){}_{\rho}{}_{\sigma}\varepsilon{}^{j}{}^{k}\varepsilon{}_{k}{}_{j}T{}_{b}{}_{c}T{}_{d}{}_{e}T{}_{f}{}_{g}\lambda{}^{\sigma}{}^{i} -\frac{8}{3}(\gamma{}^{a}){}_{\alpha}{}^{\beta}(\gamma{}_{a}){}_{\gamma}{}^{\delta}(\gamma{}^{b}{}^{c}){}_{\beta}{}^{\gamma}(\gamma{}^{d}{}^{e}){}_{\delta}{}^{\rho}\varepsilon{}^{j}{}^{k}\varepsilon{}_{k}{}_{j}T{}_{b}{}_{c}T{}_{d}{}_{e}\chi{}_{\rho}{}^{i}\\
&+\frac{8}{9}(\gamma{}^{a}){}_{\alpha}{}^{\beta}(\gamma{}_{a}){}_{\gamma}{}^{\delta}(\gamma{}^{b}{}^{c}){}_{\beta}{}^{\rho}(\gamma{}^{d}{}^{e}){}_{\rho}{}^{\gamma}\varepsilon{}^{j}{}^{k}\varepsilon{}_{k}{}_{j}T{}_{b}{}_{c}T{}_{d}{}_{e}\chi{}_{\delta}{}^{i} +\frac{8}{9}(\gamma{}^{a}){}_{\beta}{}^{\gamma}(\gamma{}_{a}){}_{\gamma}{}^{\delta}(\gamma{}^{b}{}^{c}){}_{\alpha}{}^{\beta}(\gamma{}^{d}{}^{e}){}_{\delta}{}^{\rho}\varepsilon{}^{j}{}^{k}\varepsilon{}_{k}{}_{j}T{}_{b}{}_{c}T{}_{d}{}_{e}\chi{}_{\rho}{}^{i}\\
&-\frac{8}{27}(\gamma{}^{a}){}_{\beta}{}^{\gamma}(\gamma{}_{a}){}_{\delta}{}^{\rho}(\gamma{}^{b}{}^{c}){}_{\alpha}{}^{\beta}(\gamma{}^{d}{}^{e}){}_{\gamma}{}^{\delta}\varepsilon{}^{j}{}^{k}\varepsilon{}_{k}{}_{j}T{}_{b}{}_{c}T{}_{d}{}_{e}\chi{}_{\rho}{}^{i} +\frac{16}{9}\rho^{-1}Y{}^{i}{}^{j}(\gamma{}^{a}){}_{\alpha}{}^{\beta}(\gamma{}_{a}){}_{\gamma}{}^{\delta}(\gamma{}^{b}{}^{c}){}_{\beta}{}^{\gamma}T{}_{b}{}_{c}\chi{}_{\delta}{}_{j}\\
&-\frac{16}{27}\rho^{-1}Y{}^{i}{}^{j}(\gamma{}^{a}){}_{\beta}{}^{\gamma}(\gamma{}_{a}){}_{\gamma}{}^{\delta}(\gamma{}^{b}{}^{c}){}_{\alpha}{}^{\beta}T{}_{b}{}_{c}\chi{}_{\delta}{}_{j} -\frac{8}{3}\rho^{-1}Y{}_{j}{}^{i}(\gamma{}^{a}){}_{\alpha}{}^{\beta}(\gamma{}_{a}){}_{\gamma}{}^{\delta}(\gamma{}^{b}{}^{c}){}_{\beta}{}^{\gamma}T{}_{b}{}_{c}\chi{}_{\delta}{}^{j}\\
&-\frac{8}{3}\rho^{-1}Y{}_{j}{}^{j}(\gamma{}^{a}){}_{\alpha}{}^{\beta}(\gamma{}_{a}){}_{\gamma}{}^{\delta}(\gamma{}^{b}{}^{c}){}_{\beta}{}^{\gamma}T{}_{b}{}_{c}\chi{}_{\delta}{}^{i} +\frac{8}{9}\rho^{-1}Y{}_{j}{}^{i}(\gamma{}^{a}){}_{\beta}{}^{\gamma}(\gamma{}_{a}){}_{\gamma}{}^{\delta}(\gamma{}^{b}{}^{c}){}_{\alpha}{}^{\beta}T{}_{b}{}_{c}\chi{}_{\delta}{}^{j}\\
&+\frac{8}{9}\rho^{-1}Y{}_{j}{}^{j}(\gamma{}^{a}){}_{\beta}{}^{\gamma}(\gamma{}_{a}){}_{\gamma}{}^{\delta}(\gamma{}^{b}{}^{c}){}_{\alpha}{}^{\beta}T{}_{b}{}_{c}\chi{}_{\delta}{}^{i} +\frac{8}{3}\rho^{-1}Y{}^{i}{}_{j}\delta{}^{k}{}_{l}(\gamma{}^{a}){}_{\alpha}{}^{\beta}(\gamma{}_{a}){}_{\gamma}{}^{\delta}(\gamma{}^{b}{}^{c}){}_{\beta}{}^{\gamma}\varepsilon{}^{m}{}^{l}\varepsilon{}_{k}{}_{m}T{}_{b}{}_{c}\chi{}_{\delta}{}^{j}\\
&-\frac{8}{3}\rho^{-1}Y{}^{i}{}_{j}(\gamma{}^{a}){}_{\alpha}{}^{\beta}(\gamma{}_{a}){}_{\gamma}{}^{\delta}(\gamma{}^{b}{}^{c}){}_{\beta}{}^{\gamma}T{}_{b}{}_{c}\chi{}_{\delta}{}^{j} -\frac{8}{9}\rho^{-1}Y{}^{i}{}_{j}\delta{}^{k}{}_{l}(\gamma{}^{a}){}_{\beta}{}^{\gamma}(\gamma{}_{a}){}_{\gamma}{}^{\delta}(\gamma{}^{b}{}^{c}){}_{\alpha}{}^{\beta}\varepsilon{}^{m}{}^{l}\varepsilon{}_{k}{}_{m}T{}_{b}{}_{c}\chi{}_{\delta}{}^{j}\\
&+\frac{8}{9}\rho^{-1}Y{}^{i}{}_{j}(\gamma{}^{a}){}_{\beta}{}^{\gamma}(\gamma{}_{a}){}_{\gamma}{}^{\delta}(\gamma{}^{b}{}^{c}){}_{\alpha}{}^{\beta}T{}_{b}{}_{c}\chi{}_{\delta}{}^{j} -\frac{1}{36}\rho^{-1}R(V){}_{a}{}_{b}{}_{j}{}^{i}(\gamma{}^{c}){}_{\alpha}{}^{\beta}(\gamma{}_{c}){}_{\gamma}{}^{\delta}(\gamma{}^{d}{}^{e}){}_{\beta}{}^{\rho}(\gamma{}^{a}{}^{b}){}_{\rho}{}^{\gamma}T{}_{d}{}_{e}\lambda{}_{\delta}{}^{j}\\
&+\frac{1}{18}\rho^{-1}R(V){}_{a}{}_{b}{}_{j}{}^{i}(\gamma{}^{c}){}_{\alpha}{}^{\beta}(\gamma{}_{c}){}_{\gamma}{}^{\delta}(\gamma{}^{d}{}^{e}){}_{\beta}{}^{\gamma}(\gamma{}^{a}{}^{b}){}_{\delta}{}^{\rho}T{}_{d}{}_{e}\lambda{}_{\rho}{}^{j} +\frac{2i}{9}\rho^{-1}(\gamma{}^{a}){}_{\alpha}{}^{\beta}(\gamma{}^{b}{}^{c}){}_{\beta}{}^{\gamma}(\gamma{}^{d}{}^{e}){}_{\gamma}{}^{\delta}T{}_{b}{}_{c}\big(\mathcal D_{a}T{}_{d}{}_{e}\big)\lambda{}_{\delta}{}^{i}\\
&+\frac{2i}{9}\rho^{-1}(\gamma{}^{a}){}_{\alpha}{}^{\beta}(\gamma{}^{b}{}^{c}){}_{\beta}{}^{\gamma}(\gamma{}^{d}{}^{e}){}_{\gamma}{}^{\delta}T{}_{b}{}_{c}\big(\mathcal D_{d}T{}_{e}{}_{a}\big)\lambda{}_{\delta}{}^{i} +\frac{2i}{9}\rho^{-1}(\gamma{}^{a}){}_{\alpha}{}^{\beta}(\gamma{}^{b}{}^{c}){}_{\beta}{}^{\gamma}(\gamma{}^{d}{}^{e}){}_{\gamma}{}^{\delta}T{}_{b}{}_{c}\big(\mathcal D_{e}T{}_{a}{}_{d}\big)\lambda{}_{\delta}{}^{i}\\
&+\frac{2i}{9}\rho^{-1}(\gamma{}^{a}){}_{\alpha}{}^{\beta}(\gamma{}^{b}{}^{c}){}_{\beta}{}^{\gamma}(\gamma{}_{d}{}_{a}){}_{\gamma}{}^{\delta}T{}_{b}{}_{c}\big(\mathcal D_{e}T{}^{e}{}^{d}\big)\lambda{}_{\delta}{}^{i} -\frac{2i}{3}\rho^{-1}(\gamma{}^{a}){}_{\alpha}{}^{\beta}(\gamma{}^{b}{}^{c}){}_{\beta}{}^{\gamma}T{}_{b}{}_{c}\big(\mathcal D^{d}T{}_{d}{}_{a}\big)\lambda{}_{\gamma}{}^{i}\\
&+\frac{2}{9}\rho^{-1}(\gamma{}^{a}){}_{\alpha}{}^{\beta}(\gamma{}_{b}){}_{\gamma}{}^{\delta}(\gamma{}^{c}{}^{d}){}_{\beta}{}^{\gamma}T{}_{c}{}_{d}\big(\mathcal D^{e}T{}^{f}{}^{g}\big)\epsilon{}_{e}{}_{a}{}^{b}{}_{f}{}_{g}\lambda{}_{\delta}{}^{i} +\frac{8i}{27}\rho^{-1}(\gamma{}^{a}){}_{\alpha}{}^{\beta}(\gamma{}^{b}{}^{c}){}_{\beta}{}^{\gamma}(\gamma{}_{d}{}_{a}){}_{\gamma}{}^{\delta}T{}^{e}{}^{f}T{}_{b}{}_{c}T{}_{g}{}_{h}\epsilon{}^{d}{}^{g}{}^{h}{}_{e}{}_{f}\lambda{}_{\delta}{}^{i}\\
&-\frac{8i}{9}\rho^{-1}(\gamma{}^{a}){}_{\alpha}{}^{\beta}(\gamma{}^{b}{}^{c}){}_{\beta}{}^{\gamma}T{}^{d}{}^{e}T{}^{f}{}^{g}T{}_{b}{}_{c}\epsilon{}_{a}{}_{f}{}_{g}{}_{d}{}_{e}\lambda{}_{\gamma}{}^{i} +\frac{128}{27}\rho^{-1}(\gamma{}^{a}){}_{\alpha}{}^{\beta}(\gamma{}_{b}){}_{\gamma}{}^{\delta}(\gamma{}^{c}{}^{d}){}_{\beta}{}^{\gamma}T{}^{b}{}^{e}T{}_{c}{}_{d}T{}_{a}{}_{e}\lambda{}_{\delta}{}^{i}\\
&-\frac{8}{9}\rho^{-1}(\gamma{}^{a}){}_{\alpha}{}^{\beta}(\gamma{}_{a}){}_{\gamma}{}^{\delta}(\gamma{}^{b}{}^{c}){}_{\beta}{}^{\gamma}T{}^{d}{}^{e}T{}_{b}{}_{c}T{}_{d}{}_{e}\lambda{}_{\delta}{}^{i} +\frac{1}{108}\rho^{-1}R(V){}_{a}{}_{b}{}_{j}{}^{i}(\gamma{}^{c}){}_{\beta}{}^{\gamma}(\gamma{}_{c}){}_{\delta}{}^{\rho}(\gamma{}^{d}{}^{e}){}_{\alpha}{}^{\beta}(\gamma{}^{a}{}^{b}){}_{\gamma}{}^{\delta}T{}_{d}{}_{e}\lambda{}_{\rho}{}^{j}\\
&-\frac{1}{54}\rho^{-1}R(V){}_{a}{}_{b}{}_{j}{}^{i}(\gamma{}^{c}){}_{\beta}{}^{\gamma}(\gamma{}_{c}){}_{\gamma}{}^{\delta}(\gamma{}^{d}{}^{e}){}_{\alpha}{}^{\beta}(\gamma{}^{a}{}^{b}){}_{\delta}{}^{\rho}T{}_{d}{}_{e}\lambda{}_{\rho}{}^{j} -\frac{2i}{27}\rho^{-1}(\gamma{}^{a}){}_{\beta}{}^{\gamma}(\gamma{}^{b}{}^{c}){}_{\alpha}{}^{\beta}(\gamma{}^{d}{}^{e}){}_{\gamma}{}^{\delta}T{}_{b}{}_{c}\big(\mathcal D_{a}T{}_{d}{}_{e}\big)\lambda{}_{\delta}{}^{i}\\
&-\frac{2i}{27}\rho^{-1}(\gamma{}^{a}){}_{\beta}{}^{\gamma}(\gamma{}^{b}{}^{c}){}_{\alpha}{}^{\beta}(\gamma{}^{d}{}^{e}){}_{\gamma}{}^{\delta}T{}_{b}{}_{c}\big(\mathcal D_{d}T{}_{e}{}_{a}\big)\lambda{}_{\delta}{}^{i} -\frac{2i}{27}\rho^{-1}(\gamma{}^{a}){}_{\beta}{}^{\gamma}(\gamma{}^{b}{}^{c}){}_{\alpha}{}^{\beta}(\gamma{}^{d}{}^{e}){}_{\gamma}{}^{\delta}T{}_{b}{}_{c}\big(\mathcal D_{e}T{}_{a}{}_{d}\big)\lambda{}_{\delta}{}^{i}\\
&-\frac{2i}{27}\rho^{-1}(\gamma{}^{a}){}_{\beta}{}^{\gamma}(\gamma{}^{b}{}^{c}){}_{\alpha}{}^{\beta}(\gamma{}_{d}{}_{a}){}_{\gamma}{}^{\delta}T{}_{b}{}_{c}\big(\mathcal D_{e}T{}^{e}{}^{d}\big)\lambda{}_{\delta}{}^{i} +\frac{2i}{9}\rho^{-1}(\gamma{}^{a}){}_{\beta}{}^{\gamma}(\gamma{}^{b}{}^{c}){}_{\alpha}{}^{\beta}T{}_{b}{}_{c}\big(\mathcal D^{d}T{}_{d}{}_{a}\big)\lambda{}_{\gamma}{}^{i}\\
&-\frac{2}{27}\rho^{-1}(\gamma{}^{a}){}_{\beta}{}^{\gamma}(\gamma{}_{b}){}_{\gamma}{}^{\delta}(\gamma{}^{c}{}^{d}){}_{\alpha}{}^{\beta}T{}_{c}{}_{d}\big(\mathcal D^{e}T{}^{f}{}^{g}\big)\epsilon{}_{e}{}_{a}{}^{b}{}_{f}{}_{g}\lambda{}_{\delta}{}^{i} -\frac{8i}{81}\rho^{-1}(\gamma{}^{a}){}_{\beta}{}^{\gamma}(\gamma{}^{b}{}^{c}){}_{\alpha}{}^{\beta}(\gamma{}_{d}{}_{a}){}_{\gamma}{}^{\delta}T{}^{e}{}^{f}T{}_{b}{}_{c}T{}_{g}{}_{h}\epsilon{}^{d}{}^{g}{}^{h}{}_{e}{}_{f}\lambda{}_{\delta}{}^{i}\\
&+\frac{8i}{27}\rho^{-1}(\gamma{}^{a}){}_{\beta}{}^{\gamma}(\gamma{}^{b}{}^{c}){}_{\alpha}{}^{\beta}T{}^{d}{}^{e}T{}^{f}{}^{g}T{}_{b}{}_{c}\epsilon{}_{a}{}_{f}{}_{g}{}_{d}{}_{e}\lambda{}_{\gamma}{}^{i} -\frac{128}{81}\rho^{-1}(\gamma{}^{a}){}_{\beta}{}^{\gamma}(\gamma{}_{b}){}_{\gamma}{}^{\delta}(\gamma{}^{c}{}^{d}){}_{\alpha}{}^{\beta}T{}^{b}{}^{e}T{}_{c}{}_{d}T{}_{a}{}_{e}\lambda{}_{\delta}{}^{i}\\
&+\frac{8}{27}\rho^{-1}(\gamma{}^{a}){}_{\beta}{}^{\gamma}(\gamma{}_{a}){}_{\gamma}{}^{\delta}(\gamma{}^{b}{}^{c}){}_{\alpha}{}^{\beta}T{}^{d}{}^{e}T{}_{b}{}_{c}T{}_{d}{}_{e}\lambda{}_{\delta}{}^{i} -\frac{1}{36}\rho^{-1}R(V){}_{a}{}_{b}{}_{j}{}^{j}(\gamma{}^{c}){}_{\alpha}{}^{\beta}(\gamma{}_{c}){}_{\gamma}{}^{\delta}(\gamma{}^{d}{}^{e}){}_{\beta}{}^{\rho}(\gamma{}^{a}{}^{b}){}_{\rho}{}^{\gamma}T{}_{d}{}_{e}\lambda{}_{\delta}{}^{i}\\
&+\frac{1}{18}\rho^{-1}R(V){}_{a}{}_{b}{}_{j}{}^{j}(\gamma{}^{c}){}_{\alpha}{}^{\beta}(\gamma{}_{c}){}_{\gamma}{}^{\delta}(\gamma{}^{d}{}^{e}){}_{\beta}{}^{\gamma}(\gamma{}^{a}{}^{b}){}_{\delta}{}^{\rho}T{}_{d}{}_{e}\lambda{}_{\rho}{}^{i} -\frac{2i}{9}\rho^{-1}\delta{}^{j}{}_{k}(\gamma{}^{a}){}_{\alpha}{}^{\beta}(\gamma{}^{b}{}^{c}){}_{\beta}{}^{\gamma}(\gamma{}^{d}{}^{e}){}_{\gamma}{}^{\delta}\varepsilon{}^{l}{}^{k}\varepsilon{}_{j}{}_{l}T{}_{b}{}_{c}\big(\mathcal D_{a}T{}_{d}{}_{e}\big)\lambda{}_{\delta}{}^{i}\\
&-\frac{2i}{9}\rho^{-1}\delta{}^{j}{}_{k}(\gamma{}^{a}){}_{\alpha}{}^{\beta}(\gamma{}^{b}{}^{c}){}_{\beta}{}^{\gamma}(\gamma{}^{d}{}^{e}){}_{\gamma}{}^{\delta}\varepsilon{}^{l}{}^{k}\varepsilon{}_{j}{}_{l}T{}_{b}{}_{c}\big(\mathcal D_{d}T{}_{e}{}_{a}\big)\lambda{}_{\delta}{}^{i} -\frac{2i}{9}\rho^{-1}\delta{}^{j}{}_{k}(\gamma{}^{a}){}_{\alpha}{}^{\beta}(\gamma{}^{b}{}^{c}){}_{\beta}{}^{\gamma}(\gamma{}^{d}{}^{e}){}_{\gamma}{}^{\delta}\varepsilon{}^{l}{}^{k}\varepsilon{}_{j}{}_{l}T{}_{b}{}_{c}\big(\mathcal D_{e}T{}_{a}{}_{d}\big)\lambda{}_{\delta}{}^{i}\\
&-\frac{2i}{9}\rho^{-1}\delta{}^{j}{}_{k}(\gamma{}^{a}){}_{\alpha}{}^{\beta}(\gamma{}^{b}{}^{c}){}_{\beta}{}^{\gamma}(\gamma{}_{d}{}_{a}){}_{\gamma}{}^{\delta}\varepsilon{}^{l}{}^{k}\varepsilon{}_{j}{}_{l}T{}_{b}{}_{c}\big(\mathcal D_{e}T{}^{e}{}^{d}\big)\lambda{}_{\delta}{}^{i} +\frac{2i}{3}\rho^{-1}\delta{}^{j}{}_{k}(\gamma{}^{a}){}_{\alpha}{}^{\beta}(\gamma{}^{b}{}^{c}){}_{\beta}{}^{\gamma}\varepsilon{}^{l}{}^{k}\varepsilon{}_{j}{}_{l}T{}_{b}{}_{c}\big(\mathcal D^{d}T{}_{d}{}_{a}\big)\lambda{}_{\gamma}{}^{i}\\
&-\frac{2}{9}\rho^{-1}\delta{}^{j}{}_{k}(\gamma{}^{a}){}_{\alpha}{}^{\beta}(\gamma{}_{b}){}_{\gamma}{}^{\delta}(\gamma{}^{c}{}^{d}){}_{\beta}{}^{\gamma}\varepsilon{}^{l}{}^{k}\varepsilon{}_{j}{}_{l}T{}_{c}{}_{d}\big(\mathcal D^{e}T{}^{f}{}^{g}\big)\epsilon{}_{e}{}_{a}{}^{b}{}_{f}{}_{g}\lambda{}_{\delta}{}^{i} -\frac{8i}{27}\rho^{-1}\delta{}^{j}{}_{k}(\gamma{}^{a}){}_{\alpha}{}^{\beta}(\gamma{}^{b}{}^{c}){}_{\beta}{}^{\gamma}(\gamma{}_{d}{}_{a}){}_{\gamma}{}^{\delta}\varepsilon{}^{l}{}^{k}\varepsilon{}_{j}{}_{l}T{}^{e}{}^{f}T{}_{b}{}_{c}T{}_{g}{}_{h}\epsilon{}^{d}{}^{g}{}^{h}{}_{e}{}_{f}\lambda{}_{\delta}{}^{i}\\
&+\frac{8i}{9}\rho^{-1}\delta{}^{j}{}_{k}(\gamma{}^{a}){}_{\alpha}{}^{\beta}(\gamma{}^{b}{}^{c}){}_{\beta}{}^{\gamma}\varepsilon{}^{l}{}^{k}\varepsilon{}_{j}{}_{l}T{}^{d}{}^{e}T{}^{f}{}^{g}T{}_{b}{}_{c}\epsilon{}_{a}{}_{f}{}_{g}{}_{d}{}_{e}\lambda{}_{\gamma}{}^{i} -\frac{128}{27}\rho^{-1}\delta{}^{j}{}_{k}(\gamma{}^{a}){}_{\alpha}{}^{\beta}(\gamma{}_{b}){}_{\gamma}{}^{\delta}(\gamma{}^{c}{}^{d}){}_{\beta}{}^{\gamma}\varepsilon{}^{l}{}^{k}\varepsilon{}_{j}{}_{l}T{}^{b}{}^{e}T{}_{c}{}_{d}T{}_{a}{}_{e}\lambda{}_{\delta}{}^{i}\\
&+\frac{8}{9}\rho^{-1}\delta{}^{j}{}_{k}(\gamma{}^{a}){}_{\alpha}{}^{\beta}(\gamma{}_{a}){}_{\gamma}{}^{\delta}(\gamma{}^{b}{}^{c}){}_{\beta}{}^{\gamma}\varepsilon{}^{l}{}^{k}\varepsilon{}_{j}{}_{l}T{}^{d}{}^{e}T{}_{b}{}_{c}T{}_{d}{}_{e}\lambda{}_{\delta}{}^{i} +\frac{1}{108}\rho^{-1}R(V){}_{a}{}_{b}{}_{j}{}^{j}(\gamma{}^{c}){}_{\beta}{}^{\gamma}(\gamma{}_{c}){}_{\delta}{}^{\rho}(\gamma{}^{d}{}^{e}){}_{\alpha}{}^{\beta}(\gamma{}^{a}{}^{b}){}_{\gamma}{}^{\delta}T{}_{d}{}_{e}\lambda{}_{\rho}{}^{i}\\
&-\frac{1}{54}\rho^{-1}R(V){}_{a}{}_{b}{}_{j}{}^{j}(\gamma{}^{c}){}_{\beta}{}^{\gamma}(\gamma{}_{c}){}_{\gamma}{}^{\delta}(\gamma{}^{d}{}^{e}){}_{\alpha}{}^{\beta}(\gamma{}^{a}{}^{b}){}_{\delta}{}^{\rho}T{}_{d}{}_{e}\lambda{}_{\rho}{}^{i} +\frac{2i}{27}\rho^{-1}\delta{}^{j}{}_{k}(\gamma{}^{a}){}_{\beta}{}^{\gamma}(\gamma{}^{b}{}^{c}){}_{\alpha}{}^{\beta}(\gamma{}^{d}{}^{e}){}_{\gamma}{}^{\delta}\varepsilon{}^{l}{}^{k}\varepsilon{}_{j}{}_{l}T{}_{b}{}_{c}\big(\mathcal D_{a}T{}_{d}{}_{e}\big)\lambda{}_{\delta}{}^{i}\\
&+\frac{2i}{27}\rho^{-1}\delta{}^{j}{}_{k}(\gamma{}^{a}){}_{\beta}{}^{\gamma}(\gamma{}^{b}{}^{c}){}_{\alpha}{}^{\beta}(\gamma{}^{d}{}^{e}){}_{\gamma}{}^{\delta}\varepsilon{}^{l}{}^{k}\varepsilon{}_{j}{}_{l}T{}_{b}{}_{c}\big(\mathcal D_{d}T{}_{e}{}_{a}\big)\lambda{}_{\delta}{}^{i} +\frac{2i}{27}\rho^{-1}\delta{}^{j}{}_{k}(\gamma{}^{a}){}_{\beta}{}^{\gamma}(\gamma{}^{b}{}^{c}){}_{\alpha}{}^{\beta}(\gamma{}^{d}{}^{e}){}_{\gamma}{}^{\delta}\varepsilon{}^{l}{}^{k}\varepsilon{}_{j}{}_{l}T{}_{b}{}_{c}\big(\mathcal D_{e}T{}_{a}{}_{d}\big)\lambda{}_{\delta}{}^{i}\\
&+\frac{2i}{27}\rho^{-1}\delta{}^{j}{}_{k}(\gamma{}^{a}){}_{\beta}{}^{\gamma}(\gamma{}^{b}{}^{c}){}_{\alpha}{}^{\beta}(\gamma{}_{d}{}_{a}){}_{\gamma}{}^{\delta}\varepsilon{}^{l}{}^{k}\varepsilon{}_{j}{}_{l}T{}_{b}{}_{c}\big(\mathcal D_{e}T{}^{e}{}^{d}\big)\lambda{}_{\delta}{}^{i} -\frac{2i}{9}\rho^{-1}\delta{}^{j}{}_{k}(\gamma{}^{a}){}_{\beta}{}^{\gamma}(\gamma{}^{b}{}^{c}){}_{\alpha}{}^{\beta}\varepsilon{}^{l}{}^{k}\varepsilon{}_{j}{}_{l}T{}_{b}{}_{c}\big(\mathcal D^{d}T{}_{d}{}_{a}\big)\lambda{}_{\gamma}{}^{i}\\
&+\frac{2}{27}\rho^{-1}\delta{}^{j}{}_{k}(\gamma{}^{a}){}_{\beta}{}^{\gamma}(\gamma{}_{b}){}_{\gamma}{}^{\delta}(\gamma{}^{c}{}^{d}){}_{\alpha}{}^{\beta}\varepsilon{}^{l}{}^{k}\varepsilon{}_{j}{}_{l}T{}_{c}{}_{d}\big(\mathcal D^{e}T{}^{f}{}^{g}\big)\epsilon{}_{e}{}_{a}{}^{b}{}_{f}{}_{g}\lambda{}_{\delta}{}^{i} +\frac{8i}{81}\rho^{-1}\delta{}^{j}{}_{k}(\gamma{}^{a}){}_{\beta}{}^{\gamma}(\gamma{}^{b}{}^{c}){}_{\alpha}{}^{\beta}(\gamma{}_{d}{}_{a}){}_{\gamma}{}^{\delta}\varepsilon{}^{l}{}^{k}\varepsilon{}_{j}{}_{l}T{}^{e}{}^{f}T{}_{b}{}_{c}T{}_{g}{}_{h}\epsilon{}^{d}{}^{g}{}^{h}{}_{e}{}_{f}\lambda{}_{\delta}{}^{i}\\
&-\frac{8i}{27}\rho^{-1}\delta{}^{j}{}_{k}(\gamma{}^{a}){}_{\beta}{}^{\gamma}(\gamma{}^{b}{}^{c}){}_{\alpha}{}^{\beta}\varepsilon{}^{l}{}^{k}\varepsilon{}_{j}{}_{l}T{}^{d}{}^{e}T{}^{f}{}^{g}T{}_{b}{}_{c}\epsilon{}_{a}{}_{f}{}_{g}{}_{d}{}_{e}\lambda{}_{\gamma}{}^{i} +\frac{128}{81}\rho^{-1}\delta{}^{j}{}_{k}(\gamma{}^{a}){}_{\beta}{}^{\gamma}(\gamma{}_{b}){}_{\gamma}{}^{\delta}(\gamma{}^{c}{}^{d}){}_{\alpha}{}^{\beta}\varepsilon{}^{l}{}^{k}\varepsilon{}_{j}{}_{l}T{}^{b}{}^{e}T{}_{c}{}_{d}T{}_{a}{}_{e}\lambda{}_{\delta}{}^{i}\\
&-\frac{8}{27}\rho^{-1}\delta{}^{j}{}_{k}(\gamma{}^{a}){}_{\beta}{}^{\gamma}(\gamma{}_{a}){}_{\gamma}{}^{\delta}(\gamma{}^{b}{}^{c}){}_{\alpha}{}^{\beta}\varepsilon{}^{l}{}^{k}\varepsilon{}_{j}{}_{l}T{}^{d}{}^{e}T{}_{b}{}_{c}T{}_{d}{}_{e}\lambda{}_{\delta}{}^{i} +\frac{i}{3}\rho^{-1}\big(\mathcal D_{a}Y{}^{i}{}^{j}\big)(\gamma{}^{b}){}_{\alpha}{}^{\beta}R(Q){}_{b}{}^{a}{}_{\beta}{}_{j}\\
&-\frac{1}{12}\rho^{-1}\big(\mathcal D_{a}Y{}^{i}{}^{j}\big)\epsilon{}^{b}{}_{b}{}^{a}{}^{c}{}^{d}R(Q){}_{c}{}_{d}{}_{\alpha}{}_{j} +\frac{16i}{9}\rho^{-1}\big(\mathcal D_{a}Y{}^{i}{}^{j}\big)\delta{}_{b}{}^{c}\eta{}^{d}{}^{b}\eta{}_{d}{}_{c}(\gamma{}^{a}){}_{\alpha}{}^{\beta}\chi{}_{\beta}{}_{j}\\
&-\frac{i}{3}\rho^{-1}\big(\mathcal D_{a}Y{}^{i}{}^{j}\big)(\gamma{}^{b}){}_{\alpha}{}^{\beta}R(Q){}^{a}{}_{b}{}_{\beta}{}_{j} +\frac{1}{12}\rho^{-1}\big(\mathcal D_{a}Y{}^{i}{}^{j}\big)\epsilon{}^{b}{}^{a}{}_{b}{}^{c}{}^{d}R(Q){}_{c}{}_{d}{}_{\alpha}{}_{j}\\
&-\frac{32i}{9}\rho^{-1}\big(\mathcal D_{a}Y{}^{i}{}^{j}\big)(\gamma{}^{a}){}_{\alpha}{}^{\beta}\chi{}_{\beta}{}_{j} +\frac{8i}{3}\rho^{-1}\big(\mathcal D_{a}Y{}_{j}{}^{i}\big)(\gamma{}^{a}){}_{\alpha}{}^{\beta}\chi{}_{\beta}{}^{j}\\
&+\frac{8i}{3}\rho^{-1}\big(\mathcal D_{a}Y{}_{j}{}^{j}\big)(\gamma{}^{a}){}_{\alpha}{}^{\beta}\chi{}_{\beta}{}^{i} -\frac{8i}{3}\rho^{-1}\big(\mathcal D_{a}Y{}^{i}{}_{j}\big)\delta{}^{k}{}_{l}(\gamma{}^{a}){}_{\alpha}{}^{\beta}\varepsilon{}^{m}{}^{l}\varepsilon{}_{k}{}_{m}\chi{}_{\beta}{}^{j}\\
&+\frac{8i}{3}\rho^{-1}\big(\mathcal D_{a}Y{}^{i}{}_{j}\big)(\gamma{}^{a}){}_{\alpha}{}^{\beta}\chi{}_{\beta}{}^{j} +\frac{i}{36}\rho^{-1}R(V){}_{a}{}_{b}{}_{j}{}^{i}(\gamma{}^{c}){}_{\beta}{}^{\gamma}(\gamma{}^{a}{}^{b}){}_{\alpha}{}^{\beta}\big(\mathcal D_{c}\lambda{}_{\gamma}{}^{j}\big)\\
&-\frac{i}{18}\rho^{-1}R(V){}_{a}{}_{b}{}_{j}{}^{i}(\gamma{}^{c}){}_{\alpha}{}^{\beta}(\gamma{}^{a}{}^{b}){}_{\beta}{}^{\gamma}\big(\mathcal D_{c}\lambda{}_{\gamma}{}^{j}\big) -\frac{2}{9}\rho^{-1}(\gamma{}^{a}{}^{b}){}_{\alpha}{}^{\beta}\big(\mathcal D^{c}T{}_{a}{}_{b}\big)\big(\mathcal D_{c}\lambda{}_{\beta}{}^{i}\big)\\
&+\frac{2}{9}\rho^{-1}(\gamma{}^{a}{}^{b}){}_{\alpha}{}^{\beta}\big(\mathcal D_{a}T{}_{b}{}^{c}\big)\big(\mathcal D_{c}\lambda{}_{\beta}{}^{i}\big) +\frac{2}{9}\rho^{-1}(\gamma{}^{a}{}^{b}){}_{\alpha}{}^{\beta}\big(\mathcal D_{b}T{}^{c}{}_{a}\big)\big(\mathcal D_{c}\lambda{}_{\beta}{}^{i}\big)
\end{aligned}
\tag{S6-phi-004}
```

```math
\begin{aligned}
&+\frac{2}{9}\rho^{-1}(\gamma{}_{a}{}^{b}){}_{\alpha}{}^{\beta}\big(\mathcal D_{c}T{}^{c}{}^{a}\big)\big(\mathcal D_{b}\lambda{}_{\beta}{}^{i}\big) -\frac{2}{3}\rho^{-1}\big(\mathcal D^{a}T{}_{a}{}^{b}\big)\big(\mathcal D_{b}\lambda{}_{\alpha}{}^{i}\big)\\
&-\frac{2i}{9}\rho^{-1}(\gamma{}_{a}){}_{\alpha}{}^{\beta}\big(\mathcal D^{b}T{}^{c}{}^{d}\big)\epsilon{}_{b}{}^{e}{}^{a}{}_{c}{}_{d}\big(\mathcal D_{e}\lambda{}_{\beta}{}^{i}\big) +\frac{8}{27}\rho^{-1}(\gamma{}_{a}{}^{b}){}_{\alpha}{}^{\beta}T{}^{c}{}^{d}T{}_{e}{}_{f}\epsilon{}^{a}{}^{e}{}^{f}{}_{c}{}_{d}\big(\mathcal D_{b}\lambda{}_{\beta}{}^{i}\big)\\
&-\frac{8}{9}\rho^{-1}T{}^{a}{}^{b}T{}^{c}{}^{d}\epsilon{}^{e}{}_{c}{}_{d}{}_{a}{}_{b}\big(\mathcal D_{e}\lambda{}_{\alpha}{}^{i}\big) -\frac{128i}{27}\rho^{-1}(\gamma{}_{a}){}_{\alpha}{}^{\beta}T{}^{a}{}^{b}T{}^{c}{}_{b}\big(\mathcal D_{c}\lambda{}_{\beta}{}^{i}\big)\\
&+\frac{32i}{9}\rho^{-1}(\gamma{}^{a}){}_{\alpha}{}^{\beta}T{}^{b}{}^{c}T{}_{b}{}_{c}\big(\mathcal D_{a}\lambda{}_{\beta}{}^{i}\big) +\frac{i}{72}\rho^{-1}R(V){}_{a}{}_{b}{}_{j}{}^{j}(\gamma{}^{c}){}_{\beta}{}^{\gamma}(\gamma{}^{a}{}^{b}){}_{\alpha}{}^{\beta}\big(\mathcal D_{c}\lambda{}_{\gamma}{}^{i}\big)\\
&-\frac{i}{36}\rho^{-1}R(V){}_{a}{}_{b}{}_{j}{}^{j}(\gamma{}^{c}){}_{\alpha}{}^{\beta}(\gamma{}^{a}{}^{b}){}_{\beta}{}^{\gamma}\big(\mathcal D_{c}\lambda{}_{\gamma}{}^{i}\big) -\frac{1}{9}\rho^{-1}\delta{}^{j}{}_{k}(\gamma{}^{a}{}^{b}){}_{\alpha}{}^{\beta}\varepsilon{}^{l}{}^{k}\varepsilon{}_{j}{}_{l}\big(\mathcal D^{c}T{}_{a}{}_{b}\big)\big(\mathcal D_{c}\lambda{}_{\beta}{}^{i}\big)\\
&-\frac{1}{9}\rho^{-1}\delta{}^{j}{}_{k}(\gamma{}^{a}{}^{b}){}_{\alpha}{}^{\beta}\varepsilon{}^{l}{}^{k}\varepsilon{}_{j}{}_{l}\big(\mathcal D_{a}T{}_{b}{}^{c}\big)\big(\mathcal D_{c}\lambda{}_{\beta}{}^{i}\big) -\frac{1}{9}\rho^{-1}\delta{}^{j}{}_{k}(\gamma{}^{a}{}^{b}){}_{\alpha}{}^{\beta}\varepsilon{}^{l}{}^{k}\varepsilon{}_{j}{}_{l}\big(\mathcal D_{b}T{}^{c}{}_{a}\big)\big(\mathcal D_{c}\lambda{}_{\beta}{}^{i}\big)\\
&-\frac{1}{9}\rho^{-1}\delta{}^{j}{}_{k}(\gamma{}_{a}{}^{b}){}_{\alpha}{}^{\beta}\varepsilon{}^{l}{}^{k}\varepsilon{}_{j}{}_{l}\big(\mathcal D_{c}T{}^{c}{}^{a}\big)\big(\mathcal D_{b}\lambda{}_{\beta}{}^{i}\big) +\frac{1}{3}\rho^{-1}\delta{}^{j}{}_{k}\varepsilon{}^{l}{}^{k}\varepsilon{}_{j}{}_{l}\big(\mathcal D^{a}T{}_{a}{}^{b}\big)\big(\mathcal D_{b}\lambda{}_{\alpha}{}^{i}\big)\\
&+\frac{i}{9}\rho^{-1}\delta{}^{j}{}_{k}(\gamma{}_{a}){}_{\alpha}{}^{\beta}\varepsilon{}^{l}{}^{k}\varepsilon{}_{j}{}_{l}\big(\mathcal D^{b}T{}^{c}{}^{d}\big)\epsilon{}_{b}{}^{e}{}^{a}{}_{c}{}_{d}\big(\mathcal D_{e}\lambda{}_{\beta}{}^{i}\big) -\frac{4}{27}\rho^{-1}\delta{}^{j}{}_{k}(\gamma{}_{a}{}^{b}){}_{\alpha}{}^{\beta}\varepsilon{}^{l}{}^{k}\varepsilon{}_{j}{}_{l}T{}^{c}{}^{d}T{}_{e}{}_{f}\epsilon{}^{a}{}^{e}{}^{f}{}_{c}{}_{d}\big(\mathcal D_{b}\lambda{}_{\beta}{}^{i}\big)\\
&+\frac{4}{9}\rho^{-1}\delta{}^{j}{}_{k}\varepsilon{}^{l}{}^{k}\varepsilon{}_{j}{}_{l}T{}^{a}{}^{b}T{}^{c}{}^{d}\epsilon{}^{e}{}_{c}{}_{d}{}_{a}{}_{b}\big(\mathcal D_{e}\lambda{}_{\alpha}{}^{i}\big) +\frac{64i}{27}\rho^{-1}\delta{}^{j}{}_{k}(\gamma{}_{a}){}_{\alpha}{}^{\beta}\varepsilon{}^{l}{}^{k}\varepsilon{}_{j}{}_{l}T{}^{a}{}^{b}T{}^{c}{}_{b}\big(\mathcal D_{c}\lambda{}_{\beta}{}^{i}\big)\\
&-\frac{4i}{9}\rho^{-1}\delta{}^{j}{}_{k}(\gamma{}^{a}){}_{\alpha}{}^{\beta}\varepsilon{}^{l}{}^{k}\varepsilon{}_{j}{}_{l}T{}^{b}{}^{c}T{}_{b}{}_{c}\big(\mathcal D_{a}\lambda{}_{\beta}{}^{i}\big) -\frac{i}{72}\rho^{-1}R(V){}_{a}{}_{b}{}_{j}{}^{i}(\gamma{}^{c}){}_{\beta}{}^{\gamma}(\gamma{}^{d}){}_{\delta}{}^{\rho}(\gamma{}_{c}){}_{\gamma}{}^{\delta}(\gamma{}^{a}{}^{b}){}_{\alpha}{}^{\beta}\big(\mathcal D_{d}\lambda{}_{\rho}{}^{j}\big)\\
&+\frac{i}{36}\rho^{-1}R(V){}_{a}{}_{b}{}_{j}{}^{i}(\gamma{}^{c}){}_{\alpha}{}^{\beta}(\gamma{}^{d}){}_{\gamma}{}^{\delta}(\gamma{}_{c}){}_{\rho}{}^{\gamma}(\gamma{}^{a}{}^{b}){}_{\beta}{}^{\rho}\big(\mathcal D_{d}\lambda{}_{\delta}{}^{j}\big) -\frac{1}{9}\rho^{-1}(\gamma{}^{a}){}_{\beta}{}^{\gamma}(\gamma{}_{b}){}_{\delta}{}^{\beta}(\gamma{}^{c}{}^{d}){}_{\alpha}{}^{\delta}\big(\mathcal D_{c}T{}_{d}{}^{b}\big)\big(\mathcal D_{a}\lambda{}_{\gamma}{}^{i}\big)\\
&-\frac{1}{9}\rho^{-1}(\gamma{}^{a}){}_{\beta}{}^{\gamma}(\gamma{}_{b}){}_{\delta}{}^{\beta}(\gamma{}^{c}{}^{d}){}_{\alpha}{}^{\delta}\big(\mathcal D_{d}T{}^{b}{}_{c}\big)\big(\mathcal D_{a}\lambda{}_{\gamma}{}^{i}\big) -\frac{1}{9}\rho^{-1}(\gamma{}^{a}){}_{\beta}{}^{\gamma}(\gamma{}_{b}){}_{\delta}{}^{\beta}(\gamma{}_{c}{}^{b}){}_{\alpha}{}^{\delta}\big(\mathcal D_{d}T{}^{d}{}^{c}\big)\big(\mathcal D_{a}\lambda{}_{\gamma}{}^{i}\big)\\
&+\frac{1}{3}\rho^{-1}(\gamma{}^{a}){}_{\beta}{}^{\gamma}(\gamma{}_{b}){}_{\alpha}{}^{\beta}\big(\mathcal D^{c}T{}_{c}{}^{b}\big)\big(\mathcal D_{a}\lambda{}_{\gamma}{}^{i}\big) +\frac{i}{9}\rho^{-1}(\gamma{}^{a}){}_{\beta}{}^{\gamma}(\gamma{}_{b}){}_{\alpha}{}^{\delta}(\gamma{}_{c}){}_{\delta}{}^{\beta}\big(\mathcal D^{d}T{}^{e}{}^{f}\big)\epsilon{}_{d}{}^{c}{}^{b}{}_{e}{}_{f}\big(\mathcal D_{a}\lambda{}_{\gamma}{}^{i}\big)\\
&-\frac{4}{27}\rho^{-1}(\gamma{}^{a}){}_{\beta}{}^{\gamma}(\gamma{}_{b}){}_{\delta}{}^{\beta}(\gamma{}_{c}{}^{b}){}_{\alpha}{}^{\delta}T{}^{d}{}^{e}T{}_{f}{}_{g}\epsilon{}^{c}{}^{f}{}^{g}{}_{d}{}_{e}\big(\mathcal D_{a}\lambda{}_{\gamma}{}^{i}\big) +\frac{4}{9}\rho^{-1}(\gamma{}^{a}){}_{\beta}{}^{\gamma}(\gamma{}_{b}){}_{\alpha}{}^{\beta}T{}^{c}{}^{d}T{}^{e}{}^{f}\epsilon{}^{b}{}_{e}{}_{f}{}_{c}{}_{d}\big(\mathcal D_{a}\lambda{}_{\gamma}{}^{i}\big)\\
&+\frac{64i}{27}\rho^{-1}(\gamma{}^{a}){}_{\beta}{}^{\gamma}(\gamma{}_{b}){}_{\alpha}{}^{\delta}(\gamma{}_{c}){}_{\delta}{}^{\beta}T{}^{b}{}^{d}T{}^{c}{}_{d}\big(\mathcal D_{a}\lambda{}_{\gamma}{}^{i}\big) -\frac{4i}{9}\rho^{-1}(\gamma{}^{a}){}_{\alpha}{}^{\beta}(\gamma{}^{b}){}_{\gamma}{}^{\delta}(\gamma{}_{a}){}_{\beta}{}^{\gamma}T{}^{c}{}^{d}T{}_{c}{}_{d}\big(\mathcal D_{b}\lambda{}_{\delta}{}^{i}\big)\\
&-\frac{1}{108}\rho^{-1}R(V){}_{a}{}_{b}{}_{j}{}^{i}(\gamma{}^{c}){}_{\beta}{}^{\gamma}(\gamma{}_{c}){}_{\gamma}{}^{\delta}(\gamma{}^{a}{}^{b}){}_{\alpha}{}^{\beta}(\gamma{}^{d}{}^{e}){}_{\delta}{}_{\rho}T{}_{d}{}_{e}\lambda{}^{\rho}{}^{j} +\frac{1}{54}\rho^{-1}R(V){}_{a}{}_{b}{}_{j}{}^{i}(\gamma{}^{c}){}_{\alpha}{}^{\beta}(\gamma{}_{c}){}_{\gamma}{}^{\delta}(\gamma{}^{a}{}^{b}){}_{\beta}{}^{\gamma}(\gamma{}^{d}{}^{e}){}_{\delta}{}_{\rho}T{}_{d}{}_{e}\lambda{}^{\rho}{}^{j}\\
&+\frac{2i}{27}\rho^{-1}(\gamma{}_{a}){}_{\beta}{}^{\gamma}(\gamma{}^{b}{}^{c}){}_{\alpha}{}^{\beta}(\gamma{}^{d}{}^{e}){}_{\gamma}{}_{\delta}T{}_{d}{}_{e}\big(\mathcal D_{b}T{}_{c}{}^{a}\big)\lambda{}^{\delta}{}^{i} +\frac{2i}{27}\rho^{-1}(\gamma{}_{a}){}_{\beta}{}^{\gamma}(\gamma{}^{b}{}^{c}){}_{\alpha}{}^{\beta}(\gamma{}^{d}{}^{e}){}_{\gamma}{}_{\delta}T{}_{d}{}_{e}\big(\mathcal D_{c}T{}^{a}{}_{b}\big)\lambda{}^{\delta}{}^{i}\\
&+\frac{2i}{27}\rho^{-1}(\gamma{}_{a}){}_{\beta}{}^{\gamma}(\gamma{}^{b}{}^{c}){}_{\gamma}{}_{\delta}(\gamma{}_{d}{}^{a}){}_{\alpha}{}^{\beta}T{}_{b}{}_{c}\big(\mathcal D_{e}T{}^{e}{}^{d}\big)\lambda{}^{\delta}{}^{i} -\frac{2i}{9}\rho^{-1}(\gamma{}_{a}){}_{\alpha}{}^{\beta}(\gamma{}^{b}{}^{c}){}_{\beta}{}_{\gamma}T{}_{b}{}_{c}\big(\mathcal D^{d}T{}_{d}{}^{a}\big)\lambda{}^{\gamma}{}^{i}\\
&+\frac{2}{27}\rho^{-1}(\gamma{}_{a}){}_{\alpha}{}^{\beta}(\gamma{}_{b}){}_{\beta}{}^{\gamma}(\gamma{}^{c}{}^{d}){}_{\gamma}{}_{\delta}T{}_{c}{}_{d}\big(\mathcal D^{e}T{}^{f}{}^{g}\big)\epsilon{}_{e}{}^{b}{}^{a}{}_{f}{}_{g}\lambda{}^{\delta}{}^{i} +\frac{8i}{81}\rho^{-1}(\gamma{}_{a}){}_{\beta}{}^{\gamma}(\gamma{}^{b}{}^{c}){}_{\gamma}{}_{\delta}(\gamma{}_{d}{}^{a}){}_{\alpha}{}^{\beta}T{}^{e}{}^{f}T{}_{g}{}_{h}T{}_{b}{}_{c}\epsilon{}^{d}{}^{g}{}^{h}{}_{e}{}_{f}\lambda{}^{\delta}{}^{i}\\
&-\frac{8i}{27}\rho^{-1}(\gamma{}_{a}){}_{\alpha}{}^{\beta}(\gamma{}^{b}{}^{c}){}_{\beta}{}_{\gamma}T{}^{d}{}^{e}T{}^{f}{}^{g}T{}_{b}{}_{c}\epsilon{}^{a}{}_{f}{}_{g}{}_{d}{}_{e}\lambda{}^{\gamma}{}^{i} +\frac{128}{81}\rho^{-1}(\gamma{}_{a}){}_{\alpha}{}^{\beta}(\gamma{}_{b}){}_{\beta}{}^{\gamma}(\gamma{}^{c}{}^{d}){}_{\gamma}{}_{\delta}T{}^{a}{}^{e}T{}^{b}{}_{e}T{}_{c}{}_{d}\lambda{}^{\delta}{}^{i}\\
&-\frac{8}{27}\rho^{-1}(\gamma{}^{a}){}_{\alpha}{}^{\beta}(\gamma{}_{a}){}_{\beta}{}^{\gamma}(\gamma{}^{b}{}^{c}){}_{\gamma}{}_{\delta}T{}^{d}{}^{e}T{}_{d}{}_{e}T{}_{b}{}_{c}\lambda{}^{\delta}{}^{i} +\frac{1}{9}R(V){}_{a}{}_{b}{}_{j}{}^{i}(\gamma{}^{c}){}_{\beta}{}^{\gamma}(\gamma{}_{c}){}_{\gamma}{}^{\delta}(\gamma{}^{a}{}^{b}){}_{\alpha}{}^{\beta}\chi{}_{\delta}{}^{j}\\
&-\frac{2}{9}R(V){}_{a}{}_{b}{}_{j}{}^{i}(\gamma{}^{c}){}_{\alpha}{}^{\beta}(\gamma{}_{c}){}_{\gamma}{}^{\delta}(\gamma{}^{a}{}^{b}){}_{\beta}{}^{\gamma}\chi{}_{\delta}{}^{j} -\frac{8i}{9}(\gamma{}_{a}){}_{\beta}{}^{\gamma}(\gamma{}^{b}{}^{c}){}_{\alpha}{}^{\beta}\big(\mathcal D_{b}T{}_{c}{}^{a}\big)\chi{}_{\gamma}{}^{i}\\
&-\frac{8i}{9}(\gamma{}_{a}){}_{\beta}{}^{\gamma}(\gamma{}^{b}{}^{c}){}_{\alpha}{}^{\beta}\big(\mathcal D_{c}T{}^{a}{}_{b}\big)\chi{}_{\gamma}{}^{i} -\frac{8i}{9}(\gamma{}_{a}){}_{\beta}{}^{\gamma}(\gamma{}_{b}{}^{a}){}_{\alpha}{}^{\beta}\big(\mathcal D_{c}T{}^{c}{}^{b}\big)\chi{}_{\gamma}{}^{i}\\
&+\frac{8i}{3}(\gamma{}_{a}){}_{\alpha}{}^{\beta}\big(\mathcal D^{b}T{}_{b}{}^{a}\big)\chi{}_{\beta}{}^{i} -\frac{8}{9}(\gamma{}_{a}){}_{\alpha}{}^{\beta}(\gamma{}_{b}){}_{\beta}{}^{\gamma}\big(\mathcal D^{c}T{}^{d}{}^{e}\big)\epsilon{}_{c}{}^{b}{}^{a}{}_{d}{}_{e}\chi{}_{\gamma}{}^{i}\\
&-\frac{32i}{27}(\gamma{}_{a}){}_{\beta}{}^{\gamma}(\gamma{}_{b}{}^{a}){}_{\alpha}{}^{\beta}T{}^{c}{}^{d}T{}_{e}{}_{f}\epsilon{}^{b}{}^{e}{}^{f}{}_{c}{}_{d}\chi{}_{\gamma}{}^{i} +\frac{32i}{9}(\gamma{}_{a}){}_{\alpha}{}^{\beta}T{}^{b}{}^{c}T{}^{d}{}^{e}\epsilon{}^{a}{}_{d}{}_{e}{}_{b}{}_{c}\chi{}_{\beta}{}^{i}\\
&-\frac{512}{27}(\gamma{}_{a}){}_{\alpha}{}^{\beta}(\gamma{}_{b}){}_{\beta}{}^{\gamma}T{}^{a}{}^{c}T{}^{b}{}_{c}\chi{}_{\gamma}{}^{i} +\frac{32}{9}(\gamma{}^{a}){}_{\alpha}{}^{\beta}(\gamma{}_{a}){}_{\beta}{}^{\gamma}T{}^{b}{}^{c}T{}_{b}{}_{c}\chi{}_{\gamma}{}^{i}\\
&+\frac{i}{72}\rho^{-1}R(V){}_{a}{}_{b}{}^{j}{}_{j}(\gamma{}^{c}){}_{\beta}{}^{\gamma}(\gamma{}^{d}){}_{\delta}{}^{\rho}(\gamma{}_{c}){}_{\gamma}{}^{\delta}(\gamma{}^{a}{}^{b}){}_{\alpha}{}^{\beta}\big(\mathcal D_{d}\lambda{}_{\rho}{}^{i}\big) -\frac{i}{36}\rho^{-1}R(V){}_{a}{}_{b}{}^{j}{}_{j}(\gamma{}^{c}){}_{\alpha}{}^{\beta}(\gamma{}^{d}){}_{\gamma}{}^{\delta}(\gamma{}_{c}){}_{\rho}{}^{\gamma}(\gamma{}^{a}{}^{b}){}_{\beta}{}^{\rho}\big(\mathcal D_{d}\lambda{}_{\delta}{}^{i}\big)\\
&-\frac{1}{9}\rho^{-1}(\gamma{}^{a}){}_{\beta}{}^{\gamma}(\gamma{}_{b}){}_{\delta}{}^{\beta}(\gamma{}^{c}{}^{d}){}_{\alpha}{}^{\delta}\varepsilon{}^{j}{}^{k}\varepsilon{}^{l}{}^{m}\varepsilon{}_{m}{}_{j}\varepsilon{}_{k}{}_{l}\big(\mathcal D^{b}T{}_{c}{}_{d}\big)\big(\mathcal D_{a}\lambda{}_{\gamma}{}^{i}\big) -\frac{1}{9}\rho^{-1}(\gamma{}^{a}){}_{\beta}{}^{\gamma}(\gamma{}_{b}){}_{\delta}{}^{\beta}(\gamma{}^{c}{}^{d}){}_{\alpha}{}^{\delta}\varepsilon{}^{j}{}^{k}\varepsilon{}^{l}{}^{m}\varepsilon{}_{m}{}_{j}\varepsilon{}_{k}{}_{l}\big(\mathcal D_{c}T{}_{d}{}^{b}\big)\big(\mathcal D_{a}\lambda{}_{\gamma}{}^{i}\big)\\
&-\frac{1}{9}\rho^{-1}(\gamma{}^{a}){}_{\beta}{}^{\gamma}(\gamma{}_{b}){}_{\delta}{}^{\beta}(\gamma{}^{c}{}^{d}){}_{\alpha}{}^{\delta}\varepsilon{}^{j}{}^{k}\varepsilon{}^{l}{}^{m}\varepsilon{}_{m}{}_{j}\varepsilon{}_{k}{}_{l}\big(\mathcal D_{d}T{}^{b}{}_{c}\big)\big(\mathcal D_{a}\lambda{}_{\gamma}{}^{i}\big) -\frac{1}{9}\rho^{-1}(\gamma{}^{a}){}_{\beta}{}^{\gamma}(\gamma{}_{b}){}_{\delta}{}^{\beta}(\gamma{}_{c}{}^{b}){}_{\alpha}{}^{\delta}\varepsilon{}^{j}{}^{k}\varepsilon{}^{l}{}^{m}\varepsilon{}_{m}{}_{j}\varepsilon{}_{k}{}_{l}\big(\mathcal D_{d}T{}^{d}{}^{c}\big)\big(\mathcal D_{a}\lambda{}_{\gamma}{}^{i}\big)\\
&+\frac{1}{3}\rho^{-1}(\gamma{}^{a}){}_{\beta}{}^{\gamma}(\gamma{}_{b}){}_{\alpha}{}^{\beta}\varepsilon{}^{j}{}^{k}\varepsilon{}^{l}{}^{m}\varepsilon{}_{m}{}_{j}\varepsilon{}_{k}{}_{l}\big(\mathcal D^{c}T{}_{c}{}^{b}\big)\big(\mathcal D_{a}\lambda{}_{\gamma}{}^{i}\big) +\frac{i}{9}\rho^{-1}(\gamma{}^{a}){}_{\beta}{}^{\gamma}(\gamma{}_{b}){}_{\alpha}{}^{\delta}(\gamma{}_{c}){}_{\delta}{}^{\beta}\varepsilon{}^{j}{}^{k}\varepsilon{}^{l}{}^{m}\varepsilon{}_{m}{}_{j}\varepsilon{}_{k}{}_{l}\big(\mathcal D^{d}T{}^{e}{}^{f}\big)\epsilon{}_{d}{}^{c}{}^{b}{}_{e}{}_{f}\big(\mathcal D_{a}\lambda{}_{\gamma}{}^{i}\big)\\
&-\frac{4}{27}\rho^{-1}(\gamma{}^{a}){}_{\beta}{}^{\gamma}(\gamma{}_{b}){}_{\delta}{}^{\beta}(\gamma{}_{c}{}^{b}){}_{\alpha}{}^{\delta}\varepsilon{}^{j}{}^{k}\varepsilon{}^{l}{}^{m}\varepsilon{}_{m}{}_{j}\varepsilon{}_{k}{}_{l}T{}^{d}{}^{e}T{}_{f}{}_{g}\epsilon{}^{c}{}^{f}{}^{g}{}_{d}{}_{e}\big(\mathcal D_{a}\lambda{}_{\gamma}{}^{i}\big) +\frac{4}{9}\rho^{-1}(\gamma{}^{a}){}_{\beta}{}^{\gamma}(\gamma{}_{b}){}_{\alpha}{}^{\beta}\varepsilon{}^{j}{}^{k}\varepsilon{}^{l}{}^{m}\varepsilon{}_{m}{}_{j}\varepsilon{}_{k}{}_{l}T{}^{c}{}^{d}T{}^{e}{}^{f}\epsilon{}^{b}{}_{e}{}_{f}{}_{c}{}_{d}\big(\mathcal D_{a}\lambda{}_{\gamma}{}^{i}\big)\\
&+\frac{64i}{27}\rho^{-1}(\gamma{}^{a}){}_{\beta}{}^{\gamma}(\gamma{}_{b}){}_{\alpha}{}^{\delta}(\gamma{}_{c}){}_{\delta}{}^{\beta}\varepsilon{}^{j}{}^{k}\varepsilon{}^{l}{}^{m}\varepsilon{}_{m}{}_{j}\varepsilon{}_{k}{}_{l}T{}^{b}{}^{d}T{}^{c}{}_{d}\big(\mathcal D_{a}\lambda{}_{\gamma}{}^{i}\big) -\frac{4i}{9}\rho^{-1}(\gamma{}^{a}){}_{\alpha}{}^{\beta}(\gamma{}^{b}){}_{\gamma}{}^{\delta}(\gamma{}_{a}){}_{\beta}{}^{\gamma}\varepsilon{}^{j}{}^{k}\varepsilon{}^{l}{}^{m}\varepsilon{}_{m}{}_{j}\varepsilon{}_{k}{}_{l}T{}^{c}{}^{d}T{}_{c}{}_{d}\big(\mathcal D_{b}\lambda{}_{\delta}{}^{i}\big)\\
&+\frac{1}{108}\rho^{-1}R(V){}_{a}{}_{b}{}^{j}{}_{j}(\gamma{}^{c}){}_{\beta}{}^{\gamma}(\gamma{}_{c}){}_{\gamma}{}^{\delta}(\gamma{}^{a}{}^{b}){}_{\alpha}{}^{\beta}(\gamma{}^{d}{}^{e}){}_{\delta}{}_{\rho}T{}_{d}{}_{e}\lambda{}^{\rho}{}^{i} -\frac{1}{54}\rho^{-1}R(V){}_{a}{}_{b}{}^{j}{}_{j}(\gamma{}^{c}){}_{\alpha}{}^{\beta}(\gamma{}_{c}){}_{\gamma}{}^{\delta}(\gamma{}^{a}{}^{b}){}_{\beta}{}^{\gamma}(\gamma{}^{d}{}^{e}){}_{\delta}{}_{\rho}T{}_{d}{}_{e}\lambda{}^{\rho}{}^{i}\\
&+\frac{2i}{27}\rho^{-1}(\gamma{}_{a}){}_{\beta}{}^{\gamma}(\gamma{}^{b}{}^{c}){}_{\alpha}{}^{\beta}(\gamma{}^{d}{}^{e}){}_{\gamma}{}_{\delta}\varepsilon{}^{j}{}^{k}\varepsilon{}^{l}{}^{m}\varepsilon{}_{m}{}_{j}\varepsilon{}_{k}{}_{l}T{}_{d}{}_{e}\big(\mathcal D^{a}T{}_{b}{}_{c}\big)\lambda{}^{\delta}{}^{i} +\frac{2i}{27}\rho^{-1}(\gamma{}_{a}){}_{\beta}{}^{\gamma}(\gamma{}^{b}{}^{c}){}_{\alpha}{}^{\beta}(\gamma{}^{d}{}^{e}){}_{\gamma}{}_{\delta}\varepsilon{}^{j}{}^{k}\varepsilon{}^{l}{}^{m}\varepsilon{}_{m}{}_{j}\varepsilon{}_{k}{}_{l}T{}_{d}{}_{e}\big(\mathcal D_{b}T{}_{c}{}^{a}\big)\lambda{}^{\delta}{}^{i}\\
&+\frac{2i}{27}\rho^{-1}(\gamma{}_{a}){}_{\beta}{}^{\gamma}(\gamma{}^{b}{}^{c}){}_{\alpha}{}^{\beta}(\gamma{}^{d}{}^{e}){}_{\gamma}{}_{\delta}\varepsilon{}^{j}{}^{k}\varepsilon{}^{l}{}^{m}\varepsilon{}_{m}{}_{j}\varepsilon{}_{k}{}_{l}T{}_{d}{}_{e}\big(\mathcal D_{c}T{}^{a}{}_{b}\big)\lambda{}^{\delta}{}^{i} +\frac{2i}{27}\rho^{-1}(\gamma{}_{a}){}_{\beta}{}^{\gamma}(\gamma{}^{b}{}^{c}){}_{\gamma}{}_{\delta}(\gamma{}_{d}{}^{a}){}_{\alpha}{}^{\beta}\varepsilon{}^{j}{}^{k}\varepsilon{}^{l}{}^{m}\varepsilon{}_{m}{}_{j}\varepsilon{}_{k}{}_{l}T{}_{b}{}_{c}\big(\mathcal D_{e}T{}^{e}{}^{d}\big)\lambda{}^{\delta}{}^{i}\\
&-\frac{2i}{9}\rho^{-1}(\gamma{}_{a}){}_{\alpha}{}^{\beta}(\gamma{}^{b}{}^{c}){}_{\beta}{}_{\gamma}\varepsilon{}^{j}{}^{k}\varepsilon{}^{l}{}^{m}\varepsilon{}_{m}{}_{j}\varepsilon{}_{k}{}_{l}T{}_{b}{}_{c}\big(\mathcal D^{d}T{}_{d}{}^{a}\big)\lambda{}^{\gamma}{}^{i} +\frac{2}{27}\rho^{-1}(\gamma{}_{a}){}_{\alpha}{}^{\beta}(\gamma{}_{b}){}_{\beta}{}^{\gamma}(\gamma{}^{c}{}^{d}){}_{\gamma}{}_{\delta}\varepsilon{}^{j}{}^{k}\varepsilon{}^{l}{}^{m}\varepsilon{}_{m}{}_{j}\varepsilon{}_{k}{}_{l}T{}_{c}{}_{d}\big(\mathcal D^{e}T{}^{f}{}^{g}\big)\epsilon{}_{e}{}^{b}{}^{a}{}_{f}{}_{g}\lambda{}^{\delta}{}^{i}\\
&+\frac{8i}{81}\rho^{-1}(\gamma{}_{a}){}_{\beta}{}^{\gamma}(\gamma{}^{b}{}^{c}){}_{\gamma}{}_{\delta}(\gamma{}_{d}{}^{a}){}_{\alpha}{}^{\beta}\varepsilon{}^{j}{}^{k}\varepsilon{}^{l}{}^{m}\varepsilon{}_{m}{}_{j}\varepsilon{}_{k}{}_{l}T{}^{e}{}^{f}T{}_{g}{}_{h}T{}_{b}{}_{c}\epsilon{}^{d}{}^{g}{}^{h}{}_{e}{}_{f}\lambda{}^{\delta}{}^{i} -\frac{8i}{27}\rho^{-1}(\gamma{}_{a}){}_{\alpha}{}^{\beta}(\gamma{}^{b}{}^{c}){}_{\beta}{}_{\gamma}\varepsilon{}^{j}{}^{k}\varepsilon{}^{l}{}^{m}\varepsilon{}_{m}{}_{j}\varepsilon{}_{k}{}_{l}T{}^{d}{}^{e}T{}^{f}{}^{g}T{}_{b}{}_{c}\epsilon{}^{a}{}_{f}{}_{g}{}_{d}{}_{e}\lambda{}^{\gamma}{}^{i}\\
&+\frac{128}{81}\rho^{-1}(\gamma{}_{a}){}_{\alpha}{}^{\beta}(\gamma{}_{b}){}_{\beta}{}^{\gamma}(\gamma{}^{c}{}^{d}){}_{\gamma}{}_{\delta}\varepsilon{}^{j}{}^{k}\varepsilon{}^{l}{}^{m}\varepsilon{}_{m}{}_{j}\varepsilon{}_{k}{}_{l}T{}^{a}{}^{e}T{}^{b}{}_{e}T{}_{c}{}_{d}\lambda{}^{\delta}{}^{i} -\frac{8}{27}\rho^{-1}(\gamma{}^{a}){}_{\alpha}{}^{\beta}(\gamma{}_{a}){}_{\beta}{}^{\gamma}(\gamma{}^{b}{}^{c}){}_{\gamma}{}_{\delta}\varepsilon{}^{j}{}^{k}\varepsilon{}^{l}{}^{m}\varepsilon{}_{m}{}_{j}\varepsilon{}_{k}{}_{l}T{}^{d}{}^{e}T{}_{d}{}_{e}T{}_{b}{}_{c}\lambda{}^{\delta}{}^{i}\\
&-\frac{1}{9}R(V){}_{a}{}_{b}{}^{j}{}_{j}(\gamma{}^{c}){}_{\beta}{}^{\gamma}(\gamma{}_{c}){}_{\gamma}{}^{\delta}(\gamma{}^{a}{}^{b}){}_{\alpha}{}^{\beta}\chi{}_{\delta}{}^{i} +\frac{2}{9}R(V){}_{a}{}_{b}{}^{j}{}_{j}(\gamma{}^{c}){}_{\alpha}{}^{\beta}(\gamma{}_{c}){}_{\gamma}{}^{\delta}(\gamma{}^{a}{}^{b}){}_{\beta}{}^{\gamma}\chi{}_{\delta}{}^{i}\\
&-\frac{8i}{9}(\gamma{}_{a}){}_{\beta}{}^{\gamma}(\gamma{}^{b}{}^{c}){}_{\alpha}{}^{\beta}\varepsilon{}^{j}{}^{k}\varepsilon{}^{l}{}^{m}\varepsilon{}_{m}{}_{j}\varepsilon{}_{k}{}_{l}\big(\mathcal D^{a}T{}_{b}{}_{c}\big)\chi{}_{\gamma}{}^{i} -\frac{8i}{9}(\gamma{}_{a}){}_{\beta}{}^{\gamma}(\gamma{}^{b}{}^{c}){}_{\alpha}{}^{\beta}\varepsilon{}^{j}{}^{k}\varepsilon{}^{l}{}^{m}\varepsilon{}_{m}{}_{j}\varepsilon{}_{k}{}_{l}\big(\mathcal D_{b}T{}_{c}{}^{a}\big)\chi{}_{\gamma}{}^{i}
\end{aligned}
\tag{S6-phi-005}
```

```math
\begin{aligned}
&-\frac{8i}{9}(\gamma{}_{a}){}_{\beta}{}^{\gamma}(\gamma{}^{b}{}^{c}){}_{\alpha}{}^{\beta}\varepsilon{}^{j}{}^{k}\varepsilon{}^{l}{}^{m}\varepsilon{}_{m}{}_{j}\varepsilon{}_{k}{}_{l}\big(\mathcal D_{c}T{}^{a}{}_{b}\big)\chi{}_{\gamma}{}^{i} -\frac{8i}{9}(\gamma{}_{a}){}_{\beta}{}^{\gamma}(\gamma{}_{b}{}^{a}){}_{\alpha}{}^{\beta}\varepsilon{}^{j}{}^{k}\varepsilon{}^{l}{}^{m}\varepsilon{}_{m}{}_{j}\varepsilon{}_{k}{}_{l}\big(\mathcal D_{c}T{}^{c}{}^{b}\big)\chi{}_{\gamma}{}^{i}\\
&+\frac{8i}{3}(\gamma{}_{a}){}_{\alpha}{}^{\beta}\varepsilon{}^{j}{}^{k}\varepsilon{}^{l}{}^{m}\varepsilon{}_{m}{}_{j}\varepsilon{}_{k}{}_{l}\big(\mathcal D^{b}T{}_{b}{}^{a}\big)\chi{}_{\beta}{}^{i} -\frac{8}{9}(\gamma{}_{a}){}_{\alpha}{}^{\beta}(\gamma{}_{b}){}_{\beta}{}^{\gamma}\varepsilon{}^{j}{}^{k}\varepsilon{}^{l}{}^{m}\varepsilon{}_{m}{}_{j}\varepsilon{}_{k}{}_{l}\big(\mathcal D^{c}T{}^{d}{}^{e}\big)\epsilon{}_{c}{}^{b}{}^{a}{}_{d}{}_{e}\chi{}_{\gamma}{}^{i}\\
&-\frac{32i}{27}(\gamma{}_{a}){}_{\beta}{}^{\gamma}(\gamma{}_{b}{}^{a}){}_{\alpha}{}^{\beta}\varepsilon{}^{j}{}^{k}\varepsilon{}^{l}{}^{m}\varepsilon{}_{m}{}_{j}\varepsilon{}_{k}{}_{l}T{}^{c}{}^{d}T{}_{e}{}_{f}\epsilon{}^{b}{}^{e}{}^{f}{}_{c}{}_{d}\chi{}_{\gamma}{}^{i} +\frac{32i}{9}(\gamma{}_{a}){}_{\alpha}{}^{\beta}\varepsilon{}^{j}{}^{k}\varepsilon{}^{l}{}^{m}\varepsilon{}_{m}{}_{j}\varepsilon{}_{k}{}_{l}T{}^{b}{}^{c}T{}^{d}{}^{e}\epsilon{}^{a}{}_{d}{}_{e}{}_{b}{}_{c}\chi{}_{\beta}{}^{i}\\
&-\frac{512}{27}(\gamma{}_{a}){}_{\alpha}{}^{\beta}(\gamma{}_{b}){}_{\beta}{}^{\gamma}\varepsilon{}^{j}{}^{k}\varepsilon{}^{l}{}^{m}\varepsilon{}_{m}{}_{j}\varepsilon{}_{k}{}_{l}T{}^{a}{}^{c}T{}^{b}{}_{c}\chi{}_{\gamma}{}^{i} +\frac{32}{9}(\gamma{}^{a}){}_{\alpha}{}^{\beta}(\gamma{}_{a}){}_{\beta}{}^{\gamma}\varepsilon{}^{j}{}^{k}\varepsilon{}^{l}{}^{m}\varepsilon{}_{m}{}_{j}\varepsilon{}_{k}{}_{l}T{}^{b}{}^{c}T{}_{b}{}_{c}\chi{}_{\gamma}{}^{i}\\
&+\frac{1}{27}\rho^{-1}R(V){}_{a}{}_{b}{}_{j}{}^{i}(\gamma{}^{c}){}_{\beta}{}^{\gamma}(\gamma{}_{d}){}_{\gamma}{}^{\delta}(\gamma{}^{a}{}^{b}){}_{\alpha}{}^{\beta}T{}_{c}{}^{d}\lambda{}_{\delta}{}^{j} -\frac{2}{27}\rho^{-1}R(V){}_{a}{}_{b}{}_{j}{}^{i}(\gamma{}^{c}){}_{\alpha}{}^{\beta}(\gamma{}_{d}){}_{\gamma}{}^{\delta}(\gamma{}^{a}{}^{b}){}_{\beta}{}^{\gamma}T{}_{c}{}^{d}\lambda{}_{\delta}{}^{j}\\
&-\frac{8i}{27}\rho^{-1}(\gamma{}_{a}){}_{\beta}{}^{\gamma}(\gamma{}^{b}{}^{c}){}_{\alpha}{}^{\beta}T{}_{d}{}^{a}\big(\mathcal D^{d}T{}_{b}{}_{c}\big)\lambda{}_{\gamma}{}^{i} -\frac{8i}{27}\rho^{-1}(\gamma{}_{a}){}_{\beta}{}^{\gamma}(\gamma{}^{b}{}^{c}){}_{\alpha}{}^{\beta}T{}_{d}{}^{a}\big(\mathcal D_{b}T{}_{c}{}^{d}\big)\lambda{}_{\gamma}{}^{i}\\
&-\frac{8i}{27}\rho^{-1}(\gamma{}_{a}){}_{\beta}{}^{\gamma}(\gamma{}^{b}{}^{c}){}_{\alpha}{}^{\beta}T{}_{d}{}^{a}\big(\mathcal D_{c}T{}^{d}{}_{b}\big)\lambda{}_{\gamma}{}^{i} -\frac{8i}{27}\rho^{-1}(\gamma{}_{a}){}_{\beta}{}^{\gamma}(\gamma{}_{b}{}^{c}){}_{\alpha}{}^{\beta}T{}_{c}{}^{a}\big(\mathcal D_{d}T{}^{d}{}^{b}\big)\lambda{}_{\gamma}{}^{i}\\
&+\frac{8i}{9}\rho^{-1}(\gamma{}_{a}){}_{\alpha}{}^{\beta}T{}_{b}{}^{a}\big(\mathcal D^{c}T{}_{c}{}^{b}\big)\lambda{}_{\beta}{}^{i} -\frac{8}{27}\rho^{-1}(\gamma{}_{a}){}_{\alpha}{}^{\beta}(\gamma{}_{b}){}_{\beta}{}^{\gamma}T{}_{c}{}^{b}\big(\mathcal D^{d}T{}^{e}{}^{f}\big)\epsilon{}_{d}{}^{c}{}^{a}{}_{e}{}_{f}\lambda{}_{\gamma}{}^{i}\\
&-\frac{32i}{81}\rho^{-1}(\gamma{}_{a}){}_{\beta}{}^{\gamma}(\gamma{}_{b}{}^{c}){}_{\alpha}{}^{\beta}T{}^{d}{}^{e}T{}_{c}{}^{a}T{}_{f}{}_{g}\epsilon{}^{b}{}^{f}{}^{g}{}_{d}{}_{e}\lambda{}_{\gamma}{}^{i} +\frac{32i}{27}\rho^{-1}(\gamma{}_{a}){}_{\alpha}{}^{\beta}T{}^{b}{}^{c}T{}^{d}{}^{e}T{}_{f}{}^{a}\epsilon{}^{f}{}_{d}{}_{e}{}_{b}{}_{c}\lambda{}_{\beta}{}^{i}\\
&-\frac{512}{81}\rho^{-1}(\gamma{}_{a}){}_{\alpha}{}^{\beta}(\gamma{}_{b}){}_{\beta}{}^{\gamma}T{}^{a}{}^{c}T{}^{d}{}_{c}T{}_{d}{}^{b}\lambda{}_{\gamma}{}^{i} +\frac{32}{27}\rho^{-1}(\gamma{}^{a}){}_{\alpha}{}^{\beta}(\gamma{}_{b}){}_{\beta}{}^{\gamma}T{}^{c}{}^{d}T{}_{a}{}^{b}T{}_{c}{}_{d}\lambda{}_{\gamma}{}^{i}\\
&+\frac{1}{27}\rho^{-1}R(V){}_{a}{}_{b}{}_{j}{}^{j}(\gamma{}^{c}){}_{\beta}{}^{\gamma}(\gamma{}_{d}){}_{\gamma}{}^{\delta}(\gamma{}^{a}{}^{b}){}_{\alpha}{}^{\beta}T{}_{c}{}^{d}\lambda{}_{\delta}{}^{i} -\frac{2}{27}\rho^{-1}R(V){}_{a}{}_{b}{}_{j}{}^{j}(\gamma{}^{c}){}_{\alpha}{}^{\beta}(\gamma{}_{d}){}_{\gamma}{}^{\delta}(\gamma{}^{a}{}^{b}){}_{\beta}{}^{\gamma}T{}_{c}{}^{d}\lambda{}_{\delta}{}^{i}\\
&+\frac{8i}{27}\rho^{-1}\delta{}^{j}{}_{k}(\gamma{}_{a}){}_{\beta}{}^{\gamma}(\gamma{}^{b}{}^{c}){}_{\alpha}{}^{\beta}\varepsilon{}^{l}{}^{k}\varepsilon{}_{j}{}_{l}T{}_{d}{}^{a}\big(\mathcal D^{d}T{}_{b}{}_{c}\big)\lambda{}_{\gamma}{}^{i} +\frac{8i}{27}\rho^{-1}\delta{}^{j}{}_{k}(\gamma{}_{a}){}_{\beta}{}^{\gamma}(\gamma{}^{b}{}^{c}){}_{\alpha}{}^{\beta}\varepsilon{}^{l}{}^{k}\varepsilon{}_{j}{}_{l}T{}_{d}{}^{a}\big(\mathcal D_{b}T{}_{c}{}^{d}\big)\lambda{}_{\gamma}{}^{i}\\
&+\frac{8i}{27}\rho^{-1}\delta{}^{j}{}_{k}(\gamma{}_{a}){}_{\beta}{}^{\gamma}(\gamma{}^{b}{}^{c}){}_{\alpha}{}^{\beta}\varepsilon{}^{l}{}^{k}\varepsilon{}_{j}{}_{l}T{}_{d}{}^{a}\big(\mathcal D_{c}T{}^{d}{}_{b}\big)\lambda{}_{\gamma}{}^{i} +\frac{8i}{27}\rho^{-1}\delta{}^{j}{}_{k}(\gamma{}_{a}){}_{\beta}{}^{\gamma}(\gamma{}_{b}{}^{c}){}_{\alpha}{}^{\beta}\varepsilon{}^{l}{}^{k}\varepsilon{}_{j}{}_{l}T{}_{c}{}^{a}\big(\mathcal D_{d}T{}^{d}{}^{b}\big)\lambda{}_{\gamma}{}^{i}\\
&-\frac{8i}{9}\rho^{-1}\delta{}^{j}{}_{k}(\gamma{}_{a}){}_{\alpha}{}^{\beta}\varepsilon{}^{l}{}^{k}\varepsilon{}_{j}{}_{l}T{}_{b}{}^{a}\big(\mathcal D^{c}T{}_{c}{}^{b}\big)\lambda{}_{\beta}{}^{i} +\frac{8}{27}\rho^{-1}\delta{}^{j}{}_{k}(\gamma{}_{a}){}_{\alpha}{}^{\beta}(\gamma{}_{b}){}_{\beta}{}^{\gamma}\varepsilon{}^{l}{}^{k}\varepsilon{}_{j}{}_{l}T{}_{c}{}^{b}\big(\mathcal D^{d}T{}^{e}{}^{f}\big)\epsilon{}_{d}{}^{c}{}^{a}{}_{e}{}_{f}\lambda{}_{\gamma}{}^{i}\\
&+\frac{32i}{81}\rho^{-1}\delta{}^{j}{}_{k}(\gamma{}_{a}){}_{\beta}{}^{\gamma}(\gamma{}_{b}{}^{c}){}_{\alpha}{}^{\beta}\varepsilon{}^{l}{}^{k}\varepsilon{}_{j}{}_{l}T{}^{d}{}^{e}T{}_{c}{}^{a}T{}_{f}{}_{g}\epsilon{}^{b}{}^{f}{}^{g}{}_{d}{}_{e}\lambda{}_{\gamma}{}^{i} -\frac{32i}{27}\rho^{-1}\delta{}^{j}{}_{k}(\gamma{}_{a}){}_{\alpha}{}^{\beta}\varepsilon{}^{l}{}^{k}\varepsilon{}_{j}{}_{l}T{}^{b}{}^{c}T{}^{d}{}^{e}T{}_{f}{}^{a}\epsilon{}^{f}{}_{d}{}_{e}{}_{b}{}_{c}\lambda{}_{\beta}{}^{i}\\
&+\frac{512}{81}\rho^{-1}\delta{}^{j}{}_{k}(\gamma{}_{a}){}_{\alpha}{}^{\beta}(\gamma{}_{b}){}_{\beta}{}^{\gamma}\varepsilon{}^{l}{}^{k}\varepsilon{}_{j}{}_{l}T{}^{a}{}^{c}T{}^{d}{}_{c}T{}_{d}{}^{b}\lambda{}_{\gamma}{}^{i} -\frac{32}{27}\rho^{-1}\delta{}^{j}{}_{k}(\gamma{}^{a}){}_{\alpha}{}^{\beta}(\gamma{}_{b}){}_{\beta}{}^{\gamma}\varepsilon{}^{l}{}^{k}\varepsilon{}_{j}{}_{l}T{}^{c}{}^{d}T{}_{a}{}^{b}T{}_{c}{}_{d}\lambda{}_{\gamma}{}^{i}\\
&-\frac{2i}{9}\rho^{-1}Y{}^{i}{}^{j}(\gamma{}^{a}){}_{\alpha}{}^{\beta}\big(\mathcal D^{b}R(Q){}_{b}{}_{a}{}_{\beta}{}_{j}\big) -\frac{i}{9}\rho^{-1}Y{}^{i}{}^{j}(\gamma{}_{a}){}_{\alpha}{}^{\beta}\big(\mathcal D^{b}R(Q){}_{b}{}^{a}{}_{\beta}{}_{j}\big)\\
&-\frac{2i}{9}\rho^{-1}Y{}^{i}{}^{j}(\gamma{}^{a}){}_{\alpha}{}^{\beta}\big(\mathcal D_{a}R(Q){}_{b}{}^{b}{}_{\beta}{}_{j}\big) -\frac{1}{18}\rho^{-1}Y{}^{i}{}^{j}\epsilon{}_{a}{}^{a}{}^{b}{}^{c}{}^{d}\big(\mathcal D_{b}R(Q){}_{c}{}_{d}{}_{\alpha}{}_{j}\big)\\
&-\frac{16}{9}\rho^{-1}Y{}^{i}{}^{j}(\gamma{}^{a}){}_{\beta}{}^{\gamma}(\gamma{}_{a}){}_{\alpha}{}^{\delta}(\gamma{}_{b}{}_{c}){}_{\delta}{}^{\beta}T{}^{b}{}^{c}\chi{}_{\gamma}{}_{j} +\frac{16}{27}\rho^{-1}Y{}^{i}{}^{j}(\gamma{}^{a}){}_{\beta}{}^{\gamma}(\gamma{}_{a}){}_{\delta}{}^{\beta}(\gamma{}_{b}{}_{c}){}_{\alpha}{}^{\delta}T{}^{b}{}^{c}\chi{}_{\gamma}{}_{j}\\
&-\frac{2i}{27}\rho^{-1}Y{}^{i}{}^{j}(\gamma{}^{a}){}_{\alpha}{}^{\beta}T{}^{b}{}^{c}\epsilon{}_{a}{}_{d}{}_{e}{}_{b}{}_{c}R(Q){}^{d}{}^{e}{}_{\beta}{}_{j} -\frac{8}{9}\rho^{-1}Y{}^{i}{}^{j}\delta{}_{a}{}^{b}\eta{}^{c}{}^{a}\eta{}_{b}{}_{c}T{}^{d}{}^{e}R(Q){}_{d}{}_{e}{}_{\alpha}{}_{j}\\
&-\frac{8}{27}\rho^{-1}Y{}^{i}{}^{j}(\gamma{}_{a}{}^{a}){}_{\alpha}{}^{\beta}T{}^{b}{}^{c}R(Q){}_{b}{}_{c}{}_{\beta}{}_{j} +\frac{8}{27}\rho^{-1}Y{}^{i}{}^{j}(\gamma{}_{a}{}_{b}){}_{\alpha}{}^{\beta}T{}^{a}{}^{b}R(Q){}_{c}{}^{c}{}_{\beta}{}_{j}\\
&-\frac{52}{27}\rho^{-1}Y{}^{i}{}^{j}T{}_{a}{}_{b}R(Q){}^{b}{}^{a}{}_{\alpha}{}_{j} -\frac{44}{27}\rho^{-1}Y{}^{i}{}^{j}T{}^{a}{}^{b}R(Q){}_{b}{}_{a}{}_{\alpha}{}_{j}\\
&-\frac{13i}{27}\rho^{-1}Y{}^{i}{}^{j}(\gamma{}_{a}){}_{\alpha}{}^{\beta}T{}^{b}{}^{c}\epsilon{}^{d}{}^{e}{}^{a}{}_{b}{}_{c}R(Q){}_{d}{}_{e}{}_{\beta}{}_{j} -\frac{16}{3}\rho^{-2}Y{}^{i}{}^{j}T{}^{a}{}^{b}T{}_{a}{}_{b}\lambda{}_{\alpha}{}_{j}\\
&-\frac{16}{9}\rho^{-1}(\gamma{}^{a}{}^{b}){}_{\alpha}{}_{\beta}T{}^{c}{}^{d}T{}_{a}{}_{b}T{}_{c}{}_{d}\lambda{}^{\beta}{}^{i} -\frac{64}{3}T{}^{a}{}^{b}T{}_{a}{}_{b}\chi{}_{\alpha}{}^{i}\\
&-\frac{8i}{3}\rho^{-1}(\gamma{}^{a}){}_{\alpha}{}^{\beta}\varepsilon{}^{j}{}^{k}\varepsilon{}_{k}{}_{j}T{}^{b}{}^{c}T{}_{b}{}_{c}\big(\mathcal D_{a}\lambda{}_{\beta}{}^{i}\big) +\frac{16}{9}\rho^{-1}(\gamma{}^{a}{}^{b}){}_{\alpha}{}_{\beta}\varepsilon{}^{j}{}^{k}\varepsilon{}_{k}{}_{j}T{}^{c}{}^{d}T{}_{a}{}_{b}T{}_{c}{}_{d}\lambda{}^{\beta}{}^{i}\\
&+\frac{64}{3}\varepsilon{}^{j}{}^{k}\varepsilon{}_{k}{}_{j}T{}^{a}{}^{b}T{}_{a}{}_{b}\chi{}_{\alpha}{}^{i} -\frac{1}{8}\rho^{-1}Y{}^{i}{}^{j}(\gamma{}^{a}{}^{b}){}^{\beta}{}^{\gamma}(\gamma{}^{c}{}^{d}){}_{\alpha}{}_{\beta}T{}_{a}{}_{b}R(Q){}_{c}{}_{d}{}_{\gamma}{}_{j}\\
&+\frac{8}{3}\rho^{-1}Y{}^{i}{}^{j}(\gamma{}^{a}{}^{b}){}^{\beta}{}_{\alpha}T{}_{a}{}_{b}\chi{}_{\beta}{}_{j} -\frac{1}{8}\rho^{-1}Y{}^{i}{}^{j}(\gamma{}^{a}{}^{b}){}_{\alpha}{}_{\beta}(\gamma{}_{c}{}_{d}){}^{\beta}{}^{\gamma}T{}^{c}{}^{d}R(Q){}_{a}{}_{b}{}_{\gamma}{}_{j}\\
&+\frac{8}{3}\rho^{-1}Y{}^{i}{}^{j}(\gamma{}_{a}{}_{b}){}_{\alpha}{}^{\beta}T{}^{a}{}^{b}\chi{}_{\beta}{}_{j} +\frac{8}{3}\rho^{-1}Y{}^{i}{}^{j}(\gamma{}_{a}{}_{b}){}^{\beta}{}_{\alpha}T{}^{a}{}^{b}\chi{}_{\beta}{}_{j}\\
&-\frac{1}{36}\rho^{-1}R(M){}_{a}{}_{b}{}_{c}{}_{d}(\gamma{}^{c}{}^{d}){}_{\beta}{}^{\gamma}(\gamma{}^{a}{}^{b}){}_{\alpha}{}_{\delta}(\gamma{}_{e}{}_{f}){}^{\delta}{}^{\beta}T{}^{e}{}^{f}\lambda{}_{\gamma}{}^{i} +\frac{16}{81}\rho^{-1}(\gamma{}^{a}{}^{b}){}_{\beta}{}^{\gamma}(\gamma{}^{c}{}^{d}){}_{\alpha}{}_{\delta}(\gamma{}_{e}{}_{f}){}^{\delta}{}^{\beta}T{}^{e}{}^{f}T{}_{c}{}_{d}T{}_{a}{}_{b}\lambda{}_{\gamma}{}^{i}\\
&+\frac{16}{81}\rho^{-1}(\gamma{}^{a}{}^{b}){}_{\beta}{}^{\gamma}(\gamma{}^{c}{}^{d}){}_{\alpha}{}_{\delta}(\gamma{}_{e}{}_{f}){}^{\beta}{}^{\delta}T{}^{e}{}^{f}T{}_{c}{}_{d}T{}_{a}{}_{b}\lambda{}_{\gamma}{}^{i} +\frac{16}{81}\rho^{-1}(\gamma{}^{a}{}^{b}){}_{\alpha}{}^{\beta}(\gamma{}^{c}{}^{d}){}_{\gamma}{}_{\delta}(\gamma{}_{e}{}_{f}){}^{\gamma}{}^{\delta}T{}^{e}{}^{f}T{}_{a}{}_{b}T{}_{c}{}_{d}\lambda{}_{\beta}{}^{i}\\
&+\frac{4i}{27}\rho^{-1}(\gamma{}^{a}){}_{\alpha}{}_{\beta}(\gamma{}^{b}{}^{c}){}_{\gamma}{}^{\delta}(\gamma{}_{d}{}_{e}){}^{\beta}{}^{\gamma}T{}^{d}{}^{e}\big(\mathcal D_{a}T{}_{b}{}_{c}\big)\lambda{}_{\delta}{}^{i} -\frac{1}{27}\rho^{-1}R(V){}_{a}{}_{b}{}_{j}{}^{i}(\gamma{}^{a}{}^{b}){}_{\beta}{}^{\gamma}(\gamma{}_{c}{}_{d}){}_{\alpha}{}^{\beta}T{}^{c}{}^{d}\lambda{}_{\gamma}{}^{j}\\
&+\frac{4i}{27}\rho^{-1}(\gamma{}^{a}){}_{\alpha}{}_{\beta}(\gamma{}^{b}{}^{c}){}_{\gamma}{}^{\delta}(\gamma{}_{d}{}_{e}){}^{\gamma}{}^{\beta}T{}^{d}{}^{e}\big(\mathcal D_{a}T{}_{b}{}_{c}\big)\lambda{}_{\delta}{}^{i} -\frac{1}{27}\rho^{-1}R(V){}_{a}{}_{b}{}_{j}{}^{i}(\gamma{}^{a}{}^{b}){}_{\beta}{}^{\gamma}(\gamma{}_{c}{}_{d}){}^{\beta}{}_{\alpha}T{}^{c}{}^{d}\lambda{}_{\gamma}{}^{j}\\
&+\frac{4i}{27}\rho^{-1}(\gamma{}^{a}){}_{\alpha}{}^{\beta}(\gamma{}^{b}{}^{c}){}_{\gamma}{}_{\delta}(\gamma{}_{d}{}_{e}){}^{\gamma}{}^{\delta}T{}^{d}{}^{e}\big(\mathcal D_{a}T{}_{b}{}_{c}\big)\lambda{}_{\beta}{}^{i} +\frac{1}{27}\rho^{-1}R(V){}_{a}{}_{b}{}_{j}{}^{i}(\gamma{}^{a}{}^{b}){}_{\beta}{}_{\gamma}(\gamma{}_{c}{}_{d}){}^{\beta}{}^{\gamma}T{}^{c}{}^{d}\lambda{}_{\alpha}{}^{j}\\
&+\frac{2i}{27}\rho^{-1}(\gamma{}^{a}){}_{\beta}{}^{\gamma}(\gamma{}^{b}{}^{c}){}^{\delta}{}_{\gamma}(\gamma{}_{d}{}_{e}){}_{\alpha}{}^{\beta}T{}^{d}{}^{e}\big(\mathcal D_{a}T{}_{b}{}_{c}\big)\lambda{}_{\delta}{}^{i} +\frac{2i}{27}\rho^{-1}(\gamma{}^{a}){}^{\beta}{}^{\gamma}(\gamma{}^{b}{}^{c}){}_{\delta}{}_{\gamma}(\gamma{}_{d}{}_{e}){}_{\alpha}{}^{\delta}T{}^{d}{}^{e}\big(\mathcal D_{a}T{}_{b}{}_{c}\big)\lambda{}_{\beta}{}^{i}\\
&+\frac{2i}{27}\rho^{-1}(\gamma{}^{a}){}_{\beta}{}^{\gamma}(\gamma{}^{b}{}^{c}){}^{\delta}{}_{\gamma}(\gamma{}_{d}{}_{e}){}^{\beta}{}_{\alpha}T{}^{d}{}^{e}\big(\mathcal D_{a}T{}_{b}{}_{c}\big)\lambda{}_{\delta}{}^{i} +\frac{2i}{27}\rho^{-1}(\gamma{}^{a}){}^{\beta}{}^{\gamma}(\gamma{}^{b}{}^{c}){}_{\delta}{}_{\gamma}(\gamma{}_{d}{}_{e}){}^{\delta}{}_{\alpha}T{}^{d}{}^{e}\big(\mathcal D_{a}T{}_{b}{}_{c}\big)\lambda{}_{\beta}{}^{i}\\
&-\frac{2i}{27}\rho^{-1}(\gamma{}^{a}){}_{\beta}{}^{\gamma}(\gamma{}^{b}{}^{c}){}_{\delta}{}_{\gamma}(\gamma{}_{d}{}_{e}){}^{\beta}{}^{\delta}T{}^{d}{}^{e}\big(\mathcal D_{a}T{}_{b}{}_{c}\big)\lambda{}_{\alpha}{}^{i} -\frac{2i}{27}\rho^{-1}(\gamma{}^{a}){}_{\beta}{}^{\gamma}(\gamma{}^{b}{}^{c}){}_{\delta}{}_{\gamma}(\gamma{}_{d}{}_{e}){}^{\delta}{}^{\beta}T{}^{d}{}^{e}\big(\mathcal D_{a}T{}_{b}{}_{c}\big)\lambda{}_{\alpha}{}^{i}\\
&+\frac{2}{9}\rho^{-1}(\gamma{}^{a}{}^{b}){}_{\alpha}{}_{\beta}\widehat F{}_{a}{}_{b}\varepsilon{}^{j}{}^{k}\varepsilon{}_{k}{}_{j}T{}^{c}{}^{d}R(Q){}_{c}{}_{d}{}^{\beta}{}^{i} -\frac{32}{27}(\gamma{}^{a}{}^{b}){}_{\alpha}{}_{\beta}\varepsilon{}^{j}{}^{k}\varepsilon{}_{k}{}_{j}T{}^{c}{}^{d}T{}_{a}{}_{b}R(Q){}_{c}{}_{d}{}^{\beta}{}^{i}\\
&+\frac{8}{9}\rho^{-1}Y{}_{j}{}^{j}T{}^{a}{}^{b}R(Q){}_{a}{}_{b}{}_{\alpha}{}^{i} -\frac{4i}{9}\rho^{-1}(\gamma{}^{a}){}_{\alpha}{}_{\beta}\big(\mathcal D_{a}\rho\big)\varepsilon{}^{j}{}^{k}\varepsilon{}_{k}{}_{j}T{}^{b}{}^{c}R(Q){}_{b}{}_{c}{}^{\beta}{}^{i}\\
&+\frac{1}{36}\rho^{-1}R(M){}_{a}{}_{b}{}_{c}{}_{d}(\gamma{}^{c}{}^{d}){}_{\beta}{}^{\gamma}(\gamma{}^{a}{}^{b}){}_{\alpha}{}_{\delta}(\gamma{}_{e}{}_{f}){}^{\delta}{}^{\beta}\varepsilon{}^{j}{}^{k}\varepsilon{}_{k}{}_{j}T{}^{e}{}^{f}\lambda{}_{\gamma}{}^{i} -\frac{16}{81}\rho^{-1}(\gamma{}^{a}{}^{b}){}_{\beta}{}^{\gamma}(\gamma{}^{c}{}^{d}){}_{\alpha}{}_{\delta}(\gamma{}_{e}{}_{f}){}^{\delta}{}^{\beta}\varepsilon{}^{j}{}^{k}\varepsilon{}_{k}{}_{j}T{}^{e}{}^{f}T{}_{c}{}_{d}T{}_{a}{}_{b}\lambda{}_{\gamma}{}^{i}\\
&-\frac{16}{81}\rho^{-1}(\gamma{}^{a}{}^{b}){}_{\beta}{}^{\gamma}(\gamma{}^{c}{}^{d}){}_{\alpha}{}_{\delta}(\gamma{}_{e}{}_{f}){}^{\beta}{}^{\delta}\varepsilon{}^{j}{}^{k}\varepsilon{}_{k}{}_{j}T{}^{e}{}^{f}T{}_{c}{}_{d}T{}_{a}{}_{b}\lambda{}_{\gamma}{}^{i} -\frac{16}{81}\rho^{-1}(\gamma{}^{a}{}^{b}){}_{\alpha}{}^{\beta}(\gamma{}^{c}{}^{d}){}_{\gamma}{}_{\delta}(\gamma{}_{e}{}_{f}){}^{\gamma}{}^{\delta}\varepsilon{}^{j}{}^{k}\varepsilon{}_{k}{}_{j}T{}^{e}{}^{f}T{}_{a}{}_{b}T{}_{c}{}_{d}\lambda{}_{\beta}{}^{i}
\end{aligned}
\tag{S6-phi-006}
```

```math
\begin{aligned}
&-\frac{4i}{27}\rho^{-1}(\gamma{}^{a}){}_{\alpha}{}_{\beta}(\gamma{}^{b}{}^{c}){}_{\gamma}{}^{\delta}(\gamma{}_{d}{}_{e}){}^{\beta}{}^{\gamma}\varepsilon{}^{j}{}^{k}\varepsilon{}_{k}{}_{j}T{}^{d}{}^{e}\big(\mathcal D_{a}T{}_{b}{}_{c}\big)\lambda{}_{\delta}{}^{i} -\frac{1}{27}\rho^{-1}R(V){}_{a}{}_{b}{}_{j}{}^{j}(\gamma{}^{a}{}^{b}){}_{\beta}{}^{\gamma}(\gamma{}_{c}{}_{d}){}_{\alpha}{}^{\beta}T{}^{c}{}^{d}\lambda{}_{\gamma}{}^{i}\\
&-\frac{4i}{27}\rho^{-1}(\gamma{}^{a}){}_{\alpha}{}_{\beta}(\gamma{}^{b}{}^{c}){}_{\gamma}{}^{\delta}(\gamma{}_{d}{}_{e}){}^{\gamma}{}^{\beta}\varepsilon{}^{j}{}^{k}\varepsilon{}_{k}{}_{j}T{}^{d}{}^{e}\big(\mathcal D_{a}T{}_{b}{}_{c}\big)\lambda{}_{\delta}{}^{i} -\frac{1}{27}\rho^{-1}R(V){}_{a}{}_{b}{}_{j}{}^{j}(\gamma{}^{a}{}^{b}){}_{\beta}{}^{\gamma}(\gamma{}_{c}{}_{d}){}^{\beta}{}_{\alpha}T{}^{c}{}^{d}\lambda{}_{\gamma}{}^{i}\\
&-\frac{4i}{27}\rho^{-1}(\gamma{}^{a}){}_{\alpha}{}^{\beta}(\gamma{}^{b}{}^{c}){}_{\gamma}{}_{\delta}(\gamma{}_{d}{}_{e}){}^{\gamma}{}^{\delta}\varepsilon{}^{j}{}^{k}\varepsilon{}_{k}{}_{j}T{}^{d}{}^{e}\big(\mathcal D_{a}T{}_{b}{}_{c}\big)\lambda{}_{\beta}{}^{i} +\frac{1}{27}\rho^{-1}R(V){}_{a}{}_{b}{}_{j}{}^{j}(\gamma{}^{a}{}^{b}){}_{\beta}{}_{\gamma}(\gamma{}_{c}{}_{d}){}^{\beta}{}^{\gamma}T{}^{c}{}^{d}\lambda{}_{\alpha}{}^{i}\\
&-\frac{2i}{27}\rho^{-1}(\gamma{}^{a}){}_{\beta}{}^{\gamma}(\gamma{}^{b}{}^{c}){}^{\delta}{}_{\gamma}(\gamma{}_{d}{}_{e}){}_{\alpha}{}^{\beta}\varepsilon{}^{j}{}^{k}\varepsilon{}_{k}{}_{j}T{}^{d}{}^{e}\big(\mathcal D_{a}T{}_{b}{}_{c}\big)\lambda{}_{\delta}{}^{i} -\frac{2i}{27}\rho^{-1}(\gamma{}^{a}){}^{\beta}{}^{\gamma}(\gamma{}^{b}{}^{c}){}_{\delta}{}_{\gamma}(\gamma{}_{d}{}_{e}){}_{\alpha}{}^{\delta}\varepsilon{}^{j}{}^{k}\varepsilon{}_{k}{}_{j}T{}^{d}{}^{e}\big(\mathcal D_{a}T{}_{b}{}_{c}\big)\lambda{}_{\beta}{}^{i}\\
&-\frac{2i}{27}\rho^{-1}(\gamma{}^{a}){}_{\beta}{}^{\gamma}(\gamma{}^{b}{}^{c}){}^{\delta}{}_{\gamma}(\gamma{}_{d}{}_{e}){}^{\beta}{}_{\alpha}\varepsilon{}^{j}{}^{k}\varepsilon{}_{k}{}_{j}T{}^{d}{}^{e}\big(\mathcal D_{a}T{}_{b}{}_{c}\big)\lambda{}_{\delta}{}^{i} -\frac{2i}{27}\rho^{-1}(\gamma{}^{a}){}^{\beta}{}^{\gamma}(\gamma{}^{b}{}^{c}){}_{\delta}{}_{\gamma}(\gamma{}_{d}{}_{e}){}^{\delta}{}_{\alpha}\varepsilon{}^{j}{}^{k}\varepsilon{}_{k}{}_{j}T{}^{d}{}^{e}\big(\mathcal D_{a}T{}_{b}{}_{c}\big)\lambda{}_{\beta}{}^{i}\\
&+\frac{2i}{27}\rho^{-1}(\gamma{}^{a}){}_{\beta}{}^{\gamma}(\gamma{}^{b}{}^{c}){}_{\delta}{}_{\gamma}(\gamma{}_{d}{}_{e}){}^{\beta}{}^{\delta}\varepsilon{}^{j}{}^{k}\varepsilon{}_{k}{}_{j}T{}^{d}{}^{e}\big(\mathcal D_{a}T{}_{b}{}_{c}\big)\lambda{}_{\alpha}{}^{i} +\frac{2i}{27}\rho^{-1}(\gamma{}^{a}){}_{\beta}{}^{\gamma}(\gamma{}^{b}{}^{c}){}_{\delta}{}_{\gamma}(\gamma{}_{d}{}_{e}){}^{\delta}{}^{\beta}\varepsilon{}^{j}{}^{k}\varepsilon{}_{k}{}_{j}T{}^{d}{}^{e}\big(\mathcal D_{a}T{}_{b}{}_{c}\big)\lambda{}_{\alpha}{}^{i}\\
&-\frac{2}{9}\rho^{-1}(\gamma{}^{a}{}^{b}){}_{\alpha}{}_{\beta}\widehat F{}_{a}{}_{b}T{}^{c}{}^{d}R(Q){}_{c}{}_{d}{}^{\beta}{}^{i} +\frac{32}{27}(\gamma{}^{a}{}^{b}){}_{\alpha}{}_{\beta}T{}^{c}{}^{d}T{}_{a}{}_{b}R(Q){}_{c}{}_{d}{}^{\beta}{}^{i}\\
&+\frac{8}{9}\rho^{-1}Y{}_{j}{}^{i}T{}^{a}{}^{b}R(Q){}_{a}{}_{b}{}_{\alpha}{}^{j} +\frac{4i}{9}\rho^{-1}(\gamma{}^{a}){}_{\alpha}{}_{\beta}\big(\mathcal D_{a}\rho\big)T{}^{b}{}^{c}R(Q){}_{b}{}_{c}{}^{\beta}{}^{i}\\
&-\frac{i}{12}\rho^{-1}R(V){}_{a}{}_{b}{}_{j}{}^{i}(\gamma{}^{c}){}^{\beta}{}^{\gamma}(\gamma{}^{a}{}^{b}){}_{\alpha}{}_{\beta}\big(\mathcal D_{c}\lambda{}_{\gamma}{}^{j}\big) +\frac{1}{2}\rho^{-1}(\gamma{}^{a}){}^{\beta}{}^{\gamma}(\gamma{}^{b}){}_{\alpha}{}^{\delta}(\gamma{}^{c}{}^{d}){}_{\beta}{}_{\delta}\big(\mathcal D_{b}T{}_{c}{}_{d}\big)\big(\mathcal D_{a}\lambda{}_{\gamma}{}^{i}\big)\\
&-\frac{8i}{9}\rho^{-1}(\gamma{}^{a}){}^{\beta}{}^{\gamma}(\gamma{}^{b}{}^{c}){}_{\alpha}{}^{\delta}(\gamma{}^{d}{}^{e}){}_{\beta}{}_{\delta}T{}_{b}{}_{c}T{}_{d}{}_{e}\big(\mathcal D_{a}\lambda{}_{\gamma}{}^{i}\big) +\frac{2i}{9}\rho^{-1}(\gamma{}^{a}){}_{\alpha}{}^{\beta}(\gamma{}^{b}{}^{c}){}^{\gamma}{}^{\delta}(\gamma{}^{d}{}^{e}){}_{\gamma}{}_{\delta}T{}_{b}{}_{c}T{}_{d}{}_{e}\big(\mathcal D_{a}\lambda{}_{\beta}{}^{i}\big)\\
&+\frac{1}{6}\rho^{-1}(\gamma{}^{a}){}^{\beta}{}^{\gamma}(\gamma{}^{b}){}_{\beta}{}^{\delta}(\gamma{}^{c}{}^{d}){}_{\alpha}{}_{\delta}\big(\mathcal D_{b}T{}_{c}{}_{d}\big)\big(\mathcal D_{a}\lambda{}_{\gamma}{}^{i}\big) +\frac{4i}{3}\rho^{-1}(\gamma{}^{a}){}^{\beta}{}^{\gamma}(\gamma{}^{b}{}^{c}){}_{\alpha}{}_{\gamma}\big(\mathcal D_{a}\widehat F{}_{b}{}_{c}\big)\varepsilon{}^{j}{}^{k}\varepsilon{}_{k}{}_{j}\chi{}_{\beta}{}^{i}\\
&-\frac{64i}{9}(\gamma{}^{a}){}^{\beta}{}^{\gamma}(\gamma{}^{b}{}^{c}){}_{\alpha}{}_{\gamma}\varepsilon{}^{j}{}^{k}\varepsilon{}_{k}{}_{j}\big(\mathcal D_{a}T{}_{b}{}_{c}\big)\chi{}_{\beta}{}^{i} -\frac{64i}{9}\rho^{-1}(\gamma{}^{a}){}^{\beta}{}^{\gamma}(\gamma{}^{b}{}^{c}){}_{\alpha}{}_{\gamma}\big(\mathcal D_{a}\rho\big)\varepsilon{}^{j}{}^{k}\varepsilon{}_{k}{}_{j}T{}_{b}{}_{c}\chi{}_{\beta}{}^{i}\\
&+\frac{16i}{3}\rho^{-1}\big(\mathcal D_{a}Y{}_{j}{}^{j}\big)(\gamma{}^{a}){}^{\beta}{}_{\alpha}\chi{}_{\beta}{}^{i} +\frac{8}{3}\rho^{-1}(\gamma{}^{a}){}^{\beta}{}^{\gamma}(\gamma{}^{b}){}_{\alpha}{}_{\gamma}\big(\mathcal D_{a}\mathcal D_{b}\rho\big)\varepsilon{}^{j}{}^{k}\varepsilon{}_{k}{}_{j}\chi{}_{\beta}{}^{i}\\
&-\frac{4}{3}\rho^{-1}(\gamma{}^{a}){}^{\beta}{}^{\gamma}(\gamma{}_{a}){}_{\alpha}{}^{\delta}(\gamma{}^{b}{}^{c}){}_{\delta}{}^{\rho}(\gamma{}^{d}{}^{e}){}_{\rho}{}_{\gamma}\widehat F{}_{d}{}_{e}\varepsilon{}^{j}{}^{k}\varepsilon{}_{k}{}_{j}T{}_{b}{}_{c}\chi{}_{\beta}{}^{i} +\frac{4}{9}\rho^{-1}(\gamma{}^{a}){}^{\beta}{}^{\gamma}(\gamma{}_{a}){}_{\delta}{}^{\rho}(\gamma{}^{b}{}^{c}){}_{\alpha}{}^{\delta}(\gamma{}^{d}{}^{e}){}_{\rho}{}_{\gamma}\widehat F{}_{d}{}_{e}\varepsilon{}^{j}{}^{k}\varepsilon{}_{k}{}_{j}T{}_{b}{}_{c}\chi{}_{\beta}{}^{i}\\
&+\frac{64}{9}(\gamma{}^{a}){}^{\beta}{}^{\gamma}(\gamma{}_{a}){}_{\alpha}{}^{\delta}(\gamma{}^{b}{}^{c}){}_{\delta}{}^{\rho}(\gamma{}^{d}{}^{e}){}_{\rho}{}_{\gamma}\varepsilon{}^{j}{}^{k}\varepsilon{}_{k}{}_{j}T{}_{b}{}_{c}T{}_{d}{}_{e}\chi{}_{\beta}{}^{i} -\frac{64}{27}(\gamma{}^{a}){}^{\beta}{}^{\gamma}(\gamma{}_{a}){}_{\delta}{}^{\rho}(\gamma{}^{b}{}^{c}){}_{\alpha}{}^{\delta}(\gamma{}^{d}{}^{e}){}_{\rho}{}_{\gamma}\varepsilon{}^{j}{}^{k}\varepsilon{}_{k}{}_{j}T{}_{b}{}_{c}T{}_{d}{}_{e}\chi{}_{\beta}{}^{i}\\
&-\frac{16}{3}\rho^{-1}Y{}_{j}{}^{j}(\gamma{}^{a}){}^{\beta}{}_{\gamma}(\gamma{}_{a}){}_{\alpha}{}^{\delta}(\gamma{}^{b}{}^{c}){}_{\delta}{}^{\gamma}T{}_{b}{}_{c}\chi{}_{\beta}{}^{i} +\frac{16}{9}\rho^{-1}Y{}_{j}{}^{j}(\gamma{}^{a}){}^{\beta}{}_{\gamma}(\gamma{}_{a}){}_{\delta}{}^{\gamma}(\gamma{}^{b}{}^{c}){}_{\alpha}{}^{\delta}T{}_{b}{}_{c}\chi{}_{\beta}{}^{i}\\
&+\frac{8i}{3}\rho^{-1}(\gamma{}^{a}){}^{\beta}{}^{\gamma}(\gamma{}^{b}){}_{\delta}{}_{\gamma}(\gamma{}_{a}){}_{\alpha}{}^{\rho}(\gamma{}^{c}{}^{d}){}_{\rho}{}^{\delta}\big(\mathcal D_{b}\rho\big)\varepsilon{}^{j}{}^{k}\varepsilon{}_{k}{}_{j}T{}_{c}{}_{d}\chi{}_{\beta}{}^{i} -\frac{8i}{9}\rho^{-1}(\gamma{}^{a}){}^{\beta}{}^{\gamma}(\gamma{}^{b}){}_{\delta}{}_{\gamma}(\gamma{}_{a}){}_{\rho}{}^{\delta}(\gamma{}^{c}{}^{d}){}_{\alpha}{}^{\rho}\big(\mathcal D_{b}\rho\big)\varepsilon{}^{j}{}^{k}\varepsilon{}_{k}{}_{j}T{}_{c}{}_{d}\chi{}_{\beta}{}^{i}\\
&-\frac{2}{9}R(V){}_{a}{}_{b}{}_{j}{}^{j}(\gamma{}^{c}){}^{\beta}{}_{\gamma}(\gamma{}_{c}){}_{\delta}{}^{\gamma}(\gamma{}^{a}{}^{b}){}_{\alpha}{}^{\delta}\chi{}_{\beta}{}^{i} +\frac{4}{9}R(V){}_{a}{}_{b}{}_{j}{}^{j}(\gamma{}^{c}){}^{\beta}{}_{\gamma}(\gamma{}_{c}){}_{\alpha}{}^{\delta}(\gamma{}^{a}{}^{b}){}_{\delta}{}^{\gamma}\chi{}_{\beta}{}^{i}\\
&-\frac{16i}{9}\delta{}^{j}{}_{k}(\gamma{}^{a}){}^{\beta}{}_{\gamma}(\gamma{}^{b}{}^{c}){}_{\alpha}{}^{\gamma}\varepsilon{}^{l}{}^{k}\varepsilon{}_{j}{}_{l}\big(\mathcal D_{a}T{}_{b}{}_{c}\big)\chi{}_{\beta}{}^{i} -\frac{16i}{9}\delta{}^{j}{}_{k}(\gamma{}^{a}){}^{\beta}{}_{\gamma}(\gamma{}^{b}{}^{c}){}_{\alpha}{}^{\gamma}\varepsilon{}^{l}{}^{k}\varepsilon{}_{j}{}_{l}\big(\mathcal D_{b}T{}_{c}{}_{a}\big)\chi{}_{\beta}{}^{i}\\
&-\frac{16i}{9}\delta{}^{j}{}_{k}(\gamma{}^{a}){}^{\beta}{}_{\gamma}(\gamma{}^{b}{}^{c}){}_{\alpha}{}^{\gamma}\varepsilon{}^{l}{}^{k}\varepsilon{}_{j}{}_{l}\big(\mathcal D_{c}T{}_{a}{}_{b}\big)\chi{}_{\beta}{}^{i} -\frac{16i}{9}\delta{}^{j}{}_{k}(\gamma{}^{a}){}^{\beta}{}_{\gamma}(\gamma{}_{b}{}_{a}){}_{\alpha}{}^{\gamma}\varepsilon{}^{l}{}^{k}\varepsilon{}_{j}{}_{l}\big(\mathcal D_{c}T{}^{c}{}^{b}\big)\chi{}_{\beta}{}^{i}\\
&+\frac{16i}{3}\delta{}^{j}{}_{k}(\gamma{}^{a}){}^{\beta}{}_{\alpha}\varepsilon{}^{l}{}^{k}\varepsilon{}_{j}{}_{l}\big(\mathcal D^{b}T{}_{b}{}_{a}\big)\chi{}_{\beta}{}^{i} -\frac{16}{9}\delta{}^{j}{}_{k}(\gamma{}^{a}){}^{\beta}{}_{\gamma}(\gamma{}_{b}){}_{\alpha}{}^{\gamma}\varepsilon{}^{l}{}^{k}\varepsilon{}_{j}{}_{l}\big(\mathcal D^{c}T{}^{d}{}^{e}\big)\epsilon{}_{c}{}_{a}{}^{b}{}_{d}{}_{e}\chi{}_{\beta}{}^{i}\\
&-\frac{64i}{27}\delta{}^{j}{}_{k}(\gamma{}^{a}){}^{\beta}{}_{\gamma}(\gamma{}_{b}{}_{a}){}_{\alpha}{}^{\gamma}\varepsilon{}^{l}{}^{k}\varepsilon{}_{j}{}_{l}T{}^{c}{}^{d}T{}_{e}{}_{f}\epsilon{}^{b}{}^{e}{}^{f}{}_{c}{}_{d}\chi{}_{\beta}{}^{i} +\frac{64i}{9}\delta{}^{j}{}_{k}(\gamma{}^{a}){}^{\beta}{}_{\alpha}\varepsilon{}^{l}{}^{k}\varepsilon{}_{j}{}_{l}T{}^{b}{}^{c}T{}^{d}{}^{e}\epsilon{}_{a}{}_{d}{}_{e}{}_{b}{}_{c}\chi{}_{\beta}{}^{i}\\
&-\frac{1024}{27}\delta{}^{j}{}_{k}(\gamma{}^{a}){}^{\beta}{}_{\gamma}(\gamma{}_{b}){}_{\alpha}{}^{\gamma}\varepsilon{}^{l}{}^{k}\varepsilon{}_{j}{}_{l}T{}^{b}{}^{c}T{}_{a}{}_{c}\chi{}_{\beta}{}^{i} +\frac{64}{9}\delta{}^{j}{}_{k}(\gamma{}^{a}){}^{\beta}{}_{\gamma}(\gamma{}_{a}){}_{\alpha}{}^{\gamma}\varepsilon{}^{l}{}^{k}\varepsilon{}_{j}{}_{l}T{}^{b}{}^{c}T{}_{b}{}_{c}\chi{}_{\beta}{}^{i}\\
&-\frac{i}{12}\rho^{-1}R(V){}_{a}{}_{b}{}_{j}{}^{j}(\gamma{}^{c}){}^{\beta}{}^{\gamma}(\gamma{}^{a}{}^{b}){}_{\alpha}{}_{\beta}\big(\mathcal D_{c}\lambda{}_{\gamma}{}^{i}\big) -\frac{1}{2}\rho^{-1}(\gamma{}^{a}){}^{\beta}{}^{\gamma}(\gamma{}^{b}){}_{\alpha}{}^{\delta}(\gamma{}^{c}{}^{d}){}_{\beta}{}_{\delta}\varepsilon{}^{j}{}^{k}\varepsilon{}_{k}{}_{j}\big(\mathcal D_{b}T{}_{c}{}_{d}\big)\big(\mathcal D_{a}\lambda{}_{\gamma}{}^{i}\big)\\
&+\frac{8i}{9}\rho^{-1}(\gamma{}^{a}){}^{\beta}{}^{\gamma}(\gamma{}^{b}{}^{c}){}_{\alpha}{}^{\delta}(\gamma{}^{d}{}^{e}){}_{\beta}{}_{\delta}\varepsilon{}^{j}{}^{k}\varepsilon{}_{k}{}_{j}T{}_{b}{}_{c}T{}_{d}{}_{e}\big(\mathcal D_{a}\lambda{}_{\gamma}{}^{i}\big) -\frac{2i}{9}\rho^{-1}(\gamma{}^{a}){}_{\alpha}{}^{\beta}(\gamma{}^{b}{}^{c}){}^{\gamma}{}^{\delta}(\gamma{}^{d}{}^{e}){}_{\gamma}{}_{\delta}\varepsilon{}^{j}{}^{k}\varepsilon{}_{k}{}_{j}T{}_{b}{}_{c}T{}_{d}{}_{e}\big(\mathcal D_{a}\lambda{}_{\beta}{}^{i}\big)\\
&-\frac{1}{6}\rho^{-1}(\gamma{}^{a}){}^{\beta}{}^{\gamma}(\gamma{}^{b}){}_{\beta}{}^{\delta}(\gamma{}^{c}{}^{d}){}_{\alpha}{}_{\delta}\varepsilon{}^{j}{}^{k}\varepsilon{}_{k}{}_{j}\big(\mathcal D_{b}T{}_{c}{}_{d}\big)\big(\mathcal D_{a}\lambda{}_{\gamma}{}^{i}\big) -\frac{4i}{3}\rho^{-1}(\gamma{}^{a}){}^{\beta}{}^{\gamma}(\gamma{}^{b}{}^{c}){}_{\alpha}{}_{\gamma}\big(\mathcal D_{a}\widehat F{}_{b}{}_{c}\big)\chi{}_{\beta}{}^{i}\\
&+\frac{64i}{9}\rho^{-1}(\gamma{}^{a}){}^{\beta}{}^{\gamma}(\gamma{}^{b}{}^{c}){}_{\alpha}{}_{\gamma}\big(\mathcal D_{a}\rho\big)T{}_{b}{}_{c}\chi{}_{\beta}{}^{i} +\frac{16i}{3}\rho^{-1}\big(\mathcal D_{a}Y{}_{j}{}^{i}\big)(\gamma{}^{a}){}^{\beta}{}_{\alpha}\chi{}_{\beta}{}^{j}\\
&-\frac{8}{3}\rho^{-1}(\gamma{}^{a}){}^{\beta}{}^{\gamma}(\gamma{}^{b}){}_{\alpha}{}_{\gamma}\big(\mathcal D_{a}\mathcal D_{b}\rho\big)\chi{}_{\beta}{}^{i} +\frac{4}{3}\rho^{-1}(\gamma{}^{a}){}^{\beta}{}^{\gamma}(\gamma{}_{a}){}_{\alpha}{}^{\delta}(\gamma{}^{b}{}^{c}){}_{\delta}{}^{\rho}(\gamma{}^{d}{}^{e}){}_{\rho}{}_{\gamma}\widehat F{}_{d}{}_{e}T{}_{b}{}_{c}\chi{}_{\beta}{}^{i}\\
&-\frac{4}{9}\rho^{-1}(\gamma{}^{a}){}^{\beta}{}^{\gamma}(\gamma{}_{a}){}_{\delta}{}^{\rho}(\gamma{}^{b}{}^{c}){}_{\alpha}{}^{\delta}(\gamma{}^{d}{}^{e}){}_{\rho}{}_{\gamma}\widehat F{}_{d}{}_{e}T{}_{b}{}_{c}\chi{}_{\beta}{}^{i} -\frac{64}{9}(\gamma{}^{a}){}^{\beta}{}^{\gamma}(\gamma{}_{a}){}_{\alpha}{}^{\delta}(\gamma{}^{b}{}^{c}){}_{\delta}{}^{\rho}(\gamma{}^{d}{}^{e}){}_{\rho}{}_{\gamma}T{}_{b}{}_{c}T{}_{d}{}_{e}\chi{}_{\beta}{}^{i}\\
&+\frac{64}{27}(\gamma{}^{a}){}^{\beta}{}^{\gamma}(\gamma{}_{a}){}_{\delta}{}^{\rho}(\gamma{}^{b}{}^{c}){}_{\alpha}{}^{\delta}(\gamma{}^{d}{}^{e}){}_{\rho}{}_{\gamma}T{}_{b}{}_{c}T{}_{d}{}_{e}\chi{}_{\beta}{}^{i} -\frac{16}{3}\rho^{-1}Y{}_{j}{}^{i}(\gamma{}^{a}){}^{\beta}{}_{\gamma}(\gamma{}_{a}){}_{\alpha}{}^{\delta}(\gamma{}^{b}{}^{c}){}_{\delta}{}^{\gamma}T{}_{b}{}_{c}\chi{}_{\beta}{}^{j}\\
&+\frac{16}{9}\rho^{-1}Y{}_{j}{}^{i}(\gamma{}^{a}){}^{\beta}{}_{\gamma}(\gamma{}_{a}){}_{\delta}{}^{\gamma}(\gamma{}^{b}{}^{c}){}_{\alpha}{}^{\delta}T{}_{b}{}_{c}\chi{}_{\beta}{}^{j} -\frac{8i}{3}\rho^{-1}(\gamma{}^{a}){}^{\beta}{}^{\gamma}(\gamma{}^{b}){}_{\delta}{}_{\gamma}(\gamma{}_{a}){}_{\alpha}{}^{\rho}(\gamma{}^{c}{}^{d}){}_{\rho}{}^{\delta}\big(\mathcal D_{b}\rho\big)T{}_{c}{}_{d}\chi{}_{\beta}{}^{i}\\
&+\frac{8i}{9}\rho^{-1}(\gamma{}^{a}){}^{\beta}{}^{\gamma}(\gamma{}^{b}){}_{\delta}{}_{\gamma}(\gamma{}_{a}){}_{\rho}{}^{\delta}(\gamma{}^{c}{}^{d}){}_{\alpha}{}^{\rho}\big(\mathcal D_{b}\rho\big)T{}_{c}{}_{d}\chi{}_{\beta}{}^{i} -\frac{2}{9}R(V){}_{a}{}_{b}{}_{j}{}^{i}(\gamma{}^{c}){}^{\beta}{}_{\gamma}(\gamma{}_{c}){}_{\delta}{}^{\gamma}(\gamma{}^{a}{}^{b}){}_{\alpha}{}^{\delta}\chi{}_{\beta}{}^{j}\\
&+\frac{4}{9}R(V){}_{a}{}_{b}{}_{j}{}^{i}(\gamma{}^{c}){}^{\beta}{}_{\gamma}(\gamma{}_{c}){}_{\alpha}{}^{\delta}(\gamma{}^{a}{}^{b}){}_{\delta}{}^{\gamma}\chi{}_{\beta}{}^{j} +\frac{16i}{9}(\gamma{}^{a}){}^{\beta}{}_{\gamma}(\gamma{}^{b}{}^{c}){}_{\alpha}{}^{\gamma}\big(\mathcal D_{a}T{}_{b}{}_{c}\big)\chi{}_{\beta}{}^{i}\\
&+\frac{16i}{9}(\gamma{}^{a}){}^{\beta}{}_{\gamma}(\gamma{}^{b}{}^{c}){}_{\alpha}{}^{\gamma}\big(\mathcal D_{b}T{}_{c}{}_{a}\big)\chi{}_{\beta}{}^{i} +\frac{16i}{9}(\gamma{}^{a}){}^{\beta}{}_{\gamma}(\gamma{}^{b}{}^{c}){}_{\alpha}{}^{\gamma}\big(\mathcal D_{c}T{}_{a}{}_{b}\big)\chi{}_{\beta}{}^{i}\\
&+\frac{16i}{9}(\gamma{}^{a}){}^{\beta}{}_{\gamma}(\gamma{}_{b}{}_{a}){}_{\alpha}{}^{\gamma}\big(\mathcal D_{c}T{}^{c}{}^{b}\big)\chi{}_{\beta}{}^{i} -\frac{16i}{3}(\gamma{}^{a}){}^{\beta}{}_{\alpha}\big(\mathcal D^{b}T{}_{b}{}_{a}\big)\chi{}_{\beta}{}^{i}\\
&+\frac{16}{9}(\gamma{}^{a}){}^{\beta}{}_{\gamma}(\gamma{}_{b}){}_{\alpha}{}^{\gamma}\big(\mathcal D^{c}T{}^{d}{}^{e}\big)\epsilon{}_{c}{}_{a}{}^{b}{}_{d}{}_{e}\chi{}_{\beta}{}^{i} +\frac{64i}{27}(\gamma{}^{a}){}^{\beta}{}_{\gamma}(\gamma{}_{b}{}_{a}){}_{\alpha}{}^{\gamma}T{}^{c}{}^{d}T{}_{e}{}_{f}\epsilon{}^{b}{}^{e}{}^{f}{}_{c}{}_{d}\chi{}_{\beta}{}^{i}\\
&-\frac{64i}{9}(\gamma{}^{a}){}^{\beta}{}_{\alpha}T{}^{b}{}^{c}T{}^{d}{}^{e}\epsilon{}_{a}{}_{d}{}_{e}{}_{b}{}_{c}\chi{}_{\beta}{}^{i} +\frac{1024}{27}(\gamma{}^{a}){}^{\beta}{}_{\gamma}(\gamma{}_{b}){}_{\alpha}{}^{\gamma}T{}^{b}{}^{c}T{}_{a}{}_{c}\chi{}_{\beta}{}^{i}\\
&-\frac{64}{9}(\gamma{}^{a}){}^{\beta}{}_{\gamma}(\gamma{}_{a}){}_{\alpha}{}^{\gamma}T{}^{b}{}^{c}T{}_{b}{}_{c}\chi{}_{\beta}{}^{i} -\frac{4i}{3}\rho^{-1}(\gamma{}^{a}){}^{\beta}{}^{\gamma}(\gamma{}^{b}{}^{c}){}_{\alpha}{}_{\beta}\widehat F{}_{b}{}_{c}\big(\mathcal D_{a}\chi{}_{\gamma}{}^{i}\big)\\
&+\frac{64i}{9}(\gamma{}^{a}){}^{\beta}{}^{\gamma}(\gamma{}^{b}{}^{c}){}_{\alpha}{}_{\beta}T{}_{b}{}_{c}\big(\mathcal D_{a}\chi{}_{\gamma}{}^{i}\big) +\frac{16i}{3}\rho^{-1}Y{}_{j}{}^{i}(\gamma{}^{a}){}_{\alpha}{}^{\beta}\big(\mathcal D_{a}\chi{}_{\beta}{}^{j}\big)\\
&-\frac{8}{3}\rho^{-1}(\gamma{}^{a}){}^{\beta}{}^{\gamma}(\gamma{}^{b}){}_{\alpha}{}_{\beta}\big(\mathcal D_{b}\rho\big)\big(\mathcal D_{a}\chi{}_{\gamma}{}^{i}\big) -\frac{i}{12}\rho^{-1}\big(\mathcal D_{a}R(V){}_{b}{}_{c}{}_{j}{}^{j}\big)(\gamma{}^{a}){}^{\beta}{}^{\gamma}(\gamma{}^{b}{}^{c}){}_{\alpha}{}_{\gamma}\lambda{}_{\beta}{}^{i}
\end{aligned}
\tag{S6-phi-007}
```

```math
\begin{aligned}
&+\frac{4i}{3}\rho^{-1}\big(\mathcal D_{a}D\big)(\gamma{}^{a}){}^{\beta}{}_{\alpha}\varepsilon{}^{j}{}^{k}\varepsilon{}_{k}{}_{j}\lambda{}_{\beta}{}^{i} -\frac{1}{2}\rho^{-1}(\gamma{}^{a}){}^{\beta}{}^{\gamma}(\gamma{}^{b}){}_{\alpha}{}^{\delta}(\gamma{}^{c}{}^{d}){}_{\gamma}{}_{\delta}\varepsilon{}^{j}{}^{k}\varepsilon{}_{k}{}_{j}\big(\mathcal D_{a}\mathcal D_{b}T{}_{c}{}_{d}\big)\lambda{}_{\beta}{}^{i}\\
&+\frac{8i}{9}\rho^{-1}(\gamma{}^{a}){}^{\beta}{}^{\gamma}(\gamma{}^{b}{}^{c}){}_{\alpha}{}^{\delta}(\gamma{}^{d}{}^{e}){}_{\gamma}{}_{\delta}\varepsilon{}^{j}{}^{k}\varepsilon{}_{k}{}_{j}T{}_{d}{}_{e}\big(\mathcal D_{a}T{}_{b}{}_{c}\big)\lambda{}_{\beta}{}^{i} +\frac{8i}{9}\rho^{-1}(\gamma{}^{a}){}^{\beta}{}^{\gamma}(\gamma{}^{b}{}^{c}){}_{\alpha}{}^{\delta}(\gamma{}^{d}{}^{e}){}_{\gamma}{}_{\delta}\varepsilon{}^{j}{}^{k}\varepsilon{}_{k}{}_{j}T{}_{b}{}_{c}\big(\mathcal D_{a}T{}_{d}{}_{e}\big)\lambda{}_{\beta}{}^{i}\\
&-\frac{2i}{9}\rho^{-1}(\gamma{}^{a}){}^{\beta}{}_{\alpha}(\gamma{}^{b}{}^{c}){}^{\gamma}{}^{\delta}(\gamma{}^{d}{}^{e}){}_{\gamma}{}_{\delta}\varepsilon{}^{j}{}^{k}\varepsilon{}_{k}{}_{j}T{}_{d}{}_{e}\big(\mathcal D_{a}T{}_{b}{}_{c}\big)\lambda{}_{\beta}{}^{i} -\frac{2i}{9}\rho^{-1}(\gamma{}^{a}){}^{\beta}{}_{\alpha}(\gamma{}^{b}{}^{c}){}^{\gamma}{}^{\delta}(\gamma{}^{d}{}^{e}){}_{\gamma}{}_{\delta}\varepsilon{}^{j}{}^{k}\varepsilon{}_{k}{}_{j}T{}_{b}{}_{c}\big(\mathcal D_{a}T{}_{d}{}_{e}\big)\lambda{}_{\beta}{}^{i}\\
&-\frac{1}{6}\rho^{-1}(\gamma{}^{a}){}^{\beta}{}^{\gamma}(\gamma{}^{b}){}_{\gamma}{}^{\delta}(\gamma{}^{c}{}^{d}){}_{\alpha}{}_{\delta}\varepsilon{}^{j}{}^{k}\varepsilon{}_{k}{}_{j}\big(\mathcal D_{a}\mathcal D_{b}T{}_{c}{}_{d}\big)\lambda{}_{\beta}{}^{i} +\frac{1}{12}\rho^{-1}R(V){}_{a}{}_{b}{}_{j}{}^{j}(\gamma{}^{c}){}^{\beta}{}^{\gamma}(\gamma{}_{c}){}_{\alpha}{}^{\delta}(\gamma{}^{d}{}^{e}){}_{\delta}{}^{\rho}(\gamma{}^{a}{}^{b}){}_{\rho}{}_{\gamma}T{}_{d}{}_{e}\lambda{}_{\beta}{}^{i}\\
&-\frac{1}{36}\rho^{-1}R(V){}_{a}{}_{b}{}_{j}{}^{j}(\gamma{}^{c}){}^{\beta}{}^{\gamma}(\gamma{}_{c}){}_{\delta}{}^{\rho}(\gamma{}^{d}{}^{e}){}_{\alpha}{}^{\delta}(\gamma{}^{a}{}^{b}){}_{\rho}{}_{\gamma}T{}_{d}{}_{e}\lambda{}_{\beta}{}^{i} -\frac{4}{3}\rho^{-1}D(\gamma{}^{a}){}^{\beta}{}_{\gamma}(\gamma{}_{a}){}_{\alpha}{}^{\delta}(\gamma{}^{b}{}^{c}){}_{\delta}{}^{\gamma}\varepsilon{}^{j}{}^{k}\varepsilon{}_{k}{}_{j}T{}_{b}{}_{c}\lambda{}_{\beta}{}^{i}\\
&+\frac{4}{9}\rho^{-1}D(\gamma{}^{a}){}^{\beta}{}_{\gamma}(\gamma{}_{a}){}_{\delta}{}^{\gamma}(\gamma{}^{b}{}^{c}){}_{\alpha}{}^{\delta}\varepsilon{}^{j}{}^{k}\varepsilon{}_{k}{}_{j}T{}_{b}{}_{c}\lambda{}_{\beta}{}^{i} -\frac{i}{2}\rho^{-1}(\gamma{}^{a}){}^{\beta}{}^{\gamma}(\gamma{}^{b}){}_{\delta}{}^{\rho}(\gamma{}_{a}){}_{\alpha}{}^{\sigma}(\gamma{}^{c}{}^{d}){}_{\sigma}{}^{\delta}(\gamma{}^{e}{}^{f}){}_{\gamma}{}_{\rho}\varepsilon{}^{j}{}^{k}\varepsilon{}_{k}{}_{j}T{}_{c}{}_{d}\big(\mathcal D_{b}T{}_{e}{}_{f}\big)\lambda{}_{\beta}{}^{i}\\
&+\frac{i}{6}\rho^{-1}(\gamma{}^{a}){}^{\beta}{}^{\gamma}(\gamma{}^{b}){}_{\delta}{}^{\rho}(\gamma{}_{a}){}_{\sigma}{}^{\delta}(\gamma{}^{c}{}^{d}){}_{\alpha}{}^{\sigma}(\gamma{}^{e}{}^{f}){}_{\gamma}{}_{\rho}\varepsilon{}^{j}{}^{k}\varepsilon{}_{k}{}_{j}T{}_{c}{}_{d}\big(\mathcal D_{b}T{}_{e}{}_{f}\big)\lambda{}_{\beta}{}^{i} -\frac{8}{9}\rho^{-1}(\gamma{}^{a}){}^{\beta}{}^{\gamma}(\gamma{}_{a}){}_{\alpha}{}^{\delta}(\gamma{}^{b}{}^{c}){}_{\delta}{}^{\rho}(\gamma{}^{d}{}^{e}){}_{\rho}{}^{\sigma}(\gamma{}^{f}{}^{g}){}_{\gamma}{}_{\sigma}\varepsilon{}^{j}{}^{k}\varepsilon{}_{k}{}_{j}T{}_{b}{}_{c}T{}_{d}{}_{e}T{}_{f}{}_{g}\lambda{}_{\beta}{}^{i}\\
&+\frac{8}{27}\rho^{-1}(\gamma{}^{a}){}^{\beta}{}^{\gamma}(\gamma{}_{a}){}_{\delta}{}^{\rho}(\gamma{}^{b}{}^{c}){}_{\alpha}{}^{\delta}(\gamma{}^{d}{}^{e}){}_{\rho}{}^{\sigma}(\gamma{}^{f}{}^{g}){}_{\gamma}{}_{\sigma}\varepsilon{}^{j}{}^{k}\varepsilon{}_{k}{}_{j}T{}_{b}{}_{c}T{}_{d}{}_{e}T{}_{f}{}_{g}\lambda{}_{\beta}{}^{i} +\frac{2}{9}\rho^{-1}(\gamma{}^{a}){}^{\beta}{}_{\gamma}(\gamma{}_{a}){}_{\alpha}{}^{\delta}(\gamma{}^{b}{}^{c}){}^{\rho}{}^{\sigma}(\gamma{}^{d}{}^{e}){}_{\delta}{}^{\gamma}(\gamma{}^{f}{}^{g}){}_{\rho}{}_{\sigma}\varepsilon{}^{j}{}^{k}\varepsilon{}_{k}{}_{j}T{}_{d}{}_{e}T{}_{b}{}_{c}T{}_{f}{}_{g}\lambda{}_{\beta}{}^{i}\\
&-\frac{2}{27}\rho^{-1}(\gamma{}^{a}){}^{\beta}{}_{\gamma}(\gamma{}_{a}){}_{\delta}{}^{\gamma}(\gamma{}^{b}{}^{c}){}^{\rho}{}^{\sigma}(\gamma{}^{d}{}^{e}){}_{\alpha}{}^{\delta}(\gamma{}^{f}{}^{g}){}_{\rho}{}_{\sigma}\varepsilon{}^{j}{}^{k}\varepsilon{}_{k}{}_{j}T{}_{d}{}_{e}T{}_{b}{}_{c}T{}_{f}{}_{g}\lambda{}_{\beta}{}^{i} -\frac{i}{6}\rho^{-1}(\gamma{}^{a}){}^{\beta}{}^{\gamma}(\gamma{}^{b}){}_{\gamma}{}^{\delta}(\gamma{}_{a}){}_{\alpha}{}^{\rho}(\gamma{}^{c}{}^{d}){}_{\rho}{}^{\sigma}(\gamma{}^{e}{}^{f}){}_{\sigma}{}_{\delta}\varepsilon{}^{j}{}^{k}\varepsilon{}_{k}{}_{j}T{}_{c}{}_{d}\big(\mathcal D_{b}T{}_{e}{}_{f}\big)\lambda{}_{\beta}{}^{i}\\
&+\frac{i}{18}\rho^{-1}(\gamma{}^{a}){}^{\beta}{}^{\gamma}(\gamma{}^{b}){}_{\gamma}{}^{\delta}(\gamma{}_{a}){}_{\rho}{}^{\sigma}(\gamma{}^{c}{}^{d}){}_{\alpha}{}^{\rho}(\gamma{}^{e}{}^{f}){}_{\sigma}{}_{\delta}\varepsilon{}^{j}{}^{k}\varepsilon{}_{k}{}_{j}T{}_{c}{}_{d}\big(\mathcal D_{b}T{}_{e}{}_{f}\big)\lambda{}_{\beta}{}^{i} +\frac{1}{18}\rho^{-1}R(V){}_{a}{}_{b}{}_{j}{}^{j}(\gamma{}^{c}){}^{\beta}{}^{\gamma}(\gamma{}_{c}){}_{\delta}{}^{\rho}(\gamma{}^{a}{}^{b}){}_{\alpha}{}^{\delta}(\gamma{}^{d}{}^{e}){}_{\rho}{}_{\gamma}T{}_{d}{}_{e}\lambda{}_{\beta}{}^{i}\\
&-\frac{1}{9}\rho^{-1}R(V){}_{a}{}_{b}{}_{j}{}^{j}(\gamma{}^{c}){}^{\beta}{}^{\gamma}(\gamma{}_{c}){}_{\alpha}{}^{\delta}(\gamma{}^{a}{}^{b}){}_{\delta}{}^{\rho}(\gamma{}^{d}{}^{e}){}_{\rho}{}_{\gamma}T{}_{d}{}_{e}\lambda{}_{\beta}{}^{i} +\frac{4i}{9}\rho^{-1}\delta{}^{j}{}_{k}(\gamma{}^{a}){}^{\beta}{}^{\gamma}(\gamma{}^{b}{}^{c}){}_{\alpha}{}^{\delta}(\gamma{}^{d}{}^{e}){}_{\delta}{}_{\gamma}\varepsilon{}^{l}{}^{k}\varepsilon{}_{j}{}_{l}T{}_{d}{}_{e}\big(\mathcal D_{a}T{}_{b}{}_{c}\big)\lambda{}_{\beta}{}^{i}\\
&+\frac{4i}{9}\rho^{-1}\delta{}^{j}{}_{k}(\gamma{}^{a}){}^{\beta}{}^{\gamma}(\gamma{}^{b}{}^{c}){}_{\alpha}{}^{\delta}(\gamma{}^{d}{}^{e}){}_{\delta}{}_{\gamma}\varepsilon{}^{l}{}^{k}\varepsilon{}_{j}{}_{l}T{}_{d}{}_{e}\big(\mathcal D_{b}T{}_{c}{}_{a}\big)\lambda{}_{\beta}{}^{i} +\frac{4i}{9}\rho^{-1}\delta{}^{j}{}_{k}(\gamma{}^{a}){}^{\beta}{}^{\gamma}(\gamma{}^{b}{}^{c}){}_{\alpha}{}^{\delta}(\gamma{}^{d}{}^{e}){}_{\delta}{}_{\gamma}\varepsilon{}^{l}{}^{k}\varepsilon{}_{j}{}_{l}T{}_{d}{}_{e}\big(\mathcal D_{c}T{}_{a}{}_{b}\big)\lambda{}_{\beta}{}^{i}\\
&+\frac{4i}{9}\rho^{-1}\delta{}^{j}{}_{k}(\gamma{}^{a}){}^{\beta}{}^{\gamma}(\gamma{}^{b}{}^{c}){}_{\delta}{}_{\gamma}(\gamma{}_{d}{}_{a}){}_{\alpha}{}^{\delta}\varepsilon{}^{l}{}^{k}\varepsilon{}_{j}{}_{l}T{}_{b}{}_{c}\big(\mathcal D_{e}T{}^{e}{}^{d}\big)\lambda{}_{\beta}{}^{i} -\frac{4i}{3}\rho^{-1}\delta{}^{j}{}_{k}(\gamma{}^{a}){}^{\beta}{}^{\gamma}(\gamma{}^{b}{}^{c}){}_{\alpha}{}_{\gamma}\varepsilon{}^{l}{}^{k}\varepsilon{}_{j}{}_{l}T{}_{b}{}_{c}\big(\mathcal D^{d}T{}_{d}{}_{a}\big)\lambda{}_{\beta}{}^{i}\\
&+\frac{4}{9}\rho^{-1}\delta{}^{j}{}_{k}(\gamma{}^{a}){}^{\beta}{}^{\gamma}(\gamma{}_{b}){}_{\alpha}{}^{\delta}(\gamma{}^{c}{}^{d}){}_{\delta}{}_{\gamma}\varepsilon{}^{l}{}^{k}\varepsilon{}_{j}{}_{l}T{}_{c}{}_{d}\big(\mathcal D^{e}T{}^{f}{}^{g}\big)\epsilon{}_{e}{}_{a}{}^{b}{}_{f}{}_{g}\lambda{}_{\beta}{}^{i} +\frac{16i}{27}\rho^{-1}\delta{}^{j}{}_{k}(\gamma{}^{a}){}^{\beta}{}^{\gamma}(\gamma{}^{b}{}^{c}){}_{\delta}{}_{\gamma}(\gamma{}_{d}{}_{a}){}_{\alpha}{}^{\delta}\varepsilon{}^{l}{}^{k}\varepsilon{}_{j}{}_{l}T{}^{e}{}^{f}T{}_{g}{}_{h}T{}_{b}{}_{c}\epsilon{}^{d}{}^{g}{}^{h}{}_{e}{}_{f}\lambda{}_{\beta}{}^{i}\\
&-\frac{16i}{9}\rho^{-1}\delta{}^{j}{}_{k}(\gamma{}^{a}){}^{\beta}{}^{\gamma}(\gamma{}^{b}{}^{c}){}_{\alpha}{}_{\gamma}\varepsilon{}^{l}{}^{k}\varepsilon{}_{j}{}_{l}T{}^{d}{}^{e}T{}^{f}{}^{g}T{}_{b}{}_{c}\epsilon{}_{a}{}_{f}{}_{g}{}_{d}{}_{e}\lambda{}_{\beta}{}^{i} +\frac{256}{27}\rho^{-1}\delta{}^{j}{}_{k}(\gamma{}^{a}){}^{\beta}{}^{\gamma}(\gamma{}_{b}){}_{\alpha}{}^{\delta}(\gamma{}^{c}{}^{d}){}_{\delta}{}_{\gamma}\varepsilon{}^{l}{}^{k}\varepsilon{}_{j}{}_{l}T{}^{b}{}^{e}T{}_{a}{}_{e}T{}_{c}{}_{d}\lambda{}_{\beta}{}^{i}\\
&-\frac{16}{9}\rho^{-1}\delta{}^{j}{}_{k}(\gamma{}^{a}){}^{\beta}{}^{\gamma}(\gamma{}_{a}){}_{\alpha}{}^{\delta}(\gamma{}^{b}{}^{c}){}_{\delta}{}_{\gamma}\varepsilon{}^{l}{}^{k}\varepsilon{}_{j}{}_{l}T{}^{d}{}^{e}T{}_{d}{}_{e}T{}_{b}{}_{c}\lambda{}_{\beta}{}^{i} +\frac{4i}{3}\rho^{-1}(\gamma{}^{a}){}^{\beta}{}^{\gamma}(\gamma{}^{b}{}^{c}){}_{\alpha}{}_{\beta}\widehat F{}_{b}{}_{c}\varepsilon{}^{j}{}^{k}\varepsilon{}_{k}{}_{j}\big(\mathcal D_{a}\chi{}_{\gamma}{}^{i}\big)\\
&-\frac{64i}{9}(\gamma{}^{a}){}^{\beta}{}^{\gamma}(\gamma{}^{b}{}^{c}){}_{\alpha}{}_{\beta}\varepsilon{}^{j}{}^{k}\varepsilon{}_{k}{}_{j}T{}_{b}{}_{c}\big(\mathcal D_{a}\chi{}_{\gamma}{}^{i}\big) +\frac{16i}{3}\rho^{-1}Y{}_{j}{}^{j}(\gamma{}^{a}){}_{\alpha}{}^{\beta}\big(\mathcal D_{a}\chi{}_{\beta}{}^{i}\big)\\
&+\frac{8}{3}\rho^{-1}(\gamma{}^{a}){}^{\beta}{}^{\gamma}(\gamma{}^{b}){}_{\alpha}{}_{\beta}\big(\mathcal D_{b}\rho\big)\varepsilon{}^{j}{}^{k}\varepsilon{}_{k}{}_{j}\big(\mathcal D_{a}\chi{}_{\gamma}{}^{i}\big) -\frac{i}{12}\rho^{-1}\big(\mathcal D_{a}R(V){}_{b}{}_{c}{}_{j}{}^{i}\big)(\gamma{}^{a}){}^{\beta}{}^{\gamma}(\gamma{}^{b}{}^{c}){}_{\alpha}{}_{\gamma}\lambda{}_{\beta}{}^{j}\\
&-\frac{4i}{3}\rho^{-1}\big(\mathcal D_{a}D\big)(\gamma{}^{a}){}^{\beta}{}_{\alpha}\lambda{}_{\beta}{}^{i} +\frac{1}{2}\rho^{-1}(\gamma{}^{a}){}^{\beta}{}^{\gamma}(\gamma{}^{b}){}_{\alpha}{}^{\delta}(\gamma{}^{c}{}^{d}){}_{\gamma}{}_{\delta}\big(\mathcal D_{a}\mathcal D_{b}T{}_{c}{}_{d}\big)\lambda{}_{\beta}{}^{i}\\
&-\frac{8i}{9}\rho^{-1}(\gamma{}^{a}){}^{\beta}{}^{\gamma}(\gamma{}^{b}{}^{c}){}_{\alpha}{}^{\delta}(\gamma{}^{d}{}^{e}){}_{\gamma}{}_{\delta}T{}_{d}{}_{e}\big(\mathcal D_{a}T{}_{b}{}_{c}\big)\lambda{}_{\beta}{}^{i} -\frac{8i}{9}\rho^{-1}(\gamma{}^{a}){}^{\beta}{}^{\gamma}(\gamma{}^{b}{}^{c}){}_{\alpha}{}^{\delta}(\gamma{}^{d}{}^{e}){}_{\gamma}{}_{\delta}T{}_{b}{}_{c}\big(\mathcal D_{a}T{}_{d}{}_{e}\big)\lambda{}_{\beta}{}^{i}\\
&+\frac{2i}{9}\rho^{-1}(\gamma{}^{a}){}^{\beta}{}_{\alpha}(\gamma{}^{b}{}^{c}){}^{\gamma}{}^{\delta}(\gamma{}^{d}{}^{e}){}_{\gamma}{}_{\delta}T{}_{d}{}_{e}\big(\mathcal D_{a}T{}_{b}{}_{c}\big)\lambda{}_{\beta}{}^{i} +\frac{2i}{9}\rho^{-1}(\gamma{}^{a}){}^{\beta}{}_{\alpha}(\gamma{}^{b}{}^{c}){}^{\gamma}{}^{\delta}(\gamma{}^{d}{}^{e}){}_{\gamma}{}_{\delta}T{}_{b}{}_{c}\big(\mathcal D_{a}T{}_{d}{}_{e}\big)\lambda{}_{\beta}{}^{i}\\
&+\frac{1}{6}\rho^{-1}(\gamma{}^{a}){}^{\beta}{}^{\gamma}(\gamma{}^{b}){}_{\gamma}{}^{\delta}(\gamma{}^{c}{}^{d}){}_{\alpha}{}_{\delta}\big(\mathcal D_{a}\mathcal D_{b}T{}_{c}{}_{d}\big)\lambda{}_{\beta}{}^{i} +\frac{1}{12}\rho^{-1}R(V){}_{a}{}_{b}{}_{j}{}^{i}(\gamma{}^{c}){}^{\beta}{}^{\gamma}(\gamma{}_{c}){}_{\alpha}{}^{\delta}(\gamma{}^{d}{}^{e}){}_{\delta}{}^{\rho}(\gamma{}^{a}{}^{b}){}_{\rho}{}_{\gamma}T{}_{d}{}_{e}\lambda{}_{\beta}{}^{j}\\
&-\frac{1}{36}\rho^{-1}R(V){}_{a}{}_{b}{}_{j}{}^{i}(\gamma{}^{c}){}^{\beta}{}^{\gamma}(\gamma{}_{c}){}_{\delta}{}^{\rho}(\gamma{}^{d}{}^{e}){}_{\alpha}{}^{\delta}(\gamma{}^{a}{}^{b}){}_{\rho}{}_{\gamma}T{}_{d}{}_{e}\lambda{}_{\beta}{}^{j} +\frac{4}{3}\rho^{-1}D(\gamma{}^{a}){}^{\beta}{}_{\gamma}(\gamma{}_{a}){}_{\alpha}{}^{\delta}(\gamma{}^{b}{}^{c}){}_{\delta}{}^{\gamma}T{}_{b}{}_{c}\lambda{}_{\beta}{}^{i}\\
&-\frac{4}{9}\rho^{-1}D(\gamma{}^{a}){}^{\beta}{}_{\gamma}(\gamma{}_{a}){}_{\delta}{}^{\gamma}(\gamma{}^{b}{}^{c}){}_{\alpha}{}^{\delta}T{}_{b}{}_{c}\lambda{}_{\beta}{}^{i} +\frac{i}{2}\rho^{-1}(\gamma{}^{a}){}^{\beta}{}^{\gamma}(\gamma{}^{b}){}_{\delta}{}^{\rho}(\gamma{}_{a}){}_{\alpha}{}^{\sigma}(\gamma{}^{c}{}^{d}){}_{\sigma}{}^{\delta}(\gamma{}^{e}{}^{f}){}_{\gamma}{}_{\rho}T{}_{c}{}_{d}\big(\mathcal D_{b}T{}_{e}{}_{f}\big)\lambda{}_{\beta}{}^{i}\\
&-\frac{i}{6}\rho^{-1}(\gamma{}^{a}){}^{\beta}{}^{\gamma}(\gamma{}^{b}){}_{\delta}{}^{\rho}(\gamma{}_{a}){}_{\sigma}{}^{\delta}(\gamma{}^{c}{}^{d}){}_{\alpha}{}^{\sigma}(\gamma{}^{e}{}^{f}){}_{\gamma}{}_{\rho}T{}_{c}{}_{d}\big(\mathcal D_{b}T{}_{e}{}_{f}\big)\lambda{}_{\beta}{}^{i} +\frac{8}{9}\rho^{-1}(\gamma{}^{a}){}^{\beta}{}^{\gamma}(\gamma{}_{a}){}_{\alpha}{}^{\delta}(\gamma{}^{b}{}^{c}){}_{\delta}{}^{\rho}(\gamma{}^{d}{}^{e}){}_{\rho}{}^{\sigma}(\gamma{}^{f}{}^{g}){}_{\gamma}{}_{\sigma}T{}_{b}{}_{c}T{}_{d}{}_{e}T{}_{f}{}_{g}\lambda{}_{\beta}{}^{i}\\
&-\frac{8}{27}\rho^{-1}(\gamma{}^{a}){}^{\beta}{}^{\gamma}(\gamma{}_{a}){}_{\delta}{}^{\rho}(\gamma{}^{b}{}^{c}){}_{\alpha}{}^{\delta}(\gamma{}^{d}{}^{e}){}_{\rho}{}^{\sigma}(\gamma{}^{f}{}^{g}){}_{\gamma}{}_{\sigma}T{}_{b}{}_{c}T{}_{d}{}_{e}T{}_{f}{}_{g}\lambda{}_{\beta}{}^{i} -\frac{2}{9}\rho^{-1}(\gamma{}^{a}){}^{\beta}{}_{\gamma}(\gamma{}_{a}){}_{\alpha}{}^{\delta}(\gamma{}^{b}{}^{c}){}^{\rho}{}^{\sigma}(\gamma{}^{d}{}^{e}){}_{\delta}{}^{\gamma}(\gamma{}^{f}{}^{g}){}_{\rho}{}_{\sigma}T{}_{d}{}_{e}T{}_{b}{}_{c}T{}_{f}{}_{g}\lambda{}_{\beta}{}^{i}\\
&+\frac{2}{27}\rho^{-1}(\gamma{}^{a}){}^{\beta}{}_{\gamma}(\gamma{}_{a}){}_{\delta}{}^{\gamma}(\gamma{}^{b}{}^{c}){}^{\rho}{}^{\sigma}(\gamma{}^{d}{}^{e}){}_{\alpha}{}^{\delta}(\gamma{}^{f}{}^{g}){}_{\rho}{}_{\sigma}T{}_{d}{}_{e}T{}_{b}{}_{c}T{}_{f}{}_{g}\lambda{}_{\beta}{}^{i} +\frac{i}{6}\rho^{-1}(\gamma{}^{a}){}^{\beta}{}^{\gamma}(\gamma{}^{b}){}_{\gamma}{}^{\delta}(\gamma{}_{a}){}_{\alpha}{}^{\rho}(\gamma{}^{c}{}^{d}){}_{\rho}{}^{\sigma}(\gamma{}^{e}{}^{f}){}_{\sigma}{}_{\delta}T{}_{c}{}_{d}\big(\mathcal D_{b}T{}_{e}{}_{f}\big)\lambda{}_{\beta}{}^{i}\\
&-\frac{i}{18}\rho^{-1}(\gamma{}^{a}){}^{\beta}{}^{\gamma}(\gamma{}^{b}){}_{\gamma}{}^{\delta}(\gamma{}_{a}){}_{\rho}{}^{\sigma}(\gamma{}^{c}{}^{d}){}_{\alpha}{}^{\rho}(\gamma{}^{e}{}^{f}){}_{\sigma}{}_{\delta}T{}_{c}{}_{d}\big(\mathcal D_{b}T{}_{e}{}_{f}\big)\lambda{}_{\beta}{}^{i} +\frac{1}{18}\rho^{-1}R(V){}_{a}{}_{b}{}_{j}{}^{i}(\gamma{}^{c}){}^{\beta}{}^{\gamma}(\gamma{}_{c}){}_{\delta}{}^{\rho}(\gamma{}^{a}{}^{b}){}_{\alpha}{}^{\delta}(\gamma{}^{d}{}^{e}){}_{\rho}{}_{\gamma}T{}_{d}{}_{e}\lambda{}_{\beta}{}^{j}\\
&-\frac{1}{9}\rho^{-1}R(V){}_{a}{}_{b}{}_{j}{}^{i}(\gamma{}^{c}){}^{\beta}{}^{\gamma}(\gamma{}_{c}){}_{\alpha}{}^{\delta}(\gamma{}^{a}{}^{b}){}_{\delta}{}^{\rho}(\gamma{}^{d}{}^{e}){}_{\rho}{}_{\gamma}T{}_{d}{}_{e}\lambda{}_{\beta}{}^{j} -\frac{4i}{9}\rho^{-1}(\gamma{}^{a}){}^{\beta}{}^{\gamma}(\gamma{}^{b}{}^{c}){}_{\alpha}{}^{\delta}(\gamma{}^{d}{}^{e}){}_{\delta}{}_{\gamma}T{}_{d}{}_{e}\big(\mathcal D_{a}T{}_{b}{}_{c}\big)\lambda{}_{\beta}{}^{i}\\
&-\frac{4i}{9}\rho^{-1}(\gamma{}^{a}){}^{\beta}{}^{\gamma}(\gamma{}^{b}{}^{c}){}_{\alpha}{}^{\delta}(\gamma{}^{d}{}^{e}){}_{\delta}{}_{\gamma}T{}_{d}{}_{e}\big(\mathcal D_{b}T{}_{c}{}_{a}\big)\lambda{}_{\beta}{}^{i} -\frac{4i}{9}\rho^{-1}(\gamma{}^{a}){}^{\beta}{}^{\gamma}(\gamma{}^{b}{}^{c}){}_{\alpha}{}^{\delta}(\gamma{}^{d}{}^{e}){}_{\delta}{}_{\gamma}T{}_{d}{}_{e}\big(\mathcal D_{c}T{}_{a}{}_{b}\big)\lambda{}_{\beta}{}^{i}\\
&-\frac{4i}{9}\rho^{-1}(\gamma{}^{a}){}^{\beta}{}^{\gamma}(\gamma{}^{b}{}^{c}){}_{\delta}{}_{\gamma}(\gamma{}_{d}{}_{a}){}_{\alpha}{}^{\delta}T{}_{b}{}_{c}\big(\mathcal D_{e}T{}^{e}{}^{d}\big)\lambda{}_{\beta}{}^{i} +\frac{4i}{3}\rho^{-1}(\gamma{}^{a}){}^{\beta}{}^{\gamma}(\gamma{}^{b}{}^{c}){}_{\alpha}{}_{\gamma}T{}_{b}{}_{c}\big(\mathcal D^{d}T{}_{d}{}_{a}\big)\lambda{}_{\beta}{}^{i}\\
&-\frac{4}{9}\rho^{-1}(\gamma{}^{a}){}^{\beta}{}^{\gamma}(\gamma{}_{b}){}_{\alpha}{}^{\delta}(\gamma{}^{c}{}^{d}){}_{\delta}{}_{\gamma}T{}_{c}{}_{d}\big(\mathcal D^{e}T{}^{f}{}^{g}\big)\epsilon{}_{e}{}_{a}{}^{b}{}_{f}{}_{g}\lambda{}_{\beta}{}^{i} -\frac{16i}{27}\rho^{-1}(\gamma{}^{a}){}^{\beta}{}^{\gamma}(\gamma{}^{b}{}^{c}){}_{\delta}{}_{\gamma}(\gamma{}_{d}{}_{a}){}_{\alpha}{}^{\delta}T{}^{e}{}^{f}T{}_{g}{}_{h}T{}_{b}{}_{c}\epsilon{}^{d}{}^{g}{}^{h}{}_{e}{}_{f}\lambda{}_{\beta}{}^{i}\\
&+\frac{16i}{9}\rho^{-1}(\gamma{}^{a}){}^{\beta}{}^{\gamma}(\gamma{}^{b}{}^{c}){}_{\alpha}{}_{\gamma}T{}^{d}{}^{e}T{}^{f}{}^{g}T{}_{b}{}_{c}\epsilon{}_{a}{}_{f}{}_{g}{}_{d}{}_{e}\lambda{}_{\beta}{}^{i} -\frac{256}{27}\rho^{-1}(\gamma{}^{a}){}^{\beta}{}^{\gamma}(\gamma{}_{b}){}_{\alpha}{}^{\delta}(\gamma{}^{c}{}^{d}){}_{\delta}{}_{\gamma}T{}^{b}{}^{e}T{}_{a}{}_{e}T{}_{c}{}_{d}\lambda{}_{\beta}{}^{i}\\
&+\frac{16}{9}\rho^{-1}(\gamma{}^{a}){}^{\beta}{}^{\gamma}(\gamma{}_{a}){}_{\alpha}{}^{\delta}(\gamma{}^{b}{}^{c}){}_{\delta}{}_{\gamma}T{}^{d}{}^{e}T{}_{d}{}_{e}T{}_{b}{}_{c}\lambda{}_{\beta}{}^{i} +\frac{4}{3}\rho^{-3}Y{}^{i}{}^{j}\big(\mathcal D^{a}\mathcal D_{a}\rho\big)\lambda{}_{\alpha}{}_{j}\\
&-\frac{i}{3}\rho^{-2}(\gamma{}^{a}){}_{\alpha}{}^{\beta}\big(\mathcal D^{b}\mathcal D_{b}\rho\big)\big(\mathcal D_{a}\lambda{}_{\beta}{}^{i}\big) +\frac{2}{3}\rho^{-2}(\gamma{}^{a}{}^{b}){}_{\alpha}{}_{\beta}\big(\mathcal D^{c}\mathcal D_{c}\rho\big)T{}_{a}{}_{b}\lambda{}^{\beta}{}^{i}\\
&+\frac{i}{3}\rho^{-2}(\gamma{}^{a}){}_{\alpha}{}^{\beta}\big(\mathcal D^{b}\mathcal D_{b}\rho\big)\varepsilon{}^{j}{}^{k}\varepsilon{}_{k}{}_{j}\big(\mathcal D_{a}\lambda{}_{\beta}{}^{i}\big) -\frac{2}{9}\rho^{-2}(\gamma{}^{a}{}^{b}){}_{\alpha}{}_{\beta}\big(\mathcal D^{c}\mathcal D_{c}\rho\big)\varepsilon{}^{j}{}^{k}\varepsilon{}_{k}{}_{j}T{}_{a}{}_{b}\lambda{}^{\beta}{}^{i}\\
&-\frac{2}{3}\rho^{-2}Y{}^{i}{}^{j}\big(\mathcal D^{a}\mathcal D_{a}\lambda{}_{\alpha}{}_{j}\big) -\frac{2i}{3}\rho^{-2}Y{}^{i}{}^{j}(\gamma{}_{a}){}_{\alpha}{}^{\beta}(\gamma{}^{b}{}^{c}){}_{\beta}{}^{\gamma}\big(\mathcal D^{a}T{}_{b}{}_{c}\big)\lambda{}_{\gamma}{}_{j}\\
&-\frac{2i}{3}\rho^{-2}Y{}^{i}{}^{j}(\gamma{}_{a}){}_{\alpha}{}^{\beta}(\gamma{}^{b}{}^{c}){}_{\beta}{}^{\gamma}T{}_{b}{}_{c}\big(\mathcal D^{a}\lambda{}_{\gamma}{}_{j}\big) +\frac{2i}{9}\rho^{-2}Y{}^{i}{}^{j}(\gamma{}_{a}){}_{\beta}{}^{\gamma}(\gamma{}^{b}{}^{c}){}_{\alpha}{}^{\beta}T{}_{b}{}_{c}\big(\mathcal D^{a}\lambda{}_{\gamma}{}_{j}\big)\\
&+\frac{56i}{9}\rho^{-2}Y{}^{i}{}^{j}(\gamma{}_{a}){}_{\alpha}{}^{\beta}\big(\mathcal D^{a}\rho\big)\chi{}_{\beta}{}_{j} -\frac{2i}{3}\rho^{-2}Y{}^{i}{}^{j}(\gamma{}^{a}){}_{\alpha}{}^{\beta}(\gamma{}^{b}{}^{c}){}_{\beta}{}^{\gamma}T{}_{b}{}_{c}\big(\mathcal D_{a}\lambda{}_{\gamma}{}_{j}\big)\\
&+\frac{2i}{9}\rho^{-2}Y{}^{i}{}^{j}(\gamma{}^{a}){}_{\beta}{}^{\gamma}(\gamma{}^{b}{}^{c}){}_{\alpha}{}^{\beta}T{}_{b}{}_{c}\big(\mathcal D_{a}\lambda{}_{\gamma}{}_{j}\big) +\frac{2}{3}\rho^{-2}Y{}^{i}{}^{j}(\gamma{}^{a}){}_{\alpha}{}^{\beta}(\gamma{}_{a}){}_{\gamma}{}^{\delta}(\gamma{}^{b}{}^{c}){}_{\beta}{}^{\gamma}(\gamma{}^{d}{}^{e}){}_{\delta}{}^{\rho}T{}_{b}{}_{c}T{}_{d}{}_{e}\lambda{}_{\rho}{}_{j}
\end{aligned}
\tag{S6-phi-008}
```

```math
\begin{aligned}
&-\frac{2}{9}\rho^{-2}Y{}^{i}{}^{j}(\gamma{}^{a}){}_{\alpha}{}^{\beta}(\gamma{}_{a}){}_{\gamma}{}^{\delta}(\gamma{}^{b}{}^{c}){}_{\beta}{}^{\rho}(\gamma{}^{d}{}^{e}){}_{\rho}{}^{\gamma}T{}_{b}{}_{c}T{}_{d}{}_{e}\lambda{}_{\delta}{}_{j} -\frac{2}{9}\rho^{-2}Y{}^{i}{}^{j}(\gamma{}^{a}){}_{\beta}{}^{\gamma}(\gamma{}_{a}){}_{\gamma}{}^{\delta}(\gamma{}^{b}{}^{c}){}_{\alpha}{}^{\beta}(\gamma{}^{d}{}^{e}){}_{\delta}{}^{\rho}T{}_{b}{}_{c}T{}_{d}{}_{e}\lambda{}_{\rho}{}_{j}\\
&+\frac{2}{27}\rho^{-2}Y{}^{i}{}^{j}(\gamma{}^{a}){}_{\beta}{}^{\gamma}(\gamma{}_{a}){}_{\delta}{}^{\rho}(\gamma{}^{b}{}^{c}){}_{\alpha}{}^{\beta}(\gamma{}^{d}{}^{e}){}_{\gamma}{}^{\delta}T{}_{b}{}_{c}T{}_{d}{}_{e}\lambda{}_{\rho}{}_{j} -\frac{i}{3}\rho^{-2}Y{}^{i}{}^{j}(\gamma{}^{a}){}_{\alpha}{}^{\beta}\big(\mathcal D_{b}\rho\big)R(Q){}_{a}{}^{b}{}_{\beta}{}_{j}\\
&+\frac{1}{12}\rho^{-2}Y{}^{i}{}^{j}\big(\mathcal D_{a}\rho\big)\epsilon{}^{b}{}_{b}{}^{a}{}^{c}{}^{d}R(Q){}_{c}{}_{d}{}_{\alpha}{}_{j} -\frac{16i}{9}\rho^{-2}Y{}^{i}{}^{j}\delta{}_{a}{}^{b}\eta{}^{c}{}^{a}\eta{}_{c}{}_{b}(\gamma{}^{d}){}_{\alpha}{}^{\beta}\big(\mathcal D_{d}\rho\big)\chi{}_{\beta}{}_{j}\\
&+\frac{i}{3}\rho^{-2}Y{}^{i}{}^{j}(\gamma{}^{a}){}_{\alpha}{}^{\beta}\big(\mathcal D_{b}\rho\big)R(Q){}^{b}{}_{a}{}_{\beta}{}_{j} -\frac{1}{12}\rho^{-2}Y{}^{i}{}^{j}\big(\mathcal D_{a}\rho\big)\epsilon{}^{b}{}^{a}{}_{b}{}^{c}{}^{d}R(Q){}_{c}{}_{d}{}_{\alpha}{}_{j}\\
&+\frac{8i}{3}\rho^{-2}Y{}^{i}{}^{j}(\gamma{}^{a}){}_{\alpha}{}^{\beta}\big(\mathcal D_{a}\rho\big)\chi{}_{\beta}{}_{j} +\frac{1}{36}\rho^{-2}R(V){}_{a}{}_{b}{}_{j}{}^{k}Y{}^{i}{}^{j}(\gamma{}^{c}){}_{\beta}{}^{\gamma}(\gamma{}_{c}){}_{\gamma}{}^{\delta}(\gamma{}^{a}{}^{b}){}_{\alpha}{}^{\beta}\lambda{}_{\delta}{}_{k}\\
&-\frac{1}{18}\rho^{-2}R(V){}_{a}{}_{b}{}_{j}{}^{k}Y{}^{i}{}^{j}(\gamma{}^{c}){}_{\alpha}{}^{\beta}(\gamma{}_{c}){}_{\gamma}{}^{\delta}(\gamma{}^{a}{}^{b}){}_{\beta}{}^{\gamma}\lambda{}_{\delta}{}_{k} -\frac{2i}{9}\rho^{-2}Y{}^{i}{}^{j}(\gamma{}_{a}){}_{\beta}{}^{\gamma}(\gamma{}^{b}{}^{c}){}_{\alpha}{}^{\beta}\big(\mathcal D_{b}T{}_{c}{}^{a}\big)\lambda{}_{\gamma}{}_{j}\\
&-\frac{2i}{9}\rho^{-2}Y{}^{i}{}^{j}(\gamma{}_{a}){}_{\beta}{}^{\gamma}(\gamma{}^{b}{}^{c}){}_{\alpha}{}^{\beta}\big(\mathcal D_{c}T{}^{a}{}_{b}\big)\lambda{}_{\gamma}{}_{j} -\frac{2i}{9}\rho^{-2}Y{}^{i}{}^{j}(\gamma{}_{a}){}_{\beta}{}^{\gamma}(\gamma{}_{b}{}^{a}){}_{\alpha}{}^{\beta}\big(\mathcal D_{c}T{}^{c}{}^{b}\big)\lambda{}_{\gamma}{}_{j}\\
&+\frac{2i}{3}\rho^{-2}Y{}^{i}{}^{j}(\gamma{}_{a}){}_{\alpha}{}^{\beta}\big(\mathcal D^{b}T{}_{b}{}^{a}\big)\lambda{}_{\beta}{}_{j} -\frac{2}{9}\rho^{-2}Y{}^{i}{}^{j}(\gamma{}_{a}){}_{\alpha}{}^{\beta}(\gamma{}_{b}){}_{\beta}{}^{\gamma}\big(\mathcal D^{c}T{}^{d}{}^{e}\big)\epsilon{}_{c}{}^{b}{}^{a}{}_{d}{}_{e}\lambda{}_{\gamma}{}_{j}\\
&-\frac{8i}{27}\rho^{-2}Y{}^{i}{}^{j}(\gamma{}_{a}){}_{\beta}{}^{\gamma}(\gamma{}_{b}{}^{a}){}_{\alpha}{}^{\beta}T{}^{c}{}^{d}T{}_{e}{}_{f}\epsilon{}^{b}{}^{e}{}^{f}{}_{c}{}_{d}\lambda{}_{\gamma}{}_{j} +\frac{8i}{9}\rho^{-2}Y{}^{i}{}^{j}(\gamma{}_{a}){}_{\alpha}{}^{\beta}T{}^{b}{}^{c}T{}^{d}{}^{e}\epsilon{}^{a}{}_{d}{}_{e}{}_{b}{}_{c}\lambda{}_{\beta}{}_{j}\\
&-\frac{128}{27}\rho^{-2}Y{}^{i}{}^{j}(\gamma{}_{a}){}_{\alpha}{}^{\beta}(\gamma{}_{b}){}_{\beta}{}^{\gamma}T{}^{a}{}^{c}T{}^{b}{}_{c}\lambda{}_{\gamma}{}_{j} +\frac{8}{9}\rho^{-2}Y{}^{i}{}^{j}(\gamma{}^{a}){}_{\alpha}{}^{\beta}(\gamma{}_{a}){}_{\beta}{}^{\gamma}T{}^{b}{}^{c}T{}_{b}{}_{c}\lambda{}_{\gamma}{}_{j}\\
&+\frac{4}{3}\rho^{-3}\big(\mathcal D_{a}Y{}^{i}{}^{j}\big)\big(\mathcal D^{a}\rho\big)\lambda{}_{\alpha}{}_{j} -\frac{2}{3}\rho^{-2}\big(\mathcal D_{a}Y{}^{i}{}^{j}\big)\big(\mathcal D^{a}\lambda{}_{\alpha}{}_{j}\big)\\
&-\frac{2i}{3}\rho^{-2}\big(\mathcal D_{a}Y{}^{i}{}^{j}\big)(\gamma{}^{a}){}_{\alpha}{}^{\beta}(\gamma{}^{b}{}^{c}){}_{\beta}{}^{\gamma}T{}_{b}{}_{c}\lambda{}_{\gamma}{}_{j} +\frac{2i}{9}\rho^{-2}\big(\mathcal D_{a}Y{}^{i}{}^{j}\big)(\gamma{}^{a}){}_{\beta}{}^{\gamma}(\gamma{}^{b}{}^{c}){}_{\alpha}{}^{\beta}T{}_{b}{}_{c}\lambda{}_{\gamma}{}_{j}\\
&-\frac{i}{3}\rho^{-2}(\gamma{}^{a}){}_{\alpha}{}^{\beta}\big(\mathcal D^{b}\rho\big)\big(\mathcal D_{b}\mathcal D_{a}\lambda{}_{\beta}{}^{i}\big) +\frac{2}{9}\rho^{-2}(\gamma{}^{a}{}^{b}){}_{\alpha}{}_{\beta}\big(\mathcal D^{c}\rho\big)T{}_{a}{}_{b}\big(\mathcal D_{c}\lambda{}^{\beta}{}^{i}\big)\\
&+\frac{4}{3}\rho^{-2}\big(\mathcal D^{a}\rho\big)\big(\mathcal D_{a}\rho\big)\chi{}_{\alpha}{}^{i} +\frac{i}{3}\rho^{-2}(\gamma{}^{a}){}_{\alpha}{}^{\beta}\big(\mathcal D^{b}\rho\big)\varepsilon{}^{j}{}^{k}\varepsilon{}_{k}{}_{j}\big(\mathcal D_{b}\mathcal D_{a}\lambda{}_{\beta}{}^{i}\big)\\
&-\frac{2}{9}\rho^{-2}(\gamma{}^{a}{}^{b}){}_{\alpha}{}_{\beta}\big(\mathcal D^{c}\rho\big)\varepsilon{}^{j}{}^{k}\varepsilon{}_{k}{}_{j}T{}_{a}{}_{b}\big(\mathcal D_{c}\lambda{}^{\beta}{}^{i}\big) -\frac{4}{3}\rho^{-2}\big(\mathcal D^{a}\rho\big)\big(\mathcal D_{a}\rho\big)\varepsilon{}^{j}{}^{k}\varepsilon{}_{k}{}_{j}\chi{}_{\alpha}{}^{i}\\
&+\frac{1}{3}\rho^{-2}(\gamma{}^{a}){}_{\beta}{}^{\gamma}(\gamma{}_{b}){}_{\alpha}{}^{\delta}(\gamma{}^{c}{}^{d}){}_{\delta}{}^{\beta}\big(\mathcal D^{b}\rho\big)T{}_{c}{}_{d}\big(\mathcal D_{a}\lambda{}_{\gamma}{}^{i}\big) -\frac{1}{9}\rho^{-2}(\gamma{}^{a}){}_{\beta}{}^{\gamma}(\gamma{}_{b}){}_{\delta}{}^{\beta}(\gamma{}^{c}{}^{d}){}_{\alpha}{}^{\delta}\big(\mathcal D^{b}\rho\big)T{}_{c}{}_{d}\big(\mathcal D_{a}\lambda{}_{\gamma}{}^{i}\big)\\
&-\frac{1}{3}\rho^{-2}(\gamma{}^{a}){}_{\beta}{}^{\gamma}(\gamma{}_{b}){}_{\alpha}{}^{\delta}(\gamma{}^{c}{}^{d}){}_{\delta}{}^{\beta}\big(\mathcal D^{b}\rho\big)\varepsilon{}^{j}{}^{k}\varepsilon{}_{k}{}_{j}T{}_{c}{}_{d}\big(\mathcal D_{a}\lambda{}_{\gamma}{}^{i}\big) +\frac{1}{9}\rho^{-2}(\gamma{}^{a}){}_{\beta}{}^{\gamma}(\gamma{}_{b}){}_{\delta}{}^{\beta}(\gamma{}^{c}{}^{d}){}_{\alpha}{}^{\delta}\big(\mathcal D^{b}\rho\big)\varepsilon{}^{j}{}^{k}\varepsilon{}_{k}{}_{j}T{}_{c}{}_{d}\big(\mathcal D_{a}\lambda{}_{\gamma}{}^{i}\big)\\
&-\frac{8i}{3}\rho^{-2}Y{}_{j}{}^{i}(\gamma{}_{a}){}_{\alpha}{}^{\beta}\big(\mathcal D^{a}\rho\big)\chi{}_{\beta}{}^{j} -\frac{8i}{3}\rho^{-2}Y{}_{j}{}^{j}(\gamma{}_{a}){}_{\alpha}{}^{\beta}\big(\mathcal D^{a}\rho\big)\chi{}_{\beta}{}^{i}\\
&+\frac{8i}{3}\rho^{-2}Y{}^{i}{}_{j}\delta{}^{k}{}_{l}(\gamma{}_{a}){}_{\alpha}{}^{\beta}\big(\mathcal D^{a}\rho\big)\varepsilon{}^{m}{}^{l}\varepsilon{}_{k}{}_{m}\chi{}_{\beta}{}^{j} -\frac{8i}{3}\rho^{-2}Y{}^{i}{}_{j}(\gamma{}_{a}){}_{\alpha}{}^{\beta}\big(\mathcal D^{a}\rho\big)\chi{}_{\beta}{}^{j}\\
&-\frac{i}{48}\rho^{-2}R(V){}_{a}{}_{b}{}_{j}{}^{i}(\gamma{}_{c}){}_{\beta}{}^{\gamma}(\gamma{}^{a}{}^{b}){}_{\alpha}{}^{\beta}\big(\mathcal D^{c}\rho\big)\lambda{}_{\gamma}{}^{j} +\frac{i}{24}\rho^{-2}R(V){}_{a}{}_{b}{}_{j}{}^{i}(\gamma{}_{c}){}_{\alpha}{}^{\beta}(\gamma{}^{a}{}^{b}){}_{\beta}{}^{\gamma}\big(\mathcal D^{c}\rho\big)\lambda{}_{\gamma}{}^{j}\\
&-\frac{1}{6}\rho^{-2}(\gamma{}^{a}{}^{b}){}_{\alpha}{}^{\beta}\big(\mathcal D^{c}\rho\big)\big(\mathcal D_{c}T{}_{a}{}_{b}\big)\lambda{}_{\beta}{}^{i} -\frac{1}{6}\rho^{-2}(\gamma{}^{a}{}^{b}){}_{\alpha}{}^{\beta}\big(\mathcal D^{c}\rho\big)\big(\mathcal D_{a}T{}_{b}{}_{c}\big)\lambda{}_{\beta}{}^{i}\\
&-\frac{1}{6}\rho^{-2}(\gamma{}^{a}{}^{b}){}_{\alpha}{}^{\beta}\big(\mathcal D^{c}\rho\big)\big(\mathcal D_{b}T{}_{c}{}_{a}\big)\lambda{}_{\beta}{}^{i} -\frac{1}{6}\rho^{-2}(\gamma{}_{a}{}_{b}){}_{\alpha}{}^{\beta}\big(\mathcal D^{b}\rho\big)\big(\mathcal D_{c}T{}^{c}{}^{a}\big)\lambda{}_{\beta}{}^{i}\\
&+\frac{1}{2}\rho^{-2}\big(\mathcal D^{a}\rho\big)\big(\mathcal D^{b}T{}_{b}{}_{a}\big)\lambda{}_{\alpha}{}^{i} +\frac{i}{6}\rho^{-2}(\gamma{}_{a}){}_{\alpha}{}^{\beta}\big(\mathcal D^{b}\rho\big)\big(\mathcal D^{c}T{}^{d}{}^{e}\big)\epsilon{}_{c}{}_{b}{}^{a}{}_{d}{}_{e}\lambda{}_{\beta}{}^{i}\\
&-\frac{2}{9}\rho^{-2}(\gamma{}_{a}{}_{b}){}_{\alpha}{}^{\beta}\big(\mathcal D^{b}\rho\big)T{}^{c}{}^{d}T{}_{e}{}_{f}\epsilon{}^{a}{}^{e}{}^{f}{}_{c}{}_{d}\lambda{}_{\beta}{}^{i} +\frac{2}{3}\rho^{-2}\big(\mathcal D^{a}\rho\big)T{}^{b}{}^{c}T{}^{d}{}^{e}\epsilon{}_{a}{}_{d}{}_{e}{}_{b}{}_{c}\lambda{}_{\alpha}{}^{i}\\
&+\frac{32i}{9}\rho^{-2}(\gamma{}_{a}){}_{\alpha}{}^{\beta}\big(\mathcal D^{b}\rho\big)T{}^{a}{}^{c}T{}_{b}{}_{c}\lambda{}_{\beta}{}^{i} -\frac{2i}{3}\rho^{-2}(\gamma{}_{a}){}_{\alpha}{}^{\beta}\big(\mathcal D^{a}\rho\big)T{}^{b}{}^{c}T{}_{b}{}_{c}\lambda{}_{\beta}{}^{i}\\
&-\frac{i}{48}\rho^{-2}R(V){}_{a}{}_{b}{}_{j}{}^{j}(\gamma{}_{c}){}_{\beta}{}^{\gamma}(\gamma{}^{a}{}^{b}){}_{\alpha}{}^{\beta}\big(\mathcal D^{c}\rho\big)\lambda{}_{\gamma}{}^{i} +\frac{i}{24}\rho^{-2}R(V){}_{a}{}_{b}{}_{j}{}^{j}(\gamma{}_{c}){}_{\alpha}{}^{\beta}(\gamma{}^{a}{}^{b}){}_{\beta}{}^{\gamma}\big(\mathcal D^{c}\rho\big)\lambda{}_{\gamma}{}^{i}\\
&+\frac{1}{6}\rho^{-2}\delta{}^{j}{}_{k}(\gamma{}^{a}{}^{b}){}_{\alpha}{}^{\beta}\big(\mathcal D^{c}\rho\big)\varepsilon{}^{l}{}^{k}\varepsilon{}_{j}{}_{l}\big(\mathcal D_{c}T{}_{a}{}_{b}\big)\lambda{}_{\beta}{}^{i} +\frac{1}{6}\rho^{-2}\delta{}^{j}{}_{k}(\gamma{}^{a}{}^{b}){}_{\alpha}{}^{\beta}\big(\mathcal D^{c}\rho\big)\varepsilon{}^{l}{}^{k}\varepsilon{}_{j}{}_{l}\big(\mathcal D_{a}T{}_{b}{}_{c}\big)\lambda{}_{\beta}{}^{i}\\
&+\frac{1}{6}\rho^{-2}\delta{}^{j}{}_{k}(\gamma{}^{a}{}^{b}){}_{\alpha}{}^{\beta}\big(\mathcal D^{c}\rho\big)\varepsilon{}^{l}{}^{k}\varepsilon{}_{j}{}_{l}\big(\mathcal D_{b}T{}_{c}{}_{a}\big)\lambda{}_{\beta}{}^{i} +\frac{1}{6}\rho^{-2}\delta{}^{j}{}_{k}(\gamma{}_{a}{}_{b}){}_{\alpha}{}^{\beta}\big(\mathcal D^{b}\rho\big)\varepsilon{}^{l}{}^{k}\varepsilon{}_{j}{}_{l}\big(\mathcal D_{c}T{}^{c}{}^{a}\big)\lambda{}_{\beta}{}^{i}\\
&-\frac{1}{2}\rho^{-2}\delta{}^{j}{}_{k}\big(\mathcal D^{a}\rho\big)\varepsilon{}^{l}{}^{k}\varepsilon{}_{j}{}_{l}\big(\mathcal D^{b}T{}_{b}{}_{a}\big)\lambda{}_{\alpha}{}^{i} -\frac{i}{6}\rho^{-2}\delta{}^{j}{}_{k}(\gamma{}_{a}){}_{\alpha}{}^{\beta}\big(\mathcal D^{b}\rho\big)\varepsilon{}^{l}{}^{k}\varepsilon{}_{j}{}_{l}\big(\mathcal D^{c}T{}^{d}{}^{e}\big)\epsilon{}_{c}{}_{b}{}^{a}{}_{d}{}_{e}\lambda{}_{\beta}{}^{i}\\
&+\frac{2}{9}\rho^{-2}\delta{}^{j}{}_{k}(\gamma{}_{a}{}_{b}){}_{\alpha}{}^{\beta}\big(\mathcal D^{b}\rho\big)\varepsilon{}^{l}{}^{k}\varepsilon{}_{j}{}_{l}T{}^{c}{}^{d}T{}_{e}{}_{f}\epsilon{}^{a}{}^{e}{}^{f}{}_{c}{}_{d}\lambda{}_{\beta}{}^{i} -\frac{2}{3}\rho^{-2}\delta{}^{j}{}_{k}\big(\mathcal D^{a}\rho\big)\varepsilon{}^{l}{}^{k}\varepsilon{}_{j}{}_{l}T{}^{b}{}^{c}T{}^{d}{}^{e}\epsilon{}_{a}{}_{d}{}_{e}{}_{b}{}_{c}\lambda{}_{\alpha}{}^{i}\\
&-\frac{32i}{9}\rho^{-2}\delta{}^{j}{}_{k}(\gamma{}_{a}){}_{\alpha}{}^{\beta}\big(\mathcal D^{b}\rho\big)\varepsilon{}^{l}{}^{k}\varepsilon{}_{j}{}_{l}T{}^{a}{}^{c}T{}_{b}{}_{c}\lambda{}_{\beta}{}^{i} +\frac{2i}{3}\rho^{-2}\delta{}^{j}{}_{k}(\gamma{}_{a}){}_{\alpha}{}^{\beta}\big(\mathcal D^{a}\rho\big)\varepsilon{}^{l}{}^{k}\varepsilon{}_{j}{}_{l}T{}^{b}{}^{c}T{}_{b}{}_{c}\lambda{}_{\beta}{}^{i}\\
&+\frac{1}{192}\rho^{-2}R(M){}_{a}{}_{b}{}_{c}{}_{d}(\gamma{}^{c}{}^{d}){}_{\beta}{}^{\gamma}(\gamma{}^{a}{}^{b}){}_{\alpha}{}_{\delta}(\gamma{}_{e}{}_{f}){}^{\delta}{}^{\beta}\widehat F{}^{e}{}^{f}\lambda{}_{\gamma}{}^{i} -\frac{1}{27}\rho^{-2}(\gamma{}^{a}{}^{b}){}_{\beta}{}^{\gamma}(\gamma{}^{c}{}^{d}){}_{\alpha}{}_{\delta}(\gamma{}_{e}{}_{f}){}^{\delta}{}^{\beta}\widehat F{}^{e}{}^{f}T{}_{c}{}_{d}T{}_{a}{}_{b}\lambda{}_{\gamma}{}^{i}\\
&-\frac{1}{27}\rho^{-2}(\gamma{}^{a}{}^{b}){}_{\beta}{}^{\gamma}(\gamma{}^{c}{}^{d}){}_{\alpha}{}_{\delta}(\gamma{}_{e}{}_{f}){}^{\beta}{}^{\delta}\widehat F{}^{e}{}^{f}T{}_{c}{}_{d}T{}_{a}{}_{b}\lambda{}_{\gamma}{}^{i} -\frac{1}{27}\rho^{-2}(\gamma{}^{a}{}^{b}){}_{\alpha}{}^{\beta}(\gamma{}^{c}{}^{d}){}_{\gamma}{}_{\delta}(\gamma{}_{e}{}_{f}){}^{\gamma}{}^{\delta}\widehat F{}^{e}{}^{f}T{}_{a}{}_{b}T{}_{c}{}_{d}\lambda{}_{\beta}{}^{i}\\
&-\frac{i}{36}\rho^{-2}(\gamma{}^{a}){}_{\alpha}{}_{\beta}(\gamma{}^{b}{}^{c}){}_{\gamma}{}^{\delta}(\gamma{}_{d}{}_{e}){}^{\beta}{}^{\gamma}\widehat F{}^{d}{}^{e}\big(\mathcal D_{a}T{}_{b}{}_{c}\big)\lambda{}_{\delta}{}^{i} +\frac{1}{144}\rho^{-2}R(V){}_{a}{}_{b}{}_{j}{}^{i}(\gamma{}^{a}{}^{b}){}_{\beta}{}^{\gamma}(\gamma{}_{c}{}_{d}){}_{\alpha}{}^{\beta}\widehat F{}^{c}{}^{d}\lambda{}_{\gamma}{}^{j}\\
&-\frac{i}{36}\rho^{-2}(\gamma{}^{a}){}_{\alpha}{}_{\beta}(\gamma{}^{b}{}^{c}){}_{\gamma}{}^{\delta}(\gamma{}_{d}{}_{e}){}^{\gamma}{}^{\beta}\widehat F{}^{d}{}^{e}\big(\mathcal D_{a}T{}_{b}{}_{c}\big)\lambda{}_{\delta}{}^{i} +\frac{1}{144}\rho^{-2}R(V){}_{a}{}_{b}{}_{j}{}^{i}(\gamma{}^{a}{}^{b}){}_{\beta}{}^{\gamma}(\gamma{}_{c}{}_{d}){}^{\beta}{}_{\alpha}\widehat F{}^{c}{}^{d}\lambda{}_{\gamma}{}^{j}\\
&-\frac{i}{36}\rho^{-2}(\gamma{}^{a}){}_{\alpha}{}^{\beta}(\gamma{}^{b}{}^{c}){}_{\gamma}{}_{\delta}(\gamma{}_{d}{}_{e}){}^{\gamma}{}^{\delta}\widehat F{}^{d}{}^{e}\big(\mathcal D_{a}T{}_{b}{}_{c}\big)\lambda{}_{\beta}{}^{i} -\frac{1}{144}\rho^{-2}R(V){}_{a}{}_{b}{}_{j}{}^{i}(\gamma{}^{a}{}^{b}){}_{\beta}{}_{\gamma}(\gamma{}_{c}{}_{d}){}^{\beta}{}^{\gamma}\widehat F{}^{c}{}^{d}\lambda{}_{\alpha}{}^{j}\\
&-\frac{i}{72}\rho^{-2}(\gamma{}^{a}){}_{\beta}{}^{\gamma}(\gamma{}^{b}{}^{c}){}^{\delta}{}_{\gamma}(\gamma{}_{d}{}_{e}){}_{\alpha}{}^{\beta}\widehat F{}^{d}{}^{e}\big(\mathcal D_{a}T{}_{b}{}_{c}\big)\lambda{}_{\delta}{}^{i} -\frac{i}{72}\rho^{-2}(\gamma{}^{a}){}^{\beta}{}^{\gamma}(\gamma{}^{b}{}^{c}){}_{\delta}{}_{\gamma}(\gamma{}_{d}{}_{e}){}_{\alpha}{}^{\delta}\widehat F{}^{d}{}^{e}\big(\mathcal D_{a}T{}_{b}{}_{c}\big)\lambda{}_{\beta}{}^{i}\\
&-\frac{i}{72}\rho^{-2}(\gamma{}^{a}){}_{\beta}{}^{\gamma}(\gamma{}^{b}{}^{c}){}^{\delta}{}_{\gamma}(\gamma{}_{d}{}_{e}){}^{\beta}{}_{\alpha}\widehat F{}^{d}{}^{e}\big(\mathcal D_{a}T{}_{b}{}_{c}\big)\lambda{}_{\delta}{}^{i} -\frac{i}{72}\rho^{-2}(\gamma{}^{a}){}^{\beta}{}^{\gamma}(\gamma{}^{b}{}^{c}){}_{\delta}{}_{\gamma}(\gamma{}_{d}{}_{e}){}^{\delta}{}_{\alpha}\widehat F{}^{d}{}^{e}\big(\mathcal D_{a}T{}_{b}{}_{c}\big)\lambda{}_{\beta}{}^{i}\\
&+\frac{i}{72}\rho^{-2}(\gamma{}^{a}){}_{\beta}{}^{\gamma}(\gamma{}^{b}{}^{c}){}_{\delta}{}_{\gamma}(\gamma{}_{d}{}_{e}){}^{\beta}{}^{\delta}\widehat F{}^{d}{}^{e}\big(\mathcal D_{a}T{}_{b}{}_{c}\big)\lambda{}_{\alpha}{}^{i} +\frac{i}{72}\rho^{-2}(\gamma{}^{a}){}_{\beta}{}^{\gamma}(\gamma{}^{b}{}^{c}){}_{\delta}{}_{\gamma}(\gamma{}_{d}{}_{e}){}^{\delta}{}^{\beta}\widehat F{}^{d}{}^{e}\big(\mathcal D_{a}T{}_{b}{}_{c}\big)\lambda{}_{\alpha}{}^{i}\\
&-\frac{1}{24}\rho^{-2}(\gamma{}^{a}{}^{b}){}_{\alpha}{}_{\beta}\widehat F{}^{c}{}^{d}\widehat F{}_{a}{}_{b}\varepsilon{}^{j}{}^{k}\varepsilon{}_{k}{}_{j}R(Q){}_{c}{}_{d}{}^{\beta}{}^{i} +\frac{2}{9}\rho^{-1}(\gamma{}^{a}{}^{b}){}_{\alpha}{}_{\beta}\widehat F{}^{c}{}^{d}\varepsilon{}^{j}{}^{k}\varepsilon{}_{k}{}_{j}T{}_{a}{}_{b}R(Q){}_{c}{}_{d}{}^{\beta}{}^{i}
\end{aligned}
\tag{S6-phi-009}
```

```math
\begin{aligned}
&-\frac{1}{6}\rho^{-2}Y{}_{j}{}^{j}\widehat F{}^{a}{}^{b}R(Q){}_{a}{}_{b}{}_{\alpha}{}^{i} +\frac{i}{12}\rho^{-2}(\gamma{}^{a}){}_{\alpha}{}_{\beta}\widehat F{}^{b}{}^{c}\big(\mathcal D_{a}\rho\big)\varepsilon{}^{j}{}^{k}\varepsilon{}_{k}{}_{j}R(Q){}_{b}{}_{c}{}^{\beta}{}^{i}\\
&-\frac{1}{192}\rho^{-2}R(M){}_{a}{}_{b}{}_{c}{}_{d}(\gamma{}^{c}{}^{d}){}_{\beta}{}^{\gamma}(\gamma{}^{a}{}^{b}){}_{\alpha}{}_{\delta}(\gamma{}_{e}{}_{f}){}^{\delta}{}^{\beta}\widehat F{}^{e}{}^{f}\varepsilon{}^{j}{}^{k}\varepsilon{}_{k}{}_{j}\lambda{}_{\gamma}{}^{i} +\frac{1}{27}\rho^{-2}(\gamma{}^{a}{}^{b}){}_{\beta}{}^{\gamma}(\gamma{}^{c}{}^{d}){}_{\alpha}{}_{\delta}(\gamma{}_{e}{}_{f}){}^{\delta}{}^{\beta}\widehat F{}^{e}{}^{f}\varepsilon{}^{j}{}^{k}\varepsilon{}_{k}{}_{j}T{}_{c}{}_{d}T{}_{a}{}_{b}\lambda{}_{\gamma}{}^{i}\\
&+\frac{1}{27}\rho^{-2}(\gamma{}^{a}{}^{b}){}_{\beta}{}^{\gamma}(\gamma{}^{c}{}^{d}){}_{\alpha}{}_{\delta}(\gamma{}_{e}{}_{f}){}^{\beta}{}^{\delta}\widehat F{}^{e}{}^{f}\varepsilon{}^{j}{}^{k}\varepsilon{}_{k}{}_{j}T{}_{c}{}_{d}T{}_{a}{}_{b}\lambda{}_{\gamma}{}^{i} +\frac{1}{27}\rho^{-2}(\gamma{}^{a}{}^{b}){}_{\alpha}{}^{\beta}(\gamma{}^{c}{}^{d}){}_{\gamma}{}_{\delta}(\gamma{}_{e}{}_{f}){}^{\gamma}{}^{\delta}\widehat F{}^{e}{}^{f}\varepsilon{}^{j}{}^{k}\varepsilon{}_{k}{}_{j}T{}_{a}{}_{b}T{}_{c}{}_{d}\lambda{}_{\beta}{}^{i}\\
&+\frac{i}{36}\rho^{-2}(\gamma{}^{a}){}_{\alpha}{}_{\beta}(\gamma{}^{b}{}^{c}){}_{\gamma}{}^{\delta}(\gamma{}_{d}{}_{e}){}^{\beta}{}^{\gamma}\widehat F{}^{d}{}^{e}\varepsilon{}^{j}{}^{k}\varepsilon{}_{k}{}_{j}\big(\mathcal D_{a}T{}_{b}{}_{c}\big)\lambda{}_{\delta}{}^{i} +\frac{1}{144}\rho^{-2}R(V){}_{a}{}_{b}{}_{j}{}^{j}(\gamma{}^{a}{}^{b}){}_{\beta}{}^{\gamma}(\gamma{}_{c}{}_{d}){}_{\alpha}{}^{\beta}\widehat F{}^{c}{}^{d}\lambda{}_{\gamma}{}^{i}\\
&+\frac{i}{36}\rho^{-2}(\gamma{}^{a}){}_{\alpha}{}_{\beta}(\gamma{}^{b}{}^{c}){}_{\gamma}{}^{\delta}(\gamma{}_{d}{}_{e}){}^{\gamma}{}^{\beta}\widehat F{}^{d}{}^{e}\varepsilon{}^{j}{}^{k}\varepsilon{}_{k}{}_{j}\big(\mathcal D_{a}T{}_{b}{}_{c}\big)\lambda{}_{\delta}{}^{i} +\frac{1}{144}\rho^{-2}R(V){}_{a}{}_{b}{}_{j}{}^{j}(\gamma{}^{a}{}^{b}){}_{\beta}{}^{\gamma}(\gamma{}_{c}{}_{d}){}^{\beta}{}_{\alpha}\widehat F{}^{c}{}^{d}\lambda{}_{\gamma}{}^{i}\\
&+\frac{i}{36}\rho^{-2}(\gamma{}^{a}){}_{\alpha}{}^{\beta}(\gamma{}^{b}{}^{c}){}_{\gamma}{}_{\delta}(\gamma{}_{d}{}_{e}){}^{\gamma}{}^{\delta}\widehat F{}^{d}{}^{e}\varepsilon{}^{j}{}^{k}\varepsilon{}_{k}{}_{j}\big(\mathcal D_{a}T{}_{b}{}_{c}\big)\lambda{}_{\beta}{}^{i} -\frac{1}{144}\rho^{-2}R(V){}_{a}{}_{b}{}_{j}{}^{j}(\gamma{}^{a}{}^{b}){}_{\beta}{}_{\gamma}(\gamma{}_{c}{}_{d}){}^{\beta}{}^{\gamma}\widehat F{}^{c}{}^{d}\lambda{}_{\alpha}{}^{i}\\
&+\frac{i}{72}\rho^{-2}(\gamma{}^{a}){}_{\beta}{}^{\gamma}(\gamma{}^{b}{}^{c}){}^{\delta}{}_{\gamma}(\gamma{}_{d}{}_{e}){}_{\alpha}{}^{\beta}\widehat F{}^{d}{}^{e}\varepsilon{}^{j}{}^{k}\varepsilon{}_{k}{}_{j}\big(\mathcal D_{a}T{}_{b}{}_{c}\big)\lambda{}_{\delta}{}^{i} +\frac{i}{72}\rho^{-2}(\gamma{}^{a}){}^{\beta}{}^{\gamma}(\gamma{}^{b}{}^{c}){}_{\delta}{}_{\gamma}(\gamma{}_{d}{}_{e}){}_{\alpha}{}^{\delta}\widehat F{}^{d}{}^{e}\varepsilon{}^{j}{}^{k}\varepsilon{}_{k}{}_{j}\big(\mathcal D_{a}T{}_{b}{}_{c}\big)\lambda{}_{\beta}{}^{i}\\
&+\frac{i}{72}\rho^{-2}(\gamma{}^{a}){}_{\beta}{}^{\gamma}(\gamma{}^{b}{}^{c}){}^{\delta}{}_{\gamma}(\gamma{}_{d}{}_{e}){}^{\beta}{}_{\alpha}\widehat F{}^{d}{}^{e}\varepsilon{}^{j}{}^{k}\varepsilon{}_{k}{}_{j}\big(\mathcal D_{a}T{}_{b}{}_{c}\big)\lambda{}_{\delta}{}^{i} +\frac{i}{72}\rho^{-2}(\gamma{}^{a}){}^{\beta}{}^{\gamma}(\gamma{}^{b}{}^{c}){}_{\delta}{}_{\gamma}(\gamma{}_{d}{}_{e}){}^{\delta}{}_{\alpha}\widehat F{}^{d}{}^{e}\varepsilon{}^{j}{}^{k}\varepsilon{}_{k}{}_{j}\big(\mathcal D_{a}T{}_{b}{}_{c}\big)\lambda{}_{\beta}{}^{i}\\
&-\frac{i}{72}\rho^{-2}(\gamma{}^{a}){}_{\beta}{}^{\gamma}(\gamma{}^{b}{}^{c}){}_{\delta}{}_{\gamma}(\gamma{}_{d}{}_{e}){}^{\beta}{}^{\delta}\widehat F{}^{d}{}^{e}\varepsilon{}^{j}{}^{k}\varepsilon{}_{k}{}_{j}\big(\mathcal D_{a}T{}_{b}{}_{c}\big)\lambda{}_{\alpha}{}^{i} -\frac{i}{72}\rho^{-2}(\gamma{}^{a}){}_{\beta}{}^{\gamma}(\gamma{}^{b}{}^{c}){}_{\delta}{}_{\gamma}(\gamma{}_{d}{}_{e}){}^{\delta}{}^{\beta}\widehat F{}^{d}{}^{e}\varepsilon{}^{j}{}^{k}\varepsilon{}_{k}{}_{j}\big(\mathcal D_{a}T{}_{b}{}_{c}\big)\lambda{}_{\alpha}{}^{i}\\
&+\frac{1}{24}\rho^{-2}(\gamma{}^{a}{}^{b}){}_{\alpha}{}_{\beta}\widehat F{}^{c}{}^{d}\widehat F{}_{a}{}_{b}R(Q){}_{c}{}_{d}{}^{\beta}{}^{i} -\frac{2}{9}\rho^{-1}(\gamma{}^{a}{}^{b}){}_{\alpha}{}_{\beta}\widehat F{}^{c}{}^{d}T{}_{a}{}_{b}R(Q){}_{c}{}_{d}{}^{\beta}{}^{i}\\
&-\frac{1}{6}\rho^{-2}Y{}_{j}{}^{i}\widehat F{}^{a}{}^{b}R(Q){}_{a}{}_{b}{}_{\alpha}{}^{j} -\frac{i}{12}\rho^{-2}(\gamma{}^{a}){}_{\alpha}{}_{\beta}\widehat F{}^{b}{}^{c}\big(\mathcal D_{a}\rho\big)R(Q){}_{b}{}_{c}{}^{\beta}{}^{i}\\
&-\frac{1}{12}\rho^{-2}(\gamma{}^{a}{}^{b}){}_{\alpha}{}^{\beta}\widehat F{}_{a}{}_{b}\varepsilon{}^{j}{}^{k}\varepsilon{}_{k}{}_{j}\big(\mathcal D^{c}\mathcal D_{c}\lambda{}_{\beta}{}^{i}\big) +\frac{4}{9}\rho^{-1}(\gamma{}^{a}{}^{b}){}_{\alpha}{}^{\beta}\varepsilon{}^{j}{}^{k}\varepsilon{}_{k}{}_{j}T{}_{a}{}_{b}\big(\mathcal D^{c}\mathcal D_{c}\lambda{}_{\beta}{}^{i}\big)\\
&+\frac{1}{3}\rho^{-2}Y{}_{j}{}^{j}\big(\mathcal D^{a}\mathcal D_{a}\lambda{}_{\alpha}{}^{i}\big) +\frac{i}{6}\rho^{-2}(\gamma{}^{a}){}_{\alpha}{}^{\beta}\big(\mathcal D_{a}\rho\big)\varepsilon{}^{j}{}^{k}\varepsilon{}_{k}{}_{j}\big(\mathcal D^{b}\mathcal D_{b}\lambda{}_{\beta}{}^{i}\big)\\
&-\frac{1}{12}\rho^{-2}(\gamma{}^{a}{}^{b}){}_{\alpha}{}_{\beta}\big(\mathcal D^{c}\mathcal D_{c}\widehat F{}_{a}{}_{b}\big)\lambda{}^{\beta}{}^{i} +\frac{4}{9}\rho^{-2}(\gamma{}^{a}{}^{b}){}_{\alpha}{}_{\beta}\big(\mathcal D_{c}\rho\big)\big(\mathcal D^{c}T{}_{a}{}_{b}\big)\lambda{}^{\beta}{}^{i}\\
&+\frac{1}{3}\rho^{-2}\big(\mathcal D^{a}\mathcal D_{a}Y{}_{j}{}^{i}\big)\lambda{}_{\alpha}{}^{j} +\frac{i}{6}\rho^{-2}(\gamma{}^{a}){}_{\alpha}{}_{\beta}\big(\mathcal D^{b}\mathcal D_{b}\mathcal D_{a}\rho\big)\lambda{}^{\beta}{}^{i}\\
&-\frac{i}{12}\rho^{-2}(\gamma{}_{a}){}_{\alpha}{}^{\beta}(\gamma{}^{b}{}^{c}){}_{\beta}{}^{\gamma}(\gamma{}^{d}{}^{e}){}_{\gamma}{}_{\delta}\widehat F{}_{d}{}_{e}\big(\mathcal D^{a}T{}_{b}{}_{c}\big)\lambda{}^{\delta}{}^{i} -\frac{i}{12}\rho^{-2}(\gamma{}_{a}){}_{\alpha}{}^{\beta}(\gamma{}^{b}{}^{c}){}_{\beta}{}^{\gamma}(\gamma{}^{d}{}^{e}){}_{\gamma}{}_{\delta}\big(\mathcal D^{a}\widehat F{}_{d}{}_{e}\big)T{}_{b}{}_{c}\lambda{}^{\delta}{}^{i}\\
&+\frac{i}{36}\rho^{-2}(\gamma{}_{a}){}_{\beta}{}^{\gamma}(\gamma{}^{b}{}^{c}){}_{\alpha}{}^{\beta}(\gamma{}^{d}{}^{e}){}_{\gamma}{}_{\delta}\big(\mathcal D^{a}\widehat F{}_{d}{}_{e}\big)T{}_{b}{}_{c}\lambda{}^{\delta}{}^{i} +\frac{i}{3}\rho^{-2}Y{}_{j}{}^{i}(\gamma{}_{a}){}_{\alpha}{}^{\beta}(\gamma{}^{b}{}^{c}){}_{\beta}{}^{\gamma}\big(\mathcal D^{a}T{}_{b}{}_{c}\big)\lambda{}_{\gamma}{}^{j}\\
&+\frac{i}{3}\rho^{-2}\big(\mathcal D^{a}Y{}_{j}{}^{i}\big)(\gamma{}_{a}){}_{\alpha}{}^{\beta}(\gamma{}^{b}{}^{c}){}_{\beta}{}^{\gamma}T{}_{b}{}_{c}\lambda{}_{\gamma}{}^{j} -\frac{i}{9}\rho^{-2}\big(\mathcal D^{a}Y{}_{j}{}^{i}\big)(\gamma{}_{a}){}_{\beta}{}^{\gamma}(\gamma{}^{b}{}^{c}){}_{\alpha}{}^{\beta}T{}_{b}{}_{c}\lambda{}_{\gamma}{}^{j}\\
&-\frac{1}{6}\rho^{-2}(\gamma{}^{a}){}_{\beta}{}_{\gamma}(\gamma{}_{b}){}_{\alpha}{}^{\delta}(\gamma{}^{c}{}^{d}){}_{\delta}{}^{\beta}\big(\mathcal D_{a}\rho\big)\big(\mathcal D^{b}T{}_{c}{}_{d}\big)\lambda{}^{\gamma}{}^{i} -\frac{1}{6}\rho^{-2}(\gamma{}^{a}){}_{\beta}{}_{\gamma}(\gamma{}_{b}){}_{\alpha}{}^{\delta}(\gamma{}^{c}{}^{d}){}_{\delta}{}^{\beta}\big(\mathcal D^{b}\mathcal D_{a}\rho\big)T{}_{c}{}_{d}\lambda{}^{\gamma}{}^{i}\\
&+\frac{1}{18}\rho^{-2}(\gamma{}^{a}){}_{\beta}{}_{\gamma}(\gamma{}_{b}){}_{\delta}{}^{\beta}(\gamma{}^{c}{}^{d}){}_{\alpha}{}^{\delta}\big(\mathcal D^{b}\mathcal D_{a}\rho\big)T{}_{c}{}_{d}\lambda{}^{\gamma}{}^{i} -\frac{i}{12}\rho^{-2}(\gamma{}^{a}){}_{\alpha}{}^{\beta}(\gamma{}^{b}{}^{c}){}_{\beta}{}^{\gamma}(\gamma{}^{d}{}^{e}){}_{\gamma}{}_{\delta}\big(\mathcal D_{a}\widehat F{}_{d}{}_{e}\big)T{}_{b}{}_{c}\lambda{}^{\delta}{}^{i}\\
&+\frac{i}{36}\rho^{-2}(\gamma{}^{a}){}_{\beta}{}^{\gamma}(\gamma{}^{b}{}^{c}){}_{\alpha}{}^{\beta}(\gamma{}^{d}{}^{e}){}_{\gamma}{}_{\delta}\big(\mathcal D_{a}\widehat F{}_{d}{}_{e}\big)T{}_{b}{}_{c}\lambda{}^{\delta}{}^{i} +\frac{4i}{9}\rho^{-2}(\gamma{}^{a}){}_{\alpha}{}^{\beta}(\gamma{}^{b}{}^{c}){}_{\beta}{}^{\gamma}(\gamma{}^{d}{}^{e}){}_{\gamma}{}_{\delta}\big(\mathcal D_{a}\rho\big)T{}_{b}{}_{c}T{}_{d}{}_{e}\lambda{}^{\delta}{}^{i}\\
&-\frac{4i}{27}\rho^{-2}(\gamma{}^{a}){}_{\beta}{}^{\gamma}(\gamma{}^{b}{}^{c}){}_{\alpha}{}^{\beta}(\gamma{}^{d}{}^{e}){}_{\gamma}{}_{\delta}\big(\mathcal D_{a}\rho\big)T{}_{b}{}_{c}T{}_{d}{}_{e}\lambda{}^{\delta}{}^{i} +\frac{i}{3}\rho^{-2}\big(\mathcal D_{a}Y{}_{j}{}^{i}\big)(\gamma{}^{a}){}_{\alpha}{}^{\beta}(\gamma{}^{b}{}^{c}){}_{\beta}{}^{\gamma}T{}_{b}{}_{c}\lambda{}_{\gamma}{}^{j}\\
&-\frac{i}{9}\rho^{-2}\big(\mathcal D_{a}Y{}_{j}{}^{i}\big)(\gamma{}^{a}){}_{\beta}{}^{\gamma}(\gamma{}^{b}{}^{c}){}_{\alpha}{}^{\beta}T{}_{b}{}_{c}\lambda{}_{\gamma}{}^{j} -\frac{1}{6}\rho^{-2}(\gamma{}^{a}){}_{\alpha}{}^{\beta}(\gamma{}^{b}){}_{\gamma}{}_{\delta}(\gamma{}^{c}{}^{d}){}_{\beta}{}^{\gamma}\big(\mathcal D_{a}\mathcal D_{b}\rho\big)T{}_{c}{}_{d}\lambda{}^{\delta}{}^{i}\\
&+\frac{1}{18}\rho^{-2}(\gamma{}^{a}){}_{\beta}{}^{\gamma}(\gamma{}^{b}){}_{\gamma}{}_{\delta}(\gamma{}^{c}{}^{d}){}_{\alpha}{}^{\beta}\big(\mathcal D_{a}\mathcal D_{b}\rho\big)T{}_{c}{}_{d}\lambda{}^{\delta}{}^{i} +\frac{1}{12}\rho^{-2}(\gamma{}^{a}){}_{\alpha}{}^{\beta}(\gamma{}_{a}){}_{\gamma}{}^{\delta}(\gamma{}^{b}{}^{c}){}_{\beta}{}^{\gamma}(\gamma{}^{d}{}^{e}){}_{\delta}{}^{\rho}(\gamma{}^{f}{}^{g}){}_{\rho}{}_{\sigma}\widehat F{}_{f}{}_{g}T{}_{b}{}_{c}T{}_{d}{}_{e}\lambda{}^{\sigma}{}^{i}\\
&-\frac{1}{36}\rho^{-2}(\gamma{}^{a}){}_{\alpha}{}^{\beta}(\gamma{}_{a}){}_{\gamma}{}^{\delta}(\gamma{}^{b}{}^{c}){}_{\beta}{}^{\rho}(\gamma{}^{d}{}^{e}){}_{\rho}{}^{\gamma}(\gamma{}^{f}{}^{g}){}_{\delta}{}_{\sigma}\widehat F{}_{f}{}_{g}T{}_{b}{}_{c}T{}_{d}{}_{e}\lambda{}^{\sigma}{}^{i} -\frac{1}{36}\rho^{-2}(\gamma{}^{a}){}_{\beta}{}^{\gamma}(\gamma{}_{a}){}_{\gamma}{}^{\delta}(\gamma{}^{b}{}^{c}){}_{\alpha}{}^{\beta}(\gamma{}^{d}{}^{e}){}_{\delta}{}^{\rho}(\gamma{}^{f}{}^{g}){}_{\rho}{}_{\sigma}\widehat F{}_{f}{}_{g}T{}_{b}{}_{c}T{}_{d}{}_{e}\lambda{}^{\sigma}{}^{i}\\
&+\frac{1}{108}\rho^{-2}(\gamma{}^{a}){}_{\beta}{}^{\gamma}(\gamma{}_{a}){}_{\delta}{}^{\rho}(\gamma{}^{b}{}^{c}){}_{\alpha}{}^{\beta}(\gamma{}^{d}{}^{e}){}_{\gamma}{}^{\delta}(\gamma{}^{f}{}^{g}){}_{\rho}{}_{\sigma}\widehat F{}_{f}{}_{g}T{}_{b}{}_{c}T{}_{d}{}_{e}\lambda{}^{\sigma}{}^{i} -\frac{1}{3}\rho^{-2}Y{}_{j}{}^{i}(\gamma{}^{a}){}_{\alpha}{}^{\beta}(\gamma{}_{a}){}_{\gamma}{}^{\delta}(\gamma{}^{b}{}^{c}){}_{\beta}{}^{\gamma}(\gamma{}^{d}{}^{e}){}_{\delta}{}^{\rho}T{}_{b}{}_{c}T{}_{d}{}_{e}\lambda{}_{\rho}{}^{j}\\
&+\frac{1}{9}\rho^{-2}Y{}_{j}{}^{i}(\gamma{}^{a}){}_{\alpha}{}^{\beta}(\gamma{}_{a}){}_{\gamma}{}^{\delta}(\gamma{}^{b}{}^{c}){}_{\beta}{}^{\rho}(\gamma{}^{d}{}^{e}){}_{\rho}{}^{\gamma}T{}_{b}{}_{c}T{}_{d}{}_{e}\lambda{}_{\delta}{}^{j} +\frac{1}{9}\rho^{-2}Y{}_{j}{}^{i}(\gamma{}^{a}){}_{\beta}{}^{\gamma}(\gamma{}_{a}){}_{\gamma}{}^{\delta}(\gamma{}^{b}{}^{c}){}_{\alpha}{}^{\beta}(\gamma{}^{d}{}^{e}){}_{\delta}{}^{\rho}T{}_{b}{}_{c}T{}_{d}{}_{e}\lambda{}_{\rho}{}^{j}\\
&-\frac{1}{27}\rho^{-2}Y{}_{j}{}^{i}(\gamma{}^{a}){}_{\beta}{}^{\gamma}(\gamma{}_{a}){}_{\delta}{}^{\rho}(\gamma{}^{b}{}^{c}){}_{\alpha}{}^{\beta}(\gamma{}^{d}{}^{e}){}_{\gamma}{}^{\delta}T{}_{b}{}_{c}T{}_{d}{}_{e}\lambda{}_{\rho}{}^{j} -\frac{i}{6}\rho^{-2}(\gamma{}^{a}){}_{\alpha}{}^{\beta}(\gamma{}^{b}){}_{\gamma}{}_{\delta}(\gamma{}_{a}){}_{\rho}{}^{\sigma}(\gamma{}^{c}{}^{d}){}_{\beta}{}^{\rho}(\gamma{}^{e}{}^{f}){}_{\sigma}{}^{\gamma}\big(\mathcal D_{b}\rho\big)T{}_{c}{}_{d}T{}_{e}{}_{f}\lambda{}^{\delta}{}^{i}\\
&+\frac{i}{18}\rho^{-2}(\gamma{}^{a}){}_{\alpha}{}^{\beta}(\gamma{}^{b}){}_{\gamma}{}_{\delta}(\gamma{}_{a}){}_{\rho}{}^{\gamma}(\gamma{}^{c}{}^{d}){}_{\beta}{}^{\sigma}(\gamma{}^{e}{}^{f}){}_{\sigma}{}^{\rho}\big(\mathcal D_{b}\rho\big)T{}_{c}{}_{d}T{}_{e}{}_{f}\lambda{}^{\delta}{}^{i} +\frac{i}{18}\rho^{-2}(\gamma{}^{a}){}_{\beta}{}^{\gamma}(\gamma{}^{b}){}_{\delta}{}_{\rho}(\gamma{}_{a}){}_{\gamma}{}^{\sigma}(\gamma{}^{c}{}^{d}){}_{\alpha}{}^{\beta}(\gamma{}^{e}{}^{f}){}_{\sigma}{}^{\delta}\big(\mathcal D_{b}\rho\big)T{}_{c}{}_{d}T{}_{e}{}_{f}\lambda{}^{\rho}{}^{i}\\
&-\frac{i}{54}\rho^{-2}(\gamma{}^{a}){}_{\beta}{}^{\gamma}(\gamma{}^{b}){}_{\delta}{}_{\rho}(\gamma{}_{a}){}_{\sigma}{}^{\delta}(\gamma{}^{c}{}^{d}){}_{\alpha}{}^{\beta}(\gamma{}^{e}{}^{f}){}_{\gamma}{}^{\sigma}\big(\mathcal D_{b}\rho\big)T{}_{c}{}_{d}T{}_{e}{}_{f}\lambda{}^{\rho}{}^{i} +\frac{i}{72}\rho^{-2}R(V){}_{a}{}_{b}{}_{j}{}^{i}(\gamma{}^{c}){}_{\beta}{}^{\gamma}(\gamma{}^{a}{}^{b}){}_{\alpha}{}^{\beta}\big(\mathcal D_{c}\rho\big)\lambda{}_{\gamma}{}^{j}\\
&-\frac{i}{36}\rho^{-2}R(V){}_{a}{}_{b}{}_{j}{}^{i}(\gamma{}^{c}){}_{\alpha}{}^{\beta}(\gamma{}^{a}{}^{b}){}_{\beta}{}^{\gamma}\big(\mathcal D_{c}\rho\big)\lambda{}_{\gamma}{}^{j} +\frac{1}{9}\rho^{-2}(\gamma{}^{a}{}^{b}){}_{\alpha}{}^{\beta}\big(\mathcal D_{c}\rho\big)\big(\mathcal D^{c}T{}_{a}{}_{b}\big)\lambda{}_{\beta}{}^{i}\\
&+\frac{1}{9}\rho^{-2}(\gamma{}^{a}{}^{b}){}_{\alpha}{}^{\beta}\big(\mathcal D_{c}\rho\big)\big(\mathcal D_{a}T{}_{b}{}^{c}\big)\lambda{}_{\beta}{}^{i} +\frac{1}{9}\rho^{-2}(\gamma{}^{a}{}^{b}){}_{\alpha}{}^{\beta}\big(\mathcal D_{c}\rho\big)\big(\mathcal D_{b}T{}^{c}{}_{a}\big)\lambda{}_{\beta}{}^{i}\\
&+\frac{1}{9}\rho^{-2}(\gamma{}_{a}{}^{b}){}_{\alpha}{}^{\beta}\big(\mathcal D_{b}\rho\big)\big(\mathcal D_{c}T{}^{c}{}^{a}\big)\lambda{}_{\beta}{}^{i} -\frac{1}{3}\rho^{-2}\big(\mathcal D_{a}\rho\big)\big(\mathcal D^{b}T{}_{b}{}^{a}\big)\lambda{}_{\alpha}{}^{i}\\
&-\frac{i}{9}\rho^{-2}(\gamma{}_{a}){}_{\alpha}{}^{\beta}\big(\mathcal D_{b}\rho\big)\big(\mathcal D^{c}T{}^{d}{}^{e}\big)\epsilon{}_{c}{}^{b}{}^{a}{}_{d}{}_{e}\lambda{}_{\beta}{}^{i} +\frac{4}{27}\rho^{-2}(\gamma{}_{a}{}^{b}){}_{\alpha}{}^{\beta}\big(\mathcal D_{b}\rho\big)T{}^{c}{}^{d}T{}_{e}{}_{f}\epsilon{}^{a}{}^{e}{}^{f}{}_{c}{}_{d}\lambda{}_{\beta}{}^{i}\\
&-\frac{4}{9}\rho^{-2}\big(\mathcal D_{a}\rho\big)T{}^{b}{}^{c}T{}^{d}{}^{e}\epsilon{}^{a}{}_{d}{}_{e}{}_{b}{}_{c}\lambda{}_{\alpha}{}^{i} -\frac{64i}{27}\rho^{-2}(\gamma{}_{a}){}_{\alpha}{}^{\beta}\big(\mathcal D_{b}\rho\big)T{}^{a}{}^{c}T{}^{b}{}_{c}\lambda{}_{\beta}{}^{i}\\
&+\frac{8i}{9}\rho^{-2}(\gamma{}^{a}){}_{\alpha}{}^{\beta}\big(\mathcal D_{a}\rho\big)T{}^{b}{}^{c}T{}_{b}{}_{c}\lambda{}_{\beta}{}^{i} +\frac{1}{288}\rho^{-2}R(V){}_{a}{}_{b}{}_{j}{}^{i}(\gamma{}^{c}){}_{\beta}{}^{\gamma}(\gamma{}_{c}){}_{\gamma}{}^{\delta}(\gamma{}^{a}{}^{b}){}_{\alpha}{}^{\beta}(\gamma{}^{d}{}^{e}){}_{\delta}{}_{\rho}\widehat F{}_{d}{}_{e}\lambda{}^{\rho}{}^{j}\\
&-\frac{1}{144}\rho^{-2}R(V){}_{a}{}_{b}{}_{j}{}^{i}(\gamma{}^{c}){}_{\alpha}{}^{\beta}(\gamma{}_{c}){}_{\gamma}{}^{\delta}(\gamma{}^{a}{}^{b}){}_{\beta}{}^{\gamma}(\gamma{}^{d}{}^{e}){}_{\delta}{}_{\rho}\widehat F{}_{d}{}_{e}\lambda{}^{\rho}{}^{j} -\frac{i}{36}\rho^{-2}(\gamma{}_{a}){}_{\beta}{}^{\gamma}(\gamma{}^{b}{}^{c}){}_{\alpha}{}^{\beta}(\gamma{}^{d}{}^{e}){}_{\gamma}{}_{\delta}\widehat F{}_{d}{}_{e}\big(\mathcal D_{b}T{}_{c}{}^{a}\big)\lambda{}^{\delta}{}^{i}\\
&-\frac{i}{36}\rho^{-2}(\gamma{}_{a}){}_{\beta}{}^{\gamma}(\gamma{}^{b}{}^{c}){}_{\alpha}{}^{\beta}(\gamma{}^{d}{}^{e}){}_{\gamma}{}_{\delta}\widehat F{}_{d}{}_{e}\big(\mathcal D_{c}T{}^{a}{}_{b}\big)\lambda{}^{\delta}{}^{i} -\frac{i}{36}\rho^{-2}(\gamma{}_{a}){}_{\beta}{}^{\gamma}(\gamma{}^{b}{}^{c}){}_{\gamma}{}_{\delta}(\gamma{}_{d}{}^{a}){}_{\alpha}{}^{\beta}\widehat F{}_{b}{}_{c}\big(\mathcal D_{e}T{}^{e}{}^{d}\big)\lambda{}^{\delta}{}^{i}\\
&+\frac{i}{12}\rho^{-2}(\gamma{}_{a}){}_{\alpha}{}^{\beta}(\gamma{}^{b}{}^{c}){}_{\beta}{}_{\gamma}\widehat F{}_{b}{}_{c}\big(\mathcal D^{d}T{}_{d}{}^{a}\big)\lambda{}^{\gamma}{}^{i} -\frac{1}{36}\rho^{-2}(\gamma{}_{a}){}_{\alpha}{}^{\beta}(\gamma{}_{b}){}_{\beta}{}^{\gamma}(\gamma{}^{c}{}^{d}){}_{\gamma}{}_{\delta}\widehat F{}_{c}{}_{d}\big(\mathcal D^{e}T{}^{f}{}^{g}\big)\epsilon{}_{e}{}^{b}{}^{a}{}_{f}{}_{g}\lambda{}^{\delta}{}^{i}\\
&-\frac{i}{27}\rho^{-2}(\gamma{}_{a}){}_{\beta}{}^{\gamma}(\gamma{}^{b}{}^{c}){}_{\gamma}{}_{\delta}(\gamma{}_{d}{}^{a}){}_{\alpha}{}^{\beta}\widehat F{}_{b}{}_{c}T{}^{e}{}^{f}T{}_{g}{}_{h}\epsilon{}^{d}{}^{g}{}^{h}{}_{e}{}_{f}\lambda{}^{\delta}{}^{i} +\frac{i}{9}\rho^{-2}(\gamma{}_{a}){}_{\alpha}{}^{\beta}(\gamma{}^{b}{}^{c}){}_{\beta}{}_{\gamma}\widehat F{}_{b}{}_{c}T{}^{d}{}^{e}T{}^{f}{}^{g}\epsilon{}^{a}{}_{f}{}_{g}{}_{d}{}_{e}\lambda{}^{\gamma}{}^{i}
\end{aligned}
\tag{S6-phi-010}
```


[Component index](../STEP_06_LOG_PROJECTED_MULTIPLET_AND_BOSONIC_ACTION.md) · [Next component](spinor_002.md)
