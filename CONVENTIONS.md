# Common convention authority

The common convention dictionary is [Notation and conventions](common/conventions.md),
with the detailed [source definitions](common/details/source_conventions.md)
and [algebraic conversion appendix](common/details/convention_conversions.md).
These definitions fix the index and Clifford interpretation of the scientific
chapters.

## Geometry and density

```math
D=5,\qquad \eta_{ab}=\mathop{\mathrm{diag}}\nolimits(-,+,+,+,+),\qquad
e=\det(e_\mu{}^a)=\sqrt{-\det g_{\mu\nu}},\qquad
S=\int d^5x\,e\,\ell .
```

Antisymmetrization has unit weight. The coordinate epsilon tensor and density
symbol obey $`\epsilon^{\mu\nu\rho\sigma\lambda} =e\,\varepsilon^{\mu\nu\rho\sigma\lambda}`$.
The common dictionary assigns no numerical value to $`\varepsilon^{01234}`$.
Lorentzian epsilon contraction and gamma duality are retained symbolically.

## Spinors and internal indices

```math
\{\gamma^a,\gamma^b\}=2\eta^{ab},\qquad
\gamma^{abcde}=i\varepsilon^{abcde}\mathbf1,\qquad
\gamma\!\cdot\!X=\gamma^{a_1\cdots a_p}X_{a_1\cdots a_p}.
```

The dot contraction has no extra $`1/p!`$. The NW–SE rules are

```math
\epsilon_{12}=\epsilon^{12}=1,\qquad
X^i=\epsilon^{ij}X_j,\qquad X_i=X^j\epsilon_{ji}.
```

For Grassmann-odd spinors, the open-index flip signs are
$`(t_0,t_1,t_2,t_3,t_4,t_5)=(1,1,-1,-1,1,1)`$;
the contracted flip has sign $`-t_n`$. A source's explicit charge-conjugation
matrix, adjoint phase or orientation does not supply missing common data by
implication. The physical-norm sections specify any additional reality input.

## Derivatives and source corrections

The full supercovariant derivative is distinguished from its Lorentz part.
For a lower antisymmetric Lorentz tensor,

```math
\left.\mathcal D_\mu T_{ab}\right|_\omega
=2\omega_\mu{}^c{}_{[a}T_{b]c}.
```

Lowering both indices of the upper-triplet connection gives

```math
\left.\mathcal D_\mu L_{ij}\right|_V=-2V_{\mu(i}{}^kL_{j)k}.
```

The [two-derivative construction](common/two_derivative_action/details/construction.md)
derives this sign in (4.27a). Earlier source copies with a positive lower-index
term are read with the [current action conventions](references/fermionic_input_correspondence.md).
The working explicit $`\chi`$ term in $`R'(M)`$ and the dependent $`f_\mu{}^a`$
definition must be converted together, as shown in the common source reference.

Hatted strengths, dependent connections and differentiated gauge-fixed fields
retain their defined fermionic contributions. In particular the vanishing
defining dilatino is distinct from its nonzero supercovariant derivative and
from the gravitino.

## Couplings, background branches and source frames

The [coupling dictionary](README.md#action-and-coupling-correspondence) separates the common $`\alpha,\beta,\zeta`$
basis, the GB spectrum coupling and the assembled action's $`c_2`$.
Background values are used only on the branch determined by their displayed
equations. Source-local orientation and explicit matrix frames are documented
with their derivations; fixed-parameter component checks are not general
symbolic verification.
