# Gauge directions, constraints, and physical field content on fluxless AdS₅

This calculation uses the quadratic action and verified linearized equations
in [quadratic_action_ads5.bg](../../ads5/details/fermionic_density.md), with the conventions of
[CONVENTIONS.md](../../../common/details/source_conventions.md). The selected background branch is the $`A_0>0`$ branch
in ads5_bgs.md.

The local propagation count of the complete coupled system is
```math
\boxed{
\lambda_{R^2}\neq0:\quad 20_{\mathrm B}+20_{\mathrm F},
\qquad
\lambda_{R^2}=0:\quad 12_{\mathrm B}+12_{\mathrm F}.
}
```
The variables below parametrize the solution space; no fields are eliminated
from the off-shell action.

<a id="1-background-and-notation"></a>

## Background and notation

Throughout the calculation, write
```math
\lambda=\lambda_{R^2},\qquad L=L_0,\qquad
A=A_0=L-3\lambda g^2L^2=4-3L>0,
```
```math
L=\frac{2}{1+\sqrt{1-3\lambda g^2}},
\qquad
q=-2g^2L^2,\qquad \bar R_{\mu\nu}=q\bar g_{\mu\nu}
```
In this region,
```math
g\neq0,\qquad \lambda g^2<\frac14,\qquad 0<L<\frac43,
\qquad 3\lambda g^2L^2-4L+4=0.
```
The independent fluctuations are denoted by
```math
\begin{gathered}
e_\mu{}^a=\bar e_\mu{}^a+u_\mu{}^a,\qquad
h_{\mu\nu}=2u_{(\mu\nu)},\qquad
L_{\rm field}=L_0+s,\qquad N=N_0+n,\\
C=c,\qquad B=b,\qquad E_3=a,\qquad V=v,\qquad V'_\mu{}^{ij}=w_\mu{}^{ij},\\
\psi_\mu{}^i=\Psi_\mu{}^i,\qquad \varphi^i=\zeta^i
\end{gathered}
```
Here $`L`$ abbreviates the constant $`L_0`$ in the coefficients below;
its independent scalar fluctuation is $`s`$.
All derivatives and index operations refer to the background geometry.

<a id="2-gauge-directions-and-off-shell-counting"></a>

## Gauge directions and off-shell counting

The background shift parts of the gauge transformations are
```math
\begin{aligned}
\delta h_{\mu\nu}&=2\nabla_{(\mu}\xi_{\nu)},\\
\delta u_{[\mu\nu]}&=\nabla_{[\mu}\xi_{\nu]}+\theta_{\mu\nu},\\
\delta c&=d\alpha,\qquad \delta v=d\beta,\\
\delta b&=d\Lambda_1-\frac g2\Lambda_2,\qquad
\delta a=d\Lambda_2,\\
\delta\Psi_\mu&=\mathscr D_\mu\epsilon,\qquad
\mathscr D_\mu=\nabla_\mu-\frac{igL}{2}\gamma_\mu\mathbb I,\\
\delta s&=\delta n=\delta w_\mu{}^{ij}=\delta\zeta=0,
\end{aligned}
```
Here
```math
\mathbb I^i{}_j=\epsilon^{ik}\nu_{kj},\qquad
\nu_{ij}=\frac{\delta_{ij}}{\sqrt2},\qquad
\mathbb I^2=-\frac12\mathbf1.
```
The last line concerns background shifts. $`w,\Psi,\zeta`$ also transforms homogeneously
under the residual internal $`U(1)`$. In alignment gauge there are no two
additional independent gauge shifts for $`w_\mu{}^{ij}`$. In particular,
```math
\boxed{\delta_\epsilon\zeta\big|_0=0}
```
so $`\zeta`$ cannot be set to zero using local SUSY.

Combining the form parameters through
```math
\Gamma_2=\Lambda_2-\frac2g\,d\Lambda_1
```
gives
```math
\delta b=-\frac g2\Gamma_2,\qquad
\delta a=d\Gamma_2,\qquad
\delta\!\left(a+\frac2g\,db\right)=0
```
For $`g\neq0`$, the form pair therefore has ten independent gauge directions;
the $`\Lambda_1,\Lambda_2`$ components are not counted as separately independent.

The component count on the current gauge slice is
```math
\begin{aligned}
N_{\mathrm B}^{\mathrm{off}}
&=(25+5+10+1+1+10+5+10)\\
&\quad -(10_{\rm Lorentz}+5_{\rm diff}+1_C+1_V+10_{\rm form})
=40,\\
N_{\mathrm F}^{\mathrm{off}}
&=(5+1)\,8-8_{\rm SUSY}=40
\end{aligned}
```
The constraints in the equations of motion must also be used to determine
the propagation count.

<a id="3-metricscalar-system"></a>

## Metric–scalar system

In the metric–scalar equations, define
```math
X=(1-5\lambda g^2L)s-3\lambda gn
+\frac{\lambda}{2}\left(r_1-\frac2L\Box s\right)
```
Here
```math
r_1=\nabla_\mu\nabla_\nu h^{\mu\nu}-\Box h-qh
```
is the linearized scalar curvature. The metric equation is
```math
-A\mathscr G_{\mu\nu}(h)+\mathscr P_{\mu\nu}X=0,
```
```math
\mathscr G_{\mu\nu}(h)
=R_{1\mu\nu}-\frac12\bar g_{\mu\nu}r_1-qh_{\mu\nu},
\qquad
\mathscr P_{\mu\nu}
=\nabla_\mu\nabla_\nu-\bar g_{\mu\nu}\Box-q\bar g_{\mu\nu}
```
$`R_{1\mu\nu}`$ is the linear variation of the Ricci tensor. For a pure-trace input,
```math
\mathscr G_{\mu\nu}(\bar g X)=-\frac32\mathscr P_{\mu\nu}X
```
and hence
```math
h^{\mathrm E}_{\mu\nu}
=h_{\mu\nu}+\frac{2}{3A}\bar g_{\mu\nu}X
\quad\Longrightarrow\quad
\boxed{\mathscr G_{\mu\nu}(h^{\mathrm E})=0}.
```
With five diffeomorphism directions and five Einstein constraints,
the spin-2 part therefore carries
```math
15-5-5=5
```
local polarizations. This equality does not require imposing TT gauge.

The trace equation and the definition of $`X`$ give
```math
\frac{3A}{2}r_1-4\Box X-5qX=0,
```
```math
r_1=\frac2\lambda\big[X-(1-5\lambda g^2L)s+3\lambda gn\big]
+\frac2L\Box s
```
For $`\lambda\neq0`$, the scalar system is therefore second order:
```math
(\mathsf K\Box+\mathsf M)
\begin{pmatrix}X\\s\\n\end{pmatrix}=0
```
```math
\mathsf K=
\begin{pmatrix}
-4&3A/L&0\\
-2/L&2/L+3\lambda g^2&6\lambda g/L\\
0&6\lambda g/L&4\lambda/L^2
\end{pmatrix},
```
```math
\mathsf M=
\begin{pmatrix}
3A/\lambda+10g^2L^2&
-3A/\lambda+15Ag^2L&9Ag\\
2/\lambda-10g^2L&
-2/\lambda+g^2(4+8L)+3\lambda g^4L^2&
-2g+18\lambda g^3L\\
-6g&-2g+18\lambda g^3L&-4/L+20\lambda g^2
\end{pmatrix}.
```
Since the kinetic determinant is
```math
\begin{aligned}
\det\mathsf K
&=-\frac{32\lambda}{L^3}
+\frac{96\lambda^2g^2}{L^2}
+\frac{24A\lambda}{L^4}\\
&=\boxed{-\frac{8A\lambda}{L^4}}\neq0
\end{aligned}
```
$`X,s,n`$ together carry **three scalar modes**.
In particular, $`N`$ is not an algebraic auxiliary field in the full theory.

For $`\lambda=0`$, take $`L=A=1`$ and use the original equations:
```math
-4n-8gs=0
\quad\Longrightarrow\quad n=-2gs,
```
```math
\frac32r_1-4\Box s+10g^2s=0,
\qquad
r_1-2\Box s+8g^2s=0.
```
Substitution gives
```math
\frac23\Box s+\frac43g^2s=0
\quad\Longrightarrow\quad
\boxed{(\Box+2g^2)s=0}
```
One propagating scalar mode remains in this limit.

<a id="4-constraints-of-the-traceless-internal-connection"></a>

## Constraints of the traceless internal connection

For the traceless internal connection, defining
```math
\Pi^{ij}:=\nabla^\mu w_\mu{}^{ij}
```
gives the equation
```math
Aw_\mu{}^{ij}-\lambda\nabla_\mu\Pi^{ij}=0
```
Therefore
```math
w_\mu{}^{ij}=\frac{\lambda}{A}\nabla_\mu\Pi^{ij},
\qquad
\boxed{(\lambda\Box-A)\Pi^{ij}=0}.
```
The symmetric traceless pair $`ij`$ carries two real components.
For $`\lambda\neq0`$, $`w`$ has two longitudinal scalar modes; the remaining vector
components are not independent initial data. For $`\lambda=0`$,
```math
\boxed{w_\mu{}^{ij}=0}
```
is an algebraic constraint.

<a id="5-coupled-formvector-system-for-gneq0"></a>

## Coupled form–vector system for $`g\neq0`$

In the form sector, use
```math
\mathsf G=dc,\qquad
\mathsf H=db+\frac g2a,\qquad
Q=*\,\mathsf H,\qquad
Q_{\mu\nu}=\frac16\varepsilon_{\mu\nu\rho\sigma\lambda}
\mathsf H^{\rho\sigma\lambda},
```
```math
\mathsf E^\mu
=-\frac1{12}\varepsilon^{\mu\nu\rho\sigma\lambda}
\nabla_\nu a_{\rho\sigma\lambda}
```
The definitions directly imply
```math
\begin{aligned}
\nabla_\nu Q^{\mu\nu}
&=\frac16\varepsilon^{\mu\nu\rho\sigma\lambda}
\nabla_\nu\mathsf H_{\rho\sigma\lambda}\\
&=\frac g{12}\varepsilon^{\mu\nu\rho\sigma\lambda}
\nabla_\nu a_{\rho\sigma\lambda}
=-g\mathsf E^\mu
\end{aligned}
```
Thus
```math
\boxed{\nabla_\nu Q^{\nu\mu}=g\mathsf E^\mu,\qquad
\nabla_\mu\mathsf E^\mu=0}.
```
The second equality is a Bianchi identity and is not counted as an additional
independent field equation.

Let the Maxwell operator be
```math
(\mathscr M z)^\mu
:=\nabla_\nu(2\nabla^{[\nu}z^{\mu]})
```
The $`v`$ equation of the quadratic action is
```math
J_{\mathcal A}^{\mu}=2\mathsf E^\mu,
\qquad
J_{\mathcal A}^{\mu}
=\lambda\nabla_\nu\!
\left[\mathsf F^{\nu\mu}
+3gL(\mathsf G^{\nu\mu}+2Q^{\nu\mu})\right]
```
Substituting it into the three-form equation gives
```math
2AQ-3\lambda gL\mathsf F
-\frac92\lambda g^2L^2\mathsf G+\frac1g\,dW=0,
```
```math
W=\sqrt2v+2gc+6\lambda g^2\mathsf E,
\qquad
\mathsf F=\sqrt2\,dv+\frac2L\,d\mathsf E
```
The $`d\mathsf E`$ coefficients cancel:
```math
\begin{aligned}
0={}&2AQ
+\sqrt2(1/g-3\lambda gL)\,dv
+(2-\tfrac92\lambda g^2L^2)\,dc\\
={}&2A\left(Q+dc+\frac1{\sqrt2gL}dv\right).
\end{aligned}
```
The coupled form constraint is therefore
```math
\boxed{Q=-dc-\frac1{\sqrt2gL}dv}
```

Combining the $`c`$ and $`v`$ equations also gives
```math
2A\big(\mathscr M c+g\mathsf E\big)=0
```
Taking its divergence together with that of the $`Q`$ constraint yields
```math
\boxed{\mathscr M c=-g\mathsf E,\qquad \mathscr M v=0}
```
Finally, back-substitution into the $`v`$ equation gives
```math
\boxed{
\frac{2\lambda}{L}\mathscr M\mathsf E
+(3\lambda g^2L-2)\mathsf E=0
}
```

For $`\lambda\neq0`$, defining
```math
m_E^2=\frac L\lambda-\frac32g^2L^2
=\frac{L+A}{2\lambda}\neq0,
\qquad
c^{(0)}=c+\frac g{m_E^2}\mathsf E
```
gives
```math
\boxed{
\mathscr M c^{(0)}=0,\qquad
\mathscr M v=0,\qquad
(\mathscr M-m_E^2)\mathsf E=0,\qquad
\nabla\cdot\mathsf E=0.
}
```
These are two Maxwell fields and one Proca field:
```math
(5-1_{\rm gauge}-1_{\rm Gauss})
+(5-1_{\rm gauge}-1_{\rm Gauss})
+(5-1_{\rm Proca})
=\boxed{10}.
```
The divergence condition of $`\mathsf E`$ is counted only once here.

The inverse of this parametrization is explicit:
```math
c=c^{(0)}-\frac g{m_E^2}\mathsf E,\qquad
Q=-dc-\frac1{\sqrt2gL}dv,\qquad Q=*\,\mathsf H.
```
The $`\mathsf H=db+ga/2`$ potentials are recovered up to form-gauge equivalence.
No additional independent $`E_a`$ mode or second independent form count
is therefore introduced.

For $`\lambda=0`$, the same undivided equation gives
```math
\mathsf E=0,\qquad \mathscr M c=0,\qquad \mathscr M v=0
```
Six modes remain in the form–vector sector. This shows that the linear
appearance of $`v_\mu`$ in the action is insufficient to classify the entire
$`V_\mu`$ field as auxiliary; the coupled form equations carry its Maxwell data.

<a id="6-coupled-fermionic-system-and-constraints"></a>

## Coupled fermionic system and constraints

Let the explicit fermion operators be
```math
\begin{aligned}
\mathscr R^a(\Psi)
&=\gamma^{abc}\nabla_b\Psi_c
+\frac{3igL}{2}\gamma^{ab}\mathbb I\Psi_b,\\
\mathcal H&=\mathord{\not{\nabla}}-\frac{igL}{2}\mathbb I,\\
\mathcal K_F&=\mathord{\not{\nabla}}+\frac{5igL}{2}\mathbb I,\qquad
\mathcal P_F=\mathord{\not{\nabla}}-\frac{3igL}{2}\mathbb I
\end{aligned}
```
Since the composite spinor is
```math
\Lambda=\frac23\mathbb I\gamma_a\mathscr R^a(\Psi)
-\frac{2i}{L}\mathcal K_F\zeta
```
no independent gaugino is introduced.

The gravitino equation is
```math
\mathscr R^a\!\left[
\Psi+\gamma\mathbb I
\left(\frac{2i}{3L}\zeta+\frac{\lambda}{3A}\mathcal H\Lambda\right)
\right]=0
```
On the solution space, define
```math
\Psi_a^{\mathrm E}
:=\Psi_a+\gamma_a\mathbb I
\left(\frac{2i}{3L}\zeta+\frac{\lambda}{3A}\mathcal H\Lambda\right)
```
Then
```math
\boxed{\mathscr R^a(\Psi^{\mathrm E})=0,\qquad
\delta\Psi_a^{\mathrm E}=\mathscr D_a\epsilon}.
```

Gamma contraction gives
```math
\gamma_a\mathscr R^a(\gamma Z)
=12\left(\mathord{\not{\nabla}}+\frac{5igL}{2}\mathbb I\right)Z
=12\mathcal K_F Z
```
Using this in the composite definition and the $`\zeta`$ equation gives
```math
\left(1-\frac{4\lambda}{3A}\mathcal K_F\mathcal H\right)\Lambda
=\frac{2i}{3L}\mathcal K_F\zeta,
```
```math
\mathcal H\left(
\zeta-\frac{i\lambda L}{2A}\mathcal K_F\Lambda
\right)=0
```

Now define
```math
\zeta_0
:=\zeta-\frac{i\lambda L}{2A}\mathcal K_F\Lambda
```
Substitution into the first equation, together with the identity
```math
\mathcal K_F^2-4\mathcal K_F\mathcal H
=-3\mathcal K_F\mathcal P_F
```
gives
```math
\left(1-\frac{\lambda}{A}\mathcal K_F\mathcal P_F\right)\Lambda
=\frac{2i}{3L}\mathcal K_F\zeta_0
=-2g\mathbb I\zeta_0
```
where the last equality uses $`\mathcal H\zeta_0=0`$. Also,
```math
\mathcal K_F\mathcal P_F\zeta_0
=-\frac32g^2L^2\zeta_0,\qquad
A+\frac32\lambda g^2L^2=2-L>0.
```
Therefore, with
```math
\zeta_1:=\Lambda+\frac{2gA}{2-L}\mathbb I\zeta_0
```
the fermionic solution system becomes
```math
\boxed{
\begin{aligned}
\mathscr R^a(\Psi^{\mathrm E})&=0,\\
\left(\mathord{\not{\nabla}}-\frac{igL}{2}\mathbb I\right)\zeta_0&=0,\\
\left[
\lambda\left(\mathord{\not{\nabla}}+\frac{5igL}{2}\mathbb I\right)
\left(\mathord{\not{\nabla}}-\frac{3igL}{2}\mathbb I\right)-A
\right]\zeta_1&=0
\end{aligned}}
```
These are not new off-shell fields. The inverse uses
```math
\Lambda=\zeta_1-\frac{2gA}{2-L}\mathbb I\zeta_0,\qquad
\zeta=\zeta_0+\frac{i\lambda L}{2A}\mathcal K_F\Lambda
```
and the definition of $`\Psi^{\mathrm E}`$.

The fermionic constraint count is explicit in this system. The gravitino
equation
```math
\mathscr R^0(\Psi^{\mathrm E})
=\gamma^{0ij}\nabla_i\Psi_j^{\mathrm E}
+\frac{3igL}{2}\gamma^{0i}\mathbb I\Psi_i^{\mathrm E}=0
```
contains no time-evolution derivative and constitutes **eight real fermionic
constraints**. Only in this equality, $`i,j=1,\ldots,4`$ are spatial tangent indices;
the spinor $`SU(2)`$ indices are implicit. Subtracting the eight real local
SUSY directions leaves
```math
4\times8-8_{\rm constraint}-8_{\rm SUSY}=16
```
real gravitino Cauchy data, or eight propagating polarizations.

The gamma-trace relation
```math
\nabla_a\Psi_{\mathrm E}^a
=\left(\mathord{\not{\nabla}}+2igL\mathbb I\right)
\gamma_a\Psi_{\mathrm E}^a
```
and the identity
```math
\mathscr D^\sharp_a\mathscr R^a\equiv0
```
are not counted again as independent constraints.
Here $`\sharp`$ is the transpose, including integration by parts, with respect
to the fixed symplectic–Majorana bilinear:
```math
\mathscr D^\sharp_a=-\nabla_a+\frac{igL}{2}\mathbb I\gamma_a.
```
Neither the original $`\gamma\cdot\Psi`$ nor $`\zeta`$ is set to zero.

$`\zeta_0`$ carries eight real first-order Cauchy data, while $`\zeta_1`$ carries
sixteen real second-order Cauchy data for $`\lambda\neq0`$. Thus
```math
N_{\mathrm F}=\frac{16+8+16}{2}=\boxed{20}.
```
When $`\lambda=0`$, the last equation becomes the algebraic constraint
```math
-A\zeta_1=0
```
so
```math
N_{\mathrm F}=\frac{16+8}{2}=\boxed{12}.
```

<a id="7-total-physical-content-and-special-parameters"></a>

## Total physical content and special parameters

Counting all sectors together gives:

| Local propagating sector | $`\lambda_{R^2}\neq0`$ | $`\lambda_{R^2}=0`$ |
|---|---:|---:|
| Massless graviton | 5 | 5 |
| Two Maxwell modes | 6 | 6 |
| Additional Proca mode | 4 | 0 |
| Coupled metric–$`L`$–$`N`$ scalars | 3 | 1 |
| Longitudinal scalars of $`V_\mu^{\prime ij}`$ | 2 | 0 |
| **Total bosonic** | **20** | **12** |
| Massless gravitino | 8 | 8 |
| First-order spin-$`\tfrac12`$ sector | 4 | 4 |
| Two additional spin-$`\tfrac12`$ modes | 8 | 0 |
| **Total fermionic** | **20** | **12** |

At the branch intersection,
```math
\lambda_{R^2}g^2=\frac{19}{121},\qquad L_0=\frac{22}{19},
```
the determinant of the derivative-free scalar matrix,
```math
\det\mathsf M
=\frac{4g^4(L_0-2)(3L_0-4)(19L_0-22)}{L_0-1}
```
vanishes, but
```math
\det\mathsf K=-\frac{8A_0\lambda_{R^2}}{L_0^4}\neq0.
```
This intersection therefore produces neither a new gauge direction nor
a reduction in the propagation count. The endpoint $`A_0=0`$ lies outside
the selected open region; the $`1/A_0`$ transformations used here cannot
be extended to that point.

These counts describe local propagating data modulo gauge equivalence.
At the global AdS boundary, only gauge directions preserving the selected
boundary conditions and carrying zero surface charge are removed;
asymptotic symmetries are not counted as additional gauge losses.
