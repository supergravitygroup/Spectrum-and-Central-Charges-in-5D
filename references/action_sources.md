# Use of the actions in the spectrum paper

The common density is defined by

```math
\ell_{\le2}=\ell_{2,\le2}+\alpha\ell_{W,\le2}
+\beta\ell_{\log,\le2}+\zeta\ell_{R,\le2}
```

The [theory classification](../common/action_family.md) and [complete component index](../common/action_family.md) fix the action representation. The bosonic body, explicit two-fermion monomials, and implicit two-fermion contributions in covariant objects are used together; counting explicit spinors alone is insufficient.

| Action | Local construction input | Scope of literature use |
|---|---|---|
| Two derivatives | `two_derivative_construction.md` and the shared composite definitions | Coomans–Ozkan supplies the gauged off-shell construction; the coefficient map to the current representation is a local record. |
| Weyl² | `weyl2_construction.md`, `weyl2_map.md` | Established curvature-squared invariants and component constructions are cited. |
| LOG | `log_construction.md`, `log_covariant_rules.md` | The LOG multiplet/superspace construction and component maps are linked to the relevant work of Gold and collaborators. |
| R² | `r2_construction.md`, `linear_vector_map.md` | Vector–linear and R²-invariant sources are used. |
| GB | Weyl² + 2 LOG | The linear combination applies to every component; the literature normalization is converted separately. |

These names are resolved in the [local source index](component_records/02_action_sources.json) and [additional map record](component_records/02_susy_check_record.json). Bibliographic details and equation matching are given in the manuscript's [bibliography](bibliography.md). A published construction does not automatically verify a local change to a fermionic coefficient.

The [fermionic input correspondence](fermionic_input_correspondence.md)
identifies the 2016-map component expressions, quadratic actions and mixing
reductions used by the spectra.
