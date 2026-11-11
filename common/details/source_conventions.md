<a id="3-dimension-indices-metric-and-density"></a>

# Dimension, indices, metric and density

```math
D_{\rm spacetime}=5,\qquad
\eta_{ab}=\mathop{\mathrm{diag}}\nolimits(-,+,+,+,+),\qquad
\mu,\nu,a,b=0,\ldots,4,\qquad i,j=1,2.
```

$`\mu,\nu`$ are coordinate indices; $`a,b`$ are tangent indices. The dimension here must not be confused with the scalar field $`D`$.

```math
g_{\mu\nu}=e_\mu{}^ae_\nu{}^b\eta_{ab},\qquad
X_a=e_a{}^\mu X_\mu,\qquad
X^a=e_\mu{}^aX^\mu.
```

All form and curvature indices are converted using the same vielbein. The density notation is

```math
e=\det(e_\mu{}^a)=\sqrt{-g},\qquad
S=\int d^5x\,\mathcal L
=\int d^5x\,e\,(e^{-1}\mathcal L)
```

Here $`e^{-1}\mathcal L`$ is generally the scalar Lagrangian; it does not mean only the bosonic two-derivative sector.

Densities and map components retain their supplied coefficients; no overall factor of two is applied. General sign choices are not used as a rule for collectively redefining the fields of a multiplet.

<a id="4-antisymmetrization-clifford-algebra-and-spinor-operations"></a>

## Antisymmetrization, Clifford algebra and spinor operations

Unit-weight (anti)symmetrization and Clifford notation:

```math
X_{[ab]}=\frac12(X_{ab}-X_{ba}),\qquad
X_{(ab)}=\frac12(X_{ab}+X_{ba}),
```

```math
\{\gamma^a,\gamma^b\}=2\eta^{ab},\qquad
\gamma^{a_1\ldots a_n}=\gamma^{[a_1}\cdots\gamma^{a_n]}.
```

Dot and slash denote full contraction:

```math
\gamma\!\cdot\!X=\gamma^{a_1\ldots a_p}X_{a_1\ldots a_p},\qquad
\mathord{\not{X}}=\gamma^aX_a,\qquad
\mathord{\not{\mathcal D}}=\gamma^a\mathcal D_a.
```

No $`1/p!`$ is added to the dot contraction. The five-index gamma identity is

```math
\gamma^{abcde}=i\varepsilon^{abcde}\mathbf1
```

Its equivalent duality expression in the Clifford algebra is

```math
\gamma^{a_1\ldots a_r}
=\frac{i}{(5-r)!}\varepsilon^{a_1\ldots a_5}
 \gamma_{a_5\ldots a_{r+1}}
```

The reversed order of the gamma indices on the right is retained.

NW–SE convention:

```math
\epsilon_{12}=\epsilon^{12}=1,\qquad
\epsilon_{ij}=-\epsilon_{ji},\qquad
X^i=\epsilon^{ij}X_j,\qquad X_i=X^j\epsilon_{ji},
```

```math
\epsilon^{ij}\epsilon_{kj}=\delta^i{}_k,\qquad
\bar X\Gamma Y=\bar X^i\Gamma Y_i.
```

For symmetric $`L_{ij}`$, these rules yield

```math
L^{ij}=\epsilon^{ik}\epsilon^{j\ell}L_{k\ell},\qquad
L_i{}^j=\epsilon^{jk}L_{ik},\qquad
L^i{}_j=\epsilon^{ik}L_{kj}
```

Changing the position of a contracted $`SU(2)`$ pair produces a sign:

```math
\bar X^i\Gamma Y_i=-\bar X_i\Gamma Y^i.
```

Open-index flip and Fierz relation:

```math
\bar X^i\gamma_{(n)}Y^j=t_n\bar Y^j\gamma_{(n)}X^i,
\qquad t_0=t_1=+1,\quad t_2=t_3=-1,
```

```math
\psi_j\bar\lambda^i
=-\frac14(\bar\lambda^i\psi_j)\mathbf1
 -\frac14(\bar\lambda^i\gamma^a\psi_j)\gamma_a
 +\frac18(\bar\lambda^i\gamma^{ab}\psi_j)\gamma_{ab}.
```

The NW–SE-contracted flip follows directly from the same rules:

```math
\begin{aligned}
\bar X^i\gamma_{(n)}Y_i
&=\epsilon_{ji}\bar X^i\gamma_{(n)}Y^j\\
&=t_n\epsilon_{ji}\bar Y^j\gamma_{(n)}X^i
=-t_n\bar Y^j\gamma_{(n)}X_j.
\end{aligned}
```

For ranks 4 and 5, $`t_4=t_5=+1`$ follows by gamma duality from ranks 1 and 0, respectively. Grassmann signs remain consistent with these flip/Fierz rules; fermions are not interchanged as commuting objects.

No explicit $`C`$ matrix, Dirac-bar phase or detailed complex-conjugation operation has been specified. Bar operations follow the NW–SE, flip and Fierz rules above. If conjugation beyond these identities is needed, the missing input is identified separately.

<a id="5-epsilon-forms-and-field-strengths"></a>

## Epsilon, forms and field strengths

Epsilon is real, and for $`n+p=5`$

```math
\varepsilon_{a_1\ldots a_n b_1\ldots b_p}
\varepsilon^{a_1\ldots a_n c_1\ldots c_p}
=-n!p!\,\delta_{[b_1}^{c_1}\cdots\delta_{b_p]}^{c_p}.
```

The numerical value of the $`\varepsilon^{01234}`$ component is unspecified. No numerical orientation is chosen; epsilon and gamma matrices remain symbolic through epsilon-contraction and gamma-duality identities.

To distinguish the coordinate epsilon tensor from the density symbol, this file writes

```math
\varepsilon^{\mu\nu\rho\sigma\lambda}
=e_a{}^\mu e_b{}^\nu e_c{}^\rho e_d{}^\sigma e_e{}^\lambda
 \varepsilon^{abcde},\qquad
\epsilon^{\mu\nu\rho\sigma\lambda}
=e\,\varepsilon^{\mu\nu\rho\sigma\lambda}
```

The second object is a density symbol; if used in place of the tensor, the factor $`e^{-1}`$ is retained explicitly. This distinction introduces no new physical normalization.

The ordinary field strengths are

```math
G_{\mu\nu}=2\partial_{[\mu}C_{\nu]},\qquad
H_{\mu\nu\rho}=3\partial_{[\mu}B_{\nu\rho]}
 +\frac32C_{[\mu}G_{\nu\rho]}+\frac g2E_{\mu\nu\rho}
```

and the gauge transformations are

```math
\delta C_\mu=\partial_\mu\Lambda,\qquad
\delta B_{\mu\nu}=2\partial_{[\mu}\Lambda_{\nu]}
 -\frac12\Lambda G_{\mu\nu}-\frac g2\Lambda_{\mu\nu}
```

The supergravity under study is gauged, with $`g\neq0`$. The $`+\tfrac g2E_{\mu\nu\rho}`$ contribution in $`H_{\mu\nu\rho}`$ is retained; this normalization agrees with definition (D.1) of the supplied $`R^2`$ action. Under $`\delta E_{\mu\nu\rho}=3\partial_{[\mu}\Lambda_{\nu\rho]}`$, the $`-\tfrac g2\Lambda_{\mu\nu}`$ term in $`\delta B_{\mu\nu}`$ ensures gauge invariance of $`H_{\mu\nu\rho}`$.

Full supercovariant field strengths:

```math
\begin{aligned}
\widehat G_{\mu\nu}
&=G_{\mu\nu}-\bar\psi_{[\mu}\gamma_{\nu]}\psi
 +\frac{i}{2}\sigma\bar\psi_{[\mu}\psi_{\nu]},\\
\widehat H_{\mu\nu\rho}
&=H_{\mu\nu\rho}
 -\frac34\sigma^2\bar\psi_{[\mu}\gamma_\nu\psi_{\rho]}
 -\frac{3i}{2}\sigma\bar\psi_{[\mu}\gamma_{\nu\rho]}\psi.
\end{aligned}
```

$`H`$ remains a three-form. The normalized two-form $`H_{ab}`$ and $`\widetilde H_{ab}`$ are not used. $`H_\mu{}^{ab}`$ is not a two-form dual but $`e^{a\nu}e^{b\rho}H_{\mu\nu\rho}`$; its hatted counterpart is defined by the same pullback.

<a id="6-weyl-weights-and-derivatives"></a>

## Weyl weights and derivatives

$`w`$ denotes the Weyl weight:

| Object | $`w`$ |
|---|---:|
| $`e_\mu{}^a`$ | $`-1`$ |
| $`\psi_\mu^i`$ | $`-1/2`$ |
| $`b_\mu,V_\mu^{ij},C_\mu,B_{\mu\nu}`$ | $`0`$ |
| $`\sigma,\rho`$ | $`1`$ |
| $`\psi^i,\lambda^i`$ | $`3/2`$ |
| $`Y^{ij}`$ | $`2`$ |
| $`L^{ij}`$ | $`3`$ |
| $`\varphi^i`$ | $`7/2`$ |
| $`E_a,N`$ | $`4`$ |
| $`T_{ab},\chi^i,D`$ | $`1,3/2,2`$ |
| $`\widehat G_{ab},\widehat R_{ab}^{ij}(V),\widehat C_{abcd}`$ | $`2`$ |
| $`\widehat R_{ab}^i(Q)`$ | $`3/2`$ |

Since $`w(e_a{}^\mu)=1`$, a tangent derivative increases the weight by one. For example, $`\widehat G_{\mu\nu}`$ has weight zero, whereas $`\widehat G_{ab}=e_a{}^\mu e_b{}^\nu\widehat G_{\mu\nu}`$ has weight two. Weyl weights are not replaced by Poincaré derivative counting.

$`\mathcal D_\mu`$ is the full supercovariant derivative. $`\partial_\mu`$ is not identical to the Lorentz-only derivative $`\nabla_\mu`$, a derivative containing only the residual $`U(1)`$ connection, or a purely bosonic gauge-covariant derivative. The connection part for a doublet is

```math
\left(\partial_\mu-wb_\mu+\frac14\omega_\mu{}^{ab}\gamma_{ab}\right)X^i
 -V_\mu^{ij}X_j
```

Its supercovariant completion depends on the field's own transformation. This expression alone is not the full definition of $`\mathcal D_\mu X^i`$.

For example:

```math
\mathcal D_\mu\sigma=(\partial_\mu-b_\mu)\sigma
 -\frac{i}{2}\bar\psi_\mu\psi,
```

```math
\mathcal D_\mu L^{ij}
=(\partial_\mu-3b_\mu)L^{ij}
 +2V_\mu^{(i}{}_kL^{j)k}
 -i\bar\psi_\mu^{(i}\varphi^{j)}.
```

The working definition of the $`T`$ derivative, with the Lorentz-connection sign verified in Section 11.5, is

```math
\mathcal D_\mu T_{ab}
=\partial_\mu T_{ab}-b_\mu T_{ab}
 +2\omega_\mu{}^c{}_{[a}T_{b]c}
 -\frac{i}{2}\bar\psi_\mu\gamma_{ab}\chi
 +\frac{3i}{32}\bar\psi_\mu\widehat R_{ab}(Q).
```

The negative-sign Lorentz term $`-2\omega_\mu{}^c{}_{[a}T_{b]c}`$ with the same index order is not used as the working definition. Two independent internal-consistency checks are given in Section 11.5.

The working coefficient for $`\mathcal D_\mu\chi^i`$ is $`-\tfrac32b_\mu\chi^i`$. Its difference from the alternative $`-\tfrac72b_\mu\chi^i`$ is shown in Section 11.1. These internal-consistency checks determine the working definitions.

<a id="7-connections-and-curvature-distinctions"></a>

## Connections and curvature distinctions

Spin connection:

```math
\begin{aligned}
\omega_\mu{}^{ab}
={}&2e^{\nu[a}\partial_{[\mu}e_{\nu]}{}^{b]}
 -e^{\nu[a}e^{b]\rho}e_{\mu c}\partial_\nu e_\rho{}^c
 +2e_\mu{}^{[a}b^{b]}\\
&+\frac12\bar\psi^{[a}\gamma^{b]}\psi_\mu
 +\frac14\bar\psi^a\gamma_\mu\psi^b,\\
\psi^a&=e^{a\mu}\psi_\mu,\qquad b^a=e^{a\mu}b_\mu.
\end{aligned}
```

$`\omega_\mu{}^{ab}`$ is dependent; it is not held as an independent, unchanged connection during calculation. The dilatino condition $`\psi^i=0`$ does not set gravitino contorsion to zero.

$`Q`$ curvature:

```math
\begin{aligned}
\widehat R_{\mu\nu}^{\prime\,i}(Q)
={}&2\partial_{[\mu}\psi_{\nu]}^i
 +\frac12\omega_{[\mu}{}^{ab}\gamma_{ab}\psi_{\nu]}^i
 +b_{[\mu}\psi_{\nu]}^i-2V_{[\mu}^{ij}\psi_{\nu]j}
 +2i\gamma\!\cdot\!T\gamma_{[\mu}\psi_{\nu]}^i,\\
\phi_\mu^i
={}&\frac{i}{3}\gamma^a\widehat R_{\mu a}^{\prime\,i}(Q)
 -\frac{i}{24}\gamma_\mu\gamma^{ab}\widehat R_{ab}^{\prime\,i}(Q),\\
\widehat R_{\mu\nu}^i(Q)
={}&\widehat R_{\mu\nu}^{\prime\,i}(Q)-2i\gamma_{[\mu}\phi_{\nu]}^i.
\end{aligned}
```

The prime here means that the $`\phi_\mu^i`$ contribution is omitted. For $`\widehat R'(M)`$, the prime means that the $`f_\mu{}^a`$ contribution is omitted.

Ordinary Lorentz curvature and Ricci contraction:

```math
\begin{aligned}
R_{\mu\nu}{}^{ab}(\omega)
&=2\partial_{[\mu}\omega_{\nu]}{}^{ab}
 +2\omega_{[\mu}{}^{ac}\omega_{\nu]c}{}^b,\\
R_{abcd}(\omega)&=e_a{}^\mu e_b{}^\nu R_{\mu\nu cd}(\omega),\\
R_{bd}(\omega)&=\eta^{ac}R_{abcd}(\omega),\qquad
R(\omega)=\eta^{bd}R_{bd}(\omega).
\end{aligned}
```

The Lorentz curvature is the supercovariant completion of the calculated connection transformation. For the index order below, the working sign of the explicit $`\chi`$ term is **$`+8`$**. Its difference from the alternative $`-8`$ and its effect on the dependent $`f_\mu{}^a`$ connection are shown in Section 11.4.

```math
\begin{aligned}
\widehat R'_{\mu\nu}{}^{ab}(M)
={}&R_{\mu\nu}{}^{ab}(\omega)
 +i\bar\phi_{[\mu}\gamma^{ab}\psi_{\nu]}
 +i\bar\psi_{[\mu}\gamma^{[a}\gamma\!\cdot\!T\gamma^{b]}\psi_{\nu]}\\
&+\bar\psi_{[\mu}\gamma^{[a}\widehat R_{\nu]}{}^{b]}(Q)
 +\frac12\bar\psi_{[\mu}\gamma_{\nu]}\widehat R^{ab}(Q)
 +8\bar\psi_{[\mu}e_{\nu]}{}^{[a}\gamma^{b]}\chi,\\
\widehat R_{\mu\nu}{}^{ab}(M)
={}&\widehat R'_{\mu\nu}{}^{ab}(M)
 +8f_{[\mu}{}^{[a}e_{\nu]}{}^{b]},\\
\widehat R_\mu{}^a(Q)&=e^{a\nu}\widehat R_{\mu\nu}(Q).
\end{aligned}
```

$`i\bar\psi_{[\mu}\gamma^{ab}\psi_{\nu]}`$ vanishes identically and therefore does not appear separately above (Section 11.2). Hatted curvatures and composite fields retain their full definitions; this notation is not a fermion-order truncation.

Algebraic definition of the dependent connection:

```math
R_{\mu\nu}=\widehat R'_{\mu\rho}{}^{ab}(M)e_b{}^\rho e_{\nu a},
\qquad R=R_\mu{}^\mu,\qquad
f_\mu{}^a=-\frac16R_\mu{}^a+\frac1{48}e_\mu{}^aR.
```

The $`R_{\mu\nu}`$ in the last line comes from supercovariant $`\widehat R'(M)`$; it is not identified with ordinary $`R_{\mu\nu}(\omega)`$ when fermions are present. Here $`\widehat R'(M)`$ is the working expression with the $`+8`$ sign given above. A $`f_\mu{}^a`$ calculated from the alternative $`-8`$ expression cannot be inserted unchanged; Section 11.4 gives the conversion. The bosonic contraction order agrees with $`R_{bd}=\eta^{ac}R_{abcd}`$ above.

Ordinary internal curvature and its supercovariant counterpart:

```math
\begin{aligned}
V_{\mu\nu}^{ij}
&=2\partial_{[\mu}V_{\nu]}^{ij}
 -2V_{[\mu}^{k(i}V_{\nu]k}{}^{j)},\\
\widehat R_{\mu\nu}^{ij}(V)
&=V_{\mu\nu}^{ij}
 -3i\bar\phi_{[\mu}^{(i}\psi_{\nu]}^{j)}
 -8\bar\psi_{[\mu}^{(i}\gamma_{\nu]}\chi^{j)}
 -i\bar\psi_{[\mu}^{(i}\gamma\!\cdot\!T\psi_{\nu]}^{j)}.
\end{aligned}
```

The conventional curvature constraint is

```math
e_b{}^\nu\widehat R_{\mu\nu}{}^{ab}(M)=0
```

and the supercovariant Weyl-tensor notation is

```math
\widehat C_{\mu\nu\rho\sigma}
=e_{\rho a}e_{\sigma b}\widehat R_{\mu\nu}{}^{ab}(M)
```

The ordinary Weyl tensor is:

```math
\begin{aligned}
C_{\mu\nu\rho\sigma}
={}&R_{\mu\nu\rho\sigma}
 -\frac13(g_{\mu\rho}R_{\nu\sigma}-g_{\nu\rho}R_{\mu\sigma}
          -g_{\mu\sigma}R_{\nu\rho}+g_{\nu\sigma}R_{\mu\rho})\\
&+\frac1{12}(g_{\mu\rho}g_{\nu\sigma}-g_{\mu\sigma}g_{\nu\rho})R.
\end{aligned}
```

Merely adding hats to this bosonic formula does not derive the full fermionic expansion of $`\widehat C`$. The vanishing bilinear was checked in Section 11.2; the sign of the explicit $`\chi`$ term and its treatment together with $`f`$ were checked in Section 11.4.

<a id="8-linear-multiplet-transformation-rules"></a>

## Linear-multiplet transformation rules

The $`Q`$ and $`S`$ transformations against which the map components are compared:

```math
\begin{aligned}
\delta L^{ij}&=i\bar\epsilon^{(i}\varphi^{j)},\\
\delta\varphi^i
&=-\frac{i}{2}\mathord{\not{\mathcal D}}L^{ij}\epsilon_j
 -\frac{i}{2}\gamma^aE_a\epsilon^i+\frac12N\epsilon^i
 -\gamma\!\cdot\!T L^{ij}\epsilon_j+3L^{ij}\eta_j,\\
\delta E_a
&=-\frac{i}{2}\bar\epsilon\gamma_{ab}\mathcal D^b\varphi
 -2\bar\epsilon\gamma^b\varphi T_{ba}
 -2\bar\eta\gamma_a\varphi,\\
\delta N
&=\frac12\bar\epsilon\mathord{\not{\mathcal D}}\varphi
 +\frac{3i}{2}\bar\epsilon\gamma\!\cdot\!T\varphi
 +4i\bar\epsilon^i\chi^jL_{ij}
 +\frac{3i}{2}\bar\eta\varphi.
\end{aligned}
```

Fermionic completions for $`\mathcal D_\mu\varphi^i`$ and $`\mathcal D_\mu E_a`$ are retained. In tensor notation

```math
\mathcal D^aE_a=0,\qquad
E^\mu=-\frac1{12}\varepsilon^{\mu\nu\rho\sigma\lambda}
                  \mathcal D_\nu E_{\rho\sigma\lambda},\qquad
\delta E_{\mu\nu\rho}=3\partial_{[\mu}\Lambda_{\nu\rho]}.
```

When the density symbol is used, the second equality becomes

```math
E^a=-\frac1{12}e_\mu{}^a e^{-1}
 \epsilon^{\mu\nu\rho\sigma\lambda}\mathcal D_\nu E_{\rho\sigma\lambda}
```

$`E_{\mu\nu\rho}`$ is not counted as a second independent linear-multiplet component. $`\mathcal D E_3`$ is not replaced by ordinary $`\partial E_3`$.

<a id="9-gauge-conditions-and-scope-of-the-torsionful-connection"></a>

## Gauge conditions and scope of the torsionful connection

The gauge conditions are

```math
L_{ij}=\frac{L}{\sqrt2}\delta_{ij},\qquad
\sigma=1,\qquad \psi^i=0,\qquad b_\mu=0
```

They are not applied automatically to the superconformal map inputs in this file. In particular, the first condition does not instruct using the map's composite $`L_{ij}`$ as an independent compensator for gauge fixing.

$`V_\mu^{ij}`$ is decomposed into trace and traceless parts:

```math
V_\mu^{ij}=V_\mu^{\prime\,ij}+\frac12\delta^{ij}V_\mu,
\qquad V_\mu^{\prime\,ij}\delta_{ij}=0.
```

By the NW–SE rule, the full connection acts on a doublet as

```math
\begin{aligned}
-V_\mu^{ij}X_j
&=-V_\mu^{\prime\,ij}X^k\epsilon_{kj}
  -\frac12V_\mu\delta^{ij}X_j\\
&=+V_\mu^{\prime\,ij}\epsilon_{jk}X^k
  -\frac12V_\mu\delta^{ij}X_j
=+V_\mu^{\prime\,i}{}_kX^k-\frac12V_\mu\delta^{ij}X_j.
\end{aligned}
```

The torsionful connection is exactly

```math
\boxed{\omega_{\pm\mu}{}^{ab}
 =\omega_\mu{}^{ab}\pm\widehat H_\mu{}^{ab}}
```

The hat is retained here. Under the gauge conditions above

```math
\widehat G_{\mu\nu}=G_{\mu\nu}+\frac{i}{2}\bar\psi_{[\mu}\psi_{\nu]},
\qquad
\widehat H_{\mu\nu\rho}
=H_{\mu\nu\rho}-\frac34\bar\psi_{[\mu}\gamma_\nu\psi_{\rho]}.
```

Thus, its difference from the connection constructed using ordinary $`H`$ is

```math
(\omega_\mu{}^{ab}\pm\widehat H_\mu{}^{ab})
 -(\omega_\mu{}^{ab}\pm H_\mu{}^{ab})
=\mp\frac34e^{a\nu}e^{b\rho}\bar\psi_{[\mu}\gamma_\nu\psi_{\rho]}
```

Equality between bosonic expressions is not promoted to full fermionic equality.

Gauge-fixed transformations omitting cubic fermion terms are not a complete transformation system for the entire multiplet. Full rules supplied for a particular set of Weyl fields before imposing the $`SU(2)`$ gauge condition also have a different scope.

<a id="10-map-normalization-and-completeness-boundary"></a>

## Map normalization and completeness boundary

The $`L^{ij}`$ and $`\varphi^i`$ expressions are the initial data of the map. Fermion-order counting includes the contributions contained in supercovariant objects. The $`E_a`$ and $`N`$ expressions in this section specify the displayed source components; the full fermionic inputs are those explicitly defined in each action construction.

In particular, in the $`N`$ component

```math
N\supset\frac18C_{abcd}C^{abcd}+\frac{64}{3}D^2,
\qquad
\frac{64/3}{1/8}=\frac{512}{3}.
```

$`512/3`$ is a relative coefficient; it does not replace the $`64/3`$ coefficient in $`N`$. The coefficient pair $`1/8,64/3`$ is retained.

Notation:

```math
T^2=T_{ab}T^{ab},\qquad
T^4=T_{ab}T^{bc}T_{cd}T^{da},\qquad
(T^2)^2=(T_{ab}T^{ab})^2.
```

If a required $`Q`$ or $`S`$ curvature transformation is derived from definitions, it is presented as a separate calculation step, not assumed as a supplied and verified input.

<a id="11-internal-consistency-checks"></a>

## Internal-consistency checks

The checks in this section are restricted to the specific expressions below; they do not establish verification of every equation.

<a id="111-dilatation-coefficient"></a>

### Dilatation coefficient

The $`-\tfrac72b_\mu\chi^i`$ option in $`\mathcal D_\mu\chi^i`$ is inconsistent with the Weyl weights. The five monomials of $`\chi^i`$ together give

```math
\begin{aligned}
w(\sigma^{-1}\mathord{\not{\mathcal D}}\psi^i)&=-1+1+\frac32=\frac32,\\
w(\sigma^{-2}\mathord{\not{\mathcal D}}\sigma\,\psi^i)&=-2+2+\frac32=\frac32,\\
w(\sigma^{-2}\gamma\!\cdot\!\widehat G\psi^i)&=-2+2+\frac32=\frac32,\\
w(\sigma^{-1}\gamma\!\cdot\!T\psi^i)&=-1+1+\frac32=\frac32,\\
w(\sigma^{-3}\psi_j\bar\psi^i\psi^j)&=-3+3\left(\frac32\right)=\frac32
\end{aligned}
```

Likewise, $`w(T)=1`$ follows from the respective weights $`-2+1+2`$, $`-2+3`$ and $`-2+3`$ of the $`\sigma^{-2}\sigma\widehat G_{ab}`$, $`\sigma^{-2}\widehat H_{abc}`$ and $`\sigma^{-2}\bar\psi\gamma_{ab}\psi`$ terms. The $`\sigma^{-2}\widehat G^2`$ term of $`D`$ gives $`w(D)=-2+4=2`$.

Since the connection sign and weight rule is $`\partial_\mu-wb_\mu`$, the consistent result is

```math
\boxed{w(\chi^i)=\frac32,\qquad
\left.\mathcal D_\mu\chi^i\right|_{b_\mu}
=-\frac32b_\mu\chi^i.}
```

The working coefficient is the result of this internal-consistency check. For $`\varphi^i`$, $`7/2`$ is consistent with the Weyl weight and covariant-derivative rule.

<a id="112-the-ibarpsi_mugammaabpsi_nu-term"></a>

### The $`i\bar\psi_{[\mu}\gamma^{ab}\psi_{\nu]}`$ term

Because of $`t_2=-1`$ and the NW–SE contraction

```math
\bar\psi_\mu\gamma^{ab}\psi_\nu
=-t_2\bar\psi_\nu\gamma^{ab}\psi_\mu
=\bar\psi_\nu\gamma^{ab}\psi_\mu,
```

```math
i\bar\psi_{[\mu}\gamma^{ab}\psi_{\nu]}
=\frac{i}{2}\left(\bar\psi_\mu\gamma^{ab}\psi_\nu
                  -\bar\psi_\nu\gamma^{ab}\psi_\mu\right)=0.
```

This term vanishes under the flip and contraction rules. An incorrect Weyl weight alone does not imply a missing $`\phi_\mu`$ term, and no guessed bilinear is substituted.

<a id="113-weyl-weight-of-deltawidehat-h_abc"></a>

### Weyl weight of $`\delta\widehat H_{abc}`$

The derivative term being checked is

```math
\frac{3i}{2}\bar\epsilon\gamma_{[ab}\mathcal D_{c]}\psi
```

There is no prefactor $`\sigma`$. From the Weyl weights

```math
w(\epsilon)=w(\sigma)-w(\psi)=1-\frac32=-\frac12,
\qquad w(\widehat H_{abc})=3,
```

whereas for this term

```math
w(\bar\epsilon\gamma_{[ab}\mathcal D_{c]}\psi)
=-\frac12+1+\frac32=2.
```

The curvature term in the same variation has

```math
w(\sigma^2\bar\epsilon\gamma_{[a}\widehat R_{bc]}(Q))
=2-\frac12+\frac32=3
```

as its weight. Thus, the $`\delta\widehat H_{abc}`$ expression containing these terms is not homogeneous at this point. A factor $`\sigma`$ could repair the weight; the weight check alone does not prove the full variation. This file does not adopt a guessed correction as a transformation rule. If needed, the full variation must be derived separately from the field definitions and SUSY transformations; until then, this expression is not used as a verified complete input.

<a id="114-explicit-chi-term-in-the-calculated-rm-and-the-dependent-f-connection"></a>

### Explicit $`\chi`$ term in the calculated $`R(M)`$ and the dependent $`f`$ connection

This derivation uses the connection definitions, SUSY transformations and conventional curvature constraint. It calculates the coefficient of the explicit $`\chi`$ term. This sign calculation is separate from the $`-\tfrac72b_\mu\chi^i\to-\tfrac32b_\mu\chi^i`$ correction in Section 11.1.

The spin connection's $`b_\mu`$ dependence and the relevant transformation:

```math
\left.\omega_\mu{}^{ab}\right|_b=2e_\mu{}^{[a}b^{b]},\qquad
\left.\delta_Qb_\mu\right|_\chi=-2\bar\epsilon\gamma_\mu\chi,
```

```math
\left.\delta_Q\omega_\mu{}^{ab}\right|_{\bar\epsilon\chi}
=2e_\mu{}^{[a}e^{b]\nu}
 (-2\bar\epsilon\gamma_\nu\chi)
=-4e_\mu{}^{[a}\bar\epsilon\gamma^{b]}\chi.
```

The operation $`\left.\vphantom{X}\right|_{\partial\epsilon}`$ below selects the derivative coefficient of the independent local parameter; it is not a field or fermion-order truncation. Variation of the ordinary curvature:

```math
\begin{aligned}
\left.\delta_QR_{\mu\nu}{}^{ab}(\omega)
\right|_{\partial\epsilon\,\chi}
&=\left.2\partial_{[\mu}
 \left(-4e_{\nu]}{}^{[a}\bar\epsilon\gamma^{b]}\chi\right)
 \right|_{\partial\epsilon}\\
&=-8(\partial_{[\mu}\bar\epsilon)
       e_{\nu]}{}^{[a}\gamma^{b]}\chi.
\end{aligned}
```

Using $`\left.\delta_Q\bar\psi_\mu\right|_{\partial\epsilon} =\partial_\mu\bar\epsilon`$, for the temporary coefficient $`c`$ of the completing term

```math
\begin{aligned}
\left.\delta_Q
 \left(c\bar\psi_{[\mu}e_{\nu]}{}^{[a}\gamma^{b]}\chi\right)
 \right|_{\partial\epsilon}
&=c(\partial_{[\mu}\bar\epsilon)e_{\nu]}{}^{[a}\gamma^{b]}\chi,\\
-8+c&=0\quad\Longrightarrow\quad c=+8.
\end{aligned}
```

The working term of the supercovariant completion constructed with the standard $`K`$ connection is therefore

```math
\boxed{+8\bar\psi_{[\mu}e_{\nu]}{}^{[a}\gamma^{b]}\chi}
```

This index order must be retained:

```math
e_\nu{}^{[a}\gamma^{b]}=-\gamma^{[a}e_\nu{}^{b]},\qquad
+8\bar\psi_{[\mu}e_{\nu]}{}^{[a}\gamma^{b]}\chi
=-8\bar\psi_{[\mu}\gamma^{[a}e_{\nu]}{}^{b]}\chi.
```

Using the Ricci contractions of the primed curvature,

```math
R_a{}^c=\widehat R'_{ab}{}^{cb}(M),\qquad
R=\widehat R'_{ab}{}^{ab}(M),\qquad
f_a{}^c=-\frac16R_a{}^c+\frac1{48}\delta_a{}^cR
```

The trace of the dependent connection and the trace of the full curvature are:

```math
\begin{aligned}
f_a{}^a&=-\frac16R+\frac5{48}R=-\frac1{16}R,\\
\widehat R_{ab}{}^{cb}(M)
&=R_a{}^c+6f_a{}^c+2\delta_a{}^cf_b{}^b\\
&=R_a{}^c-R_a{}^c
 +\left(\frac18-\frac18\right)\delta_a{}^cR=0.
\end{aligned}
```

In comparison with the alternative $`-8`$ expression, $`\Delta`$ denotes the calculated $`+8`$ expression minus the alternative $`-8`$ expression. Temporarily defining $`J_\mu{}^a\equiv\bar\psi_\mu\gamma^a\chi`$,

```math
\begin{aligned}
\bar\psi_{[\mu}e_{\nu]}{}^{[a}\gamma^{b]}\chi
&=-J_{[\mu}{}^{[a}e_{\nu]}{}^{b]},\\
\Delta\widehat R'_{\mu\nu}{}^{ab}(M)
&=-16J_{[\mu}{}^{[a}e_{\nu]}{}^{b]},\\
\Delta R_a{}^c&=-12J_a{}^c-4\delta_a{}^cJ_b{}^b,\\
\Delta R&=-32J_a{}^a,\\
\Delta f_a{}^c
&=-\frac16\Delta R_a{}^c+\frac1{48}\delta_a{}^c\Delta R\\
&=2J_a{}^c+\left(\frac23-\frac23\right)\delta_a{}^cJ_b{}^b
=2J_a{}^c.
\end{aligned}
```

Result in the original fields:

```math
\boxed{\Delta f_\mu{}^a=2\bar\psi_\mu\gamma^a\chi,}
```

```math
\begin{aligned}
\Delta\widehat R_{\mu\nu}{}^{ab}(M)
&=\Delta\widehat R'_{\mu\nu}{}^{ab}(M)
 +8\Delta f_{[\mu}{}^{[a}e_{\nu]}{}^{b]}\\
&=-16(\bar\psi_{[\mu}\gamma^{[a}\chi)e_{\nu]}{}^{b]}
  +16(\bar\psi_{[\mu}\gamma^{[a}\chi)e_{\nu]}{}^{b]}=0.
\end{aligned}
```

This last equality holds provided that $`f`$ is recalculated from its own Ricci contractions for both primed definitions. It does not hold if $`f`$ is kept fixed and only the sign of the explicit $`\chi`$ term is changed. The calculation uses the $`+8`$ definition of Section 7 together with $`f`$ calculated from it. This consistently tracks the dependent-connection definition; it is not an EOM substitution or auxiliary-field elimination. No claim is made that the full traceless $`\widehat R(M)`$, and hence $`\widehat C`$, changes solely because of this consistent rewriting.

<a id="115-lorentz-sign-of-the-t_ab-derivative"></a>

### Lorentz sign of the $`T_{ab}`$ derivative

For the index order below, the negative-sign option is

```math
\left.\mathcal D_\mu T_{ab}\right|_{\omega,\,\mathrm{alternative}}
=-2\omega_\mu{}^c{}_{[a}T_{b]c}
```

This is not the working definition in Section 6. Below, $`\nabla_\mu^{\mathrm L}`$ denotes only the Lorentz-connection contribution. This distinction is neither a gauge choice nor a field truncation; the Lorentz-connection coefficient in the full supercovariant derivative is being checked.

The first check follows from the derivative of a lower-index vector:

```math
\begin{aligned}
\nabla_\mu^{\mathrm L}E_a
&=\partial_\mu E_a+\omega_{\mu ab}E^b\\
&=\partial_\mu E_a+\omega_{\mu ab}\eta^{bc}E_c
=\partial_\mu E_a-\omega_\mu{}^c{}_aE_c.
\end{aligned}
```

The last equality uses $`\omega_{\mu ab}=-\omega_{\mu ba}`$. Using the connection's action on each lower Lorentz index and $`T_{cb}=-T_{bc}`$,

```math
\begin{aligned}
\nabla_\mu^{\mathrm L}T_{ab}
&=\partial_\mu T_{ab}
 -\omega_\mu{}^c{}_aT_{cb}-\omega_\mu{}^c{}_bT_{ac}\\
&=\partial_\mu T_{ab}
 +\omega_\mu{}^c{}_aT_{bc}-\omega_\mu{}^c{}_bT_{ac}\\
&=\partial_\mu T_{ab}+2\omega_\mu{}^c{}_{[a}T_{b]c}.
\end{aligned}
```

The second check is compatibility between the spinor connection and Clifford multiplication. Temporarily define

```math
\Omega_\mu:=\frac14\omega_\mu{}^{cd}\gamma_{cd},\qquad
\mathsf T:=T_{ab}\gamma^{ab},\qquad
\nabla_\mu^{\mathrm s}:=\partial_\mu+\Omega_\mu
```

where $`\xi`$ is an arbitrary spinor. The covariant product rule must be

```math
\begin{aligned}
\nabla_\mu^{\mathrm s}(\mathsf T\xi)
-\mathsf T\nabla_\mu^{\mathrm s}\xi
&=\bigl(\partial_\mu\mathsf T+[\Omega_\mu,\mathsf T]\bigr)\xi\\
&=\gamma^{ab}(\nabla_\mu^{\mathrm L}T_{ab})\xi
\end{aligned}
```

From the Clifford algebra

```math
\begin{aligned}
[\gamma_{cd},\gamma^a]
&=2(\delta_d{}^a\gamma_c-\delta_c{}^a\gamma_d),\\
[\Omega_\mu,\gamma^a]
&=\frac12\omega_\mu{}^{cd}
 (\delta_d{}^a\gamma_c-\delta_c{}^a\gamma_d)
=-\omega_\mu{}^a{}_c\gamma^c,\\
[\Omega_\mu,\gamma^{ab}]
&=-\omega_\mu{}^a{}_c\gamma^{cb}
 -\omega_\mu{}^b{}_c\gamma^{ac},\\
[\Omega_\mu,\mathsf T]
&=\gamma^{ab}
 (-\omega_\mu{}^c{}_aT_{cb}-\omega_\mu{}^c{}_bT_{ac})\\
&=\gamma^{ab}\,2\omega_\mu{}^c{}_{[a}T_{b]c}.
\end{aligned}
```

The positive-sign tensor derivative satisfies the covariant product rule. With the negative-sign derivative, the left-hand side minus the right-hand side is

```math
4\gamma^{ab}\omega_\mu{}^c{}_{[a}T_{b]c}\,\xi
```

which does not vanish identically. For example, the independent monomial $`\omega_\mu{}^{12}T_{23}`$ contributes $`4\omega_\mu{}^{12}T_{23}\gamma^{13}\xi`$. Selecting this coefficient does not set the other fields to zero.

Working result in the original variables and equivalent index notation:

```math
\boxed{\left.\mathcal D_\mu T_{ab}\right|_\omega
=+2\omega_\mu{}^c{}_{[a}T_{b]c},}
\qquad
-2\omega_\mu{}^c{}_{[a}T_{|c|b]}
=+2\omega_\mu{}^c{}_{[a}T_{b]c}.
```

This correction determines only the Lorentz-connection term checked; it does not mean that all coefficients of the map's $`\varphi^i`$, $`N`$ and $`E_a`$ components have been rederived or verified.
