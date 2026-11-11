# Canonical scalar coefficient multiplying epsilon^i

## 37. Problem and Target

Calculate and simplify the **complete local coefficient** $`p`$ in
$`\delta_Q\varphi_W^i|_{\rm singlet}=(p+\gamma_at^a)\epsilon^i`$.
Starting point: master M11b, notebook G707. The singlet bivector was
separately proved zero in Part VI/master M12. This calculation changes
neither the adopted spinor M08 nor any source coefficient.

The original variations and the gamma multiplication giving G707 are
already displayed in Parts III–V. We begin with all 22 terms of G707 below,
then show every additional canonicalization. The final expression uses
original fields and the same full supercovariant objects.

**Provenance.** The starting scalar is a derived result, not a printed
fermionic completion. Its inputs are master W/G/R and M08. Clifford and
Majorana rules are C01–C05 [OP Appendix A; W Appendix A]. The conventional
curvature constraints are G03 [W(3.9)–(3.12), footnote5]. The full $`T`$
commutator and the spinor-curvature identity are proved in M12/Part VI.
The printed bosonic comparison is M04 [OP(5.8)]; the quartic definitions
are M05 [OP(5.9)]. The comparison is made only after obtaining $`p`$.

**Assumptions and permitted operations.**

1. Five-dimensional Lorentzian, physical $`g=0`$, gauge-unfixed, off shell.
2. All fermion orders implicit in hats, connections and full derivatives
   remain. No physical fermion is set to zero in the derivation.
3. Use Clifford algebra, contracted Majorana flips, conventional curvature
   constraints, and the complete covariant commutator. Use no EOM.
4. This is an equality of local transformation coefficients. No integration
   by parts, discarded divergence, background ansatz or boundary condition
   is permitted. Keep the ordered second derivative in the final result.
5. Choose the original M04 derivative order and M05 quartic contraction
   as the final readable basis. No claim of uniqueness among all possible
   tensor bases is required.

## 38. Convention Ledger

<!-- ASSERT_CONVENTION: source_lock=UNG-WEYL2-OP58-CONVENTIONS-v5; natural_units=hbar=c=1; metric_signature=(-,+,+,+,+); epsilon_upper_01234=+1; gamma_upper_01234=+i -->

Lorentz indices are $`a,b,c=0,\ldots,4`$; doublet indices are $`i,j=1,2`$.
Use $`\eta=(-,+,+,+,+)`$, $`\varepsilon^{01234}=+1`$,
$`\varepsilon_{01234}=-1`$ and weighted antisymmetrization.
$`\gamma_{ab}=\gamma_{[a}\gamma_{b]}`$,
$`\{\gamma_a,\gamma_b\}=2\eta_{ab}`$ and
$`\gamma_{abcde}=i\varepsilon_{abcde}\mathbf1`$.
A two-form contraction sums both orders; there is no hidden $`1/2`$.

$`\bar\zeta^{\,i}=(\zeta^i)^T\mathsf C`$, with
$`\mathsf C^T=-\mathsf C`$ and $`(\mathsf C\gamma_a)^T=-\mathsf C\gamma_a`$.
The bar is linear, so $`\overline{i\zeta}=i\bar\zeta`$.
Spinors and supersymmetry parameters are Grassmann odd. Their contracted
bilinears are even; $`T,D,C`$ commute with them. Contracted doublet indices
follow C02's NW–SE rule. In particular

```math
\bar u v=-\bar v u,\qquad
\bar u\gamma_a v=-\bar v\gamma_a u,\qquad
\bar u\gamma_{ab}v=+\bar v\gamma_{ab}u.
```

The Riemann and covariant derivative signs are G02 and G01:
$`[\nabla_\mu,\nabla_\nu]X^\rho=R^\rho{}_{\sigma\mu\nu}X^\sigma`$.
The derivative in this calculation is the full $`\mathcal D`$ of G01,
not the Levi-Civita derivative. Its noncommutativity is explicitly retained.

For the intermediate algebra only, write
$`R_{ab}=\widehat R_{ab}(Q)`$ and $`C_{abcd}=\widehat C_{abcd}`$.
These are short names for the two original curvatures. No new operation,
response field, or auxiliary composite is introduced. The final result
restores the full notation.

**Convention scope.** The result-sensitive conventions are those of the
component reference. Fourier transforms, state normalization, regularization,
renormalization and operator time ordering do not enter this local classical
tensor identity. The coupling convention is unchanged and no action is varied here.

## 39. Definitions and Required Identities

### 39.1 All 22 starting terms

Count the following displayed terms in order from 1 to 22. These numbers
label lines of the starting expression, not new fields.

```math
\begin{aligned}
p={}&\frac{1}{16}\widehat C_{cdef}\,\widehat C^{cdef}\\
&-\frac{52}{3}\widehat C_{cdef}\,T^{cd}\,T^{ef}\\
&+8\widehat C_{cdef}\,T^{ce}\,T^{df}\\
&-\frac{1}{12}\widehat C_{cdef}\,\varepsilon^{cdef}{}_{g}\,(\mathcal D_{h}T^{gh})\\
&+\frac{1}{6}\widehat C_{cdef}\,\varepsilon^{cde}{}_{gh}\,(\mathcal D^{f}T^{gh})\\
&-\frac{1}{3}\widehat C_{cdef}\,\varepsilon^{cde}{}_{gh}\,(\mathcal D^{g}T^{fh})\\
&-\frac{1}{12}\widehat C_{cdef}\,\varepsilon^{cef}{}_{gh}\,(\mathcal D^{d}T^{gh})\\
&-\frac{1}{6}\widehat C_{cdef}\,\varepsilon^{cef}{}_{gh}\,(\mathcal D^{g}T^{dh})\\
&+\frac{512}{9}D\,T_{cd}\,T^{cd}\\
&+\frac{32}{3}D^2\\
&-\frac{1408}{27}T_{cd}\,T^{cd}\,T_{ef}\,T^{ef}\\
&+512T_{cd}\,T^{c}{}_{e}\,T^{d}{}_{f}\,T^{ef}\\
&-\frac{64}{3}\varepsilon_{cdefg}\,T^{cd}\,T^{ef}\,(\mathcal D_{h}T^{gh})\\
&+\frac{64}{3}T_{cd}\,(\mathcal D_{e}\mathcal D^{c}T^{de})\\
&-\frac{32}{3}(\mathcal D_{c}T_{de})\,(\mathcal D^{c}T^{de})\\
&+\frac{32}{3}(\mathcal D_{c}T_{de})\,(\mathcal D^{d}T^{ce})\\
&-\frac{1}{6}\widehat R(V)_{cd}{}^{rs}\,\widehat R(V)^{cd}{}_{rs}\\
&+\frac{113i}{16}\big(\overline{\widehat R(Q)_{ec}}\widehat R(Q)^{e}{}_{d}\big)\,T^{cd}\\
&-\frac{97i}{64}\big(\overline{\widehat R(Q)_{ef}}\gamma^{cd}\widehat R(Q)^{ef}\big)\,T_{cd}\\
&+\frac{3}{8}\big(\overline{\widehat R(Q)_{de}}\gamma^{c}\mathcal D_{c}\widehat R(Q)^{de}\big)\\
&-\frac{112i}{3}\big(\overline{\widehat R(Q)_{cd}}\chi\big)\,T^{cd}\\
&-\frac{128}{3}\big(\bar\chi\gamma^{c}\mathcal D_{c}\chi\big)
\end{aligned}\tag{SC01}
```

### 39.2 The matrix algebra and the scalar projection

<!-- ASSERT_CONVENTION: source_lock=UNG-WEYL2-OP58-CONVENTIONS-v5; Clifford=anticommutator_2eta; gamma_antisymmetrization=unit_weight -->

Insert the antisymmetrized definition and anticommute one gamma at a time:

```math
\begin{aligned}
\gamma_a\gamma_b&=\gamma_{ab}+\eta_{ab},\\
\gamma_{ab}\gamma_c&=\gamma_{abc}+\eta_{bc}\gamma_a-\eta_{ac}\gamma_b,\\
\gamma_{ab}\gamma_{cd}
&=(\gamma_{abc}+\eta_{bc}\gamma_a-\eta_{ac}\gamma_b)\gamma_d
  -\eta_{cd}\gamma_{ab}\\
&=\gamma_{abcd}+\eta_{bc}\gamma_{ad}-\eta_{ac}\gamma_{bd}
 -\eta_{bd}\gamma_{ac}+\eta_{ad}\gamma_{bc}
 +\eta_{ad}\eta_{bc}-\eta_{ac}\eta_{bd}.
\end{aligned}\tag{SC02}
```

The last subtraction in the third line comes from
$`\gamma_{cd}=\gamma_c\gamma_d-\eta_{cd}`$.
For the 4-dimensional spinor representation,

```math
\begin{aligned}
\mathop{\mathrm{tr}}\nolimits\mathbf1&=4,\qquad
\mathop{\mathrm{tr}}\nolimits\gamma_a=\mathop{\mathrm{tr}}\nolimits\gamma_{ab}=0,\\
\frac14\mathop{\mathrm{tr}}\nolimits(\gamma_{ab}\gamma_{cd})
&=\eta_{ad}\eta_{bc}-\eta_{ac}\eta_{bd},\\
\frac14\mathop{\mathrm{tr}}\nolimits\gamma_{abcde}&=i\varepsilon_{abcde}.
\end{aligned}\tag{SC03}
```

The already factored singlet satisfies

```math
\frac14\mathop{\mathrm{tr}}\nolimits_{\rm spin}
 (p\mathbf1+\gamma_at^a+\gamma_{ab}k^{ab})=p.
```

This trace acts on matrices multiplying $`\epsilon^i`$; it does not erase
matrices between physical fermions inside a scalar bilinear.

Therefore a rank-five gamma word can contribute to the scalar; it must
not be discarded as a higher-rank matrix. Part V already included those
terms. An external rank-three gamma is dual to rank two and has zero
scalar trace. When it occurs inside a longer product it is multiplied
before the scalar projection. This is also how the independent check
below evaluates the original ordered matrix contributions.

The remaining nontrivial matrices in SC01 are inside actual spinor
bilinears. They will be reduced using the conventional gamma trace:

```math
\gamma^aR_{ab}=0,\qquad \bar R_{ab}\gamma^a=0,\qquad
\bar R_{ab}\gamma^b=0.
\tag{SC04}
```

The required four-index relation is the expanded source identity
$`\gamma_{[ab}R_{cd]}=0`$:

```math
0=\gamma_{ab}R_{cd}-\gamma_{ac}R_{bd}+\gamma_{ad}R_{bc}
+\gamma_{bc}R_{ad}-\gamma_{bd}R_{ac}+\gamma_{cd}R_{ab}.
\tag{SC05}
```

G03/M12 also supply $`C_{abcd}=C_{cdab}`$, $`C_{[abc]d}=0`$ and vanishing
curvature traces for the constrained full curvature. These are used as
proved conventional identities, without a bosonic truncation.

## 40. Detailed Derivation

### 40.1 Combine the two curvature–T–T contractions

<!-- ASSERT_CONVENTION: source_lock=UNG-WEYL2-OP58-CONVENTIONS-v5; constrained_curvature=G03_R03_M12 -->

Contract $`C_{abcd}+C_{acdb}+C_{adbc}=0`$ with $`T^{ab}T^{cd}`$.
In the second term relabel $`b\leftrightarrow c`$, then use antisymmetry
of the second curvature pair. In the third relabel $`(b,c,d)\mapsto(c,d,b)`$,
then use $`T^{db}=-T^{bd}`$. This gives

```math
\begin{aligned}
0&=C_{abcd}T^{ab}T^{cd}
  +C_{acdb}T^{ab}T^{cd}+C_{adbc}T^{ab}T^{cd}\\
 &=C_{abcd}T^{ab}T^{cd}
  -C_{abcd}T^{ac}T^{bd}-C_{abcd}T^{ac}T^{bd},\\
C_{abcd}T^{ac}T^{bd}&=\tfrac12C_{abcd}T^{ab}T^{cd}.
\end{aligned}\tag{SC06}
```

Starting terms 2 and 3 therefore add to

```math
-\frac{52}{3}C_{abcd}T^{ab}T^{cd}
+8C_{abcd}T^{ac}T^{bd}
=\left(-\frac{52}{3}+4\right)C_{abcd}T^{ab}T^{cd}
=-\frac{40}{3}C_{abcd}T^{ab}T^{cd}.
\tag{SC07}
```

The derivative commutator will supply another curvature contribution;
$`-40/3`$ is not the final coefficient.

### 40.2 Evaluate all five curvature–epsilon terms separately

Every epsilon is fully antisymmetric. Therefore its contraction selects
the indicated cyclic curvature part. None of these five terms requires
an integration by parts or a condition on $`\mathcal DT`$:

```math
-\frac1{12}C_{cdef}\varepsilon^{cdef}{}_g\mathcal D_hT^{gh}
=-\frac1{12}C_{[cde]f}\varepsilon^{cdef}{}_g\mathcal D_hT^{gh}=0.
\tag{SC08a}
```

```math
+\frac16C_{cdef}\varepsilon^{cde}{}_{gh}\mathcal D^fT^{gh}
=+\frac16C_{[cde]f}\varepsilon^{cde}{}_{gh}\mathcal D^fT^{gh}=0.
\tag{SC08b}
```

```math
-\frac13C_{cdef}\varepsilon^{cde}{}_{gh}\mathcal D^gT^{fh}
=-\frac13C_{[cde]f}\varepsilon^{cde}{}_{gh}\mathcal D^gT^{fh}=0.
\tag{SC08c}
```

For the last two use pair exchange $`C_{cdef}=C_{efcd}`$ first:

```math
-\frac1{12}C_{cdef}\varepsilon^{cef}{}_{gh}\mathcal D^dT^{gh}
=-\frac1{12}C_{[efc]d}\varepsilon^{cef}{}_{gh}\mathcal D^dT^{gh}=0.
\tag{SC08d}
```

```math
-\frac16C_{cdef}\varepsilon^{cef}{}_{gh}\mathcal D^gT^{dh}
=-\frac16C_{[efc]d}\varepsilon^{cef}{}_{gh}\mathcal D^gT^{dh}=0.
\tag{SC08e}
```

Thus starting terms 4–8 are individually zero. The different term 13,
$`\varepsilon T T\mathcal DT`$, contains no cyclic curvature and remains.

### 40.3 Put the second derivatives in the chosen order

<!-- ASSERT_CONVENTION: source_lock=UNG-WEYL2-OP58-CONVENTIONS-v5; full_commutator=M12b; integration_by_parts=none -->

Start with term 14, without its numerical coefficient:

```math
\begin{aligned}
T_{cd}\mathcal D_e\mathcal D^cT^{de}
&=T_{cd}\mathcal D^c\mathcal D_eT^{de}
  +T_{cd}[\mathcal D_e,\mathcal D^c]T^{de}\\
&=-T_{cd}\mathcal D^d\mathcal D_eT^{ce}
  +T_{cd}[\mathcal D_e,\mathcal D^c]T^{de}\\
&=-T_{ab}\mathcal D^b\mathcal D_cT^{ac}
  +T_{cd}[\mathcal D_e,\mathcal D^c]T^{de}.
\end{aligned}\tag{SC09}
```

The second line relabels $`c\leftrightarrow d`$ and uses $`T_{dc}=-T_{cd}`$.
The last line only renames dummy indices. The two derivatives have not
been treated as commuting.

Insert the complete M12b commutator, with its two Lorentz actions and its
Q-curvature action:

```math
\begin{aligned}
T_{cd}[\mathcal D_e,\mathcal D^c]T^{de}
={}&T_{cd}C_e{}^{cd}{}_fT^{fe}
 +T_{cd}C_e{}^{ce}{}_fT^{df}\\
&-\frac i2T_{cd}\bar R_e{}^c\gamma^{de}\chi
 +\frac{3i}{32}T_{cd}\bar R_e{}^cR^{de}.
\end{aligned}\tag{SC10}
```

**First Lorentz action.** Antisymmetry of the first curvature pair and
$`T^{fe}=-T^{ef}`$ give two minus signs. Relabel the four contracted indices:

```math
\begin{aligned}
T_{cd}C_e{}^{cd}{}_fT^{fe}
&=C_{abcd}T^{ac}T^{bd}
=\frac12C_{abcd}T^{ab}T^{cd}.\\
T_{cd}C_e{}^{ce}{}_fT^{df}&=0.
\end{aligned}\tag{SC11}
```

The second line is a vanishing curvature trace. The last equality in the
first line is SC06.

**The R–chi matrix product.** Expand the antisymmetrized gamma, move
$`\gamma^e`$ to the left, and use the left gamma trace:

```math
\begin{aligned}
\bar R_e{}^c\gamma^{de}
&=\bar R_e{}^c\gamma^d\gamma^e-\bar R^{dc}\\
&=-\bar R_e{}^c\gamma^e\gamma^d
  +2\bar R^{dc}-\bar R^{dc}\\
&=\bar R^{dc}.
\end{aligned}\tag{SC12}
```

Consequently

```math
-\frac i2T_{cd}\bar R_e{}^c\gamma^{de}\chi
=-\frac i2T_{cd}\bar R^{dc}\chi
=+\frac i2T^{ab}\bar R_{ab}\chi.
\tag{SC13}
```

This sign comes from curvature antisymmetry; no odd fields were interchanged.

**The R–R term.** Antisymmetrize the second curvature, then rename indices:

```math
\frac{3i}{32}T_{cd}\bar R_e{}^cR^{de}
=-\frac{3i}{32}T_{cd}\bar R_e{}^cR^{ed}
=-\frac{3i}{32}T^{ab}\bar R_{ca}R^c{}_b.
\tag{SC14}
```

Adding all four pieces of SC10 gives the exact contracted commutator

```math
T_{cd}[\mathcal D_e,\mathcal D^c]T^{de}
=\frac12C_{abcd}T^{ab}T^{cd}
 +\frac i2T^{ab}\bar R_{ab}\chi
 -\frac{3i}{32}T^{ab}\bar R_{ca}R^c{}_b.
\tag{SC15}
```

Now restore the original coefficient $`64/3`$:

```math
\begin{aligned}
\frac{64}{3}T_{cd}\mathcal D_e\mathcal D^cT^{de}
={}&-\frac{64}{3}T_{ab}\mathcal D^b\mathcal D_cT^{ac}
 +\frac{32}{3}C_{abcd}T^{ab}T^{cd}\\
&+\frac{32i}{3}T^{ab}\bar R_{ab}\chi
 -2iT^{ab}\bar R_{ca}R^c{}_b.
\end{aligned}\tag{SC16}
```

The relative factors are explicitly
$`(64/3)(1/2)=32/3`$, $`(64/3)(i/2)=32i/3`$ and
$`(64/3)(-3i/32)=-2i`$.

### 40.4 Remove the gamma-two matrix inside the RR bilinear

The two original RR terms are numbers 18 and 19 in SC01. We cannot drop the
gamma-two bilinear: its matrix acts between physical fermions and its
external Clifford structure is scalar.

First calculate the two left gamma contractions from SC02/SC04:

```math
\begin{aligned}
\bar R^{cd}\gamma_{ac}
 &=\bar R^{cd}(\gamma_a\gamma_c-\eta_{ac})\\
 &=-\bar R^{cd}\gamma_c\gamma_a+2\bar R_a{}^d-\bar R_a{}^d
 =\bar R_a{}^d,\\
\bar R^{cd}\gamma_{ad}
 &=\bar R^{cd}(\gamma_a\gamma_d-\eta_{ad})\\
 &=-\bar R^{cd}\gamma_d\gamma_a+2\bar R^c{}_a-\bar R^c{}_a
 =\bar R^c{}_a.
\end{aligned}\tag{SC17}
```

Multiply SC05 by the actual left spinor $`\bar R^{cd}`$:

```math
\begin{aligned}
0={}&\bar R^{cd}\gamma_{ab}R_{cd}
-\bar R_a{}^dR_{bd}+\bar R^c{}_aR_{bc}\\
&+\bar R_b{}^dR_{ad}-\bar R^c{}_bR_{ac}
+\underbrace{\bar R^{cd}\gamma_{cd}}_{0}R_{ab}.
\end{aligned}\tag{SC18}
```

The scalar Majorana interchange, including the contracted SU(2) minus,
is

```math
\bar R_{cb}R^c{}_a=-\bar R_{ca}R^c{}_b.
\tag{SC19}
```

Now reduce each of the four middle terms separately:

```math
\begin{aligned}
-\bar R_a{}^dR_{bd}&=-\bar R_{ca}R^c{}_b,\\
+\bar R^c{}_aR_{bc}&=-\bar R_{ca}R^c{}_b,\\
+\bar R_b{}^dR_{ad}&=+\bar R_{cb}R^c{}_a
                  =-\bar R_{ca}R^c{}_b,\\
-\bar R^c{}_bR_{ac}&=+\bar R_{cb}R^c{}_a
                  =-\bar R_{ca}R^c{}_b.
\end{aligned}
```

SC18 therefore gives

```math
\bar R_{cd}\gamma_{ab}R^{cd}=4\bar R_{ca}R^c{}_b.
\tag{SC20}
```

Substitute this result into term 19 before adding it to term 18:

```math
\begin{aligned}
&\frac{113i}{16}T^{ab}\bar R_{ca}R^c{}_b
-\frac{97i}{64}T^{ab}\bar R_{cd}\gamma_{ab}R^{cd}\\
&=\left(\frac{113i}{16}-\frac{97i}{64}\,4\right)
 T^{ab}\bar R_{ca}R^c{}_b
=+iT^{ab}\bar R_{ca}R^c{}_b.
\end{aligned}\tag{SC21}
```

No new Fierz rearrangement is required here: the parameter has already
been factored to the right in Part IV. SC17–SC21 preserve the actual
physical-spinor pairing and explicitly evaluate the remaining matrix.

### 40.5 Add the commutator contributions to all matching terms

There are exactly three changed algebraic coefficients:

```math
\begin{aligned}
C_{abcd}T^{ab}T^{cd}:&\quad
-\frac{52}{3}+8\!\left(\frac12\right)+\frac{32}{3}
=-\frac83,\\
T^{ab}\bar R_{ca}R^c{}_b:&\quad
\frac{113i}{16}-\frac{97i}{64}(4)-2i=-i,\\
T^{ab}\bar R_{ab}\chi:&\quad
-\frac{112i}{3}+\frac{32i}{3}=-\frac{80i}{3}.
\end{aligned}\tag{SC22}
```

Thus keeping only the Lorentz part of the commutator would give two wrong
fermionic coefficients: $`+i`$ and $`-112i/3`$ instead of $`-i`$ and $`-80i/3`$.
This provides a useful sign-sensitive diagnostic.

### 40.6 Put the quartic contraction into the source order

Starting term 12 is not $`(T^2)^2`$. Rename $`(c,d,e,f)`$ as $`(a,b,c,d)`$,
apply the two displayed antisymmetries, and commute only bosonic factors:

```math
\begin{aligned}
T_{cd}T^c{}_eT^d{}_fT^{ef}
 &=T_{ab}T^a{}_cT^b{}_dT^{cd}\\
 &=T_{ab}(-T_c{}^a)T^b{}_d(-T^{dc})\\
 &=T_{ab}T^b{}_dT^{dc}T_c{}^a\\
 &=T_a{}^bT_b{}^dT_d{}^cT_c{}^a\\
 &=T_a{}^bT_b{}^cT_c{}^dT_d{}^a
 =T_{ab}T^{bc}T_{cd}T^{da}.
\end{aligned}\tag{SC23}
```

This is the mixed-index matrix trace $`\mathop{\mathrm{tr}}\nolimits(T^4)`$.
The other quartic term is the distinct contraction $`(T_{ab}T^{ab})^2`$.
They stay separate. For example, with only spatial $`T_{12}=x`$ and
$`T_{34}=y`$ nonzero, they are respectively $`2(x^4+y^4)`$ and
$`4(x^2+y^2)^2`$; their different $`x^2y^2`$ content forbids combining them.

### 40.7 Put the first derivatives and surviving one-gamma terms in order

The mixed gradient in term 16 needs a dummy-index relabeling only:

```math
(\mathcal D_cT_{de})(\mathcal D^dT^{ce})
=(\mathcal D_bT_{ac})(\mathcal D^aT^{bc}),
\qquad (c,d,e)\mapsto(b,a,c).
\tag{SC24}
```

The unmixed gradient is already canonical:
$`(\mathcal D_cT_{de})(\mathcal D^cT^{de}) =(\mathcal D_aT_{bc})(\mathcal D^aT^{bc})`$.
There is no local equality replacing the mixed gradient by a divergence
square without retaining the product-rule divergence and commutator terms.
No such replacement is made.

The two kinetic bilinears contain a single gamma, with no unmultiplied
matrix product left:

```math
\begin{aligned}
\frac38\bar R_{de}\gamma^c\mathcal D_cR^{de}
 &=\frac38\bar R_{ab}\gamma^c\mathcal D_cR^{ab},\\
-\frac{128}{3}\bar\chi\gamma^c\mathcal D_c\chi
 &=-\frac{128}{3}\bar\chi\gamma^a\mathcal D_a\chi.
\end{aligned}\tag{SC25}
```

These matrices are internal to the bilinears; both full bilinears multiply
$`\mathbf1\epsilon^i`$. They must not be moved into the external
$`\gamma_at^a\epsilon^i`$ sector. They also do not vanish by the identical
spinor vector flip: the differentiated spinor is a different argument.
Explicitly $`\bar\chi\gamma^a\mathcal D_a\chi =-\overline{\mathcal D_a\chi}\gamma^a\chi`$ relates two terms; it does
not set either one to zero.

### 40.8 Account for every starting term and add the final coefficients

| Terms of SC01 | Operation and final contribution |
|---|---|
| 1 | $`+\widehat C_{abcd}\widehat C^{abcd}/16`$; unchanged |
| 2,3 | $`(-52/3+4)\widehat C_{abcd}T^{ab}T^{cd}`$, then add $`+32/3`$ from14, giving $`-8/3`$ |
| 4 | Zero by SC08a |
| 5 | Zero by SC08b |
| 6 | Zero by SC08c |
| 7 | Zero by SC08d |
| 8 | Zero by SC08e |
| 9 | $`+(512/9)D T_{ab}T^{ab}`$; unchanged |
| 10 | $`+(32/3)D^2`$; unchanged |
| 11 | $`-(1408/27)(T_{ab}T^{ab})^2`$; unchanged |
| 12 | $`+512T_{ab}T^{bc}T_{cd}T^{da}`$ by SC23 |
| 13 | $`-(64/3)\varepsilon_{abcde}T^{ab}T^{cd}\mathcal D_fT^{ef}`$; unchanged |
| 14 | $`-(64/3)T_{ab}\mathcal D^b\mathcal D_cT^{ac}`$, plus the three corrections in SC16, all added in SC22 |
| 15 | $`-(32/3)(\mathcal D_aT_{bc})(\mathcal D^aT^{bc})`$; dummy relabeling |
| 16 | $`+(32/3)(\mathcal D_bT_{ac})(\mathcal D^aT^{bc})`$ by SC24 |
| 17 | $`-\widehat R_{ab}{}^{ij}(V)\widehat R^{ab}{}_{ij}(V)/6`$; unchanged |
| 18,19 | $`+iT^{ab}\bar R_{ca}R^c{}_b`$, then add $`-2i`$ from14, giving $`-i`$ |
| 20 | $`+(3/8)\bar R_{ab}\gamma^c\mathcal D_cR^{ab}`$; dummy relabeling |
| 21 | $`-(112i/3)T^{ab}\bar R_{ab}\chi`$, then add $`+32i/3`$ from14, giving $`-80i/3`$ |
| 22 | $`-(128/3)\bar\chi\gamma^a\mathcal D_a\chi`$; dummy relabeling |

The resulting four explicit fermion bilinears, before restoring hats, are

```math
\frac38\bar R_{ab}\gamma^c\mathcal D_cR^{ab}
-iT^{ab}\bar R_{ca}R^c{}_b
-\frac{80i}{3}T^{ab}\bar R_{ab}\chi
-\frac{128}{3}\bar\chi\gamma^a\mathcal D_a\chi.
\tag{SC26}
```

This is a statement about explicit bilinears in a supercovariant
representation, not a restriction to quadratic order in independent fermions.

## 41. Consistency Checks

<!-- ASSERT_CONVENTION: source_lock=UNG-WEYL2-OP58-CONVENTIONS-v5; fermion_scope=all_orders; equations_of_motion=none; integration_by_parts=none -->

### 41.1 Indices, parity, weights and reality

Every Lorentz index is paired exactly twice and every doublet index is
contracted. $`\mathcal D`$ is even, so all four bilinears are Grassmann even.
Multiplication by odd $`\epsilon^i`$ gives an odd doublet as required.

The field weights give

```math
\begin{aligned}
w(C^2)=w(D^2)=w(R(V)^2)&=2+2=4,\\
w(DT^2)=w(CT^2)=w(T^4)&=4,\\
w((\mathcal DT)^2)=w(T\mathcal D\mathcal DT)
=w(TT\mathcal DT)&=4,\\
w(\bar R\mathcal DR)=w(\bar\chi\mathcal D\chi)&=\tfrac32+1+\tfrac32=4,\\
w(T\bar RR)=w(T\bar R\chi)&=1+\tfrac32+\tfrac32=4,\\
w(p\epsilon^i)&=4-\tfrac12=\tfrac72.
\end{aligned}\tag{SC27}
```

These are the superconformal weights of the locked fields; they are not
misidentified with canonically normalized Poincare fermion dimensions.

For the C03 reality convention, put $`B=\mathsf C\gamma_0`$. The matrix
relation (checked for the full rank0,1,2 basis) is

```math
B^T(\mathsf C\gamma_{(n)})^*B
=(-1)^{n+1}\mathsf C\gamma_{(n)},\qquad n=0,1,2.
\tag{SC28}
```

The two SU(2) reality matrices preserve the contracted epsilon. Because
complex conjugation does not reverse odd factors in C03, SC28 yields

```math
(\bar u v)^*=-\bar u v,\qquad
(\bar u\gamma_a v)^*=+\bar u\gamma_a v.
\tag{SC29}
```

The scalar bilinears in SC26 carry $`i`$ and are therefore real; the vector
kinetic bilinears have real coefficients and are real. This checks the
relative reality assignments without changing to a Dirac conjugate.
There is no chirality projection in this 5D representation.

### 41.2 Compare every bosonic coefficient with the located source

After setting physical fermions to zero **for this comparison only**,
$`\mathcal D`$ and hats reduce to their bosonic covariants. Twice our answer
has the following coefficients in the exact M04 order:

| Contraction | $`2p`$ bosonic | Printed M04 |
|---|---:|---:|
| $`C^{abcd}C_{abcd}`$ | $`1/8`$ | $`1/8`$ |
| $`D^2`$ | $`64/3`$ | $`64/3`$ |
| $`DT_{ab}T^{ab}`$ | $`1024/9`$ | $`1024/9`$ |
| $`C_{abcd}T^{ab}T^{cd}`$ | $`-16/3`$ | $`-16/3`$ |
| $`R_{ab}{}^{ij}(V)R^{ab}{}_{ij}(V)`$ | $`-1/3`$ | $`-1/3`$ |
| $`(\mathcal D_aT_{bc})(\mathcal D^aT^{bc})`$ | $`-64/3`$ | $`-64/3`$ |
| $`(\mathcal D_bT_{ac})(\mathcal D^aT^{bc})`$ | $`64/3`$ | $`64/3`$ |
| $`T_{ab}\mathcal D^b\mathcal D_cT^{ac}`$ | $`-128/3`$ | $`-128/3`$ |
| $`\varepsilon_{abcde}T^{ab}T^{cd}\mathcal D_fT^{ef}`$ | $`-128/3`$ | $`-128/3`$ |
| $`T_{ab}T^{bc}T_{cd}T^{da}`$ | $`1024`$ | $`1024`$ |
| $`(T_{ab}T^{ab})^2`$ | $`-2816/27`$ | $`-2816/27`$ |

Thus $`2p|_{\rm bos}=N_{\rm printed}|_{\rm bos}`$, term by term with no
integration by parts. This is an output check, not a condition used to
choose the coefficients.

### 41.3 Algebraic limits

For an algebraic restriction, set $`T_{ab}`$ and its displayed derivative
jets to zero separately. A zero field need not have zero full supercovariant
derivatives, so the latter is an explicit restriction here, not an inference.
The expression reduces to

```math
\begin{aligned}
p\big|_{T\equiv0}={}&\frac1{16}C_{abcd}C^{abcd}
+\frac{32}{3}D^2-\frac16\widehat R_{ab}{}^{ij}(V)\widehat R^{ab}{}_{ij}(V)\\
&+\frac38\bar R_{ab}\gamma^c\mathcal D_cR^{ab}
-\frac{128}{3}\bar\chi\gamma^a\mathcal D_a\chi.
\end{aligned}\tag{SC30}
```

This is also what remains directly in SC01. All explicit fermions set to
zero give the 11-term source comparison above. At vanishing curvature,
vanishing fermions and vanishing derivative jets, the remaining polynomial
is

```math
p=\frac{32}{3}D^2+\frac{512}{9}DT_{ab}T^{ab}
+512T_{ab}T^{bc}T_{cd}T^{da}
-\frac{1408}{27}(T_{ab}T^{ab})^2.
\tag{SC31}
```

These are algebraic restrictions of the expression, not claims of new
solutions or supersymmetric backgrounds.

### 41.4 Independent matrix and Grassmann verification

Run [verify_weyl_scalar_canonicalization.py](../src/reference_checks/verify_weyl_scalar_canonicalization.py) through the [component-check runner](../checks/reference_suite.py)
with `--check verify_weyl_scalar_canonicalization` and the package dependencies.
The runner generates `SCALAR-CANONICALIZATION-CHECKS.json` in its temporary
workspace. The retained scalar input/output ledger is
[SCALAR-CANONICALIZATION-LEDGER.json](../inputs/component_ledgers/SCALAR-CANONICALIZATION-LEDGER.json).

The check uses explicit 4x4 Lorentzian gamma matrices, arbitrary constrained
Weyl tensors, gamma-traceless $`R_{ab}`$, arbitrary $`\chi`$, two independent
Grassmann generators, and the contracted SU(2) epsilon. Symmetric
second-derivative jets remain arbitrary; the antisymmetric jets obey the
full M12b commutator. The fermion bilinears are antisymmetric Grassmann
polarizations, not products of commuting spinor coefficients.

Executed results:

- All 625 two-bivector matrix products in SC02 and their scalar traces:
  exact numerical matrix equality, maximum error0.
- The full rank0,1,2 reality matrix basis in SC28: maximum error0.
- All 22 original coefficient additions and the three new coefficient sums:
  exact rational PASS.
- Six independent component samples for the complete22-to15 equality:
  maximum relative residual $`1.75\times10^{-16}`$.
- The crossed $`CTT`$ identity, five vanishing curvature–epsilon terms,
  quartic matrix trace, both spinor gamma reductions and full contracted
  commutator were also checked separately.
- For two samples, all 272 potentially scalar matrix contributions from
  Part V were evaluated before multiplying/reducing their gamma words.
  Their scalar traces agree with the final expression; maximum total
  relative residual $`6.18\times10^{-16}`$. Every individual scalar
  reduction was compared as well (maximum normalized residual
  $`4.17\times10^{-13}`$, including near-zero cancellations).
- All 15 final monomials have weight4 and valid paired indices.

The finite checks supplement the displayed hand derivation; random
component samples alone are not the proof. No claim of an independent
nonlinear supersymmetry-closure test is made.

## 42. Final Result

Restore the full curvature notation. The complete simplified coefficient is

```math
\boxed{
\begin{aligned}
p={}&\frac1{16}\widehat C_{abcd}\widehat C^{abcd}
+\frac{32}{3}D^2+\frac{512}{9}D\,T_{ab}T^{ab}
-\frac83\widehat C_{abcd}T^{ab}T^{cd}
-\frac16\widehat R_{ab}{}^{ij}(V)\widehat R^{ab}{}_{ij}(V)\\
&-\frac{32}{3}(\mathcal D_aT_{bc})(\mathcal D^aT^{bc})
+\frac{32}{3}(\mathcal D_bT_{ac})(\mathcal D^aT^{bc})
-\frac{64}{3}T_{ab}\mathcal D^b\mathcal D_cT^{ac}\\
&-\frac{64}{3}\varepsilon_{abcde}T^{ab}T^{cd}\mathcal D_fT^{ef}
+512T_{ab}T^{bc}T_{cd}T^{da}
-\frac{1408}{27}(T_{ab}T^{ab})^2\\
&+\frac38\overline{\widehat R_{ab}(Q)}\gamma^c\mathcal D_c\widehat R^{ab}(Q)
-iT^{ab}\overline{\widehat R_{ca}(Q)}\widehat R^c{}_{b}(Q)\\
&-\frac{80i}{3}T^{ab}\overline{\widehat R_{ab}(Q)}\chi
-\frac{128}{3}\bar\chi\gamma^a\mathcal D_a\chi.
\end{aligned}
}
\tag{SC32}
```

It contributes to the variation as

```math
\boxed{\left.\delta_Q\varphi_W^i\right|_{\text{scalar singlet}}
=p\,\epsilon^i,\qquad p\text{ given by SC32}.}
\tag{SC33}
```

All 22 starting terms have been added: five vanish, the two $`CTT`$
contractions combine, and the two $`TRR`$ contractions combine. The ordered
second derivative contributes to the three coefficient sums in SC22.
The final representation contains 11 bosonic-looking supercovariant
contractions and 4 explicit fermion bilinears. Hidden fermions in all
covariants remain part of the answer.

## 43. Convention Dependence and Remaining Uncertainties

The result is exact relative to v5/M08 and the previously established
M12 identities. No convention, source coefficient, gauge or formulation
has changed. The result fixes the scalar-singlet slot of the computed
variation; L01 then assigns the candidate linear-multiplet scalar $`N_W=2p`$.
That slot assignment is not a proof of the independent transformation
$`\delta N_W`$ or of full multiplet closure. The vector coefficient,
traceless SU(2) sector, spinor S-law, descendant laws and complete invariant
remain their own calculations. No fermionic Dilaton-Weyl substitution or
Poincare gauge fixing is silently performed here.
