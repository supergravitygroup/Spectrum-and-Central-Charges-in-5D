

The equations and reported residuals below belong to the cited construction. Finite component tests and formal symbolic identities retain their distinct scopes; the former do not establish an unrestricted symbolic identity.

# Curved LOG multiplet certification

## Problem and Target

Certify the actual stored calculated primary and descendants in general curved superspace through the retained fermion order. The earlier finite-jet tests are supporting evidence, not the endpoint. The targets are S/K primarity, linearity, descendant identities, and constrained-vector conservation. This investigation has **confirmed a new source-algebra defect** and derived its repair; the complete actual primary now passes the curved constraints at **all** its explicit fermion orders. The current-conservation implication is derived below. Defining-projector equality and component-chain equality retain their separate certificates.

## Convention Ledger

Use the branch source lock, Gold $`\Gamma=i\gamma`$, $`\Sigma=\gamma^{ab}/2`$, the locked antisymmetric spinor and SU(2) metrics, graded left differentiation, and unit-weight symmetrization. Work locally off shell on $`W>0`$, with no field equation, integration by parts, or background specialization. All spacetime derivatives remain full ordered superconformal derivatives. The Gold lowering convention is $`X_i=\varepsilon_{ij}X^j`$, with numerical $`\varepsilon_{ij}=-\varepsilon^{ij}`$; this is applied before the component bridge.

Even components retain degrees zero/two; the spinor retains degree one. Cubic spinor inputs and quartic primary inputs must be retained when a subsequent odd derivative can lower their degree. A degree-one linearity check is **not** by itself a degree-two current-conservation certificate.

## Definitions and Required Identities

The starting primary is the actual 58-term `make_inputs()` polynomial, including the documented H3.9 coefficient. Spinor and second descendants use S23 (3.26); elementary derivative and generator identities use S23 (2.6), (2.8), (2.13), (2.15), and C24 Appendix A. A theorem for the defining projector does not replace reduction of the actual polynomial.

The relevant algebra is C24 (2.2), (A.1), (A.2):

```math
[\nabla_A,\nabla_B\}=-T_{AB}{}^C\nabla_C-\tfrac12R(M)_{AB}{}^{cd}M_{cd}-R(J)_{AB}{}^{kl}J_{kl}-R(D)_{AB}\mathbb D-R(S)_{AB}{}^{\gamma k}S_{\gamma k}-R(K)_{AB}{}^cK_c.
```

The original printed C24 (A.1l), given on PDF page 82, reads

```math
[S_{\beta i},\nabla_a]=i(\Gamma_a)_\beta{}^\alpha\nabla_{\alpha i}-\tfrac14W_a{}^b(\Gamma_b)_\beta{}^\alpha S_{\alpha i}+\tfrac18(\Gamma_a\Gamma^b)_\beta{}^\gamma X_{\gamma i}K_b-\tfrac14W_{ab\beta i}K^b.\tag{CC-01-printed}
```

Its last two coefficients are real in the actual PDF, so this is not an OCR/transcription issue. Both require an additional $`i`$ to satisfy the same paper's super-Jacobi identity. Keep the printed formula and the project-derived repair separately identified.

## Detailed Derivation

### 1. Isolate the disputed coefficients by the $`S,\nabla,\nabla`$ super-Jacobi identity

Write the last two terms with initially unknown multipliers $`a_X,a_W`$:

```math
[S_{\delta l},\nabla_a]\big|_K=\mathcal V_{\delta l,a}{}^c K_c,\qquad \mathcal V_{\delta l,a}{}^c=\frac{a_X}{8}(\Gamma_a\Gamma^c)_\delta{}^\gamma X_{\gamma l}-\frac{a_W}{4}W_a{}^c{}_{\delta l}.\tag{CC-02}
```

The printed expression sets $`a_X=a_W=1`$. The super-Jacobi identity in the ordering used here is

```math
[S,\{\nabla_\alpha^i,\nabla_\beta^j\}]=[\{S,\nabla_\alpha^i\},\nabla_\beta^j]+[\{S,\nabla_\beta^j\},\nabla_\alpha^i].\tag{CC-03}
```

The right side has no $`K`$ coefficient: $`\{S,\nabla\}`$ is a linear combination of $`M,J,\mathbb D`$, whose commutators with a spinor derivative are again spinor derivatives. On the left, the $`-R(S)S`$ term needs an explicit graded sign. Since both $`S`$ and $`R(S)`$ are odd,

```math
[S,-R(S)S']=-(S R(S))S'+R(S)\{S,S'\}.\tag{CC-04}
```

Consequently the complete $`K_c`$ coefficient is

```math
\mathscr J_{\alpha\beta\delta}^{ij}{}_{l}{}^c=-2i\varepsilon^{ij}(\Gamma^a)_{\alpha\beta}\mathcal V_{\delta l,a}{}^c-S_{\delta l}R(K)_{\alpha\beta}^{ij,c}+R(S)_{\alpha\beta}^{ij,\gamma k}\{S_{\delta l},S_{\gamma k}\}\big|_{K_c}.\tag{CC-05}
```

There is no omitted $`R(M)`$ contribution to this coefficient: $`S W=0`$ and $`[S,M]`$ is an S generator. The $`W S`$ term in (CC-01) likewise has no role in (CC-05). The check is therefore independent of the separate $`W S`$ coefficient/frame issue.

C24 (A.2c,d) supplies

```math
R(S)_{\alpha\beta}^{ij,\gamma k}=\frac{3i}{4}\varepsilon^{ij}\varepsilon_{\alpha\beta}X^{\gamma k}+i\varepsilon^{ij}\delta_{[\alpha}^{\gamma}X_{\beta]}{}^k,\qquad R(K)_{\alpha\beta}^{ij,c}=-\frac i2\varepsilon^{ij}\varepsilon_{\alpha\beta}\nabla^bW_b{}^c+\frac i2\varepsilon^{ij}(\Gamma^a)_{\alpha\beta}\nabla^d\widetilde W_{da}{}^c-\frac{i}{32}\varepsilon^{ij}(\Gamma^c)_{\alpha\beta}Y+R(K)\big|_{W^2}.\tag{CC-06}
```

The last term is annihilated by $`S`$ since it is quadratic in the primary $`W_{ab}`$. To act on the derivative terms, use $`S W_{bc}=0`$ directly:

```math
S_{\delta l}(\nabla_aW_{bc})=[S_{\delta l},\nabla_a]W_{bc}=i(\Gamma_a)_\delta{}^\eta\varepsilon_{lr}\nabla_\eta^rW_{bc},\qquad S_{\delta l}Y=8iX_{\delta l}.\tag{CC-07}
```

The $`M,S,K`$ parts do not survive here: (CC-01) contains no $`M`$ term and $`S W=K W=0`$. S23 (2.6a) and the two-form/spinor dictionary give each derivative explicitly:

```math
\nabla_\eta^rW_{bc}=(\Sigma_{bc})^{\mu\nu}\left(W_{\mu\nu\eta}{}^r+\tfrac12\varepsilon_{\eta\mu}X_\nu{}^r+\tfrac12\varepsilon_{\eta\nu}X_\mu{}^r\right),\qquad\widetilde W_{abc}=\tfrac12\varepsilon_{abcde}W^{de}.\tag{CC-08}
```

Equations (CC-05)–(CC-08) reduce the Jacobi identity to a linear algebraic identity in the independent Weyl descendants $`X_\alpha^i`$ and completely symmetric $`W_{\alpha\beta\gamma}{}^i`$. There are $`4\times2=8`$ and $`\binom63\times2=40`$ independent entries, respectively. No background value or differential field equation has been imposed.

The executable [[jacobi_SDD.py](../results/gauged_full_fermionic_log/sources/certification_20260925/curved/jacobi_SDD.py)](../results/gauged_full_fermionic_log/sources/certification_20260925/curved/jacobi_SDD.py) separately builds the three contributions of (CC-05) from these equations using explicit Gold gamma matrices. It exhausts all **48** independent basis inputs and all **2560** free-index components for each input. Matrix entries and all coefficients are Gaussian dyadic rationals, so binary complex arithmetic is exact in this calculation; the comparison is literal `residual == 0`, with no tolerance. The complete result is **122880 exact zero equalities for $`a_X=a_W=i`$**. The original real coefficients fail.

Two individual entries make both corrections independently visible. The arrays use zero-based spinor and SU(2) labels. For $`X_0{}^0=1`$ with every other Weyl descendant zero, choose $`(\alpha,\beta,i,j,\delta,l,c)=(0,1,0,1,0,1,0)`$. The three entries of (CC-05) are $`-ia_X/4,-3/4,+1/2`$, hence

```math
0=-\frac i4a_X-\frac34+\frac12\quad\Longrightarrow\quad a_X=i.\tag{CC-09}
```

For $`W_{000}{}^0=1`$ with the other descendants zero, choose $`(\alpha,\beta,i,j,\delta,l,c)=(0,2,0,1,0,1,3)`$. The entries are $`-a_W/2,+i/2,0`$, hence

```math
0=-\frac12a_W+\frac i2\quad\Longrightarrow\quad a_W=i.\tag{CC-10}
```

These witnesses determine the two coefficients separately, and the exhaustive tensor check verifies them in every remaining component. The repaired relation is therefore

```math
\boxed{[S_{\beta i},\nabla_a]=i(\Gamma_a)_\beta{}^\alpha\nabla_{\alpha i}-\tfrac14W_a{}^b(\Gamma_b)_\beta{}^\alpha S_{\alpha i}+\tfrac{i}{8}(\Gamma_a\Gamma^b)_\beta{}^\gamma X_{\gamma i}K_b-\tfrac{i}{4}W_{ab\beta i}K^b.}\tag{CC-11-repaired}
```

Independent source support is [Butter et al., arXiv:1410.8682v2, Appendix C, (C.2)](https://arxiv.org/html/1410.8682v2#A3.E2): its last two coefficients are $`+i/8,-i/4`$. The linked source equation has MathML id `A3.E2.m2`. That paper's displayed hatted-frame $`W S`$ coefficient is $`-1/2`$, so **the full older relation is not imported unchanged**. The new repair follows (CC-05) within C24's own conventions. C24 page 9 identifies its traceless frame with this earlier appendix, but any remaining difference is a separate source audit question.

### 2. Why the omitted phases first affect the second LOG descendants

For an elementary K-primary $`U`$, $`K_cU=0`$. The difference between printed and repaired $`S\nabla`$ consequently vanishes on $`\nabla_aU`$ but need not vanish on a second derivative:

```math
\delta S_{\beta i}(\nabla_a\nabla_bU)=(i-1)\left[\tfrac18(\Gamma_a\Gamma^c)_\beta{}^\gamma X_{\gamma i}K_c(\nabla_bU)-\tfrac14W_a{}^c{}_{\beta i}K_c(\nabla_bU)\right],\qquad K_c\nabla_bU=2\eta_{cb}\mathbb DU+2M_{cb}U.\tag{CC-12}
```

For the vector gaugino, $`\mathbb D\lambda=3\lambda/2`$. Thus the difference is proportional to an undifferentiated $`\lambda`$, rather than a derivative of $`\lambda`$. In the second spinor differentiation this enters through the $`R(S)S`$ term of $`[\nabla_\alpha^i,\nabla_a]`$. This locates the defect upstream of the component projection and Clifford canonicalization. It also explains why tests with zero Weyl fermions miss it. The corresponding scalar/vector descendants require the same algebraic phases; reality alone does not determine the correction.

### 3. Exact K primarity of the actual primary through two fermions

The K-primary calculation applies every $`K_a`$ action to every factor of the actual primary retained through two fermions. It keeps all ordered spacetime derivatives and general bosonic/fermionic fields. The resulting 88 source contributions reduce to exact zero using only the locked tensor/Clifford rules and conventional traces. No background specialization, differential Bianchi identity, field equation, or integration by parts is used. The full-primary certificate linked below records the completed K-primary result.

### 4. Exact linearity through one fermion

Differentiate the actual $`H^{ij}_{(0)}+H^{ij}_{(2)}`$ before retaining odd degree one, and perform the three cyclic SU(2) placements explicitly. This gives 2778 source contributions and 5631 projected contributions. The SU(2) component expansion exhausts all eight free SU(2) triples and all dummy SU(2) sums; all spacetime fields and jets remain symbolic. After Clifford reduction, the remaining derivative structures are only

```math
\lambda\,\gamma^{ab}\nabla_a\nabla_bW,\qquad \lambda\,\varepsilon^{abcde}\nabla_aF_{bc},\qquad\lambda\,\varepsilon^{abcde}\nabla_aR(J)_{bc},\tag{CC-13}
```

plus algebraic $`R(Q)`$ gamma traces. C24 (A.4), the vector Bianchi identity S23 (2.14), and the curvature super-Bianchi identity imply that each antisymmetrized derivative in (CC-13) begins at two explicit fermions. For the scalar, $`[\nabla_a,\nabla_b]W=-T_{ab}{}^{\gamma k}\nabla_{\gamma k}W`$ because $`W`$ is a Lorentz/SU(2) singlet and primary and $`R(D)_{ab}=0`$. Both factors on the right are odd. For a two-form curvature, the three-vector Bianchi's corrections contain the odd spinor torsion times an odd spinor-vector curvature. Therefore each whole expression (CC-13) begins at degree three, and can be omitted **only in this degree-one check**.

The remaining algebraic curvature terms vanish after the explicit $`R(Q)`$ gamma-traceless projector. Each of the eight free SU(2) components becomes exactly zero. The displayed degree argument identifies the omitted derivative structures. This establishes $`[\nabla_\alpha^{(i}H^{jk)}]_{\le1}=0`$ for the actual expression in general curved geometry. The degree-three identity still requires the nonzero right sides of (CC-13), quartic-primary differentiation, and cubic-spinor Fierz reduction.

### 5. S primarity after the phase repair

The unrepaired polynomial contains a nonzero $`\rho^{-1}Y^{ij}\chi`$ residue; in two SU(2) components it is the sole remaining monomial. Installing (CC-11) in a certification-only copy cancels those two components exactly. The other components require the actual vector-vector commutator on the gaugino rather than treating ordered derivatives as commuting.

[vector_commutator.py](../results/gauged_full_fermionic_log/sources/certification_20260925/curved/vector_commutator.py) implements C24 (A.4a–d) explicitly:

```math
[\nabla_a,\nabla_b]\lambda=-T_{ab}{}^{\gamma k}\nabla_{\gamma k}\lambda-\tfrac12R(M)_{ab}{}^{cd}M_{cd}\lambda-R(J)_{ab}{}^{kl}J_{kl}\lambda-R(S)_{ab}{}^{\gamma k}S_{\gamma k}\lambda.\tag{CC-14}
```

Here $`K\lambda=0`$ and $`R(D)_{ab}=0`$ remove those two terms; all other terms, including the spinor torsion, are retained. The source result is projected using the locked $`\lambda_G|=-\lambda`$ bridge exactly once. The S-primary reduction replaces only a gamma-antisymmetrized Hessian by one half of this commutator, then applies the correctly counted Bianchi relations and $`R(Q)`$ projector. The fully antisymmetric $`R(M)`$ term multiplied by $`\lambda`$ begins at degree three by the torsionless super-Bianchi identity, so its omission is valid at degree one. The completed S-primary results are recorded in the full-primary certificate below.

### 6. Complete primary checks, including the fermions needed before odd differentiation

The full input has degrees zero, two, four and six. The full-primary calculation keeps the complete 58-term input before applying any generator or spinor derivative. Its linearity polynomial contains degrees one, three, five and seven; its S-primary polynomial contains degrees one, three and five. The degree-six part of $`H`$ is an undifferentiated polynomial in $`\lambda`$, so $`K H_{(6)}=0`$ directly. Checking $`K H`$ through degree four therefore checks its entire possible result.

The multi-chain reduction treats every open/bilinear chain and gives each dualization its own dummy labels. Its independent tensor comparison evaluates both the complete raw projected polynomial and the reduced polynomial as tensors of coefficients in independent field components. Every occurrence of a physical field has an independent component-selector axis. Identical bosonic factors are symmetrized and identical fermionic factors antisymmetrized. Thus these arrays test every Fierz/Grassmann coefficient, rather than values at sampled fields.

For $`R(Q)`$ the selectors span the full gamma-traceless space. The implementation uses 24 times the projector

```math
(\Pi R)_{ab}=R_{ab}+\frac13\gamma_a\gamma^cR_{bc}-\frac13\gamma_b\gamma^cR_{ac}-\frac1{24}\gamma_a\gamma_b\gamma^{cd}R_{cd}+\frac1{24}\gamma_b\gamma_a\gamma^{cd}R_{cd}.\tag{CC-15}
```

Its gamma trace vanishes exactly. If the input already has zero gamma trace, the added terms vanish, so $`\Pi R=R`$; the image therefore spans the whole constrained space. The factor 24 keeps all selector entries Gaussian integers. Derivative selectors retain the order of their vector indices and impose only the differentiated algebraic gamma-trace constraint.

Laurent powers of $`W`$ are compared separately. No numerical value of $`W`$, a background curvature, a field equation, a vanishing fermion, or a commuting-derivative assumption is used.

Before replacing any derivative by a Bianchi or commutator, the complete coefficient tensor is tested to be antisymmetric in precisely those derivative slots. For example, if $`A_{a,bc}`$ denotes a field-strength derivative with $`b<c`$, the ten three-form basis columns $`B`$ obey $`B^TB=3\mathbf1`$. The residual coefficient $`C`$ passes the exact test $`3C-CBB^T=0`$. Only then is the fully antisymmetric derivative replaced. Scalar and spinor Hessian coefficients pass $`C_{ab}+C_{ba}=0`$, allowing replacement by one half of the commutator.

The nonzero differential identities are retained at their full fermion order. The source spinor Bianchi identities S23 (2.14), (2.7a) give, in the locked projected spinor-index notation,

```math
\mathcal D_{[a}\widehat F_{bc]}=\frac12 R(Q)_{[ab}{}^{\alpha k}(\gamma_{c]})_{\alpha\beta}\lambda^\beta{}_k,\qquad \mathcal D_{[a}R(V)_{bc]}{}^{ij}=4R(Q)_{[ab}{}^{\alpha(i}(\gamma_{c]})_{\alpha\beta}\chi^{\beta j)}.\tag{CC-16}
```

Here the indexed $`\gamma_{a\alpha\beta}`$ and spinor raising use the locked $`\mathsf C`$ bridge; (CC-16) is not an informal conversion to untracked barred-spinor notation. The curl-identity comparison projects both sides of the source identities, substitutes the displayed fully antisymmetric tensor expressions, and checks every independent $`R(Q)`$–spinor coefficient. After clearing denominators, the coefficient $`1/2`$ and coefficient $`4`$ each have exactly zero residual.

The scalar commutator follows directly from the spinor torsion and $`\nabla_\alpha^iW=i\lambda_{G\alpha}^i`$:

```math
[\nabla_a,\nabla_b]W=\frac i2 W_{ab}{}^\alpha{}_i\nabla_\alpha^i W=-\frac12W_{ab}{}^\alpha{}_i\lambda_{G\alpha}^i,\qquad [\mathcal D_a,\mathcal D_b]\rho=\frac i2R(Q)_{ab}{}^\alpha{}_i\lambda_\alpha^i.\tag{CC-17}
```

The gaugino Hessian uses the complete (CC-14). The complete differential reduction keeps all resulting terms through degree seven for full linearity and through degree five for full S primarity. In particular, the two-fermion right sides of (CC-16)–(CC-17) are **not discarded** when they multiply cubic or quintic fermion factors. This removes the order-counting loophole present in a degree-one-only test.

There is also an exact algebraic curvature identity, stronger than a bosonic approximation. C24 (A.4c) maps the completely symmetric rank-four spinor $`iW_{\alpha\beta\gamma\delta}+3W_{(\alpha\beta}W_{\gamma\delta)}`$ to $`R(M)_{ab,cd}`$. The script [curvature_algebraic_bianchi.py](../results/gauged_full_fermionic_log/sources/certification_20260925/curved/curvature_algebraic_bianchi.py) evaluates this map on every one of its 35 independent basis tensors and verifies cyclic symmetry, pair exchange and the Lorentz trace exactly. Thus a contraction of three $`R(M)`$ indices into an epsilon tensor vanishes in the **full traceless superspace frame**, including when multiplied by one or three fermions. No bosonic truncation is used for this step.

The final complete-field identities are:

| Actual polynomial tested | Complete raw component terms | Final independent coefficient entries | Residual |
|---|---:|---:|---:|
| $`\nabla_\alpha^0H^{00}`$, all degrees 1,3,5,7 | 6840 | 603104 in 56 groups | exactly zero |
| $`S_{\alpha0}H^{00}`$, all degrees 1,3,5 | 813 | 24576 in 19 groups | exactly zero |
| $`S_{\alpha1}H^{00}`$, all degrees 1,3,5 | 321 | 15104 in 9 groups | exactly zero |
| $`K_aH^{00}`$, all possible degrees 0,2,4 | 126 | 1280 in 1 group | exactly zero |

The free SU(2) components are exhausted by covariance, rather than inferred from a particular field sample. The linearity tensor is completely symmetric with three SU(2) indices. Its highest component vanishes for **arbitrary values of every SU(2) field component**. Rotating all arbitrary fields therefore proves the contraction with any rotated highest-weight vector vanishes; polarization gives every symmetric component. The same argument applies to $`K_aH^{ij}`$. Raising the lower index of $`S_{\alpha k}H^{ij}`$ produces a tensor symmetric in $`i,j`$, decomposing into a symmetric rank-three tensor and $`\varepsilon^{ki}A^j+\varepsilon^{kj}A^i`$. The tested $`S_{\alpha1}H^{00}`$ kills the highest rank-three component; $`S_{\alpha0}H^{00}`$ then kills the highest doublet component. Covariance kills both irreducible tensors. The fermion grading and every identity used in the reduction preserve SU(2) covariance.

The full raw-to-reduced comparison is itself exhaustive: all raw coefficient groups agree after cross-multiplying their exact coefficient denominators. The largest comparison $`L^1`$ bound is $`5435817984<2^{53}`$, and the residual is exactly zero. This independently checks the multi-chain extension against the actual unreduced polynomial.

### 7. Why the coefficient certificates are exact

The arrays have Gaussian-integer entries after clearing the rational polynomial coefficients. `bounded_einsum` executes the selected contraction path one contraction at a time. Before each contraction, it bounds every output entry by the product of the input maximum entry $`L^1`$ norms times the number of summed-index combinations. It requires this bound to be below $`2^{53}`$ **before** performing the floating-storage integer operations. It separately bounds coefficient multiplication, group addition, and each permutation sum. Thus checking that an output happens to be integer-valued is not the sole safeguard.

For the largest raw linearity calculation, the maximum internal contraction bound is 36864, the maximum coefficient-product bound is 2949120, the maximum group-addition bound is 4128768, and the maximum permutation-addition bound is 6045696. All are far below the exact binary64 integer range. The exact-identity result is therefore supported by a bound on the actual arithmetic path, not just by a numerical tolerance. [full-primary-certificate.json](../results/gauged_full_fermionic_log/sources/certification_20260925/curved/full-primary-certificate.json) records all bounds and the input/script hashes.

### 8. Apply the verified primary to the complete descendant tower and vector constraint

The full primary constraint is established for the actual polynomial, so using the general linear-multiplet integrability identities is justified. This is different from assuming that the stored polynomial equals a projector merely because the projector is known to define a linear multiplet.

First, the linearity constraint leaves only the SU(2) doublet part of $`\nabla_\alpha^iH^{jk}`$. Contracting that doublet fixes its coefficient by the definition of $`\varphi`$:

```math
\varphi_\alpha^i=\frac13\nabla_{\alpha j}H^{ij},\qquad\nabla_\alpha^iH^{jk}=\varepsilon^{ij}\varphi_\alpha^k+\varepsilon^{ik}\varphi_\alpha^j.\tag{CC-18}
```

When the two-spinor derivative algebra acts directly on $`H`$, the Lorentz curvature acts on a Lorentz scalar, while $`R(S)`$ and $`R(K)`$ annihilate the verified primary. C24 (A.2) has no spinor-spinor $`R(D)`$ or $`R(J)`$ term. Therefore

```math
\{\nabla_\alpha^i,\nabla_\beta^j\}H^{kl}=-2i\varepsilon^{ij}\nabla_{\alpha\beta}H^{kl}.\tag{CC-19}
```

Differentiating (CC-18), interchanging the two derivatives with (CC-19), and taking the scalar/vector traces gives precisely the general identity S23 (2.21b), with descendants defined by S23 (2.22):

```math
\nabla_\alpha^i\varphi_\beta^j=-\frac i2\varepsilon^{ij}\varepsilon_{\alpha\beta}F+\frac i2\varepsilon^{ij}\mathcal H_{\alpha\beta}+i\nabla_{\alpha\beta}H^{ij},\qquad F=-\frac i4\nabla^{\alpha k}\varphi_{\alpha k},\qquad \mathcal H^a=\frac i{12}(\Gamma^a)^{\alpha\beta}\nabla_{\alpha i}\nabla_{\beta j}H^{ij}.\tag{CC-20}
```

The higher identities S23 (2.21c,d) and S transformations (2.24) apply to these definitions with the **repaired, Jacobi-consistent** algebra. The separate production-chain certificates must identify the stored scalar and vector with these definitions; this report does not replace that equality check.

The constrained-vector identity can also be seen directly from the closed four-form. Butter et al. (8.5), (8.6b,c), give

```math
\nabla_{[A}\Phi_{BCDE\}}+2T_{[AB}{}^F\Phi_{|F|CDE\}}=0,\qquad\Phi_{abc\,\alpha}{}^i=-2\varepsilon_{abcde}(\Sigma^{de})_\alpha{}^\beta\varphi_\beta^i,\qquad\Phi_{abcd}=\varepsilon_{abcde}\mathcal H^e.\tag{CC-21}
```

Their original unhatted derivative is not the current traceless-frame derivative: the same source's (8.9) explicitly states $`\nabla^a\Phi_a+5iX^{\gamma k}\varphi_{\gamma k}=\widehat\nabla^a\Phi_a=0`$. In the present C24 traceless frame the spinor torsion is instead exactly $`T_{ab}{}^\alpha{}_i=-iW_{ab}{}^\alpha{}_i/2`$, C24 (A.4a). Use that torsion in the all-vector component of (CC-21).

Contract (CC-21) with $`\varepsilon^{abcde}`$. The derivative term is $`-4!\nabla_a\mathcal H^a`$. Moving the spinor slot of $`\Phi_{\alpha cde}`$ through three vector slots gives $`\Phi_{\alpha cde}=-\Phi_{cde\alpha}=+2\varepsilon_{cdefg}\Sigma^{fg}\varphi`$. The epsilon contraction is $`\varepsilon^{abcde}\varepsilon_{cdefg}=-3!(\delta^a_f\delta^b_g-\delta^a_g\delta^b_f)`$. Hence

```math
0=-24\nabla_a\mathcal H^a-48T_{ab}{}^\alpha{}_i(\Sigma^{ab})_\alpha{}^\beta\varphi_\beta^i,\qquad\nabla_a\mathcal H^a=-2T_{ab}{}^\alpha{}_i(\Sigma^{ab})_\alpha{}^\beta\varphi_\beta^i=iW_{ab}{}^\alpha{}_i(\Sigma^{ab})_\alpha{}^\beta\varphi_\beta^i=0.\tag{CC-22}
```

The last equality is the full algebraic gamma-trace constraint on $`W_{ab\alpha}{}^i`$; multiplying the one-gamma trace by another gamma kills its two-gamma trace as well. This proves conservation in the **full** supercovariant traceless derivative. The proof consumes the all-order verified linearity constraint, so no degree-five/seven omission can contaminate the retained two-fermion current. Translating this into a coordinate divergence of the component completed current, including explicit gravitino terms, is given in the form/BF projection certificate.

## Consistency Checks

- The algebra phase repair is fixed by an independent source-local Jacobi identity, not by fitting a LOG coefficient or a reality condition.
- All source and projected primary-check monomials pass weight and free/dummy-index checks before simplification.
- Finite SU(2) componentization is exhaustive, not random sampling. Spacetime/Lorentz tensors remain general symbolic tensors.
- The old-source failure and the corrected zero residuals are retained separately.
- Component reality and descendant-to-component equality are separate identities, with their own source records.

## Final Result

**Confirmed:** C24 (A.1l) is missing factors of $`i`$ in both displayed K-generator terms; the correct coefficients in the locked algebra are $`+i/8`$ and $`-i/4`$. This is established by all 122880 exact source-local Jacobi components and independently supported by the earlier conformal-superspace paper. The actual LOG primary passes exact general-field K primarity, S primarity and linearity at all its explicit fermion orders. The final evidence is [the full-primary certificate](../results/gauged_full_fermionic_log/sources/certification_20260925/curved/full-primary-certificate.json); the degree-one arguments are displayed above as intermediate reductions.

**Recorded result:** full curved linearity, S primarity and K primarity of the actual 58-term polynomial at every possible explicit fermion order, with exhaustive raw-polynomial comparisons and bounded exact arithmetic. The full supercovariant vector constraint follows by the explicit closed-four-form calculation (CC-21)–(CC-22). **Separate certificates:** equality to the defining six-derivative projector; equality of the regenerated stored descendants to their derivative definitions; their component reality; and the completed BF density/current projection.

## Convention Dependence and Remaining Uncertainties

All statements use the Gold traceless-frame derivative and source-to-project bridge. The different printed $`W S`$ coefficient in the older paper was not changed by this investigation. Full nonlinear BF FORM-01 and bosonic boundary reduction are separate source comparisons. No spectrum certificate is claimed here. The source-to-component BF supersymmetry conclusion depends additionally on the separately regenerated descendant and FORM certificates.
