# R²: selected AdS5 background

[Notation dictionary](../notation.md).


```math
\mathbb I^i{}_j=\epsilon^{ik}\frac{\delta_{kj}}{\sqrt2},\quad
\mathbb I^2=-\frac12,\quad\mathbb J=i\sqrt2\mathbb I,\quad\mathbb J^2=1.
```
Under gauge-preserving SUSY, the background variation of the linear-multiplet fermion is
```math
\delta\varphi|_0=\left(\frac{N_0}{2}+\frac{3gL_0^2}{4}\right)\epsilon
```
so a nonzero Killing spinor requires
```math
N_0=-\frac32gL_0^2
```
The gravitino equation
```math
\nabla_\mu\epsilon=m\gamma_\mu\mathbb J\epsilon,
\quad m=\frac{gL_0}{2\sqrt2}
```
and its integrability condition
```math
[\nabla_\mu,\nabla_\nu]\epsilon=-2m^2\gamma_{\mu\nu}\epsilon
=-\frac1{2\ell^2}\gamma_{\mu\nu}\epsilon
```
give eight real supersymmetries. Family II satisfies these conditions only at $`L_0=4/3`$, and family III only at its $`L_0=22/19`$ intersection with family I.

The selected, Einstein-connected vacuum branch is
```math
\boxed{
L_0=\frac2{1+\sqrt{1-3\lambda_{R^2}g^2}},\quad
\lambda_{R^2}g^2\le\frac13,\quad g\neq0
}
```
The abbreviations are $`L=L_0`$, $`A=4-3L`$, and $`B=2-L`$. On the open branch $`\lambda_{R^2}g^2<1/3`$, $`B>0`$, while $`A`$ changes sign at $`\lambda_{R^2}g^2=1/4`$. The generic eigenfield and simple-pole formulas require $`\lambda_{R^2}AB\ne0`$. The two-derivative point, the $`A=0`$ degeneration and the $`B=0`$ endpoint are treated separately in [critical branches](details/critical_branches.md). This choice uses a root of the total background equation rather than assuming the two-derivative background in advance.

$`L_0>0`$ is the field region where the composite denominators $`L^{-1}`$ are regular. At finite admissible parameters,
```math
R_0=-20\ell^{-2},\quad R_{\mu\nu}R^{\mu\nu}=80\ell^{-4},\quad
R_{\mu\nu\rho\sigma}R^{\mu\nu\rho\sigma}=40\ell^{-4}
```
is finite. The preserved local gauge structure comprises diffeomorphisms, Lorentz symmetry, residual $`U(1)`$, $`C`$ gauge symmetry, coupled form gauge symmetry, and local SUSY. The subset of gauge parameters leaving the background fixed is distinguished from gauge equivalence of fluctuations.

The global spectrum uses the universal cover of AdS₅, central regularity, fixed boundary sources, and zero symplectic boundary flux. Only gauge directions preserving the boundary conditions and carrying zero surface charge are removed in the quotient; asymptotic symmetries are not removed in the same way.


## Background equations and other roots

The [background equations and branch classification](details/background_branches.md) give the derivation and the other roots of the same theory. The spectrum uses the branch specified above.

[Quadratic action](quadratic_action.md) · [Spectrum](spectrum.md)
