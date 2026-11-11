# Gauss–Bonnet on AdS₅: inputs and calculation scope

The [equation-to-code map](code/SOURCE_MAP.md) and
[input manifest](code/inputs/action_sources.json) identify the component inputs.
The [component action](../action/gb_splus_action.md), GB09, fixes the upper-index
triplet derivative used in the connection-sector calculation (6.21), followed
by the coefficient collection (6.29)–(6.30). The
[fermionic reduction](details/fermionic_reduction.md), FC1–FC6 and FC14–FC15,
supplies the fermionic quadratic action (6.31).

The [two-derivative coefficient derivation](../../common/two_derivative_action/details/gb_input_qualifications.md),
A9–A13, specifies the raw gravitino mass and algebraic mixing used by that Hessian.

## Component calculation and parameter restoration

The [component core](code/src/fermion_operator.py) uses
`k=-1, g=1, x=sqrt(2), m=1/2, u=3`. The
[operator calculation](code/calculations/fermion_operator.py) evaluates radial
exponents 0 through 4 and interpolates the matrix. FC10–FC13 state the covariance
and homogeneity argument restoring the branch-parameter dependence.

This finite component evaluation and the
[symbolic fermionic reduction](code/calculations/fermionic_reduction.py) have
separate roles. The retained FC1–FC9 expansion and FC13–FC15 coefficient relations
supply the analytical derivation. The
[reproduction guide](../../README.md#reproduction) states the executable check coverage.
