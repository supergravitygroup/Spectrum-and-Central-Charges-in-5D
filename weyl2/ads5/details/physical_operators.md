# Physical operators and field combinations

[Reading guide](../README.md). The equation labels and local symbols below follow the action conventions specified for this theory.

<a id="10-decomposition-of-physical-operators-and-field-combinations"></a>

## Decomposition of physical operators and field combinations

This section decomposes the solution space of the coupled linearized equations. No independent field is removed from the off-shell action in Appendix A. Abbreviations:

```math
q:=\alpha g^2,\quad
m:=\frac{ig}{2\sqrt2}J,\quad m^2=\frac{g^2}{8},\quad
\rho^2:=1-\frac6{\alpha g^2},
```

```math
\nu^2:=\frac{g^2}{2}-\frac3\alpha=\frac{g^2}{2}\rho^2,\qquad
\kappa:=\frac{3g^2}{2}+\frac3\alpha=2g^2-\nu^2.
```

In the real-root region, $`\rho\ge0`$ is only a label choice; both $`\sigma=\pm1`$ branches are retained. $`q`$ is never fixed to a sample number. $`\rho=1`$ is not a solution for finite $`\alpha,g`$.

<a id="101-scalarmetric-decomposition"></a>

### Scalar–metric decomposition

```math
\lambda_{\rm s}=\lambda-\frac{16\alpha}{3}d,\qquad
h_{\mu\nu}
=H_{\mu\nu}
-\frac23\bar g_{\mu\nu}(\lambda_{\rm s}+4\alpha d)
+\text{diffeomorphism direction}.
```

Back-substitution into the source scalar equations:

```math
\lambda=\lambda_{\rm s}+\frac{16\alpha}{3}d,\qquad
n=-2g\lambda+\frac{8\alpha g}{3}d
=-2g\lambda_{\rm s}-8\alpha g\,d.
```

```math
(\Box+2g^2)\lambda_{\rm s}=0,\qquad
(\Box+\kappa)d=0.
```

The physical spin-2 part of $`H_{\mu\nu}`$ is transverse and traceless. Defining $`O_0:=\Box+g^2`$ gives

```math
\mathcal L_{TT}^{(2)}
=\frac{\alpha}{12}H^{\mu\nu}O_0(O_0+\kappa)H_{\mu\nu},
\qquad
O_0(O_0+\kappa)H=0.
```

When $`\kappa\neq0`$,

```math
H_0=\frac{O_0+\kappa}{\kappa}H,\qquad
H_1=-\frac{O_0}{\kappa}H,\qquad H=H_0+H_1
```

and

```math
O_0H_0=0,\qquad (O_0+\kappa)H_1=0
```

This division is not performed when $`\kappa=0`$.

<a id="102-coupled-formvector-decomposition"></a>

### Coupled form–vector decomposition

Denote the linearized field strengths here by $`G,H_3`$:

```math
G=dc,\qquad H_3=db+\frac g2a_3,\qquad
F=G+*H_3=8\tau,\qquad
j_F^\mu=\nabla_\nu F^{\nu\mu}.
```

This $`F`$ is not the field strength of the linear-map vector in Appendix A.
The Bianchi relation and the definition of $`E_3`$ give

```math
p^\mu=\frac1g(j_F^\mu-j_G^\mu)
```

Thus neither $`p`$ nor $`E_a`$ is counted as a separate independent field.

When $`\nu^2\neq0`$,

```math
T=\frac{\mathop{\mathrm{div}}\nolimits dF}{\nu^2},\qquad
j_T=0,\qquad F=T+dA
```

This decomposition can be used on physical solutions. The two-form mode $`T`$ here does not have the same normalization as the nonlinear composite $`T_{ab}`$; it is the transverse component defined through $`F=8\tau`$. $`A`$ is also a potential for this decomposition, not a new off-shell field.

```math
(\Box+3g^2-\nu^2)T=0.
```

For transverse vectors,

```math
t:=\mathop{\mathrm{div}}\nolimits d=\Box+2g^2,\qquad
Y=(A,c,v)^T,\qquad a_0=1-\frac{\alpha g^2}{6}
```

the quadratic form is

```math
\mathcal L_V=Y^TtM(t)Y,
```

```math
M(t)=
\begin{pmatrix}
-2a_0+(\alpha/3-2/g^2)t&2t/g^2&-\sqrt2a_0/g\\
2t/g^2&3-2t/g^2&\sqrt2/g\\
-\sqrt2a_0/g&\sqrt2/g&\alpha/3
\end{pmatrix}.
```

The full $`F`$ equation gives the first row with **$`M`$**; the $`c,v`$ equations give the remaining rows with **$`tM`$**. The correct characteristic factor is therefore

```math
t^2\det M(t)
=-\frac{2\alpha^2}{9g^2}t^2
\left[(t-\nu^2)^2-2g^2\nu^2\right]
```

It is incorrect to write only $`F=dA`$, vary with respect to $`A`$, and generate an extra $`t`$ root.

Additional roots and field directions:

```math
\boxed{
t_\sigma=\frac{g^2}{2}(\rho^2+2\sigma\rho),\qquad
\begin{pmatrix}A\\c\\v\end{pmatrix}_{\!\sigma}
=
\begin{pmatrix}
1-\sigma\rho\\
-\sigma\rho\\
-\dfrac g{\sqrt2}(\rho^2-\sigma\rho)
\end{pmatrix}Z_\sigma,\qquad \sigma=\pm1 .
}
```

Direct check:

```math
\left[(t_\sigma-\nu^2)^2-2g^2\nu^2\right]
=(\sigma g^2\rho)^2-g^4\rho^2=0,
\qquad
M(t_\sigma)Y_\sigma=0.
```

The null-vector equality applies to all three rows with the same symbolic coupling and background relations.


For the two Maxwell modes, at generic $`a_0\neq0`$,

```math
A_0=-\frac{v_0}{\sqrt2g},\qquad
u_0=c_0+\frac{\sqrt2}{3g}v_0,\qquad
tu_0=tv_0=0.
```

At $`\alpha g^2=6`$, singular steps of this decomposition are not used.
For the two real internal components of $`v'_\mu{}^{ij}`$,

```math
\left(t+\frac3\alpha\right)v'_\mu{}^{ij}=0.
```

<a id="103-gravitinospinor-decomposition"></a>

### Gravitino–spinor decomposition

$`X:=\mathcal X=\chi^{(1)}`$ is the physical combination of the dependent spinor:

```math
X=\frac1{32}
\left(\gamma^{ab}\nabla_a\Psi_b
-4m\gamma^a\Psi_a+4g\zeta\right).
```

```math
\zeta_{\rm s}
=\zeta+\frac{64\alpha m}{3g}\mathord{\not{\nabla}} X
-\frac{8\alpha g}{3}X,
```

```math
\widehat\Psi_a
=\Psi_a-\gamma_a
\left[\frac{4m}{3g}\zeta
+\frac{8\alpha}{9}(\mathord{\not{\nabla}}-m)X\right].
```

These transformations do not set mixing terms to zero at the outset. They separate physical spins after using the full coupled equations:

```math
(\mathord{\not{\nabla}}+m)\zeta_{\rm s}=0,
\qquad
[(\mathord{\not{\nabla}}+m)^2-\nu^2]X=0,
```

```math
P_{3/2}(\mathord{\not{\nabla}})\widehat\Psi^{TT}=0,\qquad
P_{3/2}(z)=-\frac\alpha3(z+3m)[(z-m)^2-\nu^2].
```

The relevant components satisfy

```math
\gamma^a\widehat\Psi_a^{TT}=0,\qquad
\nabla^a\widehat\Psi_a^{TT}=0
```

these constraints. They do not remove the total $`\Psi`$ or $`\zeta`$.

Root labels:

```math
\begin{array}{c|c}
\text{branch}&\mathord{\not{\nabla}}\text{ eigenvalue}\\ \hline
\widehat\Psi_0&-3m\\
\widehat\Psi_\sigma&(1+2\sigma\rho)m\\
\zeta_{\rm s}&-m\\
X_\sigma&-(1+2\sigma\rho)m
\end{array}
```

The pure $`X`$ solution ($`\widehat\Psi=\zeta_{\rm s}=0`$) is represented in the original fermions by

```math
\zeta=\left(\frac{8\alpha g}{3}
-\frac{64\alpha m}{3g}\mathord{\not{\nabla}}\right)X,\qquad
\Psi_a=\gamma_a\,\frac{8\alpha}{3}(m-\mathord{\not{\nabla}})X
```

On $`X_\sigma`$, these become

```math
\zeta=\frac{16\alpha g}{3}(1+\sigma\rho)X_\sigma,
\qquad
\Psi_a=\gamma_a\frac{16\alpha m}{3}(1+\sigma\rho)X_\sigma
```

Thus the spin-$`1/2`$ branch is retained with its actual mixing between the compensator and gravitino trace.

<a id="bolum-11"></a>

