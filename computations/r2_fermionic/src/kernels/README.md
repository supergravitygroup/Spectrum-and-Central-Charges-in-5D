# Exact component tensors

`step6_elementary_algebra.py` implements ordered tensor algebra.
`step6_elementary_maps.py` and `step6_supercovariant_maps.py` give the elementary
and retained-supercovariant composite maps. The final coefficient ledgers are
in [expected](../../expected/README.md), and the canonical density is in
[the action record](../../outputs/r2_action.md).

The insertion builders and verification kernels are executed through
[the component-check runner](../../checks/run_component_checks.py), which
supplies the required source layout in temporary storage. Run that entry point
rather than invoking these source-layout-dependent kernels in place.
