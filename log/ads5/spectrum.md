# LOG on AdS5: local spectrum

[Notation dictionary](../notation.md).

[Study index](README.md) · [Inputs](action_inputs.md) · [Background](background.md) · [Quadratic problem](quadratic_action.md)

## Bosonic sector

$`L=L_0=2/(1+\sqrt{1-\beta g^2/2})`$, $`\ell_5^{-2}=g^2L^2/2`$, $`\beta\ne0`$, $`L\ne4/3,2`$. The value $`L=1`$ denotes the zero-coupling reference.

| Mode | $`M^2`$ | Real local polarizations |
|---|---|---:|
| Massless graviton | 0 | 5 |
| Additional spin-2 mode | $`6(4-3L)/\beta`$ | 9 |
| Light scalar | $`-2g^2L^2`$ | 1 |
| Additional scalar | $`6(4-3L)/\beta`$ | 1 |
| Two Maxwell channels | 0 | 6 |
| Two mixed Proca channels | $`\lambda_+,\lambda_-`$ | 8 |
| Two traceless internal connections | $`6(2-L)/\beta`$ | 8 |
| Closed three-form channel | $`2(4-L)/\beta`$ | 6 |

$`\lambda_\pm`$ are the two roots of the following polynomial:

```math
16(L-1)^2x^2+8L^2g^2(L-1)(L-4)x
+3L^4g^4(L-4)(3L-4)=0.
```

This definition retains all symbolic dependence. Nonreal roots are not interpreted as real stable particles. The generic bosonic total is 44. [Bosonic masses and wave equations](bosonic_spectrum.md).

## Fermionic characteristic data

| Theory | Source root definition | Generic real count in the source |
|---|---|---:|
| LOG | $`t_F=igM,\ t_F^2=g^2L^2/2`$, with $`z`$ the eigenvalue of $`t_F^{-1}\mathord{\not{\nabla}}`$. Spin-3/2: $`(z+3/2)[4(L-1)(z^2-z)+3L-9]=0`$; spin-1/2: $`(2z+1)[4(L-1)(z^2+z)+3L-9]=0`$ | 44 |

These entries retain the source action and fermion conventions. The [source-version record](source_notes.md) specifies the conventions used in this table. The signs of internal eigenvalues are paired by symplectic Majorana reality; they are not extra independent doublets.

In an internal eigenspace with $`t_F=\sigma/\ell_5`$, the signed Dirac mass is $`m_D=\sigma z/\ell_5`$. Source: [Fermionic roots and signed masses](fermionic_spectrum.md).

## Norms, special branches and interpretation

| Question | Derivation |
|---|---|
| Kinetic signs and norm convention | [Reduced norms](details/kinetic_norms.md) |
| Singular kinetic coefficients and coincident roots | [Special branches](details/multiplets_and_critical_branches.md) |
| Local masses versus boundary-admissible states | [Common stability definitions](../../common/kinetic_terms_and_stability.md) |
| Action and fermion conventions used in this table | [Component inputs](action_inputs.md) and [source definitions](source_notes.md) |
