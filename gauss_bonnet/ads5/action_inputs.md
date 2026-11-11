# Gauss–Bonnet on AdS₅: action and normalization

[Notation dictionary](../notation.md).

The analysis selects the AdS₅ branch that continuously approaches the two-derivative AdS₅ vacuum as the Gauss–Bonnet coupling tends to zero. The calculation uses

```math
S=(2\kappa_5^2)^{-1}\int e[\ell_{2\partial}+\lambda_{\rm GB}(-2\ell_{W,OP}-4\ell_{\log})]_{\le2}.
```

This expression is transcribed from the [package convention record](code/CONVENTIONS.md). The [full action](../action/gb_splus_action.md), [assembled expression](code/outputs/action.md), source lock, and [coefficient ledger](code/outputs/action_coefficient_ledger.md) supply the bosonic and physical two-fermion terms, including implicit supercovariant contributions.

| Notation issue | Convention used |
|---|---|
| GB coupling | The coupling used for Gauss–Bonnet on AdS₅ is `lambda_GB`; its pure-curvature term is `-lambda_GB*GB/4`. The shared action classification uses `lambda*GB/8`. These labels are not interchanged. |
| Complete component inputs | The GB input set governs this spectrum; the [shared GB action appendix](../action/common_basis.md) remains the common-basis classification. A pure-curvature coefficient comparison alone is not a full fermionic version map. |
| Scalar and radius | `x=L0` is the background compensator. The source radius is `mathcal L`, not the scalar field `L`. |
| Fermion symbol | `zeta` in the GB notes is a spinor, not the R² coupling of the shared narrative. |
| Orientation and bar | The source chooses positive epsilon orientation and a linear Majorana bar. These source choices are recorded in [CONVENTIONS](code/CONVENTIONS.md), without changing the parent convention authority. |
| Two-derivative correction | Preserve [TWO_DERIVATIVE_QUALIFICATIONS](../../common/two_derivative_action/details/gb_input_qualifications.md) with the frozen input version. |
