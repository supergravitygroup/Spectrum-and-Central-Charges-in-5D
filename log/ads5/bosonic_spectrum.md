# LOG: bosonic spectrum on AdS5

[Notation dictionary](../notation.md).

[Reading guide](README.md). The equation labels and local symbols below follow the action conventions specified for this theory.

<a id="11-all-physical-masses-and-wave-equations"></a>

## All physical masses and wave equations

Retain the exact branch dependence

```math
L_0=\frac{2}{1+\sqrt{1-\alpha g^2/2}},\qquad
k=-\frac{g^2L_0^2}{2},\qquad
\ell_{\mathrm{AdS}}^{-2}=-k,
```

```math
\alpha g^2L_0^2=8(L_0-1),\qquad
0<L_0\le2,\quad L_0\ne1
\tag{M-1}
```

as displayed.

Separate physical mass parameters from curvature shifts by defining

```math
\begin{aligned}
&(\bar\Box-2k-m_2^2)h_{\mu\nu}^{TT}=0,\\
&(\bar\Box-m_0^2)\phi=0,\\
&(\bar\Box-4k-m_1^2)A_\mu^{T}=0,\\
&(\bar\Box-6k-m_H^2)H_c=0,\qquad dH_c=0
\end{aligned}
\tag{M-2}
```

Thus an eigenvalue of $`\bar\Box`$ is not confused with a mass parameter.

First consider $`L_0\ne4/3,2`$.

The bosonic characteristic equations are

```math
\begin{aligned}
&x\left[x-\frac{6(4-3L_0)}{\alpha}\right]=0
&&\text{(spin-2)},\\
&\left[x+2g^2L_0^2\right]
 \left[x-\frac{6(4-3L_0)}{\alpha}\right]=0
&&\text{(scalar)},\\
&x-\frac{6(2-L_0)}{\alpha}=0
&&\text{(two traceless internal vectors)},\\
&x-\frac{2(4-L_0)}{\alpha}=0
&&\text{(closed three-form)}
\end{aligned}
\tag{M-3}
```

Here $`x`$ denotes the eigenvalue of $`\bar\Box-2k`$, $`\bar\Box`$, $`\bar\Box-4k`$, or $`\bar\Box-6k`$ in the respective sector.

With the undifferentiated form constraint retained, the mixed vector–form polynomial is

```math
x^2P_V(x)=0,
```

```math
\begin{aligned}
P_V(x)={}&16(L_0-1)^2x^2
+8L_0^2g^2(L_0-1)(L_0-4)x\\
&+3L_0^4g^4(L_0-4)(3L_0-4).
\end{aligned}
\tag{M-4}
```

The two zero roots are two Maxwell channels. The other roots have sum and product

```math
\lambda_++\lambda_-=
\frac{g^2L_0^2(4-L_0)}{2(L_0-1)},
```

```math
\lambda_+\lambda_-=
\frac{3g^4L_0^4(L_0-4)(3L_0-4)}
     {16(L_0-1)^2}
```

and hence

```math
\boxed{
\lambda_\pm=
\frac{g^2L_0^2}{2}
\left[
\frac{4-L_0}{2(L_0-1)}
\pm\sqrt{\frac{2(4-L_0)}{L_0-1}}
\right].
}
\tag{M-5}
```

The following table lists every bosonic mass and wave equation. The last column counts local real polarizations after gauge and constraints.

| Field channel | $`m^2`$ | Wave equation and constraint | Multiplicity / polarizations |
|---|---:|---|---:|
| $`h_0^{TT}`$ | $`0`$ | $`(\bar\Box-2k)h_0^{TT}=0`$ | $`1 / 5`$ |
| $`h_M^{TT}`$ | $`\displaystyle\frac{6(4-3L_0)}{\alpha}`$ | $`(\bar\Box-2k-m_2^2)h_M^{TT}=0`$ | $`1 / 9`$ |
| $`\phi_0`$ | $`-2g^2L_0^2`$ | $`(\bar\Box+2g^2L_0^2)\phi_0=0`$ | $`1 / 1`$ |
| $`\phi_M`$ | $`\displaystyle\frac{6(4-3L_0)}{\alpha}`$ | $`(\bar\Box-m_0^2)\phi_M=0`$ | $`1 / 1`$ |
| $`c_0,v_0`$ | $`0`$ | $`(\bar\Box-4k)A^T=0`$, Maxwell gauge quotient | $`2 / 6`$ |
| $`p_+`$ | $`\lambda_+`$ | $`(\bar\Box-4k-\lambda_+)p_+=0,\ \bar\nabla\cdot p_+=0`$ | $`1 / 4`$ |
| $`p_-`$ | $`\lambda_-`$ | $`(\bar\Box-4k-\lambda_-)p_-=0,\ \bar\nabla\cdot p_-=0`$ | $`1 / 4`$ |
| $`w^{ij}`$, traceless | $`\displaystyle\frac{6(2-L_0)}{\alpha}`$ | $`(\bar\Box-4k-m_w^2)w^{ij}=0,\ \bar\nabla\cdot w^{ij}=0`$ | $`2 / 8`$ |
| $`H_c`$ | $`\displaystyle\frac{2(4-L_0)}{\alpha}`$ | $`(\bar\Box-6k-m_H^2)H_c=0,\ dH_c=0`$ | $`1 / 6`$ |

The field $`H_c`$ is an invariant closed three-form, not an unconstrained independent three-form potential. Closure leaves $`\binom42=6`$ polarizations.

Keep eigenvectors as well as masses. The scalar combinations are

```math
\phi_0=\frac ng+\frac32L_0l,\qquad
\phi_M=\frac ng+2L_0l,
```

```math
l=\frac2{L_0}(\phi_M-\phi_0),\qquad
n=g(4\phi_0-3\phi_M).
\tag{M-6}
```

Metric reconstruction uses

```math
h_{\mu\nu}
=h_{0,\mu\nu}^{TT}+h_{M,\mu\nu}^{TT}
+\frac{\bar g_{\mu\nu}}{L_0^2}
 \left(\frac43\phi_0-\phi_M\right)
+2\bar\nabla_{(\mu}\xi_{\nu)}
\tag{M-7}
```

With $`\mu=6(4-3L_0)/\alpha`$,

```math
h_M^{TT}=\frac{\bar\Box-2k}{\mu}h^{TT},
\qquad h_0^{TT}=h^{TT}-h_M^{TT}.
\tag{M-8}
```

For vector–form reconstruction write

```math
\mathcal H^{abc}=H_c^{abc}
+\varepsilon^{deabc}(da)_{de},\qquad
p=-\frac2g(\bar\Box-4k)a
\tag{M-9}
```

The field $`a`$ is a representative potential, not an additional independent variable. The massive projectors are

```math
p_\pm=
\frac{\bar\Box-4k-\lambda_\mp}{\lambda_\pm-\lambda_\mp}p
\tag{M-10}
```

For each root define

```math
\begin{aligned}
C_\lambda&=4(4-L_0)+2\alpha\lambda,\\
A_\lambda&=2(5L_0-8)+\alpha\lambda,\\
V_\lambda&=-\frac{gL_0}{\sqrt2}C_\lambda
-\frac{gL_0(L_0-4)}{\sqrt2(L_0-1)}A_\lambda
\end{aligned}
\tag{M-11}
```

so that

```math
a_\pm=-\frac{g}{2\lambda_\pm}p_\pm,\qquad
c_\pm=\frac{C_{\lambda_\pm}}{A_{\lambda_\pm}}a_\pm,\qquad
v_\pm=\frac{V_{\lambda_\pm}}{A_{\lambda_\pm}}a_\pm.
\tag{M-12}
```

The complete reconstruction is

```math
\begin{aligned}
c&=c_0+c_++c_-,\\
v&=v_0+v_++v_-,\\
a&=\frac12c_0+\frac{v_0}{2\sqrt2gL_0}+a_++a_-
\end{aligned}
\tag{M-13}
```

A massive $`p_\pm`$ mode therefore generally excites $`c,v`$, and $`\mathcal H`$ simultaneously.

The denominators are checked explicitly:

```math
P_V\!\left(-\frac{2(5L_0-8)}{\alpha}\right)
=24L_0^4g^4(L_0-2)(L_0-1).
\tag{M-14}
```

Thus $`P_V(\lambda)=0`$ and $`A_\lambda=0`$ cannot coincide in the selected generic region.

