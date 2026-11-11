# Weyl² on AdS5: local spectrum

[Notation dictionary](../notation.md).

[Study index](README.md) · [Inputs](action_inputs.md) · [Background](background.md) · [Quadratic problem](quadratic_action.md)

## Bosonic sector

$`L_0=1,\ell_5^2=2/g^2`$,
$`\rho_W^2=1-6/(\alpha g^2)`$, $`\alpha g\ne0`$.

| Mode | $`M^2`$ | Real local polarizations |
|---|---|---:|
| Massless graviton | 0 | 5 |
| Additional spin-2 mode | $`-3g^2/2-3/\alpha`$ | 9 |
| Light neutral scalar | $`-2g^2`$ | 1 |
| Additional neutral scalar | $`-3g^2/2-3/\alpha`$ | 1 |
| Two Maxwell channels | 0 | 6 |
| Two mixed Proca channels | $`g^2(\rho_W^2\pm2\rho_W)/2`$ | 8 |
| Constrained form channel | $`g^2/2-3/\alpha`$ | 6 |
| Two internal-connection channels | $`-3/\alpha`$ | 8 |

The generic total is 44. At $`\alpha g^2=-2,6`$ and related mass/rank degeneracies, the generic eigenmode projectors require separate treatment. [Physical operators](details/physical_operators.md) and [kinetic norms](details/kinetic_norms.md).

## Fermionic characteristic data

| Theory | Source root definition | Generic real count in the source |
|---|---|---:|
| Weyl² | Internal mass matrix $`m_W=igJ/(2\sqrt2)`$, $`m_W^2=g^2/8`$. Spin-3/2: $`-3m_W,(1\pm2\rho_W)m_W`$; spin-1/2: $`-m_W,-(1\pm2\rho_W)m_W`$ | $`8+12+12+4+4+4=44`$ |

These entries retain the source action and fermion conventions. The [source-version record](source_notes.md) specifies the conventions used in this table. The signs of internal eigenvalues are paired by symplectic Majorana reality; they are not extra independent doublets.

In this row J is the source internal complex structure. Source: [Fermionic spectrum](fermionic_spectrum.md).

## Norms, special branches and interpretation

| Question | Derivation |
|---|---|
| Kinetic signs and norm convention | [Reduced norms](details/kinetic_norms.md) |
| Singular kinetic coefficients and coincident roots | [Special branches](details/critical_branches.md) |
| Local masses versus boundary-admissible states | [Common stability definitions](../../common/kinetic_terms_and_stability.md) |
| Action and fermion conventions used in this table | [Component inputs](action_inputs.md) and [source definitions](source_notes.md) |
