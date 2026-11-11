# Computational support

These packages supply component constructions, coefficient ledgers and
source-specific algebra used by the analytic chapters. The default executable
checks are described in [Reproduction](../README.md#reproduction); source packages are
not a universal action-variation engine.

| Package | Main mathematical content | Scientific chapter |
|---|---|---|
| [Two derivatives](two_derivative_fermionic/README.md) | Linear-to-vector map, BF insertion and quadratic reference action | [Common action](../common/two_derivative_action/README.md), [AdS₅ reference](../two_derivative/ads5/README.md) |
| [Weyl](weyl_fermionic/README.md) | Weyl-to-linear map and covariant component density | [Weyl² action](../weyl2/action/README.md), [AdS₅ operators](../weyl2/ads5/README.md) |
| [LOG](log_fermionic/README.md) | Primary, ordered descendants, component bridge and BF density | [LOG action](../log/action/README.md), [AdS₅ spectrum](../log/ads5/README.md) |
| [R²](r2_fermionic/README.md) | Mixed multiplets, 365-term source representation and elementary expansion | [R² action](../r2/action/README.md), [analytic AdS₅ reduction](../r2/ads5/README.md) |
| [Generic AdS5 massless sector](generic_ads5_massless/README.md) | Paper equations (3.63)–(3.64): symbolic central charges, source-grouped vector-form block and exact massless kinetic coefficients | [Central charges and massless vectors](../generic_combination/ads5/central_charges_and_massless_vectors.md) |
| [Gauss–Bonnet](../gauss_bonnet/ads5/code/README.md) | GB assembly, quadratic coefficients, physical reductions | [GB AdS₅ analysis](../gauss_bonnet/ads5/README.md) |
| [GB AdS3 × Sigma2 bosons](gb_ads3_sigma2/README.md) | Paper Sections 4.2–4.5: symbolic off-shell Hessians, maximal-minor certificates, restricted harmonic levels and signed residues | [Regular BPS product spectrum](../gauss_bonnet/product_backgrounds/supersymmetric_ads3_sigma2/README.md) |
| [GB AdS3 × Sigma2 fermionic action](gb_ads3_sigma2_fermionic/README.md) | Paper Section 4.6 (repository citation 25): complete coupled quadratic action with full supercovariant derivatives; exact LR algebra and explicitly numerical GB matrices | [Fermionic action and checks](../gauss_bonnet/product_backgrounds/supersymmetric_ads3_sigma2/fermionic_quadratic_action.md) |

The [exceptional-background and tower-norm checks](paper_extra_checks/README.md)
cover the additional Section 4 statements listed in their guide.
[Figure scripts](../figures/README.md) redraw Figures 2 and 3.

The additional citation-map packages are:

| Package | Main mathematical content | Scientific chapter |
|---|---|---|
| [GB product fermion spectrum](gb_ads3_sigma2_fermionic_spectrum/README.md) | Paper Section 4.6, Table 12: polynomial mode operators, numerical physical-root census and fixed-charge multiplet matching | [Fermionic spectrum](../gauss_bonnet/product_backgrounds/supersymmetric_ads3_sigma2/fermionic_spectrum.md) |
| [Paper conventions](paper_conventions/README.md) | Exact symbolic vacuum and torsion checks | [Scope and provenance](../references/paper_scope_and_provenance.md) |
| [Composite vector correspondence](composite_vector_correspondence/README.md) | Items 30–31: exact convention identities and bounded numerical Grassmann checks of the corrected map | [Paper-to-component correspondence](../common/details/composite_vector_paper_correspondence.md) |
| [R² final-paper checks](r2_ads5_paper_checks/README.md) | Regular norm reductions and the finite tau=2 vector/scalar/fermion matrices | [R² critical branches](../r2/ads5/details/critical_branches.md) |
| [Weyl/LOG final-paper checks](ads5_paper_checks/README.md) | Vector reduction, norm pullbacks, fermion factors and critical blocks | [Weyl norms](../weyl2/ads5/details/kinetic_norms.md), [LOG operators](../log/ads5/details/physical_operators.md) |
| [Central-charge extremization](central_charge_extremization/README.md) | Trial a, normalized flavor current, c-extremization and universal twist | [Anomalies and extremization](../generic_combination/ads5/anomalies_and_extremization.md) |

Stored outputs identify the calculations and their stated domains. Numerical
evaluations at the paper's sample points are distinguished from exact symbolic
identities. The package guides state the inputs and reproduction commands.

The invariant construction and the spectrum are separate stages: an algebraic
BF-insertion check does not establish a complete Hessian, and a Hessian identity
does not establish all-order nonlinear supersymmetry.

The item-25 package has a separate read-only reproduction command. Its
96 stored matrices and source-term trace are numerical evaluations at the
manuscript's stated sample points. Exact identities and numerical
consistency checks are labelled separately. Item-26 spectral roots and
multiplet matching are supplied by the separate package linked above.
