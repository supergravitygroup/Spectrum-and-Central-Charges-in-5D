---
concept: Relative normalization of the gauged fermionic Gauss–Bonnet action
date: 2026-09-28
mode: project-context
project_context: GB-FERMION-SPECTRUM-CONVENTIONS-v1
citation_status: source equations and versions identified in the Literature Guide below
status: normalization of the inherited Weyl map and stated coefficient comparisons
---

# Relative normalization of the gauged fermionic Gauss–Bonnet action

## Executive Summary

The inherited Özkan–Pang-normalized Weyl density must be multiplied by **−2**, while the inherited LOG density keeps its existing normalization. This follows from comparing the complete Weyl primary, including its two fermion bilinears, and then applying the already established generic linear-multiplet bridge. It therefore multiplies every descendant and every BF slot, including the ordinary-current completion. The intended combination is $`\ell_{\mathrm{GB}}=-2\ell_{\mathrm{W,OP}}-4\ell_{\log}`$. The normalization argument uses the specified Weyl map as input. The specified action scope is complete through two physical fermions, with all full supercovariant definitions retained until the final fermion-degree projection.

## Why This Matters Here

Matching the coefficient of $`C_{abcd}C^{abcd}`$ alone would miss relative errors in $`\bar R(Q)R(Q)`$, $`\bar\chi\chi`$, the linear-multiplet spinor, and the two gravitino terms in the ordinary conserved current. These terms contribute to the fermionic Hessian. A common primary and a common BF density fix the multiplier of all of them before choosing a background.

This note gives the source conversion associated with SOURCE_LOCK.md and used in the action construction.

## Prerequisites and Dependencies

The operational component frame is the [anchored convention ledger](../../references/CONVENTIONS.md), and its explicit fields and derivatives are in [COMPONENT_CONVENTIONS.md](../../references/COMPONENT_CONVENTIONS.md). The input Weyl multiplet is [FM01–FM04](../../../../../computations/weyl_fermionic/inputs/reference/notes/04_full_fermionic_weyl_linear_map.md); its action is [GA24](../../../../../weyl2/action/details/construction.md). The generic bridge and repaired ordinary-current BF interface are [LOG-S1-02–16](../../../../../log/action/details/component_construction/results/gauged_full_fermionic_log/LOG_CONVENTIONS.md). The desired bosonic normalization is [GB-WEYLOG-DEF-v1](../../inputs/action_sources/09_gauss_bonnet_from_weyl_log_action_lock.md).

Three different operations must be kept distinct: convert Gold's fields into the common component frame; convert a Gold linear multiplet into the component linear-multiplet normalization; insert that multiplet in the common BF density. The factor −2 arises in the second operation for this particular Weyl primary. It is not a new universal prefactor of the BF density.

## Core Explanation

### Problem and Target

We seek the normalization of the gauged Weyl invariant relative to the already normalized LOG invariant. No equation of motion, vacuum ansatz, auxiliary elimination, dualization, or field redefinition is permitted. We first work before gauge fixing. The identities then survive the common source gauge because they are identities of the same component fields and full derivatives. Terms through two physical fermions are needed for the action; the elementary primary comparison below is exact as a polynomial in its full covariants.

### Convention Ledger

<!-- ASSERT_CONVENTION: natural_units=true, metric_signature=(-,+,+,+,+), source_lock=GB-FERMION-SPECTRUM-CONVENTIONS-v1, fourier_convention=not_used, renormalization_scheme=not_applicable_classical -->

Use five-dimensional mostly-plus signature, $`a,b=0,\ldots,4`$, $`i,j=1,2`$, unit-weight brackets, $`\epsilon^{01234}=1`$, $`\{\gamma^a,\gamma^b\}=2\eta^{ab}`$, and $`\gamma^{01234}=i`$. Spinors are Grassmann odd. The Majorana bar is linear: $`\overline{i\zeta}=i\bar\zeta`$. There is no hidden conjugation of $`i`$ in the following bilinears. The common derivative includes Q, S and K connections. The curvature tensor in a full covariant derivative commutator is the full $`R(M)`$, not an independently substituted Levi–Civita Riemann tensor.

The superspace spinor metric can be represented as $`\varepsilon^{\alpha\beta}=-\mathsf C^{\alpha\beta}`$ and $`\varepsilon_{\alpha\beta}=\mathsf C_{\alpha\beta}`$ with $`\mathsf C^2=-1`$. A source scalar contraction $`u^\alpha v_\alpha`$ is then $`\bar u v`$ for the lower-index spinor columns. This is the calibrated indexed convention of the LOG current audit, not an additional spinor convention.

### Definitions and Required Identities

Gold's C24 primary, equation (4.3a), is

```math
h_W^{ij}=-\frac i2 W^{\alpha\beta\gamma(i}W_{\alpha\beta\gamma}{}^{j)}-w^{ab}\Phi_{ab}{}^{ij}+\frac{256i}{3}\chi^{\alpha(i}\chi_\alpha{}^{j)}.
\tag{GN01}
```

Here $`W_{\alpha\beta\gamma}`$ is the symmetric spinor descendant of the super-Weyl tensor, $`w_{ab}=W_{ab}|`$, and $`\Phi_{ab}^{ij}=R_G(J)_{ab}^{ij}`$. These are not the defining vector scalar $`W`$ or its triplet. C24 footnote 4, PDF p.9, gives the spinor/two-form conversion. C24 (A.4a), PDF p.83, gives the spinor torsion; (2.17), PDF p.13, identifies its projection with the component Q-curvature:

```math
W_{ab\,\gamma}^{i}=(\Sigma_{ab})^{\alpha\beta}W_{\alpha\beta\gamma}^{i},\qquad W_{\alpha\beta\gamma}^{i}=\frac12(\Sigma^{ab})_{\alpha\beta}W_{ab\,\gamma}^{i},\qquad R_G(Q)_{ab}^{i}=-\frac i2W_{ab}^{i}.
\tag{GN02}
```

C24 Appendix C, Table 4, and the common bridge give

```math
w_{ab}=\frac{16}{3}T_{ab},\quad \Phi_{ab}^{ij}=-\widehat R_{ab}^{ij}(V),\quad \chi_G^i=\chi^i,\quad R_G(Q)_{ab}^{i}=\frac12\widehat R_{ab}^{i}(Q),\quad R_G(M)_{ab}{}^{cd}=-\widehat C_{ab}{}^{cd}.
\tag{GN03}
```

The last equality uses the traceless conformal frame and the branch's definition $`\widehat C=\widehat R(M)`$. The field-dependent S and K shifts in Tables 4–5 belong to this conversion. Their cancellation in the full vector derivative is part of the bridge; identifying individual unshifted connections would give a different calculation.

## Formal Structure / Equations

### Detailed Derivation

#### Step 1. Convert the complete primary, including fermions

<!-- ASSERT_CONVENTION: metric_signature=(-,+,+,+,+), source_lock=GB-FERMION-SPECTRUM-CONVENTIONS-v1 -->

The symmetric-pair completeness identity associated with GN02 is

```math
\frac12(\Sigma_{ab})^{\alpha\beta}(\Sigma^{ab})_{\rho\sigma}=\delta_{(\rho}^{\alpha}\delta_{\sigma)}^{\beta}.
\tag{GN04}
```

Insert the inverse conversion for both symmetric spinor pairs, contract GN04, and retain the original order of the two odd spinors. This yields the factor $`1/2`$:

```math
W^{\alpha\beta\gamma(i}W_{\alpha\beta\gamma}{}^{j)}=\frac12\overline{W_{ab}^{(i}}W^{j)ab}.
\tag{GN05}
```

From the two expressions for $`R_G(Q)`$ in GN02–GN03, $`-iW_{ab}=\widehat R_{ab}(Q)`$, hence $`W_{ab}=i\widehat R_{ab}(Q)`$. The bar does not conjugate this $`i`$. Therefore

```math
\frac12\overline{W_{ab}^{(i}}W^{j)ab}=\frac12i^2\overline{\widehat R_{ab}^{(i}(Q)}\widehat R^{j)ab}(Q)=-\frac12\overline{\widehat R_{ab}^{(i}(Q)}\widehat R^{j)ab}(Q).
\tag{GN06}
```

There has been no interchange of two Grassmann factors. The minus is $`i^2=-1`$. Insert GN03 and GN06 separately in the three terms of GN01:

```math
-\frac i2\left(-\frac12\overline{\widehat R^{(i}_{ab}(Q)}\widehat R^{j)ab}(Q)\right)=\frac i4\overline{\widehat R^{(i}_{ab}(Q)}\widehat R^{j)ab}(Q),\qquad -\frac{16}{3}T^{ab}\left(-\widehat R_{ab}^{ij}(V)\right)=\frac{16}{3}\widehat R_{ab}^{ij}(V)T^{ab}.
\tag{GN07}
```

The remaining scalar spinor contraction is $`\chi^{\alpha(i}\chi_\alpha{}^{j)}=\bar\chi^{(i}\chi^{j)}`$. Consequently the converted Gold primary is

```math
h_W^{ij}\big|_{G\to B}=\frac i4\overline{\widehat R^{(i}_{ab}(Q)}\widehat R^{j)ab}(Q)+\frac{256i}{3}\bar\chi^{(i}\chi^{j)}+\frac{16}{3}\widehat R_{ab}^{ij}(V)T^{ab}=L_{W,\mathrm{OP}}^{ij}.
\tag{GN08}
```

This is the full FM01 primary, not merely its bosonic term. Each term has conformal weight three: $`w(R(Q))=3/2`$, $`w(\chi)=3/2`$, $`w(R(V))=2`$ and $`w(T)=1`$.

#### Step 2. Distinguish primary equality from component normalization

<!-- ASSERT_CONVENTION: metric_signature=(-,+,+,+,+), source_lock=GB-FERMION-SPECTRUM-CONVENTIONS-v1 -->

The universal component bridge, LOG-S1-11, is

```math
h_G^{ij}=-\frac12L^{ij},\qquad \varphi_G^i=\frac i2\varphi^i,\qquad F_G=-N,\qquad \mathcal H_G^a=E^a.
\tag{GN09}
```

Apply its first equality to GN08: the component multiplet associated with the Gold Weyl primary starts with $`L_{W,\mathrm{target}}=-2L_{W,\mathrm{OP}}`$. The scalar-triplet law is linear, $`\delta L^{ij}=i\bar\epsilon^{(i}\varphi^{j)}`$. Keeping the supersymmetry parameters and the common derivative fixed gives

```math
\delta L_{W,\mathrm{target}}^{ij}=-2\delta L_{W,\mathrm{OP}}^{ij}=i\bar\epsilon^{(i}\big(-2\varphi_{W,\mathrm{OP}}^{j)}\big),\qquad \varphi_{W,\mathrm{target}}=-2\varphi_{W,\mathrm{OP}}.
\tag{GN10}
```

In the spinor law the scalar and vector singlets are $`N\epsilon^i/2`$ and $`-i\gamma^aE_a\epsilon^i/2`$. Multiplication of the complete spinor by −2 multiplies these two independent gamma projections by −2:

```math
\frac12N_{W,\mathrm{target}}\epsilon^i-\frac i2\gamma^aE_{W,\mathrm{target}\,a}\epsilon^i=-2\left(\frac12N_{W,\mathrm{OP}}\epsilon^i-\frac i2\gamma^aE_{W,\mathrm{OP}\,a}\epsilon^i\right),\qquad (N_{W,\mathrm{target}},E_{W,\mathrm{target}})=(-2N_{W,\mathrm{OP}},-2E_{W,\mathrm{OP}}).
\tag{GN11}
```

The source/projector construction is linear in its input primary. GN10–GN11 prove the propagation of the normalization for the inherited descendants. In particular, the FM02 coefficient $`8/3`$ remains the adopted Q(FM01) result. Multiplying it by −2 produces $`-16/3`$ in the target spinor; it does not replace it with the literal OP coefficient $`16/3`$ before multiplication.

#### Step 3. Carry the same multiplier through the current and every BF slot

<!-- ASSERT_CONVENTION: metric_signature=(-,+,+,+,+), source_lock=GB-FERMION-SPECTRUM-CONVENTIONS-v1 -->

The source-current completion is linear in the linear multiplet:

```math
P^a=E^a+\frac i2\bar\psi_b\gamma^{ba}\varphi+\frac14\bar\psi_b^i\gamma^{abc}\psi_c^jL_{ij},\qquad P_{W,\mathrm{target}}^a=-2E_{W,\mathrm{OP}}^a-i\bar\psi_b\gamma^{ba}\varphi_{W,\mathrm{OP}}-\frac12\bar\psi_b^i\gamma^{abc}\psi_c^jL_{W,\mathrm{OP}\,ij}=-2P_{W,\mathrm{OP}}^a.
\tag{GN12}
```

The defining vector $`(\rho,A,\lambda,Y)=(\sigma,C,\psi,Y)`$ is held fixed. Expanding the ordinary-current term gives nine insertions. Their coefficients transform as follows; the field/spinor order in each row stays fixed.

| Insertion | Component coefficient | Target coefficient |
|---|---:|---:|
| $`\sigma N_W`$ | $`1`$ | $`-2`$ |
| $`C_aE_W^a`$ | $`1`$ | $`-2`$ |
| $`\bar\psi\varphi_W`$ | $`i`$ | $`-2i`$ |
| $`\sigma\bar\psi_a\gamma^a\varphi_W`$ | $`1/2`$ | $`-1`$ |
| $`C_a\bar\psi_b\gamma^{ba}\varphi_W`$ | $`i/2`$ | $`-i`$ |
| $`Y^{ij}L_{W\,ij}`$ | $`1`$ | $`-2`$ |
| $`\bar\psi_a^i\gamma^a\psi^jL_{W\,ij}`$ | $`-1/2`$ | $`+1`$ |
| $`\sigma\bar\psi_a^i\gamma^{ab}\psi_b^jL_{W\,ij}`$ | $`i/4`$ | $`-i/2`$ |
| $`C_a\bar\psi_b^i\gamma^{abc}\psi_c^jL_{W\,ij}`$ | $`1/4`$ | $`-1/2`$ |

This follows by ordinary multiplication of each coefficient by −2. No integration by parts or spinor interchange is involved. Inserting $`Y^{ij}=i\bar\psi^{(i}\psi^{j)}/(4\sigma)-gL_c^{ij}/(2\sigma)`$ preserves the same multiplier for both parts. Thus the two new gauged couplings and all implicit gauging inside $`T,\chi,D`$ carry the same normalization.

Each BF row has conformal weight five; the current has weight four. The factor −2 is dimensionless. Gauge fixing does not change this arithmetic, but full differentiation must precede the gauge evaluation.

#### Step 4. Check the bosonic scalar and current independently

<!-- ASSERT_CONVENTION: metric_signature=(-,+,+,+,+), source_lock=GB-FERMION-SPECTRUM-CONVENTIONS-v1 -->

C24 (4.3c) supplies the bosonic scalar descendant. In the target BF density it appears as $`-\sigma F_W`$. Inserting $`w=16T/3`$, $`C_G=-C_B`$, $`\Phi=-R(V)`$ and $`\epsilon_G=-\epsilon_B`$ gives the following arithmetic before any gauge restriction:

| Structure in $`-F_W`$ | Converted coefficient | $`-2N_{W,\mathrm{OP}}`$ coefficient |
|---|---:|---:|
| $`C^2`$ | $`-1/4`$ | $`-1/4`$ |
| $`D^2`$ | $`-128/3`$ | $`-128/3`$ |
| $`DT^2`$ | $`-8(16/3)^2=-2048/9`$ | $`-2048/9`$ |
| $`R(V)^2`$ | $`+2/3`$ | $`+2/3`$ |
| $`(\mathcal D_aT_{bc})(\mathcal D^aT^{bc})`$ | $`+(3/2)(16/3)^2=128/3`$ | $`128/3`$ |
| $`(\mathcal D_bT_{ac})(\mathcal D^aT^{bc})`$ | $`-(3/2)(16/3)^2=-128/3`$ | $`-128/3`$ |
| $`T_{ab}T^{bc}T_{cd}T^{da}`$ | $`-(81/32)(16/3)^4=-2048`$ | $`-2048`$ |
| $`(T^2)^2`$ | $`+(33/128)(16/3)^4=5632/27`$ | $`5632/27`$ |
| $`\epsilon_{abcde}T^{ab}T^{cd}\mathcal D_fT^{ef}`$ | $`+(9/16)(16/3)^3=256/3`$ | $`256/3`$ |

The remaining $`CTT`$ coefficient is not comparable until the second derivative is ordered. Gold's converted pair is

```math
\frac{160}{3}C_{abcd}T^{ab}T^{cd}+\frac{256}{3}T_{ab}\mathcal D_c\mathcal D^aT^{cb}.
\tag{GN13}
```

FM04 instead uses $`T_{ab}\mathcal D^b\mathcal D_cT^{ac}=T_{ab}\mathcal D^a\mathcal D_cT^{cb}`$, obtained by exchanging the two dummy indices and using $`T_{ba}=-T_{ab}`$. For this bosonic check the full conformal commutator acts through the traceless Lorentz curvature on the primary $`T`$; its Q/S terms vanish with fermions and its K action on $`T`$ vanishes. Therefore

```math
T_{ab}[\mathcal D_c,\mathcal D^a]T^{cb}=T_{ab}\left(C_c{}^a{}^c{}_dT^{db}+C_c{}^a{}^b{}_dT^{cd}\right)=-C_{acbd}T^{ab}T^{cd}=-\frac12C_{abcd}T^{ab}T^{cd}.
\tag{GN14}
```

The first curvature term vanishes by the **specified trace** $`C_c{}^a{}^c{}_d=0`$. For the last equality contract the algebraic Bianchi identity $`C_{abcd}+C_{acdb}+C_{adbc}=0`$ with $`T^{ab}T^{cd}`$. The second term is $`-C_{acbd}T^{ab}T^{cd}`$ by antisymmetry in its last pair. Exchange $`c,d`$ in the third term; $`T^{dc}=-T^{cd}`$ supplies the same expression again. Hence $`C_{abcd}T^{ab}T^{cd}=2C_{acbd}T^{ab}T^{cd}`$.

Insert GN14 into GN13, without integration by parts:

```math
\frac{160}{3}CTT+\frac{256}{3}T_{ab}\mathcal D_c\mathcal D^aT^{cb}=\left(\frac{160}{3}-\frac{128}{3}\right)CTT+\frac{256}{3}T_{ab}\mathcal D^a\mathcal D_cT^{cb}=\frac{32}{3}CTT+\frac{256}{3}T_{ab}\mathcal D^b\mathcal D_cT^{ac}.
\tag{GN15}
```

Here $`CTT`$ is used only in this equality chain for the explicit contraction in GN13–14. This matches $`-2`$ times both FM04 terms. The **bosonic restriction** in GN14 is essential: at two fermions the Q/S curvature terms must also be retained. The primary/projector argument, not bosonic GN14, controls the full relative normalization.

C24 (4.3d–e) gives an independent current check. Its converted bosonic vector is

```math
\begin{aligned}
E_{W,\mathrm{target}}^a\big|_{\mathrm{bos}}={}&-\frac18\epsilon^{abcde}C_{bcfg}C_{de}{}^{fg}+\frac16\epsilon^{abcde}R(V)_{bc}^{ij}R(V)_{de\,ij} \\
&+\mathcal D_b\left[-8C^{ab}{}_{cd}T^{cd}+\frac{128}{3}DT^{ab}+\frac{256}{9}T^{ab}T_{cd}T^{cd}+\frac{1024}{3}T^a{}_cT^{cd}T^b{}_d\right] \\
&+64\epsilon^a{}_{bcde}\mathcal D^b\left[\frac23T^{cf}\mathcal D_fT^{de}+T^c{}_f\mathcal D^dT^{ef}\right]=-2E_{W,\mathrm{OP}}^a\big|_{\mathrm{bos}}.
\end{aligned}
\tag{GN16}
```

The coefficients in its divergence follow from $`8(16/3)=128/3`$, $`(3/2)(-1)(16/3)=-8`$, $`(3/16)(16/3)^3=256/9`$ and $`-(9/4)(16/3)^3=-1024/3`$. The last contraction in C24 is $`T^{ac}T_{cd}T^{db}=-T^a{}_cT^{cd}T^b{}_d`$, which supplies the displayed plus. The parity-odd coefficients are $`(9/4)(16/3)^2=64`$ and $`(3/2)(16/3)^2=128/3`$, with their sign reversed by $`\epsilon_G=-\epsilon_B`$. Every bosonic vector slot therefore has the same −2 factor.

#### Step 5. Check the curvature-only GB endpoint

On the curvature-only normalization probe, $`T=G=H=g=0`$ while the defining Dilaton-Weyl scalar still obeys $`D=-R/32`$. This is a probe, not a background solution or a global truncation. The normalized Weyl scalar is

```math
-\frac14C^2-\frac{128}{3}\left(-\frac R{32}\right)^2=-\frac14C^2-\frac1{24}R^2=-\frac14R_{abcd}R^{abcd}+\frac13R_{ab}R^{ab}-\frac1{12}R^2.
\tag{GN17}
```

The inherited LOG probe is $`-R_{ab}R^{ab}/6+R^2/24`$, with unit overall factor. Subtracting four times it gives

```math
\left(-\frac14R_{abcd}R^{abcd}+\frac13R_{ab}R^{ab}-\frac1{12}R^2\right)-4\left(-\frac16R_{ab}R^{ab}+\frac1{24}R^2\right)=-\frac14\left(R_{abcd}R^{abcd}-4R_{ab}R^{ab}+R^2\right).
\tag{GN18}
```

### Consistency Checks

GN04 was checked in the same exact Gaussian-rational gamma representation used by the LOG current audit. All 256 entries of its pair-completeness kernel passed. As additional nonzero checks, three symmetric-spinor-pair evaluations gave $`(W^{\alpha\beta\gamma}U_{\alpha\beta\gamma},\overline W_{ab}U^{ab})=(2855,5710),(4833,9666),(7725,15450)`$, so the ratio is $`1/2`$ in every case. These numerical values check the tensor-conversion kernel, not a physical field configuration, Fierz reduction of the full action, or supersymmetry certificate.

An exact rational five-dimensional Weyl-tensor test independently gave $`C_{abcd}T^{ab}T^{cd}=12712/3`$ and $`T_{ab}C_c{}^a{}^b{}_dT^{cd}=-6356/3`$, verifying the nonzero contraction in GN14. The five nontrivial rational coefficient conversions involving $`(16/3)^2`$, $`(16/3)^3`$, $`(16/3)^4`$ and the commutator shift also passed. All 19 display equations and 151 inline mathematical expressions rendered successfully with the local KaTeX engine.

The full primary equality GN08 includes all its bosonic and quadratic-fermion terms. The nine-slot table checks the BF relative coefficients explicitly. GN13–16 compare every bosonic scalar and vector structure before specializing the gauged realization. The multiplication also commutes with $`g\to0`$ since it is a constant and all fields use the same gauged realization. There are no integrations by parts in this normalization argument, so no boundary term has been discarded. The relative dimensions and weights are unchanged. GN17–18 give an independent curvature-only check, not the derivation of the factor.

The component traces defining FM03–04 are adopted inputs. The primary comparison and linearity of the descendant construction establish the common normalization factor; the BF-slot comparisons test its propagation into the density.

### Final Result

For the inherited Weyl map and the already normalized LOG action, the common-frame combination through two physical fermions is

```math
\boxed{\ell_{\mathrm{GB}}\big|_{\leq2\mathrm f}=\left[-2\ell_{\mathrm{W,OP}}^{\mathrm{map}}-4\ell_{\log}\right]_{\leq2\mathrm f},\qquad S=\frac1{2\kappa_5^2}\int d^5x\,e\left(\ell_{2\partial}+\lambda_{\mathrm{GB}}\ell_{\mathrm{GB}}\right)+O(\Psi^4).}
\tag{GN19}
```

The projection applies after all full covariant definitions and ordered differentiations, including the implicit fermions in hatted tensors and connections. With $`[\kappa_5^2]=-3`$, $`[\lambda_{\mathrm{GB}}]=-2`$, $`[\ell_{2\partial}]=2`$ and $`[\ell_{\mathrm{GB}}]=4`$, the action is dimensionless. The omitted degree-four-and-higher terms do not contribute to the fermionic Hessian around a bosonic background. This note fixes the combination; the expanded action is a separate deliverable in the same branch.

### Convention Dependence and Scope

The normalization factor is tied to the actual FM01 primary and the generic bridge GN09. The same −2 occurs in the two-derivative construction for a separate reason; that coincidence is not evidence for this conversion. LOG has already undergone its component projection and receives no further conversion factor. The assembly uses the adopted Weyl spinor coefficient $`8/3`$ and the stated two-derivative source slots and reality conventions.

## Project-Specific Connection

The branch may use $`-2`$ times GA24 in the common action and retain the current LOG coefficient $`-4`$. Its current completion must include both $`\bar\psi\gamma\varphi_W`$ and $`\bar\psi\gamma\psi L_W`$. The coefficient proof begins at GN08, so it applies to terms that vanish in the bosonic comparison and to all gauging dependence inside the composites. The main action document must state the inherited map status next to its retained-order endpoint. No vacuum, gauge for fluctuations, spectrum, or norm has been fixed by this calculation.

## Common Confusions and Failure Modes

- $`h_G|_{G\to B}=L_{W,\mathrm{OP}}`$ is an equality of polynomial contents. The component field representing that Gold primary is $`L_{W,\mathrm{target}}=-2h_G`$. Omitting the second statement loses the factor.
- A Dirac-style complex conjugation of $`i`$ in GN06 reverses the R(Q)-bilinear sign. The project bar is linear.
- The apparent $`160/3`$ versus $`32/3`$ coefficient mismatch is resolved by the explicit bosonic commutator GN14. The corresponding fermionic commutator may not be discarded in a quadratic-fermion reduction.
- $`P^a`$ is the ordinary conserved current; replacing it by its supercovariant part $`E^a`$ drops two BF insertions.
- An overall normalization proof does not replace the independent verification of the source composite multiplet. The adopted $`8/3`$ term stays visible.

## Literature Guide

### Foundational papers

- Mehmet Özkan and Yi Pang, *Supersymmetric Completion of Gauss-Bonnet Combination in Five Dimensions*, arXiv:1301.6622v4, 8 July 2013. See the [cited source](../../../../../references/bibliography.md#OzkanPangGB2013), (3.1) and (5.8), for the component BF normalization and original Weyl map. The adopted map's $`8/3`$ modification is a project-derived result, not attributed to that printed equation.

### Practical/working references

- Gregory Gold, Jessica Hutomo, Saurish Khandelwal and Gabriele Tartaglino-Mazzucchelli, *Components of curvature-squared invariants of minimal supergravity in five dimensions*. The equation locators refer to arXiv:2311.00679v1, 1 November 2023. See the [cited source](../../../../../references/bibliography.md#GoldEtAlComponents2023), footnote 4, (2.17), (4.1)–(4.6), (A.4a) and Appendix C Tables 4–6. These are the direct anchors for GN01–16.
- Gregory Gold, Jessica Hutomo, Saurish Khandelwal and Gabriele Tartaglino-Mazzucchelli, *On curvature-squared invariants of minimal five-dimensional supergravity from superspace*, arXiv:2302.14295v2, 16 March 2023. See the [cited source](../../../../../references/bibliography.md#GoldEtAlSuperspace2023), (3.24)–(3.27), for the LOG primary and its descendant construction. The retained-order LOG certificate records the component projection and its checks.

### Gauss–Bonnet invariant

- Gregory Gold, Peng-Ju Hu, Jessica Hutomo, Saurish Khandelwal, Mehmet Özkan, Yi Pang and Gabriele Tartaglino-Mazzucchelli, *On five-dimensional curvature squared supergravity and holography*, arXiv:2504.10856v1, 15 April 2025. See the [cited source](../../../../../references/bibliography.md#GoldEtAl2025), (22)–(23), PDF p.13, for $`H_{\mathrm{GB}}=H_W-4H_{\log}`$ and the corresponding invariant. The corrected definition-derived bosonic project representative remains the comparison action.

The bibliography identifies the cited source versions. Page and equation locators above refer to those versions; source PDFs are not bundled with this calculation.

## Component action

The [assembled action](../../../../action/gb_splus_action.md) gives the density through two physical fermions, its source-term ledger, and the bosonic coefficient comparison in the declared boundary representative.
