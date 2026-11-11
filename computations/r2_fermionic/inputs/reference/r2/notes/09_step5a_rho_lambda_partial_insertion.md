# Intermediate Step 5a: scalar and gaugino insertion with the triplet and strength retained

## 1. Problem and Target

Insert only $`\rho'`$ and $`\lambda'_i`$ into the accepted Step 4 density. Retain $`Y'_{ij}`$, $`\widehat F'_{ab}`$ and $`A'_a`$ as primed quantities. Distribute every multiplicative product through explicit fermion degree four. This intermediate representation precedes Step 6 and is distinct from the full Step 5 insertion.

**Starting point:** [Step 4, Eq. (47)](06_step4_Gold_unprimed_vector_and_gauge.md), lock `R2-GOLD4-UNPRIMED-SUBSTITUTION-v2`. **Substitutions:** [Step 5, Eqs. (3), (4), (8)](08_step5_primed_composite_vector_insertion.md), from the [locked earlier map](../../../../../two_derivative_fermionic/inputs/reference/results/gauged_two_derivative_fermionic_action/02_single_linear_multiplet_mapping_construction.md), Sections 7.9 and 8.7/8.11. The scalar and gaugino source is Özkan (3.14); the mixed-map parent is (3.20). Coomans (2.16) fixes the operational derivatives.

**A1.** Work off shell, with the inherited Gold (7) restriction $`\sigma=1,b_\mu=0,\psi^i=0`$. The gravitino $`\psi_\mu^i`$ survives. No additional alignment is necessary here because $`A'`$ is retained.

**A2.** The original $`L_{ij},\varphi_i,E_a,N`$ are the same input in both maps. Neither $`Y'`$ nor $`\widehat F'`$ nor $`A'`$ is substituted. The shared $`T,\chi,D,\phi_\mu,f_\mu{}^a`$ remain bound to the gauged Coomans background, with the existing source-order qualifications.

**A3. Explicit-degree convention.** An unexpanded even component or covariant derivative of one is assigned explicit degree zero. Each displayed $`\varphi,\bar\varphi,\psi_\mu,\bar\psi_\mu,\chi,\bar\chi,\phi_\mu`$ has degree one. Covariant differential operators preserve this *formal displayed degree*. The labels 0, 2 and 4 below therefore count explicit fermions; they are not the fully expanded physical Grassmann coefficients. In particular, hidden fermions in $`\widehat F',Y',A',\widehat G,T,D`$ and connections remain. The actual zero-fermion restriction is given separately in Section 6.4.

**A4.** Omit formal explicit degree six only in this intermediate display. The full untruncated Step 5 parent remains available. This is a polynomial projection, with no numerical smallness or error percentage asserted for Grassmann variables. No ordinary-field equation, Fierz rearrangement, integration by parts or boundary-term removal is used.

**A5.** Retain covariant differential operators. Expand first-derivative Leibniz products, but keep $`\Box_c`$ on its explicit scalar arguments. Its source definition is displayed below. It cannot be replaced by an ordinary Laplacian in the fermionic sectors.

## 2. Convention Ledger

<!-- ASSERT_CONVENTION: natural_units=hbar=c=1; metric_signature=mostly_plus (-++++); spinor_bar=NW-SE-transpose; gauge_slice=R2-GOLD7-GAUGE-v1; fermion_order=formal_explicit_degree_le_4 -->

| Item | Convention |
|---|---|
| Dimension; indices | Five; $`a,b,\mu,\nu=0,\ldots,4`$; $`i,j=1,2`$ |
| Metric and orientation | $`\eta=(-++++)`$; $`\varepsilon^{01234}=+1`$, lower $`\varepsilon_{01234}=-1`$ |
| Gamma algebra | $`\{\gamma_a,\gamma_b\}=2\eta_{ab}`$; $`\gamma^{abcde}=i\varepsilon^{abcde}`$; dot contractions have no factorial |
| Symmetrization | Unit weight |
| Spinors | Odd symplectic Majorana; operational transpose bar, no conjugation of scalar $`i`$ |
| Raising/lowering | $`X^i=\varepsilon^{ij}X_j`$, $`X_i=X^j\varepsilon_{ji}`$; $`\varepsilon^{12}=\varepsilon_{12}=1`$ |
| Curvature | $`R^\rho{}_{\sigma\mu\nu}=2\partial_{[\mu}\Gamma^\rho_{\nu]\sigma}+2\Gamma^\rho_{[\mu\vert\lambda\vert}\Gamma^\lambda_{\nu]\sigma}`$; inherited sign unchanged |
| Derivatives | Even covariant operators; full spin and conformal connections retained |
| Coupling | Existing $`g`$ and source BF normalization; no fit to Gold's $`R^2`$ normalization |
| Unused conventions | Fourier transforms, state normalization and renormalization are not involved |

Numerical subscripts such as $`j_{12}`$ are fresh dummy-index names, not multiplet labels or new physical fields. The labels attached to equation rows identify their parent group only.

## 3. Definitions and Required Identities

```math
L^2=L_{ij}L^{ij},\quad L>0,\qquad \mathcal D_aL^{-p}=-pL^{-p-1}\mathcal D_aL.
\tag{1}
```

```math
\rho'=\left[\begin{aligned}
&2L^{-1}N\\
&+iL^{-3}L_{ij}\bar\varphi^i\varphi^j
\end{aligned}\right]
\tag{2}
```

```math
\lambda'_i=\left[\begin{aligned}
&-2iL^{-1}\not{\mathcal D}\varphi_i\\
&+16L^{-1}L_{ij}\chi^j\\
&+4L^{-1}\gamma\!\cdot\!T\varphi_i\\
&-2NL^{-3}L_{ij}\varphi^j\\
&+2iL^{-3}(\not{\mathcal D}L_{ij})L^{jk}\varphi_k\\
&-2iL^{-3}\not E L_{ij}\varphi^j\\
&+2iL^{-3}\varphi^j\bar\varphi_i\varphi_j\\
&-6iL^{-5}\varphi^j\bar\varphi_k\varphi_lL^{kl}L_{ij}
\end{aligned}\right]
\tag{3}
```

```math
\bar\lambda'_i=\left[\begin{aligned}
&-2iL^{-1}(\mathcal D_a\bar\varphi_i)\gamma^a\\
&+16L^{-1}L_{ij}\bar\chi^j\\
&-4L^{-1}\bar\varphi_i\gamma\!\cdot\!T\\
&-2NL^{-3}L_{ij}\bar\varphi^j\\
&+2iL^{-3}L^{jk}\bar\varphi_k(\not{\mathcal D}L_{ij})\\
&-2iL^{-3}L_{ij}\bar\varphi^j\not E\\
&+2iL^{-3}\bar\varphi^j(\bar\varphi_i\varphi_j)\\
&-6iL^{-5}\bar\varphi^j(\bar\varphi_k\varphi_l)L^{kl}L_{ij}
\end{aligned}\right]
\tag{4}
```

The rank-two gamma matrix changes sign under the operational transpose. An even bilinear crosses an odd spinor with sign $`(-1)^{2\cdot1}=+1`$. These two operations give the bar map above; the scalar $`i`$ retains its sign. Upper gaugino indices are raised before insertion:

```math
\bar\lambda'{}^i=\varepsilon^{ir}\bar\lambda'_r,\qquad \lambda'{}^j=\varepsilon^{js}\lambda'_s,\qquad \bar\chi\lambda'=\bar\chi^i\lambda'_i.
\tag{5}
```

The even Leibniz rule, with factors in their displayed order, is

```math
\mathcal D_a(X_1\cdots X_n)=\sum_{r=1}^{n}X_1\cdots(\mathcal D_aX_r)\cdots X_n,\qquad \mathcal D_a\gamma^b=0.
\tag{6}
```

The summation labels in this identity are abstract factor positions, not fields. In particular,

```math
\begin{aligned}
&\mathcal D_a(\gamma^{bc}T_{bc}\varphi_i)=\gamma^{bc}(\mathcal D_aT_{bc})\varphi_i+\gamma^{bc}T_{bc}\mathcal D_a\varphi_i,\\
&\mathcal D_a(\not E)=\gamma^b\mathcal D_a E_b,\qquad \mathcal D_a(\not{\mathcal D}\varphi_i)=\gamma^b\mathcal D_a\mathcal D_b\varphi_i.
\end{aligned}
\tag{7}
```

The inherited operational scalar and gaugino derivatives on Gold (7) are Coomans (2.16), with vector indices lowered by epsilon. These definitions specify what remains inside the displayed derivative operators:

```math
\begin{aligned}
&\mathcal D_a\rho'=\partial_a\rho'-\frac i2\bar\psi_a^i\lambda'_i,\\
&\mathcal D_a\lambda'_i=(\partial_a+\tfrac14\omega_a{}^{bc}\gamma_{bc})\lambda'_i-V_a{}^{jk}\lambda'_k\varepsilon_{ji}\\
&\quad+\frac14\gamma\!\cdot\!\widehat F'\psi_{ai}+\frac i2\not{\mathcal D}\rho'\psi_{ai}-Y'_{ij}\psi_a{}^j-\rho'\gamma\!\cdot\!T\psi_{ai}-\rho'\phi_{ai}. 
\end{aligned}
\tag{8}
```

```math
\begin{aligned}
&\Box_c\rho'=(\partial^a+\omega_b{}^{ba})\mathcal D_a\rho'-\frac i2\bar\psi_a\mathcal D^a\lambda'\\
&\quad-2\rho'\bar\psi_a\gamma^a\chi+\frac12\bar\psi_a\gamma^a\gamma\!\cdot\!T\lambda'+\frac12\bar\phi_a\gamma^a\lambda'+2f_a{}^a\rho'.
\end{aligned}
\tag{9}
```

These are operator definitions, not further substitutions of $`Y'`$ or $`\widehat F'`$. Expanding their hidden fermion content and all gauged background slots is not part of the formal grouping below. In the scalar-box rows, linearity is applied to the two explicit scalar arguments; the source operator is retained rather than assuming a scalar-product rule for independently unspecified conformal multiplets.

## 4. Detailed Derivation

### 4.1 Scalar powers and degree projection

```math
\begin{aligned}
&\rho'=2NL^{-1}+iL^{-3}L_{ij}\bar\varphi^i\varphi^j,\\
&(\rho')^2=4N^2L^{-2}+4iNL^{-4}L_{ij}\bar\varphi^i\varphi^j\\
&\qquad-L^{-6}L_{ij}L_{kl}(\bar\varphi^i\varphi^j)(\bar\varphi^k\varphi^l). 
\end{aligned}
\tag{10}
```

The cross coefficient is $`2(2N/L)(i/L^3)=4iN/L^4`$; the quartic coefficient is $`i^2/L^6=-L^{-6}`$. The scalar bilinear is even, so the two cross products agree without a minus sign.

```math
\begin{aligned}
&\frac12\rho'\Box_c\rho'=\frac{2N}{L}\Box_c(L^{-1}N)\\
&\quad+\frac{iN}{L}\Box_c(L^{-3}L_{ij}\bar\varphi^i\varphi^j)\\
&\quad+iL^{-3}L_{ij}\bar\varphi^i\varphi^j\Box_c(L^{-1}N)\\
&\quad-\frac12 L^{-3}L_{ij}\bar\varphi^i\varphi^j\Box_c(L^{-3}L_{kl}\bar\varphi^k\varphi^l). 
\end{aligned}
\tag{11}
```

The four scalar-box contributions have explicit degrees $`0,2,2,4`$. No scalar argument remains primed.

### 4.2 Differentiate the scalar and each gaugino monomial

The six scalar derivative contributions follow from the coefficient and each of the three bilinear factors:

```math
\begin{aligned}
&- \frac{2 N}{L^{2}} (\mathcal D_{a}L)\\
&\frac{2}{L} (\mathcal D_{a}N)\\
&- \frac{3 i}{L^{4}} (\mathcal D_{a}L) L_{r_1s_1} \bar\varphi^{r_1} \varphi^{s_1}\\
&\frac{i}{L^{3}} \mathcal D_{a}\!\left(L_{r_1s_1}\right) \bar\varphi^{r_1} \varphi^{s_1}\\
&\frac{i}{L^{3}} L_{r_1s_1} \mathcal D_{a}\!\left(\bar\varphi^{r_1}\right) \varphi^{s_1}\\
&\frac{i}{L^{3}} L_{r_1s_1} \bar\varphi^{r_1} \mathcal D_{a}\!\left(\varphi^{s_1}\right)
\end{aligned}
\tag{12}
```

For the gaugino, the following eight displays are the derivatives of the eight source monomials, in source order. Their sum is $`\mathcal D_a\lambda'_i`$. Each coefficient derivative and each field-factor derivative is present; no odd factors are interchanged.

**Gaugino monomial 1.**

```math
\mathcal D_a\!\left(- \frac{2 i}{L} \not{\mathcal D}\varphi_{i}\right)=\begin{aligned}
&+\frac{2 i}{L^{2}} (\mathcal D_{a}L) \not{\mathcal D}\varphi_{i}\\
&- \frac{2 i}{L} \mathcal D_{a}\!\left(\not{\mathcal D}\varphi_{i}\right)
\end{aligned}
\tag{13}
```

**Gaugino monomial 2.**

```math
\mathcal D_a\!\left(\frac{16}{L} L_{ij_{2}} \chi^{j_{2}}\right)=\begin{aligned}
&- \frac{16}{L^{2}} (\mathcal D_{a}L) L_{ij_{2}} \chi^{j_{2}}\\
&+\frac{16}{L} \mathcal D_{a}\!\left(L_{ij_{2}}\right) \chi^{j_{2}}\\
&+\frac{16}{L} L_{ij_{2}} \mathcal D_{a}\!\left(\chi^{j_{2}}\right)
\end{aligned}
\tag{14}
```

**Gaugino monomial 3.**

```math
\mathcal D_a\!\left(\frac{4}{L} \gamma\!\cdot\!T \varphi_{i}\right)=\begin{aligned}
&- \frac{4}{L^{2}} (\mathcal D_{a}L) \gamma\!\cdot\!T \varphi_{i}\\
&+\frac{4}{L} \gamma\!\cdot\!T \mathcal D_{a}\!\left(\varphi_{i}\right)\\
&+\frac{4}{L} \gamma^{mn}(\mathcal D_{a}T_{mn}) \varphi_{i}
\end{aligned}
\tag{15}
```

**Gaugino monomial 4.**

```math
\mathcal D_a\!\left(- \frac{2 N}{L^{3}} L_{ij_{2}} \varphi^{j_{2}}\right)=\begin{aligned}
&+\frac{6 N}{L^{4}} (\mathcal D_{a}L) L_{ij_{2}} \varphi^{j_{2}}\\
&- \frac{2}{L^{3}} (\mathcal D_{a}N) L_{ij_{2}} \varphi^{j_{2}}\\
&- \frac{2 N}{L^{3}} \mathcal D_{a}\!\left(L_{ij_{2}}\right) \varphi^{j_{2}}\\
&- \frac{2 N}{L^{3}} L_{ij_{2}} \mathcal D_{a}\!\left(\varphi^{j_{2}}\right)
\end{aligned}
\tag{16}
```

**Gaugino monomial 5.**

```math
\mathcal D_a\!\left(\frac{2 i}{L^{3}} (\not{\mathcal D}L_{ij_{2}}) L^{j_{2}k_{2}} \varphi_{k_{2}}\right)=\begin{aligned}
&- \frac{6 i}{L^{4}} (\mathcal D_{a}L) (\not{\mathcal D}L_{ij_{2}}) L^{j_{2}k_{2}} \varphi_{k_{2}}\\
&+\frac{2 i}{L^{3}} \mathcal D_{a}\!\left((\not{\mathcal D}L_{ij_{2}})\right) L^{j_{2}k_{2}} \varphi_{k_{2}}\\
&+\frac{2 i}{L^{3}} (\not{\mathcal D}L_{ij_{2}}) \mathcal D_{a}\!\left(L^{j_{2}k_{2}}\right) \varphi_{k_{2}}\\
&+\frac{2 i}{L^{3}} (\not{\mathcal D}L_{ij_{2}}) L^{j_{2}k_{2}} \mathcal D_{a}\!\left(\varphi_{k_{2}}\right)
\end{aligned}
\tag{17}
```

**Gaugino monomial 6.**

```math
\mathcal D_a\!\left(- \frac{2 i}{L^{3}} \not E L_{ij_{2}} \varphi^{j_{2}}\right)=\begin{aligned}
&+\frac{6 i}{L^{4}} (\mathcal D_{a}L) \not E L_{ij_{2}} \varphi^{j_{2}}\\
&- \frac{2 i}{L^{3}} \mathcal D_{a}\!\left(\not E\right) L_{ij_{2}} \varphi^{j_{2}}\\
&- \frac{2 i}{L^{3}} \not E \mathcal D_{a}\!\left(L_{ij_{2}}\right) \varphi^{j_{2}}\\
&- \frac{2 i}{L^{3}} \not E L_{ij_{2}} \mathcal D_{a}\!\left(\varphi^{j_{2}}\right)
\end{aligned}
\tag{18}
```

**Gaugino monomial 7.**

```math
\mathcal D_a\!\left(\frac{2 i}{L^{3}} \varphi^{j_{2}} \bar\varphi_{i} \varphi_{j_{2}}\right)=\begin{aligned}
&- \frac{6 i}{L^{4}} (\mathcal D_{a}L) \varphi^{j_{2}} \bar\varphi_{i} \varphi_{j_{2}}\\
&+\frac{2 i}{L^{3}} \mathcal D_{a}\!\left(\varphi^{j_{2}}\right) \bar\varphi_{i} \varphi_{j_{2}}\\
&+\frac{2 i}{L^{3}} \varphi^{j_{2}} \mathcal D_{a}\!\left(\bar\varphi_{i}\right) \varphi_{j_{2}}\\
&+\frac{2 i}{L^{3}} \varphi^{j_{2}} \bar\varphi_{i} \mathcal D_{a}\!\left(\varphi_{j_{2}}\right)
\end{aligned}
\tag{19}
```

**Gaugino monomial 8.**

```math
\mathcal D_a\!\left(- \frac{6 i}{L^{5}} \varphi^{j_{2}} \bar\varphi_{k_{2}} \varphi_{l_{2}} L^{k_{2}l_{2}} L_{ij_{2}}\right)=\begin{aligned}
&+\frac{30 i}{L^{6}} (\mathcal D_{a}L) \varphi^{j_{2}} \bar\varphi_{k_{2}} \varphi_{l_{2}} L^{k_{2}l_{2}} L_{ij_{2}}\\
&- \frac{6 i}{L^{5}} \mathcal D_{a}\!\left(\varphi^{j_{2}}\right) \bar\varphi_{k_{2}} \varphi_{l_{2}} L^{k_{2}l_{2}} L_{ij_{2}}\\
&- \frac{6 i}{L^{5}} \varphi^{j_{2}} \mathcal D_{a}\!\left(\bar\varphi_{k_{2}}\right) \varphi_{l_{2}} L^{k_{2}l_{2}} L_{ij_{2}}\\
&- \frac{6 i}{L^{5}} \varphi^{j_{2}} \bar\varphi_{k_{2}} \mathcal D_{a}\!\left(\varphi_{l_{2}}\right) L^{k_{2}l_{2}} L_{ij_{2}}\\
&- \frac{6 i}{L^{5}} \varphi^{j_{2}} \bar\varphi_{k_{2}} \varphi_{l_{2}} \mathcal D_{a}\!\left(L^{k_{2}l_{2}}\right) L_{ij_{2}}\\
&- \frac{6 i}{L^{5}} \varphi^{j_{2}} \bar\varphi_{k_{2}} \varphi_{l_{2}} L^{k_{2}l_{2}} \mathcal D_{a}\!\left(L_{ij_{2}}\right)
\end{aligned}
\tag{20}
```

For the bilinear kinetic term, these eight derivative expansions multiply each of the eight displayed bar-map monomials. The degree-two sector retains all 36 pairings of the six linear monomials on either side, before derivative distribution; degree four retains both linear-by-cubic orders; cubic-by-cubic terms have degree six and are discarded here. Their complete distributed rows appear below, so this rule does not stand in for an unevaluated product.

### 4.3 Parent-row ledger

The following 42 groups are transcribed from Step 4 Eq. (47). A four-term bracket is distributed before the component insertion. Group 33 resolves the suppressed contraction as $`\bar\chi^i\lambda'_i`$. Each result row in Section 6 retains its group number, allowing every contribution to be traced back to this ledger.

```math
\left.e^{-1}\mathcal L_{VL}\right|_{\text{parent group }1}=\begin{aligned}
&+Y'^{ij} Y'_{ij}
\end{aligned}
\tag{21}
```

```math
\left.e^{-1}\mathcal L_{VL}\right|_{\text{parent group }2}=\begin{aligned}
&- g \rho' Y'^{ij} L_{ij}
\end{aligned}
\tag{22}
```

```math
\left.e^{-1}\mathcal L_{VL}\right|_{\text{parent group }3}=\begin{aligned}
&- \frac{1}{2} \bar\lambda'^i \not{\mathcal D}\lambda'_i
\end{aligned}
\tag{23}
```

```math
\left.e^{-1}\mathcal L_{VL}\right|_{\text{parent group }4}=\begin{aligned}
&+i \bar\lambda'^i \gamma\cdot T \lambda'_i
\end{aligned}
\tag{24}
```

```math
\left.e^{-1}\mathcal L_{VL}\right|_{\text{parent group }5}=\begin{aligned}
&- 8 i \rho' \bar\lambda'^i \chi_i
\end{aligned}
\tag{25}
```

```math
\left.e^{-1}\mathcal L_{VL}\right|_{\text{parent group }6}=\begin{aligned}
&- \frac{i}{8} \bar\lambda'^i \gamma\cdot\widehat G \lambda'_i
\end{aligned}
\tag{26}
```

```math
\left.e^{-1}\mathcal L_{VL}\right|_{\text{parent group }7}=\begin{aligned}
&+\frac{i g}{4} \bar\lambda'^i L_{ij} \lambda'^j
\end{aligned}
\tag{27}
```

```math
\left.e^{-1}\mathcal L_{VL}\right|_{\text{parent group }8}=\begin{aligned}
&+\frac{g}{4} \rho' \bar\psi_a^i \gamma^a \lambda'^j L_{ij}
\end{aligned}
\tag{28}
```

```math
\left.e^{-1}\mathcal L_{VL}\right|_{\text{parent group }9}=\begin{aligned}
&- \frac{1}{2} \bar\psi_a^i \gamma^a \lambda'^j Y'_{ij}
\end{aligned}
\tag{29}
```

```math
\left.e^{-1}\mathcal L_{VL}\right|_{\text{parent group }10}=\begin{aligned}
&- \frac{3}{16} \rho' \bar\lambda'^i \gamma^a \gamma\cdot\widehat G \psi_{ai}\\
&+\frac{3}{4} \rho' \bar\lambda'^i \gamma^a \gamma\cdot T \psi_{ai}\\
&- \frac{3 g}{8} \rho' \bar\lambda'^i \gamma^a L_{ij} \psi_a^j\\
&+\frac{3}{4} \rho' \bar\lambda'^i \gamma^a \phi_{ai}
\end{aligned}
\tag{30}
```

```math
\left.e^{-1}\mathcal L_{VL}\right|_{\text{parent group }11}=\begin{aligned}
&- \frac{1}{2} A'_a (\mathcal D_b\rho') \widehat G^{ab}
\end{aligned}
\tag{31}
```

```math
\left.e^{-1}\mathcal L_{VL}\right|_{\text{parent group }12}=\begin{aligned}
&- \frac{1}{2} A'_a \rho' \mathcal D_b\widehat G^{ab}
\end{aligned}
\tag{32}
```

```math
\left.e^{-1}\mathcal L_{VL}\right|_{\text{parent group }13}=\begin{aligned}
&- \frac{1}{2} A'_a \mathcal D_b\widehat F'^{ab}
\end{aligned}
\tag{33}
```

```math
\left.e^{-1}\mathcal L_{VL}\right|_{\text{parent group }14}=\begin{aligned}
&+8 A'_a (\mathcal D_b\rho') T^{ab}
\end{aligned}
\tag{34}
```

```math
\left.e^{-1}\mathcal L_{VL}\right|_{\text{parent group }15}=\begin{aligned}
&+8 A'_a \rho' \mathcal D_bT^{ab}
\end{aligned}
\tag{35}
```

```math
\left.e^{-1}\mathcal L_{VL}\right|_{\text{parent group }16}=\begin{aligned}
&- \frac{1}{8} A'_a \varepsilon^{abcde} \widehat F'_{bc} \widehat G_{de}
\end{aligned}
\tag{36}
```

```math
\left.e^{-1}\mathcal L_{VL}\right|_{\text{parent group }17}=\begin{aligned}
&- \frac{i}{16} A'_a \bar\lambda'^i \gamma^{ab} \gamma\cdot\widehat G \psi_{bi}\\
&+\frac{i}{4} A'_a \bar\lambda'^i \gamma^{ab} \gamma\cdot T \psi_{bi}\\
&- \frac{i g}{8} A'_a \bar\lambda'^i \gamma^{ab} L_{ij} \psi_b^j\\
&+\frac{i}{4} A'_a \bar\lambda'^i \gamma^{ab} \phi_{bi}
\end{aligned}
\tag{37}
```

```math
\left.e^{-1}\mathcal L_{VL}\right|_{\text{parent group }18}=\begin{aligned}
&- \frac{1}{16} A'_a \rho' \bar\psi_b^i \gamma^{ba} \gamma^c \gamma\cdot\widehat G \psi_{ci}\\
&+\frac{1}{4} A'_a \rho' \bar\psi_b^i \gamma^{ba} \gamma^c \gamma\cdot T \psi_{ci}\\
&- \frac{g}{8} A'_a \rho' \bar\psi_b^i \gamma^{ba} \gamma^c L_{ij} \psi_c^j\\
&+\frac{1}{4} A'_a \rho' \bar\psi_b^i \gamma^{ba} \gamma^c \phi_{ci}
\end{aligned}
\tag{38}
```

```math
\left.e^{-1}\mathcal L_{VL}\right|_{\text{parent group }19}=\begin{aligned}
&- \frac{1}{4} A'_a \bar\psi_b^i \gamma^{ba} \not{\mathcal D}\lambda'_i
\end{aligned}
\tag{39}
```

```math
\left.e^{-1}\mathcal L_{VL}\right|_{\text{parent group }20}=\begin{aligned}
&+\frac{i}{2} A'_a \bar\psi_b^i \gamma^{ba} \gamma\cdot T \lambda'_i
\end{aligned}
\tag{40}
```

```math
\left.e^{-1}\mathcal L_{VL}\right|_{\text{parent group }21}=\begin{aligned}
&- 4 i A'_a \rho' \bar\psi_b^i \gamma^{ba} \chi_i
\end{aligned}
\tag{41}
```

```math
\left.e^{-1}\mathcal L_{VL}\right|_{\text{parent group }22}=\begin{aligned}
&- \frac{i}{16} A'_a \bar\psi_b^i \gamma^{ba} \gamma\cdot\widehat G \lambda'_i
\end{aligned}
\tag{42}
```

```math
\left.e^{-1}\mathcal L_{VL}\right|_{\text{parent group }23}=\begin{aligned}
&+\frac{i g}{8} A'_a \bar\psi_b^i \gamma^{ba} L_{ij} \lambda'^j
\end{aligned}
\tag{43}
```

```math
\left.e^{-1}\mathcal L_{VL}\right|_{\text{parent group }24}=\begin{aligned}
&- \frac{g}{8} A'_a \rho' \bar\psi_b^i \gamma^{abc} \psi_c^j L_{ij}
\end{aligned}
\tag{44}
```

```math
\left.e^{-1}\mathcal L_{VL}\right|_{\text{parent group }25}=\begin{aligned}
&+\frac{1}{4} A'_a \bar\psi_b^i \gamma^{abc} \psi_c^j Y'_{ij}
\end{aligned}
\tag{45}
```

```math
\left.e^{-1}\mathcal L_{VL}\right|_{\text{parent group }26}=\begin{aligned}
&+\frac{1}{2} \rho' \Box_c\rho'
\end{aligned}
\tag{46}
```

```math
\left.e^{-1}\mathcal L_{VL}\right|_{\text{parent group }27}=\begin{aligned}
&+(\rho')^2 f_a^a
\end{aligned}
\tag{47}
```

```math
\left.e^{-1}\mathcal L_{VL}\right|_{\text{parent group }28}=\begin{aligned}
&- \frac{1}{4} \rho' \widehat F'_{ab} \widehat G^{ab}
\end{aligned}
\tag{48}
```

```math
\left.e^{-1}\mathcal L_{VL}\right|_{\text{parent group }29}=\begin{aligned}
&+4 (\rho')^2 \widehat G_{ab} T^{ab}
\end{aligned}
\tag{49}
```

```math
\left.e^{-1}\mathcal L_{VL}\right|_{\text{parent group }30}=\begin{aligned}
&+4 \rho' \widehat F'_{ab} T^{ab}
\end{aligned}
\tag{50}
```

```math
\left.e^{-1}\mathcal L_{VL}\right|_{\text{parent group }31}=\begin{aligned}
&-4 (\rho')^2 D
\end{aligned}
\tag{51}
```

```math
\left.e^{-1}\mathcal L_{VL}\right|_{\text{parent group }32}=\begin{aligned}
&- \frac{104}{3} (\rho')^2 T^2
\end{aligned}
\tag{52}
```

```math
\left.e^{-1}\mathcal L_{VL}\right|_{\text{parent group }33}=\begin{aligned}
&+8 i \rho' \bar\chi \lambda'
\end{aligned}
\tag{53}
```

```math
\left.e^{-1}\mathcal L_{VL}\right|_{\text{parent group }34}=\begin{aligned}
&-5 (\rho')^2 \bar\psi_a^i \gamma^a \chi_i
\end{aligned}
\tag{54}
```

```math
\left.e^{-1}\mathcal L_{VL}\right|_{\text{parent group }35}=\begin{aligned}
&+\frac{i}{4} \rho' \bar\psi_a^i \gamma^a \not{\mathcal D}\lambda'_i
\end{aligned}
\tag{55}
```

```math
\left.e^{-1}\mathcal L_{VL}\right|_{\text{parent group }36}=\begin{aligned}
&+\frac{1}{2} \rho' \bar\psi_a^i \gamma^a \gamma\cdot T \lambda'_i
\end{aligned}
\tag{56}
```

```math
\left.e^{-1}\mathcal L_{VL}\right|_{\text{parent group }37}=\begin{aligned}
&- \frac{1}{16} \rho' \bar\psi_a^i \gamma^a \gamma\cdot\widehat G \lambda'_i
\end{aligned}
\tag{57}
```

```math
\left.e^{-1}\mathcal L_{VL}\right|_{\text{parent group }38}=\begin{aligned}
&+\frac{g}{8} \rho' \bar\psi_a^i \gamma^a L_{ij} \lambda'^j
\end{aligned}
\tag{58}
```

```math
\left.e^{-1}\mathcal L_{VL}\right|_{\text{parent group }39}=\begin{aligned}
&+\frac{i}{16} (\rho')^2 \bar\psi_a^i \gamma^a \gamma^b \gamma\cdot\widehat G \psi_{bi}\\
&- \frac{i}{4} (\rho')^2 \bar\psi_a^i \gamma^a \gamma^b \gamma\cdot T \psi_{bi}\\
&+\frac{i g}{8} (\rho')^2 \bar\psi_a^i \gamma^a \gamma^b L_{ij} \psi_b^j\\
&- \frac{i}{4} (\rho')^2 \bar\psi_a^i \gamma^a \gamma^b \phi_{bi}
\end{aligned}
\tag{59}
```

```math
\left.e^{-1}\mathcal L_{VL}\right|_{\text{parent group }40}=\begin{aligned}
&- \frac{i}{16} (\rho')^2 \bar\psi_a^i \gamma\cdot\widehat G \psi^a_i\\
&+\frac{i}{4} (\rho')^2 \bar\psi_a^i \gamma\cdot T \psi^a_i\\
&- \frac{i g}{8} (\rho')^2 \bar\psi_a^i L_{ij} \psi^{aj}\\
&+\frac{i}{4} (\rho')^2 \bar\psi_a^i \phi^a_i
\end{aligned}
\tag{60}
```

```math
\left.e^{-1}\mathcal L_{VL}\right|_{\text{parent group }41}=\begin{aligned}
&- \frac{i g}{8} (\rho')^2 \bar\psi_a^i \gamma^{ab} \psi_b^j L_{ij}
\end{aligned}
\tag{61}
```

```math
\left.e^{-1}\mathcal L_{VL}\right|_{\text{parent group }42}=\begin{aligned}
&+\frac{i}{4} \rho' \bar\psi_a^i \gamma^{ab} \psi_b^j Y'_{ij}
\end{aligned}
\tag{62}
```

### 4.4 Distribution and omission ledger

For each source row: substitute the two scalar monomials or eight gaugino monomials at each occurrence; raise the displayed free spinor index with epsilon; multiply coefficients; add exponents of the commuting scalar $`L`$; retain the original ordered spinor/gamma factors; then sort by the sum of explicit degrees. The bilinear square uses the three-term identity in Section 4.1. The table records the number of resulting rows, before optional Clifford or Fierz reduction.

| Parent group | Degree 0 | Degree 2 | Degree 4 | Omitted degree 6 |
|---|---:|---:|---:|---:|

| 1 | 1 | 0 | 0 | 0 |

| 2 | 1 | 1 | 0 | 0 |

| 3 | 0 | 120 | 100 | 20 |

| 4 | 0 | 36 | 24 | 4 |

| 5 | 0 | 6 | 8 | 2 |

| 6 | 0 | 36 | 24 | 4 |

| 7 | 0 | 36 | 24 | 4 |

| 8 | 0 | 6 | 8 | 2 |

| 9 | 0 | 6 | 2 | 0 |

| 10 | 0 | 24 | 32 | 8 |

| 11 | 2 | 4 | 0 | 0 |

| 12 | 1 | 1 | 0 | 0 |

| 13 | 1 | 0 | 0 | 0 |

| 14 | 2 | 4 | 0 | 0 |

| 15 | 1 | 1 | 0 | 0 |

| 16 | 1 | 0 | 0 | 0 |

| 17 | 0 | 24 | 8 | 0 |

| 18 | 0 | 4 | 4 | 0 |

| 19 | 0 | 20 | 10 | 0 |

| 20 | 0 | 6 | 2 | 0 |

| 21 | 0 | 1 | 1 | 0 |

| 22 | 0 | 6 | 2 | 0 |

| 23 | 0 | 6 | 2 | 0 |

| 24 | 0 | 1 | 1 | 0 |

| 25 | 0 | 1 | 0 | 0 |

| 26 | 1 | 2 | 1 | 0 |

| 27 | 1 | 1 | 1 | 0 |

| 28 | 1 | 1 | 0 | 0 |

| 29 | 1 | 1 | 1 | 0 |

| 30 | 1 | 1 | 0 | 0 |

| 31 | 1 | 1 | 1 | 0 |

| 32 | 1 | 1 | 1 | 0 |

| 33 | 0 | 6 | 8 | 2 |

| 34 | 0 | 1 | 1 | 1 |

| 35 | 0 | 20 | 30 | 10 |

| 36 | 0 | 6 | 8 | 2 |

| 37 | 0 | 6 | 8 | 2 |

| 38 | 0 | 6 | 8 | 2 |

| 39 | 0 | 4 | 4 | 4 |

| 40 | 0 | 4 | 4 | 4 |

| 41 | 0 | 1 | 1 | 1 |

| 42 | 0 | 1 | 1 | 0 |

Only the degree-six rows are omitted. No hidden completion is set to zero by this table. The ordered partial-insertion builder retains their coefficients and ordered factors when generating its expansion ledger.

## 5. Consistency Checks

### 5.1 Algebra, signs and source coverage

The [ordered partial-insertion builder](../../../../src/kernels/build_step5a_partial_insertion.py) implements the formal-factor expansion used here. The [component-check runner](../../../../checks/run_component_checks.py) uses these factors in the complete degree-two supercovariant insertion and compares its regenerated tensor ledgers with the retained action. The independent ordered-product check is [verify_step6_supercovariant.py](../../../../src/kernels/verify_step6_supercovariant.py). Its scope is stated in [Step 6](10_step6_gauged_action_through_two_fermions.md); the present partial insertion alone does not test Clifford/Fierz identities or full local supersymmetry.

The scalar-square cross factor and quartic sign are derived in Section 4.1. The bar-map rank-two sign and epsilon raising are shown in Section 3. Every multiplicative row remains even, and its parent free-index pattern is closed. Fresh dummy names avoid collisions between two inserted maps. No gauge invariance of an individually truncated explicit-degree sector is asserted.

### 5.2 Weights and limits

The pre-gauge weights are $`w(L)=w(L_{ij})=3`$, $`w(N)=w(E_a)=4`$, $`w(\varphi)=7/2`$, $`w(T)=1`$, $`w(\chi)=3/2`$. The scalar monomials have weights $`-3+4=1`$ and $`-9+3+7=1`$. The eight gaugino monomials have weights:

```math
-3+1+\tfrac72=\tfrac32,\quad -3+3+\tfrac32=\tfrac32,\quad -3+1+\tfrac72=\tfrac32,\quad4-9+3+\tfrac72=\tfrac32.
\tag{63}
```

```math
-9+4+3+\tfrac72=\tfrac32,\quad -9+4+3+\tfrac72=\tfrac32,\quad -9+3\tfrac72=\tfrac32,\quad -15+3\tfrac72+6=\tfrac32.
\tag{64}
```

Every replacement therefore has its original slot weight; a covariant derivative adds one. Each Step 4 parent term consequently retains its pre-gauge weight five after restoring the fixed compensator powers. This weight argument applies term by term to every Cartesian-product row, including discarded rows. No Poincaré normalization or value of the curvature-squared coupling is inferred.

Setting the explicit odd fields to zero leaves exactly the 17 degree-zero rows; the actual bosonic operator restriction is then performed in Section 6.4. Setting $`g=0`$ removes precisely coefficients containing explicit $`g`$ while leaving common background slots fixed; it is a coefficient limit, not the full ungauged composite substitution.

### 5.3 Truncation scope

The remainder begins at formal explicit degree six. There is no numerical norm bound on this Grassmann-degree projection. A true expansion by physical fermion number requires opening the retained composites and connections; the present sectors must not be used as already complete quadratic or quartic action kernels.

## 6. Final Result

The result is the sum of the three explicitly printed sectors below. Each labelled row contributes with the displayed coefficient; labels are equation identifiers, not new physical fields. All multiplicative products are distributed. Covariant derivative operators remain in the declared representation.

```math
\left.e^{-1}\mathcal L_{VL}\right|_{\rho^{\prime},\lambda^{\prime}\ \mathrm{inserted}}=\left.e^{-1}\mathcal L_{VL}\right|_{[0]}+\left.e^{-1}\mathcal L_{VL}\right|_{[2]}+\left.e^{-1}\mathcal L_{VL}\right|_{[4]}+O_{\mathrm{explicit}}(\mathrm{fermion}^{6}).
\tag{65}
```

### 6.1 Bosonic-looking sector: no explicit fermions

```math
\begin{aligned}
&+Y'^{ij} Y'_{ij}\qquad\text{(0.1; G1)}\\
&- \frac{2 N g}{L} Y'^{ij} L_{ij}\qquad\text{(0.2; G2)}\\
&+\frac{N}{L^{2}} A'_a (\mathcal D_{b}L) \widehat G^{ab}\qquad\text{(0.3; G11)}\\
&- \frac{1}{L} A'_a (\mathcal D_{b}N) \widehat G^{ab}\qquad\text{(0.4; G11)}
\end{aligned}
\tag{66}
```

```math
\begin{aligned}
&- \frac{N}{L} A'_a \mathcal D_b\widehat G^{ab}\qquad\text{(0.5; G12)}\\
&- \frac{1}{2} A'_a \mathcal D_b\widehat F'^{ab}\qquad\text{(0.6; G13)}\\
&- \frac{16 N}{L^{2}} A'_a (\mathcal D_{b}L) T^{ab}\qquad\text{(0.7; G14)}\\
&+\frac{16}{L} A'_a (\mathcal D_{b}N) T^{ab}\qquad\text{(0.8; G14)}
\end{aligned}
\tag{67}
```

```math
\begin{aligned}
&+\frac{16 N}{L} A'_a \mathcal D_bT^{ab}\qquad\text{(0.9; G15)}\\
&- \frac{1}{8} A'_a \varepsilon^{abcde} \widehat F'_{bc} \widehat G_{de}\qquad\text{(0.10; G16)}\\
&+\frac{2 N}{L} \Box_c\!\left(L^{-1}N\right)\qquad\text{(0.11; G26)}\\
&+\frac{4 N^{2}}{L^{2}} f_a^a\qquad\text{(0.12; G27)}
\end{aligned}
\tag{68}
```

```math
\begin{aligned}
&- \frac{N}{2 L} \widehat F'_{ab} \widehat G^{ab}\qquad\text{(0.13; G28)}\\
&+\frac{16 N^{2}}{L^{2}} \widehat G_{ab} T^{ab}\qquad\text{(0.14; G29)}\\
&+\frac{8 N}{L} \widehat F'_{ab} T^{ab}\qquad\text{(0.15; G30)}\\
&- \frac{16 N^{2}}{L^{2}} D\qquad\text{(0.16; G31)}
\end{aligned}
\tag{69}
```

```math
\begin{aligned}
&- \frac{416 N^{2}}{3 L^{2}} T^2\qquad\text{(0.17; G32)}
\end{aligned}
\tag{70}
```

### 6.2 Two explicit fermions

```math
\begin{aligned}
&- \frac{i g}{L^{3}} L_{r_3s_3} \bar\varphi^{r_3} \varphi^{s_3} Y'^{ij} L_{ij}\qquad\text{(2.1; G2)}\\
&- \frac{2}{L^{3}} \varepsilon^{ir_{6}} (\mathcal D_{d_{6}}\bar\varphi_{r_{6}}) \gamma^{d_{6}} \gamma^{q_{7}} (\mathcal D_{q_{7}}L) \not{\mathcal D}\varphi_{i}\qquad\text{(2.2; G3)}\\
&+\frac{2}{L^{2}} \varepsilon^{ir_{6}} (\mathcal D_{d_{6}}\bar\varphi_{r_{6}}) \gamma^{d_{6}} \gamma^{q_{7}} \mathcal D_{q_{7}}\!\left(\not{\mathcal D}\varphi_{i}\right)\qquad\text{(2.3; G3)}\\
&- \frac{16 i}{L^{3}} \varepsilon^{ir_{6}} (\mathcal D_{d_{6}}\bar\varphi_{r_{6}}) \gamma^{d_{6}} \gamma^{q_{7}} (\mathcal D_{q_{7}}L) L_{ij_{7}} \chi^{j_{7}}\qquad\text{(2.4; G3)}
\end{aligned}
\tag{71}
```

```math
\begin{aligned}
&+\frac{16 i}{L^{2}} \varepsilon^{ir_{6}} (\mathcal D_{d_{6}}\bar\varphi_{r_{6}}) \gamma^{d_{6}} \gamma^{q_{7}} \mathcal D_{q_{7}}\!\left(L_{ij_{7}}\right) \chi^{j_{7}}\qquad\text{(2.5; G3)}\\
&+\frac{16 i}{L^{2}} \varepsilon^{ir_{6}} (\mathcal D_{d_{6}}\bar\varphi_{r_{6}}) \gamma^{d_{6}} \gamma^{q_{7}} L_{ij_{7}} \mathcal D_{q_{7}}\!\left(\chi^{j_{7}}\right)\qquad\text{(2.6; G3)}\\
&- \frac{4 i}{L^{3}} \varepsilon^{ir_{6}} (\mathcal D_{d_{6}}\bar\varphi_{r_{6}}) \gamma^{d_{6}} \gamma^{q_{7}} (\mathcal D_{q_{7}}L) \gamma\!\cdot\!T \varphi_{i}\qquad\text{(2.7; G3)}\\
&+\frac{4 i}{L^{2}} \varepsilon^{ir_{6}} (\mathcal D_{d_{6}}\bar\varphi_{r_{6}}) \gamma^{d_{6}} \gamma^{q_{7}} \gamma\!\cdot\!T \mathcal D_{q_{7}}\!\left(\varphi_{i}\right)\qquad\text{(2.8; G3)}
\end{aligned}
\tag{72}
```

```math
\begin{aligned}
&+\frac{6 i N}{L^{5}} \varepsilon^{ir_{6}} (\mathcal D_{d_{6}}\bar\varphi_{r_{6}}) \gamma^{d_{6}} \gamma^{q_{7}} (\mathcal D_{q_{7}}L) L_{ij_{7}} \varphi^{j_{7}}\qquad\text{(2.9; G3)}\\
&- \frac{2 i}{L^{4}} \varepsilon^{ir_{6}} (\mathcal D_{d_{6}}\bar\varphi_{r_{6}}) \gamma^{d_{6}} \gamma^{q_{7}} (\mathcal D_{q_{7}}N) L_{ij_{7}} \varphi^{j_{7}}\qquad\text{(2.10; G3)}\\
&- \frac{2 i N}{L^{4}} \varepsilon^{ir_{6}} (\mathcal D_{d_{6}}\bar\varphi_{r_{6}}) \gamma^{d_{6}} \gamma^{q_{7}} \mathcal D_{q_{7}}\!\left(L_{ij_{7}}\right) \varphi^{j_{7}}\qquad\text{(2.11; G3)}\\
&- \frac{2 i N}{L^{4}} \varepsilon^{ir_{6}} (\mathcal D_{d_{6}}\bar\varphi_{r_{6}}) \gamma^{d_{6}} \gamma^{q_{7}} L_{ij_{7}} \mathcal D_{q_{7}}\!\left(\varphi^{j_{7}}\right)\qquad\text{(2.12; G3)}
\end{aligned}
\tag{73}
```

```math
\begin{aligned}
&+\frac{6}{L^{5}} \varepsilon^{ir_{6}} (\mathcal D_{d_{6}}\bar\varphi_{r_{6}}) \gamma^{d_{6}} \gamma^{q_{7}} (\mathcal D_{q_{7}}L) (\not{\mathcal D}L_{ij_{7}}) L^{j_{7}k_{7}} \varphi_{k_{7}}\qquad\text{(2.13; G3)}\\
&- \frac{2}{L^{4}} \varepsilon^{ir_{6}} (\mathcal D_{d_{6}}\bar\varphi_{r_{6}}) \gamma^{d_{6}} \gamma^{q_{7}} \mathcal D_{q_{7}}\!\left((\not{\mathcal D}L_{ij_{7}})\right) L^{j_{7}k_{7}} \varphi_{k_{7}}\qquad\text{(2.14; G3)}\\
&- \frac{2}{L^{4}} \varepsilon^{ir_{6}} (\mathcal D_{d_{6}}\bar\varphi_{r_{6}}) \gamma^{d_{6}} \gamma^{q_{7}} (\not{\mathcal D}L_{ij_{7}}) \mathcal D_{q_{7}}\!\left(L^{j_{7}k_{7}}\right) \varphi_{k_{7}}\qquad\text{(2.15; G3)}\\
&- \frac{2}{L^{4}} \varepsilon^{ir_{6}} (\mathcal D_{d_{6}}\bar\varphi_{r_{6}}) \gamma^{d_{6}} \gamma^{q_{7}} (\not{\mathcal D}L_{ij_{7}}) L^{j_{7}k_{7}} \mathcal D_{q_{7}}\!\left(\varphi_{k_{7}}\right)\qquad\text{(2.16; G3)}
\end{aligned}
\tag{74}
```

```math
\begin{aligned}
&- \frac{6}{L^{5}} \varepsilon^{ir_{6}} (\mathcal D_{d_{6}}\bar\varphi_{r_{6}}) \gamma^{d_{6}} \gamma^{q_{7}} (\mathcal D_{q_{7}}L) \not E L_{ij_{7}} \varphi^{j_{7}}\qquad\text{(2.17; G3)}\\
&+\frac{2}{L^{4}} \varepsilon^{ir_{6}} (\mathcal D_{d_{6}}\bar\varphi_{r_{6}}) \gamma^{d_{6}} \gamma^{q_{7}} \mathcal D_{q_{7}}\!\left(\not E\right) L_{ij_{7}} \varphi^{j_{7}}\qquad\text{(2.18; G3)}\\
&+\frac{2}{L^{4}} \varepsilon^{ir_{6}} (\mathcal D_{d_{6}}\bar\varphi_{r_{6}}) \gamma^{d_{6}} \gamma^{q_{7}} \not E \mathcal D_{q_{7}}\!\left(L_{ij_{7}}\right) \varphi^{j_{7}}\qquad\text{(2.19; G3)}\\
&+\frac{2}{L^{4}} \varepsilon^{ir_{6}} (\mathcal D_{d_{6}}\bar\varphi_{r_{6}}) \gamma^{d_{6}} \gamma^{q_{7}} \not E L_{ij_{7}} \mathcal D_{q_{7}}\!\left(\varphi^{j_{7}}\right)\qquad\text{(2.20; G3)}
\end{aligned}
\tag{75}
```

```math
\begin{aligned}
&+\frac{4 i}{L^{2}} \varepsilon^{ir_{6}} (\mathcal D_{d_{6}}\bar\varphi_{r_{6}}) \gamma^{d_{6}} \gamma^{q_{7}} \gamma^{mn}(\mathcal D_{q_{7}}T_{mn}) \varphi_{i}\qquad\text{(2.21; G3)}\\
&- \frac{16 i}{L^{3}} \varepsilon^{ir_{6}} L_{r_{6}j_{6}} \bar\chi^{j_{6}} \gamma^{q_{7}} (\mathcal D_{q_{7}}L) \not{\mathcal D}\varphi_{i}\qquad\text{(2.22; G3)}\\
&+\frac{16 i}{L^{2}} \varepsilon^{ir_{6}} L_{r_{6}j_{6}} \bar\chi^{j_{6}} \gamma^{q_{7}} \mathcal D_{q_{7}}\!\left(\not{\mathcal D}\varphi_{i}\right)\qquad\text{(2.23; G3)}\\
&+\frac{128}{L^{3}} \varepsilon^{ir_{6}} L_{r_{6}j_{6}} \bar\chi^{j_{6}} \gamma^{q_{7}} (\mathcal D_{q_{7}}L) L_{ij_{7}} \chi^{j_{7}}\qquad\text{(2.24; G3)}
\end{aligned}
\tag{76}
```

```math
\begin{aligned}
&- \frac{128}{L^{2}} \varepsilon^{ir_{6}} L_{r_{6}j_{6}} \bar\chi^{j_{6}} \gamma^{q_{7}} \mathcal D_{q_{7}}\!\left(L_{ij_{7}}\right) \chi^{j_{7}}\qquad\text{(2.25; G3)}\\
&- \frac{128}{L^{2}} \varepsilon^{ir_{6}} L_{r_{6}j_{6}} \bar\chi^{j_{6}} \gamma^{q_{7}} L_{ij_{7}} \mathcal D_{q_{7}}\!\left(\chi^{j_{7}}\right)\qquad\text{(2.26; G3)}\\
&+\frac{32}{L^{3}} \varepsilon^{ir_{6}} L_{r_{6}j_{6}} \bar\chi^{j_{6}} \gamma^{q_{7}} (\mathcal D_{q_{7}}L) \gamma\!\cdot\!T \varphi_{i}\qquad\text{(2.27; G3)}\\
&- \frac{32}{L^{2}} \varepsilon^{ir_{6}} L_{r_{6}j_{6}} \bar\chi^{j_{6}} \gamma^{q_{7}} \gamma\!\cdot\!T \mathcal D_{q_{7}}\!\left(\varphi_{i}\right)\qquad\text{(2.28; G3)}
\end{aligned}
\tag{77}
```

```math
\begin{aligned}
&- \frac{48 N}{L^{5}} \varepsilon^{ir_{6}} L_{r_{6}j_{6}} \bar\chi^{j_{6}} \gamma^{q_{7}} (\mathcal D_{q_{7}}L) L_{ij_{7}} \varphi^{j_{7}}\qquad\text{(2.29; G3)}\\
&+\frac{16}{L^{4}} \varepsilon^{ir_{6}} L_{r_{6}j_{6}} \bar\chi^{j_{6}} \gamma^{q_{7}} (\mathcal D_{q_{7}}N) L_{ij_{7}} \varphi^{j_{7}}\qquad\text{(2.30; G3)}\\
&+\frac{16 N}{L^{4}} \varepsilon^{ir_{6}} L_{r_{6}j_{6}} \bar\chi^{j_{6}} \gamma^{q_{7}} \mathcal D_{q_{7}}\!\left(L_{ij_{7}}\right) \varphi^{j_{7}}\qquad\text{(2.31; G3)}\\
&+\frac{16 N}{L^{4}} \varepsilon^{ir_{6}} L_{r_{6}j_{6}} \bar\chi^{j_{6}} \gamma^{q_{7}} L_{ij_{7}} \mathcal D_{q_{7}}\!\left(\varphi^{j_{7}}\right)\qquad\text{(2.32; G3)}
\end{aligned}
\tag{78}
```

```math
\begin{aligned}
&+\frac{48 i}{L^{5}} \varepsilon^{ir_{6}} L_{r_{6}j_{6}} \bar\chi^{j_{6}} \gamma^{q_{7}} (\mathcal D_{q_{7}}L) (\not{\mathcal D}L_{ij_{7}}) L^{j_{7}k_{7}} \varphi_{k_{7}}\qquad\text{(2.33; G3)}\\
&- \frac{16 i}{L^{4}} \varepsilon^{ir_{6}} L_{r_{6}j_{6}} \bar\chi^{j_{6}} \gamma^{q_{7}} \mathcal D_{q_{7}}\!\left((\not{\mathcal D}L_{ij_{7}})\right) L^{j_{7}k_{7}} \varphi_{k_{7}}\qquad\text{(2.34; G3)}\\
&- \frac{16 i}{L^{4}} \varepsilon^{ir_{6}} L_{r_{6}j_{6}} \bar\chi^{j_{6}} \gamma^{q_{7}} (\not{\mathcal D}L_{ij_{7}}) \mathcal D_{q_{7}}\!\left(L^{j_{7}k_{7}}\right) \varphi_{k_{7}}\qquad\text{(2.35; G3)}\\
&- \frac{16 i}{L^{4}} \varepsilon^{ir_{6}} L_{r_{6}j_{6}} \bar\chi^{j_{6}} \gamma^{q_{7}} (\not{\mathcal D}L_{ij_{7}}) L^{j_{7}k_{7}} \mathcal D_{q_{7}}\!\left(\varphi_{k_{7}}\right)\qquad\text{(2.36; G3)}
\end{aligned}
\tag{79}
```

```math
\begin{aligned}
&- \frac{48 i}{L^{5}} \varepsilon^{ir_{6}} L_{r_{6}j_{6}} \bar\chi^{j_{6}} \gamma^{q_{7}} (\mathcal D_{q_{7}}L) \not E L_{ij_{7}} \varphi^{j_{7}}\qquad\text{(2.37; G3)}\\
&+\frac{16 i}{L^{4}} \varepsilon^{ir_{6}} L_{r_{6}j_{6}} \bar\chi^{j_{6}} \gamma^{q_{7}} \mathcal D_{q_{7}}\!\left(\not E\right) L_{ij_{7}} \varphi^{j_{7}}\qquad\text{(2.38; G3)}\\
&+\frac{16 i}{L^{4}} \varepsilon^{ir_{6}} L_{r_{6}j_{6}} \bar\chi^{j_{6}} \gamma^{q_{7}} \not E \mathcal D_{q_{7}}\!\left(L_{ij_{7}}\right) \varphi^{j_{7}}\qquad\text{(2.39; G3)}\\
&+\frac{16 i}{L^{4}} \varepsilon^{ir_{6}} L_{r_{6}j_{6}} \bar\chi^{j_{6}} \gamma^{q_{7}} \not E L_{ij_{7}} \mathcal D_{q_{7}}\!\left(\varphi^{j_{7}}\right)\qquad\text{(2.40; G3)}
\end{aligned}
\tag{80}
```

```math
\begin{aligned}
&- \frac{32}{L^{2}} \varepsilon^{ir_{6}} L_{r_{6}j_{6}} \bar\chi^{j_{6}} \gamma^{q_{7}} \gamma^{mn}(\mathcal D_{q_{7}}T_{mn}) \varphi_{i}\qquad\text{(2.41; G3)}\\
&+\frac{4 i}{L^{3}} \varepsilon^{ir_{6}} \bar\varphi_{r_{6}} \gamma\!\cdot\!T \gamma^{q_{7}} (\mathcal D_{q_{7}}L) \not{\mathcal D}\varphi_{i}\qquad\text{(2.42; G3)}\\
&- \frac{4 i}{L^{2}} \varepsilon^{ir_{6}} \bar\varphi_{r_{6}} \gamma\!\cdot\!T \gamma^{q_{7}} \mathcal D_{q_{7}}\!\left(\not{\mathcal D}\varphi_{i}\right)\qquad\text{(2.43; G3)}\\
&- \frac{32}{L^{3}} \varepsilon^{ir_{6}} \bar\varphi_{r_{6}} \gamma\!\cdot\!T \gamma^{q_{7}} (\mathcal D_{q_{7}}L) L_{ij_{7}} \chi^{j_{7}}\qquad\text{(2.44; G3)}
\end{aligned}
\tag{81}
```

```math
\begin{aligned}
&+\frac{32}{L^{2}} \varepsilon^{ir_{6}} \bar\varphi_{r_{6}} \gamma\!\cdot\!T \gamma^{q_{7}} \mathcal D_{q_{7}}\!\left(L_{ij_{7}}\right) \chi^{j_{7}}\qquad\text{(2.45; G3)}\\
&+\frac{32}{L^{2}} \varepsilon^{ir_{6}} \bar\varphi_{r_{6}} \gamma\!\cdot\!T \gamma^{q_{7}} L_{ij_{7}} \mathcal D_{q_{7}}\!\left(\chi^{j_{7}}\right)\qquad\text{(2.46; G3)}\\
&- \frac{8}{L^{3}} \varepsilon^{ir_{6}} \bar\varphi_{r_{6}} \gamma\!\cdot\!T \gamma^{q_{7}} (\mathcal D_{q_{7}}L) \gamma\!\cdot\!T \varphi_{i}\qquad\text{(2.47; G3)}\\
&+\frac{8}{L^{2}} \varepsilon^{ir_{6}} \bar\varphi_{r_{6}} \gamma\!\cdot\!T \gamma^{q_{7}} \gamma\!\cdot\!T \mathcal D_{q_{7}}\!\left(\varphi_{i}\right)\qquad\text{(2.48; G3)}
\end{aligned}
\tag{82}
```

```math
\begin{aligned}
&+\frac{12 N}{L^{5}} \varepsilon^{ir_{6}} \bar\varphi_{r_{6}} \gamma\!\cdot\!T \gamma^{q_{7}} (\mathcal D_{q_{7}}L) L_{ij_{7}} \varphi^{j_{7}}\qquad\text{(2.49; G3)}\\
&- \frac{4}{L^{4}} \varepsilon^{ir_{6}} \bar\varphi_{r_{6}} \gamma\!\cdot\!T \gamma^{q_{7}} (\mathcal D_{q_{7}}N) L_{ij_{7}} \varphi^{j_{7}}\qquad\text{(2.50; G3)}\\
&- \frac{4 N}{L^{4}} \varepsilon^{ir_{6}} \bar\varphi_{r_{6}} \gamma\!\cdot\!T \gamma^{q_{7}} \mathcal D_{q_{7}}\!\left(L_{ij_{7}}\right) \varphi^{j_{7}}\qquad\text{(2.51; G3)}\\
&- \frac{4 N}{L^{4}} \varepsilon^{ir_{6}} \bar\varphi_{r_{6}} \gamma\!\cdot\!T \gamma^{q_{7}} L_{ij_{7}} \mathcal D_{q_{7}}\!\left(\varphi^{j_{7}}\right)\qquad\text{(2.52; G3)}
\end{aligned}
\tag{83}
```

```math
\begin{aligned}
&- \frac{12 i}{L^{5}} \varepsilon^{ir_{6}} \bar\varphi_{r_{6}} \gamma\!\cdot\!T \gamma^{q_{7}} (\mathcal D_{q_{7}}L) (\not{\mathcal D}L_{ij_{7}}) L^{j_{7}k_{7}} \varphi_{k_{7}}\qquad\text{(2.53; G3)}\\
&+\frac{4 i}{L^{4}} \varepsilon^{ir_{6}} \bar\varphi_{r_{6}} \gamma\!\cdot\!T \gamma^{q_{7}} \mathcal D_{q_{7}}\!\left((\not{\mathcal D}L_{ij_{7}})\right) L^{j_{7}k_{7}} \varphi_{k_{7}}\qquad\text{(2.54; G3)}\\
&+\frac{4 i}{L^{4}} \varepsilon^{ir_{6}} \bar\varphi_{r_{6}} \gamma\!\cdot\!T \gamma^{q_{7}} (\not{\mathcal D}L_{ij_{7}}) \mathcal D_{q_{7}}\!\left(L^{j_{7}k_{7}}\right) \varphi_{k_{7}}\qquad\text{(2.55; G3)}\\
&+\frac{4 i}{L^{4}} \varepsilon^{ir_{6}} \bar\varphi_{r_{6}} \gamma\!\cdot\!T \gamma^{q_{7}} (\not{\mathcal D}L_{ij_{7}}) L^{j_{7}k_{7}} \mathcal D_{q_{7}}\!\left(\varphi_{k_{7}}\right)\qquad\text{(2.56; G3)}
\end{aligned}
\tag{84}
```

```math
\begin{aligned}
&+\frac{12 i}{L^{5}} \varepsilon^{ir_{6}} \bar\varphi_{r_{6}} \gamma\!\cdot\!T \gamma^{q_{7}} (\mathcal D_{q_{7}}L) \not E L_{ij_{7}} \varphi^{j_{7}}\qquad\text{(2.57; G3)}\\
&- \frac{4 i}{L^{4}} \varepsilon^{ir_{6}} \bar\varphi_{r_{6}} \gamma\!\cdot\!T \gamma^{q_{7}} \mathcal D_{q_{7}}\!\left(\not E\right) L_{ij_{7}} \varphi^{j_{7}}\qquad\text{(2.58; G3)}\\
&- \frac{4 i}{L^{4}} \varepsilon^{ir_{6}} \bar\varphi_{r_{6}} \gamma\!\cdot\!T \gamma^{q_{7}} \not E \mathcal D_{q_{7}}\!\left(L_{ij_{7}}\right) \varphi^{j_{7}}\qquad\text{(2.59; G3)}\\
&- \frac{4 i}{L^{4}} \varepsilon^{ir_{6}} \bar\varphi_{r_{6}} \gamma\!\cdot\!T \gamma^{q_{7}} \not E L_{ij_{7}} \mathcal D_{q_{7}}\!\left(\varphi^{j_{7}}\right)\qquad\text{(2.60; G3)}
\end{aligned}
\tag{85}
```

```math
\begin{aligned}
&+\frac{8}{L^{2}} \varepsilon^{ir_{6}} \bar\varphi_{r_{6}} \gamma\!\cdot\!T \gamma^{q_{7}} \gamma^{mn}(\mathcal D_{q_{7}}T_{mn}) \varphi_{i}\qquad\text{(2.61; G3)}\\
&+\frac{2 i N}{L^{5}} \varepsilon^{ir_{6}} L_{r_{6}j_{6}} \bar\varphi^{j_{6}} \gamma^{q_{7}} (\mathcal D_{q_{7}}L) \not{\mathcal D}\varphi_{i}\qquad\text{(2.62; G3)}\\
&- \frac{2 i N}{L^{4}} \varepsilon^{ir_{6}} L_{r_{6}j_{6}} \bar\varphi^{j_{6}} \gamma^{q_{7}} \mathcal D_{q_{7}}\!\left(\not{\mathcal D}\varphi_{i}\right)\qquad\text{(2.63; G3)}\\
&- \frac{16 N}{L^{5}} \varepsilon^{ir_{6}} L_{r_{6}j_{6}} \bar\varphi^{j_{6}} \gamma^{q_{7}} (\mathcal D_{q_{7}}L) L_{ij_{7}} \chi^{j_{7}}\qquad\text{(2.64; G3)}
\end{aligned}
\tag{86}
```

```math
\begin{aligned}
&+\frac{16 N}{L^{4}} \varepsilon^{ir_{6}} L_{r_{6}j_{6}} \bar\varphi^{j_{6}} \gamma^{q_{7}} \mathcal D_{q_{7}}\!\left(L_{ij_{7}}\right) \chi^{j_{7}}\qquad\text{(2.65; G3)}\\
&+\frac{16 N}{L^{4}} \varepsilon^{ir_{6}} L_{r_{6}j_{6}} \bar\varphi^{j_{6}} \gamma^{q_{7}} L_{ij_{7}} \mathcal D_{q_{7}}\!\left(\chi^{j_{7}}\right)\qquad\text{(2.66; G3)}\\
&- \frac{4 N}{L^{5}} \varepsilon^{ir_{6}} L_{r_{6}j_{6}} \bar\varphi^{j_{6}} \gamma^{q_{7}} (\mathcal D_{q_{7}}L) \gamma\!\cdot\!T \varphi_{i}\qquad\text{(2.67; G3)}\\
&+\frac{4 N}{L^{4}} \varepsilon^{ir_{6}} L_{r_{6}j_{6}} \bar\varphi^{j_{6}} \gamma^{q_{7}} \gamma\!\cdot\!T \mathcal D_{q_{7}}\!\left(\varphi_{i}\right)\qquad\text{(2.68; G3)}
\end{aligned}
\tag{87}
```

```math
\begin{aligned}
&+\frac{6 N^{2}}{L^{7}} \varepsilon^{ir_{6}} L_{r_{6}j_{6}} \bar\varphi^{j_{6}} \gamma^{q_{7}} (\mathcal D_{q_{7}}L) L_{ij_{7}} \varphi^{j_{7}}\qquad\text{(2.69; G3)}\\
&- \frac{2 N}{L^{6}} \varepsilon^{ir_{6}} L_{r_{6}j_{6}} \bar\varphi^{j_{6}} \gamma^{q_{7}} (\mathcal D_{q_{7}}N) L_{ij_{7}} \varphi^{j_{7}}\qquad\text{(2.70; G3)}\\
&- \frac{2 N^{2}}{L^{6}} \varepsilon^{ir_{6}} L_{r_{6}j_{6}} \bar\varphi^{j_{6}} \gamma^{q_{7}} \mathcal D_{q_{7}}\!\left(L_{ij_{7}}\right) \varphi^{j_{7}}\qquad\text{(2.71; G3)}\\
&- \frac{2 N^{2}}{L^{6}} \varepsilon^{ir_{6}} L_{r_{6}j_{6}} \bar\varphi^{j_{6}} \gamma^{q_{7}} L_{ij_{7}} \mathcal D_{q_{7}}\!\left(\varphi^{j_{7}}\right)\qquad\text{(2.72; G3)}
\end{aligned}
\tag{88}
```

```math
\begin{aligned}
&- \frac{6 i N}{L^{7}} \varepsilon^{ir_{6}} L_{r_{6}j_{6}} \bar\varphi^{j_{6}} \gamma^{q_{7}} (\mathcal D_{q_{7}}L) (\not{\mathcal D}L_{ij_{7}}) L^{j_{7}k_{7}} \varphi_{k_{7}}\qquad\text{(2.73; G3)}\\
&+\frac{2 i N}{L^{6}} \varepsilon^{ir_{6}} L_{r_{6}j_{6}} \bar\varphi^{j_{6}} \gamma^{q_{7}} \mathcal D_{q_{7}}\!\left((\not{\mathcal D}L_{ij_{7}})\right) L^{j_{7}k_{7}} \varphi_{k_{7}}\qquad\text{(2.74; G3)}\\
&+\frac{2 i N}{L^{6}} \varepsilon^{ir_{6}} L_{r_{6}j_{6}} \bar\varphi^{j_{6}} \gamma^{q_{7}} (\not{\mathcal D}L_{ij_{7}}) \mathcal D_{q_{7}}\!\left(L^{j_{7}k_{7}}\right) \varphi_{k_{7}}\qquad\text{(2.75; G3)}\\
&+\frac{2 i N}{L^{6}} \varepsilon^{ir_{6}} L_{r_{6}j_{6}} \bar\varphi^{j_{6}} \gamma^{q_{7}} (\not{\mathcal D}L_{ij_{7}}) L^{j_{7}k_{7}} \mathcal D_{q_{7}}\!\left(\varphi_{k_{7}}\right)\qquad\text{(2.76; G3)}
\end{aligned}
\tag{89}
```

```math
\begin{aligned}
&+\frac{6 i N}{L^{7}} \varepsilon^{ir_{6}} L_{r_{6}j_{6}} \bar\varphi^{j_{6}} \gamma^{q_{7}} (\mathcal D_{q_{7}}L) \not E L_{ij_{7}} \varphi^{j_{7}}\qquad\text{(2.77; G3)}\\
&- \frac{2 i N}{L^{6}} \varepsilon^{ir_{6}} L_{r_{6}j_{6}} \bar\varphi^{j_{6}} \gamma^{q_{7}} \mathcal D_{q_{7}}\!\left(\not E\right) L_{ij_{7}} \varphi^{j_{7}}\qquad\text{(2.78; G3)}\\
&- \frac{2 i N}{L^{6}} \varepsilon^{ir_{6}} L_{r_{6}j_{6}} \bar\varphi^{j_{6}} \gamma^{q_{7}} \not E \mathcal D_{q_{7}}\!\left(L_{ij_{7}}\right) \varphi^{j_{7}}\qquad\text{(2.79; G3)}\\
&- \frac{2 i N}{L^{6}} \varepsilon^{ir_{6}} L_{r_{6}j_{6}} \bar\varphi^{j_{6}} \gamma^{q_{7}} \not E L_{ij_{7}} \mathcal D_{q_{7}}\!\left(\varphi^{j_{7}}\right)\qquad\text{(2.80; G3)}
\end{aligned}
\tag{90}
```

```math
\begin{aligned}
&+\frac{4 N}{L^{4}} \varepsilon^{ir_{6}} L_{r_{6}j_{6}} \bar\varphi^{j_{6}} \gamma^{q_{7}} \gamma^{mn}(\mathcal D_{q_{7}}T_{mn}) \varphi_{i}\qquad\text{(2.81; G3)}\\
&+\frac{2}{L^{5}} \varepsilon^{ir_{6}} L^{j_{6}k_{6}} \bar\varphi_{k_{6}} (\not{\mathcal D}L_{r_{6}j_{6}}) \gamma^{q_{7}} (\mathcal D_{q_{7}}L) \not{\mathcal D}\varphi_{i}\qquad\text{(2.82; G3)}\\
&- \frac{2}{L^{4}} \varepsilon^{ir_{6}} L^{j_{6}k_{6}} \bar\varphi_{k_{6}} (\not{\mathcal D}L_{r_{6}j_{6}}) \gamma^{q_{7}} \mathcal D_{q_{7}}\!\left(\not{\mathcal D}\varphi_{i}\right)\qquad\text{(2.83; G3)}\\
&+\frac{16 i}{L^{5}} \varepsilon^{ir_{6}} L^{j_{6}k_{6}} \bar\varphi_{k_{6}} (\not{\mathcal D}L_{r_{6}j_{6}}) \gamma^{q_{7}} (\mathcal D_{q_{7}}L) L_{ij_{7}} \chi^{j_{7}}\qquad\text{(2.84; G3)}
\end{aligned}
\tag{91}
```

```math
\begin{aligned}
&- \frac{16 i}{L^{4}} \varepsilon^{ir_{6}} L^{j_{6}k_{6}} \bar\varphi_{k_{6}} (\not{\mathcal D}L_{r_{6}j_{6}}) \gamma^{q_{7}} \mathcal D_{q_{7}}\!\left(L_{ij_{7}}\right) \chi^{j_{7}}\qquad\text{(2.85; G3)}\\
&- \frac{16 i}{L^{4}} \varepsilon^{ir_{6}} L^{j_{6}k_{6}} \bar\varphi_{k_{6}} (\not{\mathcal D}L_{r_{6}j_{6}}) \gamma^{q_{7}} L_{ij_{7}} \mathcal D_{q_{7}}\!\left(\chi^{j_{7}}\right)\qquad\text{(2.86; G3)}\\
&+\frac{4 i}{L^{5}} \varepsilon^{ir_{6}} L^{j_{6}k_{6}} \bar\varphi_{k_{6}} (\not{\mathcal D}L_{r_{6}j_{6}}) \gamma^{q_{7}} (\mathcal D_{q_{7}}L) \gamma\!\cdot\!T \varphi_{i}\qquad\text{(2.87; G3)}\\
&- \frac{4 i}{L^{4}} \varepsilon^{ir_{6}} L^{j_{6}k_{6}} \bar\varphi_{k_{6}} (\not{\mathcal D}L_{r_{6}j_{6}}) \gamma^{q_{7}} \gamma\!\cdot\!T \mathcal D_{q_{7}}\!\left(\varphi_{i}\right)\qquad\text{(2.88; G3)}
\end{aligned}
\tag{92}
```

```math
\begin{aligned}
&- \frac{6 i N}{L^{7}} \varepsilon^{ir_{6}} L^{j_{6}k_{6}} \bar\varphi_{k_{6}} (\not{\mathcal D}L_{r_{6}j_{6}}) \gamma^{q_{7}} (\mathcal D_{q_{7}}L) L_{ij_{7}} \varphi^{j_{7}}\qquad\text{(2.89; G3)}\\
&+\frac{2 i}{L^{6}} \varepsilon^{ir_{6}} L^{j_{6}k_{6}} \bar\varphi_{k_{6}} (\not{\mathcal D}L_{r_{6}j_{6}}) \gamma^{q_{7}} (\mathcal D_{q_{7}}N) L_{ij_{7}} \varphi^{j_{7}}\qquad\text{(2.90; G3)}\\
&+\frac{2 i N}{L^{6}} \varepsilon^{ir_{6}} L^{j_{6}k_{6}} \bar\varphi_{k_{6}} (\not{\mathcal D}L_{r_{6}j_{6}}) \gamma^{q_{7}} \mathcal D_{q_{7}}\!\left(L_{ij_{7}}\right) \varphi^{j_{7}}\qquad\text{(2.91; G3)}\\
&+\frac{2 i N}{L^{6}} \varepsilon^{ir_{6}} L^{j_{6}k_{6}} \bar\varphi_{k_{6}} (\not{\mathcal D}L_{r_{6}j_{6}}) \gamma^{q_{7}} L_{ij_{7}} \mathcal D_{q_{7}}\!\left(\varphi^{j_{7}}\right)\qquad\text{(2.92; G3)}
\end{aligned}
\tag{93}
```

```math
\begin{aligned}
&- \frac{6}{L^{7}} \varepsilon^{ir_{6}} L^{j_{6}k_{6}} \bar\varphi_{k_{6}} (\not{\mathcal D}L_{r_{6}j_{6}}) \gamma^{q_{7}} (\mathcal D_{q_{7}}L) (\not{\mathcal D}L_{ij_{7}}) L^{j_{7}k_{7}} \varphi_{k_{7}}\qquad\text{(2.93; G3)}\\
&+\frac{2}{L^{6}} \varepsilon^{ir_{6}} L^{j_{6}k_{6}} \bar\varphi_{k_{6}} (\not{\mathcal D}L_{r_{6}j_{6}}) \gamma^{q_{7}} \mathcal D_{q_{7}}\!\left((\not{\mathcal D}L_{ij_{7}})\right) L^{j_{7}k_{7}} \varphi_{k_{7}}\qquad\text{(2.94; G3)}\\
&+\frac{2}{L^{6}} \varepsilon^{ir_{6}} L^{j_{6}k_{6}} \bar\varphi_{k_{6}} (\not{\mathcal D}L_{r_{6}j_{6}}) \gamma^{q_{7}} (\not{\mathcal D}L_{ij_{7}}) \mathcal D_{q_{7}}\!\left(L^{j_{7}k_{7}}\right) \varphi_{k_{7}}\qquad\text{(2.95; G3)}\\
&+\frac{2}{L^{6}} \varepsilon^{ir_{6}} L^{j_{6}k_{6}} \bar\varphi_{k_{6}} (\not{\mathcal D}L_{r_{6}j_{6}}) \gamma^{q_{7}} (\not{\mathcal D}L_{ij_{7}}) L^{j_{7}k_{7}} \mathcal D_{q_{7}}\!\left(\varphi_{k_{7}}\right)\qquad\text{(2.96; G3)}
\end{aligned}
\tag{94}
```

```math
\begin{aligned}
&+\frac{6}{L^{7}} \varepsilon^{ir_{6}} L^{j_{6}k_{6}} \bar\varphi_{k_{6}} (\not{\mathcal D}L_{r_{6}j_{6}}) \gamma^{q_{7}} (\mathcal D_{q_{7}}L) \not E L_{ij_{7}} \varphi^{j_{7}}\qquad\text{(2.97; G3)}\\
&- \frac{2}{L^{6}} \varepsilon^{ir_{6}} L^{j_{6}k_{6}} \bar\varphi_{k_{6}} (\not{\mathcal D}L_{r_{6}j_{6}}) \gamma^{q_{7}} \mathcal D_{q_{7}}\!\left(\not E\right) L_{ij_{7}} \varphi^{j_{7}}\qquad\text{(2.98; G3)}\\
&- \frac{2}{L^{6}} \varepsilon^{ir_{6}} L^{j_{6}k_{6}} \bar\varphi_{k_{6}} (\not{\mathcal D}L_{r_{6}j_{6}}) \gamma^{q_{7}} \not E \mathcal D_{q_{7}}\!\left(L_{ij_{7}}\right) \varphi^{j_{7}}\qquad\text{(2.99; G3)}\\
&- \frac{2}{L^{6}} \varepsilon^{ir_{6}} L^{j_{6}k_{6}} \bar\varphi_{k_{6}} (\not{\mathcal D}L_{r_{6}j_{6}}) \gamma^{q_{7}} \not E L_{ij_{7}} \mathcal D_{q_{7}}\!\left(\varphi^{j_{7}}\right)\qquad\text{(2.100; G3)}
\end{aligned}
\tag{95}
```

```math
\begin{aligned}
&- \frac{4 i}{L^{4}} \varepsilon^{ir_{6}} L^{j_{6}k_{6}} \bar\varphi_{k_{6}} (\not{\mathcal D}L_{r_{6}j_{6}}) \gamma^{q_{7}} \gamma^{mn}(\mathcal D_{q_{7}}T_{mn}) \varphi_{i}\qquad\text{(2.101; G3)}\\
&- \frac{2}{L^{5}} \varepsilon^{ir_{6}} L_{r_{6}j_{6}} \bar\varphi^{j_{6}} \not E \gamma^{q_{7}} (\mathcal D_{q_{7}}L) \not{\mathcal D}\varphi_{i}\qquad\text{(2.102; G3)}\\
&+\frac{2}{L^{4}} \varepsilon^{ir_{6}} L_{r_{6}j_{6}} \bar\varphi^{j_{6}} \not E \gamma^{q_{7}} \mathcal D_{q_{7}}\!\left(\not{\mathcal D}\varphi_{i}\right)\qquad\text{(2.103; G3)}\\
&- \frac{16 i}{L^{5}} \varepsilon^{ir_{6}} L_{r_{6}j_{6}} \bar\varphi^{j_{6}} \not E \gamma^{q_{7}} (\mathcal D_{q_{7}}L) L_{ij_{7}} \chi^{j_{7}}\qquad\text{(2.104; G3)}
\end{aligned}
\tag{96}
```

```math
\begin{aligned}
&+\frac{16 i}{L^{4}} \varepsilon^{ir_{6}} L_{r_{6}j_{6}} \bar\varphi^{j_{6}} \not E \gamma^{q_{7}} \mathcal D_{q_{7}}\!\left(L_{ij_{7}}\right) \chi^{j_{7}}\qquad\text{(2.105; G3)}\\
&+\frac{16 i}{L^{4}} \varepsilon^{ir_{6}} L_{r_{6}j_{6}} \bar\varphi^{j_{6}} \not E \gamma^{q_{7}} L_{ij_{7}} \mathcal D_{q_{7}}\!\left(\chi^{j_{7}}\right)\qquad\text{(2.106; G3)}\\
&- \frac{4 i}{L^{5}} \varepsilon^{ir_{6}} L_{r_{6}j_{6}} \bar\varphi^{j_{6}} \not E \gamma^{q_{7}} (\mathcal D_{q_{7}}L) \gamma\!\cdot\!T \varphi_{i}\qquad\text{(2.107; G3)}\\
&+\frac{4 i}{L^{4}} \varepsilon^{ir_{6}} L_{r_{6}j_{6}} \bar\varphi^{j_{6}} \not E \gamma^{q_{7}} \gamma\!\cdot\!T \mathcal D_{q_{7}}\!\left(\varphi_{i}\right)\qquad\text{(2.108; G3)}
\end{aligned}
\tag{97}
```

```math
\begin{aligned}
&+\frac{6 i N}{L^{7}} \varepsilon^{ir_{6}} L_{r_{6}j_{6}} \bar\varphi^{j_{6}} \not E \gamma^{q_{7}} (\mathcal D_{q_{7}}L) L_{ij_{7}} \varphi^{j_{7}}\qquad\text{(2.109; G3)}\\
&- \frac{2 i}{L^{6}} \varepsilon^{ir_{6}} L_{r_{6}j_{6}} \bar\varphi^{j_{6}} \not E \gamma^{q_{7}} (\mathcal D_{q_{7}}N) L_{ij_{7}} \varphi^{j_{7}}\qquad\text{(2.110; G3)}\\
&- \frac{2 i N}{L^{6}} \varepsilon^{ir_{6}} L_{r_{6}j_{6}} \bar\varphi^{j_{6}} \not E \gamma^{q_{7}} \mathcal D_{q_{7}}\!\left(L_{ij_{7}}\right) \varphi^{j_{7}}\qquad\text{(2.111; G3)}\\
&- \frac{2 i N}{L^{6}} \varepsilon^{ir_{6}} L_{r_{6}j_{6}} \bar\varphi^{j_{6}} \not E \gamma^{q_{7}} L_{ij_{7}} \mathcal D_{q_{7}}\!\left(\varphi^{j_{7}}\right)\qquad\text{(2.112; G3)}
\end{aligned}
\tag{98}
```

```math
\begin{aligned}
&+\frac{6}{L^{7}} \varepsilon^{ir_{6}} L_{r_{6}j_{6}} \bar\varphi^{j_{6}} \not E \gamma^{q_{7}} (\mathcal D_{q_{7}}L) (\not{\mathcal D}L_{ij_{7}}) L^{j_{7}k_{7}} \varphi_{k_{7}}\qquad\text{(2.113; G3)}\\
&- \frac{2}{L^{6}} \varepsilon^{ir_{6}} L_{r_{6}j_{6}} \bar\varphi^{j_{6}} \not E \gamma^{q_{7}} \mathcal D_{q_{7}}\!\left((\not{\mathcal D}L_{ij_{7}})\right) L^{j_{7}k_{7}} \varphi_{k_{7}}\qquad\text{(2.114; G3)}\\
&- \frac{2}{L^{6}} \varepsilon^{ir_{6}} L_{r_{6}j_{6}} \bar\varphi^{j_{6}} \not E \gamma^{q_{7}} (\not{\mathcal D}L_{ij_{7}}) \mathcal D_{q_{7}}\!\left(L^{j_{7}k_{7}}\right) \varphi_{k_{7}}\qquad\text{(2.115; G3)}\\
&- \frac{2}{L^{6}} \varepsilon^{ir_{6}} L_{r_{6}j_{6}} \bar\varphi^{j_{6}} \not E \gamma^{q_{7}} (\not{\mathcal D}L_{ij_{7}}) L^{j_{7}k_{7}} \mathcal D_{q_{7}}\!\left(\varphi_{k_{7}}\right)\qquad\text{(2.116; G3)}
\end{aligned}
\tag{99}
```

```math
\begin{aligned}
&- \frac{6}{L^{7}} \varepsilon^{ir_{6}} L_{r_{6}j_{6}} \bar\varphi^{j_{6}} \not E \gamma^{q_{7}} (\mathcal D_{q_{7}}L) \not E L_{ij_{7}} \varphi^{j_{7}}\qquad\text{(2.117; G3)}\\
&+\frac{2}{L^{6}} \varepsilon^{ir_{6}} L_{r_{6}j_{6}} \bar\varphi^{j_{6}} \not E \gamma^{q_{7}} \mathcal D_{q_{7}}\!\left(\not E\right) L_{ij_{7}} \varphi^{j_{7}}\qquad\text{(2.118; G3)}\\
&+\frac{2}{L^{6}} \varepsilon^{ir_{6}} L_{r_{6}j_{6}} \bar\varphi^{j_{6}} \not E \gamma^{q_{7}} \not E \mathcal D_{q_{7}}\!\left(L_{ij_{7}}\right) \varphi^{j_{7}}\qquad\text{(2.119; G3)}\\
&+\frac{2}{L^{6}} \varepsilon^{ir_{6}} L_{r_{6}j_{6}} \bar\varphi^{j_{6}} \not E \gamma^{q_{7}} \not E L_{ij_{7}} \mathcal D_{q_{7}}\!\left(\varphi^{j_{7}}\right)\qquad\text{(2.120; G3)}
\end{aligned}
\tag{100}
```

```math
\begin{aligned}
&+\frac{4 i}{L^{4}} \varepsilon^{ir_{6}} L_{r_{6}j_{6}} \bar\varphi^{j_{6}} \not E \gamma^{q_{7}} \gamma^{mn}(\mathcal D_{q_{7}}T_{mn}) \varphi_{i}\qquad\text{(2.121; G3)}\\
&- \frac{4 i}{L^{2}} \varepsilon^{ir_{8}} (\mathcal D_{d_{8}}\bar\varphi_{r_{8}}) \gamma^{d_{8}} \gamma\cdot T \not{\mathcal D}\varphi_{i}\qquad\text{(2.122; G4)}\\
&+\frac{32}{L^{2}} \varepsilon^{ir_{8}} (\mathcal D_{d_{8}}\bar\varphi_{r_{8}}) \gamma^{d_{8}} \gamma\cdot T L_{ij_{10}} \chi^{j_{10}}\qquad\text{(2.123; G4)}\\
&+\frac{8}{L^{2}} \varepsilon^{ir_{8}} (\mathcal D_{d_{8}}\bar\varphi_{r_{8}}) \gamma^{d_{8}} \gamma\cdot T \gamma\!\cdot\!T \varphi_{i}\qquad\text{(2.124; G4)}
\end{aligned}
\tag{101}
```

```math
\begin{aligned}
&- \frac{4 N}{L^{4}} \varepsilon^{ir_{8}} (\mathcal D_{d_{8}}\bar\varphi_{r_{8}}) \gamma^{d_{8}} \gamma\cdot T L_{ij_{10}} \varphi^{j_{10}}\qquad\text{(2.125; G4)}\\
&+\frac{4 i}{L^{4}} \varepsilon^{ir_{8}} (\mathcal D_{d_{8}}\bar\varphi_{r_{8}}) \gamma^{d_{8}} \gamma\cdot T (\not{\mathcal D}L_{ij_{10}}) L^{j_{10}k_{10}} \varphi_{k_{10}}\qquad\text{(2.126; G4)}\\
&- \frac{4 i}{L^{4}} \varepsilon^{ir_{8}} (\mathcal D_{d_{8}}\bar\varphi_{r_{8}}) \gamma^{d_{8}} \gamma\cdot T \not E L_{ij_{10}} \varphi^{j_{10}}\qquad\text{(2.127; G4)}\\
&+\frac{32}{L^{2}} \varepsilon^{ir_{8}} L_{r_{8}j_{8}} \bar\chi^{j_{8}} \gamma\cdot T \not{\mathcal D}\varphi_{i}\qquad\text{(2.128; G4)}
\end{aligned}
\tag{102}
```

```math
\begin{aligned}
&+\frac{256 i}{L^{2}} \varepsilon^{ir_{8}} L_{r_{8}j_{8}} \bar\chi^{j_{8}} \gamma\cdot T L_{ij_{10}} \chi^{j_{10}}\qquad\text{(2.129; G4)}\\
&+\frac{64 i}{L^{2}} \varepsilon^{ir_{8}} L_{r_{8}j_{8}} \bar\chi^{j_{8}} \gamma\cdot T \gamma\!\cdot\!T \varphi_{i}\qquad\text{(2.130; G4)}\\
&- \frac{32 i N}{L^{4}} \varepsilon^{ir_{8}} L_{r_{8}j_{8}} \bar\chi^{j_{8}} \gamma\cdot T L_{ij_{10}} \varphi^{j_{10}}\qquad\text{(2.131; G4)}\\
&- \frac{32}{L^{4}} \varepsilon^{ir_{8}} L_{r_{8}j_{8}} \bar\chi^{j_{8}} \gamma\cdot T (\not{\mathcal D}L_{ij_{10}}) L^{j_{10}k_{10}} \varphi_{k_{10}}\qquad\text{(2.132; G4)}
\end{aligned}
\tag{103}
```

```math
\begin{aligned}
&+\frac{32}{L^{4}} \varepsilon^{ir_{8}} L_{r_{8}j_{8}} \bar\chi^{j_{8}} \gamma\cdot T \not E L_{ij_{10}} \varphi^{j_{10}}\qquad\text{(2.133; G4)}\\
&- \frac{8}{L^{2}} \varepsilon^{ir_{8}} \bar\varphi_{r_{8}} \gamma\!\cdot\!T \gamma\cdot T \not{\mathcal D}\varphi_{i}\qquad\text{(2.134; G4)}\\
&- \frac{64 i}{L^{2}} \varepsilon^{ir_{8}} \bar\varphi_{r_{8}} \gamma\!\cdot\!T \gamma\cdot T L_{ij_{10}} \chi^{j_{10}}\qquad\text{(2.135; G4)}\\
&- \frac{16 i}{L^{2}} \varepsilon^{ir_{8}} \bar\varphi_{r_{8}} \gamma\!\cdot\!T \gamma\cdot T \gamma\!\cdot\!T \varphi_{i}\qquad\text{(2.136; G4)}
\end{aligned}
\tag{104}
```

```math
\begin{aligned}
&+\frac{8 i N}{L^{4}} \varepsilon^{ir_{8}} \bar\varphi_{r_{8}} \gamma\!\cdot\!T \gamma\cdot T L_{ij_{10}} \varphi^{j_{10}}\qquad\text{(2.137; G4)}\\
&+\frac{8}{L^{4}} \varepsilon^{ir_{8}} \bar\varphi_{r_{8}} \gamma\!\cdot\!T \gamma\cdot T (\not{\mathcal D}L_{ij_{10}}) L^{j_{10}k_{10}} \varphi_{k_{10}}\qquad\text{(2.138; G4)}\\
&- \frac{8}{L^{4}} \varepsilon^{ir_{8}} \bar\varphi_{r_{8}} \gamma\!\cdot\!T \gamma\cdot T \not E L_{ij_{10}} \varphi^{j_{10}}\qquad\text{(2.139; G4)}\\
&- \frac{4 N}{L^{4}} \varepsilon^{ir_{8}} L_{r_{8}j_{8}} \bar\varphi^{j_{8}} \gamma\cdot T \not{\mathcal D}\varphi_{i}\qquad\text{(2.140; G4)}
\end{aligned}
\tag{105}
```

```math
\begin{aligned}
&- \frac{32 i N}{L^{4}} \varepsilon^{ir_{8}} L_{r_{8}j_{8}} \bar\varphi^{j_{8}} \gamma\cdot T L_{ij_{10}} \chi^{j_{10}}\qquad\text{(2.141; G4)}\\
&- \frac{8 i N}{L^{4}} \varepsilon^{ir_{8}} L_{r_{8}j_{8}} \bar\varphi^{j_{8}} \gamma\cdot T \gamma\!\cdot\!T \varphi_{i}\qquad\text{(2.142; G4)}\\
&+\frac{4 i N^{2}}{L^{6}} \varepsilon^{ir_{8}} L_{r_{8}j_{8}} \bar\varphi^{j_{8}} \gamma\cdot T L_{ij_{10}} \varphi^{j_{10}}\qquad\text{(2.143; G4)}\\
&+\frac{4 N}{L^{6}} \varepsilon^{ir_{8}} L_{r_{8}j_{8}} \bar\varphi^{j_{8}} \gamma\cdot T (\not{\mathcal D}L_{ij_{10}}) L^{j_{10}k_{10}} \varphi_{k_{10}}\qquad\text{(2.144; G4)}
\end{aligned}
\tag{106}
```

```math
\begin{aligned}
&- \frac{4 N}{L^{6}} \varepsilon^{ir_{8}} L_{r_{8}j_{8}} \bar\varphi^{j_{8}} \gamma\cdot T \not E L_{ij_{10}} \varphi^{j_{10}}\qquad\text{(2.145; G4)}\\
&+\frac{4 i}{L^{4}} \varepsilon^{ir_{8}} L^{j_{8}k_{8}} \bar\varphi_{k_{8}} (\not{\mathcal D}L_{r_{8}j_{8}}) \gamma\cdot T \not{\mathcal D}\varphi_{i}\qquad\text{(2.146; G4)}\\
&- \frac{32}{L^{4}} \varepsilon^{ir_{8}} L^{j_{8}k_{8}} \bar\varphi_{k_{8}} (\not{\mathcal D}L_{r_{8}j_{8}}) \gamma\cdot T L_{ij_{10}} \chi^{j_{10}}\qquad\text{(2.147; G4)}\\
&- \frac{8}{L^{4}} \varepsilon^{ir_{8}} L^{j_{8}k_{8}} \bar\varphi_{k_{8}} (\not{\mathcal D}L_{r_{8}j_{8}}) \gamma\cdot T \gamma\!\cdot\!T \varphi_{i}\qquad\text{(2.148; G4)}
\end{aligned}
\tag{107}
```

```math
\begin{aligned}
&+\frac{4 N}{L^{6}} \varepsilon^{ir_{8}} L^{j_{8}k_{8}} \bar\varphi_{k_{8}} (\not{\mathcal D}L_{r_{8}j_{8}}) \gamma\cdot T L_{ij_{10}} \varphi^{j_{10}}\qquad\text{(2.149; G4)}\\
&- \frac{4 i}{L^{6}} \varepsilon^{ir_{8}} L^{j_{8}k_{8}} \bar\varphi_{k_{8}} (\not{\mathcal D}L_{r_{8}j_{8}}) \gamma\cdot T (\not{\mathcal D}L_{ij_{10}}) L^{j_{10}k_{10}} \varphi_{k_{10}}\qquad\text{(2.150; G4)}\\
&+\frac{4 i}{L^{6}} \varepsilon^{ir_{8}} L^{j_{8}k_{8}} \bar\varphi_{k_{8}} (\not{\mathcal D}L_{r_{8}j_{8}}) \gamma\cdot T \not E L_{ij_{10}} \varphi^{j_{10}}\qquad\text{(2.151; G4)}\\
&- \frac{4 i}{L^{4}} \varepsilon^{ir_{8}} L_{r_{8}j_{8}} \bar\varphi^{j_{8}} \not E \gamma\cdot T \not{\mathcal D}\varphi_{i}\qquad\text{(2.152; G4)}
\end{aligned}
\tag{108}
```

```math
\begin{aligned}
&+\frac{32}{L^{4}} \varepsilon^{ir_{8}} L_{r_{8}j_{8}} \bar\varphi^{j_{8}} \not E \gamma\cdot T L_{ij_{10}} \chi^{j_{10}}\qquad\text{(2.153; G4)}\\
&+\frac{8}{L^{4}} \varepsilon^{ir_{8}} L_{r_{8}j_{8}} \bar\varphi^{j_{8}} \not E \gamma\cdot T \gamma\!\cdot\!T \varphi_{i}\qquad\text{(2.154; G4)}\\
&- \frac{4 N}{L^{6}} \varepsilon^{ir_{8}} L_{r_{8}j_{8}} \bar\varphi^{j_{8}} \not E \gamma\cdot T L_{ij_{10}} \varphi^{j_{10}}\qquad\text{(2.155; G4)}\\
&+\frac{4 i}{L^{6}} \varepsilon^{ir_{8}} L_{r_{8}j_{8}} \bar\varphi^{j_{8}} \not E \gamma\cdot T (\not{\mathcal D}L_{ij_{10}}) L^{j_{10}k_{10}} \varphi_{k_{10}}\qquad\text{(2.156; G4)}
\end{aligned}
\tag{109}
```

```math
\begin{aligned}
&- \frac{4 i}{L^{6}} \varepsilon^{ir_{8}} L_{r_{8}j_{8}} \bar\varphi^{j_{8}} \not E \gamma\cdot T \not E L_{ij_{10}} \varphi^{j_{10}}\qquad\text{(2.157; G4)}\\
&- \frac{32 N}{L^{2}} \varepsilon^{ir_{12}} (\mathcal D_{d_{12}}\bar\varphi_{r_{12}}) \gamma^{d_{12}} \chi_i\qquad\text{(2.158; G5)}\\
&- \frac{256 i N}{L^{2}} \varepsilon^{ir_{12}} L_{r_{12}j_{12}} \bar\chi^{j_{12}} \chi_i\qquad\text{(2.159; G5)}\\
&+\frac{64 i N}{L^{2}} \varepsilon^{ir_{12}} \bar\varphi_{r_{12}} \gamma\!\cdot\!T \chi_i\qquad\text{(2.160; G5)}
\end{aligned}
\tag{110}
```

```math
\begin{aligned}
&+\frac{32 i N^{2}}{L^{4}} \varepsilon^{ir_{12}} L_{r_{12}j_{12}} \bar\varphi^{j_{12}} \chi_i\qquad\text{(2.161; G5)}\\
&+\frac{32 N}{L^{4}} \varepsilon^{ir_{12}} L^{j_{12}k_{12}} \bar\varphi_{k_{12}} (\not{\mathcal D}L_{r_{12}j_{12}}) \chi_i\qquad\text{(2.162; G5)}\\
&- \frac{32 N}{L^{4}} \varepsilon^{ir_{12}} L_{r_{12}j_{12}} \bar\varphi^{j_{12}} \not E \chi_i\qquad\text{(2.163; G5)}\\
&+\frac{i}{2 L^{2}} \varepsilon^{ir_{14}} (\mathcal D_{d_{14}}\bar\varphi_{r_{14}}) \gamma^{d_{14}} \gamma\cdot\widehat G \not{\mathcal D}\varphi_{i}\qquad\text{(2.164; G6)}
\end{aligned}
\tag{111}
```

```math
\begin{aligned}
&- \frac{4}{L^{2}} \varepsilon^{ir_{14}} (\mathcal D_{d_{14}}\bar\varphi_{r_{14}}) \gamma^{d_{14}} \gamma\cdot\widehat G L_{ij_{16}} \chi^{j_{16}}\qquad\text{(2.165; G6)}\\
&- \frac{1}{L^{2}} \varepsilon^{ir_{14}} (\mathcal D_{d_{14}}\bar\varphi_{r_{14}}) \gamma^{d_{14}} \gamma\cdot\widehat G \gamma\!\cdot\!T \varphi_{i}\qquad\text{(2.166; G6)}\\
&+\frac{N}{2 L^{4}} \varepsilon^{ir_{14}} (\mathcal D_{d_{14}}\bar\varphi_{r_{14}}) \gamma^{d_{14}} \gamma\cdot\widehat G L_{ij_{16}} \varphi^{j_{16}}\qquad\text{(2.167; G6)}\\
&- \frac{i}{2 L^{4}} \varepsilon^{ir_{14}} (\mathcal D_{d_{14}}\bar\varphi_{r_{14}}) \gamma^{d_{14}} \gamma\cdot\widehat G (\not{\mathcal D}L_{ij_{16}}) L^{j_{16}k_{16}} \varphi_{k_{16}}\qquad\text{(2.168; G6)}
\end{aligned}
\tag{112}
```

```math
\begin{aligned}
&+\frac{i}{2 L^{4}} \varepsilon^{ir_{14}} (\mathcal D_{d_{14}}\bar\varphi_{r_{14}}) \gamma^{d_{14}} \gamma\cdot\widehat G \not E L_{ij_{16}} \varphi^{j_{16}}\qquad\text{(2.169; G6)}\\
&- \frac{4}{L^{2}} \varepsilon^{ir_{14}} L_{r_{14}j_{14}} \bar\chi^{j_{14}} \gamma\cdot\widehat G \not{\mathcal D}\varphi_{i}\qquad\text{(2.170; G6)}\\
&- \frac{32 i}{L^{2}} \varepsilon^{ir_{14}} L_{r_{14}j_{14}} \bar\chi^{j_{14}} \gamma\cdot\widehat G L_{ij_{16}} \chi^{j_{16}}\qquad\text{(2.171; G6)}\\
&- \frac{8 i}{L^{2}} \varepsilon^{ir_{14}} L_{r_{14}j_{14}} \bar\chi^{j_{14}} \gamma\cdot\widehat G \gamma\!\cdot\!T \varphi_{i}\qquad\text{(2.172; G6)}
\end{aligned}
\tag{113}
```

```math
\begin{aligned}
&+\frac{4 i N}{L^{4}} \varepsilon^{ir_{14}} L_{r_{14}j_{14}} \bar\chi^{j_{14}} \gamma\cdot\widehat G L_{ij_{16}} \varphi^{j_{16}}\qquad\text{(2.173; G6)}\\
&+\frac{4}{L^{4}} \varepsilon^{ir_{14}} L_{r_{14}j_{14}} \bar\chi^{j_{14}} \gamma\cdot\widehat G (\not{\mathcal D}L_{ij_{16}}) L^{j_{16}k_{16}} \varphi_{k_{16}}\qquad\text{(2.174; G6)}\\
&- \frac{4}{L^{4}} \varepsilon^{ir_{14}} L_{r_{14}j_{14}} \bar\chi^{j_{14}} \gamma\cdot\widehat G \not E L_{ij_{16}} \varphi^{j_{16}}\qquad\text{(2.175; G6)}\\
&+\frac{1}{L^{2}} \varepsilon^{ir_{14}} \bar\varphi_{r_{14}} \gamma\!\cdot\!T \gamma\cdot\widehat G \not{\mathcal D}\varphi_{i}\qquad\text{(2.176; G6)}
\end{aligned}
\tag{114}
```

```math
\begin{aligned}
&+\frac{8 i}{L^{2}} \varepsilon^{ir_{14}} \bar\varphi_{r_{14}} \gamma\!\cdot\!T \gamma\cdot\widehat G L_{ij_{16}} \chi^{j_{16}}\qquad\text{(2.177; G6)}\\
&+\frac{2 i}{L^{2}} \varepsilon^{ir_{14}} \bar\varphi_{r_{14}} \gamma\!\cdot\!T \gamma\cdot\widehat G \gamma\!\cdot\!T \varphi_{i}\qquad\text{(2.178; G6)}\\
&- \frac{i N}{L^{4}} \varepsilon^{ir_{14}} \bar\varphi_{r_{14}} \gamma\!\cdot\!T \gamma\cdot\widehat G L_{ij_{16}} \varphi^{j_{16}}\qquad\text{(2.179; G6)}\\
&- \frac{1}{L^{4}} \varepsilon^{ir_{14}} \bar\varphi_{r_{14}} \gamma\!\cdot\!T \gamma\cdot\widehat G (\not{\mathcal D}L_{ij_{16}}) L^{j_{16}k_{16}} \varphi_{k_{16}}\qquad\text{(2.180; G6)}
\end{aligned}
\tag{115}
```

```math
\begin{aligned}
&+\frac{1}{L^{4}} \varepsilon^{ir_{14}} \bar\varphi_{r_{14}} \gamma\!\cdot\!T \gamma\cdot\widehat G \not E L_{ij_{16}} \varphi^{j_{16}}\qquad\text{(2.181; G6)}\\
&+\frac{N}{2 L^{4}} \varepsilon^{ir_{14}} L_{r_{14}j_{14}} \bar\varphi^{j_{14}} \gamma\cdot\widehat G \not{\mathcal D}\varphi_{i}\qquad\text{(2.182; G6)}\\
&+\frac{4 i N}{L^{4}} \varepsilon^{ir_{14}} L_{r_{14}j_{14}} \bar\varphi^{j_{14}} \gamma\cdot\widehat G L_{ij_{16}} \chi^{j_{16}}\qquad\text{(2.183; G6)}\\
&+\frac{i N}{L^{4}} \varepsilon^{ir_{14}} L_{r_{14}j_{14}} \bar\varphi^{j_{14}} \gamma\cdot\widehat G \gamma\!\cdot\!T \varphi_{i}\qquad\text{(2.184; G6)}
\end{aligned}
\tag{116}
```

```math
\begin{aligned}
&- \frac{i N^{2}}{2 L^{6}} \varepsilon^{ir_{14}} L_{r_{14}j_{14}} \bar\varphi^{j_{14}} \gamma\cdot\widehat G L_{ij_{16}} \varphi^{j_{16}}\qquad\text{(2.185; G6)}\\
&- \frac{N}{2 L^{6}} \varepsilon^{ir_{14}} L_{r_{14}j_{14}} \bar\varphi^{j_{14}} \gamma\cdot\widehat G (\not{\mathcal D}L_{ij_{16}}) L^{j_{16}k_{16}} \varphi_{k_{16}}\qquad\text{(2.186; G6)}\\
&+\frac{N}{2 L^{6}} \varepsilon^{ir_{14}} L_{r_{14}j_{14}} \bar\varphi^{j_{14}} \gamma\cdot\widehat G \not E L_{ij_{16}} \varphi^{j_{16}}\qquad\text{(2.187; G6)}\\
&- \frac{i}{2 L^{4}} \varepsilon^{ir_{14}} L^{j_{14}k_{14}} \bar\varphi_{k_{14}} (\not{\mathcal D}L_{r_{14}j_{14}}) \gamma\cdot\widehat G \not{\mathcal D}\varphi_{i}\qquad\text{(2.188; G6)}
\end{aligned}
\tag{117}
```

```math
\begin{aligned}
&+\frac{4}{L^{4}} \varepsilon^{ir_{14}} L^{j_{14}k_{14}} \bar\varphi_{k_{14}} (\not{\mathcal D}L_{r_{14}j_{14}}) \gamma\cdot\widehat G L_{ij_{16}} \chi^{j_{16}}\qquad\text{(2.189; G6)}\\
&+\frac{1}{L^{4}} \varepsilon^{ir_{14}} L^{j_{14}k_{14}} \bar\varphi_{k_{14}} (\not{\mathcal D}L_{r_{14}j_{14}}) \gamma\cdot\widehat G \gamma\!\cdot\!T \varphi_{i}\qquad\text{(2.190; G6)}\\
&- \frac{N}{2 L^{6}} \varepsilon^{ir_{14}} L^{j_{14}k_{14}} \bar\varphi_{k_{14}} (\not{\mathcal D}L_{r_{14}j_{14}}) \gamma\cdot\widehat G L_{ij_{16}} \varphi^{j_{16}}\qquad\text{(2.191; G6)}\\
&+\frac{i}{2 L^{6}} \varepsilon^{ir_{14}} L^{j_{14}k_{14}} \bar\varphi_{k_{14}} (\not{\mathcal D}L_{r_{14}j_{14}}) \gamma\cdot\widehat G (\not{\mathcal D}L_{ij_{16}}) L^{j_{16}k_{16}} \varphi_{k_{16}}\qquad\text{(2.192; G6)}
\end{aligned}
\tag{118}
```

```math
\begin{aligned}
&- \frac{i}{2 L^{6}} \varepsilon^{ir_{14}} L^{j_{14}k_{14}} \bar\varphi_{k_{14}} (\not{\mathcal D}L_{r_{14}j_{14}}) \gamma\cdot\widehat G \not E L_{ij_{16}} \varphi^{j_{16}}\qquad\text{(2.193; G6)}\\
&+\frac{i}{2 L^{4}} \varepsilon^{ir_{14}} L_{r_{14}j_{14}} \bar\varphi^{j_{14}} \not E \gamma\cdot\widehat G \not{\mathcal D}\varphi_{i}\qquad\text{(2.194; G6)}\\
&- \frac{4}{L^{4}} \varepsilon^{ir_{14}} L_{r_{14}j_{14}} \bar\varphi^{j_{14}} \not E \gamma\cdot\widehat G L_{ij_{16}} \chi^{j_{16}}\qquad\text{(2.195; G6)}\\
&- \frac{1}{L^{4}} \varepsilon^{ir_{14}} L_{r_{14}j_{14}} \bar\varphi^{j_{14}} \not E \gamma\cdot\widehat G \gamma\!\cdot\!T \varphi_{i}\qquad\text{(2.196; G6)}
\end{aligned}
\tag{119}
```

```math
\begin{aligned}
&+\frac{N}{2 L^{6}} \varepsilon^{ir_{14}} L_{r_{14}j_{14}} \bar\varphi^{j_{14}} \not E \gamma\cdot\widehat G L_{ij_{16}} \varphi^{j_{16}}\qquad\text{(2.197; G6)}\\
&- \frac{i}{2 L^{6}} \varepsilon^{ir_{14}} L_{r_{14}j_{14}} \bar\varphi^{j_{14}} \not E \gamma\cdot\widehat G (\not{\mathcal D}L_{ij_{16}}) L^{j_{16}k_{16}} \varphi_{k_{16}}\qquad\text{(2.198; G6)}\\
&+\frac{i}{2 L^{6}} \varepsilon^{ir_{14}} L_{r_{14}j_{14}} \bar\varphi^{j_{14}} \not E \gamma\cdot\widehat G \not E L_{ij_{16}} \varphi^{j_{16}}\qquad\text{(2.199; G6)}\\
&- \frac{i g}{L^{2}} \varepsilon^{ir_{17}} (\mathcal D_{d_{17}}\bar\varphi_{r_{17}}) \gamma^{d_{17}} L_{ij} \varepsilon^{jr_{19}} \not{\mathcal D}\varphi_{r_{19}}\qquad\text{(2.200; G7)}
\end{aligned}
\tag{120}
```

```math
\begin{aligned}
&+\frac{8 g}{L^{2}} \varepsilon^{ir_{17}} (\mathcal D_{d_{17}}\bar\varphi_{r_{17}}) \gamma^{d_{17}} L_{ij} \varepsilon^{jr_{19}} L_{r_{19}j_{19}} \chi^{j_{19}}\qquad\text{(2.201; G7)}\\
&+\frac{2 g}{L^{2}} \varepsilon^{ir_{17}} (\mathcal D_{d_{17}}\bar\varphi_{r_{17}}) \gamma^{d_{17}} L_{ij} \varepsilon^{jr_{19}} \gamma\!\cdot\!T \varphi_{r_{19}}\qquad\text{(2.202; G7)}\\
&- \frac{N g}{L^{4}} \varepsilon^{ir_{17}} (\mathcal D_{d_{17}}\bar\varphi_{r_{17}}) \gamma^{d_{17}} L_{ij} \varepsilon^{jr_{19}} L_{r_{19}j_{19}} \varphi^{j_{19}}\qquad\text{(2.203; G7)}\\
&+\frac{i g}{L^{4}} \varepsilon^{ir_{17}} (\mathcal D_{d_{17}}\bar\varphi_{r_{17}}) \gamma^{d_{17}} L_{ij} \varepsilon^{jr_{19}} (\not{\mathcal D}L_{r_{19}j_{19}}) L^{j_{19}k_{19}} \varphi_{k_{19}}\qquad\text{(2.204; G7)}
\end{aligned}
\tag{121}
```

```math
\begin{aligned}
&- \frac{i g}{L^{4}} \varepsilon^{ir_{17}} (\mathcal D_{d_{17}}\bar\varphi_{r_{17}}) \gamma^{d_{17}} L_{ij} \varepsilon^{jr_{19}} \not E L_{r_{19}j_{19}} \varphi^{j_{19}}\qquad\text{(2.205; G7)}\\
&+\frac{8 g}{L^{2}} \varepsilon^{ir_{17}} L_{r_{17}j_{17}} \bar\chi^{j_{17}} L_{ij} \varepsilon^{jr_{19}} \not{\mathcal D}\varphi_{r_{19}}\qquad\text{(2.206; G7)}\\
&+\frac{64 i g}{L^{2}} \varepsilon^{ir_{17}} L_{r_{17}j_{17}} \bar\chi^{j_{17}} L_{ij} \varepsilon^{jr_{19}} L_{r_{19}j_{19}} \chi^{j_{19}}\qquad\text{(2.207; G7)}\\
&+\frac{16 i g}{L^{2}} \varepsilon^{ir_{17}} L_{r_{17}j_{17}} \bar\chi^{j_{17}} L_{ij} \varepsilon^{jr_{19}} \gamma\!\cdot\!T \varphi_{r_{19}}\qquad\text{(2.208; G7)}
\end{aligned}
\tag{122}
```

```math
\begin{aligned}
&- \frac{8 i N g}{L^{4}} \varepsilon^{ir_{17}} L_{r_{17}j_{17}} \bar\chi^{j_{17}} L_{ij} \varepsilon^{jr_{19}} L_{r_{19}j_{19}} \varphi^{j_{19}}\qquad\text{(2.209; G7)}\\
&- \frac{8 g}{L^{4}} \varepsilon^{ir_{17}} L_{r_{17}j_{17}} \bar\chi^{j_{17}} L_{ij} \varepsilon^{jr_{19}} (\not{\mathcal D}L_{r_{19}j_{19}}) L^{j_{19}k_{19}} \varphi_{k_{19}}\qquad\text{(2.210; G7)}\\
&+\frac{8 g}{L^{4}} \varepsilon^{ir_{17}} L_{r_{17}j_{17}} \bar\chi^{j_{17}} L_{ij} \varepsilon^{jr_{19}} \not E L_{r_{19}j_{19}} \varphi^{j_{19}}\qquad\text{(2.211; G7)}\\
&- \frac{2 g}{L^{2}} \varepsilon^{ir_{17}} \bar\varphi_{r_{17}} \gamma\!\cdot\!T L_{ij} \varepsilon^{jr_{19}} \not{\mathcal D}\varphi_{r_{19}}\qquad\text{(2.212; G7)}
\end{aligned}
\tag{123}
```

```math
\begin{aligned}
&- \frac{16 i g}{L^{2}} \varepsilon^{ir_{17}} \bar\varphi_{r_{17}} \gamma\!\cdot\!T L_{ij} \varepsilon^{jr_{19}} L_{r_{19}j_{19}} \chi^{j_{19}}\qquad\text{(2.213; G7)}\\
&- \frac{4 i g}{L^{2}} \varepsilon^{ir_{17}} \bar\varphi_{r_{17}} \gamma\!\cdot\!T L_{ij} \varepsilon^{jr_{19}} \gamma\!\cdot\!T \varphi_{r_{19}}\qquad\text{(2.214; G7)}\\
&+\frac{2 i N g}{L^{4}} \varepsilon^{ir_{17}} \bar\varphi_{r_{17}} \gamma\!\cdot\!T L_{ij} \varepsilon^{jr_{19}} L_{r_{19}j_{19}} \varphi^{j_{19}}\qquad\text{(2.215; G7)}\\
&+\frac{2 g}{L^{4}} \varepsilon^{ir_{17}} \bar\varphi_{r_{17}} \gamma\!\cdot\!T L_{ij} \varepsilon^{jr_{19}} (\not{\mathcal D}L_{r_{19}j_{19}}) L^{j_{19}k_{19}} \varphi_{k_{19}}\qquad\text{(2.216; G7)}
\end{aligned}
\tag{124}
```

```math
\begin{aligned}
&- \frac{2 g}{L^{4}} \varepsilon^{ir_{17}} \bar\varphi_{r_{17}} \gamma\!\cdot\!T L_{ij} \varepsilon^{jr_{19}} \not E L_{r_{19}j_{19}} \varphi^{j_{19}}\qquad\text{(2.217; G7)}\\
&- \frac{N g}{L^{4}} \varepsilon^{ir_{17}} L_{r_{17}j_{17}} \bar\varphi^{j_{17}} L_{ij} \varepsilon^{jr_{19}} \not{\mathcal D}\varphi_{r_{19}}\qquad\text{(2.218; G7)}\\
&- \frac{8 i N g}{L^{4}} \varepsilon^{ir_{17}} L_{r_{17}j_{17}} \bar\varphi^{j_{17}} L_{ij} \varepsilon^{jr_{19}} L_{r_{19}j_{19}} \chi^{j_{19}}\qquad\text{(2.219; G7)}\\
&- \frac{2 i N g}{L^{4}} \varepsilon^{ir_{17}} L_{r_{17}j_{17}} \bar\varphi^{j_{17}} L_{ij} \varepsilon^{jr_{19}} \gamma\!\cdot\!T \varphi_{r_{19}}\qquad\text{(2.220; G7)}
\end{aligned}
\tag{125}
```

```math
\begin{aligned}
&+\frac{i N^{2} g}{L^{6}} \varepsilon^{ir_{17}} L_{r_{17}j_{17}} \bar\varphi^{j_{17}} L_{ij} \varepsilon^{jr_{19}} L_{r_{19}j_{19}} \varphi^{j_{19}}\qquad\text{(2.221; G7)}\\
&+\frac{N g}{L^{6}} \varepsilon^{ir_{17}} L_{r_{17}j_{17}} \bar\varphi^{j_{17}} L_{ij} \varepsilon^{jr_{19}} (\not{\mathcal D}L_{r_{19}j_{19}}) L^{j_{19}k_{19}} \varphi_{k_{19}}\qquad\text{(2.222; G7)}\\
&- \frac{N g}{L^{6}} \varepsilon^{ir_{17}} L_{r_{17}j_{17}} \bar\varphi^{j_{17}} L_{ij} \varepsilon^{jr_{19}} \not E L_{r_{19}j_{19}} \varphi^{j_{19}}\qquad\text{(2.223; G7)}\\
&+\frac{i g}{L^{4}} \varepsilon^{ir_{17}} L^{j_{17}k_{17}} \bar\varphi_{k_{17}} (\not{\mathcal D}L_{r_{17}j_{17}}) L_{ij} \varepsilon^{jr_{19}} \not{\mathcal D}\varphi_{r_{19}}\qquad\text{(2.224; G7)}
\end{aligned}
\tag{126}
```

```math
\begin{aligned}
&- \frac{8 g}{L^{4}} \varepsilon^{ir_{17}} L^{j_{17}k_{17}} \bar\varphi_{k_{17}} (\not{\mathcal D}L_{r_{17}j_{17}}) L_{ij} \varepsilon^{jr_{19}} L_{r_{19}j_{19}} \chi^{j_{19}}\qquad\text{(2.225; G7)}\\
&- \frac{2 g}{L^{4}} \varepsilon^{ir_{17}} L^{j_{17}k_{17}} \bar\varphi_{k_{17}} (\not{\mathcal D}L_{r_{17}j_{17}}) L_{ij} \varepsilon^{jr_{19}} \gamma\!\cdot\!T \varphi_{r_{19}}\qquad\text{(2.226; G7)}\\
&+\frac{N g}{L^{6}} \varepsilon^{ir_{17}} L^{j_{17}k_{17}} \bar\varphi_{k_{17}} (\not{\mathcal D}L_{r_{17}j_{17}}) L_{ij} \varepsilon^{jr_{19}} L_{r_{19}j_{19}} \varphi^{j_{19}}\qquad\text{(2.227; G7)}\\
&- \frac{i g}{L^{6}} \varepsilon^{ir_{17}} L^{j_{17}k_{17}} \bar\varphi_{k_{17}} (\not{\mathcal D}L_{r_{17}j_{17}}) L_{ij} \varepsilon^{jr_{19}} (\not{\mathcal D}L_{r_{19}j_{19}}) L^{j_{19}k_{19}} \varphi_{k_{19}}\qquad\text{(2.228; G7)}
\end{aligned}
\tag{127}
```

```math
\begin{aligned}
&+\frac{i g}{L^{6}} \varepsilon^{ir_{17}} L^{j_{17}k_{17}} \bar\varphi_{k_{17}} (\not{\mathcal D}L_{r_{17}j_{17}}) L_{ij} \varepsilon^{jr_{19}} \not E L_{r_{19}j_{19}} \varphi^{j_{19}}\qquad\text{(2.229; G7)}\\
&- \frac{i g}{L^{4}} \varepsilon^{ir_{17}} L_{r_{17}j_{17}} \bar\varphi^{j_{17}} \not E L_{ij} \varepsilon^{jr_{19}} \not{\mathcal D}\varphi_{r_{19}}\qquad\text{(2.230; G7)}\\
&+\frac{8 g}{L^{4}} \varepsilon^{ir_{17}} L_{r_{17}j_{17}} \bar\varphi^{j_{17}} \not E L_{ij} \varepsilon^{jr_{19}} L_{r_{19}j_{19}} \chi^{j_{19}}\qquad\text{(2.231; G7)}\\
&+\frac{2 g}{L^{4}} \varepsilon^{ir_{17}} L_{r_{17}j_{17}} \bar\varphi^{j_{17}} \not E L_{ij} \varepsilon^{jr_{19}} \gamma\!\cdot\!T \varphi_{r_{19}}\qquad\text{(2.232; G7)}
\end{aligned}
\tag{128}
```

```math
\begin{aligned}
&- \frac{N g}{L^{6}} \varepsilon^{ir_{17}} L_{r_{17}j_{17}} \bar\varphi^{j_{17}} \not E L_{ij} \varepsilon^{jr_{19}} L_{r_{19}j_{19}} \varphi^{j_{19}}\qquad\text{(2.233; G7)}\\
&+\frac{i g}{L^{6}} \varepsilon^{ir_{17}} L_{r_{17}j_{17}} \bar\varphi^{j_{17}} \not E L_{ij} \varepsilon^{jr_{19}} (\not{\mathcal D}L_{r_{19}j_{19}}) L^{j_{19}k_{19}} \varphi_{k_{19}}\qquad\text{(2.234; G7)}\\
&- \frac{i g}{L^{6}} \varepsilon^{ir_{17}} L_{r_{17}j_{17}} \bar\varphi^{j_{17}} \not E L_{ij} \varepsilon^{jr_{19}} \not E L_{r_{19}j_{19}} \varphi^{j_{19}}\qquad\text{(2.235; G7)}\\
&- \frac{i N g}{L^{2}} \bar\psi_a^i \gamma^a \varepsilon^{jr_{23}} \not{\mathcal D}\varphi_{r_{23}} L_{ij}\qquad\text{(2.236; G8)}
\end{aligned}
\tag{129}
```

```math
\begin{aligned}
&+\frac{8 N g}{L^{2}} \bar\psi_a^i \gamma^a \varepsilon^{jr_{23}} L_{r_{23}j_{23}} \chi^{j_{23}} L_{ij}\qquad\text{(2.237; G8)}\\
&+\frac{2 N g}{L^{2}} \bar\psi_a^i \gamma^a \varepsilon^{jr_{23}} \gamma\!\cdot\!T \varphi_{r_{23}} L_{ij}\qquad\text{(2.238; G8)}\\
&- \frac{N^{2} g}{L^{4}} \bar\psi_a^i \gamma^a \varepsilon^{jr_{23}} L_{r_{23}j_{23}} \varphi^{j_{23}} L_{ij}\qquad\text{(2.239; G8)}\\
&+\frac{i N g}{L^{4}} \bar\psi_a^i \gamma^a \varepsilon^{jr_{23}} (\not{\mathcal D}L_{r_{23}j_{23}}) L^{j_{23}k_{23}} \varphi_{k_{23}} L_{ij}\qquad\text{(2.240; G8)}
\end{aligned}
\tag{130}
```

```math
\begin{aligned}
&- \frac{i N g}{L^{4}} \bar\psi_a^i \gamma^a \varepsilon^{jr_{23}} \not E L_{r_{23}j_{23}} \varphi^{j_{23}} L_{ij}\qquad\text{(2.241; G8)}\\
&+\frac{i}{L} \bar\psi_a^i \gamma^a \varepsilon^{jr_{27}} \not{\mathcal D}\varphi_{r_{27}} Y'_{ij}\qquad\text{(2.242; G9)}\\
&- \frac{8}{L} \bar\psi_a^i \gamma^a \varepsilon^{jr_{27}} L_{r_{27}j_{27}} \chi^{j_{27}} Y'_{ij}\qquad\text{(2.243; G9)}\\
&- \frac{2}{L} \bar\psi_a^i \gamma^a \varepsilon^{jr_{27}} \gamma\!\cdot\!T \varphi_{r_{27}} Y'_{ij}\qquad\text{(2.244; G9)}
\end{aligned}
\tag{131}
```

```math
\begin{aligned}
&+\frac{N}{L^{3}} \bar\psi_a^i \gamma^a \varepsilon^{jr_{27}} L_{r_{27}j_{27}} \varphi^{j_{27}} Y'_{ij}\qquad\text{(2.245; G9)}\\
&- \frac{i}{L^{3}} \bar\psi_a^i \gamma^a \varepsilon^{jr_{27}} (\not{\mathcal D}L_{r_{27}j_{27}}) L^{j_{27}k_{27}} \varphi_{k_{27}} Y'_{ij}\qquad\text{(2.246; G9)}\\
&+\frac{i}{L^{3}} \bar\psi_a^i \gamma^a \varepsilon^{jr_{27}} \not E L_{r_{27}j_{27}} \varphi^{j_{27}} Y'_{ij}\qquad\text{(2.247; G9)}\\
&+\frac{3 i N}{4 L^{2}} \varepsilon^{ir_{30}} (\mathcal D_{d_{30}}\bar\varphi_{r_{30}}) \gamma^{d_{30}} \gamma^a \gamma\cdot\widehat G \psi_{ai}\qquad\text{(2.248; G10)}
\end{aligned}
\tag{132}
```

```math
\begin{aligned}
&- \frac{6 N}{L^{2}} \varepsilon^{ir_{30}} L_{r_{30}j_{30}} \bar\chi^{j_{30}} \gamma^a \gamma\cdot\widehat G \psi_{ai}\qquad\text{(2.249; G10)}\\
&+\frac{3 N}{2 L^{2}} \varepsilon^{ir_{30}} \bar\varphi_{r_{30}} \gamma\!\cdot\!T \gamma^a \gamma\cdot\widehat G \psi_{ai}\qquad\text{(2.250; G10)}\\
&+\frac{3 N^{2}}{4 L^{4}} \varepsilon^{ir_{30}} L_{r_{30}j_{30}} \bar\varphi^{j_{30}} \gamma^a \gamma\cdot\widehat G \psi_{ai}\qquad\text{(2.251; G10)}\\
&- \frac{3 i N}{4 L^{4}} \varepsilon^{ir_{30}} L^{j_{30}k_{30}} \bar\varphi_{k_{30}} (\not{\mathcal D}L_{r_{30}j_{30}}) \gamma^a \gamma\cdot\widehat G \psi_{ai}\qquad\text{(2.252; G10)}
\end{aligned}
\tag{133}
```

```math
\begin{aligned}
&+\frac{3 i N}{4 L^{4}} \varepsilon^{ir_{30}} L_{r_{30}j_{30}} \bar\varphi^{j_{30}} \not E \gamma^a \gamma\cdot\widehat G \psi_{ai}\qquad\text{(2.253; G10)}\\
&- \frac{3 i N}{L^{2}} \varepsilon^{ir_{35}} (\mathcal D_{d_{35}}\bar\varphi_{r_{35}}) \gamma^{d_{35}} \gamma^a \gamma\cdot T \psi_{ai}\qquad\text{(2.254; G10)}\\
&+\frac{24 N}{L^{2}} \varepsilon^{ir_{35}} L_{r_{35}j_{35}} \bar\chi^{j_{35}} \gamma^a \gamma\cdot T \psi_{ai}\qquad\text{(2.255; G10)}\\
&- \frac{6 N}{L^{2}} \varepsilon^{ir_{35}} \bar\varphi_{r_{35}} \gamma\!\cdot\!T \gamma^a \gamma\cdot T \psi_{ai}\qquad\text{(2.256; G10)}
\end{aligned}
\tag{134}
```

```math
\begin{aligned}
&- \frac{3 N^{2}}{L^{4}} \varepsilon^{ir_{35}} L_{r_{35}j_{35}} \bar\varphi^{j_{35}} \gamma^a \gamma\cdot T \psi_{ai}\qquad\text{(2.257; G10)}\\
&+\frac{3 i N}{L^{4}} \varepsilon^{ir_{35}} L^{j_{35}k_{35}} \bar\varphi_{k_{35}} (\not{\mathcal D}L_{r_{35}j_{35}}) \gamma^a \gamma\cdot T \psi_{ai}\qquad\text{(2.258; G10)}\\
&- \frac{3 i N}{L^{4}} \varepsilon^{ir_{35}} L_{r_{35}j_{35}} \bar\varphi^{j_{35}} \not E \gamma^a \gamma\cdot T \psi_{ai}\qquad\text{(2.259; G10)}\\
&+\frac{3 i N g}{2 L^{2}} \varepsilon^{ir_{40}} (\mathcal D_{d_{40}}\bar\varphi_{r_{40}}) \gamma^{d_{40}} \gamma^a L_{ij} \psi_a^j\qquad\text{(2.260; G10)}
\end{aligned}
\tag{135}
```

```math
\begin{aligned}
&- \frac{12 N g}{L^{2}} \varepsilon^{ir_{40}} L_{r_{40}j_{40}} \bar\chi^{j_{40}} \gamma^a L_{ij} \psi_a^j\qquad\text{(2.261; G10)}\\
&+\frac{3 N g}{L^{2}} \varepsilon^{ir_{40}} \bar\varphi_{r_{40}} \gamma\!\cdot\!T \gamma^a L_{ij} \psi_a^j\qquad\text{(2.262; G10)}\\
&+\frac{3 N^{2} g}{2 L^{4}} \varepsilon^{ir_{40}} L_{r_{40}j_{40}} \bar\varphi^{j_{40}} \gamma^a L_{ij} \psi_a^j\qquad\text{(2.263; G10)}\\
&- \frac{3 i N g}{2 L^{4}} \varepsilon^{ir_{40}} L^{j_{40}k_{40}} \bar\varphi_{k_{40}} (\not{\mathcal D}L_{r_{40}j_{40}}) \gamma^a L_{ij} \psi_a^j\qquad\text{(2.264; G10)}
\end{aligned}
\tag{136}
```

```math
\begin{aligned}
&+\frac{3 i N g}{2 L^{4}} \varepsilon^{ir_{40}} L_{r_{40}j_{40}} \bar\varphi^{j_{40}} \not E \gamma^a L_{ij} \psi_a^j\qquad\text{(2.265; G10)}\\
&- \frac{3 i N}{L^{2}} \varepsilon^{ir_{45}} (\mathcal D_{d_{45}}\bar\varphi_{r_{45}}) \gamma^{d_{45}} \gamma^a \phi_{ai}\qquad\text{(2.266; G10)}\\
&+\frac{24 N}{L^{2}} \varepsilon^{ir_{45}} L_{r_{45}j_{45}} \bar\chi^{j_{45}} \gamma^a \phi_{ai}\qquad\text{(2.267; G10)}\\
&- \frac{6 N}{L^{2}} \varepsilon^{ir_{45}} \bar\varphi_{r_{45}} \gamma\!\cdot\!T \gamma^a \phi_{ai}\qquad\text{(2.268; G10)}
\end{aligned}
\tag{137}
```

```math
\begin{aligned}
&- \frac{3 N^{2}}{L^{4}} \varepsilon^{ir_{45}} L_{r_{45}j_{45}} \bar\varphi^{j_{45}} \gamma^a \phi_{ai}\qquad\text{(2.269; G10)}\\
&+\frac{3 i N}{L^{4}} \varepsilon^{ir_{45}} L^{j_{45}k_{45}} \bar\varphi_{k_{45}} (\not{\mathcal D}L_{r_{45}j_{45}}) \gamma^a \phi_{ai}\qquad\text{(2.270; G10)}\\
&- \frac{3 i N}{L^{4}} \varepsilon^{ir_{45}} L_{r_{45}j_{45}} \bar\varphi^{j_{45}} \not E \gamma^a \phi_{ai}\qquad\text{(2.271; G10)}\\
&+\frac{3 i}{2 L^{4}} A'_a (\mathcal D_{b}L) L_{r_49s_49} \bar\varphi^{r_49} \varphi^{s_49} \widehat G^{ab}\qquad\text{(2.272; G11)}
\end{aligned}
\tag{138}
```

```math
\begin{aligned}
&- \frac{i}{2 L^{3}} A'_a \mathcal D_{b}\!\left(L_{r_49s_49}\right) \bar\varphi^{r_49} \varphi^{s_49} \widehat G^{ab}\qquad\text{(2.273; G11)}\\
&- \frac{i}{2 L^{3}} A'_a L_{r_49s_49} \mathcal D_{b}\!\left(\bar\varphi^{r_49}\right) \varphi^{s_49} \widehat G^{ab}\qquad\text{(2.274; G11)}\\
&- \frac{i}{2 L^{3}} A'_a L_{r_49s_49} \bar\varphi^{r_49} \mathcal D_{b}\!\left(\varphi^{s_49}\right) \widehat G^{ab}\qquad\text{(2.275; G11)}\\
&- \frac{i}{2 L^{3}} A'_a L_{r_52s_52} \bar\varphi^{r_52} \varphi^{s_52} \mathcal D_b\widehat G^{ab}\qquad\text{(2.276; G12)}
\end{aligned}
\tag{139}
```

```math
\begin{aligned}
&- \frac{24 i}{L^{4}} A'_a (\mathcal D_{b}L) L_{r_57s_57} \bar\varphi^{r_57} \varphi^{s_57} T^{ab}\qquad\text{(2.277; G14)}\\
&+\frac{8 i}{L^{3}} A'_a \mathcal D_{b}\!\left(L_{r_57s_57}\right) \bar\varphi^{r_57} \varphi^{s_57} T^{ab}\qquad\text{(2.278; G14)}\\
&+\frac{8 i}{L^{3}} A'_a L_{r_57s_57} \mathcal D_{b}\!\left(\bar\varphi^{r_57}\right) \varphi^{s_57} T^{ab}\qquad\text{(2.279; G14)}\\
&+\frac{8 i}{L^{3}} A'_a L_{r_57s_57} \bar\varphi^{r_57} \mathcal D_{b}\!\left(\varphi^{s_57}\right) T^{ab}\qquad\text{(2.280; G14)}
\end{aligned}
\tag{140}
```

```math
\begin{aligned}
&+\frac{8 i}{L^{3}} A'_a L_{r_60s_60} \bar\varphi^{r_60} \varphi^{s_60} \mathcal D_bT^{ab}\qquad\text{(2.281; G15)}\\
&- \frac{1}{8 L} A'_a \varepsilon^{ir_{67}} (\mathcal D_{d_{67}}\bar\varphi_{r_{67}}) \gamma^{d_{67}} \gamma^{ab} \gamma\cdot\widehat G \psi_{bi}\qquad\text{(2.282; G17)}\\
&- \frac{i}{L} A'_a \varepsilon^{ir_{67}} L_{r_{67}j_{67}} \bar\chi^{j_{67}} \gamma^{ab} \gamma\cdot\widehat G \psi_{bi}\qquad\text{(2.283; G17)}\\
&+\frac{i}{4 L} A'_a \varepsilon^{ir_{67}} \bar\varphi_{r_{67}} \gamma\!\cdot\!T \gamma^{ab} \gamma\cdot\widehat G \psi_{bi}\qquad\text{(2.284; G17)}
\end{aligned}
\tag{141}
```

```math
\begin{aligned}
&+\frac{i N}{8 L^{3}} A'_a \varepsilon^{ir_{67}} L_{r_{67}j_{67}} \bar\varphi^{j_{67}} \gamma^{ab} \gamma\cdot\widehat G \psi_{bi}\qquad\text{(2.285; G17)}\\
&+\frac{1}{8 L^{3}} A'_a \varepsilon^{ir_{67}} L^{j_{67}k_{67}} \bar\varphi_{k_{67}} (\not{\mathcal D}L_{r_{67}j_{67}}) \gamma^{ab} \gamma\cdot\widehat G \psi_{bi}\qquad\text{(2.286; G17)}\\
&- \frac{1}{8 L^{3}} A'_a \varepsilon^{ir_{67}} L_{r_{67}j_{67}} \bar\varphi^{j_{67}} \not E \gamma^{ab} \gamma\cdot\widehat G \psi_{bi}\qquad\text{(2.287; G17)}\\
&+\frac{1}{2 L} A'_a \varepsilon^{ir_{72}} (\mathcal D_{d_{72}}\bar\varphi_{r_{72}}) \gamma^{d_{72}} \gamma^{ab} \gamma\cdot T \psi_{bi}\qquad\text{(2.288; G17)}
\end{aligned}
\tag{142}
```

```math
\begin{aligned}
&+\frac{4 i}{L} A'_a \varepsilon^{ir_{72}} L_{r_{72}j_{72}} \bar\chi^{j_{72}} \gamma^{ab} \gamma\cdot T \psi_{bi}\qquad\text{(2.289; G17)}\\
&- \frac{i}{L} A'_a \varepsilon^{ir_{72}} \bar\varphi_{r_{72}} \gamma\!\cdot\!T \gamma^{ab} \gamma\cdot T \psi_{bi}\qquad\text{(2.290; G17)}\\
&- \frac{i N}{2 L^{3}} A'_a \varepsilon^{ir_{72}} L_{r_{72}j_{72}} \bar\varphi^{j_{72}} \gamma^{ab} \gamma\cdot T \psi_{bi}\qquad\text{(2.291; G17)}\\
&- \frac{1}{2 L^{3}} A'_a \varepsilon^{ir_{72}} L^{j_{72}k_{72}} \bar\varphi_{k_{72}} (\not{\mathcal D}L_{r_{72}j_{72}}) \gamma^{ab} \gamma\cdot T \psi_{bi}\qquad\text{(2.292; G17)}
\end{aligned}
\tag{143}
```

```math
\begin{aligned}
&+\frac{1}{2 L^{3}} A'_a \varepsilon^{ir_{72}} L_{r_{72}j_{72}} \bar\varphi^{j_{72}} \not E \gamma^{ab} \gamma\cdot T \psi_{bi}\qquad\text{(2.293; G17)}\\
&- \frac{g}{4 L} A'_a \varepsilon^{ir_{77}} (\mathcal D_{d_{77}}\bar\varphi_{r_{77}}) \gamma^{d_{77}} \gamma^{ab} L_{ij} \psi_b^j\qquad\text{(2.294; G17)}\\
&- \frac{2 i g}{L} A'_a \varepsilon^{ir_{77}} L_{r_{77}j_{77}} \bar\chi^{j_{77}} \gamma^{ab} L_{ij} \psi_b^j\qquad\text{(2.295; G17)}\\
&+\frac{i g}{2 L} A'_a \varepsilon^{ir_{77}} \bar\varphi_{r_{77}} \gamma\!\cdot\!T \gamma^{ab} L_{ij} \psi_b^j\qquad\text{(2.296; G17)}
\end{aligned}
\tag{144}
```

```math
\begin{aligned}
&+\frac{i N g}{4 L^{3}} A'_a \varepsilon^{ir_{77}} L_{r_{77}j_{77}} \bar\varphi^{j_{77}} \gamma^{ab} L_{ij} \psi_b^j\qquad\text{(2.297; G17)}\\
&+\frac{g}{4 L^{3}} A'_a \varepsilon^{ir_{77}} L^{j_{77}k_{77}} \bar\varphi_{k_{77}} (\not{\mathcal D}L_{r_{77}j_{77}}) \gamma^{ab} L_{ij} \psi_b^j\qquad\text{(2.298; G17)}\\
&- \frac{g}{4 L^{3}} A'_a \varepsilon^{ir_{77}} L_{r_{77}j_{77}} \bar\varphi^{j_{77}} \not E \gamma^{ab} L_{ij} \psi_b^j\qquad\text{(2.299; G17)}\\
&+\frac{1}{2 L} A'_a \varepsilon^{ir_{82}} (\mathcal D_{d_{82}}\bar\varphi_{r_{82}}) \gamma^{d_{82}} \gamma^{ab} \phi_{bi}\qquad\text{(2.300; G17)}
\end{aligned}
\tag{145}
```

```math
\begin{aligned}
&+\frac{4 i}{L} A'_a \varepsilon^{ir_{82}} L_{r_{82}j_{82}} \bar\chi^{j_{82}} \gamma^{ab} \phi_{bi}\qquad\text{(2.301; G17)}\\
&- \frac{i}{L} A'_a \varepsilon^{ir_{82}} \bar\varphi_{r_{82}} \gamma\!\cdot\!T \gamma^{ab} \phi_{bi}\qquad\text{(2.302; G17)}\\
&- \frac{i N}{2 L^{3}} A'_a \varepsilon^{ir_{82}} L_{r_{82}j_{82}} \bar\varphi^{j_{82}} \gamma^{ab} \phi_{bi}\qquad\text{(2.303; G17)}\\
&- \frac{1}{2 L^{3}} A'_a \varepsilon^{ir_{82}} L^{j_{82}k_{82}} \bar\varphi_{k_{82}} (\not{\mathcal D}L_{r_{82}j_{82}}) \gamma^{ab} \phi_{bi}\qquad\text{(2.304; G17)}
\end{aligned}
\tag{146}
```

```math
\begin{aligned}
&+\frac{1}{2 L^{3}} A'_a \varepsilon^{ir_{82}} L_{r_{82}j_{82}} \bar\varphi^{j_{82}} \not E \gamma^{ab} \phi_{bi}\qquad\text{(2.305; G17)}\\
&- \frac{N}{8 L} A'_a \bar\psi_b^i \gamma^{ba} \gamma^c \gamma\cdot\widehat G \psi_{ci}\qquad\text{(2.306; G18)}\\
&+\frac{N}{2 L} A'_a \bar\psi_b^i \gamma^{ba} \gamma^c \gamma\cdot T \psi_{ci}\qquad\text{(2.307; G18)}\\
&- \frac{N g}{4 L} A'_a \bar\psi_b^i \gamma^{ba} \gamma^c L_{ij} \psi_c^j\qquad\text{(2.308; G18)}
\end{aligned}
\tag{147}
```

```math
\begin{aligned}
&+\frac{N}{2 L} A'_a \bar\psi_b^i \gamma^{ba} \gamma^c \phi_{ci}\qquad\text{(2.309; G18)}\\
&- \frac{i}{2 L^{2}} A'_a \bar\psi_b^i \gamma^{ba} \gamma^{q_{115}} (\mathcal D_{q_{115}}L) \not{\mathcal D}\varphi_{i}\qquad\text{(2.310; G19)}\\
&+\frac{i}{2 L} A'_a \bar\psi_b^i \gamma^{ba} \gamma^{q_{115}} \mathcal D_{q_{115}}\!\left(\not{\mathcal D}\varphi_{i}\right)\qquad\text{(2.311; G19)}\\
&+\frac{4}{L^{2}} A'_a \bar\psi_b^i \gamma^{ba} \gamma^{q_{115}} (\mathcal D_{q_{115}}L) L_{ij_{115}} \chi^{j_{115}}\qquad\text{(2.312; G19)}
\end{aligned}
\tag{148}
```

```math
\begin{aligned}
&- \frac{4}{L} A'_a \bar\psi_b^i \gamma^{ba} \gamma^{q_{115}} \mathcal D_{q_{115}}\!\left(L_{ij_{115}}\right) \chi^{j_{115}}\qquad\text{(2.313; G19)}\\
&- \frac{4}{L} A'_a \bar\psi_b^i \gamma^{ba} \gamma^{q_{115}} L_{ij_{115}} \mathcal D_{q_{115}}\!\left(\chi^{j_{115}}\right)\qquad\text{(2.314; G19)}\\
&+\frac{1}{L^{2}} A'_a \bar\psi_b^i \gamma^{ba} \gamma^{q_{115}} (\mathcal D_{q_{115}}L) \gamma\!\cdot\!T \varphi_{i}\qquad\text{(2.315; G19)}\\
&- \frac{1}{L} A'_a \bar\psi_b^i \gamma^{ba} \gamma^{q_{115}} \gamma\!\cdot\!T \mathcal D_{q_{115}}\!\left(\varphi_{i}\right)\qquad\text{(2.316; G19)}
\end{aligned}
\tag{149}
```

```math
\begin{aligned}
&- \frac{3 N}{2 L^{4}} A'_a \bar\psi_b^i \gamma^{ba} \gamma^{q_{115}} (\mathcal D_{q_{115}}L) L_{ij_{115}} \varphi^{j_{115}}\qquad\text{(2.317; G19)}\\
&+\frac{1}{2 L^{3}} A'_a \bar\psi_b^i \gamma^{ba} \gamma^{q_{115}} (\mathcal D_{q_{115}}N) L_{ij_{115}} \varphi^{j_{115}}\qquad\text{(2.318; G19)}\\
&+\frac{N}{2 L^{3}} A'_a \bar\psi_b^i \gamma^{ba} \gamma^{q_{115}} \mathcal D_{q_{115}}\!\left(L_{ij_{115}}\right) \varphi^{j_{115}}\qquad\text{(2.319; G19)}\\
&+\frac{N}{2 L^{3}} A'_a \bar\psi_b^i \gamma^{ba} \gamma^{q_{115}} L_{ij_{115}} \mathcal D_{q_{115}}\!\left(\varphi^{j_{115}}\right)\qquad\text{(2.320; G19)}
\end{aligned}
\tag{150}
```

```math
\begin{aligned}
&+\frac{3 i}{2 L^{4}} A'_a \bar\psi_b^i \gamma^{ba} \gamma^{q_{115}} (\mathcal D_{q_{115}}L) (\not{\mathcal D}L_{ij_{115}}) L^{j_{115}k_{115}} \varphi_{k_{115}}\qquad\text{(2.321; G19)}\\
&- \frac{i}{2 L^{3}} A'_a \bar\psi_b^i \gamma^{ba} \gamma^{q_{115}} \mathcal D_{q_{115}}\!\left((\not{\mathcal D}L_{ij_{115}})\right) L^{j_{115}k_{115}} \varphi_{k_{115}}\qquad\text{(2.322; G19)}\\
&- \frac{i}{2 L^{3}} A'_a \bar\psi_b^i \gamma^{ba} \gamma^{q_{115}} (\not{\mathcal D}L_{ij_{115}}) \mathcal D_{q_{115}}\!\left(L^{j_{115}k_{115}}\right) \varphi_{k_{115}}\qquad\text{(2.323; G19)}\\
&- \frac{i}{2 L^{3}} A'_a \bar\psi_b^i \gamma^{ba} \gamma^{q_{115}} (\not{\mathcal D}L_{ij_{115}}) L^{j_{115}k_{115}} \mathcal D_{q_{115}}\!\left(\varphi_{k_{115}}\right)\qquad\text{(2.324; G19)}
\end{aligned}
\tag{151}
```

```math
\begin{aligned}
&- \frac{3 i}{2 L^{4}} A'_a \bar\psi_b^i \gamma^{ba} \gamma^{q_{115}} (\mathcal D_{q_{115}}L) \not E L_{ij_{115}} \varphi^{j_{115}}\qquad\text{(2.325; G19)}\\
&+\frac{i}{2 L^{3}} A'_a \bar\psi_b^i \gamma^{ba} \gamma^{q_{115}} \mathcal D_{q_{115}}\!\left(\not E\right) L_{ij_{115}} \varphi^{j_{115}}\qquad\text{(2.326; G19)}\\
&+\frac{i}{2 L^{3}} A'_a \bar\psi_b^i \gamma^{ba} \gamma^{q_{115}} \not E \mathcal D_{q_{115}}\!\left(L_{ij_{115}}\right) \varphi^{j_{115}}\qquad\text{(2.327; G19)}\\
&+\frac{i}{2 L^{3}} A'_a \bar\psi_b^i \gamma^{ba} \gamma^{q_{115}} \not E L_{ij_{115}} \mathcal D_{q_{115}}\!\left(\varphi^{j_{115}}\right)\qquad\text{(2.328; G19)}
\end{aligned}
\tag{152}
```

```math
\begin{aligned}
&- \frac{1}{L} A'_a \bar\psi_b^i \gamma^{ba} \gamma^{q_{115}} \gamma^{mn}(\mathcal D_{q_{115}}T_{mn}) \varphi_{i}\qquad\text{(2.329; G19)}\\
&+\frac{1}{L} A'_a \bar\psi_b^i \gamma^{ba} \gamma\cdot T \not{\mathcal D}\varphi_{i}\qquad\text{(2.330; G20)}\\
&+\frac{8 i}{L} A'_a \bar\psi_b^i \gamma^{ba} \gamma\cdot T L_{ij_{120}} \chi^{j_{120}}\qquad\text{(2.331; G20)}\\
&+\frac{2 i}{L} A'_a \bar\psi_b^i \gamma^{ba} \gamma\cdot T \gamma\!\cdot\!T \varphi_{i}\qquad\text{(2.332; G20)}
\end{aligned}
\tag{153}
```

```math
\begin{aligned}
&- \frac{i N}{L^{3}} A'_a \bar\psi_b^i \gamma^{ba} \gamma\cdot T L_{ij_{120}} \varphi^{j_{120}}\qquad\text{(2.333; G20)}\\
&- \frac{1}{L^{3}} A'_a \bar\psi_b^i \gamma^{ba} \gamma\cdot T (\not{\mathcal D}L_{ij_{120}}) L^{j_{120}k_{120}} \varphi_{k_{120}}\qquad\text{(2.334; G20)}\\
&+\frac{1}{L^{3}} A'_a \bar\psi_b^i \gamma^{ba} \gamma\cdot T \not E L_{ij_{120}} \varphi^{j_{120}}\qquad\text{(2.335; G20)}\\
&- \frac{8 i N}{L} A'_a \bar\psi_b^i \gamma^{ba} \chi_i\qquad\text{(2.336; G21)}
\end{aligned}
\tag{154}
```

```math
\begin{aligned}
&- \frac{1}{8 L} A'_a \bar\psi_b^i \gamma^{ba} \gamma\cdot\widehat G \not{\mathcal D}\varphi_{i}\qquad\text{(2.337; G22)}\\
&- \frac{i}{L} A'_a \bar\psi_b^i \gamma^{ba} \gamma\cdot\widehat G L_{ij_{130}} \chi^{j_{130}}\qquad\text{(2.338; G22)}\\
&- \frac{i}{4 L} A'_a \bar\psi_b^i \gamma^{ba} \gamma\cdot\widehat G \gamma\!\cdot\!T \varphi_{i}\qquad\text{(2.339; G22)}\\
&+\frac{i N}{8 L^{3}} A'_a \bar\psi_b^i \gamma^{ba} \gamma\cdot\widehat G L_{ij_{130}} \varphi^{j_{130}}\qquad\text{(2.340; G22)}
\end{aligned}
\tag{155}
```

```math
\begin{aligned}
&+\frac{1}{8 L^{3}} A'_a \bar\psi_b^i \gamma^{ba} \gamma\cdot\widehat G (\not{\mathcal D}L_{ij_{130}}) L^{j_{130}k_{130}} \varphi_{k_{130}}\qquad\text{(2.341; G22)}\\
&- \frac{1}{8 L^{3}} A'_a \bar\psi_b^i \gamma^{ba} \gamma\cdot\widehat G \not E L_{ij_{130}} \varphi^{j_{130}}\qquad\text{(2.342; G22)}\\
&+\frac{g}{4 L} A'_a \bar\psi_b^i \gamma^{ba} L_{ij} \varepsilon^{jr_{135}} \not{\mathcal D}\varphi_{r_{135}}\qquad\text{(2.343; G23)}\\
&+\frac{2 i g}{L} A'_a \bar\psi_b^i \gamma^{ba} L_{ij} \varepsilon^{jr_{135}} L_{r_{135}j_{135}} \chi^{j_{135}}\qquad\text{(2.344; G23)}
\end{aligned}
\tag{156}
```

```math
\begin{aligned}
&+\frac{i g}{2 L} A'_a \bar\psi_b^i \gamma^{ba} L_{ij} \varepsilon^{jr_{135}} \gamma\!\cdot\!T \varphi_{r_{135}}\qquad\text{(2.345; G23)}\\
&- \frac{i N g}{4 L^{3}} A'_a \bar\psi_b^i \gamma^{ba} L_{ij} \varepsilon^{jr_{135}} L_{r_{135}j_{135}} \varphi^{j_{135}}\qquad\text{(2.346; G23)}\\
&- \frac{g}{4 L^{3}} A'_a \bar\psi_b^i \gamma^{ba} L_{ij} \varepsilon^{jr_{135}} (\not{\mathcal D}L_{r_{135}j_{135}}) L^{j_{135}k_{135}} \varphi_{k_{135}}\qquad\text{(2.347; G23)}\\
&+\frac{g}{4 L^{3}} A'_a \bar\psi_b^i \gamma^{ba} L_{ij} \varepsilon^{jr_{135}} \not E L_{r_{135}j_{135}} \varphi^{j_{135}}\qquad\text{(2.348; G23)}
\end{aligned}
\tag{157}
```

```math
\begin{aligned}
&- \frac{N g}{4 L} A'_a \bar\psi_b^i \gamma^{abc} \psi_c^j L_{ij}\qquad\text{(2.349; G24)}\\
&+\frac{1}{4} A'_a \bar\psi_b^i \gamma^{abc} \psi_c^j Y'_{ij}\qquad\text{(2.350; G25)}\\
&+\frac{i N}{L} \Box_c\!\left(\frac{1}{L^{3}} L_{r_148s_148} \bar\varphi^{r_148} \varphi^{s_148}\right)\qquad\text{(2.351; G26)}\\
&+\frac{i}{L^{3}} L_{r_147s_147} \bar\varphi^{r_147} \varphi^{s_147} \Box_c\!\left(L^{-1}N\right)\qquad\text{(2.352; G26)}
\end{aligned}
\tag{158}
```

```math
\begin{aligned}
&+\frac{4 i N}{L^{4}} L_{r_149s_149} \bar\varphi^{r_149} \varphi^{s_149} f_a^a\qquad\text{(2.353; G27)}\\
&- \frac{i}{4 L^{3}} L_{r_151s_151} \bar\varphi^{r_151} \varphi^{s_151} \widehat F'_{ab} \widehat G^{ab}\qquad\text{(2.354; G28)}\\
&+\frac{16 i N}{L^{4}} L_{r_154s_154} \bar\varphi^{r_154} \varphi^{s_154} \widehat G_{ab} T^{ab}\qquad\text{(2.355; G29)}\\
&+\frac{4 i}{L^{3}} L_{r_157s_157} \bar\varphi^{r_157} \varphi^{s_157} \widehat F'_{ab} T^{ab}\qquad\text{(2.356; G30)}
\end{aligned}
\tag{159}
```

```math
\begin{aligned}
&- \frac{16 i N}{L^{4}} L_{r_160s_160} \bar\varphi^{r_160} \varphi^{s_160} D\qquad\text{(2.357; G31)}\\
&- \frac{416 i N}{3 L^{4}} L_{r_162s_162} \bar\varphi^{r_162} \varphi^{s_162} T^2\qquad\text{(2.358; G32)}\\
&+\frac{32 N}{L^{2}} \bar\chi^i \not{\mathcal D}\varphi_{i}\qquad\text{(2.359; G33)}\\
&+\frac{256 i N}{L^{2}} \bar\chi^i L_{ij_{166}} \chi^{j_{166}}\qquad\text{(2.360; G33)}
\end{aligned}
\tag{160}
```

```math
\begin{aligned}
&+\frac{64 i N}{L^{2}} \bar\chi^i \gamma\!\cdot\!T \varphi_{i}\qquad\text{(2.361; G33)}\\
&- \frac{32 i N^{2}}{L^{4}} \bar\chi^i L_{ij_{166}} \varphi^{j_{166}}\qquad\text{(2.362; G33)}\\
&- \frac{32 N}{L^{4}} \bar\chi^i (\not{\mathcal D}L_{ij_{166}}) L^{j_{166}k_{166}} \varphi_{k_{166}}\qquad\text{(2.363; G33)}\\
&+\frac{32 N}{L^{4}} \bar\chi^i \not E L_{ij_{166}} \varphi^{j_{166}}\qquad\text{(2.364; G33)}
\end{aligned}
\tag{161}
```

```math
\begin{aligned}
&- \frac{20 N^{2}}{L^{2}} \bar\psi_a^i \gamma^a \chi_i\qquad\text{(2.365; G34)}\\
&- \frac{N}{L^{3}} \bar\psi_a^i \gamma^a \gamma^{q_{174}} (\mathcal D_{q_{174}}L) \not{\mathcal D}\varphi_{i}\qquad\text{(2.366; G35)}\\
&+\frac{N}{L^{2}} \bar\psi_a^i \gamma^a \gamma^{q_{174}} \mathcal D_{q_{174}}\!\left(\not{\mathcal D}\varphi_{i}\right)\qquad\text{(2.367; G35)}\\
&- \frac{8 i N}{L^{3}} \bar\psi_a^i \gamma^a \gamma^{q_{174}} (\mathcal D_{q_{174}}L) L_{ij_{174}} \chi^{j_{174}}\qquad\text{(2.368; G35)}
\end{aligned}
\tag{162}
```

```math
\begin{aligned}
&+\frac{8 i N}{L^{2}} \bar\psi_a^i \gamma^a \gamma^{q_{174}} \mathcal D_{q_{174}}\!\left(L_{ij_{174}}\right) \chi^{j_{174}}\qquad\text{(2.369; G35)}\\
&+\frac{8 i N}{L^{2}} \bar\psi_a^i \gamma^a \gamma^{q_{174}} L_{ij_{174}} \mathcal D_{q_{174}}\!\left(\chi^{j_{174}}\right)\qquad\text{(2.370; G35)}\\
&- \frac{2 i N}{L^{3}} \bar\psi_a^i \gamma^a \gamma^{q_{174}} (\mathcal D_{q_{174}}L) \gamma\!\cdot\!T \varphi_{i}\qquad\text{(2.371; G35)}\\
&+\frac{2 i N}{L^{2}} \bar\psi_a^i \gamma^a \gamma^{q_{174}} \gamma\!\cdot\!T \mathcal D_{q_{174}}\!\left(\varphi_{i}\right)\qquad\text{(2.372; G35)}
\end{aligned}
\tag{163}
```

```math
\begin{aligned}
&+\frac{3 i N^{2}}{L^{5}} \bar\psi_a^i \gamma^a \gamma^{q_{174}} (\mathcal D_{q_{174}}L) L_{ij_{174}} \varphi^{j_{174}}\qquad\text{(2.373; G35)}\\
&- \frac{i N}{L^{4}} \bar\psi_a^i \gamma^a \gamma^{q_{174}} (\mathcal D_{q_{174}}N) L_{ij_{174}} \varphi^{j_{174}}\qquad\text{(2.374; G35)}\\
&- \frac{i N^{2}}{L^{4}} \bar\psi_a^i \gamma^a \gamma^{q_{174}} \mathcal D_{q_{174}}\!\left(L_{ij_{174}}\right) \varphi^{j_{174}}\qquad\text{(2.375; G35)}\\
&- \frac{i N^{2}}{L^{4}} \bar\psi_a^i \gamma^a \gamma^{q_{174}} L_{ij_{174}} \mathcal D_{q_{174}}\!\left(\varphi^{j_{174}}\right)\qquad\text{(2.376; G35)}
\end{aligned}
\tag{164}
```

```math
\begin{aligned}
&+\frac{3 N}{L^{5}} \bar\psi_a^i \gamma^a \gamma^{q_{174}} (\mathcal D_{q_{174}}L) (\not{\mathcal D}L_{ij_{174}}) L^{j_{174}k_{174}} \varphi_{k_{174}}\qquad\text{(2.377; G35)}\\
&- \frac{N}{L^{4}} \bar\psi_a^i \gamma^a \gamma^{q_{174}} \mathcal D_{q_{174}}\!\left((\not{\mathcal D}L_{ij_{174}})\right) L^{j_{174}k_{174}} \varphi_{k_{174}}\qquad\text{(2.378; G35)}\\
&- \frac{N}{L^{4}} \bar\psi_a^i \gamma^a \gamma^{q_{174}} (\not{\mathcal D}L_{ij_{174}}) \mathcal D_{q_{174}}\!\left(L^{j_{174}k_{174}}\right) \varphi_{k_{174}}\qquad\text{(2.379; G35)}\\
&- \frac{N}{L^{4}} \bar\psi_a^i \gamma^a \gamma^{q_{174}} (\not{\mathcal D}L_{ij_{174}}) L^{j_{174}k_{174}} \mathcal D_{q_{174}}\!\left(\varphi_{k_{174}}\right)\qquad\text{(2.380; G35)}
\end{aligned}
\tag{165}
```

```math
\begin{aligned}
&- \frac{3 N}{L^{5}} \bar\psi_a^i \gamma^a \gamma^{q_{174}} (\mathcal D_{q_{174}}L) \not E L_{ij_{174}} \varphi^{j_{174}}\qquad\text{(2.381; G35)}\\
&+\frac{N}{L^{4}} \bar\psi_a^i \gamma^a \gamma^{q_{174}} \mathcal D_{q_{174}}\!\left(\not E\right) L_{ij_{174}} \varphi^{j_{174}}\qquad\text{(2.382; G35)}\\
&+\frac{N}{L^{4}} \bar\psi_a^i \gamma^a \gamma^{q_{174}} \not E \mathcal D_{q_{174}}\!\left(L_{ij_{174}}\right) \varphi^{j_{174}}\qquad\text{(2.383; G35)}\\
&+\frac{N}{L^{4}} \bar\psi_a^i \gamma^a \gamma^{q_{174}} \not E L_{ij_{174}} \mathcal D_{q_{174}}\!\left(\varphi^{j_{174}}\right)\qquad\text{(2.384; G35)}
\end{aligned}
\tag{166}
```

```math
\begin{aligned}
&+\frac{2 i N}{L^{2}} \bar\psi_a^i \gamma^a \gamma^{q_{174}} \gamma^{mn}(\mathcal D_{q_{174}}T_{mn}) \varphi_{i}\qquad\text{(2.385; G35)}\\
&- \frac{2 i N}{L^{2}} \bar\psi_a^i \gamma^a \gamma\cdot T \not{\mathcal D}\varphi_{i}\qquad\text{(2.386; G36)}\\
&+\frac{16 N}{L^{2}} \bar\psi_a^i \gamma^a \gamma\cdot T L_{ij_{179}} \chi^{j_{179}}\qquad\text{(2.387; G36)}\\
&+\frac{4 N}{L^{2}} \bar\psi_a^i \gamma^a \gamma\cdot T \gamma\!\cdot\!T \varphi_{i}\qquad\text{(2.388; G36)}
\end{aligned}
\tag{167}
```

```math
\begin{aligned}
&- \frac{2 N^{2}}{L^{4}} \bar\psi_a^i \gamma^a \gamma\cdot T L_{ij_{179}} \varphi^{j_{179}}\qquad\text{(2.389; G36)}\\
&+\frac{2 i N}{L^{4}} \bar\psi_a^i \gamma^a \gamma\cdot T (\not{\mathcal D}L_{ij_{179}}) L^{j_{179}k_{179}} \varphi_{k_{179}}\qquad\text{(2.390; G36)}\\
&- \frac{2 i N}{L^{4}} \bar\psi_a^i \gamma^a \gamma\cdot T \not E L_{ij_{179}} \varphi^{j_{179}}\qquad\text{(2.391; G36)}\\
&+\frac{i N}{4 L^{2}} \bar\psi_a^i \gamma^a \gamma\cdot\widehat G \not{\mathcal D}\varphi_{i}\qquad\text{(2.392; G37)}
\end{aligned}
\tag{168}
```

```math
\begin{aligned}
&- \frac{2 N}{L^{2}} \bar\psi_a^i \gamma^a \gamma\cdot\widehat G L_{ij_{184}} \chi^{j_{184}}\qquad\text{(2.393; G37)}\\
&- \frac{N}{2 L^{2}} \bar\psi_a^i \gamma^a \gamma\cdot\widehat G \gamma\!\cdot\!T \varphi_{i}\qquad\text{(2.394; G37)}\\
&+\frac{N^{2}}{4 L^{4}} \bar\psi_a^i \gamma^a \gamma\cdot\widehat G L_{ij_{184}} \varphi^{j_{184}}\qquad\text{(2.395; G37)}\\
&- \frac{i N}{4 L^{4}} \bar\psi_a^i \gamma^a \gamma\cdot\widehat G (\not{\mathcal D}L_{ij_{184}}) L^{j_{184}k_{184}} \varphi_{k_{184}}\qquad\text{(2.396; G37)}
\end{aligned}
\tag{169}
```

```math
\begin{aligned}
&+\frac{i N}{4 L^{4}} \bar\psi_a^i \gamma^a \gamma\cdot\widehat G \not E L_{ij_{184}} \varphi^{j_{184}}\qquad\text{(2.397; G37)}\\
&- \frac{i N g}{2 L^{2}} \bar\psi_a^i \gamma^a L_{ij} \varepsilon^{jr_{189}} \not{\mathcal D}\varphi_{r_{189}}\qquad\text{(2.398; G38)}\\
&+\frac{4 N g}{L^{2}} \bar\psi_a^i \gamma^a L_{ij} \varepsilon^{jr_{189}} L_{r_{189}j_{189}} \chi^{j_{189}}\qquad\text{(2.399; G38)}\\
&+\frac{N g}{L^{2}} \bar\psi_a^i \gamma^a L_{ij} \varepsilon^{jr_{189}} \gamma\!\cdot\!T \varphi_{r_{189}}\qquad\text{(2.400; G38)}
\end{aligned}
\tag{170}
```

```math
\begin{aligned}
&- \frac{N^{2} g}{2 L^{4}} \bar\psi_a^i \gamma^a L_{ij} \varepsilon^{jr_{189}} L_{r_{189}j_{189}} \varphi^{j_{189}}\qquad\text{(2.401; G38)}\\
&+\frac{i N g}{2 L^{4}} \bar\psi_a^i \gamma^a L_{ij} \varepsilon^{jr_{189}} (\not{\mathcal D}L_{r_{189}j_{189}}) L^{j_{189}k_{189}} \varphi_{k_{189}}\qquad\text{(2.402; G38)}\\
&- \frac{i N g}{2 L^{4}} \bar\psi_a^i \gamma^a L_{ij} \varepsilon^{jr_{189}} \not E L_{r_{189}j_{189}} \varphi^{j_{189}}\qquad\text{(2.403; G38)}\\
&+\frac{i N^{2}}{4 L^{2}} \bar\psi_a^i \gamma^a \gamma^b \gamma\cdot\widehat G \psi_{bi}\qquad\text{(2.404; G39)}
\end{aligned}
\tag{171}
```

```math
\begin{aligned}
&- \frac{i N^{2}}{L^{2}} \bar\psi_a^i \gamma^a \gamma^b \gamma\cdot T \psi_{bi}\qquad\text{(2.405; G39)}\\
&+\frac{i N^{2} g}{2 L^{2}} \bar\psi_a^i \gamma^a \gamma^b L_{ij} \psi_b^j\qquad\text{(2.406; G39)}\\
&- \frac{i N^{2}}{L^{2}} \bar\psi_a^i \gamma^a \gamma^b \phi_{bi}\qquad\text{(2.407; G39)}\\
&- \frac{i N^{2}}{4 L^{2}} \bar\psi_a^i \gamma\cdot\widehat G \psi^a_i\qquad\text{(2.408; G40)}
\end{aligned}
\tag{172}
```

```math
\begin{aligned}
&+\frac{i N^{2}}{L^{2}} \bar\psi_a^i \gamma\cdot T \psi^a_i\qquad\text{(2.409; G40)}\\
&- \frac{i N^{2} g}{2 L^{2}} \bar\psi_a^i L_{ij} \psi^{aj}\qquad\text{(2.410; G40)}\\
&+\frac{i N^{2}}{L^{2}} \bar\psi_a^i \phi^a_i\qquad\text{(2.411; G40)}\\
&- \frac{i N^{2} g}{2 L^{2}} \bar\psi_a^i \gamma^{ab} \psi_b^j L_{ij}\qquad\text{(2.412; G41)}
\end{aligned}
\tag{173}
```

```math
\begin{aligned}
&+\frac{i N}{2 L} \bar\psi_a^i \gamma^{ab} \psi_b^j Y'_{ij}\qquad\text{(2.413; G42)}
\end{aligned}
\tag{174}
```

### 6.3 Four explicit fermions

```math
\begin{aligned}
&+\frac{6}{L^{5}} \varepsilon^{ir_{6}} (\mathcal D_{d_{6}}\bar\varphi_{r_{6}}) \gamma^{d_{6}} \gamma^{q_{7}} (\mathcal D_{q_{7}}L) \varphi^{j_{7}} \bar\varphi_{i} \varphi_{j_{7}}\qquad\text{(4.1; G3)}\\
&- \frac{2}{L^{4}} \varepsilon^{ir_{6}} (\mathcal D_{d_{6}}\bar\varphi_{r_{6}}) \gamma^{d_{6}} \gamma^{q_{7}} \mathcal D_{q_{7}}\!\left(\varphi^{j_{7}}\right) \bar\varphi_{i} \varphi_{j_{7}}\qquad\text{(4.2; G3)}\\
&- \frac{2}{L^{4}} \varepsilon^{ir_{6}} (\mathcal D_{d_{6}}\bar\varphi_{r_{6}}) \gamma^{d_{6}} \gamma^{q_{7}} \varphi^{j_{7}} \mathcal D_{q_{7}}\!\left(\bar\varphi_{i}\right) \varphi_{j_{7}}\qquad\text{(4.3; G3)}\\
&- \frac{2}{L^{4}} \varepsilon^{ir_{6}} (\mathcal D_{d_{6}}\bar\varphi_{r_{6}}) \gamma^{d_{6}} \gamma^{q_{7}} \varphi^{j_{7}} \bar\varphi_{i} \mathcal D_{q_{7}}\!\left(\varphi_{j_{7}}\right)\qquad\text{(4.4; G3)}
\end{aligned}
\tag{175}
```

```math
\begin{aligned}
&- \frac{30}{L^{7}} \varepsilon^{ir_{6}} (\mathcal D_{d_{6}}\bar\varphi_{r_{6}}) \gamma^{d_{6}} \gamma^{q_{7}} (\mathcal D_{q_{7}}L) \varphi^{j_{7}} \bar\varphi_{k_{7}} \varphi_{l_{7}} L^{k_{7}l_{7}} L_{ij_{7}}\qquad\text{(4.5; G3)}\\
&+\frac{6}{L^{6}} \varepsilon^{ir_{6}} (\mathcal D_{d_{6}}\bar\varphi_{r_{6}}) \gamma^{d_{6}} \gamma^{q_{7}} \mathcal D_{q_{7}}\!\left(\varphi^{j_{7}}\right) \bar\varphi_{k_{7}} \varphi_{l_{7}} L^{k_{7}l_{7}} L_{ij_{7}}\qquad\text{(4.6; G3)}\\
&+\frac{6}{L^{6}} \varepsilon^{ir_{6}} (\mathcal D_{d_{6}}\bar\varphi_{r_{6}}) \gamma^{d_{6}} \gamma^{q_{7}} \varphi^{j_{7}} \mathcal D_{q_{7}}\!\left(\bar\varphi_{k_{7}}\right) \varphi_{l_{7}} L^{k_{7}l_{7}} L_{ij_{7}}\qquad\text{(4.7; G3)}\\
&+\frac{6}{L^{6}} \varepsilon^{ir_{6}} (\mathcal D_{d_{6}}\bar\varphi_{r_{6}}) \gamma^{d_{6}} \gamma^{q_{7}} \varphi^{j_{7}} \bar\varphi_{k_{7}} \mathcal D_{q_{7}}\!\left(\varphi_{l_{7}}\right) L^{k_{7}l_{7}} L_{ij_{7}}\qquad\text{(4.8; G3)}
\end{aligned}
\tag{176}
```

```math
\begin{aligned}
&+\frac{6}{L^{6}} \varepsilon^{ir_{6}} (\mathcal D_{d_{6}}\bar\varphi_{r_{6}}) \gamma^{d_{6}} \gamma^{q_{7}} \varphi^{j_{7}} \bar\varphi_{k_{7}} \varphi_{l_{7}} \mathcal D_{q_{7}}\!\left(L^{k_{7}l_{7}}\right) L_{ij_{7}}\qquad\text{(4.9; G3)}\\
&+\frac{6}{L^{6}} \varepsilon^{ir_{6}} (\mathcal D_{d_{6}}\bar\varphi_{r_{6}}) \gamma^{d_{6}} \gamma^{q_{7}} \varphi^{j_{7}} \bar\varphi_{k_{7}} \varphi_{l_{7}} L^{k_{7}l_{7}} \mathcal D_{q_{7}}\!\left(L_{ij_{7}}\right)\qquad\text{(4.10; G3)}\\
&+\frac{48 i}{L^{5}} \varepsilon^{ir_{6}} L_{r_{6}j_{6}} \bar\chi^{j_{6}} \gamma^{q_{7}} (\mathcal D_{q_{7}}L) \varphi^{j_{7}} \bar\varphi_{i} \varphi_{j_{7}}\qquad\text{(4.11; G3)}\\
&- \frac{16 i}{L^{4}} \varepsilon^{ir_{6}} L_{r_{6}j_{6}} \bar\chi^{j_{6}} \gamma^{q_{7}} \mathcal D_{q_{7}}\!\left(\varphi^{j_{7}}\right) \bar\varphi_{i} \varphi_{j_{7}}\qquad\text{(4.12; G3)}
\end{aligned}
\tag{177}
```

```math
\begin{aligned}
&- \frac{16 i}{L^{4}} \varepsilon^{ir_{6}} L_{r_{6}j_{6}} \bar\chi^{j_{6}} \gamma^{q_{7}} \varphi^{j_{7}} \mathcal D_{q_{7}}\!\left(\bar\varphi_{i}\right) \varphi_{j_{7}}\qquad\text{(4.13; G3)}\\
&- \frac{16 i}{L^{4}} \varepsilon^{ir_{6}} L_{r_{6}j_{6}} \bar\chi^{j_{6}} \gamma^{q_{7}} \varphi^{j_{7}} \bar\varphi_{i} \mathcal D_{q_{7}}\!\left(\varphi_{j_{7}}\right)\qquad\text{(4.14; G3)}\\
&- \frac{240 i}{L^{7}} \varepsilon^{ir_{6}} L_{r_{6}j_{6}} \bar\chi^{j_{6}} \gamma^{q_{7}} (\mathcal D_{q_{7}}L) \varphi^{j_{7}} \bar\varphi_{k_{7}} \varphi_{l_{7}} L^{k_{7}l_{7}} L_{ij_{7}}\qquad\text{(4.15; G3)}\\
&+\frac{48 i}{L^{6}} \varepsilon^{ir_{6}} L_{r_{6}j_{6}} \bar\chi^{j_{6}} \gamma^{q_{7}} \mathcal D_{q_{7}}\!\left(\varphi^{j_{7}}\right) \bar\varphi_{k_{7}} \varphi_{l_{7}} L^{k_{7}l_{7}} L_{ij_{7}}\qquad\text{(4.16; G3)}
\end{aligned}
\tag{178}
```

```math
\begin{aligned}
&+\frac{48 i}{L^{6}} \varepsilon^{ir_{6}} L_{r_{6}j_{6}} \bar\chi^{j_{6}} \gamma^{q_{7}} \varphi^{j_{7}} \mathcal D_{q_{7}}\!\left(\bar\varphi_{k_{7}}\right) \varphi_{l_{7}} L^{k_{7}l_{7}} L_{ij_{7}}\qquad\text{(4.17; G3)}\\
&+\frac{48 i}{L^{6}} \varepsilon^{ir_{6}} L_{r_{6}j_{6}} \bar\chi^{j_{6}} \gamma^{q_{7}} \varphi^{j_{7}} \bar\varphi_{k_{7}} \mathcal D_{q_{7}}\!\left(\varphi_{l_{7}}\right) L^{k_{7}l_{7}} L_{ij_{7}}\qquad\text{(4.18; G3)}\\
&+\frac{48 i}{L^{6}} \varepsilon^{ir_{6}} L_{r_{6}j_{6}} \bar\chi^{j_{6}} \gamma^{q_{7}} \varphi^{j_{7}} \bar\varphi_{k_{7}} \varphi_{l_{7}} \mathcal D_{q_{7}}\!\left(L^{k_{7}l_{7}}\right) L_{ij_{7}}\qquad\text{(4.19; G3)}\\
&+\frac{48 i}{L^{6}} \varepsilon^{ir_{6}} L_{r_{6}j_{6}} \bar\chi^{j_{6}} \gamma^{q_{7}} \varphi^{j_{7}} \bar\varphi_{k_{7}} \varphi_{l_{7}} L^{k_{7}l_{7}} \mathcal D_{q_{7}}\!\left(L_{ij_{7}}\right)\qquad\text{(4.20; G3)}
\end{aligned}
\tag{179}
```

```math
\begin{aligned}
&- \frac{12 i}{L^{5}} \varepsilon^{ir_{6}} \bar\varphi_{r_{6}} \gamma\!\cdot\!T \gamma^{q_{7}} (\mathcal D_{q_{7}}L) \varphi^{j_{7}} \bar\varphi_{i} \varphi_{j_{7}}\qquad\text{(4.21; G3)}\\
&+\frac{4 i}{L^{4}} \varepsilon^{ir_{6}} \bar\varphi_{r_{6}} \gamma\!\cdot\!T \gamma^{q_{7}} \mathcal D_{q_{7}}\!\left(\varphi^{j_{7}}\right) \bar\varphi_{i} \varphi_{j_{7}}\qquad\text{(4.22; G3)}\\
&+\frac{4 i}{L^{4}} \varepsilon^{ir_{6}} \bar\varphi_{r_{6}} \gamma\!\cdot\!T \gamma^{q_{7}} \varphi^{j_{7}} \mathcal D_{q_{7}}\!\left(\bar\varphi_{i}\right) \varphi_{j_{7}}\qquad\text{(4.23; G3)}\\
&+\frac{4 i}{L^{4}} \varepsilon^{ir_{6}} \bar\varphi_{r_{6}} \gamma\!\cdot\!T \gamma^{q_{7}} \varphi^{j_{7}} \bar\varphi_{i} \mathcal D_{q_{7}}\!\left(\varphi_{j_{7}}\right)\qquad\text{(4.24; G3)}
\end{aligned}
\tag{180}
```

```math
\begin{aligned}
&+\frac{60 i}{L^{7}} \varepsilon^{ir_{6}} \bar\varphi_{r_{6}} \gamma\!\cdot\!T \gamma^{q_{7}} (\mathcal D_{q_{7}}L) \varphi^{j_{7}} \bar\varphi_{k_{7}} \varphi_{l_{7}} L^{k_{7}l_{7}} L_{ij_{7}}\qquad\text{(4.25; G3)}\\
&- \frac{12 i}{L^{6}} \varepsilon^{ir_{6}} \bar\varphi_{r_{6}} \gamma\!\cdot\!T \gamma^{q_{7}} \mathcal D_{q_{7}}\!\left(\varphi^{j_{7}}\right) \bar\varphi_{k_{7}} \varphi_{l_{7}} L^{k_{7}l_{7}} L_{ij_{7}}\qquad\text{(4.26; G3)}\\
&- \frac{12 i}{L^{6}} \varepsilon^{ir_{6}} \bar\varphi_{r_{6}} \gamma\!\cdot\!T \gamma^{q_{7}} \varphi^{j_{7}} \mathcal D_{q_{7}}\!\left(\bar\varphi_{k_{7}}\right) \varphi_{l_{7}} L^{k_{7}l_{7}} L_{ij_{7}}\qquad\text{(4.27; G3)}\\
&- \frac{12 i}{L^{6}} \varepsilon^{ir_{6}} \bar\varphi_{r_{6}} \gamma\!\cdot\!T \gamma^{q_{7}} \varphi^{j_{7}} \bar\varphi_{k_{7}} \mathcal D_{q_{7}}\!\left(\varphi_{l_{7}}\right) L^{k_{7}l_{7}} L_{ij_{7}}\qquad\text{(4.28; G3)}
\end{aligned}
\tag{181}
```

```math
\begin{aligned}
&- \frac{12 i}{L^{6}} \varepsilon^{ir_{6}} \bar\varphi_{r_{6}} \gamma\!\cdot\!T \gamma^{q_{7}} \varphi^{j_{7}} \bar\varphi_{k_{7}} \varphi_{l_{7}} \mathcal D_{q_{7}}\!\left(L^{k_{7}l_{7}}\right) L_{ij_{7}}\qquad\text{(4.29; G3)}\\
&- \frac{12 i}{L^{6}} \varepsilon^{ir_{6}} \bar\varphi_{r_{6}} \gamma\!\cdot\!T \gamma^{q_{7}} \varphi^{j_{7}} \bar\varphi_{k_{7}} \varphi_{l_{7}} L^{k_{7}l_{7}} \mathcal D_{q_{7}}\!\left(L_{ij_{7}}\right)\qquad\text{(4.30; G3)}\\
&- \frac{6 i N}{L^{7}} \varepsilon^{ir_{6}} L_{r_{6}j_{6}} \bar\varphi^{j_{6}} \gamma^{q_{7}} (\mathcal D_{q_{7}}L) \varphi^{j_{7}} \bar\varphi_{i} \varphi_{j_{7}}\qquad\text{(4.31; G3)}\\
&+\frac{2 i N}{L^{6}} \varepsilon^{ir_{6}} L_{r_{6}j_{6}} \bar\varphi^{j_{6}} \gamma^{q_{7}} \mathcal D_{q_{7}}\!\left(\varphi^{j_{7}}\right) \bar\varphi_{i} \varphi_{j_{7}}\qquad\text{(4.32; G3)}
\end{aligned}
\tag{182}
```

```math
\begin{aligned}
&+\frac{2 i N}{L^{6}} \varepsilon^{ir_{6}} L_{r_{6}j_{6}} \bar\varphi^{j_{6}} \gamma^{q_{7}} \varphi^{j_{7}} \mathcal D_{q_{7}}\!\left(\bar\varphi_{i}\right) \varphi_{j_{7}}\qquad\text{(4.33; G3)}\\
&+\frac{2 i N}{L^{6}} \varepsilon^{ir_{6}} L_{r_{6}j_{6}} \bar\varphi^{j_{6}} \gamma^{q_{7}} \varphi^{j_{7}} \bar\varphi_{i} \mathcal D_{q_{7}}\!\left(\varphi_{j_{7}}\right)\qquad\text{(4.34; G3)}\\
&+\frac{30 i N}{L^{9}} \varepsilon^{ir_{6}} L_{r_{6}j_{6}} \bar\varphi^{j_{6}} \gamma^{q_{7}} (\mathcal D_{q_{7}}L) \varphi^{j_{7}} \bar\varphi_{k_{7}} \varphi_{l_{7}} L^{k_{7}l_{7}} L_{ij_{7}}\qquad\text{(4.35; G3)}\\
&- \frac{6 i N}{L^{8}} \varepsilon^{ir_{6}} L_{r_{6}j_{6}} \bar\varphi^{j_{6}} \gamma^{q_{7}} \mathcal D_{q_{7}}\!\left(\varphi^{j_{7}}\right) \bar\varphi_{k_{7}} \varphi_{l_{7}} L^{k_{7}l_{7}} L_{ij_{7}}\qquad\text{(4.36; G3)}
\end{aligned}
\tag{183}
```

```math
\begin{aligned}
&- \frac{6 i N}{L^{8}} \varepsilon^{ir_{6}} L_{r_{6}j_{6}} \bar\varphi^{j_{6}} \gamma^{q_{7}} \varphi^{j_{7}} \mathcal D_{q_{7}}\!\left(\bar\varphi_{k_{7}}\right) \varphi_{l_{7}} L^{k_{7}l_{7}} L_{ij_{7}}\qquad\text{(4.37; G3)}\\
&- \frac{6 i N}{L^{8}} \varepsilon^{ir_{6}} L_{r_{6}j_{6}} \bar\varphi^{j_{6}} \gamma^{q_{7}} \varphi^{j_{7}} \bar\varphi_{k_{7}} \mathcal D_{q_{7}}\!\left(\varphi_{l_{7}}\right) L^{k_{7}l_{7}} L_{ij_{7}}\qquad\text{(4.38; G3)}\\
&- \frac{6 i N}{L^{8}} \varepsilon^{ir_{6}} L_{r_{6}j_{6}} \bar\varphi^{j_{6}} \gamma^{q_{7}} \varphi^{j_{7}} \bar\varphi_{k_{7}} \varphi_{l_{7}} \mathcal D_{q_{7}}\!\left(L^{k_{7}l_{7}}\right) L_{ij_{7}}\qquad\text{(4.39; G3)}\\
&- \frac{6 i N}{L^{8}} \varepsilon^{ir_{6}} L_{r_{6}j_{6}} \bar\varphi^{j_{6}} \gamma^{q_{7}} \varphi^{j_{7}} \bar\varphi_{k_{7}} \varphi_{l_{7}} L^{k_{7}l_{7}} \mathcal D_{q_{7}}\!\left(L_{ij_{7}}\right)\qquad\text{(4.40; G3)}
\end{aligned}
\tag{184}
```

```math
\begin{aligned}
&- \frac{6}{L^{7}} \varepsilon^{ir_{6}} L^{j_{6}k_{6}} \bar\varphi_{k_{6}} (\not{\mathcal D}L_{r_{6}j_{6}}) \gamma^{q_{7}} (\mathcal D_{q_{7}}L) \varphi^{j_{7}} \bar\varphi_{i} \varphi_{j_{7}}\qquad\text{(4.41; G3)}\\
&+\frac{2}{L^{6}} \varepsilon^{ir_{6}} L^{j_{6}k_{6}} \bar\varphi_{k_{6}} (\not{\mathcal D}L_{r_{6}j_{6}}) \gamma^{q_{7}} \mathcal D_{q_{7}}\!\left(\varphi^{j_{7}}\right) \bar\varphi_{i} \varphi_{j_{7}}\qquad\text{(4.42; G3)}\\
&+\frac{2}{L^{6}} \varepsilon^{ir_{6}} L^{j_{6}k_{6}} \bar\varphi_{k_{6}} (\not{\mathcal D}L_{r_{6}j_{6}}) \gamma^{q_{7}} \varphi^{j_{7}} \mathcal D_{q_{7}}\!\left(\bar\varphi_{i}\right) \varphi_{j_{7}}\qquad\text{(4.43; G3)}\\
&+\frac{2}{L^{6}} \varepsilon^{ir_{6}} L^{j_{6}k_{6}} \bar\varphi_{k_{6}} (\not{\mathcal D}L_{r_{6}j_{6}}) \gamma^{q_{7}} \varphi^{j_{7}} \bar\varphi_{i} \mathcal D_{q_{7}}\!\left(\varphi_{j_{7}}\right)\qquad\text{(4.44; G3)}
\end{aligned}
\tag{185}
```

```math
\begin{aligned}
&+\frac{30}{L^{9}} \varepsilon^{ir_{6}} L^{j_{6}k_{6}} \bar\varphi_{k_{6}} (\not{\mathcal D}L_{r_{6}j_{6}}) \gamma^{q_{7}} (\mathcal D_{q_{7}}L) \varphi^{j_{7}} \bar\varphi_{k_{7}} \varphi_{l_{7}} L^{k_{7}l_{7}} L_{ij_{7}}\qquad\text{(4.45; G3)}\\
&- \frac{6}{L^{8}} \varepsilon^{ir_{6}} L^{j_{6}k_{6}} \bar\varphi_{k_{6}} (\not{\mathcal D}L_{r_{6}j_{6}}) \gamma^{q_{7}} \mathcal D_{q_{7}}\!\left(\varphi^{j_{7}}\right) \bar\varphi_{k_{7}} \varphi_{l_{7}} L^{k_{7}l_{7}} L_{ij_{7}}\qquad\text{(4.46; G3)}\\
&- \frac{6}{L^{8}} \varepsilon^{ir_{6}} L^{j_{6}k_{6}} \bar\varphi_{k_{6}} (\not{\mathcal D}L_{r_{6}j_{6}}) \gamma^{q_{7}} \varphi^{j_{7}} \mathcal D_{q_{7}}\!\left(\bar\varphi_{k_{7}}\right) \varphi_{l_{7}} L^{k_{7}l_{7}} L_{ij_{7}}\qquad\text{(4.47; G3)}\\
&- \frac{6}{L^{8}} \varepsilon^{ir_{6}} L^{j_{6}k_{6}} \bar\varphi_{k_{6}} (\not{\mathcal D}L_{r_{6}j_{6}}) \gamma^{q_{7}} \varphi^{j_{7}} \bar\varphi_{k_{7}} \mathcal D_{q_{7}}\!\left(\varphi_{l_{7}}\right) L^{k_{7}l_{7}} L_{ij_{7}}\qquad\text{(4.48; G3)}
\end{aligned}
\tag{186}
```

```math
\begin{aligned}
&- \frac{6}{L^{8}} \varepsilon^{ir_{6}} L^{j_{6}k_{6}} \bar\varphi_{k_{6}} (\not{\mathcal D}L_{r_{6}j_{6}}) \gamma^{q_{7}} \varphi^{j_{7}} \bar\varphi_{k_{7}} \varphi_{l_{7}} \mathcal D_{q_{7}}\!\left(L^{k_{7}l_{7}}\right) L_{ij_{7}}\qquad\text{(4.49; G3)}\\
&- \frac{6}{L^{8}} \varepsilon^{ir_{6}} L^{j_{6}k_{6}} \bar\varphi_{k_{6}} (\not{\mathcal D}L_{r_{6}j_{6}}) \gamma^{q_{7}} \varphi^{j_{7}} \bar\varphi_{k_{7}} \varphi_{l_{7}} L^{k_{7}l_{7}} \mathcal D_{q_{7}}\!\left(L_{ij_{7}}\right)\qquad\text{(4.50; G3)}\\
&+\frac{6}{L^{7}} \varepsilon^{ir_{6}} L_{r_{6}j_{6}} \bar\varphi^{j_{6}} \not E \gamma^{q_{7}} (\mathcal D_{q_{7}}L) \varphi^{j_{7}} \bar\varphi_{i} \varphi_{j_{7}}\qquad\text{(4.51; G3)}\\
&- \frac{2}{L^{6}} \varepsilon^{ir_{6}} L_{r_{6}j_{6}} \bar\varphi^{j_{6}} \not E \gamma^{q_{7}} \mathcal D_{q_{7}}\!\left(\varphi^{j_{7}}\right) \bar\varphi_{i} \varphi_{j_{7}}\qquad\text{(4.52; G3)}
\end{aligned}
\tag{187}
```

```math
\begin{aligned}
&- \frac{2}{L^{6}} \varepsilon^{ir_{6}} L_{r_{6}j_{6}} \bar\varphi^{j_{6}} \not E \gamma^{q_{7}} \varphi^{j_{7}} \mathcal D_{q_{7}}\!\left(\bar\varphi_{i}\right) \varphi_{j_{7}}\qquad\text{(4.53; G3)}\\
&- \frac{2}{L^{6}} \varepsilon^{ir_{6}} L_{r_{6}j_{6}} \bar\varphi^{j_{6}} \not E \gamma^{q_{7}} \varphi^{j_{7}} \bar\varphi_{i} \mathcal D_{q_{7}}\!\left(\varphi_{j_{7}}\right)\qquad\text{(4.54; G3)}\\
&- \frac{30}{L^{9}} \varepsilon^{ir_{6}} L_{r_{6}j_{6}} \bar\varphi^{j_{6}} \not E \gamma^{q_{7}} (\mathcal D_{q_{7}}L) \varphi^{j_{7}} \bar\varphi_{k_{7}} \varphi_{l_{7}} L^{k_{7}l_{7}} L_{ij_{7}}\qquad\text{(4.55; G3)}\\
&+\frac{6}{L^{8}} \varepsilon^{ir_{6}} L_{r_{6}j_{6}} \bar\varphi^{j_{6}} \not E \gamma^{q_{7}} \mathcal D_{q_{7}}\!\left(\varphi^{j_{7}}\right) \bar\varphi_{k_{7}} \varphi_{l_{7}} L^{k_{7}l_{7}} L_{ij_{7}}\qquad\text{(4.56; G3)}
\end{aligned}
\tag{188}
```

```math
\begin{aligned}
&+\frac{6}{L^{8}} \varepsilon^{ir_{6}} L_{r_{6}j_{6}} \bar\varphi^{j_{6}} \not E \gamma^{q_{7}} \varphi^{j_{7}} \mathcal D_{q_{7}}\!\left(\bar\varphi_{k_{7}}\right) \varphi_{l_{7}} L^{k_{7}l_{7}} L_{ij_{7}}\qquad\text{(4.57; G3)}\\
&+\frac{6}{L^{8}} \varepsilon^{ir_{6}} L_{r_{6}j_{6}} \bar\varphi^{j_{6}} \not E \gamma^{q_{7}} \varphi^{j_{7}} \bar\varphi_{k_{7}} \mathcal D_{q_{7}}\!\left(\varphi_{l_{7}}\right) L^{k_{7}l_{7}} L_{ij_{7}}\qquad\text{(4.58; G3)}\\
&+\frac{6}{L^{8}} \varepsilon^{ir_{6}} L_{r_{6}j_{6}} \bar\varphi^{j_{6}} \not E \gamma^{q_{7}} \varphi^{j_{7}} \bar\varphi_{k_{7}} \varphi_{l_{7}} \mathcal D_{q_{7}}\!\left(L^{k_{7}l_{7}}\right) L_{ij_{7}}\qquad\text{(4.59; G3)}\\
&+\frac{6}{L^{8}} \varepsilon^{ir_{6}} L_{r_{6}j_{6}} \bar\varphi^{j_{6}} \not E \gamma^{q_{7}} \varphi^{j_{7}} \bar\varphi_{k_{7}} \varphi_{l_{7}} L^{k_{7}l_{7}} \mathcal D_{q_{7}}\!\left(L_{ij_{7}}\right)\qquad\text{(4.60; G3)}
\end{aligned}
\tag{189}
```

```math
\begin{aligned}
&+\frac{2}{L^{5}} \varepsilon^{ir_{6}} \bar\varphi^{j_{6}} \bar\varphi_{r_{6}} \varphi_{j_{6}} \gamma^{q_{7}} (\mathcal D_{q_{7}}L) \not{\mathcal D}\varphi_{i}\qquad\text{(4.61; G3)}\\
&- \frac{2}{L^{4}} \varepsilon^{ir_{6}} \bar\varphi^{j_{6}} \bar\varphi_{r_{6}} \varphi_{j_{6}} \gamma^{q_{7}} \mathcal D_{q_{7}}\!\left(\not{\mathcal D}\varphi_{i}\right)\qquad\text{(4.62; G3)}\\
&+\frac{16 i}{L^{5}} \varepsilon^{ir_{6}} \bar\varphi^{j_{6}} \bar\varphi_{r_{6}} \varphi_{j_{6}} \gamma^{q_{7}} (\mathcal D_{q_{7}}L) L_{ij_{7}} \chi^{j_{7}}\qquad\text{(4.63; G3)}\\
&- \frac{16 i}{L^{4}} \varepsilon^{ir_{6}} \bar\varphi^{j_{6}} \bar\varphi_{r_{6}} \varphi_{j_{6}} \gamma^{q_{7}} \mathcal D_{q_{7}}\!\left(L_{ij_{7}}\right) \chi^{j_{7}}\qquad\text{(4.64; G3)}
\end{aligned}
\tag{190}
```

```math
\begin{aligned}
&- \frac{16 i}{L^{4}} \varepsilon^{ir_{6}} \bar\varphi^{j_{6}} \bar\varphi_{r_{6}} \varphi_{j_{6}} \gamma^{q_{7}} L_{ij_{7}} \mathcal D_{q_{7}}\!\left(\chi^{j_{7}}\right)\qquad\text{(4.65; G3)}\\
&+\frac{4 i}{L^{5}} \varepsilon^{ir_{6}} \bar\varphi^{j_{6}} \bar\varphi_{r_{6}} \varphi_{j_{6}} \gamma^{q_{7}} (\mathcal D_{q_{7}}L) \gamma\!\cdot\!T \varphi_{i}\qquad\text{(4.66; G3)}\\
&- \frac{4 i}{L^{4}} \varepsilon^{ir_{6}} \bar\varphi^{j_{6}} \bar\varphi_{r_{6}} \varphi_{j_{6}} \gamma^{q_{7}} \gamma\!\cdot\!T \mathcal D_{q_{7}}\!\left(\varphi_{i}\right)\qquad\text{(4.67; G3)}\\
&- \frac{6 i N}{L^{7}} \varepsilon^{ir_{6}} \bar\varphi^{j_{6}} \bar\varphi_{r_{6}} \varphi_{j_{6}} \gamma^{q_{7}} (\mathcal D_{q_{7}}L) L_{ij_{7}} \varphi^{j_{7}}\qquad\text{(4.68; G3)}
\end{aligned}
\tag{191}
```

```math
\begin{aligned}
&+\frac{2 i}{L^{6}} \varepsilon^{ir_{6}} \bar\varphi^{j_{6}} \bar\varphi_{r_{6}} \varphi_{j_{6}} \gamma^{q_{7}} (\mathcal D_{q_{7}}N) L_{ij_{7}} \varphi^{j_{7}}\qquad\text{(4.69; G3)}\\
&+\frac{2 i N}{L^{6}} \varepsilon^{ir_{6}} \bar\varphi^{j_{6}} \bar\varphi_{r_{6}} \varphi_{j_{6}} \gamma^{q_{7}} \mathcal D_{q_{7}}\!\left(L_{ij_{7}}\right) \varphi^{j_{7}}\qquad\text{(4.70; G3)}\\
&+\frac{2 i N}{L^{6}} \varepsilon^{ir_{6}} \bar\varphi^{j_{6}} \bar\varphi_{r_{6}} \varphi_{j_{6}} \gamma^{q_{7}} L_{ij_{7}} \mathcal D_{q_{7}}\!\left(\varphi^{j_{7}}\right)\qquad\text{(4.71; G3)}\\
&- \frac{6}{L^{7}} \varepsilon^{ir_{6}} \bar\varphi^{j_{6}} \bar\varphi_{r_{6}} \varphi_{j_{6}} \gamma^{q_{7}} (\mathcal D_{q_{7}}L) (\not{\mathcal D}L_{ij_{7}}) L^{j_{7}k_{7}} \varphi_{k_{7}}\qquad\text{(4.72; G3)}
\end{aligned}
\tag{192}
```

```math
\begin{aligned}
&+\frac{2}{L^{6}} \varepsilon^{ir_{6}} \bar\varphi^{j_{6}} \bar\varphi_{r_{6}} \varphi_{j_{6}} \gamma^{q_{7}} \mathcal D_{q_{7}}\!\left((\not{\mathcal D}L_{ij_{7}})\right) L^{j_{7}k_{7}} \varphi_{k_{7}}\qquad\text{(4.73; G3)}\\
&+\frac{2}{L^{6}} \varepsilon^{ir_{6}} \bar\varphi^{j_{6}} \bar\varphi_{r_{6}} \varphi_{j_{6}} \gamma^{q_{7}} (\not{\mathcal D}L_{ij_{7}}) \mathcal D_{q_{7}}\!\left(L^{j_{7}k_{7}}\right) \varphi_{k_{7}}\qquad\text{(4.74; G3)}\\
&+\frac{2}{L^{6}} \varepsilon^{ir_{6}} \bar\varphi^{j_{6}} \bar\varphi_{r_{6}} \varphi_{j_{6}} \gamma^{q_{7}} (\not{\mathcal D}L_{ij_{7}}) L^{j_{7}k_{7}} \mathcal D_{q_{7}}\!\left(\varphi_{k_{7}}\right)\qquad\text{(4.75; G3)}\\
&+\frac{6}{L^{7}} \varepsilon^{ir_{6}} \bar\varphi^{j_{6}} \bar\varphi_{r_{6}} \varphi_{j_{6}} \gamma^{q_{7}} (\mathcal D_{q_{7}}L) \not E L_{ij_{7}} \varphi^{j_{7}}\qquad\text{(4.76; G3)}
\end{aligned}
\tag{193}
```

```math
\begin{aligned}
&- \frac{2}{L^{6}} \varepsilon^{ir_{6}} \bar\varphi^{j_{6}} \bar\varphi_{r_{6}} \varphi_{j_{6}} \gamma^{q_{7}} \mathcal D_{q_{7}}\!\left(\not E\right) L_{ij_{7}} \varphi^{j_{7}}\qquad\text{(4.77; G3)}\\
&- \frac{2}{L^{6}} \varepsilon^{ir_{6}} \bar\varphi^{j_{6}} \bar\varphi_{r_{6}} \varphi_{j_{6}} \gamma^{q_{7}} \not E \mathcal D_{q_{7}}\!\left(L_{ij_{7}}\right) \varphi^{j_{7}}\qquad\text{(4.78; G3)}\\
&- \frac{2}{L^{6}} \varepsilon^{ir_{6}} \bar\varphi^{j_{6}} \bar\varphi_{r_{6}} \varphi_{j_{6}} \gamma^{q_{7}} \not E L_{ij_{7}} \mathcal D_{q_{7}}\!\left(\varphi^{j_{7}}\right)\qquad\text{(4.79; G3)}\\
&- \frac{4 i}{L^{4}} \varepsilon^{ir_{6}} \bar\varphi^{j_{6}} \bar\varphi_{r_{6}} \varphi_{j_{6}} \gamma^{q_{7}} \gamma^{mn}(\mathcal D_{q_{7}}T_{mn}) \varphi_{i}\qquad\text{(4.80; G3)}
\end{aligned}
\tag{194}
```

```math
\begin{aligned}
&- \frac{6}{L^{7}} \varepsilon^{ir_{6}} \bar\varphi^{j_{6}} \bar\varphi_{k_{6}} \varphi_{l_{6}} L^{k_{6}l_{6}} L_{r_{6}j_{6}} \gamma^{q_{7}} (\mathcal D_{q_{7}}L) \not{\mathcal D}\varphi_{i}\qquad\text{(4.81; G3)}\\
&+\frac{6}{L^{6}} \varepsilon^{ir_{6}} \bar\varphi^{j_{6}} \bar\varphi_{k_{6}} \varphi_{l_{6}} L^{k_{6}l_{6}} L_{r_{6}j_{6}} \gamma^{q_{7}} \mathcal D_{q_{7}}\!\left(\not{\mathcal D}\varphi_{i}\right)\qquad\text{(4.82; G3)}\\
&- \frac{48 i}{L^{7}} \varepsilon^{ir_{6}} \bar\varphi^{j_{6}} \bar\varphi_{k_{6}} \varphi_{l_{6}} L^{k_{6}l_{6}} L_{r_{6}j_{6}} \gamma^{q_{7}} (\mathcal D_{q_{7}}L) L_{ij_{7}} \chi^{j_{7}}\qquad\text{(4.83; G3)}\\
&+\frac{48 i}{L^{6}} \varepsilon^{ir_{6}} \bar\varphi^{j_{6}} \bar\varphi_{k_{6}} \varphi_{l_{6}} L^{k_{6}l_{6}} L_{r_{6}j_{6}} \gamma^{q_{7}} \mathcal D_{q_{7}}\!\left(L_{ij_{7}}\right) \chi^{j_{7}}\qquad\text{(4.84; G3)}
\end{aligned}
\tag{195}
```

```math
\begin{aligned}
&+\frac{48 i}{L^{6}} \varepsilon^{ir_{6}} \bar\varphi^{j_{6}} \bar\varphi_{k_{6}} \varphi_{l_{6}} L^{k_{6}l_{6}} L_{r_{6}j_{6}} \gamma^{q_{7}} L_{ij_{7}} \mathcal D_{q_{7}}\!\left(\chi^{j_{7}}\right)\qquad\text{(4.85; G3)}\\
&- \frac{12 i}{L^{7}} \varepsilon^{ir_{6}} \bar\varphi^{j_{6}} \bar\varphi_{k_{6}} \varphi_{l_{6}} L^{k_{6}l_{6}} L_{r_{6}j_{6}} \gamma^{q_{7}} (\mathcal D_{q_{7}}L) \gamma\!\cdot\!T \varphi_{i}\qquad\text{(4.86; G3)}\\
&+\frac{12 i}{L^{6}} \varepsilon^{ir_{6}} \bar\varphi^{j_{6}} \bar\varphi_{k_{6}} \varphi_{l_{6}} L^{k_{6}l_{6}} L_{r_{6}j_{6}} \gamma^{q_{7}} \gamma\!\cdot\!T \mathcal D_{q_{7}}\!\left(\varphi_{i}\right)\qquad\text{(4.87; G3)}\\
&+\frac{18 i N}{L^{9}} \varepsilon^{ir_{6}} \bar\varphi^{j_{6}} \bar\varphi_{k_{6}} \varphi_{l_{6}} L^{k_{6}l_{6}} L_{r_{6}j_{6}} \gamma^{q_{7}} (\mathcal D_{q_{7}}L) L_{ij_{7}} \varphi^{j_{7}}\qquad\text{(4.88; G3)}
\end{aligned}
\tag{196}
```

```math
\begin{aligned}
&- \frac{6 i}{L^{8}} \varepsilon^{ir_{6}} \bar\varphi^{j_{6}} \bar\varphi_{k_{6}} \varphi_{l_{6}} L^{k_{6}l_{6}} L_{r_{6}j_{6}} \gamma^{q_{7}} (\mathcal D_{q_{7}}N) L_{ij_{7}} \varphi^{j_{7}}\qquad\text{(4.89; G3)}\\
&- \frac{6 i N}{L^{8}} \varepsilon^{ir_{6}} \bar\varphi^{j_{6}} \bar\varphi_{k_{6}} \varphi_{l_{6}} L^{k_{6}l_{6}} L_{r_{6}j_{6}} \gamma^{q_{7}} \mathcal D_{q_{7}}\!\left(L_{ij_{7}}\right) \varphi^{j_{7}}\qquad\text{(4.90; G3)}\\
&- \frac{6 i N}{L^{8}} \varepsilon^{ir_{6}} \bar\varphi^{j_{6}} \bar\varphi_{k_{6}} \varphi_{l_{6}} L^{k_{6}l_{6}} L_{r_{6}j_{6}} \gamma^{q_{7}} L_{ij_{7}} \mathcal D_{q_{7}}\!\left(\varphi^{j_{7}}\right)\qquad\text{(4.91; G3)}\\
&+\frac{18}{L^{9}} \varepsilon^{ir_{6}} \bar\varphi^{j_{6}} \bar\varphi_{k_{6}} \varphi_{l_{6}} L^{k_{6}l_{6}} L_{r_{6}j_{6}} \gamma^{q_{7}} (\mathcal D_{q_{7}}L) (\not{\mathcal D}L_{ij_{7}}) L^{j_{7}k_{7}} \varphi_{k_{7}}\qquad\text{(4.92; G3)}
\end{aligned}
\tag{197}
```

```math
\begin{aligned}
&- \frac{6}{L^{8}} \varepsilon^{ir_{6}} \bar\varphi^{j_{6}} \bar\varphi_{k_{6}} \varphi_{l_{6}} L^{k_{6}l_{6}} L_{r_{6}j_{6}} \gamma^{q_{7}} \mathcal D_{q_{7}}\!\left((\not{\mathcal D}L_{ij_{7}})\right) L^{j_{7}k_{7}} \varphi_{k_{7}}\qquad\text{(4.93; G3)}\\
&- \frac{6}{L^{8}} \varepsilon^{ir_{6}} \bar\varphi^{j_{6}} \bar\varphi_{k_{6}} \varphi_{l_{6}} L^{k_{6}l_{6}} L_{r_{6}j_{6}} \gamma^{q_{7}} (\not{\mathcal D}L_{ij_{7}}) \mathcal D_{q_{7}}\!\left(L^{j_{7}k_{7}}\right) \varphi_{k_{7}}\qquad\text{(4.94; G3)}\\
&- \frac{6}{L^{8}} \varepsilon^{ir_{6}} \bar\varphi^{j_{6}} \bar\varphi_{k_{6}} \varphi_{l_{6}} L^{k_{6}l_{6}} L_{r_{6}j_{6}} \gamma^{q_{7}} (\not{\mathcal D}L_{ij_{7}}) L^{j_{7}k_{7}} \mathcal D_{q_{7}}\!\left(\varphi_{k_{7}}\right)\qquad\text{(4.95; G3)}\\
&- \frac{18}{L^{9}} \varepsilon^{ir_{6}} \bar\varphi^{j_{6}} \bar\varphi_{k_{6}} \varphi_{l_{6}} L^{k_{6}l_{6}} L_{r_{6}j_{6}} \gamma^{q_{7}} (\mathcal D_{q_{7}}L) \not E L_{ij_{7}} \varphi^{j_{7}}\qquad\text{(4.96; G3)}
\end{aligned}
\tag{198}
```

```math
\begin{aligned}
&+\frac{6}{L^{8}} \varepsilon^{ir_{6}} \bar\varphi^{j_{6}} \bar\varphi_{k_{6}} \varphi_{l_{6}} L^{k_{6}l_{6}} L_{r_{6}j_{6}} \gamma^{q_{7}} \mathcal D_{q_{7}}\!\left(\not E\right) L_{ij_{7}} \varphi^{j_{7}}\qquad\text{(4.97; G3)}\\
&+\frac{6}{L^{8}} \varepsilon^{ir_{6}} \bar\varphi^{j_{6}} \bar\varphi_{k_{6}} \varphi_{l_{6}} L^{k_{6}l_{6}} L_{r_{6}j_{6}} \gamma^{q_{7}} \not E \mathcal D_{q_{7}}\!\left(L_{ij_{7}}\right) \varphi^{j_{7}}\qquad\text{(4.98; G3)}\\
&+\frac{6}{L^{8}} \varepsilon^{ir_{6}} \bar\varphi^{j_{6}} \bar\varphi_{k_{6}} \varphi_{l_{6}} L^{k_{6}l_{6}} L_{r_{6}j_{6}} \gamma^{q_{7}} \not E L_{ij_{7}} \mathcal D_{q_{7}}\!\left(\varphi^{j_{7}}\right)\qquad\text{(4.99; G3)}\\
&+\frac{12 i}{L^{6}} \varepsilon^{ir_{6}} \bar\varphi^{j_{6}} \bar\varphi_{k_{6}} \varphi_{l_{6}} L^{k_{6}l_{6}} L_{r_{6}j_{6}} \gamma^{q_{7}} \gamma^{mn}(\mathcal D_{q_{7}}T_{mn}) \varphi_{i}\qquad\text{(4.100; G3)}
\end{aligned}
\tag{199}
```

```math
\begin{aligned}
&+\frac{4 i}{L^{4}} \varepsilon^{ir_{8}} (\mathcal D_{d_{8}}\bar\varphi_{r_{8}}) \gamma^{d_{8}} \gamma\cdot T \varphi^{j_{10}} \bar\varphi_{i} \varphi_{j_{10}}\qquad\text{(4.101; G4)}\\
&- \frac{12 i}{L^{6}} \varepsilon^{ir_{8}} (\mathcal D_{d_{8}}\bar\varphi_{r_{8}}) \gamma^{d_{8}} \gamma\cdot T \varphi^{j_{10}} \bar\varphi_{k_{10}} \varphi_{l_{10}} L^{k_{10}l_{10}} L_{ij_{10}}\qquad\text{(4.102; G4)}\\
&- \frac{32}{L^{4}} \varepsilon^{ir_{8}} L_{r_{8}j_{8}} \bar\chi^{j_{8}} \gamma\cdot T \varphi^{j_{10}} \bar\varphi_{i} \varphi_{j_{10}}\qquad\text{(4.103; G4)}\\
&+\frac{96}{L^{6}} \varepsilon^{ir_{8}} L_{r_{8}j_{8}} \bar\chi^{j_{8}} \gamma\cdot T \varphi^{j_{10}} \bar\varphi_{k_{10}} \varphi_{l_{10}} L^{k_{10}l_{10}} L_{ij_{10}}\qquad\text{(4.104; G4)}
\end{aligned}
\tag{200}
```

```math
\begin{aligned}
&+\frac{8}{L^{4}} \varepsilon^{ir_{8}} \bar\varphi_{r_{8}} \gamma\!\cdot\!T \gamma\cdot T \varphi^{j_{10}} \bar\varphi_{i} \varphi_{j_{10}}\qquad\text{(4.105; G4)}\\
&- \frac{24}{L^{6}} \varepsilon^{ir_{8}} \bar\varphi_{r_{8}} \gamma\!\cdot\!T \gamma\cdot T \varphi^{j_{10}} \bar\varphi_{k_{10}} \varphi_{l_{10}} L^{k_{10}l_{10}} L_{ij_{10}}\qquad\text{(4.106; G4)}\\
&+\frac{4 N}{L^{6}} \varepsilon^{ir_{8}} L_{r_{8}j_{8}} \bar\varphi^{j_{8}} \gamma\cdot T \varphi^{j_{10}} \bar\varphi_{i} \varphi_{j_{10}}\qquad\text{(4.107; G4)}\\
&- \frac{12 N}{L^{8}} \varepsilon^{ir_{8}} L_{r_{8}j_{8}} \bar\varphi^{j_{8}} \gamma\cdot T \varphi^{j_{10}} \bar\varphi_{k_{10}} \varphi_{l_{10}} L^{k_{10}l_{10}} L_{ij_{10}}\qquad\text{(4.108; G4)}
\end{aligned}
\tag{201}
```

```math
\begin{aligned}
&- \frac{4 i}{L^{6}} \varepsilon^{ir_{8}} L^{j_{8}k_{8}} \bar\varphi_{k_{8}} (\not{\mathcal D}L_{r_{8}j_{8}}) \gamma\cdot T \varphi^{j_{10}} \bar\varphi_{i} \varphi_{j_{10}}\qquad\text{(4.109; G4)}\\
&+\frac{12 i}{L^{8}} \varepsilon^{ir_{8}} L^{j_{8}k_{8}} \bar\varphi_{k_{8}} (\not{\mathcal D}L_{r_{8}j_{8}}) \gamma\cdot T \varphi^{j_{10}} \bar\varphi_{k_{10}} \varphi_{l_{10}} L^{k_{10}l_{10}} L_{ij_{10}}\qquad\text{(4.110; G4)}\\
&+\frac{4 i}{L^{6}} \varepsilon^{ir_{8}} L_{r_{8}j_{8}} \bar\varphi^{j_{8}} \not E \gamma\cdot T \varphi^{j_{10}} \bar\varphi_{i} \varphi_{j_{10}}\qquad\text{(4.111; G4)}\\
&- \frac{12 i}{L^{8}} \varepsilon^{ir_{8}} L_{r_{8}j_{8}} \bar\varphi^{j_{8}} \not E \gamma\cdot T \varphi^{j_{10}} \bar\varphi_{k_{10}} \varphi_{l_{10}} L^{k_{10}l_{10}} L_{ij_{10}}\qquad\text{(4.112; G4)}
\end{aligned}
\tag{202}
```

```math
\begin{aligned}
&+\frac{4 i}{L^{4}} \varepsilon^{ir_{8}} \bar\varphi^{j_{8}} \bar\varphi_{r_{8}} \varphi_{j_{8}} \gamma\cdot T \not{\mathcal D}\varphi_{i}\qquad\text{(4.113; G4)}\\
&- \frac{32}{L^{4}} \varepsilon^{ir_{8}} \bar\varphi^{j_{8}} \bar\varphi_{r_{8}} \varphi_{j_{8}} \gamma\cdot T L_{ij_{10}} \chi^{j_{10}}\qquad\text{(4.114; G4)}\\
&- \frac{8}{L^{4}} \varepsilon^{ir_{8}} \bar\varphi^{j_{8}} \bar\varphi_{r_{8}} \varphi_{j_{8}} \gamma\cdot T \gamma\!\cdot\!T \varphi_{i}\qquad\text{(4.115; G4)}\\
&+\frac{4 N}{L^{6}} \varepsilon^{ir_{8}} \bar\varphi^{j_{8}} \bar\varphi_{r_{8}} \varphi_{j_{8}} \gamma\cdot T L_{ij_{10}} \varphi^{j_{10}}\qquad\text{(4.116; G4)}
\end{aligned}
\tag{203}
```

```math
\begin{aligned}
&- \frac{4 i}{L^{6}} \varepsilon^{ir_{8}} \bar\varphi^{j_{8}} \bar\varphi_{r_{8}} \varphi_{j_{8}} \gamma\cdot T (\not{\mathcal D}L_{ij_{10}}) L^{j_{10}k_{10}} \varphi_{k_{10}}\qquad\text{(4.117; G4)}\\
&+\frac{4 i}{L^{6}} \varepsilon^{ir_{8}} \bar\varphi^{j_{8}} \bar\varphi_{r_{8}} \varphi_{j_{8}} \gamma\cdot T \not E L_{ij_{10}} \varphi^{j_{10}}\qquad\text{(4.118; G4)}\\
&- \frac{12 i}{L^{6}} \varepsilon^{ir_{8}} \bar\varphi^{j_{8}} \bar\varphi_{k_{8}} \varphi_{l_{8}} L^{k_{8}l_{8}} L_{r_{8}j_{8}} \gamma\cdot T \not{\mathcal D}\varphi_{i}\qquad\text{(4.119; G4)}\\
&+\frac{96}{L^{6}} \varepsilon^{ir_{8}} \bar\varphi^{j_{8}} \bar\varphi_{k_{8}} \varphi_{l_{8}} L^{k_{8}l_{8}} L_{r_{8}j_{8}} \gamma\cdot T L_{ij_{10}} \chi^{j_{10}}\qquad\text{(4.120; G4)}
\end{aligned}
\tag{204}
```

```math
\begin{aligned}
&+\frac{24}{L^{6}} \varepsilon^{ir_{8}} \bar\varphi^{j_{8}} \bar\varphi_{k_{8}} \varphi_{l_{8}} L^{k_{8}l_{8}} L_{r_{8}j_{8}} \gamma\cdot T \gamma\!\cdot\!T \varphi_{i}\qquad\text{(4.121; G4)}\\
&- \frac{12 N}{L^{8}} \varepsilon^{ir_{8}} \bar\varphi^{j_{8}} \bar\varphi_{k_{8}} \varphi_{l_{8}} L^{k_{8}l_{8}} L_{r_{8}j_{8}} \gamma\cdot T L_{ij_{10}} \varphi^{j_{10}}\qquad\text{(4.122; G4)}\\
&+\frac{12 i}{L^{8}} \varepsilon^{ir_{8}} \bar\varphi^{j_{8}} \bar\varphi_{k_{8}} \varphi_{l_{8}} L^{k_{8}l_{8}} L_{r_{8}j_{8}} \gamma\cdot T (\not{\mathcal D}L_{ij_{10}}) L^{j_{10}k_{10}} \varphi_{k_{10}}\qquad\text{(4.123; G4)}\\
&- \frac{12 i}{L^{8}} \varepsilon^{ir_{8}} \bar\varphi^{j_{8}} \bar\varphi_{k_{8}} \varphi_{l_{8}} L^{k_{8}l_{8}} L_{r_{8}j_{8}} \gamma\cdot T \not E L_{ij_{10}} \varphi^{j_{10}}\qquad\text{(4.124; G4)}
\end{aligned}
\tag{205}
```

```math
\begin{aligned}
&+\frac{32 N}{L^{4}} \varepsilon^{ir_{12}} \bar\varphi^{j_{12}} \bar\varphi_{r_{12}} \varphi_{j_{12}} \chi_i\qquad\text{(4.125; G5)}\\
&- \frac{96 N}{L^{6}} \varepsilon^{ir_{12}} \bar\varphi^{j_{12}} \bar\varphi_{k_{12}} \varphi_{l_{12}} L^{k_{12}l_{12}} L_{r_{12}j_{12}} \chi_i\qquad\text{(4.126; G5)}\\
&- \frac{16 i}{L^{4}} L_{r_11s_11} \bar\varphi^{r_11} \varphi^{s_11} \varepsilon^{ir_{12}} (\mathcal D_{d_{12}}\bar\varphi_{r_{12}}) \gamma^{d_{12}} \chi_i\qquad\text{(4.127; G5)}\\
&+\frac{128}{L^{4}} L_{r_11s_11} \bar\varphi^{r_11} \varphi^{s_11} \varepsilon^{ir_{12}} L_{r_{12}j_{12}} \bar\chi^{j_{12}} \chi_i\qquad\text{(4.128; G5)}
\end{aligned}
\tag{206}
```

```math
\begin{aligned}
&- \frac{32}{L^{4}} L_{r_11s_11} \bar\varphi^{r_11} \varphi^{s_11} \varepsilon^{ir_{12}} \bar\varphi_{r_{12}} \gamma\!\cdot\!T \chi_i\qquad\text{(4.129; G5)}\\
&- \frac{16 N}{L^{6}} L_{r_11s_11} \bar\varphi^{r_11} \varphi^{s_11} \varepsilon^{ir_{12}} L_{r_{12}j_{12}} \bar\varphi^{j_{12}} \chi_i\qquad\text{(4.130; G5)}\\
&+\frac{16 i}{L^{6}} L_{r_11s_11} \bar\varphi^{r_11} \varphi^{s_11} \varepsilon^{ir_{12}} L^{j_{12}k_{12}} \bar\varphi_{k_{12}} (\not{\mathcal D}L_{r_{12}j_{12}}) \chi_i\qquad\text{(4.131; G5)}\\
&- \frac{16 i}{L^{6}} L_{r_11s_11} \bar\varphi^{r_11} \varphi^{s_11} \varepsilon^{ir_{12}} L_{r_{12}j_{12}} \bar\varphi^{j_{12}} \not E \chi_i\qquad\text{(4.132; G5)}
\end{aligned}
\tag{207}
```

```math
\begin{aligned}
&- \frac{i}{2 L^{4}} \varepsilon^{ir_{14}} (\mathcal D_{d_{14}}\bar\varphi_{r_{14}}) \gamma^{d_{14}} \gamma\cdot\widehat G \varphi^{j_{16}} \bar\varphi_{i} \varphi_{j_{16}}\qquad\text{(4.133; G6)}\\
&+\frac{3 i}{2 L^{6}} \varepsilon^{ir_{14}} (\mathcal D_{d_{14}}\bar\varphi_{r_{14}}) \gamma^{d_{14}} \gamma\cdot\widehat G \varphi^{j_{16}} \bar\varphi_{k_{16}} \varphi_{l_{16}} L^{k_{16}l_{16}} L_{ij_{16}}\qquad\text{(4.134; G6)}\\
&+\frac{4}{L^{4}} \varepsilon^{ir_{14}} L_{r_{14}j_{14}} \bar\chi^{j_{14}} \gamma\cdot\widehat G \varphi^{j_{16}} \bar\varphi_{i} \varphi_{j_{16}}\qquad\text{(4.135; G6)}\\
&- \frac{12}{L^{6}} \varepsilon^{ir_{14}} L_{r_{14}j_{14}} \bar\chi^{j_{14}} \gamma\cdot\widehat G \varphi^{j_{16}} \bar\varphi_{k_{16}} \varphi_{l_{16}} L^{k_{16}l_{16}} L_{ij_{16}}\qquad\text{(4.136; G6)}
\end{aligned}
\tag{208}
```

```math
\begin{aligned}
&- \frac{1}{L^{4}} \varepsilon^{ir_{14}} \bar\varphi_{r_{14}} \gamma\!\cdot\!T \gamma\cdot\widehat G \varphi^{j_{16}} \bar\varphi_{i} \varphi_{j_{16}}\qquad\text{(4.137; G6)}\\
&+\frac{3}{L^{6}} \varepsilon^{ir_{14}} \bar\varphi_{r_{14}} \gamma\!\cdot\!T \gamma\cdot\widehat G \varphi^{j_{16}} \bar\varphi_{k_{16}} \varphi_{l_{16}} L^{k_{16}l_{16}} L_{ij_{16}}\qquad\text{(4.138; G6)}\\
&- \frac{N}{2 L^{6}} \varepsilon^{ir_{14}} L_{r_{14}j_{14}} \bar\varphi^{j_{14}} \gamma\cdot\widehat G \varphi^{j_{16}} \bar\varphi_{i} \varphi_{j_{16}}\qquad\text{(4.139; G6)}\\
&+\frac{3 N}{2 L^{8}} \varepsilon^{ir_{14}} L_{r_{14}j_{14}} \bar\varphi^{j_{14}} \gamma\cdot\widehat G \varphi^{j_{16}} \bar\varphi_{k_{16}} \varphi_{l_{16}} L^{k_{16}l_{16}} L_{ij_{16}}\qquad\text{(4.140; G6)}
\end{aligned}
\tag{209}
```

```math
\begin{aligned}
&+\frac{i}{2 L^{6}} \varepsilon^{ir_{14}} L^{j_{14}k_{14}} \bar\varphi_{k_{14}} (\not{\mathcal D}L_{r_{14}j_{14}}) \gamma\cdot\widehat G \varphi^{j_{16}} \bar\varphi_{i} \varphi_{j_{16}}\qquad\text{(4.141; G6)}\\
&- \frac{3 i}{2 L^{8}} \varepsilon^{ir_{14}} L^{j_{14}k_{14}} \bar\varphi_{k_{14}} (\not{\mathcal D}L_{r_{14}j_{14}}) \gamma\cdot\widehat G \varphi^{j_{16}} \bar\varphi_{k_{16}} \varphi_{l_{16}} L^{k_{16}l_{16}} L_{ij_{16}}\qquad\text{(4.142; G6)}\\
&- \frac{i}{2 L^{6}} \varepsilon^{ir_{14}} L_{r_{14}j_{14}} \bar\varphi^{j_{14}} \not E \gamma\cdot\widehat G \varphi^{j_{16}} \bar\varphi_{i} \varphi_{j_{16}}\qquad\text{(4.143; G6)}\\
&+\frac{3 i}{2 L^{8}} \varepsilon^{ir_{14}} L_{r_{14}j_{14}} \bar\varphi^{j_{14}} \not E \gamma\cdot\widehat G \varphi^{j_{16}} \bar\varphi_{k_{16}} \varphi_{l_{16}} L^{k_{16}l_{16}} L_{ij_{16}}\qquad\text{(4.144; G6)}
\end{aligned}
\tag{210}
```

```math
\begin{aligned}
&- \frac{i}{2 L^{4}} \varepsilon^{ir_{14}} \bar\varphi^{j_{14}} \bar\varphi_{r_{14}} \varphi_{j_{14}} \gamma\cdot\widehat G \not{\mathcal D}\varphi_{i}\qquad\text{(4.145; G6)}\\
&+\frac{4}{L^{4}} \varepsilon^{ir_{14}} \bar\varphi^{j_{14}} \bar\varphi_{r_{14}} \varphi_{j_{14}} \gamma\cdot\widehat G L_{ij_{16}} \chi^{j_{16}}\qquad\text{(4.146; G6)}\\
&+\frac{1}{L^{4}} \varepsilon^{ir_{14}} \bar\varphi^{j_{14}} \bar\varphi_{r_{14}} \varphi_{j_{14}} \gamma\cdot\widehat G \gamma\!\cdot\!T \varphi_{i}\qquad\text{(4.147; G6)}\\
&- \frac{N}{2 L^{6}} \varepsilon^{ir_{14}} \bar\varphi^{j_{14}} \bar\varphi_{r_{14}} \varphi_{j_{14}} \gamma\cdot\widehat G L_{ij_{16}} \varphi^{j_{16}}\qquad\text{(4.148; G6)}
\end{aligned}
\tag{211}
```

```math
\begin{aligned}
&+\frac{i}{2 L^{6}} \varepsilon^{ir_{14}} \bar\varphi^{j_{14}} \bar\varphi_{r_{14}} \varphi_{j_{14}} \gamma\cdot\widehat G (\not{\mathcal D}L_{ij_{16}}) L^{j_{16}k_{16}} \varphi_{k_{16}}\qquad\text{(4.149; G6)}\\
&- \frac{i}{2 L^{6}} \varepsilon^{ir_{14}} \bar\varphi^{j_{14}} \bar\varphi_{r_{14}} \varphi_{j_{14}} \gamma\cdot\widehat G \not E L_{ij_{16}} \varphi^{j_{16}}\qquad\text{(4.150; G6)}\\
&+\frac{3 i}{2 L^{6}} \varepsilon^{ir_{14}} \bar\varphi^{j_{14}} \bar\varphi_{k_{14}} \varphi_{l_{14}} L^{k_{14}l_{14}} L_{r_{14}j_{14}} \gamma\cdot\widehat G \not{\mathcal D}\varphi_{i}\qquad\text{(4.151; G6)}\\
&- \frac{12}{L^{6}} \varepsilon^{ir_{14}} \bar\varphi^{j_{14}} \bar\varphi_{k_{14}} \varphi_{l_{14}} L^{k_{14}l_{14}} L_{r_{14}j_{14}} \gamma\cdot\widehat G L_{ij_{16}} \chi^{j_{16}}\qquad\text{(4.152; G6)}
\end{aligned}
\tag{212}
```

```math
\begin{aligned}
&- \frac{3}{L^{6}} \varepsilon^{ir_{14}} \bar\varphi^{j_{14}} \bar\varphi_{k_{14}} \varphi_{l_{14}} L^{k_{14}l_{14}} L_{r_{14}j_{14}} \gamma\cdot\widehat G \gamma\!\cdot\!T \varphi_{i}\qquad\text{(4.153; G6)}\\
&+\frac{3 N}{2 L^{8}} \varepsilon^{ir_{14}} \bar\varphi^{j_{14}} \bar\varphi_{k_{14}} \varphi_{l_{14}} L^{k_{14}l_{14}} L_{r_{14}j_{14}} \gamma\cdot\widehat G L_{ij_{16}} \varphi^{j_{16}}\qquad\text{(4.154; G6)}\\
&- \frac{3 i}{2 L^{8}} \varepsilon^{ir_{14}} \bar\varphi^{j_{14}} \bar\varphi_{k_{14}} \varphi_{l_{14}} L^{k_{14}l_{14}} L_{r_{14}j_{14}} \gamma\cdot\widehat G (\not{\mathcal D}L_{ij_{16}}) L^{j_{16}k_{16}} \varphi_{k_{16}}\qquad\text{(4.155; G6)}\\
&+\frac{3 i}{2 L^{8}} \varepsilon^{ir_{14}} \bar\varphi^{j_{14}} \bar\varphi_{k_{14}} \varphi_{l_{14}} L^{k_{14}l_{14}} L_{r_{14}j_{14}} \gamma\cdot\widehat G \not E L_{ij_{16}} \varphi^{j_{16}}\qquad\text{(4.156; G6)}
\end{aligned}
\tag{213}
```

```math
\begin{aligned}
&+\frac{i g}{L^{4}} \varepsilon^{ir_{17}} (\mathcal D_{d_{17}}\bar\varphi_{r_{17}}) \gamma^{d_{17}} L_{ij} \varepsilon^{jr_{19}} \varphi^{j_{19}} \bar\varphi_{r_{19}} \varphi_{j_{19}}\qquad\text{(4.157; G7)}\\
&- \frac{3 i g}{L^{6}} \varepsilon^{ir_{17}} (\mathcal D_{d_{17}}\bar\varphi_{r_{17}}) \gamma^{d_{17}} L_{ij} \varepsilon^{jr_{19}} \varphi^{j_{19}} \bar\varphi_{k_{19}} \varphi_{l_{19}} L^{k_{19}l_{19}} L_{r_{19}j_{19}}\qquad\text{(4.158; G7)}\\
&- \frac{8 g}{L^{4}} \varepsilon^{ir_{17}} L_{r_{17}j_{17}} \bar\chi^{j_{17}} L_{ij} \varepsilon^{jr_{19}} \varphi^{j_{19}} \bar\varphi_{r_{19}} \varphi_{j_{19}}\qquad\text{(4.159; G7)}\\
&+\frac{24 g}{L^{6}} \varepsilon^{ir_{17}} L_{r_{17}j_{17}} \bar\chi^{j_{17}} L_{ij} \varepsilon^{jr_{19}} \varphi^{j_{19}} \bar\varphi_{k_{19}} \varphi_{l_{19}} L^{k_{19}l_{19}} L_{r_{19}j_{19}}\qquad\text{(4.160; G7)}
\end{aligned}
\tag{214}
```

```math
\begin{aligned}
&+\frac{2 g}{L^{4}} \varepsilon^{ir_{17}} \bar\varphi_{r_{17}} \gamma\!\cdot\!T L_{ij} \varepsilon^{jr_{19}} \varphi^{j_{19}} \bar\varphi_{r_{19}} \varphi_{j_{19}}\qquad\text{(4.161; G7)}\\
&- \frac{6 g}{L^{6}} \varepsilon^{ir_{17}} \bar\varphi_{r_{17}} \gamma\!\cdot\!T L_{ij} \varepsilon^{jr_{19}} \varphi^{j_{19}} \bar\varphi_{k_{19}} \varphi_{l_{19}} L^{k_{19}l_{19}} L_{r_{19}j_{19}}\qquad\text{(4.162; G7)}\\
&+\frac{N g}{L^{6}} \varepsilon^{ir_{17}} L_{r_{17}j_{17}} \bar\varphi^{j_{17}} L_{ij} \varepsilon^{jr_{19}} \varphi^{j_{19}} \bar\varphi_{r_{19}} \varphi_{j_{19}}\qquad\text{(4.163; G7)}\\
&- \frac{3 N g}{L^{8}} \varepsilon^{ir_{17}} L_{r_{17}j_{17}} \bar\varphi^{j_{17}} L_{ij} \varepsilon^{jr_{19}} \varphi^{j_{19}} \bar\varphi_{k_{19}} \varphi_{l_{19}} L^{k_{19}l_{19}} L_{r_{19}j_{19}}\qquad\text{(4.164; G7)}
\end{aligned}
\tag{215}
```

```math
\begin{aligned}
&- \frac{i g}{L^{6}} \varepsilon^{ir_{17}} L^{j_{17}k_{17}} \bar\varphi_{k_{17}} (\not{\mathcal D}L_{r_{17}j_{17}}) L_{ij} \varepsilon^{jr_{19}} \varphi^{j_{19}} \bar\varphi_{r_{19}} \varphi_{j_{19}}\qquad\text{(4.165; G7)}\\
&+\frac{3 i g}{L^{8}} \varepsilon^{ir_{17}} L^{j_{17}k_{17}} \bar\varphi_{k_{17}} (\not{\mathcal D}L_{r_{17}j_{17}}) L_{ij} \varepsilon^{jr_{19}} \varphi^{j_{19}} \bar\varphi_{k_{19}} \varphi_{l_{19}} L^{k_{19}l_{19}} L_{r_{19}j_{19}}\qquad\text{(4.166; G7)}\\
&+\frac{i g}{L^{6}} \varepsilon^{ir_{17}} L_{r_{17}j_{17}} \bar\varphi^{j_{17}} \not E L_{ij} \varepsilon^{jr_{19}} \varphi^{j_{19}} \bar\varphi_{r_{19}} \varphi_{j_{19}}\qquad\text{(4.167; G7)}\\
&- \frac{3 i g}{L^{8}} \varepsilon^{ir_{17}} L_{r_{17}j_{17}} \bar\varphi^{j_{17}} \not E L_{ij} \varepsilon^{jr_{19}} \varphi^{j_{19}} \bar\varphi_{k_{19}} \varphi_{l_{19}} L^{k_{19}l_{19}} L_{r_{19}j_{19}}\qquad\text{(4.168; G7)}
\end{aligned}
\tag{216}
```

```math
\begin{aligned}
&+\frac{i g}{L^{4}} \varepsilon^{ir_{17}} \bar\varphi^{j_{17}} \bar\varphi_{r_{17}} \varphi_{j_{17}} L_{ij} \varepsilon^{jr_{19}} \not{\mathcal D}\varphi_{r_{19}}\qquad\text{(4.169; G7)}\\
&- \frac{8 g}{L^{4}} \varepsilon^{ir_{17}} \bar\varphi^{j_{17}} \bar\varphi_{r_{17}} \varphi_{j_{17}} L_{ij} \varepsilon^{jr_{19}} L_{r_{19}j_{19}} \chi^{j_{19}}\qquad\text{(4.170; G7)}\\
&- \frac{2 g}{L^{4}} \varepsilon^{ir_{17}} \bar\varphi^{j_{17}} \bar\varphi_{r_{17}} \varphi_{j_{17}} L_{ij} \varepsilon^{jr_{19}} \gamma\!\cdot\!T \varphi_{r_{19}}\qquad\text{(4.171; G7)}\\
&+\frac{N g}{L^{6}} \varepsilon^{ir_{17}} \bar\varphi^{j_{17}} \bar\varphi_{r_{17}} \varphi_{j_{17}} L_{ij} \varepsilon^{jr_{19}} L_{r_{19}j_{19}} \varphi^{j_{19}}\qquad\text{(4.172; G7)}
\end{aligned}
\tag{217}
```

```math
\begin{aligned}
&- \frac{i g}{L^{6}} \varepsilon^{ir_{17}} \bar\varphi^{j_{17}} \bar\varphi_{r_{17}} \varphi_{j_{17}} L_{ij} \varepsilon^{jr_{19}} (\not{\mathcal D}L_{r_{19}j_{19}}) L^{j_{19}k_{19}} \varphi_{k_{19}}\qquad\text{(4.173; G7)}\\
&+\frac{i g}{L^{6}} \varepsilon^{ir_{17}} \bar\varphi^{j_{17}} \bar\varphi_{r_{17}} \varphi_{j_{17}} L_{ij} \varepsilon^{jr_{19}} \not E L_{r_{19}j_{19}} \varphi^{j_{19}}\qquad\text{(4.174; G7)}\\
&- \frac{3 i g}{L^{6}} \varepsilon^{ir_{17}} \bar\varphi^{j_{17}} \bar\varphi_{k_{17}} \varphi_{l_{17}} L^{k_{17}l_{17}} L_{r_{17}j_{17}} L_{ij} \varepsilon^{jr_{19}} \not{\mathcal D}\varphi_{r_{19}}\qquad\text{(4.175; G7)}\\
&+\frac{24 g}{L^{6}} \varepsilon^{ir_{17}} \bar\varphi^{j_{17}} \bar\varphi_{k_{17}} \varphi_{l_{17}} L^{k_{17}l_{17}} L_{r_{17}j_{17}} L_{ij} \varepsilon^{jr_{19}} L_{r_{19}j_{19}} \chi^{j_{19}}\qquad\text{(4.176; G7)}
\end{aligned}
\tag{218}
```

```math
\begin{aligned}
&+\frac{6 g}{L^{6}} \varepsilon^{ir_{17}} \bar\varphi^{j_{17}} \bar\varphi_{k_{17}} \varphi_{l_{17}} L^{k_{17}l_{17}} L_{r_{17}j_{17}} L_{ij} \varepsilon^{jr_{19}} \gamma\!\cdot\!T \varphi_{r_{19}}\qquad\text{(4.177; G7)}\\
&- \frac{3 N g}{L^{8}} \varepsilon^{ir_{17}} \bar\varphi^{j_{17}} \bar\varphi_{k_{17}} \varphi_{l_{17}} L^{k_{17}l_{17}} L_{r_{17}j_{17}} L_{ij} \varepsilon^{jr_{19}} L_{r_{19}j_{19}} \varphi^{j_{19}}\qquad\text{(4.178; G7)}\\
&+\frac{3 i g}{L^{8}} \varepsilon^{ir_{17}} \bar\varphi^{j_{17}} \bar\varphi_{k_{17}} \varphi_{l_{17}} L^{k_{17}l_{17}} L_{r_{17}j_{17}} L_{ij} \varepsilon^{jr_{19}} (\not{\mathcal D}L_{r_{19}j_{19}}) L^{j_{19}k_{19}} \varphi_{k_{19}}\qquad\text{(4.179; G7)}\\
&- \frac{3 i g}{L^{8}} \varepsilon^{ir_{17}} \bar\varphi^{j_{17}} \bar\varphi_{k_{17}} \varphi_{l_{17}} L^{k_{17}l_{17}} L_{r_{17}j_{17}} L_{ij} \varepsilon^{jr_{19}} \not E L_{r_{19}j_{19}} \varphi^{j_{19}}\qquad\text{(4.180; G7)}
\end{aligned}
\tag{219}
```

```math
\begin{aligned}
&+\frac{i N g}{L^{4}} \bar\psi_a^i \gamma^a \varepsilon^{jr_{23}} \varphi^{j_{23}} \bar\varphi_{r_{23}} \varphi_{j_{23}} L_{ij}\qquad\text{(4.181; G8)}\\
&- \frac{3 i N g}{L^{6}} \bar\psi_a^i \gamma^a \varepsilon^{jr_{23}} \varphi^{j_{23}} \bar\varphi_{k_{23}} \varphi_{l_{23}} L^{k_{23}l_{23}} L_{r_{23}j_{23}} L_{ij}\qquad\text{(4.182; G8)}\\
&+\frac{g}{2 L^{4}} L_{r_20s_20} \bar\varphi^{r_20} \varphi^{s_20} \bar\psi_a^i \gamma^a \varepsilon^{jr_{23}} \not{\mathcal D}\varphi_{r_{23}} L_{ij}\qquad\text{(4.183; G8)}\\
&+\frac{4 i g}{L^{4}} L_{r_20s_20} \bar\varphi^{r_20} \varphi^{s_20} \bar\psi_a^i \gamma^a \varepsilon^{jr_{23}} L_{r_{23}j_{23}} \chi^{j_{23}} L_{ij}\qquad\text{(4.184; G8)}
\end{aligned}
\tag{220}
```

```math
\begin{aligned}
&+\frac{i g}{L^{4}} L_{r_20s_20} \bar\varphi^{r_20} \varphi^{s_20} \bar\psi_a^i \gamma^a \varepsilon^{jr_{23}} \gamma\!\cdot\!T \varphi_{r_{23}} L_{ij}\qquad\text{(4.185; G8)}\\
&- \frac{i N g}{2 L^{6}} L_{r_20s_20} \bar\varphi^{r_20} \varphi^{s_20} \bar\psi_a^i \gamma^a \varepsilon^{jr_{23}} L_{r_{23}j_{23}} \varphi^{j_{23}} L_{ij}\qquad\text{(4.186; G8)}\\
&- \frac{g}{2 L^{6}} L_{r_20s_20} \bar\varphi^{r_20} \varphi^{s_20} \bar\psi_a^i \gamma^a \varepsilon^{jr_{23}} (\not{\mathcal D}L_{r_{23}j_{23}}) L^{j_{23}k_{23}} \varphi_{k_{23}} L_{ij}\qquad\text{(4.187; G8)}\\
&+\frac{g}{2 L^{6}} L_{r_20s_20} \bar\varphi^{r_20} \varphi^{s_20} \bar\psi_a^i \gamma^a \varepsilon^{jr_{23}} \not E L_{r_{23}j_{23}} \varphi^{j_{23}} L_{ij}\qquad\text{(4.188; G8)}
\end{aligned}
\tag{221}
```

```math
\begin{aligned}
&- \frac{i}{L^{3}} \bar\psi_a^i \gamma^a \varepsilon^{jr_{27}} \varphi^{j_{27}} \bar\varphi_{r_{27}} \varphi_{j_{27}} Y'_{ij}\qquad\text{(4.189; G9)}\\
&+\frac{3 i}{L^{5}} \bar\psi_a^i \gamma^a \varepsilon^{jr_{27}} \varphi^{j_{27}} \bar\varphi_{k_{27}} \varphi_{l_{27}} L^{k_{27}l_{27}} L_{r_{27}j_{27}} Y'_{ij}\qquad\text{(4.190; G9)}\\
&- \frac{3 i N}{4 L^{4}} \varepsilon^{ir_{30}} \bar\varphi^{j_{30}} \bar\varphi_{r_{30}} \varphi_{j_{30}} \gamma^a \gamma\cdot\widehat G \psi_{ai}\qquad\text{(4.191; G10)}\\
&+\frac{9 i N}{4 L^{6}} \varepsilon^{ir_{30}} \bar\varphi^{j_{30}} \bar\varphi_{k_{30}} \varphi_{l_{30}} L^{k_{30}l_{30}} L_{r_{30}j_{30}} \gamma^a \gamma\cdot\widehat G \psi_{ai}\qquad\text{(4.192; G10)}
\end{aligned}
\tag{222}
```

```math
\begin{aligned}
&- \frac{3}{8 L^{4}} L_{r_29s_29} \bar\varphi^{r_29} \varphi^{s_29} \varepsilon^{ir_{30}} (\mathcal D_{d_{30}}\bar\varphi_{r_{30}}) \gamma^{d_{30}} \gamma^a \gamma\cdot\widehat G \psi_{ai}\qquad\text{(4.193; G10)}\\
&- \frac{3 i}{L^{4}} L_{r_29s_29} \bar\varphi^{r_29} \varphi^{s_29} \varepsilon^{ir_{30}} L_{r_{30}j_{30}} \bar\chi^{j_{30}} \gamma^a \gamma\cdot\widehat G \psi_{ai}\qquad\text{(4.194; G10)}\\
&+\frac{3 i}{4 L^{4}} L_{r_29s_29} \bar\varphi^{r_29} \varphi^{s_29} \varepsilon^{ir_{30}} \bar\varphi_{r_{30}} \gamma\!\cdot\!T \gamma^a \gamma\cdot\widehat G \psi_{ai}\qquad\text{(4.195; G10)}\\
&+\frac{3 i N}{8 L^{6}} L_{r_29s_29} \bar\varphi^{r_29} \varphi^{s_29} \varepsilon^{ir_{30}} L_{r_{30}j_{30}} \bar\varphi^{j_{30}} \gamma^a \gamma\cdot\widehat G \psi_{ai}\qquad\text{(4.196; G10)}
\end{aligned}
\tag{223}
```

```math
\begin{aligned}
&+\frac{3}{8 L^{6}} L_{r_29s_29} \bar\varphi^{r_29} \varphi^{s_29} \varepsilon^{ir_{30}} L^{j_{30}k_{30}} \bar\varphi_{k_{30}} (\not{\mathcal D}L_{r_{30}j_{30}}) \gamma^a \gamma\cdot\widehat G \psi_{ai}\qquad\text{(4.197; G10)}\\
&- \frac{3}{8 L^{6}} L_{r_29s_29} \bar\varphi^{r_29} \varphi^{s_29} \varepsilon^{ir_{30}} L_{r_{30}j_{30}} \bar\varphi^{j_{30}} \not E \gamma^a \gamma\cdot\widehat G \psi_{ai}\qquad\text{(4.198; G10)}\\
&+\frac{3 i N}{L^{4}} \varepsilon^{ir_{35}} \bar\varphi^{j_{35}} \bar\varphi_{r_{35}} \varphi_{j_{35}} \gamma^a \gamma\cdot T \psi_{ai}\qquad\text{(4.199; G10)}\\
&- \frac{9 i N}{L^{6}} \varepsilon^{ir_{35}} \bar\varphi^{j_{35}} \bar\varphi_{k_{35}} \varphi_{l_{35}} L^{k_{35}l_{35}} L_{r_{35}j_{35}} \gamma^a \gamma\cdot T \psi_{ai}\qquad\text{(4.200; G10)}
\end{aligned}
\tag{224}
```

```math
\begin{aligned}
&+\frac{3}{2 L^{4}} L_{r_34s_34} \bar\varphi^{r_34} \varphi^{s_34} \varepsilon^{ir_{35}} (\mathcal D_{d_{35}}\bar\varphi_{r_{35}}) \gamma^{d_{35}} \gamma^a \gamma\cdot T \psi_{ai}\qquad\text{(4.201; G10)}\\
&+\frac{12 i}{L^{4}} L_{r_34s_34} \bar\varphi^{r_34} \varphi^{s_34} \varepsilon^{ir_{35}} L_{r_{35}j_{35}} \bar\chi^{j_{35}} \gamma^a \gamma\cdot T \psi_{ai}\qquad\text{(4.202; G10)}\\
&- \frac{3 i}{L^{4}} L_{r_34s_34} \bar\varphi^{r_34} \varphi^{s_34} \varepsilon^{ir_{35}} \bar\varphi_{r_{35}} \gamma\!\cdot\!T \gamma^a \gamma\cdot T \psi_{ai}\qquad\text{(4.203; G10)}\\
&- \frac{3 i N}{2 L^{6}} L_{r_34s_34} \bar\varphi^{r_34} \varphi^{s_34} \varepsilon^{ir_{35}} L_{r_{35}j_{35}} \bar\varphi^{j_{35}} \gamma^a \gamma\cdot T \psi_{ai}\qquad\text{(4.204; G10)}
\end{aligned}
\tag{225}
```

```math
\begin{aligned}
&- \frac{3}{2 L^{6}} L_{r_34s_34} \bar\varphi^{r_34} \varphi^{s_34} \varepsilon^{ir_{35}} L^{j_{35}k_{35}} \bar\varphi_{k_{35}} (\not{\mathcal D}L_{r_{35}j_{35}}) \gamma^a \gamma\cdot T \psi_{ai}\qquad\text{(4.205; G10)}\\
&+\frac{3}{2 L^{6}} L_{r_34s_34} \bar\varphi^{r_34} \varphi^{s_34} \varepsilon^{ir_{35}} L_{r_{35}j_{35}} \bar\varphi^{j_{35}} \not E \gamma^a \gamma\cdot T \psi_{ai}\qquad\text{(4.206; G10)}\\
&- \frac{3 i N g}{2 L^{4}} \varepsilon^{ir_{40}} \bar\varphi^{j_{40}} \bar\varphi_{r_{40}} \varphi_{j_{40}} \gamma^a L_{ij} \psi_a^j\qquad\text{(4.207; G10)}\\
&+\frac{9 i N g}{2 L^{6}} \varepsilon^{ir_{40}} \bar\varphi^{j_{40}} \bar\varphi_{k_{40}} \varphi_{l_{40}} L^{k_{40}l_{40}} L_{r_{40}j_{40}} \gamma^a L_{ij} \psi_a^j\qquad\text{(4.208; G10)}
\end{aligned}
\tag{226}
```

```math
\begin{aligned}
&- \frac{3 g}{4 L^{4}} L_{r_39s_39} \bar\varphi^{r_39} \varphi^{s_39} \varepsilon^{ir_{40}} (\mathcal D_{d_{40}}\bar\varphi_{r_{40}}) \gamma^{d_{40}} \gamma^a L_{ij} \psi_a^j\qquad\text{(4.209; G10)}\\
&- \frac{6 i g}{L^{4}} L_{r_39s_39} \bar\varphi^{r_39} \varphi^{s_39} \varepsilon^{ir_{40}} L_{r_{40}j_{40}} \bar\chi^{j_{40}} \gamma^a L_{ij} \psi_a^j\qquad\text{(4.210; G10)}\\
&+\frac{3 i g}{2 L^{4}} L_{r_39s_39} \bar\varphi^{r_39} \varphi^{s_39} \varepsilon^{ir_{40}} \bar\varphi_{r_{40}} \gamma\!\cdot\!T \gamma^a L_{ij} \psi_a^j\qquad\text{(4.211; G10)}\\
&+\frac{3 i N g}{4 L^{6}} L_{r_39s_39} \bar\varphi^{r_39} \varphi^{s_39} \varepsilon^{ir_{40}} L_{r_{40}j_{40}} \bar\varphi^{j_{40}} \gamma^a L_{ij} \psi_a^j\qquad\text{(4.212; G10)}
\end{aligned}
\tag{227}
```

```math
\begin{aligned}
&+\frac{3 g}{4 L^{6}} L_{r_39s_39} \bar\varphi^{r_39} \varphi^{s_39} \varepsilon^{ir_{40}} L^{j_{40}k_{40}} \bar\varphi_{k_{40}} (\not{\mathcal D}L_{r_{40}j_{40}}) \gamma^a L_{ij} \psi_a^j\qquad\text{(4.213; G10)}\\
&- \frac{3 g}{4 L^{6}} L_{r_39s_39} \bar\varphi^{r_39} \varphi^{s_39} \varepsilon^{ir_{40}} L_{r_{40}j_{40}} \bar\varphi^{j_{40}} \not E \gamma^a L_{ij} \psi_a^j\qquad\text{(4.214; G10)}\\
&+\frac{3 i N}{L^{4}} \varepsilon^{ir_{45}} \bar\varphi^{j_{45}} \bar\varphi_{r_{45}} \varphi_{j_{45}} \gamma^a \phi_{ai}\qquad\text{(4.215; G10)}\\
&- \frac{9 i N}{L^{6}} \varepsilon^{ir_{45}} \bar\varphi^{j_{45}} \bar\varphi_{k_{45}} \varphi_{l_{45}} L^{k_{45}l_{45}} L_{r_{45}j_{45}} \gamma^a \phi_{ai}\qquad\text{(4.216; G10)}
\end{aligned}
\tag{228}
```

```math
\begin{aligned}
&+\frac{3}{2 L^{4}} L_{r_44s_44} \bar\varphi^{r_44} \varphi^{s_44} \varepsilon^{ir_{45}} (\mathcal D_{d_{45}}\bar\varphi_{r_{45}}) \gamma^{d_{45}} \gamma^a \phi_{ai}\qquad\text{(4.217; G10)}\\
&+\frac{12 i}{L^{4}} L_{r_44s_44} \bar\varphi^{r_44} \varphi^{s_44} \varepsilon^{ir_{45}} L_{r_{45}j_{45}} \bar\chi^{j_{45}} \gamma^a \phi_{ai}\qquad\text{(4.218; G10)}\\
&- \frac{3 i}{L^{4}} L_{r_44s_44} \bar\varphi^{r_44} \varphi^{s_44} \varepsilon^{ir_{45}} \bar\varphi_{r_{45}} \gamma\!\cdot\!T \gamma^a \phi_{ai}\qquad\text{(4.219; G10)}\\
&- \frac{3 i N}{2 L^{6}} L_{r_44s_44} \bar\varphi^{r_44} \varphi^{s_44} \varepsilon^{ir_{45}} L_{r_{45}j_{45}} \bar\varphi^{j_{45}} \gamma^a \phi_{ai}\qquad\text{(4.220; G10)}
\end{aligned}
\tag{229}
```

```math
\begin{aligned}
&- \frac{3}{2 L^{6}} L_{r_44s_44} \bar\varphi^{r_44} \varphi^{s_44} \varepsilon^{ir_{45}} L^{j_{45}k_{45}} \bar\varphi_{k_{45}} (\not{\mathcal D}L_{r_{45}j_{45}}) \gamma^a \phi_{ai}\qquad\text{(4.221; G10)}\\
&+\frac{3}{2 L^{6}} L_{r_44s_44} \bar\varphi^{r_44} \varphi^{s_44} \varepsilon^{ir_{45}} L_{r_{45}j_{45}} \bar\varphi^{j_{45}} \not E \gamma^a \phi_{ai}\qquad\text{(4.222; G10)}\\
&+\frac{1}{8 L^{3}} A'_a \varepsilon^{ir_{67}} \bar\varphi^{j_{67}} \bar\varphi_{r_{67}} \varphi_{j_{67}} \gamma^{ab} \gamma\cdot\widehat G \psi_{bi}\qquad\text{(4.223; G17)}\\
&- \frac{3}{8 L^{5}} A'_a \varepsilon^{ir_{67}} \bar\varphi^{j_{67}} \bar\varphi_{k_{67}} \varphi_{l_{67}} L^{k_{67}l_{67}} L_{r_{67}j_{67}} \gamma^{ab} \gamma\cdot\widehat G \psi_{bi}\qquad\text{(4.224; G17)}
\end{aligned}
\tag{230}
```

```math
\begin{aligned}
&- \frac{1}{2 L^{3}} A'_a \varepsilon^{ir_{72}} \bar\varphi^{j_{72}} \bar\varphi_{r_{72}} \varphi_{j_{72}} \gamma^{ab} \gamma\cdot T \psi_{bi}\qquad\text{(4.225; G17)}\\
&+\frac{3}{2 L^{5}} A'_a \varepsilon^{ir_{72}} \bar\varphi^{j_{72}} \bar\varphi_{k_{72}} \varphi_{l_{72}} L^{k_{72}l_{72}} L_{r_{72}j_{72}} \gamma^{ab} \gamma\cdot T \psi_{bi}\qquad\text{(4.226; G17)}\\
&+\frac{g}{4 L^{3}} A'_a \varepsilon^{ir_{77}} \bar\varphi^{j_{77}} \bar\varphi_{r_{77}} \varphi_{j_{77}} \gamma^{ab} L_{ij} \psi_b^j\qquad\text{(4.227; G17)}\\
&- \frac{3 g}{4 L^{5}} A'_a \varepsilon^{ir_{77}} \bar\varphi^{j_{77}} \bar\varphi_{k_{77}} \varphi_{l_{77}} L^{k_{77}l_{77}} L_{r_{77}j_{77}} \gamma^{ab} L_{ij} \psi_b^j\qquad\text{(4.228; G17)}
\end{aligned}
\tag{231}
```

```math
\begin{aligned}
&- \frac{1}{2 L^{3}} A'_a \varepsilon^{ir_{82}} \bar\varphi^{j_{82}} \bar\varphi_{r_{82}} \varphi_{j_{82}} \gamma^{ab} \phi_{bi}\qquad\text{(4.229; G17)}\\
&+\frac{3}{2 L^{5}} A'_a \varepsilon^{ir_{82}} \bar\varphi^{j_{82}} \bar\varphi_{k_{82}} \varphi_{l_{82}} L^{k_{82}l_{82}} L_{r_{82}j_{82}} \gamma^{ab} \phi_{bi}\qquad\text{(4.230; G17)}\\
&- \frac{i}{16 L^{3}} A'_a L_{r_86s_86} \bar\varphi^{r_86} \varphi^{s_86} \bar\psi_b^i \gamma^{ba} \gamma^c \gamma\cdot\widehat G \psi_{ci}\qquad\text{(4.231; G18)}\\
&+\frac{i}{4 L^{3}} A'_a L_{r_93s_93} \bar\varphi^{r_93} \varphi^{s_93} \bar\psi_b^i \gamma^{ba} \gamma^c \gamma\cdot T \psi_{ci}\qquad\text{(4.232; G18)}
\end{aligned}
\tag{232}
```

```math
\begin{aligned}
&- \frac{i g}{8 L^{3}} A'_a L_{r_100s_100} \bar\varphi^{r_100} \varphi^{s_100} \bar\psi_b^i \gamma^{ba} \gamma^c L_{ij} \psi_c^j\qquad\text{(4.233; G18)}\\
&+\frac{i}{4 L^{3}} A'_a L_{r_107s_107} \bar\varphi^{r_107} \varphi^{s_107} \bar\psi_b^i \gamma^{ba} \gamma^c \phi_{ci}\qquad\text{(4.234; G18)}\\
&+\frac{3 i}{2 L^{4}} A'_a \bar\psi_b^i \gamma^{ba} \gamma^{q_{115}} (\mathcal D_{q_{115}}L) \varphi^{j_{115}} \bar\varphi_{i} \varphi_{j_{115}}\qquad\text{(4.235; G19)}\\
&- \frac{i}{2 L^{3}} A'_a \bar\psi_b^i \gamma^{ba} \gamma^{q_{115}} \mathcal D_{q_{115}}\!\left(\varphi^{j_{115}}\right) \bar\varphi_{i} \varphi_{j_{115}}\qquad\text{(4.236; G19)}
\end{aligned}
\tag{233}
```

```math
\begin{aligned}
&- \frac{i}{2 L^{3}} A'_a \bar\psi_b^i \gamma^{ba} \gamma^{q_{115}} \varphi^{j_{115}} \mathcal D_{q_{115}}\!\left(\bar\varphi_{i}\right) \varphi_{j_{115}}\qquad\text{(4.237; G19)}\\
&- \frac{i}{2 L^{3}} A'_a \bar\psi_b^i \gamma^{ba} \gamma^{q_{115}} \varphi^{j_{115}} \bar\varphi_{i} \mathcal D_{q_{115}}\!\left(\varphi_{j_{115}}\right)\qquad\text{(4.238; G19)}\\
&- \frac{15 i}{2 L^{6}} A'_a \bar\psi_b^i \gamma^{ba} \gamma^{q_{115}} (\mathcal D_{q_{115}}L) \varphi^{j_{115}} \bar\varphi_{k_{115}} \varphi_{l_{115}} L^{k_{115}l_{115}} L_{ij_{115}}\qquad\text{(4.239; G19)}\\
&+\frac{3 i}{2 L^{5}} A'_a \bar\psi_b^i \gamma^{ba} \gamma^{q_{115}} \mathcal D_{q_{115}}\!\left(\varphi^{j_{115}}\right) \bar\varphi_{k_{115}} \varphi_{l_{115}} L^{k_{115}l_{115}} L_{ij_{115}}\qquad\text{(4.240; G19)}
\end{aligned}
\tag{234}
```

```math
\begin{aligned}
&+\frac{3 i}{2 L^{5}} A'_a \bar\psi_b^i \gamma^{ba} \gamma^{q_{115}} \varphi^{j_{115}} \mathcal D_{q_{115}}\!\left(\bar\varphi_{k_{115}}\right) \varphi_{l_{115}} L^{k_{115}l_{115}} L_{ij_{115}}\qquad\text{(4.241; G19)}\\
&+\frac{3 i}{2 L^{5}} A'_a \bar\psi_b^i \gamma^{ba} \gamma^{q_{115}} \varphi^{j_{115}} \bar\varphi_{k_{115}} \mathcal D_{q_{115}}\!\left(\varphi_{l_{115}}\right) L^{k_{115}l_{115}} L_{ij_{115}}\qquad\text{(4.242; G19)}\\
&+\frac{3 i}{2 L^{5}} A'_a \bar\psi_b^i \gamma^{ba} \gamma^{q_{115}} \varphi^{j_{115}} \bar\varphi_{k_{115}} \varphi_{l_{115}} \mathcal D_{q_{115}}\!\left(L^{k_{115}l_{115}}\right) L_{ij_{115}}\qquad\text{(4.243; G19)}\\
&+\frac{3 i}{2 L^{5}} A'_a \bar\psi_b^i \gamma^{ba} \gamma^{q_{115}} \varphi^{j_{115}} \bar\varphi_{k_{115}} \varphi_{l_{115}} L^{k_{115}l_{115}} \mathcal D_{q_{115}}\!\left(L_{ij_{115}}\right)\qquad\text{(4.244; G19)}
\end{aligned}
\tag{235}
```

```math
\begin{aligned}
&- \frac{1}{L^{3}} A'_a \bar\psi_b^i \gamma^{ba} \gamma\cdot T \varphi^{j_{120}} \bar\varphi_{i} \varphi_{j_{120}}\qquad\text{(4.245; G20)}\\
&+\frac{3}{L^{5}} A'_a \bar\psi_b^i \gamma^{ba} \gamma\cdot T \varphi^{j_{120}} \bar\varphi_{k_{120}} \varphi_{l_{120}} L^{k_{120}l_{120}} L_{ij_{120}}\qquad\text{(4.246; G20)}\\
&+\frac{4}{L^{3}} A'_a L_{r_122s_122} \bar\varphi^{r_122} \varphi^{s_122} \bar\psi_b^i \gamma^{ba} \chi_i\qquad\text{(4.247; G21)}\\
&+\frac{1}{8 L^{3}} A'_a \bar\psi_b^i \gamma^{ba} \gamma\cdot\widehat G \varphi^{j_{130}} \bar\varphi_{i} \varphi_{j_{130}}\qquad\text{(4.248; G22)}
\end{aligned}
\tag{236}
```

```math
\begin{aligned}
&- \frac{3}{8 L^{5}} A'_a \bar\psi_b^i \gamma^{ba} \gamma\cdot\widehat G \varphi^{j_{130}} \bar\varphi_{k_{130}} \varphi_{l_{130}} L^{k_{130}l_{130}} L_{ij_{130}}\qquad\text{(4.249; G22)}\\
&- \frac{g}{4 L^{3}} A'_a \bar\psi_b^i \gamma^{ba} L_{ij} \varepsilon^{jr_{135}} \varphi^{j_{135}} \bar\varphi_{r_{135}} \varphi_{j_{135}}\qquad\text{(4.250; G23)}\\
&+\frac{3 g}{4 L^{5}} A'_a \bar\psi_b^i \gamma^{ba} L_{ij} \varepsilon^{jr_{135}} \varphi^{j_{135}} \bar\varphi_{k_{135}} \varphi_{l_{135}} L^{k_{135}l_{135}} L_{r_{135}j_{135}}\qquad\text{(4.251; G23)}\\
&- \frac{i g}{8 L^{3}} A'_a L_{r_137s_137} \bar\varphi^{r_137} \varphi^{s_137} \bar\psi_b^i \gamma^{abc} \psi_c^j L_{ij}\qquad\text{(4.252; G24)}
\end{aligned}
\tag{237}
```

```math
\begin{aligned}
&- \frac{1}{2 L^{3}} L_{r_147s_147} \bar\varphi^{r_147} \varphi^{s_147} \Box_c\!\left(\frac{1}{L^{3}} L_{r_148s_148} \bar\varphi^{r_148} \varphi^{s_148}\right)\qquad\text{(4.253; G26)}\\
&- \frac{1}{L^{6}} L_{r_149s_149} \bar\varphi^{r_149} \varphi^{s_149} L_{r_10149s_10149} \bar\varphi^{r_10149} \varphi^{s_10149} f_a^a\qquad\text{(4.254; G27)}\\
&- \frac{4}{L^{6}} L_{r_154s_154} \bar\varphi^{r_154} \varphi^{s_154} L_{r_10154s_10154} \bar\varphi^{r_10154} \varphi^{s_10154} \widehat G_{ab} T^{ab}\qquad\text{(4.255; G29)}\\
&+\frac{4}{L^{6}} L_{r_160s_160} \bar\varphi^{r_160} \varphi^{s_160} L_{r_10160s_10160} \bar\varphi^{r_10160} \varphi^{s_10160} D\qquad\text{(4.256; G31)}
\end{aligned}
\tag{238}
```

```math
\begin{aligned}
&+\frac{104}{3 L^{6}} L_{r_162s_162} \bar\varphi^{r_162} \varphi^{s_162} L_{r_10162s_10162} \bar\varphi^{r_10162} \varphi^{s_10162} T^2\qquad\text{(4.257; G32)}\\
&- \frac{32 N}{L^{4}} \bar\chi^i \varphi^{j_{166}} \bar\varphi_{i} \varphi_{j_{166}}\qquad\text{(4.258; G33)}\\
&+\frac{96 N}{L^{6}} \bar\chi^i \varphi^{j_{166}} \bar\varphi_{k_{166}} \varphi_{l_{166}} L^{k_{166}l_{166}} L_{ij_{166}}\qquad\text{(4.259; G33)}\\
&+\frac{16 i}{L^{4}} L_{r_164s_164} \bar\varphi^{r_164} \varphi^{s_164} \bar\chi^i \not{\mathcal D}\varphi_{i}\qquad\text{(4.260; G33)}
\end{aligned}
\tag{239}
```

```math
\begin{aligned}
&- \frac{128}{L^{4}} L_{r_164s_164} \bar\varphi^{r_164} \varphi^{s_164} \bar\chi^i L_{ij_{166}} \chi^{j_{166}}\qquad\text{(4.261; G33)}\\
&- \frac{32}{L^{4}} L_{r_164s_164} \bar\varphi^{r_164} \varphi^{s_164} \bar\chi^i \gamma\!\cdot\!T \varphi_{i}\qquad\text{(4.262; G33)}\\
&+\frac{16 N}{L^{6}} L_{r_164s_164} \bar\varphi^{r_164} \varphi^{s_164} \bar\chi^i L_{ij_{166}} \varphi^{j_{166}}\qquad\text{(4.263; G33)}\\
&- \frac{16 i}{L^{6}} L_{r_164s_164} \bar\varphi^{r_164} \varphi^{s_164} \bar\chi^i (\not{\mathcal D}L_{ij_{166}}) L^{j_{166}k_{166}} \varphi_{k_{166}}\qquad\text{(4.264; G33)}
\end{aligned}
\tag{240}
```

```math
\begin{aligned}
&+\frac{16 i}{L^{6}} L_{r_164s_164} \bar\varphi^{r_164} \varphi^{s_164} \bar\chi^i \not E L_{ij_{166}} \varphi^{j_{166}}\qquad\text{(4.265; G33)}\\
&- \frac{20 i N}{L^{4}} L_{r_167s_167} \bar\varphi^{r_167} \varphi^{s_167} \bar\psi_a^i \gamma^a \chi_i\qquad\text{(4.266; G34)}\\
&+\frac{3 N}{L^{5}} \bar\psi_a^i \gamma^a \gamma^{q_{174}} (\mathcal D_{q_{174}}L) \varphi^{j_{174}} \bar\varphi_{i} \varphi_{j_{174}}\qquad\text{(4.267; G35)}\\
&- \frac{N}{L^{4}} \bar\psi_a^i \gamma^a \gamma^{q_{174}} \mathcal D_{q_{174}}\!\left(\varphi^{j_{174}}\right) \bar\varphi_{i} \varphi_{j_{174}}\qquad\text{(4.268; G35)}
\end{aligned}
\tag{241}
```

```math
\begin{aligned}
&- \frac{N}{L^{4}} \bar\psi_a^i \gamma^a \gamma^{q_{174}} \varphi^{j_{174}} \mathcal D_{q_{174}}\!\left(\bar\varphi_{i}\right) \varphi_{j_{174}}\qquad\text{(4.269; G35)}\\
&- \frac{N}{L^{4}} \bar\psi_a^i \gamma^a \gamma^{q_{174}} \varphi^{j_{174}} \bar\varphi_{i} \mathcal D_{q_{174}}\!\left(\varphi_{j_{174}}\right)\qquad\text{(4.270; G35)}\\
&- \frac{15 N}{L^{7}} \bar\psi_a^i \gamma^a \gamma^{q_{174}} (\mathcal D_{q_{174}}L) \varphi^{j_{174}} \bar\varphi_{k_{174}} \varphi_{l_{174}} L^{k_{174}l_{174}} L_{ij_{174}}\qquad\text{(4.271; G35)}\\
&+\frac{3 N}{L^{6}} \bar\psi_a^i \gamma^a \gamma^{q_{174}} \mathcal D_{q_{174}}\!\left(\varphi^{j_{174}}\right) \bar\varphi_{k_{174}} \varphi_{l_{174}} L^{k_{174}l_{174}} L_{ij_{174}}\qquad\text{(4.272; G35)}
\end{aligned}
\tag{242}
```

```math
\begin{aligned}
&+\frac{3 N}{L^{6}} \bar\psi_a^i \gamma^a \gamma^{q_{174}} \varphi^{j_{174}} \mathcal D_{q_{174}}\!\left(\bar\varphi_{k_{174}}\right) \varphi_{l_{174}} L^{k_{174}l_{174}} L_{ij_{174}}\qquad\text{(4.273; G35)}\\
&+\frac{3 N}{L^{6}} \bar\psi_a^i \gamma^a \gamma^{q_{174}} \varphi^{j_{174}} \bar\varphi_{k_{174}} \mathcal D_{q_{174}}\!\left(\varphi_{l_{174}}\right) L^{k_{174}l_{174}} L_{ij_{174}}\qquad\text{(4.274; G35)}\\
&+\frac{3 N}{L^{6}} \bar\psi_a^i \gamma^a \gamma^{q_{174}} \varphi^{j_{174}} \bar\varphi_{k_{174}} \varphi_{l_{174}} \mathcal D_{q_{174}}\!\left(L^{k_{174}l_{174}}\right) L_{ij_{174}}\qquad\text{(4.275; G35)}\\
&+\frac{3 N}{L^{6}} \bar\psi_a^i \gamma^a \gamma^{q_{174}} \varphi^{j_{174}} \bar\varphi_{k_{174}} \varphi_{l_{174}} L^{k_{174}l_{174}} \mathcal D_{q_{174}}\!\left(L_{ij_{174}}\right)\qquad\text{(4.276; G35)}
\end{aligned}
\tag{243}
```

```math
\begin{aligned}
&- \frac{i}{2 L^{5}} L_{r_171s_171} \bar\varphi^{r_171} \varphi^{s_171} \bar\psi_a^i \gamma^a \gamma^{q_{174}} (\mathcal D_{q_{174}}L) \not{\mathcal D}\varphi_{i}\qquad\text{(4.277; G35)}\\
&+\frac{i}{2 L^{4}} L_{r_171s_171} \bar\varphi^{r_171} \varphi^{s_171} \bar\psi_a^i \gamma^a \gamma^{q_{174}} \mathcal D_{q_{174}}\!\left(\not{\mathcal D}\varphi_{i}\right)\qquad\text{(4.278; G35)}\\
&+\frac{4}{L^{5}} L_{r_171s_171} \bar\varphi^{r_171} \varphi^{s_171} \bar\psi_a^i \gamma^a \gamma^{q_{174}} (\mathcal D_{q_{174}}L) L_{ij_{174}} \chi^{j_{174}}\qquad\text{(4.279; G35)}\\
&- \frac{4}{L^{4}} L_{r_171s_171} \bar\varphi^{r_171} \varphi^{s_171} \bar\psi_a^i \gamma^a \gamma^{q_{174}} \mathcal D_{q_{174}}\!\left(L_{ij_{174}}\right) \chi^{j_{174}}\qquad\text{(4.280; G35)}
\end{aligned}
\tag{244}
```

```math
\begin{aligned}
&- \frac{4}{L^{4}} L_{r_171s_171} \bar\varphi^{r_171} \varphi^{s_171} \bar\psi_a^i \gamma^a \gamma^{q_{174}} L_{ij_{174}} \mathcal D_{q_{174}}\!\left(\chi^{j_{174}}\right)\qquad\text{(4.281; G35)}\\
&+\frac{1}{L^{5}} L_{r_171s_171} \bar\varphi^{r_171} \varphi^{s_171} \bar\psi_a^i \gamma^a \gamma^{q_{174}} (\mathcal D_{q_{174}}L) \gamma\!\cdot\!T \varphi_{i}\qquad\text{(4.282; G35)}\\
&- \frac{1}{L^{4}} L_{r_171s_171} \bar\varphi^{r_171} \varphi^{s_171} \bar\psi_a^i \gamma^a \gamma^{q_{174}} \gamma\!\cdot\!T \mathcal D_{q_{174}}\!\left(\varphi_{i}\right)\qquad\text{(4.283; G35)}\\
&- \frac{3 N}{2 L^{7}} L_{r_171s_171} \bar\varphi^{r_171} \varphi^{s_171} \bar\psi_a^i \gamma^a \gamma^{q_{174}} (\mathcal D_{q_{174}}L) L_{ij_{174}} \varphi^{j_{174}}\qquad\text{(4.284; G35)}
\end{aligned}
\tag{245}
```

```math
\begin{aligned}
&+\frac{1}{2 L^{6}} L_{r_171s_171} \bar\varphi^{r_171} \varphi^{s_171} \bar\psi_a^i \gamma^a \gamma^{q_{174}} (\mathcal D_{q_{174}}N) L_{ij_{174}} \varphi^{j_{174}}\qquad\text{(4.285; G35)}\\
&+\frac{N}{2 L^{6}} L_{r_171s_171} \bar\varphi^{r_171} \varphi^{s_171} \bar\psi_a^i \gamma^a \gamma^{q_{174}} \mathcal D_{q_{174}}\!\left(L_{ij_{174}}\right) \varphi^{j_{174}}\qquad\text{(4.286; G35)}\\
&+\frac{N}{2 L^{6}} L_{r_171s_171} \bar\varphi^{r_171} \varphi^{s_171} \bar\psi_a^i \gamma^a \gamma^{q_{174}} L_{ij_{174}} \mathcal D_{q_{174}}\!\left(\varphi^{j_{174}}\right)\qquad\text{(4.287; G35)}\\
&+\frac{3 i}{2 L^{7}} L_{r_171s_171} \bar\varphi^{r_171} \varphi^{s_171} \bar\psi_a^i \gamma^a \gamma^{q_{174}} (\mathcal D_{q_{174}}L) (\not{\mathcal D}L_{ij_{174}}) L^{j_{174}k_{174}} \varphi_{k_{174}}\qquad\text{(4.288; G35)}
\end{aligned}
\tag{246}
```

```math
\begin{aligned}
&- \frac{i}{2 L^{6}} L_{r_171s_171} \bar\varphi^{r_171} \varphi^{s_171} \bar\psi_a^i \gamma^a \gamma^{q_{174}} \mathcal D_{q_{174}}\!\left((\not{\mathcal D}L_{ij_{174}})\right) L^{j_{174}k_{174}} \varphi_{k_{174}}\qquad\text{(4.289; G35)}\\
&- \frac{i}{2 L^{6}} L_{r_171s_171} \bar\varphi^{r_171} \varphi^{s_171} \bar\psi_a^i \gamma^a \gamma^{q_{174}} (\not{\mathcal D}L_{ij_{174}}) \mathcal D_{q_{174}}\!\left(L^{j_{174}k_{174}}\right) \varphi_{k_{174}}\qquad\text{(4.290; G35)}\\
&- \frac{i}{2 L^{6}} L_{r_171s_171} \bar\varphi^{r_171} \varphi^{s_171} \bar\psi_a^i \gamma^a \gamma^{q_{174}} (\not{\mathcal D}L_{ij_{174}}) L^{j_{174}k_{174}} \mathcal D_{q_{174}}\!\left(\varphi_{k_{174}}\right)\qquad\text{(4.291; G35)}\\
&- \frac{3 i}{2 L^{7}} L_{r_171s_171} \bar\varphi^{r_171} \varphi^{s_171} \bar\psi_a^i \gamma^a \gamma^{q_{174}} (\mathcal D_{q_{174}}L) \not E L_{ij_{174}} \varphi^{j_{174}}\qquad\text{(4.292; G35)}
\end{aligned}
\tag{247}
```

```math
\begin{aligned}
&+\frac{i}{2 L^{6}} L_{r_171s_171} \bar\varphi^{r_171} \varphi^{s_171} \bar\psi_a^i \gamma^a \gamma^{q_{174}} \mathcal D_{q_{174}}\!\left(\not E\right) L_{ij_{174}} \varphi^{j_{174}}\qquad\text{(4.293; G35)}\\
&+\frac{i}{2 L^{6}} L_{r_171s_171} \bar\varphi^{r_171} \varphi^{s_171} \bar\psi_a^i \gamma^a \gamma^{q_{174}} \not E \mathcal D_{q_{174}}\!\left(L_{ij_{174}}\right) \varphi^{j_{174}}\qquad\text{(4.294; G35)}\\
&+\frac{i}{2 L^{6}} L_{r_171s_171} \bar\varphi^{r_171} \varphi^{s_171} \bar\psi_a^i \gamma^a \gamma^{q_{174}} \not E L_{ij_{174}} \mathcal D_{q_{174}}\!\left(\varphi^{j_{174}}\right)\qquad\text{(4.295; G35)}\\
&- \frac{1}{L^{4}} L_{r_171s_171} \bar\varphi^{r_171} \varphi^{s_171} \bar\psi_a^i \gamma^a \gamma^{q_{174}} \gamma^{mn}(\mathcal D_{q_{174}}T_{mn}) \varphi_{i}\qquad\text{(4.296; G35)}
\end{aligned}
\tag{248}
```

```math
\begin{aligned}
&+\frac{2 i N}{L^{4}} \bar\psi_a^i \gamma^a \gamma\cdot T \varphi^{j_{179}} \bar\varphi_{i} \varphi_{j_{179}}\qquad\text{(4.297; G36)}\\
&- \frac{6 i N}{L^{6}} \bar\psi_a^i \gamma^a \gamma\cdot T \varphi^{j_{179}} \bar\varphi_{k_{179}} \varphi_{l_{179}} L^{k_{179}l_{179}} L_{ij_{179}}\qquad\text{(4.298; G36)}\\
&+\frac{1}{L^{4}} L_{r_175s_175} \bar\varphi^{r_175} \varphi^{s_175} \bar\psi_a^i \gamma^a \gamma\cdot T \not{\mathcal D}\varphi_{i}\qquad\text{(4.299; G36)}\\
&+\frac{8 i}{L^{4}} L_{r_175s_175} \bar\varphi^{r_175} \varphi^{s_175} \bar\psi_a^i \gamma^a \gamma\cdot T L_{ij_{179}} \chi^{j_{179}}\qquad\text{(4.300; G36)}
\end{aligned}
\tag{249}
```

```math
\begin{aligned}
&+\frac{2 i}{L^{4}} L_{r_175s_175} \bar\varphi^{r_175} \varphi^{s_175} \bar\psi_a^i \gamma^a \gamma\cdot T \gamma\!\cdot\!T \varphi_{i}\qquad\text{(4.301; G36)}\\
&- \frac{i N}{L^{6}} L_{r_175s_175} \bar\varphi^{r_175} \varphi^{s_175} \bar\psi_a^i \gamma^a \gamma\cdot T L_{ij_{179}} \varphi^{j_{179}}\qquad\text{(4.302; G36)}\\
&- \frac{1}{L^{6}} L_{r_175s_175} \bar\varphi^{r_175} \varphi^{s_175} \bar\psi_a^i \gamma^a \gamma\cdot T (\not{\mathcal D}L_{ij_{179}}) L^{j_{179}k_{179}} \varphi_{k_{179}}\qquad\text{(4.303; G36)}\\
&+\frac{1}{L^{6}} L_{r_175s_175} \bar\varphi^{r_175} \varphi^{s_175} \bar\psi_a^i \gamma^a \gamma\cdot T \not E L_{ij_{179}} \varphi^{j_{179}}\qquad\text{(4.304; G36)}
\end{aligned}
\tag{250}
```

```math
\begin{aligned}
&- \frac{i N}{4 L^{4}} \bar\psi_a^i \gamma^a \gamma\cdot\widehat G \varphi^{j_{184}} \bar\varphi_{i} \varphi_{j_{184}}\qquad\text{(4.305; G37)}\\
&+\frac{3 i N}{4 L^{6}} \bar\psi_a^i \gamma^a \gamma\cdot\widehat G \varphi^{j_{184}} \bar\varphi_{k_{184}} \varphi_{l_{184}} L^{k_{184}l_{184}} L_{ij_{184}}\qquad\text{(4.306; G37)}\\
&- \frac{1}{8 L^{4}} L_{r_180s_180} \bar\varphi^{r_180} \varphi^{s_180} \bar\psi_a^i \gamma^a \gamma\cdot\widehat G \not{\mathcal D}\varphi_{i}\qquad\text{(4.307; G37)}\\
&- \frac{i}{L^{4}} L_{r_180s_180} \bar\varphi^{r_180} \varphi^{s_180} \bar\psi_a^i \gamma^a \gamma\cdot\widehat G L_{ij_{184}} \chi^{j_{184}}\qquad\text{(4.308; G37)}
\end{aligned}
\tag{251}
```

```math
\begin{aligned}
&- \frac{i}{4 L^{4}} L_{r_180s_180} \bar\varphi^{r_180} \varphi^{s_180} \bar\psi_a^i \gamma^a \gamma\cdot\widehat G \gamma\!\cdot\!T \varphi_{i}\qquad\text{(4.309; G37)}\\
&+\frac{i N}{8 L^{6}} L_{r_180s_180} \bar\varphi^{r_180} \varphi^{s_180} \bar\psi_a^i \gamma^a \gamma\cdot\widehat G L_{ij_{184}} \varphi^{j_{184}}\qquad\text{(4.310; G37)}\\
&+\frac{1}{8 L^{6}} L_{r_180s_180} \bar\varphi^{r_180} \varphi^{s_180} \bar\psi_a^i \gamma^a \gamma\cdot\widehat G (\not{\mathcal D}L_{ij_{184}}) L^{j_{184}k_{184}} \varphi_{k_{184}}\qquad\text{(4.311; G37)}\\
&- \frac{1}{8 L^{6}} L_{r_180s_180} \bar\varphi^{r_180} \varphi^{s_180} \bar\psi_a^i \gamma^a \gamma\cdot\widehat G \not E L_{ij_{184}} \varphi^{j_{184}}\qquad\text{(4.312; G37)}
\end{aligned}
\tag{252}
```

```math
\begin{aligned}
&+\frac{i N g}{2 L^{4}} \bar\psi_a^i \gamma^a L_{ij} \varepsilon^{jr_{189}} \varphi^{j_{189}} \bar\varphi_{r_{189}} \varphi_{j_{189}}\qquad\text{(4.313; G38)}\\
&- \frac{3 i N g}{2 L^{6}} \bar\psi_a^i \gamma^a L_{ij} \varepsilon^{jr_{189}} \varphi^{j_{189}} \bar\varphi_{k_{189}} \varphi_{l_{189}} L^{k_{189}l_{189}} L_{r_{189}j_{189}}\qquad\text{(4.314; G38)}\\
&+\frac{g}{4 L^{4}} L_{r_185s_185} \bar\varphi^{r_185} \varphi^{s_185} \bar\psi_a^i \gamma^a L_{ij} \varepsilon^{jr_{189}} \not{\mathcal D}\varphi_{r_{189}}\qquad\text{(4.315; G38)}\\
&+\frac{2 i g}{L^{4}} L_{r_185s_185} \bar\varphi^{r_185} \varphi^{s_185} \bar\psi_a^i \gamma^a L_{ij} \varepsilon^{jr_{189}} L_{r_{189}j_{189}} \chi^{j_{189}}\qquad\text{(4.316; G38)}
\end{aligned}
\tag{253}
```

```math
\begin{aligned}
&+\frac{i g}{2 L^{4}} L_{r_185s_185} \bar\varphi^{r_185} \varphi^{s_185} \bar\psi_a^i \gamma^a L_{ij} \varepsilon^{jr_{189}} \gamma\!\cdot\!T \varphi_{r_{189}}\qquad\text{(4.317; G38)}\\
&- \frac{i N g}{4 L^{6}} L_{r_185s_185} \bar\varphi^{r_185} \varphi^{s_185} \bar\psi_a^i \gamma^a L_{ij} \varepsilon^{jr_{189}} L_{r_{189}j_{189}} \varphi^{j_{189}}\qquad\text{(4.318; G38)}\\
&- \frac{g}{4 L^{6}} L_{r_185s_185} \bar\varphi^{r_185} \varphi^{s_185} \bar\psi_a^i \gamma^a L_{ij} \varepsilon^{jr_{189}} (\not{\mathcal D}L_{r_{189}j_{189}}) L^{j_{189}k_{189}} \varphi_{k_{189}}\qquad\text{(4.319; G38)}\\
&+\frac{g}{4 L^{6}} L_{r_185s_185} \bar\varphi^{r_185} \varphi^{s_185} \bar\psi_a^i \gamma^a L_{ij} \varepsilon^{jr_{189}} \not E L_{r_{189}j_{189}} \varphi^{j_{189}}\qquad\text{(4.320; G38)}
\end{aligned}
\tag{254}
```

```math
\begin{aligned}
&- \frac{N}{4 L^{4}} L_{r_190s_190} \bar\varphi^{r_190} \varphi^{s_190} \bar\psi_a^i \gamma^a \gamma^b \gamma\cdot\widehat G \psi_{bi}\qquad\text{(4.321; G39)}\\
&+\frac{N}{L^{4}} L_{r_196s_196} \bar\varphi^{r_196} \varphi^{s_196} \bar\psi_a^i \gamma^a \gamma^b \gamma\cdot T \psi_{bi}\qquad\text{(4.322; G39)}\\
&- \frac{N g}{2 L^{4}} L_{r_202s_202} \bar\varphi^{r_202} \varphi^{s_202} \bar\psi_a^i \gamma^a \gamma^b L_{ij} \psi_b^j\qquad\text{(4.323; G39)}\\
&+\frac{N}{L^{4}} L_{r_208s_208} \bar\varphi^{r_208} \varphi^{s_208} \bar\psi_a^i \gamma^a \gamma^b \phi_{bi}\qquad\text{(4.324; G39)}
\end{aligned}
\tag{255}
```

```math
\begin{aligned}
&+\frac{N}{4 L^{4}} L_{r_213s_213} \bar\varphi^{r_213} \varphi^{s_213} \bar\psi_a^i \gamma\cdot\widehat G \psi^a_i\qquad\text{(4.325; G40)}\\
&- \frac{N}{L^{4}} L_{r_217s_217} \bar\varphi^{r_217} \varphi^{s_217} \bar\psi_a^i \gamma\cdot T \psi^a_i\qquad\text{(4.326; G40)}\\
&+\frac{N g}{2 L^{4}} L_{r_221s_221} \bar\varphi^{r_221} \varphi^{s_221} \bar\psi_a^i L_{ij} \psi^{aj}\qquad\text{(4.327; G40)}\\
&- \frac{N}{L^{4}} L_{r_225s_225} \bar\varphi^{r_225} \varphi^{s_225} \bar\psi_a^i \phi^a_i\qquad\text{(4.328; G40)}
\end{aligned}
\tag{256}
```

```math
\begin{aligned}
&+\frac{N g}{2 L^{4}} L_{r_228s_228} \bar\varphi^{r_228} \varphi^{s_228} \bar\psi_a^i \gamma^{ab} \psi_b^j L_{ij}\qquad\text{(4.329; G41)}\\
&- \frac{1}{4 L^{3}} L_{r_233s_233} \bar\varphi^{r_233} \varphi^{s_233} \bar\psi_a^i \gamma^{ab} \psi_b^j Y'_{ij}\qquad\text{(4.330; G42)}
\end{aligned}
\tag{257}
```

### 6.4 Actual bosonic restriction and scalar derivative simplification

Here alone, set *all* fermions to zero, including those hidden in the retained composites and connections. Interpret $`Y'`$, $`F'`$, $`A'`$, $`T,D,f`$ as their bosonic restrictions without expanding their component maps. The hatted strengths become ordinary strengths. On $`b_a=0`$, the source operator gives

```math
\left.\Box_c\rho^{\prime}\right|_{\mathrm{bos}}=\nabla^a\nabla_a(2N/L)+2f_a{}^a(2N/L).
\tag{258}
```

```math
\begin{aligned}
&\nabla_a(N/L)=L^{-1}\partial_aN-NL^{-2}\partial_aL,\\
&\nabla^2(N/L)=L^{-1}\nabla^2N-NL^{-2}\nabla^2L-2L^{-2}\partial_aL\partial^aN+2NL^{-3}\partial_aL\partial^aL.
\end{aligned}
\tag{259}
```

```math
\begin{aligned}
&\left[\tfrac12\rho^{\prime}\Box_c\rho^{\prime}+(\rho^{\prime})^2f_a{}^a\right]_{\mathrm{bos}}\\
&=2NL^{-2}\nabla^2N-2N^2L^{-3}\nabla^2L-4NL^{-3}\partial_aL\partial^aN\\
&\quad+4N^2L^{-4}\partial_aL\partial^aL+8N^2L^{-2}f_a{}^a.
\end{aligned}
\tag{260}
```

```math
\boxed{\begin{aligned}\left.e^{-1}\mathcal L_{VL}\right|_{\mathrm{bos}}={}&Y^{\prime}{}^{ij}Y^{\prime}_{ij}-2gNL^{-1}Y^{\prime}{}^{ij}L_{ij}\\
&+2NL^{-2}\nabla^2N-2N^2L^{-3}\nabla^2L-4NL^{-3}\partial_aL\partial^aN\\
&+4N^2L^{-4}\partial_aL\partial^aL+8N^2L^{-2}f_a{}^a\\
&-\frac{N}{2L}F^{\prime}_{ab}G^{ab}+16N^2L^{-2}G_{ab}T^{ab}+8NL^{-1}F^{\prime}_{ab}T^{ab}\\
&-16N^2L^{-2}D-\frac{416}{3}N^2L^{-2}T^2\\
&+NL^{-2}A^{\prime}_a(\partial_bL)G^{ab}-L^{-1}A^{\prime}_a(\partial_bN)G^{ab}\\
&-NL^{-1}A^{\prime}_a\nabla_bG^{ab}-\frac12A^{\prime}_a\nabla_bF^{\prime}{}^{ab}\\
&-16NL^{-2}A^{\prime}_a(\partial_bL)T^{ab}+16L^{-1}A^{\prime}_a(\partial_bN)T^{ab}\\
&+16NL^{-1}A^{\prime}_a\nabla_bT^{ab}-\frac18A^{\prime}_a\varepsilon^{abcde}F^{\prime}_{bc}G_{de}\end{aligned}}
\tag{261}
```

This is the explicitly simplified bosonic restriction of the partially substituted density, in the retained potential representative. No $`A'`$ integration by parts and no auxiliary equation has been used. It is not yet the fully substituted Gold $`R^2`$ density.

## 7. Convention Dependence and Remaining Uncertainties

- The 0/2/4 sectors are an explicit covariant-slot organization. Hidden fermion orders in retained primed fields, gauged backgrounds and derivative connections remain. Section 6.4 is the actual zero-fermion restriction.
- $`\Box_c`$ remains the full source operator in the fermionic sectors; its scalar arguments are explicitly substituted, but its connection and multiplet completions are not expanded into physical fermion sectors.
- The alternative mixed two-form candidate is not used: its unrestricted full-fermion divergence identity was not established. The accepted Step 4 potential representative is preserved.
- The source-gradient phase repair and prior map qualifications remain in force. No independent all-order SUSY or reality audit is claimed.
- The [gauged action through two physical fermions](10_step6_gauged_action_through_two_fermions.md) gives Step 6. The degree-six omission in this partial insertion does not apply to the full [Step 5 result](08_step5_primed_composite_vector_insertion.md).
