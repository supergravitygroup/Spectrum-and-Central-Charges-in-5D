---
title: Canonical vector coefficient in Q(varphi_W)
date: 2026-09-18
status: completed
assumptions: [A1, A2, A3, A4]
method: exact Clifford, Schouten and full covariant-commutator reduction
result: All34 vector terms reduced to the explicit VC42 coefficient with24 product-rule summands
verified_limits: [bosonic source M03, pure curvature, constant T with vanishing curvatures and fermions]
convention_lock: UNG-WEYL2-OP58-CONVENTIONS-v5
---
# Part VIII — Canonical vector coefficient of the full Q variation

## 44. Problem and Target

**Derived result, 2026-09-18.** We simplify the complete coefficient of
$`\gamma_a\epsilon^i`$ in Q(M08), starting from all **34** terms of
G708/master M11c. This continues the actual variation in Parts III–V; the
printed bosonic vector M03 is a comparison at the end, not an ansatz for
its fermionic completion.

The target is

```math
\left.\delta_Q\varphi_W^i\right|_{\text{vector singlet}}
=\gamma_a t^a\epsilon^i.
\tag{VC01}
```

A1. Work off shell, in the ungauged, gauge-unfixed Standard-Weyl variables
of the map, with the M08 coefficient $`8/3`$ from the derivation in M07–M08/X12.

A2. Retain the complete supercovariant fields, derivatives and all their
physical fermion orders. A hat is never replaced by its bosonic part.

A3. Use the conventional curvature identities already derived in M12.
No field equation, background, gauge fixing, Dilaton-Weyl substitution or
auxiliary-field elimination is permitted in this calculation.

A4. We use exact covariant product rules. Every derivative displayed below
is retained. There is no integration by parts or equality modulo a
boundary term.

The two abbreviations $`R_{ab}=\widehat R_{ab}(Q)`$ and
$`C_{abcd}=\widehat C_{abcd}`$ are used only inside the calculation. These
are the existing physical curvatures; no new response fields are defined.
The final answer restores the full names.

## 45. Convention Ledger

<!-- ASSERT_CONVENTION: natural_units=hbar=c=1, metric_signature=(-,+,+,+,+), source_lock=UNG-WEYL2-OP58-CONVENTIONS-v5 -->

- Tangent indices $`a,b,\ldots=0,\ldots,4`$; $`\eta_{ab}=\mathop{\mathrm{diag}}\nolimits(-,+,+,+,+)`$.
- $`\varepsilon^{01234}=+1`$, $`\varepsilon_{01234}=-1`$;
  $`\gamma^{01234}=i\mathbf1`$, $`\{\gamma_a,\gamma_b\}=2\eta_{ab}`$.
- Antisymmetrization has unit weight; antisymmetric repeated pairs are
  summed over all ordered values, with no implicit extra $`1/2`$.
- $`R,\chi,\epsilon`$ are Grassmann odd. Their contracted symplectic-Majorana
  bilinears obey C03. In particular scalar and vector bilinears change
  sign under interchange; bivector bilinears do not. The Majorana bar
  used in these identities is linear in $`i`$.
- $`\mathcal D`$ is the complete G01/G03 derivative. It preserves the
  invariant tensors and obeys the tensor product rule. Its two derivatives
  may be interchanged only with the **full** M12b commutator.
- The Riemann sign is G02,
  $`[\nabla_\mu,\nabla_\nu]X^\rho=R^\rho{}_{\sigma\mu\nu}X^\sigma`$.
  Coupling conventions, Fourier transforms, state normalizations and
  renormalization schemes do not enter this local algebraic identity;
  the later action normalization is unchanged.

The weights are $`w(T)=1`$, $`w(C)=w(D)=w(\widehat R(V))=2`$,
$`w(R)=w(\chi)=3/2`$, $`w(\mathcal D_a)=1`$ and $`w(\epsilon)=-1/2`$.
Thus every term in $`t^a`$ must have weight four.

**Source anchors:** master C01–C06, G01–G03 and R01–R07 fix the
conventions and full curvatures; M08 fixes the spinor being varied;
M11c/G708 is the starting sum; M12a–M12d/Part VI prove the curvature and
spinor identities used below. M03 is the extracted vector line of the
local Özkan–Pang Eq. (5.8). No new external formula is imported.

## 46. Definitions and Required Identities

The Clifford products needed inside bilinears are

```math
\begin{aligned}
\gamma_a\gamma_{bc}
&=\gamma_{abc}+\eta_{ab}\gamma_c-\eta_{ac}\gamma_b,\\
\gamma^b\gamma_{bc}&=4\gamma_c,\\
\gamma_{abc}&=-\frac i2\varepsilon_{abcde}\gamma^{de},\\
\gamma_{abcd}&=i\varepsilon_{abcde}\gamma^e.
\end{aligned}
\tag{VC02}
```

The second line follows directly from
$`\gamma^b(\gamma_b\gamma_c-\eta_{bc})=5\gamma_c-\gamma_c`$.
The last two lines use the locked orientation and volume gamma. They
include the rank-three and rank-four contributions; no higher-rank
Clifford structure is discarded.

The conventional constraints and their consequences are

```math
\begin{gathered}
C_{abcd}=-C_{bacd}=-C_{abdc}=C_{cdab},\qquad
C_{[abc]d}=0,\qquad C^a{}_{bad}=0,\\
\gamma^aR_{ab}=0,\qquad \bar R_{ab}\gamma^a=\bar R_{ab}\gamma^b=0,
\qquad \gamma_{[ab}R_{cd]}=0,\\
\varepsilon_{abcde}R^{de}
=2i(\gamma_aR_{bc}+\gamma_bR_{ca}+\gamma_cR_{ab}),\\
\bar u v=-\bar v u,\qquad
\bar u\gamma_a v=-\bar v\gamma_a u,\qquad
\bar u\gamma_{ab}v=+\bar v\gamma_{ab}u.
\end{gathered}
\tag{VC03}
```

The last line applies to contracted SU(2) indices and odd spinors,
including differentiated odd spinors. Its signs include their Grassmann
interchange. The barred version of the preceding duality has the same
coefficient $`2i`$.

The derivative commutator is, without a fermion truncation,

```math
[\mathcal D_a,\mathcal D_b]T_{cd}
=C_{ab c}{}^eT_{ed}+C_{ab d}{}^eT_{ce}
-\frac i2\bar R_{ab}\gamma_{cd}\chi
+\frac{3i}{32}\bar R_{ab}R_{cd}.
\tag{VC04}
```

For traceability, here is the complete starting expression. The labels
“1–6”, etc., number consecutive summands, rather than new fields.

**Terms 1–6:**

```math
\begin{aligned}
&-\frac{i}{32}C_{cdef}C^{cd}{}_{gh}\varepsilon^{efgha}
+4iC_{cdef}\varepsilon^{cea}{}_{gh}T^{df}T^{gh}\\
&+8iC_{cdef}\varepsilon^{cea}{}_{gh}T^{dg}T^{fh}
-4iC_{cdef}\varepsilon^{cefa}{}_{g}T^d{}_hT^{gh}\\
&-\frac{22i}{3}C_{cdef}\varepsilon^{efa}{}_{gh}T^{cd}T^{gh}
+4iC_{cdef}\varepsilon^{efa}{}_{gh}T^{cg}T^{dh}.
\end{aligned}
\tag{VC05a}
```

**Terms 7–13:**

```math
\begin{aligned}
&-\frac i3 C^a{}_{cde}\mathcal D^cT^{de}
+\frac{8i}{3}C_{cd}{}^a{}_e\mathcal D^cT^{de}
-\frac i3 C_{cd}{}^a{}_e\mathcal D^eT^{cd}\\
&-4i(\mathcal D_cC^c{}_d{}^a{}_e)T^{de}
+4i(\mathcal D_cC_{de}{}^{ca})T^{de}\\
&+\frac{32i}{3}D\mathcal D_cT^{ac}
-\frac{32i}{3}(\mathcal D_cD)T^{ca}.
\end{aligned}
\tag{VC05b}
```

**Terms 14–18:**

```math
\begin{aligned}
&-\frac{256i}{3}T^a{}_cT^c{}_d\mathcal D_eT^{de}
+\frac{128i}{9}T^a{}_cT_{de}\mathcal D^cT^{de}\\
&+\frac{256i}{3}T^a{}_cT_{de}\mathcal D^dT^{ce}
+\frac{64i}{9}T_{cd}T^{cd}\mathcal D_eT^{ae}
+\frac{256i}{3}T_{cd}T^c{}_e\mathcal D^dT^{ae}.
\end{aligned}
\tag{VC05c}
```

**Terms 19–25:**

```math
\begin{aligned}
&+\frac{32i}{3}\varepsilon^a{}_{cdef}T^{cd}\mathcal D^e\mathcal D_gT^{fg}
-\frac{32i}{3}\varepsilon^a{}_{cdef}T^{cd}\mathcal D_g\mathcal D^eT^{fg}\\
&+\frac{32i}{3}\varepsilon^a{}_{cdef}T^c{}_g\mathcal D^d\mathcal D^eT^{fg}
-\frac{32i}{3}\varepsilon^a{}_{cdef}T^c{}_g\mathcal D^d\mathcal D^gT^{ef}\\
&+16i\varepsilon^a{}_{cdef}(\mathcal D^cT^d{}_g)(\mathcal D^eT^{fg})
+\frac{32i}{3}\varepsilon^a{}_{cdef}(\mathcal D^cT^d{}_g)(\mathcal D^gT^{ef})\\
&+\frac{i}{24}\varepsilon^a{}_{cdef}\widehat R(V)^{cd\,rs}\widehat R(V)^{ef}{}_{rs}.
\end{aligned}
\tag{VC05d}
```

**Terms 26–34:**

```math
\begin{aligned}
&-3iT_c{}^d\bar R_e{}^a\gamma^cR^e{}_d
+\frac14\bar R_{cd}\mathcal D^aR^{cd}
+\frac14\bar R_{cd}\mathcal D^cR^{da}\\
&-\frac12\bar R_c{}^a\mathcal D_dR^{cd}
-\frac14\bar R_{de}\gamma^{ca}\mathcal D_cR^{de}
-16iT^c{}_d\bar R^a{}_c\gamma^d\chi\\
&-4\bar R_c{}^a\mathcal D^c\chi
+4\bar\chi\mathcal D_cR^{ca}
+\frac{64}{3}\bar\chi\gamma^{ca}\mathcal D_c\chi.
\end{aligned}
\tag{VC05e}
```

$`t^a`$ is the sum of VC05a–VC05e, with every SU(2) bilinear contraction
understood exactly as in M11c. In particular terms 19 and 20 are not
cancelled by treating covariant derivatives as commuting.

## 47. Detailed Derivation

### 47.1. Curvature derivatives and the scalar auxiliary field

<!-- ASSERT_CONVENTION: metric_signature=(-,+,+,+,+), source_lock=UNG-WEYL2-OP58-CONVENTIONS-v5 -->

First apply pair exchange, the algebraic cyclic identity and the
antisymmetry of $`T`$. They give the following contractions, with a common
free index $`a`$:

```math
\begin{aligned}
C_{cd}{}^a{}_e\mathcal D^cT^{de}
&=-\frac12 C^a{}_{bcd}\mathcal D^bT^{cd},\\
C_{cd}{}^a{}_e\mathcal D^eT^{cd}
&=C^a{}_{bcd}\mathcal D^bT^{cd},\\
(\mathcal D_cC^c{}_d{}^a{}_e)T^{de}
&=-\frac12(\mathcal D_bC^{ab}{}_{cd})T^{cd},\\
(\mathcal D_cC_{de}{}^{ca})T^{de}
&=-(\mathcal D_bC^{ab}{}_{cd})T^{cd}.
\end{aligned}
\tag{VC06}
```

For example, after pair exchange the first line contains
$`C^a{}_{ecd}\mathcal D^cT^{de}`$. Antisymmetrizing $`d,e`$ and inserting
$`C^a{}_{ecd}+C^a{}_{cde}+C^a{}_{dec}=0`$ gives

```math
\begin{aligned}
C^a{}_{ecd}\mathcal D^cT^{de}
&=\frac12(C^a{}_{ecd}-C^a{}_{dce})\mathcal D^cT^{de}\\
&=-\frac12 C^a{}_{cde}\mathcal D^cT^{de}.
\end{aligned}
\tag{VC07}
```

For the third line of VC06 the corresponding explicit contraction is

```math
\begin{aligned}
(\mathcal D_cC^c{}_d{}^a{}_e)T^{de}
&=\frac12\mathcal D_c\left(C^a{}_e{}^c{}_d-C^a{}_d{}^c{}_e\right)T^{de}\\
&=-\frac12(\mathcal D_cC^{ac}{}_{de})T^{de}.
\end{aligned}
```

This differentiates an algebraic identity; it does not assume the
bosonic differential Bianchi identity. The last line simply uses
$`C_{de}{}^{ca}=C^{ca}{}_{de}=-C^{ac}{}_{de}`$.
Consequently the coefficients of terms 7–11 add as

```math
\begin{aligned}
\left(-\frac i3-\frac{4i}{3}-\frac i3\right)
 C^{ab}{}_{cd}\mathcal D_bT^{cd}
&=-2i C^{ab}{}_{cd}\mathcal D_bT^{cd},\\
\left(2i-4i\right)(\mathcal D_bC^{ab}{}_{cd})T^{cd}
&=-2i(\mathcal D_bC^{ab}{}_{cd})T^{cd},\\
\text{terms 7--11}
&=-2i\mathcal D_b(C^{ab}{}_{cd}T^{cd}).
\end{aligned}
\tag{VC08}
```

Terms 12 and 13 give, using $`T^{ca}=-T^{ac}`$,

```math
\begin{aligned}
\frac{32i}{3}D\mathcal D_cT^{ac}
-\frac{32i}{3}(\mathcal D_cD)T^{ca}
&=\frac{32i}{3}\left[D\mathcal D_cT^{ac}
 +(\mathcal D_cD)T^{ac}\right]\\
&=\frac{32i}{3}\mathcal D_c(DT^{ac}).
\end{aligned}
\tag{VC09}
```

These are exact product derivatives. Their weights are respectively
$`1+2+1=4`$ and $`1+2+1=4`$.

### 47.2. All five cubic-$`T`$ derivative terms

The derivative of the quadratic contraction is
$`\mathcal D_b(T_{cd}T^{cd})=2T_{cd}\mathcal D_bT^{cd}`$.
Thus terms 15 and 17 are exactly

```math
\begin{aligned}
&\frac{128i}{9}T^{ab}T_{cd}\mathcal D_bT^{cd}
+\frac{64i}{9}(T_{cd}T^{cd})\mathcal D_bT^{ab}\\
&\hspace{12mm}=\frac{64i}{9}\mathcal D_b
 (T^{ab}T_{cd}T^{cd}).
\end{aligned}
\tag{VC10}
```

For the other three terms, expand the product before matching:

```math
\begin{aligned}
\mathcal D_b(T^a{}_cT^{cd}T^b{}_d)
={}&(\mathcal D_bT^a{}_c)T^{cd}T^b{}_d
 +T^a{}_c(\mathcal D_bT^{cd})T^b{}_d
 +T^a{}_cT^{cd}\mathcal D_bT^b{}_d\\
={}&T_{cd}T^c{}_e\mathcal D^dT^{ae}
 +T^a{}_cT_{de}\mathcal D^dT^{ce}
 -T^a{}_cT^c{}_d\mathcal D_eT^{de}.
\end{aligned}
\tag{VC11}
```

In the first product use $`(b,c,d)\mapsto(d,e,c)`$ and the two
antisymmetries $`T^{ec}=-T^{ce}`$, $`T^d{}_c=-T_c{}^d`$.
In the second use $`(b,d)\mapsto(d,e)`$. In the third use
$`\mathcal D_bT^b{}_d=-\mathcal D_bT_d{}^b`$.
Multiplication by $`256i/3`$ reproduces terms 18, 16 and 14, including their
signs. Together, terms 14–18 are

```math
\mathcal D_b\left[
\frac{64i}{9}T^{ab}T_{cd}T^{cd}
+\frac{256i}{3}T^a{}_cT^{cd}T^b{}_d\right].
\tag{VC12}
```

Both products inside the derivative have weight three, so their
derivatives have weight four.

### 47.3. The six epsilon–derivative terms: retain the commutators

To expose the product derivatives, first expand the following ordinary
physical expression:

```math
\begin{aligned}
&16i\varepsilon^a{}_{cdef}\mathcal D^c
 \left[\frac23T^d{}_g\mathcal D^gT^{ef}
                  +T^d{}_g\mathcal D^eT^{fg}\right]\\
={}&\frac{32i}{3}\varepsilon^a{}_{cdef}
 (\mathcal D^cT^d{}_g)(\mathcal D^gT^{ef})
 +\frac{32i}{3}\varepsilon^a{}_{cdef}
 T^d{}_g\mathcal D^c\mathcal D^gT^{ef}\\
&+16i\varepsilon^a{}_{cdef}
 (\mathcal D^cT^d{}_g)(\mathcal D^eT^{fg})
 +16i\varepsilon^a{}_{cdef}
 T^d{}_g\mathcal D^c\mathcal D^eT^{fg}.
\end{aligned}
\tag{VC13}
```

The first and third summands are terms 24 and 23. For term 22,
interchange $`c,d`$ in the epsilon tensor:

```math
-\frac{32i}{3}\varepsilon^a{}_{cdef}
 T^c{}_g\mathcal D^d\mathcal D^gT^{ef}
=+\frac{32i}{3}\varepsilon^a{}_{cdef}
 T^d{}_g\mathcal D^c\mathcal D^gT^{ef}.
\tag{VC14}
```

This is the second summand of VC13. The same interchange in term 21
produces $`-32i/3`$ times the last tensor product in VC13, whose desired
coefficient is $`16i`$. Their difference is

```math
\begin{aligned}
\left(-\frac{32i}{3}-16i\right)
 \varepsilon^a{}_{cdef}T^d{}_g\mathcal D^c\mathcal D^eT^{fg}
&=-\frac{80i}{3}\varepsilon^a{}_{cdef}
 T^d{}_g\mathcal D^{[c}\mathcal D^{e]}T^{fg}\\
&=-\frac{40i}{3}\varepsilon^a{}_{cdef}
 T^d{}_g[\mathcal D^c,\mathcal D^e]T^{fg}.
\end{aligned}
\tag{VC15}
```

Here epsilon is antisymmetric under $`c\leftrightarrow e`$ and
$`T^d{}_g`$ has neither of those indices. Terms 19 and 20 give the other
commutator directly. Hence the **exact** sum of terms 19–24 is

```math
\begin{aligned}
&16i\varepsilon^a{}_{cdef}\mathcal D^c
 \left[\frac23T^d{}_g\mathcal D^gT^{ef}
                  +T^d{}_g\mathcal D^eT^{fg}\right]\\
&+\frac{32i}{3}\varepsilon^a{}_{cdef}T^{cd}
 [\mathcal D^e,\mathcal D_g]T^{fg}
-\frac{40i}{3}\varepsilon^a{}_{cdef}T^d{}_g
 [\mathcal D^c,\mathcal D^e]T^{fg}.
\end{aligned}
\tag{VC16}
```

Substitute **all four terms** of VC04. The curvature contribution is

```math
\begin{aligned}
&\frac{32i}{3}\varepsilon^a{}_{cdef}T^{cd}
 \left(C^e{}_g{}^f{}_hT^{hg}+C^e{}_g{}^g{}_hT^{fh}\right)\\
&-\frac{40i}{3}\varepsilon^a{}_{cdef}T^d{}_g
 \left(C^{ce f}{}_hT^{hg}+C^{ce g}{}_hT^{fh}\right).
\end{aligned}
\tag{VC17}
```

The full fermionic contribution is

```math
\begin{aligned}
&+\frac{16}{3}\varepsilon^a{}_{cdef}T^{cd}
 \bar R^e{}_g\gamma^{fg}\chi
-\frac{20}{3}\varepsilon^a{}_{cdef}T^d{}_g
 \bar R^{ce}\gamma^{fg}\chi\\
&-\varepsilon^a{}_{cdef}T^{cd}\bar R^e{}_gR^{fg}
+\frac54\varepsilon^a{}_{cdef}T^d{}_g\bar R^{ce}R^{fg}.
\end{aligned}
\tag{VC18}
```

The four numerical multiplications are
$`(32i/3)(-i/2)=16/3`$,
$`(-40i/3)(-i/2)=-20/3`$,
$`(32i/3)(3i/32)=-1`$ and
$`(-40i/3)(3i/32)=5/4`$.
Thus commuting the derivatives changes the explicit fermion terms;
retaining just VC17 would give a wrong answer.

### 47.4. The curvature–epsilon–$`T^2`$ cancellation, including Schouten

First,
$`C_{cdef}\varepsilon^{cefa}{}_gT^d{}_hT^{gh}=0`$:
epsilon antisymmetrizes $`c,e,f`$, and pair exchange turns the contraction
into the cyclic identity $`C_{d[cef]}=0`$. This removes term 4 alone.

The other contractions will be reduced to the *written* tensor
$`\varepsilon^{aefgh}C_{cdef}T^{cd}T_{gh}`$; we do not give it a new field
name. The six-index Schouten identity in five dimensions is

```math
\begin{aligned}
0={}&\delta_x^d\varepsilon^{acegh}
-\delta_x^a\varepsilon^{dcegh}
-\delta_x^c\varepsilon^{adegh}
-\delta_x^e\varepsilon^{acdgh}
-\delta_x^g\varepsilon^{acedh}
-\delta_x^h\varepsilon^{acegd}.
\end{aligned}
\tag{VC19}
```

Contract it with $`C_{cdef}T^{xf}T_{gh}`$. In its second, fifth and sixth
summands epsilon antisymmetrizes the three curvature indices $`c,d,e`$,
so the cyclic identity sets those summands to zero. Interchanging $`c,d`$
in the third summand changes the curvature sign, and pair exchange in
the fourth puts the other pair against $`T`$. The six contributions are
therefore, in order,

```math
\begin{aligned}
0={}&\varepsilon^{acegh}C_{cdef}T^{df}T_{gh}
+0+\varepsilon^{acegh}C_{cdef}T^{df}T_{gh}\\
&-\varepsilon^{aefgh}C_{cdef}T^{cd}T_{gh}+0+0.
\end{aligned}
\tag{VC20}
```

This proves the factor $`1/2`$ for term 2. Next use
$`C_{cdef}+C_{decf}+C_{ecdf}=0`$ and contract with
$`\varepsilon^{acegh}T^d{}_gT^f{}_h`$. Its three terms, after dummy
relabeling and $`T_{ab}=-T_{ba}`$, are

```math
0=2\varepsilon^{acegh}C_{cdef}T^d{}_gT^f{}_h
 -\varepsilon^{aefgh}C_{cdef}T^c{}_gT^d{}_h.
\tag{VC21}
```

The two relabelings in VC21 can be followed without combining terms:
in its second curvature contraction use $`(d,f)\leftrightarrow(f,d)`$ and
$`g\leftrightarrow h`$, obtaining

```math
\varepsilon^{acegh}C_{decf}T^d{}_gT^f{}_h
=\varepsilon^{acehg}C_{fecd}T^f{}_hT^d{}_g
=\varepsilon^{acegh}C_{cdef}T^d{}_gT^f{}_h.
```

Here $`C_{fecd}=C_{cdfe}=-C_{cdef}`$ and epsilon supplies the other minus.
In the third use $`(c,d,e,f)\mapsto(e,c,f,d)`$:

```math
\varepsilon^{acegh}C_{ecdf}T^d{}_gT^f{}_h
=\varepsilon^{aefgh}C_{fecd}T^c{}_gT^d{}_h
=-\varepsilon^{aefgh}C_{cdef}T^c{}_gT^d{}_h.
```

To finish this reduction one also needs **trace-freeness**, not merely
cyclicity. Display the weighted four-index antisymmetrization explicitly:

```math
T_{[cd}T_{gh]}
=\frac13(T_{cd}T_{gh}-T_{cg}T_{dh}+T_{ch}T_{dg})
=-\frac1{24}\varepsilon_{cdghk}
 \varepsilon^{klmnp}T_{lm}T_{np}.
\tag{VC22}
```

The coefficient $`-1/24`$ follows by contracting the two volume tensors
in Lorentzian five dimensions. In the epsilon contraction, the last
product in the parentheses equals minus the middle product after
$`g\leftrightarrow h`$. Thus

```math
\begin{aligned}
&\varepsilon^{aefgh}C^{cd}{}_{ef}
 (T_{cd}T_{gh}-2T_{cg}T_{dh})\\
&=3\varepsilon^{aefgh}C^{cd}{}_{ef}T_{[cd}T_{gh]}\\
&=-\frac18\varepsilon^{aefgh}\varepsilon_{cdghk}
 C^{cd}{}_{ef}\varepsilon^{klmnp}T_{lm}T_{np}\\
&=\frac14\delta^{aef}_{cdk}C^{cd}{}_{ef}
 \varepsilon^{klmnp}T_{lm}T_{np}\\
&=\left[-C^{ca}{}_{ck}+\frac12\delta^a_k C^{cd}{}_{cd}\right]
 \varepsilon^{klmnp}T_{lm}T_{np}=0.
\end{aligned}
\tag{VC23}
```

Here $`\delta^{aef}_{cdk}`$ is the determinant of three Kronecker deltas,
not a new operation: the volume contraction is
$`\varepsilon^{aefgh}\varepsilon_{cdghk}=-2\delta^{aef}_{cdk}`$.
To see every trace and sign in its contraction, expand it:

```math
\begin{aligned}
\delta^{aef}_{cdk}C^{cd}{}_{ef}
={}&C^{ad}{}_{dk}-C^{ad}{}_{kd}
-C^{ca}{}_{ck}+C^{ca}{}_{kc}
+\delta^a_k(C^{cd}{}_{cd}-C^{cd}{}_{dc})\\
={}&-4C^{ca}{}_{ck}+2\delta^a_k C^{cd}{}_{cd}=0.
\end{aligned}
\tag{VC24}
```

Combining VC20–VC24 gives all five required reductions:

```math
\begin{aligned}
C_{cdef}\varepsilon^{cea}{}_{gh}T^{df}T^{gh}
 &=\frac12\varepsilon^{aefgh}C_{cdef}T^{cd}T_{gh},\\
C_{cdef}\varepsilon^{cea}{}_{gh}T^{dg}T^{fh}
 &=\frac14\varepsilon^{aefgh}C_{cdef}T^{cd}T_{gh},\\
C_{cdef}\varepsilon^{cefa}{}_gT^d{}_hT^{gh}&=0,\\
C_{cdef}\varepsilon^{efa}{}_{gh}T^{cd}T^{gh}
 &=\varepsilon^{aefgh}C_{cdef}T^{cd}T_{gh},\\
C_{cdef}\varepsilon^{efa}{}_{gh}T^{cg}T^{dh}
 &=\frac12\varepsilon^{aefgh}C_{cdef}T^{cd}T_{gh}.
\end{aligned}
\tag{VC25}
```

For VC17, its second contraction contains $`C^e{}_g{}^g{}_h=0`$.
Its third contains $`\varepsilon^a{}_{cdef}C^{cef}{}_h=0`$ by cyclicity.
The two remaining contractions, by dummy relabeling and one $`T`$
antisymmetry, are minus the first and last contractions of VC25:

```math
\begin{aligned}
\varepsilon^a{}_{cdef}T^{cd}C^e{}_g{}^f{}_hT^{hg}
&=-\frac12\varepsilon^{aefgh}C_{cdef}T^{cd}T_{gh},\\
\varepsilon^a{}_{cdef}T^d{}_gC^{ce g}{}_hT^{fh}
&=-\frac12\varepsilon^{aefgh}C_{cdef}T^{cd}T_{gh}.
\end{aligned}
\tag{VC26}
```

For completeness, the dummy relabelings in VC26 can be displayed
before invoking VC25:

```math
\begin{aligned}
\varepsilon^{acdef}T_{cd}C_{egfh}T^{hg}
&=-\varepsilon^{acegh}C_{cdef}T^{df}T_{gh},\\
\varepsilon^{acdef}C_{cegh}T_d{}^gT_f{}^h
&=-\varepsilon^{acedf}C_{ghce}T^g{}_dT^h{}_f\\
&=-\varepsilon^{aefgh}C_{cdef}T^c{}_gT^d{}_h.
\end{aligned}
```

In the first line use $`T^{hg}=-T^{gh}`$ and the renaming
$`(c,d,e,f,g,h)\mapsto(g,h,c,e,d,f)`$; moving the two epsilon pairs
past each other has even parity. In the second chain first interchange
$`d,e`$ in epsilon, use pair exchange of $`C`$, and reverse both $`T`$ pairs;
then rename $`(c,e,d,f,g,h)\mapsto(e,f,g,h,c,d)`$.

We can now add **every coefficient** of this tensor:

```math
\begin{aligned}
\text{terms 2--6}:&\quad
4i\left(\frac12\right)+8i\left(\frac14\right)-4i(0)
-\frac{22i}{3}+4i\left(\frac12\right)=-\frac{4i}{3},\\
\text{VC17}:&\quad
\frac{32i}{3}\left(-\frac12\right)
-\frac{40i}{3}\left(0-\frac12\right)=+\frac{4i}{3},\\
\text{total}:&\quad -\frac{4i}{3}+\frac{4i}{3}=0.
\end{aligned}
\tag{VC27}
```

This cancels all undifferentiated $`\varepsilon CTT`$ structures. Their
weight is $`2+1+1=4`$. It does **not** cancel VC18 or the product derivative
in VC16.

### 47.5. Explicit gamma and duality reduction of the $`TRR`$ terms

<!-- ASSERT_CONVENTION: metric_signature=(-,+,+,+,+), source_lock=UNG-WEYL2-OP58-CONVENTIONS-v5 -->

We first evaluate the third summand of VC18. The already proved M12d
identity, with its contracted odd-spinor sign, says

```math
\bar R_{eg}R_f{}^g=\frac14\bar R_{gh}\gamma_{ef}R^{gh}.
\tag{VC28a}
```

Use it and then the rank-three duality in VC02:

```math
\begin{aligned}
\varepsilon^a{}_{cdef}T^{cd}\bar R^e{}_gR^{fg}
&=\frac14\varepsilon^{acdef}T_{cd}\bar R_{gh}\gamma_{ef}R^{gh}\\
&=\frac i2 T_{cd}\bar R_{ef}\gamma^{acd}R^{ef}\\
&=\frac i2 T_{cd}\bar R_{ef}\gamma^a\gamma^{cd}R^{ef}.
\end{aligned}
\tag{VC28b}
```

For the last equality,
$`\gamma^{acd}=\gamma^a\gamma^{cd}-\eta^{ac}\gamma^d+\eta^{ad}\gamma^c`$.
Each extra contraction contains $`\bar R_{ef}\gamma^bR^{ef}=0`$:
VC03 changes its sign under interchange of the identical spinors while
the contraction of their curvature indices is symmetric.

Now expand the **six** terms of the spinor two-form identity:

```math
\gamma^{cd}R^{ef}
=\gamma^{ce}R^{df}-\gamma^{cf}R^{de}
-\gamma^{de}R^{cf}+\gamma^{df}R^{ce}
-\gamma^{ef}R^{cd}.
\tag{VC29a}
```

The needed matrix operation in the first product is

```math
\begin{aligned}
\bar R_{ef}\gamma^a\gamma_c{}^e
&=\bar R_{ef}(\gamma^a\gamma_c\gamma^e-\delta_c^e\gamma^a)\\
&=\bar R_{ef}(\gamma^e\gamma^a\gamma_c
 +2\delta_c^e\gamma^a-2\eta^{ae}\gamma_c-\delta_c^e\gamma^a)\\
&=\bar R_{cf}\gamma^a-2\bar R^a{}_f\gamma_c.
\end{aligned}
\tag{VC29b}
```

The term with $`\bar R_{ef}\gamma^e`$ vanishes by the barred gamma trace.
After multiplication by $`T^{cd}R_d{}^f`$, this gives

```math
T^{cd}\bar R_{ef}\gamma^a\gamma_c{}^e R_d{}^f
=T^{cd}\bar R_{ec}\gamma^aR^e{}_d
 -2T_c{}^d\bar R_e{}^a\gamma^cR^e{}_d.
\tag{VC29c}
```

In the first term on the right, both $`\bar R_{cf}`$ and $`R_d{}^f`$ have
been reversed, giving two minus signs. The same two reversals produce
the displayed second contraction.

All four mixed products in VC29a give exactly VC29c. Their signs can
be followed separately:

| Product from VC29a | Relabeling | Net result after the displayed sign |
|---|---|---|
| $`+\gamma^{ce}R^{df}`$ | none | VC29c |
| $`-\gamma^{cf}R^{de}`$ | $`e\leftrightarrow f`$, so $`\bar R_{fe}=-\bar R_{ef}`$ | VC29c |
| $`-\gamma^{de}R^{cf}`$ | $`c\leftrightarrow d`$, so $`T^{dc}=-T^{cd}`$ | VC29c |
| $`+\gamma^{df}R^{ce}`$ | both previous interchanges | VC29c |

The fifth product is zero, including the gamma at its left:

```math
\begin{aligned}
\bar R_{ef}\gamma^a\gamma^{ef}
&=\bar R_{ef}\left(\gamma^{ef}\gamma^a
 +2\eta^{ae}\gamma^f-2\eta^{af}\gamma^e\right)=0.
\end{aligned}
\tag{VC29d}
```

Each of its three terms has a barred gamma trace. Consequently

```math
\begin{aligned}
T_{cd}\bar R_{ef}\gamma^{acd}R^{ef}
&=4T^{cd}\bar R_{ec}\gamma^aR^e{}_d
 -8T_c{}^d\bar R_e{}^a\gamma^cR^e{}_d,\\
\varepsilon^a{}_{cdef}T^{cd}\bar R^e{}_gR^{fg}
&=2iT^{cd}\bar R_{ec}\gamma^aR^e{}_d
 -4iT_c{}^d\bar R_e{}^a\gamma^cR^e{}_d.
\end{aligned}
\tag{VC30}
```

For the last summand of VC18, apply the *barred* duality with its
indices in the actual order that occurs:

```math
\varepsilon^{acdef}\bar R_{ce}
=-2i(\bar R^{df}\gamma^a+\bar R^{fa}\gamma^d+\bar R^{ad}\gamma^f).
\tag{VC31a}
```

The minus sign is the odd permutation that moves the contracted pair
$`c,e`$ to the last epsilon pair before applying VC03. Multiplication by
$`T_{dg}R_f{}^g`$ gives the three contractions

```math
\begin{aligned}
T_{dg}\bar R^{df}\gamma^aR_f{}^g
 &=-T^{cd}\bar R_{ec}\gamma^aR^e{}_d,\\
T_{dg}\bar R^{fa}\gamma^dR_f{}^g
 &=T_c{}^d\bar R_e{}^a\gamma^cR^e{}_d,\\
T_{dg}\bar R^{ad}\gamma^fR_f{}^g&=0.
\end{aligned}
\tag{VC31b}
```

The first line uses $`\bar R^{df}=-\bar R^{fd}`$; the second only renames
contracted indices; the last is $`\gamma^fR_f{}^g=0`$.
Therefore

```math
\varepsilon^a{}_{cdef}T^d{}_g\bar R^{ce}R^{fg}
=2iT^{cd}\bar R_{ec}\gamma^aR^e{}_d
 -2iT_c{}^d\bar R_e{}^a\gamma^cR^e{}_d.
\tag{VC31c}
```

Add the two terms just derived with their actual VC18 coefficients,
$`-1`$ and $`5/4`$, and the original term 26, whose coefficient is $`-3i`$:

```math
\begin{aligned}
T^{cd}\bar R_{ec}\gamma^aR^e{}_d:&\quad
-2i+\frac54(2i)=\frac i2,\\
T_c{}^d\bar R_e{}^a\gamma^cR^e{}_d:&\quad
-3i+4i+\frac54(-2i)=-\frac{3i}{2}.
\end{aligned}
\tag{VC32a}
```

The complete $`TRR`$ result is

```math
\frac i2T^{cd}\bar R_{ec}\gamma^aR^e{}_d
-\frac{3i}{2}T_c{}^d\bar R_e{}^a\gamma^cR^e{}_d.
\tag{VC32b}
```

Only one gamma remains in each bilinear. There is no unevaluated
matrix product or epsilon contraction in this fermion sector.

### 47.6. Explicit gamma reduction of both $`TR\chi`$ commutator terms

For the first term of VC18, first multiply the two-gamma matrix:

```math
\begin{aligned}
\bar R^e{}_g\gamma^{fg}
&=\bar R^e{}_g(\gamma^f\gamma^g-\eta^{fg})\\
&=\bar R^e{}_g(-\gamma^g\gamma^f+2\eta^{fg}-\eta^{fg})
=\bar R^{ef}.
\end{aligned}
\tag{VC33a}
```

Duality on the remaining spinor two-form gives

```math
\begin{aligned}
\varepsilon^a{}_{cdef}T^{cd}\bar R^e{}_g\gamma^{fg}\chi
&=\varepsilon^a{}_{cdef}T^{cd}\bar R^{ef}\chi\\
&=2iT^{cd}(\bar R_{cd}\gamma^a
 +\bar R_d{}^a\gamma_c+\bar R^a{}_c\gamma_d)\chi\\
&=2iT^{cd}\bar R_{cd}\gamma^a\chi
 +4iT^c{}_d\bar R^a{}_c\gamma^d\chi.
\end{aligned}
\tag{VC33b}
```

The second and third bilinears in the middle line are equal after
$`c\leftrightarrow d`$, using one minus from $`T`$ and one from $`R`$.

For the second term of VC18 use VC31a and multiply by
$`T_{dg}\gamma_f{}^g\chi`$. All three matrix products are

```math
\begin{aligned}
T_{dg}\bar R^{df}\gamma^a\gamma_f{}^g\chi
&=T_{dg}\bar R^{df}(\gamma^a\gamma_f\gamma^g
 -\delta_f^g\gamma^a)\chi\\
&=2T_{dg}\bar R^{da}\gamma^g\chi
 -T_{dg}\bar R^{dg}\gamma^a\chi\\
&=-2T^c{}_d\bar R^a{}_c\gamma^d\chi
 -T^{cd}\bar R_{cd}\gamma^a\chi,\\[2mm]
T_{dg}\bar R^{fa}\gamma^d\gamma_f{}^g\chi
&=2T_{dg}\bar R^{da}\gamma^g\chi
 -T_{dg}\bar R^{ga}\gamma^d\chi\\
&=-3T^c{}_d\bar R^a{}_c\gamma^d\chi,\\[2mm]
T_{dg}\bar R^{ad}\gamma^f\gamma_f{}^g\chi
&=4T_{dg}\bar R^{ad}\gamma^g\chi
=4T^c{}_d\bar R^a{}_c\gamma^d\chi.
\end{aligned}
\tag{VC34a}
```

In the first two lines with three gammas, moving $`\gamma_f`$ left
annihilates the barred gamma trace and leaves its anticommutator $`2\eta`$.
In the last line $`\gamma^f\gamma_f{}^g=4\gamma^g`$ is VC02.
Multiply the sum by $`-2i`$ from VC31a:

```math
\begin{aligned}
\varepsilon^a{}_{cdef}T^d{}_g\bar R^{ce}\gamma^{fg}\chi
&=-2i\left[-T^{cd}\bar R_{cd}\gamma^a\chi
 +(-2-3+4)T^c{}_d\bar R^a{}_c\gamma^d\chi\right]\\
&=2iT^{cd}\bar R_{cd}\gamma^a\chi
 +2iT^c{}_d\bar R^a{}_c\gamma^d\chi.
\end{aligned}
\tag{VC34b}
```

Now include the original term 31. Every coefficient is visible:

```math
\begin{aligned}
T^c{}_d\bar R^a{}_c\gamma^d\chi:&\quad
-16i+\frac{16}{3}(4i)-\frac{20}{3}(2i)=-8i,\\
T^{cd}\bar R_{cd}\gamma^a\chi:&\quad
\frac{16}{3}(2i)-\frac{20}{3}(2i)=-\frac{8i}{3}.
\end{aligned}
\tag{VC35a}
```

Thus the complete $`TR\chi`$ result is

```math
-8iT^c{}_d\bar R^a{}_c\gamma^d\chi
-\frac{8i}{3}T^{cd}\bar R_{cd}\gamma^a\chi.
\tag{VC35b}
```

The reductions in 47.5–47.6 use gamma traces and the spinor two-form
duality. They keep the existing spinor pairings, so no further Fierz
re-pairing or discarded Clifford channel is needed. The SU(2) singlet
Fierz extraction itself remains the complete calculation of Part IV.

### 47.7. The four $`R\mathcal DR`$ terms and their two-gamma product

The derivative of $`\gamma_{[ab}R_{cd]}=0`$ has the same six-term
expansion because $`\mathcal D\gamma=0`$. Contract it with $`\bar R^{cd}`$:

```math
\begin{aligned}
0={}&\bar R^{cd}\gamma_{ab}\mathcal D_mR_{cd}
-\bar R^{cd}\gamma_{ac}\mathcal D_mR_{bd}
+\bar R^{cd}\gamma_{ad}\mathcal D_mR_{bc}\\
&+\bar R^{cd}\gamma_{bc}\mathcal D_mR_{ad}
-\bar R^{cd}\gamma_{bd}\mathcal D_mR_{ac}
+\bar R^{cd}\gamma_{cd}\mathcal D_mR_{ab}.
\end{aligned}
\tag{VC36a}
```

The actual matrix contractions are

```math
\begin{aligned}
\bar R^{cd}\gamma_{ac}
&=\bar R^{cd}(\gamma_a\gamma_c-\eta_{ac})
=2\bar R_a{}^d-\bar R_a{}^d=\bar R_a{}^d,\\
\bar R^{cd}\gamma_{ad}&=-\bar R_a{}^c,\\
\bar R^{cd}\gamma_{bc}&=\bar R_b{}^d,\qquad
\bar R^{cd}\gamma_{bd}=-\bar R_b{}^c,\\
\bar R^{cd}\gamma_{cd}&=0.
\end{aligned}
\tag{VC36b}
```

The second and fourth equalities follow by $`c\leftrightarrow d`$ in
the first and third; the resulting minus is that of $`R^{dc}`$.
Insert these five equalities into VC36a, combine the two equal $`a`$
contractions and the two equal $`b`$ contractions, and then raise $`a,b`$:

```math
\bar R_{de}\gamma^{ab}\mathcal D_mR^{de}
=2\bar R_d{}^a\mathcal D_mR^{db}
 -2\bar R_d{}^b\mathcal D_mR^{da}.
\tag{VC36c}
```

Set $`a=c`$, $`b=a`$, $`m=c`$ with the derivative index contracted. The
original term 30 is therefore

```math
\begin{aligned}
-\frac14\bar R_{de}\gamma^{ca}\mathcal D_cR^{de}
&=-\frac12\bar R_d{}^c\mathcal D_cR^{da}
 +\frac12\bar R_d{}^a\mathcal D_cR^{dc}\\
&=+\frac12\bar R_{cd}\mathcal D^cR^{da}
 +\frac12\bar R_c{}^a\mathcal D_dR^{cd}.
\end{aligned}
\tag{VC37a}
```

In the first summand $`\bar R_d{}^c=-\bar R^c{}_d`$; in the second
rename $`c,d`$. The last term cancels term 29 exactly. The first adds to
term 28 with $`1/4+1/2=3/4`$. Term 27 remains unchanged:

```math
\text{terms 27--30}
=\frac14\bar R_{cd}\mathcal D^aR^{cd}
 +\frac34\bar R_{cd}\mathcal D^cR^{da}.
\tag{VC37b}
```

No derivative has been commuted, and no differential Bianchi identity
or field equation has been inserted into this reduction.

### 47.8. The final three differentiated fermion terms

Use the scalar odd-spinor flip *with the differentiated curvature*
when expanding the first product:

```math
\begin{aligned}
4\mathcal D_b(\bar R^{ab}\chi)
&=4(\mathcal D_b\bar R^{ab})\chi+4\bar R^{ab}\mathcal D_b\chi\\
&=-4\bar\chi\mathcal D_bR^{ab}+4\bar R^{ab}\mathcal D_b\chi\\
&=4\bar\chi\mathcal D_bR^{ba}-4\bar R_b{}^a\mathcal D^b\chi.
\end{aligned}
\tag{VC38a}
```

These are terms 33 and 32. For term 34 the bivector flip has a plus:

```math
\begin{aligned}
\mathcal D_b(\bar\chi\gamma^{ab}\chi)
&=(\mathcal D_b\bar\chi)\gamma^{ab}\chi
 +\bar\chi\gamma^{ab}\mathcal D_b\chi\\
&=\bar\chi\gamma^{ab}\mathcal D_b\chi
 +\bar\chi\gamma^{ab}\mathcal D_b\chi
=2\bar\chi\gamma^{ab}\mathcal D_b\chi,\\
\frac{64}{3}\bar\chi\gamma^{ca}\mathcal D_c\chi
&=-\frac{32}{3}\mathcal D_b(\bar\chi\gamma^{ab}\chi).
\end{aligned}
\tag{VC38b}
```

Combining them gives the exact retained derivative

```math
\text{terms 32--34}
=\mathcal D_b\left[4\bar R^{ab}\chi
 -\frac{32}{3}\bar\chi\gamma^{ab}\chi\right].
\tag{VC38c}
```

The two products in brackets are antisymmetric in $`a,b`$, Grassmann
even and of weight three. The exterior gamma $`\gamma_a`$ in the
variation is distinct from the gamma inside the scalar bilinear
$`\bar\chi\gamma^{ab}\chi`$.

### 47.9. Add the complete result

The following accounting exhausts the 34 starting terms:

| Starting terms | Calculated destination |
|---|---|
| 1 | unchanged $`\varepsilon CC`$ term |
| 2–6 | VC25–VC27: cancel the Lorentz-curvature part of VC16 |
| 7–11 | $`-2i\mathcal D_b(C^{ab}{}_{cd}T^{cd})`$, VC08 |
| 12–13 | $`32i\mathcal D_b(DT^{ab})/3`$, VC09 |
| 14–18 | both cubic product derivatives, VC12 |
| 19–24 | VC16 product derivative; its curvature terms cancel 2–6 and its fermions add in VC32/VC35 |
| 25 | unchanged $`\varepsilon\widehat R(V)\widehat R(V)`$ term |
| 26 | included in the two $`TRR`$ coefficients VC32 |
| 27–30 | two $`R\mathcal DR`$ terms VC37 |
| 31 | included in the two $`TR\chi`$ coefficients VC35 |
| 32–34 | two fermionic product derivatives VC38 |

There are **24 summands when the retained product derivatives are
expanded** (15 with no explicit spinor factor and 9 explicit fermion
bilinears). This count refers to the displayed product-rule basis; it
does not assert independence modulo every other covariant identity.
The compact result is written in original fields in Section 49.

## 48. Consistency Checks

### 48.1. Indices, weights and Grassmann parity

Every line of the final $`t^a`$ has the single free Lorentz index $`a`$.
The external product $`\gamma_a t^a\epsilon^i`$ has only the free SU(2)
index $`i`$. Each internal bilinear is an SU(2) singlet. The coefficient
is Grassmann even and the complete variation is odd.

The weight check for each type of term is explicit:

```math
\begin{array}{c|c}
\text{contraction type}&w\\ \hline
CC,\ \widehat R(V)\widehat R(V)&2+2=4\\
\mathcal D(CT),\ \mathcal D(DT)&1+2+1=4\\
\mathcal D(TTT)&1+1+1+1=4\\
\mathcal D(T\mathcal DT)&1+1+1+1=4\\
TRR,\ TR\chi&1+\frac32+\frac32=4\\
R\mathcal DR,\ \mathcal D(R\chi),\ \mathcal D(\chi\chi)
 &\frac32+1+\frac32=4.
\end{array}
\tag{VC39}
```

Multiplication by $`\epsilon`$ of weight $`-1/2`$ gives $`7/2`$, the weight of
$`\varphi_W`$. Full covariant derivatives and invariant contractions
preserve Lorentz and SU(2) covariance. No boundary condition is needed
because no derivative is discarded.

### 48.2. Reality

With C03's contracted symplectic-Majorana convention, scalar and
two-gamma odd-spinor bilinears are imaginary, while one-gamma bilinears
are real. The same statements apply with a full derivative on one
spinor. Thus the relevant conjugation checks are

```math
\begin{aligned}
(\bar u v)^*&=-\bar u v,&
(\bar u\gamma_a v)^*&=+\bar u\gamma_a v,&
(\bar u\gamma_{ab}v)^*&=-\bar u\gamma_{ab}v,\\
(t^a)^*&=-t^a,& (2it^a)^*&=2it^a.
\end{aligned}
\tag{VC40}
```

In the final answer the bosonic tensor structures and one-gamma
bilinears carry an explicit $`i`$; the scalar and two-gamma bilinears
carry real coefficients. This is exactly the reality pattern required
by L01's $`-i\gamma^aE_a\epsilon^i/2`$. The checker verifies the
rank-zero, rank-one and rank-two conjugation matrices in the locked
four-component gamma representation. The random algebra samples test
polynomial identities with two independent odd generators; they do not
assume that commuting numerical spinors have fermionic flip signs.

### 48.3. Comparison with all printed bosonic vector terms

Set the independent physical fermions and their derivatives to zero
only for this comparison. L01 assigns

```math
-\frac i2E_W^a=t^a,\qquad E_W^a=2it^a.
\tag{VC41a}
```

Multiply the bosonic coefficients we derived by $`2i`$:

| Structure, with the same derivative placement as M03 | Coefficient in $`t^a`$ | Coefficient in $`2it^a`$ | Printed M03 |
|---|---:|---:|---:|
| $`\varepsilon CC`$ | $`-i/32`$ | $`1/16`$ | $`1/16`$ |
| $`\varepsilon\widehat R(V)\widehat R(V)`$ | $`i/24`$ | $`-1/12`$ | $`-1/12`$ |
| $`\mathcal D(CT)`$ | $`-2i`$ | $`4`$ | $`4`$ |
| $`\mathcal D(DT)`$ | $`32i/3`$ | $`-64/3`$ | $`-64/3`$ |
| $`\mathcal D(TT^2)`$ | $`64i/9`$ | $`-128/9`$ | $`-128/9`$ |
| $`\mathcal D(T_{ac}T^{cd}T_{bd})`$ | $`256i/3`$ | $`-512/3`$ | $`-512/3`$ |
| $`\varepsilon_{abcde}\mathcal D^b(T^{cf}\mathcal D_fT^{de})`$ | $`32i/3`$ | $`-64/3`$ | $`-64/3`$ |
| $`\varepsilon_{abcde}\mathcal D^b(T^c{}_f\mathcal D^dT^{ef})`$ | $`16i`$ | $`-32`$ | $`-32`$ |

The first six entries have their free index lowered to compare with M03;
this changes no coefficient. The two last entries already display that
placement. There is no bosonic remainder, no integration by parts and
no unrecorded derivative interchange in this comparison.

Two simple restrictions also follow explicitly:

```math
\begin{aligned}
T=\mathcal DT=\mathcal D\mathcal DT=R=\chi=\mathcal DR=\mathcal D\chi=0:
\quad t^a={}&-\frac i{32}\varepsilon^{abcde}C_{bcfg}C_{de}{}^{fg}
+\frac i{24}\varepsilon^{abcde}\widehat R(V)_{bc}{}^{ij}
 \widehat R(V)_{de\,ij},\\
C=\widehat R(V)=R=\chi=0,\quad
\mathcal DT=\mathcal D\mathcal DT=\mathcal DD=0:
\quad t^a={}&0.
\end{aligned}
\tag{VC41b}
```

These are algebraic restrictions, not asserted supergravity backgrounds.

### 48.4. Independent matrix and component verification

The reproducible checker is
[verify_weyl_vector_canonicalization.py](../src/reference_checks/verify_weyl_vector_canonicalization.py); its complete report is
`VECTOR-CANONICALIZATION-CHECKS.json`, generated in the temporary workspace
of the [component-check runner](../checks/reference_suite.py). It checks:

- The full 34-term starting expression against the final expression with
  all product derivatives expanded into 24 summands, on six independent
  component/Grassmann samples. The second-derivative jets obey the **full
  fermionic** VC04 commutator and retain arbitrary symmetric derivatives.
  Maximum normalized residual: $`1.51\times10^{-16}`$.
- Each of the five spinor identities and eight curvature contractions
  separately, as well as each differentiated sector. This prevents a
  cancellation of unrelated errors in the final sum.
- Seven exact rational coefficient additions; 125 one-gamma/two-gamma
  products, five contracted products and 125 rank-three dualities.
- All $`5^6=15625`$ epsilon-epsilon contractions used in VC23; zero error.
- For two samples, the vector projection of all **272** potentially
  vector ordered-matrix contributions in the Part V ledger, before their
  gamma products are reduced. These agree with the final vector with
  maximum total normalized residual $`8.51\times10^{-16}`$; the largest
  individual normalized reduction residual is $`4.00\times10^{-13}`$.
- Paired indices and weight four for every expanded final monomial;
  the rank-zero through rank-two reality matrices and the two restrictions
  in VC41b.

The projector in this independent matrix check is the usual Clifford
trace: if the epsilon-right matrix is $`p\mathbf1+\gamma_b t^b+\gamma_{bc}k^{bc}`$,
its contraction with $`\gamma^a`$ and division of the trace by four gives $`t^a`$; it is used only in the verification code. The
hand derivation above, rather than this numerical check, supplies the
analytic proof. These tests do not certify the independent descendant
laws or the entire nonlinear supersymmetry algebra.

## 49. Final Result

Restoring the full supercovariant curvature names, the requested
coefficient is

```math
\boxed{
\begin{aligned}
t^a={}&-\frac i{32}\varepsilon^{abcde}
 \widehat C_{bcfg}\widehat C_{de}{}^{fg}
+\frac i{24}\varepsilon^{abcde}
 \widehat R(V)_{bc}{}^{ij}\widehat R(V)_{de\,ij}\\
&+\mathcal D_b\Big[
 -2i\widehat C^{ab}{}_{cd}T^{cd}
 +\frac{32i}{3}DT^{ab}
 +\frac{64i}{9}T^{ab}T_{cd}T^{cd}
 +\frac{256i}{3}T^a{}_cT^{cd}T^b{}_d\\
&\hspace{24mm}
 +4\overline{\widehat R(Q)^{ab}}\chi
 -\frac{32}{3}\bar\chi\gamma^{ab}\chi\Big]\\
&+16i\varepsilon^a{}_{bcde}\mathcal D^b\Big[
 \frac23T^{cf}\mathcal D_fT^{de}
 +T^c{}_f\mathcal D^dT^{ef}\Big]\\
&+\frac i2T^{cd}\overline{\widehat R(Q)_{ec}}
 \gamma^a\widehat R(Q)^e{}_d
-\frac{3i}{2}T_c{}^d\overline{\widehat R(Q)_e{}^a}
 \gamma^c\widehat R(Q)^e{}_d\\
&-8iT^c{}_d\overline{\widehat R(Q)^a{}_c}\gamma^d\chi
-\frac{8i}{3}T^{cd}\overline{\widehat R(Q)_{cd}}\gamma^a\chi\\
&+\frac14\overline{\widehat R(Q)_{cd}}\mathcal D^a\widehat R(Q)^{cd}
+\frac34\overline{\widehat R(Q)_{cd}}\mathcal D^c\widehat R(Q)^{da}.
\end{aligned}}
\tag{VC42}
```

Accordingly, the fully simplified contribution asked for is

```math
\boxed{\left.\delta_Q\varphi_W^i\right|_{\text{vector singlet}}
=\gamma_a t^a\epsilon^i,\qquad t^a\text{ given by VC42}.}
\tag{VC43}
```

There are no remaining gamma-matrix products inside any bilinear, no
unevaluated commutator, and no “fermions” placeholder. The covariant
product derivatives in VC42 are exactly those explicitly expanded in
VC08–VC16 and VC38. Every hidden physical fermion inside the hatted
curvatures and the full derivatives remains included.

Together with SC32 and the proved $`k^{ab}=0`$, this completes the
canonical **singlet** coefficients of the computed variation:

```math
\boxed{\left.\delta_Q\varphi_W^i\right|_{\rm singlet}
=(p+\gamma_a t^a)\epsilon^i,
\quad p=\text{SC32},\quad t^a=\text{VC42}.}
\tag{VC44}
```

## 50. Convention Dependence and Remaining Uncertainties

This is an exact canonicalization of M11c relative to the unchanged
v5/M08 inputs and the established M12 conventional identities. It is
not a weak-field or quadratic-fermion approximation. No normalization,
orientation, source coefficient, gauge or formulation has changed.

L01 now assigns both extracted singlet slots, $`N_W=2p`$ and $`E_W^a=2it^a`$.
Their bosonic restrictions agree with M04 and M03 respectively. Calling
these **slot candidates** distinguishes this completed calculation from
the separate checks of $`\delta N_W`$, $`\delta E_W`$, the full
supercovariant divergence constraint, the traceless SU(2) variation and
the spinor S-law. Those transformation and divergence checks are outside this Clifford
decomposition. The [invariant density](full-fermionic-weyl2-action.md) and
[AdS5 spectrum](../../../weyl2/ads5/README.md) have their own calculations.
