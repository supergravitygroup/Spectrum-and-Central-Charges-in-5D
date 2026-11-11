# Multiplet roles

Use [the construction framework](00_action_construction_framework.md), lock `R2-PRIMED-BF-CONSTRUCTION-FRAMEWORK-v1`. The machine record is [multiplet_selection.json](multiplet_selection.json).

```math
\begin{aligned}
1&:\ (Y'_{ij},\rho',A'_\mu,\lambda'^i),\\
2&:\ (Y_{ij},\rho,A_\mu,\lambda^i),\\
\text{original linear input}&:\ (L_{ij},\varphi_i,E_a,N),\\
\text{new mixed linear output}&:\ (L'_{ij},\varphi'_i,E'_a,N').
\end{aligned}
```

Both vector maps use the same original unprimed linear input. The primed vector is the earlier composite; the unprimed vector is Gold's defining vector. BF pairs the primed vector with the new primed linear output. Apply the two vector maps only after constructing and inserting the mixed linear output into BF. Step 1’s full primed BF density is fixed in [the BF density derivation](03_step1_full_primed_BF_density.md). The [mixed components](04_step2_mixed_primed_linear_multiplet.md) are now constructed in vector notation. The [BF insertion](05_step3_mixed_linear_inserted_in_BF.md) is complete in Step 3; the [unprimed Gold substitution and gauge restriction](06_step4_Gold_unprimed_vector_and_gauge.md) are complete in Step 4. The [primed-vector substitution](08_step5_primed_composite_vector_insertion.md) is given in Step 5, followed by the [gauged action through two physical fermions](10_step6_gauged_action_through_two_fermions.md).
