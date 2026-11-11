# Fluxless AdS₅ backgrounds of the total theory

```math
\begin{gathered}
R_{abcd}=-\ell^{-2}
(\eta_{ac}\eta_{bd}-\eta_{ad}\eta_{bc}),
\qquad R_0=-\frac{20}{\ell^2}<0,\\
L=L_0>0,\qquad N=N_0,\qquad
G=H=dE_3=dV=0,\\
E_a=V_\mu^{\prime\,ij}=0,\qquad
\psi_\mu{}^i=\varphi^i=0.
\end{gathered}
```

The total theory has **three solution families** in this class. The earlier AdS₅ branch is one; the others are retained below.

Throughout the calculation

```math
\lambda:=\lambda_{R^2},\qquad g\ne0
```

as the notation used below.

Background values of the dependent objects in the total action are

```math
\begin{aligned}
T_{ab}&=0,
&
f_a{}^a&=-\frac{R_0}{16},\\
D_0&=-\frac{R_0}{32}+\frac g4N_0+\frac{g^2L_0^2}{16},
&
\rho'_0&=\frac{2N_0}{L_0},\\
Y'_{ij}\big|_0&=\frac{\delta_{ij}}{\sqrt2}y_0,
&
y_0&=-\frac{R_0}{2}-\frac{N_0^2}{L_0^2}
+gN_0+\frac{g^2L_0^2}{4}
\end{aligned}
```

In particular, $`D_0=0`$ has not been imposed at the outset.

Extract the algebraic density determining the nonvanishing variations in this class. Temporarily replace $`L_0,N_0,R_0`$ by $`L,N,R`$:

```math
z:=-\frac R2-\frac{N^2}{L^2}+\frac{g^2L^2}{4},
\qquad y=z+gN.
```

Keeping the source coefficients,

```math
\begin{aligned}
I_2
&=-2\left(Ly+\frac{2N^2}{L}\right)
-4g\left(N-\frac g2L^2\right)\\
&=LR-\frac{2N^2}{L}-2gLN-4gN
-\frac{g^2L^3}{2}+2g^2L^2,\\
I_4
&=y^2-2gNy+
\left(\frac{2N}{L}\right)^2(2f_a{}^a-4D)\\
&=(y-gN)^2-g^2N^2
+\frac{4N^2}{L^2}\left(-gN-\frac{g^2L^2}{4}\right)\\
&=z^2-2g^2N^2-\frac{4gN^3}{L^2}.
\end{aligned}
```

Therefore,

```math
\boxed{
\begin{aligned}
\mathcal F(R,L,N)
={}&LR-\frac{2N^2}{L}-2gLN-4gN
-\frac{g^2L^3}{2}+2g^2L^2\\
&+\lambda\left(z^2-2g^2N^2-\frac{4gN^3}{L^2}\right).
\end{aligned}}
\tag{1}
```

Background conditions are imposed after variation. For example, the $`\Box L/L`$ contribution in the full composite gives

```math
\delta S\big|_{\delta(\Box L)}
=\int e\,\frac{2\lambda z}{L}\Box\delta L
=\int e\,\delta L\,\Box\left(\frac{2\lambda z}{L}\right)=0
```

The final equality holds on a constant background. Other contributions containing $`\nabla L`$ and $`\nabla(2N/L)`$ also vanish after their first variations are taken.

```math
\partial_Rz=-\frac12,\qquad
\partial_Nz=-\frac{2N}{L^2},\qquad
\partial_Lz=\frac{2N^2}{L^3}+\frac{g^2L}{2}
```

Using this relation, the original independent $`N,L`$ equations are

```math
\boxed{
\begin{aligned}
0=\mathcal E_N
={}&-\frac{4N}{L}-2gL-4g\\
&+\lambda\left(
-\frac{4Nz}{L^2}-4g^2N-\frac{12gN^2}{L^2}
\right),\\[2mm]
0=\mathcal E_L
={}&R+\frac{2N^2}{L^2}-2gN
-\frac32g^2L^2+4g^2L\\
&+\lambda\left[
\left(g^2L+\frac{4N^2}{L^3}\right)z
+\frac{8gN^3}{L^3}
\right]
\end{aligned}}
\tag{2}
```

as stated.

In the metric variation

```math
\mathcal A:=\partial_R\mathcal F=L-\lambda z,
```

```math
\mathcal E_{\mu\nu}
=\mathcal A R_{\mu\nu}
-\frac12\mathcal Fg_{\mu\nu}
+(g_{\mu\nu}\Box-\nabla_\mu\nabla_\nu)\mathcal A.
```

On the constant maximally symmetric background, its only independent condition is

```math
\boxed{
0=\mathcal E_{\mathrm{met}}
=\frac R5(L-\lambda z)-\frac12\mathcal F.
}
\tag{3}
```

No division by $`\mathcal A`$ has been performed.

The other independent field equations are also checked together. In particular, the $`E_3`$ variation must be taken even though $`E_a=0`$:

```math
\begin{aligned}
0={}&
\left(1+\frac{2\lambda gN}{L}\right)F'_{ab}
+g\left(2-\frac{2\lambda N^2}{L^2}\right)G_{ab}\\
&+2g(L-\lambda z)\left(\frac16\varepsilon_{abcde}H^{cde}\right).
\end{aligned}
```

This equation vanishes in the selected class. Currents in the $`C,B,V`$ equations consist of vanishing field strengths and their derivatives. The linear contribution of the $`V'`$ variation is orthogonal to $`L_{ij}`$; since $`Y'_{ij}\propto L_{ij}`$, its contraction vanishes. Thus

```math
\mathcal E_C=\mathcal E_B=\mathcal E_{E_3}
=\mathcal E_V=\mathcal E_{V'}=0.
```

Since the fermionic action is Grassmann-even,

```math
\left.\frac{\delta^L S}{\delta\psi_\mu{}^i}\right|_0
=
\left.\frac{\delta^L S}{\delta\varphi^i}\right|_0=0.
```

The complete background system to solve is therefore **(2) and (3)**.

Define dimensionless variables to solve without losing branches:

```math
t:=\lambda g^2,\qquad
v:=\frac{2N}{gL^2},\qquad
\zeta:=\frac{z}{g^2L^2},\qquad
\xi:=tL^2.
```

These imply

```math
N=\frac g2vL^2,\qquad
R=\frac{g^2L^2}{2}(1-v^2-4\zeta)
\tag{4}
```

as obtained.

The following equation combinations are invertible and use only $`g\ne0,L>0`$:

```math
P_1=-\frac{\mathcal E_N}{2g},\qquad
P_2=\frac{\mathcal E_L}{g^2L}+\frac{v\mathcal E_N}{2g},
\qquad
P_3=\frac{10\mathcal E_{\mathrm{met}}}{g^2L^2}.
```

Direct substitution gives

```math
\begin{pmatrix}P_1\\P_2\\P_3\end{pmatrix}
=
\begin{pmatrix}
v+1 & v(\zeta+1+\frac32v) & 2\\
-2\zeta-(v+1)^2 & \zeta-v^2-\frac12v^3 & 4-2v\\
6\zeta+4v^2+5v+1 &
-\zeta^2+\zeta v^2-\zeta+\frac52v^3+\frac52v^2 &
10(v-1)
\end{pmatrix}
\begin{pmatrix}L\\\xi\\1\end{pmatrix}
=0
\tag{5}
```

gives the result.

The determinant of this matrix is

```math
\boxed{\det M=2(\zeta+v)K(v,\zeta)}
\tag{6}
```

and factorizes as shown, where

```math
K(v,\zeta)
=2\zeta^2+(2v^2+3v-1)\zeta
+v^4+7v^3+7v^2-2v-3.
\tag{7}
```

Define the determinant and numerators of the first two rows by

```math
\begin{aligned}
\Delta(v,\zeta)
&:=(v+1)\left(\zeta-v^2-\frac12v^3\right)\\
&\quad+v\left(\zeta+1+\frac32v\right)
\left[2\zeta+(v+1)^2\right],\\
b(v,\zeta)&:=\zeta(v-1)^2+v^3-3v^2-2v,\\
c(v,\zeta)&:=2\zeta+3v+3
\end{aligned}
```

Then, for $`\Delta\ne0`$,

```math
L=-\frac{2b}{\Delta},\qquad
\xi=-\frac{2c}{\Delta},\qquad
P_3=\frac{2(\zeta+v)K}{\Delta}.
\tag{8}
```

The case $`\Delta=0`$ is retained separately. Consistency requires $`b=c=0`$:

```math
c=0\ \Longrightarrow\ \zeta=-\frac32(v+1),
```

```math
b=-\frac12(v+3)(v^2+1)=0.
```

For real fields, the only possibility is

```math
v=-3,\qquad \zeta=3
\tag{9}
```

as stated.

The **first family** comes from this special point. In (5),

```math
(P_1,P_2,P_3)
=(1,5,-20)\left(-2L+2+\frac32\xi\right),
```

and therefore

```math
\boxed{
\begin{gathered}
3\lambda g^2L_0^2-4L_0+4=0,\qquad L_0>0,\\
N_0=-\frac32gL_0^2,\qquad
R_0=-10g^2L_0^2,\qquad
\ell^2=\frac{2}{g^2L_0^2}.
\end{gathered}}
\tag{10}
```

These values are derived from the total system, not imported from the two-derivative theory.

The positive roots are

```math
L_-=\frac{2}{1+\sqrt{1-3\lambda g^2}},\qquad
L_+=\frac{2}{1-\sqrt{1-3\lambda g^2}}
\tag{11}
```

with:

- $`t<0`$: only $`L_-`$.
- $`t=0`$: $`L_0=1`$.
- $`0<t<1/3`$: two positive roots.
- $`t=1/3`$: coincident root $`L_0=2`$.
- $`t>1/3`$: no real solution in this family.

In this family,

```math
D_0=0,\qquad \mathcal A_0=4-3L_0.
```

The **second family** is the $`\zeta=-v`$, $`v\ne-3`$ branch. Here

```math
\Delta=-\frac12v^2(v+3),\qquad
b=-v(v+3),\qquad c=v+3.
```

Equation (8) directly gives

```math
L=-\frac4v,\qquad
\xi=\frac4{v^2},\qquad
t=\frac{\xi}{L^2}=\frac14
```

Since $`v=0`$ requires $`P_1=L+2=0`$, it is incompatible with $`L>0`$.

The solution in the original fields is:

```math
\boxed{
\begin{gathered}
\lambda g^2=\frac14,\qquad
N_0=-2gL_0,\\
R_0=\frac{g^2}{2}(L_0^2-16L_0-16),\\
0<L_0<8+4\sqrt5,\qquad
\ell^2=\frac{40}{g^2(16+16L_0-L_0^2)}.
\end{gathered}}
\tag{12}
```

The upper bound is the condition $`R_0<0`$; equality gives Minkowski geometry.

In this family,

```math
\boxed{
\mathcal A_0=0,\qquad
D_0=\frac{g^2}{64}(3L_0^2-16L_0+16).
}
\tag{13}
```

Thus $`D_0`$ is generally nonzero. The point $`L_0=4/3`$ is shared with the first family.

The **third family** is the $`K(v,\zeta)=0`$ branch. Its discriminant is

```math
\mathscr D(v):=-4v^4-44v^3-51v^2+10v+25
```

with

```math
\zeta_\pm(v)
=\frac{-(2v^2+3v-1)\pm\sqrt{\mathscr D(v)}}4.
```

The curvature follows from (4):

```math
\frac{R_0}{g^2L_0^2}
=\frac{v(v+3)\mp\sqrt{\mathscr D(v)}}2
\tag{14}
```

as stated.

The AdS choice leaves no sign ambiguity, because

```math
\mathscr D(v)-[v(v+3)]^2
=-5(v+1)^2(v^2+8v-5),
```

On the $`\zeta_-`$ branch, $`R_0\ge0`$. On the $`\zeta_+`$ branch,

```math
R_0<0
\quad\Longleftrightarrow\quad
-4-\sqrt{21}<v<-4+\sqrt{21}.
\tag{15}
```

Hereafter, evaluate $`b,c,\Delta`$ on $`\zeta=\zeta_+(v)`$ and define

```math
\mathcal L(v):=-\frac{2b}{\Delta},\qquad
\mathcal T(v):=-\frac{c\Delta}{2b^2}
\tag{16}
```

as follows. **For a supplied $`\lambda,g`$, the full solution of this family is**

```math
\boxed{
\begin{gathered}
\mathcal T(v)=\lambda_{R^2}g^2,\\
L_0=\mathcal L(v),\qquad
N_0=\frac g2v\,\mathcal L(v)^2,\\
\ell^2=
\frac{40}{
g^2\mathcal L(v)^2
\left[\sqrt{\mathscr D(v)}-v(v+3)\right]}.
\end{gathered}}
\tag{17}
```

Take **all real roots** in the allowed intervals below. Equation (17) thus replaces multivariable field equations with explicitly defined univariate algebraic root functions; no $`\lambda`$ expansion is made.

The boundaries of the condition $`L_0>0`$ follow from these polynomials:

```math
\begin{aligned}
P_B(v)&=v^5-2v^4-v^3+4v^2+3v-1,\\
P_\Delta(v)&=2v^5+22v^4+28v^3+v^2-14v-2.
\end{aligned}
```

Indeed,

```math
\begin{aligned}
\mathop{\mathrm{Res}}\nolimits_\zeta(K,b)
&=(v+3)(v^2+1)P_B(v),\\
\mathop{\mathrm{Res}}\nolimits_\zeta(K,\Delta)
&=(v+1)^2(v+3)(v^2+1)P_\Delta(v).
\end{aligned}
```

```math
\begin{aligned}
\beta&:=\text{root of }P_\Delta\text{ in }(-0.147,-0.146)
\approx-0.1469371230,\\
\gamma&:=\text{root of }P_B\text{ in }(0.254,0.255)
\approx0.2547590577.
\end{aligned}
```

The allowed parameter set of the third family is therefore

```math
\boxed{
v\in(-4-\sqrt{21},\,\beta)
\ \cup\
(\gamma,\,-4+\sqrt{21})
}
\tag{18}
```

as stated.

The apparent $`0/0`$ at $`v=-3`$ has the continuous extension

```math
\mathcal L(-3)=\frac{22}{19},\qquad
\mathcal T(-3)=\frac{19}{121}
\tag{19}
```

This point already belongs to the first family and is not counted twice.

To specify special parameter regions, also determine the turning points of $`\mathcal T`$. With the partial derivatives $`K_v,K_\zeta`$,

```math
\zeta_+'=-\frac{K_v}{K_\zeta},
```

```math
\begin{aligned}
J:={}&b\left[(c\Delta)_vK_\zeta
-(c\Delta)_\zeta K_v\right]\\
&-2c\Delta\left[b_vK_\zeta-b_\zeta K_v\right],
\qquad
\mathcal T'=-\frac{J}{2b^3K_\zeta}.
\end{aligned}
```

Here

```math
\mathop{\mathrm{Res}}\nolimits_\zeta(J,K)
=16(v+1)^3(v+3)^3(v^2+1)^3P_{12}(v),
```

```math
\begin{aligned}
P_{12}(v)={}&4v^{12}+152v^{11}+1855v^{10}
+7903v^9+13976v^8+9559v^7\\
&-1285v^6-4103v^5+1061v^4+3928v^3
+1688v^2-755v-375.
\end{aligned}
```

The roots giving the two maxima on the AdS branch are

```math
\begin{aligned}
v_{\rm I}&\in(-1.319,-1.318),
&v_{\rm I}&\approx-1.31814535135,\\
v_{\rm II}&\in(-0.399,-0.398),
&v_{\rm II}&\approx-0.398492412927
\end{aligned}
```

and are uniquely isolated as shown. The other two real roots of $`P_{12}`$ fail $`\mathcal T'=0`$ on $`\zeta_+`$. Also,

```math
\mathcal T(-1)=\frac14,\qquad
\mathcal T'(-1)=0,\qquad
\mathcal T''(-1)=1.
```

The point $`v=-3`$ is not a turning point:

```math
\mathcal T'(-3)=\frac{72}{1331}.
```

With their exact algebraic definitions and approximate values, let

```math
\begin{aligned}
\tau_-&:=\frac{-27-6\sqrt{21}}{28}
\approx-1.94626622035,\\
\tau_+&:=\frac{-27+6\sqrt{21}}{28}
\approx0.0176947917763,\\
t_{\rm I}&:=\mathcal T(v_{\rm I})
\approx0.261217524538,\\
t_{\rm II}&:=\mathcal T(v_{\rm II})
\approx0.397672304715
\end{aligned}
\tag{20}
```

The value $`\tau_\pm`$ comes from the $`R_0=0`$ endpoints of the third family:

```math
v=-4\pm\sqrt{21}
\quad\Longrightarrow\quad
L_0=\frac43,\qquad
\mathcal T(v)=\frac{-27\mp6\sqrt{21}}{28}.
```

Roots in (17) are unique in each monotonic interval below. Thus taking $`v=\mathcal T^{-1}_{I}(\lambda_{R^2}g^2)`$ in the appropriate row fixes the full coefficient dependence.

| Interval of $`v`$ | Interval of $`\lambda_{R^2}g^2`$ | $`\mathcal T`$ |
|---|---|---|
| $`(-4-\sqrt{21},v_{\rm I}]`$ | $`(\tau_+,t_{\rm I}]`$ | Increasing |
| $`[v_{\rm I},-1]`$ | $`[1/4,t_{\rm I}]`$ | Decreasing |
| $`[-1,v_{\rm II}]`$ | $`[1/4,t_{\rm II}]`$ | Increasing |
| $`[v_{\rm II},\beta)`$ | $`(0,t_{\rm II}]`$ | Decreasing |
| $`(\gamma,-4+\sqrt{21})`$ | $`(-\infty,\tau_-)`$ | Increasing |

Shared endpoints count as one solution. The Sturm sequence used to count root intervals is

```math
S_0=P,\quad S_1=P',\quad
S_{n+1}=-\mathop{\mathrm{rem}}\nolimits(S_{n-1},S_n)
```

The sign variations at the infinite endpoints are

```math
\begin{array}{c|ccc}
P&P_B&P_\Delta&P_{12}\\ \hline
V(-\infty)&3&4&8\\
V(+\infty)&2&1&4
\end{array}
```

giving $`1,3,4`$ real roots, respectively. Filtering these roots by the branch and sign conditions above gives (18) and the monotonicity table.

Combining the three families, the number of **distinct finite local AdS₅ backgrounds with $`L_0>0`$**, for $`t=\lambda_{R^2}g^2`$, is:

| Parameter region | AdS₅ solutions |
|---|---:|
| $`t<\tau_-`$ | 2 |
| $`\tau_-\le t\le0`$ | 1 |
| $`0<t\le\tau_+`$ | 3 |
| $`\tau_+<t<1/4,\quad t\ne19/121`$ | 4 |
| $`t=19/121`$ | 3; two families intersect at one solution |
| $`t=1/4`$ | One continuous family and two discrete solutions |
| $`1/4<t<t_{\rm I}`$ | 6 |
| $`t=t_{\rm I}`$ | 5 |
| $`t_{\rm I}<t<1/3`$ | 4 |
| $`t=1/3`$ | 3 |
| $`1/3<t<t_{\rm II}`$ | 2 |
| $`t=t_{\rm II}`$ | 1; two branches merge |
| $`t>t_{\rm II}`$ | 0 |

At $`t=1/4`$, the continuous family is (12). The two discrete solutions outside it are:

```math
L_0=4,\qquad N_0=-24g,\qquad R_0=-160g^2,
```

and the solution from the third-family root

```math
v_*\in(-0.219,-0.218),
```

```math
v_*^6-7v_*^5+53v_*^4+178v_*^3
+191v_*^2+75v_*+9=0
```

Its values are exactly defined by (17); approximately,

```math
L_0\approx8.46074854076,\qquad
N_0\approx-7.81773897909\,g,\qquad
R_0\approx-185.108807922\,g^2.
```

For all families, the remaining dependent background values in the original fields are

```math
\boxed{
\begin{aligned}
T_{ab}&=0,&
\chi^i&=\phi_\mu{}^i=\lambda'^i=0,\\
\omega_\mu{}^{ab}&=\omega_\mu{}^{ab}(e),&
f_\mu{}^a&=\frac{1}{4\ell^2}e_\mu{}^a,\\
D_0&=\frac{5}{8\ell^2}+\frac g4N_0
+\frac{g^2L_0^2}{16},&
\rho'_0&=\frac{2N_0}{L_0},\\
Y'_{ij}\big|_0
&=\frac{\delta_{ij}}{\sqrt2}
\left(\frac{10}{\ell^2}-\frac{N_0^2}{L_0^2}
+gN_0+\frac{g^2L_0^2}{4}\right),&
F'_0&=0
\end{aligned}}
\tag{21}
```

as computed.

Thus the exact upper bound for AdS₅ existence in the selected fluxless class is

```math
\boxed{
\lambda_{R^2}g^2\le
t_{\rm II}
=\mathcal T(v_{\rm II})
\approx0.397672304715
}
```

The $`\mathcal A_0>0`$, $`\mathcal A_0<0`$, and $`\mathcal A_0=0`$ solutions are all retained. These are background results; all independent fluctuations, including $`\delta\psi_\mu{}^i,\delta\varphi^i`$, remain available.

## Verification of solution branches and selection of the spectral branch

This section substitutes the candidates above into the original field equations and checks reality, regularity, gauge symmetries, and background SUSY. It then specifies the branch and global boundary conditions for the spectrum. The notation $`\lambda=\lambda_{R^2}`$ and $`t=\lambda_{R^2}g^2`$ is retained. The field domain is

```math
g\in\mathbb R\setminus\{0\},\qquad
0<L_0<\infty,\qquad N_0\in\mathbb R\text{ finite},\qquad
0<\ell<\infty
```

The convention source is [CONVENTIONS.md](../../../common/details/source_conventions.md), and the action input is action.md.

### Back-substitution into the original field equations

The quantity $`\mathcal F`$ in (1) is only the part of the full density surviving for constant fields. Derivative terms are not dropped before variation. For example, retaining the boundary contribution explicitly,

```math
\begin{aligned}
\int_M e\,\frac{2\lambda z}{L}\Box\delta L
={}&\int_M e\,\delta L\,
\Box\!\left(\frac{2\lambda z}{L}\right)\\
&+\int_{\partial M}d\Sigma_\mu
\left[
\frac{2\lambda z}{L}\nabla^\mu\delta L
-\delta L\,\nabla^\mu\!\left(\frac{2\lambda z}{L}\right)
\right].
\end{aligned}
\tag{V.1}
```

Here $`d\Sigma_\mu`$ is the oriented geometric surface element. The volume contribution vanishes only after evaluation on the constant background. Equations (2) and (3) above are the original scalar and metric equations obtained in this way; no division by $`\mathcal A=L-\lambda z`$ is performed.

In the first family

```math
N=-\frac32gL^2,\qquad R=-10g^2L^2,\qquad z=3g^2L^2
```

Substituting these expressions,

```math
\begin{aligned}
\mathcal E_N
&=4gL-4g+\lambda g^3L^2(18+6-27)\\
&=-g(3tL^2-4L+4),\\
\mathcal E_L
&=g^2(-4L^2+4L)+\lambda g^4L^3(30-27)\\
&=g^2L(3tL^2-4L+4),\\
\mathcal F
&=-12g^2L^3+8g^2L^2+18\lambda g^4L^4,\\
\mathcal E_{\mathrm{met}}
&=-2g^2L^2(L-3tL^2)
-\frac12\left(-12g^2L^3+8g^2L^2+18tg^2L^4\right)\\
&=-g^2L^2(3tL^2-4L+4).
\end{aligned}
\tag{V.2}
```

Thus both roots satisfy all three equations simultaneously wherever they exist in the field domain:

```math
3tL^2-4L+4=0,\qquad
L_-=\frac{2}{1+\sqrt{1-3t}},\qquad
L_+=\frac{2}{1-\sqrt{1-3t}}.
```

| Parameter | Real, finite, positive roots |
|---|---|
| $`t<0`$ | Only $`L_-`$ |
| $`t=0`$ | $`L_0=1`$ |
| $`0<t<1/3`$ | $`L_-`$ and $`L_+`$ |
| $`t=1/3`$ | Coincident root $`L_0=2`$ |
| $`t>1/3`$ | None |

In the second family,

```math
t=\frac14,\qquad
N=-2gL,\qquad
R=\frac{g^2}{2}(L^2-16L-16),\qquad z=4g^2L
```

using this relation,

```math
\begin{aligned}
\mathcal E_N
&=g(4-2L)+\frac{1}{4g^2}g^3(8L-16)=0,\\
\mathcal E_L
&=-g^2L^2+\frac{1}{4g^2}(4g^4L^2)=0,\\
\mathcal A
&=L-\frac{4g^2L}{4g^2}=0,\\
\mathcal F
&=-2g^2L^2-8g^2L
+\frac{8g^4L^2+32g^4L}{4g^2}=0,\\
\mathcal E_{\mathrm{met}}&=0.
\end{aligned}
\tag{V.3}
```

The AdS condition directly gives

```math
L^2-16L-16<0,\qquad L>0
\quad\Longleftrightarrow\quad
\boxed{0<L<8+4\sqrt5}
```

This is a real continuous solution family; it cannot be removed from the equations because $`\mathcal A=0`$.

In the parametrization (7), (8), (16), and (17) of the third family,

```math
\begin{aligned}
v&=\frac{2N}{gL^2},\qquad \zeta=\frac{z}{g^2L^2},\\
K&=2\zeta^2+(2v^2+3v-1)\zeta
+v^4+7v^3+7v^2-2v-3,\\
b&=\zeta(v-1)^2+v^3-3v^2-2v,\\
c&=2\zeta+3v+3,\\
\Delta&=(v+1)\left(\zeta-v^2-\frac12v^3\right)
+v\left(\zeta+1+\frac32v\right)\left[2\zeta+(v+1)^2\right].
\end{aligned}
```

The denominator denoted by $`d`$ in the earlier explanation is the same $`\Delta`$ in this file's notation. The candidate solution is

```math
L=-\frac{2b}{\Delta},\qquad
t=-\frac{c\Delta}{2b^2},\qquad
N=\frac g2vL^2,\qquad
R=\frac{g^2L^2}{2}(1-v^2-4\zeta),\qquad K=0
\tag{V.4}
```

On back-substitution, the numerators of the first two equations vanish by the identities:

```math
\begin{aligned}
\Delta-(v+1)b-v\left(\zeta+1+\frac32v\right)c&=0,\\
\left[2\zeta+(v+1)^2\right]b
-\left(\zeta-v^2-\frac12v^3\right)c+(2-v)\Delta&=0.
\end{aligned}
\tag{V.5}
```

These give $`P_1=0`$ and $`P_2=0`$, respectively. Since $`P_1=-\mathcal E_N/(2g)`$ and $`P_2=\mathcal E_L/(g^2L)+v\mathcal E_N/(2g)`$, their counterparts in the original equations are

```math
\boxed{
\mathcal E_N=0,\qquad
\mathcal E_L=0,\qquad
\mathcal E_{\mathrm{met}}
=\frac{g^2L^2(\zeta+v)}{5\Delta}K
=\frac{4g^2b^2(\zeta+v)}{5\Delta^3}K=0
}
\tag{V.6}
```

This back-substitution covers every admissible root in (V.4). The point $`\Delta=0`$ is considered separately below.

### Reality and regularity

For the third family,

```math
\mathscr D(v)=-4v^4-44v^3-51v^2+10v+25,
```

```math
\zeta_\pm=\frac{-(2v^2+3v-1)\pm\sqrt{\mathscr D}}4,
\qquad
R_\pm=\frac{g^2L^2}{2}
\left[v(v+3)\mp\sqrt{\mathscr D}\right].
```

The factorization determining the sign check is

```math
\mathscr D-[v(v+3)]^2
=-5(v+1)^2(v^2+8v-5)
\tag{V.7}
```

If $`v(v+3)\ge0`$, then $`R_-\ge0`$ directly. If $`-3<v<0`$, then $`v^2+8v-5<0`$ and $`\sqrt{\mathscr D}\ge|v(v+3)|`$, again giving $`R_-\ge0`$. Thus the root $`\zeta_-`$ does not give AdS. For $`\zeta_+`$,

```math
R_+<0
\quad\Longleftrightarrow\quad
-4-\sqrt{21}<v<-4+\sqrt{21}.
```

Positivity of $`L=-2b/\Delta`$ is imposed separately. The results checking zeros of numerator and denominator are

```math
\begin{aligned}
\mathop{\mathrm{Res}}\nolimits_\zeta(K,b)
&=(v+3)(v^2+1)
\underbrace{(v^5-2v^4-v^3+4v^2+3v-1)}_{P_B(v)},\\
\mathop{\mathrm{Res}}\nolimits_\zeta(K,\Delta)
&=(v+1)^2(v+3)(v^2+1)
\underbrace{(2v^5+22v^4+28v^3+v^2-14v-2)}_{P_\Delta(v)}
\end{aligned}
```

The relevant roots remaining on $`\zeta_+`$ within the AdS interval are

```math
\begin{aligned}
\beta&=-0.146937123027868\ldots,\qquad P_\Delta(\beta)=0,\\
\gamma&=0.254759057728730\ldots,\qquad P_B(\gamma)=0
\end{aligned}
```

Consequently,

```math
\begin{array}{c|cccc}
v&(-4-\sqrt{21},-3)&(-3,\beta)&(\beta,\gamma)&(\gamma,-4+\sqrt{21})\\ \hline
b&-&+&+&-\\
\Delta&+&-&+&+\\
L&+&+&-&+
\end{array}
```

and

```math
\boxed{
v\in(-4-\sqrt{21},\beta)\cup(\gamma,-4+\sqrt{21})
}
```

The apparent singularity at $`v=-3`$ is removable. Along $`\zeta_+(v)`$,

```math
\begin{aligned}
b&=11(v+3)+O((v+3)^2),\\
\Delta&=-19(v+3)+O((v+3)^2),\\
c&=2(v+3)+O((v+3)^2)
\end{aligned}
```

and hence

```math
L\longrightarrow\frac{22}{19},\qquad
t\longrightarrow\frac{19}{121}.
\tag{V.8}
```

This local expansion computes only the $`0/0`$ limit of the parametrization; it makes no perturbative approximation to the action or field equations. The point is the same background as in the first family and is not counted twice. In contrast, $`L`$ diverges at $`v=\beta`$, while $`L=0`$ at $`v=\gamma`$. Both points lie outside the field domain. At the $`v=-4\pm\sqrt{21}`$ endpoints, $`R=0`$, outside the AdS class.

For every admissible candidate,

```math
R=-\frac{20}{\ell^2},\qquad
R_{\mu\nu}R^{\mu\nu}=\frac{80}{\ell^4},\qquad
R_{\mu\nu\rho\sigma}R^{\mu\nu\rho\sigma}=\frac{40}{\ell^4}
\tag{V.9}
```

these quantities are finite. The final two contractions give $`5\cdot16\ell^{-4}`$ and $`2\cdot5\cdot4\ell^{-4}`$ for $`R_{\mu\nu}=-4\ell^{-2}g_{\mu\nu}`$ and $`R_{\mu\nu\rho\sigma}=-\ell^{-2}(g_{\mu\rho}g_{\nu\sigma}-g_{\mu\sigma}g_{\nu\rho})`$, respectively. The composites are also regular for finite $`L_0>0,N_0,\ell^{-2}`$:

```math
T_{ab}=0,\qquad
D_0=\frac{5}{8\ell^2}+\frac g4N_0+\frac{g^2L_0^2}{16},
\qquad
\rho'_0=\frac{2N_0}{L_0}.
```

### Equations of the other independent fields

For every candidate, substitute

```math
G=H=dE_3=dV=0,\qquad E_a=V_\mu^{\prime\,ij}=0
```

as specified. For example,

```math
\delta(G^2)|_0=2G^{ab}\delta G_{ab}|_0=0,\qquad
\delta(H^2)|_0=2H^{abc}\delta H_{abc}|_0=0
```

The same operation cancels first variations of $`E^2,F'^2`$ and mixed field-strength terms. First variations of BF terms also multiply vanishing background field strengths. In the zero-potential representative, the equality $`\delta[E_3\wedge(F'+2gG)]|_0=0`$ is explicit.

There is no invariant one-, two-, or three-form under the point stabilizer of maximal symmetry: the metric and five-index volume tensor alone cannot produce a nonzero fully antisymmetric tensor of these degrees. Thus no nonzero component of a covariant form or vector equation can survive on this background:

```math
\boxed{
\mathcal E_C=\mathcal E_B=\mathcal E_{E_3}
=\mathcal E_V=\mathcal E_{V'}=0.
}
\tag{V.10}
```

No additional independent equation is introduced for $`E_a`$. It is computed by definition from $`E_a`$, $`E_3`$, and the other independent fields.

Since the fermionic action is Grassmann-even and at least quadratic in fermions, each term retains at least one background fermion after left variation:

```math
\boxed{
\left.\frac{\delta^L S}{\delta\psi_\mu{}^i}\right|_0
=
\left.\frac{\delta^L S}{\delta\varphi^i}\right|_0=0.
}
\tag{V.11}
```

These equalities do not set fermionic fluctuations to zero. No separate independent field equations are added for $`T,D,\chi`$ or dependent connections; their field dependence remains in the original variations.

### SUSY preserved by the background

To keep the NW–SE sign explicit, define

```math
J^i{}_k:=\delta^{ij}\epsilon_{kj}
=\begin{pmatrix}0&-1\\1&0\end{pmatrix},\qquad J^2=-\mathbf1
```

The defining gaugino $`\psi^i`$, set to zero by gauge fixing, is distinct from the independent gravitino $`\psi_\mu{}^i`$. Its transformation comes from the [first input, (4.12)–(4.13)](../../../common/two_derivative_action/details/construction.md). On the fluxless background, using $`\sigma=1`$, $`Y^{ij}=-gL^{ij}/2`$,

```math
0=\delta\psi^i\big|_0=-Y^{ij}\epsilon_j+\eta^i
=\frac g2L^{ij}\epsilon_j+\eta^i
```

this equality determines the gauge-preserving $`S`$-SUSY parameter:

```math
\eta=-\frac{gL_0}{2\sqrt2}J\epsilon.
```

Therefore,

```math
L_0^{ij}\eta_j
=\frac{L_0}{\sqrt2}(J\eta)^i
=-\frac{gL_0^2}{4}(J^2\epsilon)^i
=\frac{gL_0^2}{4}\epsilon^i.
```

The variation of the linear-multiplet fermion
$`\delta\varphi^i|_0=N_0\epsilon^i/2+3L_0^{ij}\eta_j`$
is therefore

```math
\boxed{
\delta\varphi^i\big|_0
=\left(\frac{N_0}{2}+\frac{3gL_0^2}{4}\right)\epsilon^i
=\frac{gL_0^2}{4}(v+3)\epsilon^i
}
\tag{V.12}
```

Since the coefficient multiplies the identity matrix, a projector cannot preserve partial SUSY where it is nonzero:

```math
\epsilon\ne0\quad\Longrightarrow\quad
N_0=-\frac32gL_0^2.
```

The required Weyl-multiplet gravitino transformation is taken from [Coomans–Ozkan, Eq. (2.4)](https://arxiv.org/pdf/1210.4704), using the same signature and NW–SE conventions. In the current gauge it reads

```math
\delta\psi_\mu
=\nabla_\mu\epsilon-\frac12V_\mu J\epsilon
+i\gamma\!\cdot\!T\,\gamma_\mu\epsilon-i\gamma_\mu\eta
```

Here $`\nabla_\mu=\partial_\mu+ \omega_\mu{}^{ab}(e)\gamma_{ab}/4`$. No action or different gauge choice is imported from this external source; transformation signs are evaluated with the spinor and curvature conventions above.

On the fluxless background, in the zero representative of the flat $`V`$ connection,

```math
\left(\nabla_\mu+
\frac{igL_0}{2\sqrt2}\gamma_\mu J\right)\epsilon=0.
```

```math
M:=iJ,\quad M^2=\mathbf1,\qquad
m:=\frac{gL_0}{2\sqrt2}
```

with the definitions

```math
\nabla_\mu\epsilon=-m\gamma_\mu M\epsilon
```

and

```math
\begin{aligned}
[\nabla_\mu,\nabla_\nu]\epsilon
&=m^2(\gamma_\nu\gamma_\mu-\gamma_\mu\gamma_\nu)\epsilon\\
&=-2m^2\gamma_{\mu\nu}\epsilon,\\
\frac14R_{\mu\nu ab}\gamma^{ab}\epsilon
&=-\frac{1}{2\ell^2}\gamma_{\mu\nu}\epsilon
\end{aligned}
```

follows. The equality requires

```math
\boxed{\ell^{-2}=4m^2=\frac{g^2L_0^2}{2}}
\tag{V.13}
```

this condition. Together, (V.12) and (V.13) select exactly the first-family values. Under these conditions, the Killing spinor connection is flat. On the simply connected AdS cover, eight real symplectic–Majorana initial spinor components remain free, giving eight real Killing spinors.

| Family | Preserved background SUSY |
|---|---|
| First family: $`L_-`$ and $`L_+`$ | 8 real supercharges |
| The second family is | 8 only at $`L_0=4/3`$; 0 elsewhere |
| Third family | 8 only at the intersection $`v=-3`$, $`L_0=22/19`$, $`t=19/121`$; 0 elsewhere |

For example, in the second family,

```math
D_0=\frac{g^2}{64}(3L_0-4)(L_0-4)
```

yet the point $`L_0=4`$ is not supersymmetric:

```math
\delta\varphi^i\big|_{L_0=4}
=\left(-gL_0+\frac34gL_0^2\right)_{L_0=4}\epsilon^i
=8g\,\epsilon^i\ne0.
```

Thus $`D_0=0`$ alone is not a sufficient SUSY condition.

### Preserved gauge symmetries

The internal connection symmetry remaining after gauge fixing is $`U(1)_V`$:

```math
\delta_\theta V=d\theta,\qquad
\delta_\theta\epsilon=\frac{\theta}{2}J\epsilon,
\qquad
J\,\mathbf1+\mathbf1 J^T=0.
```

The final equality shows that the $`L_{ij}=L_0\delta_{ij}/\sqrt2`$ direction is preserved. The condition $`V'=0`$ does not restore the gauge-fixed $`SU(2)`$ directions. The Abelian gauge symmetries of $`U(1)_V`$ and $`C`$ remain separate gauge redundancies.

The vector and form gauge transformations are

```math
\boxed{
\delta C=d\Lambda,\qquad
\delta E_3=d\Lambda_2,\qquad
\delta B=d\Lambda_1-\frac12\Lambda G-\frac g2\Lambda_2
}
\tag{V.14}
```

Using $`dG=0`$,

```math
\begin{aligned}
\delta H
&=d\delta B+\frac12d\Lambda\wedge G+\frac g2d\Lambda_2\\
&=-\frac12d\Lambda\wedge G-\frac g2d\Lambda_2
+\frac12d\Lambda\wedge G+\frac g2d\Lambda_2=0.
\end{aligned}
```

Diffeomorphisms and local Lorentz symmetries accompany these transformations. The background's geometric isometry algebra is $`\mathfrak{so}(4,2)`$. The two-derivative auxiliary-field equation relating $`V`$ and $`C`$ is not used here. This gauge classification alone does not determine the number of massless vectors.

### Selected spectral branch and special parameters

Branch selection checks the graviton kinetic coefficient at constant scalars. For a transverse-traceless fluctuation,

```math
\nabla^\mu h_{\mu\nu}=0,\qquad h^\mu{}_\mu=0,
\qquad \delta R=0
```

and with $`\kappa:=-\ell^{-2}`$,

```math
\begin{aligned}
\delta R_{\mu\nu}
&=\frac12\left(-\Box h_{\mu\nu}
-2R_{\mu\rho\nu\sigma}h^{\rho\sigma}
+2R_{\rho(\mu}h_{\nu)}{}^\rho\right)\\
&=-\frac12\Box h_{\mu\nu}+5\kappa h_{\mu\nu},\\
\delta\mathcal E_{\mu\nu}^{\rm TT}
&=\mathcal A_0(\delta R_{\mu\nu}-4\kappa h_{\mu\nu})\\
&=-\frac{\mathcal A_0}{2}
\left(\Box+\frac2{\ell^2}\right)h_{\mu\nu}.
\end{aligned}
\tag{V.15}
```

This examines only the spin-2 block for branch selection; other fluctuations remain in the total theory. In the first family,

```math
3tL_0^2=4L_0-4
\quad\Longrightarrow\quad
\mathcal A_0=L_0-3tL_0^2=4-3L_0.
```

Thus

```math
\begin{aligned}
L_-:\quad
\mathcal A_0>0
&\Longleftrightarrow L_-<\frac43
\Longleftrightarrow t<\frac14,\\
L_+:\quad
L_+\ge2
&\Longrightarrow\mathcal A_0\le-2.
\end{aligned}
\tag{V.16}
```

In the second family, $`\mathcal A_0=0`$. Therefore the selected spectral branch is $`L_-`$, continuously connected to the two-derivative limit and preserving eight real supersymmetries:

```math
\boxed{
\begin{gathered}
L_0=\frac{2}{1+\sqrt{1-3\lambda_{R^2}g^2}},\qquad
N_0=-\frac32gL_0^2,\\
R_0=-10g^2L_0^2,\qquad
\ell^{-2}=\frac{g^2L_0^2}{2},\qquad D_0=0,\\
\lambda_{R^2}g^2<\frac14,\qquad
g\in\mathbb R\setminus\{0\}.
\end{gathered}
}
\tag{V.17}
```

The continuity check is

```math
\lim_{\lambda_{R^2}\to0}L_0=1,\qquad
\lim_{\lambda_{R^2}\to0}N_0=-\frac32g,\qquad
\lim_{\lambda_{R^2}\to0}\ell^2=\frac2{g^2}
```

This limit does not mean using the two-derivative background at finite $`\lambda_{R^2}`$; the exact dependence in (V.17) is retained. Negative $`\lambda_{R^2}`$ is not separately excluded at this stage. A positive graviton coefficient does not prove positive norms or stability for every mode.

The background Jacobian of the original equations, computed at fixed $`\lambda,g`$, is, on the first family,

```math
\left.
\frac{\partial(\mathcal E_N,\mathcal E_L,\mathcal E_{\mathrm{met}})}
{\partial(N,L,R)}\right|_0
=
\begin{pmatrix}
\frac{4(35L_0-38)}{3L_0^2}
&\frac{8g(7L_0-8)}{L_0}
&-\frac{4(L_0-1)}{gL_0^2}\\
\frac{8g(7L_0-8)}{L_0}
&\frac{8g^2(22L_0-25)}3
&-\frac{17L_0-20}{3L_0}\\
8g(L_0-1)
&\frac{2g^2L_0(17L_0-20)}3
&-\frac{13L_0-4}{30}
\end{pmatrix}
```

This matrix is obtained by first differentiating (2) and (3) with respect to $`N,L,R`$ and then substituting $`N=-3gL_0^2/2`$, $`R=-10g^2L_0^2`$, and $`\lambda=4(L_0-1)/(3g^2L_0^2)`$. Its determinant is

```math
\boxed{
-\frac{8g^2}{15L_0^2}
(L_0-2)(3L_0-4)(19L_0-22)
}
\tag{V.18}
```

and factorizes as shown.

| Point | Meaning |
|---|---|
| $`\lambda_{R^2}=0`$ | Separate limit where the higher-derivative sector disappears |
| $`\lambda_{R^2}g^2=19/121`$, $`L_0=22/19`$ | Intersection of the selected branch with the third family; singular background Jacobian |
| $`\lambda_{R^2}g^2=1/4`$, $`L_0=4/3`$ | Graviton kinetic coefficient vanishes; intersection with the continuous family |
| $`\lambda_{R^2}g^2=1/3`$, $`L_0=2`$ | Merger of the two SUSY roots |

A vanishing Jacobian determinant implies neither a geometric singularity nor automatically a normalizable zero-frequency mode. In particular, $`19/121`$ lies on the selected branch; scalar–metric equations must not be eliminated there by dividing by a singular matrix. The point $`1/4`$ bounds the open region with positive graviton coefficient; it cannot be included in the generic calculation as though a regular inverse coefficient existed. Other solution families and special points remain in the background classification above.

### Geometry and boundary conditions for the global spectrum

The geometric and boundary choice is fixed by

```math
\boxed{
ds^2=\frac{\ell^2}{\cos^2\rho}
\left(-d\tau^2+d\rho^2+\sin^2\rho\,d\Omega_3^2\right),
\quad
\tau\in\mathbb R,\quad 0\le\rho<\frac{\pi}{2}
}
\tag{V.19}
```

This is global AdS$`_5`$ with unwrapped time. No quotient or thermal-time identification is taken; the boundary is $`\mathbb R\times S^3`$. Flat background connections have trivial holonomy, and the spin structure is that of the cover.

At the center, all fluctuations must have smooth Cartesian components. For example, for $`S^3`$ scalar harmonic degree $`j`$, the near-center equation is

```math
q''+\frac3\rho q'-\frac{j(j+2)}{\rho^2}q=0
```

and hence

```math
q\sim\rho^s,\qquad
s(s+2)-j(j+2)=(s-j)(s+j+2)=0.
```

The choice is $`q\sim\rho^j`$; the solution $`\rho^{-j-2}`$ is excluded at the center. Tensors and spinors likewise retain their smooth harmonics.

At the conformal boundary, choose **standard reflecting boundary conditions with zero sources**. The boundary metric is fixed to the Einstein cylinder; scalar, gauge, form, and fermionic sources vanish. Invariantly, the total theory must have a finite symplectic form and zero boundary flux for every pair of allowed fluctuations. Let $`\Phi^A`$ denote all independent fields and $`|\delta_r|`$ the Grassmann parity of a variation:

```math
\delta\boldsymbol L
=\boldsymbol E_A\,\delta\Phi^A+d\boldsymbol\Theta,
```

```math
\boldsymbol\omega(\delta_1,\delta_2)
=\delta_1\boldsymbol\Theta(\delta_2)
-(-1)^{|\delta_1||\delta_2|}
\delta_2\boldsymbol\Theta(\delta_1),
```

```math
\boxed{
\Omega_\Sigma=\int_\Sigma\boldsymbol\omega\ \text{finite},\qquad
\int_{\mathscr I}\boldsymbol\omega=0.
}
\tag{V.20}
```

Here $`\Sigma`$ is a spatial slice and $`\mathscr I`$ the timelike conformal boundary between two slices. For fluctuations satisfying the linear equations, $`d\boldsymbol\omega=0`$; Stokes' theorem gives

```math
\Omega_{\Sigma_2}-\Omega_{\Sigma_1}
=-\int_{\mathscr I}\boldsymbol\omega=0
```

The quantity $`\boldsymbol\Theta`$ must be computed from the **total action** preserving the selected boundary representative. This statement does not claim that the component symplectic flux of the full theory has been computed here.

The boundary difference of the previously selected representative (5.10) for the first sector is retained:

```math
S_{2\partial}^{\rm pot}-S_{2\partial}^{F}
=\frac16\int_{\partial M}d\Sigma_\nu\,
e\varepsilon^{\mu\nu\rho\sigma\lambda}
(A'_\mu+2gC_\mu)E_{\rho\sigma\lambda}.
```

The surface-density notation here follows action.md (A.32). This boundary difference is neither silently added to the selected total action nor assumed zero. Required boundary variations and the finite-flux definition use the same representative.

The standard boundary choice for a scalar second-order factor explicitly reads as follows. For $`z=\cos\rho`$ and $`(\Box-m_s^2)q=0`$,

```math
\Box q=\ell^{-2}(z^2q''-3zq')+\text{subleading terms},
```

```math
q\sim z^\Delta
\quad\Longrightarrow\quad
\Delta(\Delta-4)=m_s^2\ell^2.
```

Therefore,

```math
q=z^{2-\nu}a+z^{2+\nu}b+\cdots,\qquad
\nu=\sqrt{4+m_s^2\ell^2}.
```

Here $`a,b`$ are scalar boundary coefficients, unrelated to the earlier polynomial $`b(v,\zeta)`$. For real $`\nu>0`$, the radial flux of two solutions per unit boundary volume is

```math
\begin{aligned}
\sqrt{|g|}g^{zz}(q_1\partial_zq_2-q_2\partial_zq_1)
&\longrightarrow
\ell^3\big[(2+\nu)-(2-\nu)\big](a_1b_2-a_2b_1)\\
&=2\ell^3\nu(a_1b_2-a_2b_1).
\end{aligned}
```

The standard choice $`a=0`$ makes this flux vanish. At $`\nu=0`$,

```math
q=z^2(a\log z+b)+\cdots
```

the logarithmic **source** coefficient is set to zero. The mass window permitting alternative boundary conditions is not automatically included in the standard choice. For the distinction between boundary conditions and the operator domain, see [Ishibashi–Wald](https://arxiv.org/pdf/hep-th/0402184). This second-order example does not compute the mass or positive norm of every mode in the total theory. In particular, for $`m_s^2\ell^2<-4`$, $`\nu`$ is not real; applicability of the standard condition written with real exponents requires separate treatment.

For fermions, fix independent source data instead of setting the entire field to zero. For example, when a Dirac factor is written as

```math
(\mathord{\not{\nabla}}-\mu_f)\chi=0
```

the near-boundary indicial equation is

```math
\left[\gamma^{\hat z}(z\partial_z-2)-\mu_f\ell\right]\chi=0
```

and

```math
\gamma^{\hat z}u_s=s\,u_s,\quad s=\pm1
\quad\Longrightarrow\quad
s(\Delta-2)-\mu_f\ell=0
\quad\Longrightarrow\quad
\chi_s\sim z^{2+s\mu_f\ell}u_s
```

In this example, $`\chi`$ denotes a general Dirac eigenmode; the theory's dependent Weyl fermion $`\chi^i`$ is not added as an independent field. The source projector is fixed while the corresponding normalizable fermionic data remain. The parameter $`\mu_f`$ is not used as an already computed mass of the actual theory.

In a higher-derivative theory, this procedure applies to **every independent radial solution pair** of the linear operator. Fixing one boundary value for each original field is insufficient. In particular:

- $`\delta\psi_\mu{}^i`$ and $`\delta\varphi^i`$ are fully retained.
- $`\delta E_a`$, derived from $`E_3`$, is not an additional independent boundary field.
- Fluctuations of fields auxiliary in the two-derivative theory are not eliminated beforehand.
- Normalizable logarithmic solutions of critical operators are not removed merely because they are logarithmic.

This section verifies that **the background preserves eight supersymmetries**. Field-specific falloff exponents, all mode norms, and closure of the selected boundary conditions under those eight supersymmetries require the total quadratic operator. They do not follow from verification of the background equations.

The branch used in the spectrum is (V.17). Exact $`\lambda_{R^2},g`$ dependence is retained at generic parameters; the $`\lambda_{R^2}=0`$ limit, $`\lambda_{R^2}g^2=19/121`$ intersection, and $`\lambda_{R^2}g^2=1/4`$ critical boundary remain separate cases.
