# Step 4 — Zeroth-order action with unknown background values

This calculation substitutes [Step 3](STEP_03_FIRST_ORDER_INGREDIENTS.md) into the accepted `GB-FINAL-DENSITY`. Write $`L=L_0`$, $`N=N_0`$ in background-only formulas below. Neither scalar is yet on shell. The answer is a local density, multiplied by the formal background volume; no regularized total AdS/dS volume is assumed.

## 4.1 Two-derivative contribution

Equation (3.18) gives

```math
\ell_{2,0}=-2\left(-\frac{15}{2}kL\right)-8L\left(-\frac58k+\frac g4N+\frac{g^2}{16}L^2\right)-\frac{2N^2}{L}-4gN+2g^2L^2. \tag{4.1}
```

Distribute $`-8L`$ and combine the two curvature terms:

```math
\ell_{2,0}=15kL+5kL-2gLN-\frac12g^2L^3-\frac{2N^2}{L}-4gN+2g^2L^2
=20Lk-\frac{2N^2}{L}-2gLN-4gN+2g^2L^2-\frac12g^2L^3. \tag{4.2}
```

The $`20Lk`$ coefficient arises from the conformal box and $`D`$ together. Setting the conformal box of a constant compensator to zero would destroy it.

## 4.2 Every scalar higher-derivative contribution

The labels below locate terms in the accepted full density via its assembly ledger; they do not introduce a new input action. The exterior coupling $`\lambda`$ is not included in this table.

| Locator | Term in full density | Background substitution | Contribution |
|---|---|---|---|
| W2 | $`-128D^2/3`$ | $`D=-5k/8+gN/4+g^2L^2/16`$ | Expanded in (4.3) |
| L46 | $`-10(\Box^c\sigma)^2/3`$ | $`(-5k/2)^2`$ | $`-125k^2/6`$ |
| L47 | $`-26g^2L^{ij}L_{ij}\Box^c\sigma/3`$ | $`L^2(-5k/2)`$ | $`65g^2L^2k/3`$ |
| L48 | $`-32gN\Box^c\sigma/3`$ | $`N(-5k/2)`$ | $`80gNk/3`$ |
| L49 | $`-7g^4(L^{ij}L_{ij})^2/12`$ | $`(L^2)^2`$ | $`-7g^4L^4/12`$ |
| L50 | $`-8g^3NL^{ij}L_{ij}/3`$ | $`NL^2`$ | $`-8g^3NL^2/3`$ |
| L51 | $`2g^2N^2/3`$ | $`N^2`$ | $`2g^2N^2/3`$ |
| L71 | $`2g^2L^{ij}\Box^cL_{ij}`$ | $`L(-15kL/2)`$ | $`-15g^2L^2k`$ |
| L74 | $`6(\mathcal D^a\mathcal D^b\sigma)(\mathcal D_a\mathcal D_b\sigma)`$ | $`6(5k^2/4)`$ | $`15k^2/2`$ |
| L75 | $`3g^2\mathcal D^aL^{ij}\mathcal D_aL_{ij}`$ | $`(0)(0)`$ | $`0`$ |
| L76 | $`4g\Box^cN`$ | $`4g(-10kN)`$ | $`-40gNk`$ |
| L80 | $`-g^4L^{ij}L_i{}^kL_j{}^lL_{kl}/2`$ | $`-g^4(L^4/2)/2`$ | $`-g^4L^4/4`$ |

For W2 square all three terms before collecting:

```math
\begin{aligned}
-\frac{128}{3}D_0^2&=-\frac{128}{3}\left[\frac{25k^2}{64}+\frac{g^2N^2}{16}+\frac{g^4L^4}{256}-\frac{5gNk}{16}-\frac{5g^2L^2k}{64}+\frac{g^3NL^2}{32}\right]\\
&=-\frac{50}{3}k^2-\frac83g^2N^2-\frac16g^4L^4+\frac{40}{3}gNk+\frac{10}{3}g^2L^2k-\frac43g^3NL^2 .
\end{aligned}\tag{4.3}
```

The cross terms in the first row are $`2(-5k/8)(gN/4)`$, $`2(-5k/8)(g^2L^2/16)`$ and $`2(gN/4)(g^2L^2/16)`$. Thus each factor of two is fixed by the ordinary square, with no fermionic exchange involved.

Collect the actual contributions of each monomial:

```math
\begin{aligned}
[k^2]:&\ -\frac{50}{3}-\frac{125}{6}+\frac{15}{2}=\frac{-100-125+45}{6}=-30,\qquad
[gNk]:\ \frac{40}{3}+\frac{80}{3}-40=0,\\
[g^2L^2k]:&\ \frac{10}{3}+\frac{65}{3}-15=\frac{10+65-45}{3}=10,\qquad
[g^2N^2]:\ -\frac83+\frac23=-2,\\
[g^3NL^2]:&\ -\frac43-\frac83=-4,\qquad
[g^4L^4]:\ -\frac16-\frac7{12}-\frac14=\frac{-2-7-3}{12}=-1.
\end{aligned}\tag{4.4}
```

Therefore the higher-derivative background density is

```math
\ell_{\mathrm{GB},0}=-30k^2+10g^2L^2k-2g^2N^2-4g^3NL^2-g^4L^4. \tag{4.5}
```

All other outer terms have zero zeroth-order coefficient for the explicit reasons and locators in Step 3 and its ledger. In particular (4.5) was not taken from a pre-existing bosonic GB formula.

## 4.3 Complete zeroth-order result

Combining (4.2) and (4.5), define $`F`$ to be the local background density:

```math
\boxed{F(k,L,N)=20Lk-\frac{2N^2}{L}-2gLN-4gN+2g^2L^2-\frac12g^2L^3+\lambda\left(-30k^2+10g^2L^2k-2g^2N^2-4g^3NL^2-g^4L^4\right).} \tag{4.6}
```

```math
\boxed{S^{(0)}=\frac1{2\kappa_5^2}\int d^5x\,\bar e\,F(k,L_0,N_0).} \tag{4.7}
```

Every term outside the $`\lambda`$ bracket has engineering dimension two; each term inside has dimension four. Hence $`[d^5x]+[\kappa_5^{-2}]+[F]=-5+3+2=0`$. This includes $`N^2/L`$ and $`g^4L^4`$, whose different powers of $`L`$ are dimensionally allowed because $`[L]=0`$.

## 4.4 Reduced checks and their limitation

Since $`L_0,N_0`$ are constants, reduced differentiation of (4.6) must agree with the scalar coefficients subsequently found from arbitrary $`\ell(x),n(x)`$. For a constant metric rescaling $`\delta g_{\mu\nu}=\epsilon\bar g_{\mu\nu}`$, $`\delta e=5\epsilon\bar e/2`$ and $`\delta k=-\epsilon k`$, so

```math
\delta(\bar eF)=\epsilon\bar e\left(\frac52F-kF_k\right). \tag{4.8}
```

This gives a check on the trace tadpole. It does not establish vector, form, internal-connection, traceless-metric or fermion stationarity. Those coefficients are derived from the unrestricted fluctuation expansion in Step 5.
