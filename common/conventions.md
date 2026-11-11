# Notation and conventions

This section fixes geometric, Clifford, and spinor notation and covariant-derivative conventions. It follows the [recorded project conventions](details/source_conventions.md). Derivations of the algebraic identities used are in the [symbolic-check appendix](details/convention_conversions.md), while sources and verification scope are listed in the [section record](../references/convention_sources.md).

<a id="1-dimension-indices-and-vielbein"></a>

## Dimension, indices, and vielbein

Spacetime is five-dimensional, with a mostly-plus tangent-space metric:

```math
D_{\mathrm{spacetime}}=5,
\qquad
\eta_{ab}=\mathop{\mathrm{diag}}\nolimits(-,+,+,+,+).
```

The symbols $`\mu,\nu,\ldots=0,\ldots,4`$ denote coordinate indices, $`a,b,\ldots=0,\ldots,4`$ tangent indices, and $`i,j,\ldots=1,2`$ internal $`SU(2)`$ indices. The symbol $`D_{\mathrm{spacetime}}`$ must not be confused with the scalar field $`D`$.

For the vielbein $`e_\mu{}^a`$ and its inverse $`e_a{}^\mu`$,

```math
e_\mu{}^a e_a{}^\nu=\delta_\mu{}^\nu,
\qquad
e_a{}^\mu e_\mu{}^b=\delta_a{}^b,
\qquad
g_{\mu\nu}=e_\mu{}^a e_\nu{}^b\eta_{ab}.
```

Coordinate indices are raised and lowered with $`g_{\mu\nu}`$, and tangent indices with $`\eta_{ab}`$. For example,

```math
X_a=e_a{}^\mu X_\mu,
\qquad
X^a=e_\mu{}^a X^\mu,
\qquad
X_{a_1\ldots a_p}
=e_{a_1}{}^{\mu_1}\cdots e_{a_p}{}^{\mu_p}
 X_{\mu_1\ldots\mu_p}.
```

The same vielbein is used in every tensor and Clifford expression.

<a id="2-volume-element-and-lagrangian-density"></a>

## Volume element and Lagrangian density

The symbol $`\det g_{\mu\nu}`$ denotes the metric determinant, written explicitly to avoid confusion with the coupling $`g`$. With the source vielbein orientation,

```math
e:=\det(e_\mu{}^a)>0,
\qquad
\det g_{\mu\nu}=-e^2,
\qquad
e=\sqrt{-\det g_{\mu\nu}}.
```

The positive-determinant branch is the condition underlying the source identity $`e=\det(e_\mu{}^a)=\sqrt{-\det g_{\mu\nu}}`$. No additional numerical orientation sign is assigned to the epsilon component $`01234`$.

The symbol $`\mathcal L`$ denotes the Lagrangian density, and $`e^{-1}\mathcal L`$ the scalar Lagrangian:

```math
S=\int d^5x\,\mathcal L
 =\int d^5x\,e\,(e^{-1}\mathcal L).
```

This notation selects neither a bosonic nor a fixed-derivative sector and changes no action normalization.

<a id="3-symmetrization-antisymmetrization-and-epsilon"></a>

## Symmetrization, antisymmetrization, and epsilon

Round and square brackets have unit weight:

```math
X_{(ab)}=\frac12(X_{ab}+X_{ba}),
\qquad
X_{[ab]}=\frac12(X_{ab}-X_{ba}).
```

More generally, with $`S_p`$ the set of all permutations of $`p`$ indices,

```math
X_{[a_1\ldots a_p]}
=\frac1{p!}\sum_{\pi\in S_p}\mathop{\mathrm{sgn}}\nolimits(\pi)
 X_{a_{\pi(1)}\ldots a_{\pi(p)}}.
```

Vertical bars exclude the enclosed index from antisymmetrization; for example,

```math
A_{[a|c|b]}=\frac12(A_{acb}-A_{bca}).
```

For the real epsilon tensor, with $`n+p=5`$,

```math
\varepsilon_{a_1\ldots a_n b_1\ldots b_p}
\varepsilon^{a_1\ldots a_n c_1\ldots c_p}
=-n!p!\,\delta_{[b_1}^{c_1}\cdots\delta_{b_p]}^{c_p}.
```

The minus sign comes from Lorentzian signature. Either epsilon orientation gives the same contraction.

The coordinate epsilon tensor and density symbol are defined respectively by

```math
\varepsilon^{\mu\nu\rho\sigma\lambda}
=e_a{}^\mu e_b{}^\nu e_c{}^\rho e_d{}^\sigma e_f{}^\lambda
 \varepsilon^{abcdf},
\qquad
\epsilon^{\mu\nu\rho\sigma\lambda}
=e\,\varepsilon^{\mu\nu\rho\sigma\lambda}
```

Consequently,

```math
\varepsilon^{\mu\nu\rho\sigma\lambda}X_{\mu\nu\rho\sigma\lambda}
=e^{-1}\epsilon^{\mu\nu\rho\sigma\lambda}
 X_{\mu\nu\rho\sigma\lambda}.
```

Expressions involving the density symbol retain the factor $`e^{-1}`$.

<a id="4-clifford-algebra-and-gamma-duality"></a>

## Clifford algebra and gamma duality

The tangent gamma matrices satisfy

```math
\{\gamma^a,\gamma^b\}=2\eta^{ab}\mathbf1,
\qquad
\gamma^{a_1\ldots a_r}
=\gamma^{[a_1}\cdots\gamma^{a_r]},
\qquad
\gamma^{(0)}=\mathbf1
```

These relations define the algebra. Repeated tangent indices are contracted with the metric. Coordinate gamma matrices are fixed by

```math
\gamma_\mu=e_\mu{}^a\gamma_a,
\qquad
\gamma^\mu=e_a{}^\mu\gamma^a,
\qquad
\{\gamma_\mu,\gamma_\nu\}=2g_{\mu\nu}\mathbf1
```

which defines the coordinate representation.

The highest-rank convention is

```math
\gamma^{abcdf}=i\varepsilon^{abcdf}\mathbf1
```

Together with the Clifford algebra, this gives, for $`0\leq r\leq5`$,

```math
\gamma^{a_1\ldots a_r}
=\frac{i}{(5-r)!}\varepsilon^{a_1\ldots a_r b_1\ldots b_{5-r}}
 \gamma_{b_{5-r}\ldots b_1}
```

The gamma indices on the right are reversed. Reordering them into increasing order gives the equivalent identity

```math
\gamma^{a_1\ldots a_r}
=\frac{i(-1)^{(5-r)(4-r)/2}}{(5-r)!}
 \varepsilon^{a_1\ldots a_r b_1\ldots b_{5-r}}
 \gamma_{b_1\ldots b_{5-r}}
```

In particular,

```math
\begin{aligned}
\gamma^a&=\frac{i}{24}\varepsilon^{abcdf}\gamma_{bcdf},\\
\gamma^{ab}&=-\frac{i}{6}\varepsilon^{abcdf}\gamma_{cdf},\\
\gamma^{abc}&=-\frac{i}{2}\varepsilon^{abcdf}\gamma_{df},\\
\gamma^{abcd}&=i\varepsilon^{abcdf}\gamma_f.
\end{aligned}
```

Dot and slash notation denote complete contractions:

```math
\gamma\!\cdot\!X
=\gamma^{a_1\ldots a_p}X_{a_1\ldots a_p},
\qquad
\mathord{\not{X}}=\gamma^aX_a,
\qquad
\mathord{\not{\mathcal D}}=\gamma^a\mathcal D_a.
```

No extra factor $`1/p!`$ is included in the definition of $`\gamma\!\cdot\!X`$.

<a id="5-internal-indices-and-grassmann-signs"></a>

## Internal indices and Grassmann signs

Internal indices follow the NW–SE convention:

```math
\epsilon_{12}=\epsilon^{12}=1,
\qquad
\epsilon_{ij}=-\epsilon_{ji},
\qquad
X^i=\epsilon^{ij}X_j,
\qquad
X_i=X^j\epsilon_{ji}.
```

With these definitions,

```math
\epsilon^{ij}\epsilon_{kj}=\delta^i{}_k,
\qquad
\epsilon^{ij}\epsilon_{jk}=-\delta^i{}_k.
```

The internal epsilon $`\epsilon_{ij}`$, spacetime epsilon tensor $`\varepsilon_{abcdf}`$, and density symbol $`\epsilon^{\mu\nu\rho\sigma\lambda}`$ are distinct objects.

For a tensor with two internal indices,

```math
L^{ij}=\epsilon^{ik}\epsilon^{j\ell}L_{k\ell},
\qquad
L_i{}^j=\epsilon^{jk}L_{ik},
\qquad
L^i{}_j=\epsilon^{ik}L_{kj}.
```

The spinor contraction is defined by

```math
\bar X\Gamma Y:=\bar X^i\Gamma Y_i
```

where $`\Gamma`$ is a Clifford matrix or product. Interchanging internal-index positions produces

```math
\bar X^i\Gamma Y_i=-\bar X_i\Gamma Y^i
```

with the indicated sign. Spinor product order is unchanged in this identity.

The following interchange rule is the source pairing convention for Grassmann-odd spinors. The symbol $`\gamma_{(n)}`$ denotes a rank-$`n`$ antisymmetric gamma matrix with Lorentz indices suppressed:

```math
\bar X^i\gamma_{(n)}Y^j
=t_n\bar Y^j\gamma_{(n)}X^i,
\qquad
(t_0,t_1,t_2,t_3,t_4,t_5)=(+1,+1,-1,-1,+1,+1).
```

The choices $`t_0=t_1=+1`$ define the basic pairing. Relative signs at other ranks agree with reversal of Clifford-product order and gamma duality. Applying NW–SE contraction gives

```math
\begin{aligned}
\bar X^i\gamma_{(n)}Y_i
&=\epsilon_{ji}\bar X^i\gamma_{(n)}Y^j\\
&=t_n\epsilon_{ji}\bar Y^j\gamma_{(n)}X^i\\
&=-t_n\bar Y^j\gamma_{(n)}X_j.
\end{aligned}
```

Thus the open-index and contracted interchange signs are

| Gamma rank $`n`$ | Open-index $`t_n`$ | Contracted $`-t_n`$ |
|---|---:|---:|
| $`0,1,4,5`$ | $`+1`$ | $`-1`$ |
| $`2,3`$ | $`-1`$ | $`+1`$ |

This table does not apply to Grassmann-even spinors. The source does not fix an explicit charge-conjugation matrix, Dirac-adjoint phase, or complex-conjugation rules; this section introduces none.

<a id="6-derivative-notation"></a>

## Derivative notation

The symbol $`\partial_\mu`$ denotes an ordinary partial derivative, $`\nabla_\mu^{\mathrm L}`$ the Lorentz-connection action alone, and $`\mathcal D_\mu`$ the source's full supercovariant derivative. The Lorentz connection is $`\omega_\mu{}^{ab}=-\omega_\mu{}^{ba}`$. For a spinor without coordinate indices, the Lorentz derivative is

```math
\nabla_\mu^{\mathrm L}X^i
=\left(\partial_\mu+\frac14\omega_\mu{}^{ab}\gamma_{ab}\right)X^i
```

For a spinor doublet of Weyl weight $`w`$, its Lorentz, dilatation, and $`SU(2)`$ connection part is

```math
\left(\partial_\mu-wb_\mu
 +\frac14\omega_\mu{}^{ab}\gamma_{ab}\right)X^i
 -V_\mu^{ij}X_j
```

Here $`b_\mu`$ is the dilatation connection and $`V_\mu^{ij}`$ the internal-symmetry connection. This connection part alone is not the full $`\mathcal D_\mu X^i`$; supercovariant completions follow from the field's transformation rules.

The Lorentz derivative of a vector with a lower tangent index is

```math
\nabla_\mu^{\mathrm L}X_a
=\partial_\mu X_a-\omega_\mu{}^b{}_aX_b
```

so, for antisymmetric $`T_{ab}`$,

```math
\begin{aligned}
\nabla_\mu^{\mathrm L}T_{ab}
&=\partial_\mu T_{ab}
 -\omega_\mu{}^c{}_aT_{cb}
 -\omega_\mu{}^c{}_bT_{ac}\\
&=\partial_\mu T_{ab}
 +2\omega_\mu{}^c{}_{[a}T_{b]c}.
\end{aligned}
```

This sign also agrees with the spinor connection acting on Clifford products. Writing the Lorentz connection separately does not set other connections or fields to zero.

Tangent-derivative notation is

```math
\mathcal D_a:=e_a{}^\mu\mathcal D_\mu,
\qquad
\mathord{\not{\mathcal D}}:=\gamma^a\mathcal D_a
```

The full supercovariant derivative of each field used subsequently is specified separately among that calculation's inputs.

<a id="7-tensor-product-notation"></a>

## Tensor-product notation

For antisymmetric $`T_{ab}`$, the source abbreviations are defined by

```math
T^2:=T_{ab}T^{ab},
\qquad
T^4:=T_{ab}T^{bc}T_{cd}T^{da},
\qquad
(T^2)^2:=(T_{ab}T^{ab})^2
```

The quantities $`T^4`$ and $`(T^2)^2`$ denote distinct contractions and are not interchangeable.
