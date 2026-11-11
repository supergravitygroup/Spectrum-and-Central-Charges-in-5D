# Symbolic checks of notation and conventions

This appendix derives the algebraic identities used in the [notation section](../conventions.md). Its inputs are the dimension, metric, Clifford algebra, orientation, and internal-index definitions in the [recorded conventions](source_conventions.md). No numerical values are assigned to fields, couplings, or their combinations. Finite index sums are exact contractions over the specified five spacetime and two internal indices.

## A. Vielbein, metric, and density

Let $`E`$ be an invertible matrix with components $`e_\mu{}^a`$. The metric definition and specified signature give

```math
g=E\eta E^{\mathsf T},
\qquad
\det\eta=-1
```

and hence

```math
\det g
=\det E\,\det\eta\,\det E^{\mathsf T}
=-(\det E)^2.
```

Here $`g`$ denotes the metric matrix only in this matrix identity; no coupling value has been chosen. In the original notation,

```math
\sqrt{-\det g_{\mu\nu}}
=\left|\det(e_\mu{}^a)\right|.
```

Since the source uses $`\det(e_\mu{}^a)=\sqrt{-\det g_{\mu\nu}}`$, the selected branch on the invertible-vielbein patch is $`\det(e_\mu{}^a)>0`$:

```math
e=\det(e_\mu{}^a)>0
\quad\Longrightarrow\quad
e=\sqrt{-\det g_{\mu\nu}}.
```

This branch is an explicit condition of the source identity. It does not separately fix the epsilon orientation sign.

Substitution of the proposed inverse metric

```math
\begin{aligned}
g_{\mu\rho}\bigl(e_c{}^\rho e_d{}^\nu\eta^{cd}\bigr)
&=e_\mu{}^a e_\rho{}^b\eta_{ab}
  e_c{}^\rho e_d{}^\nu\eta^{cd}\\
&=e_\mu{}^a e_d{}^\nu\eta_{ab}\eta^{bd}\\
&=e_\mu{}^a e_a{}^\nu
=\delta_\mu{}^\nu
\end{aligned}
```

with

```math
g^{\mu\nu}=e_c{}^\mu e_d{}^\nu\eta^{cd}
```

verifies the result. The two representations of a vector also

```math
\begin{aligned}
e_\mu{}^aX^\mu
&=e_\mu{}^a g^{\mu\nu}X_\nu\\
&=e_\mu{}^a e_c{}^\mu e_d{}^\nu\eta^{cd}X_\nu\\
&=\eta^{ad}e_d{}^\nu X_\nu
=\eta^{ad}X_d=X^a
\end{aligned}
```

agree with this identity. In Lagrangian notation, assuming $`e\ne0`$,

```math
e\,(e^{-1}\mathcal L)=\mathcal L,
\qquad
\int d^5x\,e\,(e^{-1}\mathcal L)
=\int d^5x\,\mathcal L.
```

This operation does not use any field equation.

## B. Antisymmetrization weight

Let $`P_-`$ denote antisymmetrization of a rank-$`p`$ tensor. By definition,

```math
(P_-X)_{a_1\ldots a_p}
=\frac1{p!}\sum_{\pi\in S_p}\mathop{\mathrm{sgn}}\nolimits(\pi)
 X_{a_{\pi(1)}\ldots a_{\pi(p)}}
```

and each composite permutation $`\rho\in S_p`$ corresponds to $`p!`$ distinct pairs $`(\pi,\sigma)`$, so

```math
\begin{aligned}
P_-^2X
&=\frac1{(p!)^2}\sum_{\pi,\sigma\in S_p}
  \mathop{\mathrm{sgn}}\nolimits(\pi)\mathop{\mathrm{sgn}}\nolimits(\sigma)
  (\pi\sigma)X\\
&=\frac{p!}{(p!)^2}\sum_{\rho\in S_p}
  \mathop{\mathrm{sgn}}\nolimits(\rho)\rho X
=P_-X.
\end{aligned}
```

Thus the weight $`1/p!`$ leaves an already antisymmetric tensor unchanged. The explicit check for $`p=2`$ is

```math
(P_-^2X)_{ab}
=\frac14(X_{ab}-X_{ba}-X_{ba}+X_{ab})
=\frac12(X_{ab}-X_{ba})
```

For the symmetric part, all permutation signs in the same expansion are positive, again yielding $`P_+^2=P_+`$.

## C. Orientation and epsilon contractions

Temporarily define

```math
s:=\varepsilon^{01234},
\qquad
\mathcal V:=\gamma^0\gamma^1\gamma^2\gamma^3\gamma^4
```

Keep $`s`$ real without choosing its sign. Anticommutation of distinct gamma matrices and the specified metric imply

```math
\begin{aligned}
\mathcal V^2
&=(-1)^{4+3+2+1}
  (\gamma^0)^2(\gamma^1)^2(\gamma^2)^2(\gamma^3)^2(\gamma^4)^2\\
&=(-1)^{10}\eta^{00}\eta^{11}\eta^{22}\eta^{33}\eta^{44}\mathbf1
=-\mathbf1
\end{aligned}
```

Comparing with the source's highest-rank convention $`\mathcal V=is\mathbf1`$ gives

```math
-s^2\mathbf1=-\mathbf1
\quad\Longrightarrow\quad
s^2=1.
```

This normalization follows from the Clifford algebra and the specified highest-rank relation. Neither branch $`s=+1`$ nor $`s=-1`$ is discarded. The operations below use only $`s^2=1`$.

Let $`(a_1,\ldots,a_5)`$ be a permutation of $`(0,1,2,3,4)`$, with permutation sign $`\mathop{\mathrm{sgn}}\nolimits(a_1\ldots a_5)`$. Then

```math
\begin{aligned}
\varepsilon^{a_1\ldots a_5}
&=s\mathop{\mathrm{sgn}}\nolimits(a_1\ldots a_5),\\
\varepsilon_{a_1\ldots a_5}
&=\eta_{a_1a_1}\cdots\eta_{a_5a_5}
  \varepsilon^{a_1\ldots a_5}
=-s\mathop{\mathrm{sgn}}\nolimits(a_1\ldots a_5).
\end{aligned}
```

There is no sum over the indices in the second line. Epsilon components with repeated indices vanish by antisymmetry. Using $`s^2=1`$ in the product of two rank-five epsilon tensors gives

```math
\varepsilon_{a_1\ldots a_5}\varepsilon^{c_1\ldots c_5}
=-\det\!\bigl(\delta_{a_i}^{c_j}\bigr)_{i,j=1}^{5}
=-5!\,\delta_{[a_1}^{c_1}\cdots\delta_{a_5]}^{c_5}
```

For equal index sets, the determinant is the product of the two permutation signs; with repeated indices, both sides vanish.

For $`n+p=5`$, contract the first $`n`$ indices. For fixed distinct indices $`b_1,\ldots,b_p`$, their complementary $`n`$ indices contribute in $`n!`$ orders. If $`c_1,\ldots,c_p`$ is a permutation of the same $`b`$ indices, each contribution is its permutation sign times $`-s^2`$; different index sets give no contribution. Thus

```math
\begin{aligned}
\varepsilon_{a_1\ldots a_n b_1\ldots b_p}
\varepsilon^{a_1\ldots a_n c_1\ldots c_p}
&=-n!\det\!\bigl(\delta_{b_i}^{c_j}\bigr)_{i,j=1}^{p}\\
&=-n!p!\,\delta_{[b_1}^{c_1}\cdots\delta_{b_p]}^{c_p}.
\end{aligned}
```

For example, the rank-three contraction coefficient and the complete contraction are

```math
\varepsilon_{ab cdf}\varepsilon^{ab ghi}
=-2!3!\,\delta_{[c}^{g}\delta_d^h\delta_{f]}^i,
\qquad
\varepsilon_{abcdf}\varepsilon^{abcdf}=-5!
```

These are exact index contractions fixed by the dimension, not samples of fields or parameters.

Substitution into the inverse density transformation

```math
e^{-1}\epsilon^{\mu\nu\rho\sigma\lambda}
=e^{-1}e\,\varepsilon^{\mu\nu\rho\sigma\lambda}
=\varepsilon^{\mu\nu\rho\sigma\lambda}
```

verifies the factor $`e^{-1}`$. The vielbein definition also gives

```math
\begin{aligned}
\varepsilon^{\mu\nu\rho\sigma\lambda}X_{\mu\nu\rho\sigma\lambda}
&=e_a{}^\mu e_b{}^\nu e_c{}^\rho e_d{}^\sigma e_f{}^\lambda
  \varepsilon^{abcdf}X_{\mu\nu\rho\sigma\lambda}\\
&=\varepsilon^{abcdf}X_{abcdf}
\end{aligned}
```

The final results do not require the abbreviations $`s`$ or $`\mathcal V`$.

## D. Clifford duality

First, the coordinate gamma-matrix algebra is checked by

```math
\begin{aligned}
\{\gamma_\mu,\gamma_\nu\}
&=e_\mu{}^a e_\nu{}^b\{\gamma_a,\gamma_b\}\\
&=2e_\mu{}^a e_\nu{}^b\eta_{ab}\mathbf1
=2g_{\mu\nu}\mathbf1
\end{aligned}
```

which verifies the identity.

For duality, let $`p:=5-r`$. For fixed distinct $`a_1,\ldots,a_r`$ and their ordered complement $`b_1,\ldots,b_p`$, in an orthonormal tangent frame and without summing these fixed indices,

```math
\begin{aligned}
\gamma^{a_1\ldots a_r b_1\ldots b_p}
\gamma_{b_p\ldots b_1}
&=\gamma^{a_1}\cdots\gamma^{a_r}
  \gamma^{b_1}\cdots\gamma^{b_p}
  \gamma_{b_p}\cdots\gamma_{b_1}\\
&=\gamma^{a_1}\cdots\gamma^{a_r}
  \prod_{j=1}^{p}(\eta^{b_jb_j}\eta_{b_jb_j})\\
&=\gamma^{a_1\ldots a_r}.
\end{aligned}
```

The first line contains five distinct indices inside the gamma matrices. Every permutation of the complementary indices gives the same right-hand side; there are $`p!`$ contributions. Therefore

```math
\gamma^{a_1\ldots a_r b_1\ldots b_p}
\gamma_{b_p\ldots b_1}
=p!\gamma^{a_1\ldots a_r}
```

where the indices $`b`$ are summed in the last line. Substituting the highest-rank relation gives

```math
\begin{aligned}
i\varepsilon^{a_1\ldots a_r b_1\ldots b_p}
\gamma_{b_p\ldots b_1}
&=p!\gamma^{a_1\ldots a_r},\\
\gamma^{a_1\ldots a_r}
&=\frac{i}{(5-r)!}
\varepsilon^{a_1\ldots a_r b_1\ldots b_{5-r}}
\gamma_{b_{5-r}\ldots b_1}.
\end{aligned}
```

With repeated free indices, both sides vanish by antisymmetry, so the identity holds for every component. Reversing an antisymmetric rank-$`p`$ gamma product requires $`p(p-1)/2`$ interchanges:

```math
\gamma_{b_p\ldots b_1}
=(-1)^{p(p-1)/2}\gamma_{b_1\ldots b_p}.
```

Substituting this sign gives the coefficients in the same-order gamma representation:

| $`r`$ | $`p=5-r`$ | $`(-1)^{p(p-1)/2}`$ | Coefficient |
|---|---:|---:|---:|
| $`0`$ | $`5`$ | $`+1`$ | $`i/120`$ |
| $`1`$ | $`4`$ | $`+1`$ | $`i/24`$ |
| $`2`$ | $`3`$ | $`-1`$ | $`-i/6`$ |
| $`3`$ | $`2`$ | $`-1`$ | $`-i/2`$ |
| $`4`$ | $`1`$ | $`+1`$ | $`i`$ |
| $`5`$ | $`0`$ | $`+1`$ | $`i`$ |

is thereby fixed. The rank-zero identity also follows from

```math
\frac{i}{5!}\varepsilon^{abcdf}\gamma_{abcdf}
=\frac{i^2}{5!}\varepsilon^{abcdf}\varepsilon_{abcdf}\mathbf1
=\frac{-1}{5!}(-5!)\mathbf1
=\mathbf1
```

while the rank-five identity closes directly through $`\gamma^{abcdf}=i\varepsilon^{abcdf}\mathbf1`$.

## E. $`SU(2)`$ index algebra

Let $`\mathsf E`$ denote only the matrix of internal epsilon components:

```math
\mathsf E=(\epsilon_{ij})=(\epsilon^{ij})
=\begin{pmatrix}0&1\\-1&0\end{pmatrix}.
```

These components are defined in the source; no numerical value is assigned to a free physical parameter. The products

```math
\mathsf E\mathsf E^{\mathsf T}
=\begin{pmatrix}1&0\\0&1\end{pmatrix},
\qquad
\mathsf E^2
=\begin{pmatrix}-1&0\\0&-1\end{pmatrix}
```

with

```math
\epsilon^{ij}\epsilon_{kj}=\delta^i{}_k,
\qquad
\epsilon^{ij}\epsilon_{jk}=-\delta^i{}_k
```

are verified. Composing the raising and lowering operations gives

```math
\epsilon^{ij}X_j
=\epsilon^{ij}X^k\epsilon_{kj}
=\delta^i{}_kX^k=X^i
```

so the two rules are inverses. Applying them separately to a two-index tensor gives

```math
L_i{}^j=\epsilon^{j\ell}L_{i\ell},
\qquad
L^{ij}=\epsilon^{ik}L_k{}^j
=\epsilon^{ik}\epsilon^{j\ell}L_{k\ell}
```

which establishes the identity.

For a spinor contraction, keeping the product order and only relabelling dummy indices,

```math
\begin{aligned}
\bar X_i\Gamma Y^i
&=\bar X^j\epsilon_{ji}\Gamma Y^i\\
&=\bar X^i\Gamma Y^j\epsilon_{ij}\\
&=-\bar X^i\Gamma Y^j\epsilon_{ji}\\
&=-\bar X^i\Gamma Y_i.
\end{aligned}
```

This sign comes from the $`SU(2)`$ epsilon tensor; no two Grassmann-odd objects have been interchanged.

## F. Open-index and contracted spinor interchange rules

For the source's Grassmann-odd spinor pairing, $`t_0=t_1=+1`$ is a definition. Compatibility with the Clifford algebra can be examined using the complex-linear operation $`\tau`$ that reverses Clifford-product order:

```math
\tau(\mathbf1)=\mathbf1,
\qquad
\tau(\gamma^a)=\gamma^a,
\qquad
\tau(AB)=\tau(B)\tau(A),
\qquad
\tau(i)=i.
```

Here $`\tau`$ acts on the Clifford algebra; it is neither complex conjugation nor a new Dirac-adjoint definition. Applied to the defining Clifford relation,

```math
\tau\!\left(\gamma^a\gamma^b+\gamma^b\gamma^a
             -2\eta^{ab}\mathbf1\right)
=\gamma^b\gamma^a+\gamma^a\gamma^b-2\eta^{ab}\mathbf1
=0
```

it preserves the algebra. For an antisymmetric rank-$`n`$ product,

```math
\begin{aligned}
\tau(\gamma^{a_1\ldots a_n})
&=\gamma^{a_n\ldots a_1}\\
&=(-1)^{n(n-1)/2}\gamma^{a_1\ldots a_n}.
\end{aligned}
```

Thus the relative Clifford signs in the specified spinor interchange table

```math
t_n=(-1)^{n(n-1)/2},
\qquad
(t_0,t_1,t_2,t_3,t_4,t_5)=(+1,+1,-1,-1,+1,+1)
```

are consistent. In particular, applying $`\tau`$ to both sides of the rank-five relation preserves $`\gamma^{abcdf}=i\varepsilon^{abcdf}\mathbf1`$, since $`(-1)^{10}=+1`$ and $`\tau(i)=i`$. The ranks related by duality also satisfy

```math
t_5=t_0,
\qquad t_4=t_1,
\qquad t_3=t_2
```

This check establishes the relative signs of the defined flip algebra and its compatibility with Clifford duality. It does not derive the adjoint operation from an explicit charge-conjugation matrix or reality condition absent from the source.

The contracted interchange rule follows directly from the defined open-index rule:

```math
\begin{aligned}
\bar X^i\gamma_{(n)}Y_i
&=\epsilon_{ji}\bar X^i\gamma_{(n)}Y^j\\
&=t_n\epsilon_{ji}\bar Y^j\gamma_{(n)}X^i\\
&=-t_n\bar Y^j\gamma_{(n)}(X^i\epsilon_{ij})\\
&=-t_n\bar Y^j\gamma_{(n)}X_j.
\end{aligned}
```

Repeating the interchange gives $`(-t_n)^2=1`$, restoring the original contraction. No Fierz rearrangement is used or added as a verified result in this section.

## G. Lorentz connection and the Clifford product rule

The Lorentz connection is antisymmetric: $`\omega_{\mu ab}=-\omega_{\mu ba}`$. The Lorentz derivative of an upper-index vector is

```math
\nabla_\mu^{\mathrm L}X^a
=\partial_\mu X^a+\omega_\mu{}^a{}_bX^b
```

and metric compatibility gives

```math
\begin{aligned}
\nabla_\mu^{\mathrm L}X_a
&=\partial_\mu X_a+\omega_{\mu ab}X^b\\
&=\partial_\mu X_a+\omega_{\mu ab}\eta^{bc}X_c\\
&=\partial_\mu X_a-\omega_\mu{}^c{}_aX_c
\end{aligned}
```

Since the connection acts on every lower index in the same way,

```math
\begin{aligned}
\nabla_\mu^{\mathrm L}T_{ab}
&=\partial_\mu T_{ab}
 -\omega_\mu{}^c{}_aT_{cb}
 -\omega_\mu{}^c{}_bT_{ac}\\
&=\partial_\mu T_{ab}
 +\omega_\mu{}^c{}_aT_{bc}
 -\omega_\mu{}^c{}_bT_{ac}\\
&=\partial_\mu T_{ab}+2\omega_\mu{}^c{}_{[a}T_{b]c}.
\end{aligned}
```

For an independent check using the spinor connection, temporarily define

```math
\Omega_\mu:=\frac14\omega_\mu{}^{cd}\gamma_{cd},
\qquad
\mathsf T:=T_{ab}\gamma^{ab}
```

The first required commutator follows directly from the Clifford relation. First,

```math
\begin{aligned}
\gamma_c\gamma_d\gamma^a
&=2\delta_d{}^a\gamma_c-\gamma_c\gamma^a\gamma_d\\
&=2\delta_d{}^a\gamma_c-2\delta_c{}^a\gamma_d
 +\gamma^a\gamma_c\gamma_d,\\
[\gamma_c\gamma_d,\gamma^a]
&=2\delta_d{}^a\gamma_c-2\delta_c{}^a\gamma_d.
\end{aligned}
```

Substituting $`\gamma_{cd}=\tfrac12(\gamma_c\gamma_d-\gamma_d\gamma_c)`$ gives

```math
\begin{aligned}
[\gamma_{cd},\gamma^a]
&=\frac12\left(2\delta_d{}^a\gamma_c-2\delta_c{}^a\gamma_d
               -2\delta_c{}^a\gamma_d+2\delta_d{}^a\gamma_c\right)\\
&=2(\delta_d{}^a\gamma_c-\delta_c{}^a\gamma_d),\\
[\Omega_\mu,\gamma^a]
&=\frac12\omega_\mu{}^{cd}
 (\delta_d{}^a\gamma_c-\delta_c{}^a\gamma_d)\\
&=\frac12\omega_\mu{}^{ca}\gamma_c
  -\frac12\omega_\mu{}^{ad}\gamma_d\\
&=-\omega_\mu{}^a{}_c\gamma^c.
\end{aligned}
```

Using the commutator product rule and antisymmetrization,

```math
\begin{aligned}
[\Omega_\mu,\gamma^{ab}]
&=[\Omega_\mu,\gamma^{[a}]\gamma^{b]}
  +\gamma^{[a}[\Omega_\mu,\gamma^{b]}]\\
&=-\omega_\mu{}^a{}_c\gamma^{cb}
  -\omega_\mu{}^b{}_c\gamma^{ac},\\
[\Omega_\mu,\mathsf T]
&=-T_{ab}\omega_\mu{}^a{}_c\gamma^{cb}
  -T_{ab}\omega_\mu{}^b{}_c\gamma^{ac}\\
&=\gamma^{ab}
  (-\omega_\mu{}^c{}_aT_{cb}-\omega_\mu{}^c{}_bT_{ac})\\
&=\gamma^{ab}\,2\omega_\mu{}^c{}_{[a}T_{b]c}.
\end{aligned}
```

Let $`\xi`$ be an arbitrary spinor. Tangent gamma matrices represent a fixed Clifford basis. Using $`\nabla_\mu^{\mathrm L}=\partial_\mu+\Omega_\mu`$ on a spinor gives

```math
\begin{aligned}
\nabla_\mu^{\mathrm L}(\mathsf T\xi)
-\mathsf T\nabla_\mu^{\mathrm L}\xi
&=\bigl(\partial_\mu\mathsf T+[\Omega_\mu,\mathsf T]\bigr)\xi\\
&=\gamma^{ab}
  \left(\partial_\mu T_{ab}
       +2\omega_\mu{}^c{}_{[a}T_{b]c}\right)\xi\\
&=\gamma^{ab}(\nabla_\mu^{\mathrm L}T_{ab})\xi.
\end{aligned}
```

In the original variables, the common result of both checks is

```math
\nabla_\mu^{\mathrm L}T_{ab}
=\partial_\mu T_{ab}+2\omega_\mu{}^c{}_{[a}T_{b]c}
```

No field value, torsionless condition, or equation of motion has been imposed on $`\omega_\mu{}^{ab}`$ or $`T_{ab}`$. The remaining supercovariant-derivative terms do not follow from this connection check.

## H. Scope of the check

This appendix covers the metric–determinant relation, vielbein transformations, antisymmetrization weight, epsilon contractions, gamma duality, $`SU(2)`$ signs, consistency of the defined flip algebra, and the Lorentz-derivative sign. Dot, slash, and $`T^2,T^4,(T^2)^2`$ notation are definitions; no additional physical identity between them is assumed.

The source's action, multiplet, SUSY transformation, supercovariant field-strength, and curvature completions were not used as inputs to this section. Preserving a source record does not establish every result in that file.
