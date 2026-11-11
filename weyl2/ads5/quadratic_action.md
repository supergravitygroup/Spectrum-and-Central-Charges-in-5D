# Weyl²: quadratic action on AdS5

[Notation dictionary](../notation.md).

[Reading guide](README.md). The equation labels and local symbols below follow the action conventions specified for this theory.

<a id="7-quadratic-action-including-all-fields"></a>

## Quadratic action including all fields

The following block contains the geometry, connections, composites, and four Lagrangian blocks of the quadratic action.

The inverse-metric expansion includes the second-order term with the following sign:

```math
g^{\mu\nu}=\bar g^{\mu\nu}-zh^{\mu\nu}
+z^2(h^\mu{}_\rho h^{\rho\nu}-q^{\mu\nu})
```

Check:

```math
(\bar g+zh+z^2q)
\big(\bar g^{-1}-zh^\sharp+z^2[(h^\sharp)^2-q^\sharp]\big)
=\mathbf1+O(z^3).
```

In this block, $`z`$ counts expansion order and must be distinguished from the radial $`z`$ used later for boundary behavior.

<a id="1-background-and-meaning-of-the-expansion"></a>

### Background and meaning of the expansion

```math
S=S_{2\mathrm{-der}}+\alpha S_{\mathrm{Weyl}^2},\qquad
\alpha\in\mathbb R\setminus\{0\},\qquad g\in\mathbb R\setminus\{0\}.
```

$`\alpha`$ is a generic constant, not perturbative. Fields remain off shell;
fermion order does not exceed two. The selected branch's values
determined by the background equations are:

```math
\bar L=1,\quad \bar N=-\frac{3g}{2},\quad \bar D=0,\quad
\bar R_{\mu\nu}=-2g^2\bar g_{\mu\nu},\quad
\bar R=-10g^2,\quad \ell^2=\frac2{g^2},\quad
\bar f_a{}^b=\frac{g^2}{8}\delta_a{}^b.
```

Background form strengths and fermions vanish. Local potential
representatives are $`\bar C=\bar B=\bar E_3=\bar V=\bar V'=0`$. The current gauge $`\sigma=1,\psi^i=0,b_\mu=0, L_{ij}=L\delta_{ij}/\sqrt2`$ is retained.
Here $`\psi^i`$ is not the gravitino.

```math
S(z)=S^{(0)}+zS^{(1)}+z^2S^{(2)}+O(z^3),\qquad
S^{(2)}=\frac12\left.\frac{d^2S(z)}{dz^2}\right|_{z=0}.
\tag{1}
```

$`z`$ counts fluctuation order only.

<a id="2-independent-fluctuations-and-geometry"></a>

### Independent fluctuations and geometry

```math
\begin{gathered}
e_\mu{}^a=\bar e_\mu{}^a+z k_\mu{}^a,\qquad
L=1+z\lambda,\qquad N=-\frac{3g}{2}+zn,\\
C_\mu=zc_\mu,\quad B_{\mu\nu}=zb_{\mu\nu},\quad
E_{\mu\nu\rho}=za_{\mu\nu\rho},\\
V_\mu=zv_\mu,\quad V_\mu^{\prime\,ij}=zv_\mu^{\prime\,ij},
\quad\delta_{ij}v_\mu^{\prime\,ij}=0,\\
\psi_\mu{}^i=z\Psi_\mu{}^i,\qquad\varphi^i=z\zeta^i.
\end{gathered}\tag{2}
```

No new Lorentz gauge is selected. All contractions and $`\nabla`$ derivatives
below use the background metric and connections.

```math
\begin{gathered}
k_{\mu\nu}=k_\mu{}^a\bar e_{\nu a},\quad
h_{\mu\nu}=k_{\mu\nu}+k_{\nu\mu},\quad
q_{\mu\nu}=k_\mu{}^ak_{\nu a},\quad h=\bar g^{\mu\nu}h_{\mu\nu},\\
g_{\mu\nu}=\bar g_{\mu\nu}+zh_{\mu\nu}+z^2q_{\mu\nu},\\
g^{\mu\nu}=\bar g^{\mu\nu}-zh^{\mu\nu}
+z^2(h^\mu{}_\rho h^{\rho\nu}-q^{\mu\nu}),\\
\frac e{\bar e}=1+zm_1+z^2m_2,\qquad
m_1=\frac h2,\qquad
m_2=\frac12q^\mu{}_\mu+\frac18h^2-\frac14h_{\mu\nu}h^{\mu\nu}.
\end{gathered}\tag{3}
```

```math
\begin{aligned}
A^\rho{}_{\mu\nu}
&=\frac12\bar g^{\rho\sigma}
(\nabla_\mu h_{\nu\sigma}+\nabla_\nu h_{\mu\sigma}
-\nabla_\sigma h_{\mu\nu}),\\
B^\rho{}_{\mu\nu}
&=\frac12\bar g^{\rho\sigma}
(\nabla_\mu q_{\nu\sigma}+\nabla_\nu q_{\mu\sigma}
-\nabla_\sigma q_{\mu\nu})-h^\rho{}_\sigma A^\sigma{}_{\mu\nu},\\
\Gamma^\rho{}_{\mu\nu}
&=\bar\Gamma^\rho{}_{\mu\nu}+zA^\rho{}_{\mu\nu}+z^2B^\rho{}_{\mu\nu},\\
P_{\mu\nu}&=\nabla_\rho A^\rho{}_{\mu\nu}
-\nabla_\nu A^\rho{}_{\mu\rho},\\
Q_{\mu\nu}&=\nabla_\rho B^\rho{}_{\mu\nu}
-\nabla_\nu B^\rho{}_{\mu\rho}
+A^\rho{}_{\rho\lambda}A^\lambda{}_{\mu\nu}
-A^\rho{}_{\nu\lambda}A^\lambda{}_{\mu\rho},\\
r_1&=\bar g^{\mu\nu}P_{\mu\nu}+2g^2h
=\nabla_\mu\nabla_\nu h^{\mu\nu}-\Box h+2g^2h,\\
r_2&=\bar g^{\mu\nu}Q_{\mu\nu}-h^{\mu\nu}P_{\mu\nu}
-2g^2(h_{\mu\nu}h^{\mu\nu}-q^\mu{}_\mu),\\
R(g)&=-10g^2+zr_1+z^2r_2.
\end{aligned}\tag{4}
```

$`\bar D_\mu k_\nu{}^a`$ contains both coordinate and Lorentz background connections:

```math
\begin{aligned}
\Omega_{1\mu}{}^a{}_b
&=\bar e_b{}^\nu(A^\rho{}_{\mu\nu}\bar e_\rho{}^a-\bar D_\mu k_\nu{}^a),\\
\Omega_{2\mu}{}^a{}_b
&=\bar e_b{}^\nu(B^\rho{}_{\mu\nu}\bar e_\rho{}^a
+A^\rho{}_{\mu\nu}k_\rho{}^a-\Omega_{1\mu}{}^a{}_c k_\nu{}^c),\\
\kappa_\mu{}^{ab}
&=\frac12\bar\Psi^{[a}\gamma^{b]}\Psi_\mu
+\frac14\bar\Psi^a\gamma_\mu\Psi^b,\\
\omega_\mu{}^{ab}
&=\bar\omega_\mu{}^{ab}+z\Omega_{1\mu}{}^{ab}
+z^2(\Omega_{2\mu}{}^{ab}+\kappa_\mu{}^{ab}).
\end{aligned}\tag{5}
```

<a id="3-forms-and-dependent-bosonic-objects"></a>

### Forms and dependent bosonic objects

```math
\begin{gathered}
\mathsf G_{\mu\nu}=2\nabla_{[\mu}c_{\nu]},\qquad
\mathsf H_{\mu\nu\rho}=3\nabla_{[\mu}b_{\nu\rho]}+\frac g2a_{\mu\nu\rho},\\
\mathsf v_{\mu\nu}=2\nabla_{[\mu}v_{\nu]},\qquad
\mathsf V'_{\mu\nu}{}^{ij}=2\nabla_{[\mu}v'_{\nu]}{}^{ij},\\
\mathsf V_{\mu\nu}{}^{ij}
=\mathsf V'_{\mu\nu}{}^{ij}+\frac12\delta^{ij}\mathsf v_{\mu\nu},\\
\mathsf E^{\mu\nu}=-\frac1{12}\bar\varepsilon^{\mu\nu\rho\sigma\lambda}
a_{\rho\sigma\lambda},\qquad
p^\mu=\nabla_\nu\mathsf E^{\mu\nu},\quad
\nabla_\mu\mathsf E^{\mu\nu}=-p^\nu,\quad\nabla_\mu p^\mu=0.
\end{gathered}\tag{6}
```

```math
\begin{aligned}
\widehat G_{\mu\nu}
&=z\mathsf G_{\mu\nu}+z^2\frac i2\bar\Psi_{[\mu}\Psi_{\nu]}+O(z^3),\\
\widehat H_{\mu\nu\rho}
&=z\mathsf H_{\mu\nu\rho}
+z^2\left(\frac32c_{[\mu}\mathsf G_{\nu\rho]}
-\frac34\bar\Psi_{[\mu}\gamma_\nu\Psi_{\rho]}\right)+O(z^3),\\
E^\mu&=zp^\mu+z^2\left[-m_1p^\mu
+\frac i2\bar\Psi_\nu\gamma^{\mu\nu}\zeta
-\frac1{4\sqrt2}\delta_{ij}
\bar\Psi_\nu^i\gamma^{\mu\nu\rho}\Psi_\rho^j\right]+O(z^3).
\end{aligned}\tag{7}
```

$`E^\mu`$ is not a separate independent field.

```math
\tau_{ab}:=T_{ab}^{(1)}
=\frac18\left(\mathsf G_{ab}
+\frac16\bar\varepsilon_{abcde}\mathsf H^{cde}\right),
\qquad
d:=D^{(1)}=-\frac{r_1}{32}+\frac g4 n+\frac{g^2}{8}\lambda .
\tag{8}
```

```math
\begin{aligned}
\mathsf R_{\mu\nu\rho\sigma}
&=h_{\rho\lambda}\bar R^\lambda{}_{\sigma\mu\nu}
+\bar g_{\rho\lambda}
(\nabla_\mu A^\lambda{}_{\nu\sigma}-\nabla_\nu A^\lambda{}_{\mu\sigma}),\\
\mathsf C_{\mu\nu\rho\sigma}
&=\mathsf R_{\mu\nu\rho\sigma}
-\frac13(\bar g_{\mu\rho}P_{\nu\sigma}-\bar g_{\nu\rho}P_{\mu\sigma}
-\bar g_{\mu\sigma}P_{\nu\rho}+\bar g_{\nu\sigma}P_{\mu\rho})\\
&\quad+\frac{r_1}{12}
(\bar g_{\mu\rho}\bar g_{\nu\sigma}-\bar g_{\mu\sigma}\bar g_{\nu\rho})\\
&\quad-\frac{g^2}{6}
(h_{\mu\rho}\bar g_{\nu\sigma}-h_{\nu\rho}\bar g_{\mu\sigma}
-h_{\mu\sigma}\bar g_{\nu\rho}+h_{\nu\sigma}\bar g_{\mu\rho}).
\end{aligned}\tag{9}
```

<a id="4-dependent-fermionic-objects-and-connections"></a>

### Dependent fermionic objects and connections

```math
J^i{}_j=\delta^{ik}\epsilon_{jk},\qquad J^2=-\mathbf1,\qquad
Q'_{ab}{}^i=2\nabla_{[a}\Psi_{b]}{}^i .
```

```math
\begin{aligned}
\Phi_a{}^i:=\phi_a^{(1)i}
&=\frac i3\gamma^bQ'_{ab}{}^i-\frac i{24}\gamma_a\gamma^{bc}Q'_{bc}{}^i,
&\gamma^a\Phi_a{}^i&=\frac i8\gamma^{ab}Q'_{ab}{}^i,\\
\mathcal Q_{ab}{}^i[\Psi]
&=Q'_{ab}{}^i+\frac23\gamma_{[a}\gamma^cQ'_{b]c}{}^i
-\frac1{12}\gamma_{ab}\gamma^{cd}Q'_{cd}{}^i,
&\gamma^a\mathcal Q_{ab}{}^i&=0,\\
\mathcal X^i[\Psi,\zeta]:=\chi^{(1)i}
&=\frac1{32}\gamma^{ab}\nabla_a\Psi_b{}^i
-\frac{ig}{16\sqrt2}\gamma^aJ^i{}_j\Psi_a{}^j+\frac g8\zeta^i .
\end{aligned}\tag{10}
```

$`\gamma^a\mathcal Q_{ab}=0`$ follows identically from the definition; no additional gauge
condition or field equation is imposed on the gravitino.

```math
\begin{aligned}
\mathcal A_a{}^i:=(\mathcal D_a\psi^i)^{(1)}
&=-\Phi_a{}^i-\frac g{2\sqrt2}J^i{}_j\Psi_a{}^j,\\
\mathcal U_a{}^i:=(\mathcal D_a\varphi^i)^{(1)}
&=\nabla_a\zeta^i+\frac{3g}{4}\Psi_a{}^i-\frac3{\sqrt2}J^i{}_j\Phi_a{}^j,\\
\mathcal A_{ai}&=-\Phi_{ai}+\frac g{2\sqrt2}\delta_{ij}\Psi_a{}^j,\\
\mathcal U_{ai}&=\nabla_a\zeta_i+\frac{3g}{4}\Psi_{ai}
+\frac3{\sqrt2}\delta_{ij}\Phi_a{}^j,\\
\Upsilon_i:=(\lambda_{{\rm linear}\,i})^{(1)}
&=-2i\gamma^a\mathcal U_{ai}+8\sqrt2\delta_{ij}\mathcal X^j
+\frac{3g}{\sqrt2}\delta_{ij}\zeta^j\\
&=-2i\mathord{\not{\nabla}}\zeta_i-2ig\gamma^a\Psi_{ai}
-4\sqrt2i\delta_{ij}\gamma^a\Phi_a{}^j
+\frac{5g}{\sqrt2}\delta_{ij}\zeta^j .
\end{aligned}\tag{11}
```

Bar and spinor flips use the Majorana/NW–SE rules of CONVENTIONS.md;
this algebraic bar does not reverse the sign of $`i`$
by complex conjugation.

```math
\begin{aligned}
R_F&=2\nabla_a\kappa_b{}^{ab}
+i\bar\Phi_a\gamma^{ab}\Psi_b-16\bar\Psi_a\gamma^a\mathcal X,\\
f_a{}^{a(1)}&=-\frac{r_1}{16},\qquad
f_a{}^{a(2)}=-\frac{r_2+R_F}{16},\\
D^{(2)}
&=-\frac{r_2+R_F}{32}-\frac1{16}\mathsf G^2-\frac{26}{3}\tau^2
+2\mathsf G_{ab}\tau^{ab}+\frac{g^2}{16}\lambda^2
-\frac i8\bar\Psi_a\mathcal A^a-\frac12\bar\Psi_a\gamma^a\mathcal X .
\end{aligned}\tag{12}
```

The final coefficient in the curvature contraction is:

```math
8\bar\Psi_{[a}\delta_{b]}{}^{[a}\gamma^{b]}\mathcal X
=8\frac{1-5}{2}\bar\Psi_a\gamma^a\mathcal X
=-16\bar\Psi_a\gamma^a\mathcal X .
```

The second conformal derivative retains the dependent $`f`$ connection:

```math
\begin{aligned}
\delta_K(\mathcal D_cT^{ac})
&=(-2-2+2\cdot5-2)\Lambda_{Kb}T^{ab}
=4\Lambda_{Kb}T^{ab},\\
(\mathcal D^b\mathcal D_cT^{ac})^{(1)}
&=\nabla^b\nabla_c\tau^{ac}-4\bar f^{bc}\tau^a{}_c\\
&=\nabla^b\nabla_c\tau^{ac}-\frac{g^2}{2}\tau^{ab}.
\end{aligned}\tag{13}
```

At the required order, first derivatives reduce to $`\nabla\tau,\nabla\mathcal X, \nabla\mathcal Q`$.

<a id="5-four-blocks-of-the-quadratic-action"></a>

### Four blocks of the quadratic action

```math
\boxed{
S^{(2)}=\int d^5x\,\bar e\,
\big[\mathcal L_{2B}^{(2)}+\mathcal L_{2F}^{(2)}
+\alpha\mathcal L_{WB}^{(2)}+\alpha\mathcal L_{WF}^{(2)}\big].}
\tag{14}
```

<a id="51-two-derivative-bosonic-block"></a>

#### Two-derivative bosonic block

```math
\boxed{\begin{aligned}
\mathcal L_{2B}^{(2)}
={}&r_2+m_1r_1-4g^2m_2+\lambda r_1
+(\nabla\lambda)^2-4g^2\lambda^2-8g\lambda n-2n^2\\
&-\frac12\mathsf G^2-\frac13\mathsf H^2
+2v'_\mu{}^{ij}v'^\mu{}_{ij}+2p_\mu p^\mu\\
&-\mathsf E^{\mu\nu}
\left(4\nabla_{[\mu}p_{\nu]}+\sqrt2\mathsf v_{\mu\nu}
+2g\mathsf G_{\mu\nu}\right)\\
&-2\nabla_\mu\left[(m_1\bar g^{\mu\nu}-h^{\mu\nu})
\nabla_\nu\lambda\right].
\end{aligned}}\tag{15}
```

The source boundary representative is retained. After integration by parts,
the form block is:

```math
\begin{aligned}
&2p^2-\mathsf E^{\mu\nu}
(4\nabla_{[\mu}p_{\nu]}+\sqrt2\mathsf v_{\mu\nu}+2g\mathsf G_{\mu\nu})\\
&=-2p^2-2\sqrt2p^\mu v_\mu-4gp^\mu c_\mu\\
&\quad-\nabla_\mu(4\mathsf E^{\mu\nu}p_\nu
+2\sqrt2\mathsf E^{\mu\nu}v_\nu+4g\mathsf E^{\mu\nu}c_\nu).
\end{aligned}\tag{16}
```

Expansion of geometric and potential coefficients:

```math
\begin{aligned}
U(L,N)&=-\frac{2N^2}{L}-2g(L+2)N+2g^2L^2-\frac12g^2L^3,\\
U(1+z\lambda,-3g/2+zn)
&=6g^2+10zg^2\lambda
+z^2(-4g^2\lambda^2-8g\lambda n-2n^2)+O(z^3),\\
\left[\frac e{\bar e}(LR+U)\right]_{z^2}
&=r_2+m_1r_1-4g^2m_2+\lambda r_1
-4g^2\lambda^2-8g\lambda n-2n^2 .
\end{aligned}\tag{17}
```

<a id="52-two-derivative-fermionic-block"></a>

#### Two-derivative fermionic block

```math
j^a=-\frac i{\sqrt2}\delta_{ij}\bar\Psi^{ai}\zeta^j .
```

```math
\boxed{\begin{aligned}
\mathcal L_{2F}^{(2)}
={}&-\bar\Psi_a\gamma^{abc}\nabla_b\Psi_c
+2\bar\zeta\mathord{\not{\nabla}}\zeta
-\frac{3ig}{2\sqrt2}\delta_{ij}\bar\Psi_a^i\gamma^{ab}\Psi_b^j
+\frac{7ig}{\sqrt2}\delta_{ij}\bar\zeta^i\zeta^j\\
&-\sqrt2i\delta_{ij}\bar\Psi_a^i\gamma^{ab}\nabla_b\zeta^j
+\sqrt2i\delta_{ij}\bar\zeta^i\gamma^{ab}\nabla_a\Psi_b^j
-4g\bar\Psi_a\gamma^a\zeta\\
&+2\nabla_a(\kappa_b{}^{ab}-j^a).
\end{aligned}}\tag{18}
```

The two mixed derivative terms remain separate. Intermediate source-map
expressions producing this block ($`Z:=\delta_{ij}\bar\zeta^i\zeta^j`$) are:

```math
\begin{aligned}
B_F&=\nabla_a j^a+6f_F
-\frac i{\sqrt2}\delta_{ij}\bar\Psi^{ai}\mathcal U_a{}^j
-6\bar\Psi_a\gamma^a\mathcal X
+\frac1{\sqrt2}\delta_{ij}\bar\zeta^i\gamma^a\Phi_a{}^j,\\
D_F&=\frac12f_F-\frac i8\bar\Psi_a\mathcal A^a
-\frac12\bar\Psi_a\gamma^a\mathcal X,\qquad f_F=-\frac{R_F}{16},\\
(Y_{\rm trace})_F
&=B_F+4D_F+\frac{3ig}{\sqrt2}Z
+\bar\zeta^i\gamma^a\mathcal U_{ai}.
\end{aligned}\tag{19}
```

The two explicit $`\chi\varphi`$ traces cancel. In the mass terms,
the $`\rho_{\rm linear}N`$ contribution is $`-3igZ/(2\sqrt2)`$, and the $`i\bar\Upsilon^i\zeta_i`$ contribution
is $`-5igZ/\sqrt2`$. Thus:

```math
\begin{aligned}
[Z]:\quad&-2\left(3-\frac32-5\right)\frac{ig}{\sqrt2}
=\frac{7ig}{\sqrt2},\\
3i\bar\Psi_a\gamma^{ab}\Phi_b
&=-\frac12\bar\Psi_a\gamma^{abc}Q'_{bc}
=-\bar\Psi_a\gamma^{abc}\nabla_b\Psi_c,\\
[\bar\Psi_a\Psi^a]:\quad&
ig\left(\frac3{2\sqrt2}+\frac1{2\sqrt2}-\sqrt2\right)=0,\\
[\delta_{ij}\bar\Psi_a^i\gamma^{ab}\Psi_b^j]:\quad&
ig\left(-\sqrt2+\frac1{2\sqrt2}\right)=-\frac{3ig}{2\sqrt2},\\
[\bar\Psi_a\gamma^a\zeta]:\quad&
g\left(\frac32-4-\frac52+1\right)=-4g .
\end{aligned}\tag{20}
```

<a id="53-weyl-squared-bosonic-block"></a>

#### Weyl-squared bosonic block

```math
\boxed{\begin{aligned}
\mathcal L_{WB}^{(2)}
={}&\frac18\mathsf C_{abcd}\mathsf C^{abcd}+\frac{64}{3}d^2
-\frac13\mathsf V'_{ab}{}^{ij}\mathsf V'^{ab}{}_{ij}
-\frac16\mathsf v_{ab}\mathsf v^{ab}\\
&-\frac{64}{3}\nabla_a\tau_{bc}\nabla^a\tau^{bc}
+\frac{64}{3}\nabla_b\tau_{ac}\nabla^a\tau^{bc}
-\frac{128}{3}\tau_{ab}\nabla^b\nabla_c\tau^{ac}\\
&+\frac{64g^2}{3}\tau_{ab}\tau^{ab}
-\frac{8g}{3\sqrt2}\mathsf v_{ab}\tau^{ab}.
\end{aligned}}\tag{21}
```

The $`64g^2\tau^2/3`$ term comes from the dependent $`f`$ connection in (13).
$`d`$ is not an independent field:

```math
\begin{aligned}
\frac{64\alpha}{3}d^2
=\alpha\left[
\frac{r_1^2}{48}-\frac g3r_1n-\frac{g^2}{6}r_1\lambda
+\frac{4g^2}{3}n^2+\frac{4g^3}{3}n\lambda+\frac{g^4}{3}\lambda^2
\right].
\end{aligned}\tag{22}
```

<a id="54-weyl-squared-fermionic-block"></a>

#### Weyl-squared fermionic block

```math
\boxed{\begin{aligned}
\mathcal L_{WF}^{(2)}
={}&\frac34\overline{\mathcal Q}_{ab}\gamma^c\nabla_c\mathcal Q^{ab}
-\frac{256}{3}\overline{\mathcal X}\mathord{\not{\nabla}}\mathcal X\\
&-\frac{ig}{8\sqrt2}\delta^{ij}
\overline{\mathcal Q}_{ab\,i}\mathcal Q_j{}^{ab}
-\frac{128ig}{3\sqrt2}\delta^{ij}\overline{\mathcal X}_i\mathcal X_j .
\end{aligned}}\tag{23}
```

$`\mathcal Q`$ and $`\mathcal X`$ are the explicit differential operators in (10),
not new independent spinors. Since $`\bar C=\bar D=\bar T=\bar R(V)=0`$ and background fermions
vanish, the other monomials in W1 start at third fluctuation order.
The Weyl sector vanishes at zeroth and first order; its determinant
contribution to the quadratic action is therefore only $`\bar e`$.

<a id="6-first-variation"></a>

### First variation

```math
\begin{aligned}
\bar e^{-1}\mathcal L^{(1)}
&=r_1-2g^2h-2\Box\lambda\\
&=\nabla_\mu
(\nabla_\nu h^{\mu\nu}-\nabla^\mu h-2\nabla^\mu\lambda).
\end{aligned}\tag{24}
```

The bulk first variation vanishes by the background equations. This does
not imply that the boundary integral vanishes without a further boundary
condition. No independent fluctuation has been set to zero or eliminated
through an algebraic or differential field equation.

<a id="bolum-8"></a>

