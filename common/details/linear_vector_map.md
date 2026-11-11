# Scalar and spinor transformations of the common linear–vector map

<a id="1-input-and-degree"></a>

## Input and degree

The [source map](linear_vector_construction.md) defines the components $`(\rho_1,\lambda_1^i,Y_1^{ij},\widehat F_{1ab})`$ used in the two-derivative and $`R^2`$ constructions. The equations checked in this appendix are

```math
\begin{aligned}
[\delta_Q\rho_1]_1&=\frac i2\bar\epsilon^i\lambda_{1i}^{(1)},&
[\delta_S\rho_1]_1&=0,\\
[\delta_Q\lambda_1^i]_0
&=-\frac14\gamma^{ab}F_{1ab}^{(0)}\epsilon^i
 -\frac i2\gamma^a\mathcal D_a\rho_1^{(0)}\epsilon^i
 +\rho_1^{(0)}\gamma^{ab}T_{ab}\epsilon^i-Y_1^{ij(0)}\epsilon_j,&
[\delta_S\lambda_1^i]_0&=\rho_1^{(0)}\eta^i
\end{aligned}
```

The branch $`L=\sqrt{L_{ij}L^{ij}}>0`$ is retained. The quantity $`L`$ is not fixed as a gauge constant. These equations use Standard-Weyl covariants; gauged composite substitutions use the same field definitions specified in the [shared dictionary](../fields_and_derivatives.md).

<a id="2-scalar-variation"></a>

## Scalar variation

The required map components are

```math
\begin{aligned}
\rho_1^{(0)}&=\frac{2N}{L},&
\rho_1^{(2)}&=\frac i{L^3}L^{ij}\bar\varphi_i\varphi_j,\\
\lambda_{1i}^{(1)}={}&-\frac{2i}{L}\mathord{\not{\mathcal D}}\varphi_i
 -\frac{2N}{L^3}L_{ij}\varphi^j
 -\frac{2i}{L^3}L_{ij}\mathord{\not{E}}\varphi^j\\
&+\frac{2i}{L^3}L^{jk}(\mathord{\not{\mathcal D}}L_{ij})\varphi_k
 +\frac{16}{L}L_{ij}\chi^j
 +\frac4L\gamma^{ab}T_{ab}\varphi_i
\end{aligned}
```

The quantity $`\mathcal D\varphi`$ includes the full one-fermion derivative coefficient; it is not replaced by $`\nabla\varphi`$. The norm variation is

```math
\delta L=\frac{L_{ij}}L\delta L^{ij}
=\frac iL L_{ij}\bar\epsilon^i\varphi^j
```

so the first part is

```math
\begin{aligned}
[\delta(2N/L)]_1
={}&\frac1L\bar\epsilon\mathord{\not{\mathcal D}}\varphi
 +\frac{3i}{L}\bar\epsilon\gamma^{ab}T_{ab}\varphi
 +\frac{8i}{L}L_{ij}\bar\epsilon^i\chi^j
 +\frac{3i}{L}\bar\eta\varphi\\
&-\frac{2iN}{L^3}L_{ij}\bar\epsilon^i\varphi^j.
\end{aligned}
```

In the second part, varying the coefficient produces fermion degree three; its one-fermion coefficient comes only from varying the two fermions separately:

```math
[\delta\rho_1^{(2)}]_1
=\frac i{L^3}L^{ij}\left[
 \overline{\delta\varphi_i}\varphi_j+\bar\varphi_i\delta\varphi_j\right]_1.
```

Substituting the [linear-multiplet transformation](vector_linear_density.md) and putting both contributions in the same order using the open-index flip gives

```math
\begin{aligned}
[\delta\rho_1^{(2)}]_1={}&
\frac{iN}{L^3}L_{ij}\bar\epsilon^i\varphi^j
 -\frac iL\bar\epsilon\gamma^{ab}T_{ab}\varphi
 -\frac{3i}{L}\bar\eta\varphi\\
&+\frac1{L^3}L_{ij}\bar\epsilon^i\mathord{\not{E}}\varphi^j
 -\frac1{L^3}L^{jk}\bar\epsilon^i
       (\mathord{\not{\mathcal D}}L_{ij})\varphi_k.
\end{aligned}
```

Here the contraction $`SU(2)`$ uses $`L^{ik}L_{kj}=L^2\delta^i{}_j/2`$. For example, if $`L^{ij}=\left(\begin{smallmatrix}a&b\\b&c\end{smallmatrix}\right)`$,

```math
L_{ij}=\begin{pmatrix}c&-b\\-b&a\end{pmatrix},qquad
L^{ik}L_{kj}=(ac-b^2)\delta^i{}_j,qquad L^2=2(ac-b^2).
```

The quantities $`a,b,c`$ are independent symbolic components. In the sum, the $`\eta`$ terms give $`3i/L-3i/L=0`$, the coefficient of $`N`$ is $`-2i+i=-i`$, and that of $`T`$ is $`3i-i=2i`$. The other three terms remain unchanged:

```math
\begin{aligned}
[\delta\rho_1]_1={}&\frac1L\bar\epsilon\mathord{\not{\mathcal D}}\varphi
 -\frac{iN}{L^3}L_{ij}\bar\epsilon^i\varphi^j
 +\frac1{L^3}L_{ij}\bar\epsilon^i\mathord{\not{E}}\varphi^j\\
&-\frac1{L^3}L^{jk}\bar\epsilon^i
 (\mathord{\not{\mathcal D}}L_{ij})\varphi_k
 +\frac{8i}{L}L_{ij}\bar\epsilon^i\chi^j
 +\frac{2i}{L}\bar\epsilon\gamma^{ab}T_{ab}\varphi\\
&=\boxed{\frac i2\bar\epsilon^i\lambda_{1i}^{(1)}}.
\end{aligned}
```

<a id="3-calculating-the-gaugino-variation"></a>

## Calculating the gaugino variation

Introduce the temporary matrices $`\varepsilon=\left(\begin{smallmatrix}0&1\\-1&0\end{smallmatrix}\right)`$, $`U=(L^{ij})`$, and $`D_L=\varepsilon^TU\varepsilon`$. In this section, $`D_L`$ is neither a derivative nor the auxiliary field $`D`$. Using upper spinor components as columns gives $`\varphi_i=-(\varepsilon\varphi)_i`$ and

```math
\begin{aligned}
\lambda_1^{(1)}={}&-\frac{2i}{L}\gamma^a\mathcal D_a\varphi
 -\frac{2N}{L^3}U\varepsilon\varphi
 -\frac{2i}{L^3}U\varepsilon\gamma^aE_a\varphi\\
&-\frac{2i}{L^3}(\mathcal D_aU)\varepsilon U\varepsilon\gamma^a\varphi
 +\frac{16}{L}U\varepsilon\chi
 +\frac4L\gamma^{ab}T_{ab}\varphi.
\end{aligned}
```

The bosonic coefficients of the transformation are defined by

```math
\begin{aligned}
M_\varphi&=\frac i2(\nabla_aU)\varepsilon\gamma^a
 -\frac i2\gamma^aE_a+\frac12N
 +U\varepsilon\gamma^{ab}T_{ab},& N_\varphi&=-3U\varepsilon,\\
[\delta_Q\varphi]_0&=M_\varphi\epsilon,&
[\delta_S\varphi]_0&=N_\varphi\eta
\end{aligned}
```

The quantities $`M_\chi,N_\chi,\Phi_{Q,a},\Phi_{S,a}`$ are the same explicit operators as in [§§1 and 3 of the Weyl-transformation derivation](../../weyl2/action/multiplet_derivations.md). The relation $`\mathcal D_a\varphi=\nabla_a\varphi -M_\varphi\psi_a-N_\varphi\phi_a`$ gives

```math
\begin{aligned}
[\delta_Q(\mathcal D_a\varphi)]_0
&=(\nabla_aM_\varphi-iM_\varphi\gamma^{bc}T_{bc}\gamma_a
 -N_\varphi\Phi_{Q,a})\epsilon,\\
[\delta_S(\mathcal D_a\varphi)]_0
&=(\nabla_aN_\varphi+iM_\varphi\gamma_a
 -N_\varphi\Phi_{S,a})\eta
\end{aligned}
```

These two lines are substituted into the first term of $`\lambda_1`$ above; $`M_\varphi,N_\varphi`$ is substituted into the other $`\varphi`$ terms, and $`M_\chi,N_\chi`$ into the $`\chi`$ term.

The equations used to reduce second derivatives are:

```math
\begin{aligned}
\nabla_aL&=\frac1L L_{ij}\nabla_aL^{ij},\\
\nabla_a\nabla_bU
&=\nabla_{(a}\nabla_{b)}U
 +\frac12\left[\widehat R_{ab}(V)\varepsilon U
 +U(\widehat R_{ab}(V)\varepsilon)^T\right],\\
[\Box^cL_{ij}]_0&=\nabla^a\nabla_aL_{ij}+6f_a{}^aL_{ij}
=\nabla^a\nabla_aL_{ij}-\frac38RL_{ij},\\
\nabla^aE_a&=0,qquad L^2=2\det U.
\end{aligned}
```

The divergence condition is the specified linear-multiplet constraint, not a new equation of motion. The coefficient $`6f_a{}^a`$ comes from $`K_m\nabla_aL_{ij}=-6\eta_{ma}L_{ij}`$.

<a id="4-final-components-and-back-substitution"></a>

## Final components and back-substitution

The separate gamma coefficients of the variation are the following bosonic components:

```math
\begin{aligned}
Y_{1ij}^{(0)}={}&\frac1L\Box^cL_{ij}
 -\frac{L_{ij}}{L^3}(N^2+E_aE^a)
 -\frac{L^{km}}{L^3}\mathcal D_aL_{ki}\mathcal D^aL_{jm}\\
&-\frac2{L^3}L_{(i}{}^kE_a\mathcal D^aL_{j)k}
 +\frac{4L_{ij}}L\left(D+\frac23T^2\right),\\
F_{1ab}^{(0)}={}&\frac4L\mathcal D_{[a}E_{b]}
 -\frac4{L^3}L^{ij}(\mathcal D_{[a}L_{ij})E_{b]}
 +\frac2L\widehat R_{ab}^{ij}(V)L_{ij}\\
&-\frac2{L^3}L_k{}^l(\mathcal D_aL^{kp})(\mathcal D_bL_{lp}).
\end{aligned}
```

Right-hand sides in this section are evaluated at fermion degree zero. For example, the term $`N^2`$ directly gives

```math
\left.\delta\left(-\frac{2N}{L^3}L_{ij}\varphi^j\right)\right|_{N^2}
=-\frac{2N}{L^3}L_{ij}\left(\frac12N\epsilon^j\right)
=-\frac{N^2}{L^3}L_{ij}\epsilon^j
```

Together with the $`+Y_{1ij}\epsilon^j`$ sign in the lower-index gaugino transformation, this fixes the displayed coefficient of $`Y_{1ij}^{(0)}`$.

The back-substitution residuals are defined as

```math
\begin{aligned}
\mathcal R_Q^i:={}&[\delta_Q\lambda_1^i]_0
 +\frac14\gamma^{ab}F_{1ab}^{(0)}\epsilon^i
 +\frac i2\gamma^a\nabla_a(2N/L)\epsilon^i
 -\frac{2N}{L}\gamma^{ab}T_{ab}\epsilon^i+Y_1^{ij(0)}\epsilon_j,\\
\mathcal R_S^i:={}&[\delta_S\lambda_1^i]_0-\frac{2N}{L}\eta^i
\end{aligned}
```

Both denominators are cleared using $`L^3`$, which is valid on the branch $`L>0`$. Polynomial division by $`L^2-2\det U`$, followed by the commutator, conformal-box, and divergence relations in §3, makes every Clifford coefficient vanish separately in both $`SU(2)`$ components:

```math
\boxed{\mathcal R_Q^i=0,qquad\mathcal R_S^i=0.}
```

No numerical values were assigned to the free components $`N,L,E,T,D`$, curvatures, or derivatives. Division does not establish a result on the $`L=0`$ branch. The result verifies the scalar and spinor transformations specified in §1.
