# Substitution of the gauged linear map into density formula (3.2)

<a id="1-purpose-and-authoritative-inputs"></a>

## Purpose and authoritative inputs

This report records substitution of the gauged linear-multiplet map
in [gauged_linear_map.md](gauged_linear_map.md) into the vector–linear density formula
(3.2) of gaugedMap.pdf, and organization of the resulting terms.

The local inputs used are:

1. `gaugedMap.pdf`, equation (3.2);
2. `gauged_linear_map.md`, gauged linear-multiplet components;
3. [CONVENTIONS.md](../gR2/CONVENTIONS.md), index, NW–SE contraction,
   symplectic–Majorana flip, and Clifford conventions.

The calculation remains complete and off shell. No EOM are used,
auxiliary fields eliminated, additional gauge selected, or fermion
truncation made. Since the stated inputs do not detail the gauged
target-gauge supercovariant completions,

```math
\widehat F_{ab},\qquad \widehat G_{ab},\qquad
T_{g\,ab},\qquad D_g,\qquad \chi_{g\,i}
```

are retained unexpanded.

<a id="2-notational-distinction"></a>

## Notational distinction

The first line of `gauged_linear_map.md` uses `L_{ij}` both for the output map component
and for the elementary linear-multiplet field in the gauging term

```math
-\frac12g\rho\sigma^{-1}L_{ij}
```

To make the distinction used in the earlier calculation explicit,
the composite components inserted into the density formula are
denoted in this report by

```math
(\mathbb L_{ij},\mathbb\varphi_i,\mathbb E^{ab},\mathbb N)
```

The gauging field on the map's right-hand side remains $`L_{ij}`$.
The first map equality is therefore read as

```math
\boxed{
\mathbb L_{ij}
=
\sigma Y_{ij}
-\frac12g\rho\sigma^{-1}L_{ij}
+\frac{i}{4}\rho\sigma^{-1}\bar\psi_{(i}\psi_{j)}
-\frac{i}{2}\bar\lambda_{(i}\psi_{j)} }
```

Here $`\psi_a^i`$ is the gravitino, while $`\psi_i`$, with no tangent index,
is the Dilaton–Weyl multiplet spinor appearing in the map.

<a id="3-initial-density"></a>

## Initial density

In project conventions,

```math
\mathscr L_{V\mathbb L}\equiv e^{-1}\mathcal L_{V\mathbb L}.
```

The paper's (3.2), in tangent-space components,

```math
\boxed{
\begin{aligned}
\mathscr L_{V\mathbb L}
={}&Y^{ij}\mathbb L_{ij}
+i\bar\lambda^i\mathbb\varphi_i
-\frac12\bar\psi_a^i\gamma^a\lambda^j\mathbb L_{ij}
+\frac12F_{ab}\mathbb E^{ab}
\\
&+\rho\mathbb N
+\frac{\rho}{2}\bar\psi_a^i\gamma^a\mathbb\varphi_i
+\frac{i\rho}{4}
 \bar\psi_a^i\gamma^{ab}\psi_b^j\mathbb L_{ij}.
\end{aligned}}
\tag{3.2'}
```

Here

```math
F_{\mu\nu}\mathbb E^{\mu\nu}=F_{ab}\mathbb E^{ab}
```

was used.

<a id="4-map-components"></a>

## Map components

The other three substituted components are

```math
\begin{aligned}
\mathbb\varphi_i
={}&
\frac{i}{2}\sigma\not D\lambda_i
+\frac{i}{2}\rho\not D\psi_i
+\rho\,\gamma\!\cdot\!T_g\,\psi_i
+\sigma\,\gamma\!\cdot\!T_g\,\lambda_i
-8\sigma\rho\chi_{g\,i}
\\
&-\frac18\gamma\!\cdot\!\widehat G\,\lambda_i
-\frac18\gamma\!\cdot\!\widehat F\,\psi_i
+\frac14\not D\sigma\,\lambda_i
+\frac14\not D\rho\,\psi_i
-\frac12Y_{ij}\psi^j
\\
&-\frac{i}{8}\sigma^{-1}\lambda^j\bar\psi_i\psi_j
+\frac14g\sigma^{-1}L_{ij}\lambda^j,
\end{aligned}
\tag{4.1}
```

```math
\boxed{
\begin{aligned}
\mathbb E^{ab}
={}&-\frac12\sigma\widehat F^{ab}
-\frac12\rho\widehat G^{ab}
+8\sigma\rho T_g^{ab}
-\frac{i}{8}\bar\lambda\gamma^{ab}\psi
-\frac14\varepsilon^{abcde}C_cF_{de},
\end{aligned}}
\tag{4.2}
```

and

```math
\begin{aligned}
\mathbb N
={}&
\frac12\rho\square^C\sigma
+\frac12\sigma\square^C\rho
+\frac12D_a\rho D^a\sigma
-\frac14\widehat G_{ab}\widehat F^{ab}
-4\rho\sigma\left(D_g+\frac{26}{3}T_g^2\right)
\\
&+4\sigma\widehat F^{ab}T_{g\,ab}
+4\rho\widehat G^{ab}T_{g\,ab}
+8i\sigma\bar\chi_g\lambda
+8i\rho\bar\chi_g\psi
\\
&-\frac14\bar\lambda\not D\psi
-\frac14\bar\psi\not D\lambda
+i\bar\psi\gamma\!\cdot\!T_g\lambda,
\qquad
T_g^2=T_{g\,ab}T_g^{ab}.
\end{aligned}
\tag{4.3}
```

<a id="5-term-by-term-expansion-of-the-density"></a>

## Term-by-term expansion of the density

<a id="51-the-yijmathbb-l_ij-term"></a>

### The $`Y^{ij}\mathbb L_{ij}`$ term

Direct substitution

```math
\begin{aligned}
Y^{ij}\mathbb L_{ij}
={}&\sigma Y^{ij}Y_{ij}
-\frac12g\rho\sigma^{-1}Y^{ij}L_{ij}
\\
&+\frac{i}{4}\rho\sigma^{-1}
  Y^{ij}\bar\psi_{(i}\psi_{j)}
-\frac{i}{2}Y^{ij}\bar\lambda_{(i}\psi_{j)}.
\end{aligned}
\tag{5.1}
```

Since $`Y^{ij}=Y^{ji}`$, symmetrizations are selected directly by $`Y^{ij}`$.
Since the two SU(2) index pairs are exchanged together,

```math
Y^{ij}\bar\psi_i\psi_j
=Y_{ij}\bar\psi^i\psi^j,
\qquad
Y^{ij}\bar\lambda_i\psi_j
=Y_{ij}\bar\lambda^i\psi^j.
```

Therefore

```math
\boxed{
\begin{aligned}
Y^{ij}\mathbb L_{ij}
={}&\sigma Y^{ij}Y_{ij}
-\frac12g\rho\sigma^{-1}Y^{ij}L_{ij}
\\
&+\frac{i}{4}\rho\sigma^{-1}
  Y_{ij}\bar\psi^i\psi^j
-\frac{i}{2}Y_{ij}\bar\lambda^i\psi^j.
\end{aligned}}
\tag{5.2}
```

<a id="52-the-ibarlambdaimathbbvarphi_i-term"></a>

### The $`i\bar\lambda^i\mathbb\varphi_i`$ term

Multiplying every term of (4.1) from the left by $`i\bar\lambda^i`$ gives

```math
\begin{aligned}
i\bar\lambda^i\mathbb\varphi_i
={}&-\frac12\sigma\bar\lambda\not D\lambda
-\frac12\rho\bar\lambda\not D\psi
+i\rho\bar\lambda\gamma\!\cdot\!T_g\psi
+i\sigma\bar\lambda\gamma\!\cdot\!T_g\lambda
\\
&-8i\sigma\rho\bar\lambda\chi_g
-\frac{i}{8}\bar\lambda\gamma\!\cdot\!\widehat G\lambda
-\frac{i}{8}\bar\lambda\gamma\!\cdot\!\widehat F\psi
\\
&+\frac{i}{4}\bar\lambda(\not D\sigma)\lambda
+\frac{i}{4}\bar\lambda(\not D\rho)\psi
-\frac{i}{2}\bar\lambda^iY_{ij}\psi^j
\\
&+\frac18\sigma^{-1}
 (\bar\lambda^i\lambda^j)(\bar\psi_i\psi_j)
+\frac{i}{4}g\sigma^{-1}L_{ij}\bar\lambda^i\lambda^j.
\end{aligned}
\tag{5.3}
```

The phases of the last two coefficients follow directly from

```math
i\left(-\frac{i}{8}\right)=+\frac18,
\qquad
i\left(+\frac14g\right)=+\frac{i}{4}g
```

arise from the products.

The NW–SE flip rule for $`n=1`$ gives

```math
\bar\lambda^i\gamma^a\lambda_i
=-\bar\lambda^i\gamma^a\lambda_i=0
```

since it gives

```math
\boxed{
\bar\lambda(\not D\sigma)\lambda
=(D_a\sigma)\bar\lambda\gamma^a\lambda=0.}
\tag{5.4}
```

<a id="53-the-frac12f_abmathbb-eab-term"></a>

### The $`\frac12F_{ab}\mathbb E^{ab}`$ term

Substitution of (4.2)

```math
\begin{aligned}
\frac12F_{ab}\mathbb E^{ab}
={}&-\frac14\sigma F_{ab}\widehat F^{ab}
-\frac14\rho F_{ab}\widehat G^{ab}
+4\sigma\rho F_{ab}T_g^{ab}
\\
&-\frac{i}{16}F_{ab}\bar\lambda\gamma^{ab}\psi
-\frac18\varepsilon^{abcde}F_{ab}C_cF_{de}.
\end{aligned}
\tag{5.5}
```

Bosonic factors in the last term can be exchanged. Cyclic relabeling
of dummy indices $`(c,d,e)\mapsto(e,c,d)`$ uses two transpositions and does not change
the epsilon sign:

```math
\boxed{
-\frac18\varepsilon^{abcde}F_{ab}C_cF_{de}
=-\frac18\varepsilon^{abcde}F_{ab}F_{cd}C_e.}
\tag{5.6}
```

Also, since the gamma-dot convention contains no $`1/2!`$,

```math
F_{ab}\bar\lambda\gamma^{ab}\psi
=\bar\lambda\gamma\!\cdot\!F\,\psi.
```

<a id="54-the-rhomathbb-n-term"></a>

### The $`\rho\mathbb N`$ term

Multiplying every term of (4.3) by $`\rho`$ gives

```math
\begin{aligned}
\rho\mathbb N
={}&\frac12\rho^2\square^C\sigma
+\frac12\rho\sigma\square^C\rho
+\frac12\rho D_a\rho D^a\sigma
-\frac14\rho\widehat G_{ab}\widehat F^{ab}
\\
&-4\rho^2\sigma
 \left(D_g+\frac{26}{3}T_g^2\right)
+4\rho\sigma\widehat F^{ab}T_{g\,ab}
+4\rho^2\widehat G^{ab}T_{g\,ab}
\\
&+8i\rho\sigma\bar\chi_g\lambda
+8i\rho^2\bar\chi_g\psi
-\frac14\rho\bar\lambda\not D\psi
-\frac14\rho\bar\psi\not D\lambda
\\
&+i\rho\bar\psi\gamma\!\cdot\!T_g\lambda.
\end{aligned}
\tag{5.7}
```

<a id="55-the--frac12barpsi_aigammaalambdajmathbb-l_ij-term"></a>

### The $`-\frac12\bar\psi_a^i\gamma^a\lambda^j\mathbb L_{ij}`$ term

Substituting the composite $`\mathbb L_{ij}`$ gives

```math
\begin{aligned}
-\frac12\bar\psi_a^i\gamma^a\lambda^j\mathbb L_{ij}
={}&-\frac12\sigma Y_{ij}
 \bar\psi_a^i\gamma^a\lambda^j
+\frac14g\rho\sigma^{-1}L_{ij}
 \bar\psi_a^i\gamma^a\lambda^j
\\
&-\frac{i}{8}\rho\sigma^{-1}
 (\bar\psi_a^i\gamma^a\lambda^j)
 \bar\psi_{(i}\psi_{j)}
\\
&+\frac{i}{4}
 (\bar\psi_a^i\gamma^a\lambda^j)
 \bar\lambda_{(i}\psi_{j)}.
\end{aligned}
\tag{5.8}
```

<a id="56-the-fracrho2barpsi_aigammaamathbbvarphi_i-term"></a>

### The $`\frac\rho2\bar\psi_a^i\gamma^a\mathbb\varphi_i`$ term

The product of (4.1) with the gravitino is

```math
\begin{aligned}
\frac\rho2\bar\psi_a^i\gamma^a\mathbb\varphi_i
={}&\frac{i}{4}\rho\sigma
 \bar\psi_a\gamma^a\not D\lambda
+\frac{i}{4}\rho^2
 \bar\psi_a\gamma^a\not D\psi
\\
&+\frac12\rho^2
 \bar\psi_a\gamma^a\gamma\!\cdot\!T_g\psi
+\frac12\rho\sigma
 \bar\psi_a\gamma^a\gamma\!\cdot\!T_g\lambda
\\
&-4\sigma\rho^2\bar\psi_a\gamma^a\chi_g
-\frac{\rho}{16}
 \bar\psi_a\gamma^a\gamma\!\cdot\!\widehat G\lambda
\\
&-\frac{\rho}{16}
 \bar\psi_a\gamma^a\gamma\!\cdot\!\widehat F\psi
+\frac{\rho}{8}
 \bar\psi_a\gamma^a(\not D\sigma)\lambda
\\
&+\frac{\rho}{8}
 \bar\psi_a\gamma^a(\not D\rho)\psi
-\frac{\rho}{4}Y_{ij}
 \bar\psi_a^i\gamma^a\psi^j
\\
&-\frac{i}{16}\rho\sigma^{-1}
 (\bar\psi_a^i\gamma^a\lambda^j)(\bar\psi_i\psi_j)
\\
&+\frac18g\rho\sigma^{-1}L_{ij}
 \bar\psi_a^i\gamma^a\lambda^j.
\end{aligned}
\tag{5.9}
```

<a id="57-the-fracirho4barpsi_aigammaabpsi_bjmathbb-l_ij-term"></a>

### The $`\frac{i\rho}{4}\bar\psi_a^i\gamma^{ab}\psi_b^j\mathbb L_{ij}`$ term

The final density term

```math
\begin{aligned}
\frac{i\rho}{4}
\bar\psi_a^i\gamma^{ab}\psi_b^j\mathbb L_{ij}
={}&\frac{i}{4}\rho\sigma Y_{ij}
 \bar\psi_a^i\gamma^{ab}\psi_b^j
\\
&-\frac{i}{8}g\rho^2\sigma^{-1}L_{ij}
 \bar\psi_a^i\gamma^{ab}\psi_b^j
\\
&-\frac1{16}\rho^2\sigma^{-1}
 (\bar\psi_a^i\gamma^{ab}\psi_b^j)
 \bar\psi_{(i}\psi_{j)}
\\
&+\frac18\rho
 (\bar\psi_a^i\gamma^{ab}\psi_b^j)
 \bar\lambda_{(i}\psi_{j)}.
\end{aligned}
\tag{5.10}
```

The coefficient signs here are

```math
\frac{i\rho}{4}\frac{i\rho}{4\sigma}
=-\frac{\rho^2}{16\sigma},
\qquad
\frac{i\rho}{4}\left(-\frac{i}{2}\right)
=+\frac\rho8
```

arise from the products.

<a id="6-spinor-and-index-rearrangements"></a>

## Spinor and index rearrangements

The principal identities used when collecting terms are as follows.

<a id="61-symmetric-su2-tensor"></a>

### Symmetric SU(2) tensor

```math
Y^{ij}\bar\lambda_{(i}\psi_{j)}
=Y_{ij}\bar\lambda^i\psi^j.
\tag{6.1}
```

The two $`Y\lambda\psi`$ terms in (5.2) and (5.3) therefore combine as

```math
-\frac{i}{2}Y_{ij}\bar\lambda^i\psi^j
-\frac{i}{2}Y_{ij}\bar\lambda^i\psi^j
=-iY_{ij}\bar\lambda^i\psi^j
\tag{6.2}
```

in this combination.

<a id="62-nw--se-scalar-flip"></a>

### NW--SE scalar flip

Since $`t_0=+1`$,

```math
\bar\lambda\chi_g=-\bar\chi_g\lambda.
```

Thus the $`\chi_g\lambda`$ terms in (5.3) and (5.7) are

```math
\begin{aligned}
-8i\sigma\rho\bar\lambda\chi_g
+8i\rho\sigma\bar\chi_g\lambda
&=+8i\sigma\rho\bar\chi_g\lambda
  +8i\sigma\rho\bar\chi_g\lambda
\\
&=16i\sigma\rho\bar\chi_g\lambda
\end{aligned}
\tag{6.3}
```

gives this result.

<a id="63-nw--se-rank-two-flip"></a>

### NW--SE rank-two flip

Since $`t_2=-1`$,

```math
\bar\lambda\gamma\!\cdot\!T_g\psi
=-t_2\bar\psi\gamma\!\cdot\!T_g\lambda
=\bar\psi\gamma\!\cdot\!T_g\lambda.
```

Thus

```math
i\rho\bar\lambda\gamma\!\cdot\!T_g\psi
+i\rho\bar\psi\gamma\!\cdot\!T_g\lambda
=2i\rho\bar\psi\gamma\!\cdot\!T_g\lambda.
\tag{6.4}
```

<a id="64-derivative-terms"></a>

### Derivative terms

The two terms of structure $`\bar\lambda\not D\psi`$ directly sum to

```math
-\frac12\rho\bar\lambda\not D\psi
-\frac14\rho\bar\lambda\not D\psi
=-\frac34\rho\bar\lambda\not D\psi
\tag{6.5}
```

No further integration by parts is performed at this stage;
$`-\frac14\rho\bar\psi\not D\lambda`$ remains separate.

<a id="65-field-strength-fermion-terms"></a>

### Field-strength fermion terms

The $`\widehat F`$ and $`F`$ terms in (5.3) and (5.5) are

```math
\begin{aligned}
-\frac{i}{8}\bar\lambda\gamma\!\cdot\!\widehat F\psi
-\frac{i}{16}\bar\lambda\gamma\!\cdot\!F\psi
&=-\frac{i}{16}\bar\lambda
 \gamma\!\cdot\!(2\widehat F+F)\psi.
\end{aligned}
\tag{6.6}
```

Here $`F`$ has not been identified with $`\widehat F`$.

<a id="66-gauging-term-with-one-gravitino"></a>

### Gauging term with one gravitino

The coefficients of the same monomial in (5.8) and (5.9) sum to

```math
\frac14g\rho\sigma^{-1}
+\frac18g\rho\sigma^{-1}
=\frac38g\rho\sigma^{-1}
\tag{6.7}
```

in this sum.

<a id="67-four-fermion-term-with-one-gravitino"></a>

### Four-fermion term with one gravitino

For identical spinors, $`t_0=+1`$

```math
\bar\psi_i\psi_j=\bar\psi_j\psi_i,
\qquad
\bar\psi_{(i}\psi_{j)}=\bar\psi_i\psi_j
```

Thus the terms in (5.8) and (5.9) give

```math
-\frac{i}{8}\rho\sigma^{-1}
 (\bar\psi_a^i\gamma^a\lambda^j)(\bar\psi_i\psi_j)
-\frac{i}{16}\rho\sigma^{-1}
 (\bar\psi_a^i\gamma^a\lambda^j)(\bar\psi_i\psi_j)
```

```math
\boxed{
=-\frac{3i}{16}\rho\sigma^{-1}
 (\bar\psi_a^i\gamma^a\lambda^j)(\bar\psi_i\psi_j)}
\tag{6.8}
```

combine in this form.

<a id="68-bosonic-supercovariant-blocks"></a>

### Bosonic supercovariant blocks

The equal tensor structures in (5.5) and (5.7) are grouped as

```math
-\frac14\rho F_{ab}\widehat G^{ab}
-\frac14\rho\widehat G_{ab}\widehat F^{ab}
=-\frac\rho4
 \left(F_{ab}\widehat G^{ab}
       +\widehat G_{ab}\widehat F^{ab}\right),
\tag{6.9}
```

```math
4\sigma\rho F^{ab}T_{g\,ab}
+4\sigma\rho\widehat F^{ab}T_{g\,ab}
=4\sigma\rho(F^{ab}+\widehat F^{ab})T_{g\,ab}
\tag{6.10}
```

Again, neither $`F=\widehat F`$ nor $`G=\widehat G`$ is assumed.

<a id="7-full-collected-result"></a>

## Full collected result

To keep the result readable,

```math
\mathscr L_{V\mathbb L}
=\mathscr L_{[0]}+\mathscr L_{[1]}+\mathscr L_{[2]}
\tag{7.1}
```

Here $`[n]`$ counts only the gravitino $`\psi_a^i`$ factors explicitly written
in (3.2'). Since possible gravitino completions inside hatted objects
are unexpanded, this does not classify total fermion degree.

<a id="71-block-without-explicit-gravitini"></a>

### Block without explicit gravitini

```math
\boxed{
\begin{aligned}
\mathscr L_{[0]}
={}&
\sigma Y^{ij}Y_{ij}
-\frac12g\rho\sigma^{-1}Y^{ij}L_{ij}
+\frac{i}{4}\rho\sigma^{-1}Y_{ij}\bar\psi^i\psi^j
-iY_{ij}\bar\lambda^i\psi^j
\\
&+\frac12\rho^2\square^C\sigma
+\frac12\rho\sigma\square^C\rho
+\frac12\rho D_a\rho D^a\sigma
-4\rho^2\sigma
 \left(D_g+\frac{26}{3}T_g^2\right)
\\
&-\frac14\sigma F_{ab}\widehat F^{ab}
-\frac{\rho}{4}
 \left(F_{ab}\widehat G^{ab}
       +\widehat G_{ab}\widehat F^{ab}\right)
\\
&+4\sigma\rho(F^{ab}+\widehat F^{ab})T_{g\,ab}
+4\rho^2\widehat G^{ab}T_{g\,ab}
-\frac18\varepsilon^{abcde}F_{ab}F_{cd}C_e
\\
&-\frac12\sigma\bar\lambda\not D\lambda
-\frac34\rho\bar\lambda\not D\psi
-\frac14\rho\bar\psi\not D\lambda
+\frac{i}{4}\bar\lambda(\not D\rho)\psi
\\
&+i\sigma\bar\lambda\gamma\!\cdot\!T_g\lambda
+2i\rho\bar\psi\gamma\!\cdot\!T_g\lambda
-\frac{i}{8}\bar\lambda\gamma\!\cdot\!\widehat G\lambda
\\
&-\frac{i}{16}\bar\lambda
 \gamma\!\cdot\!(2\widehat F+F)\psi
+16i\sigma\rho\bar\chi_g\lambda
+8i\rho^2\bar\chi_g\psi
\\
&+\frac18\sigma^{-1}
 (\bar\lambda^i\lambda^j)(\bar\psi_i\psi_j)
+\frac{i}{4}g\sigma^{-1}L_{ij}\bar\lambda^i\lambda^j.
\end{aligned}}
\tag{7.2}
```

<a id="72-block-with-one-explicit-gravitino"></a>

### Block with one explicit gravitino

```math
\boxed{
\begin{aligned}
\mathscr L_{[1]}
={}&
-\frac12\sigma Y_{ij}\bar\psi_a^i\gamma^a\lambda^j
-\frac14\rho Y_{ij}\bar\psi_a^i\gamma^a\psi^j
+\frac38g\rho\sigma^{-1}L_{ij}
 \bar\psi_a^i\gamma^a\lambda^j
\\
&+\frac{i}{4}\rho\sigma
 \bar\psi_a\gamma^a\not D\lambda
+\frac{i}{4}\rho^2
 \bar\psi_a\gamma^a\not D\psi
\\
&+\frac12\rho\sigma
 \bar\psi_a\gamma^a\gamma\!\cdot\!T_g\lambda
+\frac12\rho^2
 \bar\psi_a\gamma^a\gamma\!\cdot\!T_g\psi
-4\sigma\rho^2\bar\psi_a\gamma^a\chi_g
\\
&-\frac{\rho}{16}
 \bar\psi_a\gamma^a\gamma\!\cdot\!\widehat G\lambda
-\frac{\rho}{16}
 \bar\psi_a\gamma^a\gamma\!\cdot\!\widehat F\psi
\\
&+\frac{\rho}{8}
 \bar\psi_a\gamma^a(\not D\sigma)\lambda
+\frac{\rho}{8}
 \bar\psi_a\gamma^a(\not D\rho)\psi
\\
&-\frac{3i}{16}\rho\sigma^{-1}
 (\bar\psi_a^i\gamma^a\lambda^j)(\bar\psi_i\psi_j)
\\
&+\frac{i}{4}
 (\bar\psi_a^i\gamma^a\lambda^j)
 \bar\lambda_{(i}\psi_{j)}.
\end{aligned}}
\tag{7.3}
```

<a id="73-block-with-two-explicit-gravitini"></a>

### Block with two explicit gravitini

```math
\boxed{
\begin{aligned}
\mathscr L_{[2]}
={}&
\frac{i}{4}\rho\sigma Y_{ij}
 \bar\psi_a^i\gamma^{ab}\psi_b^j
-\frac{i}{8}g\rho^2\sigma^{-1}L_{ij}
 \bar\psi_a^i\gamma^{ab}\psi_b^j
\\
&-\frac1{16}\rho^2\sigma^{-1}
 (\bar\psi_a^i\gamma^{ab}\psi_b^j)
 (\bar\psi_i\psi_j)
\\
&+\frac18\rho
 (\bar\psi_a^i\gamma^{ab}\psi_b^j)
 \bar\lambda_{(i}\psi_{j)}.
\end{aligned}}
\tag{7.4}
```

<a id="8-separating-explicit-g-dependence"></a>

## Separating explicit $`g`$ dependence

Selecting from (7.2)–(7.4) all map terms whose coefficients explicitly contain $`g`$ gives

```math
\boxed{
\begin{aligned}
\Delta_g^{\mathrm{explicit}}\mathscr L_{V\mathbb L}
={}&-\frac12g\rho\sigma^{-1}Y^{ij}L_{ij}
+\frac{i}{4}g\sigma^{-1}L_{ij}\bar\lambda^i\lambda^j
\\
&+\frac38g\rho\sigma^{-1}L_{ij}
 \bar\psi_a^i\gamma^a\lambda^j
\\
&-\frac{i}{8}g\rho^2\sigma^{-1}L_{ij}
 \bar\psi_a^i\gamma^{ab}\psi_b^j.
\end{aligned}}
\tag{8.1}
```

This separates only the $`g`$ factors explicitly visible in the formulas.
No further assumption is made about the implicit $`g`$ dependence
of the $`T_g,D_g,\chi_g,\widehat F,\widehat G`$ objects themselves.

<a id="9-scope-of-the-result"></a>

## Scope of the result

The resulting (7.1)–(7.4):

- is a direct component substitution into the supplied density formula (3.2);
- is complete and off shell;
- uses no EOM, auxiliary-field elimination, gauge fixing, or field redefinition;
- identifies neither $`F`$ with $`\widehat F`$ nor $`G`$ with $`\widehat G`$;
- uses only the SU(2), NW–SE flip, and gamma-dot conventions in `CONVENTIONS.md`.

