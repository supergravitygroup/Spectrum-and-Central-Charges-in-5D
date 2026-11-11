# Action, source correspondence and background

Use the bosonic blocks (G-2D), (G-W), (G-LOG) and definitions (G-D1)–(G-D11)
of the [current component action](../../../generic_combination/action.md).
The parameter specialization is the definition of the Gauss–Bonnet theory:

```math
\begin{aligned}
\mathcal L&=\mathcal L_{LR}+\lambda(\ell_W+2\ell_{\log}),&
k&=\lambda g^2,&(\alpha,\beta,\zeta)&=(\lambda,2\lambda,0),\\
\lambda&=-2\lambda_{\rm GB},&
\ell_W+2\ell_{\log}&\supset\tfrac18\mathrm{GB}.
\end{aligned}
```

The last conversion relates the component coefficient to the paper normalization
used throughout this chapter. The metric
has signature (-,+,+,+,+), epsilon upper 01234 is +1, and light-cone
components are X_plus = X0 + X1, X_minus = X0 - X1. The curvature convention
is the one in the current action. The engine variable `h` denotes the
background flux q; the spectral variable D is not the auxiliary Weyl scalar.

| Source identifier | Implementation and verification |
|---|---|
| G-2D | `action.py:LLR`; the triplet contraction becomes 2 Z barZ in the charged basis |
| G-D7, G-D8 | T=(G-2H)/8, the full bosonic auxiliary D, f and conformal Weyl curvature in `source_weyl.py` |
| G-W, G-D9–G-D11 | Independent differentiated-current representative; C nabla Q and the T second derivative are integrated by parts once with all f and K corrections retained |
| G-LOG | `source_LOG` retains the cyclic H derivative, double-epsilon term and explicit g²E²/3; compared to the Bianchi-rewritten representative |
| W + 2 LOG | Compared entry by entry with the compact GB density, including its three E-dependent terms |
| Paper equations (2.3), (2.17), (4.1), (4.4) | Compact bulk representative, field dictionary and BPS branch |

These comparisons hold for all **662 entries** of the six off-shell sector
matrices, before the BPS substitution and with the background parameters
free. They establish equality of these quadratic actions modulo the stated
bulk integrations by parts, not an independent all-order SUSY proof.
The [source manifest](../../../computations/gb_ads3_sigma2/source_manifest.json)
locks the current inputs and identifies the manuscript and component-source versions.

The form definitions, retained during variation, are

```math
\begin{aligned}
G&=dC,& H_3&=dB+\tfrac12 C\wedge G+\tfrac g2E_3,
&dH_3&=\tfrac12G\wedge G+\tfrac g2dE_3,\\
H_{ab}&=-\tfrac1{12}\varepsilon_{abcde}H^{cde},
&B'&=B-\tfrac12\bar C\wedge c,\\
H_3&=\bar H_3+db'+c\wedge\bar G+\tfrac12c\wedge dc+\tfrac g2e_3.
\end{aligned}
```

The potential and field-strength representatives are verified by the exact
congruence induced by B = B' + barC wedge c/2. The latter also replaces bare
background-potential CS terms by their flux/CS representatives and has a
regular constant-torus limit. In particular, E_a=0 on the background does
not remove the terms -g epsilon EGG/8, -g epsilon EHH and g²E² from its Hessian.

With the upper-sign BPS projection of v109, define

```math
\begin{aligned}
P_1&=2-kL,&P_2&=4-kL,&P_3&=2L+4-kL^2,\\
P_4&=8-4k-4kL+k^2L^2,&P_5&=8+4k-8kL+k^2L^2,\\
v&=\frac{2g^2L(2L-8+3kL-kL^2)}{P_4},&
\ell_s&=\frac{\sqrt2P_2}{gP_3},&\ell&=|\ell_s|,\\
p&=\frac{gL}{\sqrt2},&q&=\frac{g(L-2)}{\sqrt2P_2},&
r&=v,\qquad N=-\frac{gLP_3}{P_2},\\
\chi&=\mathop{\mathrm{sgn}}\nolimits(P_3/P_2),&w^2&=-v.
\end{aligned}
```

The BPS identities and the stationary fixed-flux Einstein-frame scalar
potential are checked symbolically. On the sphere, w is an analytic harmonic
coordinate; its imaginary phase must be restored in the harmonic inner
product when interpreting norms. No value g=1 or g=sqrt(2) is used.
