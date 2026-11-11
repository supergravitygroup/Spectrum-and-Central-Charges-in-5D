# Symbolic SUSY checks

This directory reruns coefficient checks for the following mathematical appendices:

- [General vector–linear density and boundary current](../vector_linear_density.md).
- [Weyl triplet/spinor transformations](../../../weyl2/action/multiplet_derivations.md).
- [Scalar/spinor transformations of the common linear–vector map](../linear_vector_map.md).

[run_checks.py](run_checks.py) uses Python 3 and SymPy. Intermediate polynomials are evaluated in a temporary directory. Successful output also includes the calculation-file SHA-256 hashes. The runner rejects optimized Python execution (`-O`, `-OO`, or a nonzero `PYTHONOPTIMIZE`) before executing any calculation, because the final equality checks use assertions.

The checks assign no numerical values to physical fields, couplings, or ratios. They use Clifford-basis indices, the specified dimension five, the metric, and fixed rational coefficients. Fields, field derivatives, and curvatures remain symbolic. Norm, gamma-trace, and Bianchi relations required by the equations are applied through explicit projectors.

Some intermediate files generate residual polynomials before tensor identities are applied. A nonzero intermediate residual is not itself a failure; that polynomial is the direct input to the final reduction. Final residuals are tested for exact equality to zero, without numerical tolerances.

The [check record](../../../references/component_records/02_action_family.md) specifies the proof scope and fermion degrees of the executed calculations. A successful runner does not certify action or multiplet identities outside that record.
