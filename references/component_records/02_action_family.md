# EYL-002 — Action family, sources and verification scope

Date: 13 October 2026.

## Scope of the component identities

The action record distinguishes the vector–linear density identity, the component-map checks, and the source assumptions used in the spectrum analysis.

The retained SUSY variation has physical fermion degree one. The following derivations specify the gauge compensations and the composite coefficients through two physical fermions:

- [SUSY compensations](../../common/details/gauge_compensations.md): $`S`$ and $`K`$ were solved from the gauge-preservation equations. The compensating-parameter coefficient for the working generator $`SU(2)`$ was found to be $`-i/(\sqrt2L)`$. Using the source expression $`-1/(\sqrt2L)`$ with the same generator definition leaves the residual $`(i-1)S^{ij}`$. The residual $`U(1)`$ parameter was left free; back-substitution gave zero residual in every symbolic component.
- [Composite-field coefficients](../../common/details/composite_fields.md): the degree coefficients used in the two-fermion action were derived for $`\widehat G`$, $`\widehat H`$, $`T`$, $`E^a`$, $`\omega`$, $`R'(Q)`$, $`\phi`$, $`R(Q)`$, $`\chi`$, $`R'(M)`$, $`f`$ and $`D`$. The gamma trace of the gravitino curvature, $`\gamma\cdot\phi`$, the $`R'(Q)`$ coefficient in $`\chi`$, and the four flux–spinor coefficients in $`D`$ were checked by independent exact symbolic algebra.

The inputs to these additional calculations are listed in a [separate source record](02_susy_additional_sources.json). The tables below distinguish density identities from composite-map checks.

## Selected two-fermion SUSY check

For the action through two physical fermions, the retained density variation is $`[\delta\mathcal L]_1`$.

| Calculation | Equality obtained directly |
|---|---|
| [General vector–linear density](../../common/details/vector_linear_density.md) | $`[\delta(e\ell_{VL})]_1=\partial_\mu(eJ_{VL}^\mu)`$; $`J_{VL}^\mu`$ was written with all its terms. |
| Three-form current | $`[\delta(eP^\mu)]_1=\partial_\nu(eQ^{\mu\nu})`$. The potential coefficients were derived as $`(+1,-3)`$ in the working conventions. |
| [Weyl triplet](../../weyl2/action/multiplet_derivations.md) | $`[\delta_Q L_W-i\bar\epsilon\varphi_W]_1=0`$ and $`[\delta_S L_W]_1=0`$. |
| Weyl spinor | The zero-fermion coefficients of the linear-multiplet $`Q`$ and $`S`$ rules gave zero residual. $`N_W^{(0)},E_W^{(0)}`$ were extracted separately and substituted back into the full spinor equation. |
| [Shared composite vector](../../common/details/linear_vector_map.md) | $`[\delta_Q\rho_1-i\bar\epsilon\lambda_1/2]_1=0`$, $`[\delta_S\rho_1]_1=0`$; the $`Q,S`$ rules of $`\lambda_1`$ were verified at zero-fermion order. |
| Curvature rules | $`\delta R'(Q)`$ was derived from its definition and matched to R05 using the gamma-trace projector. The $`\mathcal DQ`$ and $`TQ`$ coefficients of $`R(S)`$ were substituted back into the Bianchi equation. |

The scalar and vector traces were not substituted for the full spinor equation. All remaining Clifford coefficients of the Weyl spinor also vanished. Exact rational ranks of the fixed-index projectors showed that the symbolic parametrization used in the differential Riemann Bianchi check spans the full constraint space.

The sources and content hashes of these appendices are in a [separate record](02_susy_check_record.json). The [symbolic check files](../../common/details/code/README.md) reproduce the same coefficient checks in a temporary working directory.

## Action basis and retained order

The action basis contains one two-derivative density and three four-derivative invariants: $`R^2`$, Weyl squared and LOG. Their generic linear combination contains the Gauss–Bonnet combination as a special case. The component appendices give the bosonic and physical two-fermion parts.

## Component documents

- [Main narrative](../../common/action_family.md): building blocks, subfamilies, normalizations, field content and the GB relation.
- [Technical index](../../common/action_family.md): six theory pages, four basic building blocks and their GB combination.
- Separate bosonic, covariant-core and explicit two-fermion lists, plus a physical two-fermion definition, for each building block.
- [Shared dictionary](../../common/fields_and_derivatives.md) and [fermion order](../../common/fermion_order.md).
- [Symbolic derivations](../../common/details/action_normalizations.md) and source constructions.

The bosonic and fermionic expressions retain their source-specific mathematical scope. Labels such as ‘verified’, ‘full’ or ‘complete’ refer only to the equations and fermion orders identified by each construction. The individual SUSY identities checked in the component analysis are listed in the table above; faithful transcription alone does not establish those identities.

## Source mapping

| Component source | Mathematical role |
|---|---|
| [Main action](../../common/details/component_action.md) | Closed supercovariant master expression with the three couplings separated; direct input to all core and explicit two-fermion lists. |
| [Bosonic action](../../common/details/bosonic_action.md) | Direct input to the bosonic lists; also compared with the bosonic representation of the master core. |
| [Component source comparison](../component_source_comparison.md) | Coefficient and convention distinctions, with the mathematical scope stated for each recorded check. |
| [Two-derivative construction](../../common/two_derivative_action/details/construction.md) | Provenance of the version used and conformal-box definitions. |
| [Weyl-squared construction](../../weyl2/action/details/construction.md) | Origin of the building block and source scope. |
| [R-squared construction](../../r2/action/details/construction.md) | Source provenance of the BF construction and normalization. |
| [LOG construction](../../log/action/details/construction.md) | Source provenance of the closed representation used for the LOG components. |

The [machine-readable source record](02_action_sources.json) identifies the action inputs and formula-group counts.

The [two-fermion term trace](../two_fermion_terms.json) maps each `v-...` group to an equation block and line range in the master source copy. GB records also include the Weyl/LOG multiplier. Source block numbering starts at one; this mapping is not a SUSY verification label.

## Completed symbolic checks

| Check | Result and scope |
|---|---|
| Coupling decomposition | Only constant, $`\alpha`$, $`\beta`$ and $`\zeta`$ coefficients occurred in each source block. Recombining the four outputs reproduced the same ordered polynomial. |
| File output | The generated formula groups were read back and compared with the coefficient expressions using exact arithmetic. |
| Bosonic-record comparison | The body of the master core, converted to bosonic notation, matched the separate bosonic action record. |
| Explicit fermion order | Core groups contained zero explicit odd-degree objects, and explicit two-fermion groups contained two. This is not a claim that implicit contributions are absent. |
| Curvature coefficients | The normalizations of the recorded densities were calculated by explicit substitution and contraction. |
| Weyl decomposition | For a general symbolic Riemann tensor, the residuals of five contractions vanished; no numerical values were assigned to independent free components. |
| GB relation | The coefficient system gave $`\beta=2\alpha`$, $`\zeta=0`$; back-substitution established exact equality. No division by $`\alpha`$ was performed. |
| All GB blocks | $`\mathcal B_G=\mathcal B_W+2\mathcal B_{\log}`$, $`\mathcal U_G=\mathcal U_W+2\mathcal U_{\log}`$ and $`\mathcal V_G=\mathcal V_W+2\mathcal V_{\log}`$ were checked by exact ordered coefficient equality. |
| Convention agreement | The equalities between different Clifford representations in $`\phi_\mu`$, $`R'(Q)`$ and $`R'(M)`$ were explained; no new bar/charge-conjugation choice was made. |
| Bosonic composites | The equality of $`T^2`$ and the two representations of $`D`$ was shown using epsilon contraction and exact rational arithmetic. |

The curvature check used the Riemann/Bianchi symmetries while leaving the 55 independent entries of the symmetric bivector matrix symbolic. Clifford checks used antisymmetric basis coefficients. The fixed dimension five, indices and exact rational coefficients were used; no free coupling, field or dimensionless ratio was sampled.

### Scope of the formula groups

| Building block | Bosonic $`\mathcal B`$ | Covariant $`\mathcal U`$ | Explicit two-fermion $`\mathcal V`$ |
|---|---:|---:|---:|
| Two derivatives | 11 | 11 | 33 |
| Weyl squared | 17 | 17 | 62 |
| LOG | 40 | 40 | 326 |
| $`R^2`$ | 49 | 49 | 423 |
| GB combination | 54 | 54 | 387 |

These numbers count the groups written to the files. A group may contain several monomials. The GB count is not a count of additional independent invariants. No source-polynomial contributions were omitted using a ‘similar terms’ abbreviation.

## Conventions and distinctions

1. The root `CONVENTIONS.md` file is authoritative for signs, Clifford algebra, $`SU(2)`$ and epsilon. The version used is preserved in [the convention reference](../../common/details/source_conventions.md). The additional complex bar/charge-conjugation assumptions in the master action heading were not imported into the new shared dictionary.
2. Couplings use a single notation: $`\alpha`$ for Weyl squared, $`\beta`$ for LOG, $`\zeta`$ for R squared. The external coupling is not multiplied a second time. For GB, only the free family coordinate $`\lambda`$ is defined.
3. The source's ‘zero explicit fermions’ block was not called the physical bosonic density. The physical two-fermion part is defined as $`\Pi_2\mathcal U_A+\Pi_2\mathcal V_A`$.
4. The source's existing $`\sigma=1`$, dilatino $`\psi^i=0`$, $`b_\mu=0`$ and $`L_{ij}=L\delta_{ij}/\sqrt2`$ notation was recorded. Gravitino $`\psi_\mu^i`$ and $`\varphi^i`$ were retained.
5. The $`L\ne0`$ domain of the shared conventions was not identified with the $`L>0`$ branch of the source action. This version carries the source branch and the condition $`g\ne0`$. No extension to $`L<0`$, $`L=0`$ or $`g=0`$ was derived.
6. Using a dependent-connection definition is not solving an auxiliary-field EOM. No new field elimination was performed here.

## Building-block-specific verification equations

A proof of the general density and a proof of a composite map are distinct mathematical claims. The equalities verified in this record are listed above. The following equalities are **not used as verified results** in this record:

- The Weyl map's $`[\delta N_W]_1`$ and $`[\delta E_{Wa}]_1`$ rules, which also test the $`N_W^{(2)}`$ and $`E_{Wa}^{(2)}`$ coefficients.
- The shared composite vector's $`[\delta Y_1^{ij}]_1`$ and $`[\delta\widehat F_{1ab}]_1`$ rules, which also test the $`Y_1^{(2)}`$ and $`\widehat F_1^{(2)}`$ coefficients.
- The full component transformations of the $`R^2`$ mixed vector–linear map at the same orders, and the LOG map's full one-fermion transformation chain.
- The $`[\delta(e\ell_A)]_1=\partial_\mu(eJ_A^\mu)`$ equalities for the four building blocks after all these composite substitutions.

The zero residual of the general density establishes the stated density identity, not independent one-fermion variations of all four composite actions. The equalities above delimit this check record; they are not a list of missing spectrum calculations. The [action-to-Hessian correspondence](../fermionic_input_correspondence.md) identifies the component inputs and background-specific reductions supporting the selected spectra.

## Symbolic implementation

Fourteen symbolic calculation files were rerun in an independent temporary directory using the packaged runner. All final equality checks passed. The [execution record](02_susy_symbolic_execution.json) contains the SymPy version used and the content hash of each calculation file. This record checks only the equalities at the orders specified above.
