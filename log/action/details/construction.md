# Gauged LOG invariant with full supercovariant derivatives

<!-- LOG_CURRENT_CERTIFICATION_20260925 -->

**Current scope:** [the 2026-09-25 certificate](component_construction/results/gauged_full_fermionic_log/CERTIFICATION_LOG_TWO_FERMI_2026-09-25.md) verifies the full primary and the component action through two physical fermions. The source comparisons and restricted tests below retain their stated mathematical scope.

**Derivative convention.** All component derivatives below use the same $`\mathcal D_a`$ and $`\Box^c`$ as [the fermionic gauged Weyl-squared calculation](../../../weyl2/action/details/construction.md), GC14–GC24. Their Q/S/K connections and implicit fermions remain inside them.

## Contents

1. [Problem and Target](construction.md#1-problem-and-target)
2. [Convention Ledger](construction.md#2-convention-ledger)
3. [Definitions and Required Identities](construction.md#3-definitions-and-required-identities)
4. [Detailed Derivation](construction.md#4-detailed-derivation), including the [gauge-fixed derivative dictionary](construction.md#gauge-fixed-derivatives)
5. [Consistency Checks](construction.md#5-consistency-checks)
6. [Final Result](construction.md#6-final-result): [triplet](construction.md#61-triplet), [spinor](construction.md#62-spinor), [scalar](construction.md#63-scalar), [vector](construction.md#64-constrained-vector), [BF action](construction.md#65-bf-current-and-action)
7. [Convention Dependence and Remaining Uncertainties](construction.md#7-convention-dependence-and-remaining-uncertainties)

<a id="1-problem-and-target"></a>

## Problem and Target

**Goal.** Present the gauged, gauge-evaluated LOG multiplet and BF density with all derivatives fully supercovariant, all four algebraic Weyl composites $`Y,T,\chi,D`$ substituted, curvature tensors retained, and the tensor/Clifford contractions canonicalized. The dependent $`\omega,\phi,f`$ relations are given in the same file; their occurrences inside derivatives and curvatures are kept implicit.

**Starting point.** The full-derivative polynomials in [the canonical two-fermion LOG multiplet](component_construction/results/gauged_full_fermionic_log/LOG_MULTIPLET_CANONICAL_TWO_FERMI.md), obtained from [Step 6](component_construction/results/gauged_full_fermionic_log/STEP_06_LOG_PROJECTED_MULTIPLET_AND_BOSONIC_ACTION.md). The substitution preserves the full Q/S/K connections in the ordered derivatives.

**Method.** Insert the gauged composite identities while the compensator is unfixed; use the even covariant product rule with the original derivative order; evaluate the gauge values; then contract and collect. This order retains every connection descendant of a field whose undifferentiated gauge value vanishes. The resulting expressions retain the full supercovariant derivatives.

**A1.** Five-dimensional classical off-shell fields; no background, field equation, auxiliary elimination or integration by parts. **A2.** The defining vector is $`(\rho,A_\mu,\lambda^i)=(\sigma,C_\mu,\psi^i)`$. The independent linear compensator $`(L_c^{ij},\varphi_c^i,N_c,E_c^a)`$ is distinct from the LOG multiplet. **A3.** The target gauge is (SC7-02). **A4.** Retain degree zero and two in even slots and degree one in the spinor, counting implicit fermions when the covariants are evaluated; higher orders are $`+\text{high fermi terms}`$. **A5.** Derivatives are not interchanged. Canonicality is with respect to the declared algebraic symmetries, Clifford identities and conventional curvature traces, not a minimal basis under every differential Bianchi, Schouten or boundary identity.

| Input | Located source and equation | Role |
|---|---|---|
| LOG multiplet and BF density | S23, arXiv:2302.14295v2, (3.24)–(3.27), (3.2); project Step 6 and canonical CTF-01 | Once-projected component input |
| Full gauged composites | W, hep-th/0104113v4, (5.10)–(5.14); CO, arXiv:1210.4704v3, (5.2)–(5.8); master GC01–GC12 | $`Y,T,\chi,D`$ before fixing the gauge |
| Derivative notation and meaning | Fermionic Weyl-squared calculation GC14, GC16–GC24; identical master GC entries | Full $`\mathcal D_a`$, $`\Box^c`$, ordered descendant action |
| Conventional constraints | W (3.9)–(3.12); OP, arXiv:1301.6622v4, (2.5)–(2.9); master GC18–GC20 | $`\omega,\phi,f`$ and curvature traces |
| Target gauge | G25, arXiv:2504.10856v1, (7), (25), (27); master LOG-G01 | Scale, S gauge, K gauge and SU(2) alignment |
| Linear constraint/current | OP (2.18)–(2.23), OPall arXiv:1306.1540v3 (3.1)–(3.2); master L02–L03, A02 | Full covariant vector constraint and BF current |

The [main branch conventions](component_construction/results/gauged_full_fermionic_log/CONVENTIONS.md) and [LOG-specific conventions](component_construction/results/gauged_full_fermionic_log/LOG_CONVENTIONS.md) remain authoritative. The source caches and printed-versus-project-corrected distinctions are preserved.

<a id="2-convention-ledger"></a>

## Convention Ledger

<!-- ASSERT_CONVENTION: metric_signature=(-,+,+,+,+), natural_units=hbar=c=1, gamma_volume=+i, bar=linear Majorana, derivative=full supercovariant mathcal D, derivative_order=preserved, source_lock=GAUGED-LOG-CONVENTIONS-v1 -->

Tangent/world indices run over five dimensions, spinor indices over four components, and $`i,j=1,2`$. Use $`\eta=(-,+,+,+,+)`$, $`\epsilon^{01234}=1`$, $`\gamma^{01234}=i`$, $`\{\gamma^a,\gamma^b\}=2\eta^{ab}`$, and unit-weight (anti)symmetrization. The Majorana bar is linear, $`\bar u=u^T\mathsf C`$, including on a coefficient $`i`$; spinors are odd. Right lowering is $`u_i=u^j\varepsilon_{ji}`$ with $`\varepsilon_{12}=\varepsilon^{12}=1`$. The fixed-doublet bilinear exchange signs for gamma rank $`0,1,2`$ are $`+,+,-`$; a contracted doublet reversal supplies its separate minus.

Use the project Riemann sign $`R_{\mu\nu}{}^{ab}(\omega)=2\partial_{[\mu}\omega_{\nu]}{}^{ab}+2\omega_{[\mu}{}^{ac}\omega_{\nu]c}{}^b`$. The Ricci contraction is fixed by (SC7-06). Before gauge evaluation the conformal weights of $`(\sigma,\psi^i,\widehat G,\widehat H_{ab},L_c,\varphi_c,N_c,g)`$ are $`(1,3/2,2,3,3,7/2,4,0)`$. On the fixed scale their engineering dimensions are $`(0,1/2,1,1,0,1/2,1,1)`$; $`\mathcal D_a`$ has dimension one. The LOG slots have dimensions $`3,7/2,4,4`$. The coupling is $`S=(2\kappa_5^2)^{-1}\int e(\ell_{2\partial}+\lambda_{\rm LOG}\ell_{\log})`$, $`[\lambda_{\rm LOG}]=-2`$.

There is one component derivative convention throughout the active calculation: $`\mathcal D_a`$ is full and supercovariant. $`D`$ without an index is the auxiliary scalar; it is never a derivative. Gold's $`\nabla_A`$ remains its source superspace notation in the earlier superspace derivations; the bridge is applied once at Step 6. Fourier/state normalization and renormalization are not involved.

<a id="3-definitions-and-required-identities"></a>

## Definitions and Required Identities

<a id="31-full-derivative-box-and-gauge-evaluation"></a>

### Full derivative, box and gauge evaluation

The Weyl-squared definition GC21 is used verbatim in meaning:

```math
\mathcal D_\mu\Phi=\partial_\mu\Phi-\delta_D(b_\mu)\Phi-\delta_M(\omega_\mu)\Phi-\delta_U(V_\mu)\Phi-\delta_Q(\psi_\mu)\Phi-\delta_S(\phi_\mu)\Phi-\delta_K(f_\mu)\Phi,\qquad \mathcal D_a=e_a{}^\mu\mathcal D_\mu,\qquad \Box^c\Phi:=\mathcal D^a\mathcal D_a\Phi.
\tag{SC7-01}
```

Each generator acts on the actual field or descendant to its right. For example, in $`\mathcal D_a\mathcal D_b\Phi`$ the outer derivative acts on the tangent index $`b`$ and the Q/S/K transformation of $`\mathcal D_b\Phi`$. The superscript $`c`$ means conformal; it is not an index or a fermion-order label. Adjacent contracted derivatives alone are abbreviated by $`\Box^c`$. Ordered expressions such as $`\mathcal D^a\mathcal D_b\mathcal D_a\Phi`$ stay in that order. The use of this operator does not import the Weyl-squared composite or its normalization.

```math
\sigma=1,\qquad \psi^i=0,\qquad b_\mu=0,\qquad L_c^{ij}=\frac{L}{\sqrt2}\delta^{ij},\qquad V_\mu{}^{ij}=V'_\mu{}^{ij}+\frac12\delta^{ij}V_\mu .
\tag{SC7-02}
```

**Evaluation convention for every final formula:** $`\mathcal D_{a_1}\cdots\mathcal D_{a_n}\Phi`$ means $`(\mathcal D_{a_1}\cdots\mathcal D_{a_n}\Phi)|_{\rm gauge}`$, with all derivatives taken before (SC7-02). We suppress the repeated vertical bar in §6. The symbols $`\sigma`$ and $`\psi^i`$ there occur only inside such derivatives. They introduce no independent scalar or dilatino after gauge fixing. In particular,

```math
\mathcal D_a\sigma|_{\rm gauge}=0,\qquad
\mathcal D_a\psi^i|_{\rm gauge}=\frac18\gamma^{bc}(\widehat G_{bc}+2\widehat H_{bc})\psi_a^i-\frac g2L_c^{ij}\psi_{aj}-\phi_a^i,\qquad
\Box^c\sigma|_{\rm gauge}=2f_a{}^a-\frac i2\bar\psi_a\mathcal D^a\psi-2\bar\psi_a\gamma^a\chi.
\tag{SC7-03}
```

These are definitions for interpreting surviving descendants, not extra terms to add to a density already written with full derivatives. Master GC14, GC16 supply them. Section 4.4 gives the explicit first derivatives, Hessians and boxes, with the connection contributions evaluated. Higher ordered descendants remain full operators with the same inherited transformation law; they are not obtained by differentiating the numerical gauge values as ordinary functions.

The independent compensator has, in this notation,

```math
\mathcal D_aL_c^{ij}=\frac{\delta^{ij}}{\sqrt2}\partial_aL+\frac{L}{\sqrt2}\left(V'_a{}^i{}_k\delta^{jk}+V'_a{}^j{}_k\delta^{ik}\right)-i\bar\psi_a^{(i}\varphi_c^{j)}.
\tag{SC7-04}
```

The last term is retained implicitly whenever $`\mathcal D_aL_c^{ij}`$ occurs in §6. Constant $`L`$ does not remove the connection terms. The source is Weyl GC24/master L02.

<a id="32-strengths-curvature-constraints-and-dependent-connections"></a>

### Strengths, curvature constraints and dependent connections

The strength conventions at the gauge are

```math
\widehat G_{\mu\nu}=2\partial_{[\mu}C_{\nu]}+\frac i2\bar\psi_{[\mu}\psi_{\nu]},\qquad
\widehat H_{\mu\nu\rho}=3\partial_{[\mu}B_{\nu\rho]}+\frac32C_{[\mu}G_{\nu\rho]}+\frac g2E_{c\mu\nu\rho}-\frac34\bar\psi_{[\mu}\gamma_\nu\psi_{\rho]},\qquad
\widehat H_{ab}:=-\frac1{12}\epsilon_{abcde}\widehat H^{cde}.
\tag{SC7-05}
```

When differentiated, the hats mean the full definitions before gauge evaluation, Weyl GC03. In particular $`\widehat G`$ before the gauge also contains $`-\bar\psi_{[\mu}\gamma_{\nu]}\psi`$ and the coefficient of its gravitino bilinear is $`i\sigma/2`$; the three-form includes $`-3i\sigma\bar\psi_{[\mu}\gamma_{\nu\rho]}\psi/2`$ and the coefficient $`-3\sigma^2/4`$. Their undifferentiated dilatino terms vanish at the gauge, but are part of the inherited derivative definitions.

The conventional constraints are $`R(P)=0`$, $`\gamma^a\widehat R(Q)_{ab}^i=0`$, and $`\widehat R(M)_{acb}{}^c=0`$. Their connection solutions are

```math
\begin{aligned}
\omega_\mu{}^{ab}&=\omega_\mu{}^{ab}(e)+\frac12\bar\psi^{[a}\gamma^{b]}\psi_\mu+\frac14\bar\psi^a\gamma_\mu\psi^b,\qquad
\phi_a^i=\frac i3\gamma^b\widehat R'(Q)_{ab}^i-\frac i{24}\gamma_a\gamma^{bc}\widehat R'(Q)_{bc}^i,\\
f_{ab}&=-\frac16\mathcal R_{ab}+\frac1{48}\eta_{ab}\mathcal R,\qquad f_a{}^a=-\frac1{16}\mathcal R,\qquad
\mathcal R_{\mu\nu}:=\widehat R'(M)_{\mu\rho}{}^{ab}e_b{}^\rho e_{\nu a},\quad\mathcal R:=\mathcal R_\mu{}^\mu .
\end{aligned}\tag{SC7-06}
```

Here $`\widehat R'(Q)=\widehat R(Q)+2i\gamma_{[a}\phi_{b]}`$ and $`\widehat R'(M)=\widehat R(M)-8f_{[\mu}{}^{[a}e_{\nu]}{}^{b]}`$ omit the S and K connections respectively. Master GC18–GC20 define the primed curvatures before those connections are inserted, including the project-corrected $`+8\bar\psi e\gamma\chi`$ term. The trace follows directly from $`-1/6+5/48=-1/16`$. No trace constraint is imposed on $`R'(Q)`$ or $`\mathcal R_{ab}`$.

For consistency with the Weyl calculation, hats on the three retained curvatures are printed in §6; $`\widehat C_{abcd}=\widehat R(M)_{abcd}`$. Curvatures keep their full gauged definitions, and no field-strength or curvature is expanded into a connection polynomial there.

<a id="33-gauged-composite-identities-before-differentiation"></a>

### Gauged composite identities before differentiation

The identities to be substituted, before (SC7-02), are

```math
\begin{aligned}
Y^{ij}&=\frac{i}{4\sigma}\bar\psi^{(i}\psi^{j)}-\frac g{2\sigma}L_c^{ij},\qquad
T_{ab}=\frac{\widehat G_{ab}}{8\sigma}-\frac{\widehat H_{ab}}{4\sigma^2}+\frac{i}{32\sigma^2}\bar\psi\gamma_{ab}\psi,\\
\chi^i&=\frac i{8\sigma}\gamma^a\mathcal D_a\psi^i+\frac i{16\sigma^2}\gamma^a(\mathcal D_a\sigma)\psi^i-\frac1{32\sigma^2}\gamma^{ab}\widehat G_{ab}\psi^i+\frac1{4\sigma}\gamma^{ab}T_{ab}\psi^i-\frac g{16\sigma^3}L_c^{ij}\psi_j+\frac g{8\sigma^2}\varphi_c^i+\text{high fermi terms},\\
D&=\frac1{4\sigma}\Box^c\sigma+\frac1{8\sigma^2}(\mathcal D_a\sigma)(\mathcal D^a\sigma)-\frac1{16\sigma^2}\widehat G^2-\frac1{8\sigma^2}\bar\psi\gamma^a\mathcal D_a\psi+\frac1{4\sigma^2}Y^{ij}Y_{ij}+\frac i{4\sigma^2}T_{ab}\bar\psi\gamma^{ab}\psi-\frac{4i}{\sigma}\bar\psi\chi-\frac{26}{3}T^2+\frac2\sigma\widehat G_{ab}T^{ab}+\frac g{4\sigma^2}N_c.
\end{aligned}\tag{SC7-07}
```

The $`Y`$ and $`T`$ identities are complete. Only the cubic term of $`\chi`$ is suppressed here; its full expression is master GC08. Inserting $`Y,T,\chi`$ recursively in $`D`$ generates the full even identity through degree two. Differentiation is even and does not reduce total fermion degree, so discarded cubic/quartic pieces cannot feed the retained slots. The two-index $`\widehat H`$ is only the conventional dual in (SC7-05); it is unrelated to the LOG triplet.

<a id="4-detailed-derivation"></a>

## Detailed Derivation

<a id="41-recover-the-gauge-values-without-changing-the-derivative"></a>

### Recover the gauge values without changing the derivative

Set $`\sigma=1`$, undifferentiated $`\psi^i=0`$, and $`\mathcal D_a\sigma=0`$ in (SC7-07), retaining its differentiated spinor and conformal box. This gives

```math
Y^{ij}=-\frac g2L_c^{ij},\qquad T_{ab}=\frac18(\widehat G_{ab}-2\widehat H_{ab}),\qquad
\chi^i=\frac i8\gamma^a\mathcal D_a\psi^i+\frac g8\varphi_c^i.
\tag{SC7-08}
```

For $`D`$, insert $`T=(\widehat G-2\widehat H)/8`$ into its three flux terms. Their coefficients are

```math
\begin{aligned}
-\frac1{16}\widehat G^2-\frac{26}{3}T^2+2\widehat G_{ab}T^{ab}
&=\left(-\frac1{16}-\frac{13}{96}+\frac14\right)\widehat G^2+\left(\frac{13}{24}-\frac12\right)\widehat G_{ab}\widehat H^{ab}-\frac{13}{24}\widehat H^2\\
&=\frac5{96}\widehat G^2+\frac1{24}\widehat G_{ab}\widehat H^{ab}-\frac{13}{24}\widehat H^2.
\end{aligned}\tag{SC7-09}
```

Since $`Y^{ij}Y_{ij}=g^2L_c^{ij}L_{cij}/4`$, the scalar composite is

```math
D=\frac14\Box^c\sigma+\frac5{96}\widehat G^2+\frac1{24}\widehat G_{ab}\widehat H^{ab}-\frac{13}{24}\widehat H^2+\frac g4N_c+\frac{g^2}{16}L_c^{ij}L_{cij}.
\tag{SC7-10}
```

Its curvature and gravitino terms are inside $`\Box^c\sigma`$. Using (SC7-03) only to identify them gives $`\Box^c\sigma=-\mathcal R/8-i\bar\psi_a\mathcal D^a\psi/2-2\bar\psi_a\gamma^a\chi`$. This relation is not applied to expand the final component collection.

<a id="42-differentiate-before-evaluating-the-gauge"></a>

### Differentiate before evaluating the gauge

The even covariant derivative obeys

```math
\mathcal D_a(UV)=(\mathcal D_aU)V+U\mathcal D_aV,\qquad
\mathcal D_a\sigma^{-n}=-n\sigma^{-n-1}\mathcal D_a\sigma,
\tag{SC7-11}
```

and, without interchanging derivatives or fermions,

```math
\mathcal D_a\mathcal D_b(UV)=(\mathcal D_a\mathcal D_bU)V+(\mathcal D_bU)(\mathcal D_aV)+(\mathcal D_aU)(\mathcal D_bV)+U\mathcal D_a\mathcal D_bV.
\tag{SC7-12}
```

For example, first differentiating $`Y`$ in (SC7-07) gives

```math
\begin{aligned}
\mathcal D_bY^{ij}={}&-\frac{i}{4\sigma^2}(\mathcal D_b\sigma)\bar\psi^i\psi^j+\frac i{4\sigma}\left[\overline{\mathcal D_b\psi^i}\psi^j+\bar\psi^i\mathcal D_b\psi^j\right]
+\frac g{2\sigma^2}(\mathcal D_b\sigma)L_c^{ij}-\frac g{2\sigma}\mathcal D_bL_c^{ij}.
\end{aligned}\tag{SC7-13}
```

Its value at the gauge is $`-g\mathcal D_bL_c^{ij}/2`$. Apply the second derivative to (SC7-13), rather than to this gauge value. The factors of undifferentiated $`\psi`$ and first $`\mathcal D\sigma`$ vanish only after that operation. The surviving terms are

```math
\mathcal D_a\mathcal D_bY^{ij}=-\frac g2\mathcal D_a\mathcal D_bL_c^{ij}+\frac g2L_c^{ij}\mathcal D_a\mathcal D_b\sigma
+\frac i4\left[\overline{\mathcal D_b\psi^i}\mathcal D_a\psi^j+\overline{\mathcal D_a\psi^i}\mathcal D_b\psi^j\right]+\text{high fermi terms}.
\tag{SC7-14}
```

The two spinors stay in their original order; no Grassmann interchange is used. Contracting $`a,b`$ is permitted only after retaining these terms.

For $`T`$, the first derivative of the full identity is

```math
\begin{aligned}
\mathcal D_bT_{cd}={}&\frac1{8\sigma}\mathcal D_b\widehat G_{cd}-\frac1{8\sigma^2}(\mathcal D_b\sigma)\widehat G_{cd}-\frac1{4\sigma^2}\mathcal D_b\widehat H_{cd}+\frac1{2\sigma^3}(\mathcal D_b\sigma)\widehat H_{cd}\\
&+\frac i{32\sigma^2}\left[\overline{\mathcal D_b\psi}\gamma_{cd}\psi+\bar\psi\gamma_{cd}\mathcal D_b\psi\right]-\frac i{16\sigma^3}(\mathcal D_b\sigma)\bar\psi\gamma_{cd}\psi.
\end{aligned}\tag{SC7-15}
```

Differentiating this and then evaluating the gauge gives

```math
\begin{aligned}
\mathcal D_aT_{bc}&=\frac18\mathcal D_a\widehat G_{bc}-\frac14\mathcal D_a\widehat H_{bc},\\
\mathcal D_a\mathcal D_bT_{cd}&=\frac18\mathcal D_a\mathcal D_b\widehat G_{cd}-\frac14\mathcal D_a\mathcal D_b\widehat H_{cd}-\frac18(\mathcal D_a\mathcal D_b\sigma)\widehat G_{cd}+\frac12(\mathcal D_a\mathcal D_b\sigma)\widehat H_{cd}\\
&\quad+\frac i{32}\left[\overline{\mathcal D_b\psi}\gamma_{cd}\mathcal D_a\psi+\overline{\mathcal D_a\psi}\gamma_{cd}\mathcal D_b\psi\right]+\text{high fermi terms}.
\end{aligned}\tag{SC7-16}
```

For the spinor composite, differentiation of the six retained terms in (SC7-07) leaves, on the gauge,

```math
\begin{aligned}
\mathcal D_c\chi^i={}&\frac i8\gamma^a\mathcal D_c\mathcal D_a\psi^i-\frac1{32}\gamma^{ab}\widehat G_{ab}\mathcal D_c\psi^i+\frac14\gamma^{ab}T_{ab}\mathcal D_c\psi^i-\frac g{16}L_c^{ij}\mathcal D_c\psi_j+\frac g8\mathcal D_c\varphi_c^i+\text{high fermi terms}\\
={}&\frac i8\gamma^a\mathcal D_c\mathcal D_a\psi^i-\frac1{16}\gamma^{ab}\widehat H_{ab}\mathcal D_c\psi^i-\frac g{16}L_c^{ij}\mathcal D_c\psi_j+\frac g8\mathcal D_c\varphi_c^i+\text{high fermi terms}.
\end{aligned}\tag{SC7-17}
```

The $`\widehat G`$ coefficient cancels because $`-1/32+(1/4)(1/8)=0`$. The second and third terms in the last line would be lost by differentiating only the gauge value in (SC7-08). The subscript c on $`\varphi_c,L_c`$ labels the independent compensator, while a derivative index $`c`$ is a tangent index.

For $`\mathcal D_eD`$, the scalar product-rule contributions from the two fermionic terms in (SC7-07) are

```math
\begin{aligned}
-\frac18\overline{\mathcal D_e\psi}\gamma^a\mathcal D_a\psi-4i\overline{\mathcal D_e\psi}\chi
&=\left(-\frac18+\frac12\right)\overline{\mathcal D_e\psi}\gamma^a\mathcal D_a\psi-\frac{ig}{2}\overline{\mathcal D_e\psi}\varphi_c\\
&=\frac38\overline{\mathcal D_e\psi}\gamma^a\mathcal D_a\psi-\frac{ig}{2}\overline{\mathcal D_e\psi}\varphi_c.
\end{aligned}\tag{SC7-18}
```

The coefficient $`+1/2`$ is $`(-4i)(i/8)`$. The other derivatives of terms containing undifferentiated $`\psi`$ or $`\mathcal D\sigma`$ vanish on this first-derivative evaluation. Differentiating the flux products and $`Y^2`$ gives the complete retained expression

```math
\begin{aligned}
\mathcal D_eD={}&\frac14\mathcal D_e\Box^c\sigma+\frac5{48}\widehat G^{ab}\mathcal D_e\widehat G_{ab}+\frac1{24}\left(\widehat H^{ab}\mathcal D_e\widehat G_{ab}+\widehat G^{ab}\mathcal D_e\widehat H_{ab}\right)-\frac{13}{12}\widehat H^{ab}\mathcal D_e\widehat H_{ab}\\
&+\frac g4\mathcal D_eN_c+\frac{g^2}{8}L_{cij}\mathcal D_eL_c^{ij}+\frac38\overline{\mathcal D_e\psi}\gamma^a\mathcal D_a\psi-\frac{ig}{2}\overline{\mathcal D_e\psi}\varphi_c+\text{high fermi terms}.
\end{aligned}\tag{SC7-19}
```

The superscript $`c`$ in $`\Box^c`$ is its fixed conformal label, not the free derivative index $`e`$. These four product-rule identities are checked against independent explicitly entered expressions with zero exact coefficient residual.

<a id="43-substitute-into-the-log-slots-and-canonicalize"></a>

### Substitute into the LOG slots and canonicalize

Every occurrence of $`Y,T,\chi,D`$, including ordered derivatives of them, is processed by (SC7-07), (SC7-11) and (SC7-12) before applying (SC7-02). There are no explicit gravitino-connection additions to this operation: they already belong to $`\mathcal D`$. For example, the original triplet term $`2\sigma^{-1}\Box^cY^{ij}`$ becomes

```math
2\sigma^{-1}\Box^cY^{ij}|_{\rm gauge}=-g\Box^cL_c^{ij}+gL_c^{ij}\Box^c\sigma+i\overline{\mathcal D_a\psi^i}\mathcal D^a\psi^j.
\tag{SC7-20}
```

Both contracted bilinears in (SC7-14) are identical by dummy relabeling and metric contraction, with no spinor exchange. The coefficient is $`2(i/4)\cdot2=i`$. Other original triplet terms supply the remaining coefficients in §6.1; (SC7-20) is this one input term, not the whole triplet.

Dummy names are then normalized and inverse metrics contracted. Clifford chains use

```math
\gamma^a\gamma^b=\gamma^{ab}+\eta^{ab},\qquad
\gamma^{ab}\gamma^c=\gamma^{abc}+\eta^{bc}\gamma^a-\eta^{ac}\gamma^b,\qquad
\gamma^{abc}=-\frac i2\epsilon^{abcde}\gamma_{de},\quad\gamma^{abcd}=i\epsilon^{abcde}\gamma_e.
\tag{SC7-21}
```

The general recursion and epsilon-pair reductions are canonical CTF-07–CTF-12. The fixed-doublet spinor exchange uses $`\bar u\Gamma_pv=-\tau_p\bar v\Gamma_pu`$, where $`\tau_p=(-1,-1,+1)`$ for ranks $`0,1,2`$. These signs are applied before collecting equal monomials. The curvature trace rules are

```math
\gamma^a\widehat R(Q)_{ab}=0,\qquad
\gamma^{ac}\widehat R(Q)_{ab}=\widehat R(Q)^c{}_b,\qquad
\overline{\widehat R(Q)_{ab}}\gamma^{ac}=-\overline{\widehat R(Q)^c{}_b},\qquad
\widehat R(M)_{acb}{}^c=0.
\tag{SC7-22}
```

The rank-two identity follows from $`\gamma^{ac}=\eta^{ac}-\gamma^c\gamma^a`$; its bar has the rank-two transpose sign. The metric and gamma tensors are covariantly constant, so an ordered full derivative of these zero constraints is also zero. No derivative permutation is used. All four output slots pass a second full algebraic reduction with zero coefficient difference.

<a id="gauge-fixed-derivatives"></a>

<a id="44-gauge-fixed-derivative-dictionary--reference-only"></a>

### Gauge-fixed derivative dictionary — reference only

This section supplies the gauge-evaluated derivatives that were left implicit in (SC7-03). **None of these formulas is inserted into the LOG multiplet or the BF density in §6.** Throughout this section a vertical bar means (SC7-02), after taking the indicated full supercovariant derivatives. The dilatino is $`\psi^i`$; the gravitino is $`\psi_a^i`$. The S connection is $`\phi_a^i`$; the independent compensator spinor is $`\varphi_c^i`$.

**Sources and scope.** First derivatives: Weyl-squared GC14, equivalently master V01–V03 and OP (2.14)–(2.16). Scalar box: Weyl-squared GC16. Connection solutions and transformations: Weyl-squared GC18–GC20 and master R04a–R04c, anchored to W (3.9)–(3.12), (3.20)–(3.21). The Hessians and spinor box below are derived from these definitions. They are off shell, retain two fermions for the scalar and one for the spinor, and use no integration by parts or background equation. Higher omitted degrees are denoted $`+\text{high fermi terms}`$. The truncation is a formal fermion-degree truncation, not a small-curvature approximation.

<!-- ASSERT_CONVENTION: metric_signature=(-,+,+,+,+), gamma_volume=+i, bar=linear Majorana, derivative=full supercovariant mathcal D, derivative_order=preserved, gauge_evaluation=after differentiation -->

<a id="441-first-derivatives-and-the-dirac-derivative"></a>

#### First derivatives and the Dirac derivative

Begin with the ungauge-fixed GC14 formula rather than with the numerical gauge values:

```math
\begin{aligned}
\mathcal D_a\sigma&=(\partial_a-b_a)\sigma-\frac i2\bar\psi_a\psi,\\
\mathcal D_a\psi^i&=e_a{}^\mu\left[\left(\partial_\mu-\frac32b_\mu+\frac14\omega_\mu{}^{cd}\gamma_{cd}\right)\psi^i-V_\mu{}^{ij}\psi_j\right]+\frac14\gamma\!\cdot\!\widehat G\,\psi_a^i+\frac i2\gamma^b\mathcal D_b\sigma\,\psi_a^i+\frac i{4\sigma}\psi_{aj}\bar\psi^i\psi^j-\frac g{2\sigma}L_c^{ij}\psi_{aj}-\sigma\gamma\!\cdot\!T\,\psi_a^i-\sigma\phi_a^i.
\end{aligned}\tag{SC7D-01}
```

Here $`\partial_a=e_a{}^\mu\partial_\mu`$ occurs only inside an explicitly written definition; it does not replace $`\mathcal D_a`$. Substituting the gauge values removes the first bracket, $`\mathcal D_b\sigma`$ and the dilatino bilinear. The flux coefficient is $`\widehat G/4-(\widehat G-2\widehat H)/8=(\widehat G+2\widehat H)/8`$. Thus

```math
\boxed{\left.\mathcal D_a\sigma\right|=0,\qquad \left.\mathcal D_a\psi^i\right|=\frac18\gamma^{bc}(\widehat G_{bc}+2\widehat H_{bc})\psi_a^i-\frac g2L_c^{ij}\psi_{aj}-\phi_a^i.}\tag{SC7D-02}
```

Inserting the gamma-trace constraint solution for $`\phi_a`$ from (SC7-06) gives its explicit curvature form:

```math
\left.\mathcal D_a\psi^i\right|=\frac18\gamma^{bc}(\widehat G_{bc}+2\widehat H_{bc})\psi_a^i-\frac g2L_c^{ij}\psi_{aj}-\frac i3\gamma^b\widehat R'(Q)_{ab}^i+\frac i{24}\gamma_a\gamma^{bc}\widehat R'(Q)_{bc}^i.
\tag{SC7D-03}
```

The prime is essential: the gamma-trace constraint applies to $`\widehat R(Q)`$, not to $`\widehat R'(Q)`$. Contracting the solved connection first gives $`\gamma^a\phi_a=i(1/3-5/24)\gamma^{ab}\widehat R'(Q)_{ab}=i\gamma^{ab}\widehat R'(Q)_{ab}/8`$. Therefore

```math
\boxed{\left.\not{\mathcal D}\psi^i\right|=\frac18\gamma^a\gamma^{bc}(\widehat G_{bc}+2\widehat H_{bc})\psi_a^i-\frac g2L_c^{ij}\gamma^a\psi_{aj}-\frac i8\gamma^{ab}\widehat R'(Q)_{ab}^i.}\tag{SC7D-04}
```

This also gives $`\chi^i=(i/8)(\not{\mathcal D}\psi^i)|+g\varphi_c^i/8`$ in (SC7-08), with no additional projection factor.

<a id="442-scalar-hessian-and-conformal-box"></a>

#### Scalar Hessian and conformal box

The transformations of the first scalar descendant, evaluated only after taking the variation, are

```math
\left.\delta_Q(\epsilon)\mathcal D_b\sigma\right|=\frac i2\bar\epsilon\left.\mathcal D_b\psi\right|+2\bar\epsilon\gamma_b\chi,\qquad
\left.\delta_S(\eta)\mathcal D_b\sigma\right|=0,\qquad
\left.\delta_K(\Lambda_K)\mathcal D_b\sigma\right|=-2\Lambda_{Kb}.
\tag{SC7D-05}
```

The $`2\chi`$ term comes from $`-\sigma\delta_Qb_b`$ in W01; the $`-2\Lambda_{Kb}`$ term comes from the K variation of that same connection. The terms in $`\delta_Qb_b`$ and $`\delta_Q\psi_b`$ proportional to $`\phi_b`$ combine with the spinor derivative in (SC7D-02). The S law before the gauge is proportional to the dilatino and hence vanishes here. These are transformations of the **unfixed descendant**, not supersymmetry transformations tangent to the gauge slice.

The partial, Lorentz and dilatation contributions to the outer derivative of $`\mathcal D_b\sigma`$ vanish on this gauge because its gauge value is identically zero. In (SC7-01) the negative Q variation gives the first two fermionic terms, and the negative K variation gives $`+2f_{ab}`$. Consequently,

```math
\left.\mathcal D_a\mathcal D_b\sigma\right|=2f_{ab}-\frac i2\bar\psi_a\left.\mathcal D_b\psi\right|-2\bar\psi_a\gamma_b\chi
=-\frac13\mathcal R_{ab}+\frac1{24}\eta_{ab}\mathcal R-\frac i2\bar\psi_a\left.\mathcal D_b\psi\right|-\frac i4\bar\psi_a\gamma_b\gamma^c\left.\mathcal D_c\psi\right|-\frac g4\bar\psi_a\gamma_b\varphi_c.
\tag{SC7D-06}
```

The second equality uses both solved composites, $`f_{ab}`$ and $`\chi`$. It does not symmetrize $`a,b`$ or exchange their derivatives. Trace the first equality with $`\eta^{ab}`$ and use $`2f_a{}^a=-\mathcal R/8`$:

```math
\boxed{\left.\Box^c\sigma\right|=-\frac18\mathcal R-\frac i2\bar\psi_a\left.\mathcal D^a\psi\right|-\frac i4\bar\psi_a\gamma^a\gamma^b\left.\mathcal D_b\psi\right|-\frac g4\bar\psi_a\gamma^a\varphi_c.}\tag{SC7D-07}
```

For an expression with no remaining dilatino derivatives, insert (SC7D-02) into these two occurrences. Right lowering gives $`\bar\psi_a{}^i\varepsilon_{ji}L_c^{jk}\psi_{bk}=-L_c^{jk}\bar\psi_{aj}\psi_{bk}`$; this accounts for both negative $`igL_c`$ coefficients below. No two odd fields are interchanged:

```math
\begin{aligned}
\left.\Box^c\sigma\right|={}&-\frac18\mathcal R-\frac i{16}(\widehat G_{bc}+2\widehat H_{bc})\bar\psi_a\gamma^{bc}\psi^a-\frac{ig}{4}L_c^{ij}\bar\psi_{ai}\psi^a{}_j+\frac i2\bar\psi_a\phi^a\\
&-\frac i{32}(\widehat G_{cd}+2\widehat H_{cd})\bar\psi_a\gamma^a\gamma^b\gamma^{cd}\psi_b-\frac{ig}{8}L_c^{ij}\bar\psi_{ai}\gamma^a\gamma^b\psi_{bj}+\frac i4\bar\psi_a\gamma^a\gamma^b\phi_b-\frac g4\bar\psi_a\gamma^a\varphi_c+\text{high fermi terms}.
\end{aligned}\tag{SC7D-08}
```

All $`\phi_a`$ in this reference formula have the solved relation (SC7-06); $`\mathcal R_{ab}`$ is the retained primed curvature contraction. Thus neither introduces an independent field. Equation (SC7D-08) expands the derivative definition only, and is not a replacement performed in §6.

<a id="443-transformations-needed-for-the-spinor-hessian"></a>

#### Transformations needed for the spinor Hessian

At one-fermion order the connection parameters $`\psi_a,\phi_a`$ multiply the **bosonic** Q/S transformations of $`\mathcal D_b\psi`$. It is enough to determine those transformations at degree zero; their degree-two corrections would contribute three fermions. Temporarily keep the source composites $`Y^{ij}=-gL_c^{ij}/2`$ and $`T_{ab}=(\widehat G_{ab}-2\widehat H_{ab})/8`$ visible to show the origin of each term.

The bosonic part of the S-connection variation follows from its defining projector (SC7-06). Varying the primed gravitino curvature first gives

```math
\begin{aligned}
\left.\delta_Q\widehat R'(Q)_{ab}^i\right|_{0}={}&\frac14R_{ab}{}^{cd}(\omega)\gamma_{cd}\epsilon^i-\widehat R(V)_{ab}^{ij}\epsilon_j
+i\left[(\mathcal D_a\gamma\!\cdot\!T)\gamma_b-(\mathcal D_b\gamma\!\cdot\!T)\gamma_a\right]\epsilon^i-\left[\gamma\!\cdot\!T\gamma_a,\gamma\!\cdot\!T\gamma_b\right]\epsilon^i,\\
\left.\delta_Q\phi_b^i\right|_0={}&\frac i3\gamma^c\left.\delta_Q\widehat R'(Q)_{bc}^i\right|_0-\frac i{24}\gamma_b\gamma^{cd}\left.\delta_Q\widehat R'(Q)_{cd}^i\right|_0 .
\end{aligned}\tag{SC7D-09}
```

Here the label $`0`$ counts dynamical fermions, excluding the variation parameter. To obtain the first line, substitute $`\delta_Q\psi_a=(\partial_a+\omega_a\gamma/4-V_a)\epsilon+i\gamma\!\cdot\!T\gamma_a\epsilon`$ into GC18. The terms containing one derivative of $`\epsilon`$ from differentiating $`T\gamma\epsilon`$ cancel those from the explicit $`T\gamma\delta\psi`$ connection; two derivatives leave $`R(\omega)/4-\widehat R(V)`$. The product of the two $`iT`$ terms gives the displayed negative commutator. Frame variations and variations of $`T`$ multiplying a gravitino have two dynamical fermions and are outside this bosonic transformation.

In the second line, the gamma variation likewise multiplies a fermionic curvature and contributes only at degree two. Applying that projector to the curvature, derivative and $`T^2`$ terms separately gives

```math
\begin{aligned}
\left.\delta_Q\phi_b^i\right|_0={}&if_b{}^c\gamma_c\epsilon^i+\frac i{12}\left(\gamma^{cd}\gamma_b-\frac12\gamma_b\gamma^{cd}\right)\widehat R(V)_{cd}^{ij}\epsilon_j\\
&+\frac13\left[\gamma^c\gamma^{de}(\mathcal D_cT_{de})\gamma_b-\gamma^{cd}\mathcal D_bT_{cd}+\gamma_b\gamma^c\mathcal D^dT_{dc}\right]\epsilon^i\\
&+i\left[-\gamma_{bcdef}T^{cd}T^{ef}+8\gamma^cT_c{}^dT_{bd}-2\gamma_bT^{cd}T_{cd}\right]\epsilon^i,\\
\left.\delta_S\phi_b^i\right|_0={}&e_b{}^\mu\left[\left(\partial_\mu+\frac14\omega_\mu{}^{cd}\gamma_{cd}\right)\eta^i-V_\mu{}^{ij}\eta_j\right]+\frac i3\left(8\gamma^cT_{bc}-\gamma_b\gamma\!\cdot\!T\right)\eta^i.
\end{aligned}\tag{SC7D-10}
```

For the $`R(\omega)`$ contraction the trace-free Lorentz curvature drops from this projector, and the Ricci pieces give $`if_b{}^c\gamma_c`$ using (SC7-06). For the other contractions use $`\gamma^{cd}\gamma_b=\gamma_b{}^{cd}-2\delta_b{}^{[c}\gamma^{d]}`$, $`\gamma_b\gamma^{cd}=\gamma_b{}^{cd}+2\delta_b{}^{[c}\gamma^{d]}`$, and (SC7-21). The first identity includes the contracted antisymmetric tensor; in particular $`T_{cd}\gamma^{cd}\gamma_b=T_{cd}\gamma_b{}^{cd}-2T_{bc}\gamma^c`$. These gamma projections are checked componentwise in the verification described in §5. The $`\widehat R(V)`$ coefficient is **positive** in the all-upper triplet notation: the mixed-index version of R04c has a minus sign, and $`\widehat R(V)^i{}_j\epsilon^j=-\widehat R(V)^{ij}\epsilon_j`$ supplies the second minus.

Equation (SC7D-10) is only the bosonic part of the connection variation. It does not replace the full all-order defining variation R04b.

Now vary (SC7D-01). Terms where a bosonic field is varied and then multiplied by a dynamical spinor have degree two and do not enter this step. The ordinary derivative of $`\delta_Q\psi`$ contributes the negative derivative of $`\widehat G/4-T`$ and of $`Y`$. Its terms proportional to a derivative of the parameter cancel against those from $`\delta_Q\psi_b`$. The surviving transformations are

```math
\begin{aligned}
\left.\delta_Q(\epsilon)\mathcal D_b\psi^i\right|_0={}&-\left[\frac14\gamma^{cd}\mathcal D_b\widehat G_{cd}-\gamma^{cd}\mathcal D_bT_{cd}\right]\epsilon^i+\frac g2(\mathcal D_bL_c^{ij})\epsilon_j
+i\left(\frac14\gamma\!\cdot\!\widehat G-\gamma\!\cdot\!T\right)\gamma\!\cdot\!T\gamma_b\epsilon^i-\frac{ig}{2}L_c^{ij}\gamma\!\cdot\!T\gamma_b\epsilon_j-\left.\delta_Q\phi_b^i\right|_0,\\
\left.\delta_S(\eta)\mathcal D_b\psi^i\right|_0={}&-i\left(\frac14\gamma\!\cdot\!\widehat G-\gamma\!\cdot\!T\right)\gamma_b\eta^i+\frac{ig}{2}L_c^{ij}\gamma_b\eta_j-\frac i3\left(8\gamma^cT_{bc}-\gamma_b\gamma\!\cdot\!T\right)\eta^i,\qquad
\left.\delta_K\mathcal D_b\psi^i\right|=0.
\end{aligned}\tag{SC7D-11}
```

For S, the ordinary derivative of $`\delta_S\psi=\sigma\eta`$ cancels the ordinary derivative in $`\delta_S\phi_b`$. The K transformation of this first descendant is proportional to the undifferentiated dilatino and vanishes at the gauge. It is the Q transformation of $`\phi_b`$ that supplies the surviving $`f`$ term below.

<a id="444-full-second-derivative-of-the-dilatino"></a>

#### Full second derivative of the dilatino

For a lower tangent index, the explicit Lorentz connection is $`-\omega_a{}^c{}_b`$. In GC17, $`2\omega_a{}^c{}_{[b}T_{d]c}=-\omega_a{}^c{}_bT_{cd}-\omega_a{}^c{}_dT_{bc}`$ fixes this sign. Therefore, at the declared order,

```math
\begin{aligned}
\left.\mathcal D_a\mathcal D_b\psi^i\right|={}&e_a{}^\mu\left(\partial_\mu+\frac14\omega_\mu{}^{cd}\gamma_{cd}\right)\left[\mathcal D_b\psi^i\right]_{\rm gauge}-\omega_a{}^c{}_b\left.\mathcal D_c\psi^i\right|-V_a{}^{ij}\left.\mathcal D_b\psi_j\right|\\
&+\left[\frac14\gamma^{cd}\mathcal D_b\widehat G_{cd}-\gamma^{cd}\mathcal D_bT_{cd}\right]\psi_a^i-\frac g2(\mathcal D_bL_c^{ij})\psi_{aj}-i\left(\frac14\gamma\!\cdot\!\widehat G-\gamma\!\cdot\!T\right)\gamma\!\cdot\!T\gamma_b\psi_a^i+\frac{ig}{2}L_c^{ij}\gamma\!\cdot\!T\gamma_b\psi_{aj}+if_b{}^c\gamma_c\psi_a^i\\
&+\frac i{12}\left(\gamma^{cd}\gamma_b-\frac12\gamma_b\gamma^{cd}\right)\widehat R(V)_{cd}^{ij}\psi_{aj}+\frac13\left[\gamma^c\gamma^{de}(\mathcal D_cT_{de})\gamma_b-\gamma^{cd}\mathcal D_bT_{cd}+\gamma_b\gamma^c\mathcal D^dT_{dc}\right]\psi_a^i\\
&+i\left[-\gamma_{bcdef}T^{cd}T^{ef}+8\gamma^cT_c{}^dT_{bd}-2\gamma_bT^{cd}T_{cd}\right]\psi_a^i+i\left(\frac14\gamma\!\cdot\!\widehat G-\gamma\!\cdot\!T\right)\gamma_b\phi_a^i-\frac{ig}{2}L_c^{ij}\gamma_b\phi_{aj}+\frac i3\left(8\gamma^cT_{bc}-\gamma_b\gamma\!\cdot\!T\right)\phi_a^i+\text{high fermi terms}.
\end{aligned}\tag{SC7D-12}
```

The first line means a partial derivative of the **known gauge-evaluated expression (SC7D-02)** with its written Lorentz and SU(2) connections. It is not another full $`\mathcal D`$ and is not named with a competing derivative symbol. The remaining lines are exactly $`-\delta_Q(\psi_a)\mathcal D_b\psi-\delta_S(\phi_a)\mathcal D_b\psi`$ from (SC7D-10)–(SC7D-11). This states every contribution of the outer full derivative. The $`\mathcal D\widehat G`$, $`\mathcal DT`$, and $`\mathcal DL_c`$ on those lines retain the same full supercovariant meaning as elsewhere. Replacing their connection-only parts by full derivatives changes the displayed odd result only at degree three, because these differences are bilinear and each is multiplied by a gravitino.

Here is the product-rule content of the first line, without introducing a second derivative notation. Its partial-derivative contribution is

```math
\begin{aligned}
\partial_\mu\left[\mathcal D_b\psi^i\right]_{\rm gauge}={}&\frac18\gamma^{cd}\left[(\partial_\mu\widehat G_{cd}+2\partial_\mu\widehat H_{cd})\psi_b^i+(\widehat G_{cd}+2\widehat H_{cd})\partial_\mu\psi_b^i\right]\\
&-\frac g2\left[(\partial_\mu L_c^{ij})\psi_{bj}+L_c^{ij}\partial_\mu\psi_{bj}\right]-\partial_\mu\phi_b^i.
\end{aligned}\tag{SC7D-13}
```

The remaining three written connections in the first line of (SC7D-12) act on this tensor-spinor's spinor, tangent and doublet indices. They combine with (SC7D-13); neither a derivative of $`\psi^i=0`$ nor a zero scalar derivative has been substituted for that line.

<a id="445-gauge-fixed-spinor-box-with-the-algebraic-composites-inserted"></a>

#### Gauge-fixed spinor box with the algebraic composites inserted

Contract $`a,b`$ in (SC7D-12). The tangent connection gives $`-\eta^{ab}\omega_a{}^c{}_b=\omega_b{}^{bc}`$ after using antisymmetry of the last two connection indices; hence the divergence contains $`+\omega_b{}^{ba}`$. Insert $`T=(\widehat G-2\widehat H)/8`$, $`\mathcal D_bT_{cd}=(\mathcal D_b\widehat G_{cd}-2\mathcal D_b\widehat H_{cd})/8`$ from (SC7-16), and the solved $`f`$ from (SC7-06). The coefficients of the flux-product, mixed-compensator, derivative-flux and flux-square terms are respectively $`-i/64`$, $`ig/16`$, $`1/24`$ and $`i/64`$. This gives the specified box explicitly:

```math
\begin{aligned}
\left.\Box^c\psi^i\right|={}&\left(\partial^a+\omega_b{}^{ba}+\frac14\omega^{a cd}\gamma_{cd}\right)\left[\mathcal D_a\psi^i\right]_{\rm gauge}-V^{aij}\left.\mathcal D_a\psi_j\right|+\frac18\gamma^{cd}\mathcal D_a(\widehat G_{cd}+2\widehat H_{cd})\psi^{ai}-\frac g2(\mathcal D_aL_c^{ij})\psi^a{}_j\\
&-\frac i{64}\gamma^{cd}(\widehat G_{cd}+2\widehat H_{cd})\gamma^{ef}(\widehat G_{ef}-2\widehat H_{ef})\gamma_a\psi^{ai}+\frac{ig}{16}L_c^{ij}\gamma^{cd}(\widehat G_{cd}-2\widehat H_{cd})\gamma_a\psi^a{}_j+i\left(-\frac16\mathcal R_a{}^b+\frac1{48}\delta_a{}^b\mathcal R\right)\gamma_b\psi^{ai}\\
&+\frac i{12}\left(\gamma^{cd}\gamma_a-\frac12\gamma_a\gamma^{cd}\right)\widehat R(V)_{cd}^{ij}\psi^a{}_j+\frac1{24}\left[\gamma^b\gamma^{cd}\mathcal D_b(\widehat G_{cd}-2\widehat H_{cd})\gamma_a-\gamma^{cd}\mathcal D_a(\widehat G_{cd}-2\widehat H_{cd})+\gamma_a\gamma^b\mathcal D^c(\widehat G_{cb}-2\widehat H_{cb})\right]\psi^{ai}\\
&+\frac i{64}\left[-\gamma_{abcde}(\widehat G^{bc}-2\widehat H^{bc})(\widehat G^{de}-2\widehat H^{de})+8\gamma^b(\widehat G_b{}^c-2\widehat H_b{}^c)(\widehat G_{ac}-2\widehat H_{ac})-2\gamma_a(\widehat G^{bc}-2\widehat H^{bc})(\widehat G_{bc}-2\widehat H_{bc})\right]\psi^{ai}\\
&+\frac i8\gamma^{cd}(\widehat G_{cd}+2\widehat H_{cd})\gamma_a\phi^{ai}-\frac{ig}{2}L_c^{ij}\gamma^a\phi_{aj}+\frac i{24}\left[8\gamma^b(\widehat G_{ab}-2\widehat H_{ab})-\gamma_a\gamma^{cd}(\widehat G_{cd}-2\widehat H_{cd})\right]\phi^{ai}+\text{high fermi terms}.
\end{aligned}\tag{SC7D-14}
```

The occurrence $`[\mathcal D_a\psi]_{\rm gauge}`$ on the first line is the explicit field expression (SC7D-02) or (SC7D-03), with its partial derivative expanded in (SC7D-13). It is not an unspecified box or another independent field. Likewise $`\phi_a`$ has (SC7-06), and the curvatures remain compact. Every $`\mathcal D`$ in the formula is full and supercovariant. The gamma products are deliberately factorized with their order fixed; their reduction to the rank-at-most-two Clifford basis agrees with the previously canonicalized derivative calculation. No changes of fermion order or integrations by parts are hidden in (SC7D-14).

<a id="446-inverse-powers-and-higher-ordered-boxes"></a>

#### Inverse powers and higher ordered boxes

The full even product rule gives, before imposing the gauge,

```math
\mathcal D_a\mathcal D_b\sigma^{-n}=n(n+1)\sigma^{-n-2}(\mathcal D_a\sigma)(\mathcal D_b\sigma)-n\sigma^{-n-1}\mathcal D_a\mathcal D_b\sigma.
\tag{SC7D-15}
```

Thus $`\mathcal D_a\sigma^{-n}|=0`$, but the Hessian and box are nonzero in general:

```math
\left.\mathcal D_a\mathcal D_b\sigma^{-n}\right|=-n\left.\mathcal D_a\mathcal D_b\sigma\right|,\qquad \left.\Box^c\sigma^{-n}\right|=-n\left.\Box^c\sigma\right|.
\tag{SC7D-16}
```

For the higher ordered operators already present in §6, the definitions remain

```math
\begin{aligned}
\left.\mathcal D_a\Box^c\sigma\right|&:=\left.\mathcal D_a\mathcal D^b\mathcal D_b\sigma\right|,\qquad
\left.\Box^c\mathcal D_a\sigma\right|:=\left.\mathcal D^b\mathcal D_b\mathcal D_a\sigma\right|,\qquad
\left.(\Box^c)^2\sigma\right|:=\left.\mathcal D^a\mathcal D_a\mathcal D^b\mathcal D_b\sigma\right|,\\
\left.\mathcal D_a\Box^c\psi^i\right|&:=\left.\mathcal D_a\mathcal D^b\mathcal D_b\psi^i\right|,\qquad
\left.\Box^c\mathcal D_a\psi^i\right|:=\left.\mathcal D^b\mathcal D_b\mathcal D_a\psi^i\right|,\qquad
\left.(\not{\mathcal D})^2\psi^i\right|:=\left.\Box^c\psi^i\right|+\frac12\gamma^{ab}\left.[\mathcal D_a,\mathcal D_b]\psi^i\right|.
\end{aligned}\tag{SC7D-17}
```

The first two operators on each line are different. More explicitly, for either scalar or spinor $`\Phi`$, the exact difference is

```math
[\Box^c,\mathcal D_a]\Phi=\mathcal D^b[\mathcal D_b,\mathcal D_a]\Phi+[\mathcal D^b,\mathcal D_a]\mathcal D_b\Phi.
\tag{SC7D-18}
```

Both commutators are the full superconformal commutators of (SC7-01), including their action on the lower tangent index in the second term. Equations (SC7D-17)–(SC7D-18) define the higher ordered operators; they do not claim to be a connection expansion of every third or fourth derivative. Such an expansion is deferred with the implicit fermionic dependence. In particular, one must not apply an ordinary derivative to the **gauge-only equalities** (SC7D-06), (SC7D-08) or (SC7D-14) and regard it as the next full descendant. The parent, unfixed transformation law is needed for that operation.

The entries (SC7D-02)–(SC7D-04), (SC7D-06)–(SC7D-08) and (SC7D-12)–(SC7D-14) are the gauge-fixed first/second derivative dictionary. Their use is optional during a later BF or spectrum calculation; §6 retains its canonical full-supercovariant form.

<a id="5-consistency-checks"></a>

## Consistency Checks

| Component | Original full-derivative terms | After gauged substitutions and gauge evaluation | Canonical terms |
|---|---:|---:|---:|
| Triplet | 59 | 33 | 13 |
| Spinor | 278 | 271 | 94 |
| Scalar | 514 | 663 | 141 |
| Constrained vector | 1332 | 1259 | 373 |

All source and substituted expressions pass the conformal-weight check before fixing the scale. Every collected output passes free/dummy-index, engineering-dimension and parity checks. A repeated full tensor/Clifford/epsilon/constraint reduction gives exactly zero coefficient difference in all four slots. The full triplet is symmetric under exchanging its free doublet indices, with exact zero difference.

The four independently entered product-rule identities (SC7-14), (SC7-16), (SC7-17), (SC7-19) each agree with the full ungauged-identity differentiation and subsequent gauge evaluation with exactly zero rational-coefficient residual. The direct composite-array checks give maximum absolute residual $`3.56\times10^{-15}`$. An additional 107 component/Grassmann samples compare the substituted terms against their canonical reductions; their largest relative residual is $`7.69\times10^{-15}`$. These samples use explicit four-component Clifford matrices, two independent Grassmann generators and tensors satisfying the imposed curvature traces. They test algebraic equality, not nonlinear supersymmetry.

Evidence: [canonicalization](../../../references/source_evidence/log/results/gauged_full_fermionic_log/sources/step7/supercovariant/canonicalization.json), [verification](../../../references/source_evidence/log/results/gauged_full_fermionic_log/sources/step7/supercovariant/verification.json), [reproducible checker](../../../references/source_evidence/log/results/gauged_full_fermionic_log/scripts/verify_log_step7_supercovariant.py). The primitive supercovariant derivative jets are kept ordered in both the derivation and the checker.

### Derivative dictionary scope

Equation (SC7D-06) retains ordered connection indices, including the two-fermion antisymmetric part of the scalar Hessian.

| Object | Engineering dimension after fixing the scale | Matching terms |
|---|---:|---|
| $`\mathcal D_a\psi`$, $`\not{\mathcal D}\psi`$ | $`3/2`$ | flux times gravitino, $`gL_c\psi_a`$, $`\phi_a`$ |
| $`\mathcal D_a\mathcal D_b\sigma`$, $`\Box^c\sigma`$ | $`2`$ | $`\mathcal R_{ab}`$, $`\bar\psi_a\mathcal D_b\psi`$, $`g\bar\psi_a\varphi_c`$ |
| $`\mathcal D_a\mathcal D_b\psi`$, $`\Box^c\psi`$ | $`5/2`$ | derivative of $`\mathcal D\psi`$, curvature times gravitino, two fluxes times gravitino, flux times $`\phi_a`$ |

The scalar formulas have even parity and no free spinor/doublet indices; the spinor formulas have one free $`i`$ and odd parity. Hessians retain the ordered free tangent pair $`a,b`$ until a metric trace is explicitly taken. The only doublet rearrangement in (SC7D-08) was displayed just before that equation. Conjugation is the same linear Majorana bar as §2.

For the purely bosonic specialization, all fermions and $`\phi_a`$ vanish, while $`f`$ need not vanish. Equations (SC7D-03) and (SC7D-06)–(SC7D-14) then give

```math
\left.\mathcal D_a\psi^i\right|_{\rm bos}=0,\qquad \left.\Box^c\psi^i\right|_{\rm bos}=0,\qquad \left.\mathcal D_a\mathcal D_b\sigma\right|_{\rm bos}=-\frac13\mathcal R_{ab}+\frac1{24}\eta_{ab}\mathcal R,\qquad \left.\Box^c\sigma\right|_{\rm bos}=\left(-\frac13+\frac5{24}\right)\mathcal R=-\frac18\mathcal R.
\tag{SC7D-19}
```

On flat bosonic geometry it gives zero. On a flat, fluxless, ungauged bosonic background while retaining linear gravitino fluctuations, (SC7D-02) and (SC7D-14) reduce to $`\mathcal D_a\psi^i|=-\phi_a^i`$ and $`\Box^c\psi^i|=-\partial^a\phi_a^i`$ at one-fermion order: all explicit curvature/flux/compensator coefficients of a gravitino vanish. The limit $`g\to0`$ is regular because every new expression is polynomial in $`g`$; it removes the explicit gauging contributions without removing the dependent S/K connections.

The derivative dictionary uses the same component normalization and BF density as the four-component result. The comparison uses neither integration by parts nor field equations or auxiliary elimination.

The bosonic, flat and ungauged specializations commute with the exact substitutions and algebraic identities when applied to the full defined covariants. In particular a conformal box on the fixed scalar can retain bosonic curvature. Setting every displayed derivative to zero is not a valid bosonic or constant-compensator limit. Section 5.3 supplies the complete bosonic reduction and comparison.

### Covariant component comparison

The comparison uses the same gauge, mostly-plus metric, linear Majorana bar, doublet rules, slot normalization and fermion truncation. It tests local equality without integration by parts, field equations or derivative interchange.

First undo the gauged composite map (SC7-07) algebraically before evaluating the gauge. For example, write $`Y=Y_{\rm rem}-gL_c/(2\sigma)`$ and $`\chi=\chi_{\rm rem}+g\varphi_c/(8\sigma^2)`$, where each remainder contains every other retained term in its defining identity. The triangular inverse is

```math
L_c=-\frac{2\sigma}{g}(Y-Y_{\rm rem}),\qquad \widehat H=-4\sigma^2(T-T_{\rm rem}),\qquad \varphi_c=\frac{8\sigma^2}{g}(\chi-\chi_{\rm rem}),\qquad N_c=\frac{4\sigma^2}{g}(D-D_{\rm rem}).
\tag{SC7A-01}
```

Here the suppressed indices are those of the corresponding full identities in (SC7-07). Invert the remainders recursively, apply their ordered derivatives, then impose the elementary gauge values. Although this intermediate inverse is written for $`g\ne0`$, every inverse power of $`g`$ cancels from every compared component. Equality is consequently a polynomial identity and extends to $`g=0`$. The dilaton remains on the original nonzero patch until the gauge evaluation.

Subtract the corresponding unfixed component after the same elementary gauge evaluation. Reduce only by source-valid tensor and Clifford identities, six-index antisymmetrization in five dimensions, and the conventional $`R(Q)`$ gamma-trace constraint. For the latter, an arbitrary antisymmetric spinor tensor $`U_{ab}`$ can parameterize every allowed curvature:

```math
\Phi_a(U)=\frac i3\gamma^bU_{ab}-\frac i{24}\gamma_a\gamma^{bc}U_{bc},\qquad (\Pi U)_{ab}=U_{ab}-i\gamma_a\Phi_b(U)+i\gamma_b\Phi_a(U),\qquad \gamma^a(\Pi U)_{ab}=0.
\tag{SC7A-02}
```

This is the solved conventional constraint already used in (SC7-06), not an extra field equation. If $`U`$ is gamma-traceless, $`\Phi(U)=0`$ and $`\Pi U=U`$, so the projector loses no allowed curvature. Indeed, with $`v_b=\gamma^aU_{ab}`$ and $`A=\gamma^{ab}U_{ab}`$, one has $`\Phi_b=-iv_b/3-i\gamma_bA/24`$, $`\gamma^b\Phi_b=iA/8`$, and $`\gamma^a(\Pi U)_{ab}=v_b-3i\Phi_b-i\gamma_b\gamma^a\Phi_a=0`$.

| Component | Residual monomials after the first tensor/Clifford reduction | Additional exact reduction | Final coefficient residual |
|---|---:|---|---:|
| $`L_{\log}^{ij}`$ | 0 | none | 0 |
| $`\varphi_{\log}^{i}`$ | 5 | five-dimensional Schouten identities | 0 |
| $`N_{\log}`$ | 9 | $`R(Q)`$ projector and Schouten identities | 0 |
| $`E_{\log}^{a}`$ | 57 | $`R(Q)`$ projector and Schouten identities | 0 |

These are exact rational-complex polynomial comparisons, not numerical samples or equality of term counts. Neither side of this decisive comparison contains an expanded $`f_{ab}`$, primed Ricci tensor or explicit S connection. The [comparison script](../../../references/source_evidence/log/results/gauged_full_fermionic_log/scripts/verify_log_derivative_equivalence_covariant.py), [projector reduction](../../../references/source_evidence/log/results/gauged_full_fermionic_log/scripts/verify_log_derivative_equivalence_projector.py), [common-basis evidence](component_construction/EXTERNAL_REFERENCES.md#ref-c5ab3f5b5b46) and [derivation of the equivalence test](component_construction/EXTERNAL_REFERENCES.md#ref-19dd58a1d5f6) record the inputs and reductions. The inverse uses the same algebraic map as the forward construction; its coefficient correctness is checked separately by the [independent ungauged-template test](../../../references/source_evidence/log/results/gauged_full_fermionic_log/scripts/verify_log_ungauged_composite_templates.py), which retains a nonconstant dilaton and a nonzero dilatino and passes 21 matrix/Grassmann comparisons with maximum relative residual $`3.50\times10^{-15}`$.

The full dependent connection and primed Ricci tensor retain their ordered indices, including their antisymmetric fermion bilinears.

Define $`J_{ab}=\bar\psi_a\gamma_b\chi`$. In the independent $`\chi`$ sector the weighted antisymmetrizations give

```math
\left.\widehat R'_{acbd}(M)\right|_{\chi}=2(\eta_{cb}J_{ad}-\eta_{cd}J_{ab}-\eta_{ab}J_{cd}+\eta_{ad}J_{cb}),\qquad
\left.\mathcal R_{ab}\right|_{\chi}=-6J_{ab}-2\eta_{ab}J_c{}^c,\qquad \left.\mathcal R\right|_{\chi}=-16J_c{}^c.
\tag{SC7A-03}
```

Inserting these two contractions into (SC7-06) gives

```math
\left.f_{ab}\right|_{\chi}=-\frac16(-6J_{ab}-2\eta_{ab}J_c{}^c)+\frac1{48}\eta_{ab}(-16J_c{}^c)=J_{ab},\qquad
\left.f_{[ab]}\right|_{\chi}=\bar\psi_{[a}\gamma_{b]}\chi.
\tag{SC7A-04}
```

This term survives at two fermions. It is not removed by the dilatino gauge, since the gravitino and compensator spinor inside $`\chi`$ remain.
<a id="53-source-repair-and-expanded-certification-25-september-2026"></a>

### Component verification

The source-local super-Jacobi identity fixes the two K-generator coefficients in C24 (A.1l) to $`+i/8,-i/4`$. These coefficients are used in the scalar and vector descents. Substitution, ordered differentiation, gauge evaluation and canonicalization give the four gauged polynomials in §6 with 13, 94, 141 and 373 terms. Derivatives of the gauge-fixed dilatino and scalar remain as defined covariants.

All corrected unfixed and gauged canonical components pass the [exact coefficient-phase reality check](../../../references/source_evidence/log/results/gauged_full_fermionic_log/sources/certification_20260925/canonical/reality_phase_after_correction.json). The independent [complete displayed-polynomial evaluation](../../../references/source_evidence/log/results/gauged_full_fermionic_log/sources/certification_20260925/canonical/all_terms_seed_926255_rho_1_printed.json) covers all 179,396 Step 6 terms; this numerical cross-check is additional evidence, not an unrestricted proof by sampling or a claim about every internal floating-point contraction.

The [full superform reconstruction](../../../references/source_evidence/log/derivations/form-interface.md) closes the generic current, potential and BF interface. The complete [bosonic comparison](../../../references/source_evidence/log/derivations/bosonic.md) reproduces LOG-CORR05 including flux, derivative and compensator terms, with the explicit boundary current retained. The [certification report](component_construction/results/gauged_full_fermionic_log/CERTIFICATION_LOG_TWO_FERMI_2026-09-25.md) records the separate curved-primary, defining-projector and retained-order supersymmetry gates.

<a id="6-final-result"></a>

## Final Result

All four sums below have the algebraic composites substituted, retain full supercovariant curvatures and derivatives, and obey the gauge-evaluation convention after (SC7-02). They are collected by **explicit** fermion degree. The outer projection counts implicit fermions in every strength, derivative and curvature as well:

```math
\left[\prod_rB_r\right]_{\le2}=\prod_rB_r^{(0)}+\sum_sB_s^{(2)}\prod_{r\ne s}B_r^{(0)},\qquad
[B\bar u\Gamma v]_{\le2}=B^{(0)}\overline{u^{(1)}}\Gamma v^{(1)},\qquad [Bu]_{\le2}=B^{(0)}u^{(1)}.
\tag{SC7-23}
```

Each consecutive display under a component/degree heading continues the same sum; two summands are printed per row. $`\widehat G^2=\widehat G_{ab}\widehat G^{ab}`$; $`L_c^{ij}L_{cij}=L^2`$. The ordered descendants of the fixed dilaton/dilatino are intentional defined covariants and must not be set to zero.

<!-- SUPERCOVARIANT_COMPONENTS_BEGIN -->

<a id="61-triplet"></a>

### Triplet

```math
\boxed{L_{\log}^{ij}=\left[L_{\log}^{ij}[0]+L_{\log}^{ij}[2]\right]_{\le2}+\text{high fermi terms}.}\tag{SC7-44}
```

#### Triplet: 0 explicit fermions

```math
\begin{aligned}
L_{\log}^{ij}[0]={}&-\frac{1}{3}\widehat R(V){}^{a}{}^{b}{}^{i}{}^{j}\widehat G{}_{a}{}_{b} -\frac{4}{3}\widehat H{}^{a}{}^{b}\widehat R(V){}_{a}{}_{b}{}^{i}{}^{j}\\
&-gL_c{}^{i}{}^{j}\big(\Box^c \sigma\big) -\frac{1}{2}gL_c{}^{i}{}^{j}\widehat G^2\\
&-g^{3}L_c{}^{i}{}^{j}L_c{}^{k}{}^{l}L_c{}_{k}{}_{l} +6g\widehat H{}^{a}{}^{b}\widehat H{}_{a}{}_{b}L_c{}^{i}{}^{j}\\
&-3N_cg^{2}L_c{}^{i}{}^{j} -g\big(\Box^c L_c{}^{i}{}^{j}\big)
\end{aligned}
\tag{SC7-LF0}
```

#### Triplet: 2 explicit fermions

```math
\begin{aligned}
L_{\log}^{ij}[2]={}&-\frac{5i}{6}\overline{\big(\mathcal D_{a}\psi{}^{i}\big)}\gamma{}^{a}{}^{b}\big(\mathcal D_{b}\psi{}^{j}\big) +\frac{2i}{3}\overline{\big(\mathcal D^{a}\psi{}^{i}\big)}\big(\mathcal D_{a}\psi{}^{j}\big)\\
&-\frac{11}{6}g\overline{\varphi_c{}^{j}}\gamma{}^{a}\big(\mathcal D_{a}\psi{}^{i}\big) -\frac{11}{6}g\overline{\varphi_c{}^{i}}\gamma{}^{a}\big(\mathcal D_{a}\psi{}^{j}\big)\\
&+\frac{17i}{6}g^{2}\overline{\varphi_c{}^{i}}\varphi_c{}^{j}
\end{aligned}
\tag{SC7-LF2}
```

<a id="62-spinor"></a>

### Spinor

```math
\boxed{\varphi_{\log}^{i}=\left[\varphi_{\log}^{i}[1]\right]_{\le2}+\text{high fermi terms}.}\tag{SC7-45}
```

#### Spinor: 1 explicit fermions

```math
\begin{aligned}
\varphi_{\log}^{i}[1]={}&\frac{1}{6}\widehat R(V){}^{a}{}^{b}{}^{i}{}^{j}\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\gamma{}^{c}{}^{d}\big(\mathcal D^{e}\psi{}_{j}\big) -\frac{i}{3}\widehat R(V){}^{a}{}^{b}{}^{i}{}^{j}\gamma{}_{a}\big(\mathcal D_{b}\psi{}_{j}\big)\\
&+\frac{1}{3}g\widehat R(V){}^{a}{}^{b}{}^{i}{}^{j}\gamma{}_{a}{}_{b}\varphi_c{}_{j} +\frac{1}{144}\widehat G{}_{a}{}_{b}\widehat G{}_{c}{}_{d}\gamma{}^{c}{}^{d}\widehat R(Q){}^{a}{}^{b}{}^{i}\\
&+\frac{1}{36}\widehat H{}^{a}{}^{b}\widehat G{}_{c}{}_{d}\gamma{}_{a}{}_{b}\widehat R(Q){}^{c}{}^{d}{}^{i} -\frac{7}{72}\widehat H{}^{a}{}^{b}\widehat G{}_{c}{}_{d}\gamma{}^{c}{}^{d}\widehat R(Q){}_{a}{}_{b}{}^{i}\\
&-\frac{7}{18}\widehat H{}^{a}{}^{b}\widehat H{}^{c}{}^{d}\gamma{}_{c}{}_{d}\widehat R(Q){}_{a}{}_{b}{}^{i} -\frac{2i}{3}\widehat H{}^{a}{}^{b}\widehat G{}_{a}{}_{b}\gamma{}^{c}\big(\mathcal D_{c}\psi{}^{i}\big)\\
&-\frac{1}{4}g\widehat G^2\varphi_c{}^{i} -\frac{2}{3}g\widehat H{}^{a}{}^{b}\widehat G{}_{a}{}_{b}\varphi_c{}^{i}\\
&+\frac{5}{2}g\widehat H{}^{a}{}^{b}\widehat H{}_{a}{}_{b}\varphi_c{}^{i} -\frac{5i}{16}\widehat G{}_{b}{}_{c}\gamma{}_{a}\big(\mathcal D^{a}\widehat R(Q){}^{b}{}^{c}{}^{i}\big)\\
&-\frac{5i}{4}\widehat H{}^{a}{}^{b}\gamma{}_{c}\big(\mathcal D^{c}\widehat R(Q){}_{a}{}_{b}{}^{i}\big) +\widehat H{}^{a}{}^{b}\widehat G{}_{b}{}_{c}\widehat R(Q){}_{a}{}^{c}{}^{i}\\
&-\frac{1}{24}\widehat G{}_{a}{}_{c}\widehat G{}_{b}{}_{d}\gamma{}^{c}{}^{d}\widehat R(Q){}^{a}{}^{b}{}^{i} -\frac{1}{12}\widehat H{}^{a}{}^{b}\widehat G{}_{c}{}_{d}\gamma{}_{b}{}^{d}\widehat R(Q){}_{a}{}^{c}{}^{i}\\
&+\frac{1}{3}\widehat H{}^{a}{}^{b}\widehat H{}^{c}{}^{d}\gamma{}_{b}{}_{d}\widehat R(Q){}_{a}{}_{c}{}^{i} -\frac{3}{16}\widehat G{}^{c}{}^{d}\widehat G{}^{e}{}^{f}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\gamma{}^{a}{}^{b}\big(\mathcal D_{a}\psi{}^{i}\big)\\
&+\frac{1}{16}\widehat G{}^{a}{}^{b}\widehat G{}^{c}{}^{d}\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\big(\mathcal D^{e}\psi{}^{i}\big) +\frac{1}{2}\widehat H{}^{a}{}^{b}\widehat G{}^{e}{}^{f}\epsilon{}_{a}{}_{b}{}_{d}{}_{e}{}_{f}\gamma{}^{c}{}^{d}\big(\mathcal D_{c}\psi{}^{i}\big)\\
&+\frac{2}{3}\widehat H{}^{a}{}^{b}\widehat H{}^{c}{}^{d}\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{f}\gamma{}^{e}{}^{f}\big(\mathcal D_{e}\psi{}^{i}\big) -\frac{3i}{16}g\widehat G{}^{b}{}^{c}\widehat G{}^{d}{}^{e}\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\gamma{}^{a}\varphi_c{}^{i}\\
&+\frac{i}{2}g\widehat H{}^{a}{}^{b}\widehat G{}^{d}{}^{e}\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\gamma{}^{c}\varphi_c{}^{i} +\frac{i}{4}g\widehat H{}^{a}{}^{b}\widehat H{}^{c}{}^{d}\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\gamma{}^{e}\varphi_c{}^{i}\\
&-\frac{1}{32}\widehat G{}^{d}{}^{e}\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\big(\mathcal D^{a}\widehat R(Q){}^{b}{}^{c}{}^{i}\big) -\frac{1}{8}\widehat H{}^{a}{}^{b}\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\big(\mathcal D^{c}\widehat R(Q){}^{d}{}^{e}{}^{i}\big)\\
&-\frac{1}{32}\widehat G{}^{e}{}^{f}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\gamma{}^{c}{}^{d}\big(\mathcal D^{a}\widehat R(Q){}_{a}{}^{b}{}^{i}\big) -\frac{1}{8}\widehat H{}^{a}{}^{b}\epsilon{}_{a}{}_{b}{}_{d}{}_{e}{}_{f}\gamma{}^{e}{}^{f}\big(\mathcal D^{c}\widehat R(Q){}_{c}{}^{d}{}^{i}\big)\\
&-\frac{1}{32}\widehat G{}_{a}{}^{f}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\gamma{}^{d}{}^{e}\big(\mathcal D^{a}\widehat R(Q){}^{b}{}^{c}{}^{i}\big) -\frac{1}{8}\widehat H{}^{a}{}^{b}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\gamma{}^{e}{}^{f}\big(\mathcal D_{a}\widehat R(Q){}^{c}{}^{d}{}^{i}\big)\\
&-\frac{1}{16}\widehat G{}_{b}{}^{f}\epsilon{}_{a}{}_{c}{}_{d}{}_{e}{}_{f}\gamma{}^{d}{}^{e}\big(\mathcal D^{a}\widehat R(Q){}^{b}{}^{c}{}^{i}\big) -\frac{1}{4}\widehat H{}^{a}{}^{b}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\gamma{}^{e}{}^{f}\big(\mathcal D^{c}\widehat R(Q){}_{a}{}^{d}{}^{i}\big)\\
&-\frac{i}{8}\widehat G{}_{b}{}_{c}\gamma{}^{c}\big(\mathcal D^{a}\widehat R(Q){}_{a}{}^{b}{}^{i}\big) +\frac{i}{2}\widehat H{}^{a}{}^{b}\gamma{}_{b}\big(\mathcal D^{c}\widehat R(Q){}_{a}{}_{c}{}^{i}\big)\\
&+\frac{4}{3}\widehat H{}^{a}{}^{b}\gamma{}_{a}{}^{c}\big(\mathcal D_{c}\mathcal D_{b}\psi{}^{i}\big) -\frac{2i}{3}\widehat H{}^{a}{}^{b}\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\gamma{}^{c}\big(\mathcal D^{d}\mathcal D^{e}\psi{}^{i}\big)
\end{aligned}
\tag{SC7-phiF1-1}
```

```math
\begin{aligned}
&-\frac{8i}{3}\widehat H{}^{a}{}^{b}\widehat H{}_{a}{}^{c}\gamma{}_{b}\big(\mathcal D_{c}\psi{}^{i}\big) -g\widehat H{}^{a}{}^{b}L_c{}^{i}{}^{j}\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\gamma{}^{c}{}^{d}\big(\mathcal D^{e}\psi{}_{j}\big)\\
&+\frac{1}{2}g\widehat H{}^{a}{}^{b}\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\gamma{}^{d}{}^{e}\big(\mathcal D^{c}\varphi_c{}^{i}\big) +\frac{1}{24}\widehat H{}^{a}{}^{b}\widehat G{}^{e}{}^{f}\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{f}\gamma{}^{c}{}^{d}\big(\mathcal D_{e}\psi{}^{i}\big)\\
&+\frac{2i}{3}\widehat H{}^{a}{}^{b}\widehat G{}_{b}{}^{c}\gamma{}_{a}\big(\mathcal D_{c}\psi{}^{i}\big) +\frac{i}{6}gL_c{}^{i}{}^{j}\widehat G{}_{a}{}^{b}\gamma{}^{a}\big(\mathcal D_{b}\psi{}_{j}\big)\\
&+\frac{8i}{3}g\widehat H{}^{a}{}^{b}L_c{}^{i}{}^{j}\gamma{}_{a}\big(\mathcal D_{b}\psi{}_{j}\big) -\frac{2i}{3}g\widehat G{}_{a}{}_{b}\gamma{}^{b}\big(\mathcal D^{a}\varphi_c{}^{i}\big)\\
&+\frac{4i}{3}g\widehat H{}^{a}{}^{b}\gamma{}_{b}\big(\mathcal D_{a}\varphi_c{}^{i}\big) +\frac{5i}{6}\big(\Box^c \sigma\big)\gamma{}^{a}\big(\mathcal D_{a}\psi{}^{i}\big)\\
&+\frac{5}{6}g\big(\Box^c \sigma\big)\varphi_c{}^{i} +\frac{11i}{24}g^{2}L_c{}^{j}{}^{k}L_c{}_{j}{}_{k}\gamma{}^{a}\big(\mathcal D_{a}\psi{}^{i}\big)\\
&-\frac{7}{24}g^{3}L_c{}^{j}{}^{k}L_c{}_{j}{}_{k}\varphi_c{}^{i} +\frac{11i}{6}N_cg\gamma{}^{a}\big(\mathcal D_{a}\psi{}^{i}\big)\\
&-\frac{1}{6}N_cg^{2}\varphi_c{}^{i} +\frac{13}{12}\big(\mathcal D^{c}\widehat G{}_{a}{}_{b}\big)\gamma{}^{a}{}^{b}\big(\mathcal D_{c}\psi{}^{i}\big)\\
&+\frac{5}{3}\big(\mathcal D_{a}\widehat G{}_{b}{}^{c}\big)\gamma{}^{a}{}^{b}\big(\mathcal D_{c}\psi{}^{i}\big) +\frac{7i}{12}\big(\mathcal D^{b}\widehat G{}^{c}{}^{d}\big)\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\gamma{}^{a}\big(\mathcal D^{e}\psi{}^{i}\big)\\
&+\frac{1}{3}\big(\mathcal D^{a}\widehat H{}^{b}{}^{c}\big)\gamma{}_{b}{}_{c}\big(\mathcal D_{a}\psi{}^{i}\big) -\frac{4}{3}\big(\mathcal D^{a}\widehat H{}^{b}{}^{c}\big)\gamma{}_{a}{}_{b}\big(\mathcal D_{c}\psi{}^{i}\big)\\
&+\frac{i}{6}\big(\mathcal D^{a}\widehat H{}^{b}{}^{c}\big)\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\gamma{}^{d}\big(\mathcal D^{e}\psi{}^{i}\big) -\frac{13}{24}g\big(\mathcal D^{c}\widehat G{}^{d}{}^{e}\big)\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\gamma{}^{a}{}^{b}\varphi_c{}^{i}\\
&+\frac{7}{12}g\big(\mathcal D^{a}\widehat H{}^{b}{}^{c}\big)\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\gamma{}^{d}{}^{e}\varphi_c{}^{i} -\frac{1}{3}\big(\mathcal D^{c}\widehat G{}_{a}{}_{c}\big)\gamma{}^{a}{}^{b}\big(\mathcal D_{b}\psi{}^{i}\big)\\
&-\frac{1}{6}\big(\mathcal D^{a}\widehat G{}_{a}{}^{b}\big)\big(\mathcal D_{b}\psi{}^{i}\big) -\frac{8}{3}\big(\mathcal D^{a}\widehat H{}_{a}{}^{b}\big)\gamma{}_{b}{}^{c}\big(\mathcal D_{c}\psi{}^{i}\big)\\
&-\frac{5}{3}\big(\mathcal D^{a}\widehat H{}_{a}{}^{b}\big)\big(\mathcal D_{b}\psi{}^{i}\big) +\frac{5i}{6}g\big(\mathcal D^{b}\widehat G{}_{a}{}_{b}\big)\gamma{}^{a}\varphi_c{}^{i}\\
&+\frac{11i}{3}g\big(\mathcal D^{a}\widehat H{}_{a}{}^{b}\big)\gamma{}_{b}\varphi_c{}^{i} -2gL_c{}^{i}{}^{j}\gamma{}^{a}{}^{b}\big(\mathcal D_{a}\mathcal D_{b}\psi{}_{j}\big)\\
&-gL_c{}^{i}{}^{j}\big(\Box^c \psi{}_{j}\big) -\frac{5i}{4}g^{2}L_c{}^{i}{}^{j}L_c{}_{j}{}^{k}\gamma{}^{a}\big(\mathcal D_{a}\psi{}_{k}\big)\\
&+2ig^{2}L_c{}^{i}{}^{j}\gamma{}_{a}\big(\mathcal D^{a}\varphi_c{}_{j}\big) +\frac{i}{4}\widehat H{}^{a}{}^{b}\widehat G{}^{e}{}^{f}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\gamma{}^{d}\widehat R(Q){}_{a}{}^{c}{}^{i}\\
&-\frac{i}{4}\widehat H{}^{a}{}^{b}\widehat G{}_{a}{}^{f}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\gamma{}^{e}\widehat R(Q){}^{c}{}^{d}{}^{i} +\frac{i}{8}\widehat H{}^{a}{}^{b}\widehat G{}_{c}{}^{f}\epsilon{}_{a}{}_{b}{}_{d}{}_{e}{}_{f}\gamma{}^{e}\widehat R(Q){}^{c}{}^{d}{}^{i}
\end{aligned}
\tag{SC7-phiF1-2}
```

```math
\begin{aligned}
&-\frac{5i}{2}\big(\mathcal D_{b}\mathcal D_{a}\sigma\big)\gamma{}^{a}\big(\mathcal D^{b}\psi{}^{i}\big) +\frac{1}{2}g\big(\mathcal D^{a}L_c{}^{i}{}^{j}\big)\big(\mathcal D_{a}\psi{}_{j}\big)\\
&-g\big(\Box^c \varphi_c{}^{i}\big) -\frac{i}{6}\widehat G{}^{b}{}^{c}\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\gamma{}^{a}\big(\mathcal D^{d}\mathcal D^{e}\psi{}^{i}\big)\\
&+\frac{1}{3}\widehat G{}_{a}{}^{c}\gamma{}^{a}{}^{b}\big(\mathcal D_{b}\mathcal D_{c}\psi{}^{i}\big) -g\big(\mathcal D^{a}L_c{}^{i}{}^{j}\big)\gamma{}_{a}{}^{b}\big(\mathcal D_{b}\psi{}_{j}\big)\\
&+ig^{2}\big(\mathcal D^{a}L_c{}^{i}{}^{j}\big)\gamma{}_{a}\varphi_c{}_{j} +\frac{i}{2}\widehat G{}_{a}{}^{b}\widehat G{}_{b}{}^{c}\gamma{}^{a}\big(\mathcal D_{c}\psi{}^{i}\big)\\
&+i\widehat H{}^{a}{}^{b}\widehat G{}_{a}{}_{c}\gamma{}^{c}\big(\mathcal D_{b}\psi{}^{i}\big) +\frac{23i}{576}gL_c{}^{i}{}^{j}\widehat G{}^{d}{}^{e}\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\gamma{}^{c}\widehat R(Q){}^{a}{}^{b}{}_{j}\\
&-\frac{11i}{288}g\widehat H{}^{a}{}^{b}L_c{}^{i}{}^{j}\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\gamma{}^{e}\widehat R(Q){}^{c}{}^{d}{}_{j} -\frac{1}{288}gL_c{}^{i}{}^{j}\widehat G{}_{a}{}_{b}\widehat R(Q){}^{a}{}^{b}{}_{j}\\
&-\frac{59}{144}g\widehat H{}^{a}{}^{b}L_c{}^{i}{}^{j}\widehat R(Q){}_{a}{}_{b}{}_{j} +\frac{1}{2}\big(\mathcal D^{d}\mathcal D^{e}\sigma\big)\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\gamma{}^{a}{}^{b}\big(\mathcal D^{c}\psi{}^{i}\big)\\
&+i\big(\mathcal D_{a}\mathcal D_{b}\sigma\big)\gamma{}^{a}\big(\mathcal D^{b}\psi{}^{i}\big) +g\big(\mathcal D_{a}\mathcal D_{b}\sigma\big)\gamma{}^{a}{}^{b}\varphi_c{}^{i}\\
&+\frac{1}{12}\widehat H{}^{a}{}^{b}\widehat G{}_{a}{}^{e}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\gamma{}^{c}{}^{d}\big(\mathcal D^{f}\psi{}^{i}\big) -\frac{1}{12}\widehat H{}^{a}{}^{b}\widehat G{}^{e}{}^{f}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\gamma{}^{c}{}^{d}\big(\mathcal D_{a}\psi{}^{i}\big)\\
&+\frac{1}{4}\widehat H{}^{a}{}^{b}\widehat G{}_{c}{}^{e}\epsilon{}_{a}{}_{b}{}_{d}{}_{e}{}_{f}\gamma{}^{c}{}^{d}\big(\mathcal D^{f}\psi{}^{i}\big) +\frac{1}{8}gL_c{}^{i}{}^{j}\widehat G{}^{c}{}^{d}\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\gamma{}^{a}{}^{b}\big(\mathcal D^{e}\psi{}_{j}\big)\\
&+\frac{1}{4}g^{2}L_c{}^{i}{}^{j}\widehat G{}_{a}{}_{b}\gamma{}^{a}{}^{b}\varphi_c{}_{j} -\frac{1}{6}\widehat H{}^{a}{}^{b}\widehat G{}^{d}{}^{e}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\gamma{}_{a}{}^{c}\big(\mathcal D^{f}\psi{}^{i}\big)
\end{aligned}
\tag{SC7-phiF1-3}
```

<a id="63-scalar"></a>

### Scalar

```math
\boxed{N_{\log}=\left[N_{\log}[0]+N_{\log}[2]\right]_{\le2}+\text{high fermi terms}.}\tag{SC7-46}
```

#### Scalar: 0 explicit fermions

```math
\begin{aligned}
N_{\log}[0]={}&\frac{1}{6}\widehat R(V){}^{a}{}^{b}{}^{i}{}^{j}\widehat R(V){}_{a}{}_{b}{}_{i}{}_{j} +\frac{17}{144}\widehat C{}^{a}{}^{b}{}^{c}{}^{d}\widehat G{}_{a}{}_{b}\widehat G{}_{c}{}_{d}\\
&+\frac{23}{72}\widehat H{}^{a}{}^{b}\widehat C{}_{a}{}_{b}{}^{c}{}^{d}\widehat G{}_{c}{}_{d} -\frac{11}{18}\widehat H{}^{a}{}^{b}\widehat H{}^{c}{}^{d}\widehat C{}_{a}{}_{b}{}_{c}{}_{d}\\
&+\frac{11}{72}\widehat C{}^{a}{}^{b}{}^{c}{}^{d}\widehat G{}_{a}{}_{c}\widehat G{}_{b}{}_{d} +\frac{17}{36}\widehat H{}^{a}{}^{b}\widehat C{}_{a}{}^{c}{}_{b}{}^{d}\widehat G{}_{c}{}_{d}\\
&-\frac{5}{9}\widehat H{}^{a}{}^{b}\widehat H{}^{c}{}^{d}\widehat C{}_{a}{}_{c}{}_{b}{}_{d} +\frac{1}{16}(\widehat G^2)^{2}\\
&-\widehat H{}^{a}{}^{b}\widehat G{}_{a}{}_{b}\widehat G^2 +\widehat H{}^{a}{}^{b}\widehat H{}_{a}{}_{b}\widehat G^2\\
&+\frac{4}{3}\widehat H{}^{a}{}^{b}\widehat H{}^{c}{}^{d}\widehat G{}_{a}{}_{b}\widehat G{}_{c}{}_{d} -2\widehat H{}^{a}{}^{b}\widehat H{}_{a}{}_{b}\widehat H{}^{c}{}^{d}\widehat H{}_{c}{}_{d}\\
&+\frac{1}{12}\widehat G{}^{a}{}^{b}\widehat G{}^{c}{}^{d}\big(\mathcal D^{e}\widehat G{}_{e}{}^{f}\big)\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{f} +\frac{1}{3}\big(\mathcal D^{a}\widehat H{}_{a}{}^{b}\big)\widehat G{}^{c}{}^{d}\widehat G{}^{e}{}^{f}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\\
&-\frac{863}{1152}\widehat H{}^{a}{}^{b}\widehat G{}^{c}{}^{d}\big(\mathcal D^{e}\widehat G{}_{e}{}^{f}\big)\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{f} -\frac{1129}{576}\widehat H{}^{a}{}^{b}\big(\mathcal D^{c}\widehat H{}_{c}{}^{d}\big)\widehat G{}^{e}{}^{f}\epsilon{}_{a}{}_{b}{}_{d}{}_{e}{}_{f}\\
&+\frac{1}{3}\widehat H{}^{a}{}^{b}\widehat H{}^{c}{}^{d}\big(\mathcal D^{e}\widehat G{}_{e}{}^{f}\big)\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{f} +\frac{4}{3}\widehat H{}^{a}{}^{b}\widehat H{}^{c}{}^{d}\big(\mathcal D^{e}\widehat H{}_{e}{}^{f}\big)\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{f}\\
&-\frac{4}{3}\widehat H{}^{a}{}^{b}\widehat G{}_{a}{}_{b}\big(\Box^c \sigma\big) +\frac{1}{8}g^{2}L_c{}^{i}{}^{j}L_c{}_{i}{}_{j}\widehat G^2\\
&-\frac{1}{3}g^{2}\widehat H{}^{a}{}^{b}L_c{}^{i}{}^{j}L_c{}_{i}{}_{j}\widehat G{}_{a}{}_{b} +2g^{2}\widehat H{}^{a}{}^{b}\widehat H{}_{a}{}_{b}L_c{}^{i}{}^{j}L_c{}_{i}{}_{j}\\
&+\frac{1}{2}N_cg\widehat G^2 -\frac{4}{3}N_cg\widehat H{}^{a}{}^{b}\widehat G{}_{a}{}_{b}\\
&+2N_cg\widehat H{}^{a}{}^{b}\widehat H{}_{a}{}_{b} -\frac{3}{32}\big(\mathcal D^{a}\widehat C{}_{a}{}^{b}{}^{c}{}^{d}\big)\widehat G{}^{e}{}^{f}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\\
&-\frac{3}{8}\widehat H{}^{a}{}^{b}\big(\mathcal D^{c}\widehat C{}_{c}{}^{d}{}^{e}{}^{f}\big)\epsilon{}_{a}{}_{b}{}_{d}{}_{e}{}_{f} -\frac{1}{16}\big(\mathcal D^{a}\widehat C{}^{b}{}^{c}{}^{d}{}^{e}\big)\widehat G{}_{b}{}^{f}\epsilon{}_{a}{}_{c}{}_{d}{}_{e}{}_{f}\\
&-\frac{1}{4}\widehat H{}^{a}{}^{b}\big(\mathcal D^{c}\widehat C{}_{a}{}^{d}{}^{e}{}^{f}\big)\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f} -\frac{1}{16}\big(\mathcal D^{a}\widehat C{}^{b}{}^{c}{}^{d}{}^{e}\big)\widehat G{}_{a}{}^{f}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\\
&-\frac{1}{4}\widehat H{}^{a}{}^{b}\big(\mathcal D_{a}\widehat C{}^{c}{}^{d}{}^{e}{}^{f}\big)\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f} -\frac{4}{3}\widehat G{}^{a}{}^{b}\widehat G{}_{a}{}^{c}\big(\mathcal D_{b}\mathcal D_{c}\sigma\big)\\
&+\frac{2}{9}\widehat G{}^{a}{}^{b}\big(\mathcal D_{a}\mathcal D^{c}\widehat G{}_{b}{}_{c}\big) -\frac{28}{9}\widehat H{}^{a}{}^{b}\widehat G{}_{a}{}^{c}\big(\mathcal D_{c}\mathcal D_{b}\sigma\big)\\
&+\frac{28}{9}\big(\mathcal D^{a}\mathcal D^{b}\widehat H{}_{b}{}^{c}\big)\widehat G{}_{a}{}_{c} +\frac{28}{9}\widehat H{}^{a}{}^{b}\widehat G{}_{a}{}^{c}\big(\mathcal D_{b}\mathcal D_{c}\sigma\big)
\end{aligned}
\tag{SC7-NF0-1}
```

```math
\begin{aligned}
&+\frac{8}{9}\widehat H{}^{a}{}^{b}\big(\mathcal D_{a}\mathcal D^{c}\widehat G{}_{b}{}_{c}\big) -\frac{8}{3}\widehat H{}^{a}{}^{b}\widehat H{}_{a}{}^{c}\big(\mathcal D_{b}\mathcal D_{c}\sigma\big)\\
&+\frac{32}{9}\widehat H{}^{a}{}^{b}\big(\mathcal D_{a}\mathcal D^{c}\widehat H{}_{b}{}_{c}\big) +\frac{1}{3}\widehat G{}^{a}{}^{b}\big(\Box^c \widehat G{}_{a}{}_{b}\big)\\
&+\frac{4}{3}\widehat H{}^{a}{}^{b}\big(\Box^c \widehat G{}_{a}{}_{b}\big) +\frac{1}{9}\widehat G{}^{a}{}^{b}\big(\mathcal D^{c}\mathcal D_{a}\widehat G{}_{b}{}_{c}\big)\\
&+\frac{2}{9}\big(\mathcal D^{a}\mathcal D^{b}\widehat H{}_{a}{}^{c}\big)\widehat G{}_{b}{}_{c} +\frac{4}{9}\widehat H{}^{a}{}^{b}\big(\mathcal D^{c}\mathcal D_{a}\widehat G{}_{b}{}_{c}\big)\\
&-\frac{8}{9}\widehat H{}^{a}{}^{b}\big(\mathcal D^{c}\mathcal D_{a}\widehat H{}_{b}{}_{c}\big) +\frac{5}{6}\big(\Box^c \sigma\big)\big(\Box^c \sigma\big)\\
&+\frac{5}{3}g^{2}L_c{}^{i}{}^{j}L_c{}_{i}{}_{j}\big(\Box^c \sigma\big) +\frac{8}{3}N_cg\big(\Box^c \sigma\big)\\
&-\frac{17}{48}g^{4}L_c{}^{i}{}^{j}L_c{}_{i}{}_{j}L_c{}^{k}{}^{l}L_c{}_{k}{}_{l} -\frac{5}{6}N_cg^{3}L_c{}^{i}{}^{j}L_c{}_{i}{}_{j}\\
&-\frac{1}{6}N_cN_cg^{2} +\frac{5}{6}\big(\mathcal D^{a}\widehat G{}^{b}{}^{c}\big)\big(\mathcal D_{b}\widehat G{}_{a}{}_{c}\big)\\
&-\frac{7}{3}\big(\mathcal D^{a}\widehat H{}^{b}{}^{c}\big)\big(\mathcal D_{b}\widehat G{}_{a}{}_{c}\big) +\frac{4}{3}\big(\mathcal D^{a}\widehat H{}^{b}{}^{c}\big)\big(\mathcal D_{b}\widehat H{}_{a}{}_{c}\big)\\
&-\frac{1}{3}\big(\mathcal D^{a}\widehat G{}^{b}{}^{c}\big)\big(\mathcal D_{a}\widehat G{}_{b}{}_{c}\big) +\frac{11}{6}\big(\mathcal D^{a}\widehat H{}^{b}{}^{c}\big)\big(\mathcal D_{a}\widehat G{}_{b}{}_{c}\big)\\
&+\frac{2}{3}\big(\mathcal D^{a}\widehat H{}^{b}{}^{c}\big)\big(\mathcal D_{a}\widehat H{}_{b}{}_{c}\big) -2\big(\mathcal D^{a}\widehat H{}_{a}{}^{b}\big)\big(\mathcal D^{c}\widehat G{}_{b}{}_{c}\big)\\
&+4\big(\mathcal D^{a}\widehat H{}_{a}{}^{b}\big)\big(\mathcal D^{c}\widehat H{}_{b}{}_{c}\big) -\frac{1}{2}gL_c{}^{i}{}^{j}\widehat R(V){}^{a}{}^{b}{}_{i}{}_{j}\widehat G{}_{a}{}_{b}\\
&-\frac{1163}{1152}\widehat H{}^{a}{}^{b}\widehat G{}^{c}{}^{d}\big(\mathcal D_{c}\widehat G{}^{e}{}^{f}\big)\epsilon{}_{a}{}_{b}{}_{d}{}_{e}{}_{f} +\frac{563}{576}\widehat H{}^{a}{}^{b}\big(\mathcal D^{c}\widehat H{}^{d}{}^{e}\big)\widehat G{}_{c}{}^{f}\epsilon{}_{a}{}_{b}{}_{d}{}_{e}{}_{f}\\
&+\frac{269}{576}\widehat H{}^{a}{}^{b}\widehat G{}_{a}{}^{c}\big(\mathcal D^{d}\widehat G{}^{e}{}^{f}\big)\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f} -\frac{139}{288}\widehat H{}^{a}{}^{b}\big(\mathcal D^{c}\widehat H{}^{d}{}^{e}\big)\widehat G{}_{a}{}^{f}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\\
&+\frac{3}{16}\widehat H{}^{a}{}^{b}\widehat G{}^{c}{}^{d}\big(\mathcal D^{e}\widehat G{}_{c}{}^{f}\big)\epsilon{}_{a}{}_{b}{}_{d}{}_{e}{}_{f} +\frac{19}{24}\widehat H{}^{a}{}^{b}\big(\mathcal D^{c}\widehat H{}^{d}{}^{e}\big)\widehat G{}_{d}{}^{f}\epsilon{}_{a}{}_{b}{}_{c}{}_{e}{}_{f}\\
&-\frac{353}{576}\widehat H{}^{a}{}^{b}\widehat G{}^{c}{}^{d}\big(\mathcal D^{e}\widehat G{}_{a}{}^{f}\big)\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f} +\frac{89}{288}\widehat H{}^{a}{}^{b}\big(\mathcal D^{c}\widehat H{}_{a}{}^{d}\big)\widehat G{}^{e}{}^{f}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\\
&-\frac{7}{64}\widehat H{}^{a}{}^{b}\widehat G{}^{c}{}^{d}\big(\mathcal D_{a}\widehat G{}^{e}{}^{f}\big)\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f} -\frac{25}{32}\widehat H{}^{a}{}^{b}\big(\mathcal D_{a}\widehat H{}^{c}{}^{d}\big)\widehat G{}^{e}{}^{f}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\\
&-g^{2}L_c{}^{i}{}^{j}\big(\Box^c L_c{}_{i}{}_{j}\big) -\frac{3}{4}\big(\mathcal D^{a}\widehat G{}^{b}{}^{c}\big)\big(\mathcal D^{d}\mathcal D^{e}\sigma\big)\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}
\end{aligned}
\tag{SC7-NF0-2}
```

```math
\begin{aligned}
&+\frac{3}{2}\big(\mathcal D^{a}\widehat H{}^{b}{}^{c}\big)\big(\mathcal D^{d}\mathcal D^{e}\sigma\big)\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e} -\frac{3}{2}\big(\mathcal D^{a}\mathcal D^{b}\sigma\big)\big(\mathcal D_{a}\mathcal D_{b}\sigma\big)\\
&-\frac{3}{4}g^{2}\big(\mathcal D^{a}L_c{}^{i}{}^{j}\big)\big(\mathcal D_{a}L_c{}_{i}{}_{j}\big) -g\big(\Box^c N_c\big)\\
&-\frac{3}{8}\widehat G{}^{a}{}^{b}\widehat G{}_{a}{}^{c}\widehat G{}_{b}{}^{d}\widehat G{}_{c}{}_{d} +2\widehat H{}^{a}{}^{b}\widehat G{}_{a}{}^{c}\widehat G{}_{b}{}^{d}\widehat G{}_{c}{}_{d}\\
&-4\widehat H{}^{a}{}^{b}\widehat H{}_{a}{}^{c}\widehat G{}_{b}{}^{d}\widehat G{}_{c}{}_{d} +\frac{1}{8}g^{4}L_c{}^{i}{}^{j}L_c{}_{i}{}^{k}L_c{}_{j}{}^{l}L_c{}_{k}{}_{l}
\end{aligned}
\tag{SC7-NF0-3}
```

#### Scalar: 2 explicit fermions

```math
\begin{aligned}
N_{\log}[2]={}&\frac{685i}{6144}\widehat G{}^{e}{}^{f}\epsilon{}_{a}{}_{b}{}_{d}{}_{e}{}_{f}\overline{\widehat R(Q){}^{a}{}^{b}{}^{i}}\gamma{}^{c}{}^{d}\big(\mathcal D_{c}\psi{}_{i}\big) -\frac{2125i}{18432}\widehat G{}^{c}{}^{d}\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\widehat R(Q){}^{a}{}^{b}{}^{i}}\big(\mathcal D^{e}\psi{}_{i}\big)\\
&+\frac{379i}{3072}\widehat H{}^{a}{}^{b}\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{f}\overline{\widehat R(Q){}^{c}{}^{d}{}^{i}}\gamma{}^{e}{}^{f}\big(\mathcal D_{e}\psi{}_{i}\big) -\frac{1211i}{9216}\widehat H{}^{a}{}^{b}\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\widehat R(Q){}^{c}{}^{d}{}^{i}}\big(\mathcal D^{e}\psi{}_{i}\big)\\
&-\frac{2651}{18432}g\widehat G{}^{d}{}^{e}\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\widehat R(Q){}^{a}{}^{b}{}^{i}}\gamma{}^{c}\varphi_c{}_{i} -\frac{541}{9216}g\widehat H{}^{a}{}^{b}\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\widehat R(Q){}^{c}{}^{d}{}^{i}}\gamma{}^{e}\varphi_c{}_{i}\\
&-\frac{607i}{18432}\widehat G{}_{a}{}^{e}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\widehat R(Q){}^{a}{}^{b}{}^{i}}\gamma{}^{c}{}^{d}\big(\mathcal D^{f}\psi{}_{i}\big) -\frac{289}{576}\widehat G{}_{a}{}_{c}\overline{\widehat R(Q){}^{a}{}^{b}{}^{i}}\gamma{}^{c}\big(\mathcal D_{b}\psi{}_{i}\big)\\
&+\frac{65i}{9216}\widehat H{}^{a}{}^{b}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\widehat R(Q){}_{a}{}^{c}{}^{i}}\gamma{}^{d}{}^{e}\big(\mathcal D^{f}\psi{}_{i}\big) +\frac{11}{144}\widehat H{}^{a}{}^{b}\overline{\widehat R(Q){}_{a}{}^{c}{}^{i}}\gamma{}_{b}\big(\mathcal D_{c}\psi{}_{i}\big)\\
&+\frac{859i}{9216}g\widehat G{}_{a}{}_{b}\overline{\widehat R(Q){}^{a}{}^{b}{}^{i}}\varphi_c{}_{i} +\frac{6173i}{4608}g\widehat H{}^{a}{}^{b}\overline{\widehat R(Q){}_{a}{}_{b}{}^{i}}\varphi_c{}_{i}\\
&-\frac{209}{9216}\widehat G{}_{a}{}_{b}\overline{\widehat R(Q){}^{a}{}^{b}{}^{i}}\gamma{}^{c}\big(\mathcal D_{c}\psi{}_{i}\big) -\frac{8167}{4608}\widehat H{}^{a}{}^{b}\overline{\widehat R(Q){}_{a}{}_{b}{}^{i}}\gamma{}^{c}\big(\mathcal D_{c}\psi{}_{i}\big)\\
&-\frac{1}{8}\widehat G{}^{b}{}^{c}\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\big(\mathcal D^{d}\psi{}^{i}\big)}\gamma{}^{a}\big(\mathcal D^{e}\psi{}_{i}\big) -\frac{i}{4}\widehat G{}_{a}{}_{b}\overline{\big(\mathcal D^{c}\psi{}^{i}\big)}\gamma{}^{a}{}^{b}\big(\mathcal D_{c}\psi{}_{i}\big)\\
&-\frac{i}{12}\widehat G{}_{a}{}^{c}\overline{\big(\mathcal D_{b}\psi{}^{i}\big)}\gamma{}^{a}{}^{b}\big(\mathcal D_{c}\psi{}_{i}\big) -\frac{3i}{2}\widehat G{}^{a}{}^{b}\overline{\big(\mathcal D_{a}\psi{}^{i}\big)}\big(\mathcal D_{b}\psi{}_{i}\big)\\
&+\frac{1}{12}\widehat H{}^{a}{}^{b}\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\big(\mathcal D^{d}\psi{}^{i}\big)}\gamma{}^{c}\big(\mathcal D^{e}\psi{}_{i}\big) +\frac{i}{6}\widehat H{}^{a}{}^{b}\overline{\big(\mathcal D_{b}\psi{}^{i}\big)}\gamma{}_{a}{}^{c}\big(\mathcal D_{c}\psi{}_{i}\big)\\
&-\frac{5i}{6}\widehat H{}^{a}{}^{b}\overline{\big(\mathcal D^{c}\psi{}^{i}\big)}\gamma{}_{a}{}_{b}\big(\mathcal D_{c}\psi{}_{i}\big) +\frac{2i}{3}\widehat H{}^{a}{}^{b}\overline{\big(\mathcal D_{a}\psi{}^{i}\big)}\big(\mathcal D_{b}\psi{}_{i}\big)\\
&-\frac{i}{4}g\widehat G{}^{c}{}^{d}\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\varphi_c{}^{i}}\gamma{}^{a}{}^{b}\big(\mathcal D^{e}\psi{}_{i}\big) -\frac{1}{2}g\widehat G{}_{a}{}^{b}\overline{\varphi_c{}^{i}}\gamma{}^{a}\big(\mathcal D_{b}\psi{}_{i}\big)\\
&+\frac{19i}{24}g\widehat H{}^{a}{}^{b}\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\varphi_c{}^{i}}\gamma{}^{c}{}^{d}\big(\mathcal D^{e}\psi{}_{i}\big) +\frac{1}{6}g\widehat H{}^{a}{}^{b}\overline{\varphi_c{}^{i}}\gamma{}_{a}\big(\mathcal D_{b}\psi{}_{i}\big)\\
&-\frac{3i}{8}g^{2}\widehat G{}_{a}{}_{b}\overline{\varphi_c{}^{i}}\gamma{}^{a}{}^{b}\varphi_c{}_{i} +\frac{3i}{4}g^{2}\widehat H{}^{a}{}^{b}\overline{\varphi_c{}^{i}}\gamma{}_{a}{}_{b}\varphi_c{}_{i}\\
&-\frac{81i}{256}\overline{\big(\mathcal D^{a}\widehat R(Q){}_{a}{}^{b}{}^{i}\big)}\big(\mathcal D_{b}\psi{}_{i}\big) +\frac{111}{512}\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\big(\mathcal D^{a}\widehat R(Q){}^{b}{}^{c}{}^{i}\big)}\gamma{}^{d}\big(\mathcal D^{e}\psi{}_{i}\big)\\
&-\frac{153i}{1024}g\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\big(\mathcal D^{a}\widehat R(Q){}^{b}{}^{c}{}^{i}\big)}\gamma{}^{d}{}^{e}\varphi_c{}_{i} -\frac{i}{12}\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\big(\mathcal D^{c}\psi{}^{i}\big)}\gamma{}^{a}{}^{b}\big(\mathcal D^{d}\mathcal D^{e}\psi{}_{i}\big)\\
&+\frac{5}{6}\overline{\big(\mathcal D_{a}\psi{}^{i}\big)}\gamma{}^{a}\big(\Box^c \psi{}_{i}\big) -\frac{1}{6}\overline{\big(\mathcal D^{b}\psi{}^{i}\big)}\gamma{}^{a}\big(\mathcal D_{a}\mathcal D_{b}\psi{}_{i}\big)\\
&-\frac{4}{3}\overline{\big(\mathcal D^{b}\psi{}^{i}\big)}\gamma{}^{a}\big(\mathcal D_{b}\mathcal D_{a}\psi{}_{i}\big) +\frac{i}{3}gL_c{}^{i}{}^{j}\overline{\big(\mathcal D_{a}\psi{}_{i}\big)}\gamma{}^{a}{}^{b}\big(\mathcal D_{b}\psi{}_{j}\big)
\end{aligned}
\tag{SC7-NF2-1}
```

```math
\begin{aligned}
&+\frac{10i}{3}gL_c{}^{i}{}^{j}\overline{\big(\mathcal D^{a}\psi{}_{i}\big)}\big(\mathcal D_{a}\psi{}_{j}\big) +\frac{5i}{6}g\overline{\big(\mathcal D^{a}\varphi_c{}^{i}\big)}\gamma{}_{a}{}^{b}\big(\mathcal D_{b}\psi{}_{i}\big)\\
&-\frac{13i}{6}g\overline{\big(\mathcal D^{a}\varphi_c{}^{i}\big)}\big(\mathcal D_{a}\psi{}_{i}\big) +\frac{5i}{6}g\overline{\varphi_c{}^{i}}\gamma{}^{a}{}^{b}\big(\mathcal D_{a}\mathcal D_{b}\psi{}_{i}\big)\\
&-\frac{5i}{6}g\overline{\varphi_c{}^{i}}\big(\Box^c \psi{}_{i}\big) +\frac{13}{12}g^{2}L_c{}^{i}{}^{j}\overline{\varphi_c{}_{i}}\gamma{}^{a}\big(\mathcal D_{a}\psi{}_{j}\big)\\
&+\frac{1}{6}g^{2}\overline{\varphi_c{}^{i}}\gamma{}_{a}\big(\mathcal D^{a}\varphi_c{}_{i}\big) -\frac{19i}{64}\widehat G{}_{b}{}_{c}\overline{\widehat R(Q){}^{a}{}^{b}{}^{i}}\widehat R(Q){}_{a}{}^{c}{}_{i}\\
&-\frac{19i}{16}\widehat H{}^{a}{}^{b}\overline{\widehat R(Q){}_{a}{}^{c}{}^{i}}\widehat R(Q){}_{b}{}_{c}{}_{i} +\frac{15}{512}\widehat G{}_{a}{}^{f}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\widehat R(Q){}^{a}{}^{b}{}^{i}}\gamma{}^{e}\widehat R(Q){}^{c}{}^{d}{}_{i}\\
&+\frac{15}{128}\widehat H{}^{a}{}^{b}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\widehat R(Q){}_{a}{}^{c}{}^{i}}\gamma{}^{f}\widehat R(Q){}^{d}{}^{e}{}_{i} +\frac{3}{256}\widehat G{}^{e}{}^{f}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\widehat R(Q){}^{a}{}^{b}{}^{i}}\gamma{}^{d}\widehat R(Q){}_{a}{}^{c}{}_{i}\\
&+\frac{3}{64}\widehat H{}^{a}{}^{b}\epsilon{}_{a}{}_{b}{}_{d}{}_{e}{}_{f}\overline{\widehat R(Q){}^{c}{}^{d}{}^{i}}\gamma{}^{f}\widehat R(Q){}_{c}{}^{e}{}_{i} -\frac{9i}{1024}\widehat G{}_{c}{}_{d}\overline{\widehat R(Q){}^{a}{}^{b}{}^{i}}\gamma{}^{c}{}^{d}\widehat R(Q){}_{a}{}_{b}{}_{i}\\
&-\frac{9i}{256}\widehat H{}^{a}{}^{b}\overline{\widehat R(Q){}^{c}{}^{d}{}^{i}}\gamma{}_{a}{}_{b}\widehat R(Q){}_{c}{}_{d}{}_{i} +\frac{355i}{2304}gL_c{}^{i}{}^{j}\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\widehat R(Q){}^{a}{}^{b}{}_{i}}\gamma{}^{c}{}^{d}\big(\mathcal D^{e}\psi{}_{j}\big)\\
&+\frac{131i}{1152}\widehat G{}^{e}{}^{f}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\widehat R(Q){}^{a}{}^{b}{}^{i}}\gamma{}^{c}{}^{d}\big(\mathcal D_{a}\psi{}_{i}\big) -\frac{95i}{576}\widehat H{}^{a}{}^{b}\epsilon{}_{a}{}_{b}{}_{d}{}_{e}{}_{f}\overline{\widehat R(Q){}^{c}{}^{d}{}^{i}}\gamma{}^{e}{}^{f}\big(\mathcal D_{c}\psi{}_{i}\big)\\
&+\frac{4999i}{36864}\widehat G{}^{e}{}^{f}\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{f}\overline{\widehat R(Q){}^{a}{}^{b}{}^{i}}\gamma{}^{c}{}^{d}\big(\mathcal D_{e}\psi{}_{i}\big) -\frac{3271i}{18432}\widehat H{}^{a}{}^{b}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\widehat R(Q){}^{c}{}^{d}{}^{i}}\gamma{}^{e}{}^{f}\big(\mathcal D_{a}\psi{}_{i}\big)\\
&+\frac{117i}{2048}\widehat G{}_{c}{}^{e}\epsilon{}_{a}{}_{b}{}_{d}{}_{e}{}_{f}\overline{\widehat R(Q){}^{a}{}^{b}{}^{i}}\gamma{}^{c}{}^{d}\big(\mathcal D^{f}\psi{}_{i}\big) +\frac{69i}{1024}\widehat H{}^{a}{}^{b}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\widehat R(Q){}^{c}{}^{d}{}^{i}}\gamma{}_{a}{}^{e}\big(\mathcal D^{f}\psi{}_{i}\big)\\
&-\frac{i}{64}g\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\widehat R(Q){}^{a}{}^{b}{}^{i}}\gamma{}^{d}{}^{e}\big(\mathcal D^{c}\varphi_c{}_{i}\big) -\frac{i}{1024}gL_c{}^{i}{}^{j}\overline{\widehat R(Q){}^{a}{}^{b}{}_{i}}\widehat R(Q){}_{a}{}_{b}{}_{j}\\
&+\frac{1}{2048}gL_c{}^{i}{}^{j}\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\widehat R(Q){}^{a}{}^{b}{}_{i}}\gamma{}^{e}\widehat R(Q){}^{c}{}^{d}{}_{j}
\end{aligned}
\tag{SC7-NF2-2}
```

<a id="64-constrained-vector"></a>

### Constrained vector

```math
\boxed{E_{\log}^{a}=\left[E_{\log}^{a}[0]+E_{\log}^{a}[2]\right]_{\le2}+\text{high fermi terms}.}\tag{SC7-47}
```

#### Constrained vector: 0 explicit fermions

```math
\begin{aligned}
E_{\log}^{a}[0]={}&-\frac{1}{12}\widehat R(V){}^{b}{}^{c}{}^{i}{}^{j}\widehat R(V){}^{d}{}^{e}{}_{i}{}_{j}\epsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{e} -\frac{1}{128}\widehat C{}^{b}{}^{c}{}^{d}{}^{e}\widehat G{}^{a}{}^{f}\widehat G{}_{b}{}^{g}\epsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g}\\
&+\frac{3}{8}\widehat H{}^{b}{}^{c}\widehat C{}_{b}{}^{d}{}^{e}{}^{f}\widehat G{}^{a}{}^{g}\epsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g} +\frac{21}{64}\widehat H{}^{a}{}^{b}\widehat C{}^{c}{}^{d}{}^{e}{}^{f}\widehat G{}_{c}{}^{g}\epsilon{}_{b}{}_{d}{}_{e}{}_{f}{}_{g}\\
&+\frac{5}{16}\widehat H{}^{a}{}^{b}\widehat H{}^{c}{}^{d}\widehat C{}_{c}{}^{e}{}^{f}{}^{g}\epsilon{}_{b}{}_{d}{}_{e}{}_{f}{}_{g} +\frac{25}{768}\widehat C{}^{b}{}^{c}{}^{d}{}^{e}\widehat G{}^{a}{}_{b}\widehat G{}^{f}{}^{g}\epsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g}\\
&+\frac{11}{96}\widehat H{}^{b}{}^{c}\widehat C{}^{d}{}^{e}{}^{f}{}^{g}\widehat G{}^{a}{}_{d}\epsilon{}_{b}{}_{c}{}_{e}{}_{f}{}_{g} -\frac{31}{384}\widehat H{}^{a}{}^{b}\widehat C{}_{b}{}^{c}{}^{d}{}^{e}\widehat G{}^{f}{}^{g}\epsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g}\\
&-\frac{37}{96}\widehat H{}^{a}{}^{b}\widehat H{}^{c}{}^{d}\widehat C{}_{b}{}^{e}{}^{f}{}^{g}\epsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g} +\frac{1}{192}\widehat C{}^{b}{}^{c}{}^{d}{}^{e}\widehat G{}^{a}{}^{f}\widehat G{}_{f}{}^{g}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{g}\\
&-\frac{5}{192}\widehat H{}^{b}{}^{c}\widehat C{}^{d}{}^{e}{}^{f}{}^{g}\widehat G{}^{a}{}_{b}\epsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g} +\frac{7}{192}\widehat H{}^{a}{}^{b}\widehat C{}^{c}{}^{d}{}^{e}{}^{f}\widehat G{}_{b}{}^{g}\epsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g}\\
&-\frac{1}{24}\widehat H{}^{a}{}^{b}\widehat H{}_{b}{}^{c}\widehat C{}^{d}{}^{e}{}^{f}{}^{g}\epsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g} -\frac{41}{576}\widehat C{}^{b}{}^{c}{}^{d}{}^{e}\widehat G{}_{b}{}^{f}\widehat G{}_{d}{}^{g}\epsilon{}^{a}{}_{c}{}_{e}{}_{f}{}_{g}\\
&-\frac{29}{288}\widehat H{}^{b}{}^{c}\widehat C{}_{b}{}^{d}{}^{e}{}^{f}\widehat G{}_{e}{}^{g}\epsilon{}^{a}{}_{c}{}_{d}{}_{f}{}_{g} +\frac{53}{72}\widehat H{}^{b}{}^{c}\widehat H{}^{d}{}^{e}\widehat C{}_{b}{}^{f}{}_{d}{}^{g}\epsilon{}^{a}{}_{c}{}_{e}{}_{f}{}_{g}\\
&-\frac{31}{1152}\widehat C{}^{b}{}^{c}{}^{d}{}^{e}\widehat G{}_{b}{}_{d}\widehat G{}^{f}{}^{g}\epsilon{}^{a}{}_{c}{}_{e}{}_{f}{}_{g} +\frac{59}{288}\widehat H{}^{b}{}^{c}\widehat C{}^{d}{}^{e}{}^{f}{}^{g}\widehat G{}_{d}{}_{f}\epsilon{}^{a}{}_{b}{}_{c}{}_{e}{}_{g}\\
&-\frac{161}{576}\widehat H{}^{b}{}^{c}\widehat C{}_{b}{}^{d}{}_{c}{}^{e}\widehat G{}^{f}{}^{g}\epsilon{}^{a}{}_{d}{}_{e}{}_{f}{}_{g} +\frac{19}{144}\widehat H{}^{b}{}^{c}\widehat H{}^{d}{}^{e}\widehat C{}_{b}{}^{f}{}_{c}{}^{g}\epsilon{}^{a}{}_{d}{}_{e}{}_{f}{}_{g}\\
&-\frac{1}{1152}\widehat C{}^{b}{}^{c}{}^{d}{}^{e}\widehat G{}_{b}{}_{c}\widehat G{}^{f}{}^{g}\epsilon{}^{a}{}_{d}{}_{e}{}_{f}{}_{g} +\frac{23}{1152}\widehat H{}^{b}{}^{c}\widehat C{}^{d}{}^{e}{}^{f}{}^{g}\widehat G{}_{d}{}_{e}\epsilon{}^{a}{}_{b}{}_{c}{}_{f}{}_{g}\\
&+\frac{23}{1152}\widehat H{}^{b}{}^{c}\widehat C{}_{b}{}_{c}{}^{d}{}^{e}\widehat G{}^{f}{}^{g}\epsilon{}^{a}{}_{d}{}_{e}{}_{f}{}_{g} +\frac{25}{144}\widehat H{}^{b}{}^{c}\widehat H{}^{d}{}^{e}\widehat C{}_{b}{}_{c}{}^{f}{}^{g}\epsilon{}^{a}{}_{d}{}_{e}{}_{f}{}_{g}\\
&-\frac{43}{576}\widehat C{}^{b}{}^{c}{}^{d}{}^{e}\widehat G{}_{b}{}^{f}\widehat G{}_{f}{}^{g}\epsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{g} +\frac{29}{144}\widehat H{}^{b}{}^{c}\widehat C{}^{d}{}^{e}{}^{f}{}^{g}\widehat G{}_{b}{}_{d}\epsilon{}^{a}{}_{c}{}_{e}{}_{f}{}_{g}\\
&-\frac{149}{288}\widehat H{}^{b}{}^{c}\widehat C{}_{b}{}^{d}{}^{e}{}^{f}\widehat G{}_{c}{}^{g}\epsilon{}^{a}{}_{d}{}_{e}{}_{f}{}_{g} -\frac{5}{72}\widehat H{}^{b}{}^{c}\widehat H{}_{b}{}^{d}\widehat C{}_{c}{}^{e}{}^{f}{}^{g}\epsilon{}^{a}{}_{d}{}_{e}{}_{f}{}_{g}\\
&+\frac{35}{2304}\widehat C{}^{b}{}^{c}{}^{d}{}^{e}\epsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{e}\widehat G^2 +\frac{59}{1152}\widehat H{}^{b}{}^{c}\widehat C{}^{d}{}^{e}{}^{f}{}^{g}\widehat G{}_{b}{}_{c}\epsilon{}^{a}{}_{d}{}_{e}{}_{f}{}_{g}\\
&-\frac{11}{288}\widehat H{}^{b}{}^{c}\widehat H{}_{b}{}_{c}\widehat C{}^{d}{}^{e}{}^{f}{}^{g}\epsilon{}^{a}{}_{d}{}_{e}{}_{f}{}_{g} +\frac{5}{576}\widehat C{}^{b}{}^{c}{}^{d}{}^{e}\widehat G{}_{b}{}^{f}\widehat G{}_{c}{}^{g}\epsilon{}^{a}{}_{d}{}_{e}{}_{f}{}_{g}\\
&+\frac{29}{288}\widehat H{}^{b}{}^{c}\widehat C{}_{b}{}^{d}{}^{e}{}^{f}\widehat G{}_{d}{}^{g}\epsilon{}^{a}{}_{c}{}_{e}{}_{f}{}_{g} +\frac{19}{72}\widehat H{}^{b}{}^{c}\widehat H{}^{d}{}^{e}\widehat C{}_{b}{}_{d}{}^{f}{}^{g}\epsilon{}^{a}{}_{c}{}_{e}{}_{f}{}_{g}\\
&-\frac{86015}{82944}\widehat G{}^{a}{}^{b}\widehat G{}_{b}{}^{c}\widehat G{}^{d}{}^{e}\widehat G{}^{f}{}^{g}\epsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g} +\frac{98689}{41472}\widehat H{}^{b}{}^{c}\widehat G{}^{a}{}^{d}\widehat G{}_{d}{}^{e}\widehat G{}^{f}{}^{g}\epsilon{}_{b}{}_{c}{}_{e}{}_{f}{}_{g}
\end{aligned}
\tag{SC7-EF0-1}
```

```math
\begin{aligned}
&-\frac{23027}{20736}\widehat H{}^{b}{}^{c}\widehat H{}^{d}{}^{e}\widehat G{}^{a}{}^{f}\widehat G{}_{f}{}^{g}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{g} +\frac{2243}{41472}\widehat H{}^{b}{}^{c}\widehat G{}^{a}{}_{b}\widehat G{}^{d}{}^{e}\widehat G{}^{f}{}^{g}\epsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g}\\
&-\frac{6947}{5184}\widehat H{}^{b}{}^{c}\widehat H{}^{d}{}^{e}\widehat H{}^{f}{}^{g}\widehat G{}^{a}{}_{b}\epsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g} +\frac{34427}{41472}\widehat H{}^{a}{}^{b}\widehat G{}_{b}{}^{c}\widehat G{}^{d}{}^{e}\widehat G{}^{f}{}^{g}\epsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g}\\
&-\frac{4385}{20736}\widehat H{}^{a}{}^{b}\widehat H{}_{b}{}^{c}\widehat G{}^{d}{}^{e}\widehat G{}^{f}{}^{g}\epsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g} +\frac{1801}{5184}\widehat H{}^{a}{}^{b}\widehat H{}^{c}{}^{d}\widehat H{}^{e}{}^{f}\widehat G{}_{b}{}^{g}\epsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g}\\
&-\frac{44159}{10368}\widehat H{}^{a}{}^{b}\widehat H{}_{b}{}^{c}\widehat H{}^{d}{}^{e}\widehat G{}^{f}{}^{g}\epsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g} +\frac{13625}{2592}\widehat H{}^{a}{}^{b}\widehat H{}_{b}{}^{c}\widehat H{}^{d}{}^{e}\widehat H{}^{f}{}^{g}\epsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g}\\
&-\frac{551}{10368}\widehat G{}^{b}{}^{c}\widehat G{}_{b}{}^{d}\widehat G{}_{c}{}^{e}\widehat G{}^{f}{}^{g}\epsilon{}^{a}{}_{d}{}_{e}{}_{f}{}_{g} +\frac{889}{2592}\widehat H{}^{b}{}^{c}\widehat G{}^{d}{}^{e}\widehat G{}_{d}{}^{f}\widehat G{}_{e}{}^{g}\epsilon{}^{a}{}_{b}{}_{c}{}_{f}{}_{g}\\
&+\frac{26779}{20736}\widehat H{}^{b}{}^{c}\widehat G{}_{b}{}^{d}\widehat G{}_{d}{}^{e}\widehat G{}^{f}{}^{g}\epsilon{}^{a}{}_{c}{}_{e}{}_{f}{}_{g} -\frac{23027}{41472}\widehat H{}^{b}{}^{c}\widehat H{}^{d}{}^{e}\epsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{e}\widehat G^2\\
&-\frac{19823}{10368}\widehat H{}^{b}{}^{c}\widehat H{}^{d}{}^{e}\widehat G{}_{b}{}_{d}\widehat G{}^{f}{}^{g}\epsilon{}^{a}{}_{c}{}_{e}{}_{f}{}_{g} +\frac{21275}{5184}\widehat H{}^{b}{}^{c}\widehat H{}^{d}{}^{e}\widehat H{}^{f}{}^{g}\widehat G{}_{b}{}_{d}\epsilon{}^{a}{}_{c}{}_{e}{}_{f}{}_{g}\\
&+\frac{125}{20736}\widehat H{}^{b}{}^{c}\widehat G{}_{b}{}^{d}\widehat G{}_{c}{}^{e}\widehat G{}^{f}{}^{g}\epsilon{}^{a}{}_{d}{}_{e}{}_{f}{}_{g} -\frac{1181}{10368}\widehat H{}^{b}{}^{c}\widehat H{}^{d}{}^{e}\widehat G{}_{b}{}^{f}\widehat G{}_{c}{}^{g}\epsilon{}^{a}{}_{d}{}_{e}{}_{f}{}_{g}\\
&-\frac{4385}{41472}\widehat H{}^{b}{}^{c}\widehat H{}_{b}{}_{c}\widehat G{}^{d}{}^{e}\widehat G{}^{f}{}^{g}\epsilon{}^{a}{}_{d}{}_{e}{}_{f}{}_{g} +\frac{12205}{5184}\widehat H{}^{b}{}^{c}\widehat H{}_{b}{}^{d}\widehat H{}^{e}{}^{f}\widehat G{}_{c}{}^{g}\epsilon{}^{a}{}_{d}{}_{e}{}_{f}{}_{g}\\
&+\frac{122}{81}\widehat H{}^{b}{}^{c}\widehat H{}_{b}{}^{d}\widehat H{}_{c}{}^{e}\widehat G{}^{f}{}^{g}\epsilon{}^{a}{}_{d}{}_{e}{}_{f}{}_{g} -\frac{635}{162}\widehat H{}^{b}{}^{c}\widehat H{}_{b}{}^{d}\widehat H{}_{c}{}^{e}\widehat H{}^{f}{}^{g}\epsilon{}^{a}{}_{d}{}_{e}{}_{f}{}_{g}\\
&+\frac{551}{41472}\widehat G{}^{b}{}^{c}\widehat G{}^{d}{}^{e}\epsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{e}\widehat G^2 -\frac{889}{5184}\widehat H{}^{b}{}^{c}\widehat G{}^{d}{}^{e}\epsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{e}\widehat G^2\\
&-\frac{1237}{5184}\widehat H{}^{b}{}^{c}\widehat G{}_{b}{}_{c}\widehat G{}^{d}{}^{e}\widehat G{}^{f}{}^{g}\epsilon{}^{a}{}_{d}{}_{e}{}_{f}{}_{g} +\frac{1513}{1296}\widehat H{}^{b}{}^{c}\widehat H{}^{d}{}^{e}\widehat G{}_{b}{}_{c}\widehat G{}^{f}{}^{g}\epsilon{}^{a}{}_{d}{}_{e}{}_{f}{}_{g}\\
&-\frac{3209}{2592}\widehat H{}^{b}{}^{c}\widehat H{}^{d}{}^{e}\widehat H{}^{f}{}^{g}\widehat G{}_{b}{}_{c}\epsilon{}^{a}{}_{d}{}_{e}{}_{f}{}_{g} -\frac{61}{81}\widehat H{}^{b}{}^{c}\widehat H{}_{b}{}_{c}\widehat H{}^{d}{}^{e}\widehat G{}^{f}{}^{g}\epsilon{}^{a}{}_{d}{}_{e}{}_{f}{}_{g}\\
&+\frac{635}{648}\widehat H{}^{b}{}^{c}\widehat H{}_{b}{}_{c}\widehat H{}^{d}{}^{e}\widehat H{}^{f}{}^{g}\epsilon{}^{a}{}_{d}{}_{e}{}_{f}{}_{g} -\frac{1}{6}\big(\mathcal D^{b}\widehat G{}^{a}{}_{b}\big)\widehat G^2\\
&-\frac{2}{3}\big(\mathcal D^{b}\widehat H{}^{a}{}_{b}\big)\widehat G^2 +2\widehat H{}^{b}{}^{c}\widehat G{}_{b}{}_{c}\big(\mathcal D^{d}\widehat G{}^{a}{}_{d}\big)\\
&-\frac{2}{3}\widehat H{}^{b}{}^{c}\widehat H{}_{b}{}_{c}\big(\mathcal D^{d}\widehat G{}^{a}{}_{d}\big) -\frac{8}{3}\widehat H{}^{b}{}^{c}\widehat H{}_{b}{}_{c}\big(\mathcal D^{d}\widehat H{}^{a}{}_{d}\big)\\
&+\frac{2}{3}\widehat G{}^{b}{}^{c}\widehat G{}_{b}{}^{d}\big(\mathcal D_{c}\widehat G{}^{a}{}_{d}\big) +\frac{2}{3}\big(\mathcal D^{b}\widehat H{}^{a}{}^{c}\big)\widehat G{}_{b}{}^{d}\widehat G{}_{c}{}_{d}\\
&-\frac{8}{3}\widehat H{}^{b}{}^{c}\widehat G{}_{b}{}^{d}\big(\mathcal D_{d}\widehat G{}^{a}{}_{c}\big) -\frac{8}{3}\widehat H{}^{b}{}^{c}\big(\mathcal D^{d}\widehat H{}^{a}{}_{b}\big)\widehat G{}_{c}{}_{d}
\end{aligned}
\tag{SC7-EF0-2}
```

```math
\begin{aligned}
&+\frac{16}{3}\widehat H{}^{b}{}^{c}\big(\mathcal D_{b}\widehat H{}^{a}{}^{d}\big)\widehat G{}_{c}{}_{d} +\frac{8}{3}\widehat H{}^{b}{}^{c}\widehat H{}_{b}{}^{d}\big(\mathcal D_{c}\widehat G{}^{a}{}_{d}\big)\\
&+\frac{32}{3}\widehat H{}^{b}{}^{c}\widehat H{}_{b}{}^{d}\big(\mathcal D_{c}\widehat H{}^{a}{}_{d}\big) -\frac{2}{3}\widehat G{}^{a}{}^{b}\widehat G{}_{b}{}^{c}\big(\mathcal D^{d}\widehat G{}_{c}{}_{d}\big)\\
&-\frac{2}{3}\big(\mathcal D^{b}\widehat H{}_{b}{}^{c}\big)\widehat G{}^{a}{}^{d}\widehat G{}_{c}{}_{d} +\frac{10}{3}\widehat H{}^{b}{}^{c}\widehat G{}^{a}{}_{b}\big(\mathcal D^{d}\widehat G{}_{c}{}_{d}\big)\\
&+\frac{8}{3}\widehat H{}^{b}{}^{c}\big(\mathcal D^{d}\widehat H{}_{b}{}_{d}\big)\widehat G{}^{a}{}_{c} -\frac{2}{3}\widehat H{}^{a}{}^{b}\widehat G{}_{b}{}^{c}\big(\mathcal D^{d}\widehat G{}_{c}{}_{d}\big)\\
&-\frac{16}{3}\widehat H{}^{a}{}^{b}\big(\mathcal D^{c}\widehat H{}_{c}{}^{d}\big)\widehat G{}_{b}{}_{d} -\frac{8}{3}\widehat H{}^{a}{}^{b}\widehat H{}_{b}{}^{c}\big(\mathcal D^{d}\widehat G{}_{c}{}_{d}\big)\\
&-\frac{32}{3}\widehat H{}^{a}{}^{b}\widehat H{}_{b}{}^{c}\big(\mathcal D^{d}\widehat H{}_{c}{}_{d}\big) +\frac{7}{3}\widehat G{}^{a}{}^{b}\widehat G{}^{c}{}^{d}\big(\mathcal D_{c}\widehat G{}_{b}{}_{d}\big)\\
&-\frac{10}{3}\big(\mathcal D^{b}\widehat H{}^{c}{}^{d}\big)\widehat G{}^{a}{}_{c}\widehat G{}_{b}{}_{d} +2\widehat H{}^{b}{}^{c}\widehat G{}^{a}{}^{d}\big(\mathcal D_{b}\widehat G{}_{c}{}_{d}\big)\\
&-\frac{8}{3}\widehat H{}^{b}{}^{c}\big(\mathcal D_{b}\widehat H{}_{c}{}^{d}\big)\widehat G{}^{a}{}_{d} -\frac{4}{3}\widehat H{}^{a}{}^{b}\widehat G{}^{c}{}^{d}\big(\mathcal D_{c}\widehat G{}_{b}{}_{d}\big)\\
&+\frac{8}{3}\widehat H{}^{a}{}^{b}\big(\mathcal D^{c}\widehat H{}_{b}{}^{d}\big)\widehat G{}_{c}{}_{d} -\frac{20}{3}\widehat H{}^{a}{}^{b}\widehat H{}^{c}{}^{d}\big(\mathcal D_{c}\widehat G{}_{b}{}_{d}\big)\\
&+\frac{32}{3}\widehat H{}^{a}{}^{b}\widehat H{}^{c}{}^{d}\big(\mathcal D_{c}\widehat H{}_{b}{}_{d}\big) -\frac{7}{6}\widehat G{}^{a}{}^{b}\widehat G{}^{c}{}^{d}\big(\mathcal D_{b}\widehat G{}_{c}{}_{d}\big)\\
&+2\big(\mathcal D^{b}\widehat H{}^{c}{}^{d}\big)\widehat G{}^{a}{}_{b}\widehat G{}_{c}{}_{d} +\frac{10}{3}\widehat H{}^{b}{}^{c}\widehat G{}^{a}{}^{d}\big(\mathcal D_{d}\widehat G{}_{b}{}_{c}\big)\\
&-\frac{4}{3}\widehat H{}^{b}{}^{c}\big(\mathcal D^{d}\widehat H{}_{b}{}_{c}\big)\widehat G{}^{a}{}_{d} -\frac{1}{3}\widehat H{}^{a}{}^{b}\widehat G{}^{c}{}^{d}\big(\mathcal D_{b}\widehat G{}_{c}{}_{d}\big)\\
&+\frac{2}{3}\widehat H{}^{a}{}^{b}\widehat H{}^{c}{}^{d}\big(\mathcal D_{b}\widehat G{}_{c}{}_{d}\big) -\frac{16}{3}\widehat H{}^{a}{}^{b}\widehat H{}^{c}{}^{d}\big(\mathcal D_{b}\widehat H{}_{c}{}_{d}\big)\\
&-\frac{1}{4}\big(\mathcal D^{b}\widehat C{}^{a}{}^{c}{}_{b}{}^{d}\big)\widehat G{}_{c}{}_{d} +\widehat H{}^{b}{}^{c}\big(\mathcal D^{d}\widehat C{}^{a}{}_{b}{}_{c}{}_{d}\big)\\
&-\frac{1}{8}\big(\mathcal D^{b}\widehat C{}^{a}{}_{b}{}^{c}{}^{d}\big)\widehat G{}_{c}{}_{d} -\frac{1}{2}\widehat H{}^{b}{}^{c}\big(\mathcal D^{d}\widehat C{}^{a}{}_{d}{}_{b}{}_{c}\big)\\
&-\frac{7}{18}\widehat G{}^{b}{}^{c}\widehat G{}^{d}{}^{e}\big(\mathcal D^{f}\mathcal D^{a}\sigma\big)\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f} +\frac{7}{72}\widehat G{}^{b}{}^{c}\widehat G{}^{d}{}^{e}\big(\mathcal D^{a}\mathcal D^{f}\sigma\big)\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\\
&+\frac{7}{144}\widehat G{}^{a}{}^{b}\big(\mathcal D^{c}\mathcal D^{d}\widehat G{}^{e}{}^{f}\big)\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f} +\frac{13}{9}\widehat H{}^{b}{}^{c}\widehat G{}^{a}{}^{d}\big(\mathcal D^{e}\mathcal D^{f}\sigma\big)\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\\
&-\frac{25}{72}\big(\mathcal D^{b}\mathcal D^{c}\widehat H{}^{d}{}^{e}\big)\widehat G{}^{a}{}^{f}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f} +\frac{257}{144}\widehat H{}^{a}{}^{b}\widehat G{}^{c}{}^{d}\big(\mathcal D^{e}\mathcal D^{f}\sigma\big)\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}
\end{aligned}
\tag{SC7-EF0-3}
```

```math
\begin{aligned}
&+\frac{91}{144}\widehat H{}^{a}{}^{b}\big(\mathcal D^{c}\mathcal D^{d}\widehat G{}^{e}{}^{f}\big)\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f} +\frac{37}{18}\widehat H{}^{b}{}^{c}\widehat H{}^{d}{}^{e}\big(\mathcal D^{f}\mathcal D^{a}\sigma\big)\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\\
&-\frac{7}{18}\widehat H{}^{b}{}^{c}\widehat H{}^{d}{}^{e}\big(\mathcal D^{a}\mathcal D^{f}\sigma\big)\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f} -\frac{55}{72}\widehat H{}^{a}{}^{b}\big(\mathcal D^{c}\mathcal D^{d}\widehat H{}^{e}{}^{f}\big)\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\\
&+\frac{7}{24}\widehat G{}^{b}{}^{c}\widehat G{}^{d}{}^{e}\big(\Box^c \sigma\big)\epsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{e} -\frac{1}{36}\widehat G{}^{b}{}^{c}\big(\mathcal D_{b}\mathcal D^{d}\widehat G{}^{e}{}^{f}\big)\epsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f}\\
&-\frac{11}{36}\widehat H{}^{b}{}^{c}\widehat G{}^{d}{}^{e}\big(\mathcal D_{d}\mathcal D^{f}\sigma\big)\epsilon{}^{a}{}_{b}{}_{c}{}_{e}{}_{f} -\frac{5}{36}\big(\mathcal D^{b}\mathcal D^{c}\widehat H{}^{d}{}^{e}\big)\widehat G{}_{b}{}^{f}\epsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f}\\
&+\frac{149}{144}\widehat H{}^{b}{}^{c}\widehat G{}^{d}{}^{e}\big(\mathcal D_{b}\mathcal D^{f}\sigma\big)\epsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f} -\frac{37}{144}\widehat H{}^{b}{}^{c}\big(\mathcal D_{b}\mathcal D^{d}\widehat G{}^{e}{}^{f}\big)\epsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f}\\
&-\frac{5}{3}\widehat H{}^{b}{}^{c}\widehat H{}^{d}{}^{e}\big(\Box^c \sigma\big)\epsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{e} +\frac{25}{72}\widehat H{}^{b}{}^{c}\big(\mathcal D_{b}\mathcal D^{d}\widehat H{}^{e}{}^{f}\big)\epsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f}\\
&-\frac{1}{8}\widehat G{}^{b}{}^{c}\big(\mathcal D^{d}\mathcal D^{e}\widehat G{}_{b}{}^{f}\big)\epsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f} +\frac{43}{24}\widehat H{}^{b}{}^{c}\widehat G{}_{b}{}^{d}\big(\mathcal D^{e}\mathcal D^{f}\sigma\big)\epsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f}\\
&-\frac{5}{12}\big(\mathcal D^{b}\mathcal D^{c}\widehat H{}^{d}{}^{e}\big)\widehat G{}_{d}{}^{f}\epsilon{}^{a}{}_{b}{}_{c}{}_{e}{}_{f} -\frac{5}{8}\widehat H{}^{b}{}^{c}\big(\mathcal D^{d}\mathcal D^{e}\widehat G{}_{b}{}^{f}\big)\epsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f}\\
&+\frac{11}{12}\widehat H{}^{b}{}^{c}\big(\mathcal D^{d}\mathcal D^{e}\widehat H{}_{b}{}^{f}\big)\epsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f} +\frac{1}{12}\widehat G{}^{b}{}^{c}\big(\mathcal D^{d}\mathcal D^{e}\widehat G{}^{a}{}^{f}\big)\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\\
&-\frac{1}{2}\big(\mathcal D^{b}\mathcal D^{c}\widehat H{}^{a}{}^{d}\big)\widehat G{}^{e}{}^{f}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f} +\frac{5}{6}\widehat H{}^{b}{}^{c}\big(\mathcal D^{d}\mathcal D^{e}\widehat G{}^{a}{}^{f}\big)\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\\
&-\widehat H{}^{b}{}^{c}\big(\mathcal D^{d}\mathcal D^{e}\widehat H{}^{a}{}^{f}\big)\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f} -\frac{25}{144}\widehat G{}^{b}{}^{c}\big(\mathcal D^{d}\mathcal D^{e}\widehat G{}_{d}{}^{f}\big)\epsilon{}^{a}{}_{b}{}_{c}{}_{e}{}_{f}\\
&+\frac{25}{72}\big(\mathcal D^{b}\mathcal D^{c}\widehat H{}_{b}{}^{d}\big)\widehat G{}^{e}{}^{f}\epsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f} -\frac{11}{18}\widehat H{}^{b}{}^{c}\big(\mathcal D^{d}\mathcal D^{e}\widehat G{}_{d}{}^{f}\big)\epsilon{}^{a}{}_{b}{}_{c}{}_{e}{}_{f}\\
&+\frac{11}{9}\widehat H{}^{b}{}^{c}\big(\mathcal D^{d}\mathcal D^{e}\widehat H{}_{d}{}^{f}\big)\epsilon{}^{a}{}_{b}{}_{c}{}_{e}{}_{f} -\frac{5}{288}\widehat G{}^{b}{}^{c}\big(\mathcal D^{a}\mathcal D^{d}\widehat G{}^{e}{}^{f}\big)\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\\
&+\frac{13}{24}\widehat H{}^{b}{}^{c}\widehat G{}^{d}{}^{e}\big(\mathcal D^{a}\mathcal D^{f}\sigma\big)\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f} -\frac{19}{144}\big(\mathcal D^{a}\mathcal D^{b}\widehat H{}^{c}{}^{d}\big)\widehat G{}^{e}{}^{f}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\\
&+\frac{2}{9}\widehat H{}^{b}{}^{c}\big(\mathcal D^{a}\mathcal D^{d}\widehat G{}^{e}{}^{f}\big)\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f} -\frac{1}{9}\widehat H{}^{b}{}^{c}\big(\mathcal D^{a}\mathcal D^{d}\widehat H{}^{e}{}^{f}\big)\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\\
&-\frac{5}{144}\widehat G{}^{b}{}^{c}\big(\mathcal D^{d}\mathcal D^{e}\widehat G{}_{e}{}^{f}\big)\epsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{f} -\frac{371}{144}\widehat H{}^{b}{}^{c}\widehat G{}^{d}{}^{e}\big(\mathcal D^{f}\mathcal D_{b}\sigma\big)\epsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f}\\
&-\frac{55}{72}\big(\mathcal D^{b}\mathcal D^{c}\widehat H{}_{c}{}^{d}\big)\widehat G{}^{e}{}^{f}\epsilon{}^{a}{}_{b}{}_{d}{}_{e}{}_{f} -\frac{65}{72}\widehat H{}^{b}{}^{c}\widehat G{}^{d}{}^{e}\big(\mathcal D^{f}\mathcal D_{d}\sigma\big)\epsilon{}^{a}{}_{b}{}_{c}{}_{e}{}_{f}\\
&-\frac{7}{72}\widehat H{}^{b}{}^{c}\big(\mathcal D^{d}\mathcal D^{e}\widehat G{}_{e}{}^{f}\big)\epsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{f} +\frac{67}{36}\widehat H{}^{b}{}^{c}\big(\mathcal D^{d}\mathcal D^{e}\widehat H{}_{e}{}^{f}\big)\epsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{f}
\end{aligned}
\tag{SC7-EF0-4}
```

```math
\begin{aligned}
&+\frac{23}{288}\widehat G{}^{b}{}^{c}\big(\mathcal D^{d}\mathcal D^{a}\widehat G{}^{e}{}^{f}\big)\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f} +\frac{43}{48}\widehat H{}^{b}{}^{c}\widehat G{}^{d}{}^{e}\big(\mathcal D^{f}\mathcal D^{a}\sigma\big)\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\\
&-\frac{11}{144}\big(\mathcal D^{b}\mathcal D^{a}\widehat H{}^{c}{}^{d}\big)\widehat G{}^{e}{}^{f}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f} +\frac{13}{144}\widehat H{}^{b}{}^{c}\big(\mathcal D^{d}\mathcal D^{a}\widehat G{}^{e}{}^{f}\big)\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\\
&-\frac{25}{72}\widehat H{}^{b}{}^{c}\big(\mathcal D^{d}\mathcal D^{a}\widehat H{}^{e}{}^{f}\big)\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f} +\frac{5}{72}\widehat G{}^{b}{}^{c}\big(\mathcal D^{d}\mathcal D_{b}\widehat G{}^{e}{}^{f}\big)\epsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f}\\
&+\frac{1}{18}\big(\mathcal D^{b}\mathcal D^{c}\widehat H{}^{d}{}^{e}\big)\widehat G{}_{c}{}^{f}\epsilon{}^{a}{}_{b}{}_{d}{}_{e}{}_{f} +\frac{43}{144}\widehat H{}^{b}{}^{c}\big(\mathcal D^{d}\mathcal D_{b}\widehat G{}^{e}{}^{f}\big)\epsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f}\\
&-\frac{55}{72}\widehat H{}^{b}{}^{c}\big(\mathcal D^{d}\mathcal D_{b}\widehat H{}^{e}{}^{f}\big)\epsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f} -\frac{7}{48}\widehat G{}^{b}{}^{c}\big(\Box^c \widehat G{}^{e}{}^{f}\big)\epsilon{}^{a}{}_{b}{}_{c}{}_{e}{}_{f}\\
&-\frac{23}{16}\widehat H{}^{b}{}^{c}\widehat G{}^{d}{}^{e}\big(\Box^c \sigma\big)\epsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{e} +\frac{5}{24}\big(\Box^c \widehat H{}^{c}{}^{d}\big)\widehat G{}^{e}{}^{f}\epsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f}\\
&+\frac{17}{48}\widehat H{}^{b}{}^{c}\big(\Box^c \widehat G{}^{e}{}^{f}\big)\epsilon{}^{a}{}_{b}{}_{c}{}_{e}{}_{f} +\frac{11}{24}\widehat H{}^{b}{}^{c}\big(\Box^c \widehat H{}^{e}{}^{f}\big)\epsilon{}^{a}{}_{b}{}_{c}{}_{e}{}_{f}\\
&-\frac{1}{3}\widehat G{}^{a}{}^{b}\big(\mathcal D_{b}\Box^c \sigma\big) -\frac{4}{3}\widehat H{}^{a}{}^{b}\big(\mathcal D_{b}\Box^c \sigma\big)\\
&-\frac{4}{3}g^{2}L_c{}^{i}{}^{j}\big(\mathcal D^{b}L_c{}_{i}{}_{j}\big)\widehat G{}^{a}{}_{b} +\frac{2}{3}g^{2}\widehat H{}^{a}{}^{b}L_c{}^{i}{}^{j}\big(\mathcal D_{b}L_c{}_{i}{}_{j}\big)\\
&-\frac{5}{3}g\big(\mathcal D^{b}N_c\big)\widehat G{}^{a}{}_{b} +\frac{4}{3}g\widehat H{}^{a}{}^{b}\big(\mathcal D_{b}N_c\big)\\
&-\frac{2}{3}\big(\mathcal D^{b}\widehat G{}^{a}{}_{b}\big)\big(\Box^c \sigma\big) +\frac{10}{3}\big(\mathcal D^{b}\widehat H{}^{a}{}_{b}\big)\big(\Box^c \sigma\big)\\
&-\frac{2}{3}g^{2}L_c{}^{i}{}^{j}L_c{}_{i}{}_{j}\big(\mathcal D^{b}\widehat G{}^{a}{}_{b}\big) +\frac{1}{3}g^{2}\big(\mathcal D^{b}\widehat H{}^{a}{}_{b}\big)L_c{}^{i}{}^{j}L_c{}_{i}{}_{j}\\
&-\frac{5}{3}N_cg\big(\mathcal D^{b}\widehat G{}^{a}{}_{b}\big) +\frac{4}{3}N_cg\big(\mathcal D^{b}\widehat H{}^{a}{}_{b}\big)\\
&+\frac{113}{1536}\big(\mathcal D^{b}\widehat G{}^{a}{}^{c}\big)\big(\mathcal D^{d}\widehat G{}^{e}{}^{f}\big)\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f} -\frac{881}{768}\big(\mathcal D^{b}\widehat H{}^{c}{}^{d}\big)\big(\mathcal D^{e}\widehat G{}^{a}{}^{f}\big)\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\\
&+\frac{1199}{768}\big(\mathcal D^{b}\widehat H{}^{a}{}^{c}\big)\big(\mathcal D^{d}\widehat G{}^{e}{}^{f}\big)\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f} -\frac{431}{384}\big(\mathcal D^{b}\widehat H{}^{a}{}^{c}\big)\big(\mathcal D^{d}\widehat H{}^{e}{}^{f}\big)\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\\
&+\frac{1105}{1536}\big(\mathcal D^{b}\widehat G{}^{c}{}^{d}\big)\big(\mathcal D_{c}\widehat G{}^{e}{}^{f}\big)\epsilon{}^{a}{}_{b}{}_{d}{}_{e}{}_{f} -\frac{401}{768}\big(\mathcal D^{b}\widehat H{}^{c}{}^{d}\big)\big(\mathcal D^{e}\widehat G{}_{b}{}^{f}\big)\epsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f}\\
&-\frac{1265}{768}\big(\mathcal D^{b}\widehat H{}^{c}{}^{d}\big)\big(\mathcal D_{c}\widehat G{}^{e}{}^{f}\big)\epsilon{}^{a}{}_{b}{}_{d}{}_{e}{}_{f} +\frac{187}{128}\big(\mathcal D^{b}\widehat H{}^{c}{}^{d}\big)\big(\mathcal D_{c}\widehat H{}^{e}{}^{f}\big)\epsilon{}^{a}{}_{b}{}_{d}{}_{e}{}_{f}\\
&-\frac{1039}{768}\big(\mathcal D^{b}\widehat G{}^{c}{}^{d}\big)\big(\mathcal D^{e}\widehat G{}_{c}{}^{f}\big)\epsilon{}^{a}{}_{b}{}_{d}{}_{e}{}_{f} +\frac{245}{64}\big(\mathcal D^{b}\widehat H{}^{c}{}^{d}\big)\big(\mathcal D^{e}\widehat G{}_{c}{}^{f}\big)\epsilon{}^{a}{}_{b}{}_{d}{}_{e}{}_{f}
\end{aligned}
\tag{SC7-EF0-5}
```

```math
\begin{aligned}
&-\frac{431}{192}\big(\mathcal D^{b}\widehat H{}^{c}{}^{d}\big)\big(\mathcal D^{e}\widehat H{}_{c}{}^{f}\big)\epsilon{}^{a}{}_{b}{}_{d}{}_{e}{}_{f} +\frac{175}{512}\big(\mathcal D^{b}\widehat G{}_{b}{}^{c}\big)\big(\mathcal D^{d}\widehat G{}^{e}{}^{f}\big)\epsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f}\\
&-\frac{17}{256}\big(\mathcal D^{b}\widehat H{}^{c}{}^{d}\big)\big(\mathcal D^{e}\widehat G{}_{e}{}^{f}\big)\epsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{f} +\frac{49}{256}\big(\mathcal D^{b}\widehat H{}_{b}{}^{c}\big)\big(\mathcal D^{d}\widehat G{}^{e}{}^{f}\big)\epsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f}\\
&-\frac{241}{128}\big(\mathcal D^{b}\widehat H{}_{b}{}^{c}\big)\big(\mathcal D^{d}\widehat H{}^{e}{}^{f}\big)\epsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f} -\frac{415}{1536}\big(\mathcal D^{a}\widehat G{}^{b}{}^{c}\big)\big(\mathcal D^{d}\widehat G{}^{e}{}^{f}\big)\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\\
&+\frac{415}{768}\big(\mathcal D^{b}\widehat H{}^{c}{}^{d}\big)\big(\mathcal D^{a}\widehat G{}^{e}{}^{f}\big)\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f} +\frac{191}{768}\big(\mathcal D^{a}\widehat H{}^{b}{}^{c}\big)\big(\mathcal D^{d}\widehat G{}^{e}{}^{f}\big)\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\\
&-\frac{191}{384}\big(\mathcal D^{a}\widehat H{}^{b}{}^{c}\big)\big(\mathcal D^{d}\widehat H{}^{e}{}^{f}\big)\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f} -\frac{353}{1536}\big(\mathcal D^{b}\widehat G{}^{c}{}^{d}\big)\big(\mathcal D_{b}\widehat G{}^{e}{}^{f}\big)\epsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f}\\
&+\frac{59}{128}\big(\mathcal D^{b}\widehat H{}^{c}{}^{d}\big)\big(\mathcal D_{b}\widehat G{}^{e}{}^{f}\big)\epsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f} +\frac{191}{384}\big(\mathcal D^{b}\widehat H{}^{c}{}^{d}\big)\big(\mathcal D_{b}\widehat H{}^{e}{}^{f}\big)\epsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f}\\
&+gL_c{}^{i}{}^{j}\big(\mathcal D^{b}\widehat R(V){}^{a}{}_{b}{}_{i}{}_{j}\big) +g\big(\mathcal D^{b}L_c{}^{i}{}^{j}\big)\widehat R(V){}^{a}{}_{b}{}_{i}{}_{j}\\
&-\frac{31}{192}\widehat H{}^{b}{}^{c}\widehat C{}^{a}{}^{d}{}^{e}{}^{f}\widehat G{}_{e}{}^{g}\epsilon{}_{b}{}_{c}{}_{d}{}_{f}{}_{g} -\frac{1}{8}\widehat H{}^{b}{}^{c}\widehat C{}^{a}{}^{d}{}^{e}{}^{f}\widehat G{}_{b}{}^{g}\epsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g}\\
&-\frac{11}{24}\widehat H{}^{b}{}^{c}\widehat C{}^{a}{}^{d}{}_{b}{}^{e}\widehat G{}^{f}{}^{g}\epsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g} -\frac{25}{64}\widehat H{}^{b}{}^{c}\widehat C{}^{a}{}^{d}{}^{e}{}^{f}\widehat G{}_{d}{}^{g}\epsilon{}_{b}{}_{c}{}_{e}{}_{f}{}_{g}\\
&+\frac{1}{64}\widehat H{}^{b}{}^{c}\widehat C{}^{a}{}_{b}{}^{d}{}^{e}\widehat G{}^{f}{}^{g}\epsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g} +\frac{63}{16}\widehat H{}^{b}{}^{c}\widehat G{}^{a}{}^{d}\widehat G{}_{b}{}^{e}\widehat G{}^{f}{}^{g}\epsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g}\\
&-\frac{37}{4}\widehat H{}^{a}{}^{b}\widehat H{}^{c}{}^{d}\widehat H{}^{e}{}^{f}\widehat G{}_{c}{}^{g}\epsilon{}_{b}{}_{d}{}_{e}{}_{f}{}_{g} +\frac{2}{3}\widehat G{}^{a}{}^{b}\big(\Box^c \mathcal D_{b}\sigma\big)\\
&+\frac{1}{2}\big(\mathcal D^{b}\widehat G{}^{a}{}^{c}\big)\big(\mathcal D_{b}\mathcal D_{c}\sigma\big) +\frac{8}{3}\widehat H{}^{a}{}^{b}\big(\Box^c \mathcal D_{b}\sigma\big)\\
&+5\big(\mathcal D^{b}\widehat H{}^{a}{}^{c}\big)\big(\mathcal D_{b}\mathcal D_{c}\sigma\big) -2\big(\Box^c \mathcal D^{c}\widehat H{}^{a}{}_{c}\big)\\
&+\frac{1}{2}\big(\mathcal D^{b}\widehat G{}^{a}{}^{c}\big)\big(\mathcal D_{c}\mathcal D_{b}\sigma\big) -\big(\mathcal D^{b}\widehat H{}^{a}{}^{c}\big)\big(\mathcal D_{c}\mathcal D_{b}\sigma\big)\\
&-\frac{5}{4}\big(\mathcal D^{b}\widehat G{}_{b}{}^{c}\big)\big(\mathcal D_{c}\mathcal D^{a}\sigma\big) +\frac{5}{2}\big(\mathcal D^{b}\widehat H{}_{b}{}^{c}\big)\big(\mathcal D_{c}\mathcal D^{a}\sigma\big)\\
&+\frac{1}{4}\big(\mathcal D^{b}\widehat G{}_{b}{}^{c}\big)\big(\mathcal D^{a}\mathcal D_{c}\sigma\big) -\frac{1}{2}\big(\mathcal D^{b}\widehat H{}_{b}{}^{c}\big)\big(\mathcal D^{a}\mathcal D_{c}\sigma\big)\\
&+\frac{1}{2}\big(\mathcal D^{a}\widehat G{}^{b}{}^{c}\big)\big(\mathcal D_{b}\mathcal D_{c}\sigma\big) -\big(\mathcal D^{a}\widehat H{}^{b}{}^{c}\big)\big(\mathcal D_{b}\mathcal D_{c}\sigma\big)\\
&-\frac{89}{144}\widehat H{}^{b}{}^{c}\widehat H{}^{d}{}^{e}\widehat G{}_{b}{}^{f}\widehat G{}_{d}{}^{g}\epsilon{}^{a}{}_{c}{}_{e}{}_{f}{}_{g} +\frac{2}{3}\widehat H{}^{b}{}^{c}\widehat G{}_{b}{}^{d}\big(\mathcal D^{a}\widehat G{}_{c}{}_{d}\big)
\end{aligned}
\tag{SC7-EF0-6}
```

#### Constrained vector: 2 explicit fermions

```math
\begin{aligned}
E_{\log}^{a}[2]={}&-\frac{803}{18432}\widehat G{}^{e}{}^{f}\epsilon{}^{a}{}_{b}{}_{c}{}_{e}{}_{f}\overline{\widehat R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{d}\big(\mathcal D_{d}\psi{}_{i}\big) +\frac{539}{9216}\widehat H{}^{b}{}^{c}\epsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\widehat R(Q){}^{d}{}^{e}{}^{i}}\gamma{}^{f}\big(\mathcal D_{f}\psi{}_{i}\big)\\
&+\frac{919i}{18432}g\widehat G{}^{d}{}^{e}\epsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\widehat R(Q){}^{b}{}^{c}{}^{i}}\varphi_c{}_{i} -\frac{655i}{9216}g\widehat H{}^{b}{}^{c}\epsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\widehat R(Q){}^{d}{}^{e}{}^{i}}\varphi_c{}_{i}\\
&-\frac{2269i}{9216}\widehat G{}_{c}{}_{d}\overline{\widehat R(Q){}^{a}{}^{b}{}^{i}}\gamma{}^{c}{}^{d}\big(\mathcal D_{b}\psi{}_{i}\big) +\frac{2047i}{1536}\widehat G{}_{b}{}^{c}\overline{\widehat R(Q){}^{a}{}^{b}{}^{i}}\big(\mathcal D_{c}\psi{}_{i}\big)\\
&-\frac{181}{3072}\widehat G{}^{d}{}^{e}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\widehat R(Q){}^{a}{}^{b}{}^{i}}\gamma{}^{c}\big(\mathcal D^{f}\psi{}_{i}\big) +\frac{473i}{768}\widehat H{}^{b}{}^{c}\overline{\widehat R(Q){}^{a}{}_{b}{}^{i}}\big(\mathcal D_{c}\psi{}_{i}\big)\\
&-\frac{3731i}{4608}\widehat H{}^{b}{}^{c}\overline{\widehat R(Q){}^{a}{}^{d}{}^{i}}\gamma{}_{b}{}_{c}\big(\mathcal D_{d}\psi{}_{i}\big) -\frac{115}{1536}\widehat H{}^{b}{}^{c}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\widehat R(Q){}^{a}{}^{d}{}^{i}}\gamma{}^{e}\big(\mathcal D^{f}\psi{}_{i}\big)\\
&+\frac{719i}{18432}g\widehat G{}^{e}{}^{f}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\widehat R(Q){}^{a}{}^{b}{}^{i}}\gamma{}^{c}{}^{d}\varphi_c{}_{i} +\frac{889i}{9216}g\widehat H{}^{b}{}^{c}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\widehat R(Q){}^{a}{}^{d}{}^{i}}\gamma{}^{e}{}^{f}\varphi_c{}_{i}\\
&+\frac{4685i}{9216}\widehat G{}_{b}{}_{c}\overline{\widehat R(Q){}^{b}{}^{c}{}^{i}}\big(\mathcal D^{a}\psi{}_{i}\big) +\frac{425i}{2304}\widehat G{}_{b}{}_{d}\overline{\widehat R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{a}{}^{d}\big(\mathcal D_{c}\psi{}_{i}\big)\\
&+\frac{401}{2304}\widehat G{}_{b}{}^{e}\epsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\widehat R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{d}\big(\mathcal D^{f}\psi{}_{i}\big) +\frac{3691i}{4608}\widehat H{}^{b}{}^{c}\overline{\widehat R(Q){}_{b}{}_{c}{}^{i}}\big(\mathcal D^{a}\psi{}_{i}\big)\\
&-\frac{305i}{1152}\widehat H{}^{b}{}^{c}\overline{\widehat R(Q){}_{b}{}^{d}{}^{i}}\gamma{}^{a}{}_{c}\big(\mathcal D_{d}\psi{}_{i}\big) -\frac{1469}{1152}\widehat H{}^{b}{}^{c}\epsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\widehat R(Q){}_{b}{}^{d}{}^{i}}\gamma{}^{e}\big(\mathcal D^{f}\psi{}_{i}\big)\\
&+\frac{2071i}{18432}g\widehat G{}_{b}{}^{f}\epsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\widehat R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{d}{}^{e}\varphi_c{}_{i} +\frac{5191i}{9216}g\widehat H{}^{b}{}^{c}\epsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\widehat R(Q){}_{b}{}^{d}{}^{i}}\gamma{}^{e}{}^{f}\varphi_c{}_{i}\\
&+\frac{2129i}{2304}\widehat G{}_{b}{}_{c}\overline{\widehat R(Q){}^{a}{}^{b}{}^{i}}\gamma{}^{c}{}^{d}\big(\mathcal D_{d}\psi{}_{i}\big) +\frac{151i}{1152}\widehat H{}^{b}{}^{c}\overline{\widehat R(Q){}^{a}{}_{b}{}^{i}}\gamma{}_{c}{}^{d}\big(\mathcal D_{d}\psi{}_{i}\big)\\
&+\frac{2341}{2304}g\widehat G{}_{b}{}_{c}\overline{\widehat R(Q){}^{a}{}^{b}{}^{i}}\gamma{}^{c}\varphi_c{}_{i} -\frac{241}{1152}g\widehat H{}^{b}{}^{c}\overline{\widehat R(Q){}^{a}{}_{b}{}^{i}}\gamma{}_{c}\varphi_c{}_{i}\\
&+\frac{719i}{3072}\widehat G{}_{b}{}_{c}\overline{\widehat R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{a}{}^{d}\big(\mathcal D_{d}\psi{}_{i}\big) +\frac{929i}{1536}\widehat H{}^{b}{}^{c}\overline{\widehat R(Q){}_{b}{}_{c}{}^{i}}\gamma{}^{a}{}^{d}\big(\mathcal D_{d}\psi{}_{i}\big)\\
&+\frac{1099}{9216}g\widehat G{}_{b}{}_{c}\overline{\widehat R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{a}\varphi_c{}_{i} +\frac{6509}{4608}g\widehat H{}^{b}{}^{c}\overline{\widehat R(Q){}_{b}{}_{c}{}^{i}}\gamma{}^{a}\varphi_c{}_{i}\\
&-\frac{505i}{1152}\widehat G{}^{a}{}_{b}\overline{\widehat R(Q){}^{b}{}^{c}{}^{i}}\big(\mathcal D_{c}\psi{}_{i}\big) +\frac{313}{1536}\widehat G{}^{a}{}^{e}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\widehat R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{d}\big(\mathcal D^{f}\psi{}_{i}\big)\\
&-\frac{839i}{576}\widehat H{}^{a}{}^{b}\overline{\widehat R(Q){}_{b}{}^{c}{}^{i}}\big(\mathcal D_{c}\psi{}_{i}\big) -\frac{319}{768}\widehat H{}^{a}{}^{b}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\widehat R(Q){}^{c}{}^{d}{}^{i}}\gamma{}^{e}\big(\mathcal D^{f}\psi{}_{i}\big)\\
&+\frac{2645i}{36864}g\widehat G{}^{a}{}^{f}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\widehat R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{d}{}^{e}\varphi_c{}_{i} +\frac{5083i}{18432}g\widehat H{}^{a}{}^{b}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\widehat R(Q){}^{c}{}^{d}{}^{i}}\gamma{}^{e}{}^{f}\varphi_c{}_{i}\\
&-\frac{197i}{768}\epsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{f}\overline{\big(\mathcal D^{b}\widehat R(Q){}^{c}{}^{d}{}^{i}\big)}\gamma{}^{e}{}^{f}\big(\mathcal D_{e}\psi{}_{i}\big) +\frac{49i}{192}\epsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\big(\mathcal D^{b}\widehat R(Q){}^{c}{}^{d}{}^{i}\big)}\big(\mathcal D^{e}\psi{}_{i}\big)
\end{aligned}
\tag{SC7-EF2-1}
```

```math
\begin{aligned}
&+\frac{67}{256}g\epsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\big(\mathcal D^{b}\widehat R(Q){}^{c}{}^{d}{}^{i}\big)}\gamma{}^{e}\varphi_c{}_{i} +\frac{209i}{768}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\big(\mathcal D^{b}\widehat R(Q){}^{a}{}^{c}{}^{i}\big)}\gamma{}^{d}{}^{e}\big(\mathcal D^{f}\psi{}_{i}\big)\\
&+\frac{167}{384}\overline{\big(\mathcal D^{b}\widehat R(Q){}^{a}{}^{c}{}^{i}\big)}\gamma{}_{b}\big(\mathcal D_{c}\psi{}_{i}\big) +\frac{221i}{128}g\overline{\big(\mathcal D^{b}\widehat R(Q){}^{a}{}_{b}{}^{i}\big)}\varphi_c{}_{i}\\
&-\frac{217i}{768}\epsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\big(\mathcal D^{b}\widehat R(Q){}_{b}{}^{c}{}^{i}\big)}\gamma{}^{d}{}^{e}\big(\mathcal D^{f}\psi{}_{i}\big) -\frac{283}{768}\overline{\big(\mathcal D^{b}\widehat R(Q){}_{b}{}^{c}{}^{i}\big)}\gamma{}^{a}\big(\mathcal D_{c}\psi{}_{i}\big)\\
&-\frac{173}{256}\overline{\big(\mathcal D^{b}\widehat R(Q){}^{a}{}_{b}{}^{i}\big)}\gamma{}^{c}\big(\mathcal D_{c}\psi{}_{i}\big) +\frac{257i}{1536}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\big(\mathcal D^{a}\widehat R(Q){}^{b}{}^{c}{}^{i}\big)}\gamma{}^{d}{}^{e}\big(\mathcal D^{f}\psi{}_{i}\big)\\
&-\frac{1}{2}\epsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\big(\mathcal D^{c}\psi{}^{i}\big)}\gamma{}^{b}\big(\mathcal D^{d}\mathcal D^{e}\psi{}_{i}\big) -\frac{3i}{2}\overline{\big(\mathcal D_{b}\psi{}^{i}\big)}\gamma{}^{b}{}^{c}\big(\mathcal D_{c}\mathcal D^{a}\psi{}_{i}\big)\\
&+\frac{i}{2}\overline{\big(\mathcal D^{c}\psi{}^{i}\big)}\gamma{}^{a}{}^{b}\big(\mathcal D_{b}\mathcal D_{c}\psi{}_{i}\big) -\frac{i}{6}\overline{\big(\mathcal D_{b}\psi{}^{i}\big)}\gamma{}^{a}{}^{b}\big(\Box^c \psi{}_{i}\big)\\
&-\frac{5i}{2}\overline{\big(\mathcal D^{b}\psi{}^{i}\big)}\big(\mathcal D_{b}\mathcal D^{a}\psi{}_{i}\big) +\frac{i}{2}\overline{\big(\mathcal D^{a}\psi{}^{i}\big)}\gamma{}^{b}{}^{c}\big(\mathcal D_{b}\mathcal D_{c}\psi{}_{i}\big)\\
&+\frac{7i}{6}\overline{\big(\mathcal D^{a}\psi{}^{i}\big)}\big(\Box^c \psi{}_{i}\big) -\frac{7i}{6}\widehat H{}^{b}{}^{c}\epsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\big(\mathcal D^{d}\psi{}^{i}\big)}\big(\mathcal D^{e}\psi{}_{i}\big)\\
&-\frac{25i}{48}\widehat H{}^{b}{}^{c}\epsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\big(\mathcal D_{b}\psi{}^{i}\big)}\gamma{}^{d}{}^{e}\big(\mathcal D^{f}\psi{}_{i}\big) -\frac{11}{6}\widehat H{}^{a}{}^{b}\overline{\big(\mathcal D_{b}\psi{}^{i}\big)}\gamma{}^{c}\big(\mathcal D_{c}\psi{}_{i}\big)\\
&-\frac{1}{6}\widehat H{}^{b}{}^{c}\overline{\big(\mathcal D_{b}\psi{}^{i}\big)}\gamma{}^{a}\big(\mathcal D_{c}\psi{}_{i}\big) -\frac{23i}{32}\widehat H{}^{b}{}^{c}\epsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\big(\mathcal D^{f}\psi{}^{i}\big)}\gamma{}^{d}{}^{e}\big(\mathcal D_{f}\psi{}_{i}\big)\\
&+\frac{23i}{32}\widehat H{}^{b}{}^{c}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\big(\mathcal D^{a}\psi{}^{i}\big)}\gamma{}^{d}{}^{e}\big(\mathcal D^{f}\psi{}_{i}\big) -\frac{4}{3}\widehat H{}^{b}{}^{c}\overline{\big(\mathcal D^{a}\psi{}^{i}\big)}\gamma{}_{b}\big(\mathcal D_{c}\psi{}_{i}\big)\\
&-\frac{i}{12}gL_c{}^{i}{}^{j}\epsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\big(\mathcal D^{d}\psi{}_{i}\big)}\gamma{}^{b}{}^{c}\big(\mathcal D^{e}\psi{}_{j}\big) -\frac{1}{3}gL_c{}^{i}{}^{j}\overline{\big(\mathcal D^{b}\psi{}_{i}\big)}\gamma{}^{a}\big(\mathcal D_{b}\psi{}_{j}\big)\\
&+\frac{1}{3}gL_c{}^{i}{}^{j}\overline{\big(\mathcal D^{a}\psi{}_{i}\big)}\gamma{}^{b}\big(\mathcal D_{b}\psi{}_{j}\big) -\frac{i}{12}g\epsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\big(\mathcal D^{b}\varphi_c{}^{i}\big)}\gamma{}^{c}{}^{d}\big(\mathcal D^{e}\psi{}_{i}\big)\\
&-\frac{1}{6}g\overline{\big(\mathcal D^{b}\varphi_c{}^{i}\big)}\gamma{}_{b}\big(\mathcal D^{a}\psi{}_{i}\big) +\frac{7}{6}g\overline{\big(\mathcal D^{b}\varphi_c{}^{i}\big)}\gamma{}^{a}\big(\mathcal D_{b}\psi{}_{i}\big)\\
&+\frac{i}{4}g\epsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\varphi_c{}^{i}}\gamma{}^{b}{}^{c}\big(\mathcal D^{d}\mathcal D^{e}\psi{}_{i}\big) -\frac{1}{2}g\overline{\varphi_c{}^{i}}\gamma{}^{b}\big(\mathcal D_{b}\mathcal D^{a}\psi{}_{i}\big)\\
&+\frac{1}{6}g\overline{\varphi_c{}^{i}}\gamma{}^{a}\big(\Box^c \psi{}_{i}\big) -\frac{23}{12}g\widehat H{}^{b}{}^{c}\epsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\varphi_c{}^{i}}\gamma{}^{d}\big(\mathcal D^{e}\psi{}_{i}\big)\\
&-\frac{5i}{6}g\widehat H{}^{a}{}^{b}\overline{\varphi_c{}^{i}}\gamma{}_{b}{}^{c}\big(\mathcal D_{c}\psi{}_{i}\big) +\frac{5i}{6}g\widehat H{}^{b}{}^{c}\overline{\varphi_c{}^{i}}\gamma{}^{a}{}_{b}\big(\mathcal D_{c}\psi{}_{i}\big)\\
&+\frac{i}{2}g\widehat H{}^{a}{}^{b}\overline{\varphi_c{}^{i}}\big(\mathcal D_{b}\psi{}_{i}\big) +\frac{11i}{12}g^{2}L_c{}^{i}{}^{j}\overline{\varphi_c{}_{i}}\gamma{}^{a}{}^{b}\big(\mathcal D_{b}\psi{}_{j}\big)
\end{aligned}
\tag{SC7-EF2-2}
```

```math
\begin{aligned}
&+\frac{5i}{6}g^{2}\overline{\varphi_c{}^{i}}\gamma{}^{a}{}_{b}\big(\mathcal D^{b}\varphi_c{}_{i}\big) +\frac{5i}{48}\widehat G{}^{d}{}^{e}\epsilon{}^{a}{}_{b}{}_{c}{}_{e}{}_{f}\overline{\big(\mathcal D_{d}\psi{}^{i}\big)}\gamma{}^{b}{}^{c}\big(\mathcal D^{f}\psi{}_{i}\big)\\
&+\frac{7i}{48}\widehat G{}^{d}{}^{e}\epsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\big(\mathcal D_{b}\psi{}^{i}\big)}\gamma{}^{b}{}^{c}\big(\mathcal D^{f}\psi{}_{i}\big) -\frac{29i}{48}\widehat H{}^{b}{}^{c}\epsilon{}^{a}{}_{b}{}_{c}{}_{e}{}_{f}\overline{\big(\mathcal D_{d}\psi{}^{i}\big)}\gamma{}^{d}{}^{e}\big(\mathcal D^{f}\psi{}_{i}\big)\\
&+\frac{5i}{96}\widehat G{}^{d}{}^{e}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\big(\mathcal D^{a}\psi{}^{i}\big)}\gamma{}^{b}{}^{c}\big(\mathcal D^{f}\psi{}_{i}\big) -\frac{65}{256}\widehat G{}_{c}{}_{d}\overline{\widehat R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{a}\widehat R(Q){}_{b}{}^{d}{}_{i}\\
&-\frac{65}{64}\widehat H{}^{b}{}^{c}\overline{\widehat R(Q){}_{b}{}^{d}{}^{i}}\gamma{}^{a}\widehat R(Q){}_{c}{}_{d}{}_{i} -\frac{11i}{512}\widehat G{}_{b}{}^{g}\epsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g}\overline{\widehat R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{a}{}^{f}\widehat R(Q){}^{d}{}^{e}{}_{i}\\
&-\frac{11i}{128}\widehat H{}^{b}{}^{c}\epsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g}\overline{\widehat R(Q){}_{b}{}^{d}{}^{i}}\gamma{}^{a}{}^{g}\widehat R(Q){}^{e}{}^{f}{}_{i} -\frac{13i}{256}\widehat G{}_{b}{}^{f}\epsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\widehat R(Q){}^{b}{}^{c}{}^{i}}\widehat R(Q){}^{d}{}^{e}{}_{i}\\
&+\frac{13i}{64}\widehat H{}^{b}{}^{c}\epsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\widehat R(Q){}_{b}{}^{d}{}^{i}}\widehat R(Q){}^{e}{}^{f}{}_{i} -\frac{35i}{2048}\widehat G{}_{b}{}_{c}\epsilon{}^{a}{}_{d}{}_{e}{}_{f}{}_{g}\overline{\widehat R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{f}{}^{g}\widehat R(Q){}^{d}{}^{e}{}_{i}\\
&-\frac{35i}{512}\widehat H{}^{b}{}^{c}\epsilon{}^{a}{}_{d}{}_{e}{}_{f}{}_{g}\overline{\widehat R(Q){}_{b}{}_{c}{}^{i}}\gamma{}^{f}{}^{g}\widehat R(Q){}^{d}{}^{e}{}_{i} +\frac{7i}{512}\widehat G{}^{e}{}^{f}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\widehat R(Q){}^{a}{}^{b}{}^{i}}\widehat R(Q){}^{c}{}^{d}{}_{i}\\
&+\frac{7i}{128}\widehat H{}^{b}{}^{c}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\widehat R(Q){}^{a}{}^{d}{}^{i}}\widehat R(Q){}^{e}{}^{f}{}_{i} -\frac{23i}{512}\widehat G{}^{e}{}^{f}\epsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\widehat R(Q){}^{b}{}^{c}{}^{i}}\widehat R(Q){}_{b}{}^{d}{}_{i}\\
&-\frac{23i}{128}\widehat H{}^{b}{}^{c}\epsilon{}^{a}{}_{b}{}_{c}{}_{e}{}_{f}\overline{\widehat R(Q){}^{d}{}^{e}{}^{i}}\widehat R(Q){}_{d}{}^{f}{}_{i} -\frac{5i}{96}\widehat G{}^{d}{}^{e}\epsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\big(\mathcal D^{f}\psi{}^{i}\big)}\gamma{}^{b}{}^{c}\big(\mathcal D_{f}\psi{}_{i}\big)\\
&+\frac{19i}{1024}\widehat G{}_{b}{}^{g}\epsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g}\overline{\widehat R(Q){}^{a}{}^{b}{}^{i}}\gamma{}^{e}{}^{f}\widehat R(Q){}^{c}{}^{d}{}_{i} +\frac{19i}{256}\widehat H{}^{b}{}^{c}\epsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g}\overline{\widehat R(Q){}^{a}{}_{b}{}^{i}}\gamma{}^{f}{}^{g}\widehat R(Q){}^{d}{}^{e}{}_{i}\\
&-\frac{3i}{128}\widehat G{}_{c}{}^{g}\epsilon{}^{a}{}_{d}{}_{e}{}_{f}{}_{g}\overline{\widehat R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{e}{}^{f}\widehat R(Q){}_{b}{}^{d}{}_{i} -\frac{3i}{32}\widehat H{}^{b}{}^{c}\epsilon{}^{a}{}_{c}{}_{e}{}_{f}{}_{g}\overline{\widehat R(Q){}_{b}{}^{d}{}^{i}}\gamma{}^{f}{}^{g}\widehat R(Q){}_{d}{}^{e}{}_{i}\\
&-\frac{7i}{1024}\widehat G{}^{a}{}_{b}\epsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g}\overline{\widehat R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{f}{}^{g}\widehat R(Q){}^{d}{}^{e}{}_{i} -\frac{7i}{256}\widehat H{}^{a}{}^{b}\epsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g}\overline{\widehat R(Q){}_{b}{}^{c}{}^{i}}\gamma{}^{f}{}^{g}\widehat R(Q){}^{d}{}^{e}{}_{i}\\
&+\frac{i}{256}\widehat G{}_{b}{}_{d}\epsilon{}^{a}{}_{c}{}_{e}{}_{f}{}_{g}\overline{\widehat R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{f}{}^{g}\widehat R(Q){}^{d}{}^{e}{}_{i} +\frac{i}{64}\widehat H{}^{b}{}^{c}\epsilon{}^{a}{}_{d}{}_{e}{}_{f}{}_{g}\overline{\widehat R(Q){}_{b}{}^{d}{}^{i}}\gamma{}^{f}{}^{g}\widehat R(Q){}_{c}{}^{e}{}_{i}\\
&+\frac{i}{128}\widehat G{}^{f}{}^{g}\epsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g}\overline{\widehat R(Q){}^{a}{}^{b}{}^{i}}\gamma{}^{d}{}^{e}\widehat R(Q){}_{b}{}^{c}{}_{i} +\frac{i}{32}\widehat H{}^{b}{}^{c}\epsilon{}_{b}{}_{c}{}_{e}{}_{f}{}_{g}\overline{\widehat R(Q){}^{a}{}^{d}{}^{i}}\gamma{}^{f}{}^{g}\widehat R(Q){}_{d}{}^{e}{}_{i}\\
&-\frac{3}{32}\widehat G{}_{c}{}_{d}\overline{\widehat R(Q){}^{a}{}^{b}{}^{i}}\gamma{}^{d}\widehat R(Q){}_{b}{}^{c}{}_{i} +\frac{3}{8}\widehat H{}^{b}{}^{c}\overline{\widehat R(Q){}^{a}{}^{d}{}^{i}}\gamma{}_{c}\widehat R(Q){}_{b}{}_{d}{}_{i}\\
&+\frac{5i}{1024}\widehat G{}^{f}{}^{g}\epsilon{}^{a}{}_{d}{}_{e}{}_{f}{}_{g}\overline{\widehat R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{d}{}^{e}\widehat R(Q){}_{b}{}_{c}{}_{i} +\frac{5i}{256}\widehat H{}^{b}{}^{c}\epsilon{}^{a}{}_{b}{}_{c}{}_{f}{}_{g}\overline{\widehat R(Q){}^{d}{}^{e}{}^{i}}\gamma{}^{f}{}^{g}\widehat R(Q){}_{d}{}_{e}{}_{i}\\
&-\frac{i}{512}\widehat G{}_{b}{}_{f}\epsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{g}\overline{\widehat R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{f}{}^{g}\widehat R(Q){}^{d}{}^{e}{}_{i} -\frac{i}{128}\widehat H{}^{b}{}^{c}\epsilon{}^{a}{}_{d}{}_{e}{}_{f}{}_{g}\overline{\widehat R(Q){}_{b}{}^{d}{}^{i}}\gamma{}_{c}{}^{g}\widehat R(Q){}^{e}{}^{f}{}_{i}\\
&+\frac{i}{1024}\widehat G{}^{a}{}_{f}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{g}\overline{\widehat R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{f}{}^{g}\widehat R(Q){}^{d}{}^{e}{}_{i} +\frac{i}{256}\widehat H{}^{a}{}^{b}\epsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g}\overline{\widehat R(Q){}^{c}{}^{d}{}^{i}}\gamma{}_{b}{}^{g}\widehat R(Q){}^{e}{}^{f}{}_{i}
\end{aligned}
\tag{SC7-EF2-3}
```

```math
\begin{aligned}
&-\frac{7i}{1024}\widehat G{}_{f}{}^{g}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{g}\overline{\widehat R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{a}{}^{f}\widehat R(Q){}^{d}{}^{e}{}_{i} -\frac{7i}{256}\widehat H{}^{b}{}^{c}\epsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g}\overline{\widehat R(Q){}^{d}{}^{e}{}^{i}}\gamma{}^{a}{}_{b}\widehat R(Q){}^{f}{}^{g}{}_{i}\\
&+\frac{i}{2048}\widehat G{}_{f}{}_{g}\epsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\widehat R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{f}{}^{g}\widehat R(Q){}^{d}{}^{e}{}_{i} +\frac{i}{512}\widehat H{}^{b}{}^{c}\epsilon{}^{a}{}_{d}{}_{e}{}_{f}{}_{g}\overline{\widehat R(Q){}^{d}{}^{e}{}^{i}}\gamma{}_{b}{}_{c}\widehat R(Q){}^{f}{}^{g}{}_{i}\\
&-\frac{3i}{512}\widehat G{}_{e}{}^{g}\epsilon{}_{b}{}_{c}{}_{d}{}_{f}{}_{g}\overline{\widehat R(Q){}^{a}{}^{b}{}^{i}}\gamma{}^{e}{}^{f}\widehat R(Q){}^{c}{}^{d}{}_{i} -\frac{3i}{128}\widehat H{}^{b}{}^{c}\epsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g}\overline{\widehat R(Q){}^{a}{}^{d}{}^{i}}\gamma{}_{b}{}^{g}\widehat R(Q){}^{e}{}^{f}{}_{i}\\
&+\frac{3}{4}\widehat G{}^{a}{}^{c}\overline{\big(\mathcal D_{b}\psi{}^{i}\big)}\gamma{}^{b}\big(\mathcal D_{c}\psi{}_{i}\big) -\frac{11i}{6}g\widehat G{}^{a}{}^{b}\overline{\varphi_c{}^{i}}\big(\mathcal D_{b}\psi{}_{i}\big)\\
&-\frac{433}{4608}\widehat G{}^{e}{}^{f}\epsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{f}\overline{\widehat R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{d}\big(\mathcal D_{e}\psi{}_{i}\big) -\frac{83}{384}\widehat G{}_{d}{}^{e}\epsilon{}^{a}{}_{b}{}_{c}{}_{e}{}_{f}\overline{\widehat R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{d}\big(\mathcal D^{f}\psi{}_{i}\big)\\
&+\frac{503}{2304}\widehat H{}^{b}{}^{c}\epsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\widehat R(Q){}^{d}{}^{e}{}^{i}}\gamma{}^{f}\big(\mathcal D_{b}\psi{}_{i}\big) +\frac{5}{192}\widehat H{}^{b}{}^{c}\epsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\widehat R(Q){}^{d}{}^{e}{}^{i}}\gamma{}_{b}\big(\mathcal D^{f}\psi{}_{i}\big)\\
&-\frac{461i}{2048}g\widehat G{}_{d}{}^{f}\epsilon{}^{a}{}_{b}{}_{c}{}_{e}{}_{f}\overline{\widehat R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{d}{}^{e}\varphi_c{}_{i} -\frac{77i}{1024}g\widehat H{}^{b}{}^{c}\epsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\widehat R(Q){}^{d}{}^{e}{}^{i}}\gamma{}_{b}{}^{f}\varphi_c{}_{i}\\
&+\frac{1}{24}\widehat G{}^{e}{}^{f}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\widehat R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{d}\big(\mathcal D^{a}\psi{}_{i}\big) +\frac{107}{9216}\widehat G{}^{d}{}^{e}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\widehat R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{a}\big(\mathcal D^{f}\psi{}_{i}\big)\\
&-\frac{49}{192}\widehat H{}^{b}{}^{c}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\widehat R(Q){}^{d}{}^{e}{}^{i}}\gamma{}^{f}\big(\mathcal D^{a}\psi{}_{i}\big) +\frac{469}{4608}\widehat H{}^{b}{}^{c}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\widehat R(Q){}^{d}{}^{e}{}^{i}}\gamma{}^{a}\big(\mathcal D^{f}\psi{}_{i}\big)\\
&+\frac{5i}{256}g\widehat G{}^{e}{}^{f}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\widehat R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{a}{}^{d}\varphi_c{}_{i} -\frac{27i}{128}g\widehat H{}^{b}{}^{c}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\widehat R(Q){}^{d}{}^{e}{}^{i}}\gamma{}^{a}{}^{f}\varphi_c{}_{i}\\
&+\frac{4i}{3}\overline{\big(\mathcal D_{b}\psi{}^{i}\big)}\gamma{}^{b}{}^{c}\big(\mathcal D^{a}\mathcal D_{c}\psi{}_{i}\big) +\frac{4i}{3}\overline{\big(\mathcal D^{b}\psi{}^{i}\big)}\big(\mathcal D^{a}\mathcal D_{b}\psi{}_{i}\big)\\
&-g\overline{\big(\mathcal D^{a}\varphi_c{}^{i}\big)}\gamma{}^{b}\big(\mathcal D_{b}\psi{}_{i}\big) +\frac{i}{4}\widehat G{}^{b}{}^{c}\epsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\big(\mathcal D^{d}\psi{}^{i}\big)}\big(\mathcal D^{e}\psi{}_{i}\big)\\
&+\frac{1}{4}g\widehat G{}^{c}{}^{d}\epsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\varphi_c{}^{i}}\gamma{}^{b}\big(\mathcal D^{e}\psi{}_{i}\big) +\frac{211i}{144}gL_c{}^{i}{}^{j}\overline{\widehat R(Q){}^{a}{}^{b}{}_{i}}\big(\mathcal D_{b}\psi{}_{j}\big)\\
&+\frac{103}{288}gL_c{}^{i}{}^{j}\epsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\widehat R(Q){}^{b}{}^{c}{}_{i}}\gamma{}^{d}\big(\mathcal D^{e}\psi{}_{j}\big) -\frac{499i}{2304}g^{2}L_c{}^{i}{}^{j}\epsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\widehat R(Q){}^{b}{}^{c}{}_{i}}\gamma{}^{d}{}^{e}\varphi_c{}_{j}\\
&+\frac{259}{4608}\widehat G{}^{e}{}^{f}\epsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\widehat R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{d}\big(\mathcal D_{b}\psi{}_{i}\big) +\frac{533}{2304}\widehat H{}^{b}{}^{c}\epsilon{}^{a}{}_{b}{}_{c}{}_{e}{}_{f}\overline{\widehat R(Q){}^{d}{}^{e}{}^{i}}\gamma{}^{f}\big(\mathcal D_{d}\psi{}_{i}\big)\\
&-\frac{437i}{1536}\epsilon{}^{a}{}_{b}{}_{d}{}_{e}{}_{f}\overline{\big(\mathcal D^{b}\widehat R(Q){}^{c}{}^{d}{}^{i}\big)}\gamma{}^{e}{}^{f}\big(\mathcal D_{c}\psi{}_{i}\big) -\frac{39i}{1024}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\big(\mathcal D^{b}\widehat R(Q){}^{c}{}^{d}{}^{i}\big)}\gamma{}^{e}{}^{f}\big(\mathcal D^{a}\psi{}_{i}\big)\\
&+\frac{95i}{768}\epsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\big(\mathcal D^{b}\widehat R(Q){}^{c}{}^{d}{}^{i}\big)}\gamma{}^{e}{}^{f}\big(\mathcal D_{b}\psi{}_{i}\big) +\frac{13i}{128}\epsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\widehat R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{d}{}^{e}\big(\Box^c \psi{}_{i}\big)\\
&+\frac{35i}{1536}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\big(\mathcal D^{b}\widehat R(Q){}^{c}{}^{d}{}^{i}\big)}\gamma{}^{a}{}^{e}\big(\mathcal D^{f}\psi{}_{i}\big) +\frac{i}{16}\epsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\widehat R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{d}{}^{e}\big(\mathcal D^{f}\mathcal D_{b}\psi{}_{i}\big)
\end{aligned}
\tag{SC7-EF2-4}
```

```math
\begin{aligned}
&-\frac{i}{32}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\widehat R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{a}{}^{d}\big(\mathcal D^{e}\mathcal D^{f}\psi{}_{i}\big) +\frac{1}{3}g\overline{\varphi_c{}^{i}}\gamma{}^{b}\big(\mathcal D^{a}\mathcal D_{b}\psi{}_{i}\big)\\
&-\frac{i}{32}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\widehat R(Q){}^{a}{}^{b}{}^{i}}\gamma{}^{c}{}^{d}\big(\mathcal D^{e}\mathcal D^{f}\psi{}_{i}\big) -\frac{i}{64}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\widehat R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{d}{}^{e}\big(\mathcal D^{f}\mathcal D^{a}\psi{}_{i}\big)\\
&-\frac{i}{64}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\widehat R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{d}{}^{e}\big(\mathcal D^{a}\mathcal D^{f}\psi{}_{i}\big) +\frac{i}{16}\epsilon{}^{a}{}_{b}{}_{c}{}_{e}{}_{f}\overline{\widehat R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{d}{}^{e}\big(\mathcal D^{f}\mathcal D_{d}\psi{}_{i}\big)\\
&+\frac{3}{32}g\epsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\widehat R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{e}\big(\mathcal D^{d}\varphi_c{}_{i}\big) +\frac{13i}{16}g\overline{\widehat R(Q){}^{a}{}^{b}{}^{i}}\big(\mathcal D_{b}\varphi_c{}_{i}\big)\\
&+\frac{23i}{3072}gL_c{}^{i}{}^{j}\epsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\widehat R(Q){}^{b}{}^{c}{}_{i}}\gamma{}^{e}{}^{f}\widehat R(Q){}_{b}{}^{d}{}_{j} -\frac{17}{1024}gL_c{}^{i}{}^{j}\overline{\widehat R(Q){}^{b}{}^{c}{}_{i}}\gamma{}^{a}\widehat R(Q){}_{b}{}_{c}{}_{j}\\
&-\frac{5i}{6144}gL_c{}^{i}{}^{j}\epsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\widehat R(Q){}^{b}{}^{c}{}_{i}}\widehat R(Q){}^{d}{}^{e}{}_{j} -\frac{i}{192}gL_c{}^{i}{}^{j}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\widehat R(Q){}^{a}{}^{b}{}_{i}}\gamma{}^{e}{}^{f}\widehat R(Q){}^{c}{}^{d}{}_{j}\\
&-\frac{1}{4}\widehat G{}^{b}{}^{c}\overline{\big(\mathcal D_{b}\psi{}^{i}\big)}\gamma{}^{a}\big(\mathcal D_{c}\psi{}_{i}\big)
\end{aligned}
\tag{SC7-EF2-5}
```

<!-- SUPERCOVARIANT_COMPONENTS_END -->

<a id="65-bf-current-and-action"></a>

### BF current and action

The defining vector leg is $`(1,C_\mu,0,-gL_c^{ij}/2)`$. The composite linear leg is exactly the four slots in §§6.1–6.4. The independent $`c`$ multiplet receives the compensator gauge; the LOG triplet does not.

Substitute this defining vector into the full density (master A01, LOG-S1-16). Its $`i\bar\lambda\varphi_{\log}`$ and $`-\bar\psi_a^i\gamma^a\lambda^jL_{\log ij}/2`$ terms vanish because they contain an undifferentiated dilatino. The descendants of that dilatino already present inside the LOG slots remain. The ordinary current and the compact action are

```math
\boxed{P_{\log}^a=\left[E_{\log}^a+\frac i2\bar\psi_b\gamma^{ba}\varphi_{\log}+\frac14\bar\psi_b^i\gamma^{abc}\psi_c^jL_{\log ij}\right]_{\le2}+\text{high fermi terms}.}
\tag{SC7-50}
```

```math
\boxed{e^{-1}\mathcal L_{\log}^{\rm gauged}=\left[N_{\log}-\frac g2L_c^{ij}L_{\log ij}+C_aP_{\log}^a+\frac12\bar\psi_a\gamma^a\varphi_{\log}+\frac i4\bar\psi_a^i\gamma^{ab}\psi_b^jL_{\log ij}\right]_{\le2}+\text{high fermi terms}.}
\tag{SC7-51}
```

Displaying the current contributions and aligned triplet coefficient gives

```math
\begin{aligned}
e^{-1}\mathcal L_{\log}^{\rm gauged}={}&\left[N_{\log}-\frac{gL}{2\sqrt2}\delta^{ij}L_{\log ij}+C_aE_{\log}^a+\frac12\bar\psi_a\gamma^a\varphi_{\log}+\frac i2C_a\bar\psi_b\gamma^{ba}\varphi_{\log}\right.\\
&\left.\qquad+\frac i4\bar\psi_a^i\gamma^{ab}\psi_b^jL_{\log ij}+\frac14C_a\bar\psi_b^i\gamma^{abc}\psi_c^jL_{\log ij}\right]_{\le2}+\text{high fermi terms}.
\end{aligned}\tag{SC7-52}
```

Use the even components through degree two in the first three terms, the one-fermion spinor in the next two, and the degree-zero triplet in the last two. The implicit degree-two parts of the covariants in an explicitly bosonic term remain included. No second projection factor is applied: the established $`(-2,-2i,-1,+1)`$ slot bridge has already been used in the input.

With the present full derivative convention the linear-multiplet constraint has its source form

```math
\boxed{\mathcal D^aE_{\log a}=0\quad\text{through the retained order}.}
\tag{SC7-53}
```

This constraint is now certified by full-primary linearity and the closed-four-form identity with the full R(Q) gamma trace. The proof and its polynomial premises are in the current certification report; it does not claim a separate brute-force expansion of the divergence of every canonical vector term. It includes the Q/S completions of master L02. It is distinct from the ordinary-current statement $`\partial_\mu(eP_{\log}^\mu)=0`$ in the operational potential representation. The generic current/potential interface FORM-01 is resolved by the complete superform pullback; its literal source discrepancy is explicitly recorded in the certification report.

The bosonic density is $`\ell_{\log}^{(0)}=N_{\log}^{(0)}-gL_c^{ij}L_{\log ij}^{(0)}/2+C_aE_{\log}^{a(0)}`$. Its covariant derivatives still contain bosonic S/K-descendant structure; for example $`\Box^c\sigma|_{\rm bosonic,gauge}=2f_a{}^a=-R/8`$. The independent compensator is kept off shell. The later independent complete bosonic reduction reproduces LOG-CORR05 with the explicit boundary current; see the certification report and its exact equation transcript.

<a id="7-convention-dependence-and-remaining-uncertainties"></a>

## Convention Dependence and Scope

The active derivative convention is the fermionic Weyl-squared GC21 convention, evaluated with the gauged composites. It is not a new gauge-preserving Poincaré derivative obtained by silently removing the S/K generators. The gauge evaluation applies after every ordered derivative, as defined explicitly in §3.1.

All algebraic $`Y,T,\chi,D`$ occurrences have been substituted before that evaluation. The full connection dependence of the curvatures, strengths, $`\Box^c\sigma`$ and differentiated dilatino remains implicit by the stated instruction. It must be included when a later component expansion, variation or spectrum calculation is carried out. The dependent-connection solutions are in this same file, (SC7-06).

Canonicality and the performed checks have the algebraic scope stated in §§1 and 5. The generic FORM-01 interface, retained-order reality and complete bosonic comparison are certified in the later audit. Full defining-projector equality, all-order primary constraints and retained-order BF supersymmetry through the linear-multiplet/superform theorem are certified separately in [the current report](component_construction/results/gauged_full_fermionic_log/CERTIFICATION_LOG_TWO_FERMI_2026-09-25.md). Unrestricted higher-fermion action terms and any spectrum calculation remain outside this retained-order result.
