# SUSY variation of the two-fermion vector–linear density

<a id="1-identity-being-checked"></a>

## Identity being checked

The notation $`[\;]_n`$ selects physical fermion degree $`n`$. The SUSY parameter is not a physical fermion in this counting. The retained-order condition is

```math
[\delta\mathcal L]_1
=\delta_{+1}\mathcal L^{(0)}+\delta_{-1}\mathcal L^{(2)}
=\partial_\mu(eJ^\mu)
```

Here $`\delta_{-1}`$ replaces a physical fermion by its bosonic variation, while $`\delta_{+1}`$ replaces a bosonic field by its one-fermion variation. Varying a four-fermion action term cannot contribute to this identity: $`4-1=3`$.

The target of this file is the **general vector–linear density**, with every term written below. The vector- and linear-multiplet components are independent in this calculation. Application to a composite map assumes that it obeys these multiplet transformations.

Conventions are given in the [shared dictionary](../fields_and_derivatives.md) and the [root-convention source](source_conventions.md). Input transformations are [W01, L01–L02, V01–V02, A02](../../log/action/details/covariant_rules.md). The results below come from directly varying these inputs, not from source verification labels.

<a id="2-density-and-transformations-used"></a>

## Density and transformations used

Let the vector multiplet be $`(\rho,A_\mu,\lambda^i,Y^{ij})`$ and the linear multiplet $`(L^{ij},\varphi^i,E_a,N)`$. The field $`\varphi`$ and the dependent $`S`$ connection $`\phi_a`$ are distinct. We use the abbreviations

```math
\mathsf T:=T_{ab}\gamma^{ab},\qquad
\mathsf F:=F_{ab}\gamma^{ab},\qquad
F_{ab}:=e_a{}^\mu e_b{}^\nu,2\partial_{[\mu}A_{\nu]}
```

Here $`\nabla_a`$ denotes the part of the full supercovariant derivative containing only bosonic connections. It is not the same operator as $`\mathcal D`$. When a variation below requires its zero-fermion coefficient, $`T,F,L,Y,E,N`$ denotes that coefficient; no free field is assigned a numerical value.

```math
\begin{aligned}
P^a&=E^a+\frac i2\bar\psi_b\gamma^{ba}\varphi
 +\frac14L_{ij}\bar\psi_b^i\gamma^{abc}\psi_c^j,\\
\ell_{VL}&=Y^{ij}L_{ij}+\rho N+A_aP^a+i\bar\lambda\varphi
 -\frac12L_{ij}\bar\psi_a^i\gamma^a\lambda^j\\
&\quad+\frac\rho2\bar\psi_a\gamma^a\varphi
 +\frac{i\rho}{4}L_{ij}\bar\psi_a^i\gamma^{ab}\psi_b^j,qquad
\mathcal L_{VL}=e\ell_{VL}.
\end{aligned}
```

Required fermion transformations:

```math
\begin{aligned}
[\delta\psi_a^i]_0&=\nabla_a\epsilon^i+i\mathsf T\gamma_a\epsilon^i
 -i\gamma_a\eta^i,\\
[\delta\lambda^i]_0&=-\frac14\mathsf F\epsilon^i
 -\frac i2\gamma^a\nabla_a\rho\,\epsilon^i
 +\rho\mathsf T\epsilon^i-Y^{ij}\epsilon_j+\rho\eta^i,\\
[\delta\varphi^i]_0&=-\frac i2\gamma^a\nabla_aL^{ij}\epsilon_j
 -\frac i2\gamma^aE_a\epsilon^i+\frac12N\epsilon^i
 -\mathsf T L^{ij}\epsilon_j+3L^{ij}\eta_j.
\end{aligned}
```

One-fermion transformations of bosonic fields:

```math
\begin{aligned}
\delta e/e&=\frac12\bar\epsilon\gamma^a\psi_a,&
\delta\rho&=\frac i2\bar\epsilon\lambda,\\
\delta A_\mu&=-\frac i2\rho\bar\epsilon\psi_\mu
 +\frac12\bar\epsilon\gamma_\mu\lambda,&
\delta L^{ij}&=i\bar\epsilon^{(i}\varphi^{j)},\\
\delta Y^{ij}&=-\frac12\bar\epsilon^{(i}\mathord{\not{\mathcal D}}\lambda^{j)}
 +\frac i2\bar\epsilon^{(i}\mathsf T\lambda^{j)}
 -4i\rho\bar\epsilon^{(i}\chi^{j)}
 +\frac i2\bar\eta^{(i}\lambda^{j)},\\
\delta N&=\frac12\bar\epsilon\mathord{\not{\mathcal D}}\varphi
 +\frac{3i}{2}\bar\epsilon\mathsf T\varphi
 +4iL_{ij}\bar\epsilon^i\chi^j+\frac{3i}{2}\bar\eta\varphi,\\
\delta E_a&=-\frac i2\bar\epsilon\gamma_{ab}\mathcal D^b\varphi
 -2\bar\epsilon\gamma^b\varphi T_{ba}-2\bar\eta\gamma_a\varphi.
\end{aligned}
```

One-fermion contributions inside derivatives are used explicitly:

```math
\begin{aligned}
[\mathcal D_a\lambda^i]_1={}&\nabla_a\lambda^i
 +\frac14\mathsf F\psi_a^i+\frac i2\gamma^b\nabla_b\rho\,\psi_a^i
 +Y^{ij}\psi_{aj}-\rho\mathsf T\psi_a^i-\rho\phi_a^i,\\
[\mathcal D_a\varphi^i]_1={}&\nabla_a\varphi^i
 +\frac i2\gamma^b\nabla_bL^{ij}\psi_{aj}
 +\frac i2\gamma^bE_b\psi_a^i-\frac12N\psi_a^i
 +\mathsf T L^{ij}\psi_{aj}-3L^{ij}\phi_{aj}.
\end{aligned}
```

<a id="3-clifford-and-connection-identities"></a>

## Clifford and connection identities

The open-index flip $`t_n=(-1)^{n(n-1)/2}`$, $`n=0,\ldots,5`$ reverses Clifford-product order. Thus, in computing $`\overline{M\epsilon}\,\Gamma X`$, the gamma products in $`M`$ are reversed. This directly uses the given flip relation twice and introduces no new complex-conjugation convention. For example,

```math
\overline{i\mathsf T\gamma_a\epsilon}^{\,i}\gamma^bX^j
=-i\bar\epsilon^i\gamma_a\mathsf T\gamma^bX^j.
```

Required five-dimensional anticommutator reductions:

```math
\begin{aligned}
\gamma_a\gamma^{ab}&=4\gamma^b,&
\gamma_b\gamma^{abc}&=-3\gamma^{ac},\\
\gamma_a\mathsf T\gamma^a&=(5-4)\mathsf T=\mathsf T,&
\{\gamma^a,\mathsf F\}&=2F_{bc}\gamma^{abc},\\
[\gamma^{ab},\gamma^c]&=2(\eta^{bc}\gamma^a-\eta^{ac}\gamma^b),&
\{\gamma^{ab},\gamma^c\}&=2\gamma^{abc},\\
\gamma_b\mathsf T\gamma^{ba}&=[\mathsf T,\gamma^a]
=-4T^a{}_b\gamma^b,&
\gamma_a\mathsf T\gamma^{ab}&=\gamma^{ab}\mathsf T\gamma_a,\\
[\gamma^{ac},\mathsf T]
-\gamma_b\mathsf T\gamma^{abc}
+\gamma^{abc}\mathsf T\gamma_b&=0.
\end{aligned}
```

In the last three lines, substitute $`\mathsf T=T_{cd}\gamma^{cd}`$ and use $`\gamma^a\gamma^b=\gamma^{ab}+\eta^{ab}`$; $`T_{cd}\eta^{cd}=0`$ and $`T_{cd}=-T_{dc}`$ remove symmetric parts. For example, the first commutator is

```math
T_{cd}[\gamma^{cd},\gamma^a]
=2T_{cd}(\eta^{da}\gamma^c-\eta^{ca}\gamma^d)
=-4T^a{}_b\gamma^b
```

All gamma identities were also checked in an antisymmetric Clifford basis while retaining every $`T_{cd}`$ coefficient separately.

The solution $`\phi`$ in the [dependent-connection derivation](composite_fields.md) yields two contractions:

```math
\begin{aligned}
\gamma^{ab}R'_{ab}(Q)&=-8i\gamma^a\phi_a,\\
\gamma^{abc}R'_{bc}(Q)&=-6i\gamma^{ab}\phi_b.
\end{aligned}
```

To see the second, write $`q_a:=\gamma^bR'_{ba}(Q)`$ and $`q:=\gamma^{ab}R'_{ab}(Q)`$. The definition and first contraction give

```math
\phi_a=-\frac i3q_a-\frac i{24}\gamma_aq,qquad
q_a=3i\phi_a-\frac18\gamma_aq,qquad q=-8i\gamma^a\phi_a
```

and hence

```math
\begin{aligned}
\gamma^{abc}R'_{bc}(Q)
&=\gamma^a q+2q^a
=\frac34\gamma^a q+6i\phi^a\\
&=-6i\gamma^a\gamma^b\phi_b+6i\phi^a
=-6i\gamma^{ab}\phi_b.
\end{aligned}
```

Using $`R'_{ab}(Q)=2\nabla_{[a}\psi_{b]}+2i\mathsf T\gamma_{[a}\psi_{b]}`$, this implies

```math
\begin{aligned}
\gamma^{ab}\nabla_a\psi_b
&=-4i\gamma^a\phi_a-i\gamma^{ab}\mathsf T\gamma_a\psi_b,\\
\gamma^{abc}\nabla_b\psi_c
&=-3i\gamma^{ab}\phi_b-i\gamma^{abc}\mathsf T\gamma_b\psi_c
\end{aligned}
```

These follow from the algebraic definition of the dependent $`S`$ connection, not from a gravitino equation of motion.

<a id="4-variation-of-the-three-form-current"></a>

## Variation of the three-form current

Define the antisymmetric tensor:

```math
Q^{ab}:=-\frac i2\bar\epsilon\gamma^{ab}\varphi
 +\frac12L_{ij}\bar\epsilon^i\gamma^{abc}\psi_c^j,qquad
Q^{\mu\nu}=e_a{}^\mu e_b{}^\nu Q^{ab}.
```

The determinant and inverse vielbein both contribute to the coordinate-density variation:

```math
e_\mu{}^a e^{-1}\delta(eP^\mu)
=\delta E^a+\frac12E^a\bar\epsilon\gamma^b\psi_b
-\frac12E^b\bar\epsilon\gamma^a\psi_b
+\delta\left(\frac i2\bar\psi_b\gamma^{ba}\varphi
+\frac14L_{ij}\bar\psi_b^i\gamma^{abc}\psi_c^j\right)
```

Here the one-fermion coefficient is selected. With the transformations in §2, the $`\nabla\epsilon`$ and $`\nabla\varphi`$ terms become

```math
-\frac i2\left[(\nabla_b\bar\epsilon)\gamma^{ab}\varphi
+\bar\epsilon\gamma^{ab}\nabla_b\varphi\right]
+\frac12L_{ij}(\nabla_b\bar\epsilon^i)\gamma^{abc}\psi_c^j
```

The remaining terms have the following explicit reductions:

```math
\begin{aligned}
\varphi T:&\quad
2T^a{}_b\bar\epsilon\gamma^b\varphi
+\frac12\bar\epsilon\gamma_b\mathsf T\gamma^{ba}\varphi=0,\\
\eta\varphi:&\quad
-2\bar\eta\gamma^a\varphi
+\frac12\bar\eta\gamma_b\gamma^{ba}\varphi=0,\\
N\psi:&\quad
\frac{iN}{4}\bar\epsilon(\gamma^{ab}+\gamma^{ba})\psi_b=0,\\
E\psi:&\quad
\frac12\bar\epsilon(E^a\gamma^b-E^b\gamma^a)\psi_b
+\frac14\bar\epsilon[\gamma^{ab},\gamma^c]E_c\psi_b=0,\\
\nabla L\,\psi:&\quad
-\frac14(\nabla_cL_{ij})\bar\epsilon^i
 \{\gamma^{ab},\gamma^c\}\psi_b^j
=\frac12(\nabla_bL_{ij})\bar\epsilon^i\gamma^{abc}\psi_c^j,\\
\eta\psi:&\quad
-\frac{3i}{2}L_{ij}\bar\eta^i\gamma^{ab}\psi_b^j
-\frac i2L_{ij}\bar\eta^i\gamma_b\gamma^{abc}\psi_c^j=0,\\
\phi:&\quad
-\frac{3i}{2}L_{ij}\bar\epsilon^i\gamma^{ab}\phi_b^j,\\
T\psi:&\quad
\frac i2L_{ij}\bar\epsilon^i
\left([\gamma^{ac},\mathsf T]-\gamma_b\mathsf T\gamma^{abc}\right)\psi_c^j
=-\frac i2L_{ij}\bar\epsilon^i\gamma^{abc}\mathsf T\gamma_b\psi_c^j.
\end{aligned}
```

The last two lines sum to $`L_{ij}\bar\epsilon^i\gamma^{abc}\nabla_b\psi_c^j/2`$ by the second connection identity in §3. Combining all terms with the product rule gives

```math
\boxed{[\delta(eP^\mu)]_1=\partial_\nu(eQ^{\mu\nu}).}
```

No hidden dilatation-connection residual remains: because $`w(Q^{ab})=3`$, $`w(Q^{\mu\nu})=5`$, and $`w(e)=-5`$, the object $`eQ^{\mu\nu}`$ is an antisymmetric density of weight zero. Its covariant density divergence equals the ordinary derivative displayed above.

<a id="5-potential-transformation-and-convention-conversion"></a>

## Potential transformation and convention conversion

Using the definition $`P^\mu=-e^{-1}\epsilon^{\mu\nu\rho\sigma\lambda} \partial_\nu E_{\rho\sigma\lambda}/12`$, solve

```math
-\frac1{12}\epsilon^{\mu\nu\rho\sigma\lambda}
\partial_\nu[\delta E_{\rho\sigma\lambda}]_1
=\partial_\nu(eQ^{\mu\nu})
```

Epsilon contraction and gamma duality give

```math
\varepsilon_{abcde}\gamma^{de}=2i\gamma_{abc},qquad
\varepsilon_{abcde}\gamma^{def}
=6i\delta_{[a}{}^f\gamma_{bc]}
```

and therefore

```math
\begin{aligned}
[\delta E_{abc}]_1
&=\varepsilon_{abcde}Q^{de}\\
&=\bar\epsilon\gamma_{abc}\varphi
+3iL_{ij}\bar\epsilon^i\gamma_{[ab}\psi_{c]}^j\\
&=\bar\epsilon\gamma_{abc}\varphi
-3iL_{ij}\bar\psi_{[a}^i\gamma_{bc]}\epsilon^j.
\end{aligned}
```

Here $`\delta E_{abc}`$ means $`e_a{}^\mu e_b{}^\nu e_c{}^\rho \delta E_{\mu\nu\rho}`$, not the total variation of the vielbein-converted potential. In the original coordinate field, including the free three-form gauge parameter, the result is

```math
\boxed{
[\delta E_{\mu\nu\rho}]_1=
\bar\epsilon\gamma_{\mu\nu\rho}\varphi
-3iL_{ij}\bar\psi_{[\mu}^i\gamma_{\nu\rho]}\epsilon^j
+3\partial_{[\mu}\Lambda_{\nu\rho]}.}
```

The two literal potential rules in source line L04 are not used together. The coefficients $`(+1,-3)`$ above are fixed by the transformation $`E_a`$, the completion $`P^a`$, and the root gamma-duality convention. For example, its $`\varphi`$ contribution to gauged $`T_{ab}`$ is

```math
\left[\delta T_{ab}\right]_{g\varphi}
=\frac1{48}\varepsilon_{abcde}\frac g2
\bar\epsilon\gamma^{cde}\varphi
=\frac{ig}{16}\bar\epsilon\gamma_{ab}\varphi
=\left[\frac i2\bar\epsilon\gamma_{ab}\chi\right]_{g\varphi},
\qquad \chi\supset\frac g8\varphi.
```

The same sign is therefore preserved in the gauged-composite transformation.

<a id="6-density-variation-and-boundary-current"></a>

## Density variation and boundary current

By §4, the three-form contribution is directly

```math
\begin{aligned}
[\delta(eA_\mu P^\mu)]_1
&=eE^\mu\delta A_\mu+A_\mu\partial_\nu(eQ^{\mu\nu})\\
&=eE^\mu\delta A_\mu+\frac e2F_{\mu\nu}Q^{\mu\nu}
 +\partial_\nu(eA_\mu Q^{\mu\nu})
\end{aligned}
```

The sign of $`FQ`$ is positive because $`-(\partial_\nu A_\mu)Q^{\mu\nu}=F_{\mu\nu}Q^{\mu\nu}/2`$.

Vary the seven remaining terms separately:

```math
\begin{aligned}
e^{-1}\delta\!\left[e(\ell_{VL}-A_aP^a)\right]
={}&\frac12\bar\epsilon\gamma^a\psi_a(Y^{ij}L_{ij}+\rho N)
 +(\delta Y^{ij})L_{ij}+Y^{ij}\delta L_{ij}
 +(\delta\rho)N+\rho\delta N\\
&+i(\delta\bar\lambda)\varphi+i\bar\lambda\delta\varphi\\
&-\frac12L_{ij}\left[(\delta\bar\psi_a^i)\gamma^a\lambda^j
 +\bar\psi_a^i\gamma^a\delta\lambda^j\right]\\
&+\frac\rho2\left[(\delta\bar\psi_a)\gamma^a\varphi
 +\bar\psi_a\gamma^a\delta\varphi\right]\\
&+\frac{i\rho}{4}L_{ij}\left[(\delta\bar\psi_a^i)\gamma^{ab}\psi_b^j
 +\bar\psi_a^i\gamma^{ab}\delta\psi_b^j\right].
\end{aligned}
```

Only the one-fermion coefficient is retained. Substituting §2 gives the algebraic coefficients for the matter spinors:

| Structure | Sum of separate contributions |
|---|---|
| $`N\bar\epsilon\lambda`$ | $`i/2-i/2=0`$ |
| $`L_{ij}\bar\epsilon^i\mathsf T\lambda^j`$ | $`i/2-i+i/2=0`$ |
| $`L_{ij}\bar\eta^i\lambda^j`$ | $`i/2-3i+5i/2=0`$ |
| $`E_a\bar\epsilon\gamma^a\lambda`$ | $`-1/2+1/2=0`$ |
| $`Y_{ij}\bar\epsilon^i\varphi^j`$ | $`i-i=0`$ |
| $`\bar\epsilon\mathsf F\varphi`$ | $`i/4-i/4=0`$ |
| $`\rho\bar\epsilon\mathsf T\varphi`$ | $`3i/2-i-i/2=0`$ |
| $`\rho\bar\eta\varphi`$ | $`3i/2+i-5i/2=0`$ |
| $`\rho L_{ij}\bar\epsilon^i\chi^j`$ | $`-4i+4i=0`$ |

The derivative terms, using the temporary current $`K_{\rm mat}^a`$, are

```math
\begin{aligned}
K_{\rm mat}^a&:=-\frac12L_{ij}\bar\epsilon^i\gamma^a\lambda^j
 +\frac\rho2\bar\epsilon\gamma^a\varphi,\\
\nabla_aK_{\rm mat}^a
&=-\frac12(\nabla_aL_{ij})\bar\epsilon^i\gamma^a\lambda^j
 -\frac12L_{ij}(\nabla_a\bar\epsilon^i)\gamma^a\lambda^j
 -\frac12L_{ij}\bar\epsilon^i\gamma^a\nabla_a\lambda^j\\
&\quad+\frac12(\nabla_a\rho)\bar\epsilon\gamma^a\varphi
 +\frac\rho2(\nabla_a\bar\epsilon)\gamma^a\varphi
 +\frac\rho2\bar\epsilon\gamma^a\nabla_a\varphi.
\end{aligned}
```

Explicit cancellations of gravitino structures:

```math
\begin{aligned}
N\psi:&\quad \rho N\left(\frac12-\frac14-\frac14\right)
 \bar\epsilon\gamma^a\psi_a=0,\\
E\psi:&\quad \frac{i\rho}{4}\bar\epsilon
 \{\gamma^a,\gamma^b\}E_b\psi_a
 -\frac{i\rho}{2}E^a\bar\epsilon\psi_a=0,\\
F\psi:&\quad -\frac18L_{ij}\bar\epsilon^i
 \{\gamma^a,\mathsf F\}\psi_a^j
 +\frac14F_{bc}L_{ij}\bar\epsilon^i\gamma^{bca}\psi_a^j=0,\\
\eta\psi:&\quad \rho L_{ij}\bar\eta^i
 \left[-\frac12\gamma^a-\frac32\gamma^a
       +\frac12\gamma_b\gamma^{ba}\right]\psi_a^j=0.
\end{aligned}
```

To check the $`SU(2)`$ sign in the $`Y\psi`$ cancellation explicitly, write $`\varepsilon=\left(\begin{smallmatrix}0&1\\-1&0\end{smallmatrix}\right)`$ and $`L_\downarrow=\varepsilon^TL_\uparrow\varepsilon`$. For general symbolic symmetric matrices $`L_\uparrow,Y_\uparrow`$,

```math
L_\downarrow Y_\uparrow\varepsilon
+\varepsilon Y_\uparrow L_\downarrow
=(Y^{ij}L_{ij})\varepsilon.
```

The two terms on the left come from fermion variations; varying the determinant gives minus the right-hand side. No triplet component is fixed.

The gradients and remaining connection/flux terms are

```math
\begin{aligned}
\nabla(\rho L)\,\psi:&\quad
\frac i4\nabla_b(\rho L_{ij})\bar\epsilon^i
 [\gamma^b,\gamma^a]\psi_a^j
=\frac i2\nabla_a(\rho L_{ij})\bar\epsilon^i\gamma^{ab}\psi_b^j,\\
\nabla\epsilon\,\psi:&\quad
\frac{i\rho}{2}L_{ij}(\nabla_a\bar\epsilon^i)\gamma^{ab}\psi_b^j,\\
\phi+T\psi:&\quad
2\rho L_{ij}\bar\epsilon^i\gamma^a\phi_a^j
+\frac\rho2L_{ij}\bar\epsilon^i\gamma_a\mathsf T\gamma^{ab}\psi_b^j\\
&=\frac{i\rho}{2}L_{ij}\bar\epsilon^i\gamma^{ab}\nabla_a\psi_b^j
\end{aligned}
```

The last equality uses the connection and Clifford identities derived in §3. Together, these three lines give

```math
\nabla_aK_\psi^a,qquad
K_\psi^a:=\frac{i\rho}{2}L_{ij}\bar\epsilon^i\gamma^{ab}\psi_b^j
```

Expanding every temporary abbreviation, the result is:

```math
\boxed{
\begin{aligned}
[\delta(e\ell_{VL})]_1&=\partial_\mu(eJ_{VL}^{\mu}),\\
J_{VL}^{\mu}
&=-\frac12L_{ij}\bar\epsilon^i\gamma^\mu\lambda^j
 +\frac\rho2\bar\epsilon\gamma^\mu\varphi
 +\frac{i\rho}{2}L_{ij}\bar\epsilon^i\gamma^{\mu\nu}\psi_\nu^j\\
&\quad+A_\nu\left(-\frac i2\bar\epsilon\gamma^{\nu\mu}\varphi
 +\frac12L_{ij}\bar\epsilon^i\gamma^{\nu\mu\rho}\psi_\rho^j\right).
\end{aligned}}
```

Since $`w(K_{\rm mat}^a)=w(K_\psi^a)=4`$, we have $`w(e e_a{}^\mu K^a)=0`$. No dilatation connection or determinant factor is lost when converting the boundary current to a density. All $`S`$ terms cancel while $`\eta`$ remains independent. The $`K`$ and $`SU(2)`$ contributions vanish through the density's tensor contractions and multiplet weights. Thus subsequently substituting the [gauge-preserving parameters](gauge_compensations.md) does not change this identity.

At action level, without imposing a new boundary condition,

```math
\boxed{[\delta S_{VL}]_1=\int d^5x\,\partial_\mu(eJ_{VL}^{\mu})}
```

The right-hand side vanishes on a closed spacetime or for a class of variations that removes the boundary contribution; this file chooses no boundary condition.
