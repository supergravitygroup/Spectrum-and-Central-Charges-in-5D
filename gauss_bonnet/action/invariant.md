# Gauss–Bonnet combination

This building block is the combination $`\ell_G=\ell_W+2\ell_{\log}`$. The source normalization is retained with pure-curvature coefficient $`\mathcal G/8`$; no additional unit normalization is chosen.

The symbol $`\mathcal U_A`$ denotes the covariant core without explicit fermions, $`\mathcal V_A`$ the blocks with two explicit fermions, and $`\mathcal B_A`$ the physical bosonic density. The symbols $`\Pi_0`$ and $`\Pi_2`$ are physical fermion-degree projections.

```math
\begin{aligned}
\ell_{G}^{(0)}&=\mathcal B_{G}=\Pi_0\mathcal U_{G},\\
\ell_{G}^{(2)}&=\Pi_2\mathcal U_{G}+\Pi_2\mathcal V_{G},\\
\ell_{G,\le2}&=\mathcal B_{G}+\ell_{G}^{(2)}=\Pi_{\le2}\bigl(\mathcal U_{G}+\mathcal V_{G}\bigr).
\end{aligned}
```

This definition includes fermions implicit in supercovariant objects. Expressions use the compact supercovariant representation of the sources; they are not claimed to be fully expanded monomial lists in fundamental fields for every connection and ordered derivative. No completion at higher fermion orders is claimed.

| Content | Explicit formulas |
|---|---|
| All blocks of the bosonic density | [Bosonic](bosonic.md) |
| All core blocks, including implicit fermions | [Covariant core](covariant_core.md) |
| All blocks containing two explicit fermions | [Explicit two-fermion part](explicit_two_fermion.md) |
| Complete definition of the physical two-fermion part | [Fermionic density](fermionic.md) |

The [shared definitions](../../common/fields_and_derivatives.md), [grading rules](../../common/fermion_order.md), and [source/check scope](../../references/component_records/02_action_family.md) form part of this expression. The invariant is defined without its coupling; the relevant theory action supplies that coefficient once.
