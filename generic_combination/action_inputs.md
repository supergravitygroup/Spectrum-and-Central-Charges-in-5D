# Action inputs and normalization dictionary

The component action uses the source normalizations of the
[common action family](../common/action_family.md); its precise component
versions are identified in [the action record](action.md). The background
projection uses the bosonic parts. The action retains an independent two-derivative coefficient:

```math
\mathcal L=e\bigl(c_2\ell_2+\alpha\ell_W+\beta\ell_{\log}
+\lambda\ell_{R^2}\bigr).
```

The [full bosonic expression](action.md), labelled
`GENERIC-COMBINATION-BOSONIC-v1`, records every term and composite. The
[common theory action](../common/generic_action.md) also supplies the physical
two-fermion formulation; a bosonic action alone does not supply a generic
fermionic Hessian.

| Component-action notation | Common action notation | Interpretation |
| --- | --- | --- |
| $`c_2`$ | Coefficient of $`\ell_2`$ is explicitly $`1`$ in the common family | The component action retains this coefficient; the paper's AdS5 calculations use $`c_2=1`$ |
| $`\alpha`$ | $`\alpha`$ | Weyl block in OP normalization |
| $`\beta`$ | $`\beta`$ | LOG block |
| $`\lambda`$ | $`\zeta`$ | $`R^2`$ coefficient |
| $`(\alpha,\beta,\lambda)=(-2\lambda_{\rm GB},-4\lambda_{\rm GB},0)`$ | GB spectrum normalization | Relation to the specific GB action record |

The pure-curvature coefficients are

```math
\frac\alpha8R_{abcd}R^{abcd}
-\frac{\alpha+\beta}{6}R_{ab}R^{ab}
+\left(\frac{\alpha+\beta}{24}+\frac\lambda4\right)R^2.
```

Thus the common Gauss–Bonnet line is $`\beta=2\alpha,\lambda=0`$.
This coefficient identity does not identify generic kinetic operators or
fermionic spectra. The dimensions are

```math
[L]=[c_2]=0,\qquad [N]=[g]=1,\qquad
[\alpha]=[\beta]=[\lambda]=-2.
```

The compact action densities are bulk representatives with the boundary
transfers specified in their source derivations. Boundary counterterms and a
global boundary variational principle are additional data.

The shared [conventions](../common/conventions.md) leave spacetime orientation
symbolic. The lower-triplet derivative is obtained by NW–SE lowering,

```math
\nabla_\mu L_{ij}=\partial_\mu L_{ij}
-2V_{\mu(i}{}^kL_{j)k}.
```

The action
uses the minus sign, with its derivation in the
[two-derivative component record](../common/two_derivative_action/details/construction.md).
No general connection-profile or quadratic-operator result is inferred from
this convention correction. See the [scope note](source_notes.md).
