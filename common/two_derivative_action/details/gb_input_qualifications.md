# Two-derivative fermionic reduction

The scalar background is $`L=1`$, $`N=-3g/2`$, $`k=-g^2/2=-1/\ell^2`$.
Fluctuation fermions are first order. The 2016 map, Eq. (3.14), gives



```math
\begin{aligned}
-i\mathcal F_{1111\,ij}{}^{kl}N\bar\varphi_k\varphi_l
={}&iNL^{-3}\bar\varphi_{(i}\varphi_{j)}\\
&-3iNL^{-5}L_{ij}L^{kl}\bar\varphi_k\varphi_l.
\end{aligned}
\tag{A3}
```

At the background, the Gold-normalized density traces this with
$`-\sqrt2\delta^{ij}`$. Both lowered spinors use epsilon in the same
order, so the resulting coefficient is

```math
-\sqrt2(iN-3iN)=2\sqrt2iN=-\frac{6ig}{\sqrt2}.
\tag{A4}
```

<a id="3-majorana-bar-the-source-convention-not-an-antilinear-replacement"></a>

## Majorana bar: the source convention, not an antilinear replacement

`Sources/2013-Proeyen-Weyl multiplets of N = 2 conformal supergravity in
five dimensions.pdf`, Appendix A, Eqs. (A.4), (A.7), (A.9), printed pp.
31–32 (PDF pp. 32–33), explicitly uses the Majorana bar:

```math
\bar\zeta^i=(\zeta^i)^TC,
\qquad C^T=-C,
\qquad (\gamma^a)^TC=C\gamma^a.
\tag{A6}
```

In particular, an external commuting coefficient is **not complex
conjugated** by this transpose. The equivalent Dirac-adjoint description
would require the full symplectic-Majorana reality conversion, not merely
replacing i by −i. For the source bar,

```math
\begin{aligned}
\overline{\zeta_i}&=\bar\zeta^j\varepsilon_{ji},\\
\overline{c\gamma_a\zeta^i}&=c\bar\zeta^i\gamma_a,\\
\overline{c\gamma_{ab}\zeta^i}&=-c\bar\zeta^i\gamma_{ab}.
\end{aligned}
\tag{A7}
```

Consequently $`\delta^{ij}\bar\alpha_i\beta_j =\delta_{ij}\bar\alpha^i\beta^j`$. The fixed-upper flip is
$`\bar\alpha^i\gamma_{(n)}\beta^j=t_n\bar\beta^j\gamma_{(n)}\alpha^i`$,
with $`t_{0,1}=1`$, $`t_{2,3}=-1`$. Contracting explicitly gives

```math
\begin{aligned}
\bar\alpha^i\gamma_{(n)}\beta_i
&=\varepsilon_{ji}\bar\alpha^i\gamma_{(n)}\beta^j\\
&=t_n\varepsilon_{ji}\bar\beta^j\gamma_{(n)}\alpha^i\\
&=-t_n\varepsilon_{ji}\bar\beta^i\gamma_{(n)}\alpha^j.
\end{aligned}
\tag{A8}
```

This last minus is from epsilon, not a changed fixed-index flip.

<a id="4-forward-correction-of-the-raw-quadratic-action"></a>

## Raw quadratic action

<a id="41-the-barred-composite-gaugino"></a>

### The barred composite gaugino

The composite gaugino’s algebraic gravitino piece is
$`-2ig\gamma^\mu\psi_{\mu i}`$. Raise before taking the source bar:

```math
\begin{aligned}
\lambda^i\big|_{g\psi}&=-2ig\gamma^\mu\psi_\mu^i,\\
\bar\lambda^i\big|_{g\psi}&=-2ig\bar\psi_\mu^i\gamma^\mu,\\
-2i\bar\lambda^i\varphi_i\big|_{g\psi\varphi}
&=(-2i)(-2ig)\bar\psi_\mu^i\gamma^\mu\varphi_i\\
&=-4g\bar\psi_\mu^i\gamma^\mu\varphi_i.
\end{aligned}
\tag{A9}
```

<a id="42-the-conformal-box-and-d-block"></a>

### The conformal-box and D block

The component curvature includes

```math
\widehat R'_{\mu\nu}{}^{ab}(M)\big|_\chi
=8\bar\psi_{[\mu}e_{\nu]}{}^{[a}\gamma^{b]}\chi.
\tag{A10}
```

Use the source Ricci contraction in Özkan–Pang Eq. (2.10), PDF p. 7.
The unit-weight antisymmetrizations give, in five dimensions,

```math
\begin{aligned}
e_a{}^\mu e_b{}^\nu
\bar\psi_{[\mu}e_{\nu]}{}^{[a}\gamma^{b]}\chi
&=\frac14(1-5-5+1)\bar\psi_a\gamma^a\chi\\
&=-2\bar\psi_a\gamma^a\chi,\\
R'\big|_\chi&=-16\bar\psi_a\gamma^a\chi,\\
f_a{}^a\big|_\chi&=+\bar\psi_a\gamma^a\chi.
\end{aligned}
\tag{A11}
```

The coefficient of f in $`-2[L_{ij}\square^CL^{ij}+4D]`$ is
$`-2(6+4/2)=-16`$. The explicit box term contributes
$`+12\bar\psi\gamma\chi`$; their sum is −4. Insert the correctly
lowered gauging piece

```math
\chi_i\big|_g
=\frac{ig}{16\sqrt2}\delta_{ij}\gamma^a\psi_a^j
+\frac g8\varphi_i.
\tag{A12}
```

The resulting three algebraic contributions, with coefficients of
$`\delta_{ij}\bar\psi_\mu^i\gamma^{\mu\nu}\psi_\nu^j`$ and
$`\delta_{ij}\bar\psi_\mu^i\psi^{\mu j}`$ measured in $`ig/\sqrt2`$,
and $`\bar\psi\gamma\varphi`$ measured in g, are:

| Density contribution | rank-two gravitino | scalar gravitino | mixed |
|---|---:|---:|---:|
| f and explicit box chi: −4 psi-bar gamma chi | −1/4 | −1/4 | −1/2 |
| explicit gauging terms in −8D | +1/4 | +3/4 | +1/2 |
| box term with D varphi, N background | 0 | +3/2 | 0 |
| **sum** | **0** | **2** | **0** |

Here $`\gamma^a\gamma^b=\gamma^{ab}+\eta^{ab}`$. All other f terms
are derivative terms at this fluxless background: the S connection has no
g-algebraic piece, and T has zero background. Adding the explicit
D-varphi triplet term gives mixed +3/2.

<a id="43-collect-all-four-density-blocks"></a>

### Collect all four density blocks

| Density block | RS mass in ig/sqrt(2) | mixed in g | spinor mass in ig/sqrt(2) |
|---|---:|---:|---:|
| traced composite Y | 0 | +3/2 | −6 |
| −2i lambda-bar varphi | 0 | −4 | +10 |
| explicit psi–lambda term | −2 | −5/2 | 0 |
| scalar rho term | +1/2 | +1 | +3 |
| **sum** | **−3/2** | **−4** | **+7** |

No auxiliary fluctuation equation, fermionic equation, or desired AdS mass
was used. The raw action is

```math
\begin{aligned}
\bar e^{-1}\mathcal L_F^{(2)}\doteq{}&
-\bar\psi_\mu^i\gamma^{\mu\nu\rho}\bar\nabla_\nu\psi_{\rho i}
+2\bar\varphi^i\not{\bar\nabla}\varphi_i\\
&+2i\sqrt2\delta_{ij}\bar\varphi^i\gamma^{\mu\nu}
\bar\nabla_\mu\psi_\nu^j\\
&-\frac{3ig}{2\sqrt2}\delta_{ij}\bar\psi_\mu^i
\gamma^{\mu\nu}\psi_\nu^j\\
&-4g\bar\psi_\mu^i\gamma^\mu\varphi_i
+\frac{7ig}{\sqrt2}\delta_{ij}\bar\varphi^i\varphi^j.
\end{aligned}
\tag{A13}
```

<a id="5-diagonalization-and-reverse-reconstruction"></a>

## Diagonalization and reverse reconstruction

Define the diagonal field:

```math
\begin{aligned}
\Psi_{\mu i}&=\psi_{\mu i}
+\frac{i\sqrt2}{3}\delta_{ij}\gamma_\mu\varphi^j,\\
\Psi_\mu^i&=\psi_\mu^i
-\frac{i\sqrt2}{3}\delta^{ij}\gamma_\mu\varphi_j,\\
\bar\Psi_\mu^i&=\bar\psi_\mu^i
-\frac{i\sqrt2}{3}\delta^{ij}\bar\varphi_j\gamma_\mu.
\end{aligned}
\tag{A14}
```

The source bar has the same displayed coefficient as the upper field.
The kinetic square gives the derivative mixing and +8/3 spinor kinetic
term. With a=i sqrt(2)/3, the mass square is

```math
\begin{aligned}
\delta_{ij}\bar\Psi_\mu^i\gamma^{\mu\nu}\Psi_\nu^j
={}&\delta_{ij}\bar\psi_\mu^i\gamma^{\mu\nu}\psi_\nu^j\\
&-8a\bar\psi_\mu^i\gamma^\mu\varphi_i
+20a^2\delta_{ij}\bar\varphi^i\varphi^j.
\end{aligned}
\tag{A15}
```

Each mixed term is −4a, from $`\gamma_\mu\gamma^{\mu\nu} =4\gamma^\nu`$ and $`\gamma^{\mu\nu}\gamma_\nu=4\gamma^\mu`$.
Their signs agree after the contracted rank-one flip. Multiplying by the
RS coefficient gives

```math
\left(-\frac{3ig}{2\sqrt2}\right)(-8a)=-4g,
\qquad
\left(-\frac{3ig}{2\sqrt2}\right)(20a^2)
=\frac{20ig}{3\sqrt2}.
\tag{A16}
```

Thus all six raw structures are reconstructed by

```math
\begin{aligned}
\bar e^{-1}\mathcal L_{F,\mathrm{diag}}^{(2)}\doteq{}&
-\bar\Psi_\mu^i\gamma^{\mu\nu\rho}\bar\nabla_\nu\Psi_{\rho i}\\
&-\frac{3ig}{2\sqrt2}\delta_{ij}\bar\Psi_\mu^i
\gamma^{\mu\nu}\Psi_\nu^j\\
&-\frac23\bar\varphi^i\not{\bar\nabla}\varphi_i
+\frac{ig}{3\sqrt2}\delta_{ij}\bar\varphi^i\varphi^j,
\end{aligned}
\tag{A17}
```

since 8/3−2/3=2 and 20/3+1/3=7.

<a id="6-equations-and-the-unchanged-mass-magnitudes"></a>

## Equations and mass magnitudes

Varying the Majorana action gives two identical contributions to each
diagonal kinetic/mass bilinear. Dividing both rows by that common two, the
original coupled equations are

```math
\begin{aligned}
0={}&-\gamma^{\mu\nu\rho}\bar\nabla_\nu\psi_{\rho i}
-i\sqrt2\delta_{ij}\gamma^{\mu\nu}\bar\nabla_\nu\varphi^j\\
&-\frac{3ig}{2\sqrt2}\delta_{ij}\gamma^{\mu\nu}\psi_\nu^j
-2g\gamma^\mu\varphi_i,\\
0={}&2\not{\bar\nabla}\varphi_i
+i\sqrt2\delta_{ij}\gamma^{\mu\nu}\bar\nabla_\mu\psi_\nu^j\\
&+2g\gamma^\mu\psi_{\mu i}
+\frac{7ig}{\sqrt2}\delta_{ij}\varphi^j.
\end{aligned}
\tag{A18}
```

These equations and (A17) are related by the transpose Jacobian of (A14),
including its spinor-transpose signs. For the fixed charge convention
$`i\delta_{ij}X^{(q)j}=-qX_i^{(q)}`$, the diagonal equations are

```math
\begin{aligned}
\gamma^{\mu\nu\rho}\bar\nabla_\nu\Psi_{\rho i}^{(q)}
-\frac{3q}{2\ell}\gamma^{\mu\nu}\Psi_{\nu i}^{(q)}&=0,\\
\left(\not{\bar\nabla}+\frac{q}{2\ell}\right)
\varphi_i^{(q)}&=0.
\end{aligned}
\tag{A19}
```

The RS gauge transformation is now
$`\delta\Psi_{\mu i}^{(q)}=(\bar\nabla_\mu+q\gamma_\mu/(2\ell)) \epsilon_i^{(q)}`$, as follows also by lowering the defining-compensator
transformation. Its derivative variation is proportional to
$`3q/(2\ell)-3q/(2\ell)=0`$; its remaining two terms are
$`+3\gamma^\mu\epsilon/\ell^2`$ and
$`-3\gamma^\mu\epsilon/\ell^2`$.

The local mass magnitudes and dimensions are:

| Field | Action mass | Standard AdS dimension | Local DoF |
|---|---|---|---:|
| graviton | massless | 4 | 5 |
| scalar | m² ell²=−4 | 2 | 1 |
| Maxwell vector | massless | 3 | 3 |
| two-form | massless | 2 (potential boundary data) | 3 |
| gravitino | abs(m ell)=3/2, massless gauge system | 7/2 | 8 |
| spinor | abs(m ell)=1/2 | 5/2 | 4 |

The two-form's Maxwell-dual boundary interpretation must be specified when
using the current-multiplet label. The labels are an output consistency
check, not a substitute for a boundary-condition or norm calculation.
