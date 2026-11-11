# Fermionic component input on the regular BPS product family

This page and the [quadratic-action derivation](fermionic_quadratic_action.md)
supply the action evaluation cited in paper Section 4.6 (repository citation 25). The [component package](../../../computations/gb_ads3_sigma2_fermionic/README.md)
retains the manuscript's numerical evaluation method for the GB contribution.
Source coefficients and background formulas remain exact; a numerical matrix
at specified parameters is not a free-parameter symbolic identity.

## Action and normalization

The two-derivative input is the 2016-map
[density (5.10)](../../../common/two_derivative_action/details/construction.md),
with its composite slots (4.19), (4.21), (4.24), (4.30), (4.32), (5.5)
and dependent connections. The higher-derivative input is the current
[GB-FINAL-DENSITY](../../action/gb_splus_action.md), including explicitly
fermionic terms and two-fermion completions of bosonic-form terms.
The [2016-map qualifications](../../../common/two_derivative_action/details/gb_input_qualifications.md)
continue to apply; the literal 2013-map action is not substituted.

The source and manuscript normalizations are related by

```math
\begin{aligned}
\mathcal L_{\mathrm{source}}
 &=\mathcal L_{LR}+\lambda_{\mathrm{GB}}(-2\mathcal L_W-4\mathcal L_{\log}),\\
\mathcal L_{\mathrm{paper}}
 &=\mathcal L_{LR}+\lambda(\mathcal L_W+2\mathcal L_{\log}),\\
k&=\lambda g^2,\qquad
\lambda_{\mathrm{GB}}=-\frac{\lambda}{2}=-\frac{k}{2g^2}.
\end{aligned}
\tag{F24.1}
```

In stored matrices W already includes $`-2`$, and LOG includes $`-4`$.
Thus K = LR + lambda_GB*(W + LOG). This is the specified source
representation, not an assertion of all-order equivalence between
different nonlinear fermionic actions.

## Background and conventions

Use the upper-sign BPS family of paper equations (4.1) and (4.4),
with $`L>0,\ g>0`$. The exact [background function](../../../computations/gb_ads3_sigma2_fermionic/background.py)
agrees with the accepted [bosonic input](action_inputs.md):

```math
\begin{aligned}
P_1&=2-kL,& P_2&=4-kL,& P_3&=2L+4-kL^2,\\
P_4&=8-4k-4kL+k^2L^2,&
P_5&=8+4k-8kL+k^2L^2,\\
v&=\frac{2g^2L(2L-8+3kL-kL^2)}{P_4},&
\ell_s&=\frac{\sqrt2P_2}{gP_3},&
\ell&=\chi\ell_s>0,\\
p&=\frac{gL}{\sqrt2},&
h=q_{\mathrm{flux}}&=\frac{g(L-2)}{\sqrt2P_2},&
N&=-\frac{gLP_3}{P_2},\\
r&=v,& w^2&=-v,&
\chi&=\mathop{\mathrm{sign}}\nolimits(P_3/P_2).
\end{aligned}
\tag{F24.2}
```

The code's h is the manuscript's flux q, not the R-charge $`q_R`$.
The background ordinary current and $`V'`$ vanish. The regular calculation
excludes $`P_1P_2P_3P_4P_5=0`$; the bare-potential chart additionally
requires $`v\ne0`$. It uses $`C_3=p/w,\ V_3=r/w`$, with continuation
$`w=i\sqrt v`$ for the sphere. The $`k\ne0`$ torus and excluded families
are outside the manuscript's fermionic calculation. A separate check of
the constant torus at $`k=0`$ concerns only the LR block.

The source uses signature $`(-++++)`$, a linear Majorana bar, NW–SE
SU(2) lowering, unit-weight antisymmetrization, and left Grassmann
variation. The charge dictionaries are
$`J_{\mathrm{source}}^2=-1`$ and
$`\mathbb J=-iJ_{\mathrm{source}}`$, so that
$`J_{\mathrm{source}}u=i q_Ru`$ corresponds to
$`\mathbb Ju=q_Ru`$, $`q_R=\pm1`$.
The [component dictionary](../../ads5/code/references/COMPONENT_CONVENTIONS.md)
and the following H variation specify the conventions used by the calculation.

## Three-form variation

The tangent variation contains the following G–dilatino and gauged
linear-multiplet contributions:

```math
\delta\widehat H_{abc}\big|_{\mathrm{two\ corrections}}
=+\frac32\bar\epsilon\gamma_{[a}\widehat G_{bc]}\psi
 +\frac g2\bar\epsilon\gamma_{abc}\varphi .
\tag{F24.3}
```

Here $`\psi`$ without a frame index is the dilatino. The sigma and frame
variations are also retained in the full H02 expression.

The first contribution follows from $`H=dB+\tfrac12C\wedge G`$,
$`\delta B|_C=\tfrac12C\wedge\delta C`$, and
$`\delta C_a=\tfrac12\bar\epsilon\gamma_a\psi`$:

```math
\begin{aligned}
\delta H\big|_C
 &=d\!\left(\frac12C\wedge\delta C\right)
   +\frac12\delta C\wedge G+\frac12C\wedge d\delta C
   =G\wedge\delta C,\\
(\delta H)_{abc}\big|_{G\psi}
 &=+\frac32\bar\epsilon\gamma_{[a}G_{bc]}\psi.
\end{aligned}
\tag{F24.4}
```

For the second, H contains $`gE_3/2`$, while the linear-multiplet
variation in the GB14/GG04a potential convention contains
$`\delta E_{abc}|_\varphi=\bar\epsilon\gamma_{abc}\varphi`$.
The X10 convention for the L04 potential variation applies. The complete composite-T variation and the gauged
H Bianchi identity are checked against these rules. The [source manifest](../../../computations/gb_ads3_sigma2_fermionic/source_manifest.json)
identifies the current component inputs.

## Full derivatives at quadratic order

The Poincaré dilatino gauge $`\psi=0`$ does not set
$`\mathcal D_a\psi`$ to zero. GB07 and its ordered descendants retain
the Q/S connections; derivatives of these descendants also retain
the K connection. In particular, bare-C source term 17 (zero-based)
differentiates a fermion bilinear. Its Q/S connection terms have
fermion order two and survive:

```math
\mathcal D_b(\bar X\Gamma Y)
=\overline{\mathcal D_bX}\Gamma Y+\bar X\Gamma\mathcal D_bY.
\tag{F24.5}
```

Replacing this derivative by an ordinary covariant divergence breaks
the action's local-SUSY null columns. The implementation applies
(F24.5) before contraction; it does not discard the bare-C term by
ordinary integration by parts.

Similarly $`\bar E^a=0`$ does not imply $`\widehat E^{a(2)}=0`$.
With the ordinary current $`P^{a(2)}=0`$,

```math
\widehat E^{a(2)}
=-\frac i2\bar\psi_b\gamma^{ba}\varphi
 -\frac14L_{ij}\bar\psi_b^i\gamma^{abc}\psi_c^j.
\tag{F24.6}
```

This ordinary-current expression is compared with the independent
gauged-Bianchi construction used internally. The same order bookkeeping
applies to $`\widehat G,\widehat H,T,D,R(M),R(V)`$ and their ordered
derivatives. All gravitino and compensator components in the specified
mode ansatz remain; no fluctuation gauge or fermion field equation is
used to simplify the action.
