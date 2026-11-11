# LOG: fermionic spectrum on AdS5

[Notation dictionary](../notation.md).

[Reading guide](README.md). The equation labels and local symbols below follow the action conventions specified for this theory.

## Fermionic roots and signed masses

Define

```math
D:=\gamma^a\bar\nabla_a,\qquad t:=igM,\qquad
t^2=\frac{g^2L_0^2}{2},\qquad J:=t^{-1}D
\tag{M-15}
```

Let $`z`$ denote an eigenvalue of $`J`$. The gauge- and constraint-reduced characteristic equations are

```math
\left(z+\frac32\right)
\left[4(L_0-1)(z^2-z)+3L_0-9\right]=0
\quad\text{(spin-$\tfrac32$)},
\tag{M-16}
```

```math
(2z+1)
\left[4(L_0-1)(z^2+z)+3L_0-9\right]=0
\quad\text{(spin-$\tfrac12$)}
\tag{M-17}
```


Temporarily put

```math
\Delta:=\sqrt{\frac{2(4-L_0)}{L_0-1}}
```

Then

```math
z^2-z+\frac{3(L_0-3)}{4(L_0-1)}
=\left(z-\frac{1+\Delta}{2}\right)
 \left(z-\frac{1-\Delta}{2}\right),
```

```math
z^2+z+\frac{3(L_0-3)}{4(L_0-1)}
=\left(z-\frac{-1+\Delta}{2}\right)
 \left(z-\frac{-1-\Delta}{2}\right).
\tag{M-18}
```

The first-order equations and squared Dirac masses are listed below.

| Channel | First-order wave equation | $`m_D^2`$ | Polarizations |
|---|---|---:|---:|
| $`\Psi_0^{TT}`$ | $`(D+\frac32igM)\Psi_0^{TT}=0`$ | $`\frac{9g^2L_0^2}{8}`$ | $`8`$ |
| $`\Psi_+^{TT}`$ | $`\displaystyle\left[D-\frac{igM}{2}\left(1+\sqrt{\frac{2(4-L_0)}{L_0-1}}\right)\right]\Psi_+^{TT}=0`$ | $`\displaystyle\frac{g^2L_0^2}{8}\left(1+\sqrt{\frac{2(4-L_0)}{L_0-1}}\right)^2`$ | $`12`$ |
| $`\Psi_-^{TT}`$ | $`\displaystyle\left[D-\frac{igM}{2}\left(1-\sqrt{\frac{2(4-L_0)}{L_0-1}}\right)\right]\Psi_-^{TT}=0`$ | $`\displaystyle\frac{g^2L_0^2}{8}\left(1-\sqrt{\frac{2(4-L_0)}{L_0-1}}\right)^2`$ | $`12`$ |
| $`\chi`$ | $`(D+\frac12igM)\chi=0`$ | $`\frac{g^2L_0^2}{8}`$ | $`4`$ |
| $`\rho_+`$ | $`\displaystyle\left[D-\frac{igM}{2}\left(-1+\sqrt{\frac{2(4-L_0)}{L_0-1}}\right)\right]\rho_+=0`$ | $`\displaystyle\frac{g^2L_0^2}{8}\left(-1+\sqrt{\frac{2(4-L_0)}{L_0-1}}\right)^2`$ | $`4`$ |
| $`\rho_-`$ | $`\displaystyle\left[D-\frac{igM}{2}\left(-1-\sqrt{\frac{2(4-L_0)}{L_0-1}}\right)\right]\rho_-=0`$ | $`\displaystyle\frac{g^2L_0^2}{8}\left(-1-\sqrt{\frac{2(4-L_0)}{L_0-1}}\right)^2`$ | $`4`$ |

The signed mass is also fixed. On an internal eigenspace of $`t`$,

```math
tX_\sigma=\frac{\sigma}{\ell_{\rm AdS}}X_\sigma,\qquad \sigma=\pm1,
```

the equation $`JX=zX`$ means

```math
(D-m_{D,\sigma})X_\sigma=0,\qquad
\boxed{m_{D,\sigma}=\frac{\sigma z}{\ell_{\rm AdS}}}
\tag{M-19}
```

The two internal eigenspaces are related by symplectic-Majorana reality and do not double the listed multiplicities.

The massless AdS gravitino has nonzero Dirac mass; gauge masslessness occurs at

```math
m_D^2=\frac{9}{4\ell_{\rm AdS}^2}
\tag{M-20}
```

the displayed value.

The curvature commutator gives the second-order equations:

```math
D^2\chi=(\bar\Box-5k)\chi,\qquad
D^2\Psi_a^{TT}=(\bar\Box-6k)\Psi_a^{TT}.
\tag{M-21}
```

Therefore

```math
\boxed{
\begin{aligned}
&(\bar\Box-6k-m_D^2)\Psi_a^{TT}=0,
&&\gamma^a\Psi_a^{TT}=0,\quad\bar\nabla^a\Psi_a^{TT}=0,\\
&(\bar\Box-5k-m_D^2)\chi=0,\qquad
(\bar\Box-5k-m_D^2)\rho_\pm=0.
\end{aligned}}
\tag{M-22}
```

Squaring loses the signed root, so these equations must be used together with the first-order equations.

For explicit fermionic eigenvectors define

```math
P_{1/2}(J):=4(L_0-1)(J^2+J)+3L_0-9
```

The mixed system is solved by

```math
\chi=\frac{g}{6(4-L_0)}t^{-1}P_{1/2}(J)\zeta,\qquad
\rho=\frac14\left(gt^{-1}\zeta+3\chi\right),
\tag{M-23}
```

```math
\rho_\pm=
\frac{J-(-1\mp\Delta)/2}{\pm\Delta}\rho,\qquad
\rho=\rho_++\rho_-
\tag{M-24}
```

The original fermions are reconstructed as

```math
\boxed{
\begin{aligned}
\zeta&=\frac tg(4\rho_++4\rho_--3\chi),\\
\Psi_a&=\Psi_{0a}^{TT}+\Psi_{+a}^{TT}+\Psi_{-a}^{TT}
+\gamma_a(\rho_++\rho_--\chi)
+\left(\bar\nabla_a+\frac t2\gamma_a\right)\epsilon
\end{aligned}}
\tag{M-25}
```

The TT root projectors are

```math
\Psi_r^{TT}
=\prod_{\substack{s\in\{-3/2,(1+\Delta)/2,(1-\Delta)/2\}\\s\ne r}}
\frac{J-s}{r-s}\,\Psi^{TT}
\tag{M-26}
```

as displayed.

Each root is simple within its generic sector. The two Maxwell and two traceless-vector channels have the separately indicated field multiplicities. The total local count is

```math
N_B=(5+9)+1+1+(3+3+4+4)+8+6=44,
```

```math
\boxed{N_F=8+12+12+4+4+4=44.}
\tag{M-27}
```

