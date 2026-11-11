# Superconformal derivatives, field strengths and the BF relation

Source: Mehmet Ozkan, *Off-shell N = 2 linear multiplets in five dimensions*, JHEP 11 (2016) 157, multiplets.pdf. Equations used: (3.1)–(3.15), (3.20)–(3.21), (A.3)–(A.7), (A.9), (A.10). Local convention source: [CONVENTIONS.md](../../r2/action/details/component_maps/gR2/CONVENTIONS.md).

This record contains the shared **source superconformal definitions before gauge fixing** for the following three files:

- [composite_vector_multiplet.md](linear_vector_construction.md),
- [composite_linear_multiplet.md](../../r2/action/details/component_maps/gR2/composite_linear_multiplet.md),
- [BFaction.md](../../r2/action/details/component_maps/gR2/BFaction.md).

Unlabeled formulas use the corrected expressions in the shared convention dictionary; source expressions are identified separately.

<a id="1-symbols-and-scope"></a>

## Symbols and scope

```math
\begin{gathered}
\mathcal D_a=e_a{}^\mu\mathcal D_\mu,\qquad
\partial_a=e_a{}^\mu\partial_\mu,\qquad
\mathord{\not{\mathcal D}}=\gamma^a\mathcal D_a,\\
\mathord{\not{E}}_A=\gamma^aE_{Aa},\qquad
\gamma\!\cdot\!T=\gamma^{ab}T_{ab},\qquad
\gamma\!\cdot\!\widehat F_A=\gamma^{ab}\widehat F_{Aab},\\
T^2\equiv T_{ab}T^{ab},\qquad
D\equiv D_{\mathrm{aux}},\qquad
\Box^c\equiv\square^c.
\end{gathered}
```

Here $`D_{\mathrm{aux}}`$ is the auxiliary scalar, not the spacetime dimension or covariant-derivative operator. Dot contractions contain no $`1/2!`$. $`A`$ is a multiplet label, always placed at the start of the subscript group; it is neither a Lorentz nor an SU(2) index. Vector components are written as $`\rho_A`$, $`\lambda_A^i`$, $`\lambda_{Ai}`$, $`Y_A^{ij}`$, $`Y_{Aij}`$, $`A_{A\mu}`$ and $`\widehat F_{Aab}`$. Lorentz and SU(2) index positions are retained. Upper or lower placement of a label in the source does not define different multiplets; the same label of the same field denotes the same multiplet across these files. General vector definitions apply to each $`A`$ label. Unlabeled $`L_{ij}`$ and $`L_{1ij}`$ are distinct objects.

```math
\psi_\mu^i:\ Q\text{-connection (gravitino)},\qquad
\phi_\mu^i:\ S\text{-connection},\qquad
\varphi_A^i:\ \text{linear-multiplet fermion}.
```

$`\phi_\mu^i`$ and $`\varphi_A^i`$ are different fields. $`\lambda_A^i`$ is a general vector-multiplet fermion; it is not automatically identical to the defining-vector dilatino set to zero by gauge fixing. $`b_\mu,V_\mu{}^{ij}`$ are the full source connections. $`\omega_\mu{}^{ab},\phi_\mu^i,f_\mu{}^a`$ are the source's dependent connections, defined in Section 4.

Here $`\mathcal D`$ is the full superconformal derivative. It is not identified with the project's residual-$`U(1)_R`$ derivatives, ordinary $`\partial`$ or torsion-free $`\nabla`$. No gauge choice, fermion truncation, auxiliary-field elimination or conversion to the gauged target representation has been applied.

All bilinears with suppressed SU(2) indices use

```math
\bar X\Gamma Y=\bar X^i\Gamma Y_i,\qquad
X_i=X^j\epsilon_{ji},\qquad
\epsilon_{12}=\epsilon^{12}=1
```

Upper SU(2) indices in the source equations below are retained; explicit lowering operations are supplied for lower-index components.

<a id="2-general-vector-multiplet-39-310-321"></a>

## General vector multiplet: (3.9), (3.10), (3.21)

<a id="21-ordinary-and-supercovariant-field-strengths"></a>

### Ordinary and supercovariant field strengths

```math
\begin{aligned}
F_{A\mu\nu}&\equiv2\partial_{[\mu}A_{A\nu]},\\
\widehat F_{A\mu\nu}
&=F_{A\mu\nu}
-\bar\psi_{[\mu}\gamma_{\nu]}\lambda_A
+\frac{i}{2}\rho_A\bar\psi_{[\mu}\psi_{\nu]},\\
F_{Aab}&=e_a{}^\mu e_b{}^\nu F_{A\mu\nu},\qquad
\widehat F_{Aab}=e_a{}^\mu e_b{}^\nu\widehat F_{A\mu\nu}.
\end{aligned}
```

The second line is source (3.9). $`\widehat F_A`$ is not an ordinary curl. The inverse expansion of this definition is applied to the $`A_{1a}`$ field of the BF action in Section 5.

<a id="22-first-derivatives"></a>

### First derivatives

As printed in source (3.10):

```math
\boxed{
\begin{aligned}
\mathcal D_\mu\rho_A
={}&\partial_\mu\rho_A-b_\mu\rho_A
-\frac{i}{2}\bar\psi_\mu\lambda_A,\\
\mathcal D_\mu\lambda_A^i
={}&\left(\partial_\mu-\frac32b_\mu
+\frac14\omega_\mu{}^{ab}\gamma_{ab}\right)\lambda_A^i
-V_\mu{}^{ij}\lambda_{Aj}\\
&+\frac14(\gamma\!\cdot\!\widehat F_A)\psi_\mu^i
+\frac{i}{2}(\mathord{\not{\mathcal D}}\rho_A)\psi_\mu^i
+Y_A^{ij}\psi_{\mu j}
-\rho_A(\gamma\!\cdot\!T)\psi_\mu^i
-\rho_A\phi_\mu^i.
\end{aligned}}
```

For the composite linear multiplet using the lower-index fermion,

```math
\begin{aligned}
\mathcal D_\mu\lambda_{Ai}
&=(\mathcal D_\mu\lambda_A^j)\epsilon_{ji},\\
(S^{jk}X_k)\epsilon_{ji}
&=S^{jk}X^\ell\epsilon_{\ell k}\epsilon_{ji}
=-S_{i\ell}X^\ell
\qquad(S^{jk}=S^{kj}),\\
\mathcal D_\mu\lambda_{Ai}
&=\left(\partial_\mu-\frac32b_\mu
+\frac14\omega_\mu{}^{ab}\gamma_{ab}\right)\lambda_{Ai}
+V_{\mu ij}\lambda_A^j\\
&\quad+\frac14(\gamma\!\cdot\!\widehat F_A)\psi_{\mu i}
+\frac{i}{2}(\mathord{\not{\mathcal D}}\rho_A)\psi_{\mu i}
-Y_{Aij}\psi_\mu^j
-\rho_A(\gamma\!\cdot\!T)\psi_{\mu i}
-\rho_A\phi_{\mu i}.
\end{aligned}
```

Thus the lower-index equality has a positive $`V`$ term and a negative $`Y`$ term. The phase discrepancy between the SUSY rule in (3.8) and (3.10) is recorded in Section 6.1.

<a id="23-scalar-superconformal-dalembertian"></a>

### Scalar superconformal d'Alembertian

Source (3.21):

```math
\boxed{
\begin{aligned}
\Box^c\rho_A
={}&\left(\partial^a-2b^a+\omega_b{}^{ba}\right)
\mathcal D_a\rho_A
-\frac{i}{2}\bar\psi_a\mathcal D^a\lambda_A
-2\rho_A\bar\psi_a\gamma^a\chi\\
&+\frac12\bar\psi_a\gamma^a(\gamma\!\cdot\!T)\lambda_A
+\frac12\bar\phi_a\gamma^a\lambda_A
+2f_a{}^a\rho_A.
\end{aligned}}
```

$`f_a{}^a=e_a{}^\mu f_\mu{}^a`$ is the trace of the dependent $`K`$ connection. It is not directly replaced by the ordinary Ricci scalar in the exact expression.

<a id="3-linear-multiplet-37-315-and-source-discrepancy"></a>

## Linear multiplet: (3.7), (3.15) and source discrepancy

<a id="31-triplet-and-constrained-vector-derivatives"></a>

### Triplet and constrained-vector derivatives

Source (3.7):

```math
\boxed{
\begin{aligned}
\mathcal D_\mu L_A^{ij}
={}&\partial_\mu L_A^{ij}-3b_\mu L_A^{ij}
+2V_\mu{}^{(i}{}_kL_A^{j)k}
-i\bar\psi_\mu^{(i}\varphi_A^{j)},\\
\mathcal D_\mu E_{Aa}
={}&\partial_\mu E_{Aa}-4b_\mu E_{Aa}
+\omega_{\mu ab}E_A^b
+\frac{i}{2}\bar\psi_\mu\gamma_{ab}\mathcal D^b\varphi_A\\
&-2\bar\psi_\mu\gamma^b\varphi_A T_{ab}
+2\bar\phi_\mu\gamma_a\varphi_A.
\end{aligned}}
```

Source constraint (3.2) is $`\mathcal D_aE_A^a=0`$. In these equalities, $`E_A^a`$ is the full supercovariant component; its relation to $`P_A^a`$, the dual of the ordinary curl, is given in Section 5.2.

<a id="32-fermion-derivative-corrected-definition-and-check"></a>

### Fermion derivative: corrected definition and check

**Definition used:** The coefficient of the $`\mathord{\not{\mathcal D}}L`$ term in (3.7) is corrected to $`i/2`$ by the supercovariance check below.

```math
\begin{aligned}
\mathcal D_\mu\varphi_A^i
={}&\left(\partial_\mu-\frac72b_\mu
+\frac14\omega_\mu{}^{ab}\gamma_{ab}\right)\varphi_A^i
-V_\mu{}^{ij}\varphi_{Aj}\\
&+\frac{i}{2}(\mathord{\not{\mathcal D}}L_A^{ij})\psi_{\mu j}
+\frac{i}{2}\mathord{\not{E}}_A\psi_\mu^i
-\frac12N_A\psi_\mu^i
+(\gamma\!\cdot\!T)L_A^{ij}\psi_{\mu j}
-3L_A^{ij}\phi_{\mu j}.
\end{aligned}
```

For the same independent field structure, source (3.1) gives

```math
\delta_Q\varphi_A^i\supset
-\frac{i}{2}(\mathord{\not{\mathcal D}}L_A^{ij})\epsilon_j,
\qquad
\delta_Q\psi_{\mu j}\supset\partial_\mu\epsilon_j
\quad\text{[(A.3)]}
```

To check the Q-connection coefficient, temporarily write $`c(\mathord{\not{\mathcal D}}L_A^{ij})\psi_{\mu j}`$. The coefficient of this independent $`\partial\epsilon`$ structure is

```math
\begin{aligned}
\left.\delta_Q(\mathcal D_\mu\varphi_A^i)\right|_{
(\mathord{\not{\mathcal D}}L_A^{ij})\partial_\mu\epsilon_j}
&=-\frac{i}{2}+c,\\
c_{\mathrm{printed}}=\frac12
&\quad\Longrightarrow\quad\frac{1-i}{2}\neq0,\\
-\frac{i}{2}+c=0
&\quad\Longrightarrow\quad c=\frac{i}{2}.
\end{aligned}
```

Thus the correction required by supercovariance compatibility with (3.1), and applied in this record only to this term, is

```math
\boxed{
\frac12(\mathord{\not{\mathcal D}}L_A^{ij})\psi_{\mu j}
\ \longrightarrow\
\frac{i}{2}(\mathord{\not{\mathcal D}}L_A^{ij})\psi_{\mu j}.}
```

Equivalently

```math
\mathcal D_\mu\varphi_A^i
=(\mathcal D_\mu\varphi_A^i)_{\mathrm{printed}}
+\frac{i-1}{2}(\mathord{\not{\mathcal D}}L_A^{ij})\psi_{\mu j}.
```

The subscript $`\mathrm{printed}`$ denotes only the old coefficient in the source, not an alternative calculation branch. The corrected derivative above is used in the composite vector and in $`\Box^cL_A^{ij}`$.

Lower SU(2) indices follow by the same epsilon operation:

```math
\mathcal D_\mu\varphi_{Ai}
=(\mathcal D_\mu\varphi_A^j)\epsilon_{ji},\qquad
\mathcal D_\mu L_{Aij}
=\epsilon_{ik}\epsilon_{j\ell}\mathcal D_\mu L_A^{k\ell}.
```

<a id="33-triplet-superconformal-dalembertian"></a>

### Triplet superconformal d'Alembertian

Source (3.15), retaining its printed symmetrizations:

```math
\boxed{
\begin{aligned}
\Box^cL_A^{ij}
={}&(\partial^a-4b^a+\omega_b{}^{ba})\mathcal D_aL_A^{ij}
+2V_a{}^{(i}{}_k\mathcal D^aL_A^{j)k}
+6f_a{}^aL_A^{ij}
-i\bar\psi^{a(i}\mathcal D_a\varphi_A^{j)}\\
&+4\bar\psi^{a(i}\gamma_a\chi^{k)}L_A{}^j{}_k
+4\bar\psi^{a(j}\gamma_a\chi^{k)}L_A{}^i{}_k
-6L_A^{ij}\bar\psi^a\gamma_a\chi\\
&-\bar\varphi_A^{(i}(\gamma\!\cdot\!T)\gamma^a\psi_a^{j)}
+\bar\varphi_A^{(i}\gamma^a\phi_a^{j)}.
\end{aligned}}
```

Here $`L_A{}^i{}_j=\epsilon^{ik}L_{Akj}`$ and

```math
\Box^cL_{Aij}=\epsilon_{ik}\epsilon_{j\ell}\Box^cL_A^{k\ell}.
```

Expanding the two positive $`\chi`$ terms without parentheses gives

```math
\begin{aligned}
&4\bar\psi^{a(i}\gamma_a\chi^{k)}L_A{}^j{}_k
+4\bar\psi^{a(j}\gamma_a\chi^{k)}L_A{}^i{}_k\\
&\quad=2(\bar\psi^{ai}\gamma_a\chi^k
+\bar\psi^{ak}\gamma_a\chi^i)L_A{}^j{}_k
+2(\bar\psi^{aj}\gamma_a\chi^k
+\bar\psi^{ak}\gamma_a\chi^j)L_A{}^i{}_k
\end{aligned}
```

which explains the source's respective symmetrizations $`(i,k)`$ and $`(j,k)`$. No additional $`(i,j)`$ symmetrization is assumed on each bilinear. The $`\mathcal D\varphi_A`$ dependence of this operator uses the corrected definition of Section 3.2.

<a id="4-weyl-multiplet-curvatures-and-dependent-connections"></a>

## Weyl-multiplet curvatures and dependent connections

<a id="41-widehat-rv-and-widehat-rq-a5"></a>

### $`\widehat R(V)`$ and $`\widehat R(Q)`$: (A.5)

```math
\boxed{
\begin{aligned}
\widehat R_{\mu\nu}{}^{ij}(V)
={}&2\partial_{[\mu}V_{\nu]}{}^{ij}
-2V_{[\mu}{}^{k(i}V_{\nu]k}{}^{j)}
-3i\bar\phi_{[\mu}^{(i}\psi_{\nu]}^{j)}\\
&-8\bar\psi_{[\mu}^{(i}\gamma_{\nu]}\chi^{j)}
-i\bar\psi_{[\mu}^{(i}(\gamma\!\cdot\!T)\psi_{\nu]}^{j)},\\
\widehat R_{\mu\nu}{}^i(Q)
={}&2\partial_{[\mu}\psi_{\nu]}^i
+\frac12\omega_{[\mu}{}^{ab}\gamma_{ab}\psi_{\nu]}^i
+b_{[\mu}\psi_{\nu]}^i
-2V_{[\mu}{}^{ij}\psi_{\nu]j}\\
&-2i\gamma_{[\mu}\phi_{\nu]}^i
+2i(\gamma\!\cdot\!T)\gamma_{[\mu}\psi_{\nu]}^i.
\end{aligned}}
```

Tangent components are obtained using $`\widehat R_{ab}=e_a{}^\mu e_b{}^\nu\widehat R_{\mu\nu}`$. Here $`\gamma_\mu=e_\mu{}^a\gamma_a`$.

<a id="42-spin-connection-and-s-connection-a6"></a>

### Spin connection and $`S`$ connection: (A.6)

The spin connection in the project's chosen index order:

```math
\begin{aligned}
\omega_\mu{}^{ab}
={}&2e^{\nu[a}\partial_{[\mu}e_{\nu]}{}^{b]}
-e^{\nu[a}e^{b]\rho}e_{\mu c}\partial_\nu e_\rho{}^c
+2e_\mu{}^{[a}b^{b]}\\
&+\frac12\bar\psi^{[a}\gamma^{b]}\psi_\mu
+\frac14\bar\psi^a\gamma_\mu\psi^b,\qquad
\psi^a=e^{a\mu}\psi_\mu,\quad b^a=e^{a\mu}b_\mu.
\end{aligned}
```

Equality with the source's last two terms is

```math
\begin{aligned}
-\frac12\bar\psi^{[b}\gamma^{a]}\psi_\mu
&=+\frac12\bar\psi^{[a}\gamma^{b]}\psi_\mu,\\
-\frac14\bar\psi^b\gamma_\mu\psi^a
&=+\frac14\bar\psi^a\gamma_\mu\psi^b
\end{aligned}
```

where the second line uses the NW–SE rank-one flip.

$`\widehat R'_{\mu\nu}{}^i(Q)`$ is defined by removing only the explicit $`-2i\gamma_{[\mu}\phi_{\nu]}^i`$ term from $`\widehat R(Q)`$:

```math
\begin{aligned}
\widehat R'_{\mu\nu}{}^i(Q)
={}&2\partial_{[\mu}\psi_{\nu]}^i
+\frac12\omega_{[\mu}{}^{ab}\gamma_{ab}\psi_{\nu]}^i
+b_{[\mu}\psi_{\nu]}^i
-2V_{[\mu}{}^{ij}\psi_{\nu]j}
+2i(\gamma\!\cdot\!T)\gamma_{[\mu}\psi_{\nu]}^i,\\
\phi_\mu^i
={}&\frac{i}{3}\gamma^a\widehat R'_{\mu a}{}^i(Q)
-\frac{i}{24}\gamma_\mu\gamma^{ab}\widehat R'_{ab}{}^i(Q).
\end{aligned}
```

<a id="43-the-k-connection-and-the-sources-primed-lorentz-curvature"></a>

### The $`K`$ connection and the source's primed Lorentz curvature

The source's $`M`$ curvature in (A.5), after removing $`i\bar\psi_{[\mu}\gamma^{ab}\psi_{\nu]}`$, which Section 6.2 shows to vanish identically:

```math
\begin{aligned}
\widehat R_{\mu\nu}{}^{ab}(M)
={}&2\partial_{[\mu}\omega_{\nu]}{}^{ab}
+2\omega_{[\mu}{}^{ac}\omega_{\nu]c}{}^b
+8f_{[\mu}{}^{[a}e_{\nu]}{}^{b]}\\
&+i\bar\psi_{[\mu}\gamma^{[a}(\gamma\!\cdot\!T)\gamma^{b]}\psi_{\nu]}
+\bar\psi_{[\mu}\gamma^{[a}\widehat R_{\nu]}{}^{b]}(Q)
+\frac12\bar\psi_{[\mu}\gamma_{\nu]}\widehat R^{ab}(Q)\\
&-8\bar\psi_{[\mu}e_{\nu]}{}^{[a}\gamma^{b]}\chi
+i\bar\phi_{[\mu}\gamma^{ab}\psi_{\nu]}.
\end{aligned}
```

The removed term is printed with two gravitini in the source. This simplifies an identically vanishing expression; no unknown $`\phi_\mu`$ contribution has been inserted in place of a possible misprint. No reconstruction of a different curvature intended by the source is claimed.

```math
\begin{aligned}
\widehat R'_{\mu\nu}{}^{ab}(M)
&\equiv\widehat R_{\mu\nu}{}^{ab}(M)
-8f_{[\mu}{}^{[a}e_{\nu]}{}^{b]},\\
\mathcal R_{\mu\nu}
&\equiv\widehat R'_{\mu\rho}{}^{ab}(M)e_b{}^\rho e_{\nu a},\qquad
\mathcal R\equiv g^{\mu\nu}\mathcal R_{\mu\nu},\qquad
\mathcal R_\mu{}^a\equiv e^{a\nu}\mathcal R_{\mu\nu},\\
f_\mu{}^a
&=-\frac16\mathcal R_\mu{}^a+\frac1{48}e_\mu{}^a\mathcal R,\\
f_a{}^a
&=\left(-\frac16+\frac5{48}\right)\mathcal R
=-\frac1{16}\mathcal R.
\end{aligned}
```

Here $`\mathcal R_{\mu\nu},\mathcal R`$ denotes only the source's primed superconformal Ricci contractions; it does not replace the project's ordinary $`R_{\mu\nu},R`$ symbols. In primed $`M`$, $`\phi`$ and the full $`\widehat R(Q)`$ are retained; only the explicit $`f`$ term is removed. Thus the definition order is

```math
\omega\ \longrightarrow\ \widehat R'(Q)\ \longrightarrow\ \phi
\ \longrightarrow\ \widehat R(Q)\ \longrightarrow\ \widehat R'(M)
\ \longrightarrow\ (\mathcal R_{\mu\nu},\mathcal R)
\ \longrightarrow\ f
```

These are the dependent-connection definitions in (A.6); no auxiliary field has been eliminated using dynamical field equations.

<a id="44-the-mathcal-d_btab-contribution-of-the-composite-linear-multiplet"></a>

### The $`\mathcal D_bT^{ab}`$ contribution of the composite linear multiplet

**Definition used:** The Lorentz-connection contribution in (A.4) is corrected by the tensor check below.

```math
\mathcal D_\mu T_{ab}
=\partial_\mu T_{ab}-b_\mu T_{ab}
+2\omega_\mu{}^c{}_{[a}T_{b]c}
-\frac{i}{2}\bar\psi_\mu\gamma_{ab}\chi
+\frac{3i}{32}\bar\psi_\mu\widehat R_{ab}(Q).
```

The lower-index vector derivative in source (3.7) is used to check the Lorentz indices:

```math
\begin{aligned}
(\mathcal D_\mu E_a)_\omega
&=\omega_{\mu ab}E^b
=-\omega_\mu{}^c{}_aE_c,\\
(\mathcal D_\mu T_{ab})_{\omega,\mathrm{tensor}}
&=-\omega_\mu{}^c{}_aT_{cb}
-\omega_\mu{}^c{}_bT_{ac}\\
&=\omega_\mu{}^c{}_aT_{bc}
-\omega_\mu{}^c{}_bT_{ac}
=+2\omega_\mu{}^c{}_{[a}T_{b]c},\\
(\mathcal D_\mu T_{ab})_{\omega,\mathrm{printed}}
&=-2\omega_\mu{}^c{}_{[a}T_{b]c}
=-(\mathcal D_\mu T_{ab})_{\omega,\mathrm{tensor}}.
\end{aligned}
```

The subscript $`\omega`$ here selects only the Lorentz-connection contribution; it is not a field or fermion truncation. Thus the correction required for consistency with the existing Lorentz convention, and applied here, is

```math
\boxed{
-2\omega_\mu{}^c{}_{[a}T_{b]c}
\ \longrightarrow\
+2\omega_\mu{}^c{}_{[a}T_{b]c}
=-2\omega_{\mu[a}{}^cT_{b]c}.}
```

The last equality uses $`\omega_\mu{}^c{}_a=-\omega_{\mu a}{}^c`$. The negative-sign term printed in the source is retained only in the comparison above. The $`\mathcal D T`$ contributions in composite $`E_1^a`$ and $`E_{1a}`$ use the positive-sign Lorentz connection at the start of this section.

The paper does not give a separate expanded component formula for general $`\mathcal D_c\widehat F_{Aab}`$; this object is assigned neither an ordinary derivative nor an unsupported extra completion here.

<a id="5-a_1a-ordinary-curl-and-the-bf-action"></a>

## $`A_{1a}`$, ordinary curl and the BF action

<a id="51-inverse-relation-of-39-for-the-composite-vector"></a>

### Inverse relation of (3.9) for the composite vector

```math
\begin{aligned}
A_{1a}&=e_a{}^\mu A_{1\mu},\qquad
F_{1\mu\nu}=2\partial_{[\mu}A_{1\nu]},\\
\widehat F_{1\mu\nu}
&=F_{1\mu\nu}
-\bar\psi_{[\mu}\gamma_{\nu]}\lambda_1
+\frac{i}{2}\rho_1\bar\psi_{[\mu}\psi_{\nu]},\\
F_{1\mu\nu}
&=\widehat F_{1\mu\nu}
+\bar\psi_{[\mu}\gamma_{\nu]}\lambda_1
-\frac{i}{2}\rho_1\bar\psi_{[\mu}\psi_{\nu]}.
\end{aligned}
```

Direct substitution check of the inverse relation:

```math
\begin{aligned}
&\left[\widehat F_{1\mu\nu}
+\bar\psi_{[\mu}\gamma_{\nu]}\lambda_1
-\frac{i}{2}\rho_1\bar\psi_{[\mu}\psi_{\nu]}\right]
-\bar\psi_{[\mu}\gamma_{\nu]}\lambda_1
+\frac{i}{2}\rho_1\bar\psi_{[\mu}\psi_{\nu]}\\
&\qquad=\widehat F_{1\mu\nu}.
\end{aligned}
```

Its tangent counterpart is

```math
F_{1ab}
=\widehat F_{1ab}
+\bar\psi_{[a}\gamma_{b]}\lambda_1
-\frac{i}{2}\rho_1\bar\psi_{[a}\psi_{b]},\qquad
F_{1ab}=e_a{}^\mu e_b{}^\nu2\partial_{[\mu}A_{1\nu]}
```

In a moving tangent basis, $`F_{1ab}`$ is not written as $`2\partial_{[a}A_{1b]}`$ without additional connection/anholonomy terms.

This relation determines the curl of $`A_{1\mu}`$. $`A_{1\mu}`$ and $`A_{1\mu}+\partial_\mu\alpha_1`$ have the same curl:

```math
2\partial_{[\mu}(A_{1\nu]}+\partial_{\nu]}\alpha_1)
=2\partial_{[\mu}A_{1\nu]}+2\partial_{[\mu}\partial_{\nu]}\alpha_1
=F_{1\mu\nu}.
```

The paper gives no separate explicit $`A_{1\mu}[L_A,\varphi_A,E_A,N_A,\ldots]`$ representative for the full-fermion two-linear-multiplet composite in (3.14). Equation (3.16) is only a bosonic rewriting of $`F`$; it does not replace the full potential. No potential gauge or global boundary condition has been chosen here.

<a id="52-the-p_1ae_1a-distinction-312-313"></a>

### The $`P_1^a`$–$`E_1^a`$ distinction: (3.12), (3.13)

The paper's $`P_1^a`$ symbol retains its source meaning in this section; no additional field mapping to the unidentified alternative frame in `CONVENTIONS.md` is made.

```math
\begin{aligned}
P_1^a
&=E_1^a+\frac{i}{2}\bar\psi_b^i\gamma^{ba}\varphi_{1i}
+\frac14\bar\psi_b^i\gamma^{abc}\psi_c^jL_{1ij},\\
P_1^a
&=-\frac1{12}e_\mu{}^a e^{-1}
\epsilon^{\mu\nu\rho\sigma\lambda}\partial_\nu E_{1\rho\sigma\lambda}.
\end{aligned}
```

The second line rewrites source (3.13) using the project's coordinate epsilon symbol. $`\varepsilon^{\mu\nu\rho\sigma\lambda}=e^{-1} \epsilon^{\mu\nu\rho\sigma\lambda}`$ is used. The determinant factor is not hidden in the epsilon symbol.

<a id="53-the-e_1ab-used-in-bf"></a>

### The $`E_1^{ab}`$ used in BF

`BFaction.md` retains its earlier form containing $`\widehat F_{1ab}E_1^{ab}`$. Here $`E_1^{ab}`$ is the project-normalized dual of the composite linear multiplet's three-form potential:

```math
\begin{aligned}
E_1^{ab}&=-\frac1{12}\varepsilon^{abcde}E_{1cde},\qquad
E_{1abc}=\varepsilon_{abcde}E_1^{de},\\
E_1^{\mu\nu}&=e_a{}^\mu e_b{}^\nu E_1^{ab},\qquad
P_1^\mu=e^{-1}\partial_\nu(eE_1^{\mu\nu}).
\end{aligned}
```

The explicit expression for this potential in terms of the input vector multiplets, including Chern–Simons and gravitino contributions, is derived in the `$E_1^{ab}$ potansiyeli` section of [composite_linear_multiplet.md](../../r2/action/details/component_maps/gR2/composite_linear_multiplet.md). The $`\mathcal D_b[\cdots]`$ bracket in the $`E_1^a`$ formula alone is not $`E_1^{ab}`$. Using source relations (3.6) and (3.12),

```math
\begin{aligned}
E_1^a
&=e_\mu{}^a e^{-1}\partial_\nu(eE_1^{\mu\nu})
-\frac i2\bar\psi_b^i\gamma^{ba}\varphi_{1i}
-\frac14\bar\psi_b^i\gamma^{abc}\psi_c^jL_{1ij}.
\end{aligned}
```

Using Section 5.1 and $`E_1^{ab}=-E_1^{ba}`$, the three potential terms in the BF file combine as

```math
\begin{aligned}
&\frac12\widehat F_{1ab}E_1^{ab}
+\frac12E_1^{ab}\bar\psi_a^i\gamma_b\lambda_{1i}
-\frac i4\rho_1E_1^{ab}\bar\psi_a^i\psi_{bi}\\
&\quad=\frac12E_1^{ab}\left(
\widehat F_{1ab}+\bar\psi_{[a}^i\gamma_{b]}\lambda_{1i}
-\frac i2\rho_1\bar\psi_{[a}^i\psi_{b]i}\right)
=\frac12F_{1ab}E_1^{ab}
\end{aligned}
```

No integration by parts or representation change through $`A_1^aE_{1a}`$ has been applied to the BF density.

<a id="6-source-check-result-and-usage-boundary"></a>

## Source-check result and usage boundary

<a id="61-missing-i-in-38"></a>

### Missing $`i`$ in (3.8)

Source (3.8) prints $`-\tfrac12(\mathord{\not{\mathcal D}}\rho_A)\epsilon^i`$ in $`\delta_Q\lambda_A^i`$. Equation (3.10), however, contains $`+\tfrac{i}{2}(\mathord{\not{\mathcal D}}\rho_A)\psi_\mu^i`$ in $`\mathcal D_\mu\lambda_A^i`$. Temporarily denoting the first coefficient by $`-c`$,

```math
\begin{aligned}
\delta_Q\lambda_A^i
&\supset-c(\mathord{\not{\mathcal D}}\rho_A)\epsilon^i,\qquad
\delta_Q\psi_\mu^i\supset\partial_\mu\epsilon^i,\\
\left.\delta_Q(\mathcal D_\mu\lambda_A^i)\right|_{
(\mathord{\not{\mathcal D}}\rho_A)\partial_\mu\epsilon^i}
&=-c+\frac{i}{2},\\
c_{\mathrm{printed}}=\frac12
&\quad\Longrightarrow\quad\frac{i-1}{2}\neq0,\\
-c+\frac{i}{2}=0
&\quad\Longrightarrow\quad c=\frac{i}{2}.
\end{aligned}
```

The source correction preserving (3.10), applied in this record, is

```math
-\frac12(\mathord{\not{\mathcal D}}\rho_A)\epsilon^i
\ \longrightarrow\
-\frac{i}{2}(\mathord{\not{\mathcal D}}\rho_A)\epsilon^i
```

The defining-vector derivative terms in (A.9) and (A.10) of the same paper also contain the pair $`-i/2,+i/2`$. This corrected $`\delta\lambda`$ is used in checking composite coefficients; the relevant transformations are written explicitly in Section 6.4.

<a id="62-the-two-gravitino-term-in-a5"></a>

### The two-gravitino term in (A.5)

The printed term is $`i\bar\psi_{[\mu}\gamma^{ab}\psi_{\nu]}`$. Using the project's contracted rank-two flip,

```math
\begin{aligned}
\bar\psi_\mu\gamma^{ab}\psi_\nu
&=-t_2\bar\psi_\nu\gamma^{ab}\psi_\mu
=\bar\psi_\nu\gamma^{ab}\psi_\mu,\\
\bar\psi_{[\mu}\gamma^{ab}\psi_{\nu]}
&=\frac12\left(
\bar\psi_\mu\gamma^{ab}\psi_\nu
-\bar\psi_\nu\gamma^{ab}\psi_\mu\right)=0.
\end{aligned}
```

Moreover, this monomial alone has world Weyl weight $`-1`$, while the other $`\widehat R_{\mu\nu}{}^{ab}(M)`$ terms have weight $`0`$. Since it vanishes in the local conventions, the printed contribution was removed from the working expression in Section 4.3. The weight check does not determine which nonzero term was intended instead. In particular, replacing $`\psi_\nu`$ by $`\phi_\nu`$ without justification is not a valid source conversion.

<a id="63-weight-and-index-checks"></a>

### Weight and index checks

```math
\begin{gathered}
w(\rho_A)=1,\quad w(\lambda_A^i)=\frac32,\quad
w(L_A^{ij})=3,\quad w(\varphi_A^i)=\frac72,\quad
w(E_{Aa})=w(N_A)=4,\\
w(\psi_a)=\frac12,\quad w(\phi_a)=\frac32,\quad
w(f_a{}^a)=2,\quad w(\mathcal D_aX)=w(X)+1.
\end{gathered}
```

For example, the six terms in $`\Box^c\rho_A`$ have weights

```math
1+2=\frac12+\frac52
=1+\frac12+\frac32
=\frac12+1+\frac32
=\frac32+\frac32
=2+1=3
```

In $`\Box^cL_A^{ij}`$, the respective weights are

```math
1+4=1+4=2+3=\frac12+\frac92
=\frac12+\frac32+3
=3+\frac12+\frac32
=\frac72+1+\frac12
=\frac72+\frac32=5
```

The two positive $`\chi`$ terms have the same weight. Thus $`-2b^a`$ in the first operator and $`-4b^a`$ in the second are consistent with the weights. The explicit epsilon operations in Sections 2.2 and 3.2 must be used between upper- and lower-SU(2)-index equations.

<a id="64-sign-and-phase-corrections-of-the-composite-linear-multiplet"></a>

### Sign and phase corrections of the composite linear multiplet

This section resolves the discrepancy among source (3.1), (3.8) and (3.20). The choice preserves $`\mathcal D\lambda`$ in Section 2.2, $`\mathcal D L`$ in Section 3.1 and the composite-fermion coefficient $`+\frac i2(\rho_1\mathord{\not{\mathcal D}}\lambda_{2i} +\rho_2\mathord{\not{\mathcal D}}\lambda_{1i})`$. The incompatible source $`\delta Y`$ coefficients and the missing $`i`$ in the composite $`(\mathord{\not{\mathcal D}}\rho)\lambda`$ term are corrected.

<a id="641-inputs-and-majorana-conjugate"></a>

#### Inputs and Majorana conjugate

From source (3.1) and (3.8), corrected by Section 6.1, only the $`Q+S`$ transformations:

```math
\begin{aligned}
\delta_{Q+S}L_{1ij}&=i\bar\epsilon_{(i}\varphi_{1j)},\qquad
\delta_S L_{1ij}=0,\\
\delta_Q\rho_A&=\frac i2\bar\epsilon^i\lambda_{Ai},\qquad
\delta_S\rho_A=0,\\
\delta_{Q+S}\lambda_{Ai}
&=-\frac14(\gamma\!\cdot\!\widehat F_A)\epsilon_i
-\frac i2(\mathord{\not{\mathcal D}}\rho_A)\epsilon_i
+Y_{Aij}\epsilon^j
+\rho_A(\gamma\!\cdot\!T)\epsilon_i+\rho_A\eta_i.
\end{aligned}
```

The lower-index positive sign of the $`Y`$ term uses the same epsilon operation as Section 2.2. Temporarily denote the three coefficients in the source's $`\delta Y_{Aij}`$ by $`a,b,d`$:

```math
\begin{aligned}
\delta_{Q+S}Y_{Aij}
={}&a\bar\epsilon_{(i}\mathord{\not{\mathcal D}}\lambda_{Aj)}
+b\bar\epsilon_{(i}(\gamma\!\cdot\!T)\lambda_{Aj)}
-4i\rho_A\bar\epsilon_{(i}\chi_{j)}
+d\bar\eta_{(i}\lambda_{Aj)},\\
a_{\mathrm{printed}}&=\frac12,\qquad
b_{\mathrm{printed}}=\frac12,\qquad
d_{\mathrm{printed}}=\frac12.
\end{aligned}
```

For anticommuting spinors, with $`\gamma_{(n)}`$ denoting a rank-$`n`$ Clifford element, the flip rule gives

```math
\begin{aligned}
\bar\xi\gamma_{(n)}\zeta
&=-\zeta^T(C\gamma_{(n)})^T\xi
=t_n\zeta^TC\gamma_{(n)}\xi,\\
(C\gamma_{(n)})^T&=-t_nC\gamma_{(n)},\qquad
C^T=-C\quad(n=0),\\
(\gamma_{(n)})^TC&=t_nC\gamma_{(n)}
\end{aligned}
```

The spinors in this line are open SU(2) components; the additional minus sign of the NW–SE-contracted flip is not used here. Using $`t_1=+1`$, $`t_2=-1`$ and $`\bar\xi=\xi^TC`$,

```math
\begin{aligned}
C^T&=-C,\qquad
(\gamma^a)^TC=C\gamma^a,\qquad
(\gamma^{ab})^TC=-C\gamma^{ab},\\
\overline{\gamma^a\xi}&=\bar\xi\gamma^a,\qquad
\overline{\gamma^{ab}\xi}=-\bar\xi\gamma^{ab},\qquad
\overline{i\xi}=i\bar\xi.
\end{aligned}
```

The last equality denotes Majorana transposition; no Dirac adjoint or complex conjugation has been introduced.

<a id="642-independent-terms-of-composite-l_1ij"></a>

#### Independent terms of composite $`L_{1ij}`$

The initial expression and Leibniz expansion are

```math
\begin{aligned}
L_{1ij}&=\rho_1Y_{2ij}+\rho_2Y_{1ij}
-\frac i2\bar\lambda_{1(i}\lambda_{2j)},\\
\delta L_{1ij}
&=(\delta\rho_1)Y_{2ij}+\rho_1\delta Y_{2ij}
+(\delta\rho_2)Y_{1ij}+\rho_2\delta Y_{1ij}\\
&\quad-\frac i2\left[
(\delta\bar\lambda_{1(i})\lambda_{2j)}
+\bar\lambda_{1(i}\delta\lambda_{2j)}\right]
\end{aligned}
```

The subscripts below select only independent monomial coefficients; no field or fermion truncation is performed.

In the $`\rho\mathcal D\lambda`$ structure, since $`\delta\lambda`$ does not contain this derivative,

```math
\begin{aligned}
\left.\delta L_{1ij}\right|_{\rho\mathcal D\lambda}
&=a\bar\epsilon_{(i}
\left(\rho_1\mathord{\not{\mathcal D}}\lambda_{2j)}
+\rho_2\mathord{\not{\mathcal D}}\lambda_{1j)}\right),\\
\left.i\bar\epsilon_{(i}\varphi_{1j)}\right|_{\rho\mathcal D\lambda}
&=i\frac i2\bar\epsilon_{(i}
\left(\rho_1\mathord{\not{\mathcal D}}\lambda_{2j)}
+\rho_2\mathord{\not{\mathcal D}}\lambda_{1j)}\right),\\
a&=i\frac i2=-\frac12.
\end{aligned}
```

In the $`\mathcal D\rho`$ structure, using the $`t_1=+1`$ flip,

```math
\begin{aligned}
\left.\delta\bar\lambda_{1i}\right|_{\mathcal D\rho}
&=-\frac i2\bar\epsilon_i\mathord{\not{\mathcal D}}\rho_1,\\
\left.\delta L_{1ij}\right|_{\mathcal D\rho}
&=-\frac i2\left(-\frac i2\right)
\left[
\bar\epsilon_{(i}(\mathord{\not{\mathcal D}}\rho_1)\lambda_{2j)}
+\bar\lambda_{1(i}(\mathord{\not{\mathcal D}}\rho_2)\epsilon_{j)}
\right]\\
&=-\frac14\bar\epsilon_{(i}
\left[(\mathord{\not{\mathcal D}}\rho_1)\lambda_{2j)}
+(\mathord{\not{\mathcal D}}\rho_2)\lambda_{1j)}\right].
\end{aligned}
```

Temporarily denoting the coefficient of this symmetric sum in composite $`\varphi_{1i}`$ by $`c`$,

```math
ic=-\frac14\quad\Longrightarrow\quad c=\frac i4,
\qquad
c_{\mathrm{printed}}=\frac14.
```

In the $`T`$ structure, since $`\delta\bar\lambda_{1i}=-\rho_1\bar\epsilon_i(\gamma\!\cdot\!T)`$ and $`t_2=-1`$,

```math
\begin{aligned}
\left.\delta L_{1ij}\right|_T
&=b\bar\epsilon_{(i}(\gamma\!\cdot\!T)
\left(\rho_1\lambda_{2j)}+\rho_2\lambda_{1j)}\right)\\
&\quad-\frac i2\left[
-\rho_1\bar\epsilon_{(i}(\gamma\!\cdot\!T)\lambda_{2j)}
+\rho_2\bar\lambda_{1(i}(\gamma\!\cdot\!T)\epsilon_{j)}
\right]\\
&=\left(b+\frac i2\right)
\bar\epsilon_{(i}(\gamma\!\cdot\!T)
\left(\rho_1\lambda_{2j)}+\rho_2\lambda_{1j)}\right),\\
b+\frac i2&=i\quad\Longrightarrow\quad b=\frac i2.
\end{aligned}
```

In the $`S`$ transformation, using $`t_0=+1`$, $`\delta_S\lambda_{Ai}=\rho_A\eta_i`$ and $`\delta_S\rho_A=0`$,

```math
\begin{aligned}
\delta_S L_{1ij}
&=d\bar\eta_{(i}
\left(\rho_1\lambda_{2j)}+\rho_2\lambda_{1j)}\right)\\
&\quad-\frac i2\left[
\rho_1\bar\eta_{(i}\lambda_{2j)}
+\rho_2\bar\lambda_{1(i}\eta_{j)}\right]\\
&=\left(d-\frac i2\right)\bar\eta_{(i}
\left(\rho_1\lambda_{2j)}+\rho_2\lambda_{1j)}\right)=0,\\
d&=\frac i2.
\end{aligned}
```

<a id="643-coefficients-used"></a>

#### Coefficients used

Substituting the temporary coefficients, the working $`Q+S`$ transformation is

```math
\boxed{
\begin{aligned}
\delta_{Q+S}Y_{Aij}
={}&-\frac12\bar\epsilon_{(i}\mathord{\not{\mathcal D}}\lambda_{Aj)}
+\frac i2\bar\epsilon_{(i}(\gamma\!\cdot\!T)\lambda_{Aj)}
-4i\rho_A\bar\epsilon_{(i}\chi_{j)}
+\frac i2\bar\eta_{(i}\lambda_{Aj)}
\end{aligned}}
```

The upper-index equality follows by raising with two epsilons; these four coefficients are unchanged. The change applied to the composite fermion is

```math
\boxed{
\begin{aligned}
\left.\varphi_{1i}\right|_{\mathcal D\rho}
&=\frac i4\left[
(\mathord{\not{\mathcal D}}\rho_1)\lambda_{2i}
+(\mathord{\not{\mathcal D}}\rho_2)\lambda_{1i}
\right].
\end{aligned}}
```

The complete composite expression in [composite_linear_multiplet.md](../../r2/action/details/component_maps/gR2/composite_linear_multiplet.md) uses this coefficient. Thus the same choice satisfies $`\delta L_{1ij}=i\bar\epsilon_{(i}\varphi_{1j)}`$ and $`\delta_S L_{1ij}=0`$ for the four independent structures checked. This coefficient check is not a full multiplet-closure or action-invariance calculation.

**Component definitions:** The versions used for $`\mathcal D\varphi`$, $`\mathcal D T`$, $`\delta\lambda`$, $`\delta Y`$ and composite $`\varphi_{1i}`$ are now explicitly fixed above. The BF density retains its earlier $`\widehat F_{1ab}E_1^{ab}`$ form. The explicit calculation of the $`E_1^{ab}`$ potential is in [the mixed linear-multiplet derivation](../../r2/action/details/component_maps/gR2/composite_linear_multiplet.md), and its defining relation is in Section 5.3 above. The cited source does not supply the source's general $`\mathcal D\widehat F`$ completion or a separately expanded representative of the full composite $`A_{1\mu}`$ potential. This record does not rederive missing gauged target-gauge transformations or the intended replacement of a possible source misprint in $`\widehat R(M)`$.
