# Mathematical evidence and verification scope

The spectrum results are attached to specific component actions, branches and quadratic reductions. The [source map](source_map.md) and [fermionic input correspondence](fermionic_input_correspondence.md) give equation-level links. A literature citation, an analytic reduction, an exact algebraic check and a saved numerical comparison support different claims.

## Adopted constructions and local results

Established superconformal multiplets, vector–linear density formulas and invariant constructions are adopted from the cited literature. Their source equations, assumptions, fermion order and convention conversions are specified in the action appendices. A local sign or coefficient correction is supported by its own displayed algebra; it is not described as a published erratum or a new proof of every supersymmetry identity.

The project-specific spectrum evidence is the chain

```math
\text{component action}
\ \longrightarrow\ 
\text{background equations}
\ \longrightarrow\
S^{(2)}
\ \longrightarrow\
\text{coupled constraints and physical operator}
\ \longrightarrow\
\text{roots, eigenfields and norms}.
```

Each arrow is interpreted within the assumptions stated at that step. An off-shell auxiliary field may become dynamical in a higher-derivative theory. A root count alone does not establish a positive physical norm, a supersymmetric boundary domain or equivalence of two nonlinear actions.

| Subject | Primary mathematical evidence | Computational support and limitation |
|---|---|---|
| Common two-derivative action | [2016-map construction](../common/two_derivative_action/details/construction.md), especially (4.27a), (4.33)–(4.37), (5.10) | [Component package](../computations/two_derivative_fermionic/README.md). The lower-index derivative has the negative connection term. |
| R² on AdS5 | [Quadratic action](../r2/ads5/quadratic_action.md), [fermionic reduction](../r2/ads5/details/fermionic_operator_reduction.md), (F.1)–(F.8), and [norms](../r2/ads5/details/kinetic_norms.md) | [Final-paper checks](../computations/r2_ads5_paper_checks/README.md) verify the displayed reductions, norms and critical matrices. The [construction package](../computations/r2_fermionic/README.md) supplies the component expressions. |
| R² critical endpoint | [Critical action and constraints](../r2/ads5/details/critical_branches.md) | Generic inverse eigenfield transformations are not continued through a zero denominator. The displayed critical action determines the linearized degeneracy. |
| Weyl² on AdS5 | [Quadratic action](../weyl2/ads5/quadratic_action.md) and [physical operators](../weyl2/ads5/details/physical_operators.md) | [Final-paper checks](../computations/ads5_paper_checks/README.md) cover vector reduction, norm pullbacks, fermion factors and critical blocks. The [construction package](../computations/weyl_fermionic/README.md) supplies the component expressions. |
| LOG on AdS5 | [Component input](../log/action/details/spectrum_input.md) and [quadratic action](../log/ads5/quadratic_action.md) | [Final-paper checks](../computations/ads5_paper_checks/README.md) verify the displayed fermionic operator reduction and roots. The [construction package](../computations/log_fermionic/README.md) and [source evidence](source_evidence/README.md) retain their component-construction scope. |
| Gauss–Bonnet on AdS5 | [Specified action](../gauss_bonnet/ads5/action_inputs.md), [quadratic action](../gauss_bonnet/ads5/quadratic_action.md) and [fermionic reduction](../gauss_bonnet/ads5/details/fermionic_reduction.md) | The fixed-frame component comparison uses $`k=-1,g=1,x=\sqrt2`$. It is distinct from the symbolic parameter-restoration argument and is not general symbolic verification. |
| GB BPS AdS3 × Sigma2, Sections 4.2–4.5 (repository citation 24) | [Action correspondence, quadratic matrices, polynomials and norms](../gauss_bonnet/product_backgrounds/supersymmetric_ads3_sigma2/README.md) | [Executable package](../computations/gb_ads3_sigma2/README.md): free-parameter source/Hessian comparisons, exact rank factorizations and all-minor divisibility certificates, restricted harmonics, exact residue identities. The separate v109 norm tables are finite samples with 80/140-digit checks; they do not prove global boundary unitarity. The fermionic action and spectrum (repository citations 25–26) are excluded. |
| GB BPS product fermionic action, Section 4.6 (repository citation 25) | [Complete mode action, source coverage and derivative overlay](../gauss_bonnet/product_backgrounds/supersymmetric_ads3_sigma2/fermionic_quadratic_action.md) | [Executable package](../computations/gb_ads3_sigma2_fermionic/README.md): exact LR/background checks; 96 double-precision coupled matrices, full derivative identities, FQ.26 diagonal, SUSY columns and four negative controls. Scaled matrix tolerance is 2e-10; numerical interpolation uses 2e-8 with two resolutions and holdouts. No symbolic GB-family proof, generic nullity certificate, fermionic root census, multiplet matching or fermion norms. |

## Symbolic verification

The [complete final-paper citation index](paper_citation_map.md)
connects the existing calculations and the following bounded verification routes:

| Route | New evidence | Limit |
|---|---|---|
| [Item-26 spectrum](../computations/gb_ads3_sigma2_fermionic_spectrum/README.md) | Reconstructed polynomial operators, independent projections and interpolation checks, direct-action root residuals, fixed-charge perfect matching and two-derivative limits | Finite numerical samples; no universal symbolic GB rank proof, fermion norms or global harmonic multiplicities |
| [Items 27 and 29: vacuum and connection](../computations/paper_conventions/README.md) | Exact free-bilinear torsion identities and free-coupling vacuum first variations, including a nonzero second Weyl variation and negative controls | Bounded identities using the existing item-23 action projection; the paper contains its author acknowledgments |
| [Items 30–31 map correspondence](../computations/composite_vector_correspondence/README.md) | Exact SU(2), derivative and current identities, plus fresh numerical Grassmann checks of the stated corrected blocks | The numerical tests are not symbolic all-order SUSY proofs; their block coverage and tolerances are recorded separately |
| [Central-charge extremization](../computations/central_charge_extremization/README.md) | Source-grouped CS terms, trial a, current normalization, general-family c-extremization and universal twist | Exact identities for the final paper's displayed formulas; adopted anomaly inflow normalization |

Free couplings, moduli and combinations such as $`\alpha g^2`$ remain symbolic. Exact coefficient comparison, factorization, back-substitution and reduction modulo the background equations can establish identities on their stated branches. Numerical evaluation of a free parameter, including a rational choice or a purported unit normalization, cannot establish such an identity.

A branch substitution must follow from the relevant equation. Denominators and rank-changing loci remain visible. The definition $`x=\alpha g^2`$ preserves the dependency; assigning $`x`$ a sample value removes it.

The [targeted symbolic script](../tools/check_symbolic_identities.py) concerns the lower-triplet index-lowering sign, the Weyl vector determinant, and the pure-curvature GB coefficient relation. These are finite algebraic checks, not complete certifications of the actions or spectra. The [structural validator](../tools/validate_repository.py) checks document and file consistency; its result does not certify a physical claim.

The [boundary conditions](../common/kinetic_terms_and_stability.md) and
adjoint definitions determine the physical interpretation of norms.
Numerical sample results remain restricted to their stated domains.
