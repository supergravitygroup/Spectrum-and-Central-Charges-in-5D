# Gauged LOG invariant with full supercovariant derivatives

<!-- LOG_CURRENT_CERTIFICATION_20260925 -->

**Current scope:** [the 2026-09-25 certificate](../../../CERTIFICATION_LOG_TWO_FERMI_2026-09-25.md) verifies the full primary and the component action through two physical fermions. The source comparisons and restricted tests below retain their stated mathematical scope.

**Derivative convention.** All component derivatives below use the same $`\mathcal D_a`$ and $`\Box^c`$ as [the fermionic gauged Weyl-squared calculation](../../../../../../../../../weyl2/action/details/construction.md), GC14–GC24. Their Q/S/K connections and implicit fermions remain inside them.

## Contents

1. [Problem and Target](derivation.md#1-problem-and-target)
2. [Convention Ledger](derivation.md#2-convention-ledger)
3. [Definitions and Required Identities](derivation.md#3-definitions-and-required-identities)
4. [Detailed Derivation](derivation.md#4-detailed-derivation), including the [gauge-fixed derivative dictionary](derivation.md#gauge-fixed-derivatives)
5. [Consistency Checks](derivation.md#5-consistency-checks)
6. [Final Result](derivation.md#6-final-result): triplet, spinor, scalar, vector, [BF action](bf_result.md#65-bf-current-and-action)
7. [Convention Dependence and Remaining Uncertainties](bf_result.md#7-convention-dependence-and-remaining-uncertainties)

## 1. Problem and Target

**Goal.** Present the gauged, gauge-evaluated LOG multiplet and BF density with all derivatives fully supercovariant, all four algebraic Weyl composites $`Y,T,\chi,D`$ substituted, curvature tensors retained, and the tensor/Clifford contractions canonicalized. The dependent $`\omega,\phi,f`$ relations are given in the same file; their occurrences inside derivatives and curvatures are kept implicit.

**Starting point.** The full-derivative polynomials in [the canonical two-fermion LOG multiplet](../../../LOG_MULTIPLET_CANONICAL_TWO_FERMI.md), obtained from [Step 6](../../../STEP_06_LOG_PROJECTED_MULTIPLET_AND_BOSONIC_ACTION.md). We return to those polynomials before the former expansion of the Q/S/K connections. The old expanded component sums are not reused with a changed derivative symbol.

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

The calculation uses the [main conventions](../../../CONVENTIONS.md) and [LOG conventions](../../../LOG_CONVENTIONS.md). Literal source expressions are distinguished from corrected component formulas.

## 2. Convention Ledger

<!-- ASSERT_CONVENTION: metric_signature=(-,+,+,+,+), natural_units=hbar=c=1, gamma_volume=+i, bar=linear Majorana, derivative=full supercovariant mathcal D, derivative_order=preserved, source_lock=GAUGED-LOG-CONVENTIONS-v1 -->

Tangent/world indices run over five dimensions, spinor indices over four components, and $`i,j=1,2`$. Use $`\eta=(-,+,+,+,+)`$, $`\epsilon^{01234}=1`$, $`\gamma^{01234}=i`$, $`\{\gamma^a,\gamma^b\}=2\eta^{ab}`$, and unit-weight (anti)symmetrization. The Majorana bar is linear, $`\bar u=u^T\mathsf C`$, including on a coefficient $`i`$; spinors are odd. Right lowering is $`u_i=u^j\varepsilon_{ji}`$ with $`\varepsilon_{12}=\varepsilon^{12}=1`$. The fixed-doublet bilinear exchange signs for gamma rank $`0,1,2`$ are $`+,+,-`$; a contracted doublet reversal supplies its separate minus.

Use the project Riemann sign $`R_{\mu\nu}{}^{ab}(\omega)=2\partial_{[\mu}\omega_{\nu]}{}^{ab}+2\omega_{[\mu}{}^{ac}\omega_{\nu]c}{}^b`$. The Ricci contraction is fixed by (SC7-06). Before gauge evaluation the conformal weights of $`(\sigma,\psi^i,\widehat G,\widehat H_{ab},L_c,\varphi_c,N_c,g)`$ are $`(1,3/2,2,3,3,7/2,4,0)`$. On the fixed scale their engineering dimensions are $`(0,1/2,1,1,0,1/2,1,1)`$; $`\mathcal D_a`$ has dimension one. The LOG slots have dimensions $`3,7/2,4,4`$. The coupling is $`S=(2\kappa_5^2)^{-1}\int e(\ell_{2\partial}+\lambda_{\rm LOG}\ell_{\log})`$, $`[\lambda_{\rm LOG}]=-2`$.

There is one component derivative convention throughout the active calculation: $`\mathcal D_a`$ is full and supercovariant. $`D`$ without an index is the auxiliary scalar; it is never a derivative. Gold's $`\nabla_A`$ remains its source superspace notation in the earlier superspace derivations; the bridge is applied once at Step 6. Fourier/state normalization and renormalization are not involved.

## 3. Definitions and Required Identities

### 3.1 Full derivative, box and gauge evaluation

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

### 3.2 Strengths, curvature constraints and dependent connections

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

### 3.3 Gauged composite identities before differentiation

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

## 4. Detailed Derivation

### 4.1 Recover the gauge values without changing the derivative

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

### 4.2 Differentiate before evaluating the gauge

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

### 4.3 Substitute into the LOG slots and canonicalize

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

### 4.4 Gauge-fixed derivative dictionary — reference only

This section supplies the gauge-evaluated derivatives that were left implicit in (SC7-03). **None of these formulas is inserted into the LOG multiplet or the BF density in §6.** Throughout this section a vertical bar means (SC7-02), after taking the indicated full supercovariant derivatives. The dilatino is $`\psi^i`$; the gravitino is $`\psi_a^i`$. The S connection is $`\phi_a^i`$; the independent compensator spinor is $`\varphi_c^i`$.

**Sources and scope.** First derivatives: Weyl-squared GC14, equivalently master V01–V03 and OP (2.14)–(2.16). Scalar box: Weyl-squared GC16. Connection solutions and transformations: Weyl-squared GC18–GC20 and master R04a–R04c, anchored to W (3.9)–(3.12), (3.20)–(3.21). The Hessians and spinor box below are derived from these definitions. They are off shell, retain two fermions for the scalar and one for the spinor, and use no integration by parts or background equation. Higher omitted degrees are denoted $`+\text{high fermi terms}`$. The truncation is a formal fermion-degree truncation, not a small-curvature approximation.

<!-- ASSERT_CONVENTION: metric_signature=(-,+,+,+,+), gamma_volume=+i, bar=linear Majorana, derivative=full supercovariant mathcal D, derivative_order=preserved, gauge_evaluation=after differentiation -->

#### 4.4.1 First derivatives and the Dirac derivative

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

#### 4.4.2 Scalar Hessian and conformal box

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

#### 4.4.3 Transformations needed for the spinor Hessian

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

#### 4.4.4 Full second derivative of the dilatino

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

#### 4.4.5 Gauge-fixed spinor box with the algebraic composites inserted

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

#### 4.4.6 Inverse powers and higher ordered boxes

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

## 5. Consistency Checks

<!-- SUPERCOVARIANT_CHECKS -->

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

These are exact rational-complex polynomial comparisons, not numerical samples or equality of term counts. Neither side of this decisive comparison contains an expanded $`f_{ab}`$, primed Ricci tensor or explicit S connection. The [comparison script](../../../../../../../../../references/source_evidence/log/results/gauged_full_fermionic_log/scripts/verify_log_derivative_equivalence_covariant.py), [projector reduction](../../../../../../../../../references/source_evidence/log/results/gauged_full_fermionic_log/scripts/verify_log_derivative_equivalence_projector.py), [common-basis evidence](../../../../../EXTERNAL_REFERENCES.md#ref-37ce0601c58b) and [derivation of the equivalence test](../../../../../EXTERNAL_REFERENCES.md#ref-2ba366a06e84) record the inputs and reductions. The inverse uses the same algebraic map as the forward construction; its coefficient correctness is checked separately by the [independent ungauged-template test](../../../../../../../../../references/source_evidence/log/results/gauged_full_fermionic_log/scripts/verify_log_ungauged_composite_templates.py), which retains a nonconstant dilaton and a nonzero dilatino and passes 21 matrix/Grassmann comparisons with maximum relative residual $`3.50\times10^{-15}`$.

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

### 5.3 Component verification

The source-local super-Jacobi identity fixes the two K-generator coefficients in C24 (A.1l) to $`+i/8,-i/4`$. These coefficients are used in the scalar and vector descents. Substitution, ordered differentiation, gauge evaluation and canonicalization give the four gauged polynomials in §6 with 13, 94, 141 and 373 terms. Derivatives of the gauge-fixed dilatino and scalar remain as defined covariants.

All corrected unfixed and gauged canonical components pass the [exact coefficient-phase reality check](../../../../../../../../../references/source_evidence/log/results/gauged_full_fermionic_log/sources/certification_20260925/canonical/reality_phase_after_correction.json). The independent [complete displayed-polynomial evaluation](../../../../../../../../../references/source_evidence/log/results/gauged_full_fermionic_log/sources/certification_20260925/canonical/all_terms_seed_926255_rho_1_printed.json) covers all 179,396 Step 6 terms; this numerical cross-check is additional evidence, not an unrestricted proof by sampling or a claim about every internal floating-point contraction.

The [full superform reconstruction](../../../../../../../../../references/source_evidence/log/derivations/form-interface.md) closes the generic current, potential and BF interface. The complete [bosonic comparison](../../../../../../../../../references/source_evidence/log/derivations/bosonic.md) reproduces LOG-CORR05 including flux, derivative and compensator terms, with the explicit boundary current retained. The [certification report](../../../CERTIFICATION_LOG_TWO_FERMI_2026-09-25.md) records the separate curved-primary, defining-projector and retained-order supersymmetry gates.

## 6. Final Result

All four sums below have the algebraic composites substituted, retain full supercovariant curvatures and derivatives, and obey the gauge-evaluation convention after (SC7-02). They are collected by **explicit** fermion degree. The outer projection counts implicit fermions in every strength, derivative and curvature as well:

```math
\left[\prod_rB_r\right]_{\le2}=\prod_rB_r^{(0)}+\sum_sB_s^{(2)}\prod_{r\ne s}B_r^{(0)},\qquad
[B\bar u\Gamma v]_{\le2}=B^{(0)}\overline{u^{(1)}}\Gamma v^{(1)},\qquad [Bu]_{\le2}=B^{(0)}u^{(1)}.
\tag{SC7-23}
```

Each consecutive display under a component/degree heading continues the same sum; two summands are printed per row. $`\widehat G^2=\widehat G_{ab}\widehat G^{ab}`$; $`L_c^{ij}L_{cij}=L^2`$. The ordered descendants of the fixed dilaton/dilatino are intentional defined covariants and must not be set to zero.
