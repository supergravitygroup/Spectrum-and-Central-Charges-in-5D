# Map of actions and spectrum derivations

| Analysis | Action input | Background | Quadratic reduction | Spectrum | Norms and exceptional branches |
|---|---|---|---|---|---|
| Two-derivative reference | [2016-map action](../common/two_derivative_action/README.md) | [AdS₅ branch](../two_derivative/ads5/README.md) | [Quadratic action and reduction sources](../two_derivative/ads5/README.md) | [Reference modes](../two_derivative/ads5/README.md) | The reference source representation and its parameter-domain qualifications |
| R² on AdS5 | [Input](../r2/ads5/action_inputs.md) | [Branches](../r2/ads5/background.md) | [Quadratic action](../r2/ads5/quadratic_action.md), [constraints](../r2/ads5/details/gauge_constraints.md) | [Table](../r2/ads5/spectrum.md), [eigenfields](../r2/ads5/details/masses_and_eigenfields.md) | [Norms](../r2/ads5/details/kinetic_norms.md), [critical branches](../r2/ads5/details/critical_branches.md) |
| Weyl² on AdS5 | [Input](../weyl2/ads5/action_inputs.md) | [Branches](../weyl2/ads5/background.md) | [Quadratic action](../weyl2/ads5/quadratic_action.md), [operators](../weyl2/ads5/details/physical_operators.md) | [Bosons](../weyl2/ads5/bosonic_spectrum.md), [fermions](../weyl2/ads5/fermionic_spectrum.md) | [Norms](../weyl2/ads5/details/kinetic_norms.md), [critical branches](../weyl2/ads5/details/critical_branches.md) |
| LOG on AdS5 | [Input](../log/ads5/action_inputs.md) | [Branches](../log/ads5/background.md) | [Quadratic action](../log/ads5/quadratic_action.md), [operators](../log/ads5/details/physical_operators.md) | [Bosons](../log/ads5/bosonic_spectrum.md), [fermions](../log/ads5/fermionic_spectrum.md) | [Norms](../log/ads5/details/kinetic_norms.md), [exceptional spectra](../log/ads5/details/exceptional_spectra.md) |
| Gauss–Bonnet on AdS₅ | [Action](../gauss_bonnet/action/gb_splus_action.md), [normalization](../gauss_bonnet/ads5/action_inputs.md) | [Branches](../gauss_bonnet/ads5/background.md) | [Quadratic action](../gauss_bonnet/ads5/quadratic_action.md), [fermionic reduction](../gauss_bonnet/ads5/details/fermionic_reduction.md) | [Table](../gauss_bonnet/ads5/spectrum.md), [eigenfields](../gauss_bonnet/ads5/details/masses_and_eigenfields.md) | [Norms](../gauss_bonnet/ads5/details/kinetic_norms.md), [critical endpoint](../gauss_bonnet/ads5/details/critical_branches.md) |
| GB BPS AdS3 × Sigma2, Sections 4.2–4.5 (repository citation 24) | [Current-source correspondence](../gauss_bonnet/product_backgrounds/supersymmetric_ads3_sigma2/action_inputs.md) | Regular BPS branch on the same page | [Complete bosonic matrices and certificates](../gauss_bonnet/product_backgrounds/supersymmetric_ads3_sigma2/quadratic_actions.md) | [Generic polynomials](../gauss_bonnet/product_backgrounds/supersymmetric_ads3_sigma2/generic_levels.md), [special levels](../gauss_bonnet/product_backgrounds/supersymmetric_ads3_sigma2/special_levels.md) | [Signed residues and scope](../gauss_bonnet/product_backgrounds/supersymmetric_ads3_sigma2/norms_and_multiplets.md) |
| GB BPS product fermionic action, Section 4.6 (repository citation 25) | [Component density, normalization and H02 overlay](../gauss_bonnet/product_backgrounds/supersymmetric_ads3_sigma2/fermionic_action_inputs.md) | Regular BPS branch, both chiralities, nonzero surface curvature | [Coupled quadratic matrices and source-term trace](../gauss_bonnet/product_backgrounds/supersymmetric_ads3_sigma2/fermionic_quadratic_action.md) | The separate fermionic spectrum roots and multiplet matching are not part of this calculation | Fermion norms, global multiplicities and excluded loci are not computed |

The [component source map](action_sources.md),
[two-fermion term index](two_fermion_terms.json) and
[fermionic input correspondence](fermionic_input_correspondence.md)
identify the expressions used in these reductions.

The [product fermionic spectrum](../gauss_bonnet/product_backgrounds/supersymmetric_ads3_sigma2/fermionic_spectrum.md)
continues the coupled mode action to numerical roots and fixed-charge multiplet
matching at the paper's sample points.

The [complete citation index](paper_citation_map.md) gives all 31 manuscript
locators, implementations and results. The
[convention analysis](paper_scope_and_provenance.md) covers the vacuum and
torsion, while the [composite-vector correspondence](../common/details/composite_vector_paper_correspondence.md)
identifies the Appendix-B map.

The [general-combination AdS₅ calculation](../generic_combination/ads5/central_charges_and_massless_vectors.md)
supplies the central charges and massless-vector kinetic coefficients.
The [verification guide](verification_scope.md) specifies the exact and
numerical checks, with commands in [Reproduction](../README.md#reproduction).
