# Action inputs and convention correspondence

Each spectrum is defined by the component input used in its quadratic action. The table identifies that input directly.

| Spectrum | Component input | Quadratic action | Convention note |
|---|---|---|---|
| R² on AdS5 | [Action and fields](../r2/action/details/spectrum_input.md) | [AdS5 Hessian](../r2/ads5/quadratic_action.md) | Source-local coupling and field names are retained in the derivation. |
| Weyl² on AdS5 | [Spectrum input](../weyl2/action/details/spectrum_input.md), [complete component expression](../weyl2/action/details/complete_spectrum_input.md) | [AdS5 Hessian](../weyl2/ads5/quadratic_action.md) | The component action and signed fermion roots use the stated Weyl conventions. |
| LOG on AdS5 | [Component input](../log/action/details/spectrum_input.md) | [AdS5 Hessian](../log/ads5/quadratic_action.md) | The source uses its local LOG coupling. |
| Gauss–Bonnet on AdS₅ | [Component action](../gauss_bonnet/action/gb_splus_action.md), [input convention](../gauss_bonnet/ads5/action_inputs.md) | [Hessian](../gauss_bonnet/ads5/quadratic_action.md) | [Two-derivative input qualifications](../common/two_derivative_action/details/gb_input_qualifications.md) specify the mass sign and algebraic mixing. |

## Two-derivative fermion inputs

The [equation-level correspondence](fermionic_input_correspondence.md)
identifies the 2016-map component expressions used by the spectra and the
SU(2) index-lowering convention. The
[Gauss–Bonnet input definitions](../gauss_bonnet/ads5/action_inputs.md)
state its action and coupling normalization.

## Norms and boundary interpretation

The GB calculation uses its stated two-derivative kinetic reference. Formal bilinear coefficients have the physical norm interpretation appropriate to the norm definitions of each calculation. Local characteristic roots are distinguished from a global spectrum with specified boundary conditions.

## Scope of the GB component comparison

The [component method](../gauss_bonnet/ads5/source_notes.md) distinguishes its fixed-frame matrix comparison from the symbolic parameter-restoration argument. The former alone is not an unrestricted symbolic evaluation of the component operator. The fixed values in that comparison do not belong to the symbolic verification route.

The [verification scope](verification_scope.md) states the identities and
numerical calculations supporting these reductions.
