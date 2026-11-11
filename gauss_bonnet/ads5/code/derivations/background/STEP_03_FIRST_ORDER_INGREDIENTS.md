# Step 3 — Ingredients and term ledger through first order

Starting data: action GB07–GB14, `GB-FINAL-DENSITY`, and component SC7-01–06/SC7D-05–07. Background and arbitrary variations are [Step 2](STEP_02_BACKGROUND_CLASSES.md). In this file $`L_0,N_0,k`$ remain free. The abbreviation $`O(t^2)`$ is perturbative order, not an assumption about small $`\lambda`$.

## 3.1 Metric, measure, frame and duals

Write $`h=\bar g^{\mu\nu}h_{\mu\nu}`$ and raise fluctuation indices with $`\bar g`$. Differentiating $`g^{\mu\rho}g_{\rho\nu}=\delta^\mu{}_\nu`$ gives $`\delta g^{\mu\rho}\bar g_{\rho\nu}+\bar g^{\mu\rho}h_{\rho\nu}=0`$, hence

```math
\delta g^{\mu\nu}=-h^{\mu\nu},\qquad \delta e=\tfrac12\bar e\,h,\qquad
\delta e_a{}^\mu=-\tfrac12h^\mu{}_\nu\bar e_a{}^\nu-\theta^b{}_a\bar e_b{}^\mu,\qquad
\delta\varepsilon^{\mu\nu\rho\sigma\tau}=-\tfrac12h\,\bar\varepsilon^{\mu\nu\rho\sigma\tau}. \tag{3.1}
```

The determinant step is $`\delta\log e=\mathop{\mathrm{tr}}\nolimits(e^{-1}\delta e)=h/2+\theta^a{}_a=h/2`$, because an antisymmetric matrix has zero trace. For a lower $`p`$-form $`A`$, $`(*A)_{\mu_1\cdots\mu_{5-p}}=\varepsilon_{\mu_1\cdots\mu_{5-p}\nu_1\cdots\nu_p}g^{\nu_1\rho_1}\cdots g^{\nu_p\rho_p}A_{\rho_1\cdots\rho_p}/p!`$. The product rule gives

```math
\delta(*A)=*\delta A+\tfrac12h*\bar A-*(h^\sharp\!\cdot\bar A),\qquad
(h^\sharp\!\cdot A)_{\rho_1\cdots\rho_p}=\sum_{j=1}^p h_{\rho_j}{}^\nu A_{\rho_1\cdots\rho_{j-1}\nu\rho_{j+1}\cdots\rho_p}. \tag{3.2}
```

Here the first extra term is the varied lower volume tensor, and each summand is one varied inverse metric. In the actual applications $`\bar H_3=\bar E_3=0`$, so both metric-dependent terms vanish: $`\delta(*H_3)=*\delta H_3`$ and $`\delta(*E_3)=*u_3`$. This explains why no hidden Hodge-metric tadpole is lost.

## 3.2 Connection and curvature

At this order the gravitino contorsion is a product of two $`t\zeta`$ factors and starts at $`t^2`$. Varying the torsionless metric-compatible connection gives

```math
\delta\Gamma^\rho{}_{\mu\nu}=\tfrac12\bar g^{\rho\sigma}(\bar\nabla_\mu h_{\nu\sigma}+\bar\nabla_\nu h_{\mu\sigma}-\bar\nabla_\sigma h_{\mu\nu}),\qquad
\delta R^\rho{}_{\sigma\mu\nu}=2\bar\nabla_{[\mu}\delta\Gamma^\rho{}_{\nu]\sigma}. \tag{3.3}
```

The frame-compatible version is obtained by varying $`\nabla_\mu e_\nu{}^a=0`$:

```math
\delta\omega_\mu{}^{ab}=\tfrac12\bar e^{a\rho}\bar e^{b\sigma}(\bar\nabla_\sigma h_{\mu\rho}-\bar\nabla_\rho h_{\mu\sigma})-\bar D_\mu\theta^{ab}. \tag{3.4}
```

The $`\theta`$ term is the connection's Lorentz gauge variation and cancels from scalar curvature contractions. Contracting (3.3), with the Ricci sign in Step 1, gives

```math
\delta R_{\mu\nu}=\tfrac12(\bar\nabla_\rho\bar\nabla_\mu h_\nu{}^\rho+\bar\nabla_\rho\bar\nabla_\nu h_\mu{}^\rho-\bar\Box h_{\mu\nu}-\bar\nabla_\nu\bar\nabla_\mu h). \tag{3.5}
```

No derivative commutation is needed. Contract (3.5), add the varied inverse metric and use $`\bar R_{\mu\nu}=4k\bar g_{\mu\nu}`$:

```math
\begin{aligned}
r:=\delta R&=-h^{\mu\nu}(4k\bar g_{\mu\nu})+\tfrac12(2\bar\nabla_\rho\bar\nabla_\mu h^{\rho\mu}-\bar\Box h-\bar\Box h)\\
&=\bar\nabla_\mu\bar\nabla_\nu h^{\mu\nu}-\bar\Box h-4kh.
\end{aligned}\tag{3.6}
```

The symmetric two terms were combined by relabeling dummy indices, not by commuting covariant derivatives.

## 3.3 First variations of strengths and internal derivatives

Substitute (2.4) into the definitions GB12–GB14. Products $`C G`$ and $`\bar\psi\psi`$ contain two fluctuations. Therefore

```math
G^{(1)}_{\mu\nu}=2\partial_{[\mu}c_{\nu]},\qquad H^{(1)}_{\mu\nu\rho}=3\partial_{[\mu}b_{\nu\rho]}+\frac g2u_{\mu\nu\rho},\qquad H^{ab(1)}=-\frac1{12}\bar\varepsilon^{abcde}H^{(1)}_{cde}. \tag{3.7}
```

For the constrained potential,

```math
E^{\mu\nu(1)}=-\frac1{12}\bar\varepsilon^{\mu\nu\rho\sigma\tau}u_{\rho\sigma\tau},\qquad P^{\mu(1)}=\bar\nabla_\nu E^{\mu\nu(1)},\qquad E^{a(1)}=P^{a(1)}. \tag{3.8}
```

The last equality follows because the difference GB13 is bilinear in physical fermions. Varying the two factors $`e^{-1}`$ and $`eE^{\mu\nu}`$ in GB14 produces no extra term, since $`\bar E^{\mu\nu}=0`$. The internal curvature is $`R_{\mu\nu}^{ij}(V)^{(1)}=2\partial_{[\mu}(v'_{\nu]}{}^{ij}+\delta^{ij}v_{\nu]}/2)`$ in the local flat connection representative.

From GB09,

```math
(\mathcal D_aL^{ij})^{(1)}=\frac{\delta^{ij}}{\sqrt2}\partial_a\ell+\frac{L_0}{\sqrt2}(v'_a{}^i{}_k\delta^{jk}+v'_a{}^j{}_k\delta^{ik}),\qquad (\mathcal D_aN)^{(1)}=\partial_an. \tag{3.9}
```

The internal-connection contribution has zero contraction along $`\delta_{ij}`$: $`\delta_{ij}(v'^i{}_k\delta^{jk}+v'^j{}_k\delta^{ik})=2v'^i{}_i=2v'^{ik}\varepsilon_{ki}=0`$, since $`v'^{ik}`$ is symmetric and $`\varepsilon_{ki}`$ antisymmetric. Its linear divergence also has zero projection. The quadratic connection terms are retained for Part II, not set identically to zero in the full theory.

## 3.4 Ordered Hessians and conformal boxes

For a primary scalar of Weyl weight $`w`$, the first derivative is $`(\partial_b-wb_b)X`$ before evaluation in $`b=0`$. The given conformal transformation $`\delta_K b_b=2\Lambda_{Kb}`$ therefore implies $`\delta_K(\mathcal D_bX)=-2w\Lambda_{Kb}X`$. The outer derivative contains $`-\delta_K(f_a)`$; its contribution is consequently $`+2wf_{ab}X`$. At the relevant bosonic order,

```math
\mathcal D_a\mathcal D_bX=\nabla_a\nabla_bX+2wf_{ab}X+\text{internal-connection terms}+O(\Psi^2),\qquad \Box^cX=\nabla^2X+2wf_a{}^aX+\text{internal terms}+O(\Psi^2). \tag{3.10}
```

The internal terms for the aligned $`L`$ projection have no linear contribution by (3.9); $`N`$ and $`\sigma`$ have no internal scalar index. The weights are $`w_\sigma=1,w_L=3,w_N=4`$ (component L02 and SC7 convention ledger). Using the defining SC7-06 connection, through first order only,

```math
f_{ab}=-\frac16R_{ab}+\frac1{48}\eta_{ab}R+O(t^2),\qquad f_a{}^a=\left(-\frac16+\frac5{48}\right)R=-\frac R{16}+O(t^2). \tag{3.11}
```

This reduction follows because each additional primed-curvature term contains two odd factors. It does not impose symmetry on the original full fermionic $`f_{ab}`$.

The background value is $`\bar f_{ab}=(-4/6+20/48)k\eta_{ab}=-k\eta_{ab}/4`$. Hence

```math
\begin{aligned}
\overline{\Box^c\sigma}&=-\frac52k,&(\Box^c\sigma)^{(1)}&=-\frac18r,\qquad
\overline{\mathcal D_a\mathcal D_b\sigma}=-\frac12k\eta_{ab},\\
\frac{\delta^{ij}}{\sqrt2}\Box^cL_{ij}&=-\frac{15}{2}kL_0+t\left(\bar\Box\ell-\frac{15}{2}k\ell-\frac38L_0r\right)+O(t^2),\\
\Box^cN&=-10kN_0+t\left(\bar\Box n-10kn-\frac12N_0r\right)+O(t^2).
\end{aligned}\tag{3.12}
```

For example, the middle line is $`(\bar\Box(L_0+t\ell))-(3/8)(20k+tr)(L_0+t\ell)`$, with $`\bar\Box L_0=0`$. The last line is $`\bar\Box(N_0+tn)-(1/2)(20k+tr)(N_0+tn)`$. No conformal box was replaced by the derivative of a numerical constant.

In fixed tangent indices $`\eta`$ does not vary. The Hessian square and its first variation are

```math
\overline{(\mathcal D_a\mathcal D_b\sigma)^2}=5k^2/4,\qquad
\delta[(2f_{ab})(2f^{ab})]=8\bar f^{ab}\delta f_{ab}=8\left(-\frac k4\right)\delta(f_a{}^a)=\frac k8r. \tag{3.13}
```

Here $`\delta(f_a{}^a)=-r/16`$. This derives the contraction without making any assertion about higher-fermion-order antisymmetric components.

## 3.5 Algebraic composites and internal contractions

Set $`u=L/\sqrt2`$. NW–SE lowering gives $`L^{ij}=L_{ij}=u\delta_{ij}`$ and $`L_i{}^k=-u\varepsilon_{ik}`$. Only $`L_1{}^2=-u`$ and $`L_2{}^1=u`$ are nonzero. Therefore

```math
L^{ij}L_{ij}=u^2+u^2=L^2,\qquad
L^{ij}L_i{}^kL_j{}^lL_{kl}=u^2[(-u)^2+u^2]=2u^4=\frac12L^4. \tag{3.14}
```

In particular the quartic contraction is positive with these lowering rules. Directly from GB11 and the zero background strengths,

```math
T_{ab}^{(1)}=\frac18(G^{(1)}_{ab}-2H^{(1)}_{ab}),\qquad
D_0=-\frac58k+\frac g4N_0+\frac{g^2}{16}L_0^2,\qquad
D_1=-\frac1{32}r+\frac g4n+\frac{g^2L_0}{8}\ell . \tag{3.15}
```

Each strength-square in $`D`$ has expansion $`(tF_1)^2=t^2F_1^2`$ and contributes neither $`D_0`$ nor $`D_1`$. The Weyl curvature has $`\bar{\widehat C}_{abcd}=0`$, since the trace removal in its definition subtracts exactly $`k(\eta_{ac}\eta_{bd}-\eta_{ad}\eta_{bc})`$ from (2.2). Thus its square also starts at $`t^2`$.

## 3.6 Complete order ledger: why the unused terms have zero tadpoles

The term-by-term companion [SOURCE_TERM_LEDGER.md](SOURCE_TERM_LEDGER.md) records all 1184 higher-derivative outer terms of the accepted collected density, using the existing assembly labels solely as locators. The following calculations justify their order tags:

1. For every explicit fermion bilinear, (1.4) gives $`(0+tU_1)(0+tW_1)=t^2U_1W_1`$. Both the zeroth and first coefficients are zero, independently of any nonzero $`D_0`$, $`\Box^c\sigma_0`$ or scalar coefficient.
2. For every product containing two vanishing bosonic background tensors $`X,Y`$, substitute $`X=tX_1+O(t^2)`$ and $`Y=tY_1+O(t^2)`$: $`A(XY)=A_0t^2X_1Y_1+O(t^3)`$. The relevant zero-background factors are $`G,H,T,\widehat C,R(V),C,\mathcal D L,\nabla G,\nabla H,\nabla T,\nabla\widehat C`$. Differentiating a zero tensor background remains zero here; the conformal $`K`$ actions on its descendants multiply that tensor or its zero first descendants. A background conformal scalar Hessian is deliberately not in this list.
3. There are two special terms with only one such strength derivative. Their first coefficients vanish by an actual index contraction:

```math
\begin{aligned}
[3(\mathcal D^aG^{bc})(\mathcal D^d\mathcal D^e\sigma)\varepsilon_{abcde}]_1&=-\frac{3k}{2}\bar\nabla^aG_1^{bc}\eta^{de}\varepsilon_{abcde}=0,\\
[-6(\mathcal D^aH^{bc})(\mathcal D^d\mathcal D^e\sigma)\varepsilon_{abcde}]_1&=3k\bar\nabla^aH_1^{bc}\eta^{de}\varepsilon_{abcde}=0.
\end{aligned}\tag{3.16}
```

For both lines, exchanging $`d\leftrightarrow e`$ leaves $`\eta^{de}`$ fixed and changes the epsilon sign, so the contraction equals its negative and is zero.

The two-derivative block has no omitted linear pieces: $`\mathcal D L\mathcal D L`$, $`E^2`$, $`E\mathcal D L`$, the strength square, $`E^{\mu\nu}\mathcal D_{[\mu}(L^{-1}E_{\nu]})`$, $`E^{\mu\nu}R_{\mu\nu}(V)`$, $`E^{\mu\nu}\mathcal D L\mathcal D L`$ and $`G_{\mu\nu}E^{\mu\nu}`$ each have at least two explicitly zero background factors. Every remaining term contains a displayed odd pair. Their separate coefficients are therefore zero by the product calculation above, not by an imposed variation restriction.

The surviving two-derivative terms are obtained by contracting the first and last scalar terms inside the braces of `GB-FINAL-DENSITY`:

```math
\frac{L\delta^{ij}}{\sqrt2}L^{-1}\Box^c\left(\frac{L\delta_{ij}}{\sqrt2}\right)=\frac{\delta^{ij}}{\sqrt2}\Box^cL_{ij},\quad
\frac{L\delta^{ij}}{\sqrt2}\left(-\frac{\delta_{ij}}{\sqrt2}L^{-2}N^2\right)=-\frac{N^2}{L},\quad
(2L^{-1}N)N=\frac{2N^2}{L},\quad
\frac{L\delta^{ij}}{\sqrt2}(2\sqrt2\delta_{ij}D)=4LD. \tag{3.17}
```

Thus the inner $`N`$ terms sum to $`N^2/L`$, not $`-N^2/L`$. The exterior $`-2`$ and gauging term give the required background/linear contribution

```math
-2\frac{\delta^{ij}}{\sqrt2}\Box^cL_{ij}-8LD-\frac{2N^2}{L}-4gN+2g^2L^2. \tag{3.18}
```

Equations (3.12)–(3.18), together with the twelve scalar entries evaluated explicitly in Step 4 and Step 5, cover every possible contribution to the required action orders. They are an expansion around this background, not a replacement nonlinear bosonic action.
