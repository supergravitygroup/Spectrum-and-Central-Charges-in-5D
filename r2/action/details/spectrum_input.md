# R² action and conventions used for the spectra

[Reading guide](../README.md). The equation labels and local symbols below follow the action conventions specified for this theory.

<a id="2-fixing-the-total-action-and-conventions"></a>

## Fixing the total action and conventions

<a id="21-field-domain-and-density"></a>

### Field domain and density

The gauge conditions already imposed in the inputs are retained:
```math
\sigma=1,\qquad\psi^i=0,\qquad b_\mu=0,\qquad
L_{ij}=\frac{L}{\sqrt2}\delta_{ij},\qquad L>0
```
Here $`\psi^i`$ is the defining dilatino, $`\psi_\mu{}^i`$ the gravitino, $`\varphi^i`$ the linear-multiplet fermion, and $`\phi_\mu{}^i`$ the dependent $`S`$ connection.

```math
\eta_{ab}=\mathop{\mathrm{diag}}\nolimits(-,+,+,+,+),\qquad
e=\det e_\mu{}^a=\sqrt{-g},\qquad
\{\gamma^a,\gamma^b\}=2\eta^{ab}.
```
Antisymmetrization has unit weight; no additional $`1/2`$ is inserted in $`\gamma\cdot T=\gamma^{ab}T_{ab}`$.

<a id="22-spinor-signs"></a>

### Spinor signs

```math
\epsilon_{12}=\epsilon^{12}=1,\qquad
X^i=\epsilon^{ij}X_j,\qquad X_i=X^j\epsilon_{ji}.
```
The sign between the open-index and contracted flips is fixed by
```math
\begin{aligned}
\bar X^i\gamma_{(n)}Y_i
&=\epsilon_{ji}\bar X^i\gamma_{(n)}Y^j
=t_n\epsilon_{ji}\bar Y^j\gamma_{(n)}X^i\\
&=-t_n\bar Y^j\gamma_{(n)}X_j,
\end{aligned}
```
```math
t_0=t_1=t_4=t_5=+1,\qquad t_2=t_3=-1
```
The bar is a Majorana transpose linear in coefficients; $`i`$ is not complex-conjugated. This agrees with the formal transpose $`\sharp`$ used later and is not identified with a Hermitian adjoint.

<a id="23-forms-epsilon-and-curvature-conversions"></a>

### Forms, epsilon, and curvature conversions

```math
G=dC,\qquad H=dB+\frac12C\wedge G+\frac g2E_3,
```
```math
\widehat G_{\mu\nu}=G_{\mu\nu}+\frac i2\bar\psi_{[\mu}\psi_{\nu]},\qquad
\widehat H_{\mu\nu\rho}=H_{\mu\nu\rho}
-\frac34\bar\psi_{[\mu}\gamma_\nu\psi_{\rho]}.
```
Under the gauge transformations
```math
\delta C=d\alpha,\quad\delta E_3=d\Lambda_2,\quad
\delta B=d\Lambda_1-\frac12\alpha G-\frac g2\Lambda_2
```
we have
```math
\delta H=-\frac12d\alpha\wedge G-\frac12\alpha\,dG
-\frac g2d\Lambda_2+\frac12d\alpha\wedge G+\frac g2d\Lambda_2=0.
```

The coordinate epsilon tensor is distinguished from the density symbol:
```math
\epsilon^{\mu\nu\rho\sigma\lambda}=e\varepsilon^{\mu\nu\rho\sigma\lambda},
\quad
\varepsilon_{a_1\cdots a_n b_1\cdots b_p}
\varepsilon^{a_1\cdots a_n c_1\cdots c_p}
=-n!p!\delta_{[b_1}^{c_1}\cdots\delta_{b_p]}^{c_p}.
```
No numerical orientation is assigned. Since $`H^{edc}=-H^{cde}`$, the apparently different $`T`$ definitions in the two sources match
```math
T_{ab}=\frac18\left(\widehat G_{ab}
+\frac16\varepsilon_{abcde}\widehat H^{cde}\right)
```
No additional field rescaling is required.

In the presence of torsion, affine and tangent Ricci contractions are related by
```math
R^{\mathrm{aff}}_{bd}=R_{db}(\omega),\qquad
\eta^{bd}R^{\mathrm{aff}}_{bd}=R(\omega)
```
The scalar-curvature sign is unchanged; Ricci symmetry is not assumed in advance.

The connection term of $`T`$ with a lowered Lorentz index is
```math
\begin{aligned}
\partial_\mu T_{ab}-\omega_\mu{}^c{}_aT_{cb}-\omega_\mu{}^c{}_bT_{ac}
&=\partial_\mu T_{ab}+2\omega_\mu{}^c{}_{[a}T_{b]c}.
\end{aligned}
```
The common supercovariant derivative is used with this sign. $`\mathcal D`$ is not replaced by the Levi-Civita derivative alone. The $`\Box_cL_{ij}`$ operators of the triplet and the $`\Box_c\rho'`$ operators of the vector scalar have different weights and representations.

<a id="24-coefficients-and-composite-map"></a>

### Coefficients and composite map

Let $`\mathcal L=(L_{ij},\varphi^i,E_3,N)`$ be the linear multiplet, $`\mathcal V'_{\mathrm{lin}}`$ the primed vector constructed from it, and $`\mathcal V`$ the defining vector. Denoting the density of the first source in its field-strength representation by
```math
\begin{aligned}
\mathcal B_F(\mathcal V,\mathcal L)
={}&Y^{ij}L_{ij}+i\bar\lambda^i\varphi_i
-\frac12\bar\psi_a{}^i\gamma^a\lambda^jL_{ij}
+\frac12F_{\mu\nu}E^{\mu\nu}\\
&+\rho\left(N+\frac12\bar\psi_a{}^i\gamma^a\varphi_i
+\frac i4\bar\psi_a{}^i\gamma^{ab}\psi_b{}^jL_{ij}\right)
\end{aligned}
```
the total input is summarized as
```math
\boxed{
S^{\leq2}=\int d^5x\,e\,
\left\{-2\mathcal B_F(\mathcal V'_{\mathrm{lin}},\mathcal L)
-4g\mathcal B_F(\mathcal V,\mathcal L)
+\lambda_{R^2}\mathcal I_{R^2}^{\mathrm{source}}\right\}_{\leq2}
}
```
$`\mathcal I_{R^2}^{\mathrm{source}}`$ is the full expression (R2) of the second input as substituted in `action.md` §8; it is not replaced with another R² invariant.

```math
\rho_{\mathrm{eff}}=\rho'+2g,\quad
\lambda_{\mathrm{eff}}=\lambda',\quad
Y_{\mathrm{eff},ij}=Y'_{ij}-g^2L_{ij}.
```
This effective combination belongs to the two-derivative block. The primed vector of the R² input is $`\mathcal V'_{\mathrm{lin}}`$; the shift $`\rho'\to\rho'+2g`$ is not carried into the R² sector.

<a id="25-boundary-representative-510"></a>

### Boundary representative (5.10)

```math
E^{\mu\nu}=-\frac1{12}\varepsilon^{\mu\nu\rho\sigma\lambda}E_{\rho\sigma\lambda},
\qquad
A'_\mu=\frac2L E_\mu+\sqrt2V_\mu
-\frac{L_{ij}}{L^3}\bar\varphi^i\gamma_\mu\varphi^j
-\frac iL\bar\varphi^i\psi_{\mu i}.
```
```math
\begin{aligned}
A_\mu\partial_\nu(eE^{\mu\nu})
&=\partial_\nu(eA_\mu E^{\mu\nu})
-(\partial_\nu A_\mu)eE^{\mu\nu}\\
&=\frac e2F_{\mu\nu}E^{\mu\nu}
-\frac1{12}\partial_\nu
 (e\varepsilon^{\mu\nu\rho\sigma\lambda}A_\mu E_{\rho\sigma\lambda}).
\end{aligned}
```
With source coefficient $`-2`$ and $`A=A'+2gC`$,
```math
\boxed{
S_{2\partial}^{\mathrm{pot}}-S_{2\partial}^{F}
=\frac16\int_{\partial M}d\Sigma_\nu\,
e\varepsilon^{\mu\nu\rho\sigma\lambda}
(A'_\mu+2gC_\mu)E_{\rho\sigma\lambda}.}
```
The total retains (5.10); this difference is neither automatically added nor set to zero. Moreover, the full bridge in the potential BF term is
```math
P^a=E^a+\frac i2\bar\psi_b\gamma^{ba}\varphi
+\frac14\bar\psi_b{}^i\gamma^{abc}\psi_c{}^jL_{ij}
```
so $`-4gC_aP^a`$ cannot be reduced to $`-4gC_aE^a`$ alone. This explains the missing two-fermion contribution in the alternative expression (5.11) of the first source.

