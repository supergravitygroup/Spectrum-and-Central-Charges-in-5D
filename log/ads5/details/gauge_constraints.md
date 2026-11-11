# Gauge directions and constraints

[Reading guide](../README.md). The equation labels and local symbols below follow the action conventions specified for this theory.

<a id="9-gauge-directions-constraints-and-dynamical-fields"></a>

## Gauge directions, constraints, and dynamical fields

On the selected AdS$`_5`$ branch the local propagating counts are

```math
\boxed{
\begin{array}{c|c|c}
&\text{Bosonic}&\text{Fermionic}\\ \hline
\alpha g^2<2,\quad \alpha g^2\neq0&44&44\\
\alpha g^2=2&32&32
\end{array}}
```

The second case has additional quadratic gauge symmetries. These are local counts before any global boundary exclusion.

The off-shell action is unchanged; equations are used only to identify its physical linear quotient and constraints.

Use the branch relations

```math
L:=L_0=\frac{2}{1+\sqrt{1-\alpha g^2/2}},\qquad
N_0=-\frac32gL^2,\qquad
k=-\frac12g^2L^2
```

together with

```math
\mathcal B:=\alpha g^2L^2-8L+8=0
\tag{G-1}
```

so that

```math
0<L\leq2,\qquad L\neq1,\qquad
\alpha g^2=\frac{8(L-1)}{L^2}.
\tag{G-2}
```

The condition $`L\ne1`$ follows from $`\alpha\ne0`$; $`l=\delta L`$ and $`n=\delta N`$ remain independent.

The inhomogeneous linear gauge directions are listed below. Flat-potential Lie derivatives in the diffeomorphism row are combined with existing form/internal transformations.

| Symmetry | Linear gauge direction | Independent local parameters |
|---|---|---:|
| Diffeomorphism | $`\delta h_{\mu\nu}=2\bar\nabla_{(\mu}\xi_{\nu)}`$ | $`5`$ |
| Local Lorentz | Antisymmetric vielbein shift by $`\delta a_{ab}=\lambda_{ab}`$  | $`10`$ |
| Internal $`U(1)`$ | $`\delta v=d\beta`$ | $`1`$ |
| Vector gauge | $`\delta c=d\Lambda`$ | $`1`$ |
| Coupled form gauge | $`\delta b_2=d\Lambda_1-\frac g2\Lambda_2,\quad\delta e_3=d\Lambda_2`$ | $`10`$ |
| Local SUSY | $`\delta\Psi_a=\mathscr D_a\epsilon,\quad\delta\zeta=0`$ | $`8`$ real fermionic |

The SUSY operator and internal matrix are

```math
\mathscr D_a=\bar\nabla_a+\frac{ig}{2}M\gamma_a,\qquad
(Mu)^i=L_0^{ij}u_j,\qquad M^2=-\frac{L^2}{2}
\tag{G-3}
```

The equality $`\delta\zeta=0`$ follows from

```math
\frac{N_0}{2}+\frac{3gL^2}{4}=0
```

and does not remove the fluctuation $`\zeta`$.

The two traceless fields $`w_\mu^{ij}`$ have no independent inhomogeneous gauge directions under residual $`U(1)`$. With fixed compensator orientation they cannot be counted as three free $`SU(2)`$ gauge connections.

The form parameters have reducibility

```math
(\Lambda_1,\Lambda_2)
=\left(\kappa_1,\frac2g\,d\kappa_1\right)
\quad\Longrightarrow\quad
\delta b_2=\delta e_3=0.
\tag{G-4}
```

Thus there are $`5+10-5=10`$ independent form gauge directions; the two-form and three-form gauge counts cannot be separated.

The invariant three-form is

```math
\mathcal H=db_2+\frac12\bar C\wedge dc+\frac g2e_3
\tag{G-5}
```

and obeys

```math
p^\mu=-\frac1{6g}\bar\varepsilon^{\mu\nu\rho\sigma\lambda}
\bar\nabla_\nu\mathcal H_{\rho\sigma\lambda},\qquad
\bar\nabla_\mu p^\mu=0
\tag{G-6}
```

The last relation is a defining Bianchi identity, not an extra field equation or physical constraint.

For $`g\ne0`$, the ten components of $`\mathcal H_3`$ locally coordinatize the form quotient. This does not discard either potential beforehand.

The gauge identities are

```math
\begin{gathered}
\bar\nabla^\mu\mathcal E_{h,\mu\nu}=0,\qquad
\mathcal E_{e,[ab]}=0,\\
\bar\nabla_\mu\mathcal E_c^\mu=0,\qquad
\bar\nabla_\mu\mathcal E_v^\mu=0,\\
\bar\nabla_\mu\mathcal E_b^{\mu\nu}=0,\qquad
\bar\nabla_\rho\mathcal E_{e_3}^{\rho\mu\nu}
+\frac g2\mathcal E_b^{\mu\nu}=0,\\
\mathscr D^{a\sharp}\mathcal E_{\Psi a}=0
\end{gathered}
\tag{G-7}
```

In particular,

```math
\mathcal E_b^{\mu\nu}
=-\frac2g\bar\nabla_\rho\mathcal E_{e_3}^{\rho\mu\nu}
\tag{G-8}
```

so the two-form equations do not provide an additional constraint system independent of the three-form equations.

There are 27 bosonic gauge functions on the generic branch. This is not the number of Hamiltonian first-class constraints.

For the coupled metric–scalar sector define

```math
\begin{gathered}
B_0=L-\frac{\alpha g^2L^2}{2},\qquad
Z=\frac1L-\frac{\alpha g^2}{4},\\
A=1-\frac{\alpha g^2L}{6},\qquad b=\frac{\alpha g}{6},\\
C=4g^2-12g^2L+\frac{13\alpha g^4L^2}{6},\\
D=-8g+\frac{4\alpha g^3L}{3},\qquad
F=\frac4L+\frac{\alpha g^2}{3}
\end{gathered}
\tag{G-9}
```

The scalar $`r=\delta R`$ is diffeomorphism invariant on the constant-curvature background.

The metric trace and two scalar equations give

```math
\begin{pmatrix}
\frac{\alpha}{12}\bar\Box+\frac32B_0-\frac{\alpha k}{3}
&-4A(\bar\Box+5k)&-4b(\bar\Box+5k)\\
A&-2Z\bar\Box+C&D\\
b&D&-F
\end{pmatrix}
\begin{pmatrix}r\\l\\n\end{pmatrix}=0
\tag{G-10}
```

as a coupled system.

The first row's curvature coefficient follows directly from

```math
\mathop{\mathrm{tr}}\nolimits\!\left[
\mathscr R^\dagger
\left(-\frac\alpha3\mathscr R+\frac\alpha{12}\bar g\,r\right)
\right]
=\frac\alpha{12}(\bar\Box-4k)r
```

and

```math
\mathop{\mathrm{tr}}\nolimits(r^\dagger f)=-4(\bar\Box+5k)f
```

with the displayed substitutions.

Let $`x`$ denote the algebraic placeholder for $`\bar\Box`$. The leading determinant coefficient is

```math
[x^2]\det K_B(x)
=\frac{2\alpha}{3}Z^2
=\frac{\alpha(L\alpha g^2-4)^2}{24L^2}
\tag{G-11}
```

The complete determinant factorizes, using the branch relation, as

```math
\det K_B(x)=
\frac{4(L-2)^2}{3L^6g^2}
(x+2L^2g^2)
\left[4(L-1)x+3L^2g^2(3L-4)\right]
\tag{G-12}
```

with no free-parameter sampling.

For $`L\ne2`$ there are two scalar channels. The role of $`N`$ follows from the coupled equation:

```math
F\neq0:\qquad n=\frac{br+Dl}{F}.
\tag{G-13}
```

This is an algebraic on-equation determination; $`n`$ carries no third independent scalar initial datum.

At the exceptional coefficient locus

```math
F=0,\quad\mathcal B=0
\quad\Longrightarrow\quad
L=\frac25,\qquad \alpha g^2=-30
\tag{G-14}
```

the equation instead reads

```math
br+Dl=0
```

as a constraint. The determinant remains nonzero as a polynomial there, so a vanishing $`n^2`$ coefficient does not remove a scalar channel.

In the spin-two block use

```math
\mathscr R_{\mu\nu}^{TT}
=-\frac12(\bar\Box-2k)h_{\mu\nu}^{TT}
```

to obtain

```math
\mathcal E_{h,\mu\nu}^{TT}
=-\frac\alpha{12}
(\bar\Box-2k)
\left(\bar\Box-2k-\frac{6B_0}{\alpha}\right)
h_{\mu\nu}^{TT}=0
\tag{G-15}
```

The generic polarization count is

```math
5+9=14
```

from one massless and one massive spin-two channel.

At $`B_0=0`$, equivalently $`\alpha g^2=3/2`$, the factors merge without reducing differential order or gauge rank. Repeated roots do not justify discarding modes.

For the two traceless internal vectors,

```math
-\frac{2\alpha}{3}\bar D_\mu
(2\bar D^{[\mu}w^{\nu]ij})
+(4L-\alpha g^2L^2)w^{\nu ij}=0.
\tag{G-16}
```

Taking a divergence and using the branch relation gives

```math
4(2-L)\bar D_\mu w^{\mu ij}=0.
\tag{G-17}
```

For $`L\ne2`$ these are two Proca constraints: each vector has four polarizations, for eight total. Since $`\alpha\ne0`$, these connections are not auxiliary.

The highest-derivative vector–form mixing completes into

```math
-\frac\alpha6j^2+\frac{\alpha g}{3}p\cdot j
+\left(-\frac2L+\frac{\alpha g^2}{3}\right)p^2
=
-\frac\alpha6(j-gp)^2-2Zp^2
\tag{G-18}
```

Discarding $`p\cdot j`$ would therefore change the kinetic rank.

For $`Z\ne0`$, the three-form has both $`d\mathcal H`$ and

```math
q_{ab}=\bar\nabla^c\mathcal H_{cab}
```

kinetic terms. Its ten quotient components split into four plus six local channels. The coefficient of $`\mathcal H^2`$ is

```math
-\frac L3+\frac{\alpha g^2L^2}{18}
=\frac{L-4}{9}
\tag{G-19}
```

and never vanishes on the selected $`0<L\le2`$ domain.

The generic vector–form count is

```math
\underbrace{(3+4)}_{c\text{, fourth order}}
+\underbrace{3}_{v}
+\underbrace{(4+6)}_{\mathcal H}
=20
\tag{G-20}
```

The temporal $`c,v`$ equations impose their Gauss constraints. The identity $`\bar\nabla\cdot p=0`$ is not counted again.

The total bosonic count is

```math
\boxed{14+2+8+20=44}
\tag{G-21}
```

as displayed.

For fermionic counting, expand the full mixed operator. Temporarily define

```math
\mathsf D:=\not{\bar\nabla},\qquad t:=igM,\qquad
t^2=\frac12g^2L^2=-k
\tag{G-22}
```

as a symbolic differential operator.

The algebra used is

```math
\mathsf D^2\chi=(\bar\Box-5k)\chi,\qquad
\mathsf D^2\Psi_a^{TT}=(\bar\Box-6k)\Psi_a^{TT},
\tag{G-23}
```

```math
\gamma_a^\sharp=\gamma_a,\qquad
\mathsf D^\sharp=-\mathsf D,\qquad M^\sharp=-M,\qquad i^\sharp=i
```

together with variation of both bilinear endpoints:

```math
\delta\!\int\bar e\,c\,\overline{T_A\Xi}\Gamma T_B\Xi
\simeq_\partial
\int\bar e\,\overline{\delta\Xi}\,
c\left(T_A^\sharp\Gamma T_B-T_B^\sharp\Gamma^\sharp T_A\right)\Xi.
\tag{G-24}
```

The spin-three-halves operator is

```math
\begin{aligned}
P_{3/2}(\mathsf D)={}&
-2L\mathsf D-(L+2)t\\
&+\alpha\left(
\frac13\mathsf D^3+\frac16t\mathsf D^2
+\frac18g^2L^2\mathsf D+\frac5{16}g^2L^2t
\right)
\end{aligned}
\tag{G-25}
```

Its factorization residual is

```math
\begin{aligned}
P_{3/2}(\mathsf D)
={}&
\left(\mathsf D+\frac32t\right)
\left[
\frac\alpha3(\mathsf D^2-t\mathsf D)
-2L+\frac38\alpha g^2L^2
\right]
-\frac t4\mathcal B
\end{aligned}
```

and hence vanishes on the selected branch:

```math
\boxed{
P_{3/2}(\mathsf D)=
\left(\mathsf D+\frac32igM\right)
\left[
\frac\alpha3(\mathsf D^2-igM\mathsf D)+L-3
\right].}
\tag{G-26}
```

Retain the spin-half block. After separating the local SUSY direction, represent it by

```math
\Psi_a=\gamma_a u,\qquad \zeta=\zeta
\tag{G-27}
```

This isolates a representation sector; it does not impose a gamma-traceless condition on the full gravitino.

The dependent connections on this representative are

```math
\begin{aligned}
\Phi_a[\gamma u]&=i\bar\nabla_a u,&
Q_{ab}[\gamma u]&=0,\\
s_a[\gamma u]&=-i\bar\nabla_a u-\frac g2M\gamma_a u,\\
\upsilon_a[\gamma u,\zeta]
&=\bar\nabla_a\zeta-3iM\bar\nabla_a u
+\frac34gL^2\gamma_a u
\end{aligned}
\tag{G-28}
```

Substitute them into every quadratic bilinear and apply the graded variation:

```math
\mathcal E_\Psi^{\,a}
=\left[\bar\nabla^a-\gamma^a(\mathsf D-2t)\right]\mathcal T,
\qquad
\mathcal T=A_Fu+B_F\zeta,
\tag{G-29}
```

```math
\mathcal E_\zeta=C_Fu+H_F\zeta
\tag{G-30}
```

The coefficients are

```math
\begin{aligned}
A_F={}&6L+\alpha\left(
\frac13\mathsf D^2-t\mathsf D-\frac{31}{24}g^2L^2\right),\\
B_F={}&-\frac{4t}{gL}
+\alpha g\left(\frac13\mathsf D+\frac56t\right),\\
C_F={}&10g(L+1)-\frac{16t}{gL}\mathsf D
+\alpha g\left(\frac43\mathsf D^2-\frac{35}{12}g^2L^2\right),\\
H_F={}&
\left(\frac4L+\frac{\alpha g^2}{3}\right)\mathsf D
+t\left(-\frac{14}{L}+\frac{17\alpha g^2}{6}\right).
\end{aligned}
\tag{G-31}
```

The gamma-trace and divergence equations are not independent spinor constraints:

```math
\gamma_a\mathcal E_\Psi^{\,a}
=-4\left(\mathsf D-\frac52t\right)\mathcal T,
\qquad
\bar\nabla_a\mathcal E_\Psi^{\,a}
=-\frac t2\gamma_a\mathcal E_\Psi^{\,a}.
\tag{G-32}
```

The second equality is the local SUSY Noether identity.

A nonzero $`\mathcal T`$ satisfying the gravitino equation must obey

```math
\bar\nabla_a\mathcal T=\frac t2\gamma_a\mathcal T
\tag{G-33}
```

This finite-dimensional Killing-spinor kernel is not a local propagating fluctuation. The propagating spin-half system is

```math
\boxed{
\begin{pmatrix}A_F&B_F\\ C_F&H_F\end{pmatrix}
\begin{pmatrix}u\\\zeta\end{pmatrix}=0}
\tag{G-34}
```

with both mixed rows retained.

The highest Dirac-derivative determinant coefficient is

```math
[\mathsf D^3](A_FH_F-B_FC_F)
=
\frac{4\alpha}{3}
\left(\frac1L-\frac{\alpha g^2}{4}\right)
=\frac{4\alpha}{3}Z
\tag{G-35}
```

The three generic spin-half channels therefore carry $`3\times4=12`$ polarizations. At $`\alpha g^2=-30`$, a vanishing diagonal coefficient in $`H_F`$ does not make this determinant vanish and does not make $`\zeta`$ auxiliary.

For the Gauss constraints, extract highest time-derivative coefficients using symbolic time-normal variable $`z`$:

```math
K_{\rm time}=
\begin{pmatrix}
-\frac\alpha3\gamma^0z^3\delta_{ij}
&\frac{\alpha g}{3}\gamma^iz^2\\
-\frac{\alpha g}{3}\gamma^jz^2
&\left(\frac4L+\frac{\alpha g^2}{3}\right)\gamma^0z
\end{pmatrix},
\qquad i,j=1,\ldots,4.
\tag{G-36}
```

This extracts principal coefficients; it is not an ansatz setting spatial fluctuations to zero.

The gravitino-block Schur complement is

```math
K_{\zeta\zeta}
-K_{\zeta\Psi}K_{\Psi\Psi}^{-1}K_{\Psi\zeta}
=4Z\gamma^0z
\tag{G-37}
```

The equation $`\mathcal E_{\Psi0}=0`$ supplies eight real fermionic Gauss constraints, preserved by the eight-component Noether identity. Eight real local SUSY functions remove gauge initial data. Thus

```math
\frac{
\underbrace{4\cdot8\cdot3}_{\Psi_i}
+\underbrace{8}_{\zeta}
-\underbrace{8}_{\text{Gauss}}
-\underbrace{8}_{\text{gauge}}
}{2}=44.
\tag{G-38}
```

The polarization decomposition gives the same result:

```math
\underbrace{8+12+12}_{\text{spin-}\frac32}
+\underbrace{4+4+4}_{\text{spin-}\frac12}
=44.
\tag{G-39}
```

Solve the rank-change condition:

```math
Z=0,\quad\mathcal B=0
\quad\Longrightarrow\quad
\boxed{L=2,\qquad \alpha g^2=2,\qquad k=-2g^2.}
\tag{G-40}
```

At that point the scalar equations become

```math
\mathcal E_l=g\mathcal E_n,\qquad
\bar g^{\mu\nu}\mathcal E_{h,\mu\nu}
=\frac{\bar\Box+5k}{2g}\mathcal E_n,
\qquad
\mathcal E_n=\frac{r-8g(n+gl)}{3g}
\tag{G-41}
```

and there are two additional scalar gauge directions

```math
\begin{aligned}
&\delta l=\chi,\qquad \delta n=-g\chi,\qquad\delta h_{\mu\nu}=0,\\
&\delta h_{\mu\nu}=2\omega\bar g_{\mu\nu},\qquad
\delta l=0,\qquad
\delta n=-\frac{\bar\Box+5k}{g}\omega
\end{aligned}
\tag{G-42}
```

The second direction is verified by the action variation

```math
2\omega\,\mathop{\mathrm{tr}}\nolimits\mathcal E_h
-\frac1g(\bar\Box+5k)\omega\,\mathcal E_n
\simeq_\partial0
```

shown here.

The combination $`n+gl=r/(8g)`$ is determined algebraically and the remaining scalar direction is gauge. No independent propagating scalar remains.

In the spin-two block,

```math
\frac{6B_0}{\alpha}=3k
```

the second channel is partially massless, with count

```math
5+(9-1)=13
\tag{G-43}
```

The internal-vector divergence equations become identities, and

```math
\delta w_\mu^{ij}=\bar D_\mu\beta^{\prime ij}
```

are two additional quadratic gauge symmetries. The two vectors now carry six rather than eight polarizations.

The extra vector–form direction is

```math
\delta c_\mu=2\xi_\mu,\qquad
\delta\mathcal H^{abc}
=\bar\varepsilon^{deabc}(d\xi)_{de},\qquad
\delta v_\mu=0
\tag{G-44}
```

Its exact part $`\xi=d\sigma`$ overlaps the existing $`c`$ gauge direction, so it adds four independent directions.

The invariant three-form becomes

```math
\mathcal H'^{abc}
:=\mathcal H^{abc}
-\frac12\bar\varepsilon^{deabc}\mathcal G_{de}
\tag{G-45}
```

and the vector–form density reduces, modulo divergences, to

```math
\begin{aligned}
\ell_{c,v,\mathcal H}^{(2)}
={}&-\frac29\mathcal H'^2
-\frac13p'^2-\frac1{3g^2}q'^2
+\frac1{6g^2}f_v^{\,2}\\
&+\frac{\sqrt2}{18g}
f_v^{ab}\bar\varepsilon_{abcde}\mathcal H'^{cde},
\end{aligned}
\tag{G-46}
```

```math
p'^\mu=-\frac1{6g}\bar\varepsilon^{\mu\nu\rho\sigma\lambda}
\bar\nabla_\nu\mathcal H'_{\rho\sigma\lambda},\qquad
q'_{ab}=\bar\nabla^c\mathcal H'_{cab},\qquad f_v=dv
```

The field $`c`$ occurs only through that invariant combination. Both three-form kinetic terms remain nonzero. The count is

```math
10+3=13
\tag{G-47}
```

as displayed.

The additional fermionic gauge direction is

```math
\boxed{
\delta_\theta\Psi_a=\gamma_a\theta,\qquad
\delta_\theta\zeta
=-\frac1g\mathsf D\theta+\frac{5i}{2}M\theta.}
\tag{G-48}
```

Both components of the full quadratic Euler operator annihilate it. The extra Noether identity is

```math
\gamma_a\mathcal E_\Psi^a
+\frac1g\left(\mathsf D-\frac52igM\right)\mathcal E_\zeta=0
\tag{G-49}
```

The number of fermionic gauge functions increases from eight to sixteen.

At this point the spin-half coefficient equations reduce to

```math
\begin{gathered}
B_F=\frac2{3g}\left(\mathsf D-\frac t2\right),\qquad
A_F=\frac{B_F}{g}\left(\mathsf D-\frac52t\right),\\
C_F=4gA_F,\qquad H_F=4gB_F.
\end{gathered}
```

Define the invariant combination

```math
\eta:=\zeta+\frac1g\left(\mathsf D-\frac52t\right)u,
\qquad \delta_\theta\eta=0
```

which obeys

```math
\mathcal T=\frac2{3g}\left(\mathsf D-\frac t2\right)\eta,
\qquad
\mathcal E_\zeta=4g\mathcal T.
\tag{G-50}
```

Only one Dirac channel, with four polarizations, remains from the three generic spin-half channels.

The spin-three-halves operator is

```math
P_{3/2}(\mathsf D)
=\frac2{3g^2}
\left(\mathsf D+\frac32igM\right)
\left(\mathsf D-\frac32igM\right)
\left(\mathsf D+\frac12igM\right)
\tag{G-51}
```

Its two massless and one massive channels carry

```math
8+8+12=28
```

The extra massless direction combines existing SUSY with the new quadratic symmetry; no additional independent gravitino field is introduced.

The endpoint total is therefore

```math
\boxed{
N_B=13+0+6+13=32,\qquad
N_F=28+4=32.}
\tag{G-52}
```

The independent fields have the following status in the complete coupled linear system:

| Field or sector | Generic branch | $`\alpha g^2=2`$ |
|---|---|---|
| Antisymmetric vielbein | Local Lorentz gauge direction | Unchanged |
| Metric spin two | $`14`$ polarizations | $`13`$ polarizations |
| $`(r,l,n)`$ | Two scalar channels; $`n`$ is not a third channel | No propagating scalar; two extra gauge identities |
| Traceless internal connection $`w^{ij}`$ | Two dynamical Proca vectors: $`8`$ | Two massless vectors: $`6`$ |
| $`(c,v,b_2,e_3)`$ | Including all mixing, $`20`$ | After the extra gauge quotient, $`13`$ |
| Gravitino spin$`\tfrac32`$ | $`32`$ | $`28`$ |
| Gravitino spin$`\tfrac12`$–$`\zeta`$ mixing | $`12`$ | $`4`$ |
| $`\omega,\phi,f`$ and composites | Dependent; not separately counted as fields or modes | Unchanged |

These extra symmetries belong to the quadratic theory on this background. No extension to new nonlinear gauge symmetries is claimed. Local counts alone do not determine which ordinary or logarithmic modes satisfy global boundary conditions.

