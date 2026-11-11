# Weyl-squared action

Action obtained in the earlier calculation by inserting the components of
[map.md](../../linear_multiplet.md) into equation (3.1) of [welySquared.pdf](https://arxiv.org/abs/1301.6622).
Conventions follow [CONVENTIONS.md](CONVENTIONS.md).
The vector multiplet is retained as $`(\rho,A_\mu,\lambda^i,Y^{ij})`$.

```math
S=\int d^5x\,e\,
\bigl(\ell_{[0]}+\ell_{[2]}+\ell_{[4]}\bigr),
\qquad e=\det(e_\mu{}^a).
```

$`[n]`$ counts only explicitly displayed spinors; $`\widehat R_{ab}(Q)`$ and $`\chi`$
each count as one spinor. Fermions inside hatted curvatures, composite
fields, and full supercovariant derivatives are not additionally expanded.
Thus $`\ell_{[0]}`$ is not identical to the bosonic limit with all fermions
set to zero. This grouping is not a fermion-order truncation.

```math
T^2=T_{ab}T^{ab},\qquad
T^4=T_{ab}T^{bc}T_{cd}T^{da},\qquad
\mathord{\not{\mathcal D}}=\gamma^a\mathcal D_a.
```

Like $`a,b,c,d`$, $`m,n,p,q,r`$ are tangent indices:
$`A_m=e_m{}^\mu A_\mu`$ and $`\psi_m^i=e_m{}^\mu\psi_\mu^i`$.
Antisymmetrization has unit weight,
$`X_{[ab]}=\tfrac12(X_{ab}-X_{ba})`$.

## Explicit spinor count 0

```math
\begin{aligned}
\ell_{[0]}={}&
\frac{\rho}{8}\widehat C_{abcd}\widehat C^{abcd}
+\frac{64\rho}{3}\left(D+\frac83T^2\right)^2
+256\rho\left[4T^4-(T^2)^2\right]\\
&-\frac{16\rho}{3}\widehat C_{abcd}T^{ab}T^{cd}
-\frac{\rho}{3}\widehat R_{ab}{}^{ij}(V)
                   \widehat R^{ab}{}_{ij}(V)
+\frac{16}{3}Y^{ij}\widehat R_{ab\,ij}(V)T^{ab}\\
&-\frac{128\rho}{3}
       \mathcal D_{[a}T_{b]c}\mathcal D^{[a}T^{b]c}
-\frac{128\rho}{3}T_{ab}\mathcal D^b\mathcal D_cT^{ac}\\
&-\frac{128\rho}{3}\varepsilon_{abcde}
             T^{ab}T^{cd}\mathcal D_fT^{ef}\\
&+\frac1{16}A^a\varepsilon_{abcde}
             \widehat C^{bcfg}\widehat C^{de}{}_{fg}
-\frac1{12}A^a\varepsilon_{abcde}
             \widehat R^{bc\,ij}(V)\widehat R^{de}{}_{ij}(V)\\
&+A^a\mathcal D^b\Bigg[
4\widehat C_{abcd}T^{cd}
-\frac{64}{3}\left(D+\frac83T^2\right)T_{ab}\\
&\hspace{39mm}
-\frac{128}{3}
 \left(4T_{ac}T^{cd}T_{bd}-T_{ab}T^2\right)
\Bigg]\\
&-32A^a\varepsilon_{abcde}\mathcal D^b
 \left(
 \frac23T^{cf}\mathcal D_fT^{de}
 +T^c{}_f\mathcal D^dT^{ef}
 \right).
\end{aligned}
```

## Explicit spinor count 2

```math
\begin{aligned}
\ell_{[2]}={}&
\frac{3\rho}{4}\overline{\widehat R}_{ab}(Q)
                  \mathord{\not{\mathcal D}}\widehat R^{ab}(Q)
-\frac{256\rho}{3}\bar\chi\mathord{\not{\mathcal D}}\chi\\
&-\frac{i\rho}{2}T_{cd}\overline{\widehat R}_{ab}(Q)
                  \gamma^{cd}\widehat R^{ab}(Q)
-\frac{160i\rho}{3}T^{ab}\overline{\widehat R}_{ab}(Q)\chi\\
&+\frac i4Y^{ij}\overline{\widehat R}_{ab\,i}(Q)
                  \widehat R^{ab}{}_j(Q)
+\frac{256i}{3}Y^{ij}\bar\chi_i\chi_j\\
&+\frac i2A^a\overline{\widehat R}_{bc}(Q)
                  \mathcal D_a\widehat R^{bc}(Q)
+\frac{3i}{2}A^a\overline{\widehat R}^{bc}(Q)
                  \mathcal D_b\widehat R_{ca}(Q)\\
&+A^a\mathcal D^b\left(
8i\overline{\widehat R}_{ab}(Q)\chi
-\frac{64i}{3}\bar\chi\gamma_{ab}\chi
\right)\\
&-\frac83A^aT^{bc}
                  \overline{\widehat R}_{bc}(Q)\gamma_a\chi
-4iA^a\varepsilon_{abcde}T^{bc}
                  \overline{\widehat R}^{de}(Q)\chi\\
&+\frac12A^aT^{bc}\overline{\widehat R}_{bd}(Q)
                  \gamma_a\widehat R_c{}^d(Q)
+\frac{3i}{16}A^a\varepsilon_{abcde}T^{bc}
                  \overline{\widehat R}_{fg}(Q)
                  \gamma^{de}\widehat R^{fg}(Q)\\
&-\frac83T^{ab}\widehat R_{ab\,ij}(V)
                  \bar\lambda^i\gamma^m\psi_m^j\\
&+\frac{4i\rho}{3}T^{ab}\widehat R_{ab\,ij}(V)
                  \bar\psi_m^i\gamma^{mn}\psi_n^j
-\frac{2i}{3}A_m\varepsilon^{mnpqr}T^{ab}
                  \widehat R_{ab\,ij}(V)
                  \bar\psi_n^i\gamma_{qr}\psi_p^j\\[1mm]
&+\left(
 i\bar\lambda^i+\frac\rho2\bar\psi_m^i\gamma^m
 -\frac i2A_m\bar\psi_n^i\gamma^{mn}
 \right)
 \Bigg[
 -\frac18\widehat C_{abcd}\gamma^{cd}
                       \widehat R^{ab}{}_i(Q)\\
&\hspace{23mm}
 -4i\mathcal D^aT^{bc}\gamma_c\widehat R_{ab\,i}(Q)
 +8iT^{ab}\gamma^c\mathcal D_c\widehat R_{ab\,i}(Q)
 +8iT^{ab}\gamma_a\mathcal D^c\widehat R_{bc\,i}(Q)\\
&\hspace{23mm}
 +\frac{128}{3}\left(D+\frac83T^2\right)\chi_i
 +\frac{64i}{3}\mathcal D^bT_{ab}\gamma^a\chi_i
 +\frac{128i}{3}T_{ab}\gamma^a\mathcal D^b\chi_i\\
&\hspace{23mm}
 -\frac{32}{3}\varepsilon^{abcde}
                       \mathcal D_aT_{bc}\gamma_{de}\chi_i
 +\frac83T_{ab}T_{cd}\gamma^{ab}
                       \widehat R^{cd}{}_i(Q)\\
&\hspace{23mm}
 +\frac12\widehat R_{ab\,ij}(V)\widehat R^{ab\,j}(Q)
 -\frac83\widehat R_{ab\,ij}(V)\gamma^{ab}\chi^j
 \Bigg].
\end{aligned}
```

## Explicit spinor count 4

```math
\begin{aligned}
\ell_{[4]}={}&
-\frac i8\,
 \bar\lambda^i\gamma^m\psi_m^j\,
 \overline{\widehat R}_{ab\,i}(Q)\widehat R^{ab}{}_j(Q)
-\frac{128i}{3}\,
 \bar\lambda^i\gamma^m\psi_m^j\,\bar\chi_i\chi_j\\
&-\frac{\rho}{16}\,
 \bar\psi_m^i\gamma^{mn}\psi_n^j\,
 \overline{\widehat R}_{ab\,i}(Q)\widehat R^{ab}{}_j(Q)
-\frac{64\rho}{3}\,
 \bar\psi_m^i\gamma^{mn}\psi_n^j\,\bar\chi_i\chi_j\\
&+\frac1{32}A_m\varepsilon^{mnpqr}
 \bar\psi_n^i\gamma_{qr}\psi_p^j\,
 \overline{\widehat R}_{ab\,i}(Q)\widehat R^{ab}{}_j(Q)\\
&+\frac{32}{3}A_m\varepsilon^{mnpqr}
 \bar\psi_n^i\gamma_{qr}\psi_p^j\,\bar\chi_i\chi_j .
\end{aligned}
```

This is the local compact expression obtained in the earlier calculation;
no total derivative was discarded, gauge selected, or field equation used.
It does not claim an absolutely minimal operator basis under all
Fierz identities and integrations by parts.
