# LOG: quadratic action on AdS5

[Notation dictionary](../notation.md).

[Reading guide](README.md). The equation labels and local symbols below follow the action conventions specified for this theory.

<a id="8-quadratic-action-with-all-independent-fluctuations"></a>

## Quadratic action with all independent fluctuations

This chapter consolidates the quadratic action and its recorded checks, using the fixed action, conventions, inventory, and selected background above.

Unless stated otherwise, equalities hold for the local bulk action modulo displayed total derivatives, denoted $`\simeq_\partial`$. The fixed-source reflecting prescription remains in force; equality of bulk equations does not imply equality of boundary actions.

The fermionic action is an explicit quadratic form built from specified linear differential maps. Completed checks cover the bosonic equations, implicit and explicit fermion coefficients, diagonal spinor block, and local SUSY Noether cancellation.

## Action, branch, and expansion order

```math
S=\frac1{2\kappa_5^2}\int d^5x\,e\,
\bigl(\ell_{2\partial}+\alpha\ell_{\log}\bigr),
\qquad \alpha\ne0,\quad g\ne0.
\tag{Q1}
```

Use the selected-branch relations

```math
\boxed{
L_0=\frac2{1+\sqrt{1-\alpha g^2/2}},\qquad
N_0=-\frac32gL_0^2,\qquad
k=-\ell^{-2}=-\frac12g^2L_0^2,
\qquad \alpha g^2\le2
}
\tag{Q2}
```

and their algebraic equation

```math
\mathcal B:=\alpha g^2L_0^2-8L_0+8=0
\tag{Q3}
```

with $`L_0>0,g\ne0`$. Q2 constrains background values, not fluctuations: $`l,n`$ remain independent.

```math
\begin{gathered}
\bar R_{\mu\nu\rho\sigma}
=k(\bar g_{\mu\rho}\bar g_{\nu\sigma}
-\bar g_{\mu\sigma}\bar g_{\nu\rho}),\qquad
\bar R_{\mu\nu}=4k\bar g_{\mu\nu},\quad \bar R=20k,\\
\bar G=\bar H_3=\bar P=\bar{\mathcal F}^{ij}=0,
\qquad \bar V^{\prime ij}=0,
\qquad \bar\psi_\mu^i=\bar\varphi^i=0,\qquad
L_0^{ij}=\frac{L_0}{\sqrt2}\delta^{ij}.
\end{gathered}
\tag{Q4}
```

No additional gauge is imposed on $`\bar C,\bar V,\bar B,\bar E_3`$. Their strengths vanish as in Q4. The derivative $`\bar\nabla`$ contains Levi–Civita and the flat background internal connection, not full supercovariant $`\mathcal D`$.

Introduce one even fluctuation parameter $`\varepsilon`$:

```math
\begin{aligned}
g_{\mu\nu}&=\bar g_{\mu\nu}+\varepsilon h_{\mu\nu},&
L&=L_0+\varepsilon l,& N&=N_0+\varepsilon n,\\
C&=\bar C+\varepsilon c,&B_2&=\bar B_2+\varepsilon b_2,&
E_3&=\bar E_3+\varepsilon e_3,\\
V_\mu&=\bar V_\mu+\varepsilon v_\mu,&
V_\mu^{\prime ij}&=\varepsilon w_\mu^{ij},&\delta_{ij}w_\mu^{ij}&=0,\\
\psi_\mu^i&=\varepsilon\Psi_\mu^i,&
\varphi^i&=\varepsilon\zeta^i
\end{aligned}
\tag{Q5}
```

Keep the existing source gauges $`\sigma=1,\psi^i=0,b_\mu=0,L^{ij}=L\delta^{ij}/\sqrt2`$. The defining dilatino condition does not set the gravitino or its covariant dilatino descendants to zero.

```math
S=\bar S+\varepsilon S^{(1)}+\varepsilon^2 S^{(2)}+O(\varepsilon^3),
\qquad S^{(2)}=\frac12\left.\frac{d^2S}{d\varepsilon^2}\right|_0.
\tag{Q6}
```

No expansion in $`\alpha`$ is made. Fermion parity splits the quadratic action into bosonic and two-fermion pieces, with no single-boson/single-fermion term. Two-fermion action order suffices for both classical linear sectors.

## Determinant, inverse metric, and curvatures

Raise fluctuation indices with $`\bar g`$, and put $`h=\bar g^{\mu\nu}h_{\mu\nu}`$:

```math
\begin{aligned}
g^{\mu\nu}&=\bar g^{\mu\nu}-\varepsilon h^{\mu\nu}
+\varepsilon^2h^\mu{}_\rho h^{\rho\nu}+O(\varepsilon^3),\\
\frac e{\bar e}&=1+\frac\varepsilon2h
+\varepsilon^2\left(\frac18h^2-\frac14h_{\mu\nu}h^{\mu\nu}\right)
+O(\varepsilon^3).
\end{aligned}
\tag{Q7}
```

The antisymmetric vielbein fluctuation $`a_{ab}=-a_{ba}`$ can be retained by applying a local Lorentz matrix to the metric square-root representative:

```math
e_\mu{}^a
=\bar e_\mu{}^b
\left[\mathbf1+\frac\varepsilon2h-\frac{\varepsilon^2}8h^2\right]_b{}^c
(e^{\varepsilon a})_c{}^a+O(\varepsilon^3).
\tag{Q8}
```

This does not impose $`a_{ab}=0`$. The Lorentz-invariant density is independent of this direction; its Euler equation is the Lorentz Noether identity.

The connection and Ricci expansions are

```math
\begin{aligned}
\Gamma^\rho{}_{\mu\nu}-\bar\Gamma^\rho{}_{\mu\nu}
&=\varepsilon A^\rho{}_{\mu\nu}+\varepsilon^2B^\rho{}_{\mu\nu}+O(\varepsilon^3),\\
A^\rho{}_{\mu\nu}
&=\frac12(\bar\nabla_\mu h^\rho{}_\nu+\bar\nabla_\nu h^\rho{}_\mu
-\bar\nabla^\rho h_{\mu\nu}),\qquad
B^\rho{}_{\mu\nu}=-h^\rho{}_\sigma A^\sigma{}_{\mu\nu},\\
X_{\mu\nu}&=\bar\nabla_\rho A^\rho{}_{\mu\nu}
-\bar\nabla_\nu A^\rho{}_{\mu\rho},\\
Y_{\mu\nu}&=\bar\nabla_\rho B^\rho{}_{\mu\nu}
-\bar\nabla_\nu B^\rho{}_{\mu\rho}
+A^\rho{}_{\rho\lambda}A^\lambda{}_{\mu\nu}
-A^\rho{}_{\nu\lambda}A^\lambda{}_{\mu\rho},\\
R_{\mu\nu}&=4k\bar g_{\mu\nu}+\varepsilon X_{\mu\nu}
+\varepsilon^2Y_{\mu\nu}+O(\varepsilon^3)
\end{aligned}
\tag{Q9}
```

Define the linear and quadratic geometric expressions

```math
\begin{aligned}
\mathscr R_{\mu\nu}&:=X_{\mu\nu}-4kh_{\mu\nu},\\
r&:=\bar g^{\mu\nu}X_{\mu\nu}-4kh
=\bar\nabla_\mu\bar\nabla_\nu h^{\mu\nu}-\bar\Box h-4kh,\\
s&:=\bar g^{\mu\nu}Y_{\mu\nu}-h^{\mu\nu}X_{\mu\nu}
+4kh_{\mu\nu}h^{\mu\nu},\\
\mathscr K[h]&:=s+\frac12hr+kh^2-2kh_{\mu\nu}h^{\mu\nu}.
\end{aligned}
\tag{Q10}
```

Including inverse-metric contractions gives

```math
\begin{aligned}
R&=20k+\varepsilon r+\varepsilon^2s+O(\varepsilon^3),\\
R_{\mu\nu}R^{\mu\nu}
&=80k^2+8\varepsilon kr
+\varepsilon^2(\mathscr R_{\mu\nu}\mathscr R^{\mu\nu}+8ks)
+O(\varepsilon^3),\\
R^2&=400k^2+40\varepsilon kr
+\varepsilon^2(r^2+40ks)+O(\varepsilon^3),\\
\left[\frac e{\bar e}\left(-\frac16R_{\mu\nu}R^{\mu\nu}
+\frac1{24}R^2\right)\right]_{\varepsilon^2}
&=-\frac16\mathscr R_{\mu\nu}\mathscr R^{\mu\nu}
+\frac1{24}r^2+\frac k3\left(s+\frac12hr\right)
+\frac{10k^2}3\left(\frac18h^2-\frac14h_{\mu\nu}h^{\mu\nu}\right).
\end{aligned}
\tag{Q11}
```

## Forms, internal connections, and bosonic composites

```math
\begin{aligned}
\mathcal G&:=dc,\\
\mathcal H&:=db_2+\frac12\bar C\wedge dc+\frac g2e_3,\\
p^\mu&:=-\frac1{12}\bar\varepsilon^{\mu\nu\rho\sigma\lambda}
\partial_\nu e_{\rho\sigma\lambda},\\
\mathcal F_{\mu\nu}^{ij}
&:=2\bar D_{[\mu}\left(\frac12\delta^{ij}v_{\nu]}+w_{\nu]}^{ij}\right),\\
j^a&:=\bar\nabla_b\mathcal G^{ab},\qquad
q_{ab}:=\bar\nabla^c\mathcal H_{cab}.
\end{aligned}
\tag{Q12}
```

The quantity $`\mathcal H`$ is a three-form; $`q_{ab}`$ is its divergence, not an independent dual field. Likewise $`p`$ is derived from $`e_3`$.

```math
\begin{gathered}
d\mathcal G=0,\qquad d\mathcal H=\frac g2de_3,
\qquad \bar\nabla_\mu p^\mu=0,\\
H=\varepsilon\mathcal H+\frac{\varepsilon^2}2c\wedge dc+O(\varepsilon^3),
\qquad
P^\mu=\varepsilon p^\mu-\frac{\varepsilon^2}2h\,p^\mu+O(\varepsilon^3).
\end{gathered}
\tag{Q13}
```

The last equality follows from $`P^\mu=-e^{-1}\epsilon^{\mu\nu\rho\sigma\lambda}\partial_\nu E_{\rho\sigma\lambda}/12`$. Thus $`eP^\mu`$ is metric independent; it produces no artificial $`h\,p\cdot\bar C`$ term.

For an intermediate check only, set $`U_{ab}=-\varepsilon_{abcde}H^{cde}/12`$:

```math
U^2=-\frac1{12}H_3^2,\qquad
G\cdot U=-\frac1{12}G^{ab}\varepsilon_{abcde}H^{cde},\qquad
(3\nabla_{[a}U_{bc]})^2=-\frac34(\nabla^aH_{abc})^2.
\tag{Q14}
```

The final equality is an algebraic epsilon contraction converting $`2(3\nabla_{[a}U_{bc]})^2/9`$ to $`-(\nabla^aH_{abc})^2/6`$. The final action does not use $`U`$.

The required linear dependent bosonic composites are

```math
\begin{aligned}
T_{ab}^{(1)}&=\frac18\mathcal G_{ab}
+\frac1{48}\bar\varepsilon_{abcde}\mathcal H^{cde},\\
D^{(1)}&=-\frac1{32}r+\frac g4n+\frac{g^2L_0}8l,\\
Y^{ij}_{\rm defining}&=-\frac g2\left(L_0^{ij}
+\frac\varepsilon{\sqrt2}l\delta^{ij}\right),\\
\bar f_{ab}&=-\frac k4\eta_{ab},\qquad
\overline{\mathcal D_a\mathcal D_b\sigma}=-\frac k2\eta_{ab},\qquad
\overline{\Box^c\sigma}=-\frac{5k}2,\\
\overline{\Box^cL^{ij}}&=-\frac{15k}2L_0^{ij},\qquad
\overline{\Box^cN}=8N_0\bar f_a{}^a=-10kN_0.
\end{aligned}
\tag{Q15}
```

Here $`\bar D=-20k/32+gN_0/4+g^2L_0^2/16=0`$ and $`\bar T=0`$. Full second derivatives of constant compensators in Q15 are nevertheless nonzero.

## Bosonic quadratic density

Separate the zero-flux scalar/curvature density as

```math
\begin{aligned}
A(L,N)&:=L+\alpha\left(\frac g6N-\frac{g^2}{12}L^2\right),\\
V(L,N)&:=-\frac{2N^2}L-2gLN-4gN-\frac12g^2L^3+2g^2L^2\\
&\quad+\alpha\left(-\frac{g^2}6N^2+\frac{2g^3}3NL^2
+\frac{5g^4}{24}L^4\right),\\
\ell_{\mathrm{grav,scal}}
&=A(L,N)R+\alpha\left(-\frac16R_{\mu\nu}R^{\mu\nu}+\frac1{24}R^2\right)
+\left(\frac1L-\frac{\alpha g^2}4\right)(\partial L)^2+V(L,N)
\end{aligned}
\tag{Q16}
```

The $`k/3`$ term in Q11 implies

```math
\begin{aligned}
A_0+\frac{\alpha k}3
&=L_0+\alpha\left(-\frac{g^2L_0^2}4-\frac{g^2L_0^2}{12}
-\frac{g^2L_0^2}6\right)
=L_0-\frac{\alpha g^2L_0^2}2=:B_0,\\
a_1:=\delta A
&=\left(1-\frac{\alpha g^2L_0}6\right)l+\frac{\alpha g}6n,\\
\bar\ell-8kB_0&=g^2L_0^2\mathcal B=0.
\end{aligned}
\tag{Q17}
```

The final relation turns the second determinant coefficient into $`B_0(kh^2-2kh_{\mu\nu}h^{\mu\nu})`$. Differentiate with $`L,N`$ independent, then impose Q2 to obtain the scalar Taylor coefficients:

```math
\begin{aligned}
\frac12\left.\partial_L^2(AR+V)\right|_0
&=\frac12\left[-\frac{4N_0^2}{L_0^3}-3g^2L_0+4g^2
+\alpha\left(-\frac{g^2\bar R}6+\frac{4g^3N_0}3
+\frac{5g^4L_0^2}2\right)\right]\\
&=2g^2-6g^2L_0+\frac{13\alpha g^4L_0^2}{12},\\
\left.\partial_L\partial_N(AR+V)\right|_0
&=\frac{4N_0}{L_0^2}-2g+\frac{4\alpha g^3L_0}3
=-8g+\frac{4\alpha g^3L_0}3,\\
\frac12\left.\partial_N^2(AR+V)\right|_0
&=-\frac2{L_0}-\frac{\alpha g^2}6
\end{aligned}
\tag{Q18}
```

The LOG flux coefficients, using temporary $`U`$, are

```math
\begin{aligned}
[G^2]:\quad \frac{2k}3-\frac{gN_0}3+\frac{g^2L_0^2}{24}
&=\frac{5g^2L_0^2}{24},\\
[G\cdot U]:\quad -\frac{16k}3+\frac{20k}3
-\frac{2gN_0}3-\frac{g^2L_0^2}6
&=\frac{g^2L_0^2}6,\\
[U^2]:\quad -\frac{20k}3+2gN_0-g^2L_0^2
&=-\frac{2g^2L_0^2}3.
\end{aligned}
\tag{Q19}
```

The second line becomes $`-g^2L_0^2G^{ab}\varepsilon_{abcde}H^{cde}/72`$, and the third contributes $`g^2L_0^2H_3^2/18`$. Internal-curvature and derivative terms are already quadratic by Q12–Q14.

The full bosonic result is

```math
\boxed{\begin{aligned}
\ell_B^{(2)}={}&
\left(L_0-\frac{\alpha g^2L_0^2}2\right)\mathscr K[h]
+\alpha\left(-\frac16\mathscr R_{\mu\nu}\mathscr R^{\mu\nu}
+\frac1{24}r^2\right)\\
&+\left[\left(1-\frac{\alpha g^2L_0}6\right)l
+\frac{\alpha g}6n\right]r
+\left(\frac1{L_0}-\frac{\alpha g^2}4\right)(\bar\nabla l)^2\\
&+\left(2g^2-6g^2L_0+\frac{13\alpha g^4L_0^2}{12}\right)l^2
+\left(-8g+\frac{4\alpha g^3L_0}3\right)ln
-\left(\frac2{L_0}+\frac{\alpha g^2}6\right)n^2\\
&+\left(-\frac{L_0}2+\frac{5\alpha g^2L_0^2}{24}\right)
\mathcal G_{ab}\mathcal G^{ab}
+\left(-\frac{L_0}3+\frac{\alpha g^2L_0^2}{18}\right)
\mathcal H_{abc}\mathcal H^{abc}\\
&-\frac{\alpha g^2L_0^2}{72}\mathcal G^{ab}
\bar\varepsilon_{abcde}\mathcal H^{cde}
+\frac\alpha6\mathcal F_{ab}^{ij}\mathcal F^{ab}_{ij}
+\frac{\alpha g}6L_{0ij}\mathcal F_{ab}^{ij}\mathcal G^{ab}\\
&-\frac{\alpha g}{18}L_{0ij}\mathcal F^{abij}
\bar\varepsilon_{abcde}\mathcal H^{cde}
+\left(2L_0-\frac{\alpha g^2L_0^2}2\right)w_\mu^{ij}w^\mu_{ij}\\
&+\left(-\frac2{L_0}+\frac{\alpha g^2}3\right)p_\mu p^\mu
-2\sqrt2p^\mu v_\mu-4gp^\mu c_\mu
-\frac\alpha6(j_aj^a+q_{ab}q^{ab})
+\frac{\alpha g}3p_aj^a .
\end{aligned}}
\tag{Q20}
```

With $`d\bar C=0`$ and flat $`\bar V`$, the term $`\bar C\wedge\mathop{\mathrm{tr}}\nolimits(\mathcal F\wedge\mathcal F)`$ is locally a total derivative. It has no bulk Euler contribution and is separated into the boundary representative. This is not a choice $`\bar C=0`$.

## Spinor conventions and linear dependent maps

```math
\begin{gathered}
\eta=(-,+,+,+,+),\qquad \gamma^{abcde}=i\varepsilon^{abcde},\\
X_i=X^j\epsilon_{ji},\quad X^i=\epsilon^{ij}X_j,\quad
\epsilon_{12}=\epsilon^{12}=1,\quad
\bar X\Gamma Y=\bar X^i\Gamma Y_i,\\
\bar X^i\gamma_{(n)}Y^j=t_n\bar Y^j\gamma_{(n)}X^i,\qquad
t_n=(+,+,-,-,+,+),\\
\bar X\gamma_{(n)}Y=-t_n\bar Y\gamma_{(n)}X,\qquad
\overline{iu}=i\bar u.
\end{gathered}
\tag{Q21}
```

The bar is linear; the formal adjoint below is not Hermitian conjugation. Define the internal operator

```math
(Mu)^i:=L_0^{ij}u_j,
\qquad M^2=-\frac{L_0^2}2\mathbf1,\qquad \bar\nabla M=0,
\qquad M^\sharp=-M
\tag{Q22}
```

so that

```math
L_{0ij}\bar u^i\Gamma v^j=-\bar u\Gamma Mv,
\qquad
L_0^{ij}\bar u_i\Gamma v_j=L_{0ij}\bar u^i\Gamma v^j
\tag{Q23}
```

The sign follows from $`\epsilon_{ij}=-\epsilon_{ji}`$. The matrix $`M`$ is not a new field.

The dependent $`S`$ connection and $`Q`$ curvature are

```math
\begin{aligned}
Q'_{ab}&:=2\bar\nabla_{[a}\Psi_{b]},\\
\Phi_a&:=\frac i3\gamma^bQ'_{ab}
-\frac i{24}\gamma_a\gamma^{bc}Q'_{bc},\\
Q_{ab}&:=Q'_{ab}-2i\gamma_{[a}\Phi_{b]},\qquad
\gamma^aQ_{ab}=0,\\
s_a&:=-\frac g2M\Psi_a-\Phi_a,
\qquad S:=\gamma^as_a,\qquad
\chi_1:=\frac i8S+\frac g8\zeta,\\
\upsilon_a&:=\bar\nabla_a\zeta-\frac{N_0}2\Psi_a-3M\Phi_a
=\bar\nabla_a\zeta+3Ms_a,\\
t_{ab}&:=\bar\nabla_as_b-\frac{ik}4\gamma_b\Psi_a
-\frac{ig}2M\gamma_b\Phi_a
=\bar\nabla_as_b+\frac{ig}2M\gamma_bs_a,\\
u&:=\bar\nabla^a\upsilon_a+\frac{iN_0}2S-\frac{35k}4\zeta.
\end{aligned}
\tag{Q24}
```

These maps define the linear parts of $`\phi_a`$, $`\widehat R_{ab}(Q)`$, $`\mathcal D_a\psi_{\mathrm{defining}}`$, $`\chi`$, $`\mathcal D_a\varphi`$, $`\mathcal D_a\mathcal D_b\psi_{\mathrm{defining}}`$, and $`\Box^c\varphi`$. Only Q2 and $`M^2=-L_0^2/2`$ enter the second equalities. The indices of $`t_{ab}`$ are ordered; symmetry is not assumed.

For the gamma-trace check put $`A_b=\gamma^aQ'_{ab}`$, $`B=\gamma^{ab}Q'_{ab}`$:

```math
\Phi_b=-\frac i3A_b-\frac i{24}\gamma_bB,\qquad
\gamma^b\Phi_b=\frac i8B,\qquad
\gamma^aQ_{ab}=A_b-3i\Phi_b-i\gamma_b\gamma^a\Phi_a=0.
\tag{Q25}
```

Every derivative in Q24 is an ordinary background derivative. No direct integration by parts of full $`\mathcal D`$ is assumed.

## Implicit two-fermion terms: contorsion and scalar boxes

Define gravitino contorsion and the reduced primed Ricci contribution by

```math
\begin{aligned}
K_\mu{}^{ab}
&:=\frac12\bar\Psi^{[a}\gamma^{b]}\Psi_\mu
+\frac14\bar\Psi^a\gamma_\mu\Psi^b,\\
J_F&:=2\bar\nabla_aK_b{}^{ab}+i\bar\Phi_a\gamma^{ab}\Psi_b,\\
\left.\widehat R'(M)\right|_{F^2}&=J_F-16\bar\Psi_a\gamma^a\chi_1,\\
\left.f_a{}^a\right|_{F^2}&=-\frac1{16}J_F+\bar\Psi_a\gamma^a\chi_1
\end{aligned}
\tag{Q26}
```

Q25 removes the $`Q`$-curvature Ricci traces. The explicit $`+8\bar\psi e\gamma\chi`$ term has Ricci trace $`-16\bar\Psi\not\!\chi_1`$. Hence

```math
\begin{aligned}
X_F:=\left.\Box^c\sigma\right|_{F^2}
&=2\left.f_a{}^a\right|_{F^2}
-\frac i2\bar\Psi_as^a-2\bar\Psi_a\gamma^a\chi_1\\
&=-\frac18J_F-\frac i2\bar\Psi_as^a,\\
Y_F:=\left.L_{0ij}\Box^cL^{ij}\right|_{F^2}
&=-\frac{3L_0^2}8J_F
-iL_{0ij}\bar\nabla_a(\bar\Psi^{ai}\zeta^j)
-iL_{0ij}\bar\Psi^{ai}\upsilon_a^j
+L_{0ij}\bar\zeta^i\gamma^a\Phi_a^j.
\end{aligned}
\tag{Q27}
```

In $`Y_F`$, the explicit $`\chi_1`$ terms of $`6L_0^2f_a{}^a`$ and $`-6L_0^2\bar\Psi_a\gamma^a\chi_1`$ cancel. The term $`-i\bar\Psi_a^{(i}\zeta^{j)}`$ in $`\mathcal D_aL^{ij}`$ produces both a divergence and $`\bar\Psi\upsilon`$.

The bilinear first derivative and linear maps required for the $`N`$ box are

```math
\begin{aligned}
z_a&:=-\frac12\bar\Psi_a\not\!\upsilon
-4iL_{0ij}\bar\Psi_a^i\chi_1^j-\frac{3i}2\bar\Phi_a\zeta,\\
\mathcal A_a&:=\frac12\bar\nabla_a\not\!\upsilon
-4iM\bar\nabla_a\chi_1+\frac{5iN_0}4s_a-\frac{3k}8\gamma_a\zeta,\\
\mathcal B_a&:=\frac{3i}2\upsilon_a
+\frac i2\gamma_a\not\!\upsilon+4\gamma_aM\chi_1,\\
Z_F:=\left.\Box^cN\right|_{F^2}
&=-\frac{N_0}2J_F+\bar\nabla^az_a
-\bar\Psi^a\mathcal A_a-\bar\Phi^a\mathcal B_a
\end{aligned}
\tag{Q28}
```

where $`\not\!\upsilon=\gamma^a\upsilon_a`$. The outer derivative uses descendant transformations

```math
\begin{aligned}
\left.\delta_Q(\mathcal D_aN)\right|_{F^1}
&=\bar\epsilon(\mathcal A_a+8N_0\gamma_a\chi_1),\\
\left.\delta_S(\mathcal D_aN)\right|_{F^1}
&=\bar\eta\mathcal B_a,\qquad
\left.\delta_K(\mathcal D_aN)\right|_{F^0}=-8N_0\Lambda_{Ka}
\end{aligned}
\tag{Q29}
```

Consequently the $`+8N_0\bar\Psi\gamma\chi_1`$ from the $`K`$ connection cancels the Q-covariantization contribution. The remaining coefficient of $`J_F`$ in $`Z_F`$ is $`8N_0(-1/16)=-N_0/2`$. Also $`5iN_0s_a/4=-5iN_0\Phi_a/4-15ikM\Psi_a/8`$.

The hatted-flux bilinears are retained as

```math
\begin{aligned}
\left.\widehat G_{\mu\nu}\right|_{F^2}
&=\frac i2\bar\Psi_{[\mu}\Psi_{\nu]},\\
\left.\widehat H_{\mu\nu\rho}\right|_{F^2}
&=-\frac34\bar\Psi_{[\mu}\gamma_\nu\Psi_{\rho]},\\
\left.E^a\right|_{F^2}
&=-\frac i2\bar\Psi_b\gamma^{ba}\zeta
-\frac14L_{0ij}\bar\Psi_b^i\gamma^{abc}\Psi_c^j,\\
\left.\widehat R_{\mu\nu}^{ij}(V)\right|_{F^2}
&=-3i\bar\Phi_{[\mu}^{(i}\Psi_{\nu]}^{j)}
-8\bar\Psi_{[\mu}^{(i}\gamma_{\nu]}\chi_1^{j)}.
\end{aligned}
\tag{Q30}
```

By Q4 they enter products of zero-background fluxes only at cubic fluctuation order. The box/curvature terms Q26–Q29 multiply nonzero scalar backgrounds and survive quadratically. This order argument does not identify hatted and ordinary objects beforehand.

## Fermionic quadratic density

The linear map spinor and scalar background coefficient are

```math
\lambda:=-\frac{2i}{L_0}\not\!\upsilon
-\frac{16}{L_0}M\chi_1+\frac{2N_0}{L_0^3}M\zeta,
\qquad \rho_0:=\frac{2N_0}{L_0}+2g
\tag{Q31}
```

and the two-derivative density is

```math
\begin{aligned}
\ell_{2\partial,F}^{(2)}=-2\Big[&
\frac{Y_F}{L_0}+L_0X_F+\frac1{L_0}\bar\zeta\not\!\upsilon
-\frac{iN_0}{L_0^3}L_{0ij}\bar\zeta^i\zeta^j
+i\bar\lambda\zeta\\
&-\frac12L_{0ij}\bar\Psi_a^i\gamma^a\lambda^j
+\frac{\rho_0}2\bar\Psi_a\gamma^a\zeta
+\frac{i\rho_0}4L_{0ij}\bar\Psi_a^i\gamma^{ab}\Psi_b^j\Big]
\end{aligned}
\tag{Q32}
```

The $`J_F`$ coefficient is $`-2[-3L_0/8-L_0/8]=L_0`$, retaining the term $`iL_0\bar\Phi_a\gamma^{ab}\Psi_b`$ beyond contorsion.

The linear LOG spinor is

```math
\mathcal P:=-ig^2L_0^2S+g^3L_0^2\zeta
-2gM\gamma^{ab}t_{ab}-gMt^a{}_a
+2ig^2M\not\!\upsilon-gu
\tag{Q33}
```

and the explicit triplet bilinear is

```math
\mathcal T^{ij}:=-\frac{5i}6\bar s_a^{(i}\gamma^{ab}s_b^{j)}
+\frac{2i}3\bar s^{a(i}s_a^{j)}
-\frac{11g}3\bar\zeta^{(i}\gamma^as_a^{j)}
+\frac{17ig^2}6\bar\zeta^{(i}\zeta^{j)}
\tag{Q34}
```

The scalar polynomial $`\mathcal N`$ consists of rows 9–27 in Q37, but with pre-merger coefficients in rows 16, 17, and 22 equal to $`-ig/3,-10ig/3,-13g^2/12`$. These are the 19 surviving AL-NF2 bilinears; all other row coefficients are unchanged.

```math
\begin{aligned}
\ell_{\log,F}^{(2)}={}&
-\frac{g^2L_0^2}2X_F-\frac{g^2}2Y_F-gZ_F
+\mathcal N-\frac g2L_{0ij}\mathcal T^{ij}\\
&+\frac12\bar\Psi_a\gamma^a\mathcal P
-\frac{3ig^3L_0^2}8L_{0ij}\bar\Psi_a^i\gamma^{ab}\Psi_b^j.
\end{aligned}
\tag{Q35}
```

Each row below means coefficient times bilinear, with no additional overall $`1/2`$. The maps Q24 and Q28–Q33 express every slot in $`\Psi,\zeta`$.

### Ten two-derivative bilinears

| Row | Coefficient | Bilinear |
|---|---|---|
| 1 | $`iL_0`$ | $`\bar\Phi_a\gamma^{ab}\Psi_b`$ |
| 2 | $`iL_0`$ | $`\bar\Psi_as^a`$ |
| 3 | $`-2i/L_0`$ | $`\bar\Psi^aM\upsilon_a`$ |
| 4 | $`2/L_0`$ | $`\bar\zeta\gamma^aM\Phi_a`$ |
| 5 | $`-2/L_0`$ | $`\bar\zeta\gamma^a\upsilon_a`$ |
| 6 | $`-2iN_0/L_0^3`$ | $`\bar\zeta M\zeta`$ |
| 7 | $`-2i`$ | $`\bar\lambda\zeta`$ |
| 8 | $`-1`$ | $`\bar\Psi_a\gamma^aM\lambda`$ |
| 9 | $`-\rho_0`$ | $`\bar\Psi_a\gamma^a\zeta`$ |
| 10 | $`i\rho_0/2`$ | $`\bar\Psi_a\gamma^{ab}M\Psi_b`$ |

```math
\ell_{2\partial,F}^{(2)}\simeq_\partial
\sum_{r=1}^{10}c_r\bar A_r\Gamma_rB_r.
\tag{Q36}
```

### Twenty-eight LOG bilinears

| Row | Coefficient | Bilinear |
|---|---|---|
| 1 | $`-ig^2L_0^2/2`$ | $`\bar\Phi_a\gamma^{ab}\Psi_b`$ |
| 2 | $`ig^2L_0^2/4`$ | $`\bar\Psi_as^a`$ |
| 3 | $`-ig^2/2`$ | $`\bar\Psi^aM\upsilon_a`$ |
| 4 | $`g^2/2`$ | $`\bar\zeta\gamma^aM\Phi_a`$ |
| 5 | $`g`$ | $`\bar\Psi^a\mathcal A_a`$ |
| 6 | $`g`$ | $`\bar\Phi^a\mathcal B_a`$ |
| 7 | $`1/2`$ | $`\bar\Psi_a\gamma^a\mathcal P`$ |
| 8 | $`3ig^3L_0^2/8`$ | $`\bar\Psi_a\gamma^{ab}M\Psi_b`$ |
| 9 | $`-81i/256`$ | $`\overline{\bar\nabla^aQ_a{}^b}\,s_b`$ |
| 10 | $`111/512`$ | $`\bar\varepsilon_{abcde}\overline{\bar\nabla^aQ^{bc}}\gamma^ds^e`$ |
| 11 | $`-153ig/1024`$ | $`\bar\varepsilon_{abcde}\overline{\bar\nabla^aQ^{bc}}\gamma^{de}\zeta`$ |
| 12 | $`-i/12`$ | $`\bar\varepsilon_{abcde}\bar s^c\gamma^{ab}t^{de}`$ |
| 13 | $`5/6`$ | $`\bar s_a\gamma^at^b{}_b`$ |
| 14 | $`-1/6`$ | $`\bar s^b\gamma^at_{ab}`$ |
| 15 | $`-4/3`$ | $`\bar s^b\gamma^at_{ba}`$ |
| 16 | $`-3ig/4`$ | $`\bar s_a\gamma^{ab}Ms_b`$ |
| 17 | $`-3ig`$ | $`\bar s^aMs_a`$ |
| 18 | $`5ig/6`$ | $`\bar\upsilon^a\gamma_a{}^bs_b`$ |
| 19 | $`-13ig/6`$ | $`\bar\upsilon^as_a`$ |
| 20 | $`5ig/6`$ | $`\bar\zeta\gamma^{ab}t_{ab}`$ |
| 21 | $`-5ig/6`$ | $`\bar\zeta t^a{}_a`$ |
| 22 | $`-35g^2/12`$ | $`\bar\zeta\gamma^aMs_a`$ |
| 23 | $`g^2/6`$ | $`\bar\zeta\gamma^a\upsilon_a`$ |
| 24 | $`-355ig/2304`$ | $`\bar\varepsilon_{abcde}\bar Q^{ab}\gamma^{cd}Ms^e`$ |
| 25 | $`-ig/64`$ | $`\bar\varepsilon_{abcde}\bar Q^{ab}\gamma^{de}\upsilon^c`$ |
| 26 | $`ig/1024`$ | $`\bar Q^{ab}MQ_{ab}`$ |
| 27 | $`-g/2048`$ | $`\bar\varepsilon_{abcde}\bar Q^{ab}\gamma^eMQ^{cd}`$ |
| 28 | $`17ig^3/12`$ | $`\bar\zeta M\zeta`$ |

```math
\ell_{\log,F}^{(2)}\simeq_\partial
\sum_{r=1}^{28}d_r\bar A_r\Gamma_rB_r.
\tag{Q37}
```

In rows 16, 17, and 22 the scalar and triplet pieces combine as

```math
-\frac{ig}3-\frac{5ig}{12}=-\frac{3ig}4,
\qquad
-\frac{10ig}3+\frac{ig}3=-3ig,
\qquad
-\frac{13g^2}{12}-\frac{11g^2}6=-\frac{35g^2}{12}
\tag{Q38}
```

The total $`J_F`$ coefficient from the three implicit boxes is

```math
\frac{g^2L_0^2}{16}+\frac{3g^2L_0^2}{16}+\frac{gN_0}2
=-\frac{g^2L_0^2}2
\tag{Q39}
```

which yields row 1 of Q37. Terms $`\bar\nabla K`$, $`\bar\nabla(\bar\Psi\zeta)`$, and $`\bar\nabla z`$ are explicit total derivatives with constant background coefficients.

## Total quadratic action and retained variables

```math
\boxed{
S^{(2)}\simeq_\partial
\frac1{2\kappa_5^2}\int d^5x\,\bar e\,
\left[\ell_B^{(2)}+\ell_{2\partial,F}^{(2)}
+\alpha\ell_{\log,F}^{(2)}\right].
}
\tag{Q40}
```

Here Q20 is $`\ell_B^{(2)}`$, Q36 is $`\ell_{2\partial,F}^{(2)}`$, and Q37 is $`\ell_{\log,F}^{(2)}`$. Q2 retains exact coupling dependence. All composite spinors are defined by Q24/Q28–Q33, including gravitino–linear-multiplet mixing.

The independent fluctuations are

```math
\{h_{\mu\nu},a_{ab};\ c_\mu,b_{\mu\nu},e_{\mu\nu\rho};\
l,n,v_\mu,w_\mu^{ij};\ \Psi_\mu^i,\zeta^i\}
\tag{Q41}
```

The quantities $`\Phi,Q,s,t,u,\lambda,\mathcal P,\chi_1,p`$ and other composites are not separately varied. No field was eliminated or assigned its two-derivative auxiliary status in advance.

## Vanishing first variation

Define metric Euler coefficients with respect to inverse-metric variations: $`\delta S\simeq_\partial(2\kappa_5^2)^{-1}\int e(\mathcal E_{\mu\nu}\delta g^{\mu\nu}+\mathcal E_L\delta L+\mathcal E_N\delta N+\cdots)`$. Insert the Q2 values of $`N_0,k`$ before setting the branch polynomial Q3 to zero:

```math
\begin{aligned}
\bar{\mathcal E}_N
&=-\frac{4N_0}{L_0}-2gL_0-4g
+\alpha\left(\frac{10gk}3-\frac{g^2N_0}3+\frac{2g^3L_0^2}3\right)
=-\frac g2\mathcal B,\\
\bar{\mathcal E}_L
&=20k+\frac{2N_0^2}{L_0^2}-2gN_0-\frac32g^2L_0^2+4g^2L_0\\
&\quad+\alpha\left(-\frac{10g^2L_0k}3+\frac{4g^3L_0N_0}3
+\frac{5g^4L_0^3}6\right)
=\frac{g^2L_0}2\mathcal B,\\
\bar{\mathcal E}_{\mu\nu}
&=-\frac{g^2L_0^2}2\mathcal B\,\bar g_{\mu\nu}.
\end{aligned}
\tag{Q42}
```

The other bosonic Euler expressions vanish with background fluxes and derivatives; the fermionic ones vanish by parity at zero fermions. Since $`\delta g^{\mu\nu}=-h^{\mu\nu}`$,

```math
\boxed{
S^{(1)}\simeq_\partial
\frac1{2\kappa_5^2}\int d^5x\,\bar e\,\mathcal B
\left(\frac{g^2L_0^2}2h+\frac{g^2L_0}2l-\frac g2n\right)=0.
}
\tag{Q43}
```

## Independent bosonic linearization

### Scalars

The terms quadratic in fluxes in the full $`N`$ equation do not contribute linearly. Direct variation gives

```math
\begin{aligned}
\delta\mathcal E_N
&=\left(\frac{4N_0}{L_0^2}-2g+\frac{4\alpha g^3L_0}3\right)l
-\left(\frac4{L_0}+\frac{\alpha g^2}3\right)n+\frac{\alpha g}6r\\
&=\frac{\alpha g}6r+\left(-8g+\frac{4\alpha g^3L_0}3\right)l
-\left(\frac4{L_0}+\frac{\alpha g^2}3\right)n
\end{aligned}
\tag{Q44}
```

This equals the $`n`$ variation of Q20. The full $`L`$ equation gives

```math
\begin{aligned}
\delta\mathcal E_L={}&
\left(1-\frac{\alpha g^2L_0}6\right)r
-\left(\frac2{L_0}-\frac{\alpha g^2}2\right)\bar\Box l\\
&+\left(4g^2-12g^2L_0+\frac{13\alpha g^4L_0^2}6\right)l
+\left(-8g+\frac{4\alpha g^3L_0}3\right)n
\end{aligned}
\tag{Q45}
```

which also follows from Q20 using $`\delta(\bar\nabla l)^2\simeq_\partial-2\delta l\bar\Box l`$ and the Q18 Hessian.

### Metric

```math
\mathscr G_{\mu\nu}:=\mathscr R_{\mu\nu}-\frac12\bar g_{\mu\nu}r.
\tag{Q46}
```

For symmetric $`P^{\mu\nu}`$ and scalar $`f`$, define formal adjoints

```math
\begin{aligned}
(\mathscr R^\dagger P)_{\mu\nu}
&=\bar\nabla_\rho\bar\nabla_{(\mu}P_{\nu)}{}^\rho
-\frac12\bar\Box P_{\mu\nu}
-\frac12\bar g_{\mu\nu}\bar\nabla_\rho\bar\nabla_\sigma P^{\rho\sigma}
-4kP_{\mu\nu},\\
(r^\dagger f)_{\mu\nu}
&=\bar\nabla_\mu\bar\nabla_\nu f
-\bar g_{\mu\nu}\bar\Box f-4k\bar g_{\mu\nu}f
\end{aligned}
\tag{Q47}
```

The $`h^{\mu\nu}`$ Euler coefficient of Q20 is

```math
\mathcal E^{(1)}_{h,\mu\nu}
=-B_0\mathscr G_{\mu\nu}
+\mathscr R^\dagger\left(-\frac\alpha3\mathscr R
+\frac\alpha{12}\bar g\,r\right)_{\mu\nu}
+(r^\dagger a_1)_{\mu\nu}
\tag{Q48}
```

In the independent variation of the full metric equation, the Ricci response is

```math
\begin{aligned}
Z^{\mu\nu}&:=\frac{\partial\ell}{\partial R_{\mu\nu}}
=A g^{\mu\nu}+\alpha\left(-\frac13R^{\mu\nu}+\frac1{12}Rg^{\mu\nu}\right),\\
\bar Z^{\mu\nu}&=B_0\bar g^{\mu\nu},\\
\delta Z^{\mu\nu}&=a_1\bar g^{\mu\nu}-B_0h^{\mu\nu}+Q^{\mu\nu},
\qquad Q^{\mu\nu}:=-\frac\alpha3\mathscr R^{\mu\nu}
+\frac\alpha{12}\bar g^{\mu\nu}r
\end{aligned}
\tag{Q49}
```

The tensor $`Q^{\mu\nu}`$ here is not the spinor curvature. The Palatini operator obeys $`\mathscr R^\dagger P=-\bar{\mathcal P}[P]-4kP`$. Direct linearization of the full inverse-metric equation gives

```math
\begin{aligned}
\delta\mathcal E_{\mu\nu}
&=B_0\mathscr G_{\mu\nu}+4ka_1\bar g_{\mu\nu}+4kQ_{\mu\nu}
+\bar{\mathcal P}[a_1\bar g+Q]_{\mu\nu},\\
-\delta\mathcal E_{\mu\nu}
&=-B_0\mathscr G_{\mu\nu}+(r^\dagger a_1)_{\mu\nu}
+(\mathscr R^\dagger Q)_{\mu\nu}
=\mathcal E^{(1)}_{h,\mu\nu}
\end{aligned}
\tag{Q50}
```

The minus sign comes from $`\delta g^{\mu\nu}=-h^{\mu\nu}`$.

### Vectors, forms, and internal connections

Normalize responses by

```math
\delta\ell_B^{(2)}\simeq_\partial
\frac12\Pi^{ab}\delta\mathcal G_{ab}
+\frac16Q_H^{abc}\delta\mathcal H_{abc}
+W_a\delta p^a+\frac12\mathcal M^{ab}_{ij}\delta\mathcal F_{ab}^{ij}
+\hbox{explicit potential variations}.
\tag{Q51}
```

Variation of Q20 and direct linearization of the full responses both give

```math
\begin{aligned}
\Pi^{ab}={}&\left(-2L_0+\frac{5\alpha g^2L_0^2}6\right)\mathcal G^{ab}
-\frac{\alpha g^2L_0^2}{36}\bar\varepsilon^{abcde}\mathcal H_{cde}
+\frac{\alpha g}3L_{0ij}\mathcal F^{abij}\\
&+\frac{2\alpha}3\bar\nabla^{[a}(-j^{b]}+gp^{b]}),\\
Q_H^{abc}={}&\left(-4L_0+\frac{2\alpha g^2L_0^2}3\right)\mathcal H^{abc}
-\frac{\alpha g^2L_0^2}{12}\bar\varepsilon^{deabc}\mathcal G_{de}
-\frac{\alpha g}3L_{0ij}\bar\varepsilon^{deabc}\mathcal F_{de}^{ij}
+2\alpha\bar\nabla^{[a}q^{bc]},\\
W_a={}&\left(-\frac4{L_0}+\frac{2\alpha g^2}3\right)p_a
-2\sqrt2v_a-4gc_a+\frac{\alpha g}3j_a,\\
\mathcal M^{ab}_{ij}={}&\alpha\left[
\frac23\mathcal F^{ab}_{ij}+\frac g3L_{0ij}\mathcal G^{ab}
-\frac g9L_{0ij}\bar\varepsilon^{abcde}\mathcal H_{cde}\right].
\end{aligned}
\tag{Q52}
```

For example, using $`\delta j^a=\bar\nabla_b\delta\mathcal G^{ab}`$ and $`\delta q_{ab}=\bar\nabla^c\delta\mathcal H_{cab}`$,

```math
\begin{aligned}
\delta\left(-\frac\alpha6j^2+\frac{\alpha g}3p\cdot j\right)
&\simeq_\partial\frac\alpha3\bar\nabla^{[a}(-j^{b]}+gp^{b]})
\delta\mathcal G_{ab}+\frac{\alpha g}3j_a\delta p^a,\\
\delta\left(-\frac\alpha6q^2\right)
&\simeq_\partial\frac\alpha3\bar\nabla^{[a}q^{bc]}
\delta\mathcal H_{abc}.
\end{aligned}
\tag{Q53}
```

The factors $`1/2,1/6`$ in Q51 fix the derivative coefficients in Q52. With $`1/2!,1/3!`$ in the potential variation, the equations are

```math
\begin{aligned}
\mathcal E_b^{\nu\rho}&=-\bar\nabla_\mu Q_H^{\mu\nu\rho},\\
\mathcal E_c^\nu&=-4gp^\nu-\bar\nabla_\mu\Pi^{\mu\nu}
-\frac12\bar C_\mu\mathcal E_b^{\mu\nu},\\
\mathcal E_{e_3}^{\rho\sigma\lambda}
&=\frac g2Q_H^{\rho\sigma\lambda}
+\frac12\bar\varepsilon^{\mu\nu\rho\sigma\lambda}\bar\nabla_\nu W_\mu,\\
\mathcal V^\nu_{ij}
&=-\bar D_\mu\mathcal M^{\mu\nu}_{ij}
+(4L_0-\alpha g^2L_0^2)w^\nu_{ij}
-2\sqrt2p^\nu\delta_{ij},\\
\mathcal E_v^\nu&=\frac12\delta^{ij}\mathcal V^\nu_{ij},\qquad
\mathcal E_w^\nu{}_{ij}=(\mathcal V^\nu_{ij})_{\rm traceless}
\end{aligned}
\tag{Q54}
```

The $`\bar C`$ term retains $`\delta\mathcal H=\bar C\wedge d\delta c/2`$. Changing the response by the explicit Chern–Simons divergence leaves these bulk equations unchanged.

## Fermionic Euler operator and coefficient checks

### Graded variation

Let $`\Xi=(\Psi_a,\zeta)^T`$. For each row write $`A_r=T_{A_r}\Xi`$, $`B_r=T_{B_r}\Xi`$, with maps defined above. The formal adjoint is defined by

```math
\int\bar e\,\overline{Tu}\,v\simeq_\partial
\int\bar e\,\bar u\,T^\sharp v,\qquad
\gamma_a^\sharp=\gamma_a,\quad
\gamma_{ab}^\sharp=-\gamma_{ab},\quad
M^\sharp=-M,\quad
\bar\nabla_a^\sharp=-\bar\nabla_a,
\quad i^\sharp=i
\tag{Q55}
```

It reverses derivative order and free Lorentz matrix indices; it never identifies $`t_{ab}`$ with $`t_{ba}`$. Using $`\bar u v=-\bar v u`$,

```math
\begin{aligned}
\delta\int\bar e\,c\,\overline{T_A\Xi}\Gamma T_B\Xi
&=\int\bar e\,c\left[
\overline{T_A\delta\Xi}\Gamma T_B\Xi
+\overline{T_A\Xi}\Gamma T_B\delta\Xi\right]\\
&\simeq_\partial\int\bar e\,\overline{\delta\Xi}\,
c\left(T_A^\sharp\Gamma T_B-T_B^\sharp\Gamma^\sharp T_A\right)\Xi.
\end{aligned}
\tag{Q56}
```

The complete fermionic Euler operator of Q40 is therefore the factorized expression

```math
\boxed{
\begin{pmatrix}\mathcal E_\Psi^{(1)}\\\mathcal E_\zeta^{(1)}\end{pmatrix}
=\left[
\sum_{r=1}^{10}c_r\left(T_{A_r}^\sharp\Gamma_rT_{B_r}
-T_{B_r}^\sharp\Gamma_r^\sharp T_{A_r}\right)
+\alpha\sum_{r=1}^{28}d_r\left(T_{A_r}^\sharp\Gamma_rT_{B_r}
-T_{B_r}^\sharp\Gamma_r^\sharp T_{A_r}\right)
\right]\Xi .
}
\tag{Q57}
```

Q57 gives the factorized Euler operator obtained by varying the quadratic action Q40. The coefficient and Noether checks are specified next.

### Implicit source coefficients from first variation

Vary the source's explicit degree-zero scalar polynomial before imposing the background:

```math
\begin{aligned}
\delta N_{\log}[0]\big|_{\rm boxes}={}&
\left(\frac53\Box^c\sigma+\frac53g^2L^2+\frac83gN\right)
\delta(\Box^c\sigma)
-3(\mathcal D^a\mathcal D^b\sigma)\delta(\mathcal D_a\mathcal D_b\sigma)\\
&-g^2L_{ij}\delta(\Box^cL^{ij})-g\delta(\Box^cN),\\
\delta\left[-\frac g2L_{ij}L_{\log}^{ij}[0]\right]\big|_{\rm boxes}
={}&\frac{g^2L^2}2\delta(\Box^c\sigma)
+\frac{g^2}2L_{ij}\delta(\Box^cL^{ij})
\end{aligned}
\tag{Q58}
```

Then substitute Q15:

```math
\begin{aligned}
[\delta X_F]:\quad
-\frac{25k}6+\frac{3k}2+\frac{13g^2L_0^2}6+\frac{8gN_0}3
&=-\frac{8k}3+\frac{13g^2L_0^2}6+\frac{8gN_0}3
=-\frac{g^2L_0^2}2,\\
[\delta Y_F]:\quad -g^2+\frac{g^2}2&=-\frac{g^2}2,\\
[\delta Z_F]:\quad&-g
\end{aligned}
\tag{Q59}
```

These are the three implicit coefficients of Q35. Both fermion endpoints in $`X_F,Y_F,Z_F`$ are varied; $`\omega,\phi,f`$ are not held fixed.

The 19 explicit AL-NF2 bilinears surviving on the background match rows 9–27 with the three pre-merger coefficients specified above. Add the four triplet structures using Q34/Q38. The internal-index conversion Q23 controls the signs of $`\bar QMQ`$, $`\bar\zeta Ms`$, and $`\bar sMs`$.

This coefficient/descendant check guards against omitted implicit connections. It is not a separately expanded residual comparison of every mixed and gravitino Euler block.

### Diagonal spinor block

Collect monomials independent of $`\Psi`$ to isolate a coefficient block, without imposing $`\Psi=0`$ on the theory. In those monomials,

```math
\upsilon_a\longrightarrow\bar\nabla_a\zeta,\quad
\chi_1\longrightarrow\frac g8\zeta,\quad
\lambda\longrightarrow-\frac{2i}{L_0}\not{\bar\nabla}\zeta
-\frac{5g}{L_0}M\zeta.
\tag{Q60}
```

Rows 5–7 of Q36 give

```math
\begin{aligned}
\ell_{2\partial,\zeta\zeta}^{(2)}
&\simeq_\partial
\left(-\frac2{L_0}+\frac4{L_0}\right)\bar\zeta\not{\bar\nabla}\zeta
+\left(\frac{3ig}{L_0}-\frac{10ig}{L_0}\right)\bar\zeta M\zeta\\
&=\frac2{L_0}\bar\zeta\not{\bar\nabla}\zeta
-\frac{7ig}{L_0}\bar\zeta M\zeta,\\
\ell_{\log,\zeta\zeta}^{(2)}
&=\frac{g^2}6\bar\zeta\not{\bar\nabla}\zeta
+\frac{17ig^3}{12}\bar\zeta M\zeta
\end{aligned}
\tag{Q61}
```

The two endpoint variations double the coefficients. Returning to lower internal indices,

```math
\boxed{
(\mathcal K_{\zeta\zeta}\zeta)_i
=\left(\frac4{L_0}+\frac{\alpha g^2}3\right)
\not{\bar\nabla}\zeta_i
+i\left(\frac{14g}{L_0}-\frac{17\alpha g^3}6\right)L_{0ij}\zeta^j.
}
\tag{Q62}
```

This equals the independently derived general-field E63 after Q4/Q2 substitution. The full equation still contains $`\mathcal K_{\zeta\Psi}\Psi`$.

## Linear gauge identities

### Bosonic identities

For a background-covariant diffeomorphism,

```math
\delta h_{\mu\nu}=2\bar\nabla_{(\mu}\xi_{\nu)},\qquad
\delta l=\delta n=0,
\qquad
\delta X_{\mu\nu}=\mathcal L_\xi(4k\bar g_{\mu\nu})=4k\delta h_{\mu\nu}
\tag{Q63}
```

so $`\delta\mathscr R_{\mu\nu}=\delta r=0`$. Transformations of flat background potentials can be represented by internal/form gauge transformations. The adjoints in Q47 imply

```math
\bar\nabla^\mu\mathscr G_{\mu\nu}=0,\qquad
\bar\nabla^\mu(\mathscr R^\dagger P)_{\mu\nu}=0,\qquad
\bar\nabla^\mu(r^\dagger f)_{\mu\nu}=0,
\qquad \bar\nabla^\mu\mathcal E^{(1)}_{h,\mu\nu}=0
\tag{Q64}
```

The form and residual internal transformations are

```math
\delta c=d\Lambda,\qquad
\delta b_2=d\Lambda_1-\frac g2\Lambda_2,\qquad
\delta e_3=d\Lambda_2,\qquad
\delta v=d\beta
\tag{Q65}
```

They leave $`\mathcal G,\mathcal H,p`$ invariant. No new inhomogeneous gauge symmetry is assigned to the traceless internal connection with fixed compensator direction. Q54 implies

```math
\begin{gathered}
\bar\nabla_\nu\mathcal E_b^{\nu\rho}=0,\qquad
\bar\nabla_\nu\mathcal E_c^\nu=0,\qquad
\bar\nabla_\rho\mathcal E_{e_3}^{\rho\sigma\lambda}
+\frac g2\mathcal E_b^{\sigma\lambda}=0,\qquad
\bar\nabla_\nu\mathcal E_v^\nu=0.
\end{gathered}
\tag{Q66}
```

The $`Q_H`$ terms cancel as $`g\bar\nabla Q_H/2-g\bar\nabla Q_H/2=0`$; the epsilon double derivative is $`d^2W=0`$. The remaining $`c`$-equation terms vanish using $`d\bar C=0`$ and the first Q66 identity.

### Local fermionic Noether identity

Use an arbitrary local spinor $`\epsilon(x)`$, without imposing a Killing equation. The inhomogeneous transformations are

```math
\delta\Psi_a=\mathscr D_a\epsilon,
\qquad \mathscr D_a:=\bar\nabla_a+\frac{ig}2M\gamma_a,
\qquad \delta\zeta=0
\tag{Q67}
```

The last equality uses $`N_0/2+3gL_0^2/4=0`$. With $`[\bar\nabla_a,\bar\nabla_b]\epsilon=k\gamma_{ab}\epsilon/2`$,

```math
\Phi_a[\mathscr D\epsilon]
=-\frac g2M\bar\nabla_a\epsilon-\frac{ik}4\gamma_a\epsilon
=-\frac g2M\mathscr D_a\epsilon,
\qquad
s_a[\mathscr D\epsilon]=Q_{ab}[\mathscr D\epsilon]=0.
\tag{Q68}
```

Q24 implies $`\delta\upsilon=\delta\chi_1=\delta t=\delta u=\delta\mathcal P=0`$. The needed Clifford/derivative identities are

```math
\not{\bar\nabla}^{,2}=\bar\Box-5k,
\qquad
\bar\nabla^as_a=\not{\bar\nabla}S+2igMS
\tag{Q69}
```

To verify the second, set $`U=\gamma^a\Psi_a`$ and $`d=\bar\nabla^a\Psi_a`$:

```math
\begin{aligned}
S&=-\frac g2MU-\frac i4\not{\bar\nabla}U+\frac i4d,\\
\bar\nabla^a\not{\bar\nabla}\Psi_a
&=\not{\bar\nabla}d+2kU,\\
\bar\nabla^as_a-\not{\bar\nabla}S
&=-\frac g2M(d-\not{\bar\nabla}U)-ikU\\
&=2igMS-i\left(k+\frac{g^2L_0^2}2\right)U=2igMS.
\end{aligned}
\tag{Q70}
```

Using Q33, Q24, and Q69,

```math
\mathcal P
=(-4gM\not{\bar\nabla}+ig^2L_0^2)S
-g\bar\Box\zeta+2ig^2M\not{\bar\nabla}\zeta
-\frac{27g^3L_0^2}8\zeta.
\tag{Q71}
```

The variation of Q36–Q37 collects, with the Q21 flips, into

```math
\delta S_F^{(2)}\simeq_\partial
\frac1{2\kappa_5^2}\int\bar e\,
\overline{\mathscr D^a\epsilon}(W_a^{s}+W_a^{\zeta})
\tag{Q72}
```

where the two currents are

```math
\begin{aligned}
W_a^{s}={}&-i\left(3L_0+\frac{\alpha g^2L_0^2}2\right)\gamma_{ab}s^b
-2i\alpha g^2L_0^2s_a-2\alpha gM\gamma_{ab}\bar\nabla^bS,\\
W_a^{\zeta}={}&\frac{2i}{L_0}M\gamma_{ab}\bar\nabla^b\zeta-2g\gamma_a\zeta\\
&+\alpha\left[
\frac g2(\bar\nabla_a\not{\bar\nabla}-\gamma_a\bar\Box)\zeta
+\frac{ig^2}4M(5\gamma_a\not{\bar\nabla}-\bar\nabla_a)\zeta
-\frac{7g^3L_0^2}4\gamma_a\zeta\right].
\end{aligned}
\tag{Q73}
```

For $`\mathscr D_a^\sharp=-\bar\nabla_a-ig\gamma_aM/2`$, the pure-gravitino current gives

```math
\begin{aligned}
\mathscr D^{a\sharp}(\gamma_{ab}s^b)
&=\bar\nabla^as_a-\not{\bar\nabla}S-2igMS=0,\\
\mathscr D^{a\sharp}\left(-2ig^2L_0^2s_a
-2gM\gamma_{ab}\bar\nabla^bS\right)
&=-5g(g^2L_0^2+2k)MS=0
\end{aligned}
\tag{Q74}
```

The two source contributions to the mixed current are

```math
\begin{aligned}
\mathscr D^{a\sharp}W_{2\partial,a}^{\zeta}
&=(1-L_0)(2g\not{\bar\nabla}+5ig^2M)\zeta,\\
\mathscr D^{a\sharp}W_{\log,a}^{\zeta}
&=\left(\frac{g^3L_0^2}4\not{\bar\nabla}
+\frac{5ig^4L_0^2}8M\right)\zeta,\\
\mathscr D^{a\sharp}W_a^{\zeta}
&=\left[2g(1-L_0)+\frac{\alpha g^3L_0^2}4\right]
\not{\bar\nabla}\zeta
+i\left[5g^2(1-L_0)+\frac{5\alpha g^4L_0^2}8\right]M\zeta\\
&=\frac g4\underbrace{(\alpha g^2L_0^2-8L_0+8)}_{\mathcal B}
\left(\not{\bar\nabla}+\frac{5ig}2M\right)\zeta=0.
\end{aligned}
\tag{Q75}
```

The total quadratic form thus satisfies

```math
\boxed{\mathscr D^{a\sharp}\mathcal E_{\Psi a}^{(1)}\equiv0}
\tag{Q76}
```

The cancellation uses the total branch equation Q3, not the two-derivative vacuum alone.

## Exceptional coefficients and verification record

No potentially vanishing kinetic or mass coefficient was divided out in Q20/Q36–Q37/Q44–Q57. For example, Q3 implies

```math
\begin{aligned}
B_0&=L_0-\frac12(8L_0-8)=4-3L_0,\\
\frac1{L_0}-\frac{\alpha g^2}4
&=\frac{2-L_0}{L_0^2},\\
\frac4{L_0}+\frac{\alpha g^2}3
&=\frac{4(5L_0-2)}{3L_0^2}
\end{aligned}
\tag{Q77}
```

Solving these zero-coefficient conditions with Q3 gives

```math
\begin{array}{c|c|c}
\text{Vanishing coefficient}&L_0&\alpha g^2\\\hline
B_0&4/3&3/2\\
1/L_0-\alpha g^2/4&2&2\\
4/L_0+\alpha g^2/3&2/5&-30
\end{array}
\tag{Q78}
```

These are equation-determined exceptional points. They remain in the formulas; a physical-mode count depends on the rank of the full coupled system.

| Calculation or check | Recorded result and scope |
|---|---|
| First variation | Q42–Q43: all background Euler coefficients vanish in the bulk |
| Determinant and curvature expansion | Q7–Q11: second order including metric contractions |
| Bosonic quadratic density | Q16–Q20: scalar Hessian, curvature, fluxes, internal connection, and all mixing |
| Independent bosonic comparison | Q44–Q54: quadratic variation and direct full-equation linearization give identical bulk expressions |
| Fermionic quadratic form | Q24–Q40: implicit supercovariant terms and explicit bilinears, retaining $`\Psi`$ and $`\zeta`$ together |
| Implicit fermionic source coefficients | Q58–Q59: first source variation matches the three box coefficients |
| Explicit fermionic source coefficients | The 19 surviving AL-NF2 rows, triplet additions, and Q23 internal signs were compared |
| Diagonal fermion operator | Q60–Q62: agrees with the separate general-background derivation E63 |
| Bosonic gauge identities | Q63–Q66: diffeomorphisms, form gauge, and residual $`U(1)`$ |
| Local fermionic Noether identity | Q67–Q76: analytic cancellation for an arbitrary local SUSY parameter |
| Boundary scope | The result is a local bulk quadratic action, with equalities understood modulo the displayed total derivatives. |

The recorded checks used symbolic derivatives, coefficient comparison, exact rational coefficients, and branch relations only. Scalar tadpoles/Hessians, $`B_0`$, the Q59 implicit coefficient, and the Q75 branch-polynomial factorization were rechecked symbolically when this record was saved.

The full bulk quadratic action on Q2 is Q40. Q43 cancels the first variation; Q44–Q54 give the bosonic linear equations; Q57 gives the factorized fermionic Euler operator; Q64/Q66/Q76 give the verified local gauge identities. All independent fluctuation sectors were retained.

