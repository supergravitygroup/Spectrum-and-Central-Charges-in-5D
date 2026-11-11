# R² on AdS5: fermion operator reduction

[Unreduced density and surface currents](fermionic_density.md) · [Linear equations](quadratic_checks.md)

The equations in this appendix are the recorded reduction in `SpectrumAnalysis/R^2/quadratic_action_ads5.bg`, §§10–11. They connect the unreduced component density to the compact Hessian and its Euler operators. Here $`L=L_0`$, $`A=A_0`$, and $`\lambda=\lambda_{R^2}`$; the [background equation and branch conditions](fermionic_density.md#background-and-notation) remain in force. The pairing is $`\langle X,Y\rangle=\int d^5x\,\bar e\,\bar X^iY_i`$, with any vector indices contracted.

## Bilinear transpose and composite operators

The internal matrix is defined by

```math
\mathbb I^i{}_j=\epsilon^{ik}\nu_{kj}
=\frac1{\sqrt2}\begin{pmatrix}0&1\\-1&0\end{pmatrix},\qquad
\mathbb I^2=-\tfrac12\mathbf1,\qquad \alpha=gL/2.
```

The contractions obey $`\langle X,Y\rangle=-\langle Y,X\rangle`$ and $`\langle X,\gamma_{(n)}Y\rangle=-t_n\langle Y,\gamma_{(n)}X\rangle`$. The operation $`\sharp`$ is the bilinear transpose including integration by parts:

```math
\langle OX,Y\rangle=\langle X,O^\sharp Y\rangle,\qquad
\nabla_a^\sharp=-\nabla_a,\quad
(\gamma^a)^\sharp=\gamma^a,\quad
(\gamma^{ab})^\sharp=-\gamma^{ab},\quad
\mathbb I^\sharp=-\mathbb I.
```

It is not the Hermitian adjoint and leaves the scalar $`i`$ unchanged. Hence

```math
\delta\langle X,OY\rangle
=\langle\delta X,OY\rangle-\langle\delta Y,O^\sharp X\rangle
```

In particular, an antisymmetric operator gives $`\delta\langle X,OX\rangle=2\langle\delta X,OX\rangle`$. With spinor indices raised, the linear composites are

```math
\begin{aligned}
\mathfrak k_a&=\alpha\mathbb I\Psi_a-\Phi_a,\\
\mathfrak p_a&=\nabla_a\zeta+\frac{3gL^2}4\Psi_a+3L\mathbb I\Phi_a
=\nabla_a\zeta-3L\mathbb I\mathfrak k_a,\\
\Xi&=\frac i8\gamma^a\mathfrak k_a+\frac g8\zeta,\\
\Lambda&=-\frac{2i}{L}\mathord{\not{\nabla}}\zeta
+8i\mathbb I\gamma^a\mathfrak k_a+5g\mathbb I\zeta,\\
\mathfrak W_a&=\nabla_a\Lambda-3gL\mathfrak k_a
\end{aligned}
\tag{F.1}
```

The cancellation in the second line uses $`3L\mathbb I(\alpha\mathbb I\Psi_a)=-3gL^2\Psi_a/4`$. Define the Rarita–Schwinger operator by

```math
\mathscr R^a(\Psi)=\gamma^{abc}\nabla_b\Psi_c
+\frac{3igL}2\gamma^{ab}\mathbb I\Psi_b
```

The gamma contractions retained in the source are

```math
\begin{aligned}
\gamma^{ab}\Phi_b
&=\gamma^a\gamma^b\Phi_b-\Phi^a
=\frac i6\gamma^a\gamma^{bc}\mathcal Q_{bc}
-\frac i3\gamma^b\mathcal Q^a{}_b,\\
3i\gamma^{ab}\Phi_b
&=-\tfrac12\gamma^a\gamma^{bc}\mathcal Q_{bc}
+\gamma^b\mathcal Q^a{}_b
=-\tfrac12\gamma^{abc}\mathcal Q_{bc},\\
3i\gamma^{ab}\mathfrak k_b&=\mathscr R^a(\Psi),\qquad
\gamma_a\mathscr R^a(\Psi)=12i\gamma^a\mathfrak k_a
\end{aligned}
\tag{F.2}
```

The composite spinor can therefore be written as

```math
\boxed{\Lambda=\frac23\mathbb I\gamma_a\mathscr R^a(\Psi)
+\left(-\frac{2i}{L}\mathord{\not{\nabla}}+5g\mathbb I\right)\zeta}
\tag{F.3}
```

## From the component density to the Hessian

All relations in this subsection are integrated bulk relations; $`\simeq`$ denotes a total derivative. The [surface currents](fermionic_density.md#surface-currents) remain part of the full action. The two integration-by-parts identities are

```math
\begin{aligned}
\langle\Psi_a,\gamma^{ab}\nabla_b\Lambda\rangle
&=-\langle\nabla_b\Psi_a,\gamma^{ab}\Lambda\rangle
=\tfrac12\langle\Lambda,\gamma^{ab}\mathcal Q_{ab}\rangle\\
&=-4i\alpha\langle\Psi_a,\gamma^a\mathbb I\Lambda\rangle
+4i\langle\Lambda,\gamma^a\mathfrak k_a\rangle,\\
\langle\Psi_a,\gamma^{ab}\mathbb I\nabla_b\zeta\rangle
&=2i\alpha\langle\Psi_a,\gamma^a\zeta\rangle
-4i\langle\zeta,\mathbb I\gamma^a\mathfrak k_a\rangle.
\end{aligned}
\tag{F.4}
```

The first line uses the rank-two flip and $`\gamma^{ab}\mathcal Q_{ab}=-8i\gamma^a\Phi_a`$. Substitution of (F.1) in the unreduced density cancels the explicit $`\lambda\Psi\mathfrak k`$ terms:

```math
-\frac{9i}2\lambda g^2L^2\bar\Psi_a\gamma^a\gamma^b\mathfrak k_b
+\frac{9i}2\lambda g^2L^2\bar\Psi_a\mathfrak k^a
+\frac{9i}2\lambda g^2L^2\bar\Psi_a\gamma^{ab}\mathfrak k_b=0
```

The coefficient of $`\bar\Psi\gamma^{ab}\mathbb I\Psi`$ also vanishes on the stated branch:

```math
i\alpha\left[1-A-\frac94\lambda g^2L^2\right]
=i\alpha[1-(4-3L)-3(L-1)]=0
```

The remaining integral before applying (F.4) is

```math
\begin{aligned}
S_F^{(2)}\simeq{}&
iA\langle\Psi_a,(\gamma^a\gamma^b\mathfrak k_b+3\mathfrak k^a)\rangle
+\frac{2iA}{L}\langle\Psi_a,\mathbb I\nabla^a\zeta\rangle
+\frac{gA}2\langle\Psi_a,\gamma^a\zeta\rangle\\
&+(2-L)\langle\Psi_a,\gamma^a\mathbb I\Lambda\rangle
-\frac{3i\lambda gL}4\langle\Psi_a,\gamma^{ab}\nabla_b\Lambda\rangle\\
&-\frac{2A}{L^2}\langle\zeta,\mathord{\not{\nabla}}\zeta\rangle
+\frac{8A}{L}\langle\zeta,\mathbb I\gamma^a\mathfrak k_a\rangle
-\frac{3igA}{L}\langle\zeta,\mathbb I\zeta\rangle
+2i\langle\zeta,\Lambda\rangle\\
&+\lambda\left[-\tfrac12\langle\Lambda,\mathord{\not{\nabla}}\Lambda\rangle
-3gL\langle\Lambda,\gamma^a\mathfrak k_a\rangle
+6ig^2L\langle\Lambda,\zeta\rangle
+\tfrac{igL}4\langle\Lambda,\mathbb I\Lambda\rangle\right].
\end{aligned}
\tag{F.5}
```

The first line of (F.4) cancels the $`\Lambda\gamma\mathfrak k`$ coefficient and changes the $`\Psi\gamma\mathbb I\Lambda`$ coefficient to

```math
2-L-\frac32\lambda g^2L^2=2-L-2(L-1)=A
```

Inserting the composite spinor in that term and using the second line of (F.4) gives

```math
\begin{aligned}
S_F^{(2)}\simeq{}&-3iA\langle\Psi_a,\gamma^{ab}\mathfrak k_b\rangle
-\frac{2A}{L^2}\langle\zeta,\mathord{\not{\nabla}}\zeta\rangle
-\frac{3igA}{L}\langle\zeta,\mathbb I\zeta\rangle
+\frac{2iA}{L}\langle\zeta,\Lambda\rangle\\
&-\frac\lambda2\left\langle\Lambda,
\left(\mathord{\not{\nabla}}-\frac{igL}2\mathbb I\right)\Lambda\right\rangle.
\end{aligned}
```

Here $`2i-6i\lambda g^2L=2iA/L`$. Substitution of (F.1) and (F.2) in the remaining $`\zeta\Lambda`$ term yields

```math
\boxed{\begin{aligned}
S_F^{(2)}\simeq{}&-A\langle\Psi_a,\mathscr R^a(\Psi)\rangle
+\frac{2A}{L^2}\langle\zeta,\mathord{\not{\nabla}}\zeta\rangle
+\frac{7igA}{L}\langle\zeta,\mathbb I\zeta\rangle\\
&+\frac{4iA}{3L}\langle\zeta,\mathbb I\gamma_a\mathscr R^a(\Psi)\rangle
-\frac\lambda2\left\langle\Lambda,
\left(\mathord{\not{\nabla}}-\frac{igL}2\mathbb I\right)\Lambda\right\rangle.
\end{aligned}}
\tag{F.6}
```

Equation (F.6) is the compact fermionic Hessian quoted in the quadratic-action summary. This reduction changes the operator representation without setting the gravitino gamma trace, $`\zeta`$, or $`\Lambda`$ to zero.

## Euler operators

Define

```math
\mathcal H=\mathord{\not{\nabla}}-\frac{igL}2\mathbb I,\quad
\mathcal V=-\frac{2i}{L}\mathord{\not{\nabla}}+5g\mathbb I,\quad
\mathcal U\Psi=\frac23\mathbb I\gamma_a\mathscr R^a(\Psi),
\quad\Lambda=\mathcal U\Psi+\mathcal V\zeta.
```

The transpose includes the open tangent indices:

```math
\mathscr R^\sharp=-\mathscr R,\quad
\mathcal H^\sharp=-\mathcal H,\quad
\mathcal V^\sharp=-\mathcal V,\quad
\mathcal U^\sharp X=\frac23\mathscr R(\gamma\mathbb I X)
```

The composite spinor is varied by its dependence on $`\Psi`$ and $`\zeta`$:

```math
\begin{aligned}
\delta\left[-\frac\lambda2\langle\Lambda,\mathcal H\Lambda\rangle\right]
&=-\lambda\langle\mathcal U\delta\Psi+\mathcal V\delta\zeta,
\mathcal H\Lambda\rangle\\
&=-\lambda\langle\delta\Psi,\mathcal U^\sharp\mathcal H\Lambda\rangle
+\lambda\langle\delta\zeta,\mathcal V\mathcal H\Lambda\rangle.
\end{aligned}
```

With $`\delta S_F^{(2)}=\langle\delta\Psi_a,\mathcal E_\Psi^a\rangle+\langle\delta\zeta,\mathcal E_\zeta\rangle`$, the source gives

```math
\boxed{\begin{aligned}
\mathcal E_\Psi^a={}&-2A\mathscr R^a(\Psi)
-\frac{4iA}{3L}\mathscr R^a(\gamma\mathbb I\zeta)
-\frac{2\lambda}3\mathscr R^a(\gamma\mathbb I\mathcal H\Lambda),\\
\mathcal E_\zeta={}&\frac{4A}{L^2}\mathord{\not{\nabla}}\zeta
+\frac{14igA}{L}\mathbb I\zeta
+\frac{4iA}{3L}\mathbb I\gamma_a\mathscr R^a(\Psi)
+\lambda\left(-\frac{2i}{L}\mathord{\not{\nabla}}+5g\mathbb I\right)
\left(\mathord{\not{\nabla}}-\frac{igL}2\mathbb I\right)\Lambda.
\end{aligned}}
\tag{F.7}
```

The input of $`\mathscr R^a(\gamma\mathbb I X)`$ is the vector-spinor $`Z_b=\gamma_b\mathbb I X`$. Thus (F.7) consists of equations for $`\Psi_a`$ and $`\zeta`$ alone.

## Correspondence with the variation of the component action

The source's second route starts from the two-derivative density (5.10) and the R² density (C.1), before taking background coefficients:

```math
\begin{aligned}
\delta[Y'^2-g\rho'Y'\cdot L-2Y'\cdot L-2N\rho']
={}&(2Y'^{ij}-g\rho'L^{ij}-2L^{ij})\delta Y'_{ij}\\
&+(-gY'\cdot L-2N)\delta\rho'
+\text{bosonic field variations},\\
\delta[-\tfrac12\bar\lambda'\mathord{\not{\mathcal D}}\lambda']
={}&-\tfrac12\delta\bar\lambda'\mathord{\not{\mathcal D}}\lambda'
-\tfrac12\bar\lambda'\gamma^a\delta(\mathcal D_a\lambda')
-\tfrac12\bar\lambda'\delta\gamma^a\mathcal D_a\lambda'
\end{aligned}
```

The variations of the composite fields and dependent connections are chain-rule variations. Their coefficients with one fermionic fluctuation are

```math
\begin{gathered}
\delta\lambda'|_0=\Lambda[\delta\Psi,\delta\zeta],\quad
\delta(\mathcal D_a\lambda')|_0=\mathfrak W_a[\delta\Psi,\delta\zeta],\\
\delta\chi|_0=\Xi[\delta\Psi,\delta\zeta],\quad
\delta\phi|_0=\Phi[\delta\Psi],\quad
\delta\rho'|_1=\frac i{L^2}\nu_{ij}
(\delta\bar\zeta^i\zeta^j+\bar\zeta^i\delta\zeta^j).
\end{gathered}
```

The trace of the full linear map gives

```math
\begin{aligned}
\nu^{ij}\delta Y'_{ij}|_1={}&8\delta f|_1
-\frac i2\delta(\bar\Psi_a\mathfrak k^a)
-8\delta(\bar\Psi_a\gamma^a\Xi)\\
&-\frac iL\nu_{ij}\{\nabla_a\delta(\bar\Psi^{ai}\zeta^j)
+\delta(\bar\Psi^{ai}\mathfrak p_a{}^j)\}
+\frac1L\nu_{ij}\delta(\bar\zeta^i\gamma^a\Phi_a{}^j)\\
&+\frac{3ig}L\nu_{ij}\delta(\bar\zeta^i\zeta^j)
+\frac1{L^2}\delta(\bar\zeta^i\gamma^a\mathfrak p_{ai}),\\
\delta f|_1={}&-\frac1{16}\delta
[R_K+i\bar\Phi_a\gamma^{ab}\Psi_b-16\bar\Psi_a\gamma^a\Xi].
\end{aligned}
\tag{F.8}
```

The conformal box contributes $`6\delta f-6\delta(\bar\Psi\gamma\Xi)`$, while $`4D`$ contributes $`2\delta f-i\delta(\bar\Psi\mathfrak k)/2-2\delta(\bar\Psi\gamma\Xi)`$. The explicit $`N\bar\varphi\varphi`$ trace is $`(1-3)iN_0\nu_{ij}\delta(\bar\zeta^i\zeta^j)/L^3=3ig\nu_{ij}\delta(\bar\zeta^i\zeta^j)/L`$. The explicit $`\bar\chi\varphi`$ traces cancel, $`-16i/L+16i/L=0`$. These are the 2016-map coefficients used in (F.8).

The vector conformal box contributes

```math
\begin{aligned}
\delta(\Box_c\rho')|_1={}&\Box\delta\rho'|_1
-\tfrac i2\nabla_a\delta(\bar\Psi^a\Lambda)
-\tfrac i2\delta(\bar\Psi_a\mathfrak W^a)
-2\rho_0\delta(\bar\Psi_a\gamma^a\Xi)\\
&+\tfrac12\delta(\bar\Phi_a\gamma^a\Lambda)
+2f_0\delta\rho'|_1+2\rho_0\delta f|_1
\end{aligned}
```

The coefficients of $`\rho_0^2\delta f`$ from this box, the explicit $`\rho'^2f`$ term, and $`-4\rho'^2D`$ are $`1,1,-2`$, respectively. The recorded coefficient table below writes every row as $`c\,\delta B`$. In this table $`f_0=f_{0a}{}^a`$ and $`\rho_0=\rho'_0`$.

| $`B`$ | Coefficient from the full variation $`c`$ |
|---|---|
| $`y_{2F}`$, the integrated bilinear in (F.8) | $`-2L+\lambda(2y_0-g\rho_0L)=-2A`$ |
| $`\rho_{2F}`$ | $`-2N_0+\lambda(-gLy_0+4f_0\rho_0)=3gLA`$ |
| $`\bar\Lambda\zeta`$ | $`-2i`$ |
| $`\nu_{ij}\bar\Psi_a^i\gamma^a\Lambda^j`$ | $`L+\lambda(3g\rho_0L/8-y_0/2)=L-15\lambda g^2L^2/8`$ |
| $`\bar\Psi_a\gamma^a\zeta`$ | $`-(\rho_0+2g)=g(3L-2)`$ |
| $`\nu_{ij}\bar\Psi_a^i\gamma^{ab}\Psi_b^j`$ | $`-iL(\rho_0+2g)/2+i\lambda\rho_0y_0/4=(igL/2)(3L-2-9\lambda g^2L^2/4)`$ |
| $`\bar\Lambda\gamma^a\mathfrak W_a`$ | $`-\lambda/2`$ |
| $`\bar\Lambda\Xi`$ | $`-16i\lambda\rho_0=48i\lambda gL`$ |
| $`\nu_{ij}\bar\Lambda^i\Lambda^j`$ | $`i\lambda gL/4`$ |
| $`\bar\Lambda\gamma^a\mathfrak k_a`$ | $`-3\lambda\rho_0/4=9\lambda gL/4`$ |
| $`\bar\Phi_a\gamma^a\Lambda`$ | $`\lambda\rho_0/4=-3\lambda gL/4`$ |
| $`\bar\Psi_a\gamma^a\Xi`$ | $`-4\lambda\rho_0^2=-36\lambda g^2L^2`$ |
| $`\bar\Psi_a\mathfrak k^a`$ | $`i\lambda\rho_0^2/2=9i\lambda g^2L^2/2`$ |
| $`\bar\Psi_a\gamma^{ab}\mathfrak W_b`$ | $`i\lambda\rho_0/4=-3i\lambda gL/4`$ |
| $`\bar\Psi_a\gamma^{ab}\Phi_b`$ | $`-i\lambda\rho_0^2/4=-9i\lambda g^2L^2/4`$ |

The last row combines the two component-action terms

```math
\frac{i\lambda\rho_0^2}4\delta(\bar\Psi_a\gamma^{ab}\mathfrak k_b)
-\frac{i\lambda g\rho_0^2L}8\delta(\nu_{ij}\bar\Psi_a^i\gamma^{ab}\Psi_b^j)
=-\frac{i\lambda\rho_0^2}4\delta(\bar\Psi_a\gamma^{ab}\Phi_b).
```

The two additional total derivatives, $`\lambda\rho_0\Box\delta\rho_{2F}/2`$ and $`-i\lambda\rho_0\nabla_a\delta(\bar\Psi^a\Lambda)/4`$, occur in the fermionic surface current. Terms with a vanishing background field $`A',T,G,E`$ multiplying at least two fermions contribute at higher fluctuation order to the first fermionic variation. The background polynomial is used only after collecting the coefficients:

```math
L-\frac{15}8\lambda g^2L^2=\frac{5-3L}2,
\qquad 3L-2-\frac94\lambda g^2L^2=1.
```

With (F.8) and the integration-by-parts identities (F.4), the component-action route gives

```math
\begin{aligned}
\mathcal E_{\psi,\mathrm{full}}^{(1)a}
&=-2A\mathscr R^a(\Psi)-\frac{4iA}{3L}\mathscr R^a(\gamma\mathbb I\zeta)
-\frac{2\lambda}3\mathscr R^a(\gamma\mathbb I\mathcal H\Lambda),\\
\mathcal E_{\varphi,\mathrm{full}}^{(1)}
&=\frac{4A}{L^2}\mathord{\not{\nabla}}\zeta+\frac{14igA}{L}\mathbb I\zeta
+\frac{4iA}{3L}\mathbb I\gamma_a\mathscr R^a(\Psi)+\lambda\mathcal V\mathcal H\Lambda
\end{aligned}
```

These are the two operators in (F.7), including the composite-spinor variation and the Grassmann factor of two. This establishes the source's stated relation between its component input and the quoted Hessian; it does not identify the distinct literal 2013-map density with this action.
