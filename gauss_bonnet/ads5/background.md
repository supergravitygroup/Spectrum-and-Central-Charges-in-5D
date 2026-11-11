# Gauss–Bonnet on AdS₅: selected background

[Notation dictionary](../notation.md).

The analysis selects the AdS₅ branch that continuously approaches the two-derivative AdS₅ vacuum as the Gauss–Bonnet coupling tends to zero. Its background values are

```math
a=\lambda_{\rm GB}g^2,\qquad
x=\frac{2}{1+\sqrt{1+2a}},\qquad
L_0=x,\quad N_0=-\frac32gx^2,\quad k=-\frac12g^2x^2.
```

The regular domain is real $`g\ne0`$, $`a>-1/2`$, $`0<x<2`$. The recorded spectrum has **12 bosonic and 12 fermionic local degrees of freedom**, positive local kinetic weights in the source reference convention, and a scalar at the AdS5 BF bound. At $`a=-1/2`$, $`x=2`$, the raw quadratic action vanishes; the generic count is not assigned to that endpoint.

The [first-order equations and branch classification](details/background_branches.md) determine these background values. The [local Killing-spinor conditions](code/derivations/support/gb-splus-spectrum-method-EXPLAIN.md) specify the supersymmetric branch. The [action inputs](action_inputs.md) fix the coupling normalization.

[Quadratic action](quadratic_action.md) · [Spectrum](spectrum.md)
