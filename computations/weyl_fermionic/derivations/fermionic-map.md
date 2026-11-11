# Fermionic Weyl-to-linear map

Parts I–II derive S-invariance and the triplet Q-variation. Part III gives the
Q-variation of the working composite spinor. Parts IV–V perform the Fierz and
Clifford collection into the scalar, vector and bivector coefficients.
Part VI proves the bivector cancellation; Parts VII–VIII give the canonical
15-term scalar and 24-term vector coefficients. The displayed equation identifiers locate each
step of the component derivation.

## 1. Problem and Target

This file gives the component calculations for the fermionic terms in
Özkan–Pang Eq. (5.8). **Part I establishes S-invariance of the scalar
triplet.** Parts II–III calculate the Q-variations, and Parts IV–VIII
extract and simplify the singlet scalar and vector coefficients.

The target is a local, off-shell identity:

```math
\delta_S(\eta)L^{ij}=0.
\tag{S01}
```

The following calculation evaluates the variation explicitly. The expected result follows from the transformation
target L01 in the [master conventions](component_conventions.md), but L01 is
not used to set any contribution to zero during the proof.

### Given information and provenance

| Given object | Master relation | Original located source |
|---|---|---|
| Composite scalar triplet | M01 | OP(5.8), printed/PDF p.18 |
| $`\delta_S T`$ and $`\delta_S\chi`$ | W03 | OP(2.11), pp.7–8; W(3.16), printed19/PDF20 |
| $`\delta_S\widehat R(Q)`$ | R05, corrected index placement under X11 | W(3.23), printed21/PDF22 |
| $`\delta_S\widehat R(V)`$ | R06a | W(3.23), printed21/PDF22 |
| Gravitino-curvature gamma trace | G03a | W(3.9), printed16/PDF17 |
| Bar, Grassmann and gamma rules | C01–C04 | OP Appendix A; W Appendix A |

“OP” is the corrected local arXiv:1301.6622v4; “W” is the local
arXiv:hep-th/0104113v4. Routine inputs were read from the master file.
The original W page was reinspected only after a concrete discrepancy was
found in the extracted R05 rule; Section 2 explains that correction.

### Assumptions and permitted operations

**A1.** Five-dimensional Lorentzian, eight-supercharge superconformal tensor
calculus, with the master conventions. The physical gauging is absent.

**A2.** Work off shell and before Poincare gauge fixing. No equation of
motion, auxiliary-field equation, background equation, Killing-spinor
condition or field redefinition is permitted.

**A3.** Retain the full hatted curvatures and the complete supplied S-laws.
There is no expansion in fluctuations, coupling or physical fermion degree.
Hatted quantities include their implicit fermions. The source transformation
laws are inputs; this calculation does not independently rederive them from
all connection definitions.

**A4.** Use the conventional constraint
$`\gamma^a\widehat R_{ab}{}^i(Q)=0`$. It defines the dependent S connection;
it is not the gravitino field equation.

**A5.** $`\eta^i`$, $`\chi^i`$ and $`\widehat R_{ab}{}^i(Q)`$ are Grassmann odd.
The parameterized operator $`\delta_S(\eta)`$ is even, so its product rule has
no extra graded minus. Every actual interchange of odd factors is tracked.

**A6.** All equalities below are pointwise. No integration by parts, discarded
boundary term, boundary condition, gauge slice or bosonic truncation is used
in the proof. Limits are checked only after the identity is established.

The working fields are $`T_{ab}`$, $`\chi^i`$, the gravitino curvature and the
SU(2) curvature. They may be treated as Standard-Weyl covariants at this
stage. The identity also applies after a consistent full Dilaton-Weyl
substitution, without using an auxiliary equation.

## 2. Convention Ledger

<!-- ASSERT_CONVENTION: natural_units=hbar=c=1, metric_signature=(-,+,+,+,+); master C01, source_lock=UNG-WEYL2-OP58-CONVENTIONS-v4 -->

| Item | Convention used here |
|---|---|
| Dimension/signature | $`D=5`$, $`\eta_{ab}=\mathrm{diag}(-,+,+,+,+)`$ |
| Indices | Tangent $`a,b,c,d=0,\ldots,4`$; doublet $`i,j=1,2`$ |
| Lorentz raising | $`T_a{}^c=\eta^{cd}T_{ad}`$; $`T^c{}_a=\eta^{cd}T_{da}=-T_a{}^c`$ |
| SU(2) | $`X^i=\varepsilon^{ij}X_j`$, $`X_i=X^j\varepsilon_{ji}`$, $`\varepsilon_{12}=\varepsilon^{12}=1`$ |
| Brackets | Unit-weight antisymmetrization and symmetrization |
| Clifford algebra | $`\{\gamma_a,\gamma_b\}=2\eta_{ab}`$; $`\gamma_{ab}=\gamma_a\gamma_b-\eta_{ab}`$ |
| Gamma products | $`\gamma_{a_1\ldots a_n}=\gamma_{[a_1}\cdots\gamma_{a_n]}`$ |
| Dot | $`\gamma\!\cdot\!T=\gamma^{ab}T_{ab}`$, with no $`1/2`$ |
| Orientation | $`\epsilon^{01234}=+1`$, $`\gamma^{01234}=i`$; no duality identity is needed in the hand proof |
| Conjugation | $`\bar\zeta=\zeta^T\mathsf C`$; linear Majorana bar, not Hermitian conjugation |
| Charge-conjugation matrix | $`\mathsf C^T=-\mathsf C`$, $`(\mathsf C\gamma_a)^T=-\mathsf C\gamma_a`$ |
| Reality/chirality | Symplectic Majorana; no independent chirality condition in 5D |
| Fermionic functional derivatives | None occur; only the even SUSY variation is used |
| Curvature conventions | Master G02/R01–R03; hatted tangent S-laws R05/R06a already include dependent connections |
| Higher-derivative normalization | Unchanged; no action or $`\lambda_{\rm Weyl}`$ enters this local identity |

For reference, the curvature convention behind these laws is
$`R_{\mu\nu}{}^{ab}=2\partial_{[\mu}\omega_{\nu]}{}^{ab} +2\omega_{[\mu}{}^{ac}\omega_{\nu]c}{}^b`$ and the OP Ricci contraction is
$`\mathcal R_{\mu\nu}=\widehat R'_{\mu\rho}{}^{ab}(M)e_b{}^\rho e_{\nu a}`$.
Neither curvature sign nor a curvature commutator is changed or used to
simplify the S-variation. $`\delta_S e_\mu{}^a=0`$ from W01, so the inverse
vielbein and the world/tangent conversion also have zero S-variation.
The full curvature laws below therefore require no extra frame terms.

### Convention checks

| Check | Result |
|---|---|
| Metric signature | Matches the active lock exactly |
| Fourier convention | Unset in lock and unused here; no Fourier transformation is introduced |
| State normalization | Unset and unused; no states or mode normalization appear |
| Coupling convention | Unchanged and absent from this identity |
| Renormalization scheme | Unset and unused in this classical local calculation |

The conventions listed above are sufficient for this local classical identity. No approximation is used.

### Index ordering in the S variation

The v3 master extraction of R05 had $`T^c{}_{[a}`$ in its middle S-term.
The inspected W(3.23) page actually has **$`T_{[a}{}^c`$**. Their relation is

```math
T^c{}_a=\eta^{cd}T_{da}=-\eta^{cd}T_{ad}=-T_a{}^c.
\tag{S02}
```

This is an extraction error in our file, not a newly alleged error in W.
Master X11 fixes the source ordering. All proof lines below use that
corrected convention.
Section 5.5 displays the nonzero residual produced by the old extraction,
so the correction is independently testable and is not a silent adjustment.

## 3. Definitions and Required Identities

<!-- ASSERT_CONVENTION: natural_units=hbar=c=1, metric_signature=(-,+,+,+,+); master C01, source_lock=UNG-WEYL2-OP58-CONVENTIONS-v4 -->

### 3.1 Short notation and the complete starting expression

To keep the algebra readable, define

```math
\mathscr R_{ab}{}^i:=\widehat R_{ab}{}^i(Q),\qquad
\mathscr V_{ab}{}^{ij}:=\widehat R_{ab}{}^{ij}(V),\qquad
K:=\gamma^{cd}T_{cd}.
\tag{S03}
```

The symbols $`\mathscr R`$ and $`\mathscr V`$ always remain fully supercovariant;
these definitions are not a truncation. The three summands are

```math
\begin{aligned}
L^{ij}&=L_R^{ij}+L_\chi^{ij}+L_{VT}^{ij},\\
L_R^{ij}&=\frac i4\bar{\mathscr R}_{ab}{}^{(i}\mathscr R^{j)ab},\\
L_\chi^{ij}&=\frac{256i}{3}\bar\chi^{(i}\chi^{j)},\\
L_{VT}^{ij}&=\frac{16}{3}\mathscr V_{ab}{}^{ij}T^{ab}.
\end{aligned}\tag{S04}
```

Their conformal weights are respectively $`3/2+3/2=3`$,
$`3/2+3/2=3`$, and $`2+1=3`$. These are Weyl weights before compensator fixing,
not a claim about canonically normalized Poincare field dimensions.
Each summand is Grassmann even and symmetric in the two free SU(2) indices.

The relevant weights are

```math
w(T)=1,\quad w(\mathscr R)=w(\chi)=\frac32,\quad
w(\mathscr V)=2,\quad w(\eta)=\frac12,\quad w(L)=3.
\tag{S05}
```

### 3.2 S-transformations to substitute

Set the Q-parameter to zero in W03/R05/R06a. Retain the S-parameter:

```math
\delta_S T_{ab}=0,\qquad
\delta_S\chi^i=\frac14K\eta^i.
\tag{S06}
```

```math
\delta_S\mathscr R_{ab}{}^i=A_{ab}\eta^i,\qquad
A_{ab}:=-8T_{ab}\mathbf1
+\frac{16}{3}T_{[a}{}^c\gamma_{b]c}
+\frac43\gamma_{abcd}T^{cd}.
\tag{S07}
```

In particular,
$`T_{[a}{}^c\gamma_{b]c}=(T_a{}^c\gamma_{bc}-T_b{}^c\gamma_{ac})/2`$.
The last required law is

```math
\delta_S\mathscr V_{ab}{}^{ij}
=\frac{3i}{2}\bar\eta^{(i}\mathscr R_{ab}{}^{j)}
+8i\bar\eta^{(i}\gamma_{ab}\chi^{j)}.
\tag{S08}
```

Every term in (S07) has weight $`1+1/2=3/2`$; both terms in (S08)
have weight $`1/2+3/2=2`$. No field equation has been used to obtain these laws.
The full connection-induced terms are already included in these source
curvature transformations; varying an unhatted curvature instead would be
a different calculation.

### 3.3 Derive the Majorana transpose rule

The charge-conjugation conditions give

```math
(\mathsf C\gamma_a)^T=\gamma_a^T\mathsf C^T
=-\gamma_a^T\mathsf C=-\mathsf C\gamma_a
\quad\Longrightarrow\quad
\mathsf C^{-1}\gamma_a^T\mathsf C=\gamma_a.
\tag{S09}
```

For an even matrix $`M`$, define its Majorana transpose
$`\widetilde M=\mathsf C^{-1}M^T\mathsf C`$. Then

```math
\overline{M\eta}=(M\eta)^T\mathsf C
=\eta^TM^T\mathsf C
=\bar\eta\,\widetilde M.
\tag{S10}
```

Transposition reverses the order of the n gamma matrices. Reversing an
antisymmetric n-index string needs $`n(n-1)/2`$ interchanges, hence

```math
\widetilde{\gamma_{a_1\ldots a_n}}
=(-1)^{n(n-1)/2}\gamma_{a_1\ldots a_n},\qquad
\widetilde{\mathbf1}=\mathbf1,\quad
\widetilde{\gamma_{ab}}=-\gamma_{ab},\quad
\widetilde{\gamma_{abcd}}=+\gamma_{abcd}.
\tag{S11}
```

The bar in (S10) does not conjugate numerical factors such as i.
For the present real coefficients, (S06)–(S07) give

```math
\delta_S\bar\chi^i=-\frac14\bar\eta^iK,
\tag{S12}
```

```math
\delta_S\bar{\mathscr R}_{ab}{}^i
=\bar\eta^i\widetilde A_{ab},\qquad
\widetilde A_{ab}=-8T_{ab}\mathbf1
-\frac{16}{3}T_{[a}{}^c\gamma_{b]c}
+\frac43\gamma_{abcd}T^{cd}.
\tag{S13}
```

The middle term changes sign under the bar; the rank-four term does not.
These two different transpose signs will be needed together.

### 3.4 Derive the scalar-bilinear interchange used below

For two odd spinors with explicit SU(2) labels,

```math
\bar\alpha^i\beta^j
=\alpha^{i\,u}\mathsf C_{uv}\beta^{j\,v}
=-\beta^{j\,v}\mathsf C_{uv}\alpha^{i\,u}
=+\beta^{j\,v}\mathsf C_{vu}\alpha^{i\,u}
=\bar\beta^j\alpha^i.
\tag{S14}
```

The first minus is the odd-spinor interchange. The second minus comes
from $`\mathsf C_{uv}=-\mathsf C_{vu}`$. They cancel. Therefore

```math
\bar\alpha^{(i}\beta^{j)}
=\bar\beta^{(i}\alpha^{j)}.
\tag{S15}
```

No suppressed-index flip is used: the symmetric pair i,j remains explicit
throughout. No Fierz rearrangement is needed in this calculation.

## 4. Detailed Derivation

### Step 1 — Consequences of the conventional gamma trace

<!-- ASSERT_CONVENTION: natural_units=hbar=c=1, metric_signature=(-,+,+,+,+); master C01, source_lock=UNG-WEYL2-OP58-CONVENTIONS-v4 -->

Raise the indices of the conventional constraint and use antisymmetry:

```math
\gamma^a\mathscr R_{ab}{}^i=0
\quad\Longrightarrow\quad
\gamma_a\mathscr R^{ab\,i}=0,
\qquad
\gamma_b\mathscr R^{ab\,i}
=-\gamma_b\mathscr R^{ba\,i}=0.
\tag{S16}
```

The contracted rank-two gamma also vanishes:

```math
\begin{aligned}
\gamma_{ab}\mathscr R^{ab\,i}
&=(\gamma_a\gamma_b-\eta_{ab})\mathscr R^{ab\,i}\\
&=\gamma_a(\gamma_b\mathscr R^{ab\,i})
-\frac12\eta_{ab}(\mathscr R^{ab\,i}+\mathscr R^{ba\,i})=0.
\end{aligned}\tag{S17}
```

Here the first term vanishes by (S16). The second displays the contraction
of a symmetric metric with an antisymmetric curvature; it is zero without
any gravitino equation of motion.

### Step 2 — Reduce the middle gamma structure

<!-- ASSERT_CONVENTION: natural_units=hbar=c=1, metric_signature=(-,+,+,+,+); master C01, source_lock=UNG-WEYL2-OP58-CONVENTIONS-v4 -->

Define the spinor $`X^i:=T_{ab}\mathscr R^{ab\,i}`$ and consider

```math
\begin{aligned}
Y^i&:=T_{[a}{}^c\gamma_{b]c}\mathscr R^{ab\,i}\\
&=\frac12T_a{}^c\gamma_{bc}\mathscr R^{ab\,i}
-\frac12T_b{}^c\gamma_{ac}\mathscr R^{ab\,i}\\
&=\frac12T_a{}^c\gamma_{bc}\mathscr R^{ab\,i}
-\frac12T_a{}^c\gamma_{bc}\mathscr R^{ba\,i}\\
&=T_a{}^c\gamma_{bc}\mathscr R^{ab\,i}.
\end{aligned}\tag{S18}
```

The third line relabels a and b in the second summand only. The last line
uses $`\mathscr R^{ba}=-\mathscr R^{ab}`$; thus the antisymmetrization's
factor $`1/2`$ is accounted for.

Now move $`\gamma_b`$ to the right so it can act on the gamma trace:

```math
\begin{aligned}
\gamma_{bc}\mathscr R^{ab\,i}
&=(\gamma_b\gamma_c-\eta_{bc})\mathscr R^{ab\,i}\\
&=(-\gamma_c\gamma_b+2\eta_{bc}-\eta_{bc})\mathscr R^{ab\,i}\\
&=-\gamma_c(\gamma_b\mathscr R^{ab\,i})
+\eta_{bc}\mathscr R^{ab\,i}\\
&=\eta_{bc}\mathscr R^{ab\,i}.
\end{aligned}\tag{S19}
```

Substitute this into (S18), with the **source** Lorentz-index ordering:

```math
Y^i=T_a{}^c\eta_{bc}\mathscr R^{ab\,i}
=T_{ab}\mathscr R^{ab\,i}=X^i.
\tag{S20}
```

Both sides have weight $`1+3/2=5/2`$, one free doublet spinor index and
no free Lorentz index. Inserting $`T^c{}_a`$ instead would give $`-X^i`$;
that is precisely the v3 extraction error.

### Step 3 — Reduce the rank-four gamma structure

<!-- ASSERT_CONVENTION: natural_units=hbar=c=1, metric_signature=(-,+,+,+,+); master C01, source_lock=UNG-WEYL2-OP58-CONVENTIONS-v4 -->

We need $`Z^i:=\gamma_{abcd}T^{cd}\mathscr R^{ab\,i}`$.
First derive the gamma product to be contracted. From the Clifford algebra,

```math
\gamma_d\gamma_{ab}
=\gamma_{dab}+\eta_{da}\gamma_b-\eta_{db}\gamma_a,
\tag{S21}
```

and multiplying the antisymmetric three-gamma string by $`\gamma_c`$ gives

```math
\gamma_c\gamma_{dab}
=\gamma_{cdab}+\eta_{cd}\gamma_{ab}
-\eta_{ca}\gamma_{db}+\eta_{cb}\gamma_{da}.
\tag{S22}
```

These are the n=2 and n=3 cases of C04c, obtained by moving $`\gamma_c`$
past each gamma in turn; each contraction retains its alternating sign.
Use $`\gamma_{cd}=\gamma_c\gamma_d-\eta_{cd}`$ and insert (S21)–(S22):

```math
\begin{aligned}
\gamma_{cd}\gamma_{ab}
&=\gamma_c(\gamma_{dab}+\eta_{da}\gamma_b-\eta_{db}\gamma_a)
-\eta_{cd}\gamma_{ab}\\
&=\gamma_{cdab}+\eta_{cd}\gamma_{ab}
-\eta_{ca}\gamma_{db}+\eta_{cb}\gamma_{da}
+\eta_{da}(\gamma_{cb}+\eta_{cb})
-\eta_{db}(\gamma_{ca}+\eta_{ca})-\eta_{cd}\gamma_{ab}\\
&=\gamma_{cdab}
+\eta_{da}\gamma_{cb}-\eta_{ca}\gamma_{db}
-\eta_{db}\gamma_{ca}+\eta_{cb}\gamma_{da}
+\eta_{da}\eta_{cb}-\eta_{ca}\eta_{db}.
\end{aligned}\tag{S23}
```

Contract (S23) with $`\mathscr R^{ab\,i}`$. Its left side is zero by
(S17). Evaluate the four rank-two terms one at a time:

```math
\begin{aligned}
\eta_{da}\gamma_{cb}\mathscr R^{ab\,i}
&=\gamma_{cb}\mathscr R_d{}^{b\,i}
=(\gamma_c\gamma_b-\eta_{cb})\mathscr R_d{}^{b\,i}
=-\mathscr R_{dc}{}^i=+\mathscr R_{cd}{}^i,\\
-\eta_{ca}\gamma_{db}\mathscr R^{ab\,i}
&=-\gamma_{db}\mathscr R_c{}^{b\,i}
=-(\gamma_d\gamma_b-\eta_{db})\mathscr R_c{}^{b\,i}
=+\mathscr R_{cd}{}^i,\\
-\eta_{db}\gamma_{ca}\mathscr R^{ab\,i}
&=-\gamma_{ca}\mathscr R^a{}_d{}^i
=-(\gamma_c\gamma_a-\eta_{ca})\mathscr R^a{}_d{}^i
=+\mathscr R_{cd}{}^i,\\
\eta_{cb}\gamma_{da}\mathscr R^{ab\,i}
&=\gamma_{da}\mathscr R^a{}_c{}^i
=(\gamma_d\gamma_a-\eta_{da})\mathscr R^a{}_c{}^i
=-\mathscr R_{dc}{}^i=+\mathscr R_{cd}{}^i.
\end{aligned}\tag{S24}
```

Each rightmost gamma trace in those lines vanishes by (S16). The two scalar
metric terms give

```math
(\eta_{da}\eta_{cb}-\eta_{ca}\eta_{db})\mathscr R^{ab\,i}
=\mathscr R_{dc}{}^i-\mathscr R_{cd}{}^i=-2\mathscr R_{cd}{}^i.
\tag{S25}
```

The two pairs can be exchanged in a rank-four gamma with sign
$`(-1)^{2\times2}=+1`$, so $`\gamma_{cdab}=\gamma_{abcd}`$. Equation (S23)
therefore becomes

```math
0=\gamma_{abcd}\mathscr R^{ab\,i}
+4\mathscr R_{cd}{}^i-2\mathscr R_{cd}{}^i,
\qquad
\gamma_{abcd}\mathscr R^{ab\,i}=-2\mathscr R_{cd}{}^i.
\tag{S26}
```

Multiplying by $`T^{cd}`$ and then renaming c,d to a,b gives the required
second contraction:

```math
Z^i=-2T^{cd}\mathscr R_{cd}{}^i
=-2T_{ab}\mathscr R^{ab\,i}=-2X^i.
\tag{S27}
```

The metric factors in the second equality raise/lower both contracted
indices; no sign is guessed from treating the tangent metric as Euclidean.
Again the weight is $`5/2`$ and the free-index content matches $`X^i`$.

### Step 4 — Vary the gravitino-curvature bilinear

<!-- ASSERT_CONVENTION: natural_units=hbar=c=1, metric_signature=(-,+,+,+,+); master C01, source_lock=UNG-WEYL2-OP58-CONVENTIONS-v4 -->

Apply the even product rule to both factors, before reordering any spinor:

```math
\delta_S L_R^{ij}=\frac i4
\left[(\delta_S\bar{\mathscr R}_{ab}{}^{(i})\mathscr R^{j)ab}
+\bar{\mathscr R}_{ab}{}^{(i}\delta_S\mathscr R^{j)ab}\right].
\tag{S28}
```

To see why the two terms are equal, expand the second one's SU(2)
symmetrization and use the scalar flip (S14):

```math
\begin{aligned}
\bar{\mathscr R}_{ab}{}^{(i}\delta_S\mathscr R^{j)ab}
&=\frac12\left(\bar{\mathscr R}_{ab}{}^i\delta_S\mathscr R^{jab}
+\bar{\mathscr R}_{ab}{}^j\delta_S\mathscr R^{iab}\right)\\
&=\frac12\left(\overline{\delta_S\mathscr R^{jab}}\,\mathscr R_{ab}{}^i
+\overline{\delta_S\mathscr R^{iab}}\,\mathscr R_{ab}{}^j\right)\\
&=(\delta_S\bar{\mathscr R}_{ab}{}^{(i})\mathscr R^{j)ab}.
\end{aligned}\tag{S29}
```

The last line moves the constant tangent metrics through the Majorana bar
and exchanges the two summands. Since $`\delta_S\mathscr R`$ is odd,
(S14) applies with exactly the two cancelling signs already derived.
Thus

```math
\delta_S L_R^{ij}=\frac i2\bar\eta^{(i}
\widetilde A_{ab}\mathscr R^{j)ab}.
\tag{S30}
```

Insert all three terms of (S13), and then the two proved contractions:

```math
\begin{aligned}
\widetilde A_{ab}\mathscr R^{ab\,i}
&=-8X^i-\frac{16}{3}Y^i+\frac43Z^i\\
&=-8X^i-\frac{16}{3}X^i+\frac43(-2X^i)\\
&=\frac{-24-16-8}{3}X^i=-16X^i.
\end{aligned}\tag{S31}
```

Consequently the first part of the variation is

```math
\delta_S L_R^{ij}=-8i\bar\eta^{(i}X^{j)}
=-8iT_{ab}\bar\eta^{(i}\mathscr R^{j)ab}.
\tag{S32}
```

Its weight is $`1/2+1+3/2=3`$. It is not zero on its own.

### Step 5 — Vary the chi bilinear

<!-- ASSERT_CONVENTION: natural_units=hbar=c=1, metric_signature=(-,+,+,+,+); master C01, source_lock=UNG-WEYL2-OP58-CONVENTIONS-v4 -->

The full product rule gives

```math
\delta_S L_\chi^{ij}=\frac{256i}{3}
\left[(\delta_S\bar\chi^{(i})\chi^{j)}
+\bar\chi^{(i}\delta_S\chi^{j)}\right].
\tag{S33}
```

Display the scalar flip for this pair as well:

```math
\begin{aligned}
\bar\chi^{(i}\delta_S\chi^{j)}
&=\frac12(\bar\chi^i\delta_S\chi^j+\bar\chi^j\delta_S\chi^i)\\
&=\frac12(\overline{\delta_S\chi^j}\chi^i
+\overline{\delta_S\chi^i}\chi^j)
=(\delta_S\bar\chi^{(i})\chi^{j)}.
\end{aligned}\tag{S34}
```

Substitute (S12), retaining the rank-two transpose minus:

```math
\begin{aligned}
\delta_S L_\chi^{ij}
&=\frac{512i}{3}(\delta_S\bar\chi^{(i})\chi^{j)}\\
&=\frac{512i}{3}\left(-\frac14\bar\eta^{(i}K\chi^{j)}\right)\\
&=-\frac{128i}{3}\bar\eta^{(i}\gamma^{ab}T_{ab}\chi^{j)}.
\end{aligned}\tag{S35}
```

This has weight $`1/2+1+3/2=3`$. No contracted-SU(2) flip was substituted
for the explicit-index scalar flip.

### Step 6 — Vary the R-symmetry-curvature times T term

<!-- ASSERT_CONVENTION: natural_units=hbar=c=1, metric_signature=(-,+,+,+,+); master C01, source_lock=UNG-WEYL2-OP58-CONVENTIONS-v4 -->

First vary both factors. The second one vanishes by its actual S-law (S06):

```math
\begin{aligned}
\delta_S L_{VT}^{ij}
&=\frac{16}{3}\left[(\delta_S\mathscr V_{ab}{}^{ij})T^{ab}
+\mathscr V_{ab}{}^{ij}\delta_ST^{ab}\right]\\
&=\frac{16}{3}T^{ab}
\left[\frac{3i}{2}\bar\eta^{(i}\mathscr R_{ab}{}^{j)}
+8i\bar\eta^{(i}\gamma_{ab}\chi^{j)}\right]\\
&=8iT^{ab}\bar\eta^{(i}\mathscr R_{ab}{}^{j)}
+\frac{128i}{3}T^{ab}\bar\eta^{(i}\gamma_{ab}\chi^{j)}\\
&=8i\bar\eta^{(i}X^{j)}+\frac{128i}{3}\bar\eta^{(i}K\chi^{j)}.
\end{aligned}\tag{S36}
```

In the last line, $`T^{ab}\mathscr R_{ab}=T_{ab}\mathscr R^{ab}`$ and
$`T^{ab}\gamma_{ab}=T_{ab}\gamma^{ab}`$. The even tensor T moves through
spinors without a Grassmann sign. Both terms have weight3.

### Step 7 — Collect independent structures and cancel

<!-- ASSERT_CONVENTION: natural_units=hbar=c=1, metric_signature=(-,+,+,+,+); master C01, source_lock=UNG-WEYL2-OP58-CONVENTIONS-v4 -->

There are two remaining tensor-spinor structures. Their coefficients are

| Contribution | $`i\bar\eta^{(i}X^{j)}`$ | $`i\bar\eta^{(i}K\chi^{j)}`$ |
|---|---:|---:|
| $`\delta_S L_R^{ij}`$, (S32) | $`-8`$ | $`0`$ |
| $`\delta_S L_\chi^{ij}`$, (S35) | $`0`$ | $`-128/3`$ |
| $`\delta_S L_{VT}^{ij}`$, (S36) | $`+8`$ | $`+128/3`$ |
| Sum | $`0`$ | $`0`$ |

In equations, the complete result of the expansion is

```math
\begin{aligned}
\delta_S L^{ij}
&=(-8i+8i)\bar\eta^{(i}X^{j)}
+\left(-\frac{128i}{3}+\frac{128i}{3}\right)\bar\eta^{(i}K\chi^{j)}\\
&=0\,\bar\eta^{(i}X^{j)}+0\,\bar\eta^{(i}K\chi^{j)}=0.
\end{aligned}\tag{S37}
```

For the user's lower-index notation, lower each index by C02:

```math
L_{ij}=L^{kl}\varepsilon_{ki}\varepsilon_{lj},\qquad
\delta_S L_{ij}=(\delta_S L^{kl})\varepsilon_{ki}\varepsilon_{lj}=0.
\tag{S38}
```

The invariant SU(2) epsilon symbols do not transform under S.

## 5. Consistency Checks

<!-- ASSERT_CONVENTION: natural_units=hbar=c=1, metric_signature=(-,+,+,+,+); master C01, source_lock=UNG-WEYL2-OP58-CONVENTIONS-v4 -->

### 5.1 Indices, parity, weights, covariance and equality status

The only free indices in (S32), (S35) and (S36) are the symmetric i,j.
In $`X^i=T_{ab}\mathscr R^{ab\,i}`$, both a,b are paired once up/once down.
In $`K=\gamma^{ab}T_{ab}`$, both indices are contracted and K is a spinor
matrix. Thus $`\bar\eta^{(i}X^{j)}`$ and $`\bar\eta^{(i}K\chi^{j)}`$ are
Lorentz scalars in the same SU(2) triplet.

Each term has two odd factors, so its parity is $`1+1=0`$ modulo2.
Equations (S20), (S27), (S32), (S35) and (S36) show the weights at each
major reduction. No field rescaling or coupling-dependent dimension enters.
All expressions use covariant tangent tensors, so no preferred frame or
coordinate background was introduced by the proof.

The crucial factors are individually visible: the $`1/2`$ in (S18) cancels
against the a↔b antisymmetry; each bilinear has two product-rule contributions
in (S29)/(S34); $`\delta\chi`$ contributes $`1/4`$; the rank-two Majorana
transpose contributes its minus sign. Dot contractions have no hidden $`1/2`$.

There are no derivatives in the S-laws (S06)–(S08), and none is introduced
by the proof. Thus every equality is local and exact, with no total derivative,
boundary term or EOM-proportional remainder. No chirality projection occurs.

### 5.2 Reality check

In C03's symplectic-Majorana convention, charge conjugation leaves an even
rank gamma matrix invariant and gives one extra minus for a bispinor when
ordinary complex conjugation is restored [W(A.5), extracted in C03]. Hence,
for $`\Gamma=\mathbf1`$ or $`K`$ with real T,

```math
\left(\bar\eta^{(i}\Gamma\zeta^{j)}\right)^*
=-\bar\eta_{(i}\Gamma\zeta_{j)},\qquad
\left(i\bar\eta^{(i}\Gamma\zeta^{j)}\right)^*
=i\bar\eta_{(i}\Gamma\zeta_{j)}.
\tag{S39}
```

Here the second equality uses $`i^*=-i`$ as well as the bispinor minus.
Both cancelling structures therefore have the same triplet reality condition
$`(F^{ij})^*=F_{ij}`$. The scalar bilinears in L carry the same i-factor,
while $`\mathscr V^{ij}`$ already has triplet reality and T is real.
Thus the cancellation respects the reality assignment of L. This does not
require turning the linear Majorana bar into Hermitian conjugation.

### 5.3 Explicit restrictions of the proved identity

| Restriction | Surviving variation before collection | Result |
|---|---|---|
| $`T_{ab}=0`$ | $`K=X=0`$, $`\delta_S\mathscr R=\delta_S\chi=0`$, and $`T\delta_S\mathscr V=0`$ | $`0`$ |
| $`\mathscr R_{ab}=0`$ | $`-128i\bar\eta^{(i}K\chi^{j)}/3+128i\bar\eta^{(i}K\chi^{j)}/3`$ | $`0`$ |
| $`\chi=0`$ | $`-8i\bar\eta^{(i}X^{j)}+8i\bar\eta^{(i}X^{j)}`$ | $`0`$ |
| All physical fermions zero | $`\mathscr R=\chi=0`$, hence $`\delta_S\mathscr V=0`$ although bosonic $`\mathscr V T`$ need not vanish | $`0`$ |

These are algebraic restrictions, not asserted S-invariant gauge slices or
vacuum solutions. The ungauged condition was retained from the beginning;
there is no unexamined gauging limit in the proof.

### 5.4 Independent Clifford-matrix verification

The reproducible cross-check is
[verify_weyl_map_s_invariance.py](../src/reference_checks/verify_weyl_map_s_invariance.py),
with concrete output in [component check commands and output scope](../README.md).
It uses the representation

```math
\gamma^0=-i\sigma_3\otimes\mathbf1_2,\quad
\gamma^1=\sigma_1\otimes\sigma_1,\quad
\gamma^2=\sigma_1\otimes\sigma_2,\quad
\gamma^3=\sigma_1\otimes\sigma_3,\quad
\gamma^4=\sigma_2\otimes\mathbf1_2,\quad
\mathsf C=\gamma^2\gamma^4,
\tag{S40}
```

where $`\sigma_1=\left(\begin{smallmatrix}0&1\\1&0\end{smallmatrix}\right)`$,
$`\sigma_2=\left(\begin{smallmatrix}0&-i\\i&0\end{smallmatrix}\right)`$ and
$`\sigma_3=\mathrm{diag}(1,-1)`$. The code checks the Clifford and transpose
relations, all 625 index choices in (S23), and the even-rank reality identity
$`B^T(\mathsf C\Gamma)^*B=-\mathsf C\Gamma`$ before testing the variation.

It does not replace odd spinors by commuting numerical spinors. It computes
**coefficients of ordered Grassmann monomials** $`\eta_\alpha r_\beta`$ and
$`\eta_\alpha\chi_\beta`$. For example, the two raw curvature-bilinear variations
have coefficient matrices

```math
\overline{A\eta}\,r=\eta^TA^T\mathsf C r,
\qquad
\bar r A\eta=-\eta^T(\mathsf C A)^T r.
\tag{S41}
```

The minus in the second formula explicitly reorders the odd parameter.
These two expressions are implemented separately, rather than assuming the
factor of two used in the hand reduction.

To cover the constrained curvature, start with an arbitrary spinor two-form
$`B_{ab}`$ and define

```math
q_b=\gamma^a B_{ab},\qquad q=\gamma^bq_b,\qquad
\mathcal P(B)_{ab}=B_{ab}-\frac23\gamma_{[a}q_{b]}
+\frac1{12}\gamma_{ab}q.
\tag{S42}
```

The gamma trace vanishes because the Clifford algebra gives

```math
\begin{aligned}
\gamma^a\gamma_{[a}q_{b]}
&=\frac12(5q_b-\gamma^a\gamma_bq_a)
=\frac12(5q_b+\gamma_bq-2q_b)
=\frac32q_b+\frac12\gamma_bq,\\
\gamma^a\gamma_{ab}q&=4\gamma_bq,\\
\gamma^a\mathcal P(B)_{ab}
&=q_b-\frac23\left(\frac32q_b+\frac12\gamma_bq\right)
+\frac4{12}\gamma_bq=0.
\end{aligned}\tag{S43}
```

If B already obeys the constraint, $`q_b=q=0`$ and $`\mathcal P(B)=B`$.
Thus projecting the 40 unconstrained two-form-spinor basis elements spans
the full allowed curvature space; no special solution is sampled.

For all ten independent T basis tensors and all 40 projected curvature
basis elements, the code checks $`Y=X`$, $`Z=-2X`$, and both raw product-rule
contributions to $`\delta L_R+\delta L_{VT}|_{\mathscr R}`$. This covers
400 tensor pairs and 1600 parameter-spinor coefficients. It separately checks
160 coefficients in the chi sector and gamma-tracelessness of $`\delta_S\mathscr R`$.
Integer-scaled matrices avoid divisions by3; all resulting Gaussian-integer
components are at most768 in magnitude and are exactly representable in the
chosen binary64 storage. Equality tests use no numerical tolerance.

**Recorded output:** all of these finite-basis tests pass. They independently
check the algebra of this S-variation, not the unknown Q-variation or the
remaining map components.

### 5.5 Negative control: retain the erroneous v3 index order

With $`T^c{}_{[a}=-T_{[a}{}^c`$, the middle contraction in the barred variation
has the opposite sign. Equations (S20)/(S27) would give

```math
\widetilde A^{\rm old}_{ab}\mathscr R^{ab\,i}
=-8X^i+\frac{16}{3}X^i+\frac43(-2X^i)
=-\frac{16}{3}X^i.
\tag{S44}
```

Its first summand would therefore vary as $`-8i\bar\eta^{(i}X^{j)}/3`$,
while the correct $`VT`$ variation still contributes $`+8i\bar\eta^{(i}X^{j)}`$.
The chi terms still cancel, leaving

```math
\delta_S L^{ij}\big|_{\text{old extraction}}
=\left(-\frac{8i}{3}+8i\right)\bar\eta^{(i}X^{j)}
=\frac{16i}{3}\bar\eta^{(i}X^{j)}\ne0
\quad\text{for generic }T,\mathscr R,\eta.
\tag{S45}
```

The checker reproduces precisely this residual for every basis input and
also detects failure of $`\gamma^a\delta_S\mathscr R_{ab}=0`$ with the old
rule. It records a concrete nonzero example. This separates a meaningful
cancellation test from code that merely returns zero by assumption.

### 5.6 Approximation and verification scope

There is no approximation error: no field, fermion order or small parameter
was discarded. The result is exact subject to the given supercovariant S-laws
and their conventional gamma-trace constraint. Re-deriving those source laws
from all dependent connections is outside this check. The finite-basis test
checks their algebraic use, not their independent superspace derivation.

## 6. Final Result

Under A1–A6, with the source index ordering restored in v4,

```math
\boxed{\delta_S(\eta)L^{ij}=0,\qquad \delta_S(\eta)L_{ij}=0.}
\tag{S46}
```

The cancellation is between the two fermionic bilinears and the
supercovariant $`R(V)T`$ term. It holds locally, off shell, with no gauge or
background restriction and no fermion truncation. It establishes that the
printed scalar triplet passes the S-invariance test required of the composite
linear multiplet.

## 7. Convention Dependence and Remaining Uncertainties

1. The numerical coefficients refer to the OP/W normalization, full dot
   contraction and linear Majorana bar stated above. A different convention
   requires a complete conversion, not an isolated sign replacement.
2. The distinction $`T_a{}^c=-T^c{}_a`$ is indispensable. The new v4 lock and
   master X11 record the source-verified extraction correction; the paper's
   printed coefficient has not been altered.
3. Conventional gamma-tracelessness is essential. The proof does not assert
   invariance for an arbitrary unconstrained spinor two-form.
4. This part establishes only the S-law of L. Part II gives the Q-variation
   of L and comparison with the printed eleven-term $`\varphi^i`$; Parts III–VIII
   derive and collect the singlet E/N coefficients.
5. This does not establish the full multiplet, the density's complete
   nonlinear invariance, a total action, a vacuum or a spectrum.

Part II starts from
$`\delta_Q L^{ij}-i\bar\epsilon^{(i}\varphi^{j)}`$ and computes its residual
using the same conventions. The S-result above supplies the input
to that separate calculation.

---

# Part II — Q-variation of the scalar triplet

## 8. Problem and Target

**Task.** Calculate the Q-variation of each of the three summands of M01,
with every product-rule term retained, and compare the coefficient of
$`i\bar\epsilon^{(i}`$ with the eleven terms of the printed spinor M02.
The printed spinor is a comparison target, not an input used to choose
coefficients. We denote the actual result by $`\varphi_Q^i`$.

The starting expression and expected multiplet law are

```math
\begin{aligned}
L^{ij}&=L_R^{ij}+L_\chi^{ij}+L_{VT}^{ij},\\
L_R^{ij}&=\frac i4\bar{\mathscr R}_{ab}^{(i}\mathscr R^{j)ab},\qquad
L_\chi^{ij}=\frac{256i}{3}\bar\chi^{(i}\chi^{j)},\qquad
L_{VT}^{ij}=\frac{16}{3}\mathscr V_{ab}^{ij}T^{ab},\\
\delta_Q L^{ij}&\stackrel{\text{target}}{=}i\bar\epsilon^{(i}\varphi_{\rm OP}^{j)}.
\end{aligned}\tag{Q01}
```

Here and below $`\varphi_{\rm OP}`$ means precisely the literal M02, with its
printed $`16/3`$ coefficient. The calculation below instead gives $`8/3`$ in
that one position. Sections 12–14 display the residual, verification and
limits of this conclusion. No source coefficient is silently edited.

**Provenance.** M01–M02 and L01 come from OP(5.8), PDF/printed p.18, and
OP(2.18), p.9. Q-transformations W03 are OP(2.11) and W(3.16).
R05–R06a are W(3.23), printed21/PDF22; the eliminated S curvature R06b
is W(3.19), printed20/PDF21. Gamma and doublet rules are master C01–C05;
the conventional constraints are G03. The existing master was the working
input. The three specific pages OP18/W21/W22 were visually reinspected
when the $`T^2\mathscr R`$ discrepancy appeared; their transcriptions agree
with the operative formulas used below.

**Assumptions Q-A1–Q-A6.** A1–A4 and A6 of Part I continue to apply.
Replace the S-parameter by a Grassmann-odd Q-parameter $`\epsilon^i`$ and set
$`\eta=0`$ throughout this part. In particular:

1. The calculation is local, off shell, gauge-unfixed and at $`g=0`$.
2. No field equation, background equation, gauge choice, auxiliary
   elimination or field redefinition is used.
3. Full hatted curvatures and full $`\mathcal D`$ are retained. There is no
   expansion or truncation in physical fermion number.
4. $`\gamma^a\mathscr R_{ab}^i=0`$ is a conventional constraint, not an EOM.
5. The parameterized $`\delta_Q`$ is even; its product rule is ordinary.
   Actual exchanges of odd spinors require the flips stated below.
6. There is no integration by parts, total-derivative equivalence or
   boundary condition. Every displayed equality is pointwise relative to
   the stated source laws.

The source Q-curvature laws are inputs, as the source S-laws were in Part I.
This derivation verifies their consequence for $`L`$, not their independent
reconstruction from every elementary connection. This qualification matters
when interpreting the mismatch.

## 9. Convention Ledger

<!-- ASSERT_CONVENTION: natural_units=hbar=c=1, metric_signature=(-,+,+,+,+); master C01, source_lock=UNG-WEYL2-OP58-CONVENTIONS-v4 -->

The full ledger in Section 2 applies without change. The result-sensitive
rules for this calculation are collected here so it can be followed locally.

| Item | Rule used in Part II |
|---|---|
| Geometry | $`D=5`$, $`\eta_{ab}=(-,+,+,+,+)`$; tangent $`a,b=0,\ldots,4`$ |
| Riemann convention | G02: $`[\nabla_\mu,\nabla_\nu]X^\rho=R^\rho{}_{\sigma\mu\nu}X^\sigma`$; no curvature commutator is used here |
| Frames/connections | Full tangent-curvature laws R05/R06a already include the frame variation; do not add a second $`\delta e`$ |
| Antisymmetrization | $`A_{[a}B_{b]}=(A_aB_b-A_bB_a)/2`$; SU(2) parentheses also have weight $`1/2`$ |
| Clifford/duality | $`\{\gamma_a,\gamma_b\}=2\eta_{ab}`$; $`\gamma^{01234}=i`$; $`\epsilon^{01234}=+1`$ |
| Dot products | Full ordered sums, with no $`1/2`$: $`K=\gamma^{ab}T_{ab}`$, $`X^i=T^{ab}\mathscr R_{ab}^i`$ |
| SU(2) | $`z_i=z^j\varepsilon_{ji}`$, $`z^i=\varepsilon^{ij}z_j`$, $`\varepsilon_{12}=\varepsilon^{12}=1`$ |
| Mixed triplet | $`V^i{}_j=V^{ik}\varepsilon_{kj}`$; consequently $`V^{ij}\epsilon_j=-V^i{}_k\epsilon^k`$ |
| Bar | $`\bar z=z^T\mathsf C`$, $`\mathsf C^T=-\mathsf C`$; linear Majorana bar, so $`\overline{iz}=i\bar z`$ |
| Transposition | $`\widetilde M=\mathsf C^{-1}M^T\mathsf C`$; $`\widetilde{AB}=\widetilde B\widetilde A`$; ranks $`0,1,2,3,4`$ have signs $`+,+,-,-,+`$ |
| Odd spinors | $`\epsilon,\chi,\mathscr R,\mathscr S`$ are odd; $`T,D,\mathscr V,\mathscr C`$ even |
| Functional derivatives | None: this is a transformation of a composite, not an Euler variation |
| Coupling/order | Exact $`g=0`$; no $`\lambda_{\rm Weyl}`$ enters this map identity; later $`[\lambda_{\rm Weyl}]=-2`$ |

The supersymmetry doublet parameter and all suppressed spinor contractions
use the same NW–SE convention. They must not be interpreted as a sum of two
ordinary diagonal Dirac bilinears.

## 10. Definitions and Required Identities

### 10.1 Short names for complete covariants

```math
\begin{gathered}
\mathscr R_{ab}^i:=\widehat R_{ab}^i(Q),\quad
\mathscr V_{ab}^{ij}:=\widehat R_{ab}^{ij}(V),\quad
\mathscr C_{abcd}:=\widehat C_{abcd}=\widehat R_{ab\,cd}(M),\quad
\mathscr S_{ab}^i:=\widehat R_{ab}^i(S),\quad
K:=\gamma^{ab}T_{ab},\quad X^i:=T^{ab}\mathscr R_{ab}^i,\quad
T^2:=T_{ab}T^{ab},\quad
U_{a\,bc}:=\mathcal D_aT_{bc},\quad
J:=\gamma^a\mathcal D^bT_{ab},\quad
G_4:=\gamma^{abcd}T_{ab}T_{cd}.
\end{gathered}\tag{Q02}
```

The two-form $`T`$ is not a Clifford matrix: its components commute, while
$`K`$ acts on spinors. The symbol $`D`$ without a script is the Weyl auxiliary
scalar; $`\mathcal D`$ is the full covariant derivative G01/W04. In particular,
$`\mathcal D\mathscr R`$ is the derivative specified after R06b, including
its Q/S connections. The defining connections and supercovariant
completions remain R01–R03; the abbreviations in (Q02) do not remove them.

### 10.2 The input Q-laws, explicitly

From W03, with $`\eta=0`$,

```math
\begin{aligned}
\delta_Q T_{ab}
 &=\frac i2\bar\epsilon\gamma_{ab}\chi
   -\frac{3i}{32}\bar\epsilon\mathscr R_{ab},\\
\delta_Q\chi^i
 &=\frac14D\epsilon^i
  -\frac1{64}\gamma^{ab}\mathscr V_{ab}^{ij}\epsilon_j
  +\frac i8\gamma^{ab}\gamma^cU_{c\,ab}\epsilon^i
  -\frac i8\gamma^a\mathcal D^bT_{ab}\epsilon^i\\
 &\quad-\frac14G_4\epsilon^i+\frac16T^2\epsilon^i.
\end{aligned}\tag{Q03}
```

Write R05 in three Q-pieces:

```math
\begin{aligned}
\delta_Q\mathscr R_{ab}^i
 &=H_{ab}{}^{cd}\mathscr V_{cd}{}^i{}_k\epsilon^k
   +\frac14\mathscr C_{ab}{}^{cd}\gamma_{cd}\epsilon^i
   +2iP_{ab}\epsilon^i,\\
H_{ab}{}^{cd}
 &=\frac16\left(\gamma_{ab}{}^{cd}-\gamma^{cd}\gamma_{ab}
                          -\frac12\gamma_{ab}\gamma^{cd}\right),\\
P_{ab}
 &=(\mathcal D_{[a}K)\gamma_{b]}
   -\frac13\gamma_{[b}\mathcal D_{a]}K
   -\frac13\gamma_{[a}\gamma^c(\mathcal D_cK)\gamma_{b]}
   -\frac13\gamma_{ab}\gamma_d\mathcal D_cT^{cd}.
\end{aligned}\tag{Q04}
```

In the second term of $`P`$, the brackets mean
$`\gamma_{[b}\mathcal D_{a]}K=(\gamma_b\mathcal D_aK- \gamma_a\mathcal D_bK)/2`$. The derivative acts on $`T`$, not merely on
$`\gamma_b`$. Also $`\gamma_{ab}{}^{cd}`$ is a rank-four antisymmetric gamma.

From R06a,

```math
\begin{aligned}
\delta_Q\mathscr V_{ab}^{ij}
 &=-\frac{3i}{2}\bar\epsilon^{(i}\mathscr S_{ab}^{j)}
   -8\bar\epsilon^{(i}\gamma_{[a}\mathcal D_{b]}\chi^{j)}\\
 &\quad+i\bar\epsilon^{(i}K\mathscr R_{ab}^{j)}
   +8i\bar\epsilon^{(i}\gamma_{[a}K\gamma_{b]}\chi^{j)}.
\end{aligned}\tag{Q05}
```

The six-term eliminated S curvature, R06b, is

```math
\begin{aligned}
\mathscr S_{ab}^i
={}&-i\gamma^c\mathcal D_c\mathscr R_{ab}^i
-i\gamma_{[a}\mathcal D^c\mathscr R_{b]c}^i
-\frac83\gamma_{ab}X^i\\
&+12\gamma_dT^{cd}\gamma_{[a}\mathscr R_{b]c}^i
-3K\mathscr R_{ab}^i
-8T^c{}_{[a}\mathscr R_{b]c}^i.
\end{aligned}\tag{Q06}
```

This identity eliminates an S-curvature notation; it is not an auxiliary
field equation. In its last term the source really has $`T^c{}_a`$.
This is distinct from the index placement corrected in the **S-variation**
of $`\mathscr R`$ in Part I.

### 10.3 Spinor product rule and curvature identities

For odd $`u,v`$, retaining their order while transposing components,

```math
\bar u v=u_\alpha\mathsf C_{\alpha\beta}v_\beta
=-v_\beta\mathsf C_{\alpha\beta}u_\alpha
=-v_\alpha\mathsf C_{\beta\alpha}u_\beta
=\bar v u.
\tag{Q07}
```

The first minus exchanges two odd components; the second comes from
$`\mathsf C^T=-\mathsf C`$. For a bosonic matrix $`A`$,

```math
\overline{A\epsilon}=\bar\epsilon\widetilde A,qquad
\widetilde{\gamma_{ab}}=-\gamma_{ab},\qquad
\widetilde{\gamma^{ab}\gamma^c}=-\gamma^c\gamma^{ab}.
\tag{Q08}
```

No complex conjugation of $`i`$ occurs in (Q08). Part I proved, from the
conventional gamma trace, the identities needed here:

```math
\begin{gathered}
\gamma_a\mathscr R^{ab}=\gamma_b\mathscr R^{ab}=0,qquad
\gamma_{ab}\mathscr R^{ab}=0,\qquad
\gamma_{abcd}\mathscr R^{ab}=-2\mathscr R_{cd}.
\end{gathered}\tag{Q09}
```

The proofs are (S16)–(S27). Additional gamma reductions are derived at
exactly the steps where they enter below. No Fierz rearrangement of four
independent spinors is required: keeping complete covariants makes this
calculation bilinear in explicit odd objects, and every flip is (Q07) or
(Q08).

## 11. Detailed Derivation

### Step Q1 — Expose every product-rule term

<!-- ASSERT_CONVENTION: natural_units=hbar=c=1, metric_signature=(-,+,+,+,+); master C01, source_lock=UNG-WEYL2-OP58-CONVENTIONS-v4 -->

Apply the even variation before doing any spinor reordering:

```math
\begin{aligned}
\delta_Q L_R^{ij}
 &=\frac i4\left[(\delta_Q\bar{\mathscr R}_{ab}^{(i})\mathscr R^{j)ab}
          +\bar{\mathscr R}_{ab}^{(i}\delta_Q\mathscr R^{j)ab}\right],\\
\delta_Q L_\chi^{ij}
 &=\frac{256i}{3}\left[(\delta_Q\bar\chi^{(i})\chi^{j)}
                            +\bar\chi^{(i}\delta_Q\chi^{j)}\right],\\
\delta_Q L_{VT}^{ij}
 &=\frac{16}{3}\left[(\delta_Q\mathscr V_{ab}^{ij})T^{ab}
                            +\mathscr V_{ab}^{ij}\delta_QT^{ab}\right].
\end{aligned}\tag{Q10}
```

To reduce the second term in either fermion line, expand the parentheses
for an arbitrary odd $`z^i`$:

```math
\begin{aligned}
\bar z^{(i}\delta z^{j)}
 &=\frac12(\bar z^i\delta z^j+\bar z^j\delta z^i)\\
 &=\frac12(\overline{\delta z^j}z^i+\overline{\delta z^i}z^j)
 =\overline{\delta z}^{(i}z^{j)}.
\end{aligned}\tag{Q11}
```

Each middle equality uses (Q07), since $`\delta z`$ is still odd. Thus

```math
\delta_Q L_R^{ij}=\frac i2\overline{\delta_Q\mathscr R}_{ab}^{(i}\mathscr R^{j)ab},
\qquad
\delta_Q L_\chi^{ij}=\frac{512i}{3}\overline{\delta_Q\chi}^{(i}\chi^{j)}.
\tag{Q12}
```

An independent way to retain the two contributions is to put the parameter
left in the ordered Grassmann monomial. Its two coefficient matrices are

```math
\overline{A\epsilon}z:\ A^T\mathsf C,qquad
\bar z A\epsilon:\ -(\mathsf C A)^T
=-A^T\mathsf C^T=A^T\mathsf C.
\tag{Q13}
```

This is the product-rule check used in the verification script. Treating
$`\epsilon,z`$ as commuting test spinors would give the wrong second sign.

### Step Q2 — The $`\mathscr C\mathscr R`$ term from $`\delta L_R`$

<!-- ASSERT_CONVENTION: natural_units=hbar=c=1, metric_signature=(-,+,+,+,+); master C01, source_lock=UNG-WEYL2-OP58-CONVENTIONS-v4 -->

The Lorentz-curvature part of (Q04) has transpose

```math
\widetilde{\frac14\mathscr C_{ab}{}^{cd}\gamma_{cd}}
=-\frac14\mathscr C_{ab}{}^{cd}\gamma_{cd}.
\tag{Q14}
```

Insert this into (Q12), then raise the contracted tangent indices:

```math
\begin{aligned}
(\delta_Q L_R^{ij})_{\mathscr C}
 &=-\frac i8\bar\epsilon^{(i}\mathscr C_{ab}{}^{cd}\gamma_{cd}\mathscr R^{j)ab}\\
 &=i\bar\epsilon^{(i}
 \left[-\frac18\gamma_{cd}\mathscr R_{ab}^{j)}\mathscr C^{abcd}\right].
\end{aligned}\tag{Q15}
```

This gives printed term 1. The minus is the rank-two Majorana transpose,
not a Grassmann sign guessed from the final answer. Its spinor weight is
$`2+3/2=7/2`$.

### Step Q3 — The $`\mathscr V\mathscr R`$ term from $`\delta L_R`$

<!-- ASSERT_CONVENTION: natural_units=hbar=c=1, metric_signature=(-,+,+,+,+); master C01, source_lock=UNG-WEYL2-OP58-CONVENTIONS-v4 -->

Reverse the gamma products in $`H`$:

```math
\widetilde H_{ab}{}^{cd}
=\frac16\left(\gamma_{ab}{}^{cd}
-\gamma_{ab}\gamma^{cd}-\frac12\gamma^{cd}\gamma_{ab}\right).
\tag{Q16}
```

The rank-four gamma is even under the transpose; the two minus signs from
transposing two rank-two gammas cancel, leaving the product reversed.
We need three contractions. The first and third follow from (Q09):

```math
\gamma_{ab}{}^{cd}\mathscr R^{ab}=-2\mathscr R^{cd},\qquad
\gamma^{cd}\gamma_{ab}\mathscr R^{ab}=0.
\tag{Q17}
```

For the remaining order, first derive the commutator directly from
$`\gamma_b\gamma^{cd}=\gamma_b{}^{cd} +\delta_b^c\gamma^d-\delta_b^d\gamma^c`$ and its reversed order:

```math
[\gamma_b,\gamma^{cd}]
=2\delta_b^c\gamma^d-2\delta_b^d\gamma^c.
\tag{Q18}
```

Now move the rightmost gamma next to $`\mathscr R`$:

```math
\begin{aligned}
\gamma_{ab}\gamma^{cd}\mathscr R^{ab}
 &=\gamma_a\gamma_b\gamma^{cd}\mathscr R^{ab}\\
 &=\gamma_a\gamma^{cd}\gamma_b\mathscr R^{ab}
   +2\gamma_a\gamma^d\mathscr R^{ac}
   -2\gamma_a\gamma^c\mathscr R^{ad}\\
 &=2(2\delta_a^d-\gamma^d\gamma_a)\mathscr R^{ac}
   -2(2\delta_a^c-\gamma^c\gamma_a)\mathscr R^{ad}\\
 &=4\mathscr R^{dc}-4\mathscr R^{cd}=-8\mathscr R^{cd}.
\end{aligned}\tag{Q19}
```

The removed $`\eta_{ab}`$ term contracts an antisymmetric curvature to zero.
The zero terms on the other lines are precisely the gamma traces in (Q09).
Substitution into (Q16) gives

```math
\widetilde H_{ab}{}^{cd}\mathscr R^{ab}
=\frac16[-2-(-8)-0]\mathscr R^{cd}=\mathscr R^{cd}.
\tag{Q20}
```

Keep the SU(2) index of the parameter visible. Majorana transposition does
not transpose the SU(2) coefficient into a different contraction:

```math
\begin{aligned}
(\delta_Q L_R^{ij})_V
 &=\frac i2\mathscr V_{cd}{}^{(i}{}_k\,
                  \bar\epsilon^k\widetilde H_{ab}{}^{cd}\mathscr R^{j)ab}\\
 &=\frac i2\mathscr V_{ab}{}^{(i}{}_k\bar\epsilon^k\mathscr R^{j)ab}.
\end{aligned}\tag{Q21}
```

For later use define the three bilinears for any symmetric triplet
$`V^{ij}`$ and any odd doublet $`z^i`$:

```math
A^{ij}[V,z]:=V^{(i}{}_k\bar\epsilon^k z^{j)},\quad
B^{ij}[V,z]:=V^{ij}\bar\epsilon z,\quad
C^{ij}[V,z]:=\bar\epsilon^{(i}V^{j)}{}_kz^k.
\tag{Q22}
```

All Lorentz indices in their later use are contracted as displayed. Equation
(Q21) is $`iA[\mathscr V_{ab},\mathscr R^{ab}]/2`$. The conversion from $`A`$
to $`C`$ must wait for the $`\mathscr V\delta T`$ contribution; it cannot be
made on (Q21) alone.

### Step Q4 — The $`\mathcal DT\,\mathscr R`$ terms from $`\delta L_R`$

<!-- ASSERT_CONVENTION: natural_units=hbar=c=1, metric_signature=(-,+,+,+,+); master C01, source_lock=UNG-WEYL2-OP58-CONVENTIONS-v4 -->

The coefficient of $`i\bar\epsilon^{(i}`$ from the last part of (Q04) is
$`\tfrac12(2i)\widetilde P_{ab}\mathscr R^{j)ab} =i\widetilde P_{ab}\mathscr R^{j)ab}`$. Transpose **all four** terms before
contracting:

```math
\begin{aligned}
\widetilde P_{ab}
={}&-\gamma_{[b}\mathcal D_{a]}K
+\frac13(\mathcal D_{[a}K)\gamma_{b]}
+\frac13\gamma_{[b}(\mathcal D_cK)\gamma^c\gamma_{a]}\\
&+\frac13\gamma_d\gamma_{ab}\mathcal D_cT^{cd}.
\end{aligned}\tag{Q23}
```

For example, the third term starts with three factors
$`\gamma_a\gamma^c(\mathcal D_cK)\gamma_b`$; reversing their order and
$`\widetilde K=-K`$ supplies its plus sign. Weighted antisymmetrization
against $`\mathscr R^{ab}`$ removes the brackets with coefficient one.
The last three contractions vanish separately:

```math
\begin{aligned}
\tfrac13(\mathcal D_aK)\gamma_b\mathscr R^{ab}&=0,\\
\tfrac13\gamma_b(\mathcal D_cK)\gamma^c\gamma_a\mathscr R^{ab}&=0,\\
\tfrac13\gamma_d(\mathcal D_cT^{cd})\gamma_{ab}\mathscr R^{ab}&=0.
\end{aligned}\tag{Q24}
```

Their rightmost factors are respectively the second, first, and double
gamma traces in (Q09). The first contraction in (Q23) remains:

```math
\begin{aligned}
\widetilde P_{ab}\mathscr R^{ab}
 &=-\gamma_b\gamma^{cd}U_{a\,cd}\mathscr R^{ab}\\
 &=-\gamma^{cd}U_{a\,cd}\gamma_b\mathscr R^{ab}
   -2\gamma^dU_{a\,bd}\mathscr R^{ab}
   +2\gamma^cU_{a\,cb}\mathscr R^{ab}\\
 &=-2\gamma^dU_{a\,bd}\mathscr R^{ab}
   -2\gamma^cU_{a\,bc}\mathscr R^{ab}\\
 &=-4\gamma^cU_{a\,bc}\mathscr R^{ab}
 =-4\gamma_c\mathscr R_{ab}\mathcal D^aT^{bc}.
\end{aligned}\tag{Q25}
```

The second line uses (Q18); the third uses $`U_{a\,cb}=-U_{a\,bc}`$;
the fourth renames $`d\to c`$. Hence

```math
(\delta_Q L_R^{ij})_{\mathcal DT}
=i\bar\epsilon^{(i}
 \left[-4i\gamma_c\mathscr R_{ab}^{j)}\mathcal D^aT^{bc}\right].
\tag{Q26}
```

This is printed term 2, with spinor weight $`3/2+2=7/2`$.
The complete first-summand variation is now

```math
\delta_Q L_R^{ij}
=i\bar\epsilon^{(i}\left[-\frac18\gamma_{cd}\mathscr R_{ab}^{j)}\mathscr C^{abcd}
-4i\gamma_c\mathscr R_{ab}^{j)}\mathcal D^aT^{bc}\right]
+\frac i2A^{ij}[\mathscr V_{ab},\mathscr R^{ab}].
\tag{Q27}
```

### Step Q5 — Each of the six terms in $`\delta\chi`$

<!-- ASSERT_CONVENTION: natural_units=hbar=c=1, metric_signature=(-,+,+,+,+); master C01, source_lock=UNG-WEYL2-OP58-CONVENTIONS-v4 -->

Apply the factor $`512/3`$ in (Q12) to each transposed matrix in (Q03).
First convert the V term using the NW–SE rule:

```math
-\frac1{64}\gamma^{ab}\mathscr V_{ab}^{ij}\epsilon_j
=+\frac1{64}\gamma^{ab}\mathscr V_{ab}{}^i{}_k\epsilon^k,
\qquad
\widetilde{\gamma^{ab}}=-\gamma^{ab}.
\tag{Q28}
```

The six separate contributions, before combining derivative or $`T^2`$
structures with other summands, are

```math
\begin{array}{c|c|c}
\text{term in }\delta\chi & \text{transposed matrix coefficient}
 & \text{contribution to }\delta L_\chi\\ \hline
D\epsilon/4&D/4&i\bar\epsilon^{(i}(128D\chi^{j)}/3)\\
\gamma^{ab}\mathscr V_{ab}{}^i{}_k\epsilon^k/64
&-\gamma^{ab}\mathscr V_{ab}{}^i{}_k/64
&-(8i/3)A^{ij}[\mathscr V_{ab},\gamma^{ab}\chi]\\
i\gamma^{ab}\gamma^cU_{c\,ab}\epsilon/8
&-i\gamma^c\gamma^{ab}U_{c\,ab}/8
&i\bar\epsilon^{(i}[-(64i/3)\gamma^c\gamma^{ab}U_{c\,ab}\chi^{j)}]\\
-iJ\epsilon/8&-iJ/8&i\bar\epsilon^{(i}[-(64i/3)J\chi^{j)}]\\
-G_4\epsilon/4&-G_4/4&i\bar\epsilon^{(i}[-(128/3)G_4\chi^{j)}]\\
T^2\epsilon/6&T^2/6&i\bar\epsilon^{(i}[(256/9)T^2\chi^{j)}]
\end{array}\tag{Q29}
```

For clarity, the numerical products are
$`512/(3\cdot4)=128/3`$, $`512/(3\cdot64)=8/3`$,
$`512/(3\cdot8)=64/3`$ and $`512/(3\cdot6)=256/9`$.
The signs in the table are the transposes just listed, with the $`i`$'s
unchanged. The D term already gives printed term 3.

Reduce the two derivative terms without interchanging derivatives.
Define $`A_3:=\gamma^{abc}\mathcal D_aT_{bc}`$ only within this step.
The left product gives

```math
\begin{aligned}
\gamma^c\gamma^{ab}\mathcal D_cT_{ab}
 &=(\gamma^{cab}+\eta^{ca}\gamma^b-\eta^{cb}\gamma^a)
                                      \mathcal D_cT_{ab}\\
 &=A_3+\gamma^b\mathcal D^aT_{ab}
        -\gamma^a\mathcal D^bT_{ab}
 =A_3-2J.
\end{aligned}\tag{Q30}
```

The cyclic relabeling $`(c,a,b)\to(a,b,c)`$ has even parity. In the
penultimate line $`\gamma^b\mathcal D^aT_{ab}=-J`$ by exchanging $`a,b`$.
For the product appearing in M02,

```math
\begin{aligned}
\gamma^{ab}\gamma^c\mathcal D_aT_{bc}
 &=(\gamma^{abc}+\eta^{bc}\gamma^a-\eta^{ac}\gamma^b)
                                        \mathcal D_aT_{bc}\\
 &=A_3-\gamma^b\mathcal D^cT_{bc}=A_3-J.
\end{aligned}\tag{Q31}
```

The term with $`\eta^{bc}T_{bc}`$ is zero because the metric is symmetric
and $`T_{bc}`$ is antisymmetric. Equations (Q30)–(Q31) therefore imply

```math
\gamma^c\gamma^{ab}\mathcal D_cT_{ab}+J
=\gamma^{ab}\gamma^c\mathcal D_aT_{bc}.
\tag{Q32}
```

The second-summand result is

```math
\begin{aligned}
\delta_Q L_\chi^{ij}
={}&i\bar\epsilon^{(i}\left[
 \frac{128}{3}D\chi^{j)}
-\frac{64i}{3}\gamma^{ab}\gamma^c\mathcal D_aT_{bc}\chi^{j)}
-\frac{128}{3}G_4\chi^{j)}+\frac{256}{9}T^2\chi^{j)}\right]\\
&-\frac{8i}{3}A^{ij}[\mathscr V_{ab},\gamma^{ab}\chi].
\end{aligned}\tag{Q33}
```

The derivative term is printed term 6. Every term within the square
bracket has weight $`7/2`$.

### Step Q6 — Both factors of $`L_{VT}`$, and all six resulting terms

<!-- ASSERT_CONVENTION: natural_units=hbar=c=1, metric_signature=(-,+,+,+,+); master C01, source_lock=UNG-WEYL2-OP58-CONVENTIONS-v4 -->

Multiply every term in (Q05) by $`16T^{ab}/3`$. Since $`T`$ is even there is
no fermion exchange. For any $`Y_{ab}`$,
$`T^{ab}Y_{[ab]}=T^{ab}(Y_{ab}-Y_{ba})/2=T^{ab}Y_{ab}`$ after
$`a\leftrightarrow b`$ in the second term. Thus

```math
\begin{aligned}
\frac{16}{3}T^{ab}\delta_Q\mathscr V_{ab}^{ij}
=i\bar\epsilon^{(i}\bigg[
&-8T^{ab}\mathscr S_{ab}^{j)}
+\frac{128i}{3}T^{ab}\gamma_a\mathcal D_b\chi^{j)}\\
&+\frac{16}{3}KX^{j)}
+\frac{128}{3}T^{ab}\gamma_aK\gamma_b\chi^{j)}\bigg].
\end{aligned}\tag{Q34}
```

In the derivative term $`-128/3=i(128i/3)`$, which accounts for its $`i`$
inside the bracket. This is printed term 8. Keep the $`\mathscr S`$ term
until Step Q9; it has not vanished.

Now vary the other factor using both terms in $`\delta T`$:

```math
\begin{aligned}
\frac{16}{3}\mathscr V_{ab}^{ij}\delta_QT^{ab}
 &=\frac{8i}{3}\mathscr V_{ab}^{ij}\bar\epsilon\gamma^{ab}\chi
   -\frac i2\mathscr V_{ab}^{ij}\bar\epsilon\mathscr R^{ab}\\
 &=\frac{8i}{3}B^{ij}[\mathscr V_{ab},\gamma^{ab}\chi]
   -\frac i2B^{ij}[\mathscr V_{ab},\mathscr R^{ab}].
\end{aligned}\tag{Q35}
```

The coefficient of its second term is
$`(16/3)(-3i/32)=-i/2`$. Equations (Q34)–(Q35) contain the complete
variation of the third original summand.

### Step Q7 — Complete the two SU(2)-curvature sectors

<!-- ASSERT_CONVENTION: natural_units=hbar=c=1, metric_signature=(-,+,+,+,+); master C01, source_lock=UNG-WEYL2-OP58-CONVENTIONS-v4 -->

We must prove, with the present raising/lowering rule,

```math
A^{ij}[V,z]-B^{ij}[V,z]=C^{ij}[V,z].
\tag{Q36}
```

Set $`V^{11}=p`$, $`V^{12}=q`$, $`V^{22}=r`$ and write
$`e^i=\bar\epsilon^i`$ while retaining the order $`e^iz^j`$.
NW–SE lowering gives

```math
V^i{}_k=\begin{pmatrix}-q&p\\-r&q\end{pmatrix},\qquad
\bar\epsilon z=-e^1z^2+e^2z^1.
\tag{Q37}
```

Evaluate the three independent symmetric components:

```math
\begin{aligned}
A^{11}-B^{11}
 &=(-qe^1z^1+pe^2z^1)-p(-e^1z^2+e^2z^1)
 =-qe^1z^1+pe^1z^2=C^{11},\\
A^{22}-B^{22}
 &=(-re^1z^2+qe^2z^2)-r(-e^1z^2+e^2z^1)
 =-re^2z^1+qe^2z^2=C^{22},\\
A^{12}-B^{12}
 &=\tfrac12[-qe^1z^2+pe^2z^2-re^1z^1+qe^2z^1]
       -q(-e^1z^2+e^2z^1)\\
 &=\tfrac12[-re^1z^1+qe^1z^2-qe^2z^1+pe^2z^2]
 =C^{12}.
\end{aligned}\tag{Q38}
```

No spinors were interchanged in this component proof. Use it first for
$`z^{i\,ab}=\mathscr R^{i\,ab}`$, combining (Q21) and (Q35):

```math
\begin{aligned}
(\delta_Q L^{ij})_{V\mathscr R}
 &=\tfrac i2(A-B)^{ij}[\mathscr V_{ab},\mathscr R^{ab}]\\
 &=i\bar\epsilon^{(i}\left[
       \tfrac12\mathscr V^{ab\,j)}{}_k\mathscr R_{ab}^k\right].
\end{aligned}\tag{Q39}
```

For $`z^i=\gamma^{ab}\chi^i`$, combine (Q33) and (Q35):

```math
\begin{aligned}
(\delta_Q L^{ij})_{V\chi}
 &=-\tfrac{8i}{3}(A-B)^{ij}[\mathscr V_{ab},\gamma^{ab}\chi]\\
 &=i\bar\epsilon^{(i}\left[
       -\tfrac83\mathscr V^{ab\,j)}{}_k\gamma_{ab}\chi^k\right].
\end{aligned}\tag{Q40}
```

These are printed terms 10 and 11, each of weight $`2+3/2=7/2`$.

### Step Q8 — Reduce and combine the $`T^2\chi`$ terms

<!-- ASSERT_CONVENTION: natural_units=hbar=c=1, metric_signature=(-,+,+,+,+); master C01, source_lock=UNG-WEYL2-OP58-CONVENTIONS-v4 -->

The remaining gamma product from (Q34) is
$`F:=T^{ab}T_{cd}\gamma_a\gamma^{cd}\gamma_b`$.
Twice applying the Clifford rule gives the full decomposition

```math
\begin{aligned}
\gamma_a\gamma^{cd}\gamma_b
={}&\gamma_a{}^{cd}{}_b
+\eta_{ab}\gamma^{cd}
+\delta_b^d\gamma_a{}^c-\delta_b^c\gamma_a{}^d
+\delta_a^c\gamma^d{}_b-\delta_a^d\gamma^c{}_b\\
&+\delta_a^c\delta_b^d-\delta_a^d\delta_b^c.
\end{aligned}\tag{Q41}
```

Here $`\gamma_a{}^c`$ is the rank-two gamma with one raised index, not
$`\gamma_a\gamma^c`$. Contract each rank-two term explicitly:

```math
\begin{aligned}
T^{ab}T_{cd}\eta_{ab}\gamma^{cd}&=0,\\
T^{ab}T_{cd}\delta_b^d\gamma_a{}^c
 &=T^{ab}T_{cb}\gamma_a{}^c=0,\\
-T^{ab}T_{cd}\delta_b^c\gamma_a{}^d
 &=-T^{ab}T_{bd}\gamma_a{}^d=+T^{ab}T_{db}\gamma_a{}^d=0,\\
T^{ab}T_{cd}\delta_a^c\gamma^d{}_b
 &=T^{ab}T_{ad}\gamma^d{}_b=0,\\
-T^{ab}T_{cd}\delta_a^d\gamma^c{}_b
 &=-T^{ab}T_{ca}\gamma^c{}_b=+T^{ab}T_{ac}\gamma^c{}_b=0.
\end{aligned}\tag{Q42}
```

The first zero is $`\eta_{ab}T^{ab}=0`$. In each of the other four lines,
a symmetric tensor of the form $`T_a{}^cT_{bc}`$, with the appropriate
metrics raised, contracts an antisymmetric gamma in the two remaining
indices; exchanging those indices leaves the tensor unchanged and changes
the gamma sign. The rank-four and scalar terms are

```math
\begin{aligned}
T^{ab}T_{cd}\gamma_a{}^{cd}{}_b
 &=T_{ab}T_{cd}\gamma^{acdb}=G_4,\\
T^{ab}T_{cd}(\delta_a^c\delta_b^d-\delta_a^d\delta_b^c)
 &=T^{ab}T_{ab}-T^{ab}T_{ba}=2T^2.
\end{aligned}\tag{Q43}
```

Moving $`b`$ across $`c,d`$ in the first line is two exchanges, hence plus.
Consequently

```math
F=G_4+2T^2\mathbf1.
\tag{Q44}
```

Insert (Q44) into the $`T^2\chi`$ pieces of (Q33) and (Q34):

```math
\begin{aligned}
(\varphi_Q^i)_{T^2\chi}
 &=-\frac{128}{3}G_4\chi^i+\frac{256}{9}T^2\chi^i
       +\frac{128}{3}(G_4+2T^2)\chi^i\\
 &=\left(-\frac{128}{3}+\frac{128}{3}\right)G_4\chi^i
  +\left(\frac{256}{9}+\frac{256}{3}\right)T^2\chi^i
 =\frac{1024}{9}T^2\chi^i.
\end{aligned}\tag{Q45}
```

The rank-four matrix cancels exactly. This is printed term 7, of weight
$`2+3/2=7/2`$.

### Step Q9 — Contract every term in the eliminated S curvature

<!-- ASSERT_CONVENTION: natural_units=hbar=c=1, metric_signature=(-,+,+,+,+); master C01, source_lock=UNG-WEYL2-OP58-CONVENTIONS-v4 -->

The first two terms of (Q06), when multiplied by $`-8T^{ab}`$ in (Q34),
give directly

```math
\begin{aligned}
-8T^{ab}(-i\gamma^c\mathcal D_c\mathscr R_{ab}^i)
 &=8iT^{ab}\gamma_c\mathcal D^c\mathscr R_{ab}^i,\\
-8T^{ab}(-i\gamma_{[a}\mathcal D^c\mathscr R_{b]c}^i)
 &=8iT^{ab}\gamma_a\mathcal D^c\mathscr R_{bc}^i.
\end{aligned}\tag{Q46}
```

These are printed terms 4 and 5. The brackets disappear by the
antisymmetry argument preceding (Q34), with no derivative moved onto $`T`$.
In particular, $`T\mathcal D\mathscr R`$ is not replaced by
$`\mathcal D(T\mathscr R)`$.

The algebraic part needs two contractions:

```math
W^i:=T^{ab}T^c{}_a\mathscr R_{bc}^i,\qquad
Z^i:=T^{ab}T^{cd}\gamma_d\gamma_a\mathscr R_{bc}^i.
\tag{Q47}
```

For the first, $`M^{bc}:=T^{ab}T^c{}_a=-T^{ab}T_a{}^c`$ is symmetric.
This follows by writing $`M^{bc}=-\eta_{ad}T^{ab}T^{dc}`$ and exchanging
$`a,d`$ when $`b,c`$ are exchanged. Therefore

```math
W^i=\frac12(M^{bc}-M^{cb})\mathscr R_{bc}^i=0.
\tag{Q48}
```

To reduce $`Z`$, we need the four-index form of the gamma-trace constraint,
$`\gamma_{[ab}\mathscr R_{cd]}=0`$ (G03, W footnote5). Here is an explicit
five-dimensional derivation so its use does not hide an extra assumption.
C04c gives

```math
\gamma_{ab}=-\frac i{3!}\epsilon_{abfgh}\gamma^{fgh},\qquad
\epsilon^{eabcd}\gamma_{ab}=2i\gamma^{ecd}.
\tag{Q49}
```

For the second equality, put the contracted pair first in the upper
epsilon (two exchanges), then use
$`\epsilon^{abe cd}\epsilon_{abfgh} =-2!\,3!\,\delta^e{}_{[f}\delta^c{}_g\delta^d{}_{h]}`$.
The Lorentzian minus cancels the $`-i`$ in the first equality and $`2!/1=2`$.
Now the gamma trace implies

```math
\begin{aligned}
\gamma^{ecd}\mathscr R_{cd}
 &=\gamma^e\gamma^{cd}\mathscr R_{cd}
   -\eta^{ec}\gamma^d\mathscr R_{cd}
   +\eta^{ed}\gamma^c\mathscr R_{cd}=0,\\
\epsilon^{eabcd}\gamma_{[ab}\mathscr R_{cd]}
 &=\epsilon^{eabcd}\gamma_{ab}\mathscr R_{cd}
 =2i\gamma^{ecd}\mathscr R_{cd}=0.
\end{aligned}\tag{Q50}
```

The Hodge map from four-forms to one-forms is invertible for the
nondegenerate tangent metric. Thus $`\gamma_{[ab}\mathscr R_{cd]}=0`$.
Expanding its six distinct terms and multiplying by $`T^{ab}T^{cd}`$,

```math
\begin{aligned}
0=T^{ab}T^{cd}\big(&\gamma_{ab}\mathscr R_{cd}
+\gamma_{cd}\mathscr R_{ab}-\gamma_{ac}\mathscr R_{bd}
-\gamma_{bd}\mathscr R_{ac}\\
&+\gamma_{ad}\mathscr R_{bc}+\gamma_{bc}\mathscr R_{ad}\big).
\end{aligned}\tag{Q51}
```

This is six times the weighted antisymmetrization. Define temporarily
$`H:=T^{ab}T^{cd}\gamma_{ad}\mathscr R_{bc}`$.
The first two terms in (Q51) each give $`KX`$. The four remaining terms
are all $`H`$, as the following explicit relabelings show:

```math
\begin{aligned}
-T^{ab}T^{cd}\gamma_{ac}\mathscr R_{bd}
 &\xrightarrow{c\leftrightarrow d}
 -T^{ab}T^{dc}\gamma_{ad}\mathscr R_{bc}=H,\\
-T^{ab}T^{cd}\gamma_{bd}\mathscr R_{ac}
 &\xrightarrow{a\leftrightarrow b}
 -T^{ba}T^{cd}\gamma_{ad}\mathscr R_{bc}=H,\\
+T^{ab}T^{cd}\gamma_{ad}\mathscr R_{bc}&=H,\\
+T^{ab}T^{cd}\gamma_{bc}\mathscr R_{ad}
 &\xrightarrow{a\leftrightarrow b,\ c\leftrightarrow d}
 +T^{ba}T^{dc}\gamma_{ad}\mathscr R_{bc}=H.
\end{aligned}\tag{Q52}
```

Consequently $`2KX+4H=0`$. In $`Z`$, use
$`\gamma_d\gamma_a=\gamma_{da}+\eta_{da}=-\gamma_{ad}+\eta_{da}`$:

```math
\begin{aligned}
H&=-\frac12KX,\\
Z&=-H+T^{ab}T^{cd}\eta_{da}\mathscr R_{bc}
=-H+W=\frac12KX.
\end{aligned}\tag{Q53}
```

The last equality uses (Q48). This shows exactly where both the
five-dimensional Clifford algebra and the conventional gamma trace enter
this quadratic-$`T`$ reduction.

Now contract the **four** algebraic terms in (Q06), in their original
order. The antisymmetric brackets in the fourth and sixth terms again
contract with coefficient one:

```math
\begin{array}{c|c|c}
\text{term in }\mathscr S_{ab}&T^{ab}\text{ times that term}&\text{reduced value}\\ \hline
-\frac83\gamma_{ab}X&-\frac83KX&-\frac83KX\\
+12\gamma_dT^{cd}\gamma_{[a}\mathscr R_{b]c}&+12Z&+6KX\\
-3K\mathscr R_{ab}&-3KX&-3KX\\
-8T^c{}_{[a}\mathscr R_{b]c}&-8W&0
\end{array}\tag{Q54}
```

The sum is **not zero**:

```math
-\frac83KX+6KX-3KX
=\frac{-8+18-9}{3}KX=\frac13KX.
\tag{Q55}
```

Combining the derivative and algebraic parts yields

```math
T^{ab}\mathscr S_{ab}^i
=-iT^{ab}\gamma^c\mathcal D_c\mathscr R_{ab}^i
-iT^{ab}\gamma_a\mathcal D^c\mathscr R_{bc}^i
+\frac13KX^i.
\tag{Q56}
```

Equation (Q56) is the crucial derived contraction to carry forward.
The $`T^2\mathscr R`$ terms in the full variation come from two locations
in (Q34): $`-8T\mathscr S`$ and the explicit $`16KX/3`$. Thus

```math
\begin{aligned}
(\varphi_Q^i)_{T^2\mathscr R}
 &=-8\left(\frac13KX^i\right)+\frac{16}{3}KX^i\\
 &=\left(-\frac83+\frac{16}{3}\right)KX^i
 =\frac83\gamma_{ab}\mathscr R_{cd}^iT^{ab}T^{cd}.
\end{aligned}\tag{Q57}
```

This is the one coefficient which differs from printed term 9.
Dropping only the algebraic $`T\mathscr S`$ contraction would reproduce
the printed $`16/3`$, but (Q48)–(Q55) prohibit that step with these inputs.
This observation identifies an algebraic source of the discrepancy; it
does not assert how the authors obtained their printed expression.

### Step Q10 — Assemble the eleven structures without omissions

<!-- ASSERT_CONVENTION: natural_units=hbar=c=1, metric_signature=(-,+,+,+,+); master C01, source_lock=UNG-WEYL2-OP58-CONVENTIONS-v4 -->

The complete contributions are (Q27), (Q33), and (Q34)–(Q35).
Their reductions give the following coefficient ledger:

| # in M02 | Spinor structure | From $`\delta L_R`$ | From $`\delta L_\chi`$ | From $`\delta L_{VT}`$ and recoupling | Derived | Printed |
|---:|---|---:|---:|---:|---:|---:|
| 1 | $`\gamma_{cd}\mathscr R_{ab}\mathscr C^{abcd}`$ | $`-1/8`$ | 0 | 0 | $`-1/8`$ | $`-1/8`$ |
| 2 | $`i\gamma_c\mathscr R_{ab}\mathcal D^aT^{bc}`$ | $`-4`$ | 0 | 0 | $`-4`$ | $`-4`$ |
| 3 | $`D\chi`$ | 0 | $`128/3`$ | 0 | $`128/3`$ | $`128/3`$ |
| 4 | $`iT^{ab}\gamma_c\mathcal D^c\mathscr R_{ab}`$ | 0 | 0 | $`8`$ | $`8`$ | $`8`$ |
| 5 | $`iT^{ab}\gamma_a\mathcal D^c\mathscr R_{bc}`$ | 0 | 0 | $`8`$ | $`8`$ | $`8`$ |
| 6 | $`i\gamma^{ab}\gamma^c\mathcal D_aT_{bc}\chi`$ | 0 | $`-64/3`$ | 0 | $`-64/3`$ | $`-64/3`$ |
| 7 | $`T^2\chi`$ | 0 | $`256/9`$ | $`256/3`$ | $`1024/9`$ | $`1024/9`$ |
| 8 | $`iT^{ab}\gamma_a\mathcal D_b\chi`$ | 0 | 0 | $`128/3`$ | $`128/3`$ | $`128/3`$ |
| 9 | $`KX`$ | 0 | 0 | $`16/3-8/3`$ | **$`8/3`$** | **$`16/3`$** |
| 10 | $`\mathscr V^{ab\,i}{}_j\mathscr R_{ab}^j`$ | $`A/2`$ | 0 | $`-B/2`$ | $`C/2`$ | $`C/2`$ |
| 11 | $`\mathscr V^{ab\,i}{}_j\gamma_{ab}\chi^j`$ | 0 | $`-8A/3`$ | $`8B/3`$ | $`-8C/3`$ | $`-8C/3`$ |

In the last two rows $`A,B,C`$ denote the corresponding contractions
(Q22), not additional coefficients; the identity $`A-B=C`$ is (Q38).
The two $`G_4\chi`$ contributions, $`-128/3`$ and $`+128/3`$, cancel by (Q45)
and therefore do not create a twelfth surviving structure.

## 12. Consistency Checks

### 12.1 Weights, indices and covariance

Each term inside $`\varphi_Q`$ has Weyl weight $`7/2`$:

```math
\begin{aligned}
w(\mathscr C\mathscr R)&=2+\tfrac32=\tfrac72,
& w((\mathcal DT)\mathscr R)&=2+\tfrac32=\tfrac72,\\
w(D\chi)&=2+\tfrac32=\tfrac72,
& w(T\mathcal D\mathscr R)&=1+1+\tfrac32=\tfrac72,\\
w((\mathcal DT)\chi)&=2+\tfrac32=\tfrac72,
& w(T^2\chi)&=2+\tfrac32=\tfrac72,\\
w(T\mathcal D\chi)&=1+1+\tfrac32=\tfrac72,
& w(KX)&=1+(1+\tfrac32)=\tfrac72,\\
w(\mathscr V\mathscr R)&=2+\tfrac32=\tfrac72,
& w(\mathscr V\gamma\chi)&=2+\tfrac32=\tfrac72.
\end{aligned}\tag{Q58}
```

Consequently $`w(\bar\epsilon\varphi_Q)=-1/2+7/2=3=w(L)`$.
These are conformal engineering weights; no canonically normalized
Poincare mass assignment is being imported. The coupling does not enter.

In all eleven terms, every Lorentz index occurs twice, once raised and
once lowered after applying the constant tangent metric. Each term is an
odd Lorentz spinor with one free doublet index. Thus
$`i\bar\epsilon^{(i}\varphi_Q^{j)}`$ is an even symmetric triplet, exactly
as $`L^{ij}`$. The V-dependent pieces have this form only after the
explicit three-component proof (Q38). All factors are supercovariant and
all derivatives remain $`\mathcal D`$; no connection term has been removed.

Reality is inherited from the real triplet M01 and its source Q-laws:
(Q10) is its full variation, (Q07)–(Q08) use the Majorana bar, and all later
operations are identities in those conventions. In particular the
potentially dangerous replacement $`\overline{iA\epsilon}\to -i\bar\epsilon\widetilde A`$ was **not** made. A separate expansion into
all independent symplectic-Majorana components of all hatted quantities
has not been performed; it is not being claimed as an additional check.
There is no chirality projection in five dimensions.

### 12.2 Reproducible independent Clifford and SU(2) check

The companion script is
[verify_weyl_map_q_variation.py](../src/reference_checks/verify_weyl_map_q_variation.py).
Its concrete output is
[component check commands and output scope](../README.md).
Run it from the branch directory with

```bash
python3 -B computations/weyl_fermionic/checks/reference_suite.py --check verify_weyl_map_q_variation
```

It uses the explicit Lorentzian four-by-four matrices in the S-checker,
with $`\gamma^{01234}=i`$, $`\mathsf C=\gamma^2\gamma^4`$, and checks
ordered Grassmann monomial coefficients as in (Q13). It does not replace
odd spinors by commuting numbers in a bilinear identity.
The gamma-traceless basis is generated by

```math
q_b=\gamma^aB_{ab},\quad q=\gamma^bq_b,\qquad
\mathscr R_{ab}=12B_{ab}-4(\gamma_aq_b-\gamma_bq_a)+\gamma_{ab}q.
\tag{Q59}
```

All forty single-component two-form/spinor seeds are used. The output is
gamma-traceless, and (Q59) is $`12B`$ when $`B`$ is gamma-traceless; hence its
images span the full allowed spinor-two-form space. For quadratic $`T`$
identities the script uses ten unit two-forms and all forty-five distinct
pairwise sums. Polarization therefore tests every square and every mixed
coefficient, rather than relying on a random sample.

| Tested identity | Concrete coverage | Outcome |
|---|---|---|
| Both raw fermion product-rule terms | Rank0–4 matrix basis, ordered odd coefficients | PASS |
| Transposed V-curvature operator, (Q20) | $`10\times40`$ V/curvature inputs | PASS |
| All four $`P`$ terms, (Q23)–(Q25) | 50 derivative jets $`\times`$ 40 curvature images | PASS |
| The two derivative-$`\chi`$ terms, (Q32) | All 50 derivative jets and matrix entries | PASS |
| SU(2) recoupling, (Q38) | 3 triplet components and all parameter/spinor indices | PASS |
| $`F=G_4+2T^2`$ and $`1024/9`$, (Q44)–(Q45) | 55 quadratic-polarization tensors | PASS |
| $`W=0`$, $`2Z=KX`$, $`3T\mathscr S_{\rm alg}=KX`$ | 55 tensors $`\times`$ 40 curvature images | PASS |
| Coefficient of $`KX`$ | Source-law variation gives $`8/3`$ | PASS |
| Literal M02 matching | Difference is $`-8KX/3`$ | **FAIL** |
| Existing S-invariance regression | Existing finite-basis S assertions run on import | PASS |

The arithmetic is integer-scaled Gaussian-integer arithmetic, represented
exactly below $`2^{53}`$; no tolerance or coefficient fitting is used.
The script's overall PASS means that it reproduces this derivation,
**including its nonzero residual**. It does not mean that literal M02
passed Q-matching. The JSON records the latter separately as FAIL.

### 12.3 A nonzero residual, rather than a formal unmatched symbol

For an explicit complexified component test, take $`T_{01}=1`$ and all other
independent components zero. Let $`B_{01}=u_1=(1,0,0,0)^T`$ and form the
projected curvature (Q59); attach an odd generator to $`u_1`$ if tracking
Grassmann degree explicitly. The checker verifies every gamma trace.
Its values include

```math
\mathscr R_{01}=6u_1,\qquad
X=2T^{01}\mathscr R_{01}=-12u_1,\qquad
K=2\gamma^{01},\qquad
KX=(0,0,0,-24i)^T.
\tag{Q60}
```

Thus the difference between the derived and printed spinor in this sector
is

```math
-\frac83KX=(0,0,0,64i)^T\ne0.
\tag{Q61}
```

This is a coefficient test on the complexified curvature representation,
not a claim that these values specify a full supergravity solution.
Symplectic-Majorana reality can be restored by adjoining the conjugate
SU(2) partner; a nonzero complex-linear operator cannot vanish on its
entire real form. The example rules out an identically zero gamma-trace
or SU(2) reduction of the reported residual.

### 12.4 Limits and forbidden shortcuts tested

| Restriction on the final identity | Result | Meaning |
|---|---|---|
| $`T=0`$ identically, including $`\mathcal DT=0`$ | Only $`\mathscr C\mathscr R`$, $`D\chi`$, $`V\mathscr R`$, $`V\chi`$ remain; all four coefficients match M02 | The discrepancy is localized to the quadratic-$`T`$ curvature sector |
| $`\mathscr R=0`$ identically, including $`\mathcal D\mathscr R=0`$ | The $`D\chi`$, $`\mathcal DT\chi`$, $`T^2\chi`$, $`T\mathcal D\chi`$, $`V\chi`$ terms match | Independent check of all surviving $`\chi`$ sectors |
| All physical fermions set to zero after variation | $`\varphi_Q=0`$ and $`\delta_Q L=0`$ at first order in the odd parameter | This bosonic restriction cannot detect the discrepancy |
| $`\chi=0`$ as a covariant restriction | The residual $`-8KX/3`$ need not vanish | It cannot be removed by a $`\chi`$-only convention change |
| Ungauged limit | Already $`g=0`$ throughout; V-curvature contributions remain | No conformal SU(2) curvature has been discarded |

No integration by parts, EOM, derivative commutator or boundary term is
hidden in these checks. A constant value at a point is not being confused
with an identically zero covariant derivative; the first two rows state
both restrictions explicitly.

## 13. Final Result

Combining every term from the three original summands gives

```math
\boxed{\delta_Q L^{ij}=i\bar\epsilon^{(i}\varphi_Q^{j)}}.
\tag{Q62}
```

The spinor obtained from the locked source transformation laws is

```math
\boxed{\begin{aligned}
\varphi_Q^i={}&
-\frac18\gamma_{cd}\mathscr R_{ab}^i\mathscr C^{abcd}
-4i\gamma_c\mathscr R_{ab}^i\mathcal D^aT^{bc}
+\frac{128}{3}\chi^iD\\
&+8i\gamma_c\mathcal D^c\mathscr R_{ab}^iT^{ab}
+8i\gamma_a\mathcal D^c\mathscr R_{bc}^iT^{ab}
-\frac{64i}{3}\gamma^{ab}\gamma^c\mathcal D_aT_{bc}\chi^i\\
&+\frac{1024}{9}T^2\chi^i
+\frac{128i}{3}\gamma_a\mathcal D_b\chi^iT^{ab}
+\frac{8}{3}\gamma_{ab}\mathscr R_{cd}^iT^{ab}T^{cd}\\
&+\frac12\mathscr V^{ab\,i}{}_j\mathscr R_{ab}^j
-\frac83\mathscr V^{ab\,i}{}_j\gamma_{ab}\chi^j.
\end{aligned}}
\tag{Q63}
```

All hats are represented by (Q02); none have been stripped. Relative to
the printed M02 the precise local matching residual is

```math
\boxed{\begin{aligned}
\varphi_Q^i-\varphi_{\rm OP}^i&=-\frac83KX^i,\\
\Delta_Q^{ij}
:=\delta_Q L^{ij}-i\bar\epsilon^{(i}\varphi_{\rm OP}^{j)}
&=-\frac{8i}{3}\bar\epsilon^{(i}
       (\gamma^{ab}T_{ab})(T^{cd}\widehat R_{cd}^{j)}(Q)).
\end{aligned}}
\tag{Q64}
```

Lowering the two free SU(2) indices with the fixed epsilon tensors gives
$`\delta_Q L_{ij}`$ without an additional transformation of those tensors.
The result is exact relative to W03/R05/R06 and the conventional constraint;
it is not only a quadratic-fermion or on-shell calculation.

## 14. Convention Dependence and Remaining Uncertainties

**Established.** Every product-rule contribution to $`\delta_Q L`$ has been
evaluated. The eleven resulting structures are (Q63). Ten coefficients
match OP(5.8); its $`T^2\widehat R(Q)`$ coefficient does not. The algebraic
contraction (Q56), which explains the difference, is both hand-derived
and independently tested. Part I's S-invariance remains intact.

**Source audit of the discrepancy.** The location is OP(5.8), p.18,
third displayed line of its $`\varphi^i`$: the source prints $`+16KX/3`$.
W(3.23), PDF22, supplies $`-3i\bar\epsilon\mathscr S/2`$ in $`\delta\mathscr V`$
and $`+i\bar\epsilon K\mathscr R`$ in the same variation.
W(3.19), PDF21, supplies the four algebraic S-curvature terms whose
contraction is $`KX/3`$. These source pages were checked visually and match
(Q05)–(Q06). This is therefore not the same sort of extraction typo that
was repaired in Part I.

The following possible explanations have been tested or delimited:

- **Gamma/dot/bracket normalization:** the full contractions and weighted
  brackets are used throughout, and the ten matching terms plus the
  finite-basis checks fix these factors. Changing them only in term9
  would be an inconsistent convention change.
- **Lorentz index relabeling:** (Q48)–(Q53) explicitly retain all metric
  factors. The nonzero example (Q60)–(Q61) rules out a vanishing dummy-index
  or gamma-trace identity.
- **SU(2)/Grassmann signs:** (Q07), (Q13), and all three components in
  (Q38) were checked; the discrepant $`KX`$ term is already in the direct
  $`\bar\epsilon^{(i}z^{j)}`$ channel.
- **Different Weyl-curvature symbol:** OP's text immediately after (5.4)
  explicitly uses $`\widehat C`$ for $`\widehat R(M)`$, the identification
  already locked in R03. No extra $`T^2`$ shift is specified there.
- **Boundary representative, EOM, gauge, field redefinition or a bosonic
  restriction:** none is an allowed equivalence for the present off-shell
  local map. No supplied conversion has been found that authorizes one.
- **Physical fermion truncation:** the residual already contains one
  explicit curvature spinor on a nonzero $`T`$ background. Calling M02 a
  formula valid only at low explicit fermion order would not remove it.
- **Input curvature laws:** they have been transcribed and used exactly;
  their full independent reconstruction from the gauge-field definitions
  is not part of this calculation. A remaining source-interface error
  there is not excluded by an algebraic check of their consequences.

**Confidence and carry-forward rule.** The reduction to (Q63)–(Q64) has
high confidence for the locked input laws. Assigning a published erratum
to OP alone would require a further independent source-law audit or a
compatible transformation check of the resulting spinor. Accordingly,
M02 remains a literal source record; M07 records $`\varphi_Q`$ and the
failed literal comparison. Do not silently overwrite $`16/3`$, call the
printed map verified, or start solving the omitted E/N terms using an
unqualified choice of spinor. The next bounded calculation is to resolve
this interface, beginning with the S-law of $`\varphi_Q`$ and, if necessary,
an independent derivation of the relevant curvature identity.

The Q/S transformations of the spinor, the E/N fermions, the complete
density, the physical gauge fixing, and the spectrum remain unperformed.
No approximation error estimate is needed: this calculation made no
approximation. Its limitation is the explicitly identified source-law
interface and the unperformed descendant checks.

## 15. Working-result adoption — 2026-09-18

---

# Part III — Q-variation of the adopted composite spinor

## 16. Problem and Target

**Requested calculation:** vary every term of the adopted $`\varphi_W^i`$
(M08), retaining all fermions, frame terms, connection terms and derivative
terms. This part follows the user's explicit request for the Q-variation;
the previously proposed S-variation of this spinor is not assumed to have
been performed.

The result below is the **exact, uncollected variation**: eleven displayed
contributions, containing 94 terms at the outer substitution level, together
with explicit finite polynomials for the curvature and derivative variations
that occur in those terms. Repeated polynomials are named once and displayed
in full. A name is not an unknown variation or an omitted fermion remainder.
No unevaluated $`\delta\widehat C`$, $`\delta\phi_\mu`$, $`\delta f_\mu`$ or
$`\delta(\mathcal D X)`$ is left in the evaluated result. Ordinary derivatives
of the original fields and the local parameter are retained with their
specified order. Expanding every occurrence of a repeated polynomial into
one enormous line would repeat the same terms; it would not add terms.

Collecting this result into the irreducible linear-multiplet law and
extracting simplified $`E_a,N`$ is a further algebraic task. That matching is
**not assumed** in this calculation. In particular, no term is discarded
because it does not yet resemble $`N\epsilon`$ or $`\gamma^aE_a\epsilon`$.

**Assumptions P-A1–P-A7.**

1. Work in $`D=5`$ with eight supercharges and physical gauging $`g=0`$.
2. Use the Standard-Weyl covariants as the intermediate variables of M08;
   their full Dilaton-Weyl substitution is a later operation.
3. Work off shell and before any conformal or Poincare gauge fixing. No
   equation of motion, background equation, auxiliary elimination or field
   redefinition is permitted.
4. Keep all hatted quantities and complete connections. There is no
   truncation by explicit or implicit physical fermion degree.
5. Set the independent S- and K-parameters to zero, but **retain** the
   dependent S- and K-connections and their induced Q-variations.
6. $`\epsilon^i(x)`$ is an arbitrary odd local parameter and is held fixed
   under the single variation. The parameterized $`\delta_Q`$ is even.
7. All equalities are pointwise. No integration by parts, discarded total
   derivative, commuting of covariant derivatives or boundary condition is
   used. Ordinary coordinate partial derivatives commute on smooth fields.

## 17. Convention Ledger

<!-- ASSERT_CONVENTION: natural_units=hbar=c=1, metric_signature=(-,+,+,+,+); master C01, source_lock=UNG-WEYL2-OP58-CONVENTIONS-v5 -->

| Item | Convention used here |
|---|---|
| Signature/indices | $`\eta_{ab}=(-,+,+,+,+)`$; $`a,b,\mu,\nu=0,\ldots,4`$; $`i,j=1,2`$ |
| Lorentz curvature | G02: $`R_{\mu\nu}{}^{ab}=2\partial_{[\mu}\omega_{\nu]}{}^{ab}+2\omega_{[\mu}{}^{ac}\omega_{\nu]c}{}^b`$ |
| Ricci contraction | $`\mathcal R_{\mu\nu}=\widehat R'_{\mu\rho}{}^{ab}(M)e_b{}^\rho e_{\nu a}`$, R03 |
| Brackets | Weight $`1/2`$ on pairs; tangent metrics and epsilon tensors are constant |
| Clifford algebra | $`\{\gamma^a,\gamma^b\}=2\eta^{ab}`$; $`\gamma^{01234}=i`$; full dot contractions |
| Orientation | $`\epsilon^{01234}=+1`$, $`\epsilon_{01234}=-1`$ |
| Bar | $`\bar z=z^T\mathsf C`$, $`\mathsf C^T=-\mathsf C`$; $`\overline{iz}=i\bar z`$ |
| Matrix transpose | $`\widetilde A=\mathsf C^{-1}A^T\mathsf C`$; $`\widetilde{AB}=\widetilde B\widetilde A`$; rank 2 has minus sign |
| SU(2) | $`z_i=z^j\varepsilon_{ji}`$; $`V^i{}_j=V^{ik}\varepsilon_{kj}`$; $`\varepsilon_{12}=\varepsilon^{12}=1`$ |
| Fermions | $`\epsilon,\psi_\mu,\phi_\mu,\chi,\mathscr R`$ are odd; $`\delta_Q`$ is even |
| Derivatives | Full $`\mathcal D`$ is G01; a separately identified $`\nabla^{\rm B}`$ below contains only bosonic connections |
| Formalism | $`\omega,\phi_\mu,f_\mu`$ are dependent connections; their defining variations are retained |
| Action/coupling | No action is varied here; $`\lambda_{\rm Weyl}`$ does not enter this multiplet identity |
| Functional derivatives | None; no left/right Euler derivative is being taken |

The v4-to-v5 change is only the adoption of the already derived spinor.
All W/G/R inputs used in Parts I–II are unchanged. The compatibility is established by the Part II coefficient comparison
and [its Q-variation checker](../src/reference_checks/verify_weyl_map_q_variation.py). Fourier transforms, quantum
ordering, renormalization and state normalization do not enter this classical
local identity.

## 18. Definitions and Required Identities

### 18.1 The eleven terms and derivative variables

Use the full covariants

```math
\begin{gathered}
\mathscr R_{ab}^i=\widehat R_{ab}^i(Q),\quad
\mathscr V_{ab}^{ij}=\widehat R_{ab}^{ij}(V),\quad
\mathscr C_{abcd}=\widehat C_{abcd},\\
K=\gamma^{ab}T_{ab},\quad t_2=T_{ab}T^{ab},\quad
G_4=\gamma^{abcd}T_{ab}T_{cd},\quad X^i=T^{ab}\mathscr R_{ab}^i,\\
U_{a\,bc}=\mathcal D_aT_{bc},\quad
Z_a^i=\mathcal D_a\chi^i,\quad
Y_{a\,bc}^i=\mathcal D_a\mathscr R_{bc}^i.
\end{gathered}\tag{P01}
```

These are abbreviations for complete fields and derivatives, not independent
extra fields. The starting spinor is

```math
\begin{aligned}
\varphi_W^i=\sum_{n=1}^{11}F_n^i,\qquad
F_1^i&=-\frac18\gamma_{cd}\mathscr R_{ab}^i\mathscr C^{abcd},\\
F_2^i&=-4i\gamma_c\mathscr R_{ab}^iU^{a\,bc},\\
F_3^i&=\frac{128}{3}\chi^iD,\\
F_4^i&=8i\gamma_cY^{c}{}_{ab}^iT^{ab},\\
F_5^i&=8i\gamma_aY^{c}{}_{bc}^iT^{ab},\\
F_6^i&=-\frac{64i}{3}\gamma^{ab}\gamma^cU_{a\,bc}\chi^i,\\
F_7^i&=\frac{1024}{9}t_2\chi^i,\\
F_8^i&=\frac{128i}{3}\gamma_aZ_b^iT^{ab},\\
F_9^i&=\frac83\gamma_{ab}\mathscr R_{cd}^iT^{ab}T^{cd},\\
F_{10}^i&=\frac12\mathscr V^{ab\,i}{}_j\mathscr R_{ab}^j,\\
F_{11}^i&=-\frac83\mathscr V^{ab\,i}{}_j\gamma_{ab}\chi^j.
\end{aligned}\tag{P02}
```

In particular, the coefficient in $`F_9`$ is the adopted $`8/3`$.
The five derivative-containing terms are $`F_2,F_4,F_5,F_6,F_8`$.

### 18.2 What the variation does to a product

For ordered factors, including odd spinors,

```math
\delta_Q(AB)=(\delta_QA)B+A(\delta_QB),\qquad
\delta_Q(ABC)=(\delta_QA)BC+A(\delta_QB)C+AB(\delta_QC).
\tag{P03}
```

There is no extra graded sign because $`\delta_Q`$ is even. Below we retain
this order. A bilinear such as $`\bar\epsilon\gamma_{ab}\chi`$ is even, so
moving the **whole bilinear** past a spinor is allowed without a sign.
Moving one of its odd factors by itself would require a sign and is not
being done. For a bar,

```math
\delta_Q\bar z=(\delta_Qz)^T\mathsf C,\qquad
\overline{A z}=\bar z\widetilde A
\quad\text{for a Grassmann-even matrix }A.
\tag{P04}
```

For example $`\widetilde{K\gamma_\mu}=-\gamma_\mu K`$.
The $`i`$ multiplying a spinor does not conjugate. There are no four-spinor
Fierz reductions in the uncollected answer; the original spinor pairing
and all resulting higher-fermion terms remain visible.

### 18.3 Bosonic connection derivative used in the expansion

For a weight-$`w`$ doublet with two lower tangent indices, define

```math
\begin{aligned}
\nabla^{\rm B}_\mu A_{bc}^i
={}&\partial_\mu A_{bc}^i-wb_\mu A_{bc}^i
+\frac14\omega_\mu{}^{de}\gamma_{de}A_{bc}^i
-V_\mu{}^{ij}A_{bc\,j}\\
&+\omega_{\mu b}{}^d A_{dc}^i+\omega_{\mu c}{}^d A_{bd}^i.
\end{aligned}\tag{P05}
```

Delete the unused spinor, SU(2), or tensor-index connections for a field
without those indices. Add one such Lorentz term for each extra lower
index, with the opposite induced action for an upper index. In particular
$`\nabla^{\rm B}`$ is metric/gamma compatible and obeys Leibniz. The weights
are $`w(\epsilon)=-1/2`$, $`w(T)=1`$, $`w(\chi)=w(\mathscr R)=3/2`$,
$`w(U)=w(D)=w(\mathscr V)=w(\mathscr C)=2`$.
For a triplet use the induced connection on each SU(2) index; in mixed
notation it is explicitly

```math
\begin{aligned}
\nabla^{\rm B}_\mu\mathscr V_{ab}{}^i{}_j
={}&\partial_\mu\mathscr V_{ab}{}^i{}_j-2b_\mu\mathscr V_{ab}{}^i{}_j
+\omega_{\mu a}{}^c\mathscr V_{cb}{}^i{}_j
+\omega_{\mu b}{}^c\mathscr V_{ac}{}^i{}_j\\
&+V_\mu{}^i{}_k\mathscr V_{ab}{}^k{}_j
-\mathscr V_{ab}{}^i{}_k V_\mu{}^k{}_j.
\end{aligned}\tag{P05a}
```

The corresponding two-upper expression follows by the constant epsilon
tensor conversion; no new connection convention is introduced.
This definition fixes every occurrence of $`\nabla^{\rm B}`$ below; it is
not the full $`\mathcal D`$.

## 19. Detailed Derivation

### Step P1 — Frames and the elementary gauge-field variations

<!-- ASSERT_CONVENTION: natural_units=hbar=c=1, metric_signature=(-,+,+,+,+); master C01, source_lock=UNG-WEYL2-OP58-CONVENTIONS-v5 -->

Introduce the following explicitly evaluated polynomials from W01:

```math
\begin{aligned}
h_\mu{}^a&=\frac12\bar\epsilon\gamma^a\psi_\mu,
&h_a{}^b&=e_a{}^\mu h_\mu{}^b,
&k_a{}^\mu&=-h_a{}^b e_b{}^\mu,\\
p_\mu^i&=\partial_\mu\epsilon^i+\frac12b_\mu\epsilon^i
+\frac14\omega_\mu{}^{ab}\gamma_{ab}\epsilon^i
-V_\mu{}^{ij}\epsilon_j+iK\gamma_\mu\epsilon^i,\\
\beta_\mu&=\frac i2\bar\epsilon\phi_\mu
-2\bar\epsilon\gamma_\mu\chi,\\
v_\mu^{ij}&=-\frac{3i}{2}\bar\epsilon^{(i}\phi_\mu^{j)}
+4\bar\epsilon^{(i}\gamma_\mu\chi^{j)}
+i\bar\epsilon^{(i}K\psi_\mu^{j)}.
\end{aligned}\tag{P06}
```

They are respectively $`\delta e_\mu{}^a`$, $`\delta e_a{}^\mu`$,
$`\delta\psi_\mu`$, $`\delta b_\mu`$ and $`\delta V_\mu`$; those descriptions
are not their definitions in the final expression—the displayed right
sides are. Differentiating the inverse and metric identities gives

```math
\begin{aligned}
0&=\delta(e_a{}^\mu e_\mu{}^b)
=k_a{}^\mu e_\mu{}^b+e_a{}^\mu h_\mu{}^b,\\
s_{\mu\nu}:=\delta g_{\mu\nu}
&=h_\mu{}^a e_{\nu a}+e_{\mu a}h_\nu{}^a,
&\delta g^{\mu\nu}&=-s^{\mu\nu},\\
\delta e&=e h_a{}^a,
&\delta\gamma_\mu&=h_\mu{}^a\gamma_a,
&\delta\gamma^a&=0.
\end{aligned}\tag{P07}
```

Here $`s^{\mu\nu}=g^{\mu\rho}g^{\nu\sigma}s_{\rho\sigma}`$; $`k^{\mu a}`$
means $`\eta^{ab}k_b{}^\mu`$. There is no volume density in M08, so
$`\delta e`$ creates no term in $`\delta\varphi_W`$.

Taking the Majorana transpose of every term in $`p_\mu`$ gives the row spinor
needed in the connection polynomials:

```math
\bar p_\mu^i=\partial_\mu\bar\epsilon^i+\frac12b_\mu\bar\epsilon^i
-\frac14\omega_\mu{}^{ab}\bar\epsilon^i\gamma_{ab}
-V_\mu{}^{ij}\bar\epsilon_j-i\bar\epsilon^i\gamma_\mu K.
\tag{P08}
```

The two minus signs in its gamma terms come from transposing rank2 and
$`K\gamma_\mu`$, respectively, not from complex conjugation.

### Step P2 — Matter and gravitino-curvature polynomials

<!-- ASSERT_CONVENTION: natural_units=hbar=c=1, metric_signature=(-,+,+,+,+); master C01, source_lock=UNG-WEYL2-OP58-CONVENTIONS-v5 -->

W03 gives the following complete polynomials:

```math
\begin{aligned}
\tau_{ab}&=\frac i2\bar\epsilon\gamma_{ab}\chi
-\frac{3i}{32}\bar\epsilon\mathscr R_{ab},\\
\kappa&=\gamma^{ab}\tau_{ab},\\
\theta&=iT^{ab}\bar\epsilon\gamma_{ab}\chi
-\frac{3i}{16}T^{ab}\bar\epsilon\mathscr R_{ab},\\
\xi^i&=\frac14D\epsilon^i
-\frac1{64}\gamma^{ab}\mathscr V_{ab}^{ij}\epsilon_j
+\frac i8\gamma^{ab}\gamma^cU_{c\,ab}\epsilon^i
-\frac i8\gamma^aU^b{}_{ab}\epsilon^i
-\frac14G_4\epsilon^i+\frac16t_2\epsilon^i,\\
d&=\bar\epsilon\gamma^aZ_a-\frac{5i}{3}\bar\epsilon K\chi.
\end{aligned}\tag{P09}
```

These are the evaluated variations of $`T_{ab},K,t_2,\chi^i,D`$.
The scalar factors in $`\theta`$ follow by varying **both** T factors:

```math
\delta(T_{ab}T^{ab})=\tau_{ab}T^{ab}+T_{ab}\tau^{ab}
=2T^{ab}\tau_{ab}=\theta.
\tag{P10}
```

All metrics in this equality are tangent metrics and hence have zero
variation. The factors of two in $`\theta`$ are required.

It is useful to define three **explicit linear maps**, for any two-form
$`t_{ab}`$ or derivative-shaped tensor $`u_{a\,bc}`$:

```math
\begin{aligned}
H_{ab}{}^{cd}&=\frac16\gamma_{ab}{}^{cd}
-\frac16\gamma^{cd}\gamma_{ab}-\frac1{12}\gamma_{ab}\gamma^{cd},\\
P_{ab}[u]&=\gamma^{cd}u_{[a\,cd}\gamma_{b]}
-\frac13\gamma_{[b}\gamma^{cd}u_{a]\,cd}
-\frac13\gamma_{[a}\gamma^f\gamma^{cd}u_{f\,cd}\gamma_{b]}
-\frac13\gamma_{ab}\gamma_d\eta^{ce}\eta^{df}u_{c\,ef},\\
A_{ab}[t]&=-8t_{ab}\mathbf1
+\frac{16}{3}t_{[a}{}^c\gamma_{b]c}
+\frac43\gamma_{abcd}t^{cd}.
\end{aligned}\tag{P11}
```

The fully evaluated Q-variation of the tangent gravitino curvature is

```math
\begin{aligned}
\rho_{ab}^i={}&
\frac16\gamma_{ab}{}^{cd}\mathscr V_{cd}{}^i{}_j\epsilon^j
-\frac16\gamma^{cd}\gamma_{ab}\mathscr V_{cd}{}^i{}_j\epsilon^j
-\frac1{12}\gamma_{ab}\gamma^{cd}\mathscr V_{cd}{}^i{}_j\epsilon^j\\
&+\frac14\mathscr C_{ab}{}^{cd}\gamma_{cd}\epsilon^i
+2i\gamma^{cd}U_{[a\,cd}\gamma_{b]}\epsilon^i
-\frac{2i}{3}\gamma_{[b}\gamma^{cd}U_{a]\,cd}\epsilon^i\\
&-\frac{2i}{3}\gamma_{[a}\gamma^f\gamma^{cd}U_{f\,cd}\gamma_{b]}\epsilon^i
-\frac{2i}{3}\gamma_{ab}\gamma_d\eta^{ce}\eta^{df}U_{c\,ef}\epsilon^i.
\end{aligned}\tag{P12}
```

Equivalently $`\rho=H\mathscr V\epsilon+\mathscr C\gamma\epsilon/4+ 2iP[U]\epsilon`$, but (P12) displays its eight terms. R05 is already a
tangent variation. Adding extra $`h_a{}^b\mathscr R`$ terms here would
count the frame variation twice.

### Step P3 — Expand all S-curvature contributions to $`\delta\mathscr V`$

<!-- ASSERT_CONVENTION: natural_units=hbar=c=1, metric_signature=(-,+,+,+,+); master C01, source_lock=UNG-WEYL2-OP58-CONVENTIONS-v5 -->

R06b supplies all six terms

```math
\mathscr S_{ab}^i=-i\gamma^cY_{c\,ab}^i
-i\gamma_{[a}Y^c{}_{b]c}^i
-\frac83\gamma_{ab}X^i
+12\gamma_dT^{cd}\gamma_{[a}\mathscr R_{b]c}^i
-3K\mathscr R_{ab}^i-8T^c{}_{[a}\mathscr R_{b]c}^i.
\tag{P13}
```

Define nine displayed bilinear structures; the fifth and eighth deliberately
have the same algebraic form, because they have different origins in R06:

```math
\begin{aligned}
B_{1,ab}^{ij}&=\bar\epsilon^{(i}\gamma^cY_{c\,ab}^{j)},&
B_{2,ab}^{ij}&=\bar\epsilon^{(i}\gamma_{[a}Y^c{}_{b]c}^{j)},\\
B_{3,ab}^{ij}&=\bar\epsilon^{(i}\gamma_{ab}X^{j)},&
B_{4,ab}^{ij}&=\bar\epsilon^{(i}\gamma_dT^{cd}\gamma_{[a}\mathscr R_{b]c}^{j)},\\
B_{5,ab}^{ij}&=\bar\epsilon^{(i}K\mathscr R_{ab}^{j)},&
B_{6,ab}^{ij}&=\bar\epsilon^{(i}T^c{}_{[a}\mathscr R_{b]c}^{j)},\\
B_{7,ab}^{ij}&=\bar\epsilon^{(i}\gamma_{[a}Z_{b]}^{j)},&
B_{8,ab}^{ij}&=\bar\epsilon^{(i}K\mathscr R_{ab}^{j)},\\
B_{9,ab}^{ij}&=\bar\epsilon^{(i}\gamma_{[a}K\gamma_{b]}\chi^{j)}.
\end{aligned}\tag{P14}
```

All have weight 2 and even parity. Each symmetric spinor bilinear denotes
$`\bar\epsilon^{(i}M z^{j)}=(\bar\epsilon^iMz^j+ \bar\epsilon^jMz^i)/2`$. With no rearrangement of odd factors, R06a becomes

```math
\nu_{ab}^{ij}
=-\frac32B_{1,ab}^{ij}-\frac32B_{2,ab}^{ij}
+4iB_{3,ab}^{ij}-18iB_{4,ab}^{ij}
+\frac{9i}{2}B_{5,ab}^{ij}+12iB_{6,ab}^{ij}
-8B_{7,ab}^{ij}+iB_{8,ab}^{ij}+8iB_{9,ab}^{ij}.
\tag{P15}
```

For example $`(-3i/2)(-i)=-3/2`$, $`(-3i/2)(-8/3)=4i`$,
and $`(-3i/2)(12)=-18i`$. Thus even the algebraic pieces of the S curvature
are present, including the pieces responsible for the earlier coefficient
discrepancy. A mixed index means
$`\nu_{ab}{}^i{}_j=\nu_{ab}^{ik}\varepsilon_{kj}`$; no extra guessed sign
is inserted.

### Step P4 — Full dependent S-connection variation

<!-- ASSERT_CONVENTION: natural_units=hbar=c=1, metric_signature=(-,+,+,+,+); master C01, source_lock=UNG-WEYL2-OP58-CONVENTIONS-v5 -->

First the complete spin-connection response is R04a at $`\eta=\Lambda_K=0`$:

```math
\Omega_\mu{}^{ab}=
\frac i2\bar\epsilon\gamma^{ab}\phi_\mu
-i\bar\epsilon\gamma^{[a}K\gamma^{b]}\psi_\mu
-\frac12\bar\epsilon\gamma^{[a}\mathscr R_\mu{}^{b]}
-\frac14\bar\epsilon\gamma_\mu\mathscr R^{ab}
-4e_\mu{}^{[a}\bar\epsilon\gamma^{b]}\chi,
\quad \mathscr R_\mu{}^a=e_\mu{}^b\mathscr R_b{}^a.
\tag{P16}
```

To calculate $`\delta\phi_\mu`$, use its **defining expression**, not just
the source's M-dependent correction. Denote $`q'_{\mu\nu}= \widehat R'_{\mu\nu}(Q)`$, whose full definition is

```math
q'_{\mu\nu}{}^i=2\partial_{[\mu}\psi_{\nu]}^i
+\frac12\omega_{[\mu}{}^{ab}\gamma_{ab}\psi_{\nu]}^i
+b_{[\mu}\psi_{\nu]}^i-2V_{[\mu}^{ij}\psi_{\nu]j}
+2iK\gamma_{[\mu}\psi_{\nu]}^i.
\tag{P17}
```

Varying its five terms produces all ten contributions

```math
\begin{aligned}
a_{\mu\nu}^i={}&2\partial_{[\mu}p_{\nu]}^i
+\frac12\Omega_{[\mu}{}^{ab}\gamma_{ab}\psi_{\nu]}^i
+\frac12\omega_{[\mu}{}^{ab}\gamma_{ab}p_{\nu]}^i
+\beta_{[\mu}\psi_{\nu]}^i+b_{[\mu}p_{\nu]}^i\\
&-2v_{[\mu}^{ij}\psi_{\nu]j}-2V_{[\mu}^{ij}p_{\nu]j}
+2i\kappa\gamma_{[\mu}\psi_{\nu]}^i
+2iK h_{[\mu}{}^a\gamma_a\psi_{\nu]}^i
+2iK\gamma_{[\mu}p_{\nu]}^i.
\end{aligned}\tag{P18}
```

The first entry in (P18) contains no unevaluated variation. Expanding the
explicit polynomial $`p_\mu`$ makes all its local-parameter derivatives
visible:

```math
\begin{aligned}
2\partial_{[\mu}p_{\nu]}^i={}&
(\partial_{[\mu}b_{\nu]})\epsilon^i+b_{[\nu}\partial_{\mu]}\epsilon^i
+\frac12(\partial_{[\mu}\omega_{\nu]}{}^{ab})\gamma_{ab}\epsilon^i
+\frac12\omega_{[\nu}{}^{ab}\gamma_{ab}\partial_{\mu]}\epsilon^i\\
&-2(\partial_{[\mu}V_{\nu]}^{ij})\epsilon_j
-2V_{[\nu}^{ij}\partial_{\mu]}\epsilon_j
+2i\gamma^{ab}(\partial_{[\mu}T_{ab})\gamma_{\nu]}\epsilon^i\\
&+2iK(\partial_{[\mu}e_{\nu]}{}^a)\gamma_a\epsilon^i
+2iK\gamma_{[\nu}\partial_{\mu]}\epsilon^i.
\end{aligned}\tag{P19}
```

The absent second-parameter-derivative is exactly
$`2\partial_{[\mu}\partial_{\nu]}\epsilon=0`$; this uses commuting
coordinate partials, not commuting covariant derivatives.

Convert the indices of this **primed** curvature with their frame terms:

```math
\begin{aligned}
a_{\mu a}^i&=e_a{}^\nu a_{\mu\nu}^i+k_a{}^\nu q'_{\mu\nu}{}^i,\\
a_{ab}^i&=e_a{}^\mu e_b{}^\nu a_{\mu\nu}^i
+k_a{}^\mu e_b{}^\nu q'_{\mu\nu}{}^i
+e_a{}^\mu k_b{}^\nu q'_{\mu\nu}{}^i.
\end{aligned}\tag{P20}
```

The dependent S-connection response is therefore the following six-term
expression after substituting both lines of (P20):

```math
\begin{aligned}
\Phi_\mu^i={}&
\frac i3\gamma^a e_a{}^\nu a_{\mu\nu}^i
+\frac i3\gamma^a k_a{}^\nu q'_{\mu\nu}{}^i
-\frac i{24}h_\mu{}^c\gamma_c\gamma^{ab}q'_{ab}{}^i\\
&-\frac i{24}\gamma_\mu\gamma^{ab}e_a{}^\rho e_b{}^\sigma a_{\rho\sigma}^i
-\frac i{24}\gamma_\mu\gamma^{ab}k_a{}^\rho e_b{}^\sigma q'_{\rho\sigma}{}^i
-\frac i{24}\gamma_\mu\gamma^{ab}e_a{}^\rho k_b{}^\sigma q'_{\rho\sigma}{}^i.
\end{aligned}\tag{P21}
```

No $`\delta\phi`$ appears on its right. $`\Omega`$ contains the original
$`\phi`$, but not its variation, so this substitution is finite.
For the bar needed below it is convenient to use (P20):

```math
\bar\Phi_\mu^i=
\frac i3\bar a_{\mu a}^i\gamma^a
+\frac i{24}\bar q'_{ab}{}^i\gamma^{ab}h_\mu{}^c\gamma_c
+\frac i{24}\bar a_{ab}^i\gamma^{ab}\gamma_\mu.
\tag{P22}
```

The last two signs follow from
$`\widetilde{\gamma_\mu\gamma^{ab}}=-\gamma^{ab}\gamma_\mu`$.
For complete spinor-order bookkeeping the bar of (P18) is

```math
\begin{aligned}
\bar a_{\mu\nu}^i={}&2\partial_{[\mu}\bar p_{\nu]}^i
-\frac12\Omega_{[\mu}{}^{ab}\bar\psi_{\nu]}^i\gamma_{ab}
-\frac12\omega_{[\mu}{}^{ab}\bar p_{\nu]}^i\gamma_{ab}
+\beta_{[\mu}\bar\psi_{\nu]}^i+b_{[\mu}\bar p_{\nu]}^i\\
&-2v_{[\mu}^{ij}\bar\psi_{\nu]j}-2V_{[\mu}^{ij}\bar p_{\nu]j}
+2i\bar\psi_{[\mu}^i\gamma_{\nu]}\kappa
+2i\bar\psi_{[\mu}^i h_{\nu]}{}^a\gamma_a K
+2i\bar p_{[\mu}^i\gamma_{\nu]}K.
\end{aligned}\tag{P23}
```

For its last three terms transposition first gives a minus and reverses
the two gamma factors; exchanging the antisymmetrized world labels gives
the displayed plus. No two odd spinors were interchanged.

### Step P5 — Full Lorentz-curvature and K-connection variations

<!-- ASSERT_CONVENTION: natural_units=hbar=c=1, metric_signature=(-,+,+,+,+); master C01, source_lock=UNG-WEYL2-OP58-CONVENTIONS-v5 -->

Let $`M'_{\mu\nu}{}^{ab}:=\widehat R'_{\mu\nu}{}^{ab}(M)`$.
Its defining R03 expression contains the ordinary curvature and five
fermionic terms, all of which must be varied:

```math
\begin{aligned}
M'_{\mu\nu}{}^{ab}={}&R_{\mu\nu}{}^{ab}(\omega)
+i\bar\phi_{[\mu}\gamma^{ab}\psi_{\nu]}
+i\bar\psi_{[\mu}\gamma^{[a}K\gamma^{b]}\psi_{\nu]}\\
&+\bar\psi_{[\mu}\gamma^{[a}e_{\nu]}{}^c\mathscr R_c{}^{b]}
+\frac12\bar\psi_{[\mu}\gamma_{\nu]}\mathscr R^{ab}
+8\bar\psi_{[\mu}e_{\nu]}{}^{[a}\gamma^{b]}\chi.
\end{aligned}\tag{P23a}
```

Varying the ordinary curvature gives

```math
\mathcal O_{\mu\nu}{}^{ab}
=2\partial_{[\mu}\Omega_{\nu]}{}^{ab}
+2\Omega_{[\mu}{}^{ac}\omega_{\nu]c}{}^b
+2\omega_{[\mu}{}^{ac}\Omega_{\nu]c}{}^b.
\tag{P24}
```

Both connection products are retained. This identity follows from the
world two-form definition, so no torsion-free assumption or hidden torsion
term is introduced. The derivative of (P16) is explicitly

```math
\begin{aligned}
2\partial_{[\mu}\Omega_{\nu]}{}^{ab}={}&
i(\partial_{[\mu}\bar\epsilon)\gamma^{ab}\phi_{\nu]}
+i\bar\epsilon\gamma^{ab}\partial_{[\mu}\phi_{\nu]}\\
&-2i(\partial_{[\mu}\bar\epsilon)\gamma^{[a}K\gamma^{b]}\psi_{\nu]}
-2i\bar\epsilon\gamma^{[a}(\partial_{[\mu}K)\gamma^{b]}\psi_{\nu]}
-2i\bar\epsilon\gamma^{[a}K\gamma^{b]}\partial_{[\mu}\psi_{\nu]}\\
&-(\partial_{[\mu}\bar\epsilon)\gamma^{[a}e_{\nu]}{}^c\mathscr R_c{}^{b]}
-\bar\epsilon\gamma^{[a}(\partial_{[\mu}e_{\nu]}{}^c)\mathscr R_c{}^{b]}
-\bar\epsilon\gamma^{[a}e_{[\nu}{}^c\partial_{\mu]}\mathscr R_c{}^{b]}\\
&-\frac12(\partial_{[\mu}\bar\epsilon)\gamma_{\nu]}\mathscr R^{ab}
-\frac12\bar\epsilon(\partial_{[\mu}e_{\nu]}{}^c)\gamma_c\mathscr R^{ab}
-\frac12\bar\epsilon\gamma_{[\nu}\partial_{\mu]}\mathscr R^{ab}\\
&-8(\partial_{[\mu}e_{\nu]}{}^{[a})\bar\epsilon\gamma^{b]}\chi
-8e_{[\nu}{}^{[a}(\partial_{\mu]}\bar\epsilon)\gamma^{b]}\chi
-8e_{[\nu}{}^{[a}\bar\epsilon\gamma^{b]}\partial_{\mu]}\chi.
\end{aligned}\tag{P25}
```

The two antisymmetrizations in this display, world $`\mu\nu`$ and tangent
$`ab`$, act independently; a bracket in one pair does not close the other.
Also $`\partial_\mu K=\gamma^{cd}\partial_\mu T_{cd}`$.

Here are the variations of **all five** fermionic terms of R03, with each
varied factor on its own line:

```math
\begin{aligned}
\mathcal C_{1,\mu\nu}{}^{ab}
 &=i\bar\Phi_{[\mu}\gamma^{ab}\psi_{\nu]}
  +i\bar\phi_{[\mu}\gamma^{ab}p_{\nu]},\\
\mathcal C_{2,\mu\nu}{}^{ab}
 &=i\bar p_{[\mu}\gamma^{[a}K\gamma^{b]}\psi_{\nu]}
  +i\bar\psi_{[\mu}\gamma^{[a}\kappa\gamma^{b]}\psi_{\nu]}
  +i\bar\psi_{[\mu}\gamma^{[a}K\gamma^{b]}p_{\nu]},\\
\mathcal C_{3,\mu\nu}{}^{ab}
 &=\bar p_{[\mu}\gamma^{[a}e_{\nu]}{}^c\mathscr R_c{}^{b]}
  +\bar\psi_{[\mu}\gamma^{[a}h_{\nu]}{}^c\mathscr R_c{}^{b]}
  +\bar\psi_{[\mu}\gamma^{[a}e_{\nu]}{}^c\rho_c{}^{b]},\\
\mathcal C_{4,\mu\nu}{}^{ab}
 &=\frac12\bar p_{[\mu}\gamma_{\nu]}\mathscr R^{ab}
  +\frac12\bar\psi_{[\mu}h_{\nu]}{}^c\gamma_c\mathscr R^{ab}
  +\frac12\bar\psi_{[\mu}\gamma_{\nu]}\rho^{ab},\\
\mathcal C_{5,\mu\nu}{}^{ab}
 &=8\bar p_{[\mu}e_{\nu]}{}^{[a}\gamma^{b]}\chi
  +8\bar\psi_{[\mu}h_{\nu]}{}^{[a}\gamma^{b]}\chi
  +8\bar\psi_{[\mu}e_{\nu]}{}^{[a}\gamma^{b]}\xi.
\end{aligned}\tag{P26}
```

Thus the complete primed Lorentz-curvature response is the explicit sum

```math
\Pi_{\mu\nu}{}^{ab}
=\mathcal O_{\mu\nu}{}^{ab}
+\mathcal C_{1,\mu\nu}{}^{ab}+\mathcal C_{2,\mu\nu}{}^{ab}
+\mathcal C_{3,\mu\nu}{}^{ab}+\mathcal C_{4,\mu\nu}{}^{ab}
+\mathcal C_{5,\mu\nu}{}^{ab}.
\tag{P27}
```

The five fermionic terms have produced $`2+3+3+3+3=14`$ terms, in addition
to the three ordinary-curvature terms in (P24). In particular the $`h`$ terms
in $`\mathcal C_3,\mathcal C_4,\mathcal C_5`$ have not been discarded.

Differentiate the Ricci contraction and then the dependent K connection:

```math
\begin{aligned}
r_{\mu\nu}&=\Pi_{\mu\rho}{}^{ab}e_b{}^\rho e_{\nu a}
+M'_{\mu\rho}{}^{ab}k_b{}^\rho e_{\nu a}
+M'_{\mu\rho}{}^{ab}e_b{}^\rho h_{\nu a},\\
f^{\epsilon}_\mu{}^a
&=-\frac16 r_{\mu\nu}e^{\nu a}
-\frac16\mathcal R_{\mu\nu}k^{\nu a}
+\frac1{48}h_\mu{}^a\mathcal R
-\frac1{48}e_\mu{}^a s^{\rho\sigma}\mathcal R_{\rho\sigma}
+\frac1{48}e_\mu{}^a g^{\rho\sigma}r_{\rho\sigma}.
\end{aligned}\tag{P28}
```

Here $`\mathcal R=g^{\mu\nu}\mathcal R_{\mu\nu}`$ and its variation is
$`-s^{\mu\nu}\mathcal R_{\mu\nu}+g^{\mu\nu}r_{\mu\nu}`$. This explains
both trace terms on the last line. The defining expression uses **primed**
curvature, so $`f^\epsilon`$ does not depend on itself.

Finally the complete tangent Weyl-curvature response is

```math
\begin{aligned}
c_{abcd}={}&-h_a{}^e\mathscr C_{ebcd}-h_b{}^e\mathscr C_{aecd}\\
&+e_a{}^\mu e_b{}^\nu\big[
\Pi_{\mu\nu cd}+8 f^\epsilon_{[\mu[c}e_{\nu]d]}
+8f_{[\mu[c}h_{\nu]d]}\big].
\end{aligned}\tag{P29}
```

There are two explicit inverse-frame terms here, because R03 defines
$`\mathscr C_{abcd}=e_a{}^\mu e_b{}^\nu\widehat R_{\mu\nu cd}(M)`$:
$`c,d`$ are already the internal Lorentz indices of the connection curvature.
If one first forms a four-world-index curvature, the two extra frame
variations on its last pair cancel their inverse-frame variations on
conversion back. Adding four inverse-frame terms to (P29) would be wrong.
Equations (P06)–(P29) define $`c`$ entirely, with no unresolved $`\delta f`$
or $`\delta\phi`$ and no omitted curvature fermions.

### Step P6 — Evaluate the variation of $`\mathcal D_aT_{bc}`$

<!-- ASSERT_CONVENTION: natural_units=hbar=c=1, metric_signature=(-,+,+,+,+); master C01, source_lock=UNG-WEYL2-OP58-CONVENTIONS-v5 -->

The W04 definition in notation (P05) is

```math
U_{a\,bc}=e_a{}^\mu\left[
\nabla^{\rm B}_\mu T_{bc}-\frac i2\bar\psi_\mu\gamma_{bc}\chi
+\frac{3i}{32}\bar\psi_\mu\mathscr R_{bc}\right].
\tag{P30}
```

Apply (P03) to the outside frame, each connection in $`\nabla^{\rm B}`$,
and both factors of each bilinear. The complete response is

```math
\begin{aligned}
u_{a\,bc}={}&-h_a{}^dU_{d\,bc}\\
&+e_a{}^\mu\big[
\nabla^{\rm B}_\mu\tau_{bc}-\beta_\mu T_{bc}
+\Omega_{\mu b}{}^dT_{dc}+\Omega_{\mu c}{}^dT_{bd}\\
&\hspace{18mm}-\frac i2\bar p_\mu\gamma_{bc}\chi
-\frac i2\bar\psi_\mu\gamma_{bc}\xi
+\frac{3i}{32}\bar p_\mu\mathscr R_{bc}
+\frac{3i}{32}\bar\psi_\mu\rho_{bc}\big].
\end{aligned}\tag{P31}
```

The lowercase symbol on the left is $`u_{a\,bc}`$ (not a new SU(2)
curvature). Its only differentiated response is fully expanded as

```math
\begin{aligned}
\nabla^{\rm B}_\mu\tau_{bc}={}&
\frac i2\overline{\nabla^{\rm B}_\mu\epsilon}\gamma_{bc}\chi
+\frac i2\bar\epsilon\gamma_{bc}\nabla^{\rm B}_\mu\chi\\
&-\frac{3i}{32}\overline{\nabla^{\rm B}_\mu\epsilon}\mathscr R_{bc}
-\frac{3i}{32}\bar\epsilon\nabla^{\rm B}_\mu\mathscr R_{bc}.
\end{aligned}\tag{P32}
```

The bosonic derivative obeys Leibniz and preserves the order of the two
odd factors, so no Grassmann minus appears here. Its parameter derivative
is exactly $`\partial_\mu\epsilon+b_\mu\epsilon/2+ \omega_\mu{}^{ab}\gamma_{ab}\epsilon/4-V_\mu\epsilon`$ as in (P06),
without the $`iK\gamma_\mu\epsilon`$ term. Here $`-V_\mu\epsilon`$ means
$`-V_\mu^{ij}\epsilon_j`$, or equivalently $`+V_\mu{}^i{}_j\epsilon^j`$. Every tensor connection in (P31)
has the sign of (P05), equivalent to the audited W04 tensor derivative.

### Step P7 — Evaluate the variation of $`\mathcal D_a\chi^i`$

<!-- ASSERT_CONVENTION: natural_units=hbar=c=1, metric_signature=(-,+,+,+,+); master C01, source_lock=UNG-WEYL2-OP58-CONVENTIONS-v5 -->

In the present notation the complete W04 definition is

```math
\begin{aligned}
Z_a^i=e_a{}^\mu\big[&\nabla^{\rm B}_\mu\chi^i
-\frac14\psi_\mu^iD+\frac1{64}\gamma^{bc}\mathscr V_{bc}^{ij}\psi_{\mu j}
-\frac i8\gamma^{bc}\gamma^dU_{d\,bc}\psi_\mu^i
+\frac i8\gamma^bU^c{}_{bc}\psi_\mu^i\\
&+\frac14G_4\psi_\mu^i-\frac16t_2\psi_\mu^i
-\frac14K\phi_\mu^i\big].
\end{aligned}\tag{P33}
```

Varying all connections and every factor gives

```math
\begin{aligned}
z_a^i={}&-h_a{}^bZ_b^i+e_a{}^\mu\big[
\nabla^{\rm B}_\mu\xi^i-\frac32\beta_\mu\chi^i
+\frac14\Omega_\mu{}^{bc}\gamma_{bc}\chi^i-v_\mu^{ij}\chi_j\\
&-\frac14p_\mu^iD-\frac14\psi_\mu^i d
+\frac1{64}\gamma^{bc}\nu_{bc}^{ij}\psi_{\mu j}
+\frac1{64}\gamma^{bc}\mathscr V_{bc}^{ij}p_{\mu j}\\
&-\frac i8\gamma^{bc}\gamma^d u_{d\,bc}\psi_\mu^i
-\frac i8\gamma^{bc}\gamma^d U_{d\,bc}p_\mu^i
+\frac i8\gamma^b u^c{}_{bc}\psi_\mu^i
+\frac i8\gamma^b U^c{}_{bc}p_\mu^i\\
&+\frac14\gamma^{bcde}\tau_{bc}T_{de}\psi_\mu^i
+\frac14\gamma^{bcde}T_{bc}\tau_{de}\psi_\mu^i
+\frac14G_4p_\mu^i\\
&-\frac16\theta\psi_\mu^i-\frac16t_2p_\mu^i
-\frac14\kappa\phi_\mu^i-\frac14K\Phi_\mu^i\big].
\end{aligned}\tag{P34}
```

The two $`\tau T`$ terms are written separately to show the two varied
factors of $`G_4`$. The S-connection term has produced both
$`-\kappa\phi_\mu/4`$ and $`-K\Phi_\mu/4`$. Neither is optional.
To evaluate the derivative of $`\xi`$ in (P34), apply Leibniz to each of its
six terms in (P09):

```math
\begin{aligned}
\nabla^{\rm B}_\mu\xi^i={}&
\frac14(\nabla^{\rm B}_\mu D)\epsilon^i
+\frac14D\nabla^{\rm B}_\mu\epsilon^i\\
&-\frac1{64}\gamma^{ab}(\nabla^{\rm B}_\mu\mathscr V_{ab}^{ij})\epsilon_j
-\frac1{64}\gamma^{ab}\mathscr V_{ab}^{ij}\nabla^{\rm B}_\mu\epsilon_j\\
&+\frac i8\gamma^{ab}\gamma^c(\nabla^{\rm B}_\mu U_{c\,ab})\epsilon^i
+\frac i8\gamma^{ab}\gamma^cU_{c\,ab}\nabla^{\rm B}_\mu\epsilon^i\\
&-\frac i8\gamma^a(\nabla^{\rm B}_\mu U^b{}_{ab})\epsilon^i
-\frac i8\gamma^aU^b{}_{ab}\nabla^{\rm B}_\mu\epsilon^i\\
&-\frac14\gamma^{abcd}(\nabla^{\rm B}_\mu T_{ab})T_{cd}\epsilon^i
-\frac14\gamma^{abcd}T_{ab}(\nabla^{\rm B}_\mu T_{cd})\epsilon^i
-\frac14G_4\nabla^{\rm B}_\mu\epsilon^i\\
&+\frac13T^{ab}(\nabla^{\rm B}_\mu T_{ab})\epsilon^i
+\frac16t_2\nabla^{\rm B}_\mu\epsilon^i.
\end{aligned}\tag{P35}
```

There are thirteen terms. The coefficient $`1/3`$ in the penultimate term
is $`(1/6)\times2`$ from differentiating $`t_2`$. Derivatives on $`U`$ have not
been reordered or replaced by commuting second derivatives of $`T`$.

### Step P8 — Evaluate the variation of $`\mathcal D_a\mathscr R_{bc}^i`$

<!-- ASSERT_CONVENTION: natural_units=hbar=c=1, metric_signature=(-,+,+,+,+); master C01, source_lock=UNG-WEYL2-OP58-CONVENTIONS-v5 -->

G01 and the prescription following R06b give the explicit full derivative

```math
\begin{aligned}
Y_{a\,bc}^i=e_a{}^\mu\big[&\nabla^{\rm B}_\mu\mathscr R_{bc}^i
-H_{bc}{}^{de}\mathscr V_{de}{}^i{}_j\psi_\mu^j
-\frac14\mathscr C_{bc}{}^{de}\gamma_{de}\psi_\mu^i\\
&-2iP_{bc}[U]\psi_\mu^i-A_{bc}[T]\phi_\mu^i\big].
\end{aligned}\tag{P36}
```

The weight in the bosonic derivative is $`3/2`$; both lower tangent indices
have connections in (P05). Both curvatures in R06 are K invariant, so
there is no missing independent $`f_\mu\delta_K\mathscr R`$ term in this
first derivative. The K connection still enters the calculation through
$`\mathscr C`$ and its variation.

All product-rule contributions to (P36) are

```math
\begin{aligned}
y_{a\,bc}^i={}&-h_a{}^dY_{d\,bc}^i
+e_a{}^\mu\big[\nabla^{\rm B}_\mu\rho_{bc}^i
-\frac32\beta_\mu\mathscr R_{bc}^i
+\frac14\Omega_\mu{}^{de}\gamma_{de}\mathscr R_{bc}^i
-v_\mu^{ij}\mathscr R_{bc\,j}\\
&+\Omega_{\mu b}{}^d\mathscr R_{dc}^i
+\Omega_{\mu c}{}^d\mathscr R_{bd}^i
-H_{bc}{}^{de}\nu_{de}{}^i{}_j\psi_\mu^j
-H_{bc}{}^{de}\mathscr V_{de}{}^i{}_j p_\mu^j\\
&-\frac14c_{bc}{}^{de}\gamma_{de}\psi_\mu^i
-\frac14\mathscr C_{bc}{}^{de}\gamma_{de}p_\mu^i
-2iP_{bc}[u]\psi_\mu^i-2iP_{bc}[U]p_\mu^i\\
&-A_{bc}[\tau]\phi_\mu^i-A_{bc}[T]\Phi_\mu^i\big].
\end{aligned}\tag{P37}
```

The linearity in (P11) is the reason the coefficient variations are
$`P[u]`$ and $`A[\tau]`$. Each contains exactly the four and three terms
displayed there; no variation of a coefficient is hidden in this notation.
The remaining differentiated polynomial is

```math
\begin{aligned}
\nabla^{\rm B}_\mu\rho_{ab}^i={}&
\frac16\gamma_{ab}{}^{cd}(\nabla^{\rm B}_\mu\mathscr V_{cd}{}^i{}_j)\epsilon^j
+\frac16\gamma_{ab}{}^{cd}\mathscr V_{cd}{}^i{}_j\nabla^{\rm B}_\mu\epsilon^j\\
&-\frac16\gamma^{cd}\gamma_{ab}(\nabla^{\rm B}_\mu\mathscr V_{cd}{}^i{}_j)\epsilon^j
-\frac16\gamma^{cd}\gamma_{ab}\mathscr V_{cd}{}^i{}_j\nabla^{\rm B}_\mu\epsilon^j\\
&-\frac1{12}\gamma_{ab}\gamma^{cd}(\nabla^{\rm B}_\mu\mathscr V_{cd}{}^i{}_j)\epsilon^j
-\frac1{12}\gamma_{ab}\gamma^{cd}\mathscr V_{cd}{}^i{}_j\nabla^{\rm B}_\mu\epsilon^j\\
&+\frac14(\nabla^{\rm B}_\mu\mathscr C_{ab}{}^{cd})\gamma_{cd}\epsilon^i
+\frac14\mathscr C_{ab}{}^{cd}\gamma_{cd}\nabla^{\rm B}_\mu\epsilon^i\\
&+2i\gamma^{cd}(\nabla^{\rm B}_\mu U_{[a\,cd})\gamma_{b]}\epsilon^i
+2i\gamma^{cd}U_{[a\,cd}\gamma_{b]}\nabla^{\rm B}_\mu\epsilon^i\\
&-\frac{2i}{3}\gamma_{[b}\gamma^{cd}(\nabla^{\rm B}_\mu U_{a]\,cd})\epsilon^i
-\frac{2i}{3}\gamma_{[b}\gamma^{cd}U_{a]\,cd}\nabla^{\rm B}_\mu\epsilon^i\\
&-\frac{2i}{3}\gamma_{[a}\gamma^f\gamma^{cd}(\nabla^{\rm B}_\mu U_{f\,cd})\gamma_{b]}\epsilon^i
-\frac{2i}{3}\gamma_{[a}\gamma^f\gamma^{cd}U_{f\,cd}\gamma_{b]}\nabla^{\rm B}_\mu\epsilon^i\\
&-\frac{2i}{3}\gamma_{ab}\gamma_d\eta^{ce}\eta^{df}(\nabla^{\rm B}_\mu U_{c\,ef})\epsilon^i
-\frac{2i}{3}\gamma_{ab}\gamma_d\eta^{ce}\eta^{df}U_{c\,ef}\nabla^{\rm B}_\mu\epsilon^i.
\end{aligned}\tag{P38}
```

These sixteen terms come from the eight terms of (P12), each differentiated
on its coefficient and then on its parameter. The bosonic derivative is
compatible with the gamma tensors and their Lorentz indices; no extra
partial derivative of a constant tangent gamma matrix is generated.

### Step P9 — Account for the derivatives of the local parameter

<!-- ASSERT_CONVENTION: natural_units=hbar=c=1, metric_signature=(-,+,+,+,+); master C01, source_lock=UNG-WEYL2-OP58-CONVENTIONS-v5 -->

This step checks actual cancellations without setting $`\partial\epsilon=0`$.
It also explains why retaining every connection term in the preceding steps
is necessary.

First define the explicitly displayed matrix connection

```math
\mathcal A_\mu{}^i{}_j
=\left(\frac12b_\mu+\frac14\omega_\mu{}^{ab}\gamma_{ab}
+iK\gamma_\mu\right)\delta^i_j+V_\mu{}^i{}_j,
\qquad p_\mu=(\partial_\mu+\mathcal A_\mu)\epsilon.
\tag{P39}
```

The plus in front of the mixed $`V`$ is precisely
$`-V^{ij}\epsilon_j=+V^i{}_j\epsilon^j`$. Equation (P17) is
$`q'_{\mu\nu}=2(\partial_{[\mu}+\mathcal A_{[\mu})\psi_{\nu]}`$.
Its varied connection is the known polynomial

```math
\mathcal A_\mu^\epsilon{}^i{}_j
=\left(\frac12\beta_\mu+\frac14\Omega_\mu{}^{ab}\gamma_{ab}
+i\kappa\gamma_\mu+iK h_\mu{}^a\gamma_a\right)\delta^i_j
+v_\mu{}^i{}_j.
\tag{P40}
```

Substitute $`p`$ into the derivative terms of (P18) and expand their order:

```math
\begin{aligned}
a_{\mu\nu}
={}&2\mathcal A^\epsilon_{[\mu}\psi_{\nu]}
+2\partial_{[\mu}\partial_{\nu]}\epsilon
+2(\partial_{[\mu}\mathcal A_{\nu]})\epsilon\\
&+2\mathcal A_{[\nu}\partial_{\mu]}\epsilon
+2\mathcal A_{[\mu}\partial_{\nu]}\epsilon
+2\mathcal A_{[\mu}\mathcal A_{\nu]}\epsilon\\
={}&2\mathcal A^\epsilon_{[\mu}\psi_{\nu]}
+2(\partial_{[\mu}\mathcal A_{\nu]}+
\mathcal A_{[\mu}\mathcal A_{\nu]})\epsilon.
\end{aligned}\tag{P41}
```

The second derivative is zero by P-A7; the two adjacent first-derivative
terms are equal and opposite after exchanging $`\mu,\nu`$. Thus $`a`$, and
then every term of $`\Phi`$ in (P21), contains no derivative of $`\epsilon`$
after this cancellation. This compact identity is a check on the expanded
(P18)–(P19); their terms are still fully retained.

For $`\Pi`$, let $`\zeta_\mu=\partial_\mu\epsilon`$. Its derivative-parameter
terms from (P25) are

```math
\begin{aligned}
\mathcal O\big|_{\partial\epsilon}={}&
i\bar\zeta_{[\mu}\gamma^{ab}\phi_{\nu]}
-2i\bar\zeta_{[\mu}\gamma^{[a}K\gamma^{b]}\psi_{\nu]}
-\bar\zeta_{[\mu}\gamma^{[a}e_{\nu]}{}^c\mathscr R_c{}^{b]}\\
&-\frac12\bar\zeta_{[\mu}\gamma_{\nu]}\mathscr R^{ab}
-8\bar\zeta_{[\mu}e_{\nu]}{}^{[a}\gamma^{b]}\chi.
\end{aligned}\tag{P42}
```

The five lines of (P26) provide the respective opposite contributions:

```math
\begin{aligned}
\mathcal C_1\big|_{\partial\epsilon}
 &=i\bar\phi_{[\mu}\gamma^{ab}\zeta_{\nu]}
 =-i\bar\zeta_{[\mu}\gamma^{ab}\phi_{\nu]},\\
\mathcal C_2\big|_{\partial\epsilon}
 &=i\bar\zeta_{[\mu}\Gamma^{ab}\psi_{\nu]}
  +i\bar\psi_{[\mu}\Gamma^{ab}\zeta_{\nu]}
 =2i\bar\zeta_{[\mu}\Gamma^{ab}\psi_{\nu]},
 \quad\Gamma^{ab}=\gamma^{[a}K\gamma^{b]},\\
\mathcal C_3\big|_{\partial\epsilon}
 &=+\bar\zeta_{[\mu}\gamma^{[a}e_{\nu]}{}^c\mathscr R_c{}^{b]},\\
\mathcal C_4\big|_{\partial\epsilon}
 &=+\frac12\bar\zeta_{[\mu}\gamma_{\nu]}\mathscr R^{ab},\\
\mathcal C_5\big|_{\partial\epsilon}
 &=+8\bar\zeta_{[\mu}e_{\nu]}{}^{[a}\gamma^{b]}\chi.
\end{aligned}\tag{P43}
```

The first line uses the **contracted** rank2 flip
$`\bar\phi\gamma^{ab}\zeta=+\bar\zeta\gamma^{ab}\phi`$, followed by
exchanging the antisymmetric world labels. For the second line,

```math
\widetilde\Gamma^{ab}
=-\gamma^{[b}K\gamma^{a]}=+\Gamma^{ab},\qquad
\bar\psi\Gamma^{ab}\zeta=-\bar\zeta\Gamma^{ab}\psi.
\tag{P44}
```

The latter minus is the contracted SU(2) flip with a transpose-even
matrix. It cancels the world-label exchange. Equations (P42)–(P43)
cancel term for term. The other terms in (P26) contain $`h,\kappa,\xi,\rho`$
or $`\Phi`$, all already without parameter derivatives. Consequently
$`\Pi`$, $`r_{\mu\nu}`$, $`f^\epsilon`$ and $`c`$ have no uncancelled
$`\partial\epsilon`$ terms.

In $`u`$, the two terms in (P32) that differentiate the parameter cancel
the corresponding pieces of $`\bar p`$ in (P31):

```math
\left[\frac i2\overline{\nabla^{\rm B}_\mu\epsilon}\gamma_{bc}\chi
-\frac{3i}{32}\overline{\nabla^{\rm B}_\mu\epsilon}\mathscr R_{bc}\right]
-\frac i2\overline{\nabla^{\rm B}_\mu\epsilon}\gamma_{bc}\chi
+\frac{3i}{32}\overline{\nabla^{\rm B}_\mu\epsilon}\mathscr R_{bc}=0.
\tag{P45}
```

The finite remainders from
$`\bar p_\mu-\overline{\nabla^{\rm B}_\mu\epsilon} =-i\bar\epsilon\gamma_\mu K`$ are, explicitly,
$`-\bar\epsilon\gamma_\mu K\gamma_{bc}\chi/2`$
and $`+3\bar\epsilon\gamma_\mu K\mathscr R_{bc}/32`$.
They are retained in (P31), not discarded with the parameter derivatives.

For $`z`$ and $`y`$ there is an equally explicit coefficient-by-coefficient
pairing. Denote by $`\xi[\alpha]`$ the six-term expression (P09) with
$`\epsilon`$ replaced by $`\alpha`$, and by $`\rho[\alpha]`$ the eight-term
expression (P12) with the same replacement. The six parameter-derivative
terms of (P35) are exactly $`\xi[\nabla^{\rm B}_\mu\epsilon]`$; the terms
of (P34) proportional to $`p_\mu`$ are exactly $`-\xi[p_\mu]`$.
The eight parameter-derivative terms of (P38) are
$`\rho[\nabla^{\rm B}_\mu\epsilon]`$; the $`p_\mu`$ terms of (P37) are
$`-\rho[p_\mu]`$. Thus the two cancellations, with their retained
remainders, are

```math
\begin{aligned}
\xi[\nabla^{\rm B}_\mu\epsilon]-\xi[p_\mu]
 &=-\xi[iK\gamma_\mu\epsilon],\\
\rho[\nabla^{\rm B}_\mu\epsilon]-\rho[p_\mu]
 &=-\rho[iK\gamma_\mu\epsilon].
\end{aligned}\tag{P46}
```

This is cancellation of six and eight displayed pairs, respectively, by
linearity of their already expanded polynomials, not an assumption about
the desired multiplet. The right sides remain among the terms of
(P34),(P37). Together (P41)–(P46) account for every differentiated local
parameter. No constant-parameter restriction has been used.

### Step P10 — Vary $`F_1`$, keeping every factor

<!-- ASSERT_CONVENTION: natural_units=hbar=c=1, metric_signature=(-,+,+,+,+); master C01, source_lock=UNG-WEYL2-OP58-CONVENTIONS-v5 -->

Apply the even product rule (P03) and insert the already evaluated responses:

```math
\delta_Q F_{1}^i=-\frac18\gamma_{cd}\big[\rho_{ab}^i\mathscr C^{abcd}+\mathscr R_{ab}^ic^{abcd}\big].\tag{P47}
```

Expanding the elementary matter/curvature responses gives all 9 contributions:

```math
\begin{aligned}
\mathcal W_{1}^i:={}&
-\frac{1}{48}\gamma_{cd}\gamma_{ab}{}^{ef}\mathscr V_{ef}{}^i{}_j\epsilon^j\mathscr C^{abcd}\\
&+\frac{1}{48}\gamma_{cd}\gamma^{ef}\gamma_{ab}\mathscr V_{ef}{}^i{}_j\epsilon^j\mathscr C^{abcd}\\
&+\frac{1}{96}\gamma_{cd}\gamma_{ab}\gamma^{ef}\mathscr V_{ef}{}^i{}_j\epsilon^j\mathscr C^{abcd}\\
&-\frac{1}{32}\gamma_{cd}\mathscr C_{ab}{}^{ef}\gamma_{ef}\epsilon^i\mathscr C^{abcd}\\
&-\frac{i}{4}\gamma_{cd}\gamma^{ef}U_{[a\,ef}\gamma_{b]}\epsilon^i\mathscr C^{abcd}\\
&+\frac{i}{12}\gamma_{cd}\gamma_{[b}\gamma^{ef}U_{a]\,ef}\epsilon^i\mathscr C^{abcd}\\
&+\frac{i}{12}\gamma_{cd}\gamma_{[a}\gamma^g\gamma^{ef}U_{g\,ef}\gamma_{b]}\epsilon^i\mathscr C^{abcd}\\
&+\frac{i}{12}\gamma_{cd}\gamma_{ab}\gamma^eU^f{}_{fe}\epsilon^i\mathscr C^{abcd}\\
&-\frac{1}{8}\gamma_{cd}\mathscr R_{ab}^ic^{abcd}.
\end{aligned}\tag{P48}
```

The first eight terms vary the gravitino curvature; the ninth varies the full Weyl curvature through (P24)–(P29). The latter contains the fourteen fermionic curvature contributions in (P26).

### Step P11 — Vary $`F_2`$, keeping every factor

<!-- ASSERT_CONVENTION: natural_units=hbar=c=1, metric_signature=(-,+,+,+,+); master C01, source_lock=UNG-WEYL2-OP58-CONVENTIONS-v5 -->

Apply the even product rule (P03) and insert the already evaluated responses:

```math
\delta_Q F_{2}^i=-4i\gamma_c\big[\rho_{ab}^iU^{a\,bc}+\mathscr R_{ab}^iu^{a\,bc}\big].\tag{P49}
```

Expanding the elementary matter/curvature responses gives all 9 contributions:

```math
\begin{aligned}
\mathcal W_{2}^i:={}&
-\frac{2i}{3}\gamma_c\gamma_{ab}{}^{de}\mathscr V_{de}{}^i{}_j\epsilon^jU^{a\,bc}\\
&+\frac{2i}{3}\gamma_c\gamma^{de}\gamma_{ab}\mathscr V_{de}{}^i{}_j\epsilon^jU^{a\,bc}\\
&+\frac{i}{3}\gamma_c\gamma_{ab}\gamma^{de}\mathscr V_{de}{}^i{}_j\epsilon^jU^{a\,bc}\\
&-i\gamma_c\mathscr C_{ab}{}^{de}\gamma_{de}\epsilon^iU^{a\,bc}\\
&+8\gamma_c\gamma^{de}U_{[a\,de}\gamma_{b]}\epsilon^iU^{a\,bc}\\
&-\frac{8}{3}\gamma_c\gamma_{[b}\gamma^{de}U_{a]\,de}\epsilon^iU^{a\,bc}\\
&-\frac{8}{3}\gamma_c\gamma_{[a}\gamma^f\gamma^{de}U_{f\,de}\gamma_{b]}\epsilon^iU^{a\,bc}\\
&-\frac{8}{3}\gamma_c\gamma_{ab}\gamma^dU^e{}_{ed}\epsilon^iU^{a\,bc}\\
&-4i\gamma_c\mathscr R_{ab}^iu^{a\,bc}.
\end{aligned}\tag{P50}
```

The coefficient of its fifth term is $`(-4i)(2i)=+8`$; the next three are $`(-4i)(-2i/3)=-8/3`$. The final term includes the full derivative response (P31)–(P32).

### Step P12 — Vary $`F_3`$, keeping every factor

<!-- ASSERT_CONVENTION: natural_units=hbar=c=1, metric_signature=(-,+,+,+,+); master C01, source_lock=UNG-WEYL2-OP58-CONVENTIONS-v5 -->

Apply the even product rule (P03) and insert the already evaluated responses:

```math
\delta_Q F_{3}^i=\frac{128}{3}\big[\xi^iD+\chi^i d\big].\tag{P51}
```

Expanding the elementary matter/curvature responses gives all 8 contributions:

```math
\begin{aligned}
\mathcal W_{3}^i:={}&
\frac{32}{3}D\epsilon^iD\\
&-\frac{2}{3}\gamma^{ab}\mathscr V_{ab}^{ij}\epsilon_jD\\
&+\frac{16i}{3}\gamma^{ab}\gamma^cU_{c\,ab}\epsilon^iD\\
&-\frac{16i}{3}\gamma^aU^b{}_{ab}\epsilon^iD\\
&-\frac{32}{3}G_4\epsilon^iD\\
&+\frac{64}{9}t_2\epsilon^iD\\
&+\frac{128}{3}\chi^i(\bar\epsilon\gamma^aZ_a)\\
&-\frac{640i}{9}\chi^i(\bar\epsilon K\chi).
\end{aligned}\tag{P52}
```

The last two terms come from varying D, including its $`-5i\bar\epsilon K\chi/3`$ term. Their spinor order is the original $`\chi^i d`$ order; no Fierz transformation is implicit.

### Step P13 — Vary $`F_4`$, keeping every factor

<!-- ASSERT_CONVENTION: natural_units=hbar=c=1, metric_signature=(-,+,+,+,+); master C01, source_lock=UNG-WEYL2-OP58-CONVENTIONS-v5 -->

Apply the even product rule (P03) and insert the already evaluated responses:

```math
\delta_Q F_{4}^i=8i\gamma_c\big[y^{c}{}_{ab}^iT^{ab}+Y^{c}{}_{ab}^i\tau^{ab}\big].\tag{P53}
```

Expanding the elementary matter/curvature responses gives all 3 contributions:

```math
\begin{aligned}
\mathcal W_{4}^i:={}&
8i\gamma_cy^{c}{}_{ab}^iT^{ab}\\
&-4\gamma_cY^{c}{}_{ab}^i(\bar\epsilon\gamma^{ab}\chi)\\
&+\frac{3}{4}\gamma_cY^{c}{}_{ab}^i(\bar\epsilon\mathscr R^{ab}).
\end{aligned}\tag{P54}
```

The first term is the full covariant-curvature derivative response (P37)–(P38). In the last two terms, $`8i(i/2)=-4`$ and $`8i(-3i/32)=+3/4`$. The differentiated curvature has not been integrated by parts.

### Step P14 — Vary $`F_5`$, keeping every factor

<!-- ASSERT_CONVENTION: natural_units=hbar=c=1, metric_signature=(-,+,+,+,+); master C01, source_lock=UNG-WEYL2-OP58-CONVENTIONS-v5 -->

Apply the even product rule (P03) and insert the already evaluated responses:

```math
\delta_Q F_{5}^i=8i\gamma_a\big[y^{c}{}_{bc}^iT^{ab}+Y^{c}{}_{bc}^i\tau^{ab}\big].\tag{P55}
```

Expanding the elementary matter/curvature responses gives all 3 contributions:

```math
\begin{aligned}
\mathcal W_{5}^i:={}&
8i\gamma_ay^{c}{}_{bc}^iT^{ab}\\
&-4\gamma_aY^{c}{}_{bc}^i(\bar\epsilon\gamma^{ab}\chi)\\
&+\frac{3}{4}\gamma_aY^{c}{}_{bc}^i(\bar\epsilon\mathscr R^{ab}).
\end{aligned}\tag{P56}
```

The first term is the full covariant-curvature derivative response (P37)–(P38). In the last two terms, $`8i(i/2)=-4`$ and $`8i(-3i/32)=+3/4`$. The differentiated curvature has not been integrated by parts.

### Step P15 — Vary $`F_6`$, keeping every factor

<!-- ASSERT_CONVENTION: natural_units=hbar=c=1, metric_signature=(-,+,+,+,+); master C01, source_lock=UNG-WEYL2-OP58-CONVENTIONS-v5 -->

Apply the even product rule (P03) and insert the already evaluated responses:

```math
\delta_Q F_{6}^i=-\frac{64i}{3}\gamma^{ab}\gamma^c\big[u_{a\,bc}\chi^i+U_{a\,bc}\xi^i\big].\tag{P57}
```

Expanding the elementary matter/curvature responses gives all 7 contributions:

```math
\begin{aligned}
\mathcal W_{6}^i:={}&
-\frac{64i}{3}\gamma^{ab}\gamma^c u_{a\,bc}\chi^i\\
&-\frac{16i}{3}\gamma^{ab}\gamma^cU_{a\,bc}D\epsilon^i\\
&+\frac{i}{3}\gamma^{ab}\gamma^cU_{a\,bc}\gamma^{de}\mathscr V_{de}^{ij}\epsilon_j\\
&+\frac{8}{3}\gamma^{ab}\gamma^cU_{a\,bc}\gamma^{de}\gamma^fU_{f\,de}\epsilon^i\\
&-\frac{8}{3}\gamma^{ab}\gamma^cU_{a\,bc}\gamma^dU^e{}_{de}\epsilon^i\\
&+\frac{16i}{3}\gamma^{ab}\gamma^cU_{a\,bc}G_4\epsilon^i\\
&-\frac{32i}{9}\gamma^{ab}\gamma^cU_{a\,bc}t_2\epsilon^i.
\end{aligned}\tag{P58}
```

The first contribution varies the full derivative of T, while the other six vary chi. The $`+8/3`$ and $`-8/3`$ entries are separate ordered gamma products; no commutation of their matrices is assumed.

### Step P16 — Vary $`F_7`$, keeping every factor

<!-- ASSERT_CONVENTION: natural_units=hbar=c=1, metric_signature=(-,+,+,+,+); master C01, source_lock=UNG-WEYL2-OP58-CONVENTIONS-v5 -->

Apply the even product rule (P03) and insert the already evaluated responses:

```math
\delta_Q F_{7}^i=\frac{1024}{9}\big[\theta\chi^i+t_2\xi^i\big].\tag{P59}
```

Expanding the elementary matter/curvature responses gives all 8 contributions:

```math
\begin{aligned}
\mathcal W_{7}^i:={}&
\frac{1024i}{9}T^{ab}(\bar\epsilon\gamma_{ab}\chi)\chi^i\\
&-\frac{64i}{3}T^{ab}(\bar\epsilon\mathscr R_{ab})\chi^i\\
&+\frac{256}{9}t_2D\epsilon^i\\
&-\frac{16}{9}t_2\gamma^{ab}\mathscr V_{ab}^{ij}\epsilon_j\\
&+\frac{128i}{9}t_2\gamma^{ab}\gamma^cU_{c\,ab}\epsilon^i\\
&-\frac{128i}{9}t_2\gamma^aU^b{}_{ab}\epsilon^i\\
&-\frac{256}{9}t_2G_4\epsilon^i\\
&+\frac{512}{27}t_2t_2\epsilon^i.
\end{aligned}\tag{P60}
```

Both T factors have been varied through theta. In particular $`(1024/9)(-3i/16)=-64i/3`$, and the last term has coefficient $`(1024/9)(1/6)=512/27`$. It contains $`(T^2)^2`$.

### Step P17 — Vary $`F_8`$, keeping every factor

<!-- ASSERT_CONVENTION: natural_units=hbar=c=1, metric_signature=(-,+,+,+,+); master C01, source_lock=UNG-WEYL2-OP58-CONVENTIONS-v5 -->

Apply the even product rule (P03) and insert the already evaluated responses:

```math
\delta_Q F_{8}^i=\frac{128i}{3}\gamma_a\big[z_b^iT^{ab}+Z_b^i\tau^{ab}\big].\tag{P61}
```

Expanding the elementary matter/curvature responses gives all 3 contributions:

```math
\begin{aligned}
\mathcal W_{8}^i:={}&
\frac{128i}{3}\gamma_a z_b^iT^{ab}\\
&-\frac{64}{3}\gamma_a Z_b^i(\bar\epsilon\gamma^{ab}\chi)\\
&+4\gamma_a Z_b^i(\bar\epsilon\mathscr R^{ab}).
\end{aligned}\tag{P62}
```

The z term contains every line of (P34), including its induced S-connection variation. The two remaining coefficients are $`(128i/3)(i/2)=-64/3`$ and $`(128i/3)(-3i/32)=4`$.

### Step P18 — Vary $`F_9`$, keeping every factor

<!-- ASSERT_CONVENTION: natural_units=hbar=c=1, metric_signature=(-,+,+,+,+); master C01, source_lock=UNG-WEYL2-OP58-CONVENTIONS-v5 -->

Apply the even product rule (P03) and insert the already evaluated responses:

```math
\delta_Q F_{9}^i=\frac83\gamma_{ab}\big[\rho_{cd}^iT^{ab}T^{cd}+\mathscr R_{cd}^i\tau^{ab}T^{cd}+\mathscr R_{cd}^iT^{ab}\tau^{cd}\big].\tag{P63}
```

Expanding the elementary matter/curvature responses gives all 12 contributions:

```math
\begin{aligned}
\mathcal W_{9}^i:={}&
\frac{4}{9}\gamma_{ab}\gamma_{cd}{}^{ef}\mathscr V_{ef}{}^i{}_j\epsilon^jT^{ab}T^{cd}\\
&-\frac{4}{9}\gamma_{ab}\gamma^{ef}\gamma_{cd}\mathscr V_{ef}{}^i{}_j\epsilon^jT^{ab}T^{cd}\\
&-\frac{2}{9}\gamma_{ab}\gamma_{cd}\gamma^{ef}\mathscr V_{ef}{}^i{}_j\epsilon^jT^{ab}T^{cd}\\
&+\frac{2}{3}\gamma_{ab}\mathscr C_{cd}{}^{ef}\gamma_{ef}\epsilon^iT^{ab}T^{cd}\\
&+\frac{16i}{3}\gamma_{ab}\gamma^{ef}U_{[c\,ef}\gamma_{d]}\epsilon^iT^{ab}T^{cd}\\
&-\frac{16i}{9}\gamma_{ab}\gamma_{[d}\gamma^{ef}U_{c]\,ef}\epsilon^iT^{ab}T^{cd}\\
&-\frac{16i}{9}\gamma_{ab}\gamma_{[c}\gamma^g\gamma^{ef}U_{g\,ef}\gamma_{d]}\epsilon^iT^{ab}T^{cd}\\
&-\frac{16i}{9}\gamma_{ab}\gamma_{cd}\gamma^eU^f{}_{fe}\epsilon^iT^{ab}T^{cd}\\
&+\frac{4i}{3}\gamma_{ab}\mathscr R_{cd}^i(\bar\epsilon\gamma^{ab}\chi)T^{cd}\\
&-\frac{i}{4}\gamma_{ab}\mathscr R_{cd}^i(\bar\epsilon\mathscr R^{ab})T^{cd}\\
&+\frac{4i}{3}\gamma_{ab}\mathscr R_{cd}^iT^{ab}(\bar\epsilon\gamma^{cd}\chi)\\
&-\frac{i}{4}\gamma_{ab}\mathscr R_{cd}^iT^{ab}(\bar\epsilon\mathscr R^{cd}).
\end{aligned}\tag{P64}
```

All three factors are varied. The last four terms are not replaced by a guessed factor of 2: the two T factors have different contractions with the outside gamma and the curvature. Every coefficient in this block follows from the adopted $`8/3`$.

### Step P19 — Vary $`F_10`$, keeping every factor

<!-- ASSERT_CONVENTION: natural_units=hbar=c=1, metric_signature=(-,+,+,+,+); master C01, source_lock=UNG-WEYL2-OP58-CONVENTIONS-v5 -->

Apply the even product rule (P03) and insert the already evaluated responses:

```math
\delta_Q F_{10}^i=\frac12\big[\nu^{ab\,i}{}_{j}\mathscr R_{ab}^j+\mathscr V^{ab\,i}{}_{j}\rho_{ab}^j\big].\tag{P65}
```

Expanding the elementary matter/curvature responses gives all 17 contributions:

```math
\begin{aligned}
\mathcal W_{10}^i:={}&
-\frac{3}{4}B_{1}{}^{ab\,ik}\varepsilon_{kj}\mathscr R_{ab}^j\\
&-\frac{3}{4}B_{2}{}^{ab\,ik}\varepsilon_{kj}\mathscr R_{ab}^j\\
&+2iB_{3}{}^{ab\,ik}\varepsilon_{kj}\mathscr R_{ab}^j\\
&-9iB_{4}{}^{ab\,ik}\varepsilon_{kj}\mathscr R_{ab}^j\\
&+\frac{9i}{4}B_{5}{}^{ab\,ik}\varepsilon_{kj}\mathscr R_{ab}^j\\
&+6iB_{6}{}^{ab\,ik}\varepsilon_{kj}\mathscr R_{ab}^j\\
&-4B_{7}{}^{ab\,ik}\varepsilon_{kj}\mathscr R_{ab}^j\\
&+\frac{i}{2}B_{8}{}^{ab\,ik}\varepsilon_{kj}\mathscr R_{ab}^j\\
&+4iB_{9}{}^{ab\,ik}\varepsilon_{kj}\mathscr R_{ab}^j\\
&+\frac{1}{12}\mathscr V^{ab\,i}{}_{j}\gamma_{ab}{}^{cd}\mathscr V_{cd}{}^j{}_k\epsilon^k\\
&-\frac{1}{12}\mathscr V^{ab\,i}{}_{j}\gamma^{cd}\gamma_{ab}\mathscr V_{cd}{}^j{}_k\epsilon^k\\
&-\frac{1}{24}\mathscr V^{ab\,i}{}_{j}\gamma_{ab}\gamma^{cd}\mathscr V_{cd}{}^j{}_k\epsilon^k\\
&+\frac{1}{8}\mathscr V^{ab\,i}{}_{j}\mathscr C_{ab}{}^{cd}\gamma_{cd}\epsilon^j\\
&+i\mathscr V^{ab\,i}{}_{j}\gamma^{cd}U_{[a\,cd}\gamma_{b]}\epsilon^j\\
&-\frac{i}{3}\mathscr V^{ab\,i}{}_{j}\gamma_{[b}\gamma^{cd}U_{a]\,cd}\epsilon^j\\
&-\frac{i}{3}\mathscr V^{ab\,i}{}_{j}\gamma_{[a}\gamma^e\gamma^{cd}U_{e\,cd}\gamma_{b]}\epsilon^j\\
&-\frac{i}{3}\mathscr V^{ab\,i}{}_{j}\gamma_{ab}\gamma^cU^d{}_{dc}\epsilon^j.
\end{aligned}\tag{P66}
```

The first nine terms are the nine bilinears of (P14) with every source coefficient from (P15) multiplied by $`1/2`$. The epsilon tensor converts their second upper SU(2) index to the mixed slot. The last eight terms vary the gravitino curvature.

### Step P20 — Vary $`F_11`$, keeping every factor

<!-- ASSERT_CONVENTION: natural_units=hbar=c=1, metric_signature=(-,+,+,+,+); master C01, source_lock=UNG-WEYL2-OP58-CONVENTIONS-v5 -->

Apply the even product rule (P03) and insert the already evaluated responses:

```math
\delta_Q F_{11}^i=-\frac83\big[\nu^{ab\,i}{}_{j}\gamma_{ab}\chi^j+\mathscr V^{ab\,i}{}_{j}\gamma_{ab}\xi^j\big].\tag{P67}
```

Expanding the elementary matter/curvature responses gives all 15 contributions:

```math
\begin{aligned}
\mathcal W_{11}^i:={}&
4B_{1}{}^{ab\,ik}\varepsilon_{kj}\gamma_{ab}\chi^j\\
&+4B_{2}{}^{ab\,ik}\varepsilon_{kj}\gamma_{ab}\chi^j\\
&-\frac{32i}{3}B_{3}{}^{ab\,ik}\varepsilon_{kj}\gamma_{ab}\chi^j\\
&+48iB_{4}{}^{ab\,ik}\varepsilon_{kj}\gamma_{ab}\chi^j\\
&-12iB_{5}{}^{ab\,ik}\varepsilon_{kj}\gamma_{ab}\chi^j\\
&-32iB_{6}{}^{ab\,ik}\varepsilon_{kj}\gamma_{ab}\chi^j\\
&+\frac{64}{3}B_{7}{}^{ab\,ik}\varepsilon_{kj}\gamma_{ab}\chi^j\\
&-\frac{8i}{3}B_{8}{}^{ab\,ik}\varepsilon_{kj}\gamma_{ab}\chi^j\\
&-\frac{64i}{3}B_{9}{}^{ab\,ik}\varepsilon_{kj}\gamma_{ab}\chi^j\\
&-\frac{2}{3}\mathscr V^{ab\,i}{}_{j}\gamma_{ab}D\epsilon^j\\
&+\frac{1}{24}\mathscr V^{ab\,i}{}_{j}\gamma_{ab}\gamma^{cd}\mathscr V_{cd}^{jk}\epsilon_k\\
&-\frac{i}{3}\mathscr V^{ab\,i}{}_{j}\gamma_{ab}\gamma^{cd}\gamma^eU_{e\,cd}\epsilon^j\\
&+\frac{i}{3}\mathscr V^{ab\,i}{}_{j}\gamma_{ab}\gamma^cU^d{}_{cd}\epsilon^j\\
&+\frac{2}{3}\mathscr V^{ab\,i}{}_{j}\gamma_{ab}G_4\epsilon^j\\
&-\frac{4}{9}\mathscr V^{ab\,i}{}_{j}\gamma_{ab}t_2\epsilon^j.
\end{aligned}\tag{P68}
```

The two B5/B8 entries remain separate, preserving their S-curvature and direct-Q origins. The positive $`1/24`$ term is $`(-8/3)(-1/64)`$; it retains the source two-upper-index V and lowered supersymmetry parameter without an unrecorded SU(2) conversion.

## 20. Consistency Checks

### 20.1 Weights, indices and physical fermions

<!-- ASSERT_CONVENTION: natural_units=hbar=c=1, metric_signature=(-,+,+,+,+); master C01, source_lock=UNG-WEYL2-OP58-CONVENTIONS-v5 -->

Before gauge fixing it is the Weyl weights, equivalently the engineering
weights of these covariants, that give the useful dimensional check.
Using $`w(\epsilon)=-1/2`$ and $`w(\mathcal D_a)=1`$, the eleven weights are

```math
\begin{aligned}
(w(F_1),\ldots,w(F_{11}))
=(&\tfrac32+2,\tfrac32+2,\tfrac32+2,
\tfrac52+1,\tfrac52+1,2+\tfrac32,\\
 &2+\tfrac32,\tfrac52+1,\tfrac32+1+1,
 2+\tfrac32,2+\tfrac32)
=(\tfrac72,\ldots,\tfrac72).
\end{aligned}\tag{P69}
```

The intermediate responses preserve their inputs' weights:
$`w(\tau,u,\xi,z,\rho,y,\nu,c)=(1,2,3/2,5/2,3/2,5/2,2,2)`$.
For example $`w(\bar\epsilon\mathscr R)= -1/2+3/2=1`$,
$`w(\mathscr C\epsilon)=2-1/2=3/2`$, and
$`w(\mathscr R\,c)=3/2+2=7/2`$. Thus every displayed term in
$`\delta\varphi_W`$ has weight $`7/2`$, and a bosonic coefficient multiplying
$`\epsilon`$ has weight 4, as required for $`E_a,N`$.

Every $`F_n`$ and $`\mathcal W_n`$ has one free upper $`i`$, no free Lorentz
index, and one suppressed spinor index. In particular the four terms
from the two T variations in (P64) keep the contractions of the two
original T factors distinct. The last term of $`\rho_{ab}`$ can be written
$`\gamma_{ab}\gamma_d\eta^{ce}\eta^{df}U_{c\,ef} =\gamma_{ab}\gamma^d U^c{}_{cd}`$; the renamed versions of that contraction
in the eleven blocks do not mean $`U^c{}_{dc}`$, which would have the
opposite sign. The $`\xi`$ divergence is instead $`\gamma^aU^b{}_{ab}`$,
exactly as W03 requires.

Parity and parameter counting can be checked before any Fierz operation:

```math
\begin{gathered}
|h|=|\beta|=|v|=|\Omega|=|\tau|=|\nu|=|c|=|u|=0,\\
|p|=|\Phi|=|\xi|=|\rho|=|z|=|y|=1,\qquad
|\mathcal W_n|=|\varphi_W|=1,\\
\deg_\epsilon(\mathcal W_n)=1\quad(n=1,\ldots,11).
\end{gathered}\tag{P70}
```

Here parity includes the odd parameter. For example
$`\chi^i(\bar\epsilon K\chi)`$ is odd and linear in $`\epsilon`$, despite
containing two physical $`\chi`$ fields. It is retained in (P52).
Higher physical-fermion orders inside the original hatted quantities,
$`\Phi`$, $`\Pi`$ and the derivative responses are also retained. No proof
step identifies “bosonic coefficient” with “an unhatted ordinary field.”

All antisymmetrizations and SU(2) symmetrizations keep their factors of
$`1/2`$. The antisymmetries of $`\tau_{ab},\rho_{ab},\nu_{ab}`$ and $`c_{ab cd}`$
in their displayed pairs follow termwise from (P09),(P12),(P15),(P29).
The main calculation does **not** impose the purely bosonic pair-exchange
or first-Bianchi symmetries on the fermionic $`\mathscr C`$.

There is no chiral projection in five dimensions. Majorana transposition,
including reversal of gamma products without conjugating $`i`$, is displayed
in (P08),(P22),(P23),(P44). The independent checker tests those gamma
transpose identities. A separate component-level symplectic-Majorana
reality audit of the final Fierz-collected descendants is outside the
scope of this variation calculation. The termwise result is the linear
variation of the adopted symplectic-Majorana composite using the locked
reality-preserving input laws.

### 20.2 Algebraic bosonic check: the $`D^2`$ coefficient

These are **coefficient projections**, not claimed solutions or gauge
choices for the full calculation. In this check set physical fermions,
$`T,U,V,C`$ to zero and retain the algebraic $`D^2`$ monomial. Only the first
term of (P52) contributes:

```math
\left.\delta_Q\varphi_W^i\right|_{D^2}
=\frac{128}{3}\left(\frac14D\epsilon^i\right)D
=\frac{32}{3}D^2\epsilon^i
=\frac12\left(\frac{64}{3}D^2\right)\epsilon^i.
\tag{P71}
```

This matches precisely $`N|_{D^2}=64D^2/3`$ in M04. A zero background value
of $`\varphi`$ would not justify setting its variation to zero.

### 20.3 Algebraic bosonic check: the Weyl-curvature square

Clifford anticommutation with the declared normalization gives

```math
\begin{aligned}
\gamma^{ab}\gamma^{cd}
={}&\gamma^{abcd}+\eta^{bc}\gamma^{ad}-\eta^{ac}\gamma^{bd}
-\eta^{bd}\gamma^{ac}+\eta^{ad}\gamma^{bc}
+\eta^{ad}\eta^{bc}-\eta^{ac}\eta^{bd},\\
\frac12\{\gamma^{ab},\gamma^{cd}\}
={}&\gamma^{abcd}+\eta^{ad}\eta^{bc}-\eta^{ac}\eta^{bd},\\
\gamma^{abcd}&=i\epsilon^{abcde}\gamma_e.
\end{aligned}\tag{P72}
```

In the second line the rank-two terms cancel under exchanging the ordered
pairs $`ab\leftrightarrow cd`$. The last identity follows from the product
$`\gamma^{01234}=i`$; raising/lowering uses the one timelike minus. The
checker evaluates the anticommutator and duality for all 625 ordered
four-index choices, including repeated indices.

At zero physical fermions $`C`$ has the ordinary Weyl symmetries. Define
$`B^{cd,ef}=C^{ab cd}C_{ab}{}^{ef}`$. It is symmetric under exchanging
$`cd,ef`$. Thus its contraction with $`[\gamma_{cd},\gamma_{ef}]`$ is zero:
renaming $`cd\leftrightarrow ef`$ gives the negative of the same contraction.
The fourth term in (P48) therefore gives

```math
\begin{aligned}
\left.\delta_Q\varphi_W^i\right|_{C^2}
&=-\frac1{32}B^{cd,ef}\gamma_{cd}\gamma_{ef}\epsilon^i\\
&=-\frac1{32}B^{cd,ef}
 (\gamma_{cdef}+\eta_{cf}\eta_{de}-\eta_{ce}\eta_{df})\epsilon^i\\
&=\frac1{16}C_{abcd}C^{abcd}\epsilon^i
-\frac1{32}\gamma_{cdef}B^{cd,ef}\epsilon^i\\
&=\frac1{16}C^2\epsilon^i
-\frac i{32}\gamma^a\epsilon_{abcde}
 C^{bcfg}C^{de}{}_{fg}\epsilon^i.
\end{aligned}\tag{P73}
```

For the scalar contraction in the third line,
$`B^{cd,ef}\eta_{cf}\eta_{de}=-C^2`$ and
$`B^{cd,ef}\eta_{ce}\eta_{df}=+C^2`$ by antisymmetry of each curvature pair.
For the last line insert the lowered version of the duality in (P72),
move its fifth epsilon index to the first slot (four interchanges, sign
$`+`$), then rename its contracted pairs and use bosonic Weyl pair exchange.
Consequently the scalar and vector coefficients are

```math
N\big|_{C^2}=\frac18 C^2,\qquad
E_a\big|_{C^2}=\frac1{16}\epsilon_{abcde}C^{bcfg}C^{de}{}_{fg}.
\tag{P74}
```

Both agree with M03–M04. The checker also tests the scalar/rank-four
reduction on a complete two-form polarization set: 10 basis tensors and
45 sums of distinct basis tensors. This verifies the quadratic identity,
not just a single diagonal curvature example.

### 20.4 Algebraic bosonic check: the SU(2)-curvature square

This check must retain matrix ordering until the symmetric Lorentz
contractions have been identified. For symmetric upper-index triplets
$`S,W`$ introduce the explicit matrices

```math
\begin{aligned}
&S=\begin{pmatrix}x&y\\y&z\end{pmatrix},\quad
W=\begin{pmatrix}x'&y'\\y'&z'\end{pmatrix},\quad
\varepsilon=\begin{pmatrix}0&1\\-1&0\end{pmatrix},\\
&\mathsf S=S\varepsilon=\begin{pmatrix}-y&x\\-z&y\end{pmatrix},\quad
W_{ij}=(\varepsilon^TW\varepsilon)_{ij}
=\begin{pmatrix}z'&-y'\\-y'&x'\end{pmatrix}_{ij},\\
&\mathop{\mathrm{tr}}\nolimits(\mathsf S\mathsf W)=2yy'-xz'-zx'=-S^{ij}W_{ij},\\
&\mathsf S\mathsf W+\mathsf W\mathsf S
=(2yy'-xz'-zx')\mathbf1=-S^{ij}W_{ij}\mathbf1.
\end{aligned}\tag{P75}
```

The off-diagonal entries on the last line are, explicitly,
$`-yx'+xy'-y'x+x'y=0`$ and
$`zy'-yz'+z'y-y'z=0`$. The two diagonal entries are both
$`2yy'-xz'-zx'`$. This supplies the triplet identity with the actual NW–SE
sign; replacing it with a guessed positive trace would reverse the result.

Write $`\mathsf V_{ab}{}^i{}_j=V_{ab}^{ik}\varepsilon_{kj}`$ in this check.
Because $`V^{ij}\epsilon_j=-\mathsf V^i{}_j\epsilon^j`$, the V part of
$`\xi`$ is **positive** $`\gamma^{cd}\mathsf V_{cd}\epsilon/64`$.
Only the V part of $`F_{10}`$ and the $`\xi`$ part of $`F_{11}`$ contribute to
the bosonic $`V^2`$ monomial. Raising the contracted tangent indices on the
gammas gives

```math
\begin{aligned}
\left.\delta_Q\varphi_W\right|_{V^2}
={}&\frac1{12}\mathsf V_{ab}\mathsf V_{cd}
 \left(\gamma^{abcd}-\gamma^{cd}\gamma^{ab}
       -\frac12\gamma^{ab}\gamma^{cd}\right)\epsilon
 -\frac1{24}\mathsf V_{ab}\mathsf V_{cd}
       \gamma^{ab}\gamma^{cd}\epsilon\\
={}&\frac1{12}\mathsf V_{ab}\mathsf V_{cd}
 \left(\gamma^{abcd}-\{\gamma^{ab},\gamma^{cd}\}\right)\epsilon\\
={}&-\frac1{12}\gamma^{abcd}\mathsf V_{ab}\mathsf V_{cd}\epsilon
 +\frac13\mathsf V_{ab}\mathsf V^{ab}\epsilon\\
={}&\frac1{24}\gamma^{abcd}V_{ab}^{ij}V_{cd\,ij}\epsilon
 -\frac16 V_{ab}^{ij}V^{ab}{}_{ij}\epsilon\\
={}&-\frac16 V_{ab}^{ij}V^{ab}{}_{ij}\epsilon
 +\frac i{24}\gamma^a\epsilon_{abcde}V^{bc\,ij}V^{de}{}_{ij}\epsilon.
\end{aligned}\tag{P76}
```

The first line displays the two independently varied terms. In the second
line their two coefficients of $`\gamma^{ab}\gamma^{cd}`$ add. The third
uses (P72) and
$`(\eta^{ad}\eta^{bc}-\eta^{ac}\eta^{bd})\mathsf V_{ab}\mathsf V_{cd} =-2\mathsf V_{ab}\mathsf V^{ab}`$. Both contractions on that third line
are symmetric under exchanging the two Lorentz pairs, so each SU(2)
matrix product can be replaced by half its anticommutator in (P75).
Only at that point does it become an SU(2) singlet. The last line uses
the same rank-four duality and index raising as in (P73). Hence

```math
N\big|_{V^2}=-\frac13V_{ab}^{ij}V^{ab}{}_{ij},\qquad
E_a\big|_{V^2}=-\frac1{12}\epsilon_{abcde}V^{bc\,ij}V^{de}{}_{ij}.
\tag{P77}
```

These match M03–M04. The checker evaluates the original two contributions
on all 30 independent two-form/triplet components and their 435 pair sums.
It compares all entries of the resulting $`8\times8`$ spinor-doublet
matrices, including the noncommuting SU(2) products. Thus an Abelian-only
substitution was not used to obtain this check.

### 20.5 Local covariance, limits, and bounded computer checks

Equations (P41)–(P46) explicitly cancel every derivative of the arbitrary
local parameter; no assumption of constant $`\epsilon`$ was made. The
connection/frame terms in (P20),(P28),(P29),(P31),(P34),(P37) preserve the
Lorentz, dilatation and SU(2) tensor types because they are derivatives of
the complete defining tensors. This is a covariance check on the variation,
not a claim that the full composite already obeys its desired S/Q multiplet
laws. Physical $`g=0`$ is built into the inputs; $`V_\mu`$ and its products
were retained throughout.

On the flat zero-covariant configuration all eleven blocks vanish:

```math
\left.\delta_Q\varphi_W^i\right|_{
T=D=\mathscr C=\mathscr V=\mathscr R=\chi=\psi=0,
\ U=Y=Z=0}=0.
\tag{P78}
```

Every term of (P48)–(P68) has at least one of these zero factors after
using its response definitions. Equations (P71),(P73),(P76) separately
show why setting **only** physical fermions to zero does not make the
variation zero. The checks use no background equation. No boundary term
exists in this pointwise calculation: no integration by parts or dropping
of a total derivative occurred.

The independent script is
[verify_weyl_spinor_q_variation.py](../src/reference_checks/verify_weyl_spinor_q_variation.py)
The reproducible command from the repository root is

```bash
python3 -B computations/weyl_fermionic/checks/reference_suite.py --check verify_weyl_spinor_q_variation
```

The runner generates `VARPHI-Q-VARIATION-CHECKS.json` in its temporary
workspace and prints the result; it does not save that report beside this document.
It records the proof and ledger hashes and the following bounded checks:

| Check | Coverage |
|---|---|
| Even product rule and coefficients | All 94 outer coefficients, using exact rational real/imaginary parts |
| Repeated factors | Both factors of $`T^2`$ and both distinct T factors of $`F_9`$ |
| Gamma algebra and duality | All 625 ordered four-index choices |
| Curvature derivative-parameter flip | All 625 choices in $`\widetilde{\gamma^{[a}K\gamma^{b]}}=\gamma^{[a}K\gamma^{b]}`$ |
| Weyl-square algebra | Complete 10+45 two-form polarization set |
| SU(2) signs | All nine symmetric-triplet basis pairs |
| Full V-square matrices | Complete 30+435 polarization set, separate $`F_{10},F_{11}`$ |
| Local-parameter coefficients | Five Lorentz-curvature cancellation groups and both finite $`u`$ remainders |
| Document coverage | Required sections, equation tags, all ledger expressions and control-character scan |

The exact matrix checks use Gaussian-integer entries or exactly represented
binary halves. The largest checked final matrix entry is 48, well below
$`2^{53}`$. No tolerance or rounded approximate equality is used. The script
does **not** supply a nonlinear Fierz proof, reconstruct E/N, or certify
multiplet closure. Those tasks must not be inferred from its PASS.

## 21. Final Result

Under P-A1–P-A7, with the adopted spinor M08 and the v5 input lock,

```math
\boxed{\displaystyle
\delta_Q\varphi_W^i=\sum_{n=1}^{11}\mathcal W_n^i,
\qquad
\mathcal W_n^i\text{ given explicitly in (P48),(P50),\ldots,(P68)}.}
\tag{P79}
```

This is an exact uncollected expression in complete Standard-Weyl
covariants. The 94-term outer expansion is accompanied by all shared
response polynomials, not an unevaluated variation prescription. Its
substitution order is finite:

| Needed expression | Explicit input, in substitution order |
|---|---|
| Elementary responses | (P06)–(P12), nine bilinears (P14), curvature response (P15) |
| S-connection response $`\Phi`$ | (P16)–(P23); primed curvature has no $`\phi`$ dependence |
| Weyl-curvature response $`c`$ | (P24)–(P29); primed curvature has no $`f`$ dependence |
| T derivative response $`u`$ | (P31)–(P32), using only the preceding responses |
| $`\chi`$ derivative response $`z`$ | (P34)–(P35), using $`u,\nu,\Phi`$ |
| Gravitino-curvature derivative response $`y`$ | (P37)–(P38), using $`u,c,\nu,\Phi`$ |
| Eleven final blocks | (P48)–(P68), with those polynomials substituted wherever their names occur |

No response on this list depends on its own variation, or on a response
later in the list. Original fields and original covariant derivatives are
allowed on the right; they are explicitly defined by P01/G01/W04/R01–R03.
All 94 outer terms and their rational coefficients are also stored in
[VARPHI-Q-TERM-LEDGER.json](../inputs/component_ledgers/VARPHI-Q-TERM-LEDGER.json) for checking and subsequent collection.

The exact linear-multiplet matching operation to perform next is

```math
\mathscr X^i:=\sum_{n=1}^{11}\mathcal W_n^i
+\frac i2\gamma^a\mathcal D_aL_W^{ij}\epsilon_j
+K L_W^{ij}\epsilon_j,
\qquad
\mathscr X^i\ \stackrel{\text{to be checked}}{=}
\frac12N_W\epsilon^i-\frac i2\gamma^aE_{Wa}\epsilon^i.
\tag{P80}
```

The derivative of $`L_W`$ on this line is the full derivative L02, and the
left side must undergo the complete Clifford, Fierz and SU(2) reduction.
It is not permissible to discard a structure that fails to fit the right
side. The three algebraic bosonic sectors checked above agree with their
printed M03–M04 coefficients; that agreement is narrower than the complete
matching requested by the construction programme.

## 22. Convention Dependence and Remaining Uncertainties

- This calculation uses **M08 with $`8/3`$**, not literal M02 with $`16/3`$.
  It does not resolve the original source discrepancy by assumption and
  does not certify all transformation laws merely because the user adopted
  the working expression.
- The termwise Q-variation is complete in the explicit polynomial form
  above. Parts IV–VIII carry out the Clifford/Fierz collection of (P80)
  and extract the singlet $`E_a,N`$ expressions. The S-law of the adopted
  spinor is outside this calculation.
- Independent $`\delta E`$, $`\delta N`$ and full supercovariant-divergence
  checks are outside this calculation. The [component action](full-fermionic-weyl2-action.md)
  and [AdS5 spectrum](../../../weyl2/ads5/README.md) have their own derivations.
- The result is conditional on the operational W/G/R laws in the master.
  No new transformation-law correction or convention change has been
  introduced in Part III. A later input repair requires rerunning the
  affected derivation, not just changing its recorded lock label.
- There is no perturbative approximation or omitted fermion remainder in
  Part III, hence no truncation error estimate. Gamma products and spinor
  pairings are deliberately left in their displayed order until the next
  collection stage. The independent checks have precisely the scope
  stated in Section 20.5; unperformed closure and reality checks remain
  explicitly unperformed.

---

# Part IV — Direct hand calculation of the epsilon-i terms

## 23. Problem and Target

This part replaces the coefficient-array presentation at the user's request.
We use the original fields and ordinary spinor algebra. In particular,
$`\widehat R(Q)_{ab}`$ below is the gravitino curvature, and
$`\widehat R(V)_{ab}^{ij}`$ is the SU(2) curvature. These are the same source
objects usually written $`\widehat R_{ab}(Q)`$ and $`\widehat R_{ab}^{ij}(V)`$;
no new fields are being defined. $`T^2=T_{ab}T^{ab}`$ and
$`\gamma\!\cdot\!T=\gamma^{ab}T_{ab}`$ are the source's contractions.
We write the derivatives $`\mathcal D_aT_{bc}`$, $`\mathcal D_a\chi`$, and
$`\mathcal D_a\widehat R(Q)_{bc}`$ explicitly instead of renaming them.

The task is to keep the SU(2)-identity coefficient multiplying
$`\epsilon^i`$, including its gamma-matrix structures. We first perform
Fierz and Schouten; only then may a traceless doublet matrix be excluded.
The notation $`F_1,\ldots,F_{11}`$ labels the original eleven summands of
M08, not additional fields.

Sections 26–28 give the physical-field Fierz calculations for all nonzero
singlet origins, including the six curvature/derivative contributions in H50.
The complete sum retains the physical fields explicitly.

The input is M08 with its adopted $`8/3`$ ninth coefficient, together with
the unchanged v5 C/W/G/R laws. Work is off shell, before gauge fixing,
at physical $`g=0`$. All physical fermion orders in the hatted curvatures
and full derivatives remain. No field equation, integration by parts,
background, derivative interchange, or fermion truncation is used.

## 24. Convention Ledger

<!-- ASSERT_CONVENTION: natural_units=hbar=c=1, metric_signature=(-,+,+,+,+); master C01, source_lock=UNG-WEYL2-OP58-CONVENTIONS-v5 -->

Use master C01–C05: $`\eta=(-,+,+,+,+)`$, $`a=0,\ldots,4`$, $`i=1,2`$;
$`\gamma^{01234}=i`$, $`\epsilon^{01234}=1`$, weighted antisymmetrization,
and full ordered-pair contractions. The Majorana bar is linear, including
$`\overline{i\chi}=i\bar\chi`$. All physical spinors and $`\epsilon`$ are
odd, while the parameterized $`\delta_Q`$ is even. Raising and lowering are
$`w_i=w^j\varepsilon_{ji}`$ and
$`V^i{}_j=V^{ik}\varepsilon_{kj}`$, with
$`\varepsilon_{12}=\varepsilon^{12}=1`$.

Only inside the derivation of the Fierz identity, $`u,v`$ denote arbitrary
odd test spinors and $`M`$ a specified gamma product. They are replaced by
the actual physical spinors in every application below. $`p,q`$ are dummy
Lorentz indices for the Fierz basis, distinct from the indices in each
original term. A suppressed doublet contraction means
$`\bar u Mv=\bar u^jMv_j`$.

## 25. Definitions and Required Identities

### 25.1 Move the parameter to the right, keeping the odd signs

The complete five-dimensional matrix basis is
$`1,\gamma^a,\gamma^{ab}`$, with $`1+5+10=16`$ independent entries. Its norms
are

```math
\mathop{\mathrm{tr}}\nolimits1=4,\quad
\mathop{\mathrm{tr}}\nolimits(\gamma^a\gamma^b)=4\eta^{ab},\quad
\mathop{\mathrm{tr}}\nolimits(\gamma^{ab}\gamma^{cd})
=4(\eta^{ad}\eta^{bc}-\eta^{ac}\eta^{bd}).
\tag{H01}
```

For an odd column $`u`$ and row $`\bar v`$,
$`\mathop{\mathrm{tr}}\nolimits(u\bar v)=-\bar vu`$. Inserting the complete basis gives

```math
u\bar v=-\tfrac14(\bar vu)
-\tfrac14(\bar v\gamma_pu)\gamma^p
+\tfrac18(\bar v\gamma_{pq}u)\gamma^{pq}.
\tag{H02}
```

The first two minus signs are the odd interchange. The rank-two trace
norm supplies the additional minus giving the last plus. The last
coefficient is $`1/8`$, since the sum runs over both $`(p,q)`$ and $`(q,p)`$.

For the fixed-index Majorana flip, transpose the full gamma product:
$`\bar\epsilon^jMv^k=\bar v^k\widetilde M\epsilon^j`$, where
$`\widetilde M=\mathsf C^{-1}M^T\mathsf C`$. This is the conventional
Majorana transpose, not a new algebraic operation. Its needed values are

```math
\widetilde1=1,\quad \widetilde{\gamma_a}=\gamma_a,\quad
\widetilde{\gamma_{ab}}=-\gamma_{ab},\quad
\widetilde{\gamma\!\cdot\!T}=-\gamma\!\cdot\!T,\quad
\widetilde{\gamma_d\gamma_a}=\gamma_a\gamma_d,\quad
\widetilde{\gamma_{[a}(\gamma\!\cdot\!T)\gamma_{b]}}
=\gamma_{[a}(\gamma\!\cdot\!T)\gamma_{b]}.
\tag{H03}
```

For a contracted parameter bilinear, lowering its index gives

```math
\begin{aligned}
u^i(\bar\epsilon Mv)
 &=u^i\bar v_j\widetilde M\epsilon^j\\
 &=-\tfrac14(\bar v_j\widetilde Mu^i)\epsilon^j
   -\tfrac14(\bar v_j\widetilde M\gamma_pu^i)\gamma^p\epsilon^j
   +\tfrac18(\bar v_j\widetilde M\gamma_{pq}u^i)\gamma^{pq}\epsilon^j.
\end{aligned}\tag{H04}
```

Now decompose each doublet coefficient into its identity and traceless
parts: $`A^i{}_j=\delta^i_jA^k{}_k/2+ (A^i{}_j-\delta^i_jA^k{}_k/2)`$. Use
$`\bar v_j\Gamma u^j=-\bar v\Gamma u`$. The requested part of H04 is

```math
\left.u^i(\bar\epsilon Mv)\right|_{\epsilon^i}
=\tfrac18(\bar v\widetilde Mu)\epsilon^i
+\tfrac18(\bar v\widetilde M\gamma_pu)\gamma^p\epsilon^i
-\tfrac1{16}(\bar v\widetilde M\gamma_{pq}u)\gamma^{pq}\epsilon^i.
\tag{H05}
```

The suffix here and below means the SU(2)-identity coefficient, not
setting $`j=i`$ without summation. In particular, a traceless matrix can
have nonzero diagonal entries.

### 25.2 The Schouten step in the symmetric-triplet pairing

Expand the symmetrization before applying H02:

```math
\begin{aligned}
\bar\epsilon^{(i}Mv^{k)}\varepsilon_{kl}u^l
 &=\tfrac12u^l(\bar v^k\widetilde M\epsilon^i
                  +\bar v^i\widetilde M\epsilon^k)\varepsilon_{kl}\\
 &=-\tfrac12\left(\delta^i_j u_k\bar v^k\widetilde M
                          +u_j\bar v^i\widetilde M\right)\epsilon^j.
\end{aligned}\tag{H06}
```

The minus is $`\varepsilon_{kl}u^l=-u_k`$. Fierz each dyad by H02.
For its scalar singlet the two terms give

```math
\tfrac1{16}\big(2\bar v^k\widetilde Mu_k+
                     \bar v^i\widetilde Mu_i\big)
=\tfrac3{16}\bar v\widetilde Mu.
\tag{H07}
```

Doing the same two contractions with $`\gamma_pu`$ and $`\gamma_{pq}u`$
gives the complete retained expression

```math
\left.\bar\epsilon^{(i}Mv^{k)}\varepsilon_{kl}u^l\right|_{\epsilon^i}
=\tfrac3{16}(\bar v\widetilde Mu)\epsilon^i
+\tfrac3{16}(\bar v\widetilde M\gamma_pu)\gamma^p\epsilon^i
-\tfrac3{32}(\bar v\widetilde M\gamma_{pq}u)\gamma^{pq}\epsilon^i.
\tag{H08}
```

Thus this pairing is $`3/2`$ times H05. The factor is an SU(2) result,
not a gamma-matrix multiplicity. Equivalently, lowering the open doublet
index splits a two-index object into an antisymmetric singlet and a
symmetric triplet; antisymmetrizing three SU(2) indices vanishes.

For two symmetric triplets,

```math
\tfrac12 V^i{}_jW^j{}_i=-\tfrac12 V^{ij}W_{ij}.
\tag{H09}
```

For example $`V^{ij}=\left(\begin{smallmatrix}a&b\\b&c\end{smallmatrix}\right)`$,
$`W^{ij}=\left(\begin{smallmatrix}d&e\\e&f\end{smallmatrix}\right)`$ give
$`\mathop{\mathrm{tr}}\nolimits(VW)=2be-af-cd=-V^{ij}W_{ij}`$ in the mixed convention.
A single curvature has zero trace; a product of two curvatures must remain.

### 25.3 Ordinary gamma products

We use the usual products, without defining a custom product on coefficients:

```math
\begin{aligned}
\gamma^{ab}\gamma^c&=\gamma^{abc}+\eta^{bc}\gamma^a-\eta^{ac}\gamma^b,\\
\gamma^{ab}\gamma^{cd}&=\gamma^{abcd}
+\eta^{bc}\gamma^{ad}-\eta^{ac}\gamma^{bd}
-\eta^{bd}\gamma^{ac}+\eta^{ad}\gamma^{bc}
+\eta^{ad}\eta^{bc}-\eta^{ac}\eta^{bd},\\
\gamma^{abc}&=-\tfrac i2\epsilon^{abcde}\gamma_{de},\qquad
\gamma^{abcd}=i\epsilon^{abcde}\gamma_e.
\end{aligned}\tag{H10}
```

A gamma string still displayed below is its ordinary ordered product.
It is not an encoded coefficient array. Full reduction and collection of
all such strings has not been inferred from a computational check.

The spinor laws inserted below, written without response-field aliases, are

```math
\begin{aligned}
\delta_Q\chi^i={}&\tfrac14D\epsilon^i
-\tfrac1{64}\gamma^{ab}\widehat R(V)_{ab}^{ij}\epsilon_j
+\tfrac i8\gamma^{ab}\gamma^c(\mathcal D_cT_{ab})\epsilon^i
-\tfrac i8\gamma^a(\mathcal D^bT_{ab})\epsilon^i\\
&-\tfrac14\gamma^{abcd}T_{ab}T_{cd}\epsilon^i
+\tfrac16T^2\epsilon^i,\\
\delta_QD={}&\bar\epsilon\gamma^a\mathcal D_a\chi
-\tfrac{5i}{3}\bar\epsilon(\gamma\!\cdot\!T)\chi.
\end{aligned}\tag{H11}
```

The gravitino-curvature law is master R05:

```math
\begin{aligned}
\delta_Q\widehat R(Q)_{ab}^i={}&
\tfrac16\gamma_{ab}{}^{cd}\widehat R(V)_{cd}{}^i{}_j\epsilon^j
-\tfrac16\gamma^{cd}\gamma_{ab}\widehat R(V)_{cd}{}^i{}_j\epsilon^j
-\tfrac1{12}\gamma_{ab}\gamma^{cd}\widehat R(V)_{cd}{}^i{}_j\epsilon^j\\
&+\tfrac14\widehat C_{ab}{}^{cd}\gamma_{cd}\epsilon^i
+2i\gamma^{cd}(\mathcal D_{[a}T_{cd})\gamma_{b]}\epsilon^i
-\tfrac{2i}{3}\gamma_{[b}\gamma^{cd}(\mathcal D_{a]}T_{cd})\epsilon^i\\
&-\tfrac{2i}{3}\gamma_{[a}\gamma^f\gamma^{cd}
 (\mathcal D_fT_{cd})\gamma_{b]}\epsilon^i
-\tfrac{2i}{3}\gamma_{ab}\gamma^d(\mathcal D^cT_{cd})\epsilon^i.
\end{aligned}\tag{H12}
```

The first three terms are traceless on their own, but must be retained
when another SU(2) curvature multiplies this law in term 10.

## 26. Detailed Derivation

Each subsection keeps the original term visible, writes its product rule,
then inserts the source variations and displays the actual Fierz bilinears.
Curvatures, derivatives, and their hidden physical fermions are retained.

### 26.1. Original term 1

```math
F_{1}^i=-\tfrac18\gamma_{cd}\widehat R(Q)_{ab}^i\widehat C^{abcd}.\tag{H13}
```

Vary each factor. Since $`\delta_Q`$ is even, this step introduces no extra Grassmann sign:

```math
\delta_QF_{1}^i=-\tfrac18\gamma_{cd}(\delta_Q\widehat R(Q)_{ab}^i)\widehat C^{abcd}-\tfrac18\gamma_{cd}\widehat R(Q)_{ab}^i\delta_Q\widehat C^{abcd}.\tag{H14}
```

Adding the explicitly evaluated contributions in this subsection gives

```math
\begin{aligned}

-\frac{1}{32}\gamma_{cd} \gamma_{ef}\widehat C_{ab}{}^{ef}\widehat C^{abcd}\epsilon^i\\
&-\frac{i}{4}\gamma_{cd} \gamma^{ef} \gamma_{b]}(\mathcal D_{[a}T_{ef})\widehat C^{abcd}\epsilon^i\\
&+\frac{i}{12}\gamma_{cd} \gamma_{[b} \gamma^{ef}(\mathcal D_{a]}T_{ef})\widehat C^{abcd}\epsilon^i\\
&+\frac{i}{12}\gamma_{cd} \gamma_{[a} \gamma^{g} \gamma^{ef} \gamma_{b]}(\mathcal D_gT_{ef})\widehat C^{abcd}\epsilon^i\\
&+\frac{i}{12}\gamma_{cd} \gamma_{ab} \gamma^{e}(\mathcal D^fT_{fe})\widehat C^{abcd}\epsilon^i
.
\end{aligned}\tag{H15}
```

The other product-rule contribution is retained as

```math
-\tfrac18\gamma_{cd}\widehat R(Q)_{ab}^i\delta_Q\widehat C^{abcd}.
```
Its full uncollected expansion is P24–P29. Its remaining parameter factorization is tracked in Section 27; it is **not** included in the preceding direct terms and is not claimed to vanish.

The discarded single-curvature origins are R1, R2, R3: their SU(2) coefficient is traceless. No bilinear was discarded before H05/H08.

### 26.2. Original term 2

```math
F_{2}^i=-4i\gamma_c\widehat R(Q)_{ab}^i\mathcal D^aT^{bc}.\tag{H16}
```

Vary each factor. Since $`\delta_Q`$ is even, this step introduces no extra Grassmann sign:

```math
\delta_QF_{2}^i=-4i\gamma_c(\delta_Q\widehat R(Q)_{ab}^i)\mathcal D^aT^{bc}-4i\gamma_c\widehat R(Q)_{ab}^i\delta_Q(\mathcal D^aT^{bc}).\tag{H17}
```

Adding the explicitly evaluated contributions in this subsection gives

```math
\begin{aligned}

-i\gamma_c \gamma_{de}\widehat C_{ab}{}^{de}(\mathcal D^aT^{bc})\epsilon^i\\
&+8\gamma_c \gamma^{de} \gamma_{b]}(\mathcal D_{[a}T_{de})(\mathcal D^aT^{bc})\epsilon^i\\
&-\frac{8}{3}\gamma_c \gamma_{[b} \gamma^{de}(\mathcal D_{a]}T_{de})(\mathcal D^aT^{bc})\epsilon^i\\
&-\frac{8}{3}\gamma_c \gamma_{[a} \gamma^{f} \gamma^{de} \gamma_{b]}(\mathcal D_fT_{de})(\mathcal D^aT^{bc})\epsilon^i\\
&-\frac{8}{3}\gamma_c \gamma_{ab} \gamma^{d}(\mathcal D^eT_{ed})(\mathcal D^aT^{bc})\epsilon^i
.
\end{aligned}\tag{H18}
```

The other product-rule contribution is retained as

```math
-4i\gamma_c\widehat R(Q)_{ab}^i\delta_Q(\mathcal D^aT^{bc}).
```
Its full uncollected expansion is P30–P32. Its remaining parameter factorization is tracked in Section 27; it is **not** included in the preceding direct terms and is not claimed to vanish.

The discarded single-curvature origins are R1, R2, R3: their SU(2) coefficient is traceless. No bilinear was discarded before H05/H08.

### 26.3. Original term 3

```math
F_{3}^i=\tfrac{128}{3}\chi^iD.\tag{H19}
```

Vary each factor. Since $`\delta_Q`$ is even, this step introduces no extra Grassmann sign:

```math
\delta_QF_{3}^i=\tfrac{128}{3}(\delta_Q\chi^i)D+\tfrac{128}{3}\chi^i\delta_QD.\tag{H20}
```

The needed elementary laws are $`\delta_QT_{ab}=i\bar\epsilon\gamma_{ab}\chi/2-3i\bar\epsilon\widehat R(Q)_{ab}/32`$, together with W03 for $`\delta_Q\chi`$ and $`\delta_QD`$. The factor varied is visible in the product rule above.

Insert the actual spinors into H05. The scalar coefficient is $`(\frac{128}{3})(1)(1/8)=\frac{16}{3}`$; the vector has the same factor and the bivector has minus one half of it:

```math
\begin{aligned}
\left.\frac{128}{3}(\chi)^i(\bar\epsilon \gamma^a\mathcal D_a\chi)\right|_{\epsilon^i}&=\frac{16}{3}\big(\overline{\mathcal D_a\chi}\gamma^a\chi\big)\epsilon^i\\
&+\frac{16}{3}\big(\overline{\mathcal D_a\chi}\gamma^a\gamma_p\chi\big)\gamma^p\epsilon^i\\
&-\frac{8}{3}\big(\overline{\mathcal D_a\chi}\gamma^a\gamma_{pq}\chi\big)\gamma^{pq}\epsilon^i .
\end{aligned}
```

Insert the actual spinors into H05. The scalar coefficient is $`(-\frac{640i}{9})(-1)(1/8)=\frac{80i}{9}`$; the vector has the same factor and the bivector has minus one half of it:

```math
\begin{aligned}
\left.-\frac{640i}{9}(\chi)^i(\bar\epsilon (\gamma\!\cdot\!T)\chi)\right|_{\epsilon^i}&=\frac{80i}{9}\big(\bar\chi(\gamma\!\cdot\!T)\chi\big)\epsilon^i\\
&+\frac{80i}{9}\big(\bar\chi(\gamma\!\cdot\!T)\gamma_p\chi\big)\gamma^p\epsilon^i\\
&-\frac{40i}{9}\big(\bar\chi(\gamma\!\cdot\!T)\gamma_{pq}\chi\big)\gamma^{pq}\epsilon^i .
\end{aligned}
```

Adding the explicitly evaluated contributions in this subsection gives

```math
\begin{aligned}

\frac{32}{3}D^2\epsilon^i\\
&+\frac{16i}{3}\gamma^{ab} \gamma^{c}(\mathcal D_cT_{ab})D\epsilon^i\\
&-\frac{16i}{3}\gamma^{a}(\mathcal D^bT_{ab})D\epsilon^i\\
&-\frac{32}{3}D\gamma^{rstu}T_{rs}T_{tu}\epsilon^i\\
&+\frac{64}{9}T^2D\epsilon^i\\
&+\frac{16}{3}\big(\overline{\mathcal D_a\chi}\gamma^a\chi\big)\epsilon^i\\
&+\frac{16}{3}\big(\overline{\mathcal D_a\chi}\gamma^a\gamma_p\chi\big)\gamma^p\epsilon^i\\
&-\frac{8}{3}\big(\overline{\mathcal D_a\chi}\gamma^a\gamma_{pq}\chi\big)\gamma^{pq}\epsilon^i\\
&+\frac{80i}{9}\big(\bar\chi(\gamma\!\cdot\!T)\chi\big)\epsilon^i\\
&+\frac{80i}{9}\big(\bar\chi(\gamma\!\cdot\!T)\gamma_p\chi\big)\gamma^p\epsilon^i\\
&-\frac{40i}{9}\big(\bar\chi(\gamma\!\cdot\!T)\gamma_{pq}\chi\big)\gamma^{pq}\epsilon^i
.
\end{aligned}\tag{H21}
```

The discarded single-curvature origins are chi2: their SU(2) coefficient is traceless. No bilinear was discarded before H05/H08.

### 26.4. Original term 4

```math
F_{4}^i=8i\gamma_c(\mathcal D^c\widehat R(Q)_{ab}^i)T^{ab}.\tag{H22}
```

Vary each factor. Since $`\delta_Q`$ is even, this step introduces no extra Grassmann sign:

```math
\delta_QF_{4}^i=8i\gamma_cT^{ab}\delta_Q(\mathcal D^c\widehat R(Q)_{ab}^i)+8i\gamma_c(\mathcal D^c\widehat R(Q)_{ab}^i)\delta_QT^{ab}.\tag{H23}
```

The needed elementary laws are $`\delta_QT_{ab}=i\bar\epsilon\gamma_{ab}\chi/2-3i\bar\epsilon\widehat R(Q)_{ab}/32`$, together with W03 for $`\delta_Q\chi`$ and $`\delta_QD`$. The factor varied is visible in the product rule above.

Insert the actual spinors into H05. The scalar coefficient is $`(-4)(-1)(1/8)=\frac{1}{2}`$; the vector has the same factor and the bivector has minus one half of it:

```math
\begin{aligned}
\left.-4(\gamma_c\mathcal D^c\widehat R(Q)_{ab})^i(\bar\epsilon \gamma^{ab}\chi)\right|_{\epsilon^i}&=\frac{1}{2}\big(\bar\chi\gamma^{ab}\gamma_c\mathcal D^c\widehat R(Q)_{ab}\big)\epsilon^i\\
&+\frac{1}{2}\big(\bar\chi\gamma^{ab}\gamma_p\gamma_c\mathcal D^c\widehat R(Q)_{ab}\big)\gamma^p\epsilon^i\\
&-\frac{1}{4}\big(\bar\chi\gamma^{ab}\gamma_{pq}\gamma_c\mathcal D^c\widehat R(Q)_{ab}\big)\gamma^{pq}\epsilon^i .
\end{aligned}
```

Insert the actual spinors into H05. The scalar coefficient is $`(\frac{3}{4})(1)(1/8)=\frac{3}{32}`$; the vector has the same factor and the bivector has minus one half of it:

```math
\begin{aligned}
\left.\frac{3}{4}(\gamma_c\mathcal D^c\widehat R(Q)_{ab})^i(\bar\epsilon 1\widehat R(Q)^{ab})\right|_{\epsilon^i}&=\frac{3}{32}\big(\overline{\widehat R(Q)}^{ab}\gamma_c\mathcal D^c\widehat R(Q)_{ab}\big)\epsilon^i\\
&+\frac{3}{32}\big(\overline{\widehat R(Q)}^{ab}\gamma_p\gamma_c\mathcal D^c\widehat R(Q)_{ab}\big)\gamma^p\epsilon^i\\
&-\frac{3}{64}\big(\overline{\widehat R(Q)}^{ab}\gamma_{pq}\gamma_c\mathcal D^c\widehat R(Q)_{ab}\big)\gamma^{pq}\epsilon^i .
\end{aligned}
```

Adding the explicitly evaluated contributions in this subsection gives

```math
\begin{aligned}

\frac{1}{2}\big(\bar\chi\gamma^{ab}\gamma_c\mathcal D^c\widehat R(Q)_{ab}\big)\epsilon^i\\
&+\frac{1}{2}\big(\bar\chi\gamma^{ab}\gamma_p\gamma_c\mathcal D^c\widehat R(Q)_{ab}\big)\gamma^p\epsilon^i\\
&-\frac{1}{4}\big(\bar\chi\gamma^{ab}\gamma_{pq}\gamma_c\mathcal D^c\widehat R(Q)_{ab}\big)\gamma^{pq}\epsilon^i\\
&+\frac{3}{32}\big(\overline{\widehat R(Q)}^{ab}\gamma_c\mathcal D^c\widehat R(Q)_{ab}\big)\epsilon^i\\
&+\frac{3}{32}\big(\overline{\widehat R(Q)}^{ab}\gamma_p\gamma_c\mathcal D^c\widehat R(Q)_{ab}\big)\gamma^p\epsilon^i\\
&-\frac{3}{64}\big(\overline{\widehat R(Q)}^{ab}\gamma_{pq}\gamma_c\mathcal D^c\widehat R(Q)_{ab}\big)\gamma^{pq}\epsilon^i
.
\end{aligned}\tag{H24}
```

The other product-rule contribution is retained as

```math
8i\gamma_cT^{ab}\delta_Q(\mathcal D^c\widehat R(Q)_{ab}^i).
```
Its full uncollected expansion is P36–P38. Its remaining parameter factorization is tracked in Section 27; it is **not** included in the preceding direct terms and is not claimed to vanish.

### 26.5. Original term 5

```math
F_{5}^i=8i\gamma_a(\mathcal D^c\widehat R(Q)_{bc}^i)T^{ab}.\tag{H25}
```

Vary each factor. Since $`\delta_Q`$ is even, this step introduces no extra Grassmann sign:

```math
\delta_QF_{5}^i=8i\gamma_aT^{ab}\delta_Q(\mathcal D^c\widehat R(Q)_{bc}^i)+8i\gamma_a(\mathcal D^c\widehat R(Q)_{bc}^i)\delta_QT^{ab}.\tag{H26}
```

The needed elementary laws are $`\delta_QT_{ab}=i\bar\epsilon\gamma_{ab}\chi/2-3i\bar\epsilon\widehat R(Q)_{ab}/32`$, together with W03 for $`\delta_Q\chi`$ and $`\delta_QD`$. The factor varied is visible in the product rule above.

Insert the actual spinors into H05. The scalar coefficient is $`(-4)(-1)(1/8)=\frac{1}{2}`$; the vector has the same factor and the bivector has minus one half of it:

```math
\begin{aligned}
\left.-4(\gamma_a\mathcal D^c\widehat R(Q)_{bc})^i(\bar\epsilon \gamma^{ab}\chi)\right|_{\epsilon^i}&=\frac{1}{2}\big(\bar\chi\gamma^{ab}\gamma_a\mathcal D^c\widehat R(Q)_{bc}\big)\epsilon^i\\
&+\frac{1}{2}\big(\bar\chi\gamma^{ab}\gamma_p\gamma_a\mathcal D^c\widehat R(Q)_{bc}\big)\gamma^p\epsilon^i\\
&-\frac{1}{4}\big(\bar\chi\gamma^{ab}\gamma_{pq}\gamma_a\mathcal D^c\widehat R(Q)_{bc}\big)\gamma^{pq}\epsilon^i .
\end{aligned}
```

Insert the actual spinors into H05. The scalar coefficient is $`(\frac{3}{4})(1)(1/8)=\frac{3}{32}`$; the vector has the same factor and the bivector has minus one half of it:

```math
\begin{aligned}
\left.\frac{3}{4}(\gamma_a\mathcal D^c\widehat R(Q)_{bc})^i(\bar\epsilon 1\widehat R(Q)^{ab})\right|_{\epsilon^i}&=\frac{3}{32}\big(\overline{\widehat R(Q)}^{ab}\gamma_a\mathcal D^c\widehat R(Q)_{bc}\big)\epsilon^i\\
&+\frac{3}{32}\big(\overline{\widehat R(Q)}^{ab}\gamma_p\gamma_a\mathcal D^c\widehat R(Q)_{bc}\big)\gamma^p\epsilon^i\\
&-\frac{3}{64}\big(\overline{\widehat R(Q)}^{ab}\gamma_{pq}\gamma_a\mathcal D^c\widehat R(Q)_{bc}\big)\gamma^{pq}\epsilon^i .
\end{aligned}
```

Adding the explicitly evaluated contributions in this subsection gives

```math
\begin{aligned}

\frac{1}{2}\big(\bar\chi\gamma^{ab}\gamma_a\mathcal D^c\widehat R(Q)_{bc}\big)\epsilon^i\\
&+\frac{1}{2}\big(\bar\chi\gamma^{ab}\gamma_p\gamma_a\mathcal D^c\widehat R(Q)_{bc}\big)\gamma^p\epsilon^i\\
&-\frac{1}{4}\big(\bar\chi\gamma^{ab}\gamma_{pq}\gamma_a\mathcal D^c\widehat R(Q)_{bc}\big)\gamma^{pq}\epsilon^i\\
&+\frac{3}{32}\big(\overline{\widehat R(Q)}^{ab}\gamma_a\mathcal D^c\widehat R(Q)_{bc}\big)\epsilon^i\\
&+\frac{3}{32}\big(\overline{\widehat R(Q)}^{ab}\gamma_p\gamma_a\mathcal D^c\widehat R(Q)_{bc}\big)\gamma^p\epsilon^i\\
&-\frac{3}{64}\big(\overline{\widehat R(Q)}^{ab}\gamma_{pq}\gamma_a\mathcal D^c\widehat R(Q)_{bc}\big)\gamma^{pq}\epsilon^i
.
\end{aligned}\tag{H27}
```

The other product-rule contribution is retained as

```math
8i\gamma_aT^{ab}\delta_Q(\mathcal D^c\widehat R(Q)_{bc}^i).
```
Its full uncollected expansion is P36–P38. Its remaining parameter factorization is tracked in Section 27; it is **not** included in the preceding direct terms and is not claimed to vanish.

### 26.6. Original term 6

```math
F_{6}^i=-\tfrac{64i}{3}\gamma^{ab}\gamma^c(\mathcal D_aT_{bc})\chi^i.\tag{H28}
```

Vary each factor. Since $`\delta_Q`$ is even, this step introduces no extra Grassmann sign:

```math
\delta_QF_{6}^i=-\tfrac{64i}{3}\gamma^{ab}\gamma^c\chi^i\delta_Q(\mathcal D_aT_{bc})-\tfrac{64i}{3}\gamma^{ab}\gamma^c(\mathcal D_aT_{bc})\delta_Q\chi^i.\tag{H29}
```

Adding the explicitly evaluated contributions in this subsection gives

```math
\begin{aligned}

-\frac{16i}{3}\gamma^{ab} \gamma^c D(\mathcal D_aT_{bc})\epsilon^i\\
&+\frac{8}{3}\gamma^{ab} \gamma^c \gamma^{de} \gamma^{f}(\mathcal D_fT_{de})(\mathcal D_aT_{bc})\epsilon^i\\
&-\frac{8}{3}\gamma^{ab} \gamma^c \gamma^{d}(\mathcal D^eT_{de})(\mathcal D_aT_{bc})\epsilon^i\\
&+\frac{16i}{3}\gamma^{ab} \gamma^c \gamma^{rstu}T_{rs}T_{tu}(\mathcal D_aT_{bc})\epsilon^i\\
&-\frac{32i}{9}\gamma^{ab} \gamma^c T^2(\mathcal D_aT_{bc})\epsilon^i
.
\end{aligned}\tag{H30}
```

The other product-rule contribution is retained as

```math
-\tfrac{64i}{3}\gamma^{ab}\gamma^c\chi^i\delta_Q(\mathcal D_aT_{bc}).
```
Its full uncollected expansion is P30–P32. Its remaining parameter factorization is tracked in Section 27; it is **not** included in the preceding direct terms and is not claimed to vanish.

The discarded single-curvature origins are chi2: their SU(2) coefficient is traceless. No bilinear was discarded before H05/H08.

### 26.7. Original term 7

```math
F_{7}^i=\tfrac{1024}{9}T^2\chi^i.\tag{H31}
```

Vary each factor. Since $`\delta_Q`$ is even, this step introduces no extra Grassmann sign:

```math
\delta_QF_{7}^i=\tfrac{2048}{9}T^{ab}(\delta_QT_{ab})\chi^i+\tfrac{1024}{9}T^2\delta_Q\chi^i.\tag{H32}
```

The needed elementary laws are $`\delta_QT_{ab}=i\bar\epsilon\gamma_{ab}\chi/2-3i\bar\epsilon\widehat R(Q)_{ab}/32`$, together with W03 for $`\delta_Q\chi`$ and $`\delta_QD`$. The factor varied is visible in the product rule above.

Insert the actual spinors into H05. The scalar coefficient is $`(\frac{1024i}{9})(-1)(1/8)=-\frac{128i}{9}`$; the vector has the same factor and the bivector has minus one half of it:

```math
\begin{aligned}
\left.\frac{1024i}{9}T^{ab}(\chi)^i(\bar\epsilon \gamma_{ab}\chi)\right|_{\epsilon^i}&=-\frac{128i}{9}T^{ab}\big(\bar\chi\gamma_{ab}\chi\big)\epsilon^i\\
&-\frac{128i}{9}T^{ab}\big(\bar\chi\gamma_{ab}\gamma_p\chi\big)\gamma^p\epsilon^i\\
&+\frac{64i}{9}T^{ab}\big(\bar\chi\gamma_{ab}\gamma_{pq}\chi\big)\gamma^{pq}\epsilon^i .
\end{aligned}
```

Insert the actual spinors into H05. The scalar coefficient is $`(-\frac{64i}{3})(1)(1/8)=-\frac{8i}{3}`$; the vector has the same factor and the bivector has minus one half of it:

```math
\begin{aligned}
\left.-\frac{64i}{3}T^{ab}(\chi)^i(\bar\epsilon 1\widehat R(Q)_{ab})\right|_{\epsilon^i}&=-\frac{8i}{3}T^{ab}\big(\overline{\widehat R(Q)}_{ab}\chi\big)\epsilon^i\\
&-\frac{8i}{3}T^{ab}\big(\overline{\widehat R(Q)}_{ab}\gamma_p\chi\big)\gamma^p\epsilon^i\\
&+\frac{4i}{3}T^{ab}\big(\overline{\widehat R(Q)}_{ab}\gamma_{pq}\chi\big)\gamma^{pq}\epsilon^i .
\end{aligned}
```

Adding the explicitly evaluated contributions in this subsection gives

```math
\begin{aligned}

-\frac{128i}{9}T^{ab}\big(\bar\chi\gamma_{ab}\chi\big)\epsilon^i\\
&-\frac{128i}{9}T^{ab}\big(\bar\chi\gamma_{ab}\gamma_p\chi\big)\gamma^p\epsilon^i\\
&+\frac{64i}{9}T^{ab}\big(\bar\chi\gamma_{ab}\gamma_{pq}\chi\big)\gamma^{pq}\epsilon^i\\
&-\frac{8i}{3}T^{ab}\big(\overline{\widehat R(Q)}_{ab}\chi\big)\epsilon^i\\
&-\frac{8i}{3}T^{ab}\big(\overline{\widehat R(Q)}_{ab}\gamma_p\chi\big)\gamma^p\epsilon^i\\
&+\frac{4i}{3}T^{ab}\big(\overline{\widehat R(Q)}_{ab}\gamma_{pq}\chi\big)\gamma^{pq}\epsilon^i\\
&+\frac{256}{9}DT^2\epsilon^i\\
&+\frac{128i}{9}\gamma^{ab} \gamma^{c}(\mathcal D_cT_{ab})T^2\epsilon^i\\
&-\frac{128i}{9}\gamma^{a}(\mathcal D^bT_{ab})T^2\epsilon^i\\
&-\frac{256}{9}T^2\gamma^{rstu}T_{rs}T_{tu}\epsilon^i\\
&+\frac{512}{27}{T^2}^2\epsilon^i
.
\end{aligned}\tag{H33}
```

The discarded single-curvature origins are chi2: their SU(2) coefficient is traceless. No bilinear was discarded before H05/H08.

### 26.8. Original term 8

```math
F_{8}^i=\tfrac{128i}{3}\gamma_a(\mathcal D_b\chi^i)T^{ab}.\tag{H34}
```

Vary each factor. Since $`\delta_Q`$ is even, this step introduces no extra Grassmann sign:

```math
\delta_QF_{8}^i=\tfrac{128i}{3}\gamma_aT^{ab}\delta_Q(\mathcal D_b\chi^i)+\tfrac{128i}{3}\gamma_a(\mathcal D_b\chi^i)\delta_QT^{ab}.\tag{H35}
```

The needed elementary laws are $`\delta_QT_{ab}=i\bar\epsilon\gamma_{ab}\chi/2-3i\bar\epsilon\widehat R(Q)_{ab}/32`$, together with W03 for $`\delta_Q\chi`$ and $`\delta_QD`$. The factor varied is visible in the product rule above.

Insert the actual spinors into H05. The scalar coefficient is $`(-\frac{64}{3})(-1)(1/8)=\frac{8}{3}`$; the vector has the same factor and the bivector has minus one half of it:

```math
\begin{aligned}
\left.-\frac{64}{3}(\gamma_a \mathcal D_b\chi)^i(\bar\epsilon \gamma^{ab}\chi)\right|_{\epsilon^i}&=\frac{8}{3}\big(\bar\chi\gamma^{ab}\gamma_a \mathcal D_b\chi\big)\epsilon^i\\
&+\frac{8}{3}\big(\bar\chi\gamma^{ab}\gamma_p\gamma_a \mathcal D_b\chi\big)\gamma^p\epsilon^i\\
&-\frac{4}{3}\big(\bar\chi\gamma^{ab}\gamma_{pq}\gamma_a \mathcal D_b\chi\big)\gamma^{pq}\epsilon^i .
\end{aligned}
```

Insert the actual spinors into H05. The scalar coefficient is $`(4)(1)(1/8)=\frac{1}{2}`$; the vector has the same factor and the bivector has minus one half of it:

```math
\begin{aligned}
\left.4(\gamma_a \mathcal D_b\chi)^i(\bar\epsilon 1\widehat R(Q)^{ab})\right|_{\epsilon^i}&=\frac{1}{2}\big(\overline{\widehat R(Q)}^{ab}\gamma_a \mathcal D_b\chi\big)\epsilon^i\\
&+\frac{1}{2}\big(\overline{\widehat R(Q)}^{ab}\gamma_p\gamma_a \mathcal D_b\chi\big)\gamma^p\epsilon^i\\
&-\frac{1}{4}\big(\overline{\widehat R(Q)}^{ab}\gamma_{pq}\gamma_a \mathcal D_b\chi\big)\gamma^{pq}\epsilon^i .
\end{aligned}
```

Adding the explicitly evaluated contributions in this subsection gives

```math
\begin{aligned}

\frac{8}{3}\big(\bar\chi\gamma^{ab}\gamma_a \mathcal D_b\chi\big)\epsilon^i\\
&+\frac{8}{3}\big(\bar\chi\gamma^{ab}\gamma_p\gamma_a \mathcal D_b\chi\big)\gamma^p\epsilon^i\\
&-\frac{4}{3}\big(\bar\chi\gamma^{ab}\gamma_{pq}\gamma_a \mathcal D_b\chi\big)\gamma^{pq}\epsilon^i\\
&+\frac{1}{2}\big(\overline{\widehat R(Q)}^{ab}\gamma_a \mathcal D_b\chi\big)\epsilon^i\\
&+\frac{1}{2}\big(\overline{\widehat R(Q)}^{ab}\gamma_p\gamma_a \mathcal D_b\chi\big)\gamma^p\epsilon^i\\
&-\frac{1}{4}\big(\overline{\widehat R(Q)}^{ab}\gamma_{pq}\gamma_a \mathcal D_b\chi\big)\gamma^{pq}\epsilon^i
.
\end{aligned}\tag{H36}
```

The other product-rule contribution is retained as

```math
\tfrac{128i}{3}\gamma_aT^{ab}\delta_Q(\mathcal D_b\chi^i).
```
Its full uncollected expansion is P33–P35. Its remaining parameter factorization is tracked in Section 27; it is **not** included in the preceding direct terms and is not claimed to vanish.

### 26.9. Original term 9

```math
F_{9}^i=\tfrac83\gamma_{ab}T^{ab}T^{cd}\widehat R(Q)_{cd}^i.\tag{H37}
```

Vary each factor. Since $`\delta_Q`$ is even, this step introduces no extra Grassmann sign:

```math
\delta_QF_{9}^i=\tfrac83\gamma_{ab}T^{ab}T^{cd}\delta_Q\widehat R(Q)_{cd}^i+\tfrac83\gamma_{ab}T^{cd}\widehat R(Q)_{cd}^i\delta_QT^{ab}+\tfrac83\gamma_{ab}T^{ab}\widehat R(Q)_{cd}^i\delta_QT^{cd}.\tag{H38}
```

The needed elementary laws are $`\delta_QT_{ab}=i\bar\epsilon\gamma_{ab}\chi/2-3i\bar\epsilon\widehat R(Q)_{ab}/32`$, together with W03 for $`\delta_Q\chi`$ and $`\delta_QD`$. The factor varied is visible in the product rule above.

Insert the actual spinors into H05. The scalar coefficient is $`(\frac{4i}{3})(-1)(1/8)=-\frac{i}{6}`$; the vector has the same factor and the bivector has minus one half of it:

```math
\begin{aligned}
\left.\frac{4i}{3}T^{cd}(\gamma_{ab}\widehat R(Q)_{cd})^i(\bar\epsilon \gamma^{ab}\chi)\right|_{\epsilon^i}&=-\frac{i}{6}T^{cd}\big(\bar\chi\gamma^{ab}\gamma_{ab}\widehat R(Q)_{cd}\big)\epsilon^i\\
&-\frac{i}{6}T^{cd}\big(\bar\chi\gamma^{ab}\gamma_p\gamma_{ab}\widehat R(Q)_{cd}\big)\gamma^p\epsilon^i\\
&+\frac{i}{12}T^{cd}\big(\bar\chi\gamma^{ab}\gamma_{pq}\gamma_{ab}\widehat R(Q)_{cd}\big)\gamma^{pq}\epsilon^i .
\end{aligned}
```

Insert the actual spinors into H05. The scalar coefficient is $`(-\frac{i}{4})(1)(1/8)=-\frac{i}{32}`$; the vector has the same factor and the bivector has minus one half of it:

```math
\begin{aligned}
\left.-\frac{i}{4}T^{cd}(\gamma_{ab}\widehat R(Q)_{cd})^i(\bar\epsilon 1\widehat R(Q)^{ab})\right|_{\epsilon^i}&=-\frac{i}{32}T^{cd}\big(\overline{\widehat R(Q)}^{ab}\gamma_{ab}\widehat R(Q)_{cd}\big)\epsilon^i\\
&-\frac{i}{32}T^{cd}\big(\overline{\widehat R(Q)}^{ab}\gamma_p\gamma_{ab}\widehat R(Q)_{cd}\big)\gamma^p\epsilon^i\\
&+\frac{i}{64}T^{cd}\big(\overline{\widehat R(Q)}^{ab}\gamma_{pq}\gamma_{ab}\widehat R(Q)_{cd}\big)\gamma^{pq}\epsilon^i .
\end{aligned}
```

Insert the actual spinors into H05. The scalar coefficient is $`(\frac{4i}{3})(-1)(1/8)=-\frac{i}{6}`$; the vector has the same factor and the bivector has minus one half of it:

```math
\begin{aligned}
\left.\frac{4i}{3}T^{ab}(\gamma_{ab}\widehat R(Q)_{cd})^i(\bar\epsilon \gamma^{cd}\chi)\right|_{\epsilon^i}&=-\frac{i}{6}T^{ab}\big(\bar\chi\gamma^{cd}\gamma_{ab}\widehat R(Q)_{cd}\big)\epsilon^i\\
&-\frac{i}{6}T^{ab}\big(\bar\chi\gamma^{cd}\gamma_p\gamma_{ab}\widehat R(Q)_{cd}\big)\gamma^p\epsilon^i\\
&+\frac{i}{12}T^{ab}\big(\bar\chi\gamma^{cd}\gamma_{pq}\gamma_{ab}\widehat R(Q)_{cd}\big)\gamma^{pq}\epsilon^i .
\end{aligned}
```

Insert the actual spinors into H05. The scalar coefficient is $`(-\frac{i}{4})(1)(1/8)=-\frac{i}{32}`$; the vector has the same factor and the bivector has minus one half of it:

```math
\begin{aligned}
\left.-\frac{i}{4}T^{ab}(\gamma_{ab}\widehat R(Q)_{cd})^i(\bar\epsilon 1\widehat R(Q)^{cd})\right|_{\epsilon^i}&=-\frac{i}{32}T^{ab}\big(\overline{\widehat R(Q)}^{cd}\gamma_{ab}\widehat R(Q)_{cd}\big)\epsilon^i\\
&-\frac{i}{32}T^{ab}\big(\overline{\widehat R(Q)}^{cd}\gamma_p\gamma_{ab}\widehat R(Q)_{cd}\big)\gamma^p\epsilon^i\\
&+\frac{i}{64}T^{ab}\big(\overline{\widehat R(Q)}^{cd}\gamma_{pq}\gamma_{ab}\widehat R(Q)_{cd}\big)\gamma^{pq}\epsilon^i .
\end{aligned}
```

Adding the explicitly evaluated contributions in this subsection gives

```math
\begin{aligned}

\frac{2}{3}\gamma_{ab} \gamma_{ef}\widehat C_{cd}{}^{ef}T^{ab}T^{cd}\epsilon^i\\
&+\frac{16i}{3}\gamma_{ab} \gamma^{ef} \gamma_{d]}(\mathcal D_{[c}T_{ef})T^{ab}T^{cd}\epsilon^i\\
&-\frac{16i}{9}\gamma_{ab} \gamma_{[d} \gamma^{ef}(\mathcal D_{c]}T_{ef})T^{ab}T^{cd}\epsilon^i\\
&-\frac{16i}{9}\gamma_{ab} \gamma_{[c} \gamma^{g} \gamma^{ef} \gamma_{d]}(\mathcal D_gT_{ef})T^{ab}T^{cd}\epsilon^i\\
&-\frac{16i}{9}\gamma_{ab} \gamma_{cd} \gamma^{e}(\mathcal D^fT_{fe})T^{ab}T^{cd}\epsilon^i\\
&-\frac{i}{6}T^{cd}\big(\bar\chi\gamma^{ab}\gamma_{ab}\widehat R(Q)_{cd}\big)\epsilon^i\\
&-\frac{i}{6}T^{cd}\big(\bar\chi\gamma^{ab}\gamma_p\gamma_{ab}\widehat R(Q)_{cd}\big)\gamma^p\epsilon^i\\
&+\frac{i}{12}T^{cd}\big(\bar\chi\gamma^{ab}\gamma_{pq}\gamma_{ab}\widehat R(Q)_{cd}\big)\gamma^{pq}\epsilon^i\\
&-\frac{i}{32}T^{cd}\big(\overline{\widehat R(Q)}^{ab}\gamma_{ab}\widehat R(Q)_{cd}\big)\epsilon^i\\
&-\frac{i}{32}T^{cd}\big(\overline{\widehat R(Q)}^{ab}\gamma_p\gamma_{ab}\widehat R(Q)_{cd}\big)\gamma^p\epsilon^i\\
&+\frac{i}{64}T^{cd}\big(\overline{\widehat R(Q)}^{ab}\gamma_{pq}\gamma_{ab}\widehat R(Q)_{cd}\big)\gamma^{pq}\epsilon^i\\
&-\frac{i}{6}T^{ab}\big(\bar\chi\gamma^{cd}\gamma_{ab}\widehat R(Q)_{cd}\big)\epsilon^i\\
&-\frac{i}{6}T^{ab}\big(\bar\chi\gamma^{cd}\gamma_p\gamma_{ab}\widehat R(Q)_{cd}\big)\gamma^p\epsilon^i\\
&+\frac{i}{12}T^{ab}\big(\bar\chi\gamma^{cd}\gamma_{pq}\gamma_{ab}\widehat R(Q)_{cd}\big)\gamma^{pq}\epsilon^i\\
&-\frac{i}{32}T^{ab}\big(\overline{\widehat R(Q)}^{cd}\gamma_{ab}\widehat R(Q)_{cd}\big)\epsilon^i\\
&-\frac{i}{32}T^{ab}\big(\overline{\widehat R(Q)}^{cd}\gamma_p\gamma_{ab}\widehat R(Q)_{cd}\big)\gamma^p\epsilon^i\\
&+\frac{i}{64}T^{ab}\big(\overline{\widehat R(Q)}^{cd}\gamma_{pq}\gamma_{ab}\widehat R(Q)_{cd}\big)\gamma^{pq}\epsilon^i
.
\end{aligned}\tag{H39}
```

The discarded single-curvature origins are R1, R2, R3: their SU(2) coefficient is traceless. No bilinear was discarded before H05/H08.

### 26.10. Original term 10

The full nine-term law being inserted in terms 10 and 11 is R06/P15:

```math
\begin{aligned}
\delta_Q\widehat R(V)_{ab}^{ij}={}&
-\tfrac32\bar\epsilon^{(i}\gamma^c\mathcal D_c\widehat R(Q)_{ab}^{j)}
-\tfrac32\bar\epsilon^{(i}\gamma_{[a}\mathcal D^c\widehat R(Q)_{b]c}^{j)}
+4iT^{cd}\bar\epsilon^{(i}\gamma_{ab}\widehat R(Q)_{cd}^{j)}\\
&-18iT^{cd}\bar\epsilon^{(i}\gamma_d\gamma_{[a}\widehat R(Q)_{b]c}^{j)}
+\tfrac{9i}{2}\bar\epsilon^{(i}(\gamma\!\cdot\!T)\widehat R(Q)_{ab}^{j)}
+12iT^c{}_{[a}\bar\epsilon^{(i}\widehat R(Q)_{b]c}^{j)}\\
&-8\bar\epsilon^{(i}\gamma_{[a}\mathcal D_{b]}\chi^{j)}
+i\bar\epsilon^{(i}(\gamma\!\cdot\!T)\widehat R(Q)_{ab}^{j)}
+8i\bar\epsilon^{(i}\gamma_{[a}(\gamma\!\cdot\!T)\gamma_{b]}\chi^{j)}.
\end{aligned}\tag{H40a}
```

For example the first contribution in term 10 carries
$`(1/2)(-3/2)(3/16)=-9/64`$ after Schouten and Fierz. In term 11 it carries
$`(-8/3)(-3/2)(3/16)=3/4`$. The following lines perform the same explicit
substitution for each of the nine distinct spinor pairings.

```math
F_{10}^i=\tfrac12\widehat R(V)^{ab\,i}{}_j\widehat R(Q)_{ab}^j.\tag{H40}
```

Vary each factor. Since $`\delta_Q`$ is even, this step introduces no extra Grassmann sign:

```math
\delta_QF_{10}^i=\tfrac12(\delta_Q\widehat R(V)^{ab\,i}{}_j)\widehat R(Q)_{ab}^j+\tfrac12\widehat R(V)^{ab\,i}{}_j\delta_Q\widehat R(Q)_{ab}^j.\tag{H41}
```

Use the nine terms of $`\delta_Q\widehat R(V)`$ in R06/P15. Each is a symmetric-triplet pairing, so use H08, not H05. The direct product of the two curvatures instead uses H09. The result below shows all nine bilinear groups separately, even when two can later be combined.

Insert the actual spinors into H08. The scalar coefficient is $`(-\frac{3}{4})(1)(3/16)=-\frac{9}{64}`$; the vector has the same factor and the bivector has minus one half of it:

```math
\begin{aligned}
\left.-\frac{3}{4}\bar\epsilon^{(i}\gamma^c(\mathcal D_c\widehat R(Q)^{ab})^{j)}\varepsilon_{jk}(\widehat R(Q)_{ab})^k\right|_{\epsilon^i}&=-\frac{9}{64}\big(\overline{\mathcal D_c\widehat R(Q)^{ab}}\gamma^c\widehat R(Q)_{ab}\big)\epsilon^i\\
&-\frac{9}{64}\big(\overline{\mathcal D_c\widehat R(Q)^{ab}}\gamma^c\gamma_p\widehat R(Q)_{ab}\big)\gamma^p\epsilon^i\\
&+\frac{9}{128}\big(\overline{\mathcal D_c\widehat R(Q)^{ab}}\gamma^c\gamma_{pq}\widehat R(Q)_{ab}\big)\gamma^{pq}\epsilon^i .
\end{aligned}
```

Insert the actual spinors into H08. The scalar coefficient is $`(-\frac{3}{4})(1)(3/16)=-\frac{9}{64}`$; the vector has the same factor and the bivector has minus one half of it:

```math
\begin{aligned}
\left.-\frac{3}{4}\bar\epsilon^{(i}\gamma^{[a}(\mathcal D^c\widehat R(Q)^{b]}{}_c)^{j)}\varepsilon_{jk}(\widehat R(Q)_{ab})^k\right|_{\epsilon^i}&=-\frac{9}{64}\big(\overline{\mathcal D^c\widehat R(Q)^{b]}{}_c}\gamma^{[a}\widehat R(Q)_{ab}\big)\epsilon^i\\
&-\frac{9}{64}\big(\overline{\mathcal D^c\widehat R(Q)^{b]}{}_c}\gamma^{[a}\gamma_p\widehat R(Q)_{ab}\big)\gamma^p\epsilon^i\\
&+\frac{9}{128}\big(\overline{\mathcal D^c\widehat R(Q)^{b]}{}_c}\gamma^{[a}\gamma_{pq}\widehat R(Q)_{ab}\big)\gamma^{pq}\epsilon^i .
\end{aligned}
```

Insert the actual spinors into H08. The scalar coefficient is $`(2i)(-1)(3/16)=-\frac{3i}{8}`$; the vector has the same factor and the bivector has minus one half of it:

```math
\begin{aligned}
\left.2i\bar\epsilon^{(i}\gamma^{ab}(T^{ef}\widehat R(Q)_{ef})^{j)}\varepsilon_{jk}(\widehat R(Q)_{ab})^k\right|_{\epsilon^i}&=-\frac{3i}{8}\big(T^{ef}\overline{\widehat R(Q)}_{ef}\gamma^{ab}\widehat R(Q)_{ab}\big)\epsilon^i\\
&-\frac{3i}{8}\big(T^{ef}\overline{\widehat R(Q)}_{ef}\gamma^{ab}\gamma_p\widehat R(Q)_{ab}\big)\gamma^p\epsilon^i\\
&+\frac{3i}{16}\big(T^{ef}\overline{\widehat R(Q)}_{ef}\gamma^{ab}\gamma_{pq}\widehat R(Q)_{ab}\big)\gamma^{pq}\epsilon^i .
\end{aligned}
```

Insert the actual spinors into H08. The scalar coefficient is $`(-9i)(1)(3/16)=-\frac{27i}{16}`$; the vector has the same factor and the bivector has minus one half of it:

```math
\begin{aligned}
\left.-9iT^{cd}\bar\epsilon^{(i}\gamma_d\gamma^{[a}(\widehat R(Q)^{b]}{}_c)^{j)}\varepsilon_{jk}(\widehat R(Q)_{ab})^k\right|_{\epsilon^i}&=-\frac{27i}{16}T^{cd}\big(\overline{\widehat R(Q)}^{b]}{}_c\gamma^{[a}\gamma_d\widehat R(Q)_{ab}\big)\epsilon^i\\
&-\frac{27i}{16}T^{cd}\big(\overline{\widehat R(Q)}^{b]}{}_c\gamma^{[a}\gamma_d\gamma_p\widehat R(Q)_{ab}\big)\gamma^p\epsilon^i\\
&+\frac{27i}{32}T^{cd}\big(\overline{\widehat R(Q)}^{b]}{}_c\gamma^{[a}\gamma_d\gamma_{pq}\widehat R(Q)_{ab}\big)\gamma^{pq}\epsilon^i .
\end{aligned}
```

Insert the actual spinors into H08. The scalar coefficient is $`(\frac{9i}{4})(-1)(3/16)=-\frac{27i}{64}`$; the vector has the same factor and the bivector has minus one half of it:

```math
\begin{aligned}
\left.\frac{9i}{4}\bar\epsilon^{(i}(\gamma\!\cdot\!T)(\widehat R(Q)^{ab})^{j)}\varepsilon_{jk}(\widehat R(Q)_{ab})^k\right|_{\epsilon^i}&=-\frac{27i}{64}\big(\overline{\widehat R(Q)}^{ab}(\gamma\!\cdot\!T)\widehat R(Q)_{ab}\big)\epsilon^i\\
&-\frac{27i}{64}\big(\overline{\widehat R(Q)}^{ab}(\gamma\!\cdot\!T)\gamma_p\widehat R(Q)_{ab}\big)\gamma^p\epsilon^i\\
&+\frac{27i}{128}\big(\overline{\widehat R(Q)}^{ab}(\gamma\!\cdot\!T)\gamma_{pq}\widehat R(Q)_{ab}\big)\gamma^{pq}\epsilon^i .
\end{aligned}
```

Insert the actual spinors into H08. The scalar coefficient is $`(6i)(1)(3/16)=\frac{9i}{8}`$; the vector has the same factor and the bivector has minus one half of it:

```math
\begin{aligned}
\left.6iT^{c[a}\bar\epsilon^{(i}1(\widehat R(Q)^{b]}{}_c)^{j)}\varepsilon_{jk}(\widehat R(Q)_{ab})^k\right|_{\epsilon^i}&=\frac{9i}{8}T^{c[a}\big(\overline{\widehat R(Q)}^{b]}{}_c\widehat R(Q)_{ab}\big)\epsilon^i\\
&+\frac{9i}{8}T^{c[a}\big(\overline{\widehat R(Q)}^{b]}{}_c\gamma_p\widehat R(Q)_{ab}\big)\gamma^p\epsilon^i\\
&-\frac{9i}{16}T^{c[a}\big(\overline{\widehat R(Q)}^{b]}{}_c\gamma_{pq}\widehat R(Q)_{ab}\big)\gamma^{pq}\epsilon^i .
\end{aligned}
```

Insert the actual spinors into H08. The scalar coefficient is $`(-4)(1)(3/16)=-\frac{3}{4}`$; the vector has the same factor and the bivector has minus one half of it:

```math
\begin{aligned}
\left.-4\bar\epsilon^{(i}\gamma^{[a}(\mathcal D^{b]}\chi)^{j)}\varepsilon_{jk}(\widehat R(Q)_{ab})^k\right|_{\epsilon^i}&=-\frac{3}{4}\big(\overline{\mathcal D^{b]}\chi}\gamma^{[a}\widehat R(Q)_{ab}\big)\epsilon^i\\
&-\frac{3}{4}\big(\overline{\mathcal D^{b]}\chi}\gamma^{[a}\gamma_p\widehat R(Q)_{ab}\big)\gamma^p\epsilon^i\\
&+\frac{3}{8}\big(\overline{\mathcal D^{b]}\chi}\gamma^{[a}\gamma_{pq}\widehat R(Q)_{ab}\big)\gamma^{pq}\epsilon^i .
\end{aligned}
```

Insert the actual spinors into H08. The scalar coefficient is $`(\frac{i}{2})(-1)(3/16)=-\frac{3i}{32}`$; the vector has the same factor and the bivector has minus one half of it:

```math
\begin{aligned}
\left.\frac{i}{2}\bar\epsilon^{(i}(\gamma\!\cdot\!T)(\widehat R(Q)^{ab})^{j)}\varepsilon_{jk}(\widehat R(Q)_{ab})^k\right|_{\epsilon^i}&=-\frac{3i}{32}\big(\overline{\widehat R(Q)}^{ab}(\gamma\!\cdot\!T)\widehat R(Q)_{ab}\big)\epsilon^i\\
&-\frac{3i}{32}\big(\overline{\widehat R(Q)}^{ab}(\gamma\!\cdot\!T)\gamma_p\widehat R(Q)_{ab}\big)\gamma^p\epsilon^i\\
&+\frac{3i}{64}\big(\overline{\widehat R(Q)}^{ab}(\gamma\!\cdot\!T)\gamma_{pq}\widehat R(Q)_{ab}\big)\gamma^{pq}\epsilon^i .
\end{aligned}
```

Insert the actual spinors into H08. The scalar coefficient is $`(4i)(1)(3/16)=\frac{3i}{4}`$; the vector has the same factor and the bivector has minus one half of it:

```math
\begin{aligned}
\left.4i\bar\epsilon^{(i}\gamma^{[a}(\gamma\!\cdot\!T)\gamma^{b]}(\chi)^{j)}\varepsilon_{jk}(\widehat R(Q)_{ab})^k\right|_{\epsilon^i}&=\frac{3i}{4}\big(\bar\chi\gamma^{[a}(\gamma\!\cdot\!T)\gamma^{b]}\widehat R(Q)_{ab}\big)\epsilon^i\\
&+\frac{3i}{4}\big(\bar\chi\gamma^{[a}(\gamma\!\cdot\!T)\gamma^{b]}\gamma_p\widehat R(Q)_{ab}\big)\gamma^p\epsilon^i\\
&-\frac{3i}{8}\big(\bar\chi\gamma^{[a}(\gamma\!\cdot\!T)\gamma^{b]}\gamma_{pq}\widehat R(Q)_{ab}\big)\gamma^{pq}\epsilon^i .
\end{aligned}
```

Adding the explicitly evaluated contributions in this subsection gives

```math
\begin{aligned}

-\frac{9}{64}\big(\overline{\mathcal D_c\widehat R(Q)^{ab}}\gamma^c\widehat R(Q)_{ab}\big)\epsilon^i\\
&-\frac{9}{64}\big(\overline{\mathcal D_c\widehat R(Q)^{ab}}\gamma^c\gamma_p\widehat R(Q)_{ab}\big)\gamma^p\epsilon^i\\
&+\frac{9}{128}\big(\overline{\mathcal D_c\widehat R(Q)^{ab}}\gamma^c\gamma_{pq}\widehat R(Q)_{ab}\big)\gamma^{pq}\epsilon^i\\
&-\frac{9}{64}\big(\overline{\mathcal D^c\widehat R(Q)^{b]}{}_c}\gamma^{[a}\widehat R(Q)_{ab}\big)\epsilon^i\\
&-\frac{9}{64}\big(\overline{\mathcal D^c\widehat R(Q)^{b]}{}_c}\gamma^{[a}\gamma_p\widehat R(Q)_{ab}\big)\gamma^p\epsilon^i\\
&+\frac{9}{128}\big(\overline{\mathcal D^c\widehat R(Q)^{b]}{}_c}\gamma^{[a}\gamma_{pq}\widehat R(Q)_{ab}\big)\gamma^{pq}\epsilon^i\\
&-\frac{3i}{8}\big(T^{ef}\overline{\widehat R(Q)}_{ef}\gamma^{ab}\widehat R(Q)_{ab}\big)\epsilon^i\\
&-\frac{3i}{8}\big(T^{ef}\overline{\widehat R(Q)}_{ef}\gamma^{ab}\gamma_p\widehat R(Q)_{ab}\big)\gamma^p\epsilon^i\\
&+\frac{3i}{16}\big(T^{ef}\overline{\widehat R(Q)}_{ef}\gamma^{ab}\gamma_{pq}\widehat R(Q)_{ab}\big)\gamma^{pq}\epsilon^i\\
&-\frac{27i}{16}T^{cd}\big(\overline{\widehat R(Q)}^{b]}{}_c\gamma^{[a}\gamma_d\widehat R(Q)_{ab}\big)\epsilon^i\\
&-\frac{27i}{16}T^{cd}\big(\overline{\widehat R(Q)}^{b]}{}_c\gamma^{[a}\gamma_d\gamma_p\widehat R(Q)_{ab}\big)\gamma^p\epsilon^i\\
&+\frac{27i}{32}T^{cd}\big(\overline{\widehat R(Q)}^{b]}{}_c\gamma^{[a}\gamma_d\gamma_{pq}\widehat R(Q)_{ab}\big)\gamma^{pq}\epsilon^i\\
&-\frac{27i}{64}\big(\overline{\widehat R(Q)}^{ab}(\gamma\!\cdot\!T)\widehat R(Q)_{ab}\big)\epsilon^i\\
&-\frac{27i}{64}\big(\overline{\widehat R(Q)}^{ab}(\gamma\!\cdot\!T)\gamma_p\widehat R(Q)_{ab}\big)\gamma^p\epsilon^i\\
&+\frac{27i}{128}\big(\overline{\widehat R(Q)}^{ab}(\gamma\!\cdot\!T)\gamma_{pq}\widehat R(Q)_{ab}\big)\gamma^{pq}\epsilon^i\\
&+\frac{9i}{8}T^{c[a}\big(\overline{\widehat R(Q)}^{b]}{}_c\widehat R(Q)_{ab}\big)\epsilon^i\\
&+\frac{9i}{8}T^{c[a}\big(\overline{\widehat R(Q)}^{b]}{}_c\gamma_p\widehat R(Q)_{ab}\big)\gamma^p\epsilon^i\\
&-\frac{9i}{16}T^{c[a}\big(\overline{\widehat R(Q)}^{b]}{}_c\gamma_{pq}\widehat R(Q)_{ab}\big)\gamma^{pq}\epsilon^i\\
&-\frac{3}{4}\big(\overline{\mathcal D^{b]}\chi}\gamma^{[a}\widehat R(Q)_{ab}\big)\epsilon^i\\
&-\frac{3}{4}\big(\overline{\mathcal D^{b]}\chi}\gamma^{[a}\gamma_p\widehat R(Q)_{ab}\big)\gamma^p\epsilon^i\\
&+\frac{3}{8}\big(\overline{\mathcal D^{b]}\chi}\gamma^{[a}\gamma_{pq}\widehat R(Q)_{ab}\big)\gamma^{pq}\epsilon^i\\
&-\frac{3i}{32}\big(\overline{\widehat R(Q)}^{ab}(\gamma\!\cdot\!T)\widehat R(Q)_{ab}\big)\epsilon^i\\
&-\frac{3i}{32}\big(\overline{\widehat R(Q)}^{ab}(\gamma\!\cdot\!T)\gamma_p\widehat R(Q)_{ab}\big)\gamma^p\epsilon^i\\
&+\frac{3i}{64}\big(\overline{\widehat R(Q)}^{ab}(\gamma\!\cdot\!T)\gamma_{pq}\widehat R(Q)_{ab}\big)\gamma^{pq}\epsilon^i\\
&+\frac{3i}{4}\big(\bar\chi\gamma^{[a}(\gamma\!\cdot\!T)\gamma^{b]}\widehat R(Q)_{ab}\big)\epsilon^i\\
&+\frac{3i}{4}\big(\bar\chi\gamma^{[a}(\gamma\!\cdot\!T)\gamma^{b]}\gamma_p\widehat R(Q)_{ab}\big)\gamma^p\epsilon^i\\
&-\frac{3i}{8}\big(\bar\chi\gamma^{[a}(\gamma\!\cdot\!T)\gamma^{b]}\gamma_{pq}\widehat R(Q)_{ab}\big)\gamma^{pq}\epsilon^i\\
&-\frac{1}{24}\widehat R(V)^{ab\,kl}\gamma_{ab}{}^{cd}\widehat R(V)_{cd\,kl}\epsilon^i\\
&+\frac{1}{24}\widehat R(V)^{ab\,kl}\gamma^{cd} \gamma_{ab}\widehat R(V)_{cd\,kl}\epsilon^i\\
&+\frac{1}{48}\widehat R(V)^{ab\,kl}\gamma_{ab} \gamma^{cd}\widehat R(V)_{cd\,kl}\epsilon^i
.
\end{aligned}\tag{H42}
```

The discarded single-curvature origins are R4, R5, R6, R7, R8: their SU(2) coefficient is traceless. No bilinear was discarded before H05/H08.

Lorentz antisymmetrization is formed with the test column held fixed, before contracting its $`a,b`$ indices. The Fierz factors on the input lines are the original coefficients times $`3/16,3/16,-3/32`$, as shown.

### 26.11. Original term 11

```math
F_{11}^i=-\tfrac83\widehat R(V)^{ab\,i}{}_j\gamma_{ab}\chi^j.\tag{H43}
```

Vary each factor. Since $`\delta_Q`$ is even, this step introduces no extra Grassmann sign:

```math
\delta_QF_{11}^i=-\tfrac83(\delta_Q\widehat R(V)^{ab\,i}{}_j)\gamma_{ab}\chi^j-\tfrac83\widehat R(V)^{ab\,i}{}_j\gamma_{ab}\delta_Q\chi^j.\tag{H44}
```

Use the nine terms of $`\delta_Q\widehat R(V)`$ in R06/P15. Each is a symmetric-triplet pairing, so use H08, not H05. The direct product of the two curvatures instead uses H09. The result below shows all nine bilinear groups separately, even when two can later be combined.

Insert the actual spinors into H08. The scalar coefficient is $`(4)(1)(3/16)=\frac{3}{4}`$; the vector has the same factor and the bivector has minus one half of it:

```math
\begin{aligned}
\left.4\bar\epsilon^{(i}\gamma^c(\mathcal D_c\widehat R(Q)^{ab})^{j)}\varepsilon_{jk}(\gamma_{ab}\chi)^k\right|_{\epsilon^i}&=\frac{3}{4}\big(\overline{\mathcal D_c\widehat R(Q)^{ab}}\gamma^c\gamma_{ab}\chi\big)\epsilon^i\\
&+\frac{3}{4}\big(\overline{\mathcal D_c\widehat R(Q)^{ab}}\gamma^c\gamma_p\gamma_{ab}\chi\big)\gamma^p\epsilon^i\\
&-\frac{3}{8}\big(\overline{\mathcal D_c\widehat R(Q)^{ab}}\gamma^c\gamma_{pq}\gamma_{ab}\chi\big)\gamma^{pq}\epsilon^i .
\end{aligned}
```

Insert the actual spinors into H08. The scalar coefficient is $`(4)(1)(3/16)=\frac{3}{4}`$; the vector has the same factor and the bivector has minus one half of it:

```math
\begin{aligned}
\left.4\bar\epsilon^{(i}\gamma^{[a}(\mathcal D^c\widehat R(Q)^{b]}{}_c)^{j)}\varepsilon_{jk}(\gamma_{ab}\chi)^k\right|_{\epsilon^i}&=\frac{3}{4}\big(\overline{\mathcal D^c\widehat R(Q)^{b]}{}_c}\gamma^{[a}\gamma_{ab}\chi\big)\epsilon^i\\
&+\frac{3}{4}\big(\overline{\mathcal D^c\widehat R(Q)^{b]}{}_c}\gamma^{[a}\gamma_p\gamma_{ab}\chi\big)\gamma^p\epsilon^i\\
&-\frac{3}{8}\big(\overline{\mathcal D^c\widehat R(Q)^{b]}{}_c}\gamma^{[a}\gamma_{pq}\gamma_{ab}\chi\big)\gamma^{pq}\epsilon^i .
\end{aligned}
```

Insert the actual spinors into H08. The scalar coefficient is $`(-\frac{32i}{3})(-1)(3/16)=2i`$; the vector has the same factor and the bivector has minus one half of it:

```math
\begin{aligned}
\left.-\frac{32i}{3}\bar\epsilon^{(i}\gamma^{ab}(T^{ef}\widehat R(Q)_{ef})^{j)}\varepsilon_{jk}(\gamma_{ab}\chi)^k\right|_{\epsilon^i}&=2i\big(T^{ef}\overline{\widehat R(Q)}_{ef}\gamma^{ab}\gamma_{ab}\chi\big)\epsilon^i\\
&+2i\big(T^{ef}\overline{\widehat R(Q)}_{ef}\gamma^{ab}\gamma_p\gamma_{ab}\chi\big)\gamma^p\epsilon^i\\
&-i\big(T^{ef}\overline{\widehat R(Q)}_{ef}\gamma^{ab}\gamma_{pq}\gamma_{ab}\chi\big)\gamma^{pq}\epsilon^i .
\end{aligned}
```

Insert the actual spinors into H08. The scalar coefficient is $`(48i)(1)(3/16)=9i`$; the vector has the same factor and the bivector has minus one half of it:

```math
\begin{aligned}
\left.48iT^{cd}\bar\epsilon^{(i}\gamma_d\gamma^{[a}(\widehat R(Q)^{b]}{}_c)^{j)}\varepsilon_{jk}(\gamma_{ab}\chi)^k\right|_{\epsilon^i}&=9iT^{cd}\big(\overline{\widehat R(Q)}^{b]}{}_c\gamma^{[a}\gamma_d\gamma_{ab}\chi\big)\epsilon^i\\
&+9iT^{cd}\big(\overline{\widehat R(Q)}^{b]}{}_c\gamma^{[a}\gamma_d\gamma_p\gamma_{ab}\chi\big)\gamma^p\epsilon^i\\
&-\frac{9i}{2}T^{cd}\big(\overline{\widehat R(Q)}^{b]}{}_c\gamma^{[a}\gamma_d\gamma_{pq}\gamma_{ab}\chi\big)\gamma^{pq}\epsilon^i .
\end{aligned}
```

Insert the actual spinors into H08. The scalar coefficient is $`(-12i)(-1)(3/16)=\frac{9i}{4}`$; the vector has the same factor and the bivector has minus one half of it:

```math
\begin{aligned}
\left.-12i\bar\epsilon^{(i}(\gamma\!\cdot\!T)(\widehat R(Q)^{ab})^{j)}\varepsilon_{jk}(\gamma_{ab}\chi)^k\right|_{\epsilon^i}&=\frac{9i}{4}\big(\overline{\widehat R(Q)}^{ab}(\gamma\!\cdot\!T)\gamma_{ab}\chi\big)\epsilon^i\\
&+\frac{9i}{4}\big(\overline{\widehat R(Q)}^{ab}(\gamma\!\cdot\!T)\gamma_p\gamma_{ab}\chi\big)\gamma^p\epsilon^i\\
&-\frac{9i}{8}\big(\overline{\widehat R(Q)}^{ab}(\gamma\!\cdot\!T)\gamma_{pq}\gamma_{ab}\chi\big)\gamma^{pq}\epsilon^i .
\end{aligned}
```

Insert the actual spinors into H08. The scalar coefficient is $`(-32i)(1)(3/16)=-6i`$; the vector has the same factor and the bivector has minus one half of it:

```math
\begin{aligned}
\left.-32iT^{c[a}\bar\epsilon^{(i}1(\widehat R(Q)^{b]}{}_c)^{j)}\varepsilon_{jk}(\gamma_{ab}\chi)^k\right|_{\epsilon^i}&=-6iT^{c[a}\big(\overline{\widehat R(Q)}^{b]}{}_c\gamma_{ab}\chi\big)\epsilon^i\\
&-6iT^{c[a}\big(\overline{\widehat R(Q)}^{b]}{}_c\gamma_p\gamma_{ab}\chi\big)\gamma^p\epsilon^i\\
&+3iT^{c[a}\big(\overline{\widehat R(Q)}^{b]}{}_c\gamma_{pq}\gamma_{ab}\chi\big)\gamma^{pq}\epsilon^i .
\end{aligned}
```

Insert the actual spinors into H08. The scalar coefficient is $`(\frac{64}{3})(1)(3/16)=4`$; the vector has the same factor and the bivector has minus one half of it:

```math
\begin{aligned}
\left.\frac{64}{3}\bar\epsilon^{(i}\gamma^{[a}(\mathcal D^{b]}\chi)^{j)}\varepsilon_{jk}(\gamma_{ab}\chi)^k\right|_{\epsilon^i}&=4\big(\overline{\mathcal D^{b]}\chi}\gamma^{[a}\gamma_{ab}\chi\big)\epsilon^i\\
&+4\big(\overline{\mathcal D^{b]}\chi}\gamma^{[a}\gamma_p\gamma_{ab}\chi\big)\gamma^p\epsilon^i\\
&-2\big(\overline{\mathcal D^{b]}\chi}\gamma^{[a}\gamma_{pq}\gamma_{ab}\chi\big)\gamma^{pq}\epsilon^i .
\end{aligned}
```

Insert the actual spinors into H08. The scalar coefficient is $`(-\frac{8i}{3})(-1)(3/16)=\frac{i}{2}`$; the vector has the same factor and the bivector has minus one half of it:

```math
\begin{aligned}
\left.-\frac{8i}{3}\bar\epsilon^{(i}(\gamma\!\cdot\!T)(\widehat R(Q)^{ab})^{j)}\varepsilon_{jk}(\gamma_{ab}\chi)^k\right|_{\epsilon^i}&=\frac{i}{2}\big(\overline{\widehat R(Q)}^{ab}(\gamma\!\cdot\!T)\gamma_{ab}\chi\big)\epsilon^i\\
&+\frac{i}{2}\big(\overline{\widehat R(Q)}^{ab}(\gamma\!\cdot\!T)\gamma_p\gamma_{ab}\chi\big)\gamma^p\epsilon^i\\
&-\frac{i}{4}\big(\overline{\widehat R(Q)}^{ab}(\gamma\!\cdot\!T)\gamma_{pq}\gamma_{ab}\chi\big)\gamma^{pq}\epsilon^i .
\end{aligned}
```

Insert the actual spinors into H08. The scalar coefficient is $`(-\frac{64i}{3})(1)(3/16)=-4i`$; the vector has the same factor and the bivector has minus one half of it:

```math
\begin{aligned}
\left.-\frac{64i}{3}\bar\epsilon^{(i}\gamma^{[a}(\gamma\!\cdot\!T)\gamma^{b]}(\chi)^{j)}\varepsilon_{jk}(\gamma_{ab}\chi)^k\right|_{\epsilon^i}&=-4i\big(\bar\chi\gamma^{[a}(\gamma\!\cdot\!T)\gamma^{b]}\gamma_{ab}\chi\big)\epsilon^i\\
&-4i\big(\bar\chi\gamma^{[a}(\gamma\!\cdot\!T)\gamma^{b]}\gamma_p\gamma_{ab}\chi\big)\gamma^p\epsilon^i\\
&+2i\big(\bar\chi\gamma^{[a}(\gamma\!\cdot\!T)\gamma^{b]}\gamma_{pq}\gamma_{ab}\chi\big)\gamma^{pq}\epsilon^i .
\end{aligned}
```

Adding the explicitly evaluated contributions in this subsection gives

```math
\begin{aligned}

\frac{3}{4}\big(\overline{\mathcal D_c\widehat R(Q)^{ab}}\gamma^c\gamma_{ab}\chi\big)\epsilon^i\\
&+\frac{3}{4}\big(\overline{\mathcal D_c\widehat R(Q)^{ab}}\gamma^c\gamma_p\gamma_{ab}\chi\big)\gamma^p\epsilon^i\\
&-\frac{3}{8}\big(\overline{\mathcal D_c\widehat R(Q)^{ab}}\gamma^c\gamma_{pq}\gamma_{ab}\chi\big)\gamma^{pq}\epsilon^i\\
&+\frac{3}{4}\big(\overline{\mathcal D^c\widehat R(Q)^{b]}{}_c}\gamma^{[a}\gamma_{ab}\chi\big)\epsilon^i\\
&+\frac{3}{4}\big(\overline{\mathcal D^c\widehat R(Q)^{b]}{}_c}\gamma^{[a}\gamma_p\gamma_{ab}\chi\big)\gamma^p\epsilon^i\\
&-\frac{3}{8}\big(\overline{\mathcal D^c\widehat R(Q)^{b]}{}_c}\gamma^{[a}\gamma_{pq}\gamma_{ab}\chi\big)\gamma^{pq}\epsilon^i\\
&+2i\big(T^{ef}\overline{\widehat R(Q)}_{ef}\gamma^{ab}\gamma_{ab}\chi\big)\epsilon^i\\
&+2i\big(T^{ef}\overline{\widehat R(Q)}_{ef}\gamma^{ab}\gamma_p\gamma_{ab}\chi\big)\gamma^p\epsilon^i\\
&-i\big(T^{ef}\overline{\widehat R(Q)}_{ef}\gamma^{ab}\gamma_{pq}\gamma_{ab}\chi\big)\gamma^{pq}\epsilon^i\\
&+9iT^{cd}\big(\overline{\widehat R(Q)}^{b]}{}_c\gamma^{[a}\gamma_d\gamma_{ab}\chi\big)\epsilon^i\\
&+9iT^{cd}\big(\overline{\widehat R(Q)}^{b]}{}_c\gamma^{[a}\gamma_d\gamma_p\gamma_{ab}\chi\big)\gamma^p\epsilon^i\\
&-\frac{9i}{2}T^{cd}\big(\overline{\widehat R(Q)}^{b]}{}_c\gamma^{[a}\gamma_d\gamma_{pq}\gamma_{ab}\chi\big)\gamma^{pq}\epsilon^i\\
&+\frac{9i}{4}\big(\overline{\widehat R(Q)}^{ab}(\gamma\!\cdot\!T)\gamma_{ab}\chi\big)\epsilon^i\\
&+\frac{9i}{4}\big(\overline{\widehat R(Q)}^{ab}(\gamma\!\cdot\!T)\gamma_p\gamma_{ab}\chi\big)\gamma^p\epsilon^i\\
&-\frac{9i}{8}\big(\overline{\widehat R(Q)}^{ab}(\gamma\!\cdot\!T)\gamma_{pq}\gamma_{ab}\chi\big)\gamma^{pq}\epsilon^i\\
&-6iT^{c[a}\big(\overline{\widehat R(Q)}^{b]}{}_c\gamma_{ab}\chi\big)\epsilon^i\\
&-6iT^{c[a}\big(\overline{\widehat R(Q)}^{b]}{}_c\gamma_p\gamma_{ab}\chi\big)\gamma^p\epsilon^i\\
&+3iT^{c[a}\big(\overline{\widehat R(Q)}^{b]}{}_c\gamma_{pq}\gamma_{ab}\chi\big)\gamma^{pq}\epsilon^i\\
&+4\big(\overline{\mathcal D^{b]}\chi}\gamma^{[a}\gamma_{ab}\chi\big)\epsilon^i\\
&+4\big(\overline{\mathcal D^{b]}\chi}\gamma^{[a}\gamma_p\gamma_{ab}\chi\big)\gamma^p\epsilon^i\\
&-2\big(\overline{\mathcal D^{b]}\chi}\gamma^{[a}\gamma_{pq}\gamma_{ab}\chi\big)\gamma^{pq}\epsilon^i\\
&+\frac{i}{2}\big(\overline{\widehat R(Q)}^{ab}(\gamma\!\cdot\!T)\gamma_{ab}\chi\big)\epsilon^i\\
&+\frac{i}{2}\big(\overline{\widehat R(Q)}^{ab}(\gamma\!\cdot\!T)\gamma_p\gamma_{ab}\chi\big)\gamma^p\epsilon^i\\
&-\frac{i}{4}\big(\overline{\widehat R(Q)}^{ab}(\gamma\!\cdot\!T)\gamma_{pq}\gamma_{ab}\chi\big)\gamma^{pq}\epsilon^i\\
&-4i\big(\bar\chi\gamma^{[a}(\gamma\!\cdot\!T)\gamma^{b]}\gamma_{ab}\chi\big)\epsilon^i\\
&-4i\big(\bar\chi\gamma^{[a}(\gamma\!\cdot\!T)\gamma^{b]}\gamma_p\gamma_{ab}\chi\big)\gamma^p\epsilon^i\\
&+2i\big(\bar\chi\gamma^{[a}(\gamma\!\cdot\!T)\gamma^{b]}\gamma_{pq}\gamma_{ab}\chi\big)\gamma^{pq}\epsilon^i\\
&+\frac{1}{48}\widehat R(V)^{ab\,kl}\gamma_{ab} \gamma^{cd}\widehat R(V)_{cd\,kl}\epsilon^i
.
\end{aligned}\tag{H45}
```

The discarded single-curvature origins are chi1, chi3, chi4, chi5, chi6: their SU(2) coefficient is traceless. No bilinear was discarded before H05/H08.

Lorentz antisymmetrization is formed with the test column held fixed, before contracting its $`a,b`$ indices. The Fierz factors on the input lines are the original coefficients times $`3/16,3/16,-3/32`$, as shown.

## 27. Complete the Remaining Contributions

### 27.1 Finish the gamma reduction of the complete third term

The derivative gamma string in H21 reduces as follows:

```math
\begin{aligned}
\gamma^{ab}\gamma^c\mathcal D_cT_{ab}
&=\gamma^{abc}\mathcal D_cT_{ab}
 +\gamma^a\mathcal D^bT_{ab}-\gamma^b\mathcal D^aT_{ab}\\
&=\gamma^{abc}\mathcal D_cT_{ab}
 +2\gamma^a\mathcal D^bT_{ab}\\
&=-\tfrac i2\epsilon^{abcde}\gamma_{de}\mathcal D_cT_{ab}
 +2\gamma^a\mathcal D^bT_{ab}.
\end{aligned}\tag{H46}
```

The second line exchanges the dummy labels $`a,b`$ in its last term and
uses $`T_{ba}=-T_{ab}`$. Therefore the two derivative-vector terms in H21
have net coefficient $`(16i/3)(2-1)=16i/3`$. For the rank-three part,
$`(16i/3)(-i/2)=8/3`$. The four-gamma term gives
$`(-32/3)i\epsilon_{pabcd}T^{ab}T^{cd}\gamma^pD`$.
Inserting these three reductions and the two displayed Fierz calculations
of Section 26.3 gives the entire third-term singlet:

```math
\begin{aligned}
\left.\delta_Q\!\left(\tfrac{128}{3}\chi^iD\right)\right|_{\epsilon^i}
={}&\left[\tfrac{32}{3}D^2+\tfrac{64}{9}DT^2
+\tfrac{16}{3}\overline{\mathcal D_a\chi}\gamma^a\chi
+\tfrac{80i}{9}\bar\chi(\gamma\!\cdot\!T)\chi\right]\epsilon^i\\
&+\left[\tfrac{16i}{3}D\mathcal D^bT_{pb}
-\tfrac{32i}{3}D\epsilon_{pabcd}T^{ab}T^{cd}
+\tfrac{16}{3}\overline{\mathcal D_a\chi}\gamma^a\gamma_p\chi
+\tfrac{80i}{9}\bar\chi(\gamma\!\cdot\!T)\gamma_p\chi\right]\gamma^p\epsilon^i\\
&+\left[\tfrac83D\epsilon_{pqabc}\mathcal D^aT^{bc}
-\tfrac83\overline{\mathcal D_a\chi}\gamma^a\gamma_{pq}\chi
-\tfrac{40i}{9}\bar\chi(\gamma\!\cdot\!T)\gamma_{pq}\chi\right]\gamma^{pq}\epsilon^i.
\end{aligned}\tag{H47}
```

Here the bivector coefficient multiplies the full ordered sum
$`\gamma^{pq}`$ directly; no additional $`1/2`$ is implicit. This is why its
coefficients are half of the old array entries. Every term is expressed
in the original fields, with no coefficient-array definition to consult.

### 27.2 Add the two direct SU(2)-curvature-square contributions

The three curvature-square terms at the end of H42 and the one at the
end of H45 give

```math
\begin{aligned}
&\widehat R(V)^{ab\,kl}\widehat R(V)_{cd\,kl}
\left[-\tfrac1{24}\gamma_{ab}{}^{cd}
+\tfrac1{24}\gamma^{cd}\gamma_{ab}
+\tfrac1{48}\gamma_{ab}\gamma^{cd}
+\tfrac1{48}\gamma_{ab}\gamma^{cd}\right]\epsilon^i\\
&\quad=\widehat R(V)^{ab\,kl}\widehat R(V)_{cd\,kl}
\left[\tfrac1{24}\gamma_{ab}{}^{cd}
+\tfrac1{12}(\delta_a^d\delta_b^c-\delta_a^c\delta_b^d)\right]\epsilon^i\\
&\quad=-\tfrac16\widehat R(V)_{ab}^{kl}\widehat R(V)^{ab}{}_{kl}\epsilon^i
+\tfrac i{24}\epsilon_{pabcd}
\widehat R(V)^{ab\,kl}\widehat R(V)^{cd}{}_{kl}\gamma^p\epsilon^i.
\end{aligned}\tag{H48}
```

In the second line use the sum of the two ordered gamma products from
H10. Their two-gamma terms cancel; their scalar metric terms are equal.
The contractions in the last line give $`-2\widehat R(V)^2/12`$ and the
rank-four duality gives $`i/24`$. This works for the full hatted curvatures.
The doublet labels $`k,l`$ are dummy indices; $`i`$ belongs only to the final
parameter and is not reused inside the curvature contraction.

For comparison, the direct curvature-square term in H15 gives

```math
-\tfrac1{32}\widehat C^{abcd}\widehat C_{ab}{}^{ef}
\gamma_{cd}\gamma_{ef}\epsilon^i
=\tfrac1{16}\widehat C_{abcd}\widehat C^{abcd}\epsilon^i
-\tfrac i{32}\epsilon_{pabcd}
\widehat C_{ef}{}^{ab}\widehat C^{ef\,cd}\gamma^p\epsilon^i.
\tag{H49}
```

The two scalar contractions contribute $`+\widehat C^2/32`$ each. The
product of the two even curvatures is symmetric under exchange of their
remaining pair labels, so its contraction with the antisymmetric
bivector part is zero. This does not assume pair-exchange symmetry of
the full supercovariant Weyl curvature.

### 27.3 The six contributions to finish

The six entries of H50 are the terms omitted from the sums H15–H45:

```math
\begin{aligned}
&-\tfrac18\gamma_{cd}\widehat R(Q)_{ab}^i\delta_Q\widehat C^{abcd},\\
&-4i\gamma_c\widehat R(Q)_{ab}^i\delta_Q(\mathcal D^aT^{bc}),\\
&+8i\gamma_cT^{ab}\delta_Q(\mathcal D^c\widehat R(Q)_{ab}^i),\\
&+8i\gamma_aT^{ab}\delta_Q(\mathcal D^c\widehat R(Q)_{bc}^i),\\
&-\tfrac{64i}{3}\gamma^{ab}\gamma^c\chi^i\delta_Q(\mathcal D_aT_{bc}),\\
&+\tfrac{128i}{3}\gamma_aT^{ab}\delta_Q(\mathcal D_b\chi^i).
\end{aligned}\tag{H50}
```

The calculation below evaluates all six. The equalities refer to the
adopted M08 and the master C/W/G/R laws. No field equation, global gauge
condition, boundary manipulation or fermion truncation is introduced.
The notation $`\left.\cdots\right|_{\epsilon^i}`$ continues to mean the
SU(2)-identity part **after** the Majorana flip and Fierz rearrangement;
it never means dropping a repeated doublet label before rearranging it.

First vary the original derivative, including its connections:

```math
\mathcal D_aT_{bc}=e_a{}^\mu\left[
\partial_\mu T_{bc}-b_\mu T_{bc}
+\omega_{\mu b}{}^dT_{dc}+\omega_{\mu c}{}^dT_{bd}
-\tfrac i2\bar\psi_\mu\gamma_{bc}\chi
+\tfrac{3i}{32}\bar\psi_\mu\widehat R(Q)_{bc}\right].
\tag{H51}
```

Its product rule, before any simplification, is

```math
\begin{aligned}
\delta_Q(\mathcal D_aT_{bc})={}&
-\tfrac12(\bar\epsilon\gamma^d\psi_a)\mathcal D_dT_{bc}\\
&+e_a{}^\mu\big[
\partial_\mu(\delta_QT_{bc})-b_\mu\delta_QT_{bc}
+\omega_{\mu b}{}^d\delta_QT_{dc}
+\omega_{\mu c}{}^d\delta_QT_{bd}\\
&\hspace{13mm}-(\delta_Qb_\mu)T_{bc}
+(\delta_Q\omega_{\mu b}{}^d)T_{dc}
+(\delta_Q\omega_{\mu c}{}^d)T_{bd}\\
&\hspace{13mm}-\tfrac i2(\delta_Q\bar\psi_\mu)\gamma_{bc}\chi
-\tfrac i2\bar\psi_\mu\gamma_{bc}\delta_Q\chi
+\tfrac{3i}{32}(\delta_Q\bar\psi_\mu)\widehat R(Q)_{bc}
+\tfrac{3i}{32}\bar\psi_\mu\delta_Q\widehat R(Q)_{bc}\big].
\end{aligned}\tag{H52}
```

#### Computing covariant coefficients at one point

A useful way to evaluate these product rules without inventing response
fields is to choose a local normal frame **only for the intermediate
calculation at a point** $`x_0`$:

```math
\left.e_a{}^\mu\right|_{x_0}=\delta_a{}^\mu,
\qquad
\left.(b_\mu,\omega_\mu{}^{ab},V_\mu{}^{ij},
\psi_\mu^i,\phi_\mu^i,f_\mu{}^a)\right|_{x_0}=0.
\tag{H54}
```

Here one uses the first jets of the local gauge parameters to remove
connection values. Those parameters can have zero values at $`x_0`$;
therefore covariant fields and their covariant derivatives at $`x_0`$ are
unchanged. The constraints defining $`\omega,\phi,f`$ restrict the jets of
the independent fields, rather than setting their curvatures to zero.
For example, the gamma-trace of $`2\partial_{[a}\psi_{b]}`$ vanishes when
$`\phi=0`$, but its gamma-traceless part is the arbitrary nonzero
$`\widehat R(Q)_{ab}`$. Antisymmetric derivatives of the connections remain
curvatures. We do **not** differentiate a zero connection as if it were
zero in a neighborhood.

All objects in H50 are tangent covariants defined using G01 and G03.
Their Q-laws have no derivatives of the local parameter: this is the
purpose of the Q/S connection subtractions in G01. P41–P46 already check
the first-parameter-derivative cancellations directly. Thus their
coefficients may be evaluated in H54 and written back in terms of the
same full covariant fields. This is the covariant normal-frame argument,
not a restriction to a background with zero physical fermions. In
particular $`\chi`$, $`\widehat R(Q)`$, $`\widehat R(S)`$ and every covariant
fermion derivative below remain arbitrary. The final expressions contain
full hatted curvatures and full $`\mathcal D`$, with all their gravitino
and dependent-connection terms.

Choose the first jet of the **test Q parameter** so that its gravitino
variation vanishes at the evaluation point:

```math
\left.\partial_a\epsilon^i\right|_{x_0}
=-i(\gamma\!\cdot\!T)\gamma_a\epsilon^i,
\qquad
\left.\partial_a\bar\epsilon\right|_{x_0}
=+i\bar\epsilon\gamma_a(\gamma\!\cdot\!T),
\qquad
\delta_Q\psi_a^i=0,
\quad\delta_Qe_\mu{}^a=0.
\tag{H55}
```

The plus sign in the barred equation follows from the **linear** bar and
$`\widetilde{(\gamma\!\cdot\!T)\gamma_a} =-\gamma_a(\gamma\!\cdot\!T)`$. This sets a first jet at one point; it
does not impose a Killing-spinor equation or a condition on second jets.
In particular $`\partial_{[a}\delta\psi_{b]}`$ need not vanish. From W01
and R04a the remaining connection variations there are

```math
\begin{aligned}
\delta_Q b_a&=-2\bar\epsilon\gamma_a\chi,\\
\delta_Q V_a^{ij}&=4\bar\epsilon^{(i}\gamma_a\chi^{j)},\\
\delta_Q\omega_a{}^{de}&=
-\tfrac12\bar\epsilon\gamma^{[d}\widehat R(Q)_a{}^{e]}
-\tfrac14\bar\epsilon\gamma_a\widehat R(Q)^{de}
-4\delta_a{}^{[d}\bar\epsilon\gamma^{e]}\chi.
\end{aligned}\tag{H56}
```

All connection variations in H56 are retained. The $`\phi`$ and $`\psi`$
terms in R04a vanish as **values**, but their derivatives must still be
included when varying a curvature; H63 below does exactly that.

### 27.4 Derive the needed S-connection coefficient

<!-- ASSERT_CONVENTION: natural_units=hbar=c=1, metric_signature=(-,+,+,+,+); master C01, source_lock=UNG-WEYL2-OP58-CONVENTIONS-v5 -->

We use its definition R04b, not the incomplete printed transformation.
At the point H54, varying R01 and inserting H55 gives

```math
\begin{aligned}
\left.\delta_Q\widehat R'(Q)_{ab}^i\right|_{\epsilon^i}
={}&\big[\tfrac14\widehat C_{ab}{}^{cd}\gamma_{cd}
+i\gamma^{cd}(\mathcal D_aT_{cd})\gamma_b
-i\gamma^{cd}(\mathcal D_bT_{cd})\gamma_a\\
&\quad-(\gamma\!\cdot\!T)\gamma_a(\gamma\!\cdot\!T)\gamma_b
+(\gamma\!\cdot\!T)\gamma_b(\gamma\!\cdot\!T)\gamma_a\big]\epsilon^i.
\end{aligned}\tag{H57}
```

For clarity, the two quadratic terms come from the commutator
$`[i(\gamma\!\cdot\!T)\gamma_a, i(\gamma\!\cdot\!T)\gamma_b]`$ when differentiating
$`\delta\psi_b`$; they survive although $`\delta\psi_b(x_0)=0`$.
The SU(2)-curvature term has zero singlet trace and is not used in H57.
No fermion-bilinear term in the variation of R01 survives separately at
this point: its other factor is $`\psi`$, $`\phi`$ or $`\delta\psi`$. Their
covariant content is retained by $`\widehat C`$ and $`\mathcal D T`$.

Insert H57 into
$`\delta\phi_a=i\gamma^b\delta\widehat R'(Q)_{ab}/3 -i\gamma_a\gamma^{bc}\delta\widehat R'(Q)_{bc}/24`$.
The two curvature contractions vanish by the trace and cyclic
constraints G03: expand $`\gamma^b\gamma^{cd}=\gamma^{bcd} +\eta^{bc}\gamma^d-\eta^{bd}\gamma^c`$; its last two terms contract a
Lorentz-curvature trace, and the first contracts the cyclic part.
The four-gamma contraction in the second term gives the same traces and
the completely antisymmetric cyclic part. The remaining derivative terms
are, before reduction,

```math
\begin{aligned}
&-\tfrac13\gamma^b\gamma^{cd}(\mathcal D_aT_{cd})\gamma_b
+\tfrac13\gamma^b\gamma^{cd}(\mathcal D_bT_{cd})\gamma_a\\
&\qquad+\tfrac1{12}\gamma_a\gamma^{bc}\gamma^{de}
(\mathcal D_bT_{de})\gamma_c\\
={}&-\tfrac13\gamma^{cd}\mathcal D_aT_{cd}
+\tfrac13\gamma^b\gamma^{cd}(\mathcal D_bT_{cd})\gamma_a
+\tfrac13\gamma_a\gamma^c\mathcal D^bT_{bc}.
\end{aligned}\tag{H58}
```

Here $`\gamma^b\gamma^{cd}\gamma_b=(5-4)\gamma^{cd}`$, and
$`\gamma^{bc}(\gamma\!\cdot\!T)\gamma_c =\gamma^b(\gamma\!\cdot\!T)-(\gamma\!\cdot\!T)\gamma^b =4T^b{}_c\gamma^c`$.
The quadratic terms, with their order preserved, give

```math
\begin{aligned}
&-\tfrac i3\gamma^b(\gamma\!\cdot\!T)\gamma_a
 (\gamma\!\cdot\!T)\gamma_b
+\tfrac i3\gamma^b(\gamma\!\cdot\!T)\gamma_b
 (\gamma\!\cdot\!T)\gamma_a\\
&\qquad+\tfrac i{12}\gamma_a\gamma^{bc}
 (\gamma\!\cdot\!T)\gamma_b(\gamma\!\cdot\!T)\gamma_c\\
={}&i\big[-\gamma_{abcde}T^{bc}T^{de}
+8\gamma_bT^{bc}T_{ac}-2\gamma_aT^2\big].
\end{aligned}\tag{H59}
```

The three products on the first two lines reduce separately as follows:

```math
\begin{aligned}
\gamma^b(\gamma\!\cdot\!T)\gamma_a(\gamma\!\cdot\!T)\gamma_b
&=5\gamma_{abcde}T^{bc}T^{de}
 -24\gamma_bT^{bc}T_{ac}+6\gamma_aT^2,\\
(\gamma\!\cdot\!T)^2\gamma_a
&=\gamma_{abcde}T^{bc}T^{de}
 -4\gamma^{bcd}T_{ab}T_{cd}-2\gamma_aT^2,\\
\gamma_a\gamma^{bc}(\gamma\!\cdot\!T)\gamma_b
 (\gamma\!\cdot\!T)\gamma_c
&=4\gamma_{abcde}T^{bc}T^{de}
 +16\gamma^{bcd}T_{ab}T_{cd}+8\gamma_aT^2.
\end{aligned}\tag{H59a}
```

To obtain the first line, first expand
$`(\gamma\!\cdot\!T)\gamma_a(\gamma\!\cdot\!T) =\gamma_{abcde}T^{bc}T^{de}+8\gamma_bT^{bc}T_{ac} -2\gamma_aT^2`$, then use
$`\gamma^b\gamma_{(r)}\gamma_b=(-1)^r(5-2r)\gamma_{(r)}`$
for $`r=5,1`$. For the second, expand
$`(\gamma\!\cdot\!T)^2=\gamma^{bcde}T_{bc}T_{de}-2T^2`$
and multiply on the right by $`\gamma_a`$; the four single contractions
give $`-4\gamma^{bcd}T_{ab}T_{cd}`$. For the third, first contract
$`\gamma^{bc}(\gamma\!\cdot\!T)\gamma_b=-4T^c{}_d\gamma^d`$,
then expand the remaining $`\gamma^d\gamma^{ef}\gamma_c`$.
The rank-five, rank-three and rank-one coefficients in H59 are consequently

```math
-\tfrac53+\tfrac13+\tfrac4{12}=-1,\qquad
-\tfrac43+\tfrac{16}{12}=0,\qquad
8\gamma_bT^{bc}T_{ac}
+(-2-\tfrac23+\tfrac8{12})\gamma_aT^2
=8\gamma_bT^{bc}T_{ac}-2\gamma_aT^2.
\tag{H59b}
```

Combining H58 and H59 gives the needed singlet coefficient:

```math
\begin{aligned}
\left.\delta_Q\phi_a^i\right|_{\epsilon^i,x_0}
={}&\big[\tfrac13\gamma^f\gamma^{de}(\mathcal D_fT_{de})\gamma_a
-\tfrac13\gamma^{de}\mathcal D_aT_{de}
+\tfrac13\gamma_a\gamma^e\mathcal D^dT_{de}\\
&\quad-i\gamma_{adefg}T^{de}T^{fg}
+8i\gamma_dT^{de}T_{ae}-2i\gamma_aT^2\big]\epsilon^i.
\end{aligned}\tag{H60}
```

H60 is an evaluation at H54, where $`f_a{}^b=0`$. It is **not** asserted
to be the full connection transformation in an arbitrary frame. The
arbitrary-frame definition remains R04b. Its use below is inside the
normal-frame evaluation of a covariant derivative.

### 27.5 Evaluate the tensor-derivative variation

<!-- ASSERT_CONVENTION: natural_units=hbar=c=1, metric_signature=(-,+,+,+,+); master C01, source_lock=UNG-WEYL2-OP58-CONVENTIONS-v5 -->

In H52 the inverse-frame term and the terms proportional to $`\psi`$ or
$`\delta\psi`$ vanish as point values. The derivative of the parameter
does not vanish. Inserting H55 into the two differentiated bilinears gives

```math
\begin{aligned}
\partial_a(\tfrac i2\bar\epsilon\gamma_{bc}\chi)
&=\tfrac i2\bar\epsilon\gamma_{bc}\mathcal D_a\chi
-\tfrac12\bar\epsilon\gamma_a(\gamma\!\cdot\!T)\gamma_{bc}\chi,\\
\partial_a(-\tfrac{3i}{32}\bar\epsilon\widehat R(Q)_{bc})
&=-\tfrac{3i}{32}\bar\epsilon\mathcal D_a\widehat R(Q)_{bc}
+\tfrac3{32}\bar\epsilon\gamma_a(\gamma\!\cdot\!T)\widehat R(Q)_{bc}.
\end{aligned}\tag{H61}
```

Now insert all three connection variations from H56 into H52. Restoring
covariant notation gives the following eleven actual terms:

```math
\begin{aligned}
\delta_Q(\mathcal D_aT_{bc})={}&\frac{i}{2}\bar\epsilon \gamma_{bc}\mathcal D_a\chi\\
&-\frac{3i}{32}\bar\epsilon \mathcal D_a\widehat R(Q)_{bc}\\
&-\frac{1}{2}\bar\epsilon \gamma_a(\gamma\!\cdot\!T)\gamma_{bc}\chi\\
&+\frac{3}{32}\bar\epsilon \gamma_a(\gamma\!\cdot\!T)\widehat R(Q)_{bc}\\
&+2T_{bc}\bar\epsilon \gamma_a\chi\\
&-\frac{1}{2}T_{dc}\bar\epsilon \gamma_{[b}\widehat R(Q)_a{}^{d]}\\
&-\frac{1}{4}T_{dc}\bar\epsilon \gamma_a\widehat R(Q)_b{}^d\\
&-4\eta_{a[b}T_{dc}\bar\epsilon \gamma^{d]}\chi\\
&-\frac{1}{2}T_{bd}\bar\epsilon \gamma_{[c}\widehat R(Q)_a{}^{d]}\\
&-\frac{1}{4}T_{bd}\bar\epsilon \gamma_a\widehat R(Q)_c{}^d\\
&-4\eta_{a[c}T_{bd}\bar\epsilon \gamma^{d]}\chi
\end{aligned}\tag{H62}
```

The eleven lines are respectively: two derivatives of physical fermions,
two finite parameter-derivative terms, one dilatation-connection term,
and three terms from each Lorentz covector index. In particular the
second tensor connection has not been inferred to cancel the first.
Each line has weight $`5/2`$ after removing $`\bar\epsilon`$, as required
for the variation of a weight-two derivative.

### 27.6 Evaluate curvature and spinor-derivative variations

<!-- ASSERT_CONVENTION: natural_units=hbar=c=1, metric_signature=(-,+,+,+,+); master C01, source_lock=UNG-WEYL2-OP58-CONVENTIONS-v5 -->

#### Vary the curvature before making contractions

Differentiate the **full** R04a before imposing the point values H54.
The derivatives of its first two terms give, respectively,
$`\tfrac i2\bar\epsilon\gamma_{cd}\widehat R(S)_{ab}`$ and
$`-i\bar\epsilon\gamma_{[c}(\gamma\!\cdot\!T)\gamma_{d]} \widehat R(Q)_{ab}`$, since
$`2\partial_{[a}\phi_{b]}=\widehat R(S)_{ab}`$ and
$`2\partial_{[a}\psi_{b]}=\widehat R(Q)_{ab}`$ at this point.
The other three terms of R04a give two terms each, one when the derivative
hits $`\epsilon`$ and one when it hits the physical fermion. Thus

```math
\begin{aligned}
\left.\delta_Q\widehat R'(M)_{ab cd}\right|_{x_0}
={}&\tfrac i2\bar\epsilon\gamma_{cd}\widehat R(S)_{ab}
-i\bar\epsilon\gamma_{[c}(\gamma\!\cdot\!T)\gamma_{d]}
 \widehat R(Q)_{ab}\\
&-\bar\epsilon\gamma_{[c}\mathcal D_{[a}\widehat R(Q)_{b]d]}
-i\bar\epsilon\gamma_{[a}(\gamma\!\cdot\!T)\gamma_{[c}
 \widehat R(Q)_{b]d]}\\
&+\tfrac12\bar\epsilon\gamma_{[a}\mathcal D_{b]}
 \widehat R(Q)_{cd}
-\tfrac i2\bar\epsilon\gamma_{[a}(\gamma\!\cdot\!T)\gamma_{b]}
 \widehat R(Q)_{cd}\\
&-8\eta_{[b[c}\bar\epsilon\gamma_{d]}\mathcal D_{a]}\chi
-8i\eta_{[b[c}\bar\epsilon\gamma_{a]}
 (\gamma\!\cdot\!T)\gamma_{d]}\chi.
\end{aligned}\tag{H63}
```

The brackets on $`a,b`$ and $`c,d`$ act independently. For example, the last
line is $`-8\eta_{[b[c}\{\bar\epsilon\gamma_{d]}\mathcal D_{a]}\chi +i\bar\epsilon\gamma_{a]}(\gamma\!\cdot\!T)\gamma_{d]}\chi\}`$.
No field strength was replaced by zero.

For completeness, the fourteen varied fermion terms P26 vanish here as
follows. The first pair has factors $`(\delta\bar\phi)\psi`$ and
$`\bar\phi\delta\psi`$; the next three have factors
$`(\delta\bar\psi)\psi`$, $`\bar\psi(\delta T)\psi`$,
$`\bar\psi\delta\psi`$; the next two triples have factors
$`\delta\bar\psi`$, $`\bar\psi\delta e`$, $`\bar\psi\delta\widehat R(Q)`$;
the last triple has factors $`\delta\bar\psi`$, $`\bar\psi\delta e`$,
$`\bar\psi\delta\chi`$. Every listed product contains a factor whose
**value** is zero in H54–H55. The two inverse-frame variations also have
$`\delta e=0`$. These facts explain the reduction of P24–P29, rather than
omitting their fermionic terms. The surviving derivatives of $`\psi`$ and
$`\phi`$ have already been kept in H63.

Eliminate $`\widehat R(S)`$ by substituting all six terms of R06b. The
coefficient products are
$`(i/2)(-i)=1/2`$, $`(i/2)(-8/3)=-4i/3`$,
$`(i/2)12=6i`$, $`(i/2)(-3)=-3i/2`$, and $`(i/2)(-8)=-4i`$:

```math
\begin{aligned}
\left.\delta_Q\widehat R'(M)_{ab cd}\right|_{x_0}={}&\frac{1}{2}\bar\epsilon \gamma_{cd}\gamma^e\mathcal D_e\widehat R(Q)_{ab}\\
&+\frac{1}{2}\bar\epsilon \gamma_{cd}\gamma_{[a}\mathcal D^e\widehat R(Q)_{b]e}\\
&-\frac{4i}{3}T^{ef}\bar\epsilon \gamma_{cd}\gamma_{ab}\widehat R(Q)_{ef}\\
&+6iT^{ef}\bar\epsilon \gamma_{cd}\gamma_f\gamma_{[a}\widehat R(Q)_{b]e}\\
&-\frac{3i}{2}\bar\epsilon \gamma_{cd}(\gamma\!\cdot\!T)\widehat R(Q)_{ab}\\
&-4iT^e{}_{[a}\bar\epsilon \gamma_{cd}\widehat R(Q)_{b]e}\\
&-i\bar\epsilon \gamma_{[c}(\gamma\!\cdot\!T)\gamma_{d]}\widehat R(Q)_{ab}\\
&-\bar\epsilon \gamma_{[c}\mathcal D_{[a}\widehat R(Q)_{b]d]}\\
&-i\bar\epsilon \gamma_{[a}(\gamma\!\cdot\!T)\gamma_{[c}\widehat R(Q)_{b]d]}\\
&+\frac{1}{2}\bar\epsilon \gamma_{[a}\mathcal D_{b]}\widehat R(Q)_{cd}\\
&-\frac{i}{2}\bar\epsilon \gamma_{[a}(\gamma\!\cdot\!T)\gamma_{b]}\widehat R(Q)_{cd}\\
&-8\eta_{[b[c}\bar\epsilon \gamma_{d]}\mathcal D_{a]}\chi\\
&-8i\eta_{[b[c}\bar\epsilon \gamma_{a]}(\gamma\!\cdot\!T)\gamma_{d]}\chi
\end{aligned}\tag{H64}
```

The dependent $`f`$ variation must also be included. With all indices
lowered, R03 and R04d give

```math
\begin{aligned}
\delta_Q\widehat C_{ab cd}
&=\delta_Q\widehat R'(M)_{ab cd}
 +8(\delta_Q f_{[a[c})\eta_{b]d]},\\
\gamma^{cd}\widehat R(Q)^{ab}\,8(\delta_Q f_{[a[c})\eta_{b]d]}
&=2\gamma^{cd}\widehat R(Q)^{ab}
 [\delta f_{ac}\eta_{bd}-\delta f_{bc}\eta_{ad}
  -\delta f_{ad}\eta_{bc}+\delta f_{bd}\eta_{ac}]\\
&=-8\widehat R(Q)^{ab}\delta f_{ab},\\
\widehat R(Q)^{ab}\delta f_{ab}
&=-\tfrac16\widehat R(Q)^{ab}\eta^{cd}
 \delta_Q\widehat R'(M)_{acbd}
 +\tfrac1{48}\widehat R(Q)^{ab}\eta_{ab}\delta\mathcal R\\
&=-\tfrac16\widehat R(Q)^{ab}\eta^{cd}
 \delta_Q\widehat R'(M)_{acbd}.
\end{aligned}\tag{H65a}
```

In the second equality use $`\gamma_b\widehat R(Q)^{ab}=0`$ and
$`\gamma^c\gamma_b=\gamma^c{}_b+\delta^c_b`$; the four contractions
give four copies of $`-\widehat R(Q)^{ab}\delta f_{ab}`$ before the
outside factor two. The scalar trace in the next line is zero because
$`\widehat R(Q)^{ab}`$ is antisymmetric and $`\eta_{ab}`$ is symmetric.
Consequently the first line of H50 is exactly

```math
-\tfrac18\gamma^{cd}\widehat R(Q)^{ab\,i}
 \delta_Q\widehat R'(M)_{ab cd}
-\tfrac16\widehat R(Q)^{ab\,i}\eta^{cd}
 \delta_Q\widehat R'(M)_{acbd}.
\tag{H65b}
```

Both pieces are expanded below. Keeping the second one explicitly avoids
using a Ricci-symmetry simplification to conceal a dependent-connection
contribution. If such a trace identity is applied later, it must be applied
to its entire displayed sum.

#### The derivative of $`\chi`$

Use P34, H54–H56 and the six terms of H60. The thirteen terms in P35
supply the derivatives of the Q coefficients and their products with
$`\partial_a\epsilon=-i(\gamma\!\cdot\!T)\gamma_a\epsilon`$.
The two SU(2)-curvature terms have zero trace. Both differentiated $`T`$
factors are kept separately. The term $`-\tfrac14(\gamma\!\cdot\!T) \delta\phi_a`$ gives the last six parameter-right terms below.
The remaining five products come from $`-\tfrac32\delta b_a\chi`$,
$`\tfrac14\delta\omega_a{}^{de}\gamma_{de}\chi`$ (three terms),
and $`-\delta V_a^{ij}\chi_j`$:

```math
\begin{aligned}
\delta_Q(\mathcal D_a\chi^i)\equiv{}&\frac{1}{4}\mathcal D_aD\epsilon^i\\
&+\frac{i}{8}\gamma^{de}\gamma^f\mathcal D_a\mathcal D_fT_{de}\epsilon^i\\
&-\frac{i}{8}\gamma^d\mathcal D_a\mathcal D^eT_{de}\epsilon^i\\
&-\frac{1}{4}\gamma^{defg}(\mathcal D_aT_{de})T_{fg}\epsilon^i\\
&-\frac{1}{4}\gamma^{defg}T_{de}(\mathcal D_aT_{fg})\epsilon^i\\
&+\frac{1}{3}T^{de}\mathcal D_aT_{de}\epsilon^i\\
&-\frac{i}{4}D(\gamma\!\cdot\!T)\gamma_a\epsilon^i\\
&+\frac{1}{8}\gamma^{de}\gamma^f(\mathcal D_fT_{de})(\gamma\!\cdot\!T)\gamma_a\epsilon^i\\
&-\frac{1}{8}\gamma^d(\mathcal D^eT_{de})(\gamma\!\cdot\!T)\gamma_a\epsilon^i\\
&+\frac{i}{4}\gamma^{defg}T_{de}T_{fg}(\gamma\!\cdot\!T)\gamma_a\epsilon^i\\
&-\frac{i}{6}T^2(\gamma\!\cdot\!T)\gamma_a\epsilon^i\\
&-\frac{1}{12}(\gamma\!\cdot\!T)\gamma^f\gamma^{de}(\mathcal D_fT_{de})\gamma_a\epsilon^i\\
&+\frac{1}{12}(\gamma\!\cdot\!T)\gamma^{de}(\mathcal D_aT_{de})\epsilon^i\\
&-\frac{1}{12}(\gamma\!\cdot\!T)\gamma_a\gamma^e(\mathcal D^dT_{de})\epsilon^i\\
&+\frac{i}{4}(\gamma\!\cdot\!T)\gamma_{adefg}T^{de}T^{fg}\epsilon^i\\
&-2i(\gamma\!\cdot\!T)\gamma_dT^{de}T_{ae}\epsilon^i\\
&+\frac{i}{2}(\gamma\!\cdot\!T)\gamma_aT^2\epsilon^i\\
&+3\chi{}^i\big(\bar\epsilon \gamma_a\chi\big)\\
&-\frac{1}{8}\gamma_{de}\chi{}^i\big(\bar\epsilon \gamma^{[d}\widehat R(Q)_a{}^{e]}\big)\\
&-\frac{1}{16}\gamma_{de}\chi{}^i\big(\bar\epsilon \gamma_a\widehat R(Q)^{de}\big)\\
&-\delta_a{}^{[d}\gamma_{de}\chi{}^i\big(\bar\epsilon \gamma^{e]}\chi\big)\\
&+4\bar\epsilon^{(i}\gamma_a\chi^{k)}\varepsilon_{kl}\chi{}^l
\end{aligned}\tag{H66}
```

The symbol $`\equiv`$ in H66 and H67b means equality modulo an already-parameter-right traceless SU(2) coefficient. H66 is understood modulo the omitted traceless SU(2) coefficient in its
parameter-right terms; the displayed fermion products must still be
Fierzed before that projection. In particular the last line is retained.
The sign is $`-\delta V^{ij}\chi_j =+\delta V^{ik}\varepsilon_{kl}\chi^l`$ in the NW–SE convention.

#### The derivative of $`\widehat R(Q)`$

P37 supplies the same weight and spin connections and, in addition,
a Lorentz connection for each of its lower curvature indices. The ten
parameter-right terms from the singlet part of P38 are the derivative of
$`\widehat C`$ (one), second derivatives of $`T`$ (four), and their five
products with $`-i(\gamma\!\cdot\!T)\gamma_a`$. Finally multiply the
three terms of minus the S-generator in R05 by all six terms of H60:

```math
\begin{aligned}
-\left[-8T_{bc}+\tfrac{16}{3}T_{[b}{}^d\gamma_{c]d}
 +\tfrac43\gamma_{bcde}T^{de}\right]\delta_Q\phi_a^i.
\end{aligned}\tag{H67a}
```

The resulting $`3\times6=18`$ products follow the first ten lines below.
The last eleven products are the weight term, three spin terms, the
SU(2) term, and three terms for each Lorentz covector index. Dummy indices
$`h,r,s,t`$ in the S-connection products keep their contractions distinct
from the $`d,e`$ in H67a.

```math
\begin{aligned}
\delta_Q(\mathcal D_a\widehat R(Q)_{bc}^i)\equiv{}&\frac{1}{4}(\mathcal D_a\widehat C_{bc}{}^{de})\gamma_{de}\epsilon^i\\
&+2i\gamma^{de}(\mathcal D_a\mathcal D_{[b}T_{de})\gamma_{c]}\epsilon^i\\
&-\frac{2i}{3}\gamma_{[c}\gamma^{de}(\mathcal D_a\mathcal D_{b]}T_{de})\epsilon^i\\
&-\frac{2i}{3}\gamma_{[b}\gamma^f\gamma^{de}(\mathcal D_a\mathcal D_fT_{de})\gamma_{c]}\epsilon^i\\
&-\frac{2i}{3}\gamma_{bc}\gamma_d\mathcal D_a\mathcal D_eT^{ed}\epsilon^i\\
&-\frac{i}{4}\widehat C_{bc}{}^{de}\gamma_{de}(\gamma\!\cdot\!T)\gamma_a\epsilon^i\\
&+2\gamma^{de}(\mathcal D_{[b}T_{de})\gamma_{c]}(\gamma\!\cdot\!T)\gamma_a\epsilon^i\\
&-\frac{2}{3}\gamma_{[c}\gamma^{de}(\mathcal D_{b]}T_{de})(\gamma\!\cdot\!T)\gamma_a\epsilon^i\\
&-\frac{2}{3}\gamma_{[b}\gamma^f\gamma^{de}(\mathcal D_fT_{de})\gamma_{c]}(\gamma\!\cdot\!T)\gamma_a\epsilon^i\\
&-\frac{2}{3}\gamma_{bc}\gamma_d(\mathcal D_eT^{ed})(\gamma\!\cdot\!T)\gamma_a\epsilon^i\\
&+\frac{8}{3}T_{bc}\gamma^s\gamma^{hr}(\mathcal D_sT_{hr})\gamma_a\epsilon^i\\
&-\frac{8}{3}T_{bc}\gamma^{hr}(\mathcal D_aT_{hr})\epsilon^i\\
&+\frac{8}{3}T_{bc}\gamma_a\gamma^r(\mathcal D^hT_{hr})\epsilon^i\\
&-8iT_{bc}\gamma_{ahrst}T^{hr}T^{st}\epsilon^i\\
&+64iT_{bc}\gamma_hT^{hr}T_{ar}\epsilon^i\\
&-16iT_{bc}\gamma_aT^2\epsilon^i\\
&-\frac{16}{9}T_{[b}{}^d\gamma_{c]d}\gamma^s\gamma^{hr}(\mathcal D_sT_{hr})\gamma_a\epsilon^i\\
&+\frac{16}{9}T_{[b}{}^d\gamma_{c]d}\gamma^{hr}(\mathcal D_aT_{hr})\epsilon^i\\
&-\frac{16}{9}T_{[b}{}^d\gamma_{c]d}\gamma_a\gamma^r(\mathcal D^hT_{hr})\epsilon^i\\
&+\frac{16i}{3}T_{[b}{}^d\gamma_{c]d}\gamma_{ahrst}T^{hr}T^{st}\epsilon^i\\
&-\frac{128i}{3}T_{[b}{}^d\gamma_{c]d}\gamma_hT^{hr}T_{ar}\epsilon^i\\
&+\frac{32i}{3}T_{[b}{}^d\gamma_{c]d}\gamma_aT^2\epsilon^i\\
&-\frac{4}{9}\gamma_{bcde}T^{de}\gamma^s\gamma^{hr}(\mathcal D_sT_{hr})\gamma_a\epsilon^i\\
&+\frac{4}{9}\gamma_{bcde}T^{de}\gamma^{hr}(\mathcal D_aT_{hr})\epsilon^i\\
&-\frac{4}{9}\gamma_{bcde}T^{de}\gamma_a\gamma^r(\mathcal D^hT_{hr})\epsilon^i\\
&+\frac{4i}{3}\gamma_{bcde}T^{de}\gamma_{ahrst}T^{hr}T^{st}\epsilon^i\\
&-\frac{32i}{3}\gamma_{bcde}T^{de}\gamma_hT^{hr}T_{ar}\epsilon^i\\
&+\frac{8i}{3}\gamma_{bcde}T^{de}\gamma_aT^2\epsilon^i\\
&+3\widehat R(Q)_{bc}{}^i\big(\bar\epsilon \gamma_a\chi\big)\\
&-\frac{1}{8}\gamma_{de}\widehat R(Q)_{bc}{}^i\big(\bar\epsilon \gamma^{[d}\widehat R(Q)_a{}^{e]}\big)\\
&-\frac{1}{16}\gamma_{de}\widehat R(Q)_{bc}{}^i\big(\bar\epsilon \gamma_a\widehat R(Q)^{de}\big)\\
&-\delta_a{}^{[d}\gamma_{de}\widehat R(Q)_{bc}{}^i\big(\bar\epsilon \gamma^{e]}\chi\big)\\
&+4\bar\epsilon^{(i}\gamma_a\chi^{k)}\varepsilon_{kl}\widehat R(Q)_{bc}{}^l\\
&-\frac{1}{2}\widehat R(Q)_{dc}{}^i\big(\bar\epsilon \gamma_{[b}\widehat R(Q)_a{}^{d]}\big)\\
&-\frac{1}{4}\widehat R(Q)_{dc}{}^i\big(\bar\epsilon \gamma_a\widehat R(Q)_b{}^d\big)\\
&-4\eta_{a[b}\widehat R(Q)_{dc}{}^i\big(\bar\epsilon \gamma^{d]}\chi\big)\\
&-\frac{1}{2}\widehat R(Q)_{bd}{}^i\big(\bar\epsilon \gamma_{[c}\widehat R(Q)_a{}^{d]}\big)\\
&-\frac{1}{4}\widehat R(Q)_{bd}{}^i\big(\bar\epsilon \gamma_a\widehat R(Q)_c{}^d\big)\\
&-4\eta_{a[c}\widehat R(Q)_{bd}{}^i\big(\bar\epsilon \gamma^{d]}\chi\big)
\end{aligned}\tag{H67b}
```

As in H66, only the already-parameter-right SU(2)-traceless terms have
been suppressed in H67b. All eleven fermion products are retained for
Fierz. No second derivatives have been commuted: for example
$`\mathcal D_a\mathcal D_fT_{de}`$ retains that exact order.

#### Majorana transposes and the SU(2) trace

Every rearrangement below uses H05 or H08 with actual spinors. The
additional gamma-product transposes needed here are

```math
\begin{aligned}
\widetilde{\gamma_{cd}\gamma^e}&=-\gamma^e\gamma_{cd},&
\widetilde{\gamma_{cd}\gamma_{ab}}&=\gamma_{ab}\gamma_{cd},\\
\widetilde{\gamma_{cd}\gamma_f\gamma_a}&=-\gamma_a\gamma_f\gamma_{cd},&
\widetilde{\gamma_{cd}(\gamma\!\cdot\!T)}
&=(\gamma\!\cdot\!T)\gamma_{cd},\\
\widetilde{\gamma_a(\gamma\!\cdot\!T)\gamma_{bc}}
&=\gamma_{bc}(\gamma\!\cdot\!T)\gamma_a,&
\widetilde{\gamma_a(\gamma\!\cdot\!T)}
&=-(\gamma\!\cdot\!T)\gamma_a,\\
\widetilde{\gamma_a(\gamma\!\cdot\!T)\gamma_c}
&=-\gamma_c(\gamma\!\cdot\!T)\gamma_a,&
\widetilde{\gamma_{[a}(\gamma\!\cdot\!T)\gamma_{b]}}
&=\gamma_{[a}(\gamma\!\cdot\!T)\gamma_{b]}.
\end{aligned}\tag{H68}
```

The last equality uses both the minus from transposing $`\gamma\!\cdot\!T`$
and the minus from interchanging $`a,b`$ in the antisymmetrization.
In each Fierz equality below the weighted antisymmetrizations of the input are expanded explicitly. Thus no closing antisymmetry bracket has to be read before an opening one after the spinor pairing changes. The exterior spinor and exterior gamma factors are not part of those antisymmetrizations. Every coefficient includes the corresponding factors of $`1/2`$, these transpose signs, and the H05 factors
$`(1/8,1/8,-1/16)`$. For the symmetric SU(2) connection the H08 factors
are $`(3/16,3/16,-3/32)`$. For example, in H66 the weight and SU(2)
connection terms contribute to the same three bilinears, so their
coefficients add as

```math
3(\tfrac18,\tfrac18,-\tfrac1{16})
+4(\tfrac3{16},\tfrac3{16},-\tfrac3{32})
=(\tfrac98,\tfrac98,-\tfrac9{16}).
\tag{H69}
```

This is the Schouten contribution that would be missed by discarding the
symmetric $`\bar\epsilon^{(i}\chi^{j)}`$ term in advance.

### 27.7 First retained term: varying the Weyl curvature

<!-- ASSERT_CONVENTION: natural_units=hbar=c=1, metric_signature=(-,+,+,+,+); master C01, source_lock=UNG-WEYL2-OP58-CONVENTIONS-v5 -->

**Curvature.** Apply H05 to each of the thirteen terms in H64.

```math
\begin{aligned}
\left.-\frac{1}{16}\gamma^{cd}\widehat R(Q)^{ab}{}^i\big(\bar\epsilon \gamma_{cd}\gamma^e\mathcal D_e\widehat R(Q)_{ab}\big)\right|_{\epsilon^i}={}&\frac{1}{128}\gamma^{cd}\big(\overline{\mathcal D_e\widehat R(Q)_{ab}}\gamma^e\gamma_{cd}\widehat R(Q)^{ab}\big)\epsilon^i\\
&+\frac{1}{128}\gamma^{cd}\big(\overline{\mathcal D_e\widehat R(Q)_{ab}}\gamma^e\gamma_{cd}\gamma_p\widehat R(Q)^{ab}\big)\gamma^p\epsilon^i\\
&-\frac{1}{256}\gamma^{cd}\big(\overline{\mathcal D_e\widehat R(Q)_{ab}}\gamma^e\gamma_{cd}\gamma_{pq}\widehat R(Q)^{ab}\big)\gamma^{pq}\epsilon^i
\end{aligned}\tag{H070}
```

```math
\begin{aligned}
\left.-\frac{1}{16}\gamma^{cd}\widehat R(Q)^{ab}{}^i\big(\bar\epsilon \gamma_{cd}\gamma_{[a}\mathcal D^e\widehat R(Q)_{b]e}\big)\right|_{\epsilon^i}={}&\frac{1}{256}\gamma^{cd}\big(\overline{\mathcal D^e\widehat R(Q)_{be}}\gamma_{a}\gamma_{cd}\widehat R(Q)^{ab}\big)\epsilon^i\\
&+\frac{1}{256}\gamma^{cd}\big(\overline{\mathcal D^e\widehat R(Q)_{be}}\gamma_{a}\gamma_{cd}\gamma_p\widehat R(Q)^{ab}\big)\gamma^p\epsilon^i\\
&-\frac{1}{512}\gamma^{cd}\big(\overline{\mathcal D^e\widehat R(Q)_{be}}\gamma_{a}\gamma_{cd}\gamma_{pq}\widehat R(Q)^{ab}\big)\gamma^{pq}\epsilon^i\\
&-\frac{1}{256}\gamma^{cd}\big(\overline{\mathcal D^e\widehat R(Q)_{ae}}\gamma_{b}\gamma_{cd}\widehat R(Q)^{ab}\big)\epsilon^i\\
&-\frac{1}{256}\gamma^{cd}\big(\overline{\mathcal D^e\widehat R(Q)_{ae}}\gamma_{b}\gamma_{cd}\gamma_p\widehat R(Q)^{ab}\big)\gamma^p\epsilon^i\\
&+\frac{1}{512}\gamma^{cd}\big(\overline{\mathcal D^e\widehat R(Q)_{ae}}\gamma_{b}\gamma_{cd}\gamma_{pq}\widehat R(Q)^{ab}\big)\gamma^{pq}\epsilon^i
\end{aligned}\tag{H071}
```

```math
\begin{aligned}
\left.\frac{i}{6}T^{ef}\gamma^{cd}\widehat R(Q)^{ab}{}^i\big(\bar\epsilon \gamma_{cd}\gamma_{ab}\widehat R(Q)_{ef}\big)\right|_{\epsilon^i}={}&\frac{i}{48}T^{ef}\gamma^{cd}\big(\overline{\widehat R(Q)}_{ef}\gamma_{ab}\gamma_{cd}\widehat R(Q)^{ab}\big)\epsilon^i\\
&+\frac{i}{48}T^{ef}\gamma^{cd}\big(\overline{\widehat R(Q)}_{ef}\gamma_{ab}\gamma_{cd}\gamma_p\widehat R(Q)^{ab}\big)\gamma^p\epsilon^i\\
&-\frac{i}{96}T^{ef}\gamma^{cd}\big(\overline{\widehat R(Q)}_{ef}\gamma_{ab}\gamma_{cd}\gamma_{pq}\widehat R(Q)^{ab}\big)\gamma^{pq}\epsilon^i
\end{aligned}\tag{H072}
```

```math
\begin{aligned}
\left.-\frac{3i}{4}T^{ef}\gamma^{cd}\widehat R(Q)^{ab}{}^i\big(\bar\epsilon \gamma_{cd}\gamma_f\gamma_{[a}\widehat R(Q)_{b]e}\big)\right|_{\epsilon^i}={}&\frac{3i}{64}T^{ef}\gamma^{cd}\big(\overline{\widehat R(Q)}_{be}\gamma_{a}\gamma_f\gamma_{cd}\widehat R(Q)^{ab}\big)\epsilon^i\\
&+\frac{3i}{64}T^{ef}\gamma^{cd}\big(\overline{\widehat R(Q)}_{be}\gamma_{a}\gamma_f\gamma_{cd}\gamma_p\widehat R(Q)^{ab}\big)\gamma^p\epsilon^i\\
&-\frac{3i}{128}T^{ef}\gamma^{cd}\big(\overline{\widehat R(Q)}_{be}\gamma_{a}\gamma_f\gamma_{cd}\gamma_{pq}\widehat R(Q)^{ab}\big)\gamma^{pq}\epsilon^i\\
&-\frac{3i}{64}T^{ef}\gamma^{cd}\big(\overline{\widehat R(Q)}_{ae}\gamma_{b}\gamma_f\gamma_{cd}\widehat R(Q)^{ab}\big)\epsilon^i\\
&-\frac{3i}{64}T^{ef}\gamma^{cd}\big(\overline{\widehat R(Q)}_{ae}\gamma_{b}\gamma_f\gamma_{cd}\gamma_p\widehat R(Q)^{ab}\big)\gamma^p\epsilon^i\\
&+\frac{3i}{128}T^{ef}\gamma^{cd}\big(\overline{\widehat R(Q)}_{ae}\gamma_{b}\gamma_f\gamma_{cd}\gamma_{pq}\widehat R(Q)^{ab}\big)\gamma^{pq}\epsilon^i
\end{aligned}\tag{H073}
```

```math
\begin{aligned}
\left.\frac{3i}{16}\gamma^{cd}\widehat R(Q)^{ab}{}^i\big(\bar\epsilon \gamma_{cd}(\gamma\!\cdot\!T)\widehat R(Q)_{ab}\big)\right|_{\epsilon^i}={}&\frac{3i}{128}\gamma^{cd}\big(\overline{\widehat R(Q)}_{ab}(\gamma\!\cdot\!T)\gamma_{cd}\widehat R(Q)^{ab}\big)\epsilon^i\\
&+\frac{3i}{128}\gamma^{cd}\big(\overline{\widehat R(Q)}_{ab}(\gamma\!\cdot\!T)\gamma_{cd}\gamma_p\widehat R(Q)^{ab}\big)\gamma^p\epsilon^i\\
&-\frac{3i}{256}\gamma^{cd}\big(\overline{\widehat R(Q)}_{ab}(\gamma\!\cdot\!T)\gamma_{cd}\gamma_{pq}\widehat R(Q)^{ab}\big)\gamma^{pq}\epsilon^i
\end{aligned}\tag{H074}
```

```math
\begin{aligned}
\left.\frac{i}{2}T^e{}_{[a}\gamma^{cd}\widehat R(Q)^{ab}{}^i\big(\bar\epsilon \gamma_{cd}\widehat R(Q)_{b]e}\big)\right|_{\epsilon^i}={}&-\frac{i}{32}T^e{}_{a}\gamma^{cd}\big(\overline{\widehat R(Q)}_{be}\gamma_{cd}\widehat R(Q)^{ab}\big)\epsilon^i\\
&-\frac{i}{32}T^e{}_{a}\gamma^{cd}\big(\overline{\widehat R(Q)}_{be}\gamma_{cd}\gamma_p\widehat R(Q)^{ab}\big)\gamma^p\epsilon^i\\
&+\frac{i}{64}T^e{}_{a}\gamma^{cd}\big(\overline{\widehat R(Q)}_{be}\gamma_{cd}\gamma_{pq}\widehat R(Q)^{ab}\big)\gamma^{pq}\epsilon^i\\
&+\frac{i}{32}T^e{}_{b}\gamma^{cd}\big(\overline{\widehat R(Q)}_{ae}\gamma_{cd}\widehat R(Q)^{ab}\big)\epsilon^i\\
&+\frac{i}{32}T^e{}_{b}\gamma^{cd}\big(\overline{\widehat R(Q)}_{ae}\gamma_{cd}\gamma_p\widehat R(Q)^{ab}\big)\gamma^p\epsilon^i\\
&-\frac{i}{64}T^e{}_{b}\gamma^{cd}\big(\overline{\widehat R(Q)}_{ae}\gamma_{cd}\gamma_{pq}\widehat R(Q)^{ab}\big)\gamma^{pq}\epsilon^i
\end{aligned}\tag{H075}
```

```math
\begin{aligned}
\left.\frac{i}{8}\gamma^{cd}\widehat R(Q)^{ab}{}^i\big(\bar\epsilon \gamma_{[c}(\gamma\!\cdot\!T)\gamma_{d]}\widehat R(Q)_{ab}\big)\right|_{\epsilon^i}={}&\frac{i}{128}\gamma^{cd}\big(\overline{\widehat R(Q)}_{ab}\gamma_{c}(\gamma\!\cdot\!T)\gamma_{d}\widehat R(Q)^{ab}\big)\epsilon^i\\
&+\frac{i}{128}\gamma^{cd}\big(\overline{\widehat R(Q)}_{ab}\gamma_{c}(\gamma\!\cdot\!T)\gamma_{d}\gamma_p\widehat R(Q)^{ab}\big)\gamma^p\epsilon^i\\
&-\frac{i}{256}\gamma^{cd}\big(\overline{\widehat R(Q)}_{ab}\gamma_{c}(\gamma\!\cdot\!T)\gamma_{d}\gamma_{pq}\widehat R(Q)^{ab}\big)\gamma^{pq}\epsilon^i\\
&-\frac{i}{128}\gamma^{cd}\big(\overline{\widehat R(Q)}_{ab}\gamma_{d}(\gamma\!\cdot\!T)\gamma_{c}\widehat R(Q)^{ab}\big)\epsilon^i\\
&-\frac{i}{128}\gamma^{cd}\big(\overline{\widehat R(Q)}_{ab}\gamma_{d}(\gamma\!\cdot\!T)\gamma_{c}\gamma_p\widehat R(Q)^{ab}\big)\gamma^p\epsilon^i\\
&+\frac{i}{256}\gamma^{cd}\big(\overline{\widehat R(Q)}_{ab}\gamma_{d}(\gamma\!\cdot\!T)\gamma_{c}\gamma_{pq}\widehat R(Q)^{ab}\big)\gamma^{pq}\epsilon^i
\end{aligned}\tag{H076}
```

```math
\begin{aligned}
\left.\frac{1}{8}\gamma^{cd}\widehat R(Q)^{ab}{}^i\big(\bar\epsilon \gamma_{[c}\mathcal D_{[a}\widehat R(Q)_{b]d]}\big)\right|_{\epsilon^i}={}&\frac{1}{256}\gamma^{cd}\big(\overline{\mathcal D_{a}\widehat R(Q)_{bd}}\gamma_{c}\widehat R(Q)^{ab}\big)\epsilon^i\\
&+\frac{1}{256}\gamma^{cd}\big(\overline{\mathcal D_{a}\widehat R(Q)_{bd}}\gamma_{c}\gamma_p\widehat R(Q)^{ab}\big)\gamma^p\epsilon^i\\
&-\frac{1}{512}\gamma^{cd}\big(\overline{\mathcal D_{a}\widehat R(Q)_{bd}}\gamma_{c}\gamma_{pq}\widehat R(Q)^{ab}\big)\gamma^{pq}\epsilon^i\\
&-\frac{1}{256}\gamma^{cd}\big(\overline{\mathcal D_{a}\widehat R(Q)_{bc}}\gamma_{d}\widehat R(Q)^{ab}\big)\epsilon^i\\
&-\frac{1}{256}\gamma^{cd}\big(\overline{\mathcal D_{a}\widehat R(Q)_{bc}}\gamma_{d}\gamma_p\widehat R(Q)^{ab}\big)\gamma^p\epsilon^i\\
&+\frac{1}{512}\gamma^{cd}\big(\overline{\mathcal D_{a}\widehat R(Q)_{bc}}\gamma_{d}\gamma_{pq}\widehat R(Q)^{ab}\big)\gamma^{pq}\epsilon^i\\
&-\frac{1}{256}\gamma^{cd}\big(\overline{\mathcal D_{b}\widehat R(Q)_{ad}}\gamma_{c}\widehat R(Q)^{ab}\big)\epsilon^i\\
&-\frac{1}{256}\gamma^{cd}\big(\overline{\mathcal D_{b}\widehat R(Q)_{ad}}\gamma_{c}\gamma_p\widehat R(Q)^{ab}\big)\gamma^p\epsilon^i\\
&+\frac{1}{512}\gamma^{cd}\big(\overline{\mathcal D_{b}\widehat R(Q)_{ad}}\gamma_{c}\gamma_{pq}\widehat R(Q)^{ab}\big)\gamma^{pq}\epsilon^i\\
&+\frac{1}{256}\gamma^{cd}\big(\overline{\mathcal D_{b}\widehat R(Q)_{ac}}\gamma_{d}\widehat R(Q)^{ab}\big)\epsilon^i\\
&+\frac{1}{256}\gamma^{cd}\big(\overline{\mathcal D_{b}\widehat R(Q)_{ac}}\gamma_{d}\gamma_p\widehat R(Q)^{ab}\big)\gamma^p\epsilon^i\\
&-\frac{1}{512}\gamma^{cd}\big(\overline{\mathcal D_{b}\widehat R(Q)_{ac}}\gamma_{d}\gamma_{pq}\widehat R(Q)^{ab}\big)\gamma^{pq}\epsilon^i
\end{aligned}\tag{H077}
```

```math
\begin{aligned}
\left.\frac{i}{8}\gamma^{cd}\widehat R(Q)^{ab}{}^i\big(\bar\epsilon \gamma_{[a}(\gamma\!\cdot\!T)\gamma_{[c}\widehat R(Q)_{b]d]}\big)\right|_{\epsilon^i}={}&-\frac{i}{256}\gamma^{cd}\big(\overline{\widehat R(Q)}_{bd}\gamma_{c}(\gamma\!\cdot\!T)\gamma_{a}\widehat R(Q)^{ab}\big)\epsilon^i\\
&-\frac{i}{256}\gamma^{cd}\big(\overline{\widehat R(Q)}_{bd}\gamma_{c}(\gamma\!\cdot\!T)\gamma_{a}\gamma_p\widehat R(Q)^{ab}\big)\gamma^p\epsilon^i\\
&+\frac{i}{512}\gamma^{cd}\big(\overline{\widehat R(Q)}_{bd}\gamma_{c}(\gamma\!\cdot\!T)\gamma_{a}\gamma_{pq}\widehat R(Q)^{ab}\big)\gamma^{pq}\epsilon^i\\
&+\frac{i}{256}\gamma^{cd}\big(\overline{\widehat R(Q)}_{bc}\gamma_{d}(\gamma\!\cdot\!T)\gamma_{a}\widehat R(Q)^{ab}\big)\epsilon^i\\
&+\frac{i}{256}\gamma^{cd}\big(\overline{\widehat R(Q)}_{bc}\gamma_{d}(\gamma\!\cdot\!T)\gamma_{a}\gamma_p\widehat R(Q)^{ab}\big)\gamma^p\epsilon^i\\
&-\frac{i}{512}\gamma^{cd}\big(\overline{\widehat R(Q)}_{bc}\gamma_{d}(\gamma\!\cdot\!T)\gamma_{a}\gamma_{pq}\widehat R(Q)^{ab}\big)\gamma^{pq}\epsilon^i\\
&+\frac{i}{256}\gamma^{cd}\big(\overline{\widehat R(Q)}_{ad}\gamma_{c}(\gamma\!\cdot\!T)\gamma_{b}\widehat R(Q)^{ab}\big)\epsilon^i\\
&+\frac{i}{256}\gamma^{cd}\big(\overline{\widehat R(Q)}_{ad}\gamma_{c}(\gamma\!\cdot\!T)\gamma_{b}\gamma_p\widehat R(Q)^{ab}\big)\gamma^p\epsilon^i\\
&-\frac{i}{512}\gamma^{cd}\big(\overline{\widehat R(Q)}_{ad}\gamma_{c}(\gamma\!\cdot\!T)\gamma_{b}\gamma_{pq}\widehat R(Q)^{ab}\big)\gamma^{pq}\epsilon^i\\
&-\frac{i}{256}\gamma^{cd}\big(\overline{\widehat R(Q)}_{ac}\gamma_{d}(\gamma\!\cdot\!T)\gamma_{b}\widehat R(Q)^{ab}\big)\epsilon^i\\
&-\frac{i}{256}\gamma^{cd}\big(\overline{\widehat R(Q)}_{ac}\gamma_{d}(\gamma\!\cdot\!T)\gamma_{b}\gamma_p\widehat R(Q)^{ab}\big)\gamma^p\epsilon^i\\
&+\frac{i}{512}\gamma^{cd}\big(\overline{\widehat R(Q)}_{ac}\gamma_{d}(\gamma\!\cdot\!T)\gamma_{b}\gamma_{pq}\widehat R(Q)^{ab}\big)\gamma^{pq}\epsilon^i
\end{aligned}\tag{H078}
```

```math
\begin{aligned}
\left.-\frac{1}{16}\gamma^{cd}\widehat R(Q)^{ab}{}^i\big(\bar\epsilon \gamma_{[a}\mathcal D_{b]}\widehat R(Q)_{cd}\big)\right|_{\epsilon^i}={}&-\frac{1}{256}\gamma^{cd}\big(\overline{\mathcal D_{b}\widehat R(Q)_{cd}}\gamma_{a}\widehat R(Q)^{ab}\big)\epsilon^i\\
&-\frac{1}{256}\gamma^{cd}\big(\overline{\mathcal D_{b}\widehat R(Q)_{cd}}\gamma_{a}\gamma_p\widehat R(Q)^{ab}\big)\gamma^p\epsilon^i\\
&+\frac{1}{512}\gamma^{cd}\big(\overline{\mathcal D_{b}\widehat R(Q)_{cd}}\gamma_{a}\gamma_{pq}\widehat R(Q)^{ab}\big)\gamma^{pq}\epsilon^i\\
&+\frac{1}{256}\gamma^{cd}\big(\overline{\mathcal D_{a}\widehat R(Q)_{cd}}\gamma_{b}\widehat R(Q)^{ab}\big)\epsilon^i\\
&+\frac{1}{256}\gamma^{cd}\big(\overline{\mathcal D_{a}\widehat R(Q)_{cd}}\gamma_{b}\gamma_p\widehat R(Q)^{ab}\big)\gamma^p\epsilon^i\\
&-\frac{1}{512}\gamma^{cd}\big(\overline{\mathcal D_{a}\widehat R(Q)_{cd}}\gamma_{b}\gamma_{pq}\widehat R(Q)^{ab}\big)\gamma^{pq}\epsilon^i
\end{aligned}\tag{H079}
```

```math
\begin{aligned}
\left.\frac{i}{16}\gamma^{cd}\widehat R(Q)^{ab}{}^i\big(\bar\epsilon \gamma_{[a}(\gamma\!\cdot\!T)\gamma_{b]}\widehat R(Q)_{cd}\big)\right|_{\epsilon^i}={}&\frac{i}{256}\gamma^{cd}\big(\overline{\widehat R(Q)}_{cd}\gamma_{a}(\gamma\!\cdot\!T)\gamma_{b}\widehat R(Q)^{ab}\big)\epsilon^i\\
&+\frac{i}{256}\gamma^{cd}\big(\overline{\widehat R(Q)}_{cd}\gamma_{a}(\gamma\!\cdot\!T)\gamma_{b}\gamma_p\widehat R(Q)^{ab}\big)\gamma^p\epsilon^i\\
&-\frac{i}{512}\gamma^{cd}\big(\overline{\widehat R(Q)}_{cd}\gamma_{a}(\gamma\!\cdot\!T)\gamma_{b}\gamma_{pq}\widehat R(Q)^{ab}\big)\gamma^{pq}\epsilon^i\\
&-\frac{i}{256}\gamma^{cd}\big(\overline{\widehat R(Q)}_{cd}\gamma_{b}(\gamma\!\cdot\!T)\gamma_{a}\widehat R(Q)^{ab}\big)\epsilon^i\\
&-\frac{i}{256}\gamma^{cd}\big(\overline{\widehat R(Q)}_{cd}\gamma_{b}(\gamma\!\cdot\!T)\gamma_{a}\gamma_p\widehat R(Q)^{ab}\big)\gamma^p\epsilon^i\\
&+\frac{i}{512}\gamma^{cd}\big(\overline{\widehat R(Q)}_{cd}\gamma_{b}(\gamma\!\cdot\!T)\gamma_{a}\gamma_{pq}\widehat R(Q)^{ab}\big)\gamma^{pq}\epsilon^i
\end{aligned}\tag{H080}
```

```math
\begin{aligned}
\left.\eta_{[b[c}\gamma^{cd}\widehat R(Q)^{ab}{}^i\big(\bar\epsilon \gamma_{d]}\mathcal D_{a]}\chi\big)\right|_{\epsilon^i}={}&\frac{1}{32}\eta_{bc}\gamma^{cd}\big(\overline{\mathcal D_{a}\chi}\gamma_{d}\widehat R(Q)^{ab}\big)\epsilon^i\\
&+\frac{1}{32}\eta_{bc}\gamma^{cd}\big(\overline{\mathcal D_{a}\chi}\gamma_{d}\gamma_p\widehat R(Q)^{ab}\big)\gamma^p\epsilon^i\\
&-\frac{1}{64}\eta_{bc}\gamma^{cd}\big(\overline{\mathcal D_{a}\chi}\gamma_{d}\gamma_{pq}\widehat R(Q)^{ab}\big)\gamma^{pq}\epsilon^i\\
&-\frac{1}{32}\eta_{bd}\gamma^{cd}\big(\overline{\mathcal D_{a}\chi}\gamma_{c}\widehat R(Q)^{ab}\big)\epsilon^i\\
&-\frac{1}{32}\eta_{bd}\gamma^{cd}\big(\overline{\mathcal D_{a}\chi}\gamma_{c}\gamma_p\widehat R(Q)^{ab}\big)\gamma^p\epsilon^i\\
&+\frac{1}{64}\eta_{bd}\gamma^{cd}\big(\overline{\mathcal D_{a}\chi}\gamma_{c}\gamma_{pq}\widehat R(Q)^{ab}\big)\gamma^{pq}\epsilon^i\\
&-\frac{1}{32}\eta_{ac}\gamma^{cd}\big(\overline{\mathcal D_{b}\chi}\gamma_{d}\widehat R(Q)^{ab}\big)\epsilon^i\\
&-\frac{1}{32}\eta_{ac}\gamma^{cd}\big(\overline{\mathcal D_{b}\chi}\gamma_{d}\gamma_p\widehat R(Q)^{ab}\big)\gamma^p\epsilon^i\\
&+\frac{1}{64}\eta_{ac}\gamma^{cd}\big(\overline{\mathcal D_{b}\chi}\gamma_{d}\gamma_{pq}\widehat R(Q)^{ab}\big)\gamma^{pq}\epsilon^i\\
&+\frac{1}{32}\eta_{ad}\gamma^{cd}\big(\overline{\mathcal D_{b}\chi}\gamma_{c}\widehat R(Q)^{ab}\big)\epsilon^i\\
&+\frac{1}{32}\eta_{ad}\gamma^{cd}\big(\overline{\mathcal D_{b}\chi}\gamma_{c}\gamma_p\widehat R(Q)^{ab}\big)\gamma^p\epsilon^i\\
&-\frac{1}{64}\eta_{ad}\gamma^{cd}\big(\overline{\mathcal D_{b}\chi}\gamma_{c}\gamma_{pq}\widehat R(Q)^{ab}\big)\gamma^{pq}\epsilon^i
\end{aligned}\tag{H081}
```

```math
\begin{aligned}
\left.i\eta_{[b[c}\gamma^{cd}\widehat R(Q)^{ab}{}^i\big(\bar\epsilon \gamma_{a]}(\gamma\!\cdot\!T)\gamma_{d]}\chi\big)\right|_{\epsilon^i}={}&-\frac{i}{32}\eta_{bc}\gamma^{cd}\big(\bar\chi\gamma_{d}(\gamma\!\cdot\!T)\gamma_{a}\widehat R(Q)^{ab}\big)\epsilon^i\\
&-\frac{i}{32}\eta_{bc}\gamma^{cd}\big(\bar\chi\gamma_{d}(\gamma\!\cdot\!T)\gamma_{a}\gamma_p\widehat R(Q)^{ab}\big)\gamma^p\epsilon^i\\
&+\frac{i}{64}\eta_{bc}\gamma^{cd}\big(\bar\chi\gamma_{d}(\gamma\!\cdot\!T)\gamma_{a}\gamma_{pq}\widehat R(Q)^{ab}\big)\gamma^{pq}\epsilon^i\\
&+\frac{i}{32}\eta_{bd}\gamma^{cd}\big(\bar\chi\gamma_{c}(\gamma\!\cdot\!T)\gamma_{a}\widehat R(Q)^{ab}\big)\epsilon^i\\
&+\frac{i}{32}\eta_{bd}\gamma^{cd}\big(\bar\chi\gamma_{c}(\gamma\!\cdot\!T)\gamma_{a}\gamma_p\widehat R(Q)^{ab}\big)\gamma^p\epsilon^i\\
&-\frac{i}{64}\eta_{bd}\gamma^{cd}\big(\bar\chi\gamma_{c}(\gamma\!\cdot\!T)\gamma_{a}\gamma_{pq}\widehat R(Q)^{ab}\big)\gamma^{pq}\epsilon^i\\
&+\frac{i}{32}\eta_{ac}\gamma^{cd}\big(\bar\chi\gamma_{d}(\gamma\!\cdot\!T)\gamma_{b}\widehat R(Q)^{ab}\big)\epsilon^i\\
&+\frac{i}{32}\eta_{ac}\gamma^{cd}\big(\bar\chi\gamma_{d}(\gamma\!\cdot\!T)\gamma_{b}\gamma_p\widehat R(Q)^{ab}\big)\gamma^p\epsilon^i\\
&-\frac{i}{64}\eta_{ac}\gamma^{cd}\big(\bar\chi\gamma_{d}(\gamma\!\cdot\!T)\gamma_{b}\gamma_{pq}\widehat R(Q)^{ab}\big)\gamma^{pq}\epsilon^i\\
&-\frac{i}{32}\eta_{ad}\gamma^{cd}\big(\bar\chi\gamma_{c}(\gamma\!\cdot\!T)\gamma_{b}\widehat R(Q)^{ab}\big)\epsilon^i\\
&-\frac{i}{32}\eta_{ad}\gamma^{cd}\big(\bar\chi\gamma_{c}(\gamma\!\cdot\!T)\gamma_{b}\gamma_p\widehat R(Q)^{ab}\big)\gamma^p\epsilon^i\\
&+\frac{i}{64}\eta_{ad}\gamma^{cd}\big(\bar\chi\gamma_{c}(\gamma\!\cdot\!T)\gamma_{b}\gamma_{pq}\widehat R(Q)^{ab}\big)\gamma^{pq}\epsilon^i
\end{aligned}\tag{H082}
```

**Ricci contraction.** Apply H05 to each of the thirteen terms in H64.

```math
\begin{aligned}
\left.-\frac{1}{12}\eta^{cd}\widehat R(Q)^{ab}{}^i\big(\bar\epsilon \gamma_{bd}\gamma^e\mathcal D_e\widehat R(Q)_{ac}\big)\right|_{\epsilon^i}={}&\frac{1}{96}\eta^{cd}\big(\overline{\mathcal D_e\widehat R(Q)_{ac}}\gamma^e\gamma_{bd}\widehat R(Q)^{ab}\big)\epsilon^i\\
&+\frac{1}{96}\eta^{cd}\big(\overline{\mathcal D_e\widehat R(Q)_{ac}}\gamma^e\gamma_{bd}\gamma_p\widehat R(Q)^{ab}\big)\gamma^p\epsilon^i\\
&-\frac{1}{192}\eta^{cd}\big(\overline{\mathcal D_e\widehat R(Q)_{ac}}\gamma^e\gamma_{bd}\gamma_{pq}\widehat R(Q)^{ab}\big)\gamma^{pq}\epsilon^i
\end{aligned}\tag{H083}
```

```math
\begin{aligned}
\left.-\frac{1}{12}\eta^{cd}\widehat R(Q)^{ab}{}^i\big(\bar\epsilon \gamma_{bd}\gamma_{[a}\mathcal D^e\widehat R(Q)_{c]e}\big)\right|_{\epsilon^i}={}&\frac{1}{192}\eta^{cd}\big(\overline{\mathcal D^e\widehat R(Q)_{ce}}\gamma_{a}\gamma_{bd}\widehat R(Q)^{ab}\big)\epsilon^i\\
&+\frac{1}{192}\eta^{cd}\big(\overline{\mathcal D^e\widehat R(Q)_{ce}}\gamma_{a}\gamma_{bd}\gamma_p\widehat R(Q)^{ab}\big)\gamma^p\epsilon^i\\
&-\frac{1}{384}\eta^{cd}\big(\overline{\mathcal D^e\widehat R(Q)_{ce}}\gamma_{a}\gamma_{bd}\gamma_{pq}\widehat R(Q)^{ab}\big)\gamma^{pq}\epsilon^i\\
&-\frac{1}{192}\eta^{cd}\big(\overline{\mathcal D^e\widehat R(Q)_{ae}}\gamma_{c}\gamma_{bd}\widehat R(Q)^{ab}\big)\epsilon^i\\
&-\frac{1}{192}\eta^{cd}\big(\overline{\mathcal D^e\widehat R(Q)_{ae}}\gamma_{c}\gamma_{bd}\gamma_p\widehat R(Q)^{ab}\big)\gamma^p\epsilon^i\\
&+\frac{1}{384}\eta^{cd}\big(\overline{\mathcal D^e\widehat R(Q)_{ae}}\gamma_{c}\gamma_{bd}\gamma_{pq}\widehat R(Q)^{ab}\big)\gamma^{pq}\epsilon^i
\end{aligned}\tag{H084}
```

```math
\begin{aligned}
\left.\frac{2i}{9}T^{ef}\eta^{cd}\widehat R(Q)^{ab}{}^i\big(\bar\epsilon \gamma_{bd}\gamma_{ac}\widehat R(Q)_{ef}\big)\right|_{\epsilon^i}={}&\frac{i}{36}T^{ef}\eta^{cd}\big(\overline{\widehat R(Q)}_{ef}\gamma_{ac}\gamma_{bd}\widehat R(Q)^{ab}\big)\epsilon^i\\
&+\frac{i}{36}T^{ef}\eta^{cd}\big(\overline{\widehat R(Q)}_{ef}\gamma_{ac}\gamma_{bd}\gamma_p\widehat R(Q)^{ab}\big)\gamma^p\epsilon^i\\
&-\frac{i}{72}T^{ef}\eta^{cd}\big(\overline{\widehat R(Q)}_{ef}\gamma_{ac}\gamma_{bd}\gamma_{pq}\widehat R(Q)^{ab}\big)\gamma^{pq}\epsilon^i
\end{aligned}\tag{H085}
```

```math
\begin{aligned}
\left.-iT^{ef}\eta^{cd}\widehat R(Q)^{ab}{}^i\big(\bar\epsilon \gamma_{bd}\gamma_f\gamma_{[a}\widehat R(Q)_{c]e}\big)\right|_{\epsilon^i}={}&\frac{i}{16}T^{ef}\eta^{cd}\big(\overline{\widehat R(Q)}_{ce}\gamma_{a}\gamma_f\gamma_{bd}\widehat R(Q)^{ab}\big)\epsilon^i\\
&+\frac{i}{16}T^{ef}\eta^{cd}\big(\overline{\widehat R(Q)}_{ce}\gamma_{a}\gamma_f\gamma_{bd}\gamma_p\widehat R(Q)^{ab}\big)\gamma^p\epsilon^i\\
&-\frac{i}{32}T^{ef}\eta^{cd}\big(\overline{\widehat R(Q)}_{ce}\gamma_{a}\gamma_f\gamma_{bd}\gamma_{pq}\widehat R(Q)^{ab}\big)\gamma^{pq}\epsilon^i\\
&-\frac{i}{16}T^{ef}\eta^{cd}\big(\overline{\widehat R(Q)}_{ae}\gamma_{c}\gamma_f\gamma_{bd}\widehat R(Q)^{ab}\big)\epsilon^i\\
&-\frac{i}{16}T^{ef}\eta^{cd}\big(\overline{\widehat R(Q)}_{ae}\gamma_{c}\gamma_f\gamma_{bd}\gamma_p\widehat R(Q)^{ab}\big)\gamma^p\epsilon^i\\
&+\frac{i}{32}T^{ef}\eta^{cd}\big(\overline{\widehat R(Q)}_{ae}\gamma_{c}\gamma_f\gamma_{bd}\gamma_{pq}\widehat R(Q)^{ab}\big)\gamma^{pq}\epsilon^i
\end{aligned}\tag{H086}
```

```math
\begin{aligned}
\left.\frac{i}{4}\eta^{cd}\widehat R(Q)^{ab}{}^i\big(\bar\epsilon \gamma_{bd}(\gamma\!\cdot\!T)\widehat R(Q)_{ac}\big)\right|_{\epsilon^i}={}&\frac{i}{32}\eta^{cd}\big(\overline{\widehat R(Q)}_{ac}(\gamma\!\cdot\!T)\gamma_{bd}\widehat R(Q)^{ab}\big)\epsilon^i\\
&+\frac{i}{32}\eta^{cd}\big(\overline{\widehat R(Q)}_{ac}(\gamma\!\cdot\!T)\gamma_{bd}\gamma_p\widehat R(Q)^{ab}\big)\gamma^p\epsilon^i\\
&-\frac{i}{64}\eta^{cd}\big(\overline{\widehat R(Q)}_{ac}(\gamma\!\cdot\!T)\gamma_{bd}\gamma_{pq}\widehat R(Q)^{ab}\big)\gamma^{pq}\epsilon^i
\end{aligned}\tag{H087}
```

```math
\begin{aligned}
\left.\frac{2i}{3}T^e{}_{[a}\eta^{cd}\widehat R(Q)^{ab}{}^i\big(\bar\epsilon \gamma_{bd}\widehat R(Q)_{c]e}\big)\right|_{\epsilon^i}={}&-\frac{i}{24}T^e{}_{a}\eta^{cd}\big(\overline{\widehat R(Q)}_{ce}\gamma_{bd}\widehat R(Q)^{ab}\big)\epsilon^i\\
&-\frac{i}{24}T^e{}_{a}\eta^{cd}\big(\overline{\widehat R(Q)}_{ce}\gamma_{bd}\gamma_p\widehat R(Q)^{ab}\big)\gamma^p\epsilon^i\\
&+\frac{i}{48}T^e{}_{a}\eta^{cd}\big(\overline{\widehat R(Q)}_{ce}\gamma_{bd}\gamma_{pq}\widehat R(Q)^{ab}\big)\gamma^{pq}\epsilon^i\\
&+\frac{i}{24}T^e{}_{c}\eta^{cd}\big(\overline{\widehat R(Q)}_{ae}\gamma_{bd}\widehat R(Q)^{ab}\big)\epsilon^i\\
&+\frac{i}{24}T^e{}_{c}\eta^{cd}\big(\overline{\widehat R(Q)}_{ae}\gamma_{bd}\gamma_p\widehat R(Q)^{ab}\big)\gamma^p\epsilon^i\\
&-\frac{i}{48}T^e{}_{c}\eta^{cd}\big(\overline{\widehat R(Q)}_{ae}\gamma_{bd}\gamma_{pq}\widehat R(Q)^{ab}\big)\gamma^{pq}\epsilon^i
\end{aligned}\tag{H088}
```

```math
\begin{aligned}
\left.\frac{i}{6}\eta^{cd}\widehat R(Q)^{ab}{}^i\big(\bar\epsilon \gamma_{[b}(\gamma\!\cdot\!T)\gamma_{d]}\widehat R(Q)_{ac}\big)\right|_{\epsilon^i}={}&\frac{i}{96}\eta^{cd}\big(\overline{\widehat R(Q)}_{ac}\gamma_{b}(\gamma\!\cdot\!T)\gamma_{d}\widehat R(Q)^{ab}\big)\epsilon^i\\
&+\frac{i}{96}\eta^{cd}\big(\overline{\widehat R(Q)}_{ac}\gamma_{b}(\gamma\!\cdot\!T)\gamma_{d}\gamma_p\widehat R(Q)^{ab}\big)\gamma^p\epsilon^i\\
&-\frac{i}{192}\eta^{cd}\big(\overline{\widehat R(Q)}_{ac}\gamma_{b}(\gamma\!\cdot\!T)\gamma_{d}\gamma_{pq}\widehat R(Q)^{ab}\big)\gamma^{pq}\epsilon^i\\
&-\frac{i}{96}\eta^{cd}\big(\overline{\widehat R(Q)}_{ac}\gamma_{d}(\gamma\!\cdot\!T)\gamma_{b}\widehat R(Q)^{ab}\big)\epsilon^i\\
&-\frac{i}{96}\eta^{cd}\big(\overline{\widehat R(Q)}_{ac}\gamma_{d}(\gamma\!\cdot\!T)\gamma_{b}\gamma_p\widehat R(Q)^{ab}\big)\gamma^p\epsilon^i\\
&+\frac{i}{192}\eta^{cd}\big(\overline{\widehat R(Q)}_{ac}\gamma_{d}(\gamma\!\cdot\!T)\gamma_{b}\gamma_{pq}\widehat R(Q)^{ab}\big)\gamma^{pq}\epsilon^i
\end{aligned}\tag{H089}
```

```math
\begin{aligned}
\left.\frac{1}{6}\eta^{cd}\widehat R(Q)^{ab}{}^i\big(\bar\epsilon \gamma_{[b}\mathcal D_{[a}\widehat R(Q)_{c]d]}\big)\right|_{\epsilon^i}={}&\frac{1}{192}\eta^{cd}\big(\overline{\mathcal D_{a}\widehat R(Q)_{cd}}\gamma_{b}\widehat R(Q)^{ab}\big)\epsilon^i\\
&+\frac{1}{192}\eta^{cd}\big(\overline{\mathcal D_{a}\widehat R(Q)_{cd}}\gamma_{b}\gamma_p\widehat R(Q)^{ab}\big)\gamma^p\epsilon^i\\
&-\frac{1}{384}\eta^{cd}\big(\overline{\mathcal D_{a}\widehat R(Q)_{cd}}\gamma_{b}\gamma_{pq}\widehat R(Q)^{ab}\big)\gamma^{pq}\epsilon^i\\
&-\frac{1}{192}\eta^{cd}\big(\overline{\mathcal D_{a}\widehat R(Q)_{cb}}\gamma_{d}\widehat R(Q)^{ab}\big)\epsilon^i\\
&-\frac{1}{192}\eta^{cd}\big(\overline{\mathcal D_{a}\widehat R(Q)_{cb}}\gamma_{d}\gamma_p\widehat R(Q)^{ab}\big)\gamma^p\epsilon^i\\
&+\frac{1}{384}\eta^{cd}\big(\overline{\mathcal D_{a}\widehat R(Q)_{cb}}\gamma_{d}\gamma_{pq}\widehat R(Q)^{ab}\big)\gamma^{pq}\epsilon^i\\
&-\frac{1}{192}\eta^{cd}\big(\overline{\mathcal D_{c}\widehat R(Q)_{ad}}\gamma_{b}\widehat R(Q)^{ab}\big)\epsilon^i\\
&-\frac{1}{192}\eta^{cd}\big(\overline{\mathcal D_{c}\widehat R(Q)_{ad}}\gamma_{b}\gamma_p\widehat R(Q)^{ab}\big)\gamma^p\epsilon^i\\
&+\frac{1}{384}\eta^{cd}\big(\overline{\mathcal D_{c}\widehat R(Q)_{ad}}\gamma_{b}\gamma_{pq}\widehat R(Q)^{ab}\big)\gamma^{pq}\epsilon^i\\
&+\frac{1}{192}\eta^{cd}\big(\overline{\mathcal D_{c}\widehat R(Q)_{ab}}\gamma_{d}\widehat R(Q)^{ab}\big)\epsilon^i\\
&+\frac{1}{192}\eta^{cd}\big(\overline{\mathcal D_{c}\widehat R(Q)_{ab}}\gamma_{d}\gamma_p\widehat R(Q)^{ab}\big)\gamma^p\epsilon^i\\
&-\frac{1}{384}\eta^{cd}\big(\overline{\mathcal D_{c}\widehat R(Q)_{ab}}\gamma_{d}\gamma_{pq}\widehat R(Q)^{ab}\big)\gamma^{pq}\epsilon^i
\end{aligned}\tag{H090}
```

```math
\begin{aligned}
\left.\frac{i}{6}\eta^{cd}\widehat R(Q)^{ab}{}^i\big(\bar\epsilon \gamma_{[a}(\gamma\!\cdot\!T)\gamma_{[b}\widehat R(Q)_{c]d]}\big)\right|_{\epsilon^i}={}&-\frac{i}{192}\eta^{cd}\big(\overline{\widehat R(Q)}_{cd}\gamma_{b}(\gamma\!\cdot\!T)\gamma_{a}\widehat R(Q)^{ab}\big)\epsilon^i\\
&-\frac{i}{192}\eta^{cd}\big(\overline{\widehat R(Q)}_{cd}\gamma_{b}(\gamma\!\cdot\!T)\gamma_{a}\gamma_p\widehat R(Q)^{ab}\big)\gamma^p\epsilon^i\\
&+\frac{i}{384}\eta^{cd}\big(\overline{\widehat R(Q)}_{cd}\gamma_{b}(\gamma\!\cdot\!T)\gamma_{a}\gamma_{pq}\widehat R(Q)^{ab}\big)\gamma^{pq}\epsilon^i\\
&+\frac{i}{192}\eta^{cd}\big(\overline{\widehat R(Q)}_{cb}\gamma_{d}(\gamma\!\cdot\!T)\gamma_{a}\widehat R(Q)^{ab}\big)\epsilon^i\\
&+\frac{i}{192}\eta^{cd}\big(\overline{\widehat R(Q)}_{cb}\gamma_{d}(\gamma\!\cdot\!T)\gamma_{a}\gamma_p\widehat R(Q)^{ab}\big)\gamma^p\epsilon^i\\
&-\frac{i}{384}\eta^{cd}\big(\overline{\widehat R(Q)}_{cb}\gamma_{d}(\gamma\!\cdot\!T)\gamma_{a}\gamma_{pq}\widehat R(Q)^{ab}\big)\gamma^{pq}\epsilon^i\\
&+\frac{i}{192}\eta^{cd}\big(\overline{\widehat R(Q)}_{ad}\gamma_{b}(\gamma\!\cdot\!T)\gamma_{c}\widehat R(Q)^{ab}\big)\epsilon^i\\
&+\frac{i}{192}\eta^{cd}\big(\overline{\widehat R(Q)}_{ad}\gamma_{b}(\gamma\!\cdot\!T)\gamma_{c}\gamma_p\widehat R(Q)^{ab}\big)\gamma^p\epsilon^i\\
&-\frac{i}{384}\eta^{cd}\big(\overline{\widehat R(Q)}_{ad}\gamma_{b}(\gamma\!\cdot\!T)\gamma_{c}\gamma_{pq}\widehat R(Q)^{ab}\big)\gamma^{pq}\epsilon^i\\
&-\frac{i}{192}\eta^{cd}\big(\overline{\widehat R(Q)}_{ab}\gamma_{d}(\gamma\!\cdot\!T)\gamma_{c}\widehat R(Q)^{ab}\big)\epsilon^i\\
&-\frac{i}{192}\eta^{cd}\big(\overline{\widehat R(Q)}_{ab}\gamma_{d}(\gamma\!\cdot\!T)\gamma_{c}\gamma_p\widehat R(Q)^{ab}\big)\gamma^p\epsilon^i\\
&+\frac{i}{384}\eta^{cd}\big(\overline{\widehat R(Q)}_{ab}\gamma_{d}(\gamma\!\cdot\!T)\gamma_{c}\gamma_{pq}\widehat R(Q)^{ab}\big)\gamma^{pq}\epsilon^i
\end{aligned}\tag{H091}
```

```math
\begin{aligned}
\left.-\frac{1}{12}\eta^{cd}\widehat R(Q)^{ab}{}^i\big(\bar\epsilon \gamma_{[a}\mathcal D_{c]}\widehat R(Q)_{bd}\big)\right|_{\epsilon^i}={}&-\frac{1}{192}\eta^{cd}\big(\overline{\mathcal D_{c}\widehat R(Q)_{bd}}\gamma_{a}\widehat R(Q)^{ab}\big)\epsilon^i\\
&-\frac{1}{192}\eta^{cd}\big(\overline{\mathcal D_{c}\widehat R(Q)_{bd}}\gamma_{a}\gamma_p\widehat R(Q)^{ab}\big)\gamma^p\epsilon^i\\
&+\frac{1}{384}\eta^{cd}\big(\overline{\mathcal D_{c}\widehat R(Q)_{bd}}\gamma_{a}\gamma_{pq}\widehat R(Q)^{ab}\big)\gamma^{pq}\epsilon^i\\
&+\frac{1}{192}\eta^{cd}\big(\overline{\mathcal D_{a}\widehat R(Q)_{bd}}\gamma_{c}\widehat R(Q)^{ab}\big)\epsilon^i\\
&+\frac{1}{192}\eta^{cd}\big(\overline{\mathcal D_{a}\widehat R(Q)_{bd}}\gamma_{c}\gamma_p\widehat R(Q)^{ab}\big)\gamma^p\epsilon^i\\
&-\frac{1}{384}\eta^{cd}\big(\overline{\mathcal D_{a}\widehat R(Q)_{bd}}\gamma_{c}\gamma_{pq}\widehat R(Q)^{ab}\big)\gamma^{pq}\epsilon^i
\end{aligned}\tag{H092}
```

```math
\begin{aligned}
\left.\frac{i}{12}\eta^{cd}\widehat R(Q)^{ab}{}^i\big(\bar\epsilon \gamma_{[a}(\gamma\!\cdot\!T)\gamma_{c]}\widehat R(Q)_{bd}\big)\right|_{\epsilon^i}={}&\frac{i}{192}\eta^{cd}\big(\overline{\widehat R(Q)}_{bd}\gamma_{a}(\gamma\!\cdot\!T)\gamma_{c}\widehat R(Q)^{ab}\big)\epsilon^i\\
&+\frac{i}{192}\eta^{cd}\big(\overline{\widehat R(Q)}_{bd}\gamma_{a}(\gamma\!\cdot\!T)\gamma_{c}\gamma_p\widehat R(Q)^{ab}\big)\gamma^p\epsilon^i\\
&-\frac{i}{384}\eta^{cd}\big(\overline{\widehat R(Q)}_{bd}\gamma_{a}(\gamma\!\cdot\!T)\gamma_{c}\gamma_{pq}\widehat R(Q)^{ab}\big)\gamma^{pq}\epsilon^i\\
&-\frac{i}{192}\eta^{cd}\big(\overline{\widehat R(Q)}_{bd}\gamma_{c}(\gamma\!\cdot\!T)\gamma_{a}\widehat R(Q)^{ab}\big)\epsilon^i\\
&-\frac{i}{192}\eta^{cd}\big(\overline{\widehat R(Q)}_{bd}\gamma_{c}(\gamma\!\cdot\!T)\gamma_{a}\gamma_p\widehat R(Q)^{ab}\big)\gamma^p\epsilon^i\\
&+\frac{i}{384}\eta^{cd}\big(\overline{\widehat R(Q)}_{bd}\gamma_{c}(\gamma\!\cdot\!T)\gamma_{a}\gamma_{pq}\widehat R(Q)^{ab}\big)\gamma^{pq}\epsilon^i
\end{aligned}\tag{H093}
```

```math
\begin{aligned}
\left.\frac{4}{3}\eta_{[c[b}\eta^{cd}\widehat R(Q)^{ab}{}^i\big(\bar\epsilon \gamma_{d]}\mathcal D_{a]}\chi\big)\right|_{\epsilon^i}={}&\frac{1}{24}\eta_{cb}\eta^{cd}\big(\overline{\mathcal D_{a}\chi}\gamma_{d}\widehat R(Q)^{ab}\big)\epsilon^i\\
&+\frac{1}{24}\eta_{cb}\eta^{cd}\big(\overline{\mathcal D_{a}\chi}\gamma_{d}\gamma_p\widehat R(Q)^{ab}\big)\gamma^p\epsilon^i\\
&-\frac{1}{48}\eta_{cb}\eta^{cd}\big(\overline{\mathcal D_{a}\chi}\gamma_{d}\gamma_{pq}\widehat R(Q)^{ab}\big)\gamma^{pq}\epsilon^i\\
&-\frac{1}{24}\eta_{cd}\eta^{cd}\big(\overline{\mathcal D_{a}\chi}\gamma_{b}\widehat R(Q)^{ab}\big)\epsilon^i\\
&-\frac{1}{24}\eta_{cd}\eta^{cd}\big(\overline{\mathcal D_{a}\chi}\gamma_{b}\gamma_p\widehat R(Q)^{ab}\big)\gamma^p\epsilon^i\\
&+\frac{1}{48}\eta_{cd}\eta^{cd}\big(\overline{\mathcal D_{a}\chi}\gamma_{b}\gamma_{pq}\widehat R(Q)^{ab}\big)\gamma^{pq}\epsilon^i\\
&-\frac{1}{24}\eta_{ab}\eta^{cd}\big(\overline{\mathcal D_{c}\chi}\gamma_{d}\widehat R(Q)^{ab}\big)\epsilon^i\\
&-\frac{1}{24}\eta_{ab}\eta^{cd}\big(\overline{\mathcal D_{c}\chi}\gamma_{d}\gamma_p\widehat R(Q)^{ab}\big)\gamma^p\epsilon^i\\
&+\frac{1}{48}\eta_{ab}\eta^{cd}\big(\overline{\mathcal D_{c}\chi}\gamma_{d}\gamma_{pq}\widehat R(Q)^{ab}\big)\gamma^{pq}\epsilon^i\\
&+\frac{1}{24}\eta_{ad}\eta^{cd}\big(\overline{\mathcal D_{c}\chi}\gamma_{b}\widehat R(Q)^{ab}\big)\epsilon^i\\
&+\frac{1}{24}\eta_{ad}\eta^{cd}\big(\overline{\mathcal D_{c}\chi}\gamma_{b}\gamma_p\widehat R(Q)^{ab}\big)\gamma^p\epsilon^i\\
&-\frac{1}{48}\eta_{ad}\eta^{cd}\big(\overline{\mathcal D_{c}\chi}\gamma_{b}\gamma_{pq}\widehat R(Q)^{ab}\big)\gamma^{pq}\epsilon^i
\end{aligned}\tag{H094}
```

```math
\begin{aligned}
\left.\frac{4i}{3}\eta_{[c[b}\eta^{cd}\widehat R(Q)^{ab}{}^i\big(\bar\epsilon \gamma_{a]}(\gamma\!\cdot\!T)\gamma_{d]}\chi\big)\right|_{\epsilon^i}={}&-\frac{i}{24}\eta_{cb}\eta^{cd}\big(\bar\chi\gamma_{d}(\gamma\!\cdot\!T)\gamma_{a}\widehat R(Q)^{ab}\big)\epsilon^i\\
&-\frac{i}{24}\eta_{cb}\eta^{cd}\big(\bar\chi\gamma_{d}(\gamma\!\cdot\!T)\gamma_{a}\gamma_p\widehat R(Q)^{ab}\big)\gamma^p\epsilon^i\\
&+\frac{i}{48}\eta_{cb}\eta^{cd}\big(\bar\chi\gamma_{d}(\gamma\!\cdot\!T)\gamma_{a}\gamma_{pq}\widehat R(Q)^{ab}\big)\gamma^{pq}\epsilon^i\\
&+\frac{i}{24}\eta_{cd}\eta^{cd}\big(\bar\chi\gamma_{b}(\gamma\!\cdot\!T)\gamma_{a}\widehat R(Q)^{ab}\big)\epsilon^i\\
&+\frac{i}{24}\eta_{cd}\eta^{cd}\big(\bar\chi\gamma_{b}(\gamma\!\cdot\!T)\gamma_{a}\gamma_p\widehat R(Q)^{ab}\big)\gamma^p\epsilon^i\\
&-\frac{i}{48}\eta_{cd}\eta^{cd}\big(\bar\chi\gamma_{b}(\gamma\!\cdot\!T)\gamma_{a}\gamma_{pq}\widehat R(Q)^{ab}\big)\gamma^{pq}\epsilon^i\\
&+\frac{i}{24}\eta_{ab}\eta^{cd}\big(\bar\chi\gamma_{d}(\gamma\!\cdot\!T)\gamma_{c}\widehat R(Q)^{ab}\big)\epsilon^i\\
&+\frac{i}{24}\eta_{ab}\eta^{cd}\big(\bar\chi\gamma_{d}(\gamma\!\cdot\!T)\gamma_{c}\gamma_p\widehat R(Q)^{ab}\big)\gamma^p\epsilon^i\\
&-\frac{i}{48}\eta_{ab}\eta^{cd}\big(\bar\chi\gamma_{d}(\gamma\!\cdot\!T)\gamma_{c}\gamma_{pq}\widehat R(Q)^{ab}\big)\gamma^{pq}\epsilon^i\\
&-\frac{i}{24}\eta_{ad}\eta^{cd}\big(\bar\chi\gamma_{b}(\gamma\!\cdot\!T)\gamma_{c}\widehat R(Q)^{ab}\big)\epsilon^i\\
&-\frac{i}{24}\eta_{ad}\eta^{cd}\big(\bar\chi\gamma_{b}(\gamma\!\cdot\!T)\gamma_{c}\gamma_p\widehat R(Q)^{ab}\big)\gamma^p\epsilon^i\\
&+\frac{i}{48}\eta_{ad}\eta^{cd}\big(\bar\chi\gamma_{b}(\gamma\!\cdot\!T)\gamma_{c}\gamma_{pq}\widehat R(Q)^{ab}\big)\gamma^{pq}\epsilon^i
\end{aligned}\tag{H095}
```

### 27.8 Retained term 2: varying the tensor derivative

Insert each line of H62, then apply H05. Each equality below expands the weighted antisymmetrization and gives the three Fierz contributions for each resulting pairing, in scalar/vector/bivector order.

```math
\begin{aligned}
\left.2\gamma^c\widehat R(Q)^{ab}{}^i\big(\bar\epsilon \gamma_{bc}\mathcal D_a\chi\big)\right|_{\epsilon^i}={}&-\frac{1}{4}\gamma^c\big(\overline{\mathcal D_a\chi}\gamma_{bc}\widehat R(Q)^{ab}\big)\epsilon^i\\
&-\frac{1}{4}\gamma^c\big(\overline{\mathcal D_a\chi}\gamma_{bc}\gamma_p\widehat R(Q)^{ab}\big)\gamma^p\epsilon^i\\
&+\frac{1}{8}\gamma^c\big(\overline{\mathcal D_a\chi}\gamma_{bc}\gamma_{pq}\widehat R(Q)^{ab}\big)\gamma^{pq}\epsilon^i
\end{aligned}\tag{H096}
```

```math
\begin{aligned}
\left.-\frac{3}{8}\gamma^c\widehat R(Q)^{ab}{}^i\big(\bar\epsilon \mathcal D_a\widehat R(Q)_{bc}\big)\right|_{\epsilon^i}={}&-\frac{3}{64}\gamma^c\big(\overline{\mathcal D_a\widehat R(Q)_{bc}}\widehat R(Q)^{ab}\big)\epsilon^i\\
&-\frac{3}{64}\gamma^c\big(\overline{\mathcal D_a\widehat R(Q)_{bc}}\gamma_p\widehat R(Q)^{ab}\big)\gamma^p\epsilon^i\\
&+\frac{3}{128}\gamma^c\big(\overline{\mathcal D_a\widehat R(Q)_{bc}}\gamma_{pq}\widehat R(Q)^{ab}\big)\gamma^{pq}\epsilon^i
\end{aligned}\tag{H097}
```

```math
\begin{aligned}
\left.2i\gamma^c\widehat R(Q)^{ab}{}^i\big(\bar\epsilon \gamma_a(\gamma\!\cdot\!T)\gamma_{bc}\chi\big)\right|_{\epsilon^i}={}&\frac{i}{4}\gamma^c\big(\bar\chi\gamma_{bc}(\gamma\!\cdot\!T)\gamma_a\widehat R(Q)^{ab}\big)\epsilon^i\\
&+\frac{i}{4}\gamma^c\big(\bar\chi\gamma_{bc}(\gamma\!\cdot\!T)\gamma_a\gamma_p\widehat R(Q)^{ab}\big)\gamma^p\epsilon^i\\
&-\frac{i}{8}\gamma^c\big(\bar\chi\gamma_{bc}(\gamma\!\cdot\!T)\gamma_a\gamma_{pq}\widehat R(Q)^{ab}\big)\gamma^{pq}\epsilon^i
\end{aligned}\tag{H098}
```

```math
\begin{aligned}
\left.-\frac{3i}{8}\gamma^c\widehat R(Q)^{ab}{}^i\big(\bar\epsilon \gamma_a(\gamma\!\cdot\!T)\widehat R(Q)_{bc}\big)\right|_{\epsilon^i}={}&\frac{3i}{64}\gamma^c\big(\overline{\widehat R(Q)}_{bc}(\gamma\!\cdot\!T)\gamma_a\widehat R(Q)^{ab}\big)\epsilon^i\\
&+\frac{3i}{64}\gamma^c\big(\overline{\widehat R(Q)}_{bc}(\gamma\!\cdot\!T)\gamma_a\gamma_p\widehat R(Q)^{ab}\big)\gamma^p\epsilon^i\\
&-\frac{3i}{128}\gamma^c\big(\overline{\widehat R(Q)}_{bc}(\gamma\!\cdot\!T)\gamma_a\gamma_{pq}\widehat R(Q)^{ab}\big)\gamma^{pq}\epsilon^i
\end{aligned}\tag{H099}
```

```math
\begin{aligned}
\left.-8iT_{bc}\gamma^c\widehat R(Q)^{ab}{}^i\big(\bar\epsilon \gamma_a\chi\big)\right|_{\epsilon^i}={}&-iT_{bc}\gamma^c\big(\bar\chi\gamma_a\widehat R(Q)^{ab}\big)\epsilon^i\\
&-iT_{bc}\gamma^c\big(\bar\chi\gamma_a\gamma_p\widehat R(Q)^{ab}\big)\gamma^p\epsilon^i\\
&+\frac{i}{2}T_{bc}\gamma^c\big(\bar\chi\gamma_a\gamma_{pq}\widehat R(Q)^{ab}\big)\gamma^{pq}\epsilon^i
\end{aligned}\tag{H100}
```

```math
\begin{aligned}
\left.2iT_{dc}\gamma^c\widehat R(Q)^{ab}{}^i\big(\bar\epsilon \gamma_{[b}\widehat R(Q)_a{}^{d]}\big)\right|_{\epsilon^i}={}&\frac{i}{8}T_{dc}\gamma^c\big(\overline{\widehat R(Q)}_a{}^{d}\gamma_{b}\widehat R(Q)^{ab}\big)\epsilon^i\\
&+\frac{i}{8}T_{dc}\gamma^c\big(\overline{\widehat R(Q)}_a{}^{d}\gamma_{b}\gamma_p\widehat R(Q)^{ab}\big)\gamma^p\epsilon^i\\
&-\frac{i}{16}T_{dc}\gamma^c\big(\overline{\widehat R(Q)}_a{}^{d}\gamma_{b}\gamma_{pq}\widehat R(Q)^{ab}\big)\gamma^{pq}\epsilon^i\\
&-\frac{i}{8}T_{dc}\gamma^c\big(\overline{\widehat R(Q)}_a{}^{b}\gamma_{d}\widehat R(Q)^{ab}\big)\epsilon^i\\
&-\frac{i}{8}T_{dc}\gamma^c\big(\overline{\widehat R(Q)}_a{}^{b}\gamma_{d}\gamma_p\widehat R(Q)^{ab}\big)\gamma^p\epsilon^i\\
&+\frac{i}{16}T_{dc}\gamma^c\big(\overline{\widehat R(Q)}_a{}^{b}\gamma_{d}\gamma_{pq}\widehat R(Q)^{ab}\big)\gamma^{pq}\epsilon^i
\end{aligned}\tag{H101}
```

```math
\begin{aligned}
\left.iT_{dc}\gamma^c\widehat R(Q)^{ab}{}^i\big(\bar\epsilon \gamma_a\widehat R(Q)_b{}^d\big)\right|_{\epsilon^i}={}&\frac{i}{8}T_{dc}\gamma^c\big(\overline{\widehat R(Q)}_b{}^d\gamma_a\widehat R(Q)^{ab}\big)\epsilon^i\\
&+\frac{i}{8}T_{dc}\gamma^c\big(\overline{\widehat R(Q)}_b{}^d\gamma_a\gamma_p\widehat R(Q)^{ab}\big)\gamma^p\epsilon^i\\
&-\frac{i}{16}T_{dc}\gamma^c\big(\overline{\widehat R(Q)}_b{}^d\gamma_a\gamma_{pq}\widehat R(Q)^{ab}\big)\gamma^{pq}\epsilon^i
\end{aligned}\tag{H102}
```

```math
\begin{aligned}
\left.16i\eta_{a[b}T_{dc}\gamma^c\widehat R(Q)^{ab}{}^i\big(\bar\epsilon \gamma^{d]}\chi\big)\right|_{\epsilon^i}={}&i\eta_{ab}T_{dc}\gamma^c\big(\bar\chi\gamma^{d}\widehat R(Q)^{ab}\big)\epsilon^i\\
&+i\eta_{ab}T_{dc}\gamma^c\big(\bar\chi\gamma^{d}\gamma_p\widehat R(Q)^{ab}\big)\gamma^p\epsilon^i\\
&-\frac{i}{2}\eta_{ab}T_{dc}\gamma^c\big(\bar\chi\gamma^{d}\gamma_{pq}\widehat R(Q)^{ab}\big)\gamma^{pq}\epsilon^i\\
&-i\eta_{ad}T_{dc}\gamma^c\big(\bar\chi\gamma^{b}\widehat R(Q)^{ab}\big)\epsilon^i\\
&-i\eta_{ad}T_{dc}\gamma^c\big(\bar\chi\gamma^{b}\gamma_p\widehat R(Q)^{ab}\big)\gamma^p\epsilon^i\\
&+\frac{i}{2}\eta_{ad}T_{dc}\gamma^c\big(\bar\chi\gamma^{b}\gamma_{pq}\widehat R(Q)^{ab}\big)\gamma^{pq}\epsilon^i
\end{aligned}\tag{H103}
```

```math
\begin{aligned}
\left.2iT_{bd}\gamma^c\widehat R(Q)^{ab}{}^i\big(\bar\epsilon \gamma_{[c}\widehat R(Q)_a{}^{d]}\big)\right|_{\epsilon^i}={}&\frac{i}{8}T_{bd}\gamma^c\big(\overline{\widehat R(Q)}_a{}^{d}\gamma_{c}\widehat R(Q)^{ab}\big)\epsilon^i\\
&+\frac{i}{8}T_{bd}\gamma^c\big(\overline{\widehat R(Q)}_a{}^{d}\gamma_{c}\gamma_p\widehat R(Q)^{ab}\big)\gamma^p\epsilon^i\\
&-\frac{i}{16}T_{bd}\gamma^c\big(\overline{\widehat R(Q)}_a{}^{d}\gamma_{c}\gamma_{pq}\widehat R(Q)^{ab}\big)\gamma^{pq}\epsilon^i\\
&-\frac{i}{8}T_{bd}\gamma^c\big(\overline{\widehat R(Q)}_a{}^{c}\gamma_{d}\widehat R(Q)^{ab}\big)\epsilon^i\\
&-\frac{i}{8}T_{bd}\gamma^c\big(\overline{\widehat R(Q)}_a{}^{c}\gamma_{d}\gamma_p\widehat R(Q)^{ab}\big)\gamma^p\epsilon^i\\
&+\frac{i}{16}T_{bd}\gamma^c\big(\overline{\widehat R(Q)}_a{}^{c}\gamma_{d}\gamma_{pq}\widehat R(Q)^{ab}\big)\gamma^{pq}\epsilon^i
\end{aligned}\tag{H104}
```

```math
\begin{aligned}
\left.iT_{bd}\gamma^c\widehat R(Q)^{ab}{}^i\big(\bar\epsilon \gamma_a\widehat R(Q)_c{}^d\big)\right|_{\epsilon^i}={}&\frac{i}{8}T_{bd}\gamma^c\big(\overline{\widehat R(Q)}_c{}^d\gamma_a\widehat R(Q)^{ab}\big)\epsilon^i\\
&+\frac{i}{8}T_{bd}\gamma^c\big(\overline{\widehat R(Q)}_c{}^d\gamma_a\gamma_p\widehat R(Q)^{ab}\big)\gamma^p\epsilon^i\\
&-\frac{i}{16}T_{bd}\gamma^c\big(\overline{\widehat R(Q)}_c{}^d\gamma_a\gamma_{pq}\widehat R(Q)^{ab}\big)\gamma^{pq}\epsilon^i
\end{aligned}\tag{H105}
```

```math
\begin{aligned}
\left.16i\eta_{a[c}T_{bd}\gamma^c\widehat R(Q)^{ab}{}^i\big(\bar\epsilon \gamma^{d]}\chi\big)\right|_{\epsilon^i}={}&i\eta_{ac}T_{bd}\gamma^c\big(\bar\chi\gamma^{d}\widehat R(Q)^{ab}\big)\epsilon^i\\
&+i\eta_{ac}T_{bd}\gamma^c\big(\bar\chi\gamma^{d}\gamma_p\widehat R(Q)^{ab}\big)\gamma^p\epsilon^i\\
&-\frac{i}{2}\eta_{ac}T_{bd}\gamma^c\big(\bar\chi\gamma^{d}\gamma_{pq}\widehat R(Q)^{ab}\big)\gamma^{pq}\epsilon^i\\
&-i\eta_{ad}T_{bd}\gamma^c\big(\bar\chi\gamma^{c}\widehat R(Q)^{ab}\big)\epsilon^i\\
&-i\eta_{ad}T_{bd}\gamma^c\big(\bar\chi\gamma^{c}\gamma_p\widehat R(Q)^{ab}\big)\gamma^p\epsilon^i\\
&+\frac{i}{2}\eta_{ad}T_{bd}\gamma^c\big(\bar\chi\gamma^{c}\gamma_{pq}\widehat R(Q)^{ab}\big)\gamma^{pq}\epsilon^i
\end{aligned}\tag{H106}
```

### 27.9 Retained term 6: varying the tensor derivative

Insert each line of H62, then apply H05. Each equality below expands the weighted antisymmetrization and gives the three Fierz contributions for each resulting pairing, in scalar/vector/bivector order.

```math
\begin{aligned}
\left.\frac{32}{3}\gamma^{ab}\gamma^c\chi{}^i\big(\bar\epsilon \gamma_{bc}\mathcal D_a\chi\big)\right|_{\epsilon^i}={}&-\frac{4}{3}\gamma^{ab}\gamma^c\big(\overline{\mathcal D_a\chi}\gamma_{bc}\chi\big)\epsilon^i\\
&-\frac{4}{3}\gamma^{ab}\gamma^c\big(\overline{\mathcal D_a\chi}\gamma_{bc}\gamma_p\chi\big)\gamma^p\epsilon^i\\
&+\frac{2}{3}\gamma^{ab}\gamma^c\big(\overline{\mathcal D_a\chi}\gamma_{bc}\gamma_{pq}\chi\big)\gamma^{pq}\epsilon^i
\end{aligned}\tag{H107}
```

```math
\begin{aligned}
\left.-2\gamma^{ab}\gamma^c\chi{}^i\big(\bar\epsilon \mathcal D_a\widehat R(Q)_{bc}\big)\right|_{\epsilon^i}={}&-\frac{1}{4}\gamma^{ab}\gamma^c\big(\overline{\mathcal D_a\widehat R(Q)_{bc}}\chi\big)\epsilon^i\\
&-\frac{1}{4}\gamma^{ab}\gamma^c\big(\overline{\mathcal D_a\widehat R(Q)_{bc}}\gamma_p\chi\big)\gamma^p\epsilon^i\\
&+\frac{1}{8}\gamma^{ab}\gamma^c\big(\overline{\mathcal D_a\widehat R(Q)_{bc}}\gamma_{pq}\chi\big)\gamma^{pq}\epsilon^i
\end{aligned}\tag{H108}
```

```math
\begin{aligned}
\left.\frac{32i}{3}\gamma^{ab}\gamma^c\chi{}^i\big(\bar\epsilon \gamma_a(\gamma\!\cdot\!T)\gamma_{bc}\chi\big)\right|_{\epsilon^i}={}&\frac{4i}{3}\gamma^{ab}\gamma^c\big(\bar\chi\gamma_{bc}(\gamma\!\cdot\!T)\gamma_a\chi\big)\epsilon^i\\
&+\frac{4i}{3}\gamma^{ab}\gamma^c\big(\bar\chi\gamma_{bc}(\gamma\!\cdot\!T)\gamma_a\gamma_p\chi\big)\gamma^p\epsilon^i\\
&-\frac{2i}{3}\gamma^{ab}\gamma^c\big(\bar\chi\gamma_{bc}(\gamma\!\cdot\!T)\gamma_a\gamma_{pq}\chi\big)\gamma^{pq}\epsilon^i
\end{aligned}\tag{H109}
```

```math
\begin{aligned}
\left.-2i\gamma^{ab}\gamma^c\chi{}^i\big(\bar\epsilon \gamma_a(\gamma\!\cdot\!T)\widehat R(Q)_{bc}\big)\right|_{\epsilon^i}={}&\frac{i}{4}\gamma^{ab}\gamma^c\big(\overline{\widehat R(Q)}_{bc}(\gamma\!\cdot\!T)\gamma_a\chi\big)\epsilon^i\\
&+\frac{i}{4}\gamma^{ab}\gamma^c\big(\overline{\widehat R(Q)}_{bc}(\gamma\!\cdot\!T)\gamma_a\gamma_p\chi\big)\gamma^p\epsilon^i\\
&-\frac{i}{8}\gamma^{ab}\gamma^c\big(\overline{\widehat R(Q)}_{bc}(\gamma\!\cdot\!T)\gamma_a\gamma_{pq}\chi\big)\gamma^{pq}\epsilon^i
\end{aligned}\tag{H110}
```

```math
\begin{aligned}
\left.-\frac{128i}{3}T_{bc}\gamma^{ab}\gamma^c\chi{}^i\big(\bar\epsilon \gamma_a\chi\big)\right|_{\epsilon^i}={}&-\frac{16i}{3}T_{bc}\gamma^{ab}\gamma^c\big(\bar\chi\gamma_a\chi\big)\epsilon^i\\
&-\frac{16i}{3}T_{bc}\gamma^{ab}\gamma^c\big(\bar\chi\gamma_a\gamma_p\chi\big)\gamma^p\epsilon^i\\
&+\frac{8i}{3}T_{bc}\gamma^{ab}\gamma^c\big(\bar\chi\gamma_a\gamma_{pq}\chi\big)\gamma^{pq}\epsilon^i
\end{aligned}\tag{H111}
```

```math
\begin{aligned}
\left.\frac{32i}{3}T_{dc}\gamma^{ab}\gamma^c\chi{}^i\big(\bar\epsilon \gamma_{[b}\widehat R(Q)_a{}^{d]}\big)\right|_{\epsilon^i}={}&\frac{2i}{3}T_{dc}\gamma^{ab}\gamma^c\big(\overline{\widehat R(Q)}_a{}^{d}\gamma_{b}\chi\big)\epsilon^i\\
&+\frac{2i}{3}T_{dc}\gamma^{ab}\gamma^c\big(\overline{\widehat R(Q)}_a{}^{d}\gamma_{b}\gamma_p\chi\big)\gamma^p\epsilon^i\\
&-\frac{i}{3}T_{dc}\gamma^{ab}\gamma^c\big(\overline{\widehat R(Q)}_a{}^{d}\gamma_{b}\gamma_{pq}\chi\big)\gamma^{pq}\epsilon^i\\
&-\frac{2i}{3}T_{dc}\gamma^{ab}\gamma^c\big(\overline{\widehat R(Q)}_a{}^{b}\gamma_{d}\chi\big)\epsilon^i\\
&-\frac{2i}{3}T_{dc}\gamma^{ab}\gamma^c\big(\overline{\widehat R(Q)}_a{}^{b}\gamma_{d}\gamma_p\chi\big)\gamma^p\epsilon^i\\
&+\frac{i}{3}T_{dc}\gamma^{ab}\gamma^c\big(\overline{\widehat R(Q)}_a{}^{b}\gamma_{d}\gamma_{pq}\chi\big)\gamma^{pq}\epsilon^i
\end{aligned}\tag{H112}
```

```math
\begin{aligned}
\left.\frac{16i}{3}T_{dc}\gamma^{ab}\gamma^c\chi{}^i\big(\bar\epsilon \gamma_a\widehat R(Q)_b{}^d\big)\right|_{\epsilon^i}={}&\frac{2i}{3}T_{dc}\gamma^{ab}\gamma^c\big(\overline{\widehat R(Q)}_b{}^d\gamma_a\chi\big)\epsilon^i\\
&+\frac{2i}{3}T_{dc}\gamma^{ab}\gamma^c\big(\overline{\widehat R(Q)}_b{}^d\gamma_a\gamma_p\chi\big)\gamma^p\epsilon^i\\
&-\frac{i}{3}T_{dc}\gamma^{ab}\gamma^c\big(\overline{\widehat R(Q)}_b{}^d\gamma_a\gamma_{pq}\chi\big)\gamma^{pq}\epsilon^i
\end{aligned}\tag{H113}
```

```math
\begin{aligned}
\left.\frac{256i}{3}\eta_{a[b}T_{dc}\gamma^{ab}\gamma^c\chi{}^i\big(\bar\epsilon \gamma^{d]}\chi\big)\right|_{\epsilon^i}={}&\frac{16i}{3}\eta_{ab}T_{dc}\gamma^{ab}\gamma^c\big(\bar\chi\gamma^{d}\chi\big)\epsilon^i\\
&+\frac{16i}{3}\eta_{ab}T_{dc}\gamma^{ab}\gamma^c\big(\bar\chi\gamma^{d}\gamma_p\chi\big)\gamma^p\epsilon^i\\
&-\frac{8i}{3}\eta_{ab}T_{dc}\gamma^{ab}\gamma^c\big(\bar\chi\gamma^{d}\gamma_{pq}\chi\big)\gamma^{pq}\epsilon^i\\
&-\frac{16i}{3}\eta_{ad}T_{dc}\gamma^{ab}\gamma^c\big(\bar\chi\gamma^{b}\chi\big)\epsilon^i\\
&-\frac{16i}{3}\eta_{ad}T_{dc}\gamma^{ab}\gamma^c\big(\bar\chi\gamma^{b}\gamma_p\chi\big)\gamma^p\epsilon^i\\
&+\frac{8i}{3}\eta_{ad}T_{dc}\gamma^{ab}\gamma^c\big(\bar\chi\gamma^{b}\gamma_{pq}\chi\big)\gamma^{pq}\epsilon^i
\end{aligned}\tag{H114}
```

```math
\begin{aligned}
\left.\frac{32i}{3}T_{bd}\gamma^{ab}\gamma^c\chi{}^i\big(\bar\epsilon \gamma_{[c}\widehat R(Q)_a{}^{d]}\big)\right|_{\epsilon^i}={}&\frac{2i}{3}T_{bd}\gamma^{ab}\gamma^c\big(\overline{\widehat R(Q)}_a{}^{d}\gamma_{c}\chi\big)\epsilon^i\\
&+\frac{2i}{3}T_{bd}\gamma^{ab}\gamma^c\big(\overline{\widehat R(Q)}_a{}^{d}\gamma_{c}\gamma_p\chi\big)\gamma^p\epsilon^i\\
&-\frac{i}{3}T_{bd}\gamma^{ab}\gamma^c\big(\overline{\widehat R(Q)}_a{}^{d}\gamma_{c}\gamma_{pq}\chi\big)\gamma^{pq}\epsilon^i\\
&-\frac{2i}{3}T_{bd}\gamma^{ab}\gamma^c\big(\overline{\widehat R(Q)}_a{}^{c}\gamma_{d}\chi\big)\epsilon^i\\
&-\frac{2i}{3}T_{bd}\gamma^{ab}\gamma^c\big(\overline{\widehat R(Q)}_a{}^{c}\gamma_{d}\gamma_p\chi\big)\gamma^p\epsilon^i\\
&+\frac{i}{3}T_{bd}\gamma^{ab}\gamma^c\big(\overline{\widehat R(Q)}_a{}^{c}\gamma_{d}\gamma_{pq}\chi\big)\gamma^{pq}\epsilon^i
\end{aligned}\tag{H115}
```

```math
\begin{aligned}
\left.\frac{16i}{3}T_{bd}\gamma^{ab}\gamma^c\chi{}^i\big(\bar\epsilon \gamma_a\widehat R(Q)_c{}^d\big)\right|_{\epsilon^i}={}&\frac{2i}{3}T_{bd}\gamma^{ab}\gamma^c\big(\overline{\widehat R(Q)}_c{}^d\gamma_a\chi\big)\epsilon^i\\
&+\frac{2i}{3}T_{bd}\gamma^{ab}\gamma^c\big(\overline{\widehat R(Q)}_c{}^d\gamma_a\gamma_p\chi\big)\gamma^p\epsilon^i\\
&-\frac{i}{3}T_{bd}\gamma^{ab}\gamma^c\big(\overline{\widehat R(Q)}_c{}^d\gamma_a\gamma_{pq}\chi\big)\gamma^{pq}\epsilon^i
\end{aligned}\tag{H116}
```

```math
\begin{aligned}
\left.\frac{256i}{3}\eta_{a[c}T_{bd}\gamma^{ab}\gamma^c\chi{}^i\big(\bar\epsilon \gamma^{d]}\chi\big)\right|_{\epsilon^i}={}&\frac{16i}{3}\eta_{ac}T_{bd}\gamma^{ab}\gamma^c\big(\bar\chi\gamma^{d}\chi\big)\epsilon^i\\
&+\frac{16i}{3}\eta_{ac}T_{bd}\gamma^{ab}\gamma^c\big(\bar\chi\gamma^{d}\gamma_p\chi\big)\gamma^p\epsilon^i\\
&-\frac{8i}{3}\eta_{ac}T_{bd}\gamma^{ab}\gamma^c\big(\bar\chi\gamma^{d}\gamma_{pq}\chi\big)\gamma^{pq}\epsilon^i\\
&-\frac{16i}{3}\eta_{ad}T_{bd}\gamma^{ab}\gamma^c\big(\bar\chi\gamma^{c}\chi\big)\epsilon^i\\
&-\frac{16i}{3}\eta_{ad}T_{bd}\gamma^{ab}\gamma^c\big(\bar\chi\gamma^{c}\gamma_p\chi\big)\gamma^p\epsilon^i\\
&+\frac{8i}{3}\eta_{ad}T_{bd}\gamma^{ab}\gamma^c\big(\bar\chi\gamma^{c}\gamma_{pq}\chi\big)\gamma^{pq}\epsilon^i
\end{aligned}\tag{H117}
```

### 27.10 Retained term 4: varying the spinor derivative

First insert the differentiated Q-law and the dependent S-connection contribution. Distribute every coefficient and both differentiated $`T`$ factors:

```math
\begin{aligned}
&2iT^{ab}\gamma^c(\mathcal D_c\widehat C_{ab}{}^{de})\gamma_{de}\epsilon^i\\
&-16T^{ab}\gamma^c\gamma^{de}(\mathcal D_c\mathcal D_{[a}T_{de})\gamma_{b]}\epsilon^i\\
&+\frac{16}{3}T^{ab}\gamma^c\gamma_{[b}\gamma^{de}(\mathcal D_c\mathcal D_{a]}T_{de})\epsilon^i\\
&+\frac{16}{3}T^{ab}\gamma^c\gamma_{[a}\gamma^f\gamma^{de}(\mathcal D_c\mathcal D_fT_{de})\gamma_{b]}\epsilon^i\\
&+\frac{16}{3}T^{ab}\gamma^c\gamma_{ab}\gamma_d\mathcal D_c\mathcal D_eT^{ed}\epsilon^i\\
&+2T^{ab}\gamma^c\widehat C_{ab}{}^{de}\gamma_{de}(\gamma\!\cdot\!T)\gamma_c\epsilon^i\\
&+16iT^{ab}\gamma^c\gamma^{de}(\mathcal D_{[a}T_{de})\gamma_{b]}(\gamma\!\cdot\!T)\gamma_c\epsilon^i\\
&-\frac{16i}{3}T^{ab}\gamma^c\gamma_{[b}\gamma^{de}(\mathcal D_{a]}T_{de})(\gamma\!\cdot\!T)\gamma_c\epsilon^i\\
&-\frac{16i}{3}T^{ab}\gamma^c\gamma_{[a}\gamma^f\gamma^{de}(\mathcal D_fT_{de})\gamma_{b]}(\gamma\!\cdot\!T)\gamma_c\epsilon^i\\
&-\frac{16i}{3}T^{ab}\gamma^c\gamma_{ab}\gamma_d(\mathcal D_eT^{ed})(\gamma\!\cdot\!T)\gamma_c\epsilon^i\\
&+\frac{64i}{3}T^{ab}\gamma^cT_{ab}\gamma^s\gamma^{hr}(\mathcal D_sT_{hr})\gamma_c\epsilon^i\\
&-\frac{64i}{3}T^{ab}\gamma^cT_{ab}\gamma^{hr}(\mathcal D_cT_{hr})\epsilon^i\\
&+\frac{64i}{3}T^{ab}\gamma^cT_{ab}\gamma_c\gamma^r(\mathcal D^hT_{hr})\epsilon^i\\
&+64T^{ab}\gamma^cT_{ab}\gamma_{chrst}T^{hr}T^{st}\epsilon^i\\
&-512T^{ab}\gamma^cT_{ab}\gamma_hT^{hr}T_{cr}\epsilon^i\\
&+128T^{ab}\gamma^cT_{ab}\gamma_cT^2\epsilon^i\\
&-\frac{128i}{9}T^{ab}\gamma^cT_{[a}{}^d\gamma_{b]d}\gamma^s\gamma^{hr}(\mathcal D_sT_{hr})\gamma_c\epsilon^i\\
&+\frac{128i}{9}T^{ab}\gamma^cT_{[a}{}^d\gamma_{b]d}\gamma^{hr}(\mathcal D_cT_{hr})\epsilon^i\\
&-\frac{128i}{9}T^{ab}\gamma^cT_{[a}{}^d\gamma_{b]d}\gamma_c\gamma^r(\mathcal D^hT_{hr})\epsilon^i\\
&-\frac{128}{3}T^{ab}\gamma^cT_{[a}{}^d\gamma_{b]d}\gamma_{chrst}T^{hr}T^{st}\epsilon^i\\
&+\frac{1024}{3}T^{ab}\gamma^cT_{[a}{}^d\gamma_{b]d}\gamma_hT^{hr}T_{cr}\epsilon^i\\
&-\frac{256}{3}T^{ab}\gamma^cT_{[a}{}^d\gamma_{b]d}\gamma_cT^2\epsilon^i\\
&-\frac{32i}{9}T^{ab}\gamma^c\gamma_{abde}T^{de}\gamma^s\gamma^{hr}(\mathcal D_sT_{hr})\gamma_c\epsilon^i\\
&+\frac{32i}{9}T^{ab}\gamma^c\gamma_{abde}T^{de}\gamma^{hr}(\mathcal D_cT_{hr})\epsilon^i\\
&-\frac{32i}{9}T^{ab}\gamma^c\gamma_{abde}T^{de}\gamma_c\gamma^r(\mathcal D^hT_{hr})\epsilon^i\\
&-\frac{32}{3}T^{ab}\gamma^c\gamma_{abde}T^{de}\gamma_{chrst}T^{hr}T^{st}\epsilon^i\\
&+\frac{256}{3}T^{ab}\gamma^c\gamma_{abde}T^{de}\gamma_hT^{hr}T_{cr}\epsilon^i\\
&-\frac{64}{3}T^{ab}\gamma^c\gamma_{abde}T^{de}\gamma_cT^2\epsilon^i
\end{aligned}\tag{H118}
```

Next insert the weight, spin, SU(2), and (for the gravitino curvature) tensor-index connection variations. The SU(2) connection uses H08; the other lines use H05.

```math
\begin{aligned}
\left.24iT^{ab}\gamma^c\widehat R(Q)_{ab}{}^i\big(\bar\epsilon \gamma_c\chi\big)\right|_{\epsilon^i}={}&3iT^{ab}\gamma^c\big(\bar\chi\gamma_c\widehat R(Q)_{ab}\big)\epsilon^i\\
&+3iT^{ab}\gamma^c\big(\bar\chi\gamma_c\gamma_p\widehat R(Q)_{ab}\big)\gamma^p\epsilon^i\\
&-\frac{3i}{2}T^{ab}\gamma^c\big(\bar\chi\gamma_c\gamma_{pq}\widehat R(Q)_{ab}\big)\gamma^{pq}\epsilon^i
\end{aligned}\tag{H119}
```

```math
\begin{aligned}
\left.-iT^{ab}\gamma^c\gamma_{de}\widehat R(Q)_{ab}{}^i\big(\bar\epsilon \gamma^{[d}\widehat R(Q)_c{}^{e]}\big)\right|_{\epsilon^i}={}&-\frac{i}{16}T^{ab}\gamma^c\gamma_{de}\big(\overline{\widehat R(Q)}_c{}^{e}\gamma^{d}\widehat R(Q)_{ab}\big)\epsilon^i\\
&-\frac{i}{16}T^{ab}\gamma^c\gamma_{de}\big(\overline{\widehat R(Q)}_c{}^{e}\gamma^{d}\gamma_p\widehat R(Q)_{ab}\big)\gamma^p\epsilon^i\\
&+\frac{i}{32}T^{ab}\gamma^c\gamma_{de}\big(\overline{\widehat R(Q)}_c{}^{e}\gamma^{d}\gamma_{pq}\widehat R(Q)_{ab}\big)\gamma^{pq}\epsilon^i\\
&+\frac{i}{16}T^{ab}\gamma^c\gamma_{de}\big(\overline{\widehat R(Q)}_c{}^{d}\gamma^{e}\widehat R(Q)_{ab}\big)\epsilon^i\\
&+\frac{i}{16}T^{ab}\gamma^c\gamma_{de}\big(\overline{\widehat R(Q)}_c{}^{d}\gamma^{e}\gamma_p\widehat R(Q)_{ab}\big)\gamma^p\epsilon^i\\
&-\frac{i}{32}T^{ab}\gamma^c\gamma_{de}\big(\overline{\widehat R(Q)}_c{}^{d}\gamma^{e}\gamma_{pq}\widehat R(Q)_{ab}\big)\gamma^{pq}\epsilon^i
\end{aligned}\tag{H120}
```

```math
\begin{aligned}
\left.-\frac{i}{2}T^{ab}\gamma^c\gamma_{de}\widehat R(Q)_{ab}{}^i\big(\bar\epsilon \gamma_c\widehat R(Q)^{de}\big)\right|_{\epsilon^i}={}&-\frac{i}{16}T^{ab}\gamma^c\gamma_{de}\big(\overline{\widehat R(Q)}^{de}\gamma_c\widehat R(Q)_{ab}\big)\epsilon^i\\
&-\frac{i}{16}T^{ab}\gamma^c\gamma_{de}\big(\overline{\widehat R(Q)}^{de}\gamma_c\gamma_p\widehat R(Q)_{ab}\big)\gamma^p\epsilon^i\\
&+\frac{i}{32}T^{ab}\gamma^c\gamma_{de}\big(\overline{\widehat R(Q)}^{de}\gamma_c\gamma_{pq}\widehat R(Q)_{ab}\big)\gamma^{pq}\epsilon^i
\end{aligned}\tag{H121}
```

```math
\begin{aligned}
\left.-8i\delta_c{}^{[d}T^{ab}\gamma^c\gamma_{de}\widehat R(Q)_{ab}{}^i\big(\bar\epsilon \gamma^{e]}\chi\big)\right|_{\epsilon^i}={}&-\frac{i}{2}\delta_c{}^{d}T^{ab}\gamma^c\gamma_{de}\big(\bar\chi\gamma^{e}\widehat R(Q)_{ab}\big)\epsilon^i\\
&-\frac{i}{2}\delta_c{}^{d}T^{ab}\gamma^c\gamma_{de}\big(\bar\chi\gamma^{e}\gamma_p\widehat R(Q)_{ab}\big)\gamma^p\epsilon^i\\
&+\frac{i}{4}\delta_c{}^{d}T^{ab}\gamma^c\gamma_{de}\big(\bar\chi\gamma^{e}\gamma_{pq}\widehat R(Q)_{ab}\big)\gamma^{pq}\epsilon^i\\
&+\frac{i}{2}\delta_c{}^{e}T^{ab}\gamma^c\gamma_{de}\big(\bar\chi\gamma^{d}\widehat R(Q)_{ab}\big)\epsilon^i\\
&+\frac{i}{2}\delta_c{}^{e}T^{ab}\gamma^c\gamma_{de}\big(\bar\chi\gamma^{d}\gamma_p\widehat R(Q)_{ab}\big)\gamma^p\epsilon^i\\
&-\frac{i}{4}\delta_c{}^{e}T^{ab}\gamma^c\gamma_{de}\big(\bar\chi\gamma^{d}\gamma_{pq}\widehat R(Q)_{ab}\big)\gamma^{pq}\epsilon^i
\end{aligned}\tag{H122}
```

```math
\begin{aligned}
\left.32iT^{ab}\gamma^c\bar\epsilon^{(i}\gamma_c\chi^{k)}\varepsilon_{kl}\widehat R(Q)_{ab}{}^l\right|_{\epsilon^i}={}&6iT^{ab}\gamma^c\big(\bar\chi\gamma_c\widehat R(Q)_{ab}\big)\epsilon^i\\
&+6iT^{ab}\gamma^c\big(\bar\chi\gamma_c\gamma_p\widehat R(Q)_{ab}\big)\gamma^p\epsilon^i\\
&-3iT^{ab}\gamma^c\big(\bar\chi\gamma_c\gamma_{pq}\widehat R(Q)_{ab}\big)\gamma^{pq}\epsilon^i
\end{aligned}\tag{H123}
```

```math
\begin{aligned}
\left.-4iT^{ab}\gamma^c\widehat R(Q)_{db}{}^i\big(\bar\epsilon \gamma_{[a}\widehat R(Q)_c{}^{d]}\big)\right|_{\epsilon^i}={}&-\frac{i}{4}T^{ab}\gamma^c\big(\overline{\widehat R(Q)}_c{}^{d}\gamma_{a}\widehat R(Q)_{db}\big)\epsilon^i\\
&-\frac{i}{4}T^{ab}\gamma^c\big(\overline{\widehat R(Q)}_c{}^{d}\gamma_{a}\gamma_p\widehat R(Q)_{db}\big)\gamma^p\epsilon^i\\
&+\frac{i}{8}T^{ab}\gamma^c\big(\overline{\widehat R(Q)}_c{}^{d}\gamma_{a}\gamma_{pq}\widehat R(Q)_{db}\big)\gamma^{pq}\epsilon^i\\
&+\frac{i}{4}T^{ab}\gamma^c\big(\overline{\widehat R(Q)}_c{}^{a}\gamma_{d}\widehat R(Q)_{db}\big)\epsilon^i\\
&+\frac{i}{4}T^{ab}\gamma^c\big(\overline{\widehat R(Q)}_c{}^{a}\gamma_{d}\gamma_p\widehat R(Q)_{db}\big)\gamma^p\epsilon^i\\
&-\frac{i}{8}T^{ab}\gamma^c\big(\overline{\widehat R(Q)}_c{}^{a}\gamma_{d}\gamma_{pq}\widehat R(Q)_{db}\big)\gamma^{pq}\epsilon^i
\end{aligned}\tag{H124}
```

```math
\begin{aligned}
\left.-2iT^{ab}\gamma^c\widehat R(Q)_{db}{}^i\big(\bar\epsilon \gamma_c\widehat R(Q)_a{}^d\big)\right|_{\epsilon^i}={}&-\frac{i}{4}T^{ab}\gamma^c\big(\overline{\widehat R(Q)}_a{}^d\gamma_c\widehat R(Q)_{db}\big)\epsilon^i\\
&-\frac{i}{4}T^{ab}\gamma^c\big(\overline{\widehat R(Q)}_a{}^d\gamma_c\gamma_p\widehat R(Q)_{db}\big)\gamma^p\epsilon^i\\
&+\frac{i}{8}T^{ab}\gamma^c\big(\overline{\widehat R(Q)}_a{}^d\gamma_c\gamma_{pq}\widehat R(Q)_{db}\big)\gamma^{pq}\epsilon^i
\end{aligned}\tag{H125}
```

```math
\begin{aligned}
\left.-32i\eta_{c[a}T^{ab}\gamma^c\widehat R(Q)_{db}{}^i\big(\bar\epsilon \gamma^{d]}\chi\big)\right|_{\epsilon^i}={}&-2i\eta_{ca}T^{ab}\gamma^c\big(\bar\chi\gamma^{d}\widehat R(Q)_{db}\big)\epsilon^i\\
&-2i\eta_{ca}T^{ab}\gamma^c\big(\bar\chi\gamma^{d}\gamma_p\widehat R(Q)_{db}\big)\gamma^p\epsilon^i\\
&+i\eta_{ca}T^{ab}\gamma^c\big(\bar\chi\gamma^{d}\gamma_{pq}\widehat R(Q)_{db}\big)\gamma^{pq}\epsilon^i\\
&+2i\eta_{cd}T^{ab}\gamma^c\big(\bar\chi\gamma^{a}\widehat R(Q)_{db}\big)\epsilon^i\\
&+2i\eta_{cd}T^{ab}\gamma^c\big(\bar\chi\gamma^{a}\gamma_p\widehat R(Q)_{db}\big)\gamma^p\epsilon^i\\
&-i\eta_{cd}T^{ab}\gamma^c\big(\bar\chi\gamma^{a}\gamma_{pq}\widehat R(Q)_{db}\big)\gamma^{pq}\epsilon^i
\end{aligned}\tag{H126}
```

```math
\begin{aligned}
\left.-4iT^{ab}\gamma^c\widehat R(Q)_{ad}{}^i\big(\bar\epsilon \gamma_{[b}\widehat R(Q)_c{}^{d]}\big)\right|_{\epsilon^i}={}&-\frac{i}{4}T^{ab}\gamma^c\big(\overline{\widehat R(Q)}_c{}^{d}\gamma_{b}\widehat R(Q)_{ad}\big)\epsilon^i\\
&-\frac{i}{4}T^{ab}\gamma^c\big(\overline{\widehat R(Q)}_c{}^{d}\gamma_{b}\gamma_p\widehat R(Q)_{ad}\big)\gamma^p\epsilon^i\\
&+\frac{i}{8}T^{ab}\gamma^c\big(\overline{\widehat R(Q)}_c{}^{d}\gamma_{b}\gamma_{pq}\widehat R(Q)_{ad}\big)\gamma^{pq}\epsilon^i\\
&+\frac{i}{4}T^{ab}\gamma^c\big(\overline{\widehat R(Q)}_c{}^{b}\gamma_{d}\widehat R(Q)_{ad}\big)\epsilon^i\\
&+\frac{i}{4}T^{ab}\gamma^c\big(\overline{\widehat R(Q)}_c{}^{b}\gamma_{d}\gamma_p\widehat R(Q)_{ad}\big)\gamma^p\epsilon^i\\
&-\frac{i}{8}T^{ab}\gamma^c\big(\overline{\widehat R(Q)}_c{}^{b}\gamma_{d}\gamma_{pq}\widehat R(Q)_{ad}\big)\gamma^{pq}\epsilon^i
\end{aligned}\tag{H127}
```

```math
\begin{aligned}
\left.-2iT^{ab}\gamma^c\widehat R(Q)_{ad}{}^i\big(\bar\epsilon \gamma_c\widehat R(Q)_b{}^d\big)\right|_{\epsilon^i}={}&-\frac{i}{4}T^{ab}\gamma^c\big(\overline{\widehat R(Q)}_b{}^d\gamma_c\widehat R(Q)_{ad}\big)\epsilon^i\\
&-\frac{i}{4}T^{ab}\gamma^c\big(\overline{\widehat R(Q)}_b{}^d\gamma_c\gamma_p\widehat R(Q)_{ad}\big)\gamma^p\epsilon^i\\
&+\frac{i}{8}T^{ab}\gamma^c\big(\overline{\widehat R(Q)}_b{}^d\gamma_c\gamma_{pq}\widehat R(Q)_{ad}\big)\gamma^{pq}\epsilon^i
\end{aligned}\tag{H128}
```

```math
\begin{aligned}
\left.-32i\eta_{c[b}T^{ab}\gamma^c\widehat R(Q)_{ad}{}^i\big(\bar\epsilon \gamma^{d]}\chi\big)\right|_{\epsilon^i}={}&-2i\eta_{cb}T^{ab}\gamma^c\big(\bar\chi\gamma^{d}\widehat R(Q)_{ad}\big)\epsilon^i\\
&-2i\eta_{cb}T^{ab}\gamma^c\big(\bar\chi\gamma^{d}\gamma_p\widehat R(Q)_{ad}\big)\gamma^p\epsilon^i\\
&+i\eta_{cb}T^{ab}\gamma^c\big(\bar\chi\gamma^{d}\gamma_{pq}\widehat R(Q)_{ad}\big)\gamma^{pq}\epsilon^i\\
&+2i\eta_{cd}T^{ab}\gamma^c\big(\bar\chi\gamma^{b}\widehat R(Q)_{ad}\big)\epsilon^i\\
&+2i\eta_{cd}T^{ab}\gamma^c\big(\bar\chi\gamma^{b}\gamma_p\widehat R(Q)_{ad}\big)\gamma^p\epsilon^i\\
&-i\eta_{cd}T^{ab}\gamma^c\big(\bar\chi\gamma^{b}\gamma_{pq}\widehat R(Q)_{ad}\big)\gamma^{pq}\epsilon^i
\end{aligned}\tag{H129}
```

### 27.11 Retained term 5: varying the spinor derivative

First insert the differentiated Q-law and the dependent S-connection contribution. Distribute every coefficient and both differentiated $`T`$ factors:

```math
\begin{aligned}
&2iT^{ab}\eta^{cd}\gamma_a(\mathcal D_d\widehat C_{bc}{}^{ef})\gamma_{ef}\epsilon^i\\
&-16T^{ab}\eta^{cd}\gamma_a\gamma^{ef}(\mathcal D_d\mathcal D_{[b}T_{ef})\gamma_{c]}\epsilon^i\\
&+\frac{16}{3}T^{ab}\eta^{cd}\gamma_a\gamma_{[c}\gamma^{ef}(\mathcal D_d\mathcal D_{b]}T_{ef})\epsilon^i\\
&+\frac{16}{3}T^{ab}\eta^{cd}\gamma_a\gamma_{[b}\gamma^g\gamma^{ef}(\mathcal D_d\mathcal D_gT_{ef})\gamma_{c]}\epsilon^i\\
&+\frac{16}{3}T^{ab}\eta^{cd}\gamma_a\gamma_{bc}\gamma_e\mathcal D_d\mathcal D_fT^{fe}\epsilon^i\\
&+2T^{ab}\eta^{cd}\gamma_a\widehat C_{bc}{}^{ef}\gamma_{ef}(\gamma\!\cdot\!T)\gamma_d\epsilon^i\\
&+16iT^{ab}\eta^{cd}\gamma_a\gamma^{ef}(\mathcal D_{[b}T_{ef})\gamma_{c]}(\gamma\!\cdot\!T)\gamma_d\epsilon^i\\
&-\frac{16i}{3}T^{ab}\eta^{cd}\gamma_a\gamma_{[c}\gamma^{ef}(\mathcal D_{b]}T_{ef})(\gamma\!\cdot\!T)\gamma_d\epsilon^i\\
&-\frac{16i}{3}T^{ab}\eta^{cd}\gamma_a\gamma_{[b}\gamma^g\gamma^{ef}(\mathcal D_gT_{ef})\gamma_{c]}(\gamma\!\cdot\!T)\gamma_d\epsilon^i\\
&-\frac{16i}{3}T^{ab}\eta^{cd}\gamma_a\gamma_{bc}\gamma_e(\mathcal D_fT^{fe})(\gamma\!\cdot\!T)\gamma_d\epsilon^i\\
&+\frac{64i}{3}T^{ab}\eta^{cd}\gamma_aT_{bc}\gamma^t\gamma^{rs}(\mathcal D_tT_{rs})\gamma_d\epsilon^i\\
&-\frac{64i}{3}T^{ab}\eta^{cd}\gamma_aT_{bc}\gamma^{rs}(\mathcal D_dT_{rs})\epsilon^i\\
&+\frac{64i}{3}T^{ab}\eta^{cd}\gamma_aT_{bc}\gamma_d\gamma^s(\mathcal D^rT_{rs})\epsilon^i\\
&+64T^{ab}\eta^{cd}\gamma_aT_{bc}\gamma_{drstu}T^{rs}T^{tu}\epsilon^i\\
&-512T^{ab}\eta^{cd}\gamma_aT_{bc}\gamma_rT^{rs}T_{ds}\epsilon^i\\
&+128T^{ab}\eta^{cd}\gamma_aT_{bc}\gamma_dT^2\epsilon^i\\
&-\frac{128i}{9}T^{ab}\eta^{cd}\gamma_aT_{[b}{}^e\gamma_{c]e}\gamma^t\gamma^{rs}(\mathcal D_tT_{rs})\gamma_d\epsilon^i\\
&+\frac{128i}{9}T^{ab}\eta^{cd}\gamma_aT_{[b}{}^e\gamma_{c]e}\gamma^{rs}(\mathcal D_dT_{rs})\epsilon^i\\
&-\frac{128i}{9}T^{ab}\eta^{cd}\gamma_aT_{[b}{}^e\gamma_{c]e}\gamma_d\gamma^s(\mathcal D^rT_{rs})\epsilon^i\\
&-\frac{128}{3}T^{ab}\eta^{cd}\gamma_aT_{[b}{}^e\gamma_{c]e}\gamma_{drstu}T^{rs}T^{tu}\epsilon^i\\
&+\frac{1024}{3}T^{ab}\eta^{cd}\gamma_aT_{[b}{}^e\gamma_{c]e}\gamma_rT^{rs}T_{ds}\epsilon^i\\
&-\frac{256}{3}T^{ab}\eta^{cd}\gamma_aT_{[b}{}^e\gamma_{c]e}\gamma_dT^2\epsilon^i\\
&-\frac{32i}{9}T^{ab}\eta^{cd}\gamma_a\gamma_{bcef}T^{ef}\gamma^t\gamma^{rs}(\mathcal D_tT_{rs})\gamma_d\epsilon^i\\
&+\frac{32i}{9}T^{ab}\eta^{cd}\gamma_a\gamma_{bcef}T^{ef}\gamma^{rs}(\mathcal D_dT_{rs})\epsilon^i\\
&-\frac{32i}{9}T^{ab}\eta^{cd}\gamma_a\gamma_{bcef}T^{ef}\gamma_d\gamma^s(\mathcal D^rT_{rs})\epsilon^i\\
&-\frac{32}{3}T^{ab}\eta^{cd}\gamma_a\gamma_{bcef}T^{ef}\gamma_{drstu}T^{rs}T^{tu}\epsilon^i\\
&+\frac{256}{3}T^{ab}\eta^{cd}\gamma_a\gamma_{bcef}T^{ef}\gamma_rT^{rs}T_{ds}\epsilon^i\\
&-\frac{64}{3}T^{ab}\eta^{cd}\gamma_a\gamma_{bcef}T^{ef}\gamma_dT^2\epsilon^i
\end{aligned}\tag{H130}
```

Next insert the weight, spin, SU(2), and (for the gravitino curvature) tensor-index connection variations. The SU(2) connection uses H08; the other lines use H05.

```math
\begin{aligned}
\left.24iT^{ab}\eta^{cd}\gamma_a\widehat R(Q)_{bc}{}^i\big(\bar\epsilon \gamma_d\chi\big)\right|_{\epsilon^i}={}&3iT^{ab}\eta^{cd}\gamma_a\big(\bar\chi\gamma_d\widehat R(Q)_{bc}\big)\epsilon^i\\
&+3iT^{ab}\eta^{cd}\gamma_a\big(\bar\chi\gamma_d\gamma_p\widehat R(Q)_{bc}\big)\gamma^p\epsilon^i\\
&-\frac{3i}{2}T^{ab}\eta^{cd}\gamma_a\big(\bar\chi\gamma_d\gamma_{pq}\widehat R(Q)_{bc}\big)\gamma^{pq}\epsilon^i
\end{aligned}\tag{H131}
```

```math
\begin{aligned}
\left.-iT^{ab}\eta^{cd}\gamma_a\gamma_{ef}\widehat R(Q)_{bc}{}^i\big(\bar\epsilon \gamma^{[e}\widehat R(Q)_d{}^{f]}\big)\right|_{\epsilon^i}={}&-\frac{i}{16}T^{ab}\eta^{cd}\gamma_a\gamma_{ef}\big(\overline{\widehat R(Q)}_d{}^{f}\gamma^{e}\widehat R(Q)_{bc}\big)\epsilon^i\\
&-\frac{i}{16}T^{ab}\eta^{cd}\gamma_a\gamma_{ef}\big(\overline{\widehat R(Q)}_d{}^{f}\gamma^{e}\gamma_p\widehat R(Q)_{bc}\big)\gamma^p\epsilon^i\\
&+\frac{i}{32}T^{ab}\eta^{cd}\gamma_a\gamma_{ef}\big(\overline{\widehat R(Q)}_d{}^{f}\gamma^{e}\gamma_{pq}\widehat R(Q)_{bc}\big)\gamma^{pq}\epsilon^i\\
&+\frac{i}{16}T^{ab}\eta^{cd}\gamma_a\gamma_{ef}\big(\overline{\widehat R(Q)}_d{}^{e}\gamma^{f}\widehat R(Q)_{bc}\big)\epsilon^i\\
&+\frac{i}{16}T^{ab}\eta^{cd}\gamma_a\gamma_{ef}\big(\overline{\widehat R(Q)}_d{}^{e}\gamma^{f}\gamma_p\widehat R(Q)_{bc}\big)\gamma^p\epsilon^i\\
&-\frac{i}{32}T^{ab}\eta^{cd}\gamma_a\gamma_{ef}\big(\overline{\widehat R(Q)}_d{}^{e}\gamma^{f}\gamma_{pq}\widehat R(Q)_{bc}\big)\gamma^{pq}\epsilon^i
\end{aligned}\tag{H132}
```

```math
\begin{aligned}
\left.-\frac{i}{2}T^{ab}\eta^{cd}\gamma_a\gamma_{ef}\widehat R(Q)_{bc}{}^i\big(\bar\epsilon \gamma_d\widehat R(Q)^{ef}\big)\right|_{\epsilon^i}={}&-\frac{i}{16}T^{ab}\eta^{cd}\gamma_a\gamma_{ef}\big(\overline{\widehat R(Q)}^{ef}\gamma_d\widehat R(Q)_{bc}\big)\epsilon^i\\
&-\frac{i}{16}T^{ab}\eta^{cd}\gamma_a\gamma_{ef}\big(\overline{\widehat R(Q)}^{ef}\gamma_d\gamma_p\widehat R(Q)_{bc}\big)\gamma^p\epsilon^i\\
&+\frac{i}{32}T^{ab}\eta^{cd}\gamma_a\gamma_{ef}\big(\overline{\widehat R(Q)}^{ef}\gamma_d\gamma_{pq}\widehat R(Q)_{bc}\big)\gamma^{pq}\epsilon^i
\end{aligned}\tag{H133}
```

```math
\begin{aligned}
\left.-8i\delta_d{}^{[e}T^{ab}\eta^{cd}\gamma_a\gamma_{ef}\widehat R(Q)_{bc}{}^i\big(\bar\epsilon \gamma^{f]}\chi\big)\right|_{\epsilon^i}={}&-\frac{i}{2}\delta_d{}^{e}T^{ab}\eta^{cd}\gamma_a\gamma_{ef}\big(\bar\chi\gamma^{f}\widehat R(Q)_{bc}\big)\epsilon^i\\
&-\frac{i}{2}\delta_d{}^{e}T^{ab}\eta^{cd}\gamma_a\gamma_{ef}\big(\bar\chi\gamma^{f}\gamma_p\widehat R(Q)_{bc}\big)\gamma^p\epsilon^i\\
&+\frac{i}{4}\delta_d{}^{e}T^{ab}\eta^{cd}\gamma_a\gamma_{ef}\big(\bar\chi\gamma^{f}\gamma_{pq}\widehat R(Q)_{bc}\big)\gamma^{pq}\epsilon^i\\
&+\frac{i}{2}\delta_d{}^{f}T^{ab}\eta^{cd}\gamma_a\gamma_{ef}\big(\bar\chi\gamma^{e}\widehat R(Q)_{bc}\big)\epsilon^i\\
&+\frac{i}{2}\delta_d{}^{f}T^{ab}\eta^{cd}\gamma_a\gamma_{ef}\big(\bar\chi\gamma^{e}\gamma_p\widehat R(Q)_{bc}\big)\gamma^p\epsilon^i\\
&-\frac{i}{4}\delta_d{}^{f}T^{ab}\eta^{cd}\gamma_a\gamma_{ef}\big(\bar\chi\gamma^{e}\gamma_{pq}\widehat R(Q)_{bc}\big)\gamma^{pq}\epsilon^i
\end{aligned}\tag{H134}
```

```math
\begin{aligned}
\left.32iT^{ab}\eta^{cd}\gamma_a\bar\epsilon^{(i}\gamma_d\chi^{k)}\varepsilon_{kl}\widehat R(Q)_{bc}{}^l\right|_{\epsilon^i}={}&6iT^{ab}\eta^{cd}\gamma_a\big(\bar\chi\gamma_d\widehat R(Q)_{bc}\big)\epsilon^i\\
&+6iT^{ab}\eta^{cd}\gamma_a\big(\bar\chi\gamma_d\gamma_p\widehat R(Q)_{bc}\big)\gamma^p\epsilon^i\\
&-3iT^{ab}\eta^{cd}\gamma_a\big(\bar\chi\gamma_d\gamma_{pq}\widehat R(Q)_{bc}\big)\gamma^{pq}\epsilon^i
\end{aligned}\tag{H135}
```

```math
\begin{aligned}
\left.-4iT^{ab}\eta^{cd}\gamma_a\widehat R(Q)_{ec}{}^i\big(\bar\epsilon \gamma_{[b}\widehat R(Q)_d{}^{e]}\big)\right|_{\epsilon^i}={}&-\frac{i}{4}T^{ab}\eta^{cd}\gamma_a\big(\overline{\widehat R(Q)}_d{}^{e}\gamma_{b}\widehat R(Q)_{ec}\big)\epsilon^i\\
&-\frac{i}{4}T^{ab}\eta^{cd}\gamma_a\big(\overline{\widehat R(Q)}_d{}^{e}\gamma_{b}\gamma_p\widehat R(Q)_{ec}\big)\gamma^p\epsilon^i\\
&+\frac{i}{8}T^{ab}\eta^{cd}\gamma_a\big(\overline{\widehat R(Q)}_d{}^{e}\gamma_{b}\gamma_{pq}\widehat R(Q)_{ec}\big)\gamma^{pq}\epsilon^i\\
&+\frac{i}{4}T^{ab}\eta^{cd}\gamma_a\big(\overline{\widehat R(Q)}_d{}^{b}\gamma_{e}\widehat R(Q)_{ec}\big)\epsilon^i\\
&+\frac{i}{4}T^{ab}\eta^{cd}\gamma_a\big(\overline{\widehat R(Q)}_d{}^{b}\gamma_{e}\gamma_p\widehat R(Q)_{ec}\big)\gamma^p\epsilon^i\\
&-\frac{i}{8}T^{ab}\eta^{cd}\gamma_a\big(\overline{\widehat R(Q)}_d{}^{b}\gamma_{e}\gamma_{pq}\widehat R(Q)_{ec}\big)\gamma^{pq}\epsilon^i
\end{aligned}\tag{H136}
```

```math
\begin{aligned}
\left.-2iT^{ab}\eta^{cd}\gamma_a\widehat R(Q)_{ec}{}^i\big(\bar\epsilon \gamma_d\widehat R(Q)_b{}^e\big)\right|_{\epsilon^i}={}&-\frac{i}{4}T^{ab}\eta^{cd}\gamma_a\big(\overline{\widehat R(Q)}_b{}^e\gamma_d\widehat R(Q)_{ec}\big)\epsilon^i\\
&-\frac{i}{4}T^{ab}\eta^{cd}\gamma_a\big(\overline{\widehat R(Q)}_b{}^e\gamma_d\gamma_p\widehat R(Q)_{ec}\big)\gamma^p\epsilon^i\\
&+\frac{i}{8}T^{ab}\eta^{cd}\gamma_a\big(\overline{\widehat R(Q)}_b{}^e\gamma_d\gamma_{pq}\widehat R(Q)_{ec}\big)\gamma^{pq}\epsilon^i
\end{aligned}\tag{H137}
```

```math
\begin{aligned}
\left.-32i\eta_{d[b}T^{ab}\eta^{cd}\gamma_a\widehat R(Q)_{ec}{}^i\big(\bar\epsilon \gamma^{e]}\chi\big)\right|_{\epsilon^i}={}&-2i\eta_{db}T^{ab}\eta^{cd}\gamma_a\big(\bar\chi\gamma^{e}\widehat R(Q)_{ec}\big)\epsilon^i\\
&-2i\eta_{db}T^{ab}\eta^{cd}\gamma_a\big(\bar\chi\gamma^{e}\gamma_p\widehat R(Q)_{ec}\big)\gamma^p\epsilon^i\\
&+i\eta_{db}T^{ab}\eta^{cd}\gamma_a\big(\bar\chi\gamma^{e}\gamma_{pq}\widehat R(Q)_{ec}\big)\gamma^{pq}\epsilon^i\\
&+2i\eta_{de}T^{ab}\eta^{cd}\gamma_a\big(\bar\chi\gamma^{b}\widehat R(Q)_{ec}\big)\epsilon^i\\
&+2i\eta_{de}T^{ab}\eta^{cd}\gamma_a\big(\bar\chi\gamma^{b}\gamma_p\widehat R(Q)_{ec}\big)\gamma^p\epsilon^i\\
&-i\eta_{de}T^{ab}\eta^{cd}\gamma_a\big(\bar\chi\gamma^{b}\gamma_{pq}\widehat R(Q)_{ec}\big)\gamma^{pq}\epsilon^i
\end{aligned}\tag{H138}
```

```math
\begin{aligned}
\left.-4iT^{ab}\eta^{cd}\gamma_a\widehat R(Q)_{be}{}^i\big(\bar\epsilon \gamma_{[c}\widehat R(Q)_d{}^{e]}\big)\right|_{\epsilon^i}={}&-\frac{i}{4}T^{ab}\eta^{cd}\gamma_a\big(\overline{\widehat R(Q)}_d{}^{e}\gamma_{c}\widehat R(Q)_{be}\big)\epsilon^i\\
&-\frac{i}{4}T^{ab}\eta^{cd}\gamma_a\big(\overline{\widehat R(Q)}_d{}^{e}\gamma_{c}\gamma_p\widehat R(Q)_{be}\big)\gamma^p\epsilon^i\\
&+\frac{i}{8}T^{ab}\eta^{cd}\gamma_a\big(\overline{\widehat R(Q)}_d{}^{e}\gamma_{c}\gamma_{pq}\widehat R(Q)_{be}\big)\gamma^{pq}\epsilon^i\\
&+\frac{i}{4}T^{ab}\eta^{cd}\gamma_a\big(\overline{\widehat R(Q)}_d{}^{c}\gamma_{e}\widehat R(Q)_{be}\big)\epsilon^i\\
&+\frac{i}{4}T^{ab}\eta^{cd}\gamma_a\big(\overline{\widehat R(Q)}_d{}^{c}\gamma_{e}\gamma_p\widehat R(Q)_{be}\big)\gamma^p\epsilon^i\\
&-\frac{i}{8}T^{ab}\eta^{cd}\gamma_a\big(\overline{\widehat R(Q)}_d{}^{c}\gamma_{e}\gamma_{pq}\widehat R(Q)_{be}\big)\gamma^{pq}\epsilon^i
\end{aligned}\tag{H139}
```

```math
\begin{aligned}
\left.-2iT^{ab}\eta^{cd}\gamma_a\widehat R(Q)_{be}{}^i\big(\bar\epsilon \gamma_d\widehat R(Q)_c{}^e\big)\right|_{\epsilon^i}={}&-\frac{i}{4}T^{ab}\eta^{cd}\gamma_a\big(\overline{\widehat R(Q)}_c{}^e\gamma_d\widehat R(Q)_{be}\big)\epsilon^i\\
&-\frac{i}{4}T^{ab}\eta^{cd}\gamma_a\big(\overline{\widehat R(Q)}_c{}^e\gamma_d\gamma_p\widehat R(Q)_{be}\big)\gamma^p\epsilon^i\\
&+\frac{i}{8}T^{ab}\eta^{cd}\gamma_a\big(\overline{\widehat R(Q)}_c{}^e\gamma_d\gamma_{pq}\widehat R(Q)_{be}\big)\gamma^{pq}\epsilon^i
\end{aligned}\tag{H140}
```

```math
\begin{aligned}
\left.-32i\eta_{d[c}T^{ab}\eta^{cd}\gamma_a\widehat R(Q)_{be}{}^i\big(\bar\epsilon \gamma^{e]}\chi\big)\right|_{\epsilon^i}={}&-2i\eta_{dc}T^{ab}\eta^{cd}\gamma_a\big(\bar\chi\gamma^{e}\widehat R(Q)_{be}\big)\epsilon^i\\
&-2i\eta_{dc}T^{ab}\eta^{cd}\gamma_a\big(\bar\chi\gamma^{e}\gamma_p\widehat R(Q)_{be}\big)\gamma^p\epsilon^i\\
&+i\eta_{dc}T^{ab}\eta^{cd}\gamma_a\big(\bar\chi\gamma^{e}\gamma_{pq}\widehat R(Q)_{be}\big)\gamma^{pq}\epsilon^i\\
&+2i\eta_{de}T^{ab}\eta^{cd}\gamma_a\big(\bar\chi\gamma^{c}\widehat R(Q)_{be}\big)\epsilon^i\\
&+2i\eta_{de}T^{ab}\eta^{cd}\gamma_a\big(\bar\chi\gamma^{c}\gamma_p\widehat R(Q)_{be}\big)\gamma^p\epsilon^i\\
&-i\eta_{de}T^{ab}\eta^{cd}\gamma_a\big(\bar\chi\gamma^{c}\gamma_{pq}\widehat R(Q)_{be}\big)\gamma^{pq}\epsilon^i
\end{aligned}\tag{H141}
```

### 27.12 Retained term 8: varying the spinor derivative

First insert the differentiated Q-law and the dependent S-connection contribution. Distribute every coefficient and both differentiated $`T`$ factors:

```math
\begin{aligned}
&\frac{32i}{3}T^{ab}\gamma_a\mathcal D_bD\epsilon^i\\
&-\frac{16}{3}T^{ab}\gamma_a\gamma^{de}\gamma^f\mathcal D_b\mathcal D_fT_{de}\epsilon^i\\
&+\frac{16}{3}T^{ab}\gamma_a\gamma^d\mathcal D_b\mathcal D^eT_{de}\epsilon^i\\
&-\frac{32i}{3}T^{ab}\gamma_a\gamma^{defg}(\mathcal D_bT_{de})T_{fg}\epsilon^i\\
&-\frac{32i}{3}T^{ab}\gamma_a\gamma^{defg}T_{de}(\mathcal D_bT_{fg})\epsilon^i\\
&+\frac{128i}{9}T^{ab}\gamma_aT^{de}\mathcal D_bT_{de}\epsilon^i\\
&+\frac{32}{3}T^{ab}\gamma_aD(\gamma\!\cdot\!T)\gamma_b\epsilon^i\\
&+\frac{16i}{3}T^{ab}\gamma_a\gamma^{de}\gamma^f(\mathcal D_fT_{de})(\gamma\!\cdot\!T)\gamma_b\epsilon^i\\
&-\frac{16i}{3}T^{ab}\gamma_a\gamma^d(\mathcal D^eT_{de})(\gamma\!\cdot\!T)\gamma_b\epsilon^i\\
&-\frac{32}{3}T^{ab}\gamma_a\gamma^{defg}T_{de}T_{fg}(\gamma\!\cdot\!T)\gamma_b\epsilon^i\\
&+\frac{64}{9}T^{ab}\gamma_aT^2(\gamma\!\cdot\!T)\gamma_b\epsilon^i\\
&-\frac{32i}{9}T^{ab}\gamma_a(\gamma\!\cdot\!T)\gamma^f\gamma^{de}(\mathcal D_fT_{de})\gamma_b\epsilon^i\\
&+\frac{32i}{9}T^{ab}\gamma_a(\gamma\!\cdot\!T)\gamma^{de}(\mathcal D_bT_{de})\epsilon^i\\
&-\frac{32i}{9}T^{ab}\gamma_a(\gamma\!\cdot\!T)\gamma_b\gamma^e(\mathcal D^dT_{de})\epsilon^i\\
&-\frac{32}{3}T^{ab}\gamma_a(\gamma\!\cdot\!T)\gamma_{bdefg}T^{de}T^{fg}\epsilon^i\\
&+\frac{256}{3}T^{ab}\gamma_a(\gamma\!\cdot\!T)\gamma_dT^{de}T_{be}\epsilon^i\\
&-\frac{64}{3}T^{ab}\gamma_a(\gamma\!\cdot\!T)\gamma_bT^2\epsilon^i
\end{aligned}\tag{H142}
```

Next insert the weight, spin, SU(2), and (for the gravitino curvature) tensor-index connection variations. The SU(2) connection uses H08; the other lines use H05.

```math
\begin{aligned}
\left.128iT^{ab}\gamma_a\chi{}^i\big(\bar\epsilon \gamma_b\chi\big)\right|_{\epsilon^i}={}&16iT^{ab}\gamma_a\big(\bar\chi\gamma_b\chi\big)\epsilon^i\\
&+16iT^{ab}\gamma_a\big(\bar\chi\gamma_b\gamma_p\chi\big)\gamma^p\epsilon^i\\
&-8iT^{ab}\gamma_a\big(\bar\chi\gamma_b\gamma_{pq}\chi\big)\gamma^{pq}\epsilon^i
\end{aligned}\tag{H143}
```

```math
\begin{aligned}
\left.-\frac{16i}{3}T^{ab}\gamma_a\gamma_{de}\chi{}^i\big(\bar\epsilon \gamma^{[d}\widehat R(Q)_b{}^{e]}\big)\right|_{\epsilon^i}={}&-\frac{i}{3}T^{ab}\gamma_a\gamma_{de}\big(\overline{\widehat R(Q)}_b{}^{e}\gamma^{d}\chi\big)\epsilon^i\\
&-\frac{i}{3}T^{ab}\gamma_a\gamma_{de}\big(\overline{\widehat R(Q)}_b{}^{e}\gamma^{d}\gamma_p\chi\big)\gamma^p\epsilon^i\\
&+\frac{i}{6}T^{ab}\gamma_a\gamma_{de}\big(\overline{\widehat R(Q)}_b{}^{e}\gamma^{d}\gamma_{pq}\chi\big)\gamma^{pq}\epsilon^i\\
&+\frac{i}{3}T^{ab}\gamma_a\gamma_{de}\big(\overline{\widehat R(Q)}_b{}^{d}\gamma^{e}\chi\big)\epsilon^i\\
&+\frac{i}{3}T^{ab}\gamma_a\gamma_{de}\big(\overline{\widehat R(Q)}_b{}^{d}\gamma^{e}\gamma_p\chi\big)\gamma^p\epsilon^i\\
&-\frac{i}{6}T^{ab}\gamma_a\gamma_{de}\big(\overline{\widehat R(Q)}_b{}^{d}\gamma^{e}\gamma_{pq}\chi\big)\gamma^{pq}\epsilon^i
\end{aligned}\tag{H144}
```

```math
\begin{aligned}
\left.-\frac{8i}{3}T^{ab}\gamma_a\gamma_{de}\chi{}^i\big(\bar\epsilon \gamma_b\widehat R(Q)^{de}\big)\right|_{\epsilon^i}={}&-\frac{i}{3}T^{ab}\gamma_a\gamma_{de}\big(\overline{\widehat R(Q)}^{de}\gamma_b\chi\big)\epsilon^i\\
&-\frac{i}{3}T^{ab}\gamma_a\gamma_{de}\big(\overline{\widehat R(Q)}^{de}\gamma_b\gamma_p\chi\big)\gamma^p\epsilon^i\\
&+\frac{i}{6}T^{ab}\gamma_a\gamma_{de}\big(\overline{\widehat R(Q)}^{de}\gamma_b\gamma_{pq}\chi\big)\gamma^{pq}\epsilon^i
\end{aligned}\tag{H145}
```

```math
\begin{aligned}
\left.-\frac{128i}{3}\delta_b{}^{[d}T^{ab}\gamma_a\gamma_{de}\chi{}^i\big(\bar\epsilon \gamma^{e]}\chi\big)\right|_{\epsilon^i}={}&-\frac{8i}{3}\delta_b{}^{d}T^{ab}\gamma_a\gamma_{de}\big(\bar\chi\gamma^{e}\chi\big)\epsilon^i\\
&-\frac{8i}{3}\delta_b{}^{d}T^{ab}\gamma_a\gamma_{de}\big(\bar\chi\gamma^{e}\gamma_p\chi\big)\gamma^p\epsilon^i\\
&+\frac{4i}{3}\delta_b{}^{d}T^{ab}\gamma_a\gamma_{de}\big(\bar\chi\gamma^{e}\gamma_{pq}\chi\big)\gamma^{pq}\epsilon^i\\
&+\frac{8i}{3}\delta_b{}^{e}T^{ab}\gamma_a\gamma_{de}\big(\bar\chi\gamma^{d}\chi\big)\epsilon^i\\
&+\frac{8i}{3}\delta_b{}^{e}T^{ab}\gamma_a\gamma_{de}\big(\bar\chi\gamma^{d}\gamma_p\chi\big)\gamma^p\epsilon^i\\
&-\frac{4i}{3}\delta_b{}^{e}T^{ab}\gamma_a\gamma_{de}\big(\bar\chi\gamma^{d}\gamma_{pq}\chi\big)\gamma^{pq}\epsilon^i
\end{aligned}\tag{H146}
```

```math
\begin{aligned}
\left.\frac{512i}{3}T^{ab}\gamma_a\bar\epsilon^{(i}\gamma_b\chi^{k)}\varepsilon_{kl}\chi{}^l\right|_{\epsilon^i}={}&32iT^{ab}\gamma_a\big(\bar\chi\gamma_b\chi\big)\epsilon^i\\
&+32iT^{ab}\gamma_a\big(\bar\chi\gamma_b\gamma_p\chi\big)\gamma^p\epsilon^i\\
&-16iT^{ab}\gamma_a\big(\bar\chi\gamma_b\gamma_{pq}\chi\big)\gamma^{pq}\epsilon^i
\end{aligned}\tag{H147}
```

### 27.13 Consistency Checks

**SU(2) and Grassmann signs.** H68 lists every new transpose. H070–H147
show the actual physical spinor pairings, including all three Fierz
ranks for each application. The connection triplets were processed by
H08 before their trace was taken. All final terms have a single free
$`i`$ on $`\epsilon^i`$; contracted curvature doublets use other labels.
Every displayed bilinear is even; moving it across the exterior spinor
introduces no sign. The minus in the dyad completeness relation remains
in H02 and hence in H05/H08.

**Weights.** The first two retained terms contain
$`\widehat R(Q)`$ of weight $`3/2`$ times a Q coefficient of weight $`5/2`$;
the fifth has $`\chi`$ of weight $`3/2`$ times the same coefficient.
The other three contain $`T`$ of weight one times a spinor-derivative Q
coefficient of weight three. Thus all six final coefficients have weight
four; multiplying $`\epsilon`$ of weight $`-1/2`$ gives $`7/2`$.
For example $`T\,\bar\chi\widehat R(Q)`$, $`T\mathcal D\widehat C`$,
$`T\mathcal D\mathcal D T`$ and $`T^4`$ each have weight four.
No fermionic order has been removed by this check.

**Curvature and derivative bookkeeping.** H63–H65 retain the derivatives
of both fermionic connections, all thirteen terms after eliminating
$`\widehat R(S)`$, and the entire dependent Ricci contraction. H62 has
both Lorentz tensor connections. H66 has 17 parameter-right and five
fermion-product terms; H67b has 28 parameter-right and eleven
fermion-product terms. No derivative interchange or integration by parts
has been used. All equality signs are local, off-shell equalities for
the specified singlet, using the normal-frame argument H54–H55.

**Checks by independent finite matrices.** The verification script
`verify_weyl_h50_completion.py` tests the defining primed-curvature
calculation of H60 against its displayed six terms on all 50 independent
$`\mathcal D T`$ jets and all 55 basis/polarization configurations of $`T`$.
It separately tests the three products H59a, the additional transpose
identities, the rational Fierz multipliers and the full final addition.
As a cross-check of the normal-frame calculation, it also inserts H57
and H60 into $`\delta\widehat R(Q)_{ab}=\delta\widehat R'(Q)_{ab} -2i\gamma_{[a}\delta\phi_{b]}`$: all 50 derivative jets reproduce
R05, and its $`T^2`$ contribution cancels on all 55 two-form tests.
The existing Clifford/Grassmann checker tests the complete 16-matrix
basis, including ordered odd-component monomials and the SU(2) Schouten
factor. These tests check the stated algebra; they are not a test of
multiplet closure or the later action.

**Simple limits.** With all fermionic covariants zero, every displayed
bilinear vanishes. The new derivative terms retain the bosonic covariant
coefficients in H66–H67b, as a Q variation of a vanishing fermion should.
If in addition $`T=\widehat C=\widehat R(V)=0`$, derivatives vanish, and
$`D`$ is arbitrary at the point, the sum reduces to
$`(128/3)(D/4)D\epsilon^i=(32/3)D^2\epsilon^i`$.
Setting $`D=0`$ as well gives zero. The independent $`\widehat C^2`$ and
$`\widehat R(V)^2`$ reductions remain H49 and H48. Their scalar coefficients
are $`1/16`$ and $`-1/6`$, respectively.

## 28. Final Result: Add All Eleven Terms

All six terms in H50 now have parameter-right physical-field expressions.
The accounting of original product-rule origins is

```math
\boxed{94=66\text{ earlier evaluated origins}
+6\text{ origins evaluated above}+22\text{ zero SU(2)-trace origins}.}
\tag{H53}
```

The full sum follows. It includes the earlier H15–H45 contributions and
all six new contributions, with literally identical expressions added.
The long right-hand side is split across consecutive displays for
readability; a leading plus continues the **same sum**. There is no
unevaluated variation, response field, Fierz operation or substitution
instruction in this sum. Gamma products retain their displayed order;
this is the complete epsilon-right singlet, before optional further
Clifford reduction to minimal scalar/vector/bivector coefficients.

```math
\begin{aligned}
\left.\delta_Q\varphi_W^i\right|_{\epsilon^i}={}&-\frac{1}{32}\gamma_{cd} \gamma_{ef}\widehat C_{ab}{}^{ef}\widehat C^{abcd}\epsilon^i\\
&-\frac{i}{4}\gamma_{cd} \gamma^{ef} \gamma_{b]}(\mathcal D_{[a}T_{ef})\widehat C^{abcd}\epsilon^i\\
&+\frac{i}{12}\gamma_{cd} \gamma_{[b} \gamma^{ef}(\mathcal D_{a]}T_{ef})\widehat C^{abcd}\epsilon^i\\
&+\frac{i}{12}\gamma_{cd} \gamma_{[a} \gamma^{g} \gamma^{ef} \gamma_{b]}(\mathcal D_gT_{ef})\widehat C^{abcd}\epsilon^i\\
&+\frac{i}{12}\gamma_{cd} \gamma_{ab} \gamma^{e}(\mathcal D^fT_{fe})\widehat C^{abcd}\epsilon^i\\
&+\frac{1}{128}\gamma^{cd}\big(\overline{\mathcal D_e\widehat R(Q)_{ab}}\gamma^e\gamma_{cd}\widehat R(Q)^{ab}\big)\epsilon^i\\
&+\frac{1}{128}\gamma^{cd}\big(\overline{\mathcal D_e\widehat R(Q)_{ab}}\gamma^e\gamma_{cd}\gamma_p\widehat R(Q)^{ab}\big)\gamma^p\epsilon^i\\
&-\frac{1}{256}\gamma^{cd}\big(\overline{\mathcal D_e\widehat R(Q)_{ab}}\gamma^e\gamma_{cd}\gamma_{pq}\widehat R(Q)^{ab}\big)\gamma^{pq}\epsilon^i\\
&+\frac{1}{256}\gamma^{cd}\big(\overline{\mathcal D^e\widehat R(Q)_{be}}\gamma_{a}\gamma_{cd}\widehat R(Q)^{ab}\big)\epsilon^i\\
&+\frac{1}{256}\gamma^{cd}\big(\overline{\mathcal D^e\widehat R(Q)_{be}}\gamma_{a}\gamma_{cd}\gamma_p\widehat R(Q)^{ab}\big)\gamma^p\epsilon^i\\
&-\frac{1}{512}\gamma^{cd}\big(\overline{\mathcal D^e\widehat R(Q)_{be}}\gamma_{a}\gamma_{cd}\gamma_{pq}\widehat R(Q)^{ab}\big)\gamma^{pq}\epsilon^i\\
&-\frac{1}{256}\gamma^{cd}\big(\overline{\mathcal D^e\widehat R(Q)_{ae}}\gamma_{b}\gamma_{cd}\widehat R(Q)^{ab}\big)\epsilon^i\\
&-\frac{1}{256}\gamma^{cd}\big(\overline{\mathcal D^e\widehat R(Q)_{ae}}\gamma_{b}\gamma_{cd}\gamma_p\widehat R(Q)^{ab}\big)\gamma^p\epsilon^i\\
&+\frac{1}{512}\gamma^{cd}\big(\overline{\mathcal D^e\widehat R(Q)_{ae}}\gamma_{b}\gamma_{cd}\gamma_{pq}\widehat R(Q)^{ab}\big)\gamma^{pq}\epsilon^i\\
&+\frac{i}{48}T^{ef}\gamma^{cd}\big(\overline{\widehat R(Q)}_{ef}\gamma_{ab}\gamma_{cd}\widehat R(Q)^{ab}\big)\epsilon^i\\
&+\frac{i}{48}T^{ef}\gamma^{cd}\big(\overline{\widehat R(Q)}_{ef}\gamma_{ab}\gamma_{cd}\gamma_p\widehat R(Q)^{ab}\big)\gamma^p\epsilon^i\\
&-\frac{i}{96}T^{ef}\gamma^{cd}\big(\overline{\widehat R(Q)}_{ef}\gamma_{ab}\gamma_{cd}\gamma_{pq}\widehat R(Q)^{ab}\big)\gamma^{pq}\epsilon^i\\
&+\frac{3i}{64}T^{ef}\gamma^{cd}\big(\overline{\widehat R(Q)}_{be}\gamma_{a}\gamma_f\gamma_{cd}\widehat R(Q)^{ab}\big)\epsilon^i
\end{aligned}\tag{H150}
```

Continuation of the same right-hand side:

```math
\begin{aligned}
&+\frac{3i}{64}T^{ef}\gamma^{cd}\big(\overline{\widehat R(Q)}_{be}\gamma_{a}\gamma_f\gamma_{cd}\gamma_p\widehat R(Q)^{ab}\big)\gamma^p\epsilon^i\\
&-\frac{3i}{128}T^{ef}\gamma^{cd}\big(\overline{\widehat R(Q)}_{be}\gamma_{a}\gamma_f\gamma_{cd}\gamma_{pq}\widehat R(Q)^{ab}\big)\gamma^{pq}\epsilon^i\\
&-\frac{3i}{64}T^{ef}\gamma^{cd}\big(\overline{\widehat R(Q)}_{ae}\gamma_{b}\gamma_f\gamma_{cd}\widehat R(Q)^{ab}\big)\epsilon^i\\
&-\frac{3i}{64}T^{ef}\gamma^{cd}\big(\overline{\widehat R(Q)}_{ae}\gamma_{b}\gamma_f\gamma_{cd}\gamma_p\widehat R(Q)^{ab}\big)\gamma^p\epsilon^i\\
&+\frac{3i}{128}T^{ef}\gamma^{cd}\big(\overline{\widehat R(Q)}_{ae}\gamma_{b}\gamma_f\gamma_{cd}\gamma_{pq}\widehat R(Q)^{ab}\big)\gamma^{pq}\epsilon^i\\
&+\frac{3i}{128}\gamma^{cd}\big(\overline{\widehat R(Q)}_{ab}(\gamma\!\cdot\!T)\gamma_{cd}\widehat R(Q)^{ab}\big)\epsilon^i\\
&+\frac{3i}{128}\gamma^{cd}\big(\overline{\widehat R(Q)}_{ab}(\gamma\!\cdot\!T)\gamma_{cd}\gamma_p\widehat R(Q)^{ab}\big)\gamma^p\epsilon^i\\
&-\frac{3i}{256}\gamma^{cd}\big(\overline{\widehat R(Q)}_{ab}(\gamma\!\cdot\!T)\gamma_{cd}\gamma_{pq}\widehat R(Q)^{ab}\big)\gamma^{pq}\epsilon^i\\
&-\frac{i}{32}T^e{}_{a}\gamma^{cd}\big(\overline{\widehat R(Q)}_{be}\gamma_{cd}\widehat R(Q)^{ab}\big)\epsilon^i\\
&-\frac{i}{32}T^e{}_{a}\gamma^{cd}\big(\overline{\widehat R(Q)}_{be}\gamma_{cd}\gamma_p\widehat R(Q)^{ab}\big)\gamma^p\epsilon^i\\
&+\frac{i}{64}T^e{}_{a}\gamma^{cd}\big(\overline{\widehat R(Q)}_{be}\gamma_{cd}\gamma_{pq}\widehat R(Q)^{ab}\big)\gamma^{pq}\epsilon^i\\
&+\frac{i}{32}T^e{}_{b}\gamma^{cd}\big(\overline{\widehat R(Q)}_{ae}\gamma_{cd}\widehat R(Q)^{ab}\big)\epsilon^i\\
&+\frac{i}{32}T^e{}_{b}\gamma^{cd}\big(\overline{\widehat R(Q)}_{ae}\gamma_{cd}\gamma_p\widehat R(Q)^{ab}\big)\gamma^p\epsilon^i\\
&-\frac{i}{64}T^e{}_{b}\gamma^{cd}\big(\overline{\widehat R(Q)}_{ae}\gamma_{cd}\gamma_{pq}\widehat R(Q)^{ab}\big)\gamma^{pq}\epsilon^i\\
&+\frac{i}{128}\gamma^{cd}\big(\overline{\widehat R(Q)}_{ab}\gamma_{c}(\gamma\!\cdot\!T)\gamma_{d}\widehat R(Q)^{ab}\big)\epsilon^i\\
&+\frac{i}{128}\gamma^{cd}\big(\overline{\widehat R(Q)}_{ab}\gamma_{c}(\gamma\!\cdot\!T)\gamma_{d}\gamma_p\widehat R(Q)^{ab}\big)\gamma^p\epsilon^i\\
&-\frac{i}{256}\gamma^{cd}\big(\overline{\widehat R(Q)}_{ab}\gamma_{c}(\gamma\!\cdot\!T)\gamma_{d}\gamma_{pq}\widehat R(Q)^{ab}\big)\gamma^{pq}\epsilon^i\\
&-\frac{i}{128}\gamma^{cd}\big(\overline{\widehat R(Q)}_{ab}\gamma_{d}(\gamma\!\cdot\!T)\gamma_{c}\widehat R(Q)^{ab}\big)\epsilon^i
\end{aligned}\tag{H151}
```

Continuation of the same right-hand side:

```math
\begin{aligned}
&-\frac{i}{128}\gamma^{cd}\big(\overline{\widehat R(Q)}_{ab}\gamma_{d}(\gamma\!\cdot\!T)\gamma_{c}\gamma_p\widehat R(Q)^{ab}\big)\gamma^p\epsilon^i\\
&+\frac{i}{256}\gamma^{cd}\big(\overline{\widehat R(Q)}_{ab}\gamma_{d}(\gamma\!\cdot\!T)\gamma_{c}\gamma_{pq}\widehat R(Q)^{ab}\big)\gamma^{pq}\epsilon^i\\
&+\frac{1}{256}\gamma^{cd}\big(\overline{\mathcal D_{a}\widehat R(Q)_{bd}}\gamma_{c}\widehat R(Q)^{ab}\big)\epsilon^i\\
&+\frac{1}{256}\gamma^{cd}\big(\overline{\mathcal D_{a}\widehat R(Q)_{bd}}\gamma_{c}\gamma_p\widehat R(Q)^{ab}\big)\gamma^p\epsilon^i\\
&-\frac{1}{512}\gamma^{cd}\big(\overline{\mathcal D_{a}\widehat R(Q)_{bd}}\gamma_{c}\gamma_{pq}\widehat R(Q)^{ab}\big)\gamma^{pq}\epsilon^i\\
&-\frac{1}{256}\gamma^{cd}\big(\overline{\mathcal D_{a}\widehat R(Q)_{bc}}\gamma_{d}\widehat R(Q)^{ab}\big)\epsilon^i\\
&-\frac{1}{256}\gamma^{cd}\big(\overline{\mathcal D_{a}\widehat R(Q)_{bc}}\gamma_{d}\gamma_p\widehat R(Q)^{ab}\big)\gamma^p\epsilon^i\\
&+\frac{1}{512}\gamma^{cd}\big(\overline{\mathcal D_{a}\widehat R(Q)_{bc}}\gamma_{d}\gamma_{pq}\widehat R(Q)^{ab}\big)\gamma^{pq}\epsilon^i\\
&-\frac{1}{256}\gamma^{cd}\big(\overline{\mathcal D_{b}\widehat R(Q)_{ad}}\gamma_{c}\widehat R(Q)^{ab}\big)\epsilon^i\\
&-\frac{1}{256}\gamma^{cd}\big(\overline{\mathcal D_{b}\widehat R(Q)_{ad}}\gamma_{c}\gamma_p\widehat R(Q)^{ab}\big)\gamma^p\epsilon^i\\
&+\frac{1}{512}\gamma^{cd}\big(\overline{\mathcal D_{b}\widehat R(Q)_{ad}}\gamma_{c}\gamma_{pq}\widehat R(Q)^{ab}\big)\gamma^{pq}\epsilon^i\\
&+\frac{1}{256}\gamma^{cd}\big(\overline{\mathcal D_{b}\widehat R(Q)_{ac}}\gamma_{d}\widehat R(Q)^{ab}\big)\epsilon^i\\
&+\frac{1}{256}\gamma^{cd}\big(\overline{\mathcal D_{b}\widehat R(Q)_{ac}}\gamma_{d}\gamma_p\widehat R(Q)^{ab}\big)\gamma^p\epsilon^i\\
&-\frac{1}{512}\gamma^{cd}\big(\overline{\mathcal D_{b}\widehat R(Q)_{ac}}\gamma_{d}\gamma_{pq}\widehat R(Q)^{ab}\big)\gamma^{pq}\epsilon^i\\
&-\frac{i}{256}\gamma^{cd}\big(\overline{\widehat R(Q)}_{bd}\gamma_{c}(\gamma\!\cdot\!T)\gamma_{a}\widehat R(Q)^{ab}\big)\epsilon^i\\
&-\frac{i}{256}\gamma^{cd}\big(\overline{\widehat R(Q)}_{bd}\gamma_{c}(\gamma\!\cdot\!T)\gamma_{a}\gamma_p\widehat R(Q)^{ab}\big)\gamma^p\epsilon^i\\
&+\frac{i}{512}\gamma^{cd}\big(\overline{\widehat R(Q)}_{bd}\gamma_{c}(\gamma\!\cdot\!T)\gamma_{a}\gamma_{pq}\widehat R(Q)^{ab}\big)\gamma^{pq}\epsilon^i\\
&+\frac{i}{256}\gamma^{cd}\big(\overline{\widehat R(Q)}_{bc}\gamma_{d}(\gamma\!\cdot\!T)\gamma_{a}\widehat R(Q)^{ab}\big)\epsilon^i
\end{aligned}\tag{H152}
```

Continuation of the same right-hand side:

```math
\begin{aligned}
&+\frac{i}{256}\gamma^{cd}\big(\overline{\widehat R(Q)}_{bc}\gamma_{d}(\gamma\!\cdot\!T)\gamma_{a}\gamma_p\widehat R(Q)^{ab}\big)\gamma^p\epsilon^i\\
&-\frac{i}{512}\gamma^{cd}\big(\overline{\widehat R(Q)}_{bc}\gamma_{d}(\gamma\!\cdot\!T)\gamma_{a}\gamma_{pq}\widehat R(Q)^{ab}\big)\gamma^{pq}\epsilon^i\\
&+\frac{i}{256}\gamma^{cd}\big(\overline{\widehat R(Q)}_{ad}\gamma_{c}(\gamma\!\cdot\!T)\gamma_{b}\widehat R(Q)^{ab}\big)\epsilon^i\\
&+\frac{i}{256}\gamma^{cd}\big(\overline{\widehat R(Q)}_{ad}\gamma_{c}(\gamma\!\cdot\!T)\gamma_{b}\gamma_p\widehat R(Q)^{ab}\big)\gamma^p\epsilon^i\\
&-\frac{i}{512}\gamma^{cd}\big(\overline{\widehat R(Q)}_{ad}\gamma_{c}(\gamma\!\cdot\!T)\gamma_{b}\gamma_{pq}\widehat R(Q)^{ab}\big)\gamma^{pq}\epsilon^i\\
&-\frac{i}{256}\gamma^{cd}\big(\overline{\widehat R(Q)}_{ac}\gamma_{d}(\gamma\!\cdot\!T)\gamma_{b}\widehat R(Q)^{ab}\big)\epsilon^i\\
&-\frac{i}{256}\gamma^{cd}\big(\overline{\widehat R(Q)}_{ac}\gamma_{d}(\gamma\!\cdot\!T)\gamma_{b}\gamma_p\widehat R(Q)^{ab}\big)\gamma^p\epsilon^i\\
&+\frac{i}{512}\gamma^{cd}\big(\overline{\widehat R(Q)}_{ac}\gamma_{d}(\gamma\!\cdot\!T)\gamma_{b}\gamma_{pq}\widehat R(Q)^{ab}\big)\gamma^{pq}\epsilon^i\\
&-\frac{1}{256}\gamma^{cd}\big(\overline{\mathcal D_{b}\widehat R(Q)_{cd}}\gamma_{a}\widehat R(Q)^{ab}\big)\epsilon^i\\
&-\frac{1}{256}\gamma^{cd}\big(\overline{\mathcal D_{b}\widehat R(Q)_{cd}}\gamma_{a}\gamma_p\widehat R(Q)^{ab}\big)\gamma^p\epsilon^i\\
&+\frac{1}{512}\gamma^{cd}\big(\overline{\mathcal D_{b}\widehat R(Q)_{cd}}\gamma_{a}\gamma_{pq}\widehat R(Q)^{ab}\big)\gamma^{pq}\epsilon^i\\
&+\frac{1}{256}\gamma^{cd}\big(\overline{\mathcal D_{a}\widehat R(Q)_{cd}}\gamma_{b}\widehat R(Q)^{ab}\big)\epsilon^i\\
&+\frac{1}{256}\gamma^{cd}\big(\overline{\mathcal D_{a}\widehat R(Q)_{cd}}\gamma_{b}\gamma_p\widehat R(Q)^{ab}\big)\gamma^p\epsilon^i\\
&-\frac{1}{512}\gamma^{cd}\big(\overline{\mathcal D_{a}\widehat R(Q)_{cd}}\gamma_{b}\gamma_{pq}\widehat R(Q)^{ab}\big)\gamma^{pq}\epsilon^i\\
&+\frac{i}{256}\gamma^{cd}\big(\overline{\widehat R(Q)}_{cd}\gamma_{a}(\gamma\!\cdot\!T)\gamma_{b}\widehat R(Q)^{ab}\big)\epsilon^i\\
&+\frac{i}{256}\gamma^{cd}\big(\overline{\widehat R(Q)}_{cd}\gamma_{a}(\gamma\!\cdot\!T)\gamma_{b}\gamma_p\widehat R(Q)^{ab}\big)\gamma^p\epsilon^i\\
&-\frac{i}{512}\gamma^{cd}\big(\overline{\widehat R(Q)}_{cd}\gamma_{a}(\gamma\!\cdot\!T)\gamma_{b}\gamma_{pq}\widehat R(Q)^{ab}\big)\gamma^{pq}\epsilon^i\\
&-\frac{i}{256}\gamma^{cd}\big(\overline{\widehat R(Q)}_{cd}\gamma_{b}(\gamma\!\cdot\!T)\gamma_{a}\widehat R(Q)^{ab}\big)\epsilon^i
\end{aligned}\tag{H153}
```

Continuation of the same right-hand side:

```math
\begin{aligned}
&-\frac{i}{256}\gamma^{cd}\big(\overline{\widehat R(Q)}_{cd}\gamma_{b}(\gamma\!\cdot\!T)\gamma_{a}\gamma_p\widehat R(Q)^{ab}\big)\gamma^p\epsilon^i\\
&+\frac{i}{512}\gamma^{cd}\big(\overline{\widehat R(Q)}_{cd}\gamma_{b}(\gamma\!\cdot\!T)\gamma_{a}\gamma_{pq}\widehat R(Q)^{ab}\big)\gamma^{pq}\epsilon^i\\
&+\frac{1}{32}\eta_{bc}\gamma^{cd}\big(\overline{\mathcal D_{a}\chi}\gamma_{d}\widehat R(Q)^{ab}\big)\epsilon^i\\
&+\frac{1}{32}\eta_{bc}\gamma^{cd}\big(\overline{\mathcal D_{a}\chi}\gamma_{d}\gamma_p\widehat R(Q)^{ab}\big)\gamma^p\epsilon^i\\
&-\frac{1}{64}\eta_{bc}\gamma^{cd}\big(\overline{\mathcal D_{a}\chi}\gamma_{d}\gamma_{pq}\widehat R(Q)^{ab}\big)\gamma^{pq}\epsilon^i\\
&-\frac{1}{32}\eta_{bd}\gamma^{cd}\big(\overline{\mathcal D_{a}\chi}\gamma_{c}\widehat R(Q)^{ab}\big)\epsilon^i\\
&-\frac{1}{32}\eta_{bd}\gamma^{cd}\big(\overline{\mathcal D_{a}\chi}\gamma_{c}\gamma_p\widehat R(Q)^{ab}\big)\gamma^p\epsilon^i\\
&+\frac{1}{64}\eta_{bd}\gamma^{cd}\big(\overline{\mathcal D_{a}\chi}\gamma_{c}\gamma_{pq}\widehat R(Q)^{ab}\big)\gamma^{pq}\epsilon^i\\
&-\frac{1}{32}\eta_{ac}\gamma^{cd}\big(\overline{\mathcal D_{b}\chi}\gamma_{d}\widehat R(Q)^{ab}\big)\epsilon^i\\
&-\frac{1}{32}\eta_{ac}\gamma^{cd}\big(\overline{\mathcal D_{b}\chi}\gamma_{d}\gamma_p\widehat R(Q)^{ab}\big)\gamma^p\epsilon^i\\
&+\frac{1}{64}\eta_{ac}\gamma^{cd}\big(\overline{\mathcal D_{b}\chi}\gamma_{d}\gamma_{pq}\widehat R(Q)^{ab}\big)\gamma^{pq}\epsilon^i\\
&+\frac{1}{32}\eta_{ad}\gamma^{cd}\big(\overline{\mathcal D_{b}\chi}\gamma_{c}\widehat R(Q)^{ab}\big)\epsilon^i\\
&+\frac{1}{32}\eta_{ad}\gamma^{cd}\big(\overline{\mathcal D_{b}\chi}\gamma_{c}\gamma_p\widehat R(Q)^{ab}\big)\gamma^p\epsilon^i\\
&-\frac{1}{64}\eta_{ad}\gamma^{cd}\big(\overline{\mathcal D_{b}\chi}\gamma_{c}\gamma_{pq}\widehat R(Q)^{ab}\big)\gamma^{pq}\epsilon^i\\
&-\frac{i}{32}\eta_{bc}\gamma^{cd}\big(\bar\chi\gamma_{d}(\gamma\!\cdot\!T)\gamma_{a}\widehat R(Q)^{ab}\big)\epsilon^i\\
&-\frac{i}{32}\eta_{bc}\gamma^{cd}\big(\bar\chi\gamma_{d}(\gamma\!\cdot\!T)\gamma_{a}\gamma_p\widehat R(Q)^{ab}\big)\gamma^p\epsilon^i\\
&+\frac{i}{64}\eta_{bc}\gamma^{cd}\big(\bar\chi\gamma_{d}(\gamma\!\cdot\!T)\gamma_{a}\gamma_{pq}\widehat R(Q)^{ab}\big)\gamma^{pq}\epsilon^i\\
&+\frac{i}{32}\eta_{bd}\gamma^{cd}\big(\bar\chi\gamma_{c}(\gamma\!\cdot\!T)\gamma_{a}\widehat R(Q)^{ab}\big)\epsilon^i
\end{aligned}\tag{H154}
```

Continuation of the same right-hand side:

```math
\begin{aligned}
&+\frac{i}{32}\eta_{bd}\gamma^{cd}\big(\bar\chi\gamma_{c}(\gamma\!\cdot\!T)\gamma_{a}\gamma_p\widehat R(Q)^{ab}\big)\gamma^p\epsilon^i\\
&-\frac{i}{64}\eta_{bd}\gamma^{cd}\big(\bar\chi\gamma_{c}(\gamma\!\cdot\!T)\gamma_{a}\gamma_{pq}\widehat R(Q)^{ab}\big)\gamma^{pq}\epsilon^i\\
&+\frac{i}{32}\eta_{ac}\gamma^{cd}\big(\bar\chi\gamma_{d}(\gamma\!\cdot\!T)\gamma_{b}\widehat R(Q)^{ab}\big)\epsilon^i\\
&+\frac{i}{32}\eta_{ac}\gamma^{cd}\big(\bar\chi\gamma_{d}(\gamma\!\cdot\!T)\gamma_{b}\gamma_p\widehat R(Q)^{ab}\big)\gamma^p\epsilon^i\\
&-\frac{i}{64}\eta_{ac}\gamma^{cd}\big(\bar\chi\gamma_{d}(\gamma\!\cdot\!T)\gamma_{b}\gamma_{pq}\widehat R(Q)^{ab}\big)\gamma^{pq}\epsilon^i\\
&-\frac{i}{32}\eta_{ad}\gamma^{cd}\big(\bar\chi\gamma_{c}(\gamma\!\cdot\!T)\gamma_{b}\widehat R(Q)^{ab}\big)\epsilon^i\\
&-\frac{i}{32}\eta_{ad}\gamma^{cd}\big(\bar\chi\gamma_{c}(\gamma\!\cdot\!T)\gamma_{b}\gamma_p\widehat R(Q)^{ab}\big)\gamma^p\epsilon^i\\
&+\frac{i}{64}\eta_{ad}\gamma^{cd}\big(\bar\chi\gamma_{c}(\gamma\!\cdot\!T)\gamma_{b}\gamma_{pq}\widehat R(Q)^{ab}\big)\gamma^{pq}\epsilon^i\\
&+\frac{1}{96}\eta^{cd}\big(\overline{\mathcal D_e\widehat R(Q)_{ac}}\gamma^e\gamma_{bd}\widehat R(Q)^{ab}\big)\epsilon^i\\
&+\frac{1}{96}\eta^{cd}\big(\overline{\mathcal D_e\widehat R(Q)_{ac}}\gamma^e\gamma_{bd}\gamma_p\widehat R(Q)^{ab}\big)\gamma^p\epsilon^i\\
&-\frac{1}{192}\eta^{cd}\big(\overline{\mathcal D_e\widehat R(Q)_{ac}}\gamma^e\gamma_{bd}\gamma_{pq}\widehat R(Q)^{ab}\big)\gamma^{pq}\epsilon^i\\
&+\frac{1}{192}\eta^{cd}\big(\overline{\mathcal D^e\widehat R(Q)_{ce}}\gamma_{a}\gamma_{bd}\widehat R(Q)^{ab}\big)\epsilon^i\\
&+\frac{1}{192}\eta^{cd}\big(\overline{\mathcal D^e\widehat R(Q)_{ce}}\gamma_{a}\gamma_{bd}\gamma_p\widehat R(Q)^{ab}\big)\gamma^p\epsilon^i\\
&-\frac{1}{384}\eta^{cd}\big(\overline{\mathcal D^e\widehat R(Q)_{ce}}\gamma_{a}\gamma_{bd}\gamma_{pq}\widehat R(Q)^{ab}\big)\gamma^{pq}\epsilon^i\\
&-\frac{1}{192}\eta^{cd}\big(\overline{\mathcal D^e\widehat R(Q)_{ae}}\gamma_{c}\gamma_{bd}\widehat R(Q)^{ab}\big)\epsilon^i\\
&-\frac{1}{192}\eta^{cd}\big(\overline{\mathcal D^e\widehat R(Q)_{ae}}\gamma_{c}\gamma_{bd}\gamma_p\widehat R(Q)^{ab}\big)\gamma^p\epsilon^i\\
&+\frac{1}{384}\eta^{cd}\big(\overline{\mathcal D^e\widehat R(Q)_{ae}}\gamma_{c}\gamma_{bd}\gamma_{pq}\widehat R(Q)^{ab}\big)\gamma^{pq}\epsilon^i\\
&+\frac{i}{36}T^{ef}\eta^{cd}\big(\overline{\widehat R(Q)}_{ef}\gamma_{ac}\gamma_{bd}\widehat R(Q)^{ab}\big)\epsilon^i
\end{aligned}\tag{H155}
```

Continuation of the same right-hand side:

```math
\begin{aligned}
&+\frac{i}{36}T^{ef}\eta^{cd}\big(\overline{\widehat R(Q)}_{ef}\gamma_{ac}\gamma_{bd}\gamma_p\widehat R(Q)^{ab}\big)\gamma^p\epsilon^i\\
&-\frac{i}{72}T^{ef}\eta^{cd}\big(\overline{\widehat R(Q)}_{ef}\gamma_{ac}\gamma_{bd}\gamma_{pq}\widehat R(Q)^{ab}\big)\gamma^{pq}\epsilon^i\\
&+\frac{i}{16}T^{ef}\eta^{cd}\big(\overline{\widehat R(Q)}_{ce}\gamma_{a}\gamma_f\gamma_{bd}\widehat R(Q)^{ab}\big)\epsilon^i\\
&+\frac{i}{16}T^{ef}\eta^{cd}\big(\overline{\widehat R(Q)}_{ce}\gamma_{a}\gamma_f\gamma_{bd}\gamma_p\widehat R(Q)^{ab}\big)\gamma^p\epsilon^i\\
&-\frac{i}{32}T^{ef}\eta^{cd}\big(\overline{\widehat R(Q)}_{ce}\gamma_{a}\gamma_f\gamma_{bd}\gamma_{pq}\widehat R(Q)^{ab}\big)\gamma^{pq}\epsilon^i\\
&-\frac{i}{16}T^{ef}\eta^{cd}\big(\overline{\widehat R(Q)}_{ae}\gamma_{c}\gamma_f\gamma_{bd}\widehat R(Q)^{ab}\big)\epsilon^i\\
&-\frac{i}{16}T^{ef}\eta^{cd}\big(\overline{\widehat R(Q)}_{ae}\gamma_{c}\gamma_f\gamma_{bd}\gamma_p\widehat R(Q)^{ab}\big)\gamma^p\epsilon^i\\
&+\frac{i}{32}T^{ef}\eta^{cd}\big(\overline{\widehat R(Q)}_{ae}\gamma_{c}\gamma_f\gamma_{bd}\gamma_{pq}\widehat R(Q)^{ab}\big)\gamma^{pq}\epsilon^i\\
&+\frac{i}{32}\eta^{cd}\big(\overline{\widehat R(Q)}_{ac}(\gamma\!\cdot\!T)\gamma_{bd}\widehat R(Q)^{ab}\big)\epsilon^i\\
&+\frac{i}{32}\eta^{cd}\big(\overline{\widehat R(Q)}_{ac}(\gamma\!\cdot\!T)\gamma_{bd}\gamma_p\widehat R(Q)^{ab}\big)\gamma^p\epsilon^i\\
&-\frac{i}{64}\eta^{cd}\big(\overline{\widehat R(Q)}_{ac}(\gamma\!\cdot\!T)\gamma_{bd}\gamma_{pq}\widehat R(Q)^{ab}\big)\gamma^{pq}\epsilon^i\\
&-\frac{i}{24}T^e{}_{a}\eta^{cd}\big(\overline{\widehat R(Q)}_{ce}\gamma_{bd}\widehat R(Q)^{ab}\big)\epsilon^i\\
&-\frac{i}{24}T^e{}_{a}\eta^{cd}\big(\overline{\widehat R(Q)}_{ce}\gamma_{bd}\gamma_p\widehat R(Q)^{ab}\big)\gamma^p\epsilon^i\\
&+\frac{i}{48}T^e{}_{a}\eta^{cd}\big(\overline{\widehat R(Q)}_{ce}\gamma_{bd}\gamma_{pq}\widehat R(Q)^{ab}\big)\gamma^{pq}\epsilon^i\\
&+\frac{i}{24}T^e{}_{c}\eta^{cd}\big(\overline{\widehat R(Q)}_{ae}\gamma_{bd}\widehat R(Q)^{ab}\big)\epsilon^i\\
&+\frac{i}{24}T^e{}_{c}\eta^{cd}\big(\overline{\widehat R(Q)}_{ae}\gamma_{bd}\gamma_p\widehat R(Q)^{ab}\big)\gamma^p\epsilon^i\\
&-\frac{i}{48}T^e{}_{c}\eta^{cd}\big(\overline{\widehat R(Q)}_{ae}\gamma_{bd}\gamma_{pq}\widehat R(Q)^{ab}\big)\gamma^{pq}\epsilon^i\\
&+\frac{i}{96}\eta^{cd}\big(\overline{\widehat R(Q)}_{ac}\gamma_{b}(\gamma\!\cdot\!T)\gamma_{d}\widehat R(Q)^{ab}\big)\epsilon^i
\end{aligned}\tag{H156}
```

Continuation of the same right-hand side:

```math
\begin{aligned}
&+\frac{i}{96}\eta^{cd}\big(\overline{\widehat R(Q)}_{ac}\gamma_{b}(\gamma\!\cdot\!T)\gamma_{d}\gamma_p\widehat R(Q)^{ab}\big)\gamma^p\epsilon^i\\
&-\frac{i}{192}\eta^{cd}\big(\overline{\widehat R(Q)}_{ac}\gamma_{b}(\gamma\!\cdot\!T)\gamma_{d}\gamma_{pq}\widehat R(Q)^{ab}\big)\gamma^{pq}\epsilon^i\\
&-\frac{i}{96}\eta^{cd}\big(\overline{\widehat R(Q)}_{ac}\gamma_{d}(\gamma\!\cdot\!T)\gamma_{b}\widehat R(Q)^{ab}\big)\epsilon^i\\
&-\frac{i}{96}\eta^{cd}\big(\overline{\widehat R(Q)}_{ac}\gamma_{d}(\gamma\!\cdot\!T)\gamma_{b}\gamma_p\widehat R(Q)^{ab}\big)\gamma^p\epsilon^i\\
&+\frac{i}{192}\eta^{cd}\big(\overline{\widehat R(Q)}_{ac}\gamma_{d}(\gamma\!\cdot\!T)\gamma_{b}\gamma_{pq}\widehat R(Q)^{ab}\big)\gamma^{pq}\epsilon^i\\
&+\frac{1}{192}\eta^{cd}\big(\overline{\mathcal D_{a}\widehat R(Q)_{cd}}\gamma_{b}\widehat R(Q)^{ab}\big)\epsilon^i\\
&+\frac{1}{192}\eta^{cd}\big(\overline{\mathcal D_{a}\widehat R(Q)_{cd}}\gamma_{b}\gamma_p\widehat R(Q)^{ab}\big)\gamma^p\epsilon^i\\
&-\frac{1}{384}\eta^{cd}\big(\overline{\mathcal D_{a}\widehat R(Q)_{cd}}\gamma_{b}\gamma_{pq}\widehat R(Q)^{ab}\big)\gamma^{pq}\epsilon^i\\
&-\frac{1}{192}\eta^{cd}\big(\overline{\mathcal D_{a}\widehat R(Q)_{cb}}\gamma_{d}\widehat R(Q)^{ab}\big)\epsilon^i\\
&-\frac{1}{192}\eta^{cd}\big(\overline{\mathcal D_{a}\widehat R(Q)_{cb}}\gamma_{d}\gamma_p\widehat R(Q)^{ab}\big)\gamma^p\epsilon^i\\
&+\frac{1}{384}\eta^{cd}\big(\overline{\mathcal D_{a}\widehat R(Q)_{cb}}\gamma_{d}\gamma_{pq}\widehat R(Q)^{ab}\big)\gamma^{pq}\epsilon^i\\
&-\frac{1}{192}\eta^{cd}\big(\overline{\mathcal D_{c}\widehat R(Q)_{ad}}\gamma_{b}\widehat R(Q)^{ab}\big)\epsilon^i\\
&-\frac{1}{192}\eta^{cd}\big(\overline{\mathcal D_{c}\widehat R(Q)_{ad}}\gamma_{b}\gamma_p\widehat R(Q)^{ab}\big)\gamma^p\epsilon^i\\
&+\frac{1}{384}\eta^{cd}\big(\overline{\mathcal D_{c}\widehat R(Q)_{ad}}\gamma_{b}\gamma_{pq}\widehat R(Q)^{ab}\big)\gamma^{pq}\epsilon^i\\
&+\frac{1}{192}\eta^{cd}\big(\overline{\mathcal D_{c}\widehat R(Q)_{ab}}\gamma_{d}\widehat R(Q)^{ab}\big)\epsilon^i\\
&+\frac{1}{192}\eta^{cd}\big(\overline{\mathcal D_{c}\widehat R(Q)_{ab}}\gamma_{d}\gamma_p\widehat R(Q)^{ab}\big)\gamma^p\epsilon^i\\
&-\frac{1}{384}\eta^{cd}\big(\overline{\mathcal D_{c}\widehat R(Q)_{ab}}\gamma_{d}\gamma_{pq}\widehat R(Q)^{ab}\big)\gamma^{pq}\epsilon^i\\
&-\frac{i}{192}\eta^{cd}\big(\overline{\widehat R(Q)}_{cd}\gamma_{b}(\gamma\!\cdot\!T)\gamma_{a}\widehat R(Q)^{ab}\big)\epsilon^i
\end{aligned}\tag{H157}
```

Continuation of the same right-hand side:

```math
\begin{aligned}
&-\frac{i}{192}\eta^{cd}\big(\overline{\widehat R(Q)}_{cd}\gamma_{b}(\gamma\!\cdot\!T)\gamma_{a}\gamma_p\widehat R(Q)^{ab}\big)\gamma^p\epsilon^i\\
&+\frac{i}{384}\eta^{cd}\big(\overline{\widehat R(Q)}_{cd}\gamma_{b}(\gamma\!\cdot\!T)\gamma_{a}\gamma_{pq}\widehat R(Q)^{ab}\big)\gamma^{pq}\epsilon^i\\
&+\frac{i}{192}\eta^{cd}\big(\overline{\widehat R(Q)}_{cb}\gamma_{d}(\gamma\!\cdot\!T)\gamma_{a}\widehat R(Q)^{ab}\big)\epsilon^i\\
&+\frac{i}{192}\eta^{cd}\big(\overline{\widehat R(Q)}_{cb}\gamma_{d}(\gamma\!\cdot\!T)\gamma_{a}\gamma_p\widehat R(Q)^{ab}\big)\gamma^p\epsilon^i\\
&-\frac{i}{384}\eta^{cd}\big(\overline{\widehat R(Q)}_{cb}\gamma_{d}(\gamma\!\cdot\!T)\gamma_{a}\gamma_{pq}\widehat R(Q)^{ab}\big)\gamma^{pq}\epsilon^i\\
&+\frac{i}{192}\eta^{cd}\big(\overline{\widehat R(Q)}_{ad}\gamma_{b}(\gamma\!\cdot\!T)\gamma_{c}\widehat R(Q)^{ab}\big)\epsilon^i\\
&+\frac{i}{192}\eta^{cd}\big(\overline{\widehat R(Q)}_{ad}\gamma_{b}(\gamma\!\cdot\!T)\gamma_{c}\gamma_p\widehat R(Q)^{ab}\big)\gamma^p\epsilon^i\\
&-\frac{i}{384}\eta^{cd}\big(\overline{\widehat R(Q)}_{ad}\gamma_{b}(\gamma\!\cdot\!T)\gamma_{c}\gamma_{pq}\widehat R(Q)^{ab}\big)\gamma^{pq}\epsilon^i\\
&-\frac{i}{192}\eta^{cd}\big(\overline{\widehat R(Q)}_{ab}\gamma_{d}(\gamma\!\cdot\!T)\gamma_{c}\widehat R(Q)^{ab}\big)\epsilon^i\\
&-\frac{i}{192}\eta^{cd}\big(\overline{\widehat R(Q)}_{ab}\gamma_{d}(\gamma\!\cdot\!T)\gamma_{c}\gamma_p\widehat R(Q)^{ab}\big)\gamma^p\epsilon^i\\
&+\frac{i}{384}\eta^{cd}\big(\overline{\widehat R(Q)}_{ab}\gamma_{d}(\gamma\!\cdot\!T)\gamma_{c}\gamma_{pq}\widehat R(Q)^{ab}\big)\gamma^{pq}\epsilon^i\\
&-\frac{1}{192}\eta^{cd}\big(\overline{\mathcal D_{c}\widehat R(Q)_{bd}}\gamma_{a}\widehat R(Q)^{ab}\big)\epsilon^i\\
&-\frac{1}{192}\eta^{cd}\big(\overline{\mathcal D_{c}\widehat R(Q)_{bd}}\gamma_{a}\gamma_p\widehat R(Q)^{ab}\big)\gamma^p\epsilon^i\\
&+\frac{1}{384}\eta^{cd}\big(\overline{\mathcal D_{c}\widehat R(Q)_{bd}}\gamma_{a}\gamma_{pq}\widehat R(Q)^{ab}\big)\gamma^{pq}\epsilon^i\\
&+\frac{1}{192}\eta^{cd}\big(\overline{\mathcal D_{a}\widehat R(Q)_{bd}}\gamma_{c}\widehat R(Q)^{ab}\big)\epsilon^i\\
&+\frac{1}{192}\eta^{cd}\big(\overline{\mathcal D_{a}\widehat R(Q)_{bd}}\gamma_{c}\gamma_p\widehat R(Q)^{ab}\big)\gamma^p\epsilon^i\\
&-\frac{1}{384}\eta^{cd}\big(\overline{\mathcal D_{a}\widehat R(Q)_{bd}}\gamma_{c}\gamma_{pq}\widehat R(Q)^{ab}\big)\gamma^{pq}\epsilon^i\\
&+\frac{i}{192}\eta^{cd}\big(\overline{\widehat R(Q)}_{bd}\gamma_{a}(\gamma\!\cdot\!T)\gamma_{c}\widehat R(Q)^{ab}\big)\epsilon^i
\end{aligned}\tag{H158}
```

Continuation of the same right-hand side:

```math
\begin{aligned}
&+\frac{i}{192}\eta^{cd}\big(\overline{\widehat R(Q)}_{bd}\gamma_{a}(\gamma\!\cdot\!T)\gamma_{c}\gamma_p\widehat R(Q)^{ab}\big)\gamma^p\epsilon^i\\
&-\frac{i}{384}\eta^{cd}\big(\overline{\widehat R(Q)}_{bd}\gamma_{a}(\gamma\!\cdot\!T)\gamma_{c}\gamma_{pq}\widehat R(Q)^{ab}\big)\gamma^{pq}\epsilon^i\\
&-\frac{i}{192}\eta^{cd}\big(\overline{\widehat R(Q)}_{bd}\gamma_{c}(\gamma\!\cdot\!T)\gamma_{a}\widehat R(Q)^{ab}\big)\epsilon^i\\
&-\frac{i}{192}\eta^{cd}\big(\overline{\widehat R(Q)}_{bd}\gamma_{c}(\gamma\!\cdot\!T)\gamma_{a}\gamma_p\widehat R(Q)^{ab}\big)\gamma^p\epsilon^i\\
&+\frac{i}{384}\eta^{cd}\big(\overline{\widehat R(Q)}_{bd}\gamma_{c}(\gamma\!\cdot\!T)\gamma_{a}\gamma_{pq}\widehat R(Q)^{ab}\big)\gamma^{pq}\epsilon^i\\
&+\frac{1}{24}\eta_{cb}\eta^{cd}\big(\overline{\mathcal D_{a}\chi}\gamma_{d}\widehat R(Q)^{ab}\big)\epsilon^i\\
&+\frac{1}{24}\eta_{cb}\eta^{cd}\big(\overline{\mathcal D_{a}\chi}\gamma_{d}\gamma_p\widehat R(Q)^{ab}\big)\gamma^p\epsilon^i\\
&-\frac{1}{48}\eta_{cb}\eta^{cd}\big(\overline{\mathcal D_{a}\chi}\gamma_{d}\gamma_{pq}\widehat R(Q)^{ab}\big)\gamma^{pq}\epsilon^i\\
&-\frac{1}{24}\eta_{cd}\eta^{cd}\big(\overline{\mathcal D_{a}\chi}\gamma_{b}\widehat R(Q)^{ab}\big)\epsilon^i\\
&-\frac{1}{24}\eta_{cd}\eta^{cd}\big(\overline{\mathcal D_{a}\chi}\gamma_{b}\gamma_p\widehat R(Q)^{ab}\big)\gamma^p\epsilon^i\\
&+\frac{1}{48}\eta_{cd}\eta^{cd}\big(\overline{\mathcal D_{a}\chi}\gamma_{b}\gamma_{pq}\widehat R(Q)^{ab}\big)\gamma^{pq}\epsilon^i\\
&-\frac{1}{24}\eta_{ab}\eta^{cd}\big(\overline{\mathcal D_{c}\chi}\gamma_{d}\widehat R(Q)^{ab}\big)\epsilon^i\\
&-\frac{1}{24}\eta_{ab}\eta^{cd}\big(\overline{\mathcal D_{c}\chi}\gamma_{d}\gamma_p\widehat R(Q)^{ab}\big)\gamma^p\epsilon^i\\
&+\frac{1}{48}\eta_{ab}\eta^{cd}\big(\overline{\mathcal D_{c}\chi}\gamma_{d}\gamma_{pq}\widehat R(Q)^{ab}\big)\gamma^{pq}\epsilon^i\\
&+\frac{1}{24}\eta_{ad}\eta^{cd}\big(\overline{\mathcal D_{c}\chi}\gamma_{b}\widehat R(Q)^{ab}\big)\epsilon^i\\
&+\frac{1}{24}\eta_{ad}\eta^{cd}\big(\overline{\mathcal D_{c}\chi}\gamma_{b}\gamma_p\widehat R(Q)^{ab}\big)\gamma^p\epsilon^i\\
&-\frac{1}{48}\eta_{ad}\eta^{cd}\big(\overline{\mathcal D_{c}\chi}\gamma_{b}\gamma_{pq}\widehat R(Q)^{ab}\big)\gamma^{pq}\epsilon^i\\
&-\frac{i}{24}\eta_{cb}\eta^{cd}\big(\bar\chi\gamma_{d}(\gamma\!\cdot\!T)\gamma_{a}\widehat R(Q)^{ab}\big)\epsilon^i
\end{aligned}\tag{H159}
```

Continuation of the same right-hand side:

```math
\begin{aligned}
&-\frac{i}{24}\eta_{cb}\eta^{cd}\big(\bar\chi\gamma_{d}(\gamma\!\cdot\!T)\gamma_{a}\gamma_p\widehat R(Q)^{ab}\big)\gamma^p\epsilon^i\\
&+\frac{i}{48}\eta_{cb}\eta^{cd}\big(\bar\chi\gamma_{d}(\gamma\!\cdot\!T)\gamma_{a}\gamma_{pq}\widehat R(Q)^{ab}\big)\gamma^{pq}\epsilon^i\\
&+\frac{i}{24}\eta_{cd}\eta^{cd}\big(\bar\chi\gamma_{b}(\gamma\!\cdot\!T)\gamma_{a}\widehat R(Q)^{ab}\big)\epsilon^i\\
&+\frac{i}{24}\eta_{cd}\eta^{cd}\big(\bar\chi\gamma_{b}(\gamma\!\cdot\!T)\gamma_{a}\gamma_p\widehat R(Q)^{ab}\big)\gamma^p\epsilon^i\\
&-\frac{i}{48}\eta_{cd}\eta^{cd}\big(\bar\chi\gamma_{b}(\gamma\!\cdot\!T)\gamma_{a}\gamma_{pq}\widehat R(Q)^{ab}\big)\gamma^{pq}\epsilon^i\\
&+\frac{i}{24}\eta_{ab}\eta^{cd}\big(\bar\chi\gamma_{d}(\gamma\!\cdot\!T)\gamma_{c}\widehat R(Q)^{ab}\big)\epsilon^i\\
&+\frac{i}{24}\eta_{ab}\eta^{cd}\big(\bar\chi\gamma_{d}(\gamma\!\cdot\!T)\gamma_{c}\gamma_p\widehat R(Q)^{ab}\big)\gamma^p\epsilon^i\\
&-\frac{i}{48}\eta_{ab}\eta^{cd}\big(\bar\chi\gamma_{d}(\gamma\!\cdot\!T)\gamma_{c}\gamma_{pq}\widehat R(Q)^{ab}\big)\gamma^{pq}\epsilon^i\\
&-\frac{i}{24}\eta_{ad}\eta^{cd}\big(\bar\chi\gamma_{b}(\gamma\!\cdot\!T)\gamma_{c}\widehat R(Q)^{ab}\big)\epsilon^i\\
&-\frac{i}{24}\eta_{ad}\eta^{cd}\big(\bar\chi\gamma_{b}(\gamma\!\cdot\!T)\gamma_{c}\gamma_p\widehat R(Q)^{ab}\big)\gamma^p\epsilon^i\\
&+\frac{i}{48}\eta_{ad}\eta^{cd}\big(\bar\chi\gamma_{b}(\gamma\!\cdot\!T)\gamma_{c}\gamma_{pq}\widehat R(Q)^{ab}\big)\gamma^{pq}\epsilon^i\\
&-i\gamma_c \gamma_{de}\widehat C_{ab}{}^{de}(\mathcal D^aT^{bc})\epsilon^i\\
&+8\gamma_c \gamma^{de} \gamma_{b]}(\mathcal D_{[a}T_{de})(\mathcal D^aT^{bc})\epsilon^i\\
&-\frac{8}{3}\gamma_c \gamma_{[b} \gamma^{de}(\mathcal D_{a]}T_{de})(\mathcal D^aT^{bc})\epsilon^i\\
&-\frac{8}{3}\gamma_c \gamma_{[a} \gamma^{f} \gamma^{de} \gamma_{b]}(\mathcal D_fT_{de})(\mathcal D^aT^{bc})\epsilon^i\\
&-\frac{8}{3}\gamma_c \gamma_{ab} \gamma^{d}(\mathcal D^eT_{ed})(\mathcal D^aT^{bc})\epsilon^i\\
&-\frac{1}{4}\gamma^c\big(\overline{\mathcal D_a\chi}\gamma_{bc}\widehat R(Q)^{ab}\big)\epsilon^i\\
&-\frac{1}{4}\gamma^c\big(\overline{\mathcal D_a\chi}\gamma_{bc}\gamma_p\widehat R(Q)^{ab}\big)\gamma^p\epsilon^i
\end{aligned}\tag{H160}
```

Continuation of the same right-hand side:

```math
\begin{aligned}
&+\frac{1}{8}\gamma^c\big(\overline{\mathcal D_a\chi}\gamma_{bc}\gamma_{pq}\widehat R(Q)^{ab}\big)\gamma^{pq}\epsilon^i\\
&-\frac{3}{64}\gamma^c\big(\overline{\mathcal D_a\widehat R(Q)_{bc}}\widehat R(Q)^{ab}\big)\epsilon^i\\
&-\frac{3}{64}\gamma^c\big(\overline{\mathcal D_a\widehat R(Q)_{bc}}\gamma_p\widehat R(Q)^{ab}\big)\gamma^p\epsilon^i\\
&+\frac{3}{128}\gamma^c\big(\overline{\mathcal D_a\widehat R(Q)_{bc}}\gamma_{pq}\widehat R(Q)^{ab}\big)\gamma^{pq}\epsilon^i\\
&+\frac{i}{4}\gamma^c\big(\bar\chi\gamma_{bc}(\gamma\!\cdot\!T)\gamma_a\widehat R(Q)^{ab}\big)\epsilon^i\\
&+\frac{i}{4}\gamma^c\big(\bar\chi\gamma_{bc}(\gamma\!\cdot\!T)\gamma_a\gamma_p\widehat R(Q)^{ab}\big)\gamma^p\epsilon^i\\
&-\frac{i}{8}\gamma^c\big(\bar\chi\gamma_{bc}(\gamma\!\cdot\!T)\gamma_a\gamma_{pq}\widehat R(Q)^{ab}\big)\gamma^{pq}\epsilon^i\\
&+\frac{3i}{64}\gamma^c\big(\overline{\widehat R(Q)}_{bc}(\gamma\!\cdot\!T)\gamma_a\widehat R(Q)^{ab}\big)\epsilon^i\\
&+\frac{3i}{64}\gamma^c\big(\overline{\widehat R(Q)}_{bc}(\gamma\!\cdot\!T)\gamma_a\gamma_p\widehat R(Q)^{ab}\big)\gamma^p\epsilon^i\\
&-\frac{3i}{128}\gamma^c\big(\overline{\widehat R(Q)}_{bc}(\gamma\!\cdot\!T)\gamma_a\gamma_{pq}\widehat R(Q)^{ab}\big)\gamma^{pq}\epsilon^i\\
&-iT_{bc}\gamma^c\big(\bar\chi\gamma_a\widehat R(Q)^{ab}\big)\epsilon^i\\
&-iT_{bc}\gamma^c\big(\bar\chi\gamma_a\gamma_p\widehat R(Q)^{ab}\big)\gamma^p\epsilon^i\\
&+\frac{i}{2}T_{bc}\gamma^c\big(\bar\chi\gamma_a\gamma_{pq}\widehat R(Q)^{ab}\big)\gamma^{pq}\epsilon^i\\
&+\frac{i}{8}T_{dc}\gamma^c\big(\overline{\widehat R(Q)}_a{}^{d}\gamma_{b}\widehat R(Q)^{ab}\big)\epsilon^i\\
&+\frac{i}{8}T_{dc}\gamma^c\big(\overline{\widehat R(Q)}_a{}^{d}\gamma_{b}\gamma_p\widehat R(Q)^{ab}\big)\gamma^p\epsilon^i\\
&-\frac{i}{16}T_{dc}\gamma^c\big(\overline{\widehat R(Q)}_a{}^{d}\gamma_{b}\gamma_{pq}\widehat R(Q)^{ab}\big)\gamma^{pq}\epsilon^i\\
&-\frac{i}{8}T_{dc}\gamma^c\big(\overline{\widehat R(Q)}_a{}^{b}\gamma_{d}\widehat R(Q)^{ab}\big)\epsilon^i\\
&-\frac{i}{8}T_{dc}\gamma^c\big(\overline{\widehat R(Q)}_a{}^{b}\gamma_{d}\gamma_p\widehat R(Q)^{ab}\big)\gamma^p\epsilon^i
\end{aligned}\tag{H161}
```

Continuation of the same right-hand side:

```math
\begin{aligned}
&+\frac{i}{16}T_{dc}\gamma^c\big(\overline{\widehat R(Q)}_a{}^{b}\gamma_{d}\gamma_{pq}\widehat R(Q)^{ab}\big)\gamma^{pq}\epsilon^i\\
&+\frac{i}{8}T_{dc}\gamma^c\big(\overline{\widehat R(Q)}_b{}^d\gamma_a\widehat R(Q)^{ab}\big)\epsilon^i\\
&+\frac{i}{8}T_{dc}\gamma^c\big(\overline{\widehat R(Q)}_b{}^d\gamma_a\gamma_p\widehat R(Q)^{ab}\big)\gamma^p\epsilon^i\\
&-\frac{i}{16}T_{dc}\gamma^c\big(\overline{\widehat R(Q)}_b{}^d\gamma_a\gamma_{pq}\widehat R(Q)^{ab}\big)\gamma^{pq}\epsilon^i\\
&+i\eta_{ab}T_{dc}\gamma^c\big(\bar\chi\gamma^{d}\widehat R(Q)^{ab}\big)\epsilon^i\\
&+i\eta_{ab}T_{dc}\gamma^c\big(\bar\chi\gamma^{d}\gamma_p\widehat R(Q)^{ab}\big)\gamma^p\epsilon^i\\
&-\frac{i}{2}\eta_{ab}T_{dc}\gamma^c\big(\bar\chi\gamma^{d}\gamma_{pq}\widehat R(Q)^{ab}\big)\gamma^{pq}\epsilon^i\\
&-i\eta_{ad}T_{dc}\gamma^c\big(\bar\chi\gamma^{b}\widehat R(Q)^{ab}\big)\epsilon^i\\
&-i\eta_{ad}T_{dc}\gamma^c\big(\bar\chi\gamma^{b}\gamma_p\widehat R(Q)^{ab}\big)\gamma^p\epsilon^i\\
&+\frac{i}{2}\eta_{ad}T_{dc}\gamma^c\big(\bar\chi\gamma^{b}\gamma_{pq}\widehat R(Q)^{ab}\big)\gamma^{pq}\epsilon^i\\
&+\frac{i}{8}T_{bd}\gamma^c\big(\overline{\widehat R(Q)}_a{}^{d}\gamma_{c}\widehat R(Q)^{ab}\big)\epsilon^i\\
&+\frac{i}{8}T_{bd}\gamma^c\big(\overline{\widehat R(Q)}_a{}^{d}\gamma_{c}\gamma_p\widehat R(Q)^{ab}\big)\gamma^p\epsilon^i\\
&-\frac{i}{16}T_{bd}\gamma^c\big(\overline{\widehat R(Q)}_a{}^{d}\gamma_{c}\gamma_{pq}\widehat R(Q)^{ab}\big)\gamma^{pq}\epsilon^i\\
&-\frac{i}{8}T_{bd}\gamma^c\big(\overline{\widehat R(Q)}_a{}^{c}\gamma_{d}\widehat R(Q)^{ab}\big)\epsilon^i\\
&-\frac{i}{8}T_{bd}\gamma^c\big(\overline{\widehat R(Q)}_a{}^{c}\gamma_{d}\gamma_p\widehat R(Q)^{ab}\big)\gamma^p\epsilon^i\\
&+\frac{i}{16}T_{bd}\gamma^c\big(\overline{\widehat R(Q)}_a{}^{c}\gamma_{d}\gamma_{pq}\widehat R(Q)^{ab}\big)\gamma^{pq}\epsilon^i\\
&+\frac{i}{8}T_{bd}\gamma^c\big(\overline{\widehat R(Q)}_c{}^d\gamma_a\widehat R(Q)^{ab}\big)\epsilon^i\\
&+\frac{i}{8}T_{bd}\gamma^c\big(\overline{\widehat R(Q)}_c{}^d\gamma_a\gamma_p\widehat R(Q)^{ab}\big)\gamma^p\epsilon^i
\end{aligned}\tag{H162}
```

Continuation of the same right-hand side:

```math
\begin{aligned}
&-\frac{i}{16}T_{bd}\gamma^c\big(\overline{\widehat R(Q)}_c{}^d\gamma_a\gamma_{pq}\widehat R(Q)^{ab}\big)\gamma^{pq}\epsilon^i\\
&+i\eta_{ac}T_{bd}\gamma^c\big(\bar\chi\gamma^{d}\widehat R(Q)^{ab}\big)\epsilon^i\\
&+i\eta_{ac}T_{bd}\gamma^c\big(\bar\chi\gamma^{d}\gamma_p\widehat R(Q)^{ab}\big)\gamma^p\epsilon^i\\
&-\frac{i}{2}\eta_{ac}T_{bd}\gamma^c\big(\bar\chi\gamma^{d}\gamma_{pq}\widehat R(Q)^{ab}\big)\gamma^{pq}\epsilon^i\\
&-i\eta_{ad}T_{bd}\gamma^c\big(\bar\chi\gamma^{c}\widehat R(Q)^{ab}\big)\epsilon^i\\
&-i\eta_{ad}T_{bd}\gamma^c\big(\bar\chi\gamma^{c}\gamma_p\widehat R(Q)^{ab}\big)\gamma^p\epsilon^i\\
&+\frac{i}{2}\eta_{ad}T_{bd}\gamma^c\big(\bar\chi\gamma^{c}\gamma_{pq}\widehat R(Q)^{ab}\big)\gamma^{pq}\epsilon^i\\
&+\frac{32}{3}D^2\epsilon^i\\
&+\frac{16i}{3}\gamma^{ab} \gamma^{c}(\mathcal D_cT_{ab})D\epsilon^i\\
&-\frac{16i}{3}\gamma^{a}(\mathcal D^bT_{ab})D\epsilon^i\\
&-\frac{32}{3}D\gamma^{rstu}T_{rs}T_{tu}\epsilon^i\\
&+\frac{64}{9}T^2D\epsilon^i\\
&+\frac{16}{3}\big(\overline{\mathcal D_a\chi}\gamma^a\chi\big)\epsilon^i\\
&+\frac{16}{3}\big(\overline{\mathcal D_a\chi}\gamma^a\gamma_p\chi\big)\gamma^p\epsilon^i\\
&-\frac{8}{3}\big(\overline{\mathcal D_a\chi}\gamma^a\gamma_{pq}\chi\big)\gamma^{pq}\epsilon^i\\
&+\frac{80i}{9}\big(\bar\chi(\gamma\!\cdot\!T)\chi\big)\epsilon^i\\
&+\frac{80i}{9}\big(\bar\chi(\gamma\!\cdot\!T)\gamma_p\chi\big)\gamma^p\epsilon^i\\
&-\frac{40i}{9}\big(\bar\chi(\gamma\!\cdot\!T)\gamma_{pq}\chi\big)\gamma^{pq}\epsilon^i
\end{aligned}\tag{H163}
```

Continuation of the same right-hand side:

```math
\begin{aligned}
&+\frac{1}{2}\big(\bar\chi\gamma^{ab}\gamma_c\mathcal D^c\widehat R(Q)_{ab}\big)\epsilon^i\\
&+\frac{1}{2}\big(\bar\chi\gamma^{ab}\gamma_p\gamma_c\mathcal D^c\widehat R(Q)_{ab}\big)\gamma^p\epsilon^i\\
&-\frac{1}{4}\big(\bar\chi\gamma^{ab}\gamma_{pq}\gamma_c\mathcal D^c\widehat R(Q)_{ab}\big)\gamma^{pq}\epsilon^i\\
&+\frac{3}{32}\big(\overline{\widehat R(Q)}^{ab}\gamma_c\mathcal D^c\widehat R(Q)_{ab}\big)\epsilon^i\\
&+\frac{3}{32}\big(\overline{\widehat R(Q)}^{ab}\gamma_p\gamma_c\mathcal D^c\widehat R(Q)_{ab}\big)\gamma^p\epsilon^i\\
&-\frac{3}{64}\big(\overline{\widehat R(Q)}^{ab}\gamma_{pq}\gamma_c\mathcal D^c\widehat R(Q)_{ab}\big)\gamma^{pq}\epsilon^i\\
&+2iT^{ab}\gamma^c(\mathcal D_c\widehat C_{ab}{}^{de})\gamma_{de}\epsilon^i\\
&-16T^{ab}\gamma^c\gamma^{de}(\mathcal D_c\mathcal D_{[a}T_{de})\gamma_{b]}\epsilon^i\\
&+\frac{16}{3}T^{ab}\gamma^c\gamma_{[b}\gamma^{de}(\mathcal D_c\mathcal D_{a]}T_{de})\epsilon^i\\
&+\frac{16}{3}T^{ab}\gamma^c\gamma_{[a}\gamma^f\gamma^{de}(\mathcal D_c\mathcal D_fT_{de})\gamma_{b]}\epsilon^i\\
&+\frac{16}{3}T^{ab}\gamma^c\gamma_{ab}\gamma_d\mathcal D_c\mathcal D_eT^{ed}\epsilon^i\\
&+2T^{ab}\gamma^c\widehat C_{ab}{}^{de}\gamma_{de}(\gamma\!\cdot\!T)\gamma_c\epsilon^i\\
&+16iT^{ab}\gamma^c\gamma^{de}(\mathcal D_{[a}T_{de})\gamma_{b]}(\gamma\!\cdot\!T)\gamma_c\epsilon^i\\
&-\frac{16i}{3}T^{ab}\gamma^c\gamma_{[b}\gamma^{de}(\mathcal D_{a]}T_{de})(\gamma\!\cdot\!T)\gamma_c\epsilon^i\\
&-\frac{16i}{3}T^{ab}\gamma^c\gamma_{[a}\gamma^f\gamma^{de}(\mathcal D_fT_{de})\gamma_{b]}(\gamma\!\cdot\!T)\gamma_c\epsilon^i\\
&-\frac{16i}{3}T^{ab}\gamma^c\gamma_{ab}\gamma_d(\mathcal D_eT^{ed})(\gamma\!\cdot\!T)\gamma_c\epsilon^i\\
&+\frac{64i}{3}T^{ab}\gamma^cT_{ab}\gamma^s\gamma^{hr}(\mathcal D_sT_{hr})\gamma_c\epsilon^i\\
&-\frac{64i}{3}T^{ab}\gamma^cT_{ab}\gamma^{hr}(\mathcal D_cT_{hr})\epsilon^i
\end{aligned}\tag{H164}
```

Continuation of the same right-hand side:

```math
\begin{aligned}
&+\frac{64i}{3}T^{ab}\gamma^cT_{ab}\gamma_c\gamma^r(\mathcal D^hT_{hr})\epsilon^i\\
&+64T^{ab}\gamma^cT_{ab}\gamma_{chrst}T^{hr}T^{st}\epsilon^i\\
&-512T^{ab}\gamma^cT_{ab}\gamma_hT^{hr}T_{cr}\epsilon^i\\
&+128T^{ab}\gamma^cT_{ab}\gamma_cT^2\epsilon^i\\
&-\frac{128i}{9}T^{ab}\gamma^cT_{[a}{}^d\gamma_{b]d}\gamma^s\gamma^{hr}(\mathcal D_sT_{hr})\gamma_c\epsilon^i\\
&+\frac{128i}{9}T^{ab}\gamma^cT_{[a}{}^d\gamma_{b]d}\gamma^{hr}(\mathcal D_cT_{hr})\epsilon^i\\
&-\frac{128i}{9}T^{ab}\gamma^cT_{[a}{}^d\gamma_{b]d}\gamma_c\gamma^r(\mathcal D^hT_{hr})\epsilon^i\\
&-\frac{128}{3}T^{ab}\gamma^cT_{[a}{}^d\gamma_{b]d}\gamma_{chrst}T^{hr}T^{st}\epsilon^i\\
&+\frac{1024}{3}T^{ab}\gamma^cT_{[a}{}^d\gamma_{b]d}\gamma_hT^{hr}T_{cr}\epsilon^i\\
&-\frac{256}{3}T^{ab}\gamma^cT_{[a}{}^d\gamma_{b]d}\gamma_cT^2\epsilon^i\\
&-\frac{32i}{9}T^{ab}\gamma^c\gamma_{abde}T^{de}\gamma^s\gamma^{hr}(\mathcal D_sT_{hr})\gamma_c\epsilon^i\\
&+\frac{32i}{9}T^{ab}\gamma^c\gamma_{abde}T^{de}\gamma^{hr}(\mathcal D_cT_{hr})\epsilon^i\\
&-\frac{32i}{9}T^{ab}\gamma^c\gamma_{abde}T^{de}\gamma_c\gamma^r(\mathcal D^hT_{hr})\epsilon^i\\
&-\frac{32}{3}T^{ab}\gamma^c\gamma_{abde}T^{de}\gamma_{chrst}T^{hr}T^{st}\epsilon^i\\
&+\frac{256}{3}T^{ab}\gamma^c\gamma_{abde}T^{de}\gamma_hT^{hr}T_{cr}\epsilon^i\\
&-\frac{64}{3}T^{ab}\gamma^c\gamma_{abde}T^{de}\gamma_cT^2\epsilon^i\\
&+9iT^{ab}\gamma^c\big(\bar\chi\gamma_c\widehat R(Q)_{ab}\big)\epsilon^i\\
&+9iT^{ab}\gamma^c\big(\bar\chi\gamma_c\gamma_p\widehat R(Q)_{ab}\big)\gamma^p\epsilon^i
\end{aligned}\tag{H165}
```

Continuation of the same right-hand side:

```math
\begin{aligned}
&-\frac{9i}{2}T^{ab}\gamma^c\big(\bar\chi\gamma_c\gamma_{pq}\widehat R(Q)_{ab}\big)\gamma^{pq}\epsilon^i\\
&-\frac{i}{16}T^{ab}\gamma^c\gamma_{de}\big(\overline{\widehat R(Q)}_c{}^{e}\gamma^{d}\widehat R(Q)_{ab}\big)\epsilon^i\\
&-\frac{i}{16}T^{ab}\gamma^c\gamma_{de}\big(\overline{\widehat R(Q)}_c{}^{e}\gamma^{d}\gamma_p\widehat R(Q)_{ab}\big)\gamma^p\epsilon^i\\
&+\frac{i}{32}T^{ab}\gamma^c\gamma_{de}\big(\overline{\widehat R(Q)}_c{}^{e}\gamma^{d}\gamma_{pq}\widehat R(Q)_{ab}\big)\gamma^{pq}\epsilon^i\\
&+\frac{i}{16}T^{ab}\gamma^c\gamma_{de}\big(\overline{\widehat R(Q)}_c{}^{d}\gamma^{e}\widehat R(Q)_{ab}\big)\epsilon^i\\
&+\frac{i}{16}T^{ab}\gamma^c\gamma_{de}\big(\overline{\widehat R(Q)}_c{}^{d}\gamma^{e}\gamma_p\widehat R(Q)_{ab}\big)\gamma^p\epsilon^i\\
&-\frac{i}{32}T^{ab}\gamma^c\gamma_{de}\big(\overline{\widehat R(Q)}_c{}^{d}\gamma^{e}\gamma_{pq}\widehat R(Q)_{ab}\big)\gamma^{pq}\epsilon^i\\
&-\frac{i}{16}T^{ab}\gamma^c\gamma_{de}\big(\overline{\widehat R(Q)}^{de}\gamma_c\widehat R(Q)_{ab}\big)\epsilon^i\\
&-\frac{i}{16}T^{ab}\gamma^c\gamma_{de}\big(\overline{\widehat R(Q)}^{de}\gamma_c\gamma_p\widehat R(Q)_{ab}\big)\gamma^p\epsilon^i\\
&+\frac{i}{32}T^{ab}\gamma^c\gamma_{de}\big(\overline{\widehat R(Q)}^{de}\gamma_c\gamma_{pq}\widehat R(Q)_{ab}\big)\gamma^{pq}\epsilon^i\\
&-\frac{i}{2}\delta_c{}^{d}T^{ab}\gamma^c\gamma_{de}\big(\bar\chi\gamma^{e}\widehat R(Q)_{ab}\big)\epsilon^i\\
&-\frac{i}{2}\delta_c{}^{d}T^{ab}\gamma^c\gamma_{de}\big(\bar\chi\gamma^{e}\gamma_p\widehat R(Q)_{ab}\big)\gamma^p\epsilon^i\\
&+\frac{i}{4}\delta_c{}^{d}T^{ab}\gamma^c\gamma_{de}\big(\bar\chi\gamma^{e}\gamma_{pq}\widehat R(Q)_{ab}\big)\gamma^{pq}\epsilon^i\\
&+\frac{i}{2}\delta_c{}^{e}T^{ab}\gamma^c\gamma_{de}\big(\bar\chi\gamma^{d}\widehat R(Q)_{ab}\big)\epsilon^i\\
&+\frac{i}{2}\delta_c{}^{e}T^{ab}\gamma^c\gamma_{de}\big(\bar\chi\gamma^{d}\gamma_p\widehat R(Q)_{ab}\big)\gamma^p\epsilon^i\\
&-\frac{i}{4}\delta_c{}^{e}T^{ab}\gamma^c\gamma_{de}\big(\bar\chi\gamma^{d}\gamma_{pq}\widehat R(Q)_{ab}\big)\gamma^{pq}\epsilon^i\\
&-\frac{i}{4}T^{ab}\gamma^c\big(\overline{\widehat R(Q)}_c{}^{d}\gamma_{a}\widehat R(Q)_{db}\big)\epsilon^i\\
&-\frac{i}{4}T^{ab}\gamma^c\big(\overline{\widehat R(Q)}_c{}^{d}\gamma_{a}\gamma_p\widehat R(Q)_{db}\big)\gamma^p\epsilon^i
\end{aligned}\tag{H166}
```

Continuation of the same right-hand side:

```math
\begin{aligned}
&+\frac{i}{8}T^{ab}\gamma^c\big(\overline{\widehat R(Q)}_c{}^{d}\gamma_{a}\gamma_{pq}\widehat R(Q)_{db}\big)\gamma^{pq}\epsilon^i\\
&+\frac{i}{4}T^{ab}\gamma^c\big(\overline{\widehat R(Q)}_c{}^{a}\gamma_{d}\widehat R(Q)_{db}\big)\epsilon^i\\
&+\frac{i}{4}T^{ab}\gamma^c\big(\overline{\widehat R(Q)}_c{}^{a}\gamma_{d}\gamma_p\widehat R(Q)_{db}\big)\gamma^p\epsilon^i\\
&-\frac{i}{8}T^{ab}\gamma^c\big(\overline{\widehat R(Q)}_c{}^{a}\gamma_{d}\gamma_{pq}\widehat R(Q)_{db}\big)\gamma^{pq}\epsilon^i\\
&-\frac{i}{4}T^{ab}\gamma^c\big(\overline{\widehat R(Q)}_a{}^d\gamma_c\widehat R(Q)_{db}\big)\epsilon^i\\
&-\frac{i}{4}T^{ab}\gamma^c\big(\overline{\widehat R(Q)}_a{}^d\gamma_c\gamma_p\widehat R(Q)_{db}\big)\gamma^p\epsilon^i\\
&+\frac{i}{8}T^{ab}\gamma^c\big(\overline{\widehat R(Q)}_a{}^d\gamma_c\gamma_{pq}\widehat R(Q)_{db}\big)\gamma^{pq}\epsilon^i\\
&-2i\eta_{ca}T^{ab}\gamma^c\big(\bar\chi\gamma^{d}\widehat R(Q)_{db}\big)\epsilon^i\\
&-2i\eta_{ca}T^{ab}\gamma^c\big(\bar\chi\gamma^{d}\gamma_p\widehat R(Q)_{db}\big)\gamma^p\epsilon^i\\
&+i\eta_{ca}T^{ab}\gamma^c\big(\bar\chi\gamma^{d}\gamma_{pq}\widehat R(Q)_{db}\big)\gamma^{pq}\epsilon^i\\
&+2i\eta_{cd}T^{ab}\gamma^c\big(\bar\chi\gamma^{a}\widehat R(Q)_{db}\big)\epsilon^i\\
&+2i\eta_{cd}T^{ab}\gamma^c\big(\bar\chi\gamma^{a}\gamma_p\widehat R(Q)_{db}\big)\gamma^p\epsilon^i\\
&-i\eta_{cd}T^{ab}\gamma^c\big(\bar\chi\gamma^{a}\gamma_{pq}\widehat R(Q)_{db}\big)\gamma^{pq}\epsilon^i\\
&-\frac{i}{4}T^{ab}\gamma^c\big(\overline{\widehat R(Q)}_c{}^{d}\gamma_{b}\widehat R(Q)_{ad}\big)\epsilon^i\\
&-\frac{i}{4}T^{ab}\gamma^c\big(\overline{\widehat R(Q)}_c{}^{d}\gamma_{b}\gamma_p\widehat R(Q)_{ad}\big)\gamma^p\epsilon^i\\
&+\frac{i}{8}T^{ab}\gamma^c\big(\overline{\widehat R(Q)}_c{}^{d}\gamma_{b}\gamma_{pq}\widehat R(Q)_{ad}\big)\gamma^{pq}\epsilon^i\\
&+\frac{i}{4}T^{ab}\gamma^c\big(\overline{\widehat R(Q)}_c{}^{b}\gamma_{d}\widehat R(Q)_{ad}\big)\epsilon^i\\
&+\frac{i}{4}T^{ab}\gamma^c\big(\overline{\widehat R(Q)}_c{}^{b}\gamma_{d}\gamma_p\widehat R(Q)_{ad}\big)\gamma^p\epsilon^i
\end{aligned}\tag{H167}
```

Continuation of the same right-hand side:

```math
\begin{aligned}
&-\frac{i}{8}T^{ab}\gamma^c\big(\overline{\widehat R(Q)}_c{}^{b}\gamma_{d}\gamma_{pq}\widehat R(Q)_{ad}\big)\gamma^{pq}\epsilon^i\\
&-\frac{i}{4}T^{ab}\gamma^c\big(\overline{\widehat R(Q)}_b{}^d\gamma_c\widehat R(Q)_{ad}\big)\epsilon^i\\
&-\frac{i}{4}T^{ab}\gamma^c\big(\overline{\widehat R(Q)}_b{}^d\gamma_c\gamma_p\widehat R(Q)_{ad}\big)\gamma^p\epsilon^i\\
&+\frac{i}{8}T^{ab}\gamma^c\big(\overline{\widehat R(Q)}_b{}^d\gamma_c\gamma_{pq}\widehat R(Q)_{ad}\big)\gamma^{pq}\epsilon^i\\
&-2i\eta_{cb}T^{ab}\gamma^c\big(\bar\chi\gamma^{d}\widehat R(Q)_{ad}\big)\epsilon^i\\
&-2i\eta_{cb}T^{ab}\gamma^c\big(\bar\chi\gamma^{d}\gamma_p\widehat R(Q)_{ad}\big)\gamma^p\epsilon^i\\
&+i\eta_{cb}T^{ab}\gamma^c\big(\bar\chi\gamma^{d}\gamma_{pq}\widehat R(Q)_{ad}\big)\gamma^{pq}\epsilon^i\\
&+2i\eta_{cd}T^{ab}\gamma^c\big(\bar\chi\gamma^{b}\widehat R(Q)_{ad}\big)\epsilon^i\\
&+2i\eta_{cd}T^{ab}\gamma^c\big(\bar\chi\gamma^{b}\gamma_p\widehat R(Q)_{ad}\big)\gamma^p\epsilon^i\\
&-i\eta_{cd}T^{ab}\gamma^c\big(\bar\chi\gamma^{b}\gamma_{pq}\widehat R(Q)_{ad}\big)\gamma^{pq}\epsilon^i\\
&+\frac{1}{2}\big(\bar\chi\gamma^{ab}\gamma_a\mathcal D^c\widehat R(Q)_{bc}\big)\epsilon^i\\
&+\frac{1}{2}\big(\bar\chi\gamma^{ab}\gamma_p\gamma_a\mathcal D^c\widehat R(Q)_{bc}\big)\gamma^p\epsilon^i\\
&-\frac{1}{4}\big(\bar\chi\gamma^{ab}\gamma_{pq}\gamma_a\mathcal D^c\widehat R(Q)_{bc}\big)\gamma^{pq}\epsilon^i\\
&+\frac{3}{32}\big(\overline{\widehat R(Q)}^{ab}\gamma_a\mathcal D^c\widehat R(Q)_{bc}\big)\epsilon^i\\
&+\frac{3}{32}\big(\overline{\widehat R(Q)}^{ab}\gamma_p\gamma_a\mathcal D^c\widehat R(Q)_{bc}\big)\gamma^p\epsilon^i\\
&-\frac{3}{64}\big(\overline{\widehat R(Q)}^{ab}\gamma_{pq}\gamma_a\mathcal D^c\widehat R(Q)_{bc}\big)\gamma^{pq}\epsilon^i\\
&+2iT^{ab}\eta^{cd}\gamma_a(\mathcal D_d\widehat C_{bc}{}^{ef})\gamma_{ef}\epsilon^i\\
&-16T^{ab}\eta^{cd}\gamma_a\gamma^{ef}(\mathcal D_d\mathcal D_{[b}T_{ef})\gamma_{c]}\epsilon^i
\end{aligned}\tag{H168}
```

Continuation of the same right-hand side:

```math
\begin{aligned}
&+\frac{16}{3}T^{ab}\eta^{cd}\gamma_a\gamma_{[c}\gamma^{ef}(\mathcal D_d\mathcal D_{b]}T_{ef})\epsilon^i\\
&+\frac{16}{3}T^{ab}\eta^{cd}\gamma_a\gamma_{[b}\gamma^g\gamma^{ef}(\mathcal D_d\mathcal D_gT_{ef})\gamma_{c]}\epsilon^i\\
&+\frac{16}{3}T^{ab}\eta^{cd}\gamma_a\gamma_{bc}\gamma_e\mathcal D_d\mathcal D_fT^{fe}\epsilon^i\\
&+2T^{ab}\eta^{cd}\gamma_a\widehat C_{bc}{}^{ef}\gamma_{ef}(\gamma\!\cdot\!T)\gamma_d\epsilon^i\\
&+16iT^{ab}\eta^{cd}\gamma_a\gamma^{ef}(\mathcal D_{[b}T_{ef})\gamma_{c]}(\gamma\!\cdot\!T)\gamma_d\epsilon^i\\
&-\frac{16i}{3}T^{ab}\eta^{cd}\gamma_a\gamma_{[c}\gamma^{ef}(\mathcal D_{b]}T_{ef})(\gamma\!\cdot\!T)\gamma_d\epsilon^i\\
&-\frac{16i}{3}T^{ab}\eta^{cd}\gamma_a\gamma_{[b}\gamma^g\gamma^{ef}(\mathcal D_gT_{ef})\gamma_{c]}(\gamma\!\cdot\!T)\gamma_d\epsilon^i\\
&-\frac{16i}{3}T^{ab}\eta^{cd}\gamma_a\gamma_{bc}\gamma_e(\mathcal D_fT^{fe})(\gamma\!\cdot\!T)\gamma_d\epsilon^i\\
&+\frac{64i}{3}T^{ab}\eta^{cd}\gamma_aT_{bc}\gamma^t\gamma^{rs}(\mathcal D_tT_{rs})\gamma_d\epsilon^i\\
&-\frac{64i}{3}T^{ab}\eta^{cd}\gamma_aT_{bc}\gamma^{rs}(\mathcal D_dT_{rs})\epsilon^i\\
&+\frac{64i}{3}T^{ab}\eta^{cd}\gamma_aT_{bc}\gamma_d\gamma^s(\mathcal D^rT_{rs})\epsilon^i\\
&+64T^{ab}\eta^{cd}\gamma_aT_{bc}\gamma_{drstu}T^{rs}T^{tu}\epsilon^i\\
&-512T^{ab}\eta^{cd}\gamma_aT_{bc}\gamma_rT^{rs}T_{ds}\epsilon^i\\
&+128T^{ab}\eta^{cd}\gamma_aT_{bc}\gamma_dT^2\epsilon^i\\
&-\frac{128i}{9}T^{ab}\eta^{cd}\gamma_aT_{[b}{}^e\gamma_{c]e}\gamma^t\gamma^{rs}(\mathcal D_tT_{rs})\gamma_d\epsilon^i\\
&+\frac{128i}{9}T^{ab}\eta^{cd}\gamma_aT_{[b}{}^e\gamma_{c]e}\gamma^{rs}(\mathcal D_dT_{rs})\epsilon^i\\
&-\frac{128i}{9}T^{ab}\eta^{cd}\gamma_aT_{[b}{}^e\gamma_{c]e}\gamma_d\gamma^s(\mathcal D^rT_{rs})\epsilon^i\\
&-\frac{128}{3}T^{ab}\eta^{cd}\gamma_aT_{[b}{}^e\gamma_{c]e}\gamma_{drstu}T^{rs}T^{tu}\epsilon^i
\end{aligned}\tag{H169}
```

Continuation of the same right-hand side:

```math
\begin{aligned}
&+\frac{1024}{3}T^{ab}\eta^{cd}\gamma_aT_{[b}{}^e\gamma_{c]e}\gamma_rT^{rs}T_{ds}\epsilon^i\\
&-\frac{256}{3}T^{ab}\eta^{cd}\gamma_aT_{[b}{}^e\gamma_{c]e}\gamma_dT^2\epsilon^i\\
&-\frac{32i}{9}T^{ab}\eta^{cd}\gamma_a\gamma_{bcef}T^{ef}\gamma^t\gamma^{rs}(\mathcal D_tT_{rs})\gamma_d\epsilon^i\\
&+\frac{32i}{9}T^{ab}\eta^{cd}\gamma_a\gamma_{bcef}T^{ef}\gamma^{rs}(\mathcal D_dT_{rs})\epsilon^i\\
&-\frac{32i}{9}T^{ab}\eta^{cd}\gamma_a\gamma_{bcef}T^{ef}\gamma_d\gamma^s(\mathcal D^rT_{rs})\epsilon^i\\
&-\frac{32}{3}T^{ab}\eta^{cd}\gamma_a\gamma_{bcef}T^{ef}\gamma_{drstu}T^{rs}T^{tu}\epsilon^i\\
&+\frac{256}{3}T^{ab}\eta^{cd}\gamma_a\gamma_{bcef}T^{ef}\gamma_rT^{rs}T_{ds}\epsilon^i\\
&-\frac{64}{3}T^{ab}\eta^{cd}\gamma_a\gamma_{bcef}T^{ef}\gamma_dT^2\epsilon^i\\
&+9iT^{ab}\eta^{cd}\gamma_a\big(\bar\chi\gamma_d\widehat R(Q)_{bc}\big)\epsilon^i\\
&+9iT^{ab}\eta^{cd}\gamma_a\big(\bar\chi\gamma_d\gamma_p\widehat R(Q)_{bc}\big)\gamma^p\epsilon^i\\
&-\frac{9i}{2}T^{ab}\eta^{cd}\gamma_a\big(\bar\chi\gamma_d\gamma_{pq}\widehat R(Q)_{bc}\big)\gamma^{pq}\epsilon^i\\
&-\frac{i}{16}T^{ab}\eta^{cd}\gamma_a\gamma_{ef}\big(\overline{\widehat R(Q)}_d{}^{f}\gamma^{e}\widehat R(Q)_{bc}\big)\epsilon^i\\
&-\frac{i}{16}T^{ab}\eta^{cd}\gamma_a\gamma_{ef}\big(\overline{\widehat R(Q)}_d{}^{f}\gamma^{e}\gamma_p\widehat R(Q)_{bc}\big)\gamma^p\epsilon^i\\
&+\frac{i}{32}T^{ab}\eta^{cd}\gamma_a\gamma_{ef}\big(\overline{\widehat R(Q)}_d{}^{f}\gamma^{e}\gamma_{pq}\widehat R(Q)_{bc}\big)\gamma^{pq}\epsilon^i\\
&+\frac{i}{16}T^{ab}\eta^{cd}\gamma_a\gamma_{ef}\big(\overline{\widehat R(Q)}_d{}^{e}\gamma^{f}\widehat R(Q)_{bc}\big)\epsilon^i\\
&+\frac{i}{16}T^{ab}\eta^{cd}\gamma_a\gamma_{ef}\big(\overline{\widehat R(Q)}_d{}^{e}\gamma^{f}\gamma_p\widehat R(Q)_{bc}\big)\gamma^p\epsilon^i\\
&-\frac{i}{32}T^{ab}\eta^{cd}\gamma_a\gamma_{ef}\big(\overline{\widehat R(Q)}_d{}^{e}\gamma^{f}\gamma_{pq}\widehat R(Q)_{bc}\big)\gamma^{pq}\epsilon^i\\
&-\frac{i}{16}T^{ab}\eta^{cd}\gamma_a\gamma_{ef}\big(\overline{\widehat R(Q)}^{ef}\gamma_d\widehat R(Q)_{bc}\big)\epsilon^i
\end{aligned}\tag{H170}
```

Continuation of the same right-hand side:

```math
\begin{aligned}
&-\frac{i}{16}T^{ab}\eta^{cd}\gamma_a\gamma_{ef}\big(\overline{\widehat R(Q)}^{ef}\gamma_d\gamma_p\widehat R(Q)_{bc}\big)\gamma^p\epsilon^i\\
&+\frac{i}{32}T^{ab}\eta^{cd}\gamma_a\gamma_{ef}\big(\overline{\widehat R(Q)}^{ef}\gamma_d\gamma_{pq}\widehat R(Q)_{bc}\big)\gamma^{pq}\epsilon^i\\
&-\frac{i}{2}\delta_d{}^{e}T^{ab}\eta^{cd}\gamma_a\gamma_{ef}\big(\bar\chi\gamma^{f}\widehat R(Q)_{bc}\big)\epsilon^i\\
&-\frac{i}{2}\delta_d{}^{e}T^{ab}\eta^{cd}\gamma_a\gamma_{ef}\big(\bar\chi\gamma^{f}\gamma_p\widehat R(Q)_{bc}\big)\gamma^p\epsilon^i\\
&+\frac{i}{4}\delta_d{}^{e}T^{ab}\eta^{cd}\gamma_a\gamma_{ef}\big(\bar\chi\gamma^{f}\gamma_{pq}\widehat R(Q)_{bc}\big)\gamma^{pq}\epsilon^i\\
&+\frac{i}{2}\delta_d{}^{f}T^{ab}\eta^{cd}\gamma_a\gamma_{ef}\big(\bar\chi\gamma^{e}\widehat R(Q)_{bc}\big)\epsilon^i\\
&+\frac{i}{2}\delta_d{}^{f}T^{ab}\eta^{cd}\gamma_a\gamma_{ef}\big(\bar\chi\gamma^{e}\gamma_p\widehat R(Q)_{bc}\big)\gamma^p\epsilon^i\\
&-\frac{i}{4}\delta_d{}^{f}T^{ab}\eta^{cd}\gamma_a\gamma_{ef}\big(\bar\chi\gamma^{e}\gamma_{pq}\widehat R(Q)_{bc}\big)\gamma^{pq}\epsilon^i\\
&-\frac{i}{4}T^{ab}\eta^{cd}\gamma_a\big(\overline{\widehat R(Q)}_d{}^{e}\gamma_{b}\widehat R(Q)_{ec}\big)\epsilon^i\\
&-\frac{i}{4}T^{ab}\eta^{cd}\gamma_a\big(\overline{\widehat R(Q)}_d{}^{e}\gamma_{b}\gamma_p\widehat R(Q)_{ec}\big)\gamma^p\epsilon^i\\
&+\frac{i}{8}T^{ab}\eta^{cd}\gamma_a\big(\overline{\widehat R(Q)}_d{}^{e}\gamma_{b}\gamma_{pq}\widehat R(Q)_{ec}\big)\gamma^{pq}\epsilon^i\\
&+\frac{i}{4}T^{ab}\eta^{cd}\gamma_a\big(\overline{\widehat R(Q)}_d{}^{b}\gamma_{e}\widehat R(Q)_{ec}\big)\epsilon^i\\
&+\frac{i}{4}T^{ab}\eta^{cd}\gamma_a\big(\overline{\widehat R(Q)}_d{}^{b}\gamma_{e}\gamma_p\widehat R(Q)_{ec}\big)\gamma^p\epsilon^i\\
&-\frac{i}{8}T^{ab}\eta^{cd}\gamma_a\big(\overline{\widehat R(Q)}_d{}^{b}\gamma_{e}\gamma_{pq}\widehat R(Q)_{ec}\big)\gamma^{pq}\epsilon^i\\
&-\frac{i}{4}T^{ab}\eta^{cd}\gamma_a\big(\overline{\widehat R(Q)}_b{}^e\gamma_d\widehat R(Q)_{ec}\big)\epsilon^i\\
&-\frac{i}{4}T^{ab}\eta^{cd}\gamma_a\big(\overline{\widehat R(Q)}_b{}^e\gamma_d\gamma_p\widehat R(Q)_{ec}\big)\gamma^p\epsilon^i\\
&+\frac{i}{8}T^{ab}\eta^{cd}\gamma_a\big(\overline{\widehat R(Q)}_b{}^e\gamma_d\gamma_{pq}\widehat R(Q)_{ec}\big)\gamma^{pq}\epsilon^i\\
&-2i\eta_{db}T^{ab}\eta^{cd}\gamma_a\big(\bar\chi\gamma^{e}\widehat R(Q)_{ec}\big)\epsilon^i
\end{aligned}\tag{H171}
```

Continuation of the same right-hand side:

```math
\begin{aligned}
&-2i\eta_{db}T^{ab}\eta^{cd}\gamma_a\big(\bar\chi\gamma^{e}\gamma_p\widehat R(Q)_{ec}\big)\gamma^p\epsilon^i\\
&+i\eta_{db}T^{ab}\eta^{cd}\gamma_a\big(\bar\chi\gamma^{e}\gamma_{pq}\widehat R(Q)_{ec}\big)\gamma^{pq}\epsilon^i\\
&+2i\eta_{de}T^{ab}\eta^{cd}\gamma_a\big(\bar\chi\gamma^{b}\widehat R(Q)_{ec}\big)\epsilon^i\\
&+2i\eta_{de}T^{ab}\eta^{cd}\gamma_a\big(\bar\chi\gamma^{b}\gamma_p\widehat R(Q)_{ec}\big)\gamma^p\epsilon^i\\
&-i\eta_{de}T^{ab}\eta^{cd}\gamma_a\big(\bar\chi\gamma^{b}\gamma_{pq}\widehat R(Q)_{ec}\big)\gamma^{pq}\epsilon^i\\
&-\frac{i}{4}T^{ab}\eta^{cd}\gamma_a\big(\overline{\widehat R(Q)}_d{}^{e}\gamma_{c}\widehat R(Q)_{be}\big)\epsilon^i\\
&-\frac{i}{4}T^{ab}\eta^{cd}\gamma_a\big(\overline{\widehat R(Q)}_d{}^{e}\gamma_{c}\gamma_p\widehat R(Q)_{be}\big)\gamma^p\epsilon^i\\
&+\frac{i}{8}T^{ab}\eta^{cd}\gamma_a\big(\overline{\widehat R(Q)}_d{}^{e}\gamma_{c}\gamma_{pq}\widehat R(Q)_{be}\big)\gamma^{pq}\epsilon^i\\
&+\frac{i}{4}T^{ab}\eta^{cd}\gamma_a\big(\overline{\widehat R(Q)}_d{}^{c}\gamma_{e}\widehat R(Q)_{be}\big)\epsilon^i\\
&+\frac{i}{4}T^{ab}\eta^{cd}\gamma_a\big(\overline{\widehat R(Q)}_d{}^{c}\gamma_{e}\gamma_p\widehat R(Q)_{be}\big)\gamma^p\epsilon^i\\
&-\frac{i}{8}T^{ab}\eta^{cd}\gamma_a\big(\overline{\widehat R(Q)}_d{}^{c}\gamma_{e}\gamma_{pq}\widehat R(Q)_{be}\big)\gamma^{pq}\epsilon^i\\
&-\frac{i}{4}T^{ab}\eta^{cd}\gamma_a\big(\overline{\widehat R(Q)}_c{}^e\gamma_d\widehat R(Q)_{be}\big)\epsilon^i\\
&-\frac{i}{4}T^{ab}\eta^{cd}\gamma_a\big(\overline{\widehat R(Q)}_c{}^e\gamma_d\gamma_p\widehat R(Q)_{be}\big)\gamma^p\epsilon^i\\
&+\frac{i}{8}T^{ab}\eta^{cd}\gamma_a\big(\overline{\widehat R(Q)}_c{}^e\gamma_d\gamma_{pq}\widehat R(Q)_{be}\big)\gamma^{pq}\epsilon^i\\
&-2i\eta_{dc}T^{ab}\eta^{cd}\gamma_a\big(\bar\chi\gamma^{e}\widehat R(Q)_{be}\big)\epsilon^i\\
&-2i\eta_{dc}T^{ab}\eta^{cd}\gamma_a\big(\bar\chi\gamma^{e}\gamma_p\widehat R(Q)_{be}\big)\gamma^p\epsilon^i\\
&+i\eta_{dc}T^{ab}\eta^{cd}\gamma_a\big(\bar\chi\gamma^{e}\gamma_{pq}\widehat R(Q)_{be}\big)\gamma^{pq}\epsilon^i\\
&+2i\eta_{de}T^{ab}\eta^{cd}\gamma_a\big(\bar\chi\gamma^{c}\widehat R(Q)_{be}\big)\epsilon^i
\end{aligned}\tag{H172}
```

Continuation of the same right-hand side:

```math
\begin{aligned}
&+2i\eta_{de}T^{ab}\eta^{cd}\gamma_a\big(\bar\chi\gamma^{c}\gamma_p\widehat R(Q)_{be}\big)\gamma^p\epsilon^i\\
&-i\eta_{de}T^{ab}\eta^{cd}\gamma_a\big(\bar\chi\gamma^{c}\gamma_{pq}\widehat R(Q)_{be}\big)\gamma^{pq}\epsilon^i\\
&-\frac{16i}{3}\gamma^{ab} \gamma^c D(\mathcal D_aT_{bc})\epsilon^i\\
&+\frac{8}{3}\gamma^{ab} \gamma^c \gamma^{de} \gamma^{f}(\mathcal D_fT_{de})(\mathcal D_aT_{bc})\epsilon^i\\
&-\frac{8}{3}\gamma^{ab} \gamma^c \gamma^{d}(\mathcal D^eT_{de})(\mathcal D_aT_{bc})\epsilon^i\\
&+\frac{16i}{3}\gamma^{ab} \gamma^c \gamma^{rstu}T_{rs}T_{tu}(\mathcal D_aT_{bc})\epsilon^i\\
&-\frac{32i}{9}\gamma^{ab} \gamma^c T^2(\mathcal D_aT_{bc})\epsilon^i\\
&-\frac{4}{3}\gamma^{ab}\gamma^c\big(\overline{\mathcal D_a\chi}\gamma_{bc}\chi\big)\epsilon^i\\
&-\frac{4}{3}\gamma^{ab}\gamma^c\big(\overline{\mathcal D_a\chi}\gamma_{bc}\gamma_p\chi\big)\gamma^p\epsilon^i\\
&+\frac{2}{3}\gamma^{ab}\gamma^c\big(\overline{\mathcal D_a\chi}\gamma_{bc}\gamma_{pq}\chi\big)\gamma^{pq}\epsilon^i\\
&-\frac{1}{4}\gamma^{ab}\gamma^c\big(\overline{\mathcal D_a\widehat R(Q)_{bc}}\chi\big)\epsilon^i\\
&-\frac{1}{4}\gamma^{ab}\gamma^c\big(\overline{\mathcal D_a\widehat R(Q)_{bc}}\gamma_p\chi\big)\gamma^p\epsilon^i\\
&+\frac{1}{8}\gamma^{ab}\gamma^c\big(\overline{\mathcal D_a\widehat R(Q)_{bc}}\gamma_{pq}\chi\big)\gamma^{pq}\epsilon^i\\
&+\frac{4i}{3}\gamma^{ab}\gamma^c\big(\bar\chi\gamma_{bc}(\gamma\!\cdot\!T)\gamma_a\chi\big)\epsilon^i\\
&+\frac{4i}{3}\gamma^{ab}\gamma^c\big(\bar\chi\gamma_{bc}(\gamma\!\cdot\!T)\gamma_a\gamma_p\chi\big)\gamma^p\epsilon^i\\
&-\frac{2i}{3}\gamma^{ab}\gamma^c\big(\bar\chi\gamma_{bc}(\gamma\!\cdot\!T)\gamma_a\gamma_{pq}\chi\big)\gamma^{pq}\epsilon^i\\
&+\frac{i}{4}\gamma^{ab}\gamma^c\big(\overline{\widehat R(Q)}_{bc}(\gamma\!\cdot\!T)\gamma_a\chi\big)\epsilon^i\\
&+\frac{i}{4}\gamma^{ab}\gamma^c\big(\overline{\widehat R(Q)}_{bc}(\gamma\!\cdot\!T)\gamma_a\gamma_p\chi\big)\gamma^p\epsilon^i
\end{aligned}\tag{H173}
```

Continuation of the same right-hand side:

```math
\begin{aligned}
&-\frac{i}{8}\gamma^{ab}\gamma^c\big(\overline{\widehat R(Q)}_{bc}(\gamma\!\cdot\!T)\gamma_a\gamma_{pq}\chi\big)\gamma^{pq}\epsilon^i\\
&-\frac{16i}{3}T_{bc}\gamma^{ab}\gamma^c\big(\bar\chi\gamma_a\chi\big)\epsilon^i\\
&-\frac{16i}{3}T_{bc}\gamma^{ab}\gamma^c\big(\bar\chi\gamma_a\gamma_p\chi\big)\gamma^p\epsilon^i\\
&+\frac{8i}{3}T_{bc}\gamma^{ab}\gamma^c\big(\bar\chi\gamma_a\gamma_{pq}\chi\big)\gamma^{pq}\epsilon^i\\
&+\frac{2i}{3}T_{dc}\gamma^{ab}\gamma^c\big(\overline{\widehat R(Q)}_a{}^{d}\gamma_{b}\chi\big)\epsilon^i\\
&+\frac{2i}{3}T_{dc}\gamma^{ab}\gamma^c\big(\overline{\widehat R(Q)}_a{}^{d}\gamma_{b}\gamma_p\chi\big)\gamma^p\epsilon^i\\
&-\frac{i}{3}T_{dc}\gamma^{ab}\gamma^c\big(\overline{\widehat R(Q)}_a{}^{d}\gamma_{b}\gamma_{pq}\chi\big)\gamma^{pq}\epsilon^i\\
&-\frac{2i}{3}T_{dc}\gamma^{ab}\gamma^c\big(\overline{\widehat R(Q)}_a{}^{b}\gamma_{d}\chi\big)\epsilon^i\\
&-\frac{2i}{3}T_{dc}\gamma^{ab}\gamma^c\big(\overline{\widehat R(Q)}_a{}^{b}\gamma_{d}\gamma_p\chi\big)\gamma^p\epsilon^i\\
&+\frac{i}{3}T_{dc}\gamma^{ab}\gamma^c\big(\overline{\widehat R(Q)}_a{}^{b}\gamma_{d}\gamma_{pq}\chi\big)\gamma^{pq}\epsilon^i\\
&+\frac{2i}{3}T_{dc}\gamma^{ab}\gamma^c\big(\overline{\widehat R(Q)}_b{}^d\gamma_a\chi\big)\epsilon^i\\
&+\frac{2i}{3}T_{dc}\gamma^{ab}\gamma^c\big(\overline{\widehat R(Q)}_b{}^d\gamma_a\gamma_p\chi\big)\gamma^p\epsilon^i\\
&-\frac{i}{3}T_{dc}\gamma^{ab}\gamma^c\big(\overline{\widehat R(Q)}_b{}^d\gamma_a\gamma_{pq}\chi\big)\gamma^{pq}\epsilon^i\\
&+\frac{16i}{3}\eta_{ab}T_{dc}\gamma^{ab}\gamma^c\big(\bar\chi\gamma^{d}\chi\big)\epsilon^i\\
&+\frac{16i}{3}\eta_{ab}T_{dc}\gamma^{ab}\gamma^c\big(\bar\chi\gamma^{d}\gamma_p\chi\big)\gamma^p\epsilon^i\\
&-\frac{8i}{3}\eta_{ab}T_{dc}\gamma^{ab}\gamma^c\big(\bar\chi\gamma^{d}\gamma_{pq}\chi\big)\gamma^{pq}\epsilon^i\\
&-\frac{16i}{3}\eta_{ad}T_{dc}\gamma^{ab}\gamma^c\big(\bar\chi\gamma^{b}\chi\big)\epsilon^i\\
&-\frac{16i}{3}\eta_{ad}T_{dc}\gamma^{ab}\gamma^c\big(\bar\chi\gamma^{b}\gamma_p\chi\big)\gamma^p\epsilon^i
\end{aligned}\tag{H174}
```

Continuation of the same right-hand side:

```math
\begin{aligned}
&+\frac{8i}{3}\eta_{ad}T_{dc}\gamma^{ab}\gamma^c\big(\bar\chi\gamma^{b}\gamma_{pq}\chi\big)\gamma^{pq}\epsilon^i\\
&+\frac{2i}{3}T_{bd}\gamma^{ab}\gamma^c\big(\overline{\widehat R(Q)}_a{}^{d}\gamma_{c}\chi\big)\epsilon^i\\
&+\frac{2i}{3}T_{bd}\gamma^{ab}\gamma^c\big(\overline{\widehat R(Q)}_a{}^{d}\gamma_{c}\gamma_p\chi\big)\gamma^p\epsilon^i\\
&-\frac{i}{3}T_{bd}\gamma^{ab}\gamma^c\big(\overline{\widehat R(Q)}_a{}^{d}\gamma_{c}\gamma_{pq}\chi\big)\gamma^{pq}\epsilon^i\\
&-\frac{2i}{3}T_{bd}\gamma^{ab}\gamma^c\big(\overline{\widehat R(Q)}_a{}^{c}\gamma_{d}\chi\big)\epsilon^i\\
&-\frac{2i}{3}T_{bd}\gamma^{ab}\gamma^c\big(\overline{\widehat R(Q)}_a{}^{c}\gamma_{d}\gamma_p\chi\big)\gamma^p\epsilon^i\\
&+\frac{i}{3}T_{bd}\gamma^{ab}\gamma^c\big(\overline{\widehat R(Q)}_a{}^{c}\gamma_{d}\gamma_{pq}\chi\big)\gamma^{pq}\epsilon^i\\
&+\frac{2i}{3}T_{bd}\gamma^{ab}\gamma^c\big(\overline{\widehat R(Q)}_c{}^d\gamma_a\chi\big)\epsilon^i\\
&+\frac{2i}{3}T_{bd}\gamma^{ab}\gamma^c\big(\overline{\widehat R(Q)}_c{}^d\gamma_a\gamma_p\chi\big)\gamma^p\epsilon^i\\
&-\frac{i}{3}T_{bd}\gamma^{ab}\gamma^c\big(\overline{\widehat R(Q)}_c{}^d\gamma_a\gamma_{pq}\chi\big)\gamma^{pq}\epsilon^i\\
&+\frac{16i}{3}\eta_{ac}T_{bd}\gamma^{ab}\gamma^c\big(\bar\chi\gamma^{d}\chi\big)\epsilon^i\\
&+\frac{16i}{3}\eta_{ac}T_{bd}\gamma^{ab}\gamma^c\big(\bar\chi\gamma^{d}\gamma_p\chi\big)\gamma^p\epsilon^i\\
&-\frac{8i}{3}\eta_{ac}T_{bd}\gamma^{ab}\gamma^c\big(\bar\chi\gamma^{d}\gamma_{pq}\chi\big)\gamma^{pq}\epsilon^i\\
&-\frac{16i}{3}\eta_{ad}T_{bd}\gamma^{ab}\gamma^c\big(\bar\chi\gamma^{c}\chi\big)\epsilon^i\\
&-\frac{16i}{3}\eta_{ad}T_{bd}\gamma^{ab}\gamma^c\big(\bar\chi\gamma^{c}\gamma_p\chi\big)\gamma^p\epsilon^i\\
&+\frac{8i}{3}\eta_{ad}T_{bd}\gamma^{ab}\gamma^c\big(\bar\chi\gamma^{c}\gamma_{pq}\chi\big)\gamma^{pq}\epsilon^i\\
&-\frac{128i}{9}T^{ab}\big(\bar\chi\gamma_{ab}\chi\big)\epsilon^i\\
&-\frac{128i}{9}T^{ab}\big(\bar\chi\gamma_{ab}\gamma_p\chi\big)\gamma^p\epsilon^i
\end{aligned}\tag{H175}
```

Continuation of the same right-hand side:

```math
\begin{aligned}
&+\frac{64i}{9}T^{ab}\big(\bar\chi\gamma_{ab}\gamma_{pq}\chi\big)\gamma^{pq}\epsilon^i\\
&-\frac{8i}{3}T^{ab}\big(\overline{\widehat R(Q)}_{ab}\chi\big)\epsilon^i\\
&-\frac{8i}{3}T^{ab}\big(\overline{\widehat R(Q)}_{ab}\gamma_p\chi\big)\gamma^p\epsilon^i\\
&+\frac{4i}{3}T^{ab}\big(\overline{\widehat R(Q)}_{ab}\gamma_{pq}\chi\big)\gamma^{pq}\epsilon^i\\
&+\frac{256}{9}DT^2\epsilon^i\\
&+\frac{128i}{9}\gamma^{ab} \gamma^{c}(\mathcal D_cT_{ab})T^2\epsilon^i\\
&-\frac{128i}{9}\gamma^{a}(\mathcal D^bT_{ab})T^2\epsilon^i\\
&-\frac{256}{9}T^2\gamma^{rstu}T_{rs}T_{tu}\epsilon^i\\
&+\frac{512}{27}{T^2}^2\epsilon^i\\
&+\frac{8}{3}\big(\bar\chi\gamma^{ab}\gamma_a \mathcal D_b\chi\big)\epsilon^i\\
&+\frac{8}{3}\big(\bar\chi\gamma^{ab}\gamma_p\gamma_a \mathcal D_b\chi\big)\gamma^p\epsilon^i\\
&-\frac{4}{3}\big(\bar\chi\gamma^{ab}\gamma_{pq}\gamma_a \mathcal D_b\chi\big)\gamma^{pq}\epsilon^i\\
&+\frac{1}{2}\big(\overline{\widehat R(Q)}^{ab}\gamma_a \mathcal D_b\chi\big)\epsilon^i\\
&+\frac{1}{2}\big(\overline{\widehat R(Q)}^{ab}\gamma_p\gamma_a \mathcal D_b\chi\big)\gamma^p\epsilon^i\\
&-\frac{1}{4}\big(\overline{\widehat R(Q)}^{ab}\gamma_{pq}\gamma_a \mathcal D_b\chi\big)\gamma^{pq}\epsilon^i\\
&+\frac{32i}{3}T^{ab}\gamma_a\mathcal D_bD\epsilon^i\\
&-\frac{16}{3}T^{ab}\gamma_a\gamma^{de}\gamma^f\mathcal D_b\mathcal D_fT_{de}\epsilon^i\\
&+\frac{16}{3}T^{ab}\gamma_a\gamma^d\mathcal D_b\mathcal D^eT_{de}\epsilon^i
\end{aligned}\tag{H176}
```

Continuation of the same right-hand side:

```math
\begin{aligned}
&-\frac{32i}{3}T^{ab}\gamma_a\gamma^{defg}(\mathcal D_bT_{de})T_{fg}\epsilon^i\\
&-\frac{32i}{3}T^{ab}\gamma_a\gamma^{defg}T_{de}(\mathcal D_bT_{fg})\epsilon^i\\
&+\frac{128i}{9}T^{ab}\gamma_aT^{de}\mathcal D_bT_{de}\epsilon^i\\
&+\frac{32}{3}T^{ab}\gamma_aD(\gamma\!\cdot\!T)\gamma_b\epsilon^i\\
&+\frac{16i}{3}T^{ab}\gamma_a\gamma^{de}\gamma^f(\mathcal D_fT_{de})(\gamma\!\cdot\!T)\gamma_b\epsilon^i\\
&-\frac{16i}{3}T^{ab}\gamma_a\gamma^d(\mathcal D^eT_{de})(\gamma\!\cdot\!T)\gamma_b\epsilon^i\\
&-\frac{32}{3}T^{ab}\gamma_a\gamma^{defg}T_{de}T_{fg}(\gamma\!\cdot\!T)\gamma_b\epsilon^i\\
&+\frac{64}{9}T^{ab}\gamma_aT^2(\gamma\!\cdot\!T)\gamma_b\epsilon^i\\
&-\frac{32i}{9}T^{ab}\gamma_a(\gamma\!\cdot\!T)\gamma^f\gamma^{de}(\mathcal D_fT_{de})\gamma_b\epsilon^i\\
&+\frac{32i}{9}T^{ab}\gamma_a(\gamma\!\cdot\!T)\gamma^{de}(\mathcal D_bT_{de})\epsilon^i\\
&-\frac{32i}{9}T^{ab}\gamma_a(\gamma\!\cdot\!T)\gamma_b\gamma^e(\mathcal D^dT_{de})\epsilon^i\\
&-\frac{32}{3}T^{ab}\gamma_a(\gamma\!\cdot\!T)\gamma_{bdefg}T^{de}T^{fg}\epsilon^i\\
&+\frac{256}{3}T^{ab}\gamma_a(\gamma\!\cdot\!T)\gamma_dT^{de}T_{be}\epsilon^i\\
&-\frac{64}{3}T^{ab}\gamma_a(\gamma\!\cdot\!T)\gamma_bT^2\epsilon^i\\
&+48iT^{ab}\gamma_a\big(\bar\chi\gamma_b\chi\big)\epsilon^i\\
&+48iT^{ab}\gamma_a\big(\bar\chi\gamma_b\gamma_p\chi\big)\gamma^p\epsilon^i\\
&-24iT^{ab}\gamma_a\big(\bar\chi\gamma_b\gamma_{pq}\chi\big)\gamma^{pq}\epsilon^i\\
&-\frac{i}{3}T^{ab}\gamma_a\gamma_{de}\big(\overline{\widehat R(Q)}_b{}^{e}\gamma^{d}\chi\big)\epsilon^i
\end{aligned}\tag{H177}
```

Continuation of the same right-hand side:

```math
\begin{aligned}
&-\frac{i}{3}T^{ab}\gamma_a\gamma_{de}\big(\overline{\widehat R(Q)}_b{}^{e}\gamma^{d}\gamma_p\chi\big)\gamma^p\epsilon^i\\
&+\frac{i}{6}T^{ab}\gamma_a\gamma_{de}\big(\overline{\widehat R(Q)}_b{}^{e}\gamma^{d}\gamma_{pq}\chi\big)\gamma^{pq}\epsilon^i\\
&+\frac{i}{3}T^{ab}\gamma_a\gamma_{de}\big(\overline{\widehat R(Q)}_b{}^{d}\gamma^{e}\chi\big)\epsilon^i\\
&+\frac{i}{3}T^{ab}\gamma_a\gamma_{de}\big(\overline{\widehat R(Q)}_b{}^{d}\gamma^{e}\gamma_p\chi\big)\gamma^p\epsilon^i\\
&-\frac{i}{6}T^{ab}\gamma_a\gamma_{de}\big(\overline{\widehat R(Q)}_b{}^{d}\gamma^{e}\gamma_{pq}\chi\big)\gamma^{pq}\epsilon^i\\
&-\frac{i}{3}T^{ab}\gamma_a\gamma_{de}\big(\overline{\widehat R(Q)}^{de}\gamma_b\chi\big)\epsilon^i\\
&-\frac{i}{3}T^{ab}\gamma_a\gamma_{de}\big(\overline{\widehat R(Q)}^{de}\gamma_b\gamma_p\chi\big)\gamma^p\epsilon^i\\
&+\frac{i}{6}T^{ab}\gamma_a\gamma_{de}\big(\overline{\widehat R(Q)}^{de}\gamma_b\gamma_{pq}\chi\big)\gamma^{pq}\epsilon^i\\
&-\frac{8i}{3}\delta_b{}^{d}T^{ab}\gamma_a\gamma_{de}\big(\bar\chi\gamma^{e}\chi\big)\epsilon^i\\
&-\frac{8i}{3}\delta_b{}^{d}T^{ab}\gamma_a\gamma_{de}\big(\bar\chi\gamma^{e}\gamma_p\chi\big)\gamma^p\epsilon^i\\
&+\frac{4i}{3}\delta_b{}^{d}T^{ab}\gamma_a\gamma_{de}\big(\bar\chi\gamma^{e}\gamma_{pq}\chi\big)\gamma^{pq}\epsilon^i\\
&+\frac{8i}{3}\delta_b{}^{e}T^{ab}\gamma_a\gamma_{de}\big(\bar\chi\gamma^{d}\chi\big)\epsilon^i\\
&+\frac{8i}{3}\delta_b{}^{e}T^{ab}\gamma_a\gamma_{de}\big(\bar\chi\gamma^{d}\gamma_p\chi\big)\gamma^p\epsilon^i\\
&-\frac{4i}{3}\delta_b{}^{e}T^{ab}\gamma_a\gamma_{de}\big(\bar\chi\gamma^{d}\gamma_{pq}\chi\big)\gamma^{pq}\epsilon^i\\
&+\frac{2}{3}\gamma_{ab} \gamma_{ef}\widehat C_{cd}{}^{ef}T^{ab}T^{cd}\epsilon^i\\
&+\frac{16i}{3}\gamma_{ab} \gamma^{ef} \gamma_{d]}(\mathcal D_{[c}T_{ef})T^{ab}T^{cd}\epsilon^i\\
&-\frac{16i}{9}\gamma_{ab} \gamma_{[d} \gamma^{ef}(\mathcal D_{c]}T_{ef})T^{ab}T^{cd}\epsilon^i\\
&-\frac{16i}{9}\gamma_{ab} \gamma_{[c} \gamma^{g} \gamma^{ef} \gamma_{d]}(\mathcal D_gT_{ef})T^{ab}T^{cd}\epsilon^i
\end{aligned}\tag{H178}
```

Continuation of the same right-hand side:

```math
\begin{aligned}
&-\frac{16i}{9}\gamma_{ab} \gamma_{cd} \gamma^{e}(\mathcal D^fT_{fe})T^{ab}T^{cd}\epsilon^i\\
&-\frac{i}{6}T^{cd}\big(\bar\chi\gamma^{ab}\gamma_{ab}\widehat R(Q)_{cd}\big)\epsilon^i\\
&-\frac{i}{6}T^{cd}\big(\bar\chi\gamma^{ab}\gamma_p\gamma_{ab}\widehat R(Q)_{cd}\big)\gamma^p\epsilon^i\\
&+\frac{i}{12}T^{cd}\big(\bar\chi\gamma^{ab}\gamma_{pq}\gamma_{ab}\widehat R(Q)_{cd}\big)\gamma^{pq}\epsilon^i\\
&-\frac{i}{32}T^{cd}\big(\overline{\widehat R(Q)}^{ab}\gamma_{ab}\widehat R(Q)_{cd}\big)\epsilon^i\\
&-\frac{i}{32}T^{cd}\big(\overline{\widehat R(Q)}^{ab}\gamma_p\gamma_{ab}\widehat R(Q)_{cd}\big)\gamma^p\epsilon^i\\
&+\frac{i}{64}T^{cd}\big(\overline{\widehat R(Q)}^{ab}\gamma_{pq}\gamma_{ab}\widehat R(Q)_{cd}\big)\gamma^{pq}\epsilon^i\\
&-\frac{i}{6}T^{ab}\big(\bar\chi\gamma^{cd}\gamma_{ab}\widehat R(Q)_{cd}\big)\epsilon^i\\
&-\frac{i}{6}T^{ab}\big(\bar\chi\gamma^{cd}\gamma_p\gamma_{ab}\widehat R(Q)_{cd}\big)\gamma^p\epsilon^i\\
&+\frac{i}{12}T^{ab}\big(\bar\chi\gamma^{cd}\gamma_{pq}\gamma_{ab}\widehat R(Q)_{cd}\big)\gamma^{pq}\epsilon^i\\
&-\frac{i}{32}T^{ab}\big(\overline{\widehat R(Q)}^{cd}\gamma_{ab}\widehat R(Q)_{cd}\big)\epsilon^i\\
&-\frac{i}{32}T^{ab}\big(\overline{\widehat R(Q)}^{cd}\gamma_p\gamma_{ab}\widehat R(Q)_{cd}\big)\gamma^p\epsilon^i\\
&+\frac{i}{64}T^{ab}\big(\overline{\widehat R(Q)}^{cd}\gamma_{pq}\gamma_{ab}\widehat R(Q)_{cd}\big)\gamma^{pq}\epsilon^i\\
&-\frac{9}{64}\big(\overline{\mathcal D_c\widehat R(Q)^{ab}}\gamma^c\widehat R(Q)_{ab}\big)\epsilon^i\\
&-\frac{9}{64}\big(\overline{\mathcal D_c\widehat R(Q)^{ab}}\gamma^c\gamma_p\widehat R(Q)_{ab}\big)\gamma^p\epsilon^i\\
&+\frac{9}{128}\big(\overline{\mathcal D_c\widehat R(Q)^{ab}}\gamma^c\gamma_{pq}\widehat R(Q)_{ab}\big)\gamma^{pq}\epsilon^i\\
&-\frac{9}{64}\big(\overline{\mathcal D^c\widehat R(Q)^{b]}{}_c}\gamma^{[a}\widehat R(Q)_{ab}\big)\epsilon^i\\
&-\frac{9}{64}\big(\overline{\mathcal D^c\widehat R(Q)^{b]}{}_c}\gamma^{[a}\gamma_p\widehat R(Q)_{ab}\big)\gamma^p\epsilon^i
\end{aligned}\tag{H179}
```

Continuation of the same right-hand side:

```math
\begin{aligned}
&+\frac{9}{128}\big(\overline{\mathcal D^c\widehat R(Q)^{b]}{}_c}\gamma^{[a}\gamma_{pq}\widehat R(Q)_{ab}\big)\gamma^{pq}\epsilon^i\\
&-\frac{3i}{8}\big(T^{ef}\overline{\widehat R(Q)}_{ef}\gamma^{ab}\widehat R(Q)_{ab}\big)\epsilon^i\\
&-\frac{3i}{8}\big(T^{ef}\overline{\widehat R(Q)}_{ef}\gamma^{ab}\gamma_p\widehat R(Q)_{ab}\big)\gamma^p\epsilon^i\\
&+\frac{3i}{16}\big(T^{ef}\overline{\widehat R(Q)}_{ef}\gamma^{ab}\gamma_{pq}\widehat R(Q)_{ab}\big)\gamma^{pq}\epsilon^i\\
&-\frac{27i}{16}T^{cd}\big(\overline{\widehat R(Q)}^{b]}{}_c\gamma^{[a}\gamma_d\widehat R(Q)_{ab}\big)\epsilon^i\\
&-\frac{27i}{16}T^{cd}\big(\overline{\widehat R(Q)}^{b]}{}_c\gamma^{[a}\gamma_d\gamma_p\widehat R(Q)_{ab}\big)\gamma^p\epsilon^i\\
&+\frac{27i}{32}T^{cd}\big(\overline{\widehat R(Q)}^{b]}{}_c\gamma^{[a}\gamma_d\gamma_{pq}\widehat R(Q)_{ab}\big)\gamma^{pq}\epsilon^i\\
&-\frac{33i}{64}\big(\overline{\widehat R(Q)}^{ab}(\gamma\!\cdot\!T)\widehat R(Q)_{ab}\big)\epsilon^i\\
&-\frac{33i}{64}\big(\overline{\widehat R(Q)}^{ab}(\gamma\!\cdot\!T)\gamma_p\widehat R(Q)_{ab}\big)\gamma^p\epsilon^i\\
&+\frac{33i}{128}\big(\overline{\widehat R(Q)}^{ab}(\gamma\!\cdot\!T)\gamma_{pq}\widehat R(Q)_{ab}\big)\gamma^{pq}\epsilon^i\\
&+\frac{9i}{8}T^{c[a}\big(\overline{\widehat R(Q)}^{b]}{}_c\widehat R(Q)_{ab}\big)\epsilon^i\\
&+\frac{9i}{8}T^{c[a}\big(\overline{\widehat R(Q)}^{b]}{}_c\gamma_p\widehat R(Q)_{ab}\big)\gamma^p\epsilon^i\\
&-\frac{9i}{16}T^{c[a}\big(\overline{\widehat R(Q)}^{b]}{}_c\gamma_{pq}\widehat R(Q)_{ab}\big)\gamma^{pq}\epsilon^i\\
&-\frac{3}{4}\big(\overline{\mathcal D^{b]}\chi}\gamma^{[a}\widehat R(Q)_{ab}\big)\epsilon^i\\
&-\frac{3}{4}\big(\overline{\mathcal D^{b]}\chi}\gamma^{[a}\gamma_p\widehat R(Q)_{ab}\big)\gamma^p\epsilon^i\\
&+\frac{3}{8}\big(\overline{\mathcal D^{b]}\chi}\gamma^{[a}\gamma_{pq}\widehat R(Q)_{ab}\big)\gamma^{pq}\epsilon^i\\
&+\frac{3i}{4}\big(\bar\chi\gamma^{[a}(\gamma\!\cdot\!T)\gamma^{b]}\widehat R(Q)_{ab}\big)\epsilon^i\\
&+\frac{3i}{4}\big(\bar\chi\gamma^{[a}(\gamma\!\cdot\!T)\gamma^{b]}\gamma_p\widehat R(Q)_{ab}\big)\gamma^p\epsilon^i
\end{aligned}\tag{H180}
```

Continuation of the same right-hand side:

```math
\begin{aligned}
&-\frac{3i}{8}\big(\bar\chi\gamma^{[a}(\gamma\!\cdot\!T)\gamma^{b]}\gamma_{pq}\widehat R(Q)_{ab}\big)\gamma^{pq}\epsilon^i\\
&-\frac{1}{24}\widehat R(V)^{ab\,kl}\gamma_{ab}{}^{cd}\widehat R(V)_{cd\,kl}\epsilon^i\\
&+\frac{1}{24}\widehat R(V)^{ab\,kl}\gamma^{cd} \gamma_{ab}\widehat R(V)_{cd\,kl}\epsilon^i\\
&+\frac{1}{24}\widehat R(V)^{ab\,kl}\gamma_{ab} \gamma^{cd}\widehat R(V)_{cd\,kl}\epsilon^i\\
&+\frac{3}{4}\big(\overline{\mathcal D_c\widehat R(Q)^{ab}}\gamma^c\gamma_{ab}\chi\big)\epsilon^i\\
&+\frac{3}{4}\big(\overline{\mathcal D_c\widehat R(Q)^{ab}}\gamma^c\gamma_p\gamma_{ab}\chi\big)\gamma^p\epsilon^i\\
&-\frac{3}{8}\big(\overline{\mathcal D_c\widehat R(Q)^{ab}}\gamma^c\gamma_{pq}\gamma_{ab}\chi\big)\gamma^{pq}\epsilon^i\\
&+\frac{3}{4}\big(\overline{\mathcal D^c\widehat R(Q)^{b]}{}_c}\gamma^{[a}\gamma_{ab}\chi\big)\epsilon^i\\
&+\frac{3}{4}\big(\overline{\mathcal D^c\widehat R(Q)^{b]}{}_c}\gamma^{[a}\gamma_p\gamma_{ab}\chi\big)\gamma^p\epsilon^i\\
&-\frac{3}{8}\big(\overline{\mathcal D^c\widehat R(Q)^{b]}{}_c}\gamma^{[a}\gamma_{pq}\gamma_{ab}\chi\big)\gamma^{pq}\epsilon^i\\
&+2i\big(T^{ef}\overline{\widehat R(Q)}_{ef}\gamma^{ab}\gamma_{ab}\chi\big)\epsilon^i\\
&+2i\big(T^{ef}\overline{\widehat R(Q)}_{ef}\gamma^{ab}\gamma_p\gamma_{ab}\chi\big)\gamma^p\epsilon^i\\
&-i\big(T^{ef}\overline{\widehat R(Q)}_{ef}\gamma^{ab}\gamma_{pq}\gamma_{ab}\chi\big)\gamma^{pq}\epsilon^i\\
&+9iT^{cd}\big(\overline{\widehat R(Q)}^{b]}{}_c\gamma^{[a}\gamma_d\gamma_{ab}\chi\big)\epsilon^i\\
&+9iT^{cd}\big(\overline{\widehat R(Q)}^{b]}{}_c\gamma^{[a}\gamma_d\gamma_p\gamma_{ab}\chi\big)\gamma^p\epsilon^i\\
&-\frac{9i}{2}T^{cd}\big(\overline{\widehat R(Q)}^{b]}{}_c\gamma^{[a}\gamma_d\gamma_{pq}\gamma_{ab}\chi\big)\gamma^{pq}\epsilon^i\\
&+\frac{11i}{4}\big(\overline{\widehat R(Q)}^{ab}(\gamma\!\cdot\!T)\gamma_{ab}\chi\big)\epsilon^i\\
&+\frac{11i}{4}\big(\overline{\widehat R(Q)}^{ab}(\gamma\!\cdot\!T)\gamma_p\gamma_{ab}\chi\big)\gamma^p\epsilon^i
\end{aligned}\tag{H181}
```

Continuation of the same right-hand side:

```math
\begin{aligned}
&-\frac{11i}{8}\big(\overline{\widehat R(Q)}^{ab}(\gamma\!\cdot\!T)\gamma_{pq}\gamma_{ab}\chi\big)\gamma^{pq}\epsilon^i\\
&-6iT^{c[a}\big(\overline{\widehat R(Q)}^{b]}{}_c\gamma_{ab}\chi\big)\epsilon^i\\
&-6iT^{c[a}\big(\overline{\widehat R(Q)}^{b]}{}_c\gamma_p\gamma_{ab}\chi\big)\gamma^p\epsilon^i\\
&+3iT^{c[a}\big(\overline{\widehat R(Q)}^{b]}{}_c\gamma_{pq}\gamma_{ab}\chi\big)\gamma^{pq}\epsilon^i\\
&+4\big(\overline{\mathcal D^{b]}\chi}\gamma^{[a}\gamma_{ab}\chi\big)\epsilon^i\\
&+4\big(\overline{\mathcal D^{b]}\chi}\gamma^{[a}\gamma_p\gamma_{ab}\chi\big)\gamma^p\epsilon^i\\
&-2\big(\overline{\mathcal D^{b]}\chi}\gamma^{[a}\gamma_{pq}\gamma_{ab}\chi\big)\gamma^{pq}\epsilon^i\\
&-4i\big(\bar\chi\gamma^{[a}(\gamma\!\cdot\!T)\gamma^{b]}\gamma_{ab}\chi\big)\epsilon^i\\
&-4i\big(\bar\chi\gamma^{[a}(\gamma\!\cdot\!T)\gamma^{b]}\gamma_p\gamma_{ab}\chi\big)\gamma^p\epsilon^i\\
&+2i\big(\bar\chi\gamma^{[a}(\gamma\!\cdot\!T)\gamma^{b]}\gamma_{pq}\gamma_{ab}\chi\big)\gamma^{pq}\epsilon^i
\end{aligned}\tag{H182}
```

The displayed addition combines the two identical weight/SU(2) connection
bilinears as illustrated by H69. Other terms are left in their source
order when combining them would require another gamma identity or an
integration by parts. In particular an equality of local Q coefficients
is not replaced by equality of integrated action densities.

## 29. Convention Dependence and Remaining Uncertainties

The result is conditional on the adopted M08 (ninth coefficient $`8/3`$)
and the v5 master transformation laws. Their source-discrepancy ledger
is unchanged. H50 no longer contains an unresolved calculation.
All hatted objects and full derivatives retain their nonlinear fermionic
content; the local frame used to evaluate covariant coefficients is not
a bosonic truncation or a Poincare gauge choice.

The final sum retains ordered gamma products. Reduction to a minimal
$`N_W`$, $`E_{Wa}`$ and any residual bivector, the separate SU(2)-traceless
variation, the S-law of $`\varphi_W`$, and full linear-multiplet closure
remain distinct calculations. No full invariant or spectrum is claimed
here. The normal-frame argument is the analytic justification for
restoring full covariants; the finite-matrix checks certify its displayed
Clifford/Fierz algebra, not an independently implemented nonlinear
supersymmetry algebra.

# Part V — Collecting the scalar, vector and bivector coefficients

## 30. Problem and Target

The starting point is the complete, epsilon-right singlet in Section 28,
H150–H182. We now multiply its gamma matrices and collect like physical
contractions. The requested form is

```math
\left.\delta_Q\varphi_W^i\right|_{\epsilon^i}
 =\big(p+\gamma_a t^a+\gamma_{ab}k^{ab}\big)\epsilon^i,
\qquad k^{ab}=k^{[ab]}.
\tag{G01}
```

Here $`p,t^a,k^{ab}`$ are precisely the three coefficients requested in the
question. They are not additional fields. The singlet restriction has the
same meaning as H04–H08: perform the SU(2) Schouten and spinor Fierz
rearrangements first, then retain the coefficient of $`\epsilon^i`$.
The omitted traceless SU(2) part is not restored by this calculation.

**Assumptions.** The input is the adopted M08, with ninth coefficient $`8/3`$,
and the v5 transformation laws. Work off shell, with $`g=0`$, without gauge
fixing or a physical fermion truncation. Every hatted object and every
$`\mathcal D`$ below is the full object defined in the master conventions.
There is no integration by parts, derivative interchange, field equation,
background specialization or field redefinition. Thus every equality below
is a local algebraic equality of the supplied variation.

The source chain is master M08 → M09/Part III → M10/Part IV → this part.
The original rules and their located sources are C01–C06, G03a, W03 and
R01–R06 in [the master file](component_conventions.md). No external completed
Weyl multiplet is an input.

## 31. Convention Ledger

<!-- ASSERT_CONVENTION: metric_signature=mostly_plus, spacetime_dimension=5, convention_lock=UNG-WEYL2-OP58-CONVENTIONS-v5 -->

Use $`a,b,\ldots=0,\ldots,4`$, $`\eta_{ab}=\mathrm{diag}(-,+,+,+,+)`$,
$`\{\gamma_a,\gamma_b\}=2\eta_{ab}`$ and
$`\gamma_{a_1\cdots a_r}=\gamma_{[a_1}\cdots\gamma_{a_r]}`$ with unit-weight
antisymmetrization. The orientation is $`\gamma^{01234}=i\mathbf1`$,
$`\varepsilon^{01234}=+1`$, $`\varepsilon_{01234}=-1`$; consequently the
all-lower gamma product is $`\gamma_{01234}=-i\mathbf1`$.
The symbol $`\varepsilon_{abcde}`$ in this part denotes the volume tensor;
$`\epsilon^i`$ is always the supersymmetry parameter.

Every repeated antisymmetric pair is summed over **all ordered values**.
In particular G01 has no implicit $`1/2`$ before $`\gamma_{ab}k^{ab}`$.
Square brackets on $`a,b`$ in the final $`k^{ab}`$ have weight $`1/2`$; vertical
bars exclude intervening dummy indices from that antisymmetrization.

All spinors and $`\epsilon`$ are Grassmann odd. The bar is the linear Majorana
bar of C03, not an antilinear Dirac-bar operation on numerical coefficients.
An unlabelled bilinear contracts its SU(2) indices as in C03. For these
contracted bilinears, the extra SU(2) antisymmetry gives

```math
\bar u\gamma_{(r)}v=-t_r\bar v\gamma_{(r)}u,
\qquad(t_0,t_1,t_2,t_3,t_4,t_5)=(+,+,-,-,+,+).
\tag{G02}
```

In particular $`\bar\chi\chi=\bar\chi\gamma_a\chi=0`$, whereas
$`\bar\chi\gamma_{ab}\chi`$ need not vanish. The same flip rule applies when
one spinor is a full covariant derivative. Moving that derivative to a
**different field by integration by parts** is not allowed here.

Only the displayed antisymmetries of $`T`$, $`\widehat R(V)`$ and the two index
pairs of $`\widehat C`$, the conventional traces in G03a, and Clifford/Schouten
identities are used. No bosonic pair-exchange or differential Bianchi identity
is silently imposed on the full hatted curvature. The statement about a
cyclic Lorentz-curvature identity in master G03 is not substituted as an
unqualified bosonic identity for $`\widehat C`$.

## 32. Definitions and Required Identities

### 32.1 Multiplying gamma matrices

Start with $`\gamma_a\gamma_b=\gamma_{ab}+\eta_{ab}`$. The first nontrivial
multiplication follows by inserting the antisymmetrized definition:

```math
\begin{aligned}
\gamma_a\gamma_{bc}
 &=\tfrac12\gamma_a(\gamma_b\gamma_c-\gamma_c\gamma_b)\\
 &=\gamma_{abc}+\eta_{ab}\gamma_c-\eta_{ac}\gamma_b,\\
\gamma_{ab}\gamma_c
 &=\gamma_{abc}+\eta_{bc}\gamma_a-\eta_{ac}\gamma_b.
\end{aligned}\tag{G03}
```

For two bivectors, first multiply by $`\gamma_c`$, then $`\gamma_d`$, and
subtract $`\eta_{cd}\gamma_{ab}`$:

```math
\begin{aligned}
\gamma_{ab}\gamma_{cd}
 &=(\gamma_{abc}+\eta_{bc}\gamma_a-\eta_{ac}\gamma_b)\gamma_d
   -\eta_{cd}\gamma_{ab}\\
 &=\gamma_{abcd}
  +\eta_{bc}\gamma_{ad}-\eta_{ac}\gamma_{bd}
  -\eta_{bd}\gamma_{ac}+\eta_{ad}\gamma_{bc}
  +\eta_{ad}\eta_{bc}-\eta_{ac}\eta_{bd}.
\end{aligned}\tag{G04}
```

These steps extend to every longer word in the calculation by

```math
\gamma_{a_1\cdots a_r}\gamma_b
 =\gamma_{a_1\cdots a_rb}
 +\sum_{j=1}^r(-1)^{r-j}\eta_{a_jb}
       \gamma_{a_1\cdots\widehat{a_j}\cdots a_r}.
\tag{G05}
```

The hat on $`a_j`$ in G05 means to omit that index only. The $`j`$th contraction
crosses $`r-j`$ gamma matrices, which explains its sign. Antisymmetrize the
right-hand indices if the right factor is a higher-rank gamma. Below each
actual gamma word is followed by its multiplied and contracted expression;
G05 is not left as an instruction to finish an unevaluated term.

The contracted products needed repeatedly are

```math
\begin{aligned}
\gamma^a\gamma_{(r)}\gamma_a
 &=(-1)^r(5-2r)\gamma_{(r)},\\
\gamma^{ab}\gamma_{(r)}\gamma_{ab}
 &=\big[5-(5-2r)^2\big]\gamma_{(r)}\\
 &=\begin{cases}-20\gamma_{(0)},&r=0,\\-4\gamma_{(1)},&r=1,\\
 4\gamma_{(2)},&r=2,\\4\gamma_{(3)},&r=3.
 \end{cases}
\end{aligned}\tag{G06}
```

For the second line, write $`\gamma^{ab}=\gamma^a\gamma^b-\eta^{ab}`$ and
$`\gamma_{ab}=\gamma_a\gamma_b-\eta_{ab}`$. The first product is
$`\gamma^a\gamma^b\gamma_{(r)}\gamma_a\gamma_b =-[5-2r]^2\gamma_{(r)}+10\gamma_{(r)}`$;
the two subtractions and the last addition contribute $`-10+5`$.
This gives $`5-(5-2r)^2`$, including the full-pair factor.

### 32.2 Dualizing the remaining gamma ranks

With the orientation in Section 31,

```math
\gamma_{abc}=-\frac{i}{2}\varepsilon_{abcde}\gamma^{de},
\quad \gamma_{abcd}=i\varepsilon_{abcde}\gamma^e,
\quad \gamma_{abcde}=i\varepsilon_{abcde}\mathbf1.
\tag{G07}
```

For example $`\gamma_{012}=\gamma_{01234}\gamma_{34}^{-1} =(-i)(-\gamma_{34})=i\gamma_{34}`$. The first formula gives the same answer:
$`-i(\varepsilon_{01234}\gamma^{34}+ \varepsilon_{01243}\gamma^{43})/2=i\gamma^{34}`$.
The factor $`1/2`$ is essential because both $`(3,4)`$ and $`(4,3)`$ are summed.
The rank-four and rank-five formulas follow by multiplying this identity
by the remaining gamma matrices and using G03. These are master C04c,
with every index position retained.

When two volume tensors occur, contract them before collecting terms:

```math
\varepsilon_{a_1\cdots a_k b_1\cdots b_{5-k}}
\varepsilon^{a_1\cdots a_k c_1\cdots c_{5-k}}
=-k!(5-k)!\,\delta_{[b_1}^{c_1}\cdots
                  \delta_{b_{5-k}]}^{c_{5-k}}.
\tag{G08}
```

The minus sign comes from the single timelike direction. No volume tensor
is replaced by a Euclidean one.

### 32.3 Gamma-trace constraints inside bilinears

The conventional constraint and its covariant derivative are

```math
\gamma^a\widehat R(Q)_{ab}=0,
\qquad \gamma^a\mathcal D_c\widehat R(Q)_{ab}=0.
\tag{G09}
```

For example,

```math
\begin{aligned}
\gamma_{ac}\widehat R(Q)^c{}_b
 &=(\gamma_a\gamma_c-\eta_{ac})\widehat R(Q)^c{}_b
 =-\widehat R(Q)_{ab},\\
\gamma_{acd}\widehat R(Q)^{cd}
 &=\gamma_a\gamma_{cd}\widehat R(Q)^{cd}
   -\gamma_d\widehat R(Q)_a{}^d
   +\gamma_c\widehat R(Q)^c{}_a=0.
\end{aligned}\tag{G10}
```

The first term in the second line vanishes because
$`\gamma_{cd}\widehat R(Q)^{cd}=\gamma_c\gamma_d\widehat R(Q)^{cd}=0`$.
Use the Majorana transpose and G02 to obtain the barred identities.
These are conventional constraints, not gravitino equations of motion.

### 32.4 Keeping the correct order in a Fierz term

The sixteen matrices $`1,\gamma_a,\gamma_{ab}`$ form a complete basis.
Their nonzero trace pairings are

```math
\mathop{\mathrm{tr}}\nolimits\mathbf1=4,\quad
\mathop{\mathrm{tr}}\nolimits(\gamma_a\gamma_b)=4\eta_{ab},\quad
\mathop{\mathrm{tr}}\nolimits(\gamma_{ab}\gamma_{cd})
=4(\eta_{ad}\eta_{bc}-\eta_{ac}\eta_{bd}).
\tag{G11}
```

For any spinor matrix $`X`$, multiplication by these three basis elements
and taking the trace therefore gives

```math
X=\frac14\mathop{\mathrm{tr}}\nolimits X
 +\frac14\mathop{\mathrm{tr}}\nolimits(\gamma_aX)\gamma^a
 -\frac18\mathop{\mathrm{tr}}\nolimits(\gamma_{ab}X)\gamma^{ab}.
\tag{G12}
```

This explains the factor of two in the bivector normalization. Applying
G12 to the already proved singlet Fierz identity H05, with an exterior
gamma matrix product $`A`$, gives the ordinary bilinears

```math
\begin{aligned}
\left.Au^i(\bar\epsilon Mv)\right|_{\epsilon^i}
={}&\Big[
\tfrac18\bar v\widetilde M A u
+\tfrac18\bar v\widetilde M\gamma_a A u\,\gamma^a
-\tfrac1{16}\bar v\widetilde M\gamma_{ab}A u\,\gamma^{ab}
\Big]\epsilon^i .
\end{aligned}\tag{G13}
```

Here $`A,M`$ denote just the gamma products in this identity;
$`\widetilde M=\mathsf C^{-1}M^T\mathsf C`$. They introduce no response field or new operation.
The coefficient $`1/8`$ is the $`1/4`$ spinor completeness factor times the
$`1/2`$ SU(2) singlet trace, with the Grassmann/transpose signs already
shown in H05. The rank-two coefficient is $`-1/16`$ because the ordered-pair
sum counts both orders. For a symmetric triplet pairing, H08 supplies an
additional factor $`3/2`$ in all three slots.

If the actual spinor is $`u=\gamma_{cd}\chi`$, the vector coefficient is
$`\bar v\widetilde M\gamma_a A\gamma_{cd}\chi/8`$.
It is **not** $`\bar v\widetilde M\gamma_{cd}\gamma_a A\chi/8`$.
This order is retained separately in every actual pairing below.
The traces in G12 have all been evaluated; no trace operation occurs in
the final $`p,t^a,k^{ab}`$.

## 33. Detailed Derivation

### 33.1 The two-form Schouten reductions, written out

In five dimensions the six-index antisymmetrization vanishes. Expanding
one index gives

```math
\begin{aligned}
\varepsilon_{abcde}\delta_f{}^h={}&
\varepsilon_{fbcde}\delta_a{}^h+
\varepsilon_{afcde}\delta_b{}^h+
\varepsilon_{abfde}\delta_c{}^h+
\varepsilon_{abcfe}\delta_d{}^h+
\varepsilon_{abcdf}\delta_e{}^h.
\end{aligned}\tag{G14}
```

First multiply G14 by $`T^{ab}T^{cf}\mathcal D_hT^{de}`$.
The five terms on the right, in exactly the displayed order, become

```math
\begin{aligned}
\varepsilon_{fbcde}T^{ab}T^{cf}\mathcal D_aT^{de}
 &=-\varepsilon_{abcde}T^{ab}T^{cf}\mathcal D_fT^{de},\\
\varepsilon_{afcde}T^{ab}T^{cf}\mathcal D_bT^{de}
 &=-\varepsilon_{abcde}T^{ab}T^{cf}\mathcal D_fT^{de},\\
\varepsilon_{abfde}T^{ab}T^{cf}\mathcal D_cT^{de}
 &=-\varepsilon_{abcde}T^{ab}T^{cf}\mathcal D_fT^{de},\\
\varepsilon_{abcfe}T^{ab}T^{cf}\mathcal D_dT^{de}
 &=-\varepsilon_{abcde}T^{ab}T^{cd}\mathcal D_fT^{ef},\\
\varepsilon_{abcdf}T^{ab}T^{cf}\mathcal D_eT^{de}
 &=-\varepsilon_{abcde}T^{ab}T^{cd}\mathcal D_fT^{ef}.
\end{aligned}\tag{G15}
```

These are dummy relabelings and $`T^{ab}=-T^{ba}`$; none moves a derivative.
For the third line interchange $`c\leftrightarrow f`$, producing
$`T^{fc}=-T^{cf}`$. In the fourth line interchange $`d\leftrightarrow f`$,
then use $`\mathcal D_fT^{fe}=-\mathcal D_fT^{ef}`$.
For the first line interchange $`a,f`$, then $`b,c`$. The second swap gives
a minus from the epsilon tensor, and $`T^{fc}T^{ba}=T^{cf}T^{ab}`$ gives
two compensating tensor signs. Exchange the two commuting $`T`$ factors. The second
line first interchanges $`a,b`$ in both the epsilon tensor and the first $`T`$,
and reduces to the first. The fifth line interchanges $`e,f`$, then $`d,e`$; the latter swap gives the
minus sign from the epsilon tensor.
Adding the five lines gives

```math
\begin{aligned}
4\varepsilon_{abcde}T^{ab}T^{cf}\mathcal D_fT^{de}
 &=-2\varepsilon_{abcde}T^{ab}T^{cd}\mathcal D_fT^{ef},\\
\varepsilon_{abcde}T^{ab}T^{cf}\mathcal D_fT^{de}
 &=-\tfrac12\varepsilon_{abcde}T^{ab}T^{cd}\mathcal D_fT^{ef}.
\end{aligned}\tag{G16}
```

Next multiply G14 by $`T^{ab}T^c{}_h\mathcal D^dT^{ef}`$.
The first two terms vanish: their two-$`T`$ contraction is symmetric in
$`(b,c)`$ or $`(a,c)`$, respectively, and those slots are antisymmetric in
$`\varepsilon`$. The third contains $`T^c{}_c=0`$. The last two terms are

```math
\begin{aligned}
\varepsilon_{abcfe}T^{ab}T^{cd}\mathcal D_dT^{ef}
 &=-\varepsilon_{abcde}T^{ab}T^{cf}\mathcal D_fT^{de},\\
\varepsilon_{abcdf}T^{ab}T^{ce}\mathcal D_dT^{ef}
 &=-\varepsilon_{abcde}T^{ab}T^{cf}\mathcal D_dT^{ef}.
\end{aligned}\tag{G17}
```

In the first line interchange $`d,f`$ and use $`T^{ed}=-T^{de}`$. In the second interchange $`e,f`$ and use $`T^{fe}=-T^{ef}`$.
Putting the left-hand side of G14 back in, then using G16, yields

```math
\begin{aligned}
2\varepsilon_{abcde}T^{ab}T^{cf}\mathcal D_dT^{ef}
 &=-\varepsilon_{abcde}T^{ab}T^{cf}\mathcal D_fT^{de}\\
 &=\tfrac12\varepsilon_{abcde}T^{ab}T^{cd}\mathcal D_fT^{ef},\\
\frac{1408}{9}\varepsilon_{abcde}T^{ab}T^{cf}\mathcal D_fT^{de}
+\frac{640}{9}\varepsilon_{abcde}T^{ab}T^{cf}\mathcal D_dT^{ef}
+\frac{352}{9}\varepsilon_{abcde}T^{ab}T^{cd}\mathcal D_fT^{ef}
 &=\left(-\frac{704}{9}+\frac{160}{9}+\frac{352}{9}\right)
   \varepsilon_{abcde}T^{ab}T^{cd}\mathcal D_fT^{ef}\\
 &=-\frac{64}{3}\varepsilon_{abcde}T^{ab}T^{cd}\mathcal D_fT^{ef}.
\end{aligned}\tag{G18}
```

The quartic vector has a second useful cancellation. The six-form
$`T_{[ab}T_{cd}T_{ef]}`$ vanishes in five dimensions. Contracting its expanded
fifteen pairings with a five-index volume tensor gives

```math
\varepsilon_{cdefg}T^{cd}T^{ef}T^g{}_h=0.
\tag{G19}
```

Each of the fifteen pairings reduces to the same contraction by relabeling
the five epsilon slots, so the antisymmetrization normalization cancels
the multiplicity. Apply G14 with epsilon slots $`(a,c,d,e,f)`$, replace its
sixth slot by $`g`$, and multiply by $`T^{cd}T^{eg}T^{fj}T_{hj}`$. Its first
term on the right is
$`-\varepsilon_{cdefg}T^{cd}T^{ef}T^g{}_hT^{ah}=0`$ by G19.
The next three terms each give
$`-\varepsilon^a{}_{cdef}T^{cd}T^e{}_gT^f{}_hT^{gh}`$;
the last gives $`+\varepsilon^a{}_{cdef}T^{cd}T^{ef}T_{gh}T^{gh}`$.
Thus the complete five-term addition is

```math
\begin{aligned}
\varepsilon^a{}_{cdef}T^{cd}T^e{}_gT^f{}_hT^{gh}
 &=-\varepsilon_{cdefg}T^{cd}T^{ef}T^g{}_hT^{ah}
  -3\varepsilon^a{}_{cdef}T^{cd}T^e{}_gT^f{}_hT^{gh}
  +\varepsilon^a{}_{cdef}T^{cd}T^{ef}T_{gh}T^{gh},\\
\varepsilon^a{}_{cdef}T^{cd}T^e{}_gT^f{}_hT^{gh}
 &=\tfrac14\varepsilon^a{}_{cdef}T^{cd}T^{ef}T_{gh}T^{gh},\\
\frac{32i}{3}\varepsilon^a{}_{cdef}T^{cd}T^{ef}T_{gh}T^{gh}
-\frac{128i}{3}\varepsilon^a{}_{cdef}T^{cd}T^e{}_gT^f{}_hT^{gh}
 &=\left(\frac{32i}{3}-\frac{128i}{3}\frac14\right)
 \varepsilon^a{}_{cdef}T^{cd}T^{ef}T_{gh}T^{gh}=0.
\end{aligned}\tag{G20}
```

### 33.2 Two explicit gamma-product examples before the full calculation

The curvature-square term illustrates the full-pair normalization:

```math
\begin{aligned}
-\frac1{32}\widehat C_{ab}{}^{ef}\widehat C^{abcd}
 \gamma_{cd}\gamma_{ef}
={}&-\frac1{32}\widehat C_{ab}{}^{ef}\widehat C^{abcd}
 \big(\gamma_{cdef}+\eta_{de}\gamma_{cf}-\eta_{ce}\gamma_{df}
 -\eta_{df}\gamma_{ce}+\eta_{cf}\gamma_{de}
 +\eta_{cf}\eta_{de}-\eta_{ce}\eta_{df}\big)\\
={}&\frac1{16}\widehat C_{abcd}\widehat C^{abcd}
 -\frac1{32}\widehat C_{ab}{}^{cd}\widehat C^{abef}\gamma_{cdef}\\
={}&\frac1{16}\widehat C_{abcd}\widehat C^{abcd}
 -\frac{i}{32}\varepsilon_{cdefg}
    \widehat C_{ab}{}^{cd}\widehat C^{abef}\gamma^g.
\end{aligned}\tag{G21}
```

The four bivector terms in the first line cancel in pairs because
$`\widehat C_{ab}{}^{c}{}_e\widehat C^{abde}`$ is symmetric in $`c,d`$.
This uses the same two-form twice; it does not require exchanging the two
index pairs of one $`\widehat C`$.

One actual fermionic pairing from the first block has the following scalar
coefficient after G13:

```math
\begin{aligned}
\frac1{128}\overline{\mathcal D_c\widehat R(Q)_{de}}
 \gamma^c\gamma^{fg}\gamma_{fg}\widehat R(Q)^{de}
 &=-\frac{20}{128}\overline{\mathcal D_c\widehat R(Q)_{de}}
 \gamma^c\widehat R(Q)^{de}\\
 &=\frac5{32}\overline{\widehat R(Q)_{de}}
 \gamma^c\mathcal D_c\widehat R(Q)^{de}.
\end{aligned}\tag{G22}
```

The first equality is G06 at rank zero. The second is the **contracted**
rank-one Majorana flip G02, contributing a minus sign. Its vector
coefficient contains $`\gamma^{fg}\gamma^a\gamma_{fg}=-4\gamma^a`$:

```math
\begin{aligned}
\frac1{128}\overline{\mathcal D_c\widehat R(Q)_{de}}
 \gamma^c\gamma^{fg}\gamma^a\gamma_{fg}\widehat R(Q)^{de}
 &=-\frac1{32}\overline{\mathcal D_c\widehat R(Q)_{de}}
 (\gamma^{ca}+\eta^{ca})\widehat R(Q)^{de}\\
 &=-\frac1{32}\overline{\widehat R(Q)_{de}}
 \gamma^{ca}\mathcal D_c\widehat R(Q)^{de}
 +\frac1{32}\overline{\widehat R(Q)_{cd}}
 \mathcal D^a\widehat R(Q)^{cd}.
\end{aligned}\tag{G23}
```

The rank-two flip is plus and the rank-zero flip is minus. The latter
line also relabels the two curvature indices to $`c,d`$ in its last term.
For its bivector coefficient,

```math
\begin{aligned}
-\frac1{256}\overline{\mathcal D_c\widehat R(Q)_{de}}
 \gamma^c\gamma^{fg}\gamma^{ab}\gamma_{fg}\widehat R(Q)^{de}
 &=-\frac1{64}\overline{\mathcal D_c\widehat R(Q)_{de}}
 (\gamma^{cab}+2\eta^{c[a}\gamma^{b]})\widehat R(Q)^{de}\\
 &=-\frac1{64}\overline{\widehat R(Q)_{de}}
 \gamma^{cab}\mathcal D_c\widehat R(Q)^{de}
 -\frac1{32}\overline{\widehat R(Q)_{cd}}
 \gamma^{[a}\mathcal D^{b]}\widehat R(Q)^{cd}\\
 &=\frac{i}{128}\varepsilon_{cde}{}^{ab}
 \overline{\widehat R(Q)_{fg}}\gamma^{cd}
 \mathcal D^e\widehat R(Q)^{fg}
 -\frac1{32}\overline{\widehat R(Q)_{cd}}
 \gamma^{[a}\mathcal D^{b]}\widehat R(Q)^{cd}.
\end{aligned}\tag{G24}
```

The three equalities use G06, then G02 with $`t_3=-1,t_1=+1`$, then G07.
The identical procedure below retains the actual gamma order of every
pairing, including those whose right spinor contains $`\gamma_{ab}\chi`$.

### 33.3 Every contribution in the eleven original terms

The block number below is the position in M08, not a newly defined field.
The `origin` labels are the existing Part-IV ledger labels. For a Fierz
triple, G13 gives three displayed coefficients: scalar, vector and bivector.
For a term already proportional to $`\epsilon^i`$, the calculation displays
the whole gamma matrix multiplying that parameter.

Each equality begins with the actual physical-field expression. The next
line multiplies the gamma matrices, contracts the metrics, and uses G02/G09
where needed. If higher gamma ranks remain, the last line uses G07–G08;
G16–G20 combine the two-form Schouten contractions. A line already in its
final form is not repeated. Thus a zero is the evaluated value of the
preceding expression, not an omitted contribution. Numerical addition
across different contributions is deferred to Section 33.4.

In Section 28 the typography `{T^2}^2` occurs twice. Throughout this part it
means $`(T_{ab}T^{ab})^2`$, as follows from varying $`T^2\chi`$ and inserting
the $`T^2\epsilon`$ term in $`\delta\chi`$. The earlier ledger is preserved;
no input coefficient is changed.

#### Block 1

The original spinor term is $`-\frac18\gamma_{cd}\widehat R_{ab}{}^i(Q)\widehat C^{abcd}`$.

**G101: R4, whole coefficient matrix.**

```math
\begin{aligned}
&-\frac{1}{32}\widehat C_{cdef}\,\widehat C^{cd}{}_{gh}\,\gamma^{gh}\gamma^{ef}\\
&=-\frac{1}{32}\widehat C_{cdef}\,\widehat C^{cd}{}_{gh}\,\gamma^{efgh}\\
&+\frac{1}{16}\widehat C_{cdef}\,\widehat C^{cdef}\\
&=-\frac{i}{32}\widehat C_{cdef}\,\widehat C^{cd}{}_{gh}\,\varepsilon^{efgh}{}_{j}\,\gamma^{j}\\
&+\frac{1}{16}\widehat C_{cdef}\,\widehat C^{cdef}
\end{aligned}\tag{G101}
```

**G102: R5, whole coefficient matrix.**

```math
\begin{aligned}
&-\frac{i}{8}(\mathcal D_{c}T_{de})\,\widehat C^{c}{}_{fgh}\,\gamma^{gh}\gamma^{de}\gamma^{f}\\
&+\frac{i}{8}(\mathcal D_{c}T_{de})\,\widehat C_{f}{}^{c}{}_{gh}\,\gamma^{gh}\gamma^{de}\gamma^{f}\\
&=\frac{i}{4}\widehat C_{cdef}\,(\mathcal D^{d}T_{gh})\,\gamma^{cefgh}\\
&+\frac{i}{2}\widehat C_{cdef}\,(\mathcal D^{c}T^{d}{}_{g})\,\gamma^{efg}\\
&+i\widehat C_{cdef}\,(\mathcal D^{d}T^{f}{}_{g})\,\gamma^{ceg}\\
&+i\widehat C_{cdef}\,(\mathcal D^{c}T^{df})\,\gamma^{e}\\
&-\frac{i}{2}\widehat C_{cdef}\,(\mathcal D^{d}T^{ef})\,\gamma^{c}\\
&=-\frac{1}{4}\widehat C_{cdef}\,\varepsilon^{cef}{}_{gh}\,(\mathcal D^{d}T^{gh})\\
&+\frac{1}{4}\widehat C_{cdef}\,\varepsilon^{ef}{}_{ghj}\,(\mathcal D^{c}T^{dj})\,\gamma^{gh}\\
&+\frac{1}{2}\widehat C_{cdef}\,\varepsilon^{ce}{}_{ghj}\,(\mathcal D^{d}T^{fj})\,\gamma^{gh}\\
&+i\widehat C_{cdef}\,(\mathcal D^{c}T^{df})\,\gamma^{e}\\
&-\frac{i}{2}\widehat C_{cdef}\,(\mathcal D^{d}T^{ef})\,\gamma^{c}
\end{aligned}\tag{G102}
```

**G103: R6, whole coefficient matrix.**

```math
\begin{aligned}
&\frac{i}{24}(\mathcal D_{c}T_{de})\,\widehat C^{c}{}_{fgh}\,\gamma^{gh}\gamma^{f}\gamma^{de}\\
&-\frac{i}{24}(\mathcal D_{c}T_{de})\,\widehat C_{f}{}^{c}{}_{gh}\,\gamma^{gh}\gamma^{f}\gamma^{de}\\
&=-\frac{i}{12}\widehat C_{cdef}\,(\mathcal D^{d}T_{gh})\,\gamma^{cefgh}\\
&+\frac{i}{6}\widehat C_{cdef}\,(\mathcal D^{c}T^{d}{}_{g})\,\gamma^{efg}\\
&-\frac{i}{3}\widehat C_{cdef}\,(\mathcal D^{d}T^{f}{}_{g})\,\gamma^{ceg}\\
&+\frac{i}{3}\widehat C_{cdef}\,(\mathcal D^{c}T^{df})\,\gamma^{e}\\
&+\frac{i}{6}\widehat C_{cdef}\,(\mathcal D^{d}T^{ef})\,\gamma^{c}\\
&=\frac{1}{12}\widehat C_{cdef}\,\varepsilon^{cef}{}_{gh}\,(\mathcal D^{d}T^{gh})\\
&+\frac{1}{12}\widehat C_{cdef}\,\varepsilon^{ef}{}_{ghj}\,(\mathcal D^{c}T^{dj})\,\gamma^{gh}\\
&-\frac{1}{6}\widehat C_{cdef}\,\varepsilon^{ce}{}_{ghj}\,(\mathcal D^{d}T^{fj})\,\gamma^{gh}\\
&+\frac{i}{3}\widehat C_{cdef}\,(\mathcal D^{c}T^{df})\,\gamma^{e}\\
&+\frac{i}{6}\widehat C_{cdef}\,(\mathcal D^{d}T^{ef})\,\gamma^{c}
\end{aligned}\tag{G103}
```

**G104: R7, whole coefficient matrix.**

```math
\begin{aligned}
&\frac{i}{24}(\mathcal D_{c}T_{de})\,\widehat C_{fghj}\,\gamma^{hj}\gamma^{f}\gamma^{c}\gamma^{de}\gamma^{g}\\
&-\frac{i}{24}(\mathcal D_{c}T_{de})\,\widehat C_{fghj}\,\gamma^{hj}\gamma^{g}\gamma^{c}\gamma^{de}\gamma^{f}\\
&=\frac{i}{6}\widehat C_{cdef}\,(\mathcal D_{g}T^{d}{}_{h})\,\gamma^{cefgh}\\
&-\frac{i}{6}\widehat C_{cdef}\,(\mathcal D_{g}T^{cd})\,\gamma^{efg}\\
&-\frac{i}{3}\widehat C_{cdef}\,(\mathcal D^{c}T^{d}{}_{g})\,\gamma^{efg}\\
&+\frac{i}{3}\widehat C_{cdef}\,(\mathcal D_{g}T^{f}{}_{h})\,\gamma^{cdegh}\\
&+\frac{i}{6}\widehat C_{cdef}\,(\mathcal D_{g}T_{h}{}^{g})\,\gamma^{cdefh}\\
&-\frac{2i}{3}\widehat C_{cdef}\,(\mathcal D^{c}T^{df})\,\gamma^{e}\\
&+\frac{i}{6}\widehat C_{cdef}\,(\mathcal D_{g}T^{ef})\,\gamma^{cdg}\\
&+\frac{i}{3}\widehat C_{cdef}\,(\mathcal D_{g}T^{fg})\,\gamma^{cde}\\
&-\frac{i}{12}\widehat C_{cdef}\,(\mathcal D^{d}T_{gh})\,\gamma^{cefgh}\\
&-\frac{i}{6}\widehat C_{cdef}\,(\mathcal D^{f}T_{gh})\,\gamma^{cdegh}\\
&-\frac{i}{3}\widehat C_{cdef}\,(\mathcal D^{f}T^{cd})\,\gamma^{e}\\
&+\frac{i}{3}\widehat C_{cdef}\,(\mathcal D^{e}T^{f}{}_{g})\,\gamma^{cdg}\\
&=-\frac{1}{6}\widehat C_{cdef}\,\varepsilon^{cef}{}_{gh}\,(\mathcal D^{g}T^{dh})\\
&-\frac{1}{12}\widehat C_{cdef}\,\varepsilon^{ef}{}_{ghj}\,(\mathcal D^{j}T^{cd})\,\gamma^{gh}\\
&-\frac{1}{6}\widehat C_{cdef}\,\varepsilon^{ef}{}_{ghj}\,(\mathcal D^{c}T^{dj})\,\gamma^{gh}\\
&-\frac{1}{3}\widehat C_{cdef}\,\varepsilon^{cde}{}_{gh}\,(\mathcal D^{g}T^{fh})\\
&-\frac{1}{6}\widehat C_{cdef}\,\varepsilon^{cdef}{}_{g}\,(\mathcal D_{h}T^{gh})\\
&-\frac{2i}{3}\widehat C_{cdef}\,(\mathcal D^{c}T^{df})\,\gamma^{e}\\
&+\frac{1}{12}\widehat C_{cdef}\,\varepsilon^{cd}{}_{ghj}\,(\mathcal D^{j}T^{ef})\,\gamma^{gh}\\
&+\frac{1}{6}\widehat C_{cdef}\,\varepsilon^{cde}{}_{gh}\,(\mathcal D_{j}T^{fj})\,\gamma^{gh}\\
&+\frac{1}{12}\widehat C_{cdef}\,\varepsilon^{cef}{}_{gh}\,(\mathcal D^{d}T^{gh})\\
&+\frac{1}{6}\widehat C_{cdef}\,\varepsilon^{cde}{}_{gh}\,(\mathcal D^{f}T^{gh})\\
&-\frac{i}{3}\widehat C_{cdef}\,(\mathcal D^{f}T^{cd})\,\gamma^{e}\\
&+\frac{1}{6}\widehat C_{cdef}\,\varepsilon^{cd}{}_{ghj}\,(\mathcal D^{e}T^{fj})\,\gamma^{gh}
\end{aligned}\tag{G104}
```

**G105: R8, whole coefficient matrix.**

```math
\begin{aligned}
&\frac{i}{12}(\mathcal D_{c}T^{c}{}_{d})\,\widehat C_{efgh}\,\gamma^{gh}\gamma^{ef}\gamma^{d}\\
&=-\frac{i}{12}\widehat C_{cdef}\,(\mathcal D_{g}T_{h}{}^{g})\,\gamma^{cdefh}\\
&-\frac{i}{6}\widehat C_{cdef}\,(\mathcal D_{g}T^{dg})\,\gamma^{cef}\\
&-\frac{i}{6}\widehat C_{cdef}\,(\mathcal D_{g}T^{fg})\,\gamma^{cde}\\
&=\frac{1}{12}\widehat C_{cdef}\,\varepsilon^{cdef}{}_{g}\,(\mathcal D_{h}T^{gh})\\
&-\frac{1}{12}\widehat C_{cdef}\,\varepsilon^{cef}{}_{gh}\,(\mathcal D_{j}T^{dj})\,\gamma^{gh}\\
&-\frac{1}{12}\widehat C_{cdef}\,\varepsilon^{cde}{}_{gh}\,(\mathcal D_{j}T^{fj})\,\gamma^{gh}
\end{aligned}\tag{G105}
```

**G106: 1:curvature:1, scalar coefficient.**

```math
\begin{aligned}
&\frac{1}{128}\big(\overline{\mathcal D_{c}\widehat R(Q)_{fg}}\gamma^{c}\gamma^{de}\gamma_{de}\widehat R(Q)^{fg}\big)\\
&=\frac{5}{32}\big(\overline{\widehat R(Q)_{de}}\gamma^{c}\mathcal D_{c}\widehat R(Q)^{de}\big)
\end{aligned}\tag{G106}
```

**G107: 1:curvature:1, vector coefficient.**

```math
\begin{aligned}
&\frac{1}{128}\big(\overline{\mathcal D_{c}\widehat R(Q)_{fg}}\gamma^{c}\gamma^{de}\gamma^{a}\gamma_{de}\widehat R(Q)^{fg}\big)\\
&=-\frac{1}{32}\big(\overline{\widehat R(Q)_{de}}\gamma^{ca}\mathcal D_{c}\widehat R(Q)^{de}\big)\\
&+\frac{1}{32}\big(\overline{\widehat R(Q)_{cd}}\mathcal D^{a}\widehat R(Q)^{cd}\big)
\end{aligned}\tag{G107}
```

**G108: 1:curvature:1, bivector coefficient.**

```math
\begin{aligned}
&-\frac{1}{256}\big(\overline{\mathcal D_{c}\widehat R(Q)_{fg}}\gamma^{c}\gamma^{de}\gamma^{[ab]}\gamma_{de}\widehat R(Q)^{fg}\big)\\
&=-\frac{1}{64}\big(\overline{\widehat R(Q)_{de}}\gamma^{c[ab]}\mathcal D_{c}\widehat R(Q)^{de}\big)\\
&-\frac{1}{32}\big(\overline{\widehat R(Q)_{cd}}\gamma^{[a}\mathcal D^{b]}\widehat R(Q)^{cd}\big)\\
&=\frac{i}{128}\big(\overline{\widehat R(Q)_{fg}}\gamma^{cd}\mathcal D_{e}\widehat R(Q)^{fg}\big)\,\varepsilon_{cd}{}^{e[ab]}\\
&-\frac{1}{32}\big(\overline{\widehat R(Q)_{cd}}\gamma^{[a}\mathcal D^{b]}\widehat R(Q)^{cd}\big)
\end{aligned}\tag{G108}
```

**G109: 1:curvature:2, scalar coefficient.**

```math
\begin{aligned}
&\frac{1}{256}\big(\overline{\mathcal D_{f}\widehat R(Q)_{g}{}^{f}}\gamma^{c}\gamma^{de}\gamma_{de}\widehat R(Q)_{c}{}^{g}\big)\\
&=0
\end{aligned}\tag{G109}
```

**G110: 1:curvature:2, vector coefficient.**

```math
\begin{aligned}
&\frac{1}{256}\big(\overline{\mathcal D_{f}\widehat R(Q)_{g}{}^{f}}\gamma^{c}\gamma^{de}\gamma^{a}\gamma_{de}\widehat R(Q)_{c}{}^{g}\big)\\
&=-\frac{1}{32}\big(\overline{\widehat R(Q)_{c}{}^{a}}\mathcal D_{d}\widehat R(Q)^{cd}\big)
\end{aligned}\tag{G110}
```

**G111: 1:curvature:2, bivector coefficient.**

```math
\begin{aligned}
&-\frac{1}{512}\big(\overline{\mathcal D_{f}\widehat R(Q)_{g}{}^{f}}\gamma^{c}\gamma^{de}\gamma^{[ab]}\gamma_{de}\widehat R(Q)_{c}{}^{g}\big)\\
&=-\frac{1}{32}\big(\overline{\widehat R(Q)_{c}{}^{[a}}\gamma^{b]}\mathcal D_{d}\widehat R(Q)^{cd}\big)
\end{aligned}\tag{G111}
```

**G112: 1:curvature:2, scalar coefficient.**

```math
\begin{aligned}
&-\frac{1}{256}\big(\overline{\mathcal D_{f}\widehat R(Q)_{g}{}^{f}}\gamma^{c}\gamma^{de}\gamma_{de}\widehat R(Q)^{g}{}_{c}\big)\\
&=0
\end{aligned}\tag{G112}
```

**G113: 1:curvature:2, vector coefficient.**

```math
\begin{aligned}
&-\frac{1}{256}\big(\overline{\mathcal D_{f}\widehat R(Q)_{g}{}^{f}}\gamma^{c}\gamma^{de}\gamma^{a}\gamma_{de}\widehat R(Q)^{g}{}_{c}\big)\\
&=-\frac{1}{32}\big(\overline{\widehat R(Q)_{c}{}^{a}}\mathcal D_{d}\widehat R(Q)^{cd}\big)
\end{aligned}\tag{G113}
```

**G114: 1:curvature:2, bivector coefficient.**

```math
\begin{aligned}
&\frac{1}{512}\big(\overline{\mathcal D_{f}\widehat R(Q)_{g}{}^{f}}\gamma^{c}\gamma^{de}\gamma^{[ab]}\gamma_{de}\widehat R(Q)^{g}{}_{c}\big)\\
&=-\frac{1}{32}\big(\overline{\widehat R(Q)_{c}{}^{[a}}\gamma^{b]}\mathcal D_{d}\widehat R(Q)^{cd}\big)
\end{aligned}\tag{G114}
```

**G115: 1:curvature:3, scalar coefficient.**

```math
\begin{aligned}
&\frac{i}{48}\big(\overline{\widehat R(Q)_{cd}}\gamma^{ef}\gamma^{gh}\gamma_{gh}\widehat R(Q)_{ef}\big)\,T^{cd}\\
&=0
\end{aligned}\tag{G115}
```

**G116: 1:curvature:3, vector coefficient.**

```math
\begin{aligned}
&\frac{i}{48}\big(\overline{\widehat R(Q)_{cd}}\gamma^{ef}\gamma^{gh}\gamma^{a}\gamma_{gh}\widehat R(Q)_{ef}\big)\,T^{cd}\\
&=0
\end{aligned}\tag{G116}
```

**G117: 1:curvature:3, bivector coefficient.**

```math
\begin{aligned}
&-\frac{i}{96}\big(\overline{\widehat R(Q)_{cd}}\gamma^{ef}\gamma^{gh}\gamma^{[ab]}\gamma_{gh}\widehat R(Q)_{ef}\big)\,T^{cd}\\
&=-\frac{i}{3}\big(\overline{\widehat R(Q)^{[ab]}}\widehat R(Q)_{cd}\big)\,T^{cd}
\end{aligned}\tag{G117}
```

**G118: 1:curvature:4, scalar coefficient.**

```math
\begin{aligned}
&\frac{3i}{64}\big(\overline{\widehat R(Q)_{hc}}\gamma^{e}\gamma^{d}\gamma^{fg}\gamma_{fg}\widehat R(Q)_{e}{}^{h}\big)\,T^{c}{}_{d}\\
&=\frac{15i}{8}\big(\overline{\widehat R(Q)_{ec}}\widehat R(Q)^{e}{}_{d}\big)\,T^{cd}
\end{aligned}\tag{G118}
```

**G119: 1:curvature:4, vector coefficient.**

```math
\begin{aligned}
&\frac{3i}{64}\big(\overline{\widehat R(Q)_{hc}}\gamma^{e}\gamma^{d}\gamma^{fg}\gamma^{a}\gamma_{fg}\widehat R(Q)_{e}{}^{h}\big)\,T^{c}{}_{d}\\
&=\frac{3i}{8}\big(\overline{\widehat R(Q)_{ec}}\gamma^{a}\widehat R(Q)^{e}{}_{d}\big)\,T^{cd}\\
&-\frac{3i}{8}\big(\overline{\widehat R(Q)_{e}{}^{a}}\gamma^{c}\widehat R(Q)^{e}{}_{d}\big)\,T_{c}{}^{d}
\end{aligned}\tag{G119}
```

**G120: 1:curvature:4, bivector coefficient.**

```math
\begin{aligned}
&-\frac{3i}{128}\big(\overline{\widehat R(Q)_{hc}}\gamma^{e}\gamma^{d}\gamma^{fg}\gamma^{[ab]}\gamma_{fg}\widehat R(Q)_{e}{}^{h}\big)\,T^{c}{}_{d}\\
&=-\frac{3i}{8}\big(\overline{\widehat R(Q)_{e}{}^{[a}}\gamma^{b]c}\widehat R(Q)^{e}{}_{d}\big)\,T_{c}{}^{d}\\
&+\frac{3i}{8}\big(\overline{\widehat R(Q)_{d}{}^{[a}}\widehat R(Q)^{|d|}{}_{|c|}\big)\,T^{|c|b]}
\end{aligned}\tag{G120}
```

**G121: 1:curvature:4, scalar coefficient.**

```math
\begin{aligned}
&-\frac{3i}{64}\big(\overline{\widehat R(Q)_{hc}}\gamma^{e}\gamma^{d}\gamma^{fg}\gamma_{fg}\widehat R(Q)^{h}{}_{e}\big)\,T^{c}{}_{d}\\
&=\frac{15i}{8}\big(\overline{\widehat R(Q)_{ec}}\widehat R(Q)^{e}{}_{d}\big)\,T^{cd}
\end{aligned}\tag{G121}
```

**G122: 1:curvature:4, vector coefficient.**

```math
\begin{aligned}
&-\frac{3i}{64}\big(\overline{\widehat R(Q)_{hc}}\gamma^{e}\gamma^{d}\gamma^{fg}\gamma^{a}\gamma_{fg}\widehat R(Q)^{h}{}_{e}\big)\,T^{c}{}_{d}\\
&=\frac{3i}{8}\big(\overline{\widehat R(Q)_{ec}}\gamma^{a}\widehat R(Q)^{e}{}_{d}\big)\,T^{cd}\\
&-\frac{3i}{8}\big(\overline{\widehat R(Q)_{e}{}^{a}}\gamma^{c}\widehat R(Q)^{e}{}_{d}\big)\,T_{c}{}^{d}
\end{aligned}\tag{G122}
```

**G123: 1:curvature:4, bivector coefficient.**

```math
\begin{aligned}
&\frac{3i}{128}\big(\overline{\widehat R(Q)_{hc}}\gamma^{e}\gamma^{d}\gamma^{fg}\gamma^{[ab]}\gamma_{fg}\widehat R(Q)^{h}{}_{e}\big)\,T^{c}{}_{d}\\
&=-\frac{3i}{8}\big(\overline{\widehat R(Q)_{e}{}^{[a}}\gamma^{b]c}\widehat R(Q)^{e}{}_{d}\big)\,T_{c}{}^{d}\\
&+\frac{3i}{8}\big(\overline{\widehat R(Q)_{d}{}^{[a}}\widehat R(Q)^{|d|}{}_{|c|}\big)\,T^{|c|b]}
\end{aligned}\tag{G123}
```

**G124: 1:curvature:5, scalar coefficient.**

```math
\begin{aligned}
&\frac{3i}{128}\big(\overline{\widehat R(Q)_{gh}}\gamma^{cd}\gamma^{ef}\gamma_{ef}\widehat R(Q)^{gh}\big)\,T_{cd}\\
&=-\frac{15i}{32}\big(\overline{\widehat R(Q)_{ef}}\gamma^{cd}\widehat R(Q)^{ef}\big)\,T_{cd}
\end{aligned}\tag{G124}
```

**G125: 1:curvature:5, vector coefficient.**

```math
\begin{aligned}
&\frac{3i}{128}\big(\overline{\widehat R(Q)_{gh}}\gamma^{cd}\gamma^{ef}\gamma^{a}\gamma_{ef}\widehat R(Q)^{gh}\big)\,T_{cd}\\
&=-\frac{3i}{32}\big(\overline{\widehat R(Q)_{ef}}\gamma^{acd}\widehat R(Q)^{ef}\big)\,T_{cd}\\
&=-\frac{3}{64}\big(\overline{\widehat R(Q)_{gh}}\gamma^{cd}\widehat R(Q)^{gh}\big)\,\varepsilon_{cd}{}^{a}{}_{ef}\,T^{ef}
\end{aligned}\tag{G125}
```

**G126: 1:curvature:5, bivector coefficient.**

```math
\begin{aligned}
&-\frac{3i}{256}\big(\overline{\widehat R(Q)_{gh}}\gamma^{cd}\gamma^{ef}\gamma^{[ab]}\gamma_{ef}\widehat R(Q)^{gh}\big)\,T_{cd}\\
&=-\frac{3i}{16}\big(\overline{\widehat R(Q)_{de}}\gamma^{[a|c|}\widehat R(Q)^{|de|}\big)\,T_{|c|}{}^{b]}
\end{aligned}\tag{G126}
```

**G127: 1:curvature:6, scalar coefficient.**

```math
\begin{aligned}
&-\frac{i}{32}\big(\overline{\widehat R(Q)_{gc}}\gamma^{ef}\gamma_{ef}\widehat R(Q)_{d}{}^{g}\big)\,T^{cd}\\
&=-\frac{5i}{8}\big(\overline{\widehat R(Q)_{ec}}\widehat R(Q)^{e}{}_{d}\big)\,T^{cd}
\end{aligned}\tag{G127}
```

**G128: 1:curvature:6, vector coefficient.**

```math
\begin{aligned}
&-\frac{i}{32}\big(\overline{\widehat R(Q)_{gc}}\gamma^{ef}\gamma^{a}\gamma_{ef}\widehat R(Q)_{d}{}^{g}\big)\,T^{cd}\\
&=-\frac{i}{8}\big(\overline{\widehat R(Q)_{ec}}\gamma^{a}\widehat R(Q)^{e}{}_{d}\big)\,T^{cd}
\end{aligned}\tag{G128}
```

**G129: 1:curvature:6, bivector coefficient.**

```math
\begin{aligned}
&\frac{i}{64}\big(\overline{\widehat R(Q)_{gc}}\gamma^{ef}\gamma^{[ab]}\gamma_{ef}\widehat R(Q)_{d}{}^{g}\big)\,T^{cd}\\
&=0
\end{aligned}\tag{G129}
```

**G130: 1:curvature:6, scalar coefficient.**

```math
\begin{aligned}
&\frac{i}{32}\big(\overline{\widehat R(Q)_{gc}}\gamma^{ef}\gamma_{ef}\widehat R(Q)^{g}{}_{d}\big)\,T^{cd}\\
&=-\frac{5i}{8}\big(\overline{\widehat R(Q)_{ec}}\widehat R(Q)^{e}{}_{d}\big)\,T^{cd}
\end{aligned}\tag{G130}
```

**G131: 1:curvature:6, vector coefficient.**

```math
\begin{aligned}
&\frac{i}{32}\big(\overline{\widehat R(Q)_{gc}}\gamma^{ef}\gamma^{a}\gamma_{ef}\widehat R(Q)^{g}{}_{d}\big)\,T^{cd}\\
&=-\frac{i}{8}\big(\overline{\widehat R(Q)_{ec}}\gamma^{a}\widehat R(Q)^{e}{}_{d}\big)\,T^{cd}
\end{aligned}\tag{G131}
```

**G132: 1:curvature:6, bivector coefficient.**

```math
\begin{aligned}
&-\frac{i}{64}\big(\overline{\widehat R(Q)_{gc}}\gamma^{ef}\gamma^{[ab]}\gamma_{ef}\widehat R(Q)^{g}{}_{d}\big)\,T^{cd}\\
&=0
\end{aligned}\tag{G132}
```

**G133: 1:curvature:7, scalar coefficient.**

```math
\begin{aligned}
&\frac{i}{128}\big(\overline{\widehat R(Q)_{gh}}\gamma^{e}\gamma^{cd}\gamma^{f}\gamma_{ef}\widehat R(Q)^{gh}\big)\,T_{cd}\\
&=-\frac{i}{32}\big(\overline{\widehat R(Q)_{ef}}\gamma^{cd}\widehat R(Q)^{ef}\big)\,T_{cd}
\end{aligned}\tag{G133}
```

**G134: 1:curvature:7, vector coefficient.**

```math
\begin{aligned}
&\frac{i}{128}\big(\overline{\widehat R(Q)_{gh}}\gamma^{e}\gamma^{cd}\gamma^{f}\gamma^{a}\gamma_{ef}\widehat R(Q)^{gh}\big)\,T_{cd}\\
&=\frac{i}{32}\big(\overline{\widehat R(Q)_{ef}}\gamma^{acd}\widehat R(Q)^{ef}\big)\,T_{cd}\\
&=\frac{1}{64}\big(\overline{\widehat R(Q)_{gh}}\gamma^{cd}\widehat R(Q)^{gh}\big)\,\varepsilon_{cd}{}^{a}{}_{ef}\,T^{ef}
\end{aligned}\tag{G134}
```

**G135: 1:curvature:7, bivector coefficient.**

```math
\begin{aligned}
&-\frac{i}{256}\big(\overline{\widehat R(Q)_{gh}}\gamma^{e}\gamma^{cd}\gamma^{f}\gamma^{[ab]}\gamma_{ef}\widehat R(Q)^{gh}\big)\,T_{cd}\\
&=0
\end{aligned}\tag{G135}
```

**G136: 1:curvature:7, scalar coefficient.**

```math
\begin{aligned}
&-\frac{i}{128}\big(\overline{\widehat R(Q)_{gh}}\gamma^{e}\gamma^{cd}\gamma^{f}\gamma_{fe}\widehat R(Q)^{gh}\big)\,T_{cd}\\
&=-\frac{i}{32}\big(\overline{\widehat R(Q)_{ef}}\gamma^{cd}\widehat R(Q)^{ef}\big)\,T_{cd}
\end{aligned}\tag{G136}
```

**G137: 1:curvature:7, vector coefficient.**

```math
\begin{aligned}
&-\frac{i}{128}\big(\overline{\widehat R(Q)_{gh}}\gamma^{e}\gamma^{cd}\gamma^{f}\gamma^{a}\gamma_{fe}\widehat R(Q)^{gh}\big)\,T_{cd}\\
&=\frac{i}{32}\big(\overline{\widehat R(Q)_{ef}}\gamma^{acd}\widehat R(Q)^{ef}\big)\,T_{cd}\\
&=\frac{1}{64}\big(\overline{\widehat R(Q)_{gh}}\gamma^{cd}\widehat R(Q)^{gh}\big)\,\varepsilon_{cd}{}^{a}{}_{ef}\,T^{ef}
\end{aligned}\tag{G137}
```

**G138: 1:curvature:7, bivector coefficient.**

```math
\begin{aligned}
&\frac{i}{256}\big(\overline{\widehat R(Q)_{gh}}\gamma^{e}\gamma^{cd}\gamma^{f}\gamma^{[ab]}\gamma_{fe}\widehat R(Q)^{gh}\big)\,T_{cd}\\
&=0
\end{aligned}\tag{G138}
```

**G139: 1:curvature:8, scalar coefficient.**

```math
\begin{aligned}
&\frac{1}{256}\big(\overline{\mathcal D_{e}\widehat R(Q)_{fd}}\gamma^{c}\gamma_{c}{}^{d}\widehat R(Q)^{ef}\big)\\
&=0
\end{aligned}\tag{G139}
```

**G140: 1:curvature:8, vector coefficient.**

```math
\begin{aligned}
&\frac{1}{256}\big(\overline{\mathcal D_{e}\widehat R(Q)_{fd}}\gamma^{c}\gamma^{a}\gamma_{c}{}^{d}\widehat R(Q)^{ef}\big)\\
&=\frac{3}{128}\big(\overline{\widehat R(Q)_{cd}}\mathcal D^{c}\widehat R(Q)^{da}\big)
\end{aligned}\tag{G140}
```

**G141: 1:curvature:8, bivector coefficient.**

```math
\begin{aligned}
&-\frac{1}{512}\big(\overline{\mathcal D_{e}\widehat R(Q)_{fd}}\gamma^{c}\gamma^{[ab]}\gamma_{c}{}^{d}\widehat R(Q)^{ef}\big)\\
&=\frac{1}{128}\big(\overline{\widehat R(Q)_{cd}}\gamma^{[a}\mathcal D^{|c|}\widehat R(Q)^{|d|b]}\big)
\end{aligned}\tag{G141}
```

**G142: 1:curvature:8, scalar coefficient.**

```math
\begin{aligned}
&-\frac{1}{256}\big(\overline{\mathcal D_{e}\widehat R(Q)_{fd}}\gamma^{c}\gamma^{d}{}_{c}\widehat R(Q)^{ef}\big)\\
&=0
\end{aligned}\tag{G142}
```

**G143: 1:curvature:8, vector coefficient.**

```math
\begin{aligned}
&-\frac{1}{256}\big(\overline{\mathcal D_{e}\widehat R(Q)_{fd}}\gamma^{c}\gamma^{a}\gamma^{d}{}_{c}\widehat R(Q)^{ef}\big)\\
&=\frac{3}{128}\big(\overline{\widehat R(Q)_{cd}}\mathcal D^{c}\widehat R(Q)^{da}\big)
\end{aligned}\tag{G143}
```

**G144: 1:curvature:8, bivector coefficient.**

```math
\begin{aligned}
&\frac{1}{512}\big(\overline{\mathcal D_{e}\widehat R(Q)_{fd}}\gamma^{c}\gamma^{[ab]}\gamma^{d}{}_{c}\widehat R(Q)^{ef}\big)\\
&=\frac{1}{128}\big(\overline{\widehat R(Q)_{cd}}\gamma^{[a}\mathcal D^{|c|}\widehat R(Q)^{|d|b]}\big)
\end{aligned}\tag{G144}
```

**G145: 1:curvature:8, scalar coefficient.**

```math
\begin{aligned}
&-\frac{1}{256}\big(\overline{\mathcal D_{e}\widehat R(Q)_{fd}}\gamma^{c}\gamma_{c}{}^{d}\widehat R(Q)^{fe}\big)\\
&=0
\end{aligned}\tag{G145}
```

**G146: 1:curvature:8, vector coefficient.**

```math
\begin{aligned}
&-\frac{1}{256}\big(\overline{\mathcal D_{e}\widehat R(Q)_{fd}}\gamma^{c}\gamma^{a}\gamma_{c}{}^{d}\widehat R(Q)^{fe}\big)\\
&=\frac{3}{128}\big(\overline{\widehat R(Q)_{cd}}\mathcal D^{c}\widehat R(Q)^{da}\big)
\end{aligned}\tag{G146}
```

**G147: 1:curvature:8, bivector coefficient.**

```math
\begin{aligned}
&\frac{1}{512}\big(\overline{\mathcal D_{e}\widehat R(Q)_{fd}}\gamma^{c}\gamma^{[ab]}\gamma_{c}{}^{d}\widehat R(Q)^{fe}\big)\\
&=\frac{1}{128}\big(\overline{\widehat R(Q)_{cd}}\gamma^{[a}\mathcal D^{|c|}\widehat R(Q)^{|d|b]}\big)
\end{aligned}\tag{G147}
```

**G148: 1:curvature:8, scalar coefficient.**

```math
\begin{aligned}
&\frac{1}{256}\big(\overline{\mathcal D_{e}\widehat R(Q)_{fd}}\gamma^{c}\gamma^{d}{}_{c}\widehat R(Q)^{fe}\big)\\
&=0
\end{aligned}\tag{G148}
```

**G149: 1:curvature:8, vector coefficient.**

```math
\begin{aligned}
&\frac{1}{256}\big(\overline{\mathcal D_{e}\widehat R(Q)_{fd}}\gamma^{c}\gamma^{a}\gamma^{d}{}_{c}\widehat R(Q)^{fe}\big)\\
&=\frac{3}{128}\big(\overline{\widehat R(Q)_{cd}}\mathcal D^{c}\widehat R(Q)^{da}\big)
\end{aligned}\tag{G149}
```

**G150: 1:curvature:8, bivector coefficient.**

```math
\begin{aligned}
&-\frac{1}{512}\big(\overline{\mathcal D_{e}\widehat R(Q)_{fd}}\gamma^{c}\gamma^{[ab]}\gamma^{d}{}_{c}\widehat R(Q)^{fe}\big)\\
&=\frac{1}{128}\big(\overline{\widehat R(Q)_{cd}}\gamma^{[a}\mathcal D^{|c|}\widehat R(Q)^{|d|b]}\big)
\end{aligned}\tag{G150}
```

**G151: 1:curvature:9, scalar coefficient.**

```math
\begin{aligned}
&-\frac{i}{256}\big(\overline{\widehat R(Q)_{hg}}\gamma^{e}\gamma^{cd}\gamma^{f}\gamma_{e}{}^{g}\widehat R(Q)_{f}{}^{h}\big)\,T_{cd}\\
&=\frac{i}{128}\big(\overline{\widehat R(Q)_{ef}}\gamma^{cd}\widehat R(Q)^{ef}\big)\,T_{cd}\\
&-\frac{i}{16}\big(\overline{\widehat R(Q)_{ec}}\widehat R(Q)^{e}{}_{d}\big)\,T^{cd}
\end{aligned}\tag{G151}
```

**G152: 1:curvature:9, vector coefficient.**

```math
\begin{aligned}
&-\frac{i}{256}\big(\overline{\widehat R(Q)_{hg}}\gamma^{e}\gamma^{cd}\gamma^{f}\gamma^{a}\gamma_{e}{}^{g}\widehat R(Q)_{f}{}^{h}\big)\,T_{cd}\\
&=\frac{3i}{128}\big(\overline{\widehat R(Q)_{ef}}\gamma^{acd}\widehat R(Q)^{ef}\big)\,T_{cd}\\
&+\frac{3i}{32}\big(\overline{\widehat R(Q)_{e}{}^{a}}\gamma^{c}\widehat R(Q)^{e}{}_{d}\big)\,T_{c}{}^{d}\\
&-\frac{i}{16}\big(\overline{\widehat R(Q)_{ec}}\gamma^{a}\widehat R(Q)^{e}{}_{d}\big)\,T^{cd}\\
&=\frac{3}{256}\big(\overline{\widehat R(Q)_{gh}}\gamma^{cd}\widehat R(Q)^{gh}\big)\,\varepsilon_{cd}{}^{a}{}_{ef}\,T^{ef}\\
&+\frac{3i}{32}\big(\overline{\widehat R(Q)_{e}{}^{a}}\gamma^{c}\widehat R(Q)^{e}{}_{d}\big)\,T_{c}{}^{d}\\
&-\frac{i}{16}\big(\overline{\widehat R(Q)_{ec}}\gamma^{a}\widehat R(Q)^{e}{}_{d}\big)\,T^{cd}
\end{aligned}\tag{G152}
```

**G153: 1:curvature:9, bivector coefficient.**

```math
\begin{aligned}
&\frac{i}{512}\big(\overline{\widehat R(Q)_{hg}}\gamma^{e}\gamma^{cd}\gamma^{f}\gamma^{[ab]}\gamma_{e}{}^{g}\widehat R(Q)_{f}{}^{h}\big)\,T_{cd}\\
&=-\frac{i}{32}\big(\overline{\widehat R(Q)_{e}{}^{[a}}\gamma^{b]c}\widehat R(Q)^{e}{}_{d}\big)\,T_{c}{}^{d}\\
&-\frac{i}{64}\big(\overline{\widehat R(Q)_{de}}\gamma^{[a|c|}\widehat R(Q)^{|de|}\big)\,T_{|c|}{}^{b]}\\
&+\frac{i}{32}\big(\overline{\widehat R(Q)_{d}{}^{[a}}\widehat R(Q)^{|d|}{}_{|c|}\big)\,T^{|c|b]}
\end{aligned}\tag{G153}
```

**G154: 1:curvature:9, scalar coefficient.**

```math
\begin{aligned}
&\frac{i}{256}\big(\overline{\widehat R(Q)_{hg}}\gamma^{e}\gamma^{cd}\gamma^{f}\gamma^{g}{}_{e}\widehat R(Q)_{f}{}^{h}\big)\,T_{cd}\\
&=\frac{i}{128}\big(\overline{\widehat R(Q)_{ef}}\gamma^{cd}\widehat R(Q)^{ef}\big)\,T_{cd}\\
&-\frac{i}{16}\big(\overline{\widehat R(Q)_{ec}}\widehat R(Q)^{e}{}_{d}\big)\,T^{cd}
\end{aligned}\tag{G154}
```

**G155: 1:curvature:9, vector coefficient.**

```math
\begin{aligned}
&\frac{i}{256}\big(\overline{\widehat R(Q)_{hg}}\gamma^{e}\gamma^{cd}\gamma^{f}\gamma^{a}\gamma^{g}{}_{e}\widehat R(Q)_{f}{}^{h}\big)\,T_{cd}\\
&=\frac{3i}{128}\big(\overline{\widehat R(Q)_{ef}}\gamma^{acd}\widehat R(Q)^{ef}\big)\,T_{cd}\\
&+\frac{3i}{32}\big(\overline{\widehat R(Q)_{e}{}^{a}}\gamma^{c}\widehat R(Q)^{e}{}_{d}\big)\,T_{c}{}^{d}\\
&-\frac{i}{16}\big(\overline{\widehat R(Q)_{ec}}\gamma^{a}\widehat R(Q)^{e}{}_{d}\big)\,T^{cd}\\
&=\frac{3}{256}\big(\overline{\widehat R(Q)_{gh}}\gamma^{cd}\widehat R(Q)^{gh}\big)\,\varepsilon_{cd}{}^{a}{}_{ef}\,T^{ef}\\
&+\frac{3i}{32}\big(\overline{\widehat R(Q)_{e}{}^{a}}\gamma^{c}\widehat R(Q)^{e}{}_{d}\big)\,T_{c}{}^{d}\\
&-\frac{i}{16}\big(\overline{\widehat R(Q)_{ec}}\gamma^{a}\widehat R(Q)^{e}{}_{d}\big)\,T^{cd}
\end{aligned}\tag{G155}
```

**G156: 1:curvature:9, bivector coefficient.**

```math
\begin{aligned}
&-\frac{i}{512}\big(\overline{\widehat R(Q)_{hg}}\gamma^{e}\gamma^{cd}\gamma^{f}\gamma^{[ab]}\gamma^{g}{}_{e}\widehat R(Q)_{f}{}^{h}\big)\,T_{cd}\\
&=-\frac{i}{32}\big(\overline{\widehat R(Q)_{e}{}^{[a}}\gamma^{b]c}\widehat R(Q)^{e}{}_{d}\big)\,T_{c}{}^{d}\\
&-\frac{i}{64}\big(\overline{\widehat R(Q)_{de}}\gamma^{[a|c|}\widehat R(Q)^{|de|}\big)\,T_{|c|}{}^{b]}\\
&+\frac{i}{32}\big(\overline{\widehat R(Q)_{d}{}^{[a}}\widehat R(Q)^{|d|}{}_{|c|}\big)\,T^{|c|b]}
\end{aligned}\tag{G156}
```

**G157: 1:curvature:9, scalar coefficient.**

```math
\begin{aligned}
&\frac{i}{256}\big(\overline{\widehat R(Q)_{hg}}\gamma^{e}\gamma^{cd}\gamma^{f}\gamma_{e}{}^{g}\widehat R(Q)^{h}{}_{f}\big)\,T_{cd}\\
&=\frac{i}{128}\big(\overline{\widehat R(Q)_{ef}}\gamma^{cd}\widehat R(Q)^{ef}\big)\,T_{cd}\\
&-\frac{i}{16}\big(\overline{\widehat R(Q)_{ec}}\widehat R(Q)^{e}{}_{d}\big)\,T^{cd}
\end{aligned}\tag{G157}
```

**G158: 1:curvature:9, vector coefficient.**

```math
\begin{aligned}
&\frac{i}{256}\big(\overline{\widehat R(Q)_{hg}}\gamma^{e}\gamma^{cd}\gamma^{f}\gamma^{a}\gamma_{e}{}^{g}\widehat R(Q)^{h}{}_{f}\big)\,T_{cd}\\
&=\frac{3i}{128}\big(\overline{\widehat R(Q)_{ef}}\gamma^{acd}\widehat R(Q)^{ef}\big)\,T_{cd}\\
&+\frac{3i}{32}\big(\overline{\widehat R(Q)_{e}{}^{a}}\gamma^{c}\widehat R(Q)^{e}{}_{d}\big)\,T_{c}{}^{d}\\
&-\frac{i}{16}\big(\overline{\widehat R(Q)_{ec}}\gamma^{a}\widehat R(Q)^{e}{}_{d}\big)\,T^{cd}\\
&=\frac{3}{256}\big(\overline{\widehat R(Q)_{gh}}\gamma^{cd}\widehat R(Q)^{gh}\big)\,\varepsilon_{cd}{}^{a}{}_{ef}\,T^{ef}\\
&+\frac{3i}{32}\big(\overline{\widehat R(Q)_{e}{}^{a}}\gamma^{c}\widehat R(Q)^{e}{}_{d}\big)\,T_{c}{}^{d}\\
&-\frac{i}{16}\big(\overline{\widehat R(Q)_{ec}}\gamma^{a}\widehat R(Q)^{e}{}_{d}\big)\,T^{cd}
\end{aligned}\tag{G158}
```

**G159: 1:curvature:9, bivector coefficient.**

```math
\begin{aligned}
&-\frac{i}{512}\big(\overline{\widehat R(Q)_{hg}}\gamma^{e}\gamma^{cd}\gamma^{f}\gamma^{[ab]}\gamma_{e}{}^{g}\widehat R(Q)^{h}{}_{f}\big)\,T_{cd}\\
&=-\frac{i}{32}\big(\overline{\widehat R(Q)_{e}{}^{[a}}\gamma^{b]c}\widehat R(Q)^{e}{}_{d}\big)\,T_{c}{}^{d}\\
&-\frac{i}{64}\big(\overline{\widehat R(Q)_{de}}\gamma^{[a|c|}\widehat R(Q)^{|de|}\big)\,T_{|c|}{}^{b]}\\
&+\frac{i}{32}\big(\overline{\widehat R(Q)_{d}{}^{[a}}\widehat R(Q)^{|d|}{}_{|c|}\big)\,T^{|c|b]}
\end{aligned}\tag{G159}
```

**G160: 1:curvature:9, scalar coefficient.**

```math
\begin{aligned}
&-\frac{i}{256}\big(\overline{\widehat R(Q)_{hg}}\gamma^{e}\gamma^{cd}\gamma^{f}\gamma^{g}{}_{e}\widehat R(Q)^{h}{}_{f}\big)\,T_{cd}\\
&=\frac{i}{128}\big(\overline{\widehat R(Q)_{ef}}\gamma^{cd}\widehat R(Q)^{ef}\big)\,T_{cd}\\
&-\frac{i}{16}\big(\overline{\widehat R(Q)_{ec}}\widehat R(Q)^{e}{}_{d}\big)\,T^{cd}
\end{aligned}\tag{G160}
```

**G161: 1:curvature:9, vector coefficient.**

```math
\begin{aligned}
&-\frac{i}{256}\big(\overline{\widehat R(Q)_{hg}}\gamma^{e}\gamma^{cd}\gamma^{f}\gamma^{a}\gamma^{g}{}_{e}\widehat R(Q)^{h}{}_{f}\big)\,T_{cd}\\
&=\frac{3i}{128}\big(\overline{\widehat R(Q)_{ef}}\gamma^{acd}\widehat R(Q)^{ef}\big)\,T_{cd}\\
&+\frac{3i}{32}\big(\overline{\widehat R(Q)_{e}{}^{a}}\gamma^{c}\widehat R(Q)^{e}{}_{d}\big)\,T_{c}{}^{d}\\
&-\frac{i}{16}\big(\overline{\widehat R(Q)_{ec}}\gamma^{a}\widehat R(Q)^{e}{}_{d}\big)\,T^{cd}\\
&=\frac{3}{256}\big(\overline{\widehat R(Q)_{gh}}\gamma^{cd}\widehat R(Q)^{gh}\big)\,\varepsilon_{cd}{}^{a}{}_{ef}\,T^{ef}\\
&+\frac{3i}{32}\big(\overline{\widehat R(Q)_{e}{}^{a}}\gamma^{c}\widehat R(Q)^{e}{}_{d}\big)\,T_{c}{}^{d}\\
&-\frac{i}{16}\big(\overline{\widehat R(Q)_{ec}}\gamma^{a}\widehat R(Q)^{e}{}_{d}\big)\,T^{cd}
\end{aligned}\tag{G161}
```

**G162: 1:curvature:9, bivector coefficient.**

```math
\begin{aligned}
&\frac{i}{512}\big(\overline{\widehat R(Q)_{hg}}\gamma^{e}\gamma^{cd}\gamma^{f}\gamma^{[ab]}\gamma^{g}{}_{e}\widehat R(Q)^{h}{}_{f}\big)\,T_{cd}\\
&=-\frac{i}{32}\big(\overline{\widehat R(Q)_{e}{}^{[a}}\gamma^{b]c}\widehat R(Q)^{e}{}_{d}\big)\,T_{c}{}^{d}\\
&-\frac{i}{64}\big(\overline{\widehat R(Q)_{de}}\gamma^{[a|c|}\widehat R(Q)^{|de|}\big)\,T_{|c|}{}^{b]}\\
&+\frac{i}{32}\big(\overline{\widehat R(Q)_{d}{}^{[a}}\widehat R(Q)^{|d|}{}_{|c|}\big)\,T^{|c|b]}
\end{aligned}\tag{G162}
```

**G163: 1:curvature:10, scalar coefficient.**

```math
\begin{aligned}
&-\frac{1}{256}\big(\overline{\mathcal D_{f}\widehat R(Q)_{de}}\gamma^{c}\gamma^{de}\widehat R(Q)_{c}{}^{f}\big)\\
&=0
\end{aligned}\tag{G163}
```

**G164: 1:curvature:10, vector coefficient.**

```math
\begin{aligned}
&-\frac{1}{256}\big(\overline{\mathcal D_{f}\widehat R(Q)_{de}}\gamma^{c}\gamma^{a}\gamma^{de}\widehat R(Q)_{c}{}^{f}\big)\\
&=\frac{1}{32}\big(\overline{\widehat R(Q)_{cd}}\mathcal D^{c}\widehat R(Q)^{da}\big)
\end{aligned}\tag{G164}
```

**G165: 1:curvature:10, bivector coefficient.**

```math
\begin{aligned}
&\frac{1}{512}\big(\overline{\mathcal D_{f}\widehat R(Q)_{de}}\gamma^{c}\gamma^{[ab]}\gamma^{de}\widehat R(Q)_{c}{}^{f}\big)\\
&=\frac{1}{32}\big(\overline{\widehat R(Q)_{cd}}\gamma^{[a}\mathcal D^{|c|}\widehat R(Q)^{|d|b]}\big)
\end{aligned}\tag{G165}
```

**G166: 1:curvature:10, scalar coefficient.**

```math
\begin{aligned}
&\frac{1}{256}\big(\overline{\mathcal D_{f}\widehat R(Q)_{de}}\gamma^{c}\gamma^{de}\widehat R(Q)^{f}{}_{c}\big)\\
&=0
\end{aligned}\tag{G166}
```

**G167: 1:curvature:10, vector coefficient.**

```math
\begin{aligned}
&\frac{1}{256}\big(\overline{\mathcal D_{f}\widehat R(Q)_{de}}\gamma^{c}\gamma^{a}\gamma^{de}\widehat R(Q)^{f}{}_{c}\big)\\
&=\frac{1}{32}\big(\overline{\widehat R(Q)_{cd}}\mathcal D^{c}\widehat R(Q)^{da}\big)
\end{aligned}\tag{G167}
```

**G168: 1:curvature:10, bivector coefficient.**

```math
\begin{aligned}
&-\frac{1}{512}\big(\overline{\mathcal D_{f}\widehat R(Q)_{de}}\gamma^{c}\gamma^{[ab]}\gamma^{de}\widehat R(Q)^{f}{}_{c}\big)\\
&=\frac{1}{32}\big(\overline{\widehat R(Q)_{cd}}\gamma^{[a}\mathcal D^{|c|}\widehat R(Q)^{|d|b]}\big)
\end{aligned}\tag{G168}
```

**G169: 1:curvature:11, scalar coefficient.**

```math
\begin{aligned}
&\frac{i}{256}\big(\overline{\widehat R(Q)_{gh}}\gamma^{e}\gamma^{cd}\gamma^{f}\gamma^{gh}\widehat R(Q)_{ef}\big)\,T_{cd}\\
&=-\frac{3i}{128}\big(\overline{\widehat R(Q)_{ef}}\gamma^{cd}\widehat R(Q)^{ef}\big)\,T_{cd}\\
&+\frac{3i}{32}\big(\overline{\widehat R(Q)_{ec}}\widehat R(Q)^{e}{}_{d}\big)\,T^{cd}
\end{aligned}\tag{G169}
```

**G170: 1:curvature:11, vector coefficient.**

```math
\begin{aligned}
&\frac{i}{256}\big(\overline{\widehat R(Q)_{gh}}\gamma^{e}\gamma^{cd}\gamma^{f}\gamma^{a}\gamma^{gh}\widehat R(Q)_{ef}\big)\,T_{cd}\\
&=-\frac{i}{64}\big(\overline{\widehat R(Q)_{ef}}\gamma^{acd}\widehat R(Q)^{ef}\big)\,T_{cd}\\
&-\frac{i}{4}\big(\overline{\widehat R(Q)_{e}{}^{a}}\gamma^{c}\widehat R(Q)^{e}{}_{d}\big)\,T_{c}{}^{d}\\
&+\frac{i}{16}\big(\overline{\widehat R(Q)_{ec}}\gamma^{a}\widehat R(Q)^{e}{}_{d}\big)\,T^{cd}\\
&=-\frac{1}{128}\big(\overline{\widehat R(Q)_{gh}}\gamma^{cd}\widehat R(Q)^{gh}\big)\,\varepsilon_{cd}{}^{a}{}_{ef}\,T^{ef}\\
&-\frac{i}{4}\big(\overline{\widehat R(Q)_{e}{}^{a}}\gamma^{c}\widehat R(Q)^{e}{}_{d}\big)\,T_{c}{}^{d}\\
&+\frac{i}{16}\big(\overline{\widehat R(Q)_{ec}}\gamma^{a}\widehat R(Q)^{e}{}_{d}\big)\,T^{cd}
\end{aligned}\tag{G170}
```

**G171: 1:curvature:11, bivector coefficient.**

```math
\begin{aligned}
&-\frac{i}{512}\big(\overline{\widehat R(Q)_{gh}}\gamma^{e}\gamma^{cd}\gamma^{f}\gamma^{[ab]}\gamma^{gh}\widehat R(Q)_{ef}\big)\,T_{cd}\\
&=\frac{3i}{32}\big(\overline{\widehat R(Q)_{e}{}^{[a}}\gamma^{b]c}\widehat R(Q)^{e}{}_{d}\big)\,T_{c}{}^{d}\\
&+\frac{7i}{64}\big(\overline{\widehat R(Q)^{[ab]}}\widehat R(Q)_{cd}\big)\,T^{cd}\\
&+\frac{3i}{64}\big(\overline{\widehat R(Q)_{de}}\gamma^{[a|c|}\widehat R(Q)^{|de|}\big)\,T_{|c|}{}^{b]}\\
&-\frac{5i}{16}\big(\overline{\widehat R(Q)_{d}{}^{[a}}\widehat R(Q)^{|d|}{}_{|c|}\big)\,T^{|c|b]}
\end{aligned}\tag{G171}
```

**G172: 1:curvature:11, scalar coefficient.**

```math
\begin{aligned}
&-\frac{i}{256}\big(\overline{\widehat R(Q)_{gh}}\gamma^{e}\gamma^{cd}\gamma^{f}\gamma^{gh}\widehat R(Q)_{fe}\big)\,T_{cd}\\
&=-\frac{3i}{128}\big(\overline{\widehat R(Q)_{ef}}\gamma^{cd}\widehat R(Q)^{ef}\big)\,T_{cd}\\
&+\frac{3i}{32}\big(\overline{\widehat R(Q)_{ec}}\widehat R(Q)^{e}{}_{d}\big)\,T^{cd}
\end{aligned}\tag{G172}
```

**G173: 1:curvature:11, vector coefficient.**

```math
\begin{aligned}
&-\frac{i}{256}\big(\overline{\widehat R(Q)_{gh}}\gamma^{e}\gamma^{cd}\gamma^{f}\gamma^{a}\gamma^{gh}\widehat R(Q)_{fe}\big)\,T_{cd}\\
&=-\frac{i}{64}\big(\overline{\widehat R(Q)_{ef}}\gamma^{acd}\widehat R(Q)^{ef}\big)\,T_{cd}\\
&-\frac{i}{4}\big(\overline{\widehat R(Q)_{e}{}^{a}}\gamma^{c}\widehat R(Q)^{e}{}_{d}\big)\,T_{c}{}^{d}\\
&+\frac{i}{16}\big(\overline{\widehat R(Q)_{ec}}\gamma^{a}\widehat R(Q)^{e}{}_{d}\big)\,T^{cd}\\
&=-\frac{1}{128}\big(\overline{\widehat R(Q)_{gh}}\gamma^{cd}\widehat R(Q)^{gh}\big)\,\varepsilon_{cd}{}^{a}{}_{ef}\,T^{ef}\\
&-\frac{i}{4}\big(\overline{\widehat R(Q)_{e}{}^{a}}\gamma^{c}\widehat R(Q)^{e}{}_{d}\big)\,T_{c}{}^{d}\\
&+\frac{i}{16}\big(\overline{\widehat R(Q)_{ec}}\gamma^{a}\widehat R(Q)^{e}{}_{d}\big)\,T^{cd}
\end{aligned}\tag{G173}
```

**G174: 1:curvature:11, bivector coefficient.**

```math
\begin{aligned}
&\frac{i}{512}\big(\overline{\widehat R(Q)_{gh}}\gamma^{e}\gamma^{cd}\gamma^{f}\gamma^{[ab]}\gamma^{gh}\widehat R(Q)_{fe}\big)\,T_{cd}\\
&=\frac{3i}{32}\big(\overline{\widehat R(Q)_{e}{}^{[a}}\gamma^{b]c}\widehat R(Q)^{e}{}_{d}\big)\,T_{c}{}^{d}\\
&+\frac{7i}{64}\big(\overline{\widehat R(Q)^{[ab]}}\widehat R(Q)_{cd}\big)\,T^{cd}\\
&+\frac{3i}{64}\big(\overline{\widehat R(Q)_{de}}\gamma^{[a|c|}\widehat R(Q)^{|de|}\big)\,T_{|c|}{}^{b]}\\
&-\frac{5i}{16}\big(\overline{\widehat R(Q)_{d}{}^{[a}}\widehat R(Q)^{|d|}{}_{|c|}\big)\,T^{|c|b]}
\end{aligned}\tag{G174}
```

**G175: 1:curvature:12, scalar coefficient.**

```math
\begin{aligned}
&\frac{1}{32}\big(\overline{\mathcal D_{f}\chi}\gamma^{e}\gamma^{d}{}_{e}\widehat R(Q)^{f}{}_{c}\big)\,\eta^{c}{}_{d}\\
&=0
\end{aligned}\tag{G175}
```

**G176: 1:curvature:12, vector coefficient.**

```math
\begin{aligned}
&\frac{1}{32}\big(\overline{\mathcal D_{f}\chi}\gamma^{e}\gamma^{a}\gamma^{d}{}_{e}\widehat R(Q)^{f}{}_{c}\big)\,\eta^{c}{}_{d}\\
&=-\frac{1}{16}\big(\overline{\widehat R(Q)_{c}{}^{a}}\mathcal D^{c}\chi\big)
\end{aligned}\tag{G176}
```

**G177: 1:curvature:12, bivector coefficient.**

```math
\begin{aligned}
&-\frac{1}{64}\big(\overline{\mathcal D_{f}\chi}\gamma^{e}\gamma^{[ab]}\gamma^{d}{}_{e}\widehat R(Q)^{f}{}_{c}\big)\,\eta^{c}{}_{d}\\
&=\frac{1}{16}\big(\overline{\widehat R(Q)_{c}{}^{[a}}\gamma^{b]}\mathcal D^{c}\chi\big)
\end{aligned}\tag{G177}
```

**G178: 1:curvature:12, scalar coefficient.**

```math
\begin{aligned}
&-\frac{1}{32}\big(\overline{\mathcal D_{f}\chi}\gamma^{e}\gamma_{e}{}^{d}\widehat R(Q)^{f}{}_{c}\big)\,\eta^{c}{}_{d}\\
&=0
\end{aligned}\tag{G178}
```

**G179: 1:curvature:12, vector coefficient.**

```math
\begin{aligned}
&-\frac{1}{32}\big(\overline{\mathcal D_{f}\chi}\gamma^{e}\gamma^{a}\gamma_{e}{}^{d}\widehat R(Q)^{f}{}_{c}\big)\,\eta^{c}{}_{d}\\
&=-\frac{1}{16}\big(\overline{\widehat R(Q)_{c}{}^{a}}\mathcal D^{c}\chi\big)
\end{aligned}\tag{G179}
```

**G180: 1:curvature:12, bivector coefficient.**

```math
\begin{aligned}
&\frac{1}{64}\big(\overline{\mathcal D_{f}\chi}\gamma^{e}\gamma^{[ab]}\gamma_{e}{}^{d}\widehat R(Q)^{f}{}_{c}\big)\,\eta^{c}{}_{d}\\
&=\frac{1}{16}\big(\overline{\widehat R(Q)_{c}{}^{[a}}\gamma^{b]}\mathcal D^{c}\chi\big)
\end{aligned}\tag{G180}
```

**G181: 1:curvature:12, scalar coefficient.**

```math
\begin{aligned}
&-\frac{1}{32}\big(\overline{\mathcal D_{f}\chi}\gamma^{e}\gamma^{d}{}_{e}\widehat R(Q)_{c}{}^{f}\big)\,\eta^{c}{}_{d}\\
&=0
\end{aligned}\tag{G181}
```

**G182: 1:curvature:12, vector coefficient.**

```math
\begin{aligned}
&-\frac{1}{32}\big(\overline{\mathcal D_{f}\chi}\gamma^{e}\gamma^{a}\gamma^{d}{}_{e}\widehat R(Q)_{c}{}^{f}\big)\,\eta^{c}{}_{d}\\
&=-\frac{1}{16}\big(\overline{\widehat R(Q)_{c}{}^{a}}\mathcal D^{c}\chi\big)
\end{aligned}\tag{G182}
```

**G183: 1:curvature:12, bivector coefficient.**

```math
\begin{aligned}
&\frac{1}{64}\big(\overline{\mathcal D_{f}\chi}\gamma^{e}\gamma^{[ab]}\gamma^{d}{}_{e}\widehat R(Q)_{c}{}^{f}\big)\,\eta^{c}{}_{d}\\
&=\frac{1}{16}\big(\overline{\widehat R(Q)_{c}{}^{[a}}\gamma^{b]}\mathcal D^{c}\chi\big)
\end{aligned}\tag{G183}
```

**G184: 1:curvature:12, scalar coefficient.**

```math
\begin{aligned}
&\frac{1}{32}\big(\overline{\mathcal D_{f}\chi}\gamma^{e}\gamma_{e}{}^{d}\widehat R(Q)_{c}{}^{f}\big)\,\eta^{c}{}_{d}\\
&=0
\end{aligned}\tag{G184}
```

**G185: 1:curvature:12, vector coefficient.**

```math
\begin{aligned}
&\frac{1}{32}\big(\overline{\mathcal D_{f}\chi}\gamma^{e}\gamma^{a}\gamma_{e}{}^{d}\widehat R(Q)_{c}{}^{f}\big)\,\eta^{c}{}_{d}\\
&=-\frac{1}{16}\big(\overline{\widehat R(Q)_{c}{}^{a}}\mathcal D^{c}\chi\big)
\end{aligned}\tag{G185}
```

**G186: 1:curvature:12, bivector coefficient.**

```math
\begin{aligned}
&-\frac{1}{64}\big(\overline{\mathcal D_{f}\chi}\gamma^{e}\gamma^{[ab]}\gamma_{e}{}^{d}\widehat R(Q)_{c}{}^{f}\big)\,\eta^{c}{}_{d}\\
&=\frac{1}{16}\big(\overline{\widehat R(Q)_{c}{}^{[a}}\gamma^{b]}\mathcal D^{c}\chi\big)
\end{aligned}\tag{G186}
```

**G187: 1:curvature:13, scalar coefficient.**

```math
\begin{aligned}
&-\frac{i}{32}\big(\bar\chi\gamma^{g}\gamma^{ef}\gamma^{h}\gamma^{d}{}_{g}\widehat R(Q)_{hc}\big)\,\eta^{c}{}_{d}\,T_{ef}\\
&=0
\end{aligned}\tag{G187}
```

**G188: 1:curvature:13, vector coefficient.**

```math
\begin{aligned}
&-\frac{i}{32}\big(\bar\chi\gamma^{g}\gamma^{ef}\gamma^{h}\gamma^{a}\gamma^{d}{}_{g}\widehat R(Q)_{hc}\big)\,\eta^{c}{}_{d}\,T_{ef}\\
&=\frac{i}{4}\big(\overline{\widehat R(Q)^{a}{}_{c}}\gamma^{d}\chi\big)\,T^{c}{}_{d}
\end{aligned}\tag{G188}
```

**G189: 1:curvature:13, bivector coefficient.**

```math
\begin{aligned}
&\frac{i}{64}\big(\bar\chi\gamma^{g}\gamma^{ef}\gamma^{h}\gamma^{[ab]}\gamma^{d}{}_{g}\widehat R(Q)_{hc}\big)\,\eta^{c}{}_{d}\,T_{ef}\\
&=-\frac{i}{16}\big(\overline{\widehat R(Q)^{[ab]}}\gamma^{cd}\chi\big)\,T_{cd}\\
&+\frac{i}{2}\big(\overline{\widehat R(Q)^{[a}{}_{|c|}}\gamma^{b]d}\chi\big)\,T^{c}{}_{d}\\
&-\frac{3i}{16}\big(\overline{\widehat R(Q)_{cd}}\gamma^{[ab]}\chi\big)\,T^{cd}\\
&-\frac{i}{4}\big(\overline{\widehat R(Q)^{[a}{}_{|c|}}\chi\big)\,T^{|c|b]}
\end{aligned}\tag{G189}
```

**G190: 1:curvature:13, scalar coefficient.**

```math
\begin{aligned}
&\frac{i}{32}\big(\bar\chi\gamma^{g}\gamma^{ef}\gamma^{h}\gamma_{g}{}^{d}\widehat R(Q)_{hc}\big)\,\eta^{c}{}_{d}\,T_{ef}\\
&=0
\end{aligned}\tag{G190}
```

**G191: 1:curvature:13, vector coefficient.**

```math
\begin{aligned}
&\frac{i}{32}\big(\bar\chi\gamma^{g}\gamma^{ef}\gamma^{h}\gamma^{a}\gamma_{g}{}^{d}\widehat R(Q)_{hc}\big)\,\eta^{c}{}_{d}\,T_{ef}\\
&=\frac{i}{4}\big(\overline{\widehat R(Q)^{a}{}_{c}}\gamma^{d}\chi\big)\,T^{c}{}_{d}
\end{aligned}\tag{G191}
```

**G192: 1:curvature:13, bivector coefficient.**

```math
\begin{aligned}
&-\frac{i}{64}\big(\bar\chi\gamma^{g}\gamma^{ef}\gamma^{h}\gamma^{[ab]}\gamma_{g}{}^{d}\widehat R(Q)_{hc}\big)\,\eta^{c}{}_{d}\,T_{ef}\\
&=-\frac{i}{16}\big(\overline{\widehat R(Q)^{[ab]}}\gamma^{cd}\chi\big)\,T_{cd}\\
&+\frac{i}{2}\big(\overline{\widehat R(Q)^{[a}{}_{|c|}}\gamma^{b]d}\chi\big)\,T^{c}{}_{d}\\
&-\frac{3i}{16}\big(\overline{\widehat R(Q)_{cd}}\gamma^{[ab]}\chi\big)\,T^{cd}\\
&-\frac{i}{4}\big(\overline{\widehat R(Q)^{[a}{}_{|c|}}\chi\big)\,T^{|c|b]}
\end{aligned}\tag{G192}
```

**G193: 1:curvature:13, scalar coefficient.**

```math
\begin{aligned}
&\frac{i}{32}\big(\bar\chi\gamma^{g}\gamma^{ef}\gamma^{h}\gamma^{d}{}_{g}\widehat R(Q)_{ch}\big)\,\eta^{c}{}_{d}\,T_{ef}\\
&=0
\end{aligned}\tag{G193}
```

**G194: 1:curvature:13, vector coefficient.**

```math
\begin{aligned}
&\frac{i}{32}\big(\bar\chi\gamma^{g}\gamma^{ef}\gamma^{h}\gamma^{a}\gamma^{d}{}_{g}\widehat R(Q)_{ch}\big)\,\eta^{c}{}_{d}\,T_{ef}\\
&=\frac{i}{4}\big(\overline{\widehat R(Q)^{a}{}_{c}}\gamma^{d}\chi\big)\,T^{c}{}_{d}
\end{aligned}\tag{G194}
```

**G195: 1:curvature:13, bivector coefficient.**

```math
\begin{aligned}
&-\frac{i}{64}\big(\bar\chi\gamma^{g}\gamma^{ef}\gamma^{h}\gamma^{[ab]}\gamma^{d}{}_{g}\widehat R(Q)_{ch}\big)\,\eta^{c}{}_{d}\,T_{ef}\\
&=-\frac{i}{16}\big(\overline{\widehat R(Q)^{[ab]}}\gamma^{cd}\chi\big)\,T_{cd}\\
&+\frac{i}{2}\big(\overline{\widehat R(Q)^{[a}{}_{|c|}}\gamma^{b]d}\chi\big)\,T^{c}{}_{d}\\
&-\frac{3i}{16}\big(\overline{\widehat R(Q)_{cd}}\gamma^{[ab]}\chi\big)\,T^{cd}\\
&-\frac{i}{4}\big(\overline{\widehat R(Q)^{[a}{}_{|c|}}\chi\big)\,T^{|c|b]}
\end{aligned}\tag{G195}
```

**G196: 1:curvature:13, scalar coefficient.**

```math
\begin{aligned}
&-\frac{i}{32}\big(\bar\chi\gamma^{g}\gamma^{ef}\gamma^{h}\gamma_{g}{}^{d}\widehat R(Q)_{ch}\big)\,\eta^{c}{}_{d}\,T_{ef}\\
&=0
\end{aligned}\tag{G196}
```

**G197: 1:curvature:13, vector coefficient.**

```math
\begin{aligned}
&-\frac{i}{32}\big(\bar\chi\gamma^{g}\gamma^{ef}\gamma^{h}\gamma^{a}\gamma_{g}{}^{d}\widehat R(Q)_{ch}\big)\,\eta^{c}{}_{d}\,T_{ef}\\
&=\frac{i}{4}\big(\overline{\widehat R(Q)^{a}{}_{c}}\gamma^{d}\chi\big)\,T^{c}{}_{d}
\end{aligned}\tag{G197}
```

**G198: 1:curvature:13, bivector coefficient.**

```math
\begin{aligned}
&\frac{i}{64}\big(\bar\chi\gamma^{g}\gamma^{ef}\gamma^{h}\gamma^{[ab]}\gamma_{g}{}^{d}\widehat R(Q)_{ch}\big)\,\eta^{c}{}_{d}\,T_{ef}\\
&=-\frac{i}{16}\big(\overline{\widehat R(Q)^{[ab]}}\gamma^{cd}\chi\big)\,T_{cd}\\
&+\frac{i}{2}\big(\overline{\widehat R(Q)^{[a}{}_{|c|}}\gamma^{b]d}\chi\big)\,T^{c}{}_{d}\\
&-\frac{3i}{16}\big(\overline{\widehat R(Q)_{cd}}\gamma^{[ab]}\chi\big)\,T^{cd}\\
&-\frac{i}{4}\big(\overline{\widehat R(Q)^{[a}{}_{|c|}}\chi\big)\,T^{|c|b]}
\end{aligned}\tag{G198}
```

**G199: 1:Ricci contraction:1, scalar coefficient.**

```math
\begin{aligned}
&\frac{1}{96}\big(\overline{\mathcal D_{e}\widehat R(Q)_{gc}}\gamma^{e}\gamma^{fd}\widehat R(Q)^{g}{}_{f}\big)\,\eta^{c}{}_{d}\\
&=-\frac{1}{96}\big(\overline{\widehat R(Q)_{de}}\gamma^{c}\mathcal D_{c}\widehat R(Q)^{de}\big)
\end{aligned}\tag{G199}
```

**G200: 1:Ricci contraction:1, vector coefficient.**

```math
\begin{aligned}
&\frac{1}{96}\big(\overline{\mathcal D_{e}\widehat R(Q)_{gc}}\gamma^{e}\gamma^{fd}\gamma^{a}\widehat R(Q)^{g}{}_{f}\big)\,\eta^{c}{}_{d}\\
&=\frac{1}{96}\big(\overline{\widehat R(Q)_{de}}\gamma^{ca}\mathcal D_{c}\widehat R(Q)^{de}\big)\\
&+\frac{1}{24}\big(\overline{\widehat R(Q)_{c}{}^{a}}\mathcal D_{d}\widehat R(Q)^{cd}\big)\\
&-\frac{1}{96}\big(\overline{\widehat R(Q)_{cd}}\mathcal D^{a}\widehat R(Q)^{cd}\big)
\end{aligned}\tag{G200}
```

**G201: 1:Ricci contraction:1, bivector coefficient.**

```math
\begin{aligned}
&-\frac{1}{192}\big(\overline{\mathcal D_{e}\widehat R(Q)_{gc}}\gamma^{e}\gamma^{fd}\gamma^{[ab]}\widehat R(Q)^{g}{}_{f}\big)\,\eta^{c}{}_{d}\\
&=-\frac{1}{192}\big(\overline{\widehat R(Q)_{de}}\gamma^{c[ab]}\mathcal D_{c}\widehat R(Q)^{de}\big)\\
&-\frac{1}{24}\big(\overline{\widehat R(Q)_{c}{}^{[a}}\gamma^{b]}\mathcal D_{d}\widehat R(Q)^{cd}\big)\\
&-\frac{1}{96}\big(\overline{\widehat R(Q)_{cd}}\gamma^{[a}\mathcal D^{b]}\widehat R(Q)^{cd}\big)\\
&=\frac{i}{384}\big(\overline{\widehat R(Q)_{fg}}\gamma^{cd}\mathcal D_{e}\widehat R(Q)^{fg}\big)\,\varepsilon_{cd}{}^{e[ab]}\\
&-\frac{1}{24}\big(\overline{\widehat R(Q)_{c}{}^{[a}}\gamma^{b]}\mathcal D_{d}\widehat R(Q)^{cd}\big)\\
&-\frac{1}{96}\big(\overline{\widehat R(Q)_{cd}}\gamma^{[a}\mathcal D^{b]}\widehat R(Q)^{cd}\big)
\end{aligned}\tag{G201}
```

**G202: 1:Ricci contraction:2, scalar coefficient.**

```math
\begin{aligned}
&\frac{1}{192}\big(\overline{\mathcal D_{g}\widehat R(Q)_{c}{}^{g}}\gamma^{e}\gamma^{fd}\widehat R(Q)_{ef}\big)\,\eta^{c}{}_{d}\\
&=0
\end{aligned}\tag{G202}
```

**G203: 1:Ricci contraction:2, vector coefficient.**

```math
\begin{aligned}
&\frac{1}{192}\big(\overline{\mathcal D_{g}\widehat R(Q)_{c}{}^{g}}\gamma^{e}\gamma^{fd}\gamma^{a}\widehat R(Q)_{ef}\big)\,\eta^{c}{}_{d}\\
&=\frac{1}{32}\big(\overline{\widehat R(Q)_{c}{}^{a}}\mathcal D_{d}\widehat R(Q)^{cd}\big)
\end{aligned}\tag{G203}
```

**G204: 1:Ricci contraction:2, bivector coefficient.**

```math
\begin{aligned}
&-\frac{1}{384}\big(\overline{\mathcal D_{g}\widehat R(Q)_{c}{}^{g}}\gamma^{e}\gamma^{fd}\gamma^{[ab]}\widehat R(Q)_{ef}\big)\,\eta^{c}{}_{d}\\
&=-\frac{1}{32}\big(\overline{\widehat R(Q)_{c}{}^{[a}}\gamma^{b]}\mathcal D_{d}\widehat R(Q)^{cd}\big)
\end{aligned}\tag{G204}
```

**G205: 1:Ricci contraction:2, scalar coefficient.**

```math
\begin{aligned}
&-\frac{1}{192}\big(\overline{\mathcal D_{f}\widehat R(Q)_{g}{}^{f}}\gamma^{c}\gamma^{ed}\widehat R(Q)^{g}{}_{e}\big)\,\eta_{cd}\\
&=0
\end{aligned}\tag{G205}
```

**G206: 1:Ricci contraction:2, vector coefficient.**

```math
\begin{aligned}
&-\frac{1}{192}\big(\overline{\mathcal D_{f}\widehat R(Q)_{g}{}^{f}}\gamma^{c}\gamma^{ed}\gamma^{a}\widehat R(Q)^{g}{}_{e}\big)\,\eta_{cd}\\
&=-\frac{1}{24}\big(\overline{\widehat R(Q)_{c}{}^{a}}\mathcal D_{d}\widehat R(Q)^{cd}\big)
\end{aligned}\tag{G206}
```

**G207: 1:Ricci contraction:2, bivector coefficient.**

```math
\begin{aligned}
&\frac{1}{384}\big(\overline{\mathcal D_{f}\widehat R(Q)_{g}{}^{f}}\gamma^{c}\gamma^{ed}\gamma^{[ab]}\widehat R(Q)^{g}{}_{e}\big)\,\eta_{cd}\\
&=\frac{1}{24}\big(\overline{\widehat R(Q)_{c}{}^{[a}}\gamma^{b]}\mathcal D_{d}\widehat R(Q)^{cd}\big)
\end{aligned}\tag{G207}
```

**G208: 1:Ricci contraction:3, scalar coefficient.**

```math
\begin{aligned}
&\frac{i}{36}\big(\overline{\widehat R(Q)_{cd}}\gamma^{ge}\gamma^{hf}\widehat R(Q)_{gh}\big)\,T^{cd}\,\eta_{ef}\\
&=0
\end{aligned}\tag{G208}
```

**G209: 1:Ricci contraction:3, vector coefficient.**

```math
\begin{aligned}
&\frac{i}{36}\big(\overline{\widehat R(Q)_{cd}}\gamma^{ge}\gamma^{hf}\gamma^{a}\widehat R(Q)_{gh}\big)\,T^{cd}\,\eta_{ef}\\
&=0
\end{aligned}\tag{G209}
```

**G210: 1:Ricci contraction:3, bivector coefficient.**

```math
\begin{aligned}
&-\frac{i}{72}\big(\overline{\widehat R(Q)_{cd}}\gamma^{ge}\gamma^{hf}\gamma^{[ab]}\widehat R(Q)_{gh}\big)\,T^{cd}\,\eta_{ef}\\
&=\frac{i}{3}\big(\overline{\widehat R(Q)^{[ab]}}\widehat R(Q)_{cd}\big)\,T^{cd}
\end{aligned}\tag{G210}
```

**G211: 1:Ricci contraction:4, scalar coefficient.**

```math
\begin{aligned}
&\frac{i}{16}\big(\overline{\widehat R(Q)_{ec}}\gamma^{g}\gamma^{d}\gamma^{hf}\widehat R(Q)_{gh}\big)\,T^{c}{}_{d}\,\eta^{e}{}_{f}\\
&=-\frac{i}{8}\big(\overline{\widehat R(Q)_{ec}}\widehat R(Q)^{e}{}_{d}\big)\,T^{cd}
\end{aligned}\tag{G211}
```

**G212: 1:Ricci contraction:4, vector coefficient.**

```math
\begin{aligned}
&\frac{i}{16}\big(\overline{\widehat R(Q)_{ec}}\gamma^{g}\gamma^{d}\gamma^{hf}\gamma^{a}\widehat R(Q)_{gh}\big)\,T^{c}{}_{d}\,\eta^{e}{}_{f}\\
&=-\frac{i}{8}\big(\overline{\widehat R(Q)_{ec}}\gamma^{a}\widehat R(Q)^{e}{}_{d}\big)\,T^{cd}\\
&+\frac{3i}{8}\big(\overline{\widehat R(Q)_{e}{}^{a}}\gamma^{c}\widehat R(Q)^{e}{}_{d}\big)\,T_{c}{}^{d}
\end{aligned}\tag{G212}
```

**G213: 1:Ricci contraction:4, bivector coefficient.**

```math
\begin{aligned}
&-\frac{i}{32}\big(\overline{\widehat R(Q)_{ec}}\gamma^{g}\gamma^{d}\gamma^{hf}\gamma^{[ab]}\widehat R(Q)_{gh}\big)\,T^{c}{}_{d}\,\eta^{e}{}_{f}\\
&=-\frac{i}{4}\big(\overline{\widehat R(Q)_{e}{}^{[a}}\gamma^{b]c}\widehat R(Q)^{e}{}_{d}\big)\,T_{c}{}^{d}\\
&-\frac{7i}{16}\big(\overline{\widehat R(Q)^{[ab]}}\widehat R(Q)_{cd}\big)\,T^{cd}\\
&+\frac{3i}{8}\big(\overline{\widehat R(Q)_{d}{}^{[a}}\widehat R(Q)^{|d|}{}_{|c|}\big)\,T^{|c|b]}
\end{aligned}\tag{G213}
```

**G214: 1:Ricci contraction:4, scalar coefficient.**

```math
\begin{aligned}
&-\frac{i}{16}\big(\overline{\widehat R(Q)_{hc}}\gamma^{e}\gamma^{d}\gamma^{gf}\widehat R(Q)^{h}{}_{g}\big)\,T^{c}{}_{d}\,\eta_{ef}\\
&=-\frac{i}{8}\big(\overline{\widehat R(Q)_{ec}}\widehat R(Q)^{e}{}_{d}\big)\,T^{cd}
\end{aligned}\tag{G214}
```

**G215: 1:Ricci contraction:4, vector coefficient.**

```math
\begin{aligned}
&-\frac{i}{16}\big(\overline{\widehat R(Q)_{hc}}\gamma^{e}\gamma^{d}\gamma^{gf}\gamma^{a}\widehat R(Q)^{h}{}_{g}\big)\,T^{c}{}_{d}\,\eta_{ef}\\
&=-\frac{i}{4}\big(\overline{\widehat R(Q)_{e}{}^{a}}\gamma^{c}\widehat R(Q)^{e}{}_{d}\big)\,T_{c}{}^{d}\\
&-\frac{i}{8}\big(\overline{\widehat R(Q)_{ec}}\gamma^{a}\widehat R(Q)^{e}{}_{d}\big)\,T^{cd}
\end{aligned}\tag{G215}
```

**G216: 1:Ricci contraction:4, bivector coefficient.**

```math
\begin{aligned}
&\frac{i}{32}\big(\overline{\widehat R(Q)_{hc}}\gamma^{e}\gamma^{d}\gamma^{gf}\gamma^{[ab]}\widehat R(Q)^{h}{}_{g}\big)\,T^{c}{}_{d}\,\eta_{ef}\\
&=\frac{i}{4}\big(\overline{\widehat R(Q)_{e}{}^{[a}}\gamma^{b]c}\widehat R(Q)^{e}{}_{d}\big)\,T_{c}{}^{d}\\
&-\frac{i}{4}\big(\overline{\widehat R(Q)_{d}{}^{[a}}\widehat R(Q)^{|d|}{}_{|c|}\big)\,T^{|c|b]}
\end{aligned}\tag{G216}
```

**G217: 1:Ricci contraction:5, scalar coefficient.**

```math
\begin{aligned}
&\frac{i}{32}\big(\overline{\widehat R(Q)_{hc}}\gamma^{ef}\gamma^{gd}\widehat R(Q)^{h}{}_{g}\big)\,\eta^{c}{}_{d}\,T_{ef}\\
&=\frac{i}{32}\big(\overline{\widehat R(Q)_{ef}}\gamma^{cd}\widehat R(Q)^{ef}\big)\,T_{cd}
\end{aligned}\tag{G217}
```

**G218: 1:Ricci contraction:5, vector coefficient.**

```math
\begin{aligned}
&\frac{i}{32}\big(\overline{\widehat R(Q)_{hc}}\gamma^{ef}\gamma^{gd}\gamma^{a}\widehat R(Q)^{h}{}_{g}\big)\,\eta^{c}{}_{d}\,T_{ef}\\
&=\frac{i}{32}\big(\overline{\widehat R(Q)_{ef}}\gamma^{acd}\widehat R(Q)^{ef}\big)\,T_{cd}\\
&+\frac{i}{4}\big(\overline{\widehat R(Q)_{e}{}^{a}}\gamma^{c}\widehat R(Q)^{e}{}_{d}\big)\,T_{c}{}^{d}\\
&=\frac{1}{64}\big(\overline{\widehat R(Q)_{gh}}\gamma^{cd}\widehat R(Q)^{gh}\big)\,\varepsilon_{cd}{}^{a}{}_{ef}\,T^{ef}\\
&+\frac{i}{4}\big(\overline{\widehat R(Q)_{e}{}^{a}}\gamma^{c}\widehat R(Q)^{e}{}_{d}\big)\,T_{c}{}^{d}
\end{aligned}\tag{G218}
```

**G219: 1:Ricci contraction:5, bivector coefficient.**

```math
\begin{aligned}
&-\frac{i}{64}\big(\overline{\widehat R(Q)_{hc}}\gamma^{ef}\gamma^{gd}\gamma^{[ab]}\widehat R(Q)^{h}{}_{g}\big)\,\eta^{c}{}_{d}\,T_{ef}\\
&=-\frac{i}{4}\big(\overline{\widehat R(Q)_{e}{}^{[a}}\gamma^{b]c}\widehat R(Q)^{e}{}_{d}\big)\,T_{c}{}^{d}\\
&-\frac{i}{16}\big(\overline{\widehat R(Q)_{de}}\gamma^{[a|c|}\widehat R(Q)^{|de|}\big)\,T_{|c|}{}^{b]}\\
&+\frac{i}{4}\big(\overline{\widehat R(Q)_{d}{}^{[a}}\widehat R(Q)^{|d|}{}_{|c|}\big)\,T^{|c|b]}
\end{aligned}\tag{G219}
```

**G220: 1:Ricci contraction:6, scalar coefficient.**

```math
\begin{aligned}
&-\frac{i}{24}\big(\overline{\widehat R(Q)_{ec}}\gamma^{gf}\widehat R(Q)_{dg}\big)\,T^{cd}\,\eta^{e}{}_{f}\\
&=\frac{i}{24}\big(\overline{\widehat R(Q)_{ec}}\widehat R(Q)^{e}{}_{d}\big)\,T^{cd}
\end{aligned}\tag{G220}
```

**G221: 1:Ricci contraction:6, vector coefficient.**

```math
\begin{aligned}
&-\frac{i}{24}\big(\overline{\widehat R(Q)_{ec}}\gamma^{gf}\gamma^{a}\widehat R(Q)_{dg}\big)\,T^{cd}\,\eta^{e}{}_{f}\\
&=\frac{i}{24}\big(\overline{\widehat R(Q)_{ec}}\gamma^{a}\widehat R(Q)^{e}{}_{d}\big)\,T^{cd}
\end{aligned}\tag{G221}
```

**G222: 1:Ricci contraction:6, bivector coefficient.**

```math
\begin{aligned}
&\frac{i}{48}\big(\overline{\widehat R(Q)_{ec}}\gamma^{gf}\gamma^{[ab]}\widehat R(Q)_{dg}\big)\,T^{cd}\,\eta^{e}{}_{f}\\
&=0
\end{aligned}\tag{G222}
```

**G223: 1:Ricci contraction:6, scalar coefficient.**

```math
\begin{aligned}
&\frac{i}{24}\big(\overline{\widehat R(Q)_{gc}}\gamma^{fe}\widehat R(Q)^{g}{}_{f}\big)\,T^{c}{}_{d}\,\eta^{d}{}_{e}\\
&=\frac{i}{24}\big(\overline{\widehat R(Q)_{ec}}\widehat R(Q)^{e}{}_{d}\big)\,T^{cd}
\end{aligned}\tag{G223}
```

**G224: 1:Ricci contraction:6, vector coefficient.**

```math
\begin{aligned}
&\frac{i}{24}\big(\overline{\widehat R(Q)_{gc}}\gamma^{fe}\gamma^{a}\widehat R(Q)^{g}{}_{f}\big)\,T^{c}{}_{d}\,\eta^{d}{}_{e}\\
&=\frac{i}{24}\big(\overline{\widehat R(Q)_{ec}}\gamma^{a}\widehat R(Q)^{e}{}_{d}\big)\,T^{cd}\\
&-\frac{i}{12}\big(\overline{\widehat R(Q)_{e}{}^{a}}\gamma^{c}\widehat R(Q)^{e}{}_{d}\big)\,T_{c}{}^{d}
\end{aligned}\tag{G224}
```

**G225: 1:Ricci contraction:6, bivector coefficient.**

```math
\begin{aligned}
&-\frac{i}{48}\big(\overline{\widehat R(Q)_{gc}}\gamma^{fe}\gamma^{[ab]}\widehat R(Q)^{g}{}_{f}\big)\,T^{c}{}_{d}\,\eta^{d}{}_{e}\\
&=\frac{i}{12}\big(\overline{\widehat R(Q)_{e}{}^{[a}}\gamma^{b]c}\widehat R(Q)^{e}{}_{d}\big)\,T_{c}{}^{d}\\
&-\frac{i}{12}\big(\overline{\widehat R(Q)_{d}{}^{[a}}\widehat R(Q)^{|d|}{}_{|c|}\big)\,T^{|c|b]}
\end{aligned}\tag{G225}
```

**G226: 1:Ricci contraction:7, scalar coefficient.**

```math
\begin{aligned}
&\frac{i}{96}\big(\overline{\widehat R(Q)_{hc}}\gamma^{g}\gamma^{ef}\gamma^{d}\widehat R(Q)^{h}{}_{g}\big)\,\eta^{c}{}_{d}\,T_{ef}\\
&=\frac{i}{48}\big(\overline{\widehat R(Q)_{ef}}\gamma^{cd}\widehat R(Q)^{ef}\big)\,T_{cd}\\
&-\frac{i}{12}\big(\overline{\widehat R(Q)_{ec}}\widehat R(Q)^{e}{}_{d}\big)\,T^{cd}
\end{aligned}\tag{G226}
```

**G227: 1:Ricci contraction:7, vector coefficient.**

```math
\begin{aligned}
&\frac{i}{96}\big(\overline{\widehat R(Q)_{hc}}\gamma^{g}\gamma^{ef}\gamma^{d}\gamma^{a}\widehat R(Q)^{h}{}_{g}\big)\,\eta^{c}{}_{d}\,T_{ef}\\
&=\frac{i}{48}\big(\overline{\widehat R(Q)_{ef}}\gamma^{acd}\widehat R(Q)^{ef}\big)\,T_{cd}\\
&+\frac{i}{12}\big(\overline{\widehat R(Q)_{e}{}^{a}}\gamma^{c}\widehat R(Q)^{e}{}_{d}\big)\,T_{c}{}^{d}\\
&-\frac{i}{12}\big(\overline{\widehat R(Q)_{ec}}\gamma^{a}\widehat R(Q)^{e}{}_{d}\big)\,T^{cd}\\
&=\frac{1}{96}\big(\overline{\widehat R(Q)_{gh}}\gamma^{cd}\widehat R(Q)^{gh}\big)\,\varepsilon_{cd}{}^{a}{}_{ef}\,T^{ef}\\
&+\frac{i}{12}\big(\overline{\widehat R(Q)_{e}{}^{a}}\gamma^{c}\widehat R(Q)^{e}{}_{d}\big)\,T_{c}{}^{d}\\
&-\frac{i}{12}\big(\overline{\widehat R(Q)_{ec}}\gamma^{a}\widehat R(Q)^{e}{}_{d}\big)\,T^{cd}
\end{aligned}\tag{G227}
```

**G228: 1:Ricci contraction:7, bivector coefficient.**

```math
\begin{aligned}
&-\frac{i}{192}\big(\overline{\widehat R(Q)_{hc}}\gamma^{g}\gamma^{ef}\gamma^{d}\gamma^{[ab]}\widehat R(Q)^{h}{}_{g}\big)\,\eta^{c}{}_{d}\,T_{ef}\\
&=-\frac{i}{12}\big(\overline{\widehat R(Q)_{e}{}^{[a}}\gamma^{b]c}\widehat R(Q)^{e}{}_{d}\big)\,T_{c}{}^{d}\\
&-\frac{i}{24}\big(\overline{\widehat R(Q)_{de}}\gamma^{[a|c|}\widehat R(Q)^{|de|}\big)\,T_{|c|}{}^{b]}\\
&+\frac{i}{12}\big(\overline{\widehat R(Q)_{d}{}^{[a}}\widehat R(Q)^{|d|}{}_{|c|}\big)\,T^{|c|b]}
\end{aligned}\tag{G228}
```

**G229: 1:Ricci contraction:7, scalar coefficient.**

```math
\begin{aligned}
&-\frac{i}{96}\big(\overline{\widehat R(Q)_{hc}}\gamma^{d}\gamma^{ef}\gamma^{g}\widehat R(Q)^{h}{}_{g}\big)\,\eta^{c}{}_{d}\,T_{ef}\\
&=0
\end{aligned}\tag{G229}
```

**G230: 1:Ricci contraction:7, vector coefficient.**

```math
\begin{aligned}
&-\frac{i}{96}\big(\overline{\widehat R(Q)_{hc}}\gamma^{d}\gamma^{ef}\gamma^{g}\gamma^{a}\widehat R(Q)^{h}{}_{g}\big)\,\eta^{c}{}_{d}\,T_{ef}\\
&=0
\end{aligned}\tag{G230}
```

**G231: 1:Ricci contraction:7, bivector coefficient.**

```math
\begin{aligned}
&\frac{i}{192}\big(\overline{\widehat R(Q)_{hc}}\gamma^{d}\gamma^{ef}\gamma^{g}\gamma^{[ab]}\widehat R(Q)^{h}{}_{g}\big)\,\eta^{c}{}_{d}\,T_{ef}\\
&=0
\end{aligned}\tag{G231}
```

**G232: 1:Ricci contraction:8, scalar coefficient.**

```math
\begin{aligned}
&\frac{1}{192}\big(\overline{\mathcal D_{f}\widehat R(Q)_{cd}}\gamma^{e}\widehat R(Q)^{f}{}_{e}\big)\,\eta^{cd}\\
&=0
\end{aligned}\tag{G232}
```

**G233: 1:Ricci contraction:8, vector coefficient.**

```math
\begin{aligned}
&\frac{1}{192}\big(\overline{\mathcal D_{f}\widehat R(Q)_{cd}}\gamma^{e}\gamma^{a}\widehat R(Q)^{f}{}_{e}\big)\,\eta^{cd}\\
&=0
\end{aligned}\tag{G233}
```

**G234: 1:Ricci contraction:8, bivector coefficient.**

```math
\begin{aligned}
&-\frac{1}{384}\big(\overline{\mathcal D_{f}\widehat R(Q)_{cd}}\gamma^{e}\gamma^{[ab]}\widehat R(Q)^{f}{}_{e}\big)\,\eta^{cd}\\
&=0
\end{aligned}\tag{G234}
```

**G235: 1:Ricci contraction:8, scalar coefficient.**

```math
\begin{aligned}
&-\frac{1}{192}\big(\overline{\mathcal D_{e}\widehat R(Q)_{cf}}\gamma^{d}\widehat R(Q)^{ef}\big)\,\eta^{c}{}_{d}\\
&=0
\end{aligned}\tag{G235}
```

**G236: 1:Ricci contraction:8, vector coefficient.**

```math
\begin{aligned}
&-\frac{1}{192}\big(\overline{\mathcal D_{e}\widehat R(Q)_{cf}}\gamma^{d}\gamma^{a}\widehat R(Q)^{ef}\big)\,\eta^{c}{}_{d}\\
&=0
\end{aligned}\tag{G236}
```

**G237: 1:Ricci contraction:8, bivector coefficient.**

```math
\begin{aligned}
&\frac{1}{384}\big(\overline{\mathcal D_{e}\widehat R(Q)_{cf}}\gamma^{d}\gamma^{[ab]}\widehat R(Q)^{ef}\big)\,\eta^{c}{}_{d}\\
&=0
\end{aligned}\tag{G237}
```

**G238: 1:Ricci contraction:8, scalar coefficient.**

```math
\begin{aligned}
&-\frac{1}{192}\big(\overline{\mathcal D_{c}\widehat R(Q)_{fd}}\gamma^{e}\widehat R(Q)^{f}{}_{e}\big)\,\eta^{cd}\\
&=0
\end{aligned}\tag{G238}
```

**G239: 1:Ricci contraction:8, vector coefficient.**

```math
\begin{aligned}
&-\frac{1}{192}\big(\overline{\mathcal D_{c}\widehat R(Q)_{fd}}\gamma^{e}\gamma^{a}\widehat R(Q)^{f}{}_{e}\big)\,\eta^{cd}\\
&=\frac{1}{96}\big(\overline{\widehat R(Q)_{c}{}^{a}}\mathcal D_{d}\widehat R(Q)^{cd}\big)
\end{aligned}\tag{G239}
```

**G240: 1:Ricci contraction:8, bivector coefficient.**

```math
\begin{aligned}
&\frac{1}{384}\big(\overline{\mathcal D_{c}\widehat R(Q)_{fd}}\gamma^{e}\gamma^{[ab]}\widehat R(Q)^{f}{}_{e}\big)\,\eta^{cd}\\
&=-\frac{1}{96}\big(\overline{\widehat R(Q)_{c}{}^{[a}}\gamma^{b]}\mathcal D_{d}\widehat R(Q)^{cd}\big)
\end{aligned}\tag{G240}
```

**G241: 1:Ricci contraction:8, scalar coefficient.**

```math
\begin{aligned}
&\frac{1}{192}\big(\overline{\mathcal D_{c}\widehat R(Q)_{ef}}\gamma^{d}\widehat R(Q)^{ef}\big)\,\eta^{c}{}_{d}\\
&=-\frac{1}{192}\big(\overline{\widehat R(Q)_{de}}\gamma^{c}\mathcal D_{c}\widehat R(Q)^{de}\big)
\end{aligned}\tag{G241}
```

**G242: 1:Ricci contraction:8, vector coefficient.**

```math
\begin{aligned}
&\frac{1}{192}\big(\overline{\mathcal D_{c}\widehat R(Q)_{ef}}\gamma^{d}\gamma^{a}\widehat R(Q)^{ef}\big)\,\eta^{c}{}_{d}\\
&=\frac{1}{192}\big(\overline{\widehat R(Q)_{de}}\gamma^{ca}\mathcal D_{c}\widehat R(Q)^{de}\big)\\
&-\frac{1}{192}\big(\overline{\widehat R(Q)_{cd}}\mathcal D^{a}\widehat R(Q)^{cd}\big)
\end{aligned}\tag{G242}
```

**G243: 1:Ricci contraction:8, bivector coefficient.**

```math
\begin{aligned}
&-\frac{1}{384}\big(\overline{\mathcal D_{c}\widehat R(Q)_{ef}}\gamma^{d}\gamma^{[ab]}\widehat R(Q)^{ef}\big)\,\eta^{c}{}_{d}\\
&=-\frac{1}{384}\big(\overline{\widehat R(Q)_{de}}\gamma^{c[ab]}\mathcal D_{c}\widehat R(Q)^{de}\big)\\
&-\frac{1}{192}\big(\overline{\widehat R(Q)_{cd}}\gamma^{[a}\mathcal D^{b]}\widehat R(Q)^{cd}\big)\\
&=\frac{i}{768}\big(\overline{\widehat R(Q)_{fg}}\gamma^{cd}\mathcal D_{e}\widehat R(Q)^{fg}\big)\,\varepsilon_{cd}{}^{e[ab]}\\
&-\frac{1}{192}\big(\overline{\widehat R(Q)_{cd}}\gamma^{[a}\mathcal D^{b]}\widehat R(Q)^{cd}\big)
\end{aligned}\tag{G243}
```

**G244: 1:Ricci contraction:9, scalar coefficient.**

```math
\begin{aligned}
&-\frac{i}{192}\big(\overline{\widehat R(Q)_{cd}}\gamma^{g}\gamma^{ef}\gamma^{h}\widehat R(Q)_{hg}\big)\,\eta^{cd}\,T_{ef}\\
&=0
\end{aligned}\tag{G244}
```

**G245: 1:Ricci contraction:9, vector coefficient.**

```math
\begin{aligned}
&-\frac{i}{192}\big(\overline{\widehat R(Q)_{cd}}\gamma^{g}\gamma^{ef}\gamma^{h}\gamma^{a}\widehat R(Q)_{hg}\big)\,\eta^{cd}\,T_{ef}\\
&=0
\end{aligned}\tag{G245}
```

**G246: 1:Ricci contraction:9, bivector coefficient.**

```math
\begin{aligned}
&\frac{i}{384}\big(\overline{\widehat R(Q)_{cd}}\gamma^{g}\gamma^{ef}\gamma^{h}\gamma^{[ab]}\widehat R(Q)_{hg}\big)\,\eta^{cd}\,T_{ef}\\
&=0
\end{aligned}\tag{G246}
```

**G247: 1:Ricci contraction:9, scalar coefficient.**

```math
\begin{aligned}
&\frac{i}{192}\big(\overline{\widehat R(Q)_{ch}}\gamma^{d}\gamma^{ef}\gamma^{g}\widehat R(Q)_{g}{}^{h}\big)\,\eta^{c}{}_{d}\,T_{ef}\\
&=0
\end{aligned}\tag{G247}
```

**G248: 1:Ricci contraction:9, vector coefficient.**

```math
\begin{aligned}
&\frac{i}{192}\big(\overline{\widehat R(Q)_{ch}}\gamma^{d}\gamma^{ef}\gamma^{g}\gamma^{a}\widehat R(Q)_{g}{}^{h}\big)\,\eta^{c}{}_{d}\,T_{ef}\\
&=0
\end{aligned}\tag{G248}
```

**G249: 1:Ricci contraction:9, bivector coefficient.**

```math
\begin{aligned}
&-\frac{i}{384}\big(\overline{\widehat R(Q)_{ch}}\gamma^{d}\gamma^{ef}\gamma^{g}\gamma^{[ab]}\widehat R(Q)_{g}{}^{h}\big)\,\eta^{c}{}_{d}\,T_{ef}\\
&=0
\end{aligned}\tag{G249}
```

**G250: 1:Ricci contraction:9, scalar coefficient.**

```math
\begin{aligned}
&\frac{i}{192}\big(\overline{\widehat R(Q)_{hd}}\gamma^{g}\gamma^{ef}\gamma^{c}\widehat R(Q)^{h}{}_{g}\big)\,\eta_{c}{}^{d}\,T_{ef}\\
&=\frac{i}{96}\big(\overline{\widehat R(Q)_{ef}}\gamma^{cd}\widehat R(Q)^{ef}\big)\,T_{cd}\\
&-\frac{i}{24}\big(\overline{\widehat R(Q)_{ec}}\widehat R(Q)^{e}{}_{d}\big)\,T^{cd}
\end{aligned}\tag{G250}
```

**G251: 1:Ricci contraction:9, vector coefficient.**

```math
\begin{aligned}
&\frac{i}{192}\big(\overline{\widehat R(Q)_{hd}}\gamma^{g}\gamma^{ef}\gamma^{c}\gamma^{a}\widehat R(Q)^{h}{}_{g}\big)\,\eta_{c}{}^{d}\,T_{ef}\\
&=\frac{i}{96}\big(\overline{\widehat R(Q)_{ef}}\gamma^{acd}\widehat R(Q)^{ef}\big)\,T_{cd}\\
&+\frac{i}{24}\big(\overline{\widehat R(Q)_{e}{}^{a}}\gamma^{c}\widehat R(Q)^{e}{}_{d}\big)\,T_{c}{}^{d}\\
&-\frac{i}{24}\big(\overline{\widehat R(Q)_{ec}}\gamma^{a}\widehat R(Q)^{e}{}_{d}\big)\,T^{cd}\\
&=\frac{1}{192}\big(\overline{\widehat R(Q)_{gh}}\gamma^{cd}\widehat R(Q)^{gh}\big)\,\varepsilon_{cd}{}^{a}{}_{ef}\,T^{ef}\\
&+\frac{i}{24}\big(\overline{\widehat R(Q)_{e}{}^{a}}\gamma^{c}\widehat R(Q)^{e}{}_{d}\big)\,T_{c}{}^{d}\\
&-\frac{i}{24}\big(\overline{\widehat R(Q)_{ec}}\gamma^{a}\widehat R(Q)^{e}{}_{d}\big)\,T^{cd}
\end{aligned}\tag{G251}
```

**G252: 1:Ricci contraction:9, bivector coefficient.**

```math
\begin{aligned}
&-\frac{i}{384}\big(\overline{\widehat R(Q)_{hd}}\gamma^{g}\gamma^{ef}\gamma^{c}\gamma^{[ab]}\widehat R(Q)^{h}{}_{g}\big)\,\eta_{c}{}^{d}\,T_{ef}\\
&=-\frac{i}{24}\big(\overline{\widehat R(Q)_{e}{}^{[a}}\gamma^{b]c}\widehat R(Q)^{e}{}_{d}\big)\,T_{c}{}^{d}\\
&-\frac{i}{48}\big(\overline{\widehat R(Q)_{de}}\gamma^{[a|c|}\widehat R(Q)^{|de|}\big)\,T_{|c|}{}^{b]}\\
&+\frac{i}{24}\big(\overline{\widehat R(Q)_{d}{}^{[a}}\widehat R(Q)^{|d|}{}_{|c|}\big)\,T^{|c|b]}
\end{aligned}\tag{G252}
```

**G253: 1:Ricci contraction:9, scalar coefficient.**

```math
\begin{aligned}
&-\frac{i}{192}\big(\overline{\widehat R(Q)_{gh}}\gamma^{d}\gamma^{ef}\gamma^{c}\widehat R(Q)^{gh}\big)\,\eta_{cd}\,T_{ef}\\
&=-\frac{i}{192}\big(\overline{\widehat R(Q)_{ef}}\gamma^{cd}\widehat R(Q)^{ef}\big)\,T_{cd}
\end{aligned}\tag{G253}
```

**G254: 1:Ricci contraction:9, vector coefficient.**

```math
\begin{aligned}
&-\frac{i}{192}\big(\overline{\widehat R(Q)_{gh}}\gamma^{d}\gamma^{ef}\gamma^{c}\gamma^{a}\widehat R(Q)^{gh}\big)\,\eta_{cd}\,T_{ef}\\
&=-\frac{i}{192}\big(\overline{\widehat R(Q)_{ef}}\gamma^{acd}\widehat R(Q)^{ef}\big)\,T_{cd}\\
&=-\frac{1}{384}\big(\overline{\widehat R(Q)_{gh}}\gamma^{cd}\widehat R(Q)^{gh}\big)\,\varepsilon_{cd}{}^{a}{}_{ef}\,T^{ef}
\end{aligned}\tag{G254}
```

**G255: 1:Ricci contraction:9, bivector coefficient.**

```math
\begin{aligned}
&\frac{i}{384}\big(\overline{\widehat R(Q)_{gh}}\gamma^{d}\gamma^{ef}\gamma^{c}\gamma^{[ab]}\widehat R(Q)^{gh}\big)\,\eta_{cd}\,T_{ef}\\
&=\frac{i}{96}\big(\overline{\widehat R(Q)_{de}}\gamma^{[a|c|}\widehat R(Q)^{|de|}\big)\,T_{|c|}{}^{b]}
\end{aligned}\tag{G255}
```

**G256: 1:Ricci contraction:10, scalar coefficient.**

```math
\begin{aligned}
&-\frac{1}{192}\big(\overline{\mathcal D_{c}\widehat R(Q)_{fd}}\gamma^{e}\widehat R(Q)_{e}{}^{f}\big)\,\eta^{cd}\\
&=0
\end{aligned}\tag{G256}
```

**G257: 1:Ricci contraction:10, vector coefficient.**

```math
\begin{aligned}
&-\frac{1}{192}\big(\overline{\mathcal D_{c}\widehat R(Q)_{fd}}\gamma^{e}\gamma^{a}\widehat R(Q)_{e}{}^{f}\big)\,\eta^{cd}\\
&=-\frac{1}{96}\big(\overline{\widehat R(Q)_{c}{}^{a}}\mathcal D_{d}\widehat R(Q)^{cd}\big)
\end{aligned}\tag{G257}
```

**G258: 1:Ricci contraction:10, bivector coefficient.**

```math
\begin{aligned}
&\frac{1}{384}\big(\overline{\mathcal D_{c}\widehat R(Q)_{fd}}\gamma^{e}\gamma^{[ab]}\widehat R(Q)_{e}{}^{f}\big)\,\eta^{cd}\\
&=\frac{1}{96}\big(\overline{\widehat R(Q)_{c}{}^{[a}}\gamma^{b]}\mathcal D_{d}\widehat R(Q)^{cd}\big)
\end{aligned}\tag{G258}
```

**G259: 1:Ricci contraction:10, scalar coefficient.**

```math
\begin{aligned}
&\frac{1}{192}\big(\overline{\mathcal D_{e}\widehat R(Q)_{fd}}\gamma^{c}\widehat R(Q)^{ef}\big)\,\eta_{c}{}^{d}\\
&=0
\end{aligned}\tag{G259}
```

**G260: 1:Ricci contraction:10, vector coefficient.**

```math
\begin{aligned}
&\frac{1}{192}\big(\overline{\mathcal D_{e}\widehat R(Q)_{fd}}\gamma^{c}\gamma^{a}\widehat R(Q)^{ef}\big)\,\eta_{c}{}^{d}\\
&=0
\end{aligned}\tag{G260}
```

**G261: 1:Ricci contraction:10, bivector coefficient.**

```math
\begin{aligned}
&-\frac{1}{384}\big(\overline{\mathcal D_{e}\widehat R(Q)_{fd}}\gamma^{c}\gamma^{[ab]}\widehat R(Q)^{ef}\big)\,\eta_{c}{}^{d}\\
&=0
\end{aligned}\tag{G261}
```

**G262: 1:Ricci contraction:11, scalar coefficient.**

```math
\begin{aligned}
&\frac{i}{192}\big(\overline{\widehat R(Q)_{hd}}\gamma^{g}\gamma^{ef}\gamma^{c}\widehat R(Q)_{g}{}^{h}\big)\,\eta_{c}{}^{d}\,T_{ef}\\
&=-\frac{i}{96}\big(\overline{\widehat R(Q)_{ef}}\gamma^{cd}\widehat R(Q)^{ef}\big)\,T_{cd}\\
&+\frac{i}{24}\big(\overline{\widehat R(Q)_{ec}}\widehat R(Q)^{e}{}_{d}\big)\,T^{cd}
\end{aligned}\tag{G262}
```

**G263: 1:Ricci contraction:11, vector coefficient.**

```math
\begin{aligned}
&\frac{i}{192}\big(\overline{\widehat R(Q)_{hd}}\gamma^{g}\gamma^{ef}\gamma^{c}\gamma^{a}\widehat R(Q)_{g}{}^{h}\big)\,\eta_{c}{}^{d}\,T_{ef}\\
&=-\frac{i}{96}\big(\overline{\widehat R(Q)_{ef}}\gamma^{acd}\widehat R(Q)^{ef}\big)\,T_{cd}\\
&-\frac{i}{24}\big(\overline{\widehat R(Q)_{e}{}^{a}}\gamma^{c}\widehat R(Q)^{e}{}_{d}\big)\,T_{c}{}^{d}\\
&+\frac{i}{24}\big(\overline{\widehat R(Q)_{ec}}\gamma^{a}\widehat R(Q)^{e}{}_{d}\big)\,T^{cd}\\
&=-\frac{1}{192}\big(\overline{\widehat R(Q)_{gh}}\gamma^{cd}\widehat R(Q)^{gh}\big)\,\varepsilon_{cd}{}^{a}{}_{ef}\,T^{ef}\\
&-\frac{i}{24}\big(\overline{\widehat R(Q)_{e}{}^{a}}\gamma^{c}\widehat R(Q)^{e}{}_{d}\big)\,T_{c}{}^{d}\\
&+\frac{i}{24}\big(\overline{\widehat R(Q)_{ec}}\gamma^{a}\widehat R(Q)^{e}{}_{d}\big)\,T^{cd}
\end{aligned}\tag{G263}
```

**G264: 1:Ricci contraction:11, bivector coefficient.**

```math
\begin{aligned}
&-\frac{i}{384}\big(\overline{\widehat R(Q)_{hd}}\gamma^{g}\gamma^{ef}\gamma^{c}\gamma^{[ab]}\widehat R(Q)_{g}{}^{h}\big)\,\eta_{c}{}^{d}\,T_{ef}\\
&=\frac{i}{24}\big(\overline{\widehat R(Q)_{e}{}^{[a}}\gamma^{b]c}\widehat R(Q)^{e}{}_{d}\big)\,T_{c}{}^{d}\\
&+\frac{i}{48}\big(\overline{\widehat R(Q)_{de}}\gamma^{[a|c|}\widehat R(Q)^{|de|}\big)\,T_{|c|}{}^{b]}\\
&-\frac{i}{24}\big(\overline{\widehat R(Q)_{d}{}^{[a}}\widehat R(Q)^{|d|}{}_{|c|}\big)\,T^{|c|b]}
\end{aligned}\tag{G264}
```

**G265: 1:Ricci contraction:11, scalar coefficient.**

```math
\begin{aligned}
&-\frac{i}{192}\big(\overline{\widehat R(Q)_{hd}}\gamma^{c}\gamma^{ef}\gamma^{g}\widehat R(Q)_{g}{}^{h}\big)\,\eta_{c}{}^{d}\,T_{ef}\\
&=0
\end{aligned}\tag{G265}
```

**G266: 1:Ricci contraction:11, vector coefficient.**

```math
\begin{aligned}
&-\frac{i}{192}\big(\overline{\widehat R(Q)_{hd}}\gamma^{c}\gamma^{ef}\gamma^{g}\gamma^{a}\widehat R(Q)_{g}{}^{h}\big)\,\eta_{c}{}^{d}\,T_{ef}\\
&=0
\end{aligned}\tag{G266}
```

**G267: 1:Ricci contraction:11, bivector coefficient.**

```math
\begin{aligned}
&\frac{i}{384}\big(\overline{\widehat R(Q)_{hd}}\gamma^{c}\gamma^{ef}\gamma^{g}\gamma^{[ab]}\widehat R(Q)_{g}{}^{h}\big)\,\eta_{c}{}^{d}\,T_{ef}\\
&=0
\end{aligned}\tag{G267}
```

**G268: 1:Ricci contraction:12, scalar coefficient.**

```math
\begin{aligned}
&\frac{1}{24}\big(\overline{\mathcal D_{f}\chi}\gamma^{e}\widehat R(Q)^{f}{}_{d}\big)\,\eta_{c}{}^{d}\,\eta^{c}{}_{e}\\
&=0
\end{aligned}\tag{G268}
```

**G269: 1:Ricci contraction:12, vector coefficient.**

```math
\begin{aligned}
&\frac{1}{24}\big(\overline{\mathcal D_{f}\chi}\gamma^{e}\gamma^{a}\widehat R(Q)^{f}{}_{d}\big)\,\eta_{c}{}^{d}\,\eta^{c}{}_{e}\\
&=-\frac{1}{12}\big(\overline{\widehat R(Q)_{c}{}^{a}}\mathcal D^{c}\chi\big)
\end{aligned}\tag{G269}
```

**G270: 1:Ricci contraction:12, bivector coefficient.**

```math
\begin{aligned}
&-\frac{1}{48}\big(\overline{\mathcal D_{f}\chi}\gamma^{e}\gamma^{[ab]}\widehat R(Q)^{f}{}_{d}\big)\,\eta_{c}{}^{d}\,\eta^{c}{}_{e}\\
&=\frac{1}{12}\big(\overline{\widehat R(Q)_{c}{}^{[a}}\gamma^{b]}\mathcal D^{c}\chi\big)
\end{aligned}\tag{G270}
```

**G271: 1:Ricci contraction:12, scalar coefficient.**

```math
\begin{aligned}
&-\frac{1}{24}\big(\overline{\mathcal D_{f}\chi}\gamma^{e}\widehat R(Q)^{f}{}_{e}\big)\,\eta_{cd}\,\eta^{cd}\\
&=0
\end{aligned}\tag{G271}
```

**G272: 1:Ricci contraction:12, vector coefficient.**

```math
\begin{aligned}
&-\frac{1}{24}\big(\overline{\mathcal D_{f}\chi}\gamma^{e}\gamma^{a}\widehat R(Q)^{f}{}_{e}\big)\,\eta_{cd}\,\eta^{cd}\\
&=\frac{5}{12}\big(\overline{\widehat R(Q)_{c}{}^{a}}\mathcal D^{c}\chi\big)
\end{aligned}\tag{G272}
```

**G273: 1:Ricci contraction:12, bivector coefficient.**

```math
\begin{aligned}
&\frac{1}{48}\big(\overline{\mathcal D_{f}\chi}\gamma^{e}\gamma^{[ab]}\widehat R(Q)^{f}{}_{e}\big)\,\eta_{cd}\,\eta^{cd}\\
&=-\frac{5}{12}\big(\overline{\widehat R(Q)_{c}{}^{[a}}\gamma^{b]}\mathcal D^{c}\chi\big)
\end{aligned}\tag{G273}
```

**G274: 1:Ricci contraction:12, scalar coefficient.**

```math
\begin{aligned}
&-\frac{1}{24}\big(\overline{\mathcal D_{e}\chi}\gamma^{f}\widehat R(Q)_{cd}\big)\,\eta^{cd}\,\eta^{e}{}_{f}\\
&=0
\end{aligned}\tag{G274}
```

**G275: 1:Ricci contraction:12, vector coefficient.**

```math
\begin{aligned}
&-\frac{1}{24}\big(\overline{\mathcal D_{e}\chi}\gamma^{f}\gamma^{a}\widehat R(Q)_{cd}\big)\,\eta^{cd}\,\eta^{e}{}_{f}\\
&=0
\end{aligned}\tag{G275}
```

**G276: 1:Ricci contraction:12, bivector coefficient.**

```math
\begin{aligned}
&\frac{1}{48}\big(\overline{\mathcal D_{e}\chi}\gamma^{f}\gamma^{[ab]}\widehat R(Q)_{cd}\big)\,\eta^{cd}\,\eta^{e}{}_{f}\\
&=0
\end{aligned}\tag{G276}
```

**G277: 1:Ricci contraction:12, scalar coefficient.**

```math
\begin{aligned}
&\frac{1}{24}\big(\overline{\mathcal D_{e}\chi}\gamma^{f}\widehat R(Q)_{cf}\big)\,\eta^{c}{}_{d}\,\eta^{ed}\\
&=0
\end{aligned}\tag{G277}
```

**G278: 1:Ricci contraction:12, vector coefficient.**

```math
\begin{aligned}
&\frac{1}{24}\big(\overline{\mathcal D_{e}\chi}\gamma^{f}\gamma^{a}\widehat R(Q)_{cf}\big)\,\eta^{c}{}_{d}\,\eta^{ed}\\
&=-\frac{1}{12}\big(\overline{\widehat R(Q)_{c}{}^{a}}\mathcal D^{c}\chi\big)
\end{aligned}\tag{G278}
```

**G279: 1:Ricci contraction:12, bivector coefficient.**

```math
\begin{aligned}
&-\frac{1}{48}\big(\overline{\mathcal D_{e}\chi}\gamma^{f}\gamma^{[ab]}\widehat R(Q)_{cf}\big)\,\eta^{c}{}_{d}\,\eta^{ed}\\
&=\frac{1}{12}\big(\overline{\widehat R(Q)_{c}{}^{[a}}\gamma^{b]}\mathcal D^{c}\chi\big)
\end{aligned}\tag{G279}
```

**G280: 1:Ricci contraction:13, scalar coefficient.**

```math
\begin{aligned}
&-\frac{i}{24}\big(\bar\chi\gamma^{e}\gamma^{fg}\gamma^{h}\widehat R(Q)_{hd}\big)\,\eta_{c}{}^{d}\,\eta^{c}{}_{e}\,T_{fg}\\
&=0
\end{aligned}\tag{G280}
```

**G281: 1:Ricci contraction:13, vector coefficient.**

```math
\begin{aligned}
&-\frac{i}{24}\big(\bar\chi\gamma^{e}\gamma^{fg}\gamma^{h}\gamma^{a}\widehat R(Q)_{hd}\big)\,\eta_{c}{}^{d}\,\eta^{c}{}_{e}\,T_{fg}\\
&=\frac{i}{3}\big(\overline{\widehat R(Q)^{a}{}_{c}}\gamma^{d}\chi\big)\,T^{c}{}_{d}
\end{aligned}\tag{G281}
```

**G282: 1:Ricci contraction:13, bivector coefficient.**

```math
\begin{aligned}
&\frac{i}{48}\big(\bar\chi\gamma^{e}\gamma^{fg}\gamma^{h}\gamma^{[ab]}\widehat R(Q)_{hd}\big)\,\eta_{c}{}^{d}\,\eta^{c}{}_{e}\,T_{fg}\\
&=\frac{i}{8}\big(\overline{\widehat R(Q)^{[ab]}}\gamma^{cd}\chi\big)\,T_{cd}\\
&-\frac{i}{6}\big(\overline{\widehat R(Q)^{[a}{}_{|c|}}\gamma^{b]d}\chi\big)\,T^{c}{}_{d}\\
&-\frac{i}{3}\big(\overline{\widehat R(Q)^{[a}{}_{|c|}}\chi\big)\,T^{|c|b]}\\
&-\frac{i}{24}\big(\overline{\widehat R(Q)_{cd}}\gamma^{[ab]}\chi\big)\,T^{cd}
\end{aligned}\tag{G282}
```

**G283: 1:Ricci contraction:13, scalar coefficient.**

```math
\begin{aligned}
&\frac{i}{24}\big(\bar\chi\gamma^{g}\gamma^{ef}\gamma^{h}\widehat R(Q)_{hg}\big)\,\eta_{cd}\,\eta^{cd}\,T_{ef}\\
&=0
\end{aligned}\tag{G283}
```

**G284: 1:Ricci contraction:13, vector coefficient.**

```math
\begin{aligned}
&\frac{i}{24}\big(\bar\chi\gamma^{g}\gamma^{ef}\gamma^{h}\gamma^{a}\widehat R(Q)_{hg}\big)\,\eta_{cd}\,\eta^{cd}\,T_{ef}\\
&=-\frac{5i}{3}\big(\overline{\widehat R(Q)^{a}{}_{c}}\gamma^{d}\chi\big)\,T^{c}{}_{d}
\end{aligned}\tag{G284}
```

**G285: 1:Ricci contraction:13, bivector coefficient.**

```math
\begin{aligned}
&-\frac{i}{48}\big(\bar\chi\gamma^{g}\gamma^{ef}\gamma^{h}\gamma^{[ab]}\widehat R(Q)_{hg}\big)\,\eta_{cd}\,\eta^{cd}\,T_{ef}\\
&=-\frac{5i}{8}\big(\overline{\widehat R(Q)^{[ab]}}\gamma^{cd}\chi\big)\,T_{cd}\\
&+\frac{5i}{6}\big(\overline{\widehat R(Q)^{[a}{}_{|c|}}\gamma^{b]d}\chi\big)\,T^{c}{}_{d}\\
&+\frac{5i}{3}\big(\overline{\widehat R(Q)^{[a}{}_{|c|}}\chi\big)\,T^{|c|b]}\\
&+\frac{5i}{24}\big(\overline{\widehat R(Q)_{cd}}\gamma^{[ab]}\chi\big)\,T^{cd}
\end{aligned}\tag{G285}
```

**G286: 1:Ricci contraction:13, scalar coefficient.**

```math
\begin{aligned}
&\frac{i}{24}\big(\bar\chi\gamma^{f}\gamma^{gh}\gamma^{e}\widehat R(Q)_{cd}\big)\,\eta^{cd}\,\eta_{ef}\,T_{gh}\\
&=0
\end{aligned}\tag{G286}
```

**G287: 1:Ricci contraction:13, vector coefficient.**

```math
\begin{aligned}
&\frac{i}{24}\big(\bar\chi\gamma^{f}\gamma^{gh}\gamma^{e}\gamma^{a}\widehat R(Q)_{cd}\big)\,\eta^{cd}\,\eta_{ef}\,T_{gh}\\
&=0
\end{aligned}\tag{G287}
```

**G288: 1:Ricci contraction:13, bivector coefficient.**

```math
\begin{aligned}
&-\frac{i}{48}\big(\bar\chi\gamma^{f}\gamma^{gh}\gamma^{e}\gamma^{[ab]}\widehat R(Q)_{cd}\big)\,\eta^{cd}\,\eta_{ef}\,T_{gh}\\
&=0
\end{aligned}\tag{G288}
```

**G289: 1:Ricci contraction:13, scalar coefficient.**

```math
\begin{aligned}
&-\frac{i}{24}\big(\bar\chi\gamma^{h}\gamma^{fg}\gamma^{e}\widehat R(Q)_{ch}\big)\,\eta^{c}{}_{d}\,\eta_{e}{}^{d}\,T_{fg}\\
&=0
\end{aligned}\tag{G289}
```

**G290: 1:Ricci contraction:13, vector coefficient.**

```math
\begin{aligned}
&-\frac{i}{24}\big(\bar\chi\gamma^{h}\gamma^{fg}\gamma^{e}\gamma^{a}\widehat R(Q)_{ch}\big)\,\eta^{c}{}_{d}\,\eta_{e}{}^{d}\,T_{fg}\\
&=\frac{i}{3}\big(\overline{\widehat R(Q)^{a}{}_{c}}\gamma^{d}\chi\big)\,T^{c}{}_{d}
\end{aligned}\tag{G290}
```

**G291: 1:Ricci contraction:13, bivector coefficient.**

```math
\begin{aligned}
&\frac{i}{48}\big(\bar\chi\gamma^{h}\gamma^{fg}\gamma^{e}\gamma^{[ab]}\widehat R(Q)_{ch}\big)\,\eta^{c}{}_{d}\,\eta_{e}{}^{d}\,T_{fg}\\
&=\frac{i}{8}\big(\overline{\widehat R(Q)^{[ab]}}\gamma^{cd}\chi\big)\,T_{cd}\\
&-\frac{i}{6}\big(\overline{\widehat R(Q)^{[a}{}_{|c|}}\gamma^{b]d}\chi\big)\,T^{c}{}_{d}\\
&-\frac{i}{3}\big(\overline{\widehat R(Q)^{[a}{}_{|c|}}\chi\big)\,T^{|c|b]}\\
&-\frac{i}{24}\big(\overline{\widehat R(Q)_{cd}}\gamma^{[ab]}\chi\big)\,T^{cd}
\end{aligned}\tag{G291}
```

#### Block 2

The original spinor term is $`-4i\gamma_c\widehat R_{ab}{}^i(Q)\mathcal D^aT^{bc}`$.

**G292: R4, whole coefficient matrix.**

```math
\begin{aligned}
&-i\widehat C_{cdef}\,(\mathcal D^{c}T^{d}{}_{g})\,\gamma^{g}\gamma^{ef}\\
&=-i\widehat C_{cdef}\,(\mathcal D^{c}T^{d}{}_{g})\,\gamma^{efg}\\
&+2i\widehat C_{cdef}\,(\mathcal D^{c}T^{df})\,\gamma^{e}\\
&=-\frac{1}{2}\widehat C_{cdef}\,\varepsilon^{ef}{}_{ghj}\,(\mathcal D^{c}T^{dj})\,\gamma^{gh}\\
&+2i\widehat C_{cdef}\,(\mathcal D^{c}T^{df})\,\gamma^{e}
\end{aligned}\tag{G292}
```

**G293: R5, whole coefficient matrix.**

```math
\begin{aligned}
&4(\mathcal D_{c}T_{de})\,(\mathcal D^{c}T_{fg})\,\gamma^{g}\gamma^{de}\gamma^{f}\\
&-4(\mathcal D_{c}T_{de})\,(\mathcal D_{f}T^{c}{}_{g})\,\gamma^{g}\gamma^{de}\gamma^{f}\\
&=-4(\mathcal D_{c}T_{de})\,(\mathcal D^{c}T_{fg})\,\gamma^{defg}\\
&-8(\mathcal D_{c}T_{de})\,(\mathcal D^{c}T^{de})\\
&-4(\mathcal D_{c}T_{de})\,(\mathcal D^{e}T_{fg})\,\gamma^{cdfg}\\
&-4(\mathcal D_{c}T_{de})\,(\mathcal D_{f}T^{cf})\,\gamma^{de}\\
&-8(\mathcal D_{c}T_{de})\,(\mathcal D^{d}T_{f}{}^{e})\,\gamma^{cf}\\
&+8(\mathcal D_{c}T_{de})\,(\mathcal D^{d}T^{ce})\\
&=-4i\varepsilon_{cdefg}\,(\mathcal D_{h}T^{de})\,(\mathcal D^{h}T^{fg})\,\gamma^{c}\\
&-8(\mathcal D_{c}T_{de})\,(\mathcal D^{c}T^{de})\\
&-4i\varepsilon_{cdefg}\,(\mathcal D^{d}T^{e}{}_{h})\,(\mathcal D^{h}T^{fg})\,\gamma^{c}\\
&-4(\mathcal D_{c}T_{de})\,(\mathcal D_{f}T^{cf})\,\gamma^{de}\\
&-8(\mathcal D_{c}T_{de})\,(\mathcal D^{d}T_{f}{}^{e})\,\gamma^{cf}\\
&+8(\mathcal D_{c}T_{de})\,(\mathcal D^{d}T^{ce})
\end{aligned}\tag{G293}
```

**G294: R6, whole coefficient matrix.**

```math
\begin{aligned}
&-\frac{4}{3}(\mathcal D_{c}T_{de})\,(\mathcal D^{c}T_{fg})\,\gamma^{g}\gamma^{f}\gamma^{de}\\
&+\frac{4}{3}(\mathcal D_{c}T_{de})\,(\mathcal D_{f}T^{c}{}_{g})\,\gamma^{g}\gamma^{f}\gamma^{de}\\
&=\frac{4}{3}(\mathcal D_{c}T_{de})\,(\mathcal D^{c}T_{fg})\,\gamma^{defg}\\
&-\frac{8}{3}(\mathcal D_{c}T_{de})\,(\mathcal D^{c}T^{de})\\
&+\frac{4}{3}(\mathcal D_{c}T_{de})\,(\mathcal D^{e}T_{fg})\,\gamma^{cdfg}\\
&+\frac{8}{3}(\mathcal D_{c}T_{de})\,(\mathcal D^{d}T_{f}{}^{e})\,\gamma^{cf}\\
&+\frac{8}{3}(\mathcal D_{c}T_{de})\,(\mathcal D^{d}T^{ce})\\
&+\frac{4}{3}(\mathcal D_{c}T_{de})\,(\mathcal D_{f}T^{cf})\,\gamma^{de}\\
&=\frac{4i}{3}\varepsilon_{cdefg}\,(\mathcal D_{h}T^{de})\,(\mathcal D^{h}T^{fg})\,\gamma^{c}\\
&-\frac{8}{3}(\mathcal D_{c}T_{de})\,(\mathcal D^{c}T^{de})\\
&+\frac{4i}{3}\varepsilon_{cdefg}\,(\mathcal D^{d}T^{e}{}_{h})\,(\mathcal D^{h}T^{fg})\,\gamma^{c}\\
&+\frac{8}{3}(\mathcal D_{c}T_{de})\,(\mathcal D^{d}T_{f}{}^{e})\,\gamma^{cf}\\
&+\frac{8}{3}(\mathcal D_{c}T_{de})\,(\mathcal D^{d}T^{ce})\\
&+\frac{4}{3}(\mathcal D_{c}T_{de})\,(\mathcal D_{f}T^{cf})\,\gamma^{de}
\end{aligned}\tag{G294}
```

**G295: R7, whole coefficient matrix.**

```math
\begin{aligned}
&-\frac{4}{3}(\mathcal D_{c}T_{de})\,(\mathcal D_{f}T_{gh})\,\gamma^{h}\gamma^{f}\gamma^{c}\gamma^{de}\gamma^{g}\\
&+\frac{4}{3}(\mathcal D_{c}T_{de})\,(\mathcal D_{f}T_{gh})\,\gamma^{h}\gamma^{g}\gamma^{c}\gamma^{de}\gamma^{f}\\
&=-8(\mathcal D_{c}T_{de})\,(\mathcal D_{f}T_{g}{}^{f})\,\gamma^{cdeg}\\
&+\frac{16}{3}(\mathcal D_{c}T_{de})\,(\mathcal D_{f}T_{g}{}^{e})\,\gamma^{cdfg}\\
&+\frac{8}{3}(\mathcal D_{c}T_{de})\,(\mathcal D^{e}T_{fg})\,\gamma^{cdfg}\\
&+\frac{16}{3}(\mathcal D_{c}T_{de})\,(\mathcal D^{d}T_{f}{}^{e})\,\gamma^{cf}\\
&-\frac{16}{3}(\mathcal D_{c}T_{de})\,(\mathcal D_{f}T^{ef})\,\gamma^{cd}\\
&-\frac{32}{3}(\mathcal D_{c}T_{de})\,(\mathcal D^{d}T^{ce})\\
&+\frac{16}{3}(\mathcal D_{c}T_{de})\,(\mathcal D^{c}T^{de})\\
&=-8i\varepsilon_{cdefg}\,(\mathcal D^{d}T^{ef})\,(\mathcal D_{h}T^{gh})\,\gamma^{c}\\
&+\frac{16i}{3}\varepsilon_{cdefg}\,(\mathcal D^{d}T^{e}{}_{h})\,(\mathcal D^{f}T^{gh})\,\gamma^{c}\\
&+\frac{8i}{3}\varepsilon_{cdefg}\,(\mathcal D^{d}T^{e}{}_{h})\,(\mathcal D^{h}T^{fg})\,\gamma^{c}\\
&+\frac{16}{3}(\mathcal D_{c}T_{de})\,(\mathcal D^{d}T_{f}{}^{e})\,\gamma^{cf}\\
&-\frac{16}{3}(\mathcal D_{c}T_{de})\,(\mathcal D_{f}T^{ef})\,\gamma^{cd}\\
&-\frac{32}{3}(\mathcal D_{c}T_{de})\,(\mathcal D^{d}T^{ce})\\
&+\frac{16}{3}(\mathcal D_{c}T_{de})\,(\mathcal D^{c}T^{de})
\end{aligned}\tag{G295}
```

**G296: R8, whole coefficient matrix.**

```math
\begin{aligned}
&-\frac{8}{3}(\mathcal D_{c}T^{c}{}_{d})\,(\mathcal D_{e}T_{fg})\,\gamma^{g}\gamma^{ef}\gamma^{d}\\
&=\frac{8}{3}(\mathcal D_{c}T_{de})\,(\mathcal D_{f}T_{g}{}^{f})\,\gamma^{cdeg}\\
&+\frac{8}{3}(\mathcal D_{c}T_{de})\,(\mathcal D_{f}T^{cf})\,\gamma^{de}\\
&+\frac{16}{3}(\mathcal D_{c}T_{de})\,(\mathcal D_{f}T^{ef})\,\gamma^{cd}\\
&-\frac{8}{3}(\mathcal D_{c}T^{c}{}_{d})\,(\mathcal D_{e}T^{de})\\
&=\frac{8i}{3}\varepsilon_{cdefg}\,(\mathcal D^{d}T^{ef})\,(\mathcal D_{h}T^{gh})\,\gamma^{c}\\
&+\frac{8}{3}(\mathcal D_{c}T_{de})\,(\mathcal D_{f}T^{cf})\,\gamma^{de}\\
&+\frac{16}{3}(\mathcal D_{c}T_{de})\,(\mathcal D_{f}T^{ef})\,\gamma^{cd}\\
&-\frac{8}{3}(\mathcal D_{c}T^{c}{}_{d})\,(\mathcal D_{e}T^{de})
\end{aligned}\tag{G296}
```

**G297: 2:DT:1, scalar coefficient.**

```math
\begin{aligned}
&-\frac{1}{4}\big(\overline{\mathcal D_{e}\chi}\gamma^{cd}\gamma_{d}\widehat R(Q)^{e}{}_{c}\big)\\
&=0
\end{aligned}\tag{G297}
```

**G298: 2:DT:1, vector coefficient.**

```math
\begin{aligned}
&-\frac{1}{4}\big(\overline{\mathcal D_{e}\chi}\gamma^{cd}\gamma^{a}\gamma_{d}\widehat R(Q)^{e}{}_{c}\big)\\
&=-\frac{3}{2}\big(\overline{\widehat R(Q)_{c}{}^{a}}\mathcal D^{c}\chi\big)
\end{aligned}\tag{G298}
```

**G299: 2:DT:1, bivector coefficient.**

```math
\begin{aligned}
&\frac{1}{8}\big(\overline{\mathcal D_{e}\chi}\gamma^{cd}\gamma^{[ab]}\gamma_{d}\widehat R(Q)^{e}{}_{c}\big)\\
&=-\frac{1}{2}\big(\overline{\widehat R(Q)_{c}{}^{[a}}\gamma^{b]}\mathcal D^{c}\chi\big)
\end{aligned}\tag{G299}
```

**G300: 2:DT:2, scalar coefficient.**

```math
\begin{aligned}
&-\frac{3}{64}\big(\overline{\mathcal D_{d}\widehat R(Q)_{ec}}\gamma^{c}\widehat R(Q)^{de}\big)\\
&=0
\end{aligned}\tag{G300}
```

**G301: 2:DT:2, vector coefficient.**

```math
\begin{aligned}
&-\frac{3}{64}\big(\overline{\mathcal D_{d}\widehat R(Q)_{ec}}\gamma^{a}\gamma^{c}\widehat R(Q)^{de}\big)\\
&=\frac{3}{32}\big(\overline{\widehat R(Q)_{cd}}\mathcal D^{c}\widehat R(Q)^{da}\big)
\end{aligned}\tag{G301}
```

**G302: 2:DT:2, bivector coefficient.**

```math
\begin{aligned}
&\frac{3}{128}\big(\overline{\mathcal D_{d}\widehat R(Q)_{ec}}\gamma^{[ab]}\gamma^{c}\widehat R(Q)^{de}\big)\\
&=-\frac{3}{32}\big(\overline{\widehat R(Q)_{cd}}\gamma^{[a}\mathcal D^{|c|}\widehat R(Q)^{|d|b]}\big)
\end{aligned}\tag{G302}
```

**G303: 2:DT:3, scalar coefficient.**

```math
\begin{aligned}
&\frac{i}{4}\big(\bar\chi\gamma^{ef}\gamma^{cd}\gamma^{g}\gamma_{f}\widehat R(Q)_{ge}\big)\,T_{cd}\\
&=-4i\big(\overline{\widehat R(Q)_{cd}}\chi\big)\,T^{cd}
\end{aligned}\tag{G303}
```

**G304: 2:DT:3, vector coefficient.**

```math
\begin{aligned}
&\frac{i}{4}\big(\bar\chi\gamma^{ef}\gamma^{cd}\gamma^{g}\gamma^{a}\gamma_{f}\widehat R(Q)_{ge}\big)\,T_{cd}\\
&=6i\big(\overline{\widehat R(Q)^{a}{}_{c}}\gamma^{d}\chi\big)\,T^{c}{}_{d}\\
&+4i\big(\overline{\widehat R(Q)_{cd}}\gamma^{a}\chi\big)\,T^{cd}
\end{aligned}\tag{G304}
```

**G305: 2:DT:3, bivector coefficient.**

```math
\begin{aligned}
&-\frac{i}{8}\big(\bar\chi\gamma^{ef}\gamma^{cd}\gamma^{g}\gamma^{[ab]}\gamma_{f}\widehat R(Q)_{ge}\big)\,T_{cd}\\
&=-\frac{3i}{2}\big(\overline{\widehat R(Q)^{[ab]}}\gamma^{cd}\chi\big)\,T_{cd}\\
&+4i\big(\overline{\widehat R(Q)^{[a}{}_{|c|}}\gamma^{b]d}\chi\big)\,T^{c}{}_{d}\\
&+2i\big(\overline{\widehat R(Q)^{[a}{}_{|c|}}\chi\big)\,T^{|c|b]}\\
&-\frac{i}{2}\big(\overline{\widehat R(Q)_{cd}}\gamma^{[ab]}\chi\big)\,T^{cd}
\end{aligned}\tag{G305}
```

**G306: 2:DT:4, scalar coefficient.**

```math
\begin{aligned}
&\frac{3i}{64}\big(\overline{\widehat R(Q)_{gf}}\gamma^{cd}\gamma^{e}\gamma^{f}\widehat R(Q)_{e}{}^{g}\big)\,T_{cd}\\
&=-\frac{3i}{32}\big(\overline{\widehat R(Q)_{ef}}\gamma^{cd}\widehat R(Q)^{ef}\big)\,T_{cd}
\end{aligned}\tag{G306}
```

**G307: 2:DT:4, vector coefficient.**

```math
\begin{aligned}
&\frac{3i}{64}\big(\overline{\widehat R(Q)_{gf}}\gamma^{cd}\gamma^{e}\gamma^{a}\gamma^{f}\widehat R(Q)_{e}{}^{g}\big)\,T_{cd}\\
&=\frac{3i}{32}\big(\overline{\widehat R(Q)_{ef}}\gamma^{acd}\widehat R(Q)^{ef}\big)\,T_{cd}\\
&+\frac{3i}{8}\big(\overline{\widehat R(Q)_{e}{}^{a}}\gamma^{c}\widehat R(Q)^{e}{}_{d}\big)\,T_{c}{}^{d}\\
&=\frac{3}{64}\big(\overline{\widehat R(Q)_{gh}}\gamma^{cd}\widehat R(Q)^{gh}\big)\,\varepsilon_{cd}{}^{a}{}_{ef}\,T^{ef}\\
&+\frac{3i}{8}\big(\overline{\widehat R(Q)_{e}{}^{a}}\gamma^{c}\widehat R(Q)^{e}{}_{d}\big)\,T_{c}{}^{d}
\end{aligned}\tag{G307}
```

**G308: 2:DT:4, bivector coefficient.**

```math
\begin{aligned}
&-\frac{3i}{128}\big(\overline{\widehat R(Q)_{gf}}\gamma^{cd}\gamma^{e}\gamma^{[ab]}\gamma^{f}\widehat R(Q)_{e}{}^{g}\big)\,T_{cd}\\
&=\frac{3i}{8}\big(\overline{\widehat R(Q)_{e}{}^{[a}}\gamma^{b]c}\widehat R(Q)^{e}{}_{d}\big)\,T_{c}{}^{d}\\
&+\frac{3i}{16}\big(\overline{\widehat R(Q)_{de}}\gamma^{[a|c|}\widehat R(Q)^{|de|}\big)\,T_{|c|}{}^{b]}\\
&-\frac{3i}{8}\big(\overline{\widehat R(Q)_{d}{}^{[a}}\widehat R(Q)^{|d|}{}_{|c|}\big)\,T^{|c|b]}
\end{aligned}\tag{G308}
```

**G309: 2:DT:5, scalar coefficient.**

```math
\begin{aligned}
&-i\big(\bar\chi\gamma^{e}\gamma^{d}\widehat R(Q)_{ec}\big)\,T^{c}{}_{d}\\
&=-2i\big(\overline{\widehat R(Q)_{cd}}\chi\big)\,T^{cd}
\end{aligned}\tag{G309}
```

**G310: 2:DT:5, vector coefficient.**

```math
\begin{aligned}
&-i\big(\bar\chi\gamma^{e}\gamma^{a}\gamma^{d}\widehat R(Q)_{ec}\big)\,T^{c}{}_{d}\\
&=2i\big(\overline{\widehat R(Q)_{cd}}\gamma^{a}\chi\big)\,T^{cd}\\
&+2i\big(\overline{\widehat R(Q)^{a}{}_{c}}\gamma^{d}\chi\big)\,T^{c}{}_{d}
\end{aligned}\tag{G310}
```

**G311: 2:DT:5, bivector coefficient.**

```math
\begin{aligned}
&\frac{i}{2}\big(\bar\chi\gamma^{e}\gamma^{[ab]}\gamma^{d}\widehat R(Q)_{ec}\big)\,T^{c}{}_{d}\\
&=-i\big(\overline{\widehat R(Q)_{cd}}\gamma^{[ab]}\chi\big)\,T^{cd}\\
&+2i\big(\overline{\widehat R(Q)^{[a}{}_{|c|}}\gamma^{b]d}\chi\big)\,T^{c}{}_{d}\\
&-2i\big(\overline{\widehat R(Q)^{[a}{}_{|c|}}\chi\big)\,T^{|c|b]}
\end{aligned}\tag{G311}
```

**G312: 2:DT:6, scalar coefficient.**

```math
\begin{aligned}
&\frac{i}{8}\big(\overline{\widehat R(Q)_{fc}}\gamma^{e}\gamma^{d}\widehat R(Q)^{f}{}_{e}\big)\,T^{c}{}_{d}\\
&=\frac{i}{4}\big(\overline{\widehat R(Q)_{ec}}\widehat R(Q)^{e}{}_{d}\big)\,T^{cd}
\end{aligned}\tag{G312}
```

**G313: 2:DT:6, vector coefficient.**

```math
\begin{aligned}
&\frac{i}{8}\big(\overline{\widehat R(Q)_{fc}}\gamma^{e}\gamma^{a}\gamma^{d}\widehat R(Q)^{f}{}_{e}\big)\,T^{c}{}_{d}\\
&=-\frac{i}{4}\big(\overline{\widehat R(Q)_{ec}}\gamma^{a}\widehat R(Q)^{e}{}_{d}\big)\,T^{cd}\\
&+\frac{i}{4}\big(\overline{\widehat R(Q)_{e}{}^{a}}\gamma^{c}\widehat R(Q)^{e}{}_{d}\big)\,T_{c}{}^{d}
\end{aligned}\tag{G313}
```

**G314: 2:DT:6, bivector coefficient.**

```math
\begin{aligned}
&-\frac{i}{16}\big(\overline{\widehat R(Q)_{fc}}\gamma^{e}\gamma^{[ab]}\gamma^{d}\widehat R(Q)^{f}{}_{e}\big)\,T^{c}{}_{d}\\
&=\frac{i}{4}\big(\overline{\widehat R(Q)_{e}{}^{[a}}\gamma^{b]c}\widehat R(Q)^{e}{}_{d}\big)\,T_{c}{}^{d}\\
&+\frac{i}{4}\big(\overline{\widehat R(Q)_{d}{}^{[a}}\widehat R(Q)^{|d|}{}_{|c|}\big)\,T^{|c|b]}
\end{aligned}\tag{G314}
```

**G315: 2:DT:6, scalar coefficient.**

```math
\begin{aligned}
&-\frac{i}{8}\big(\overline{\widehat R(Q)_{ef}}\gamma^{c}\gamma^{d}\widehat R(Q)^{ef}\big)\,T_{cd}\\
&=-\frac{i}{8}\big(\overline{\widehat R(Q)_{ef}}\gamma^{cd}\widehat R(Q)^{ef}\big)\,T_{cd}
\end{aligned}\tag{G315}
```

**G316: 2:DT:6, vector coefficient.**

```math
\begin{aligned}
&-\frac{i}{8}\big(\overline{\widehat R(Q)_{ef}}\gamma^{c}\gamma^{a}\gamma^{d}\widehat R(Q)^{ef}\big)\,T_{cd}\\
&=\frac{i}{8}\big(\overline{\widehat R(Q)_{ef}}\gamma^{acd}\widehat R(Q)^{ef}\big)\,T_{cd}\\
&=\frac{1}{16}\big(\overline{\widehat R(Q)_{gh}}\gamma^{cd}\widehat R(Q)^{gh}\big)\,\varepsilon_{cd}{}^{a}{}_{ef}\,T^{ef}
\end{aligned}\tag{G316}
```

**G317: 2:DT:6, bivector coefficient.**

```math
\begin{aligned}
&\frac{i}{16}\big(\overline{\widehat R(Q)_{ef}}\gamma^{c}\gamma^{[ab]}\gamma^{d}\widehat R(Q)^{ef}\big)\,T_{cd}\\
&=0
\end{aligned}\tag{G317}
```

**G318: 2:DT:7, scalar coefficient.**

```math
\begin{aligned}
&\frac{i}{8}\big(\overline{\widehat R(Q)_{fc}}\gamma^{e}\gamma^{d}\widehat R(Q)_{e}{}^{f}\big)\,T^{c}{}_{d}\\
&=-\frac{i}{4}\big(\overline{\widehat R(Q)_{ec}}\widehat R(Q)^{e}{}_{d}\big)\,T^{cd}
\end{aligned}\tag{G318}
```

**G319: 2:DT:7, vector coefficient.**

```math
\begin{aligned}
&\frac{i}{8}\big(\overline{\widehat R(Q)_{fc}}\gamma^{e}\gamma^{a}\gamma^{d}\widehat R(Q)_{e}{}^{f}\big)\,T^{c}{}_{d}\\
&=\frac{i}{4}\big(\overline{\widehat R(Q)_{ec}}\gamma^{a}\widehat R(Q)^{e}{}_{d}\big)\,T^{cd}\\
&-\frac{i}{4}\big(\overline{\widehat R(Q)_{e}{}^{a}}\gamma^{c}\widehat R(Q)^{e}{}_{d}\big)\,T_{c}{}^{d}
\end{aligned}\tag{G319}
```

**G320: 2:DT:7, bivector coefficient.**

```math
\begin{aligned}
&-\frac{i}{16}\big(\overline{\widehat R(Q)_{fc}}\gamma^{e}\gamma^{[ab]}\gamma^{d}\widehat R(Q)_{e}{}^{f}\big)\,T^{c}{}_{d}\\
&=-\frac{i}{4}\big(\overline{\widehat R(Q)_{e}{}^{[a}}\gamma^{b]c}\widehat R(Q)^{e}{}_{d}\big)\,T_{c}{}^{d}\\
&-\frac{i}{4}\big(\overline{\widehat R(Q)_{d}{}^{[a}}\widehat R(Q)^{|d|}{}_{|c|}\big)\,T^{|c|b]}
\end{aligned}\tag{G320}
```

**G321: 2:DT:8, scalar coefficient.**

```math
\begin{aligned}
&i\big(\bar\chi\gamma^{e}\gamma^{f}\widehat R(Q)_{cd}\big)\,\eta^{cd}\,T_{ef}\\
&=0
\end{aligned}\tag{G321}
```

**G322: 2:DT:8, vector coefficient.**

```math
\begin{aligned}
&i\big(\bar\chi\gamma^{e}\gamma^{a}\gamma^{f}\widehat R(Q)_{cd}\big)\,\eta^{cd}\,T_{ef}\\
&=0
\end{aligned}\tag{G322}
```

**G323: 2:DT:8, bivector coefficient.**

```math
\begin{aligned}
&-\frac{i}{2}\big(\bar\chi\gamma^{e}\gamma^{[ab]}\gamma^{f}\widehat R(Q)_{cd}\big)\,\eta^{cd}\,T_{ef}\\
&=0
\end{aligned}\tag{G323}
```

**G324: 2:DT:8, scalar coefficient.**

```math
\begin{aligned}
&-i\big(\bar\chi\gamma^{f}\gamma^{e}\widehat R(Q)_{cf}\big)\,\eta^{c}{}_{d}\,T^{d}{}_{e}\\
&=2i\big(\overline{\widehat R(Q)_{cd}}\chi\big)\,T^{cd}
\end{aligned}\tag{G324}
```

**G325: 2:DT:8, vector coefficient.**

```math
\begin{aligned}
&-i\big(\bar\chi\gamma^{f}\gamma^{a}\gamma^{e}\widehat R(Q)_{cf}\big)\,\eta^{c}{}_{d}\,T^{d}{}_{e}\\
&=-2i\big(\overline{\widehat R(Q)_{cd}}\gamma^{a}\chi\big)\,T^{cd}\\
&-2i\big(\overline{\widehat R(Q)^{a}{}_{c}}\gamma^{d}\chi\big)\,T^{c}{}_{d}
\end{aligned}\tag{G325}
```

**G326: 2:DT:8, bivector coefficient.**

```math
\begin{aligned}
&\frac{i}{2}\big(\bar\chi\gamma^{f}\gamma^{[ab]}\gamma^{e}\widehat R(Q)_{cf}\big)\,\eta^{c}{}_{d}\,T^{d}{}_{e}\\
&=i\big(\overline{\widehat R(Q)_{cd}}\gamma^{[ab]}\chi\big)\,T^{cd}\\
&-2i\big(\overline{\widehat R(Q)^{[a}{}_{|c|}}\gamma^{b]d}\chi\big)\,T^{c}{}_{d}\\
&+2i\big(\overline{\widehat R(Q)^{[a}{}_{|c|}}\chi\big)\,T^{|c|b]}
\end{aligned}\tag{G326}
```

**G327: 2:DT:9, scalar coefficient.**

```math
\begin{aligned}
&\frac{i}{8}\big(\overline{\widehat R(Q)_{fd}}\gamma^{e}\gamma_{e}\widehat R(Q)^{f}{}_{c}\big)\,T^{cd}\\
&=-\frac{5i}{8}\big(\overline{\widehat R(Q)_{ec}}\widehat R(Q)^{e}{}_{d}\big)\,T^{cd}
\end{aligned}\tag{G327}
```

**G328: 2:DT:9, vector coefficient.**

```math
\begin{aligned}
&\frac{i}{8}\big(\overline{\widehat R(Q)_{fd}}\gamma^{e}\gamma^{a}\gamma_{e}\widehat R(Q)^{f}{}_{c}\big)\,T^{cd}\\
&=\frac{3i}{8}\big(\overline{\widehat R(Q)_{ec}}\gamma^{a}\widehat R(Q)^{e}{}_{d}\big)\,T^{cd}
\end{aligned}\tag{G328}
```

**G329: 2:DT:9, bivector coefficient.**

```math
\begin{aligned}
&-\frac{i}{16}\big(\overline{\widehat R(Q)_{fd}}\gamma^{e}\gamma^{[ab]}\gamma_{e}\widehat R(Q)^{f}{}_{c}\big)\,T^{cd}\\
&=0
\end{aligned}\tag{G329}
```

**G330: 2:DT:9, scalar coefficient.**

```math
\begin{aligned}
&-\frac{i}{8}\big(\overline{\widehat R(Q)_{fe}}\gamma^{d}\gamma^{e}\widehat R(Q)^{f}{}_{c}\big)\,T^{c}{}_{d}\\
&=\frac{i}{4}\big(\overline{\widehat R(Q)_{ec}}\widehat R(Q)^{e}{}_{d}\big)\,T^{cd}
\end{aligned}\tag{G330}
```

**G331: 2:DT:9, vector coefficient.**

```math
\begin{aligned}
&-\frac{i}{8}\big(\overline{\widehat R(Q)_{fe}}\gamma^{d}\gamma^{a}\gamma^{e}\widehat R(Q)^{f}{}_{c}\big)\,T^{c}{}_{d}\\
&=-\frac{i}{4}\big(\overline{\widehat R(Q)_{ec}}\gamma^{a}\widehat R(Q)^{e}{}_{d}\big)\,T^{cd}\\
&+\frac{i}{4}\big(\overline{\widehat R(Q)_{e}{}^{a}}\gamma^{c}\widehat R(Q)^{e}{}_{d}\big)\,T_{c}{}^{d}
\end{aligned}\tag{G331}
```

**G332: 2:DT:9, bivector coefficient.**

```math
\begin{aligned}
&\frac{i}{16}\big(\overline{\widehat R(Q)_{fe}}\gamma^{d}\gamma^{[ab]}\gamma^{e}\widehat R(Q)^{f}{}_{c}\big)\,T^{c}{}_{d}\\
&=-\frac{i}{4}\big(\overline{\widehat R(Q)_{e}{}^{[a}}\gamma^{b]c}\widehat R(Q)^{e}{}_{d}\big)\,T_{c}{}^{d}\\
&-\frac{i}{4}\big(\overline{\widehat R(Q)_{d}{}^{[a}}\widehat R(Q)^{|d|}{}_{|c|}\big)\,T^{|c|b]}
\end{aligned}\tag{G332}
```

**G333: 2:DT:10, scalar coefficient.**

```math
\begin{aligned}
&\frac{i}{8}\big(\overline{\widehat R(Q)_{fd}}\gamma^{e}\gamma^{f}\widehat R(Q)_{ec}\big)\,T^{cd}\\
&=-\frac{i}{4}\big(\overline{\widehat R(Q)_{ec}}\widehat R(Q)^{e}{}_{d}\big)\,T^{cd}
\end{aligned}\tag{G333}
```

**G334: 2:DT:10, vector coefficient.**

```math
\begin{aligned}
&\frac{i}{8}\big(\overline{\widehat R(Q)_{fd}}\gamma^{e}\gamma^{a}\gamma^{f}\widehat R(Q)_{ec}\big)\,T^{cd}\\
&=\frac{i}{4}\big(\overline{\widehat R(Q)_{ec}}\gamma^{a}\widehat R(Q)^{e}{}_{d}\big)\,T^{cd}
\end{aligned}\tag{G334}
```

**G335: 2:DT:10, bivector coefficient.**

```math
\begin{aligned}
&-\frac{i}{16}\big(\overline{\widehat R(Q)_{fd}}\gamma^{e}\gamma^{[ab]}\gamma^{f}\widehat R(Q)_{ec}\big)\,T^{cd}\\
&=0
\end{aligned}\tag{G335}
```

**G336: 2:DT:11, scalar coefficient.**

```math
\begin{aligned}
&i\big(\bar\chi\gamma^{f}\gamma^{d}\widehat R(Q)_{ce}\big)\,\eta^{c}{}_{d}\,T^{e}{}_{f}\\
&=0
\end{aligned}\tag{G336}
```

**G337: 2:DT:11, vector coefficient.**

```math
\begin{aligned}
&i\big(\bar\chi\gamma^{f}\gamma^{a}\gamma^{d}\widehat R(Q)_{ce}\big)\,\eta^{c}{}_{d}\,T^{e}{}_{f}\\
&=0
\end{aligned}\tag{G337}
```

**G338: 2:DT:11, bivector coefficient.**

```math
\begin{aligned}
&-\frac{i}{2}\big(\bar\chi\gamma^{f}\gamma^{[ab]}\gamma^{d}\widehat R(Q)_{ce}\big)\,\eta^{c}{}_{d}\,T^{e}{}_{f}\\
&=0
\end{aligned}\tag{G338}
```

**G339: 2:DT:11, scalar coefficient.**

```math
\begin{aligned}
&-i\big(\bar\chi\gamma^{f}\gamma_{f}\widehat R(Q)_{ce}\big)\,\eta^{c}{}_{d}\,T^{ed}\\
&=-5i\big(\overline{\widehat R(Q)_{cd}}\chi\big)\,T^{cd}
\end{aligned}\tag{G339}
```

**G340: 2:DT:11, vector coefficient.**

```math
\begin{aligned}
&-i\big(\bar\chi\gamma^{f}\gamma^{a}\gamma_{f}\widehat R(Q)_{ce}\big)\,\eta^{c}{}_{d}\,T^{ed}\\
&=3i\big(\overline{\widehat R(Q)_{cd}}\gamma^{a}\chi\big)\,T^{cd}
\end{aligned}\tag{G340}
```

**G341: 2:DT:11, bivector coefficient.**

```math
\begin{aligned}
&\frac{i}{2}\big(\bar\chi\gamma^{f}\gamma^{[ab]}\gamma_{f}\widehat R(Q)_{ce}\big)\,\eta^{c}{}_{d}\,T^{ed}\\
&=-\frac{i}{2}\big(\overline{\widehat R(Q)_{cd}}\gamma^{[ab]}\chi\big)\,T^{cd}
\end{aligned}\tag{G341}
```

#### Block 3

The original spinor term is $`\frac{128}{3}\chi^iD`$.

**G342: chi1, whole coefficient matrix.**

```math
\begin{aligned}
&\frac{32}{3}D^2\\
&=\frac{32}{3}D^2
\end{aligned}\tag{G342}
```

**G343: chi3, whole coefficient matrix.**

```math
\begin{aligned}
&\frac{16i}{3}(\mathcal D_{c}T_{de})\,D\,\gamma^{de}\gamma^{c}\\
&=\frac{16i}{3}D\,(\mathcal D_{c}T_{de})\,\gamma^{cde}\\
&+\frac{32i}{3}D\,(\mathcal D_{c}T_{d}{}^{c})\,\gamma^{d}\\
&=\frac{8}{3}D\,\varepsilon_{cdefg}\,(\mathcal D^{e}T^{fg})\,\gamma^{cd}\\
&+\frac{32i}{3}D\,(\mathcal D_{c}T_{d}{}^{c})\,\gamma^{d}
\end{aligned}\tag{G343}
```

**G344: chi4, whole coefficient matrix.**

```math
\begin{aligned}
&-\frac{16i}{3}(\mathcal D_{c}T_{d}{}^{c})\,D\,\gamma^{d}\\
&=-\frac{16i}{3}D\,(\mathcal D_{c}T_{d}{}^{c})\,\gamma^{d}
\end{aligned}\tag{G344}
```

**G345: chi5, whole coefficient matrix.**

```math
\begin{aligned}
&-\frac{32}{3}D\,T_{cd}\,T_{ef}\,\gamma^{cdef}\\
&=-\frac{32i}{3}D\,\varepsilon_{cdefg}\,T^{de}\,T^{fg}\,\gamma^{c}
\end{aligned}\tag{G345}
```

**G346: chi6, whole coefficient matrix.**

```math
\begin{aligned}
&\frac{64}{9}T_{cd}\,T^{cd}\,D\\
&=\frac{64}{9}D\,T_{cd}\,T^{cd}
\end{aligned}\tag{G346}
```

**G347: D1, scalar coefficient.**

```math
\begin{aligned}
&\frac{16}{3}\big(\overline{\mathcal D_{c}\chi}\gamma^{c}\chi\big)\\
&=-\frac{16}{3}\big(\bar\chi\gamma^{c}\mathcal D_{c}\chi\big)
\end{aligned}\tag{G347}
```

**G348: D1, vector coefficient.**

```math
\begin{aligned}
&\frac{16}{3}\big(\overline{\mathcal D_{c}\chi}\gamma^{c}\gamma^{a}\chi\big)\\
&=\frac{16}{3}\big(\bar\chi\gamma^{ca}\mathcal D_{c}\chi\big)\\
&-\frac{16}{3}\big(\bar\chi\mathcal D^{a}\chi\big)
\end{aligned}\tag{G348}
```

**G349: D1, bivector coefficient.**

```math
\begin{aligned}
&-\frac{8}{3}\big(\overline{\mathcal D_{c}\chi}\gamma^{c}\gamma^{[ab]}\chi\big)\\
&=-\frac{8}{3}\big(\bar\chi\gamma^{c[ab]}\mathcal D_{c}\chi\big)\\
&-\frac{16}{3}\big(\bar\chi\gamma^{[a}\mathcal D^{b]}\chi\big)\\
&=\frac{4i}{3}\big(\bar\chi\gamma^{cd}\mathcal D_{e}\chi\big)\,\varepsilon_{cd}{}^{e[ab]}\\
&-\frac{16}{3}\big(\bar\chi\gamma^{[a}\mathcal D^{b]}\chi\big)
\end{aligned}\tag{G349}
```

**G350: D2, scalar coefficient.**

```math
\begin{aligned}
&\frac{80i}{9}\big(\bar\chi\gamma^{cd}\chi\big)\,T_{cd}\\
&=\frac{80i}{9}\big(\bar\chi\gamma^{cd}\chi\big)\,T_{cd}
\end{aligned}\tag{G350}
```

**G351: D2, vector coefficient.**

```math
\begin{aligned}
&\frac{80i}{9}\big(\bar\chi\gamma^{cd}\gamma^{a}\chi\big)\,T_{cd}\\
&=\frac{80i}{9}\big(\bar\chi\gamma^{acd}\chi\big)\,T_{cd}\\
&=\frac{40}{9}\big(\bar\chi\gamma^{cd}\chi\big)\,\varepsilon_{cd}{}^{a}{}_{ef}\,T^{ef}
\end{aligned}\tag{G351}
```

**G352: D2, bivector coefficient.**

```math
\begin{aligned}
&-\frac{40i}{9}\big(\bar\chi\gamma^{cd}\gamma^{[ab]}\chi\big)\,T_{cd}\\
&=-\frac{160i}{9}\big(\bar\chi\gamma^{[a|c|}\chi\big)\,T_{|c|}{}^{b]}
\end{aligned}\tag{G352}
```

#### Block 4

The original spinor term is $`8i\gamma_c\mathcal D^c\widehat R_{ab}{}^i(Q)T^{ab}`$.

**G353: T1, scalar coefficient.**

```math
\begin{aligned}
&\frac{1}{2}\big(\bar\chi\gamma^{cd}\gamma^{e}\mathcal D_{e}\widehat R(Q)_{cd}\big)\\
&=0
\end{aligned}\tag{G353}
```

**G354: T1, vector coefficient.**

```math
\begin{aligned}
&\frac{1}{2}\big(\bar\chi\gamma^{cd}\gamma^{a}\gamma^{e}\mathcal D_{e}\widehat R(Q)_{cd}\big)\\
&=4\big(\bar\chi\mathcal D_{c}\widehat R(Q)^{ca}\big)
\end{aligned}\tag{G354}
```

**G355: T1, bivector coefficient.**

```math
\begin{aligned}
&-\frac{1}{4}\big(\bar\chi\gamma^{cd}\gamma^{[ab]}\gamma^{e}\mathcal D_{e}\widehat R(Q)_{cd}\big)\\
&=-4\big(\bar\chi\gamma^{[a}\mathcal D_{|c|}\widehat R(Q)^{|c|b]}\big)\\
&+2\big(\bar\chi\gamma^{c}\mathcal D_{c}\widehat R(Q)^{[ab]}\big)
\end{aligned}\tag{G355}
```

**G356: T2, scalar coefficient.**

```math
\begin{aligned}
&\frac{3}{32}\big(\overline{\widehat R(Q)_{de}}\gamma^{c}\mathcal D_{c}\widehat R(Q)^{de}\big)\\
&=\frac{3}{32}\big(\overline{\widehat R(Q)_{de}}\gamma^{c}\mathcal D_{c}\widehat R(Q)^{de}\big)
\end{aligned}\tag{G356}
```

**G357: T2, vector coefficient.**

```math
\begin{aligned}
&\frac{3}{32}\big(\overline{\widehat R(Q)_{de}}\gamma^{a}\gamma^{c}\mathcal D_{c}\widehat R(Q)^{de}\big)\\
&=-\frac{3}{32}\big(\overline{\widehat R(Q)_{de}}\gamma^{ca}\mathcal D_{c}\widehat R(Q)^{de}\big)\\
&+\frac{3}{32}\big(\overline{\widehat R(Q)_{cd}}\mathcal D^{a}\widehat R(Q)^{cd}\big)
\end{aligned}\tag{G357}
```

**G358: T2, bivector coefficient.**

```math
\begin{aligned}
&-\frac{3}{64}\big(\overline{\widehat R(Q)_{de}}\gamma^{[ab]}\gamma^{c}\mathcal D_{c}\widehat R(Q)^{de}\big)\\
&=-\frac{3}{64}\big(\overline{\widehat R(Q)_{de}}\gamma^{c[ab]}\mathcal D_{c}\widehat R(Q)^{de}\big)\\
&-\frac{3}{32}\big(\overline{\widehat R(Q)_{cd}}\gamma^{[a}\mathcal D^{b]}\widehat R(Q)^{cd}\big)\\
&=\frac{3i}{128}\big(\overline{\widehat R(Q)_{fg}}\gamma^{cd}\mathcal D_{e}\widehat R(Q)^{fg}\big)\,\varepsilon_{cd}{}^{e[ab]}\\
&-\frac{3}{32}\big(\overline{\widehat R(Q)_{cd}}\gamma^{[a}\mathcal D^{b]}\widehat R(Q)^{cd}\big)
\end{aligned}\tag{G358}
```

**G359: 4:bos:1, whole coefficient matrix.**

```math
\begin{aligned}
&2iT_{cd}\,(\mathcal D_{e}\widehat C^{cd}{}_{fg})\,\gamma^{e}\gamma^{fg}\\
&=2i(\mathcal D_{c}\widehat C_{defg})\,T^{de}\,\gamma^{cfg}\\
&+4i(\mathcal D_{c}\widehat C_{de}{}^{c}{}_{f})\,T^{de}\,\gamma^{f}\\
&=(\mathcal D_{c}\widehat C_{defg})\,\varepsilon^{cfg}{}_{hj}\,T^{de}\,\gamma^{hj}\\
&+4i(\mathcal D_{c}\widehat C_{de}{}^{c}{}_{f})\,T^{de}\,\gamma^{f}
\end{aligned}\tag{G359}
```

**G360: 4:bos:2, whole coefficient matrix.**

```math
\begin{aligned}
&-8T_{cd}\,(\mathcal D_{e}\mathcal D^{c}T_{fg})\,\gamma^{e}\gamma^{fg}\gamma^{d}\\
&+8T_{cd}\,(\mathcal D_{e}\mathcal D^{d}T_{fg})\,\gamma^{e}\gamma^{fg}\gamma^{c}\\
&=-16T_{cd}\,(\mathcal D_{e}\mathcal D^{d}T_{fg})\,\gamma^{cefg}\\
&+16T_{cd}\,(\mathcal D^{c}\mathcal D^{d}T_{ef})\,\gamma^{ef}\\
&-32T_{cd}\,(\mathcal D_{e}\mathcal D^{c}T_{f}{}^{d})\,\gamma^{ef}\\
&+32T_{cd}\,(\mathcal D_{e}\mathcal D^{d}T_{f}{}^{e})\,\gamma^{cf}\\
&+32T_{cd}\,(\mathcal D_{e}\mathcal D^{c}T^{de})\\
&=-16i\varepsilon_{cdefg}\,T^{d}{}_{h}\,(\mathcal D^{e}\mathcal D^{h}T^{fg})\,\gamma^{c}\\
&+16T_{cd}\,(\mathcal D^{c}\mathcal D^{d}T_{ef})\,\gamma^{ef}\\
&-32T_{cd}\,(\mathcal D_{e}\mathcal D^{c}T_{f}{}^{d})\,\gamma^{ef}\\
&+32T_{cd}\,(\mathcal D_{e}\mathcal D^{d}T_{f}{}^{e})\,\gamma^{cf}\\
&+32T_{cd}\,(\mathcal D_{e}\mathcal D^{c}T^{de})
\end{aligned}\tag{G360}
```

**G361: 4:bos:3, whole coefficient matrix.**

```math
\begin{aligned}
&\frac{8}{3}T_{cd}\,(\mathcal D_{e}\mathcal D^{c}T_{fg})\,\gamma^{e}\gamma^{d}\gamma^{fg}\\
&-\frac{8}{3}T_{cd}\,(\mathcal D_{e}\mathcal D^{d}T_{fg})\,\gamma^{e}\gamma^{c}\gamma^{fg}\\
&=\frac{16}{3}T_{cd}\,(\mathcal D_{e}\mathcal D^{d}T_{fg})\,\gamma^{cefg}\\
&-\frac{32}{3}T_{cd}\,(\mathcal D_{e}\mathcal D^{c}T_{f}{}^{d})\,\gamma^{ef}\\
&-\frac{32}{3}T_{cd}\,(\mathcal D_{e}\mathcal D^{d}T_{f}{}^{e})\,\gamma^{cf}\\
&+\frac{32}{3}T_{cd}\,(\mathcal D_{e}\mathcal D^{c}T^{de})\\
&-\frac{16}{3}T_{cd}\,(\mathcal D^{c}\mathcal D^{d}T_{ef})\,\gamma^{ef}\\
&=\frac{16i}{3}\varepsilon_{cdefg}\,T^{d}{}_{h}\,(\mathcal D^{e}\mathcal D^{h}T^{fg})\,\gamma^{c}\\
&-\frac{32}{3}T_{cd}\,(\mathcal D_{e}\mathcal D^{c}T_{f}{}^{d})\,\gamma^{ef}\\
&-\frac{32}{3}T_{cd}\,(\mathcal D_{e}\mathcal D^{d}T_{f}{}^{e})\,\gamma^{cf}\\
&+\frac{32}{3}T_{cd}\,(\mathcal D_{e}\mathcal D^{c}T^{de})\\
&-\frac{16}{3}T_{cd}\,(\mathcal D^{c}\mathcal D^{d}T_{ef})\,\gamma^{ef}
\end{aligned}\tag{G361}
```

**G362: 4:bos:4, whole coefficient matrix.**

```math
\begin{aligned}
&\frac{8}{3}T_{cd}\,(\mathcal D_{e}\mathcal D_{f}T_{gh})\,\gamma^{e}\gamma^{c}\gamma^{f}\gamma^{gh}\gamma^{d}\\
&-\frac{8}{3}T_{cd}\,(\mathcal D_{e}\mathcal D_{f}T_{gh})\,\gamma^{e}\gamma^{d}\gamma^{f}\gamma^{gh}\gamma^{c}\\
&=\frac{32}{3}T_{cd}\,(\mathcal D^{d}\mathcal D_{e}T_{fg})\,\gamma^{cefg}\\
&-\frac{32}{3}T_{cd}\,(\mathcal D_{e}\mathcal D_{f}T^{cd})\,\gamma^{ef}\\
&+\frac{64}{3}T_{cd}\,(\mathcal D_{e}\mathcal D^{c}T_{f}{}^{d})\,\gamma^{ef}\\
&-\frac{32}{3}T_{cd}\,(\mathcal D_{e}\mathcal D_{f}T_{g}{}^{e})\,\gamma^{cdfg}\\
&+\frac{32}{3}T_{cd}\,(\mathcal D_{e}\mathcal D_{f}T_{g}{}^{f})\,\gamma^{cdeg}\\
&-\frac{64}{3}T_{cd}\,(\mathcal D^{d}\mathcal D_{e}T_{f}{}^{e})\,\gamma^{cf}\\
&-\frac{64}{3}T_{cd}\,(\mathcal D_{e}\mathcal D^{c}T^{de})\\
&+\frac{32}{3}T_{cd}\,(\mathcal D_{e}\mathcal D_{f}T^{ef})\,\gamma^{cd}\\
&-\frac{16}{3}T_{cd}\,(\mathcal D_{e}\mathcal D^{e}T_{fg})\,\gamma^{cdfg}\\
&-\frac{32}{3}T_{cd}\,(\mathcal D_{e}\mathcal D^{e}T^{cd})\\
&=\frac{32i}{3}\varepsilon_{cdefg}\,T^{d}{}_{h}\,(\mathcal D^{h}\mathcal D^{e}T^{fg})\,\gamma^{c}\\
&-\frac{32}{3}T_{cd}\,(\mathcal D_{e}\mathcal D_{f}T^{cd})\,\gamma^{ef}\\
&+\frac{64}{3}T_{cd}\,(\mathcal D_{e}\mathcal D^{c}T_{f}{}^{d})\,\gamma^{ef}\\
&-\frac{32i}{3}\varepsilon_{cdefg}\,T^{de}\,(\mathcal D_{h}\mathcal D^{f}T^{gh})\,\gamma^{c}\\
&+\frac{32i}{3}\varepsilon_{cdefg}\,T^{de}\,(\mathcal D^{f}\mathcal D_{h}T^{gh})\,\gamma^{c}\\
&-\frac{64}{3}T_{cd}\,(\mathcal D^{d}\mathcal D_{e}T_{f}{}^{e})\,\gamma^{cf}\\
&-\frac{64}{3}T_{cd}\,(\mathcal D_{e}\mathcal D^{c}T^{de})\\
&+\frac{32}{3}T_{cd}\,(\mathcal D_{e}\mathcal D_{f}T^{ef})\,\gamma^{cd}\\
&-\frac{16i}{3}\varepsilon_{cdefg}\,T^{de}\,(\mathcal D_{h}\mathcal D^{h}T^{fg})\,\gamma^{c}\\
&-\frac{32}{3}T_{cd}\,(\mathcal D_{e}\mathcal D^{e}T^{cd})
\end{aligned}\tag{G362}
```

**G363: 4:bos:5, whole coefficient matrix.**

```math
\begin{aligned}
&\frac{16}{3}T_{cd}\,(\mathcal D_{e}\mathcal D_{f}T^{f}{}_{g})\,\gamma^{e}\gamma^{cd}\gamma^{g}\\
&=-\frac{16}{3}T_{cd}\,(\mathcal D_{e}\mathcal D_{f}T_{g}{}^{f})\,\gamma^{cdeg}\\
&+\frac{32}{3}T_{cd}\,(\mathcal D_{e}\mathcal D_{f}T^{df})\,\gamma^{ce}\\
&-\frac{16}{3}T_{cd}\,(\mathcal D_{e}\mathcal D_{f}T^{ef})\,\gamma^{cd}\\
&+\frac{32}{3}T_{cd}\,(\mathcal D^{d}\mathcal D_{e}T_{f}{}^{e})\,\gamma^{cf}\\
&-\frac{32}{3}T_{cd}\,(\mathcal D^{c}\mathcal D_{e}T^{de})\\
&=-\frac{16i}{3}\varepsilon_{cdefg}\,T^{de}\,(\mathcal D^{f}\mathcal D_{h}T^{gh})\,\gamma^{c}\\
&+\frac{32}{3}T_{cd}\,(\mathcal D_{e}\mathcal D_{f}T^{df})\,\gamma^{ce}\\
&-\frac{16}{3}T_{cd}\,(\mathcal D_{e}\mathcal D_{f}T^{ef})\,\gamma^{cd}\\
&+\frac{32}{3}T_{cd}\,(\mathcal D^{d}\mathcal D_{e}T_{f}{}^{e})\,\gamma^{cf}\\
&-\frac{32}{3}T_{cd}\,(\mathcal D^{c}\mathcal D_{e}T^{de})
\end{aligned}\tag{G363}
```

**G364: 4:bos:6, whole coefficient matrix.**

```math
\begin{aligned}
&2T_{cd}\,\widehat C^{cd}{}_{ef}\,T_{gh}\,\gamma^{j}\gamma^{ef}\gamma^{gh}\gamma_{j}\\
&=-6\widehat C_{cdef}\,T^{cd}\,T_{gh}\,\gamma^{efgh}\\
&+8\widehat C_{cdef}\,T^{cd}\,T^{f}{}_{g}\,\gamma^{eg}\\
&-20\widehat C_{cdef}\,T^{cd}\,T^{ef}\\
&=-6i\widehat C_{cdef}\,\varepsilon^{ef}{}_{ghj}\,T^{cd}\,T^{hj}\,\gamma^{g}\\
&+8\widehat C_{cdef}\,T^{cd}\,T^{f}{}_{g}\,\gamma^{eg}\\
&-20\widehat C_{cdef}\,T^{cd}\,T^{ef}
\end{aligned}\tag{G364}
```

**G365: 4:bos:7, whole coefficient matrix.**

```math
\begin{aligned}
&8iT_{cd}\,(\mathcal D^{c}T_{ef})\,T_{gh}\,\gamma^{j}\gamma^{ef}\gamma^{d}\gamma^{gh}\gamma_{j}\\
&-8iT_{cd}\,(\mathcal D^{d}T_{ef})\,T_{gh}\,\gamma^{j}\gamma^{ef}\gamma^{c}\gamma^{gh}\gamma_{j}\\
&=32iT_{cd}\,T^{d}{}_{e}\,(\mathcal D^{e}T_{fg})\,\gamma^{cfg}\\
&-80iT_{cd}\,T_{ef}\,(\mathcal D^{f}T_{gh})\,\gamma^{cdegh}\\
&-64iT_{cd}\,T_{ef}\,(\mathcal D^{d}T_{g}{}^{f})\,\gamma^{ceg}\\
&+192iT_{cd}\,T^{c}{}_{e}\,(\mathcal D^{d}T_{f}{}^{e})\,\gamma^{f}\\
&-96iT_{cd}\,T_{ef}\,(\mathcal D^{d}T^{ef})\,\gamma^{c}\\
&+32iT_{cd}\,T_{ef}\,(\mathcal D^{e}T_{g}{}^{f})\,\gamma^{cdg}\\
&+192iT_{cd}\,T_{ef}\,(\mathcal D^{e}T^{df})\,\gamma^{c}\\
&=16\varepsilon_{cdefg}\,T^{e}{}_{h}\,T^{h}{}_{j}\,(\mathcal D^{j}T^{fg})\,\gamma^{cd}\\
&-40\varepsilon_{cdefg}\,T^{cd}\,T^{ef}\,(\mathcal D_{h}T^{gh})\\
&-32\varepsilon_{cdefg}\,T^{e}{}_{h}\,T^{f}{}_{j}\,(\mathcal D^{h}T^{gj})\,\gamma^{cd}\\
&+192iT_{cd}\,T^{c}{}_{e}\,(\mathcal D^{d}T_{f}{}^{e})\,\gamma^{f}\\
&-96iT_{cd}\,T_{ef}\,(\mathcal D^{d}T^{ef})\,\gamma^{c}\\
&+16\varepsilon_{cdefg}\,T^{ef}\,T_{hj}\,(\mathcal D^{h}T^{gj})\,\gamma^{cd}\\
&+192iT_{cd}\,T_{ef}\,(\mathcal D^{e}T^{df})\,\gamma^{c}
\end{aligned}\tag{G365}
```

**G366: 4:bos:8, whole coefficient matrix.**

```math
\begin{aligned}
&-\frac{8i}{3}T_{cd}\,(\mathcal D^{c}T_{ef})\,T_{gh}\,\gamma^{j}\gamma^{d}\gamma^{ef}\gamma^{gh}\gamma_{j}\\
&+\frac{8i}{3}T_{cd}\,(\mathcal D^{d}T_{ef})\,T_{gh}\,\gamma^{j}\gamma^{c}\gamma^{ef}\gamma^{gh}\gamma_{j}\\
&=-\frac{32i}{3}T_{cd}\,T^{d}{}_{e}\,(\mathcal D^{e}T_{fg})\,\gamma^{cfg}\\
&+\frac{80i}{3}T_{cd}\,T_{ef}\,(\mathcal D^{f}T_{gh})\,\gamma^{cdegh}\\
&+\frac{64i}{3}T_{cd}\,T_{ef}\,(\mathcal D^{d}T_{g}{}^{f})\,\gamma^{ceg}\\
&-64iT_{cd}\,T^{c}{}_{e}\,(\mathcal D^{d}T_{f}{}^{e})\,\gamma^{f}\\
&+32iT_{cd}\,T_{ef}\,(\mathcal D^{d}T^{ef})\,\gamma^{c}\\
&+\frac{32i}{3}T_{cd}\,T_{ef}\,(\mathcal D^{e}T_{g}{}^{f})\,\gamma^{cdg}\\
&+64iT_{cd}\,T_{ef}\,(\mathcal D^{e}T^{df})\,\gamma^{c}\\
&=-\frac{16}{3}\varepsilon_{cdefg}\,T^{e}{}_{h}\,T^{h}{}_{j}\,(\mathcal D^{j}T^{fg})\,\gamma^{cd}\\
&+\frac{40}{3}\varepsilon_{cdefg}\,T^{cd}\,T^{ef}\,(\mathcal D_{h}T^{gh})\\
&+\frac{32}{3}\varepsilon_{cdefg}\,T^{e}{}_{h}\,T^{f}{}_{j}\,(\mathcal D^{h}T^{gj})\,\gamma^{cd}\\
&-64iT_{cd}\,T^{c}{}_{e}\,(\mathcal D^{d}T_{f}{}^{e})\,\gamma^{f}\\
&+32iT_{cd}\,T_{ef}\,(\mathcal D^{d}T^{ef})\,\gamma^{c}\\
&+\frac{16}{3}\varepsilon_{cdefg}\,T^{ef}\,T_{hj}\,(\mathcal D^{h}T^{gj})\,\gamma^{cd}\\
&+64iT_{cd}\,T_{ef}\,(\mathcal D^{e}T^{df})\,\gamma^{c}
\end{aligned}\tag{G366}
```

**G367: 4:bos:9, whole coefficient matrix.**

```math
\begin{aligned}
&-\frac{8i}{3}T_{cd}\,(\mathcal D_{e}T_{fg})\,T_{hj}\,\gamma^{k}\gamma^{c}\gamma^{e}\gamma^{fg}\gamma^{d}\gamma^{hj}\gamma_{k}\\
&+\frac{8i}{3}T_{cd}\,(\mathcal D_{e}T_{fg})\,T_{hj}\,\gamma^{k}\gamma^{d}\gamma^{e}\gamma^{fg}\gamma^{c}\gamma^{hj}\gamma_{k}\\
&=-\frac{32i}{3}T_{cd}\,T^{cd}\,(\mathcal D_{e}T_{fg})\,\gamma^{efg}\\
&-\frac{256i}{3}T_{cd}\,T_{ef}\,(\mathcal D_{g}T_{h}{}^{f})\,\gamma^{cdegh}\\
&-\frac{128i}{3}T_{cd}\,T^{d}{}_{e}\,(\mathcal D_{f}T_{g}{}^{e})\,\gamma^{cfg}\\
&-\frac{128i}{3}T_{cd}\,T_{ef}\,(\mathcal D^{f}T_{gh})\,\gamma^{cdegh}\\
&-\frac{64i}{3}T_{cd}\,T^{d}{}_{e}\,(\mathcal D^{e}T_{fg})\,\gamma^{cfg}\\
&-128iT_{cd}\,T_{ef}\,(\mathcal D^{e}T^{df})\,\gamma^{c}\\
&+64iT_{cd}\,T_{ef}\,(\mathcal D^{d}T^{ef})\,\gamma^{c}\\
&-\frac{160i}{3}T_{cd}\,T_{ef}\,(\mathcal D_{g}T_{h}{}^{g})\,\gamma^{cdefh}\\
&+\frac{64i}{3}T_{cd}\,T_{ef}\,(\mathcal D_{g}T^{fg})\,\gamma^{cde}\\
&-64iT_{cd}\,T^{cd}\,(\mathcal D_{e}T_{f}{}^{e})\,\gamma^{f}\\
&-128iT_{cd}\,T^{d}{}_{e}\,(\mathcal D_{f}T^{ef})\,\gamma^{c}\\
&=-\frac{16}{3}\varepsilon_{cdefg}\,T_{hj}\,T^{hj}\,(\mathcal D^{e}T^{fg})\,\gamma^{cd}\\
&+\frac{160}{3}\varepsilon_{cdefg}\,T^{cd}\,T^{ef}\,(\mathcal D_{h}T^{gh})\\
&-\frac{64}{3}\varepsilon_{cdefg}\,T^{e}{}_{h}\,T^{h}{}_{j}\,(\mathcal D^{f}T^{gj})\,\gamma^{cd}\\
&-\frac{32}{3}\varepsilon_{cdefg}\,T^{e}{}_{h}\,T^{h}{}_{j}\,(\mathcal D^{j}T^{fg})\,\gamma^{cd}\\
&-128iT_{cd}\,T_{ef}\,(\mathcal D^{e}T^{df})\,\gamma^{c}\\
&+64iT_{cd}\,T_{ef}\,(\mathcal D^{d}T^{ef})\,\gamma^{c}\\
&+\frac{32}{3}\varepsilon_{cdefg}\,T^{ef}\,T^{g}{}_{h}\,(\mathcal D_{j}T^{hj})\,\gamma^{cd}\\
&-64iT_{cd}\,T^{cd}\,(\mathcal D_{e}T_{f}{}^{e})\,\gamma^{f}\\
&-128iT_{cd}\,T^{d}{}_{e}\,(\mathcal D_{f}T^{ef})\,\gamma^{c}
\end{aligned}\tag{G367}
```

**G368: 4:bos:10, whole coefficient matrix.**

```math
\begin{aligned}
&-\frac{16i}{3}T_{cd}\,(\mathcal D_{e}T^{e}{}_{f})\,T_{gh}\,\gamma^{j}\gamma^{cd}\gamma^{f}\gamma^{gh}\gamma_{j}\\
&=\frac{80i}{3}T_{cd}\,T_{ef}\,(\mathcal D_{g}T_{h}{}^{g})\,\gamma^{cdefh}\\
&+32iT_{cd}\,T^{cd}\,(\mathcal D_{e}T_{f}{}^{e})\,\gamma^{f}\\
&+128iT_{cd}\,T^{d}{}_{e}\,(\mathcal D_{f}T^{ef})\,\gamma^{c}\\
&=-\frac{80}{3}\varepsilon_{cdefg}\,T^{cd}\,T^{ef}\,(\mathcal D_{h}T^{gh})\\
&+32iT_{cd}\,T^{cd}\,(\mathcal D_{e}T_{f}{}^{e})\,\gamma^{f}\\
&+128iT_{cd}\,T^{d}{}_{e}\,(\mathcal D_{f}T^{ef})\,\gamma^{c}
\end{aligned}\tag{G368}
```

**G369: 4:bos:11, whole coefficient matrix.**

```math
\begin{aligned}
&\frac{64i}{3}T_{cd}\,T^{cd}\,(\mathcal D_{e}T_{fg})\,\gamma^{h}\gamma^{e}\gamma^{fg}\gamma_{h}\\
&=\frac{64i}{3}T_{cd}\,T^{cd}\,(\mathcal D_{e}T_{fg})\,\gamma^{efg}\\
&+128iT_{cd}\,T^{cd}\,(\mathcal D_{e}T_{f}{}^{e})\,\gamma^{f}\\
&=\frac{32}{3}\varepsilon_{cdefg}\,T_{hj}\,T^{hj}\,(\mathcal D^{e}T^{fg})\,\gamma^{cd}\\
&+128iT_{cd}\,T^{cd}\,(\mathcal D_{e}T_{f}{}^{e})\,\gamma^{f}
\end{aligned}\tag{G369}
```

**G370: 4:bos:12, whole coefficient matrix.**

```math
\begin{aligned}
&-\frac{64i}{3}T_{cd}\,T^{cd}\,(\mathcal D_{e}T_{fg})\,\gamma^{e}\gamma^{fg}\\
&=-\frac{64i}{3}T_{cd}\,T^{cd}\,(\mathcal D_{e}T_{fg})\,\gamma^{efg}\\
&+\frac{128i}{3}T_{cd}\,T^{cd}\,(\mathcal D_{e}T_{f}{}^{e})\,\gamma^{f}\\
&=-\frac{32}{3}\varepsilon_{cdefg}\,T_{hj}\,T^{hj}\,(\mathcal D^{e}T^{fg})\,\gamma^{cd}\\
&+\frac{128i}{3}T_{cd}\,T^{cd}\,(\mathcal D_{e}T_{f}{}^{e})\,\gamma^{f}
\end{aligned}\tag{G370}
```

**G371: 4:bos:13, whole coefficient matrix.**

```math
\begin{aligned}
&\frac{64i}{3}T_{cd}\,T^{cd}\,(\mathcal D_{e}T^{e}{}_{f})\,\gamma^{g}\gamma_{g}\gamma^{f}\\
&=-\frac{320i}{3}T_{cd}\,T^{cd}\,(\mathcal D_{e}T_{f}{}^{e})\,\gamma^{f}
\end{aligned}\tag{G371}
```

**G372: 4:bos:14, whole coefficient matrix.**

```math
\begin{aligned}
&64T_{cd}\,T^{cd}\,T_{ef}\,T_{gh}\,\gamma^{j}\gamma_{j}{}^{efgh}\\
&=64T_{cd}\,T_{ef}\,T_{gh}\,T^{gh}\,\gamma^{cdef}\\
&=64i\varepsilon_{cdefg}\,T^{de}\,T^{fg}\,T_{hj}\,T^{hj}\,\gamma^{c}
\end{aligned}\tag{G372}
```

**G373: 4:bos:15, whole coefficient matrix.**

```math
\begin{aligned}
&-512T_{cd}\,T^{cd}\,T_{ef}\,T_{g}{}^{f}\,\gamma^{g}\gamma^{e}\\
&=-512T_{cd}\,T^{cd}\,T_{ef}\,T^{ef}
\end{aligned}\tag{G373}
```

**G374: 4:bos:16, whole coefficient matrix.**

```math
\begin{aligned}
&128T_{cd}\,T^{cd}\,T_{ef}\,T^{ef}\,\gamma^{g}\gamma_{g}\\
&=640T_{cd}\,T^{cd}\,T_{ef}\,T^{ef}
\end{aligned}\tag{G374}
```

**G375: 4:bos:17, whole coefficient matrix.**

```math
\begin{aligned}
&-\frac{64i}{9}T_{cd}\,T^{c}{}_{e}\,(\mathcal D_{f}T_{gh})\,\gamma^{j}\gamma^{de}\gamma^{f}\gamma^{gh}\gamma_{j}\\
&+\frac{64i}{9}T_{cd}\,T^{d}{}_{e}\,(\mathcal D_{f}T_{gh})\,\gamma^{j}\gamma^{ce}\gamma^{f}\gamma^{gh}\gamma_{j}\\
&=0
\end{aligned}\tag{G375}
```

**G376: 4:bos:18, whole coefficient matrix.**

```math
\begin{aligned}
&\frac{64i}{9}T_{cd}\,T^{c}{}_{e}\,(\mathcal D_{f}T_{gh})\,\gamma^{f}\gamma^{de}\gamma^{gh}\\
&-\frac{64i}{9}T_{cd}\,T^{d}{}_{e}\,(\mathcal D_{f}T_{gh})\,\gamma^{f}\gamma^{ce}\gamma^{gh}\\
&=0
\end{aligned}\tag{G376}
```

**G377: 4:bos:19, whole coefficient matrix.**

```math
\begin{aligned}
&-\frac{64i}{9}T_{cd}\,T^{c}{}_{e}\,(\mathcal D_{f}T^{f}{}_{g})\,\gamma^{h}\gamma^{de}\gamma_{h}\gamma^{g}\\
&+\frac{64i}{9}T_{cd}\,T^{d}{}_{e}\,(\mathcal D_{f}T^{f}{}_{g})\,\gamma^{h}\gamma^{ce}\gamma_{h}\gamma^{g}\\
&=0
\end{aligned}\tag{G377}
```

**G378: 4:bos:20, whole coefficient matrix.**

```math
\begin{aligned}
&-\frac{64}{3}T_{cd}\,T^{c}{}_{e}\,T_{fg}\,T_{hj}\,\gamma^{k}\gamma^{de}\gamma_{k}{}^{fghj}\\
&+\frac{64}{3}T_{cd}\,T^{d}{}_{e}\,T_{fg}\,T_{hj}\,\gamma^{k}\gamma^{ce}\gamma_{k}{}^{fghj}\\
&=0
\end{aligned}\tag{G378}
```

**G379: 4:bos:21, whole coefficient matrix.**

```math
\begin{aligned}
&\frac{512}{3}T_{cd}\,T^{c}{}_{e}\,T_{fg}\,T_{h}{}^{g}\,\gamma^{h}\gamma^{de}\gamma^{f}\\
&-\frac{512}{3}T_{cd}\,T^{d}{}_{e}\,T_{fg}\,T_{h}{}^{g}\,\gamma^{h}\gamma^{ce}\gamma^{f}\\
&=0
\end{aligned}\tag{G379}
```

**G380: 4:bos:22, whole coefficient matrix.**

```math
\begin{aligned}
&-\frac{128}{3}T_{cd}\,T^{c}{}_{e}\,T_{fg}\,T^{fg}\,\gamma^{h}\gamma^{de}\gamma_{h}\\
&+\frac{128}{3}T_{cd}\,T^{d}{}_{e}\,T_{fg}\,T^{fg}\,\gamma^{h}\gamma^{ce}\gamma_{h}\\
&=0
\end{aligned}\tag{G380}
```

**G381: 4:bos:23, whole coefficient matrix.**

```math
\begin{aligned}
&-\frac{32i}{9}T_{cd}\,T_{ef}\,(\mathcal D_{g}T_{hj})\,\gamma^{k}\gamma^{cdef}\gamma^{g}\gamma^{hj}\gamma_{k}\\
&=-\frac{256i}{9}T_{cd}\,T_{ef}\,(\mathcal D^{e}T_{g}{}^{f})\,\gamma^{cdg}\\
&-\frac{640i}{9}T_{cd}\,T_{ef}\,(\mathcal D^{f}T_{gh})\,\gamma^{cdegh}\\
&+\frac{512i}{9}T_{cd}\,T_{ef}\,(\mathcal D^{d}T_{g}{}^{f})\,\gamma^{ceg}\\
&+\frac{512i}{3}T_{cd}\,T_{ef}\,(\mathcal D^{e}T^{df})\,\gamma^{c}\\
&-\frac{256i}{3}T_{cd}\,T_{ef}\,(\mathcal D^{d}T^{ef})\,\gamma^{c}\\
&-\frac{1024i}{9}T_{cd}\,T_{ef}\,(\mathcal D_{g}T_{h}{}^{f})\,\gamma^{cdegh}\\
&+\frac{256i}{9}T_{cd}\,T_{ef}\,(\mathcal D_{g}T^{fg})\,\gamma^{cde}\\
&+\frac{128i}{9}T_{cd}\,T_{ef}\,(\mathcal D_{g}T^{ef})\,\gamma^{cdg}\\
&-\frac{256i}{9}T_{cd}\,T_{ef}\,(\mathcal D_{g}T^{df})\,\gamma^{ceg}\\
&+\frac{256i}{9}T_{cd}\,T_{ef}\,(\mathcal D_{g}T_{h}{}^{g})\,\gamma^{cdefh}\\
&=-\frac{128}{9}\varepsilon_{cdefg}\,T^{ef}\,T_{hj}\,(\mathcal D^{h}T^{gj})\,\gamma^{cd}\\
&-\frac{320}{9}\varepsilon_{cdefg}\,T^{cd}\,T^{ef}\,(\mathcal D_{h}T^{gh})\\
&+\frac{256}{9}\varepsilon_{cdefg}\,T^{e}{}_{h}\,T^{f}{}_{j}\,(\mathcal D^{h}T^{gj})\,\gamma^{cd}\\
&+\frac{512i}{3}T_{cd}\,T_{ef}\,(\mathcal D^{e}T^{df})\,\gamma^{c}\\
&-\frac{256i}{3}T_{cd}\,T_{ef}\,(\mathcal D^{d}T^{ef})\,\gamma^{c}\\
&+\frac{128}{9}\varepsilon_{cdefg}\,T^{ef}\,T^{g}{}_{h}\,(\mathcal D_{j}T^{hj})\,\gamma^{cd}\\
&+\frac{64}{9}\varepsilon_{cdefg}\,T^{ef}\,T_{hj}\,(\mathcal D^{g}T^{hj})\,\gamma^{cd}\\
&-\frac{128}{9}\varepsilon_{cdefg}\,T^{e}{}_{h}\,T^{f}{}_{j}\,(\mathcal D^{g}T^{hj})\,\gamma^{cd}
\end{aligned}\tag{G381}
```

**G382: 4:bos:24, whole coefficient matrix.**

```math
\begin{aligned}
&\frac{32i}{9}T_{cd}\,T_{ef}\,(\mathcal D_{g}T_{hj})\,\gamma^{g}\gamma^{cdef}\gamma^{hj}\\
&=\frac{128i}{9}T_{cd}\,T_{ef}\,(\mathcal D_{g}T_{h}{}^{f})\,\gamma^{cdegh}\\
&-\frac{128i}{9}T_{cd}\,T_{ef}\,(\mathcal D_{g}T^{ef})\,\gamma^{cdg}\\
&-\frac{256i}{9}T_{cd}\,T_{ef}\,(\mathcal D_{g}T^{fg})\,\gamma^{cde}\\
&+\frac{256i}{9}T_{cd}\,T_{ef}\,(\mathcal D_{g}T^{df})\,\gamma^{ceg}\\
&-\frac{32i}{9}T_{cd}\,T_{ef}\,(\mathcal D_{g}T_{h}{}^{g})\,\gamma^{cdefh}\\
&-\frac{128i}{9}T_{cd}\,T_{ef}\,(\mathcal D^{f}T_{gh})\,\gamma^{cdegh}\\
&-\frac{256i}{9}T_{cd}\,T_{ef}\,(\mathcal D^{e}T_{g}{}^{f})\,\gamma^{cdg}\\
&+\frac{512i}{9}T_{cd}\,T_{ef}\,(\mathcal D^{d}T_{g}{}^{f})\,\gamma^{ceg}\\
&-\frac{512i}{9}T_{cd}\,T_{ef}\,(\mathcal D^{e}T^{df})\,\gamma^{c}\\
&+\frac{256i}{9}T_{cd}\,T_{ef}\,(\mathcal D^{d}T^{ef})\,\gamma^{c}\\
&=-\frac{64}{9}\varepsilon_{cdefg}\,T^{cd}\,T^{ef}\,(\mathcal D_{h}T^{gh})\\
&-\frac{64}{9}\varepsilon_{cdefg}\,T^{ef}\,T_{hj}\,(\mathcal D^{g}T^{hj})\,\gamma^{cd}\\
&-\frac{128}{9}\varepsilon_{cdefg}\,T^{ef}\,T^{g}{}_{h}\,(\mathcal D_{j}T^{hj})\,\gamma^{cd}\\
&+\frac{128}{9}\varepsilon_{cdefg}\,T^{e}{}_{h}\,T^{f}{}_{j}\,(\mathcal D^{g}T^{hj})\,\gamma^{cd}\\
&-\frac{128}{9}\varepsilon_{cdefg}\,T^{ef}\,T_{hj}\,(\mathcal D^{h}T^{gj})\,\gamma^{cd}\\
&+\frac{256}{9}\varepsilon_{cdefg}\,T^{e}{}_{h}\,T^{f}{}_{j}\,(\mathcal D^{h}T^{gj})\,\gamma^{cd}\\
&-\frac{512i}{9}T_{cd}\,T_{ef}\,(\mathcal D^{e}T^{df})\,\gamma^{c}\\
&+\frac{256i}{9}T_{cd}\,T_{ef}\,(\mathcal D^{d}T^{ef})\,\gamma^{c}
\end{aligned}\tag{G382}
```

**G383: 4:bos:25, whole coefficient matrix.**

```math
\begin{aligned}
&-\frac{32i}{9}T_{cd}\,T_{ef}\,(\mathcal D_{g}T^{g}{}_{h})\,\gamma^{j}\gamma^{cdef}\gamma_{j}\gamma^{h}\\
&=-\frac{32i}{3}T_{cd}\,T_{ef}\,(\mathcal D_{g}T_{h}{}^{g})\,\gamma^{cdefh}\\
&-\frac{128i}{3}T_{cd}\,T_{ef}\,(\mathcal D_{g}T^{fg})\,\gamma^{cde}\\
&=\frac{32}{3}\varepsilon_{cdefg}\,T^{cd}\,T^{ef}\,(\mathcal D_{h}T^{gh})\\
&-\frac{64}{3}\varepsilon_{cdefg}\,T^{ef}\,T^{g}{}_{h}\,(\mathcal D_{j}T^{hj})\,\gamma^{cd}
\end{aligned}\tag{G383}
```

**G384: 4:bos:26, whole coefficient matrix.**

```math
\begin{aligned}
&-\frac{32}{3}T_{cd}\,T_{ef}\,T_{gh}\,T_{jk}\,\gamma^{l}\gamma^{cdef}\gamma_{l}{}^{ghjk}\\
&=\frac{11776}{15}T_{cd}\,T_{ef}\,T_{gh}\,T^{fh}\,\gamma^{cdeg}\\
&-\frac{2944}{15}T_{cd}\,T_{ef}\,T_{gh}\,T^{gh}\,\gamma^{cdef}\\
&-\frac{256}{3}T_{cd}\,T^{cd}\,T_{ef}\,T^{ef}\\
&+\frac{512}{3}T_{cd}\,T^{c}{}_{e}\,T^{d}{}_{f}\,T^{ef}\\
&=-\frac{256}{3}T_{cd}\,T^{cd}\,T_{ef}\,T^{ef}\\
&+\frac{512}{3}T_{cd}\,T^{c}{}_{e}\,T^{d}{}_{f}\,T^{ef}
\end{aligned}\tag{G384}
```

**G385: 4:bos:27, whole coefficient matrix.**

```math
\begin{aligned}
&\frac{256}{3}T_{cd}\,T_{ef}\,T_{gh}\,T_{j}{}^{h}\,\gamma^{j}\gamma^{cdef}\gamma^{g}\\
&=-\frac{2048}{3}T_{cd}\,T_{ef}\,T_{gh}\,T^{fh}\,\gamma^{cdeg}\\
&+\frac{256}{3}T_{cd}\,T_{ef}\,T_{gh}\,T^{gh}\,\gamma^{cdef}\\
&=-\frac{256i}{3}\varepsilon_{cdefg}\,T^{de}\,T^{fg}\,T_{hj}\,T^{hj}\,\gamma^{c}
\end{aligned}\tag{G385}
```

**G386: 4:bos:28, whole coefficient matrix.**

```math
\begin{aligned}
&-\frac{64}{3}T_{cd}\,T_{ef}\,T_{gh}\,T^{gh}\,\gamma^{j}\gamma^{cdef}\gamma_{j}\\
&=64T_{cd}\,T_{ef}\,T_{gh}\,T^{gh}\,\gamma^{cdef}\\
&=64i\varepsilon_{cdefg}\,T^{de}\,T^{fg}\,T_{hj}\,T^{hj}\,\gamma^{c}
\end{aligned}\tag{G386}
```

**G387: 4:connection:1, scalar coefficient.**

```math
\begin{aligned}
&3i\big(\bar\chi\gamma^{e}\gamma_{e}\widehat R(Q)_{cd}\big)\,T^{cd}\\
&=-15i\big(\overline{\widehat R(Q)_{cd}}\chi\big)\,T^{cd}
\end{aligned}\tag{G387}
```

**G388: 4:connection:1, vector coefficient.**

```math
\begin{aligned}
&3i\big(\bar\chi\gamma^{e}\gamma^{a}\gamma_{e}\widehat R(Q)_{cd}\big)\,T^{cd}\\
&=9i\big(\overline{\widehat R(Q)_{cd}}\gamma^{a}\chi\big)\,T^{cd}
\end{aligned}\tag{G388}
```

**G389: 4:connection:1, bivector coefficient.**

```math
\begin{aligned}
&-\frac{3i}{2}\big(\bar\chi\gamma^{e}\gamma^{[ab]}\gamma_{e}\widehat R(Q)_{cd}\big)\,T^{cd}\\
&=-\frac{3i}{2}\big(\overline{\widehat R(Q)_{cd}}\gamma^{[ab]}\chi\big)\,T^{cd}
\end{aligned}\tag{G389}
```

**G390: 4:connection:2, scalar coefficient.**

```math
\begin{aligned}
&-\frac{i}{16}\big(\overline{\widehat R(Q)_{fg}}\gamma^{e}\gamma^{f}\gamma_{e}{}^{g}\widehat R(Q)_{cd}\big)\,T^{cd}\\
&=0
\end{aligned}\tag{G390}
```

**G391: 4:connection:2, vector coefficient.**

```math
\begin{aligned}
&-\frac{i}{16}\big(\overline{\widehat R(Q)_{fg}}\gamma^{e}\gamma^{a}\gamma^{f}\gamma_{e}{}^{g}\widehat R(Q)_{cd}\big)\,T^{cd}\\
&=0
\end{aligned}\tag{G391}
```

**G392: 4:connection:2, bivector coefficient.**

```math
\begin{aligned}
&\frac{i}{32}\big(\overline{\widehat R(Q)_{fg}}\gamma^{e}\gamma^{[ab]}\gamma^{f}\gamma_{e}{}^{g}\widehat R(Q)_{cd}\big)\,T^{cd}\\
&=\frac{i}{4}\big(\overline{\widehat R(Q)^{[ab]}}\widehat R(Q)_{cd}\big)\,T^{cd}
\end{aligned}\tag{G392}
```

**G393: 4:connection:2, scalar coefficient.**

```math
\begin{aligned}
&\frac{i}{16}\big(\overline{\widehat R(Q)_{fg}}\gamma^{e}\gamma^{f}\gamma^{g}{}_{e}\widehat R(Q)_{cd}\big)\,T^{cd}\\
&=0
\end{aligned}\tag{G393}
```

**G394: 4:connection:2, vector coefficient.**

```math
\begin{aligned}
&\frac{i}{16}\big(\overline{\widehat R(Q)_{fg}}\gamma^{e}\gamma^{a}\gamma^{f}\gamma^{g}{}_{e}\widehat R(Q)_{cd}\big)\,T^{cd}\\
&=0
\end{aligned}\tag{G394}
```

**G395: 4:connection:2, bivector coefficient.**

```math
\begin{aligned}
&-\frac{i}{32}\big(\overline{\widehat R(Q)_{fg}}\gamma^{e}\gamma^{[ab]}\gamma^{f}\gamma^{g}{}_{e}\widehat R(Q)_{cd}\big)\,T^{cd}\\
&=\frac{i}{4}\big(\overline{\widehat R(Q)^{[ab]}}\widehat R(Q)_{cd}\big)\,T^{cd}
\end{aligned}\tag{G395}
```

**G396: 4:connection:3, scalar coefficient.**

```math
\begin{aligned}
&-\frac{i}{16}\big(\overline{\widehat R(Q)_{fg}}\gamma^{e}\gamma_{e}\gamma^{fg}\widehat R(Q)_{cd}\big)\,T^{cd}\\
&=0
\end{aligned}\tag{G396}
```

**G397: 4:connection:3, vector coefficient.**

```math
\begin{aligned}
&-\frac{i}{16}\big(\overline{\widehat R(Q)_{fg}}\gamma^{e}\gamma^{a}\gamma_{e}\gamma^{fg}\widehat R(Q)_{cd}\big)\,T^{cd}\\
&=0
\end{aligned}\tag{G397}
```

**G398: 4:connection:3, bivector coefficient.**

```math
\begin{aligned}
&\frac{i}{32}\big(\overline{\widehat R(Q)_{fg}}\gamma^{e}\gamma^{[ab]}\gamma_{e}\gamma^{fg}\widehat R(Q)_{cd}\big)\,T^{cd}\\
&=-\frac{i}{4}\big(\overline{\widehat R(Q)^{[ab]}}\widehat R(Q)_{cd}\big)\,T^{cd}
\end{aligned}\tag{G398}
```

**G399: 4:connection:4, scalar coefficient.**

```math
\begin{aligned}
&-\frac{i}{2}\big(\bar\chi\gamma^{g}\gamma^{c}\gamma^{d}{}_{g}\widehat R(Q)_{ef}\big)\,\eta_{cd}\,T^{ef}\\
&=10i\big(\overline{\widehat R(Q)_{cd}}\chi\big)\,T^{cd}
\end{aligned}\tag{G399}
```

**G400: 4:connection:4, vector coefficient.**

```math
\begin{aligned}
&-\frac{i}{2}\big(\bar\chi\gamma^{g}\gamma^{a}\gamma^{c}\gamma^{d}{}_{g}\widehat R(Q)_{ef}\big)\,\eta_{cd}\,T^{ef}\\
&=-6i\big(\overline{\widehat R(Q)_{cd}}\gamma^{a}\chi\big)\,T^{cd}
\end{aligned}\tag{G400}
```

**G401: 4:connection:4, bivector coefficient.**

```math
\begin{aligned}
&\frac{i}{4}\big(\bar\chi\gamma^{g}\gamma^{[ab]}\gamma^{c}\gamma^{d}{}_{g}\widehat R(Q)_{ef}\big)\,\eta_{cd}\,T^{ef}\\
&=i\big(\overline{\widehat R(Q)_{cd}}\gamma^{[ab]}\chi\big)\,T^{cd}
\end{aligned}\tag{G401}
```

**G402: 4:connection:4, scalar coefficient.**

```math
\begin{aligned}
&\frac{i}{2}\big(\bar\chi\gamma^{g}\gamma^{c}\gamma_{g}{}^{d}\widehat R(Q)_{ef}\big)\,\eta_{cd}\,T^{ef}\\
&=10i\big(\overline{\widehat R(Q)_{cd}}\chi\big)\,T^{cd}
\end{aligned}\tag{G402}
```

**G403: 4:connection:4, vector coefficient.**

```math
\begin{aligned}
&\frac{i}{2}\big(\bar\chi\gamma^{g}\gamma^{a}\gamma^{c}\gamma_{g}{}^{d}\widehat R(Q)_{ef}\big)\,\eta_{cd}\,T^{ef}\\
&=-6i\big(\overline{\widehat R(Q)_{cd}}\gamma^{a}\chi\big)\,T^{cd}
\end{aligned}\tag{G403}
```

**G404: 4:connection:4, bivector coefficient.**

```math
\begin{aligned}
&-\frac{i}{4}\big(\bar\chi\gamma^{g}\gamma^{[ab]}\gamma^{c}\gamma_{g}{}^{d}\widehat R(Q)_{ef}\big)\,\eta_{cd}\,T^{ef}\\
&=i\big(\overline{\widehat R(Q)_{cd}}\gamma^{[ab]}\chi\big)\,T^{cd}
\end{aligned}\tag{G404}
```

**G405: 4:connection:5, scalar coefficient.**

```math
\begin{aligned}
&6i\big(\bar\chi\gamma^{e}\gamma_{e}\widehat R(Q)_{cd}\big)\,T^{cd}\\
&=-30i\big(\overline{\widehat R(Q)_{cd}}\chi\big)\,T^{cd}
\end{aligned}\tag{G405}
```

**G406: 4:connection:5, vector coefficient.**

```math
\begin{aligned}
&6i\big(\bar\chi\gamma^{e}\gamma^{a}\gamma_{e}\widehat R(Q)_{cd}\big)\,T^{cd}\\
&=18i\big(\overline{\widehat R(Q)_{cd}}\gamma^{a}\chi\big)\,T^{cd}
\end{aligned}\tag{G406}
```

**G407: 4:connection:5, bivector coefficient.**

```math
\begin{aligned}
&-3i\big(\bar\chi\gamma^{e}\gamma^{[ab]}\gamma_{e}\widehat R(Q)_{cd}\big)\,T^{cd}\\
&=-3i\big(\overline{\widehat R(Q)_{cd}}\gamma^{[ab]}\chi\big)\,T^{cd}
\end{aligned}\tag{G407}
```

**G408: 4:connection:6, scalar coefficient.**

```math
\begin{aligned}
&-\frac{i}{4}\big(\overline{\widehat R(Q)_{ef}}\gamma^{c}\gamma^{e}\widehat R(Q)^{f}{}_{d}\big)\,T_{c}{}^{d}\\
&=\frac{i}{2}\big(\overline{\widehat R(Q)_{ec}}\widehat R(Q)^{e}{}_{d}\big)\,T^{cd}
\end{aligned}\tag{G408}
```

**G409: 4:connection:6, vector coefficient.**

```math
\begin{aligned}
&-\frac{i}{4}\big(\overline{\widehat R(Q)_{ef}}\gamma^{c}\gamma^{a}\gamma^{e}\widehat R(Q)^{f}{}_{d}\big)\,T_{c}{}^{d}\\
&=-\frac{i}{2}\big(\overline{\widehat R(Q)_{ec}}\gamma^{a}\widehat R(Q)^{e}{}_{d}\big)\,T^{cd}\\
&+\frac{i}{2}\big(\overline{\widehat R(Q)_{e}{}^{a}}\gamma^{c}\widehat R(Q)^{e}{}_{d}\big)\,T_{c}{}^{d}
\end{aligned}\tag{G409}
```

**G410: 4:connection:6, bivector coefficient.**

```math
\begin{aligned}
&\frac{i}{8}\big(\overline{\widehat R(Q)_{ef}}\gamma^{c}\gamma^{[ab]}\gamma^{e}\widehat R(Q)^{f}{}_{d}\big)\,T_{c}{}^{d}\\
&=-\frac{i}{2}\big(\overline{\widehat R(Q)_{e}{}^{[a}}\gamma^{b]c}\widehat R(Q)^{e}{}_{d}\big)\,T_{c}{}^{d}\\
&-\frac{i}{2}\big(\overline{\widehat R(Q)_{d}{}^{[a}}\widehat R(Q)^{|d|}{}_{|c|}\big)\,T^{|c|b]}
\end{aligned}\tag{G410}
```

**G411: 4:connection:6, scalar coefficient.**

```math
\begin{aligned}
&\frac{i}{4}\big(\overline{\widehat R(Q)_{fc}}\gamma^{e}\gamma^{f}\widehat R(Q)_{ed}\big)\,T^{cd}\\
&=\frac{i}{2}\big(\overline{\widehat R(Q)_{ec}}\widehat R(Q)^{e}{}_{d}\big)\,T^{cd}
\end{aligned}\tag{G411}
```

**G412: 4:connection:6, vector coefficient.**

```math
\begin{aligned}
&\frac{i}{4}\big(\overline{\widehat R(Q)_{fc}}\gamma^{e}\gamma^{a}\gamma^{f}\widehat R(Q)_{ed}\big)\,T^{cd}\\
&=-\frac{i}{2}\big(\overline{\widehat R(Q)_{ec}}\gamma^{a}\widehat R(Q)^{e}{}_{d}\big)\,T^{cd}
\end{aligned}\tag{G412}
```

**G413: 4:connection:6, bivector coefficient.**

```math
\begin{aligned}
&-\frac{i}{8}\big(\overline{\widehat R(Q)_{fc}}\gamma^{e}\gamma^{[ab]}\gamma^{f}\widehat R(Q)_{ed}\big)\,T^{cd}\\
&=0
\end{aligned}\tag{G413}
```

**G414: 4:connection:7, scalar coefficient.**

```math
\begin{aligned}
&-\frac{i}{4}\big(\overline{\widehat R(Q)_{cf}}\gamma^{e}\gamma_{e}\widehat R(Q)^{f}{}_{d}\big)\,T^{cd}\\
&=\frac{5i}{4}\big(\overline{\widehat R(Q)_{ec}}\widehat R(Q)^{e}{}_{d}\big)\,T^{cd}
\end{aligned}\tag{G414}
```

**G415: 4:connection:7, vector coefficient.**

```math
\begin{aligned}
&-\frac{i}{4}\big(\overline{\widehat R(Q)_{cf}}\gamma^{e}\gamma^{a}\gamma_{e}\widehat R(Q)^{f}{}_{d}\big)\,T^{cd}\\
&=-\frac{3i}{4}\big(\overline{\widehat R(Q)_{ec}}\gamma^{a}\widehat R(Q)^{e}{}_{d}\big)\,T^{cd}
\end{aligned}\tag{G415}
```

**G416: 4:connection:7, bivector coefficient.**

```math
\begin{aligned}
&\frac{i}{8}\big(\overline{\widehat R(Q)_{cf}}\gamma^{e}\gamma^{[ab]}\gamma_{e}\widehat R(Q)^{f}{}_{d}\big)\,T^{cd}\\
&=0
\end{aligned}\tag{G416}
```

**G417: 4:connection:8, scalar coefficient.**

```math
\begin{aligned}
&-2i\big(\bar\chi\gamma^{f}\gamma^{c}\widehat R(Q)_{fe}\big)\,\eta_{cd}\,T^{de}\\
&=4i\big(\overline{\widehat R(Q)_{cd}}\chi\big)\,T^{cd}
\end{aligned}\tag{G417}
```

**G418: 4:connection:8, vector coefficient.**

```math
\begin{aligned}
&-2i\big(\bar\chi\gamma^{f}\gamma^{a}\gamma^{c}\widehat R(Q)_{fe}\big)\,\eta_{cd}\,T^{de}\\
&=-4i\big(\overline{\widehat R(Q)_{cd}}\gamma^{a}\chi\big)\,T^{cd}\\
&-4i\big(\overline{\widehat R(Q)^{a}{}_{c}}\gamma^{d}\chi\big)\,T^{c}{}_{d}
\end{aligned}\tag{G418}
```

**G419: 4:connection:8, bivector coefficient.**

```math
\begin{aligned}
&i\big(\bar\chi\gamma^{f}\gamma^{[ab]}\gamma^{c}\widehat R(Q)_{fe}\big)\,\eta_{cd}\,T^{de}\\
&=2i\big(\overline{\widehat R(Q)_{cd}}\gamma^{[ab]}\chi\big)\,T^{cd}\\
&-4i\big(\overline{\widehat R(Q)^{[a}{}_{|c|}}\gamma^{b]d}\chi\big)\,T^{c}{}_{d}\\
&+4i\big(\overline{\widehat R(Q)^{[a}{}_{|c|}}\chi\big)\,T^{|c|b]}
\end{aligned}\tag{G419}
```

**G420: 4:connection:8, scalar coefficient.**

```math
\begin{aligned}
&2i\big(\bar\chi\gamma^{e}\gamma^{c}\widehat R(Q)_{df}\big)\,\eta_{c}{}^{d}\,T_{e}{}^{f}\\
&=0
\end{aligned}\tag{G420}
```

**G421: 4:connection:8, vector coefficient.**

```math
\begin{aligned}
&2i\big(\bar\chi\gamma^{e}\gamma^{a}\gamma^{c}\widehat R(Q)_{df}\big)\,\eta_{c}{}^{d}\,T_{e}{}^{f}\\
&=0
\end{aligned}\tag{G421}
```

**G422: 4:connection:8, bivector coefficient.**

```math
\begin{aligned}
&-i\big(\bar\chi\gamma^{e}\gamma^{[ab]}\gamma^{c}\widehat R(Q)_{df}\big)\,\eta_{c}{}^{d}\,T_{e}{}^{f}\\
&=0
\end{aligned}\tag{G422}
```

**G423: 4:connection:9, scalar coefficient.**

```math
\begin{aligned}
&-\frac{i}{4}\big(\overline{\widehat R(Q)_{ef}}\gamma^{d}\gamma^{e}\widehat R(Q)_{c}{}^{f}\big)\,T^{c}{}_{d}\\
&=\frac{i}{2}\big(\overline{\widehat R(Q)_{ec}}\widehat R(Q)^{e}{}_{d}\big)\,T^{cd}
\end{aligned}\tag{G423}
```

**G424: 4:connection:9, vector coefficient.**

```math
\begin{aligned}
&-\frac{i}{4}\big(\overline{\widehat R(Q)_{ef}}\gamma^{d}\gamma^{a}\gamma^{e}\widehat R(Q)_{c}{}^{f}\big)\,T^{c}{}_{d}\\
&=-\frac{i}{2}\big(\overline{\widehat R(Q)_{ec}}\gamma^{a}\widehat R(Q)^{e}{}_{d}\big)\,T^{cd}\\
&+\frac{i}{2}\big(\overline{\widehat R(Q)_{e}{}^{a}}\gamma^{c}\widehat R(Q)^{e}{}_{d}\big)\,T_{c}{}^{d}
\end{aligned}\tag{G424}
```

**G425: 4:connection:9, bivector coefficient.**

```math
\begin{aligned}
&\frac{i}{8}\big(\overline{\widehat R(Q)_{ef}}\gamma^{d}\gamma^{[ab]}\gamma^{e}\widehat R(Q)_{c}{}^{f}\big)\,T^{c}{}_{d}\\
&=-\frac{i}{2}\big(\overline{\widehat R(Q)_{e}{}^{[a}}\gamma^{b]c}\widehat R(Q)^{e}{}_{d}\big)\,T_{c}{}^{d}\\
&-\frac{i}{2}\big(\overline{\widehat R(Q)_{d}{}^{[a}}\widehat R(Q)^{|d|}{}_{|c|}\big)\,T^{|c|b]}
\end{aligned}\tag{G425}
```

**G426: 4:connection:9, scalar coefficient.**

```math
\begin{aligned}
&\frac{i}{4}\big(\overline{\widehat R(Q)_{fd}}\gamma^{e}\gamma^{f}\widehat R(Q)_{ce}\big)\,T^{cd}\\
&=\frac{i}{2}\big(\overline{\widehat R(Q)_{ec}}\widehat R(Q)^{e}{}_{d}\big)\,T^{cd}
\end{aligned}\tag{G426}
```

**G427: 4:connection:9, vector coefficient.**

```math
\begin{aligned}
&\frac{i}{4}\big(\overline{\widehat R(Q)_{fd}}\gamma^{e}\gamma^{a}\gamma^{f}\widehat R(Q)_{ce}\big)\,T^{cd}\\
&=-\frac{i}{2}\big(\overline{\widehat R(Q)_{ec}}\gamma^{a}\widehat R(Q)^{e}{}_{d}\big)\,T^{cd}
\end{aligned}\tag{G427}
```

**G428: 4:connection:9, bivector coefficient.**

```math
\begin{aligned}
&-\frac{i}{8}\big(\overline{\widehat R(Q)_{fd}}\gamma^{e}\gamma^{[ab]}\gamma^{f}\widehat R(Q)_{ce}\big)\,T^{cd}\\
&=0
\end{aligned}\tag{G428}
```

**G429: 4:connection:10, scalar coefficient.**

```math
\begin{aligned}
&-\frac{i}{4}\big(\overline{\widehat R(Q)_{df}}\gamma^{e}\gamma_{e}\widehat R(Q)_{c}{}^{f}\big)\,T^{cd}\\
&=\frac{5i}{4}\big(\overline{\widehat R(Q)_{ec}}\widehat R(Q)^{e}{}_{d}\big)\,T^{cd}
\end{aligned}\tag{G429}
```

**G430: 4:connection:10, vector coefficient.**

```math
\begin{aligned}
&-\frac{i}{4}\big(\overline{\widehat R(Q)_{df}}\gamma^{e}\gamma^{a}\gamma_{e}\widehat R(Q)_{c}{}^{f}\big)\,T^{cd}\\
&=-\frac{3i}{4}\big(\overline{\widehat R(Q)_{ec}}\gamma^{a}\widehat R(Q)^{e}{}_{d}\big)\,T^{cd}
\end{aligned}\tag{G430}
```

**G431: 4:connection:10, bivector coefficient.**

```math
\begin{aligned}
&\frac{i}{8}\big(\overline{\widehat R(Q)_{df}}\gamma^{e}\gamma^{[ab]}\gamma_{e}\widehat R(Q)_{c}{}^{f}\big)\,T^{cd}\\
&=0
\end{aligned}\tag{G431}
```

**G432: 4:connection:11, scalar coefficient.**

```math
\begin{aligned}
&-2i\big(\bar\chi\gamma^{f}\gamma^{c}\widehat R(Q)_{ef}\big)\,\eta_{cd}\,T^{ed}\\
&=4i\big(\overline{\widehat R(Q)_{cd}}\chi\big)\,T^{cd}
\end{aligned}\tag{G432}
```

**G433: 4:connection:11, vector coefficient.**

```math
\begin{aligned}
&-2i\big(\bar\chi\gamma^{f}\gamma^{a}\gamma^{c}\widehat R(Q)_{ef}\big)\,\eta_{cd}\,T^{ed}\\
&=-4i\big(\overline{\widehat R(Q)_{cd}}\gamma^{a}\chi\big)\,T^{cd}\\
&-4i\big(\overline{\widehat R(Q)^{a}{}_{c}}\gamma^{d}\chi\big)\,T^{c}{}_{d}
\end{aligned}\tag{G433}
```

**G434: 4:connection:11, bivector coefficient.**

```math
\begin{aligned}
&i\big(\bar\chi\gamma^{f}\gamma^{[ab]}\gamma^{c}\widehat R(Q)_{ef}\big)\,\eta_{cd}\,T^{ed}\\
&=2i\big(\overline{\widehat R(Q)_{cd}}\gamma^{[ab]}\chi\big)\,T^{cd}\\
&-4i\big(\overline{\widehat R(Q)^{[a}{}_{|c|}}\gamma^{b]d}\chi\big)\,T^{c}{}_{d}\\
&+4i\big(\overline{\widehat R(Q)^{[a}{}_{|c|}}\chi\big)\,T^{|c|b]}
\end{aligned}\tag{G434}
```

**G435: 4:connection:11, scalar coefficient.**

```math
\begin{aligned}
&2i\big(\bar\chi\gamma^{f}\gamma^{c}\widehat R(Q)_{ed}\big)\,\eta_{c}{}^{d}\,T^{e}{}_{f}\\
&=0
\end{aligned}\tag{G435}
```

**G436: 4:connection:11, vector coefficient.**

```math
\begin{aligned}
&2i\big(\bar\chi\gamma^{f}\gamma^{a}\gamma^{c}\widehat R(Q)_{ed}\big)\,\eta_{c}{}^{d}\,T^{e}{}_{f}\\
&=0
\end{aligned}\tag{G436}
```

**G437: 4:connection:11, bivector coefficient.**

```math
\begin{aligned}
&-i\big(\bar\chi\gamma^{f}\gamma^{[ab]}\gamma^{c}\widehat R(Q)_{ed}\big)\,\eta_{c}{}^{d}\,T^{e}{}_{f}\\
&=0
\end{aligned}\tag{G437}
```

#### Block 5

The original spinor term is $`8i\gamma_a\mathcal D^c\widehat R_{bc}{}^i(Q)T^{ab}`$.

**G438: T1, scalar coefficient.**

```math
\begin{aligned}
&\frac{1}{2}\big(\bar\chi\gamma^{cd}\gamma_{c}\mathcal D_{e}\widehat R(Q)_{d}{}^{e}\big)\\
&=0
\end{aligned}\tag{G438}
```

**G439: T1, vector coefficient.**

```math
\begin{aligned}
&\frac{1}{2}\big(\bar\chi\gamma^{cd}\gamma^{a}\gamma_{c}\mathcal D_{e}\widehat R(Q)_{d}{}^{e}\big)\\
&=-3\big(\bar\chi\mathcal D_{c}\widehat R(Q)^{ca}\big)
\end{aligned}\tag{G439}
```

**G440: T1, bivector coefficient.**

```math
\begin{aligned}
&-\frac{1}{4}\big(\bar\chi\gamma^{cd}\gamma^{[ab]}\gamma_{c}\mathcal D_{e}\widehat R(Q)_{d}{}^{e}\big)\\
&=\big(\bar\chi\gamma^{[a}\mathcal D_{|c|}\widehat R(Q)^{|c|b]}\big)
\end{aligned}\tag{G440}
```

**G441: T2, scalar coefficient.**

```math
\begin{aligned}
&\frac{3}{32}\big(\overline{\widehat R(Q)_{cd}}\gamma^{c}\mathcal D_{e}\widehat R(Q)^{de}\big)\\
&=0
\end{aligned}\tag{G441}
```

**G442: T2, vector coefficient.**

```math
\begin{aligned}
&\frac{3}{32}\big(\overline{\widehat R(Q)_{cd}}\gamma^{a}\gamma^{c}\mathcal D_{e}\widehat R(Q)^{de}\big)\\
&=-\frac{3}{16}\big(\overline{\widehat R(Q)_{c}{}^{a}}\mathcal D_{d}\widehat R(Q)^{cd}\big)
\end{aligned}\tag{G442}
```

**G443: T2, bivector coefficient.**

```math
\begin{aligned}
&-\frac{3}{64}\big(\overline{\widehat R(Q)_{cd}}\gamma^{[ab]}\gamma^{c}\mathcal D_{e}\widehat R(Q)^{de}\big)\\
&=-\frac{3}{16}\big(\overline{\widehat R(Q)_{c}{}^{[a}}\gamma^{b]}\mathcal D_{d}\widehat R(Q)^{cd}\big)
\end{aligned}\tag{G443}
```

**G444: 5:bos:1, whole coefficient matrix.**

```math
\begin{aligned}
&2iT_{cd}\,\eta_{ef}\,(\mathcal D^{f}\widehat C^{de}{}_{gh})\,\gamma^{c}\gamma^{gh}\\
&=2i(\mathcal D_{c}\widehat C^{c}{}_{def})\,T^{d}{}_{g}\,\gamma^{efg}\\
&-4i(\mathcal D_{c}\widehat C^{c}{}_{def})\,T^{df}\,\gamma^{e}\\
&=(\mathcal D_{c}\widehat C^{c}{}_{def})\,\varepsilon^{ef}{}_{ghj}\,T^{dj}\,\gamma^{gh}\\
&-4i(\mathcal D_{c}\widehat C^{c}{}_{def})\,T^{df}\,\gamma^{e}
\end{aligned}\tag{G444}
```

**G445: 5:bos:2, whole coefficient matrix.**

```math
\begin{aligned}
&-8T_{cd}\,\eta_{ef}\,(\mathcal D^{f}\mathcal D^{d}T_{gh})\,\gamma^{c}\gamma^{gh}\gamma^{e}\\
&+8T_{cd}\,\eta_{ef}\,(\mathcal D^{f}\mathcal D^{e}T_{gh})\,\gamma^{c}\gamma^{gh}\gamma^{d}\\
&=-8T_{cd}\,(\mathcal D_{e}\mathcal D^{d}T_{fg})\,\gamma^{cefg}\\
&-8T_{cd}\,(\mathcal D^{c}\mathcal D^{d}T_{ef})\,\gamma^{ef}\\
&-16T_{cd}\,(\mathcal D_{e}\mathcal D^{d}T_{f}{}^{e})\,\gamma^{cf}\\
&+16T_{cd}\,(\mathcal D_{e}\mathcal D^{c}T_{f}{}^{d})\,\gamma^{ef}\\
&+16T_{cd}\,(\mathcal D_{e}\mathcal D^{c}T^{de})\\
&+8T_{cd}\,(\mathcal D_{e}\mathcal D^{e}T_{fg})\,\gamma^{cdfg}\\
&+16T_{cd}\,(\mathcal D_{e}\mathcal D^{e}T^{cd})\\
&=-8i\varepsilon_{cdefg}\,T^{d}{}_{h}\,(\mathcal D^{e}\mathcal D^{h}T^{fg})\,\gamma^{c}\\
&-8T_{cd}\,(\mathcal D^{c}\mathcal D^{d}T_{ef})\,\gamma^{ef}\\
&-16T_{cd}\,(\mathcal D_{e}\mathcal D^{d}T_{f}{}^{e})\,\gamma^{cf}\\
&+16T_{cd}\,(\mathcal D_{e}\mathcal D^{c}T_{f}{}^{d})\,\gamma^{ef}\\
&+16T_{cd}\,(\mathcal D_{e}\mathcal D^{c}T^{de})\\
&+8i\varepsilon_{cdefg}\,T^{de}\,(\mathcal D_{h}\mathcal D^{h}T^{fg})\,\gamma^{c}\\
&+16T_{cd}\,(\mathcal D_{e}\mathcal D^{e}T^{cd})
\end{aligned}\tag{G445}
```

**G446: 5:bos:3, whole coefficient matrix.**

```math
\begin{aligned}
&\frac{8}{3}T_{cd}\,\eta_{ef}\,(\mathcal D^{f}\mathcal D^{d}T_{gh})\,\gamma^{c}\gamma^{e}\gamma^{gh}\\
&-\frac{8}{3}T_{cd}\,\eta_{ef}\,(\mathcal D^{f}\mathcal D^{e}T_{gh})\,\gamma^{c}\gamma^{d}\gamma^{gh}\\
&=\frac{8}{3}T_{cd}\,(\mathcal D_{e}\mathcal D^{d}T_{fg})\,\gamma^{cefg}\\
&-\frac{16}{3}T_{cd}\,(\mathcal D_{e}\mathcal D^{c}T_{f}{}^{d})\,\gamma^{ef}\\
&-\frac{16}{3}T_{cd}\,(\mathcal D_{e}\mathcal D^{d}T_{f}{}^{e})\,\gamma^{cf}\\
&+\frac{16}{3}T_{cd}\,(\mathcal D_{e}\mathcal D^{c}T^{de})\\
&+\frac{8}{3}T_{cd}\,(\mathcal D^{c}\mathcal D^{d}T_{ef})\,\gamma^{ef}\\
&-\frac{8}{3}T_{cd}\,(\mathcal D_{e}\mathcal D^{e}T_{fg})\,\gamma^{cdfg}\\
&+\frac{32}{3}T_{cd}\,(\mathcal D_{e}\mathcal D^{e}T_{f}{}^{d})\,\gamma^{cf}\\
&+\frac{16}{3}T_{cd}\,(\mathcal D_{e}\mathcal D^{e}T^{cd})\\
&=\frac{8i}{3}\varepsilon_{cdefg}\,T^{d}{}_{h}\,(\mathcal D^{e}\mathcal D^{h}T^{fg})\,\gamma^{c}\\
&-\frac{16}{3}T_{cd}\,(\mathcal D_{e}\mathcal D^{c}T_{f}{}^{d})\,\gamma^{ef}\\
&-\frac{16}{3}T_{cd}\,(\mathcal D_{e}\mathcal D^{d}T_{f}{}^{e})\,\gamma^{cf}\\
&+\frac{16}{3}T_{cd}\,(\mathcal D_{e}\mathcal D^{c}T^{de})\\
&+\frac{8}{3}T_{cd}\,(\mathcal D^{c}\mathcal D^{d}T_{ef})\,\gamma^{ef}\\
&-\frac{8i}{3}\varepsilon_{cdefg}\,T^{de}\,(\mathcal D_{h}\mathcal D^{h}T^{fg})\,\gamma^{c}\\
&+\frac{32}{3}T_{cd}\,(\mathcal D_{e}\mathcal D^{e}T_{f}{}^{d})\,\gamma^{cf}\\
&+\frac{16}{3}T_{cd}\,(\mathcal D_{e}\mathcal D^{e}T^{cd})
\end{aligned}\tag{G446}
```

**G447: 5:bos:4, whole coefficient matrix.**

```math
\begin{aligned}
&\frac{8}{3}T_{cd}\,\eta_{ef}\,(\mathcal D^{f}\mathcal D_{g}T_{hj})\,\gamma^{c}\gamma^{d}\gamma^{g}\gamma^{hj}\gamma^{e}\\
&-\frac{8}{3}T_{cd}\,\eta_{ef}\,(\mathcal D^{f}\mathcal D_{g}T_{hj})\,\gamma^{c}\gamma^{e}\gamma^{g}\gamma^{hj}\gamma^{d}\\
&=-\frac{16}{3}T_{cd}\,(\mathcal D^{d}\mathcal D_{e}T_{fg})\,\gamma^{cefg}\\
&+\frac{32}{3}T_{cd}\,(\mathcal D_{e}\mathcal D_{f}T_{g}{}^{d})\,\gamma^{cefg}\\
&-\frac{32}{3}T_{cd}\,(\mathcal D_{e}\mathcal D_{f}T^{de})\,\gamma^{cf}\\
&-\frac{32}{3}T_{cd}\,(\mathcal D_{e}\mathcal D^{e}T_{f}{}^{d})\,\gamma^{cf}\\
&+\frac{32}{3}T_{cd}\,(\mathcal D_{e}\mathcal D_{f}T_{g}{}^{f})\,\gamma^{cdeg}\\
&+\frac{32}{3}T_{cd}\,(\mathcal D^{d}\mathcal D_{e}T_{f}{}^{e})\,\gamma^{cf}\\
&-\frac{32}{3}T_{cd}\,(\mathcal D_{e}\mathcal D^{e}T^{cd})\\
&-\frac{32}{3}T_{cd}\,(\mathcal D_{e}\mathcal D_{f}T^{df})\,\gamma^{ce}\\
&+\frac{16}{3}T_{cd}\,(\mathcal D_{e}\mathcal D^{d}T_{fg})\,\gamma^{cefg}\\
&+\frac{32}{3}T_{cd}\,(\mathcal D_{e}\mathcal D^{d}T_{f}{}^{e})\,\gamma^{cf}\\
&-\frac{64}{3}T_{cd}\,(\mathcal D_{e}\mathcal D^{c}T^{de})\\
&=-\frac{16i}{3}\varepsilon_{cdefg}\,T^{d}{}_{h}\,(\mathcal D^{h}\mathcal D^{e}T^{fg})\,\gamma^{c}\\
&+\frac{32i}{3}\varepsilon_{cdefg}\,T^{d}{}_{h}\,(\mathcal D^{e}\mathcal D^{f}T^{gh})\,\gamma^{c}\\
&-\frac{32}{3}T_{cd}\,(\mathcal D_{e}\mathcal D_{f}T^{de})\,\gamma^{cf}\\
&-\frac{32}{3}T_{cd}\,(\mathcal D_{e}\mathcal D^{e}T_{f}{}^{d})\,\gamma^{cf}\\
&+\frac{32i}{3}\varepsilon_{cdefg}\,T^{de}\,(\mathcal D^{f}\mathcal D_{h}T^{gh})\,\gamma^{c}\\
&+\frac{32}{3}T_{cd}\,(\mathcal D^{d}\mathcal D_{e}T_{f}{}^{e})\,\gamma^{cf}\\
&-\frac{32}{3}T_{cd}\,(\mathcal D_{e}\mathcal D^{e}T^{cd})\\
&-\frac{32}{3}T_{cd}\,(\mathcal D_{e}\mathcal D_{f}T^{df})\,\gamma^{ce}\\
&+\frac{16i}{3}\varepsilon_{cdefg}\,T^{d}{}_{h}\,(\mathcal D^{e}\mathcal D^{h}T^{fg})\,\gamma^{c}\\
&+\frac{32}{3}T_{cd}\,(\mathcal D_{e}\mathcal D^{d}T_{f}{}^{e})\,\gamma^{cf}\\
&-\frac{64}{3}T_{cd}\,(\mathcal D_{e}\mathcal D^{c}T^{de})
\end{aligned}\tag{G447}
```

**G448: 5:bos:5, whole coefficient matrix.**

```math
\begin{aligned}
&\frac{16}{3}T_{cd}\,\eta_{ef}\,(\mathcal D^{f}\mathcal D_{g}T^{g}{}_{h})\,\gamma^{c}\gamma^{de}\gamma^{h}\\
&=-\frac{16}{3}T_{cd}\,(\mathcal D_{e}\mathcal D_{f}T_{g}{}^{f})\,\gamma^{cdeg}\\
&+\frac{32}{3}T_{cd}\,(\mathcal D_{e}\mathcal D_{f}T^{df})\,\gamma^{ce}\\
&-\frac{16}{3}T_{cd}\,(\mathcal D_{e}\mathcal D_{f}T^{ef})\,\gamma^{cd}\\
&-\frac{16}{3}T_{cd}\,(\mathcal D^{d}\mathcal D_{e}T_{f}{}^{e})\,\gamma^{cf}\\
&+\frac{16}{3}T_{cd}\,(\mathcal D^{c}\mathcal D_{e}T^{de})\\
&=-\frac{16i}{3}\varepsilon_{cdefg}\,T^{de}\,(\mathcal D^{f}\mathcal D_{h}T^{gh})\,\gamma^{c}\\
&+\frac{32}{3}T_{cd}\,(\mathcal D_{e}\mathcal D_{f}T^{df})\,\gamma^{ce}\\
&-\frac{16}{3}T_{cd}\,(\mathcal D_{e}\mathcal D_{f}T^{ef})\,\gamma^{cd}\\
&-\frac{16}{3}T_{cd}\,(\mathcal D^{d}\mathcal D_{e}T_{f}{}^{e})\,\gamma^{cf}\\
&+\frac{16}{3}T_{cd}\,(\mathcal D^{c}\mathcal D_{e}T^{de})
\end{aligned}\tag{G448}
```

**G449: 5:bos:6, whole coefficient matrix.**

```math
\begin{aligned}
&2T_{cd}\,\eta_{ef}\,\widehat C^{de}{}_{gh}\,T_{jk}\,\gamma^{c}\gamma^{gh}\gamma^{jk}\gamma^{f}\\
&=-2\widehat C_{cdef}\,T^{cd}\,T_{gh}\,\gamma^{efgh}\\
&+4\widehat C_{cdef}\,T^{c}{}_{g}\,T^{d}{}_{h}\,\gamma^{efgh}\\
&+4\widehat C_{cdef}\,T^{d}{}_{g}\,T_{h}{}^{g}\,\gamma^{cefh}\\
&+8\widehat C_{cdef}\,T^{d}{}_{g}\,T^{f}{}_{h}\,\gamma^{cegh}\\
&-8\widehat C_{cdef}\,T^{cd}\,T^{f}{}_{g}\,\gamma^{eg}\\
&+8\widehat C_{cdef}\,T^{d}{}_{g}\,T^{fg}\,\gamma^{ce}\\
&+4\widehat C_{cdef}\,T^{d}{}_{g}\,T^{ef}\,\gamma^{cg}\\
&+4\widehat C_{cdef}\,T^{cd}\,T^{ef}\\
&+4\widehat C_{cdef}\,T^{df}\,T_{gh}\,\gamma^{cegh}\\
&-8\widehat C_{cdef}\,T^{de}\,T^{f}{}_{g}\,\gamma^{cg}\\
&+8\widehat C_{cdef}\,T^{ce}\,T^{df}\\
&=-2i\widehat C_{cdef}\,\varepsilon^{ef}{}_{ghj}\,T^{cd}\,T^{hj}\,\gamma^{g}\\
&+4i\widehat C_{cdef}\,\varepsilon^{ef}{}_{ghj}\,T^{ch}\,T^{dj}\,\gamma^{g}\\
&-4i\widehat C_{cdef}\,\varepsilon^{cef}{}_{gh}\,T^{d}{}_{j}\,T^{hj}\,\gamma^{g}\\
&+8i\widehat C_{cdef}\,\varepsilon^{ce}{}_{ghj}\,T^{dh}\,T^{fj}\,\gamma^{g}\\
&-8\widehat C_{cdef}\,T^{cd}\,T^{f}{}_{g}\,\gamma^{eg}\\
&+8\widehat C_{cdef}\,T^{d}{}_{g}\,T^{fg}\,\gamma^{ce}\\
&+4\widehat C_{cdef}\,T^{d}{}_{g}\,T^{ef}\,\gamma^{cg}\\
&+4\widehat C_{cdef}\,T^{cd}\,T^{ef}\\
&+4i\widehat C_{cdef}\,\varepsilon^{ce}{}_{ghj}\,T^{df}\,T^{hj}\,\gamma^{g}\\
&-8\widehat C_{cdef}\,T^{de}\,T^{f}{}_{g}\,\gamma^{cg}\\
&+8\widehat C_{cdef}\,T^{ce}\,T^{df}
\end{aligned}\tag{G449}
```

**G450: 5:bos:7, whole coefficient matrix.**

```math
\begin{aligned}
&8iT_{cd}\,\eta_{ef}\,(\mathcal D^{d}T_{gh})\,T_{jk}\,\gamma^{c}\gamma^{gh}\gamma^{e}\gamma^{jk}\gamma^{f}\\
&-8iT_{cd}\,\eta_{ef}\,(\mathcal D^{e}T_{gh})\,T_{jk}\,\gamma^{c}\gamma^{gh}\gamma^{d}\gamma^{jk}\gamma^{f}\\
&=-16iT_{cd}\,T^{d}{}_{e}\,(\mathcal D^{e}T_{fg})\,\gamma^{cfg}\\
&+8iT_{cd}\,T_{ef}\,(\mathcal D^{f}T_{gh})\,\gamma^{cdegh}\\
&-32iT_{cd}\,T_{ef}\,(\mathcal D^{d}T_{g}{}^{f})\,\gamma^{ceg}\\
&-32iT_{cd}\,T^{c}{}_{e}\,(\mathcal D^{d}T_{f}{}^{e})\,\gamma^{f}\\
&-16iT_{cd}\,T_{ef}\,(\mathcal D^{d}T^{ef})\,\gamma^{c}\\
&+48iT_{cd}\,T_{ef}\,(\mathcal D^{e}T_{g}{}^{f})\,\gamma^{cdg}\\
&-32iT_{cd}\,T_{ef}\,(\mathcal D^{e}T^{df})\,\gamma^{c}\\
&+32iT_{cd}\,T_{ef}\,(\mathcal D_{g}T_{h}{}^{f})\,\gamma^{cdegh}\\
&+32iT_{cd}\,T_{ef}\,(\mathcal D_{g}T^{fg})\,\gamma^{cde}\\
&+16iT_{cd}\,T^{cd}\,(\mathcal D_{e}T_{fg})\,\gamma^{efg}\\
&+32iT_{cd}\,T^{cd}\,(\mathcal D_{e}T_{f}{}^{e})\,\gamma^{f}\\
&+64iT_{cd}\,T^{d}{}_{e}\,(\mathcal D_{f}T_{g}{}^{e})\,\gamma^{cfg}\\
&+64iT_{cd}\,T^{d}{}_{e}\,(\mathcal D_{f}T^{ef})\,\gamma^{c}\\
&=-8\varepsilon_{cdefg}\,T^{e}{}_{h}\,T^{h}{}_{j}\,(\mathcal D^{j}T^{fg})\,\gamma^{cd}\\
&-4\varepsilon_{cdefg}\,T^{cd}\,T^{ef}\,(\mathcal D_{h}T^{gh})\\
&-16\varepsilon_{cdefg}\,T^{e}{}_{h}\,T^{f}{}_{j}\,(\mathcal D^{h}T^{gj})\,\gamma^{cd}\\
&-32iT_{cd}\,T^{c}{}_{e}\,(\mathcal D^{d}T_{f}{}^{e})\,\gamma^{f}\\
&-16iT_{cd}\,T_{ef}\,(\mathcal D^{d}T^{ef})\,\gamma^{c}\\
&+24\varepsilon_{cdefg}\,T^{ef}\,T_{hj}\,(\mathcal D^{h}T^{gj})\,\gamma^{cd}\\
&-32iT_{cd}\,T_{ef}\,(\mathcal D^{e}T^{df})\,\gamma^{c}\\
&+16\varepsilon_{cdefg}\,T^{ef}\,T^{g}{}_{h}\,(\mathcal D_{j}T^{hj})\,\gamma^{cd}\\
&+8\varepsilon_{cdefg}\,T_{hj}\,T^{hj}\,(\mathcal D^{e}T^{fg})\,\gamma^{cd}\\
&+32iT_{cd}\,T^{cd}\,(\mathcal D_{e}T_{f}{}^{e})\,\gamma^{f}\\
&+32\varepsilon_{cdefg}\,T^{e}{}_{h}\,T^{h}{}_{j}\,(\mathcal D^{f}T^{gj})\,\gamma^{cd}\\
&+64iT_{cd}\,T^{d}{}_{e}\,(\mathcal D_{f}T^{ef})\,\gamma^{c}
\end{aligned}\tag{G450}
```

**G451: 5:bos:8, whole coefficient matrix.**

```math
\begin{aligned}
&-\frac{8i}{3}T_{cd}\,\eta_{ef}\,(\mathcal D^{d}T_{gh})\,T_{jk}\,\gamma^{c}\gamma^{e}\gamma^{gh}\gamma^{jk}\gamma^{f}\\
&+\frac{8i}{3}T_{cd}\,\eta_{ef}\,(\mathcal D^{e}T_{gh})\,T_{jk}\,\gamma^{c}\gamma^{d}\gamma^{gh}\gamma^{jk}\gamma^{f}\\
&=-16iT_{cd}\,T^{d}{}_{e}\,(\mathcal D^{e}T_{fg})\,\gamma^{cfg}\\
&+8iT_{cd}\,T_{ef}\,(\mathcal D^{f}T_{gh})\,\gamma^{cdegh}\\
&-\frac{32i}{3}T_{cd}\,T_{ef}\,(\mathcal D^{d}T_{g}{}^{f})\,\gamma^{ceg}\\
&+32iT_{cd}\,T^{c}{}_{e}\,(\mathcal D^{d}T_{f}{}^{e})\,\gamma^{f}\\
&+\frac{16i}{3}T_{cd}\,T_{ef}\,(\mathcal D^{d}T^{ef})\,\gamma^{c}\\
&+16iT_{cd}\,T_{ef}\,(\mathcal D^{e}T_{g}{}^{f})\,\gamma^{cdg}\\
&-32iT_{cd}\,T_{ef}\,(\mathcal D^{e}T^{df})\,\gamma^{c}\\
&-\frac{16i}{3}T_{cd}\,T^{cd}\,(\mathcal D_{e}T_{fg})\,\gamma^{efg}\\
&-\frac{32i}{3}T_{cd}\,T^{cd}\,(\mathcal D_{e}T_{f}{}^{e})\,\gamma^{f}\\
&-\frac{128i}{3}T_{cd}\,T^{d}{}_{e}\,(\mathcal D_{f}T_{g}{}^{e})\,\gamma^{cfg}\\
&-\frac{128i}{3}T_{cd}\,T^{d}{}_{e}\,(\mathcal D_{f}T^{ef})\,\gamma^{c}\\
&-\frac{32i}{3}T_{cd}\,T_{ef}\,(\mathcal D_{g}T^{ef})\,\gamma^{cdg}\\
&-\frac{64i}{3}T_{cd}\,T_{ef}\,(\mathcal D_{g}T^{df})\,\gamma^{ceg}\\
&=-8\varepsilon_{cdefg}\,T^{e}{}_{h}\,T^{h}{}_{j}\,(\mathcal D^{j}T^{fg})\,\gamma^{cd}\\
&+4\varepsilon_{cdefg}\,T^{cd}\,T^{ef}\,(\mathcal D_{h}T^{gh})\\
&-\frac{16}{3}\varepsilon_{cdefg}\,T^{e}{}_{h}\,T^{f}{}_{j}\,(\mathcal D^{h}T^{gj})\,\gamma^{cd}\\
&+32iT_{cd}\,T^{c}{}_{e}\,(\mathcal D^{d}T_{f}{}^{e})\,\gamma^{f}\\
&+\frac{16i}{3}T_{cd}\,T_{ef}\,(\mathcal D^{d}T^{ef})\,\gamma^{c}\\
&+8\varepsilon_{cdefg}\,T^{ef}\,T_{hj}\,(\mathcal D^{h}T^{gj})\,\gamma^{cd}\\
&-32iT_{cd}\,T_{ef}\,(\mathcal D^{e}T^{df})\,\gamma^{c}\\
&-\frac{8}{3}\varepsilon_{cdefg}\,T_{hj}\,T^{hj}\,(\mathcal D^{e}T^{fg})\,\gamma^{cd}\\
&-\frac{32i}{3}T_{cd}\,T^{cd}\,(\mathcal D_{e}T_{f}{}^{e})\,\gamma^{f}\\
&-\frac{64}{3}\varepsilon_{cdefg}\,T^{e}{}_{h}\,T^{h}{}_{j}\,(\mathcal D^{f}T^{gj})\,\gamma^{cd}\\
&-\frac{128i}{3}T_{cd}\,T^{d}{}_{e}\,(\mathcal D_{f}T^{ef})\,\gamma^{c}\\
&-\frac{16}{3}\varepsilon_{cdefg}\,T^{ef}\,T_{hj}\,(\mathcal D^{g}T^{hj})\,\gamma^{cd}\\
&-\frac{32}{3}\varepsilon_{cdefg}\,T^{e}{}_{h}\,T^{f}{}_{j}\,(\mathcal D^{g}T^{hj})\,\gamma^{cd}
\end{aligned}\tag{G451}
```

**G452: 5:bos:9, whole coefficient matrix.**

```math
\begin{aligned}
&-\frac{8i}{3}T_{cd}\,\eta_{ef}\,(\mathcal D_{g}T_{hj})\,T_{kl}\,\gamma^{c}\gamma^{d}\gamma^{g}\gamma^{hj}\gamma^{e}\gamma^{kl}\gamma^{f}\\
&+\frac{8i}{3}T_{cd}\,\eta_{ef}\,(\mathcal D_{g}T_{hj})\,T_{kl}\,\gamma^{c}\gamma^{e}\gamma^{g}\gamma^{hj}\gamma^{d}\gamma^{kl}\gamma^{f}\\
&=\frac{64i}{3}T_{cd}\,T^{d}{}_{e}\,(\mathcal D_{f}T_{g}{}^{e})\,\gamma^{cfg}\\
&+\frac{32i}{3}T_{cd}\,T^{d}{}_{e}\,(\mathcal D^{e}T_{fg})\,\gamma^{cfg}\\
&-\frac{32i}{3}T_{cd}\,T^{cd}\,(\mathcal D_{e}T_{fg})\,\gamma^{efg}\\
&+\frac{64i}{3}T_{cd}\,T_{ef}\,(\mathcal D_{g}T_{h}{}^{f})\,\gamma^{cdegh}\\
&-\frac{64i}{3}T_{cd}\,T_{ef}\,(\mathcal D_{g}T^{df})\,\gamma^{ceg}\\
&+\frac{128i}{3}T_{cd}\,T_{ef}\,(\mathcal D^{d}T_{g}{}^{f})\,\gamma^{ceg}\\
&+\frac{32i}{3}T_{cd}\,T_{ef}\,(\mathcal D^{f}T_{gh})\,\gamma^{cdegh}\\
&+32iT_{cd}\,T_{ef}\,(\mathcal D_{g}T^{ef})\,\gamma^{cdg}\\
&-\frac{32i}{3}T_{cd}\,T_{ef}\,(\mathcal D^{d}T^{ef})\,\gamma^{c}\\
&-64iT_{cd}\,T_{ef}\,(\mathcal D^{e}T_{g}{}^{f})\,\gamma^{cdg}\\
&+\frac{64i}{3}T_{cd}\,T_{ef}\,(\mathcal D^{e}T^{df})\,\gamma^{c}\\
&-32iT_{cd}\,T_{ef}\,(\mathcal D_{g}T^{fg})\,\gamma^{cde}\\
&-\frac{64i}{3}T_{cd}\,T^{cd}\,(\mathcal D_{e}T_{f}{}^{e})\,\gamma^{f}\\
&-\frac{320i}{3}T_{cd}\,T^{d}{}_{e}\,(\mathcal D_{f}T^{ef})\,\gamma^{c}\\
&-\frac{32i}{3}T_{cd}\,T_{ef}\,(\mathcal D_{g}T_{h}{}^{g})\,\gamma^{cdefh}\\
&=\frac{32}{3}\varepsilon_{cdefg}\,T^{e}{}_{h}\,T^{h}{}_{j}\,(\mathcal D^{f}T^{gj})\,\gamma^{cd}\\
&+\frac{16}{3}\varepsilon_{cdefg}\,T^{e}{}_{h}\,T^{h}{}_{j}\,(\mathcal D^{j}T^{fg})\,\gamma^{cd}\\
&-\frac{16}{3}\varepsilon_{cdefg}\,T_{hj}\,T^{hj}\,(\mathcal D^{e}T^{fg})\,\gamma^{cd}\\
&+\frac{32}{3}\varepsilon_{cdefg}\,T^{cd}\,T^{ef}\,(\mathcal D_{h}T^{gh})\\
&-\frac{32}{3}\varepsilon_{cdefg}\,T^{e}{}_{h}\,T^{f}{}_{j}\,(\mathcal D^{g}T^{hj})\,\gamma^{cd}\\
&+\frac{64}{3}\varepsilon_{cdefg}\,T^{e}{}_{h}\,T^{f}{}_{j}\,(\mathcal D^{h}T^{gj})\,\gamma^{cd}\\
&+16\varepsilon_{cdefg}\,T^{ef}\,T_{hj}\,(\mathcal D^{g}T^{hj})\,\gamma^{cd}\\
&-\frac{32i}{3}T_{cd}\,T_{ef}\,(\mathcal D^{d}T^{ef})\,\gamma^{c}\\
&-32\varepsilon_{cdefg}\,T^{ef}\,T_{hj}\,(\mathcal D^{h}T^{gj})\,\gamma^{cd}\\
&+\frac{64i}{3}T_{cd}\,T_{ef}\,(\mathcal D^{e}T^{df})\,\gamma^{c}\\
&-16\varepsilon_{cdefg}\,T^{ef}\,T^{g}{}_{h}\,(\mathcal D_{j}T^{hj})\,\gamma^{cd}\\
&-\frac{64i}{3}T_{cd}\,T^{cd}\,(\mathcal D_{e}T_{f}{}^{e})\,\gamma^{f}\\
&-\frac{320i}{3}T_{cd}\,T^{d}{}_{e}\,(\mathcal D_{f}T^{ef})\,\gamma^{c}
\end{aligned}\tag{G452}
```

**G453: 5:bos:10, whole coefficient matrix.**

```math
\begin{aligned}
&-\frac{16i}{3}T_{cd}\,\eta_{ef}\,(\mathcal D_{g}T^{g}{}_{h})\,T_{jk}\,\gamma^{c}\gamma^{de}\gamma^{h}\gamma^{jk}\gamma^{f}\\
&=\frac{32i}{3}T_{cd}\,T_{ef}\,(\mathcal D_{g}T_{h}{}^{g})\,\gamma^{cdefh}\\
&+32iT_{cd}\,T_{ef}\,(\mathcal D_{g}T^{fg})\,\gamma^{cde}\\
&+64iT_{cd}\,T^{d}{}_{e}\,(\mathcal D_{f}T^{ef})\,\gamma^{c}\\
&=-\frac{32}{3}\varepsilon_{cdefg}\,T^{cd}\,T^{ef}\,(\mathcal D_{h}T^{gh})\\
&+16\varepsilon_{cdefg}\,T^{ef}\,T^{g}{}_{h}\,(\mathcal D_{j}T^{hj})\,\gamma^{cd}\\
&+64iT_{cd}\,T^{d}{}_{e}\,(\mathcal D_{f}T^{ef})\,\gamma^{c}
\end{aligned}\tag{G453}
```

**G454: 5:bos:11, whole coefficient matrix.**

```math
\begin{aligned}
&\frac{64i}{3}T_{cd}\,\eta_{ef}\,T^{de}\,(\mathcal D_{g}T_{hj})\,\gamma^{c}\gamma^{g}\gamma^{hj}\gamma^{f}\\
&=\frac{64i}{3}T_{cd}\,T^{cd}\,(\mathcal D_{e}T_{fg})\,\gamma^{efg}\\
&+\frac{256i}{3}T_{cd}\,T^{d}{}_{e}\,(\mathcal D_{f}T_{g}{}^{e})\,\gamma^{cfg}\\
&+\frac{128i}{3}T_{cd}\,T^{d}{}_{e}\,(\mathcal D^{e}T_{fg})\,\gamma^{cfg}\\
&-\frac{128i}{3}T_{cd}\,T^{cd}\,(\mathcal D_{e}T_{f}{}^{e})\,\gamma^{f}\\
&-\frac{256i}{3}T_{cd}\,T^{d}{}_{e}\,(\mathcal D_{f}T^{ef})\,\gamma^{c}\\
&=\frac{32}{3}\varepsilon_{cdefg}\,T_{hj}\,T^{hj}\,(\mathcal D^{e}T^{fg})\,\gamma^{cd}\\
&+\frac{128}{3}\varepsilon_{cdefg}\,T^{e}{}_{h}\,T^{h}{}_{j}\,(\mathcal D^{f}T^{gj})\,\gamma^{cd}\\
&+\frac{64}{3}\varepsilon_{cdefg}\,T^{e}{}_{h}\,T^{h}{}_{j}\,(\mathcal D^{j}T^{fg})\,\gamma^{cd}\\
&-\frac{128i}{3}T_{cd}\,T^{cd}\,(\mathcal D_{e}T_{f}{}^{e})\,\gamma^{f}\\
&-\frac{256i}{3}T_{cd}\,T^{d}{}_{e}\,(\mathcal D_{f}T^{ef})\,\gamma^{c}
\end{aligned}\tag{G454}
```

**G455: 5:bos:12, whole coefficient matrix.**

```math
\begin{aligned}
&-\frac{64i}{3}T_{cd}\,\eta_{ef}\,T^{de}\,(\mathcal D^{f}T_{gh})\,\gamma^{c}\gamma^{gh}\\
&=-\frac{64i}{3}T_{cd}\,T^{d}{}_{e}\,(\mathcal D^{e}T_{fg})\,\gamma^{cfg}\\
&-\frac{128i}{3}T_{cd}\,T^{c}{}_{e}\,(\mathcal D^{d}T_{f}{}^{e})\,\gamma^{f}\\
&=-\frac{32}{3}\varepsilon_{cdefg}\,T^{e}{}_{h}\,T^{h}{}_{j}\,(\mathcal D^{j}T^{fg})\,\gamma^{cd}\\
&-\frac{128i}{3}T_{cd}\,T^{c}{}_{e}\,(\mathcal D^{d}T_{f}{}^{e})\,\gamma^{f}
\end{aligned}\tag{G455}
```

**G456: 5:bos:13, whole coefficient matrix.**

```math
\begin{aligned}
&\frac{64i}{3}T_{cd}\,\eta_{ef}\,T^{de}\,(\mathcal D_{g}T^{g}{}_{h})\,\gamma^{c}\gamma^{f}\gamma^{h}\\
&=\frac{64i}{3}T_{cd}\,T^{cd}\,(\mathcal D_{e}T_{f}{}^{e})\,\gamma^{f}
\end{aligned}\tag{G456}
```

**G457: 5:bos:14, whole coefficient matrix.**

```math
\begin{aligned}
&64T_{cd}\,\eta_{ef}\,T^{de}\,T_{gh}\,T_{jk}\,\gamma^{c}\gamma^{fghjk}\\
&=-64T_{cd}\,T_{ef}\,T_{gh}\,T^{gh}\,\gamma^{cdef}\\
&+256T_{cd}\,T_{ef}\,T_{gh}\,T^{fh}\,\gamma^{cdeg}\\
&=0
\end{aligned}\tag{G457}
```

**G458: 5:bos:15, whole coefficient matrix.**

```math
\begin{aligned}
&-512T_{cd}\,\eta_{ef}\,T^{de}\,T_{gh}\,T^{fh}\,\gamma^{c}\gamma^{g}\\
&=512T_{cd}\,T^{c}{}_{e}\,T^{d}{}_{f}\,T^{ef}
\end{aligned}\tag{G458}
```

**G459: 5:bos:16, whole coefficient matrix.**

```math
\begin{aligned}
&128T_{cd}\,\eta_{ef}\,T^{de}\,T_{gh}\,T^{gh}\,\gamma^{c}\gamma^{f}\\
&=-128T_{cd}\,T^{cd}\,T_{ef}\,T^{ef}
\end{aligned}\tag{G459}
```

**G460: 5:bos:17, whole coefficient matrix.**

```math
\begin{aligned}
&-\frac{64i}{9}T_{cd}\,\eta_{ef}\,T^{d}{}_{g}\,(\mathcal D_{h}T_{jk})\,\gamma^{c}\gamma^{eg}\gamma^{h}\gamma^{jk}\gamma^{f}\\
&+\frac{64i}{9}T_{cd}\,\eta_{ef}\,T^{e}{}_{g}\,(\mathcal D_{h}T_{jk})\,\gamma^{c}\gamma^{dg}\gamma^{h}\gamma^{jk}\gamma^{f}\\
&=-\frac{512i}{9}T_{cd}\,T^{d}{}_{e}\,(\mathcal D_{f}T_{g}{}^{e})\,\gamma^{cfg}\\
&+\frac{512i}{9}T_{cd}\,T^{d}{}_{e}\,(\mathcal D_{f}T^{ef})\,\gamma^{c}\\
&-\frac{256i}{9}T_{cd}\,T^{d}{}_{e}\,(\mathcal D^{e}T_{fg})\,\gamma^{cfg}\\
&-\frac{64i}{3}T_{cd}\,T^{cd}\,(\mathcal D_{e}T_{fg})\,\gamma^{efg}\\
&-\frac{128i}{9}T_{cd}\,T^{cd}\,(\mathcal D_{e}T_{f}{}^{e})\,\gamma^{f}\\
&+\frac{128i}{3}T_{cd}\,T_{ef}\,(\mathcal D_{g}T_{h}{}^{f})\,\gamma^{cdegh}\\
&-\frac{128i}{9}T_{cd}\,T_{ef}\,(\mathcal D_{g}T_{h}{}^{g})\,\gamma^{cdefh}\\
&-\frac{256i}{9}T_{cd}\,T_{ef}\,(\mathcal D_{g}T^{fg})\,\gamma^{cde}\\
&+\frac{256i}{9}T_{cd}\,T_{ef}\,(\mathcal D^{d}T^{ef})\,\gamma^{c}\\
&-\frac{512i}{9}T_{cd}\,T_{ef}\,(\mathcal D^{e}T^{df})\,\gamma^{c}\\
&+\frac{64i}{3}T_{cd}\,T_{ef}\,(\mathcal D^{f}T_{gh})\,\gamma^{cdegh}\\
&=-\frac{256}{9}\varepsilon_{cdefg}\,T^{e}{}_{h}\,T^{h}{}_{j}\,(\mathcal D^{f}T^{gj})\,\gamma^{cd}\\
&+\frac{512i}{9}T_{cd}\,T^{d}{}_{e}\,(\mathcal D_{f}T^{ef})\,\gamma^{c}\\
&-\frac{128}{9}\varepsilon_{cdefg}\,T^{e}{}_{h}\,T^{h}{}_{j}\,(\mathcal D^{j}T^{fg})\,\gamma^{cd}\\
&-\frac{32}{3}\varepsilon_{cdefg}\,T_{hj}\,T^{hj}\,(\mathcal D^{e}T^{fg})\,\gamma^{cd}\\
&-\frac{128i}{9}T_{cd}\,T^{cd}\,(\mathcal D_{e}T_{f}{}^{e})\,\gamma^{f}\\
&+\frac{128}{9}\varepsilon_{cdefg}\,T^{cd}\,T^{ef}\,(\mathcal D_{h}T^{gh})\\
&-\frac{128}{9}\varepsilon_{cdefg}\,T^{ef}\,T^{g}{}_{h}\,(\mathcal D_{j}T^{hj})\,\gamma^{cd}\\
&+\frac{256i}{9}T_{cd}\,T_{ef}\,(\mathcal D^{d}T^{ef})\,\gamma^{c}\\
&-\frac{512i}{9}T_{cd}\,T_{ef}\,(\mathcal D^{e}T^{df})\,\gamma^{c}
\end{aligned}\tag{G460}
```

**G461: 5:bos:18, whole coefficient matrix.**

```math
\begin{aligned}
&\frac{64i}{9}T_{cd}\,\eta_{ef}\,T^{d}{}_{g}\,(\mathcal D^{f}T_{hj})\,\gamma^{c}\gamma^{eg}\gamma^{hj}\\
&-\frac{64i}{9}T_{cd}\,\eta_{ef}\,T^{e}{}_{g}\,(\mathcal D^{f}T_{hj})\,\gamma^{c}\gamma^{dg}\gamma^{hj}\\
&=\frac{128i}{9}T_{cd}\,T^{d}{}_{e}\,(\mathcal D^{e}T_{fg})\,\gamma^{cfg}\\
&+\frac{256i}{9}T_{cd}\,T^{c}{}_{e}\,(\mathcal D^{d}T_{f}{}^{e})\,\gamma^{f}\\
&+\frac{64i}{9}T_{cd}\,T^{cd}\,(\mathcal D_{e}T_{fg})\,\gamma^{efg}\\
&-\frac{128i}{9}T_{cd}\,T^{cd}\,(\mathcal D_{e}T_{f}{}^{e})\,\gamma^{f}\\
&+\frac{64i}{9}T_{cd}\,T_{ef}\,(\mathcal D^{f}T_{gh})\,\gamma^{cdegh}\\
&-\frac{256i}{9}T_{cd}\,T_{ef}\,(\mathcal D^{d}T_{g}{}^{f})\,\gamma^{ceg}\\
&+\frac{128i}{9}T_{cd}\,T_{ef}\,(\mathcal D^{e}T_{g}{}^{f})\,\gamma^{cdg}\\
&-\frac{128i}{9}T_{cd}\,T_{ef}\,(\mathcal D^{d}T^{ef})\,\gamma^{c}\\
&+\frac{256i}{9}T_{cd}\,T_{ef}\,(\mathcal D^{e}T^{df})\,\gamma^{c}\\
&=\frac{64}{9}\varepsilon_{cdefg}\,T^{e}{}_{h}\,T^{h}{}_{j}\,(\mathcal D^{j}T^{fg})\,\gamma^{cd}\\
&+\frac{256i}{9}T_{cd}\,T^{c}{}_{e}\,(\mathcal D^{d}T_{f}{}^{e})\,\gamma^{f}\\
&+\frac{32}{9}\varepsilon_{cdefg}\,T_{hj}\,T^{hj}\,(\mathcal D^{e}T^{fg})\,\gamma^{cd}\\
&-\frac{128i}{9}T_{cd}\,T^{cd}\,(\mathcal D_{e}T_{f}{}^{e})\,\gamma^{f}\\
&+\frac{32}{9}\varepsilon_{cdefg}\,T^{cd}\,T^{ef}\,(\mathcal D_{h}T^{gh})\\
&-\frac{128}{9}\varepsilon_{cdefg}\,T^{e}{}_{h}\,T^{f}{}_{j}\,(\mathcal D^{h}T^{gj})\,\gamma^{cd}\\
&+\frac{64}{9}\varepsilon_{cdefg}\,T^{ef}\,T_{hj}\,(\mathcal D^{h}T^{gj})\,\gamma^{cd}\\
&-\frac{128i}{9}T_{cd}\,T_{ef}\,(\mathcal D^{d}T^{ef})\,\gamma^{c}\\
&+\frac{256i}{9}T_{cd}\,T_{ef}\,(\mathcal D^{e}T^{df})\,\gamma^{c}
\end{aligned}\tag{G461}
```

**G462: 5:bos:19, whole coefficient matrix.**

```math
\begin{aligned}
&-\frac{64i}{9}T_{cd}\,\eta_{ef}\,T^{d}{}_{g}\,(\mathcal D_{h}T^{h}{}_{j})\,\gamma^{c}\gamma^{eg}\gamma^{f}\gamma^{j}\\
&+\frac{64i}{9}T_{cd}\,\eta_{ef}\,T^{e}{}_{g}\,(\mathcal D_{h}T^{h}{}_{j})\,\gamma^{c}\gamma^{dg}\gamma^{f}\gamma^{j}\\
&=\frac{64i}{3}T_{cd}\,T^{cd}\,(\mathcal D_{e}T_{f}{}^{e})\,\gamma^{f}\\
&+\frac{64i}{9}T_{cd}\,T_{ef}\,(\mathcal D_{g}T_{h}{}^{g})\,\gamma^{cdefh}\\
&+\frac{256i}{9}T_{cd}\,T_{ef}\,(\mathcal D_{g}T^{fg})\,\gamma^{cde}\\
&=\frac{64i}{3}T_{cd}\,T^{cd}\,(\mathcal D_{e}T_{f}{}^{e})\,\gamma^{f}\\
&-\frac{64}{9}\varepsilon_{cdefg}\,T^{cd}\,T^{ef}\,(\mathcal D_{h}T^{gh})\\
&+\frac{128}{9}\varepsilon_{cdefg}\,T^{ef}\,T^{g}{}_{h}\,(\mathcal D_{j}T^{hj})\,\gamma^{cd}
\end{aligned}\tag{G462}
```

**G463: 5:bos:20, whole coefficient matrix.**

```math
\begin{aligned}
&-\frac{64}{3}T_{cd}\,\eta_{ef}\,T^{d}{}_{g}\,T_{hj}\,T_{kl}\,\gamma^{c}\gamma^{eg}\gamma^{fhjkl}\\
&+\frac{64}{3}T_{cd}\,\eta_{ef}\,T^{e}{}_{g}\,T_{hj}\,T_{kl}\,\gamma^{c}\gamma^{dg}\gamma^{fhjkl}\\
&=-\frac{7168}{15}T_{cd}\,T_{ef}\,T_{gh}\,T^{fh}\,\gamma^{cdeg}\\
&+\frac{1472}{15}T_{cd}\,T_{ef}\,T_{gh}\,T^{gh}\,\gamma^{cdef}\\
&=-\frac{64i}{3}\varepsilon_{cdefg}\,T^{de}\,T^{fg}\,T_{hj}\,T^{hj}\,\gamma^{c}
\end{aligned}\tag{G463}
```

**G464: 5:bos:21, whole coefficient matrix.**

```math
\begin{aligned}
&\frac{512}{3}T_{cd}\,\eta_{ef}\,T^{d}{}_{g}\,T_{hj}\,T^{fj}\,\gamma^{c}\gamma^{eg}\gamma^{h}\\
&-\frac{512}{3}T_{cd}\,\eta_{ef}\,T^{e}{}_{g}\,T_{hj}\,T^{fj}\,\gamma^{c}\gamma^{dg}\gamma^{h}\\
&=-\frac{1024}{3}T_{cd}\,T^{c}{}_{e}\,T^{d}{}_{f}\,T^{ef}\\
&+\frac{512}{3}T_{cd}\,T^{cd}\,T_{ef}\,T^{ef}\\
&+\frac{512}{3}T_{cd}\,T_{ef}\,T_{gh}\,T^{fh}\,\gamma^{cdeg}\\
&=-\frac{1024}{3}T_{cd}\,T^{c}{}_{e}\,T^{d}{}_{f}\,T^{ef}\\
&+\frac{512}{3}T_{cd}\,T^{cd}\,T_{ef}\,T^{ef}\\
&+\frac{128i}{3}\varepsilon_{cdefg}\,T^{de}\,T^{fg}\,T_{hj}\,T^{hj}\,\gamma^{c}
\end{aligned}\tag{G464}
```

**G465: 5:bos:22, whole coefficient matrix.**

```math
\begin{aligned}
&-\frac{128}{3}T_{cd}\,\eta_{ef}\,T^{d}{}_{g}\,T_{hj}\,T^{hj}\,\gamma^{c}\gamma^{eg}\gamma^{f}\\
&+\frac{128}{3}T_{cd}\,\eta_{ef}\,T^{e}{}_{g}\,T_{hj}\,T^{hj}\,\gamma^{c}\gamma^{dg}\gamma^{f}\\
&=-128T_{cd}\,T^{cd}\,T_{ef}\,T^{ef}\\
&-\frac{128}{3}T_{cd}\,T_{ef}\,T_{gh}\,T^{gh}\,\gamma^{cdef}\\
&=-128T_{cd}\,T^{cd}\,T_{ef}\,T^{ef}\\
&-\frac{128i}{3}\varepsilon_{cdefg}\,T^{de}\,T^{fg}\,T_{hj}\,T^{hj}\,\gamma^{c}
\end{aligned}\tag{G465}
```

**G466: 5:bos:23, whole coefficient matrix.**

```math
\begin{aligned}
&-\frac{32i}{9}T_{cd}\,\eta_{ef}\,T_{gh}\,(\mathcal D_{j}T_{kl})\,\gamma^{c}\gamma^{degh}\gamma^{j}\gamma^{kl}\gamma^{f}\\
&=-\frac{256i}{9}T_{cd}\,T_{ef}\,(\mathcal D^{e}T_{g}{}^{f})\,\gamma^{cdg}\\
&-\frac{160i}{9}T_{cd}\,T_{ef}\,(\mathcal D^{f}T_{gh})\,\gamma^{cdegh}\\
&+\frac{512i}{9}T_{cd}\,T_{ef}\,(\mathcal D^{d}T_{g}{}^{f})\,\gamma^{ceg}\\
&+\frac{256i}{9}T_{cd}\,T_{ef}\,(\mathcal D^{e}T^{df})\,\gamma^{c}\\
&-\frac{128i}{9}T_{cd}\,T_{ef}\,(\mathcal D^{d}T^{ef})\,\gamma^{c}\\
&-\frac{64i}{9}T_{cd}\,T_{ef}\,(\mathcal D_{g}T_{h}{}^{f})\,\gamma^{cdegh}\\
&-\frac{128i}{3}T_{cd}\,T_{ef}\,(\mathcal D_{g}T^{fg})\,\gamma^{cde}\\
&+\frac{128i}{9}T_{cd}\,T_{ef}\,(\mathcal D_{g}T^{ef})\,\gamma^{cdg}\\
&-\frac{256i}{9}T_{cd}\,T_{ef}\,(\mathcal D_{g}T^{df})\,\gamma^{ceg}\\
&-\frac{64i}{9}T_{cd}\,T_{ef}\,(\mathcal D_{g}T_{h}{}^{g})\,\gamma^{cdefh}\\
&=-\frac{128}{9}\varepsilon_{cdefg}\,T^{ef}\,T_{hj}\,(\mathcal D^{h}T^{gj})\,\gamma^{cd}\\
&+\frac{256}{9}\varepsilon_{cdefg}\,T^{e}{}_{h}\,T^{f}{}_{j}\,(\mathcal D^{h}T^{gj})\,\gamma^{cd}\\
&+\frac{256i}{9}T_{cd}\,T_{ef}\,(\mathcal D^{e}T^{df})\,\gamma^{c}\\
&-\frac{128i}{9}T_{cd}\,T_{ef}\,(\mathcal D^{d}T^{ef})\,\gamma^{c}\\
&-\frac{64}{3}\varepsilon_{cdefg}\,T^{ef}\,T^{g}{}_{h}\,(\mathcal D_{j}T^{hj})\,\gamma^{cd}\\
&+\frac{64}{9}\varepsilon_{cdefg}\,T^{ef}\,T_{hj}\,(\mathcal D^{g}T^{hj})\,\gamma^{cd}\\
&-\frac{128}{9}\varepsilon_{cdefg}\,T^{e}{}_{h}\,T^{f}{}_{j}\,(\mathcal D^{g}T^{hj})\,\gamma^{cd}
\end{aligned}\tag{G466}
```

**G467: 5:bos:24, whole coefficient matrix.**

```math
\begin{aligned}
&\frac{32i}{9}T_{cd}\,\eta_{ef}\,T_{gh}\,(\mathcal D^{f}T_{jk})\,\gamma^{c}\gamma^{degh}\gamma^{jk}\\
&=\frac{128i}{9}T_{cd}\,T_{ef}\,(\mathcal D_{g}T_{h}{}^{f})\,\gamma^{cdegh}\\
&-\frac{128i}{9}T_{cd}\,T_{ef}\,(\mathcal D_{g}T^{ef})\,\gamma^{cdg}\\
&-\frac{256i}{9}T_{cd}\,T_{ef}\,(\mathcal D_{g}T^{fg})\,\gamma^{cde}\\
&+\frac{256i}{9}T_{cd}\,T_{ef}\,(\mathcal D_{g}T^{df})\,\gamma^{ceg}\\
&-\frac{32i}{9}T_{cd}\,T_{ef}\,(\mathcal D_{g}T_{h}{}^{g})\,\gamma^{cdefh}\\
&+\frac{32i}{9}T_{cd}\,T_{ef}\,(\mathcal D^{f}T_{gh})\,\gamma^{cdegh}\\
&+\frac{64i}{9}T_{cd}\,T_{ef}\,(\mathcal D^{e}T_{g}{}^{f})\,\gamma^{cdg}\\
&-\frac{128i}{9}T_{cd}\,T_{ef}\,(\mathcal D^{d}T_{g}{}^{f})\,\gamma^{ceg}\\
&+\frac{128i}{9}T_{cd}\,T_{ef}\,(\mathcal D^{e}T^{df})\,\gamma^{c}\\
&-\frac{64i}{9}T_{cd}\,T_{ef}\,(\mathcal D^{d}T^{ef})\,\gamma^{c}\\
&=\frac{16}{9}\varepsilon_{cdefg}\,T^{cd}\,T^{ef}\,(\mathcal D_{h}T^{gh})\\
&-\frac{64}{9}\varepsilon_{cdefg}\,T^{ef}\,T_{hj}\,(\mathcal D^{g}T^{hj})\,\gamma^{cd}\\
&-\frac{128}{9}\varepsilon_{cdefg}\,T^{ef}\,T^{g}{}_{h}\,(\mathcal D_{j}T^{hj})\,\gamma^{cd}\\
&+\frac{128}{9}\varepsilon_{cdefg}\,T^{e}{}_{h}\,T^{f}{}_{j}\,(\mathcal D^{g}T^{hj})\,\gamma^{cd}\\
&+\frac{32}{9}\varepsilon_{cdefg}\,T^{ef}\,T_{hj}\,(\mathcal D^{h}T^{gj})\,\gamma^{cd}\\
&-\frac{64}{9}\varepsilon_{cdefg}\,T^{e}{}_{h}\,T^{f}{}_{j}\,(\mathcal D^{h}T^{gj})\,\gamma^{cd}\\
&+\frac{128i}{9}T_{cd}\,T_{ef}\,(\mathcal D^{e}T^{df})\,\gamma^{c}\\
&-\frac{64i}{9}T_{cd}\,T_{ef}\,(\mathcal D^{d}T^{ef})\,\gamma^{c}
\end{aligned}\tag{G467}
```

**G468: 5:bos:25, whole coefficient matrix.**

```math
\begin{aligned}
&-\frac{32i}{9}T_{cd}\,\eta_{ef}\,T_{gh}\,(\mathcal D_{j}T^{j}{}_{k})\,\gamma^{c}\gamma^{degh}\gamma^{f}\gamma^{k}\\
&=\frac{64i}{9}T_{cd}\,T_{ef}\,(\mathcal D_{g}T_{h}{}^{g})\,\gamma^{cdefh}\\
&+\frac{256i}{9}T_{cd}\,T_{ef}\,(\mathcal D_{g}T^{fg})\,\gamma^{cde}\\
&=-\frac{64}{9}\varepsilon_{cdefg}\,T^{cd}\,T^{ef}\,(\mathcal D_{h}T^{gh})\\
&+\frac{128}{9}\varepsilon_{cdefg}\,T^{ef}\,T^{g}{}_{h}\,(\mathcal D_{j}T^{hj})\,\gamma^{cd}
\end{aligned}\tag{G468}
```

**G469: 5:bos:26, whole coefficient matrix.**

```math
\begin{aligned}
&-\frac{32}{3}T_{cd}\,\eta_{ef}\,T_{gh}\,T_{jk}\,T_{lm}\,\gamma^{c}\gamma^{degh}\gamma^{fjklm}\\
&=\frac{256}{15}T_{cd}\,T_{ef}\,T_{gh}\,T^{fh}\,\gamma^{cdeg}\\
&-\frac{64}{15}T_{cd}\,T_{ef}\,T_{gh}\,T^{gh}\,\gamma^{cdef}\\
&-\frac{256}{3}T_{cd}\,T^{cd}\,T_{ef}\,T^{ef}\\
&+\frac{512}{3}T_{cd}\,T^{c}{}_{e}\,T^{d}{}_{f}\,T^{ef}\\
&=-\frac{256}{3}T_{cd}\,T^{cd}\,T_{ef}\,T^{ef}\\
&+\frac{512}{3}T_{cd}\,T^{c}{}_{e}\,T^{d}{}_{f}\,T^{ef}
\end{aligned}\tag{G469}
```

**G470: 5:bos:27, whole coefficient matrix.**

```math
\begin{aligned}
&\frac{256}{3}T_{cd}\,\eta_{ef}\,T_{gh}\,T_{jk}\,T^{fk}\,\gamma^{c}\gamma^{degh}\gamma^{j}\\
&=-256T_{cd}\,T_{ef}\,T_{gh}\,T^{fh}\,\gamma^{cdeg}\\
&+\frac{256}{3}T_{cd}\,T_{ef}\,T_{gh}\,T^{gh}\,\gamma^{cdef}\\
&=\frac{64i}{3}\varepsilon_{cdefg}\,T^{de}\,T^{fg}\,T_{hj}\,T^{hj}\,\gamma^{c}
\end{aligned}\tag{G470}
```

**G471: 5:bos:28, whole coefficient matrix.**

```math
\begin{aligned}
&-\frac{64}{3}T_{cd}\,\eta_{ef}\,T_{gh}\,T_{jk}\,T^{jk}\,\gamma^{c}\gamma^{degh}\gamma^{f}\\
&=-\frac{128}{3}T_{cd}\,T_{ef}\,T_{gh}\,T^{gh}\,\gamma^{cdef}\\
&=-\frac{128i}{3}\varepsilon_{cdefg}\,T^{de}\,T^{fg}\,T_{hj}\,T^{hj}\,\gamma^{c}
\end{aligned}\tag{G471}
```

**G472: 5:connection:1, scalar coefficient.**

```math
\begin{aligned}
&3i\big(\bar\chi\gamma^{f}\gamma^{c}\widehat R(Q)_{de}\big)\,T_{c}{}^{d}\,\eta^{e}{}_{f}\\
&=6i\big(\overline{\widehat R(Q)_{cd}}\chi\big)\,T^{cd}
\end{aligned}\tag{G472}
```

**G473: 5:connection:1, vector coefficient.**

```math
\begin{aligned}
&3i\big(\bar\chi\gamma^{f}\gamma^{a}\gamma^{c}\widehat R(Q)_{de}\big)\,T_{c}{}^{d}\,\eta^{e}{}_{f}\\
&=-6i\big(\overline{\widehat R(Q)_{cd}}\gamma^{a}\chi\big)\,T^{cd}\\
&-6i\big(\overline{\widehat R(Q)^{a}{}_{c}}\gamma^{d}\chi\big)\,T^{c}{}_{d}
\end{aligned}\tag{G473}
```

**G474: 5:connection:1, bivector coefficient.**

```math
\begin{aligned}
&-\frac{3i}{2}\big(\bar\chi\gamma^{f}\gamma^{[ab]}\gamma^{c}\widehat R(Q)_{de}\big)\,T_{c}{}^{d}\,\eta^{e}{}_{f}\\
&=3i\big(\overline{\widehat R(Q)_{cd}}\gamma^{[ab]}\chi\big)\,T^{cd}\\
&-6i\big(\overline{\widehat R(Q)^{[a}{}_{|c|}}\gamma^{b]d}\chi\big)\,T^{c}{}_{d}\\
&+6i\big(\overline{\widehat R(Q)^{[a}{}_{|c|}}\chi\big)\,T^{|c|b]}
\end{aligned}\tag{G474}
```

**G475: 5:connection:2, scalar coefficient.**

```math
\begin{aligned}
&-\frac{i}{16}\big(\overline{\widehat R(Q)_{fh}}\gamma^{g}\gamma^{c}\gamma_{g}{}^{h}\widehat R(Q)_{de}\big)\,T_{c}{}^{d}\,\eta^{ef}\\
&=-\frac{3i}{8}\big(\overline{\widehat R(Q)_{ec}}\widehat R(Q)^{e}{}_{d}\big)\,T^{cd}
\end{aligned}\tag{G475}
```

**G476: 5:connection:2, vector coefficient.**

```math
\begin{aligned}
&-\frac{i}{16}\big(\overline{\widehat R(Q)_{fh}}\gamma^{g}\gamma^{a}\gamma^{c}\gamma_{g}{}^{h}\widehat R(Q)_{de}\big)\,T_{c}{}^{d}\,\eta^{ef}\\
&=\frac{i}{8}\big(\overline{\widehat R(Q)_{ec}}\gamma^{a}\widehat R(Q)^{e}{}_{d}\big)\,T^{cd}\\
&-\frac{i}{8}\big(\overline{\widehat R(Q)_{e}{}^{a}}\gamma^{c}\widehat R(Q)^{e}{}_{d}\big)\,T_{c}{}^{d}
\end{aligned}\tag{G476}
```

**G477: 5:connection:2, bivector coefficient.**

```math
\begin{aligned}
&\frac{i}{32}\big(\overline{\widehat R(Q)_{fh}}\gamma^{g}\gamma^{[ab]}\gamma^{c}\gamma_{g}{}^{h}\widehat R(Q)_{de}\big)\,T_{c}{}^{d}\,\eta^{ef}\\
&=-\frac{i}{8}\big(\overline{\widehat R(Q)_{e}{}^{[a}}\gamma^{b]c}\widehat R(Q)^{e}{}_{d}\big)\,T_{c}{}^{d}\\
&-\frac{3i}{8}\big(\overline{\widehat R(Q)_{d}{}^{[a}}\widehat R(Q)^{|d|}{}_{|c|}\big)\,T^{|c|b]}
\end{aligned}\tag{G477}
```

**G478: 5:connection:2, scalar coefficient.**

```math
\begin{aligned}
&\frac{i}{16}\big(\overline{\widehat R(Q)_{fh}}\gamma^{g}\gamma^{c}\gamma^{h}{}_{g}\widehat R(Q)_{de}\big)\,T_{c}{}^{d}\,\eta^{ef}\\
&=-\frac{3i}{8}\big(\overline{\widehat R(Q)_{ec}}\widehat R(Q)^{e}{}_{d}\big)\,T^{cd}
\end{aligned}\tag{G478}
```

**G479: 5:connection:2, vector coefficient.**

```math
\begin{aligned}
&\frac{i}{16}\big(\overline{\widehat R(Q)_{fh}}\gamma^{g}\gamma^{a}\gamma^{c}\gamma^{h}{}_{g}\widehat R(Q)_{de}\big)\,T_{c}{}^{d}\,\eta^{ef}\\
&=\frac{i}{8}\big(\overline{\widehat R(Q)_{ec}}\gamma^{a}\widehat R(Q)^{e}{}_{d}\big)\,T^{cd}\\
&-\frac{i}{8}\big(\overline{\widehat R(Q)_{e}{}^{a}}\gamma^{c}\widehat R(Q)^{e}{}_{d}\big)\,T_{c}{}^{d}
\end{aligned}\tag{G479}
```

**G480: 5:connection:2, bivector coefficient.**

```math
\begin{aligned}
&-\frac{i}{32}\big(\overline{\widehat R(Q)_{fh}}\gamma^{g}\gamma^{[ab]}\gamma^{c}\gamma^{h}{}_{g}\widehat R(Q)_{de}\big)\,T_{c}{}^{d}\,\eta^{ef}\\
&=-\frac{i}{8}\big(\overline{\widehat R(Q)_{e}{}^{[a}}\gamma^{b]c}\widehat R(Q)^{e}{}_{d}\big)\,T_{c}{}^{d}\\
&-\frac{3i}{8}\big(\overline{\widehat R(Q)_{d}{}^{[a}}\widehat R(Q)^{|d|}{}_{|c|}\big)\,T^{|c|b]}
\end{aligned}\tag{G480}
```

**G481: 5:connection:3, scalar coefficient.**

```math
\begin{aligned}
&-\frac{i}{16}\big(\overline{\widehat R(Q)_{gh}}\gamma^{f}\gamma^{c}\gamma^{gh}\widehat R(Q)_{de}\big)\,T_{c}{}^{d}\,\eta^{e}{}_{f}\\
&=-\frac{i}{2}\big(\overline{\widehat R(Q)_{ec}}\widehat R(Q)^{e}{}_{d}\big)\,T^{cd}
\end{aligned}\tag{G481}
```

**G482: 5:connection:3, vector coefficient.**

```math
\begin{aligned}
&-\frac{i}{16}\big(\overline{\widehat R(Q)_{gh}}\gamma^{f}\gamma^{a}\gamma^{c}\gamma^{gh}\widehat R(Q)_{de}\big)\,T_{c}{}^{d}\,\eta^{e}{}_{f}\\
&=\frac{i}{2}\big(\overline{\widehat R(Q)_{ec}}\gamma^{a}\widehat R(Q)^{e}{}_{d}\big)\,T^{cd}\\
&-\frac{i}{2}\big(\overline{\widehat R(Q)_{e}{}^{a}}\gamma^{c}\widehat R(Q)^{e}{}_{d}\big)\,T_{c}{}^{d}
\end{aligned}\tag{G482}
```

**G483: 5:connection:3, bivector coefficient.**

```math
\begin{aligned}
&\frac{i}{32}\big(\overline{\widehat R(Q)_{gh}}\gamma^{f}\gamma^{[ab]}\gamma^{c}\gamma^{gh}\widehat R(Q)_{de}\big)\,T_{c}{}^{d}\,\eta^{e}{}_{f}\\
&=\frac{3i}{8}\big(\overline{\widehat R(Q)_{e}{}^{[a}}\gamma^{b]c}\widehat R(Q)^{e}{}_{d}\big)\,T_{c}{}^{d}\\
&+\frac{7i}{16}\big(\overline{\widehat R(Q)^{[ab]}}\widehat R(Q)_{cd}\big)\,T^{cd}\\
&-\frac{i}{2}\big(\overline{\widehat R(Q)_{d}{}^{[a}}\widehat R(Q)^{|d|}{}_{|c|}\big)\,T^{|c|b]}
\end{aligned}\tag{G483}
```

**G484: 5:connection:4, scalar coefficient.**

```math
\begin{aligned}
&-\frac{i}{2}\big(\bar\chi\gamma^{h}\gamma^{e}\gamma^{d}{}_{h}\widehat R(Q)_{fg}\big)\,\eta_{cd}\,T_{e}{}^{f}\,\eta^{gc}\\
&=-i\big(\overline{\widehat R(Q)_{cd}}\chi\big)\,T^{cd}
\end{aligned}\tag{G484}
```

**G485: 5:connection:4, vector coefficient.**

```math
\begin{aligned}
&-\frac{i}{2}\big(\bar\chi\gamma^{h}\gamma^{a}\gamma^{e}\gamma^{d}{}_{h}\widehat R(Q)_{fg}\big)\,\eta_{cd}\,T_{e}{}^{f}\,\eta^{gc}\\
&=i\big(\overline{\widehat R(Q)_{cd}}\gamma^{a}\chi\big)\,T^{cd}\\
&+i\big(\overline{\widehat R(Q)^{a}{}_{c}}\gamma^{d}\chi\big)\,T^{c}{}_{d}
\end{aligned}\tag{G485}
```

**G486: 5:connection:4, bivector coefficient.**

```math
\begin{aligned}
&\frac{i}{4}\big(\bar\chi\gamma^{h}\gamma^{[ab]}\gamma^{e}\gamma^{d}{}_{h}\widehat R(Q)_{fg}\big)\,\eta_{cd}\,T_{e}{}^{f}\,\eta^{gc}\\
&=-\frac{i}{2}\big(\overline{\widehat R(Q)_{cd}}\gamma^{[ab]}\chi\big)\,T^{cd}\\
&+i\big(\overline{\widehat R(Q)^{[a}{}_{|c|}}\gamma^{b]d}\chi\big)\,T^{c}{}_{d}\\
&-i\big(\overline{\widehat R(Q)^{[a}{}_{|c|}}\chi\big)\,T^{|c|b]}
\end{aligned}\tag{G486}
```

**G487: 5:connection:4, scalar coefficient.**

```math
\begin{aligned}
&\frac{i}{2}\big(\bar\chi\gamma^{h}\gamma^{e}\gamma_{h}{}^{d}\widehat R(Q)_{fg}\big)\,\eta_{cd}\,T_{e}{}^{f}\,\eta^{gc}\\
&=-i\big(\overline{\widehat R(Q)_{cd}}\chi\big)\,T^{cd}
\end{aligned}\tag{G487}
```

**G488: 5:connection:4, vector coefficient.**

```math
\begin{aligned}
&\frac{i}{2}\big(\bar\chi\gamma^{h}\gamma^{a}\gamma^{e}\gamma_{h}{}^{d}\widehat R(Q)_{fg}\big)\,\eta_{cd}\,T_{e}{}^{f}\,\eta^{gc}\\
&=i\big(\overline{\widehat R(Q)_{cd}}\gamma^{a}\chi\big)\,T^{cd}\\
&+i\big(\overline{\widehat R(Q)^{a}{}_{c}}\gamma^{d}\chi\big)\,T^{c}{}_{d}
\end{aligned}\tag{G488}
```

**G489: 5:connection:4, bivector coefficient.**

```math
\begin{aligned}
&-\frac{i}{4}\big(\bar\chi\gamma^{h}\gamma^{[ab]}\gamma^{e}\gamma_{h}{}^{d}\widehat R(Q)_{fg}\big)\,\eta_{cd}\,T_{e}{}^{f}\,\eta^{gc}\\
&=-\frac{i}{2}\big(\overline{\widehat R(Q)_{cd}}\gamma^{[ab]}\chi\big)\,T^{cd}\\
&+i\big(\overline{\widehat R(Q)^{[a}{}_{|c|}}\gamma^{b]d}\chi\big)\,T^{c}{}_{d}\\
&-i\big(\overline{\widehat R(Q)^{[a}{}_{|c|}}\chi\big)\,T^{|c|b]}
\end{aligned}\tag{G489}
```

**G490: 5:connection:5, scalar coefficient.**

```math
\begin{aligned}
&6i\big(\bar\chi\gamma^{f}\gamma^{c}\widehat R(Q)_{de}\big)\,T_{c}{}^{d}\,\eta^{e}{}_{f}\\
&=12i\big(\overline{\widehat R(Q)_{cd}}\chi\big)\,T^{cd}
\end{aligned}\tag{G490}
```

**G491: 5:connection:5, vector coefficient.**

```math
\begin{aligned}
&6i\big(\bar\chi\gamma^{f}\gamma^{a}\gamma^{c}\widehat R(Q)_{de}\big)\,T_{c}{}^{d}\,\eta^{e}{}_{f}\\
&=-12i\big(\overline{\widehat R(Q)_{cd}}\gamma^{a}\chi\big)\,T^{cd}\\
&-12i\big(\overline{\widehat R(Q)^{a}{}_{c}}\gamma^{d}\chi\big)\,T^{c}{}_{d}
\end{aligned}\tag{G491}
```

**G492: 5:connection:5, bivector coefficient.**

```math
\begin{aligned}
&-3i\big(\bar\chi\gamma^{f}\gamma^{[ab]}\gamma^{c}\widehat R(Q)_{de}\big)\,T_{c}{}^{d}\,\eta^{e}{}_{f}\\
&=6i\big(\overline{\widehat R(Q)_{cd}}\gamma^{[ab]}\chi\big)\,T^{cd}\\
&-12i\big(\overline{\widehat R(Q)^{[a}{}_{|c|}}\gamma^{b]d}\chi\big)\,T^{c}{}_{d}\\
&+12i\big(\overline{\widehat R(Q)^{[a}{}_{|c|}}\chi\big)\,T^{|c|b]}
\end{aligned}\tag{G492}
```

**G493: 5:connection:6, scalar coefficient.**

```math
\begin{aligned}
&-\frac{i}{4}\big(\overline{\widehat R(Q)_{fg}}\gamma^{d}\gamma^{c}\widehat R(Q)^{g}{}_{e}\big)\,T_{cd}\,\eta^{ef}\\
&=-\frac{i}{4}\big(\overline{\widehat R(Q)_{ef}}\gamma^{cd}\widehat R(Q)^{ef}\big)\,T_{cd}
\end{aligned}\tag{G493}
```

**G494: 5:connection:6, vector coefficient.**

```math
\begin{aligned}
&-\frac{i}{4}\big(\overline{\widehat R(Q)_{fg}}\gamma^{d}\gamma^{a}\gamma^{c}\widehat R(Q)^{g}{}_{e}\big)\,T_{cd}\,\eta^{ef}\\
&=\frac{i}{4}\big(\overline{\widehat R(Q)_{ef}}\gamma^{acd}\widehat R(Q)^{ef}\big)\,T_{cd}\\
&=\frac{1}{8}\big(\overline{\widehat R(Q)_{gh}}\gamma^{cd}\widehat R(Q)^{gh}\big)\,\varepsilon_{cd}{}^{a}{}_{ef}\,T^{ef}
\end{aligned}\tag{G494}
```

**G495: 5:connection:6, bivector coefficient.**

```math
\begin{aligned}
&\frac{i}{8}\big(\overline{\widehat R(Q)_{fg}}\gamma^{d}\gamma^{[ab]}\gamma^{c}\widehat R(Q)^{g}{}_{e}\big)\,T_{cd}\,\eta^{ef}\\
&=0
\end{aligned}\tag{G495}
```

**G496: 5:connection:6, scalar coefficient.**

```math
\begin{aligned}
&\frac{i}{4}\big(\overline{\widehat R(Q)_{fd}}\gamma^{g}\gamma^{c}\widehat R(Q)_{ge}\big)\,T_{c}{}^{d}\,\eta^{ef}\\
&=\frac{i}{2}\big(\overline{\widehat R(Q)_{ec}}\widehat R(Q)^{e}{}_{d}\big)\,T^{cd}
\end{aligned}\tag{G496}
```

**G497: 5:connection:6, vector coefficient.**

```math
\begin{aligned}
&\frac{i}{4}\big(\overline{\widehat R(Q)_{fd}}\gamma^{g}\gamma^{a}\gamma^{c}\widehat R(Q)_{ge}\big)\,T_{c}{}^{d}\,\eta^{ef}\\
&=-\frac{i}{2}\big(\overline{\widehat R(Q)_{ec}}\gamma^{a}\widehat R(Q)^{e}{}_{d}\big)\,T^{cd}\\
&+\frac{i}{2}\big(\overline{\widehat R(Q)_{e}{}^{a}}\gamma^{c}\widehat R(Q)^{e}{}_{d}\big)\,T_{c}{}^{d}
\end{aligned}\tag{G497}
```

**G498: 5:connection:6, bivector coefficient.**

```math
\begin{aligned}
&-\frac{i}{8}\big(\overline{\widehat R(Q)_{fd}}\gamma^{g}\gamma^{[ab]}\gamma^{c}\widehat R(Q)_{ge}\big)\,T_{c}{}^{d}\,\eta^{ef}\\
&=\frac{i}{2}\big(\overline{\widehat R(Q)_{e}{}^{[a}}\gamma^{b]c}\widehat R(Q)^{e}{}_{d}\big)\,T_{c}{}^{d}\\
&+\frac{i}{2}\big(\overline{\widehat R(Q)_{d}{}^{[a}}\widehat R(Q)^{|d|}{}_{|c|}\big)\,T^{|c|b]}
\end{aligned}\tag{G498}
```

**G499: 5:connection:7, scalar coefficient.**

```math
\begin{aligned}
&-\frac{i}{4}\big(\overline{\widehat R(Q)_{dg}}\gamma^{f}\gamma^{c}\widehat R(Q)^{g}{}_{e}\big)\,T_{c}{}^{d}\,\eta^{e}{}_{f}\\
&=-\frac{i}{2}\big(\overline{\widehat R(Q)_{ec}}\widehat R(Q)^{e}{}_{d}\big)\,T^{cd}
\end{aligned}\tag{G499}
```

**G500: 5:connection:7, vector coefficient.**

```math
\begin{aligned}
&-\frac{i}{4}\big(\overline{\widehat R(Q)_{dg}}\gamma^{f}\gamma^{a}\gamma^{c}\widehat R(Q)^{g}{}_{e}\big)\,T_{c}{}^{d}\,\eta^{e}{}_{f}\\
&=\frac{i}{2}\big(\overline{\widehat R(Q)_{ec}}\gamma^{a}\widehat R(Q)^{e}{}_{d}\big)\,T^{cd}\\
&-\frac{i}{2}\big(\overline{\widehat R(Q)_{e}{}^{a}}\gamma^{c}\widehat R(Q)^{e}{}_{d}\big)\,T_{c}{}^{d}
\end{aligned}\tag{G500}
```

**G501: 5:connection:7, bivector coefficient.**

```math
\begin{aligned}
&\frac{i}{8}\big(\overline{\widehat R(Q)_{dg}}\gamma^{f}\gamma^{[ab]}\gamma^{c}\widehat R(Q)^{g}{}_{e}\big)\,T_{c}{}^{d}\,\eta^{e}{}_{f}\\
&=-\frac{i}{2}\big(\overline{\widehat R(Q)_{e}{}^{[a}}\gamma^{b]c}\widehat R(Q)^{e}{}_{d}\big)\,T_{c}{}^{d}\\
&-\frac{i}{2}\big(\overline{\widehat R(Q)_{d}{}^{[a}}\widehat R(Q)^{|d|}{}_{|c|}\big)\,T^{|c|b]}
\end{aligned}\tag{G501}
```

**G502: 5:connection:8, scalar coefficient.**

```math
\begin{aligned}
&-2i\big(\bar\chi\gamma^{g}\gamma^{e}\widehat R(Q)_{gf}\big)\,\eta_{cd}\,T_{e}{}^{d}\,\eta^{fc}\\
&=4i\big(\overline{\widehat R(Q)_{cd}}\chi\big)\,T^{cd}
\end{aligned}\tag{G502}
```

**G503: 5:connection:8, vector coefficient.**

```math
\begin{aligned}
&-2i\big(\bar\chi\gamma^{g}\gamma^{a}\gamma^{e}\widehat R(Q)_{gf}\big)\,\eta_{cd}\,T_{e}{}^{d}\,\eta^{fc}\\
&=-4i\big(\overline{\widehat R(Q)_{cd}}\gamma^{a}\chi\big)\,T^{cd}\\
&-4i\big(\overline{\widehat R(Q)^{a}{}_{c}}\gamma^{d}\chi\big)\,T^{c}{}_{d}
\end{aligned}\tag{G503}
```

**G504: 5:connection:8, bivector coefficient.**

```math
\begin{aligned}
&i\big(\bar\chi\gamma^{g}\gamma^{[ab]}\gamma^{e}\widehat R(Q)_{gf}\big)\,\eta_{cd}\,T_{e}{}^{d}\,\eta^{fc}\\
&=2i\big(\overline{\widehat R(Q)_{cd}}\gamma^{[ab]}\chi\big)\,T^{cd}\\
&-4i\big(\overline{\widehat R(Q)^{[a}{}_{|c|}}\gamma^{b]d}\chi\big)\,T^{c}{}_{d}\\
&+4i\big(\overline{\widehat R(Q)^{[a}{}_{|c|}}\chi\big)\,T^{|c|b]}
\end{aligned}\tag{G504}
```

**G505: 5:connection:8, scalar coefficient.**

```math
\begin{aligned}
&2i\big(\bar\chi\gamma^{f}\gamma^{e}\widehat R(Q)_{dg}\big)\,\eta_{c}{}^{d}\,T_{ef}\,\eta^{gc}\\
&=0
\end{aligned}\tag{G505}
```

**G506: 5:connection:8, vector coefficient.**

```math
\begin{aligned}
&2i\big(\bar\chi\gamma^{f}\gamma^{a}\gamma^{e}\widehat R(Q)_{dg}\big)\,\eta_{c}{}^{d}\,T_{ef}\,\eta^{gc}\\
&=0
\end{aligned}\tag{G506}
```

**G507: 5:connection:8, bivector coefficient.**

```math
\begin{aligned}
&-i\big(\bar\chi\gamma^{f}\gamma^{[ab]}\gamma^{e}\widehat R(Q)_{dg}\big)\,\eta_{c}{}^{d}\,T_{ef}\,\eta^{gc}\\
&=0
\end{aligned}\tag{G507}
```

**G508: 5:connection:9, scalar coefficient.**

```math
\begin{aligned}
&-\frac{i}{4}\big(\overline{\widehat R(Q)_{fg}}\gamma^{e}\gamma^{c}\widehat R(Q)_{d}{}^{g}\big)\,T_{c}{}^{d}\,\eta_{e}{}^{f}\\
&=0
\end{aligned}\tag{G508}
```

**G509: 5:connection:9, vector coefficient.**

```math
\begin{aligned}
&-\frac{i}{4}\big(\overline{\widehat R(Q)_{fg}}\gamma^{e}\gamma^{a}\gamma^{c}\widehat R(Q)_{d}{}^{g}\big)\,T_{c}{}^{d}\,\eta_{e}{}^{f}\\
&=0
\end{aligned}\tag{G509}
```

**G510: 5:connection:9, bivector coefficient.**

```math
\begin{aligned}
&\frac{i}{8}\big(\overline{\widehat R(Q)_{fg}}\gamma^{e}\gamma^{[ab]}\gamma^{c}\widehat R(Q)_{d}{}^{g}\big)\,T_{c}{}^{d}\,\eta_{e}{}^{f}\\
&=0
\end{aligned}\tag{G510}
```

**G511: 5:connection:9, scalar coefficient.**

```math
\begin{aligned}
&\frac{i}{4}\big(\overline{\widehat R(Q)_{fe}}\gamma^{g}\gamma^{c}\widehat R(Q)_{dg}\big)\,T_{c}{}^{d}\,\eta^{ef}\\
&=0
\end{aligned}\tag{G511}
```

**G512: 5:connection:9, vector coefficient.**

```math
\begin{aligned}
&\frac{i}{4}\big(\overline{\widehat R(Q)_{fe}}\gamma^{g}\gamma^{a}\gamma^{c}\widehat R(Q)_{dg}\big)\,T_{c}{}^{d}\,\eta^{ef}\\
&=0
\end{aligned}\tag{G512}
```

**G513: 5:connection:9, bivector coefficient.**

```math
\begin{aligned}
&-\frac{i}{8}\big(\overline{\widehat R(Q)_{fe}}\gamma^{g}\gamma^{[ab]}\gamma^{c}\widehat R(Q)_{dg}\big)\,T_{c}{}^{d}\,\eta^{ef}\\
&=0
\end{aligned}\tag{G513}
```

**G514: 5:connection:10, scalar coefficient.**

```math
\begin{aligned}
&-\frac{i}{4}\big(\overline{\widehat R(Q)_{eg}}\gamma^{f}\gamma^{c}\widehat R(Q)_{d}{}^{g}\big)\,T_{c}{}^{d}\,\eta^{e}{}_{f}\\
&=0
\end{aligned}\tag{G514}
```

**G515: 5:connection:10, vector coefficient.**

```math
\begin{aligned}
&-\frac{i}{4}\big(\overline{\widehat R(Q)_{eg}}\gamma^{f}\gamma^{a}\gamma^{c}\widehat R(Q)_{d}{}^{g}\big)\,T_{c}{}^{d}\,\eta^{e}{}_{f}\\
&=0
\end{aligned}\tag{G515}
```

**G516: 5:connection:10, bivector coefficient.**

```math
\begin{aligned}
&\frac{i}{8}\big(\overline{\widehat R(Q)_{eg}}\gamma^{f}\gamma^{[ab]}\gamma^{c}\widehat R(Q)_{d}{}^{g}\big)\,T_{c}{}^{d}\,\eta^{e}{}_{f}\\
&=0
\end{aligned}\tag{G516}
```

**G517: 5:connection:11, scalar coefficient.**

```math
\begin{aligned}
&-2i\big(\bar\chi\gamma^{g}\gamma^{e}\widehat R(Q)_{fg}\big)\,\eta_{cd}\,T_{e}{}^{f}\,\eta^{dc}\\
&=-20i\big(\overline{\widehat R(Q)_{cd}}\chi\big)\,T^{cd}
\end{aligned}\tag{G517}
```

**G518: 5:connection:11, vector coefficient.**

```math
\begin{aligned}
&-2i\big(\bar\chi\gamma^{g}\gamma^{a}\gamma^{e}\widehat R(Q)_{fg}\big)\,\eta_{cd}\,T_{e}{}^{f}\,\eta^{dc}\\
&=20i\big(\overline{\widehat R(Q)_{cd}}\gamma^{a}\chi\big)\,T^{cd}\\
&+20i\big(\overline{\widehat R(Q)^{a}{}_{c}}\gamma^{d}\chi\big)\,T^{c}{}_{d}
\end{aligned}\tag{G518}
```

**G519: 5:connection:11, bivector coefficient.**

```math
\begin{aligned}
&i\big(\bar\chi\gamma^{g}\gamma^{[ab]}\gamma^{e}\widehat R(Q)_{fg}\big)\,\eta_{cd}\,T_{e}{}^{f}\,\eta^{dc}\\
&=-10i\big(\overline{\widehat R(Q)_{cd}}\gamma^{[ab]}\chi\big)\,T^{cd}\\
&+20i\big(\overline{\widehat R(Q)^{[a}{}_{|c|}}\gamma^{b]d}\chi\big)\,T^{c}{}_{d}\\
&-20i\big(\overline{\widehat R(Q)^{[a}{}_{|c|}}\chi\big)\,T^{|c|b]}
\end{aligned}\tag{G519}
```

**G520: 5:connection:11, scalar coefficient.**

```math
\begin{aligned}
&2i\big(\bar\chi\gamma^{g}\gamma^{e}\widehat R(Q)_{fd}\big)\,\eta_{c}{}^{d}\,T_{e}{}^{f}\,\eta_{g}{}^{c}\\
&=4i\big(\overline{\widehat R(Q)_{cd}}\chi\big)\,T^{cd}
\end{aligned}\tag{G520}
```

**G521: 5:connection:11, vector coefficient.**

```math
\begin{aligned}
&2i\big(\bar\chi\gamma^{g}\gamma^{a}\gamma^{e}\widehat R(Q)_{fd}\big)\,\eta_{c}{}^{d}\,T_{e}{}^{f}\,\eta_{g}{}^{c}\\
&=-4i\big(\overline{\widehat R(Q)_{cd}}\gamma^{a}\chi\big)\,T^{cd}\\
&-4i\big(\overline{\widehat R(Q)^{a}{}_{c}}\gamma^{d}\chi\big)\,T^{c}{}_{d}
\end{aligned}\tag{G521}
```

**G522: 5:connection:11, bivector coefficient.**

```math
\begin{aligned}
&-i\big(\bar\chi\gamma^{g}\gamma^{[ab]}\gamma^{e}\widehat R(Q)_{fd}\big)\,\eta_{c}{}^{d}\,T_{e}{}^{f}\,\eta_{g}{}^{c}\\
&=2i\big(\overline{\widehat R(Q)_{cd}}\gamma^{[ab]}\chi\big)\,T^{cd}\\
&-4i\big(\overline{\widehat R(Q)^{[a}{}_{|c|}}\gamma^{b]d}\chi\big)\,T^{c}{}_{d}\\
&+4i\big(\overline{\widehat R(Q)^{[a}{}_{|c|}}\chi\big)\,T^{|c|b]}
\end{aligned}\tag{G522}
```

#### Block 6

The original spinor term is $`-\frac{64i}{3}\gamma^{ab}\gamma^c\mathcal D_aT_{bc}\chi^i`$.

**G523: chi1, whole coefficient matrix.**

```math
\begin{aligned}
&-\frac{16i}{3}D\,(\mathcal D_{c}T_{de})\,\gamma^{cd}\gamma^{e}\\
&=-\frac{16i}{3}D\,(\mathcal D_{c}T_{de})\,\gamma^{cde}\\
&+\frac{16i}{3}D\,(\mathcal D_{c}T_{d}{}^{c})\,\gamma^{d}\\
&=-\frac{8}{3}D\,\varepsilon_{cdefg}\,(\mathcal D^{e}T^{fg})\,\gamma^{cd}\\
&+\frac{16i}{3}D\,(\mathcal D_{c}T_{d}{}^{c})\,\gamma^{d}
\end{aligned}\tag{G523}
```

**G524: chi3, whole coefficient matrix.**

```math
\begin{aligned}
&\frac{8}{3}(\mathcal D_{c}T_{de})\,(\mathcal D_{f}T_{gh})\,\gamma^{fg}\gamma^{h}\gamma^{de}\gamma^{c}\\
&=\frac{8}{3}(\mathcal D_{c}T_{de})\,(\mathcal D^{c}T_{fg})\,\gamma^{defg}\\
&+\frac{32}{3}(\mathcal D_{c}T_{de})\,(\mathcal D^{e}T_{fg})\,\gamma^{cdfg}\\
&+8(\mathcal D_{c}T_{de})\,(\mathcal D_{f}T_{g}{}^{f})\,\gamma^{cdeg}\\
&+\frac{8}{3}(\mathcal D_{c}T_{de})\,(\mathcal D_{f}T^{cf})\,\gamma^{de}\\
&+\frac{32}{3}(\mathcal D_{c}T_{de})\,(\mathcal D_{f}T_{g}{}^{e})\,\gamma^{cdfg}\\
&+\frac{16}{3}(\mathcal D_{c}T_{de})\,(\mathcal D_{f}T^{ef})\,\gamma^{cd}\\
&+\frac{32}{3}(\mathcal D_{c}T_{de})\,(\mathcal D^{d}T^{ce})\\
&-\frac{16}{3}(\mathcal D_{c}T_{de})\,(\mathcal D^{c}T^{de})\\
&+\frac{16}{3}(\mathcal D_{c}T^{c}{}_{d})\,(\mathcal D_{e}T^{de})\\
&=\frac{8i}{3}\varepsilon_{cdefg}\,(\mathcal D_{h}T^{de})\,(\mathcal D^{h}T^{fg})\,\gamma^{c}\\
&+\frac{32i}{3}\varepsilon_{cdefg}\,(\mathcal D^{d}T^{e}{}_{h})\,(\mathcal D^{h}T^{fg})\,\gamma^{c}\\
&+8i\varepsilon_{cdefg}\,(\mathcal D^{d}T^{ef})\,(\mathcal D_{h}T^{gh})\,\gamma^{c}\\
&+\frac{8}{3}(\mathcal D_{c}T_{de})\,(\mathcal D_{f}T^{cf})\,\gamma^{de}\\
&+\frac{32i}{3}\varepsilon_{cdefg}\,(\mathcal D^{d}T^{e}{}_{h})\,(\mathcal D^{f}T^{gh})\,\gamma^{c}\\
&+\frac{16}{3}(\mathcal D_{c}T_{de})\,(\mathcal D_{f}T^{ef})\,\gamma^{cd}\\
&+\frac{32}{3}(\mathcal D_{c}T_{de})\,(\mathcal D^{d}T^{ce})\\
&-\frac{16}{3}(\mathcal D_{c}T_{de})\,(\mathcal D^{c}T^{de})\\
&+\frac{16}{3}(\mathcal D_{c}T^{c}{}_{d})\,(\mathcal D_{e}T^{de})
\end{aligned}\tag{G524}
```

**G525: chi4, whole coefficient matrix.**

```math
\begin{aligned}
&-\frac{8}{3}(\mathcal D_{c}T_{d}{}^{c})\,(\mathcal D_{e}T_{fg})\,\gamma^{ef}\gamma^{g}\gamma^{d}\\
&=-\frac{8}{3}(\mathcal D_{c}T_{de})\,(\mathcal D_{f}T_{g}{}^{f})\,\gamma^{cdeg}\\
&-\frac{8}{3}(\mathcal D_{c}T_{de})\,(\mathcal D_{f}T^{cf})\,\gamma^{de}\\
&-\frac{16}{3}(\mathcal D_{c}T_{de})\,(\mathcal D_{f}T^{ef})\,\gamma^{cd}\\
&-\frac{8}{3}(\mathcal D_{c}T^{c}{}_{d})\,(\mathcal D_{e}T^{de})\\
&=-\frac{8i}{3}\varepsilon_{cdefg}\,(\mathcal D^{d}T^{ef})\,(\mathcal D_{h}T^{gh})\,\gamma^{c}\\
&-\frac{8}{3}(\mathcal D_{c}T_{de})\,(\mathcal D_{f}T^{cf})\,\gamma^{de}\\
&-\frac{16}{3}(\mathcal D_{c}T_{de})\,(\mathcal D_{f}T^{ef})\,\gamma^{cd}\\
&-\frac{8}{3}(\mathcal D_{c}T^{c}{}_{d})\,(\mathcal D_{e}T^{de})
\end{aligned}\tag{G525}
```

**G526: chi5, whole coefficient matrix.**

```math
\begin{aligned}
&\frac{16i}{3}T_{cd}\,T_{ef}\,(\mathcal D_{g}T_{hj})\,\gamma^{gh}\gamma^{j}\gamma^{cdef}\\
&=-16iT_{cd}\,T_{ef}\,(\mathcal D^{f}T_{gh})\,\gamma^{cdegh}\\
&+\frac{128i}{3}T_{cd}\,T_{ef}\,(\mathcal D^{e}T_{g}{}^{f})\,\gamma^{cdg}\\
&-32iT_{cd}\,T_{ef}\,(\mathcal D_{g}T_{h}{}^{f})\,\gamma^{cdegh}\\
&-\frac{64i}{3}T_{cd}\,T_{ef}\,(\mathcal D_{g}T^{ef})\,\gamma^{cdg}\\
&-\frac{256i}{3}T_{cd}\,T_{ef}\,(\mathcal D^{d}T_{g}{}^{f})\,\gamma^{ceg}\\
&+\frac{128i}{3}T_{cd}\,T_{ef}\,(\mathcal D^{d}T^{ef})\,\gamma^{c}\\
&+\frac{128i}{3}T_{cd}\,T_{ef}\,(\mathcal D_{g}T^{df})\,\gamma^{ceg}\\
&-\frac{256i}{3}T_{cd}\,T_{ef}\,(\mathcal D^{e}T^{df})\,\gamma^{c}\\
&-\frac{16i}{3}T_{cd}\,T_{ef}\,(\mathcal D_{g}T_{h}{}^{g})\,\gamma^{cdefh}\\
&+\frac{64i}{3}T_{cd}\,T_{ef}\,(\mathcal D_{g}T^{fg})\,\gamma^{cde}\\
&=\frac{16}{3}\varepsilon_{cdefg}\,T^{cd}\,T^{ef}\,(\mathcal D_{h}T^{gh})\\
&+\frac{64}{3}\varepsilon_{cdefg}\,T^{ef}\,T_{hj}\,(\mathcal D^{h}T^{gj})\,\gamma^{cd}\\
&-\frac{32}{3}\varepsilon_{cdefg}\,T^{ef}\,T_{hj}\,(\mathcal D^{g}T^{hj})\,\gamma^{cd}\\
&-\frac{128}{3}\varepsilon_{cdefg}\,T^{e}{}_{h}\,T^{f}{}_{j}\,(\mathcal D^{h}T^{gj})\,\gamma^{cd}\\
&+\frac{128i}{3}T_{cd}\,T_{ef}\,(\mathcal D^{d}T^{ef})\,\gamma^{c}\\
&+\frac{64}{3}\varepsilon_{cdefg}\,T^{e}{}_{h}\,T^{f}{}_{j}\,(\mathcal D^{g}T^{hj})\,\gamma^{cd}\\
&-\frac{256i}{3}T_{cd}\,T_{ef}\,(\mathcal D^{e}T^{df})\,\gamma^{c}\\
&+\frac{32}{3}\varepsilon_{cdefg}\,T^{ef}\,T^{g}{}_{h}\,(\mathcal D_{j}T^{hj})\,\gamma^{cd}
\end{aligned}\tag{G526}
```

**G527: chi6, whole coefficient matrix.**

```math
\begin{aligned}
&-\frac{32i}{9}T_{cd}\,T^{cd}\,(\mathcal D_{e}T_{fg})\,\gamma^{ef}\gamma^{g}\\
&=-\frac{32i}{9}T_{cd}\,T^{cd}\,(\mathcal D_{e}T_{fg})\,\gamma^{efg}\\
&+\frac{32i}{9}T_{cd}\,T^{cd}\,(\mathcal D_{e}T_{f}{}^{e})\,\gamma^{f}\\
&=-\frac{16}{9}\varepsilon_{cdefg}\,T_{hj}\,T^{hj}\,(\mathcal D^{e}T^{fg})\,\gamma^{cd}\\
&+\frac{32i}{9}T_{cd}\,T^{cd}\,(\mathcal D_{e}T_{f}{}^{e})\,\gamma^{f}
\end{aligned}\tag{G527}
```

**G528: 6:DT:1, scalar coefficient.**

```math
\begin{aligned}
&-\frac{4}{3}\big(\overline{\mathcal D_{e}\chi}\gamma^{cd}\gamma^{e}{}_{c}\gamma_{d}\chi\big)\\
&=-\frac{32}{3}\big(\bar\chi\gamma^{c}\mathcal D_{c}\chi\big)
\end{aligned}\tag{G528}
```

**G529: 6:DT:1, vector coefficient.**

```math
\begin{aligned}
&-\frac{4}{3}\big(\overline{\mathcal D_{e}\chi}\gamma^{cd}\gamma^{a}\gamma^{e}{}_{c}\gamma_{d}\chi\big)\\
&=\frac{8}{3}\big(\bar\chi\gamma^{ca}\mathcal D_{c}\chi\big)\\
&-\frac{64}{3}\big(\bar\chi\mathcal D^{a}\chi\big)
\end{aligned}\tag{G529}
```

**G530: 6:DT:1, bivector coefficient.**

```math
\begin{aligned}
&\frac{2}{3}\big(\overline{\mathcal D_{e}\chi}\gamma^{cd}\gamma^{[ab]}\gamma^{e}{}_{c}\gamma_{d}\chi\big)\\
&=\frac{8}{3}\big(\bar\chi\gamma^{c[ab]}\mathcal D_{c}\chi\big)\\
&+\frac{8}{3}\big(\bar\chi\gamma^{[a}\mathcal D^{b]}\chi\big)\\
&=-\frac{4i}{3}\big(\bar\chi\gamma^{cd}\mathcal D_{e}\chi\big)\,\varepsilon_{cd}{}^{e[ab]}\\
&+\frac{8}{3}\big(\bar\chi\gamma^{[a}\mathcal D^{b]}\chi\big)
\end{aligned}\tag{G530}
```

**G531: 6:DT:2, scalar coefficient.**

```math
\begin{aligned}
&-\frac{1}{4}\big(\overline{\mathcal D_{c}\widehat R(Q)_{de}}\gamma^{cd}\gamma^{e}\chi\big)\\
&=0
\end{aligned}\tag{G531}
```

**G532: 6:DT:2, vector coefficient.**

```math
\begin{aligned}
&-\frac{1}{4}\big(\overline{\mathcal D_{c}\widehat R(Q)_{de}}\gamma^{a}\gamma^{cd}\gamma^{e}\chi\big)\\
&=\frac{3}{2}\big(\bar\chi\mathcal D_{c}\widehat R(Q)^{ca}\big)
\end{aligned}\tag{G532}
```

**G533: 6:DT:2, bivector coefficient.**

```math
\begin{aligned}
&\frac{1}{8}\big(\overline{\mathcal D_{c}\widehat R(Q)_{de}}\gamma^{[ab]}\gamma^{cd}\gamma^{e}\chi\big)\\
&=-\frac{3}{2}\big(\bar\chi\gamma^{[a}\mathcal D_{|c|}\widehat R(Q)^{|c|b]}\big)\\
&+\big(\bar\chi\gamma^{c}\mathcal D_{c}\widehat R(Q)^{[ab]}\big)
\end{aligned}\tag{G533}
```

**G534: 6:DT:3, scalar coefficient.**

```math
\begin{aligned}
&\frac{4i}{3}\big(\bar\chi\gamma^{ef}\gamma^{cd}\gamma^{g}\gamma_{ge}\gamma_{f}\chi\big)\,T_{cd}\\
&=\frac{64i}{3}\big(\bar\chi\gamma^{cd}\chi\big)\,T_{cd}
\end{aligned}\tag{G534}
```

**G535: 6:DT:3, vector coefficient.**

```math
\begin{aligned}
&\frac{4i}{3}\big(\bar\chi\gamma^{ef}\gamma^{cd}\gamma^{g}\gamma^{a}\gamma_{ge}\gamma_{f}\chi\big)\,T_{cd}\\
&=-\frac{32i}{3}\big(\bar\chi\gamma^{acd}\chi\big)\,T_{cd}\\
&=-\frac{16}{3}\big(\bar\chi\gamma^{cd}\chi\big)\,\varepsilon_{cd}{}^{a}{}_{ef}\,T^{ef}
\end{aligned}\tag{G535}
```

**G536: 6:DT:3, bivector coefficient.**

```math
\begin{aligned}
&-\frac{2i}{3}\big(\bar\chi\gamma^{ef}\gamma^{cd}\gamma^{g}\gamma^{[ab]}\gamma_{ge}\gamma_{f}\chi\big)\,T_{cd}\\
&=-\frac{32i}{3}\big(\bar\chi\gamma^{[a|c|}\chi\big)\,T_{|c|}{}^{b]}
\end{aligned}\tag{G536}
```

**G537: 6:DT:4, scalar coefficient.**

```math
\begin{aligned}
&\frac{i}{4}\big(\overline{\widehat R(Q)_{fg}}\gamma^{cd}\gamma^{e}\gamma_{e}{}^{f}\gamma^{g}\chi\big)\,T_{cd}\\
&=-8i\big(\overline{\widehat R(Q)_{cd}}\chi\big)\,T^{cd}
\end{aligned}\tag{G537}
```

**G538: 6:DT:4, vector coefficient.**

```math
\begin{aligned}
&\frac{i}{4}\big(\overline{\widehat R(Q)_{fg}}\gamma^{cd}\gamma^{e}\gamma^{a}\gamma_{e}{}^{f}\gamma^{g}\chi\big)\,T_{cd}\\
&=10i\big(\overline{\widehat R(Q)^{a}{}_{c}}\gamma^{d}\chi\big)\,T^{c}{}_{d}\\
&+4i\big(\overline{\widehat R(Q)_{cd}}\gamma^{a}\chi\big)\,T^{cd}
\end{aligned}\tag{G538}
```

**G539: 6:DT:4, bivector coefficient.**

```math
\begin{aligned}
&-\frac{i}{8}\big(\overline{\widehat R(Q)_{fg}}\gamma^{cd}\gamma^{e}\gamma^{[ab]}\gamma_{e}{}^{f}\gamma^{g}\chi\big)\,T_{cd}\\
&=i\big(\overline{\widehat R(Q)^{[ab]}}\gamma^{cd}\chi\big)\,T_{cd}\\
&-2i\big(\overline{\widehat R(Q)^{[a}{}_{|c|}}\gamma^{b]d}\chi\big)\,T^{c}{}_{d}\\
&+2i\big(\overline{\widehat R(Q)^{[a}{}_{|c|}}\chi\big)\,T^{|c|b]}
\end{aligned}\tag{G539}
```

**G540: 6:DT:5, scalar coefficient.**

```math
\begin{aligned}
&-\frac{16i}{3}\big(\bar\chi\gamma^{e}\gamma_{e}{}^{c}\gamma^{d}\chi\big)\,T_{cd}\\
&=-\frac{64i}{3}\big(\bar\chi\gamma^{cd}\chi\big)\,T_{cd}
\end{aligned}\tag{G540}
```

**G541: 6:DT:5, vector coefficient.**

```math
\begin{aligned}
&-\frac{16i}{3}\big(\bar\chi\gamma^{e}\gamma^{a}\gamma_{e}{}^{c}\gamma^{d}\chi\big)\,T_{cd}\\
&=\frac{32i}{3}\big(\bar\chi\gamma^{acd}\chi\big)\,T_{cd}\\
&=\frac{16}{3}\big(\bar\chi\gamma^{cd}\chi\big)\,\varepsilon_{cd}{}^{a}{}_{ef}\,T^{ef}
\end{aligned}\tag{G541}
```

**G542: 6:DT:5, bivector coefficient.**

```math
\begin{aligned}
&\frac{8i}{3}\big(\bar\chi\gamma^{e}\gamma^{[ab]}\gamma_{e}{}^{c}\gamma^{d}\chi\big)\,T_{cd}\\
&=-\frac{32i}{3}\big(\bar\chi\gamma^{[a|c|}\chi\big)\,T_{|c|}{}^{b]}
\end{aligned}\tag{G542}
```

**G543: 6:DT:6, scalar coefficient.**

```math
\begin{aligned}
&\frac{2i}{3}\big(\overline{\widehat R(Q)_{fc}}\gamma^{e}\gamma^{f}{}_{e}\gamma^{d}\chi\big)\,T^{c}{}_{d}\\
&=0
\end{aligned}\tag{G543}
```

**G544: 6:DT:6, vector coefficient.**

```math
\begin{aligned}
&\frac{2i}{3}\big(\overline{\widehat R(Q)_{fc}}\gamma^{e}\gamma^{a}\gamma^{f}{}_{e}\gamma^{d}\chi\big)\,T^{c}{}_{d}\\
&=4i\big(\overline{\widehat R(Q)^{a}{}_{c}}\gamma^{d}\chi\big)\,T^{c}{}_{d}
\end{aligned}\tag{G544}
```

**G545: 6:DT:6, bivector coefficient.**

```math
\begin{aligned}
&-\frac{i}{3}\big(\overline{\widehat R(Q)_{fc}}\gamma^{e}\gamma^{[ab]}\gamma^{f}{}_{e}\gamma^{d}\chi\big)\,T^{c}{}_{d}\\
&=-\frac{4i}{3}\big(\overline{\widehat R(Q)^{[a}{}_{|c|}}\gamma^{b]d}\chi\big)\,T^{c}{}_{d}\\
&-\frac{4i}{3}\big(\overline{\widehat R(Q)^{[a}{}_{|c|}}\chi\big)\,T^{|c|b]}
\end{aligned}\tag{G545}
```

**G546: 6:DT:6, scalar coefficient.**

```math
\begin{aligned}
&-\frac{2i}{3}\big(\overline{\widehat R(Q)_{ef}}\gamma^{c}\gamma^{ef}\gamma^{d}\chi\big)\,T_{cd}\\
&=0
\end{aligned}\tag{G546}
```

**G547: 6:DT:6, vector coefficient.**

```math
\begin{aligned}
&-\frac{2i}{3}\big(\overline{\widehat R(Q)_{ef}}\gamma^{c}\gamma^{a}\gamma^{ef}\gamma^{d}\chi\big)\,T_{cd}\\
&=-\frac{16i}{3}\big(\overline{\widehat R(Q)^{a}{}_{c}}\gamma^{d}\chi\big)\,T^{c}{}_{d}
\end{aligned}\tag{G547}
```

**G548: 6:DT:6, bivector coefficient.**

```math
\begin{aligned}
&\frac{i}{3}\big(\overline{\widehat R(Q)_{ef}}\gamma^{c}\gamma^{[ab]}\gamma^{ef}\gamma^{d}\chi\big)\,T_{cd}\\
&=\frac{2i}{3}\big(\overline{\widehat R(Q)_{cd}}\gamma^{[ab]}\chi\big)\,T^{cd}\\
&+\frac{8i}{3}\big(\overline{\widehat R(Q)^{[a}{}_{|c|}}\gamma^{b]d}\chi\big)\,T^{c}{}_{d}\\
&+\frac{16i}{3}\big(\overline{\widehat R(Q)^{[a}{}_{|c|}}\chi\big)\,T^{|c|b]}\\
&-2i\big(\overline{\widehat R(Q)^{[ab]}}\gamma^{cd}\chi\big)\,T_{cd}
\end{aligned}\tag{G548}
```

**G549: 6:DT:7, scalar coefficient.**

```math
\begin{aligned}
&\frac{2i}{3}\big(\overline{\widehat R(Q)_{fc}}\gamma^{e}\gamma_{e}{}^{f}\gamma^{d}\chi\big)\,T^{c}{}_{d}\\
&=0
\end{aligned}\tag{G549}
```

**G550: 6:DT:7, vector coefficient.**

```math
\begin{aligned}
&\frac{2i}{3}\big(\overline{\widehat R(Q)_{fc}}\gamma^{e}\gamma^{a}\gamma_{e}{}^{f}\gamma^{d}\chi\big)\,T^{c}{}_{d}\\
&=-4i\big(\overline{\widehat R(Q)^{a}{}_{c}}\gamma^{d}\chi\big)\,T^{c}{}_{d}
\end{aligned}\tag{G550}
```

**G551: 6:DT:7, bivector coefficient.**

```math
\begin{aligned}
&-\frac{i}{3}\big(\overline{\widehat R(Q)_{fc}}\gamma^{e}\gamma^{[ab]}\gamma_{e}{}^{f}\gamma^{d}\chi\big)\,T^{c}{}_{d}\\
&=\frac{4i}{3}\big(\overline{\widehat R(Q)^{[a}{}_{|c|}}\gamma^{b]d}\chi\big)\,T^{c}{}_{d}\\
&+\frac{4i}{3}\big(\overline{\widehat R(Q)^{[a}{}_{|c|}}\chi\big)\,T^{|c|b]}
\end{aligned}\tag{G551}
```

**G552: 6:DT:8, scalar coefficient.**

```math
\begin{aligned}
&\frac{16i}{3}\big(\bar\chi\gamma^{e}\gamma^{cd}\gamma^{f}\chi\big)\,\eta_{cd}\,T_{ef}\\
&=0
\end{aligned}\tag{G552}
```

**G553: 6:DT:8, vector coefficient.**

```math
\begin{aligned}
&\frac{16i}{3}\big(\bar\chi\gamma^{e}\gamma^{a}\gamma^{cd}\gamma^{f}\chi\big)\,\eta_{cd}\,T_{ef}\\
&=0
\end{aligned}\tag{G553}
```

**G554: 6:DT:8, bivector coefficient.**

```math
\begin{aligned}
&-\frac{8i}{3}\big(\bar\chi\gamma^{e}\gamma^{[ab]}\gamma^{cd}\gamma^{f}\chi\big)\,\eta_{cd}\,T_{ef}\\
&=0
\end{aligned}\tag{G554}
```

**G555: 6:DT:8, scalar coefficient.**

```math
\begin{aligned}
&-\frac{16i}{3}\big(\bar\chi\gamma^{f}\gamma^{c}{}_{f}\gamma^{e}\chi\big)\,\eta_{cd}\,T^{d}{}_{e}\\
&=\frac{64i}{3}\big(\bar\chi\gamma^{cd}\chi\big)\,T_{cd}
\end{aligned}\tag{G555}
```

**G556: 6:DT:8, vector coefficient.**

```math
\begin{aligned}
&-\frac{16i}{3}\big(\bar\chi\gamma^{f}\gamma^{a}\gamma^{c}{}_{f}\gamma^{e}\chi\big)\,\eta_{cd}\,T^{d}{}_{e}\\
&=-\frac{32i}{3}\big(\bar\chi\gamma^{acd}\chi\big)\,T_{cd}\\
&=-\frac{16}{3}\big(\bar\chi\gamma^{cd}\chi\big)\,\varepsilon_{cd}{}^{a}{}_{ef}\,T^{ef}
\end{aligned}\tag{G556}
```

**G557: 6:DT:8, bivector coefficient.**

```math
\begin{aligned}
&\frac{8i}{3}\big(\bar\chi\gamma^{f}\gamma^{[ab]}\gamma^{c}{}_{f}\gamma^{e}\chi\big)\,\eta_{cd}\,T^{d}{}_{e}\\
&=\frac{32i}{3}\big(\bar\chi\gamma^{[a|c|}\chi\big)\,T_{|c|}{}^{b]}
\end{aligned}\tag{G557}
```

**G558: 6:DT:9, scalar coefficient.**

```math
\begin{aligned}
&\frac{2i}{3}\big(\overline{\widehat R(Q)_{fd}}\gamma^{e}\gamma^{fc}\gamma_{e}\chi\big)\,T_{c}{}^{d}\\
&=-\frac{2i}{3}\big(\overline{\widehat R(Q)_{cd}}\chi\big)\,T^{cd}
\end{aligned}\tag{G558}
```

**G559: 6:DT:9, vector coefficient.**

```math
\begin{aligned}
&\frac{2i}{3}\big(\overline{\widehat R(Q)_{fd}}\gamma^{e}\gamma^{a}\gamma^{fc}\gamma_{e}\chi\big)\,T_{c}{}^{d}\\
&=-\frac{2i}{3}\big(\overline{\widehat R(Q)_{cd}}\gamma^{a}\chi\big)\,T^{cd}\\
&+\frac{4i}{3}\big(\overline{\widehat R(Q)^{a}{}_{c}}\gamma^{d}\chi\big)\,T^{c}{}_{d}
\end{aligned}\tag{G559}
```

**G560: 6:DT:9, bivector coefficient.**

```math
\begin{aligned}
&-\frac{i}{3}\big(\overline{\widehat R(Q)_{fd}}\gamma^{e}\gamma^{[ab]}\gamma^{fc}\gamma_{e}\chi\big)\,T_{c}{}^{d}\\
&=-i\big(\overline{\widehat R(Q)_{cd}}\gamma^{[ab]}\chi\big)\,T^{cd}\\
&+\frac{4i}{3}\big(\overline{\widehat R(Q)^{[a}{}_{|c|}}\gamma^{b]d}\chi\big)\,T^{c}{}_{d}\\
&-4i\big(\overline{\widehat R(Q)^{[a}{}_{|c|}}\chi\big)\,T^{|c|b]}
\end{aligned}\tag{G560}
```

**G561: 6:DT:9, scalar coefficient.**

```math
\begin{aligned}
&-\frac{2i}{3}\big(\overline{\widehat R(Q)_{ef}}\gamma^{d}\gamma^{ec}\gamma^{f}\chi\big)\,T_{cd}\\
&=4i\big(\overline{\widehat R(Q)_{cd}}\chi\big)\,T^{cd}
\end{aligned}\tag{G561}
```

**G562: 6:DT:9, vector coefficient.**

```math
\begin{aligned}
&-\frac{2i}{3}\big(\overline{\widehat R(Q)_{ef}}\gamma^{d}\gamma^{a}\gamma^{ec}\gamma^{f}\chi\big)\,T_{cd}\\
&=-4i\big(\overline{\widehat R(Q)_{cd}}\gamma^{a}\chi\big)\,T^{cd}\\
&-\frac{28i}{3}\big(\overline{\widehat R(Q)^{a}{}_{c}}\gamma^{d}\chi\big)\,T^{c}{}_{d}
\end{aligned}\tag{G562}
```

**G563: 6:DT:9, bivector coefficient.**

```math
\begin{aligned}
&\frac{i}{3}\big(\overline{\widehat R(Q)_{ef}}\gamma^{d}\gamma^{[ab]}\gamma^{ec}\gamma^{f}\chi\big)\,T_{cd}\\
&=-\frac{4i}{3}\big(\overline{\widehat R(Q)_{cd}}\gamma^{[ab]}\chi\big)\,T^{cd}\\
&+\frac{20i}{3}\big(\overline{\widehat R(Q)^{[a}{}_{|c|}}\gamma^{b]d}\chi\big)\,T^{c}{}_{d}\\
&-2i\big(\overline{\widehat R(Q)^{[ab]}}\gamma^{cd}\chi\big)\,T_{cd}\\
&+\frac{4i}{3}\big(\overline{\widehat R(Q)^{[a}{}_{|c|}}\chi\big)\,T^{|c|b]}
\end{aligned}\tag{G563}
```

**G564: 6:DT:10, scalar coefficient.**

```math
\begin{aligned}
&\frac{2i}{3}\big(\overline{\widehat R(Q)_{fd}}\gamma^{e}\gamma_{e}{}^{c}\gamma^{f}\chi\big)\,T_{c}{}^{d}\\
&=\frac{16i}{3}\big(\overline{\widehat R(Q)_{cd}}\chi\big)\,T^{cd}
\end{aligned}\tag{G564}
```

**G565: 6:DT:10, vector coefficient.**

```math
\begin{aligned}
&\frac{2i}{3}\big(\overline{\widehat R(Q)_{fd}}\gamma^{e}\gamma^{a}\gamma_{e}{}^{c}\gamma^{f}\chi\big)\,T_{c}{}^{d}\\
&=-\frac{8i}{3}\big(\overline{\widehat R(Q)_{cd}}\gamma^{a}\chi\big)\,T^{cd}\\
&-\frac{8i}{3}\big(\overline{\widehat R(Q)^{a}{}_{c}}\gamma^{d}\chi\big)\,T^{c}{}_{d}
\end{aligned}\tag{G565}
```

**G566: 6:DT:10, bivector coefficient.**

```math
\begin{aligned}
&-\frac{i}{3}\big(\overline{\widehat R(Q)_{fd}}\gamma^{e}\gamma^{[ab]}\gamma_{e}{}^{c}\gamma^{f}\chi\big)\,T_{c}{}^{d}\\
&=\frac{8i}{3}\big(\overline{\widehat R(Q)^{[a}{}_{|c|}}\chi\big)\,T^{|c|b]}
\end{aligned}\tag{G566}
```

**G567: 6:DT:11, scalar coefficient.**

```math
\begin{aligned}
&\frac{16i}{3}\big(\bar\chi\gamma^{f}\gamma^{ce}\gamma^{d}\chi\big)\,\eta_{cd}\,T_{ef}\\
&=\frac{64i}{3}\big(\bar\chi\gamma^{cd}\chi\big)\,T_{cd}
\end{aligned}\tag{G567}
```

**G568: 6:DT:11, vector coefficient.**

```math
\begin{aligned}
&\frac{16i}{3}\big(\bar\chi\gamma^{f}\gamma^{a}\gamma^{ce}\gamma^{d}\chi\big)\,\eta_{cd}\,T_{ef}\\
&=-\frac{64i}{3}\big(\bar\chi\gamma^{acd}\chi\big)\,T_{cd}\\
&=-\frac{32}{3}\big(\bar\chi\gamma^{cd}\chi\big)\,\varepsilon_{cd}{}^{a}{}_{ef}\,T^{ef}
\end{aligned}\tag{G568}
```

**G569: 6:DT:11, bivector coefficient.**

```math
\begin{aligned}
&-\frac{8i}{3}\big(\bar\chi\gamma^{f}\gamma^{[ab]}\gamma^{ce}\gamma^{d}\chi\big)\,\eta_{cd}\,T_{ef}\\
&=0
\end{aligned}\tag{G569}
```

**G570: 6:DT:11, scalar coefficient.**

```math
\begin{aligned}
&-\frac{16i}{3}\big(\bar\chi\gamma^{f}\gamma^{ce}\gamma_{f}\chi\big)\,\eta_{cd}\,T_{e}{}^{d}\\
&=\frac{16i}{3}\big(\bar\chi\gamma^{cd}\chi\big)\,T_{cd}
\end{aligned}\tag{G570}
```

**G571: 6:DT:11, vector coefficient.**

```math
\begin{aligned}
&-\frac{16i}{3}\big(\bar\chi\gamma^{f}\gamma^{a}\gamma^{ce}\gamma_{f}\chi\big)\,\eta_{cd}\,T_{e}{}^{d}\\
&=\frac{16i}{3}\big(\bar\chi\gamma^{acd}\chi\big)\,T_{cd}\\
&=\frac{8}{3}\big(\bar\chi\gamma^{cd}\chi\big)\,\varepsilon_{cd}{}^{a}{}_{ef}\,T^{ef}
\end{aligned}\tag{G571}
```

**G572: 6:DT:11, bivector coefficient.**

```math
\begin{aligned}
&\frac{8i}{3}\big(\bar\chi\gamma^{f}\gamma^{[ab]}\gamma^{ce}\gamma_{f}\chi\big)\,\eta_{cd}\,T_{e}{}^{d}\\
&=\frac{32i}{3}\big(\bar\chi\gamma^{[a|c|}\chi\big)\,T_{|c|}{}^{b]}
\end{aligned}\tag{G572}
```

#### Block 7

The original spinor term is $`\frac{1024}{9}T^2\chi^i`$.

**G573: T21, scalar coefficient.**

```math
\begin{aligned}
&-\frac{128i}{9}\big(\bar\chi\gamma^{cd}\chi\big)\,T_{cd}\\
&=-\frac{128i}{9}\big(\bar\chi\gamma^{cd}\chi\big)\,T_{cd}
\end{aligned}\tag{G573}
```

**G574: T21, vector coefficient.**

```math
\begin{aligned}
&-\frac{128i}{9}\big(\bar\chi\gamma^{cd}\gamma^{a}\chi\big)\,T_{cd}\\
&=-\frac{128i}{9}\big(\bar\chi\gamma^{acd}\chi\big)\,T_{cd}\\
&=-\frac{64}{9}\big(\bar\chi\gamma^{cd}\chi\big)\,\varepsilon_{cd}{}^{a}{}_{ef}\,T^{ef}
\end{aligned}\tag{G574}
```

**G575: T21, bivector coefficient.**

```math
\begin{aligned}
&\frac{64i}{9}\big(\bar\chi\gamma^{cd}\gamma^{[ab]}\chi\big)\,T_{cd}\\
&=\frac{256i}{9}\big(\bar\chi\gamma^{[a|c|}\chi\big)\,T_{|c|}{}^{b]}
\end{aligned}\tag{G575}
```

**G576: T22, scalar coefficient.**

```math
\begin{aligned}
&-\frac{8i}{3}\big(\overline{\widehat R(Q)_{cd}}\chi\big)\,T^{cd}\\
&=-\frac{8i}{3}\big(\overline{\widehat R(Q)_{cd}}\chi\big)\,T^{cd}
\end{aligned}\tag{G576}
```

**G577: T22, vector coefficient.**

```math
\begin{aligned}
&-\frac{8i}{3}\big(\overline{\widehat R(Q)_{cd}}\gamma^{a}\chi\big)\,T^{cd}\\
&=-\frac{8i}{3}\big(\overline{\widehat R(Q)_{cd}}\gamma^{a}\chi\big)\,T^{cd}
\end{aligned}\tag{G577}
```

**G578: T22, bivector coefficient.**

```math
\begin{aligned}
&\frac{4i}{3}\big(\overline{\widehat R(Q)_{cd}}\gamma^{[ab]}\chi\big)\,T^{cd}\\
&=\frac{4i}{3}\big(\overline{\widehat R(Q)_{cd}}\gamma^{[ab]}\chi\big)\,T^{cd}
\end{aligned}\tag{G578}
```

**G579: chi1, whole coefficient matrix.**

```math
\begin{aligned}
&\frac{256}{9}D\,T_{cd}\,T^{cd}\\
&=\frac{256}{9}D\,T_{cd}\,T^{cd}
\end{aligned}\tag{G579}
```

**G580: chi3, whole coefficient matrix.**

```math
\begin{aligned}
&\frac{128i}{9}(\mathcal D_{c}T_{de})\,T_{fg}\,T^{fg}\,\gamma^{de}\gamma^{c}\\
&=\frac{128i}{9}T_{cd}\,T^{cd}\,(\mathcal D_{e}T_{fg})\,\gamma^{efg}\\
&+\frac{256i}{9}T_{cd}\,T^{cd}\,(\mathcal D_{e}T_{f}{}^{e})\,\gamma^{f}\\
&=\frac{64}{9}\varepsilon_{cdefg}\,T_{hj}\,T^{hj}\,(\mathcal D^{e}T^{fg})\,\gamma^{cd}\\
&+\frac{256i}{9}T_{cd}\,T^{cd}\,(\mathcal D_{e}T_{f}{}^{e})\,\gamma^{f}
\end{aligned}\tag{G580}
```

**G581: chi4, whole coefficient matrix.**

```math
\begin{aligned}
&-\frac{128i}{9}(\mathcal D_{c}T_{d}{}^{c})\,T_{ef}\,T^{ef}\,\gamma^{d}\\
&=-\frac{128i}{9}T_{cd}\,T^{cd}\,(\mathcal D_{e}T_{f}{}^{e})\,\gamma^{f}
\end{aligned}\tag{G581}
```

**G582: chi5, whole coefficient matrix.**

```math
\begin{aligned}
&-\frac{256}{9}T_{cd}\,T^{cd}\,T_{ef}\,T_{gh}\,\gamma^{efgh}\\
&=-\frac{256}{9}T_{cd}\,T_{ef}\,T_{gh}\,T^{gh}\,\gamma^{cdef}\\
&=-\frac{256i}{9}\varepsilon_{cdefg}\,T^{de}\,T^{fg}\,T_{hj}\,T^{hj}\,\gamma^{c}
\end{aligned}\tag{G582}
```

**G583: chi6, whole coefficient matrix.**

```math
\begin{aligned}
&\frac{512}{27}T_{cd}\,T^{cd}\,T_{ef}\,T^{ef}\\
&=\frac{512}{27}T_{cd}\,T^{cd}\,T_{ef}\,T^{ef}
\end{aligned}\tag{G583}
```

#### Block 8

The original spinor term is $`\frac{128i}{3}\gamma_a\mathcal D_b\chi^i T^{ab}`$.

**G584: T1, scalar coefficient.**

```math
\begin{aligned}
&\frac{8}{3}\big(\bar\chi\gamma^{cd}\gamma_{c}\mathcal D_{d}\chi\big)\\
&=-\frac{32}{3}\big(\bar\chi\gamma^{c}\mathcal D_{c}\chi\big)
\end{aligned}\tag{G584}
```

**G585: T1, vector coefficient.**

```math
\begin{aligned}
&\frac{8}{3}\big(\bar\chi\gamma^{cd}\gamma^{a}\gamma_{c}\mathcal D_{d}\chi\big)\\
&=\frac{16}{3}\big(\bar\chi\gamma^{ca}\mathcal D_{c}\chi\big)\\
&+\frac{32}{3}\big(\bar\chi\mathcal D^{a}\chi\big)
\end{aligned}\tag{G585}
```

**G586: T1, bivector coefficient.**

```math
\begin{aligned}
&-\frac{4}{3}\big(\bar\chi\gamma^{cd}\gamma^{[ab]}\gamma_{c}\mathcal D_{d}\chi\big)\\
&=-\frac{16}{3}\big(\bar\chi\gamma^{[a}\mathcal D^{b]}\chi\big)
\end{aligned}\tag{G586}
```

**G587: T2, scalar coefficient.**

```math
\begin{aligned}
&\frac{1}{2}\big(\overline{\widehat R(Q)_{cd}}\gamma^{c}\mathcal D^{d}\chi\big)\\
&=0
\end{aligned}\tag{G587}
```

**G588: T2, vector coefficient.**

```math
\begin{aligned}
&\frac{1}{2}\big(\overline{\widehat R(Q)_{cd}}\gamma^{a}\gamma^{c}\mathcal D^{d}\chi\big)\\
&=-\big(\overline{\widehat R(Q)_{c}{}^{a}}\mathcal D^{c}\chi\big)
\end{aligned}\tag{G588}
```

**G589: T2, bivector coefficient.**

```math
\begin{aligned}
&-\frac{1}{4}\big(\overline{\widehat R(Q)_{cd}}\gamma^{[ab]}\gamma^{c}\mathcal D^{d}\chi\big)\\
&=-\big(\overline{\widehat R(Q)_{c}{}^{[a}}\gamma^{b]}\mathcal D^{c}\chi\big)
\end{aligned}\tag{G589}
```

**G590: 8:bos:1, whole coefficient matrix.**

```math
\begin{aligned}
&\frac{32i}{3}T_{cd}\,(\mathcal D^{d}D)\,\gamma^{c}\\
&=-\frac{32i}{3}(\mathcal D_{c}D)\,T^{c}{}_{d}\,\gamma^{d}
\end{aligned}\tag{G590}
```

**G591: 8:bos:2, whole coefficient matrix.**

```math
\begin{aligned}
&-\frac{16}{3}T_{cd}\,(\mathcal D^{d}\mathcal D_{e}T_{fg})\,\gamma^{c}\gamma^{fg}\gamma^{e}\\
&=-\frac{16}{3}T_{cd}\,(\mathcal D^{d}\mathcal D_{e}T_{fg})\,\gamma^{cefg}\\
&+\frac{16}{3}T_{cd}\,(\mathcal D^{c}\mathcal D^{d}T_{ef})\,\gamma^{ef}\\
&-\frac{32}{3}T_{cd}\,(\mathcal D^{d}\mathcal D_{e}T_{f}{}^{e})\,\gamma^{cf}\\
&+\frac{32}{3}T_{cd}\,(\mathcal D^{c}\mathcal D_{e}T_{f}{}^{d})\,\gamma^{ef}\\
&+\frac{32}{3}T_{cd}\,(\mathcal D^{c}\mathcal D_{e}T^{de})\\
&=-\frac{16i}{3}\varepsilon_{cdefg}\,T^{d}{}_{h}\,(\mathcal D^{h}\mathcal D^{e}T^{fg})\,\gamma^{c}\\
&+\frac{16}{3}T_{cd}\,(\mathcal D^{c}\mathcal D^{d}T_{ef})\,\gamma^{ef}\\
&-\frac{32}{3}T_{cd}\,(\mathcal D^{d}\mathcal D_{e}T_{f}{}^{e})\,\gamma^{cf}\\
&+\frac{32}{3}T_{cd}\,(\mathcal D^{c}\mathcal D_{e}T_{f}{}^{d})\,\gamma^{ef}\\
&+\frac{32}{3}T_{cd}\,(\mathcal D^{c}\mathcal D_{e}T^{de})
\end{aligned}\tag{G591}
```

**G592: 8:bos:3, whole coefficient matrix.**

```math
\begin{aligned}
&\frac{16}{3}T_{cd}\,(\mathcal D^{d}\mathcal D_{e}T_{f}{}^{e})\,\gamma^{c}\gamma^{f}\\
&=\frac{16}{3}T_{cd}\,(\mathcal D^{d}\mathcal D_{e}T_{f}{}^{e})\,\gamma^{cf}\\
&-\frac{16}{3}T_{cd}\,(\mathcal D^{c}\mathcal D_{e}T^{de})
\end{aligned}\tag{G592}
```

**G593: 8:bos:4, whole coefficient matrix.**

```math
\begin{aligned}
&-\frac{32i}{3}T_{cd}\,(\mathcal D^{d}T_{ef})\,T_{gh}\,\gamma^{c}\gamma^{efgh}\\
&=-\frac{32i}{3}T_{cd}\,T_{ef}\,(\mathcal D^{f}T_{gh})\,\gamma^{cdegh}\\
&-\frac{64i}{3}T_{cd}\,T_{ef}\,(\mathcal D^{e}T_{g}{}^{f})\,\gamma^{cdg}\\
&+\frac{64i}{3}T_{cd}\,T^{d}{}_{e}\,(\mathcal D^{e}T_{fg})\,\gamma^{cfg}\\
&=-\frac{16}{3}\varepsilon_{cdefg}\,T^{cd}\,T^{ef}\,(\mathcal D_{h}T^{gh})\\
&-\frac{32}{3}\varepsilon_{cdefg}\,T^{ef}\,T_{hj}\,(\mathcal D^{h}T^{gj})\,\gamma^{cd}\\
&+\frac{32}{3}\varepsilon_{cdefg}\,T^{e}{}_{h}\,T^{h}{}_{j}\,(\mathcal D^{j}T^{fg})\,\gamma^{cd}
\end{aligned}\tag{G593}
```

**G594: 8:bos:5, whole coefficient matrix.**

```math
\begin{aligned}
&-\frac{32i}{3}T_{cd}\,T_{ef}\,(\mathcal D^{d}T_{gh})\,\gamma^{c}\gamma^{efgh}\\
&=-\frac{32i}{3}T_{cd}\,T_{ef}\,(\mathcal D^{f}T_{gh})\,\gamma^{cdegh}\\
&+\frac{64i}{3}T_{cd}\,T^{d}{}_{e}\,(\mathcal D^{e}T_{fg})\,\gamma^{cfg}\\
&-\frac{64i}{3}T_{cd}\,T_{ef}\,(\mathcal D^{e}T_{g}{}^{f})\,\gamma^{cdg}\\
&=-\frac{16}{3}\varepsilon_{cdefg}\,T^{cd}\,T^{ef}\,(\mathcal D_{h}T^{gh})\\
&+\frac{32}{3}\varepsilon_{cdefg}\,T^{e}{}_{h}\,T^{h}{}_{j}\,(\mathcal D^{j}T^{fg})\,\gamma^{cd}\\
&-\frac{32}{3}\varepsilon_{cdefg}\,T^{ef}\,T_{hj}\,(\mathcal D^{h}T^{gj})\,\gamma^{cd}
\end{aligned}\tag{G594}
```

**G595: 8:bos:6, whole coefficient matrix.**

```math
\begin{aligned}
&\frac{128i}{9}T_{cd}\,T_{ef}\,(\mathcal D^{d}T^{ef})\,\gamma^{c}\\
&=\frac{128i}{9}T_{cd}\,T_{ef}\,(\mathcal D^{d}T^{ef})\,\gamma^{c}
\end{aligned}\tag{G595}
```

**G596: 8:bos:7, whole coefficient matrix.**

```math
\begin{aligned}
&\frac{32}{3}T_{cd}\,D\,T_{ef}\,\gamma^{c}\gamma^{ef}\gamma^{d}\\
&=\frac{32}{3}D\,T_{cd}\,T_{ef}\,\gamma^{cdef}\\
&+\frac{64}{3}D\,T_{cd}\,T^{cd}\\
&=\frac{32i}{3}D\,\varepsilon_{cdefg}\,T^{de}\,T^{fg}\,\gamma^{c}\\
&+\frac{64}{3}D\,T_{cd}\,T^{cd}
\end{aligned}\tag{G596}
```

**G597: 8:bos:8, whole coefficient matrix.**

```math
\begin{aligned}
&\frac{16i}{3}T_{cd}\,(\mathcal D_{e}T_{fg})\,T_{hj}\,\gamma^{c}\gamma^{fg}\gamma^{e}\gamma^{hj}\gamma^{d}\\
&=-\frac{128i}{3}T_{cd}\,T^{d}{}_{e}\,(\mathcal D_{f}T_{g}{}^{e})\,\gamma^{cfg}\\
&-\frac{64i}{3}T_{cd}\,T^{d}{}_{e}\,(\mathcal D^{e}T_{fg})\,\gamma^{cfg}\\
&-\frac{32i}{3}T_{cd}\,T^{cd}\,(\mathcal D_{e}T_{fg})\,\gamma^{efg}\\
&+\frac{32i}{3}T_{cd}\,T_{ef}\,(\mathcal D_{g}T_{h}{}^{f})\,\gamma^{cdegh}\\
&+\frac{16i}{3}T_{cd}\,T_{ef}\,(\mathcal D^{f}T_{gh})\,\gamma^{cdegh}\\
&+\frac{64i}{3}T_{cd}\,T_{ef}\,(\mathcal D^{d}T^{ef})\,\gamma^{c}\\
&-\frac{128i}{3}T_{cd}\,T_{ef}\,(\mathcal D^{e}T^{df})\,\gamma^{c}\\
&-\frac{32i}{3}T_{cd}\,T_{ef}\,(\mathcal D_{g}T_{h}{}^{g})\,\gamma^{cdefh}\\
&+\frac{64i}{3}T_{cd}\,T_{ef}\,(\mathcal D_{g}T^{fg})\,\gamma^{cde}\\
&-\frac{128i}{3}T_{cd}\,T^{d}{}_{e}\,(\mathcal D_{f}T^{ef})\,\gamma^{c}\\
&-\frac{64i}{3}T_{cd}\,T^{cd}\,(\mathcal D_{e}T_{f}{}^{e})\,\gamma^{f}\\
&=-\frac{64}{3}\varepsilon_{cdefg}\,T^{e}{}_{h}\,T^{h}{}_{j}\,(\mathcal D^{f}T^{gj})\,\gamma^{cd}\\
&-\frac{32}{3}\varepsilon_{cdefg}\,T^{e}{}_{h}\,T^{h}{}_{j}\,(\mathcal D^{j}T^{fg})\,\gamma^{cd}\\
&-\frac{16}{3}\varepsilon_{cdefg}\,T_{hj}\,T^{hj}\,(\mathcal D^{e}T^{fg})\,\gamma^{cd}\\
&+\frac{32}{3}\varepsilon_{cdefg}\,T^{cd}\,T^{ef}\,(\mathcal D_{h}T^{gh})\\
&+\frac{64i}{3}T_{cd}\,T_{ef}\,(\mathcal D^{d}T^{ef})\,\gamma^{c}\\
&-\frac{128i}{3}T_{cd}\,T_{ef}\,(\mathcal D^{e}T^{df})\,\gamma^{c}\\
&+\frac{32}{3}\varepsilon_{cdefg}\,T^{ef}\,T^{g}{}_{h}\,(\mathcal D_{j}T^{hj})\,\gamma^{cd}\\
&-\frac{128i}{3}T_{cd}\,T^{d}{}_{e}\,(\mathcal D_{f}T^{ef})\,\gamma^{c}\\
&-\frac{64i}{3}T_{cd}\,T^{cd}\,(\mathcal D_{e}T_{f}{}^{e})\,\gamma^{f}
\end{aligned}\tag{G597}
```

**G598: 8:bos:9, whole coefficient matrix.**

```math
\begin{aligned}
&-\frac{16i}{3}T_{cd}\,(\mathcal D_{e}T_{f}{}^{e})\,T_{gh}\,\gamma^{c}\gamma^{f}\gamma^{gh}\gamma^{d}\\
&=\frac{16i}{3}T_{cd}\,T_{ef}\,(\mathcal D_{g}T_{h}{}^{g})\,\gamma^{cdefh}\\
&-\frac{32i}{3}T_{cd}\,T_{ef}\,(\mathcal D_{g}T^{fg})\,\gamma^{cde}\\
&+\frac{64i}{3}T_{cd}\,T^{d}{}_{e}\,(\mathcal D_{f}T^{ef})\,\gamma^{c}\\
&+\frac{32i}{3}T_{cd}\,T^{cd}\,(\mathcal D_{e}T_{f}{}^{e})\,\gamma^{f}\\
&=-\frac{16}{3}\varepsilon_{cdefg}\,T^{cd}\,T^{ef}\,(\mathcal D_{h}T^{gh})\\
&-\frac{16}{3}\varepsilon_{cdefg}\,T^{ef}\,T^{g}{}_{h}\,(\mathcal D_{j}T^{hj})\,\gamma^{cd}\\
&+\frac{64i}{3}T_{cd}\,T^{d}{}_{e}\,(\mathcal D_{f}T^{ef})\,\gamma^{c}\\
&+\frac{32i}{3}T_{cd}\,T^{cd}\,(\mathcal D_{e}T_{f}{}^{e})\,\gamma^{f}
\end{aligned}\tag{G598}
```

**G599: 8:bos:10, whole coefficient matrix.**

```math
\begin{aligned}
&-\frac{32}{3}T_{cd}\,T_{ef}\,T_{gh}\,T_{jk}\,\gamma^{c}\gamma^{efgh}\gamma^{jk}\gamma^{d}\\
&=128T_{cd}\,T_{ef}\,T_{gh}\,T^{fh}\,\gamma^{cdeg}\\
&-\frac{32}{3}T_{cd}\,T_{ef}\,T_{gh}\,T^{gh}\,\gamma^{cdef}\\
&-\frac{512}{3}T_{cd}\,T^{c}{}_{e}\,T^{d}{}_{f}\,T^{ef}\\
&+\frac{256}{3}T_{cd}\,T^{cd}\,T_{ef}\,T^{ef}\\
&=\frac{64i}{3}\varepsilon_{cdefg}\,T^{de}\,T^{fg}\,T_{hj}\,T^{hj}\,\gamma^{c}\\
&-\frac{512}{3}T_{cd}\,T^{c}{}_{e}\,T^{d}{}_{f}\,T^{ef}\\
&+\frac{256}{3}T_{cd}\,T^{cd}\,T_{ef}\,T^{ef}
\end{aligned}\tag{G599}
```

**G600: 8:bos:11, whole coefficient matrix.**

```math
\begin{aligned}
&\frac{64}{9}T_{cd}\,T_{ef}\,T^{ef}\,T_{gh}\,\gamma^{c}\gamma^{gh}\gamma^{d}\\
&=\frac{64}{9}T_{cd}\,T_{ef}\,T_{gh}\,T^{gh}\,\gamma^{cdef}\\
&+\frac{128}{9}T_{cd}\,T^{cd}\,T_{ef}\,T^{ef}\\
&=\frac{64i}{9}\varepsilon_{cdefg}\,T^{de}\,T^{fg}\,T_{hj}\,T^{hj}\,\gamma^{c}\\
&+\frac{128}{9}T_{cd}\,T^{cd}\,T_{ef}\,T^{ef}
\end{aligned}\tag{G600}
```

**G601: 8:bos:12, whole coefficient matrix.**

```math
\begin{aligned}
&-\frac{32i}{9}T_{cd}\,T_{ef}\,(\mathcal D_{g}T_{hj})\,\gamma^{c}\gamma^{ef}\gamma^{g}\gamma^{hj}\gamma^{d}\\
&=\frac{64i}{3}T_{cd}\,T_{ef}\,(\mathcal D_{g}T_{h}{}^{f})\,\gamma^{cdegh}\\
&+\frac{256i}{9}T_{cd}\,T^{d}{}_{e}\,(\mathcal D_{f}T_{g}{}^{e})\,\gamma^{cfg}\\
&-\frac{64i}{9}T_{cd}\,T_{ef}\,(\mathcal D_{g}T_{h}{}^{g})\,\gamma^{cdefh}\\
&-\frac{128i}{9}T_{cd}\,T_{ef}\,(\mathcal D_{g}T^{fg})\,\gamma^{cde}\\
&-\frac{256i}{9}T_{cd}\,T^{d}{}_{e}\,(\mathcal D_{f}T^{ef})\,\gamma^{c}\\
&-\frac{256i}{9}T_{cd}\,T_{ef}\,(\mathcal D^{e}T^{df})\,\gamma^{c}\\
&+\frac{128i}{9}T_{cd}\,T_{ef}\,(\mathcal D^{d}T^{ef})\,\gamma^{c}\\
&+\frac{32i}{3}T_{cd}\,T_{ef}\,(\mathcal D^{f}T_{gh})\,\gamma^{cdegh}\\
&+\frac{128i}{9}T_{cd}\,T^{d}{}_{e}\,(\mathcal D^{e}T_{fg})\,\gamma^{cfg}\\
&+\frac{64i}{9}T_{cd}\,T^{cd}\,(\mathcal D_{e}T_{fg})\,\gamma^{efg}\\
&-\frac{128i}{9}T_{cd}\,T^{cd}\,(\mathcal D_{e}T_{f}{}^{e})\,\gamma^{f}\\
&=\frac{64}{9}\varepsilon_{cdefg}\,T^{cd}\,T^{ef}\,(\mathcal D_{h}T^{gh})\\
&+\frac{128}{9}\varepsilon_{cdefg}\,T^{e}{}_{h}\,T^{h}{}_{j}\,(\mathcal D^{f}T^{gj})\,\gamma^{cd}\\
&-\frac{64}{9}\varepsilon_{cdefg}\,T^{ef}\,T^{g}{}_{h}\,(\mathcal D_{j}T^{hj})\,\gamma^{cd}\\
&-\frac{256i}{9}T_{cd}\,T^{d}{}_{e}\,(\mathcal D_{f}T^{ef})\,\gamma^{c}\\
&-\frac{256i}{9}T_{cd}\,T_{ef}\,(\mathcal D^{e}T^{df})\,\gamma^{c}\\
&+\frac{128i}{9}T_{cd}\,T_{ef}\,(\mathcal D^{d}T^{ef})\,\gamma^{c}\\
&+\frac{64}{9}\varepsilon_{cdefg}\,T^{e}{}_{h}\,T^{h}{}_{j}\,(\mathcal D^{j}T^{fg})\,\gamma^{cd}\\
&+\frac{32}{9}\varepsilon_{cdefg}\,T_{hj}\,T^{hj}\,(\mathcal D^{e}T^{fg})\,\gamma^{cd}\\
&-\frac{128i}{9}T_{cd}\,T^{cd}\,(\mathcal D_{e}T_{f}{}^{e})\,\gamma^{f}
\end{aligned}\tag{G601}
```

**G602: 8:bos:13, whole coefficient matrix.**

```math
\begin{aligned}
&\frac{32i}{9}T_{cd}\,T_{ef}\,(\mathcal D^{d}T_{gh})\,\gamma^{c}\gamma^{ef}\gamma^{gh}\\
&=\frac{32i}{9}T_{cd}\,T_{ef}\,(\mathcal D^{f}T_{gh})\,\gamma^{cdegh}\\
&+\frac{64i}{9}T_{cd}\,T_{ef}\,(\mathcal D^{e}T_{g}{}^{f})\,\gamma^{cdg}\\
&-\frac{128i}{9}T_{cd}\,T_{ef}\,(\mathcal D^{d}T_{g}{}^{f})\,\gamma^{ceg}\\
&+\frac{128i}{9}T_{cd}\,T_{ef}\,(\mathcal D^{e}T^{df})\,\gamma^{c}\\
&-\frac{64i}{9}T_{cd}\,T_{ef}\,(\mathcal D^{d}T^{ef})\,\gamma^{c}\\
&-\frac{64i}{9}T_{cd}\,T^{d}{}_{e}\,(\mathcal D^{e}T_{fg})\,\gamma^{cfg}\\
&-\frac{128i}{9}T_{cd}\,T^{c}{}_{e}\,(\mathcal D^{d}T_{f}{}^{e})\,\gamma^{f}\\
&=\frac{16}{9}\varepsilon_{cdefg}\,T^{cd}\,T^{ef}\,(\mathcal D_{h}T^{gh})\\
&+\frac{32}{9}\varepsilon_{cdefg}\,T^{ef}\,T_{hj}\,(\mathcal D^{h}T^{gj})\,\gamma^{cd}\\
&-\frac{64}{9}\varepsilon_{cdefg}\,T^{e}{}_{h}\,T^{f}{}_{j}\,(\mathcal D^{h}T^{gj})\,\gamma^{cd}\\
&+\frac{128i}{9}T_{cd}\,T_{ef}\,(\mathcal D^{e}T^{df})\,\gamma^{c}\\
&-\frac{64i}{9}T_{cd}\,T_{ef}\,(\mathcal D^{d}T^{ef})\,\gamma^{c}\\
&-\frac{32}{9}\varepsilon_{cdefg}\,T^{e}{}_{h}\,T^{h}{}_{j}\,(\mathcal D^{j}T^{fg})\,\gamma^{cd}\\
&-\frac{128i}{9}T_{cd}\,T^{c}{}_{e}\,(\mathcal D^{d}T_{f}{}^{e})\,\gamma^{f}
\end{aligned}\tag{G602}
```

**G603: 8:bos:14, whole coefficient matrix.**

```math
\begin{aligned}
&-\frac{32i}{9}T_{cd}\,T_{ef}\,(\mathcal D_{g}T^{g}{}_{h})\,\gamma^{c}\gamma^{ef}\gamma^{d}\gamma^{h}\\
&=\frac{32i}{9}T_{cd}\,T_{ef}\,(\mathcal D_{g}T_{h}{}^{g})\,\gamma^{cdefh}\\
&+\frac{128i}{9}T_{cd}\,T_{ef}\,(\mathcal D_{g}T^{fg})\,\gamma^{cde}\\
&+\frac{64i}{9}T_{cd}\,T^{cd}\,(\mathcal D_{e}T_{f}{}^{e})\,\gamma^{f}\\
&=-\frac{32}{9}\varepsilon_{cdefg}\,T^{cd}\,T^{ef}\,(\mathcal D_{h}T^{gh})\\
&+\frac{64}{9}\varepsilon_{cdefg}\,T^{ef}\,T^{g}{}_{h}\,(\mathcal D_{j}T^{hj})\,\gamma^{cd}\\
&+\frac{64i}{9}T_{cd}\,T^{cd}\,(\mathcal D_{e}T_{f}{}^{e})\,\gamma^{f}
\end{aligned}\tag{G603}
```

**G604: 8:bos:15, whole coefficient matrix.**

```math
\begin{aligned}
&-\frac{32}{3}T_{cd}\,T_{ef}\,T_{gh}\,T_{jk}\,\gamma^{c}\gamma^{ef}\gamma^{dghjk}\\
&=-\frac{1024}{15}T_{cd}\,T_{ef}\,T_{gh}\,T^{fh}\,\gamma^{cdeg}\\
&+\frac{256}{15}T_{cd}\,T_{ef}\,T_{gh}\,T^{gh}\,\gamma^{cdef}\\
&=0
\end{aligned}\tag{G604}
```

**G605: 8:bos:16, whole coefficient matrix.**

```math
\begin{aligned}
&\frac{256}{3}T_{cd}\,T_{ef}\,T_{gh}\,T^{dh}\,\gamma^{c}\gamma^{ef}\gamma^{g}\\
&=\frac{256}{3}T_{cd}\,T_{ef}\,T_{gh}\,T^{fh}\,\gamma^{cdeg}\\
&+\frac{512}{3}T_{cd}\,T^{c}{}_{e}\,T^{d}{}_{f}\,T^{ef}\\
&=\frac{64i}{3}\varepsilon_{cdefg}\,T^{de}\,T^{fg}\,T_{hj}\,T^{hj}\,\gamma^{c}\\
&+\frac{512}{3}T_{cd}\,T^{c}{}_{e}\,T^{d}{}_{f}\,T^{ef}
\end{aligned}\tag{G605}
```

**G606: 8:bos:17, whole coefficient matrix.**

```math
\begin{aligned}
&-\frac{64}{3}T_{cd}\,T_{ef}\,T_{gh}\,T^{gh}\,\gamma^{c}\gamma^{ef}\gamma^{d}\\
&=-\frac{64}{3}T_{cd}\,T_{ef}\,T_{gh}\,T^{gh}\,\gamma^{cdef}\\
&-\frac{128}{3}T_{cd}\,T^{cd}\,T_{ef}\,T^{ef}\\
&=-\frac{64i}{3}\varepsilon_{cdefg}\,T^{de}\,T^{fg}\,T_{hj}\,T^{hj}\,\gamma^{c}\\
&-\frac{128}{3}T_{cd}\,T^{cd}\,T_{ef}\,T^{ef}
\end{aligned}\tag{G606}
```

**G607: 8:connection:1, scalar coefficient.**

```math
\begin{aligned}
&16i\big(\bar\chi\gamma^{d}\gamma^{c}\chi\big)\,T_{cd}\\
&=-16i\big(\bar\chi\gamma^{cd}\chi\big)\,T_{cd}
\end{aligned}\tag{G607}
```

**G608: 8:connection:1, vector coefficient.**

```math
\begin{aligned}
&16i\big(\bar\chi\gamma^{d}\gamma^{a}\gamma^{c}\chi\big)\,T_{cd}\\
&=16i\big(\bar\chi\gamma^{acd}\chi\big)\,T_{cd}\\
&=8\big(\bar\chi\gamma^{cd}\chi\big)\,\varepsilon_{cd}{}^{a}{}_{ef}\,T^{ef}
\end{aligned}\tag{G608}
```

**G609: 8:connection:1, bivector coefficient.**

```math
\begin{aligned}
&-8i\big(\bar\chi\gamma^{d}\gamma^{[ab]}\gamma^{c}\chi\big)\,T_{cd}\\
&=0
\end{aligned}\tag{G609}
```

**G610: 8:connection:2, scalar coefficient.**

```math
\begin{aligned}
&-\frac{i}{3}\big(\overline{\widehat R(Q)_{df}}\gamma^{e}\gamma^{c}\gamma_{e}{}^{f}\chi\big)\,T_{c}{}^{d}\\
&=-2i\big(\overline{\widehat R(Q)_{cd}}\chi\big)\,T^{cd}
\end{aligned}\tag{G610}
```

**G611: 8:connection:2, vector coefficient.**

```math
\begin{aligned}
&-\frac{i}{3}\big(\overline{\widehat R(Q)_{df}}\gamma^{e}\gamma^{a}\gamma^{c}\gamma_{e}{}^{f}\chi\big)\,T_{c}{}^{d}\\
&=\frac{2i}{3}\big(\overline{\widehat R(Q)_{cd}}\gamma^{a}\chi\big)\,T^{cd}\\
&+\frac{2i}{3}\big(\overline{\widehat R(Q)^{a}{}_{c}}\gamma^{d}\chi\big)\,T^{c}{}_{d}
\end{aligned}\tag{G611}
```

**G612: 8:connection:2, bivector coefficient.**

```math
\begin{aligned}
&\frac{i}{6}\big(\overline{\widehat R(Q)_{df}}\gamma^{e}\gamma^{[ab]}\gamma^{c}\gamma_{e}{}^{f}\chi\big)\,T_{c}{}^{d}\\
&=-\frac{i}{3}\big(\overline{\widehat R(Q)_{cd}}\gamma^{[ab]}\chi\big)\,T^{cd}\\
&+\frac{2i}{3}\big(\overline{\widehat R(Q)^{[a}{}_{|c|}}\gamma^{b]d}\chi\big)\,T^{c}{}_{d}\\
&-2i\big(\overline{\widehat R(Q)^{[a}{}_{|c|}}\chi\big)\,T^{|c|b]}
\end{aligned}\tag{G612}
```

**G613: 8:connection:2, scalar coefficient.**

```math
\begin{aligned}
&\frac{i}{3}\big(\overline{\widehat R(Q)_{df}}\gamma^{e}\gamma^{c}\gamma^{f}{}_{e}\chi\big)\,T_{c}{}^{d}\\
&=-2i\big(\overline{\widehat R(Q)_{cd}}\chi\big)\,T^{cd}
\end{aligned}\tag{G613}
```

**G614: 8:connection:2, vector coefficient.**

```math
\begin{aligned}
&\frac{i}{3}\big(\overline{\widehat R(Q)_{df}}\gamma^{e}\gamma^{a}\gamma^{c}\gamma^{f}{}_{e}\chi\big)\,T_{c}{}^{d}\\
&=\frac{2i}{3}\big(\overline{\widehat R(Q)_{cd}}\gamma^{a}\chi\big)\,T^{cd}\\
&+\frac{2i}{3}\big(\overline{\widehat R(Q)^{a}{}_{c}}\gamma^{d}\chi\big)\,T^{c}{}_{d}
\end{aligned}\tag{G614}
```

**G615: 8:connection:2, bivector coefficient.**

```math
\begin{aligned}
&-\frac{i}{6}\big(\overline{\widehat R(Q)_{df}}\gamma^{e}\gamma^{[ab]}\gamma^{c}\gamma^{f}{}_{e}\chi\big)\,T_{c}{}^{d}\\
&=-\frac{i}{3}\big(\overline{\widehat R(Q)_{cd}}\gamma^{[ab]}\chi\big)\,T^{cd}\\
&+\frac{2i}{3}\big(\overline{\widehat R(Q)^{[a}{}_{|c|}}\gamma^{b]d}\chi\big)\,T^{c}{}_{d}\\
&-2i\big(\overline{\widehat R(Q)^{[a}{}_{|c|}}\chi\big)\,T^{|c|b]}
\end{aligned}\tag{G615}
```

**G616: 8:connection:3, scalar coefficient.**

```math
\begin{aligned}
&-\frac{i}{3}\big(\overline{\widehat R(Q)_{ef}}\gamma^{d}\gamma^{c}\gamma^{ef}\chi\big)\,T_{cd}\\
&=-\frac{8i}{3}\big(\overline{\widehat R(Q)_{cd}}\chi\big)\,T^{cd}
\end{aligned}\tag{G616}
```

**G617: 8:connection:3, vector coefficient.**

```math
\begin{aligned}
&-\frac{i}{3}\big(\overline{\widehat R(Q)_{ef}}\gamma^{d}\gamma^{a}\gamma^{c}\gamma^{ef}\chi\big)\,T_{cd}\\
&=\frac{8i}{3}\big(\overline{\widehat R(Q)_{cd}}\gamma^{a}\chi\big)\,T^{cd}\\
&+\frac{16i}{3}\big(\overline{\widehat R(Q)^{a}{}_{c}}\gamma^{d}\chi\big)\,T^{c}{}_{d}
\end{aligned}\tag{G617}
```

**G618: 8:connection:3, bivector coefficient.**

```math
\begin{aligned}
&\frac{i}{6}\big(\overline{\widehat R(Q)_{ef}}\gamma^{d}\gamma^{[ab]}\gamma^{c}\gamma^{ef}\chi\big)\,T_{cd}\\
&=i\big(\overline{\widehat R(Q)_{cd}}\gamma^{[ab]}\chi\big)\,T^{cd}\\
&-4i\big(\overline{\widehat R(Q)^{[a}{}_{|c|}}\gamma^{b]d}\chi\big)\,T^{c}{}_{d}\\
&+i\big(\overline{\widehat R(Q)^{[ab]}}\gamma^{cd}\chi\big)\,T_{cd}
\end{aligned}\tag{G618}
```

**G619: 8:connection:4, scalar coefficient.**

```math
\begin{aligned}
&-\frac{8i}{3}\big(\bar\chi\gamma^{f}\gamma^{e}\gamma^{d}{}_{f}\chi\big)\,\eta_{cd}\,T_{e}{}^{c}\\
&=-\frac{16i}{3}\big(\bar\chi\gamma^{cd}\chi\big)\,T_{cd}
\end{aligned}\tag{G619}
```

**G620: 8:connection:4, vector coefficient.**

```math
\begin{aligned}
&-\frac{8i}{3}\big(\bar\chi\gamma^{f}\gamma^{a}\gamma^{e}\gamma^{d}{}_{f}\chi\big)\,\eta_{cd}\,T_{e}{}^{c}\\
&=0
\end{aligned}\tag{G620}
```

**G621: 8:connection:4, bivector coefficient.**

```math
\begin{aligned}
&\frac{4i}{3}\big(\bar\chi\gamma^{f}\gamma^{[ab]}\gamma^{e}\gamma^{d}{}_{f}\chi\big)\,\eta_{cd}\,T_{e}{}^{c}\\
&=-\frac{16i}{3}\big(\bar\chi\gamma^{[a|c|}\chi\big)\,T_{|c|}{}^{b]}
\end{aligned}\tag{G621}
```

**G622: 8:connection:4, scalar coefficient.**

```math
\begin{aligned}
&\frac{8i}{3}\big(\bar\chi\gamma^{f}\gamma^{e}\gamma_{f}{}^{d}\chi\big)\,\eta_{cd}\,T_{e}{}^{c}\\
&=-\frac{16i}{3}\big(\bar\chi\gamma^{cd}\chi\big)\,T_{cd}
\end{aligned}\tag{G622}
```

**G623: 8:connection:4, vector coefficient.**

```math
\begin{aligned}
&\frac{8i}{3}\big(\bar\chi\gamma^{f}\gamma^{a}\gamma^{e}\gamma_{f}{}^{d}\chi\big)\,\eta_{cd}\,T_{e}{}^{c}\\
&=0
\end{aligned}\tag{G623}
```

**G624: 8:connection:4, bivector coefficient.**

```math
\begin{aligned}
&-\frac{4i}{3}\big(\bar\chi\gamma^{f}\gamma^{[ab]}\gamma^{e}\gamma_{f}{}^{d}\chi\big)\,\eta_{cd}\,T_{e}{}^{c}\\
&=-\frac{16i}{3}\big(\bar\chi\gamma^{[a|c|}\chi\big)\,T_{|c|}{}^{b]}
\end{aligned}\tag{G624}
```

**G625: 8:connection:5, scalar coefficient.**

```math
\begin{aligned}
&32i\big(\bar\chi\gamma^{d}\gamma^{c}\chi\big)\,T_{cd}\\
&=-32i\big(\bar\chi\gamma^{cd}\chi\big)\,T_{cd}
\end{aligned}\tag{G625}
```

**G626: 8:connection:5, vector coefficient.**

```math
\begin{aligned}
&32i\big(\bar\chi\gamma^{d}\gamma^{a}\gamma^{c}\chi\big)\,T_{cd}\\
&=32i\big(\bar\chi\gamma^{acd}\chi\big)\,T_{cd}\\
&=16\big(\bar\chi\gamma^{cd}\chi\big)\,\varepsilon_{cd}{}^{a}{}_{ef}\,T^{ef}
\end{aligned}\tag{G626}
```

**G627: 8:connection:5, bivector coefficient.**

```math
\begin{aligned}
&-16i\big(\bar\chi\gamma^{d}\gamma^{[ab]}\gamma^{c}\chi\big)\,T_{cd}\\
&=0
\end{aligned}\tag{G627}
```

#### Block 9

The original spinor term is $`\frac83\gamma_{ab}\widehat R_{cd}{}^i(Q)T^{ab}T^{cd}`$.

**G628: R4, whole coefficient matrix.**

```math
\begin{aligned}
&\frac{2}{3}\widehat C_{cdef}\,T_{gh}\,T^{cd}\,\gamma^{gh}\gamma^{ef}\\
&=\frac{2}{3}\widehat C_{cdef}\,T^{cd}\,T_{gh}\,\gamma^{efgh}\\
&-\frac{8}{3}\widehat C_{cdef}\,T^{cd}\,T^{f}{}_{g}\,\gamma^{eg}\\
&-\frac{4}{3}\widehat C_{cdef}\,T^{cd}\,T^{ef}\\
&=\frac{2i}{3}\widehat C_{cdef}\,\varepsilon^{ef}{}_{ghj}\,T^{cd}\,T^{hj}\,\gamma^{g}\\
&-\frac{8}{3}\widehat C_{cdef}\,T^{cd}\,T^{f}{}_{g}\,\gamma^{eg}\\
&-\frac{4}{3}\widehat C_{cdef}\,T^{cd}\,T^{ef}
\end{aligned}\tag{G628}
```

**G629: R5, whole coefficient matrix.**

```math
\begin{aligned}
&\frac{8i}{3}(\mathcal D_{c}T_{de})\,T_{fg}\,T^{c}{}_{h}\,\gamma^{fg}\gamma^{de}\gamma^{h}\\
&-\frac{8i}{3}(\mathcal D_{c}T_{de})\,T_{fg}\,T_{h}{}^{c}\,\gamma^{fg}\gamma^{de}\gamma^{h}\\
&=-\frac{16i}{3}T_{cd}\,T_{ef}\,(\mathcal D^{f}T_{gh})\,\gamma^{cdegh}\\
&-\frac{32i}{3}T_{cd}\,T^{d}{}_{e}\,(\mathcal D^{e}T_{fg})\,\gamma^{cfg}\\
&+\frac{32i}{3}T_{cd}\,T_{ef}\,(\mathcal D^{e}T_{g}{}^{f})\,\gamma^{cdg}\\
&+\frac{64i}{3}T_{cd}\,T_{ef}\,(\mathcal D^{d}T_{g}{}^{f})\,\gamma^{ceg}\\
&-\frac{64i}{3}T_{cd}\,T^{c}{}_{e}\,(\mathcal D^{d}T_{f}{}^{e})\,\gamma^{f}\\
&+\frac{64i}{3}T_{cd}\,T_{ef}\,(\mathcal D^{e}T^{df})\,\gamma^{c}\\
&+\frac{32i}{3}T_{cd}\,T_{ef}\,(\mathcal D^{d}T^{ef})\,\gamma^{c}\\
&=-\frac{8}{3}\varepsilon_{cdefg}\,T^{cd}\,T^{ef}\,(\mathcal D_{h}T^{gh})\\
&-\frac{16}{3}\varepsilon_{cdefg}\,T^{e}{}_{h}\,T^{h}{}_{j}\,(\mathcal D^{j}T^{fg})\,\gamma^{cd}\\
&+\frac{16}{3}\varepsilon_{cdefg}\,T^{ef}\,T_{hj}\,(\mathcal D^{h}T^{gj})\,\gamma^{cd}\\
&+\frac{32}{3}\varepsilon_{cdefg}\,T^{e}{}_{h}\,T^{f}{}_{j}\,(\mathcal D^{h}T^{gj})\,\gamma^{cd}\\
&-\frac{64i}{3}T_{cd}\,T^{c}{}_{e}\,(\mathcal D^{d}T_{f}{}^{e})\,\gamma^{f}\\
&+\frac{64i}{3}T_{cd}\,T_{ef}\,(\mathcal D^{e}T^{df})\,\gamma^{c}\\
&+\frac{32i}{3}T_{cd}\,T_{ef}\,(\mathcal D^{d}T^{ef})\,\gamma^{c}
\end{aligned}\tag{G629}
```

**G630: R6, whole coefficient matrix.**

```math
\begin{aligned}
&-\frac{8i}{9}(\mathcal D_{c}T_{de})\,T_{fg}\,T^{c}{}_{h}\,\gamma^{fg}\gamma^{h}\gamma^{de}\\
&+\frac{8i}{9}(\mathcal D_{c}T_{de})\,T_{fg}\,T_{h}{}^{c}\,\gamma^{fg}\gamma^{h}\gamma^{de}\\
&=\frac{16i}{9}T_{cd}\,T_{ef}\,(\mathcal D^{f}T_{gh})\,\gamma^{cdegh}\\
&-\frac{64i}{9}T_{cd}\,T_{ef}\,(\mathcal D^{d}T_{g}{}^{f})\,\gamma^{ceg}\\
&+\frac{32i}{9}T_{cd}\,T_{ef}\,(\mathcal D^{e}T_{g}{}^{f})\,\gamma^{cdg}\\
&-\frac{32i}{9}T_{cd}\,T_{ef}\,(\mathcal D^{d}T^{ef})\,\gamma^{c}\\
&+\frac{64i}{9}T_{cd}\,T_{ef}\,(\mathcal D^{e}T^{df})\,\gamma^{c}\\
&+\frac{32i}{9}T_{cd}\,T^{d}{}_{e}\,(\mathcal D^{e}T_{fg})\,\gamma^{cfg}\\
&+\frac{64i}{9}T_{cd}\,T^{c}{}_{e}\,(\mathcal D^{d}T_{f}{}^{e})\,\gamma^{f}\\
&=\frac{8}{9}\varepsilon_{cdefg}\,T^{cd}\,T^{ef}\,(\mathcal D_{h}T^{gh})\\
&-\frac{32}{9}\varepsilon_{cdefg}\,T^{e}{}_{h}\,T^{f}{}_{j}\,(\mathcal D^{h}T^{gj})\,\gamma^{cd}\\
&+\frac{16}{9}\varepsilon_{cdefg}\,T^{ef}\,T_{hj}\,(\mathcal D^{h}T^{gj})\,\gamma^{cd}\\
&-\frac{32i}{9}T_{cd}\,T_{ef}\,(\mathcal D^{d}T^{ef})\,\gamma^{c}\\
&+\frac{64i}{9}T_{cd}\,T_{ef}\,(\mathcal D^{e}T^{df})\,\gamma^{c}\\
&+\frac{16}{9}\varepsilon_{cdefg}\,T^{e}{}_{h}\,T^{h}{}_{j}\,(\mathcal D^{j}T^{fg})\,\gamma^{cd}\\
&+\frac{64i}{9}T_{cd}\,T^{c}{}_{e}\,(\mathcal D^{d}T_{f}{}^{e})\,\gamma^{f}
\end{aligned}\tag{G630}
```

**G631: R7, whole coefficient matrix.**

```math
\begin{aligned}
&-\frac{8i}{9}(\mathcal D_{c}T_{de})\,T_{fg}\,T_{hj}\,\gamma^{fg}\gamma^{h}\gamma^{c}\gamma^{de}\gamma^{j}\\
&+\frac{8i}{9}(\mathcal D_{c}T_{de})\,T_{fg}\,T_{hj}\,\gamma^{fg}\gamma^{j}\gamma^{c}\gamma^{de}\gamma^{h}\\
&=\frac{32i}{3}T_{cd}\,T_{ef}\,(\mathcal D_{g}T_{h}{}^{f})\,\gamma^{cdegh}\\
&-\frac{128i}{9}T_{cd}\,T^{d}{}_{e}\,(\mathcal D_{f}T_{g}{}^{e})\,\gamma^{cfg}\\
&-\frac{32i}{9}T_{cd}\,T_{ef}\,(\mathcal D_{g}T_{h}{}^{g})\,\gamma^{cdefh}\\
&-\frac{64i}{9}T_{cd}\,T_{ef}\,(\mathcal D_{g}T^{fg})\,\gamma^{cde}\\
&+\frac{64i}{9}T_{cd}\,T_{ef}\,(\mathcal D^{d}T^{ef})\,\gamma^{c}\\
&-\frac{128i}{9}T_{cd}\,T_{ef}\,(\mathcal D^{e}T^{df})\,\gamma^{c}\\
&+\frac{128i}{9}T_{cd}\,T^{d}{}_{e}\,(\mathcal D_{f}T^{ef})\,\gamma^{c}\\
&+\frac{16i}{3}T_{cd}\,T_{ef}\,(\mathcal D^{f}T_{gh})\,\gamma^{cdegh}\\
&-\frac{64i}{9}T_{cd}\,T^{d}{}_{e}\,(\mathcal D^{e}T_{fg})\,\gamma^{cfg}\\
&-\frac{32i}{9}T_{cd}\,T^{cd}\,(\mathcal D_{e}T_{fg})\,\gamma^{efg}\\
&+\frac{64i}{9}T_{cd}\,T^{cd}\,(\mathcal D_{e}T_{f}{}^{e})\,\gamma^{f}\\
&=\frac{32}{9}\varepsilon_{cdefg}\,T^{cd}\,T^{ef}\,(\mathcal D_{h}T^{gh})\\
&-\frac{64}{9}\varepsilon_{cdefg}\,T^{e}{}_{h}\,T^{h}{}_{j}\,(\mathcal D^{f}T^{gj})\,\gamma^{cd}\\
&-\frac{32}{9}\varepsilon_{cdefg}\,T^{ef}\,T^{g}{}_{h}\,(\mathcal D_{j}T^{hj})\,\gamma^{cd}\\
&+\frac{64i}{9}T_{cd}\,T_{ef}\,(\mathcal D^{d}T^{ef})\,\gamma^{c}\\
&-\frac{128i}{9}T_{cd}\,T_{ef}\,(\mathcal D^{e}T^{df})\,\gamma^{c}\\
&+\frac{128i}{9}T_{cd}\,T^{d}{}_{e}\,(\mathcal D_{f}T^{ef})\,\gamma^{c}\\
&-\frac{32}{9}\varepsilon_{cdefg}\,T^{e}{}_{h}\,T^{h}{}_{j}\,(\mathcal D^{j}T^{fg})\,\gamma^{cd}\\
&-\frac{16}{9}\varepsilon_{cdefg}\,T_{hj}\,T^{hj}\,(\mathcal D^{e}T^{fg})\,\gamma^{cd}\\
&+\frac{64i}{9}T_{cd}\,T^{cd}\,(\mathcal D_{e}T_{f}{}^{e})\,\gamma^{f}
\end{aligned}\tag{G631}
```

**G632: R8, whole coefficient matrix.**

```math
\begin{aligned}
&-\frac{16i}{9}(\mathcal D_{c}T^{c}{}_{d})\,T_{ef}\,T_{gh}\,\gamma^{ef}\gamma^{gh}\gamma^{d}\\
&=\frac{16i}{9}T_{cd}\,T_{ef}\,(\mathcal D_{g}T_{h}{}^{g})\,\gamma^{cdefh}\\
&+\frac{64i}{9}T_{cd}\,T_{ef}\,(\mathcal D_{g}T^{fg})\,\gamma^{cde}\\
&-\frac{32i}{9}T_{cd}\,T^{cd}\,(\mathcal D_{e}T_{f}{}^{e})\,\gamma^{f}\\
&=-\frac{16}{9}\varepsilon_{cdefg}\,T^{cd}\,T^{ef}\,(\mathcal D_{h}T^{gh})\\
&+\frac{32}{9}\varepsilon_{cdefg}\,T^{ef}\,T^{g}{}_{h}\,(\mathcal D_{j}T^{hj})\,\gamma^{cd}\\
&-\frac{32i}{9}T_{cd}\,T^{cd}\,(\mathcal D_{e}T_{f}{}^{e})\,\gamma^{f}
\end{aligned}\tag{G632}
```

**G633: Tfirst1, scalar coefficient.**

```math
\begin{aligned}
&-\frac{i}{6}\big(\bar\chi\gamma^{ef}\gamma_{ef}\widehat R(Q)_{cd}\big)\,T^{cd}\\
&=-\frac{10i}{3}\big(\overline{\widehat R(Q)_{cd}}\chi\big)\,T^{cd}
\end{aligned}\tag{G633}
```

**G634: Tfirst1, vector coefficient.**

```math
\begin{aligned}
&-\frac{i}{6}\big(\bar\chi\gamma^{ef}\gamma^{a}\gamma_{ef}\widehat R(Q)_{cd}\big)\,T^{cd}\\
&=-\frac{2i}{3}\big(\overline{\widehat R(Q)_{cd}}\gamma^{a}\chi\big)\,T^{cd}
\end{aligned}\tag{G634}
```

**G635: Tfirst1, bivector coefficient.**

```math
\begin{aligned}
&\frac{i}{12}\big(\bar\chi\gamma^{ef}\gamma^{[ab]}\gamma_{ef}\widehat R(Q)_{cd}\big)\,T^{cd}\\
&=\frac{i}{3}\big(\overline{\widehat R(Q)_{cd}}\gamma^{[ab]}\chi\big)\,T^{cd}
\end{aligned}\tag{G635}
```

**G636: Tfirst2, scalar coefficient.**

```math
\begin{aligned}
&-\frac{i}{32}\big(\overline{\widehat R(Q)_{ef}}\gamma^{ef}\widehat R(Q)_{cd}\big)\,T^{cd}\\
&=0
\end{aligned}\tag{G636}
```

**G637: Tfirst2, vector coefficient.**

```math
\begin{aligned}
&-\frac{i}{32}\big(\overline{\widehat R(Q)_{ef}}\gamma^{a}\gamma^{ef}\widehat R(Q)_{cd}\big)\,T^{cd}\\
&=0
\end{aligned}\tag{G637}
```

**G638: Tfirst2, bivector coefficient.**

```math
\begin{aligned}
&\frac{i}{64}\big(\overline{\widehat R(Q)_{ef}}\gamma^{[ab]}\gamma^{ef}\widehat R(Q)_{cd}\big)\,T^{cd}\\
&=-\frac{i}{8}\big(\overline{\widehat R(Q)^{[ab]}}\widehat R(Q)_{cd}\big)\,T^{cd}
\end{aligned}\tag{G638}
```

**G639: Tsecond1, scalar coefficient.**

```math
\begin{aligned}
&-\frac{i}{6}\big(\bar\chi\gamma^{ef}\gamma^{cd}\widehat R(Q)_{ef}\big)\,T_{cd}\\
&=-\frac{4i}{3}\big(\overline{\widehat R(Q)_{cd}}\chi\big)\,T^{cd}
\end{aligned}\tag{G639}
```

**G640: Tsecond1, vector coefficient.**

```math
\begin{aligned}
&-\frac{i}{6}\big(\bar\chi\gamma^{ef}\gamma^{a}\gamma^{cd}\widehat R(Q)_{ef}\big)\,T_{cd}\\
&=-\frac{4i}{3}\big(\overline{\widehat R(Q)_{cd}}\gamma^{a}\chi\big)\,T^{cd}\\
&-\frac{8i}{3}\big(\overline{\widehat R(Q)^{a}{}_{c}}\gamma^{d}\chi\big)\,T^{c}{}_{d}
\end{aligned}\tag{G640}
```

**G641: Tsecond1, bivector coefficient.**

```math
\begin{aligned}
&\frac{i}{12}\big(\bar\chi\gamma^{ef}\gamma^{[ab]}\gamma^{cd}\widehat R(Q)_{ef}\big)\,T_{cd}\\
&=-\frac{i}{2}\big(\overline{\widehat R(Q)_{cd}}\gamma^{[ab]}\chi\big)\,T^{cd}\\
&+2i\big(\overline{\widehat R(Q)^{[a}{}_{|c|}}\gamma^{b]d}\chi\big)\,T^{c}{}_{d}\\
&-\frac{8i}{3}\big(\overline{\widehat R(Q)^{[a}{}_{|c|}}\chi\big)\,T^{|c|b]}\\
&-\frac{i}{2}\big(\overline{\widehat R(Q)^{[ab]}}\gamma^{cd}\chi\big)\,T_{cd}
\end{aligned}\tag{G641}
```

**G642: Tsecond2, scalar coefficient.**

```math
\begin{aligned}
&-\frac{i}{32}\big(\overline{\widehat R(Q)_{ef}}\gamma^{cd}\widehat R(Q)^{ef}\big)\,T_{cd}\\
&=-\frac{i}{32}\big(\overline{\widehat R(Q)_{ef}}\gamma^{cd}\widehat R(Q)^{ef}\big)\,T_{cd}
\end{aligned}\tag{G642}
```

**G643: Tsecond2, vector coefficient.**

```math
\begin{aligned}
&-\frac{i}{32}\big(\overline{\widehat R(Q)_{ef}}\gamma^{a}\gamma^{cd}\widehat R(Q)^{ef}\big)\,T_{cd}\\
&=-\frac{i}{32}\big(\overline{\widehat R(Q)_{ef}}\gamma^{acd}\widehat R(Q)^{ef}\big)\,T_{cd}\\
&=-\frac{1}{64}\big(\overline{\widehat R(Q)_{gh}}\gamma^{cd}\widehat R(Q)^{gh}\big)\,\varepsilon_{cd}{}^{a}{}_{ef}\,T^{ef}
\end{aligned}\tag{G643}
```

**G644: Tsecond2, bivector coefficient.**

```math
\begin{aligned}
&\frac{i}{64}\big(\overline{\widehat R(Q)_{ef}}\gamma^{[ab]}\gamma^{cd}\widehat R(Q)^{ef}\big)\,T_{cd}\\
&=-\frac{i}{16}\big(\overline{\widehat R(Q)_{de}}\gamma^{[a|c|}\widehat R(Q)^{|de|}\big)\,T_{|c|}{}^{b]}
\end{aligned}\tag{G644}
```

#### Block 10

The original spinor term is $`\frac12\widehat R^{ab\,i}{}_{j}(V)\widehat R_{ab}{}^j(Q)`$.

**G645: V1, scalar coefficient.**

```math
\begin{aligned}
&-\frac{9}{64}\big(\overline{\mathcal D_{c}\widehat R(Q)_{de}}\gamma^{c}\widehat R(Q)^{de}\big)\\
&=\frac{9}{64}\big(\overline{\widehat R(Q)_{de}}\gamma^{c}\mathcal D_{c}\widehat R(Q)^{de}\big)
\end{aligned}\tag{G645}
```

**G646: V1, vector coefficient.**

```math
\begin{aligned}
&-\frac{9}{64}\big(\overline{\mathcal D_{c}\widehat R(Q)_{de}}\gamma^{c}\gamma^{a}\widehat R(Q)^{de}\big)\\
&=-\frac{9}{64}\big(\overline{\widehat R(Q)_{de}}\gamma^{ca}\mathcal D_{c}\widehat R(Q)^{de}\big)\\
&+\frac{9}{64}\big(\overline{\widehat R(Q)_{cd}}\mathcal D^{a}\widehat R(Q)^{cd}\big)
\end{aligned}\tag{G646}
```

**G647: V1, bivector coefficient.**

```math
\begin{aligned}
&\frac{9}{128}\big(\overline{\mathcal D_{c}\widehat R(Q)_{de}}\gamma^{c}\gamma^{[ab]}\widehat R(Q)^{de}\big)\\
&=\frac{9}{128}\big(\overline{\widehat R(Q)_{de}}\gamma^{c[ab]}\mathcal D_{c}\widehat R(Q)^{de}\big)\\
&+\frac{9}{64}\big(\overline{\widehat R(Q)_{cd}}\gamma^{[a}\mathcal D^{b]}\widehat R(Q)^{cd}\big)\\
&=-\frac{9i}{256}\big(\overline{\widehat R(Q)_{fg}}\gamma^{cd}\mathcal D_{e}\widehat R(Q)^{fg}\big)\,\varepsilon_{cd}{}^{e[ab]}\\
&+\frac{9}{64}\big(\overline{\widehat R(Q)_{cd}}\gamma^{[a}\mathcal D^{b]}\widehat R(Q)^{cd}\big)
\end{aligned}\tag{G647}
```

**G648: V2, scalar coefficient.**

```math
\begin{aligned}
&-\frac{9}{128}\big(\overline{\mathcal D_{d}\widehat R(Q)_{e}{}^{d}}\gamma^{c}\widehat R(Q)_{c}{}^{e}\big)\\
&+\frac{9}{128}\big(\overline{\mathcal D_{d}\widehat R(Q)_{e}{}^{d}}\gamma^{c}\widehat R(Q)^{e}{}_{c}\big)\\
&=0
\end{aligned}\tag{G648}
```

**G649: V2, vector coefficient.**

```math
\begin{aligned}
&-\frac{9}{128}\big(\overline{\mathcal D_{d}\widehat R(Q)_{e}{}^{d}}\gamma^{c}\gamma^{a}\widehat R(Q)_{c}{}^{e}\big)\\
&+\frac{9}{128}\big(\overline{\mathcal D_{d}\widehat R(Q)_{e}{}^{d}}\gamma^{c}\gamma^{a}\widehat R(Q)^{e}{}_{c}\big)\\
&=-\frac{9}{32}\big(\overline{\widehat R(Q)_{c}{}^{a}}\mathcal D_{d}\widehat R(Q)^{cd}\big)
\end{aligned}\tag{G649}
```

**G650: V2, bivector coefficient.**

```math
\begin{aligned}
&\frac{9}{256}\big(\overline{\mathcal D_{d}\widehat R(Q)_{e}{}^{d}}\gamma^{c}\gamma^{[ab]}\widehat R(Q)_{c}{}^{e}\big)\\
&-\frac{9}{256}\big(\overline{\mathcal D_{d}\widehat R(Q)_{e}{}^{d}}\gamma^{c}\gamma^{[ab]}\widehat R(Q)^{e}{}_{c}\big)\\
&=\frac{9}{32}\big(\overline{\widehat R(Q)_{c}{}^{[a}}\gamma^{b]}\mathcal D_{d}\widehat R(Q)^{cd}\big)
\end{aligned}\tag{G650}
```

**G651: V3, scalar coefficient.**

```math
\begin{aligned}
&-\frac{3i}{8}\big(\overline{\widehat R(Q)_{cd}}\gamma^{ef}\widehat R(Q)_{ef}\big)\,T^{cd}\\
&=0
\end{aligned}\tag{G651}
```

**G652: V3, vector coefficient.**

```math
\begin{aligned}
&-\frac{3i}{8}\big(\overline{\widehat R(Q)_{cd}}\gamma^{ef}\gamma^{a}\widehat R(Q)_{ef}\big)\,T^{cd}\\
&=0
\end{aligned}\tag{G652}
```

**G653: V3, bivector coefficient.**

```math
\begin{aligned}
&\frac{3i}{16}\big(\overline{\widehat R(Q)_{cd}}\gamma^{ef}\gamma^{[ab]}\widehat R(Q)_{ef}\big)\,T^{cd}\\
&=\frac{3i}{2}\big(\overline{\widehat R(Q)^{[ab]}}\widehat R(Q)_{cd}\big)\,T^{cd}
\end{aligned}\tag{G653}
```

**G654: V4, scalar coefficient.**

```math
\begin{aligned}
&-\frac{27i}{32}\big(\overline{\widehat R(Q)_{fc}}\gamma^{e}\gamma^{d}\widehat R(Q)_{e}{}^{f}\big)\,T^{c}{}_{d}\\
&+\frac{27i}{32}\big(\overline{\widehat R(Q)_{fc}}\gamma^{e}\gamma^{d}\widehat R(Q)^{f}{}_{e}\big)\,T^{c}{}_{d}\\
&=\frac{27i}{8}\big(\overline{\widehat R(Q)_{ec}}\widehat R(Q)^{e}{}_{d}\big)\,T^{cd}
\end{aligned}\tag{G654}
```

**G655: V4, vector coefficient.**

```math
\begin{aligned}
&-\frac{27i}{32}\big(\overline{\widehat R(Q)_{fc}}\gamma^{e}\gamma^{d}\gamma^{a}\widehat R(Q)_{e}{}^{f}\big)\,T^{c}{}_{d}\\
&+\frac{27i}{32}\big(\overline{\widehat R(Q)_{fc}}\gamma^{e}\gamma^{d}\gamma^{a}\widehat R(Q)^{f}{}_{e}\big)\,T^{c}{}_{d}\\
&=\frac{27i}{8}\big(\overline{\widehat R(Q)_{ec}}\gamma^{a}\widehat R(Q)^{e}{}_{d}\big)\,T^{cd}\\
&-\frac{27i}{8}\big(\overline{\widehat R(Q)_{e}{}^{a}}\gamma^{c}\widehat R(Q)^{e}{}_{d}\big)\,T_{c}{}^{d}
\end{aligned}\tag{G655}
```

**G656: V4, bivector coefficient.**

```math
\begin{aligned}
&\frac{27i}{64}\big(\overline{\widehat R(Q)_{fc}}\gamma^{e}\gamma^{d}\gamma^{[ab]}\widehat R(Q)_{e}{}^{f}\big)\,T^{c}{}_{d}\\
&-\frac{27i}{64}\big(\overline{\widehat R(Q)_{fc}}\gamma^{e}\gamma^{d}\gamma^{[ab]}\widehat R(Q)^{f}{}_{e}\big)\,T^{c}{}_{d}\\
&=\frac{27i}{8}\big(\overline{\widehat R(Q)_{e}{}^{[a}}\gamma^{b]c}\widehat R(Q)^{e}{}_{d}\big)\,T_{c}{}^{d}\\
&-\frac{27i}{8}\big(\overline{\widehat R(Q)_{d}{}^{[a}}\widehat R(Q)^{|d|}{}_{|c|}\big)\,T^{|c|b]}
\end{aligned}\tag{G656}
```

**G657: V5, scalar coefficient.**

```math
\begin{aligned}
&-\frac{27i}{64}\big(\overline{\widehat R(Q)_{ef}}\gamma^{cd}\widehat R(Q)^{ef}\big)\,T_{cd}\\
&=-\frac{27i}{64}\big(\overline{\widehat R(Q)_{ef}}\gamma^{cd}\widehat R(Q)^{ef}\big)\,T_{cd}
\end{aligned}\tag{G657}
```

**G658: V5, vector coefficient.**

```math
\begin{aligned}
&-\frac{27i}{64}\big(\overline{\widehat R(Q)_{ef}}\gamma^{cd}\gamma^{a}\widehat R(Q)^{ef}\big)\,T_{cd}\\
&=-\frac{27i}{64}\big(\overline{\widehat R(Q)_{ef}}\gamma^{acd}\widehat R(Q)^{ef}\big)\,T_{cd}\\
&=-\frac{27}{128}\big(\overline{\widehat R(Q)_{gh}}\gamma^{cd}\widehat R(Q)^{gh}\big)\,\varepsilon_{cd}{}^{a}{}_{ef}\,T^{ef}
\end{aligned}\tag{G658}
```

**G659: V5, bivector coefficient.**

```math
\begin{aligned}
&\frac{27i}{128}\big(\overline{\widehat R(Q)_{ef}}\gamma^{cd}\gamma^{[ab]}\widehat R(Q)^{ef}\big)\,T_{cd}\\
&=\frac{27i}{32}\big(\overline{\widehat R(Q)_{de}}\gamma^{[a|c|}\widehat R(Q)^{|de|}\big)\,T_{|c|}{}^{b]}
\end{aligned}\tag{G659}
```

**G660: V6, scalar coefficient.**

```math
\begin{aligned}
&\frac{9i}{16}\big(\overline{\widehat R(Q)_{ec}}\widehat R(Q)_{d}{}^{e}\big)\,T^{cd}\\
&-\frac{9i}{16}\big(\overline{\widehat R(Q)_{ec}}\widehat R(Q)^{e}{}_{d}\big)\,T^{cd}\\
&=-\frac{9i}{8}\big(\overline{\widehat R(Q)_{ec}}\widehat R(Q)^{e}{}_{d}\big)\,T^{cd}
\end{aligned}\tag{G660}
```

**G661: V6, vector coefficient.**

```math
\begin{aligned}
&\frac{9i}{16}\big(\overline{\widehat R(Q)_{ec}}\gamma^{a}\widehat R(Q)_{d}{}^{e}\big)\,T^{cd}\\
&-\frac{9i}{16}\big(\overline{\widehat R(Q)_{ec}}\gamma^{a}\widehat R(Q)^{e}{}_{d}\big)\,T^{cd}\\
&=-\frac{9i}{8}\big(\overline{\widehat R(Q)_{ec}}\gamma^{a}\widehat R(Q)^{e}{}_{d}\big)\,T^{cd}
\end{aligned}\tag{G661}
```

**G662: V6, bivector coefficient.**

```math
\begin{aligned}
&-\frac{9i}{32}\big(\overline{\widehat R(Q)_{ec}}\gamma^{[ab]}\widehat R(Q)_{d}{}^{e}\big)\,T^{cd}\\
&+\frac{9i}{32}\big(\overline{\widehat R(Q)_{ec}}\gamma^{[ab]}\widehat R(Q)^{e}{}_{d}\big)\,T^{cd}\\
&=0
\end{aligned}\tag{G662}
```

**G663: V7, scalar coefficient.**

```math
\begin{aligned}
&-\frac{3}{8}\big(\overline{\mathcal D_{d}\chi}\gamma^{c}\widehat R(Q)_{c}{}^{d}\big)\\
&+\frac{3}{8}\big(\overline{\mathcal D_{d}\chi}\gamma^{c}\widehat R(Q)^{d}{}_{c}\big)\\
&=0
\end{aligned}\tag{G663}
```

**G664: V7, vector coefficient.**

```math
\begin{aligned}
&-\frac{3}{8}\big(\overline{\mathcal D_{d}\chi}\gamma^{c}\gamma^{a}\widehat R(Q)_{c}{}^{d}\big)\\
&+\frac{3}{8}\big(\overline{\mathcal D_{d}\chi}\gamma^{c}\gamma^{a}\widehat R(Q)^{d}{}_{c}\big)\\
&=-\frac{3}{2}\big(\overline{\widehat R(Q)_{c}{}^{a}}\mathcal D^{c}\chi\big)
\end{aligned}\tag{G664}
```

**G665: V7, bivector coefficient.**

```math
\begin{aligned}
&\frac{3}{16}\big(\overline{\mathcal D_{d}\chi}\gamma^{c}\gamma^{[ab]}\widehat R(Q)_{c}{}^{d}\big)\\
&-\frac{3}{16}\big(\overline{\mathcal D_{d}\chi}\gamma^{c}\gamma^{[ab]}\widehat R(Q)^{d}{}_{c}\big)\\
&=\frac{3}{2}\big(\overline{\widehat R(Q)_{c}{}^{[a}}\gamma^{b]}\mathcal D^{c}\chi\big)
\end{aligned}\tag{G665}
```

**G666: V8, scalar coefficient.**

```math
\begin{aligned}
&-\frac{3i}{32}\big(\overline{\widehat R(Q)_{ef}}\gamma^{cd}\widehat R(Q)^{ef}\big)\,T_{cd}\\
&=-\frac{3i}{32}\big(\overline{\widehat R(Q)_{ef}}\gamma^{cd}\widehat R(Q)^{ef}\big)\,T_{cd}
\end{aligned}\tag{G666}
```

**G667: V8, vector coefficient.**

```math
\begin{aligned}
&-\frac{3i}{32}\big(\overline{\widehat R(Q)_{ef}}\gamma^{cd}\gamma^{a}\widehat R(Q)^{ef}\big)\,T_{cd}\\
&=-\frac{3i}{32}\big(\overline{\widehat R(Q)_{ef}}\gamma^{acd}\widehat R(Q)^{ef}\big)\,T_{cd}\\
&=-\frac{3}{64}\big(\overline{\widehat R(Q)_{gh}}\gamma^{cd}\widehat R(Q)^{gh}\big)\,\varepsilon_{cd}{}^{a}{}_{ef}\,T^{ef}
\end{aligned}\tag{G667}
```

**G668: V8, bivector coefficient.**

```math
\begin{aligned}
&\frac{3i}{64}\big(\overline{\widehat R(Q)_{ef}}\gamma^{cd}\gamma^{[ab]}\widehat R(Q)^{ef}\big)\,T_{cd}\\
&=\frac{3i}{16}\big(\overline{\widehat R(Q)_{de}}\gamma^{[a|c|}\widehat R(Q)^{|de|}\big)\,T_{|c|}{}^{b]}
\end{aligned}\tag{G668}
```

**G669: V9, scalar coefficient.**

```math
\begin{aligned}
&\frac{3i}{8}\big(\bar\chi\gamma^{e}\gamma^{cd}\gamma^{f}\widehat R(Q)_{ef}\big)\,T_{cd}\\
&-\frac{3i}{8}\big(\bar\chi\gamma^{e}\gamma^{cd}\gamma^{f}\widehat R(Q)_{fe}\big)\,T_{cd}\\
&=0
\end{aligned}\tag{G669}
```

**G670: V9, vector coefficient.**

```math
\begin{aligned}
&\frac{3i}{8}\big(\bar\chi\gamma^{e}\gamma^{cd}\gamma^{f}\gamma^{a}\widehat R(Q)_{ef}\big)\,T_{cd}\\
&-\frac{3i}{8}\big(\bar\chi\gamma^{e}\gamma^{cd}\gamma^{f}\gamma^{a}\widehat R(Q)_{fe}\big)\,T_{cd}\\
&=6i\big(\overline{\widehat R(Q)^{a}{}_{c}}\gamma^{d}\chi\big)\,T^{c}{}_{d}
\end{aligned}\tag{G670}
```

**G671: V9, bivector coefficient.**

```math
\begin{aligned}
&-\frac{3i}{16}\big(\bar\chi\gamma^{e}\gamma^{cd}\gamma^{f}\gamma^{[ab]}\widehat R(Q)_{ef}\big)\,T_{cd}\\
&+\frac{3i}{16}\big(\bar\chi\gamma^{e}\gamma^{cd}\gamma^{f}\gamma^{[ab]}\widehat R(Q)_{fe}\big)\,T_{cd}\\
&=\frac{9i}{4}\big(\overline{\widehat R(Q)^{[ab]}}\gamma^{cd}\chi\big)\,T_{cd}\\
&-3i\big(\overline{\widehat R(Q)^{[a}{}_{|c|}}\gamma^{b]d}\chi\big)\,T^{c}{}_{d}\\
&-6i\big(\overline{\widehat R(Q)^{[a}{}_{|c|}}\chi\big)\,T^{|c|b]}\\
&-\frac{3i}{4}\big(\overline{\widehat R(Q)_{cd}}\gamma^{[ab]}\chi\big)\,T^{cd}
\end{aligned}\tag{G671}
```

**G672: R1, whole coefficient matrix.**

```math
\begin{aligned}
&-\frac{1}{24}\widehat R(V)_{cd}{}^{rs}\,\widehat R(V)_{ef}{}_{rs}\,\gamma^{cdef}\\
&=-\frac{i}{24}\varepsilon_{cdefg}\,\widehat R(V)^{de}{}^{rs}\,\widehat R(V)^{fg}{}_{rs}\,\gamma^{c}
\end{aligned}\tag{G672}
```

**G673: R2, whole coefficient matrix.**

```math
\begin{aligned}
&\frac{1}{24}\widehat R(V)_{cd}{}^{rs}\,\widehat R(V)_{ef}{}_{rs}\,\gamma^{ef}\gamma^{cd}\\
&=\frac{1}{24}\widehat R(V)_{cd}{}^{rs}\,\widehat R(V)_{ef}{}_{rs}\,\gamma^{cdef}\\
&-\frac{1}{12}\widehat R(V)_{cd}{}^{rs}\,\widehat R(V)^{cd}{}_{rs}\\
&=\frac{i}{24}\varepsilon_{cdefg}\,\widehat R(V)^{de}{}^{rs}\,\widehat R(V)^{fg}{}_{rs}\,\gamma^{c}\\
&-\frac{1}{12}\widehat R(V)_{cd}{}^{rs}\,\widehat R(V)^{cd}{}_{rs}
\end{aligned}\tag{G673}
```

**G674: R3, whole coefficient matrix.**

```math
\begin{aligned}
&\frac{1}{48}\widehat R(V)_{cd}{}^{rs}\,\widehat R(V)_{ef}{}_{rs}\,\gamma^{cd}\gamma^{ef}\\
&=\frac{1}{48}\widehat R(V)_{cd}{}^{rs}\,\widehat R(V)_{ef}{}_{rs}\,\gamma^{cdef}\\
&-\frac{1}{24}\widehat R(V)_{cd}{}^{rs}\,\widehat R(V)^{cd}{}_{rs}\\
&=\frac{i}{48}\varepsilon_{cdefg}\,\widehat R(V)^{de}{}^{rs}\,\widehat R(V)^{fg}{}_{rs}\,\gamma^{c}\\
&-\frac{1}{24}\widehat R(V)_{cd}{}^{rs}\,\widehat R(V)^{cd}{}_{rs}
\end{aligned}\tag{G674}
```

#### Block 11

The original spinor term is $`-\frac83\widehat R^{ab\,i}{}_{j}(V)\gamma_{ab}\chi^j`$.

**G675: V1, scalar coefficient.**

```math
\begin{aligned}
&\frac{3}{4}\big(\overline{\mathcal D_{c}\widehat R(Q)_{de}}\gamma^{c}\gamma^{de}\chi\big)\\
&=0
\end{aligned}\tag{G675}
```

**G676: V1, vector coefficient.**

```math
\begin{aligned}
&\frac{3}{4}\big(\overline{\mathcal D_{c}\widehat R(Q)_{de}}\gamma^{c}\gamma^{a}\gamma^{de}\chi\big)\\
&=6\big(\bar\chi\mathcal D_{c}\widehat R(Q)^{ca}\big)
\end{aligned}\tag{G676}
```

**G677: V1, bivector coefficient.**

```math
\begin{aligned}
&-\frac{3}{8}\big(\overline{\mathcal D_{c}\widehat R(Q)_{de}}\gamma^{c}\gamma^{[ab]}\gamma^{de}\chi\big)\\
&=6\big(\bar\chi\gamma^{[a}\mathcal D_{|c|}\widehat R(Q)^{|c|b]}\big)\\
&-3\big(\bar\chi\gamma^{c}\mathcal D_{c}\widehat R(Q)^{[ab]}\big)
\end{aligned}\tag{G677}
```

**G678: V2, scalar coefficient.**

```math
\begin{aligned}
&\frac{3}{8}\big(\overline{\mathcal D_{e}\widehat R(Q)_{d}{}^{e}}\gamma^{c}\gamma_{c}{}^{d}\chi\big)\\
&-\frac{3}{8}\big(\overline{\mathcal D_{e}\widehat R(Q)_{d}{}^{e}}\gamma^{c}\gamma^{d}{}_{c}\chi\big)\\
&=0
\end{aligned}\tag{G678}
```

**G679: V2, vector coefficient.**

```math
\begin{aligned}
&\frac{3}{8}\big(\overline{\mathcal D_{e}\widehat R(Q)_{d}{}^{e}}\gamma^{c}\gamma^{a}\gamma_{c}{}^{d}\chi\big)\\
&-\frac{3}{8}\big(\overline{\mathcal D_{e}\widehat R(Q)_{d}{}^{e}}\gamma^{c}\gamma^{a}\gamma^{d}{}_{c}\chi\big)\\
&=-\frac{9}{2}\big(\bar\chi\mathcal D_{c}\widehat R(Q)^{ca}\big)
\end{aligned}\tag{G679}
```

**G680: V2, bivector coefficient.**

```math
\begin{aligned}
&-\frac{3}{16}\big(\overline{\mathcal D_{e}\widehat R(Q)_{d}{}^{e}}\gamma^{c}\gamma^{[ab]}\gamma_{c}{}^{d}\chi\big)\\
&+\frac{3}{16}\big(\overline{\mathcal D_{e}\widehat R(Q)_{d}{}^{e}}\gamma^{c}\gamma^{[ab]}\gamma^{d}{}_{c}\chi\big)\\
&=-\frac{3}{2}\big(\bar\chi\gamma^{[a}\mathcal D_{|c|}\widehat R(Q)^{|c|b]}\big)
\end{aligned}\tag{G680}
```

**G681: V3, scalar coefficient.**

```math
\begin{aligned}
&2i\big(\overline{\widehat R(Q)_{cd}}\gamma^{ef}\gamma_{ef}\chi\big)\,T^{cd}\\
&=-40i\big(\overline{\widehat R(Q)_{cd}}\chi\big)\,T^{cd}
\end{aligned}\tag{G681}
```

**G682: V3, vector coefficient.**

```math
\begin{aligned}
&2i\big(\overline{\widehat R(Q)_{cd}}\gamma^{ef}\gamma^{a}\gamma_{ef}\chi\big)\,T^{cd}\\
&=-8i\big(\overline{\widehat R(Q)_{cd}}\gamma^{a}\chi\big)\,T^{cd}
\end{aligned}\tag{G682}
```

**G683: V3, bivector coefficient.**

```math
\begin{aligned}
&-i\big(\overline{\widehat R(Q)_{cd}}\gamma^{ef}\gamma^{[ab]}\gamma_{ef}\chi\big)\,T^{cd}\\
&=-4i\big(\overline{\widehat R(Q)_{cd}}\gamma^{[ab]}\chi\big)\,T^{cd}
\end{aligned}\tag{G683}
```

**G684: V4, scalar coefficient.**

```math
\begin{aligned}
&\frac{9i}{2}\big(\overline{\widehat R(Q)_{fc}}\gamma^{e}\gamma^{d}\gamma_{e}{}^{f}\chi\big)\,T^{c}{}_{d}\\
&-\frac{9i}{2}\big(\overline{\widehat R(Q)_{fc}}\gamma^{e}\gamma^{d}\gamma^{f}{}_{e}\chi\big)\,T^{c}{}_{d}\\
&=54i\big(\overline{\widehat R(Q)_{cd}}\chi\big)\,T^{cd}
\end{aligned}\tag{G684}
```

**G685: V4, vector coefficient.**

```math
\begin{aligned}
&\frac{9i}{2}\big(\overline{\widehat R(Q)_{fc}}\gamma^{e}\gamma^{d}\gamma^{a}\gamma_{e}{}^{f}\chi\big)\,T^{c}{}_{d}\\
&-\frac{9i}{2}\big(\overline{\widehat R(Q)_{fc}}\gamma^{e}\gamma^{d}\gamma^{a}\gamma^{f}{}_{e}\chi\big)\,T^{c}{}_{d}\\
&=18i\big(\overline{\widehat R(Q)_{cd}}\gamma^{a}\chi\big)\,T^{cd}\\
&+18i\big(\overline{\widehat R(Q)^{a}{}_{c}}\gamma^{d}\chi\big)\,T^{c}{}_{d}
\end{aligned}\tag{G685}
```

**G686: V4, bivector coefficient.**

```math
\begin{aligned}
&-\frac{9i}{4}\big(\overline{\widehat R(Q)_{fc}}\gamma^{e}\gamma^{d}\gamma^{[ab]}\gamma_{e}{}^{f}\chi\big)\,T^{c}{}_{d}\\
&+\frac{9i}{4}\big(\overline{\widehat R(Q)_{fc}}\gamma^{e}\gamma^{d}\gamma^{[ab]}\gamma^{f}{}_{e}\chi\big)\,T^{c}{}_{d}\\
&=9i\big(\overline{\widehat R(Q)_{cd}}\gamma^{[ab]}\chi\big)\,T^{cd}\\
&-18i\big(\overline{\widehat R(Q)^{[a}{}_{|c|}}\gamma^{b]d}\chi\big)\,T^{c}{}_{d}\\
&-54i\big(\overline{\widehat R(Q)^{[a}{}_{|c|}}\chi\big)\,T^{|c|b]}
\end{aligned}\tag{G686}
```

**G687: V5, scalar coefficient.**

```math
\begin{aligned}
&\frac{9i}{4}\big(\overline{\widehat R(Q)_{ef}}\gamma^{cd}\gamma^{ef}\chi\big)\,T_{cd}\\
&=-18i\big(\overline{\widehat R(Q)_{cd}}\chi\big)\,T^{cd}
\end{aligned}\tag{G687}
```

**G688: V5, vector coefficient.**

```math
\begin{aligned}
&\frac{9i}{4}\big(\overline{\widehat R(Q)_{ef}}\gamma^{cd}\gamma^{a}\gamma^{ef}\chi\big)\,T_{cd}\\
&=-36i\big(\overline{\widehat R(Q)^{a}{}_{c}}\gamma^{d}\chi\big)\,T^{c}{}_{d}\\
&-18i\big(\overline{\widehat R(Q)_{cd}}\gamma^{a}\chi\big)\,T^{cd}
\end{aligned}\tag{G688}
```

**G689: V5, bivector coefficient.**

```math
\begin{aligned}
&-\frac{9i}{8}\big(\overline{\widehat R(Q)_{ef}}\gamma^{cd}\gamma^{[ab]}\gamma^{ef}\chi\big)\,T_{cd}\\
&=\frac{27i}{4}\big(\overline{\widehat R(Q)^{[ab]}}\gamma^{cd}\chi\big)\,T_{cd}\\
&-27i\big(\overline{\widehat R(Q)^{[a}{}_{|c|}}\gamma^{b]d}\chi\big)\,T^{c}{}_{d}\\
&+\frac{27i}{4}\big(\overline{\widehat R(Q)_{cd}}\gamma^{[ab]}\chi\big)\,T^{cd}\\
&+36i\big(\overline{\widehat R(Q)^{[a}{}_{|c|}}\chi\big)\,T^{|c|b]}
\end{aligned}\tag{G689}
```

**G690: V6, scalar coefficient.**

```math
\begin{aligned}
&-3i\big(\overline{\widehat R(Q)_{ec}}\gamma^{de}\chi\big)\,T^{c}{}_{d}\\
&+3i\big(\overline{\widehat R(Q)_{ec}}\gamma^{ed}\chi\big)\,T^{c}{}_{d}\\
&=6i\big(\overline{\widehat R(Q)_{cd}}\chi\big)\,T^{cd}
\end{aligned}\tag{G690}
```

**G691: V6, vector coefficient.**

```math
\begin{aligned}
&-3i\big(\overline{\widehat R(Q)_{ec}}\gamma^{a}\gamma^{de}\chi\big)\,T^{c}{}_{d}\\
&+3i\big(\overline{\widehat R(Q)_{ec}}\gamma^{a}\gamma^{ed}\chi\big)\,T^{c}{}_{d}\\
&=6i\big(\overline{\widehat R(Q)_{cd}}\gamma^{a}\chi\big)\,T^{cd}\\
&+12i\big(\overline{\widehat R(Q)^{a}{}_{c}}\gamma^{d}\chi\big)\,T^{c}{}_{d}
\end{aligned}\tag{G691}
```

**G692: V6, bivector coefficient.**

```math
\begin{aligned}
&\frac{3i}{2}\big(\overline{\widehat R(Q)_{ec}}\gamma^{[ab]}\gamma^{de}\chi\big)\,T^{c}{}_{d}\\
&-\frac{3i}{2}\big(\overline{\widehat R(Q)_{ec}}\gamma^{[ab]}\gamma^{ed}\chi\big)\,T^{c}{}_{d}\\
&=-3i\big(\overline{\widehat R(Q)_{cd}}\gamma^{[ab]}\chi\big)\,T^{cd}\\
&+12i\big(\overline{\widehat R(Q)^{[a}{}_{|c|}}\gamma^{b]d}\chi\big)\,T^{c}{}_{d}\\
&+12i\big(\overline{\widehat R(Q)^{[a}{}_{|c|}}\chi\big)\,T^{|c|b]}
\end{aligned}\tag{G692}
```

**G693: V7, scalar coefficient.**

```math
\begin{aligned}
&2\big(\overline{\mathcal D_{d}\chi}\gamma^{c}\gamma_{c}{}^{d}\chi\big)\\
&-2\big(\overline{\mathcal D_{d}\chi}\gamma^{c}\gamma^{d}{}_{c}\chi\big)\\
&=-16\big(\bar\chi\gamma^{c}\mathcal D_{c}\chi\big)
\end{aligned}\tag{G693}
```

**G694: V7, vector coefficient.**

```math
\begin{aligned}
&2\big(\overline{\mathcal D_{d}\chi}\gamma^{c}\gamma^{a}\gamma_{c}{}^{d}\chi\big)\\
&-2\big(\overline{\mathcal D_{d}\chi}\gamma^{c}\gamma^{a}\gamma^{d}{}_{c}\chi\big)\\
&=8\big(\bar\chi\gamma^{ca}\mathcal D_{c}\chi\big)\\
&+16\big(\bar\chi\mathcal D^{a}\chi\big)
\end{aligned}\tag{G694}
```

**G695: V7, bivector coefficient.**

```math
\begin{aligned}
&-\big(\overline{\mathcal D_{d}\chi}\gamma^{c}\gamma^{[ab]}\gamma_{c}{}^{d}\chi\big)\\
&+\big(\overline{\mathcal D_{d}\chi}\gamma^{c}\gamma^{[ab]}\gamma^{d}{}_{c}\chi\big)\\
&=8\big(\bar\chi\gamma^{[a}\mathcal D^{b]}\chi\big)
\end{aligned}\tag{G695}
```

**G696: V8, scalar coefficient.**

```math
\begin{aligned}
&\frac{i}{2}\big(\overline{\widehat R(Q)_{ef}}\gamma^{cd}\gamma^{ef}\chi\big)\,T_{cd}\\
&=-4i\big(\overline{\widehat R(Q)_{cd}}\chi\big)\,T^{cd}
\end{aligned}\tag{G696}
```

**G697: V8, vector coefficient.**

```math
\begin{aligned}
&\frac{i}{2}\big(\overline{\widehat R(Q)_{ef}}\gamma^{cd}\gamma^{a}\gamma^{ef}\chi\big)\,T_{cd}\\
&=-8i\big(\overline{\widehat R(Q)^{a}{}_{c}}\gamma^{d}\chi\big)\,T^{c}{}_{d}\\
&-4i\big(\overline{\widehat R(Q)_{cd}}\gamma^{a}\chi\big)\,T^{cd}
\end{aligned}\tag{G697}
```

**G698: V8, bivector coefficient.**

```math
\begin{aligned}
&-\frac{i}{4}\big(\overline{\widehat R(Q)_{ef}}\gamma^{cd}\gamma^{[ab]}\gamma^{ef}\chi\big)\,T_{cd}\\
&=\frac{3i}{2}\big(\overline{\widehat R(Q)^{[ab]}}\gamma^{cd}\chi\big)\,T_{cd}\\
&-6i\big(\overline{\widehat R(Q)^{[a}{}_{|c|}}\gamma^{b]d}\chi\big)\,T^{c}{}_{d}\\
&+\frac{3i}{2}\big(\overline{\widehat R(Q)_{cd}}\gamma^{[ab]}\chi\big)\,T^{cd}\\
&+8i\big(\overline{\widehat R(Q)^{[a}{}_{|c|}}\chi\big)\,T^{|c|b]}
\end{aligned}\tag{G698}
```

**G699: V9, scalar coefficient.**

```math
\begin{aligned}
&-2i\big(\bar\chi\gamma^{e}\gamma^{cd}\gamma^{f}\gamma_{ef}\chi\big)\,T_{cd}\\
&+2i\big(\bar\chi\gamma^{e}\gamma^{cd}\gamma^{f}\gamma_{fe}\chi\big)\,T_{cd}\\
&=16i\big(\bar\chi\gamma^{cd}\chi\big)\,T_{cd}
\end{aligned}\tag{G699}
```

**G700: V9, vector coefficient.**

```math
\begin{aligned}
&-2i\big(\bar\chi\gamma^{e}\gamma^{cd}\gamma^{f}\gamma^{a}\gamma_{ef}\chi\big)\,T_{cd}\\
&+2i\big(\bar\chi\gamma^{e}\gamma^{cd}\gamma^{f}\gamma^{a}\gamma_{fe}\chi\big)\,T_{cd}\\
&=-16i\big(\bar\chi\gamma^{acd}\chi\big)\,T_{cd}\\
&=-8\big(\bar\chi\gamma^{cd}\chi\big)\,\varepsilon_{cd}{}^{a}{}_{ef}\,T^{ef}
\end{aligned}\tag{G700}
```

**G701: V9, bivector coefficient.**

```math
\begin{aligned}
&i\big(\bar\chi\gamma^{e}\gamma^{cd}\gamma^{f}\gamma^{[ab]}\gamma_{ef}\chi\big)\,T_{cd}\\
&-i\big(\bar\chi\gamma^{e}\gamma^{cd}\gamma^{f}\gamma^{[ab]}\gamma_{fe}\chi\big)\,T_{cd}\\
&=0
\end{aligned}\tag{G701}
```

**G702: chi2, whole coefficient matrix.**

```math
\begin{aligned}
&\frac{1}{48}\widehat R(V)_{cd}{}^{rs}\,\widehat R(V)_{ef}{}_{rs}\,\gamma^{cd}\gamma^{ef}\\
&=\frac{1}{48}\widehat R(V)_{cd}{}^{rs}\,\widehat R(V)_{ef}{}_{rs}\,\gamma^{cdef}\\
&-\frac{1}{24}\widehat R(V)_{cd}{}^{rs}\,\widehat R(V)^{cd}{}_{rs}\\
&=\frac{i}{48}\varepsilon_{cdefg}\,\widehat R(V)^{de}{}^{rs}\,\widehat R(V)^{fg}{}_{rs}\,\gamma^{c}\\
&-\frac{1}{24}\widehat R(V)_{cd}{}^{rs}\,\widehat R(V)^{cd}{}_{rs}
\end{aligned}\tag{G702}
```

### 33.4 Add equal contractions and display the cancellations

The following addition is exact rational arithmetic. Each entry in the middle
column is the sum from the indicated original M08 block; the individual
summands and their signs are displayed in G101–G702 above. The physical
contraction in the first column multiplies the indicated scalar, vector or
bivector coefficient. Thus these are sums of ordinary terms, not newly
defined component arrays. The last column is their complete sum.

#### Contractions that remain

Scalar contractions:

| Physical contraction | Contributions by original block | Sum |
|---|---|---|
| $`\widehat C_{cdef}\,\widehat C^{cdef}`$ | 1: $`\frac{1}{16}`$ | $`\frac{1}{16}`$ |
| $`\widehat C_{cdef}\,T^{cd}\,T^{ef}`$ | 4: $`-20`$; 5: $`4`$; 9: $`- \frac{4}{3}`$ | $`-\frac{52}{3}`$ |
| $`\widehat C_{cdef}\,T^{ce}\,T^{df}`$ | 5: $`8`$ | $`8`$ |
| $`\widehat C_{cdef}\,\varepsilon^{cdef}{}_{g}\,(\mathcal D_{h}T^{gh})`$ | 1: $`- \frac{1}{12}`$ | $`-\frac{1}{12}`$ |
| $`\widehat C_{cdef}\,\varepsilon^{cde}{}_{gh}\,(\mathcal D^{f}T^{gh})`$ | 1: $`\frac{1}{6}`$ | $`\frac{1}{6}`$ |
| $`\widehat C_{cdef}\,\varepsilon^{cde}{}_{gh}\,(\mathcal D^{g}T^{fh})`$ | 1: $`- \frac{1}{3}`$ | $`-\frac{1}{3}`$ |
| $`\widehat C_{cdef}\,\varepsilon^{cef}{}_{gh}\,(\mathcal D^{d}T^{gh})`$ | 1: $`- \frac{1}{12}`$ | $`-\frac{1}{12}`$ |
| $`\widehat C_{cdef}\,\varepsilon^{cef}{}_{gh}\,(\mathcal D^{g}T^{dh})`$ | 1: $`- \frac{1}{6}`$ | $`-\frac{1}{6}`$ |
| $`D\,T_{cd}\,T^{cd}`$ | 3: $`\frac{64}{9}`$; 7: $`\frac{256}{9}`$; 8: $`\frac{64}{3}`$ | $`\frac{512}{9}`$ |
| $`D^2`$ | 3: $`\frac{32}{3}`$ | $`\frac{32}{3}`$ |
| $`T_{cd}\,T^{cd}\,T_{ef}\,T^{ef}`$ | 4: $`\frac{128}{3}`$; 5: $`- \frac{512}{3}`$; 7: $`\frac{512}{27}`$; 8: $`\frac{512}{9}`$ | $`-\frac{1408}{27}`$ |
| $`T_{cd}\,T^{c}{}_{e}\,T^{d}{}_{f}\,T^{ef}`$ | 4: $`\frac{512}{3}`$; 5: $`\frac{1024}{3}`$ | $`512`$ |
| $`\varepsilon_{cdefg}\,T^{cd}\,T^{ef}\,(\mathcal D_{h}T^{gh})`$ | 4: $`-32`$; 5: $`\frac{16}{3}`$; 6: $`\frac{16}{3}`$ | $`-\frac{64}{3}`$ |
| $`T_{cd}\,(\mathcal D_{e}\mathcal D^{c}T^{de})`$ | 4: $`\frac{64}{3}`$ | $`\frac{64}{3}`$ |
| $`(\mathcal D_{c}T_{de})\,(\mathcal D^{c}T^{de})`$ | 2: $`- \frac{16}{3}`$; 6: $`- \frac{16}{3}`$ | $`-\frac{32}{3}`$ |
| $`(\mathcal D_{c}T_{de})\,(\mathcal D^{d}T^{ce})`$ | 6: $`\frac{32}{3}`$ | $`\frac{32}{3}`$ |
| $`\widehat R(V)_{cd}{}^{rs}\,\widehat R(V)^{cd}{}_{rs}`$ | 10: $`- \frac{1}{8}`$; 11: $`- \frac{1}{24}`$ | $`-\frac{1}{6}`$ |
| $`\big(\overline{\widehat R(Q)_{ec}}\widehat R(Q)^{e}{}_{d}\big)\,T^{cd}`$ | 1: $`\frac{35 i}{16}`$; 2: $`- \frac{5 i}{8}`$; 4: $`\frac{9 i}{2}`$; 5: $`- \frac{5 i}{4}`$; 10: $`\frac{9 i}{4}`$ | $`\frac{113i}{16}`$ |
| $`\big(\overline{\widehat R(Q)_{ef}}\gamma^{cd}\widehat R(Q)^{ef}\big)\,T_{cd}`$ | 1: $`- \frac{i}{2}`$; 2: $`- \frac{7 i}{32}`$; 5: $`- \frac{i}{4}`$; 9: $`- \frac{i}{32}`$; 10: $`- \frac{33 i}{64}`$ | $`-\frac{97i}{64}`$ |
| $`\big(\overline{\widehat R(Q)_{de}}\gamma^{c}\mathcal D_{c}\widehat R(Q)^{de}\big)`$ | 1: $`\frac{9}{64}`$; 4: $`\frac{3}{32}`$; 10: $`\frac{9}{64}`$ | $`\frac{3}{8}`$ |
| $`\big(\overline{\widehat R(Q)_{cd}}\chi\big)\,T^{cd}`$ | 2: $`- 9 i`$; 4: $`- 17 i`$; 5: $`4 i`$; 6: $`\frac{2 i}{3}`$; 7: $`- \frac{8 i}{3}`$; 8: $`- \frac{20 i}{3}`$; 9: $`- \frac{14 i}{3}`$; 11: $`- 2 i`$ | $`-\frac{112i}{3}`$ |
| $`\big(\bar\chi\gamma^{c}\mathcal D_{c}\chi\big)`$ | 3: $`- \frac{16}{3}`$; 6: $`- \frac{32}{3}`$; 8: $`- \frac{32}{3}`$; 11: $`-16`$ | $`-\frac{128}{3}`$ |

Vector contractions:

| Physical contraction | Contributions by original block | Sum |
|---|---|---|
| $`\widehat C_{cdef}\,\widehat C^{cd}{}_{gh}\,\varepsilon^{efgha}`$ | 1: $`- \frac{i}{32}`$ | $`-\frac{i}{32}`$ |
| $`\widehat C_{cdef}\,\varepsilon^{cea}{}_{gh}\,T^{df}\,T^{gh}`$ | 5: $`4 i`$ | $`4i`$ |
| $`\widehat C_{cdef}\,\varepsilon^{cea}{}_{gh}\,T^{dg}\,T^{fh}`$ | 5: $`8 i`$ | $`8i`$ |
| $`\widehat C_{cdef}\,\varepsilon^{cefa}{}_{g}\,T^{d}{}_{h}\,T^{gh}`$ | 5: $`- 4 i`$ | $`-4i`$ |
| $`\widehat C_{cdef}\,\varepsilon^{efa}{}_{gh}\,T^{cd}\,T^{gh}`$ | 4: $`- 6 i`$; 5: $`- 2 i`$; 9: $`\frac{2 i}{3}`$ | $`-\frac{22i}{3}`$ |
| $`\widehat C_{cdef}\,\varepsilon^{efa}{}_{gh}\,T^{cg}\,T^{dh}`$ | 5: $`4 i`$ | $`4i`$ |
| $`\widehat C^{a}{}_{cde}\,(\mathcal D^{c}T^{de})`$ | 1: $`- \frac{i}{3}`$ | $`-\frac{i}{3}`$ |
| $`\widehat C_{cd}{}^{a}{}_{e}\,(\mathcal D^{c}T^{de})`$ | 1: $`\frac{2 i}{3}`$; 2: $`2 i`$ | $`\frac{8i}{3}`$ |
| $`\widehat C_{cd}{}^{a}{}_{e}\,(\mathcal D^{e}T^{cd})`$ | 1: $`- \frac{i}{3}`$ | $`-\frac{i}{3}`$ |
| $`(\mathcal D_{c}\widehat C^{c}{}_{d}{}^{a}{}_{e})\,T^{de}`$ | 5: $`- 4 i`$ | $`-4i`$ |
| $`(\mathcal D_{c}\widehat C_{de}{}^{ca})\,T^{de}`$ | 4: $`4 i`$ | $`4i`$ |
| $`D\,(\mathcal D_{c}T^{ac})`$ | 3: $`\frac{16 i}{3}`$; 6: $`\frac{16 i}{3}`$ | $`\frac{32i}{3}`$ |
| $`(\mathcal D_{c}D)\,T^{ca}`$ | 8: $`- \frac{32 i}{3}`$ | $`-\frac{32i}{3}`$ |
| $`T^{a}{}_{c}\,T^{c}{}_{d}\,(\mathcal D_{e}T^{de})`$ | 5: $`- \frac{448 i}{9}`$; 8: $`- \frac{448 i}{9}`$; 9: $`\frac{128 i}{9}`$ | $`-\frac{256i}{3}`$ |
| $`T^{a}{}_{c}\,T_{de}\,(\mathcal D^{c}T^{de})`$ | 4: $`- \frac{512 i}{9}`$; 5: $`- \frac{256 i}{9}`$; 6: $`\frac{128 i}{3}`$; 8: $`\frac{128 i}{3}`$; 9: $`\frac{128 i}{9}`$ | $`\frac{128i}{9}`$ |
| $`T^{a}{}_{c}\,T_{de}\,(\mathcal D^{d}T^{ce})`$ | 4: $`\frac{2176 i}{9}`$; 5: $`- \frac{256 i}{9}`$; 6: $`- \frac{256 i}{3}`$; 8: $`- \frac{512 i}{9}`$; 9: $`\frac{128 i}{9}`$ | $`\frac{256i}{3}`$ |
| $`T_{cd}\,T^{cd}\,(\mathcal D_{e}T^{ae})`$ | 4: $`32 i`$; 5: $`- \frac{256 i}{9}`$; 6: $`\frac{32 i}{9}`$; 7: $`\frac{128 i}{9}`$; 8: $`- \frac{160 i}{9}`$; 9: $`\frac{32 i}{9}`$ | $`\frac{64i}{9}`$ |
| $`T_{cd}\,T^{c}{}_{e}\,(\mathcal D^{d}T^{ae})`$ | 4: $`128 i`$; 5: $`- \frac{128 i}{9}`$; 8: $`- \frac{128 i}{9}`$; 9: $`- \frac{128 i}{9}`$ | $`\frac{256i}{3}`$ |
| $`\varepsilon^{a}{}_{cdef}\,T^{cd}\,(\mathcal D^{e}\mathcal D_{g}T^{fg})`$ | 4: $`\frac{16 i}{3}`$; 5: $`\frac{16 i}{3}`$ | $`\frac{32i}{3}`$ |
| $`\varepsilon^{a}{}_{cdef}\,T^{cd}\,(\mathcal D_{g}\mathcal D^{e}T^{fg})`$ | 4: $`- \frac{32 i}{3}`$ | $`-\frac{32i}{3}`$ |
| $`\varepsilon^{a}{}_{cdef}\,T^{c}{}_{g}\,(\mathcal D^{d}\mathcal D^{e}T^{fg})`$ | 5: $`\frac{32 i}{3}`$ | $`\frac{32i}{3}`$ |
| $`\varepsilon^{a}{}_{cdef}\,T^{c}{}_{g}\,(\mathcal D^{d}\mathcal D^{g}T^{ef})`$ | 4: $`- \frac{32 i}{3}`$ | $`-\frac{32i}{3}`$ |
| $`\varepsilon^{a}{}_{cdef}\,(\mathcal D^{c}T^{d}{}_{g})\,(\mathcal D^{e}T^{fg})`$ | 2: $`\frac{16 i}{3}`$; 6: $`\frac{32 i}{3}`$ | $`16i`$ |
| $`\varepsilon^{a}{}_{cdef}\,(\mathcal D^{c}T^{d}{}_{g})\,(\mathcal D^{g}T^{ef})`$ | 6: $`\frac{32 i}{3}`$ | $`\frac{32i}{3}`$ |
| $`\varepsilon^{a}{}_{cdef}\,\widehat R(V)^{cd}{}^{rs}\,\widehat R(V)^{ef}{}_{rs}`$ | 10: $`\frac{i}{48}`$; 11: $`\frac{i}{48}`$ | $`\frac{i}{24}`$ |
| $`\big(\overline{\widehat R(Q)_{e}{}^{a}}\gamma^{c}\widehat R(Q)^{e}{}_{d}\big)\,T_{c}{}^{d}`$ | 1: $`- \frac{i}{2}`$; 2: $`\frac{5 i}{8}`$; 4: $`i`$; 5: $`- \frac{3 i}{4}`$; 10: $`- \frac{27 i}{8}`$ | $`-3i`$ |
| $`\big(\overline{\widehat R(Q)_{cd}}\mathcal D^{a}\widehat R(Q)^{cd}\big)`$ | 1: $`\frac{1}{64}`$; 4: $`\frac{3}{32}`$; 10: $`\frac{9}{64}`$ | $`\frac{1}{4}`$ |
| $`\big(\overline{\widehat R(Q)_{cd}}\mathcal D^{c}\widehat R(Q)^{da}\big)`$ | 1: $`\frac{5}{32}`$; 2: $`\frac{3}{32}`$ | $`\frac{1}{4}`$ |
| $`\big(\overline{\widehat R(Q)_{c}{}^{a}}\mathcal D_{d}\widehat R(Q)^{cd}\big)`$ | 1: $`- \frac{1}{32}`$; 5: $`- \frac{3}{16}`$; 10: $`- \frac{9}{32}`$ | $`-\frac{1}{2}`$ |
| $`\big(\overline{\widehat R(Q)_{de}}\gamma^{ca}\mathcal D_{c}\widehat R(Q)^{de}\big)`$ | 1: $`- \frac{1}{64}`$; 4: $`- \frac{3}{32}`$; 10: $`- \frac{9}{64}`$ | $`-\frac{1}{4}`$ |
| $`\big(\overline{\widehat R(Q)^{a}{}_{c}}\gamma^{d}\chi\big)\,T^{c}{}_{d}`$ | 2: $`6 i`$; 4: $`- 8 i`$; 5: $`- 4 i`$; 6: $`- 6 i`$; 8: $`\frac{20 i}{3}`$; 9: $`- \frac{8 i}{3}`$; 10: $`6 i`$; 11: $`- 14 i`$ | $`-16i`$ |
| $`\big(\overline{\widehat R(Q)_{c}{}^{a}}\mathcal D^{c}\chi\big)`$ | 2: $`- \frac{3}{2}`$; 8: $`-1`$; 10: $`- \frac{3}{2}`$ | $`-4`$ |
| $`\big(\bar\chi\mathcal D_{c}\widehat R(Q)^{ca}\big)`$ | 4: $`4`$; 5: $`-3`$; 6: $`\frac{3}{2}`$; 11: $`\frac{3}{2}`$ | $`4`$ |
| $`\big(\bar\chi\gamma^{ca}\mathcal D_{c}\chi\big)`$ | 3: $`\frac{16}{3}`$; 6: $`\frac{8}{3}`$; 8: $`\frac{16}{3}`$; 11: $`8`$ | $`\frac{64}{3}`$ |

Bivector contractions:

| Physical contraction | Contributions by original block | Sum |
|---|---|---|
| $`\widehat C^{[a}{}_{\vert cde\vert }\,T^{\vert c\vert b]}\,T^{de}`$ | 5: $`4`$ | $`4`$ |
| $`\widehat C^{[a}{}_{\vert cde\vert }\,T^{\vert cd\vert }\,T^{\vert e\vert b]}`$ | 5: $`-8`$ | $`-8`$ |
| $`\widehat C^{[a}{}_{\vert c\vert }{}^{b]}{}_{d}\,T^{c}{}_{e}\,T^{de}`$ | 5: $`8`$ | $`8`$ |
| $`\widehat C_{cd}{}^{[a}{}_{\vert e\vert }\,T^{\vert cd\vert }\,T^{\vert e\vert b]}`$ | 4: $`8`$; 5: $`-8`$; 9: $`- \frac{8}{3}`$ | $`-\frac{8}{3}`$ |
| $`\widehat C_{cdef}\,\varepsilon^{cd[ab]}{}_{g}\,(\mathcal D^{e}T^{fg})`$ | 1: $`\frac{1}{6}`$ | $`\frac{1}{6}`$ |
| $`\widehat C_{cdef}\,\varepsilon^{cd[ab]}{}_{g}\,(\mathcal D^{g}T^{ef})`$ | 1: $`\frac{1}{12}`$ | $`\frac{1}{12}`$ |
| $`\widehat C_{cdef}\,\varepsilon^{cde[ab]}\,(\mathcal D_{g}T^{fg})`$ | 1: $`\frac{1}{12}`$ | $`\frac{1}{12}`$ |
| $`\widehat C_{cdef}\,\varepsilon^{ce[ab]}{}_{g}\,(\mathcal D^{d}T^{fg})`$ | 1: $`\frac{1}{3}`$ | $`\frac{1}{3}`$ |
| $`\widehat C_{cdef}\,\varepsilon^{cef[ab]}\,(\mathcal D_{g}T^{dg})`$ | 1: $`- \frac{1}{12}`$ | $`-\frac{1}{12}`$ |
| $`\widehat C_{cdef}\,\varepsilon^{ef[ab]}{}_{g}\,(\mathcal D^{c}T^{dg})`$ | 1: $`\frac{1}{6}`$; 2: $`- \frac{1}{2}`$ | $`-\frac{1}{3}`$ |
| $`\widehat C_{cdef}\,\varepsilon^{ef[ab]}{}_{g}\,(\mathcal D^{g}T^{cd})`$ | 1: $`- \frac{1}{12}`$ | $`-\frac{1}{12}`$ |
| $`(\mathcal D_{c}\widehat C^{c}{}_{def})\,\varepsilon^{ef[ab]}{}_{g}\,T^{dg}`$ | 5: $`1`$ | $`1`$ |
| $`(\mathcal D_{c}\widehat C_{defg})\,\varepsilon^{cfg[ab]}\,T^{de}`$ | 4: $`1`$ | $`1`$ |
| $`T^{[a}{}_{\vert c\vert }\,(\mathcal D^{b]}\mathcal D_{d}T^{cd})`$ | 4: $`\frac{32}{3}`$ | $`\frac{32}{3}`$ |
| $`T^{[a}{}_{\vert c\vert }\,(\mathcal D^{\vert c\vert }\mathcal D_{\vert d\vert }T^{b]d})`$ | 4: $`- \frac{32}{3}`$; 5: $`\frac{16}{3}`$; 8: $`- \frac{16}{3}`$ | $`-\frac{32}{3}`$ |
| $`T^{[a}{}_{\vert c\vert }\,(\mathcal D_{\vert d\vert }\mathcal D^{b]}T^{cd})`$ | 5: $`- \frac{32}{3}`$ | $`-\frac{32}{3}`$ |
| $`T^{[a}{}_{\vert c\vert }\,(\mathcal D_{\vert d\vert }\mathcal D^{\vert c\vert }T^{b]d})`$ | 4: $`\frac{64}{3}`$; 5: $`- \frac{32}{3}`$ | $`\frac{32}{3}`$ |
| $`T_{cd}\,(\mathcal D^{[a}\mathcal D^{b]}T^{cd})`$ | 4: $`- \frac{32}{3}`$ | $`-\frac{32}{3}`$ |
| $`T_{cd}\,(\mathcal D^{[a}\mathcal D^{\vert c\vert }T^{b]d})`$ | 4: $`- \frac{64}{3}`$; 5: $`\frac{32}{3}`$ | $`-\frac{32}{3}`$ |
| $`T_{cd}\,(\mathcal D^{c}\mathcal D^{[a}T^{b]d})`$ | 8: $`\frac{32}{3}`$ | $`\frac{32}{3}`$ |
| $`T_{cd}\,(\mathcal D^{c}\mathcal D^{d}T^{[ab]})`$ | 4: $`\frac{32}{3}`$; 5: $`- \frac{16}{3}`$; 8: $`\frac{16}{3}`$ | $`\frac{32}{3}`$ |
| $`\big(\overline{\widehat R(Q)^{[ab]}}\widehat R(Q)_{cd}\big)\,T^{cd}`$ | 1: $`- \frac{7 i}{32}`$; 4: $`\frac{i}{4}`$; 5: $`\frac{7 i}{16}`$; 9: $`- \frac{i}{8}`$; 10: $`\frac{3 i}{2}`$ | $`\frac{59i}{32}`$ |
| $`\big(\overline{\widehat R(Q)_{de}}\gamma^{[a\vert c\vert }\widehat R(Q)^{\vert de\vert }\big)\,T_{\vert c\vert }{}^{b]}`$ | 1: $`- \frac{i}{4}`$; 2: $`\frac{3 i}{16}`$; 9: $`- \frac{i}{16}`$; 10: $`\frac{33 i}{32}`$ | $`\frac{29i}{32}`$ |
| $`\big(\overline{\widehat R(Q)_{d}{}^{[a}}\widehat R(Q)^{\vert d\vert }{}_{\vert c\vert }\big)\,T^{\vert c\vert b]}`$ | 1: $`\frac{5 i}{8}`$; 2: $`- \frac{5 i}{8}`$; 4: $`- i`$; 5: $`- \frac{5 i}{4}`$; 10: $`- \frac{27 i}{8}`$ | $`-\frac{45i}{8}`$ |
| $`\big(\overline{\widehat R(Q)_{e}{}^{[a}}\gamma^{b]c}\widehat R(Q)^{e}{}_{d}\big)\,T_{c}{}^{d}`$ | 1: $`- \frac{15 i}{16}`$; 2: $`\frac{i}{8}`$; 4: $`- i`$; 5: $`\frac{i}{8}`$; 10: $`\frac{27 i}{8}`$ | $`\frac{27i}{16}`$ |
| $`\big(\overline{\widehat R(Q)^{[ab]}}\gamma^{cd}\chi\big)\,T_{cd}`$ | 1: $`- \frac{5 i}{8}`$; 2: $`- \frac{3 i}{2}`$; 6: $`- 3 i`$; 8: $`i`$; 9: $`- \frac{i}{2}`$; 10: $`\frac{9 i}{4}`$; 11: $`\frac{33 i}{4}`$ | $`\frac{47i}{8}`$ |
| $`\big(\overline{\widehat R(Q)^{[a}{}_{\vert c\vert }}\chi\big)\,T^{\vert c\vert b]}`$ | 2: $`2 i`$; 4: $`8 i`$; 5: $`4 i`$; 6: $`\frac{22 i}{3}`$; 8: $`- 4 i`$; 9: $`- \frac{8 i}{3}`$; 10: $`- 6 i`$; 11: $`2 i`$ | $`\frac{32i}{3}`$ |
| $`\big(\overline{\widehat R(Q)^{[a}{}_{\vert c\vert }}\gamma^{b]d}\chi\big)\,T^{c}{}_{d}`$ | 1: $`\frac{5 i}{2}`$; 2: $`4 i`$; 4: $`- 8 i`$; 5: $`- 4 i`$; 6: $`\frac{26 i}{3}`$; 8: $`- \frac{8 i}{3}`$; 9: $`2 i`$; 10: $`- 3 i`$; 11: $`- 39 i`$ | $`-\frac{79i}{2}`$ |
| $`\big(\overline{\widehat R(Q)_{cd}}\gamma^{[ab]}\chi\big)\,T^{cd}`$ | 1: $`- \frac{5 i}{8}`$; 2: $`- i`$; 4: $`\frac{3 i}{2}`$; 5: $`2 i`$; 6: $`- \frac{5 i}{3}`$; 7: $`\frac{4 i}{3}`$; 8: $`\frac{i}{3}`$; 9: $`- \frac{i}{6}`$; 10: $`- \frac{3 i}{4}`$; 11: $`\frac{41 i}{4}`$ | $`\frac{269i}{24}`$ |

#### Contractions whose coefficients cancel

Scalar contractions:

| Physical contraction | Contributions by original block | Sum |
|---|---|---|
| $`T_{cd}\,(\mathcal D^{c}\mathcal D_{e}T^{de})`$ | 4: $`- \frac{32}{3}`$; 5: $`\frac{16}{3}`$; 8: $`\frac{16}{3}`$ | $`0`$ |
| $`T_{cd}\,(\mathcal D_{e}\mathcal D^{e}T^{cd})`$ | 4: $`- \frac{32}{3}`$; 5: $`\frac{32}{3}`$ | $`0`$ |
| $`(\mathcal D_{c}T^{c}{}_{d})\,(\mathcal D_{e}T^{de})`$ | 2: $`- \frac{8}{3}`$; 6: $`\frac{8}{3}`$ | $`0`$ |
| $`\big(\bar\chi\gamma^{cd}\chi\big)\,T_{cd}`$ | 3: $`\frac{80 i}{9}`$; 6: $`48 i`$; 7: $`- \frac{128 i}{9}`$; 8: $`- \frac{176 i}{3}`$; 11: $`16 i`$ | $`0`$ |

Vector contractions:

| Physical contraction | Contributions by original block | Sum |
|---|---|---|
| $`D\,\varepsilon^{a}{}_{cdef}\,T^{cd}\,T^{ef}`$ | 3: $`- \frac{32 i}{3}`$; 8: $`\frac{32 i}{3}`$ | $`0`$ |
| $`\varepsilon^{a}{}_{cdef}\,T^{cd}\,T^{ef}\,T_{gh}\,T^{gh}`$ | 4: $`\frac{128 i}{3}`$; 5: $`- \frac{128 i}{3}`$; 7: $`- \frac{256 i}{9}`$; 8: $`\frac{256 i}{9}`$ | $`0`$ |
| $`\varepsilon^{a}{}_{cdef}\,T^{cd}\,(\mathcal D_{g}\mathcal D^{g}T^{ef})`$ | 4: $`- \frac{16 i}{3}`$; 5: $`\frac{16 i}{3}`$ | $`0`$ |
| $`\varepsilon^{a}{}_{cdef}\,T^{c}{}_{g}\,(\mathcal D^{g}\mathcal D^{d}T^{ef})`$ | 4: $`\frac{32 i}{3}`$; 5: $`- \frac{16 i}{3}`$; 8: $`- \frac{16 i}{3}`$ | $`0`$ |
| $`\varepsilon^{a}{}_{cdef}\,(\mathcal D^{c}T^{de})\,(\mathcal D_{g}T^{fg})`$ | 2: $`- \frac{16 i}{3}`$; 6: $`\frac{16 i}{3}`$ | $`0`$ |
| $`\varepsilon^{a}{}_{cdef}\,(\mathcal D_{g}T^{cd})\,(\mathcal D^{g}T^{ef})`$ | 2: $`- \frac{8 i}{3}`$; 6: $`\frac{8 i}{3}`$ | $`0`$ |
| $`\big(\overline{\widehat R(Q)_{ec}}\gamma^{a}\widehat R(Q)^{e}{}_{d}\big)\,T^{cd}`$ | 1: $`\frac{i}{8}`$; 2: $`\frac{3 i}{8}`$; 4: $`- \frac{7 i}{2}`$; 5: $`\frac{3 i}{4}`$; 10: $`\frac{9 i}{4}`$ | $`0`$ |
| $`\big(\overline{\widehat R(Q)_{gh}}\gamma^{cd}\widehat R(Q)^{gh}\big)\,\varepsilon_{cd}{}^{a}{}_{ef}\,T^{ef}`$ | 1: $`\frac{5}{128}`$; 2: $`\frac{7}{64}`$; 5: $`\frac{1}{8}`$; 9: $`- \frac{1}{64}`$; 10: $`- \frac{33}{128}`$ | $`0`$ |
| $`\big(\overline{\widehat R(Q)_{cd}}\gamma^{a}\chi\big)\,T^{cd}`$ | 2: $`7 i`$; 4: $`7 i`$; 5: $`- 4 i`$; 6: $`- \frac{10 i}{3}`$; 7: $`- \frac{8 i}{3}`$; 8: $`4 i`$; 9: $`- 2 i`$; 11: $`- 6 i`$ | $`0`$ |
| $`\big(\bar\chi\gamma^{cd}\chi\big)\,\varepsilon_{cd}{}^{a}{}_{ef}\,T^{ef}`$ | 3: $`\frac{40}{9}`$; 6: $`- \frac{40}{3}`$; 7: $`- \frac{64}{9}`$; 8: $`24`$; 11: $`-8`$ | $`0`$ |
| $`\big(\bar\chi\mathcal D^{a}\chi\big)`$ | 3: $`- \frac{16}{3}`$; 6: $`- \frac{64}{3}`$; 8: $`\frac{32}{3}`$; 11: $`16`$ | $`0`$ |

Bivector contractions:

| Physical contraction | Contributions by original block | Sum |
|---|---|---|
| $`D\,\varepsilon^{[ab]}{}_{cde}\,(\mathcal D^{c}T^{de})`$ | 3: $`\frac{8}{3}`$; 6: $`- \frac{8}{3}`$ | $`0`$ |
| $`\varepsilon^{[ab]}{}_{cde}\,T^{cd}\,T^{e}{}_{f}\,(\mathcal D_{g}T^{fg})`$ | 4: $`- \frac{32}{3}`$; 5: $`- \frac{16}{3}`$; 6: $`\frac{32}{3}`$; 8: $`\frac{16}{3}`$ | $`0`$ |
| $`\varepsilon^{[ab]}{}_{cde}\,T^{cd}\,T_{fg}\,(\mathcal D^{e}T^{fg})`$ | 5: $`\frac{32}{3}`$; 6: $`- \frac{32}{3}`$ | $`0`$ |
| $`\varepsilon^{[ab]}{}_{cde}\,T^{cd}\,T_{fg}\,(\mathcal D^{f}T^{eg})`$ | 4: $`- \frac{64}{9}`$; 5: $`- \frac{32}{9}`$; 6: $`\frac{64}{3}`$; 8: $`- \frac{160}{9}`$; 9: $`\frac{64}{9}`$ | $`0`$ |
| $`\varepsilon^{[ab]}{}_{cde}\,T^{c}{}_{f}\,T^{d}{}_{g}\,(\mathcal D^{e}T^{fg})`$ | 5: $`- \frac{64}{3}`$; 6: $`\frac{64}{3}`$ | $`0`$ |
| $`\varepsilon^{[ab]}{}_{cde}\,T^{c}{}_{f}\,T^{d}{}_{g}\,(\mathcal D^{f}T^{eg})`$ | 4: $`\frac{320}{9}`$; 5: $`\frac{64}{9}`$; 6: $`- \frac{128}{3}`$; 8: $`- \frac{64}{9}`$; 9: $`\frac{64}{9}`$ | $`0`$ |
| $`\varepsilon^{[ab]}{}_{cde}\,T^{c}{}_{f}\,T^{f}{}_{g}\,(\mathcal D^{d}T^{eg})`$ | 4: $`- \frac{64}{3}`$; 5: $`\frac{320}{9}`$; 8: $`- \frac{64}{9}`$; 9: $`- \frac{64}{9}`$ | $`0`$ |
| $`\varepsilon^{[ab]}{}_{cde}\,T^{c}{}_{f}\,T^{f}{}_{g}\,(\mathcal D^{g}T^{de})`$ | 5: $`- \frac{64}{9}`$; 8: $`\frac{128}{9}`$; 9: $`- \frac{64}{9}`$ | $`0`$ |
| $`\varepsilon^{[ab]}{}_{cde}\,T_{fg}\,T^{fg}\,(\mathcal D^{c}T^{de})`$ | 4: $`- \frac{16}{3}`$; 5: $`\frac{32}{9}`$; 6: $`- \frac{16}{9}`$; 7: $`\frac{64}{9}`$; 8: $`- \frac{16}{9}`$; 9: $`- \frac{16}{9}`$ | $`0`$ |
| $`T^{[ab]}\,(\mathcal D_{c}\mathcal D_{d}T^{cd})`$ | 4: $`\frac{16}{3}`$; 5: $`- \frac{16}{3}`$ | $`0`$ |
| $`T^{[a}{}_{\vert c\vert }\,(\mathcal D_{\vert d\vert }\mathcal D^{\vert d\vert }T^{b]c})`$ | 5: $`(\frac{32}{3}) + (- \frac{32}{3})=0`$ | $`0`$ |
| $`(\mathcal D^{[a}T^{b]}{}_{c})\,(\mathcal D_{d}T^{cd})`$ | 2: $`(- \frac{16}{3}) + (\frac{16}{3})=0`$; 6: $`(\frac{16}{3}) + (- \frac{16}{3})=0`$ | $`0`$ |
| $`(\mathcal D^{[a}T_{\vert cd\vert })\,(\mathcal D^{\vert c\vert }T^{b]d})`$ | 2: $`(-8) + (\frac{8}{3}) + (\frac{16}{3})=0`$ | $`0`$ |
| $`(\mathcal D_{c}T^{[ab]})\,(\mathcal D_{d}T^{cd})`$ | 2: $`(-4) + (\frac{4}{3}) + (\frac{8}{3})=0`$; 6: $`(\frac{8}{3}) + (- \frac{8}{3})=0`$ | $`0`$ |
| $`\big(\overline{\widehat R(Q)_{cd}}\gamma^{[a}\mathcal D^{b]}\widehat R(Q)^{cd}\big)`$ | 1: $`- \frac{3}{64}`$; 4: $`- \frac{3}{32}`$; 10: $`\frac{9}{64}`$ | $`0`$ |
| $`\big(\overline{\widehat R(Q)_{cd}}\gamma^{[a}\mathcal D^{\vert c\vert }\widehat R(Q)^{\vert d\vert b]}\big)`$ | 1: $`\frac{3}{32}`$; 2: $`- \frac{3}{32}`$ | $`0`$ |
| $`\big(\overline{\widehat R(Q)_{c}{}^{[a}}\gamma^{b]}\mathcal D_{d}\widehat R(Q)^{cd}\big)`$ | 1: $`- \frac{3}{32}`$; 5: $`- \frac{3}{16}`$; 10: $`\frac{9}{32}`$ | $`0`$ |
| $`\big(\overline{\widehat R(Q)_{fg}}\gamma^{cd}\mathcal D_{e}\widehat R(Q)^{fg}\big)\,\varepsilon_{cd}{}^{e[ab]}`$ | 1: $`\frac{3 i}{256}`$; 4: $`\frac{3 i}{128}`$; 10: $`- \frac{9 i}{256}`$ | $`0`$ |
| $`\big(\overline{\widehat R(Q)_{c}{}^{[a}}\gamma^{b]}\mathcal D^{c}\chi\big)`$ | 2: $`- \frac{1}{2}`$; 8: $`-1`$; 10: $`\frac{3}{2}`$ | $`0`$ |
| $`\big(\bar\chi\gamma^{[a}\mathcal D_{\vert c\vert }\widehat R(Q)^{\vert c\vert b]}\big)`$ | 4: $`-4`$; 5: $`1`$; 6: $`- \frac{3}{2}`$; 11: $`\frac{9}{2}`$ | $`0`$ |
| $`\big(\bar\chi\gamma^{c}\mathcal D_{c}\widehat R(Q)^{[ab]}\big)`$ | 4: $`2`$; 6: $`1`$; 11: $`-3`$ | $`0`$ |
| $`\big(\bar\chi\gamma^{[a\vert c\vert }\chi\big)\,T_{\vert c\vert }{}^{b]}`$ | 3: $`- \frac{160 i}{9}`$; 7: $`\frac{256 i}{9}`$; 8: $`- \frac{32 i}{3}`$ | $`0`$ |
| $`\big(\bar\chi\gamma^{[a}\mathcal D^{b]}\chi\big)`$ | 3: $`- \frac{16}{3}`$; 6: $`\frac{8}{3}`$; 8: $`- \frac{16}{3}`$; 11: $`8`$ | $`0`$ |
| $`\big(\bar\chi\gamma^{cd}\mathcal D_{e}\chi\big)\,\varepsilon_{cd}{}^{e[ab]}`$ | 3: $`\frac{4 i}{3}`$; 6: $`- \frac{4 i}{3}`$ | $`0`$ |

## 34. Consistency Checks

The verification is limited to the algebraic collection performed here.
It does not certify the nonlinear multiplet law.

**Indices and gamma ranks.** Every summand in $`p`$ has no free Lorentz index;
every summand in $`t^a`$ has only $`a`$; every summand in $`k^{ab}`$ has only $`a,b`$
and is explicitly antisymmetrized. All other Lorentz indices occur twice.
The surviving gamma matrices, both outside and inside bilinears, have ranks
zero, one or two. There are no remaining ordered products of two gamma
matrices in the final coefficients. G07, rather than omission, removes
ranks three, four and five.

**Weights.** With the locked weights
$`w(T)=1`$, $`w(D)=w(\widehat C)=w(\widehat R(V))=2`$,
$`w(\chi)=w(\widehat R(Q))=3/2`$ and $`w(\mathcal D_a)=1`$,
every coefficient has weight four:

```math
\begin{gathered}
w(C^2)=w(D^2)=w(R(V)^2)=2+2=4,\quad
w(C\mathcal DT)=2+1+1=4,\\
w(T\mathcal D\mathcal DT)=1+1+1+1=4,\quad
w(T^2\mathcal DT)=2+1+1=4,\quad w(T^4)=4,\\
w(\bar R(Q)\mathcal DR(Q))=\tfrac32+1+\tfrac32=4,\quad
w(T\bar R(Q)R(Q))=w(T\bar R(Q)\chi)=1+\tfrac32+\tfrac32=4.
\end{gathered}\tag{G703}
```

The same computation gives $`w(\bar\chi\mathcal D\chi)=4`$.
Adding $`w(\epsilon)=-1/2`$ gives $`w(\delta\varphi_W)=7/2`$.
The coefficient checker tests this separately for every final term, including
$`D^2`$: this is a square of the auxiliary scalar, not a single $`D`$.

**Parity and conjugation.** Every displayed coefficient is Grassmann even:
it is bosonic or contains an even spinor bilinear. G02 tracks every exchange;
its vanishing identical-spinor scalar/vector bilinears are removed only
after the contracted SU(2) sign is included. The matrix test uses the linear
Majorana bar and two independent odd generators, so the bilinear coefficient
is $`\bar u_1\Gamma v_2-\bar u_2\Gamma v_1`$. Replacing the fermions by
commuting spinors would not test the signs used here. The algebra preserves
the input symplectic-Majorana real structure; this is not a separate proof
that the adopted input obeys its full nonlinear transformation law.

**Clifford and component checks.** The accompanying
[component check commands and output scope](../README.md)
records the actual run of
[verify_weyl_clifford_collection.py](../src/reference_checks/verify_weyl_clifford_collection.py).
It compares all $`32\times32`$ antisymmetric gamma-basis products with explicit
$`4\times4`$ matrices, checks the three Schouten contractions, and evaluates
both the unreduced Section-28 expression and the final result on independent
Lorentzian tensor/spinor components. The curvature samples obey pair
antisymmetry and conventional trace constraints; the spinor two-forms and
their derivative jets obey the gamma-trace constraint. Covariant derivative
jets remain ordered and otherwise independent. This is an algebra test,
not a claim that arbitrary independently chosen jets solve field equations.

**Simple restrictions.** Setting every field and jet to zero gives zero.
Keeping only $`D`$ gives $`p=32D^2/3`$, $`t^a=k^{ab}=0`$, directly matching
$`(128\chi^iD/3)`$ varied with $`\delta\chi^i=D\epsilon^i/4`$.
Keeping only $`\widehat C`$ gives G21. Keeping only $`\widehat R(V)`$ gives

```math
p=-\tfrac16\widehat R(V)_{cd}{}^{rs}\widehat R(V)^{cd}{}_{rs},
\quad t^a=\tfrac{i}{24}\varepsilon^a{}_{cdef}
 \widehat R(V)^{cd\,rs}\widehat R(V)^{ef}{}_{rs},
\quad k^{ab}=0.
\tag{G704}
```

For the latter check insert G04 into the three explicit R(V)-square terms
in H181: the two rank-four products minus the single rank-four gamma give
one rank-four term, while their scalar contractions give $`-4R(V)^2/24`$.
The rank-two contractions vanish because the two equal field strengths
produce a symmetric tensor. With only a constant $`T`$, G20 cancels $`t^a`$
and the result is

```math
p=512T_{cd}T^c{}_eT^d{}_fT^{ef}
 -\tfrac{1408}{27}(T_{cd}T^{cd})^2,
\qquad t^a=k^{ab}=0.
\tag{G705}
```

These are algebraic restrictions of the coefficient polynomial, not claimed
supergravity vacua. Their numerical comparisons with Section 28 are included
in the checker. The displayed pure $`D^2`$, $`C^2`$, $`R(V)^2`$ and $`T^4`$ scalar
coefficients agree with one half of the corresponding printed bosonic $`N`$
terms in master M04. That limited comparison is not a complete identification
of $`p`$ with $`N_W/2`$.

**Local equality and covariance.** Derivative order, all hatted definitions,
and the Section-27 restoration of full covariants are retained. No boundary
condition is used, no total derivative is dropped, and no EOM is imposed.
For example $`T_{cd}\mathcal D^c\mathcal D^aT^{bd}`$ is not combined with
$`T_{cd}\mathcal D^a\mathcal D^cT^{bd}`$ by pretending the derivatives commute.

## 35. Final Result

All coefficients below are added across the eleven original terms. They use
only the original physical fields. The complete result is

```math
\boxed{\left.\delta_Q\varphi_W^i\right|_{\epsilon^i}
 =\big[p+\gamma_a t^a+\gamma_{ab}k^{ab}\big]\epsilon^i.}
\tag{G706}
```

### Scalar coefficient

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
\end{aligned}\tag{G707}
```

### Vector coefficient

```math
\begin{aligned}
t^a={}&-\frac{i}{32}\widehat C_{cdef}\,\widehat C^{cd}{}_{gh}\,\varepsilon^{efgha}\\
&+4i\widehat C_{cdef}\,\varepsilon^{cea}{}_{gh}\,T^{df}\,T^{gh}\\
&+8i\widehat C_{cdef}\,\varepsilon^{cea}{}_{gh}\,T^{dg}\,T^{fh}\\
&-4i\widehat C_{cdef}\,\varepsilon^{cefa}{}_{g}\,T^{d}{}_{h}\,T^{gh}\\
&-\frac{22i}{3}\widehat C_{cdef}\,\varepsilon^{efa}{}_{gh}\,T^{cd}\,T^{gh}\\
&+4i\widehat C_{cdef}\,\varepsilon^{efa}{}_{gh}\,T^{cg}\,T^{dh}\\
&-\frac{i}{3}\widehat C^{a}{}_{cde}\,(\mathcal D^{c}T^{de})\\
&+\frac{8i}{3}\widehat C_{cd}{}^{a}{}_{e}\,(\mathcal D^{c}T^{de})\\
&-\frac{i}{3}\widehat C_{cd}{}^{a}{}_{e}\,(\mathcal D^{e}T^{cd})\\
&-4i(\mathcal D_{c}\widehat C^{c}{}_{d}{}^{a}{}_{e})\,T^{de}\\
&+4i(\mathcal D_{c}\widehat C_{de}{}^{ca})\,T^{de}\\
&+\frac{32i}{3}D\,(\mathcal D_{c}T^{ac})\\
&-\frac{32i}{3}(\mathcal D_{c}D)\,T^{ca}\\
&-\frac{256i}{3}T^{a}{}_{c}\,T^{c}{}_{d}\,(\mathcal D_{e}T^{de})\\
&+\frac{128i}{9}T^{a}{}_{c}\,T_{de}\,(\mathcal D^{c}T^{de})\\
&+\frac{256i}{3}T^{a}{}_{c}\,T_{de}\,(\mathcal D^{d}T^{ce})\\
&+\frac{64i}{9}T_{cd}\,T^{cd}\,(\mathcal D_{e}T^{ae})\\
&+\frac{256i}{3}T_{cd}\,T^{c}{}_{e}\,(\mathcal D^{d}T^{ae})\\
&+\frac{32i}{3}\varepsilon^{a}{}_{cdef}\,T^{cd}\,(\mathcal D^{e}\mathcal D_{g}T^{fg})\\
&-\frac{32i}{3}\varepsilon^{a}{}_{cdef}\,T^{cd}\,(\mathcal D_{g}\mathcal D^{e}T^{fg})\\
&+\frac{32i}{3}\varepsilon^{a}{}_{cdef}\,T^{c}{}_{g}\,(\mathcal D^{d}\mathcal D^{e}T^{fg})\\
&-\frac{32i}{3}\varepsilon^{a}{}_{cdef}\,T^{c}{}_{g}\,(\mathcal D^{d}\mathcal D^{g}T^{ef})\\
&+16i\varepsilon^{a}{}_{cdef}\,(\mathcal D^{c}T^{d}{}_{g})\,(\mathcal D^{e}T^{fg})\\
&+\frac{32i}{3}\varepsilon^{a}{}_{cdef}\,(\mathcal D^{c}T^{d}{}_{g})\,(\mathcal D^{g}T^{ef})\\
&+\frac{i}{24}\varepsilon^{a}{}_{cdef}\,\widehat R(V)^{cd}{}^{rs}\,\widehat R(V)^{ef}{}_{rs}\\
&-3i\big(\overline{\widehat R(Q)_{e}{}^{a}}\gamma^{c}\widehat R(Q)^{e}{}_{d}\big)\,T_{c}{}^{d}\\
&+\frac{1}{4}\big(\overline{\widehat R(Q)_{cd}}\mathcal D^{a}\widehat R(Q)^{cd}\big)\\
&+\frac{1}{4}\big(\overline{\widehat R(Q)_{cd}}\mathcal D^{c}\widehat R(Q)^{da}\big)\\
&-\frac{1}{2}\big(\overline{\widehat R(Q)_{c}{}^{a}}\mathcal D_{d}\widehat R(Q)^{cd}\big)\\
&-\frac{1}{4}\big(\overline{\widehat R(Q)_{de}}\gamma^{ca}\mathcal D_{c}\widehat R(Q)^{de}\big)\\
&-16i\big(\overline{\widehat R(Q)^{a}{}_{c}}\gamma^{d}\chi\big)\,T^{c}{}_{d}\\
&-4\big(\overline{\widehat R(Q)_{c}{}^{a}}\mathcal D^{c}\chi\big)\\
&+4\big(\bar\chi\mathcal D_{c}\widehat R(Q)^{ca}\big)\\
&+\frac{64}{3}\big(\bar\chi\gamma^{ca}\mathcal D_{c}\chi\big)
\end{aligned}\tag{G708}
```

### Bivector coefficient

```math
\begin{aligned}
k^{ab}={}&4\widehat C^{[a}{}_{|cde|}\,T^{|c|b]}\,T^{de}\\
&-8\widehat C^{[a}{}_{|cde|}\,T^{|cd|}\,T^{|e|b]}\\
&+8\widehat C^{[a}{}_{|c|}{}^{b]}{}_{d}\,T^{c}{}_{e}\,T^{de}\\
&-\frac{8}{3}\widehat C_{cd}{}^{[a}{}_{|e|}\,T^{|cd|}\,T^{|e|b]}\\
&+\frac{1}{6}\widehat C_{cdef}\,\varepsilon^{cd[ab]}{}_{g}\,(\mathcal D^{e}T^{fg})\\
&+\frac{1}{12}\widehat C_{cdef}\,\varepsilon^{cd[ab]}{}_{g}\,(\mathcal D^{g}T^{ef})\\
&+\frac{1}{12}\widehat C_{cdef}\,\varepsilon^{cde[ab]}\,(\mathcal D_{g}T^{fg})\\
&+\frac{1}{3}\widehat C_{cdef}\,\varepsilon^{ce[ab]}{}_{g}\,(\mathcal D^{d}T^{fg})\\
&-\frac{1}{12}\widehat C_{cdef}\,\varepsilon^{cef[ab]}\,(\mathcal D_{g}T^{dg})\\
&-\frac{1}{3}\widehat C_{cdef}\,\varepsilon^{ef[ab]}{}_{g}\,(\mathcal D^{c}T^{dg})\\
&-\frac{1}{12}\widehat C_{cdef}\,\varepsilon^{ef[ab]}{}_{g}\,(\mathcal D^{g}T^{cd})\\
&+(\mathcal D_{c}\widehat C^{c}{}_{def})\,\varepsilon^{ef[ab]}{}_{g}\,T^{dg}\\
&+(\mathcal D_{c}\widehat C_{defg})\,\varepsilon^{cfg[ab]}\,T^{de}\\
&+\frac{32}{3}T^{[a}{}_{|c|}\,(\mathcal D^{b]}\mathcal D_{d}T^{cd})\\
&-\frac{32}{3}T^{[a}{}_{|c|}\,(\mathcal D^{|c|}\mathcal D_{|d|}T^{b]d})\\
&-\frac{32}{3}T^{[a}{}_{|c|}\,(\mathcal D_{|d|}\mathcal D^{b]}T^{cd})\\
&+\frac{32}{3}T^{[a}{}_{|c|}\,(\mathcal D_{|d|}\mathcal D^{|c|}T^{b]d})\\
&-\frac{32}{3}T_{cd}\,(\mathcal D^{[a}\mathcal D^{b]}T^{cd})\\
&-\frac{32}{3}T_{cd}\,(\mathcal D^{[a}\mathcal D^{|c|}T^{b]d})\\
&+\frac{32}{3}T_{cd}\,(\mathcal D^{c}\mathcal D^{[a}T^{b]d})\\
&+\frac{32}{3}T_{cd}\,(\mathcal D^{c}\mathcal D^{d}T^{[ab]})\\
&+\frac{59i}{32}\big(\overline{\widehat R(Q)^{[ab]}}\widehat R(Q)_{cd}\big)\,T^{cd}\\
&+\frac{29i}{32}\big(\overline{\widehat R(Q)_{de}}\gamma^{[a|c|}\widehat R(Q)^{|de|}\big)\,T_{|c|}{}^{b]}\\
&-\frac{45i}{8}\big(\overline{\widehat R(Q)_{d}{}^{[a}}\widehat R(Q)^{|d|}{}_{|c|}\big)\,T^{|c|b]}\\
&+\frac{27i}{16}\big(\overline{\widehat R(Q)_{e}{}^{[a}}\gamma^{b]c}\widehat R(Q)^{e}{}_{d}\big)\,T_{c}{}^{d}\\
&+\frac{47i}{8}\big(\overline{\widehat R(Q)^{[ab]}}\gamma^{cd}\chi\big)\,T_{cd}\\
&+\frac{32i}{3}\big(\overline{\widehat R(Q)^{[a}{}_{|c|}}\chi\big)\,T^{|c|b]}\\
&-\frac{79i}{2}\big(\overline{\widehat R(Q)^{[a}{}_{|c|}}\gamma^{b]d}\chi\big)\,T^{c}{}_{d}\\
&+\frac{269i}{24}\big(\overline{\widehat R(Q)_{cd}}\gamma^{[ab]}\chi\big)\,T^{cd}
\end{aligned}\tag{G709}
```

The sums have **22 scalar, 34 vector and 29 bivector contractions** in this
displayed tensor basis. Square brackets make the last coefficient explicitly
antisymmetric; they introduce no extra overall $`1/2`$ in G706.
This is a complete reduction in **Clifford rank**. It is not a claim that all
Lorentz-tensor contractions are independent after every possible curvature
Bianchi identity or covariant-derivative commutator.

## 36. Convention Dependence and Remaining Uncertainties

The result is conditional on the adopted M08 and master lock v5, exactly
as the Section-28 input is. No operational convention or source coefficient
has changed in this part. The provenance and source-discrepancy records
remain in the master file.

The singlet bivector has been calculated and retained. Its vanishing cannot
be assumed from the target linear-multiplet law. Establishing such a
cancellation requires the relevant full curvature identities and ordered
supercovariant-derivative commutators, including their fermionic terms.
Likewise $`p`$ and $`t^a`$ are the collected coefficients at this stage;
identifying the complete $`N_W,E_{Wa}`$ must include the other terms in the
linear-multiplet transformation and the SU(2)-traceless sector.
The spinor S-law, complete Q/S matching and divergence constraint remain
separate calculations. No full invariant or spectrum is claimed here.

No fermion order is discarded: implicit fermions in hats and full derivatives
remain present. Expanding all those covariants into independent gauge fields
would be a different representation of the same input, not a truncation
permitted in this collection.

# Part VI — Proof of singlet bivector cancellation

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

# Part VII — Canonical scalar coefficient

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
of the map, with the user-adopted M08 coefficient $`8/3`$.

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
the spinor S-law. Those independent transformation checks are outside
this canonicalization. The [component density](full-fermionic-weyl2-action.md)
and [AdS5 spectrum](../../../weyl2/ads5/README.md) are derived separately.
