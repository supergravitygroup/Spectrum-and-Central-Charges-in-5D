# LOG component verification

**Result: PASS for the current off-shell construction through two physical fermions.** The complete primary is checked at all its fermion orders. The displayed action retains the even components through degree two and the spinor through degree one, with implicit fermions kept inside full supercovariant quantities. The certificate covers the stated supercovariant component version through two physical fermions. Higher-fermion action terms are outside its scope.

## Contents

1. Scope and conventions
2. Source algebra and normalization
3. Certification evidence
4. Conservation and supersymmetry scope
5. Bosonic comparison and limits
6. Certified action and files
7. Reproducibility and exclusions

## 1. Scope and conventions

The [master conventions](CONVENTIONS.md) and [LOG ledger](LOG_CONVENTIONS.md) apply: five dimensions, metric $`(-,+,+,+,+)`$, $`\gamma^{01234}=i`$, project Riemann sign, linear Majorana bar, NW–SE SU(2) contractions, graded left spinor differentiation and unit-weight symmetrization. The defining scalar is on a positive patch. The curvature-squared coupling has engineering dimension $`-2`$ and multiplies the G25-normalized invariant directly.

The gauge is $`\sigma=1`$, $`b_\mu=0`$, $`\psi^i=0`$, $`L_c^{ij}=\delta^{ij}L/\sqrt2`$. Here $`\psi^i`$ is the defining dilatino; the gravitino and independent compensator spinor remain. No auxiliary equation of motion, dualization, background ansatz or EFT expansion is imposed.

All active derivatives remain the full $`\mathcal D_a`$ and $`\Box^c=\mathcal D^a\mathcal D_a`$, including Q/S/K connections. Differentiate before gauge evaluation. The gauge-fixed derivative dictionary stays in the same file as a reference, without substitution into component displays. No symmetry of the full fermionic $`f_{ab}`$ or primed Ricci tensor is assumed.

## 2. Source algebra and normalization

**Source algebra.** The source-local SDD super-Jacobi identity requires the two K-generator coefficients in C24 (A.1l) to be $`+i/8,-i/4`$, where the source prints $`+1/8,-1/4`$. All 122,880 independent component equations pass with these phases. The earlier conformal-superspace source provides independent support; its different $`WS`$ coefficient is not imported. This is a project-derived repair, not an author-confirmed erratum. Literal source images and text remain unchanged. See [the curved derivation](../../../../../../references/source_evidence/log/derivations/curved.md), (CC-03)–(CC-11).

The canonical unfixed triplet, spinor, scalar and vector contain **59/278/514/1332** terms. The gauged components contain **13/94/141/373** terms, with ordered differentiation performed before gauge evaluation.

**Current-interface explanation.** Lowering the second spinor index gives $`-MC`$, not $`MC`$. Literal C24 (2.50) therefore differs from the required vector by $`2Q_1`$. The operational current $`P=E+Q_1+Q_2`$ and active BF coefficients remain unchanged. The complete superform pullback derives the project potential coefficients $`(1,-3)`$ and ordinary-current BF coupling. See [the FORM derivation](../../../../../../references/source_evidence/log/derivations/form-interface.md).

The H3.9 coefficient $`+i/4`$ passes the defining-projector test, while its literal opposite produces 40 nonzero coefficients.

## 3. Certification evidence

| Claim | Verification and result | Evidence |
|---|---|---|
| Defining S23 (3.24) equals the stored primary | Independent six-spinor reconstruction at degrees 0,2,4,6; 21,408 exhaustive coefficients vanish; negative control fails | [Projector derivation](../../../../../../references/source_evidence/log/derivations/defining-projector.md), [certificate](../../../../../../references/source_evidence/log/results/gauged_full_fermionic_log/sources/certification_20260925/defining_projector/certification.json) |
| Actual curved linearity | All possible degrees through seven; 603,104 final coefficients vanish | [Full primary certificate](../../../../../../references/source_evidence/log/results/gauged_full_fermionic_log/sources/certification_20260925/curved/full-primary-certificate.json) |
| Actual S/K primarity | S through degree five, both independent SU(2) projections; K through degree four and identically on the undifferentiated sextic sector | [Curved derivation](../../../../../../references/source_evidence/log/derivations/curved.md) |
| Once-only component projection | Primitive maps, nonlinear Weyl terms, ordered derivatives and Q/S/K shifts checked; factors $`(-2,-2i,-1,+1)`$ applied once | [Projection certificate](../../../../../../references/source_evidence/log/derivations/projection.md) |
| Canonicalization, dimensions, indices and reality | Exact coefficient collection and fixed points; charge-conjugation identities for all 32 Clifford blades; zero phase defects in unfixed and gauged outputs | [Reality evidence](../../../../../../references/source_evidence/log/results/gauged_full_fermionic_log/sources/certification_20260925/canonical/reality_phase_after_correction.json), [structural checks](../../../../../../references/source_evidence/log/results/gauged_full_fermionic_log/sources/canonical_two_fermi/final_structure_checks.json) |
| Complete independent array comparison | All 179,396 printed Step 6 contributions evaluated against tensor/canonical expressions; zero residual at the completed sample | [Finite evaluation](../../../../../../references/source_evidence/log/results/gauged_full_fermionic_log/sources/certification_20260925/canonical/all_terms_seed_926255_rho_1_printed.json) |
| Gauged composites and target gauge | Ordered full derivatives and conventional constraints retained; corrected-input rebuild equals all four active slots exactly | [Rebuild evidence](../../../../../../references/source_evidence/log/results/gauged_full_fermionic_log/sources/step7/supercovariant/derivative_debug_rebuild.json) |
| Current, potential and BF density | Full superform pullbacks and seven source-density coefficients; theorem applied to the verified actual multiplet | [FORM derivation](../../../../../../references/source_evidence/log/derivations/form-interface.md) |
| Complete bosonic action | Every flux, derivative and compensator term reproduces LOG-CORR05 with an explicit boundary current | [Bosonic derivation](../../../../../../references/source_evidence/log/derivations/bosonic.md), [complete equations](sources/certification_20260925/bosonic/EXACT_BOSONIC_COMPARISON.md) |

The exhaustive primary/projector checks use denominator-cleared Gaussian-integer tensors and bounds on the actual contraction/summation paths: their zeros are exact, without a tolerance. The separate whole-polynomial array evaluation is a finite numerical check, not an unrestricted identity proof. Another sample stopped by a conservative arithmetic-bound guard is recorded as stopped and is not counted as a PASS.

## 4. Conservation and supersymmetry scope

The verified actual primary satisfies

```math
H^{ij}=H^{ji},\qquad \mathbb D H^{ij}=3H^{ij},\qquad S_{\alpha i}H^{jk}=K_aH^{ij}=0,\qquad \nabla_\alpha^{(i}H^{jk)}=0.
\tag{CERT-01}
```

S23 (2.20)–(2.24), with descendants (3.26), therefore supplies the full linear-multiplet transformation and integrability identities. This application is justified by the actual complete primary, including higher fermion orders that feed retained descendants. Separate reconstruction/projection certificates link the stored components to these definitions.

The closed four-form identity gives $`\nabla_a\mathcal H^a=iW_{ab}{}^\alpha{}_i(\Sigma^{ab})_\alpha{}^\beta\varphi_\beta^i=0`$ in the traceless frame, using the full $`R(Q)`$ gamma trace. The bridge and pullback give

```math
\mathcal D_aE_{\log}^a=0,\qquad \partial_\mu(eP_{\log}^{\mu})=0.
\tag{CERT-02}
```

These hold for the full underlying multiplet and order by order in the truncated display. This is a superform/integrability proof with verified polynomial premises, not a separate brute-force expansion of every canonical vector term's divergence. Full $`R(P)`$, $`R(Q)`$ and $`R(M)`$ constraints remain in the algebra and dependent connections.

The BF proof uses $`J=V\wedge\Phi-\Sigma_G`$, $`d\Sigma_G=F\wedge\Phi`$, $`d\Phi=0`$, hence $`dJ=0`$. This proves the density theorem for the verified multiplet. Transport through the locked gauged realization and compensating gauge transformations gives the retained action; it is not a separately expanded calculation of every gauge-preserving transformation commutator.

For the displayed action $`S^{(0)}+S^{(2)}`$, cancellation of its supersymmetry variation is supported through one physical fermion, up to boundary terms. Degree-three variations require the omitted quartic action. The truncated display is not asserted invariant at unrestricted fermion order.

## 5. Bosonic comparison and limits

The independent reduction of the calculated components gives

```math
\ell_{\rm BF}^{(0)}=\ell_{\rm LOG\text{-}CORR05}+\nabla_b\big(C_aQ^{ab}+J^b\big).
\tag{CERT-03}
```


All terms of $`Q,J`$ and 149 weighted pointwise relations are in the [bosonic companion](sources/certification_20260925/bosonic/EXACT_BOSONIC_COMPARISON.md). Integrated equality requires the displayed boundary integral to vanish. No integration by parts establishes local multiplet equality. The comparison confirms the corrected scalar $`w^2D`$ sector and Standard-Weyl curvature coefficient, without fitting to uncorrected G25 (11).

The identities retain symbolic $`g`$ without division by $`g`$, so setting $`g=0`$ preserves them and the ungauged BF limit. Previously recorded flat-superspace descent checks and independent $`W^2Y`$ reconstruction remain valid. Engineering dimensions and free indices are checked for each collected output. No vacuum or spectrum follows from this certificate.

## 6. Certified action and files

The [active calculation](../../../construction.md) contains the composite substitutions, gauge-fixed derivative reference, dependent connections, all four canonical components in §§6.1–6.4 and BF density in §6.5:

```math
\boxed{P_{\log}^a=\left[E_{\log}^a+\frac i2\bar\psi_b\gamma^{ba}\varphi_{\log}+\frac14\bar\psi_b^i\gamma^{abc}\psi_c^jL_{\log ij}\right]_{\le2}+\text{high fermi terms}.}
\tag{CERT-04}
```

```math
\boxed{e^{-1}\mathcal L_{\log}=\left[N_{\log}-\frac g2L_c^{ij}L_{\log ij}+C_aP_{\log}^a+\frac12\bar\psi_a\gamma^a\varphi_{\log}+\frac i4\bar\psi_a^i\gamma^{ab}\psi_b^jL_{\log ij}\right]_{\le2}+\text{high fermi terms}.}
\tag{CERT-05}
```

The defining vector is $`(1,C_\mu,0,-gL_c^{ij}/2)`$; the composite linear leg is $`(L_{\log}^{ij},\varphi_{\log}^i,N_{\log},E_{\log}^a)`$. The independent compensator is the $`c`$ multiplet; no compensator condition is imposed on $`L_{\log}^{ij}`$.

The corrected unfixed input is [LOG_MULTIPLET_CANONICAL_TWO_FERMI.md](LOG_MULTIPLET_CANONICAL_TWO_FERMI.md). Steps 4–6 use the source algebra and normalization stated above.

## 7. Reproducibility and exclusions


The [action lock](../../../spectrum_input.md) and [evidence manifest](../../../../../../references/source_evidence/manifest.json) identify the retained documents and certificates by SHA-256. The linked derivations contain reproducible checks and located equation references. The certificate records the stated propagation checks; temporary descent caches are not part of the distributed evidence.


The certificate concerns the retained two-fermion action and its stated defining and component identities. Higher-fermion interactions, all-order gauge-algebra closure, and spacetime-specific boundary spectra lie outside its scope.
