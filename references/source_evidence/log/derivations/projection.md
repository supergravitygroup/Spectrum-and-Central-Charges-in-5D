# Once-only LOG component projection certificate

The equations and reported residuals below belong to the cited construction. Finite component tests and formal symbolic identities retain their distinct scopes; the former do not establish an unrestricted symbolic identity.


Scoped lock: `GAUGED-LOG-CONVENTIONS-v1`, five dimensions, mostly-plus metric, project gamma volume element $`\gamma^{01234}=i`$, $`\epsilon_B^{01234}=+1`$, linear Majorana transpose, and project right SU(2) lowering. No field equation, gauge specialization, integration by parts or derivative commutation is used in this audit.

## Verdict and scope

**PASS for the elementary projection dictionary, its four once-only slot factors, and ordered transport of the full vector derivative. No additional projection sign or coefficient error was found.** This is a review of [log_step6_projection.py](../results/gauged_full_fermionic_log/scripts/log_step6_projection.py), against the cited source pages and independently checked finite matrix/basis identities. It is not a new proof of the source LOG polynomial or its entire curved supersymmetry algebra.


## Evidence gathered

- The source comparison uses C24 PDF12, PDF91 and PDF92. The Weyl scalar/spinor factors, gamma/epsilon/curvature maps, field-dependent S/K shifts, and vector field factors agree with the implemented dictionary.
- C24 Appendix C, PDF90, explicitly identifies the complete vector derivatives after the field-dependent generator changes. It does not identify a connection-stripped derivative.

## 1. Source convention bridge

The source-page locators are [C24 PDF12](https://arxiv.org/abs/2311.00679), (2.15)–(2.16); [PDF83](https://arxiv.org/abs/2311.00679), (A.4); [PDF91](https://arxiv.org/abs/2311.00679), Tables 4–5; and [PDF92](https://arxiv.org/abs/2311.00679), Table 6. The surrounding derivative statement is at [PDF90 text](https://arxiv.org/abs/2311.00679). Every table conversion uses its **Bergshoeff et al. column**, which is the project's component frame.

The metric is unchanged while the Clifford and orientation conventions change by

```math
\Gamma_G^a=i\gamma^a,\qquad \Sigma_G^{ab}=\tfrac12\gamma^{ab},\qquad \epsilon_G^{abcde}=-\epsilon_B^{abcde},\qquad R_G(Q)=\tfrac12R_B(Q),\qquad R_G(M)=-R_B(M),\qquad R_G(J)=-R_B(V).
```

Thus $`\{\Gamma_G^a,\Gamma_G^b\}=-2\eta^{ab}`$ follows from the project Clifford algebra; it is not a signature change. Also $`\Sigma_G^{ab}=-[\Gamma_G^a,\Gamma_G^b]/4=\gamma^{ab}/2`$. The phase and the Sigma factor are therefore mutually consistent. For indexed gamma matrices the locked second-index lowering is

```math
(\gamma^{a_1\cdots a_r})_{\alpha\beta}=\mathsf C_{\beta\delta}(\gamma^{a_1\cdots a_r})_\alpha{}^\delta=-(\gamma^{a_1\cdots a_r}\mathsf C)_{\alpha\beta},\qquad \bar u\gamma^{a_1\cdots a_r}v=u^T\mathsf C\gamma^{a_1\cdots a_r}v.
```

These two kernels differ. The projection preserves the source positions of the spinor indices; it does not silently replace the first kernel by the bilinear kernel. The indexed convention is (S2-02)/(S6-03), grounded in Butter et al. Appendix A (A.3)–(A.11), as already recorded in the project. The prior exact small-matrix tests cover 240 indexed placement/transposition identities. The linear Majorana transpose never conjugates the coefficients $`i`$ in the table.

Writing the numerical SU(2) antisymmetric matrix as $`E`$, the source has $`\varepsilon_G^{ij}=E^{ij}`$ and $`\varepsilon_{Gij}=-E_{ij}`$, with lowering on the left. The target has $`\varepsilon_B^{ij}=\varepsilon_{Bij}=E_{ij}`$, with lowering on the right. Consequently

```math
u_{Gi}=(-E_{ij})u^j=u^jE_{ji}=u_{Bi}.
```

A naked lower source epsilon receives a minus sign; an already lowered physical field has the same numerical array and receives none. `elementary` makes precisely this distinction. `project` also avoids running the source epsilon contractor after switching to the target metrics. This prevents a second, spurious lowering sign.

## 2. Complete elementary field dictionary

The following includes every physical primitive handled by `elementary`. Here $`X^{ij}`$ is the vector triplet, $`X_\alpha^i`$ is the Weyl spinor, and $`Y_G`$ is the Weyl scalar; they are distinct engine symbols.

| Source primitive | Project image | Source derivation |
|---|---|---|
| $`W`$ | $`\rho`$ | C24 Table 6 |
| $`\lambda_{G\alpha}^i`$ | $`-\lambda_\alpha^i`$ | C24 Table 6 |
| $`X^{ij}`$ | $`2Y^{ij}`$ | C24 Table 6 |
| $`F_{Gab}`$ | $`-\widehat F_{ab}`$ | C24 (2.37), (2.38d), with $`v_G=-A`$ |
| $`W_{ab}`$ | $`16T_{ab}/3`$ | C24 Table 4 |
| $`X_\alpha^i`$ | $`-32i\chi_\alpha^i/3`$ | Inverse of C24 (2.15b), $`\chi=3iX\vert/32`$ |
| $`Y_G`$ | $`-128D/3`$ | Inverse of C24 (2.15c), $`D=-3Y_G\vert/128`$ |
| $`X_{ab}^{ij}`$ | $`-4iR(V)_{ab}^{ij}/3`$ | C24 (A.4b), $`R_G(J)=-3iX\vert/4=-R_B(V)`$ |
| $`W_{ab\alpha}^i`$ | $`iR(Q)_{ab\alpha}^i`$ | C24 (2.17), (A.4a), $`R_G(Q)=-iW_{ab}\vert/2=R_B(Q)/2`$ |

For example the two curvature inversions give $`(-3i/4)(-4i/3)=-1`$ and $`(-i/2)i=1/2`$, fixing both the factors and their phases. The Weyl scalar gives $`(-3/128)(-128/3)=1`$, whereas the Weyl spinor gives $`(3i/32)(-32i/3)=1`$. These are independent of the later LOG scalar's overall minus.

The vector-potential sign is not an extra assumption from Table 6: C24 (2.38d), inspected on [PDF19](https://arxiv.org/abs/2311.00679), converts to $`\delta v_G=-\delta A`$. With that sign and the same spinor order, (2.37) becomes

```math
F_{Gab}|=-2e_a{}^\mu e_b{}^\nu\partial_{[\mu}A_{\nu]}+\bar\psi_{[a}\gamma_{b]}\lambda-\tfrac i2\rho\bar\psi_{[a}\psi_{b]}=-\widehat F_{ab},
```

The first term is explicitly the frame pullback of the ordinary field strength. The hat is retained; its bilinears are not discarded.

C24 footnote 4, [PDF9](https://arxiv.org/abs/2311.00679), fixes the inverse two-form map $`U_{\alpha\beta}=\tfrac12(\Sigma_G^{ab})_{\alpha\beta}U_{ab}`$. The four bispinor primitives therefore become

```math
F_{\alpha\beta}|=-\tfrac14(\gamma^{ab})_{\alpha\beta}\widehat F_{ab},\qquad W_{\alpha\beta}|=\tfrac43(\gamma^{ab})_{\alpha\beta}T_{ab},\qquad X_{\alpha\beta}^{ij}|=-\tfrac i3(\gamma^{ab})_{\alpha\beta}R(V)_{ab}^{ij},\qquad W_{\alpha\beta\gamma}^i|=\tfrac i4(\gamma^{ab})_{\alpha\beta}R(Q)_{ab\gamma}^i.
```

These are exactly the `Fs`, `ws`, `z`, and `w3` branches. Spinor epsilons, Lorentz metric and Kronecker deltas remain unchanged; the scalar power token is rendered as the same power of $`\rho`$. Unknown or unresolved odd-derivative tokens raise an error rather than being silently passed through. Every map preserves Weyl weight: $`W,T`$ have weight 1; $`\lambda,\chi,R(Q)`$ have weight $`3/2`$; and $`Y^{ij},\widehat F,D,R(V),R(M),W_{\alpha\beta\gamma\delta}`$ have weight 2.

## 3. The nonlinear four-spinor map

Let $`B_{\alpha\beta\gamma\delta}=W_{\alpha\beta}W_{\gamma\delta}+W_{\alpha\gamma}W_{\beta\delta}+W_{\alpha\delta}W_{\beta\gamma}`$. The symmetrization has unit weight, so $`B=3W_{(\alpha\beta}W_{\gamma\delta)}`$. C24 (A.4c) is

```math
R_G(M)_{ab,cd}=-\tfrac14(\Sigma_{Gab})^{\alpha\beta}(\Sigma_{Gcd})^{\gamma\delta}\big(iW_{\alpha\beta\gamma\delta}+B_{\alpha\beta\gamma\delta}\big).
```

The exact two-form inverse identity is $`\tfrac12(\Sigma_G^{ab})_{\rho\sigma}(\Sigma_{Gab})^{\alpha\beta}=\delta_{(\rho}^{\alpha}\delta_{\sigma)}^{\beta}`$. Apply it to both pairs. The two factors 2 cancel the $`1/4`$, leaving

```math
(\Sigma_G^{ab})_{\alpha\beta}(\Sigma_G^{cd})_{\gamma\delta}R_G(M)_{ab,cd}=-iW_{\alpha\beta\gamma\delta}-B_{\alpha\beta\gamma\delta},\qquad W_{\alpha\beta\gamma\delta}=i\Sigma_G^{ab}{}_{\alpha\beta}\Sigma_G^{cd}{}_{\gamma\delta}R_G(M)_{ab,cd}+iB_{\alpha\beta\gamma\delta}.
```

Now insert $`R_G(M)=-R_B(M)`$, $`\Sigma_G=\gamma^{ab}/2`$ and $`W_{\alpha\beta}|=4\gamma^{ab}_{\alpha\beta}T_{ab}/3`$:

```math
W_{\alpha\beta\gamma\delta}|=-\tfrac i4(\gamma^{ab})_{\alpha\beta}(\gamma^{cd})_{\gamma\delta}R(M)_{ab,cd}+\tfrac{16i}{9}\Big[(\gamma^{ab})_{\alpha\beta}(\gamma^{cd})_{\gamma\delta}+(\gamma^{ab})_{\alpha\gamma}(\gamma^{cd})_{\beta\delta}+(\gamma^{ab})_{\alpha\delta}(\gamma^{cd})_{\beta\gamma}\Big]T_{ab}T_{cd}.
```

This is precisely the production `w4` branch. No quadratic Weyl term or symmetrization factor is missing. Its curvature is the **full constrained unprimed** $`R(M)`$ appearing in (2.17)/(A.4c). It is not the unconstrained primed Lorentz curvature or an assumed symmetric primed Ricci tensor.

The prior basis tests cover the whole algebraic map, not a selection of backgrounds: all 35 independent symmetric four-spinors, and all 10 basis two-forms plus their 45 distinct pair sums. A quadratic map $`Q(T)`$ is determined by $`Q(e_A)`$ and $`Q(e_A+e_B)-Q(e_A)-Q(e_B)`$, so these 55 probes cover every quadratic coefficient. The production map has only linear dependence on $`W_4`$ and quadratic dependence on $`T`$, with no mixed higher-degree term. All 256 output spinor entries were tested in all 90 cases. The production residual is at most $`7.11\times10^{-15}`$. These rational-fraction probes were evaluated in floating point: basis completeness is algebraic, while the numerical residual is finite-precision evidence. The exact displayed inversion supplies the analytic identity; the floating tests are not described as an arbitrary-precision arithmetic proof.

For $`w3`$, the analogous existing check uses all 40 independent two-form-spinor inputs for a fixed SU(2) component, then imposes the conventional solved S-connection projector. Its image is the complete gamma-traceless $`R(Q)`$ sector. The production map, its three-spinor symmetry and the gamma trace agree to $`1.12\times10^{-16}`$. SU(2) is a spectator for this linear map. This does not test an arbitrary unconstrained $`R(Q)`$ as if it were the source Weyl descendant.

The immutable evidence files are [four-spinor basis](../results/gauged_full_fermionic_log/sources/audit_20260925/projection_canonical/four_spinor_projection_basis.json), [three-spinor basis](../results/gauged_full_fermionic_log/sources/audit_20260925/projection_canonical/three_spinor_projection_basis.json), [Clifford checks](../results/gauged_full_fermionic_log/sources/canonical_two_fermi/clifford_checks.json), and [epsilon checks](../results/gauged_full_fermionic_log/sources/audit_20260925/projection_canonical/epsilon_checks.json). Their small exact matrix identities are separate from the floating polynomial probes.

## 4. Full derivative transport and its order

C24 (2.16) defines the component vector derivative as the projection of the complete superspace derivative. Appendix C states that the full derivative remains the same after both the connection and generator changes. There is a direct cancellation check. Treat each connection term as a transformation with its coefficient as parameter. The source Q, S, K parameters inside the derivative are respectively $`\xi_G=-\psi_\mu/2`$, $`\eta_G=-\phi_{G\mu}/2`$, and $`\Lambda_{KG}^a=-f_{G\mu}{}^a`$. Tables 4–5 give

```math
\epsilon_B=-\psi_\mu,\qquad \eta_B=-\tfrac13T_{ab}\gamma^{ab}\psi_\mu+i\phi_{G\mu}=-\phi_\mu,\qquad \Lambda_{KB}^a=-\tfrac13\bar\psi_\mu\gamma^a\chi+f_{G\mu}{}^a=-f_\mu{}^a.
```

The $`T\psi`$ and $`\psi\chi`$ connection shifts cancel the field-dependent S/K pieces of the Q redefinition. The Lorentz and SU(2) basis signs are those in the same tables. Therefore retaining the source derivative as the full target $`\mathcal D_a`$ keeps those terms; expanding only the connection phases would fail this check.

For a stored ordered derivative list $`(a,b)`$, `elementary` first projects the underlying field, applies $`\mathcal D_b`$, then applies $`\mathcal D_a`$. Thus it produces $`\mathcal D_a\mathcal D_b`$, not $`\mathcal D_b\mathcal D_a`$. The same recursive argument holds for arbitrary length. If the projected field is composite, the even derivative obeys its product rule. For the nonlinear map above this retains, for example,

```math
\mathcal D_a\mathcal D_b(T_{cd}T_{ef})=(\mathcal D_a\mathcal D_bT_{cd})T_{ef}+(\mathcal D_bT_{cd})(\mathcal D_aT_{ef})+(\mathcal D_aT_{cd})(\mathcal D_bT_{ef})+T_{cd}\mathcal D_a\mathcal D_bT_{ef}.
```

No derivative is commuted, and no connection, torsion or gravitino is set to zero. The intertwining statement applies to descendants as well as primaries: their source S/K action remains encoded in the full covariant derivative. Gauge evaluation happens later. In particular it cannot turn a derivative of a gauge-fixed compensator into an ordinary derivative of a constant.

## 5. Once-only four-slot normalization and truncation

The slot normalization is the previously checked four-slot Q/S bridge in [LOG_CONVENTIONS.md](../../../../log/action/details/component_construction/results/gauged_full_fermionic_log/LOG_CONVENTIONS.md) (LOG-S1-07)–(LOG-S1-12), not a second Weyl-scalar projection. With the common real normalization $`a=-1/2`$ it gives

```math
L_{\log}=-2H|,\qquad \varphi_{\log}=-2i\varphi_G|,\qquad N_{\log}=-F_G|,\qquad E_{\log}=\mathcal H_G|.
```

`input_polynomials` applies exactly these four factors. In the spinor it combines $`-2i`$ with the defining $`1/3`$ derivative to form $`-2i/3`$; the source lower SU(2) epsilon is subsequently transported by `elementary`. For N and E it imports their completed source descent polynomials and multiplies by $`-1`$ and $`+1`$, respectively. `project` applies only elementary field/geometry maps and contains no second slot factor. For example $`Y_G\mapsto-128D/3`$ and $`F_G\mapsto-N`$ are independent operations on different objects and each occurs once.

The input even slots are retained through explicit fermion degree 2 and the spinor through degree 1 only **after** the needed odd superspace differentiations. The scalar/vector do not come from differentiating that truncated spinor. Every elementary projection preserves Grassmann parity; $`w4\mapsto R(M)+T^2`$ is entirely even. The full covariant derivatives and hatted curvatures retain their implicit fermions. Projection and collection preserve mutual odd-factor order; collection moves only even factors.


## 6. Explicit assumptions and limits

1. The target field definitions are the project's **corrected** Bergshoeff/Ozkan component conventions. In particular the already reconciled explicit $`\psi\chi`$ term of $`R(M)`$, the right SU(2) lowering rule and the linear Majorana bar are part of the declared target. The dictionary does not claim equality to a literal OP expression with the disputed opposite curvature term.
2. The source R(Q) and R(M) are their full conventional constrained curvatures. This is required by C24 (2.17)/(A.4), and was checked in the basis tests. Replacing them by primed curvatures without their dependent connections is outside this map.
3. The identification of the full vector derivative uses C24 Appendix C, including its field-dependent generator changes. The cancellation was displayed above. Independent nonlinear closure of every target transformation is a separate gate, not an additional unexplained normalization assumed by this dictionary.
4. The spinor-index realization assumes the locked nondegenerate symplectic spinor metric and the recorded S2-02 placement. The exact small Clifford/metric tests cover the finite algebra; the w3/w4 probes span their full algebraic domains. They do not by themselves prove spacetime differential Bianchi identities or all-order supersymmetry.
6. No new unresolved elementary convention factor was identified. Higher explicit fermion orders and the unrestricted curved invariant are not certified by this bounded projection audit. The stated PASS applies to the declared source/target frames and current once-only polynomial pipeline.

## Resolution

Every implemented primitive substitution has a source derivation; the nonlinear four-spinor correction contains all three pairings; the gamma/SU(2) placements preserve the locked conventions; and derivative/odd-factor order and the four slot factors are preserved exactly by the implementation. The finite-basis checks cover the entire relevant local algebraic map, with their numerical precision stated separately. **No projection repair is required.**
