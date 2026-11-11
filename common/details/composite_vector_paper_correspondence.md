# Composite vector: paper correspondence and bounded checks

This note connects citations **30 and 31** of the [final-paper citation index](../../references/paper_citation_map.md) to the composite-vector appendix of `draft_v109.tex`. Equation labels identify the correspondence below.

The component expressions and the actions already exist here. This note records their equivalence, derivative conventions and use in the action. It introduces no new component map or coupling choice. All formulas use the existing $`L>0`$ domain, northwest–southeast SU(2) contractions and unit-weight (anti)symmetrization.

## 30: component map and action use

| Paper expression | Existing repository expression | Comparison required |
|---|---|---|
| $`\rho`$ immediately before equation (B.3) (`eq:compl`) | [Scalar component](linear_vector_construction.md), also [construction (4.33)](../two_derivative_action/details/construction.md) | Move SU(2) indices consistently in $`L_{ij}\bar\varphi^i\varphi^j=L^{ij}\bar\varphi_i\varphi_j`$. |
| Equation (B.3) (`eq:compl`) | [Composite map](linear_vector_construction.md), $`\lambda_{1i}`$; construction (4.34) | The cubic spinor product can be written with an outer product or a scalar bilinear. Keep the original Grassmann order when converting. |
| Equation (B.4) (`eq:compY`) | [Composite map](linear_vector_construction.md), $`Y_{1ij}`$; construction (4.35) | The active coefficients are the corrected single-multiplet 2016 map; see the dictionary below. |
| Equation (B.5) (`eq:compF`) | [Composite map](linear_vector_construction.md), $`\widehat F_{1\mu\nu}`$; construction (4.36) | The paper leaves two covariant products differentiated; the repository expands their Leibniz rules. |
| BF density $`\longrightarrow\mathcal L_{LR}`$ | [Two-derivative construction](../two_derivative_action/details/construction.md), substitution following (4.37), final (5.10) | Insert the corrected composite vector into the full vector–linear density and retain physical orders zero and two. |
| BF density $`\longrightarrow\mathcal L_{R^2}`$ | [Ricci-scalar-squared construction](../../r2/action/details/construction.md), §§2–4 and final (R2) | Keep the two vector roles distinct, form the mixed linear multiplet, insert the primed map, then collect through two physical fermions. |

The full map includes cubic $`\lambda_1`$ and quartic $`Y_1`$. Their presence in the source map does not make the displayed action a quartic-fermion action. For example, in the BF term $`\bar\lambda_1\varphi`$, only $`\lambda_1^{[1]}`$ contributes at physical order two; $`\lambda_1^{[3]}\varphi`$ has order four. Conversely, $`\lambda_1^{[3]}`$ is needed when deriving the quadratic-fermion part of $`\delta\lambda_1`$, since varying one fermion replaces it by a bosonic field times the supersymmetry parameter.

Even composites in a closed action must also be expanded: $`\rho_1^{[2]}N^{[0]}`$, $`Y_1^{[2]}L`$ and the bilinear parts of hatted curvatures, covariant derivatives and dependent fields contribute. Thus explicit odd-factor counting alone is insufficient. This is the existing rule in [fermion order](../fermion_order.md), and the current correction in §30 below is one example.

### Equivalent SU(2) bases and the 2013/2016 distinction

For $`\Gamma=1`$ or $`\gamma^a`$, define

```math
\begin{aligned}
B^{ij}(\Gamma)&=\bar\varphi^i\Gamma\varphi^j=B^{ji}(\Gamma),&
Q(\Gamma)&=L^{ij}B_{ij}(\Gamma),\\
K_{ij}(\Gamma)&=L_{k(i}L_{j)m}B^{km}(\Gamma),&
K_{ij}(\Gamma)&=L_{ij}Q(\Gamma)-\tfrac12L^2B_{ij}(\Gamma).
\end{aligned}
```

Here $`B^{ij}`$ is symmetric because $`C\Gamma`$ is antisymmetric and the spinors are Grassmann odd. The last identity is a two-dimensional triplet identity, not a numerical fit. The new check treats all three entries of each symmetric matrix as independent symbols and verifies it as a polynomial identity.

The following table gives **ordered pairs of coefficients** in the indicated 2013 basis. The scalar $`N`$ multiplies both structures in the first row; $`\Gamma=\widehat{\mathord{\not{E}}}`$ in the second.

| Sector and basis | Literal 2013 eq. (3.4) | Corrected 2016 single-multiplet map, also the paper |
|---|---|---|
| $`N\{L^{-3}B_{ij}(1),L^{-5}K_{ij}(1)\}`$ | $`(-i/2,-4/3)`$ | $`(-i/2,-3i)`$ |
| $`\{L^{-3}B_{ij}(\widehat{\mathord{\not{E}}}),L^{-5}K_{ij}(\widehat{\mathord{\not{E}}})\}`$ | $`(-2/3,-1/3)`$ | $`(1/2,3)`$ |
| $`\{S_{1ij},S_{2ij}\}`$, defined below | $`(-2/3,-1)`$ | $`(-1,3)`$ |

```math
\begin{aligned}
S_{1ij}&=L^{-3}\bar\varphi_{(i}
 (\mathord{\not{\mathcal D}}L_{j)k})\varphi^k,\\
S_{2ij}&=L^{-5}L_{mn}L^k{}_{(i}\bar\varphi^m
 (\mathord{\not{\mathcal D}}L_{j)k})\varphi^n.
\end{aligned}
```

The paper's $`N`$ and $`\widehat E`$ blocks are respectively

```math
\begin{aligned}
Y_{ij}\big|_{N\varphi^2}
 &=iNL^{-3}B_{ij}(1)-3iNL^{-5}L_{ij}Q(1),\\
Y_{ij}\big|_{\widehat E\varphi^2}
 &=-L^{-3}B_{ij}(\widehat{\mathord{\not{E}}})
   +3L^{-5}L_{ij}Q(\widehat{\mathord{\not{E}}}),\\
Y_{ij}\big|_{\mathcal DL\varphi^2}
 &=-3L^{-5}L_{k(i}L^{lm}\bar\varphi^k
     (\mathord{\not{\mathcal D}}L_{j)l})\varphi_m
   +\tfrac12L^{-3}\bar\varphi^k
     (\mathord{\not{\mathcal D}}L_{k(i})\varphi_{j)}\\
 &=-S_{1ij}+3S_{2ij}.
\end{aligned}
```

The implementation verifies the last equality for independent $`L^{ij}`$, $`\mathcal D_aL^{ij}`$ and symmetric $`B^{ij}(\gamma^a)`$, and independently solves for the two coefficients $`(-1,3)`$. It also verifies that the literal-2013 coefficients give nonzero residual polynomials. These are distinct source versions, not interchangeable transcriptions.

The additional term $`\tfrac12L^{-3}\bar\varphi^m(\mathord{\not{\mathcal D}}L_{ij})\varphi_m`$ displayed in construction (4.35) is zero: $`\bar\varphi^m\gamma^a\varphi_m`$ contracts a symmetric SU(2) bilinear with an antisymmetric epsilon. Likewise, the cubic-$`\lambda`$ outer-product arrangement agrees with the paper because $`\bar\varphi_k\varphi_i=\bar\varphi_i\varphi_k`$; no commuting of two odd factors without a sign is permitted.

The quartic terms of $`Y_1`$ are already printed in the composite map and agree with the paper's three scalar-bilinear structures. The two literal-2013 vector-bilinear structures are not adopted. No new quartic-action calculation is asserted here.

<a id="composite-field-strength"></a>

### Ordered derivative expansion in $`\widehat F_1`$

Using $`\mathcal D_\mu L=L^{-1}L^{kl}\mathcal D_\mu L_{kl}`$, the compact paper expression expands as

```math
\begin{aligned}
4\mathcal D_{[\mu}(L^{-1}\widehat E_{\nu]})
 &=4L^{-1}\mathcal D_{[\mu}\widehat E_{\nu]}
   -4L^{-3}L^{kl}(\mathcal D_{[\mu}L_{kl})\widehat E_{\nu]},\\
-2\mathcal D_{[\mu}(L^{-3}L_{ij}\bar\varphi^i\gamma_{\nu]}\varphi^j)
 &=-2L^{-3}(\mathcal D_{[\mu}L_{ij})
       \bar\varphi^i\gamma_{\nu]}\varphi^j\\
 &\quad+6L^{-5}L_{ij}L^{kl}(\mathcal D_{[\mu}L_{kl})
       \bar\varphi^i\gamma_{\nu]}\varphi^j\\
 &\quad+4L^{-3}L_{ij}\bar\varphi^i\gamma_{[\mu}
       \mathcal D_{\nu]}\varphi^j.
\end{aligned}
```

The two spinor-derivative contributions coincide after the Majorana swap and symmetric $`L_{ij}`$ contraction. Their coefficient is $`-4`$ before exchanging the antisymmetrized $`\mu,\nu`$ positions, hence $`+4`$ in the displayed order. No integration by parts or derivative commutator is used. The remaining triplet-gradient term in $`\widehat F_1`$ is already antisymmetric in $`\mu,\nu`$ by its SU(2) contractions.

## 29: current, derivative and d'Alembertian

| Paper label | Repository location | Meaning |
|---|---|---|
| Equation (B.1) (`eq:EhatE`) | [Fields and derivatives](../fields_and_derivatives.md), current dictionary; [composite fields](composite_fields.md), $`E_a^{(2)}`$ | Repository $`E^a`$ is paper $`\widehat E^a`$; repository $`P^a`$ is paper's bosonic dual $`E^a`$. |
| Equation (B.6) (`eq:Dlin`) | [Superconformal definitions](superconformal_definitions.md), linear-multiplet derivatives and correction derivation; [fields and derivatives](../fields_and_derivatives.md) | The $`\mathcal D\varphi`$ coefficient is $`+i/2`$, and $`\mathcal D_aE^a=0`$ is the adopted linear-multiplet constraint. |
| Equation (B.7) (`eq:boxc`) | [Superconformal definitions](superconformal_definitions.md), superconformal d'Alembertian | The existing ordered expression includes the inherited dependent connections and fermionic terms; it is based on the corrected derivative. |

In this repository's notation the current relation is

```math
\begin{aligned}
P^a&=E^a+\tfrac i2\bar\psi_b^i\gamma^{ba}\varphi_i
              +\tfrac14L_{ij}\bar\psi_b^i\gamma^{abc}\psi_c^j,\\
E^{a[2]}&=-\tfrac i2\bar\psi_b^i\gamma^{ba}\varphi_i
              -\tfrac14L_{ij}\bar\psi_b^i\gamma^{abc}\psi_c^j,
\qquad P^{a[2]}=0.
\end{aligned}
```

Here the square brackets indicate physical fermion order, with independent bosonic fields held fixed. Setting $`E^{[2]}=0`$ would lose the two bilinears. The BF coupling uses the ordinary conserved current, $`eA_\mu P^\mu`$. Its conservation is the three-form identity $`\partial_\mu(eP^\mu)=0`$, not an Euler–Lagrange equation. The supercovariant statement $`\mathcal D_aE^a=0`$ is the corresponding adopted multiplet constraint; the elementary antisymmetry check in the new package verifies ordinary-current conservation only, not all of its supercovariant completion.

For the coefficient $`c`$ of $`(\mathord{\not{\mathcal D}}L^{ij})\psi_{\mu j}`$ in $`\mathcal D_\mu\varphi^i`$, the variation of the leading derivative and $`\delta\psi_{\mu j}\supset\partial_\mu\epsilon_j`$ gives

```math
\delta(\mathcal D_\mu\varphi^i)\big|_{\partial\epsilon}
=(-\tfrac i2+c)(\mathord{\not{\mathcal D}}L^{ij})\partial_\mu\epsilon_j,
\qquad c=\tfrac i2.
```

Thus the real $`1/2`$ printed in 2016 eq. (3.7) must not be reinstated. The repository and paper already use this correction. On the paper's AdS$`_5`$ backgrounds, $`\mathcal D L=\widehat E=\widehat F=0`$ and all fermions vanish; the appendix explains why these derivative/current distinctions do not change the quadratic fluctuation actions there. They remain necessary for the covariant component map and its action correspondence.

## Reproducible evidence and limits

The new [computation package](../../computations/composite_vector_correspondence/README.md) records input fingerprints and fresh results. Exact symbolic checks cover the SU(2) identities, the coefficient dictionary, the ordered scalar Leibniz coefficients, the local $`\partial\epsilon`$ cancellation, ordinary-current conservation, Clifford conventions and BF fermion-order selection. These checks are algebraic identities; they do not independently reconstruct all terms of the source expressions.

An original exterior-algebra implementation keeps eight $`\varphi`$ and eight $`\epsilon`$ components formal. Even variation jets differentiate the linear and cubic pieces of $`\lambda`$ before selecting $`\epsilon\varphi^2`$ and taking the Clifford scalar trace. The **42** comparisons use two positive numerical triplets (seeds 7 and 4, both $`L=2`$), all five $`\widehat E_a`$ directions, and all five derivative directions with the three independent symmetric $`\mathcal D_aL^{ij}`$ entries. The $`N`$, $`\widehat E`$ and $`\mathcal DL`$ blocks agree with the paper; six deliberately literal-2013 negative comparisons fail as expected. All coefficients remain present until comparison; the implementation does not threshold small coefficients to zero.

These finite tests support those selected blocks at $`\psi_\mu=0`$. They are not a proof for arbitrary bosonic fields, the full nonlinear transformation, all non-scalar Clifford components, the $`\chi`$, $`T`$, $`\mathcal D\varphi`$ or gravitino-dependent blocks, or a quartic action. The full $`\widehat F`$, $`\Box^c`$ and supercovariant-current formulas remain source-defined inputs with the narrower equivalence checks described above. Existing source/action checks retain their previously documented scope.

The supplied repository's notes and scripts informed the choice of coefficient comparisons. No file or program was imported from it, and rerunning this package requires neither that folder nor the external manuscript. Its identities and source provenance are recorded in the [manifest](../../computations/composite_vector_correspondence/source_manifest.json); the current run is in the [verification record](../../computations/composite_vector_correspondence/outputs/verification.json).
