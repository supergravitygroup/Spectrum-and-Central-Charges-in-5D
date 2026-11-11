# Independent fields

[Reading guide](../README.md). The equation labels and local symbols below follow the action conventions specified for this theory.

<a id="2-independent-field-inventory"></a>

## Independent-field inventory

In the gauge already used by the action, the independent field set is

```math
\boxed{
\begin{aligned}
\Phi_{\mathrm B}
&=\left\{
e_\mu{}^a,\ C_\mu,\ B_{\mu\nu},\ E_{\mu\nu\rho},
\ L,\ N,\ V_\mu,\ V_\mu^{\prime\,ij}
\right\},\\
\Phi_{\mathrm F}
&=\left\{\psi_\mu^i,\ \varphi^i\right\},
\end{aligned}}
```

Independence refers to action variables; it does not decide whether a field is auxiliary or propagating.

| Sector | Independent field | Definition |
|---|---|---|
| Bosonic | $`e_\mu{}^a`$ | Vielbein |
| Bosonic | $`C_\mu`$ | Abelian one-form potential of the defining vector |
| Bosonic | $`B_{\mu\nu}=B_{[\mu\nu]}`$ | Two-form potential |
| Bosonic | $`E_{\mu\nu\rho}=E_{[\mu\nu\rho]}`$ | Three-form potential of the independent linear multiplet |
| Bosonic | $`L`$ | Remaining scalar of the gauge-fixed triplet; $`L\neq0`$ |
| Bosonic | $`N`$ | Second linear-multiplet scalar |
| Bosonic | $`V_\mu`$ | Trace of the internal connection; residual $`U(1)`$ connection |
| Bosonic | $`V_\mu^{\prime\,ij}`$ | Symmetric internal connection components, $`\delta`$-traceless |
| Fermionic | $`\psi_\mu^i`$ | Grassmann-odd symplectic-Majorana gravitino |
| Fermionic | $`\varphi^i`$ | Grassmann-odd symplectic-Majorana linear-multiplet fermion |

The connection $`V_\mu^{ij}`$ and its trace/traceless parts are not three separate field groups. The decomposition and inverse are

```math
\begin{aligned}
V_\mu^{ij}
&=V_\mu^{\prime\,ij}+\frac12\delta^{ij}V_\mu,
&\delta_{ij}V_\mu^{\prime\,ij}&=0,\\
\delta_{ij}V_\mu^{ij}
&=0+\frac12\delta_{ij}\delta^{ij}V_\mu=V_\mu,
&V_\mu^{\prime\,ij}
&=V_\mu^{ij}-\frac12\delta^{ij}\delta_{kl}V_\mu^{kl}
\end{aligned}
```

Thus the inventory uses either $`V_\mu^{ij}`$ or $`(V_\mu,V_\mu^{\prime ij})`$.

Likewise the gauge-fixed linear-multiplet triplet is determined by $`L`$ alone:

```math
L_{ij}=\frac{L}{\sqrt2}\delta_{ij},
\qquad
L^{ij}L_{ij}
=\frac{L^2}{2}\delta^{ij}\delta_{ij}=L^2.
```

The objects $`E_a,E^{\mu\nu},E_{\mu\nu\rho}`$ are not independent copies. In the three-form representative,

```math
\begin{aligned}
E^{\mu\nu}
&=-\frac1{12}\varepsilon^{\mu\nu\rho\sigma\lambda}
E_{\rho\sigma\lambda},\\
P^\mu
&=-\frac1{12}\varepsilon^{\mu\nu\rho\sigma\lambda}
\partial_\nu E_{\rho\sigma\lambda},\\
E^a
&=e_\mu{}^aP^\mu
-\frac i2\bar\psi_b\gamma^{ba}\varphi
-\frac14\bar\psi_b^i\gamma^{abc}\psi_c^jL_{ij}.
\end{aligned}
```

The ordinary-current conservation law follows identically:

```math
\partial_\mu(eP^\mu)
=-\frac1{12}\epsilon^{\mu\nu\rho\sigma\lambda}
\partial_\mu\partial_\nu E_{\rho\sigma\lambda}=0
```

The antisymmetric epsilon kills the symmetric pair of partial derivatives. This is not the $`E_3`$ equation of motion, and no unconstrained extra vector $`E_\mu`$ is introduced.

Dependent connections form a separate class:

| Connection | Defining condition | Inventory status |
|---|---|---|
| $`\omega_\mu{}^{ab}`$ | $`R(P)=0`$; vielbein and gravitino torsion | Dependent bosonic connection |
| $`\phi_\mu^i`$ | $`\gamma^a\widehat R(Q)_{ab}^i=0`$ | Dependent fermionic $`S`$connection |
| $`f_\mu{}^a`$ | $`\widehat R(M)`$conventional Ricci-trace condition | Dependent bosonic $`K`$connection |

Their definitions in the present gauge are

```math
\begin{aligned}
\omega_\mu{}^{ab}
&=\omega_\mu{}^{ab}(e)
+\frac12\bar\psi^{[a}\gamma^{b]}\psi_\mu
+\frac14\bar\psi^a\gamma_\mu\psi^b,\\
\phi_\mu^i
&=\frac i3\gamma^a\widehat R'_{\mu a}{}^i(Q)
-\frac i{24}\gamma_\mu\gamma^{ab}\widehat R'_{ab}{}^i(Q),\\
f_\mu{}^a
&=-\frac16\mathcal R_\mu{}^a
+\frac1{48}e_\mu{}^a\mathcal R,
\qquad
\mathcal R_{\mu\nu}
=\widehat R'_{\mu\rho}{}^{ab}(M)e_b{}^\rho e_{\nu a}
\end{aligned}
```

The curvatures are constructed from the same independent fields. Using these definitions does not eliminate auxiliaries by equations of motion.

The following objects likewise add no independent fields:

| Objects | Status |
|---|---|
| $`Y^{ij},T_{ab},D,\chi^i`$ | Gauged Dilaton–Weyl composites |
| $`\rho_{\mathrm{linear}},\lambda_{\mathrm{linear}}^i,Y_{\mathrm{linear}}^{ij},\widehat F_{\mathrm{linear}}`$ | Vector-multiplet composites built from the independent linear multiplet and common geometry |
| Effective vector slots | Specified sum of these composites and the defining vector |
| $`L_{\log}^{ij},\varphi_{\log}^i,N_{\log},E_{\log}^a,P_{\log}^a`$ | Composite LOG multiplet and current |
| $`G,\widehat G,H,\widehat H`$, all curvatures and covariant derivatives | Covariants derived from independent fields |
| $`g_{\mu\nu}=e_\mu{}^ae_\nu{}^b\eta_{ab}`$, $`e`$, $`\gamma_\mu=e_\mu{}^a\gamma_a`$ | Objects determined by the vielbein |
| $`\omega_{\pm\mu}{}^{ab}=\omega_\mu{}^{ab}\pm\widehat H_\mu{}^{ab}`$ | Derived torsionful connections |

In particular, the composite $`D`$ differs from the independent scalar $`N`$; the composites $`\chi^i,\varphi_{\log}^i`$ differ from the independent fermion $`\varphi^i`$; and the dependent $`S`$ connection $`\phi_\mu^i`$ differs from both $`\varphi^i`$ and $`\psi_\mu^i`$.

The gauge-fixed fields

```math
\sigma=1,\qquad \psi^i=0,\qquad b_\mu=0
```

are not independent in this inventory. Nevertheless the dilatino derivative remains

```math
\left.\mathcal D_a\psi^i\right|_{\mathrm P}
=
\frac18\gamma^{bc}
\left(\widehat G_{bc}
-\frac16\varepsilon_{bcdef}\widehat H^{def}\right)\psi_a^i
-\frac g2L^{ij}\psi_{aj}-\phi_a^i
```

which is generally nonzero and introduces no new fermion.

The auxiliary/dynamical status of each independent field must therefore be determined from the coupled total theory $`S_{2\text{-der}}+\alpha S_{\mathrm{Log}}`$, not inherited from its two-derivative part.

