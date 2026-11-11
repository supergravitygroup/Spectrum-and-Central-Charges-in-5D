# Weyl² action and conventions used for the AdS5 spectrum

[Reading guide](../README.md). The equation labels and local symbols below follow the action conventions specified for this theory.

<a id="1-conventions-and-calculation-regime"></a>

## Conventions and calculation regime

The authoritative convention input is [CONVENTIONS.md](../../../common/details/source_conventions.md).

```math
S=S_{2\text{-der}}^{(\leq2)}
+\alpha S_{\mathrm{Weyl}^2}^{(\leq2)},\qquad
\alpha\in\mathbb R\setminus\{0\},\quad
g\in\mathbb R\setminus\{0\},\quad
\partial_\mu\alpha=\partial_\mu g=0.
```

$`\alpha`$ is not perturbative. The action is exact in bosons and these constants and extends through second order in fermion count. The subsequent fluctuation expansion is not an expansion in $`\alpha`$. Terms with four or more fermions do not contribute to the Hessian on a bosonic background.

No free parameter or combination such as $`\alpha g^2`$ is replaced by a sample numerical value. The $`\alpha g^2=-2,6,\ldots`$ conditions below solve the relevant zero, coincidence, or rank equations. $`L_0=1`$ also follows from the background equations.

```math
\eta_{ab}=(-,+,+,+,+),\qquad
X_{[ab]}=\frac12(X_{ab}-X_{ba}),\qquad
\{\gamma^a,\gamma^b\}=2\eta^{ab},\qquad
\gamma\cdot T=\gamma^{ab}T_{ab}.
```

No $`1/p!`$ is added to the dot contraction. Spinors are Grassmann-odd:

```math
\epsilon_{12}=\epsilon^{12}=1,\qquad
X_i=X^j\epsilon_{ji},\qquad
\bar X\Gamma Y=\bar X^i\Gamma Y_i,
```

```math
\bar X^i\gamma_{(n)}Y^j=t_n\bar Y^j\gamma_{(n)}X^i,
\qquad
(t_0,t_1,t_2,t_3,t_4,t_5)=(1,1,-1,-1,1,1).
```

Calculation of the contracted sign:

```math
\bar X^i\gamma_{(n)}Y_i
=\epsilon_{ji}\bar X^i\gamma_{(n)}Y^j
=t_n\epsilon_{ji}\bar Y^j\gamma_{(n)}X^i
=-t_n\bar Y^j\gamma_{(n)}X_j.
```

The algebraic Majorana bar is not antilinear complex conjugation on $`i`$. It is not identified with the Hermiticity convention of the physical Hilbert inner product. At this stage, the absence of an explicit Dirac-bar/complex-conjugation convention remained relevant particularly to the final physical interpretation of absolute fermionic norms.

The epsilon tensor and density are kept separate:

```math
e=\sqrt{-g},\qquad
\epsilon^{\mu\nu\rho\sigma\lambda}
=e\,\varepsilon^{\mu\nu\rho\sigma\lambda},\qquad
\gamma^{abcde}=i\varepsilon^{abcde}\mathbf1.
```

No numerical orientation is selected. A common symbolic epsilon/Clifford system replaces the source's specific orientation.

<a id="11-corrected-lorentz-derivative"></a>

### Corrected Lorentz derivative

For lowered Lorentz indices,

```math
\begin{aligned}
\nabla_\mu T_{ab}
&=\partial_\mu T_{ab}
-\omega_\mu{}^c{}_aT_{cb}
-\omega_\mu{}^c{}_bT_{ac}\\
&=\partial_\mu T_{ab}
+\omega_\mu{}^c{}_aT_{bc}
-\omega_\mu{}^c{}_bT_{ac}\\
&=\partial_\mu T_{ab}
+2\omega_\mu{}^c{}_{[a}T_{b]c}.
\end{aligned}
```

Thus the correct working definition is

```math
\boxed{\left.\mathcal D_\mu T_{ab}\right|_\omega
=+2\omega_\mu{}^c{}_{[a}T_{b]c}}
```

The equivalent notation $`-2\omega_\mu{}^c{}_{[a}T_{|c|b]}`$ uses a different index order. A minus sign cannot be used with the same $`T_{b]c}`$ ordering.

Independent Clifford check with the definition $`\Omega_\mu=\omega_\mu{}^{cd}\gamma_{cd}/4`$:

```math
[\Omega_\mu,T_{ab}\gamma^{ab}]
=\gamma^{ab}\left(
-\omega_\mu{}^c{}_aT_{cb}
-\omega_\mu{}^c{}_bT_{ac}\right).
```

The product rule for spinor and tensor derivatives therefore requires the same plus sign. The incorrect choice leaves the residual
$`4\gamma^{ab}\omega_\mu{}^c{}_{[a}T_{b]c}\xi`$.

<a id="12-dependent-connection-and-weight-corrections"></a>

### Dependent-connection and weight corrections

Since $`w(\chi)=3/2`$, $`-3b_\mu\chi/2`$ is used in $`\mathcal D_\mu\chi`$.
$`f_\mu{}^a`$ is defined together with the explicit $`\chi`$ term in $`\widehat R'(M)`$.
A consistent conversion from the old sign in the primed curvature gives

```math
\Delta\mathcal R_a{}^c=-12J_a{}^c-4\delta_a{}^cJ_b{}^b,
\qquad
\Delta\mathcal R=-32J_a{}^a,\qquad
J_\mu{}^a=\bar\psi_\mu\gamma^a\chi,
```

```math
\Delta f_a{}^c
=-\frac16\Delta\mathcal R_a{}^c
+\frac1{48}\delta_a{}^c\Delta\mathcal R
=2J_a{}^c.
```

In the full traceless curvature, this change gives
$`\Delta\widehat R(M)=0`$. Changing only the explicit sign while holding $`f`$ fixed is a different operation.

<a id="bolum-2"></a>

<a id="2-construction-of-the-weyl-squared-action"></a>

## Construction of the Weyl-squared action

The initial calculation is
[05_gauged_full_fermionic_weyl2_calculation.md](construction.md).
This step uses the pregauge Dilaton–Weyl formulation.
The compensating linear multiplet $`(L_c,\varphi_c,E_c,N_c)`$ and the Weyl-composite
linear multiplet $`(L_W,\varphi_W,E_W,N_W)`$ are distinct objects.

<a id="21-vectorlinear-density-and-bridge"></a>

### Vector–linear density and bridge

```math
\begin{aligned}
e^{-1}\mathcal L_{VL}
={}&Y^{ij}L_{ij}+i\bar\lambda\varphi
-\frac12\bar\psi_m^i\gamma^m\lambda^jL_{ij}
+A_aP^a+\rho N\\
&+\frac\rho2\bar\psi_m\gamma^m\varphi
+\frac{i\rho}{4}\bar\psi_m^i\gamma^{mn}\psi_n^jL_{ij},
\\
P^a={}&E^a+\frac i2\bar\psi_b\gamma^{ba}\varphi
+\frac14\bar\psi_b^i\gamma^{abc}\psi_c^jL_{ij}.
\end{aligned}
```

The first three components of the defining vector are $`(\rho,A_\mu,\lambda^i)=(\sigma,C_\mu,\psi^i)`$. Its fourth component follows from the gauging constraint:

```math
2\sigma Y^{ij}-\frac i2\bar\psi^i\psi^j+gL_c^{ij}=0
\quad\Longrightarrow\quad
Y^{ij}=\frac{i}{4\sigma}\bar\psi^{(i}\psi^{j)}
-\frac{g}{2\sigma}L_c^{ij}.
```

The successive equations of the constraint multiplet are
$`\Gamma^i+g\varphi_c^i=0`$,
$`\mathcal C+gN_c=0`$, and
$`\mathcal H_a+gE_{ca}=0`$.
Their use defines Dilaton–Weyl composites; it does not eliminate independent fields of the target higher-derivative action on shell.

<a id="22-full-gauging-dependence-of-the-composites"></a>

### Full gauging dependence of the composites

Solve for $`-8\sigma^2\chi^i`$ in the spinor constraint:

```math
\begin{aligned}
\chi^i={}&
\frac{i}{8\sigma}\mathord{\not{\mathcal D}}\psi^i
+\frac{i}{16\sigma^2}\mathord{\not{\mathcal D}}\sigma\,\psi^i
-\frac1{32\sigma^2}\gamma\cdot\widehat G\,\psi^i
+\frac1{4\sigma}\gamma\cdot T\,\psi^i\\
&+\frac{i}{32\sigma^3}\psi_j\bar\psi^i\psi^j
-\frac{g}{16\sigma^3}L_c^{ij}\psi_j
+\frac{g}{8\sigma^2}\varphi_c^i .
\end{aligned}
```

For example, back-substitution of the gauging terms into the constraint gives

```math
-\frac{g}{2\sigma}L_c^{ij}\psi_j
-8\sigma^2\left(
-\frac{g}{16\sigma^3}L_c^{ij}\psi_j
+\frac{g}{8\sigma^2}\varphi_c^i\right)
+g\varphi_c^i=0
```

The cubic fermion term is retained in the initial map.

In the scalar constraint, first calculate

```math
Y^{ij}Y_{ij}
=-\frac1{16\sigma^2}(\bar\psi^i\psi^j)(\bar\psi_i\psi_j)
-\frac{ig}{4\sigma^2}L_{c\,ij}\bar\psi^i\psi^j
+\frac{g^2}{4\sigma^2}L_c^{ij}L_{c\,ij}
```

The two cross terms have the same sign. Then

```math
\begin{aligned}
D={}&\frac1{4\sigma}\Box^c\sigma
+\frac1{8\sigma^2}(\mathcal D\sigma)^2
-\frac1{16\sigma^2}\widehat G^2
-\frac1{8\sigma^2}\bar\psi\mathord{\not{\mathcal D}}\psi\\
&-\frac1{64\sigma^4}(\bar\psi^i\psi^j)(\bar\psi_i\psi_j)
-\frac{4i}{\sigma}\bar\psi\chi\\
&+\left(-\frac{26}{3}T_{ab}
+\frac2\sigma\widehat G_{ab}
+\frac{i}{4\sigma^2}\bar\psi\gamma_{ab}\psi\right)T^{ab}\\
&+\frac{g}{4\sigma^2}N_c
-\frac{ig}{16\sigma^4}L_{c\,ij}\bar\psi^i\psi^j
+\frac{g^2}{16\sigma^4}L_c^{ij}L_{c\,ij}.
\end{aligned}
```

$`D,\chi,\Box^c`$ and the connections and fermions inside hatted objects are part of these definitions.

Tensor composite and form strength:

```math
T_{ab}=\frac1{8\sigma^2}
\left(\sigma\widehat G_{ab}
+\frac16\varepsilon_{abcde}\widehat H^{cde}
+\frac i4\bar\psi\gamma_{ab}\psi\right),
\qquad
H=dB+\frac12C\wedge G+\frac g2E_3.
```

<a id="23-substitution-of-the-map-into-the-density"></a>

### Substitution of the map into the density

```math
\begin{aligned}
e^{-1}\mathcal L_{\sigma C^2,g}^{\rm map}
={}&\sigma N_W+C_aE_W^a
+i\bar\psi\varphi_W
+\frac\sigma2\bar\psi_m\gamma^m\varphi_W
+\frac i2 C_m\bar\psi_n\gamma^{nm}\varphi_W\\
&+\left(\frac{i}{4\sigma}\bar\psi^{(i}\psi^{j)}
-\frac g{2\sigma}L_c^{ij}\right)L_{W\,ij}\\
&-\frac12\bar\psi_m^i\gamma^m\psi^jL_{W\,ij}
+\frac{i\sigma}{4}\bar\psi_m^i\gamma^{mn}\psi_n^jL_{W\,ij}
+\frac14 C_m\bar\psi_n^i\gamma^{mnp}\psi_p^jL_{W\,ij}.
\end{aligned}
```

There are two descendant, three spinor, and four triplet contributions.
In particular, using

```math
L_{W\,ij}
=\frac i4\overline{\widehat R}_{ab(i}(Q)\widehat R_{j)}{}^{ab}(Q)
+\frac{256i}{3}\bar\chi_{(i}\chi_{j)}
+\frac{16}{3}\widehat R_{ab\,ij}(V)T^{ab}
```

gives the explicit gauging coefficients

```math
-\frac g{2\sigma}
\left(\frac i4,\frac{256i}{3},\frac{16}{3}\right)
=\left(-\frac{ig}{8\sigma},-\frac{128ig}{3\sigma},
-\frac{8g}{3\sigma}\right)
```

The full pregauge density is in Appendix B.

Weyl normalization

```math
\frac18\sigma\widehat C^2+\frac{64}{3}\sigma D^2,\qquad
\frac{64/3}{1/8}=\frac{512}{3}
```

This is retained. $`512/3`$ is a relative ratio, not the coefficient of $`D^2`$.

Symbolic polynomial check that gauging dependence is retained:
the relevant contribution from squaring the two monomials in $`D`$ is

```math
\begin{aligned}
\frac{64\sigma}{3}
\left(\frac{gN_c}{4\sigma^2}
+\frac{g^2L_c^{ij}L_{c\,ij}}{16\sigma^4}\right)^2
={}&\frac{4g^2N_c^2}{3\sigma^3}
+\frac{2g^3N_cL_c^{ij}L_{c\,ij}}{3\sigma^5}\\
&+\frac{g^4(L_c^{ij}L_{c\,ij})^2}{12\sigma^7}.
\end{aligned}
```

This is a coefficient calculation for the specified monomials, not a background choice. The $`g^3,g^4`$ contributions are retained.

The pregauge density is the complete substitution of the specified source map, including the adopted $`8/3`$ spinor coefficient. The spectrum uses this input after the common gauge choice and projection to physical fermion degree zero and two.

<a id="bolum-3"></a>

<a id="3-combination-with-the-two-derivative-action"></a>

## Combination with the two-derivative action

Common gauge:

```math
\sigma=1,\qquad \psi^i=0,\qquad b_\mu=0,\qquad
L_{ij}=\frac L{\sqrt2}\delta_{ij},\qquad
V_\mu^{ij}=V_\mu^{\prime\,ij}+\frac12\delta^{ij}V_\mu.
```

Here $`\psi^i`$ is the dilatino; $`\psi_\mu^i`$ and $`\varphi^i`$ are retained.
The role labels $`L_c,\varphi_c,E_c,N_c`$ are removed without changing coefficients.

Counting all fermions with a temporary variable $`u`$, define

```math
\Pi_{\le2}F=[u^0]F(u)+[u^2]F(u)
```

This operation applies to explicit fermions and to all hatted objects and composites. The final action is

```math
\boxed{
S=\int d^5x\,e\,
\Pi_{\le2}\big(\mathscr L_{2\partial}+\alpha\mathscr W_{\rm P}\big)
}
```

The full coefficients of $`\mathscr L_{2\partial}`$, including the linear map, all monomials of $`\mathscr W_{\rm P}`$, and the required composite definitions appear together in Appendix A. The two-derivative density's own coefficient $`-2`$ is not applied to the Weyl sector.

Check of the form definitions:

```math
\begin{gathered}
G=dC,\quad H=dB+\frac12C\wedge G+\frac g2E_3,\quad
dH=\frac12G\wedge G+\frac g2dE_3,\\
\delta C=d\Lambda,\quad
\delta E_3=d\Lambda_2,\quad
\delta B=d\Lambda_1-\frac12\Lambda G-\frac g2\Lambda_2,\\
\delta H=-\frac12d\Lambda\wedge G
-\frac12\Lambda dG-\frac g2d\Lambda_2
+\frac12d\Lambda\wedge G+\frac g2d\Lambda_2=0.
\end{gathered}
```

The determinant is retained in the bridge:

```math
E^{\mu\nu}=-\frac1{12}\varepsilon^{\mu\nu\rho\sigma\lambda}E_{\rho\sigma\lambda},
\qquad
P^\mu=e^{-1}\partial_\nu(eE^{\mu\nu}).
```

For vector potential $`A_\mu`$, the difference between the two density representatives is

```math
eA_\mu P^\mu
=\frac e2F_{\mu\nu}E^{\mu\nu}
+\partial_\nu(eA_\mu E^{\mu\nu})
```

so the boundary term is not discarded.
Moreover, replacing $`-4gC_aP^a`$ with $`-4gC_aE^a`$ loses

```math
-4gC_a(P^a-E^a)
=-2igC_a\bar\psi_b\gamma^{ba}\varphi
-gC_a\bar\psi_b^i\gamma^{abc}\psi_c^jL_{ij}
```

these terms. The combination therefore retains the appropriate source density representatives and the distinction $`P/E`$.

<a id="bolum-4"></a>

<a id="4-independent-fields-and-variation"></a>

## Independent fields and variation

The independent variables are

```math
\boxed{
e_\mu{}^a,\ C_\mu,\ B_{\mu\nu},\ L,\ N,\ E_{\mu\nu\rho},\
V_\mu,\ V_\mu^{\prime\,ij},\ \psi_\mu{}^i,\ \varphi^i
}
```

with $`E_a`$ calculated from $`E_3`$ and the fermionic bridge:

```math
E^a=P^a-\frac i2\bar\psi_b\gamma^{ba}\varphi
-\frac{L}{4\sqrt2}\delta_{ij}
\bar\psi_b^i\gamma^{abc}\psi_c^j.
```

$`T,D,\chi,Y,\omega,\phi,f`$ and the map components are not additional independent fields.
An auxiliary-field label in the two-derivative theory does not determine propagation in the total higher-derivative theory.

To make the composite chain rule explicit, denote independent fields by $`\Phi^I`$ and dependent objects by $`U^A[\Phi]`$:

```math
\delta U^A=\mathcal J^A{}_I\,\delta\Phi^I,\qquad
\delta S=\int\left[
\mathcal E_I^{\rm explicit}\delta\Phi^I+
\mathcal E_A^U\,\mathcal J^A{}_I\delta\Phi^I
\right]+\int_{\partial M}\Theta .
```

Defining the graded formal adjoint with the Grassmann/flip convention above gives

```math
\boxed{\mathcal E_I=
\mathcal E_I^{\rm explicit}
+(\mathcal J^A{}_I)^\ddagger\mathcal E_A^U}
```

Variation of the dependent spin connection is included in this $`\mathcal J`$.
Field values of the background or gauge class are substituted after the required variations.

This formula specifies the full variation method used to obtain the background and physical linearized equations below. The displayed component equations are restricted to those sectors and backgrounds.

<a id="bolum-5"></a>

