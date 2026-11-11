# Fluxless AdS₅ backgrounds

This result uses the total action in [action.md](action.md)
and the conventions in [CONVENTIONS.md](../../../common/details/source_conventions.md):

```math
S=S_{2\text{-der}}^{(\leq2)}
+\alpha S_{\mathrm{Weyl}^2}^{(\leq2)},\qquad
\alpha\neq0,\qquad g\neq0,\qquad
\partial_\mu\alpha=\partial_\mu g=0.
```

The calculation is on the $`L_0\neq0`$ patch of the action. $`\alpha`$ and $`g`$
remain symbolic; $`\alpha`$ is not perturbative. No sample values are assigned
to couplings or their combinations. The special coupling values below
follow from root, repeated-root, or curvature-boundary conditions
of the equations.

<a id="1-selected-class-and-dependent-objects"></a>

## Selected class and dependent objects

The current gauge is retained:

```math
\sigma=1,\qquad \psi^i=0,\qquad b_\mu=0,\qquad
L_{ij}=\frac{L}{\sqrt2}\delta_{ij},\qquad
V_\mu^{ij}=V_\mu^{\prime\,ij}+\frac12\delta^{ij}V_\mu.
```

Here $`\psi^i`$ is the dilatino and must be distinguished from the independent
gravitino $`\psi_\mu^i`$. The background is:

```math
\begin{gathered}
R_{\mu\nu}=\frac{R_0}{5}g_{\mu\nu},
\qquad R_0=-\frac{20}{\ell^2}<0,\qquad
\nabla_\mu L_0=\nabla_\mu N_0=0,\\
G_0=H_0=dE_{3,0}=dV_0=0,\qquad
V_{\mu,0}^{\prime\,ij}=0,\qquad
\psi_{\mu,0}^{\,i}=\varphi_0^i=0 .
\end{gathered}
```

Fermionic fluctuations are retained. Composites:

```math
T_0=\chi_0=\phi_{\mu,0}=\widehat C_0=\widehat R(V)_0=0,
\qquad
f_{\mu,0}{}^a=-\frac{R_0}{80}e_\mu{}^a,
```

```math
\boxed{
D_0=-\frac{R_0}{32}+\frac{gN_0}{4}
+\frac{g^2L_0^2}{16}.
}
```

$`D_0=0`$ is not assumed at the outset. $`D`$ is not varied independently.
$`E_{a,0}=0`$ is calculated from the definition of $`E_3`$;
$`E_a`$ is not counted as another independent field.
$`\omega_{\mu,0}{}^{ab}`$ is the Levi-Civita connection.

<a id="2-total-background-equations"></a>

## Total background equations

Contribution of the two-derivative density to the first variation in this class:

```math
\begin{aligned}
e^{-1}\mathcal L_{2\text{-der}}
&\longrightarrow
-12Lf_a{}^a-\frac{2N^2}{L}-8LD-4gN+2g^2L^2\\
&=LR-\frac{2N^2}{L}-2g(L+2)N
+2g^2L^2-\frac12g^2L^3 .
\end{aligned}
```

The last equality uses $`f_a{}^a=-R/16`$ and the definition of the composite $`D`$.
This expression is not a truncation replacing the total action;
it determines first variations on the selected background.

The Weyl-squared term contributing to the first variation is

```math
\frac{64\alpha}{3}D^2,\qquad
\delta\!\left(\frac{64\alpha}{3}D^2\right)
=\frac{128\alpha}{3}D\,\delta D
```

so the $`R,L,N`$ dependence of $`D`$ must be retained. Temporarily write

```math
F(R,L,N)=LR-\frac{2N^2}{L}-2g(L+2)N
+2g^2L^2-\frac12g^2L^3+\frac{64\alpha}{3}D^2
```

The variations are:

```math
\boxed{
\begin{aligned}
0=F_N&=-\frac{4N}{L}-2g(L+2)+\frac{32\alpha g}{3}D,\\
0=F_L&=R+\frac{2N^2}{L^2}-2gN+4g^2L-\frac32g^2L^2
+\frac{16\alpha g^2L}{3}D,\\
F_R&=L-\frac{4\alpha}{3}D,\\
0=\mathcal E_{\mu\nu}
&=F_RR_{\mu\nu}-\frac12Fg_{\mu\nu}
+(g_{\mu\nu}\Box-\nabla_\mu\nabla_\nu)F_R .
\end{aligned}
}
```

For maximal symmetry with constant scalars, the last equation becomes

```math
\boxed{0=\frac{R}{5}F_R-\frac12F}
```

No division by $`F_R`$ is made.

The other independent-field equations in this class are:

```math
\left.\frac{\delta S}{\delta C_\mu}\right|_0
=
\left.\frac{\delta S}{\delta B_{\mu\nu}}\right|_0
=
\left.\frac{\delta S}{\delta E_{\mu\nu\rho}}\right|_0
=
\left.\frac{\delta S}{\delta V_\mu}\right|_0
=
\left.\frac{\delta S}{\delta V_\mu^{\prime\,ij}}\right|_0=0 .
```

First variations of flux and internal-connection terms contain factors
with vanishing background values; the BF source vanishes because $`G_0=\widehat R(V)_0=0`$.
Since the fermionic equations are Grassmann-odd,

```math
\left.\frac{\delta S}{\delta\bar\psi_\mu^i}\right|_0
=
\left.\frac{\delta S}{\delta\bar\varphi^i}\right|_0=0 .
```

The three remaining equations are therefore the $`N,L`$ and metric equations
above. These are equations of the total theory; the two-derivative
solution is not assumed as a background input.

<a id="3-complete-algebraic-solution-of-the-equations"></a>

## Complete algebraic solution of the equations

For this calculation only, define

```math
b:=\alpha g^2,\qquad t:=\frac{8\alpha D_0}{3}
```

No values are assigned to them. $`t`$ labels the background value
of the dependent composite.

The $`N`$ equation and the definition of $`D`$ are:

```math
\begin{aligned}
0&=-\frac{4N_0}{L_0}-2g(L_0+2)+4gt,\\
N_0&=gL_0\left(t-1-\frac{L_0}{2}\right),\\
R_0&=-32D_0+8gN_0+2g^2L_0^2\\
&=g^2\left(-\frac{12t}{b}+8L_0t-2L_0^2-8L_0\right).
\end{aligned}
```

Substitution into the two remaining equations gives

```math
F_L=\frac{2g^2}{b}P,\qquad
\frac{R_0}{5}F_R-\frac12F=\frac{g^2}{10b}Q,
```

where

```math
\begin{aligned}
P={}&bt^2+(3bL_0-2b-6)t+b(1-L_0^2),\\
Q={}&(2bL_0-3)t^2
+(-22bL_0^2+8bL_0+36L_0)t\\
&+6bL_0^3+4bL_0^2-10bL_0 .
\end{aligned}
```

Thus the system to solve is $`P=Q=0`$. The following polynomial identity
performs the elimination directly:

```math
\boxed{
Q+(6L_0-4t+4)P
=-4b(t-1)^2(L_0+t-1)+3t(7t-8).
}
```

For $`t=1`$, the right-hand side is $`-3`$, so $`t=1`$ is not a solution. Thus

```math
\boxed{
L_0=1-t+\frac{3t(7t-8)}{4b(t-1)^2}.
}
\tag{1}
```

Substituting this expression into $`P`$ gives

```math
P=-\frac{3t}{16b(t-1)^4}\,\mathcal H(t;b),
```

```math
\boxed{
\mathcal H(t;b)=
16b^2(t-1)^5
-4b(t-1)^2(27t^2-38t+8)
+3t(7t-8)^2 .
}
\tag{2}
```

The exact root equation is:

```math
\boxed{t\,\mathcal H(t;\alpha g^2)=0.}
\tag{3}
```

This elimination loses no solutions:

- $`b\neq0`$ is the supplied condition $`\alpha\neq0,\ g\neq0`$.
- $`t=1`$ is already excluded by the equations.
- Setting $`L_0=0`$ gives $`Q=-3t^2=0`$, then $`P=b=0`$; no additional root arises
  on this excluded patch.
- Under (1), $`Q=(-6L_0+4t-4)P`$. Thus (3) satisfies both remaining equations.

$`P=0`$ also simplifies the curvature:

```math
\begin{aligned}
\frac{R_0}{g^2}
+2\big[(t-1)^2+(4-t)L_0\big]
&=\frac{2P}{b}=0,\\
R_0&=-2g^2\big[(t-1)^2+(4-t)L_0\big].
\end{aligned}
```

Thus the AdS selection is precisely

```math
\boxed{
\mathcal A:=(t-1)^2+(4-t)L_0>0,\qquad
\ell^2=\frac{10}{g^2\mathcal A}
}
\tag{4}
```

the stated condition.

<a id="4-first-branch-t0"></a>

## First branch: $`t=0`$

Together, (1), $`N_0`$, and (4) give

```math
\boxed{
D_0=0,\qquad L_0=1,\qquad
N_0=-\frac{3g}{2},\qquad
R_0=-10g^2,\qquad \ell^2=\frac2{g^2}
}
```

This branch follows from the total equations without assuming the
two-derivative solution as an input. $`L_0=1`$ is neither a normalization
nor an additional gauge choice.

<a id="5-additional-branches-mathcal-htalpha-g20-tneq0"></a>

## Additional branches: $`\mathcal H(t;\alpha g^2)=0`$, $`t\neq0`$

All real roots of the quintic are evaluated using (1) and (4).
To specify the AdS roots by explicit intervals, solve (2) for $`b`$:

```math
\begin{gathered}
\Delta(t):=(3t^2-4)(47t^2-40t-16),\\
\boxed{
\alpha g^2=b_\pm(t):=
\frac{27t^2-38t+8\ \pm\sqrt{\Delta(t)}}{8(t-1)^3}.
}
\end{gathered}
\tag{5}
```

This defines a solution curve, not a fixed coupling: for a given $`\alpha,g`$,
take the $`t`$ values satisfying (5).

The corresponding scalar and AdS condition are:

```math
\begin{aligned}
L_\pm(t)
&=\frac{13t^2-8t-8\ \mp\sqrt{\Delta(t)}}{2(7t-8)},\\
\mathcal A_\pm(t)
&=\frac{t^3+16t^2+22t-48
\ \mp(4-t)\sqrt{\Delta(t)}}{2(7t-8)},\\
\mathcal A_+\mathcal A_-
&=-\frac{5(t-1)^3(t^2-5t-8)}{7t-8}.
\end{aligned}
\tag{6}
```

The final factorization also locates the curvature zeros. With temporary
endpoints

```math
a_-=\frac{20-24\sqrt2}{47},\qquad
t_f^\pm=\frac{5\pm\sqrt{57}}2
```

the exact AdS regions satisfying $`\Delta\ge0`$, $`b_\pm\neq0`$, and $`\mathcal A_\pm>0`$ are:

| Solution curve | Admissible regions of $`t`$ |
|---|---|
| $`b_+(t)`$ | $`(-\infty,-2/\sqrt3]\ \cup\ [a_-,1)\ \cup\ (1,8/7)\ \cup\ [2/\sqrt3,\infty)`$ |
| $`b_-(t)`$ | $`(t_f^-,-2/\sqrt3]\ \cup\ [a_-,0)\ \cup\ (0,1)\ \cup\ [2/\sqrt3,t_f^+)`$ |

When counting additional branches, remove $`t=0`$, which already belongs
to the first branch. Endpoints where the two signed expressions reach
the same root are counted once.

<a id="6-special-coupling-conditions"></a>

## Special coupling conditions

<a id="61-intersection-of-the-first-and-an-additional-branch"></a>

### Intersection of the first and an additional branch

```math
\mathcal H(0;b)=-16b(b+2).
```

Under $`b\neq0`$, the intersection is at

```math
\boxed{\alpha g^2=-2}
```

At this point,

```math
\partial_t\mathcal H(0;-2)=80\neq0,
```

so the $`t=0`$ root of $`t\mathcal H`$ is double. This value is derived
from the branch-intersection equation, not selected as an example.

<a id="62-adszero-curvature-boundary"></a>

### AdS–zero-curvature boundary

From (6),

```math
t^2-5t-8=0.
```

Together with (2), this gives

```math
768b^2+471b-256=0
```

The boundary couplings are:

```math
\boxed{
b_f^\pm=\frac{-471\pm133\sqrt{57}}{1536}.
}
\tag{7}
```

The $`R_0=0`$ root at these points is excluded from the selected AdS class;
other AdS roots at the same coupling are retained.

<a id="63-f_r0-solutions"></a>

### $`F_R=0`$ solutions

The coefficient in the metric equation that must not be divided out is:

```math
F_R=L_0-\frac t2.
```

Together, $`F_R=0`$ and $`P=Q=0`$ give

```math
t=\frac{2\varepsilon}{\sqrt3},\qquad
\alpha g^2=\frac32(1+\varepsilon\sqrt3),
\qquad \varepsilon=\pm1
```

These solutions are:

```math
\boxed{
\begin{aligned}
L_0&=\frac{\varepsilon}{\sqrt3},&
N_0&=g\left(\frac12-\frac{\varepsilon}{\sqrt3}\right),\\
D_0&=\frac{\varepsilon\sqrt3}{4\alpha},&
R_0&=-\frac{10g^2}{3},&
\ell^2&=\frac6{g^2}.
\end{aligned}
}
\tag{8}
```

They belong to the full solution set and are not discarded because $`F_R=0`$.

<a id="7-number-of-distinct-ads-roots-in-coupling-regions"></a>

## Number of distinct AdS roots in coupling regions

Repeated-root condition:

```math
\mathop{\mathrm{Disc}}\nolimits_t[t\mathcal H]
=
2^{20}3^3\,b^5(b+2)^2\,\mathfrak D(b),
```

```math
\begin{aligned}
\mathfrak D(b)={}&
186624b^6-7846080b^5+13587168b^4\\
&+64903811b^3-29363796b^2
-181528020b-111428352 .
\end{aligned}
\tag{9}
```

Define the four real simple roots of this polynomial as

```math
\eta_-<0<\eta_1<\eta_2<\eta_3
```

These are exact algebraic roots of (9), not approximate numbers.
Their ordering is:

```math
\boxed{
-2<\eta_-<\frac32(1-\sqrt3)<b_f^-<0
<b_f^+<\eta_1<\eta_2
<\frac32(1+\sqrt3)<\eta_3 .
}
\tag{10}
```

The stationary points determining the root count are also found symbolically:

```math
\begin{aligned}
\mathcal H=\partial_t\mathcal H=0
\quad\Longrightarrow\quad
0={}&987t^6-1263t^5-2577t^4\\
&+3103t^3+1728t^2-1392t-640 .
\end{aligned}
\tag{11}
```

The coupling at these points is

```math
b_c(t)=
\frac{3(7t-8)(14t^2-11t-8)}
{4(t-1)^2(27t^2-22t-14)}
```

Temporarily denote the polynomial on the right of (11) by $`C(t)`$.
Using the Sturm sequence

```math
S_0=C,\qquad S_1=C',\qquad
S_{k+1}=-\mathop{\mathrm{rem}}\nolimits(S_{k-1},S_k)
```

the numbers of sign changes are:

```math
\begin{array}{c|ccccc}
t&-\infty&t_f^-&2/\sqrt3&t_f^+&+\infty\\ \hline
V_C(t)&5&4&4&1&1
\end{array}
```

Thus one stationary point lies in $`t<t_f^-`$ and three lie in $`2/\sqrt3<t<t_f^+`$.
At these four ordered points:

| Curve | Stationary point | Coupling |
|---|---|---|
| $`b_+`$ | Minimum | $`\eta_-`$ |
| $`b_-`$ | Minimum | $`\eta_1`$ |
| $`b_+`$ | Maximum | $`\eta_3`$ |
| $`b_-`$ | Maximum | $`\eta_2`$ |

Together with the endpoints in (5)–(7), this separation gives the following
count. Coincident roots are counted once; $`R_0=0`$ roots are not counted.

| Negative-coupling region | Distinct AdS₅ roots |
|---|---:|
| $`\alpha g^2<\eta_-`$, $`\alpha g^2\neq-2`$ | 3 |
| $`\alpha g^2=-2`$ | 2 |
| $`\alpha g^2=\eta_-`$ | 4 |
| $`\eta_-<\alpha g^2<b_f^-`$ | 5 |
| $`b_f^-\le\alpha g^2<0`$ | 4 |
| Positive-coupling region | Distinct AdS₅ roots |
|---|---:|
| $`0<\alpha g^2\le b_f^+`$ | 3 |
| $`b_f^+<\alpha g^2<\eta_1`$ | 4 |
| $`\alpha g^2=\eta_1`$ | 5 |
| $`\eta_1<\alpha g^2<\eta_2`$ | 6 |
| $`\alpha g^2=\eta_2`$ | 5 |
| $`\eta_2<\alpha g^2<\eta_3`$ | 4 |
| $`\alpha g^2=\eta_3`$ | 3 |
| $`\alpha g^2>\eta_3`$ | 2 |

<a id="8-all-background-values-in-the-original-variables"></a>

## All background values in the original variables

The function $`\mathcal H`$ is defined in (2). The final solution is:

```math
\boxed{
\begin{gathered}
\frac{8\alpha D_0}{3}\,
\mathcal H\!\left(\frac{8\alpha D_0}{3};\alpha g^2\right)=0,
\qquad \frac{8\alpha D_0}{3}\neq1,\\[2mm]
L_0=
1-\frac{8\alpha D_0}{3}
+\frac{48D_0(7\alpha D_0-3)}
{g^2(8\alpha D_0-3)^2},\\[2mm]
N_0=gL_0\left(\frac{8\alpha D_0}{3}-1-\frac{L_0}{2}\right),\\[2mm]
R_0=-2g^2
\left[
\left(1-\frac{8\alpha D_0}{3}\right)^2
+\left(4-\frac{8\alpha D_0}{3}\right)L_0
\right]<0,\\[2mm]
\ell^2=
\frac{10}{
g^2\left[
\left(1-\frac{8\alpha D_0}{3}\right)^2
+\left(4-\frac{8\alpha D_0}{3}\right)L_0
\right]} .
\end{gathered}
}
```

This polynomial is not a new independent field equation for $`D`$;
it solves the independent $`L,N,e_\mu{}^a`$ equations together with the definition
of the composite $`D`$. Fluxes and the fermionic background vanish
on all branches; background conditions are not imposed on fluctuations.

<a id="9-susy-calculation-and-comparison-of-source-conventions"></a>

## SUSY calculation and comparison of source conventions

This section compares the gravitino transformation in
[Coomans–Özkan, arXiv:1210.4704v3](https://arxiv.org/pdf/1210.4704),,
with the current project conventions. The source input is the transformation
rule; the integrability and branch-selection calculation below follows
from this rule and the total background equations.

<a id="91-gravitino-transformation-and-common-conventions"></a>

### Gravitino transformation and common conventions

Source (2.4), PDF pp. 5–6:

```math
\boxed{
\delta\psi_\mu^i
=
\left(\partial_\mu+\frac12b_\mu
+\frac14\omega_\mu{}^{ab}\gamma_{ab}\right)\epsilon^i
-V_\mu^{ij}\epsilon_j
+i\gamma^{ab}T_{ab}\gamma_\mu\epsilon^i
-i\gamma_\mu\eta^i .
}
\tag{S1}
```

The source signature $`(-++++)`$, NW–SE contraction, and spinor flip signs
agree with [CONVENTIONS.md](../../../common/details/source_conventions.md). No extra $`1/2`$ is inserted
in the $`\gamma^{ab}T_{ab}`$ contraction. The $`-V_\mu^{ij}\epsilon_j`$ connection term is retained
with the same index order.

The apparently different spin-connection terms in source (2.8)
are converted using the project's antisymmetrization and
NW–SE-contracted rank-one flip rules as follows:

```math
\begin{aligned}
-\frac12\bar\psi^{[b}\gamma^{a]}\psi_\mu
&=+\frac12\bar\psi^{[a}\gamma^{b]}\psi_\mu,\\
-\frac14\bar\psi^b\gamma_\mu\psi^a
&=+\frac14\bar\psi^a\gamma_\mu\psi^b.
\end{aligned}
\tag{S2}
```

The dependent $`\omega_\mu{}^{ab}`$ used here therefore agrees with the project definition.
On the bosonic background these bilinears vanish, leaving the Levi-Civita
connection. Neither an on-shell gravitino rule in a different source gauge
nor a source background solution is imported here.

<a id="92-compensation-preserving-the-current-gauge-and-the-killing-equation"></a>

### Compensation preserving the current gauge and the Killing equation

Source (2.15), (5.2), and (4.10)–(4.13) of the local two-derivative file
give the same defining-vector normalization. Preserving the dilatino gauge
on the fluxless background requires:

```math
\begin{aligned}
0=\delta\psi^i\big|_0
&=-Y_0^{ij}\epsilon_j+\eta^i,\\
Y_0^{ij}&=-\frac{gL_0}{2\sqrt2}\delta^{ij},\\
\eta^i&=-\frac{gL_0}{2\sqrt2}\delta^{ij}\epsilon_j.
\end{aligned}
\tag{S3}
```

Here $`\psi^i`$ is the dilatino set to zero by gauge fixing.
The other compensating parameters in (4.14) of the local file vanish
on the background with zero fermions.

To keep the internal-index operation explicit, define

```math
J^i{}_j:=\delta^{ik}\epsilon_{jk},
\qquad
J=\begin{pmatrix}0&-1\\1&0\end{pmatrix},
\qquad
J^2=-\mathbf1
\tag{S4}
```

This matrix directly expresses the project rules $`\epsilon_{12}=\epsilon^{12}=1`$ and $`X_i=X^j\epsilon_{ji}`$.

(S1)–(S3) in the $`b_\mu=V_\mu^{ij}=T_{ab}=0`$ background representative:

```math
\begin{aligned}
\delta\psi_\mu^i\big|_0
&=\nabla_\mu\epsilon^i-i\gamma_\mu
 \left(-\frac{gL_0}{2\sqrt2}J^i{}_j\epsilon^j\right)\\
&=\nabla_\mu\epsilon^i
 +\frac{igL_0}{2\sqrt2}\gamma_\mu J^i{}_j\epsilon^j.
\end{aligned}
```

The gravitino Killing equation is therefore

```math
\boxed{
\mathcal K_\mu\epsilon=0,\qquad
\mathcal K_\mu:=\nabla_\mu
+\frac{igL_0}{2\sqrt2}\gamma_\mu J
}
\tag{S5}
```

Here $`\nabla_\mu=\partial_\mu+\omega_\mu{}^{ab}\gamma_{ab}/4`$ contains only the Levi-Civita spinor connection
in this bosonic representative.

<a id="93-independent-integrability-calculation"></a>

### Independent integrability calculation

For this operation only, write $`M:=igL_0J/(2\sqrt2)`$.
The Clifford and internal-index algebras are independent:

```math
[M,\gamma_\mu]=0,\qquad
M^2
=\left(\frac{igL_0}{2\sqrt2}\right)^2J^2
=\frac{g^2L_0^2}{8}\mathbf1.
```

Under $`\partial_\mu L_0=0`$ and $`\nabla_\mu\gamma_\nu=0`$:

```math
\begin{aligned}
[\mathcal K_\mu,\mathcal K_\nu]\epsilon
&=\left(
 \frac14R_{\mu\nu}{}^{ab}\gamma_{ab}
 +M^2[\gamma_\mu,\gamma_\nu]
 \right)\epsilon,\\
R_{\mu\nu}{}^{ab}
&=\frac{R_0}{20}
 (e_\mu{}^ae_\nu{}^b-e_\nu{}^ae_\mu{}^b),\\
\frac14R_{\mu\nu}{}^{ab}\gamma_{ab}
&=\frac{R_0}{40}\gamma_{\mu\nu},\\
M^2[\gamma_\mu,\gamma_\nu]
&=\frac{g^2L_0^2}{8}\,2\gamma_{\mu\nu}.
\end{aligned}
```

Removing the temporary $`M`$ gives:

```math
\boxed{
[\mathcal K_\mu,\mathcal K_\nu]\epsilon
=\frac{R_0+10g^2L_0^2}{40}\gamma_{\mu\nu}\epsilon .
}
\tag{S6}
```

In an orthonormal frame with the project signature,

```math
(\gamma_{01})^2
=\gamma_0\gamma_1\gamma_0\gamma_1
=-\gamma_0^2\gamma_1^2
=-\eta_{00}\eta_{11}\mathbf1
=\mathbf1 .
```

Thus, for any nonzero Killing spinor, (S6) requires

```math
\boxed{R_0=-10g^2L_0^2}
\tag{S7}
```

When the coefficient is nonzero, a spinor projection cannot restore
partial SUSY.

<a id="94-compensator-fermion-and-branch-selection-using-the-total-equations"></a>

### Compensator fermion and branch selection using the total equations

In the selected class, the transformation in Section 8 of
[CONVENTIONS.md](../../../common/details/source_conventions.md) becomes

```math
\delta\varphi^i\big|_0
=\frac{N_0}{2}\epsilon^i+3L_0^{ij}\eta_j
```

The NW–SE lowering sign is explicitly:

```math
\begin{aligned}
\eta_j
&=\eta^k\epsilon_{kj}
=-\frac{gL_0}{2\sqrt2}
 \delta^{k\ell}\epsilon_\ell\epsilon_{kj}\\
&=+\frac{gL_0}{2\sqrt2}\delta_{jm}\epsilon^m,\\
3L_0^{ij}\eta_j
&=3\frac{L_0}{\sqrt2}\delta^{ij}
 \frac{gL_0}{2\sqrt2}\delta_{jm}\epsilon^m
=\frac{3gL_0^2}{4}\epsilon^i.
\end{aligned}
```

Therefore,

```math
\boxed{
\delta\varphi^i\big|_0
=\left(\frac{N_0}{2}+\frac{3gL_0^2}{4}\right)\epsilon^i,
\qquad
N_0=-\frac32gL_0^2
}
\tag{S8}
```

This is necessary. Substituting (S7)–(S8) into the definition
of the dependent $`D`$ gives:

```math
\begin{aligned}
D_0
&=-\frac{R_0}{32}+\frac{gN_0}{4}
  +\frac{g^2L_0^2}{16}\\
&=\left(\frac{10}{32}-\frac38+\frac1{16}\right)g^2L_0^2
=0.
\end{aligned}
\tag{S9}
```

This introduces no new independent $`D`$ equation. Next, the independent
$`N`$ equation of the total theory is:

```math
\begin{aligned}
0=\mathcal E_N
&=-\frac{4N_0}{L_0}-2g(L_0+2)
  +\frac{32\alpha g}{3}D_0\\
&=6gL_0-2gL_0-4g
=4g(L_0-1).
\end{aligned}
```

Under $`g\neq0`$, the result is:

```math
\boxed{
L_0=1,\qquad N_0=-\frac{3g}{2},\qquad D_0=0,\qquad
R_0=-10g^2,\qquad \ell^2=\frac2{g^2}.
}
\tag{S10}
```

Here $`L_0=1`$ follows from the equations; it is not a choice of units
or a new gauge. Direct back-substitution of these background values
into the original total equations gives:

```math
\begin{aligned}
D_0&=\frac{10g^2}{32}-\frac{3g^2}{8}+\frac{g^2}{16}=0,\\
\mathcal E_N&=6g-6g=0,\\
\mathcal E_L
&=\left(-10+\frac92+3+4-\frac32\right)g^2=0,\\
F_0&=-4g^2,\qquad F_{R,0}=1,\\
\mathcal E_{\rm met}
&=\frac{-10g^2}{5}-\frac12(-4g^2)=0.
\end{aligned}
\tag{S11}
```

The vanishing of the other independent-field equations in this class
is shown in Section 2. Bosonic SUSY transformations vanish on the
zero-fermion background. For the dependent spinor, the transformation
in source (2.4) on the same background also gives

```math
\delta\chi^i\big|_0=\frac14D_0\epsilon^i=0
```

This last equality checks composite consistency;
$`\chi`$ is not counted as a new independent field.

Since (S7)–(S10) are necessary for any candidate with a nonzero preserved
SUSY parameter, (S10) is the unique supersymmetric solution of the selected
fluxless maximally symmetric AdS class. The distinct additional AdS
solutions in Section 5 preserve no supersymmetry.

<a id="95-local-and-global-killing-spinor-counts"></a>

### Local and global Killing-spinor counts

On the selected branch:

```math
\boxed{
\mathcal K_\mu
=\nabla_\mu+\frac{ig}{2\sqrt2}\gamma_\mu J,\qquad
[\mathcal K_\mu,\mathcal K_\nu]=0 .
}
\tag{S12}
```

A five-dimensional Dirac spinor has four complex components; a doublet
has eight. The symplectic–Majorana condition reduces these to eight real
components. The connection in (S12), inherited from the source
symplectic–Majorana transformation, preserves this reality condition.
On the selected branch, (S8) and (S6) impose no additional algebraic
spinor projection. For a flat Killing connection, eight real initial
components at one point determine eight independent local parallel sections.

The global count applies to the universal cover with unwrapped time
and no quotient:

```math
\begin{gathered}
ds^2=-\left(1+\frac{r^2}{\ell^2}\right)d\tau^2
+\frac{dr^2}{1+r^2/\ell^2}+r^2d\Omega_3^2,\\
\tau\in\mathbb R,\qquad r\ge0,\qquad \ell^2=\frac2{g^2},\\
\widetilde{\mathrm{AdS}}_5\simeq\mathbb R\times\mathbb R^4.
\end{gathered}
```

Here $`d\Omega_3^2`$ is the unit three-sphere metric; the physical curvature scale
$`\ell`$ is not fixed. This space is simply connected. On the background
with zero internal connection, parallel transport of the flat $`\mathcal K`$
connection is path-independent; local solutions extend globally:

```math
\boxed{
n_{\rm SUSY}^{\rm local}=n_{\rm SUSY}^{\rm global}=8,
\qquad
\alpha,g\in\mathbb R,\quad \alpha\neq0,\quad g\neq0.
}
\tag{S13}
```

At the branch merger $`\alpha g^2=-2`$ derived from the equations in Section 6.1,
(S12) and the spinor count remain unchanged.

This is the background Killing-spinor count. For the global boundary
conditions of the fluctuations to preserve the same eight supersymmetries,
one must additionally require

```math
\boxed{
\delta_\epsilon\mathcal D_{\partial}
\subseteq\mathcal D_{\partial}
}
\tag{S14}
```

Here $`\mathcal D_{\partial}`$ is the space of admissible boundary data for all bosonic
and fermionic fluctuations. This boundary test is separate from the
background Killing-spinor calculation. A global supersymmetric spectrum
uses field-specific falloffs in a boundary domain preserved by these transformations.

<a id="10-branch-selected-for-the-spectrum-and-scope-of-the-selection"></a>

## Branch selected for the spectrum and scope of the selection

The spectrum calculation uses the $`t=0`$ branch of Section 4, namely (S10):

```math
\boxed{
\begin{gathered}
L_0=1,\qquad N_0=-\frac{3g}{2},\qquad D_0=0,\qquad
R_{\mu\nu,0}=-2g^2g_{\mu\nu,0},\qquad
\ell^2=\frac2{g^2},\\
G_0=H_0=dE_{3,0}=dV_0=0,\qquad V'_{\mu,0}{}^{ij}=0,\qquad
\psi_{\mu,0}^i=\varphi_0^i=0,\\
n_{\rm SUSY}=8
\quad\text{(on the universal cover without a quotient).}
\end{gathered}
}
```

This branch is selected because it satisfies the total background equations
for all real $`\alpha\neq0`$, $`g\neq0`$, is regular on the $`L_0\neq0`$ patch, and is the
unique supersymmetric branch in the selected AdS class. Additional real
AdS branches remain as solutions in Sections 5–7; they are not selected
as backgrounds for this spectrum calculation.

$`\alpha`$ remains a generic exact nonperturbative constant. Independence
of the background values from $`\alpha`$ on this branch does not imply
independence of the full fluctuation operator or spectrum from $`\alpha`$.
No sign interval or sample value is chosen for $`\alpha g^2`$; special parameter
conditions arising from the equations are retained in the relevant calculation.

Fluctuations of all independent bosonic and fermionic fields are retained.
Background values of $`D_0=T_0=\chi_0=0`$ do not require their definition-derived
fluctuations to vanish. The auxiliary-field classification of the
two-derivative theory is not transferred to the total theory.
Preserving eight supersymmetries alone proves neither stability
nor positivity of norms in the full higher-derivative spectrum.
