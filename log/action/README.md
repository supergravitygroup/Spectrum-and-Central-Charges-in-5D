# Two derivatives + LOG theory

[Classification](../../common/action_family.md) · [Action index](../../common/action_family.md)

## Definition and action through two fermions

```math
\alpha=\zeta=0,\quad\beta\ \text{free}.
```

```math
\begin{aligned}
\mathcal L_{\log}^{(0)}&=\ell_{2}^{(0)} + \beta\ell_{\log}^{(0)},\\
\mathcal L_{\log}^{(2)}&=\ell_{2}^{(2)} + \beta\ell_{\log}^{(2)},\\
S_{\log,\le2}&=\frac1{2\kappa_5^2}\int d^5x\,e\,\bigl(\mathcal L_{\log}^{(0)}+\mathcal L_{\log}^{(2)}\bigr).
\end{aligned}
```

Here $`e=\det e_\mu{}^a`$. Couplings are multiplied only once, as displayed above. The linked component expressions give $`\ell_A^{(0)}`$ and $`\ell_A^{(2)}`$ in the same normalization.

## Access to every term

| Building block | Bosonic part | Physical two-fermion part | Covariant core | Explicit two-fermion blocks |
|---|---|---|---|---|
| $`\ell_{2}`$ | [Formulas](../../common/two_derivative_action/bosonic.md) | [Two-fermion definition](../../common/two_derivative_action/fermionic.md) | [All blocks](../../common/two_derivative_action/covariant_core.md) | [All blocks](../../common/two_derivative_action/explicit_two_fermion.md) |
| $`\ell_{\log}`$ | [Formulas](bosonic.md) | [Two-fermion definition](fermionic.md) | [All blocks](covariant_core.md) | [All blocks](explicit_two_fermion.md) |

The physical two-fermion part contains contributions implicit in the covariant core as well as the explicit bilinears. Implicit contributions of hatted objects and derivatives are included using the [grading rule](../../common/fermion_order.md). Long formulas are stored once in shared building-block files; the sums on this page incorporate those files into the action definition.

## Representation and verification scope

The [shared definitions](../../common/fields_and_derivatives.md) include the source gauge, the domain $`L>0`$ and $`g\ne0`$, and the dependent connections. The source's compact supercovariant representation is retained. This page chooses no background, eliminates no auxiliary field, and makes no coupling expansion.

Source coefficients, composite-field expansions, and independent SUSY identities are tracked as separate mathematical records in the [check record](../../references/component_records/02_action_family.md). The general density's one-fermion variation and explicit boundary current are derived in the [SUSY appendix](../../common/details/vector_linear_density.md).

## Component construction and spectrum conventions

- [Component construction](details/construction.md).
- [Action conventions used for the spectrum](details/spectrum_input.md).
- [Primary-to-BF computational construction](../../computations/log_fermionic/README.md),
  including ordered descendants and coefficient ledgers.
