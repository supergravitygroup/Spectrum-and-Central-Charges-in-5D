# LOG component multiplet and bosonic action — S6-B01 – S6-B03

<a id="step-6--the-log-multiplet-in-our-conventions--75-bosonic-action-and-comparison"></a>

[Component index](../STEP_06_LOG_PROJECTED_MULTIPLET_AND_BOSONIC_ACTION.md). Definitions and source conventions are in [the opening section](convention_001.md).

### 7.5 Bosonic action and comparison

First, (S6-27), with the degree-zero parts of the four expressions above, is the bosonic action before gauge fixing. For a readable curvature basis we next give the $`\rho=1,b_\mu=0`$ representative. The [complete calculated bosonic certificate](../../../../../../../references/source_evidence/log/derivations/bosonic.md) establishes it from the complete newly calculated bosonic slots, in addition to the earlier raw-source audit. Covariant derivatives of the compensator are evaluated before the gauge slice; they are not set to zero before projection.

Let $`F_{ab}=2\partial_{[a}A_{b]}`$ in this bosonic subsection only, $`Y^2=Y^{ij}Y_{ij}`$ and $`T^2=T_{ab}T^{ab}`$. Here $`D_a`$ is the bosonic spin/SU(2) covariant derivative after degauging; it is distinct from the full $`\mathcal D_a`$ used in the components above. Transporting every term of the corrected Standard-Weyl bosonic ledger in the prior derivation gives

```math
\begin{aligned}
\ell_{\log}^{\rm SW,bos}\simeq_{\partial}{}&-\tfrac1{12}\epsilon^{abcde}A_aR(V)_{bc}^{ij}R(V)_{deij}+\tfrac16R(V)_{ab}^{ij}R(V)^{ab}_{ij}-\tfrac16R_{ab}R^{ab}+\tfrac{23}{384}R^2-\tfrac83D^2\\
&-\tfrac14R_{abcd}F^{ab}F^{cd}-\tfrac{32}{3}R_{abcd}T^{ab}T^{cd}+\tfrac{16}{3}R_{ab}T^{ac}F^b{}_c+\tfrac{64}{3}R_{ab}T^{ac}T^b{}_c\\
&+R\left(\tfrac3{32}F^2-\tfrac53T_{ab}F^{ab}+3T^2+\tfrac12D-\tfrac18Y^2\right)+Y^{ij}R(V)_{abij}\left(\tfrac{16}{3}T^{ab}-F^{ab}\right)\\
&+8Y^2T^2-\tfrac14Y^2F^2+\tfrac12(Y^2)^2+D\left(-\tfrac{32}{3}T_{ab}F^{ab}-F^2+\tfrac{736}{9}T^2+12Y^2\right)\\
&-\tfrac{64}{9}T^2(T_{ab}F^{ab})-\tfrac{1024}{3}T^{ab}F^{cd}T_{ac}T_{bd}-\tfrac{50}{3}T^2F^2+64T^{ab}F^{cd}T_{ac}F_{bd}\\
&+2(T_{ab}F^{ab})F^2-4T^{ab}F^{cd}F_{ac}F_{bd}-\tfrac1{32}(F^2)^2+\tfrac18F^{ab}F^{cd}F_{ac}F_{bd}+\tfrac{10720}{27}(T^2)^2\\
&+\epsilon^{abcde}(D^fT_{af})\left(-\tfrac{64}{3}T_{bc}F_{de}+F_{bc}F_{de}+\tfrac{256}{3}T_{bc}T_{de}\right)\\
&+\epsilon^{abcde}(D^fF_{af})\left(2T_{bc}F_{de}-\tfrac1{16}F_{bc}F_{de}-\tfrac{16}{3}T_{bc}T_{de}\right)\\
&-\tfrac{32}{3}T^{cd}D^aD_aT_{cd}+8F^{ac}D_cD^dT_{ad}-(D_aY^{ij})(D^aY_{ij})+\tfrac14(D_aF_{bc})(D^aF^{bc}).
\end{aligned}
\tag{S6-B01}
```

For clarity, representative multiplication chains connecting this formula to the source ledger are

```math
\begin{aligned}
\tfrac38R_Gww&\longmapsto-\tfrac38(\tfrac{16}{3})^2RTT=-\tfrac{32}{3}RTT,\qquad
\tfrac{23}{8}Dw^2\longmapsto\tfrac{23}{8}(\tfrac{16}{3})^2DT^2=\tfrac{736}{9}DT^2,\\
-\tfrac38wD^2w&\longmapsto-\tfrac38(\tfrac{16}{3})^2TD^2T=-\tfrac{32}{3}TD^2T,\qquad
-\tfrac32F_G^{ac}D_cD^dw_{ad}\longmapsto(-\tfrac32)(-1)(\tfrac{16}{3})F^{ac}D_cD^dT_{ad},\\
\tfrac{1005}{2048}(w^2)^2&\longmapsto\tfrac{1005}{2048}(\tfrac{16}{3})^4(T^2)^2=\tfrac{10720}{27}(T^2)^2,\qquad
-\tfrac12X_G^{ij}(w+F_G)^{ab}\Phi_{abij}\longmapsto Y^{ij}(\tfrac{16}{3}T-F)^{ab}R(V)_{abij}.
\end{aligned}
\tag{S6-B02}
```

Each omitted index in the short first entries of this arithmetic is precisely the contraction on the corresponding term of (S6-B01). The full algebraic coefficient audit is in the step-6 check record. The coefficient $`-32/3`$ of $`RTT`$ includes the inherited raw-source $`Rww`$ correction; it is not an extra correction to be added again.

Finally substitute (S6-31)–(S6-33), apply the boundary ledger (S6-29)–(S6-30), and keep the independent compensator. The comparison is:

| Sector | This comparison calculation | Earlier project result | Scope |
|---|---|---|---|
| Weyl scalar projection | $`-8D^2/3+736T^2D/9`$ in $`N_{\log}`$ | LOG-CORR03 after the $`w=16T/3`$ bridge | Fresh projection of the independently checked primary descent |
| Standard-frame $`Rww`$ | $`3/8`$ | LOG-CORR04 | Independently recovered from the complete calculated scalar/vector/BF polynomial |
| Gauged explicit-$`E`$ block | $`g^2E^2/3+gE\!\cdot\mathop{\mathrm{div}}\nolimits G/3-g\epsilon EGG/24-2g\epsilon EHH/3`$ | LOG-CORR02 | Reproduced term by term in (S6-33)–(S6-35) |
| Curvature-only limit | $`-R_{ab}R^{ab}/6+R^2/24`$ | Prior final LOG action | Explicit coefficient sum (S6-37) |
| Scalar and ordered-quartic sectors | Full coefficient equality under the stated maps | Prior final LOG action | Earlier independent polynomial/tensor checks rerun; no new source fit |
| Complete new raw bosonic slots versus the reduced basis | Exact zero residual | Entire LOG-CORR05, including all flux/derivative and independent-$`E`$ terms | Certified 2026-09-25 with explicit boundary currents and pointwise certificate replay |

The endpoint below is the same corrected bosonic representative as the earlier project's `eq:L-final-expanded`, with the same equality-up-to-boundary qualification. Its exact full-form comparison is recorded in the check file; the four explicit-$`E`$ terms occur once. With $`L^{ij},N,E^a`$ now denoting the **independent compensator**, the resulting comparison density is:

The boundary equality is now independently certified on the actual calculated components; the complete current and exact pointwise replays are in [the bosonic certificate](../../../../../../../references/source_evidence/log/derivations/bosonic.md), (B-13).

<!-- STEP6_BOSONIC_COMPARISON_BEGIN -->

```math
\begin{aligned}
\ell_{\log}^{\rm gauged,bos}\simeq_{\partial}{}& -\frac1{12}\epsilon^{abcde}C_aV_{bc}^{ij}V_{de\,ij} +\frac16V_{ab}^{ij}V^{ab}_{ij} +\frac g6V_{ab}^{ij}L_{ij}G^{ab} +\frac{2g}{3}V_{ab}^{ij}L_{ij}H^{ab}\\
&-\frac16R_{ab}R^{ab}+\frac1{24}R^2 +\frac16R_{ab}G^{ac}G^b{}_c -\frac43R_{ab}G^{ac}H^b{}_c\\
&+R\left(\frac g6N-\frac{g^2}{12}L^{ij}L_{ij} +\frac13G_{ab}H^{ab}-\frac13H_{ab}H^{ab}\right)\\
&-\frac{g^2}{6}N^2+\frac{2g^3}{3}N L^{ij}L_{ij} +\frac{5g^4}{24}(L^{ij}L_{ij})^2\\
&+gN\left(-\frac13G_{ab}G^{ab}-\frac23G_{ab}H^{ab} +2H_{ab}H^{ab}\right)\\
&+g^2L^{ij}L_{ij}\left(\frac1{24}G_{ab}G^{ab} -\frac16G_{ab}H^{ab}-H_{ab}H^{ab}\right)\\
&-\frac1{48}(G_{ab}G^{ab})^2 -\frac13(G_{ab}G^{ab})(G_{cd}H^{cd}) +\frac23(G_{ab}G^{ab})(H_{cd}H^{cd})\\
&+\frac43(G_{ab}H^{ab})^2 -\frac43(G_{ab}H^{ab})(H_{cd}H^{cd}) -2(H_{ab}H^{ab})^2\\
&-\frac1{24}G_{ab}G^{bc}G_{cd}G^{da} +G_{ab}G^{bc}G_{cd}H^{da} -\frac43G_{ab}G^{bc}H_{cd}H^{da}\\
&-\frac83G_{ab}H^{bc}G_{cd}H^{da} +\frac{16}{3}G_{ab}H^{bc}H_{cd}H^{da}\\
&-\frac16(\nabla_bG^{ab})(\nabla^cG_{ac}) +\frac23(\nabla_aH_{bc}) \left(\nabla^aH^{bc}+\nabla^bH^{ca}+\nabla^cH^{ab}\right)\\
&-\frac{g^2}{4}(\nabla_aL^{ij})(\nabla^aL_{ij})\\
&+\frac1{48}(\nabla^bG_{ab})\epsilon^{acdef}G_{cd}G_{ef} +\frac13(\nabla^bG_{ab})\epsilon^{acdef}H_{cd}H_{ef}\\
&-\frac16(\nabla^bG_{ab})\epsilon^{acdef}H_{cd}G_{ef}\\
&+\frac1{12}(\epsilon^{abcde}G_{bc}G_{de}) (\epsilon_{a}{}^{fghi}H_{fg}H_{hi})\\
&+\frac g3E_a\nabla_bG^{ab} -\frac g{24}E_a\epsilon^{abcde}G_{bc}G_{de} -\frac{2g}{3}E_a\epsilon^{abcde}H_{bc}H_{de} +\frac{g^2}{3}E_aE^a.
\end{aligned}
\tag{S6-B03}
```

<!-- STEP6_BOSONIC_COMPARISON_END -->

[Previous component](vector_265.md) · [Component index](../STEP_06_LOG_PROJECTED_MULTIPLET_AND_BOSONIC_ACTION.md)
