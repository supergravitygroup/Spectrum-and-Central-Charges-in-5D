# Gauss–Bonnet combination in the common action basis


The **Gauss–Bonnet on AdS₅** spectrum uses the component action specified in the following references. Read its [complete component expression](gb_splus_action.md), [construction](details/gb_splus_construction.md), and [normalization and input versions](../ads5/action_inputs.md) together. These specify the bosonic and physical two-fermion terms used in that Hessian.

The formulae below define the GB combination in the **common action basis**. The common-basis coupling and the coupling used for Gauss–Bonnet on AdS₅ are kept distinct; a pure-curvature comparison is not a complete component version map.

[Classification](../../common/action_family.md) · [Action index](../../common/action_family.md)

## Definition and action through two fermions

```math
(\alpha,\beta,\zeta)=(\lambda,2\lambda,0),\quad\lambda\ \text{free}.
```

```math
\begin{aligned}
\mathcal L_{\mathrm{GB}}^{(0)}&=\ell_{2}^{(0)} + \lambda\ell_{G}^{(0)},\\
\mathcal L_{\mathrm{GB}}^{(2)}&=\ell_{2}^{(2)} + \lambda\ell_{G}^{(2)},\\
S_{\mathrm{GB},\le2}&=\frac1{2\kappa_5^2}\int d^5x\,e\,\bigl(\mathcal L_{\mathrm{GB}}^{(0)}+\mathcal L_{\mathrm{GB}}^{(2)}\bigr).
\end{aligned}
```

Here $`e=\det e_\mu{}^a`$. Couplings are multiplied only once, as displayed above. The linked component expressions give $`\ell_A^{(0)}`$ and $`\ell_A^{(2)}`$ in the same normalization.

## Access to every term

| Building block | Bosonic part | Physical two-fermion part | Covariant core | Explicit two-fermion blocks |
|---|---|---|---|---|
| $`\ell_{2}`$ | [Formulas](../../common/two_derivative_action/bosonic.md) | [Two-fermion definition](../../common/two_derivative_action/fermionic.md) | [All blocks](../../common/two_derivative_action/covariant_core.md) | [All blocks](../../common/two_derivative_action/explicit_two_fermion.md) |
| $`\ell_{G}`$ | [Formulas](bosonic.md) | [Two-fermion definition](fermionic.md) | [All blocks](covariant_core.md) | [All blocks](explicit_two_fermion.md) |

The physical two-fermion part contains contributions implicit in the covariant core as well as the explicit bilinears. Implicit contributions of hatted objects and derivatives are included using the [grading rule](../../common/fermion_order.md). Long formulas are stored once in shared building-block files; the sums on this page incorporate those files into the action definition.

## Applying the GB combination to every field

```math
\begin{aligned}
\mathcal B_G&=\mathcal B_W+2\mathcal B_{\log},\\
\mathcal U_G&=\mathcal U_W+2\mathcal U_{\log},\\
\mathcal V_G&=\mathcal V_W+2\mathcal V_{\log},\\
\ell_G^{(q)}&=\ell_W^{(q)}+2\ell_{\log}^{(q)},\qquad q=0,2.
\end{aligned}
```

The [GB building-block files](invariant.md) list this combination itself. Its pure-curvature coefficient is $`(R_{abcd}R^{abcd}-4R_{ab}R^{ab}+R^2)/8`$. Coefficient matching is shown in the [derivation appendix](../../common/details/action_normalizations.md). The point $`\lambda=0`$ belongs to the defined family; no division by $`\lambda`$ is made.

## Representation and verification scope

The [shared definitions](../../common/fields_and_derivatives.md) include the source gauge, the domain $`L>0`$ and $`g\ne0`$, and the dependent connections. The source's compact supercovariant representation is retained. This page chooses no background, eliminates no auxiliary field, and makes no coupling expansion.

Source coefficients, composite-field expansions, and independent SUSY identities are tracked as separate mathematical records in the [check record](../../references/component_records/02_action_family.md). The general density's one-fermion variation and explicit boundary current are derived in the [SUSY appendix](../../common/details/vector_linear_density.md).

## Selected AdS5 calculation

The [Gauss–Bonnet on AdS₅ spectrum](../ads5/README.md) uses the action normalization specified in its [input record](../ads5/action_inputs.md).
