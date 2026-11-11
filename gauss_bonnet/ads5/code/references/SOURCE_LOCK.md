# Component-action inputs and normalization

The [input manifest](../inputs/action_sources.json) lists the local component
expressions used in the calculation. The action is retained through physical
fermion order two, including the implicit fermions in supercovariant objects.

| Input | Role |
|---|---|
| [Weyl linear map](../../../../computations/weyl_fermionic/inputs/reference/notes/04_full_fermionic_weyl_linear_map.md) and [Weyl density](../../../../weyl2/action/details/construction.md) | Improved vector multiplet and Weyl invariant in the stated OP normalization |
| [Two-derivative action](../../../../common/two_derivative_action/details/construction.md) | Component density and the 2016 linear-to-vector map |
| [LOG action](../inputs/action_sources/04_02_fermionic_log_action.md), [covariant seed](../inputs/action_sources/05_covariant_seed.md) and [explicit bilinears](../inputs/action_sources/06_explicit_sum.md) | Complete retained LOG density |
| [Bosonic definition-based derivation](../inputs/action_sources/10_weyl_log_from_definitions.tex) | Weyl/LOG normalization and bosonic boundary representative |
| [Component conventions](COMPONENT_CONVENTIONS.md) | Fields, curvatures, ordered derivatives and Majorana conventions |

The complete-primary comparison GB16–GB20 in the
[GB action](../../../action/gb_splus_action.md) fixes
$`\ell_{W,\mathrm{target}}=-2\ell_{W,\mathrm{OP}}`$ and the coefficient
$`-4\ell_{\log}`$ in the GB combination. These factors apply to the complete
retained component expressions and their ordinary-current density slots.
The two-derivative normalization is fixed separately by its Einstein term.

The published multiplet and invariant constructions are cited in the
[repository bibliography](../../../../references/bibliography.md).
The [equation-to-code map](../SOURCE_MAP.md) identifies the corresponding
background expansion and physical spectrum calculation.
