# R² on AdS5: local spectrum

[Notation dictionary](../notation.md).

[Study index](README.md) · [Inputs](action_inputs.md) · [Background](background.md) · [Quadratic problem](quadratic_action.md)

## Bosonic sector

$`L=L_0=2/(1+\sqrt{1-3\zeta g^2})`$, $`A_R=4-3L`$,
$`B_R=2-L`$, $`\ell_5^{-2}=g^2L^2/2`$. The generic formulas require
$`\zeta A_RB_R\ne0`$. In the paper's real-mass interval,
$`0<\zeta g^2<1/3`$ with $`\zeta g^2\ne1/4`$, one has $`\nu_R>1`$.

```math
\nu_R^2=\frac2{\zeta g^2L}-2=\frac{4-L}{2(L-1)}.
```

In the real-root table, $`\nu_R\ge0`$ only labels paired roots; both $`+,-`$ branches are retained. Negative $`\nu_R^2`$ does not support a claim of real masses and positive norm; the polynomial definition is used.

| Mode | Mass | Real local polarizations |
|---|---|---:|
| Massless graviton | $`M^2=0`$ | 5 |
| Two Maxwell channels | $`M^2=0`$ | 6 |
| Form–vector Proca channel | $`M^2\ell_5^2=\nu_R^2-1`$ | 4 |
| Light neutral scalar | $`M^2\ell_5^2=-4`$ | 1 |
| Two additional neutral scalars | $`M_\pm^2\ell_5^2=(\nu_R\pm1)^2-4`$ | 2 |
| Internally charged scalars | $`M^2\ell_5^2=\nu_R^2-4`$ | 2 |

There are 20 bosonic polarizations after solving the coupled constraints on that regular real-mass interval, including its $`A_R<0`$ portion. The separate action at $`\zeta=0`$ has 12 bosonic polarizations; the finite-coupling table is not applied there while retaining divergent roots. At $`A_R=0`$ or $`B_R=0`$, use the original critical equations, not the divided eigenfields. [Masses and eigenfields](details/masses_and_eigenfields.md).

## Fermionic characteristic data

| Theory | Source root definition | Generic real count in the source |
|---|---|---:|
| R² | $`m_R=gL/(2\sqrt2)`$; light root $`m_R`$, heavy roots $`-m_R\pm\nu_R/\ell_5`$; massless AdS gravitino | $`8+4+4+4=20`$ |

These entries retain the source action and fermion conventions. The [source-version record](source_notes.md) specifies the conventions used in this table. The signs of internal eigenvalues are paired by symplectic Majorana reality; they are not extra independent doublets.

Source: [Masses and eigenfields](details/masses_and_eigenfields.md).

## Norms, special branches and interpretation

For $`0<\tau=6\zeta g^2<3/2`$, all listed physical norms are positive.
For $`3/2<\tau<2`$, the graviton multiplet and the long vector multiplet
have negative norm, while the massless vector multiplet remains positive.
At $`\tau=2`$, the massless and massive vector channels form a Jordan pair,
as do the light spinor and one heavy spinor; the two BF scalars remain
independent. These endpoint statements are local and do not select boundary
conditions for logarithmic solutions.

| Question | Derivation |
|---|---|
| Kinetic signs and norm convention | [Reduced norms](details/kinetic_norms.md) |
| Singular kinetic coefficients and coincident roots | [Special branches](details/critical_branches.md) |
| Local masses versus boundary-admissible states | [Common stability definitions](../../common/kinetic_terms_and_stability.md) |
| Action and fermion conventions used in this table | [Component inputs](action_inputs.md) and [source definitions](source_notes.md) |
