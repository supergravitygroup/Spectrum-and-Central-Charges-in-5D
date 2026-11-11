# Quadratic fluctuation problem

The independent fields are retained as

```math
\Phi_B=\{e_\mu{}^a,C_\mu,B_{\mu\nu},E_{\mu\nu\rho},L,N,V_\mu,V_\mu^{\prime ij}\},
\qquad \Phi_F=\{\psi_\mu^i,\varphi^i\}
```

The quantities $`T,D,\chi,\omega,\phi,f`$ are substituted composites and dependent connections, not new independent Euler equations.

```math
\Phi=\bar\Phi+t\phi,\qquad
S=S^{[0]}+tS^{[1]}+t^2S^{[2]}+O(t^3),\qquad
S^{[2]}=\frac12\left.\frac{d^2S}{dt^2}\right|_{t=0}.
```

On a stationary background, $`S^{[1]}`$ vanishes by the bulk equations. This is not an expansion in $`\alpha,\beta,\zeta`$. No second factor of 1/2 is added to the quadratic coefficients used.

Since $`\bar\Phi_F=0`$ on a bosonic background, a monomial of physical fermion degree $`2r\ge4`$ has vanishing quadratic fluctuation coefficient:

```math
(t\Phi_F)^{2r}=t^{2r}(\Phi_F)^{2r},\qquad
[t^2]t^{2r}=0\quad(r\ge2).
```

The existing two-fermion action therefore supplies the order required for the fermionic Hessian. Implicit two-fermion pieces in covariant derivatives and composites are still included. [R² §1.1](../r2/ads5/README.md), [LOG Q5–Q6](../log/ads5/quadratic_action.md).

## Retaining forms and metric mixing

```math
G=dC,\qquad H=dB+\tfrac12C\wedge G+\tfrac g2E_3,
```

```math
G^{[1]}=dc,\qquad
H^{[1]}=db+\tfrac12c\wedge\bar G+\tfrac12\bar C\wedge dc+\tfrac g2e_3,
\qquad H^{[2]}=\tfrac12c\wedge dc.
```

Hodge-star variations and determinant coefficients form part of form–metric mixing. The condition $`\bar E=0`$ does not remove the e₃ fluctuation or its field equation. If the source expands the vielbein linearly, its quadratic metric coefficient is retained; comparison with a direct metric expansion requires the same stationary background and a specified field transformation. [Field definitions](details/field_definitions.txt).

## Definition of physical modes

The source procedure constructs the coupled quadratic operator, identifies gauge directions and constraints, isolates physical representatives, and reads characteristic roots. A root of a diagonal entry alone is not an eigenmode of the coupled system. Diffeomorphisms, residual internal U(1), form gauge symmetries, and local SUSY are used under the conditions of their respective source calculations.

A field redefinition containing denominators is recorded with its invertibility conditions. Divided generic-branch formulas are not used on critical surfaces. Jordan information is supplied when both the eigenvector kernel and generalized solutions have been examined at a repeated root; equal masses alone do not establish a Jordan chain.

On product geometries, fields with the same quantum numbers are treated together. Scalar, vector, and tensor harmonics have different lowest levels; substituting n=0 into the generic-level matrix does not remove nonexistent harmonics. Charge-conjugate symplectic-Majorana coefficients are not counted as two independent complex sets. Global boundary modes are not automatically included in local propagation counts.
