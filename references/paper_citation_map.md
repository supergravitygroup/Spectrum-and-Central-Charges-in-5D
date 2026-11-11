# Complete citation index for the final paper

The reference is the final supplied **draft_v109.pdf**, with its matching
TeX source. Their hashes identify the manuscript used by these calculations.

| Final source | SHA-256 |
|---|---|
| draft_v109.pdf | 7a9cc9d5a727c9e9b96723ca2eee90e20acaea6b29a3400de25f4f98730f47ed |
| draft_v109.tex | 25be4ea0ef4c3d84032b9990945be1fc017a48de3c80c0f16c2bf4877091b06b |

The final main text contains 31 repository citations. The table follows
their order in the paper. Equation, table and section numbers below are those
printed in the final PDF; TeX labels are retained for source lookup. External
manuscript files are not runtime dependencies.

## All repository citations

The derivation column enters the relevant step in the same model/background
chapters used on the front page. Evidence letters are secondary pointers to
commands and saved records; they are not a separate reading sequence.
Each calculation states its mathematical scope.

| Citation | Paper statement / locator | Repository derivation | Evidence |
|---|---|---|---|
| 1 | Section 1: complete actions, AdS5 Hessians and spectra | [Action-to-spectrum map](source_map.md) | [C](#c), sector records below |
| 2 | Section 2 (`sec:theory`): nonlinear bosons through two fermions | [Component action](../common/details/component_action.md), [fermion order](../common/fermion_order.md) | [C](#c) |
| 3 | Equation (2.16), `eq:general`: complete general action | [Action basis](../common/generic_action.md#definition-and-action-through-two-fermions), [four blocks](../generic_combination/action.md) | [C](#c) |
| 4 | Section 3.1.2: fermionic quadratic action from two-fermion terms | [Component-to-Hessian correspondence](fermionic_input_correspondence.md#component-to-hessian-correspondence) | [C](#c), sector records below |
| 5 | Equations (3.20)–(3.22), `eq:R2vec2`, `eq:R2vec3`, `eq:R2MV` | [R² vector reduction](../r2/ads5/details/kinetic_norms.md#formvector-norms) | [R](#r) |
| 6 | Equation (3.24), `eq:R2fermop`: R² fermionic gauge-invariant action | [Fermionic reduction](../r2/ads5/details/fermionic_operator_reduction.md#from-the-component-density-to-the-hessian) | [R](#r) |
| 7 | Table 3 (`tab:R2`): all kinetic coefficients | [R² norms](../r2/ads5/details/kinetic_norms.md#combined-norm-table), [spectrum](../r2/ads5/spectrum.md) | [R](#r) |
| 8 | Section 3.2.3, Table 4: fermionic norm signs, including A<0 | [R² norms](../r2/ads5/details/kinetic_norms.md#fermionic-norms) | [R](#r) |
| 9 | Section 3.2.3: tau=3/2 degenerate action and zero-source multiplet | [Critical action](../r2/ads5/details/critical_branches.md#tau-three-halves) | [R](#r) |
| 10 | Section 3.2.3: tau=2 vector/spinor Jordan pairs and independent BF scalars | [Undivided endpoint analysis](../r2/ads5/details/critical_branches.md#tau-2-endpoint) | [R](#r) |
| 11 | Equation (3.29), `eq:Wquad`: vanishing background covariants | [Weyl quadratic action](../weyl2/ads5/quadratic_action.md#forms-and-dependent-bosonic-objects) | [W](#w) |
| 12 | Equation (3.42), `eq:WV`: full two-form equation removes a spurious root | [Weyl constraints](../weyl2/ads5/details/gauge_constraints.md#coupled-analysis-of-the-formvector-sector) | [W](#w) |
| 13 | Section 3.3.1: W± vector kinetic coefficients | [Weyl norms](../weyl2/ads5/details/kinetic_norms.md#bosonic-coefficients) | [W](#w) |
| 14 | Section 3.3.2: gauge-invariant Q and X; fermionic action | [Weyl quadratic action](../weyl2/ads5/quadratic_action.md#dependent-fermionic-objects-and-connections) | [W](#w) |
| 15 | Equation (3.47), `eq:Wgravitino`: spin-3/2 and spin-1/2 separation | [Weyl coupled constraints](../weyl2/ads5/details/gauge_constraints.md#fermionic-constraints-and-dynamical-modes) | [W](#w) |
| 16 | Section 3.3.2: gravitino and spinor kinetic coefficients | [Norm pullback and reality convention](../weyl2/ads5/details/kinetic_norms.md#fermionic-coefficients) | [W](#w) |
| 17 | Section 3.3.3: longitudinal/helicity norm factors and sign counts | [Weyl kinetic norms](../weyl2/ads5/details/kinetic_norms.md#longitudinal-norms-and-counting-negative-directions) | [W](#w) |
| 18 | Section 3.3.3: alpha g²=6 repeated quadratic factors | [Weyl critical branches](../weyl2/ads5/details/critical_branches.md#alpha-six) | [W](#w) |
| 19 | Section 3.3.3: alpha g²=-2 logarithmic gravitino and vector Jordan block | [Weyl critical branches](../weyl2/ads5/details/critical_branches.md#alpha-minus-two) | [W](#w) |
| 20 | Equation (3.52), `eq:GBresult`: complete ungauge-fixed fermionic calculation | [GB fermionic reduction](../gauss_bonnet/ads5/details/fermionic_reduction.md#f4-explicit-component-reduction-and-its-domain), [normalization](../gauss_bonnet/ads5/action_inputs.md) | [G](#g) |
| 21 | Equations (3.57), (3.59), `eq:LOGundivided`, `eq:LOGmap`: direct fermionic action | [LOG quadratic action](../log/ads5/quadratic_action.md#fermionic-quadratic-density) | [W](#w) |
| 22 | Section 3.5: third-order LOG fermion operators and roots | [LOG physical operators](../log/ads5/details/physical_operators.md#gravitino-and-spinor-mixing) | [W](#w) |
| 23 | Equations (3.63)–(3.64), `eq:acgen`, `eq:uvgen`: all three couplings | [Central charges and massless vectors](../generic_combination/ads5/central_charges_and_massless_vectors.md#central-charges) | [M](#m) |
| 24 | Section 4.2, equation (4.9), `eq:Kform`: bosonic matrices, polynomials and norms | [Matrices and divisor certificate](../gauss_bonnet/product_backgrounds/supersymmetric_ads3_sigma2/quadratic_actions.md#exact-divisor-certificate), [norms](../gauss_bonnet/product_backgrounds/supersymmetric_ads3_sigma2/norms_and_multiplets.md) | [B](#b), [P](#p) |
| 25 | Section 4.6: full product fermionic action and supercovariant derivatives | [Coupled fermionic action](../gauss_bonnet/product_backgrounds/supersymmetric_ads3_sigma2/fermionic_quadratic_action.md), [inputs](../gauss_bonnet/product_backgrounds/supersymmetric_ads3_sigma2/fermionic_action_inputs.md) | [F](#f) |
| 26 | Section 4.6, Table 12 (`tab:GBferm`): fermionic operators, roots and matching | [Fermionic spectrum](../gauss_bonnet/product_backgrounds/supersymmetric_ads3_sigma2/fermionic_spectrum.md#records-and-scope-of-the-conclusion) | [S](#s) |
| 27 | Section 5: finite couplings, retained fields and vacuum | [Scope and vacuum](paper_scope_and_provenance.md), [action map](source_map.md) | [V](#v), sector records |
| 28 | Acknowledgments: contents, provenance and quoted checks | [Provenance statement](paper_scope_and_provenance.md#item-28-calculation-support), this index | [A](#a), other records here |
| 29 | Appendix A: gravitino contorsion | [Connection conventions](paper_scope_and_provenance.md#item-29-the-connection-retained-in-the-component-action) | [V](#v) |
| 30 | Appendix B: fermionic composites and current | [Composite-vector correspondence](../common/details/composite_vector_paper_correspondence.md#30-component-map-and-action-use) | [D](#d) |
| 31 | Equations (B.3)–(B.5), `eq:compl`–`eq:compF`: corrected map in fermionic actions | [Composite map](../common/details/composite_vector_paper_correspondence.md#composite-field-strength), [input correspondence](fermionic_input_correspondence.md) | [D](#d) |

## Calculations and saved records

| Identifier | Calculation / command guide | Result and scope |
|---|---|---|
| <a id="c"></a>C | [Component packages](../computations/README.md), [source/action correspondence](action_sources.md) | [Term ledger](two_fermion_terms.json), [construction records](source_evidence/README.md); adopted invariants and recorded component construction |
| <a id="r"></a>R | [R² paper checks](../computations/r2_ads5_paper_checks/README.md) | [Results](../computations/r2_ads5_paper_checks/outputs/verification.json), [log](../computations/r2_ads5_paper_checks/outputs/verification.log); exact regular and critical reductions |
| <a id="w"></a>W | [Weyl/LOG paper checks](../computations/ads5_paper_checks/README.md) | [Results](../computations/ads5_paper_checks/outputs/verification.json), [log](../computations/ads5_paper_checks/outputs/verification.log); exact displayed Hessian/operator identities |
| <a id="g"></a>G | [GB AdS5 package](../gauss_bonnet/ads5/code/README.md) | [Component groups](../gauss_bonnet/ads5/code/outputs/fermion_component_groups.json), [reduction](../gauss_bonnet/ads5/code/outputs/fermionic_reduction.json); full component calculation with its stated parameter-restoration argument |
| <a id="m"></a>M | [Generic massless sector](../computations/generic_ads5_massless/README.md) | [Results](../computations/generic_ads5_massless/outputs/results.json), [log](../computations/generic_ads5_massless/outputs/verification.log); exact all-coupling calculation |
| <a id="b"></a>B | [GB bosonic checks](../computations/gb_ads3_sigma2/README.md) | [Log](../computations/gb_ads3_sigma2/outputs/verification.log), [norm samples](../computations/gb_ads3_sigma2/outputs/norm_samples.json); exact matrices/divisors and labelled numerical norms |
| <a id="p"></a>P | [Product-model checks](../computations/gb_ads3_sigma2/product_checks.py), [guide](../computations/gb_ads3_sigma2/README.md) | [Results](../computations/gb_ads3_sigma2/outputs/product_checks/verification.json), [log](../computations/gb_ads3_sigma2/outputs/product_checks/verification.log); E-deletion example and two numerical points for each separate model |
| <a id="f"></a>F | [Product fermionic action](../computations/gb_ads3_sigma2_fermionic/README.md) | [Results](../computations/gb_ads3_sigma2_fermionic/outputs/verification.json), [log](../computations/gb_ads3_sigma2_fermionic/outputs/verification.log); exact LR identities and numerical GB matrices |
| <a id="s"></a>S | [Product fermionic spectrum](../computations/gb_ads3_sigma2_fermionic_spectrum/README.md) | [Sample and operator index](../computations/gb_ads3_sigma2_fermionic_spectrum/outputs/index.md), [table](../computations/gb_ads3_sigma2_fermionic_spectrum/outputs/table.json), [results](../computations/gb_ads3_sigma2_fermionic_spectrum/outputs/verification.json); numerical root census and fixed-charge matching |
| <a id="v"></a>V | [Vacuum and convention checks](../computations/paper_conventions/README.md) | [Results](../computations/paper_conventions/outputs/verification.json), [log](../computations/paper_conventions/outputs/verification.log); symbolic vacuum and torsion identities |
| <a id="a"></a>A | [Anomalies and extremization](../computations/central_charge_extremization/README.md) | [Results](../computations/central_charge_extremization/outputs/verification.json), [log](../computations/central_charge_extremization/outputs/verification.log); exact a-maximization, c-extremization and universal twist |
| <a id="d"></a>D | [Composite correspondence](../computations/composite_vector_correspondence/README.md) | [Results](../computations/composite_vector_correspondence/outputs/verification.json), [log](../computations/composite_vector_correspondence/outputs/verification.log); exact convention identities and specified numerical Grassmann blocks |

## Scope of the accompanying checks

The paragraph following citation 24 also states the E-term deletion example
and two numerical product-background spectra for each of W, LOG and R²;
these are evidence P. The [norm explanation](../gauss_bonnet/product_backgrounds/supersymmetric_ads3_sigma2/norms_and_multiplets.md)
specifies the branch choice for the four alternative-quantization pairs.

The central-charge statements in Sections 3.6 and 4.4 are connected through
[anomalies and extremization](../generic_combination/ads5/anomalies_and_extremization.md):
trial a, normalized flavor coefficient, general-family c-extremization,
R-current level and the universal-twist correction. They are separate
from citation 23's direct computation of a, c, u and v.

For citations 25–26, full GB matrices and physical roots are numerical at the
paper's stated samples. This index does not turn them into an all-coupling
symbolic theorem. Fermion norms, global harmonic multiplicities and the
excluded critical loci remain outside the paper's claim. Citations 29–31
adopt the stated source constructions with the bounded checks described
in their guides. The manuscript contains its own author acknowledgments.
