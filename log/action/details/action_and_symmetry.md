# Action and symmetry identities

[Reading guide](../README.md). The equation labels and local symbols below follow the action conventions specified for this theory.

<a id="3-action-and-symmetry-audit-including-the-corrections"></a>

## Action and symmetry audit, including the corrections

The two-fermion action order suffices for both classical linear sectors. This chapter derives the correction to the compensating-$`SU(2)`$ parameter and the associated symmetry identities. The earlier parameter is displayed to identify the corrected coefficient; the fixed action uses the corrected expression.

For background $`(\bar\Phi_B,0)`$ and fluctuations $`b^A,\vartheta^r`$, fermion parity gives

```math
S=S^{[0]}[\Phi_{\mathrm B}]
 +S^{[2]}[\Phi_{\mathrm B},\Phi_{\mathrm F}]
 +O(\Phi_{\mathrm F}^{4}).
```

At second variation,

```math
\left.
\frac{\delta^2 O(\Phi_{\mathrm F}^{4})}
{\delta\Phi^I\delta\Phi^J}
\right|_{\Phi_{\mathrm F}=0}=0,
\qquad
\left.
\frac{\delta^2 S}
{\delta\Phi_{\mathrm B}^{A}\delta\Phi_{\mathrm F}^{r}}
\right|_{\Phi_{\mathrm F}=0}=0.
```

so the quadratic action is

```math
S_{\mathrm{quad}}
=\frac12\langle b,\mathcal K_{\mathrm B}b\rangle
+\frac12\langle\vartheta,\mathcal K_{\mathrm F}\vartheta\rangle,
```

```math
\mathcal K_{\mathrm B}
=\left.\delta_{\mathrm B}^{\,2}S^{[0]}\right|_{\bar\Phi_{\mathrm B}},
\qquad
\mathcal K_{\mathrm F}
=\left.\delta_{\mathrm F}^{\,2}S^{[2]}\right|_{\bar\Phi_{\mathrm B},0},
```

```math
\boxed{\mathcal K_I=\mathcal K_{I,2\text{-der}}
+\alpha\mathcal K_{I,\mathrm{Log}},\qquad I=\mathrm B,\mathrm F.}
```

There is no expansion in $`\alpha`$. All boson mixing and all gravitino, spinor, and mixed fermion blocks must be retained.

The source comparison matched the four linear-to-vector slots and 21 LOG blocks, including 621 terms and 452 two-form/three-form replacements. This checks transfer equivalence, not an independent physical derivation of every source coefficient.

Implicit fermion contributions are essential. In the current gauge,

```math
\widehat G_{\mu\nu}
=G_{\mu\nu}+\frac i2\bar\psi_{[\mu}\psi_{\nu]},
\qquad
\widehat H_{\mu\nu\rho}
=H_{\mu\nu\rho}-\frac34\bar\psi_{[\mu}\gamma_\nu\psi_{\rho]},
```

and hence

```math
\begin{aligned}
[\widehat G_{\mu\nu}\widehat G^{\mu\nu}]_{\le2}
&=G_{\mu\nu}G^{\mu\nu}
+iG^{\mu\nu}\bar\psi_{[\mu}\psi_{\nu]},\\
[\widehat H_{\mu\nu\rho}\widehat H^{\mu\nu\rho}]_{\le2}
&=H_{\mu\nu\rho}H^{\mu\nu\rho}
-\frac32H^{\mu\nu\rho}
 \bar\psi_{[\mu}\gamma_\nu\psi_{\rho]}.
\end{aligned}
```

Similarly, the definition

```math
E^a=P^a-\frac i2\bar\psi_b\gamma^{ba}\varphi
-\frac14\bar\psi_b^i\gamma^{abc}\psi_c^jL_{ij}
```

implies

```math
[E_aE^a]_{\le2}
=P_aP^a
-iP_a\bar\psi_b\gamma^{ba}\varphi
-\frac12P_a\bar\psi_b^i\gamma^{abc}\psi_c^jL_{ij}
```

Thus the apparently bosonic current square contributes both mixed and pure gravitino bilinears.

The covariant derivative of the gauge-fixed dilatino is also nonzero:

```math
\left.\mathcal D_a\psi^i\right|_{\mathrm P}
=
\frac18\gamma^{bc}
\left(\widehat G_{bc}
-\frac16\varepsilon_{bcdef}\widehat H^{def}\right)\psi_a^i
-\frac g2L^{ij}\psi_{aj}-\phi_a^i.
```

Consequently,

```math
\chi^{i[1]}
=\frac i8\gamma^a(\mathcal D_a\psi^i)^{[1]}
+\frac g8\varphi^i,
```

```math
(\Box^c\sigma)^{[2]}
=2f_a{}^{a[2]}
-\frac i2\bar\psi_a(\mathcal D^a\psi)^{[1]}
-2\bar\psi_a\gamma^a\chi^{[1]}.
```

The dependent $`S`$ connection, quadratic $`K`$ connection, contorsion, and curvature bilinears contribute to kinetic and algebraic fermion terms. Replacing them by their bosonic values changes the quadratic fermion action.

The LOG density at total fermion degree two is

```math
\begin{aligned}
\ell_{\mathrm{Log}}^{[2]}={}&
N_{\log}^{[2]}
-\frac g2L^{ij}L_{\log\,ij}^{[2]}
+C_aE_{\log}^{a[2]}\\
&+\frac12\bar\psi_a\gamma^a\varphi_{\log}^{[1]}
+\frac i2C_a\bar\psi_b\gamma^{ba}\varphi_{\log}^{[1]}\\
&+\frac i4\bar\psi_a^i\gamma^{ab}\psi_b^jL_{\log\,ij}^{[0]}
+\frac14C_a\bar\psi_b^i\gamma^{abc}\psi_c^jL_{\log\,ij}^{[0]}
\end{aligned}
```

Here degree two includes implicit bilinears from slots with zero explicit fermions.

The two-derivative form-representative difference also matters at this order:

```math
-4gC_aP^a-(-4gC_aE^a)
=-2igC_a\bar\psi_b\gamma^{ba}\varphi
-gC_a\bar\psi_b^i\gamma^{abc}\psi_c^jL_{ij}.
```

The fixed action A28–A30 retains this difference and does not use the former erroneous source shorthand.

The form gauge rules can be checked directly:

```math
H=dB+\frac12C\wedge G+\frac g2E_3,
```

```math
\delta C=d\Lambda,\qquad
\delta E_3=d\Lambda_2,\qquad
\delta B=d\Lambda_1-\frac12\Lambda G-\frac g2\Lambda_2.
```

Using $`dG=0`$,

```math
\begin{aligned}
\delta H
&=d^2\Lambda_1-\frac12d\Lambda\wedge G
-\frac12\Lambda\,dG-\frac g2d\Lambda_2\\
&\quad+\frac12d\Lambda\wedge G+\frac g2d\Lambda_2
=0.
\end{aligned}
```

No field equation is needed for this identity.

The original, now-corrected source equation (4.14) had the following invalid compensator:

```math
\lambda_{\mathrm{src}}^{ij}
=-\frac1{\sqrt2L}S^{k(i}\delta^{j)\ell}\epsilon_{k\ell},
```

```math
S^{ij}
=\bar\epsilon^{(i}\varphi^{j)}
-\frac12\delta^{ij}\delta_{kl}\bar\epsilon^k\varphi^l
```

The common covariant derivative is

```math
\mathcal D_\mu L^{ij}
=\partial_\mu L^{ij}
+2V_\mu{}^{(i}{}_kL^{j)k}
-i\bar\psi_\mu^{(i}\varphi^{j)}
```

which fixes

```math
\delta_U L^{ij}=-2\lambda^{(i}{}_kL^{j)k}.
```

In the aligned gauge, $`(\delta_Q L^{ij})_{\mathrm{traceless}}=iS^{ij}`$. Substitution of the old parameter gives

```math
(\delta_U L^{ij})_{\mathrm{traceless}}=-S^{ij},
```

```math
\boxed{
(\delta_Q+\delta_U)L^{ij}\big|_{\mathrm{traceless}}
=(i-1)S^{ij}\ne0.
}
```

The parameter that actually solves the gauge-preservation equation is

```math
\boxed{
\lambda^{ij}
=-\frac{i}{\sqrt2L}
S^{k(i}\delta^{j)\ell}\epsilon_{k\ell}
}
```

because

```math
(\delta_Q+\delta_U)L^{ij}\big|_{\mathrm{traceless}}
=iS^{ij}-iS^{ij}=0.
```

This correction is fixed by the shared conventions. The original transformation did not preserve the gauge as written.

The supplied package explicitly contains the three-form SUSY rule

```math
\delta_QE_{\mu\nu\rho}
=\bar\epsilon\gamma_{\mu\nu\rho}\varphi
-3i\bar\psi_{[\mu}^{i}\gamma_{\nu\rho]}\epsilon^jL_{ij}
+3\partial_{[\mu}\Lambda_{\nu\rho]}.
```

Temporarily call its coefficients $`p,q`$ and collect derivatives of the local parameter in $`E=P-Q_1-Q_2`$:

```math
\delta E^a\big|_{\partial\epsilon}
=-\frac i2(p-1)U^a
-\left(\frac q6+\frac12\right)W^a,
```

```math
U^a=\partial_b\bar\epsilon\,\gamma^{ab}\varphi,\qquad
W^a=\partial_b\bar\epsilon^i\gamma^{abc}\psi_c^jL_{ij}
```

Supercovariance requires

```math
p-1=0,\qquad \frac q6+\frac12=0
\quad\Longrightarrow\quad
(p,q)=(1,-3)
```

This verifies the necessary parameter-derivative cancellation of the corrected rule.

The action inputs and associated checks used in the spectrum analysis are summarized below.

| Data | Input or established check |
|---|---|
| Bosonic action | Complete source dependencies were available; transfer and stated algebraic conversions checked. The subsequent EOM chapter supplies the independent body-density check. |
| Fermionic kinetic and algebraic terms | Compact supercovariant expressions; the [AdS₅ quadratic action](../../ads5/quadratic_action.md) gives their reduction in Q24–Q40 and the coefficient and diagonal-operator checks in Q58–Q62. |
| Mixing | The quadratic action retains all bosonic and fermionic blocks and implicit supercovariant terms. |
| Bosonic gauge rules | Form transformations checked; geometric and residual internal rules supplied. |
| SUSY data for the linear spectrum | Main multiplet rules supplied; the compensating internal parameter required the correction shown above. |
| Auxiliary fields | Retained in the coupled quadratic action and its constraint analysis. |

The general SUSY-invariance condition at fermion degree one is

```math
\boxed{
\delta_Q^{[1]}S^{[0]}
+\delta_Q^{[-1]}S^{[2]}
=\text{boundary term}
}
```

Here $`\delta_Q^{[-1]}`$ is the bosonic part of a fermion transformation. Fermion-degree counting shows that this condition involves the two-fermion action, including its implicit supercovariant contributions.

