# LOG multiplet: canonical form through two fermions

<!-- LOG_CURRENT_CERTIFICATION_20260925 -->

**Current scope:** [the 2026-09-25 certificate](CERTIFICATION_LOG_TWO_FERMI_2026-09-25.md) verifies the full primary and the component action through two physical fermions. The source comparisons and restricted tests below retain their stated mathematical scope.

## Contents

1. [Scope and starting point](LOG_MULTIPLET_CANONICAL_TWO_FERMI.md#1-scope-and-starting-point)
2. [Conventions and truncation](LOG_MULTIPLET_CANONICAL_TWO_FERMI.md#2-conventions-and-truncation)
3. [Algebraic reduction](LOG_MULTIPLET_CANONICAL_TWO_FERMI.md#3-algebraic-reduction)
4. [Verification and limits](LOG_MULTIPLET_CANONICAL_TWO_FERMI.md#4-verification-and-limits)
5. [Complete collected result](LOG_MULTIPLET_CANONICAL_TWO_FERMI.md#5-complete-collected-result)

**Source repair, 2026-09-25.** The scalar and vector include the Jacobi-required $`i`$ factors in the K part of C24 (A.1l). Literal source equations and pre-repair calculations are preserved. The projection factors, full $`\mathcal D`$/$`\Box^c`$ convention, Grassmann ordering and BF coefficients are unchanged. See the [certification investigation](../../../../../../references/source_evidence/README.md).

## 1. Scope and starting point

This is a separate simplification of the four projected polynomials in [Step 6](STEP_06_LOG_PROJECTED_MULTIPLET_AND_BOSONIC_ACTION.md), §§7.1–7.4. It retains the bosonic and bilinear sectors of $`L_{\log}^{ij},N_{\log},E_{\log}^{a}`$ and the linear sector of $`\varphi_{\log}^{i}`$. The scalar and vector are shortened by contracting invariant metrics, removing zero traces, reducing Clifford products, and collecting tensor contractions including their Grassmann signs. No covariant derivatives are interchanged and no integration by parts or field equation is used.

The result is **canonical under the algebraic rules stated below**, rather than a claim of the smallest possible basis under every differential Bianchi, dimension-dependent Schouten or constrained-curvature identity. It is in the same gauge-unfixed Standard-Weyl component frame as Step 6. No gauged dilaton-Weyl substitution is added here.

The source chain is S23 (3.24)–(3.26), followed by the already performed component projection and convention bridge. In particular,

```math
L_{\log}^{ij}=-2H^{ij}|,\qquad \varphi_{\log\alpha}^{i}=-2i\varphi_{G\alpha}^{i}|,\qquad N_{\log}=-F_G|,\qquad E_{\log}^{a}=\mathcal H_G^{a}|.
\tag{CTF-01}
```

These equalities define the input used in this file. Located references: S23 (3.26), [cached p.22](https://arxiv.org/abs/2302.14295); C24 (2.15)–(2.17), [p.12](https://arxiv.org/abs/2311.00679) and [p.13](https://arxiv.org/abs/2311.00679); C24 Appendix C, Tables 4–6, [p.90](https://arxiv.org/abs/2311.00679), [p.91](https://arxiv.org/abs/2311.00679), [p.92](https://arxiv.org/abs/2311.00679). The explicit input normalization is Step 6 (S6-01)–(S6-09).

## 2. Conventions and truncation

<!-- ASSERT_CONVENTION: metric_signature=(-,+,+,+,+), natural_units=hbar=c=1, source_frame=project Standard-Weyl components, gamma_volume=+i, bar=linear Majorana, derivative_order=preserved, regularization_scheme=Not applicable for initial classical analysis -->

The convention references are [CONVENTIONS.md](CONVENTIONS.md) and [LOG_CONVENTIONS.md](LOG_CONVENTIONS.md). The calculation uses the scoped Gold superspace conventions.

We use $`a=0,\ldots,4`$, $`\alpha=1,\ldots,4`$, $`i=1,2`$, weighted antisymmetrization, and

```math
\eta_{ab}=\mathop{\mathrm{diag}}\nolimits(-,+,+,+,+),\quad \{\gamma^a,\gamma^b\}=2\eta^{ab},\quad \gamma^{01234}=i,\quad \epsilon^{01234}=1,\quad \overline\zeta=\zeta^T\mathsf C.
\tag{CTF-02}
```

The Majorana bar is linear, including on $`i`$. All fermions are Grassmann odd. The doublet convention is $`v_i=v^j\varepsilon_{ji}`$, $`v^i=\varepsilon^{ij}v_j`$, with $`\varepsilon_{12}=\varepsilon^{12}=1`$. The spinor metric obeys $`\mathsf C^T=-\mathsf C`$, $`\mathsf C^2=-1`$, and $`\mathsf C^{\alpha\beta}=(-\mathsf C)_{\alpha\beta}`$. In particular,

```math
(\gamma^{a_1\cdots a_p})_{\alpha\beta}=-\big(\gamma^{a_1\cdots a_p}\mathsf C\big)_{\alpha\beta},\qquad (\gamma^{a_1\cdots a_p})^{\alpha\beta}=-\big(\mathsf C\gamma^{a_1\cdots a_p}\big)_{\alpha\beta}.
\tag{CTF-03}
```

The indexed gamma tensor and the Majorana bilinear kernel have different matrix placements; (CTF-03) is the rule of Step 6 (S6-03), not an identification of those kernels.

| Symbol | Meaning | Weyl weight |
|---|---|---:|
| $`\rho,\lambda^i,Y^{ij}`$ | Defining vector scalar, spinor and symmetric auxiliary | $`1,3/2,2`$ |
| $`\widehat F_{ab}`$ | Defining vector supercovariant two-form | $`2`$ |
| $`T_{ab},\chi^i,D`$ | Standard-Weyl auxiliary fields | $`1,3/2,2`$ |
| $`R(Q)_{ab}^{i}`$ | Supercovariant spinor-valued two-form | $`3/2`$ |
| $`R(V)_{ab}^{ij}`$ | Supercovariant SU(2) curvature, symmetric in $`ij`$ | $`2`$ |
| $`R(M)_{abcd}`$ | Project supercovariant traceless Lorentz curvature | $`2`$ |
| $`\mathcal D_a`$ | Full covariant derivative of Step 6 (S6-07)–(S6-09) | $`1`$ |

Hats on the three curvatures are suppressed. $`R(M)`$ is not replaced by the ordinary Riemann tensor. Its two antisymmetric index pairs are used; no extra pair exchange or differential Bianchi identity is assumed here. $`R(Q)_{ab}^{i}`$ in the final formulas is a spinor with its spinor index suppressed. Thus $`\overline{R(Q)_{ab}^{i}}\gamma^c\lambda_j`$ is an ordinary Majorana bilinear. A bar over a differentiated spinor applies to that entire differentiated spinor; it does not move a derivative onto another factor.

The only additional scalar contractions abbreviated in the final expressions are

```math
T^2=T_{ab}T^{ab},\qquad \widehat F^2=\widehat F_{ab}\widehat F^{ab},\qquad Y^2=Y^{ij}Y_{ij},\qquad \Box^c X=\mathcal D^a\mathcal D_aX.
\tag{CTF-03a}
```

A box is introduced only for an adjacent contracted pair of derivatives. Expressions such as $`\mathcal D^a\mathcal D_b\mathcal D_aX`$ retain their displayed order. $`D^2`$ denotes the square of the auxiliary scalar, not this box. “Traceless frame” is the source frame label; no additional contraction of $`R(M)`$ is set to zero on the strength of that name.

Assumptions and the precise order prescription:

1. All fields stay off shell and $`\rho>0`$; no auxiliary elimination or compensator gauge is imposed.
2. The retained order is a formal expansion in fermion degree. Introduce $`t`$ multiplying every elementary fermion, including the gravitino. Define $`[X]_{\leq2}`$ by retaining $`t^0,t^1,t^2`$ and then setting $`t=1`$.
3. Supercovariant tensors and derivatives are retained as compact notation. Their implicit fermions must receive the same projection. Keeping two **explicit** fermions does not permit keeping arbitrary additional fermions inside a connection.

For practical use of the displayed compact expressions, if an even covariant factor is $`B=B^{(0)}+B^{(2)}+\cdots`$ and an odd factor is $`\Psi=\Psi^{(1)}+\cdots`$, then

```math
\left[\prod_{r=1}^{m}B_r\right]_{\leq2}=\prod_{r=1}^{m}B_r^{(0)}+\sum_{s=1}^{m}B_s^{(2)}\prod_{r\ne s}B_r^{(0)},\qquad
\left[B\overline\Psi\Gamma\Xi\right]_{\leq2}=B^{(0)}\overline{\Psi^{(1)}}\Gamma\Xi^{(1)}.
\tag{CTF-04}
```

Each ordered differentiated field is a covariant factor for this rule. Likewise $`[B\Psi]_{\leq2}=B^{(0)}\Psi^{(1)}`$. This outer projection makes the final result strictly through quadratic order while leaving its supercovariant notation compact. It is not a separate expansion into elementary connection terms. The first omitted degree is four in an even slot and three in the spinor. Fermion degree is not a numerical smallness estimate, and the truncated slots alone do not assert exact nonlinear supersymmetry.

## 3. Algebraic reduction

### 3.1 Contract metrics and eliminate zeros

Let $`J=\begin{pmatrix}0&1\\-1&0\end{pmatrix}`$. Both printed project SU(2) epsilons have array $`J`$, whereas **lowering a field** on the left uses $`-J`$. Explicitly, $`v_i=(-J)_{ij}v^j`$ and $`J(-J)=1`$. This distinction is retained before contracting any closed epsilon loop. For example,

```math
\varepsilon^{ij}\varepsilon_{ij}=2,\qquad \varepsilon^{ij}\varepsilon_{ji}=-2,\qquad \mathsf C^{\alpha\beta}\mathsf C_{\alpha\beta}=-4.
\tag{CTF-05}
```

After the inverse metrics have been contracted, the following local contractions vanish:

```math
\mathop{\mathrm{tr}}\nolimits\gamma^a=\mathop{\mathrm{tr}}\nolimits\gamma^{ab}=0,\qquad A^a{}_a=0\quad(A_{ab}=-A_{ba}),\qquad S^i{}_i=S^{ij}\varepsilon_{ji}=0\quad(S^{ij}=S^{ji}).
\tag{CTF-06}
```

The last relation applies to $`Y`$ and to the SU(2) pair of $`R(V)`$. The antisymmetric trace relation applies to $`\widehat F,T,R(Q),R(V)`$ and each Lorentz pair of $`R(M)`$. It also applies after ordered covariant differentiation because the invariant metrics are covariantly constant. For example, $`\mathcal D_cR(V)_{ab}{}^i{}_i=\mathcal D_c0=0`$.

### 3.2 Reduce each Clifford chain

The anticommutator in (CTF-02) gives the following recursion, with each omitted index indicated by a hat:

```math
\gamma^{a_1\cdots a_p}\gamma^b=\gamma^{a_1\cdots a_pb}+\sum_{r=1}^{p}(-1)^{p-r}\eta^{a_rb}\gamma^{a_1\cdots\widehat{a_r}\cdots a_p}.
\tag{CTF-07}
```

For instance,

```math
\gamma^a\gamma^b=\gamma^{ab}+\eta^{ab},\qquad \gamma^{ab}\gamma^c=\gamma^{abc}+\eta^{bc}\gamma^a-\eta^{ac}\gamma^b.
\tag{CTF-08}
```

To append a two-index gamma, first append $`\gamma^b`$, then $`\gamma^c`$, and subtract $`\eta^{bc}`$ times the original chain, since $`\gamma^{bc}=\gamma^b\gamma^c-\eta^{bc}`$. This recursively fixes every coefficient; no gamma product is fitted to a desired component result.

Ranks three to five are then reduced with the locked volume element:

```math
\gamma^{abc}=-\frac{i}{2}\epsilon^{abcde}\gamma_{de},\qquad \gamma^{abcd}=i\epsilon^{abcde}\gamma_e,\qquad \gamma^{abcde}=i\epsilon^{abcde}\mathbf1.
\tag{CTF-09}
```

The sign can be checked directly: $`\gamma^{012}\gamma^{34}=i`$ and $`(\gamma^{34})^2=-1`$ give $`\gamma^{012}=-i\gamma^{34}`$. Thus the first coefficient in (CTF-09) is negative. All surviving open chains use $`1,\gamma^a,\gamma^{ab}`$. Closed chains use

```math
\mathop{\mathrm{tr}}\nolimits\mathbf1=4,\quad \mathop{\mathrm{tr}}\nolimits\gamma^{a_1\cdots a_p}=0\ (1\leq p\leq4),\quad \mathop{\mathrm{tr}}\nolimits\gamma^{abcde}=4i\epsilon^{abcde},\quad
\mathop{\mathrm{tr}}\nolimits(\gamma^{ab}\gamma^{cd})=4(\eta^{ad}\eta^{bc}-\eta^{ac}\eta^{bd}).
\tag{CTF-10}
```

Products of two Levi-Civita tensors are reduced as well. Move their $`q`$ contracted indices to the last $`q`$ slots, retaining the sign of each permutation, then use

```math
\epsilon^{a_1\cdots a_p c_1\cdots c_q}\epsilon_{b_1\cdots b_p c_1\cdots c_q}=-q!\sum_{\pi\in S_p}\mathop{\mathrm{sgn}}\nolimits(\pi)\delta^{a_1}_{b_{\pi(1)}}\cdots\delta^{a_p}_{b_{\pi(p)}},\qquad p+q=5.
\tag{CTF-10a}
```

The minus sign is the Lorentzian determinant sign. For $`q=5`$ this gives $`\epsilon^{abcde}\epsilon_{abcde}=-120`$. For $`q=3`$, it gives $`\epsilon^{ab cde}\epsilon_{fg cde}=-6(\delta^a_f\delta^b_g-\delta^a_g\delta^b_f)`$. With other free-index variances, the Kronecker tensors acquire the corresponding metrics. Each resulting metric is contracted before like monomials are collected.

One additional five-dimensional two-form identity removes repeated epsilon contractions. For an undifferentiated two-form $`A`$ (here $`T`$ or $`\widehat F`$), define $`v_a=\epsilon_{abcde}A^{bc}A^{de}`$ and $`S_{abcd}=A_{[ab}A_{cd]}`$. The weighted antisymmetrization gives $`S_{abcd}=(A_{ab}A_{cd}-A_{ac}A_{bd}+A_{ad}A_{bc})/3`$. Dualizing this four-form gives $`S_{abcd}=-\epsilon_{abcde}v^e/24`$. Consequently,

```math
\begin{aligned}
A_c{}^d\epsilon_{abdef}A^{ef}&=\epsilon_{abdef}S_c{}^{def}=-\frac1{24}\epsilon_{abdef}\epsilon_c{}^{def}{}_g v^g\\
&=\frac14(\eta_{bc}v_a-\eta_{ac}v_b).
\end{aligned}
\tag{CTF-10b}
```

In the first equality, the three terms in $`S_c{}^{def}`$ give the same contraction after relabeling $`d,e,f`$. In the last equality, moving $`g`$ past three indices and applying (CTF-10a) fixes the sign. The reduction applies this identity in sectors containing exactly two undifferentiated copies of the same two-form, then substitutes the full epsilon expression for $`v_a`$ again. Thus $`v_a`$ is not an undefined composite in the final answer. This specific dimension-dependent identity is used; a complete minimal basis under all Schouten identities is not claimed.

Every gamma in the input retains its displayed spinor variance during this calculation. In matrix notation its four placements are

```math
\gamma_{\alpha\beta}=-\Gamma\mathsf C,\qquad \gamma_\alpha{}^\beta=\Gamma,\qquad \gamma^\alpha{}_\beta=\mathsf C\Gamma\mathsf C,\qquad \gamma^{\alpha\beta}=-\mathsf C\Gamma,
\tag{CTF-11}
```

where $`\Gamma`$ denotes the corresponding Clifford matrix, including its Lorentz indices. Multiplying these matrices along a contracted spinor chain removes adjacent $`\mathsf C`$ factors using $`\mathsf C^2=-1`$. A chain ending on two lower-index spinors is proportional to $`\mathsf C\Gamma`$, which is precisely the Majorana bilinear kernel. A chain ending on the single spinor slot is proportional to $`\Gamma`$.

### 3.3 Grassmann signs and dummy indices

No sign is assigned by inspection of a printed bilinear. For $`p=0,1,2`$, set $`K_p=\mathsf C\gamma^{a_1\cdots a_p}`$. The matrix identities give $`K_p^T=\tau_pK_p`$ with $`(\tau_0,\tau_1,\tau_2)=(-1,-1,+1)`$. Hence

```math
\Psi^\alpha(K_p)_{\alpha\beta}\Xi^\beta=-\Xi^\beta(K_p)_{\alpha\beta}\Psi^\alpha=-\tau_p\Xi^\alpha(K_p)_{\alpha\beta}\Psi^\beta.
\tag{CTF-12}
```

Thus scalar and vector bilinears have exchange sign $`+1`$, and two-form bilinears have exchange sign $`-1`$, before accounting for an additional antisymmetric SU(2) contraction. Lorentz and SU(2) tensor symmetries and Grassmann factor exchanges are included together when dummy names are put in canonical order. Derivative slots never participate in a slot permutation: $`\mathcal D_a\mathcal D_bX`$ is not identified with $`\mathcal D_b\mathcal D_aX`$.

### 3.4 Worked scalar contraction

The first two input scalar summands are each $`-1/288`$ times an $`R(V)R(V)`$ contraction and a two-gamma spinor contraction. Reducing their indexed matrices with (CTF-11) gives in each case

```math
4(\delta_b^c\delta_a^d-\delta_a^c\delta_b^d)R(V)^{ab}{}_i{}^jR(V)_{cd}{}^i{}_j=-8R(V)^{ab}{}_i{}^jR(V)_{ab}{}^i{}_j.
\tag{CTF-13}
```

For symmetric doublet tensors $`X^{ij},Y^{ij}`$, substituting $`X_i{}^j=(-J)_{ik}X^{kj}`$ and $`Y^i{}_j=(-J)_{j\ell}Y^{i\ell}`$ gives $`X_i{}^jY^i{}_j=-X^{ij}Y_{ij}`$. Therefore those two summands combine as

```math
2\left(-\frac1{288}\right)(-8)(-1)R(V)_{ab}^{ij}R(V)^{ab}_{ij}=-\frac1{18}R(V)_{ab}^{ij}R(V)^{ab}_{ij}.
\tag{CTF-14}
```

This is the subtotal of the two indicated summands. Other input terms can contribute to the same structure; (CTF-14) is not substituted as the coefficient of the whole scalar. The complete sum is collected independently below.

## 4. Verification and limits

The reduction uses exact rational real and imaginary coefficients. Every retained input monomial is parsed and checked for free indices, paired dummy indices, conformal weight and Grassmann degree. Every output monomial receives the same checks. The weights are $`3,7/2,4,4`$ for $`L,\varphi,N,E`$, respectively. Since invariant metrics and gamma tensors have weight zero, each algebraic replacement preserves weight individually.

The reproducible implementation is [canonicalize_log_two_fermi.py](../../../../../../references/source_evidence/log/results/gauged_full_fermionic_log/scripts/canonicalize_log_two_fermi.py). Independent finite-matrix and two-generator exterior-algebra tests are in [verify_log_two_fermi_canonical.py](../../../../../../references/source_evidence/log/results/gauged_full_fermionic_log/scripts/verify_log_two_fermi_canonical.py). The Clifford recursion is checked for all 160 independent basis-blade/vector products, all 16 independent rank-three/four/five duality identities, and all 240 one-/two-index gamma placements and transposes, with exactly zero matrix-entry residual. A further 240 exact component tests check (CTF-10a) across all six possible numbers of contracted indices. Random component checks compare input contractions, canonical tensor contractions and reduced gamma contractions, with arbitrary independent covariant derivative jets and the stated tensor symmetries. These component checks are additional checks, not an exhaustive proof by sampling.

The zero-fermion limit simply retains the degree-zero rows below; there is no cancellation against discarded degree-four terms. The flat limit can set the Standard-Weyl curvatures and auxiliaries to zero after this algebraic reduction. Because no curvature commutator is used, that specialization commutes with the reduction. The pole expansion has the same $`\rho>0`$ domain as the input.

The complete retained triplet was also re-collected after exchanging $`i,j`$; its difference is exactly zero. The two-form identity (CTF-10b) passes 625 integer component checks, and 36 exact spinor/SU(2) kernels check the identical-fermion zeros following from (CTF-12). The Clifford reduction covers the tensor monomials. All four final polynomials pass an idempotence check: repeating the final metric, epsilon and two-form collection leaves every rational coefficient unchanged.

The [full superform proof](../../../../../../references/source_evidence/log/derivations/form-interface.md) separately resolves FORM-01 for a genuine linear multiplet, including its potential law and all BF current completions. The algebraic canonicalization here does not itself prove the actual curved LOG multiplet identities or the complete raw-scalar/vector comparison with the earlier minimal bosonic action; those claims require their own verification. It proves algebraic reductions of the specified input under the stated rules.

| Slot | Input monomials | After tensor collection | After Clifford reduction |
|---|---:|---:|---:|
| $`L_{\log}`$ | 59 | 59 | 59 |
| $`\varphi_{\log}`$ | 1,520 | 492 | 278 |
| $`N_{\log}`$ | 87,829 | 5,315 | 514 |
| $`E_{\log}`$ | 89,988 | 8,021 | 1,332 |

Detailed evidence: [array checks](../../../../../../references/source_evidence/log/results/gauged_full_fermionic_log/sources/canonical_two_fermi/array_checks.json), [Clifford identities](../../../../../../references/source_evidence/log/results/gauged_full_fermionic_log/sources/canonical_two_fermi/clifford_checks.json), and manifest.

## 5. Complete collected result

The subscripts $`n`$ label powers $`\rho^{-n}`$; superscripts $`(d)`$ label the number of **explicit** fermions before the outer projection. Every coefficient polynomial below is given in full. Consecutive displays under the same coefficient heading continue the same sum. The outer $`[\ ]_{\leq2}`$ implements (CTF-04) on the implicit fermions as well.

### 5.1 Triplet

```math
\boxed{L_{\log}^{ij}\big|_{\leq2}=\Big[\sum_{n=0}^{4}\rho^{-n}(\mathcal L_{n}^{(0)ij}+\mathcal L_{n}^{(2)ij})\Big]_{\leq2}}
\tag{CTF-L}
```

The absent coefficients are $`\mathcal L_{4}^{(0)ij}=0`$.

#### Triplet: $`n=0`$, explicit degree $`0`$

```math
\begin{aligned}
\mathcal L_{0}^{(0)ij}={}&\frac{16}{3}R(V){}^{a}{}^{b}{}^{i}{}^{j}T{}_{a}{}_{b}
\end{aligned}
\tag{CTF-L0F0}
```

#### Triplet: $`n=0`$, explicit degree $`2`$

```math
\begin{aligned}
\mathcal L_{0}^{(2)ij}={}&\frac{544i}{3}\overline{\chi{}^{i}}\chi{}^{j}
\end{aligned}
\tag{CTF-L0F2}
```

#### Triplet: $`n=1`$, explicit degree $`0`$

```math
\begin{aligned}
\mathcal L_{1}^{(0)ij}={}&24DY{}^{i}{}^{j} -R(V){}^{a}{}^{b}{}^{i}{}^{j}\widehat F{}_{a}{}_{b}\\
&+2\big(\Box^c Y{}^{i}{}^{j}\big) +16Y{}^{i}{}^{j}T^2
\end{aligned}
\tag{CTF-L1F0}
```

#### Triplet: $`n=1`$, explicit degree $`2`$

```math
\begin{aligned}
\mathcal L_{1}^{(2)ij}={}&\frac{4i}{3}T{}_{a}{}_{b}\overline{R(Q){}^{a}{}^{b}{}^{i}}\lambda{}^{j} +\frac{4i}{3}T{}_{a}{}_{b}\overline{R(Q){}^{a}{}^{b}{}^{j}}\lambda{}^{i}\\
&+8\overline{\chi{}^{i}}\gamma{}^{a}\big(\mathcal D_{a}\lambda{}^{j}\big) +8\overline{\chi{}^{j}}\gamma{}^{a}\big(\mathcal D_{a}\lambda{}^{i}\big)\\
&-8\overline{\big(\mathcal D^{a}\chi{}^{j}\big)}\gamma{}_{a}\lambda{}^{i} -8\overline{\big(\mathcal D^{a}\chi{}^{i}\big)}\gamma{}_{a}\lambda{}^{j}
\end{aligned}
\tag{CTF-L1F2}
```

#### Triplet: $`n=2`$, explicit degree $`0`$

```math
\begin{aligned}
\mathcal L_{2}^{(0)ij}={}&-2Y{}^{i}{}^{j}\big(\Box^c \rho\big) -2\big(\mathcal D^{a}Y{}^{i}{}^{j}\big)\big(\mathcal D_{a}\rho\big)
\end{aligned}
\tag{CTF-L2F0}
```

#### Triplet: $`n=2`$, explicit degree $`2`$

```math
\begin{aligned}
\mathcal L_{2}^{(2)ij}={}&-\frac{i}{4}\widehat F{}_{a}{}_{b}\overline{R(Q){}^{a}{}^{b}{}^{i}}\lambda{}^{j} -\frac{i}{4}\widehat F{}_{a}{}_{b}\overline{R(Q){}^{a}{}^{b}{}^{j}}\lambda{}^{i}\\
&+\frac{i}{2}\overline{\lambda{}^{j}}\big(\Box^c \lambda{}^{i}\big) +\frac{i}{2}\overline{\lambda{}^{i}}\big(\Box^c \lambda{}^{j}\big)\\
&+\frac{i}{2}\overline{\big(\mathcal D^{a}\lambda{}^{i}\big)}\big(\mathcal D_{a}\lambda{}^{j}\big) +\frac{i}{2}T{}^{d}{}^{e}\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\lambda{}^{i}}\gamma{}^{a}{}^{b}\big(\mathcal D^{c}\lambda{}^{j}\big)\\
&+\frac{i}{2}T{}^{d}{}^{e}\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\lambda{}^{j}}\gamma{}^{a}{}^{b}\big(\mathcal D^{c}\lambda{}^{i}\big) +4\big(\mathcal D^{b}T{}_{a}{}_{b}\big)\overline{\lambda{}^{i}}\gamma{}^{a}\lambda{}^{j}\\
&+4iD\overline{\lambda{}^{i}}\lambda{}^{j} -2i\widehat F{}_{a}{}_{b}\overline{\chi{}^{i}}\gamma{}^{a}{}^{b}\lambda{}^{j}\\
&-2i\widehat F{}_{a}{}_{b}\overline{\chi{}^{j}}\gamma{}^{a}{}^{b}\lambda{}^{i} -\frac{4i}{3}T^2\overline{\lambda{}^{i}}\lambda{}^{j}\\
&+2T{}^{b}{}^{c}T{}^{d}{}^{e}\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\lambda{}^{i}}\gamma{}^{a}\lambda{}^{j} +16iY{}^{i}{}^{j}\overline{\chi{}^{k}}\lambda{}_{k}
\end{aligned}
\tag{CTF-L2F2}
```

#### Triplet: $`n=3`$, explicit degree $`0`$

```math
\begin{aligned}
\mathcal L_{3}^{(0)ij}={}&-\frac{1}{2}Y{}^{i}{}^{j}\widehat F^2 +2Y{}^{i}{}^{j}Y^2\\
&+Y{}^{i}{}^{j}\big(\mathcal D^{a}\rho\big)\big(\mathcal D_{a}\rho\big)
\end{aligned}
\tag{CTF-L3F0}
```

#### Triplet: $`n=3`$, explicit degree $`2`$

```math
\begin{aligned}
\mathcal L_{3}^{(2)ij}={}&-\frac{i}{16}\widehat F{}^{c}{}^{d}\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\lambda{}^{i}}\gamma{}^{a}{}^{b}\big(\mathcal D^{e}\lambda{}^{j}\big) -\frac{i}{16}\widehat F{}^{c}{}^{d}\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\lambda{}^{j}}\gamma{}^{a}{}^{b}\big(\mathcal D^{e}\lambda{}^{i}\big)\\
&-\frac{1}{4}\widehat F{}_{a}{}^{b}\overline{\lambda{}^{i}}\gamma{}^{a}\big(\mathcal D_{b}\lambda{}^{j}\big) -\frac{1}{4}\widehat F{}_{a}{}^{b}\overline{\lambda{}^{j}}\gamma{}^{a}\big(\mathcal D_{b}\lambda{}^{i}\big)\\
&-\frac{1}{2}\big(\mathcal D^{b}\widehat F{}_{a}{}_{b}\big)\overline{\lambda{}^{i}}\gamma{}^{a}\lambda{}^{j} -Y{}^{i}{}^{j}\overline{\lambda{}^{k}}\gamma{}^{a}\big(\mathcal D_{a}\lambda{}_{k}\big)\\
&-\frac{1}{2}Y{}^{i}{}^{k}\overline{\lambda{}^{j}}\gamma{}^{a}\big(\mathcal D_{a}\lambda{}_{k}\big) -\frac{1}{2}Y{}^{j}{}^{k}\overline{\lambda{}^{i}}\gamma{}^{a}\big(\mathcal D_{a}\lambda{}_{k}\big)\\
&-\frac{1}{2}\big(\mathcal D^{a}Y{}^{j}{}^{k}\big)\overline{\lambda{}^{i}}\gamma{}_{a}\lambda{}_{k} -\frac{1}{2}\big(\mathcal D^{a}Y{}^{i}{}^{k}\big)\overline{\lambda{}^{j}}\gamma{}_{a}\lambda{}_{k}\\
&-\frac{i}{2}\big(\Box^c \rho\big)\overline{\lambda{}^{i}}\lambda{}^{j} -\frac{3i}{4}\big(\mathcal D_{a}\rho\big)\overline{\lambda{}^{i}}\big(\mathcal D^{a}\lambda{}^{j}\big)\\
&-\frac{3i}{4}\big(\mathcal D_{a}\rho\big)\overline{\lambda{}^{j}}\big(\mathcal D^{a}\lambda{}^{i}\big) +\frac{i}{4}\big(\mathcal D_{b}\rho\big)\overline{\lambda{}^{i}}\gamma{}^{a}{}^{b}\big(\mathcal D_{a}\lambda{}^{j}\big)\\
&+\frac{i}{4}\big(\mathcal D_{b}\rho\big)\overline{\lambda{}^{j}}\gamma{}^{a}{}^{b}\big(\mathcal D_{a}\lambda{}^{i}\big) +2\big(\mathcal D^{b}\rho\big)T{}_{a}{}_{b}\overline{\lambda{}^{i}}\gamma{}^{a}\lambda{}^{j}\\
&+i\widehat F{}^{a}{}^{b}T{}_{a}{}_{b}\overline{\lambda{}^{i}}\lambda{}^{j} -\frac{3}{2}\widehat F{}^{b}{}^{c}T{}^{d}{}^{e}\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\lambda{}^{i}}\gamma{}^{a}\lambda{}^{j}\\
&-iY{}^{i}{}^{j}T{}_{a}{}_{b}\overline{\lambda{}^{k}}\gamma{}^{a}{}^{b}\lambda{}_{k}
\end{aligned}
\tag{CTF-L3F2}
```

#### Triplet: $`n=4`$, explicit degree $`2`$

```math
\begin{aligned}
\mathcal L_{4}^{(2)ij}={}&\frac{3i}{8}\big(\mathcal D^{a}\rho\big)\big(\mathcal D_{a}\rho\big)\overline{\lambda{}^{i}}\lambda{}^{j} +\frac{3}{4}Y{}^{i}{}^{k}\big(\mathcal D_{a}\rho\big)\overline{\lambda{}^{j}}\gamma{}^{a}\lambda{}_{k}\\
&+\frac{3}{4}Y{}^{j}{}^{k}\big(\mathcal D_{a}\rho\big)\overline{\lambda{}^{i}}\gamma{}^{a}\lambda{}_{k} +\frac{3}{4}\widehat F{}_{a}{}^{b}\big(\mathcal D_{b}\rho\big)\overline{\lambda{}^{i}}\gamma{}^{a}\lambda{}^{j}\\
&-\frac{3i}{16}\widehat F^2\overline{\lambda{}^{i}}\lambda{}^{j} +\frac{3}{32}\widehat F{}^{b}{}^{c}\widehat F{}^{d}{}^{e}\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\lambda{}^{i}}\gamma{}^{a}\lambda{}^{j}\\
&+\frac{3i}{8}Y{}^{i}{}^{j}\widehat F{}_{a}{}_{b}\overline{\lambda{}^{k}}\gamma{}^{a}{}^{b}\lambda{}_{k} +\frac{3i}{2}Y{}^{i}{}^{j}Y{}^{k}{}^{l}\overline{\lambda{}_{k}}\lambda{}_{l}\\
&+\frac{3i}{4}Y^2\overline{\lambda{}^{i}}\lambda{}^{j}
\end{aligned}
\tag{CTF-L4F2}
```

### 5.2 Spinor

```math
\boxed{\varphi_{\log}^{i}\big|_{\leq2}=\Big[\sum_{n=0}^{4}\rho^{-n}\mathcal P_{n}^{(1)i}\Big]_{\leq2}}
\tag{CTF-phi}
```

#### Spinor: $`n=0`$, explicit degree $`1`$

```math
\begin{aligned}
\mathcal P_{0}^{(1)i}={}&\frac{8}{3}R(V){}^{a}{}^{b}{}^{i}{}^{j}\gamma{}_{a}{}_{b}\chi{}_{j} -\frac{56}{9}T{}_{a}{}_{b}T{}_{c}{}_{d}\gamma{}^{c}{}^{d}R(Q){}^{a}{}^{b}{}^{i}\\
&+\frac{2464}{9}T^2\chi{}^{i} +5iT{}_{b}{}_{c}\gamma{}_{a}\big(\mathcal D^{a}R(Q){}^{b}{}^{c}{}^{i}\big)\\
&+2iT{}^{c}{}^{d}T{}^{e}{}^{f}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\gamma{}_{a}R(Q){}^{a}{}^{b}{}^{i} +\frac{16}{3}T{}_{b}{}^{d}T{}_{c}{}_{d}\gamma{}_{a}{}^{c}R(Q){}^{a}{}^{b}{}^{i}\\
&-\frac{8}{3}T^2\gamma{}_{a}{}_{b}R(Q){}^{a}{}^{b}{}^{i} +\frac{16}{3}T{}_{a}{}_{c}T{}_{b}{}_{d}\gamma{}^{c}{}^{d}R(Q){}^{a}{}^{b}{}^{i}\\
&+32iT{}^{b}{}^{c}T{}^{d}{}^{e}\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\gamma{}^{a}\chi{}^{i} +\frac{1}{2}T{}^{d}{}^{e}\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\big(\mathcal D^{a}R(Q){}^{b}{}^{c}{}^{i}\big)\\
&+\frac{1}{2}T{}^{e}{}^{f}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\gamma{}^{c}{}^{d}\big(\mathcal D^{a}R(Q){}_{a}{}^{b}{}^{i}\big) +\frac{1}{2}T{}_{a}{}^{f}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\gamma{}^{d}{}^{e}\big(\mathcal D^{a}R(Q){}^{b}{}^{c}{}^{i}\big)\\
&+T{}_{b}{}^{f}\epsilon{}_{a}{}_{c}{}_{d}{}_{e}{}_{f}\gamma{}^{d}{}^{e}\big(\mathcal D^{a}R(Q){}^{b}{}^{c}{}^{i}\big) +2iT{}_{b}{}_{c}\gamma{}^{c}\big(\mathcal D^{a}R(Q){}_{a}{}^{b}{}^{i}\big)\\
&+2iT{}_{a}{}_{c}\gamma{}_{b}\big(\mathcal D^{a}R(Q){}^{b}{}^{c}{}^{i}\big) -16T{}^{d}{}^{e}\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\gamma{}^{b}{}^{c}\big(\mathcal D^{a}\chi{}^{i}\big)\\
&-\frac{128i}{3}T{}_{a}{}_{b}\gamma{}^{b}\big(\mathcal D^{a}\chi{}^{i}\big) -\frac{16}{3}D\chi{}^{i}\\
&-\frac{56}{3}\big(\mathcal D^{c}T{}^{d}{}^{e}\big)\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\gamma{}^{a}{}^{b}\chi{}^{i} +\frac{352i}{3}\big(\mathcal D^{b}T{}_{a}{}_{b}\big)\gamma{}^{a}\chi{}^{i}\\
&-8\big(\Box^c \chi{}^{i}\big)
\end{aligned}
\tag{CTF-phi0F1}
```

#### Spinor: $`n=1`$, explicit degree $`1`$

```math
\begin{aligned}
\mathcal P_{1}^{(1)i}={}&8iD\gamma{}^{a}\big(\mathcal D_{a}\lambda{}^{i}\big) -32iY{}^{i}{}^{j}\gamma{}_{a}\big(\mathcal D^{a}\chi{}_{j}\big)\\
&-iR(V){}^{a}{}^{b}{}^{i}{}^{j}\gamma{}_{a}\big(\mathcal D_{b}\lambda{}_{j}\big) -\frac{2i}{3}R(V){}^{a}{}^{b}{}^{i}{}^{j}T{}^{d}{}^{e}\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\gamma{}^{c}\lambda{}_{j}\\
&-\frac{4}{3}R(V){}^{a}{}^{b}{}^{i}{}^{j}T{}_{b}{}_{c}\gamma{}_{a}{}^{c}\lambda{}_{j} -\frac{8}{3}R(V){}^{a}{}^{b}{}^{i}{}^{j}T{}_{a}{}_{b}\lambda{}_{j}\\
&+\frac{2}{3}\widehat F{}_{a}{}_{b}T{}_{c}{}_{d}\gamma{}^{c}{}^{d}R(Q){}^{a}{}^{b}{}^{i} -48\widehat F{}^{a}{}^{b}T{}_{a}{}_{b}\chi{}^{i}\\
&-\frac{15i}{16}\widehat F{}_{b}{}_{c}\gamma{}_{a}\big(\mathcal D^{a}R(Q){}^{b}{}^{c}{}^{i}\big) -i\widehat F{}^{d}{}^{e}T{}_{a}{}^{f}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\gamma{}^{c}R(Q){}^{a}{}^{b}{}^{i}\\
&+i\widehat F{}^{d}{}^{e}T{}_{d}{}^{f}\epsilon{}_{a}{}_{b}{}_{c}{}_{e}{}_{f}\gamma{}^{c}R(Q){}^{a}{}^{b}{}^{i} +\frac{7}{6}\widehat F{}_{c}{}_{d}T{}_{a}{}_{b}\gamma{}^{c}{}^{d}R(Q){}^{a}{}^{b}{}^{i}\\
&-2\widehat F{}_{c}{}^{d}T{}_{b}{}_{d}\gamma{}_{a}{}^{c}R(Q){}^{a}{}^{b}{}^{i} +\frac{1}{2}\widehat F{}^{c}{}^{d}T{}_{c}{}_{d}\gamma{}_{a}{}_{b}R(Q){}^{a}{}^{b}{}^{i}\\
&-\frac{i}{2}\widehat F{}_{a}{}^{d}T{}^{e}{}^{f}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\gamma{}^{c}R(Q){}^{a}{}^{b}{}^{i} -\widehat F{}_{a}{}_{c}T{}_{b}{}_{d}\gamma{}^{c}{}^{d}R(Q){}^{a}{}^{b}{}^{i}\\
&+\widehat F{}_{b}{}^{d}T{}_{c}{}_{d}\gamma{}_{a}{}^{c}R(Q){}^{a}{}^{b}{}^{i} -\widehat F{}_{a}{}^{c}T{}_{b}{}_{c}R(Q){}^{a}{}^{b}{}^{i}\\
&-24i\widehat F{}^{b}{}^{c}T{}^{d}{}^{e}\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\gamma{}^{a}\chi{}^{i} -\frac{3}{32}\widehat F{}^{d}{}^{e}\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\big(\mathcal D^{a}R(Q){}^{b}{}^{c}{}^{i}\big)\\
&-\frac{3}{32}\widehat F{}^{e}{}^{f}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\gamma{}^{c}{}^{d}\big(\mathcal D^{a}R(Q){}_{a}{}^{b}{}^{i}\big) -\frac{3}{32}\widehat F{}_{a}{}^{f}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\gamma{}^{d}{}^{e}\big(\mathcal D^{a}R(Q){}^{b}{}^{c}{}^{i}\big)\\
&-\frac{3}{16}\widehat F{}_{b}{}^{f}\epsilon{}_{a}{}_{c}{}_{d}{}_{e}{}_{f}\gamma{}^{d}{}^{e}\big(\mathcal D^{a}R(Q){}^{b}{}^{c}{}^{i}\big) -\frac{3i}{8}\widehat F{}_{b}{}_{c}\gamma{}^{c}\big(\mathcal D^{a}R(Q){}_{a}{}^{b}{}^{i}\big)\\
&-\frac{3i}{8}\widehat F{}_{a}{}_{c}\gamma{}_{b}\big(\mathcal D^{a}R(Q){}^{b}{}^{c}{}^{i}\big) +2\widehat F{}^{d}{}^{e}\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\gamma{}^{b}{}^{c}\big(\mathcal D^{a}\chi{}^{i}\big)\\
&+i\gamma{}^{a}\big(\Box^c \mathcal D_{a}\lambda{}^{i}\big) -2\big(\mathcal D_{c}T{}_{a}{}_{b}\big)\gamma{}^{a}{}^{b}\big(\mathcal D^{c}\lambda{}^{i}\big)\\
&-2T{}_{a}{}_{b}\gamma{}^{a}{}^{b}\big(\Box^c \lambda{}^{i}\big) +4i\big(\mathcal D^{c}T{}^{d}{}^{e}\big)\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\gamma{}^{a}\big(\mathcal D^{b}\lambda{}^{i}\big)\\
&-4\big(\mathcal D_{a}T{}_{b}{}_{c}\big)\gamma{}^{a}{}^{b}\big(\mathcal D^{c}\lambda{}^{i}\big) -4\big(\mathcal D^{c}T{}_{b}{}_{c}\big)\gamma{}^{a}{}^{b}\big(\mathcal D_{a}\lambda{}^{i}\big)\\
&+8\big(\mathcal D^{b}T{}_{a}{}_{b}\big)\big(\mathcal D^{a}\lambda{}^{i}\big) -\frac{4i}{3}T{}^{d}{}^{e}\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\gamma{}^{a}\big(\mathcal D^{b}\mathcal D^{c}\lambda{}^{i}\big)\\
&-\frac{8}{3}T{}_{b}{}_{c}\gamma{}^{a}{}^{b}\big(\mathcal D_{a}\mathcal D^{c}\lambda{}^{i}\big) -\frac{16}{3}T{}_{b}{}_{c}\gamma{}^{a}{}^{b}\big(\mathcal D^{c}\mathcal D_{a}\lambda{}^{i}\big)
\end{aligned}
\tag{CTF-phi1F1-1}
```

```math
\begin{aligned}
&-\frac{16}{3}T{}_{a}{}_{b}\big(\mathcal D^{a}\mathcal D^{b}\lambda{}^{i}\big) -4T{}^{a}{}^{b}\big(\mathcal D^{c}T{}^{d}{}^{e}\big)\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\lambda{}^{i}\\
&-\frac{16}{9}T{}^{c}{}^{d}\big(\mathcal D_{c}T{}^{e}{}^{f}\big)\epsilon{}_{a}{}_{b}{}_{d}{}_{e}{}_{f}\gamma{}^{a}{}^{b}\lambda{}^{i} +\frac{16}{3}T{}^{c}{}^{d}\big(\mathcal D^{e}T{}_{c}{}^{f}\big)\epsilon{}_{a}{}_{b}{}_{d}{}_{e}{}_{f}\gamma{}^{a}{}^{b}\lambda{}^{i}\\
&-16iT{}^{b}{}^{c}\big(\mathcal D_{b}T{}_{a}{}_{c}\big)\gamma{}^{a}\lambda{}^{i} +\frac{40i}{3}T{}^{b}{}^{c}\big(\mathcal D_{a}T{}_{b}{}_{c}\big)\gamma{}^{a}\lambda{}^{i}\\
&+\frac{8}{9}T{}^{c}{}^{d}\big(\mathcal D^{e}T{}_{e}{}^{f}\big)\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{f}\gamma{}^{a}{}^{b}\lambda{}^{i} +16iT{}_{a}{}^{b}\big(\mathcal D^{c}T{}_{b}{}_{c}\big)\gamma{}^{a}\lambda{}^{i}\\
&-16i\big(\mathcal D^{a}Y{}^{i}{}^{j}\big)\gamma{}_{a}\chi{}_{j} +\frac{1}{18}\big(\mathcal D^{a}R(V){}^{b}{}^{c}{}^{i}{}^{j}\big)\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\gamma{}^{d}{}^{e}\lambda{}_{j}\\
&+\frac{16}{3}\big(\mathcal D^{c}\mathcal D_{a}T{}_{b}{}_{c}\big)\gamma{}^{a}{}^{b}\lambda{}^{i} +\frac{8}{3}\big(\mathcal D_{a}\mathcal D^{c}T{}_{b}{}_{c}\big)\gamma{}^{a}{}^{b}\lambda{}^{i}\\
&-\frac{4i}{3}\big(\mathcal D^{b}\mathcal D^{c}T{}^{d}{}^{e}\big)\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\gamma{}^{a}\lambda{}^{i} -\frac{4}{9}T{}^{c}{}^{d}\big(\mathcal D_{a}T{}^{e}{}^{f}\big)\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\gamma{}^{a}{}^{b}\lambda{}^{i}\\
&-4T{}^{b}{}^{c}T{}^{d}{}^{e}\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\big(\mathcal D^{a}\lambda{}^{i}\big) -32iT{}_{a}{}^{c}T{}_{b}{}_{c}\gamma{}^{a}\big(\mathcal D^{b}\lambda{}^{i}\big)\\
&+\frac{40i}{3}T^2\gamma{}^{a}\big(\mathcal D_{a}\lambda{}^{i}\big) +96i\big(\mathcal D^{b}\rho\big)T{}_{a}{}_{b}\gamma{}^{a}\chi{}^{i}\\
&-48T{}_{a}{}_{b}T^2\gamma{}^{a}{}^{b}\lambda{}^{i} +192T{}_{a}{}^{c}T{}_{b}{}^{d}T{}_{c}{}_{d}\gamma{}^{a}{}^{b}\lambda{}^{i}\\
&+\frac{8}{3}T{}_{a}{}^{c}\big(\mathcal D^{d}T{}^{e}{}^{f}\big)\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\gamma{}^{a}{}^{b}\lambda{}^{i} +\frac{1744i}{27}T{}_{a}{}^{b}T{}^{c}{}^{d}T{}^{e}{}^{f}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\gamma{}^{a}\lambda{}^{i}\\
&+\frac{2i}{3}\big(\mathcal D_{a}Y{}^{i}{}_{j}\big)\gamma{}_{b}R(Q){}^{a}{}^{b}{}^{j} +\frac{i}{3}Y{}^{i}{}_{j}\gamma{}_{b}\big(\mathcal D^{a}R(Q){}_{a}{}^{b}{}^{j}\big)\\
&+\frac{11i}{36}Y{}^{i}{}_{j}T{}^{d}{}^{e}\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\gamma{}^{c}R(Q){}^{a}{}^{b}{}^{j} +\frac{41}{18}Y{}^{i}{}_{j}T{}_{a}{}_{b}R(Q){}^{a}{}^{b}{}^{j}\\
&-Y{}^{i}{}_{j}T{}_{b}{}_{c}\gamma{}_{a}{}^{c}R(Q){}^{a}{}^{b}{}^{j} -\frac{i}{3}R(M){}^{a}{}^{b}{}_{a}{}^{c}T{}^{e}{}^{f}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\gamma{}^{d}\lambda{}^{i}\\
&-\frac{i}{3}R(M){}^{a}{}^{b}{}^{c}{}^{d}T{}_{c}{}^{f}\epsilon{}_{a}{}_{b}{}_{d}{}_{e}{}_{f}\gamma{}^{e}\lambda{}^{i} -\frac{1}{6}R(M){}^{a}{}^{b}{}_{a}{}_{b}T{}_{c}{}_{d}\gamma{}^{c}{}^{d}\lambda{}^{i}\\
&+\frac{2}{3}R(M){}^{a}{}^{b}{}_{a}{}^{c}T{}_{c}{}_{d}\gamma{}_{b}{}^{d}\lambda{}^{i} -\frac{1}{6}R(M){}^{a}{}^{b}{}^{c}{}^{d}T{}_{c}{}_{d}\gamma{}_{a}{}_{b}\lambda{}^{i}\\
&+\frac{i}{3}R(M){}^{a}{}^{b}{}^{c}{}^{d}T{}_{a}{}^{f}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\gamma{}^{e}\lambda{}^{i} +\frac{2}{3}R(M){}^{a}{}^{b}{}_{a}{}^{c}T{}_{b}{}_{d}\gamma{}_{c}{}^{d}\lambda{}^{i}\\
&-\frac{2}{3}R(M){}^{a}{}^{b}{}^{c}{}^{d}T{}_{b}{}_{d}\gamma{}_{a}{}_{c}\lambda{}^{i} -\frac{2}{3}R(M){}^{a}{}^{b}{}_{a}{}^{c}T{}_{b}{}_{c}\lambda{}^{i}
\end{aligned}
\tag{CTF-phi1F1-2}
```

```math
\begin{aligned}
&-\frac{1}{6}R(M){}^{a}{}^{b}{}^{c}{}^{d}T{}_{a}{}_{b}\gamma{}_{c}{}_{d}\lambda{}^{i} -\frac{4i}{3}\big(\mathcal D_{c}\rho\big)T{}_{a}{}_{b}\gamma{}^{c}R(Q){}^{a}{}^{b}{}^{i}\\
&-2\big(\mathcal D^{c}\widehat F{}^{d}{}^{e}\big)\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\gamma{}^{a}{}^{b}\chi{}^{i} -8i\big(\mathcal D^{b}\widehat F{}_{a}{}_{b}\big)\gamma{}^{a}\chi{}^{i}\\
&+8\big(\mathcal D_{a}\mathcal D_{b}\rho\big)\gamma{}^{a}{}^{b}\chi{}^{i} -8\big(\Box^c \rho\big)\chi{}^{i}\\
&-8\big(\mathcal D_{b}\rho\big)\gamma{}_{a}{}^{b}\big(\mathcal D^{a}\chi{}^{i}\big) +4i\big(\mathcal D^{a}D\big)\gamma{}_{a}\lambda{}^{i}\\
&+2\big(\Box^c T{}_{a}{}_{b}\big)\gamma{}^{a}{}^{b}\lambda{}^{i} +\frac{8}{3}T{}^{c}{}^{d}\big(\mathcal D^{e}T{}_{a}{}^{f}\big)\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\gamma{}^{a}{}^{b}\lambda{}^{i}
\end{aligned}
\tag{CTF-phi1F1-3}
```

#### Spinor: $`n=2`$, explicit degree $`1`$

```math
\begin{aligned}
\mathcal P_{2}^{(1)i}={}&-8DY{}^{i}{}^{j}\lambda{}_{j} +\frac{1}{2}R(V){}^{a}{}^{b}{}^{i}{}^{j}\widehat F{}_{a}{}_{b}\lambda{}_{j}\\
&-\big(\Box^c Y{}^{i}{}^{j}\big)\lambda{}_{j} +\frac{8}{3}Y{}^{i}{}^{j}T^2\lambda{}_{j}\\
&-i\big(\Box^c \rho\big)\gamma{}^{a}\big(\mathcal D_{a}\lambda{}^{i}\big) -\big(\Box^c \rho\big)T{}_{a}{}_{b}\gamma{}^{a}{}^{b}\lambda{}^{i}\\
&-Y{}^{i}{}^{j}\big(\Box^c \lambda{}_{j}\big) -Y{}^{i}{}^{j}\big(\mathcal D^{c}T{}^{d}{}^{e}\big)\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\gamma{}^{a}{}^{b}\lambda{}_{j}\\
&+8iY{}^{i}{}^{j}\big(\mathcal D^{b}T{}_{a}{}_{b}\big)\gamma{}^{a}\lambda{}_{j} -2Y{}^{i}{}^{j}T{}^{d}{}^{e}\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\gamma{}^{a}{}^{b}\big(\mathcal D^{c}\lambda{}_{j}\big)\\
&+16iY{}^{i}{}^{j}\big(\mathcal D_{a}\rho\big)\gamma{}^{a}\chi{}_{j} +4iY{}^{i}{}^{j}T{}^{b}{}^{c}T{}^{d}{}^{e}\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\gamma{}^{a}\lambda{}_{j}\\
&+\frac{2i}{3}Y{}^{i}{}_{j}\big(\mathcal D_{b}\rho\big)\gamma{}_{a}R(Q){}^{a}{}^{b}{}^{j} -\big(\mathcal D^{a}Y{}^{i}{}^{j}\big)\big(\mathcal D_{a}\lambda{}_{j}\big)\\
&-\big(\mathcal D^{a}Y{}^{i}{}^{j}\big)T{}^{d}{}^{e}\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\gamma{}^{b}{}^{c}\lambda{}_{j} -i\big(\mathcal D_{b}\rho\big)\gamma{}^{a}\big(\mathcal D^{b}\mathcal D_{a}\lambda{}^{i}\big)\\
&+4\big(\mathcal D^{a}\rho\big)\big(\mathcal D_{a}\rho\big)\chi{}^{i} -2i\big(\mathcal D^{c}\rho\big)T{}^{d}{}^{e}\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\gamma{}^{a}\big(\mathcal D^{b}\lambda{}^{i}\big)\\
&+2\big(\mathcal D_{c}\rho\big)T{}_{a}{}_{b}\gamma{}^{a}{}^{b}\big(\mathcal D^{c}\lambda{}^{i}\big) +4\big(\mathcal D_{a}\rho\big)T{}_{b}{}_{c}\gamma{}^{a}{}^{b}\big(\mathcal D^{c}\lambda{}^{i}\big)\\
&+4\big(\mathcal D^{c}\rho\big)T{}_{b}{}_{c}\gamma{}^{a}{}^{b}\big(\mathcal D_{a}\lambda{}^{i}\big) -\big(\mathcal D^{c}\rho\big)\big(\mathcal D_{c}T{}_{a}{}_{b}\big)\gamma{}^{a}{}^{b}\lambda{}^{i}\\
&+2\big(\mathcal D^{c}\rho\big)\big(\mathcal D_{a}T{}_{b}{}_{c}\big)\gamma{}^{a}{}^{b}\lambda{}^{i} -4\big(\mathcal D_{a}\rho\big)\big(\mathcal D^{c}T{}_{b}{}_{c}\big)\gamma{}^{a}{}^{b}\lambda{}^{i}\\
&-4\big(\mathcal D^{a}\rho\big)\big(\mathcal D^{b}T{}_{a}{}_{b}\big)\lambda{}^{i} -i\big(\mathcal D^{b}\rho\big)\big(\mathcal D^{c}T{}^{d}{}^{e}\big)\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\gamma{}^{a}\lambda{}^{i}\\
&+2\big(\mathcal D^{a}\rho\big)T{}^{b}{}^{c}T{}^{d}{}^{e}\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\lambda{}^{i} +16i\big(\mathcal D^{b}\rho\big)T{}_{a}{}^{c}T{}_{b}{}_{c}\gamma{}^{a}\lambda{}^{i}\\
&-\frac{20i}{3}\big(\mathcal D_{a}\rho\big)T^2\gamma{}^{a}\lambda{}^{i} +\frac{i}{16}R(M){}^{a}{}^{b}{}_{a}{}^{c}\widehat F{}^{e}{}^{f}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\gamma{}^{d}\lambda{}^{i}\\
&+\frac{i}{16}R(M){}^{a}{}^{b}{}^{c}{}^{d}\widehat F{}_{c}{}^{f}\epsilon{}_{a}{}_{b}{}_{d}{}_{e}{}_{f}\gamma{}^{e}\lambda{}^{i} +\frac{1}{32}R(M){}^{a}{}^{b}{}_{a}{}_{b}\widehat F{}_{c}{}_{d}\gamma{}^{c}{}^{d}\lambda{}^{i}\\
&-\frac{1}{8}R(M){}^{a}{}^{b}{}_{a}{}^{c}\widehat F{}_{c}{}_{d}\gamma{}_{b}{}^{d}\lambda{}^{i} +\frac{1}{32}R(M){}^{a}{}^{b}{}^{c}{}^{d}\widehat F{}_{c}{}_{d}\gamma{}_{a}{}_{b}\lambda{}^{i}\\
&-\frac{i}{16}R(M){}^{a}{}^{b}{}^{c}{}^{d}\widehat F{}_{a}{}^{f}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\gamma{}^{e}\lambda{}^{i} -\frac{1}{8}R(M){}^{a}{}^{b}{}_{a}{}^{c}\widehat F{}_{b}{}_{d}\gamma{}_{c}{}^{d}\lambda{}^{i}
\end{aligned}
\tag{CTF-phi2F1-1}
```

```math
\begin{aligned}
&+\frac{1}{8}R(M){}^{a}{}^{b}{}^{c}{}^{d}\widehat F{}_{b}{}_{d}\gamma{}_{a}{}_{c}\lambda{}^{i} +\frac{1}{8}R(M){}^{a}{}^{b}{}_{a}{}^{c}\widehat F{}_{b}{}_{c}\lambda{}^{i}\\
&+\frac{1}{32}R(M){}^{a}{}^{b}{}^{c}{}^{d}\widehat F{}_{a}{}_{b}\gamma{}_{c}{}_{d}\lambda{}^{i} +\frac{20}{3}\widehat F{}_{a}{}_{b}T^2\gamma{}^{a}{}^{b}\lambda{}^{i}\\
&-32\widehat F{}_{a}{}^{c}T{}_{b}{}^{d}T{}_{c}{}_{d}\gamma{}^{a}{}^{b}\lambda{}^{i} +4\widehat F{}^{c}{}^{d}T{}_{a}{}_{b}T{}_{c}{}_{d}\gamma{}^{a}{}^{b}\lambda{}^{i}\\
&-8\widehat F{}^{c}{}^{d}T{}_{a}{}_{c}T{}_{b}{}_{d}\gamma{}^{a}{}^{b}\lambda{}^{i} -\frac{1}{2}\widehat F{}^{a}{}^{b}\big(\mathcal D^{c}T{}^{d}{}^{e}\big)\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\lambda{}^{i}\\
&+\frac{5}{3}\widehat F{}^{c}{}^{d}\big(\mathcal D^{e}T{}_{e}{}^{f}\big)\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{f}\gamma{}^{a}{}^{b}\lambda{}^{i} -\frac{3}{2}\widehat F{}^{c}{}^{d}\big(\mathcal D^{e}T{}_{c}{}^{f}\big)\epsilon{}_{a}{}_{b}{}_{d}{}_{e}{}_{f}\gamma{}^{a}{}^{b}\lambda{}^{i}\\
&-i\widehat F{}^{b}{}^{c}\big(\mathcal D_{a}T{}_{b}{}_{c}\big)\gamma{}^{a}\lambda{}^{i} +\frac{17}{12}\widehat F{}^{c}{}^{d}\big(\mathcal D_{c}T{}^{e}{}^{f}\big)\epsilon{}_{a}{}_{b}{}_{d}{}_{e}{}_{f}\gamma{}^{a}{}^{b}\lambda{}^{i}\\
&+2i\widehat F{}^{b}{}^{c}\big(\mathcal D_{b}T{}_{a}{}_{c}\big)\gamma{}^{a}\lambda{}^{i} -\frac{1}{8}\widehat F{}_{a}{}_{b}\widehat F{}_{c}{}_{d}\gamma{}^{c}{}^{d}R(Q){}^{a}{}^{b}{}^{i}\\
&+\frac{i}{4}\widehat F{}_{a}{}_{b}\big(\mathcal D_{c}\rho\big)\gamma{}^{c}R(Q){}^{a}{}^{b}{}^{i} -\frac{1}{4}Y{}^{i}{}_{j}\widehat F{}_{a}{}_{b}R(Q){}^{a}{}^{b}{}^{j}\\
&+\frac{1}{4}\widehat F{}_{a}{}_{b}\gamma{}^{a}{}^{b}\big(\Box^c \lambda{}^{i}\big) -\frac{i}{2}\big(\mathcal D_{a}\rho\big)\gamma{}^{a}\big(\Box^c \lambda{}^{i}\big)\\
&+\frac{1}{4}\big(\Box^c \widehat F{}_{a}{}_{b}\big)\gamma{}^{a}{}^{b}\lambda{}^{i} -\frac{i}{2}\big(\Box^c \mathcal D_{a}\rho\big)\gamma{}^{a}\lambda{}^{i}\\
&+\frac{1}{6}\big(\mathcal D^{a}\widehat F{}^{b}{}^{c}\big)T{}^{d}{}^{e}\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\lambda{}^{i} +\big(\mathcal D^{c}\widehat F{}_{c}{}^{d}\big)T{}^{e}{}^{f}\epsilon{}_{a}{}_{b}{}_{d}{}_{e}{}_{f}\gamma{}^{a}{}^{b}\lambda{}^{i}\\
&+\frac{2}{3}\big(\mathcal D^{c}\widehat F{}^{d}{}^{e}\big)T{}_{d}{}^{f}\epsilon{}_{a}{}_{b}{}_{c}{}_{e}{}_{f}\gamma{}^{a}{}^{b}\lambda{}^{i} +2i\big(\mathcal D^{b}\widehat F{}_{b}{}^{c}\big)T{}_{a}{}_{c}\gamma{}^{a}\lambda{}^{i}\\
&+\frac{i}{3}\big(\mathcal D_{a}\widehat F{}^{b}{}^{c}\big)T{}_{b}{}_{c}\gamma{}^{a}\lambda{}^{i} +\frac{2}{3}\big(\mathcal D^{c}\widehat F{}^{d}{}^{e}\big)T{}_{c}{}^{f}\epsilon{}_{a}{}_{b}{}_{d}{}_{e}{}_{f}\gamma{}^{a}{}^{b}\lambda{}^{i}\\
&-\frac{8i}{3}\big(\mathcal D^{b}\widehat F{}_{a}{}^{c}\big)T{}_{b}{}_{c}\gamma{}^{a}\lambda{}^{i} +\frac{5i}{3}\big(\mathcal D^{b}\mathcal D^{c}\rho\big)T{}^{d}{}^{e}\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\gamma{}^{a}\lambda{}^{i}\\
&-\frac{2}{3}\big(\mathcal D_{a}\mathcal D^{c}\rho\big)T{}_{b}{}_{c}\gamma{}^{a}{}^{b}\lambda{}^{i} +\frac{8}{3}\big(\mathcal D^{c}\mathcal D_{a}\rho\big)T{}_{b}{}_{c}\gamma{}^{a}{}^{b}\lambda{}^{i}\\
&+\frac{8}{3}\big(\mathcal D^{a}\mathcal D^{b}\rho\big)T{}_{a}{}_{b}\lambda{}^{i} +2\big(\mathcal D_{a}\rho\big)T{}^{c}{}^{d}T{}^{e}{}^{f}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\gamma{}^{a}{}^{b}\lambda{}^{i}\\
&-\frac{1}{6}\widehat F{}_{a}{}^{c}\big(\mathcal D^{d}T{}^{e}{}^{f}\big)\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\gamma{}^{a}{}^{b}\lambda{}^{i} +\frac{1}{4}\big(\mathcal D^{c}\widehat F{}_{a}{}_{b}\big)\gamma{}^{a}{}^{b}\big(\mathcal D_{c}\lambda{}^{i}\big)\\
&-\frac{i}{2}\big(\mathcal D_{b}\mathcal D_{a}\rho\big)\gamma{}^{a}\big(\mathcal D^{b}\lambda{}^{i}\big) -\widehat F{}^{a}{}^{b}T{}^{d}{}^{e}\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\big(\mathcal D^{c}\lambda{}^{i}\big)
\end{aligned}
\tag{CTF-phi2F1-2}
```

```math
\begin{aligned}
&+\frac{1}{2}\widehat F{}^{c}{}^{d}T{}^{e}{}^{f}\epsilon{}_{a}{}_{b}{}_{d}{}_{e}{}_{f}\gamma{}^{a}{}^{b}\big(\mathcal D_{c}\lambda{}^{i}\big) -\frac{1}{3}\widehat F{}^{c}{}^{d}T{}_{c}{}^{f}\epsilon{}_{a}{}_{b}{}_{d}{}_{e}{}_{f}\gamma{}^{a}{}^{b}\big(\mathcal D^{e}\lambda{}^{i}\big)\\
&+4i\widehat F{}^{b}{}^{c}T{}_{a}{}_{c}\gamma{}^{a}\big(\mathcal D_{b}\lambda{}^{i}\big) -2i\widehat F{}^{b}{}^{c}T{}_{b}{}_{c}\gamma{}^{a}\big(\mathcal D_{a}\lambda{}^{i}\big)\\
&+\frac{1}{3}\widehat F{}^{c}{}^{d}T{}_{e}{}^{f}\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{f}\gamma{}^{a}{}^{b}\big(\mathcal D^{e}\lambda{}^{i}\big) -\widehat F{}_{a}{}^{c}T{}^{e}{}^{f}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\gamma{}^{a}{}^{b}\big(\mathcal D^{d}\lambda{}^{i}\big)\\
&-\big(\mathcal D^{c}\widehat F{}_{a}{}^{d}\big)T{}^{e}{}^{f}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\gamma{}^{a}{}^{b}\lambda{}^{i} +D\widehat F{}_{a}{}_{b}\gamma{}^{a}{}^{b}\lambda{}^{i}\\
&-4iD\big(\mathcal D_{a}\rho\big)\gamma{}^{a}\lambda{}^{i} +i\widehat F{}^{b}{}^{c}\widehat F{}^{d}{}^{e}\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\gamma{}^{a}\chi{}^{i}\\
&-\widehat F{}^{c}{}^{d}\big(\mathcal D^{e}\rho\big)\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\gamma{}^{a}{}^{b}\chi{}^{i} +4i\widehat F{}_{a}{}^{b}\big(\mathcal D_{b}\rho\big)\gamma{}^{a}\chi{}^{i}\\
&-4Y{}^{i}{}^{j}\widehat F{}_{a}{}_{b}\gamma{}^{a}{}^{b}\chi{}_{j} +\frac{i}{24}Y{}^{i}{}_{j}\widehat F{}^{d}{}^{e}\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\gamma{}^{c}R(Q){}^{a}{}^{b}{}^{j}\\
&+\frac{1}{6}Y{}^{i}{}_{j}\widehat F{}_{b}{}_{c}\gamma{}_{a}{}^{c}R(Q){}^{a}{}^{b}{}^{j} -8Y^2\chi{}^{i}\\
&+\frac{2}{3}\widehat F{}^{c}{}^{d}T{}_{a}{}^{f}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\gamma{}^{a}{}^{b}\big(\mathcal D^{e}\lambda{}^{i}\big) -\frac{1}{3}\widehat F{}^{c}{}^{d}\big(\mathcal D^{e}T{}_{a}{}^{f}\big)\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\gamma{}^{a}{}^{b}\lambda{}^{i}\\
&-\frac{1}{6}\widehat F{}^{c}{}^{d}\big(\mathcal D_{a}T{}^{e}{}^{f}\big)\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\gamma{}^{a}{}^{b}\lambda{}^{i}
\end{aligned}
\tag{CTF-phi2F1-3}
```

#### Spinor: $`n=3`$, explicit degree $`1`$

```math
\begin{aligned}
\mathcal P_{3}^{(1)i}={}&\frac{3}{2}Y{}^{i}{}^{j}\big(\Box^c \rho\big)\lambda{}_{j} +\frac{5}{2}\big(\mathcal D^{a}Y{}^{i}{}^{j}\big)\big(\mathcal D_{a}\rho\big)\lambda{}_{j}\\
&-\frac{i}{8}\widehat F^2\gamma{}^{a}\big(\mathcal D_{a}\lambda{}^{i}\big) -\frac{5}{4}T{}_{a}{}_{b}\widehat F^2\gamma{}^{a}{}^{b}\lambda{}^{i}\\
&+\frac{1}{4}Y{}^{i}{}^{j}\widehat F{}^{c}{}^{d}\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\gamma{}^{a}{}^{b}\big(\mathcal D^{e}\lambda{}_{j}\big) -3iY{}^{i}{}^{j}\widehat F{}^{b}{}^{c}T{}^{d}{}^{e}\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\gamma{}^{a}\lambda{}_{j}\\
&-2Y{}^{i}{}^{j}\widehat F{}^{a}{}^{b}T{}_{a}{}_{b}\lambda{}_{j} +iY^2\gamma{}^{a}\big(\mathcal D_{a}\lambda{}^{i}\big)\\
&-\frac{10}{9}T{}_{a}{}_{b}Y^2\gamma{}^{a}{}^{b}\lambda{}^{i} -iY{}^{i}{}^{j}Y{}_{j}{}^{k}\gamma{}^{a}\big(\mathcal D_{a}\lambda{}_{k}\big)\\
&-\frac{2}{9}Y{}^{i}{}^{j}Y{}_{j}{}^{k}T{}_{a}{}_{b}\gamma{}^{a}{}^{b}\lambda{}_{k} +\frac{3i}{4}\big(\mathcal D^{b}\rho\big)\big(\mathcal D_{b}\rho\big)\gamma{}^{a}\big(\mathcal D_{a}\lambda{}^{i}\big)\\
&+\frac{1}{2}\big(\mathcal D^{c}\rho\big)\big(\mathcal D_{c}\rho\big)T{}_{a}{}_{b}\gamma{}^{a}{}^{b}\lambda{}^{i} +2Y{}^{i}{}^{j}\big(\mathcal D_{a}\rho\big)\big(\mathcal D^{a}\lambda{}_{j}\big)\\
&+2Y{}^{i}{}^{j}\big(\mathcal D^{c}\rho\big)T{}^{d}{}^{e}\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\gamma{}^{a}{}^{b}\lambda{}_{j} +4iY{}^{i}{}^{j}\big(\mathcal D^{b}\rho\big)T{}_{a}{}_{b}\gamma{}^{a}\lambda{}_{j}\\
&+\frac{i}{2}\widehat F{}_{a}{}^{b}\widehat F{}_{b}{}^{c}\gamma{}^{a}\big(\mathcal D_{c}\lambda{}^{i}\big) +\frac{1}{16}\widehat F{}^{a}{}^{b}\widehat F{}^{c}{}^{d}\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\big(\mathcal D^{e}\lambda{}^{i}\big)\\
&-\frac{1}{2}\widehat F{}_{a}{}_{b}\big(\mathcal D_{c}\rho\big)\gamma{}^{a}{}^{b}\big(\mathcal D^{c}\lambda{}^{i}\big) +\frac{i}{4}\widehat F{}^{b}{}^{c}\big(\mathcal D^{e}\rho\big)\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\gamma{}^{a}\big(\mathcal D^{d}\lambda{}^{i}\big)\\
&-\frac{i}{8}\widehat F{}^{b}{}^{c}\big(\mathcal D_{a}\widehat F{}_{b}{}_{c}\big)\gamma{}^{a}\lambda{}^{i} +\frac{i}{4}\widehat F{}_{a}{}^{b}\big(\mathcal D^{c}\widehat F{}_{b}{}_{c}\big)\gamma{}^{a}\lambda{}^{i}\\
&+\frac{1}{8}\widehat F{}^{c}{}^{d}\big(\mathcal D^{e}\widehat F{}_{a}{}^{f}\big)\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\gamma{}^{a}{}^{b}\lambda{}^{i} -\frac{1}{16}\widehat F{}^{a}{}^{b}\big(\mathcal D^{c}\widehat F{}^{d}{}^{e}\big)\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\lambda{}^{i}\\
&+2i\widehat F{}^{b}{}^{c}\big(\mathcal D_{a}\rho\big)T{}_{b}{}_{c}\gamma{}^{a}\lambda{}^{i} -\frac{1}{3}\widehat F{}^{c}{}^{d}\big(\mathcal D^{e}\rho\big)T{}_{a}{}^{f}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\gamma{}^{a}{}^{b}\lambda{}^{i}\\
&+\widehat F{}^{a}{}^{b}\big(\mathcal D^{c}\rho\big)T{}^{d}{}^{e}\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\lambda{}^{i} -\frac{1}{4}\widehat F{}_{a}{}^{c}\big(\mathcal D_{b}\mathcal D_{c}\rho\big)\gamma{}^{a}{}^{b}\lambda{}^{i}\\
&-\frac{1}{8}\widehat F{}_{a}{}_{b}\big(\Box^c \rho\big)\gamma{}^{a}{}^{b}\lambda{}^{i} -\frac{i}{8}\widehat F{}^{b}{}^{c}\big(\mathcal D^{d}\mathcal D^{e}\rho\big)\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\gamma{}^{a}\lambda{}^{i}\\
&-\frac{3}{2}\widehat F{}_{a}{}_{b}\widehat F{}^{c}{}^{d}T{}_{c}{}_{d}\gamma{}^{a}{}^{b}\lambda{}^{i} +6\widehat F{}_{a}{}^{c}\widehat F{}_{c}{}^{d}T{}_{b}{}_{d}\gamma{}^{a}{}^{b}\lambda{}^{i}\\
&+\widehat F{}_{a}{}^{c}\widehat F{}_{b}{}^{d}T{}_{c}{}_{d}\gamma{}^{a}{}^{b}\lambda{}^{i} -4i\widehat F{}^{b}{}^{c}\big(\mathcal D_{b}\rho\big)T{}_{a}{}_{c}\gamma{}^{a}\lambda{}^{i}\\
&+\frac{5}{4}\widehat F{}^{c}{}^{d}\big(\mathcal D_{a}\rho\big)T{}^{e}{}^{f}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\gamma{}^{a}{}^{b}\lambda{}^{i} -\frac{5}{12}\widehat F{}^{c}{}^{d}\big(\mathcal D^{e}\rho\big)T{}_{e}{}^{f}\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{f}\gamma{}^{a}{}^{b}\lambda{}^{i}
\end{aligned}
\tag{CTF-phi3F1-1}
```

```math
\begin{aligned}
&+\frac{1}{8}\big(\mathcal D^{a}Y{}^{i}{}^{j}\big)\widehat F{}^{d}{}^{e}\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\gamma{}^{b}{}^{c}\lambda{}_{j} -\frac{1}{2}\widehat F{}^{a}{}^{b}\big(\mathcal D_{b}\rho\big)\big(\mathcal D_{a}\lambda{}^{i}\big)\\
&-\frac{1}{16}\widehat F{}^{c}{}^{d}\big(\mathcal D_{c}\widehat F{}^{e}{}^{f}\big)\epsilon{}_{a}{}_{b}{}_{d}{}_{e}{}_{f}\gamma{}^{a}{}^{b}\lambda{}^{i} -\frac{i}{4}\widehat F{}^{b}{}^{c}\big(\mathcal D_{b}\widehat F{}_{a}{}_{c}\big)\gamma{}^{a}\lambda{}^{i}\\
&-\frac{5}{4}\widehat F{}^{c}{}^{d}\big(\mathcal D_{c}\rho\big)T{}^{e}{}^{f}\epsilon{}_{a}{}_{b}{}_{d}{}_{e}{}_{f}\gamma{}^{a}{}^{b}\lambda{}^{i} -\frac{1}{4}\widehat F{}_{a}{}^{c}\big(\mathcal D_{c}\mathcal D_{b}\rho\big)\gamma{}^{a}{}^{b}\lambda{}^{i}\\
&-\frac{1}{4}\widehat F{}^{a}{}^{b}\big(\mathcal D_{a}\mathcal D_{b}\rho\big)\lambda{}^{i} +\frac{2}{3}\widehat F{}^{c}{}^{d}\big(\mathcal D^{e}\rho\big)T{}_{c}{}^{f}\epsilon{}_{a}{}_{b}{}_{d}{}_{e}{}_{f}\gamma{}^{a}{}^{b}\lambda{}^{i}\\
&-\frac{i}{2}\big(\mathcal D^{a}Y{}^{i}{}^{j}\big)\widehat F{}_{a}{}_{b}\gamma{}^{b}\lambda{}_{j} -\frac{1}{8}\widehat F{}^{c}{}^{d}\big(\mathcal D^{e}\widehat F{}_{e}{}^{f}\big)\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{f}\gamma{}^{a}{}^{b}\lambda{}^{i}\\
&-\frac{i}{2}Y{}^{i}{}^{j}\big(\mathcal D^{b}\widehat F{}_{a}{}_{b}\big)\gamma{}^{a}\lambda{}_{j} -\frac{3}{4}\big(\mathcal D^{c}\widehat F{}_{a}{}_{c}\big)\big(\mathcal D_{b}\rho\big)\gamma{}^{a}{}^{b}\lambda{}^{i}\\
&-\frac{1}{4}\big(\mathcal D^{a}\widehat F{}_{a}{}^{b}\big)\big(\mathcal D_{b}\rho\big)\lambda{}^{i} -Y{}^{i}{}^{j}\big(\mathcal D_{b}\rho\big)\gamma{}^{a}{}^{b}\big(\mathcal D_{a}\lambda{}_{j}\big)\\
&-\frac{1}{24}Y{}^{i}{}^{j}\big(\mathcal D^{c}\widehat F{}^{d}{}^{e}\big)\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\gamma{}^{a}{}^{b}\lambda{}_{j} -\frac{4i}{3}Y{}^{i}{}^{j}\big(\mathcal D^{a}Y{}_{j}{}^{k}\big)\gamma{}_{a}\lambda{}_{k}\\
&+\frac{1}{6}Y{}^{i}{}^{j}\big(\mathcal D_{a}\mathcal D_{b}\rho\big)\gamma{}^{a}{}^{b}\lambda{}_{j} +\frac{2i}{3}Y{}^{j}{}^{k}\big(\mathcal D^{a}Y{}_{j}{}_{k}\big)\gamma{}_{a}\lambda{}^{i}\\
&-\frac{1}{2}\big(\mathcal D^{a}Y{}^{i}{}^{j}\big)\big(\mathcal D_{b}\rho\big)\gamma{}_{a}{}^{b}\lambda{}_{j} +\frac{i}{3}Y{}^{j}{}^{k}\big(\mathcal D^{a}Y{}^{i}{}_{j}\big)\gamma{}_{a}\lambda{}_{k}\\
&+\frac{3i}{4}\big(\mathcal D_{a}\rho\big)\big(\Box^c \rho\big)\gamma{}^{a}\lambda{}^{i} +\frac{i}{2}\big(\mathcal D_{a}\rho\big)\big(\mathcal D_{b}\rho\big)\gamma{}^{a}\big(\mathcal D^{b}\lambda{}^{i}\big)\\
&-\frac{3}{8}\big(\mathcal D^{c}\widehat F{}_{a}{}_{b}\big)\big(\mathcal D_{c}\rho\big)\gamma{}^{a}{}^{b}\lambda{}^{i} +\frac{3i}{4}\big(\mathcal D^{b}\rho\big)\big(\mathcal D_{b}\mathcal D_{a}\rho\big)\gamma{}^{a}\lambda{}^{i}\\
&-6\big(\mathcal D_{a}\rho\big)\big(\mathcal D^{c}\rho\big)T{}_{b}{}_{c}\gamma{}^{a}{}^{b}\lambda{}^{i} -\frac{i}{8}\big(\mathcal D^{b}\widehat F{}^{c}{}^{d}\big)\big(\mathcal D^{e}\rho\big)\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\gamma{}^{a}\lambda{}^{i}\\
&-\frac{1}{4}\big(\mathcal D_{a}\widehat F{}_{b}{}^{c}\big)\big(\mathcal D_{c}\rho\big)\gamma{}^{a}{}^{b}\lambda{}^{i} -\frac{1}{8}\big(\mathcal D^{c}\rho\big)\big(\mathcal D^{d}\mathcal D^{e}\rho\big)\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\gamma{}^{a}{}^{b}\lambda{}^{i}\\
&-\frac{i}{4}\big(\mathcal D^{b}\rho\big)\big(\mathcal D_{a}\mathcal D_{b}\rho\big)\gamma{}^{a}\lambda{}^{i}
\end{aligned}
\tag{CTF-phi3F1-2}
```

#### Spinor: $`n=4`$, explicit degree $`1`$

```math
\begin{aligned}
\mathcal P_{4}^{(1)i}={}&\frac{3}{8}Y{}^{i}{}^{j}\widehat F^2\lambda{}_{j} -\frac{5}{2}Y{}^{i}{}^{j}Y^2\lambda{}_{j}\\
&-\frac{9}{4}Y{}^{i}{}^{j}\big(\mathcal D^{a}\rho\big)\big(\mathcal D_{a}\rho\big)\lambda{}_{j} +\frac{3}{16}\widehat F{}_{a}{}_{b}\big(\mathcal D^{c}\rho\big)\big(\mathcal D_{c}\rho\big)\gamma{}^{a}{}^{b}\lambda{}^{i}\\
&-\frac{3i}{8}\big(\mathcal D_{a}\rho\big)\big(\mathcal D^{b}\rho\big)\big(\mathcal D_{b}\rho\big)\gamma{}^{a}\lambda{}^{i} -\frac{3}{8}Y{}^{i}{}^{j}\widehat F{}^{c}{}^{d}\big(\mathcal D^{e}\rho\big)\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\gamma{}^{a}{}^{b}\lambda{}_{j}\\
&+2iY{}^{i}{}^{j}Y{}_{j}{}^{k}\big(\mathcal D_{a}\rho\big)\gamma{}^{a}\lambda{}_{k} -\frac{5i}{4}\big(\mathcal D_{a}\rho\big)Y^2\gamma{}^{a}\lambda{}^{i}\\
&-\frac{3}{16}\widehat F{}^{c}{}^{d}\widehat F{}^{e}{}^{f}\big(\mathcal D_{a}\rho\big)\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\gamma{}^{a}{}^{b}\lambda{}^{i} -\frac{3i}{4}\widehat F{}_{a}{}^{b}\widehat F{}_{b}{}^{c}\big(\mathcal D_{c}\rho\big)\gamma{}^{a}\lambda{}^{i}\\
&+\frac{3}{4}\widehat F{}_{a}{}^{c}\big(\mathcal D_{b}\rho\big)\big(\mathcal D_{c}\rho\big)\gamma{}^{a}{}^{b}\lambda{}^{i} +\frac{3}{32}\widehat F{}_{a}{}_{b}\widehat F^2\gamma{}^{a}{}^{b}\lambda{}^{i}\\
&+\frac{3i}{16}\big(\mathcal D_{a}\rho\big)\widehat F^2\gamma{}^{a}\lambda{}^{i} -\frac{3}{8}\widehat F{}_{a}{}^{c}\widehat F{}_{b}{}^{d}\widehat F{}_{c}{}_{d}\gamma{}^{a}{}^{b}\lambda{}^{i}\\
&-\frac{3i}{32}\widehat F{}_{a}{}^{b}\widehat F{}^{c}{}^{d}\widehat F{}^{e}{}^{f}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\gamma{}^{a}\lambda{}^{i} +\frac{3i}{16}Y{}^{i}{}^{j}\widehat F{}^{b}{}^{c}\widehat F{}^{d}{}^{e}\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\gamma{}^{a}\lambda{}_{j}\\
&-\frac{3}{32}\widehat F{}^{a}{}^{b}\widehat F{}^{c}{}^{d}\big(\mathcal D^{e}\rho\big)\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\lambda{}^{i} -2Y{}^{i}{}^{j}Y{}_{j}{}^{k}Y{}_{k}{}^{l}\lambda{}_{l}\\
&+\frac{3}{8}\widehat F{}_{a}{}_{b}Y^2\gamma{}^{a}{}^{b}\lambda{}^{i}
\end{aligned}
\tag{CTF-phi4F1}
```

### 5.3 Scalar

```math
\boxed{N_{\log}\big|_{\leq2}=\Big[\sum_{n=0}^{5}\rho^{-n}(\mathcal N_{n}^{(0)}+\mathcal N_{n}^{(2)})\Big]_{\leq2}}
\tag{CTF-N}
```

The absent coefficients are $`\mathcal N_{5}^{(0)}=0`$.

#### Scalar: $`n=0`$, explicit degree $`0`$

```math
\begin{aligned}
\mathcal N_{0}^{(0)}={}&\frac{1}{6}R(V){}^{a}{}^{b}{}^{i}{}^{j}R(V){}_{a}{}_{b}{}_{i}{}_{j} -\frac{68}{9}R(M){}^{a}{}^{b}{}_{a}{}_{b}T^2\\
&+\frac{352}{9}R(M){}^{a}{}^{b}{}_{a}{}^{c}T{}_{b}{}^{d}T{}_{c}{}_{d} -\frac{88}{9}R(M){}^{a}{}^{b}{}^{c}{}^{d}T{}_{a}{}_{b}T{}_{c}{}_{d}\\
&-\frac{80}{9}R(M){}^{a}{}^{b}{}^{c}{}^{d}T{}_{a}{}_{c}T{}_{b}{}_{d} +\frac{10720}{27}(T^2)^{2}\\
&-\frac{256}{3}T{}^{a}{}^{b}T{}^{c}{}^{d}\big(\mathcal D^{e}T{}_{e}{}^{f}\big)\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{f} +\frac{736}{9}DT^2\\
&+\frac{3}{4}\big(\mathcal D^{a}R(M){}_{a}{}^{b}{}^{c}{}^{d}\big)T{}^{e}{}^{f}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f} +\frac{3}{2}\big(\mathcal D^{a}R(M){}^{b}{}^{c}{}^{d}{}^{e}\big)T{}_{b}{}^{f}\epsilon{}_{a}{}_{c}{}_{d}{}_{e}{}_{f}\\
&+\big(\mathcal D^{a}R(M){}^{b}{}^{c}{}^{d}{}^{e}\big)T{}_{a}{}^{f}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f} -\frac{1}{2}\big(\mathcal D^{a}R(M){}^{b}{}^{c}{}^{d}{}^{e}\big)T{}_{d}{}^{f}\epsilon{}_{a}{}_{b}{}_{c}{}_{e}{}_{f}\\
&+\frac{3}{4}\big(\mathcal D^{a}R(M){}^{b}{}^{c}{}_{a}{}^{d}\big)T{}^{e}{}^{f}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f} +\frac{512}{9}T{}^{a}{}^{b}\big(\mathcal D_{a}\mathcal D^{c}T{}_{b}{}_{c}\big)\\
&-\frac{208}{3}T{}^{a}{}^{b}\big(\Box^c T{}_{a}{}_{b}\big) -\frac{128}{9}T{}^{a}{}^{b}\big(\mathcal D^{c}\mathcal D_{a}T{}_{b}{}_{c}\big)\\
&-\frac{8}{3}D^{2} +\frac{64}{3}\big(\mathcal D^{a}T{}^{b}{}^{c}\big)\big(\mathcal D_{b}T{}_{a}{}_{c}\big)\\
&-\frac{176}{3}\big(\mathcal D^{a}T{}^{b}{}^{c}\big)\big(\mathcal D_{a}T{}_{b}{}_{c}\big) +64\big(\mathcal D^{a}T{}_{a}{}^{b}\big)\big(\mathcal D^{c}T{}_{b}{}_{c}\big)\\
&-4\big(\Box^c D\big)
\end{aligned}
\tag{CTF-N0F0}
```

#### Scalar: $`n=0`$, explicit degree $`2`$

```math
\begin{aligned}
\mathcal N_{0}^{(2)}={}&\frac{541}{288}T{}^{d}{}^{e}\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}^{c}\chi{}_{i} +\frac{215i}{9}T{}_{b}{}_{c}\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}_{a}{}^{c}\chi{}_{i}\\
&-\frac{9613i}{144}T{}_{a}{}_{b}\overline{R(Q){}^{a}{}^{b}{}^{i}}\chi{}_{i} -192iT{}_{a}{}_{b}\overline{\chi{}^{i}}\gamma{}^{a}{}^{b}\chi{}_{i}\\
&-\frac{153i}{128}\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\big(\mathcal D^{a}R(Q){}^{b}{}^{c}{}^{i}\big)}\gamma{}^{d}{}^{e}\chi{}_{i} +\frac{27}{16}\overline{\big(\mathcal D^{a}R(Q){}_{a}{}^{b}{}^{i}\big)}\gamma{}_{b}\chi{}_{i}\\
&+\frac{32}{3}\overline{\chi{}^{i}}\gamma{}_{a}\big(\mathcal D^{a}\chi{}_{i}\big) +\frac{87i}{16}T{}_{b}{}_{c}\overline{R(Q){}^{a}{}^{b}{}^{i}}R(Q){}_{a}{}^{c}{}_{i}\\
&-\frac{15}{32}T{}_{a}{}^{f}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}^{e}R(Q){}^{c}{}^{d}{}_{i} -\frac{13i}{32}T{}_{c}{}_{d}\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}_{a}{}_{b}R(Q){}^{c}{}^{d}{}_{i}\\
&-\frac{3}{16}T{}^{e}{}^{f}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}^{d}R(Q){}_{a}{}^{c}{}_{i} +\frac{9i}{64}T{}_{c}{}_{d}\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}^{c}{}^{d}R(Q){}_{a}{}_{b}{}_{i}\\
&-\frac{5i}{8}T{}_{c}{}_{d}\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}_{b}{}^{d}R(Q){}_{a}{}^{c}{}_{i} +\frac{i}{16}T{}_{b}{}_{d}\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}_{a}{}_{c}R(Q){}^{c}{}^{d}{}_{i}\\
&-\frac{7}{64}T{}^{e}{}^{f}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}_{a}R(Q){}^{c}{}^{d}{}_{i} -\frac{i}{8}\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}^{d}{}^{e}\big(\mathcal D^{c}\chi{}_{i}\big)\\
&-\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}_{b}\big(\mathcal D_{a}\chi{}_{i}\big)
\end{aligned}
\tag{CTF-N0F2}
```

#### Scalar: $`n=1`$, explicit degree $`0`$

```math
\begin{aligned}
\mathcal N_{1}^{(0)}={}&4D\big(\Box^c \rho\big) +\frac{13}{12}R(M){}^{a}{}^{b}{}_{a}{}_{b}\widehat F{}^{c}{}^{d}T{}_{c}{}_{d}\\
&-\frac{1}{3}R(M){}^{a}{}^{b}{}_{a}{}^{c}\widehat F{}_{b}{}^{d}T{}_{c}{}_{d} +\frac{1}{12}R(M){}^{a}{}^{b}{}^{c}{}^{d}\widehat F{}_{a}{}_{b}T{}_{c}{}_{d}\\
&-\frac{13}{3}R(M){}^{a}{}^{b}{}_{a}{}^{c}\widehat F{}_{c}{}^{d}T{}_{b}{}_{d} +\frac{1}{3}R(M){}^{a}{}^{b}{}^{c}{}^{d}\widehat F{}_{a}{}_{c}T{}_{b}{}_{d}\\
&+\frac{13}{12}R(M){}^{a}{}^{b}{}^{c}{}^{d}\widehat F{}_{c}{}_{d}T{}_{a}{}_{b} +\frac{563}{36}\widehat F{}^{a}{}^{b}T{}^{c}{}^{d}\big(\mathcal D_{a}T{}^{e}{}^{f}\big)\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\\
&-\frac{139}{18}\widehat F{}^{a}{}^{b}T{}_{a}{}^{c}\big(\mathcal D^{d}T{}^{e}{}^{f}\big)\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f} +\frac{38}{3}\widehat F{}^{a}{}^{b}T{}^{c}{}^{d}\big(\mathcal D^{e}T{}_{a}{}^{f}\big)\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\\
&-\frac{361}{36}\widehat F{}^{a}{}^{b}T{}^{c}{}^{d}\big(\mathcal D^{e}T{}_{e}{}^{f}\big)\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{f} +\frac{89}{18}\widehat F{}^{a}{}^{b}T{}^{c}{}^{d}\big(\mathcal D^{e}T{}_{c}{}^{f}\big)\epsilon{}_{a}{}_{b}{}_{d}{}_{e}{}_{f}\\
&-\frac{25}{2}\widehat F{}^{a}{}^{b}T{}^{c}{}^{d}\big(\mathcal D_{c}T{}^{e}{}^{f}\big)\epsilon{}_{a}{}_{b}{}_{d}{}_{e}{}_{f} -\frac{9}{64}\big(\mathcal D^{a}R(M){}_{a}{}^{b}{}^{c}{}^{d}\big)\widehat F{}^{e}{}^{f}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\\
&-\frac{9}{32}\big(\mathcal D^{a}R(M){}^{b}{}^{c}{}^{d}{}^{e}\big)\widehat F{}_{b}{}^{f}\epsilon{}_{a}{}_{c}{}_{d}{}_{e}{}_{f} -\frac{3}{16}\big(\mathcal D^{a}R(M){}^{b}{}^{c}{}^{d}{}^{e}\big)\widehat F{}_{a}{}^{f}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\\
&+\frac{3}{32}\big(\mathcal D^{a}R(M){}^{b}{}^{c}{}^{d}{}^{e}\big)\widehat F{}_{d}{}^{f}\epsilon{}_{a}{}_{b}{}_{c}{}_{e}{}_{f} -\frac{9}{64}\big(\mathcal D^{a}R(M){}^{b}{}^{c}{}_{a}{}^{d}\big)\widehat F{}^{e}{}^{f}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\\
&+\frac{16}{3}\widehat F{}^{a}{}^{b}\big(\mathcal D_{a}\mathcal D^{c}T{}_{b}{}_{c}\big) +8\widehat F{}^{a}{}^{b}\big(\Box^c T{}_{a}{}_{b}\big)\\
&+\frac{8}{3}\widehat F{}^{a}{}^{b}\big(\mathcal D^{c}\mathcal D_{a}T{}_{b}{}_{c}\big) +\big(\Box^c \Box^c \rho\big)\\
&+6\big(\mathcal D^{a}\widehat F{}^{b}{}^{c}\big)\big(\mathcal D_{a}T{}_{b}{}_{c}\big) +\frac{8}{3}\big(\Box^c \widehat F{}^{b}{}^{c}\big)T{}_{b}{}_{c}\\
&+\frac{16}{3}\big(\mathcal D^{a}\rho\big)T{}^{b}{}^{c}\big(\mathcal D_{a}T{}_{b}{}_{c}\big) -8\big(\mathcal D^{a}\widehat F{}_{a}{}^{b}\big)\big(\mathcal D^{c}T{}_{b}{}_{c}\big)\\
&+4\big(\mathcal D^{a}\widehat F{}^{b}{}^{c}\big)\big(\mathcal D_{b}T{}_{a}{}_{c}\big) +\frac{32}{3}\big(\mathcal D^{a}\mathcal D^{b}\widehat F{}_{b}{}^{c}\big)T{}_{a}{}_{c}\\
&-128\big(\mathcal D^{a}\rho\big)T{}^{b}{}^{c}\big(\mathcal D_{b}T{}_{a}{}_{c}\big) +128\big(\mathcal D^{a}\rho\big)T{}_{a}{}^{b}\big(\mathcal D^{c}T{}_{b}{}_{c}\big)\\
&-128\big(\mathcal D^{a}\mathcal D^{b}\rho\big)T{}_{a}{}^{c}T{}_{b}{}_{c} +\frac{8}{3}\big(\Box^c \rho\big)T^2\\
&-6\big(\mathcal D^{a}\mathcal D^{b}\rho\big)\big(\mathcal D^{c}T{}^{d}{}^{e}\big)\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e} +16\big(\mathcal D^{a}\widehat F{}_{a}{}^{b}\big)T{}^{c}{}^{d}T{}^{e}{}^{f}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\\
&-\frac{8}{3}\big(\mathcal D^{a}\rho\big)\big(\mathcal D^{b}\mathcal D^{c}T{}^{d}{}^{e}\big)\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e} +\frac{800}{9}\big(\mathcal D^{a}\rho\big)T{}_{a}{}^{b}T{}^{c}{}^{d}T{}^{e}{}^{f}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}
\end{aligned}
\tag{CTF-N1F0-1}
```

```math
\begin{aligned}
&+4\big(\mathcal D^{a}D\big)\big(\mathcal D_{a}\rho\big) -\frac{1}{3}R(M){}^{a}{}^{b}{}_{a}{}^{c}\big(\mathcal D^{d}\rho\big)T{}^{e}{}^{f}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\\
&-\frac{1}{6}R(M){}^{a}{}^{b}{}^{c}{}^{d}\big(\mathcal D_{a}\rho\big)T{}^{e}{}^{f}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f} +\frac{1}{3}R(M){}^{a}{}^{b}{}^{c}{}^{d}\big(\mathcal D^{e}\rho\big)T{}_{a}{}^{f}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\\
&-\frac{2}{3}R(M){}^{a}{}^{b}{}^{c}{}^{d}\big(\mathcal D^{e}\rho\big)T{}_{c}{}^{f}\epsilon{}_{a}{}_{b}{}_{d}{}_{e}{}_{f} -\frac{1}{3}R(M){}^{a}{}^{b}{}^{c}{}^{d}\big(\mathcal D^{e}\rho\big)T{}_{e}{}^{f}\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{f}\\
&-\frac{1}{3}R(M){}^{a}{}^{b}{}^{c}{}^{d}\big(\mathcal D_{c}\rho\big)T{}^{e}{}^{f}\epsilon{}_{a}{}_{b}{}_{d}{}_{e}{}_{f}
\end{aligned}
\tag{CTF-N1F0-2}
```

#### Scalar: $`n=1`$, explicit degree $`2`$

```math
\begin{aligned}
\mathcal N_{1}^{(2)}={}&-\frac{5i}{8}D\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}_{a}{}_{b}\lambda{}_{i} +8i\overline{\big(\mathcal D^{a}\chi{}^{i}\big)}\gamma{}_{a}{}^{b}\big(\mathcal D_{b}\lambda{}_{i}\big)\\
&+16i\overline{\big(\mathcal D^{a}\chi{}^{i}\big)}\big(\mathcal D_{a}\lambda{}_{i}\big) -96T{}_{a}{}_{b}\overline{\chi{}^{i}}\gamma{}^{a}\big(\mathcal D^{b}\lambda{}_{i}\big)\\
&+96T{}_{a}{}_{b}\overline{\big(\mathcal D^{a}\chi{}^{i}\big)}\gamma{}^{b}\lambda{}_{i} +\frac{397i}{72}Y{}_{i}{}^{j}\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}_{a}{}_{b}\chi{}_{j}\\
&+\frac{1793}{18432}R(V){}^{c}{}^{d}{}_{i}{}^{j}\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}^{e}\lambda{}_{j} -\frac{181i}{1536}R(V){}_{a}{}^{c}{}_{i}{}^{j}\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}_{b}{}_{c}\lambda{}_{j}\\
&-\frac{1343i}{9216}R(V){}_{a}{}_{b}{}_{i}{}^{j}\overline{R(Q){}^{a}{}^{b}{}^{i}}\lambda{}_{j} -\frac{2i}{3}R(V){}^{a}{}^{b}{}^{i}{}^{j}\overline{\chi{}_{i}}\gamma{}_{a}{}_{b}\lambda{}_{j}\\
&+\frac{221i}{1152}T{}^{d}{}^{e}\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{R(Q){}^{a}{}^{b}{}^{i}}\big(\mathcal D^{c}\lambda{}_{i}\big) +\frac{77i}{144}T{}^{e}{}^{f}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}^{c}{}^{d}\big(\mathcal D_{a}\lambda{}_{i}\big)\\
&-\frac{3505i}{2304}T{}_{a}{}^{f}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}^{c}{}^{d}\big(\mathcal D^{e}\lambda{}_{i}\big) -\frac{157}{72}T{}_{b}{}_{c}\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}^{c}\big(\mathcal D_{a}\lambda{}_{i}\big)\\
&-\frac{217}{192}T{}_{a}{}_{b}\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}^{c}\big(\mathcal D_{c}\lambda{}_{i}\big) +\frac{3271i}{4608}T{}_{e}{}^{f}\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{f}\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}^{c}{}^{d}\big(\mathcal D^{e}\lambda{}_{i}\big)\\
&-\frac{241}{144}T{}_{b}{}_{c}\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}_{a}\big(\mathcal D^{c}\lambda{}_{i}\big) -\frac{21}{256}\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\big(\mathcal D^{a}R(Q){}^{b}{}^{c}{}^{i}\big)}\gamma{}^{d}\big(\mathcal D^{e}\lambda{}_{i}\big)\\
&+\frac{i}{16}\overline{\big(\mathcal D^{a}R(Q){}_{a}{}^{b}{}^{i}\big)}\gamma{}_{b}{}^{c}\big(\mathcal D_{c}\lambda{}_{i}\big) -\frac{41i}{128}\overline{\big(\mathcal D^{a}R(Q){}^{b}{}^{c}{}^{i}\big)}\gamma{}_{a}{}_{b}\big(\mathcal D_{c}\lambda{}_{i}\big)\\
&-\frac{17i}{32}\overline{\big(\mathcal D^{a}R(Q){}_{a}{}^{b}{}^{i}\big)}\big(\mathcal D_{b}\lambda{}_{i}\big) -\frac{75i}{256}\overline{\big(\mathcal D^{a}R(Q){}^{b}{}^{c}{}^{i}\big)}\gamma{}_{b}{}_{c}\big(\mathcal D_{a}\lambda{}_{i}\big)\\
&+\frac{3599}{864}T{}^{c}{}^{d}T{}^{e}{}^{f}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}_{a}\lambda{}_{i} -\frac{1183i}{144}T{}_{a}{}_{b}T{}_{c}{}_{d}\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}^{c}{}^{d}\lambda{}_{i}\\
&+\frac{671i}{72}T{}_{a}{}_{c}T{}_{b}{}_{d}\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}^{c}{}^{d}\lambda{}_{i} +\frac{28i}{3}T{}_{b}{}^{d}T{}_{c}{}_{d}\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}_{a}{}^{c}\lambda{}_{i}\\
&+\frac{77i}{192}T^2\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}_{a}{}_{b}\lambda{}_{i} -\frac{i}{128}T{}^{d}{}^{e}\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\big(\mathcal D^{a}R(Q){}^{b}{}^{c}{}^{i}\big)}\lambda{}_{i}\\
&-\frac{109i}{256}T{}^{e}{}^{f}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\big(\mathcal D^{a}R(Q){}_{a}{}^{b}{}^{i}\big)}\gamma{}^{c}{}^{d}\lambda{}_{i} -\frac{155i}{128}T{}_{b}{}^{f}\epsilon{}_{a}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\big(\mathcal D^{a}R(Q){}^{b}{}^{c}{}^{i}\big)}\gamma{}^{d}{}^{e}\lambda{}_{i}\\
&-\frac{41}{36}T{}_{b}{}_{c}\overline{\big(\mathcal D^{a}R(Q){}_{a}{}^{b}{}^{i}\big)}\gamma{}^{c}\lambda{}_{i} -\frac{113}{64}T{}_{b}{}_{c}\overline{\big(\mathcal D^{a}R(Q){}^{b}{}^{c}{}^{i}\big)}\gamma{}_{a}\lambda{}_{i}\\
&-\frac{23i}{1152}T{}_{a}{}^{f}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\big(\mathcal D^{a}R(Q){}^{b}{}^{c}{}^{i}\big)}\gamma{}^{d}{}^{e}\lambda{}_{i} +\frac{439}{144}T{}_{a}{}_{c}\overline{\big(\mathcal D^{a}R(Q){}^{b}{}^{c}{}^{i}\big)}\gamma{}_{b}\lambda{}_{i}\\
&+\frac{283i}{48}\widehat F{}_{a}{}_{b}\overline{R(Q){}^{a}{}^{b}{}^{i}}\chi{}_{i} -\frac{133}{96}\widehat F{}^{d}{}^{e}\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}^{c}\chi{}_{i}
\end{aligned}
\tag{CTF-N1F2-1}
```

```math
\begin{aligned}
&+\frac{5i}{24}\widehat F{}_{b}{}_{c}\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}_{a}{}^{c}\chi{}_{i} -\frac{261i}{256}\widehat F{}_{b}{}_{c}\overline{R(Q){}^{a}{}^{b}{}^{i}}R(Q){}_{a}{}^{c}{}_{i}\\
&+\frac{45}{512}\widehat F{}_{a}{}^{f}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}^{e}R(Q){}^{c}{}^{d}{}_{i} +\frac{39i}{512}\widehat F{}_{c}{}_{d}\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}_{a}{}_{b}R(Q){}^{c}{}^{d}{}_{i}\\
&+\frac{9}{256}\widehat F{}^{e}{}^{f}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}^{d}R(Q){}_{a}{}^{c}{}_{i} -\frac{27i}{1024}\widehat F{}_{c}{}_{d}\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}^{c}{}^{d}R(Q){}_{a}{}_{b}{}_{i}\\
&+\frac{15i}{128}\widehat F{}_{c}{}_{d}\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}_{b}{}^{d}R(Q){}_{a}{}^{c}{}_{i} -\frac{3i}{256}\widehat F{}_{b}{}_{d}\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}_{a}{}_{c}R(Q){}^{c}{}^{d}{}_{i}\\
&+\frac{21}{1024}\widehat F{}^{e}{}^{f}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}_{a}R(Q){}^{c}{}^{d}{}_{i} +8i\overline{\big(\Box^c \chi{}^{i}\big)}\lambda{}_{i}\\
&-96\big(\mathcal D^{b}T{}_{a}{}_{b}\big)\overline{\chi{}^{i}}\gamma{}^{a}\lambda{}_{i} -\frac{13i}{256}\overline{\big(\Box^c R(Q){}^{b}{}^{c}{}^{i}\big)}\gamma{}_{b}{}_{c}\lambda{}_{i}\\
&-\frac{9i}{64}\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}_{a}{}_{b}\big(\Box^c \lambda{}_{i}\big) +8i\overline{\chi{}^{i}}\big(\Box^c \lambda{}_{i}\big)\\
&-\frac{287i}{2304}\big(\mathcal D^{c}T{}^{d}{}^{e}\big)\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{R(Q){}^{a}{}^{b}{}^{i}}\lambda{}_{i} -\frac{1265i}{2304}\big(\mathcal D_{a}T{}^{e}{}^{f}\big)\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}^{c}{}^{d}\lambda{}_{i}\\
&+\frac{511i}{384}\big(\mathcal D^{e}T{}_{a}{}^{f}\big)\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}^{c}{}^{d}\lambda{}_{i} +\frac{2501}{576}\big(\mathcal D_{a}T{}_{b}{}_{c}\big)\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}^{c}\lambda{}_{i}\\
&+\frac{2683}{1152}\big(\mathcal D_{c}T{}_{a}{}_{b}\big)\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}^{c}\lambda{}_{i} +\frac{883i}{1536}\big(\mathcal D^{e}T{}_{e}{}^{f}\big)\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{f}\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}^{c}{}^{d}\lambda{}_{i}\\
&-\frac{8063}{1152}\big(\mathcal D^{c}T{}_{b}{}_{c}\big)\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}_{a}\lambda{}_{i} +\frac{197i}{192}\big(\mathcal D^{e}T{}_{c}{}^{f}\big)\epsilon{}_{a}{}_{b}{}_{d}{}_{e}{}_{f}\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}^{c}{}^{d}\lambda{}_{i}\\
&-\frac{161i}{288}\big(\mathcal D_{c}T{}^{e}{}^{f}\big)\epsilon{}_{a}{}_{b}{}_{d}{}_{e}{}_{f}\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}^{c}{}^{d}\lambda{}_{i} -\frac{i}{3}T{}_{d}{}^{f}\epsilon{}_{a}{}_{b}{}_{c}{}_{e}{}_{f}\overline{\big(\mathcal D^{a}R(Q){}^{b}{}^{c}{}^{i}\big)}\gamma{}^{d}{}^{e}\lambda{}_{i}\\
&-\frac{5i}{36}T{}^{e}{}^{f}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\big(\mathcal D^{a}R(Q){}^{b}{}^{c}{}^{i}\big)}\gamma{}_{a}{}^{d}\lambda{}_{i} -\frac{101i}{256}T{}_{c}{}^{f}\epsilon{}_{a}{}_{b}{}_{d}{}_{e}{}_{f}\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}^{c}{}^{d}\big(\mathcal D^{e}\lambda{}_{i}\big)\\
&-\frac{149i}{576}T{}^{e}{}^{f}\epsilon{}_{a}{}_{b}{}_{d}{}_{e}{}_{f}\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}^{c}{}^{d}\big(\mathcal D_{c}\lambda{}_{i}\big) +\frac{i}{16}\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}_{a}{}^{c}\big(\mathcal D_{c}\mathcal D_{b}\lambda{}_{i}\big)\\
&+\frac{i}{8}\overline{R(Q){}^{a}{}^{b}{}^{i}}\big(\mathcal D_{a}\mathcal D_{b}\lambda{}_{i}\big) +\frac{1}{32}\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}^{c}\big(\mathcal D^{d}\mathcal D^{e}\lambda{}_{i}\big)\\
&+\frac{16i}{3}\overline{\chi{}^{i}}\gamma{}^{a}{}^{b}\big(\mathcal D_{a}\mathcal D_{b}\lambda{}_{i}\big) -\frac{i}{8}\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}_{a}{}^{c}\big(\mathcal D_{b}\mathcal D_{c}\lambda{}_{i}\big)\\
&+\frac{9i}{64}\overline{\big(\mathcal D^{a}\mathcal D^{b}R(Q){}_{a}{}_{b}{}^{i}\big)}\lambda{}_{i} -\frac{25i}{192}\overline{\big(\mathcal D^{a}\mathcal D^{b}R(Q){}_{b}{}^{c}{}^{i}\big)}\gamma{}_{a}{}_{c}\lambda{}_{i}\\
&-\frac{49i}{384}\overline{\big(\mathcal D^{a}\mathcal D^{b}R(Q){}_{a}{}^{c}{}^{i}\big)}\gamma{}_{b}{}_{c}\lambda{}_{i} +\frac{41}{768}\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\big(\mathcal D^{a}\mathcal D^{b}R(Q){}^{c}{}^{d}{}^{i}\big)}\gamma{}^{e}\lambda{}_{i}
\end{aligned}
\tag{CTF-N1F2-2}
```

```math
\begin{aligned}
&-\frac{i}{64}\big(\mathcal D^{d}T{}^{e}{}^{f}\big)\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}_{a}{}^{c}\lambda{}_{i} -\frac{35i}{24}\big(\mathcal D^{e}\rho\big)\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}^{c}{}^{d}\chi{}_{i}\\
&-\frac{121}{12}\big(\mathcal D_{b}\rho\big)\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}_{a}\chi{}_{i} -4i\overline{\big(\mathcal D^{a}\mathcal D^{b}\chi{}^{i}\big)}\gamma{}_{a}{}_{b}\lambda{}_{i}\\
&-\frac{11i}{128}T{}^{e}{}^{f}\epsilon{}_{a}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\big(\mathcal D^{a}R(Q){}^{b}{}^{c}{}^{i}\big)}\gamma{}_{b}{}^{d}\lambda{}_{i} +\frac{7i}{192}T{}^{e}{}^{f}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}_{a}{}^{c}\big(\mathcal D^{d}\lambda{}_{i}\big)\\
&+\frac{23i}{768}Y{}_{i}{}_{j}\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}_{b}{}_{c}R(Q){}_{a}{}^{c}{}^{j} +\frac{49i}{1536}Y{}_{i}{}_{j}\overline{R(Q){}^{a}{}^{b}{}^{i}}R(Q){}_{a}{}_{b}{}^{j}\\
&-\frac{1}{1024}Y{}_{i}{}_{j}\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}^{e}R(Q){}^{c}{}^{d}{}^{j} +\frac{1}{12}R(M){}^{a}{}^{b}{}^{c}{}^{d}\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\chi{}^{i}}\gamma{}^{e}\lambda{}_{i}\\
&+\frac{i}{3}R(M){}^{a}{}^{b}{}_{a}{}^{c}\overline{\chi{}^{i}}\gamma{}_{b}{}_{c}\lambda{}_{i} +\frac{i}{6}R(M){}^{a}{}^{b}{}_{a}{}_{b}\overline{\chi{}^{i}}\lambda{}_{i}
\end{aligned}
\tag{CTF-N1F2-3}
```

#### Scalar: $`n=2`$, explicit degree $`0`$

```math
\begin{aligned}
\mathcal N_{2}^{(0)}={}&-12DY^2 +R(V){}^{a}{}^{b}{}^{i}{}^{j}Y{}_{i}{}_{j}\widehat F{}_{a}{}_{b}\\
&-2Y{}^{i}{}^{j}\big(\Box^c Y{}_{i}{}_{j}\big) -8Y^2T^2\\
&-\big(\Box^c \rho\big)\big(\Box^c \rho\big) -8\widehat F{}^{a}{}^{b}\big(\Box^c \rho\big)T{}_{a}{}_{b}\\
&-\big(\mathcal D^{a}Y{}^{i}{}^{j}\big)\big(\mathcal D_{a}Y{}_{i}{}_{j}\big) -\big(\mathcal D^{a}\rho\big)\big(\mathcal D_{a}\Box^c \rho\big)\\
&-8\widehat F{}^{a}{}^{b}\big(\mathcal D^{c}\rho\big)\big(\mathcal D_{c}T{}_{a}{}_{b}\big) -\frac{8}{3}\big(\mathcal D^{a}\widehat F{}^{b}{}^{c}\big)\big(\mathcal D_{a}\rho\big)T{}_{b}{}_{c}\\
&-\frac{4}{3}\big(\mathcal D^{a}\rho\big)\big(\mathcal D_{a}\rho\big)T^2 -\frac{32}{3}\big(\mathcal D^{a}\widehat F{}^{b}{}^{c}\big)\big(\mathcal D_{b}\rho\big)T{}_{a}{}_{c}\\
&+64\big(\mathcal D^{a}\rho\big)\big(\mathcal D^{b}\rho\big)T{}_{a}{}^{c}T{}_{b}{}_{c} +4\big(\mathcal D^{a}\rho\big)\big(\mathcal D^{b}\mathcal D^{c}\rho\big)T{}^{d}{}^{e}\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\\
&-2D\big(\mathcal D^{a}\rho\big)\big(\mathcal D_{a}\rho\big) +\frac{1}{16}R(M){}^{a}{}^{b}{}_{a}{}_{b}\widehat F^2\\
&-\frac{1}{2}R(M){}^{a}{}^{b}{}_{a}{}^{c}\widehat F{}_{b}{}^{d}\widehat F{}_{c}{}_{d} +\frac{1}{8}R(M){}^{a}{}^{b}{}^{c}{}^{d}\widehat F{}_{a}{}_{b}\widehat F{}_{c}{}_{d}\\
&+\frac{1}{4}R(M){}^{a}{}^{b}{}^{c}{}^{d}\widehat F{}_{a}{}_{c}\widehat F{}_{b}{}_{d} +\frac{50}{3}\widehat F^2T^2\\
&-64\widehat F{}^{a}{}^{b}\widehat F{}_{a}{}^{c}T{}_{b}{}^{d}T{}_{c}{}_{d} +\frac{1}{16}R(M){}^{a}{}^{b}{}_{a}{}^{c}\widehat F{}^{d}{}^{e}\big(\mathcal D^{f}\rho\big)\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\\
&+\frac{1}{32}R(M){}^{a}{}^{b}{}^{c}{}^{d}\widehat F{}^{e}{}^{f}\big(\mathcal D_{a}\rho\big)\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f} +\frac{1}{16}R(M){}^{a}{}^{b}{}^{c}{}^{d}\widehat F{}_{a}{}^{e}\big(\mathcal D^{f}\rho\big)\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\\
&-\frac{1}{8}R(M){}^{a}{}^{b}{}^{c}{}^{d}\widehat F{}_{c}{}^{e}\big(\mathcal D^{f}\rho\big)\epsilon{}_{a}{}_{b}{}_{d}{}_{e}{}_{f} +\frac{1}{16}R(M){}^{a}{}^{b}{}^{c}{}^{d}\widehat F{}^{e}{}^{f}\big(\mathcal D_{e}\rho\big)\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{f}\\
&+\frac{1}{16}R(M){}^{a}{}^{b}{}^{c}{}^{d}\widehat F{}^{e}{}^{f}\big(\mathcal D_{c}\rho\big)\epsilon{}_{a}{}_{b}{}_{d}{}_{e}{}_{f} +2\widehat F{}^{a}{}^{b}\widehat F{}^{c}{}^{d}\big(\mathcal D^{e}T{}_{e}{}^{f}\big)\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{f}\\
&+\frac{1}{2}\widehat F{}^{a}{}^{b}\big(\Box^c \widehat F{}_{a}{}_{b}\big) +\frac{25}{12}\widehat F{}^{a}{}^{b}\big(\mathcal D_{a}\widehat F{}^{c}{}^{d}\big)T{}^{e}{}^{f}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\\
&-\frac{17}{6}\widehat F{}^{a}{}^{b}\big(\mathcal D^{c}\widehat F{}^{d}{}^{e}\big)T{}_{a}{}^{f}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f} -\frac{7}{3}\widehat F{}^{a}{}^{b}\big(\mathcal D^{c}\widehat F{}_{a}{}^{d}\big)T{}^{e}{}^{f}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\\
&+\frac{35}{12}\widehat F{}^{a}{}^{b}\big(\mathcal D^{c}\widehat F{}_{c}{}^{d}\big)T{}^{e}{}^{f}\epsilon{}_{a}{}_{b}{}_{d}{}_{e}{}_{f} +\frac{11}{6}\widehat F{}^{a}{}^{b}\big(\mathcal D^{c}\widehat F{}^{d}{}^{e}\big)T{}_{d}{}^{f}\epsilon{}_{a}{}_{b}{}_{c}{}_{e}{}_{f}\\
&+2\widehat F{}^{a}{}^{b}\big(\mathcal D^{c}\widehat F{}^{d}{}^{e}\big)T{}_{c}{}^{f}\epsilon{}_{a}{}_{b}{}_{d}{}_{e}{}_{f} -\frac{16}{3}\widehat F{}^{a}{}^{b}\big(\mathcal D_{a}\mathcal D^{c}\rho\big)T{}_{b}{}_{c}
\end{aligned}
\tag{CTF-N2F0-1}
```

```math
\begin{aligned}
&+\frac{16}{3}\widehat F{}^{a}{}^{b}\big(\mathcal D^{c}\mathcal D_{a}\rho\big)T{}_{b}{}_{c} -\big(\mathcal D^{a}\rho\big)\big(\Box^c \mathcal D_{a}\rho\big)\\
&+\frac{1}{4}\big(\mathcal D^{a}\widehat F{}^{b}{}^{c}\big)\big(\mathcal D_{a}\widehat F{}_{b}{}_{c}\big) -\frac{1}{2}\big(\mathcal D^{a}\mathcal D^{b}\rho\big)\big(\mathcal D_{a}\mathcal D_{b}\rho\big)\\
&+D\widehat F^2
\end{aligned}
\tag{CTF-N2F0-2}
```

#### Scalar: $`n=2`$, explicit degree $`2`$

```math
\begin{aligned}
\mathcal N_{2}^{(2)}={}&4D\overline{\lambda{}^{i}}\gamma{}^{a}\big(\mathcal D_{a}\lambda{}_{i}\big) +16Y{}^{i}{}^{j}\overline{\big(\mathcal D^{a}\chi{}_{i}\big)}\gamma{}_{a}\lambda{}_{j}\\
&+\frac{1}{2}R(V){}^{a}{}^{b}{}^{i}{}^{j}\overline{\lambda{}_{i}}\gamma{}_{a}\big(\mathcal D_{b}\lambda{}_{j}\big) +\frac{2}{3}R(V){}^{a}{}^{b}{}^{i}{}^{j}T{}^{d}{}^{e}\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\lambda{}_{i}}\gamma{}^{c}\lambda{}_{j}\\
&+\frac{2i}{3}R(V){}^{a}{}^{b}{}^{i}{}^{j}T{}_{a}{}_{b}\overline{\lambda{}_{i}}\lambda{}_{j} +\frac{305i}{768}\widehat F{}_{a}{}_{b}T{}_{c}{}_{d}\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}^{c}{}^{d}\lambda{}_{i}\\
&-48i\widehat F{}^{a}{}^{b}T{}_{a}{}_{b}\overline{\chi{}^{i}}\lambda{}_{i} +\frac{809}{1536}\widehat F{}_{b}{}_{c}\overline{\big(\mathcal D^{a}R(Q){}^{b}{}^{c}{}^{i}\big)}\gamma{}_{a}\lambda{}_{i}\\
&+\frac{12631}{4608}\widehat F{}^{d}{}^{e}T{}_{a}{}^{f}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}^{c}\lambda{}_{i} +\frac{805}{576}\widehat F{}_{a}{}^{d}T{}^{e}{}^{f}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}^{c}\lambda{}_{i}\\
&-\frac{883i}{2304}\widehat F{}_{c}{}_{d}T{}_{a}{}_{b}\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}^{c}{}^{d}\lambda{}_{i} +\frac{41i}{36}\widehat F{}_{a}{}_{c}T{}_{b}{}_{d}\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}^{c}{}^{d}\lambda{}_{i}\\
&-\frac{2591}{4608}\widehat F{}^{d}{}^{e}T{}_{d}{}^{f}\epsilon{}_{a}{}_{b}{}_{c}{}_{e}{}_{f}\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}^{c}\lambda{}_{i} +\frac{13i}{8}\widehat F{}_{c}{}^{d}T{}_{b}{}_{d}\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}_{a}{}^{c}\lambda{}_{i}\\
&-\frac{1387i}{576}\widehat F{}_{b}{}^{d}T{}_{c}{}_{d}\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}_{a}{}^{c}\lambda{}_{i} -\frac{37i}{144}\widehat F{}_{a}{}^{c}T{}_{b}{}_{c}\overline{R(Q){}^{a}{}^{b}{}^{i}}\lambda{}_{i}\\
&+\frac{251i}{2304}\widehat F{}^{c}{}^{d}T{}_{c}{}_{d}\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}_{a}{}_{b}\lambda{}_{i} +24\widehat F{}^{b}{}^{c}T{}^{d}{}^{e}\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\chi{}^{i}}\gamma{}^{a}\lambda{}_{i}\\
&-\frac{145i}{3072}\widehat F{}^{d}{}^{e}\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\big(\mathcal D^{a}R(Q){}^{b}{}^{c}{}^{i}\big)}\lambda{}_{i} +\frac{151i}{6144}\widehat F{}^{e}{}^{f}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\big(\mathcal D^{a}R(Q){}_{a}{}^{b}{}^{i}\big)}\gamma{}^{c}{}^{d}\lambda{}_{i}\\
&+\frac{17i}{256}\widehat F{}_{b}{}^{f}\epsilon{}_{a}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\big(\mathcal D^{a}R(Q){}^{b}{}^{c}{}^{i}\big)}\gamma{}^{d}{}^{e}\lambda{}_{i} +\frac{5}{24}\widehat F{}_{b}{}_{c}\overline{\big(\mathcal D^{a}R(Q){}_{a}{}^{b}{}^{i}\big)}\gamma{}^{c}\lambda{}_{i}\\
&+\frac{169i}{2048}\widehat F{}_{a}{}^{f}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\big(\mathcal D^{a}R(Q){}^{b}{}^{c}{}^{i}\big)}\gamma{}^{d}{}^{e}\lambda{}_{i} +\frac{107}{768}\widehat F{}_{a}{}_{c}\overline{\big(\mathcal D^{a}R(Q){}^{b}{}^{c}{}^{i}\big)}\gamma{}_{b}\lambda{}_{i}\\
&-i\widehat F{}^{d}{}^{e}\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\big(\mathcal D^{a}\chi{}^{i}\big)}\gamma{}^{b}{}^{c}\lambda{}_{i} +4\widehat F{}_{a}{}_{b}\overline{\big(\mathcal D^{a}\chi{}^{i}\big)}\gamma{}^{b}\lambda{}_{i}\\
&+\frac{1}{2}\overline{\lambda{}^{i}}\gamma{}^{a}\big(\Box^c \mathcal D_{a}\lambda{}_{i}\big) -i\big(\Box^c T{}_{a}{}_{b}\big)\overline{\lambda{}^{i}}\gamma{}^{a}{}^{b}\lambda{}_{i}\\
&-i\big(\mathcal D_{c}T{}_{a}{}_{b}\big)\overline{\lambda{}^{i}}\gamma{}^{a}{}^{b}\big(\mathcal D^{c}\lambda{}_{i}\big) -iT{}_{a}{}_{b}\overline{\lambda{}^{i}}\gamma{}^{a}{}^{b}\big(\Box^c \lambda{}_{i}\big)\\
&-8i\big(\mathcal D_{a}\rho\big)\overline{\big(\mathcal D^{a}\chi{}^{i}\big)}\lambda{}_{i} -8i\big(\Box^c \rho\big)\overline{\chi{}^{i}}\lambda{}_{i}\\
&+\big(\mathcal D^{c}T{}^{d}{}^{e}\big)\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\lambda{}^{i}}\gamma{}^{a}\big(\mathcal D^{b}\lambda{}_{i}\big) +6i\big(\mathcal D^{c}T{}_{b}{}_{c}\big)\overline{\lambda{}^{i}}\gamma{}^{a}{}^{b}\big(\mathcal D_{a}\lambda{}_{i}\big)\\
&-4i\big(\mathcal D^{b}T{}_{a}{}_{b}\big)\overline{\lambda{}^{i}}\big(\mathcal D^{a}\lambda{}_{i}\big) -\frac{1}{3}T{}^{d}{}^{e}\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\lambda{}^{i}}\gamma{}^{a}\big(\mathcal D^{b}\mathcal D^{c}\lambda{}_{i}\big)
\end{aligned}
\tag{CTF-N2F2-1}
```

```math
\begin{aligned}
&-\frac{2i}{3}T{}_{b}{}_{c}\overline{\lambda{}^{i}}\gamma{}^{a}{}^{b}\big(\mathcal D_{a}\mathcal D^{c}\lambda{}_{i}\big) +\frac{8i}{3}T{}_{b}{}_{c}\overline{\lambda{}^{i}}\gamma{}^{a}{}^{b}\big(\mathcal D^{c}\mathcal D_{a}\lambda{}_{i}\big)\\
&-\frac{4i}{3}T{}_{a}{}_{b}\overline{\lambda{}^{i}}\big(\mathcal D^{a}\mathcal D^{b}\lambda{}_{i}\big) +\frac{11i}{6}T{}^{c}{}^{d}\big(\mathcal D_{c}T{}^{e}{}^{f}\big)\epsilon{}_{a}{}_{b}{}_{d}{}_{e}{}_{f}\overline{\lambda{}^{i}}\gamma{}^{a}{}^{b}\lambda{}_{i}\\
&+\frac{5i}{9}T{}^{c}{}^{d}\big(\mathcal D^{e}T{}_{c}{}^{f}\big)\epsilon{}_{a}{}_{b}{}_{d}{}_{e}{}_{f}\overline{\lambda{}^{i}}\gamma{}^{a}{}^{b}\lambda{}_{i} +\frac{19i}{9}T{}^{c}{}^{d}\big(\mathcal D^{e}T{}_{e}{}^{f}\big)\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{f}\overline{\lambda{}^{i}}\gamma{}^{a}{}^{b}\lambda{}_{i}\\
&+2iT{}^{b}{}^{c}T{}^{d}{}^{e}\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\lambda{}^{i}}\big(\mathcal D^{a}\lambda{}_{i}\big) -2iT{}^{c}{}^{d}T{}^{e}{}^{f}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\lambda{}^{i}}\gamma{}^{a}{}^{b}\big(\mathcal D_{a}\lambda{}_{i}\big)\\
&-16T{}_{a}{}^{c}T{}_{b}{}_{c}\overline{\lambda{}^{i}}\gamma{}^{a}\big(\mathcal D^{b}\lambda{}_{i}\big) +\frac{20}{3}T^2\overline{\lambda{}^{i}}\gamma{}^{a}\big(\mathcal D_{a}\lambda{}_{i}\big)\\
&-\frac{4i}{3}\big(\mathcal D^{c}\mathcal D_{a}T{}_{b}{}_{c}\big)\overline{\lambda{}^{i}}\gamma{}^{a}{}^{b}\lambda{}_{i} -\frac{2i}{3}\big(\mathcal D_{a}\mathcal D^{c}T{}_{b}{}_{c}\big)\overline{\lambda{}^{i}}\gamma{}^{a}{}^{b}\lambda{}_{i}\\
&-\frac{2i}{9}T{}^{c}{}^{d}\big(\mathcal D_{a}T{}^{e}{}^{f}\big)\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\lambda{}^{i}}\gamma{}^{a}{}^{b}\lambda{}_{i} +24iT{}_{a}{}_{b}T^2\overline{\lambda{}^{i}}\gamma{}^{a}{}^{b}\lambda{}_{i}\\
&-96iT{}_{a}{}^{c}T{}_{b}{}^{d}T{}_{c}{}_{d}\overline{\lambda{}^{i}}\gamma{}^{a}{}^{b}\lambda{}_{i} -\frac{i}{9}T{}_{a}{}^{c}\big(\mathcal D^{d}T{}^{e}{}^{f}\big)\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\lambda{}^{i}}\gamma{}^{a}{}^{b}\lambda{}_{i}\\
&-\frac{11}{48}\big(\mathcal D_{a}Y{}_{i}{}^{j}\big)\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}_{b}\lambda{}_{j} -\frac{271}{1728}Y{}_{i}{}^{j}T{}^{d}{}^{e}\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}^{c}\lambda{}_{j}\\
&+\frac{77i}{27}Y{}_{i}{}^{j}T{}_{b}{}_{c}\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}_{a}{}^{c}\lambda{}_{j} +\frac{37i}{288}Y{}_{i}{}^{j}T{}_{a}{}_{b}\overline{R(Q){}^{a}{}^{b}{}^{i}}\lambda{}_{j}\\
&+\frac{i}{8}R(M){}^{a}{}^{b}{}_{a}{}_{b}T{}_{c}{}_{d}\overline{\lambda{}^{i}}\gamma{}^{c}{}^{d}\lambda{}_{i} -\frac{i}{2}R(M){}^{a}{}^{b}{}_{a}{}^{c}T{}_{c}{}_{d}\overline{\lambda{}^{i}}\gamma{}_{b}{}^{d}\lambda{}_{i}\\
&+\frac{i}{8}R(M){}^{a}{}^{b}{}^{c}{}^{d}T{}_{c}{}_{d}\overline{\lambda{}^{i}}\gamma{}_{a}{}_{b}\lambda{}_{i} -\frac{i}{4}R(M){}^{a}{}^{b}{}_{a}{}^{c}T{}_{b}{}_{d}\overline{\lambda{}^{i}}\gamma{}_{c}{}^{d}\lambda{}_{i}\\
&+\frac{i}{4}R(M){}^{a}{}^{b}{}^{c}{}^{d}T{}_{b}{}_{d}\overline{\lambda{}^{i}}\gamma{}_{a}{}_{c}\lambda{}_{i} +\frac{i}{12}R(M){}^{a}{}^{b}{}^{c}{}^{d}T{}_{a}{}_{b}\overline{\lambda{}^{i}}\gamma{}_{c}{}_{d}\lambda{}_{i}\\
&-\frac{41}{96}\big(\mathcal D_{c}\rho\big)T{}_{a}{}_{b}\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}^{c}\lambda{}_{i} -16Y{}^{i}{}^{j}\overline{\chi{}_{i}}\gamma{}^{a}\big(\mathcal D_{a}\lambda{}_{j}\big)\\
&-\frac{i}{6}\big(\mathcal D^{c}\widehat F{}^{d}{}^{e}\big)\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\chi{}^{i}}\gamma{}^{a}{}^{b}\lambda{}_{i} +4\big(\mathcal D^{b}\widehat F{}_{a}{}_{b}\big)\overline{\chi{}^{i}}\gamma{}^{a}\lambda{}_{i}\\
&-\frac{14i}{3}\big(\mathcal D_{a}\mathcal D_{b}\rho\big)\overline{\chi{}^{i}}\gamma{}^{a}{}^{b}\lambda{}_{i} +\frac{13i}{128}\big(\Box^c \rho\big)\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}_{a}{}_{b}\lambda{}_{i}\\
&-\frac{1}{2}\overline{\big(\mathcal D_{a}\lambda{}^{i}\big)}\gamma{}^{a}\big(\Box^c \lambda{}_{i}\big) +T{}^{d}{}^{e}\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\big(\mathcal D^{b}\lambda{}^{i}\big)}\gamma{}^{a}\big(\mathcal D^{c}\lambda{}_{i}\big)\\
&-2iT{}_{a}{}_{b}\overline{\big(\mathcal D^{c}\lambda{}^{i}\big)}\gamma{}^{a}{}^{b}\big(\mathcal D_{c}\lambda{}_{i}\big) -2iT{}_{b}{}_{c}\overline{\big(\mathcal D_{a}\lambda{}^{i}\big)}\gamma{}^{a}{}^{b}\big(\mathcal D^{c}\lambda{}_{i}\big)
\end{aligned}
\tag{CTF-N2F2-2}
```

```math
\begin{aligned}
&-8i\big(\mathcal D_{a}\rho\big)\overline{\chi{}^{i}}\big(\mathcal D^{a}\lambda{}_{i}\big) +\frac{15i}{64}\big(\mathcal D_{b}\rho\big)\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}_{a}{}^{c}\big(\mathcal D_{c}\lambda{}_{i}\big)\\
&-\frac{5i}{64}\big(\mathcal D_{b}\rho\big)\overline{R(Q){}^{a}{}^{b}{}^{i}}\big(\mathcal D_{a}\lambda{}_{i}\big) -\frac{9i}{64}\big(\mathcal D_{a}\rho\big)T{}^{e}{}^{f}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}^{c}{}^{d}\lambda{}_{i}\\
&+\frac{17}{12}\big(\mathcal D_{a}\rho\big)T{}_{b}{}_{c}\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}^{c}\lambda{}_{i} -\frac{11i}{256}Y{}_{i}{}^{j}\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\big(\mathcal D^{a}R(Q){}^{b}{}^{c}{}^{i}\big)}\gamma{}^{d}{}^{e}\lambda{}_{j}\\
&-\frac{7}{96}Y{}_{i}{}^{j}\overline{\big(\mathcal D^{a}R(Q){}_{a}{}^{b}{}^{i}\big)}\gamma{}_{b}\lambda{}_{j} -\frac{i}{48}Y{}_{i}{}^{j}\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}^{c}{}^{d}\big(\mathcal D^{e}\lambda{}_{j}\big)\\
&+\frac{1}{8}Y{}_{i}{}^{j}\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}_{a}\big(\mathcal D_{b}\lambda{}_{j}\big) -\frac{i}{384}\big(\mathcal D^{c}Y{}_{i}{}^{j}\big)\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}^{d}{}^{e}\lambda{}_{j}\\
&+\frac{1}{2}\overline{\big(\mathcal D^{b}\lambda{}^{i}\big)}\gamma{}^{a}\big(\mathcal D_{b}\mathcal D_{a}\lambda{}_{i}\big) +\frac{15i}{128}\big(\mathcal D_{a}\rho\big)\overline{\big(\mathcal D^{a}R(Q){}^{b}{}^{c}{}^{i}\big)}\gamma{}_{b}{}_{c}\lambda{}_{i}\\
&+\frac{5i}{32}\big(\mathcal D_{c}\rho\big)\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}_{a}{}_{b}\big(\mathcal D^{c}\lambda{}_{i}\big) -\frac{19i}{64}\big(\mathcal D^{c}\rho\big)T{}^{d}{}^{e}\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{R(Q){}^{a}{}^{b}{}^{i}}\lambda{}_{i}\\
&-\frac{219i}{256}\big(\mathcal D^{e}\rho\big)T{}_{a}{}^{f}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}^{c}{}^{d}\lambda{}_{i} -\frac{401i}{1536}\big(\mathcal D^{e}\rho\big)T{}_{e}{}^{f}\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{f}\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}^{c}{}^{d}\lambda{}_{i}\\
&-\frac{35}{48}\big(\mathcal D^{c}\rho\big)T{}_{b}{}_{c}\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}_{a}\lambda{}_{i} -\frac{3i}{256}\big(\mathcal D^{e}\rho\big)T{}_{c}{}^{f}\epsilon{}_{a}{}_{b}{}_{d}{}_{e}{}_{f}\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}^{c}{}^{d}\lambda{}_{i}\\
&+\frac{51i}{64}\big(\mathcal D_{c}\rho\big)T{}^{e}{}^{f}\epsilon{}_{a}{}_{b}{}_{d}{}_{e}{}_{f}\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}^{c}{}^{d}\lambda{}_{i} -\frac{9i}{64}\big(\mathcal D_{c}\rho\big)\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}_{a}{}^{c}\big(\mathcal D_{b}\lambda{}_{i}\big)\\
&-\frac{3}{128}\big(\mathcal D^{e}\rho\big)\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}^{c}\big(\mathcal D^{d}\lambda{}_{i}\big) -\frac{5i}{32}\big(\mathcal D_{b}\rho\big)\overline{\big(\mathcal D^{a}R(Q){}_{a}{}^{b}{}^{i}\big)}\lambda{}_{i}\\
&-\frac{3i}{32}\big(\mathcal D_{c}\rho\big)\overline{\big(\mathcal D^{a}R(Q){}_{a}{}^{b}{}^{i}\big)}\gamma{}_{b}{}^{c}\lambda{}_{i} -\frac{i}{64}\big(\mathcal D_{c}\rho\big)\overline{\big(\mathcal D^{a}R(Q){}^{b}{}^{c}{}^{i}\big)}\gamma{}_{a}{}_{b}\lambda{}_{i}\\
&+\frac{3}{128}\big(\mathcal D^{e}\rho\big)\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\big(\mathcal D^{a}R(Q){}^{b}{}^{c}{}^{i}\big)}\gamma{}^{d}\lambda{}_{i} +\frac{3i}{32}\big(\mathcal D^{d}\rho\big)T{}^{e}{}^{f}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}_{a}{}^{c}\lambda{}_{i}\\
&-\frac{1}{16}R(M){}^{a}{}^{b}{}_{a}{}^{c}\overline{\lambda{}^{i}}\gamma{}_{c}\big(\mathcal D_{b}\lambda{}_{i}\big) +\frac{i}{64}R(M){}^{a}{}^{b}{}^{c}{}^{d}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\lambda{}^{i}}\gamma{}^{e}{}^{f}\big(\mathcal D_{a}\lambda{}_{i}\big)\\
&+\frac{3i}{64}\widehat F{}^{e}{}^{f}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}^{c}{}^{d}\big(\mathcal D_{a}\lambda{}_{i}\big) -\frac{3i}{128}\widehat F{}_{a}{}^{e}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}^{c}{}^{d}\big(\mathcal D^{f}\lambda{}_{i}\big)\\
&-\frac{3}{8}\widehat F{}_{a}{}_{c}\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}^{c}\big(\mathcal D_{b}\lambda{}_{i}\big) -\frac{3}{16}\widehat F{}_{a}{}_{b}\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}^{c}\big(\mathcal D_{c}\lambda{}_{i}\big)\\
&+\frac{3i}{64}\widehat F{}^{e}{}^{f}\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{f}\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}^{c}{}^{d}\big(\mathcal D_{e}\lambda{}_{i}\big) -\frac{11}{64}\widehat F{}_{b}{}^{c}\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}_{a}\big(\mathcal D_{c}\lambda{}_{i}\big)\\
&-\frac{89}{256}\widehat F{}_{c}{}^{d}T{}^{e}{}^{f}\epsilon{}_{a}{}_{b}{}_{d}{}_{e}{}_{f}\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}^{c}\lambda{}_{i} -\frac{1097}{9216}\widehat F{}^{d}{}^{e}T{}_{c}{}^{f}\epsilon{}_{a}{}_{b}{}_{d}{}_{e}{}_{f}\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}^{c}\lambda{}_{i}
\end{aligned}
\tag{CTF-N2F2-3}
```

```math
\begin{aligned}
&-\frac{13}{576}\widehat F{}^{c}{}^{d}T{}^{e}{}^{f}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}_{a}\lambda{}_{i} +\frac{i}{128}\widehat F{}_{c}{}^{e}\epsilon{}_{a}{}_{b}{}_{d}{}_{e}{}_{f}\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}^{c}{}^{d}\big(\mathcal D^{f}\lambda{}_{i}\big)\\
&+i\widehat F{}^{c}{}^{d}\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\chi{}^{i}}\gamma{}^{a}{}^{b}\big(\mathcal D^{e}\lambda{}_{i}\big) -4\widehat F{}_{a}{}^{b}\overline{\chi{}^{i}}\gamma{}^{a}\big(\mathcal D_{b}\lambda{}_{i}\big)\\
&-\frac{25i}{3072}\widehat F{}_{d}{}^{f}\epsilon{}_{a}{}_{b}{}_{c}{}_{e}{}_{f}\overline{\big(\mathcal D^{a}R(Q){}^{b}{}^{c}{}^{i}\big)}\gamma{}^{d}{}^{e}\lambda{}_{i} -\frac{7i}{256}\big(\mathcal D^{c}\widehat F{}^{d}{}^{e}\big)\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{R(Q){}^{a}{}^{b}{}^{i}}\lambda{}_{i}\\
&+\frac{7i}{128}\big(\mathcal D^{e}\widehat F{}_{a}{}^{f}\big)\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}^{c}{}^{d}\lambda{}_{i} +\frac{i}{128}\big(\mathcal D^{e}\widehat F{}_{e}{}^{f}\big)\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{f}\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}^{c}{}^{d}\lambda{}_{i}\\
&-\frac{1}{128}\big(\mathcal D_{c}\widehat F{}_{a}{}_{b}\big)\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}^{c}\lambda{}_{i} +\frac{3}{32}\big(\mathcal D^{c}\widehat F{}_{b}{}_{c}\big)\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}_{a}\lambda{}_{i}\\
&-\frac{3i}{128}\big(\mathcal D_{a}\widehat F{}^{e}{}^{f}\big)\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}^{c}{}^{d}\lambda{}_{i} +\frac{1}{32}\big(\mathcal D_{a}\widehat F{}_{b}{}_{c}\big)\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}^{c}\lambda{}_{i}\\
&+\frac{i}{32}\big(\mathcal D^{e}\widehat F{}_{c}{}^{f}\big)\epsilon{}_{a}{}_{b}{}_{d}{}_{e}{}_{f}\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}^{c}{}^{d}\lambda{}_{i} -\frac{5i}{32}\big(\mathcal D_{c}\mathcal D_{b}\rho\big)\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}_{a}{}^{c}\lambda{}_{i}\\
&+\frac{7i}{64}\big(\mathcal D_{a}\mathcal D_{b}\rho\big)\overline{R(Q){}^{a}{}^{b}{}^{i}}\lambda{}_{i} +\frac{3}{64}\big(\mathcal D^{d}\mathcal D^{e}\rho\big)\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}^{c}\lambda{}_{i}\\
&+\frac{9i}{64}\big(\mathcal D_{b}\mathcal D_{c}\rho\big)\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}_{a}{}^{c}\lambda{}_{i} +\frac{31i}{3072}\widehat F{}^{e}{}^{f}\epsilon{}_{a}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\big(\mathcal D^{a}R(Q){}^{b}{}^{c}{}^{i}\big)}\gamma{}_{b}{}^{d}\lambda{}_{i}\\
&+\frac{2i}{3}T{}^{c}{}^{d}\big(\mathcal D^{e}T{}_{a}{}^{f}\big)\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\lambda{}^{i}}\gamma{}^{a}{}^{b}\lambda{}_{i} -\frac{i}{192}\widehat F{}^{e}{}^{f}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\big(\mathcal D^{a}R(Q){}^{b}{}^{c}{}^{i}\big)}\gamma{}_{a}{}^{d}\lambda{}_{i}
\end{aligned}
\tag{CTF-N2F2-4}
```

#### Scalar: $`n=3`$, explicit degree $`0`$

```math
\begin{aligned}
\mathcal N_{3}^{(0)}={}&3\big(\Box^c \rho\big)Y^2 +6Y{}^{i}{}^{j}\big(\mathcal D^{a}Y{}_{i}{}_{j}\big)\big(\mathcal D_{a}\rho\big)\\
&-\frac{1}{4}\big(\Box^c \rho\big)\widehat F^2 -4\widehat F{}^{a}{}^{b}T{}_{a}{}_{b}\widehat F^2\\
&+\frac{3}{2}\big(\mathcal D^{a}\rho\big)\big(\mathcal D_{a}\rho\big)\big(\Box^c \rho\big) +8\widehat F{}^{a}{}^{b}\big(\mathcal D^{c}\rho\big)\big(\mathcal D_{c}\rho\big)T{}_{a}{}_{b}\\
&-\frac{1}{8}\widehat F{}^{a}{}^{b}\widehat F{}^{c}{}^{d}\big(\mathcal D^{e}\widehat F{}_{e}{}^{f}\big)\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{f} -\widehat F{}^{a}{}^{b}\widehat F{}_{a}{}^{c}\big(\mathcal D_{b}\mathcal D_{c}\rho\big)\\
&+8\widehat F{}^{a}{}^{b}\widehat F{}_{a}{}^{c}\widehat F{}_{b}{}^{d}T{}_{c}{}_{d} -\widehat F{}^{a}{}^{b}\big(\mathcal D^{c}\widehat F{}_{a}{}_{c}\big)\big(\mathcal D_{b}\rho\big)\\
&-\widehat F{}^{a}{}^{b}\big(\mathcal D^{c}\widehat F{}_{a}{}_{b}\big)\big(\mathcal D_{c}\rho\big) -\frac{1}{2}\widehat F{}^{a}{}^{b}\big(\mathcal D^{c}\rho\big)\big(\mathcal D^{d}\mathcal D^{e}\rho\big)\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\\
&+\big(\mathcal D^{a}\rho\big)\big(\mathcal D^{b}\rho\big)\big(\mathcal D_{a}\mathcal D_{b}\rho\big)
\end{aligned}
\tag{CTF-N3F0}
```

#### Scalar: $`n=3`$, explicit degree $`2`$

```math
\begin{aligned}
\mathcal N_{3}^{(2)}={}&-8iDY{}^{i}{}^{j}\overline{\lambda{}_{i}}\lambda{}_{j} +\frac{3i}{8}R(V){}^{a}{}^{b}{}^{i}{}^{j}\widehat F{}_{a}{}_{b}\overline{\lambda{}_{i}}\lambda{}_{j}\\
&-\frac{i}{2}\big(\Box^c Y{}^{i}{}^{j}\big)\overline{\lambda{}_{i}}\lambda{}_{j} -\frac{5}{4}\big(\Box^c \rho\big)\overline{\lambda{}^{i}}\gamma{}^{a}\big(\mathcal D_{a}\lambda{}_{i}\big)\\
&+\frac{3i}{2}\big(\Box^c \rho\big)T{}_{a}{}_{b}\overline{\lambda{}^{i}}\gamma{}^{a}{}^{b}\lambda{}_{i} -\frac{3i}{2}Y{}^{i}{}^{j}\overline{\lambda{}_{i}}\big(\Box^c \lambda{}_{j}\big)\\
&-10Y{}^{i}{}^{j}\big(\mathcal D^{b}T{}_{a}{}_{b}\big)\overline{\lambda{}_{i}}\gamma{}^{a}\lambda{}_{j} -2iY{}^{i}{}^{j}T{}^{d}{}^{e}\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\lambda{}_{i}}\gamma{}^{a}{}^{b}\big(\mathcal D^{c}\lambda{}_{j}\big)\\
&-4Y{}^{i}{}^{j}T{}_{a}{}_{b}\overline{\lambda{}_{i}}\gamma{}^{a}\big(\mathcal D^{b}\lambda{}_{j}\big) -4Y{}^{i}{}^{j}T{}^{b}{}^{c}T{}^{d}{}^{e}\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\lambda{}_{i}}\gamma{}^{a}\lambda{}_{j}\\
&+\frac{8i}{3}Y{}^{i}{}^{j}T^2\overline{\lambda{}_{i}}\lambda{}_{j} -\frac{107}{96}Y{}_{i}{}^{j}\big(\mathcal D_{b}\rho\big)\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}_{a}\lambda{}_{j}\\
&-\frac{11i}{192}R(V){}^{a}{}^{b}{}^{i}{}^{j}Y{}_{i}{}^{k}\overline{\lambda{}_{j}}\gamma{}_{a}{}_{b}\lambda{}_{k} -\frac{i}{2}\big(\mathcal D^{a}Y{}^{i}{}^{j}\big)\overline{\lambda{}_{i}}\big(\mathcal D_{a}\lambda{}_{j}\big)\\
&+2\big(\mathcal D^{a}Y{}^{i}{}^{j}\big)T{}_{a}{}_{b}\overline{\lambda{}_{i}}\gamma{}^{b}\lambda{}_{j} -\frac{5}{4}\big(\mathcal D_{b}\rho\big)\overline{\lambda{}^{i}}\gamma{}^{a}\big(\mathcal D^{b}\mathcal D_{a}\lambda{}_{i}\big)\\
&+\frac{3i}{2}\big(\mathcal D^{c}\rho\big)\big(\mathcal D_{c}T{}_{a}{}_{b}\big)\overline{\lambda{}^{i}}\gamma{}^{a}{}^{b}\lambda{}_{i} +3i\big(\mathcal D_{c}\rho\big)T{}_{a}{}_{b}\overline{\lambda{}^{i}}\gamma{}^{a}{}^{b}\big(\mathcal D^{c}\lambda{}_{i}\big)\\
&+8i\big(\mathcal D^{a}\rho\big)\big(\mathcal D_{a}\rho\big)\overline{\chi{}^{i}}\lambda{}_{i} +2i\big(\mathcal D_{a}\rho\big)T{}_{b}{}_{c}\overline{\lambda{}^{i}}\gamma{}^{a}{}^{b}\big(\mathcal D^{c}\lambda{}_{i}\big)\\
&+2i\big(\mathcal D^{c}\rho\big)T{}_{b}{}_{c}\overline{\lambda{}^{i}}\gamma{}^{a}{}^{b}\big(\mathcal D_{a}\lambda{}_{i}\big) +i\big(\mathcal D^{c}\rho\big)\big(\mathcal D_{a}T{}_{b}{}_{c}\big)\overline{\lambda{}^{i}}\gamma{}^{a}{}^{b}\lambda{}_{i}\\
&+i\big(\mathcal D_{a}\rho\big)\big(\mathcal D^{c}T{}_{b}{}_{c}\big)\overline{\lambda{}^{i}}\gamma{}^{a}{}^{b}\lambda{}_{i} -\frac{73i}{192}Y{}_{i}{}^{j}\widehat F{}_{a}{}_{b}\overline{R(Q){}^{a}{}^{b}{}^{i}}\lambda{}_{j}\\
&-\frac{i}{64}R(M){}^{a}{}^{b}{}_{a}{}_{b}\widehat F{}_{c}{}_{d}\overline{\lambda{}^{i}}\gamma{}^{c}{}^{d}\lambda{}_{i} +\frac{i}{16}R(M){}^{a}{}^{b}{}_{a}{}^{c}\widehat F{}_{c}{}_{d}\overline{\lambda{}^{i}}\gamma{}_{b}{}^{d}\lambda{}_{i}\\
&-\frac{i}{64}R(M){}^{a}{}^{b}{}^{c}{}^{d}\widehat F{}_{c}{}_{d}\overline{\lambda{}^{i}}\gamma{}_{a}{}_{b}\lambda{}_{i} +\frac{i}{16}R(M){}^{a}{}^{b}{}_{a}{}^{c}\widehat F{}_{b}{}_{d}\overline{\lambda{}^{i}}\gamma{}_{c}{}^{d}\lambda{}_{i}\\
&-\frac{i}{16}R(M){}^{a}{}^{b}{}^{c}{}^{d}\widehat F{}_{b}{}_{d}\overline{\lambda{}^{i}}\gamma{}_{a}{}_{c}\lambda{}_{i} -\frac{i}{64}R(M){}^{a}{}^{b}{}^{c}{}^{d}\widehat F{}_{a}{}_{b}\overline{\lambda{}^{i}}\gamma{}_{c}{}_{d}\lambda{}_{i}\\
&-4i\widehat F{}^{c}{}^{d}T{}_{a}{}_{b}T{}_{c}{}_{d}\overline{\lambda{}^{i}}\gamma{}^{a}{}^{b}\lambda{}_{i} +32i\widehat F{}_{a}{}^{c}T{}_{b}{}^{d}T{}_{c}{}_{d}\overline{\lambda{}^{i}}\gamma{}^{a}{}^{b}\lambda{}_{i}\\
&-\frac{20i}{3}\widehat F{}_{a}{}_{b}T^2\overline{\lambda{}^{i}}\gamma{}^{a}{}^{b}\lambda{}_{i} +8i\widehat F{}^{c}{}^{d}T{}_{a}{}_{c}T{}_{b}{}_{d}\overline{\lambda{}^{i}}\gamma{}^{a}{}^{b}\lambda{}_{i}\\
&-\frac{29i}{24}\widehat F{}^{c}{}^{d}\big(\mathcal D^{e}T{}_{e}{}^{f}\big)\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{f}\overline{\lambda{}^{i}}\gamma{}^{a}{}^{b}\lambda{}_{i} +\frac{i}{4}\widehat F{}^{c}{}^{d}\big(\mathcal D^{e}T{}_{c}{}^{f}\big)\epsilon{}_{a}{}_{b}{}_{d}{}_{e}{}_{f}\overline{\lambda{}^{i}}\gamma{}^{a}{}^{b}\lambda{}_{i}
\end{aligned}
\tag{CTF-N3F2-1}
```

```math
\begin{aligned}
&-\frac{i}{12}\widehat F{}^{c}{}^{d}\big(\mathcal D_{c}T{}^{e}{}^{f}\big)\epsilon{}_{a}{}_{b}{}_{d}{}_{e}{}_{f}\overline{\lambda{}^{i}}\gamma{}^{a}{}^{b}\lambda{}_{i} +\frac{29i}{256}\widehat F{}_{a}{}_{b}\widehat F{}_{c}{}_{d}\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}^{c}{}^{d}\lambda{}_{i}\\
&+\frac{13}{128}\widehat F{}_{a}{}_{b}\big(\mathcal D_{c}\rho\big)\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}^{c}\lambda{}_{i} -\frac{1}{16}R(V){}^{a}{}^{b}{}^{i}{}^{j}\widehat F{}^{d}{}^{e}\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\lambda{}_{i}}\gamma{}^{c}\lambda{}_{j}\\
&-\frac{i}{8}\widehat F{}_{a}{}_{b}\overline{\lambda{}^{i}}\gamma{}^{a}{}^{b}\big(\Box^c \lambda{}_{i}\big) -\frac{1}{4}\big(\mathcal D_{a}\rho\big)\overline{\lambda{}^{i}}\gamma{}^{a}\big(\Box^c \lambda{}_{i}\big)\\
&-\frac{i}{8}\big(\Box^c \widehat F{}_{a}{}_{b}\big)\overline{\lambda{}^{i}}\gamma{}^{a}{}^{b}\lambda{}_{i} +\frac{i}{8}\big(\mathcal D^{c}\widehat F{}_{c}{}^{d}\big)T{}^{e}{}^{f}\epsilon{}_{a}{}_{b}{}_{d}{}_{e}{}_{f}\overline{\lambda{}^{i}}\gamma{}^{a}{}^{b}\lambda{}_{i}\\
&+\frac{7i}{24}\big(\mathcal D^{c}\widehat F{}^{d}{}^{e}\big)T{}_{d}{}^{f}\epsilon{}_{a}{}_{b}{}_{c}{}_{e}{}_{f}\overline{\lambda{}^{i}}\gamma{}^{a}{}^{b}\lambda{}_{i} -\frac{13i}{48}\big(\mathcal D^{c}\widehat F{}^{d}{}^{e}\big)T{}_{c}{}^{f}\epsilon{}_{a}{}_{b}{}_{d}{}_{e}{}_{f}\overline{\lambda{}^{i}}\gamma{}^{a}{}^{b}\lambda{}_{i}\\
&+\frac{7i}{3}\big(\mathcal D_{a}\mathcal D^{c}\rho\big)T{}_{b}{}_{c}\overline{\lambda{}^{i}}\gamma{}^{a}{}^{b}\lambda{}_{i} -\frac{i}{3}\big(\mathcal D^{c}\mathcal D_{a}\rho\big)T{}_{b}{}_{c}\overline{\lambda{}^{i}}\gamma{}^{a}{}^{b}\lambda{}_{i}\\
&-\frac{i}{6}\widehat F{}_{a}{}^{c}\big(\mathcal D^{d}T{}^{e}{}^{f}\big)\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\lambda{}^{i}}\gamma{}^{a}{}^{b}\lambda{}_{i} -\frac{37i}{384}R(V){}^{a}{}^{b}{}^{i}{}^{j}Y{}_{i}{}_{j}\overline{\lambda{}^{k}}\gamma{}_{a}{}_{b}\lambda{}_{k}\\
&-\frac{i}{2}Y{}^{i}{}^{j}\overline{\big(\mathcal D^{a}\lambda{}_{i}\big)}\big(\mathcal D_{a}\lambda{}_{j}\big) -\frac{i}{4}\big(\mathcal D^{c}\widehat F{}_{a}{}_{b}\big)\overline{\lambda{}^{i}}\gamma{}^{a}{}^{b}\big(\mathcal D_{c}\lambda{}_{i}\big)\\
&-\frac{1}{4}\big(\mathcal D_{b}\mathcal D_{a}\rho\big)\overline{\lambda{}^{i}}\gamma{}^{a}\big(\mathcal D^{b}\lambda{}_{i}\big) +i\widehat F{}^{a}{}^{b}T{}^{d}{}^{e}\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\lambda{}^{i}}\big(\mathcal D^{c}\lambda{}_{i}\big)\\
&+i\widehat F{}^{c}{}^{d}T{}^{e}{}^{f}\epsilon{}_{a}{}_{b}{}_{d}{}_{e}{}_{f}\overline{\lambda{}^{i}}\gamma{}^{a}{}^{b}\big(\mathcal D_{c}\lambda{}_{i}\big) -\frac{i}{2}\widehat F{}^{c}{}^{d}T{}_{c}{}^{f}\epsilon{}_{a}{}_{b}{}_{d}{}_{e}{}_{f}\overline{\lambda{}^{i}}\gamma{}^{a}{}^{b}\big(\mathcal D^{e}\lambda{}_{i}\big)\\
&+4\widehat F{}^{b}{}^{c}T{}_{a}{}_{c}\overline{\lambda{}^{i}}\gamma{}^{a}\big(\mathcal D_{b}\lambda{}_{i}\big) -2\widehat F{}^{b}{}^{c}T{}_{b}{}_{c}\overline{\lambda{}^{i}}\gamma{}^{a}\big(\mathcal D_{a}\lambda{}_{i}\big)\\
&+\frac{i}{4}\widehat F{}^{c}{}^{d}T{}_{e}{}^{f}\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{f}\overline{\lambda{}^{i}}\gamma{}^{a}{}^{b}\big(\mathcal D^{e}\lambda{}_{i}\big) +\frac{5i}{6}\widehat F{}_{a}{}^{c}T{}^{e}{}^{f}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\lambda{}^{i}}\gamma{}^{a}{}^{b}\big(\mathcal D^{d}\lambda{}_{i}\big)\\
&+\frac{3i}{4}\big(\mathcal D^{c}\widehat F{}_{a}{}^{d}\big)T{}^{e}{}^{f}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\lambda{}^{i}}\gamma{}^{a}{}^{b}\lambda{}_{i} -iD\widehat F{}_{a}{}_{b}\overline{\lambda{}^{i}}\gamma{}^{a}{}^{b}\lambda{}_{i}\\
&+8iY{}^{i}{}^{j}\widehat F{}_{a}{}_{b}\overline{\chi{}_{i}}\gamma{}^{a}{}^{b}\lambda{}_{j} -2\widehat F{}^{b}{}^{c}\widehat F{}^{d}{}^{e}\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\chi{}^{i}}\gamma{}^{a}\lambda{}_{i}\\
&-\frac{167i}{9}Y^2\overline{\chi{}^{i}}\lambda{}_{i} +\frac{46i}{9}Y{}^{i}{}^{j}Y{}_{i}{}^{k}\overline{\chi{}_{j}}\lambda{}_{k}\\
&-\frac{1}{128}Y{}_{i}{}^{j}\widehat F{}^{d}{}^{e}\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}^{c}\lambda{}_{j} -\frac{5i}{48}Y{}_{i}{}^{j}\widehat F{}_{b}{}_{c}\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}_{a}{}^{c}\lambda{}_{j}\\
&+\frac{17i}{512}\widehat F^2\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}_{a}{}_{b}\lambda{}_{i} -\frac{1}{8}\widehat F{}^{b}{}^{c}\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\big(\mathcal D^{d}\lambda{}^{i}\big)}\gamma{}^{a}\big(\mathcal D^{e}\lambda{}_{i}\big)\\
&+\frac{i}{8}\widehat F{}_{a}{}_{b}\overline{\big(\mathcal D^{c}\lambda{}^{i}\big)}\gamma{}^{a}{}^{b}\big(\mathcal D_{c}\lambda{}_{i}\big) -\frac{i}{2}\widehat F{}_{a}{}^{c}\overline{\big(\mathcal D_{b}\lambda{}^{i}\big)}\gamma{}^{a}{}^{b}\big(\mathcal D_{c}\lambda{}_{i}\big)
\end{aligned}
\tag{CTF-N3F2-2}
```

```math
\begin{aligned}
&-\frac{i}{4}\widehat F{}^{a}{}^{b}\overline{\big(\mathcal D_{a}\lambda{}^{i}\big)}\big(\mathcal D_{b}\lambda{}_{i}\big) +\frac{i}{2}Y{}^{i}{}^{j}\overline{\big(\mathcal D_{a}\lambda{}_{i}\big)}\gamma{}^{a}{}^{b}\big(\mathcal D_{b}\lambda{}_{j}\big)\\
&-\frac{11i}{96}Y^2\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}_{a}{}_{b}\lambda{}_{i} +\frac{23i}{192}Y{}_{i}{}^{j}Y{}_{j}{}^{k}\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}_{a}{}_{b}\lambda{}_{k}\\
&-\frac{35i}{256}\big(\mathcal D^{c}\rho\big)\big(\mathcal D_{c}\rho\big)\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}_{a}{}_{b}\lambda{}_{i} +\big(\mathcal D_{b}\rho\big)\overline{\big(\mathcal D_{a}\lambda{}^{i}\big)}\gamma{}^{a}\big(\mathcal D^{b}\lambda{}_{i}\big)\\
&-\frac{7i}{48}Y{}_{i}{}^{j}\big(\mathcal D^{e}\rho\big)\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}^{c}{}^{d}\lambda{}_{j} -\frac{i}{3}\widehat F{}^{c}{}^{d}T{}_{a}{}^{f}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\lambda{}^{i}}\gamma{}^{a}{}^{b}\big(\mathcal D^{e}\lambda{}_{i}\big)\\
&-\frac{i}{12}\widehat F{}^{c}{}^{d}\big(\mathcal D^{e}T{}_{a}{}^{f}\big)\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\lambda{}^{i}}\gamma{}^{a}{}^{b}\lambda{}_{i} +\frac{i}{12}\widehat F{}^{c}{}^{d}\big(\mathcal D_{a}T{}^{e}{}^{f}\big)\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\lambda{}^{i}}\gamma{}^{a}{}^{b}\lambda{}_{i}\\
&-\frac{i}{4}\big(\mathcal D^{a}\widehat F{}_{a}{}^{b}\big)\overline{\lambda{}^{i}}\big(\mathcal D_{b}\lambda{}_{i}\big) +\frac{i}{4}\big(\mathcal D^{c}\widehat F{}_{a}{}_{c}\big)\overline{\lambda{}^{i}}\gamma{}^{a}{}^{b}\big(\mathcal D_{b}\lambda{}_{i}\big)\\
&+\frac{i}{2}\big(\mathcal D^{a}Y{}^{i}{}^{j}\big)\overline{\lambda{}_{i}}\gamma{}_{a}{}^{b}\big(\mathcal D_{b}\lambda{}_{j}\big) -\frac{1}{4}\big(\mathcal D_{a}\mathcal D_{b}\rho\big)\overline{\lambda{}^{i}}\gamma{}^{a}\big(\mathcal D^{b}\lambda{}_{i}\big)\\
&-\frac{i}{8}\big(\mathcal D^{d}\mathcal D^{e}\rho\big)\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\lambda{}^{i}}\gamma{}^{a}{}^{b}\big(\mathcal D^{c}\lambda{}_{i}\big) -\frac{13i}{12}\widehat F{}^{c}{}^{d}T{}^{e}{}^{f}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\lambda{}^{i}}\gamma{}^{a}{}^{b}\big(\mathcal D_{a}\lambda{}_{i}\big)\\
&+\frac{i}{8}\big(\mathcal D^{c}\widehat F{}^{d}{}^{e}\big)T{}_{a}{}^{f}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\lambda{}^{i}}\gamma{}^{a}{}^{b}\lambda{}_{i} -\frac{5i}{64}\widehat F{}_{b}{}^{d}\widehat F{}_{c}{}_{d}\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}_{a}{}^{c}\lambda{}_{i}\\
&+\frac{3i}{128}\widehat F{}_{a}{}_{c}\widehat F{}_{b}{}_{d}\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}^{c}{}^{d}\lambda{}_{i} -\frac{9}{256}\widehat F{}^{c}{}^{d}\widehat F{}^{e}{}^{f}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}_{a}\lambda{}_{i}\\
&+\frac{9}{64}\widehat F{}_{a}{}_{c}\big(\mathcal D_{b}\rho\big)\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}^{c}\lambda{}_{i} +\frac{11}{64}\widehat F{}_{b}{}^{c}\big(\mathcal D_{c}\rho\big)\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}_{a}\lambda{}_{i}\\
&-\frac{3i}{512}\widehat F{}^{e}{}^{f}\big(\mathcal D_{a}\rho\big)\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}^{c}{}^{d}\lambda{}_{i} -\frac{15i}{256}\widehat F{}^{e}{}^{f}\big(\mathcal D_{c}\rho\big)\epsilon{}_{a}{}_{b}{}_{d}{}_{e}{}_{f}\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}^{c}{}^{d}\lambda{}_{i}\\
&-\frac{9i}{256}\widehat F{}^{d}{}^{e}\big(\mathcal D^{f}\rho\big)\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}_{a}{}^{c}\lambda{}_{i} +\frac{5i}{256}\widehat F{}^{c}{}^{d}\big(\mathcal D^{e}\rho\big)\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{R(Q){}^{a}{}^{b}{}^{i}}\lambda{}_{i}\\
&-\frac{i}{16}\widehat F{}^{e}{}^{f}\big(\mathcal D_{e}\rho\big)\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{f}\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}^{c}{}^{d}\lambda{}_{i} -\frac{15i}{256}\widehat F{}_{a}{}^{e}\big(\mathcal D^{f}\rho\big)\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}^{c}{}^{d}\lambda{}_{i}\\
&-\frac{i}{4}\widehat F{}_{a}{}^{c}\overline{\lambda{}^{i}}\gamma{}^{a}{}^{b}\big(\mathcal D_{b}\mathcal D_{c}\lambda{}_{i}\big) +\frac{i}{128}\widehat F{}_{c}{}^{e}\big(\mathcal D^{f}\rho\big)\epsilon{}_{a}{}_{b}{}_{d}{}_{e}{}_{f}\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}^{c}{}^{d}\lambda{}_{i}\\
&-\frac{i}{4}\widehat F{}_{a}{}^{c}\overline{\lambda{}^{i}}\gamma{}^{a}{}^{b}\big(\mathcal D_{c}\mathcal D_{b}\lambda{}_{i}\big) -\frac{1}{4}\big(\mathcal D_{b}\rho\big)\overline{\lambda{}^{i}}\gamma{}^{a}\big(\mathcal D_{a}\mathcal D^{b}\lambda{}_{i}\big)\\
&+\frac{13i}{64}\big(\mathcal D_{b}\rho\big)\big(\mathcal D_{c}\rho\big)\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}_{a}{}^{c}\lambda{}_{i}
\end{aligned}
\tag{CTF-N3F2-3}
```

#### Scalar: $`n=4`$, explicit degree $`0`$

```math
\begin{aligned}
\mathcal N_{4}^{(0)}={}&\frac{3}{4}Y^2\widehat F^2 -\frac{5}{2}(Y^2)^{2}\\
&-\frac{9}{2}\big(\mathcal D^{a}\rho\big)\big(\mathcal D_{a}\rho\big)Y^2 +\frac{3}{8}\big(\mathcal D^{a}\rho\big)\big(\mathcal D_{a}\rho\big)\widehat F^2\\
&-\frac{3}{8}\big(\mathcal D^{a}\rho\big)\big(\mathcal D_{a}\rho\big)\big(\mathcal D^{b}\rho\big)\big(\mathcal D_{b}\rho\big) +\frac{3}{2}\widehat F{}^{a}{}^{b}\widehat F{}_{a}{}^{c}\big(\mathcal D_{b}\rho\big)\big(\mathcal D_{c}\rho\big)\\
&+\frac{3}{32}(\widehat F^2)^{2} -\frac{3}{8}\widehat F{}^{a}{}^{b}\widehat F{}_{a}{}^{c}\widehat F{}_{b}{}^{d}\widehat F{}_{c}{}_{d}\\
&+2Y{}^{i}{}^{j}Y{}_{i}{}^{k}Y{}_{j}{}^{l}Y{}_{k}{}_{l}
\end{aligned}
\tag{CTF-N4F0}
```

#### Scalar: $`n=4`$, explicit degree $`2`$

```math
\begin{aligned}
\mathcal N_{4}^{(2)}={}&\frac{9i}{4}Y{}^{i}{}^{j}\big(\Box^c \rho\big)\overline{\lambda{}_{i}}\lambda{}_{j} +\frac{9i}{4}\big(\mathcal D^{a}Y{}^{i}{}^{j}\big)\big(\mathcal D_{a}\rho\big)\overline{\lambda{}_{i}}\lambda{}_{j}\\
&-\frac{3}{16}\widehat F^2\overline{\lambda{}^{i}}\gamma{}^{a}\big(\mathcal D_{a}\lambda{}_{i}\big) +\frac{15i}{8}T{}_{a}{}_{b}\widehat F^2\overline{\lambda{}^{i}}\gamma{}^{a}{}^{b}\lambda{}_{i}\\
&+\frac{3i}{8}Y{}^{i}{}^{j}\widehat F{}^{c}{}^{d}\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\lambda{}_{i}}\gamma{}^{a}{}^{b}\big(\mathcal D^{e}\lambda{}_{j}\big) +\frac{9}{2}Y{}^{i}{}^{j}\widehat F{}^{b}{}^{c}T{}^{d}{}^{e}\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\lambda{}_{i}}\gamma{}^{a}\lambda{}_{j}\\
&-3iY{}^{i}{}^{j}\widehat F{}^{a}{}^{b}T{}_{a}{}_{b}\overline{\lambda{}_{i}}\lambda{}_{j} +2Y^2\overline{\lambda{}^{i}}\gamma{}^{a}\big(\mathcal D_{a}\lambda{}_{i}\big)\\
&+\frac{9i}{4}T{}_{a}{}_{b}Y^2\overline{\lambda{}^{i}}\gamma{}^{a}{}^{b}\lambda{}_{i} +\frac{1}{2}Y{}^{i}{}^{j}Y{}_{i}{}^{k}\overline{\lambda{}_{j}}\gamma{}^{a}\big(\mathcal D_{a}\lambda{}_{k}\big)\\
&-\frac{3i}{2}Y{}^{i}{}^{j}Y{}_{i}{}^{k}T{}_{a}{}_{b}\overline{\lambda{}_{j}}\gamma{}^{a}{}^{b}\lambda{}_{k} +\frac{15}{8}\big(\mathcal D^{b}\rho\big)\big(\mathcal D_{b}\rho\big)\overline{\lambda{}^{i}}\gamma{}^{a}\big(\mathcal D_{a}\lambda{}_{i}\big)\\
&-\frac{9i}{4}\big(\mathcal D^{c}\rho\big)\big(\mathcal D_{c}\rho\big)T{}_{a}{}_{b}\overline{\lambda{}^{i}}\gamma{}^{a}{}^{b}\lambda{}_{i} +\frac{9i}{2}Y{}^{i}{}^{j}\big(\mathcal D_{a}\rho\big)\overline{\lambda{}_{i}}\big(\mathcal D^{a}\lambda{}_{j}\big)\\
&+\frac{3}{4}\widehat F{}_{a}{}^{b}\widehat F{}_{b}{}^{c}\overline{\lambda{}^{i}}\gamma{}^{a}\big(\mathcal D_{c}\lambda{}_{i}\big) +\frac{3i}{16}\widehat F{}^{c}{}^{d}\widehat F{}^{e}{}^{f}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\lambda{}^{i}}\gamma{}^{a}{}^{b}\big(\mathcal D_{a}\lambda{}_{i}\big)\\
&-\frac{3i}{32}\widehat F{}^{a}{}^{b}\widehat F{}^{c}{}^{d}\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\lambda{}^{i}}\big(\mathcal D^{e}\lambda{}_{i}\big) +\frac{3i}{4}\widehat F{}_{a}{}^{c}\big(\mathcal D_{c}\rho\big)\overline{\lambda{}^{i}}\gamma{}^{a}{}^{b}\big(\mathcal D_{b}\lambda{}_{i}\big)\\
&+\frac{3i}{8}\widehat F{}_{a}{}_{b}\big(\mathcal D_{c}\rho\big)\overline{\lambda{}^{i}}\gamma{}^{a}{}^{b}\big(\mathcal D^{c}\lambda{}_{i}\big) -\frac{3i}{32}\widehat F{}^{c}{}^{d}\big(\mathcal D^{e}\widehat F{}_{a}{}^{f}\big)\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\lambda{}^{i}}\gamma{}^{a}{}^{b}\lambda{}_{i}\\
&+\frac{i}{2}\widehat F{}^{c}{}^{d}\big(\mathcal D^{e}\rho\big)T{}_{a}{}^{f}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\lambda{}^{i}}\gamma{}^{a}{}^{b}\lambda{}_{i} +\frac{3i}{8}\widehat F{}_{a}{}^{c}\big(\mathcal D_{b}\mathcal D_{c}\rho\big)\overline{\lambda{}^{i}}\gamma{}^{a}{}^{b}\lambda{}_{i}\\
&+\frac{3i}{16}\widehat F{}_{a}{}_{b}\big(\Box^c \rho\big)\overline{\lambda{}^{i}}\gamma{}^{a}{}^{b}\lambda{}_{i} +\frac{9i}{4}\widehat F{}_{a}{}_{b}\widehat F{}^{c}{}^{d}T{}_{c}{}_{d}\overline{\lambda{}^{i}}\gamma{}^{a}{}^{b}\lambda{}_{i}\\
&-9i\widehat F{}_{a}{}^{c}\widehat F{}_{c}{}^{d}T{}_{b}{}_{d}\overline{\lambda{}^{i}}\gamma{}^{a}{}^{b}\lambda{}_{i} -\frac{3i}{2}\widehat F{}_{a}{}^{c}\widehat F{}_{b}{}^{d}T{}_{c}{}_{d}\overline{\lambda{}^{i}}\gamma{}^{a}{}^{b}\lambda{}_{i}\\
&-\frac{17i}{16}\widehat F{}^{c}{}^{d}\big(\mathcal D_{a}\rho\big)T{}^{e}{}^{f}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\lambda{}^{i}}\gamma{}^{a}{}^{b}\lambda{}_{i} -\frac{13i}{16}\widehat F{}^{c}{}^{d}\big(\mathcal D^{e}\rho\big)T{}_{e}{}^{f}\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{f}\overline{\lambda{}^{i}}\gamma{}^{a}{}^{b}\lambda{}_{i}\\
&+\frac{3i}{4}\widehat F{}_{a}{}^{c}\big(\mathcal D_{b}\rho\big)\overline{\lambda{}^{i}}\gamma{}^{a}{}^{b}\big(\mathcal D_{c}\lambda{}_{i}\big) -\frac{17i}{16}\widehat F{}^{c}{}^{d}\big(\mathcal D_{c}\rho\big)T{}^{e}{}^{f}\epsilon{}_{a}{}_{b}{}_{d}{}_{e}{}_{f}\overline{\lambda{}^{i}}\gamma{}^{a}{}^{b}\lambda{}_{i}\\
&+\frac{3}{4}\big(\mathcal D^{a}Y{}^{i}{}^{j}\big)\widehat F{}_{a}{}_{b}\overline{\lambda{}_{i}}\gamma{}^{b}\lambda{}_{j} +\frac{3i}{8}\widehat F{}_{a}{}^{c}\big(\mathcal D_{c}\mathcal D_{b}\rho\big)\overline{\lambda{}^{i}}\gamma{}^{a}{}^{b}\lambda{}_{i}\\
&+\frac{i}{2}\widehat F{}^{c}{}^{d}\big(\mathcal D^{e}\rho\big)T{}_{c}{}^{f}\epsilon{}_{a}{}_{b}{}_{d}{}_{e}{}_{f}\overline{\lambda{}^{i}}\gamma{}^{a}{}^{b}\lambda{}_{i} +\frac{3}{4}Y{}^{i}{}^{j}\big(\mathcal D^{b}\widehat F{}_{a}{}_{b}\big)\overline{\lambda{}_{i}}\gamma{}^{a}\lambda{}_{j}\\
&+\frac{3i}{64}\widehat F{}^{c}{}^{d}\big(\mathcal D^{e}\widehat F{}_{e}{}^{f}\big)\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{f}\overline{\lambda{}^{i}}\gamma{}^{a}{}^{b}\lambda{}_{i} +\frac{3i}{8}\big(\mathcal D^{c}\widehat F{}_{a}{}_{c}\big)\big(\mathcal D_{b}\rho\big)\overline{\lambda{}^{i}}\gamma{}^{a}{}^{b}\lambda{}_{i}
\end{aligned}
\tag{CTF-N4F2-1}
```

```math
\begin{aligned}
&+\frac{3}{2}Y{}^{i}{}^{j}\big(\mathcal D^{a}Y{}_{i}{}^{k}\big)\overline{\lambda{}_{j}}\gamma{}_{a}\lambda{}_{k} +\frac{3}{4}\big(\mathcal D_{a}\rho\big)\big(\mathcal D_{b}\rho\big)\overline{\lambda{}^{i}}\gamma{}^{a}\big(\mathcal D^{b}\lambda{}_{i}\big)\\
&+\frac{3i}{8}\big(\mathcal D^{c}\widehat F{}_{a}{}_{b}\big)\big(\mathcal D_{c}\rho\big)\overline{\lambda{}^{i}}\gamma{}^{a}{}^{b}\lambda{}_{i} -3i\big(\mathcal D_{a}\rho\big)\big(\mathcal D^{c}\rho\big)T{}_{b}{}_{c}\overline{\lambda{}^{i}}\gamma{}^{a}{}^{b}\lambda{}_{i}\\
&+\frac{3i}{16}\big(\mathcal D^{c}\rho\big)\big(\mathcal D^{d}\mathcal D^{e}\rho\big)\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\lambda{}^{i}}\gamma{}^{a}{}^{b}\lambda{}_{i} -\frac{3i}{32}\widehat F{}^{c}{}^{d}\big(\mathcal D^{e}\widehat F{}_{c}{}^{f}\big)\epsilon{}_{a}{}_{b}{}_{d}{}_{e}{}_{f}\overline{\lambda{}^{i}}\gamma{}^{a}{}^{b}\lambda{}_{i}
\end{aligned}
\tag{CTF-N4F2-2}
```

#### Scalar: $`n=5`$, explicit degree $`2`$

```math
\begin{aligned}
\mathcal N_{5}^{(2)}={}&\frac{3i}{4}Y{}^{i}{}^{j}\widehat F^2\overline{\lambda{}_{i}}\lambda{}_{j} -\frac{11i}{2}Y{}^{i}{}^{j}Y^2\overline{\lambda{}_{i}}\lambda{}_{j}\\
&-\frac{9i}{2}Y{}^{i}{}^{j}\big(\mathcal D^{a}\rho\big)\big(\mathcal D_{a}\rho\big)\overline{\lambda{}_{i}}\lambda{}_{j} -\frac{3i}{8}\widehat F{}_{a}{}_{b}\big(\mathcal D^{c}\rho\big)\big(\mathcal D_{c}\rho\big)\overline{\lambda{}^{i}}\gamma{}^{a}{}^{b}\lambda{}_{i}\\
&-\frac{3i}{2}\widehat F{}_{a}{}^{c}\big(\mathcal D_{b}\rho\big)\big(\mathcal D_{c}\rho\big)\overline{\lambda{}^{i}}\gamma{}^{a}{}^{b}\lambda{}_{i} -\frac{3i}{16}\widehat F{}_{a}{}_{b}\widehat F^2\overline{\lambda{}^{i}}\gamma{}^{a}{}^{b}\lambda{}_{i}\\
&-\frac{3}{8}Y{}^{i}{}^{j}\widehat F{}^{b}{}^{c}\widehat F{}^{d}{}^{e}\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\lambda{}_{i}}\gamma{}^{a}\lambda{}_{j} +\frac{3i}{4}\widehat F{}_{a}{}^{c}\widehat F{}_{b}{}^{d}\widehat F{}_{c}{}_{d}\overline{\lambda{}^{i}}\gamma{}^{a}{}^{b}\lambda{}_{i}\\
&-\frac{9i}{8}\widehat F{}_{a}{}_{b}Y^2\overline{\lambda{}^{i}}\gamma{}^{a}{}^{b}\lambda{}_{i} +\frac{3i}{4}Y{}^{i}{}^{j}Y{}_{i}{}^{k}\widehat F{}_{a}{}_{b}\overline{\lambda{}_{j}}\gamma{}^{a}{}^{b}\lambda{}_{k}\\
&+5iY{}^{i}{}^{j}Y{}_{i}{}^{k}Y{}_{j}{}^{l}\overline{\lambda{}_{k}}\lambda{}_{l}
\end{aligned}
\tag{CTF-N5F2}
```

### 5.4 Constrained vector

```math
\boxed{E_{\log}^{a}\big|_{\leq2}=\Big[\sum_{n=0}^{5}\rho^{-n}(\mathcal E_{n}^{(0)a}+\mathcal E_{n}^{(2)a})\Big]_{\leq2}}
\tag{CTF-E}
```

The absent coefficients are $`\mathcal E_{5}^{(0)a}=0`$.

#### Constrained vector: $`n=0`$, explicit degree $`0`$

```math
\begin{aligned}
\mathcal E_{0}^{(0)a}={}&-\frac{1}{12}R(V){}^{b}{}^{c}{}^{i}{}^{j}R(V){}^{d}{}^{e}{}_{i}{}_{j}\epsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{e} -\frac{43}{9}R(M){}^{b}{}^{c}{}^{a}{}_{b}T{}^{d}{}^{e}T{}^{f}{}^{g}\epsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g}\\
&+\frac{49}{18}R(M){}^{a}{}^{b}{}_{b}{}^{c}T{}^{d}{}^{e}T{}^{f}{}^{g}\epsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g} -6R(M){}^{b}{}^{c}{}^{d}{}^{e}T{}^{a}{}^{f}T{}_{b}{}^{g}\epsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g}\\
&+R(M){}^{b}{}^{c}{}^{d}{}^{e}T{}^{a}{}_{b}T{}^{f}{}^{g}\epsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g} -\frac{43}{6}R(M){}^{b}{}^{c}{}^{d}{}^{e}T{}^{a}{}_{d}T{}^{f}{}^{g}\epsilon{}_{b}{}_{c}{}_{e}{}_{f}{}_{g}\\
&-\frac{2}{3}R(M){}^{b}{}^{c}{}^{d}{}^{e}T{}^{a}{}^{f}T{}_{f}{}^{g}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{g} -\frac{13}{36}R(M){}^{b}{}^{c}{}_{b}{}_{c}T{}^{d}{}^{e}T{}^{f}{}^{g}\epsilon{}^{a}{}_{d}{}_{e}{}_{f}{}_{g}\\
&+\frac{106}{9}R(M){}^{b}{}^{c}{}^{d}{}^{e}T{}_{b}{}^{f}T{}_{d}{}^{g}\epsilon{}^{a}{}_{c}{}_{e}{}_{f}{}_{g} +\frac{19}{9}R(M){}^{b}{}^{c}{}^{d}{}^{e}T{}_{b}{}_{d}T{}^{f}{}^{g}\epsilon{}^{a}{}_{c}{}_{e}{}_{f}{}_{g}\\
&+\frac{35}{18}R(M){}^{b}{}^{c}{}^{d}{}^{e}T{}_{d}{}_{e}T{}^{f}{}^{g}\epsilon{}^{a}{}_{b}{}_{c}{}_{f}{}_{g} -\frac{16}{9}R(M){}^{b}{}^{c}{}^{d}{}^{e}T{}_{d}{}^{f}T{}_{f}{}^{g}\epsilon{}^{a}{}_{b}{}_{c}{}_{e}{}_{g}\\
&+\frac{2}{3}R(M){}^{b}{}^{c}{}^{d}{}^{e}T{}_{b}{}^{f}T{}_{f}{}^{g}\epsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{g} -\frac{11}{18}R(M){}^{b}{}^{c}{}^{d}{}^{e}\epsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{e}T^2\\
&+11R(M){}^{b}{}^{c}{}^{d}{}^{e}T{}^{a}{}^{f}T{}_{d}{}^{g}\epsilon{}_{b}{}_{c}{}_{e}{}_{f}{}_{g} +\frac{20}{9}R(M){}^{b}{}^{c}{}^{d}{}^{e}T{}_{d}{}^{f}T{}_{e}{}^{g}\epsilon{}^{a}{}_{b}{}_{c}{}_{f}{}_{g}\\
&+\frac{109000}{81}T{}^{a}{}^{b}T{}_{b}{}^{c}T{}^{d}{}^{e}T{}^{f}{}^{g}\epsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g} -\frac{81280}{81}T{}^{b}{}^{c}T{}_{b}{}^{d}T{}_{c}{}^{e}T{}^{f}{}^{g}\epsilon{}^{a}{}_{d}{}_{e}{}_{f}{}_{g}\\
&+\frac{20320}{81}T{}^{b}{}^{c}T{}^{d}{}^{e}\epsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{e}T^2 -\frac{128}{9}\big(\mathcal D^{b}T{}^{a}{}_{b}\big)T^2\\
&-\frac{2048}{3}T{}^{b}{}^{c}T{}_{b}{}^{d}\big(\mathcal D_{c}T{}^{a}{}_{d}\big) +\frac{2048}{3}T{}^{a}{}^{b}T{}_{b}{}^{c}\big(\mathcal D^{d}T{}_{c}{}_{d}\big)\\
&-\frac{2048}{3}T{}^{a}{}^{b}T{}^{c}{}^{d}\big(\mathcal D_{c}T{}_{b}{}_{d}\big) -\frac{256}{9}T{}^{a}{}^{b}T{}^{c}{}^{d}\big(\mathcal D_{b}T{}_{c}{}_{d}\big)\\
&+2\big(\mathcal D^{b}R(M){}^{c}{}^{d}{}_{c}{}_{d}\big)T{}^{a}{}_{b} +4\big(\mathcal D^{b}R(M){}_{b}{}^{c}{}_{c}{}^{d}\big)T{}^{a}{}_{d}\\
&-4\big(\mathcal D^{b}R(M){}^{c}{}^{d}{}^{a}{}_{c}\big)T{}_{b}{}_{d} -4\big(\mathcal D^{b}R(M){}_{b}{}^{c}{}^{a}{}^{d}\big)T{}_{c}{}_{d}\\
&+4\big(\mathcal D^{a}R(M){}^{b}{}^{c}{}_{b}{}^{d}\big)T{}_{c}{}_{d} -4\big(\mathcal D^{b}R(M){}^{a}{}^{c}{}_{c}{}^{d}\big)T{}_{b}{}_{d}\\
&+2\big(\mathcal D^{b}R(M){}^{a}{}_{b}{}^{c}{}^{d}\big)T{}_{c}{}_{d} -\frac{110}{9}T{}^{a}{}^{b}\big(\mathcal D^{c}\mathcal D^{d}T{}^{e}{}^{f}\big)\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\\
&+\frac{50}{9}T{}^{b}{}^{c}\big(\mathcal D_{b}\mathcal D^{d}T{}^{e}{}^{f}\big)\epsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f} +\frac{44}{3}T{}^{b}{}^{c}\big(\mathcal D^{d}\mathcal D^{e}T{}_{b}{}^{f}\big)\epsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f}\\
&-16T{}^{b}{}^{c}\big(\mathcal D^{d}\mathcal D^{e}T{}^{a}{}^{f}\big)\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f} +\frac{176}{9}T{}^{b}{}^{c}\big(\mathcal D^{d}\mathcal D^{e}T{}_{d}{}^{f}\big)\epsilon{}^{a}{}_{b}{}_{c}{}_{e}{}_{f}
\end{aligned}
\tag{CTF-E0F0-1}
```

```math
\begin{aligned}
&-\frac{16}{9}T{}^{b}{}^{c}\big(\mathcal D^{a}\mathcal D^{d}T{}^{e}{}^{f}\big)\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f} +\frac{268}{9}T{}^{b}{}^{c}\big(\mathcal D^{d}\mathcal D^{e}T{}_{e}{}^{f}\big)\epsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{f}\\
&-\frac{50}{9}T{}^{b}{}^{c}\big(\mathcal D^{d}\mathcal D^{a}T{}^{e}{}^{f}\big)\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f} -\frac{110}{9}T{}^{b}{}^{c}\big(\mathcal D^{d}\mathcal D_{b}T{}^{e}{}^{f}\big)\epsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f}\\
&+2R(M){}^{b}{}^{c}{}^{d}{}^{e}T{}_{b}{}^{f}T{}_{c}{}^{g}\epsilon{}^{a}{}_{d}{}_{e}{}_{f}{}_{g} +\frac{5}{6}R(M){}^{b}{}^{c}{}^{d}{}^{e}T{}_{b}{}_{c}T{}^{f}{}^{g}\epsilon{}^{a}{}_{d}{}_{e}{}_{f}{}_{g}\\
&+\frac{22}{3}T{}^{b}{}^{c}\big(\Box^c T{}^{e}{}^{f}\big)\epsilon{}^{a}{}_{b}{}_{c}{}_{e}{}_{f} -\frac{64}{3}\big(\mathcal D^{b}D\big)T{}^{a}{}_{b}\\
&-\frac{64}{3}D\big(\mathcal D^{b}T{}^{a}{}_{b}\big) -\frac{431}{24}\big(\mathcal D^{b}T{}^{a}{}^{c}\big)\big(\mathcal D^{d}T{}^{e}{}^{f}\big)\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\\
&+\frac{187}{8}\big(\mathcal D^{b}T{}^{c}{}^{d}\big)\big(\mathcal D_{c}T{}^{e}{}^{f}\big)\epsilon{}^{a}{}_{b}{}_{d}{}_{e}{}_{f} -\frac{431}{12}\big(\mathcal D^{b}T{}^{c}{}^{d}\big)\big(\mathcal D^{e}T{}_{c}{}^{f}\big)\epsilon{}^{a}{}_{b}{}_{d}{}_{e}{}_{f}\\
&-\frac{241}{8}\big(\mathcal D^{b}T{}_{b}{}^{c}\big)\big(\mathcal D^{d}T{}^{e}{}^{f}\big)\epsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f} -\frac{191}{24}\big(\mathcal D^{a}T{}^{b}{}^{c}\big)\big(\mathcal D^{d}T{}^{e}{}^{f}\big)\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\\
&+\frac{191}{24}\big(\mathcal D^{b}T{}^{c}{}^{d}\big)\big(\mathcal D_{b}T{}^{e}{}^{f}\big)\epsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f} +8\big(\Box^c \mathcal D^{c}T{}^{a}{}_{c}\big)
\end{aligned}
\tag{CTF-E0F0-2}
```

#### Constrained vector: $`n=0`$, explicit degree $`2`$

```math
\begin{aligned}
\mathcal E_{0}^{(2)a}={}&\frac{295i}{288}T{}^{d}{}^{e}\epsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{R(Q){}^{b}{}^{c}{}^{i}}\chi{}_{i} -\frac{889i}{288}T{}^{e}{}^{f}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}^{c}{}^{d}\chi{}_{i}\\
&+\frac{5191i}{288}T{}_{b}{}^{f}\epsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{d}{}^{e}\chi{}_{i} +\frac{241}{36}T{}_{b}{}_{c}\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}^{c}\chi{}_{i}\\
&-\frac{6509}{144}T{}_{b}{}_{c}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{a}\chi{}_{i} -\frac{5083i}{576}T{}^{a}{}^{f}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{d}{}^{e}\chi{}_{i}\\
&-\frac{155}{72}T{}^{a}{}_{c}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}_{b}\chi{}_{i} +\frac{67}{32}\epsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\big(\mathcal D^{b}R(Q){}^{c}{}^{d}{}^{i}\big)}\gamma{}^{e}\chi{}_{i}\\
&+\frac{67i}{16}\overline{\big(\mathcal D^{b}R(Q){}^{a}{}^{c}{}^{i}\big)}\gamma{}_{b}{}_{c}\chi{}_{i} -\frac{73i}{32}\overline{\big(\mathcal D^{b}R(Q){}_{b}{}^{c}{}^{i}\big)}\gamma{}^{a}{}_{c}\chi{}_{i}\\
&+\frac{235i}{32}\overline{\big(\mathcal D^{b}R(Q){}^{a}{}_{b}{}^{i}\big)}\chi{}_{i} +\frac{153i}{64}\overline{\big(\mathcal D^{a}R(Q){}^{b}{}^{c}{}^{i}\big)}\gamma{}_{b}{}_{c}\chi{}_{i}\\
&+\frac{160i}{3}\overline{\chi{}^{i}}\gamma{}^{a}{}_{b}\big(\mathcal D^{b}\chi{}_{i}\big) +\frac{65}{16}T{}_{c}{}_{d}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{a}R(Q){}_{b}{}^{d}{}_{i}\\
&+\frac{11i}{32}T{}_{b}{}^{g}\epsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{a}{}^{f}R(Q){}^{d}{}^{e}{}_{i} +\frac{5i}{8}T{}_{b}{}^{f}\epsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f}\overline{R(Q){}^{b}{}^{c}{}^{i}}R(Q){}^{d}{}^{e}{}_{i}\\
&+\frac{35i}{128}T{}_{b}{}_{c}\epsilon{}^{a}{}_{d}{}_{e}{}_{f}{}_{g}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{f}{}^{g}R(Q){}^{d}{}^{e}{}_{i} -\frac{13}{8}T{}_{c}{}_{d}\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}_{b}R(Q){}^{c}{}^{d}{}_{i}\\
&-\frac{9i}{32}T{}^{e}{}^{f}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{R(Q){}^{a}{}^{b}{}^{i}}R(Q){}^{c}{}^{d}{}_{i} +\frac{23i}{32}T{}^{e}{}^{f}\epsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f}\overline{R(Q){}^{b}{}^{c}{}^{i}}R(Q){}_{b}{}^{d}{}_{i}\\
&-\frac{19i}{64}T{}_{b}{}^{g}\epsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g}\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}^{e}{}^{f}R(Q){}^{c}{}^{d}{}_{i} +\frac{1}{2}T{}_{b}{}_{d}\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}_{c}R(Q){}^{c}{}^{d}{}_{i}\\
&+\frac{3i}{8}T{}_{c}{}^{g}\epsilon{}^{a}{}_{d}{}_{e}{}_{f}{}_{g}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{e}{}^{f}R(Q){}_{b}{}^{d}{}_{i} -T{}^{a}{}_{d}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}_{c}R(Q){}_{b}{}^{d}{}_{i}\\
&+\frac{7i}{64}T{}^{a}{}_{b}\epsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{f}{}^{g}R(Q){}^{d}{}^{e}{}_{i} -\frac{i}{16}T{}_{b}{}_{d}\epsilon{}^{a}{}_{c}{}_{e}{}_{f}{}_{g}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{f}{}^{g}R(Q){}^{d}{}^{e}{}_{i}\\
&-\frac{i}{8}T{}^{f}{}^{g}\epsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g}\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}^{d}{}^{e}R(Q){}_{b}{}^{c}{}_{i} +\frac{3}{2}T{}_{c}{}_{d}\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}^{d}R(Q){}_{b}{}^{c}{}_{i}\\
&-\frac{5i}{64}T{}^{f}{}^{g}\epsilon{}^{a}{}_{d}{}_{e}{}_{f}{}_{g}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{d}{}^{e}R(Q){}_{b}{}_{c}{}_{i} -\frac{3i}{32}T{}^{a}{}^{g}\epsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}_{b}{}^{f}R(Q){}^{d}{}^{e}{}_{i}\\
&+\frac{3i}{32}T{}_{c}{}^{g}\epsilon{}^{a}{}_{d}{}_{e}{}_{f}{}_{g}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}_{b}{}^{f}R(Q){}^{d}{}^{e}{}_{i} +\frac{3i}{128}T{}^{f}{}^{g}\epsilon{}^{a}{}_{d}{}_{e}{}_{f}{}_{g}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}_{b}{}_{c}R(Q){}^{d}{}^{e}{}_{i}\\
&+\frac{7i}{64}T{}^{f}{}^{g}\epsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{a}{}_{b}R(Q){}^{d}{}^{e}{}_{i} +\frac{i}{32}T{}_{b}{}_{f}\epsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{g}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{f}{}^{g}R(Q){}^{d}{}^{e}{}_{i}\\
&-\frac{3i}{32}T{}_{f}{}^{g}\epsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{g}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}_{b}{}^{f}R(Q){}^{d}{}^{e}{}_{i} -\frac{i}{64}T{}^{a}{}_{f}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{g}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{f}{}^{g}R(Q){}^{d}{}^{e}{}_{i}
\end{aligned}
\tag{CTF-E0F2-1}
```

```math
\begin{aligned}
&+\frac{7i}{64}T{}_{f}{}^{g}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{g}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{a}{}^{f}R(Q){}^{d}{}^{e}{}_{i} -\frac{i}{128}T{}_{f}{}_{g}\epsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{f}{}^{g}R(Q){}^{d}{}^{e}{}_{i}\\
&+\frac{3i}{32}T{}_{e}{}^{g}\epsilon{}_{b}{}_{c}{}_{d}{}_{f}{}_{g}\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}^{e}{}^{f}R(Q){}^{c}{}^{d}{}_{i} +\frac{3i}{64}T{}^{f}{}^{g}\epsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g}\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}_{b}{}^{e}R(Q){}^{c}{}^{d}{}_{i}\\
&-\frac{77i}{32}T{}_{d}{}^{f}\epsilon{}^{a}{}_{b}{}_{c}{}_{e}{}_{f}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{d}{}^{e}\chi{}_{i} +\frac{27i}{4}T{}^{e}{}^{f}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{a}{}^{d}\chi{}_{i}\\
&+\frac{3}{4}\epsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{e}\big(\mathcal D^{d}\chi{}_{i}\big) -\frac{3i}{2}\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}_{b}{}_{c}\big(\mathcal D^{c}\chi{}_{i}\big)\\
&+i\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{a}{}_{c}\big(\mathcal D_{b}\chi{}_{i}\big) +6i\overline{R(Q){}^{a}{}^{b}{}^{i}}\big(\mathcal D_{b}\chi{}_{i}\big)\\
&+\frac{i}{4}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}_{b}{}_{c}\big(\mathcal D^{a}\chi{}_{i}\big) +\frac{5i}{4}T{}^{e}{}^{f}\epsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}_{b}{}^{d}\chi{}_{i}
\end{aligned}
\tag{CTF-E0F2-2}
```

#### Constrained vector: $`n=1`$, explicit degree $`0`$

```math
\begin{aligned}
\mathcal E_{1}^{(0)a}={}&-4D\big(\mathcal D^{b}\widehat F{}^{a}{}_{b}\big) -2\big(\mathcal D^{b}R(V){}^{a}{}_{b}{}^{i}{}^{j}\big)Y{}_{i}{}_{j}\\
&-2R(V){}^{a}{}^{b}{}^{i}{}^{j}\big(\mathcal D_{b}Y{}_{i}{}_{j}\big) +\frac{1}{8}R(M){}^{b}{}^{c}{}_{b}{}^{d}\widehat F{}^{a}{}^{e}T{}^{f}{}^{g}\epsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g}\\
&-\frac{11}{8}R(M){}^{b}{}^{c}{}^{d}{}^{e}\widehat F{}^{a}{}^{f}T{}_{b}{}^{g}\epsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g} -\frac{3}{8}R(M){}^{b}{}^{c}{}^{d}{}^{e}\widehat F{}^{a}{}_{b}T{}^{f}{}^{g}\epsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g}\\
&+\frac{11}{16}R(M){}^{b}{}^{c}{}^{d}{}^{e}\widehat F{}^{a}{}_{d}T{}^{f}{}^{g}\epsilon{}_{b}{}_{c}{}_{e}{}_{f}{}_{g} +\frac{3}{16}R(M){}^{b}{}^{c}{}^{d}{}^{e}\widehat F{}^{a}{}^{f}T{}_{f}{}^{g}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{g}\\
&+\frac{35}{48}R(M){}^{a}{}^{b}{}^{c}{}^{d}\widehat F{}_{c}{}^{e}T{}^{f}{}^{g}\epsilon{}_{b}{}_{d}{}_{e}{}_{f}{}_{g} +\frac{17}{24}R(M){}^{b}{}^{c}{}_{b}{}^{d}\widehat F{}_{d}{}^{e}T{}^{f}{}^{g}\epsilon{}^{a}{}_{c}{}_{e}{}_{f}{}_{g}\\
&+\frac{53}{24}R(M){}^{b}{}^{c}{}^{d}{}^{e}\widehat F{}_{d}{}^{f}T{}_{b}{}^{g}\epsilon{}^{a}{}_{c}{}_{e}{}_{f}{}_{g} -\frac{13}{12}R(M){}^{b}{}^{c}{}^{d}{}^{e}\widehat F{}_{b}{}_{d}T{}^{f}{}^{g}\epsilon{}^{a}{}_{c}{}_{e}{}_{f}{}_{g}\\
&-\frac{35}{96}R(M){}^{b}{}^{c}{}^{d}{}^{e}\widehat F{}_{d}{}_{e}T{}^{f}{}^{g}\epsilon{}^{a}{}_{b}{}_{c}{}_{f}{}_{g} -\frac{5}{12}R(M){}^{b}{}^{c}{}^{d}{}^{e}\widehat F{}_{d}{}^{f}T{}_{f}{}^{g}\epsilon{}^{a}{}_{b}{}_{c}{}_{e}{}_{g}\\
&+\frac{5}{4}R(M){}^{a}{}^{b}{}^{c}{}^{d}\widehat F{}^{e}{}^{f}T{}_{e}{}^{g}\epsilon{}_{b}{}_{c}{}_{d}{}_{f}{}_{g} -\frac{3}{4}R(M){}^{b}{}^{c}{}_{b}{}^{d}\widehat F{}^{e}{}^{f}T{}_{e}{}^{g}\epsilon{}^{a}{}_{c}{}_{d}{}_{f}{}_{g}\\
&+\frac{1}{8}R(M){}^{b}{}^{c}{}^{d}{}^{e}\widehat F{}^{f}{}^{g}T{}_{b}{}_{f}\epsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{g} -\frac{1}{4}R(M){}^{b}{}^{c}{}^{d}{}^{e}\widehat F{}_{b}{}^{f}T{}_{f}{}^{g}\epsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{g}\\
&-\frac{5}{96}R(M){}^{b}{}^{c}{}^{d}{}^{e}\widehat F{}^{f}{}^{g}T{}_{f}{}_{g}\epsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{e} +\frac{49}{48}R(M){}^{b}{}^{c}{}^{a}{}_{b}\widehat F{}^{d}{}^{e}T{}^{f}{}^{g}\epsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g}\\
&-\frac{29}{48}R(M){}^{b}{}^{c}{}^{a}{}^{d}\widehat F{}^{e}{}^{f}T{}_{b}{}^{g}\epsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g} +\frac{1}{12}R(M){}^{b}{}^{c}{}^{a}{}^{d}\widehat F{}_{b}{}^{e}T{}^{f}{}^{g}\epsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g}\\
&+\frac{7}{16}R(M){}^{b}{}^{c}{}^{a}{}^{d}\widehat F{}_{d}{}^{e}T{}^{f}{}^{g}\epsilon{}_{b}{}_{c}{}_{e}{}_{f}{}_{g} -\frac{3}{4}R(M){}^{b}{}^{c}{}^{a}{}^{d}\widehat F{}^{e}{}^{f}T{}_{e}{}^{g}\epsilon{}_{b}{}_{c}{}_{d}{}_{f}{}_{g}\\
&+\frac{59}{48}R(M){}^{a}{}^{b}{}^{c}{}^{d}\widehat F{}^{e}{}^{f}T{}_{c}{}^{g}\epsilon{}_{b}{}_{d}{}_{e}{}_{f}{}_{g} -\frac{1}{24}R(M){}^{b}{}^{c}{}_{b}{}^{d}\widehat F{}^{e}{}^{f}T{}_{d}{}^{g}\epsilon{}^{a}{}_{c}{}_{e}{}_{f}{}_{g}\\
&+\frac{41}{48}R(M){}^{b}{}^{c}{}^{d}{}^{e}\widehat F{}^{f}{}^{g}T{}_{b}{}_{d}\epsilon{}^{a}{}_{c}{}_{e}{}_{f}{}_{g} -\frac{1}{3}R(M){}^{b}{}^{c}{}^{d}{}^{e}\widehat F{}_{b}{}^{f}T{}_{d}{}^{g}\epsilon{}^{a}{}_{c}{}_{e}{}_{f}{}_{g}\\
&-\frac{3}{4}R(M){}^{b}{}^{c}{}^{d}{}^{e}\widehat F{}^{a}{}^{f}T{}_{d}{}^{g}\epsilon{}_{b}{}_{c}{}_{e}{}_{f}{}_{g} -\frac{13}{12}R(M){}^{b}{}^{c}{}^{d}{}^{e}\widehat F{}_{d}{}^{f}T{}_{e}{}^{g}\epsilon{}^{a}{}_{b}{}_{c}{}_{f}{}_{g}\\
&+\frac{25}{12}R(M){}^{b}{}^{c}{}^{d}{}^{e}\widehat F{}^{f}{}^{g}T{}_{d}{}_{f}\epsilon{}^{a}{}_{b}{}_{c}{}_{e}{}_{g} +\frac{1}{2}R(M){}^{b}{}^{c}{}^{a}{}^{d}\widehat F{}^{e}{}^{f}T{}_{d}{}^{g}\epsilon{}_{b}{}_{c}{}_{e}{}_{f}{}_{g}\\
&-\frac{1}{3}R(M){}^{b}{}^{c}{}^{d}{}^{e}\widehat F{}^{f}{}^{g}T{}_{d}{}_{e}\epsilon{}^{a}{}_{b}{}_{c}{}_{f}{}_{g} -\frac{11}{16}R(M){}^{b}{}^{c}{}_{b}{}^{d}\widehat F{}^{e}{}^{f}T{}^{a}{}^{g}\epsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g}\\
&+\frac{7}{16}R(M){}^{b}{}^{c}{}^{d}{}^{e}\widehat F{}^{f}{}^{g}T{}^{a}{}_{b}\epsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g} -2R(M){}^{b}{}^{c}{}^{d}{}^{e}\widehat F{}_{b}{}^{f}T{}^{a}{}^{g}\epsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g}
\end{aligned}
\tag{CTF-E1F0-1}
```

```math
\begin{aligned}
&+\frac{21}{16}R(M){}^{b}{}^{c}{}^{d}{}^{e}\widehat F{}_{d}{}^{f}T{}^{a}{}^{g}\epsilon{}_{b}{}_{c}{}_{e}{}_{f}{}_{g} -\frac{1}{16}R(M){}^{b}{}^{c}{}^{d}{}^{e}\widehat F{}^{f}{}^{g}T{}^{a}{}_{f}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{g}\\
&+\frac{21}{32}R(M){}^{b}{}^{c}{}^{d}{}^{e}\widehat F{}^{f}{}^{g}T{}^{a}{}_{d}\epsilon{}_{b}{}_{c}{}_{e}{}_{f}{}_{g} -\frac{742}{9}\widehat F{}^{a}{}^{b}T{}_{b}{}^{c}T{}^{d}{}^{e}T{}^{f}{}^{g}\epsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g}\\
&+592\widehat F{}^{b}{}^{c}T{}^{a}{}^{d}T{}_{b}{}^{e}T{}^{f}{}^{g}\epsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g} +\frac{2705}{27}\widehat F{}^{b}{}^{c}T{}_{b}{}^{d}T{}_{d}{}^{e}T{}^{f}{}^{g}\epsilon{}^{a}{}_{c}{}_{e}{}_{f}{}_{g}\\
&-\frac{1235}{9}\widehat F{}^{b}{}^{c}T{}_{b}{}^{d}T{}_{c}{}^{e}T{}^{f}{}^{g}\epsilon{}^{a}{}_{d}{}_{e}{}_{f}{}_{g} +\frac{446}{27}\widehat F{}^{b}{}^{c}T{}_{b}{}_{c}T{}^{d}{}^{e}T{}^{f}{}^{g}\epsilon{}^{a}{}_{d}{}_{e}{}_{f}{}_{g}\\
&-\frac{383}{6}\widehat F{}^{b}{}^{c}T{}^{a}{}^{d}T{}_{d}{}^{e}T{}^{f}{}^{g}\epsilon{}_{b}{}_{c}{}_{e}{}_{f}{}_{g} -\frac{1714}{9}\widehat F{}^{b}{}^{c}T{}^{a}{}_{b}T{}^{d}{}^{e}T{}^{f}{}^{g}\epsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g}\\
&+\frac{784}{27}\widehat F{}^{b}{}^{c}T{}^{d}{}^{e}T{}_{d}{}^{f}T{}_{e}{}^{g}\epsilon{}^{a}{}_{b}{}_{c}{}_{f}{}_{g} -\frac{392}{27}\widehat F{}^{b}{}^{c}T{}^{d}{}^{e}\epsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{e}T^2\\
&-128\widehat F{}^{a}{}^{b}T{}_{b}{}^{c}\big(\mathcal D^{d}T{}_{c}{}_{d}\big) +128\widehat F{}^{a}{}^{b}T{}^{c}{}^{d}\big(\mathcal D_{c}T{}_{b}{}_{d}\big)\\
&+128\widehat F{}^{b}{}^{c}T{}_{b}{}^{d}\big(\mathcal D_{c}T{}^{a}{}_{d}\big) -\frac{400}{3}\widehat F{}^{a}{}^{b}T{}^{c}{}^{d}\big(\mathcal D_{b}T{}_{c}{}_{d}\big)\\
&-128\widehat F{}^{b}{}^{c}T{}^{a}{}^{d}\big(\mathcal D_{b}T{}_{c}{}_{d}\big) -\frac{3}{8}\big(\mathcal D^{b}R(M){}^{c}{}^{d}{}_{c}{}_{d}\big)\widehat F{}^{a}{}_{b}\\
&-\frac{3}{4}\big(\mathcal D^{b}R(M){}_{b}{}^{c}{}_{c}{}^{d}\big)\widehat F{}^{a}{}_{d} +\frac{3}{4}\big(\mathcal D^{b}R(M){}^{c}{}^{d}{}^{a}{}_{c}\big)\widehat F{}_{b}{}_{d}\\
&+\frac{3}{4}\big(\mathcal D^{b}R(M){}_{b}{}^{c}{}^{a}{}^{d}\big)\widehat F{}_{c}{}_{d} -\frac{3}{4}\big(\mathcal D^{a}R(M){}^{b}{}^{c}{}_{b}{}^{d}\big)\widehat F{}_{c}{}_{d}\\
&+\frac{3}{4}\big(\mathcal D^{b}R(M){}^{a}{}^{c}{}_{c}{}^{d}\big)\widehat F{}_{b}{}_{d} -\frac{3}{8}\big(\mathcal D^{b}R(M){}^{a}{}_{b}{}^{c}{}^{d}\big)\widehat F{}_{c}{}_{d}\\
&+\frac{35}{12}\widehat F{}^{a}{}^{b}\big(\mathcal D^{c}\mathcal D^{d}T{}^{e}{}^{f}\big)\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f} -\frac{5}{4}\widehat F{}^{b}{}^{c}\big(\mathcal D_{b}\mathcal D^{d}T{}^{e}{}^{f}\big)\epsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f}\\
&-\frac{7}{2}\widehat F{}^{b}{}^{c}\big(\mathcal D^{d}\mathcal D^{e}T{}_{b}{}^{f}\big)\epsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f} +4\widehat F{}^{b}{}^{c}\big(\mathcal D^{d}\mathcal D^{e}T{}^{a}{}^{f}\big)\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\\
&-\frac{23}{6}\widehat F{}^{b}{}^{c}\big(\mathcal D^{d}\mathcal D^{e}T{}_{d}{}^{f}\big)\epsilon{}^{a}{}_{b}{}_{c}{}_{e}{}_{f} +\frac{3}{4}\widehat F{}^{b}{}^{c}\big(\mathcal D^{a}\mathcal D^{d}T{}^{e}{}^{f}\big)\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\\
&-\frac{2}{3}\widehat F{}^{b}{}^{c}\big(\mathcal D^{d}\mathcal D^{e}T{}_{e}{}^{f}\big)\epsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{f} +\widehat F{}^{b}{}^{c}\big(\mathcal D^{d}\mathcal D^{a}T{}^{e}{}^{f}\big)\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\\
&+\frac{7}{4}\widehat F{}^{b}{}^{c}\big(\mathcal D^{d}\mathcal D_{b}T{}^{e}{}^{f}\big)\epsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f} +\frac{9}{8}R(M){}^{a}{}^{b}{}^{c}{}^{d}\widehat F{}_{b}{}^{e}T{}^{f}{}^{g}\epsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g}\\
&+\frac{17}{32}R(M){}^{a}{}^{b}{}_{b}{}^{c}\widehat F{}^{d}{}^{e}T{}^{f}{}^{g}\epsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g} -\frac{3}{8}R(M){}^{b}{}^{c}{}^{d}{}^{e}\widehat F{}_{b}{}^{f}T{}_{c}{}^{g}\epsilon{}^{a}{}_{d}{}_{e}{}_{f}{}_{g}
\end{aligned}
\tag{CTF-E1F0-2}
```

```math
\begin{aligned}
&-\frac{11}{16}R(M){}^{b}{}^{c}{}_{b}{}^{d}\widehat F{}^{e}{}^{f}T{}_{c}{}^{g}\epsilon{}^{a}{}_{d}{}_{e}{}_{f}{}_{g} -\frac{9}{16}R(M){}^{a}{}^{b}{}^{c}{}^{d}\widehat F{}^{e}{}^{f}T{}_{b}{}^{g}\epsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g}\\
&-\frac{3}{32}R(M){}^{b}{}^{c}{}^{d}{}^{e}\widehat F{}^{f}{}^{g}T{}_{b}{}_{c}\epsilon{}^{a}{}_{d}{}_{e}{}_{f}{}_{g} +\frac{1}{2}R(M){}^{b}{}^{c}{}_{b}{}^{d}\widehat F{}_{c}{}^{e}T{}^{f}{}^{g}\epsilon{}^{a}{}_{d}{}_{e}{}_{f}{}_{g}\\
&-\frac{1}{16}R(M){}^{b}{}^{c}{}^{d}{}^{e}\widehat F{}_{b}{}_{c}T{}^{f}{}^{g}\epsilon{}^{a}{}_{d}{}_{e}{}_{f}{}_{g} -\frac{7}{4}\widehat F{}^{b}{}^{c}\big(\Box^c T{}^{e}{}^{f}\big)\epsilon{}^{a}{}_{b}{}_{c}{}_{e}{}_{f}\\
&-\frac{3}{32}R(M){}^{b}{}^{c}{}_{b}{}_{c}\widehat F{}^{d}{}^{e}T{}^{f}{}^{g}\epsilon{}^{a}{}_{d}{}_{e}{}_{f}{}_{g} -4\big(\mathcal D^{b}D\big)\widehat F{}^{a}{}_{b}\\
&-\big(\Box^c \mathcal D^{c}\widehat F{}^{a}{}_{c}\big) +\frac{8}{3}\big(\mathcal D^{b}\rho\big)\big(\mathcal D_{b}\mathcal D^{c}T{}^{a}{}_{c}\big)\\
&+16\big(\mathcal D^{b}\rho\big)\big(\Box^c T{}^{a}{}_{b}\big) +12\big(\mathcal D^{b}\mathcal D^{c}\rho\big)\big(\mathcal D_{b}T{}^{a}{}_{c}\big)\\
&+\frac{16}{3}\big(\Box^c \mathcal D^{c}\rho\big)T{}^{a}{}_{c} -\frac{23}{6}\big(\mathcal D^{b}\widehat F{}^{c}{}^{d}\big)\big(\mathcal D_{b}T{}^{e}{}^{f}\big)\epsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f}\\
&-\frac{7}{3}\big(\Box^c \widehat F{}^{c}{}^{d}\big)T{}^{e}{}^{f}\epsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f} +\frac{13}{9}\big(\mathcal D^{b}\rho\big)T{}^{c}{}^{d}\big(\mathcal D_{b}T{}^{e}{}^{f}\big)\epsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f}\\
&+\frac{41}{6}\big(\mathcal D^{b}\widehat F{}^{a}{}^{c}\big)\big(\mathcal D^{d}T{}^{e}{}^{f}\big)\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f} -\frac{5}{6}\big(\mathcal D^{b}\widehat F{}^{c}{}^{d}\big)\big(\mathcal D_{c}T{}^{e}{}^{f}\big)\epsilon{}^{a}{}_{b}{}_{d}{}_{e}{}_{f}\\
&-\frac{19}{3}\big(\mathcal D^{b}\widehat F{}^{c}{}^{d}\big)\big(\mathcal D^{e}T{}_{c}{}^{f}\big)\epsilon{}^{a}{}_{b}{}_{d}{}_{e}{}_{f} -4\big(\mathcal D^{b}\widehat F{}^{c}{}^{d}\big)\big(\mathcal D^{e}T{}^{a}{}^{f}\big)\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\\
&-3\big(\mathcal D^{b}\widehat F{}^{c}{}^{d}\big)\big(\mathcal D^{e}T{}_{e}{}^{f}\big)\epsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{f} -\big(\mathcal D^{b}\mathcal D^{c}\widehat F{}^{d}{}^{e}\big)T{}^{a}{}^{f}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\\
&-\frac{1}{3}\big(\mathcal D^{b}\mathcal D^{c}\widehat F{}^{d}{}^{e}\big)T{}_{c}{}^{f}\epsilon{}^{a}{}_{b}{}_{d}{}_{e}{}_{f} -\frac{2}{3}\big(\mathcal D^{b}\mathcal D^{c}\widehat F{}^{d}{}^{e}\big)T{}_{d}{}^{f}\epsilon{}^{a}{}_{b}{}_{c}{}_{e}{}_{f}\\
&-\frac{4}{3}\big(\mathcal D^{b}\mathcal D^{c}\widehat F{}^{a}{}^{d}\big)T{}^{e}{}^{f}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f} -\frac{10}{3}\big(\mathcal D^{b}\mathcal D^{c}\widehat F{}_{c}{}^{d}\big)T{}^{e}{}^{f}\epsilon{}^{a}{}_{b}{}_{d}{}_{e}{}_{f}\\
&+\frac{1}{3}\big(\mathcal D^{b}\mathcal D^{a}\widehat F{}^{c}{}^{d}\big)T{}^{e}{}^{f}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f} -\frac{2}{3}\big(\mathcal D^{a}\mathcal D^{b}\widehat F{}^{c}{}^{d}\big)T{}^{e}{}^{f}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\\
&-\frac{1}{3}\big(\mathcal D^{b}\mathcal D^{c}\widehat F{}^{d}{}^{e}\big)T{}_{b}{}^{f}\epsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f} +43\big(\mathcal D^{b}\rho\big)T{}^{a}{}^{c}\big(\mathcal D^{d}T{}^{e}{}^{f}\big)\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\\
&-\frac{41}{9}\big(\mathcal D^{b}\rho\big)T{}^{c}{}^{d}\big(\mathcal D_{c}T{}^{e}{}^{f}\big)\epsilon{}^{a}{}_{b}{}_{d}{}_{e}{}_{f} +\frac{358}{9}\big(\mathcal D^{b}\rho\big)T{}^{c}{}^{d}\big(\mathcal D^{e}T{}_{c}{}^{f}\big)\epsilon{}^{a}{}_{b}{}_{d}{}_{e}{}_{f}\\
&-\frac{208}{9}\big(\mathcal D^{b}\rho\big)T{}^{c}{}^{d}\big(\mathcal D^{e}T{}^{a}{}^{f}\big)\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f} +\frac{46}{3}\big(\mathcal D^{b}\rho\big)T{}^{c}{}^{d}\big(\mathcal D^{e}T{}_{e}{}^{f}\big)\epsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{f}\\
&+\frac{173}{9}\big(\mathcal D^{b}\rho\big)T{}^{c}{}^{d}\big(\mathcal D^{a}T{}^{e}{}^{f}\big)\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f} -\frac{40}{3}\big(\mathcal D^{b}\mathcal D^{a}\rho\big)T{}^{c}{}^{d}T{}^{e}{}^{f}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}
\end{aligned}
\tag{CTF-E1F0-3}
```

```math
\begin{aligned}
&-\frac{8}{3}\big(\mathcal D^{a}\mathcal D^{b}\rho\big)T{}^{c}{}^{d}T{}^{e}{}^{f}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f} +16\big(\Box^c \rho\big)T{}^{c}{}^{d}T{}^{e}{}^{f}\epsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f}\\
&+4\big(\mathcal D^{b}\mathcal D^{c}\rho\big)\big(\mathcal D_{c}T{}^{a}{}_{b}\big) +10\big(\mathcal D^{b}\mathcal D^{a}\rho\big)\big(\mathcal D^{c}T{}_{b}{}_{c}\big)\\
&-2\big(\mathcal D^{a}\mathcal D^{b}\rho\big)\big(\mathcal D^{c}T{}_{b}{}_{c}\big) +8\big(\Box^c \rho\big)\big(\mathcal D^{c}T{}^{a}{}_{c}\big)\\
&+4\big(\mathcal D^{b}\mathcal D^{c}\rho\big)\big(\mathcal D^{a}T{}_{b}{}_{c}\big) +\frac{32}{3}\big(\mathcal D^{b}\Box^c \rho\big)T{}^{a}{}_{b}\\
&-128\big(\mathcal D^{b}\widehat F{}_{b}{}^{c}\big)T{}^{a}{}^{d}T{}_{c}{}_{d} +\frac{32}{3}\big(\mathcal D^{b}\widehat F{}^{c}{}^{d}\big)T{}^{a}{}_{b}T{}_{c}{}_{d}\\
&+128\big(\mathcal D^{b}\widehat F{}^{a}{}^{c}\big)T{}_{b}{}^{d}T{}_{c}{}_{d} -\frac{200}{3}\big(\mathcal D^{b}\widehat F{}^{a}{}_{b}\big)T^2\\
&-\frac{64}{3}\big(\mathcal D^{b}\widehat F{}^{c}{}^{d}\big)T{}^{a}{}_{c}T{}_{b}{}_{d} -\frac{62}{3}\big(\mathcal D^{a}\rho\big)T{}^{b}{}^{c}\big(\mathcal D^{d}T{}^{e}{}^{f}\big)\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\\
&+\frac{412}{9}\big(\mathcal D^{b}\rho\big)T{}^{c}{}^{d}\big(\mathcal D^{e}T{}_{b}{}^{f}\big)\epsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f} -\frac{197}{3}\big(\mathcal D^{b}\rho\big)T{}_{b}{}^{c}\big(\mathcal D^{d}T{}^{e}{}^{f}\big)\epsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f}\\
&-\frac{32}{3}\big(\mathcal D^{b}\rho\big)\big(\mathcal D^{c}\mathcal D_{b}T{}^{a}{}_{c}\big) +\frac{32}{3}\big(\mathcal D^{b}\rho\big)\big(\mathcal D^{c}\mathcal D^{a}T{}_{b}{}_{c}\big)\\
&+\frac{16}{3}\big(\mathcal D^{b}\rho\big)\big(\mathcal D^{a}\mathcal D^{c}T{}_{b}{}_{c}\big) +\frac{11}{3}\big(\mathcal D^{b}\widehat F{}^{c}{}^{d}\big)\big(\mathcal D^{e}T{}_{b}{}^{f}\big)\epsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f}\\
&+\frac{7}{2}\big(\mathcal D^{b}\widehat F{}_{b}{}^{c}\big)\big(\mathcal D^{d}T{}^{e}{}^{f}\big)\epsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f} -\frac{7}{6}\big(\mathcal D^{a}\widehat F{}^{b}{}^{c}\big)\big(\mathcal D^{d}T{}^{e}{}^{f}\big)\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\\
&-\frac{2}{3}R(M){}^{b}{}^{c}{}_{b}{}_{c}\big(\mathcal D^{d}\rho\big)T{}^{a}{}_{d} +\frac{4}{3}R(M){}^{b}{}^{c}{}_{b}{}^{d}\big(\mathcal D_{c}\rho\big)T{}^{a}{}_{d}\\
&-\frac{4}{3}R(M){}^{b}{}^{c}{}^{a}{}_{b}\big(\mathcal D^{d}\rho\big)T{}_{c}{}_{d} +\frac{4}{3}R(M){}^{b}{}^{c}{}^{a}{}^{d}\big(\mathcal D_{b}\rho\big)T{}_{c}{}_{d}\\
&-\frac{4}{3}R(M){}^{b}{}^{c}{}_{b}{}^{d}\big(\mathcal D^{a}\rho\big)T{}_{c}{}_{d} +\frac{4}{3}R(M){}^{b}{}^{c}{}_{b}{}^{d}\big(\mathcal D_{d}\rho\big)T{}^{a}{}_{c}\\
&-\frac{2}{3}R(M){}^{b}{}^{c}{}^{a}{}^{d}\big(\mathcal D_{d}\rho\big)T{}_{b}{}_{c} -\frac{4}{3}R(M){}^{a}{}^{b}{}_{b}{}^{c}\big(\mathcal D^{d}\rho\big)T{}_{c}{}_{d}\\
&-\frac{2}{3}R(M){}^{a}{}^{b}{}^{c}{}^{d}\big(\mathcal D_{b}\rho\big)T{}_{c}{}_{d} -\frac{4}{3}R(M){}^{a}{}^{b}{}^{c}{}^{d}\big(\mathcal D_{c}\rho\big)T{}_{b}{}_{d}
\end{aligned}
\tag{CTF-E1F0-4}
```

#### Constrained vector: $`n=1`$, explicit degree $`2`$

```math
\begin{aligned}
\mathcal E_{1}^{(2)a}={}&\frac{3i}{16}D\epsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{d}{}^{e}\lambda{}_{i} +D\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}_{b}\lambda{}_{i}\\
&-4i\epsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\big(\mathcal D^{b}\chi{}^{i}\big)}\gamma{}^{c}{}^{d}\big(\mathcal D^{e}\lambda{}_{i}\big) -8\overline{\big(\mathcal D^{b}\chi{}^{i}\big)}\gamma{}_{b}\big(\mathcal D^{a}\lambda{}_{i}\big)\\
&+16\overline{\big(\mathcal D^{b}\chi{}^{i}\big)}\gamma{}^{a}\big(\mathcal D_{b}\lambda{}_{i}\big) -8\overline{\big(\mathcal D^{a}\chi{}^{i}\big)}\gamma{}^{b}\big(\mathcal D_{b}\lambda{}_{i}\big)\\
&+48T{}^{d}{}^{e}\epsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\chi{}^{i}}\gamma{}^{b}\big(\mathcal D^{c}\lambda{}_{i}\big) +96iT{}^{a}{}_{b}\overline{\chi{}^{i}}\big(\mathcal D^{b}\lambda{}_{i}\big)\\
&-48T{}^{d}{}^{e}\epsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\big(\mathcal D^{b}\chi{}^{i}\big)}\gamma{}^{c}\lambda{}_{i} +96iT{}^{a}{}_{b}\overline{\big(\mathcal D^{b}\chi{}^{i}\big)}\lambda{}_{i}\\
&-\frac{499i}{144}Y{}_{i}{}^{j}\epsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{d}{}^{e}\chi{}_{j} +\frac{419}{36}Y{}_{i}{}^{j}\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}_{b}\chi{}_{j}\\
&-\frac{959i}{18432}R(V){}^{d}{}^{e}{}_{i}{}^{j}\epsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{R(Q){}^{b}{}^{c}{}^{i}}\lambda{}_{j} +\frac{1069i}{18432}R(V){}^{c}{}^{d}{}_{i}{}^{j}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}^{e}{}^{f}\lambda{}_{j}\\
&+\frac{275i}{9216}R(V){}^{a}{}^{d}{}_{i}{}^{j}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{e}{}^{f}\lambda{}_{j} +\frac{233i}{4608}R(V){}_{b}{}^{d}{}_{i}{}^{j}\epsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{e}{}^{f}\lambda{}_{j}\\
&+\frac{271}{4608}R(V){}_{b}{}^{c}{}_{i}{}^{j}\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}_{c}\lambda{}_{j} +\frac{473}{1536}R(V){}^{a}{}_{b}{}_{i}{}^{j}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}_{c}\lambda{}_{j}\\
&+\frac{703}{9216}R(V){}_{b}{}_{c}{}_{i}{}^{j}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{a}\lambda{}_{j} -\frac{547i}{9216}R(V){}^{d}{}^{e}{}_{i}{}^{j}\epsilon{}^{a}{}_{b}{}_{c}{}_{e}{}_{f}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}_{d}{}^{f}\lambda{}_{j}\\
&+\frac{359i}{9216}R(V){}^{d}{}^{e}{}_{i}{}^{j}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{a}{}^{f}\lambda{}_{j} -iR(V){}^{b}{}^{c}{}^{i}{}^{j}\epsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\chi{}_{i}}\gamma{}^{d}{}^{e}\lambda{}_{j}\\
&-\frac{20}{3}R(V){}^{a}{}^{b}{}^{i}{}^{j}\overline{\chi{}_{i}}\gamma{}_{b}\lambda{}_{j} -\frac{7}{72}T{}^{e}{}^{f}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}^{c}\big(\mathcal D^{d}\lambda{}_{i}\big)\\
&-\frac{479}{576}T{}^{e}{}^{f}\epsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{d}\big(\mathcal D_{b}\lambda{}_{i}\big) -\frac{685}{1152}T{}_{b}{}^{f}\epsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{d}\big(\mathcal D^{e}\lambda{}_{i}\big)\\
&-\frac{505i}{576}T{}_{c}{}_{d}\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}^{c}{}^{d}\big(\mathcal D_{b}\lambda{}_{i}\big) +\frac{11i}{18}T{}_{b}{}_{d}\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}^{c}{}^{d}\big(\mathcal D_{c}\lambda{}_{i}\big)\\
&+\frac{233i}{72}T{}_{c}{}_{d}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{a}{}^{d}\big(\mathcal D_{b}\lambda{}_{i}\big) +\frac{1645i}{576}T{}_{b}{}_{c}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{a}{}^{d}\big(\mathcal D_{d}\lambda{}_{i}\big)\\
&+\frac{23}{96}T{}^{e}{}^{f}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{d}\big(\mathcal D^{a}\lambda{}_{i}\big) -\frac{361i}{144}T{}_{c}{}_{d}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}_{b}{}^{d}\big(\mathcal D^{a}\lambda{}_{i}\big)\\
&+\frac{19i}{576}T{}_{b}{}_{c}\overline{R(Q){}^{b}{}^{c}{}^{i}}\big(\mathcal D^{a}\lambda{}_{i}\big) +\frac{2705}{2304}T{}_{e}{}^{f}\epsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{f}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{d}\big(\mathcal D^{e}\lambda{}_{i}\big)\\
&-\frac{271i}{288}T{}_{c}{}_{d}\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}_{b}{}^{c}\big(\mathcal D^{d}\lambda{}_{i}\big) -\frac{421i}{144}T{}_{c}{}_{d}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{a}{}_{b}\big(\mathcal D^{d}\lambda{}_{i}\big)
\end{aligned}
\tag{CTF-E1F2-1}
```

```math
\begin{aligned}
&-\frac{235i}{144}T{}_{b}{}_{c}\overline{R(Q){}^{a}{}^{b}{}^{i}}\big(\mathcal D^{c}\lambda{}_{i}\big) -\frac{1255}{2304}T{}^{a}{}^{f}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{d}\big(\mathcal D^{e}\lambda{}_{i}\big)\\
&+\frac{97i}{48}T{}^{a}{}_{d}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}_{b}{}^{d}\big(\mathcal D_{c}\lambda{}_{i}\big) -\frac{187i}{96}T{}^{a}{}_{c}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}_{b}{}^{d}\big(\mathcal D_{d}\lambda{}_{i}\big)\\
&-\frac{69i}{32}T{}^{a}{}_{c}\overline{R(Q){}^{b}{}^{c}{}^{i}}\big(\mathcal D_{b}\lambda{}_{i}\big) -\frac{39i}{16}T{}^{a}{}_{d}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}_{b}{}_{c}\big(\mathcal D^{d}\lambda{}_{i}\big)\\
&-\frac{i}{96}\epsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\big(\mathcal D^{b}R(Q){}^{c}{}^{d}{}^{i}\big)}\big(\mathcal D^{e}\lambda{}_{i}\big) +\frac{i}{96}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\big(\mathcal D^{b}R(Q){}^{a}{}^{c}{}^{i}\big)}\gamma{}^{d}{}^{e}\big(\mathcal D^{f}\lambda{}_{i}\big)\\
&-\frac{215i}{1536}\epsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\big(\mathcal D^{b}R(Q){}_{b}{}^{c}{}^{i}\big)}\gamma{}^{d}{}^{e}\big(\mathcal D^{f}\lambda{}_{i}\big) -\frac{437i}{1536}\epsilon{}^{a}{}_{b}{}_{d}{}_{e}{}_{f}\overline{\big(\mathcal D^{b}R(Q){}^{c}{}^{d}{}^{i}\big)}\gamma{}^{e}{}^{f}\big(\mathcal D_{c}\lambda{}_{i}\big)\\
&+\frac{31}{128}\overline{\big(\mathcal D^{b}R(Q){}^{a}{}_{b}{}^{i}\big)}\gamma{}^{c}\big(\mathcal D_{c}\lambda{}_{i}\big) +\frac{23}{24}\overline{\big(\mathcal D^{b}R(Q){}^{a}{}^{c}{}^{i}\big)}\gamma{}_{b}\big(\mathcal D_{c}\lambda{}_{i}\big)\\
&-\frac{251}{384}\overline{\big(\mathcal D^{b}R(Q){}_{b}{}^{c}{}^{i}\big)}\gamma{}^{a}\big(\mathcal D_{c}\lambda{}_{i}\big) -\frac{39i}{1024}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\big(\mathcal D^{b}R(Q){}^{c}{}^{d}{}^{i}\big)}\gamma{}^{e}{}^{f}\big(\mathcal D^{a}\lambda{}_{i}\big)\\
&+\frac{23}{384}\overline{\big(\mathcal D^{b}R(Q){}_{b}{}^{c}{}^{i}\big)}\gamma{}_{c}\big(\mathcal D^{a}\lambda{}_{i}\big) +\frac{95i}{768}\epsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\big(\mathcal D^{b}R(Q){}^{c}{}^{d}{}^{i}\big)}\gamma{}^{e}{}^{f}\big(\mathcal D_{b}\lambda{}_{i}\big)\\
&-\frac{97}{192}\overline{\big(\mathcal D^{b}R(Q){}^{a}{}^{c}{}^{i}\big)}\gamma{}_{c}\big(\mathcal D_{b}\lambda{}_{i}\big) +\frac{55i}{3072}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\big(\mathcal D^{a}R(Q){}^{b}{}^{c}{}^{i}\big)}\gamma{}^{d}{}^{e}\big(\mathcal D^{f}\lambda{}_{i}\big)\\
&+\frac{77}{128}\overline{\big(\mathcal D^{a}R(Q){}^{b}{}^{c}{}^{i}\big)}\gamma{}_{b}\big(\mathcal D_{c}\lambda{}_{i}\big) -\frac{667i}{864}T{}^{c}{}^{d}T{}^{e}{}^{f}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{R(Q){}^{a}{}^{b}{}^{i}}\lambda{}_{i}\\
&+\frac{5833i}{3456}T{}^{d}{}^{e}T{}^{f}{}^{g}\epsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g}\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}_{b}{}^{c}\lambda{}_{i} +\frac{13175i}{6912}T{}_{b}{}_{c}T{}^{f}{}^{g}\epsilon{}^{a}{}_{d}{}_{e}{}_{f}{}_{g}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{d}{}^{e}\lambda{}_{i}\\
&+\frac{4337i}{1152}T{}_{b}{}^{f}T{}_{c}{}^{g}\epsilon{}^{a}{}_{d}{}_{e}{}_{f}{}_{g}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{d}{}^{e}\lambda{}_{i} -\frac{1531i}{1152}T{}^{a}{}^{f}T{}_{b}{}^{g}\epsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{d}{}^{e}\lambda{}_{i}\\
&+\frac{3847i}{3456}T{}^{a}{}_{b}T{}^{f}{}^{g}\epsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{d}{}^{e}\lambda{}_{i} +\frac{2087}{216}T{}^{a}{}_{d}T{}_{b}{}_{c}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{d}\lambda{}_{i}\\
&+\frac{2225}{108}T{}^{a}{}_{b}T{}_{c}{}_{d}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{d}\lambda{}_{i} -\frac{2939i}{864}T{}_{b}{}^{f}T{}_{f}{}^{g}\epsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{g}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{d}{}^{e}\lambda{}_{i}\\
&+\frac{523}{54}T{}_{b}{}^{d}T{}_{c}{}_{d}\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}^{c}\lambda{}_{i} +\frac{8965i}{6912}T{}^{a}{}^{f}T{}_{f}{}^{g}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{g}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{d}{}^{e}\lambda{}_{i}\\
&-\frac{3179}{108}T{}^{a}{}^{d}T{}_{c}{}_{d}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}_{b}\lambda{}_{i} +\frac{2833i}{1728}\epsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{e}T^2\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{d}{}^{e}\lambda{}_{i}\\
&-\frac{11119}{864}T^2\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}_{b}\lambda{}_{i} +\frac{17}{64}T{}^{e}{}^{f}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\big(\mathcal D^{b}R(Q){}^{a}{}^{c}{}^{i}\big)}\gamma{}^{d}\lambda{}_{i}\\
&+\frac{607}{1152}T{}^{e}{}^{f}\epsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\big(\mathcal D^{b}R(Q){}_{b}{}^{c}{}^{i}\big)}\gamma{}^{d}\lambda{}_{i} -\frac{209}{72}T{}_{c}{}^{f}\epsilon{}^{a}{}_{b}{}_{d}{}_{e}{}_{f}\overline{\big(\mathcal D^{b}R(Q){}^{c}{}^{d}{}^{i}\big)}\gamma{}^{e}\lambda{}_{i}
\end{aligned}
\tag{CTF-E1F2-2}
```

```math
\begin{aligned}
&+\frac{109i}{576}T{}_{c}{}_{d}\overline{\big(\mathcal D^{b}R(Q){}^{a}{}_{b}{}^{i}\big)}\gamma{}^{c}{}^{d}\lambda{}_{i} -\frac{77i}{72}T{}_{c}{}_{d}\overline{\big(\mathcal D^{b}R(Q){}^{a}{}^{c}{}^{i}\big)}\gamma{}_{b}{}^{d}\lambda{}_{i}\\
&+\frac{29i}{24}T{}_{c}{}_{d}\overline{\big(\mathcal D^{b}R(Q){}_{b}{}^{c}{}^{i}\big)}\gamma{}^{a}{}^{d}\lambda{}_{i} +\frac{1315i}{576}T{}_{c}{}_{d}\overline{\big(\mathcal D^{b}R(Q){}^{c}{}^{d}{}^{i}\big)}\gamma{}^{a}{}_{b}\lambda{}_{i}\\
&-\frac{19}{144}T{}^{a}{}^{f}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\big(\mathcal D^{b}R(Q){}^{c}{}^{d}{}^{i}\big)}\gamma{}^{e}\lambda{}_{i} -\frac{7i}{6}T{}^{a}{}_{d}\overline{\big(\mathcal D^{b}R(Q){}_{b}{}^{c}{}^{i}\big)}\gamma{}_{c}{}^{d}\lambda{}_{i}\\
&+\frac{23i}{96}T{}^{a}{}_{d}\overline{\big(\mathcal D^{b}R(Q){}^{c}{}^{d}{}^{i}\big)}\gamma{}_{b}{}_{c}\lambda{}_{i} +\frac{83i}{32}T{}^{a}{}_{c}\overline{\big(\mathcal D^{b}R(Q){}_{b}{}^{c}{}^{i}\big)}\lambda{}_{i}\\
&-\frac{317}{384}T{}_{b}{}^{f}\epsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\big(\mathcal D^{b}R(Q){}^{c}{}^{d}{}^{i}\big)}\gamma{}^{e}\lambda{}_{i} +\frac{407i}{288}T{}_{b}{}_{d}\overline{\big(\mathcal D^{b}R(Q){}^{a}{}^{c}{}^{i}\big)}\gamma{}_{c}{}^{d}\lambda{}_{i}\\
&+\frac{37i}{72}T{}_{b}{}_{d}\overline{\big(\mathcal D^{b}R(Q){}^{c}{}^{d}{}^{i}\big)}\gamma{}^{a}{}_{c}\lambda{}_{i} -\frac{79i}{24}T{}_{b}{}_{c}\overline{\big(\mathcal D^{b}R(Q){}^{a}{}^{c}{}^{i}\big)}\lambda{}_{i}\\
&-\frac{121i}{96}T{}^{a}{}_{b}\overline{\big(\mathcal D^{b}R(Q){}^{c}{}^{d}{}^{i}\big)}\gamma{}_{c}{}_{d}\lambda{}_{i} +\frac{37}{2304}T{}^{e}{}^{f}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\big(\mathcal D^{a}R(Q){}^{b}{}^{c}{}^{i}\big)}\gamma{}^{d}\lambda{}_{i}\\
&+\frac{67i}{144}T{}_{c}{}_{d}\overline{\big(\mathcal D^{a}R(Q){}^{b}{}^{c}{}^{i}\big)}\gamma{}_{b}{}^{d}\lambda{}_{i} -\frac{389i}{192}T{}_{b}{}_{c}\overline{\big(\mathcal D^{a}R(Q){}^{b}{}^{c}{}^{i}\big)}\lambda{}_{i}\\
&+\frac{317}{48}\widehat F{}_{b}{}_{c}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{a}\chi{}_{i} +\frac{11i}{96}\widehat F{}^{d}{}^{e}\epsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{R(Q){}^{b}{}^{c}{}^{i}}\chi{}_{i}\\
&+\frac{67i}{96}\widehat F{}^{e}{}^{f}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}^{c}{}^{d}\chi{}_{i} +\frac{161i}{96}\widehat F{}^{a}{}^{f}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{d}{}^{e}\chi{}_{i}\\
&-\frac{65i}{48}\widehat F{}_{b}{}^{f}\epsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{d}{}^{e}\chi{}_{i} +\frac{175}{24}\widehat F{}_{b}{}_{c}\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}^{c}\chi{}_{i}\\
&+\frac{197}{24}\widehat F{}^{a}{}_{c}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}_{b}\chi{}_{i} -\frac{195}{256}\widehat F{}_{c}{}_{d}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{a}R(Q){}_{b}{}^{d}{}_{i}\\
&-\frac{33i}{512}\widehat F{}_{b}{}^{g}\epsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{a}{}^{f}R(Q){}^{d}{}^{e}{}_{i} -\frac{15i}{128}\widehat F{}_{b}{}^{f}\epsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f}\overline{R(Q){}^{b}{}^{c}{}^{i}}R(Q){}^{d}{}^{e}{}_{i}\\
&-\frac{105i}{2048}\widehat F{}_{b}{}_{c}\epsilon{}^{a}{}_{d}{}_{e}{}_{f}{}_{g}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{f}{}^{g}R(Q){}^{d}{}^{e}{}_{i} +\frac{39}{128}\widehat F{}_{c}{}_{d}\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}_{b}R(Q){}^{c}{}^{d}{}_{i}\\
&+\frac{27i}{512}\widehat F{}^{e}{}^{f}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{R(Q){}^{a}{}^{b}{}^{i}}R(Q){}^{c}{}^{d}{}_{i} -\frac{69i}{512}\widehat F{}^{e}{}^{f}\epsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f}\overline{R(Q){}^{b}{}^{c}{}^{i}}R(Q){}_{b}{}^{d}{}_{i}\\
&+\frac{57i}{1024}\widehat F{}_{b}{}^{g}\epsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g}\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}^{e}{}^{f}R(Q){}^{c}{}^{d}{}_{i} -\frac{3}{32}\widehat F{}_{b}{}_{d}\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}_{c}R(Q){}^{c}{}^{d}{}_{i}\\
&-\frac{9i}{128}\widehat F{}_{c}{}^{g}\epsilon{}^{a}{}_{d}{}_{e}{}_{f}{}_{g}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{e}{}^{f}R(Q){}_{b}{}^{d}{}_{i} +\frac{3}{16}\widehat F{}^{a}{}_{d}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}_{c}R(Q){}_{b}{}^{d}{}_{i}\\
&-\frac{21i}{1024}\widehat F{}^{a}{}_{b}\epsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{f}{}^{g}R(Q){}^{d}{}^{e}{}_{i} +\frac{3i}{256}\widehat F{}_{b}{}_{d}\epsilon{}^{a}{}_{c}{}_{e}{}_{f}{}_{g}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{f}{}^{g}R(Q){}^{d}{}^{e}{}_{i}
\end{aligned}
\tag{CTF-E1F2-3}
```

```math
\begin{aligned}
&+\frac{3i}{128}\widehat F{}^{f}{}^{g}\epsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g}\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}^{d}{}^{e}R(Q){}_{b}{}^{c}{}_{i} -\frac{9}{32}\widehat F{}_{c}{}_{d}\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}^{d}R(Q){}_{b}{}^{c}{}_{i}\\
&+\frac{15i}{1024}\widehat F{}^{f}{}^{g}\epsilon{}^{a}{}_{d}{}_{e}{}_{f}{}_{g}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{d}{}^{e}R(Q){}_{b}{}_{c}{}_{i} +\frac{9i}{512}\widehat F{}^{a}{}^{g}\epsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}_{b}{}^{f}R(Q){}^{d}{}^{e}{}_{i}\\
&-\frac{9i}{512}\widehat F{}_{c}{}^{g}\epsilon{}^{a}{}_{d}{}_{e}{}_{f}{}_{g}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}_{b}{}^{f}R(Q){}^{d}{}^{e}{}_{i} -\frac{9i}{2048}\widehat F{}^{f}{}^{g}\epsilon{}^{a}{}_{d}{}_{e}{}_{f}{}_{g}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}_{b}{}_{c}R(Q){}^{d}{}^{e}{}_{i}\\
&-\frac{21i}{1024}\widehat F{}^{f}{}^{g}\epsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{a}{}_{b}R(Q){}^{d}{}^{e}{}_{i} -\frac{3i}{512}\widehat F{}_{b}{}_{f}\epsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{g}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{f}{}^{g}R(Q){}^{d}{}^{e}{}_{i}\\
&+\frac{9i}{512}\widehat F{}_{f}{}^{g}\epsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{g}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}_{b}{}^{f}R(Q){}^{d}{}^{e}{}_{i} +\frac{3i}{1024}\widehat F{}^{a}{}_{f}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{g}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{f}{}^{g}R(Q){}^{d}{}^{e}{}_{i}\\
&-\frac{21i}{1024}\widehat F{}_{f}{}^{g}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{g}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{a}{}^{f}R(Q){}^{d}{}^{e}{}_{i} +\frac{3i}{2048}\widehat F{}_{f}{}_{g}\epsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{f}{}^{g}R(Q){}^{d}{}^{e}{}_{i}\\
&-\frac{9i}{512}\widehat F{}_{e}{}^{g}\epsilon{}_{b}{}_{c}{}_{d}{}_{f}{}_{g}\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}^{e}{}^{f}R(Q){}^{c}{}^{d}{}_{i} -\frac{9i}{1024}\widehat F{}^{f}{}^{g}\epsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g}\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}_{b}{}^{e}R(Q){}^{c}{}^{d}{}_{i}\\
&-\frac{3i}{2}\widehat F{}_{d}{}^{f}\epsilon{}^{a}{}_{b}{}_{c}{}_{e}{}_{f}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{d}{}^{e}\chi{}_{i} -\frac{11i}{16}\widehat F{}^{e}{}^{f}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{a}{}^{d}\chi{}_{i}\\
&+8\overline{\big(\Box^c \chi{}^{i}\big)}\gamma{}^{a}\lambda{}_{i} +48\big(\mathcal D^{c}T{}^{d}{}^{e}\big)\epsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\chi{}^{i}}\gamma{}^{b}\lambda{}_{i}\\
&+96i\big(\mathcal D^{b}T{}^{a}{}_{b}\big)\overline{\chi{}^{i}}\lambda{}_{i} +\frac{9i}{256}\epsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\big(\Box^c R(Q){}^{c}{}^{d}{}^{i}\big)}\gamma{}^{e}{}^{f}\lambda{}_{i}\\
&-\frac{9}{64}\overline{\big(\Box^c R(Q){}^{a}{}^{c}{}^{i}\big)}\gamma{}_{c}\lambda{}_{i} +\frac{13i}{128}\epsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{d}{}^{e}\big(\Box^c \lambda{}_{i}\big)\\
&-\frac{15}{32}\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}_{b}\big(\Box^c \lambda{}_{i}\big) +8\overline{\chi{}^{i}}\gamma{}^{a}\big(\Box^c \lambda{}_{i}\big)\\
&-\frac{679}{384}\big(\mathcal D^{d}T{}^{e}{}^{f}\big)\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}^{c}\lambda{}_{i} +\frac{3043}{1152}\big(\mathcal D_{b}T{}^{e}{}^{f}\big)\epsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{d}\lambda{}_{i}\\
&-\frac{1189}{192}\big(\mathcal D^{e}T{}_{b}{}^{f}\big)\epsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{d}\lambda{}_{i} +\frac{629i}{384}\big(\mathcal D_{b}T{}_{c}{}_{d}\big)\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}^{c}{}^{d}\lambda{}_{i}\\
&-\frac{253i}{64}\big(\mathcal D_{c}T{}_{b}{}_{d}\big)\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}^{c}{}^{d}\lambda{}_{i} +\frac{1061i}{576}\big(\mathcal D_{b}T{}_{c}{}_{d}\big)\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{a}{}^{d}\lambda{}_{i}\\
&+\frac{1643i}{1152}\big(\mathcal D_{d}T{}_{b}{}_{c}\big)\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{a}{}^{d}\lambda{}_{i} +\frac{1141}{2304}\big(\mathcal D^{a}T{}^{e}{}^{f}\big)\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{d}\lambda{}_{i}\\
&+\frac{373i}{192}\big(\mathcal D^{a}T{}_{c}{}_{d}\big)\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}_{b}{}^{d}\lambda{}_{i} -\frac{1825i}{1152}\big(\mathcal D^{a}T{}_{b}{}_{c}\big)\overline{R(Q){}^{b}{}^{c}{}^{i}}\lambda{}_{i}\\
&-\frac{175}{384}\big(\mathcal D^{e}T{}^{a}{}^{f}\big)\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{d}\lambda{}_{i} -\frac{331i}{576}\big(\mathcal D_{c}T{}^{a}{}_{d}\big)\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}_{b}{}^{d}\lambda{}_{i}
\end{aligned}
\tag{CTF-E1F2-4}
```

```math
\begin{aligned}
&+\frac{73i}{64}\big(\mathcal D_{d}T{}^{a}{}_{c}\big)\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}_{b}{}^{d}\lambda{}_{i} +\frac{995i}{192}\big(\mathcal D_{b}T{}^{a}{}_{c}\big)\overline{R(Q){}^{b}{}^{c}{}^{i}}\lambda{}_{i}\\
&-\frac{959}{768}\big(\mathcal D^{e}T{}_{e}{}^{f}\big)\epsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{f}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{d}\lambda{}_{i} +\frac{655i}{1152}\big(\mathcal D^{d}T{}_{c}{}_{d}\big)\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}_{b}{}^{c}\lambda{}_{i}\\
&+\frac{2341i}{1152}\big(\mathcal D^{d}T{}_{c}{}_{d}\big)\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{a}{}_{b}\lambda{}_{i} +\frac{4555i}{1152}\big(\mathcal D^{c}T{}_{b}{}_{c}\big)\overline{R(Q){}^{a}{}^{b}{}^{i}}\lambda{}_{i}\\
&-\frac{731i}{2304}\big(\mathcal D^{d}T{}^{a}{}_{d}\big)\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}_{b}{}_{c}\lambda{}_{i} +\frac{63}{64}\big(\mathcal D^{e}T{}_{d}{}^{f}\big)\epsilon{}^{a}{}_{b}{}_{c}{}_{e}{}_{f}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{d}\lambda{}_{i}\\
&-\frac{7}{18}\big(\mathcal D_{d}T{}^{e}{}^{f}\big)\epsilon{}^{a}{}_{b}{}_{c}{}_{e}{}_{f}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{d}\lambda{}_{i} +\frac{55}{1152}\big(\mathcal D^{d}T{}^{e}{}^{f}\big)\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{a}\lambda{}_{i}\\
&+\frac{143}{288}T{}_{e}{}^{f}\epsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{f}\overline{\big(\mathcal D^{b}R(Q){}^{c}{}^{d}{}^{i}\big)}\gamma{}^{e}\lambda{}_{i} -\frac{499}{2304}T{}^{e}{}^{f}\epsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\big(\mathcal D^{b}R(Q){}^{c}{}^{d}{}^{i}\big)}\gamma{}_{b}\lambda{}_{i}\\
&-\frac{11}{576}T{}^{e}{}^{f}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\big(\mathcal D^{b}R(Q){}^{c}{}^{d}{}^{i}\big)}\gamma{}^{a}\lambda{}_{i} +\frac{137}{768}T{}_{d}{}^{f}\epsilon{}^{a}{}_{b}{}_{c}{}_{e}{}_{f}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{d}\big(\mathcal D^{e}\lambda{}_{i}\big)\\
&-\frac{61}{576}T{}^{e}{}^{f}\epsilon{}^{a}{}_{b}{}_{c}{}_{e}{}_{f}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{d}\big(\mathcal D_{d}\lambda{}_{i}\big) +\frac{503}{1152}T{}^{e}{}^{f}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{a}\big(\mathcal D^{d}\lambda{}_{i}\big)\\
&+\frac{35i}{1536}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\big(\mathcal D^{b}R(Q){}^{c}{}^{d}{}^{i}\big)}\gamma{}^{a}{}^{e}\big(\mathcal D^{f}\lambda{}_{i}\big) +\frac{i}{16}\epsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{d}{}^{e}\big(\mathcal D^{f}\mathcal D_{b}\lambda{}_{i}\big)\\
&+\frac{3}{16}\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}^{c}\big(\mathcal D_{c}\mathcal D_{b}\lambda{}_{i}\big) +\frac{1}{8}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{a}\big(\mathcal D_{b}\mathcal D_{c}\lambda{}_{i}\big)\\
&+\frac{1}{16}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}_{b}\big(\mathcal D^{a}\mathcal D_{c}\lambda{}_{i}\big) -\frac{i}{32}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{a}{}^{d}\big(\mathcal D^{e}\mathcal D^{f}\lambda{}_{i}\big)\\
&-\frac{3i}{32}\epsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{R(Q){}^{b}{}^{c}{}^{i}}\big(\mathcal D^{d}\mathcal D^{e}\lambda{}_{i}\big) -\frac{4i}{3}\epsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\chi{}^{i}}\gamma{}^{b}{}^{c}\big(\mathcal D^{d}\mathcal D^{e}\lambda{}_{i}\big)\\
&+\frac{8}{3}\overline{\chi{}^{i}}\gamma{}^{b}\big(\mathcal D^{a}\mathcal D_{b}\lambda{}_{i}\big) -\frac{32}{3}\overline{\chi{}^{i}}\gamma{}^{b}\big(\mathcal D_{b}\mathcal D^{a}\lambda{}_{i}\big)\\
&+\frac{i}{192}\epsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{f}\overline{\big(\mathcal D^{b}R(Q){}^{c}{}^{d}{}^{i}\big)}\gamma{}^{e}{}^{f}\big(\mathcal D_{e}\lambda{}_{i}\big) +\frac{i}{16}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}^{c}{}^{d}\big(\mathcal D^{e}\mathcal D^{f}\lambda{}_{i}\big)\\
&-\frac{i}{16}\epsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{d}{}^{e}\big(\mathcal D_{b}\mathcal D^{f}\lambda{}_{i}\big) +\frac{3}{4}\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}^{c}\big(\mathcal D_{b}\mathcal D_{c}\lambda{}_{i}\big)\\
&-\frac{i}{64}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{d}{}^{e}\big(\mathcal D^{f}\mathcal D^{a}\lambda{}_{i}\big) +\frac{1}{8}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}_{b}\big(\mathcal D_{c}\mathcal D^{a}\lambda{}_{i}\big)\\
&-\frac{i}{32}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{d}{}^{e}\big(\mathcal D^{a}\mathcal D^{f}\lambda{}_{i}\big) -\frac{i}{32}\epsilon{}^{a}{}_{b}{}_{c}{}_{e}{}_{f}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{d}{}^{e}\big(\mathcal D^{f}\mathcal D_{d}\lambda{}_{i}\big)\\
&+\frac{31}{384}\overline{\big(\mathcal D^{b}\mathcal D^{c}R(Q){}_{b}{}_{c}{}^{i}\big)}\gamma{}^{a}\lambda{}_{i} +\frac{17i}{192}\epsilon{}^{a}{}_{b}{}_{d}{}_{e}{}_{f}\overline{\big(\mathcal D^{b}\mathcal D^{c}R(Q){}_{c}{}^{d}{}^{i}\big)}\gamma{}^{e}{}^{f}\lambda{}_{i}
\end{aligned}
\tag{CTF-E1F2-5}
```

```math
\begin{aligned}
&-\frac{59}{384}\overline{\big(\mathcal D^{b}\mathcal D^{c}R(Q){}^{a}{}_{c}{}^{i}\big)}\gamma{}_{b}\lambda{}_{i} -\frac{25}{384}\overline{\big(\mathcal D^{a}\mathcal D^{b}R(Q){}_{b}{}^{c}{}^{i}\big)}\gamma{}_{c}\lambda{}_{i}\\
&+\frac{31i}{768}\epsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\big(\mathcal D^{b}\mathcal D^{c}R(Q){}_{b}{}^{d}{}^{i}\big)}\gamma{}^{e}{}^{f}\lambda{}_{i} -\frac{17}{192}\overline{\big(\mathcal D^{b}\mathcal D^{c}R(Q){}^{a}{}_{b}{}^{i}\big)}\gamma{}_{c}\lambda{}_{i}\\
&+\frac{25}{384}\overline{\big(\mathcal D^{b}\mathcal D^{a}R(Q){}_{b}{}^{c}{}^{i}\big)}\gamma{}_{c}\lambda{}_{i} +\frac{5i}{768}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\big(\mathcal D^{b}\mathcal D^{c}R(Q){}^{d}{}^{e}{}^{i}\big)}\gamma{}^{a}{}^{f}\lambda{}_{i}\\
&-\frac{17i}{384}\epsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\big(\mathcal D^{b}\mathcal D^{c}R(Q){}^{d}{}^{e}{}^{i}\big)}\lambda{}_{i} -\frac{3877i}{3456}T{}_{d}{}_{e}T{}^{f}{}^{g}\epsilon{}^{a}{}_{b}{}_{c}{}_{f}{}_{g}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{d}{}^{e}\lambda{}_{i}\\
&-\frac{313i}{384}T{}_{d}{}^{f}T{}_{e}{}^{g}\epsilon{}^{a}{}_{b}{}_{c}{}_{f}{}_{g}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{d}{}^{e}\lambda{}_{i} -\frac{3737i}{2304}T{}^{d}{}^{e}T{}^{f}{}^{g}\epsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{a}{}_{b}\lambda{}_{i}\\
&+\frac{397i}{144}T{}^{a}{}^{f}T{}_{d}{}^{g}\epsilon{}_{b}{}_{c}{}_{e}{}_{f}{}_{g}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{d}{}^{e}\lambda{}_{i} -\frac{209i}{432}T{}^{a}{}_{d}T{}^{f}{}^{g}\epsilon{}_{b}{}_{c}{}_{e}{}_{f}{}_{g}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{d}{}^{e}\lambda{}_{i}\\
&+\frac{833i}{384}T{}_{d}{}^{f}T{}_{f}{}^{g}\epsilon{}^{a}{}_{b}{}_{c}{}_{e}{}_{g}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{d}{}^{e}\lambda{}_{i} +\frac{25}{192}\big(\mathcal D^{d}T{}^{e}{}^{f}\big)\epsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}_{b}\lambda{}_{i}\\
&-\frac{1723i}{4608}T{}^{d}{}^{e}T{}^{f}{}^{g}\epsilon{}^{a}{}_{d}{}_{e}{}_{f}{}_{g}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}_{b}{}_{c}\lambda{}_{i} +\frac{19}{12}\big(\mathcal D^{e}\rho\big)\epsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{d}\chi{}_{i}\\
&-\frac{i}{3}\big(\mathcal D_{c}\rho\big)\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}_{b}{}^{c}\chi{}_{i} +\frac{7i}{12}\big(\mathcal D_{c}\rho\big)\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{a}{}_{b}\chi{}_{i}\\
&+\frac{139i}{12}\big(\mathcal D_{b}\rho\big)\overline{R(Q){}^{a}{}^{b}{}^{i}}\chi{}_{i} -\frac{13i}{12}\big(\mathcal D^{a}\rho\big)\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}_{b}{}_{c}\chi{}_{i}\\
&+\frac{13i}{512}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\big(\mathcal D^{a}\mathcal D^{b}R(Q){}^{c}{}^{d}{}^{i}\big)}\gamma{}^{e}{}^{f}\lambda{}_{i} +\frac{7i}{128}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\big(\mathcal D^{b}\mathcal D^{c}R(Q){}^{a}{}^{d}{}^{i}\big)}\gamma{}^{e}{}^{f}\lambda{}_{i}\\
&+\frac{5i}{128}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\big(\mathcal D^{b}\mathcal D^{a}R(Q){}^{c}{}^{d}{}^{i}\big)}\gamma{}^{e}{}^{f}\lambda{}_{i} -4\overline{\big(\mathcal D^{b}\mathcal D^{a}\chi{}^{i}\big)}\gamma{}_{b}\lambda{}_{i}\\
&+\frac{2i}{3}\epsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\big(\mathcal D^{b}\mathcal D^{c}\chi{}^{i}\big)}\gamma{}^{d}{}^{e}\lambda{}_{i} -4\overline{\big(\mathcal D^{a}\mathcal D^{b}\chi{}^{i}\big)}\gamma{}_{b}\lambda{}_{i}\\
&+\frac{i}{128}\epsilon{}^{a}{}_{b}{}_{c}{}_{e}{}_{f}\overline{\big(\mathcal D^{b}\mathcal D^{c}R(Q){}^{d}{}^{e}{}^{i}\big)}\gamma{}_{d}{}^{f}\lambda{}_{i} -\frac{427i}{288}T{}_{b}{}_{d}T{}^{f}{}^{g}\epsilon{}^{a}{}_{c}{}_{e}{}_{f}{}_{g}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{d}{}^{e}\lambda{}_{i}\\
&+\frac{1367i}{576}T{}_{b}{}^{f}T{}_{d}{}^{g}\epsilon{}^{a}{}_{c}{}_{e}{}_{f}{}_{g}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{d}{}^{e}\lambda{}_{i} -\frac{i}{512}R(V){}^{d}{}^{e}{}_{i}{}^{j}\epsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}_{b}{}^{f}\lambda{}_{j}\\
&-\frac{1}{96}T{}^{e}{}^{f}\epsilon{}^{a}{}_{b}{}_{d}{}_{e}{}_{f}\overline{\big(\mathcal D^{b}R(Q){}^{c}{}^{d}{}^{i}\big)}\gamma{}_{c}\lambda{}_{i} +\frac{i}{256}\epsilon{}^{a}{}_{b}{}_{d}{}_{e}{}_{f}\overline{\big(\mathcal D^{b}R(Q){}^{c}{}^{d}{}^{i}\big)}\gamma{}_{c}{}^{e}\big(\mathcal D^{f}\lambda{}_{i}\big)\\
&-\frac{1}{96}T{}^{e}{}^{f}\epsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}_{b}\big(\mathcal D^{d}\lambda{}_{i}\big) -\frac{23i}{1536}Y{}_{i}{}_{j}\epsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{e}{}^{f}R(Q){}_{b}{}^{d}{}^{j}\\
&+\frac{7}{384}Y{}_{i}{}_{j}\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}_{c}R(Q){}_{b}{}^{c}{}^{j} +\frac{17}{512}Y{}_{i}{}_{j}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{a}R(Q){}_{b}{}_{c}{}^{j}
\end{aligned}
\tag{CTF-E1F2-6}
```

```math
\begin{aligned}
&-\frac{31i}{3072}Y{}_{i}{}_{j}\epsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{R(Q){}^{b}{}^{c}{}^{i}}R(Q){}^{d}{}^{e}{}^{j} +\frac{i}{96}Y{}_{i}{}_{j}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}^{e}{}^{f}R(Q){}^{c}{}^{d}{}^{j}\\
&+\frac{3i}{256}Y{}_{i}{}_{j}\epsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}_{b}{}^{f}R(Q){}^{d}{}^{e}{}^{j} +\frac{i}{12}R(M){}^{b}{}^{c}{}^{d}{}^{e}\epsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\chi{}^{i}}\lambda{}_{i}\\
&-\frac{i}{12}R(M){}^{b}{}^{c}{}^{a}{}^{d}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\chi{}^{i}}\gamma{}^{e}{}^{f}\lambda{}_{i} +\frac{i}{6}R(M){}^{b}{}^{c}{}_{b}{}^{d}\epsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\chi{}^{i}}\gamma{}^{e}{}^{f}\lambda{}_{i}\\
&-\frac{1}{3}R(M){}^{b}{}^{c}{}^{a}{}_{b}\overline{\chi{}^{i}}\gamma{}_{c}\lambda{}_{i} -\frac{1}{6}R(M){}^{b}{}^{c}{}_{b}{}_{c}\overline{\chi{}^{i}}\gamma{}^{a}\lambda{}_{i}\\
&+\frac{i}{12}R(M){}^{a}{}^{b}{}^{c}{}^{d}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\chi{}^{i}}\gamma{}^{e}{}^{f}\lambda{}_{i} -\frac{1}{3}R(M){}^{a}{}^{b}{}_{b}{}^{c}\overline{\chi{}^{i}}\gamma{}_{c}\lambda{}_{i}
\end{aligned}
\tag{CTF-E1F2-7}
```

#### Constrained vector: $`n=2`$, explicit degree $`0`$

```math
\begin{aligned}
\mathcal E_{2}^{(0)a}={}&\big(\mathcal D^{b}\widehat F{}^{a}{}_{b}\big)\big(\Box^c \rho\big) -16\big(\mathcal D^{b}\rho\big)\big(\Box^c \rho\big)T{}^{a}{}_{b}\\
&+\widehat F{}^{b}{}^{c}\big(\Box^c \rho\big)T{}^{e}{}^{f}\epsilon{}^{a}{}_{b}{}_{c}{}_{e}{}_{f} +2R(V){}^{a}{}^{b}{}^{i}{}^{j}Y{}_{i}{}_{j}\big(\mathcal D_{b}\rho\big)\\
&+\big(\mathcal D^{b}\mathcal D^{c}\widehat F{}^{a}{}_{c}\big)\big(\mathcal D_{b}\rho\big) -16\big(\mathcal D^{b}\rho\big)\big(\mathcal D^{c}\rho\big)\big(\mathcal D_{b}T{}^{a}{}_{c}\big)\\
&-\frac{16}{3}\big(\mathcal D^{b}\rho\big)\big(\mathcal D_{b}\mathcal D^{c}\rho\big)T{}^{a}{}_{c} +\frac{5}{6}\widehat F{}^{b}{}^{c}\big(\mathcal D^{d}\rho\big)\big(\mathcal D_{d}T{}^{e}{}^{f}\big)\epsilon{}^{a}{}_{b}{}_{c}{}_{e}{}_{f}\\
&+\frac{5}{3}\big(\mathcal D^{b}\widehat F{}^{c}{}^{d}\big)\big(\mathcal D_{b}\rho\big)T{}^{e}{}^{f}\epsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f} -16\big(\mathcal D^{b}\rho\big)\big(\mathcal D_{b}\rho\big)T{}^{c}{}^{d}T{}^{e}{}^{f}\epsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f}\\
&-\frac{31}{6}\big(\mathcal D^{b}\widehat F{}^{a}{}^{c}\big)\big(\mathcal D^{d}\rho\big)T{}^{e}{}^{f}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f} +\frac{29}{6}\big(\mathcal D^{b}\widehat F{}^{c}{}^{d}\big)\big(\mathcal D_{c}\rho\big)T{}^{e}{}^{f}\epsilon{}^{a}{}_{b}{}_{d}{}_{e}{}_{f}\\
&+\frac{8}{3}\big(\mathcal D^{b}\widehat F{}^{c}{}^{d}\big)\big(\mathcal D^{e}\rho\big)T{}_{c}{}^{f}\epsilon{}^{a}{}_{b}{}_{d}{}_{e}{}_{f} +\frac{5}{2}\big(\mathcal D^{b}\widehat F{}^{c}{}^{d}\big)\big(\mathcal D^{e}\rho\big)T{}^{a}{}^{f}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\\
&+\frac{7}{2}\big(\mathcal D^{b}\widehat F{}^{c}{}^{d}\big)\big(\mathcal D^{e}\rho\big)T{}_{e}{}^{f}\epsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{f} +\frac{1}{2}\big(\mathcal D^{b}\widehat F{}^{c}{}^{d}\big)\big(\mathcal D^{a}\rho\big)T{}^{e}{}^{f}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\\
&+16\big(\mathcal D^{a}\rho\big)\big(\mathcal D^{b}\rho\big)T{}^{c}{}^{d}T{}^{e}{}^{f}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f} -\frac{32}{3}\big(\mathcal D^{b}\rho\big)\big(\mathcal D^{c}\mathcal D_{b}\rho\big)T{}^{a}{}_{c}\\
&+128\widehat F{}^{b}{}^{c}\big(\mathcal D_{b}\rho\big)T{}^{a}{}^{d}T{}_{c}{}_{d} -128\widehat F{}^{a}{}^{b}\big(\mathcal D^{c}\rho\big)T{}_{b}{}^{d}T{}_{c}{}_{d}\\
&+\frac{200}{3}\widehat F{}^{a}{}^{b}\big(\mathcal D_{b}\rho\big)T^2 -8\big(\mathcal D^{a}\rho\big)\big(\mathcal D^{b}\rho\big)\big(\mathcal D^{c}T{}_{b}{}_{c}\big)\\
&-\frac{2}{3}\widehat F{}^{b}{}^{c}\big(\mathcal D^{d}\rho\big)\big(\mathcal D^{e}T{}_{d}{}^{f}\big)\epsilon{}^{a}{}_{b}{}_{c}{}_{e}{}_{f} +7\widehat F{}^{b}{}^{c}\big(\mathcal D^{d}\rho\big)\big(\mathcal D^{e}T{}_{e}{}^{f}\big)\epsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{f}\\
&+\frac{19}{6}\widehat F{}^{a}{}^{b}\big(\mathcal D^{c}\rho\big)\big(\mathcal D^{d}T{}^{e}{}^{f}\big)\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f} -\frac{3}{2}\big(\mathcal D^{b}\widehat F{}^{c}{}^{d}\big)\big(\mathcal D^{e}\rho\big)T{}_{b}{}^{f}\epsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f}\\
&+\frac{1}{2}\big(\mathcal D^{a}\widehat F{}^{b}{}^{c}\big)\big(\mathcal D^{d}\rho\big)T{}^{e}{}^{f}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f} -\frac{23}{6}\big(\mathcal D^{b}\widehat F{}_{b}{}^{c}\big)\big(\mathcal D^{d}\rho\big)T{}^{e}{}^{f}\epsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f}\\
&+\frac{1}{32}R(M){}^{b}{}^{c}{}^{a}{}_{b}\widehat F{}^{d}{}^{e}\widehat F{}^{f}{}^{g}\epsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g} -\frac{1}{64}R(M){}^{a}{}^{b}{}_{b}{}^{c}\widehat F{}^{d}{}^{e}\widehat F{}^{f}{}^{g}\epsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g}\\
&+\frac{3}{32}R(M){}^{b}{}^{c}{}^{d}{}^{e}\widehat F{}^{a}{}^{f}\widehat F{}_{b}{}^{g}\epsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g} -\frac{3}{64}R(M){}^{b}{}^{c}{}^{d}{}^{e}\widehat F{}^{a}{}_{b}\widehat F{}^{f}{}^{g}\epsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g}\\
&+\frac{1}{128}R(M){}^{b}{}^{c}{}_{b}{}_{c}\widehat F{}^{d}{}^{e}\widehat F{}^{f}{}^{g}\epsilon{}^{a}{}_{d}{}_{e}{}_{f}{}_{g} +\frac{1}{16}R(M){}^{b}{}^{c}{}^{d}{}^{e}\widehat F{}_{b}{}^{f}\widehat F{}_{d}{}^{g}\epsilon{}^{a}{}_{c}{}_{e}{}_{f}{}_{g}\\
&-\frac{1}{32}R(M){}^{b}{}^{c}{}^{d}{}^{e}\widehat F{}_{b}{}_{d}\widehat F{}^{f}{}^{g}\epsilon{}^{a}{}_{c}{}_{e}{}_{f}{}_{g} +\frac{1}{16}R(M){}^{b}{}^{c}{}^{d}{}^{e}\widehat F{}_{d}{}_{e}\widehat F{}^{f}{}^{g}\epsilon{}^{a}{}_{b}{}_{c}{}_{f}{}_{g}
\end{aligned}
\tag{CTF-E2F0-1}
```

```math
\begin{aligned}
&-\frac{1}{4}R(M){}^{b}{}^{c}{}^{d}{}^{e}\widehat F{}_{d}{}^{f}\widehat F{}_{f}{}^{g}\epsilon{}^{a}{}_{b}{}_{c}{}_{e}{}_{g} +\frac{1}{32}R(M){}^{b}{}^{c}{}^{d}{}^{e}\epsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{e}\widehat F^2\\
&+\frac{1}{8}R(M){}^{b}{}^{c}{}^{d}{}^{e}\widehat F{}_{d}{}^{f}\widehat F{}_{e}{}^{g}\epsilon{}^{a}{}_{b}{}_{c}{}_{f}{}_{g} -\frac{65}{36}\widehat F{}^{b}{}^{c}\widehat F{}^{d}{}^{e}T{}^{a}{}^{f}T{}_{f}{}^{g}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{g}\\
&-\frac{65}{72}\widehat F{}^{b}{}^{c}\widehat F{}^{d}{}^{e}\epsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{e}T^2 -\frac{19}{6}\widehat F{}^{a}{}^{b}\widehat F{}_{b}{}^{c}T{}^{d}{}^{e}T{}^{f}{}^{g}\epsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g}\\
&-\frac{89}{9}\widehat F{}^{b}{}^{c}\widehat F{}^{d}{}^{e}T{}_{b}{}^{f}T{}_{d}{}^{g}\epsilon{}^{a}{}_{c}{}_{e}{}_{f}{}_{g} +\frac{4}{3}\widehat F{}^{b}{}^{c}\widehat F{}^{d}{}^{e}T{}_{b}{}_{d}T{}^{f}{}^{g}\epsilon{}^{a}{}_{c}{}_{e}{}_{f}{}_{g}\\
&-\frac{19}{12}T{}^{b}{}^{c}T{}^{d}{}^{e}\epsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{e}\widehat F^2 +\frac{5}{2}\widehat F{}^{b}{}^{c}\widehat F{}^{d}{}^{e}T{}_{b}{}_{c}T{}^{f}{}^{g}\epsilon{}^{a}{}_{d}{}_{e}{}_{f}{}_{g}\\
&-\frac{25}{18}\widehat F{}^{b}{}^{c}\widehat F{}^{d}{}^{e}T{}_{b}{}^{f}T{}_{c}{}^{g}\epsilon{}^{a}{}_{d}{}_{e}{}_{f}{}_{g} +\frac{1}{8}R(M){}^{b}{}^{c}{}_{b}{}_{c}\widehat F{}^{a}{}^{d}\big(\mathcal D_{d}\rho\big)\\
&-\frac{1}{4}R(M){}^{b}{}^{c}{}_{b}{}^{d}\widehat F{}^{a}{}_{d}\big(\mathcal D_{c}\rho\big) +\frac{1}{4}R(M){}^{b}{}^{c}{}^{a}{}_{b}\widehat F{}_{c}{}^{d}\big(\mathcal D_{d}\rho\big)\\
&+\frac{1}{4}R(M){}^{b}{}^{c}{}^{a}{}^{d}\widehat F{}_{b}{}_{d}\big(\mathcal D_{c}\rho\big) +\frac{1}{4}R(M){}^{b}{}^{c}{}_{b}{}^{d}\widehat F{}_{c}{}_{d}\big(\mathcal D^{a}\rho\big)\\
&-\frac{1}{4}R(M){}^{b}{}^{c}{}_{b}{}^{d}\widehat F{}^{a}{}_{c}\big(\mathcal D_{d}\rho\big) +\frac{1}{8}R(M){}^{b}{}^{c}{}^{a}{}^{d}\widehat F{}_{b}{}_{c}\big(\mathcal D_{d}\rho\big)\\
&+\frac{1}{4}R(M){}^{a}{}^{b}{}_{b}{}^{c}\widehat F{}_{c}{}^{d}\big(\mathcal D_{d}\rho\big) +\frac{1}{8}R(M){}^{a}{}^{b}{}^{c}{}^{d}\widehat F{}_{c}{}_{d}\big(\mathcal D_{b}\rho\big)\\
&-\frac{1}{4}R(M){}^{a}{}^{b}{}^{c}{}^{d}\widehat F{}_{b}{}_{c}\big(\mathcal D_{d}\rho\big) +4\big(\mathcal D^{b}T{}^{a}{}_{b}\big)\widehat F^2\\
&-8\widehat F{}^{b}{}^{c}\widehat F{}_{b}{}^{d}\big(\mathcal D_{c}T{}^{a}{}_{d}\big) +8\widehat F{}^{a}{}^{b}\widehat F{}_{b}{}^{c}\big(\mathcal D^{d}T{}_{c}{}_{d}\big)\\
&-8\widehat F{}^{a}{}^{b}\widehat F{}^{c}{}^{d}\big(\mathcal D_{c}T{}_{b}{}_{d}\big) +8\widehat F{}^{a}{}^{b}\widehat F{}^{c}{}^{d}\big(\mathcal D_{b}T{}_{c}{}_{d}\big)\\
&-\frac{11}{6}\widehat F{}^{b}{}^{c}\big(\mathcal D_{b}\rho\big)\big(\mathcal D^{d}T{}^{e}{}^{f}\big)\epsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f} +3\widehat F{}^{b}{}^{c}\big(\mathcal D^{d}\rho\big)\big(\mathcal D^{e}T{}_{b}{}^{f}\big)\epsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f}\\
&+\frac{5}{3}\widehat F{}^{b}{}^{c}\big(\mathcal D^{d}\rho\big)\big(\mathcal D^{e}T{}^{a}{}^{f}\big)\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f} +\frac{1}{2}\widehat F{}^{b}{}^{c}\big(\mathcal D^{a}\rho\big)\big(\mathcal D^{d}T{}^{e}{}^{f}\big)\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\\
&-\frac{4}{3}\widehat F{}^{b}{}^{c}\big(\mathcal D^{d}\rho\big)\big(\mathcal D^{a}T{}^{e}{}^{f}\big)\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f} -\frac{9}{2}\widehat F{}^{b}{}^{c}\big(\mathcal D^{d}\rho\big)\big(\mathcal D_{b}T{}^{e}{}^{f}\big)\epsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f}\\
&+\frac{1}{4}\widehat F{}^{b}{}^{c}\big(\Box^c \widehat F{}^{e}{}^{f}\big)\epsilon{}^{a}{}_{b}{}_{c}{}_{e}{}_{f} +\widehat F{}^{a}{}^{b}\big(\Box^c \mathcal D_{b}\rho\big)\\
&+8\widehat F{}^{b}{}^{c}\big(\mathcal D^{d}\widehat F{}^{a}{}_{d}\big)T{}_{b}{}_{c} +\frac{32}{3}\widehat F{}^{b}{}^{c}\big(\mathcal D_{b}\widehat F{}^{a}{}^{d}\big)T{}_{c}{}_{d}
\end{aligned}
\tag{CTF-E2F0-2}
```

```math
\begin{aligned}
&-8\widehat F{}^{b}{}^{c}\big(\mathcal D^{d}\widehat F{}_{b}{}_{d}\big)T{}^{a}{}_{c} -\frac{8}{3}\widehat F{}^{b}{}^{c}\big(\mathcal D_{b}\widehat F{}_{c}{}^{d}\big)T{}^{a}{}_{d}\\
&-\frac{8}{3}\widehat F{}^{b}{}^{c}\big(\mathcal D^{a}\widehat F{}_{b}{}^{d}\big)T{}_{c}{}_{d} +\frac{16}{3}\widehat F{}^{b}{}^{c}\big(\mathcal D^{d}\widehat F{}^{a}{}_{b}\big)T{}_{c}{}_{d}\\
&+\frac{8}{3}\widehat F{}^{b}{}^{c}\big(\mathcal D^{d}\widehat F{}_{b}{}_{c}\big)T{}^{a}{}_{d} +\frac{16}{3}\widehat F{}^{a}{}^{b}\big(\mathcal D^{c}\widehat F{}_{b}{}^{d}\big)T{}_{c}{}_{d}\\
&-\frac{14}{3}\widehat F{}^{b}{}^{c}\big(\mathcal D^{d}\mathcal D^{e}\rho\big)T{}^{a}{}^{f}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f} -\frac{8}{3}\widehat F{}^{b}{}^{c}\big(\mathcal D^{d}\mathcal D^{e}\rho\big)T{}_{e}{}^{f}\epsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{f}\\
&+2\widehat F{}^{b}{}^{c}\big(\mathcal D^{d}\mathcal D^{e}\rho\big)T{}_{b}{}^{f}\epsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f} -\frac{1}{3}\widehat F{}^{b}{}^{c}\big(\mathcal D^{d}\mathcal D^{a}\rho\big)T{}^{e}{}^{f}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\\
&+\frac{1}{3}\widehat F{}^{b}{}^{c}\big(\mathcal D^{d}\mathcal D_{b}\rho\big)T{}^{e}{}^{f}\epsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f} -5\widehat F{}^{a}{}^{b}\big(\mathcal D^{c}\mathcal D^{d}\rho\big)T{}^{e}{}^{f}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\\
&-\frac{7}{3}\widehat F{}^{b}{}^{c}\big(\mathcal D_{b}\mathcal D^{d}\rho\big)T{}^{e}{}^{f}\epsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f} -\frac{2}{3}\widehat F{}^{b}{}^{c}\big(\mathcal D^{a}\mathcal D^{d}\rho\big)T{}^{e}{}^{f}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\\
&+\frac{2}{3}\widehat F{}^{b}{}^{c}\big(\mathcal D^{d}\mathcal D^{e}\rho\big)T{}_{d}{}^{f}\epsilon{}^{a}{}_{b}{}_{c}{}_{e}{}_{f} +\big(\Box^c \widehat F{}^{a}{}^{c}\big)\big(\mathcal D_{c}\rho\big)\\
&+\frac{1}{8}\big(\mathcal D^{b}\widehat F{}^{c}{}^{d}\big)\big(\mathcal D_{b}\widehat F{}^{e}{}^{f}\big)\epsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f} +\big(\mathcal D^{b}\widehat F{}^{a}{}^{c}\big)\big(\mathcal D_{b}\mathcal D_{c}\rho\big)\\
&+4D\widehat F{}^{a}{}^{b}\big(\mathcal D_{b}\rho\big) -8\widehat F{}^{a}{}^{b}\big(\mathcal D^{c}\widehat F{}_{c}{}^{d}\big)T{}_{b}{}_{d}\\
&+\frac{4}{3}\widehat F{}^{a}{}^{b}\big(\mathcal D_{b}\widehat F{}^{c}{}^{d}\big)T{}_{c}{}_{d}
\end{aligned}
\tag{CTF-E2F0-3}
```

#### Constrained vector: $`n=2`$, explicit degree $`2`$

```math
\begin{aligned}
\mathcal E_{2}^{(2)a}={}&2iD\overline{\lambda{}^{i}}\gamma{}^{a}{}^{b}\big(\mathcal D_{b}\lambda{}_{i}\big) -8iY{}^{i}{}^{j}\overline{\big(\mathcal D^{b}\chi{}_{i}\big)}\gamma{}^{a}{}_{b}\lambda{}_{j}\\
&+\frac{i}{2}R(V){}^{b}{}^{c}{}^{i}{}^{j}\overline{\lambda{}_{i}}\gamma{}^{a}{}_{b}\big(\mathcal D_{c}\lambda{}_{j}\big) -iR(V){}^{a}{}^{b}{}^{i}{}^{j}\overline{\lambda{}_{i}}\big(\mathcal D_{b}\lambda{}_{j}\big)\\
&-\frac{2i}{3}R(V){}^{b}{}^{c}{}^{i}{}^{j}T{}^{d}{}^{e}\epsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\lambda{}_{i}}\lambda{}_{j} -\frac{2}{3}R(V){}^{a}{}^{b}{}^{i}{}^{j}T{}_{b}{}_{c}\overline{\lambda{}_{i}}\gamma{}^{c}\lambda{}_{j}\\
&+\frac{2}{3}R(V){}^{b}{}^{c}{}^{i}{}^{j}T{}_{b}{}_{c}\overline{\lambda{}_{i}}\gamma{}^{a}\lambda{}_{j} +\frac{2}{3}R(V){}^{b}{}^{c}{}^{i}{}^{j}T{}^{a}{}_{c}\overline{\lambda{}_{i}}\gamma{}_{b}\lambda{}_{j}\\
&-\frac{299i}{768}\widehat F{}_{b}{}_{c}T{}^{f}{}^{g}\epsilon{}^{a}{}_{d}{}_{e}{}_{f}{}_{g}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{d}{}^{e}\lambda{}_{i} +\frac{341}{288}\widehat F{}_{b}{}_{c}T{}^{a}{}_{d}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{d}\lambda{}_{i}\\
&-\frac{35i}{96}\widehat F{}_{c}{}_{d}\overline{\big(\mathcal D^{b}R(Q){}^{c}{}^{d}{}^{i}\big)}\gamma{}^{a}{}_{b}\lambda{}_{i} +\frac{409i}{1536}\widehat F{}_{b}{}_{c}\overline{\big(\mathcal D^{a}R(Q){}^{b}{}^{c}{}^{i}\big)}\lambda{}_{i}\\
&+\frac{17467i}{9216}\widehat F{}^{d}{}^{e}T{}_{b}{}^{f}\epsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f}\overline{R(Q){}^{b}{}^{c}{}^{i}}\lambda{}_{i} +\frac{3793i}{9216}\widehat F{}^{e}{}^{f}T{}_{b}{}^{g}\epsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g}\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}^{c}{}^{d}\lambda{}_{i}\\
&-\frac{595i}{1024}\widehat F{}^{f}{}^{g}T{}^{a}{}_{b}\epsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{d}{}^{e}\lambda{}_{i} +\frac{2063i}{1152}\widehat F{}^{a}{}^{f}T{}_{b}{}^{g}\epsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{d}{}^{e}\lambda{}_{i}\\
&+\frac{241i}{256}\widehat F{}_{b}{}^{d}T{}^{e}{}^{f}\epsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f}\overline{R(Q){}^{b}{}^{c}{}^{i}}\lambda{}_{i} -\frac{19i}{3072}\widehat F{}_{b}{}^{e}T{}^{f}{}^{g}\epsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g}\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}^{c}{}^{d}\lambda{}_{i}\\
&-\frac{8921i}{9216}\widehat F{}_{b}{}^{f}T{}^{a}{}^{g}\epsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{d}{}^{e}\lambda{}_{i} -\frac{889i}{2304}\widehat F{}^{a}{}_{b}T{}^{f}{}^{g}\epsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{d}{}^{e}\lambda{}_{i}\\
&-\frac{1189i}{2304}\widehat F{}^{f}{}^{g}T{}_{b}{}_{c}\epsilon{}^{a}{}_{d}{}_{e}{}_{f}{}_{g}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{d}{}^{e}\lambda{}_{i} +\frac{1069}{1152}\widehat F{}^{a}{}_{d}T{}_{b}{}_{c}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{d}\lambda{}_{i}\\
&+\frac{227i}{9216}\widehat F{}_{b}{}^{f}T{}_{c}{}^{g}\epsilon{}^{a}{}_{d}{}_{e}{}_{f}{}_{g}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{d}{}^{e}\lambda{}_{i} -\frac{153}{64}\widehat F{}_{b}{}_{d}T{}^{a}{}_{c}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{d}\lambda{}_{i}\\
&-\frac{203}{288}\widehat F{}^{a}{}_{b}T{}_{c}{}_{d}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{d}\lambda{}_{i} -\frac{6617i}{9216}\widehat F{}^{d}{}^{e}T{}_{d}{}^{f}\epsilon{}^{a}{}_{b}{}_{c}{}_{e}{}_{f}\overline{R(Q){}^{b}{}^{c}{}^{i}}\lambda{}_{i}\\
&-\frac{2131i}{9216}\widehat F{}^{e}{}^{f}T{}_{e}{}^{g}\epsilon{}_{b}{}_{c}{}_{d}{}_{f}{}_{g}\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}^{c}{}^{d}\lambda{}_{i} -\frac{23i}{384}\widehat F{}^{f}{}^{g}T{}^{a}{}_{f}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{g}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{d}{}^{e}\lambda{}_{i}\\
&+\frac{305i}{1152}\widehat F{}^{a}{}^{f}T{}_{f}{}^{g}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{g}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{d}{}^{e}\lambda{}_{i} +\frac{155i}{3072}\widehat F{}^{f}{}^{g}T{}_{b}{}_{f}\epsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{g}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{d}{}^{e}\lambda{}_{i}\\
&+\frac{163}{96}\widehat F{}_{c}{}^{d}T{}_{b}{}_{d}\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}^{c}\lambda{}_{i} -\frac{155}{96}\widehat F{}^{a}{}^{d}T{}_{c}{}_{d}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}_{b}\lambda{}_{i}\\
&+\frac{1223i}{2304}\widehat F{}_{b}{}^{f}T{}_{f}{}^{g}\epsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{g}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{d}{}^{e}\lambda{}_{i} -\frac{2029}{576}\widehat F{}_{b}{}^{d}T{}_{c}{}_{d}\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}^{c}\lambda{}_{i}\\
&+\frac{173}{48}\widehat F{}_{c}{}^{d}T{}^{a}{}_{d}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}_{b}\lambda{}_{i} +\frac{95}{288}\widehat F{}_{b}{}^{d}T{}_{c}{}_{d}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{a}\lambda{}_{i}
\end{aligned}
\tag{CTF-E2F2-1}
```

```math
\begin{aligned}
&-\frac{533i}{4608}\widehat F{}^{f}{}^{g}T{}_{f}{}_{g}\epsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{d}{}^{e}\lambda{}_{i} +\frac{189}{128}\widehat F{}^{c}{}^{d}T{}_{c}{}_{d}\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}_{b}\lambda{}_{i}\\
&+\frac{7i}{6}\widehat F{}^{a}{}^{d}T{}^{e}{}^{f}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\chi{}^{i}}\gamma{}^{b}{}^{c}\lambda{}_{i} +\frac{41i}{72}\widehat F{}^{d}{}^{e}T{}^{a}{}^{f}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\chi{}^{i}}\gamma{}^{b}{}^{c}\lambda{}_{i}\\
&+\frac{43i}{36}\widehat F{}^{d}{}^{e}T{}_{d}{}^{f}\epsilon{}^{a}{}_{b}{}_{c}{}_{e}{}_{f}\overline{\chi{}^{i}}\gamma{}^{b}{}^{c}\lambda{}_{i} +\frac{431}{6144}\widehat F{}^{e}{}^{f}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\big(\mathcal D^{a}R(Q){}^{b}{}^{c}{}^{i}\big)}\gamma{}^{d}\lambda{}_{i}\\
&-\frac{1}{384}\widehat F{}^{e}{}^{f}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\big(\mathcal D^{b}R(Q){}^{a}{}^{c}{}^{i}\big)}\gamma{}^{d}\lambda{}_{i} +\frac{13}{1024}\widehat F{}^{a}{}^{f}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\big(\mathcal D^{b}R(Q){}^{c}{}^{d}{}^{i}\big)}\gamma{}^{e}\lambda{}_{i}\\
&-\frac{61}{1024}\widehat F{}^{e}{}^{f}\epsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\big(\mathcal D^{b}R(Q){}_{b}{}^{c}{}^{i}\big)}\gamma{}^{d}\lambda{}_{i} -\frac{61i}{512}\widehat F{}_{c}{}_{d}\overline{\big(\mathcal D^{b}R(Q){}^{a}{}_{b}{}^{i}\big)}\gamma{}^{c}{}^{d}\lambda{}_{i}\\
&+\frac{143i}{768}\widehat F{}^{a}{}_{d}\overline{\big(\mathcal D^{b}R(Q){}_{b}{}^{c}{}^{i}\big)}\gamma{}_{c}{}^{d}\lambda{}_{i} +\frac{45}{512}\widehat F{}_{c}{}^{f}\epsilon{}^{a}{}_{b}{}_{d}{}_{e}{}_{f}\overline{\big(\mathcal D^{b}R(Q){}^{c}{}^{d}{}^{i}\big)}\gamma{}^{e}\lambda{}_{i}\\
&+\frac{35i}{768}\widehat F{}_{c}{}_{d}\overline{\big(\mathcal D^{a}R(Q){}^{b}{}^{c}{}^{i}\big)}\gamma{}_{b}{}^{d}\lambda{}_{i} -\frac{7i}{32}\widehat F{}_{c}{}_{d}\overline{\big(\mathcal D^{b}R(Q){}^{a}{}^{c}{}^{i}\big)}\gamma{}_{b}{}^{d}\lambda{}_{i}\\
&-\frac{5i}{24}\widehat F{}^{a}{}_{d}\overline{\big(\mathcal D^{b}R(Q){}^{c}{}^{d}{}^{i}\big)}\gamma{}_{b}{}_{c}\lambda{}_{i} -\frac{143i}{768}\widehat F{}_{c}{}_{d}\overline{\big(\mathcal D^{b}R(Q){}_{b}{}^{c}{}^{i}\big)}\gamma{}^{a}{}^{d}\lambda{}_{i}\\
&+\frac{i}{256}\widehat F{}^{a}{}_{c}\overline{\big(\mathcal D^{b}R(Q){}_{b}{}^{c}{}^{i}\big)}\lambda{}_{i} +\frac{247}{1536}\widehat F{}_{b}{}^{f}\epsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\big(\mathcal D^{b}R(Q){}^{c}{}^{d}{}^{i}\big)}\gamma{}^{e}\lambda{}_{i}\\
&+\frac{3i}{64}\widehat F{}_{b}{}_{d}\overline{\big(\mathcal D^{b}R(Q){}^{a}{}^{c}{}^{i}\big)}\gamma{}_{c}{}^{d}\lambda{}_{i} +\frac{5i}{384}\widehat F{}^{a}{}_{b}\overline{\big(\mathcal D^{b}R(Q){}^{c}{}^{d}{}^{i}\big)}\gamma{}_{c}{}_{d}\lambda{}_{i}\\
&-\frac{19i}{192}\widehat F{}_{b}{}_{d}\overline{\big(\mathcal D^{b}R(Q){}^{c}{}^{d}{}^{i}\big)}\gamma{}^{a}{}_{c}\lambda{}_{i} +\frac{5i}{48}\widehat F{}_{b}{}_{c}\overline{\big(\mathcal D^{b}R(Q){}^{a}{}^{c}{}^{i}\big)}\lambda{}_{i}\\
&+4\widehat F{}^{d}{}^{e}\epsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\big(\mathcal D^{b}\chi{}^{i}\big)}\gamma{}^{c}\lambda{}_{i} +\frac{i}{2}\overline{\lambda{}^{i}}\gamma{}^{a}{}^{b}\big(\Box^c \mathcal D_{b}\lambda{}_{i}\big)\\
&+\frac{43i}{24}\big(\mathcal D_{d}T{}^{e}{}^{f}\big)\epsilon{}^{a}{}_{b}{}_{c}{}_{e}{}_{f}\overline{\lambda{}^{i}}\gamma{}^{b}{}^{c}\big(\mathcal D^{d}\lambda{}_{i}\big) -2\big(\mathcal D_{c}T{}^{a}{}_{b}\big)\overline{\lambda{}^{i}}\gamma{}^{b}\big(\mathcal D^{c}\lambda{}_{i}\big)\\
&+\frac{7i}{4}T{}^{e}{}^{f}\epsilon{}^{a}{}_{b}{}_{c}{}_{e}{}_{f}\overline{\lambda{}^{i}}\gamma{}^{b}{}^{c}\big(\Box^c \lambda{}_{i}\big) -2T{}^{a}{}_{b}\overline{\lambda{}^{i}}\gamma{}^{b}\big(\Box^c \lambda{}_{i}\big)\\
&-12\big(\mathcal D_{b}\rho\big)\overline{\big(\mathcal D^{b}\chi{}^{i}\big)}\gamma{}^{a}\lambda{}_{i} -4\big(\Box^c \rho\big)\overline{\chi{}^{i}}\gamma{}^{a}\lambda{}_{i}\\
&+i\big(\mathcal D^{c}T{}^{d}{}^{e}\big)\epsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\lambda{}^{i}}\big(\mathcal D^{b}\lambda{}_{i}\big) -\frac{19i}{12}\big(\mathcal D^{d}T{}^{e}{}^{f}\big)\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\lambda{}^{i}}\gamma{}^{b}{}^{c}\big(\mathcal D^{a}\lambda{}_{i}\big)\\
&-\frac{11i}{4}\big(\mathcal D^{e}T{}_{d}{}^{f}\big)\epsilon{}^{a}{}_{b}{}_{c}{}_{e}{}_{f}\overline{\lambda{}^{i}}\gamma{}^{b}{}^{c}\big(\mathcal D^{d}\lambda{}_{i}\big) -\frac{5i}{12}\big(\mathcal D^{e}T{}^{a}{}^{f}\big)\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\lambda{}^{i}}\gamma{}^{b}{}^{c}\big(\mathcal D^{d}\lambda{}_{i}\big)\\
&+\frac{7i}{6}\big(\mathcal D^{e}T{}_{e}{}^{f}\big)\epsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{f}\overline{\lambda{}^{i}}\gamma{}^{b}{}^{c}\big(\mathcal D^{d}\lambda{}_{i}\big) -2\big(\mathcal D^{c}T{}_{b}{}_{c}\big)\overline{\lambda{}^{i}}\gamma{}^{b}\big(\mathcal D^{a}\lambda{}_{i}\big)
\end{aligned}
\tag{CTF-E2F2-2}
```

```math
\begin{aligned}
&+2\big(\mathcal D^{c}T{}^{a}{}_{c}\big)\overline{\lambda{}^{i}}\gamma{}^{b}\big(\mathcal D_{b}\lambda{}_{i}\big) -\frac{5i}{24}\big(\mathcal D^{a}T{}^{e}{}^{f}\big)\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\lambda{}^{i}}\gamma{}^{b}{}^{c}\big(\mathcal D^{d}\lambda{}_{i}\big)\\
&-\frac{4i}{3}T{}^{e}{}^{f}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\lambda{}^{i}}\gamma{}^{b}{}^{c}\big(\mathcal D^{d}\mathcal D^{a}\lambda{}_{i}\big) -\frac{13i}{6}T{}_{e}{}^{f}\epsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{f}\overline{\lambda{}^{i}}\gamma{}^{b}{}^{c}\big(\mathcal D^{d}\mathcal D^{e}\lambda{}_{i}\big)\\
&-\frac{i}{6}T{}^{a}{}^{f}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\lambda{}^{i}}\gamma{}^{b}{}^{c}\big(\mathcal D^{d}\mathcal D^{e}\lambda{}_{i}\big) -\frac{4i}{3}T{}_{d}{}^{f}\epsilon{}^{a}{}_{b}{}_{c}{}_{e}{}_{f}\overline{\lambda{}^{i}}\gamma{}^{b}{}^{c}\big(\mathcal D^{d}\mathcal D^{e}\lambda{}_{i}\big)\\
&-\frac{4}{3}T{}_{b}{}_{c}\overline{\lambda{}^{i}}\gamma{}^{b}\big(\mathcal D^{c}\mathcal D^{a}\lambda{}_{i}\big) -\frac{4}{3}T{}_{b}{}_{c}\overline{\lambda{}^{i}}\gamma{}^{a}\big(\mathcal D^{b}\mathcal D^{c}\lambda{}_{i}\big)\\
&+\frac{8}{3}T{}^{a}{}_{c}\overline{\lambda{}^{i}}\gamma{}^{b}\big(\mathcal D^{c}\mathcal D_{b}\lambda{}_{i}\big) -\frac{5i}{12}T{}^{e}{}^{f}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\lambda{}^{i}}\gamma{}^{b}{}^{c}\big(\mathcal D^{a}\mathcal D^{d}\lambda{}_{i}\big)\\
&+4iT{}^{a}{}^{d}\big(\mathcal D_{d}T{}_{b}{}_{c}\big)\overline{\lambda{}^{i}}\gamma{}^{b}{}^{c}\lambda{}_{i} +16iT{}^{a}{}^{d}\big(\mathcal D_{b}T{}_{c}{}_{d}\big)\overline{\lambda{}^{i}}\gamma{}^{b}{}^{c}\lambda{}_{i}\\
&-16iT{}^{c}{}^{d}\big(\mathcal D_{c}T{}_{b}{}_{d}\big)\overline{\lambda{}^{i}}\gamma{}^{a}{}^{b}\lambda{}_{i} +\frac{40i}{3}T{}^{c}{}^{d}\big(\mathcal D_{b}T{}_{c}{}_{d}\big)\overline{\lambda{}^{i}}\gamma{}^{a}{}^{b}\lambda{}_{i}\\
&-8iT{}_{b}{}^{d}\big(\mathcal D_{d}T{}^{a}{}_{c}\big)\overline{\lambda{}^{i}}\gamma{}^{b}{}^{c}\lambda{}_{i} -16iT{}_{b}{}^{d}\big(\mathcal D_{c}T{}^{a}{}_{d}\big)\overline{\lambda{}^{i}}\gamma{}^{b}{}^{c}\lambda{}_{i}\\
&+8iT{}^{a}{}_{b}\big(\mathcal D^{d}T{}_{c}{}_{d}\big)\overline{\lambda{}^{i}}\gamma{}^{b}{}^{c}\lambda{}_{i} +16iT{}_{b}{}^{c}\big(\mathcal D^{d}T{}_{c}{}_{d}\big)\overline{\lambda{}^{i}}\gamma{}^{a}{}^{b}\lambda{}_{i}\\
&+4iT{}_{b}{}_{c}\big(\mathcal D^{d}T{}^{a}{}_{d}\big)\overline{\lambda{}^{i}}\gamma{}^{b}{}^{c}\lambda{}_{i} +8iT{}^{a}{}_{d}T{}_{b}{}_{c}\overline{\lambda{}^{i}}\gamma{}^{b}{}^{c}\big(\mathcal D^{d}\lambda{}_{i}\big)\\
&+32iT{}^{a}{}^{d}T{}_{c}{}_{d}\overline{\lambda{}^{i}}\gamma{}^{b}{}^{c}\big(\mathcal D_{b}\lambda{}_{i}\big) -32iT{}_{b}{}^{d}T{}_{c}{}_{d}\overline{\lambda{}^{i}}\gamma{}^{a}{}^{b}\big(\mathcal D^{c}\lambda{}_{i}\big)\\
&+\frac{40i}{3}T^2\overline{\lambda{}^{i}}\gamma{}^{a}{}^{b}\big(\mathcal D_{b}\lambda{}_{i}\big) +16iT{}^{a}{}_{b}T{}_{c}{}_{d}\overline{\lambda{}^{i}}\gamma{}^{b}{}^{c}\big(\mathcal D^{d}\lambda{}_{i}\big)\\
&-48\big(\mathcal D^{c}\rho\big)T{}^{d}{}^{e}\epsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\chi{}^{i}}\gamma{}^{b}\lambda{}_{i} -96i\big(\mathcal D^{b}\rho\big)T{}^{a}{}_{b}\overline{\chi{}^{i}}\lambda{}_{i}\\
&-8i\big(\mathcal D^{b}Y{}^{i}{}^{j}\big)\overline{\chi{}_{i}}\gamma{}^{a}{}_{b}\lambda{}_{j} +\frac{2i}{3}\big(\mathcal D^{d}\mathcal D^{e}T{}_{d}{}^{f}\big)\epsilon{}^{a}{}_{b}{}_{c}{}_{e}{}_{f}\overline{\lambda{}^{i}}\gamma{}^{b}{}^{c}\lambda{}_{i}\\
&+\frac{i}{3}\big(\mathcal D^{d}\mathcal D^{e}T{}_{e}{}^{f}\big)\epsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{f}\overline{\lambda{}^{i}}\gamma{}^{b}{}^{c}\lambda{}_{i} +\frac{i}{6}\big(\mathcal D^{c}\mathcal D^{d}T{}^{e}{}^{f}\big)\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\lambda{}^{i}}\gamma{}^{a}{}^{b}\lambda{}_{i}\\
&+\frac{i}{2}\big(\mathcal D^{d}T{}^{e}{}^{f}\big)\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\lambda{}^{i}}\gamma{}^{a}{}^{b}\big(\mathcal D^{c}\lambda{}_{i}\big) +\frac{5}{72}\big(\mathcal D^{b}R(V){}^{c}{}^{d}{}^{i}{}^{j}\big)\epsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\lambda{}_{i}}\gamma{}^{e}\lambda{}_{j}\\
&-\frac{i}{2}\big(\mathcal D^{b}R(V){}^{a}{}_{b}{}^{i}{}^{j}\big)\overline{\lambda{}_{i}}\lambda{}_{j} +\frac{2236i}{27}T{}^{a}{}^{d}T{}_{d}{}^{e}T{}^{f}{}^{g}\epsilon{}_{b}{}_{c}{}_{e}{}_{f}{}_{g}\overline{\lambda{}^{i}}\gamma{}^{b}{}^{c}\lambda{}_{i}\\
&+\frac{520i}{27}T{}^{d}{}^{e}\epsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{e}T^2\overline{\lambda{}^{i}}\gamma{}^{b}{}^{c}\lambda{}_{i} -\frac{1040i}{27}T{}^{d}{}^{e}T{}_{d}{}^{f}T{}_{e}{}^{g}\epsilon{}^{a}{}_{b}{}_{c}{}_{f}{}_{g}\overline{\lambda{}^{i}}\gamma{}^{b}{}^{c}\lambda{}_{i}
\end{aligned}
\tag{CTF-E2F2-3}
```

```math
\begin{aligned}
&+\frac{1772i}{27}T{}_{b}{}^{c}T{}^{d}{}^{e}T{}^{f}{}^{g}\epsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g}\overline{\lambda{}^{i}}\gamma{}^{a}{}^{b}\lambda{}_{i} +\frac{512i}{27}T{}^{a}{}_{b}T{}^{d}{}^{e}T{}^{f}{}^{g}\epsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g}\overline{\lambda{}^{i}}\gamma{}^{b}{}^{c}\lambda{}_{i}\\
&-\frac{136i}{27}T{}_{b}{}_{c}T{}^{d}{}^{e}T{}^{f}{}^{g}\epsilon{}^{a}{}_{d}{}_{e}{}_{f}{}_{g}\overline{\lambda{}^{i}}\gamma{}^{b}{}^{c}\lambda{}_{i} +\frac{7i}{32}\big(\mathcal D_{b}Y{}_{i}{}^{j}\big)\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{a}{}_{c}\lambda{}_{j}\\
&+\frac{13i}{96}\big(\mathcal D_{b}Y{}_{i}{}^{j}\big)\overline{R(Q){}^{a}{}^{b}{}^{i}}\lambda{}_{j} +\frac{2i}{3}\big(\mathcal D^{d}T{}^{e}{}^{f}\big)\epsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\lambda{}^{i}}\gamma{}^{b}{}^{c}\big(\mathcal D_{b}\lambda{}_{i}\big)\\
&-\frac{103i}{576}Y{}_{i}{}^{j}T{}^{d}{}^{e}\epsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{R(Q){}^{b}{}^{c}{}^{i}}\lambda{}_{j} +\frac{497i}{1728}Y{}_{i}{}^{j}T{}^{e}{}^{f}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}^{c}{}^{d}\lambda{}_{j}\\
&-\frac{3539i}{6912}Y{}_{i}{}^{j}T{}^{a}{}^{f}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{d}{}^{e}\lambda{}_{j} +\frac{4387i}{3456}Y{}_{i}{}^{j}T{}_{b}{}^{f}\epsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{d}{}^{e}\lambda{}_{j}\\
&+\frac{209}{216}Y{}_{i}{}^{j}T{}_{b}{}_{c}\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}^{c}\lambda{}_{j} -\frac{109}{144}Y{}_{i}{}^{j}T{}^{a}{}_{c}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}_{b}\lambda{}_{j}\\
&-\frac{2393}{864}Y{}_{i}{}^{j}T{}_{b}{}_{c}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{a}\lambda{}_{j} +\frac{i}{12}R(M){}^{b}{}^{c}{}^{a}{}_{b}T{}^{f}{}^{g}\epsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g}\overline{\lambda{}^{i}}\gamma{}^{d}{}^{e}\lambda{}_{i}\\
&+\frac{i}{12}R(M){}^{b}{}^{c}{}^{a}{}^{d}T{}_{d}{}^{g}\epsilon{}_{b}{}_{c}{}_{e}{}_{f}{}_{g}\overline{\lambda{}^{i}}\gamma{}^{e}{}^{f}\lambda{}_{i} +\frac{i}{24}R(M){}^{b}{}^{c}{}_{b}{}_{c}T{}^{f}{}^{g}\epsilon{}^{a}{}_{d}{}_{e}{}_{f}{}_{g}\overline{\lambda{}^{i}}\gamma{}^{d}{}^{e}\lambda{}_{i}\\
&-\frac{i}{6}R(M){}^{b}{}^{c}{}_{b}{}^{d}T{}_{d}{}^{g}\epsilon{}^{a}{}_{c}{}_{e}{}_{f}{}_{g}\overline{\lambda{}^{i}}\gamma{}^{e}{}^{f}\lambda{}_{i} +\frac{i}{24}R(M){}^{b}{}^{c}{}^{d}{}^{e}T{}_{d}{}_{e}\epsilon{}^{a}{}_{b}{}_{c}{}_{f}{}_{g}\overline{\lambda{}^{i}}\gamma{}^{f}{}^{g}\lambda{}_{i}\\
&+\frac{i}{8}R(M){}^{b}{}^{c}{}_{b}{}^{d}T{}^{a}{}^{g}\epsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g}\overline{\lambda{}^{i}}\gamma{}^{e}{}^{f}\lambda{}_{i} -\frac{i}{16}R(M){}^{b}{}^{c}{}^{d}{}^{e}T{}^{a}{}_{d}\epsilon{}_{b}{}_{c}{}_{e}{}_{f}{}_{g}\overline{\lambda{}^{i}}\gamma{}^{f}{}^{g}\lambda{}_{i}\\
&-\frac{i}{8}R(M){}^{b}{}^{c}{}^{a}{}^{d}T{}_{b}{}^{g}\epsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g}\overline{\lambda{}^{i}}\gamma{}^{e}{}^{f}\lambda{}_{i} -\frac{i}{8}R(M){}^{b}{}^{c}{}_{b}{}^{d}T{}_{c}{}^{g}\epsilon{}^{a}{}_{d}{}_{e}{}_{f}{}_{g}\overline{\lambda{}^{i}}\gamma{}^{e}{}^{f}\lambda{}_{i}\\
&+\frac{i}{8}R(M){}^{b}{}^{c}{}^{d}{}^{e}T{}_{b}{}_{d}\epsilon{}^{a}{}_{c}{}_{e}{}_{f}{}_{g}\overline{\lambda{}^{i}}\gamma{}^{f}{}^{g}\lambda{}_{i} +\frac{i}{8}R(M){}^{b}{}^{c}{}^{d}{}^{e}T{}^{a}{}_{b}\epsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g}\overline{\lambda{}^{i}}\gamma{}^{f}{}^{g}\lambda{}_{i}\\
&+\frac{i}{16}R(M){}^{b}{}^{c}{}^{d}{}^{e}T{}_{b}{}_{c}\epsilon{}^{a}{}_{d}{}_{e}{}_{f}{}_{g}\overline{\lambda{}^{i}}\gamma{}^{f}{}^{g}\lambda{}_{i} -\frac{i}{12}R(M){}^{a}{}^{b}{}_{b}{}^{c}T{}^{f}{}^{g}\epsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g}\overline{\lambda{}^{i}}\gamma{}^{d}{}^{e}\lambda{}_{i}\\
&-\frac{i}{6}R(M){}^{a}{}^{b}{}^{c}{}^{d}T{}_{c}{}^{g}\epsilon{}_{b}{}_{d}{}_{e}{}_{f}{}_{g}\overline{\lambda{}^{i}}\gamma{}^{e}{}^{f}\lambda{}_{i} -\frac{7i}{48}R(M){}^{a}{}^{b}{}^{c}{}^{d}T{}_{b}{}^{g}\epsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g}\overline{\lambda{}^{i}}\gamma{}^{e}{}^{f}\lambda{}_{i}\\
&-\frac{259i}{96}\big(\mathcal D_{d}\rho\big)T{}_{b}{}_{c}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{a}{}^{d}\lambda{}_{i} +\frac{125i}{96}\big(\mathcal D^{a}\rho\big)T{}_{b}{}_{c}\overline{R(Q){}^{b}{}^{c}{}^{i}}\lambda{}_{i}\\
&+4\big(\mathcal D^{a}\rho\big)\overline{\chi{}^{i}}\gamma{}^{b}\big(\mathcal D_{b}\lambda{}_{i}\big) +\frac{1}{3}\big(\mathcal D^{c}\widehat F{}^{d}{}^{e}\big)\epsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\chi{}^{i}}\gamma{}^{b}\lambda{}_{i}\\
&-\frac{5i}{3}\big(\mathcal D^{a}\widehat F{}_{b}{}_{c}\big)\overline{\chi{}^{i}}\gamma{}^{b}{}^{c}\lambda{}_{i} +\frac{10i}{3}\big(\mathcal D_{b}\widehat F{}^{a}{}_{c}\big)\overline{\chi{}^{i}}\gamma{}^{b}{}^{c}\lambda{}_{i}\\
&-\frac{i}{3}\big(\mathcal D^{d}\mathcal D^{e}\rho\big)\epsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\chi{}^{i}}\gamma{}^{b}{}^{c}\lambda{}_{i} -\frac{10}{3}\big(\mathcal D^{a}\mathcal D_{b}\rho\big)\overline{\chi{}^{i}}\gamma{}^{b}\lambda{}_{i}
\end{aligned}
\tag{CTF-E2F2-4}
```

```math
\begin{aligned}
&+\frac{22}{3}\big(\mathcal D_{b}\mathcal D^{a}\rho\big)\overline{\chi{}^{i}}\gamma{}^{b}\lambda{}_{i} +2i\big(\mathcal D^{e}\rho\big)\epsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\big(\mathcal D^{b}\chi{}^{i}\big)}\gamma{}^{c}{}^{d}\lambda{}_{i}\\
&+8\big(\mathcal D_{b}\rho\big)\overline{\big(\mathcal D^{a}\chi{}^{i}\big)}\gamma{}^{b}\lambda{}_{i} +4\big(\mathcal D^{a}\rho\big)\overline{\big(\mathcal D^{b}\chi{}^{i}\big)}\gamma{}_{b}\lambda{}_{i}\\
&+i\big(\mathcal D^{b}D\big)\overline{\lambda{}^{i}}\gamma{}^{a}{}_{b}\lambda{}_{i} +\frac{i}{4}\big(\mathcal D^{a}\mathcal D^{d}T{}^{e}{}^{f}\big)\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\lambda{}^{i}}\gamma{}^{b}{}^{c}\lambda{}_{i}\\
&+\frac{i}{2}\big(\mathcal D^{d}\mathcal D^{e}T{}^{a}{}^{f}\big)\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\lambda{}^{i}}\gamma{}^{b}{}^{c}\lambda{}_{i} -\frac{i}{4}\big(\mathcal D^{d}\mathcal D^{a}T{}^{e}{}^{f}\big)\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\lambda{}^{i}}\gamma{}^{b}{}^{c}\lambda{}_{i}\\
&-\frac{5i}{64}\big(\Box^c \rho\big)\epsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{d}{}^{e}\lambda{}_{i} +\frac{5}{16}\big(\Box^c \rho\big)\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}_{b}\lambda{}_{i}\\
&+\frac{i}{2}\overline{\big(\mathcal D_{b}\lambda{}^{i}\big)}\gamma{}^{a}{}^{b}\big(\Box^c \lambda{}_{i}\big) -iT{}^{d}{}^{e}\epsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\big(\mathcal D^{b}\lambda{}^{i}\big)}\big(\mathcal D^{c}\lambda{}_{i}\big)\\
&-\frac{5i}{4}T{}^{e}{}^{f}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\big(\mathcal D^{a}\lambda{}^{i}\big)}\gamma{}^{b}{}^{c}\big(\mathcal D^{d}\lambda{}_{i}\big) +\frac{5i}{4}T{}^{e}{}^{f}\epsilon{}^{a}{}_{b}{}_{c}{}_{e}{}_{f}\overline{\big(\mathcal D^{d}\lambda{}^{i}\big)}\gamma{}^{b}{}^{c}\big(\mathcal D_{d}\lambda{}_{i}\big)\\
&-\frac{5i}{2}T{}_{d}{}^{f}\epsilon{}^{a}{}_{b}{}_{c}{}_{e}{}_{f}\overline{\big(\mathcal D^{d}\lambda{}^{i}\big)}\gamma{}^{b}{}^{c}\big(\mathcal D^{e}\lambda{}_{i}\big) +2T{}_{b}{}_{c}\overline{\big(\mathcal D^{a}\lambda{}^{i}\big)}\gamma{}^{b}\big(\mathcal D^{c}\lambda{}_{i}\big)\\
&-2T{}^{a}{}_{c}\overline{\big(\mathcal D_{b}\lambda{}^{i}\big)}\gamma{}^{b}\big(\mathcal D^{c}\lambda{}_{i}\big) -2i\big(\mathcal D^{e}\rho\big)\epsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\chi{}^{i}}\gamma{}^{b}{}^{c}\big(\mathcal D^{d}\lambda{}_{i}\big)\\
&+8\big(\mathcal D_{b}\rho\big)\overline{\chi{}^{i}}\gamma{}^{b}\big(\mathcal D^{a}\lambda{}_{i}\big) -12\big(\mathcal D_{b}\rho\big)\overline{\chi{}^{i}}\gamma{}^{a}\big(\mathcal D^{b}\lambda{}_{i}\big)\\
&+\frac{13i}{128}\big(\mathcal D_{b}\rho\big)\epsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{d}{}^{e}\big(\mathcal D^{f}\lambda{}_{i}\big) -\frac{5}{64}\big(\mathcal D_{c}\rho\big)\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}_{b}\big(\mathcal D^{a}\lambda{}_{i}\big)\\
&-\frac{1}{8}\big(\mathcal D_{c}\rho\big)\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{a}\big(\mathcal D_{b}\lambda{}_{i}\big) -\frac{5}{8}\big(\mathcal D_{b}\rho\big)\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}^{c}\big(\mathcal D_{c}\lambda{}_{i}\big)\\
&-\frac{1}{96}\big(\mathcal D_{b}\rho\big)T{}^{e}{}^{f}\epsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{d}\lambda{}_{i} -\frac{3i}{4}\big(\mathcal D_{c}\rho\big)T{}^{a}{}_{d}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}_{b}{}^{d}\lambda{}_{i}\\
&-\frac{67i}{24}\big(\mathcal D_{b}\rho\big)T{}_{c}{}_{d}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{a}{}^{d}\lambda{}_{i} -\frac{25i}{48}\big(\mathcal D_{b}\rho\big)T{}^{a}{}_{c}\overline{R(Q){}^{b}{}^{c}{}^{i}}\lambda{}_{i}\\
&+\frac{71i}{96}\big(\mathcal D_{b}\rho\big)T{}_{c}{}_{d}\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}^{c}{}^{d}\lambda{}_{i} +\frac{7}{72}Y{}_{i}{}^{j}\epsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\big(\mathcal D^{b}R(Q){}^{c}{}^{d}{}^{i}\big)}\gamma{}^{e}\lambda{}_{j}\\
&+\frac{7i}{36}Y{}_{i}{}^{j}\overline{\big(\mathcal D^{b}R(Q){}^{a}{}^{c}{}^{i}\big)}\gamma{}_{b}{}_{c}\lambda{}_{j} +\frac{35i}{576}Y{}_{i}{}^{j}\overline{\big(\mathcal D^{b}R(Q){}_{b}{}^{c}{}^{i}\big)}\gamma{}^{a}{}_{c}\lambda{}_{j}\\
&+\frac{113i}{192}Y{}_{i}{}^{j}\overline{\big(\mathcal D^{b}R(Q){}^{a}{}_{b}{}^{i}\big)}\lambda{}_{j} +\frac{11i}{128}Y{}_{i}{}^{j}\overline{\big(\mathcal D^{a}R(Q){}^{b}{}^{c}{}^{i}\big)}\gamma{}_{b}{}_{c}\lambda{}_{j}\\
&-\frac{11}{192}Y{}_{i}{}^{j}\epsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{d}\big(\mathcal D^{e}\lambda{}_{j}\big) -\frac{11i}{96}Y{}_{i}{}^{j}\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}_{b}{}^{c}\big(\mathcal D_{c}\lambda{}_{j}\big)
\end{aligned}
\tag{CTF-E2F2-5}
```

```math
\begin{aligned}
&-\frac{17i}{96}Y{}_{i}{}^{j}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{a}{}_{b}\big(\mathcal D_{c}\lambda{}_{j}\big) +\frac{43i}{96}Y{}_{i}{}^{j}\overline{R(Q){}^{a}{}^{b}{}^{i}}\big(\mathcal D_{b}\lambda{}_{j}\big)\\
&+\frac{i}{24}Y{}_{i}{}^{j}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}_{b}{}_{c}\big(\mathcal D^{a}\lambda{}_{j}\big) -8iY{}^{i}{}^{j}\overline{\chi{}_{i}}\gamma{}^{a}{}^{b}\big(\mathcal D_{b}\lambda{}_{j}\big)\\
&+\frac{49i}{1152}Y{}_{i}{}^{j}T{}_{d}{}^{f}\epsilon{}^{a}{}_{b}{}_{c}{}_{e}{}_{f}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{d}{}^{e}\lambda{}_{j} +\frac{203i}{216}Y{}_{i}{}^{j}T{}^{e}{}^{f}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{a}{}^{d}\lambda{}_{j}\\
&+\frac{19i}{144}Y{}_{i}{}^{j}T{}^{e}{}^{f}\epsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}_{b}{}^{d}\lambda{}_{j} +\frac{1}{48}\big(\mathcal D^{d}Y{}_{i}{}^{j}\big)\epsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{e}\lambda{}_{j}\\
&-\frac{i}{24}\big(\mathcal D^{c}Y{}_{i}{}^{j}\big)\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}_{b}{}_{c}\lambda{}_{j} +\frac{i}{192}\big(\mathcal D^{a}Y{}_{i}{}^{j}\big)\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}_{b}{}_{c}\lambda{}_{j}\\
&+\frac{i}{2}\overline{\big(\mathcal D^{c}\lambda{}^{i}\big)}\gamma{}^{a}{}^{b}\big(\mathcal D_{c}\mathcal D_{b}\lambda{}_{i}\big) -\frac{9i}{128}\big(\mathcal D_{b}\rho\big)\epsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\big(\mathcal D^{b}R(Q){}^{c}{}^{d}{}^{i}\big)}\gamma{}^{e}{}^{f}\lambda{}_{i}\\
&+\frac{19}{64}\big(\mathcal D_{b}\rho\big)\overline{\big(\mathcal D^{b}R(Q){}^{a}{}^{c}{}^{i}\big)}\gamma{}_{c}\lambda{}_{i} -\frac{15i}{128}\big(\mathcal D_{f}\rho\big)\epsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{d}{}^{e}\big(\mathcal D^{f}\lambda{}_{i}\big)\\
&+\frac{35}{64}\big(\mathcal D_{c}\rho\big)\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}_{b}\big(\mathcal D^{c}\lambda{}_{i}\big) +\frac{25}{48}\big(\mathcal D^{d}\rho\big)T{}^{e}{}^{f}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}^{c}\lambda{}_{i}\\
&+\frac{1285}{384}\big(\mathcal D^{e}\rho\big)T{}_{b}{}^{f}\epsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{d}\lambda{}_{i} +\frac{17i}{8}\big(\mathcal D_{c}\rho\big)T{}_{b}{}_{d}\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}^{c}{}^{d}\lambda{}_{i}\\
&-\frac{29}{96}\big(\mathcal D^{a}\rho\big)T{}^{e}{}^{f}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{d}\lambda{}_{i} +\frac{i}{8}\big(\mathcal D^{a}\rho\big)T{}_{c}{}_{d}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}_{b}{}^{d}\lambda{}_{i}\\
&+\frac{67}{768}\big(\mathcal D^{e}\rho\big)T{}^{a}{}^{f}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{d}\lambda{}_{i} +\frac{71i}{48}\big(\mathcal D_{d}\rho\big)T{}^{a}{}_{c}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}_{b}{}^{d}\lambda{}_{i}\\
&-\frac{421}{768}\big(\mathcal D^{e}\rho\big)T{}_{e}{}^{f}\epsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{f}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{d}\lambda{}_{i} +\frac{7i}{12}\big(\mathcal D^{d}\rho\big)T{}_{c}{}_{d}\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}_{b}{}^{c}\lambda{}_{i}\\
&+\frac{5i}{16}\big(\mathcal D^{d}\rho\big)T{}_{c}{}_{d}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{a}{}_{b}\lambda{}_{i} -\frac{43i}{48}\big(\mathcal D^{c}\rho\big)T{}_{b}{}_{c}\overline{R(Q){}^{a}{}^{b}{}^{i}}\lambda{}_{i}\\
&+\frac{13i}{32}\big(\mathcal D^{d}\rho\big)T{}^{a}{}_{d}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}_{b}{}_{c}\lambda{}_{i} -\frac{81}{256}\big(\mathcal D^{e}\rho\big)T{}_{d}{}^{f}\epsilon{}^{a}{}_{b}{}_{c}{}_{e}{}_{f}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{d}\lambda{}_{i}\\
&+\frac{67}{192}\big(\mathcal D_{d}\rho\big)T{}^{e}{}^{f}\epsilon{}^{a}{}_{b}{}_{c}{}_{e}{}_{f}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{d}\lambda{}_{i} -\frac{41}{96}\big(\mathcal D^{d}\rho\big)T{}^{e}{}^{f}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{a}\lambda{}_{i}\\
&-\frac{3i}{32}\big(\mathcal D^{f}\rho\big)\epsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{d}{}^{e}\big(\mathcal D_{b}\lambda{}_{i}\big) -\frac{9}{16}\big(\mathcal D_{c}\rho\big)\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}^{c}\big(\mathcal D_{b}\lambda{}_{i}\big)\\
&-\frac{7}{32}\big(\mathcal D^{a}\rho\big)\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}_{b}\big(\mathcal D_{c}\lambda{}_{i}\big) -\frac{3i}{128}\big(\mathcal D^{f}\rho\big)\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{a}{}^{d}\big(\mathcal D^{e}\lambda{}_{i}\big)\\
&+\frac{i}{64}\big(\mathcal D^{f}\rho\big)\epsilon{}^{a}{}_{b}{}_{c}{}_{e}{}_{f}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{d}{}^{e}\big(\mathcal D_{d}\lambda{}_{i}\big) +\frac{5i}{128}\big(\mathcal D^{f}\rho\big)\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{d}{}^{e}\big(\mathcal D^{a}\lambda{}_{i}\big)
\end{aligned}
\tag{CTF-E2F2-6}
```

```math
\begin{aligned}
&-\frac{1}{16}\big(\mathcal D_{c}\rho\big)\overline{\big(\mathcal D^{b}R(Q){}_{b}{}^{c}{}^{i}\big)}\gamma{}^{a}\lambda{}_{i} +\frac{i}{16}\big(\mathcal D^{f}\rho\big)\epsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\big(\mathcal D^{b}R(Q){}_{b}{}^{c}{}^{i}\big)}\gamma{}^{d}{}^{e}\lambda{}_{i}\\
&-\frac{7}{32}\big(\mathcal D_{c}\rho\big)\overline{\big(\mathcal D^{b}R(Q){}^{a}{}_{b}{}^{i}\big)}\gamma{}^{c}\lambda{}_{i} +\frac{1}{16}\big(\mathcal D^{a}\rho\big)\overline{\big(\mathcal D^{b}R(Q){}_{b}{}^{c}{}^{i}\big)}\gamma{}_{c}\lambda{}_{i}\\
&+\frac{i}{64}\big(\mathcal D_{c}\rho\big)\epsilon{}^{a}{}_{b}{}_{d}{}_{e}{}_{f}\overline{\big(\mathcal D^{b}R(Q){}^{c}{}^{d}{}^{i}\big)}\gamma{}^{e}{}^{f}\lambda{}_{i} +\frac{1}{64}\big(\mathcal D_{c}\rho\big)\overline{\big(\mathcal D^{b}R(Q){}^{a}{}^{c}{}^{i}\big)}\gamma{}_{b}\lambda{}_{i}\\
&-\frac{3}{64}\big(\mathcal D_{c}\rho\big)\overline{\big(\mathcal D^{a}R(Q){}^{b}{}^{c}{}^{i}\big)}\gamma{}_{b}\lambda{}_{i} -\frac{i}{128}\big(\mathcal D^{f}\rho\big)\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\big(\mathcal D^{b}R(Q){}^{c}{}^{d}{}^{i}\big)}\gamma{}^{a}{}^{e}\lambda{}_{i}\\
&-\frac{i}{128}\big(\mathcal D^{e}\rho\big)\epsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\big(\mathcal D^{b}R(Q){}^{c}{}^{d}{}^{i}\big)}\lambda{}_{i} +\frac{i}{256}\big(\mathcal D^{a}\rho\big)\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\big(\mathcal D^{b}R(Q){}^{c}{}^{d}{}^{i}\big)}\gamma{}^{e}{}^{f}\lambda{}_{i}\\
&+\frac{i}{64}\big(\mathcal D^{f}\rho\big)\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\big(\mathcal D^{b}R(Q){}^{a}{}^{c}{}^{i}\big)}\gamma{}^{d}{}^{e}\lambda{}_{i} -\frac{5}{32}\big(\mathcal D^{d}\rho\big)T{}^{e}{}^{f}\epsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}_{b}\lambda{}_{i}\\
&+\frac{i}{16}R(M){}^{b}{}^{c}{}_{b}{}^{d}\overline{\lambda{}^{i}}\gamma{}^{a}{}_{c}\big(\mathcal D_{d}\lambda{}_{i}\big) +\frac{1}{16}R(M){}^{b}{}^{c}{}_{b}{}^{d}\epsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\lambda{}^{i}}\gamma{}^{e}\big(\mathcal D^{f}\lambda{}_{i}\big)\\
&-\frac{i}{16}R(M){}^{a}{}^{b}{}_{b}{}^{c}\overline{\lambda{}^{i}}\gamma{}_{c}{}^{d}\big(\mathcal D_{d}\lambda{}_{i}\big) -\frac{i}{16}R(M){}^{a}{}^{b}{}_{b}{}^{c}\overline{\lambda{}^{i}}\big(\mathcal D_{c}\lambda{}_{i}\big)\\
&-\frac{i}{16}R(M){}^{b}{}^{c}{}^{a}{}_{b}\overline{\lambda{}^{i}}\gamma{}_{c}{}^{d}\big(\mathcal D_{d}\lambda{}_{i}\big) -\frac{i}{16}R(M){}^{a}{}^{b}{}^{c}{}^{d}\overline{\lambda{}^{i}}\gamma{}_{c}{}_{d}\big(\mathcal D_{b}\lambda{}_{i}\big)\\
&+\frac{1}{32}R(M){}^{b}{}^{c}{}^{d}{}^{e}\epsilon{}^{a}{}_{b}{}_{c}{}_{e}{}_{f}\overline{\lambda{}^{i}}\gamma{}^{f}\big(\mathcal D_{d}\lambda{}_{i}\big) +\frac{i}{16}R(M){}^{a}{}^{b}{}^{c}{}^{d}\overline{\lambda{}^{i}}\gamma{}_{b}{}_{c}\big(\mathcal D_{d}\lambda{}_{i}\big)\\
&+\frac{1}{32}R(M){}^{a}{}^{b}{}^{c}{}^{d}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\lambda{}^{i}}\gamma{}^{e}\big(\mathcal D^{f}\lambda{}_{i}\big) -\frac{1}{32}R(M){}^{b}{}^{c}{}^{a}{}^{d}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\lambda{}^{i}}\gamma{}^{e}\big(\mathcal D^{f}\lambda{}_{i}\big)\\
&-\frac{i}{32}R(M){}^{b}{}^{c}{}^{a}{}^{d}\overline{\lambda{}^{i}}\gamma{}_{b}{}_{c}\big(\mathcal D_{d}\lambda{}_{i}\big) -\frac{i}{32}R(M){}^{b}{}^{c}{}_{b}{}_{c}\overline{\lambda{}^{i}}\gamma{}^{a}{}^{d}\big(\mathcal D_{d}\lambda{}_{i}\big)\\
&+\frac{1}{32}\widehat F{}^{d}{}^{e}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}^{c}\big(\mathcal D^{f}\lambda{}_{i}\big) +\frac{9}{64}\widehat F{}^{e}{}^{f}\epsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{d}\big(\mathcal D_{b}\lambda{}_{i}\big)\\
&-\frac{1}{8}\widehat F{}_{b}{}^{e}\epsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{d}\big(\mathcal D^{f}\lambda{}_{i}\big) -\frac{15i}{128}\widehat F{}_{c}{}_{d}\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}^{c}{}^{d}\big(\mathcal D_{b}\lambda{}_{i}\big)\\
&-\frac{i}{64}\widehat F{}_{b}{}_{c}\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}^{c}{}^{d}\big(\mathcal D_{d}\lambda{}_{i}\big) -\frac{3i}{64}\widehat F{}_{b}{}_{d}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{a}{}^{d}\big(\mathcal D_{c}\lambda{}_{i}\big)\\
&-\frac{31i}{128}\widehat F{}_{b}{}_{c}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{a}{}^{d}\big(\mathcal D_{d}\lambda{}_{i}\big) -\frac{1}{128}\widehat F{}^{e}{}^{f}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{d}\big(\mathcal D^{a}\lambda{}_{i}\big)\\
&-\frac{i}{16}\widehat F{}_{c}{}_{d}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}_{b}{}^{d}\big(\mathcal D^{a}\lambda{}_{i}\big) +\frac{i}{8}\widehat F{}_{b}{}_{c}\overline{R(Q){}^{b}{}^{c}{}^{i}}\big(\mathcal D^{a}\lambda{}_{i}\big)\\
&-\frac{1}{64}\widehat F{}^{e}{}^{f}\epsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{f}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{d}\big(\mathcal D_{e}\lambda{}_{i}\big) -\frac{i}{8}\widehat F{}_{c}{}^{d}\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}_{b}{}^{c}\big(\mathcal D_{d}\lambda{}_{i}\big)
\end{aligned}
\tag{CTF-E2F2-7}
```

```math
\begin{aligned}
&-\frac{3i}{32}\widehat F{}_{c}{}^{d}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{a}{}_{b}\big(\mathcal D_{d}\lambda{}_{i}\big) -\frac{1}{128}\widehat F{}^{a}{}^{e}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{d}\big(\mathcal D^{f}\lambda{}_{i}\big)\\
&+\frac{11i}{64}\widehat F{}^{a}{}_{d}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}_{b}{}^{d}\big(\mathcal D_{c}\lambda{}_{i}\big) +\frac{3i}{64}\widehat F{}^{a}{}_{c}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}_{b}{}^{d}\big(\mathcal D_{d}\lambda{}_{i}\big)\\
&-\frac{21i}{64}\widehat F{}^{a}{}_{b}\overline{R(Q){}^{b}{}^{c}{}^{i}}\big(\mathcal D_{c}\lambda{}_{i}\big) -\frac{5i}{64}\widehat F{}^{a}{}^{d}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}_{b}{}_{c}\big(\mathcal D_{d}\lambda{}_{i}\big)\\
&-\frac{i}{128}\big(\mathcal D^{f}\rho\big)\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}^{c}{}^{d}\big(\mathcal D^{e}\lambda{}_{i}\big) +\frac{i}{32}\big(\mathcal D^{a}\rho\big)\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{d}{}^{e}\big(\mathcal D^{f}\lambda{}_{i}\big)\\
&+\frac{145i}{384}\widehat F{}^{c}{}^{d}T{}^{e}{}^{f}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{R(Q){}^{a}{}^{b}{}^{i}}\lambda{}_{i} -\frac{403i}{18432}\widehat F{}^{d}{}^{e}T{}^{a}{}^{f}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{R(Q){}^{b}{}^{c}{}^{i}}\lambda{}_{i}\\
&-\frac{299i}{4608}\widehat F{}^{a}{}^{d}T{}^{e}{}^{f}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{R(Q){}^{b}{}^{c}{}^{i}}\lambda{}_{i} +\frac{185}{6144}\widehat F{}^{e}{}^{f}\epsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\big(\mathcal D^{b}R(Q){}^{c}{}^{d}{}^{i}\big)}\gamma{}_{b}\lambda{}_{i}\\
&-\frac{79i}{576}\widehat F{}^{f}{}^{g}T{}_{d}{}_{e}\epsilon{}^{a}{}_{b}{}_{c}{}_{f}{}_{g}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{d}{}^{e}\lambda{}_{i} -\frac{125i}{512}\widehat F{}_{d}{}^{f}T{}_{f}{}^{g}\epsilon{}^{a}{}_{b}{}_{c}{}_{e}{}_{g}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{d}{}^{e}\lambda{}_{i}\\
&-\frac{5i}{384}\widehat F{}_{d}{}_{e}T{}^{f}{}^{g}\epsilon{}^{a}{}_{b}{}_{c}{}_{f}{}_{g}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{d}{}^{e}\lambda{}_{i} -\frac{589i}{1536}\widehat F{}_{d}{}^{f}T{}^{a}{}^{g}\epsilon{}_{b}{}_{c}{}_{e}{}_{f}{}_{g}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{d}{}^{e}\lambda{}_{i}\\
&-\frac{133i}{768}\widehat F{}^{e}{}^{f}T{}_{e}{}^{g}\epsilon{}_{b}{}_{c}{}_{d}{}_{f}{}_{g}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{a}{}^{d}\lambda{}_{i} +\frac{131i}{2304}\widehat F{}_{d}{}^{e}T{}^{f}{}^{g}\epsilon{}_{b}{}_{c}{}_{e}{}_{f}{}_{g}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{a}{}^{d}\lambda{}_{i}\\
&+\frac{469i}{1536}\widehat F{}_{d}{}^{f}T{}_{e}{}^{g}\epsilon{}^{a}{}_{b}{}_{c}{}_{f}{}_{g}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{d}{}^{e}\lambda{}_{i} +\frac{29i}{256}\widehat F{}^{f}{}^{g}T{}_{d}{}_{f}\epsilon{}^{a}{}_{b}{}_{c}{}_{e}{}_{g}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{d}{}^{e}\lambda{}_{i}\\
&-\frac{851i}{4608}\widehat F{}^{f}{}^{g}T{}^{a}{}_{d}\epsilon{}_{b}{}_{c}{}_{e}{}_{f}{}_{g}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{d}{}^{e}\lambda{}_{i} -\frac{1243i}{4608}\widehat F{}^{e}{}^{f}T{}_{d}{}^{g}\epsilon{}_{b}{}_{c}{}_{e}{}_{f}{}_{g}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{a}{}^{d}\lambda{}_{i}\\
&-\frac{217i}{288}\widehat F{}^{a}{}_{d}T{}^{f}{}^{g}\epsilon{}_{b}{}_{c}{}_{e}{}_{f}{}_{g}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{d}{}^{e}\lambda{}_{i} +\frac{197i}{768}\widehat F{}^{a}{}^{f}T{}_{d}{}^{g}\epsilon{}_{b}{}_{c}{}_{e}{}_{f}{}_{g}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{d}{}^{e}\lambda{}_{i}\\
&-\frac{37i}{96}\widehat F{}_{b}{}^{e}T{}^{f}{}^{g}\epsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{a}{}^{d}\lambda{}_{i} -\frac{73i}{2304}\widehat F{}^{d}{}^{e}T{}^{f}{}^{g}\epsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{a}{}_{b}\lambda{}_{i}\\
&-\frac{13i}{384}\widehat F{}^{e}{}^{f}T{}_{b}{}^{g}\epsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{a}{}^{d}\lambda{}_{i} -\frac{35i}{9}\widehat F{}^{c}{}^{d}T{}^{e}{}^{f}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\chi{}^{i}}\gamma{}^{a}{}^{b}\lambda{}_{i}\\
&+\frac{1}{32}\widehat F{}_{d}{}^{e}\epsilon{}^{a}{}_{b}{}_{c}{}_{e}{}_{f}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{d}\big(\mathcal D^{f}\lambda{}_{i}\big) -\frac{3}{128}\widehat F{}^{d}{}^{e}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{a}\big(\mathcal D^{f}\lambda{}_{i}\big)\\
&-4\widehat F{}^{c}{}^{d}\epsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\chi{}^{i}}\gamma{}^{b}\big(\mathcal D^{e}\lambda{}_{i}\big) -\frac{i}{128}\big(\mathcal D_{e}\rho\big)\epsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{f}\overline{\big(\mathcal D^{b}R(Q){}^{c}{}^{d}{}^{i}\big)}\gamma{}^{e}{}^{f}\lambda{}_{i}\\
&+\frac{3i}{128}\big(\mathcal D_{d}\rho\big)\epsilon{}^{a}{}_{b}{}_{c}{}_{e}{}_{f}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{d}{}^{e}\big(\mathcal D^{f}\lambda{}_{i}\big) -\frac{19}{3072}\widehat F{}^{e}{}^{f}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\big(\mathcal D^{b}R(Q){}^{c}{}^{d}{}^{i}\big)}\gamma{}^{a}\lambda{}_{i}\\
&+\frac{25}{3072}\widehat F{}_{e}{}^{f}\epsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{f}\overline{\big(\mathcal D^{b}R(Q){}^{c}{}^{d}{}^{i}\big)}\gamma{}^{e}\lambda{}_{i} -\frac{3}{64}\big(\mathcal D^{e}\widehat F{}^{a}{}^{f}\big)\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{d}\lambda{}_{i}
\end{aligned}
\tag{CTF-E2F2-8}
```

```math
\begin{aligned}
&-\frac{3}{32}\big(\mathcal D^{e}\widehat F{}_{b}{}^{f}\big)\epsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{d}\lambda{}_{i} +\frac{7i}{32}\big(\mathcal D_{d}\widehat F{}^{a}{}_{c}\big)\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}_{b}{}^{d}\lambda{}_{i}\\
&-\frac{3i}{128}\big(\mathcal D^{d}\widehat F{}^{a}{}_{d}\big)\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}_{b}{}_{c}\lambda{}_{i} -\frac{7i}{64}\big(\mathcal D^{d}\widehat F{}_{c}{}_{d}\big)\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{a}{}_{b}\lambda{}_{i}\\
&-\frac{5i}{32}\big(\mathcal D_{c}\widehat F{}_{b}{}_{d}\big)\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}^{c}{}^{d}\lambda{}_{i} -\frac{5i}{64}\big(\mathcal D^{d}\widehat F{}_{c}{}_{d}\big)\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}_{b}{}^{c}\lambda{}_{i}\\
&-\frac{i}{64}\big(\mathcal D^{c}\widehat F{}_{b}{}_{c}\big)\overline{R(Q){}^{a}{}^{b}{}^{i}}\lambda{}_{i} +\frac{3}{32}\big(\mathcal D_{b}\widehat F{}^{e}{}^{f}\big)\epsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{d}\lambda{}_{i}\\
&-\frac{9i}{64}\big(\mathcal D_{c}\widehat F{}^{a}{}_{d}\big)\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}_{b}{}^{d}\lambda{}_{i} -\frac{i}{64}\big(\mathcal D_{b}\widehat F{}_{c}{}_{d}\big)\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{a}{}^{d}\lambda{}_{i}\\
&-\frac{7i}{64}\big(\mathcal D_{b}\widehat F{}^{a}{}_{c}\big)\overline{R(Q){}^{b}{}^{c}{}^{i}}\lambda{}_{i} -\frac{21i}{128}\big(\mathcal D_{b}\widehat F{}_{c}{}_{d}\big)\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}^{c}{}^{d}\lambda{}_{i}\\
&-\frac{3i}{64}\big(\mathcal D^{a}\widehat F{}_{c}{}_{d}\big)\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}_{b}{}^{d}\lambda{}_{i} +\frac{7i}{128}\big(\mathcal D^{a}\widehat F{}_{b}{}_{c}\big)\overline{R(Q){}^{b}{}^{c}{}^{i}}\lambda{}_{i}\\
&+\frac{3}{256}\big(\mathcal D^{d}\widehat F{}^{e}{}^{f}\big)\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{a}\lambda{}_{i} +\frac{7}{128}\big(\mathcal D^{e}\widehat F{}_{d}{}^{f}\big)\epsilon{}^{a}{}_{b}{}_{c}{}_{e}{}_{f}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{d}\lambda{}_{i}\\
&-\frac{7i}{128}\big(\mathcal D^{f}\mathcal D_{b}\rho\big)\epsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{d}{}^{e}\lambda{}_{i} -\frac{9}{64}\big(\mathcal D_{c}\mathcal D_{b}\rho\big)\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}^{c}\lambda{}_{i}\\
&-\frac{3}{32}\big(\mathcal D^{a}\mathcal D_{c}\rho\big)\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}_{b}\lambda{}_{i} +\frac{i}{32}\big(\mathcal D^{e}\mathcal D^{f}\rho\big)\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{a}{}^{d}\lambda{}_{i}\\
&+\frac{11i}{128}\big(\mathcal D^{d}\mathcal D^{e}\rho\big)\epsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{R(Q){}^{b}{}^{c}{}^{i}}\lambda{}_{i} +\frac{3i}{64}\big(\mathcal D_{b}\mathcal D^{f}\rho\big)\epsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{d}{}^{e}\lambda{}_{i}\\
&-\frac{5}{32}\big(\mathcal D_{c}\mathcal D^{a}\rho\big)\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}_{b}\lambda{}_{i} -\frac{11}{32}\big(\mathcal D_{b}\mathcal D_{c}\rho\big)\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}^{c}\lambda{}_{i}\\
&-\frac{11}{1536}\widehat F{}^{e}{}^{f}\epsilon{}^{a}{}_{b}{}_{d}{}_{e}{}_{f}\overline{\big(\mathcal D^{b}R(Q){}^{c}{}^{d}{}^{i}\big)}\gamma{}_{c}\lambda{}_{i} +\frac{229i}{1152}\widehat F{}^{f}{}^{g}T{}_{b}{}_{d}\epsilon{}^{a}{}_{c}{}_{e}{}_{f}{}_{g}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{d}{}^{e}\lambda{}_{i}\\
&-\frac{313i}{2304}\widehat F{}^{e}{}^{f}T{}_{c}{}^{g}\epsilon{}^{a}{}_{d}{}_{e}{}_{f}{}_{g}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}_{b}{}^{d}\lambda{}_{i} +\frac{37i}{768}\widehat F{}_{d}{}^{f}T{}_{b}{}^{g}\epsilon{}^{a}{}_{c}{}_{e}{}_{f}{}_{g}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{d}{}^{e}\lambda{}_{i}\\
&-\frac{91i}{1152}\widehat F{}^{e}{}^{f}T{}_{c}{}^{g}\epsilon{}_{b}{}_{d}{}_{e}{}_{f}{}_{g}\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}^{c}{}^{d}\lambda{}_{i} +\frac{7i}{48}\widehat F{}^{d}{}^{e}T{}^{f}{}^{g}\epsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g}\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}_{b}{}^{c}\lambda{}_{i}\\
&+\frac{i}{128}\widehat F{}_{c}{}^{e}T{}^{f}{}^{g}\epsilon{}_{b}{}_{d}{}_{e}{}_{f}{}_{g}\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}^{c}{}^{d}\lambda{}_{i} -\frac{41i}{1536}\widehat F{}_{b}{}^{f}T{}_{d}{}^{g}\epsilon{}^{a}{}_{c}{}_{e}{}_{f}{}_{g}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{d}{}^{e}\lambda{}_{i}\\
&+\frac{1237i}{4608}\widehat F{}^{e}{}^{f}T{}_{d}{}^{g}\epsilon{}^{a}{}_{c}{}_{e}{}_{f}{}_{g}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}_{b}{}^{d}\lambda{}_{i} +\frac{41i}{1536}\widehat F{}^{e}{}^{f}T{}_{e}{}^{g}\epsilon{}^{a}{}_{c}{}_{d}{}_{f}{}_{g}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}_{b}{}^{d}\lambda{}_{i}\\
&-\frac{213i}{512}\widehat F{}_{c}{}^{e}T{}^{f}{}^{g}\epsilon{}^{a}{}_{d}{}_{e}{}_{f}{}_{g}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}_{b}{}^{d}\lambda{}_{i} +\frac{673i}{3072}\widehat F{}^{d}{}^{e}T{}^{f}{}^{g}\epsilon{}^{a}{}_{d}{}_{e}{}_{f}{}_{g}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}_{b}{}_{c}\lambda{}_{i}
\end{aligned}
\tag{CTF-E2F2-9}
```

```math
\begin{aligned}
&+\frac{71i}{192}\widehat F{}_{b}{}_{d}T{}^{f}{}^{g}\epsilon{}^{a}{}_{c}{}_{e}{}_{f}{}_{g}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{d}{}^{e}\lambda{}_{i} -\frac{23i}{96}\widehat F{}_{d}{}^{e}T{}^{f}{}^{g}\epsilon{}^{a}{}_{c}{}_{e}{}_{f}{}_{g}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}_{b}{}^{d}\lambda{}_{i}\\
&-\frac{473i}{2304}\widehat F{}^{e}{}^{f}T{}^{a}{}^{g}\epsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}_{b}{}^{d}\lambda{}_{i} -\frac{11i}{96}\widehat F{}^{a}{}^{e}T{}^{f}{}^{g}\epsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}_{b}{}^{d}\lambda{}_{i}\\
&-\frac{107i}{12}\widehat F{}^{d}{}^{e}T{}_{b}{}^{f}\epsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\chi{}^{i}}\gamma{}^{b}{}^{c}\lambda{}_{i} -\frac{91i}{9}\widehat F{}_{b}{}^{d}T{}^{e}{}^{f}\epsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\chi{}^{i}}\gamma{}^{b}{}^{c}\lambda{}_{i}\\
&+\frac{260i}{27}T{}^{a}{}^{d}T{}_{b}{}^{e}T{}^{f}{}^{g}\epsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g}\overline{\lambda{}^{i}}\gamma{}^{b}{}^{c}\lambda{}_{i} -\frac{580i}{27}T{}_{b}{}^{d}T{}_{c}{}^{e}T{}^{f}{}^{g}\epsilon{}^{a}{}_{d}{}_{e}{}_{f}{}_{g}\overline{\lambda{}^{i}}\gamma{}^{b}{}^{c}\lambda{}_{i}\\
&+\frac{28i}{9}T{}_{b}{}^{d}T{}_{d}{}^{e}T{}^{f}{}^{g}\epsilon{}^{a}{}_{c}{}_{e}{}_{f}{}_{g}\overline{\lambda{}^{i}}\gamma{}^{b}{}^{c}\lambda{}_{i} +\frac{3}{128}\widehat F{}^{d}{}^{e}\epsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}_{b}\big(\mathcal D^{f}\lambda{}_{i}\big)\\
&-\frac{3}{128}\big(\mathcal D^{d}\widehat F{}^{e}{}^{f}\big)\epsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}_{b}\lambda{}_{i} -\frac{i}{256}\big(\mathcal D^{f}\mathcal D^{a}\rho\big)\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{d}{}^{e}\lambda{}_{i}\\
&-\frac{i}{128}\big(\mathcal D^{e}\mathcal D^{f}\rho\big)\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}^{c}{}^{d}\lambda{}_{i} -\frac{i}{2}T{}^{e}{}^{f}\epsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\big(\mathcal D_{b}\lambda{}^{i}\big)}\gamma{}^{b}{}^{c}\big(\mathcal D^{d}\lambda{}_{i}\big)\\
&+\frac{i}{2}T{}^{e}{}^{f}\epsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\lambda{}^{i}}\gamma{}^{b}{}^{c}\big(\mathcal D^{d}\mathcal D_{b}\lambda{}_{i}\big) -\frac{i}{2}T{}^{e}{}^{f}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\lambda{}^{i}}\gamma{}^{a}{}^{b}\big(\mathcal D^{c}\mathcal D^{d}\lambda{}_{i}\big)\\
&-\frac{i}{6}\big(\mathcal D^{e}T{}_{b}{}^{f}\big)\epsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\lambda{}^{i}}\gamma{}^{b}{}^{c}\big(\mathcal D^{d}\lambda{}_{i}\big) -\frac{i}{12}\big(\mathcal D_{b}T{}^{e}{}^{f}\big)\epsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\lambda{}^{i}}\gamma{}^{b}{}^{c}\big(\mathcal D^{d}\lambda{}_{i}\big)\\
&+\frac{i}{16}\widehat F{}_{b}{}^{c}\overline{R(Q){}^{a}{}^{b}{}^{i}}\big(\mathcal D_{c}\lambda{}_{i}\big) -\frac{i}{64}\big(\mathcal D_{d}\widehat F{}_{b}{}_{c}\big)\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{a}{}^{d}\lambda{}_{i}\\
&-\frac{1}{32}\big(\mathcal D^{e}\widehat F{}_{e}{}^{f}\big)\epsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{f}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{d}\lambda{}_{i} +\frac{1}{64}\big(\mathcal D^{d}\widehat F{}^{e}{}^{f}\big)\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}^{c}\lambda{}_{i}\\
&-\frac{1}{64}\big(\mathcal D^{a}\widehat F{}^{e}{}^{f}\big)\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{d}\lambda{}_{i} +\frac{i}{128}\big(\mathcal D^{a}\mathcal D^{f}\rho\big)\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{d}{}^{e}\lambda{}_{i}\\
&-\frac{1}{32}\big(\mathcal D_{b}\mathcal D_{c}\rho\big)\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{a}\lambda{}_{i} +\frac{i}{3}T{}^{d}{}^{e}\epsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\lambda{}^{i}}\big(\mathcal D^{b}\mathcal D^{c}\lambda{}_{i}\big)\\
&-\frac{2}{3}T{}_{b}{}_{c}\overline{\lambda{}^{i}}\gamma{}^{b}\big(\mathcal D^{a}\mathcal D^{c}\lambda{}_{i}\big) -\frac{2}{3}T{}^{a}{}_{c}\overline{\lambda{}^{i}}\gamma{}^{b}\big(\mathcal D_{b}\mathcal D^{c}\lambda{}_{i}\big)
\end{aligned}
\tag{CTF-E2F2-10}
```

#### Constrained vector: $`n=3`$, explicit degree $`0`$

```math
\begin{aligned}
\mathcal E_{3}^{(0)a}={}&-\frac{1}{4}\big(\mathcal D^{b}\widehat F{}^{a}{}_{b}\big)\widehat F^2 -8\big(\mathcal D^{b}\rho\big)T{}^{a}{}_{b}\widehat F^2\\
&-\frac{1}{2}\widehat F{}^{b}{}^{c}T{}^{d}{}^{e}\epsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{e}\widehat F^2 -2Y{}^{i}{}^{j}\big(\mathcal D^{b}Y{}_{i}{}_{j}\big)\widehat F{}^{a}{}_{b}\\
&-\big(\mathcal D^{b}\widehat F{}^{a}{}_{b}\big)Y^2 -\frac{3}{2}\big(\mathcal D^{b}\widehat F{}^{a}{}_{b}\big)\big(\mathcal D^{c}\rho\big)\big(\mathcal D_{c}\rho\big)\\
&+16\big(\mathcal D^{b}\rho\big)\big(\mathcal D_{b}\rho\big)\big(\mathcal D^{c}\rho\big)T{}^{a}{}_{c} -\frac{5}{4}\widehat F{}^{b}{}^{c}\big(\mathcal D^{d}\rho\big)\big(\mathcal D_{d}\rho\big)T{}^{e}{}^{f}\epsilon{}^{a}{}_{b}{}_{c}{}_{e}{}_{f}\\
&+\widehat F{}^{b}{}^{c}\widehat F{}_{b}{}^{d}\big(\mathcal D_{c}\widehat F{}^{a}{}_{d}\big) -16\widehat F{}^{a}{}^{b}\widehat F{}_{b}{}^{c}\big(\mathcal D^{d}\rho\big)T{}_{c}{}_{d}\\
&-16\widehat F{}^{a}{}^{b}\widehat F{}^{c}{}^{d}\big(\mathcal D_{b}\rho\big)T{}_{c}{}_{d} +16\widehat F{}^{a}{}^{b}\widehat F{}^{c}{}^{d}\big(\mathcal D_{c}\rho\big)T{}_{b}{}_{d}\\
&+16\widehat F{}^{b}{}^{c}\widehat F{}_{b}{}^{d}\big(\mathcal D_{c}\rho\big)T{}^{a}{}_{d} +\frac{1}{8}\widehat F{}^{b}{}^{c}\widehat F{}^{d}{}^{e}\big(\mathcal D^{f}\mathcal D^{a}\rho\big)\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\\
&-\frac{107}{24}\widehat F{}^{a}{}^{b}\widehat F{}_{b}{}^{c}\widehat F{}^{d}{}^{e}T{}^{f}{}^{g}\epsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g} -\frac{13}{2}\widehat F{}^{a}{}^{b}\widehat F{}^{c}{}^{d}\widehat F{}^{e}{}^{f}T{}_{c}{}^{g}\epsilon{}_{b}{}_{d}{}_{e}{}_{f}{}_{g}\\
&+\frac{11}{12}\widehat F{}^{b}{}^{c}\widehat F{}_{b}{}^{d}\widehat F{}^{e}{}^{f}T{}_{c}{}^{g}\epsilon{}^{a}{}_{d}{}_{e}{}_{f}{}_{g} -\frac{7}{4}\widehat F{}^{b}{}^{c}\widehat F{}^{d}{}^{e}\widehat F{}^{f}{}^{g}T{}^{a}{}_{b}\epsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g}\\
&+\frac{1}{12}\widehat F{}^{b}{}^{c}\widehat F{}^{d}{}^{e}\widehat F{}^{f}{}^{g}T{}_{b}{}_{c}\epsilon{}^{a}{}_{d}{}_{e}{}_{f}{}_{g} -\frac{1}{4}\widehat F{}^{b}{}^{c}\widehat F{}^{d}{}^{e}\widehat F{}^{f}{}^{g}T{}_{b}{}_{d}\epsilon{}^{a}{}_{c}{}_{e}{}_{f}{}_{g}\\
&-\frac{1}{3}\widehat F{}^{a}{}^{b}\widehat F{}^{c}{}^{d}\widehat F{}^{e}{}^{f}T{}_{b}{}^{g}\epsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g} +\frac{1}{2}\widehat F{}^{b}{}^{c}\big(\mathcal D^{d}\widehat F{}^{a}{}^{e}\big)\big(\mathcal D^{f}\rho\big)\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\\
&+\frac{5}{4}\widehat F{}^{b}{}^{c}\big(\mathcal D^{a}\rho\big)\big(\mathcal D^{d}\rho\big)T{}^{e}{}^{f}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f} -\widehat F{}^{a}{}^{b}\big(\mathcal D_{b}\rho\big)\big(\Box^c \rho\big)\\
&-2\widehat F{}^{a}{}^{b}\big(\mathcal D^{c}\rho\big)\big(\mathcal D_{c}\mathcal D_{b}\rho\big) +\widehat F{}^{b}{}^{c}\widehat F{}_{b}{}^{d}\widehat F{}_{c}{}^{e}T{}^{f}{}^{g}\epsilon{}^{a}{}_{d}{}_{e}{}_{f}{}_{g}\\
&+\frac{1}{8}\widehat F{}^{b}{}^{c}\big(\mathcal D_{b}\widehat F{}^{d}{}^{e}\big)\big(\mathcal D^{f}\rho\big)\epsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f} +\frac{11}{2}\widehat F{}^{b}{}^{c}\big(\mathcal D_{b}\rho\big)\big(\mathcal D^{d}\rho\big)T{}^{e}{}^{f}\epsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f}\\
&+\widehat F{}^{b}{}^{c}\big(\mathcal D_{b}\rho\big)\big(\mathcal D_{c}\mathcal D^{a}\rho\big) -\widehat F{}^{a}{}^{b}\widehat F{}_{b}{}^{c}\big(\mathcal D^{d}\widehat F{}_{c}{}_{d}\big)\\
&+\frac{3}{4}\widehat F{}^{b}{}^{c}\big(\mathcal D^{d}\widehat F{}_{d}{}^{e}\big)\big(\mathcal D^{f}\rho\big)\epsilon{}^{a}{}_{b}{}_{c}{}_{e}{}_{f} -\big(\mathcal D^{b}\widehat F{}_{b}{}^{c}\big)\big(\mathcal D^{a}\rho\big)\big(\mathcal D_{c}\rho\big)\\
&-\frac{1}{8}\widehat F{}^{b}{}^{c}\widehat F{}^{d}{}^{e}\big(\Box^c \rho\big)\epsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{e} -\frac{3}{8}\widehat F{}^{b}{}^{c}\big(\mathcal D^{d}\widehat F{}^{e}{}^{f}\big)\big(\mathcal D_{d}\rho\big)\epsilon{}^{a}{}_{b}{}_{c}{}_{e}{}_{f}\\
&+\frac{5}{2}\widehat F{}^{b}{}^{c}\big(\mathcal D^{d}\rho\big)\big(\mathcal D^{e}\rho\big)T{}_{d}{}^{f}\epsilon{}^{a}{}_{b}{}_{c}{}_{e}{}_{f} -\big(\mathcal D^{b}\widehat F{}^{a}{}^{c}\big)\big(\mathcal D_{b}\rho\big)\big(\mathcal D_{c}\rho\big)
\end{aligned}
\tag{CTF-E3F0-1}
```

```math
\begin{aligned}
&-\frac{1}{8}\widehat F{}^{a}{}^{b}\big(\mathcal D^{c}\widehat F{}^{d}{}^{e}\big)\big(\mathcal D^{f}\rho\big)\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f} +\frac{1}{4}\widehat F{}^{b}{}^{c}\big(\mathcal D^{d}\widehat F{}_{b}{}^{e}\big)\big(\mathcal D^{f}\rho\big)\epsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f}\\
&+\frac{1}{8}\widehat F{}^{b}{}^{c}\big(\mathcal D^{d}\widehat F{}^{e}{}^{f}\big)\big(\mathcal D_{b}\rho\big)\epsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f} -\frac{1}{8}\widehat F{}^{b}{}^{c}\big(\mathcal D^{a}\widehat F{}^{d}{}^{e}\big)\big(\mathcal D^{f}\rho\big)\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}
\end{aligned}
\tag{CTF-E3F0-2}
```

#### Constrained vector: $`n=3`$, explicit degree $`2`$

```math
\begin{aligned}
\mathcal E_{3}^{(2)a}={}&-\frac{1}{8}R(V){}^{b}{}^{c}{}^{i}{}^{j}\widehat F{}_{b}{}_{c}\overline{\lambda{}_{i}}\gamma{}^{a}\lambda{}_{j} +\frac{1}{2}\big(\Box^c Y{}^{i}{}^{j}\big)\overline{\lambda{}_{i}}\gamma{}^{a}\lambda{}_{j}\\
&-\frac{3i}{4}\big(\Box^c \rho\big)\overline{\lambda{}^{i}}\gamma{}^{a}{}^{b}\big(\mathcal D_{b}\lambda{}_{i}\big) -\frac{i}{4}\big(\Box^c \rho\big)\overline{\lambda{}^{i}}\big(\mathcal D^{a}\lambda{}_{i}\big)\\
&-\frac{5i}{8}\big(\Box^c \rho\big)T{}^{e}{}^{f}\epsilon{}^{a}{}_{b}{}_{c}{}_{e}{}_{f}\overline{\lambda{}^{i}}\gamma{}^{b}{}^{c}\lambda{}_{i} +\frac{1}{2}Y{}^{i}{}^{j}\overline{\lambda{}_{i}}\gamma{}^{a}\big(\Box^c \lambda{}_{j}\big)\\
&+3Y{}^{i}{}^{j}\big(\mathcal D^{c}T{}^{d}{}^{e}\big)\epsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\lambda{}_{i}}\gamma{}^{b}\lambda{}_{j} +2iY{}^{i}{}^{j}\big(\mathcal D^{b}T{}^{a}{}_{b}\big)\overline{\lambda{}_{i}}\lambda{}_{j}\\
&+6Y{}^{i}{}^{j}T{}^{d}{}^{e}\epsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\lambda{}_{i}}\gamma{}^{b}\big(\mathcal D^{c}\lambda{}_{j}\big) +4iY{}^{i}{}^{j}T{}^{a}{}_{b}\overline{\lambda{}_{i}}\big(\mathcal D^{b}\lambda{}_{j}\big)\\
&+16iY{}^{i}{}^{j}\big(\mathcal D_{b}\rho\big)\overline{\chi{}_{i}}\gamma{}^{a}{}^{b}\lambda{}_{j} +\frac{i}{3}Y{}_{i}{}^{j}\big(\mathcal D_{c}\rho\big)\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{a}{}_{b}\lambda{}_{j}\\
&-\frac{3i}{8}Y{}_{i}{}^{j}\big(\mathcal D_{b}\rho\big)\overline{R(Q){}^{a}{}^{b}{}^{i}}\lambda{}_{j} +\frac{71i}{1152}R(V){}^{b}{}^{c}{}^{i}{}^{j}Y{}_{i}{}^{k}\epsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\lambda{}_{j}}\gamma{}^{d}{}^{e}\lambda{}_{k}\\
&-\frac{1}{6}R(V){}^{a}{}^{b}{}^{i}{}^{j}Y{}_{i}{}^{k}\overline{\lambda{}_{j}}\gamma{}_{b}\lambda{}_{k} +\frac{3}{2}\big(\mathcal D^{b}Y{}^{i}{}^{j}\big)\overline{\lambda{}_{i}}\gamma{}^{a}\big(\mathcal D_{b}\lambda{}_{j}\big)\\
&-3\big(\mathcal D^{b}Y{}^{i}{}^{j}\big)T{}^{d}{}^{e}\epsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\lambda{}_{i}}\gamma{}^{c}\lambda{}_{j} +2i\big(\mathcal D^{b}Y{}^{i}{}^{j}\big)T{}^{a}{}_{b}\overline{\lambda{}_{i}}\lambda{}_{j}\\
&-\frac{5i}{4}\big(\mathcal D_{c}\rho\big)\overline{\lambda{}^{i}}\gamma{}^{a}{}^{b}\big(\mathcal D^{c}\mathcal D_{b}\lambda{}_{i}\big) -\frac{i}{4}\big(\mathcal D_{b}\rho\big)\overline{\lambda{}^{i}}\big(\mathcal D^{b}\mathcal D^{a}\lambda{}_{i}\big)\\
&-\frac{5i}{8}\big(\mathcal D^{d}\rho\big)\big(\mathcal D_{d}T{}^{e}{}^{f}\big)\epsilon{}^{a}{}_{b}{}_{c}{}_{e}{}_{f}\overline{\lambda{}^{i}}\gamma{}^{b}{}^{c}\lambda{}_{i} -\frac{77i}{24}\big(\mathcal D_{d}\rho\big)T{}^{e}{}^{f}\epsilon{}^{a}{}_{b}{}_{c}{}_{e}{}_{f}\overline{\lambda{}^{i}}\gamma{}^{b}{}^{c}\big(\mathcal D^{d}\lambda{}_{i}\big)\\
&+4\big(\mathcal D_{c}\rho\big)T{}^{a}{}_{b}\overline{\lambda{}^{i}}\gamma{}^{b}\big(\mathcal D^{c}\lambda{}_{i}\big) +8\big(\mathcal D^{b}\rho\big)\big(\mathcal D_{b}\rho\big)\overline{\chi{}^{i}}\gamma{}^{a}\lambda{}_{i}\\
&-2i\big(\mathcal D^{c}\rho\big)T{}^{d}{}^{e}\epsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\lambda{}^{i}}\big(\mathcal D^{b}\lambda{}_{i}\big) +\frac{31i}{12}\big(\mathcal D^{d}\rho\big)T{}^{e}{}^{f}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\lambda{}^{i}}\gamma{}^{b}{}^{c}\big(\mathcal D^{a}\lambda{}_{i}\big)\\
&+\frac{14i}{3}\big(\mathcal D^{e}\rho\big)T{}_{d}{}^{f}\epsilon{}^{a}{}_{b}{}_{c}{}_{e}{}_{f}\overline{\lambda{}^{i}}\gamma{}^{b}{}^{c}\big(\mathcal D^{d}\lambda{}_{i}\big) +\frac{i}{2}\big(\mathcal D^{e}\rho\big)T{}^{a}{}^{f}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\lambda{}^{i}}\gamma{}^{b}{}^{c}\big(\mathcal D^{d}\lambda{}_{i}\big)\\
&+\frac{11i}{4}\big(\mathcal D^{e}\rho\big)T{}_{e}{}^{f}\epsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{f}\overline{\lambda{}^{i}}\gamma{}^{b}{}^{c}\big(\mathcal D^{d}\lambda{}_{i}\big) +4\big(\mathcal D^{c}\rho\big)T{}_{b}{}_{c}\overline{\lambda{}^{i}}\gamma{}^{b}\big(\mathcal D^{a}\lambda{}_{i}\big)\\
&-4\big(\mathcal D^{c}\rho\big)T{}^{a}{}_{c}\overline{\lambda{}^{i}}\gamma{}^{b}\big(\mathcal D_{b}\lambda{}_{i}\big) +\frac{5i}{8}\big(\mathcal D^{a}\rho\big)T{}^{e}{}^{f}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\lambda{}^{i}}\gamma{}^{b}{}^{c}\big(\mathcal D^{d}\lambda{}_{i}\big)\\
&-8i\big(\mathcal D^{d}\rho\big)T{}^{a}{}_{d}T{}_{b}{}_{c}\overline{\lambda{}^{i}}\gamma{}^{b}{}^{c}\lambda{}_{i} -32i\big(\mathcal D_{b}\rho\big)T{}^{a}{}^{d}T{}_{c}{}_{d}\overline{\lambda{}^{i}}\gamma{}^{b}{}^{c}\lambda{}_{i}\\
&+32i\big(\mathcal D^{c}\rho\big)T{}_{b}{}^{d}T{}_{c}{}_{d}\overline{\lambda{}^{i}}\gamma{}^{a}{}^{b}\lambda{}_{i} -\frac{40i}{3}\big(\mathcal D_{b}\rho\big)T^2\overline{\lambda{}^{i}}\gamma{}^{a}{}^{b}\lambda{}_{i}
\end{aligned}
\tag{CTF-E3F2-1}
```

```math
\begin{aligned}
&-16i\big(\mathcal D^{d}\rho\big)T{}^{a}{}_{b}T{}_{c}{}_{d}\overline{\lambda{}^{i}}\gamma{}^{b}{}^{c}\lambda{}_{i} +\frac{5i}{4}\big(\mathcal D^{d}\rho\big)\big(\mathcal D^{e}T{}_{d}{}^{f}\big)\epsilon{}^{a}{}_{b}{}_{c}{}_{e}{}_{f}\overline{\lambda{}^{i}}\gamma{}^{b}{}^{c}\lambda{}_{i}\\
&-\frac{3i}{2}\big(\mathcal D^{d}\rho\big)\big(\mathcal D^{e}T{}_{e}{}^{f}\big)\epsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{f}\overline{\lambda{}^{i}}\gamma{}^{b}{}^{c}\lambda{}_{i} -\frac{i}{4}\big(\mathcal D^{c}\rho\big)\big(\mathcal D^{d}T{}^{e}{}^{f}\big)\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\lambda{}^{i}}\gamma{}^{a}{}^{b}\lambda{}_{i}\\
&+\frac{1}{8}R(V){}^{b}{}^{c}{}^{i}{}^{j}\big(\mathcal D^{e}\rho\big)\epsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\lambda{}_{i}}\gamma{}^{d}\lambda{}_{j} +iR(V){}^{a}{}^{b}{}^{i}{}^{j}\big(\mathcal D_{b}\rho\big)\overline{\lambda{}_{i}}\lambda{}_{j}\\
&-\frac{i}{64}R(M){}^{b}{}^{c}{}^{a}{}_{b}\widehat F{}^{f}{}^{g}\epsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g}\overline{\lambda{}^{i}}\gamma{}^{d}{}^{e}\lambda{}_{i} -\frac{i}{64}R(M){}^{b}{}^{c}{}^{a}{}^{d}\widehat F{}_{d}{}^{g}\epsilon{}_{b}{}_{c}{}_{e}{}_{f}{}_{g}\overline{\lambda{}^{i}}\gamma{}^{e}{}^{f}\lambda{}_{i}\\
&-\frac{i}{128}R(M){}^{b}{}^{c}{}_{b}{}_{c}\widehat F{}^{f}{}^{g}\epsilon{}^{a}{}_{d}{}_{e}{}_{f}{}_{g}\overline{\lambda{}^{i}}\gamma{}^{d}{}^{e}\lambda{}_{i} +\frac{i}{32}R(M){}^{b}{}^{c}{}_{b}{}^{d}\widehat F{}_{d}{}^{g}\epsilon{}^{a}{}_{c}{}_{e}{}_{f}{}_{g}\overline{\lambda{}^{i}}\gamma{}^{e}{}^{f}\lambda{}_{i}\\
&-\frac{i}{128}R(M){}^{b}{}^{c}{}^{d}{}^{e}\widehat F{}_{d}{}_{e}\epsilon{}^{a}{}_{b}{}_{c}{}_{f}{}_{g}\overline{\lambda{}^{i}}\gamma{}^{f}{}^{g}\lambda{}_{i} -\frac{i}{32}R(M){}^{b}{}^{c}{}_{b}{}^{d}\widehat F{}^{a}{}^{g}\epsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g}\overline{\lambda{}^{i}}\gamma{}^{e}{}^{f}\lambda{}_{i}\\
&+\frac{i}{64}R(M){}^{b}{}^{c}{}^{d}{}^{e}\widehat F{}^{a}{}_{d}\epsilon{}_{b}{}_{c}{}_{e}{}_{f}{}_{g}\overline{\lambda{}^{i}}\gamma{}^{f}{}^{g}\lambda{}_{i} +\frac{i}{32}R(M){}^{b}{}^{c}{}^{a}{}^{d}\widehat F{}_{b}{}^{g}\epsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g}\overline{\lambda{}^{i}}\gamma{}^{e}{}^{f}\lambda{}_{i}\\
&+\frac{i}{32}R(M){}^{b}{}^{c}{}_{b}{}^{d}\widehat F{}_{c}{}^{g}\epsilon{}^{a}{}_{d}{}_{e}{}_{f}{}_{g}\overline{\lambda{}^{i}}\gamma{}^{e}{}^{f}\lambda{}_{i} -\frac{i}{32}R(M){}^{b}{}^{c}{}^{d}{}^{e}\widehat F{}_{b}{}_{d}\epsilon{}^{a}{}_{c}{}_{e}{}_{f}{}_{g}\overline{\lambda{}^{i}}\gamma{}^{f}{}^{g}\lambda{}_{i}\\
&-\frac{i}{64}R(M){}^{b}{}^{c}{}^{d}{}^{e}\widehat F{}^{a}{}_{b}\epsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g}\overline{\lambda{}^{i}}\gamma{}^{f}{}^{g}\lambda{}_{i} -\frac{i}{128}R(M){}^{b}{}^{c}{}^{d}{}^{e}\widehat F{}_{b}{}_{c}\epsilon{}^{a}{}_{d}{}_{e}{}_{f}{}_{g}\overline{\lambda{}^{i}}\gamma{}^{f}{}^{g}\lambda{}_{i}\\
&+\frac{i}{64}R(M){}^{a}{}^{b}{}_{b}{}^{c}\widehat F{}^{f}{}^{g}\epsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g}\overline{\lambda{}^{i}}\gamma{}^{d}{}^{e}\lambda{}_{i} +\frac{i}{32}R(M){}^{a}{}^{b}{}^{c}{}^{d}\widehat F{}_{c}{}^{g}\epsilon{}_{b}{}_{d}{}_{e}{}_{f}{}_{g}\overline{\lambda{}^{i}}\gamma{}^{e}{}^{f}\lambda{}_{i}\\
&+\frac{i}{64}R(M){}^{a}{}^{b}{}^{c}{}^{d}\widehat F{}_{b}{}^{g}\epsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g}\overline{\lambda{}^{i}}\gamma{}^{e}{}^{f}\lambda{}_{i} -\frac{118i}{9}\widehat F{}^{d}{}^{e}T{}^{a}{}^{f}T{}_{f}{}^{g}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{g}\overline{\lambda{}^{i}}\gamma{}^{b}{}^{c}\lambda{}_{i}\\
&-\frac{547i}{36}\widehat F{}^{d}{}^{e}T{}^{a}{}_{d}T{}^{f}{}^{g}\epsilon{}_{b}{}_{c}{}_{e}{}_{f}{}_{g}\overline{\lambda{}^{i}}\gamma{}^{b}{}^{c}\lambda{}_{i} -\frac{103i}{36}\widehat F{}^{d}{}^{e}\epsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{e}T^2\overline{\lambda{}^{i}}\gamma{}^{b}{}^{c}\lambda{}_{i}\\
&+\frac{205i}{18}\widehat F{}^{d}{}^{e}T{}_{d}{}^{f}T{}_{f}{}^{g}\epsilon{}^{a}{}_{b}{}_{c}{}_{e}{}_{g}\overline{\lambda{}^{i}}\gamma{}^{b}{}^{c}\lambda{}_{i} -\frac{161i}{36}\widehat F{}^{d}{}^{e}T{}_{d}{}_{e}T{}^{f}{}^{g}\epsilon{}^{a}{}_{b}{}_{c}{}_{f}{}_{g}\overline{\lambda{}^{i}}\gamma{}^{b}{}^{c}\lambda{}_{i}\\
&+\frac{23i}{36}\widehat F{}^{a}{}_{b}T{}^{d}{}^{e}T{}^{f}{}^{g}\epsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g}\overline{\lambda{}^{i}}\gamma{}^{b}{}^{c}\lambda{}_{i} +\frac{38i}{9}\widehat F{}^{d}{}^{e}T{}^{a}{}^{f}T{}_{d}{}^{g}\epsilon{}_{b}{}_{c}{}_{e}{}_{f}{}_{g}\overline{\lambda{}^{i}}\gamma{}^{b}{}^{c}\lambda{}_{i}\\
&+\frac{59i}{18}\widehat F{}^{d}{}^{e}T{}_{d}{}^{f}T{}_{e}{}^{g}\epsilon{}^{a}{}_{b}{}_{c}{}_{f}{}_{g}\overline{\lambda{}^{i}}\gamma{}^{b}{}^{c}\lambda{}_{i} -\frac{3i}{2}\widehat F{}_{b}{}_{c}\big(\mathcal D^{d}T{}^{a}{}_{d}\big)\overline{\lambda{}^{i}}\gamma{}^{b}{}^{c}\lambda{}_{i}\\
&+i\widehat F{}_{b}{}^{d}\big(\mathcal D_{c}T{}^{a}{}_{d}\big)\overline{\lambda{}^{i}}\gamma{}^{b}{}^{c}\lambda{}_{i} -i\widehat F{}_{b}{}^{c}\big(\mathcal D^{d}T{}_{c}{}_{d}\big)\overline{\lambda{}^{i}}\gamma{}^{a}{}^{b}\lambda{}_{i}\\
&-\frac{3i}{2}\widehat F{}^{c}{}^{d}\big(\mathcal D_{b}T{}_{c}{}_{d}\big)\overline{\lambda{}^{i}}\gamma{}^{a}{}^{b}\lambda{}_{i} -3i\widehat F{}^{a}{}_{b}\big(\mathcal D^{d}T{}_{c}{}_{d}\big)\overline{\lambda{}^{i}}\gamma{}^{b}{}^{c}\lambda{}_{i}\\
&-3i\widehat F{}^{a}{}^{d}\big(\mathcal D_{b}T{}_{c}{}_{d}\big)\overline{\lambda{}^{i}}\gamma{}^{b}{}^{c}\lambda{}_{i} +3i\widehat F{}_{b}{}^{d}\big(\mathcal D_{d}T{}^{a}{}_{c}\big)\overline{\lambda{}^{i}}\gamma{}^{b}{}^{c}\lambda{}_{i}
\end{aligned}
\tag{CTF-E3F2-2}
```

```math
\begin{aligned}
&+3i\widehat F{}^{c}{}^{d}\big(\mathcal D_{c}T{}_{b}{}_{d}\big)\overline{\lambda{}^{i}}\gamma{}^{a}{}^{b}\lambda{}_{i} -\frac{5i}{2}\widehat F{}^{a}{}^{d}\big(\mathcal D_{d}T{}_{b}{}_{c}\big)\overline{\lambda{}^{i}}\gamma{}^{b}{}^{c}\lambda{}_{i}\\
&+\frac{73i}{1024}\widehat F{}_{b}{}_{c}\widehat F{}^{f}{}^{g}\epsilon{}^{a}{}_{d}{}_{e}{}_{f}{}_{g}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{d}{}^{e}\lambda{}_{i} -\frac{5}{64}\widehat F{}^{a}{}_{d}\widehat F{}_{b}{}_{c}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{d}\lambda{}_{i}\\
&+\frac{17}{64}Y{}_{i}{}^{j}\widehat F{}_{b}{}_{c}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{a}\lambda{}_{j} +\frac{i}{4}\widehat F{}_{b}{}_{c}\big(\mathcal D_{d}\rho\big)\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{a}{}^{d}\lambda{}_{i}\\
&-\frac{33i}{128}\widehat F{}_{b}{}_{c}\big(\mathcal D^{a}\rho\big)\overline{R(Q){}^{b}{}^{c}{}^{i}}\lambda{}_{i} +\frac{i}{16}R(V){}^{b}{}^{c}{}^{i}{}^{j}\widehat F{}^{d}{}^{e}\epsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\lambda{}_{i}}\lambda{}_{j}\\
&-\frac{7i}{32}\widehat F{}^{d}{}^{e}\epsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\lambda{}^{i}}\gamma{}^{b}{}^{c}\big(\Box^c \lambda{}_{i}\big) +\frac{1}{4}\widehat F{}^{a}{}_{b}\overline{\lambda{}^{i}}\gamma{}^{b}\big(\Box^c \lambda{}_{i}\big)\\
&-\frac{i}{4}\big(\mathcal D_{b}\rho\big)\overline{\lambda{}^{i}}\gamma{}^{a}{}^{b}\big(\Box^c \lambda{}_{i}\big) +\frac{i}{4}\big(\mathcal D^{a}\rho\big)\overline{\lambda{}^{i}}\big(\Box^c \lambda{}_{i}\big)\\
&-\frac{i}{16}\big(\Box^c \widehat F{}^{e}{}^{f}\big)\epsilon{}^{a}{}_{b}{}_{c}{}_{e}{}_{f}\overline{\lambda{}^{i}}\gamma{}^{b}{}^{c}\lambda{}_{i} -\frac{i}{4}\big(\Box^c \mathcal D_{b}\rho\big)\overline{\lambda{}^{i}}\gamma{}^{a}{}^{b}\lambda{}_{i}\\
&-\frac{5i}{2}\big(\mathcal D^{d}\widehat F{}^{a}{}_{d}\big)T{}_{b}{}_{c}\overline{\lambda{}^{i}}\gamma{}^{b}{}^{c}\lambda{}_{i} -\frac{11i}{3}\big(\mathcal D_{b}\widehat F{}^{a}{}^{d}\big)T{}_{c}{}_{d}\overline{\lambda{}^{i}}\gamma{}^{b}{}^{c}\lambda{}_{i}\\
&-\frac{i}{3}\big(\mathcal D_{b}\widehat F{}^{c}{}^{d}\big)T{}_{c}{}_{d}\overline{\lambda{}^{i}}\gamma{}^{a}{}^{b}\lambda{}_{i} +3i\big(\mathcal D^{d}\widehat F{}_{b}{}_{d}\big)T{}^{a}{}_{c}\overline{\lambda{}^{i}}\gamma{}^{b}{}^{c}\lambda{}_{i}\\
&+\frac{2i}{3}\big(\mathcal D_{b}\widehat F{}_{c}{}^{d}\big)T{}^{a}{}_{d}\overline{\lambda{}^{i}}\gamma{}^{b}{}^{c}\lambda{}_{i} -\frac{7i}{3}\big(\mathcal D^{d}\widehat F{}^{a}{}_{b}\big)T{}_{c}{}_{d}\overline{\lambda{}^{i}}\gamma{}^{b}{}^{c}\lambda{}_{i}\\
&-\frac{4i}{3}\big(\mathcal D^{c}\widehat F{}_{b}{}^{d}\big)T{}_{c}{}_{d}\overline{\lambda{}^{i}}\gamma{}^{a}{}^{b}\lambda{}_{i} -\frac{2i}{3}\big(\mathcal D^{d}\widehat F{}_{b}{}_{c}\big)T{}^{a}{}_{d}\overline{\lambda{}^{i}}\gamma{}^{b}{}^{c}\lambda{}_{i}\\
&+\frac{2i}{3}\big(\mathcal D^{a}\widehat F{}_{b}{}^{d}\big)T{}_{c}{}_{d}\overline{\lambda{}^{i}}\gamma{}^{b}{}^{c}\lambda{}_{i} +\frac{i}{2}\big(\mathcal D^{a}\rho\big)\big(\mathcal D^{d}T{}^{e}{}^{f}\big)\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\lambda{}^{i}}\gamma{}^{b}{}^{c}\lambda{}_{i}\\
&+\frac{i}{4}\big(\mathcal D^{d}\rho\big)\big(\mathcal D^{e}T{}^{a}{}^{f}\big)\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\lambda{}^{i}}\gamma{}^{b}{}^{c}\lambda{}_{i} +\frac{i}{8}\big(\mathcal D^{d}\rho\big)\big(\mathcal D^{a}T{}^{e}{}^{f}\big)\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\lambda{}^{i}}\gamma{}^{b}{}^{c}\lambda{}_{i}\\
&+\frac{5i}{12}\big(\mathcal D^{d}\mathcal D^{a}\rho\big)T{}^{e}{}^{f}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\lambda{}^{i}}\gamma{}^{b}{}^{c}\lambda{}_{i} +\frac{23i}{24}\big(\mathcal D^{d}\mathcal D^{e}\rho\big)T{}_{e}{}^{f}\epsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{f}\overline{\lambda{}^{i}}\gamma{}^{b}{}^{c}\lambda{}_{i}\\
&+\frac{7i}{24}\big(\mathcal D^{d}\mathcal D^{e}\rho\big)T{}^{a}{}^{f}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\lambda{}^{i}}\gamma{}^{b}{}^{c}\lambda{}_{i} +\frac{19i}{24}\big(\mathcal D^{d}\mathcal D^{e}\rho\big)T{}_{d}{}^{f}\epsilon{}^{a}{}_{b}{}_{c}{}_{e}{}_{f}\overline{\lambda{}^{i}}\gamma{}^{b}{}^{c}\lambda{}_{i}\\
&+\frac{5i}{24}\big(\mathcal D^{a}\mathcal D^{d}\rho\big)T{}^{e}{}^{f}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\lambda{}^{i}}\gamma{}^{b}{}^{c}\lambda{}_{i} +\frac{9i}{4}\widehat F{}_{b}{}^{c}T{}^{d}{}^{e}T{}^{f}{}^{g}\epsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g}\overline{\lambda{}^{i}}\gamma{}^{a}{}^{b}\lambda{}_{i}\\
&+\frac{13i}{9}\widehat F{}_{b}{}_{c}T{}^{d}{}^{e}T{}^{f}{}^{g}\epsilon{}^{a}{}_{d}{}_{e}{}_{f}{}_{g}\overline{\lambda{}^{i}}\gamma{}^{b}{}^{c}\lambda{}_{i} +\frac{73i}{2304}R(V){}^{b}{}^{c}{}^{i}{}^{j}Y{}_{i}{}_{j}\epsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\lambda{}^{k}}\gamma{}^{d}{}^{e}\lambda{}_{k}\\
&-\frac{3i}{4}\big(\mathcal D_{b}\rho\big)\big(\mathcal D^{d}T{}^{e}{}^{f}\big)\epsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\lambda{}^{i}}\gamma{}^{b}{}^{c}\lambda{}_{i} -\frac{i}{8}\big(\mathcal D^{d}\widehat F{}^{e}{}^{f}\big)\epsilon{}^{a}{}_{b}{}_{c}{}_{e}{}_{f}\overline{\lambda{}^{i}}\gamma{}^{b}{}^{c}\big(\mathcal D_{d}\lambda{}_{i}\big)
\end{aligned}
\tag{CTF-E3F2-3}
```

```math
\begin{aligned}
&+\frac{1}{4}\big(\mathcal D^{c}\widehat F{}^{a}{}_{b}\big)\overline{\lambda{}^{i}}\gamma{}^{b}\big(\mathcal D_{c}\lambda{}_{i}\big) -\frac{i}{2}\big(\mathcal D_{c}\mathcal D_{b}\rho\big)\overline{\lambda{}^{i}}\gamma{}^{a}{}^{b}\big(\mathcal D^{c}\lambda{}_{i}\big)\\
&+\frac{i}{4}\big(\mathcal D_{b}\mathcal D^{a}\rho\big)\overline{\lambda{}^{i}}\big(\mathcal D^{b}\lambda{}_{i}\big) +\frac{3}{4}\widehat F{}^{a}{}^{c}T{}^{e}{}^{f}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\lambda{}^{i}}\gamma{}^{b}\big(\mathcal D^{d}\lambda{}_{i}\big)\\
&-\frac{35}{12}\widehat F{}^{c}{}^{d}T{}^{e}{}^{f}\epsilon{}^{a}{}_{b}{}_{d}{}_{e}{}_{f}\overline{\lambda{}^{i}}\gamma{}^{b}\big(\mathcal D_{c}\lambda{}_{i}\big) -\widehat F{}^{c}{}^{d}T{}_{c}{}^{f}\epsilon{}^{a}{}_{b}{}_{d}{}_{e}{}_{f}\overline{\lambda{}^{i}}\gamma{}^{b}\big(\mathcal D^{e}\lambda{}_{i}\big)\\
&-5i\widehat F{}^{a}{}^{d}T{}_{b}{}_{c}\overline{\lambda{}^{i}}\gamma{}^{b}{}^{c}\big(\mathcal D_{d}\lambda{}_{i}\big) -6i\widehat F{}^{a}{}^{d}T{}_{c}{}_{d}\overline{\lambda{}^{i}}\gamma{}^{b}{}^{c}\big(\mathcal D_{b}\lambda{}_{i}\big)\\
&+6i\widehat F{}^{c}{}^{d}T{}_{b}{}_{d}\overline{\lambda{}^{i}}\gamma{}^{a}{}^{b}\big(\mathcal D_{c}\lambda{}_{i}\big) -3i\widehat F{}^{c}{}^{d}T{}_{c}{}_{d}\overline{\lambda{}^{i}}\gamma{}^{a}{}^{b}\big(\mathcal D_{b}\lambda{}_{i}\big)\\
&-\frac{5}{4}\widehat F{}^{c}{}^{d}T{}^{a}{}^{f}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\lambda{}^{i}}\gamma{}^{b}\big(\mathcal D^{e}\lambda{}_{i}\big) +6i\widehat F{}_{b}{}^{d}T{}^{a}{}_{c}\overline{\lambda{}^{i}}\gamma{}^{b}{}^{c}\big(\mathcal D_{d}\lambda{}_{i}\big)\\
&+2i\widehat F{}_{b}{}^{d}T{}^{a}{}_{d}\overline{\lambda{}^{i}}\gamma{}^{b}{}^{c}\big(\mathcal D_{c}\lambda{}_{i}\big) -\frac{41}{12}\widehat F{}^{c}{}^{d}T{}_{e}{}^{f}\epsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{f}\overline{\lambda{}^{i}}\gamma{}^{b}\big(\mathcal D^{e}\lambda{}_{i}\big)\\
&-6i\widehat F{}^{a}{}_{b}T{}_{c}{}_{d}\overline{\lambda{}^{i}}\gamma{}^{b}{}^{c}\big(\mathcal D^{d}\lambda{}_{i}\big) -2i\widehat F{}_{b}{}^{c}T{}_{c}{}_{d}\overline{\lambda{}^{i}}\gamma{}^{a}{}^{b}\big(\mathcal D^{d}\lambda{}_{i}\big)\\
&-3i\widehat F{}_{b}{}_{c}T{}^{a}{}_{d}\overline{\lambda{}^{i}}\gamma{}^{b}{}^{c}\big(\mathcal D^{d}\lambda{}_{i}\big) -\frac{13}{12}\widehat F{}^{c}{}^{d}T{}^{e}{}^{f}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\lambda{}^{i}}\gamma{}^{b}\big(\mathcal D^{a}\lambda{}_{i}\big)\\
&+\frac{31}{12}\widehat F{}_{b}{}^{c}T{}^{e}{}^{f}\epsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\lambda{}^{i}}\gamma{}^{b}\big(\mathcal D^{d}\lambda{}_{i}\big) -\frac{5}{3}\widehat F{}^{b}{}^{c}T{}^{e}{}^{f}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\lambda{}^{i}}\gamma{}^{a}\big(\mathcal D^{d}\lambda{}_{i}\big)\\
&+\frac{7i}{12}\big(\mathcal D_{b}\rho\big)T{}^{e}{}^{f}\epsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\lambda{}^{i}}\gamma{}^{b}{}^{c}\big(\mathcal D^{d}\lambda{}_{i}\big) -\frac{5i}{6}\big(\mathcal D^{d}\rho\big)T{}^{e}{}^{f}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\lambda{}^{i}}\gamma{}^{a}{}^{b}\big(\mathcal D^{c}\lambda{}_{i}\big)\\
&-\frac{3i}{4}\big(\mathcal D^{d}\mathcal D_{b}\rho\big)T{}^{e}{}^{f}\epsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\lambda{}^{i}}\gamma{}^{b}{}^{c}\lambda{}_{i} +\frac{3i}{4}\big(\mathcal D^{c}\mathcal D^{d}\rho\big)T{}^{e}{}^{f}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\lambda{}^{i}}\gamma{}^{a}{}^{b}\lambda{}_{i}\\
&+\frac{23i}{12}\widehat F{}^{d}{}^{e}T{}_{b}{}_{c}T{}^{f}{}^{g}\epsilon{}^{a}{}_{d}{}_{e}{}_{f}{}_{g}\overline{\lambda{}^{i}}\gamma{}^{b}{}^{c}\lambda{}_{i} -\frac{2i}{3}\widehat F{}^{d}{}^{e}T{}_{b}{}_{d}T{}^{f}{}^{g}\epsilon{}^{a}{}_{c}{}_{e}{}_{f}{}_{g}\overline{\lambda{}^{i}}\gamma{}^{b}{}^{c}\lambda{}_{i}\\
&-\frac{259i}{36}\widehat F{}^{d}{}^{e}T{}^{a}{}_{b}T{}^{f}{}^{g}\epsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g}\overline{\lambda{}^{i}}\gamma{}^{b}{}^{c}\lambda{}_{i} -2iD\big(\mathcal D_{b}\rho\big)\overline{\lambda{}^{i}}\gamma{}^{a}{}^{b}\lambda{}_{i}\\
&+8\widehat F{}^{c}{}^{d}\big(\mathcal D^{e}\rho\big)\epsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\chi{}^{i}}\gamma{}^{b}\lambda{}_{i} -\frac{82}{9}Y{}^{i}{}^{j}Y{}_{i}{}^{k}\overline{\chi{}_{j}}\gamma{}^{a}\lambda{}_{k}\\
&-\frac{25i}{384}Y{}_{i}{}^{j}\widehat F{}^{d}{}^{e}\epsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{R(Q){}^{b}{}^{c}{}^{i}}\lambda{}_{j} -\frac{17i}{768}Y{}_{i}{}^{j}\widehat F{}^{e}{}^{f}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}^{c}{}^{d}\lambda{}_{j}\\
&+\frac{41i}{384}Y{}_{i}{}^{j}\widehat F{}^{a}{}^{f}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{d}{}^{e}\lambda{}_{j} -\frac{7i}{128}Y{}_{i}{}^{j}\widehat F{}_{b}{}^{f}\epsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{d}{}^{e}\lambda{}_{j}\\
&+\frac{13}{48}Y{}_{i}{}^{j}\widehat F{}_{b}{}_{c}\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}^{c}\lambda{}_{j} +\frac{55}{96}Y{}_{i}{}^{j}\widehat F{}^{a}{}_{c}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}_{b}\lambda{}_{j}
\end{aligned}
\tag{CTF-E3F2-4}
```

```math
\begin{aligned}
&-\frac{i}{64}\epsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{e}\widehat F^2\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{d}{}^{e}\lambda{}_{i} +\frac{1}{256}\widehat F^2\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}_{b}\lambda{}_{i}\\
&+\frac{i}{8}\widehat F{}^{b}{}^{c}\epsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\big(\mathcal D^{d}\lambda{}^{i}\big)}\big(\mathcal D^{e}\lambda{}_{i}\big) +\frac{5i}{32}\widehat F{}^{d}{}^{e}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\big(\mathcal D^{a}\lambda{}^{i}\big)}\gamma{}^{b}{}^{c}\big(\mathcal D^{f}\lambda{}_{i}\big)\\
&-\frac{5i}{32}\widehat F{}^{d}{}^{e}\epsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\big(\mathcal D^{f}\lambda{}^{i}\big)}\gamma{}^{b}{}^{c}\big(\mathcal D_{f}\lambda{}_{i}\big) -\frac{3i}{16}\widehat F{}^{d}{}^{e}\epsilon{}^{a}{}_{b}{}_{c}{}_{e}{}_{f}\overline{\big(\mathcal D_{d}\lambda{}^{i}\big)}\gamma{}^{b}{}^{c}\big(\mathcal D^{f}\lambda{}_{i}\big)\\
&-\frac{1}{4}\widehat F{}_{b}{}^{c}\overline{\big(\mathcal D^{a}\lambda{}^{i}\big)}\gamma{}^{b}\big(\mathcal D_{c}\lambda{}_{i}\big) -\frac{i}{12}Y{}_{i}{}^{j}\widehat F{}_{d}{}^{f}\epsilon{}^{a}{}_{b}{}_{c}{}_{e}{}_{f}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{d}{}^{e}\lambda{}_{j}\\
&-\frac{23i}{384}Y{}_{i}{}^{j}\widehat F{}^{e}{}^{f}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{a}{}^{d}\lambda{}_{j} -\frac{i}{4}Y{}^{i}{}^{j}\epsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\big(\mathcal D^{d}\lambda{}_{i}\big)}\gamma{}^{b}{}^{c}\big(\mathcal D^{e}\lambda{}_{j}\big)\\
&-\frac{1}{2}Y{}^{i}{}^{j}\overline{\big(\mathcal D^{a}\lambda{}_{i}\big)}\gamma{}^{b}\big(\mathcal D_{b}\lambda{}_{j}\big) +\frac{1}{2}Y{}^{i}{}^{j}\overline{\big(\mathcal D^{b}\lambda{}_{i}\big)}\gamma{}^{a}\big(\mathcal D_{b}\lambda{}_{j}\big)\\
&+\frac{41}{9}Y^2\overline{\chi{}^{i}}\gamma{}^{a}\lambda{}_{i} +\frac{13i}{192}\epsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{e}Y^2\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{d}{}^{e}\lambda{}_{i}\\
&-\frac{1}{8}Y^2\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}_{b}\lambda{}_{i} -\frac{3i}{128}Y{}_{i}{}^{j}Y{}_{j}{}^{k}\epsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{d}{}^{e}\lambda{}_{k}\\
&-\frac{11}{32}Y{}_{i}{}^{j}Y{}_{j}{}^{k}\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}_{b}\lambda{}_{k} +\frac{47i}{512}\big(\mathcal D^{f}\rho\big)\big(\mathcal D_{f}\rho\big)\epsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{d}{}^{e}\lambda{}_{i}\\
&-\frac{53}{128}\big(\mathcal D^{c}\rho\big)\big(\mathcal D_{c}\rho\big)\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}_{b}\lambda{}_{i} -\frac{3i}{2}\big(\mathcal D_{c}\rho\big)\overline{\big(\mathcal D_{b}\lambda{}^{i}\big)}\gamma{}^{a}{}^{b}\big(\mathcal D^{c}\lambda{}_{i}\big)\\
&+\frac{i}{4}\big(\mathcal D_{b}\rho\big)\overline{\big(\mathcal D^{a}\lambda{}^{i}\big)}\big(\mathcal D^{b}\lambda{}_{i}\big) +\frac{13}{192}Y{}_{i}{}^{j}\big(\mathcal D^{e}\rho\big)\epsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{d}\lambda{}_{j}\\
&-\frac{i}{96}Y{}_{i}{}^{j}\big(\mathcal D_{c}\rho\big)\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}_{b}{}^{c}\lambda{}_{j} -\frac{5i}{24}Y{}_{i}{}^{j}\big(\mathcal D^{a}\rho\big)\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}_{b}{}_{c}\lambda{}_{j}\\
&-\frac{25}{12}\widehat F{}^{c}{}^{d}T{}_{b}{}^{f}\epsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\lambda{}^{i}}\gamma{}^{b}\big(\mathcal D^{e}\lambda{}_{i}\big) -\frac{i}{9}\widehat F{}^{d}{}^{e}T{}^{a}{}^{f}T{}_{b}{}^{g}\epsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g}\overline{\lambda{}^{i}}\gamma{}^{b}{}^{c}\lambda{}_{i}\\
&+\frac{13i}{6}\widehat F{}^{d}{}^{e}T{}_{b}{}^{f}T{}_{c}{}^{g}\epsilon{}^{a}{}_{d}{}_{e}{}_{f}{}_{g}\overline{\lambda{}^{i}}\gamma{}^{b}{}^{c}\lambda{}_{i} -\frac{5i}{18}\widehat F{}^{d}{}^{e}T{}_{b}{}^{f}T{}_{f}{}^{g}\epsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{g}\overline{\lambda{}^{i}}\gamma{}^{b}{}^{c}\lambda{}_{i}\\
&-\frac{i}{4}\big(\mathcal D^{b}Y{}^{i}{}^{j}\big)\epsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\lambda{}_{i}}\gamma{}^{c}{}^{d}\big(\mathcal D^{e}\lambda{}_{j}\big) +\frac{1}{4}\big(\mathcal D^{e}\rho\big)\epsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\big(\mathcal D^{c}\lambda{}^{i}\big)}\gamma{}^{b}\big(\mathcal D^{d}\lambda{}_{i}\big)\\
&+\frac{1}{4}\big(\mathcal D^{c}\widehat F{}_{b}{}_{c}\big)\overline{\lambda{}^{i}}\gamma{}^{b}\big(\mathcal D^{a}\lambda{}_{i}\big) +\frac{1}{4}\big(\mathcal D_{b}\widehat F{}^{a}{}^{c}\big)\overline{\lambda{}^{i}}\gamma{}^{b}\big(\mathcal D_{c}\lambda{}_{i}\big)\\
&-\frac{1}{4}\big(\mathcal D^{b}\widehat F{}_{b}{}^{c}\big)\overline{\lambda{}^{i}}\gamma{}^{a}\big(\mathcal D_{c}\lambda{}_{i}\big) +\frac{1}{4}\big(\mathcal D^{c}\widehat F{}^{a}{}_{c}\big)\overline{\lambda{}^{i}}\gamma{}^{b}\big(\mathcal D_{b}\lambda{}_{i}\big)\\
&+\frac{i}{16}\big(\mathcal D^{d}\widehat F{}_{b}{}^{e}\big)\epsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\lambda{}^{i}}\gamma{}^{b}{}^{c}\big(\mathcal D^{f}\lambda{}_{i}\big) -\frac{i}{32}\big(\mathcal D^{c}\widehat F{}^{d}{}^{e}\big)\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\lambda{}^{i}}\gamma{}^{a}{}^{b}\big(\mathcal D^{f}\lambda{}_{i}\big)
\end{aligned}
\tag{CTF-E3F2-5}
```

```math
\begin{aligned}
&+\frac{i}{8}\big(\mathcal D^{d}\widehat F{}^{a}{}^{e}\big)\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\lambda{}^{i}}\gamma{}^{b}{}^{c}\big(\mathcal D^{f}\lambda{}_{i}\big) -\frac{2i}{3}\big(\mathcal D^{e}\rho\big)T{}_{b}{}^{f}\epsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\lambda{}^{i}}\gamma{}^{b}{}^{c}\big(\mathcal D^{d}\lambda{}_{i}\big)\\
&-\frac{1}{2}\big(\mathcal D^{b}Y{}^{i}{}^{j}\big)\overline{\lambda{}_{i}}\gamma{}_{b}\big(\mathcal D^{a}\lambda{}_{j}\big) -\big(\mathcal D^{a}Y{}^{i}{}^{j}\big)\overline{\lambda{}_{i}}\gamma{}^{b}\big(\mathcal D_{b}\lambda{}_{j}\big)\\
&-\frac{i}{4}\big(\mathcal D_{c}\mathcal D^{a}\rho\big)\overline{\lambda{}^{i}}\gamma{}^{b}{}^{c}\big(\mathcal D_{b}\lambda{}_{i}\big) +\frac{i}{4}\big(\mathcal D^{d}\mathcal D^{e}\rho\big)T{}_{b}{}^{f}\epsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\lambda{}^{i}}\gamma{}^{b}{}^{c}\lambda{}_{i}\\
&+\frac{2i}{3}\widehat F{}^{d}{}^{e}T{}_{b}{}^{f}T{}_{d}{}^{g}\epsilon{}^{a}{}_{c}{}_{e}{}_{f}{}_{g}\overline{\lambda{}^{i}}\gamma{}^{b}{}^{c}\lambda{}_{i} +3i\big(\mathcal D^{c}\widehat F{}_{c}{}^{d}\big)T{}_{b}{}_{d}\overline{\lambda{}^{i}}\gamma{}^{a}{}^{b}\lambda{}_{i}\\
&+\frac{i}{16}\widehat F{}^{d}{}^{e}\epsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\big(\mathcal D_{b}\lambda{}^{i}\big)}\gamma{}^{b}{}^{c}\big(\mathcal D^{f}\lambda{}_{i}\big) +\frac{5}{64}\widehat F{}_{b}{}^{d}\widehat F{}_{c}{}_{d}\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}^{c}\lambda{}_{i}\\
&-\frac{3}{32}\widehat F{}^{a}{}_{b}\widehat F{}_{c}{}_{d}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{d}\lambda{}_{i} -\frac{5}{32}\widehat F{}^{a}{}^{d}\widehat F{}_{c}{}_{d}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}_{b}\lambda{}_{i}\\
&-\frac{7i}{256}\widehat F{}_{b}{}_{d}\widehat F{}^{f}{}^{g}\epsilon{}^{a}{}_{c}{}_{e}{}_{f}{}_{g}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{d}{}^{e}\lambda{}_{i} +\frac{17i}{1024}\widehat F{}_{d}{}_{e}\widehat F{}^{f}{}^{g}\epsilon{}^{a}{}_{b}{}_{c}{}_{f}{}_{g}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{d}{}^{e}\lambda{}_{i}\\
&-\frac{11i}{1024}\widehat F{}^{d}{}^{e}\widehat F{}^{f}{}^{g}\epsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g}\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}_{b}{}^{c}\lambda{}_{i} -\frac{7i}{1024}\widehat F{}^{d}{}^{e}\widehat F{}^{f}{}^{g}\epsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{a}{}_{b}\lambda{}_{i}\\
&-\frac{9i}{1024}\widehat F{}^{d}{}^{e}\widehat F{}^{f}{}^{g}\epsilon{}^{a}{}_{d}{}_{e}{}_{f}{}_{g}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}_{b}{}_{c}\lambda{}_{i} +\frac{13i}{512}\widehat F{}^{c}{}^{d}\widehat F{}^{e}{}^{f}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{R(Q){}^{a}{}^{b}{}^{i}}\lambda{}_{i}\\
&+\frac{i}{32}\widehat F{}^{a}{}_{b}\widehat F{}^{f}{}^{g}\epsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{d}{}^{e}\lambda{}_{i} +\frac{17i}{512}\widehat F{}^{a}{}_{d}\widehat F{}^{f}{}^{g}\epsilon{}_{b}{}_{c}{}_{e}{}_{f}{}_{g}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{d}{}^{e}\lambda{}_{i}\\
&+\frac{3i}{512}\widehat F{}^{a}{}^{f}\widehat F{}_{f}{}^{g}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{g}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{d}{}^{e}\lambda{}_{i} -\frac{15i}{256}\widehat F{}_{b}{}^{f}\widehat F{}_{f}{}^{g}\epsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{g}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{d}{}^{e}\lambda{}_{i}\\
&-\frac{17i}{256}\widehat F{}^{a}{}^{f}\widehat F{}_{b}{}^{g}\epsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{d}{}^{e}\lambda{}_{i} -\frac{5i}{256}\widehat F{}_{b}{}^{f}\widehat F{}_{c}{}^{g}\epsilon{}^{a}{}_{d}{}_{e}{}_{f}{}_{g}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{d}{}^{e}\lambda{}_{i}\\
&-\frac{3i}{128}Y{}_{i}{}^{j}\widehat F{}^{e}{}^{f}\epsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}_{b}{}^{d}\lambda{}_{j} -\frac{5i}{32}\widehat F{}_{b}{}^{c}\big(\mathcal D_{c}\rho\big)\overline{R(Q){}^{a}{}^{b}{}^{i}}\lambda{}_{i}\\
&+\frac{35i}{128}\widehat F{}_{c}{}_{d}\big(\mathcal D_{b}\rho\big)\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}^{c}{}^{d}\lambda{}_{i} +\frac{11i}{64}\widehat F{}_{c}{}^{d}\big(\mathcal D_{d}\rho\big)\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}_{b}{}^{c}\lambda{}_{i}\\
&+\frac{13i}{64}\widehat F{}^{a}{}_{b}\big(\mathcal D_{c}\rho\big)\overline{R(Q){}^{b}{}^{c}{}^{i}}\lambda{}_{i} -\frac{i}{32}\widehat F{}^{a}{}_{d}\big(\mathcal D_{c}\rho\big)\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}_{b}{}^{d}\lambda{}_{i}\\
&+\frac{i}{8}\widehat F{}^{a}{}^{d}\big(\mathcal D_{d}\rho\big)\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}_{b}{}_{c}\lambda{}_{i} -\frac{7i}{32}\widehat F{}_{b}{}_{d}\big(\mathcal D_{c}\rho\big)\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{a}{}^{d}\lambda{}_{i}\\
&+\frac{3i}{16}\widehat F{}_{c}{}_{d}\big(\mathcal D^{a}\rho\big)\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}_{b}{}^{d}\lambda{}_{i} +\frac{3i}{32}\widehat F{}_{c}{}^{d}\big(\mathcal D_{d}\rho\big)\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{a}{}_{b}\lambda{}_{i}\\
&-\frac{13}{256}\widehat F{}^{e}{}^{f}\big(\mathcal D_{b}\rho\big)\epsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{d}\lambda{}_{i} -\frac{17}{256}\widehat F{}^{e}{}^{f}\big(\mathcal D_{d}\rho\big)\epsilon{}^{a}{}_{b}{}_{c}{}_{e}{}_{f}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{d}\lambda{}_{i}
\end{aligned}
\tag{CTF-E3F2-6}
```

```math
\begin{aligned}
&-\frac{11i}{64}\widehat F{}_{b}{}_{c}\big(\mathcal D_{d}\rho\big)\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}^{c}{}^{d}\lambda{}_{i} -\frac{5i}{16}\widehat F{}^{a}{}_{c}\big(\mathcal D_{d}\rho\big)\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}_{b}{}^{d}\lambda{}_{i}\\
&-\frac{21}{256}\widehat F{}^{d}{}^{e}\big(\mathcal D^{f}\rho\big)\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}^{c}\lambda{}_{i} +\frac{9}{256}\widehat F{}^{d}{}^{e}\big(\mathcal D^{f}\rho\big)\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{a}\lambda{}_{i}\\
&-\frac{11}{256}\widehat F{}^{d}{}^{e}\big(\mathcal D^{f}\rho\big)\epsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}_{b}\lambda{}_{i} +\frac{17}{256}\widehat F{}^{e}{}^{f}\big(\mathcal D^{a}\rho\big)\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{d}\lambda{}_{i}\\
&-\frac{5}{128}\widehat F{}^{a}{}^{e}\big(\mathcal D^{f}\rho\big)\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{d}\lambda{}_{i} +\frac{51}{128}\widehat F{}_{b}{}^{e}\big(\mathcal D^{f}\rho\big)\epsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{d}\lambda{}_{i}\\
&+\frac{17}{128}\widehat F{}^{e}{}^{f}\big(\mathcal D_{e}\rho\big)\epsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{f}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{d}\lambda{}_{i} +\frac{i}{8}\widehat F{}^{d}{}^{e}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\lambda{}^{i}}\gamma{}^{b}{}^{c}\big(\mathcal D^{f}\mathcal D^{a}\lambda{}_{i}\big)\\
&+\frac{1}{4}\widehat F{}^{a}{}^{c}\overline{\lambda{}^{i}}\gamma{}^{b}\big(\mathcal D_{b}\mathcal D_{c}\lambda{}_{i}\big) -\frac{i}{16}\widehat F{}^{d}{}^{e}\epsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\lambda{}^{i}}\gamma{}^{b}{}^{c}\big(\mathcal D^{f}\mathcal D_{b}\lambda{}_{i}\big)\\
&+\frac{i}{16}\widehat F{}^{c}{}^{d}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\lambda{}^{i}}\gamma{}^{a}{}^{b}\big(\mathcal D^{e}\mathcal D^{f}\lambda{}_{i}\big) -\frac{1}{4}\widehat F{}^{b}{}^{c}\overline{\big(\mathcal D_{b}\lambda{}^{i}\big)}\gamma{}^{a}\big(\mathcal D_{c}\lambda{}_{i}\big)\\
&-\frac{3i}{4}\big(\mathcal D_{c}\rho\big)\overline{\big(\mathcal D^{a}\lambda{}^{i}\big)}\gamma{}^{b}{}^{c}\big(\mathcal D_{b}\lambda{}_{i}\big) -\frac{i}{64}\big(\mathcal D^{a}\widehat F{}^{d}{}^{e}\big)\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\lambda{}^{i}}\gamma{}^{b}{}^{c}\big(\mathcal D^{f}\lambda{}_{i}\big)\\
&+\frac{5i}{32}\big(\mathcal D^{d}\widehat F{}_{d}{}^{e}\big)\epsilon{}^{a}{}_{b}{}_{c}{}_{e}{}_{f}\overline{\lambda{}^{i}}\gamma{}^{b}{}^{c}\big(\mathcal D^{f}\lambda{}_{i}\big) +\frac{i}{64}\big(\mathcal D^{d}\widehat F{}^{e}{}^{f}\big)\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\lambda{}^{i}}\gamma{}^{b}{}^{c}\big(\mathcal D^{a}\lambda{}_{i}\big)\\
&+\frac{i}{32}\big(\mathcal D^{d}\widehat F{}^{e}{}^{f}\big)\epsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{f}\overline{\lambda{}^{i}}\gamma{}^{b}{}^{c}\big(\mathcal D_{e}\lambda{}_{i}\big) -\frac{i}{256}\widehat F{}_{d}{}^{f}\widehat F{}_{e}{}^{g}\epsilon{}^{a}{}_{b}{}_{c}{}_{f}{}_{g}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{d}{}^{e}\lambda{}_{i}\\
&-\frac{i}{128}\widehat F{}^{a}{}^{f}\widehat F{}_{d}{}^{g}\epsilon{}_{b}{}_{c}{}_{e}{}_{f}{}_{g}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{d}{}^{e}\lambda{}_{i} -\frac{i}{256}\widehat F{}_{d}{}^{f}\widehat F{}_{f}{}^{g}\epsilon{}^{a}{}_{b}{}_{c}{}_{e}{}_{g}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{d}{}^{e}\lambda{}_{i}\\
&+\frac{1}{128}\widehat F{}_{d}{}^{e}\big(\mathcal D^{f}\rho\big)\epsilon{}^{a}{}_{b}{}_{c}{}_{e}{}_{f}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{d}\lambda{}_{i} +\frac{1}{4}\widehat F{}_{b}{}^{c}\overline{\lambda{}^{i}}\gamma{}^{b}\big(\mathcal D_{c}\mathcal D^{a}\lambda{}_{i}\big)\\
&-\frac{i}{8}\widehat F{}^{d}{}^{e}\epsilon{}^{a}{}_{b}{}_{c}{}_{e}{}_{f}\overline{\lambda{}^{i}}\gamma{}^{b}{}^{c}\big(\mathcal D_{d}\mathcal D^{f}\lambda{}_{i}\big) +\frac{1}{4}\widehat F{}^{a}{}^{c}\overline{\lambda{}^{i}}\gamma{}^{b}\big(\mathcal D_{c}\mathcal D_{b}\lambda{}_{i}\big)\\
&+\frac{3i}{32}\widehat F{}^{d}{}^{e}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\lambda{}^{i}}\gamma{}^{b}{}^{c}\big(\mathcal D^{a}\mathcal D^{f}\lambda{}_{i}\big) -\frac{3i}{16}\widehat F{}^{d}{}^{e}\epsilon{}^{a}{}_{b}{}_{c}{}_{e}{}_{f}\overline{\lambda{}^{i}}\gamma{}^{b}{}^{c}\big(\mathcal D^{f}\mathcal D_{d}\lambda{}_{i}\big)\\
&+\frac{i}{16}\widehat F{}^{a}{}^{d}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\lambda{}^{i}}\gamma{}^{b}{}^{c}\big(\mathcal D^{e}\mathcal D^{f}\lambda{}_{i}\big) -\frac{1}{6}Y{}^{i}{}^{j}\overline{\lambda{}_{i}}\gamma{}^{b}\big(\mathcal D^{a}\mathcal D_{b}\lambda{}_{j}\big)\\
&-\frac{1}{3}Y{}^{i}{}^{j}\overline{\lambda{}_{i}}\gamma{}^{b}\big(\mathcal D_{b}\mathcal D^{a}\lambda{}_{j}\big) -\frac{i}{2}\big(\mathcal D_{c}\rho\big)\overline{\lambda{}^{i}}\gamma{}^{b}{}^{c}\big(\mathcal D_{b}\mathcal D^{a}\lambda{}_{i}\big)\\
&-\frac{i}{4}\big(\mathcal D_{c}\rho\big)\overline{\lambda{}^{i}}\gamma{}^{a}{}^{b}\big(\mathcal D_{b}\mathcal D^{c}\lambda{}_{i}\big) -\frac{i}{4}\big(\mathcal D_{c}\rho\big)\overline{\lambda{}^{i}}\gamma{}^{b}{}^{c}\big(\mathcal D^{a}\mathcal D_{b}\lambda{}_{i}\big)\\
&+\frac{51}{64}\big(\mathcal D_{b}\rho\big)\big(\mathcal D_{c}\rho\big)\overline{R(Q){}^{a}{}^{b}{}^{i}}\gamma{}^{c}\lambda{}_{i} -\frac{9i}{256}\big(\mathcal D^{a}\rho\big)\big(\mathcal D^{f}\rho\big)\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{d}{}^{e}\lambda{}_{i}
\end{aligned}
\tag{CTF-E3F2-7}
```

```math
\begin{aligned}
&+\frac{1}{8}\big(\mathcal D^{a}\rho\big)\big(\mathcal D_{c}\rho\big)\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}_{b}\lambda{}_{i} +\frac{i}{128}\big(\mathcal D_{b}\rho\big)\big(\mathcal D^{f}\rho\big)\epsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{d}{}^{e}\lambda{}_{i}\\
&-\frac{1}{6}\big(\mathcal D^{a}\mathcal D^{b}Y{}^{i}{}^{j}\big)\overline{\lambda{}_{i}}\gamma{}_{b}\lambda{}_{j} +\frac{11}{4}\widehat F{}^{c}{}^{d}T{}^{e}{}^{f}\epsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\lambda{}^{i}}\gamma{}^{b}\big(\mathcal D_{b}\lambda{}_{i}\big)\\
&+\frac{i}{4}\big(\mathcal D_{b}\rho\big)\overline{\big(\mathcal D^{c}\lambda{}^{i}\big)}\gamma{}^{a}{}^{b}\big(\mathcal D_{c}\lambda{}_{i}\big) -8\big(\mathcal D^{a}\rho\big)\big(\mathcal D_{b}\rho\big)\overline{\chi{}^{i}}\gamma{}^{b}\lambda{}_{i}\\
&-\frac{1}{3}\big(\mathcal D^{b}\mathcal D^{a}Y{}^{i}{}^{j}\big)\overline{\lambda{}_{i}}\gamma{}_{b}\lambda{}_{j} +\frac{i}{32}\big(\mathcal D_{d}\rho\big)\big(\mathcal D^{f}\rho\big)\epsilon{}^{a}{}_{b}{}_{c}{}_{e}{}_{f}\overline{R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{d}{}^{e}\lambda{}_{i}
\end{aligned}
\tag{CTF-E3F2-8}
```

#### Constrained vector: $`n=4`$, explicit degree $`0`$

```math
\begin{aligned}
\mathcal E_{4}^{(0)a}={}&\frac{3}{8}\widehat F{}^{b}{}^{c}\widehat F{}^{d}{}^{e}\big(\mathcal D^{f}\rho\big)\big(\mathcal D_{f}\rho\big)\epsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{e} +\frac{3}{2}\widehat F{}^{a}{}^{b}\big(\mathcal D_{b}\rho\big)\big(\mathcal D^{c}\rho\big)\big(\mathcal D_{c}\rho\big)\\
&+3\widehat F{}^{a}{}^{b}\big(\mathcal D_{b}\rho\big)Y^2 +\frac{3}{4}\widehat F{}^{a}{}^{b}\big(\mathcal D_{b}\rho\big)\widehat F^2\\
&+3\widehat F{}^{a}{}^{b}\widehat F{}_{b}{}^{c}\widehat F{}_{c}{}^{d}\big(\mathcal D_{d}\rho\big) -\frac{3}{8}\widehat F{}^{b}{}^{c}\widehat F{}^{d}{}^{e}\big(\mathcal D^{a}\rho\big)\big(\mathcal D^{f}\rho\big)\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\\
&+\frac{3}{16}\widehat F{}^{a}{}^{b}\widehat F{}_{b}{}^{c}\widehat F{}^{d}{}^{e}\widehat F{}^{f}{}^{g}\epsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g}
\end{aligned}
\tag{CTF-E4F0}
```

#### Constrained vector: $`n=4`$, explicit degree $`2`$

```math
\begin{aligned}
\mathcal E_{4}^{(2)a}={}&-\frac{3}{4}Y{}^{i}{}^{j}\big(\Box^c \rho\big)\overline{\lambda{}_{i}}\gamma{}^{a}\lambda{}_{j} -\frac{9}{4}\big(\mathcal D^{b}Y{}^{i}{}^{j}\big)\big(\mathcal D_{b}\rho\big)\overline{\lambda{}_{i}}\gamma{}^{a}\lambda{}_{j}\\
&+\frac{3i}{16}\widehat F^2\overline{\lambda{}^{i}}\gamma{}^{a}{}^{b}\big(\mathcal D_{b}\lambda{}_{i}\big) +\frac{13i}{32}T{}^{d}{}^{e}\epsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{e}\widehat F^2\overline{\lambda{}^{i}}\gamma{}^{b}{}^{c}\lambda{}_{i}\\
&-\frac{3}{4}Y{}^{i}{}^{j}\widehat F{}^{c}{}^{d}\epsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\lambda{}_{i}}\gamma{}^{b}\big(\mathcal D^{e}\lambda{}_{j}\big) -\frac{3i}{2}Y{}^{i}{}^{j}\widehat F{}^{a}{}^{b}\overline{\lambda{}_{i}}\big(\mathcal D_{b}\lambda{}_{j}\big)\\
&+\frac{3i}{4}Y^2\overline{\lambda{}^{i}}\gamma{}^{a}{}^{b}\big(\mathcal D_{b}\lambda{}_{i}\big) +\frac{i}{4}Y^2\overline{\lambda{}^{i}}\big(\mathcal D^{a}\lambda{}_{i}\big)\\
&+\frac{5i}{8}T{}^{d}{}^{e}\epsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{e}Y^2\overline{\lambda{}^{i}}\gamma{}^{b}{}^{c}\lambda{}_{i} -\frac{i}{2}Y{}^{i}{}^{j}Y{}_{i}{}^{k}\overline{\lambda{}_{j}}\big(\mathcal D^{a}\lambda{}_{k}\big)\\
&-\frac{5i}{4}Y{}^{i}{}^{j}Y{}_{i}{}^{k}T{}^{d}{}^{e}\epsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\lambda{}_{j}}\gamma{}^{b}{}^{c}\lambda{}_{k} +\frac{15i}{8}\big(\mathcal D^{c}\rho\big)\big(\mathcal D_{c}\rho\big)\overline{\lambda{}^{i}}\gamma{}^{a}{}^{b}\big(\mathcal D_{b}\lambda{}_{i}\big)\\
&+\frac{3i}{4}\big(\mathcal D^{b}\rho\big)\big(\mathcal D_{b}\rho\big)\overline{\lambda{}^{i}}\big(\mathcal D^{a}\lambda{}_{i}\big) +\frac{3i}{4}\big(\mathcal D^{d}\rho\big)\big(\mathcal D_{d}\rho\big)T{}^{e}{}^{f}\epsilon{}^{a}{}_{b}{}_{c}{}_{e}{}_{f}\overline{\lambda{}^{i}}\gamma{}^{b}{}^{c}\lambda{}_{i}\\
&-3Y{}^{i}{}^{j}\big(\mathcal D_{b}\rho\big)\overline{\lambda{}_{i}}\gamma{}^{a}\big(\mathcal D^{b}\lambda{}_{j}\big) -9Y{}^{i}{}^{j}\big(\mathcal D^{c}\rho\big)T{}^{d}{}^{e}\epsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\lambda{}_{i}}\gamma{}^{b}\lambda{}_{j}\\
&-6iY{}^{i}{}^{j}\big(\mathcal D^{b}\rho\big)T{}^{a}{}_{b}\overline{\lambda{}_{i}}\lambda{}_{j} +\frac{3i}{8}\widehat F{}^{a}{}^{d}\widehat F{}_{b}{}_{c}\overline{\lambda{}^{i}}\gamma{}^{b}{}^{c}\big(\mathcal D_{d}\lambda{}_{i}\big)\\
&+\frac{3i}{4}\widehat F{}_{b}{}^{c}\widehat F{}_{c}{}^{d}\overline{\lambda{}^{i}}\gamma{}^{a}{}^{b}\big(\mathcal D_{d}\lambda{}_{i}\big) +\frac{3i}{4}\widehat F{}^{a}{}_{b}\widehat F{}_{c}{}^{d}\overline{\lambda{}^{i}}\gamma{}^{b}{}^{c}\big(\mathcal D_{d}\lambda{}_{i}\big)\\
&-\frac{3}{4}\widehat F{}^{a}{}^{c}\big(\mathcal D_{c}\rho\big)\overline{\lambda{}^{i}}\gamma{}^{b}\big(\mathcal D_{b}\lambda{}_{i}\big) -\frac{3}{4}\widehat F{}^{a}{}_{b}\big(\mathcal D_{c}\rho\big)\overline{\lambda{}^{i}}\gamma{}^{b}\big(\mathcal D^{c}\lambda{}_{i}\big)\\
&-\frac{3}{4}\widehat F{}_{b}{}^{c}\big(\mathcal D_{c}\rho\big)\overline{\lambda{}^{i}}\gamma{}^{b}\big(\mathcal D^{a}\lambda{}_{i}\big) -\frac{3i}{32}\widehat F{}^{d}{}^{e}\big(\mathcal D_{b}\rho\big)\epsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\lambda{}^{i}}\gamma{}^{b}{}^{c}\big(\mathcal D^{f}\lambda{}_{i}\big)\\
&+\frac{3i}{32}\widehat F{}^{c}{}^{d}\big(\mathcal D^{f}\rho\big)\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\lambda{}^{i}}\gamma{}^{a}{}^{b}\big(\mathcal D^{e}\lambda{}_{i}\big) +\frac{3i}{8}\widehat F{}^{b}{}^{c}\big(\mathcal D^{e}\rho\big)\epsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\lambda{}^{i}}\big(\mathcal D^{d}\lambda{}_{i}\big)\\
&-\frac{3i}{16}\widehat F{}^{d}{}^{e}\big(\mathcal D^{a}\rho\big)\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\lambda{}^{i}}\gamma{}^{b}{}^{c}\big(\mathcal D^{f}\lambda{}_{i}\big) -\frac{3i}{8}\widehat F{}_{b}{}^{d}\big(\mathcal D_{c}\widehat F{}^{a}{}_{d}\big)\overline{\lambda{}^{i}}\gamma{}^{b}{}^{c}\lambda{}_{i}\\
&+\frac{3i}{16}\widehat F{}_{b}{}_{c}\big(\mathcal D^{d}\widehat F{}^{a}{}_{d}\big)\overline{\lambda{}^{i}}\gamma{}^{b}{}^{c}\lambda{}_{i} +\frac{3i}{8}\widehat F{}_{b}{}^{c}\big(\mathcal D^{d}\widehat F{}_{c}{}_{d}\big)\overline{\lambda{}^{i}}\gamma{}^{a}{}^{b}\lambda{}_{i}\\
&+\frac{3i}{8}\widehat F{}^{a}{}_{b}\big(\mathcal D^{d}\widehat F{}_{c}{}_{d}\big)\overline{\lambda{}^{i}}\gamma{}^{b}{}^{c}\lambda{}_{i} -3i\widehat F{}_{b}{}^{d}\big(\mathcal D_{c}\rho\big)T{}^{a}{}_{d}\overline{\lambda{}^{i}}\gamma{}^{b}{}^{c}\lambda{}_{i}\\
&+\frac{9i}{2}\widehat F{}_{b}{}_{c}\big(\mathcal D^{d}\rho\big)T{}^{a}{}_{d}\overline{\lambda{}^{i}}\gamma{}^{b}{}^{c}\lambda{}_{i} +\frac{9i}{2}\widehat F{}^{c}{}^{d}\big(\mathcal D_{b}\rho\big)T{}_{c}{}_{d}\overline{\lambda{}^{i}}\gamma{}^{a}{}^{b}\lambda{}_{i}\\
&+3i\widehat F{}_{b}{}^{c}\big(\mathcal D^{d}\rho\big)T{}_{c}{}_{d}\overline{\lambda{}^{i}}\gamma{}^{a}{}^{b}\lambda{}_{i} +9i\widehat F{}^{a}{}^{d}\big(\mathcal D_{b}\rho\big)T{}_{c}{}_{d}\overline{\lambda{}^{i}}\gamma{}^{b}{}^{c}\lambda{}_{i}
\end{aligned}
\tag{CTF-E4F2-1}
```

```math
\begin{aligned}
&+9i\widehat F{}^{a}{}_{b}\big(\mathcal D^{d}\rho\big)T{}_{c}{}_{d}\overline{\lambda{}^{i}}\gamma{}^{b}{}^{c}\lambda{}_{i} +\frac{3}{8}\big(\mathcal D^{b}Y{}^{i}{}^{j}\big)\widehat F{}^{d}{}^{e}\epsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\lambda{}_{i}}\gamma{}^{c}\lambda{}_{j}\\
&+\frac{3i}{32}\widehat F{}^{d}{}^{e}\big(\mathcal D^{f}\mathcal D_{b}\rho\big)\epsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\lambda{}^{i}}\gamma{}^{b}{}^{c}\lambda{}_{i} -\frac{3i}{32}\widehat F{}^{c}{}^{d}\big(\mathcal D^{e}\mathcal D^{f}\rho\big)\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\lambda{}^{i}}\gamma{}^{a}{}^{b}\lambda{}_{i}\\
&-\frac{3i}{32}\widehat F{}^{d}{}^{e}\big(\mathcal D^{f}\mathcal D^{a}\rho\big)\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\lambda{}^{i}}\gamma{}^{b}{}^{c}\lambda{}_{i} +\frac{23i}{16}\widehat F{}^{a}{}_{b}\widehat F{}^{d}{}^{e}T{}^{f}{}^{g}\epsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g}\overline{\lambda{}^{i}}\gamma{}^{b}{}^{c}\lambda{}_{i}\\
&-\frac{21i}{32}\widehat F{}^{d}{}^{e}\widehat F{}^{f}{}^{g}T{}^{a}{}_{b}\epsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g}\overline{\lambda{}^{i}}\gamma{}^{b}{}^{c}\lambda{}_{i} +\frac{3i}{32}\widehat F{}^{c}{}^{d}\widehat F{}^{e}{}^{f}T{}_{b}{}^{g}\epsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g}\overline{\lambda{}^{i}}\gamma{}^{a}{}^{b}\lambda{}_{i}\\
&-\frac{9i}{32}\widehat F{}^{d}{}^{e}\widehat F{}^{f}{}^{g}T{}_{b}{}_{c}\epsilon{}^{a}{}_{d}{}_{e}{}_{f}{}_{g}\overline{\lambda{}^{i}}\gamma{}^{b}{}^{c}\lambda{}_{i} +\frac{35i}{32}\widehat F{}^{d}{}^{e}\widehat F{}^{f}{}^{g}T{}_{d}{}_{e}\epsilon{}^{a}{}_{b}{}_{c}{}_{f}{}_{g}\overline{\lambda{}^{i}}\gamma{}^{b}{}^{c}\lambda{}_{i}\\
&-\frac{13i}{32}\widehat F{}_{b}{}_{c}\widehat F{}^{d}{}^{e}T{}^{f}{}^{g}\epsilon{}^{a}{}_{d}{}_{e}{}_{f}{}_{g}\overline{\lambda{}^{i}}\gamma{}^{b}{}^{c}\lambda{}_{i} -9i\widehat F{}_{b}{}^{d}\big(\mathcal D_{d}\rho\big)T{}^{a}{}_{c}\overline{\lambda{}^{i}}\gamma{}^{b}{}^{c}\lambda{}_{i}\\
&+\frac{15i}{2}\widehat F{}^{a}{}^{d}\big(\mathcal D_{d}\rho\big)T{}_{b}{}_{c}\overline{\lambda{}^{i}}\gamma{}^{b}{}^{c}\lambda{}_{i} +\frac{3i}{4}\widehat F{}^{d}{}^{e}\big(\mathcal D^{f}\rho\big)\epsilon{}^{a}{}_{b}{}_{c}{}_{e}{}_{f}\overline{\lambda{}^{i}}\gamma{}^{b}{}^{c}\big(\mathcal D_{d}\lambda{}_{i}\big)\\
&-\frac{3}{4}\widehat F{}^{a}{}^{c}\big(\mathcal D_{b}\rho\big)\overline{\lambda{}^{i}}\gamma{}^{b}\big(\mathcal D_{c}\lambda{}_{i}\big) -\frac{3}{4}\widehat F{}^{b}{}^{c}\big(\mathcal D_{c}\rho\big)\overline{\lambda{}^{i}}\gamma{}^{a}\big(\mathcal D_{b}\lambda{}_{i}\big)\\
&-\frac{3i}{8}\widehat F{}_{b}{}^{d}\big(\mathcal D_{d}\widehat F{}^{a}{}_{c}\big)\overline{\lambda{}^{i}}\gamma{}^{b}{}^{c}\lambda{}_{i} -9i\widehat F{}^{c}{}^{d}\big(\mathcal D_{c}\rho\big)T{}_{b}{}_{d}\overline{\lambda{}^{i}}\gamma{}^{a}{}^{b}\lambda{}_{i}\\
&-\frac{3i}{4}\big(\mathcal D^{b}Y{}^{i}{}^{j}\big)\widehat F{}^{a}{}_{b}\overline{\lambda{}_{i}}\lambda{}_{j} +\frac{3i}{8}\widehat F{}^{a}{}^{d}\widehat F{}^{e}{}^{f}T{}_{e}{}^{g}\epsilon{}_{b}{}_{c}{}_{d}{}_{f}{}_{g}\overline{\lambda{}^{i}}\gamma{}^{b}{}^{c}\lambda{}_{i}\\
&-\frac{15i}{8}\widehat F{}^{d}{}^{e}\widehat F{}_{d}{}^{f}T{}_{e}{}^{g}\epsilon{}^{a}{}_{b}{}_{c}{}_{f}{}_{g}\overline{\lambda{}^{i}}\gamma{}^{b}{}^{c}\lambda{}_{i} -\frac{9i}{8}\widehat F{}^{d}{}^{e}\widehat F{}^{f}{}^{g}T{}_{d}{}_{f}\epsilon{}^{a}{}_{b}{}_{c}{}_{e}{}_{g}\overline{\lambda{}^{i}}\gamma{}^{b}{}^{c}\lambda{}_{i}\\
&+\frac{35i}{16}\widehat F{}^{a}{}^{d}\widehat F{}^{e}{}^{f}T{}_{d}{}^{g}\epsilon{}_{b}{}_{c}{}_{e}{}_{f}{}_{g}\overline{\lambda{}^{i}}\gamma{}^{b}{}^{c}\lambda{}_{i} -\frac{3i}{16}\big(\mathcal D^{d}\widehat F{}_{d}{}^{e}\big)\big(\mathcal D^{f}\rho\big)\epsilon{}^{a}{}_{b}{}_{c}{}_{e}{}_{f}\overline{\lambda{}^{i}}\gamma{}^{b}{}^{c}\lambda{}_{i}\\
&-\frac{3i}{4}Y{}^{i}{}^{j}\big(\mathcal D^{b}\widehat F{}^{a}{}_{b}\big)\overline{\lambda{}_{i}}\lambda{}_{j} -\frac{3i}{4}Y{}^{i}{}^{j}\big(\mathcal D^{e}\rho\big)\epsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\lambda{}_{i}}\gamma{}^{b}{}^{c}\big(\mathcal D^{d}\lambda{}_{j}\big)\\
&+\frac{3}{2}Y{}^{i}{}^{j}\big(\mathcal D_{b}\rho\big)\overline{\lambda{}_{i}}\gamma{}^{b}\big(\mathcal D^{a}\lambda{}_{j}\big) +\frac{3}{2}Y{}^{i}{}^{j}\big(\mathcal D^{a}\rho\big)\overline{\lambda{}_{i}}\gamma{}^{b}\big(\mathcal D_{b}\lambda{}_{j}\big)\\
&+iY{}^{i}{}^{j}\big(\mathcal D^{b}Y{}_{i}{}^{k}\big)\overline{\lambda{}_{j}}\gamma{}^{a}{}_{b}\lambda{}_{k} +\frac{3}{4}Y{}^{i}{}^{j}\big(\mathcal D_{b}\mathcal D^{a}\rho\big)\overline{\lambda{}_{i}}\gamma{}^{b}\lambda{}_{j}\\
&+\frac{i}{4}Y{}^{i}{}^{j}\big(\mathcal D^{b}Y{}_{i}{}_{j}\big)\overline{\lambda{}^{k}}\gamma{}^{a}{}_{b}\lambda{}_{k} +\frac{3}{4}\big(\mathcal D^{b}Y{}^{i}{}^{j}\big)\big(\mathcal D^{a}\rho\big)\overline{\lambda{}_{i}}\gamma{}_{b}\lambda{}_{j}\\
&+\frac{3}{2}\big(\mathcal D^{a}Y{}^{i}{}^{j}\big)\big(\mathcal D_{b}\rho\big)\overline{\lambda{}_{i}}\gamma{}^{b}\lambda{}_{j} +\frac{9i}{64}\widehat F{}^{d}{}^{e}\big(\Box^c \rho\big)\epsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\lambda{}^{i}}\gamma{}^{b}{}^{c}\lambda{}_{i}\\
&+\frac{3i}{8}\big(\mathcal D_{b}\rho\big)\big(\Box^c \rho\big)\overline{\lambda{}^{i}}\gamma{}^{a}{}^{b}\lambda{}_{i} +\frac{45i}{64}\widehat F{}^{d}{}^{e}\big(\mathcal D_{f}\rho\big)\epsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\lambda{}^{i}}\gamma{}^{b}{}^{c}\big(\mathcal D^{f}\lambda{}_{i}\big)
\end{aligned}
\tag{CTF-E4F2-2}
```

```math
\begin{aligned}
&+\frac{3i}{4}\big(\mathcal D_{b}\rho\big)\big(\mathcal D_{c}\rho\big)\overline{\lambda{}^{i}}\gamma{}^{a}{}^{b}\big(\mathcal D^{c}\lambda{}_{i}\big) -\frac{3i}{4}\big(\mathcal D^{a}\rho\big)\big(\mathcal D_{b}\rho\big)\overline{\lambda{}^{i}}\big(\mathcal D^{b}\lambda{}_{i}\big)\\
&+\frac{3i}{16}\big(\mathcal D^{d}\widehat F{}^{e}{}^{f}\big)\big(\mathcal D_{d}\rho\big)\epsilon{}^{a}{}_{b}{}_{c}{}_{e}{}_{f}\overline{\lambda{}^{i}}\gamma{}^{b}{}^{c}\lambda{}_{i} +\frac{3i}{4}\big(\mathcal D^{c}\rho\big)\big(\mathcal D_{c}\mathcal D_{b}\rho\big)\overline{\lambda{}^{i}}\gamma{}^{a}{}^{b}\lambda{}_{i}\\
&-3i\big(\mathcal D^{d}\rho\big)\big(\mathcal D^{e}\rho\big)T{}_{d}{}^{f}\epsilon{}^{a}{}_{b}{}_{c}{}_{e}{}_{f}\overline{\lambda{}^{i}}\gamma{}^{b}{}^{c}\lambda{}_{i} -\frac{3i}{32}\widehat F{}^{d}{}^{e}\big(\mathcal D_{d}\rho\big)\epsilon{}^{a}{}_{b}{}_{c}{}_{e}{}_{f}\overline{\lambda{}^{i}}\gamma{}^{b}{}^{c}\big(\mathcal D^{f}\lambda{}_{i}\big)\\
&-\frac{33i}{64}\widehat F{}^{d}{}^{e}\big(\mathcal D^{f}\rho\big)\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\lambda{}^{i}}\gamma{}^{b}{}^{c}\big(\mathcal D^{a}\lambda{}_{i}\big) +\frac{3i}{32}\widehat F{}^{a}{}^{d}\big(\mathcal D^{f}\rho\big)\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\lambda{}^{i}}\gamma{}^{b}{}^{c}\big(\mathcal D^{e}\lambda{}_{i}\big)\\
&-\frac{3i}{16}\big(\mathcal D^{d}\widehat F{}^{a}{}^{e}\big)\big(\mathcal D^{f}\rho\big)\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\lambda{}^{i}}\gamma{}^{b}{}^{c}\lambda{}_{i} -\frac{3i}{8}\big(\mathcal D_{b}\rho\big)\big(\mathcal D_{c}\mathcal D^{a}\rho\big)\overline{\lambda{}^{i}}\gamma{}^{b}{}^{c}\lambda{}_{i}\\
&-\frac{3i}{4}\big(\mathcal D^{a}\rho\big)\big(\mathcal D^{d}\rho\big)T{}^{e}{}^{f}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\lambda{}^{i}}\gamma{}^{b}{}^{c}\lambda{}_{i} +\frac{3i}{2}\big(\mathcal D^{a}\rho\big)\big(\mathcal D_{c}\rho\big)\overline{\lambda{}^{i}}\gamma{}^{b}{}^{c}\big(\mathcal D_{b}\lambda{}_{i}\big)\\
&+\frac{9i}{4}\widehat F{}^{a}{}^{d}\widehat F{}_{d}{}^{e}T{}^{f}{}^{g}\epsilon{}_{b}{}_{c}{}_{e}{}_{f}{}_{g}\overline{\lambda{}^{i}}\gamma{}^{b}{}^{c}\lambda{}_{i} -\frac{3i}{4}\widehat F{}^{a}{}^{d}\widehat F{}_{b}{}_{d}\overline{\lambda{}^{i}}\gamma{}^{b}{}^{c}\big(\mathcal D_{c}\lambda{}_{i}\big)\\
&-\frac{i}{4}\widehat F{}_{b}{}^{d}\widehat F{}^{e}{}^{f}T{}_{d}{}^{g}\epsilon{}^{a}{}_{c}{}_{e}{}_{f}{}_{g}\overline{\lambda{}^{i}}\gamma{}^{b}{}^{c}\lambda{}_{i} -\frac{3i}{64}\widehat F{}^{d}{}^{e}\big(\mathcal D^{a}\mathcal D^{f}\rho\big)\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\lambda{}^{i}}\gamma{}^{b}{}^{c}\lambda{}_{i}\\
&-\frac{3i}{32}\widehat F{}^{a}{}^{d}\big(\mathcal D^{e}\mathcal D^{f}\rho\big)\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\lambda{}^{i}}\gamma{}^{b}{}^{c}\lambda{}_{i} +\frac{3i}{32}\widehat F{}^{d}{}^{e}\big(\mathcal D^{f}\mathcal D_{d}\rho\big)\epsilon{}^{a}{}_{b}{}_{c}{}_{e}{}_{f}\overline{\lambda{}^{i}}\gamma{}^{b}{}^{c}\lambda{}_{i}
\end{aligned}
\tag{CTF-E4F2-3}
```

#### Constrained vector: $`n=5`$, explicit degree $`2`$

```math
\begin{aligned}
\mathcal E_{5}^{(2)a}={}&\frac{3}{2}Y{}^{i}{}^{j}Y^2\overline{\lambda{}_{i}}\gamma{}^{a}\lambda{}_{j} +3Y{}^{i}{}^{j}\big(\mathcal D^{b}\rho\big)\big(\mathcal D_{b}\rho\big)\overline{\lambda{}_{i}}\gamma{}^{a}\lambda{}_{j}\\
&-\frac{3i}{8}\widehat F{}^{d}{}^{e}\big(\mathcal D^{f}\rho\big)\big(\mathcal D_{f}\rho\big)\epsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\lambda{}^{i}}\gamma{}^{b}{}^{c}\lambda{}_{i} -\frac{3i}{4}\big(\mathcal D_{b}\rho\big)\big(\mathcal D^{c}\rho\big)\big(\mathcal D_{c}\rho\big)\overline{\lambda{}^{i}}\gamma{}^{a}{}^{b}\lambda{}_{i}\\
&-3Y{}^{i}{}^{j}\big(\mathcal D^{a}\rho\big)\big(\mathcal D_{b}\rho\big)\overline{\lambda{}_{i}}\gamma{}^{b}\lambda{}_{j} +\frac{3}{2}Y{}^{i}{}^{j}\widehat F{}^{c}{}^{d}\big(\mathcal D^{e}\rho\big)\epsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\lambda{}_{i}}\gamma{}^{b}\lambda{}_{j}\\
&+3iY{}^{i}{}^{j}\widehat F{}^{a}{}^{b}\big(\mathcal D_{b}\rho\big)\overline{\lambda{}_{i}}\lambda{}_{j} -\frac{3i}{4}Y{}^{i}{}^{j}Y{}_{i}{}^{k}\big(\mathcal D_{b}\rho\big)\overline{\lambda{}_{j}}\gamma{}^{a}{}^{b}\lambda{}_{k}\\
&-\frac{9i}{8}\big(\mathcal D_{b}\rho\big)Y^2\overline{\lambda{}^{i}}\gamma{}^{a}{}^{b}\lambda{}_{i} -\frac{3i}{4}\widehat F{}^{a}{}^{d}\widehat F{}_{b}{}_{c}\big(\mathcal D_{d}\rho\big)\overline{\lambda{}^{i}}\gamma{}^{b}{}^{c}\lambda{}_{i}\\
&-\frac{3i}{2}\widehat F{}_{b}{}^{c}\widehat F{}_{c}{}^{d}\big(\mathcal D_{d}\rho\big)\overline{\lambda{}^{i}}\gamma{}^{a}{}^{b}\lambda{}_{i} -\frac{3i}{2}\widehat F{}^{a}{}_{b}\widehat F{}_{c}{}^{d}\big(\mathcal D_{d}\rho\big)\overline{\lambda{}^{i}}\gamma{}^{b}{}^{c}\lambda{}_{i}\\
&-\frac{3i}{32}\widehat F{}^{d}{}^{e}\epsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{e}\widehat F^2\overline{\lambda{}^{i}}\gamma{}^{b}{}^{c}\lambda{}_{i} -\frac{3i}{8}\big(\mathcal D_{b}\rho\big)\widehat F^2\overline{\lambda{}^{i}}\gamma{}^{a}{}^{b}\lambda{}_{i}\\
&+\frac{3i}{64}\widehat F{}_{b}{}_{c}\widehat F{}^{d}{}^{e}\widehat F{}^{f}{}^{g}\epsilon{}^{a}{}_{d}{}_{e}{}_{f}{}_{g}\overline{\lambda{}^{i}}\gamma{}^{b}{}^{c}\lambda{}_{i} -\frac{3i}{32}\widehat F{}_{b}{}^{c}\widehat F{}^{d}{}^{e}\widehat F{}^{f}{}^{g}\epsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g}\overline{\lambda{}^{i}}\gamma{}^{a}{}^{b}\lambda{}_{i}\\
&-\frac{3i}{32}\widehat F{}^{a}{}_{b}\widehat F{}^{d}{}^{e}\widehat F{}^{f}{}^{g}\epsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g}\overline{\lambda{}^{i}}\gamma{}^{b}{}^{c}\lambda{}_{i} +\frac{3i}{8}Y{}^{i}{}^{j}Y{}_{i}{}^{k}\widehat F{}^{d}{}^{e}\epsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\lambda{}_{j}}\gamma{}^{b}{}^{c}\lambda{}_{k}\\
&-3Y{}^{i}{}^{j}Y{}_{i}{}^{k}Y{}_{j}{}^{l}\overline{\lambda{}_{k}}\gamma{}^{a}\lambda{}_{l} -\frac{3i}{16}\widehat F{}^{d}{}^{e}\epsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{e}Y^2\overline{\lambda{}^{i}}\gamma{}^{b}{}^{c}\lambda{}_{i}\\
&+\frac{3i}{2}\widehat F{}^{a}{}^{d}\widehat F{}_{b}{}_{d}\big(\mathcal D_{c}\rho\big)\overline{\lambda{}^{i}}\gamma{}^{b}{}^{c}\lambda{}_{i} +\frac{3i}{8}\widehat F{}^{d}{}^{e}\big(\mathcal D^{a}\rho\big)\big(\mathcal D^{f}\rho\big)\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\lambda{}^{i}}\gamma{}^{b}{}^{c}\lambda{}_{i}\\
&-\frac{3i}{8}\widehat F{}^{a}{}^{d}\widehat F{}_{d}{}^{e}\widehat F{}^{f}{}^{g}\epsilon{}_{b}{}_{c}{}_{e}{}_{f}{}_{g}\overline{\lambda{}^{i}}\gamma{}^{b}{}^{c}\lambda{}_{i} +\frac{3i}{16}\widehat F{}^{d}{}^{e}\widehat F{}_{d}{}^{f}\widehat F{}_{e}{}^{g}\epsilon{}^{a}{}_{b}{}_{c}{}_{f}{}_{g}\overline{\lambda{}^{i}}\gamma{}^{b}{}^{c}\lambda{}_{i}
\end{aligned}
\tag{CTF-E5F2}
```

