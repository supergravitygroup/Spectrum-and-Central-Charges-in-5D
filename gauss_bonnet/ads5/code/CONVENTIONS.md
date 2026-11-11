# Working conventions and symbols

This summary records the accepted inputs `GB-FERMION-SPECTRUM-CONVENTIONS-v1` and `GB-FERMION-ACTION-0+2-v1`. See the [full conventions](references/CONVENTIONS.md) and [component definitions](references/COMPONENT_CONVENTIONS.md). It does not declare a new convention lock or source certificate. The relation to the shared paper notation is documented in the [study input record](../action_inputs.md).

| Topic | Definition in this package |
|---|---|
| Indices | $`a,b,\mu,\nu=0,\ldots,4`$; $`i,j=1,2`$ |
| Metric and orientation | $`\eta=(-,+,+,+,+)`$, $`\epsilon^{01234}=+1`$, $`\epsilon_{01234}=-1`$ |
| Curvature | $`R_{\mu\nu\rho\sigma}=k(g_{\mu\rho}g_{\nu\sigma}-g_{\mu\sigma}g_{\nu\rho})`$; $`R_{\mu\nu}=4kg_{\mu\nu}`$, $`R=20k`$ |
| AdS radius | $`k=-\mathcal L^{-2}`$; $`\mathcal L`$ is the radius, $`L`$ the compensator field |
| Clifford algebra | $`\{\gamma^a,\gamma^b\}=2\eta^{ab}`$, $`\gamma^{01234}=i`$; unit-weight antisymmetrization |
| Majorana bar | $`\bar\zeta=\zeta^T\mathsf C`$, $`\overline{i\zeta}=i\bar\zeta`$; linear transpose, not Hermitian conjugation |
| SU(2) | NW–SE, $`\varepsilon_{12}=\varepsilon^{12}=1`$; $`X^i=\varepsilon^{ij}X_j`$, $`X_i=X^j\varepsilon_{ji}`$ |
| Doublet generator | $`J=\left(\begin{smallmatrix}0&-1\\1&0\end{smallmatrix}\right)`$, $`J^2=-1`$; $`\delta_{ij}\bar A^i B^j=-\bar A J B`$ |
| Action | $`S=(2\kappa_5^2)^{-1}\int e[\ell_{2\partial}+\lambda_{\rm GB}(-2\ell_{W,OP}-4\ell_{\log})]_{\le2}`$ |
| Pure GB curvature term | $`-\lambda_{\rm GB}(Riem^2-4Ric^2+R^2)/4`$ |
| Expansion | $`S=S^{(0)}+tS^{(1)}+t^2S^{(2)}+O(t^3)`$; $`S^{(2)}`$ is the Taylor coefficient |
| Equality | $`\doteq`$: equality within the stated total-derivative and fermion-order scope |
| Fermion variation | Left variation of independent Grassmann-odd components; the bar is not an independent field |

The source gauge is $`\sigma=1,b_\mu=0,\psi^i=0,L^{ij}=\delta^{ij}L/\sqrt2`$. The dilatino $`\psi^i`$ differs from the gravitino $`\psi_\mu^i`$. Gauge conditions are applied after expanding covariant derivatives: $`\mathcal D\psi\vert_{\psi=0}`$ need not vanish, and a constant compensator can produce connection mass terms.

## Field and branch dictionary

| Symbol / Python name | Meaning |
|---|---|
| `L,N,k,g,lam` | Compensator, auxiliary scalar, curvature, gauging, and $`\lambda_{\rm GB}`$ before branch substitution |
| `x,a,c,m` | $`x=L_0`$, $`a=\lambda_{\rm GB}g^2`$, $`c=2-x`$, $`m=gx/(2\sqrt2)`$ |
| $`h_{\mu\nu},\ell,n`$ | Fluctuations of the metric, $`L`$, and $`N`$ |
| $`A,b,e_3`$ | One-, two-, and three-form potential fluctuations |
| $`G,H,p`$ | Their derived field strengths; Hodge factors are in Step 6 (6.19) |
| $`v,v'`$ | Trace and traceless R-symmetry connection fluctuations |
| $`\Psi_a,\zeta`$ | Independent gravitino and compensator spinor fluctuations |
| $`H_{\mu\nu},\Upsilon_a,Q`$ | Diagonal metric, gravitino, and local dual Maxwell potential |
| $`r,\mathcal G^L`$ | Linear scalar curvature and cosmological Einstein operator, Step 6 (6.14) |
| $`s=\pm1`$ | Eigenvalue of $`iJ`$; signed equation $`(\not\nabla+\mu_s)q_s=0`$ |
| `exponent` in the operator code | Eigenvalue of $`z\partial_z`$, distinct from the internal sign $`s=\pm1`$ |

Physical source-frame dimensions are $`[g]=[\nabla]=1`$, $`[k]=2`$, $`[L]=[x]=[a]=[c]=0`$, $`[N]=[G]=[H]=[p]=[v]=[v']=1`$, $`[\Psi]=[\zeta]=1/2`$, $`[\lambda_{\rm GB}]=-2`$, $`[\kappa_5^2]=-3`$. The bracketed action density has dimension two. These dimensions are distinct from pre-gauge Weyl weights.

`inputs/symbols.py` assumes only $`x>0`$. The conditions $`x<2`$ and $`c\ne0`$ belong to the reduction domain. The raw coefficients, rather than divided reduction formulas, describe the endpoint.
