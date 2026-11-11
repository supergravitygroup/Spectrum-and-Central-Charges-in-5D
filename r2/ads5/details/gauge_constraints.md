# Gauge directions and coupled constraints

[Reading guide](../README.md). The equation labels and local symbols below follow the action conventions specified for this theory.

<a id="9-gauge-directions-coupled-constraints-and-physical-operators"></a>

## Gauge directions, coupled constraints, and physical operators

<a id="91-gauge-symmetry-and-off-shell-counting"></a>

### Gauge symmetry and off-shell counting

The gauge shifts on the background are
```math
\begin{gathered}
\delta h_{\mu\nu}=2\nabla_{(\mu}\xi_{\nu)},\quad
\delta c=d\alpha,\quad\delta v=d\beta,\\
\delta b=d\Lambda_1-\frac g2\Lambda_2,\quad\delta a=d\Lambda_2,\quad
\delta\Psi_\mu=(\nabla_\mu-m\gamma_\mu\mathbb J)\epsilon,\\
\delta s=\delta n=\delta w=\delta\zeta=0
\end{gathered}
```
The last line gives only the background shifts; homogeneous charge transformations under internal $`U(1)`$ are also present.

```math
\Gamma_2=\Lambda_2-\frac2g d\Lambda_1
\quad\Longrightarrow\quad
\delta b=-\frac g2\Gamma_2,\quad\delta a=d\Gamma_2.
```
Thus the form pair has ten independent gauge directions at $`g\neq0`$. $`\Lambda_1`$ and $`\Lambda_2`$ are not counted separately as fifteen independent directions.

```math
\begin{aligned}
N_B^{\mathrm{off}}
&=(25+5+10+1+1+10+5+10)-(10+5+1+1+10)=40,\\
N_F^{\mathrm{off}}&=(5+1)8-8=40.
\end{aligned}
```
This is not the number of propagating polarizations; the equations-of-motion constraints are also required.

<a id="92-metricscalar-decomposition"></a>

### Metric–scalar decomposition

Since
```math
\mathscr G_{\mu\nu}(\bar g X)=-\frac32\mathscr P_{\mu\nu}X
```
for $`A\neq0`$, on the solution space,
```math
h^{\mathrm E}_{\mu\nu}=h_{\mu\nu}+\frac2{3A}\bar g_{\mu\nu}X,
\qquad\mathscr G(h^{\mathrm E})=0.
```
In a physical TT representative, the spin-2 block is
```math
\left(\Box+\frac2{\ell^2}\right)h^{\mathrm{TT}}_{\mu\nu}=0,
\qquad\nabla^\mu h^{\mathrm{TT}}_{\mu\nu}=0,\quad h^{\mathrm{TT}\,\mu}{}_{\mu}=0
```
This does not set $`s,n`$ or the metric trace to zero in the original action.

The trace equation and the definition of $`X`$, through
```math
\frac{3A}{2}r_1-4\Box X-5qX=0,
\quad
r_1=\frac2\lambda[X-(1-5\lambda g^2L)s+3\lambda gn]+\frac2L\Box s
```
give the second-order system for $`(X,s,n)`$:
```math
(\mathsf K\Box+\mathsf M)\begin{pmatrix}X\\s\\n\end{pmatrix}=0,
```
```math
\mathsf K=\begin{pmatrix}
-4&3A/L&0\\-2/L&2/L+3\lambda g^2&6\lambda g/L\\0&6\lambda g/L&4\lambda/L^2
\end{pmatrix},
```
```math
\mathsf M=\begin{pmatrix}
3A/\lambda+10g^2L^2&-3A/\lambda+15Ag^2L&9Ag\\
2/\lambda-10g^2L&-2/\lambda+g^2(4+8L)+3\lambda g^4L^2&-2g+18\lambda g^3L\\
-6g&-2g+18\lambda g^3L&-4/L+20\lambda g^2
\end{pmatrix}.
```
```math
\det\mathsf K=-\frac{8A\lambda}{L^4}\neq0
```
This shows that the general branch has three propagating scalar modes. $`N`$ cannot be treated as algebraically auxiliary in the total theory.

<a id="93-internal-connection-and-coupled-formvector-system"></a>

### Internal connection and coupled form–vector system

With
```math
\Pi^{ij}=\nabla\cdot w^{ij},\quad
Aw_\mu{}^{ij}-\lambda\nabla_\mu\Pi^{ij}=0
```
we have
```math
w_\mu{}^{ij}=\frac\lambda A\nabla_\mu\Pi^{ij},\qquad
(\lambda\Box-A)\Pi^{ij}=0.
```
The two traceless internal components carry two scalars; the other components of $`w`$ are not separate vector modes.

Let $`\mathscr M z^\mu:=\nabla_\nu(2\nabla^{[\nu}z^{\mu]})`$ be the Maxwell operator. For transverse vectors,
```math
\mathscr M=\Box+\frac4{\ell^2}.
```
The coupled $`c,b,a,v`$ equations give, for $`A\neq0`$,
```math
Q=-dc-\frac1{\sqrt2gL}dv,\quad
\mathscr M c=-g\mathsf E,\quad\mathscr M v=0,
```
```math
\frac{2\lambda}{L}\mathscr M\mathsf E+(3\lambda g^2L-2)\mathsf E=0
```
Using the background relation,
```math
M_V^2=\frac L\lambda-\frac32g^2L^2
=\frac{2-L}{\lambda}=\frac B\lambda.
```
```math
c^{(0)}=c+\frac{g}{M_V^2}\mathsf E,
\quad\mathscr M c^{(0)}=0,\quad\mathscr M v=0,
\quad(\mathscr M-M_V^2)\mathsf E=0,\quad\nabla\cdot\mathsf E=0.
```
There are two Maxwell modes and one Proca mode. $`\mathsf H`$ is recovered from $`Q`$, followed by $`(a,b)`$ up to gauge equivalence; no separate independent $`E_a`$ mode is added.

<a id="94-gravitinospinor-mixing"></a>

### Gravitino–spinor mixing

```math
\Psi_\mu^{\mathrm E}=\Psi_\mu+\gamma_\mu\mathbb I
\left(\frac{2i}{3L}\zeta+\frac\lambda{3A}\mathcal H\Lambda\right)
\quad\Longrightarrow\quad\mathscr R^\mu(\Psi^{\mathrm E})=0.
```
Using the gamma contraction
```math
\gamma_\mu\mathscr R^\mu(\gamma Z)=12\mathcal K_F Z
```
gives
```math
\zeta_0=\zeta-\frac{i\lambda L}{2A}\mathcal K_F\Lambda,
\quad \mathcal H\zeta_0=0,
\quad \mathcal P_F=\mathord{\not{\nabla}}-3m\mathbb J
```
With the algebraic operator identity
```math
\mathcal K_F^2-4\mathcal K_F\mathcal H=-3\mathcal K_F\mathcal P_F
```
we have
```math
\left(1-\frac\lambda A\mathcal K_F\mathcal P_F\right)\Lambda
=-2g\mathbb I\zeta_0.
```
Since $`\mathcal K_F\mathcal P_F\zeta_0=-12m^2\zeta_0`$ and
$`A+12\lambda m^2=B`$,
```math
\zeta_1=\Lambda+\frac{2gA}{B}\mathbb I\zeta_0,
\qquad[\lambda\mathcal K_F\mathcal P_F-A]\zeta_1=0.
```
No mixing term was discarded at the outset. The inverse transformation uses
```math
\Lambda=\zeta_1-\frac{2gA}{B}\mathbb I\zeta_0,\qquad
\zeta=\zeta_0+\frac{i\lambda L}{2A}\mathcal K_F\Lambda
```
and the definition of $`\Psi^{\mathrm E}`$.

The gravitino time component $`\mathscr R^0\Psi^{\mathrm E}=0`$ supplies eight real constraints without time derivatives. Together with the eight local SUSY directions, this leaves
```math
4\cdot8-8_{\mathrm{constraint}}-8_{\mathrm{SUSY}}=16
```
real Cauchy data, or eight fermionic polarizations. The gamma-trace equation
```math
\nabla\cdot\Psi^{\mathrm E}=(\mathord{\not{\nabla}}+4m\mathbb J)\gamma\cdot\Psi^{\mathrm E}
```
and the SUSY Noether identity are not counted again as independent constraints. The physical spin-$`3/2`$ representative is defined by
```math
(\mathord{\not{\nabla}}_{3/2}-3m\mathbb J)\psi^{3/2}_\mu=0,
\quad\gamma\cdot\psi^{3/2}=\nabla\cdot\psi^{3/2}=0
```
The original $`\gamma\cdot\Psi`$ and $`\zeta`$ have not been set to zero.

