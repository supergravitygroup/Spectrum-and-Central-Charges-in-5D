# Constant-curvature density and tadpoles

This shared projection supplies the background density used in the paper's
[AdS5 central-charge calculation](../computations/generic_ads5_massless/SOURCE_MAP.md#curvature-inputs-for-a-and-c).
The calculation differentiates the density before imposing the supersymmetric
AdS5 relations. No general vacuum classification is included here.

The field domain is $`L_0>0`$, $`c_2\ne0`$, with real couplings. The metric convention is

```math
\bar R_{\mu\nu\rho\sigma}
=k(\bar g_{\mu\rho}\bar g_{\nu\sigma}-\bar g_{\mu\sigma}\bar g_{\nu\rho}),
\qquad\bar R_{\mu\nu}=4k\bar g_{\mu\nu},\qquad\bar R=20k.
```

Full invariance of the bosonic configuration, including its compact source-real
SU(2) representation, gives the following field values in local gauge
representatives:

```math
\begin{gathered}
\bar L=L_0>0,\qquad\bar N=N_0,\qquad
\bar L^{ij}=\frac{L_0}{\sqrt2}\delta^{ij},\qquad
\bar C=\bar B=\bar E_3=0,\\
\bar\nabla_\mu\bar L^{ij}=0,\qquad
\bar V'_\mu{}^{ij}=0,\qquad
\bar V_\mu=\partial_\mu\chi\quad\text{locally},\qquad
\bar V_{\mu\nu}^{ij}=0,\\
\bar D=-\frac58k+\frac14gN_0+\frac1{16}g^2L_0^2,\qquad
\bar{\boldsymbol Y}^{ij}
=-\left(\frac{10k}{L_0}+\frac{N_0^2}{L_0^3}\right)\bar L^{ij}.
\end{gathered}
```

Here $`\chi`$ is the local residual gauge function. Covariant constancy fixes the source-traceless connection; isotropy separately
sets the residual curvature to zero. The
[paper background](../computations/generic_ads5_massless/SOURCE_MAP.md#background-and-retained-fields)
uses this zero-form-strength configuration.
No coupling division is used in those symmetry conditions. A maximally symmetric
metric with arbitrary nonsymmetric connection profiles is a different problem.

Background restrictions do not restrict the variations. In particular,
$`L(t)=L_0+t\ell`$ and $`N(t)=N_0+tn`$ retain arbitrary independent $`\ell,n`$;
zero-background potentials and connections also retain their fluctuations.
The [component action](action.md) fixes the independent fields and potential definitions.
The constrained current $`E^a`$ is varied through $`E_3`$, yielding
$`dJ_E+gP_H=0`$, not an independent equation $`J_E=0`$.
Here $`J_E`$ is the source three-form current and $`P_H`$ is the coefficient of the
$`H`$-strength variation.

## Density and tadpoles

The density retains the four source blocks separately; their exact expressions
are also supplied in the [background-block input](../computations/generic_ads5_massless/background_blocks.py).


```math
\begin{aligned}
\mathcal F={}&c_2\left(20kL_0-\frac{2N_0^2}{L_0}
-2gL_0N_0-4gN_0-\frac12g^2L_0^3+2g^2L_0^2\right)
+\frac{64\alpha}{3}\bar D^2\\
&+\beta\left(\frac{10}{3}k^2+\frac{10}{3}gkN_0
-\frac53g^2kL_0^2-\frac16g^2N_0^2
+\frac23g^3N_0L_0^2+\frac5{24}g^4L_0^4\right)\\
&+\lambda\left[\left(10k+\frac{N_0^2}{L_0^2}\right)^2
-5g^2kL_0^2-\frac52g^2N_0^2
-\frac{4gN_0^3}{L_0^2}+\frac1{16}g^4L_0^4\right].
\end{aligned}\tag{S4-6}
```

The local tadpoles already derived with arbitrary fluctuations obey

```math
\mathcal E_N^{(0)}=\partial_{N_0}\mathcal F,\qquad
\mathcal E_L^{(0)}=\partial_{L_0}\mathcal F,\qquad
\mathcal E_g^{(0)}=\frac12\mathcal F-\frac{k}{5}\partial_k\mathcal F .
\tag{S4-7}
```

The last equation includes the measure variation; it is not $`\partial_k\mathcal F=0`$.
These are the local $`S^{(1)}`$ coefficients on the stated background class.
This projection does not turn a general restricted variation into an unrestricted EOM derivation.


The [AdS5 source projection](../computations/generic_ads5_massless/SOURCE_MAP.md#curvature-inputs-for-a-and-c)
states the three tadpoles on the supersymmetric background, and its checks
verify their reduction to the paper's vacuum polynomial. On the fully symmetric
class the three scalar equations cancel the remaining bulk tadpoles. With
$`h=\bar g^{\mu\nu}h_{\mu\nu}`$ denoting the metric-fluctuation trace,

```math
S^{(1)}_{\rm bulk}=\frac1{2\kappa_5^2}\int d^5x\,\bar e
\left(n\mathcal E_N^{(0)}+\ell\mathcal E_L^{(0)}
+h\mathcal E_g^{(0)}+\sum_{\text{other fields}}\delta\Phi\cdot0\right).
```

The sum denotes contractions with coefficients that vanish on this background,
not discarded fluctuations. The independent boundary term must still be treated;
compactly supported variations establish local stationarity only.
