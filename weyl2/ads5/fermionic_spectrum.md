# Weyl²: fermionic spectrum on AdS5

[Notation dictionary](../notation.md).

[Reading guide](README.md) · [Definitions of masses, operators and eigenfields](details/physical_operators.md). The equation labels and local symbols below follow the action conventions specified for this theory.

<a id="112-fermionic-table"></a>

### Fermionic table

First-order equations retain the **signed** Dirac roots of the [physical-operator reduction](details/physical_operators.md).
Squaring them alone does not select the same physical branch.

```math
\mathord{\not{\nabla}}^2=\Box+\frac{5g^2}{2}
\quad\text{(spinor)},\qquad
\mathord{\not{\nabla}}^2=\Box+3g^2
\quad\text{(transverse gamma-traceless vector-spinor)}.
```

Thus, on the $`\mathord{\not{\nabla}}\Phi=\mu\Phi`$ branch,

```math
\left(\Box+\frac{5g^2}{2}-\mu^2\right)X=0,\qquad
(\Box+3g^2-\mu^2)\widehat\Psi^{TT}=0
```


| Mode | Signed Dirac eigenvalue | Generic local polarizations |
|---|---|---:|
| $`\widehat\Psi_0`$ | $`-3m`$ | $`8`$ |
| $`\widehat\Psi_+`$ | $`(1+2\rho)m`$ | $`12`$ |
| $`\widehat\Psi_-`$ | $`(1-2\rho)m`$ | $`12`$ |
| $`\zeta_{\rm s}`$ | $`-m`$ | $`4`$ |
| $`X_+`$ | $`-(1+2\rho)m`$ | $`4`$ |
| $`X_-`$ | $`-(1-2\rho)m`$ | $`4`$ |

```math
N_F=8+12+12+4+4+4=44.
```

All finite-$`\alpha`$ roots are retained. Growth of some masses in the small-$`\alpha`$ limit does not justify removing those modes from the total finite-$`\alpha`$ theory.

<a id="bolum-12"></a>

