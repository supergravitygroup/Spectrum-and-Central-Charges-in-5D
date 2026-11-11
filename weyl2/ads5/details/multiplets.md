# Supermultiplet matching

[Reading guide](../README.md). The equation labels and local symbols below follow the action conventions specified for this theory.

<a id="13-supermultiplet-matching"></a>

## Supermultiplet matching

<a id="131-algebra-notation-and-scope-of-the-claim"></a>

### Algebra, notation, and scope of the claim

The eight Killing spinors of the selected branch are compatible with
the $`\mathfrak{su}(2,2|1)`$ algebra in AdS₅. In the notation $`D(\Delta;j_L,j_R)_r`$, $`\Delta/\ell`$ is the
lowest energy and $`j_L,j_R`$ are the $`SO(4)\simeq SU(2)_L\times SU(2)_R`$ spins.

This section matches field content, mass/energy relations, and the displayed SUSY links. Its representation statements refer to these data and component links.

Fix the orientation of the $`R`$ charge by

```math
Q_L:(\tfrac12,0)_{-1},\qquad
Q_R:(0,\tfrac12)_{+1}
```

This fixes only the orientation of the charge label; it does not change the $`g`$ normalization.

With this choice of $`Q_L,Q_R`$, acting with $`Q_L`$ on the scalar primary gives $`(1/2,0)_{-1}`$. The table below uses this orientation throughout.

<a id="132-two-massless-multiplets"></a>

### Two massless multiplets

```math
\begin{aligned}
\mathcal G:\quad&
D(3;\tfrac12,\tfrac12)_0
\oplus D(\tfrac72;1,\tfrac12)_{-1}
\oplus D(\tfrac72;\tfrac12,1)_{+1}
\oplus D(4;1,1)_0,\\
&N_B=N_F=8,
\\[1mm]
\mathcal V:\quad&
D(2;0,0)_0
\oplus D(\tfrac52;\tfrac12,0)_{-1}
\oplus D(\tfrac52;0,\tfrac12)_{+1}
\oplus D(3;\tfrac12,\tfrac12)_0,\\
&N_B=N_F=4.
\end{aligned}
```

The vectors are $`v_0`$ and $`u_0=c_0+\sqrt2v_0/(3g)`$, respectively.
One check showing that this is not an arbitrary assignment based only on pole counting is the following: on the Maxwell solution, with $`F=-dv_0/(\sqrt2g)`$, $`p=0`$,

```math
\delta X=-\frac{J}{128}\gamma\cdot(dv_0+\sqrt2gF)\epsilon=0,
```

```math
\delta\zeta_{\rm s}
=\frac{J}{4\sqrt2}\gamma\cdot(3G-2F)\epsilon
=\frac{3J}{4\sqrt2}\gamma\cdot du_0\,\epsilon.
```

This link identifies $`u_0`$ as the vector of the scalar–spinor multiplet.

<a id="133-content-of-the-additional-long-spin-2-multiplet"></a>

### Content of the additional long spin-2 multiplet

```math
E_0=1+\rho=1+\sqrt{1-\frac6{\alpha g^2}}.
```

The primary is the vector $`Z_-`$. The name spin-2 multiplet refers to its highest spin.
These additional SUSY-linked modes are extra operator branches produced by the finite Weyl-squared coefficient; they do not introduce new fields into the independent-field list.

```math
V=(\tfrac12,\tfrac12)_0,\qquad
U=(\tfrac12,0)_{-1}\oplus(0,\tfrac12)_{+1},
\qquad
V\otimes\wedge^nU,\quad n=0,\ldots,4.
```

| Level | $`SO(4)\times U(1)_R`$ content | Fields | $`\Delta`$ | Count |
|---|---|---|---:|---:|
| $`0`$ | $`(1/2,1/2)_0`$ | $`Z_-`$ | $`1+\rho`$ | $`4_B`$ |
| $`1`$ | $`(1,1/2)_{-1}+(0,1/2)_{-1}+(1/2,1)_{+1}+(1/2,0)_{+1}`$ | $`\Psi_-,X_-`$ | $`3/2+\rho`$ | $`16_F`$ |
| $`2`$ | $`(1,1)_0+(0,0)_0+(1,0)_0+(0,1)_0+(1/2,1/2)_{+2}+(1/2,1/2)_{-2}`$ | $`H_1,d,T_+,T_-,v'_+,v'_-`$ | $`2+\rho`$ | $`24_B`$ |
| $`3`$ | $`(1,1/2)_{+1}+(0,1/2)_{+1}+(1/2,1)_{-1}+(1/2,0)_{-1}`$ | $`\Psi_+,X_+`$ | $`5/2+\rho`$ | $`16_F`$ |
| $`4`$ | $`(1/2,1/2)_0`$ | $`Z_+`$ | $`3+\rho`$ | $`4_B`$ |

Dimension check:
Using $`(2j_L+1)(2j_R+1)`$,

```math
4+24+4=32,\qquad 16+16=32,\qquad
24=9+1+3+3+4+4.
```

Mass matching:

```math
\begin{aligned}
M_{H_1,d}^2\ell^2
&=\rho^2-4=(E_0+1)(E_0-3),\\
M_{v'}^2\ell^2&=\rho^2-1=E_0(E_0-2),\\
M_{Z_-}^2\ell^2&=\rho^2-2\rho=(E_0-1)(E_0-3),\\
M_{Z_+}^2\ell^2&=\rho^2+2\rho=(E_0+1)(E_0-1),\\
M_T^2\ell^2&=\rho^2 .
\end{aligned}
```

With boundary chiralities selected together, the signed fermionic Dirac roots
give energies $`\Delta=3/2+\rho`$ and $`5/2+\rho`$.
Taking absolute values to select fast falloff independently for every field
is incompatible with this matching.

Direct check of a scalar–spinor link:

```math
\delta d=\bar\epsilon(\mathord{\not{\nabla}}-m)X,\qquad
\Box(\bar\epsilon X)
=\bar\epsilon(\mathord{\not{\nabla}}^2+2m\mathord{\not{\nabla}}-15m^2)X,
```

```math
\begin{aligned}
(\Box+\kappa)(\bar\epsilon X)
&=\bar\epsilon[(\mathord{\not{\nabla}}+m)^2+\kappa-16m^2]X\\
&=\bar\epsilon[(\mathord{\not{\nabla}}+m)^2-\nu^2]X=0 .
\end{aligned}
```

Also, $`\delta\lambda_{\rm s}=-(2/g)\bar\epsilon m\zeta_{\rm s}`$ maps to the scalar equation of the same massless vector multiplet.

Generic candidate organization:

```math
\boxed{
\mathcal G_{8+8}\oplus\mathcal V_{4+4}
\oplus\mathfrak L_{32+32}
\left(1+\sqrt{1-\frac6{\alpha g^2}}\right).
}
```

Here “long” denotes content whose state count has not been reduced by a
shortening condition. For a unitary long representation, $`E_0>3`$ requires
$`\rho>2`$, equivalently $`-2<\alpha g^2<0`$. In this region the overall kinetic sign
of the long multiplet is still that of a ghost. Abstract representation
unitarity and positive norm in the action are distinct criteria.
$`E_0=1-\rho`$ denotes the formal shadow organization of the other boundary
quantization; it is not added as a second independent set of $`32+32`$ bulk modes.

<a id="bolum-14"></a>

