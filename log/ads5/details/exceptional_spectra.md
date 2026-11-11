# Critical roots and endpoint spectrum

[Reading guide](../README.md). The equation labels and local symbols below follow the action conventions specified for this theory.

## Critical root merger

The double-root condition gives

```math
4-3L_0=0
\quad\Longrightarrow\quad
L_0=\frac43,\qquad \alpha g^2=\frac32
\tag{M-28}
```

The gauge rank does not change here; generalized solutions remain.

The bosonic masses are

```math
\begin{array}{c|c}
\text{Channel}&m^2\\ \hline
\text{TT metric}&0\ \text{(double root)}\\
\phi_0&-32g^2/9\\
\phi_M&0\\
w^{ij}\ \text{(two channels)}&8g^2/3\\
H_c&32g^2/9\\
\text{vector--form block}&0\ \text{(three algebraic roots)},\quad64g^2/9
\end{array}
\tag{M-29}
```

as displayed.

For the metric,

```math
(\bar\Box-2k)^2h^{TT}=0
```

the solution chain is

```math
(\bar\Box-2k)h_1=h_0,\qquad
(\bar\Box-2k)h_0=0
\tag{M-30}
```

It is not two independent Einstein gravitons: the common diffeomorphism quotient is taken once.

The three zero roots in the vector block comprise a simple Maxwell channel and a length-two chain. With $`\mathfrak M_1=\bar\Box-4k`$,

```math
\begin{pmatrix}c\\v\\a\end{pmatrix}
=
\begin{pmatrix}1\\0\\1/2\end{pmatrix}A_0
+
\begin{pmatrix}4\\8\sqrt2g/3\\1\end{pmatrix}A_M
+
\begin{pmatrix}-4\\8\sqrt2g\\1\end{pmatrix}W_1
+
\begin{pmatrix}0\\0\\-27/(32g^2)\end{pmatrix}W_0,
\tag{M-31}
```

```math
\mathfrak M_1A_0=0,\qquad
\left(\mathfrak M_1-\frac{64g^2}{9}\right)A_M=0,
```

```math
\mathfrak M_1W_1=W_0,\qquad
\mathfrak M_1W_0=0,\qquad
p_{\rm chain}=-\frac2gW_0.
\tag{M-32}
```

Since $`W_0`$ is invariant, no new Maxwell quotient is applied to it.

The fermionic roots and algebraic multiplicities are

```math
\begin{array}{c|c|c}
\text{Representation}&z\ \text{and algebraic multiplicity}&m_D^2\\ \hline
3/2&-3/2\ \text{(double)}&2g^2\\
3/2&5/2\ \text{(simple)}&50g^2/9\\
1/2&-1/2\ \text{(simple)}&2g^2/9\\
1/2&3/2\ \text{(simple)}&2g^2\\
1/2&-5/2\ \text{(simple)}&50g^2/9
\end{array}
\tag{M-33}
```

The double gravitino root is retained as

```math
(D+3t/2)\Psi_1^{TT}=\Psi_0^{TT},\qquad
(D+3t/2)\Psi_0^{TT}=0
\tag{M-34}
```

The remaining gravitino satisfies

```math
(D-5t/2)\Psi_M^{TT}=0,\qquad
\Psi_M^{TT}=\frac{(J+3/2)^2}{16}\Psi^{TT}
\tag{M-35}
```

the displayed simple-root equation.

The ordinary/generalized metric chain carries $`5+9`$ polarizations, the gravitino chain $`8+12`$, and the vector chain $`3+4`$. Hence

```math
\boxed{N_B=N_F=44\qquad(\alpha g^2=3/2)}
\tag{M-36}
```

The count would change if the generalized pieces were discarded.

## Endpoint with additional gauge directions

The rank-changing endpoint is

```math
L_0-2=0
\quad\Longrightarrow\quad
L_0=2,\qquad \alpha g^2=2,\qquad k=-2g^2
\tag{M-37}
```

Simply substituting into the generic mass table is insufficient.

The scalar equation gives

```math
n=\frac{r}{8g}-gl
\tag{M-38}
```

and the additional directions are

```math
\delta l=\sigma,\quad\delta n=-g\sigma,
```

```math
\delta h_{\mu\nu}=2\omega\bar g_{\mu\nu},\quad
\delta n=-\frac1g(\bar\Box+5k)\omega
\tag{M-39}
```

so no independent propagating scalar remains.

The surviving bosonic modes are listed below.

| Channel | $`m^2`$ | Wave equation | Polarizations |
|---|---:|---|---:|
| Massless graviton | $`0`$ | $`(\bar\Box+4g^2)h_0^{TT}=0`$ | $`5`$ |
| Partially massless graviton | $`-6g^2=3k`$ | $`(\bar\Box+10g^2)h_{\rm PM}^{TT}=0`$ | $`8`$ |
| Two $`w^{ij}`$ Maxwell channels | $`0`$ | $`(\bar\Box+8g^2)w^{ij,T}=0`$ | $`6`$ |
| Mixed Maxwell channel $`v_0`$ | $`0`$ | $`(\bar\Box+8g^2)v_0^T=0`$ | $`3`$ |
| Mixed vector $`p'`$ | $`-2g^2`$ | $`(\bar\Box+10g^2)p'=0,\ \bar\nabla\cdot p'=0`$ | $`4`$ |
| Closed $`H'_c`$ | $`2g^2`$ | $`(\bar\Box+10g^2)H'_c=0,\ dH'_c=0`$ | $`6`$ |

The partially massless spin-two scalar gauge direction is

```math
\delta h_{\mu\nu}^{\rm PM}
=(\bar\nabla_\mu\bar\nabla_\nu+k\bar g_{\mu\nu})\sigma
\tag{M-40}
```

and removes one of the nine massive spin-two polarizations.

The vector–form combinations obey

```math
\mathcal H'^{abc}
=\mathcal H^{abc}-\frac12\varepsilon^{deabc}\mathcal G_{de},
\qquad a'=a-\frac12c,
```

```math
v=v_0+\frac{p'}{\sqrt2},\qquad
a'=\frac{v_0}{4\sqrt2g}+\frac{p'}{4g}.
\tag{M-41}
```

The reduced characteristic equation is

```math
x(x+2g^2)=0
\tag{M-42}
```

The apparent generic $`+6g^2`$ root is absent after the enlarged gauge quotient and is not a physical channel at this endpoint.

Use the additional fermionic gauge symmetry

```math
\delta\Psi_a=\gamma_a\theta,\qquad
\delta\zeta=-\frac1g(D-5t/2)\theta
\tag{M-43}
```

and invariant combination

```math
\eta=\zeta+\frac1g(D-5t/2)u,\qquad
\Psi_a^{(1/2)}=\gamma_a u
\tag{M-44}
```

The surviving fermions are listed below.

| Channel | First-order equation | $`m_D^2`$ | Second-order equation | Polarizations |
|---|---|---:|---|---:|
| $`\Psi_{-3/2}^{TT}`$ | $`(D+3t/2)\Psi=0`$ | $`9g^2/2`$ | $`(\bar\Box+15g^2/2)\Psi=0`$ | $`8`$ |
| $`\Psi_{+3/2}^{TT}`$ | $`(D-3t/2)\Psi=0`$ | $`9g^2/2`$ | $`(\bar\Box+15g^2/2)\Psi=0`$ | $`8`$ |
| $`\Psi_{-1/2}^{TT}`$ | $`(D+t/2)\Psi=0`$ | $`g^2/2`$ | $`(\bar\Box+23g^2/2)\Psi=0`$ | $`12`$ |
| $`\eta`$ | $`(D-t/2)\eta=0`$ | $`g^2/2`$ | $`(\bar\Box+19g^2/2)\eta=0`$ | $`4`$ |

The first two gravitini share a squared mass but have different signed first-order roots; both are gauge massless and must remain distinct. The count is

```math
\boxed{
N_B=5+8+6+3+4+6=32,\qquad
N_F=8+8+12+4=32
\quad(\alpha g^2=2).
}
\tag{M-45}
```

On the selected $`\alpha<0`$ branch, $`0<L_0<1`$ and

```math
\frac{2(4-L_0)}{L_0-1}<0.
```

Complex-conjugate roots are kept together in the real field system. The points $`L_0=2/5`$ and $`22/19`$ do not reduce the physical polynomial degree or remove modes.

All finite-$`\alpha`$ channels, signed fermionic roots, and generalized critical solutions are retained. These are local bulk counts, not multiplicities of a fully specified global normal-mode space.

