# Fermionic action inputs and spectrum Hessians

The spectra use the 2016 single-linear-multiplet construction for their
two-derivative sector. Each quadratic action retains its own background
scalar and coupling normalization.

## Component-to-Hessian correspondence

For citation-map items 30–31, the
[paper-to-component bridge](../common/details/composite_vector_paper_correspondence.md)
matches paper equations (B.3)–(B.5), (B.1), (B.6) and (B.7) to these
2016-map constructions. It distinguishes the paper's supercovariant
E-hat from its ordinary conserved current and records the corrected
fermionic coefficients. The
[correspondence package](../computations/composite_vector_correspondence/README.md)
provides exact convention checks and explicitly numerical Grassmann
tests of the stated map blocks.

| Spectrum | Action and map | Quadratic expression and recorded reduction |
|---|---|---|
| R², AdS5 | [Assembled action](../r2/action/details/source_action.md), (A.19), (M.1)–(M.4), (A.31)–(A.35); two-derivative density (5.10), R² density (R2) | [Raw density and currents](../r2/ads5/details/fermionic_density.md); [operator reduction](../r2/ads5/details/fermionic_operator_reduction.md), (F.1)–(F.8). In particular, the explicit 2016 trace is retained in (F.8) before the component-action coefficient table is compared with the Hessian. |
| Weyl², AdS5 | [Full input](../weyl2/action/details/complete_spectrum_input.md), (D-4.33)–(D-4.37), (V-4.27a), and (GA24) | [Quadratic action](../weyl2/ads5/quadratic_action.md), (10)–(13) for linear composites, (18) for the raw two-derivative fermion density, and (19)–(20) for its source-slot coefficient sum. |
| LOG, AdS5 | [Full input](../log/action/details/spectrum_input.md), (A2-4.33)–(A2-4.37), (A28), (A32), (A34); (A35)–(A37) state the compensating-transformation correction and its lack of change to (A28), (A32) | [Quadratic action](../log/ads5/quadratic_action.md), (Q24), (Q26)–(Q29) for composites, (Q31)–(Q32), (Q36) for the two-derivative fermion block, (Q35), (Q37) for the LOG block, and (Q40), (Q57) for the assembled quadratic system. |
| Gauss–Bonnet on AdS₅ | [Component action](../gauss_bonnet/action/gb_splus_action.md), (GB16), (GB-FINAL-ACTION), (GB-FINAL-DENSITY), and their component definitions; [2016-map qualification](../common/two_derivative_action/details/gb_input_qualifications.md), (A3), (A9)–(A13) | [Quadratic action](../gauss_bonnet/ads5/quadratic_action.md), (6.31)–(6.32), with the source scalar $`x`$ and kinetic factor $`c`$; [fermionic reduction](../gauss_bonnet/ads5/details/fermionic_reduction.md). |

These locators identify the component input of each quadratic derivation.

## Product-background fermionic action, item 25

The [new input ledger](../gauss_bonnet/product_backgrounds/supersymmetric_ads3_sigma2/fermionic_action_inputs.md)
connects the 2016-map density (5.10) and GB-FINAL-DENSITY to the complete
[coupled primary-mode action](../gauss_bonnet/product_backgrounds/supersymmetric_ads3_sigma2/fermionic_quadratic_action.md),
(F24.8)–(F24.11). Its source-to-matrix trace retains all 1184 original
higher-derivative summands. Bosonic-form terms supply their implicit
fermion bilinears as well as the explicit two-fermion terms.

This calculation uses the displayed local H02 overlay (F24.3)–(F24.4):
the isolated G–dilatino sign is positive and the gauged varphi term is
included. It also differentiates the bilinear in source term 17 with
the full Q/S connections. The AdS5 reductions use the same surviving quadratic terms, as explained below. Numerical matrix and derivative checks
are labelled separately from exact LR/background identities. This is
the action input for the separate
[item-26 physical-root calculation](../gauss_bonnet/product_backgrounds/supersymmetric_ads3_sigma2/fermionic_spectrum.md).

The H02 overlay does not alter the displayed AdS5 quadratic reductions.
Its changes enter implicit bilinears in derivatives of H. In the AdS5
[source-term reduction](../gauss_bonnet/ads5/code/derivations/spectrum/SOURCE_TERM_LEDGER.md),
such terms carry another vanishing background factor; the possible
epsilon contraction with the background scalar Hessian vanishes by
symmetry. The surviving scalar-box bilinears in GB (FC1–FC6) and LOG
(Q24–Q30) are unaffected. This background-specific statement explains
why these derivative terms leave the quoted AdS5 spectra unchanged.

## Lower-triplet derivative

The common construction's (4.27a) and the [Weyl input](../weyl2/action/details/complete_spectrum_input.md), (V-4.27a), explicitly lower both SU(2) indices. They give a negative connection term for $`\mathcal D_\mu L_{ij}`$ while retaining the positive upper-index connection term in (C-GC24). The R² assembled action already uses the negative lower-index term in (A.19).

The [GB component reference](../gauss_bonnet/ads5/code/references/COMPONENT_CONVENTIONS.md),
(GC24), and the assembled action's (GB09) state the upper-index expression.
The [GB quadratic action](../gauss_bonnet/ads5/quadratic_action.md) uses
(GB09) in (6.21), with coefficients collected in (6.29)–(6.30).
The [fermionic reduction](../gauss_bonnet/ads5/details/fermionic_reduction.md),
(FC1)–(FC6), (FC14)–(FC15), gives the terms in (6.31).

## Scope of the comparison

The comparison concerns the stated background Hessians through two physical fermions, their input maps, and their recorded reductions. Full nonlinear equivalence between the common-basis GB action and the component action used for Gauss–Bonnet on AdS₅ is not assumed; the selected spectrum belongs to the explicitly specified component action and AdS₅ branch. The [GB normalization definitions](../gauss_bonnet/ads5/action_inputs.md) retain that distinction.
