# gaugedMap: (2.6), (2.7), (2.9), (2.10), and (2.12)

Source: Mehmet Ozkan and Yi Pang, *Supersymmetric Completion of Gauss-Bonnet
Combination in Five Dimensions*, source
gaugedMap.pdf, pp. 6–8.
Conventions: [CONVENTIONS.md](CONVENTIONS.md).

The source's pregauge notation is retained. In the definition of $`\widehat R(M)`$
in (2.7), only the explicit $`\chi`$ coefficient is corrected to $`-8\longrightarrow+8`$.
Its derivation from $`\omega`$ appears below. Other printed expressions
are retained; source issues not corrected here are identified at the end.

## Notation

Multiplet labels, when used, appear first in the subscript group;
for example, $`\rho_A`$, $`\lambda_{Ai}`$, $`Y_{Aij}`$, and $`A_{A\mu}`$.
Upper or lower label placement in the source does not define another
multiplet. Lorentz and SU(2) index positions are retained;
unlabeled $`L_{ij}`$ and $`L_{1ij}`$ are distinct objects.

```math
\begin{gathered}
\mathcal D_a=e_a{}^\mu\mathcal D_\mu,\qquad
\mathord{\not{\mathcal D}}=\gamma^a\mathcal D_a,\qquad
\gamma_\mu=e_\mu{}^a\gamma_a,\\
\gamma\!\cdot\!T=\gamma^{ab}T_{ab},\qquad
\gamma\!\cdot\!\widehat G=\gamma^{ab}\widehat G_{ab},\qquad
\gamma\!\cdot\!\widehat R^{ij}(V)
=\gamma^{ab}\widehat R_{ab}{}^{ij}(V),\qquad
T^2=T_{ab}T^{ab},\\
X_{[ab]}=\frac12(X_{ab}-X_{ba}),\qquad
X_{(ab)}=\frac12(X_{ab}+X_{ba}),\qquad
\bar X\Gamma Y=\bar X^i\Gamma Y_i.
\end{gathered}
```

$`\psi_\mu^i`$ is the gravitino, $`\psi^i`$ the dilatino, and $`\phi_\mu^i`$ the
$`S`$-supersymmetry connection. $`D`$ denotes the auxiliary scalar;
$`\mathcal D`$ is the derivative operator. Tangent components of hatted
curvatures use the vielbein; for example, $`\widehat R_{ab}(Q)=e_a{}^\mu e_b{}^\nu\widehat R_{\mu\nu}(Q)`$.

## (2.6)

```math
\begin{aligned}
\widehat R_{\mu\nu}{}^i(Q)
={}&\widehat R'_{\mu\nu}{}^i(Q)
-2i\gamma_{[\mu}\phi_{\nu]}^i,\\
\widehat R'_{\mu\nu}{}^i(Q)
={}&2\partial_{[\mu}\psi_{\nu]}^i
+\frac12\omega_{[\mu}{}^{ab}\gamma_{ab}\psi_{\nu]}^i
+b_{[\mu}\psi_{\nu]}^i
-2V_{[\mu}{}^{ij}\psi_{\nu]j}
+2i(\gamma\!\cdot\!T)\gamma_{[\mu}\psi_{\nu]}^i.
\end{aligned}
\tag{2.6}
```

## (2.7): $`\widehat R(M)`$ with the corrected $`\chi`$ coefficient

```math
\begin{aligned}
\widehat R_{\mu\nu}{}^{ab}(M)
={}&2\partial_{[\mu}\omega_{\nu]}{}^{ab}
+2\omega_{[\mu}{}^{ac}\omega_{\nu]c}{}^b
+8f_{[\mu}{}^{[a}e_{\nu]}{}^{b]}
+i\bar\psi_{[\mu}\gamma^{ab}\psi_{\nu]}\\
&+i\bar\psi_{[\mu}\gamma^{[a}(\gamma\!\cdot\!T)
 \gamma^{b]}\psi_{\nu]}
+\bar\psi_{[\mu}\gamma^{[a}\widehat R_{\nu]}{}^{b]}(Q)
+\frac12\bar\psi_{[\mu}\gamma_{\nu]}\widehat R^{ab}(Q)\\
&+8\bar\psi_{[\mu}e_{\nu]}{}^{[a}\gamma^{b]}\chi
+i\bar\phi_{[\mu}\gamma^{ab}\psi_{\nu]},\\[4pt]
\widehat R_{\mu\nu}{}^{ij}(V)
={}&2\partial_{[\mu}V_{\nu]}{}^{ij}
-2V_{[\mu}{}^{k(i}V_{\nu]k}{}^{j)}
-3i\bar\phi_{[\mu}^{(i}\psi_{\nu]}^{j)}\\
&-8\bar\psi_{[\mu}^{(i}\gamma_{\nu]}\chi^{j)}
-i\bar\psi_{[\mu}^{(i}(\gamma\!\cdot\!T)\psi_{\nu]}^{j)}.
\end{aligned}
\tag{2.7}
```

## (2.9)

```math
\begin{aligned}
T_{ab}
={}&\frac18\sigma^{-2}
\left(
\sigma\widehat G_{ab}
+\frac16\varepsilon_{abcde}\widehat H^{cde}
+\frac{i}{4}\bar\psi\gamma_{ab}\psi
\right),\\[4pt]
\chi^i
={}&\frac{i}{8}\sigma^{-1}\mathord{\not{\mathcal D}}\psi^i
+\frac{i}{16}\sigma^{-2}(\mathord{\not{\mathcal D}}\sigma)\psi^i
-\frac1{32}\sigma^{-2}(\gamma\!\cdot\!\widehat G)\psi^i
+\frac14\sigma^{-1}(\gamma\!\cdot\!T)\psi^i\\
&+\frac{i}{32}\sigma^{-3}\psi_j\bar\psi^i\psi^j,\\[4pt]
D
={}&\frac14\sigma^{-1}\Box^c\sigma
+\frac18\sigma^{-2}(\mathcal D_a\sigma)(\mathcal D^a\sigma)
-\frac1{16}\sigma^{-2}\widehat G_{\mu\nu}\widehat G^{\mu\nu}\\
&-\frac18\sigma^{-2}\bar\psi\mathord{\not{\mathcal D}}\psi
-\frac1{64}\sigma^{-4}\bar\psi^i\psi^j\bar\psi_i\psi_j
-4i\sigma^{-1}\psi\chi\\
&+\left(
-\frac{26}{3}T_{ab}
+2\sigma^{-1}\widehat G_{ab}
+\frac{i}{4}\sigma^{-2}\bar\psi\gamma_{ab}\psi
\right)T^{ab}.
\end{aligned}
\tag{2.9}
```

## (2.10)

```math
\begin{aligned}
\Box^c\sigma
={}&\left(\partial^a-2b^a+\omega_b{}^{ba}\right)\mathcal D_a\sigma
-\frac{i}{2}\bar\psi_a\mathcal D^a\psi
-2\sigma\bar\psi_a\gamma^a\chi\\
&+\frac12\bar\psi_a\gamma^a(\gamma\!\cdot\!T)\psi
+\frac12\bar\phi_a\gamma^a\psi
+2f_a{}^a\sigma,\\[4pt]
f_\mu{}^a
={}&-\frac16\mathcal R_\mu{}^a
+\frac1{48}e_\mu{}^a\mathcal R,\\
\mathcal R_{\mu\nu}
\equiv{}&\widehat R'_{\mu\rho}{}^{ab}(M)e_b{}^\rho e_{\nu a},
\qquad
\mathcal R\equiv\mathcal R_\mu{}^\mu.
\end{aligned}
\tag{2.10}
```

```math
\begin{aligned}
\widehat R'_{\mu\nu}{}^{ab}(M)
&\equiv\widehat R_{\mu\nu}{}^{ab}(M)
-8f_{[\mu}{}^{[a}e_{\nu]}{}^{b]},\\
\mathcal R_\mu{}^a&=e^{a\nu}\mathcal R_{\mu\nu},\qquad
\mathcal R=g^{\mu\nu}\mathcal R_{\mu\nu},\qquad
f_a{}^a=e_a{}^\mu f_\mu{}^a.
\end{aligned}
```

The primed curvature removes only the explicit $`f`$ term;
the corrected $`+8`$ $`\chi`$ term remains. $`\mathcal R_{\mu\nu}`$ and $`\mathcal R`$
are kept distinct from the ordinary Ricci tensor and scalar.

## (2.12): As printed in the PDF

```math
\begin{aligned}
\mathcal D_\mu\chi^i
={}&\left(\partial_\mu-\frac72b_\mu
+\frac14\omega_\mu{}^{ab}\gamma_{ab}\right)\chi^i
-V_\mu{}^{ij}\chi_j
-\frac14\psi_\mu^iD
+\frac1{64}(\gamma\!\cdot\!\widehat R^{ij}(V))\psi_{\mu j}\\
&-\frac{i}{8}\gamma^{ab}(\mathord{\not{\mathcal D}}T_{ab})\psi_\mu^i
+\frac{i}{8}\gamma^a(\mathcal D^bT_{ab})\psi_\mu^i
+\frac14\gamma^{abcd}T_{ab}T_{cd}\psi_\mu^i
-\frac16T^2\psi_\mu^i
-\frac14(\gamma\!\cdot\!T)\phi_\mu^i,\\[4pt]
\mathcal D_\mu T_{ab}
={}&\partial_\mu T_{ab}-b_\mu T_{ab}
-2\omega_\mu{}^c{}_{[a}T_{b]c}
-\frac{i}{2}\bar\psi_\mu\gamma_{ab}\chi
+\frac{3i}{32}\bar\psi_\mu\widehat R_{ab}(Q).
\end{aligned}
\tag{2.12}
```

## Checking the $`\chi`$ coefficient in $`\widehat R(M)`$ from $`\omega`$

The input is the dependent connection in PDF (2.5):

```math
\begin{aligned}
\omega_\mu{}^{ab}
={}&2e^{\nu[a}\partial_{[\mu}e_{\nu]}{}^{b]}
-e^{\nu[a}e^{b]\rho}e_{\mu c}\partial_\nu e_\rho{}^c
+2e_\mu{}^{[a}b^{b]}\\
&+\frac12\bar\psi^{[a}\gamma^{b]}\psi_\mu
+\frac14\bar\psi^a\gamma_\mu\psi^b,
\qquad b^a=e^{a\mu}b_\mu.
\end{aligned}
```

Required transformations from PDF (2.1):

```math
\begin{aligned}
\delta_Qe_\mu{}^a
&=\frac12\bar\epsilon\gamma^a\psi_\mu,\\
\delta_Q\psi_\mu^i
&=\left(\partial_\mu+\frac12b_\mu
+\frac14\omega_\mu{}^{ab}\gamma_{ab}\right)\epsilon^i
-V_\mu{}^{ij}\epsilon_j
+i(\gamma\!\cdot\!T)\gamma_\mu\epsilon^i,\\
\delta_Qb_\mu
&=\frac{i}{2}\bar\epsilon\phi_\mu
-2\bar\epsilon\gamma_\mu\chi.
\end{aligned}
```

$`\left.\cdot\right|_\chi`$ selects only the coefficient of the explicit $`\chi`$ structure;
it neither sets fields to zero nor truncates fermion order.
Since $`\delta_Qe`$ and $`\delta_Q\psi_\mu`$ contain no explicit $`\chi`$,

```math
\begin{aligned}
\left.\delta_Qb^a\right|_\chi
&=e^{a\mu}\left.\delta_Qb_\mu\right|_\chi
=-2\bar\epsilon\gamma^a\chi,\\
\left.\delta_Q\omega_\mu{}^{ab}\right|_\chi
&=2e_\mu{}^{[a}\left.\delta_Qb^{b]}\right|_\chi\\
&=2e_\mu{}^{[a}\left(-2\bar\epsilon\gamma^{b]}\chi\right)
=-4e_\mu{}^{[a}\bar\epsilon\gamma^{b]}\chi.
\end{aligned}
```

The Q-connection completion of the curvature replaces $`\bar\epsilon`$ by $`\bar\psi_\mu`$
in the connection's Q-transformation and subtracts it antisymmetrically.
This acts on the curl of $`\omega`$; the separate $`K`$-connection term
$`8f_{[\mu}{}^{[a}e_{\nu]}{}^{b]}`$ is neither substituted nor redefined at this stage. Thus

```math
\begin{aligned}
\left.\widehat R_{\mu\nu}{}^{ab}(M)\right|_{
\text{explicit Q-connection, }\chi}
&=-\left.\delta_Q\omega_\nu{}^{ab}\right|_{
\chi,\,\bar\epsilon\to\bar\psi_\mu}
+\left.\delta_Q\omega_\mu{}^{ab}\right|_{
\chi,\,\bar\epsilon\to\bar\psi_\nu}\\
&=4\bar\psi_\mu e_\nu{}^{[a}\gamma^{b]}\chi
-4\bar\psi_\nu e_\mu{}^{[a}\gamma^{b]}\chi\\
&=8\bar\psi_{[\mu}e_{\nu]}{}^{[a}\gamma^{b]}\chi.
\end{aligned}
```

Cancellation of derivative parameters between the curl and this Q-connection term:

```math
\begin{aligned}
\left.2\partial_{[\mu}\delta_Q\omega_{\nu]}{}^{ab}
\right|_{\partial\bar\epsilon\,\chi}
&=-8(\partial_{[\mu}\bar\epsilon)
 e_{\nu]}{}^{[a}\gamma^{b]}\chi,\\
\left.\delta_Q\left(
8\bar\psi_{[\mu}e_{\nu]}{}^{[a}\gamma^{b]}\chi
\right)\right|_{\partial\bar\epsilon\,\chi}
&=+8(\partial_{[\mu}\bar\epsilon)
 e_{\nu]}{}^{[a}\gamma^{b]}\chi,\\
(-8+8)(\partial_{[\mu}\bar\epsilon)
 e_{\nu]}{}^{[a}\gamma^{b]}\chi&=0.
\end{aligned}
```

```math
\boxed{
-8\bar\psi_{[\mu}e_{\nu]}{}^{[a}\gamma^{b]}\chi
\quad\longrightarrow\quad
+8\bar\psi_{[\mu}e_{\nu]}{}^{[a}\gamma^{b]}\chi.}
```

This corrects the sign in the Q-connection completion of $`\omega`$
in the specified connection representation; it does not claim
a coefficient determination independent of the full curvature
after substituting $`f`$.

## Other printed expressions left uncorrected

- The $`i\bar\psi_{[\mu}\gamma^{ab}\psi_{\nu]}`$ in (2.7) is retained as printed; no $`\psi`$ is replaced
  by $`\phi`$ here.
- In (2.9), the PDF prints the $`-4i\sigma^{-1}\psi\chi`$ term without a bar on its
  first spinor. This is transcribed unchanged; it is not an explicit
  barred scalar-bilinear definition in project conventions.
- The printed $`-\tfrac72b_\mu\chi^i`$ and $`-2\omega_\mu{}^c{}_{[a}T_{b]c}`$ in (2.12) are retained.
  The former disagrees with $`w(\chi)=\tfrac32`$ in `CONVENTIONS.md`, and the latter with
  the Lorentz-connection convention of the same file. These lines
  must not be used as corrected project derivatives.
