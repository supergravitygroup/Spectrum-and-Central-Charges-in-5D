# Collected primed-variable insertion through two explicit fermions

## 1. Problem and Target

Insert the definitions of $`\rho'`$, $`\lambda'_i`$, $`Y'_{ij}`$, $`\widehat F'_{ab}`$ and $`A'_a`$ into the accepted action. Distribute the products created by these insertions, collect equal contractions, and show only zero or two explicit fermions in one final density. Supercovariant differential operators and the common gauged background composites remain intact.

This is the supercovariant representation. Its elementary-field counterpart is given in [the Step 6 report](10_step6_gauged_action_through_two_fermions.md). Its separate bosonic result, Eq. (C13), remains available there and is unchanged.

**Starting density:** [Step 4, Eq. (47)](06_step4_Gold_unprimed_vector_and_gauge.md), 42 additive groups and 57 distributed source rows, lock `R2-GOLD4-UNPRIMED-SUBSTITUTION-v2`. **Primed definitions:** [Step 5, Eqs. (3)–(8) and its local potential derivation](08_step5_primed_composite_vector_insertion.md). These descend from the [locked single-linear map](../../../../../two_derivative_fermionic/inputs/reference/results/gauged_two_derivative_fermionic_action/02_single_linear_multiplet_mapping_construction.md), Sections 7.9, 8.7/8.11, 9.7 and Eq. (10.11). The map source is Özkan 2016, [arXiv:1608.00349v2](../../../../../../references/bibliography.md#Ozkan2016), Eq. (3.14), PDF p. 9. The mixed-map parent remains Eq. (3.20), with the already recorded gradient-phase repair.

**A1.** Work off shell in the existing gauge $`\sigma=1`$, $`b_\mu=0`$, defining $`\psi^i=0`$, and the authorized local alignment $`L_{ij}=L\delta_{ij}/\sqrt2`$, $`L>0`$. The gravitino $`\psi_\mu{}^i`$, original linear fermion $`\varphi^i`$ and dynamical $`L`$ survive.

**A2.** Substitute the primed variables only. Retain $`T_{ab},\chi^i,D`$, dependent $`\phi_\mu{}^i,f_\mu{}^a`$, $`E_a`$, $`\widehat G`$, $`\widehat R(V)`$ and $`\widehat R(Q)`$ in their full gauged definitions. In particular, retain their implicit fermions. Their common background is Coomans–Özkan (5.2)–(5.8), PDF 16–17 ([publication](../../../../../../references/bibliography.md#CoomansOzkan2013)).

**A3.** Keep $`\mathcal D`$ and the appropriate source $`\Box_c`$ without splitting their connections or applying Leibniz expansions to their arguments. Operator linearity and the newly authorized inverse product rule collect shared derivative arguments. Thus, for example, $`\mathcal D_a(L^{-1}E_b)`$ stays as one derivative of that product. Section 4.4 derives the symmetric/antisymmetric and shared-derivative collections used in the current final expression.

**A4.** Count displayed odd factors: $`\varphi,\psi_\mu,\chi,\phi_\mu,\widehat R(Q)`$ and their bars have degree one. A supercovariant differential operator preserves this explicit grading. Discard displayed degree four and above. Retained even composites and operators may contain implicit higher fermions: this is the supercovariant representation, not a split into physical component projections.

**A5.** No field equation, auxiliary elimination, derivative commutator, Fierz identity, integration by parts, boundary conversion or change of normalization is used in this insertion. The previous potential representative and its hatted source terms are preserved together.

## 2. Convention Ledger

<!-- ASSERT_CONVENTION: natural_units=hbar=c=1; metric_signature=mostly_plus (-++++); spinor_bar=NW-SE-transpose; gauge_slice=Gold7-and-local-Gold25; fermion_order=explicit-0-and-2; background=gauged_Coomans; derivative=source-supercovariant -->

| Item | Convention |
|---|---|
| Dimension and indices | Five; $`a,b,\mu,\nu=0,\ldots,4`$; $`i,j=1,2`$ |
| Metric, orientation | $`\eta=(-++++)`$; $`\varepsilon^{01234}=+1`$, $`\varepsilon_{01234}=-1`$ |
| Curvature | $`R^\rho{}_{\sigma\mu\nu}=2\partial_{[\mu}\Gamma^\rho_{\nu]\sigma}+2\Gamma^\rho_{[\mu\vert\lambda\vert}\Gamma^\lambda_{\nu]\sigma}`$ |
| Gamma matrices | $`\{\gamma_a,\gamma_b\}=2\eta_{ab}`$; $`\gamma^{abcde}=i\varepsilon^{abcde}`$; dot contractions have no factorial |
| Symmetrization | Unit weight, including $`X_{(ij)}=(X_{ij}+X_{ji})/2`$ |
| Spinors | Grassmann-odd symplectic Majorana; the operational transpose bar preserves scalar $`i`$ and reverses gamma-matrix order |
| Spinor indices | $`X^i=\varepsilon^{ij}X_j`$, $`X_i=X^j\varepsilon_{ji}`$, $`\varepsilon^{12}=\varepsilon_{12}=1`$ |
| Derivatives | Original full supercovariant derivatives; all gauged, torsion, $`S`$- and $`K`$-connection definitions are retained |
| Couplings | Same $`g`$ and unit BF normalization as Steps 4–5; no new fit or rescaling |
| Unused choices | Fourier transforms, renormalization, functional-derivative conventions and boundary conditions are unnecessary for this algebraic insertion |

The symbol $`V_a`$ in $`A'_a`$ is the existing trace connection in $`V_a{}^{ij}=V'_a{}^{ij}+\delta^{ij}V_a/2`$. It is not a new vector multiplet. Triplet alignment does not set $`\mathcal D_aL_{ij}`$ to zero.

## 3. Definitions and Required Identities

The following literal input maps retain precisely the terms needed for the displayed order. They are preserved as the starting point for the reductions (SC21)–(SC35); the collected maps are (SC30)–(SC31). The terms omitted from the gaugino contain three explicit fermions; every gaugino occurrence in this even action is accompanied by another odd factor. The omitted triplet terms contain four. Neither can contribute to the retained outer products.

```math
\rho'=\left[\begin{aligned}
&2L^{-1}N\\
&+iL^{-3}L_{ij}\bar\varphi^i\varphi^j
\end{aligned}\right]
\tag{SC1}
```

```math
\lambda'_i=\left[\begin{aligned}
&-2iL^{-1}\not{\mathcal D}\varphi_i\\
&+16L^{-1}L_{ij}\chi^j\\
&+4L^{-1}\gamma\!\cdot\!T\varphi_i\\
&-2NL^{-3}L_{ij}\varphi^j\\
&+2iL^{-3}(\not{\mathcal D}L_{ij})L^{jk}\varphi_k\\
&-2iL^{-3}\not E L_{ij}\varphi^j
\end{aligned}\right]+O_{\rm explicit}(\mathrm{fermion}^3)
\tag{SC2}
```

```math
Y'_{ij}=\left[\begin{aligned}
&L^{-1}\square^c L_{ij}\\
&-L^{-3}L^{km}\mathcal D_aL_{k(i}\mathcal D^aL_{j)m}\\
&-L^{-3}L_{ij}N^2\\
&-L^{-3}L_{ij}E_aE^a\\
&+2L^{-3}E_aL_{k(i}\mathcal D^aL_{j)}{}^k\\
&+\frac83L^{-1}L_{ij}T^2\\
&+4L^{-1}L_{ij}D\\
&+iNL^{-3}\bar\varphi_{(i}\varphi_{j)}\\
&-3iNL^{-5}L_{ij}L^{kl}\bar\varphi_k\varphi_l\\
&+3L^{-5}L_{ij}L^{kl}\bar\varphi_k\not E\varphi_l\\
&-L^{-3}\bar\varphi_{(i}\not E\varphi_{j)}\\
&-16iL^{-1}\bar\chi_{(i}\varphi_{j)}\\
&+16iL^{-3}L_{ij}L_{kl}\bar\chi^k\varphi^l\\
&+2L^{-3}L_{k(i}\bar\varphi^k\not{\mathcal D}\varphi_{j)}\\
&-3L^{-5}L_{k(i}L^{lm}\bar\varphi^k(\not{\mathcal D}L_{j)l})\varphi_m\\
&+\frac12L^{-3}\bar\varphi^l(\not{\mathcal D}L_{l(i})\varphi_{j)}\\
&+\frac12L^{-3}\bar\varphi^m(\not{\mathcal D}L_{ij})\varphi_m\\
&+2iL^{-3}L_{ij}\bar\varphi\gamma\!\cdot\!T\varphi
\end{aligned}\right]+O_{\rm explicit}(\mathrm{fermion}^4)
\tag{SC3}
```

```math
\widehat F'_{\mu\nu}=\left[\begin{aligned}
&4\mathcal D_{[\mu}(L^{-1}E_{\nu]})\\
&+2L^{-1}\widehat R_{\mu\nu}^{ij}(V)L_{ij}\\
&-2L^{-3}L_k{}^l\mathcal D_{[\mu}L^{kp}\mathcal D_{\nu]}L_{lp}\\
&-2\mathcal D_{[\mu}(L^{-3}L_{ij}\bar\varphi^i\gamma_{\nu]}\varphi^j)\\
&-iL^{-1}\bar\varphi^i\widehat R_{\mu\nu i}(Q)
\end{aligned}\right]
\tag{SC4}
```

```math
A'_a=\frac{2}{L}E_a+\sqrt2V_a-\frac{1}{L^3}L_{ij}\bar\varphi^i\gamma_a\varphi^j-\frac{i}{L}\bar\varphi^i\psi_{ai}.
\tag{SC5}
```

Equation (SC5) is the earlier derived local aligned representative. The full source-strength formula (SC4), rather than an ordinary curl substituted for it, is inserted wherever the parent action contains $`\widehat F'`$.

The bar map follows by transposing the six retained gaugino terms. In particular, $`C^{-1}(\gamma^a)^TC=\gamma^a`$ and $`C^{-1}(\gamma^{ab})^TC=-\gamma^{ab}`$ give

```math
\begin{aligned}
\overline{-2iL^{-1}\gamma^a\mathcal D_a\varphi_i}
&=-2iL^{-1}(\mathcal D_a\bar\varphi_i)\gamma^a,\\
\overline{4L^{-1}\gamma^{ab}T_{ab}\varphi_i}
&=-4L^{-1}\bar\varphi_i\gamma^{ab}T_{ab}.
\end{aligned}
\tag{SC6}
```

```math
\bar\lambda'_i=\left[\begin{aligned}
&-2iL^{-1}(\mathcal D_a\bar\varphi_i)\gamma^a\\
&+16L^{-1}L_{ij}\bar\chi^j\\
&-4L^{-1}\bar\varphi_i\gamma\!\cdot\!T\\
&-2NL^{-3}L_{ij}\bar\varphi^j\\
&+2iL^{-3}L^{jk}\bar\varphi_k(\not{\mathcal D}L_{ij})\\
&-2iL^{-3}L_{ij}\bar\varphi^j\not E
\end{aligned}\right]+O_{\rm explicit}(\mathrm{fermion}^3).
\tag{SC7}
```

```math
\bar\lambda'{}^i=\varepsilon^{ir}\bar\lambda'_r,\qquad \lambda'{}^j=\varepsilon^{js}\lambda'_s,\qquad Y'^{ij}=\varepsilon^{ir}\varepsilon^{js}Y'_{rs}.
\tag{SC8}
```

The background composites in these maps remain unexpanded. Numeric labels on equation groups below are traceability labels and introduce no physical fields.

## 4. Detailed Derivation

### 4.1 Scalar multiplication and retained derivative arguments

<!-- ASSERT_CONVENTION: metric_signature=mostly_plus (-++++); spinor_bar=NW-SE-transpose; derivative=source-supercovariant; fermion_order=explicit-0-and-2 -->

Multiplication of the two scalar summands gives

```math
\begin{aligned}
(\rho')^2
&=\frac{4N^2}{L^2}+\frac{2iN}{L^4}L_{ij}\bar\varphi^i\varphi^j
+\frac{2iN}{L^4}L_{ij}\bar\varphi^i\varphi^j
-\frac{1}{L^6}(L_{ij}\bar\varphi^i\varphi^j)(L_{kl}\bar\varphi^k\varphi^l)\\
&=\frac{4N^2}{L^2}+\frac{4iN}{L^4}L_{ij}\bar\varphi^i\varphi^j
+O_{\rm explicit}(\mathrm{fermion}^4).
\end{aligned}
\tag{SC9}
```

The two cross terms have equal signs because each scalar bilinear is even. The omitted coefficient is $`i^2=-1`$, with four displayed fermions. Applying only linearity, then distributing the *outer* scalar product, gives

```math
\begin{aligned}
\frac12\rho'\Box_c\rho'
={}&\frac{2N}{L}\Box_c\!\left(\frac NL\right)
+\frac{iN}{L}\Box_c\!\left(L^{-3}L_{ij}\bar\varphi^i\varphi^j\right)\\
&+iL^{-3}L_{ij}\bar\varphi^i\varphi^j\Box_c\!\left(\frac NL\right)
+O_{\rm explicit}(\mathrm{fermion}^4).
\end{aligned}
\tag{SC10}
```

The factor $`\Box_c`$ has not been replaced or expanded. Its action on the entire indicated composite argument is retained. The same treatment of first derivatives gives

```math
\mathcal D_a\rho'=2\mathcal D_a\!\left(\frac NL\right)
+i\mathcal D_a\!\left(L^{-3}L_{ij}\bar\varphi^i\varphi^j\right).
\tag{SC11}
```

```math
\begin{aligned}
\mathcal D_a\lambda'_i={}&-2i\mathcal D_a\!\left(L^{-1}\not{\mathcal D}\varphi_i\right)
+16\mathcal D_a\!\left(L^{-1}L_{ij}\chi^j\right)\\
&+4\mathcal D_a\!\left(L^{-1}\gamma\!\cdot\!T\varphi_i\right)
-2\mathcal D_a\!\left(NL^{-3}L_{ij}\varphi^j\right)\\
&+2i\mathcal D_a\!\left(L^{-3}(\not{\mathcal D}L_{ij})L^{jk}\varphi_k\right)
-2i\mathcal D_a\!\left(L^{-3}\not E L_{ij}\varphi^j\right)
+O_{\rm explicit}(\mathrm{fermion}^3).
\end{aligned}
\tag{SC12}
```

Each derivative retains its argument, including all products and the inner derivative. For instance, multiplying the first term of (SC7) by the derivative of the first term of (SC2) in the kinetic coupling produces

```math
\begin{aligned}
&-\frac12\varepsilon^{ij}
\left[-\frac{2i}{L}(\mathcal D_a\bar\varphi_j)\gamma^a\right]
\gamma^b\left[-2i\mathcal D_b(L^{-1}\not{\mathcal D}\varphi_i)\right]\\
&\qquad=\frac{2}{L}\varepsilon^{ij}(\mathcal D_a\bar\varphi_j)
\gamma^a\gamma^b\mathcal D_b\!\left(L^{-1}\not{\mathcal D}\varphi_i\right).
\end{aligned}
\tag{SC13}
```

Here $`(-1/2)(-2i)(-2i)=2`$. No spinors interchange and the gamma order is unchanged. The complete kinetic group contains all $`6\times6=36`$ pairings and is printed in Section 4.3.

### 4.2 Symmetrization, norm identities and collection

The unit-weight parentheses in (SC3) and brackets in (SC4) are expanded before their products. For example,

```math
\begin{aligned}
-L^{-3}L^{km}\mathcal D_aL_{k(i}\mathcal D^aL_{j)m}
={}&-\frac{L^{km}}{2L^3}(\mathcal D_aL_{ki})(\mathcal D^aL_{jm})
-\frac{L^{km}}{2L^3}(\mathcal D_aL_{kj})(\mathcal D^aL_{im}),\\
4\mathcal D_{[a}(L^{-1}E_{b]})
={}&2\mathcal D_a(L^{-1}E_b)-2\mathcal D_b(L^{-1}E_a).
\end{aligned}
\tag{SC14}
```

This distributes the index symmetrizations, not the operator's connection terms or argument products. Undifferentiated triplet contractions use

```math
L_{ij}L^{jk}=\frac{L^2}{2}\delta_i{}^k,\qquad
L_{ij}L^{ij}=L^2,\qquad L_i{}^i=0.
\tag{SC15}
```

To verify the norm factors, write a general symmetric two-by-two matrix only for this algebra check:

```math
\begin{aligned}
L_{ij}&=\begin{pmatrix}p&q\\q&r\end{pmatrix},&
L^{ij}&=\begin{pmatrix}r&-q\\-q&p\end{pmatrix},\\
L_{ij}L^{jk}&=(pr-q^2)\delta_i{}^k,&
L^2&=2(pr-q^2).
\end{aligned}
\tag{SC16}
```

The matrix entries in (SC16) are not fields in the action. Equations (SC15)–(SC16) do not act through a differential operator. As an example of the resulting coefficient simplification,

```math
\left(-\frac{N^2}{L^3}L^{ij}\right)
\left(-\frac{N^2}{L^3}L_{ij}\right)
=\frac{N^4}{L^6}L^2=\frac{N^4}{L^4}.
\tag{SC17}
```

Dummy indices are renamed without moving odd factors. Transferring a contracted Lorentz index between two factors has sign $`+1`$; transferring an $`SU(2)`$ index obeys $`X^iY_i=-X_iY^i`$ in the locked NW–SE convention. Epsilon raising/lowering is applied before equivalent scalar contractions are collected. Closed gamma contractions use

```math
\begin{aligned}
\gamma^a\gamma_a&=5,&
\gamma^a\gamma_{ab}&=4\gamma_b,&
\gamma_{ab}\gamma^a&=-4\gamma_b,\\
\gamma^a\gamma^{b_1\ldots b_p}\gamma_a
&=(-1)^p(5-2p)\gamma^{b_1\ldots b_p},\\
\gamma^{a_1\ldots a_p}\gamma_{a_1\ldots a_p}
&=(-1)^{p(p-1)/2}\frac{5!}{(5-p)!}.
\end{aligned}
\tag{SC18}
```

The sandwich coefficient follows by moving the first gamma past the $`p`$ antisymmetrized entries: the crossed term contributes $`(-1)^p5`$, and the $`p`$ anticommutators contribute $`-2p(-1)^p`$. Their sum is $`(-1)^p(5-2p)`$. Iterating a vector contraction gives $`5(5-1)\cdots(5-p+1)`$, with reversal sign $`(-1)^{p(p-1)/2}`$. These operations apply only to closed gamma contractions outside retained derivative arguments. No Fierz reduction or derivative commutation is performed.

### 4.3 Every source group after insertion and distribution

The following groups preserve the insertion before the new reductions. Each source expression is followed by its distributed products through two explicit fermions. All primed occurrences on the right are replaced; the left source expression identifies the input contribution. These are unreduced intermediate equalities: the zero singlet, SU(2) identities and cross-group mergers in Section 4.4 are subsequently applied throughout the final density.

**Source group 1.**

```math
\left.e^{-1}\mathcal L_{R^2}\right|_{\text{source group }1}=Y'^{ij}Y'_{ij}
\tag{SCI1}
```

Substitute (SC1)–(SC8), retain the permitted degree and collect:

```math
\begin{aligned}
\left.e^{-1}\mathcal L_{R^2}\right|_{\text{group }1}={}&\frac{1}{L^{2}} \Box_c\!\left(L_{ij}\right) \Box_c\!\left(L^{ij}\right)\\
&- \frac{2}{L^{4}} E_{a} E^{a} L_{ij} \Box_c\!\left(L^{ij}\right)\\
&- \frac{2 N^{2}}{L^{4}} L_{ij} \Box_c\!\left(L^{ij}\right)\\
&+\frac{16}{3 L^{2}} L_{ij} \Box_c\!\left(L^{ij}\right) T_{ab} T^{ab}\\
&+\frac{8}{L^{2}} D L_{ij} \Box_c\!\left(L^{ij}\right)\\
&- \frac{1}{L^{4}} L_{ij} \Box_c\!\left(L_{kl}\right) \mathcal D_{a}\!\left(L^{ik}\right) \mathcal D^{a}\!\left(L^{lj}\right)\\
&- \frac{2}{L^{4}} E_{a} L_{ij} \Box_c\!\left(L^{j}{}_{k}\right) \mathcal D^{a}\!\left(L^{ki}\right)\\
&- \frac{i N}{L^{4}} \Box_c\!\left(L_{i}{}^{j}\right) \bar\varphi^{i} \varphi_{j}
\end{aligned}
\tag{SCG1.1}
```

```math
\begin{aligned}
&+\frac{1}{L^{4}} E_{a} \Box_c\!\left(L_{i}{}^{j}\right) \bar\varphi^{i} \gamma^{a} \varphi_{j}\\
&+\frac{16 i}{L^{2}} \Box_c\!\left(L_{i}{}^{j}\right) \bar\chi^{i} \varphi_{j}\\
&+\frac{2}{L^{4}} L_{ik} \Box_c\!\left(L^{kj}\right) \bar\varphi^{i} \gamma^{a} \mathcal D_{a}\!\left(\varphi_{j}\right)\\
&- \frac{3}{L^{6}} L_{ik} L^{j}{}_{l} \Box_c\!\left(L^{k}{}_{m}\right) \mathcal D_{a}\!\left(L^{ml}\right) \bar\varphi^{i} \gamma^{a} \varphi_{j}\\
&- \frac{1}{2 L^{4}} \Box_c\!\left(L_{k}{}^{j}\right) \mathcal D_{a}\!\left(L_{i}{}^{k}\right) \bar\varphi^{i} \gamma^{a} \varphi_{j}\\
&- \frac{1}{L^{4}} L_{ij} \Box_c\!\left(L_{kl}\right) \mathcal D_{a}\!\left(L^{il}\right) \mathcal D^{a}\!\left(L^{kj}\right)\\
&- \frac{2}{L^{4}} E_{a} L_{ij} \Box_c\!\left(L_{k}{}^{j}\right) \mathcal D^{a}\!\left(L^{ki}\right)\\
&- \frac{i N}{L^{4}} \Box_c\!\left(L^{j}{}_{i}\right) \bar\varphi^{i} \varphi_{j}
\end{aligned}
\tag{SCG1.2}
```

```math
\begin{aligned}
&+\frac{1}{L^{4}} E_{a} \Box_c\!\left(L^{j}{}_{i}\right) \bar\varphi^{i} \gamma^{a} \varphi_{j}\\
&+\frac{16 i}{L^{2}} \Box_c\!\left(L^{j}{}_{i}\right) \bar\chi^{i} \varphi_{j}\\
&+\frac{2}{L^{4}} L_{ik} \Box_c\!\left(L^{jk}\right) \bar\varphi^{i} \gamma^{a} \mathcal D_{a}\!\left(\varphi_{j}\right)\\
&- \frac{3}{L^{6}} L_{ik} L^{j}{}_{l} \Box_c\!\left(L_{m}{}^{k}\right) \mathcal D_{a}\!\left(L^{ml}\right) \bar\varphi^{i} \gamma^{a} \varphi_{j}\\
&- \frac{1}{2 L^{4}} \Box_c\!\left(L^{j}{}_{k}\right) \mathcal D_{a}\!\left(L_{i}{}^{k}\right) \bar\varphi^{i} \gamma^{a} \varphi_{j}\\
&+\frac{6 i N}{L^{6}} L_{i}{}^{j} L_{kl} \Box_c\!\left(L^{kl}\right) \bar\varphi^{i} \varphi_{j}\\
&- \frac{6}{L^{6}} E_{a} L_{i}{}^{j} L_{kl} \Box_c\!\left(L^{kl}\right) \bar\varphi^{i} \gamma^{a} \varphi_{j}\\
&- \frac{32 i}{L^{4}} L_{i}{}^{j} L_{kl} \Box_c\!\left(L^{kl}\right) \bar\chi^{i} \varphi_{j}
\end{aligned}
\tag{SCG1.3}
```

```math
\begin{aligned}
&+\frac{1}{L^{4}} \Box_c\!\left(L_{jk}\right) \mathcal D_{a}\!\left(L^{jk}\right) \bar\varphi^{i} \gamma^{a} \varphi_{i}\\
&+\frac{4 i}{L^{4}} L_{jk} \Box_c\!\left(L^{jk}\right) T_{ab} \bar\varphi^{i} \gamma^{ab} \varphi_{i}\\
&+\frac{1}{L^{4}} E_{a} E^{a} E_{b} E^{b}\\
&+\frac{2 N^{2}}{L^{4}} E_{a} E^{a}\\
&- \frac{16}{3 L^{2}} E_{a} E^{a} T_{bc} T^{bc}\\
&- \frac{8}{L^{2}} D E_{a} E^{a}\\
&+\frac{1}{2 L^{6}} E_{a} E^{a} L_{ij} L_{kl} \mathcal D_{b}\!\left(L^{ki}\right) \mathcal D^{b}\!\left(L^{jl}\right)\\
&- \frac{1}{L^{6}} E_{a} E^{a} E_{b} L_{ij} L^{i}{}_{k} \mathcal D^{b}\!\left(L^{jk}\right)
\end{aligned}
\tag{SCG1.4}
```

```math
\begin{aligned}
&- \frac{4 i N}{L^{6}} E_{a} E^{a} L_{i}{}^{j} \bar\varphi^{i} \varphi_{j}\\
&+\frac{4}{L^{6}} E_{a} E_{b} E^{b} L_{i}{}^{j} \bar\varphi^{i} \gamma^{a} \varphi_{j}\\
&- \frac{2}{L^{4}} E_{b} E^{b} \bar\varphi^{i} \gamma^{a} \mathcal D_{a}\!\left(\varphi_{i}\right)\\
&+\frac{3}{L^{8}} E_{b} E^{b} L_{ik} L^{j}{}_{l} L^{k}{}_{m} \mathcal D_{a}\!\left(L^{ml}\right) \bar\varphi^{i} \gamma^{a} \varphi_{j}\\
&- \frac{1}{2 L^{6}} E_{b} E^{b} L^{j}{}_{k} \mathcal D_{a}\!\left(L_{i}{}^{k}\right) \bar\varphi^{i} \gamma^{a} \varphi_{j}\\
&+\frac{1}{2 L^{6}} E_{a} E^{a} L_{ij} L_{kl} \mathcal D_{b}\!\left(L^{kj}\right) \mathcal D^{b}\!\left(L^{il}\right)\\
&- \frac{1}{L^{6}} E_{a} E^{a} E_{b} L_{ij} L^{j}{}_{k} \mathcal D^{b}\!\left(L^{ik}\right)\\
&- \frac{1}{L^{6}} E_{b} E^{b} L_{jk} \mathcal D_{a}\!\left(L^{jk}\right) \bar\varphi^{i} \gamma^{a} \varphi_{i}
\end{aligned}
\tag{SCG1.5}
```

```math
\begin{aligned}
&- \frac{4 i}{L^{4}} E_{c} E^{c} T_{ab} \bar\varphi^{i} \gamma^{ab} \varphi_{i}\\
&+\frac{N^{4}}{L^{4}}\\
&- \frac{16 N^{2}}{3 L^{2}} T_{ab} T^{ab}\\
&- \frac{8 N^{2}}{L^{2}} D\\
&+\frac{N^{2}}{2 L^{6}} L_{ij} L_{kl} \mathcal D_{a}\!\left(L^{ki}\right) \mathcal D^{a}\!\left(L^{jl}\right)\\
&- \frac{N^{2}}{L^{6}} E_{a} L_{ij} L^{i}{}_{k} \mathcal D^{a}\!\left(L^{jk}\right)\\
&- \frac{4 i N^{3}}{L^{6}} L_{i}{}^{j} \bar\varphi^{i} \varphi_{j}\\
&+\frac{4 N^{2}}{L^{6}} E_{a} L_{i}{}^{j} \bar\varphi^{i} \gamma^{a} \varphi_{j}
\end{aligned}
\tag{SCG1.6}
```

```math
\begin{aligned}
&- \frac{2 N^{2}}{L^{4}} \bar\varphi^{i} \gamma^{a} \mathcal D_{a}\!\left(\varphi_{i}\right)\\
&+\frac{3 N^{2}}{L^{8}} L_{ik} L^{j}{}_{l} L^{k}{}_{m} \mathcal D_{a}\!\left(L^{ml}\right) \bar\varphi^{i} \gamma^{a} \varphi_{j}\\
&- \frac{N^{2}}{2 L^{6}} L^{j}{}_{k} \mathcal D_{a}\!\left(L_{i}{}^{k}\right) \bar\varphi^{i} \gamma^{a} \varphi_{j}\\
&+\frac{N^{2}}{2 L^{6}} L_{ij} L_{kl} \mathcal D_{a}\!\left(L^{kj}\right) \mathcal D^{a}\!\left(L^{il}\right)\\
&- \frac{N^{2}}{L^{6}} E_{a} L_{ij} L^{j}{}_{k} \mathcal D^{a}\!\left(L^{ik}\right)\\
&- \frac{N^{2}}{L^{6}} L_{jk} \mathcal D_{a}\!\left(L^{jk}\right) \bar\varphi^{i} \gamma^{a} \varphi_{i}\\
&- \frac{4 i N^{2}}{L^{4}} T_{ab} \bar\varphi^{i} \gamma^{ab} \varphi_{i}\\
&+\frac{64}{9} T_{ab} T^{ab} T_{cd} T^{cd}
\end{aligned}
\tag{SCG1.7}
```

```math
\begin{aligned}
&+\frac{64}{3} D T_{ab} T^{ab}\\
&- \frac{4}{3 L^{4}} L_{ij} L_{kl} \mathcal D_{a}\!\left(L^{ki}\right) \mathcal D^{a}\!\left(L^{jl}\right) T_{bc} T^{bc}\\
&+\frac{8}{3 L^{4}} E_{a} L_{ij} L^{i}{}_{k} \mathcal D^{a}\!\left(L^{jk}\right) T_{bc} T^{bc}\\
&+\frac{32 i N}{3 L^{4}} L_{i}{}^{j} T_{ab} T^{ab} \bar\varphi^{i} \varphi_{j}\\
&- \frac{32}{3 L^{4}} E_{a} L_{i}{}^{j} T_{bc} T^{bc} \bar\varphi^{i} \gamma^{a} \varphi_{j}\\
&+\frac{16}{3 L^{2}} T_{bc} T^{bc} \bar\varphi^{i} \gamma^{a} \mathcal D_{a}\!\left(\varphi_{i}\right)\\
&- \frac{8}{L^{6}} L_{ik} L^{j}{}_{l} L^{k}{}_{m} \mathcal D_{a}\!\left(L^{ml}\right) T_{bc} T^{bc} \bar\varphi^{i} \gamma^{a} \varphi_{j}\\
&+\frac{4}{3 L^{4}} L^{j}{}_{k} \mathcal D_{a}\!\left(L_{i}{}^{k}\right) T_{bc} T^{bc} \bar\varphi^{i} \gamma^{a} \varphi_{j}
\end{aligned}
\tag{SCG1.8}
```

```math
\begin{aligned}
&- \frac{4}{3 L^{4}} L_{ij} L_{kl} \mathcal D_{a}\!\left(L^{kj}\right) \mathcal D^{a}\!\left(L^{il}\right) T_{bc} T^{bc}\\
&+\frac{8}{3 L^{4}} E_{a} L_{ij} L^{j}{}_{k} \mathcal D^{a}\!\left(L^{ik}\right) T_{bc} T^{bc}\\
&+\frac{8}{3 L^{4}} L_{jk} \mathcal D_{a}\!\left(L^{jk}\right) T_{bc} T^{bc} \bar\varphi^{i} \gamma^{a} \varphi_{i}\\
&+\frac{32 i}{3 L^{2}} T_{ab} T_{cd} T^{cd} \bar\varphi^{i} \gamma^{ab} \varphi_{i}\\
&+16 D D\\
&- \frac{2}{L^{4}} D L_{ij} L_{kl} \mathcal D_{a}\!\left(L^{ki}\right) \mathcal D^{a}\!\left(L^{jl}\right)\\
&+\frac{4}{L^{4}} D E_{a} L_{ij} L^{i}{}_{k} \mathcal D^{a}\!\left(L^{jk}\right)\\
&+\frac{16 i N}{L^{4}} D L_{i}{}^{j} \bar\varphi^{i} \varphi_{j}
\end{aligned}
\tag{SCG1.9}
```

```math
\begin{aligned}
&- \frac{16}{L^{4}} D E_{a} L_{i}{}^{j} \bar\varphi^{i} \gamma^{a} \varphi_{j}\\
&+\frac{8}{L^{2}} D \bar\varphi^{i} \gamma^{a} \mathcal D_{a}\!\left(\varphi_{i}\right)\\
&- \frac{12}{L^{6}} D L_{ik} L^{j}{}_{l} L^{k}{}_{m} \mathcal D_{a}\!\left(L^{ml}\right) \bar\varphi^{i} \gamma^{a} \varphi_{j}\\
&+\frac{2}{L^{4}} D L^{j}{}_{k} \mathcal D_{a}\!\left(L_{i}{}^{k}\right) \bar\varphi^{i} \gamma^{a} \varphi_{j}\\
&- \frac{2}{L^{4}} D L_{ij} L_{kl} \mathcal D_{a}\!\left(L^{kj}\right) \mathcal D^{a}\!\left(L^{il}\right)\\
&+\frac{4}{L^{4}} D E_{a} L_{ij} L^{j}{}_{k} \mathcal D^{a}\!\left(L^{ik}\right)\\
&+\frac{4}{L^{4}} D L_{jk} \mathcal D_{a}\!\left(L^{jk}\right) \bar\varphi^{i} \gamma^{a} \varphi_{i}\\
&+\frac{16 i}{L^{2}} D T_{ab} \bar\varphi^{i} \gamma^{ab} \varphi_{i}
\end{aligned}
\tag{SCG1.10}
```

```math
\begin{aligned}
&+\frac{1}{2 L^{6}} E_{a} E^{a} L_{ij} L_{kl} \mathcal D_{b}\!\left(L^{ik}\right) \mathcal D^{b}\!\left(L^{lj}\right)\\
&+\frac{N^{2}}{2 L^{6}} L_{ij} L_{kl} \mathcal D_{a}\!\left(L^{ik}\right) \mathcal D^{a}\!\left(L^{lj}\right)\\
&- \frac{4}{3 L^{4}} L_{ij} L_{kl} \mathcal D_{a}\!\left(L^{ik}\right) \mathcal D^{a}\!\left(L^{lj}\right) T_{bc} T^{bc}\\
&- \frac{2}{L^{4}} D L_{ij} L_{kl} \mathcal D_{a}\!\left(L^{ik}\right) \mathcal D^{a}\!\left(L^{lj}\right)\\
&+\frac{1}{2 L^{6}} L_{ij} L_{kl} \mathcal D_{a}\!\left(L^{i}{}_{m}\right) \mathcal D^{a}\!\left(L_{n}{}^{j}\right) \mathcal D_{b}\!\left(L^{km}\right) \mathcal D^{b}\!\left(L^{nl}\right)\\
&+\frac{2}{L^{6}} E_{a} L_{ij} L_{kl} \mathcal D_{b}\!\left(L^{kj}\right) \mathcal D^{b}\!\left(L_{m}{}^{l}\right) \mathcal D^{a}\!\left(L^{mi}\right)\\
&+\frac{i N}{L^{6}} L_{kl} \mathcal D_{a}\!\left(L^{k}{}_{i}\right) \mathcal D^{a}\!\left(L^{jl}\right) \bar\varphi^{i} \varphi_{j}\\
&- \frac{1}{L^{6}} E_{a} L_{kl} \mathcal D_{b}\!\left(L^{k}{}_{i}\right) \mathcal D^{b}\!\left(L^{jl}\right) \bar\varphi^{i} \gamma^{a} \varphi_{j}
\end{aligned}
\tag{SCG1.11}
```

```math
\begin{aligned}
&- \frac{16 i}{L^{4}} L_{kl} \mathcal D_{a}\!\left(L^{k}{}_{i}\right) \mathcal D^{a}\!\left(L^{jl}\right) \bar\chi^{i} \varphi_{j}\\
&- \frac{2}{L^{6}} L_{ik} L_{lm} \mathcal D_{b}\!\left(L^{lk}\right) \mathcal D^{b}\!\left(L^{jm}\right) \bar\varphi^{i} \gamma^{a} \mathcal D_{a}\!\left(\varphi_{j}\right)\\
&- \frac{3}{L^{8}} L_{ik} L^{j}{}_{l} L_{mn} \mathcal D_{a}\!\left(L_{o}{}^{l}\right) \mathcal D_{b}\!\left(L^{mk}\right) \mathcal D^{b}\!\left(L^{on}\right) \bar\varphi^{i} \gamma^{a} \varphi_{j}\\
&- \frac{1}{2 L^{6}} L_{kl} \mathcal D_{a}\!\left(L_{im}\right) \mathcal D_{b}\!\left(L^{km}\right) \mathcal D^{b}\!\left(L^{jl}\right) \bar\varphi^{i} \gamma^{a} \varphi_{j}\\
&+\frac{1}{2 L^{6}} L_{ij} L_{kl} \mathcal D_{a}\!\left(L^{i}{}_{m}\right) \mathcal D^{a}\!\left(L_{n}{}^{j}\right) \mathcal D_{b}\!\left(L^{kn}\right) \mathcal D^{b}\!\left(L^{ml}\right)\\
&+\frac{2}{L^{6}} E_{a} L_{ij} L_{kl} \mathcal D_{b}\!\left(L^{k}{}_{m}\right) \mathcal D^{b}\!\left(L^{jl}\right) \mathcal D^{a}\!\left(L^{mi}\right)\\
&+\frac{i N}{L^{6}} L_{kl} \mathcal D_{a}\!\left(L^{kj}\right) \mathcal D^{a}\!\left(L_{i}{}^{l}\right) \bar\varphi^{i} \varphi_{j}\\
&- \frac{1}{L^{6}} E_{a} L_{kl} \mathcal D_{b}\!\left(L^{kj}\right) \mathcal D^{b}\!\left(L_{i}{}^{l}\right) \bar\varphi^{i} \gamma^{a} \varphi_{j}
\end{aligned}
\tag{SCG1.12}
```

```math
\begin{aligned}
&- \frac{16 i}{L^{4}} L_{kl} \mathcal D_{a}\!\left(L^{kj}\right) \mathcal D^{a}\!\left(L_{i}{}^{l}\right) \bar\chi^{i} \varphi_{j}\\
&- \frac{2}{L^{6}} L_{ik} L_{lm} \mathcal D_{b}\!\left(L^{lj}\right) \mathcal D^{b}\!\left(L^{km}\right) \bar\varphi^{i} \gamma^{a} \mathcal D_{a}\!\left(\varphi_{j}\right)\\
&- \frac{3}{L^{8}} L_{ik} L^{j}{}_{l} L_{mn} \mathcal D_{a}\!\left(L_{o}{}^{l}\right) \mathcal D_{b}\!\left(L^{mo}\right) \mathcal D^{b}\!\left(L^{kn}\right) \bar\varphi^{i} \gamma^{a} \varphi_{j}\\
&- \frac{1}{2 L^{6}} L_{kl} \mathcal D_{a}\!\left(L_{im}\right) \mathcal D_{b}\!\left(L^{kj}\right) \mathcal D^{b}\!\left(L^{ml}\right) \bar\varphi^{i} \gamma^{a} \varphi_{j}\\
&- \frac{3 i N}{2 L^{8}} L_{i}{}^{j} L_{kl} L_{mn} \mathcal D_{a}\!\left(L^{km}\right) \mathcal D^{a}\!\left(L^{nl}\right) \bar\varphi^{i} \varphi_{j}\\
&+\frac{3}{2 L^{8}} E_{a} L_{i}{}^{j} L_{kl} L_{mn} \mathcal D_{b}\!\left(L^{km}\right) \mathcal D^{b}\!\left(L^{nl}\right) \bar\varphi^{i} \gamma^{a} \varphi_{j}\\
&+\frac{8 i}{L^{6}} L_{i}{}^{j} L_{kl} L_{mn} \mathcal D_{a}\!\left(L^{km}\right) \mathcal D^{a}\!\left(L^{nl}\right) \bar\chi^{i} \varphi_{j}\\
&- \frac{1}{2 L^{6}} L_{jk} \mathcal D_{a}\!\left(L_{lm}\right) \mathcal D_{b}\!\left(L^{jl}\right) \mathcal D^{b}\!\left(L^{mk}\right) \bar\varphi^{i} \gamma^{a} \varphi_{i}
\end{aligned}
\tag{SCG1.13}
```

```math
\begin{aligned}
&- \frac{i}{L^{6}} L_{jk} L_{lm} \mathcal D_{c}\!\left(L^{jl}\right) \mathcal D^{c}\!\left(L^{mk}\right) T_{ab} \bar\varphi^{i} \gamma^{ab} \varphi_{i}\\
&- \frac{1}{L^{4}} E_{a} E_{b} E^{b} \mathcal D^{a}\!\left(L_{i}{}^{i}\right)\\
&- \frac{N^{2}}{L^{4}} E_{a} \mathcal D^{a}\!\left(L_{i}{}^{i}\right)\\
&+\frac{8}{3 L^{2}} E_{a} \mathcal D^{a}\!\left(L_{i}{}^{i}\right) T_{bc} T^{bc}\\
&+\frac{4}{L^{2}} D E_{a} \mathcal D^{a}\!\left(L_{i}{}^{i}\right)\\
&+\frac{2}{L^{6}} E_{a} E_{b} L_{ij} L^{j}{}_{k} \mathcal D^{a}\!\left(L_{l}{}^{i}\right) \mathcal D^{b}\!\left(L^{lk}\right)\\
&- \frac{2 i N}{L^{6}} E_{a} L_{ik} \mathcal D^{a}\!\left(L^{jk}\right) \bar\varphi^{i} \varphi_{j}\\
&+\frac{2}{L^{6}} E_{a} E_{b} L_{ik} \mathcal D^{b}\!\left(L^{jk}\right) \bar\varphi^{i} \gamma^{a} \varphi_{j}
\end{aligned}
\tag{SCG1.14}
```

```math
\begin{aligned}
&+\frac{32 i}{L^{4}} E_{a} L_{ik} \mathcal D^{a}\!\left(L^{jk}\right) \bar\chi^{i} \varphi_{j}\\
&+\frac{4}{L^{6}} E_{b} L_{ik} L^{k}{}_{l} \mathcal D^{b}\!\left(L^{jl}\right) \bar\varphi^{i} \gamma^{a} \mathcal D_{a}\!\left(\varphi_{j}\right)\\
&+\frac{6}{L^{8}} E_{b} L_{ik} L^{j}{}_{l} L^{k}{}_{m} \mathcal D_{a}\!\left(L_{n}{}^{l}\right) \mathcal D^{b}\!\left(L^{nm}\right) \bar\varphi^{i} \gamma^{a} \varphi_{j}\\
&- \frac{1}{L^{6}} E_{b} L_{kl} \mathcal D_{a}\!\left(L_{i}{}^{l}\right) \mathcal D^{b}\!\left(L^{jk}\right) \bar\varphi^{i} \gamma^{a} \varphi_{j}\\
&- \frac{2}{L^{6}} E_{a} E_{b} L_{ij} L_{kl} \mathcal D^{a}\!\left(L^{li}\right) \mathcal D^{b}\!\left(L^{jk}\right)\\
&- \frac{2 i N}{L^{6}} E_{a} L^{j}{}_{k} \mathcal D^{a}\!\left(L_{i}{}^{k}\right) \bar\varphi^{i} \varphi_{j}\\
&+\frac{2}{L^{6}} E_{a} E_{b} L^{j}{}_{k} \mathcal D^{b}\!\left(L_{i}{}^{k}\right) \bar\varphi^{i} \gamma^{a} \varphi_{j}\\
&+\frac{32 i}{L^{4}} E_{a} L^{j}{}_{k} \mathcal D^{a}\!\left(L_{i}{}^{k}\right) \bar\chi^{i} \varphi_{j}
\end{aligned}
\tag{SCG1.15}
```

```math
\begin{aligned}
&+\frac{4}{L^{6}} E_{b} L_{ik} L^{j}{}_{l} \mathcal D^{b}\!\left(L^{kl}\right) \bar\varphi^{i} \gamma^{a} \mathcal D_{a}\!\left(\varphi_{j}\right)\\
&- \frac{6}{L^{8}} E_{b} L_{ik} L^{j}{}_{l} L_{mn} \mathcal D_{a}\!\left(L^{nl}\right) \mathcal D^{b}\!\left(L^{km}\right) \bar\varphi^{i} \gamma^{a} \varphi_{j}\\
&+\frac{1}{L^{6}} E_{b} L^{j}{}_{k} \mathcal D_{a}\!\left(L_{il}\right) \mathcal D^{b}\!\left(L^{lk}\right) \bar\varphi^{i} \gamma^{a} \varphi_{j}\\
&+\frac{3 i N}{L^{6}} E_{a} L_{i}{}^{j} \mathcal D^{a}\!\left(L_{k}{}^{k}\right) \bar\varphi^{i} \varphi_{j}\\
&- \frac{3}{L^{6}} E_{a} E_{b} L_{i}{}^{j} \mathcal D^{b}\!\left(L_{k}{}^{k}\right) \bar\varphi^{i} \gamma^{a} \varphi_{j}\\
&- \frac{16 i}{L^{4}} E_{a} L_{i}{}^{j} \mathcal D^{a}\!\left(L_{k}{}^{k}\right) \bar\chi^{i} \varphi_{j}\\
&- \frac{1}{L^{6}} E_{b} L_{jk} \mathcal D_{a}\!\left(L^{k}{}_{l}\right) \mathcal D^{b}\!\left(L^{lj}\right) \bar\varphi^{i} \gamma^{a} \varphi_{i}\\
&+\frac{2 i}{L^{4}} E_{c} \mathcal D^{c}\!\left(L_{j}{}^{j}\right) T_{ab} \bar\varphi^{i} \gamma^{ab} \varphi_{i}
\end{aligned}
\tag{SCG1.16}
```

```math
\begin{aligned}
&+\frac{1}{2 L^{6}} E_{a} E^{a} L_{ij} L_{kl} \mathcal D_{b}\!\left(L^{il}\right) \mathcal D^{b}\!\left(L^{kj}\right)\\
&+\frac{N^{2}}{2 L^{6}} L_{ij} L_{kl} \mathcal D_{a}\!\left(L^{il}\right) \mathcal D^{a}\!\left(L^{kj}\right)\\
&- \frac{4}{3 L^{4}} L_{ij} L_{kl} \mathcal D_{a}\!\left(L^{il}\right) \mathcal D^{a}\!\left(L^{kj}\right) T_{bc} T^{bc}\\
&- \frac{2}{L^{4}} D L_{ij} L_{kl} \mathcal D_{a}\!\left(L^{il}\right) \mathcal D^{a}\!\left(L^{kj}\right)\\
&- \frac{3 i N}{2 L^{8}} L_{i}{}^{j} L_{kl} L_{mn} \mathcal D_{a}\!\left(L^{kn}\right) \mathcal D^{a}\!\left(L^{ml}\right) \bar\varphi^{i} \varphi_{j}\\
&+\frac{3}{2 L^{8}} E_{a} L_{i}{}^{j} L_{kl} L_{mn} \mathcal D_{b}\!\left(L^{kn}\right) \mathcal D^{b}\!\left(L^{ml}\right) \bar\varphi^{i} \gamma^{a} \varphi_{j}\\
&+\frac{8 i}{L^{6}} L_{i}{}^{j} L_{kl} L_{mn} \mathcal D_{a}\!\left(L^{kn}\right) \mathcal D^{a}\!\left(L^{ml}\right) \bar\chi^{i} \varphi_{j}\\
&- \frac{1}{2 L^{6}} L_{jk} \mathcal D_{a}\!\left(L_{lm}\right) \mathcal D_{b}\!\left(L^{jm}\right) \mathcal D^{b}\!\left(L^{lk}\right) \bar\varphi^{i} \gamma^{a} \varphi_{i}
\end{aligned}
\tag{SCG1.17}
```

```math
\begin{aligned}
&- \frac{i}{L^{6}} L_{jk} L_{lm} \mathcal D_{c}\!\left(L^{jm}\right) \mathcal D^{c}\!\left(L^{lk}\right) T_{ab} \bar\varphi^{i} \gamma^{ab} \varphi_{i}\\
&- \frac{1}{L^{6}} E_{b} L_{jk} \mathcal D_{a}\!\left(L_{l}{}^{k}\right) \mathcal D^{b}\!\left(L^{lj}\right) \bar\varphi^{i} \gamma^{a} \varphi_{i}\\
&- \frac{3 i N}{2 L^{8}} L_{i}{}^{j} L_{kl} L_{mn} \mathcal D_{a}\!\left(L^{mk}\right) \mathcal D^{a}\!\left(L^{ln}\right) \bar\varphi^{i} \varphi_{j}\\
&+\frac{3 i N}{L^{8}} E_{a} L_{i}{}^{j} L_{kl} L^{k}{}_{m} \mathcal D^{a}\!\left(L^{lm}\right) \bar\varphi^{i} \varphi_{j}\\
&- \frac{3 i N}{2 L^{8}} L_{i}{}^{j} L_{kl} L_{mn} \mathcal D_{a}\!\left(L^{ml}\right) \mathcal D^{a}\!\left(L^{kn}\right) \bar\varphi^{i} \varphi_{j}\\
&+\frac{3 i N}{L^{8}} E_{a} L_{i}{}^{j} L_{kl} L^{l}{}_{m} \mathcal D^{a}\!\left(L^{km}\right) \bar\varphi^{i} \varphi_{j}\\
&+\frac{3}{2 L^{8}} E_{a} L_{i}{}^{j} L_{kl} L_{mn} \mathcal D_{b}\!\left(L^{mk}\right) \mathcal D^{b}\!\left(L^{ln}\right) \bar\varphi^{i} \gamma^{a} \varphi_{j}\\
&- \frac{3}{L^{8}} E_{a} E_{b} L_{i}{}^{j} L_{kl} L^{k}{}_{m} \mathcal D^{b}\!\left(L^{lm}\right) \bar\varphi^{i} \gamma^{a} \varphi_{j}
\end{aligned}
\tag{SCG1.18}
```

```math
\begin{aligned}
&+\frac{3}{2 L^{8}} E_{a} L_{i}{}^{j} L_{kl} L_{mn} \mathcal D_{b}\!\left(L^{ml}\right) \mathcal D^{b}\!\left(L^{kn}\right) \bar\varphi^{i} \gamma^{a} \varphi_{j}\\
&- \frac{3}{L^{8}} E_{a} E_{b} L_{i}{}^{j} L_{kl} L^{l}{}_{m} \mathcal D^{b}\!\left(L^{km}\right) \bar\varphi^{i} \gamma^{a} \varphi_{j}\\
&+\frac{8 i}{L^{6}} L_{i}{}^{j} L_{kl} L_{mn} \mathcal D_{a}\!\left(L^{mk}\right) \mathcal D^{a}\!\left(L^{ln}\right) \bar\chi^{i} \varphi_{j}\\
&- \frac{16 i}{L^{6}} E_{a} L_{i}{}^{j} L_{kl} L^{k}{}_{m} \mathcal D^{a}\!\left(L^{lm}\right) \bar\chi^{i} \varphi_{j}\\
&+\frac{8 i}{L^{6}} L_{i}{}^{j} L_{kl} L_{mn} \mathcal D_{a}\!\left(L^{ml}\right) \mathcal D^{a}\!\left(L^{kn}\right) \bar\chi^{i} \varphi_{j}\\
&- \frac{16 i}{L^{6}} E_{a} L_{i}{}^{j} L_{kl} L^{l}{}_{m} \mathcal D^{a}\!\left(L^{km}\right) \bar\chi^{i} \varphi_{j}\\
&- \frac{i}{L^{6}} L_{jk} L_{lm} \mathcal D_{c}\!\left(L^{lj}\right) \mathcal D^{c}\!\left(L^{km}\right) T_{ab} \bar\varphi^{i} \gamma^{ab} \varphi_{i}\\
&+\frac{2 i}{L^{6}} E_{c} L_{jk} L^{j}{}_{l} \mathcal D^{c}\!\left(L^{kl}\right) T_{ab} \bar\varphi^{i} \gamma^{ab} \varphi_{i}
\end{aligned}
\tag{SCG1.19}
```

```math
\begin{aligned}
&- \frac{i}{L^{6}} L_{jk} L_{lm} \mathcal D_{c}\!\left(L^{lk}\right) \mathcal D^{c}\!\left(L^{jm}\right) T_{ab} \bar\varphi^{i} \gamma^{ab} \varphi_{i}\\
&+\frac{2 i}{L^{6}} E_{c} L_{jk} L^{k}{}_{l} \mathcal D^{c}\!\left(L^{jl}\right) T_{ab} \bar\varphi^{i} \gamma^{ab} \varphi_{i}
\end{aligned}
\tag{SCG1.20}
```

**Source group 2.**

```math
\left.e^{-1}\mathcal L_{R^2}\right|_{\text{source group }2}=-g\rho'Y'^{ij}L_{ij}
\tag{SCI2}
```

Substitute (SC1)–(SC8), retain the permitted degree and collect:

```math
\begin{aligned}
\left.e^{-1}\mathcal L_{R^2}\right|_{\text{group }2}={}&- \frac{2 N g}{L^{2}} L_{ij} \Box_c\!\left(L^{ij}\right)\\
&+\frac{2 N g}{L^{2}} E_{a} E^{a}\\
&+\frac{2 N^{3} g}{L^{2}}\\
&- \frac{16 N g}{3} T_{ab} T^{ab}\\
&- 8 N g D\\
&+\frac{N g}{L^{4}} L_{ij} L_{kl} \mathcal D_{a}\!\left(L^{ik}\right) \mathcal D^{a}\!\left(L^{lj}\right)\\
&- \frac{2 N g}{L^{2}} E_{a} \mathcal D^{a}\!\left(L_{i}{}^{i}\right)\\
&- \frac{5 i N^{2} g}{L^{4}} L_{i}{}^{j} \bar\varphi^{i} \varphi_{j}
\end{aligned}
\tag{SCG2.1}
```

```math
\begin{aligned}
&+\frac{4 N g}{L^{4}} E_{a} L_{i}{}^{j} \bar\varphi^{i} \gamma^{a} \varphi_{j}\\
&- \frac{2 N g}{L^{2}} \bar\varphi^{i} \gamma^{a} \mathcal D_{a}\!\left(\varphi_{i}\right)\\
&- \frac{2 N g}{L^{4}} L^{j}{}_{k} \mathcal D_{a}\!\left(L_{i}{}^{k}\right) \bar\varphi^{i} \gamma^{a} \varphi_{j}\\
&+\frac{N g}{L^{4}} L_{ij} L_{kl} \mathcal D_{a}\!\left(L^{il}\right) \mathcal D^{a}\!\left(L^{kj}\right)\\
&- \frac{N g}{L^{4}} L_{jk} \mathcal D_{a}\!\left(L^{jk}\right) \bar\varphi^{i} \gamma^{a} \varphi_{i}\\
&- \frac{4 i N g}{L^{2}} T_{ab} \bar\varphi^{i} \gamma^{ab} \varphi_{i}\\
&+\frac{i g}{L^{4}} L_{i}{}^{j} L_{kl} \Box_c\!\left(L^{kl}\right) \bar\varphi^{i} \varphi_{j}\\
&- \frac{i g}{L^{4}} E_{a} E^{a} L_{i}{}^{j} \bar\varphi^{i} \varphi_{j}
\end{aligned}
\tag{SCG2.2}
```

```math
\begin{aligned}
&+\frac{8 i g}{3 L^{2}} L_{i}{}^{j} T_{ab} T^{ab} \bar\varphi^{i} \varphi_{j}\\
&+\frac{4 i g}{L^{2}} D L_{i}{}^{j} \bar\varphi^{i} \varphi_{j}\\
&- \frac{i g}{2 L^{6}} L_{i}{}^{j} L_{kl} L_{mn} \mathcal D_{a}\!\left(L^{km}\right) \mathcal D^{a}\!\left(L^{nl}\right) \bar\varphi^{i} \varphi_{j}\\
&+\frac{i g}{L^{4}} E_{a} L_{i}{}^{j} \mathcal D^{a}\!\left(L_{k}{}^{k}\right) \bar\varphi^{i} \varphi_{j}\\
&- \frac{i g}{2 L^{6}} L_{i}{}^{j} L_{kl} L_{mn} \mathcal D_{a}\!\left(L^{kn}\right) \mathcal D^{a}\!\left(L^{ml}\right) \bar\varphi^{i} \varphi_{j}
\end{aligned}
\tag{SCG2.3}
```

**Source group 3.**

```math
\left.e^{-1}\mathcal L_{R^2}\right|_{\text{source group }3}=-\frac12\bar\lambda'{}^i\not{\mathcal D}\lambda'_i
\tag{SCI3}
```

Substitute (SC1)–(SC8), retain the permitted degree and collect:

```math
\begin{aligned}
\left.e^{-1}\mathcal L_{R^2}\right|_{\text{group }3}={}&- \frac{2}{L} \mathcal D_{a}\!\left(\bar\varphi_{i}\right) \gamma^{a} \gamma^{b} \mathcal D_{b}\!\left(\frac{1}{L} \gamma^{c} \mathcal D_{c}\!\left(\varphi^{i}\right)\right)\\
&- \frac{16 i}{L} \mathcal D_{a}\!\left(\bar\varphi_{i}\right) \gamma^{a} \gamma^{b} \mathcal D_{b}\!\left(\frac{1}{L} L^{i}{}_{j} \chi^{j}\right)\\
&- \frac{4 i}{L} \mathcal D_{a}\!\left(\bar\varphi_{i}\right) \gamma^{a} \gamma^{b} \mathcal D_{b}\!\left(\frac{1}{L} \gamma^{cd} T_{cd} \varphi^{i}\right)\\
&+\frac{2 i}{L} \mathcal D_{a}\!\left(\bar\varphi_{i}\right) \gamma^{a} \gamma^{b} \mathcal D_{b}\!\left(\frac{N}{L^{3}} L^{i}{}_{j} \varphi^{j}\right)\\
&+\frac{2}{L} \mathcal D_{a}\!\left(\bar\varphi_{i}\right) \gamma^{a} \gamma^{b} \mathcal D_{b}\!\left(\frac{1}{L^{3}} \gamma^{c} \mathcal D_{c}\!\left(L^{i}{}_{j}\right) L^{jk} \varphi_{k}\right)\\
&- \frac{2}{L} \mathcal D_{a}\!\left(\bar\varphi_{i}\right) \gamma^{a} \gamma^{b} \mathcal D_{b}\!\left(\frac{1}{L^{3}} \gamma^{c} E_{c} L^{i}{}_{j} \varphi^{j}\right)\\
&+\frac{16 i}{L} L_{i}{}^{j} \bar\chi^{i} \gamma^{a} \mathcal D_{a}\!\left(\frac{1}{L} \gamma^{b} \mathcal D_{b}\!\left(\varphi_{j}\right)\right)\\
&- \frac{128}{L} L_{i}{}^{j} \bar\chi^{i} \gamma^{a} \mathcal D_{a}\!\left(\frac{1}{L} L_{jk} \chi^{k}\right)
\end{aligned}
\tag{SCG3.1}
```

```math
\begin{aligned}
&- \frac{32}{L} L_{i}{}^{j} \bar\chi^{i} \gamma^{a} \mathcal D_{a}\!\left(\frac{1}{L} \gamma^{bc} T_{bc} \varphi_{j}\right)\\
&+\frac{16}{L} L_{i}{}^{j} \bar\chi^{i} \gamma^{a} \mathcal D_{a}\!\left(\frac{N}{L^{3}} L_{jk} \varphi^{k}\right)\\
&- \frac{16 i}{L} L_{i}{}^{j} \bar\chi^{i} \gamma^{a} \mathcal D_{a}\!\left(\frac{1}{L^{3}} \gamma^{b} \mathcal D_{b}\!\left(L_{jk}\right) L^{kl} \varphi_{l}\right)\\
&+\frac{16 i}{L} L_{i}{}^{j} \bar\chi^{i} \gamma^{a} \mathcal D_{a}\!\left(\frac{1}{L^{3}} \gamma^{b} E_{b} L_{jk} \varphi^{k}\right)\\
&- \frac{4 i}{L} T_{ab} \bar\varphi^{i} \gamma^{ab} \gamma^{c} \mathcal D_{c}\!\left(\frac{1}{L} \gamma^{d} \mathcal D_{d}\!\left(\varphi_{i}\right)\right)\\
&+\frac{32}{L} T_{ab} \bar\varphi^{i} \gamma^{ab} \gamma^{c} \mathcal D_{c}\!\left(\frac{1}{L} L_{ij} \chi^{j}\right)\\
&+\frac{8}{L} T_{ab} \bar\varphi^{i} \gamma^{ab} \gamma^{c} \mathcal D_{c}\!\left(\frac{1}{L} \gamma^{de} T_{de} \varphi_{i}\right)\\
&- \frac{4}{L} T_{ab} \bar\varphi^{i} \gamma^{ab} \gamma^{c} \mathcal D_{c}\!\left(\frac{N}{L^{3}} L_{ij} \varphi^{j}\right)
\end{aligned}
\tag{SCG3.2}
```

```math
\begin{aligned}
&+\frac{4 i}{L} T_{ab} \bar\varphi^{i} \gamma^{ab} \gamma^{c} \mathcal D_{c}\!\left(\frac{1}{L^{3}} \gamma^{d} \mathcal D_{d}\!\left(L_{ij}\right) L^{jk} \varphi_{k}\right)\\
&- \frac{4 i}{L} T_{ab} \bar\varphi^{i} \gamma^{ab} \gamma^{c} \mathcal D_{c}\!\left(\frac{1}{L^{3}} \gamma^{d} E_{d} L_{ij} \varphi^{j}\right)\\
&- \frac{2 i N}{L^{3}} L_{i}{}^{j} \bar\varphi^{i} \gamma^{a} \mathcal D_{a}\!\left(\frac{1}{L} \gamma^{b} \mathcal D_{b}\!\left(\varphi_{j}\right)\right)\\
&+\frac{16 N}{L^{3}} L_{i}{}^{j} \bar\varphi^{i} \gamma^{a} \mathcal D_{a}\!\left(\frac{1}{L} L_{jk} \chi^{k}\right)\\
&+\frac{4 N}{L^{3}} L_{i}{}^{j} \bar\varphi^{i} \gamma^{a} \mathcal D_{a}\!\left(\frac{1}{L} \gamma^{bc} T_{bc} \varphi_{j}\right)\\
&- \frac{2 N}{L^{3}} L_{i}{}^{j} \bar\varphi^{i} \gamma^{a} \mathcal D_{a}\!\left(\frac{N}{L^{3}} L_{jk} \varphi^{k}\right)\\
&+\frac{2 i N}{L^{3}} L_{i}{}^{j} \bar\varphi^{i} \gamma^{a} \mathcal D_{a}\!\left(\frac{1}{L^{3}} \gamma^{b} \mathcal D_{b}\!\left(L_{jk}\right) L^{kl} \varphi_{l}\right)\\
&- \frac{2 i N}{L^{3}} L_{i}{}^{j} \bar\varphi^{i} \gamma^{a} \mathcal D_{a}\!\left(\frac{1}{L^{3}} \gamma^{b} E_{b} L_{jk} \varphi^{k}\right)
\end{aligned}
\tag{SCG3.3}
```

```math
\begin{aligned}
&- \frac{2}{L^{3}} L_{ik} \mathcal D_{a}\!\left(L^{jk}\right) \bar\varphi^{i} \gamma^{a} \gamma^{b} \mathcal D_{b}\!\left(\frac{1}{L} \gamma^{c} \mathcal D_{c}\!\left(\varphi_{j}\right)\right)\\
&- \frac{16 i}{L^{3}} L_{ik} \mathcal D_{a}\!\left(L^{jk}\right) \bar\varphi^{i} \gamma^{a} \gamma^{b} \mathcal D_{b}\!\left(\frac{1}{L} L_{jl} \chi^{l}\right)\\
&- \frac{4 i}{L^{3}} L_{ik} \mathcal D_{a}\!\left(L^{jk}\right) \bar\varphi^{i} \gamma^{a} \gamma^{b} \mathcal D_{b}\!\left(\frac{1}{L} \gamma^{cd} T_{cd} \varphi_{j}\right)\\
&+\frac{2 i}{L^{3}} L_{ik} \mathcal D_{a}\!\left(L^{jk}\right) \bar\varphi^{i} \gamma^{a} \gamma^{b} \mathcal D_{b}\!\left(\frac{N}{L^{3}} L_{jl} \varphi^{l}\right)\\
&+\frac{2}{L^{3}} L_{ik} \mathcal D_{a}\!\left(L^{jk}\right) \bar\varphi^{i} \gamma^{a} \gamma^{b} \mathcal D_{b}\!\left(\frac{1}{L^{3}} \gamma^{c} \mathcal D_{c}\!\left(L_{jl}\right) L^{lm} \varphi_{m}\right)\\
&- \frac{2}{L^{3}} L_{ik} \mathcal D_{a}\!\left(L^{jk}\right) \bar\varphi^{i} \gamma^{a} \gamma^{b} \mathcal D_{b}\!\left(\frac{1}{L^{3}} \gamma^{c} E_{c} L_{jl} \varphi^{l}\right)\\
&+\frac{2}{L^{3}} E_{a} L_{i}{}^{j} \bar\varphi^{i} \gamma^{a} \gamma^{b} \mathcal D_{b}\!\left(\frac{1}{L} \gamma^{c} \mathcal D_{c}\!\left(\varphi_{j}\right)\right)\\
&+\frac{16 i}{L^{3}} E_{a} L_{i}{}^{j} \bar\varphi^{i} \gamma^{a} \gamma^{b} \mathcal D_{b}\!\left(\frac{1}{L} L_{jk} \chi^{k}\right)
\end{aligned}
\tag{SCG3.4}
```

```math
\begin{aligned}
&+\frac{4 i}{L^{3}} E_{a} L_{i}{}^{j} \bar\varphi^{i} \gamma^{a} \gamma^{b} \mathcal D_{b}\!\left(\frac{1}{L} \gamma^{cd} T_{cd} \varphi_{j}\right)\\
&- \frac{2 i}{L^{3}} E_{a} L_{i}{}^{j} \bar\varphi^{i} \gamma^{a} \gamma^{b} \mathcal D_{b}\!\left(\frac{N}{L^{3}} L_{jk} \varphi^{k}\right)\\
&- \frac{2}{L^{3}} E_{a} L_{i}{}^{j} \bar\varphi^{i} \gamma^{a} \gamma^{b} \mathcal D_{b}\!\left(\frac{1}{L^{3}} \gamma^{c} \mathcal D_{c}\!\left(L_{jk}\right) L^{kl} \varphi_{l}\right)\\
&+\frac{2}{L^{3}} E_{a} L_{i}{}^{j} \bar\varphi^{i} \gamma^{a} \gamma^{b} \mathcal D_{b}\!\left(\frac{1}{L^{3}} \gamma^{c} E_{c} L_{jk} \varphi^{k}\right)
\end{aligned}
\tag{SCG3.5}
```

**Source group 4.**

```math
\left.e^{-1}\mathcal L_{R^2}\right|_{\text{source group }4}=+i\bar\lambda'{}^i\gamma\!\cdot\!T\lambda'_i
\tag{SCI4}
```

Substitute (SC1)–(SC8), retain the permitted degree and collect:

```math
\begin{aligned}
\left.e^{-1}\mathcal L_{R^2}\right|_{\text{group }4}={}&\frac{4 i}{L^{2}} T_{bc} \mathcal D_{a}\!\left(\bar\varphi_{i}\right) \gamma^{a} \gamma^{bc} \gamma^{d} \mathcal D_{d}\!\left(\varphi^{i}\right)\\
&+\frac{32}{L^{2}} L^{ij} T_{bc} \mathcal D_{a}\!\left(\bar\varphi_{i}\right) \gamma^{a} \gamma^{bc} \chi_{j}\\
&- \frac{8}{L^{2}} T_{bc} T_{de} \mathcal D_{a}\!\left(\bar\varphi_{i}\right) \gamma^{a} \gamma^{bc} \gamma^{de} \varphi^{i}\\
&- \frac{4 N}{L^{4}} L^{ij} T_{bc} \mathcal D_{a}\!\left(\bar\varphi_{i}\right) \gamma^{a} \gamma^{bc} \varphi_{j}\\
&+\frac{4 i}{L^{4}} L^{j}{}_{k} \mathcal D_{d}\!\left(L^{ik}\right) T_{bc} \mathcal D_{a}\!\left(\bar\varphi_{i}\right) \gamma^{a} \gamma^{bc} \gamma^{d} \varphi_{j}\\
&- \frac{4 i}{L^{4}} E_{d} L^{ij} T_{bc} \mathcal D_{a}\!\left(\bar\varphi_{i}\right) \gamma^{a} \gamma^{bc} \gamma^{d} \varphi_{j}\\
&+\frac{32}{L^{2}} L_{i}{}^{j} T_{ab} \bar\chi^{i} \gamma^{ab} \gamma^{c} \mathcal D_{c}\!\left(\varphi_{j}\right)\\
&+128 i T_{ab} \bar\chi^{i} \gamma^{ab} \chi_{i}
\end{aligned}
\tag{SCG4.1}
```

```math
\begin{aligned}
&+\frac{64 i}{L^{2}} L_{i}{}^{j} T_{ab} T_{cd} \bar\chi^{i} \gamma^{ab} \gamma^{cd} \varphi_{j}\\
&- \frac{16 i N}{L^{2}} T_{ab} \bar\chi^{i} \gamma^{ab} \varphi_{i}\\
&- \frac{32}{L^{4}} L_{ik} L^{j}{}_{l} \mathcal D_{c}\!\left(L^{kl}\right) T_{ab} \bar\chi^{i} \gamma^{ab} \gamma^{c} \varphi_{j}\\
&+\frac{16}{L^{2}} E_{c} T_{ab} \bar\chi^{i} \gamma^{ab} \gamma^{c} \varphi_{i}\\
&- \frac{8}{L^{2}} T_{ab} T_{cd} \bar\varphi^{i} \gamma^{ab} \gamma^{cd} \gamma^{e} \mathcal D_{e}\!\left(\varphi_{i}\right)\\
&+\frac{64 i}{L^{2}} L_{i}{}^{j} T_{ab} T_{cd} \bar\varphi^{i} \gamma^{ab} \gamma^{cd} \chi_{j}\\
&- \frac{16 i}{L^{2}} T_{ab} T_{cd} T_{ef} \bar\varphi^{i} \gamma^{ab} \gamma^{cd} \gamma^{ef} \varphi_{i}\\
&- \frac{16 i N}{L^{4}} L_{i}{}^{j} T_{ab} T_{cd} \bar\varphi^{i} \gamma^{ab} \gamma^{cd} \varphi_{j}
\end{aligned}
\tag{SCG4.2}
```

```math
\begin{aligned}
&- \frac{8}{L^{4}} L^{j}{}_{k} \mathcal D_{e}\!\left(L_{i}{}^{k}\right) T_{ab} T_{cd} \bar\varphi^{i} \gamma^{ab} \gamma^{cd} \gamma^{e} \varphi_{j}\\
&+\frac{8}{L^{4}} E_{e} L_{i}{}^{j} T_{ab} T_{cd} \bar\varphi^{i} \gamma^{ab} \gamma^{cd} \gamma^{e} \varphi_{j}\\
&- \frac{4 N}{L^{4}} L_{i}{}^{j} T_{ab} \bar\varphi^{i} \gamma^{ab} \gamma^{c} \mathcal D_{c}\!\left(\varphi_{j}\right)\\
&- \frac{16 i N}{L^{2}} T_{ab} \bar\varphi^{i} \gamma^{ab} \chi_{i}\\
&+\frac{2 i N^{2}}{L^{4}} T_{ab} \bar\varphi^{i} \gamma^{ab} \varphi_{i}\\
&+\frac{4 N}{L^{6}} L_{ik} L^{j}{}_{l} \mathcal D_{c}\!\left(L^{kl}\right) T_{ab} \bar\varphi^{i} \gamma^{ab} \gamma^{c} \varphi_{j}\\
&- \frac{2 N}{L^{4}} E_{c} T_{ab} \bar\varphi^{i} \gamma^{ab} \gamma^{c} \varphi_{i}\\
&+\frac{4 i}{L^{4}} L_{ik} \mathcal D_{a}\!\left(L^{jk}\right) T_{bc} \bar\varphi^{i} \gamma^{a} \gamma^{bc} \gamma^{d} \mathcal D_{d}\!\left(\varphi_{j}\right)
\end{aligned}
\tag{SCG4.3}
```

```math
\begin{aligned}
&+\frac{32}{L^{4}} L_{ik} L^{j}{}_{l} \mathcal D_{a}\!\left(L^{lk}\right) T_{bc} \bar\varphi^{i} \gamma^{a} \gamma^{bc} \chi_{j}\\
&- \frac{8}{L^{4}} L_{ik} \mathcal D_{a}\!\left(L^{jk}\right) T_{bc} T_{de} \bar\varphi^{i} \gamma^{a} \gamma^{bc} \gamma^{de} \varphi_{j}\\
&- \frac{4 N}{L^{6}} L_{ik} L^{j}{}_{l} \mathcal D_{a}\!\left(L^{lk}\right) T_{bc} \bar\varphi^{i} \gamma^{a} \gamma^{bc} \varphi_{j}\\
&- \frac{4 i}{L^{6}} L_{ik} L^{j}{}_{l} \mathcal D_{a}\!\left(L_{m}{}^{k}\right) \mathcal D_{d}\!\left(L^{ml}\right) T_{bc} \bar\varphi^{i} \gamma^{a} \gamma^{bc} \gamma^{d} \varphi_{j}\\
&- \frac{4 i}{L^{6}} E_{d} L_{ik} L^{j}{}_{l} \mathcal D_{a}\!\left(L^{lk}\right) T_{bc} \bar\varphi^{i} \gamma^{a} \gamma^{bc} \gamma^{d} \varphi_{j}\\
&- \frac{4 i}{L^{4}} E_{a} L_{i}{}^{j} T_{bc} \bar\varphi^{i} \gamma^{a} \gamma^{bc} \gamma^{d} \mathcal D_{d}\!\left(\varphi_{j}\right)\\
&+\frac{16}{L^{2}} E_{a} T_{bc} \bar\varphi^{i} \gamma^{a} \gamma^{bc} \chi_{i}\\
&+\frac{8}{L^{4}} E_{a} L_{i}{}^{j} T_{bc} T_{de} \bar\varphi^{i} \gamma^{a} \gamma^{bc} \gamma^{de} \varphi_{j}
\end{aligned}
\tag{SCG4.4}
```

```math
\begin{aligned}
&- \frac{2 N}{L^{4}} E_{a} T_{bc} \bar\varphi^{i} \gamma^{a} \gamma^{bc} \varphi_{i}\\
&+\frac{4 i}{L^{6}} E_{a} L_{ik} L^{j}{}_{l} \mathcal D_{d}\!\left(L^{kl}\right) T_{bc} \bar\varphi^{i} \gamma^{a} \gamma^{bc} \gamma^{d} \varphi_{j}\\
&- \frac{2 i}{L^{4}} E_{a} E_{d} T_{bc} \bar\varphi^{i} \gamma^{a} \gamma^{bc} \gamma^{d} \varphi_{i}
\end{aligned}
\tag{SCG4.5}
```

**Source group 5.**

```math
\left.e^{-1}\mathcal L_{R^2}\right|_{\text{source group }5}=-8i\rho'\bar\lambda'{}^i\chi_i
\tag{SCI5}
```

Substitute (SC1)–(SC8), retain the permitted degree and collect:

```math
\begin{aligned}
\left.e^{-1}\mathcal L_{R^2}\right|_{\text{group }5}={}&\frac{32 N}{L^{2}} \mathcal D_{a}\!\left(\bar\varphi_{i}\right) \gamma^{a} \chi^{i}\\
&- \frac{256 i N}{L^{2}} L_{i}{}^{j} \bar\chi^{i} \chi_{j}\\
&+\frac{64 i N}{L^{2}} T_{ab} \bar\varphi^{i} \gamma^{ab} \chi_{i}\\
&+\frac{32 i N^{2}}{L^{4}} L_{i}{}^{j} \bar\varphi^{i} \chi_{j}\\
&+\frac{32 N}{L^{4}} L_{ik} \mathcal D_{a}\!\left(L^{jk}\right) \bar\varphi^{i} \gamma^{a} \chi_{j}\\
&- \frac{32 N}{L^{4}} E_{a} L_{i}{}^{j} \bar\varphi^{i} \gamma^{a} \chi_{j}
\end{aligned}
\tag{SCG5.1}
```

**Source group 6.**

```math
\left.e^{-1}\mathcal L_{R^2}\right|_{\text{source group }6}=-\frac i8\bar\lambda'{}^i\gamma\!\cdot\!\widehat G\lambda'_i
\tag{SCI6}
```

Substitute (SC1)–(SC8), retain the permitted degree and collect:

```math
\begin{aligned}
\left.e^{-1}\mathcal L_{R^2}\right|_{\text{group }6}={}&- \frac{i}{2 L^{2}} \widehat G_{bc} \mathcal D_{a}\!\left(\bar\varphi_{i}\right) \gamma^{a} \gamma^{bc} \gamma^{d} \mathcal D_{d}\!\left(\varphi^{i}\right)\\
&- \frac{4}{L^{2}} \widehat G_{bc} L^{ij} \mathcal D_{a}\!\left(\bar\varphi_{i}\right) \gamma^{a} \gamma^{bc} \chi_{j}\\
&+\frac{1}{L^{2}} \widehat G_{bc} T_{de} \mathcal D_{a}\!\left(\bar\varphi_{i}\right) \gamma^{a} \gamma^{bc} \gamma^{de} \varphi^{i}\\
&+\frac{N}{2 L^{4}} \widehat G_{bc} L^{ij} \mathcal D_{a}\!\left(\bar\varphi_{i}\right) \gamma^{a} \gamma^{bc} \varphi_{j}\\
&- \frac{i}{2 L^{4}} \widehat G_{bc} L^{j}{}_{k} \mathcal D_{d}\!\left(L^{ik}\right) \mathcal D_{a}\!\left(\bar\varphi_{i}\right) \gamma^{a} \gamma^{bc} \gamma^{d} \varphi_{j}\\
&+\frac{i}{2 L^{4}} E_{d} \widehat G_{bc} L^{ij} \mathcal D_{a}\!\left(\bar\varphi_{i}\right) \gamma^{a} \gamma^{bc} \gamma^{d} \varphi_{j}\\
&- \frac{4}{L^{2}} \widehat G_{ab} L_{i}{}^{j} \bar\chi^{i} \gamma^{ab} \gamma^{c} \mathcal D_{c}\!\left(\varphi_{j}\right)\\
&- 16 i \widehat G_{ab} \bar\chi^{i} \gamma^{ab} \chi_{i}
\end{aligned}
\tag{SCG6.1}
```

```math
\begin{aligned}
&- \frac{8 i}{L^{2}} \widehat G_{ab} L_{i}{}^{j} T_{cd} \bar\chi^{i} \gamma^{ab} \gamma^{cd} \varphi_{j}\\
&+\frac{2 i N}{L^{2}} \widehat G_{ab} \bar\chi^{i} \gamma^{ab} \varphi_{i}\\
&+\frac{4}{L^{4}} \widehat G_{ab} L_{ik} L^{j}{}_{l} \mathcal D_{c}\!\left(L^{kl}\right) \bar\chi^{i} \gamma^{ab} \gamma^{c} \varphi_{j}\\
&- \frac{2}{L^{2}} E_{c} \widehat G_{ab} \bar\chi^{i} \gamma^{ab} \gamma^{c} \varphi_{i}\\
&+\frac{1}{L^{2}} \widehat G_{cd} T_{ab} \bar\varphi^{i} \gamma^{ab} \gamma^{cd} \gamma^{e} \mathcal D_{e}\!\left(\varphi_{i}\right)\\
&- \frac{8 i}{L^{2}} \widehat G_{cd} L_{i}{}^{j} T_{ab} \bar\varphi^{i} \gamma^{ab} \gamma^{cd} \chi_{j}\\
&+\frac{2 i}{L^{2}} \widehat G_{cd} T_{ab} T_{ef} \bar\varphi^{i} \gamma^{ab} \gamma^{cd} \gamma^{ef} \varphi_{i}\\
&+\frac{i N}{L^{4}} \widehat G_{cd} L_{i}{}^{j} T_{ab} \bar\varphi^{i} \gamma^{ab} \gamma^{cd} \varphi_{j}
\end{aligned}
\tag{SCG6.2}
```

```math
\begin{aligned}
&+\frac{1}{L^{4}} \widehat G_{cd} L^{j}{}_{k} \mathcal D_{e}\!\left(L_{i}{}^{k}\right) T_{ab} \bar\varphi^{i} \gamma^{ab} \gamma^{cd} \gamma^{e} \varphi_{j}\\
&- \frac{1}{L^{4}} E_{e} \widehat G_{cd} L_{i}{}^{j} T_{ab} \bar\varphi^{i} \gamma^{ab} \gamma^{cd} \gamma^{e} \varphi_{j}\\
&+\frac{N}{2 L^{4}} \widehat G_{ab} L_{i}{}^{j} \bar\varphi^{i} \gamma^{ab} \gamma^{c} \mathcal D_{c}\!\left(\varphi_{j}\right)\\
&+\frac{2 i N}{L^{2}} \widehat G_{ab} \bar\varphi^{i} \gamma^{ab} \chi_{i}\\
&+\frac{i N}{L^{4}} \widehat G_{ab} L_{i}{}^{j} T_{cd} \bar\varphi^{i} \gamma^{ab} \gamma^{cd} \varphi_{j}\\
&- \frac{i N^{2}}{4 L^{4}} \widehat G_{ab} \bar\varphi^{i} \gamma^{ab} \varphi_{i}\\
&- \frac{N}{2 L^{6}} \widehat G_{ab} L_{ik} L^{j}{}_{l} \mathcal D_{c}\!\left(L^{kl}\right) \bar\varphi^{i} \gamma^{ab} \gamma^{c} \varphi_{j}\\
&+\frac{N}{4 L^{4}} E_{c} \widehat G_{ab} \bar\varphi^{i} \gamma^{ab} \gamma^{c} \varphi_{i}
\end{aligned}
\tag{SCG6.3}
```

```math
\begin{aligned}
&- \frac{i}{2 L^{4}} \widehat G_{bc} L_{ik} \mathcal D_{a}\!\left(L^{jk}\right) \bar\varphi^{i} \gamma^{a} \gamma^{bc} \gamma^{d} \mathcal D_{d}\!\left(\varphi_{j}\right)\\
&- \frac{4}{L^{4}} \widehat G_{bc} L_{ik} L^{j}{}_{l} \mathcal D_{a}\!\left(L^{lk}\right) \bar\varphi^{i} \gamma^{a} \gamma^{bc} \chi_{j}\\
&+\frac{1}{L^{4}} \widehat G_{bc} L_{ik} \mathcal D_{a}\!\left(L^{jk}\right) T_{de} \bar\varphi^{i} \gamma^{a} \gamma^{bc} \gamma^{de} \varphi_{j}\\
&+\frac{N}{2 L^{6}} \widehat G_{bc} L_{ik} L^{j}{}_{l} \mathcal D_{a}\!\left(L^{lk}\right) \bar\varphi^{i} \gamma^{a} \gamma^{bc} \varphi_{j}\\
&+\frac{i}{2 L^{6}} \widehat G_{bc} L_{ik} L^{j}{}_{l} \mathcal D_{a}\!\left(L_{m}{}^{k}\right) \mathcal D_{d}\!\left(L^{ml}\right) \bar\varphi^{i} \gamma^{a} \gamma^{bc} \gamma^{d} \varphi_{j}\\
&+\frac{i}{2 L^{6}} E_{d} \widehat G_{bc} L_{ik} L^{j}{}_{l} \mathcal D_{a}\!\left(L^{lk}\right) \bar\varphi^{i} \gamma^{a} \gamma^{bc} \gamma^{d} \varphi_{j}\\
&+\frac{i}{2 L^{4}} E_{a} \widehat G_{bc} L_{i}{}^{j} \bar\varphi^{i} \gamma^{a} \gamma^{bc} \gamma^{d} \mathcal D_{d}\!\left(\varphi_{j}\right)\\
&- \frac{2}{L^{2}} E_{a} \widehat G_{bc} \bar\varphi^{i} \gamma^{a} \gamma^{bc} \chi_{i}
\end{aligned}
\tag{SCG6.4}
```

```math
\begin{aligned}
&- \frac{1}{L^{4}} E_{a} \widehat G_{bc} L_{i}{}^{j} T_{de} \bar\varphi^{i} \gamma^{a} \gamma^{bc} \gamma^{de} \varphi_{j}\\
&+\frac{N}{4 L^{4}} E_{a} \widehat G_{bc} \bar\varphi^{i} \gamma^{a} \gamma^{bc} \varphi_{i}\\
&- \frac{i}{2 L^{6}} E_{a} \widehat G_{bc} L_{ik} L^{j}{}_{l} \mathcal D_{d}\!\left(L^{kl}\right) \bar\varphi^{i} \gamma^{a} \gamma^{bc} \gamma^{d} \varphi_{j}\\
&+\frac{i}{4 L^{4}} E_{a} E_{d} \widehat G_{bc} \bar\varphi^{i} \gamma^{a} \gamma^{bc} \gamma^{d} \varphi_{i}
\end{aligned}
\tag{SCG6.5}
```

**Source group 7.**

```math
\left.e^{-1}\mathcal L_{R^2}\right|_{\text{source group }7}=+\frac{ig}4\bar\lambda'{}^iL_{ij}\lambda'{}^j
\tag{SCI7}
```

Substitute (SC1)–(SC8), retain the permitted degree and collect:

```math
\begin{aligned}
\left.e^{-1}\mathcal L_{R^2}\right|_{\text{group }7}={}&- \frac{i g}{L^{2}} L^{ij} \mathcal D_{a}\!\left(\bar\varphi_{i}\right) \gamma^{a} \gamma^{b} \mathcal D_{b}\!\left(\varphi_{j}\right)\\
&+4 g \mathcal D_{a}\!\left(\bar\varphi_{i}\right) \gamma^{a} \chi^{i}\\
&+\frac{2 g}{L^{2}} L^{ij} T_{bc} \mathcal D_{a}\!\left(\bar\varphi_{i}\right) \gamma^{a} \gamma^{bc} \varphi_{j}\\
&- \frac{N g}{2 L^{2}} \mathcal D_{a}\!\left(\bar\varphi_{i}\right) \gamma^{a} \varphi^{i}\\
&+\frac{i g}{L^{4}} L^{i}{}_{k} L^{j}{}_{l} \mathcal D_{b}\!\left(L^{kl}\right) \mathcal D_{a}\!\left(\bar\varphi_{i}\right) \gamma^{a} \gamma^{b} \varphi_{j}\\
&- \frac{i g}{2 L^{2}} E_{b} \mathcal D_{a}\!\left(\bar\varphi_{i}\right) \gamma^{a} \gamma^{b} \varphi^{i}\\
&+4 g \bar\chi^{i} \gamma^{a} \mathcal D_{a}\!\left(\varphi_{i}\right)\\
&- 32 i g L_{i}{}^{j} \bar\chi^{i} \chi_{j}
\end{aligned}
\tag{SCG7.1}
```

```math
\begin{aligned}
&+8 i g T_{ab} \bar\chi^{i} \gamma^{ab} \varphi_{i}\\
&+\frac{4 i N g}{L^{2}} L_{i}{}^{j} \bar\chi^{i} \varphi_{j}\\
&+\frac{4 g}{L^{2}} L^{j}{}_{k} \mathcal D_{a}\!\left(L_{i}{}^{k}\right) \bar\chi^{i} \gamma^{a} \varphi_{j}\\
&- \frac{4 g}{L^{2}} E_{a} L_{i}{}^{j} \bar\chi^{i} \gamma^{a} \varphi_{j}\\
&+\frac{2 g}{L^{2}} L_{i}{}^{j} T_{ab} \bar\varphi^{i} \gamma^{ab} \gamma^{c} \mathcal D_{c}\!\left(\varphi_{j}\right)\\
&+8 i g T_{ab} \bar\varphi^{i} \gamma^{ab} \chi_{i}\\
&+\frac{4 i g}{L^{2}} L_{i}{}^{j} T_{ab} T_{cd} \bar\varphi^{i} \gamma^{ab} \gamma^{cd} \varphi_{j}\\
&- \frac{2 i N g}{L^{2}} T_{ab} \bar\varphi^{i} \gamma^{ab} \varphi_{i}
\end{aligned}
\tag{SCG7.2}
```

```math
\begin{aligned}
&- \frac{2 g}{L^{4}} L_{ik} L^{j}{}_{l} \mathcal D_{c}\!\left(L^{kl}\right) T_{ab} \bar\varphi^{i} \gamma^{ab} \gamma^{c} \varphi_{j}\\
&+\frac{g}{L^{2}} E_{c} T_{ab} \bar\varphi^{i} \gamma^{ab} \gamma^{c} \varphi_{i}\\
&- \frac{N g}{2 L^{2}} \bar\varphi^{i} \gamma^{a} \mathcal D_{a}\!\left(\varphi_{i}\right)\\
&+\frac{4 i N g}{L^{2}} L_{i}{}^{j} \bar\varphi^{i} \chi_{j}\\
&- \frac{i N^{2} g}{2 L^{4}} L_{i}{}^{j} \bar\varphi^{i} \varphi_{j}\\
&- \frac{N g}{2 L^{4}} L^{j}{}_{k} \mathcal D_{a}\!\left(L_{i}{}^{k}\right) \bar\varphi^{i} \gamma^{a} \varphi_{j}\\
&+\frac{N g}{L^{4}} E_{a} L_{i}{}^{j} \bar\varphi^{i} \gamma^{a} \varphi_{j}\\
&- \frac{i g}{L^{4}} L_{ik} L^{j}{}_{l} \mathcal D_{a}\!\left(L^{lk}\right) \bar\varphi^{i} \gamma^{a} \gamma^{b} \mathcal D_{b}\!\left(\varphi_{j}\right)
\end{aligned}
\tag{SCG7.3}
```

```math
\begin{aligned}
&+\frac{4 g}{L^{2}} L_{ik} \mathcal D_{a}\!\left(L^{jk}\right) \bar\varphi^{i} \gamma^{a} \chi_{j}\\
&+\frac{2 g}{L^{4}} L_{ik} L^{j}{}_{l} \mathcal D_{a}\!\left(L^{lk}\right) T_{bc} \bar\varphi^{i} \gamma^{a} \gamma^{bc} \varphi_{j}\\
&- \frac{N g}{2 L^{4}} L_{ik} \mathcal D_{a}\!\left(L^{jk}\right) \bar\varphi^{i} \gamma^{a} \varphi_{j}\\
&+\frac{i g}{L^{6}} L_{ik} L^{j}{}_{l} L_{mn} \mathcal D_{a}\!\left(L^{mk}\right) \mathcal D_{b}\!\left(L^{nl}\right) \bar\varphi^{i} \gamma^{a} \gamma^{b} \varphi_{j}\\
&- \frac{i g}{2 L^{4}} E_{b} L_{ik} \mathcal D_{a}\!\left(L^{jk}\right) \bar\varphi^{i} \gamma^{a} \gamma^{b} \varphi_{j}\\
&- \frac{i g}{2 L^{2}} E_{a} \bar\varphi^{i} \gamma^{a} \gamma^{b} \mathcal D_{b}\!\left(\varphi_{i}\right)\\
&- \frac{4 g}{L^{2}} E_{a} L_{i}{}^{j} \bar\varphi^{i} \gamma^{a} \chi_{j}\\
&+\frac{g}{L^{2}} E_{a} T_{bc} \bar\varphi^{i} \gamma^{a} \gamma^{bc} \varphi_{i}
\end{aligned}
\tag{SCG7.4}
```

```math
\begin{aligned}
&- \frac{i g}{2 L^{4}} E_{a} L^{j}{}_{k} \mathcal D_{b}\!\left(L_{i}{}^{k}\right) \bar\varphi^{i} \gamma^{a} \gamma^{b} \varphi_{j}\\
&+\frac{i g}{2 L^{4}} E_{a} E_{b} L_{i}{}^{j} \bar\varphi^{i} \gamma^{a} \gamma^{b} \varphi_{j}
\end{aligned}
\tag{SCG7.5}
```

**Source group 8.**

```math
\left.e^{-1}\mathcal L_{R^2}\right|_{\text{source group }8}=+\frac g4\rho'\bar\psi_a{}^i\gamma^a\lambda'{}^jL_{ij}
\tag{SCI8}
```

Substitute (SC1)–(SC8), retain the permitted degree and collect:

```math
\begin{aligned}
\left.e^{-1}\mathcal L_{R^2}\right|_{\text{group }8}={}&\frac{i N g}{L^{2}} L_{i}{}^{j} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{b} \mathcal D_{b}\!\left(\varphi_{j}\right)\\
&- 4 N g \bar\psi_{a}{}^{i} \gamma^{a} \chi_{i}\\
&- \frac{2 N g}{L^{2}} L_{i}{}^{j} T_{bc} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{bc} \varphi_{j}\\
&+\frac{N^{2} g}{2 L^{2}} \bar\psi_{a}{}^{i} \gamma^{a} \varphi_{i}\\
&- \frac{i N g}{L^{4}} L_{ik} L^{j}{}_{l} \mathcal D_{b}\!\left(L^{kl}\right) \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{b} \varphi_{j}\\
&+\frac{i N g}{2 L^{2}} E_{b} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{b} \varphi_{i}
\end{aligned}
\tag{SCG8.1}
```

**Source group 9.**

```math
\left.e^{-1}\mathcal L_{R^2}\right|_{\text{source group }9}=-\frac12\bar\psi_a{}^i\gamma^a\lambda'{}^jY'_{ij}
\tag{SCI9}
```

Substitute (SC1)–(SC8), retain the permitted degree and collect:

```math
\begin{aligned}
\left.e^{-1}\mathcal L_{R^2}\right|_{\text{group }9}={}&- \frac{i}{L^{2}} \Box_c\!\left(L_{i}{}^{j}\right) \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{b} \mathcal D_{b}\!\left(\varphi_{j}\right)\\
&+\frac{i}{L^{4}} E_{c} E^{c} L_{i}{}^{j} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{b} \mathcal D_{b}\!\left(\varphi_{j}\right)\\
&+\frac{i N^{2}}{L^{4}} L_{i}{}^{j} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{b} \mathcal D_{b}\!\left(\varphi_{j}\right)\\
&- \frac{8 i}{3 L^{2}} L_{i}{}^{j} T_{cd} T^{cd} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{b} \mathcal D_{b}\!\left(\varphi_{j}\right)\\
&- \frac{4 i}{L^{2}} D L_{i}{}^{j} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{b} \mathcal D_{b}\!\left(\varphi_{j}\right)\\
&+\frac{i}{2 L^{4}} L_{kl} \mathcal D_{c}\!\left(L^{k}{}_{i}\right) \mathcal D^{c}\!\left(L^{jl}\right) \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{b} \mathcal D_{b}\!\left(\varphi_{j}\right)\\
&- \frac{i}{L^{4}} E_{c} L_{ik} \mathcal D^{c}\!\left(L^{jk}\right) \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{b} \mathcal D_{b}\!\left(\varphi_{j}\right)\\
&+\frac{i}{2 L^{4}} L_{kl} \mathcal D_{c}\!\left(L^{kj}\right) \mathcal D^{c}\!\left(L_{i}{}^{l}\right) \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{b} \mathcal D_{b}\!\left(\varphi_{j}\right)
\end{aligned}
\tag{SCG9.1}
```

```math
\begin{aligned}
&- \frac{i}{L^{4}} E_{c} L^{j}{}_{k} \mathcal D^{c}\!\left(L_{i}{}^{k}\right) \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{b} \mathcal D_{b}\!\left(\varphi_{j}\right)\\
&- \frac{8}{L^{2}} L^{j}{}_{k} \Box_c\!\left(L_{i}{}^{k}\right) \bar\psi_{a}{}^{i} \gamma^{a} \chi_{j}\\
&- \frac{4}{L^{2}} E_{b} E^{b} \bar\psi_{a}{}^{i} \gamma^{a} \chi_{i}\\
&- \frac{4 N^{2}}{L^{2}} \bar\psi_{a}{}^{i} \gamma^{a} \chi_{i}\\
&+\frac{32}{3} T_{bc} T^{bc} \bar\psi_{a}{}^{i} \gamma^{a} \chi_{i}\\
&+16 D \bar\psi_{a}{}^{i} \gamma^{a} \chi_{i}\\
&+\frac{4}{L^{4}} L^{j}{}_{k} L_{lm} \mathcal D_{b}\!\left(L^{l}{}_{i}\right) \mathcal D^{b}\!\left(L^{km}\right) \bar\psi_{a}{}^{i} \gamma^{a} \chi_{j}\\
&- \frac{8}{L^{4}} E_{b} L_{ik} L^{j}{}_{l} \mathcal D^{b}\!\left(L^{lk}\right) \bar\psi_{a}{}^{i} \gamma^{a} \chi_{j}
\end{aligned}
\tag{SCG9.2}
```

```math
\begin{aligned}
&+\frac{4}{L^{4}} L^{j}{}_{k} L_{lm} \mathcal D_{b}\!\left(L^{lk}\right) \mathcal D^{b}\!\left(L_{i}{}^{m}\right) \bar\psi_{a}{}^{i} \gamma^{a} \chi_{j}\\
&- \frac{8}{L^{4}} E_{b} L^{j}{}_{k} L^{k}{}_{l} \mathcal D^{b}\!\left(L_{i}{}^{l}\right) \bar\psi_{a}{}^{i} \gamma^{a} \chi_{j}\\
&+\frac{2}{L^{2}} \Box_c\!\left(L_{i}{}^{j}\right) T_{bc} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{bc} \varphi_{j}\\
&- \frac{2}{L^{4}} E_{d} E^{d} L_{i}{}^{j} T_{bc} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{bc} \varphi_{j}\\
&- \frac{2 N^{2}}{L^{4}} L_{i}{}^{j} T_{bc} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{bc} \varphi_{j}\\
&+\frac{16}{3 L^{2}} L_{i}{}^{j} T_{bc} T_{de} T^{de} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{bc} \varphi_{j}\\
&+\frac{8}{L^{2}} D L_{i}{}^{j} T_{bc} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{bc} \varphi_{j}\\
&- \frac{1}{L^{4}} L_{kl} \mathcal D_{d}\!\left(L^{k}{}_{i}\right) \mathcal D^{d}\!\left(L^{jl}\right) T_{bc} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{bc} \varphi_{j}
\end{aligned}
\tag{SCG9.3}
```

```math
\begin{aligned}
&+\frac{2}{L^{4}} E_{d} L_{ik} \mathcal D^{d}\!\left(L^{jk}\right) T_{bc} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{bc} \varphi_{j}\\
&- \frac{1}{L^{4}} L_{kl} \mathcal D_{d}\!\left(L^{kj}\right) \mathcal D^{d}\!\left(L_{i}{}^{l}\right) T_{bc} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{bc} \varphi_{j}\\
&+\frac{2}{L^{4}} E_{d} L^{j}{}_{k} \mathcal D^{d}\!\left(L_{i}{}^{k}\right) T_{bc} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{bc} \varphi_{j}\\
&+\frac{N}{L^{4}} L^{j}{}_{k} \Box_c\!\left(L_{i}{}^{k}\right) \bar\psi_{a}{}^{i} \gamma^{a} \varphi_{j}\\
&+\frac{N}{2 L^{4}} E_{b} E^{b} \bar\psi_{a}{}^{i} \gamma^{a} \varphi_{i}\\
&+\frac{N^{3}}{2 L^{4}} \bar\psi_{a}{}^{i} \gamma^{a} \varphi_{i}\\
&- \frac{4 N}{3 L^{2}} T_{bc} T^{bc} \bar\psi_{a}{}^{i} \gamma^{a} \varphi_{i}\\
&- \frac{2 N}{L^{2}} D \bar\psi_{a}{}^{i} \gamma^{a} \varphi_{i}
\end{aligned}
\tag{SCG9.4}
```

```math
\begin{aligned}
&- \frac{N}{2 L^{6}} L^{j}{}_{k} L_{lm} \mathcal D_{b}\!\left(L^{l}{}_{i}\right) \mathcal D^{b}\!\left(L^{km}\right) \bar\psi_{a}{}^{i} \gamma^{a} \varphi_{j}\\
&+\frac{N}{L^{6}} E_{b} L_{ik} L^{j}{}_{l} \mathcal D^{b}\!\left(L^{lk}\right) \bar\psi_{a}{}^{i} \gamma^{a} \varphi_{j}\\
&- \frac{N}{2 L^{6}} L^{j}{}_{k} L_{lm} \mathcal D_{b}\!\left(L^{lk}\right) \mathcal D^{b}\!\left(L_{i}{}^{m}\right) \bar\psi_{a}{}^{i} \gamma^{a} \varphi_{j}\\
&+\frac{N}{L^{6}} E_{b} L^{j}{}_{k} L^{k}{}_{l} \mathcal D^{b}\!\left(L_{i}{}^{l}\right) \bar\psi_{a}{}^{i} \gamma^{a} \varphi_{j}\\
&+\frac{i}{L^{4}} L^{j}{}_{k} \Box_c\!\left(L_{il}\right) \mathcal D_{b}\!\left(L^{lk}\right) \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{b} \varphi_{j}\\
&- \frac{i}{L^{6}} E_{c} E^{c} L_{ik} L^{j}{}_{l} \mathcal D_{b}\!\left(L^{kl}\right) \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{b} \varphi_{j}\\
&- \frac{i N^{2}}{L^{6}} L_{ik} L^{j}{}_{l} \mathcal D_{b}\!\left(L^{kl}\right) \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{b} \varphi_{j}\\
&+\frac{8 i}{3 L^{4}} L_{ik} L^{j}{}_{l} \mathcal D_{b}\!\left(L^{kl}\right) T_{cd} T^{cd} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{b} \varphi_{j}
\end{aligned}
\tag{SCG9.5}
```

```math
\begin{aligned}
&+\frac{4 i}{L^{4}} D L_{ik} L^{j}{}_{l} \mathcal D_{b}\!\left(L^{kl}\right) \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{b} \varphi_{j}\\
&+\frac{i}{2 L^{6}} L^{j}{}_{k} L_{lm} \mathcal D_{b}\!\left(L_{n}{}^{k}\right) \mathcal D_{c}\!\left(L^{l}{}_{i}\right) \mathcal D^{c}\!\left(L^{nm}\right) \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{b} \varphi_{j}\\
&- \frac{i}{L^{6}} E_{c} L_{ik} L^{j}{}_{l} \mathcal D_{b}\!\left(L_{m}{}^{l}\right) \mathcal D^{c}\!\left(L^{mk}\right) \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{b} \varphi_{j}\\
&+\frac{i}{2 L^{6}} L^{j}{}_{k} L_{lm} \mathcal D_{b}\!\left(L_{n}{}^{k}\right) \mathcal D_{c}\!\left(L^{ln}\right) \mathcal D^{c}\!\left(L_{i}{}^{m}\right) \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{b} \varphi_{j}\\
&+\frac{i}{L^{6}} E_{c} L^{j}{}_{k} L_{lm} \mathcal D_{b}\!\left(L^{mk}\right) \mathcal D^{c}\!\left(L_{i}{}^{l}\right) \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{b} \varphi_{j}\\
&+\frac{i}{L^{4}} E_{b} L^{j}{}_{k} \Box_c\!\left(L_{i}{}^{k}\right) \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{b} \varphi_{j}\\
&+\frac{i}{2 L^{4}} E_{b} E_{c} E^{c} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{b} \varphi_{i}\\
&+\frac{i N^{2}}{2 L^{4}} E_{b} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{b} \varphi_{i}
\end{aligned}
\tag{SCG9.6}
```

```math
\begin{aligned}
&- \frac{4 i}{3 L^{2}} E_{b} T_{cd} T^{cd} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{b} \varphi_{i}\\
&- \frac{2 i}{L^{2}} D E_{b} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{b} \varphi_{i}\\
&- \frac{i}{2 L^{6}} E_{b} L^{j}{}_{k} L_{lm} \mathcal D_{c}\!\left(L^{l}{}_{i}\right) \mathcal D^{c}\!\left(L^{km}\right) \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{b} \varphi_{j}\\
&+\frac{i}{L^{6}} E_{b} E_{c} L_{ik} L^{j}{}_{l} \mathcal D^{c}\!\left(L^{lk}\right) \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{b} \varphi_{j}\\
&- \frac{i}{2 L^{6}} E_{b} L^{j}{}_{k} L_{lm} \mathcal D_{c}\!\left(L^{lk}\right) \mathcal D^{c}\!\left(L_{i}{}^{m}\right) \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{b} \varphi_{j}\\
&+\frac{i}{L^{6}} E_{b} E_{c} L^{j}{}_{k} L^{k}{}_{l} \mathcal D^{c}\!\left(L_{i}{}^{l}\right) \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{b} \varphi_{j}
\end{aligned}
\tag{SCG9.7}
```

**Source group 10.**

```math
\left.e^{-1}\mathcal L_{R^2}\right|_{\text{source group }10}=-\frac{3\rho'}4\bar\lambda'{}^i\gamma^a [\frac14\gamma\!\cdot\!\widehat G\psi_{ai} -\gamma\!\cdot\!T\psi_{ai}+\frac g2L_{ij}\psi_a{}^j-\phi_{ai}]
\tag{SCI10}
```

Substitute (SC1)–(SC8), retain the permitted degree and collect:

```math
\begin{aligned}
\left.e^{-1}\mathcal L_{R^2}\right|_{\text{group }10}={}&- \frac{3 i N}{4 L^{2}} \widehat G_{cd} \mathcal D_{a}\!\left(\bar\varphi_{i}\right) \gamma^{a} \gamma^{b} \gamma^{cd} \psi_{b}{}^{i}\\
&- \frac{6 N}{L^{2}} \widehat G_{bc} L_{i}{}^{j} \bar\chi^{i} \gamma^{a} \gamma^{bc} \psi_{aj}\\
&+\frac{3 N}{2 L^{2}} \widehat G_{de} T_{ab} \bar\varphi^{i} \gamma^{ab} \gamma^{c} \gamma^{de} \psi_{ci}\\
&+\frac{3 N^{2}}{4 L^{4}} \widehat G_{bc} L_{i}{}^{j} \bar\varphi^{i} \gamma^{a} \gamma^{bc} \psi_{aj}\\
&- \frac{3 i N}{4 L^{4}} \widehat G_{cd} L_{ik} \mathcal D_{a}\!\left(L^{jk}\right) \bar\varphi^{i} \gamma^{a} \gamma^{b} \gamma^{cd} \psi_{bj}\\
&+\frac{3 i N}{4 L^{4}} E_{a} \widehat G_{cd} L_{i}{}^{j} \bar\varphi^{i} \gamma^{a} \gamma^{b} \gamma^{cd} \psi_{bj}\\
&+\frac{3 i N}{L^{2}} T_{cd} \mathcal D_{a}\!\left(\bar\varphi_{i}\right) \gamma^{a} \gamma^{b} \gamma^{cd} \psi_{b}{}^{i}\\
&+\frac{24 N}{L^{2}} L_{i}{}^{j} T_{bc} \bar\chi^{i} \gamma^{a} \gamma^{bc} \psi_{aj}
\end{aligned}
\tag{SCG10.1}
```

```math
\begin{aligned}
&- \frac{6 N}{L^{2}} T_{ab} T_{de} \bar\varphi^{i} \gamma^{ab} \gamma^{c} \gamma^{de} \psi_{ci}\\
&- \frac{3 N^{2}}{L^{4}} L_{i}{}^{j} T_{bc} \bar\varphi^{i} \gamma^{a} \gamma^{bc} \psi_{aj}\\
&+\frac{3 i N}{L^{4}} L_{ik} \mathcal D_{a}\!\left(L^{jk}\right) T_{cd} \bar\varphi^{i} \gamma^{a} \gamma^{b} \gamma^{cd} \psi_{bj}\\
&- \frac{3 i N}{L^{4}} E_{a} L_{i}{}^{j} T_{cd} \bar\varphi^{i} \gamma^{a} \gamma^{b} \gamma^{cd} \psi_{bj}\\
&+\frac{3 i N g}{2 L^{2}} L^{ij} \mathcal D_{a}\!\left(\bar\varphi_{i}\right) \gamma^{a} \gamma^{b} \psi_{bj}\\
&- 6 N g \bar\chi^{i} \gamma^{a} \psi_{ai}\\
&- \frac{3 N g}{L^{2}} L_{i}{}^{j} T_{ab} \bar\varphi^{i} \gamma^{ab} \gamma^{c} \psi_{cj}\\
&+\frac{3 N^{2} g}{4 L^{2}} \bar\varphi^{i} \gamma^{a} \psi_{ai}
\end{aligned}
\tag{SCG10.2}
```

```math
\begin{aligned}
&+\frac{3 i N g}{2 L^{4}} L_{ik} L^{j}{}_{l} \mathcal D_{a}\!\left(L^{lk}\right) \bar\varphi^{i} \gamma^{a} \gamma^{b} \psi_{bj}\\
&+\frac{3 i N g}{4 L^{2}} E_{a} \bar\varphi^{i} \gamma^{a} \gamma^{b} \psi_{bi}\\
&+\frac{3 i N}{L^{2}} \mathcal D_{a}\!\left(\bar\varphi_{i}\right) \gamma^{a} \gamma^{b} \phi_{b}{}^{i}\\
&+\frac{24 N}{L^{2}} L_{i}{}^{j} \bar\chi^{i} \gamma^{a} \phi_{aj}\\
&- \frac{6 N}{L^{2}} T_{ab} \bar\varphi^{i} \gamma^{ab} \gamma^{c} \phi_{ci}\\
&- \frac{3 N^{2}}{L^{4}} L_{i}{}^{j} \bar\varphi^{i} \gamma^{a} \phi_{aj}\\
&+\frac{3 i N}{L^{4}} L_{ik} \mathcal D_{a}\!\left(L^{jk}\right) \bar\varphi^{i} \gamma^{a} \gamma^{b} \phi_{bj}\\
&- \frac{3 i N}{L^{4}} E_{a} L_{i}{}^{j} \bar\varphi^{i} \gamma^{a} \gamma^{b} \phi_{bj}
\end{aligned}
\tag{SCG10.3}
```

**Source group 11.**

```math
\left.e^{-1}\mathcal L_{R^2}\right|_{\text{source group }11}=-\frac12A'_a(\mathcal D_b\rho')\widehat G^{ab}
\tag{SCI11}
```

Substitute (SC1)–(SC8), retain the permitted degree and collect:

```math
\begin{aligned}
\left.e^{-1}\mathcal L_{R^2}\right|_{\text{group }11}={}&- \frac{2}{L} E_{a} \widehat G^{a}{}_{b} \mathcal D^{b}\!\left(\frac{N}{L}\right)\\
&+\frac{i}{L} E_{b} \widehat G^{ab} \mathcal D_{a}\!\left(\frac{1}{L^{3}} L_{ij} \bar\varphi^{i} \varphi^{j}\right)\\
&- \sqrt{2} \widehat G_{ab} \mathcal D^{b}\!\left(\frac{N}{L}\right) V^{a}\\
&+\frac{\sqrt{2} i}{2} \widehat G^{a}{}_{b} V^{b} \mathcal D_{a}\!\left(\frac{1}{L^{3}} L_{ij} \bar\varphi^{i} \varphi^{j}\right)\\
&- \frac{1}{L^{3}} \widehat G_{ab} L_{i}{}^{j} \mathcal D^{b}\!\left(\frac{N}{L}\right) \bar\varphi^{i} \gamma^{a} \varphi_{j}\\
&+\frac{i}{L} \widehat G^{a}{}_{b} \mathcal D^{b}\!\left(\frac{N}{L}\right) \bar\varphi^{i} \psi_{ai}
\end{aligned}
\tag{SCG11.1}
```

**Source group 12.**

```math
\left.e^{-1}\mathcal L_{R^2}\right|_{\text{source group }12}=-\frac12A'_a\rho'\mathcal D_b\widehat G^{ab}
\tag{SCI12}
```

Substitute (SC1)–(SC8), retain the permitted degree and collect:

```math
\begin{aligned}
\left.e^{-1}\mathcal L_{R^2}\right|_{\text{group }12}={}&- \frac{2 N}{L^{2}} E_{a} \mathcal D_{b}\!\left(\widehat G^{ab}\right)\\
&+\frac{i}{L^{4}} E_{a} L_{i}{}^{j} \mathcal D_{b}\!\left(\widehat G^{ab}\right) \bar\varphi^{i} \varphi_{j}\\
&- \frac{\sqrt{2} N}{L} \mathcal D_{a}\!\left(\widehat G_{b}{}^{a}\right) V^{b}\\
&+\frac{\sqrt{2} i}{2 L^{3}} L_{i}{}^{j} \mathcal D_{a}\!\left(\widehat G_{b}{}^{a}\right) V^{b} \bar\varphi^{i} \varphi_{j}\\
&- \frac{N}{L^{4}} L_{i}{}^{j} \mathcal D_{b}\!\left(\widehat G_{a}{}^{b}\right) \bar\varphi^{i} \gamma^{a} \varphi_{j}\\
&+\frac{i N}{L^{2}} \mathcal D_{b}\!\left(\widehat G^{ab}\right) \bar\varphi^{i} \psi_{ai}
\end{aligned}
\tag{SCG12.1}
```

**Source group 13.**

```math
\left.e^{-1}\mathcal L_{R^2}\right|_{\text{source group }13}=-\frac12A'_a\mathcal D_b\widehat F'^{ab}
\tag{SCI13}
```

Substitute (SC1)–(SC8), retain the permitted degree and collect:

```math
\begin{aligned}
\left.e^{-1}\mathcal L_{R^2}\right|_{\text{group }13}={}&- \frac{2}{L} E_{a} \mathcal D_{b}\!\left(\mathcal D^{a}\!\left(\frac{1}{L} E^{b}\right)\right)\\
&+\frac{2}{L} E_{a} \mathcal D_{b}\!\left(\mathcal D^{b}\!\left(\frac{1}{L} E^{a}\right)\right)\\
&- \frac{2}{L} E_{a} \mathcal D_{b}\!\left(\frac{1}{L} \widehat R(V)^{abij} L_{ij}\right)\\
&+\frac{1}{L} E_{a} \mathcal D_{b}\!\left(\frac{1}{L^{3}} L_{i}{}^{j} \mathcal D^{a}\!\left(L^{ik}\right) \mathcal D^{b}\!\left(L_{jk}\right)\right)\\
&- \frac{1}{L} E_{a} \mathcal D_{b}\!\left(\frac{1}{L^{3}} L_{i}{}^{j} \mathcal D^{b}\!\left(L^{ik}\right) \mathcal D^{a}\!\left(L_{jk}\right)\right)\\
&+\frac{1}{L} E^{b} \mathcal D_{a}\!\left(\mathcal D_{b}\!\left(\frac{1}{L^{3}} L_{ij} \bar\varphi^{i} \gamma^{a} \varphi^{j}\right)\right)\\
&- \frac{1}{L} E^{b} \mathcal D_{a}\!\left(\mathcal D^{a}\!\left(\frac{1}{L^{3}} L_{ij} \bar\varphi^{i} \gamma_{b} \varphi^{j}\right)\right)\\
&+\frac{i}{L} E^{b} \mathcal D_{a}\!\left(\frac{1}{L} \bar\varphi^{i} \widehat R(Q)_{b}{}^{a}{}_{i}\right)
\end{aligned}
\tag{SCG13.1}
```

```math
\begin{aligned}
&- \sqrt{2} \mathcal D_{a}\!\left(\mathcal D_{b}\!\left(\frac{1}{L} E^{a}\right)\right) V^{b}\\
&+\sqrt{2} \mathcal D_{a}\!\left(\mathcal D^{a}\!\left(\frac{1}{L} E_{b}\right)\right) V^{b}\\
&- \sqrt{2} \mathcal D_{a}\!\left(\frac{1}{L} \widehat R(V)_{b}{}^{aij} L_{ij}\right) V^{b}\\
&+\frac{\sqrt{2}}{2} \mathcal D_{a}\!\left(\frac{1}{L^{3}} L_{i}{}^{j} \mathcal D_{b}\!\left(L^{ik}\right) \mathcal D^{a}\!\left(L_{jk}\right)\right) V^{b}\\
&- \frac{\sqrt{2}}{2} \mathcal D_{a}\!\left(\frac{1}{L^{3}} L_{i}{}^{j} \mathcal D^{a}\!\left(L^{ik}\right) \mathcal D_{b}\!\left(L_{jk}\right)\right) V^{b}\\
&+\frac{\sqrt{2}}{2} V^{b} \mathcal D_{a}\!\left(\mathcal D_{b}\!\left(\frac{1}{L^{3}} L_{ij} \bar\varphi^{i} \gamma^{a} \varphi^{j}\right)\right)\\
&- \frac{\sqrt{2}}{2} V^{b} \mathcal D_{a}\!\left(\mathcal D^{a}\!\left(\frac{1}{L^{3}} L_{ij} \bar\varphi^{i} \gamma_{b} \varphi^{j}\right)\right)\\
&+\frac{\sqrt{2} i}{2} V^{b} \mathcal D_{a}\!\left(\frac{1}{L} \bar\varphi^{i} \widehat R(Q)_{b}{}^{a}{}_{i}\right)
\end{aligned}
\tag{SCG13.2}
```

```math
\begin{aligned}
&- \frac{1}{L^{3}} L_{i}{}^{j} \mathcal D_{b}\!\left(\mathcal D_{a}\!\left(\frac{1}{L} E^{b}\right)\right) \bar\varphi^{i} \gamma^{a} \varphi_{j}\\
&+\frac{1}{L^{3}} L_{i}{}^{j} \mathcal D_{b}\!\left(\mathcal D^{b}\!\left(\frac{1}{L} E_{a}\right)\right) \bar\varphi^{i} \gamma^{a} \varphi_{j}\\
&- \frac{1}{L^{3}} L_{i}{}^{j} \mathcal D_{b}\!\left(\frac{1}{L} \widehat R(V)_{a}{}^{bkl} L_{kl}\right) \bar\varphi^{i} \gamma^{a} \varphi_{j}\\
&+\frac{1}{2 L^{3}} L_{i}{}^{j} \mathcal D_{b}\!\left(\frac{1}{L^{3}} L_{k}{}^{l} \mathcal D_{a}\!\left(L^{km}\right) \mathcal D^{b}\!\left(L_{lm}\right)\right) \bar\varphi^{i} \gamma^{a} \varphi_{j}\\
&- \frac{1}{2 L^{3}} L_{i}{}^{j} \mathcal D_{b}\!\left(\frac{1}{L^{3}} L_{k}{}^{l} \mathcal D^{b}\!\left(L^{km}\right) \mathcal D_{a}\!\left(L_{lm}\right)\right) \bar\varphi^{i} \gamma^{a} \varphi_{j}\\
&+\frac{i}{L} \mathcal D_{b}\!\left(\mathcal D^{a}\!\left(\frac{1}{L} E^{b}\right)\right) \bar\varphi^{i} \psi_{ai}\\
&- \frac{i}{L} \mathcal D_{b}\!\left(\mathcal D^{b}\!\left(\frac{1}{L} E^{a}\right)\right) \bar\varphi^{i} \psi_{ai}\\
&+\frac{i}{L} \mathcal D_{b}\!\left(\frac{1}{L} \widehat R(V)^{abjk} L_{jk}\right) \bar\varphi^{i} \psi_{ai}
\end{aligned}
\tag{SCG13.3}
```

```math
\begin{aligned}
&- \frac{i}{2 L} \mathcal D_{b}\!\left(\frac{1}{L^{3}} L_{j}{}^{k} \mathcal D^{a}\!\left(L^{jl}\right) \mathcal D^{b}\!\left(L_{kl}\right)\right) \bar\varphi^{i} \psi_{ai}\\
&+\frac{i}{2 L} \mathcal D_{b}\!\left(\frac{1}{L^{3}} L_{j}{}^{k} \mathcal D^{b}\!\left(L^{jl}\right) \mathcal D^{a}\!\left(L_{kl}\right)\right) \bar\varphi^{i} \psi_{ai}
\end{aligned}
\tag{SCG13.4}
```

**Source group 14.**

```math
\left.e^{-1}\mathcal L_{R^2}\right|_{\text{source group }14}=+8A'_a(\mathcal D_b\rho')T^{ab}
\tag{SCI14}
```

Substitute (SC1)–(SC8), retain the permitted degree and collect:

```math
\begin{aligned}
\left.e^{-1}\mathcal L_{R^2}\right|_{\text{group }14}={}&\frac{32}{L} E_{a} \mathcal D_{b}\!\left(\frac{N}{L}\right) T^{ab}\\
&+\frac{16 i}{L} E_{b} T^{ba} \mathcal D_{a}\!\left(\frac{1}{L^{3}} L_{ij} \bar\varphi^{i} \varphi^{j}\right)\\
&+16 \sqrt{2} \mathcal D_{a}\!\left(\frac{N}{L}\right) T_{b}{}^{a} V^{b}\\
&+8 \sqrt{2} i T_{b}{}^{a} V^{b} \mathcal D_{a}\!\left(\frac{1}{L^{3}} L_{ij} \bar\varphi^{i} \varphi^{j}\right)\\
&+\frac{16}{L^{3}} L_{i}{}^{j} \mathcal D_{b}\!\left(\frac{N}{L}\right) T_{a}{}^{b} \bar\varphi^{i} \gamma^{a} \varphi_{j}\\
&- \frac{16 i}{L} \mathcal D_{b}\!\left(\frac{N}{L}\right) T^{ab} \bar\varphi^{i} \psi_{ai}
\end{aligned}
\tag{SCG14.1}
```

**Source group 15.**

```math
\left.e^{-1}\mathcal L_{R^2}\right|_{\text{source group }15}=+8A'_a\rho'\mathcal D_bT^{ab}
\tag{SCI15}
```

Substitute (SC1)–(SC8), retain the permitted degree and collect:

```math
\begin{aligned}
\left.e^{-1}\mathcal L_{R^2}\right|_{\text{group }15}={}&\frac{32 N}{L^{2}} E_{a} \mathcal D_{b}\!\left(T^{ab}\right)\\
&- \frac{16 i}{L^{4}} E_{a} L_{i}{}^{j} \mathcal D_{b}\!\left(T^{ab}\right) \bar\varphi^{i} \varphi_{j}\\
&+\frac{16 \sqrt{2} N}{L} \mathcal D_{a}\!\left(T_{b}{}^{a}\right) V^{b}\\
&- \frac{8 \sqrt{2} i}{L^{3}} L_{i}{}^{j} \mathcal D_{a}\!\left(T_{b}{}^{a}\right) V^{b} \bar\varphi^{i} \varphi_{j}\\
&+\frac{16 N}{L^{4}} L_{i}{}^{j} \mathcal D_{b}\!\left(T_{a}{}^{b}\right) \bar\varphi^{i} \gamma^{a} \varphi_{j}\\
&- \frac{16 i N}{L^{2}} \mathcal D_{b}\!\left(T^{ab}\right) \bar\varphi^{i} \psi_{ai}
\end{aligned}
\tag{SCG15.1}
```

**Source group 16.**

```math
\left.e^{-1}\mathcal L_{R^2}\right|_{\text{source group }16}=-\frac18A'_a\varepsilon^{abcde}\widehat F'_{bc}\widehat G_{de}
\tag{SCI16}
```

Substitute (SC1)–(SC8), retain the permitted degree and collect:

```math
\begin{aligned}
\left.e^{-1}\mathcal L_{R^2}\right|_{\text{group }16}={}&- \frac{1}{L} E_{a} \widehat G_{bc} \mathcal D_{d}\!\left(\frac{1}{L} E_{e}\right) \varepsilon^{abcde}\\
&- \frac{1}{2 L^{2}} E_{a} \widehat G_{bc} L_{ij} \widehat R(V)_{de}{}^{ij} \varepsilon^{abcde}\\
&+\frac{1}{2 L^{4}} E_{a} \widehat G_{bc} L_{ij} \mathcal D_{d}\!\left(L^{j}{}_{k}\right) \mathcal D_{e}\!\left(L^{ik}\right) \varepsilon^{abcde}\\
&+\frac{1}{2 L} E_{c} \widehat G_{de} \varepsilon^{abcde} \mathcal D_{a}\!\left(\frac{1}{L^{3}} L_{ij} \bar\varphi^{i} \gamma_{b} \varphi^{j}\right)\\
&+\frac{i}{4 L^{2}} E_{c} \widehat G_{de} \varepsilon^{abcde} \bar\varphi^{i} \widehat R(Q)_{abi}\\
&- \frac{\sqrt{2}}{2} \widehat G_{ab} \mathcal D_{c}\!\left(\frac{1}{L} E_{d}\right) V_{e} \varepsilon^{abcde}\\
&- \frac{\sqrt{2}}{4 L} \widehat G_{ab} L_{ij} \widehat R(V)_{cd}{}^{ij} V_{e} \varepsilon^{abcde}\\
&+\frac{\sqrt{2}}{4 L^{3}} \widehat G_{ab} L_{ij} \mathcal D_{c}\!\left(L^{j}{}_{k}\right) \mathcal D_{d}\!\left(L^{ik}\right) V_{e} \varepsilon^{abcde}
\end{aligned}
\tag{SCG16.1}
```

```math
\begin{aligned}
&+\frac{\sqrt{2}}{4} \widehat G_{cd} V_{e} \varepsilon^{abcde} \mathcal D_{a}\!\left(\frac{1}{L^{3}} L_{ij} \bar\varphi^{i} \gamma_{b} \varphi^{j}\right)\\
&+\frac{\sqrt{2} i}{8 L} \widehat G_{cd} V_{e} \varepsilon^{abcde} \bar\varphi^{i} \widehat R(Q)_{abi}\\
&- \frac{1}{2 L^{3}} \widehat G_{bc} L_{i}{}^{j} \mathcal D_{d}\!\left(\frac{1}{L} E_{e}\right) \varepsilon_{a}{}^{bcde} \bar\varphi^{i} \gamma^{a} \varphi_{j}\\
&- \frac{1}{4 L^{4}} \widehat G_{bc} L_{i}{}^{j} L_{kl} \widehat R(V)_{de}{}^{kl} \varepsilon_{a}{}^{bcde} \bar\varphi^{i} \gamma^{a} \varphi_{j}\\
&+\frac{1}{4 L^{6}} \widehat G_{bc} L_{i}{}^{j} L_{kl} \mathcal D_{d}\!\left(L^{l}{}_{m}\right) \mathcal D_{e}\!\left(L^{km}\right) \varepsilon_{a}{}^{bcde} \bar\varphi^{i} \gamma^{a} \varphi_{j}\\
&+\frac{i}{2 L} \widehat G_{bc} \mathcal D_{d}\!\left(\frac{1}{L} E_{e}\right) \varepsilon^{abcde} \bar\varphi^{i} \psi_{ai}\\
&+\frac{i}{4 L^{2}} \widehat G_{bc} L_{jk} \widehat R(V)_{de}{}^{jk} \varepsilon^{abcde} \bar\varphi^{i} \psi_{ai}\\
&- \frac{i}{4 L^{4}} \widehat G_{bc} L_{jk} \mathcal D_{d}\!\left(L^{k}{}_{l}\right) \mathcal D_{e}\!\left(L^{jl}\right) \varepsilon^{abcde} \bar\varphi^{i} \psi_{ai}
\end{aligned}
\tag{SCG16.2}
```

**Source group 17.**

```math
\left.e^{-1}\mathcal L_{R^2}\right|_{\text{source group }17}=-\frac i4A'_a\bar\lambda'{}^i\gamma^{ab} [\frac14\gamma\!\cdot\!\widehat G\psi_{bi} -\gamma\!\cdot\!T\psi_{bi}+\frac g2L_{ij}\psi_b{}^j-\phi_{bi}]
\tag{SCI17}
```

Substitute (SC1)–(SC8), retain the permitted degree and collect:

```math
\begin{aligned}
\left.e^{-1}\mathcal L_{R^2}\right|_{\text{group }17}={}&\frac{1}{4 L^{2}} E_{b} \widehat G_{de} \mathcal D_{a}\!\left(\bar\varphi_{i}\right) \gamma^{a} \gamma^{bc} \gamma^{de} \psi_{c}{}^{i}\\
&- \frac{2 i}{L^{2}} E_{a} \widehat G_{cd} L_{i}{}^{j} \bar\chi^{i} \gamma^{ab} \gamma^{cd} \psi_{bj}\\
&+\frac{i}{2 L^{2}} E_{c} \widehat G_{ef} T_{ab} \bar\varphi^{i} \gamma^{ab} \gamma^{cd} \gamma^{ef} \psi_{di}\\
&+\frac{i N}{4 L^{4}} E_{a} \widehat G_{cd} L_{i}{}^{j} \bar\varphi^{i} \gamma^{ab} \gamma^{cd} \psi_{bj}\\
&+\frac{1}{4 L^{4}} E_{b} \widehat G_{de} L_{ik} \mathcal D_{a}\!\left(L^{jk}\right) \bar\varphi^{i} \gamma^{a} \gamma^{bc} \gamma^{de} \psi_{cj}\\
&- \frac{1}{4 L^{4}} E_{a} E_{b} \widehat G_{de} L_{i}{}^{j} \bar\varphi^{i} \gamma^{a} \gamma^{bc} \gamma^{de} \psi_{cj}\\
&+\frac{\sqrt{2}}{8 L} \widehat G_{de} V_{b} \mathcal D_{a}\!\left(\bar\varphi_{i}\right) \gamma^{a} \gamma^{bc} \gamma^{de} \psi_{c}{}^{i}\\
&- \frac{\sqrt{2} i}{L} \widehat G_{cd} L_{i}{}^{j} V_{a} \bar\chi^{i} \gamma^{ab} \gamma^{cd} \psi_{bj}
\end{aligned}
\tag{SCG17.1}
```

```math
\begin{aligned}
&+\frac{\sqrt{2} i}{4 L} \widehat G_{ef} T_{ab} V_{c} \bar\varphi^{i} \gamma^{ab} \gamma^{cd} \gamma^{ef} \psi_{di}\\
&+\frac{\sqrt{2} i N}{8 L^{3}} \widehat G_{cd} L_{i}{}^{j} V_{a} \bar\varphi^{i} \gamma^{ab} \gamma^{cd} \psi_{bj}\\
&+\frac{\sqrt{2}}{8 L^{3}} \widehat G_{de} L_{ik} \mathcal D_{a}\!\left(L^{jk}\right) V_{b} \bar\varphi^{i} \gamma^{a} \gamma^{bc} \gamma^{de} \psi_{cj}\\
&- \frac{\sqrt{2}}{8 L^{3}} E_{a} \widehat G_{de} L_{i}{}^{j} V_{b} \bar\varphi^{i} \gamma^{a} \gamma^{bc} \gamma^{de} \psi_{cj}\\
&- \frac{1}{L^{2}} E_{b} T_{de} \mathcal D_{a}\!\left(\bar\varphi_{i}\right) \gamma^{a} \gamma^{bc} \gamma^{de} \psi_{c}{}^{i}\\
&+\frac{8 i}{L^{2}} E_{a} L_{i}{}^{j} T_{cd} \bar\chi^{i} \gamma^{ab} \gamma^{cd} \psi_{bj}\\
&- \frac{2 i}{L^{2}} E_{c} T_{ab} T_{ef} \bar\varphi^{i} \gamma^{ab} \gamma^{cd} \gamma^{ef} \psi_{di}\\
&- \frac{i N}{L^{4}} E_{a} L_{i}{}^{j} T_{cd} \bar\varphi^{i} \gamma^{ab} \gamma^{cd} \psi_{bj}
\end{aligned}
\tag{SCG17.2}
```

```math
\begin{aligned}
&- \frac{1}{L^{4}} E_{b} L_{ik} \mathcal D_{a}\!\left(L^{jk}\right) T_{de} \bar\varphi^{i} \gamma^{a} \gamma^{bc} \gamma^{de} \psi_{cj}\\
&+\frac{1}{L^{4}} E_{a} E_{b} L_{i}{}^{j} T_{de} \bar\varphi^{i} \gamma^{a} \gamma^{bc} \gamma^{de} \psi_{cj}\\
&- \frac{\sqrt{2}}{2 L} T_{de} V_{b} \mathcal D_{a}\!\left(\bar\varphi_{i}\right) \gamma^{a} \gamma^{bc} \gamma^{de} \psi_{c}{}^{i}\\
&+\frac{4 \sqrt{2} i}{L} L_{i}{}^{j} T_{cd} V_{a} \bar\chi^{i} \gamma^{ab} \gamma^{cd} \psi_{bj}\\
&- \frac{\sqrt{2} i}{L} T_{ab} T_{ef} V_{c} \bar\varphi^{i} \gamma^{ab} \gamma^{cd} \gamma^{ef} \psi_{di}\\
&- \frac{\sqrt{2} i N}{2 L^{3}} L_{i}{}^{j} T_{cd} V_{a} \bar\varphi^{i} \gamma^{ab} \gamma^{cd} \psi_{bj}\\
&- \frac{\sqrt{2}}{2 L^{3}} L_{ik} \mathcal D_{a}\!\left(L^{jk}\right) T_{de} V_{b} \bar\varphi^{i} \gamma^{a} \gamma^{bc} \gamma^{de} \psi_{cj}\\
&+\frac{\sqrt{2}}{2 L^{3}} E_{a} L_{i}{}^{j} T_{de} V_{b} \bar\varphi^{i} \gamma^{a} \gamma^{bc} \gamma^{de} \psi_{cj}
\end{aligned}
\tag{SCG17.3}
```

```math
\begin{aligned}
&- \frac{g}{2 L^{2}} E_{b} L^{ij} \mathcal D_{a}\!\left(\bar\varphi_{i}\right) \gamma^{a} \gamma^{bc} \psi_{cj}\\
&- 2 i g E_{a} \bar\chi^{i} \gamma^{ab} \psi_{bi}\\
&- \frac{i g}{L^{2}} E_{c} L_{i}{}^{j} T_{ab} \bar\varphi^{i} \gamma^{ab} \gamma^{cd} \psi_{dj}\\
&+\frac{i N g}{4 L^{2}} E_{a} \bar\varphi^{i} \gamma^{ab} \psi_{bi}\\
&- \frac{g}{2 L^{4}} E_{b} L_{ik} L^{j}{}_{l} \mathcal D_{a}\!\left(L^{lk}\right) \bar\varphi^{i} \gamma^{a} \gamma^{bc} \psi_{cj}\\
&- \frac{g}{4 L^{2}} E_{a} E_{b} \bar\varphi^{i} \gamma^{a} \gamma^{bc} \psi_{ci}\\
&- \frac{\sqrt{2} g}{4 L} L^{ij} V_{b} \mathcal D_{a}\!\left(\bar\varphi_{i}\right) \gamma^{a} \gamma^{bc} \psi_{cj}\\
&- \sqrt{2} i L g V_{a} \bar\chi^{i} \gamma^{ab} \psi_{bi}
\end{aligned}
\tag{SCG17.4}
```

```math
\begin{aligned}
&- \frac{\sqrt{2} i g}{2 L} L_{i}{}^{j} T_{ab} V_{c} \bar\varphi^{i} \gamma^{ab} \gamma^{cd} \psi_{dj}\\
&+\frac{\sqrt{2} i N g}{8 L} V_{a} \bar\varphi^{i} \gamma^{ab} \psi_{bi}\\
&- \frac{\sqrt{2} g}{4 L^{3}} L_{ik} L^{j}{}_{l} \mathcal D_{a}\!\left(L^{lk}\right) V_{b} \bar\varphi^{i} \gamma^{a} \gamma^{bc} \psi_{cj}\\
&- \frac{\sqrt{2} g}{8 L} E_{a} V_{b} \bar\varphi^{i} \gamma^{a} \gamma^{bc} \psi_{ci}\\
&- \frac{1}{L^{2}} E_{b} \mathcal D_{a}\!\left(\bar\varphi_{i}\right) \gamma^{a} \gamma^{bc} \phi_{c}{}^{i}\\
&+\frac{8 i}{L^{2}} E_{a} L_{i}{}^{j} \bar\chi^{i} \gamma^{ab} \phi_{bj}\\
&- \frac{2 i}{L^{2}} E_{c} T_{ab} \bar\varphi^{i} \gamma^{ab} \gamma^{cd} \phi_{di}\\
&- \frac{i N}{L^{4}} E_{a} L_{i}{}^{j} \bar\varphi^{i} \gamma^{ab} \phi_{bj}
\end{aligned}
\tag{SCG17.5}
```

```math
\begin{aligned}
&- \frac{1}{L^{4}} E_{b} L_{ik} \mathcal D_{a}\!\left(L^{jk}\right) \bar\varphi^{i} \gamma^{a} \gamma^{bc} \phi_{cj}\\
&+\frac{1}{L^{4}} E_{a} E_{b} L_{i}{}^{j} \bar\varphi^{i} \gamma^{a} \gamma^{bc} \phi_{cj}\\
&- \frac{\sqrt{2}}{2 L} V_{b} \mathcal D_{a}\!\left(\bar\varphi_{i}\right) \gamma^{a} \gamma^{bc} \phi_{c}{}^{i}\\
&+\frac{4 \sqrt{2} i}{L} L_{i}{}^{j} V_{a} \bar\chi^{i} \gamma^{ab} \phi_{bj}\\
&- \frac{\sqrt{2} i}{L} T_{ab} V_{c} \bar\varphi^{i} \gamma^{ab} \gamma^{cd} \phi_{di}\\
&- \frac{\sqrt{2} i N}{2 L^{3}} L_{i}{}^{j} V_{a} \bar\varphi^{i} \gamma^{ab} \phi_{bj}\\
&- \frac{\sqrt{2}}{2 L^{3}} L_{ik} \mathcal D_{a}\!\left(L^{jk}\right) V_{b} \bar\varphi^{i} \gamma^{a} \gamma^{bc} \phi_{cj}\\
&+\frac{\sqrt{2}}{2 L^{3}} E_{a} L_{i}{}^{j} V_{b} \bar\varphi^{i} \gamma^{a} \gamma^{bc} \phi_{cj}
\end{aligned}
\tag{SCG17.6}
```

**Source group 18.**

```math
\left.e^{-1}\mathcal L_{R^2}\right|_{\text{source group }18}=-\frac14A'_a\rho'\bar\psi_b{}^i\gamma^{ba}\gamma^c [\frac14\gamma\!\cdot\!\widehat G\psi_{ci} -\gamma\!\cdot\!T\psi_{ci}+\frac g2L_{ij}\psi_c{}^j-\phi_{ci}]
\tag{SCI18}
```

Substitute (SC1)–(SC8), retain the permitted degree and collect:

```math
\begin{aligned}
\left.e^{-1}\mathcal L_{R^2}\right|_{\text{group }18}={}&- \frac{N}{4 L^{2}} E_{b} \widehat G_{de} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{c} \gamma^{de} \psi_{ci}\\
&- \frac{\sqrt{2} N}{8 L} \widehat G_{de} V_{b} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{c} \gamma^{de} \psi_{ci}\\
&+\frac{N}{L^{2}} E_{b} T_{de} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{c} \gamma^{de} \psi_{ci}\\
&+\frac{\sqrt{2} N}{2 L} T_{de} V_{b} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{c} \gamma^{de} \psi_{ci}\\
&+\frac{N g}{2 L^{2}} E_{b} L_{i}{}^{j} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{c} \psi_{cj}\\
&+\frac{\sqrt{2} N g}{4 L} L_{i}{}^{j} V_{b} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{c} \psi_{cj}\\
&+\frac{N}{L^{2}} E_{b} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{c} \phi_{ci}\\
&+\frac{\sqrt{2} N}{2 L} V_{b} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{c} \phi_{ci}
\end{aligned}
\tag{SCG18.1}
```

**Source group 19.**

```math
\left.e^{-1}\mathcal L_{R^2}\right|_{\text{source group }19}=-\frac14A'_a\bar\psi_b{}^i\gamma^{ba}\not{\mathcal D}\lambda'_i
\tag{SCI19}
```

Substitute (SC1)–(SC8), retain the permitted degree and collect:

```math
\begin{aligned}
\left.e^{-1}\mathcal L_{R^2}\right|_{\text{group }19}={}&\frac{i}{L} E_{b} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{c} \mathcal D_{c}\!\left(\frac{1}{L} \gamma^{d} \mathcal D_{d}\!\left(\varphi_{i}\right)\right)\\
&- \frac{8}{L} E_{b} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{c} \mathcal D_{c}\!\left(\frac{1}{L} L_{ij} \chi^{j}\right)\\
&- \frac{2}{L} E_{b} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{c} \mathcal D_{c}\!\left(\frac{1}{L} \gamma^{de} T_{de} \varphi_{i}\right)\\
&+\frac{1}{L} E_{b} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{c} \mathcal D_{c}\!\left(\frac{N}{L^{3}} L_{ij} \varphi^{j}\right)\\
&- \frac{i}{L} E_{b} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{c} \mathcal D_{c}\!\left(\frac{1}{L^{3}} \gamma^{d} \mathcal D_{d}\!\left(L_{ij}\right) L^{jk} \varphi_{k}\right)\\
&+\frac{i}{L} E_{b} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{c} \mathcal D_{c}\!\left(\frac{1}{L^{3}} \gamma^{d} E_{d} L_{ij} \varphi^{j}\right)\\
&+\frac{\sqrt{2} i}{2} V_{b} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{c} \mathcal D_{c}\!\left(\frac{1}{L} \gamma^{d} \mathcal D_{d}\!\left(\varphi_{i}\right)\right)\\
&- 4 \sqrt{2} V_{b} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{c} \mathcal D_{c}\!\left(\frac{1}{L} L_{ij} \chi^{j}\right)
\end{aligned}
\tag{SCG19.1}
```

```math
\begin{aligned}
&- \sqrt{2} V_{b} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{c} \mathcal D_{c}\!\left(\frac{1}{L} \gamma^{de} T_{de} \varphi_{i}\right)\\
&+\frac{\sqrt{2}}{2} V_{b} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{c} \mathcal D_{c}\!\left(\frac{N}{L^{3}} L_{ij} \varphi^{j}\right)\\
&- \frac{\sqrt{2} i}{2} V_{b} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{c} \mathcal D_{c}\!\left(\frac{1}{L^{3}} \gamma^{d} \mathcal D_{d}\!\left(L_{ij}\right) L^{jk} \varphi_{k}\right)\\
&+\frac{\sqrt{2} i}{2} V_{b} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{c} \mathcal D_{c}\!\left(\frac{1}{L^{3}} \gamma^{d} E_{d} L_{ij} \varphi^{j}\right)
\end{aligned}
\tag{SCG19.2}
```

**Source group 20.**

```math
\left.e^{-1}\mathcal L_{R^2}\right|_{\text{source group }20}=+\frac i2A'_a\bar\psi_b{}^i\gamma^{ba}\gamma\!\cdot\!T\lambda'_i
\tag{SCI20}
```

Substitute (SC1)–(SC8), retain the permitted degree and collect:

```math
\begin{aligned}
\left.e^{-1}\mathcal L_{R^2}\right|_{\text{group }20}={}&\frac{2}{L^{2}} E_{b} T_{cd} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{cd} \gamma^{e} \mathcal D_{e}\!\left(\varphi_{i}\right)\\
&- \frac{16 i}{L^{2}} E_{b} L_{i}{}^{j} T_{cd} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{cd} \chi_{j}\\
&+\frac{4 i}{L^{2}} E_{b} T_{cd} T_{ef} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{cd} \gamma^{ef} \varphi_{i}\\
&+\frac{2 i N}{L^{4}} E_{b} L_{i}{}^{j} T_{cd} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{cd} \varphi_{j}\\
&+\frac{2}{L^{4}} E_{b} L^{j}{}_{k} \mathcal D_{e}\!\left(L_{i}{}^{k}\right) T_{cd} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{cd} \gamma^{e} \varphi_{j}\\
&- \frac{2}{L^{4}} E_{b} E_{e} L_{i}{}^{j} T_{cd} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{cd} \gamma^{e} \varphi_{j}\\
&+\frac{\sqrt{2}}{L} T_{cd} V_{b} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{cd} \gamma^{e} \mathcal D_{e}\!\left(\varphi_{i}\right)\\
&- \frac{8 \sqrt{2} i}{L} L_{i}{}^{j} T_{cd} V_{b} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{cd} \chi_{j}
\end{aligned}
\tag{SCG20.1}
```

```math
\begin{aligned}
&+\frac{2 \sqrt{2} i}{L} T_{cd} T_{ef} V_{b} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{cd} \gamma^{ef} \varphi_{i}\\
&+\frac{\sqrt{2} i N}{L^{3}} L_{i}{}^{j} T_{cd} V_{b} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{cd} \varphi_{j}\\
&+\frac{\sqrt{2}}{L^{3}} L^{j}{}_{k} \mathcal D_{e}\!\left(L_{i}{}^{k}\right) T_{cd} V_{b} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{cd} \gamma^{e} \varphi_{j}\\
&- \frac{\sqrt{2}}{L^{3}} E_{e} L_{i}{}^{j} T_{cd} V_{b} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{cd} \gamma^{e} \varphi_{j}
\end{aligned}
\tag{SCG20.2}
```

**Source group 21.**

```math
\left.e^{-1}\mathcal L_{R^2}\right|_{\text{source group }21}=-4iA'_a\rho'\bar\psi_b{}^i\gamma^{ba}\chi_i
\tag{SCI21}
```

Substitute (SC1)–(SC8), retain the permitted degree and collect:

```math
\begin{aligned}
\left.e^{-1}\mathcal L_{R^2}\right|_{\text{group }21}={}&- \frac{16 i N}{L^{2}} E_{b} \bar\psi_{a}{}^{i} \gamma^{ab} \chi_{i}\\
&- \frac{8 \sqrt{2} i N}{L} V_{b} \bar\psi_{a}{}^{i} \gamma^{ab} \chi_{i}
\end{aligned}
\tag{SCG21.1}
```

**Source group 22.**

```math
\left.e^{-1}\mathcal L_{R^2}\right|_{\text{source group }22}=-\frac i{16}A'_a\bar\psi_b{}^i\gamma^{ba}\gamma\!\cdot\!\widehat G\lambda'_i
\tag{SCI22}
```

Substitute (SC1)–(SC8), retain the permitted degree and collect:

```math
\begin{aligned}
\left.e^{-1}\mathcal L_{R^2}\right|_{\text{group }22}={}&- \frac{1}{4 L^{2}} E_{b} \widehat G_{cd} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{cd} \gamma^{e} \mathcal D_{e}\!\left(\varphi_{i}\right)\\
&+\frac{2 i}{L^{2}} E_{b} \widehat G_{cd} L_{i}{}^{j} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{cd} \chi_{j}\\
&- \frac{i}{2 L^{2}} E_{b} \widehat G_{cd} T_{ef} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{cd} \gamma^{ef} \varphi_{i}\\
&- \frac{i N}{4 L^{4}} E_{b} \widehat G_{cd} L_{i}{}^{j} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{cd} \varphi_{j}\\
&- \frac{1}{4 L^{4}} E_{b} \widehat G_{cd} L^{j}{}_{k} \mathcal D_{e}\!\left(L_{i}{}^{k}\right) \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{cd} \gamma^{e} \varphi_{j}\\
&+\frac{1}{4 L^{4}} E_{b} E_{e} \widehat G_{cd} L_{i}{}^{j} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{cd} \gamma^{e} \varphi_{j}\\
&- \frac{\sqrt{2}}{8 L} \widehat G_{cd} V_{b} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{cd} \gamma^{e} \mathcal D_{e}\!\left(\varphi_{i}\right)\\
&+\frac{\sqrt{2} i}{L} \widehat G_{cd} L_{i}{}^{j} V_{b} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{cd} \chi_{j}
\end{aligned}
\tag{SCG22.1}
```

```math
\begin{aligned}
&- \frac{\sqrt{2} i}{4 L} \widehat G_{cd} T_{ef} V_{b} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{cd} \gamma^{ef} \varphi_{i}\\
&- \frac{\sqrt{2} i N}{8 L^{3}} \widehat G_{cd} L_{i}{}^{j} V_{b} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{cd} \varphi_{j}\\
&- \frac{\sqrt{2}}{8 L^{3}} \widehat G_{cd} L^{j}{}_{k} \mathcal D_{e}\!\left(L_{i}{}^{k}\right) V_{b} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{cd} \gamma^{e} \varphi_{j}\\
&+\frac{\sqrt{2}}{8 L^{3}} E_{e} \widehat G_{cd} L_{i}{}^{j} V_{b} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{cd} \gamma^{e} \varphi_{j}
\end{aligned}
\tag{SCG22.2}
```

**Source group 23.**

```math
\left.e^{-1}\mathcal L_{R^2}\right|_{\text{source group }23}=+\frac{ig}8A'_a\bar\psi_b{}^i\gamma^{ba}L_{ij}\lambda'{}^j
\tag{SCI23}
```

Substitute (SC1)–(SC8), retain the permitted degree and collect:

```math
\begin{aligned}
\left.e^{-1}\mathcal L_{R^2}\right|_{\text{group }23}={}&- \frac{g}{2 L^{2}} E_{b} L_{i}{}^{j} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{c} \mathcal D_{c}\!\left(\varphi_{j}\right)\\
&- 2 i g E_{b} \bar\psi_{a}{}^{i} \gamma^{ab} \chi_{i}\\
&- \frac{i g}{L^{2}} E_{b} L_{i}{}^{j} T_{cd} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{cd} \varphi_{j}\\
&+\frac{i N g}{4 L^{2}} E_{b} \bar\psi_{a}{}^{i} \gamma^{ab} \varphi_{i}\\
&+\frac{g}{2 L^{4}} E_{b} L_{ik} L^{j}{}_{l} \mathcal D_{c}\!\left(L^{kl}\right) \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{c} \varphi_{j}\\
&- \frac{g}{4 L^{2}} E_{b} E_{c} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{c} \varphi_{i}\\
&- \frac{\sqrt{2} g}{4 L} L_{i}{}^{j} V_{b} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{c} \mathcal D_{c}\!\left(\varphi_{j}\right)\\
&- \sqrt{2} i L g V_{b} \bar\psi_{a}{}^{i} \gamma^{ab} \chi_{i}
\end{aligned}
\tag{SCG23.1}
```

```math
\begin{aligned}
&- \frac{\sqrt{2} i g}{2 L} L_{i}{}^{j} T_{cd} V_{b} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{cd} \varphi_{j}\\
&+\frac{\sqrt{2} i N g}{8 L} V_{b} \bar\psi_{a}{}^{i} \gamma^{ab} \varphi_{i}\\
&+\frac{\sqrt{2} g}{4 L^{3}} L_{ik} L^{j}{}_{l} \mathcal D_{c}\!\left(L^{kl}\right) V_{b} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{c} \varphi_{j}\\
&- \frac{\sqrt{2} g}{8 L} E_{c} V_{b} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{c} \varphi_{i}
\end{aligned}
\tag{SCG23.2}
```

**Source group 24.**

```math
\left.e^{-1}\mathcal L_{R^2}\right|_{\text{source group }24}=-\frac g8A'_a\rho'\bar\psi_b{}^i\gamma^{abc}\psi_c{}^jL_{ij}
\tag{SCI24}
```

Substitute (SC1)–(SC8), retain the permitted degree and collect:

```math
\begin{aligned}
\left.e^{-1}\mathcal L_{R^2}\right|_{\text{group }24}={}&- \frac{N g}{2 L^{2}} E_{b} L_{i}{}^{j} \bar\psi_{a}{}^{i} \gamma^{abc} \psi_{cj}\\
&- \frac{\sqrt{2} N g}{4 L} L_{i}{}^{j} V_{b} \bar\psi_{a}{}^{i} \gamma^{abc} \psi_{cj}
\end{aligned}
\tag{SCG24.1}
```

**Source group 25.**

```math
\left.e^{-1}\mathcal L_{R^2}\right|_{\text{source group }25}=+\frac14A'_a\bar\psi_b{}^i\gamma^{abc}\psi_c{}^jY'_{ij}
\tag{SCI25}
```

Substitute (SC1)–(SC8), retain the permitted degree and collect:

```math
\begin{aligned}
\left.e^{-1}\mathcal L_{R^2}\right|_{\text{group }25}={}&\frac{1}{2 L^{2}} E_{b} \Box_c\!\left(L_{i}{}^{j}\right) \bar\psi_{a}{}^{i} \gamma^{abc} \psi_{cj}\\
&- \frac{1}{2 L^{4}} E_{b} E_{d} E^{d} L_{i}{}^{j} \bar\psi_{a}{}^{i} \gamma^{abc} \psi_{cj}\\
&- \frac{N^{2}}{2 L^{4}} E_{b} L_{i}{}^{j} \bar\psi_{a}{}^{i} \gamma^{abc} \psi_{cj}\\
&+\frac{4}{3 L^{2}} E_{b} L_{i}{}^{j} T_{de} T^{de} \bar\psi_{a}{}^{i} \gamma^{abc} \psi_{cj}\\
&+\frac{2}{L^{2}} D E_{b} L_{i}{}^{j} \bar\psi_{a}{}^{i} \gamma^{abc} \psi_{cj}\\
&- \frac{1}{4 L^{4}} E_{b} L_{kl} \mathcal D_{d}\!\left(L^{k}{}_{i}\right) \mathcal D^{d}\!\left(L^{jl}\right) \bar\psi_{a}{}^{i} \gamma^{abc} \psi_{cj}\\
&+\frac{1}{2 L^{4}} E_{b} E_{d} L_{ik} \mathcal D^{d}\!\left(L^{jk}\right) \bar\psi_{a}{}^{i} \gamma^{abc} \psi_{cj}\\
&- \frac{1}{4 L^{4}} E_{b} L_{kl} \mathcal D_{d}\!\left(L^{kj}\right) \mathcal D^{d}\!\left(L_{i}{}^{l}\right) \bar\psi_{a}{}^{i} \gamma^{abc} \psi_{cj}
\end{aligned}
\tag{SCG25.1}
```

```math
\begin{aligned}
&+\frac{1}{2 L^{4}} E_{b} E_{d} L^{j}{}_{k} \mathcal D^{d}\!\left(L_{i}{}^{k}\right) \bar\psi_{a}{}^{i} \gamma^{abc} \psi_{cj}\\
&+\frac{\sqrt{2}}{4 L} \Box_c\!\left(L_{i}{}^{j}\right) V_{b} \bar\psi_{a}{}^{i} \gamma^{abc} \psi_{cj}\\
&- \frac{\sqrt{2}}{4 L^{3}} E_{d} E^{d} L_{i}{}^{j} V_{b} \bar\psi_{a}{}^{i} \gamma^{abc} \psi_{cj}\\
&- \frac{\sqrt{2} N^{2}}{4 L^{3}} L_{i}{}^{j} V_{b} \bar\psi_{a}{}^{i} \gamma^{abc} \psi_{cj}\\
&+\frac{2 \sqrt{2}}{3 L} L_{i}{}^{j} T_{de} T^{de} V_{b} \bar\psi_{a}{}^{i} \gamma^{abc} \psi_{cj}\\
&+\frac{\sqrt{2}}{L} D L_{i}{}^{j} V_{b} \bar\psi_{a}{}^{i} \gamma^{abc} \psi_{cj}\\
&- \frac{\sqrt{2}}{8 L^{3}} L_{kl} \mathcal D_{d}\!\left(L^{k}{}_{i}\right) \mathcal D^{d}\!\left(L^{jl}\right) V_{b} \bar\psi_{a}{}^{i} \gamma^{abc} \psi_{cj}\\
&+\frac{\sqrt{2}}{4 L^{3}} E_{d} L_{ik} \mathcal D^{d}\!\left(L^{jk}\right) V_{b} \bar\psi_{a}{}^{i} \gamma^{abc} \psi_{cj}
\end{aligned}
\tag{SCG25.2}
```

```math
\begin{aligned}
&- \frac{\sqrt{2}}{8 L^{3}} L_{kl} \mathcal D_{d}\!\left(L^{kj}\right) \mathcal D^{d}\!\left(L_{i}{}^{l}\right) V_{b} \bar\psi_{a}{}^{i} \gamma^{abc} \psi_{cj}\\
&+\frac{\sqrt{2}}{4 L^{3}} E_{d} L^{j}{}_{k} \mathcal D^{d}\!\left(L_{i}{}^{k}\right) V_{b} \bar\psi_{a}{}^{i} \gamma^{abc} \psi_{cj}
\end{aligned}
\tag{SCG25.3}
```

**Source group 26.**

```math
\left.e^{-1}\mathcal L_{R^2}\right|_{\text{source group }26}=+\frac12\rho'\Box_c\rho'
\tag{SCI26}
```

Substitute (SC1)–(SC8), retain the permitted degree and collect:

```math
\begin{aligned}
\left.e^{-1}\mathcal L_{R^2}\right|_{\text{group }26}={}&\frac{2 N}{L} \Box_c\!\left(\frac{N}{L}\right)\\
&+\frac{i N}{L} \Box_c\!\left(\frac{1}{L^{3}} L_{ij} \bar\varphi^{i} \varphi^{j}\right)\\
&- \frac{i}{L^{3}} L_{i}{}^{j} \Box_c\!\left(\frac{N}{L}\right) \bar\varphi^{i} \varphi_{j}
\end{aligned}
\tag{SCG26.1}
```

**Source group 27.**

```math
\left.e^{-1}\mathcal L_{R^2}\right|_{\text{source group }27}=+(\rho')^2 f_a{}^a
\tag{SCI27}
```

Substitute (SC1)–(SC8), retain the permitted degree and collect:

```math
\begin{aligned}
\left.e^{-1}\mathcal L_{R^2}\right|_{\text{group }27}={}&\frac{4 N^{2}}{L^{2}} f_{a}{}^{a}\\
&- \frac{4 i N}{L^{4}} L_{i}{}^{j} f_{a}{}^{a} \bar\varphi^{i} \varphi_{j}
\end{aligned}
\tag{SCG27.1}
```

**Source group 28.**

```math
\left.e^{-1}\mathcal L_{R^2}\right|_{\text{source group }28}=-\frac14\rho'\widehat F'_{ab}\widehat G^{ab}
\tag{SCI28}
```

Substitute (SC1)–(SC8), retain the permitted degree and collect:

```math
\begin{aligned}
\left.e^{-1}\mathcal L_{R^2}\right|_{\text{group }28}={}&- \frac{N}{L} \widehat G_{ab} \mathcal D^{a}\!\left(\frac{1}{L} E^{b}\right)\\
&+\frac{N}{L} \widehat G_{ab} \mathcal D^{b}\!\left(\frac{1}{L} E^{a}\right)\\
&- \frac{N}{L^{2}} \widehat G_{ab} L_{ij} \widehat R(V)^{abij}\\
&- \frac{N}{2 L^{4}} \widehat G_{ab} L_{ij} \mathcal D^{b}\!\left(L^{j}{}_{k}\right) \mathcal D^{a}\!\left(L^{ik}\right)\\
&+\frac{N}{2 L^{4}} \widehat G_{ab} L_{ij} \mathcal D^{a}\!\left(L^{j}{}_{k}\right) \mathcal D^{b}\!\left(L^{ik}\right)\\
&+\frac{N}{L} \widehat G^{ab} \mathcal D_{a}\!\left(\frac{1}{L^{3}} L_{ij} \bar\varphi^{i} \gamma_{b} \varphi^{j}\right)\\
&+\frac{i N}{2 L^{2}} \widehat G^{ab} \bar\varphi^{i} \widehat R(Q)_{abi}\\
&+\frac{i}{2 L^{3}} \widehat G_{ab} L_{i}{}^{j} \mathcal D^{a}\!\left(\frac{1}{L} E^{b}\right) \bar\varphi^{i} \varphi_{j}
\end{aligned}
\tag{SCG28.1}
```

```math
\begin{aligned}
&- \frac{i}{2 L^{3}} \widehat G_{ab} L_{i}{}^{j} \mathcal D^{b}\!\left(\frac{1}{L} E^{a}\right) \bar\varphi^{i} \varphi_{j}\\
&+\frac{i}{2 L^{4}} \widehat G_{ab} L_{i}{}^{j} L_{kl} \widehat R(V)^{abkl} \bar\varphi^{i} \varphi_{j}\\
&+\frac{i}{4 L^{6}} \widehat G_{ab} L_{i}{}^{j} L_{kl} \mathcal D^{b}\!\left(L^{l}{}_{m}\right) \mathcal D^{a}\!\left(L^{km}\right) \bar\varphi^{i} \varphi_{j}\\
&- \frac{i}{4 L^{6}} \widehat G_{ab} L_{i}{}^{j} L_{kl} \mathcal D^{a}\!\left(L^{l}{}_{m}\right) \mathcal D^{b}\!\left(L^{km}\right) \bar\varphi^{i} \varphi_{j}
\end{aligned}
\tag{SCG28.2}
```

**Source group 29.**

```math
\left.e^{-1}\mathcal L_{R^2}\right|_{\text{source group }29}=+4(\rho')^2\widehat G_{ab}T^{ab}
\tag{SCI29}
```

Substitute (SC1)–(SC8), retain the permitted degree and collect:

```math
\begin{aligned}
\left.e^{-1}\mathcal L_{R^2}\right|_{\text{group }29}={}&\frac{16 N^{2}}{L^{2}} \widehat G_{ab} T^{ab}\\
&- \frac{16 i N}{L^{4}} \widehat G_{ab} L_{i}{}^{j} T^{ab} \bar\varphi^{i} \varphi_{j}
\end{aligned}
\tag{SCG29.1}
```

**Source group 30.**

```math
\left.e^{-1}\mathcal L_{R^2}\right|_{\text{source group }30}=+4\rho'\widehat F'_{ab}T^{ab}
\tag{SCI30}
```

Substitute (SC1)–(SC8), retain the permitted degree and collect:

```math
\begin{aligned}
\left.e^{-1}\mathcal L_{R^2}\right|_{\text{group }30}={}&\frac{16 N}{L} \mathcal D_{a}\!\left(\frac{1}{L} E_{b}\right) T^{ab}\\
&- \frac{16 N}{L} \mathcal D_{a}\!\left(\frac{1}{L} E_{b}\right) T^{ba}\\
&+\frac{16 N}{L^{2}} L_{ij} \widehat R(V)_{ab}{}^{ij} T^{ab}\\
&+\frac{8 N}{L^{4}} L_{ij} \mathcal D_{a}\!\left(L^{j}{}_{k}\right) \mathcal D_{b}\!\left(L^{ik}\right) T^{ba}\\
&- \frac{8 N}{L^{4}} L_{ij} \mathcal D_{a}\!\left(L^{j}{}_{k}\right) \mathcal D_{b}\!\left(L^{ik}\right) T^{ab}\\
&- \frac{8 N}{L} T^{ab} \mathcal D_{a}\!\left(\frac{1}{L^{3}} L_{ij} \bar\varphi^{i} \gamma_{b} \varphi^{j}\right)\\
&+\frac{8 N}{L} T^{ba} \mathcal D_{a}\!\left(\frac{1}{L^{3}} L_{ij} \bar\varphi^{i} \gamma_{b} \varphi^{j}\right)\\
&- \frac{8 i N}{L^{2}} T^{ab} \bar\varphi^{i} \widehat R(Q)_{abi}
\end{aligned}
\tag{SCG30.1}
```

```math
\begin{aligned}
&- \frac{8 i}{L^{3}} L_{i}{}^{j} \mathcal D_{a}\!\left(\frac{1}{L} E_{b}\right) T^{ab} \bar\varphi^{i} \varphi_{j}\\
&+\frac{8 i}{L^{3}} L_{i}{}^{j} \mathcal D_{a}\!\left(\frac{1}{L} E_{b}\right) T^{ba} \bar\varphi^{i} \varphi_{j}\\
&- \frac{8 i}{L^{4}} L_{i}{}^{j} L_{kl} \widehat R(V)_{ab}{}^{kl} T^{ab} \bar\varphi^{i} \varphi_{j}\\
&- \frac{4 i}{L^{6}} L_{i}{}^{j} L_{kl} \mathcal D_{a}\!\left(L^{l}{}_{m}\right) \mathcal D_{b}\!\left(L^{km}\right) T^{ba} \bar\varphi^{i} \varphi_{j}\\
&+\frac{4 i}{L^{6}} L_{i}{}^{j} L_{kl} \mathcal D_{a}\!\left(L^{l}{}_{m}\right) \mathcal D_{b}\!\left(L^{km}\right) T^{ab} \bar\varphi^{i} \varphi_{j}
\end{aligned}
\tag{SCG30.2}
```

**Source group 31.**

```math
\left.e^{-1}\mathcal L_{R^2}\right|_{\text{source group }31}=-4(\rho')^2D
\tag{SCI31}
```

Substitute (SC1)–(SC8), retain the permitted degree and collect:

```math
\begin{aligned}
\left.e^{-1}\mathcal L_{R^2}\right|_{\text{group }31}={}&- \frac{16 N^{2}}{L^{2}} D\\
&+\frac{16 i N}{L^{4}} D L_{i}{}^{j} \bar\varphi^{i} \varphi_{j}
\end{aligned}
\tag{SCG31.1}
```

**Source group 32.**

```math
\left.e^{-1}\mathcal L_{R^2}\right|_{\text{source group }32}=-\frac{104}{3}(\rho')^2T^2
\tag{SCI32}
```

Substitute (SC1)–(SC8), retain the permitted degree and collect:

```math
\begin{aligned}
\left.e^{-1}\mathcal L_{R^2}\right|_{\text{group }32}={}&- \frac{416 N^{2}}{3 L^{2}} T_{ab} T^{ab}\\
&+\frac{416 i N}{3 L^{4}} L_{i}{}^{j} T_{ab} T^{ab} \bar\varphi^{i} \varphi_{j}
\end{aligned}
\tag{SCG32.1}
```

**Source group 33.**

```math
\left.e^{-1}\mathcal L_{R^2}\right|_{\text{source group }33}=+8i\rho'\bar\chi^i\lambda'_i
\tag{SCI33}
```

Substitute (SC1)–(SC8), retain the permitted degree and collect:

```math
\begin{aligned}
\left.e^{-1}\mathcal L_{R^2}\right|_{\text{group }33}={}&\frac{32 N}{L^{2}} \bar\chi^{i} \gamma^{a} \mathcal D_{a}\!\left(\varphi_{i}\right)\\
&- \frac{256 i N}{L^{2}} L_{i}{}^{j} \bar\chi^{i} \chi_{j}\\
&+\frac{64 i N}{L^{2}} T_{ab} \bar\chi^{i} \gamma^{ab} \varphi_{i}\\
&+\frac{32 i N^{2}}{L^{4}} L_{i}{}^{j} \bar\chi^{i} \varphi_{j}\\
&+\frac{32 N}{L^{4}} L^{j}{}_{k} \mathcal D_{a}\!\left(L_{i}{}^{k}\right) \bar\chi^{i} \gamma^{a} \varphi_{j}\\
&- \frac{32 N}{L^{4}} E_{a} L_{i}{}^{j} \bar\chi^{i} \gamma^{a} \varphi_{j}
\end{aligned}
\tag{SCG33.1}
```

**Source group 34.**

```math
\left.e^{-1}\mathcal L_{R^2}\right|_{\text{source group }34}=-5(\rho')^2\bar\psi_a{}^i\gamma^a\chi_i
\tag{SCI34}
```

Substitute (SC1)–(SC8), retain the permitted degree and collect:

```math
\begin{aligned}
\left.e^{-1}\mathcal L_{R^2}\right|_{\text{group }34}={}&- \frac{20 N^{2}}{L^{2}} \bar\psi_{a}{}^{i} \gamma^{a} \chi_{i}
\end{aligned}
\tag{SCG34.1}
```

**Source group 35.**

```math
\left.e^{-1}\mathcal L_{R^2}\right|_{\text{source group }35}=+\frac i4\rho'\bar\psi_a{}^i\gamma^a\not{\mathcal D}\lambda'_i
\tag{SCI35}
```

Substitute (SC1)–(SC8), retain the permitted degree and collect:

```math
\begin{aligned}
\left.e^{-1}\mathcal L_{R^2}\right|_{\text{group }35}={}&\frac{N}{L} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{b} \mathcal D_{b}\!\left(\frac{1}{L} \gamma^{c} \mathcal D_{c}\!\left(\varphi_{i}\right)\right)\\
&+\frac{8 i N}{L} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{b} \mathcal D_{b}\!\left(\frac{1}{L} L_{ij} \chi^{j}\right)\\
&+\frac{2 i N}{L} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{b} \mathcal D_{b}\!\left(\frac{1}{L} \gamma^{cd} T_{cd} \varphi_{i}\right)\\
&- \frac{i N}{L} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{b} \mathcal D_{b}\!\left(\frac{N}{L^{3}} L_{ij} \varphi^{j}\right)\\
&- \frac{N}{L} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{b} \mathcal D_{b}\!\left(\frac{1}{L^{3}} \gamma^{c} \mathcal D_{c}\!\left(L_{ij}\right) L^{jk} \varphi_{k}\right)\\
&+\frac{N}{L} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{b} \mathcal D_{b}\!\left(\frac{1}{L^{3}} \gamma^{c} E_{c} L_{ij} \varphi^{j}\right)
\end{aligned}
\tag{SCG35.1}
```

**Source group 36.**

```math
\left.e^{-1}\mathcal L_{R^2}\right|_{\text{source group }36}=+\frac12\rho'\bar\psi_a{}^i\gamma^a\gamma\!\cdot\!T\lambda'_i
\tag{SCI36}
```

Substitute (SC1)–(SC8), retain the permitted degree and collect:

```math
\begin{aligned}
\left.e^{-1}\mathcal L_{R^2}\right|_{\text{group }36}={}&- \frac{2 i N}{L^{2}} T_{bc} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{bc} \gamma^{d} \mathcal D_{d}\!\left(\varphi_{i}\right)\\
&- \frac{16 N}{L^{2}} L_{i}{}^{j} T_{bc} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{bc} \chi_{j}\\
&+\frac{4 N}{L^{2}} T_{bc} T_{de} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{bc} \gamma^{de} \varphi_{i}\\
&+\frac{2 N^{2}}{L^{4}} L_{i}{}^{j} T_{bc} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{bc} \varphi_{j}\\
&- \frac{2 i N}{L^{4}} L^{j}{}_{k} \mathcal D_{d}\!\left(L_{i}{}^{k}\right) T_{bc} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{bc} \gamma^{d} \varphi_{j}\\
&+\frac{2 i N}{L^{4}} E_{d} L_{i}{}^{j} T_{bc} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{bc} \gamma^{d} \varphi_{j}
\end{aligned}
\tag{SCG36.1}
```

**Source group 37.**

```math
\left.e^{-1}\mathcal L_{R^2}\right|_{\text{source group }37}=-\frac1{16}\rho'\bar\psi_a{}^i\gamma^a\gamma\!\cdot\!\widehat G\lambda'_i
\tag{SCI37}
```

Substitute (SC1)–(SC8), retain the permitted degree and collect:

```math
\begin{aligned}
\left.e^{-1}\mathcal L_{R^2}\right|_{\text{group }37}={}&\frac{i N}{4 L^{2}} \widehat G_{bc} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{bc} \gamma^{d} \mathcal D_{d}\!\left(\varphi_{i}\right)\\
&+\frac{2 N}{L^{2}} \widehat G_{bc} L_{i}{}^{j} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{bc} \chi_{j}\\
&- \frac{N}{2 L^{2}} \widehat G_{bc} T_{de} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{bc} \gamma^{de} \varphi_{i}\\
&- \frac{N^{2}}{4 L^{4}} \widehat G_{bc} L_{i}{}^{j} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{bc} \varphi_{j}\\
&+\frac{i N}{4 L^{4}} \widehat G_{bc} L^{j}{}_{k} \mathcal D_{d}\!\left(L_{i}{}^{k}\right) \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{bc} \gamma^{d} \varphi_{j}\\
&- \frac{i N}{4 L^{4}} E_{d} \widehat G_{bc} L_{i}{}^{j} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{bc} \gamma^{d} \varphi_{j}
\end{aligned}
\tag{SCG37.1}
```

**Source group 38.**

```math
\left.e^{-1}\mathcal L_{R^2}\right|_{\text{source group }38}=+\frac g8\rho'\bar\psi_a{}^i\gamma^aL_{ij}\lambda'{}^j
\tag{SCI38}
```

Substitute (SC1)–(SC8), retain the permitted degree and collect:

```math
\begin{aligned}
\left.e^{-1}\mathcal L_{R^2}\right|_{\text{group }38}={}&\frac{i N g}{2 L^{2}} L_{i}{}^{j} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{b} \mathcal D_{b}\!\left(\varphi_{j}\right)\\
&- 2 N g \bar\psi_{a}{}^{i} \gamma^{a} \chi_{i}\\
&- \frac{N g}{L^{2}} L_{i}{}^{j} T_{bc} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{bc} \varphi_{j}\\
&+\frac{N^{2} g}{4 L^{2}} \bar\psi_{a}{}^{i} \gamma^{a} \varphi_{i}\\
&- \frac{i N g}{2 L^{4}} L_{ik} L^{j}{}_{l} \mathcal D_{b}\!\left(L^{kl}\right) \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{b} \varphi_{j}\\
&+\frac{i N g}{4 L^{2}} E_{b} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{b} \varphi_{i}
\end{aligned}
\tag{SCG38.1}
```

**Source group 39.**

```math
\left.e^{-1}\mathcal L_{R^2}\right|_{\text{source group }39}=+\frac i4(\rho')^2\bar\psi_a{}^i\gamma^a\gamma^b [\frac14\gamma\!\cdot\!\widehat G\psi_{bi} -\gamma\!\cdot\!T\psi_{bi}+\frac g2L_{ij}\psi_b{}^j-\phi_{bi}]
\tag{SCI39}
```

Substitute (SC1)–(SC8), retain the permitted degree and collect:

```math
\begin{aligned}
\left.e^{-1}\mathcal L_{R^2}\right|_{\text{group }39}={}&\frac{i N^{2}}{4 L^{2}} \widehat G_{cd} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{b} \gamma^{cd} \psi_{bi}\\
&- \frac{i N^{2}}{L^{2}} T_{cd} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{b} \gamma^{cd} \psi_{bi}\\
&- \frac{i N^{2} g}{2 L^{2}} L_{i}{}^{j} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{b} \psi_{bj}\\
&- \frac{i N^{2}}{L^{2}} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{b} \phi_{bi}
\end{aligned}
\tag{SCG39.1}
```

**Source group 40.**

```math
\left.e^{-1}\mathcal L_{R^2}\right|_{\text{source group }40}=-\frac i4(\rho')^2\bar\psi_a{}^i [\frac14\gamma\!\cdot\!\widehat G\psi^a_i -\gamma\!\cdot\!T\psi^a_i+\frac g2L_{ij}\psi^{aj}-\phi^a_i]
\tag{SCI40}
```

Substitute (SC1)–(SC8), retain the permitted degree and collect:

```math
\begin{aligned}
\left.e^{-1}\mathcal L_{R^2}\right|_{\text{group }40}={}&- \frac{i N^{2}}{4 L^{2}} \widehat G_{bc} \bar\psi_{a}{}^{i} \gamma^{bc} \psi^{a}{}_{i}\\
&+\frac{i N^{2}}{L^{2}} T_{bc} \bar\psi_{a}{}^{i} \gamma^{bc} \psi^{a}{}_{i}\\
&+\frac{i N^{2} g}{2 L^{2}} L_{i}{}^{j} \bar\psi_{a}{}^{i} \psi^{a}{}_{j}\\
&+\frac{i N^{2}}{L^{2}} \bar\psi_{a}{}^{i} \phi^{a}{}_{i}
\end{aligned}
\tag{SCG40.1}
```

**Source group 41.**

```math
\left.e^{-1}\mathcal L_{R^2}\right|_{\text{source group }41}=-\frac{ig}8(\rho')^2\bar\psi_a{}^i\gamma^{ab}\psi_b{}^jL_{ij}
\tag{SCI41}
```

Substitute (SC1)–(SC8), retain the permitted degree and collect:

```math
\begin{aligned}
\left.e^{-1}\mathcal L_{R^2}\right|_{\text{group }41}={}&\frac{i N^{2} g}{2 L^{2}} L_{i}{}^{j} \bar\psi_{a}{}^{i} \gamma^{ab} \psi_{bj}
\end{aligned}
\tag{SCG41.1}
```

**Source group 42.**

```math
\left.e^{-1}\mathcal L_{R^2}\right|_{\text{source group }42}=+\frac i4\rho'\bar\psi_a{}^i\gamma^{ab}\psi_b{}^jY'_{ij}
\tag{SCI42}
```

Substitute (SC1)–(SC8), retain the permitted degree and collect:

```math
\begin{aligned}
\left.e^{-1}\mathcal L_{R^2}\right|_{\text{group }42}={}&- \frac{i N}{2 L^{2}} \Box_c\!\left(L_{i}{}^{j}\right) \bar\psi_{a}{}^{i} \gamma^{ab} \psi_{bj}\\
&+\frac{i N}{2 L^{4}} E_{c} E^{c} L_{i}{}^{j} \bar\psi_{a}{}^{i} \gamma^{ab} \psi_{bj}\\
&+\frac{i N^{3}}{2 L^{4}} L_{i}{}^{j} \bar\psi_{a}{}^{i} \gamma^{ab} \psi_{bj}\\
&- \frac{4 i N}{3 L^{2}} L_{i}{}^{j} T_{cd} T^{cd} \bar\psi_{a}{}^{i} \gamma^{ab} \psi_{bj}\\
&- \frac{2 i N}{L^{2}} D L_{i}{}^{j} \bar\psi_{a}{}^{i} \gamma^{ab} \psi_{bj}\\
&+\frac{i N}{4 L^{4}} L_{kl} \mathcal D_{c}\!\left(L^{k}{}_{i}\right) \mathcal D^{c}\!\left(L^{jl}\right) \bar\psi_{a}{}^{i} \gamma^{ab} \psi_{bj}\\
&- \frac{i N}{2 L^{4}} E_{c} L_{ik} \mathcal D^{c}\!\left(L^{jk}\right) \bar\psi_{a}{}^{i} \gamma^{ab} \psi_{bj}\\
&+\frac{i N}{4 L^{4}} L_{kl} \mathcal D_{c}\!\left(L^{kj}\right) \mathcal D^{c}\!\left(L_{i}{}^{l}\right) \bar\psi_{a}{}^{i} \gamma^{ab} \psi_{bj}
\end{aligned}
\tag{SCG42.1}
```

```math
\begin{aligned}
&- \frac{i N}{2 L^{4}} E_{c} L^{j}{}_{k} \mathcal D^{c}\!\left(L_{i}{}^{k}\right) \bar\psi_{a}{}^{i} \gamma^{ab} \psi_{bj}
\end{aligned}
\tag{SCG42.2}
```

### 4.4 Index collections and the shared derivative

All equalities in this subsection are off-shell algebraic identities, at the displayed explicit fermion order. No integration by parts is used. Inverse product-rule collection is now authorized; the full supercovariant derivative and every background composite remain intact.

First restore the unit-weight index operations by reversing (SC14):

```math
\begin{aligned}
&-\frac{L^{kl}}{2L^3}\left[(\mathcal D_aL_{ki})(\mathcal D^aL_{jl})+(\mathcal D_aL_{kj})(\mathcal D^aL_{il})\right]
=-\frac{L^{kl}}{L^3}\mathcal D_aL_{k(i}\mathcal D^aL_{j)l},\\
&2\mathcal D_a(L^{-1}E_b)-2\mathcal D_b(L^{-1}E_a)
=4\mathcal D_{[a}(L^{-1}E_{b]}).
\end{aligned}
\tag{SC21}
```

The fixed-index Majorana vector flip is symmetric. Raising the first SU(2) index contracts that symmetric tensor with epsilon:

```math
\begin{aligned}
\bar\varphi_i\gamma^a\varphi_j&=\bar\varphi_j\gamma^a\varphi_i,\\
\bar\varphi^i\gamma^a\varphi_i
&=\varepsilon^{ij}\bar\varphi_j\gamma^a\varphi_i
=\tfrac12\varepsilon^{ij}\left(\bar\varphi_j\gamma^a\varphi_i-\bar\varphi_i\gamma^a\varphi_j\right)=0,\\
\frac1{2L^3}\bar\varphi^m(\not{\mathcal D}L_{ij})\varphi_m
&=\frac{\mathcal D_aL_{ij}}{2L^3}\bar\varphi^m\gamma^a\varphi_m=0.
\end{aligned}
\tag{SC22}
```

Thus the last derivative-of-triplet singlet in (SC3) contributes zero in every descendant action product. This statement concerns the full identical spinors, not independent barred and unbarred test arrays.

For the remaining derivative terms, differentiate the defining norm algebraically with the covariant product rule:

```math
\begin{aligned}
L^2&=L_{ij}L^{ij},\\
2L\mathcal D_aL&=(\mathcal D_aL_{ij})L^{ij}+L_{ij}\mathcal D_aL^{ij}
=2L^{ij}\mathcal D_aL_{ij},\\
L\mathcal D_aL&=L^{ij}\mathcal D_aL_{ij}.
\end{aligned}
\tag{SC23}
```

Here metric/epsilon compatibility is used. This norm identity does not set a triplet derivative to zero in the aligned gauge. A general symmetric two-by-two matrix identity supplies the required tensor reduction. For this proof only let $`S`$ denote the matrix of entries $`L_{ij}`$, $`P`$ the matrix of entries $`\mathcal D_aL_{ij}`$ for a fixed tangent direction, and $`J=(\varepsilon^{ij})`$. These are temporary proof matrices, not additional fields. With $`S=\left(\begin{smallmatrix}u&v\\v&w\end{smallmatrix}\right)`$ and $`P=\left(\begin{smallmatrix}p&q\\q&r\end{smallmatrix}\right)`$, the three independent entries on both sides are

```math
\begin{aligned}
\mathop{\mathrm{adj}}\nolimits S&=\begin{pmatrix}w&-v\\-v&u\end{pmatrix},\\
(P\mathop{\mathrm{adj}}\nolimits S P)_{11}&=wp^2-2vpq+uq^2,\\
(P\mathop{\mathrm{adj}}\nolimits S P)_{12}&=wpq-v(pr+q^2)+uqr,\\
(P\mathop{\mathrm{adj}}\nolimits S P)_{22}&=wq^2-2vqr+ur^2,\\
P\mathop{\mathrm{adj}}\nolimits S P&=\mathop{\mathrm{tr}}\nolimits(\mathop{\mathrm{adj}}\nolimits S P)P-\det(P)S.
\end{aligned}
\tag{SC24}
```

Use $`\mathop{\mathrm{tr}}\nolimits(\mathop{\mathrm{adj}}\nolimits S P)=L\mathcal D_aL`$ and $`2\det P=\mathcal D_aL_{kl}\mathcal D_aL^{kl}`$; sum with $`\eta^{aa}`$, without changing derivative order. Multiplication by $`-L^{-3}`$ gives

```math
\begin{aligned}
L^{kl}\mathcal D_aL_{k(i}\mathcal D^aL_{j)l}
&=L(\mathcal D_aL)\mathcal D^aL_{ij}
-\tfrac12 L_{ij}\mathcal D_aL_{kl}\mathcal D^aL^{kl},\\
-L^{-3}L^{kl}\mathcal D_aL_{k(i}\mathcal D^aL_{j)l}
&=-L^{-2}(\mathcal D_aL)\mathcal D^aL_{ij}
+\frac{L_{ij}}{2L^3}\mathcal D_aL_{kl}\mathcal D^aL^{kl}.
\end{aligned}
\tag{SC25}
```

The second SU(2) identity involves the symmetric matrix with entries $`\bar\varphi_i\gamma_a\varphi_j`$. For this proof denote those entries by $`B=\left(\begin{smallmatrix}b&d\\d&e\end{smallmatrix}\right)`$. With $`\mathop{\mathrm{sym}}\nolimits M=(M+M^T)/2`$, direct multiplication gives

```math
\begin{aligned}
\mathop{\mathrm{tr}}\nolimits(\mathop{\mathrm{adj}}\nolimits B S)&=eu-2dv+bw,\\
\mathop{\mathrm{sym}}\nolimits(SJP)_{11}&=uq-vp,\\
\mathop{\mathrm{sym}}\nolimits(SJP)_{12}&=\tfrac12(ur-wp),\\
\mathop{\mathrm{sym}}\nolimits(SJP)_{22}&=vr-wq,\\
\mathop{\mathrm{sym}}\nolimits(PJB)_{11}&=pd-qb,\\
\mathop{\mathrm{sym}}\nolimits(PJB)_{12}&=\tfrac12(pe-rb),\\
\mathop{\mathrm{sym}}\nolimits(PJB)_{22}&=qe-rd,\\
\mathop{\mathrm{sym}}\nolimits(SJB\mathop{\mathrm{adj}}\nolimits S P)
&=(eu-2dv+bw)\mathop{\mathrm{sym}}\nolimits(SJP)
+(uw-v^2)\mathop{\mathrm{sym}}\nolimits(PJB).
\end{aligned}
\tag{SC26}
```

The three entries in the last line are, respectively,

```math
\begin{aligned}
& (eu-2dv+bw)(uq-vp)+(uw-v^2)(pd-qb),\\
& \tfrac12(eu-2dv+bw)(ur-wp)+\tfrac12(uw-v^2)(pe-rb),\\
& (eu-2dv+bw)(vr-wq)+(uw-v^2)(qe-rd).
\end{aligned}
\tag{SC27}
```

Restoring indices and $`\det S=L^2/2`$ yields the identity, followed by its substitution into the two original terms:

```math
\begin{aligned}
L_{k(i}L^{lm}\bar\varphi^k(\not{\mathcal D}L_{j)l})\varphi_m
={}&L^{mn}\bar\varphi_m\gamma_a\varphi_n\,L_{k(i}\mathcal D^aL_{j)}{}^k
+\frac{L^2}{2}\bar\varphi^k(\not{\mathcal D}L_{k(i})\varphi_{j)},\\
&-\frac3{L^5}L_{k(i}L^{lm}\bar\varphi^k(\not{\mathcal D}L_{j)l})\varphi_m
+\frac1{2L^3}\bar\varphi^k(\not{\mathcal D}L_{k(i})\varphi_{j)}\\
={}&-\frac3{L^5}L^{mn}\bar\varphi_m\gamma_a\varphi_n\,L_{k(i}\mathcal D^aL_{j)}{}^k
+\frac{-3/2+1/2}{L^3}\bar\varphi^k(\not{\mathcal D}L_{k(i})\varphi_{j)}\\
={}&-\frac3{L^5}L^{mn}\bar\varphi_m\gamma_a\varphi_n\,L_{k(i}\mathcal D^aL_{j)}{}^k
-\frac1{L^3}\bar\varphi^k(\not{\mathcal D}L_{k(i})\varphi_{j)}.
\end{aligned}
\tag{SC28}
```

Now collect the $`N`$ and $`E`$ bilinears without changing spinor order. Collect the two $`\chi`$ terms using $`L_{kl}\bar\chi^k\varphi^l=L^{kl}\bar\chi_k\varphi_l`$; the two epsilon transfers give a positive sign:

```math
\begin{aligned}
&\frac{iN}{L^3}\bar\varphi_{(i}\varphi_{j)}-\frac1{L^3}\bar\varphi_{(i}\not E\varphi_{j)}
=\frac1{L^3}\bar\varphi_{(i}(iN-\not E)\varphi_{j)},\\
&-\frac{3iN}{L^5}L_{ij}L^{kl}\bar\varphi_k\varphi_l
+\frac3{L^5}L_{ij}L^{kl}\bar\varphi_k\not E\varphi_l
=-\frac3{L^5}L_{ij}L^{kl}\bar\varphi_k(iN-\not E)\varphi_l,\\
&-\frac{16i}{L}\bar\chi_{(i}\varphi_{j)}+\frac{16i}{L^3}L_{ij}L^{kl}\bar\chi_k\varphi_l
=-\frac{16i}{L}\left(\delta_{(i}{}^k\delta_{j)}{}^l-\frac{L_{ij}L^{kl}}{L^2}\right)\bar\chi_k\varphi_l.
\end{aligned}
\tag{SC29}
```

Equations (SC22), (SC25), (SC28) and (SC29) turn the literal input (SC3) into the following collected map:

```math
\begin{aligned}
Y'_{ij}={}&\frac1L\Box_cL_{ij}-\frac1{L^2}(\mathcal D_aL)\mathcal D^aL_{ij}\\
&+\frac{L_{ij}}L\left(4D+\frac83T^2-\frac{N^2+E_aE^a}{L^2}
+\frac{\mathcal D_aL_{kl}\mathcal D^aL^{kl}}{2L^2}\right)\\
&+\frac2{L^3}L_{k(i}\mathcal D^aL_{j)}{}^k
\left(E_a-\frac3{2L^2}L^{mn}\bar\varphi_m\gamma_a\varphi_n\right)\\
&+\frac1{L^3}\bar\varphi_{(i}(iN-\not E)\varphi_{j)}
-\frac3{L^5}L_{ij}L^{kl}\bar\varphi_k(iN-\not E)\varphi_l\\
&-\frac{16i}{L}\left(\delta_{(i}{}^k\delta_{j)}{}^l-\frac{L_{ij}L^{kl}}{L^2}\right)\bar\chi_k\varphi_l\\
&+\frac2{L^3}L_{k(i}\bar\varphi^k\not{\mathcal D}\varphi_{j)}
-\frac1{L^3}\bar\varphi^k(\not{\mathcal D}L_{k(i})\varphi_{j)}\\
&+\frac{2i}{L^3}L_{ij}\bar\varphi^k\gamma\!\cdot\!T\varphi_k
+O_{\rm explicit}(\mathrm{fermion}^4).
\end{aligned}
\tag{SC30}
```

The $`-2NL^{-3}`$ and $`-2iL^{-3}\not E`$ terms in (SC2) have the common coefficient $`-2L^{-3}L_{ij}`$. The two antisymmetric derivatives in (SC4) combine by linearity. Hence

```math
\begin{aligned}
\lambda'_i={}&-\frac{2i}{L}\not{\mathcal D}\varphi_i+\frac{16}{L}L_{ij}\chi^j
+\frac4L\gamma\!\cdot\!T\varphi_i
-\frac2{L^3}L_{ij}(N+i\not E)\varphi^j\\
&+\frac{2i}{L^3}(\not{\mathcal D}L_{ij})L^{jk}\varphi_k
+O_{\rm explicit}(\mathrm{fermion}^3),\\
\widehat F'_{ab}={}&2\mathcal D_{[a}\!\left(\frac{2E_{b]}}L
-\frac{L_{ij}}{L^3}\bar\varphi^i\gamma_{b]}\varphi^j\right)
+\frac2L L_{ij}\widehat R_{ab}{}^{ij}(V)\\
&-\frac2{L^3}L_k{}^l\mathcal D_{[a}L^{kp}\mathcal D_{b]}L_{lp}
-\frac iL\bar\varphi^i\widehat R_{ab,i}(Q).
\end{aligned}
\tag{SC31}
```

For the action, groups 11–15 share $`A'_a`$. The displayed intermediate product rule keeps all derivative orderings:

```math
\begin{aligned}
&-\tfrac12A'_a(\mathcal D_b\rho')\widehat G^{ab}
-\tfrac12A'_a\rho'\mathcal D_b\widehat G^{ab}
-\tfrac12A'_a\mathcal D_b\widehat F'^{ab}\\
&\qquad+8A'_a(\mathcal D_b\rho')T^{ab}+8A'_a\rho'\mathcal D_bT^{ab}\\
&=-\tfrac12A'_a\left\{\mathcal D_b\widehat F'^{ab}
+(\mathcal D_b\rho')(\widehat G^{ab}-16T^{ab})
+\rho'\mathcal D_b(\widehat G^{ab}-16T^{ab})\right\}\\
&=-\tfrac12A'_a\mathcal D_b\!\left[\widehat F'^{ab}
+\rho'(\widehat G^{ab}-16T^{ab})\right].
\end{aligned}
\tag{SC32}
```

This is the inverse covariant product rule, not a discarded divergence. It differentiates the product of the two indicated representations with their inherited supercovariant connections. Substituting (SC1), (SC5) and (SC31) produces

```math
\begin{aligned}
&-\frac12\left(\frac{2E_a}L+\sqrt2V_a
-\frac{L_{rs}}{L^3}\bar\varphi^r\gamma_a\varphi^s
-\frac iL\bar\varphi^r\psi_{ar}\right)\mathcal D_b\Bigg[
2\mathcal D^{[a}\!\left(\frac{2E^{b]}}L-\frac{L_{ij}}{L^3}\bar\varphi^i\gamma^{b]}\varphi^j\right)\\
&\qquad+\frac2L L_{ij}\widehat R^{ab,ij}(V)
-\frac2{L^3}L_k{}^l\mathcal D^{[a}L^{kp}\mathcal D^{b]}L_{lp}
-\frac iL\bar\varphi^i\widehat R^{ab}{}_i(Q)\\
&\qquad+\left(\frac{2N}L+\frac{iL_{mn}}{L^3}\bar\varphi^m\varphi^n\right)
(\widehat G^{ab}-16T^{ab})\Bigg].
\end{aligned}
\tag{SC33}
```

In (SC33) the outer products are to be retained through two explicit fermions; Section 7 performs that truncation and displays their products separately, without any field projections. The derivative argument remains collected.

The other three group mergers follow directly:

```math
\begin{aligned}
-\tfrac14\rho'\widehat F'_{ab}\widehat G^{ab}+4\rho'\widehat F'_{ab}T^{ab}
&=-\tfrac14\rho'\widehat F'_{ab}(\widehat G^{ab}-16T^{ab}),\\
\bar\chi^i\lambda'_i
&=\varepsilon^{ij}\bar\chi_j\lambda'_i
=\varepsilon^{ij}\bar\lambda'_i\chi_j=-\bar\lambda'^i\chi_i,\\
-8i\rho'\bar\lambda'^i\chi_i+8i\rho'\bar\chi^i\lambda'_i
&=-16i\rho'\bar\lambda'^i\chi_i,\\
\gamma^a\gamma^b&=\gamma^{ab}+\eta^{ab},\\
\frac{i(\rho')^2}{4}\bar\psi_a^i\gamma^a\gamma^b\mathcal D_b\psi_i
-\frac{i(\rho')^2}{4}\bar\psi_a^i\mathcal D^a\psi_i
&=\frac{i(\rho')^2}{4}\bar\psi_a^i\gamma^{ab}\mathcal D_b\psi_i.
\end{aligned}
\tag{SC34}
```

The middle minus sign includes the epsilon interchange after the fixed-index scalar flip. The last line uses the defining gaugino derivative from Step 4, evaluated before its field is set to zero:

```math
\mathcal D_a\psi_i
=\left(\tfrac14\gamma\!\cdot\!\widehat G-\gamma\!\cdot\!T\right)\psi_{ai}
+\tfrac g2L_{ij}\psi_a{}^j-\phi_{ai}.
\tag{SC35}
```

That bracket, including $`\phi_{ai}`$, is inserted in the final density. It is never replaced by zero.

For reproducible outer multiplication, assign each *term*, internally, its displayed odd degree and use $`(cM)(dN)=cd\,MN`$ only when the sum of degrees is at most two. This bookkeeping introduces no projected field in the report. Equal contractions are then collected. The source coverage is: groups $`(11,12,13,14,15)`$ become (SC32), $`(28,30)`$ give the first line of (SC34), $`(5,33)`$ the scalar flip, and $`(39,40)`$ the Clifford cancellation. Every other original group appears once. The result is recorded term by term in [the collected ledger](<../../../../expected/step6_supercovariant_collected_ledger.json>).

The printed parentheses and brackets act on indices of the same variance. Where dummy-index normalization would otherwise produce a mixed SU(2) pair, the final expression displays the required epsilon explicitly; no delta is substituted for epsilon. Common scalar or Clifford coefficients are collected inside ordinary brackets, with their full field expressions written out. These brackets are not new composites or field names.

## 5. Consistency Checks

### 5.1 Source coverage, indices and dimensions

The strict parent parser supplies all 42 groups and 57 rows. Each replacement uses the same tensor and spinor index positions as its parent slot. Every raw and collected scalar monomial has exactly two occurrences of each dummy index with opposite variance; no free index remains. The grading retains only zero or two explicit odd factors. Numeric coefficients and powers of $`L,N,g`$ are multiplied exactly.

On the fixed-compensator slice, the engineering dimensions are

```math
\begin{aligned}
[L]=[L_{ij}]&=0,&[N]=[E_a]=[g]=[V_a]=[\widehat G]=[T]&=1,\\
[\varphi]=[\psi_a]&=\tfrac12,&[\chi]=[\phi_a]=[\widehat R(Q)]&=\tfrac32,\\
[D]=[f_a{}^a]=[\widehat R(V)]&=2,&[\mathcal D]=1,\quad[\Box_c]&=2.
\end{aligned}
\tag{SC19}
```

Consequently $`[\rho']=1`$, $`[\lambda']=3/2`$, $`[Y']=2`$, $`[\widehat F']=2`$, $`[A']=1`$. Every resulting density monomial has dimension four; this is checked recursively through each retained operator's argument. The pre-gauge Weyl-weight checks of Step 5 remain the source-level anchor and are not replaced by these gauge-fixed dimensions.

### 5.2 Explicit algebra and limit checks

Equations (SC9), (SC13), (SC14) and (SC17) display respectively the scalar cross coefficient, a kinetic coefficient, the symmetry factors and a triplet contraction. A separate constant bosonic-slot test sets derivative arguments, $`E`$, curvatures and all odd factors to zero, while keeping $`T^2,D,N,L`$ as algebraic test values. Then the triplet square and mixed coupling reduce to

```math
\begin{aligned}
Y'^{ij}Y'_{ij}-g\rho'Y'^{ij}L_{ij}
={}&L^2\left(-\frac{N^2}{L^3}+\frac{8T^2}{3L}+\frac{4D}{L}\right)^2
-2gNL\left(-\frac{N^2}{L^3}+\frac{8T^2}{3L}+\frac{4D}{L}\right)\\
={}&\frac{N^4}{L^4}-\frac{16N^2T^2}{3L^2}-\frac{8N^2D}{L^2}
+\frac{64}{9}(T^2)^2+\frac{64}{3}DT^2+16D^2\\
&+\frac{2gN^3}{L^2}-\frac{16}{3}gNT^2-8gND.
\end{aligned}
\tag{SC20}
```

This is a coefficient check, not an on-shell field configuration. The coefficient limit $`g\to0`$ is regular and removes exactly the terms with an explicit factor of $`g`$. The retained background composites continue to carry their gauged definitions; a complete ungauged limit also acts on those definitions. The actual bosonic restriction, including the earlier background insertion and boundary conventions, remains Eq. (C13) of the preserved Step 6 report.

### 5.3 Reproducible checks and their scope

- [Ordered symbolic verification](<../../../../README.md>): **136/136 pass**. Each group is checked against a separately expanded noncommuting SymPy polynomial; indices, dimensions, retained degree, source hashes and the displayed limits are checked.
- [Independent tensor verification](<../../../../README.md>): **161/161 pass**, maximum scaled residual $`3.78e-16`$ against threshold $`2\times10^{-10}`$. This evaluates explicit five-dimensional gamma matrices, Lorentz and SU(2) contractions, and two-generator Grassmann coefficients before and after simplification.
- [Distribution ledger](<../../../../expected/step6_supercovariant_ledger.json>): all source groups, insertion counts, resulting coefficients, operator arguments and final display rows. Internal implementation identifiers do not appear in the action.

The numerical test treats retained operator arguments as tensor jets; it tests the *outer* contraction simplifications without expanding those arguments. For two odd jets it uses $`x_1y_2-x_2y_1`$, while an even degree-two jet multiplies the single coefficient of $`\theta_1\theta_2`$. It therefore does not silently commute the spinors. No local-SUSY or complete reality proof is claimed by these algebraic tests.

The preceding baseline tests do not impose a relation between barred and unbarred jets and therefore do not verify the new Majorana flip. The additional current-revision tests below supply that check separately.

The [exact collection checks](<../../../../README.md>) pass **386/386** checks: the general two-by-two polynomial identities, numerical coefficients, inverse product rule, unique coverage of all 42 source groups, recursively matched dimensions, grading, expanded-node indices and source hashes. The [independent Majorana-aware test](<../../../../README.md>) passes **120/120** checks. It sets $`C=\gamma^2\gamma^4`$, verifies $`C^T=-C`$ and $`(\gamma^a)^TC=C\gamma^a`$, constructs bars as $`\varphi_i^TC`$, and uses two Grassmann channels. It tests all three symmetric triplet components in three deterministic samples and every outer source-group collection; its maximum scaled residual is $`1.75e-16`$ against $`2\times10^{-10}`$. These check the displayed algebra, without asserting a local-SUSY or full reality proof.

## 6. Convention Dependence and Remaining Uncertainties

The inherited map-source qualifications and gradient-phase repair remain unchanged. The full supercovariant definitions retain their original common gauged background, including source-order qualifications. This representation does not resolve the earlier source-comparison, full reality or local-supersymmetry questions. Gauge fixing has not removed the derivative of a fixed field or replaced the spin connection by its bosonic value.

The remainder below counts *explicit* fermions. Full operators and hatted quantities implicitly retain higher-order completions, in this representation. The excluded cubic gaugino and quartic triplet contributions first affect the even density at degree four. No numerical error estimate for Grassmann degree, spectrum assertion, or auxiliary elimination is implied.

## 7. Final Result

All primed definitions are inserted. Outer products are distributed through two explicit fermions, then common scalar/Clifford brackets, symmetric/antisymmetric contractions and shared derivative arguments are collected using Section 4.4. The following continued displays are **one action density**, without a bosonic/fermionic split or new field aliases. They contain 373 additive terms, replacing the former 661-term endpoint. Derivatives continue to act on the complete explicitly written arguments; $`T,\chi,D`$ and the other retained background quantities are their full gauged composites. A product of two identical collected coefficient brackets may be read as their square; no omitted term is hidden in a primed variable.

```math
\boxed{S_{R^2}=\int d^5x\,\mathcal L_{R^2}}.
\tag{SCA}
```

```math
\begin{aligned}
e^{-1}\mathcal L_{R^2}={}&\frac{1}{L^{2}} \Box_c\!\left(L_{ij}\right) \Box_c\!\left(L^{ij}\right)\\
&- \frac{2}{L^{3}} \Box_c\!\left(L_{ij}\right) \mathcal D_{a}\!\left(L\right) \mathcal D^{a}\!\left(L^{ij}\right)\\
&+\frac{2}{L^{2}} \left(4 D +\frac{8}{3} T_{ab} T^{ab} - \frac{1}{L^{2}} E_{a} E^{a} - \frac{N^{2}}{L^{2}} +\frac{1}{2 L^{2}} \mathcal D_{a}\!\left(L_{kl}\right) \mathcal D^{a}\!\left(L^{kl}\right)\right) L_{ij} \Box_c\!\left(L^{ij}\right)\\
&+\frac{2}{L^{4}} \Box_c\!\left(L^{ij}\right) \left(\bar\varphi_{(i} \left(i N - \gamma^{b} E_{b}\right) \varphi_{j)}\right)\\
&+\frac{6}{L^{6}} L_{i}{}^{j} L_{kl} \Box_c\!\left(L^{kl}\right) \bar\varphi^{i} \left(i N - \gamma^{a} E_{a}\right) \varphi_{j}\\
&+\frac{4}{L^{4}} E_{a} \left(L_{k(i} \mathcal D^{a}\!\left(L_{j)}{}^{k}\right)\right) \Box_c\!\left(L^{ij}\right)\\
&+\frac{6}{L^{6}} \left(L_{m(k} \mathcal D_{a}\!\left(L_{l)}{}^{m}\right)\right) L_{i}{}^{j} \Box_c\!\left(L^{kl}\right) \bar\varphi^{i} \gamma^{a} \varphi_{j}\\
&- \frac{32 i}{L^{2}} \Box_c\!\left(L^{ij}\right) \left(\bar\chi_{(i} \varphi_{j)}\right)
\end{aligned}
\tag{SCF.1}
```

```math
\begin{aligned}
&- \frac{32 i}{L^{4}} L_{i}{}^{j} L_{kl} \Box_c\!\left(L^{kl}\right) \bar\chi^{i} \varphi_{j}\\
&+\frac{4}{L^{4}} \Box_c\!\left(L^{ij}\right) \left(L_{k(i} \bar\varphi^{k} \gamma^{a} \mathcal D_{a}\!\left(\varphi_{j)}\right)\right)\\
&- \frac{2}{L^{4}} \Box_c\!\left(L^{ij}\right) \left(\bar\varphi^{k} \gamma^{a} \mathcal D_{a}\!\left(L_{k(i}\right) \varphi_{j)}\right)\\
&+\frac{4 i}{L^{4}} L_{jk} \Box_c\!\left(L^{jk}\right) T_{ab} \bar\varphi^{i} \gamma^{ab} \varphi_{i}\\
&+\frac{1}{L^{4}} \mathcal D_{a}\!\left(L\right) \mathcal D_{b}\!\left(L\right) \mathcal D^{a}\!\left(L_{ij}\right) \mathcal D^{b}\!\left(L^{ij}\right)\\
&- \frac{2}{L^{3}} \left(4 D +\frac{8}{3} T_{bc} T^{bc} - \frac{1}{L^{2}} E_{b} E^{b} - \frac{N^{2}}{L^{2}} +\frac{1}{2 L^{2}} \mathcal D_{b}\!\left(L_{kl}\right) \mathcal D^{b}\!\left(L^{kl}\right)\right) L_{ij} \mathcal D_{a}\!\left(L\right) \mathcal D^{a}\!\left(L^{ij}\right)\\
&- \frac{2}{L^{5}} \mathcal D_{a}\!\left(L\right) \mathcal D^{a}\!\left(L^{ij}\right) \left(\bar\varphi_{(i} \left(i N - \gamma^{c} E_{c}\right) \varphi_{j)}\right)\\
&- \frac{6}{L^{7}} L_{i}{}^{j} L_{kl} \mathcal D_{a}\!\left(L\right) \mathcal D^{a}\!\left(L^{kl}\right) \bar\varphi^{i} \left(i N - \gamma^{b} E_{b}\right) \varphi_{j}
\end{aligned}
\tag{SCF.2}
```

```math
\begin{aligned}
&- \frac{4}{L^{5}} E_{a} \left(L_{k(i} \mathcal D^{a}\!\left(L_{j)}{}^{k}\right)\right) \mathcal D_{b}\!\left(L\right) \mathcal D^{b}\!\left(L^{ij}\right)\\
&- \frac{6}{L^{7}} \left(L_{m(k} \mathcal D_{a}\!\left(L_{l)}{}^{m}\right)\right) L_{i}{}^{j} \mathcal D_{b}\!\left(L\right) \mathcal D^{b}\!\left(L^{kl}\right) \bar\varphi^{i} \gamma^{a} \varphi_{j}\\
&+\frac{32 i}{L^{3}} \mathcal D_{a}\!\left(L\right) \mathcal D^{a}\!\left(L^{ij}\right) \left(\bar\chi_{(i} \varphi_{j)}\right)\\
&+\frac{32 i}{L^{5}} L_{i}{}^{j} L_{kl} \mathcal D_{a}\!\left(L\right) \mathcal D^{a}\!\left(L^{kl}\right) \bar\chi^{i} \varphi_{j}\\
&- \frac{4}{L^{5}} \mathcal D_{a}\!\left(L\right) \mathcal D^{a}\!\left(L^{ij}\right) \left(L_{k(i} \bar\varphi^{k} \gamma^{b} \mathcal D_{b}\!\left(\varphi_{j)}\right)\right)\\
&+\frac{2}{L^{5}} \mathcal D_{a}\!\left(L\right) \mathcal D^{a}\!\left(L^{ij}\right) \left(\bar\varphi^{k} \gamma^{b} \mathcal D_{b}\!\left(L_{k(i}\right) \varphi_{j)}\right)\\
&- \frac{4 i}{L^{5}} L_{jk} \mathcal D_{c}\!\left(L\right) \mathcal D^{c}\!\left(L^{jk}\right) T_{ab} \bar\varphi^{i} \gamma^{ab} \varphi_{i}\\
&+\left(4 D +\frac{8}{3} T_{ab} T^{ab} - \frac{1}{L^{2}} E_{a} E^{a} - \frac{N^{2}}{L^{2}} +\frac{1}{2 L^{2}} \mathcal D_{a}\!\left(L_{ij}\right) \mathcal D^{a}\!\left(L^{ij}\right)\right) \left(4 D +\frac{8}{3} T_{cd} T^{cd} - \frac{1}{L^{2}} E_{c} E^{c} - \frac{N^{2}}{L^{2}} +\frac{1}{2 L^{2}} \mathcal D_{c}\!\left(L_{kl}\right) \mathcal D^{c}\!\left(L^{kl}\right)\right)
\end{aligned}
\tag{SCF.3}
```

```math
\begin{aligned}
&+\frac{2}{L^{4}} \left(4 D +\frac{8}{3} T_{ab} T^{ab} - \frac{1}{L^{2}} E_{a} E^{a} - \frac{N^{2}}{L^{2}} +\frac{1}{2 L^{2}} \mathcal D_{a}\!\left(L_{kl}\right) \mathcal D^{a}\!\left(L^{kl}\right)\right) L^{ij} \left(\bar\varphi_{(i} \left(i N - \gamma^{d} E_{d}\right) \varphi_{j)}\right)\\
&+\frac{6}{L^{4}} \left(4 D +\frac{8}{3} T_{ab} T^{ab} - \frac{1}{L^{2}} E_{a} E^{a} - \frac{N^{2}}{L^{2}} +\frac{1}{2 L^{2}} \mathcal D_{a}\!\left(L_{kl}\right) \mathcal D^{a}\!\left(L^{kl}\right)\right) L_{i}{}^{j} \bar\varphi^{i} \left(i N - \gamma^{c} E_{c}\right) \varphi_{j}\\
&+\frac{4}{L^{4}} E_{a} \left(4 D +\frac{8}{3} T_{bc} T^{bc} - \frac{1}{L^{2}} E_{b} E^{b} - \frac{N^{2}}{L^{2}} +\frac{1}{2 L^{2}} \mathcal D_{b}\!\left(L_{kl}\right) \mathcal D^{b}\!\left(L^{kl}\right)\right) \left(L_{m(i} \mathcal D^{a}\!\left(L_{j)}{}^{m}\right)\right) L^{ij}\\
&+\frac{6}{L^{6}} \left(4 D +\frac{8}{3} T_{bc} T^{bc} - \frac{1}{L^{2}} E_{b} E^{b} - \frac{N^{2}}{L^{2}} +\frac{1}{2 L^{2}} \mathcal D_{b}\!\left(L_{mn}\right) \mathcal D^{b}\!\left(L^{mn}\right)\right) \left(L_{o(k} \mathcal D_{a}\!\left(L_{l)}{}^{o}\right)\right) L_{i}{}^{j} L^{kl} \bar\varphi^{i} \gamma^{a} \varphi_{j}\\
&- \frac{32 i}{L^{2}} \left(4 D +\frac{8}{3} T_{ab} T^{ab} - \frac{1}{L^{2}} E_{a} E^{a} - \frac{N^{2}}{L^{2}} +\frac{1}{2 L^{2}} \mathcal D_{a}\!\left(L_{kl}\right) \mathcal D^{a}\!\left(L^{kl}\right)\right) L^{ij} \left(\bar\chi_{(i} \varphi_{j)}\right)\\
&- \frac{32 i}{L^{2}} \left(4 D +\frac{8}{3} T_{ab} T^{ab} - \frac{1}{L^{2}} E_{a} E^{a} - \frac{N^{2}}{L^{2}} +\frac{1}{2 L^{2}} \mathcal D_{a}\!\left(L_{kl}\right) \mathcal D^{a}\!\left(L^{kl}\right)\right) L_{i}{}^{j} \bar\chi^{i} \varphi_{j}\\
&+\frac{4}{L^{4}} \left(4 D +\frac{8}{3} T_{ab} T^{ab} - \frac{1}{L^{2}} E_{a} E^{a} - \frac{N^{2}}{L^{2}} +\frac{1}{2 L^{2}} \mathcal D_{a}\!\left(L_{kl}\right) \mathcal D^{a}\!\left(L^{kl}\right)\right) L^{ij} \left(L_{m(i} \bar\varphi^{m} \gamma^{c} \mathcal D_{c}\!\left(\varphi_{j)}\right)\right)\\
&- \frac{2}{L^{4}} \left(4 D +\frac{8}{3} T_{ab} T^{ab} - \frac{1}{L^{2}} E_{a} E^{a} - \frac{N^{2}}{L^{2}} +\frac{1}{2 L^{2}} \mathcal D_{a}\!\left(L_{kl}\right) \mathcal D^{a}\!\left(L^{kl}\right)\right) L^{ij} \left(\bar\varphi^{m} \gamma^{c} \mathcal D_{c}\!\left(L_{m(i}\right) \varphi_{j)}\right)
\end{aligned}
\tag{SCF.4}
```

```math
\begin{aligned}
&+\frac{4 i}{L^{2}} \left(4 D +\frac{8}{3} T_{cd} T^{cd} - \frac{1}{L^{2}} E_{c} E^{c} - \frac{N^{2}}{L^{2}} +\frac{1}{2 L^{2}} \mathcal D_{c}\!\left(L_{jk}\right) \mathcal D^{c}\!\left(L^{jk}\right)\right) T_{ab} \bar\varphi^{i} \gamma^{ab} \varphi_{i}\\
&+\frac{4}{L^{6}} E_{a} \left(L_{k}{}^{(i} \mathcal D^{a}\!\left(L^{j)k}\right)\right) \left(\bar\varphi_{(i} \left(i N - \gamma^{c} E_{c}\right) \varphi_{j)}\right)\\
&+\frac{12}{L^{8}} E_{a} \left(L_{m(k} \mathcal D^{a}\!\left(L_{l)}{}^{m}\right)\right) L_{i}{}^{j} L^{kl} \bar\varphi^{i} \left(i N - \gamma^{b} E_{b}\right) \varphi_{j}\\
&+\frac{4}{L^{6}} E_{a} E_{b} \left(L_{k(i} \mathcal D^{a}\!\left(L_{j)}{}^{k}\right)\right) \left(L_{l}{}^{(i} \mathcal D^{b}\!\left(L^{j)l}\right)\right)\\
&+\frac{6}{L^{8}} E_{b} \left(L_{m(k} \mathcal D^{b}\!\left(L_{l)}{}^{m}\right)\right) \left(L_{n}{}^{(k} \mathcal D_{a}\!\left(L^{l)n}\right)\right) L_{i}{}^{j} \bar\varphi^{i} \gamma^{a} \varphi_{j}\\
&- \frac{64 i}{L^{4}} E_{a} \left(L_{k}{}^{(i} \mathcal D^{a}\!\left(L^{j)k}\right)\right) \left(\bar\chi_{(i} \varphi_{j)}\right)\\
&- \frac{64 i}{L^{6}} E_{a} \left(L_{m(k} \mathcal D^{a}\!\left(L_{l)}{}^{m}\right)\right) L_{i}{}^{j} L^{kl} \bar\chi^{i} \varphi_{j}\\
&+\frac{8}{L^{6}} E_{a} \left(L_{k}{}^{(i} \mathcal D^{a}\!\left(L^{j)k}\right)\right) \left(L_{l(i} \bar\varphi^{l} \gamma^{b} \mathcal D_{b}\!\left(\varphi_{j)}\right)\right)
\end{aligned}
\tag{SCF.5}
```

```math
\begin{aligned}
&- \frac{4}{L^{6}} E_{a} \left(L_{k}{}^{(i} \mathcal D^{a}\!\left(L^{j)k}\right)\right) \left(\bar\varphi^{l} \gamma^{b} \mathcal D_{b}\!\left(L_{l(i}\right) \varphi_{j)}\right)\\
&+\frac{8 i}{L^{6}} E_{c} \left(L_{l(j} \mathcal D^{c}\!\left(L_{k)}{}^{l}\right)\right) L^{jk} T_{ab} \bar\varphi^{i} \gamma^{ab} \varphi_{i}\\
&+\frac{6}{L^{8}} E_{b} \left(L_{m(k} \mathcal D_{a}\!\left(L_{l)}{}^{m}\right)\right) \left(L_{n}{}^{(k} \mathcal D^{b}\!\left(L^{l)n}\right)\right) L_{i}{}^{j} \bar\varphi^{i} \gamma^{a} \varphi_{j}\\
&- \frac{2 N g}{L^{2}} L_{ij} \Box_c\!\left(L^{ij}\right)\\
&+\frac{2 N g}{L^{3}} L_{ij} \mathcal D_{a}\!\left(L\right) \mathcal D^{a}\!\left(L^{ij}\right)\\
&- 2 N g \left(4 D +\frac{8}{3} T_{ab} T^{ab} - \frac{1}{L^{2}} E_{a} E^{a} - \frac{N^{2}}{L^{2}} +\frac{1}{2 L^{2}} \mathcal D_{a}\!\left(L_{ij}\right) \mathcal D^{a}\!\left(L^{ij}\right)\right)\\
&- \frac{2 N g}{L^{4}} L^{ij} \left(\bar\varphi_{(i} \left(i N - \gamma^{b} E_{b}\right) \varphi_{j)}\right)\\
&- \frac{6 N g}{L^{4}} L_{i}{}^{j} \bar\varphi^{i} \left(i N - \gamma^{a} E_{a}\right) \varphi_{j}
\end{aligned}
\tag{SCF.6}
```

```math
\begin{aligned}
&- \frac{4 N g}{L^{4}} E_{a} \left(L_{k(i} \mathcal D^{a}\!\left(L_{j)}{}^{k}\right)\right) L^{ij}\\
&- \frac{6 N g}{L^{6}} \left(L_{m(k} \mathcal D_{a}\!\left(L_{l)}{}^{m}\right)\right) L_{i}{}^{j} L^{kl} \bar\varphi^{i} \gamma^{a} \varphi_{j}\\
&+\frac{32 i N g}{L^{2}} L^{ij} \left(\bar\chi_{(i} \varphi_{j)}\right)\\
&+\frac{32 i N g}{L^{2}} L_{i}{}^{j} \bar\chi^{i} \varphi_{j}\\
&- \frac{4 N g}{L^{4}} L^{ij} \left(L_{k(i} \bar\varphi^{k} \gamma^{a} \mathcal D_{a}\!\left(\varphi_{j)}\right)\right)\\
&+\frac{2 N g}{L^{4}} L^{ij} \left(\bar\varphi^{k} \gamma^{a} \mathcal D_{a}\!\left(L_{k(i}\right) \varphi_{j)}\right)\\
&- \frac{4 i N g}{L^{2}} T_{ab} \bar\varphi^{i} \gamma^{ab} \varphi_{i}\\
&+\frac{i g}{L^{4}} L_{i}{}^{j} L_{kl} \Box_c\!\left(L^{kl}\right) \bar\varphi^{i} \varphi_{j}
\end{aligned}
\tag{SCF.7}
```

```math
\begin{aligned}
&- \frac{i g}{L^{5}} L_{i}{}^{j} L_{kl} \mathcal D_{a}\!\left(L\right) \mathcal D^{a}\!\left(L^{kl}\right) \bar\varphi^{i} \varphi_{j}\\
&+\frac{i g}{L^{2}} \left(4 D +\frac{8}{3} T_{ab} T^{ab} - \frac{1}{L^{2}} E_{a} E^{a} - \frac{N^{2}}{L^{2}} +\frac{1}{2 L^{2}} \mathcal D_{a}\!\left(L_{kl}\right) \mathcal D^{a}\!\left(L^{kl}\right)\right) L_{i}{}^{j} \bar\varphi^{i} \varphi_{j}\\
&+\frac{2 i g}{L^{6}} E_{a} \left(L_{m(k} \mathcal D^{a}\!\left(L_{l)}{}^{m}\right)\right) L_{i}{}^{j} L^{kl} \bar\varphi^{i} \varphi_{j}\\
&- \frac{2}{L} \mathcal D_{a}\!\left(\bar\varphi_{i}\right) \gamma^{a} \gamma^{b} \mathcal D_{b}\!\left(\frac{1}{L} \gamma^{c} \mathcal D_{c}\!\left(\varphi^{i}\right)\right)\\
&- \frac{16 i}{L} \mathcal D_{a}\!\left(\bar\varphi_{i}\right) \gamma^{a} \gamma^{b} \mathcal D_{b}\!\left(\frac{1}{L} L^{i}{}_{j} \chi^{j}\right)\\
&- \frac{4 i}{L} \mathcal D_{a}\!\left(\bar\varphi_{i}\right) \gamma^{a} \gamma^{b} \mathcal D_{b}\!\left(\frac{1}{L} \gamma^{cd} T_{cd} \varphi^{i}\right)\\
&+\frac{2 i}{L} \mathcal D_{a}\!\left(\bar\varphi_{i}\right) \gamma^{a} \gamma^{b} \mathcal D_{b}\!\left(\frac{1}{L^{3}} L^{i}{}_{j} \left(i \gamma^{c} E_{c} +N\right) \varphi^{j}\right)\\
&+\frac{2}{L} \mathcal D_{a}\!\left(\bar\varphi_{i}\right) \gamma^{a} \gamma^{b} \mathcal D_{b}\!\left(\frac{1}{L^{3}} \gamma^{c} \mathcal D_{c}\!\left(L^{i}{}_{j}\right) L^{jk} \varphi_{k}\right)
\end{aligned}
\tag{SCF.8}
```

```math
\begin{aligned}
&+\frac{16 i}{L} L_{i}{}^{j} \bar\chi^{i} \gamma^{a} \mathcal D_{a}\!\left(\frac{1}{L} \gamma^{b} \mathcal D_{b}\!\left(\varphi_{j}\right)\right)\\
&- \frac{128}{L} L_{i}{}^{j} \bar\chi^{i} \gamma^{a} \mathcal D_{a}\!\left(\frac{1}{L} L_{jk} \chi^{k}\right)\\
&- \frac{32}{L} L_{i}{}^{j} \bar\chi^{i} \gamma^{a} \mathcal D_{a}\!\left(\frac{1}{L} \gamma^{bc} T_{bc} \varphi_{j}\right)\\
&+\frac{16}{L} L_{i}{}^{j} \bar\chi^{i} \gamma^{a} \mathcal D_{a}\!\left(\frac{1}{L^{3}} L_{jk} \left(i \gamma^{b} E_{b} +N\right) \varphi^{k}\right)\\
&- \frac{16 i}{L} L_{i}{}^{j} \bar\chi^{i} \gamma^{a} \mathcal D_{a}\!\left(\frac{1}{L^{3}} \gamma^{b} \mathcal D_{b}\!\left(L_{jk}\right) L^{kl} \varphi_{l}\right)\\
&- \frac{4 i}{L} T_{ab} \bar\varphi^{i} \gamma^{ab} \gamma^{c} \mathcal D_{c}\!\left(\frac{1}{L} \gamma^{d} \mathcal D_{d}\!\left(\varphi_{i}\right)\right)\\
&+\frac{32}{L} T_{ab} \bar\varphi^{i} \gamma^{ab} \gamma^{c} \mathcal D_{c}\!\left(\frac{1}{L} L_{ij} \chi^{j}\right)\\
&+\frac{8}{L} T_{ab} \bar\varphi^{i} \gamma^{ab} \gamma^{c} \mathcal D_{c}\!\left(\frac{1}{L} \gamma^{de} T_{de} \varphi_{i}\right)
\end{aligned}
\tag{SCF.9}
```

```math
\begin{aligned}
&- \frac{4}{L} T_{ab} \bar\varphi^{i} \gamma^{ab} \gamma^{c} \mathcal D_{c}\!\left(\frac{1}{L^{3}} L_{ij} \left(i \gamma^{d} E_{d} +N\right) \varphi^{j}\right)\\
&+\frac{4 i}{L} T_{ab} \bar\varphi^{i} \gamma^{ab} \gamma^{c} \mathcal D_{c}\!\left(\frac{1}{L^{3}} \gamma^{d} \mathcal D_{d}\!\left(L_{ij}\right) L^{jk} \varphi_{k}\right)\\
&- \frac{2 i}{L^{3}} L_{i}{}^{j} \bar\varphi^{i} \left(i E_{b} \gamma^{b} +N\right) \gamma^{a} \mathcal D_{a}\!\left(\frac{1}{L} \gamma^{c} \mathcal D_{c}\!\left(\varphi_{j}\right)\right)\\
&+\frac{16}{L^{3}} L_{i}{}^{j} \bar\varphi^{i} \left(i E_{b} \gamma^{b} +N\right) \gamma^{a} \mathcal D_{a}\!\left(\frac{1}{L} L_{jk} \chi^{k}\right)\\
&+\frac{4}{L^{3}} L_{i}{}^{j} \bar\varphi^{i} \left(i E_{b} \gamma^{b} +N\right) \gamma^{a} \mathcal D_{a}\!\left(\frac{1}{L} \gamma^{cd} T_{cd} \varphi_{j}\right)\\
&- \frac{2}{L^{3}} L_{i}{}^{j} \bar\varphi^{i} \left(i E_{b} \gamma^{b} +N\right) \gamma^{a} \mathcal D_{a}\!\left(\frac{1}{L^{3}} L_{jk} \left(i \gamma^{c} E_{c} +N\right) \varphi^{k}\right)\\
&+\frac{2 i}{L^{3}} L_{i}{}^{j} \bar\varphi^{i} \left(i E_{b} \gamma^{b} +N\right) \gamma^{a} \mathcal D_{a}\!\left(\frac{1}{L^{3}} \gamma^{c} \mathcal D_{c}\!\left(L_{jk}\right) L^{kl} \varphi_{l}\right)\\
&- \frac{2}{L^{3}} L_{ik} \mathcal D_{a}\!\left(L^{jk}\right) \bar\varphi^{i} \gamma^{a} \gamma^{b} \mathcal D_{b}\!\left(\frac{1}{L} \gamma^{c} \mathcal D_{c}\!\left(\varphi_{j}\right)\right)
\end{aligned}
\tag{SCF.10}
```

```math
\begin{aligned}
&- \frac{16 i}{L^{3}} L_{ik} \mathcal D_{a}\!\left(L^{jk}\right) \bar\varphi^{i} \gamma^{a} \gamma^{b} \mathcal D_{b}\!\left(\frac{1}{L} L_{jl} \chi^{l}\right)\\
&- \frac{4 i}{L^{3}} L_{ik} \mathcal D_{a}\!\left(L^{jk}\right) \bar\varphi^{i} \gamma^{a} \gamma^{b} \mathcal D_{b}\!\left(\frac{1}{L} \gamma^{cd} T_{cd} \varphi_{j}\right)\\
&+\frac{2 i}{L^{3}} L_{ik} \mathcal D_{a}\!\left(L^{jk}\right) \bar\varphi^{i} \gamma^{a} \gamma^{b} \mathcal D_{b}\!\left(\frac{1}{L^{3}} L_{jl} \left(i \gamma^{c} E_{c} +N\right) \varphi^{l}\right)\\
&+\frac{2}{L^{3}} L_{ik} \mathcal D_{a}\!\left(L^{jk}\right) \bar\varphi^{i} \gamma^{a} \gamma^{b} \mathcal D_{b}\!\left(\frac{1}{L^{3}} \gamma^{c} \mathcal D_{c}\!\left(L_{jl}\right) L^{lm} \varphi_{m}\right)\\
&+\frac{4 i}{L^{2}} T_{bc} \mathcal D_{a}\!\left(\bar\varphi_{i}\right) \gamma^{a} \gamma^{bc} \gamma^{d} \mathcal D_{d}\!\left(\varphi^{i}\right)\\
&+\frac{32}{L^{2}} L^{ij} T_{bc} \mathcal D_{a}\!\left(\bar\varphi_{i}\right) \gamma^{a} \gamma^{bc} \chi_{j}\\
&- \frac{8}{L^{2}} T_{bc} T_{de} \mathcal D_{a}\!\left(\bar\varphi_{i}\right) \gamma^{a} \gamma^{bc} \gamma^{de} \varphi^{i}\\
&- \frac{4}{L^{4}} L^{ij} T_{bc} \mathcal D_{a}\!\left(\bar\varphi_{i}\right) \gamma^{a} \gamma^{bc} \left(i \gamma^{d} E_{d} +N\right) \varphi_{j}
\end{aligned}
\tag{SCF.11}
```

```math
\begin{aligned}
&+\frac{4 i}{L^{4}} L^{j}{}_{k} \mathcal D_{d}\!\left(L^{ik}\right) T_{bc} \mathcal D_{a}\!\left(\bar\varphi_{i}\right) \gamma^{a} \gamma^{bc} \gamma^{d} \varphi_{j}\\
&+\frac{32}{L^{2}} L_{i}{}^{j} T_{ab} \bar\chi^{i} \gamma^{ab} \gamma^{c} \mathcal D_{c}\!\left(\varphi_{j}\right)\\
&+128 i T_{ab} \bar\chi^{i} \gamma^{ab} \chi_{i}\\
&+\frac{64 i}{L^{2}} L_{i}{}^{j} T_{ab} T_{cd} \bar\chi^{i} \gamma^{ab} \gamma^{cd} \varphi_{j}\\
&- \frac{16 i}{L^{2}} T_{ab} \bar\chi^{i} \gamma^{ab} \left(i \gamma^{c} E_{c} +N\right) \varphi_{i}\\
&- \frac{32}{L^{4}} L_{ik} L^{j}{}_{l} \mathcal D_{c}\!\left(L^{kl}\right) T_{ab} \bar\chi^{i} \gamma^{ab} \gamma^{c} \varphi_{j}\\
&- \frac{8}{L^{2}} T_{ab} T_{cd} \bar\varphi^{i} \gamma^{ab} \gamma^{cd} \gamma^{e} \mathcal D_{e}\!\left(\varphi_{i}\right)\\
&+\frac{64 i}{L^{2}} L_{i}{}^{j} T_{ab} T_{cd} \bar\varphi^{i} \gamma^{ab} \gamma^{cd} \chi_{j}
\end{aligned}
\tag{SCF.12}
```

```math
\begin{aligned}
&- \frac{16 i}{L^{2}} T_{ab} T_{cd} T_{ef} \bar\varphi^{i} \gamma^{ab} \gamma^{cd} \gamma^{ef} \varphi_{i}\\
&- \frac{8 i}{L^{4}} L_{i}{}^{j} T_{ab} T_{cd} \bar\varphi^{i} \gamma^{ab} \gamma^{cd} \left(i \gamma^{e} E_{e} +N\right) \varphi_{j}\\
&- \frac{8}{L^{4}} L^{j}{}_{k} \mathcal D_{e}\!\left(L_{i}{}^{k}\right) T_{ab} T_{cd} \bar\varphi^{i} \gamma^{ab} \gamma^{cd} \gamma^{e} \varphi_{j}\\
&- \frac{4}{L^{4}} L_{i}{}^{j} T_{ab} \bar\varphi^{i} \left(i E_{d} \gamma^{d} +N\right) \gamma^{ab} \gamma^{c} \mathcal D_{c}\!\left(\varphi_{j}\right)\\
&- \frac{16 i}{L^{2}} T_{ab} \bar\varphi^{i} \left(i E_{c} \gamma^{c} +N\right) \gamma^{ab} \chi_{i}\\
&- \frac{8 i}{L^{4}} L_{i}{}^{j} T_{ab} T_{cd} \bar\varphi^{i} \left(i E_{e} \gamma^{e} +N\right) \gamma^{ab} \gamma^{cd} \varphi_{j}\\
&+\frac{2 i}{L^{4}} T_{ab} \bar\varphi^{i} \left(i E_{c} \gamma^{c} +N\right) \gamma^{ab} \left(i \gamma^{d} E_{d} +N\right) \varphi_{i}\\
&+\frac{4}{L^{6}} L_{ik} L^{j}{}_{l} \mathcal D_{c}\!\left(L^{kl}\right) T_{ab} \bar\varphi^{i} \left(i E_{d} \gamma^{d} +N\right) \gamma^{ab} \gamma^{c} \varphi_{j}
\end{aligned}
\tag{SCF.13}
```

```math
\begin{aligned}
&+\frac{4 i}{L^{4}} L_{ik} \mathcal D_{a}\!\left(L^{jk}\right) T_{bc} \bar\varphi^{i} \gamma^{a} \gamma^{bc} \gamma^{d} \mathcal D_{d}\!\left(\varphi_{j}\right)\\
&+\frac{32}{L^{4}} L_{ik} L^{j}{}_{l} \mathcal D_{a}\!\left(L^{lk}\right) T_{bc} \bar\varphi^{i} \gamma^{a} \gamma^{bc} \chi_{j}\\
&- \frac{8}{L^{4}} L_{ik} \mathcal D_{a}\!\left(L^{jk}\right) T_{bc} T_{de} \bar\varphi^{i} \gamma^{a} \gamma^{bc} \gamma^{de} \varphi_{j}\\
&- \frac{4}{L^{6}} L_{ik} L^{j}{}_{l} \mathcal D_{a}\!\left(L^{lk}\right) T_{bc} \bar\varphi^{i} \gamma^{a} \gamma^{bc} \left(i \gamma^{d} E_{d} +N\right) \varphi_{j}\\
&- \frac{4 i}{L^{6}} L_{ik} L^{j}{}_{l} \mathcal D_{a}\!\left(L_{m}{}^{k}\right) \mathcal D_{d}\!\left(L^{ml}\right) T_{bc} \bar\varphi^{i} \gamma^{a} \gamma^{bc} \gamma^{d} \varphi_{j}\\
&+4 g \mathcal D_{a}\!\left(\bar\varphi_{i}\right) \gamma^{a} \chi^{i}\\
&+\frac{64 N}{L^{2}} \mathcal D_{a}\!\left(\bar\varphi_{i}\right) \gamma^{a} \chi^{i}\\
&- 32 i g L_{i}{}^{j} \bar\chi^{i} \chi_{j}
\end{aligned}
\tag{SCF.14}
```

```math
\begin{aligned}
&- \frac{512 i N}{L^{2}} L_{i}{}^{j} \bar\chi^{i} \chi_{j}\\
&+8 i g T_{ab} \bar\varphi^{i} \gamma^{ab} \chi_{i}\\
&+\frac{128 i N}{L^{2}} T_{ab} \bar\varphi^{i} \gamma^{ab} \chi_{i}\\
&+\frac{4 i g}{L^{2}} L_{i}{}^{j} \bar\varphi^{i} \left(i E_{a} \gamma^{a} +N\right) \chi_{j}\\
&+\frac{64 i N}{L^{4}} L_{i}{}^{j} \bar\varphi^{i} \left(i E_{a} \gamma^{a} +N\right) \chi_{j}\\
&+\frac{4 g}{L^{2}} L_{ik} \mathcal D_{a}\!\left(L^{jk}\right) \bar\varphi^{i} \gamma^{a} \chi_{j}\\
&+\frac{64 N}{L^{4}} L_{ik} \mathcal D_{a}\!\left(L^{jk}\right) \bar\varphi^{i} \gamma^{a} \chi_{j}\\
&- \frac{i}{2 L^{2}} \widehat G_{bc} \mathcal D_{a}\!\left(\bar\varphi_{i}\right) \gamma^{a} \gamma^{bc} \gamma^{d} \mathcal D_{d}\!\left(\varphi^{i}\right)
\end{aligned}
\tag{SCF.15}
```

```math
\begin{aligned}
&- \frac{4}{L^{2}} \widehat G_{bc} L^{ij} \mathcal D_{a}\!\left(\bar\varphi_{i}\right) \gamma^{a} \gamma^{bc} \chi_{j}\\
&+\frac{1}{L^{2}} \widehat G_{bc} T_{de} \mathcal D_{a}\!\left(\bar\varphi_{i}\right) \gamma^{a} \gamma^{bc} \gamma^{de} \varphi^{i}\\
&+\frac{1}{2 L^{4}} \widehat G_{bc} L^{ij} \mathcal D_{a}\!\left(\bar\varphi_{i}\right) \gamma^{a} \gamma^{bc} \left(i \gamma^{d} E_{d} +N\right) \varphi_{j}\\
&- \frac{i}{2 L^{4}} \widehat G_{bc} L^{j}{}_{k} \mathcal D_{d}\!\left(L^{ik}\right) \mathcal D_{a}\!\left(\bar\varphi_{i}\right) \gamma^{a} \gamma^{bc} \gamma^{d} \varphi_{j}\\
&- \frac{4}{L^{2}} \widehat G_{ab} L_{i}{}^{j} \bar\chi^{i} \gamma^{ab} \gamma^{c} \mathcal D_{c}\!\left(\varphi_{j}\right)\\
&- 16 i \widehat G_{ab} \bar\chi^{i} \gamma^{ab} \chi_{i}\\
&- \frac{8 i}{L^{2}} \widehat G_{ab} L_{i}{}^{j} T_{cd} \bar\chi^{i} \gamma^{ab} \gamma^{cd} \varphi_{j}\\
&+\frac{2 i}{L^{2}} \widehat G_{ab} \bar\chi^{i} \gamma^{ab} \left(i \gamma^{c} E_{c} +N\right) \varphi_{i}
\end{aligned}
\tag{SCF.16}
```

```math
\begin{aligned}
&+\frac{4}{L^{4}} \widehat G_{ab} L_{ik} L^{j}{}_{l} \mathcal D_{c}\!\left(L^{kl}\right) \bar\chi^{i} \gamma^{ab} \gamma^{c} \varphi_{j}\\
&+\frac{1}{L^{2}} \widehat G_{cd} T_{ab} \bar\varphi^{i} \gamma^{ab} \gamma^{cd} \gamma^{e} \mathcal D_{e}\!\left(\varphi_{i}\right)\\
&- \frac{8 i}{L^{2}} \widehat G_{cd} L_{i}{}^{j} T_{ab} \bar\varphi^{i} \gamma^{ab} \gamma^{cd} \chi_{j}\\
&+\frac{2 i}{L^{2}} \widehat G_{cd} T_{ab} T_{ef} \bar\varphi^{i} \gamma^{ab} \gamma^{cd} \gamma^{ef} \varphi_{i}\\
&+\frac{i}{L^{4}} \widehat G_{cd} L_{i}{}^{j} T_{ab} \bar\varphi^{i} \gamma^{ab} \gamma^{cd} \left(i \gamma^{e} E_{e} +N\right) \varphi_{j}\\
&+\frac{1}{L^{4}} \widehat G_{cd} L^{j}{}_{k} \mathcal D_{e}\!\left(L_{i}{}^{k}\right) T_{ab} \bar\varphi^{i} \gamma^{ab} \gamma^{cd} \gamma^{e} \varphi_{j}\\
&+\frac{1}{2 L^{4}} \widehat G_{ab} L_{i}{}^{j} \bar\varphi^{i} \left(i E_{d} \gamma^{d} +N\right) \gamma^{ab} \gamma^{c} \mathcal D_{c}\!\left(\varphi_{j}\right)\\
&+\frac{2 i}{L^{2}} \widehat G_{ab} \bar\varphi^{i} \left(i E_{c} \gamma^{c} +N\right) \gamma^{ab} \chi_{i}
\end{aligned}
\tag{SCF.17}
```

```math
\begin{aligned}
&+\frac{i}{L^{4}} \widehat G_{ab} L_{i}{}^{j} T_{cd} \bar\varphi^{i} \left(i E_{e} \gamma^{e} +N\right) \gamma^{ab} \gamma^{cd} \varphi_{j}\\
&- \frac{i}{4 L^{4}} \widehat G_{ab} \bar\varphi^{i} \left(i E_{c} \gamma^{c} +N\right) \gamma^{ab} \left(i \gamma^{d} E_{d} +N\right) \varphi_{i}\\
&- \frac{1}{2 L^{6}} \widehat G_{ab} L_{ik} L^{j}{}_{l} \mathcal D_{c}\!\left(L^{kl}\right) \bar\varphi^{i} \left(i E_{d} \gamma^{d} +N\right) \gamma^{ab} \gamma^{c} \varphi_{j}\\
&- \frac{i}{2 L^{4}} \widehat G_{bc} L_{ik} \mathcal D_{a}\!\left(L^{jk}\right) \bar\varphi^{i} \gamma^{a} \gamma^{bc} \gamma^{d} \mathcal D_{d}\!\left(\varphi_{j}\right)\\
&- \frac{4}{L^{4}} \widehat G_{bc} L_{ik} L^{j}{}_{l} \mathcal D_{a}\!\left(L^{lk}\right) \bar\varphi^{i} \gamma^{a} \gamma^{bc} \chi_{j}\\
&+\frac{1}{L^{4}} \widehat G_{bc} L_{ik} \mathcal D_{a}\!\left(L^{jk}\right) T_{de} \bar\varphi^{i} \gamma^{a} \gamma^{bc} \gamma^{de} \varphi_{j}\\
&+\frac{1}{2 L^{6}} \widehat G_{bc} L_{ik} L^{j}{}_{l} \mathcal D_{a}\!\left(L^{lk}\right) \bar\varphi^{i} \gamma^{a} \gamma^{bc} \left(i \gamma^{d} E_{d} +N\right) \varphi_{j}\\
&+\frac{i}{2 L^{6}} \widehat G_{bc} L_{ik} L^{j}{}_{l} \mathcal D_{a}\!\left(L_{m}{}^{k}\right) \mathcal D_{d}\!\left(L^{ml}\right) \bar\varphi^{i} \gamma^{a} \gamma^{bc} \gamma^{d} \varphi_{j}
\end{aligned}
\tag{SCF.18}
```

```math
\begin{aligned}
&- \frac{i g}{L^{2}} L^{ij} \mathcal D_{a}\!\left(\bar\varphi_{i}\right) \gamma^{a} \gamma^{b} \mathcal D_{b}\!\left(\varphi_{j}\right)\\
&+\frac{2 g}{L^{2}} L^{ij} T_{bc} \mathcal D_{a}\!\left(\bar\varphi_{i}\right) \gamma^{a} \gamma^{bc} \varphi_{j}\\
&- \frac{g}{2 L^{2}} \mathcal D_{a}\!\left(\bar\varphi_{i}\right) \gamma^{a} \left(i \gamma^{b} E_{b} +N\right) \varphi^{i}\\
&+\frac{i g}{L^{4}} L^{i}{}_{k} L^{j}{}_{l} \mathcal D_{b}\!\left(L^{kl}\right) \mathcal D_{a}\!\left(\bar\varphi_{i}\right) \gamma^{a} \gamma^{b} \varphi_{j}\\
&+4 g \bar\chi^{i} \gamma^{a} \mathcal D_{a}\!\left(\varphi_{i}\right)\\
&+8 i g T_{ab} \bar\chi^{i} \gamma^{ab} \varphi_{i}\\
&+\frac{4 i g}{L^{2}} L_{i}{}^{j} \bar\chi^{i} \left(i \gamma^{a} E_{a} +N\right) \varphi_{j}\\
&+\frac{4 g}{L^{2}} L^{j}{}_{k} \mathcal D_{a}\!\left(L_{i}{}^{k}\right) \bar\chi^{i} \gamma^{a} \varphi_{j}
\end{aligned}
\tag{SCF.19}
```

```math
\begin{aligned}
&+\frac{2 g}{L^{2}} L_{i}{}^{j} T_{ab} \bar\varphi^{i} \gamma^{ab} \gamma^{c} \mathcal D_{c}\!\left(\varphi_{j}\right)\\
&+\frac{4 i g}{L^{2}} L_{i}{}^{j} T_{ab} T_{cd} \bar\varphi^{i} \gamma^{ab} \gamma^{cd} \varphi_{j}\\
&- \frac{i g}{L^{2}} T_{ab} \bar\varphi^{i} \gamma^{ab} \left(i \gamma^{c} E_{c} +N\right) \varphi_{i}\\
&- \frac{2 g}{L^{4}} L_{ik} L^{j}{}_{l} \mathcal D_{c}\!\left(L^{kl}\right) T_{ab} \bar\varphi^{i} \gamma^{ab} \gamma^{c} \varphi_{j}\\
&- \frac{g}{2 L^{2}} \bar\varphi^{i} \left(i E_{b} \gamma^{b} +N\right) \gamma^{a} \mathcal D_{a}\!\left(\varphi_{i}\right)\\
&- \frac{i g}{L^{2}} T_{ab} \bar\varphi^{i} \left(i E_{c} \gamma^{c} +N\right) \gamma^{ab} \varphi_{i}\\
&- \frac{i g}{2 L^{4}} L_{i}{}^{j} \bar\varphi^{i} \left(i E_{a} \gamma^{a} +N\right) \left(i \gamma^{b} E_{b} +N\right) \varphi_{j}\\
&- \frac{g}{2 L^{4}} L^{j}{}_{k} \mathcal D_{a}\!\left(L_{i}{}^{k}\right) \bar\varphi^{i} \left(i E_{b} \gamma^{b} +N\right) \gamma^{a} \varphi_{j}
\end{aligned}
\tag{SCF.20}
```

```math
\begin{aligned}
&- \frac{i g}{L^{4}} L_{ik} L^{j}{}_{l} \mathcal D_{a}\!\left(L^{lk}\right) \bar\varphi^{i} \gamma^{a} \gamma^{b} \mathcal D_{b}\!\left(\varphi_{j}\right)\\
&+\frac{2 g}{L^{4}} L_{ik} L^{j}{}_{l} \mathcal D_{a}\!\left(L^{lk}\right) T_{bc} \bar\varphi^{i} \gamma^{a} \gamma^{bc} \varphi_{j}\\
&- \frac{g}{2 L^{4}} L_{ik} \mathcal D_{a}\!\left(L^{jk}\right) \bar\varphi^{i} \gamma^{a} \left(i \gamma^{b} E_{b} +N\right) \varphi_{j}\\
&+\frac{i g}{L^{6}} L_{ik} L^{j}{}_{l} L_{mn} \mathcal D_{a}\!\left(L^{mk}\right) \mathcal D_{b}\!\left(L^{nl}\right) \bar\varphi^{i} \gamma^{a} \gamma^{b} \varphi_{j}\\
&+\frac{3 i N g}{2 L^{2}} L_{i}{}^{j} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{b} \mathcal D_{b}\!\left(\varphi_{j}\right)\\
&- 6 N g \bar\psi_{a}{}^{i} \gamma^{a} \chi_{i}\\
&- \frac{20 N^{2}}{L^{2}} \bar\psi_{a}{}^{i} \gamma^{a} \chi_{i}\\
&- \frac{3 N g}{L^{2}} L_{i}{}^{j} T_{bc} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{bc} \varphi_{j}
\end{aligned}
\tag{SCF.21}
```

```math
\begin{aligned}
&+\frac{3 N g}{4 L^{2}} \bar\psi_{a}{}^{i} \gamma^{a} \left(i \gamma^{b} E_{b} +N\right) \varphi_{i}\\
&- \frac{3 i N g}{2 L^{4}} L_{ik} L^{j}{}_{l} \mathcal D_{b}\!\left(L^{kl}\right) \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{b} \varphi_{j}\\
&- \frac{i}{L^{2}} \Box_c\!\left(L_{i}{}^{j}\right) \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{b} \mathcal D_{b}\!\left(\varphi_{j}\right)\\
&+\frac{i}{L^{3}} \mathcal D_{c}\!\left(L\right) \mathcal D^{c}\!\left(L_{i}{}^{j}\right) \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{b} \mathcal D_{b}\!\left(\varphi_{j}\right)\\
&- \frac{i}{L^{2}} \left(4 D +\frac{8}{3} T_{cd} T^{cd} - \frac{1}{L^{2}} E_{c} E^{c} - \frac{N^{2}}{L^{2}} +\frac{1}{2 L^{2}} \mathcal D_{c}\!\left(L_{kl}\right) \mathcal D^{c}\!\left(L^{kl}\right)\right) L_{i}{}^{j} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{b} \mathcal D_{b}\!\left(\varphi_{j}\right)\\
&- \frac{2 i}{L^{4}} E_{c} \varepsilon^{jk}\left(L_{l(i} \mathcal D^{c}\!\left(L_{k)}{}^{l}\right)\right) \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{b} \mathcal D_{b}\!\left(\varphi_{j}\right)\\
&- \frac{8}{L^{2}} L^{j}{}_{k} \Box_c\!\left(L_{i}{}^{k}\right) \bar\psi_{a}{}^{i} \gamma^{a} \chi_{j}\\
&+\frac{8}{L^{3}} L^{j}{}_{k} \mathcal D_{b}\!\left(L\right) \mathcal D^{b}\!\left(L_{i}{}^{k}\right) \bar\psi_{a}{}^{i} \gamma^{a} \chi_{j}
\end{aligned}
\tag{SCF.22}
```

```math
\begin{aligned}
&+4 \left(4 D +\frac{8}{3} T_{bc} T^{bc} - \frac{1}{L^{2}} E_{b} E^{b} - \frac{N^{2}}{L^{2}} +\frac{1}{2 L^{2}} \mathcal D_{b}\!\left(L_{jk}\right) \mathcal D^{b}\!\left(L^{jk}\right)\right) \bar\psi_{a}{}^{i} \gamma^{a} \chi_{i}\\
&+\frac{16}{L^{4}} E_{b} \left(L_{l(i} \mathcal D^{b}\!\left(L_{k)}{}^{l}\right)\right) L^{jk} \bar\psi_{a}{}^{i} \gamma^{a} \chi_{j}\\
&+\frac{2}{L^{2}} \Box_c\!\left(L_{i}{}^{j}\right) T_{bc} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{bc} \varphi_{j}\\
&- \frac{2}{L^{3}} \mathcal D_{d}\!\left(L\right) \mathcal D^{d}\!\left(L_{i}{}^{j}\right) T_{bc} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{bc} \varphi_{j}\\
&+\frac{2}{L^{2}} \left(4 D +\frac{8}{3} T_{de} T^{de} - \frac{1}{L^{2}} E_{d} E^{d} - \frac{N^{2}}{L^{2}} +\frac{1}{2 L^{2}} \mathcal D_{d}\!\left(L_{kl}\right) \mathcal D^{d}\!\left(L^{kl}\right)\right) L_{i}{}^{j} T_{bc} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{bc} \varphi_{j}\\
&+\frac{4}{L^{4}} E_{d} \varepsilon^{jk}\left(L_{l(i} \mathcal D^{d}\!\left(L_{k)}{}^{l}\right)\right) T_{bc} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{bc} \varphi_{j}\\
&+\frac{1}{L^{4}} L^{j}{}_{k} \Box_c\!\left(L_{i}{}^{k}\right) \bar\psi_{a}{}^{i} \gamma^{a} \left(i \gamma^{b} E_{b} +N\right) \varphi_{j}\\
&- \frac{1}{L^{5}} L^{j}{}_{k} \mathcal D_{b}\!\left(L\right) \mathcal D^{b}\!\left(L_{i}{}^{k}\right) \bar\psi_{a}{}^{i} \gamma^{a} \left(i \gamma^{c} E_{c} +N\right) \varphi_{j}
\end{aligned}
\tag{SCF.23}
```

```math
\begin{aligned}
&- \frac{1}{2 L^{2}} \left(4 D +\frac{8}{3} T_{bc} T^{bc} - \frac{1}{L^{2}} E_{b} E^{b} - \frac{N^{2}}{L^{2}} +\frac{1}{2 L^{2}} \mathcal D_{b}\!\left(L_{jk}\right) \mathcal D^{b}\!\left(L^{jk}\right)\right) \bar\psi_{a}{}^{i} \gamma^{a} \left(i \gamma^{d} E_{d} +N\right) \varphi_{i}\\
&- \frac{2}{L^{6}} E_{b} \left(L_{l(i} \mathcal D^{b}\!\left(L_{k)}{}^{l}\right)\right) L^{jk} \bar\psi_{a}{}^{i} \gamma^{a} \left(i \gamma^{c} E_{c} +N\right) \varphi_{j}\\
&+\frac{i}{L^{4}} L^{j}{}_{k} \Box_c\!\left(L_{il}\right) \mathcal D_{b}\!\left(L^{lk}\right) \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{b} \varphi_{j}\\
&+\frac{i}{L^{5}} L^{j}{}_{k} \mathcal D_{c}\!\left(L\right) \mathcal D_{b}\!\left(L_{l}{}^{k}\right) \mathcal D^{c}\!\left(L_{i}{}^{l}\right) \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{b} \varphi_{j}\\
&+\frac{i}{L^{4}} \left(4 D +\frac{8}{3} T_{cd} T^{cd} - \frac{1}{L^{2}} E_{c} E^{c} - \frac{N^{2}}{L^{2}} +\frac{1}{2 L^{2}} \mathcal D_{c}\!\left(L_{mn}\right) \mathcal D^{c}\!\left(L^{mn}\right)\right) L_{ik} L^{j}{}_{l} \mathcal D_{b}\!\left(L^{kl}\right) \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{b} \varphi_{j}\\
&+\frac{2 i}{L^{6}} E_{c} \left(L_{m(i} \mathcal D^{c}\!\left(L_{k)}{}^{m}\right)\right) L^{j}{}_{l} \mathcal D_{b}\!\left(L^{kl}\right) \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{b} \varphi_{j}\\
&- \frac{3 i N}{4 L^{2}} \widehat G_{cd} \mathcal D_{a}\!\left(\bar\varphi_{i}\right) \gamma^{a} \gamma^{b} \gamma^{cd} \psi_{b}{}^{i}\\
&- \frac{6 N}{L^{2}} \widehat G_{bc} L_{i}{}^{j} \bar\chi^{i} \gamma^{a} \gamma^{bc} \psi_{aj}
\end{aligned}
\tag{SCF.24}
```

```math
\begin{aligned}
&+\frac{3 N}{2 L^{2}} \widehat G_{de} T_{ab} \bar\varphi^{i} \gamma^{ab} \gamma^{c} \gamma^{de} \psi_{ci}\\
&+\frac{3 N}{4 L^{4}} \widehat G_{bc} L_{i}{}^{j} \bar\varphi^{i} \left(i E_{d} \gamma^{d} +N\right) \gamma^{a} \gamma^{bc} \psi_{aj}\\
&- \frac{3 i N}{4 L^{4}} \widehat G_{cd} L_{ik} \mathcal D_{a}\!\left(L^{jk}\right) \bar\varphi^{i} \gamma^{a} \gamma^{b} \gamma^{cd} \psi_{bj}\\
&+\frac{3 i N}{L^{2}} T_{cd} \mathcal D_{a}\!\left(\bar\varphi_{i}\right) \gamma^{a} \gamma^{b} \gamma^{cd} \psi_{b}{}^{i}\\
&+\frac{24 N}{L^{2}} L_{i}{}^{j} T_{bc} \bar\chi^{i} \gamma^{a} \gamma^{bc} \psi_{aj}\\
&- \frac{6 N}{L^{2}} T_{ab} T_{de} \bar\varphi^{i} \gamma^{ab} \gamma^{c} \gamma^{de} \psi_{ci}\\
&- \frac{3 N}{L^{4}} L_{i}{}^{j} T_{bc} \bar\varphi^{i} \left(i E_{d} \gamma^{d} +N\right) \gamma^{a} \gamma^{bc} \psi_{aj}\\
&+\frac{3 i N}{L^{4}} L_{ik} \mathcal D_{a}\!\left(L^{jk}\right) T_{cd} \bar\varphi^{i} \gamma^{a} \gamma^{b} \gamma^{cd} \psi_{bj}
\end{aligned}
\tag{SCF.25}
```

```math
\begin{aligned}
&+\frac{3 i N g}{2 L^{2}} L^{ij} \mathcal D_{a}\!\left(\bar\varphi_{i}\right) \gamma^{a} \gamma^{b} \psi_{bj}\\
&- 6 N g \bar\chi^{i} \gamma^{a} \psi_{ai}\\
&- \frac{3 N g}{L^{2}} L_{i}{}^{j} T_{ab} \bar\varphi^{i} \gamma^{ab} \gamma^{c} \psi_{cj}\\
&+\frac{3 N g}{4 L^{2}} \bar\varphi^{i} \left(i E_{b} \gamma^{b} +N\right) \gamma^{a} \psi_{ai}\\
&+\frac{3 i N g}{2 L^{4}} L_{ik} L^{j}{}_{l} \mathcal D_{a}\!\left(L^{lk}\right) \bar\varphi^{i} \gamma^{a} \gamma^{b} \psi_{bj}\\
&+\frac{3 i N}{L^{2}} \mathcal D_{a}\!\left(\bar\varphi_{i}\right) \gamma^{a} \gamma^{b} \phi_{b}{}^{i}\\
&+\frac{24 N}{L^{2}} L_{i}{}^{j} \bar\chi^{i} \gamma^{a} \phi_{aj}\\
&- \frac{6 N}{L^{2}} T_{ab} \bar\varphi^{i} \gamma^{ab} \gamma^{c} \phi_{ci}
\end{aligned}
\tag{SCF.26}
```

```math
\begin{aligned}
&- \frac{3 N}{L^{4}} L_{i}{}^{j} \bar\varphi^{i} \left(i E_{b} \gamma^{b} +N\right) \gamma^{a} \phi_{aj}\\
&+\frac{3 i N}{L^{4}} L_{ik} \mathcal D_{a}\!\left(L^{jk}\right) \bar\varphi^{i} \gamma^{a} \gamma^{b} \phi_{bj}\\
&- \frac{1}{L} E_{a} \mathcal D_{b}\!\left(\left(4 \left(\mathcal D^{[a}\!\left(\frac{1}{L} E^{b]}\right)\right) +\frac{2}{L} L_{ij} \widehat R(V)^{abij} - \frac{2}{L^{3}} L_{i}{}^{j} \left(\mathcal D^{[a}\!\left(L^{ik}\right) \mathcal D^{b]}\!\left(L_{jk}\right)\right) +\frac{2 N}{L} \left(\widehat G^{ab} -16 T^{ab}\right)\right)\right)\\
&- \frac{1}{L} E^{b} \mathcal D_{a}\!\left(\left(-2 \eta^{ac}\left(\mathcal D_{[b}\!\left(\frac{1}{L^{3}} L_{mn} \bar\varphi^{m} \gamma_{c]} \varphi^{n}\right)\right) - \frac{i}{L} \bar\varphi^{i} \widehat R(Q)_{b}{}^{a}{}_{i} +\frac{i}{L^{3}} L_{ij} \bar\varphi^{i} \varphi^{j} \left(\widehat G_{b}{}^{a} -16 T_{b}{}^{a}\right)\right)\right)\\
&- \frac{\sqrt{2}}{2} \mathcal D_{a}\!\left(\left(4 \eta^{ac}\left(\mathcal D_{[b}\!\left(\frac{1}{L} E_{c]}\right)\right) +\frac{2}{L} L_{ij} \widehat R(V)_{b}{}^{aij} - \frac{2}{L^{3}} L_{i}{}^{j} \eta^{ad}\left(\mathcal D_{[b}\!\left(L^{ik}\right) \mathcal D_{d]}\!\left(L_{jk}\right)\right) +\frac{2 N}{L} \left(\widehat G_{b}{}^{a} -16 T_{b}{}^{a}\right)\right)\right) V^{b}\\
&- \frac{\sqrt{2}}{2} V^{b} \mathcal D_{a}\!\left(\left(-2 \eta^{ac}\left(\mathcal D_{[b}\!\left(\frac{1}{L^{3}} L_{mn} \bar\varphi^{m} \gamma_{c]} \varphi^{n}\right)\right) - \frac{i}{L} \bar\varphi^{i} \widehat R(Q)_{b}{}^{a}{}_{i} +\frac{i}{L^{3}} L_{ij} \bar\varphi^{i} \varphi^{j} \left(\widehat G_{b}{}^{a} -16 T_{b}{}^{a}\right)\right)\right)\\
&- \frac{1}{2 L^{3}} L_{i}{}^{j} \mathcal D_{b}\!\left(\left(4 \eta^{bc}\left(\mathcal D_{[a}\!\left(\frac{1}{L} E_{c]}\right)\right) +\frac{2}{L} L_{kl} \widehat R(V)_{a}{}^{bkl} - \frac{2}{L^{3}} L_{k}{}^{l} \eta^{bd}\left(\mathcal D_{[a}\!\left(L^{km}\right) \mathcal D_{d]}\!\left(L_{lm}\right)\right) +\frac{2 N}{L} \left(\widehat G_{a}{}^{b} -16 T_{a}{}^{b}\right)\right)\right) \bar\varphi^{i} \gamma^{a} \varphi_{j}\\
&+\frac{i}{2 L} \mathcal D_{b}\!\left(\left(4 \left(\mathcal D^{[a}\!\left(\frac{1}{L} E^{b]}\right)\right) +\frac{2}{L} L_{jk} \widehat R(V)^{abjk} - \frac{2}{L^{3}} L_{j}{}^{k} \left(\mathcal D^{[a}\!\left(L^{jl}\right) \mathcal D^{b]}\!\left(L_{kl}\right)\right) +\frac{2 N}{L} \left(\widehat G^{ab} -16 T^{ab}\right)\right)\right) \bar\varphi^{i} \psi_{ai}
\end{aligned}
\tag{SCF.27}
```

```math
\begin{aligned}
&- \frac{1}{L} E_{a} \widehat G_{bc} \left(\mathcal D_{[d}\!\left(\frac{1}{L} E_{e]}\right)\right) \varepsilon^{abcde}\\
&- \frac{1}{2 L^{2}} E_{a} \widehat G_{bc} L_{ij} \widehat R(V)_{de}{}^{ij} \varepsilon^{abcde}\\
&- \frac{1}{2 L^{4}} E_{a} \widehat G_{bc} \left(\mathcal D_{[d}\!\left(L_{i}{}^{k}\right) \mathcal D_{e]}\!\left(L_{jk}\right)\right) L^{ij} \varepsilon^{abcde}\\
&+\frac{1}{2 L} E_{c} \widehat G_{de} \varepsilon^{abcde} \left(\mathcal D_{[a}\!\left(\frac{1}{L^{3}} L_{kl} \bar\varphi^{k} \gamma_{b]} \varphi^{l}\right)\right)\\
&+\frac{i}{4 L^{2}} E_{c} \widehat G_{de} \varepsilon^{abcde} \bar\varphi^{i} \widehat R(Q)_{abi}\\
&- \frac{\sqrt{2}}{2} \widehat G_{ab} \left(\mathcal D_{[c}\!\left(\frac{1}{L} E_{d]}\right)\right) V_{e} \varepsilon^{abcde}\\
&- \frac{\sqrt{2}}{4 L} \widehat G_{ab} L_{ij} \widehat R(V)_{cd}{}^{ij} V_{e} \varepsilon^{abcde}\\
&- \frac{\sqrt{2}}{4 L^{3}} \widehat G_{ab} \left(\mathcal D_{[c}\!\left(L_{i}{}^{k}\right) \mathcal D_{d]}\!\left(L_{jk}\right)\right) L^{ij} V_{e} \varepsilon^{abcde}
\end{aligned}
\tag{SCF.28}
```

```math
\begin{aligned}
&+\frac{\sqrt{2}}{4} \widehat G_{cd} V_{e} \varepsilon^{abcde} \left(\mathcal D_{[a}\!\left(\frac{1}{L^{3}} L_{kl} \bar\varphi^{k} \gamma_{b]} \varphi^{l}\right)\right)\\
&+\frac{\sqrt{2} i}{8 L} \widehat G_{cd} V_{e} \varepsilon^{abcde} \bar\varphi^{i} \widehat R(Q)_{abi}\\
&- \frac{1}{2 L^{3}} \widehat G_{bc} \left(\mathcal D_{[d}\!\left(\frac{1}{L} E_{e]}\right)\right) L_{i}{}^{j} \varepsilon_{a}{}^{bcde} \bar\varphi^{i} \gamma^{a} \varphi_{j}\\
&- \frac{1}{4 L^{4}} \widehat G_{bc} L_{i}{}^{j} L_{kl} \widehat R(V)_{de}{}^{kl} \varepsilon_{a}{}^{bcde} \bar\varphi^{i} \gamma^{a} \varphi_{j}\\
&- \frac{1}{4 L^{6}} \widehat G_{bc} \left(\mathcal D_{[d}\!\left(L_{k}{}^{m}\right) \mathcal D_{e]}\!\left(L_{lm}\right)\right) L_{i}{}^{j} L^{kl} \varepsilon_{a}{}^{bcde} \bar\varphi^{i} \gamma^{a} \varphi_{j}\\
&+\frac{i}{2 L} \widehat G_{bc} \left(\mathcal D_{[d}\!\left(\frac{1}{L} E_{e]}\right)\right) \varepsilon^{abcde} \bar\varphi^{i} \psi_{ai}\\
&+\frac{i}{4 L^{2}} \widehat G_{bc} L_{jk} \widehat R(V)_{de}{}^{jk} \varepsilon^{abcde} \bar\varphi^{i} \psi_{ai}\\
&+\frac{i}{4 L^{4}} \widehat G_{bc} \left(\mathcal D_{[d}\!\left(L_{j}{}^{l}\right) \mathcal D_{e]}\!\left(L_{kl}\right)\right) L^{jk} \varepsilon^{abcde} \bar\varphi^{i} \psi_{ai}
\end{aligned}
\tag{SCF.29}
```

```math
\begin{aligned}
&+\frac{1}{4 L^{2}} E_{b} \widehat G_{de} \mathcal D_{a}\!\left(\bar\varphi_{i}\right) \gamma^{a} \gamma^{bc} \gamma^{de} \psi_{c}{}^{i}\\
&- \frac{2 i}{L^{2}} E_{a} \widehat G_{cd} L_{i}{}^{j} \bar\chi^{i} \gamma^{ab} \gamma^{cd} \psi_{bj}\\
&+\frac{i}{2 L^{2}} E_{c} \widehat G_{ef} T_{ab} \bar\varphi^{i} \gamma^{ab} \gamma^{cd} \gamma^{ef} \psi_{di}\\
&+\frac{i}{4 L^{4}} E_{a} \widehat G_{cd} L_{i}{}^{j} \bar\varphi^{i} \left(i E_{e} \gamma^{e} +N\right) \gamma^{ab} \gamma^{cd} \psi_{bj}\\
&+\frac{1}{4 L^{4}} E_{b} \widehat G_{de} L_{ik} \mathcal D_{a}\!\left(L^{jk}\right) \bar\varphi^{i} \gamma^{a} \gamma^{bc} \gamma^{de} \psi_{cj}\\
&+\frac{\sqrt{2}}{8 L} \widehat G_{de} V_{b} \mathcal D_{a}\!\left(\bar\varphi_{i}\right) \gamma^{a} \gamma^{bc} \gamma^{de} \psi_{c}{}^{i}\\
&- \frac{\sqrt{2} i}{L} \widehat G_{cd} L_{i}{}^{j} V_{a} \bar\chi^{i} \gamma^{ab} \gamma^{cd} \psi_{bj}\\
&+\frac{\sqrt{2} i}{4 L} \widehat G_{ef} T_{ab} V_{c} \bar\varphi^{i} \gamma^{ab} \gamma^{cd} \gamma^{ef} \psi_{di}
\end{aligned}
\tag{SCF.30}
```

```math
\begin{aligned}
&+\frac{\sqrt{2} i}{8 L^{3}} \widehat G_{cd} L_{i}{}^{j} V_{a} \bar\varphi^{i} \left(i E_{e} \gamma^{e} +N\right) \gamma^{ab} \gamma^{cd} \psi_{bj}\\
&+\frac{\sqrt{2}}{8 L^{3}} \widehat G_{de} L_{ik} \mathcal D_{a}\!\left(L^{jk}\right) V_{b} \bar\varphi^{i} \gamma^{a} \gamma^{bc} \gamma^{de} \psi_{cj}\\
&- \frac{1}{L^{2}} E_{b} T_{de} \mathcal D_{a}\!\left(\bar\varphi_{i}\right) \gamma^{a} \gamma^{bc} \gamma^{de} \psi_{c}{}^{i}\\
&+\frac{8 i}{L^{2}} E_{a} L_{i}{}^{j} T_{cd} \bar\chi^{i} \gamma^{ab} \gamma^{cd} \psi_{bj}\\
&- \frac{2 i}{L^{2}} E_{c} T_{ab} T_{ef} \bar\varphi^{i} \gamma^{ab} \gamma^{cd} \gamma^{ef} \psi_{di}\\
&- \frac{i}{L^{4}} E_{a} L_{i}{}^{j} T_{cd} \bar\varphi^{i} \left(i E_{e} \gamma^{e} +N\right) \gamma^{ab} \gamma^{cd} \psi_{bj}\\
&- \frac{1}{L^{4}} E_{b} L_{ik} \mathcal D_{a}\!\left(L^{jk}\right) T_{de} \bar\varphi^{i} \gamma^{a} \gamma^{bc} \gamma^{de} \psi_{cj}\\
&- \frac{\sqrt{2}}{2 L} T_{de} V_{b} \mathcal D_{a}\!\left(\bar\varphi_{i}\right) \gamma^{a} \gamma^{bc} \gamma^{de} \psi_{c}{}^{i}
\end{aligned}
\tag{SCF.31}
```

```math
\begin{aligned}
&+\frac{4 \sqrt{2} i}{L} L_{i}{}^{j} T_{cd} V_{a} \bar\chi^{i} \gamma^{ab} \gamma^{cd} \psi_{bj}\\
&- \frac{\sqrt{2} i}{L} T_{ab} T_{ef} V_{c} \bar\varphi^{i} \gamma^{ab} \gamma^{cd} \gamma^{ef} \psi_{di}\\
&- \frac{\sqrt{2} i}{2 L^{3}} L_{i}{}^{j} T_{cd} V_{a} \bar\varphi^{i} \left(i E_{e} \gamma^{e} +N\right) \gamma^{ab} \gamma^{cd} \psi_{bj}\\
&- \frac{\sqrt{2}}{2 L^{3}} L_{ik} \mathcal D_{a}\!\left(L^{jk}\right) T_{de} V_{b} \bar\varphi^{i} \gamma^{a} \gamma^{bc} \gamma^{de} \psi_{cj}\\
&- \frac{g}{2 L^{2}} E_{b} L^{ij} \mathcal D_{a}\!\left(\bar\varphi_{i}\right) \gamma^{a} \gamma^{bc} \psi_{cj}\\
&- 2 i g E_{a} \bar\chi^{i} \gamma^{ab} \psi_{bi}\\
&- \frac{i g}{L^{2}} E_{c} L_{i}{}^{j} T_{ab} \bar\varphi^{i} \gamma^{ab} \gamma^{cd} \psi_{dj}\\
&+\frac{i g}{4 L^{2}} E_{a} \bar\varphi^{i} \left(i E_{c} \gamma^{c} +N\right) \gamma^{ab} \psi_{bi}
\end{aligned}
\tag{SCF.32}
```

```math
\begin{aligned}
&- \frac{g}{2 L^{4}} E_{b} L_{ik} L^{j}{}_{l} \mathcal D_{a}\!\left(L^{lk}\right) \bar\varphi^{i} \gamma^{a} \gamma^{bc} \psi_{cj}\\
&- \frac{\sqrt{2} g}{4 L} L^{ij} V_{b} \mathcal D_{a}\!\left(\bar\varphi_{i}\right) \gamma^{a} \gamma^{bc} \psi_{cj}\\
&- \sqrt{2} i L g V_{a} \bar\chi^{i} \gamma^{ab} \psi_{bi}\\
&- \frac{\sqrt{2} i g}{2 L} L_{i}{}^{j} T_{ab} V_{c} \bar\varphi^{i} \gamma^{ab} \gamma^{cd} \psi_{dj}\\
&+\frac{\sqrt{2} i g}{8 L} V_{a} \bar\varphi^{i} \left(i E_{c} \gamma^{c} +N\right) \gamma^{ab} \psi_{bi}\\
&- \frac{\sqrt{2} g}{4 L^{3}} L_{ik} L^{j}{}_{l} \mathcal D_{a}\!\left(L^{lk}\right) V_{b} \bar\varphi^{i} \gamma^{a} \gamma^{bc} \psi_{cj}\\
&- \frac{1}{L^{2}} E_{b} \mathcal D_{a}\!\left(\bar\varphi_{i}\right) \gamma^{a} \gamma^{bc} \phi_{c}{}^{i}\\
&+\frac{8 i}{L^{2}} E_{a} L_{i}{}^{j} \bar\chi^{i} \gamma^{ab} \phi_{bj}
\end{aligned}
\tag{SCF.33}
```

```math
\begin{aligned}
&- \frac{2 i}{L^{2}} E_{c} T_{ab} \bar\varphi^{i} \gamma^{ab} \gamma^{cd} \phi_{di}\\
&- \frac{i}{L^{4}} E_{a} L_{i}{}^{j} \bar\varphi^{i} \left(i E_{c} \gamma^{c} +N\right) \gamma^{ab} \phi_{bj}\\
&- \frac{1}{L^{4}} E_{b} L_{ik} \mathcal D_{a}\!\left(L^{jk}\right) \bar\varphi^{i} \gamma^{a} \gamma^{bc} \phi_{cj}\\
&- \frac{\sqrt{2}}{2 L} V_{b} \mathcal D_{a}\!\left(\bar\varphi_{i}\right) \gamma^{a} \gamma^{bc} \phi_{c}{}^{i}\\
&+\frac{4 \sqrt{2} i}{L} L_{i}{}^{j} V_{a} \bar\chi^{i} \gamma^{ab} \phi_{bj}\\
&- \frac{\sqrt{2} i}{L} T_{ab} V_{c} \bar\varphi^{i} \gamma^{ab} \gamma^{cd} \phi_{di}\\
&- \frac{\sqrt{2} i}{2 L^{3}} L_{i}{}^{j} V_{a} \bar\varphi^{i} \left(i E_{c} \gamma^{c} +N\right) \gamma^{ab} \phi_{bj}\\
&- \frac{\sqrt{2}}{2 L^{3}} L_{ik} \mathcal D_{a}\!\left(L^{jk}\right) V_{b} \bar\varphi^{i} \gamma^{a} \gamma^{bc} \phi_{cj}
\end{aligned}
\tag{SCF.34}
```

```math
\begin{aligned}
&- \frac{N}{4 L^{2}} E_{b} \widehat G_{de} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{c} \gamma^{de} \psi_{ci}\\
&- \frac{\sqrt{2} N}{8 L} \widehat G_{de} V_{b} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{c} \gamma^{de} \psi_{ci}\\
&+\frac{N}{L^{2}} E_{b} T_{de} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{c} \gamma^{de} \psi_{ci}\\
&+\frac{\sqrt{2} N}{2 L} T_{de} V_{b} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{c} \gamma^{de} \psi_{ci}\\
&+\frac{N g}{2 L^{2}} E_{b} L_{i}{}^{j} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{c} \psi_{cj}\\
&+\frac{\sqrt{2} N g}{4 L} L_{i}{}^{j} V_{b} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{c} \psi_{cj}\\
&+\frac{N}{L^{2}} E_{b} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{c} \phi_{ci}\\
&+\frac{\sqrt{2} N}{2 L} V_{b} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{c} \phi_{ci}
\end{aligned}
\tag{SCF.35}
```

```math
\begin{aligned}
&+\frac{i}{L} E_{b} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{c} \mathcal D_{c}\!\left(\frac{1}{L} \gamma^{d} \mathcal D_{d}\!\left(\varphi_{i}\right)\right)\\
&- \frac{8}{L} E_{b} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{c} \mathcal D_{c}\!\left(\frac{1}{L} L_{ij} \chi^{j}\right)\\
&- \frac{2}{L} E_{b} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{c} \mathcal D_{c}\!\left(\frac{1}{L} \gamma^{de} T_{de} \varphi_{i}\right)\\
&+\frac{1}{L} E_{b} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{c} \mathcal D_{c}\!\left(\frac{1}{L^{3}} L_{ij} \left(i \gamma^{d} E_{d} +N\right) \varphi^{j}\right)\\
&- \frac{i}{L} E_{b} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{c} \mathcal D_{c}\!\left(\frac{1}{L^{3}} \gamma^{d} \mathcal D_{d}\!\left(L_{ij}\right) L^{jk} \varphi_{k}\right)\\
&+\frac{\sqrt{2} i}{2} V_{b} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{c} \mathcal D_{c}\!\left(\frac{1}{L} \gamma^{d} \mathcal D_{d}\!\left(\varphi_{i}\right)\right)\\
&- 4 \sqrt{2} V_{b} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{c} \mathcal D_{c}\!\left(\frac{1}{L} L_{ij} \chi^{j}\right)\\
&- \sqrt{2} V_{b} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{c} \mathcal D_{c}\!\left(\frac{1}{L} \gamma^{de} T_{de} \varphi_{i}\right)
\end{aligned}
\tag{SCF.36}
```

```math
\begin{aligned}
&+\frac{\sqrt{2}}{2} V_{b} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{c} \mathcal D_{c}\!\left(\frac{1}{L^{3}} L_{ij} \left(i \gamma^{d} E_{d} +N\right) \varphi^{j}\right)\\
&- \frac{\sqrt{2} i}{2} V_{b} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{c} \mathcal D_{c}\!\left(\frac{1}{L^{3}} \gamma^{d} \mathcal D_{d}\!\left(L_{ij}\right) L^{jk} \varphi_{k}\right)\\
&+\frac{2}{L^{2}} E_{b} T_{cd} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{cd} \gamma^{e} \mathcal D_{e}\!\left(\varphi_{i}\right)\\
&- \frac{16 i}{L^{2}} E_{b} L_{i}{}^{j} T_{cd} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{cd} \chi_{j}\\
&+\frac{4 i}{L^{2}} E_{b} T_{cd} T_{ef} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{cd} \gamma^{ef} \varphi_{i}\\
&+\frac{2 i}{L^{4}} E_{b} L_{i}{}^{j} T_{cd} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{cd} \left(i \gamma^{e} E_{e} +N\right) \varphi_{j}\\
&+\frac{2}{L^{4}} E_{b} L^{j}{}_{k} \mathcal D_{e}\!\left(L_{i}{}^{k}\right) T_{cd} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{cd} \gamma^{e} \varphi_{j}\\
&+\frac{\sqrt{2}}{L} T_{cd} V_{b} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{cd} \gamma^{e} \mathcal D_{e}\!\left(\varphi_{i}\right)
\end{aligned}
\tag{SCF.37}
```

```math
\begin{aligned}
&- \frac{8 \sqrt{2} i}{L} L_{i}{}^{j} T_{cd} V_{b} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{cd} \chi_{j}\\
&+\frac{2 \sqrt{2} i}{L} T_{cd} T_{ef} V_{b} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{cd} \gamma^{ef} \varphi_{i}\\
&+\frac{\sqrt{2} i}{L^{3}} L_{i}{}^{j} T_{cd} V_{b} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{cd} \left(i \gamma^{e} E_{e} +N\right) \varphi_{j}\\
&+\frac{\sqrt{2}}{L^{3}} L^{j}{}_{k} \mathcal D_{e}\!\left(L_{i}{}^{k}\right) T_{cd} V_{b} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{cd} \gamma^{e} \varphi_{j}\\
&- 2 i g E_{b} \bar\psi_{a}{}^{i} \gamma^{ab} \chi_{i}\\
&- \frac{16 i N}{L^{2}} E_{b} \bar\psi_{a}{}^{i} \gamma^{ab} \chi_{i}\\
&- \sqrt{2} i L g V_{b} \bar\psi_{a}{}^{i} \gamma^{ab} \chi_{i}\\
&- \frac{8 \sqrt{2} i N}{L} V_{b} \bar\psi_{a}{}^{i} \gamma^{ab} \chi_{i}
\end{aligned}
\tag{SCF.38}
```

```math
\begin{aligned}
&- \frac{1}{4 L^{2}} E_{b} \widehat G_{cd} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{cd} \gamma^{e} \mathcal D_{e}\!\left(\varphi_{i}\right)\\
&+\frac{2 i}{L^{2}} E_{b} \widehat G_{cd} L_{i}{}^{j} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{cd} \chi_{j}\\
&- \frac{i}{2 L^{2}} E_{b} \widehat G_{cd} T_{ef} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{cd} \gamma^{ef} \varphi_{i}\\
&- \frac{i}{4 L^{4}} E_{b} \widehat G_{cd} L_{i}{}^{j} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{cd} \left(i \gamma^{e} E_{e} +N\right) \varphi_{j}\\
&- \frac{1}{4 L^{4}} E_{b} \widehat G_{cd} L^{j}{}_{k} \mathcal D_{e}\!\left(L_{i}{}^{k}\right) \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{cd} \gamma^{e} \varphi_{j}\\
&- \frac{\sqrt{2}}{8 L} \widehat G_{cd} V_{b} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{cd} \gamma^{e} \mathcal D_{e}\!\left(\varphi_{i}\right)\\
&+\frac{\sqrt{2} i}{L} \widehat G_{cd} L_{i}{}^{j} V_{b} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{cd} \chi_{j}\\
&- \frac{\sqrt{2} i}{4 L} \widehat G_{cd} T_{ef} V_{b} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{cd} \gamma^{ef} \varphi_{i}
\end{aligned}
\tag{SCF.39}
```

```math
\begin{aligned}
&- \frac{\sqrt{2} i}{8 L^{3}} \widehat G_{cd} L_{i}{}^{j} V_{b} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{cd} \left(i \gamma^{e} E_{e} +N\right) \varphi_{j}\\
&- \frac{\sqrt{2}}{8 L^{3}} \widehat G_{cd} L^{j}{}_{k} \mathcal D_{e}\!\left(L_{i}{}^{k}\right) V_{b} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{cd} \gamma^{e} \varphi_{j}\\
&- \frac{g}{2 L^{2}} E_{b} L_{i}{}^{j} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{c} \mathcal D_{c}\!\left(\varphi_{j}\right)\\
&- \frac{i g}{L^{2}} E_{b} L_{i}{}^{j} T_{cd} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{cd} \varphi_{j}\\
&+\frac{i g}{4 L^{2}} E_{b} \bar\psi_{a}{}^{i} \gamma^{ab} \left(i \gamma^{c} E_{c} +N\right) \varphi_{i}\\
&+\frac{g}{2 L^{4}} E_{b} L_{ik} L^{j}{}_{l} \mathcal D_{c}\!\left(L^{kl}\right) \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{c} \varphi_{j}\\
&- \frac{\sqrt{2} g}{4 L} L_{i}{}^{j} V_{b} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{c} \mathcal D_{c}\!\left(\varphi_{j}\right)\\
&- \frac{\sqrt{2} i g}{2 L} L_{i}{}^{j} T_{cd} V_{b} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{cd} \varphi_{j}
\end{aligned}
\tag{SCF.40}
```

```math
\begin{aligned}
&+\frac{\sqrt{2} i g}{8 L} V_{b} \bar\psi_{a}{}^{i} \gamma^{ab} \left(i \gamma^{c} E_{c} +N\right) \varphi_{i}\\
&+\frac{\sqrt{2} g}{4 L^{3}} L_{ik} L^{j}{}_{l} \mathcal D_{c}\!\left(L^{kl}\right) V_{b} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{c} \varphi_{j}\\
&- \frac{N g}{2 L^{2}} E_{b} L_{i}{}^{j} \bar\psi_{a}{}^{i} \gamma^{abc} \psi_{cj}\\
&- \frac{\sqrt{2} N g}{4 L} L_{i}{}^{j} V_{b} \bar\psi_{a}{}^{i} \gamma^{abc} \psi_{cj}\\
&+\frac{1}{2 L^{2}} E_{b} \Box_c\!\left(L_{i}{}^{j}\right) \bar\psi_{a}{}^{i} \gamma^{abc} \psi_{cj}\\
&- \frac{1}{2 L^{3}} E_{b} \mathcal D_{d}\!\left(L\right) \mathcal D^{d}\!\left(L_{i}{}^{j}\right) \bar\psi_{a}{}^{i} \gamma^{abc} \psi_{cj}\\
&+\frac{1}{2 L^{2}} E_{b} \left(4 D +\frac{8}{3} T_{de} T^{de} - \frac{1}{L^{2}} E_{d} E^{d} - \frac{N^{2}}{L^{2}} +\frac{1}{2 L^{2}} \mathcal D_{d}\!\left(L_{kl}\right) \mathcal D^{d}\!\left(L^{kl}\right)\right) L_{i}{}^{j} \bar\psi_{a}{}^{i} \gamma^{abc} \psi_{cj}\\
&+\frac{1}{L^{4}} E_{b} E_{d} \varepsilon^{jk}\left(L_{l(i} \mathcal D^{d}\!\left(L_{k)}{}^{l}\right)\right) \bar\psi_{a}{}^{i} \gamma^{abc} \psi_{cj}
\end{aligned}
\tag{SCF.41}
```

```math
\begin{aligned}
&+\frac{\sqrt{2}}{4 L} \Box_c\!\left(L_{i}{}^{j}\right) V_{b} \bar\psi_{a}{}^{i} \gamma^{abc} \psi_{cj}\\
&- \frac{\sqrt{2}}{4 L^{2}} \mathcal D_{d}\!\left(L\right) \mathcal D^{d}\!\left(L_{i}{}^{j}\right) V_{b} \bar\psi_{a}{}^{i} \gamma^{abc} \psi_{cj}\\
&+\frac{\sqrt{2}}{4 L} \left(4 D +\frac{8}{3} T_{de} T^{de} - \frac{1}{L^{2}} E_{d} E^{d} - \frac{N^{2}}{L^{2}} +\frac{1}{2 L^{2}} \mathcal D_{d}\!\left(L_{kl}\right) \mathcal D^{d}\!\left(L^{kl}\right)\right) L_{i}{}^{j} V_{b} \bar\psi_{a}{}^{i} \gamma^{abc} \psi_{cj}\\
&+\frac{\sqrt{2}}{2 L^{3}} E_{d} \varepsilon^{jk}\left(L_{l(i} \mathcal D^{d}\!\left(L_{k)}{}^{l}\right)\right) V_{b} \bar\psi_{a}{}^{i} \gamma^{abc} \psi_{cj}\\
&+\frac{2 N}{L} \Box_c\!\left(\frac{N}{L}\right)\\
&+\frac{i N}{L} \Box_c\!\left(\frac{1}{L^{3}} L_{ij} \bar\varphi^{i} \varphi^{j}\right)\\
&- \frac{i}{L^{3}} L_{i}{}^{j} \Box_c\!\left(\frac{N}{L}\right) \bar\varphi^{i} \varphi_{j}\\
&+\frac{4 N^{2}}{L^{2}} f_{a}{}^{a}
\end{aligned}
\tag{SCF.42}
```

```math
\begin{aligned}
&- \frac{4 i N}{L^{4}} L_{i}{}^{j} f_{a}{}^{a} \bar\varphi^{i} \varphi_{j}\\
&- \frac{2 N}{L} \left(\widehat G_{ab} -16 T_{ab}\right) \left(\mathcal D^{[a}\!\left(\frac{1}{L} E^{b]}\right)\right)\\
&- \frac{N}{L^{2}} \left(\widehat G_{ab} -16 T_{ab}\right) L_{ij} \widehat R(V)^{abij}\\
&- \frac{N}{L^{4}} \left(\widehat G_{ab} -16 T_{ab}\right) \left(\mathcal D^{[a}\!\left(L_{i}{}^{k}\right) \mathcal D^{b]}\!\left(L_{jk}\right)\right) L^{ij}\\
&+\frac{N}{L} \left(\widehat G^{ab} -16 T^{ab}\right) \left(\mathcal D_{[a}\!\left(\frac{1}{L^{3}} L_{kl} \bar\varphi^{k} \gamma_{b]} \varphi^{l}\right)\right)\\
&+\frac{i N}{2 L^{2}} \left(\widehat G^{ab} -16 T^{ab}\right) \bar\varphi^{i} \widehat R(Q)_{abi}\\
&+\frac{i}{L^{3}} \left(\widehat G_{ab} -16 T_{ab}\right) \left(\mathcal D^{[a}\!\left(\frac{1}{L} E^{b]}\right)\right) L_{i}{}^{j} \bar\varphi^{i} \varphi_{j}\\
&+\frac{i}{2 L^{4}} \left(\widehat G_{ab} -16 T_{ab}\right) L_{i}{}^{j} L_{kl} \widehat R(V)^{abkl} \bar\varphi^{i} \varphi_{j}
\end{aligned}
\tag{SCF.43}
```

```math
\begin{aligned}
&+\frac{i}{2 L^{6}} \left(\widehat G_{ab} -16 T_{ab}\right) \left(\mathcal D^{[a}\!\left(L_{k}{}^{m}\right) \mathcal D^{b]}\!\left(L_{lm}\right)\right) L_{i}{}^{j} L^{kl} \bar\varphi^{i} \varphi_{j}\\
&+\frac{16 N^{2}}{L^{2}} \widehat G_{ab} T^{ab}\\
&- \frac{16 i N}{L^{4}} \widehat G_{ab} L_{i}{}^{j} T^{ab} \bar\varphi^{i} \varphi_{j}\\
&- \frac{16 N^{2}}{L^{2}} D\\
&+\frac{16 i N}{L^{4}} D L_{i}{}^{j} \bar\varphi^{i} \varphi_{j}\\
&- \frac{416 N^{2}}{3 L^{2}} T_{ab} T^{ab}\\
&+\frac{416 i N}{3 L^{4}} L_{i}{}^{j} T_{ab} T^{ab} \bar\varphi^{i} \varphi_{j}\\
&+\frac{N}{L} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{b} \mathcal D_{b}\!\left(\frac{1}{L} \gamma^{c} \mathcal D_{c}\!\left(\varphi_{i}\right)\right)
\end{aligned}
\tag{SCF.44}
```

```math
\begin{aligned}
&+\frac{8 i N}{L} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{b} \mathcal D_{b}\!\left(\frac{1}{L} L_{ij} \chi^{j}\right)\\
&+\frac{2 i N}{L} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{b} \mathcal D_{b}\!\left(\frac{1}{L} \gamma^{cd} T_{cd} \varphi_{i}\right)\\
&- \frac{i N}{L} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{b} \mathcal D_{b}\!\left(\frac{1}{L^{3}} L_{ij} \left(i \gamma^{c} E_{c} +N\right) \varphi^{j}\right)\\
&- \frac{N}{L} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{b} \mathcal D_{b}\!\left(\frac{1}{L^{3}} \gamma^{c} \mathcal D_{c}\!\left(L_{ij}\right) L^{jk} \varphi_{k}\right)\\
&- \frac{2 i N}{L^{2}} T_{bc} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{bc} \gamma^{d} \mathcal D_{d}\!\left(\varphi_{i}\right)\\
&- \frac{16 N}{L^{2}} L_{i}{}^{j} T_{bc} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{bc} \chi_{j}\\
&+\frac{4 N}{L^{2}} T_{bc} T_{de} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{bc} \gamma^{de} \varphi_{i}\\
&+\frac{2 N}{L^{4}} L_{i}{}^{j} T_{bc} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{bc} \left(i \gamma^{d} E_{d} +N\right) \varphi_{j}
\end{aligned}
\tag{SCF.45}
```

```math
\begin{aligned}
&- \frac{2 i N}{L^{4}} L^{j}{}_{k} \mathcal D_{d}\!\left(L_{i}{}^{k}\right) T_{bc} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{bc} \gamma^{d} \varphi_{j}\\
&+\frac{i N}{4 L^{2}} \widehat G_{bc} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{bc} \gamma^{d} \mathcal D_{d}\!\left(\varphi_{i}\right)\\
&+\frac{2 N}{L^{2}} \widehat G_{bc} L_{i}{}^{j} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{bc} \chi_{j}\\
&- \frac{N}{2 L^{2}} \widehat G_{bc} T_{de} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{bc} \gamma^{de} \varphi_{i}\\
&- \frac{N}{4 L^{4}} \widehat G_{bc} L_{i}{}^{j} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{bc} \left(i \gamma^{d} E_{d} +N\right) \varphi_{j}\\
&+\frac{i N}{4 L^{4}} \widehat G_{bc} L^{j}{}_{k} \mathcal D_{d}\!\left(L_{i}{}^{k}\right) \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{bc} \gamma^{d} \varphi_{j}\\
&+\frac{i N^{2}}{4 L^{2}} \widehat G_{cd} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{cd} \psi_{bi}\\
&- \frac{i N^{2}}{L^{2}} T_{cd} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{cd} \psi_{bi}
\end{aligned}
\tag{SCF.46}
```

```math
\begin{aligned}
&- \frac{i N^{2}}{L^{2}} \bar\psi_{a}{}^{i} \gamma^{ab} \phi_{bi}\\
&- \frac{i N}{2 L^{2}} \Box_c\!\left(L_{i}{}^{j}\right) \bar\psi_{a}{}^{i} \gamma^{ab} \psi_{bj}\\
&+\frac{i N}{2 L^{3}} \mathcal D_{c}\!\left(L\right) \mathcal D^{c}\!\left(L_{i}{}^{j}\right) \bar\psi_{a}{}^{i} \gamma^{ab} \psi_{bj}\\
&- \frac{i N}{2 L^{2}} \left(4 D +\frac{8}{3} T_{cd} T^{cd} - \frac{1}{L^{2}} E_{c} E^{c} - \frac{N^{2}}{L^{2}} +\frac{1}{2 L^{2}} \mathcal D_{c}\!\left(L_{kl}\right) \mathcal D^{c}\!\left(L^{kl}\right)\right) L_{i}{}^{j} \bar\psi_{a}{}^{i} \gamma^{ab} \psi_{bj}\\
&- \frac{i N}{L^{4}} E_{c} \varepsilon^{jk}\left(L_{l(i} \mathcal D^{c}\!\left(L_{k)}{}^{l}\right)\right) \bar\psi_{a}{}^{i} \gamma^{ab} \psi_{bj}\\
&+O_{\rm explicit}(\mathrm{fermion}^{4}).
\end{aligned}
\tag{SCF.47}
```
