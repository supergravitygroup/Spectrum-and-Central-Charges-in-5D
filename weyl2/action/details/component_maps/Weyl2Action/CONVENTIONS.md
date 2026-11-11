# Conventions: Özkan–Pang, equation (5.8)

<a id="1-source-equations-and-scope"></a>

## Source equations and scope

The sole physical source for this file is the source
[welySquared.pdf](https://arxiv.org/abs/1301.6622):
Mehmet Ozkan and Yi Pang, *Supersymmetric Completion of Gauss-Bonnet
Combination in Five Dimensions*, identified in the PDF as arXiv:1301.6622v4,
8 July 2013. Equation and page numbers below refer to that PDF.
Reference [26] in its bibliography and other external sources are not
used as separate component inputs here. The PDF's bibliography does not specify
use of those sources' formulas.

The component inputs below concern the fermionic terms of the composite
linear multiplet built from Weyl-multiplet fields in (5.8). The source
formulas and the individually checked corrections have distinct scopes.

- The map is treated in the source superconformal variables. Gauge conditions
  (4.1) are recorded as context and are not automatically imposed on the map.
- The theory remains complete and off shell. No EOM, auxiliary-field
  elimination, field truncation, or fermion-order truncation is applied.
- Definitions explicitly given in the paper are distinguished from algebraic
  deductions. Identified typographical issues are recorded in Section 11.
- The earlier gauged parent action, two-derivative ansatz, alternative-frame
  sign conversions, and overall factor of two are not inputs here.
- Composite-field equalities are local. A total derivative cannot be dropped
  from a map component; integration by parts inside an integral is distinct.

<a id="2-fields-and-meanings-of-symbols"></a>

## Fields and meanings of symbols

According to Section 2.1 and Appendix B, the source fields of the
Dilaton Weyl multiplet are

```math
(e_\mu{}^a,\psi_\mu^i,b_\mu,V_\mu^{ij},C_\mu,B_{\mu\nu},\sigma,\psi^i)
```

In this multiplet, $`T_{ab},\chi^i,D`$ are the composite fields of (2.9)–(2.10).
The paper separately explains that they are independent in the
Standard Weyl multiplet; the two uses must not be confused.

The $`(L^{ij},\varphi^i,E_a,N)`$ in (5.8) form a composite linear multiplet built from these
Weyl fields. They are not identified with the independent compensator
multiplet in Section 4 merely because they use the same letters.
If both multiplets occur in one calculation, the parent multiplet
of each component must be specified.

| Symbol | Meaning |
|---|---|
| $`\psi_\mu^i`$ | Gravitino |
| $`\psi^i`$ | Dilatino; distinct from the gravitino |
| $`\chi^i`$ | Composite Weyl fermion in (2.9) |
| $`\varphi^i`$ | Linear-multiplet fermion |
| $`\phi_\mu^i`$ | Dependent $`S`$-supersymmetry connection in (2.5) |
| $`D`$ | Scalar component of the Weyl multiplet |
| $`\mathcal D_\mu`$ | Source supercovariant derivative |
| $`C_\mu`$ | One-form of the Dilaton Weyl multiplet |
| $`C_{abcd},\widehat C_{abcd}`$ | Ordinary and supercovariant Weyl curvatures |
| $`V_\mu^{ij}`$ | Full $`SU(2)`$ connection |
| $`V_{\mu\nu}^{ij},\widehat R_{\mu\nu}^{ij}(V)`$ | Ordinary and supercovariant internal curvatures |

$`\epsilon^i`$ and $`\eta^i`$ are the transformation parameters of $`Q`$ and $`S`$,
respectively. The paper's $`\Lambda`$ is used for the one-form gauge parameter
and must be distinguished from $`\eta^i`$.

<a id="3-dimension-indices-metric-and-density"></a>

## Dimension, indices, metric and density

With Appendix A and the field notation used,

```math
D_{\rm spacetime}=5,\qquad
\eta_{ab}=\mathop{\mathrm{diag}}\nolimits(-,+,+,+,+),\qquad
\mu,\nu,a,b=0,\ldots,4,\qquad i,j=1,2.
```

$`\mu,\nu`$ are coordinate indices; $`a,b`$ are tangent indices. The dimension here must not be confused with the scalar field $`D`$.

```math
g_{\mu\nu}=e_\mu{}^ae_\nu{}^b\eta_{ab},\qquad
X_a=e_a{}^\mu X_\mu,\qquad
X^a=e_\mu{}^aX^\mu.
```

All form and curvature indices are converted using the same vielbein. The density notation is

```math
e=\det(e_\mu{}^a)=\sqrt{-g},\qquad
S=\int d^5x\,\mathcal L
=\int d^5x\,e\,(e^{-1}\mathcal L)
```

Here $`e^{-1}\mathcal L`$ is generally the scalar Lagrangian; it does not mean only the bosonic two-derivative sector.

The Einstein term in (4.4) is $`\tfrac12 LR`$. The paper's densities and the
components of (5.8) retain source coefficients; the earlier overall
factor of two is not applied. Footnote 3 on p. 14 is also relevant to
the overall sign between (3.5) and (4.4); it is not a rule for uniformly
redefining multiplet fields.

<a id="4-antisymmetrization-clifford-algebra-and-spinor-operations"></a>

## Antisymmetrization, Clifford algebra and spinor operations

Unit-weight (anti)symmetrization and Clifford notation:

```math
X_{[ab]}=\frac12(X_{ab}-X_{ba}),\qquad
X_{(ab)}=\frac12(X_{ab}+X_{ba}),
```

```math
\{\gamma^a,\gamma^b\}=2\eta^{ab},\qquad
\gamma^{a_1\ldots a_n}=\gamma^{[a_1}\cdots\gamma^{a_n]}.
```

Dot and slash denote full contraction:

```math
\gamma\!\cdot\!X=\gamma^{a_1\ldots a_p}X_{a_1\ldots a_p},\qquad
\mathord{\not{X}}=\gamma^aX_a,\qquad
\mathord{\not{\mathcal D}}=\gamma^a\mathcal D_a.
```

No $`1/p!`$ is added to the dot contraction. Equation (A.7) explicitly gives

```math
\gamma^{abcde}=i\varepsilon^{abcde}\mathbf1
```

Its Clifford-algebra-equivalent duality form is

```math
\gamma^{a_1\ldots a_r}
=\frac{i}{(5-r)!}\varepsilon^{a_1\ldots a_5}
 \gamma_{a_5\ldots a_{r+1}}
```

The reversed order of the gamma indices on the right is retained.

NW–SE convention in (A.1)–(A.2):

```math
\epsilon_{12}=\epsilon^{12}=1,\qquad
\epsilon_{ij}=-\epsilon_{ji},\qquad
X^i=\epsilon^{ij}X_j,\qquad X_i=X^j\epsilon_{ji},
```

```math
\epsilon^{ij}\epsilon_{kj}=\delta^i{}_k,\qquad
\bar X\Gamma Y=\bar X^i\Gamma Y_i.
```

For symmetric $`L_{ij}`$, these rules yield

```math
L^{ij}=\epsilon^{ik}\epsilon^{j\ell}L_{k\ell},\qquad
L_i{}^j=\epsilon^{jk}L_{ik},\qquad
L^i{}_j=\epsilon^{ik}L_{kj}
```

Changing the position of a contracted $`SU(2)`$ pair produces a sign:

```math
\bar X^i\Gamma Y_i=-\bar X_i\Gamma Y^i.
```

The open-index flip in (A.4) and the Fierz relation in (A.5) are:

```math
\bar X^i\gamma_{(n)}Y^j=t_n\bar Y^j\gamma_{(n)}X^i,
\qquad t_0=t_1=+1,\quad t_2=t_3=-1,
```

```math
\psi_j\bar\lambda^i
=-\frac14(\bar\lambda^i\psi_j)\mathbf1
 -\frac14(\bar\lambda^i\gamma^a\psi_j)\gamma_a
 +\frac18(\bar\lambda^i\gamma^{ab}\psi_j)\gamma_{ab}.
```

The NW–SE-contracted flip follows directly from the same rules:

```math
\begin{aligned}
\bar X^i\gamma_{(n)}Y_i
&=\epsilon_{ji}\bar X^i\gamma_{(n)}Y^j\\
&=t_n\epsilon_{ji}\bar Y^j\gamma_{(n)}X^i
=-t_n\bar Y^j\gamma_{(n)}X_j.
\end{aligned}
```

For ranks 4 and 5, $`t_4=t_5=+1`$ follows from (A.7) by reduction to ranks 1
and 0, respectively. Grassmann signs remain consistent with these
flip/Fierz rules; fermions are not exchanged as commuting objects.

The cited PDF gives no explicit $`C`$ matrix, Dirac-bar phase,
or detailed complex-conjugation definition. Bar operations here use
(A.2), (A.4), and (A.5). No external bar/phase definition is imported;
any conjugation needed beyond these identities requires the missing
input to be identified separately.

<a id="5-epsilon-forms-and-field-strengths"></a>

## Epsilon, forms and field strengths

According to (A.6), epsilon is real and, for $`n+p=5`$,

```math
\varepsilon_{a_1\ldots a_n b_1\ldots b_p}
\varepsilon^{a_1\ldots a_n c_1\ldots c_p}
=-n!p!\,\delta_{[b_1}^{c_1}\cdots\delta_{b_p]}^{c_p}.
```

The PDF does not specify a numerical value for $`\varepsilon^{01234}`$. This file does
not attribute a numerical orientation choice to it; epsilon and gamma
matrices remain symbolic under (A.6)–(A.7).

To distinguish the coordinate epsilon tensor from the density symbol, this file writes

```math
\varepsilon^{\mu\nu\rho\sigma\lambda}
=e_a{}^\mu e_b{}^\nu e_c{}^\rho e_d{}^\sigma e_e{}^\lambda
 \varepsilon^{abcde},\qquad
\epsilon^{\mu\nu\rho\sigma\lambda}
=e\,\varepsilon^{\mu\nu\rho\sigma\lambda}
```

The second object is a density symbol; if used in place of the tensor, the factor $`e^{-1}`$ is retained explicitly. This distinction introduces no new physical normalization.

The ordinary field strengths below (2.3) are

```math
G_{\mu\nu}=2\partial_{[\mu}C_{\nu]},\qquad
H_{\mu\nu\rho}=3\partial_{[\mu}B_{\nu\rho]}
 +\frac32C_{[\mu}G_{\nu\rho]}
```

and the gauge transformations in (2.4) are

```math
\delta C_\mu=\partial_\mu\Lambda,\qquad
\delta B_{\mu\nu}=2\partial_{[\mu}\Lambda_{\nu]}
 -\frac12\Lambda G_{\mu\nu}
```

No $`gE_{\mu\nu\rho}`$ is added to this ungauged supergravity definition.
The coupling of the separate Yang–Mills sector in Section 2.2
is not an input for such a term.

Full source supercovariant field strengths, (2.3):

```math
\begin{aligned}
\widehat G_{\mu\nu}
&=G_{\mu\nu}-\bar\psi_{[\mu}\gamma_{\nu]}\psi
 +\frac{i}{2}\sigma\bar\psi_{[\mu}\psi_{\nu]},\\
\widehat H_{\mu\nu\rho}
&=H_{\mu\nu\rho}
 -\frac34\sigma^2\bar\psi_{[\mu}\gamma_\nu\psi_{\rho]}
 -\frac{3i}{2}\sigma\bar\psi_{[\mu}\gamma_{\nu\rho]}\psi.
\end{aligned}
```

$`H`$ denotes a three-form, not a normalized two-form dual. $`H_\mu{}^{ab}`$ is not a two-form dual
but $`e^{a\nu}e^{b\rho}H_{\mu\nu\rho}`$; its hatted counterpart uses the same pullback.

<a id="6-weyl-weights-and-derivatives"></a>

## Weyl weights and derivatives

$`w`$ denotes the source Weyl weight. Weights explicitly supplied
in Appendix B are distinguished from those following from
(2.3), (2.6), and (2.9):

| Object | $`w`$ | Basis |
|---|---:|---|
| $`e_\mu{}^a`$ | $`-1`$ | Appendix B |
| $`\psi_\mu^i`$ | $`-1/2`$ | Appendix B |
| $`b_\mu,V_\mu^{ij},C_\mu,B_{\mu\nu}`$ | $`0`$ | Appendix B |
| $`\sigma,\rho`$ | $`1`$ | Appendix B |
| $`\psi^i,\lambda^i`$ | $`3/2`$ | Appendix B |
| $`Y^{ij}`$ | $`2`$ | Appendix B |
| $`L^{ij}`$ | $`3`$ | Appendix B |
| $`\varphi^i`$ | $`7/2`$ | Appendix B |
| $`E_a,N`$ | $`4`$ | Appendix B |
| $`T_{ab},\chi^i,D`$ | $`1,3/2,2`$ | (2.9), check below |
| $`\widehat G_{ab},\widehat R_{ab}^{ij}(V),\widehat C_{abcd}`$ | $`2`$ | Definitions and tangent indices |
| $`\widehat R_{ab}^i(Q)`$ | $`3/2`$ | (2.6) and tangent indices |

Since $`w(e_a{}^\mu)=1`$, a tangent derivative increases the weight by one.
For example, $`\widehat G_{\mu\nu}`$ has weight zero, while $`\widehat G_{ab}=e_a{}^\mu e_b{}^\nu\widehat G_{\mu\nu}`$ has weight two.
Source Weyl weights are distinct from Poincaré derivative counting.

$`\mathcal D_\mu`$ is the full supercovariant derivative. $`\partial_\mu`$ is not identical
to $`\nabla_\mu`$ with only a Lorentz connection, a derivative containing only
the residual $`U(1)`$ connection, or a purely bosonic gauge-covariant
derivative. The source gives the connection part of a doublet as

```math
\left(\partial_\mu-wb_\mu+\frac14\omega_\mu{}^{ab}\gamma_{ab}\right)X^i
 -V_\mu^{ij}X_j
```

Its supercovariant completion depends on the field's own transformation. This expression alone is not the full definition of $`\mathcal D_\mu X^i`$.

For example, (2.2) and (2.19):

```math
\mathcal D_\mu\sigma=(\partial_\mu-b_\mu)\sigma
 -\frac{i}{2}\bar\psi_\mu\psi,
```

```math
\mathcal D_\mu L^{ij}
=(\partial_\mu-3b_\mu)L^{ij}
 +2V_\mu^{(i}{}_kL^{j)k}
 -i\bar\psi_\mu^{(i}\varphi^{j)}.
```

The working definition of the $`T`$ derivative in (2.12) used in this
project, with the Lorentz-connection sign verified in Section 11.5, is

```math
\mathcal D_\mu T_{ab}
=\partial_\mu T_{ab}-b_\mu T_{ab}
 +2\omega_\mu{}^c{}_{[a}T_{b]c}
 -\frac{i}{2}\bar\psi_\mu\gamma_{ab}\chi
 +\frac{3i}{32}\bar\psi_\mu\widehat R_{ab}(Q).
```

With the same index order, the PDF prints the Lorentz term as $`-2\omega_\mu{}^c{}_{[a}T_{b]c}`$;
that printed sign is not used in the working definition. The source
expression and two independent internal-consistency checks are
retained in Section 11.5.

The working coefficient for $`\mathcal D_\mu\chi^i`$ is $`-\tfrac32b_\mu\chi^i`$. Its difference from
the printed $`-\tfrac72b_\mu\chi^i`$ in (2.12) is shown in Section 11.1. Printed formulas
are distinguished from the working definitions established through
these internal-consistency checks.

<a id="7-connections-and-curvature-distinctions"></a>

## Connections and curvature distinctions

Spin connection, (2.5):

```math
\begin{aligned}
\omega_\mu{}^{ab}
={}&2e^{\nu[a}\partial_{[\mu}e_{\nu]}{}^{b]}
 -e^{\nu[a}e^{b]\rho}e_{\mu c}\partial_\nu e_\rho{}^c
 +2e_\mu{}^{[a}b^{b]}\\
&+\frac12\bar\psi^{[a}\gamma^{b]}\psi_\mu
 +\frac14\bar\psi^a\gamma_\mu\psi^b,\\
\psi^a&=e^{a\mu}\psi_\mu,\qquad b^a=e^{a\mu}b_\mu.
\end{aligned}
```

$`\omega_\mu{}^{ab}`$ is dependent; it is not held as an independent, unchanged connection during calculation. The dilatino condition $`\psi^i=0`$ does not set gravitino contorsion to zero.

The $`Q`$ curvature in (2.5)–(2.6) is:

```math
\begin{aligned}
\widehat R_{\mu\nu}^{\prime\,i}(Q)
={}&2\partial_{[\mu}\psi_{\nu]}^i
 +\frac12\omega_{[\mu}{}^{ab}\gamma_{ab}\psi_{\nu]}^i
 +b_{[\mu}\psi_{\nu]}^i-2V_{[\mu}^{ij}\psi_{\nu]j}
 +2i\gamma\!\cdot\!T\gamma_{[\mu}\psi_{\nu]}^i,\\
\phi_\mu^i
={}&\frac{i}{3}\gamma^a\widehat R_{\mu a}^{\prime\,i}(Q)
 -\frac{i}{24}\gamma_\mu\gamma^{ab}\widehat R_{ab}^{\prime\,i}(Q),\\
\widehat R_{\mu\nu}^i(Q)
={}&\widehat R_{\mu\nu}^{\prime\,i}(Q)-2i\gamma_{[\mu}\phi_{\nu]}^i.
\end{aligned}
```

The prime here removes the $`\phi_\mu^i`$ contribution. For $`\widehat R'(M)`$ in (2.10),
the prime removes the $`f_\mu{}^a`$ contribution.

Ordinary Lorentz curvature and Ricci contraction:

```math
\begin{aligned}
R_{\mu\nu}{}^{ab}(\omega)
&=2\partial_{[\mu}\omega_{\nu]}{}^{ab}
 +2\omega_{[\mu}{}^{ac}\omega_{\nu]c}{}^b,\\
R_{abcd}(\omega)&=e_a{}^\mu e_b{}^\nu R_{\mu\nu cd}(\omega),\\
R_{bd}(\omega)&=\eta^{ac}R_{abcd}(\omega),\qquad
R(\omega)=\eta^{bd}R_{bd}(\omega).
\end{aligned}
```

The Lorentz curvature used here is not copied directly from (2.7);
it is the supercovariant completion of the connection transformation
calculated from (2.1), (2.5), and (2.6). With the index order below,
the working sign of the explicit $`\chi`$ term is **$`+8`$**. Its difference
from the printed $`-8`$ and its effect on the dependent $`f_\mu{}^a`$ connection
are shown in Section 11.4.

```math
\begin{aligned}
\widehat R'_{\mu\nu}{}^{ab}(M)
={}&R_{\mu\nu}{}^{ab}(\omega)
 +i\bar\phi_{[\mu}\gamma^{ab}\psi_{\nu]}
 +i\bar\psi_{[\mu}\gamma^{[a}\gamma\!\cdot\!T\gamma^{b]}\psi_{\nu]}\\
&+\bar\psi_{[\mu}\gamma^{[a}\widehat R_{\nu]}{}^{b]}(Q)
 +\frac12\bar\psi_{[\mu}\gamma_{\nu]}\widehat R^{ab}(Q)
 +8\bar\psi_{[\mu}e_{\nu]}{}^{[a}\gamma^{b]}\chi,\\
\widehat R_{\mu\nu}{}^{ab}(M)
={}&\widehat R'_{\mu\nu}{}^{ab}(M)
 +8f_{[\mu}{}^{[a}e_{\nu]}{}^{b]},\\
\widehat R_\mu{}^a(Q)&=e^{a\nu}\widehat R_{\mu\nu}(Q).
\end{aligned}
```

$`i\bar\psi_{[\mu}\gamma^{ab}\psi_{\nu]}`$ vanishes identically and therefore does not appear separately above (Section 11.2). Hatted curvatures and composite fields retain their full definitions; this notation is not a fermion-order truncation.

The algebraic form of the dependent-connection definition in (2.10) is retained:

```math
R_{\mu\nu}=\widehat R'_{\mu\rho}{}^{ab}(M)e_b{}^\rho e_{\nu a},
\qquad R=R_\mu{}^\mu,\qquad
f_\mu{}^a=-\frac16R_\mu{}^a+\frac1{48}e_\mu{}^aR.
```

The $`R_{\mu\nu}`$ in the final line comes from the supercovariant $`\widehat R'(M)`$;
it is not identified with ordinary $`R_{\mu\nu}(\omega)`$ in the presence of fermions.
Here $`\widehat R'(M)`$ is the working expression above with sign $`+8`$. A $`f_\mu{}^a`$
calculated from the printed $`-8`$ expression cannot be inserted unchanged;
the conversion is given in Section 11.4. The bosonic contraction order
agrees with $`R_{bd}=\eta^{ac}R_{abcd}`$ above. No Ricci sign from another paper is imported.

Ordinary internal curvature (5.13) and its supercovariant counterpart (2.7):

```math
\begin{aligned}
V_{\mu\nu}^{ij}
&=2\partial_{[\mu}V_{\nu]}^{ij}
 -2V_{[\mu}^{k(i}V_{\nu]k}{}^{j)},\\
\widehat R_{\mu\nu}^{ij}(V)
&=V_{\mu\nu}^{ij}
 -3i\bar\phi_{[\mu}^{(i}\psi_{\nu]}^{j)}
 -8\bar\psi_{[\mu}^{(i}\gamma_{\nu]}\chi^{j)}
 -i\bar\psi_{[\mu}^{(i}\gamma\!\cdot\!T\psi_{\nu]}^{j)}.
\end{aligned}
```

The conventional curvature condition in (5.2),

```math
e_b{}^\nu\widehat R_{\mu\nu}{}^{ab}(M)=0
```

and the notation introduced after (5.3),

```math
\widehat C_{\mu\nu\rho\sigma}
=e_{\rho a}e_{\sigma b}\widehat R_{\mu\nu}{}^{ab}(M)
```

are retained. The ordinary Weyl tensor (5.3) is:

```math
\begin{aligned}
C_{\mu\nu\rho\sigma}
={}&R_{\mu\nu\rho\sigma}
 -\frac13(g_{\mu\rho}R_{\nu\sigma}-g_{\nu\rho}R_{\mu\sigma}
          -g_{\mu\sigma}R_{\nu\rho}+g_{\nu\sigma}R_{\mu\rho})\\
&+\frac1{12}(g_{\mu\rho}g_{\nu\sigma}-g_{\mu\sigma}g_{\nu\rho})R.
\end{aligned}
```

Merely adding hats to this bosonic formula does not derive the fermionic
expansion of the full $`\widehat C`$. The vanishing bilinear in printed (2.7)
is checked in Section 11.2; the explicit $`\chi`$ sign and its joint
treatment with $`f`$ are checked in Section 11.4.

<a id="8-source-rules-for-the-linear-multiplet"></a>

## Source rules for the linear multiplet

The $`Q`$ and $`S`$ transformations against which map components
are compared are (2.18):

```math
\begin{aligned}
\delta L^{ij}&=i\bar\epsilon^{(i}\varphi^{j)},\\
\delta\varphi^i
&=-\frac{i}{2}\mathord{\not{\mathcal D}}L^{ij}\epsilon_j
 -\frac{i}{2}\gamma^aE_a\epsilon^i+\frac12N\epsilon^i
 -\gamma\!\cdot\!T L^{ij}\epsilon_j+3L^{ij}\eta_j,\\
\delta E_a
&=-\frac{i}{2}\bar\epsilon\gamma_{ab}\mathcal D^b\varphi
 -2\bar\epsilon\gamma^b\varphi T_{ba}
 -2\bar\eta\gamma_a\varphi,\\
\delta N
&=\frac12\bar\epsilon\mathord{\not{\mathcal D}}\varphi
 +\frac{3i}{2}\bar\epsilon\gamma\!\cdot\!T\varphi
 +4i\bar\epsilon^i\chi^jL_{ij}
 +\frac{3i}{2}\bar\eta\varphi.
\end{aligned}
```

For $`\mathcal D_\mu\varphi^i`$ and $`\mathcal D_\mu E_a`$, the fermionic completions in (2.19) are retained.
In the tensor notation of (2.20)–(2.22),

```math
\mathcal D^aE_a=0,\qquad
E^\mu=-\frac1{12}\varepsilon^{\mu\nu\rho\sigma\lambda}
                  \mathcal D_\nu E_{\rho\sigma\lambda},\qquad
\delta E_{\mu\nu\rho}=3\partial_{[\mu}\Lambda_{\nu\rho]}.
```

When the density symbol is used, the second equality becomes

```math
E^a=-\frac1{12}e_\mu{}^a e^{-1}
 \epsilon^{\mu\nu\rho\sigma\lambda}\mathcal D_\nu E_{\rho\sigma\lambda}
```

$`E_{\mu\nu\rho}`$ is not counted as a second independent linear-multiplet component. $`\mathcal D E_3`$ is not replaced by ordinary $`\partial E_3`$.

<a id="9-gauge-conditions-and-scope-of-the-torsionful-connection"></a>

## Gauge conditions and scope of the torsionful connection

The conditions in the paper's (4.1) are

```math
L_{ij}=\frac{L}{\sqrt2}\delta_{ij},\qquad
\sigma=1,\qquad \psi^i=0,\qquad b_\mu=0
```

They are not automatically imposed on this file's superconformal map
inputs. In particular, the first condition does not instruct the use
of the composite $`L_{ij}`$ in (5.8) as an independent compensator
for gauge fixing.

In (4.5),

```math
V_\mu^{ij}=V_\mu^{\prime\,ij}+\frac12\delta^{ij}V_\mu,
\qquad V_\mu^{\prime\,ij}\delta_{ij}=0.
```

By the NW–SE rule, the full connection acts on a doublet as

```math
\begin{aligned}
-V_\mu^{ij}X_j
&=-V_\mu^{\prime\,ij}X^k\epsilon_{kj}
  -\frac12V_\mu\delta^{ij}X_j\\
&=+V_\mu^{\prime\,ij}\epsilon_{jk}X^k
  -\frac12V_\mu\delta^{ij}X_j
=+V_\mu^{\prime\,i}{}_kX^k-\frac12V_\mu\delta^{ij}X_j.
\end{aligned}
```

The torsionful connection in (4.7) is exactly

```math
\boxed{\omega_{\pm\mu}{}^{ab}
 =\omega_\mu{}^{ab}\pm\widehat H_\mu{}^{ab}}
```

The hat is retained here. In the gauge specified in (4.9)–(4.10),

```math
\widehat G_{\mu\nu}=G_{\mu\nu}+\frac{i}{2}\bar\psi_{[\mu}\psi_{\nu]},
\qquad
\widehat H_{\mu\nu\rho}
=H_{\mu\nu\rho}-\frac34\bar\psi_{[\mu}\gamma_\nu\psi_{\rho]}.
```

Thus, its difference from the connection constructed using ordinary $`H`$ is

```math
(\omega_\mu{}^{ab}\pm\widehat H_\mu{}^{ab})
 -(\omega_\mu{}^{ab}\pm H_\mu{}^{ab})
=\mp\frac34e^{a\nu}e^{b\rho}\bar\psi_{[\mu}\gamma_\nu\psi_{\rho]}
```

Equality between bosonic expressions is not promoted to full fermionic equality.

Gauge-preserving parameters appear in (4.3), transformations in (4.6);
the paper states that cubic fermion terms are omitted from that presentation.
Equation (4.11) in Section 4.3 is presented as complete rules for the
specified Weyl-field set, without imposing $`SU(2)`$ there. These different
scopes do not constitute one complete gauge-fixed transformation system
for the whole multiplet.

<a id="10-normalization-and-completeness-limit-of-58"></a>

## Normalization and completeness limit of (5.8)

The $`L^{ij}`$ and $`\varphi^i`$ expressions in (5.8) are initial map data.
Their fermion order cannot be classified without counting fermions
inside supercovariant objects. The `fermions` at the ends of the $`E_a`$
and $`N`$ lines denotes contributions not explicitly supplied.
Until those are completed, (5.8) is not used as a full fermionic map.

In particular, the displayed $`N`$ component of (5.8) contains

```math
N\supset\frac18C_{abcd}C^{abcd}+\frac{64}{3}D^2,
\qquad
\frac{64/3}{1/8}=\frac{512}{3}.
```

The $`512/3`$ in (5.6) is this relative coefficient. The sentence suppressing
normalization at the beginning of Section 5.1 does not justify changing
the $`64/3`$ coefficient in $`N`$ to $`512/3`$. The same coefficient pair
$`1/8,64/3`$ appears in (5.12).

Notation in (5.9):

```math
T^2=T_{ab}T^{ab},\qquad
T^4=T_{ab}T^{bc}T_{cd}T^{da},\qquad
(T^2)^2=(T_{ab}T^{ab})^2.
```

Referral on p. 19 to another source for the $`Q`$ and $`S`$ curvature
transformations does not import data from that source into this file.
If a required transformation is later derived from the PDF's own
definitions, it must be shown as a separate calculation rather than
assumed as an available verified input.

<a id="11-typographical-and-consistency-checks-using-only-the-pdf"></a>

## Typographical and consistency checks using only the PDF

This section checks the specific expressions below; it does not claim
that all equations in the paper are free of typographical errors.

<a id="111-dilatation-coefficient-in-212"></a>

### Dilatation coefficient in (2.12)

The printed expression for $`\mathcal D_\mu\chi^i`$ contains $`-\tfrac72b_\mu\chi^i`$. However,
Appendix B and the five monomials of (2.9) together give

```math
\begin{aligned}
w(\sigma^{-1}\mathord{\not{\mathcal D}}\psi^i)&=-1+1+\frac32=\frac32,\\
w(\sigma^{-2}\mathord{\not{\mathcal D}}\sigma\,\psi^i)&=-2+2+\frac32=\frac32,\\
w(\sigma^{-2}\gamma\!\cdot\!\widehat G\psi^i)&=-2+2+\frac32=\frac32,\\
w(\sigma^{-1}\gamma\!\cdot\!T\psi^i)&=-1+1+\frac32=\frac32,\\
w(\sigma^{-3}\psi_j\bar\psi^i\psi^j)&=-3+3\left(\frac32\right)=\frac32
\end{aligned}
```

Also, $`w(T)=1`$ follows from the respective weights $`-2+1+2`$, $`-2+3`$, and $`-2+3`$
of the $`\sigma^{-2}\sigma\widehat G_{ab}`$, $`\sigma^{-2}\widehat H_{abc}`$, and $`\sigma^{-2}\bar\psi\gamma_{ab}\psi`$ terms in (2.9).
The $`\sigma^{-2}\widehat G^2`$ term of $`D`$ in (2.9) gives $`w(D)=-2+4=2`$.

The connection-sign and weight rule in (2.2), (2.15), and (2.19)
is $`\partial_\mu-wb_\mu`$, so the consistent result is

```math
\boxed{w(\chi^i)=\frac32,\qquad
\left.\mathcal D_\mu\chi^i\right|_{b_\mu}
=-\frac32b_\mu\chi^i.}
```

The working coefficient in this file is this internal-consistency result;
it is not claimed that the PDF actually prints $`3/2`$. For $`\varphi^i`$,
$`7/2`$ agrees with Appendix B and (2.19). No other paper or different
definition of $`\chi`$ is used here.

<a id="112-the-ibarpsi_mugammaabpsi_nu-term-appearing-in-27"></a>

### The $`i\bar\psi_{[\mu}\gamma^{ab}\psi_{\nu]}`$ term appearing in (2.7)

The PDF prints this term. By $`t_2=-1`$ in (A.4) and the NW–SE contraction,

```math
\bar\psi_\mu\gamma^{ab}\psi_\nu
=-t_2\bar\psi_\nu\gamma^{ab}\psi_\mu
=\bar\psi_\nu\gamma^{ab}\psi_\mu,
```

```math
i\bar\psi_{[\mu}\gamma^{ab}\psi_{\nu]}
=\frac{i}{2}\left(\bar\psi_\mu\gamma^{ab}\psi_\nu
                  -\bar\psi_\nu\gamma^{ab}\psi_\mu\right)=0.
```

This printed term vanishes under the source rules. An incorrect Weyl
weight alone does not establish a missing $`\phi_\mu`$ term, and no guessed
bilinear is substituted for it.

<a id="113-the-deltawidehat-h_abc-expression-in-28"></a>

### The $`\delta\widehat H_{abc}`$ expression in (2.8)

The printed second term is

```math
\frac{3i}{2}\bar\epsilon\gamma_{[ab}\mathcal D_{c]}\psi
```

with no preceding $`\sigma`$. From Appendix B and (2.1),

```math
w(\epsilon)=w(\sigma)-w(\psi)=1-\frac32=-\frac12,
\qquad w(\widehat H_{abc})=3,
```

whereas for this printed term,

```math
w(\bar\epsilon\gamma_{[ab}\mathcal D_{c]}\psi)
=-\frac12+1+\frac32=2.
```

The first term of the same line has

```math
w(\sigma^2\bar\epsilon\gamma_{[a}\widehat R_{bc]}(Q))
=2-\frac12+\frac32=3
```

this weight. Thus the printed $`\delta\widehat H_{abc}`$ formula in (2.8) is not homogeneous
at this point. A $`\sigma`$ factor could restore the weight, but the weight
check alone does not prove the full variation. This file does not accept
the conjectured correction as a transformation rule. If needed, the full
variation must be derived separately from (2.1)–(2.3); until then,
the printed line is not used as a verified complete input.

<a id="114-explicit-chi-term-in-the-calculated-rm-and-the-dependent-f-connection"></a>

### Explicit $`\chi`$ term in the calculated $`R(M)`$ and the dependent $`f`$ connection

This derivation calculates
$`R(M)`$ rather than copy the printed formula. Inputs are exclusively
(2.1), (2.5), (2.6), (2.10), and (5.2) of the cited PDF; [26] was
not used. The printed $`-8`$ coefficient in (2.7) was not an input.
This sign calculation is separate from the $`-\tfrac72b_\mu\chi^i\to-\tfrac32b_\mu\chi^i`$ correction
in Section 11.1.

The $`b_\mu`$ dependence of (2.5) and transformation in (2.1) are:

```math
\left.\omega_\mu{}^{ab}\right|_b=2e_\mu{}^{[a}b^{b]},\qquad
\left.\delta_Qb_\mu\right|_\chi=-2\bar\epsilon\gamma_\mu\chi,
```

```math
\left.\delta_Q\omega_\mu{}^{ab}\right|_{\bar\epsilon\chi}
=2e_\mu{}^{[a}e^{b]\nu}
 (-2\bar\epsilon\gamma_\nu\chi)
=-4e_\mu{}^{[a}\bar\epsilon\gamma^{b]}\chi.
```

The operation $`\left.\vphantom{X}\right|_{\partial\epsilon}`$ below selects the derivative coefficient of the independent local parameter; it is not a field or fermion-order truncation. Variation of the ordinary curvature:

```math
\begin{aligned}
\left.\delta_QR_{\mu\nu}{}^{ab}(\omega)
\right|_{\partial\epsilon\,\chi}
&=\left.2\partial_{[\mu}
 \left(-4e_{\nu]}{}^{[a}\bar\epsilon\gamma^{b]}\chi\right)
 \right|_{\partial\epsilon}\\
&=-8(\partial_{[\mu}\bar\epsilon)
       e_{\nu]}{}^{[a}\gamma^{b]}\chi.
\end{aligned}
```

Using $`\left.\delta_Q\bar\psi_\mu\right|_{\partial\epsilon} =\partial_\mu\bar\epsilon`$, for the temporary coefficient $`c`$ of the completing term

```math
\begin{aligned}
\left.\delta_Q
 \left(c\bar\psi_{[\mu}e_{\nu]}{}^{[a}\gamma^{b]}\chi\right)
 \right|_{\partial\epsilon}
&=c(\partial_{[\mu}\bar\epsilon)e_{\nu]}{}^{[a}\gamma^{b]}\chi,\\
-8+c&=0\quad\Longrightarrow\quad c=+8.
\end{aligned}
```

The working term of the supercovariant completion constructed with the standard $`K`$ connection is therefore

```math
\boxed{+8\bar\psi_{[\mu}e_{\nu]}{}^{[a}\gamma^{b]}\chi}
```

This index order must be retained:

```math
e_\nu{}^{[a}\gamma^{b]}=-\gamma^{[a}e_\nu{}^{b]},\qquad
+8\bar\psi_{[\mu}e_{\nu]}{}^{[a}\gamma^{b]}\chi
=-8\bar\psi_{[\mu}\gamma^{[a}e_{\nu]}{}^{b]}\chi.
```

Using the Ricci contractions of the primed curvature,

```math
R_a{}^c=\widehat R'_{ab}{}^{cb}(M),\qquad
R=\widehat R'_{ab}{}^{ab}(M),\qquad
f_a{}^c=-\frac16R_a{}^c+\frac1{48}\delta_a{}^cR
```

The trace of the dependent connection and the trace of the full curvature are:

```math
\begin{aligned}
f_a{}^a&=-\frac16R+\frac5{48}R=-\frac1{16}R,\\
\widehat R_{ab}{}^{cb}(M)
&=R_a{}^c+6f_a{}^c+2\delta_a{}^cf_b{}^b\\
&=R_a{}^c-R_a{}^c
 +\left(\frac18-\frac18\right)\delta_a{}^cR=0.
\end{aligned}
```

In comparison with the printed $`-8`$, $`\Delta`$ denotes the calculated
$`+8`$ minus the printed $`-8`$. Temporarily defining $`J_\mu{}^a\equiv\bar\psi_\mu\gamma^a\chi`$ gives

```math
\begin{aligned}
\bar\psi_{[\mu}e_{\nu]}{}^{[a}\gamma^{b]}\chi
&=-J_{[\mu}{}^{[a}e_{\nu]}{}^{b]},\\
\Delta\widehat R'_{\mu\nu}{}^{ab}(M)
&=-16J_{[\mu}{}^{[a}e_{\nu]}{}^{b]},\\
\Delta R_a{}^c&=-12J_a{}^c-4\delta_a{}^cJ_b{}^b,\\
\Delta R&=-32J_a{}^a,\\
\Delta f_a{}^c
&=-\frac16\Delta R_a{}^c+\frac1{48}\delta_a{}^c\Delta R\\
&=2J_a{}^c+\left(\frac23-\frac23\right)\delta_a{}^cJ_b{}^b
=2J_a{}^c.
\end{aligned}
```

Result in the original fields:

```math
\boxed{\Delta f_\mu{}^a=2\bar\psi_\mu\gamma^a\chi,}
```

```math
\begin{aligned}
\Delta\widehat R_{\mu\nu}{}^{ab}(M)
&=\Delta\widehat R'_{\mu\nu}{}^{ab}(M)
 +8\Delta f_{[\mu}{}^{[a}e_{\nu]}{}^{b]}\\
&=-16(\bar\psi_{[\mu}\gamma^{[a}\chi)e_{\nu]}{}^{b]}
  +16(\bar\psi_{[\mu}\gamma^{[a}\chi)e_{\nu]}{}^{b]}=0.
\end{aligned}
```

This last equality holds provided that $`f`$ is recalculated from its own Ricci contractions for both primed definitions. It does not hold if $`f`$ is kept fixed and only the sign of the explicit $`\chi`$ term is changed. The calculation uses the $`+8`$ definition of Section 7 together with $`f`$ calculated from it. This consistently tracks the dependent-connection definition; it is not an EOM substitution or auxiliary-field elimination. No claim is made that the full traceless $`\widehat R(M)`$, and hence $`\widehat C`$, changes solely because of this consistent rewriting.

<a id="115-lorentz-sign-of-the-t_ab-derivative-in-212"></a>

### Lorentz sign of the $`T_{ab}`$ derivative in (2.12)

This record derives the Lorentz-sign correction.
With the index order below, the PDF's (2.12) prints

```math
\left.\mathcal D_\mu T_{ab}\right|_{\omega,\,\mathrm{printed}}
=-2\omega_\mu{}^c{}_{[a}T_{b]c}
```

This is the source record, not the working definition in Section 6.
Below, $`\nabla_\mu^{\mathrm L}`$ denotes only the Lorentz-connection action. This distinction
is neither a gauge choice nor a field truncation; the Lorentz-connection
coefficient of the full supercovariant derivative is being checked.

The first check follows from the lower-index vector derivative in (2.19)
of the same PDF:

```math
\begin{aligned}
\nabla_\mu^{\mathrm L}E_a
&=\partial_\mu E_a+\omega_{\mu ab}E^b\\
&=\partial_\mu E_a+\omega_{\mu ab}\eta^{bc}E_c
=\partial_\mu E_a-\omega_\mu{}^c{}_aE_c.
\end{aligned}
```

The last equality uses $`\omega_{\mu ab}=-\omega_{\mu ba}`$. Using the connection's action on each lower Lorentz index and $`T_{cb}=-T_{bc}`$,

```math
\begin{aligned}
\nabla_\mu^{\mathrm L}T_{ab}
&=\partial_\mu T_{ab}
 -\omega_\mu{}^c{}_aT_{cb}-\omega_\mu{}^c{}_bT_{ac}\\
&=\partial_\mu T_{ab}
 +\omega_\mu{}^c{}_aT_{bc}-\omega_\mu{}^c{}_bT_{ac}\\
&=\partial_\mu T_{ab}+2\omega_\mu{}^c{}_{[a}T_{b]c}.
\end{aligned}
```

The second check is compatibility of the spinor connection in (2.2)
with Clifford multiplication. Temporarily write

```math
\Omega_\mu:=\frac14\omega_\mu{}^{cd}\gamma_{cd},\qquad
\mathsf T:=T_{ab}\gamma^{ab},\qquad
\nabla_\mu^{\mathrm s}:=\partial_\mu+\Omega_\mu
```

where $`\xi`$ is an arbitrary spinor. The covariant product rule must be

```math
\begin{aligned}
\nabla_\mu^{\mathrm s}(\mathsf T\xi)
-\mathsf T\nabla_\mu^{\mathrm s}\xi
&=\bigl(\partial_\mu\mathsf T+[\Omega_\mu,\mathsf T]\bigr)\xi\\
&=\gamma^{ab}(\nabla_\mu^{\mathrm L}T_{ab})\xi
\end{aligned}
```

From the Clifford algebra

```math
\begin{aligned}
[\gamma_{cd},\gamma^a]
&=2(\delta_d{}^a\gamma_c-\delta_c{}^a\gamma_d),\\
[\Omega_\mu,\gamma^a]
&=\frac12\omega_\mu{}^{cd}
 (\delta_d{}^a\gamma_c-\delta_c{}^a\gamma_d)
=-\omega_\mu{}^a{}_c\gamma^c,\\
[\Omega_\mu,\gamma^{ab}]
&=-\omega_\mu{}^a{}_c\gamma^{cb}
 -\omega_\mu{}^b{}_c\gamma^{ac},\\
[\Omega_\mu,\mathsf T]
&=\gamma^{ab}
 (-\omega_\mu{}^c{}_aT_{cb}-\omega_\mu{}^c{}_bT_{ac})\\
&=\gamma^{ab}\,2\omega_\mu{}^c{}_{[a}T_{b]c}.
\end{aligned}
```

The tensor derivative with a plus sign satisfies the covariant product
rule. Using the printed minus-sign derivative instead, the left-hand
side minus the right-hand side is

```math
4\gamma^{ab}\omega_\mu{}^c{}_{[a}T_{b]c}\,\xi
```

which does not vanish identically. For example, the independent monomial $`\omega_\mu{}^{12}T_{23}`$ contributes $`4\omega_\mu{}^{12}T_{23}\gamma^{13}\xi`$. Selecting this coefficient does not set the other fields to zero.

Working result in the original variables and equivalent index notation:

```math
\boxed{\left.\mathcal D_\mu T_{ab}\right|_\omega
=+2\omega_\mu{}^c{}_{[a}T_{b]c},}
\qquad
-2\omega_\mu{}^c{}_{[a}T_{|c|b]}
=+2\omega_\mu{}^c{}_{[a}T_{b]c}.
```

This correction determines only the Lorentz-connection term checked; it does not mean that all coefficients of the map's $`\varphi^i`$, $`N`$ and $`E_a`$ components have been rederived or verified.
