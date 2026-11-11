# Cancellation of the singlet bivector

## 1. Problem and target

Starting point: the **29-term** coefficient M11d, equivalently Part V G709
of `DERIVATION-fermionic-map.md`. We prove that this coefficient vanishes;
we do not infer its vanishing from the desired linear-multiplet law.

The inputs are master C01–C05, G01–G03, W03, R03 and the adopted M08.
G03 is anchored to W(3.9)–(3.12), including footnote 5; R03 is the
project's explicitly derived operational curvature, not literal OP(2.7).
The conclusion is conditional on those already locked inputs. No change
to a source coefficient or convention is made here.

A1. Work off shell, with all supercovariant fermions retained.
A2. Use only conventional constraints, not field equations.
A3. A connection-normal frame, when used to derive a tensor identity, is
only a local coefficient calculation as in H54–H55. Curvatures and their
fermionic parts remain nonzero. No physical background is selected.

## 2. Convention ledger

<!-- ASSERT_CONVENTION: natural_units=hbar=c=1; metric_signature=(-,+,+,+,+); source_lock=UNG-WEYL2-OP58-CONVENTIONS-v5; epsilon_upper_01234=+1; gamma_upper_01234=+i -->

In this proof only, omit hats by writing
$`R_{ab}^i=\widehat R_{ab}^i(Q)`$ and $`C_{abcd}=\widehat C_{abcd}`$.
These are the original curvatures, not new fields. Lorentz indices run
from 0 to 4. Raise them with $`\eta`$; all SU(2) contractions are the locked
NW–SE contractions. Antisymmetrization has unit weight. Pair sums include
both orders. In particular the coefficient multiplies $`\gamma_{ab}`$,
without an extra $`1/2`$.

The odd contracted Majorana bilinears obey

```math
\bar u v=-\bar v u,\qquad
\bar u\gamma_a v=-\bar v\gamma_a u,\qquad
\bar u\gamma_{ab}v=+\bar v\gamma_{ab}u.
\tag{B01}
```

Majorana conjugation is linear, including in $`i`$. The dualities are

```math
\gamma_{abc}=-\frac i2\varepsilon_{abcde}\gamma^{de},\qquad
\gamma_{abcd}=i\varepsilon_{abcde}\gamma^e,\qquad
\gamma_{abcde}=i\varepsilon_{abcde}.
\tag{B02}
```

Thus rank three contributes to the bivector coefficient already collected
in M11d. No rank-three contribution is discarded in the present proof.

## 3. Definitions and required identities

<!-- ASSERT_CONVENTION: source_lock=UNG-WEYL2-OP58-CONVENTIONS-v5; covariant_derivative=G01; curvature=R03 -->

The conventional constraints and their Bianchi consequences are

```math
R(P)=0,\quad R(D)=0,\quad \gamma^aR_{ab}=0,\quad
C_{ab}{}^{b}{}_{c}=0,\quad
C_{abcd}=C_{cdab},\quad C_{[abc]d}=0.
\tag{B03}
```

The last two statements concern the constrained R03 curvature. They are
not assumptions about an arbitrary hatted four-index tensor. The cyclic
constraint follows from the $`R(P)=0`$ Bianchi identity and $`R(D)=0`$ in G03;
pair exchange follows from that cyclic identity and antisymmetry within
both pairs. In the local normal frame of H54, $`C=R(\omega)`$ at the point,
and this argument reduces to the ordinary cyclic identity. Its derivative
is different: derivatives of the fermionic connection terms must remain.

The gamma trace implies the source footnote-5 identity

```math
0=\gamma_{ab}R_{cd}-\gamma_{ac}R_{bd}+\gamma_{ad}R_{bc}
 +\gamma_{bc}R_{ad}-\gamma_{bd}R_{ac}+\gamma_{cd}R_{ab}.
\tag{B04}
```

For later epsilon contractions we also need

```math
\varepsilon_{abcde}R^{de}
=2i(\gamma_aR_{bc}+\gamma_bR_{ca}+\gamma_cR_{ab}).
\tag{B05}
```

Here is its gamma-algebra derivation. The gamma trace gives
$`\gamma^{cd}R_{cd}=0`$ and
$`\gamma_a{}^cR_{bc}=R_{ab}`$. Therefore

```math
\begin{aligned}
0=\gamma_{ab}\gamma_{cd}R^{cd}
&=\gamma_{abcd}R^{cd}
 +4\gamma_{[a}{}^cR_{b]c}-2R_{ab}\\
&=\gamma_{abcd}R^{cd}+2R_{ab}.
\end{aligned}\tag{B06}
```

Multiply by $`\gamma_a`$, with the free pair in B06 renamed $`b,c`$:

```math
\begin{aligned}
-2\gamma_aR_{bc}
&=\gamma_a\gamma_{bcde}R^{de}\\
&=\gamma_{abcde}R^{de}
  +2\gamma_{bce}R_a{}^e\\
&=\gamma_{abcde}R^{de}
  +2\gamma_cR_{ab}-2\gamma_bR_{ac}.
\end{aligned}\tag{B07}
```

Insert $`\gamma_{abcde}=i\varepsilon_{abcde}`$ to obtain B05.
Contracting B05 with $`\gamma^c`$ gives

```math
\varepsilon_{abcde}\gamma^cR^{de}
=2i(-2-2+5)R_{ab}=2iR_{ab}.
\tag{B08}
```

The barred identities follow by linear Majorana conjugation; no complex
conjugation of the displayed $`i`$ is performed.

## 4. Detailed derivation

### 4.1 The four CTT terms

<!-- ASSERT_CONVENTION: source_lock=UNG-WEYL2-OP58-CONVENTIONS-v5; antisymmetrization=unit_weight -->

The starting terms are

```math
\begin{aligned}
&4C^{[a}{}_{cde}T^{c b]}T^{de}
-8C^{[a}{}_{cde}T^{cd}T^{e b]}\\
&\qquad+8C^{[a}{}_{c}{}^{b]}{}_{d}T^c{}_eT^{de}
-\frac83C_{cd}{}^{[a}{}_eT^{cd}T^{e b]}.
\end{aligned}\tag{B09}
```

The cyclic identity, contracted with $`T^{cd}`$, gives
$`C_{acde}T^{cd}=-C_{aecd}T^{cd}/2`$.
The third term vanishes because $`T^c{}_eT^{de}`$ is symmetric in $`c,d`$,
whereas the antisymmetric part in $`a,b`$ of $`C_{acbd}`$ is antisymmetric
in $`c,d`$. Pair exchange converts the last term to the first contraction.
Consequently B09 is

```math
\left(4+4+0-\frac83\right)
 C^{[a}{}_{cde}T^{c b]}T^{de}
=\frac{16}{3}C^{[a}{}_{cde}T^{c b]}T^{de}.
\tag{B10}
```

### 4.2 The seven C DT terms

Write them in their original order:

```math
\begin{aligned}
&\frac16C_{cdef}\varepsilon^{cdab}{}_g\mathcal D^eT^{fg}
+\frac1{12}C_{cdef}\varepsilon^{cdab}{}_g\mathcal D^gT^{ef}\\
&+\frac1{12}C_{cdef}\varepsilon^{cdeab}\mathcal D_gT^{fg}
+\frac13C_{cdef}\varepsilon^{ceab}{}_g\mathcal D^dT^{fg}\\
&-\frac1{12}C_{cdef}\varepsilon^{cefab}\mathcal D_gT^{dg}
-\frac13C_{cdef}\varepsilon^{efab}{}_g\mathcal D^cT^{dg}\\
&-\frac1{12}C_{cdef}\varepsilon^{efab}{}_g\mathcal D^gT^{cd}.
\end{aligned}\tag{B11}
```

Terms 2 and 7 cancel by $`(c,d)\leftrightarrow(e,f)`$ and pair exchange.
Terms 3 and 5 vanish because the epsilon antisymmetrizes three indices
of $`C`$. Term 6 becomes
$`-C_{cdef}\varepsilon^{cdab}{}_g\mathcal D^eT^{fg}/3`$
by the same pair interchange. For term 4, the cyclic identity gives

```math
C_{cdef}\varepsilon^{ceab}{}_g
=\frac12C_{cedf}\varepsilon^{ceab}{}_g.
\tag{B12}
```

Rename $`d\leftrightarrow e`$ in its contraction. All seven terms are now

```math
\left(\frac16+\frac16-\frac13\right)
 C_{cdef}\varepsilon^{cdab}{}_g\mathcal D^eT^{fg}=0.
\tag{B13}
```

### 4.3 The eight second-derivative terms

Pair the ordered derivatives in M11d, without integrating by parts:

```math
\begin{aligned}
\frac{32}{3}\big\{&
T^{[a}{}_c[\mathcal D^{b]},\mathcal D_d]T^{cd}
+T^{[a}{}_c[\mathcal D_d,\mathcal D^c]T^{b]d}\\
&+T_{cd}[\mathcal D^c,\mathcal D^{[a}]T^{b]d}
+\tfrac12T_{cd}[\mathcal D^c,\mathcal D^d]T^{ab}
-\tfrac12T_{cd}[\mathcal D^a,\mathcal D^b]T^{cd}\big\}.
\end{aligned}\tag{B14}
```

For example, the first and third original derivative terms produce the
first commutator. The second and fourth produce the second commutator;
the sixth and seventh produce the third. Antisymmetry in $`c,d`$ and $`a,b`$
produces the two factors $`1/2`$ in the last two terms.

G01 gives a curvature acting by minus its local transformation. Since $`T`$
is an SU(2) singlet and S/K inert, and $`R(P)=R(D)=0`$, its full commutator is

```math
\begin{aligned}
[\mathcal D_a,\mathcal D_b]T_{cd}
={}&C_{ab c}{}^eT_{ed}+C_{ab d}{}^eT_{ce}\\
&-\frac i2\bar R_{ab}\gamma_{cd}\chi
+\frac{3i}{32}\bar R_{ab}R_{cd}.
\end{aligned}\tag{B15}
```

The last line is $`-\delta_Q(R_{ab})T_{cd}`$ with W03 inserted. In
particular it cannot be removed in an all-fermion calculation.

The Lorentz parts of the five contractions inside B14 are, respectively,

```math
\begin{array}{rcl}
T^{[a}{}_c(C^{b]}{}_{d}{}^c{}_eT^{ed}
 +C^{b]}{}_{d}{}^d{}_eT^{ce})
&=&-\tfrac12C^{[a}{}_{cde}T^{c b]}T^{de},\\
T^{[a}{}_c(C_d{}^{c b]}{}_eT^{ed}
 +C_d{}^{c d}{}_eT^{b]e})
&=&-\tfrac12C^{[a}{}_{cde}T^{c b]}T^{de},\\
T_{cd}(C^{c[a b]}{}_eT^{ed}
 +C^{c[a|d|}{}_eT^{b]e})
&=&-\tfrac12C^{[a}{}_{cde}T^{c b]}T^{de},\\
T_{cd}(C^{cd a}{}_eT^{eb}+C^{cd b}{}_eT^{ae})
&=&2C^{[a}{}_{cde}T^{c b]}T^{de},\\
T_{cd}(C^{ab c}{}_eT^{ed}+C^{ab d}{}_eT^{ce})
&=&0.
\end{array}\tag{B16}
```

In rows 1–2 the Ricci trace vanishes and the crossed contraction uses
$`C_{acde}T^{cd}=-C_{aecd}T^{cd}/2`$. In row 3 the first contraction is
symmetric in $`a,b`$ after pair exchange and $`TT`$ interchange; the second
uses the same crossed contraction. Row 4 has two equal antisymmetrized
contributions. In row 5 the Lorentz generator contracts the symmetric
$`TT`$ tensor. Including the explicit halves in B14 gives

```math
\frac{32}{3}\left(-\frac12-\frac12-\frac12+1-0\right)
C^{[a}{}_{cde}T^{c b]}T^{de}
=-\frac{16}{3}C^{[a}{}_{cde}T^{c b]}T^{de}.
\tag{B17}
```

This cancels B10.

### 4.4 Add every fermionic commutator contribution

The following table gives coefficients of the actual displayed contractions.
All entries multiply $`i`$. Column 2 is M11d; column 3 is the last line of
B15 substituted into B14. No term is suppressed in this addition.

| Contraction | M11d / i | B14 fermionic part / i | Sum / i |
|---|---:|---:|---:|
| $`T^{cd}\bar R^{ab}R_{cd}`$ | $`59/32`$ | $`-1`$ | $`27/32`$ |
| $`\bar R_{cd}\gamma^{[a\vert e\vert}R^{cd}T_e{}^{b]}`$ | $`29/32`$ | $`0`$ | $`29/32`$ |
| $`\bar R_c{}^{[a}R^c{}_dT^{d b]}`$ | $`-45/8`$ | $`2`$ | $`-29/8`$ |
| $`\bar R_c{}^{[a}\gamma^{b]d}R^c{}_eT_d{}^e`$ | $`27/16`$ | $`0`$ | $`27/16`$ |
| $`T_{cd}\bar R^{ab}\gamma^{cd}\chi`$ | $`47/8`$ | $`8/3`$ | $`205/24`$ |
| $`\bar R^{[a}{}_c\chi T^{c b]}`$ | $`32/3`$ | $`-32/3`$ | $`0`$ |
| $`\bar R^{[a}{}_c\gamma^{b]d}\chi T^c{}_d`$ | $`-79/2`$ | $`16/3`$ | $`-205/6`$ |
| $`T^{cd}\bar R_{cd}\gamma^{ab}\chi`$ | $`269/24`$ | $`-8/3`$ | $`205/24`$ |

For transparency, the substitution which produces column 3 before collection is

```math
\begin{aligned}
\frac{32}{3}\big\{&
T^{[a}{}_c(-\tfrac i2\bar R^{b]}{}_d\gamma^{cd}\chi
 +\tfrac{3i}{32}\bar R^{b]}{}_dR^{cd})\\
&+T^{[a}{}_c(-\tfrac i2\bar R_d{}^c\gamma^{b]d}\chi
 +\tfrac{3i}{32}\bar R_d{}^cR^{b]d})\\
&+T_{cd}(-\tfrac i2\bar R^{c[a}\gamma^{b]d}\chi
 +\tfrac{3i}{32}\bar R^{c[a}R^{b]d})\\
&+\tfrac12T_{cd}(-\tfrac i2\bar R^{cd}\gamma^{ab}\chi
 +\tfrac{3i}{32}\bar R^{cd}R^{ab})\\
&-\tfrac12T_{cd}(-\tfrac i2\bar R^{ab}\gamma^{cd}\chi
 +\tfrac{3i}{32}\bar R^{ab}R^{cd})\big\}.
\end{aligned}\tag{B18}
```

Collecting this line with B01 yields precisely the table. Its sum is

```math
\begin{aligned}
&\frac{27i}{32}\left[
T^{cd}\bar R^{ab}R_{cd}
+2\bar R_c{}^{[a}\gamma^{b]d}R^c{}_eT_d{}^e\right]\\
+&\frac{29i}{32}\left[
\bar R_{cd}\gamma^{[a\vert e\vert}R^{cd}T_e{}^{b]}
-4\bar R_c{}^{[a}R^c{}_dT^{d b]}\right]\\
+&\frac{205i}{24}\left[
T_{cd}\bar R^{ab}\gamma^{cd}\chi
-4\bar R^{[a}{}_c\gamma^{b]d}\chi T^c{}_d
+T^{cd}\bar R_{cd}\gamma^{ab}\chi\right].
\end{aligned}\tag{B19}
```

Each bracket vanishes, as the following explicit contractions show.

**The chi bracket.** Conjugate B04, multiply by $`T^{cd}\chi`$:

```math
\begin{aligned}
0={}&(\bar R_{ab}\gamma_{cd}-\bar R_{ac}\gamma_{bd}
+\bar R_{ad}\gamma_{bc}+\bar R_{bc}\gamma_{ad}
-\bar R_{bd}\gamma_{ac}+\bar R_{cd}\gamma_{ab})T^{cd}\chi\\
={}&T^{cd}\bar R_{ab}\gamma_{cd}\chi
-4\bar R_{[a|c|}\gamma_{b]d}\chi T^{cd}
+T^{cd}\bar R_{cd}\gamma_{ab}\chi.
\end{aligned}\tag{B20}
```

Here terms 2–3 combine by $`c\leftrightarrow d`$, as do terms 4–5.

**The second RR bracket.** Contract B04 with $`\bar R^{cd}`$.
Use $`\bar R^{cd}\gamma_{ac}=\bar R_a{}^d`$,
$`\bar R^{cd}\gamma_{ad}=\bar R^c{}_a`$ and
$`\bar R^{cd}\gamma_{cd}=0`$. The four mixed terms are

```math
\begin{aligned}
&-\bar R_a{}^dR_{bd}+\bar R^c{}_aR_{bc}
 +\bar R_b{}^dR_{ad}-\bar R^c{}_bR_{ac}\\
&=-\bar R_{ca}R^c{}_b-\bar R_{ca}R^c{}_b
 -\bar R_{ca}R^c{}_b-\bar R_{ca}R^c{}_b.
\end{aligned}\tag{B21}
```

The last two signs use the scalar flip B01. Thus

```math
\bar R_{cd}\gamma_{ab}R^{cd}=4\bar R_{ca}R^c{}_b.
\tag{B22}
```

Multiplying by $`T^b{}_e`$ and antisymmetrizing the free indices proves the
second bracket of B19 is zero.

**The first RR bracket.** Use B04 on the indices $`b,c,d,e`$:

```math
\begin{aligned}
0=\bar R^{ae}\big(&\gamma_{bc}R_{de}-\gamma_{bd}R_{ce}
+\gamma_{be}R_{cd}+\gamma_{cd}R_{be}
-\gamma_{ce}R_{bd}+\gamma_{de}R_{bc}\big)T^{cd}\\
= {}&2\bar R^{ae}\gamma_{bc}R_{de}T^{cd}
+\bar R^{ae}\gamma_{cd}R_{be}T^{cd}
+\bar R^a{}_bR_{cd}T^{cd}
-2\bar R^a{}_cR_{bd}T^{cd}.
\end{aligned}\tag{B23}
```

The first pair uses $`c\leftrightarrow d`$; the last three gamma reductions
use the left gamma trace. Now antisymmetrize $`a,b`$.
The second term is symmetric in $`a,b`$ by the rank-two flip in B01.
The fourth is symmetric because interchanging the fermions gives minus
and interchanging $`c,d`$ in $`T^{cd}`$ gives a second minus. The surviving
terms give

```math
T^{cd}\bar R_{ab}R_{cd}
+2\bar R_{c[a}\gamma_{b]d}R^c{}_eT^{de}=0.
\tag{B24}
```

All of B19 has therefore vanished.

### 4.5 The two differentiated-curvature terms

These must not be discarded using the ordinary bosonic Bianchi identity.
Their sum is

```math
\varepsilon^{abcfg}T^{de}\mathcal D_cC_{defg}
+\varepsilon^{abef}{}_gT^{dg}\mathcal D_cC^c{}_{def}.
\tag{B25}
```

For the first term, pair exchange and the epsilon give
$`\varepsilon^{abcfg}T^{de}(\mathcal D_cC_{fgde} +\mathcal D_fC_{gcde}+\mathcal D_gC_{cfde})/3`$.
For the second, tracefreeness gives

```math
\mathcal D^cC_{cdef}
=\mathcal D^cC_{efcd}+\mathcal D_eC_f{}^c{}_{cd}
 +\mathcal D_fC^c{}_{ecd}.
\tag{B26}
```

The last two terms are zero traces, so this is exactly the contracted
cyclic derivative, not an assumption that it vanishes.

Differentiate R03 in the H54 connection-normal frame. The terms quadratic
in undifferentiated connections drop at the point; $`d\psi=R(Q)`$ and
$`df=R(K)`$ do not. For example,

```math
\begin{aligned}
\partial_{[a}(\bar\psi_b\gamma_dR_{c]e})
&=(\partial_{[a}\bar\psi_b)\gamma_dR_{c]e},\\
\partial_{[a}(\bar\psi_b\eta_{c]d}\gamma_e\chi)
&=(\partial_{[a}\bar\psi_b)\eta_{c]d}\gamma_e\chi.
\end{aligned}
```

Inserting the coefficients of R03, and then restoring the covariants,
gives the full cyclic identity

```math
\begin{aligned}
&\mathcal D_aC_{bcde}+\mathcal D_bC_{cade}+\mathcal D_cC_{abde}\\
={}&2\sum_{\mathrm{cyc}(abc)}
 [R(K)_{ab d}\eta_{ce}-R(K)_{ab e}\eta_{cd}]\\
&+\frac14\sum_{\mathrm{cyc}(abc)}
 [\bar R_{ab}\gamma_dR_{ce}-\bar R_{ab}\gamma_eR_{cd}
  +\bar R_{ab}\gamma_cR_{de}]\\
&+2\sum_{\mathrm{cyc}(abc)}
 [\eta_{cd}\bar R_{ab}\gamma_e\chi
 -\eta_{ce}\bar R_{ab}\gamma_d\chi].
\end{aligned}\tag{B27}
```

Here $`R(K)_{ab c}=2\partial_{[a}f_{b]c}`$ at that point. It denotes the
existing special-conformal curvature. Its trace vanishes: double-contract
B27 in $`(b,d)`$ and $`(c,e)`$. The left side is zero by the traces of $`C`$;
the first line on the right gives

```math
[2(5-1)-4+2(5-1)]R(K)_{ab}{}^b=12R(K)_{ab}{}^b.
\tag{B28}
```

In the fermionic terms every contraction contains a left or right gamma
trace, except $`\bar R_{bc}\gamma_aR^{bc}/4`$, which is zero by the
vector flip B01. Hence $`R(K)_{ab}{}^b=0`$ follows without an EOM.

The two terms of B25 give respectively the following special-conformal
and chi contributions:

```math
\begin{array}{c|c|c}
&\text{first term of B25}&\text{second term of B25}\\ \hline
R(K)&-4\varepsilon^{abcde}R(K)_{cd f}T_e{}^f
&+4\varepsilon^{abcde}R(K)_{cd f}T_e{}^f
 -4\varepsilon^{abcde}R(K)_{cf}{}^fT_{de}\\
R\chi&-4\varepsilon^{cdab}{}_eT_f{}^e\bar R_{cd}\gamma^f\chi
&+4\varepsilon^{cdab}{}_eT_f{}^e\bar R_{cd}\gamma^f\chi.
\end{array}\tag{B29}
```

Both rows cancel, using B28 in the first.

For the RR terms, the first term of B25 becomes

```math
\begin{aligned}
&\frac12\varepsilon^{abcfg}T^{de}\bar R_{cf}\gamma_dR_{ge}
+\frac14\varepsilon^{abcfg}T^{de}\bar R_{cf}\gamma_gR_{de}\\
={}&iT^{de}(\bar R^{bg}\gamma^a+\bar R^{ga}\gamma^b
 +\bar R^{ab}\gamma^g)\gamma_dR_{ge}
 +\frac i2T^{de}\bar R^{ab}R_{de}\\
={}&2i\bar R_c{}^{[a}\gamma^{b]d}R^c{}_eT_d{}^e
 -2i\bar R_c{}^{[a}R^c{}_dT^{d b]}
 +\frac{5i}{2}T^{cd}\bar R^{ab}R_{cd}\\
={}&\frac{3i}{2}T^{cd}\bar R^{ab}R_{cd}
 -2i\bar R_c{}^{[a}R^c{}_dT^{d b]}.
\end{aligned}\tag{B30}
```

The second equality uses barred B05/B08; the third uses
$`\gamma^g\gamma_dR_{ge}=2R_{de}`$ and
$`\gamma^b\gamma_d=\gamma^b{}_d+\delta^b_d`$.
The last uses B24.

Contracting the RR line of B27 for the second term of B25 leaves

```math
\frac12\varepsilon^{abefg}T^d{}_g
 [\bar R_{ce}\gamma_dR^c{}_f+\bar R_{ce}\gamma_fR^c{}_d].
\tag{B31}
```

The discarded contractions here are individually gamma traces, not a
fermion truncation. To evaluate the two displayed terms, use B05 to write

```math
\gamma_dR_{cf}={1\over2i}\varepsilon_{dcfhk}R^{hk}
 -\gamma_cR_{fd}-\gamma_fR_{dc}.
\tag{B32}
```

The middle term vanishes against $`\bar R_{ce}`$. The last reproduces the
second term of B31. For that second term, apply barred B05; its gamma-trace
term vanishes and the remaining gamma term is minus itself after
$`e\leftrightarrow f`$. Therefore

```math
\begin{aligned}
\frac12\varepsilon_{abefg}T^{dg}\bar R_c{}^e\gamma^fR^c{}_d
&={1\over8i}\varepsilon_{abefg}\varepsilon^{fcehk}
 T^{dg}\bar R_{hk}R_{cd}\\
&=-\frac i2T^{cd}\bar R_{ab}R_{cd}.
\end{aligned}\tag{B33}
```

The epsilon-product calculations in B32–B33 are explicitly

```math
\begin{aligned}
\varepsilon_{abefg}\varepsilon^{fcehk}
 &=-2\delta_{abg}^{chk},\\
\delta_{abg}^{chk}T^{dg}\bar R_{hk}R_{cd}
 &=2T^{dg}(\bar R_{bg}R_{ad}+\bar R_{ga}R_{bd}
 +\bar R_{ab}R_{gd})\\
 &=-2T^{cd}\bar R_{ab}R_{cd},\\[2pt]
\varepsilon_{abefg}\varepsilon^{dcfhk}
 &=\delta_{abeg}^{dchk},\\
\delta_{abeg}^{dchk}T_d{}^g\bar R_c{}^eR_{hk}
 &=(\delta_a^d\delta_{beg}^{chk}
 -\delta_b^d\delta_{aeg}^{chk}
 +\delta_e^d\delta_{abg}^{chk}
 -\delta_g^d\delta_{abe}^{chk})T_d{}^g\bar R_c{}^eR_{hk}\\
 &=-8\bar R_{c[a}R^c{}_dT^d{}_{b]}
   +2T^{cd}\bar R_{ab}R_{cd}.
\end{aligned}\tag{B34}
```

Here generalized deltas are unnormalized determinants. In the first
three-index delta expansion the first two terms cancel because
$`T^{dg}\bar R_{bg}R_{ad}`$ is symmetric in $`a,b`$ (scalar flip and
$`d\leftrightarrow g`$). In the four-index expansion the first two terms
give the displayed $`-8`$ contraction; the third gives the displayed $`2`$
contraction; the fourth is $`T_d{}^d=0`$.

Thus the first term of B31 is
$`-iT^{cd}\bar R_{ab}R_{cd}+2i\bar R_{c[a}R^c{}_dT^d{}_{b]}`$,
and adding B33 gives

```math
-\frac{3i}{2}T^{cd}\bar R^{ab}R_{cd}
+2i\bar R_c{}^{[a}R^c{}_dT^{d b]}.
\tag{B35}
```

This is exactly minus B30. The complete B25, including all its fermionic
Bianchi terms, is zero.

## 5. Consistency checks

<!-- ASSERT_CONVENTION: source_lock=UNG-WEYL2-OP58-CONVENTIONS-v5; fermion_scope=all_orders; equations_of_motion=none -->

Every contribution has weight four:
$`w(C)=2`$, $`w(T)=1`$, $`w(\mathcal D)=1`$,
$`w(R(Q))=w(\chi)=3/2`$. Hence
$`w(CTT)=w(C\mathcal DT)=w(T\mathcal DC)=w(T\mathcal D\mathcal DT) =w(T\bar RR)=w(T\bar R\chi)=4`$.
All free pairs are antisymmetric, all bilinears are Grassmann even, and the
result multiplies the odd parameter of weight $`-1/2`$ to give weight $`7/2`$.
No integration by parts, boundary condition, EOM or perturbative expansion
is used. In the bosonic limit B10+B17 still cancels; in the $`T=0`$ limit
every term of M11d is zero. Arbitrary $`\mathcal DT`$ is retained in B11–B13.

The independent component check is [verify_weyl_bivector_cancellation.py](../src/reference_checks/verify_weyl_bivector_cancellation.py).
The [component-check runner](../checks/reference_suite.py) generates its
`BIVECTOR-CANCELLATION-CHECKS.json` report in a temporary workspace.
It tests B05, B15, B19–B24 and the differentiated-curvature contractions
with explicit Lorentzian gamma matrices, constrained Weyl tensors,
gamma-traceless spinor two-forms, two independent odd generators and SU(2)
contractions. These finite component checks support the displayed proof;
random samples alone are not a proof of a tensor identity.

## 6. Final result

All 29 terms have now been accounted for:

```math
\underbrace{4\ CTT+8\ T\mathcal D\mathcal DT
 +4\ T\bar RR+4\ T\bar R\chi}_{\text{B10+B17+B19}=0}
\quad+\underbrace{7\ C\mathcal DT}_{\text{B13}=0}
\quad+\underbrace{2\ T\mathcal DC}_{\text{B29+B30+B35}=0}.
```

The integers in this accounting line count terms; they are not coefficients
of a tensor equation. The actual result is

```math
\boxed{k^{ab}=0,\qquad
\left.\delta_Q\varphi_W^i\right|_{\mathrm{SU(2)\ singlet}}
=(p+\gamma_a t^a)\epsilon^i.}
\tag{B36}
```

## 7. Convention dependence and remaining uncertainties

This proves the cancellation of M11d for the adopted M08 and locked
operational covariants. It does not establish the traceless SU(2) sector,
identify the final simplified E/N composites, prove S(varphi), or certify
nonlinear closure/the full invariant. In particular the full variation may
still contain the prescribed triplet $`\gamma\cdot T\,L^{ij}\epsilon_j`$;
B36 concerns only the singlet coefficient requested by the user.
