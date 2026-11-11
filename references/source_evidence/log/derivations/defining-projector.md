# Direct defining-projector certification

The equations and reported residuals below belong to the cited construction. Finite component tests and formal symbolic identities retain their distinct scopes; the former do not establish an unrestricted symbolic identity.


Inputs are Step2 (S2-01), (S2-14), (S2-28)–(S2-31), corrected full [log_step4_covariant_rules.py](../../../../computations/log_fermionic/src/kernels/log_step4_covariant_rules.py), and the stored 58-term primary for comparison only. Use the Gold source frame until the common component projection; no gauge, field equations, flat specialization or integration by parts. Source spinor derivative order remains explicit.

The exact polarized operator identity is $`H^{++}=(i/256)(\nabla^{++})^2\nabla^{--}\log W`$, with seed $`-4iW^{-1}X^{--}+W^{-2}\lambda^{\alpha-}\lambda_\alpha^-`$. The factors are $`(-3i/40)(5/3)(-1/32)=i/256`$. Four derivatives are applied from the right. Each contracted pair is $`\varepsilon^{\alpha\beta}\nabla_\beta^+\nabla_\alpha^+`$. No target coefficient enters the derivative chain.

After the successive derivatives the maximal allowed fermion degrees are 5,4,3,2; higher terms cannot reach final degree2 because one spinor derivative lowers degree by at most1. In practice the first derivative has degree at most3. This retains the quartic intermediate terms which a two-fermion intermediate truncation would lose.

**Verdict:** the independently differentiated defining operator equals the project's corrected, stored 58-term primary in every possible fermion degree, $`0,2,4,6`$. This includes the quartic primary inputs required by the two-fermion scalar and vector descendants. Equality is local, with ordered covariant derivatives, off shell, without integration by parts or a spacetime/gauge specialization. It is not a comparison only to the literal published polynomial: the project's previously derived H3.9 sign correction is retained and independently detected by a negative control.

## 1. Exact scope and conventions

Use [Step 2](../../../../log/action/details/component_construction/results/gauged_full_fermionic_log/STEP_02_LOG_PRIMARY.md), the branch `GAUGED-LOG-CONVENTIONS-v1` and `GAUGED-LOG-STEP1-v1` locks. Lorentz indices run from 0 to 4, spinor indices from 1 to 4, and SU(2) indices from 1 to 2. The metric is mostly plus. The indexed Gold Clifford matrices, spinor metrics and all curvature signs are those of Step 2 (S2-02) and the full C24 Appendix A algebra; the fixed exact Clifford representation is used only to exhaust tensor coefficients, not to choose a physical background. Source SU(2) lowering is $`v_i=\varepsilon_{ij}v^j`$, with $`\varepsilon^{12}=\varepsilon_{21}=1`$. Ordered Grassmann products and derivatives acting from the left are retained.

The scalar obeys $`W>0`$, $`\mathbb DW=W`$ and $`S_\alpha^iW=K_aW=0`$. The logarithm obeys $`\mathbb D\log W=1`$, not zero. No independent auxiliary field is eliminated. Source-to-component projection is applied equally once on both sides by the existing exact field bridge; it is not a gauge fixing. No action coupling, Fourier transform, quantum normalization or boundary representative enters this local test.

## 2. Ordered calculation and degree control

The [retained certificate](../results/gauged_full_fermionic_log/sources/certification_20260925/defining_projector/certification.json) records the defining-projector comparison. The ordered calculation below begins with the two seed summands only; the stored target is used separately for comparison, not while differentiating.

Write $`D_\alpha=\nabla_\alpha^+`$ and $`U=\nabla^{--}\log W`$. Then the actual ordered word is

```math
H^{++}=\frac{i}{256}\varepsilon^{\alpha\beta}\varepsilon^{\gamma\delta}D_\beta D_\alpha D_\delta D_\gamma\left(-4iW^{-1}X^{--}+W^{-2}\lambda^{\tau-}\lambda_\tau^-\right).
```

The derivative stages therefore add $`D_\gamma,D_\delta,D_\alpha,D_\beta`$, in that order. Every product differentiation uses $`D(AB)=(DA)B+(-1)^{|A|}A(DB)`$. Every mixed spinor/vector derivative uses the corrected full covariant rules, including torsion and Lorentz, SU(2), S and K generators. The four outer spinor derivative slots remain abstract until their contractions have been performed.

| Stage | Raw monomials | Retained before geometric expansion | Collected source monomials |
|---|---:|---:|---:|
| First outer derivative | 16 | 16 | 12 |
| Second outer derivative | 134 | 134 | 122 |
| Third outer derivative, endpoint degree two | 1,654 | 1,653 | 1,955 |
| Fourth outer derivative, endpoint degree two | 33,495 | 32,729 | 29,946 |

The seed has Weyl weight one; stage $`n`$ has weight $`1+n/2`$. All stages pass exact index, parity and weight checks, and the endpoint has weight three. The increased third-stage count comes from explicit geometric expansion, not additional input terms.

For degree four, the untruncated second stage is reused. Its next derivative contains **one quintic monomial**, which the degree-two route properly omits but the quartic route must restore. The third stage then supplies 273 cubic monomials and this quintic monomial. Their final derivative gives 786 raw quartic terms, collected to 749 source terms. Thus no intermediate degree-five contribution is lost.

For degree six, only the $`W^{-2}\lambda^-\lambda^-`$ seed can contribute, and each of the four derivatives must hit the inverse scalar power. A derivative of a gaugino produces bosonic fields and cannot reach maximal degree six. The successive factors are $`(-2i)(-3i)(-4i)(-5i)=120`$. The sextic calculation reconstructs this path with the same graded derivative rule, without inserting a stored sextic coefficient.

## 3. Exact equality checks and the curved quadratic cancellation

All free and dummy SU(2) components are treated explicitly. The $`++`$ target component is evaluated for unrestricted values of every physical field component; Lorentz/spinor contractions and all identical-fermion antisymmetrizations are then exhausted. This proves an identity of covariant symmetric SU(2) tensors, rather than an identity on a chosen field configuration. The independent $`--`$ collection gives the corresponding same intermediate residual count as well.

The comparison sign is always **direct defining projector minus stored corrected primary**.

| Sector | Remaining algebraic structures before final identities | Exhaustive coefficient groups | Coefficients checked | Result |
|---|---:|---:|---:|---|
| Bosonic | 0 | — | Exact symbolic collection | PASS |
| Two fermions | 20 before the commutator, 19 afterward | 10 | 7,840 | All zero |
| Four fermions | 24 | 7 | 9,472 | All zero |
| Six fermions | 2 | 1 | 4,096 | All zero |

The sole second derivative in the quadratic residual is

```math
\frac{i}{4}W^{-2}(\gamma^{ab})^{\alpha\beta}\lambda_\alpha^+\mathcal D_a\mathcal D_b\lambda_\beta^+=\frac{i}{8}W^{-2}(\gamma^{ab})^{\alpha\beta}\lambda_\alpha^+[\mathcal D_a,\mathcal D_b]\lambda_\beta^+.
```

The quadratic reduction first proves that the coefficient tensor is antisymmetric in the two derivative slots. Only then does it substitute half the complete C24 (A.4) vector commutator, using [vector_commutator.py](../results/gauged_full_fermionic_log/sources/certification_20260925/curved/vector_commutator.py). It retains the torsion, Lorentz, SU(2) and S-curvature actions. There is no substitution $`[\mathcal D_a,\mathcal D_b]=0`$.

The resulting Lorentz-curvature term contracts three or more curvature indices into the epsilon tensor and vanishes by the **full** C24 (A.4c) cyclic identity. That identity is proved on all 35 independent symmetric rank-four spinor basis tensors by [curvature_algebraic_bianchi.py](../results/gauged_full_fermionic_log/sources/certification_20260925/curved/curvature_algebraic_bianchi.py); it is not an assumed bosonic Ricci symmetry. The remaining 19 monomials contain $`R(Q)`$, its derivative, and fermion bilinears. They cancel after the full gamma-traceless $`R(Q)`$ projector and Grassmann antisymmetrization. No extra differential condition on $`R(Q)`$ is imposed.

The retained $`R(Q)`$ space is represented by the complete image of 24 times its gamma-traceless projector acting on the 40-component unconstrained two-form-spinor basis. Covariant derivatives preserve this algebraic projector. All output coefficients are exhausted; there is no numerical field sampling or fitting of target coefficients.

Rational denominators are cleared first. Every contraction, coefficient multiplication, group sum and identical-field permutation sum is checked to remain a Gaussian integer whose conservative internal bound is below $`2^{53}`$. The largest contraction bound is 7,200,000, far below that threshold. Hence the complex binary64 storage performs exact integer arithmetic in these checks; zero is not tolerance-based. The retained certificate summarizes the recorded sector comparisons; the bound above states the arithmetic used in those comparisons.

As a sensitivity check, restoring the literal S23 (3.25) sign of H3.9 leaves 40 nonzero component coefficients. More precisely, direct minus literal is twice the corrected H3.9 term, with coefficient $`+i/2`$ in front of $`W^{-3}(\Gamma^a)^{\alpha\beta}\lambda_\alpha^{(i}\nabla_aX^{j)k}\lambda_{\beta k}`$. The literal source is preserved. This independently supports the existing $`-i/4\to+i/4`$ correction instead of silently treating the printed polynomial as the defining answer.

## 4. Why this closes the defining-operator gate

The same-plus anticommutator vanishes in the **full** C24 (A.2) algebra: every coefficient has a factor $`\varepsilon^{ij}`$. Four spinor values imply $`D_{[\alpha_1}\cdots D_{\alpha_5]}=0`$. Consequently, for the reconstructed operator and an arbitrary isotwistor,

```math
D_\eta H^{++}=0\quad\Longrightarrow\quad\nabla_\eta^{(i}H^{jk)}=0.
```

This formal proof now applies to the actual full polynomial because its equality to the defining operator has been checked in **all** degrees. In particular, the result does not infer defining-operator equality merely from some separately checked linearity or primarity conditions.

Primarity including the inhomogeneous logarithm is established in the primary formalism source, Butter et al., arXiv:1410.8682v2, §14.3 (14.26)–(14.27), using §7.1 (7.6)–(7.9). See the source [§7.1](https://arxiv.org/abs/1410.8682v2) and [§14.3](https://arxiv.org/abs/1410.8682v2). S23 §3.6, directly below (3.24) and (3.25), independently identifies this construction as a primary linear multiplet. The exact extension to the logarithm is as follows.

Let $`U=\nabla^{(-2)}\log W`$, with the auxiliary-isotwistor notation of that source. Although $`\mathbb D\log W=1`$, its two-spinor derivative is homogeneous:

```math
\mathbb DU=[\mathbb D,\nabla^{(-2)}]\log W+\nabla^{(-2)}1=U,\qquad J^{(0)}U=U,\qquad M_{\alpha\beta}U=0.
```

Equation (7.7) gives $`[S_\alpha^{(-1)},\nabla^{(-2)}]\log W=6(J^{(-2)}\nabla_\alpha^{(-1)}+\nabla_\alpha^{(-1)}J^{(-2)})\log W=0`$: the logarithm is an SU(2) singlet and $`[J^{(-2)},\nabla_\alpha^{(-1)}]=0`$. For the outer projector, (5.30b) and (7.9) reduce its S-variation to three plus derivatives acting on $`(8-2\mathbb D-6J^{(0)})U`$. The coefficient is $`8-2-6=0`$. Thus $`S^{(-1)}H^{(2)}=0`$ with no discarded logarithmic shift. Auxiliary-isotwistor independence gives $`S^{(1)}H^{(2)}=0`$ as in (7.9). The superconformal $`\{S,S\}`$ algebra then gives $`K_aH^{ij}=0`$.

Likewise, for the full six-spinor operator $`\mathcal O^{ij}`$, $`\mathbb D H^{ij}=3H^{ij}+\mathcal O^{ij}1=3H^{ij}`$. Reality follows from the same real linear-multiplet projector on the real scalar $`\log W`$; no complex branch of the logarithm is used. These source-level conclusions supplement the independent component identities supplied by the curved certification, rather than replacing their evidence.

## 5. Certification-helper issue and reproducibility

The metric-chain reduction collapses those constant open metric chains by exact finite matrix multiplication before dummy-index canonicalization. No physical field or covariant derivative rule is altered. The source comparison uses the metric-chain reduction before canonicalization.

The recorded orchestration check covers 1,360 open-chain cases of lengths one through four in dimensions two and four, including all index variances and edge reversals. It also compares the streamed seed derivative and geometric expansion to the original production routines. All pass.

The [retained certificate](../results/gauged_full_fermionic_log/sources/certification_20260925/defining_projector/certification.json) contains the reported sector results, negative control and provenance hashes. The complete projector replay scripts and intermediate pickle caches are not distributed here; the [component evidence guide](../../README.md) distinguishes these recorded results from the runnable checks supplied in the repository.

**Boundary of this certificate:** it proves the full corrected primary equals its defining operator, and therefore supports the source primary/linear-multiplet identities. It does not by itself certify every descendant translation, the gauged composite substitutions, the BF current normalization, the final action coefficient map, or a spectrum. Those comparisons have separate source records.
