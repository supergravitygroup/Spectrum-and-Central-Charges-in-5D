# Two derivatives + generic four-derivative theory

[Classification](action_family.md) · [Action index](action_family.md)

## Definition and action through two fermions

```math
\alpha,\beta,\zeta\ \text{free}.
```

```math
\begin{aligned}
\mathcal L_{\mathrm{gen}}^{(0)}&=\ell_{2}^{(0)} + \alpha\ell_{W}^{(0)} + \beta\ell_{\log}^{(0)} + \zeta\ell_{R}^{(0)},\\
\mathcal L_{\mathrm{gen}}^{(2)}&=\ell_{2}^{(2)} + \alpha\ell_{W}^{(2)} + \beta\ell_{\log}^{(2)} + \zeta\ell_{R}^{(2)},\\
S_{\mathrm{gen},\le2}&=\frac1{2\kappa_5^2}\int d^5x\,e\,\bigl(\mathcal L_{\mathrm{gen}}^{(0)}+\mathcal L_{\mathrm{gen}}^{(2)}\bigr).
\end{aligned}
```

Here $`e=\det e_\mu{}^a`$. Couplings are multiplied only once, as displayed above. The linked component expressions give $`\ell_A^{(0)}`$ and $`\ell_A^{(2)}`$ in the same normalization.

## Access to every term

| Building block | Bosonic part | Physical two-fermion part | Covariant core | Explicit two-fermion blocks |
|---|---|---|---|---|
| $`\ell_{2}`$ | [Formulas](two_derivative_action/bosonic.md) | [Two-fermion definition](two_derivative_action/fermionic.md) | [All blocks](two_derivative_action/covariant_core.md) | [All blocks](two_derivative_action/explicit_two_fermion.md) |
| $`\ell_{W}`$ | [Formulas](../weyl2/action/bosonic.md) | [Two-fermion definition](../weyl2/action/fermionic.md) | [All blocks](../weyl2/action/covariant_core.md) | [All blocks](../weyl2/action/explicit_two_fermion.md) |
| $`\ell_{\log}`$ | [Formulas](../log/action/bosonic.md) | [Two-fermion definition](../log/action/fermionic.md) | [All blocks](../log/action/covariant_core.md) | [All blocks](../log/action/explicit_two_fermion.md) |
| $`\ell_{R}`$ | [Formulas](../r2/action/bosonic.md) | [Two-fermion definition](../r2/action/fermionic.md) | [All blocks](../r2/action/covariant_core.md) | [All blocks](../r2/action/explicit_two_fermion.md) |

The physical two-fermion part contains contributions implicit in the covariant core as well as the explicit bilinears. Implicit contributions of hatted objects and derivatives are included using the [grading rule](fermion_order.md). Long formulas are stored once in shared building-block files; the sums on this page incorporate those files into the action definition.

## Representation and verification scope

The [shared definitions](fields_and_derivatives.md) include the source gauge, the domain $`L>0`$ and $`g\ne0`$, and the dependent connections. The source's compact supercovariant representation is retained. This page chooses no background, eliminates no auxiliary field, and makes no coupling expansion.

Source coefficients, composite-field expansions, and independent SUSY identities are tracked as separate mathematical records in the [check record](../references/component_records/02_action_family.md). The general density's one-fermion variation and explicit boundary current are derived in the [SUSY appendix](details/vector_linear_density.md).

The [general-combination AdS₅ calculation](../generic_combination/ads5/central_charges_and_massless_vectors.md) gives the central charges and massless-vector kinetic coefficients on the supersymmetric vacuum, with all three higher-derivative couplings symbolic.
