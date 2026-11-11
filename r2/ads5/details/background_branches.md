# R²: AdS5 backgrounds and selected branch

[Reading guide](../README.md). The equation labels and local symbols below follow the action conventions specified for this theory.

<a id="5-fluxless-ads₅-background-equations-of-the-total-theory"></a>

## Fluxless AdS₅ background equations of the total theory

```math
R_{abcd}=-\ell^{-2}(\eta_{ac}\eta_{bd}-\eta_{ad}\eta_{bc}),\quad
R=-20\ell^{-2},\quad L=L_0>0,\quad N=N_0,
```
```math
G=H=dE_3=dV=0,\qquad E_a=V'=\psi_\mu=\varphi=0.
```
Temporarily denote the background scalars by $`(R,L,N)`$. The composites give
```math
T=0,\quad f_a{}^a=-\frac R{16},\quad
D=-\frac R{32}+\frac g4N+\frac{g^2L^2}{16},\quad
\rho'=\frac{2N}{L},
```
```math
z=-\frac R2-\frac{N^2}{L^2}+\frac{g^2L^2}{4},\qquad y=z+gN
```
With the source coefficients,
```math
\begin{aligned}
I_2&=-2\left(Ly+\frac{2N^2}{L}\right)-4g\left(N-\frac g2L^2\right),\\
I_4&=y^2-2gNy+\frac{4N^2}{L^2}
\left(-gN-\frac{g^2L^2}{4}\right)
=z^2-2g^2N^2-\frac{4gN^3}{L^2}.
\end{aligned}
```
The density remaining at constant fields is thus
```math
\mathcal F=LR-\frac{2N^2}{L}-2gLN-4gN-\frac{g^2L^3}{2}+2g^2L^2
+\lambda\left(z^2-2g^2N^2-\frac{4gN^3}{L^2}\right),
\qquad\lambda:=\lambda_{R^2}.
```
Derivative composites are varied first; for example, the final step of
```math
\int e\frac{2\lambda z}{L}\Box\delta L
\simeq\int e\,\delta L\,\Box\left(\frac{2\lambda z}{L}\right)=0
```
holds only on a constant background.

The three independent equations are
```math
\begin{aligned}
0=\mathcal E_N&=-\frac{4N}{L}-2gL-4g
+\lambda\left(-\frac{4Nz}{L^2}-4g^2N-\frac{12gN^2}{L^2}\right),\\
0=\mathcal E_L&=R+\frac{2N^2}{L^2}-2gN-\frac32g^2L^2+4g^2L
+\lambda\left[\left(g^2L+\frac{4N^2}{L^3}\right)z+\frac{8gN^3}{L^3}\right],\\
0=\mathcal E_{\mathrm{met}}&=\frac R5(L-\lambda z)-\frac12\mathcal F.
\end{aligned}
```
The form/connection equations vanish by zero field strengths and isotropy. After variation, the fermion equations contain at least one fermion and therefore vanish on this background. $`D=0`$ is not an initial assumption.

<a id="51-symbolic-separation-of-three-families"></a>

### Symbolic separation of three families

Only in this subsection, define
```math
t=\lambda g^2,\quad v=\frac{2N}{gL^2},\quad
z_*=\frac{z}{g^2L^2},\quad\xi=tL^2
```
Here $`v`$ is not an internal-connection fluctuation. The invertible equation combinations
```math
P_1=-\frac{\mathcal E_N}{2g},\quad
P_2=\frac{\mathcal E_L}{g^2L}+\frac{v\mathcal E_N}{2g},\quad
P_3=\frac{10\mathcal E_{\mathrm{met}}}{g^2L^2}
```
give the system
```math
\begin{pmatrix}P_1\\P_2\\P_3\end{pmatrix}
=\begin{pmatrix}
v+1&v(z_*+1+3v/2)&2\\
-2z_*-(v+1)^2&z_*-v^2-v^3/2&4-2v\\
6z_*+4v^2+5v+1&-z_*^2+z_*v^2-z_*+5v^3/2+5v^2/2&10(v-1)
\end{pmatrix}
\begin{pmatrix}L\\\xi\\1\end{pmatrix}.
```
The matrix determinant factorizes as
```math
\det M=2(z_*+v)K(v,z_*),
\quad K=2z_*^2+(2v^2+3v-1)z_*+v^4+7v^3+7v^2-2v-3
```
For the first two rows,
```math
\begin{aligned}
\Delta&=(v+1)(z_*-v^2-v^3/2)
+v(z_*+1+3v/2)[2z_*+(v+1)^2],\\
b&=z_*(v-1)^2+v^3-3v^2-2v,\qquad c=2z_*+3v+3.
\end{aligned}
```
For $`\Delta\neq0`$,
```math
L=-\frac{2b}{\Delta},\quad \xi=-\frac{2c}{\Delta},\quad
t=-\frac{c\Delta}{2b^2},\quad
P_3=\frac{2(z_*+v)K}{\Delta}.
```
The $`\Delta=0`$ branch is retained. Consistency requires $`b=c=0`$:
```math
z_*=-\frac32(v+1),\qquad
b=-\frac12(v+3)(v^2+1)=0
\quad\Longrightarrow\quad(v,z_*)=(-3,3).
```

**Family I.** At this special point,
```math
(P_1,P_2,P_3)=(1,5,-20)(-2L+2+3\xi/2),
```
```math
\boxed{3\lambda_{R^2}g^2L_0^2-4L_0+4=0,\quad
N_0=-\frac32gL_0^2,\quad R_0=-10g^2L_0^2.}
```
```math
L_\mp=\frac2{1\pm\sqrt{1-3\lambda_{R^2}g^2}}.
```
There is only $`L_-`$ at $`t<0`$, $`L_0=1`$ at $`t=0`$, two positive roots at $`0<t<1/3`$, and a repeated $`L_0=2`$ at $`t=1/3`$. This family has no real root at $`t>1/3`$. These statements classify backgrounds. The separate $`L_+`$ spectrum is not included; the shared $`t=1/3`$ endpoint is treated in the [local critical analysis](critical_branches.md#tau-2-endpoint).

Back-substitution gives
```math
(\mathcal E_N,\mathcal E_L,\mathcal E_{\mathrm{met}})
=(-g,g^2L_0,-g^2L_0^2)
(3\lambda g^2L_0^2-4L_0+4)
```
Also,
```math
D_0=\left(\frac5{16}-\frac6{16}+\frac1{16}\right)g^2L_0^2=0,
\quad \ell^2=\frac2{g^2L_0^2},\quad \mathcal A_0=4-3L_0.
```

**Family II.** For $`z_*=-v`$, $`v\neq-3`$,
```math
\Delta=-\frac12v^2(v+3),\quad b=-v(v+3),\quad c=v+3
```
and hence
```math
L=-\frac4v,\quad \xi=\frac4{v^2},\quad t=\frac14.
```
The original fields
```math
N_0=-2gL_0,\quad R_0=\frac{g^2}{2}(L_0^2-16L_0-16),\quad
0<L_0<8+4\sqrt5
```
give AdS₅. $`\mathcal A_0=\mathcal F_0=0`$ and the scalar Euler residuals vanish. In this continuous family,
```math
D_0=\frac{g^2}{64}(3L_0^2-16L_0+16)
```
is generally nonzero.

**Family III.** On $`K=0`$ and $`\Delta\neq0`$,
```math
\mathscr D(v)=-4v^4-44v^3-51v^2+10v+25,\qquad
z_*^\pm=\frac{-(2v^2+3v-1)\pm\sqrt{\mathscr D(v)}}4.
```
The solutions are retained through the exact algebraic conditions
```math
\boxed{
\begin{gathered}
K(v,z_*)=0,\quad\mathscr D(v)\geq0,\quad\Delta\neq0,\quad
L_0=-2b/\Delta>0,\\
-\frac{c\Delta}{2b^2}=\lambda_{R^2}g^2,\qquad
1-v^2-4z_*<0,\\
N_0=\frac g2vL_0^2,\quad
R_0=\frac{g^2L_0^2}{2}(1-v^2-4z_*),\quad\ell^2=-20/R_0.
\end{gathered}}
```
without numerical specialization. This definition keeps all admissible real roots rather than selecting one sample root. The back-substitution identities
```math
\begin{aligned}
\Delta-(v+1)b-v(z_*+1+3v/2)c&=0,\\
[2z_*+(v+1)^2]b-(z_*-v^2-v^3/2)c+(2-v)\Delta&=0
\end{aligned}
```
and
```math
\mathcal E_{\mathrm{met}}
=\frac{4g^2b^2(z_*+v)}{5\Delta^3}K=0
```
satisfy all three original equations. The apparent $`0/0`$ point is $`v=-3`$, the intersection with the first family at $`L_0=22/19`$, $`\lambda_{R^2}g^2=19/121`$; it is not counted twice.

<a id="6-susy-regularity-and-selection-of-the-spectrum-branch"></a>

## SUSY, regularity, and selection of the spectrum branch

```math
\mathbb I^i{}_j=\epsilon^{ik}\frac{\delta_{kj}}{\sqrt2},\quad
\mathbb I^2=-\frac12,\quad\mathbb J=i\sqrt2\mathbb I,\quad\mathbb J^2=1.
```
Under gauge-preserving SUSY, the background variation of the linear-multiplet fermion is
```math
\delta\varphi|_0=\left(\frac{N_0}{2}+\frac{3gL_0^2}{4}\right)\epsilon
```
so a nonzero Killing spinor requires
```math
N_0=-\frac32gL_0^2
```
The gravitino equation
```math
\nabla_\mu\epsilon=m\gamma_\mu\mathbb J\epsilon,
\quad m=\frac{gL_0}{2\sqrt2}
```
and its integrability condition
```math
[\nabla_\mu,\nabla_\nu]\epsilon=-2m^2\gamma_{\mu\nu}\epsilon
=-\frac1{2\ell^2}\gamma_{\mu\nu}\epsilon
```
give eight real supersymmetries. Family II satisfies these conditions only at $`L_0=4/3`$, and family III only at its $`L_0=22/19`$ intersection with family I.

The selected spectrum branch is
```math
\boxed{
L_0=\frac2{1+\sqrt{1-3\lambda_{R^2}g^2}},\quad
\lambda_{R^2}g^2<\frac14,\quad g\neq0
}
```
The abbreviations $`L=L_0`$, $`A=4-3L>0`$, and $`B=2-L>0`$ are used below. This choice uses a root of the total background equation rather than assuming the two-derivative background in advance.

$`L_0>0`$ is the field region where the composite denominators $`L^{-1}`$ are regular. At finite admissible parameters,
```math
R_0=-20\ell^{-2},\quad R_{\mu\nu}R^{\mu\nu}=80\ell^{-4},\quad
R_{\mu\nu\rho\sigma}R^{\mu\nu\rho\sigma}=40\ell^{-4}
```
is finite. The preserved local gauge structure comprises diffeomorphisms, Lorentz symmetry, residual $`U(1)`$, $`C`$ gauge symmetry, coupled form gauge symmetry, and local SUSY. The subset of gauge parameters leaving the background fixed is distinguished from gauge equivalence of fluctuations.

The global spectrum uses the universal cover of AdS₅, central regularity, fixed boundary sources, and zero symplectic boundary flux. Only gauge directions preserving the boundary conditions and carrying zero surface charge are removed in the quotient; asymptotic symmetries are not removed in the same way.

