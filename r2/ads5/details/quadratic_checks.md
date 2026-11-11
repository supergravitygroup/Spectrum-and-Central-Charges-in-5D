# Quadratic action and linearized equations

[Reading guide](../README.md). The equation labels and local symbols below follow the action conventions specified for this theory.

<a id="8-independent-check-of-the-quadratic-action-and-linearized-equations"></a>

## Independent check of the quadratic action and linearized equations

Two routes were compared: expanding the action to second order and then varying it; and varying the original action in the independent fields before linearizing. The check concerns
```math
\frac1{\bar e}\frac{\delta S^{(2)}}{\delta\eta^A}
=\left[\frac1e\frac{\delta S}{\delta\Phi^A}\right]^{(1)}
```
For fermions, left variation and the same bilinear normalization are used.

After imposing the background polynomial, the first variation is the total derivative
```math
\frac{\mathcal L^{(1)}}{\bar e}
=A(\nabla_\mu\nabla_\nu h^{\mu\nu}-\Box h)
-\frac{2A}{L}\Box s+\frac{\lambda\rho'_0}{2}\Box\rho'_1
```
This term does not automatically vanish for arbitrary variations at a finite boundary.

With the definitions
```math
X=(1-5\lambda g^2L)s-3\lambda gn+\frac\lambda2(r_1-2\Box s/L),
\quad q=-2g^2L^2=-4\ell^{-2}
```
one obtains
```math
\mathscr G_{\mu\nu}=R_{1\mu\nu}-\frac12\bar g_{\mu\nu}r_1-qh_{\mu\nu},\qquad
\mathscr P_{\mu\nu}=\nabla_\mu\nabla_\nu-\bar g_{\mu\nu}\Box-q\bar g_{\mu\nu}
```
and
```math
\mathcal E_h=-A\mathscr G(h)+\mathscr PX
```
The scalar equations are
```math
\begin{aligned}
\mathcal E_s={}&(1-5\lambda g^2L)r_1-\frac\lambda L\Box(r_1-2\Box s/L)
+g^2(4-12L+53\lambda g^2L^2)s\\
&+g(-8+48\lambda g^2L)n-(2/L-23\lambda g^2)\Box s
+\frac{12\lambda g}{L}\Box n,\\
\mathcal E_n={}&-3\lambda gr_1+g(-8+48\lambda g^2L)s
+(-4/L+38\lambda g^2)n+\frac{12\lambda g}{L}\Box s
+\frac{4\lambda}{L^2}\Box n
\end{aligned}
```

For the form Euler equations, the temporary coefficients
```math
\begin{aligned}
P_G^{ab}&=-\left(A+\frac92\lambda g^2L^2\right)\mathsf G^{ab}
-\frac32\lambda gL\mathsf F^{ab}-\frac92\lambda g^2L^2Q^{ab},\\
P_F^{ab}&=-\frac\lambda2[\mathsf F^{ab}+3gL(\mathsf G^{ab}+2Q^{ab})],\\
P_H^{abc}&=-\frac{2A}{3}\mathsf H^{abc}
+\frac16\varepsilon_{de}{}^{abc}
[-3\lambda gL\mathsf F^{de}-\tfrac92\lambda g^2L^2\mathsf G^{de}],\\
J_{\mathcal A}^a&=-2\nabla_bP_F^{ba},\quad
Z^a=-2(2/L+6\lambda g^2)\mathsf E^a-2\sqrt2v^a-4gc^a+2J_{\mathcal A}^a/L
\end{aligned}
```
give
```math
\begin{aligned}
\mathcal E_c^a&=-2\nabla_bP_G^{ba}-4g\mathsf E^a,&
\mathcal E_v^a&=\sqrt2J_{\mathcal A}^a-2\sqrt2\mathsf E^a,\\
\mathcal E_b^{ab}&=-3\nabla_cP_H^{cab},&
\mathcal E_a^{abc}&=\frac g2P_H^{abc}
+\frac1{12}\varepsilon^{\mu\nu abc}\nabla_\nu Z_\mu,\\
\mathcal E_w^{aij}&=4Aw^{aij}-4\lambda\nabla^a\nabla_bw^{bij}.
\end{aligned}
```
No extra factorial is inserted before the form variations.

For fermions, using $`\mathscr R^\sharp=-\mathscr R`$ and $`\mathcal H^\sharp=-\mathcal H`$ gives
```math
\begin{aligned}
\mathcal E_\Psi^\mu={}&-2A\mathscr R^\mu\Psi
-\frac{4iA}{3L}\mathscr R^\mu(\gamma\mathbb I\zeta)
-\frac{2\lambda}{3}\mathscr R^\mu(\gamma\mathbb I\mathcal H\Lambda),\\
\mathcal E_\zeta={}&\frac{4A}{L^2}\mathord{\not{\nabla}}\zeta
+\frac{14igA}{L}\mathbb I\zeta
+\frac{4iA}{3L}\mathbb I\gamma_\mu\mathscr R^\mu\Psi
-\frac{2i\lambda}{L}\mathcal K_F\mathcal H\Lambda
\end{aligned}
```
Since $`\delta\Lambda=(2/3)\mathbb I\gamma\mathscr R\delta\Psi-(2i/L)\mathcal K_F\delta\zeta`$ is retained, the composite spinor has not been varied independently.

The linearized gauge identities are
```math
\nabla_\mu\mathcal E_h^{\mu\nu}=0,\quad
\nabla\cdot\mathcal E_c=\nabla\cdot\mathcal E_v=0,\quad
\nabla_a\mathcal E_b^{ab}=0,
```
```math
3\nabla_a\mathcal E_a^{abc}+\frac g2\mathcal E_b^{bc}=0,
\qquad
(-\nabla_\mu+m\mathbb J\gamma_\mu)\mathcal E_\Psi^\mu\equiv0
```
For example, $`3(g/2)\nabla P_H`$ and $`(g/2)(-3\nabla P_H)`$ cancel in the form identity. In the metric identity,
```math
\nabla_\mu\mathscr P^{\mu\nu}X
=[\Box,\nabla^\nu]X-q\nabla^\nu X
=(\bar R^{\nu\rho}-q\bar g^{\nu\rho})\nabla_\rho X=0.
```
These checks concern the bulk quadratic calculation; they are not a check of general nonlinear SUSY invariance at all fermion orders.

