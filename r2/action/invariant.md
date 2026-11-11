# R-squared building block

The symbol $`\mathcal U_A`$ denotes the covariant core without explicit fermions, $`\mathcal V_A`$ the blocks with two explicit fermions, and $`\mathcal B_A`$ the physical bosonic density. The symbols $`\Pi_0`$ and $`\Pi_2`$ are physical fermion-degree projections.

```math
\begin{aligned}
\ell_{R}^{(0)}&=\mathcal B_{R}=\Pi_0\mathcal U_{R},\\
\ell_{R}^{(2)}&=\Pi_2\mathcal U_{R}+\Pi_2\mathcal V_{R},\\
\ell_{R,\le2}&=\mathcal B_{R}+\ell_{R}^{(2)}=\Pi_{\le2}\bigl(\mathcal U_{R}+\mathcal V_{R}\bigr).
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
