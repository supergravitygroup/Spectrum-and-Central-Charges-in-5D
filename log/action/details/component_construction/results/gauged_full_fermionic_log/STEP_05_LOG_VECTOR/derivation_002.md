# LOG vector descent — S5-D01 – S5-H1.3-product-4

<a id="step-5--deriving-the-log-vector--4-detailed-derivation"></a>

[Component index](../STEP_05_LOG_VECTOR.md). Definitions and source conventions are in [the opening section](convention_001.md).

## 4. Detailed Derivation

### 4.1 Differentiate the denominator without changing odd-factor order

For each actual term $`W^{-n}P`$ of the calculated primary, the first derivative is

```math
\nabla_\eta^r(W^{-n}P)=-niW^{-n-1}\lambda_\eta^rP+W^{-n}\nabla_\eta^rP.
\tag{S5-D01}
```

Apply the second derivative to each displayed factor, retaining the original ordering of the two gaugini:

```math
\begin{aligned}
\nabla_\zeta^t\nabla_\eta^r(W^{-n}P)
={}&-n(n+1)W^{-n-2}\lambda_\zeta^t\lambda_\eta^rP
-niW^{-n-1}(\nabla_\zeta^t\lambda_\eta^r)P
+niW^{-n-1}\lambda_\eta^r\nabla_\zeta^tP\\
&-niW^{-n-1}\lambda_\zeta^t\nabla_\eta^rP
+W^{-n}\nabla_\zeta^t\nabla_\eta^rP,\\
-ni(\nabla_\zeta^t\lambda_\eta^r)P
={}&2ni\varepsilon^{tr}(F_{\zeta\eta}+W_{\zeta\eta}W)P
+ni\varepsilon_{\zeta\eta}X^{tr}P
+ni\varepsilon^{tr}(\Gamma^b)_{\zeta\eta}(\nabla_bW)P.
\end{aligned}
\tag{S5-D02}
```

The third term has a plus sign because the second derivative passes the odd $`\lambda_\eta^r`$. The first coefficient is $`(-ni)(-(n+1)i)=-n(n+1)`$. No denominator derivative is omitted. If $`P`$ already contains two fermions, the first term has degree four and belongs to the higher remainder; when $`P`$ is bosonic it is a retained bilinear.

### 4.2 Product signs and vector-derivative commutators

For a specific ordered product, each differentiated factor receives $`(-1)`$ for every odd factor to its left. For example the actual field pattern $`\lambda_\alpha^i(\nabla_bX^{jl})\lambda_{\beta l}`$ occurring in H3.9 gives

```math
\begin{aligned}
\nabla_\eta^r\!\left[\lambda_\alpha^i(\nabla_bX^{jl})\lambda_{\beta l}\right]
={}&(\nabla_\eta^r\lambda_\alpha^i)(\nabla_bX^{jl})\lambda_{\beta l}
-\lambda_\alpha^i(\nabla_\eta^r\nabla_bX^{jl})\lambda_{\beta l}
-\lambda_\alpha^i(\nabla_bX^{jl})(\nabla_\eta^r\lambda_{\beta l}),\\
\nabla_\zeta^t\nabla_\eta^r\!\left[\lambda_\alpha^i(\nabla_bX^{jl})\lambda_{\beta l}\right]
={}&(\nabla_\zeta^t\nabla_\eta^r\lambda_\alpha^i)(\nabla_bX^{jl})\lambda_{\beta l}
+(\nabla_\eta^r\lambda_\alpha^i)(\nabla_\zeta^t\nabla_bX^{jl})\lambda_{\beta l}
+(\nabla_\eta^r\lambda_\alpha^i)(\nabla_bX^{jl})(\nabla_\zeta^t\lambda_{\beta l})\\
&-(\nabla_\zeta^t\lambda_\alpha^i)(\nabla_\eta^r\nabla_bX^{jl})\lambda_{\beta l}
+\lambda_\alpha^i(\nabla_\zeta^t\nabla_\eta^r\nabla_bX^{jl})\lambda_{\beta l}
-\lambda_\alpha^i(\nabla_\eta^r\nabla_bX^{jl})(\nabla_\zeta^t\lambda_{\beta l})\\
&-(\nabla_\zeta^t\lambda_\alpha^i)(\nabla_bX^{jl})(\nabla_\eta^r\lambda_{\beta l})
+\lambda_\alpha^i(\nabla_\zeta^t\nabla_bX^{jl})(\nabla_\eta^r\lambda_{\beta l})
+\lambda_\alpha^i(\nabla_bX^{jl})(\nabla_\zeta^t\nabla_\eta^r\lambda_{\beta l}).
\end{aligned}
\tag{S5-D03}
```

The minus on the sixth summand is the product of the existing minus and the two odd factors passed; the middle differentiated triplet factor is odd there. The second and eighth summands have the signs written because the differentiated gaugino is even. This sign expansion is before the $`i,j`$ symmetrization and the denominator terms; both are included in the actual H3.9 calculation below.

Each $`\nabla_\eta^r\nabla_bU`$ is replaced by the ordered $`\nabla_b\nabla_\eta^rU`$ **plus every term** of the vector–spinor commutator in §3.4. The second derivative can act on those curvatures; §3.5 displays the differentiated curvature formulas. Lorentz and SU(2) generators act on every free slot of $`U`$, including any vector-derivative index. The S and K terms on a vector descendant are retained, even when its undifferentiated parent is primary.

### 4.3 Calculations for the 58 primary inputs

For every input below, the first equation is its actual contribution to our calculated $`H^{ij}`$. The next equation inserts the elementary and commutator identities into its first derivative, retaining all degree-one and degree-three terms of that derivative. The following equations show **every term of the second graded product rule**, before substitution of the differentiated single factors from §3. The selector on the first derivative is stated explicitly; it is justified by (S5-V06).

After those substitutions, contract with the common factor in (S5-V02) and retain degrees zero and two. The evaluated endpoint for every input is written in §7, not left as a derivative prescription. The contribution-location ledger gives the exact final display segments for each input. For H6.1 and H6.2 the degree bound gives zero retained terms, and the equations below state that bound rather than differentiating an irrelevant sector.

### Input H0.1

```math
\begin{aligned}
\left.H^{ij}\right|_{\mathrm{H0.1}}={}&-\frac{3i}{8}W{}_{a b}X{}^{a b i j}
\end{aligned}
\tag{S5-H0.1-input}
```

Insert the derivative laws in §3 and expand the weighted symmetrization. The retained first derivative is

```math
\begin{aligned}
\left[\left.\nabla_\eta^r H^{ij}\right|_{\mathrm{H0.1}}\right]_{\le3}={}&-\frac{3i}{8}(\Sigma{}_{a b}){}^{\alpha \beta}W{}_{\eta \alpha \beta}{}^{r}X{}^{a b i j} -\frac{3i}{16}(\Sigma{}_{a b}){}_{\eta}{}^{\alpha}X{}_{\alpha}{}^{r}X{}^{a b i j}\\
&-\frac{3i}{16}(\Sigma{}_{a b}){}^{\alpha}{}_{\eta}X{}_{\alpha}{}^{r}X{}^{a b i j} -\frac{3}{16}W{}_{a b}(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r i}W{}_{\eta \gamma}W{}_{\alpha \beta}{}^{\gamma j}\\
&-\frac{9}{32}W{}_{a b}(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r i}W{}_{\alpha \beta}X{}_{\eta}{}^{j} +\frac{3}{8}W{}_{a b}(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r i}(\Gamma{}^{c}){}_{\eta}{}^{\gamma}\big(\nabla_{c}W{}_{\alpha \beta \gamma}{}^{j}\big)\\
&-\frac{9}{32}W{}_{a b}(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r i}W{}_{\alpha}{}^{\gamma}W{}_{\beta \eta \gamma}{}^{j} -\frac{3}{32}W{}_{a b}(\Sigma{}^{a b}){}_{\eta}{}^{\alpha}\varepsilon{}^{r i}W{}^{\beta \gamma}W{}_{\alpha \beta \gamma}{}^{j}\\
&+\frac{3}{64}W{}_{a b}(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r i}W{}_{\eta \alpha}X{}_{\beta}{}^{j} +\frac{9}{64}W{}_{a b}(\Sigma{}^{a b}){}_{\eta}{}^{\alpha}\varepsilon{}^{r i}W{}_{\alpha \beta}X{}^{\beta j}\\
&+\frac{3}{16}W{}_{a b}(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r i}(\Gamma{}^{c}){}_{\alpha}{}^{\gamma}\big(\nabla_{c}W{}_{\beta \eta \gamma}{}^{j}\big) -\frac{3}{32}W{}_{a b}(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r i}(\Gamma{}^{c}){}_{\eta \alpha}\big(\nabla_{c}X{}_{\beta}{}^{j}\big)\\
&+\frac{3}{32}W{}_{a b}(\Sigma{}^{a b}){}_{\eta}{}^{\alpha}\varepsilon{}^{r i}(\Gamma{}^{c}){}_{\alpha \beta}\big(\nabla_{c}X{}^{\beta j}\big) -\frac{9}{32}W{}_{a b}(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r i}W{}_{\beta}{}^{\gamma}W{}_{\alpha \eta \gamma}{}^{j}\\
&-\frac{3}{32}W{}_{a b}(\Sigma{}^{a b}){}^{\alpha}{}_{\eta}\varepsilon{}^{r i}W{}^{\beta \gamma}W{}_{\alpha \beta \gamma}{}^{j} +\frac{3}{64}W{}_{a b}(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r i}W{}_{\eta \beta}X{}_{\alpha}{}^{j}\\
&+\frac{9}{64}W{}_{a b}(\Sigma{}^{a b}){}^{\alpha}{}_{\eta}\varepsilon{}^{r i}W{}_{\alpha \beta}X{}^{\beta j} +\frac{3}{16}W{}_{a b}(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r i}(\Gamma{}^{c}){}_{\beta}{}^{\gamma}\big(\nabla_{c}W{}_{\alpha \eta \gamma}{}^{j}\big)\\
&-\frac{3}{32}W{}_{a b}(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r i}(\Gamma{}^{c}){}_{\eta \beta}\big(\nabla_{c}X{}_{\alpha}{}^{j}\big) +\frac{3}{32}W{}_{a b}(\Sigma{}^{a b}){}^{\alpha}{}_{\eta}\varepsilon{}^{r i}(\Gamma{}^{c}){}_{\alpha \beta}\big(\nabla_{c}X{}^{\beta j}\big)\\
&-\frac{3}{16}W{}_{a b}(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r j}W{}_{\eta \gamma}W{}_{\alpha \beta}{}^{\gamma i} -\frac{9}{32}W{}_{a b}(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r j}W{}_{\alpha \beta}X{}_{\eta}{}^{i}\\
&+\frac{3}{8}W{}_{a b}(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r j}(\Gamma{}^{c}){}_{\eta}{}^{\gamma}\big(\nabla_{c}W{}_{\alpha \beta \gamma}{}^{i}\big) -\frac{9}{32}W{}_{a b}(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r j}W{}_{\alpha}{}^{\gamma}W{}_{\beta \eta \gamma}{}^{i}\\
&-\frac{3}{32}W{}_{a b}(\Sigma{}^{a b}){}_{\eta}{}^{\alpha}\varepsilon{}^{r j}W{}^{\beta \gamma}W{}_{\alpha \beta \gamma}{}^{i} +\frac{3}{64}W{}_{a b}(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r j}W{}_{\eta \alpha}X{}_{\beta}{}^{i}\\
&+\frac{9}{64}W{}_{a b}(\Sigma{}^{a b}){}_{\eta}{}^{\alpha}\varepsilon{}^{r j}W{}_{\alpha \beta}X{}^{\beta i} +\frac{3}{16}W{}_{a b}(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r j}(\Gamma{}^{c}){}_{\alpha}{}^{\gamma}\big(\nabla_{c}W{}_{\beta \eta \gamma}{}^{i}\big)\\
&-\frac{3}{32}W{}_{a b}(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r j}(\Gamma{}^{c}){}_{\eta \alpha}\big(\nabla_{c}X{}_{\beta}{}^{i}\big) +\frac{3}{32}W{}_{a b}(\Sigma{}^{a b}){}_{\eta}{}^{\alpha}\varepsilon{}^{r j}(\Gamma{}^{c}){}_{\alpha \beta}\big(\nabla_{c}X{}^{\beta i}\big)\\
&-\frac{9}{32}W{}_{a b}(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r j}W{}_{\beta}{}^{\gamma}W{}_{\alpha \eta \gamma}{}^{i} -\frac{3}{32}W{}_{a b}(\Sigma{}^{a b}){}^{\alpha}{}_{\eta}\varepsilon{}^{r j}W{}^{\beta \gamma}W{}_{\alpha \beta \gamma}{}^{i}\\
&+\frac{3}{64}W{}_{a b}(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r j}W{}_{\eta \beta}X{}_{\alpha}{}^{i} +\frac{9}{64}W{}_{a b}(\Sigma{}^{a b}){}^{\alpha}{}_{\eta}\varepsilon{}^{r j}W{}_{\alpha \beta}X{}^{\beta i}\\
&+\frac{3}{16}W{}_{a b}(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r j}(\Gamma{}^{c}){}_{\beta}{}^{\gamma}\big(\nabla_{c}W{}_{\alpha \eta \gamma}{}^{i}\big) -\frac{3}{32}W{}_{a b}(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r j}(\Gamma{}^{c}){}_{\eta \beta}\big(\nabla_{c}X{}_{\alpha}{}^{i}\big)\\
&+\frac{3}{32}W{}_{a b}(\Sigma{}^{a b}){}^{\alpha}{}_{\eta}\varepsilon{}^{r j}(\Gamma{}^{c}){}_{\alpha \beta}\big(\nabla_{c}X{}^{\beta i}\big)
\end{aligned}
\tag{S5-H0.1-spinor}
```

Act with the next left derivative on each written factor, with its graded sign:

```math
\begin{aligned}
\nabla_\zeta^t\left[\left.\nabla_\eta^rH^{ij}\right|_{\mathrm{H0.1}}\right]_{\le3}={}&-\frac{3i}{8}(\Sigma{}_{a b}){}^{\alpha \beta}\nabla_{\zeta}^{t}\big(W{}_{\eta \alpha \beta}{}^{r}\big)X{}^{a b i j} +\frac{3i}{8}(\Sigma{}_{a b}){}^{\alpha \beta}W{}_{\eta \alpha \beta}{}^{r}\nabla_{\zeta}^{t}\big(X{}^{a b i j}\big)\\
&-\frac{3i}{16}(\Sigma{}_{a b}){}_{\eta}{}^{\alpha}\nabla_{\zeta}^{t}\big(X{}_{\alpha}{}^{r}\big)X{}^{a b i j} +\frac{3i}{16}(\Sigma{}_{a b}){}_{\eta}{}^{\alpha}X{}_{\alpha}{}^{r}\nabla_{\zeta}^{t}\big(X{}^{a b i j}\big)\\
&-\frac{3i}{16}(\Sigma{}_{a b}){}^{\alpha}{}_{\eta}\nabla_{\zeta}^{t}\big(X{}_{\alpha}{}^{r}\big)X{}^{a b i j} +\frac{3i}{16}(\Sigma{}_{a b}){}^{\alpha}{}_{\eta}X{}_{\alpha}{}^{r}\nabla_{\zeta}^{t}\big(X{}^{a b i j}\big)\\
&-\frac{3}{16}\nabla_{\zeta}^{t}\big(W{}_{a b}\big)(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r i}W{}_{\eta \gamma}W{}_{\alpha \beta}{}^{\gamma j} -\frac{3}{16}W{}_{a b}(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r i}\nabla_{\zeta}^{t}\big(W{}_{\eta \gamma}\big)W{}_{\alpha \beta}{}^{\gamma j}\\
&-\frac{3}{16}W{}_{a b}(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r i}W{}_{\eta \gamma}\nabla_{\zeta}^{t}\big(W{}_{\alpha \beta}{}^{\gamma j}\big) -\frac{9}{32}\nabla_{\zeta}^{t}\big(W{}_{a b}\big)(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r i}W{}_{\alpha \beta}X{}_{\eta}{}^{j}\\
&-\frac{9}{32}W{}_{a b}(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r i}\nabla_{\zeta}^{t}\big(W{}_{\alpha \beta}\big)X{}_{\eta}{}^{j} -\frac{9}{32}W{}_{a b}(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r i}W{}_{\alpha \beta}\nabla_{\zeta}^{t}\big(X{}_{\eta}{}^{j}\big)\\
&+\frac{3}{8}\nabla_{\zeta}^{t}\big(W{}_{a b}\big)(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r i}(\Gamma{}^{c}){}_{\eta}{}^{\gamma}\big(\nabla_{c}W{}_{\alpha \beta \gamma}{}^{j}\big) +\frac{3}{8}W{}_{a b}(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r i}(\Gamma{}^{c}){}_{\eta}{}^{\gamma}\nabla_{\zeta}^{t}\big(\nabla_{c}W{}_{\alpha \beta \gamma}{}^{j}\big)\\
&-\frac{9}{32}\nabla_{\zeta}^{t}\big(W{}_{a b}\big)(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r i}W{}_{\alpha}{}^{\gamma}W{}_{\beta \eta \gamma}{}^{j} -\frac{9}{32}W{}_{a b}(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r i}\nabla_{\zeta}^{t}\big(W{}_{\alpha}{}^{\gamma}\big)W{}_{\beta \eta \gamma}{}^{j}\\
&-\frac{9}{32}W{}_{a b}(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r i}W{}_{\alpha}{}^{\gamma}\nabla_{\zeta}^{t}\big(W{}_{\beta \eta \gamma}{}^{j}\big) -\frac{3}{32}\nabla_{\zeta}^{t}\big(W{}_{a b}\big)(\Sigma{}^{a b}){}_{\eta}{}^{\alpha}\varepsilon{}^{r i}W{}^{\beta \gamma}W{}_{\alpha \beta \gamma}{}^{j}\\
&-\frac{3}{32}W{}_{a b}(\Sigma{}^{a b}){}_{\eta}{}^{\alpha}\varepsilon{}^{r i}\nabla_{\zeta}^{t}\big(W{}^{\beta \gamma}\big)W{}_{\alpha \beta \gamma}{}^{j} -\frac{3}{32}W{}_{a b}(\Sigma{}^{a b}){}_{\eta}{}^{\alpha}\varepsilon{}^{r i}W{}^{\beta \gamma}\nabla_{\zeta}^{t}\big(W{}_{\alpha \beta \gamma}{}^{j}\big)\\
&+\frac{3}{64}\nabla_{\zeta}^{t}\big(W{}_{a b}\big)(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r i}W{}_{\eta \alpha}X{}_{\beta}{}^{j} +\frac{3}{64}W{}_{a b}(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r i}\nabla_{\zeta}^{t}\big(W{}_{\eta \alpha}\big)X{}_{\beta}{}^{j}\\
&+\frac{3}{64}W{}_{a b}(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r i}W{}_{\eta \alpha}\nabla_{\zeta}^{t}\big(X{}_{\beta}{}^{j}\big) +\frac{9}{64}\nabla_{\zeta}^{t}\big(W{}_{a b}\big)(\Sigma{}^{a b}){}_{\eta}{}^{\alpha}\varepsilon{}^{r i}W{}_{\alpha \beta}X{}^{\beta j}\\
&+\frac{9}{64}W{}_{a b}(\Sigma{}^{a b}){}_{\eta}{}^{\alpha}\varepsilon{}^{r i}\nabla_{\zeta}^{t}\big(W{}_{\alpha \beta}\big)X{}^{\beta j} +\frac{9}{64}W{}_{a b}(\Sigma{}^{a b}){}_{\eta}{}^{\alpha}\varepsilon{}^{r i}W{}_{\alpha \beta}\nabla_{\zeta}^{t}\big(X{}^{\beta j}\big)\\
&+\frac{3}{16}\nabla_{\zeta}^{t}\big(W{}_{a b}\big)(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r i}(\Gamma{}^{c}){}_{\alpha}{}^{\gamma}\big(\nabla_{c}W{}_{\beta \eta \gamma}{}^{j}\big) +\frac{3}{16}W{}_{a b}(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r i}(\Gamma{}^{c}){}_{\alpha}{}^{\gamma}\nabla_{\zeta}^{t}\big(\nabla_{c}W{}_{\beta \eta \gamma}{}^{j}\big)\\
&-\frac{3}{32}\nabla_{\zeta}^{t}\big(W{}_{a b}\big)(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r i}(\Gamma{}^{c}){}_{\eta \alpha}\big(\nabla_{c}X{}_{\beta}{}^{j}\big) -\frac{3}{32}W{}_{a b}(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r i}(\Gamma{}^{c}){}_{\eta \alpha}\nabla_{\zeta}^{t}\big(\nabla_{c}X{}_{\beta}{}^{j}\big)\\
&+\frac{3}{32}\nabla_{\zeta}^{t}\big(W{}_{a b}\big)(\Sigma{}^{a b}){}_{\eta}{}^{\alpha}\varepsilon{}^{r i}(\Gamma{}^{c}){}_{\alpha \beta}\big(\nabla_{c}X{}^{\beta j}\big) +\frac{3}{32}W{}_{a b}(\Sigma{}^{a b}){}_{\eta}{}^{\alpha}\varepsilon{}^{r i}(\Gamma{}^{c}){}_{\alpha \beta}\nabla_{\zeta}^{t}\big(\nabla_{c}X{}^{\beta j}\big)\\
&-\frac{9}{32}\nabla_{\zeta}^{t}\big(W{}_{a b}\big)(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r i}W{}_{\beta}{}^{\gamma}W{}_{\alpha \eta \gamma}{}^{j} -\frac{9}{32}W{}_{a b}(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r i}\nabla_{\zeta}^{t}\big(W{}_{\beta}{}^{\gamma}\big)W{}_{\alpha \eta \gamma}{}^{j}\\
&-\frac{9}{32}W{}_{a b}(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r i}W{}_{\beta}{}^{\gamma}\nabla_{\zeta}^{t}\big(W{}_{\alpha \eta \gamma}{}^{j}\big) -\frac{3}{32}\nabla_{\zeta}^{t}\big(W{}_{a b}\big)(\Sigma{}^{a b}){}^{\alpha}{}_{\eta}\varepsilon{}^{r i}W{}^{\beta \gamma}W{}_{\alpha \beta \gamma}{}^{j}\\
&-\frac{3}{32}W{}_{a b}(\Sigma{}^{a b}){}^{\alpha}{}_{\eta}\varepsilon{}^{r i}\nabla_{\zeta}^{t}\big(W{}^{\beta \gamma}\big)W{}_{\alpha \beta \gamma}{}^{j} -\frac{3}{32}W{}_{a b}(\Sigma{}^{a b}){}^{\alpha}{}_{\eta}\varepsilon{}^{r i}W{}^{\beta \gamma}\nabla_{\zeta}^{t}\big(W{}_{\alpha \beta \gamma}{}^{j}\big)\\
&+\frac{3}{64}\nabla_{\zeta}^{t}\big(W{}_{a b}\big)(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r i}W{}_{\eta \beta}X{}_{\alpha}{}^{j} +\frac{3}{64}W{}_{a b}(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r i}\nabla_{\zeta}^{t}\big(W{}_{\eta \beta}\big)X{}_{\alpha}{}^{j}\\
&+\frac{3}{64}W{}_{a b}(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r i}W{}_{\eta \beta}\nabla_{\zeta}^{t}\big(X{}_{\alpha}{}^{j}\big) +\frac{9}{64}\nabla_{\zeta}^{t}\big(W{}_{a b}\big)(\Sigma{}^{a b}){}^{\alpha}{}_{\eta}\varepsilon{}^{r i}W{}_{\alpha \beta}X{}^{\beta j}\\
&+\frac{9}{64}W{}_{a b}(\Sigma{}^{a b}){}^{\alpha}{}_{\eta}\varepsilon{}^{r i}\nabla_{\zeta}^{t}\big(W{}_{\alpha \beta}\big)X{}^{\beta j} +\frac{9}{64}W{}_{a b}(\Sigma{}^{a b}){}^{\alpha}{}_{\eta}\varepsilon{}^{r i}W{}_{\alpha \beta}\nabla_{\zeta}^{t}\big(X{}^{\beta j}\big)\\
&+\frac{3}{16}\nabla_{\zeta}^{t}\big(W{}_{a b}\big)(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r i}(\Gamma{}^{c}){}_{\beta}{}^{\gamma}\big(\nabla_{c}W{}_{\alpha \eta \gamma}{}^{j}\big) +\frac{3}{16}W{}_{a b}(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r i}(\Gamma{}^{c}){}_{\beta}{}^{\gamma}\nabla_{\zeta}^{t}\big(\nabla_{c}W{}_{\alpha \eta \gamma}{}^{j}\big)\\
&-\frac{3}{32}\nabla_{\zeta}^{t}\big(W{}_{a b}\big)(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r i}(\Gamma{}^{c}){}_{\eta \beta}\big(\nabla_{c}X{}_{\alpha}{}^{j}\big) -\frac{3}{32}W{}_{a b}(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r i}(\Gamma{}^{c}){}_{\eta \beta}\nabla_{\zeta}^{t}\big(\nabla_{c}X{}_{\alpha}{}^{j}\big)\\
&+\frac{3}{32}\nabla_{\zeta}^{t}\big(W{}_{a b}\big)(\Sigma{}^{a b}){}^{\alpha}{}_{\eta}\varepsilon{}^{r i}(\Gamma{}^{c}){}_{\alpha \beta}\big(\nabla_{c}X{}^{\beta j}\big) +\frac{3}{32}W{}_{a b}(\Sigma{}^{a b}){}^{\alpha}{}_{\eta}\varepsilon{}^{r i}(\Gamma{}^{c}){}_{\alpha \beta}\nabla_{\zeta}^{t}\big(\nabla_{c}X{}^{\beta j}\big)\\
&-\frac{3}{16}\nabla_{\zeta}^{t}\big(W{}_{a b}\big)(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r j}W{}_{\eta \gamma}W{}_{\alpha \beta}{}^{\gamma i} -\frac{3}{16}W{}_{a b}(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r j}\nabla_{\zeta}^{t}\big(W{}_{\eta \gamma}\big)W{}_{\alpha \beta}{}^{\gamma i}\\
&-\frac{3}{16}W{}_{a b}(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r j}W{}_{\eta \gamma}\nabla_{\zeta}^{t}\big(W{}_{\alpha \beta}{}^{\gamma i}\big) -\frac{9}{32}\nabla_{\zeta}^{t}\big(W{}_{a b}\big)(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r j}W{}_{\alpha \beta}X{}_{\eta}{}^{i}\\
&-\frac{9}{32}W{}_{a b}(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r j}\nabla_{\zeta}^{t}\big(W{}_{\alpha \beta}\big)X{}_{\eta}{}^{i} -\frac{9}{32}W{}_{a b}(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r j}W{}_{\alpha \beta}\nabla_{\zeta}^{t}\big(X{}_{\eta}{}^{i}\big)\\
&+\frac{3}{8}\nabla_{\zeta}^{t}\big(W{}_{a b}\big)(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r j}(\Gamma{}^{c}){}_{\eta}{}^{\gamma}\big(\nabla_{c}W{}_{\alpha \beta \gamma}{}^{i}\big) +\frac{3}{8}W{}_{a b}(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r j}(\Gamma{}^{c}){}_{\eta}{}^{\gamma}\nabla_{\zeta}^{t}\big(\nabla_{c}W{}_{\alpha \beta \gamma}{}^{i}\big)\\
&-\frac{9}{32}\nabla_{\zeta}^{t}\big(W{}_{a b}\big)(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r j}W{}_{\alpha}{}^{\gamma}W{}_{\beta \eta \gamma}{}^{i} -\frac{9}{32}W{}_{a b}(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r j}\nabla_{\zeta}^{t}\big(W{}_{\alpha}{}^{\gamma}\big)W{}_{\beta \eta \gamma}{}^{i}\\
&-\frac{9}{32}W{}_{a b}(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r j}W{}_{\alpha}{}^{\gamma}\nabla_{\zeta}^{t}\big(W{}_{\beta \eta \gamma}{}^{i}\big) -\frac{3}{32}\nabla_{\zeta}^{t}\big(W{}_{a b}\big)(\Sigma{}^{a b}){}_{\eta}{}^{\alpha}\varepsilon{}^{r j}W{}^{\beta \gamma}W{}_{\alpha \beta \gamma}{}^{i}\\
&-\frac{3}{32}W{}_{a b}(\Sigma{}^{a b}){}_{\eta}{}^{\alpha}\varepsilon{}^{r j}\nabla_{\zeta}^{t}\big(W{}^{\beta \gamma}\big)W{}_{\alpha \beta \gamma}{}^{i} -\frac{3}{32}W{}_{a b}(\Sigma{}^{a b}){}_{\eta}{}^{\alpha}\varepsilon{}^{r j}W{}^{\beta \gamma}\nabla_{\zeta}^{t}\big(W{}_{\alpha \beta \gamma}{}^{i}\big)\\
&+\frac{3}{64}\nabla_{\zeta}^{t}\big(W{}_{a b}\big)(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r j}W{}_{\eta \alpha}X{}_{\beta}{}^{i} +\frac{3}{64}W{}_{a b}(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r j}\nabla_{\zeta}^{t}\big(W{}_{\eta \alpha}\big)X{}_{\beta}{}^{i}\\
&+\frac{3}{64}W{}_{a b}(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r j}W{}_{\eta \alpha}\nabla_{\zeta}^{t}\big(X{}_{\beta}{}^{i}\big) +\frac{9}{64}\nabla_{\zeta}^{t}\big(W{}_{a b}\big)(\Sigma{}^{a b}){}_{\eta}{}^{\alpha}\varepsilon{}^{r j}W{}_{\alpha \beta}X{}^{\beta i}\\
&+\frac{9}{64}W{}_{a b}(\Sigma{}^{a b}){}_{\eta}{}^{\alpha}\varepsilon{}^{r j}\nabla_{\zeta}^{t}\big(W{}_{\alpha \beta}\big)X{}^{\beta i} +\frac{9}{64}W{}_{a b}(\Sigma{}^{a b}){}_{\eta}{}^{\alpha}\varepsilon{}^{r j}W{}_{\alpha \beta}\nabla_{\zeta}^{t}\big(X{}^{\beta i}\big)\\
&+\frac{3}{16}\nabla_{\zeta}^{t}\big(W{}_{a b}\big)(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r j}(\Gamma{}^{c}){}_{\alpha}{}^{\gamma}\big(\nabla_{c}W{}_{\beta \eta \gamma}{}^{i}\big) +\frac{3}{16}W{}_{a b}(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r j}(\Gamma{}^{c}){}_{\alpha}{}^{\gamma}\nabla_{\zeta}^{t}\big(\nabla_{c}W{}_{\beta \eta \gamma}{}^{i}\big)\\
&-\frac{3}{32}\nabla_{\zeta}^{t}\big(W{}_{a b}\big)(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r j}(\Gamma{}^{c}){}_{\eta \alpha}\big(\nabla_{c}X{}_{\beta}{}^{i}\big) -\frac{3}{32}W{}_{a b}(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r j}(\Gamma{}^{c}){}_{\eta \alpha}\nabla_{\zeta}^{t}\big(\nabla_{c}X{}_{\beta}{}^{i}\big)\\
&+\frac{3}{32}\nabla_{\zeta}^{t}\big(W{}_{a b}\big)(\Sigma{}^{a b}){}_{\eta}{}^{\alpha}\varepsilon{}^{r j}(\Gamma{}^{c}){}_{\alpha \beta}\big(\nabla_{c}X{}^{\beta i}\big) +\frac{3}{32}W{}_{a b}(\Sigma{}^{a b}){}_{\eta}{}^{\alpha}\varepsilon{}^{r j}(\Gamma{}^{c}){}_{\alpha \beta}\nabla_{\zeta}^{t}\big(\nabla_{c}X{}^{\beta i}\big)\\
&-\frac{9}{32}\nabla_{\zeta}^{t}\big(W{}_{a b}\big)(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r j}W{}_{\beta}{}^{\gamma}W{}_{\alpha \eta \gamma}{}^{i} -\frac{9}{32}W{}_{a b}(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r j}\nabla_{\zeta}^{t}\big(W{}_{\beta}{}^{\gamma}\big)W{}_{\alpha \eta \gamma}{}^{i}\\
&-\frac{9}{32}W{}_{a b}(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r j}W{}_{\beta}{}^{\gamma}\nabla_{\zeta}^{t}\big(W{}_{\alpha \eta \gamma}{}^{i}\big) -\frac{3}{32}\nabla_{\zeta}^{t}\big(W{}_{a b}\big)(\Sigma{}^{a b}){}^{\alpha}{}_{\eta}\varepsilon{}^{r j}W{}^{\beta \gamma}W{}_{\alpha \beta \gamma}{}^{i}\\
&-\frac{3}{32}W{}_{a b}(\Sigma{}^{a b}){}^{\alpha}{}_{\eta}\varepsilon{}^{r j}\nabla_{\zeta}^{t}\big(W{}^{\beta \gamma}\big)W{}_{\alpha \beta \gamma}{}^{i} -\frac{3}{32}W{}_{a b}(\Sigma{}^{a b}){}^{\alpha}{}_{\eta}\varepsilon{}^{r j}W{}^{\beta \gamma}\nabla_{\zeta}^{t}\big(W{}_{\alpha \beta \gamma}{}^{i}\big)\\
&+\frac{3}{64}\nabla_{\zeta}^{t}\big(W{}_{a b}\big)(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r j}W{}_{\eta \beta}X{}_{\alpha}{}^{i} +\frac{3}{64}W{}_{a b}(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r j}\nabla_{\zeta}^{t}\big(W{}_{\eta \beta}\big)X{}_{\alpha}{}^{i}\\
&+\frac{3}{64}W{}_{a b}(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r j}W{}_{\eta \beta}\nabla_{\zeta}^{t}\big(X{}_{\alpha}{}^{i}\big) +\frac{9}{64}\nabla_{\zeta}^{t}\big(W{}_{a b}\big)(\Sigma{}^{a b}){}^{\alpha}{}_{\eta}\varepsilon{}^{r j}W{}_{\alpha \beta}X{}^{\beta i}\\
&+\frac{9}{64}W{}_{a b}(\Sigma{}^{a b}){}^{\alpha}{}_{\eta}\varepsilon{}^{r j}\nabla_{\zeta}^{t}\big(W{}_{\alpha \beta}\big)X{}^{\beta i} +\frac{9}{64}W{}_{a b}(\Sigma{}^{a b}){}^{\alpha}{}_{\eta}\varepsilon{}^{r j}W{}_{\alpha \beta}\nabla_{\zeta}^{t}\big(X{}^{\beta i}\big)\\
&+\frac{3}{16}\nabla_{\zeta}^{t}\big(W{}_{a b}\big)(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r j}(\Gamma{}^{c}){}_{\beta}{}^{\gamma}\big(\nabla_{c}W{}_{\alpha \eta \gamma}{}^{i}\big) +\frac{3}{16}W{}_{a b}(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r j}(\Gamma{}^{c}){}_{\beta}{}^{\gamma}\nabla_{\zeta}^{t}\big(\nabla_{c}W{}_{\alpha \eta \gamma}{}^{i}\big)\\
&-\frac{3}{32}\nabla_{\zeta}^{t}\big(W{}_{a b}\big)(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r j}(\Gamma{}^{c}){}_{\eta \beta}\big(\nabla_{c}X{}_{\alpha}{}^{i}\big) -\frac{3}{32}W{}_{a b}(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r j}(\Gamma{}^{c}){}_{\eta \beta}\nabla_{\zeta}^{t}\big(\nabla_{c}X{}_{\alpha}{}^{i}\big)\\
&+\frac{3}{32}\nabla_{\zeta}^{t}\big(W{}_{a b}\big)(\Sigma{}^{a b}){}^{\alpha}{}_{\eta}\varepsilon{}^{r j}(\Gamma{}^{c}){}_{\alpha \beta}\big(\nabla_{c}X{}^{\beta i}\big) +\frac{3}{32}W{}_{a b}(\Sigma{}^{a b}){}^{\alpha}{}_{\eta}\varepsilon{}^{r j}(\Gamma{}^{c}){}_{\alpha \beta}\nabla_{\zeta}^{t}\big(\nabla_{c}X{}^{\beta i}\big)
\end{aligned}
\tag{S5-H0.1-product}
```

Substitution of §3 and the gamma contraction (S5-V02) produce 841 retained covariant contributions from this input. Their exact coefficients and contractions are included in §7; their locations are recorded in [the input-to-result ledger](../../../../../../../references/source_evidence/log/results/gauged_full_fermionic_log/sources/step5/endpoint_term_locations.json).

### Input H0.2

```math
\begin{aligned}
\left.H^{ij}\right|_{\mathrm{H0.2}}={}&\frac{51i}{64}X{}^{\alpha i}X{}_{\alpha}{}^{j}
\end{aligned}
\tag{S5-H0.2-input}
```

Insert the derivative laws in §3 and expand the weighted symmetrization. The retained first derivative is

```math
\begin{aligned}
\left[\left.\nabla_\eta^r H^{ij}\right|_{\mathrm{H0.2}}\right]_{\le3}={}&\frac{51i}{64}X{}_{\eta}{}^{\alpha r i}X{}_{\alpha}{}^{j} +\frac{51}{512}\varepsilon{}^{r i}YX{}_{\eta}{}^{j}\\
&+\frac{153}{128}\varepsilon{}^{r i}(\Gamma{}^{a}){}_{\eta}{}^{\alpha}\big(\nabla_{a}W{}^{\beta}{}_{\alpha}\big)X{}_{\beta}{}^{j} +\frac{51}{32}\varepsilon{}^{r i}W{}_{\eta}{}^{\alpha}W{}^{\beta}{}_{\alpha}X{}_{\beta}{}^{j}\\
&+\frac{51}{128}\varepsilon{}^{r i}W{}^{\alpha \beta}W{}_{\alpha \beta}X{}_{\eta}{}^{j} +\frac{51}{128}\varepsilon{}^{r i}(\Gamma{}^{a}){}^{\alpha \beta}\big(\nabla_{a}W{}_{\eta \beta}\big)X{}_{\alpha}{}^{j}\\
&-\frac{51i}{64}X{}^{\alpha i}X{}_{\eta \alpha}{}^{r j} +\frac{51}{512}X{}_{\eta}{}^{i}\varepsilon{}^{r j}Y\\
&-\frac{153}{128}X{}^{\alpha i}\varepsilon{}^{r j}(\Gamma{}^{a}){}_{\eta}{}^{\beta}\big(\nabla_{a}W{}_{\alpha \beta}\big) -\frac{51}{32}X{}^{\alpha i}\varepsilon{}^{r j}W{}_{\eta}{}^{\beta}W{}_{\alpha \beta}\\
&+\frac{51}{128}X{}_{\eta}{}^{i}\varepsilon{}^{r j}W{}^{\alpha \beta}W{}_{\alpha \beta} -\frac{51}{128}X{}^{\alpha i}\varepsilon{}^{r j}(\Gamma{}^{a}){}_{\alpha}{}^{\beta}\big(\nabla_{a}W{}_{\eta \beta}\big)
\end{aligned}
\tag{S5-H0.2-spinor}
```

Act with the next left derivative on each written factor, with its graded sign:

```math
\begin{aligned}
\nabla_\zeta^t\left[\left.\nabla_\eta^rH^{ij}\right|_{\mathrm{H0.2}}\right]_{\le3}={}&\frac{51i}{64}\nabla_{\zeta}^{t}\big(X{}_{\eta}{}^{\alpha r i}\big)X{}_{\alpha}{}^{j} +\frac{51i}{64}X{}_{\eta}{}^{\alpha r i}\nabla_{\zeta}^{t}\big(X{}_{\alpha}{}^{j}\big)\\
&+\frac{51}{512}\varepsilon{}^{r i}\nabla_{\zeta}^{t}\big(Y\big)X{}_{\eta}{}^{j} +\frac{51}{512}\varepsilon{}^{r i}Y\nabla_{\zeta}^{t}\big(X{}_{\eta}{}^{j}\big)\\
&+\frac{153}{128}\varepsilon{}^{r i}(\Gamma{}^{a}){}_{\eta}{}^{\alpha}\nabla_{\zeta}^{t}\big(\nabla_{a}W{}^{\beta}{}_{\alpha}\big)X{}_{\beta}{}^{j} +\frac{153}{128}\varepsilon{}^{r i}(\Gamma{}^{a}){}_{\eta}{}^{\alpha}\big(\nabla_{a}W{}^{\beta}{}_{\alpha}\big)\nabla_{\zeta}^{t}\big(X{}_{\beta}{}^{j}\big)\\
&+\frac{51}{32}\varepsilon{}^{r i}\nabla_{\zeta}^{t}\big(W{}_{\eta}{}^{\alpha}\big)W{}^{\beta}{}_{\alpha}X{}_{\beta}{}^{j} +\frac{51}{32}\varepsilon{}^{r i}W{}_{\eta}{}^{\alpha}\nabla_{\zeta}^{t}\big(W{}^{\beta}{}_{\alpha}\big)X{}_{\beta}{}^{j}\\
&+\frac{51}{32}\varepsilon{}^{r i}W{}_{\eta}{}^{\alpha}W{}^{\beta}{}_{\alpha}\nabla_{\zeta}^{t}\big(X{}_{\beta}{}^{j}\big) +\frac{51}{128}\varepsilon{}^{r i}\nabla_{\zeta}^{t}\big(W{}^{\alpha \beta}\big)W{}_{\alpha \beta}X{}_{\eta}{}^{j}\\
&+\frac{51}{128}\varepsilon{}^{r i}W{}^{\alpha \beta}\nabla_{\zeta}^{t}\big(W{}_{\alpha \beta}\big)X{}_{\eta}{}^{j} +\frac{51}{128}\varepsilon{}^{r i}W{}^{\alpha \beta}W{}_{\alpha \beta}\nabla_{\zeta}^{t}\big(X{}_{\eta}{}^{j}\big)\\
&+\frac{51}{128}\varepsilon{}^{r i}(\Gamma{}^{a}){}^{\alpha \beta}\nabla_{\zeta}^{t}\big(\nabla_{a}W{}_{\eta \beta}\big)X{}_{\alpha}{}^{j} +\frac{51}{128}\varepsilon{}^{r i}(\Gamma{}^{a}){}^{\alpha \beta}\big(\nabla_{a}W{}_{\eta \beta}\big)\nabla_{\zeta}^{t}\big(X{}_{\alpha}{}^{j}\big)\\
&-\frac{51i}{64}\nabla_{\zeta}^{t}\big(X{}^{\alpha i}\big)X{}_{\eta \alpha}{}^{r j} +\frac{51i}{64}X{}^{\alpha i}\nabla_{\zeta}^{t}\big(X{}_{\eta \alpha}{}^{r j}\big)\\
&+\frac{51}{512}\nabla_{\zeta}^{t}\big(X{}_{\eta}{}^{i}\big)\varepsilon{}^{r j}Y -\frac{51}{512}X{}_{\eta}{}^{i}\varepsilon{}^{r j}\nabla_{\zeta}^{t}\big(Y\big)\\
&-\frac{153}{128}\nabla_{\zeta}^{t}\big(X{}^{\alpha i}\big)\varepsilon{}^{r j}(\Gamma{}^{a}){}_{\eta}{}^{\beta}\big(\nabla_{a}W{}_{\alpha \beta}\big) +\frac{153}{128}X{}^{\alpha i}\varepsilon{}^{r j}(\Gamma{}^{a}){}_{\eta}{}^{\beta}\nabla_{\zeta}^{t}\big(\nabla_{a}W{}_{\alpha \beta}\big)\\
&-\frac{51}{32}\nabla_{\zeta}^{t}\big(X{}^{\alpha i}\big)\varepsilon{}^{r j}W{}_{\eta}{}^{\beta}W{}_{\alpha \beta} +\frac{51}{32}X{}^{\alpha i}\varepsilon{}^{r j}\nabla_{\zeta}^{t}\big(W{}_{\eta}{}^{\beta}\big)W{}_{\alpha \beta}\\
&+\frac{51}{32}X{}^{\alpha i}\varepsilon{}^{r j}W{}_{\eta}{}^{\beta}\nabla_{\zeta}^{t}\big(W{}_{\alpha \beta}\big) +\frac{51}{128}\nabla_{\zeta}^{t}\big(X{}_{\eta}{}^{i}\big)\varepsilon{}^{r j}W{}^{\alpha \beta}W{}_{\alpha \beta}\\
&-\frac{51}{128}X{}_{\eta}{}^{i}\varepsilon{}^{r j}\nabla_{\zeta}^{t}\big(W{}^{\alpha \beta}\big)W{}_{\alpha \beta} -\frac{51}{128}X{}_{\eta}{}^{i}\varepsilon{}^{r j}W{}^{\alpha \beta}\nabla_{\zeta}^{t}\big(W{}_{\alpha \beta}\big)\\
&-\frac{51}{128}\nabla_{\zeta}^{t}\big(X{}^{\alpha i}\big)\varepsilon{}^{r j}(\Gamma{}^{a}){}_{\alpha}{}^{\beta}\big(\nabla_{a}W{}_{\eta \beta}\big) +\frac{51}{128}X{}^{\alpha i}\varepsilon{}^{r j}(\Gamma{}^{a}){}_{\alpha}{}^{\beta}\nabla_{\zeta}^{t}\big(\nabla_{a}W{}_{\eta \beta}\big)
\end{aligned}
\tag{S5-H0.2-product}
```

Substitution of §3 and the gamma contraction (S5-V02) produce 204 retained covariant contributions from this input. Their exact coefficients and contractions are included in §7; their locations are recorded in [the input-to-result ledger](../../../../../../../references/source_evidence/log/results/gauged_full_fermionic_log/sources/step5/endpoint_term_locations.json).

### Input H1.1

```math
\begin{aligned}
\left.H^{ij}\right|_{\mathrm{H1.1}}={}&\frac{9}{64}W^{-1}X{}^{i j}Y
\end{aligned}
\tag{S5-H1.1-input}
```

Insert the derivative laws in §3 and expand the weighted symmetrization. The retained first derivative is

```math
\begin{aligned}
\left[\left.\nabla_\eta^r H^{ij}\right|_{\mathrm{H1.1}}\right]_{\le3}={}&-\frac{9i}{64}W^{-2}\lambda{}_{\eta}{}^{r}X{}^{i j}Y +\frac{9i}{64}W^{-1}\varepsilon{}^{r i}(\Gamma{}^{a}){}_{\eta}{}^{\alpha}\big(\nabla_{a}\lambda{}_{\alpha}{}^{j}\big)Y\\
&-\frac{9i}{128}W^{-1}\varepsilon{}^{r i}W{}_{\eta \alpha}\lambda{}^{\alpha j}Y -\frac{27}{256}\varepsilon{}^{r i}X{}_{\eta}{}^{j}Y\\
&+\frac{9i}{64}W^{-1}\varepsilon{}^{r j}(\Gamma{}^{a}){}_{\eta}{}^{\alpha}\big(\nabla_{a}\lambda{}_{\alpha}{}^{i}\big)Y -\frac{9i}{128}W^{-1}\varepsilon{}^{r j}W{}_{\eta \alpha}\lambda{}^{\alpha i}Y\\
&-\frac{27}{256}\varepsilon{}^{r j}X{}_{\eta}{}^{i}Y +\frac{9}{8}W^{-1}X{}^{i j}(\Gamma{}^{a}){}_{\eta}{}^{\alpha}\big(\nabla_{a}X{}_{\alpha}{}^{r}\big)\\
&+\frac{9}{8}W^{-1}X{}^{i j}W{}_{\eta}{}^{\alpha}X{}_{\alpha}{}^{r}
\end{aligned}
\tag{S5-H1.1-spinor}
```

Act with the next left derivative on each written factor, with its graded sign:

```math
\begin{aligned}
\nabla_\zeta^t\left[\left.\nabla_\eta^rH^{ij}\right|_{\mathrm{H1.1}}\right]_{\le3}={}&-\frac{9i}{64}\nabla_{\zeta}^{t}\big(W^{-2}\big)\lambda{}_{\eta}{}^{r}X{}^{i j}Y -\frac{9i}{64}W^{-2}\nabla_{\zeta}^{t}\big(\lambda{}_{\eta}{}^{r}\big)X{}^{i j}Y\\
&+\frac{9i}{64}W^{-2}\lambda{}_{\eta}{}^{r}\nabla_{\zeta}^{t}\big(X{}^{i j}\big)Y +\frac{9i}{64}W^{-2}\lambda{}_{\eta}{}^{r}X{}^{i j}\nabla_{\zeta}^{t}\big(Y\big)\\
&+\frac{9i}{64}\nabla_{\zeta}^{t}\big(W^{-1}\big)\varepsilon{}^{r i}(\Gamma{}^{a}){}_{\eta}{}^{\alpha}\big(\nabla_{a}\lambda{}_{\alpha}{}^{j}\big)Y +\frac{9i}{64}W^{-1}\varepsilon{}^{r i}(\Gamma{}^{a}){}_{\eta}{}^{\alpha}\nabla_{\zeta}^{t}\big(\nabla_{a}\lambda{}_{\alpha}{}^{j}\big)Y\\
&-\frac{9i}{64}W^{-1}\varepsilon{}^{r i}(\Gamma{}^{a}){}_{\eta}{}^{\alpha}\big(\nabla_{a}\lambda{}_{\alpha}{}^{j}\big)\nabla_{\zeta}^{t}\big(Y\big) -\frac{9i}{128}\nabla_{\zeta}^{t}\big(W^{-1}\big)\varepsilon{}^{r i}W{}_{\eta \alpha}\lambda{}^{\alpha j}Y\\
&-\frac{9i}{128}W^{-1}\varepsilon{}^{r i}\nabla_{\zeta}^{t}\big(W{}_{\eta \alpha}\big)\lambda{}^{\alpha j}Y -\frac{9i}{128}W^{-1}\varepsilon{}^{r i}W{}_{\eta \alpha}\nabla_{\zeta}^{t}\big(\lambda{}^{\alpha j}\big)Y\\
&+\frac{9i}{128}W^{-1}\varepsilon{}^{r i}W{}_{\eta \alpha}\lambda{}^{\alpha j}\nabla_{\zeta}^{t}\big(Y\big) -\frac{27}{256}W\nabla_{\zeta}^{t}\big(W^{-1}\big)\varepsilon{}^{r i}X{}_{\eta}{}^{j}Y\\
&-\frac{27}{256}\varepsilon{}^{r i}\nabla_{\zeta}^{t}\big(X{}_{\eta}{}^{j}\big)Y +\frac{27}{256}W^{-1}\varepsilon{}^{r i}X{}_{\eta}{}^{j}\nabla_{\zeta}^{t}\big(W\big)Y\\
&+\frac{27}{256}\varepsilon{}^{r i}X{}_{\eta}{}^{j}\nabla_{\zeta}^{t}\big(Y\big) +\frac{9i}{64}\nabla_{\zeta}^{t}\big(W^{-1}\big)\varepsilon{}^{r j}(\Gamma{}^{a}){}_{\eta}{}^{\alpha}\big(\nabla_{a}\lambda{}_{\alpha}{}^{i}\big)Y\\
&+\frac{9i}{64}W^{-1}\varepsilon{}^{r j}(\Gamma{}^{a}){}_{\eta}{}^{\alpha}\nabla_{\zeta}^{t}\big(\nabla_{a}\lambda{}_{\alpha}{}^{i}\big)Y -\frac{9i}{64}W^{-1}\varepsilon{}^{r j}(\Gamma{}^{a}){}_{\eta}{}^{\alpha}\big(\nabla_{a}\lambda{}_{\alpha}{}^{i}\big)\nabla_{\zeta}^{t}\big(Y\big)\\
&-\frac{9i}{128}\nabla_{\zeta}^{t}\big(W^{-1}\big)\varepsilon{}^{r j}W{}_{\eta \alpha}\lambda{}^{\alpha i}Y -\frac{9i}{128}W^{-1}\varepsilon{}^{r j}\nabla_{\zeta}^{t}\big(W{}_{\eta \alpha}\big)\lambda{}^{\alpha i}Y\\
&-\frac{9i}{128}W^{-1}\varepsilon{}^{r j}W{}_{\eta \alpha}\nabla_{\zeta}^{t}\big(\lambda{}^{\alpha i}\big)Y +\frac{9i}{128}W^{-1}\varepsilon{}^{r j}W{}_{\eta \alpha}\lambda{}^{\alpha i}\nabla_{\zeta}^{t}\big(Y\big)\\
&-\frac{27}{256}W\nabla_{\zeta}^{t}\big(W^{-1}\big)\varepsilon{}^{r j}X{}_{\eta}{}^{i}Y -\frac{27}{256}\varepsilon{}^{r j}\nabla_{\zeta}^{t}\big(X{}_{\eta}{}^{i}\big)Y\\
&+\frac{27}{256}W^{-1}\varepsilon{}^{r j}X{}_{\eta}{}^{i}\nabla_{\zeta}^{t}\big(W\big)Y +\frac{27}{256}\varepsilon{}^{r j}X{}_{\eta}{}^{i}\nabla_{\zeta}^{t}\big(Y\big)\\
&+\frac{9}{8}\nabla_{\zeta}^{t}\big(W^{-1}\big)X{}^{i j}(\Gamma{}^{a}){}_{\eta}{}^{\alpha}\big(\nabla_{a}X{}_{\alpha}{}^{r}\big) +\frac{9}{8}W^{-1}\nabla_{\zeta}^{t}\big(X{}^{i j}\big)(\Gamma{}^{a}){}_{\eta}{}^{\alpha}\big(\nabla_{a}X{}_{\alpha}{}^{r}\big)\\
&+\frac{9}{8}W^{-1}X{}^{i j}(\Gamma{}^{a}){}_{\eta}{}^{\alpha}\nabla_{\zeta}^{t}\big(\nabla_{a}X{}_{\alpha}{}^{r}\big) +\frac{9}{8}\nabla_{\zeta}^{t}\big(W^{-1}\big)X{}^{i j}W{}_{\eta}{}^{\alpha}X{}_{\alpha}{}^{r}\\
&+\frac{9}{8}W^{-1}\nabla_{\zeta}^{t}\big(X{}^{i j}\big)W{}_{\eta}{}^{\alpha}X{}_{\alpha}{}^{r} +\frac{9}{8}W^{-1}X{}^{i j}\nabla_{\zeta}^{t}\big(W{}_{\eta}{}^{\alpha}\big)X{}_{\alpha}{}^{r}\\
&+\frac{9}{8}W^{-1}X{}^{i j}W{}_{\eta}{}^{\alpha}\nabla_{\zeta}^{t}\big(X{}_{\alpha}{}^{r}\big)
\end{aligned}
\tag{S5-H1.1-product}
```

Substitution of §3 and the gamma contraction (S5-V02) produce 129 retained covariant contributions from this input. Their exact coefficients and contractions are included in §7; their locations are recorded in [the input-to-result ledger](../../../../../../../references/source_evidence/log/results/gauged_full_fermionic_log/sources/step5/endpoint_term_locations.json).

### Input H1.2

```math
\begin{aligned}
\left.H^{ij}\right|_{\mathrm{H1.2}}={}&-\frac{3i}{8}W^{-1}F{}_{a b}X{}^{a b i j}
\end{aligned}
\tag{S5-H1.2-input}
```

Insert the derivative laws in §3 and expand the weighted symmetrization. The retained first derivative is

```math
\begin{aligned}
\left[\left.\nabla_\eta^r H^{ij}\right|_{\mathrm{H1.2}}\right]_{\le3}={}&-\frac{3}{8}W^{-2}\lambda{}_{\eta}{}^{r}F{}_{a b}X{}^{a b i j} -\frac{3}{16}W^{-1}(\Sigma{}_{a b}){}^{\alpha \beta}(\Gamma{}^{c}){}_{\eta \alpha}\big(\nabla_{c}\lambda{}_{\beta}{}^{r}\big)X{}^{a b i j}\\
&-\frac{3}{16}W^{-1}(\Sigma{}_{a b}){}_{\eta}{}^{\alpha}(\Gamma{}^{c}){}_{\alpha}{}^{\beta}\big(\nabla_{c}\lambda{}_{\beta}{}^{r}\big)X{}^{a b i j} +\frac{3}{32}W^{-1}(\Sigma{}_{a b}){}^{\alpha \beta}W{}_{\eta \alpha}\lambda{}_{\beta}{}^{r}X{}^{a b i j}\\
&-\frac{9}{32}W^{-1}(\Sigma{}_{a b}){}_{\eta}{}^{\alpha}W{}_{\alpha}{}^{\beta}\lambda{}_{\beta}{}^{r}X{}^{a b i j} -\frac{3}{16}W^{-1}(\Sigma{}_{a b}){}^{\alpha \beta}(\Gamma{}^{c}){}_{\eta \beta}\big(\nabla_{c}\lambda{}_{\alpha}{}^{r}\big)X{}^{a b i j}\\
&-\frac{3}{16}W^{-1}(\Sigma{}_{a b}){}^{\alpha}{}_{\eta}(\Gamma{}^{c}){}_{\alpha}{}^{\beta}\big(\nabla_{c}\lambda{}_{\beta}{}^{r}\big)X{}^{a b i j} +\frac{3}{32}W^{-1}(\Sigma{}_{a b}){}^{\alpha \beta}W{}_{\eta \beta}\lambda{}_{\alpha}{}^{r}X{}^{a b i j}\\
&-\frac{9}{32}W^{-1}(\Sigma{}_{a b}){}^{\alpha}{}_{\eta}W{}_{\alpha}{}^{\beta}\lambda{}_{\beta}{}^{r}X{}^{a b i j} -\frac{9}{16}W^{-1}(\Sigma{}_{a b}){}^{\alpha \beta}W{}_{\alpha \beta}\lambda{}_{\eta}{}^{r}X{}^{a b i j}\\
&+\frac{3i}{8}(\Sigma{}_{a b}){}^{\alpha \beta}W{}_{\eta \alpha \beta}{}^{r}X{}^{a b i j} -\frac{3}{16}W^{-1}F{}_{a b}(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r i}W{}_{\eta \gamma}W{}_{\alpha \beta}{}^{\gamma j}\\
&-\frac{9}{32}W^{-1}F{}_{a b}(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r i}W{}_{\alpha \beta}X{}_{\eta}{}^{j} +\frac{3}{8}W^{-1}F{}_{a b}(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r i}(\Gamma{}^{c}){}_{\eta}{}^{\gamma}\big(\nabla_{c}W{}_{\alpha \beta \gamma}{}^{j}\big)\\
&-\frac{9}{32}W^{-1}F{}_{a b}(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r i}W{}_{\alpha}{}^{\gamma}W{}_{\beta \eta \gamma}{}^{j} -\frac{3}{32}W^{-1}F{}_{a b}(\Sigma{}^{a b}){}_{\eta}{}^{\alpha}\varepsilon{}^{r i}W{}^{\beta \gamma}W{}_{\alpha \beta \gamma}{}^{j}\\
&+\frac{3}{64}W^{-1}F{}_{a b}(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r i}W{}_{\eta \alpha}X{}_{\beta}{}^{j} +\frac{9}{64}W^{-1}F{}_{a b}(\Sigma{}^{a b}){}_{\eta}{}^{\alpha}\varepsilon{}^{r i}W{}_{\alpha \beta}X{}^{\beta j}\\
&+\frac{3}{16}W^{-1}F{}_{a b}(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r i}(\Gamma{}^{c}){}_{\alpha}{}^{\gamma}\big(\nabla_{c}W{}_{\beta \eta \gamma}{}^{j}\big) -\frac{3}{32}W^{-1}F{}_{a b}(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r i}(\Gamma{}^{c}){}_{\eta \alpha}\big(\nabla_{c}X{}_{\beta}{}^{j}\big)\\
&+\frac{3}{32}W^{-1}F{}_{a b}(\Sigma{}^{a b}){}_{\eta}{}^{\alpha}\varepsilon{}^{r i}(\Gamma{}^{c}){}_{\alpha \beta}\big(\nabla_{c}X{}^{\beta j}\big) -\frac{9}{32}W^{-1}F{}_{a b}(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r i}W{}_{\beta}{}^{\gamma}W{}_{\alpha \eta \gamma}{}^{j}\\
&-\frac{3}{32}W^{-1}F{}_{a b}(\Sigma{}^{a b}){}^{\alpha}{}_{\eta}\varepsilon{}^{r i}W{}^{\beta \gamma}W{}_{\alpha \beta \gamma}{}^{j} +\frac{3}{64}W^{-1}F{}_{a b}(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r i}W{}_{\eta \beta}X{}_{\alpha}{}^{j}\\
&+\frac{9}{64}W^{-1}F{}_{a b}(\Sigma{}^{a b}){}^{\alpha}{}_{\eta}\varepsilon{}^{r i}W{}_{\alpha \beta}X{}^{\beta j} +\frac{3}{16}W^{-1}F{}_{a b}(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r i}(\Gamma{}^{c}){}_{\beta}{}^{\gamma}\big(\nabla_{c}W{}_{\alpha \eta \gamma}{}^{j}\big)\\
&-\frac{3}{32}W^{-1}F{}_{a b}(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r i}(\Gamma{}^{c}){}_{\eta \beta}\big(\nabla_{c}X{}_{\alpha}{}^{j}\big) +\frac{3}{32}W^{-1}F{}_{a b}(\Sigma{}^{a b}){}^{\alpha}{}_{\eta}\varepsilon{}^{r i}(\Gamma{}^{c}){}_{\alpha \beta}\big(\nabla_{c}X{}^{\beta j}\big)\\
&-\frac{3}{16}W^{-1}F{}_{a b}(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r j}W{}_{\eta \gamma}W{}_{\alpha \beta}{}^{\gamma i} -\frac{9}{32}W^{-1}F{}_{a b}(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r j}W{}_{\alpha \beta}X{}_{\eta}{}^{i}\\
&+\frac{3}{8}W^{-1}F{}_{a b}(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r j}(\Gamma{}^{c}){}_{\eta}{}^{\gamma}\big(\nabla_{c}W{}_{\alpha \beta \gamma}{}^{i}\big) -\frac{9}{32}W^{-1}F{}_{a b}(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r j}W{}_{\alpha}{}^{\gamma}W{}_{\beta \eta \gamma}{}^{i}\\
&-\frac{3}{32}W^{-1}F{}_{a b}(\Sigma{}^{a b}){}_{\eta}{}^{\alpha}\varepsilon{}^{r j}W{}^{\beta \gamma}W{}_{\alpha \beta \gamma}{}^{i} +\frac{3}{64}W^{-1}F{}_{a b}(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r j}W{}_{\eta \alpha}X{}_{\beta}{}^{i}\\
&+\frac{9}{64}W^{-1}F{}_{a b}(\Sigma{}^{a b}){}_{\eta}{}^{\alpha}\varepsilon{}^{r j}W{}_{\alpha \beta}X{}^{\beta i} +\frac{3}{16}W^{-1}F{}_{a b}(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r j}(\Gamma{}^{c}){}_{\alpha}{}^{\gamma}\big(\nabla_{c}W{}_{\beta \eta \gamma}{}^{i}\big)\\
&-\frac{3}{32}W^{-1}F{}_{a b}(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r j}(\Gamma{}^{c}){}_{\eta \alpha}\big(\nabla_{c}X{}_{\beta}{}^{i}\big) +\frac{3}{32}W^{-1}F{}_{a b}(\Sigma{}^{a b}){}_{\eta}{}^{\alpha}\varepsilon{}^{r j}(\Gamma{}^{c}){}_{\alpha \beta}\big(\nabla_{c}X{}^{\beta i}\big)\\
&-\frac{9}{32}W^{-1}F{}_{a b}(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r j}W{}_{\beta}{}^{\gamma}W{}_{\alpha \eta \gamma}{}^{i} -\frac{3}{32}W^{-1}F{}_{a b}(\Sigma{}^{a b}){}^{\alpha}{}_{\eta}\varepsilon{}^{r j}W{}^{\beta \gamma}W{}_{\alpha \beta \gamma}{}^{i}\\
&+\frac{3}{64}W^{-1}F{}_{a b}(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r j}W{}_{\eta \beta}X{}_{\alpha}{}^{i} +\frac{9}{64}W^{-1}F{}_{a b}(\Sigma{}^{a b}){}^{\alpha}{}_{\eta}\varepsilon{}^{r j}W{}_{\alpha \beta}X{}^{\beta i}\\
&+\frac{3}{16}W^{-1}F{}_{a b}(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r j}(\Gamma{}^{c}){}_{\beta}{}^{\gamma}\big(\nabla_{c}W{}_{\alpha \eta \gamma}{}^{i}\big) -\frac{3}{32}W^{-1}F{}_{a b}(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r j}(\Gamma{}^{c}){}_{\eta \beta}\big(\nabla_{c}X{}_{\alpha}{}^{i}\big)\\
&+\frac{3}{32}W^{-1}F{}_{a b}(\Sigma{}^{a b}){}^{\alpha}{}_{\eta}\varepsilon{}^{r j}(\Gamma{}^{c}){}_{\alpha \beta}\big(\nabla_{c}X{}^{\beta i}\big)
\end{aligned}
\tag{S5-H1.2-spinor}
```

Act with the next left derivative on each written factor, with its graded sign:

```math
\begin{aligned}
\nabla_\zeta^t\left[\left.\nabla_\eta^rH^{ij}\right|_{\mathrm{H1.2}}\right]_{\le3}={}&-\frac{3}{8}\nabla_{\zeta}^{t}\big(W^{-2}\big)\lambda{}_{\eta}{}^{r}F{}_{a b}X{}^{a b i j} -\frac{3}{8}W^{-2}\nabla_{\zeta}^{t}\big(\lambda{}_{\eta}{}^{r}\big)F{}_{a b}X{}^{a b i j}\\
&+\frac{3}{8}W^{-2}\lambda{}_{\eta}{}^{r}\nabla_{\zeta}^{t}\big(F{}_{a b}\big)X{}^{a b i j} +\frac{3}{8}W^{-2}\lambda{}_{\eta}{}^{r}F{}_{a b}\nabla_{\zeta}^{t}\big(X{}^{a b i j}\big)\\
&-\frac{3}{16}\nabla_{\zeta}^{t}\big(W^{-1}\big)(\Sigma{}_{a b}){}^{\alpha \beta}(\Gamma{}^{c}){}_{\eta \alpha}\big(\nabla_{c}\lambda{}_{\beta}{}^{r}\big)X{}^{a b i j} -\frac{3}{16}W^{-1}(\Sigma{}_{a b}){}^{\alpha \beta}(\Gamma{}^{c}){}_{\eta \alpha}\nabla_{\zeta}^{t}\big(\nabla_{c}\lambda{}_{\beta}{}^{r}\big)X{}^{a b i j}\\
&+\frac{3}{16}W^{-1}(\Sigma{}_{a b}){}^{\alpha \beta}(\Gamma{}^{c}){}_{\eta \alpha}\big(\nabla_{c}\lambda{}_{\beta}{}^{r}\big)\nabla_{\zeta}^{t}\big(X{}^{a b i j}\big) -\frac{3}{16}\nabla_{\zeta}^{t}\big(W^{-1}\big)(\Sigma{}_{a b}){}_{\eta}{}^{\alpha}(\Gamma{}^{c}){}_{\alpha}{}^{\beta}\big(\nabla_{c}\lambda{}_{\beta}{}^{r}\big)X{}^{a b i j}\\
&-\frac{3}{16}W^{-1}(\Sigma{}_{a b}){}_{\eta}{}^{\alpha}(\Gamma{}^{c}){}_{\alpha}{}^{\beta}\nabla_{\zeta}^{t}\big(\nabla_{c}\lambda{}_{\beta}{}^{r}\big)X{}^{a b i j} +\frac{3}{16}W^{-1}(\Sigma{}_{a b}){}_{\eta}{}^{\alpha}(\Gamma{}^{c}){}_{\alpha}{}^{\beta}\big(\nabla_{c}\lambda{}_{\beta}{}^{r}\big)\nabla_{\zeta}^{t}\big(X{}^{a b i j}\big)\\
&+\frac{3}{32}\nabla_{\zeta}^{t}\big(W^{-1}\big)(\Sigma{}_{a b}){}^{\alpha \beta}W{}_{\eta \alpha}\lambda{}_{\beta}{}^{r}X{}^{a b i j} +\frac{3}{32}W^{-1}(\Sigma{}_{a b}){}^{\alpha \beta}\nabla_{\zeta}^{t}\big(W{}_{\eta \alpha}\big)\lambda{}_{\beta}{}^{r}X{}^{a b i j}\\
&+\frac{3}{32}W^{-1}(\Sigma{}_{a b}){}^{\alpha \beta}W{}_{\eta \alpha}\nabla_{\zeta}^{t}\big(\lambda{}_{\beta}{}^{r}\big)X{}^{a b i j} -\frac{3}{32}W^{-1}(\Sigma{}_{a b}){}^{\alpha \beta}W{}_{\eta \alpha}\lambda{}_{\beta}{}^{r}\nabla_{\zeta}^{t}\big(X{}^{a b i j}\big)\\
&-\frac{9}{32}\nabla_{\zeta}^{t}\big(W^{-1}\big)(\Sigma{}_{a b}){}_{\eta}{}^{\alpha}W{}_{\alpha}{}^{\beta}\lambda{}_{\beta}{}^{r}X{}^{a b i j} -\frac{9}{32}W^{-1}(\Sigma{}_{a b}){}_{\eta}{}^{\alpha}\nabla_{\zeta}^{t}\big(W{}_{\alpha}{}^{\beta}\big)\lambda{}_{\beta}{}^{r}X{}^{a b i j}\\
&-\frac{9}{32}W^{-1}(\Sigma{}_{a b}){}_{\eta}{}^{\alpha}W{}_{\alpha}{}^{\beta}\nabla_{\zeta}^{t}\big(\lambda{}_{\beta}{}^{r}\big)X{}^{a b i j} +\frac{9}{32}W^{-1}(\Sigma{}_{a b}){}_{\eta}{}^{\alpha}W{}_{\alpha}{}^{\beta}\lambda{}_{\beta}{}^{r}\nabla_{\zeta}^{t}\big(X{}^{a b i j}\big)\\
&-\frac{3}{16}\nabla_{\zeta}^{t}\big(W^{-1}\big)(\Sigma{}_{a b}){}^{\alpha \beta}(\Gamma{}^{c}){}_{\eta \beta}\big(\nabla_{c}\lambda{}_{\alpha}{}^{r}\big)X{}^{a b i j} -\frac{3}{16}W^{-1}(\Sigma{}_{a b}){}^{\alpha \beta}(\Gamma{}^{c}){}_{\eta \beta}\nabla_{\zeta}^{t}\big(\nabla_{c}\lambda{}_{\alpha}{}^{r}\big)X{}^{a b i j}\\
&+\frac{3}{16}W^{-1}(\Sigma{}_{a b}){}^{\alpha \beta}(\Gamma{}^{c}){}_{\eta \beta}\big(\nabla_{c}\lambda{}_{\alpha}{}^{r}\big)\nabla_{\zeta}^{t}\big(X{}^{a b i j}\big) -\frac{3}{16}\nabla_{\zeta}^{t}\big(W^{-1}\big)(\Sigma{}_{a b}){}^{\alpha}{}_{\eta}(\Gamma{}^{c}){}_{\alpha}{}^{\beta}\big(\nabla_{c}\lambda{}_{\beta}{}^{r}\big)X{}^{a b i j}\\
&-\frac{3}{16}W^{-1}(\Sigma{}_{a b}){}^{\alpha}{}_{\eta}(\Gamma{}^{c}){}_{\alpha}{}^{\beta}\nabla_{\zeta}^{t}\big(\nabla_{c}\lambda{}_{\beta}{}^{r}\big)X{}^{a b i j} +\frac{3}{16}W^{-1}(\Sigma{}_{a b}){}^{\alpha}{}_{\eta}(\Gamma{}^{c}){}_{\alpha}{}^{\beta}\big(\nabla_{c}\lambda{}_{\beta}{}^{r}\big)\nabla_{\zeta}^{t}\big(X{}^{a b i j}\big)\\
&+\frac{3}{32}\nabla_{\zeta}^{t}\big(W^{-1}\big)(\Sigma{}_{a b}){}^{\alpha \beta}W{}_{\eta \beta}\lambda{}_{\alpha}{}^{r}X{}^{a b i j} +\frac{3}{32}W^{-1}(\Sigma{}_{a b}){}^{\alpha \beta}\nabla_{\zeta}^{t}\big(W{}_{\eta \beta}\big)\lambda{}_{\alpha}{}^{r}X{}^{a b i j}\\
&+\frac{3}{32}W^{-1}(\Sigma{}_{a b}){}^{\alpha \beta}W{}_{\eta \beta}\nabla_{\zeta}^{t}\big(\lambda{}_{\alpha}{}^{r}\big)X{}^{a b i j} -\frac{3}{32}W^{-1}(\Sigma{}_{a b}){}^{\alpha \beta}W{}_{\eta \beta}\lambda{}_{\alpha}{}^{r}\nabla_{\zeta}^{t}\big(X{}^{a b i j}\big)\\
&-\frac{9}{32}\nabla_{\zeta}^{t}\big(W^{-1}\big)(\Sigma{}_{a b}){}^{\alpha}{}_{\eta}W{}_{\alpha}{}^{\beta}\lambda{}_{\beta}{}^{r}X{}^{a b i j} -\frac{9}{32}W^{-1}(\Sigma{}_{a b}){}^{\alpha}{}_{\eta}\nabla_{\zeta}^{t}\big(W{}_{\alpha}{}^{\beta}\big)\lambda{}_{\beta}{}^{r}X{}^{a b i j}\\
&-\frac{9}{32}W^{-1}(\Sigma{}_{a b}){}^{\alpha}{}_{\eta}W{}_{\alpha}{}^{\beta}\nabla_{\zeta}^{t}\big(\lambda{}_{\beta}{}^{r}\big)X{}^{a b i j} +\frac{9}{32}W^{-1}(\Sigma{}_{a b}){}^{\alpha}{}_{\eta}W{}_{\alpha}{}^{\beta}\lambda{}_{\beta}{}^{r}\nabla_{\zeta}^{t}\big(X{}^{a b i j}\big)\\
&-\frac{9}{16}\nabla_{\zeta}^{t}\big(W^{-1}\big)(\Sigma{}_{a b}){}^{\alpha \beta}W{}_{\alpha \beta}\lambda{}_{\eta}{}^{r}X{}^{a b i j} -\frac{9}{16}W^{-1}(\Sigma{}_{a b}){}^{\alpha \beta}\nabla_{\zeta}^{t}\big(W{}_{\alpha \beta}\big)\lambda{}_{\eta}{}^{r}X{}^{a b i j}\\
&-\frac{9}{16}W^{-1}(\Sigma{}_{a b}){}^{\alpha \beta}W{}_{\alpha \beta}\nabla_{\zeta}^{t}\big(\lambda{}_{\eta}{}^{r}\big)X{}^{a b i j} +\frac{9}{16}W^{-1}(\Sigma{}_{a b}){}^{\alpha \beta}W{}_{\alpha \beta}\lambda{}_{\eta}{}^{r}\nabla_{\zeta}^{t}\big(X{}^{a b i j}\big)\\
&+\frac{3i}{8}W\nabla_{\zeta}^{t}\big(W^{-1}\big)(\Sigma{}_{a b}){}^{\alpha \beta}W{}_{\eta \alpha \beta}{}^{r}X{}^{a b i j} +\frac{3i}{8}(\Sigma{}_{a b}){}^{\alpha \beta}\nabla_{\zeta}^{t}\big(W{}_{\eta \alpha \beta}{}^{r}\big)X{}^{a b i j}\\
&-\frac{3i}{8}W^{-1}(\Sigma{}_{a b}){}^{\alpha \beta}W{}_{\eta \alpha \beta}{}^{r}\nabla_{\zeta}^{t}\big(W\big)X{}^{a b i j} -\frac{3i}{8}(\Sigma{}_{a b}){}^{\alpha \beta}W{}_{\eta \alpha \beta}{}^{r}\nabla_{\zeta}^{t}\big(X{}^{a b i j}\big)\\
&-\frac{3}{16}\nabla_{\zeta}^{t}\big(W^{-1}\big)F{}_{a b}(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r i}W{}_{\eta \gamma}W{}_{\alpha \beta}{}^{\gamma j} -\frac{3}{16}W^{-1}\nabla_{\zeta}^{t}\big(F{}_{a b}\big)(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r i}W{}_{\eta \gamma}W{}_{\alpha \beta}{}^{\gamma j}\\
&-\frac{3}{16}W^{-1}F{}_{a b}(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r i}\nabla_{\zeta}^{t}\big(W{}_{\eta \gamma}\big)W{}_{\alpha \beta}{}^{\gamma j} -\frac{3}{16}W^{-1}F{}_{a b}(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r i}W{}_{\eta \gamma}\nabla_{\zeta}^{t}\big(W{}_{\alpha \beta}{}^{\gamma j}\big)\\
&-\frac{9}{32}\nabla_{\zeta}^{t}\big(W^{-1}\big)F{}_{a b}(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r i}W{}_{\alpha \beta}X{}_{\eta}{}^{j} -\frac{9}{32}W^{-1}\nabla_{\zeta}^{t}\big(F{}_{a b}\big)(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r i}W{}_{\alpha \beta}X{}_{\eta}{}^{j}\\
&-\frac{9}{32}W^{-1}F{}_{a b}(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r i}\nabla_{\zeta}^{t}\big(W{}_{\alpha \beta}\big)X{}_{\eta}{}^{j} -\frac{9}{32}W^{-1}F{}_{a b}(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r i}W{}_{\alpha \beta}\nabla_{\zeta}^{t}\big(X{}_{\eta}{}^{j}\big)\\
&+\frac{3}{8}\nabla_{\zeta}^{t}\big(W^{-1}\big)F{}_{a b}(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r i}(\Gamma{}^{c}){}_{\eta}{}^{\gamma}\big(\nabla_{c}W{}_{\alpha \beta \gamma}{}^{j}\big) +\frac{3}{8}W^{-1}\nabla_{\zeta}^{t}\big(F{}_{a b}\big)(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r i}(\Gamma{}^{c}){}_{\eta}{}^{\gamma}\big(\nabla_{c}W{}_{\alpha \beta \gamma}{}^{j}\big)\\
&+\frac{3}{8}W^{-1}F{}_{a b}(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r i}(\Gamma{}^{c}){}_{\eta}{}^{\gamma}\nabla_{\zeta}^{t}\big(\nabla_{c}W{}_{\alpha \beta \gamma}{}^{j}\big) -\frac{9}{32}\nabla_{\zeta}^{t}\big(W^{-1}\big)F{}_{a b}(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r i}W{}_{\alpha}{}^{\gamma}W{}_{\beta \eta \gamma}{}^{j}\\
&-\frac{9}{32}W^{-1}\nabla_{\zeta}^{t}\big(F{}_{a b}\big)(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r i}W{}_{\alpha}{}^{\gamma}W{}_{\beta \eta \gamma}{}^{j} -\frac{9}{32}W^{-1}F{}_{a b}(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r i}\nabla_{\zeta}^{t}\big(W{}_{\alpha}{}^{\gamma}\big)W{}_{\beta \eta \gamma}{}^{j}\\
&-\frac{9}{32}W^{-1}F{}_{a b}(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r i}W{}_{\alpha}{}^{\gamma}\nabla_{\zeta}^{t}\big(W{}_{\beta \eta \gamma}{}^{j}\big) -\frac{3}{32}\nabla_{\zeta}^{t}\big(W^{-1}\big)F{}_{a b}(\Sigma{}^{a b}){}_{\eta}{}^{\alpha}\varepsilon{}^{r i}W{}^{\beta \gamma}W{}_{\alpha \beta \gamma}{}^{j}\\
&-\frac{3}{32}W^{-1}\nabla_{\zeta}^{t}\big(F{}_{a b}\big)(\Sigma{}^{a b}){}_{\eta}{}^{\alpha}\varepsilon{}^{r i}W{}^{\beta \gamma}W{}_{\alpha \beta \gamma}{}^{j} -\frac{3}{32}W^{-1}F{}_{a b}(\Sigma{}^{a b}){}_{\eta}{}^{\alpha}\varepsilon{}^{r i}\nabla_{\zeta}^{t}\big(W{}^{\beta \gamma}\big)W{}_{\alpha \beta \gamma}{}^{j}\\
&-\frac{3}{32}W^{-1}F{}_{a b}(\Sigma{}^{a b}){}_{\eta}{}^{\alpha}\varepsilon{}^{r i}W{}^{\beta \gamma}\nabla_{\zeta}^{t}\big(W{}_{\alpha \beta \gamma}{}^{j}\big) +\frac{3}{64}\nabla_{\zeta}^{t}\big(W^{-1}\big)F{}_{a b}(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r i}W{}_{\eta \alpha}X{}_{\beta}{}^{j}\\
&+\frac{3}{64}W^{-1}\nabla_{\zeta}^{t}\big(F{}_{a b}\big)(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r i}W{}_{\eta \alpha}X{}_{\beta}{}^{j} +\frac{3}{64}W^{-1}F{}_{a b}(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r i}\nabla_{\zeta}^{t}\big(W{}_{\eta \alpha}\big)X{}_{\beta}{}^{j}\\
&+\frac{3}{64}W^{-1}F{}_{a b}(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r i}W{}_{\eta \alpha}\nabla_{\zeta}^{t}\big(X{}_{\beta}{}^{j}\big) +\frac{9}{64}\nabla_{\zeta}^{t}\big(W^{-1}\big)F{}_{a b}(\Sigma{}^{a b}){}_{\eta}{}^{\alpha}\varepsilon{}^{r i}W{}_{\alpha \beta}X{}^{\beta j}\\
&+\frac{9}{64}W^{-1}\nabla_{\zeta}^{t}\big(F{}_{a b}\big)(\Sigma{}^{a b}){}_{\eta}{}^{\alpha}\varepsilon{}^{r i}W{}_{\alpha \beta}X{}^{\beta j} +\frac{9}{64}W^{-1}F{}_{a b}(\Sigma{}^{a b}){}_{\eta}{}^{\alpha}\varepsilon{}^{r i}\nabla_{\zeta}^{t}\big(W{}_{\alpha \beta}\big)X{}^{\beta j}\\
&+\frac{9}{64}W^{-1}F{}_{a b}(\Sigma{}^{a b}){}_{\eta}{}^{\alpha}\varepsilon{}^{r i}W{}_{\alpha \beta}\nabla_{\zeta}^{t}\big(X{}^{\beta j}\big) +\frac{3}{16}\nabla_{\zeta}^{t}\big(W^{-1}\big)F{}_{a b}(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r i}(\Gamma{}^{c}){}_{\alpha}{}^{\gamma}\big(\nabla_{c}W{}_{\beta \eta \gamma}{}^{j}\big)\\
&+\frac{3}{16}W^{-1}\nabla_{\zeta}^{t}\big(F{}_{a b}\big)(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r i}(\Gamma{}^{c}){}_{\alpha}{}^{\gamma}\big(\nabla_{c}W{}_{\beta \eta \gamma}{}^{j}\big) +\frac{3}{16}W^{-1}F{}_{a b}(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r i}(\Gamma{}^{c}){}_{\alpha}{}^{\gamma}\nabla_{\zeta}^{t}\big(\nabla_{c}W{}_{\beta \eta \gamma}{}^{j}\big)\\
&-\frac{3}{32}\nabla_{\zeta}^{t}\big(W^{-1}\big)F{}_{a b}(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r i}(\Gamma{}^{c}){}_{\eta \alpha}\big(\nabla_{c}X{}_{\beta}{}^{j}\big) -\frac{3}{32}W^{-1}\nabla_{\zeta}^{t}\big(F{}_{a b}\big)(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r i}(\Gamma{}^{c}){}_{\eta \alpha}\big(\nabla_{c}X{}_{\beta}{}^{j}\big)\\
&-\frac{3}{32}W^{-1}F{}_{a b}(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r i}(\Gamma{}^{c}){}_{\eta \alpha}\nabla_{\zeta}^{t}\big(\nabla_{c}X{}_{\beta}{}^{j}\big) +\frac{3}{32}\nabla_{\zeta}^{t}\big(W^{-1}\big)F{}_{a b}(\Sigma{}^{a b}){}_{\eta}{}^{\alpha}\varepsilon{}^{r i}(\Gamma{}^{c}){}_{\alpha \beta}\big(\nabla_{c}X{}^{\beta j}\big)\\
&+\frac{3}{32}W^{-1}\nabla_{\zeta}^{t}\big(F{}_{a b}\big)(\Sigma{}^{a b}){}_{\eta}{}^{\alpha}\varepsilon{}^{r i}(\Gamma{}^{c}){}_{\alpha \beta}\big(\nabla_{c}X{}^{\beta j}\big) +\frac{3}{32}W^{-1}F{}_{a b}(\Sigma{}^{a b}){}_{\eta}{}^{\alpha}\varepsilon{}^{r i}(\Gamma{}^{c}){}_{\alpha \beta}\nabla_{\zeta}^{t}\big(\nabla_{c}X{}^{\beta j}\big)\\
&-\frac{9}{32}\nabla_{\zeta}^{t}\big(W^{-1}\big)F{}_{a b}(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r i}W{}_{\beta}{}^{\gamma}W{}_{\alpha \eta \gamma}{}^{j} -\frac{9}{32}W^{-1}\nabla_{\zeta}^{t}\big(F{}_{a b}\big)(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r i}W{}_{\beta}{}^{\gamma}W{}_{\alpha \eta \gamma}{}^{j}\\
&-\frac{9}{32}W^{-1}F{}_{a b}(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r i}\nabla_{\zeta}^{t}\big(W{}_{\beta}{}^{\gamma}\big)W{}_{\alpha \eta \gamma}{}^{j} -\frac{9}{32}W^{-1}F{}_{a b}(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r i}W{}_{\beta}{}^{\gamma}\nabla_{\zeta}^{t}\big(W{}_{\alpha \eta \gamma}{}^{j}\big)\\
&-\frac{3}{32}\nabla_{\zeta}^{t}\big(W^{-1}\big)F{}_{a b}(\Sigma{}^{a b}){}^{\alpha}{}_{\eta}\varepsilon{}^{r i}W{}^{\beta \gamma}W{}_{\alpha \beta \gamma}{}^{j} -\frac{3}{32}W^{-1}\nabla_{\zeta}^{t}\big(F{}_{a b}\big)(\Sigma{}^{a b}){}^{\alpha}{}_{\eta}\varepsilon{}^{r i}W{}^{\beta \gamma}W{}_{\alpha \beta \gamma}{}^{j}\\
&-\frac{3}{32}W^{-1}F{}_{a b}(\Sigma{}^{a b}){}^{\alpha}{}_{\eta}\varepsilon{}^{r i}\nabla_{\zeta}^{t}\big(W{}^{\beta \gamma}\big)W{}_{\alpha \beta \gamma}{}^{j} -\frac{3}{32}W^{-1}F{}_{a b}(\Sigma{}^{a b}){}^{\alpha}{}_{\eta}\varepsilon{}^{r i}W{}^{\beta \gamma}\nabla_{\zeta}^{t}\big(W{}_{\alpha \beta \gamma}{}^{j}\big)\\
&+\frac{3}{64}\nabla_{\zeta}^{t}\big(W^{-1}\big)F{}_{a b}(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r i}W{}_{\eta \beta}X{}_{\alpha}{}^{j} +\frac{3}{64}W^{-1}\nabla_{\zeta}^{t}\big(F{}_{a b}\big)(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r i}W{}_{\eta \beta}X{}_{\alpha}{}^{j}\\
&+\frac{3}{64}W^{-1}F{}_{a b}(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r i}\nabla_{\zeta}^{t}\big(W{}_{\eta \beta}\big)X{}_{\alpha}{}^{j} +\frac{3}{64}W^{-1}F{}_{a b}(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r i}W{}_{\eta \beta}\nabla_{\zeta}^{t}\big(X{}_{\alpha}{}^{j}\big)\\
&+\frac{9}{64}\nabla_{\zeta}^{t}\big(W^{-1}\big)F{}_{a b}(\Sigma{}^{a b}){}^{\alpha}{}_{\eta}\varepsilon{}^{r i}W{}_{\alpha \beta}X{}^{\beta j} +\frac{9}{64}W^{-1}\nabla_{\zeta}^{t}\big(F{}_{a b}\big)(\Sigma{}^{a b}){}^{\alpha}{}_{\eta}\varepsilon{}^{r i}W{}_{\alpha \beta}X{}^{\beta j}\\
&+\frac{9}{64}W^{-1}F{}_{a b}(\Sigma{}^{a b}){}^{\alpha}{}_{\eta}\varepsilon{}^{r i}\nabla_{\zeta}^{t}\big(W{}_{\alpha \beta}\big)X{}^{\beta j} +\frac{9}{64}W^{-1}F{}_{a b}(\Sigma{}^{a b}){}^{\alpha}{}_{\eta}\varepsilon{}^{r i}W{}_{\alpha \beta}\nabla_{\zeta}^{t}\big(X{}^{\beta j}\big)\\
&+\frac{3}{16}\nabla_{\zeta}^{t}\big(W^{-1}\big)F{}_{a b}(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r i}(\Gamma{}^{c}){}_{\beta}{}^{\gamma}\big(\nabla_{c}W{}_{\alpha \eta \gamma}{}^{j}\big) +\frac{3}{16}W^{-1}\nabla_{\zeta}^{t}\big(F{}_{a b}\big)(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r i}(\Gamma{}^{c}){}_{\beta}{}^{\gamma}\big(\nabla_{c}W{}_{\alpha \eta \gamma}{}^{j}\big)\\
&+\frac{3}{16}W^{-1}F{}_{a b}(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r i}(\Gamma{}^{c}){}_{\beta}{}^{\gamma}\nabla_{\zeta}^{t}\big(\nabla_{c}W{}_{\alpha \eta \gamma}{}^{j}\big) -\frac{3}{32}\nabla_{\zeta}^{t}\big(W^{-1}\big)F{}_{a b}(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r i}(\Gamma{}^{c}){}_{\eta \beta}\big(\nabla_{c}X{}_{\alpha}{}^{j}\big)\\
&-\frac{3}{32}W^{-1}\nabla_{\zeta}^{t}\big(F{}_{a b}\big)(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r i}(\Gamma{}^{c}){}_{\eta \beta}\big(\nabla_{c}X{}_{\alpha}{}^{j}\big) -\frac{3}{32}W^{-1}F{}_{a b}(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r i}(\Gamma{}^{c}){}_{\eta \beta}\nabla_{\zeta}^{t}\big(\nabla_{c}X{}_{\alpha}{}^{j}\big)\\
&+\frac{3}{32}\nabla_{\zeta}^{t}\big(W^{-1}\big)F{}_{a b}(\Sigma{}^{a b}){}^{\alpha}{}_{\eta}\varepsilon{}^{r i}(\Gamma{}^{c}){}_{\alpha \beta}\big(\nabla_{c}X{}^{\beta j}\big) +\frac{3}{32}W^{-1}\nabla_{\zeta}^{t}\big(F{}_{a b}\big)(\Sigma{}^{a b}){}^{\alpha}{}_{\eta}\varepsilon{}^{r i}(\Gamma{}^{c}){}_{\alpha \beta}\big(\nabla_{c}X{}^{\beta j}\big)
\end{aligned}
\tag{S5-H1.2-product-1}
```

```math
\begin{aligned}
&+\frac{3}{32}W^{-1}F{}_{a b}(\Sigma{}^{a b}){}^{\alpha}{}_{\eta}\varepsilon{}^{r i}(\Gamma{}^{c}){}_{\alpha \beta}\nabla_{\zeta}^{t}\big(\nabla_{c}X{}^{\beta j}\big) -\frac{3}{16}\nabla_{\zeta}^{t}\big(W^{-1}\big)F{}_{a b}(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r j}W{}_{\eta \gamma}W{}_{\alpha \beta}{}^{\gamma i}\\
&-\frac{3}{16}W^{-1}\nabla_{\zeta}^{t}\big(F{}_{a b}\big)(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r j}W{}_{\eta \gamma}W{}_{\alpha \beta}{}^{\gamma i} -\frac{3}{16}W^{-1}F{}_{a b}(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r j}\nabla_{\zeta}^{t}\big(W{}_{\eta \gamma}\big)W{}_{\alpha \beta}{}^{\gamma i}\\
&-\frac{3}{16}W^{-1}F{}_{a b}(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r j}W{}_{\eta \gamma}\nabla_{\zeta}^{t}\big(W{}_{\alpha \beta}{}^{\gamma i}\big) -\frac{9}{32}\nabla_{\zeta}^{t}\big(W^{-1}\big)F{}_{a b}(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r j}W{}_{\alpha \beta}X{}_{\eta}{}^{i}\\
&-\frac{9}{32}W^{-1}\nabla_{\zeta}^{t}\big(F{}_{a b}\big)(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r j}W{}_{\alpha \beta}X{}_{\eta}{}^{i} -\frac{9}{32}W^{-1}F{}_{a b}(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r j}\nabla_{\zeta}^{t}\big(W{}_{\alpha \beta}\big)X{}_{\eta}{}^{i}\\
&-\frac{9}{32}W^{-1}F{}_{a b}(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r j}W{}_{\alpha \beta}\nabla_{\zeta}^{t}\big(X{}_{\eta}{}^{i}\big) +\frac{3}{8}\nabla_{\zeta}^{t}\big(W^{-1}\big)F{}_{a b}(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r j}(\Gamma{}^{c}){}_{\eta}{}^{\gamma}\big(\nabla_{c}W{}_{\alpha \beta \gamma}{}^{i}\big)\\
&+\frac{3}{8}W^{-1}\nabla_{\zeta}^{t}\big(F{}_{a b}\big)(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r j}(\Gamma{}^{c}){}_{\eta}{}^{\gamma}\big(\nabla_{c}W{}_{\alpha \beta \gamma}{}^{i}\big) +\frac{3}{8}W^{-1}F{}_{a b}(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r j}(\Gamma{}^{c}){}_{\eta}{}^{\gamma}\nabla_{\zeta}^{t}\big(\nabla_{c}W{}_{\alpha \beta \gamma}{}^{i}\big)\\
&-\frac{9}{32}\nabla_{\zeta}^{t}\big(W^{-1}\big)F{}_{a b}(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r j}W{}_{\alpha}{}^{\gamma}W{}_{\beta \eta \gamma}{}^{i} -\frac{9}{32}W^{-1}\nabla_{\zeta}^{t}\big(F{}_{a b}\big)(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r j}W{}_{\alpha}{}^{\gamma}W{}_{\beta \eta \gamma}{}^{i}\\
&-\frac{9}{32}W^{-1}F{}_{a b}(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r j}\nabla_{\zeta}^{t}\big(W{}_{\alpha}{}^{\gamma}\big)W{}_{\beta \eta \gamma}{}^{i} -\frac{9}{32}W^{-1}F{}_{a b}(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r j}W{}_{\alpha}{}^{\gamma}\nabla_{\zeta}^{t}\big(W{}_{\beta \eta \gamma}{}^{i}\big)\\
&-\frac{3}{32}\nabla_{\zeta}^{t}\big(W^{-1}\big)F{}_{a b}(\Sigma{}^{a b}){}_{\eta}{}^{\alpha}\varepsilon{}^{r j}W{}^{\beta \gamma}W{}_{\alpha \beta \gamma}{}^{i} -\frac{3}{32}W^{-1}\nabla_{\zeta}^{t}\big(F{}_{a b}\big)(\Sigma{}^{a b}){}_{\eta}{}^{\alpha}\varepsilon{}^{r j}W{}^{\beta \gamma}W{}_{\alpha \beta \gamma}{}^{i}\\
&-\frac{3}{32}W^{-1}F{}_{a b}(\Sigma{}^{a b}){}_{\eta}{}^{\alpha}\varepsilon{}^{r j}\nabla_{\zeta}^{t}\big(W{}^{\beta \gamma}\big)W{}_{\alpha \beta \gamma}{}^{i} -\frac{3}{32}W^{-1}F{}_{a b}(\Sigma{}^{a b}){}_{\eta}{}^{\alpha}\varepsilon{}^{r j}W{}^{\beta \gamma}\nabla_{\zeta}^{t}\big(W{}_{\alpha \beta \gamma}{}^{i}\big)\\
&+\frac{3}{64}\nabla_{\zeta}^{t}\big(W^{-1}\big)F{}_{a b}(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r j}W{}_{\eta \alpha}X{}_{\beta}{}^{i} +\frac{3}{64}W^{-1}\nabla_{\zeta}^{t}\big(F{}_{a b}\big)(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r j}W{}_{\eta \alpha}X{}_{\beta}{}^{i}\\
&+\frac{3}{64}W^{-1}F{}_{a b}(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r j}\nabla_{\zeta}^{t}\big(W{}_{\eta \alpha}\big)X{}_{\beta}{}^{i} +\frac{3}{64}W^{-1}F{}_{a b}(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r j}W{}_{\eta \alpha}\nabla_{\zeta}^{t}\big(X{}_{\beta}{}^{i}\big)\\
&+\frac{9}{64}\nabla_{\zeta}^{t}\big(W^{-1}\big)F{}_{a b}(\Sigma{}^{a b}){}_{\eta}{}^{\alpha}\varepsilon{}^{r j}W{}_{\alpha \beta}X{}^{\beta i} +\frac{9}{64}W^{-1}\nabla_{\zeta}^{t}\big(F{}_{a b}\big)(\Sigma{}^{a b}){}_{\eta}{}^{\alpha}\varepsilon{}^{r j}W{}_{\alpha \beta}X{}^{\beta i}\\
&+\frac{9}{64}W^{-1}F{}_{a b}(\Sigma{}^{a b}){}_{\eta}{}^{\alpha}\varepsilon{}^{r j}\nabla_{\zeta}^{t}\big(W{}_{\alpha \beta}\big)X{}^{\beta i} +\frac{9}{64}W^{-1}F{}_{a b}(\Sigma{}^{a b}){}_{\eta}{}^{\alpha}\varepsilon{}^{r j}W{}_{\alpha \beta}\nabla_{\zeta}^{t}\big(X{}^{\beta i}\big)\\
&+\frac{3}{16}\nabla_{\zeta}^{t}\big(W^{-1}\big)F{}_{a b}(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r j}(\Gamma{}^{c}){}_{\alpha}{}^{\gamma}\big(\nabla_{c}W{}_{\beta \eta \gamma}{}^{i}\big) +\frac{3}{16}W^{-1}\nabla_{\zeta}^{t}\big(F{}_{a b}\big)(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r j}(\Gamma{}^{c}){}_{\alpha}{}^{\gamma}\big(\nabla_{c}W{}_{\beta \eta \gamma}{}^{i}\big)\\
&+\frac{3}{16}W^{-1}F{}_{a b}(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r j}(\Gamma{}^{c}){}_{\alpha}{}^{\gamma}\nabla_{\zeta}^{t}\big(\nabla_{c}W{}_{\beta \eta \gamma}{}^{i}\big) -\frac{3}{32}\nabla_{\zeta}^{t}\big(W^{-1}\big)F{}_{a b}(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r j}(\Gamma{}^{c}){}_{\eta \alpha}\big(\nabla_{c}X{}_{\beta}{}^{i}\big)\\
&-\frac{3}{32}W^{-1}\nabla_{\zeta}^{t}\big(F{}_{a b}\big)(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r j}(\Gamma{}^{c}){}_{\eta \alpha}\big(\nabla_{c}X{}_{\beta}{}^{i}\big) -\frac{3}{32}W^{-1}F{}_{a b}(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r j}(\Gamma{}^{c}){}_{\eta \alpha}\nabla_{\zeta}^{t}\big(\nabla_{c}X{}_{\beta}{}^{i}\big)\\
&+\frac{3}{32}\nabla_{\zeta}^{t}\big(W^{-1}\big)F{}_{a b}(\Sigma{}^{a b}){}_{\eta}{}^{\alpha}\varepsilon{}^{r j}(\Gamma{}^{c}){}_{\alpha \beta}\big(\nabla_{c}X{}^{\beta i}\big) +\frac{3}{32}W^{-1}\nabla_{\zeta}^{t}\big(F{}_{a b}\big)(\Sigma{}^{a b}){}_{\eta}{}^{\alpha}\varepsilon{}^{r j}(\Gamma{}^{c}){}_{\alpha \beta}\big(\nabla_{c}X{}^{\beta i}\big)\\
&+\frac{3}{32}W^{-1}F{}_{a b}(\Sigma{}^{a b}){}_{\eta}{}^{\alpha}\varepsilon{}^{r j}(\Gamma{}^{c}){}_{\alpha \beta}\nabla_{\zeta}^{t}\big(\nabla_{c}X{}^{\beta i}\big) -\frac{9}{32}\nabla_{\zeta}^{t}\big(W^{-1}\big)F{}_{a b}(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r j}W{}_{\beta}{}^{\gamma}W{}_{\alpha \eta \gamma}{}^{i}\\
&-\frac{9}{32}W^{-1}\nabla_{\zeta}^{t}\big(F{}_{a b}\big)(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r j}W{}_{\beta}{}^{\gamma}W{}_{\alpha \eta \gamma}{}^{i} -\frac{9}{32}W^{-1}F{}_{a b}(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r j}\nabla_{\zeta}^{t}\big(W{}_{\beta}{}^{\gamma}\big)W{}_{\alpha \eta \gamma}{}^{i}\\
&-\frac{9}{32}W^{-1}F{}_{a b}(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r j}W{}_{\beta}{}^{\gamma}\nabla_{\zeta}^{t}\big(W{}_{\alpha \eta \gamma}{}^{i}\big) -\frac{3}{32}\nabla_{\zeta}^{t}\big(W^{-1}\big)F{}_{a b}(\Sigma{}^{a b}){}^{\alpha}{}_{\eta}\varepsilon{}^{r j}W{}^{\beta \gamma}W{}_{\alpha \beta \gamma}{}^{i}\\
&-\frac{3}{32}W^{-1}\nabla_{\zeta}^{t}\big(F{}_{a b}\big)(\Sigma{}^{a b}){}^{\alpha}{}_{\eta}\varepsilon{}^{r j}W{}^{\beta \gamma}W{}_{\alpha \beta \gamma}{}^{i} -\frac{3}{32}W^{-1}F{}_{a b}(\Sigma{}^{a b}){}^{\alpha}{}_{\eta}\varepsilon{}^{r j}\nabla_{\zeta}^{t}\big(W{}^{\beta \gamma}\big)W{}_{\alpha \beta \gamma}{}^{i}\\
&-\frac{3}{32}W^{-1}F{}_{a b}(\Sigma{}^{a b}){}^{\alpha}{}_{\eta}\varepsilon{}^{r j}W{}^{\beta \gamma}\nabla_{\zeta}^{t}\big(W{}_{\alpha \beta \gamma}{}^{i}\big) +\frac{3}{64}\nabla_{\zeta}^{t}\big(W^{-1}\big)F{}_{a b}(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r j}W{}_{\eta \beta}X{}_{\alpha}{}^{i}\\
&+\frac{3}{64}W^{-1}\nabla_{\zeta}^{t}\big(F{}_{a b}\big)(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r j}W{}_{\eta \beta}X{}_{\alpha}{}^{i} +\frac{3}{64}W^{-1}F{}_{a b}(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r j}\nabla_{\zeta}^{t}\big(W{}_{\eta \beta}\big)X{}_{\alpha}{}^{i}\\
&+\frac{3}{64}W^{-1}F{}_{a b}(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r j}W{}_{\eta \beta}\nabla_{\zeta}^{t}\big(X{}_{\alpha}{}^{i}\big) +\frac{9}{64}\nabla_{\zeta}^{t}\big(W^{-1}\big)F{}_{a b}(\Sigma{}^{a b}){}^{\alpha}{}_{\eta}\varepsilon{}^{r j}W{}_{\alpha \beta}X{}^{\beta i}\\
&+\frac{9}{64}W^{-1}\nabla_{\zeta}^{t}\big(F{}_{a b}\big)(\Sigma{}^{a b}){}^{\alpha}{}_{\eta}\varepsilon{}^{r j}W{}_{\alpha \beta}X{}^{\beta i} +\frac{9}{64}W^{-1}F{}_{a b}(\Sigma{}^{a b}){}^{\alpha}{}_{\eta}\varepsilon{}^{r j}\nabla_{\zeta}^{t}\big(W{}_{\alpha \beta}\big)X{}^{\beta i}\\
&+\frac{9}{64}W^{-1}F{}_{a b}(\Sigma{}^{a b}){}^{\alpha}{}_{\eta}\varepsilon{}^{r j}W{}_{\alpha \beta}\nabla_{\zeta}^{t}\big(X{}^{\beta i}\big) +\frac{3}{16}\nabla_{\zeta}^{t}\big(W^{-1}\big)F{}_{a b}(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r j}(\Gamma{}^{c}){}_{\beta}{}^{\gamma}\big(\nabla_{c}W{}_{\alpha \eta \gamma}{}^{i}\big)\\
&+\frac{3}{16}W^{-1}\nabla_{\zeta}^{t}\big(F{}_{a b}\big)(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r j}(\Gamma{}^{c}){}_{\beta}{}^{\gamma}\big(\nabla_{c}W{}_{\alpha \eta \gamma}{}^{i}\big) +\frac{3}{16}W^{-1}F{}_{a b}(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r j}(\Gamma{}^{c}){}_{\beta}{}^{\gamma}\nabla_{\zeta}^{t}\big(\nabla_{c}W{}_{\alpha \eta \gamma}{}^{i}\big)\\
&-\frac{3}{32}\nabla_{\zeta}^{t}\big(W^{-1}\big)F{}_{a b}(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r j}(\Gamma{}^{c}){}_{\eta \beta}\big(\nabla_{c}X{}_{\alpha}{}^{i}\big) -\frac{3}{32}W^{-1}\nabla_{\zeta}^{t}\big(F{}_{a b}\big)(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r j}(\Gamma{}^{c}){}_{\eta \beta}\big(\nabla_{c}X{}_{\alpha}{}^{i}\big)\\
&-\frac{3}{32}W^{-1}F{}_{a b}(\Sigma{}^{a b}){}^{\alpha \beta}\varepsilon{}^{r j}(\Gamma{}^{c}){}_{\eta \beta}\nabla_{\zeta}^{t}\big(\nabla_{c}X{}_{\alpha}{}^{i}\big) +\frac{3}{32}\nabla_{\zeta}^{t}\big(W^{-1}\big)F{}_{a b}(\Sigma{}^{a b}){}^{\alpha}{}_{\eta}\varepsilon{}^{r j}(\Gamma{}^{c}){}_{\alpha \beta}\big(\nabla_{c}X{}^{\beta i}\big)\\
&+\frac{3}{32}W^{-1}\nabla_{\zeta}^{t}\big(F{}_{a b}\big)(\Sigma{}^{a b}){}^{\alpha}{}_{\eta}\varepsilon{}^{r j}(\Gamma{}^{c}){}_{\alpha \beta}\big(\nabla_{c}X{}^{\beta i}\big) +\frac{3}{32}W^{-1}F{}_{a b}(\Sigma{}^{a b}){}^{\alpha}{}_{\eta}\varepsilon{}^{r j}(\Gamma{}^{c}){}_{\alpha \beta}\nabla_{\zeta}^{t}\big(\nabla_{c}X{}^{\beta i}\big)
\end{aligned}
\tag{S5-H1.2-product-2}
```

Substitution of §3 and the gamma contraction (S5-V02) produce 1490 retained covariant contributions from this input. Their exact coefficients and contractions are included in §7; their locations are recorded in [the input-to-result ledger](../../../../../../../references/source_evidence/log/results/gauged_full_fermionic_log/sources/step5/endpoint_term_locations.json).

### Input H1.3

```math
\begin{aligned}
\left.H^{ij}\right|_{\mathrm{H1.3}}={}&-\frac{1}{2}W^{-1}\big(\nabla^{a}\nabla_{a}X{}^{i j}\big)
\end{aligned}
\tag{S5-H1.3-input}
```

Insert the derivative laws in §3 and expand the weighted symmetrization. The retained first derivative is

```math
\begin{aligned}
\left[\left.\nabla_\eta^r H^{ij}\right|_{\mathrm{H1.3}}\right]_{\le3}={}&\frac{i}{2}W^{-2}\lambda{}_{\eta}{}^{r}\big(\nabla^{a}\nabla_{a}X{}^{i j}\big) -\frac{i}{2}W^{-1}\varepsilon{}^{r i}(\Gamma{}^{a}){}_{\eta}{}^{\alpha}\big(\nabla^{b}\nabla_{b}\nabla_{a}\lambda{}_{\alpha}{}^{j}\big)\\
&+\frac{i}{4}W^{-1}\varepsilon{}^{r i}\big(\nabla^{a}\nabla_{a}W{}_{\eta \alpha}\big)\lambda{}^{\alpha j} +\frac{i}{4}W^{-1}\varepsilon{}^{r i}\big(\nabla_{a}W{}_{\eta \alpha}\big)\big(\nabla^{a}\lambda{}^{\alpha j}\big)\\
&+\frac{i}{4}W^{-1}\varepsilon{}^{r i}\big(\nabla^{a}W{}_{\eta \alpha}\big)\big(\nabla_{a}\lambda{}^{\alpha j}\big) +\frac{i}{4}W^{-1}\varepsilon{}^{r i}W{}_{\eta \alpha}\big(\nabla^{a}\nabla_{a}\lambda{}^{\alpha j}\big)\\
&+\frac{3}{8}\varepsilon{}^{r i}\big(\nabla^{a}\nabla_{a}X{}_{\eta}{}^{j}\big) +\frac{3}{8}W^{-1}\varepsilon{}^{r i}\big(\nabla_{a}X{}_{\eta}{}^{j}\big)\big(\nabla^{a}W\big)\\
&+\frac{3}{8}W^{-1}\varepsilon{}^{r i}\big(\nabla^{a}X{}_{\eta}{}^{j}\big)\big(\nabla_{a}W\big) +\frac{3}{8}W^{-1}\varepsilon{}^{r i}X{}_{\eta}{}^{j}\big(\nabla^{a}\nabla_{a}W\big)\\
&-\frac{i}{2}W^{-1}\varepsilon{}^{r j}(\Gamma{}^{a}){}_{\eta}{}^{\alpha}\big(\nabla^{b}\nabla_{b}\nabla_{a}\lambda{}_{\alpha}{}^{i}\big) +\frac{i}{4}W^{-1}\varepsilon{}^{r j}\big(\nabla^{a}\nabla_{a}W{}_{\eta \alpha}\big)\lambda{}^{\alpha i}\\
&+\frac{i}{4}W^{-1}\varepsilon{}^{r j}\big(\nabla_{a}W{}_{\eta \alpha}\big)\big(\nabla^{a}\lambda{}^{\alpha i}\big) +\frac{i}{4}W^{-1}\varepsilon{}^{r j}\big(\nabla^{a}W{}_{\eta \alpha}\big)\big(\nabla_{a}\lambda{}^{\alpha i}\big)\\
&+\frac{i}{4}W^{-1}\varepsilon{}^{r j}W{}_{\eta \alpha}\big(\nabla^{a}\nabla_{a}\lambda{}^{\alpha i}\big) +\frac{3}{8}\varepsilon{}^{r j}\big(\nabla^{a}\nabla_{a}X{}_{\eta}{}^{i}\big)\\
&+\frac{3}{8}W^{-1}\varepsilon{}^{r j}\big(\nabla_{a}X{}_{\eta}{}^{i}\big)\big(\nabla^{a}W\big) +\frac{3}{8}W^{-1}\varepsilon{}^{r j}\big(\nabla^{a}X{}_{\eta}{}^{i}\big)\big(\nabla_{a}W\big)\\
&+\frac{3}{8}W^{-1}\varepsilon{}^{r j}X{}_{\eta}{}^{i}\big(\nabla^{a}\nabla_{a}W\big) -\frac{i}{2}W^{-1}\big(\nabla^{a}\mathcal T{}_{a \eta}{}^{\alpha}\big)\varepsilon{}^{r i}(\Gamma{}^{b}){}_{\alpha}{}^{\beta}\big(\nabla_{b}\lambda{}_{\beta}{}^{j}\big)\\
&-\frac{i}{2}W^{-1}\mathcal T{}_{a \eta}{}^{\alpha}\varepsilon{}^{r i}(\Gamma{}^{b}){}_{\alpha}{}^{\beta}\big(\nabla^{a}\nabla_{b}\lambda{}_{\beta}{}^{j}\big) +\frac{i}{4}W^{-1}\big(\nabla^{a}\mathcal T{}_{a \eta}{}^{\alpha}\big)\varepsilon{}^{r i}W{}_{\alpha \beta}\lambda{}^{\beta j}\\
&+\frac{i}{4}W^{-1}\mathcal T{}_{a \eta}{}^{\alpha}\varepsilon{}^{r i}\big(\nabla^{a}W{}_{\alpha \beta}\big)\lambda{}^{\beta j} +\frac{i}{4}W^{-1}\mathcal T{}_{a \eta}{}^{\alpha}\varepsilon{}^{r i}W{}_{\alpha \beta}\big(\nabla^{a}\lambda{}^{\beta j}\big)\\
&+\frac{3}{8}\big(\nabla^{a}\mathcal T{}_{a \eta}{}^{\alpha}\big)\varepsilon{}^{r i}X{}_{\alpha}{}^{j} +\frac{3}{8}\mathcal T{}_{a \eta}{}^{\alpha}\varepsilon{}^{r i}\big(\nabla^{a}X{}_{\alpha}{}^{j}\big)\\
&+\frac{3}{8}W^{-1}\mathcal T{}_{a \eta}{}^{\alpha}\varepsilon{}^{r i}X{}_{\alpha}{}^{j}\big(\nabla^{a}W\big) -\frac{i}{2}W^{-1}\big(\nabla^{a}\mathcal T{}_{a \eta}{}^{\alpha}\big)\varepsilon{}^{r j}(\Gamma{}^{b}){}_{\alpha}{}^{\beta}\big(\nabla_{b}\lambda{}_{\beta}{}^{i}\big)\\
&-\frac{i}{2}W^{-1}\mathcal T{}_{a \eta}{}^{\alpha}\varepsilon{}^{r j}(\Gamma{}^{b}){}_{\alpha}{}^{\beta}\big(\nabla^{a}\nabla_{b}\lambda{}_{\beta}{}^{i}\big) +\frac{i}{4}W^{-1}\big(\nabla^{a}\mathcal T{}_{a \eta}{}^{\alpha}\big)\varepsilon{}^{r j}W{}_{\alpha \beta}\lambda{}^{\beta i}\\
&+\frac{i}{4}W^{-1}\mathcal T{}_{a \eta}{}^{\alpha}\varepsilon{}^{r j}\big(\nabla^{a}W{}_{\alpha \beta}\big)\lambda{}^{\beta i} +\frac{i}{4}W^{-1}\mathcal T{}_{a \eta}{}^{\alpha}\varepsilon{}^{r j}W{}_{\alpha \beta}\big(\nabla^{a}\lambda{}^{\beta i}\big)\\
&+\frac{3}{8}\big(\nabla^{a}\mathcal T{}_{a \eta}{}^{\alpha}\big)\varepsilon{}^{r j}X{}_{\alpha}{}^{i} +\frac{3}{8}\mathcal T{}_{a \eta}{}^{\alpha}\varepsilon{}^{r j}\big(\nabla^{a}X{}_{\alpha}{}^{i}\big)\\
&+\frac{3}{8}W^{-1}\mathcal T{}_{a \eta}{}^{\alpha}\varepsilon{}^{r j}X{}_{\alpha}{}^{i}\big(\nabla^{a}W\big) -W^{-1}\big(\nabla^{a}\mathcal R(\mathbb D){}_{a \eta}{}^{r}\big)X{}^{i j}\\
&-W^{-1}\mathcal R(\mathbb D){}_{a \eta}{}^{r}\big(\nabla^{a}X{}^{i j}\big) +\frac{1}{4}W^{-1}\big(\nabla^{a}\mathcal R(J){}_{a \eta}{}^{r i k}\big)X{}_{k}{}^{j}\\
&+\frac{1}{4}W^{-1}\mathcal R(J){}_{a \eta}{}^{r i k}\big(\nabla^{a}X{}_{k}{}^{j}\big) +\frac{1}{4}W^{-1}\big(\nabla^{a}\mathcal R(J){}_{a \eta}{}^{r k i}\big)X{}_{k}{}^{j}\\
&+\frac{1}{4}W^{-1}\mathcal R(J){}_{a \eta}{}^{r k i}\big(\nabla^{a}X{}_{k}{}^{j}\big) +\frac{1}{4}W^{-1}\big(\nabla^{a}\mathcal R(J){}_{a \eta}{}^{r j k}\big)X{}^{i}{}_{k}\\
&+\frac{1}{4}W^{-1}\mathcal R(J){}_{a \eta}{}^{r j k}\big(\nabla^{a}X{}^{i}{}_{k}\big) +\frac{1}{4}W^{-1}\big(\nabla^{a}\mathcal R(J){}_{a \eta}{}^{r k j}\big)X{}^{i}{}_{k}\\
&+\frac{1}{4}W^{-1}\mathcal R(J){}_{a \eta}{}^{r k j}\big(\nabla^{a}X{}^{i}{}_{k}\big) +\frac{1}{2}W^{-1}\big(\nabla^{a}\mathcal R(S){}_{a \eta}{}^{r \alpha i}\big)\lambda{}_{\alpha}{}^{j}\\
&+\frac{1}{2}W^{-1}\mathcal R(S){}_{a \eta}{}^{r \alpha i}\big(\nabla^{a}\lambda{}_{\alpha}{}^{j}\big) +\frac{1}{2}W^{-1}\big(\nabla^{a}\mathcal R(S){}_{a \eta}{}^{r \alpha j}\big)\lambda{}_{\alpha}{}^{i}\\
&+\frac{1}{2}W^{-1}\mathcal R(S){}_{a \eta}{}^{r \alpha j}\big(\nabla^{a}\lambda{}_{\alpha}{}^{i}\big) -\frac{i}{2}W^{-1}\mathcal T{}^{a}{}_{\eta}{}^{\alpha}\varepsilon{}^{r i}(\Gamma{}^{b}){}_{\alpha}{}^{\beta}\big(\nabla_{a}\nabla_{b}\lambda{}_{\beta}{}^{j}\big)\\
&+\frac{i}{4}W^{-1}\mathcal T{}^{a}{}_{\eta}{}^{\alpha}\varepsilon{}^{r i}\big(\nabla_{a}W{}_{\alpha \beta}\big)\lambda{}^{\beta j} +\frac{i}{4}W^{-1}\mathcal T{}^{a}{}_{\eta}{}^{\alpha}\varepsilon{}^{r i}W{}_{\alpha \beta}\big(\nabla_{a}\lambda{}^{\beta j}\big)\\
&+\frac{3}{8}\mathcal T{}^{a}{}_{\eta}{}^{\alpha}\varepsilon{}^{r i}\big(\nabla_{a}X{}_{\alpha}{}^{j}\big) +\frac{3}{8}W^{-1}\mathcal T{}^{a}{}_{\eta}{}^{\alpha}\varepsilon{}^{r i}X{}_{\alpha}{}^{j}\big(\nabla_{a}W\big)\\
&-\frac{i}{2}W^{-1}\mathcal T{}^{a}{}_{\eta}{}^{\alpha}\varepsilon{}^{r j}(\Gamma{}^{b}){}_{\alpha}{}^{\beta}\big(\nabla_{a}\nabla_{b}\lambda{}_{\beta}{}^{i}\big) +\frac{i}{4}W^{-1}\mathcal T{}^{a}{}_{\eta}{}^{\alpha}\varepsilon{}^{r j}\big(\nabla_{a}W{}_{\alpha \beta}\big)\lambda{}^{\beta i}\\
&+\frac{i}{4}W^{-1}\mathcal T{}^{a}{}_{\eta}{}^{\alpha}\varepsilon{}^{r j}W{}_{\alpha \beta}\big(\nabla_{a}\lambda{}^{\beta i}\big) +\frac{3}{8}\mathcal T{}^{a}{}_{\eta}{}^{\alpha}\varepsilon{}^{r j}\big(\nabla_{a}X{}_{\alpha}{}^{i}\big)\\
&+\frac{3}{8}W^{-1}\mathcal T{}^{a}{}_{\eta}{}^{\alpha}\varepsilon{}^{r j}X{}_{\alpha}{}^{i}\big(\nabla_{a}W\big) -\frac{i}{2}W^{-1}\mathcal T{}^{a}{}_{\eta}{}^{\alpha}\mathcal T{}_{a \alpha}{}^{\beta}\varepsilon{}^{r i}(\Gamma{}^{b}){}_{\beta}{}^{\gamma}\big(\nabla_{b}\lambda{}_{\gamma}{}^{j}\big)\\
&+\frac{i}{4}W^{-1}\mathcal T{}^{a}{}_{\eta}{}^{\alpha}\mathcal T{}_{a \alpha}{}^{\beta}\varepsilon{}^{r i}W{}_{\beta \gamma}\lambda{}^{\gamma j} +\frac{3}{8}\mathcal T{}^{a}{}_{\eta}{}^{\alpha}\mathcal T{}_{a \alpha}{}^{\beta}\varepsilon{}^{r i}X{}_{\beta}{}^{j}\\
&-\frac{i}{2}W^{-1}\mathcal T{}^{a}{}_{\eta}{}^{\alpha}\mathcal T{}_{a \alpha}{}^{\beta}\varepsilon{}^{r j}(\Gamma{}^{b}){}_{\beta}{}^{\gamma}\big(\nabla_{b}\lambda{}_{\gamma}{}^{i}\big) +\frac{i}{4}W^{-1}\mathcal T{}^{a}{}_{\eta}{}^{\alpha}\mathcal T{}_{a \alpha}{}^{\beta}\varepsilon{}^{r j}W{}_{\beta \gamma}\lambda{}^{\gamma i}\\
&+\frac{3}{8}\mathcal T{}^{a}{}_{\eta}{}^{\alpha}\mathcal T{}_{a \alpha}{}^{\beta}\varepsilon{}^{r j}X{}_{\beta}{}^{i} -W^{-1}\mathcal T{}^{a}{}_{\eta}{}^{\alpha}\mathcal R(\mathbb D){}_{a \alpha}{}^{r}X{}^{i j}\\
&+\frac{1}{4}W^{-1}\mathcal T{}^{a}{}_{\eta}{}^{\alpha}\mathcal R(J){}_{a \alpha}{}^{r i k}X{}_{k}{}^{j} +\frac{1}{4}W^{-1}\mathcal T{}^{a}{}_{\eta}{}^{\alpha}\mathcal R(J){}_{a \alpha}{}^{r k i}X{}_{k}{}^{j}\\
&+\frac{1}{4}W^{-1}\mathcal T{}^{a}{}_{\eta}{}^{\alpha}\mathcal R(J){}_{a \alpha}{}^{r j k}X{}^{i}{}_{k} +\frac{1}{4}W^{-1}\mathcal T{}^{a}{}_{\eta}{}^{\alpha}\mathcal R(J){}_{a \alpha}{}^{r k j}X{}^{i}{}_{k}\\
&+\frac{1}{2}W^{-1}\mathcal T{}^{a}{}_{\eta}{}^{\alpha}\mathcal R(S){}_{a \alpha}{}^{r \beta i}\lambda{}_{\beta}{}^{j} +\frac{1}{2}W^{-1}\mathcal T{}^{a}{}_{\eta}{}^{\alpha}\mathcal R(S){}_{a \alpha}{}^{r \beta j}\lambda{}_{\beta}{}^{i}\\
&-\frac{1}{4}W^{-1}\mathcal R(M){}^{a}{}_{\eta}{}^{r}{}_{a}{}^{b}\big(\nabla_{b}X{}^{i j}\big) +\frac{1}{4}W^{-1}\mathcal R(M){}^{a}{}_{\eta}{}^{r b}{}_{a}\big(\nabla_{b}X{}^{i j}\big)\\
&-\frac{3}{2}W^{-1}\mathcal R(\mathbb D){}^{a}{}_{\eta}{}^{r}\big(\nabla_{a}X{}^{i j}\big) +\frac{1}{4}W^{-1}\mathcal R(J){}^{a}{}_{\eta}{}^{r i k}\big(\nabla_{a}X{}_{k}{}^{j}\big)\\
&+\frac{1}{4}W^{-1}\mathcal R(J){}^{a}{}_{\eta}{}^{r k i}\big(\nabla_{a}X{}_{k}{}^{j}\big) +\frac{1}{4}W^{-1}\mathcal R(J){}^{a}{}_{\eta}{}^{r j k}\big(\nabla_{a}X{}^{i}{}_{k}\big)\\
&+\frac{1}{4}W^{-1}\mathcal R(J){}^{a}{}_{\eta}{}^{r k j}\big(\nabla_{a}X{}^{i}{}_{k}\big) +\frac{1}{2}W^{-1}\mathcal R(S){}^{a}{}_{\eta}{}^{r \alpha i}\big(\nabla_{a}\lambda{}_{\alpha}{}^{j}\big)\\
&+\frac{1}{2}W^{-1}\mathcal R(S){}^{a}{}_{\eta}{}^{r \alpha j}\big(\nabla_{a}\lambda{}_{\alpha}{}^{i}\big) +\frac{1}{2}W^{-1}\mathcal R(S){}^{a}{}_{\eta}{}^{r \alpha i}(\Gamma{}_{a}){}_{\alpha}{}^{\beta}(\Gamma{}^{b}){}_{\beta}{}^{\gamma}\big(\nabla_{b}\lambda{}_{\gamma}{}^{j}\big)\\
&-\frac{1}{4}W^{-1}\mathcal R(S){}^{a}{}_{\eta}{}^{r \alpha i}(\Gamma{}_{a}){}_{\alpha}{}^{\beta}W{}_{\beta \gamma}\lambda{}^{\gamma j} +\frac{3i}{8}\mathcal R(S){}^{a}{}_{\eta}{}^{r \alpha i}(\Gamma{}_{a}){}_{\alpha}{}^{\beta}X{}_{\beta}{}^{j}\\
&+\frac{1}{2}W^{-1}\mathcal R(S){}^{a}{}_{\eta}{}^{r \alpha j}(\Gamma{}_{a}){}_{\alpha}{}^{\beta}(\Gamma{}^{b}){}_{\beta}{}^{\gamma}\big(\nabla_{b}\lambda{}_{\gamma}{}^{i}\big) -\frac{1}{4}W^{-1}\mathcal R(S){}^{a}{}_{\eta}{}^{r \alpha j}(\Gamma{}_{a}){}_{\alpha}{}^{\beta}W{}_{\beta \gamma}\lambda{}^{\gamma i}\\
&+\frac{3i}{8}\mathcal R(S){}^{a}{}_{\eta}{}^{r \alpha j}(\Gamma{}_{a}){}_{\alpha}{}^{\beta}X{}_{\beta}{}^{i} -\frac{1}{8}W^{-1}\mathcal R(S){}^{a}{}_{\eta}{}^{r \alpha i}W{}_{a}{}^{b}(\Gamma{}_{b}){}_{\alpha}{}^{\beta}\lambda{}_{\beta}{}^{j}\\
&-\frac{1}{8}W^{-1}\mathcal R(S){}^{a}{}_{\eta}{}^{r \alpha j}W{}_{a}{}^{b}(\Gamma{}_{b}){}_{\alpha}{}^{\beta}\lambda{}_{\beta}{}^{i} -2W^{-1}\mathcal R(K){}_{a \eta}{}^{r a}X{}^{i j}
\end{aligned}
\tag{S5-H1.3-spinor}
```

Act with the next left derivative on each written factor, with its graded sign:

```math
\begin{aligned}
\nabla_\zeta^t\left[\left.\nabla_\eta^rH^{ij}\right|_{\mathrm{H1.3}}\right]_{\le3}={}&\frac{i}{2}\nabla_{\zeta}^{t}\big(W^{-2}\big)\lambda{}_{\eta}{}^{r}\big(\nabla^{a}\nabla_{a}X{}^{i j}\big) +\frac{i}{2}W^{-2}\nabla_{\zeta}^{t}\big(\lambda{}_{\eta}{}^{r}\big)\big(\nabla^{a}\nabla_{a}X{}^{i j}\big)\\
&-\frac{i}{2}W^{-2}\lambda{}_{\eta}{}^{r}\nabla_{\zeta}^{t}\big(\nabla^{a}\nabla_{a}X{}^{i j}\big) -\frac{i}{2}\nabla_{\zeta}^{t}\big(W^{-1}\big)\varepsilon{}^{r i}(\Gamma{}^{a}){}_{\eta}{}^{\alpha}\big(\nabla^{b}\nabla_{b}\nabla_{a}\lambda{}_{\alpha}{}^{j}\big)\\
&-\frac{i}{2}W^{-1}\varepsilon{}^{r i}(\Gamma{}^{a}){}_{\eta}{}^{\alpha}\nabla_{\zeta}^{t}\big(\nabla^{b}\nabla_{b}\nabla_{a}\lambda{}_{\alpha}{}^{j}\big) +\frac{i}{4}\nabla_{\zeta}^{t}\big(W^{-1}\big)\varepsilon{}^{r i}\big(\nabla^{a}\nabla_{a}W{}_{\eta \alpha}\big)\lambda{}^{\alpha j}\\
&+\frac{i}{4}W^{-1}\varepsilon{}^{r i}\nabla_{\zeta}^{t}\big(\nabla^{a}\nabla_{a}W{}_{\eta \alpha}\big)\lambda{}^{\alpha j} +\frac{i}{4}W^{-1}\varepsilon{}^{r i}\big(\nabla^{a}\nabla_{a}W{}_{\eta \alpha}\big)\nabla_{\zeta}^{t}\big(\lambda{}^{\alpha j}\big)\\
&+\frac{i}{4}\nabla_{\zeta}^{t}\big(W^{-1}\big)\varepsilon{}^{r i}\big(\nabla_{a}W{}_{\eta \alpha}\big)\big(\nabla^{a}\lambda{}^{\alpha j}\big) +\frac{i}{4}W^{-1}\varepsilon{}^{r i}\nabla_{\zeta}^{t}\big(\nabla_{a}W{}_{\eta \alpha}\big)\big(\nabla^{a}\lambda{}^{\alpha j}\big)\\
&+\frac{i}{4}W^{-1}\varepsilon{}^{r i}\big(\nabla_{a}W{}_{\eta \alpha}\big)\nabla_{\zeta}^{t}\big(\nabla^{a}\lambda{}^{\alpha j}\big) +\frac{i}{4}\nabla_{\zeta}^{t}\big(W^{-1}\big)\varepsilon{}^{r i}\big(\nabla^{a}W{}_{\eta \alpha}\big)\big(\nabla_{a}\lambda{}^{\alpha j}\big)\\
&+\frac{i}{4}W^{-1}\varepsilon{}^{r i}\nabla_{\zeta}^{t}\big(\nabla^{a}W{}_{\eta \alpha}\big)\big(\nabla_{a}\lambda{}^{\alpha j}\big) +\frac{i}{4}W^{-1}\varepsilon{}^{r i}\big(\nabla^{a}W{}_{\eta \alpha}\big)\nabla_{\zeta}^{t}\big(\nabla_{a}\lambda{}^{\alpha j}\big)\\
&+\frac{i}{4}\nabla_{\zeta}^{t}\big(W^{-1}\big)\varepsilon{}^{r i}W{}_{\eta \alpha}\big(\nabla^{a}\nabla_{a}\lambda{}^{\alpha j}\big) +\frac{i}{4}W^{-1}\varepsilon{}^{r i}\nabla_{\zeta}^{t}\big(W{}_{\eta \alpha}\big)\big(\nabla^{a}\nabla_{a}\lambda{}^{\alpha j}\big)\\
&+\frac{i}{4}W^{-1}\varepsilon{}^{r i}W{}_{\eta \alpha}\nabla_{\zeta}^{t}\big(\nabla^{a}\nabla_{a}\lambda{}^{\alpha j}\big) +\frac{3}{8}W\nabla_{\zeta}^{t}\big(W^{-1}\big)\varepsilon{}^{r i}\big(\nabla^{a}\nabla_{a}X{}_{\eta}{}^{j}\big)\\
&+\frac{3}{8}\varepsilon{}^{r i}\nabla_{\zeta}^{t}\big(\nabla^{a}\nabla_{a}X{}_{\eta}{}^{j}\big) -\frac{3}{8}W^{-1}\varepsilon{}^{r i}\big(\nabla^{a}\nabla_{a}X{}_{\eta}{}^{j}\big)\nabla_{\zeta}^{t}\big(W\big)\\
&+\frac{3}{8}\nabla_{\zeta}^{t}\big(W^{-1}\big)\varepsilon{}^{r i}\big(\nabla_{a}X{}_{\eta}{}^{j}\big)\big(\nabla^{a}W\big) +\frac{3}{8}W^{-1}\varepsilon{}^{r i}\nabla_{\zeta}^{t}\big(\nabla_{a}X{}_{\eta}{}^{j}\big)\big(\nabla^{a}W\big)\\
&-\frac{3}{8}W^{-1}\varepsilon{}^{r i}\big(\nabla_{a}X{}_{\eta}{}^{j}\big)\nabla_{\zeta}^{t}\big(\nabla^{a}W\big) +\frac{3}{8}\nabla_{\zeta}^{t}\big(W^{-1}\big)\varepsilon{}^{r i}\big(\nabla^{a}X{}_{\eta}{}^{j}\big)\big(\nabla_{a}W\big)\\
&+\frac{3}{8}W^{-1}\varepsilon{}^{r i}\nabla_{\zeta}^{t}\big(\nabla^{a}X{}_{\eta}{}^{j}\big)\big(\nabla_{a}W\big) -\frac{3}{8}W^{-1}\varepsilon{}^{r i}\big(\nabla^{a}X{}_{\eta}{}^{j}\big)\nabla_{\zeta}^{t}\big(\nabla_{a}W\big)\\
&+\frac{3}{8}\nabla_{\zeta}^{t}\big(W^{-1}\big)\varepsilon{}^{r i}X{}_{\eta}{}^{j}\big(\nabla^{a}\nabla_{a}W\big) +\frac{3}{8}W^{-1}\varepsilon{}^{r i}\nabla_{\zeta}^{t}\big(X{}_{\eta}{}^{j}\big)\big(\nabla^{a}\nabla_{a}W\big)\\
&-\frac{3}{8}W^{-1}\varepsilon{}^{r i}X{}_{\eta}{}^{j}\nabla_{\zeta}^{t}\big(\nabla^{a}\nabla_{a}W\big) -\frac{i}{2}\nabla_{\zeta}^{t}\big(W^{-1}\big)\varepsilon{}^{r j}(\Gamma{}^{a}){}_{\eta}{}^{\alpha}\big(\nabla^{b}\nabla_{b}\nabla_{a}\lambda{}_{\alpha}{}^{i}\big)\\
&-\frac{i}{2}W^{-1}\varepsilon{}^{r j}(\Gamma{}^{a}){}_{\eta}{}^{\alpha}\nabla_{\zeta}^{t}\big(\nabla^{b}\nabla_{b}\nabla_{a}\lambda{}_{\alpha}{}^{i}\big) +\frac{i}{4}\nabla_{\zeta}^{t}\big(W^{-1}\big)\varepsilon{}^{r j}\big(\nabla^{a}\nabla_{a}W{}_{\eta \alpha}\big)\lambda{}^{\alpha i}\\
&+\frac{i}{4}W^{-1}\varepsilon{}^{r j}\nabla_{\zeta}^{t}\big(\nabla^{a}\nabla_{a}W{}_{\eta \alpha}\big)\lambda{}^{\alpha i} +\frac{i}{4}W^{-1}\varepsilon{}^{r j}\big(\nabla^{a}\nabla_{a}W{}_{\eta \alpha}\big)\nabla_{\zeta}^{t}\big(\lambda{}^{\alpha i}\big)\\
&+\frac{i}{4}\nabla_{\zeta}^{t}\big(W^{-1}\big)\varepsilon{}^{r j}\big(\nabla_{a}W{}_{\eta \alpha}\big)\big(\nabla^{a}\lambda{}^{\alpha i}\big) +\frac{i}{4}W^{-1}\varepsilon{}^{r j}\nabla_{\zeta}^{t}\big(\nabla_{a}W{}_{\eta \alpha}\big)\big(\nabla^{a}\lambda{}^{\alpha i}\big)\\
&+\frac{i}{4}W^{-1}\varepsilon{}^{r j}\big(\nabla_{a}W{}_{\eta \alpha}\big)\nabla_{\zeta}^{t}\big(\nabla^{a}\lambda{}^{\alpha i}\big) +\frac{i}{4}\nabla_{\zeta}^{t}\big(W^{-1}\big)\varepsilon{}^{r j}\big(\nabla^{a}W{}_{\eta \alpha}\big)\big(\nabla_{a}\lambda{}^{\alpha i}\big)\\
&+\frac{i}{4}W^{-1}\varepsilon{}^{r j}\nabla_{\zeta}^{t}\big(\nabla^{a}W{}_{\eta \alpha}\big)\big(\nabla_{a}\lambda{}^{\alpha i}\big) +\frac{i}{4}W^{-1}\varepsilon{}^{r j}\big(\nabla^{a}W{}_{\eta \alpha}\big)\nabla_{\zeta}^{t}\big(\nabla_{a}\lambda{}^{\alpha i}\big)\\
&+\frac{i}{4}\nabla_{\zeta}^{t}\big(W^{-1}\big)\varepsilon{}^{r j}W{}_{\eta \alpha}\big(\nabla^{a}\nabla_{a}\lambda{}^{\alpha i}\big) +\frac{i}{4}W^{-1}\varepsilon{}^{r j}\nabla_{\zeta}^{t}\big(W{}_{\eta \alpha}\big)\big(\nabla^{a}\nabla_{a}\lambda{}^{\alpha i}\big)\\
&+\frac{i}{4}W^{-1}\varepsilon{}^{r j}W{}_{\eta \alpha}\nabla_{\zeta}^{t}\big(\nabla^{a}\nabla_{a}\lambda{}^{\alpha i}\big) +\frac{3}{8}W\nabla_{\zeta}^{t}\big(W^{-1}\big)\varepsilon{}^{r j}\big(\nabla^{a}\nabla_{a}X{}_{\eta}{}^{i}\big)\\
&+\frac{3}{8}\varepsilon{}^{r j}\nabla_{\zeta}^{t}\big(\nabla^{a}\nabla_{a}X{}_{\eta}{}^{i}\big) -\frac{3}{8}W^{-1}\varepsilon{}^{r j}\big(\nabla^{a}\nabla_{a}X{}_{\eta}{}^{i}\big)\nabla_{\zeta}^{t}\big(W\big)\\
&+\frac{3}{8}\nabla_{\zeta}^{t}\big(W^{-1}\big)\varepsilon{}^{r j}\big(\nabla_{a}X{}_{\eta}{}^{i}\big)\big(\nabla^{a}W\big) +\frac{3}{8}W^{-1}\varepsilon{}^{r j}\nabla_{\zeta}^{t}\big(\nabla_{a}X{}_{\eta}{}^{i}\big)\big(\nabla^{a}W\big)\\
&-\frac{3}{8}W^{-1}\varepsilon{}^{r j}\big(\nabla_{a}X{}_{\eta}{}^{i}\big)\nabla_{\zeta}^{t}\big(\nabla^{a}W\big) +\frac{3}{8}\nabla_{\zeta}^{t}\big(W^{-1}\big)\varepsilon{}^{r j}\big(\nabla^{a}X{}_{\eta}{}^{i}\big)\big(\nabla_{a}W\big)\\
&+\frac{3}{8}W^{-1}\varepsilon{}^{r j}\nabla_{\zeta}^{t}\big(\nabla^{a}X{}_{\eta}{}^{i}\big)\big(\nabla_{a}W\big) -\frac{3}{8}W^{-1}\varepsilon{}^{r j}\big(\nabla^{a}X{}_{\eta}{}^{i}\big)\nabla_{\zeta}^{t}\big(\nabla_{a}W\big)\\
&+\frac{3}{8}\nabla_{\zeta}^{t}\big(W^{-1}\big)\varepsilon{}^{r j}X{}_{\eta}{}^{i}\big(\nabla^{a}\nabla_{a}W\big) +\frac{3}{8}W^{-1}\varepsilon{}^{r j}\nabla_{\zeta}^{t}\big(X{}_{\eta}{}^{i}\big)\big(\nabla^{a}\nabla_{a}W\big)\\
&-\frac{3}{8}W^{-1}\varepsilon{}^{r j}X{}_{\eta}{}^{i}\nabla_{\zeta}^{t}\big(\nabla^{a}\nabla_{a}W\big) -\frac{i}{2}\nabla_{\zeta}^{t}\big(W^{-1}\big)\big(\nabla^{a}\mathcal T{}_{a \eta}{}^{\alpha}\big)\varepsilon{}^{r i}(\Gamma{}^{b}){}_{\alpha}{}^{\beta}\big(\nabla_{b}\lambda{}_{\beta}{}^{j}\big)\\
&-\frac{i}{2}W^{-1}\nabla_{\zeta}^{t}\big(\nabla^{a}\mathcal T{}_{a \eta}{}^{\alpha}\big)\varepsilon{}^{r i}(\Gamma{}^{b}){}_{\alpha}{}^{\beta}\big(\nabla_{b}\lambda{}_{\beta}{}^{j}\big) -\frac{i}{2}W^{-1}\big(\nabla^{a}\mathcal T{}_{a \eta}{}^{\alpha}\big)\varepsilon{}^{r i}(\Gamma{}^{b}){}_{\alpha}{}^{\beta}\nabla_{\zeta}^{t}\big(\nabla_{b}\lambda{}_{\beta}{}^{j}\big)\\
&-\frac{i}{2}\nabla_{\zeta}^{t}\big(W^{-1}\big)\mathcal T{}_{a \eta}{}^{\alpha}\varepsilon{}^{r i}(\Gamma{}^{b}){}_{\alpha}{}^{\beta}\big(\nabla^{a}\nabla_{b}\lambda{}_{\beta}{}^{j}\big) -\frac{i}{2}W^{-1}\nabla_{\zeta}^{t}\big(\mathcal T{}_{a \eta}{}^{\alpha}\big)\varepsilon{}^{r i}(\Gamma{}^{b}){}_{\alpha}{}^{\beta}\big(\nabla^{a}\nabla_{b}\lambda{}_{\beta}{}^{j}\big)\\
&-\frac{i}{2}W^{-1}\mathcal T{}_{a \eta}{}^{\alpha}\varepsilon{}^{r i}(\Gamma{}^{b}){}_{\alpha}{}^{\beta}\nabla_{\zeta}^{t}\big(\nabla^{a}\nabla_{b}\lambda{}_{\beta}{}^{j}\big) +\frac{i}{4}\nabla_{\zeta}^{t}\big(W^{-1}\big)\big(\nabla^{a}\mathcal T{}_{a \eta}{}^{\alpha}\big)\varepsilon{}^{r i}W{}_{\alpha \beta}\lambda{}^{\beta j}\\
&+\frac{i}{4}W^{-1}\nabla_{\zeta}^{t}\big(\nabla^{a}\mathcal T{}_{a \eta}{}^{\alpha}\big)\varepsilon{}^{r i}W{}_{\alpha \beta}\lambda{}^{\beta j} +\frac{i}{4}W^{-1}\big(\nabla^{a}\mathcal T{}_{a \eta}{}^{\alpha}\big)\varepsilon{}^{r i}\nabla_{\zeta}^{t}\big(W{}_{\alpha \beta}\big)\lambda{}^{\beta j}\\
&+\frac{i}{4}W^{-1}\big(\nabla^{a}\mathcal T{}_{a \eta}{}^{\alpha}\big)\varepsilon{}^{r i}W{}_{\alpha \beta}\nabla_{\zeta}^{t}\big(\lambda{}^{\beta j}\big) +\frac{i}{4}\nabla_{\zeta}^{t}\big(W^{-1}\big)\mathcal T{}_{a \eta}{}^{\alpha}\varepsilon{}^{r i}\big(\nabla^{a}W{}_{\alpha \beta}\big)\lambda{}^{\beta j}\\
&+\frac{i}{4}W^{-1}\nabla_{\zeta}^{t}\big(\mathcal T{}_{a \eta}{}^{\alpha}\big)\varepsilon{}^{r i}\big(\nabla^{a}W{}_{\alpha \beta}\big)\lambda{}^{\beta j} +\frac{i}{4}W^{-1}\mathcal T{}_{a \eta}{}^{\alpha}\varepsilon{}^{r i}\nabla_{\zeta}^{t}\big(\nabla^{a}W{}_{\alpha \beta}\big)\lambda{}^{\beta j}\\
&+\frac{i}{4}W^{-1}\mathcal T{}_{a \eta}{}^{\alpha}\varepsilon{}^{r i}\big(\nabla^{a}W{}_{\alpha \beta}\big)\nabla_{\zeta}^{t}\big(\lambda{}^{\beta j}\big) +\frac{i}{4}\nabla_{\zeta}^{t}\big(W^{-1}\big)\mathcal T{}_{a \eta}{}^{\alpha}\varepsilon{}^{r i}W{}_{\alpha \beta}\big(\nabla^{a}\lambda{}^{\beta j}\big)\\
&+\frac{i}{4}W^{-1}\nabla_{\zeta}^{t}\big(\mathcal T{}_{a \eta}{}^{\alpha}\big)\varepsilon{}^{r i}W{}_{\alpha \beta}\big(\nabla^{a}\lambda{}^{\beta j}\big) +\frac{i}{4}W^{-1}\mathcal T{}_{a \eta}{}^{\alpha}\varepsilon{}^{r i}\nabla_{\zeta}^{t}\big(W{}_{\alpha \beta}\big)\big(\nabla^{a}\lambda{}^{\beta j}\big)\\
&+\frac{i}{4}W^{-1}\mathcal T{}_{a \eta}{}^{\alpha}\varepsilon{}^{r i}W{}_{\alpha \beta}\nabla_{\zeta}^{t}\big(\nabla^{a}\lambda{}^{\beta j}\big) +\frac{3}{8}W\nabla_{\zeta}^{t}\big(W^{-1}\big)\big(\nabla^{a}\mathcal T{}_{a \eta}{}^{\alpha}\big)\varepsilon{}^{r i}X{}_{\alpha}{}^{j}\\
&+\frac{3}{8}\nabla_{\zeta}^{t}\big(\nabla^{a}\mathcal T{}_{a \eta}{}^{\alpha}\big)\varepsilon{}^{r i}X{}_{\alpha}{}^{j} +\frac{3}{8}\big(\nabla^{a}\mathcal T{}_{a \eta}{}^{\alpha}\big)\varepsilon{}^{r i}\nabla_{\zeta}^{t}\big(X{}_{\alpha}{}^{j}\big)\\
&-\frac{3}{8}W^{-1}\big(\nabla^{a}\mathcal T{}_{a \eta}{}^{\alpha}\big)\varepsilon{}^{r i}X{}_{\alpha}{}^{j}\nabla_{\zeta}^{t}\big(W\big) +\frac{3}{8}W\nabla_{\zeta}^{t}\big(W^{-1}\big)\mathcal T{}_{a \eta}{}^{\alpha}\varepsilon{}^{r i}\big(\nabla^{a}X{}_{\alpha}{}^{j}\big)\\
&+\frac{3}{8}\nabla_{\zeta}^{t}\big(\mathcal T{}_{a \eta}{}^{\alpha}\big)\varepsilon{}^{r i}\big(\nabla^{a}X{}_{\alpha}{}^{j}\big) +\frac{3}{8}\mathcal T{}_{a \eta}{}^{\alpha}\varepsilon{}^{r i}\nabla_{\zeta}^{t}\big(\nabla^{a}X{}_{\alpha}{}^{j}\big)\\
&-\frac{3}{8}W^{-1}\mathcal T{}_{a \eta}{}^{\alpha}\varepsilon{}^{r i}\big(\nabla^{a}X{}_{\alpha}{}^{j}\big)\nabla_{\zeta}^{t}\big(W\big) +\frac{3}{8}\nabla_{\zeta}^{t}\big(W^{-1}\big)\mathcal T{}_{a \eta}{}^{\alpha}\varepsilon{}^{r i}X{}_{\alpha}{}^{j}\big(\nabla^{a}W\big)\\
&+\frac{3}{8}W^{-1}\nabla_{\zeta}^{t}\big(\mathcal T{}_{a \eta}{}^{\alpha}\big)\varepsilon{}^{r i}X{}_{\alpha}{}^{j}\big(\nabla^{a}W\big) +\frac{3}{8}W^{-1}\mathcal T{}_{a \eta}{}^{\alpha}\varepsilon{}^{r i}\nabla_{\zeta}^{t}\big(X{}_{\alpha}{}^{j}\big)\big(\nabla^{a}W\big)\\
&-\frac{3}{8}W^{-1}\mathcal T{}_{a \eta}{}^{\alpha}\varepsilon{}^{r i}X{}_{\alpha}{}^{j}\nabla_{\zeta}^{t}\big(\nabla^{a}W\big) -\frac{i}{2}\nabla_{\zeta}^{t}\big(W^{-1}\big)\big(\nabla^{a}\mathcal T{}_{a \eta}{}^{\alpha}\big)\varepsilon{}^{r j}(\Gamma{}^{b}){}_{\alpha}{}^{\beta}\big(\nabla_{b}\lambda{}_{\beta}{}^{i}\big)\\
&-\frac{i}{2}W^{-1}\nabla_{\zeta}^{t}\big(\nabla^{a}\mathcal T{}_{a \eta}{}^{\alpha}\big)\varepsilon{}^{r j}(\Gamma{}^{b}){}_{\alpha}{}^{\beta}\big(\nabla_{b}\lambda{}_{\beta}{}^{i}\big) -\frac{i}{2}W^{-1}\big(\nabla^{a}\mathcal T{}_{a \eta}{}^{\alpha}\big)\varepsilon{}^{r j}(\Gamma{}^{b}){}_{\alpha}{}^{\beta}\nabla_{\zeta}^{t}\big(\nabla_{b}\lambda{}_{\beta}{}^{i}\big)\\
&-\frac{i}{2}\nabla_{\zeta}^{t}\big(W^{-1}\big)\mathcal T{}_{a \eta}{}^{\alpha}\varepsilon{}^{r j}(\Gamma{}^{b}){}_{\alpha}{}^{\beta}\big(\nabla^{a}\nabla_{b}\lambda{}_{\beta}{}^{i}\big) -\frac{i}{2}W^{-1}\nabla_{\zeta}^{t}\big(\mathcal T{}_{a \eta}{}^{\alpha}\big)\varepsilon{}^{r j}(\Gamma{}^{b}){}_{\alpha}{}^{\beta}\big(\nabla^{a}\nabla_{b}\lambda{}_{\beta}{}^{i}\big)\\
&-\frac{i}{2}W^{-1}\mathcal T{}_{a \eta}{}^{\alpha}\varepsilon{}^{r j}(\Gamma{}^{b}){}_{\alpha}{}^{\beta}\nabla_{\zeta}^{t}\big(\nabla^{a}\nabla_{b}\lambda{}_{\beta}{}^{i}\big) +\frac{i}{4}\nabla_{\zeta}^{t}\big(W^{-1}\big)\big(\nabla^{a}\mathcal T{}_{a \eta}{}^{\alpha}\big)\varepsilon{}^{r j}W{}_{\alpha \beta}\lambda{}^{\beta i}\\
&+\frac{i}{4}W^{-1}\nabla_{\zeta}^{t}\big(\nabla^{a}\mathcal T{}_{a \eta}{}^{\alpha}\big)\varepsilon{}^{r j}W{}_{\alpha \beta}\lambda{}^{\beta i} +\frac{i}{4}W^{-1}\big(\nabla^{a}\mathcal T{}_{a \eta}{}^{\alpha}\big)\varepsilon{}^{r j}\nabla_{\zeta}^{t}\big(W{}_{\alpha \beta}\big)\lambda{}^{\beta i}\\
&+\frac{i}{4}W^{-1}\big(\nabla^{a}\mathcal T{}_{a \eta}{}^{\alpha}\big)\varepsilon{}^{r j}W{}_{\alpha \beta}\nabla_{\zeta}^{t}\big(\lambda{}^{\beta i}\big) +\frac{i}{4}\nabla_{\zeta}^{t}\big(W^{-1}\big)\mathcal T{}_{a \eta}{}^{\alpha}\varepsilon{}^{r j}\big(\nabla^{a}W{}_{\alpha \beta}\big)\lambda{}^{\beta i}\\
&+\frac{i}{4}W^{-1}\nabla_{\zeta}^{t}\big(\mathcal T{}_{a \eta}{}^{\alpha}\big)\varepsilon{}^{r j}\big(\nabla^{a}W{}_{\alpha \beta}\big)\lambda{}^{\beta i} +\frac{i}{4}W^{-1}\mathcal T{}_{a \eta}{}^{\alpha}\varepsilon{}^{r j}\nabla_{\zeta}^{t}\big(\nabla^{a}W{}_{\alpha \beta}\big)\lambda{}^{\beta i}\\
&+\frac{i}{4}W^{-1}\mathcal T{}_{a \eta}{}^{\alpha}\varepsilon{}^{r j}\big(\nabla^{a}W{}_{\alpha \beta}\big)\nabla_{\zeta}^{t}\big(\lambda{}^{\beta i}\big) +\frac{i}{4}\nabla_{\zeta}^{t}\big(W^{-1}\big)\mathcal T{}_{a \eta}{}^{\alpha}\varepsilon{}^{r j}W{}_{\alpha \beta}\big(\nabla^{a}\lambda{}^{\beta i}\big)
\end{aligned}
\tag{S5-H1.3-product-1}
```

```math
\begin{aligned}
&+\frac{i}{4}W^{-1}\nabla_{\zeta}^{t}\big(\mathcal T{}_{a \eta}{}^{\alpha}\big)\varepsilon{}^{r j}W{}_{\alpha \beta}\big(\nabla^{a}\lambda{}^{\beta i}\big) +\frac{i}{4}W^{-1}\mathcal T{}_{a \eta}{}^{\alpha}\varepsilon{}^{r j}\nabla_{\zeta}^{t}\big(W{}_{\alpha \beta}\big)\big(\nabla^{a}\lambda{}^{\beta i}\big)\\
&+\frac{i}{4}W^{-1}\mathcal T{}_{a \eta}{}^{\alpha}\varepsilon{}^{r j}W{}_{\alpha \beta}\nabla_{\zeta}^{t}\big(\nabla^{a}\lambda{}^{\beta i}\big) +\frac{3}{8}W\nabla_{\zeta}^{t}\big(W^{-1}\big)\big(\nabla^{a}\mathcal T{}_{a \eta}{}^{\alpha}\big)\varepsilon{}^{r j}X{}_{\alpha}{}^{i}\\
&+\frac{3}{8}\nabla_{\zeta}^{t}\big(\nabla^{a}\mathcal T{}_{a \eta}{}^{\alpha}\big)\varepsilon{}^{r j}X{}_{\alpha}{}^{i} +\frac{3}{8}\big(\nabla^{a}\mathcal T{}_{a \eta}{}^{\alpha}\big)\varepsilon{}^{r j}\nabla_{\zeta}^{t}\big(X{}_{\alpha}{}^{i}\big)\\
&-\frac{3}{8}W^{-1}\big(\nabla^{a}\mathcal T{}_{a \eta}{}^{\alpha}\big)\varepsilon{}^{r j}X{}_{\alpha}{}^{i}\nabla_{\zeta}^{t}\big(W\big) +\frac{3}{8}W\nabla_{\zeta}^{t}\big(W^{-1}\big)\mathcal T{}_{a \eta}{}^{\alpha}\varepsilon{}^{r j}\big(\nabla^{a}X{}_{\alpha}{}^{i}\big)\\
&+\frac{3}{8}\nabla_{\zeta}^{t}\big(\mathcal T{}_{a \eta}{}^{\alpha}\big)\varepsilon{}^{r j}\big(\nabla^{a}X{}_{\alpha}{}^{i}\big) +\frac{3}{8}\mathcal T{}_{a \eta}{}^{\alpha}\varepsilon{}^{r j}\nabla_{\zeta}^{t}\big(\nabla^{a}X{}_{\alpha}{}^{i}\big)\\
&-\frac{3}{8}W^{-1}\mathcal T{}_{a \eta}{}^{\alpha}\varepsilon{}^{r j}\big(\nabla^{a}X{}_{\alpha}{}^{i}\big)\nabla_{\zeta}^{t}\big(W\big) +\frac{3}{8}\nabla_{\zeta}^{t}\big(W^{-1}\big)\mathcal T{}_{a \eta}{}^{\alpha}\varepsilon{}^{r j}X{}_{\alpha}{}^{i}\big(\nabla^{a}W\big)\\
&+\frac{3}{8}W^{-1}\nabla_{\zeta}^{t}\big(\mathcal T{}_{a \eta}{}^{\alpha}\big)\varepsilon{}^{r j}X{}_{\alpha}{}^{i}\big(\nabla^{a}W\big) +\frac{3}{8}W^{-1}\mathcal T{}_{a \eta}{}^{\alpha}\varepsilon{}^{r j}\nabla_{\zeta}^{t}\big(X{}_{\alpha}{}^{i}\big)\big(\nabla^{a}W\big)\\
&-\frac{3}{8}W^{-1}\mathcal T{}_{a \eta}{}^{\alpha}\varepsilon{}^{r j}X{}_{\alpha}{}^{i}\nabla_{\zeta}^{t}\big(\nabla^{a}W\big) -\nabla_{\zeta}^{t}\big(W^{-1}\big)\big(\nabla^{a}\mathcal R(\mathbb D){}_{a \eta}{}^{r}\big)X{}^{i j}\\
&-W^{-1}\nabla_{\zeta}^{t}\big(\nabla^{a}\mathcal R(\mathbb D){}_{a \eta}{}^{r}\big)X{}^{i j} +W^{-1}\big(\nabla^{a}\mathcal R(\mathbb D){}_{a \eta}{}^{r}\big)\nabla_{\zeta}^{t}\big(X{}^{i j}\big)\\
&-\nabla_{\zeta}^{t}\big(W^{-1}\big)\mathcal R(\mathbb D){}_{a \eta}{}^{r}\big(\nabla^{a}X{}^{i j}\big) -W^{-1}\nabla_{\zeta}^{t}\big(\mathcal R(\mathbb D){}_{a \eta}{}^{r}\big)\big(\nabla^{a}X{}^{i j}\big)\\
&+W^{-1}\mathcal R(\mathbb D){}_{a \eta}{}^{r}\nabla_{\zeta}^{t}\big(\nabla^{a}X{}^{i j}\big) +\frac{1}{4}\nabla_{\zeta}^{t}\big(W^{-1}\big)\big(\nabla^{a}\mathcal R(J){}_{a \eta}{}^{r i k}\big)X{}_{k}{}^{j}\\
&+\frac{1}{4}W^{-1}\nabla_{\zeta}^{t}\big(\nabla^{a}\mathcal R(J){}_{a \eta}{}^{r i k}\big)X{}_{k}{}^{j} -\frac{1}{4}W^{-1}\big(\nabla^{a}\mathcal R(J){}_{a \eta}{}^{r i k}\big)\nabla_{\zeta}^{t}\big(X{}_{k}{}^{j}\big)\\
&+\frac{1}{4}\nabla_{\zeta}^{t}\big(W^{-1}\big)\mathcal R(J){}_{a \eta}{}^{r i k}\big(\nabla^{a}X{}_{k}{}^{j}\big) +\frac{1}{4}W^{-1}\nabla_{\zeta}^{t}\big(\mathcal R(J){}_{a \eta}{}^{r i k}\big)\big(\nabla^{a}X{}_{k}{}^{j}\big)\\
&-\frac{1}{4}W^{-1}\mathcal R(J){}_{a \eta}{}^{r i k}\nabla_{\zeta}^{t}\big(\nabla^{a}X{}_{k}{}^{j}\big) +\frac{1}{4}\nabla_{\zeta}^{t}\big(W^{-1}\big)\big(\nabla^{a}\mathcal R(J){}_{a \eta}{}^{r k i}\big)X{}_{k}{}^{j}\\
&+\frac{1}{4}W^{-1}\nabla_{\zeta}^{t}\big(\nabla^{a}\mathcal R(J){}_{a \eta}{}^{r k i}\big)X{}_{k}{}^{j} -\frac{1}{4}W^{-1}\big(\nabla^{a}\mathcal R(J){}_{a \eta}{}^{r k i}\big)\nabla_{\zeta}^{t}\big(X{}_{k}{}^{j}\big)\\
&+\frac{1}{4}\nabla_{\zeta}^{t}\big(W^{-1}\big)\mathcal R(J){}_{a \eta}{}^{r k i}\big(\nabla^{a}X{}_{k}{}^{j}\big) +\frac{1}{4}W^{-1}\nabla_{\zeta}^{t}\big(\mathcal R(J){}_{a \eta}{}^{r k i}\big)\big(\nabla^{a}X{}_{k}{}^{j}\big)\\
&-\frac{1}{4}W^{-1}\mathcal R(J){}_{a \eta}{}^{r k i}\nabla_{\zeta}^{t}\big(\nabla^{a}X{}_{k}{}^{j}\big) +\frac{1}{4}\nabla_{\zeta}^{t}\big(W^{-1}\big)\big(\nabla^{a}\mathcal R(J){}_{a \eta}{}^{r j k}\big)X{}^{i}{}_{k}\\
&+\frac{1}{4}W^{-1}\nabla_{\zeta}^{t}\big(\nabla^{a}\mathcal R(J){}_{a \eta}{}^{r j k}\big)X{}^{i}{}_{k} -\frac{1}{4}W^{-1}\big(\nabla^{a}\mathcal R(J){}_{a \eta}{}^{r j k}\big)\nabla_{\zeta}^{t}\big(X{}^{i}{}_{k}\big)\\
&+\frac{1}{4}\nabla_{\zeta}^{t}\big(W^{-1}\big)\mathcal R(J){}_{a \eta}{}^{r j k}\big(\nabla^{a}X{}^{i}{}_{k}\big) +\frac{1}{4}W^{-1}\nabla_{\zeta}^{t}\big(\mathcal R(J){}_{a \eta}{}^{r j k}\big)\big(\nabla^{a}X{}^{i}{}_{k}\big)\\
&-\frac{1}{4}W^{-1}\mathcal R(J){}_{a \eta}{}^{r j k}\nabla_{\zeta}^{t}\big(\nabla^{a}X{}^{i}{}_{k}\big) +\frac{1}{4}\nabla_{\zeta}^{t}\big(W^{-1}\big)\big(\nabla^{a}\mathcal R(J){}_{a \eta}{}^{r k j}\big)X{}^{i}{}_{k}\\
&+\frac{1}{4}W^{-1}\nabla_{\zeta}^{t}\big(\nabla^{a}\mathcal R(J){}_{a \eta}{}^{r k j}\big)X{}^{i}{}_{k} -\frac{1}{4}W^{-1}\big(\nabla^{a}\mathcal R(J){}_{a \eta}{}^{r k j}\big)\nabla_{\zeta}^{t}\big(X{}^{i}{}_{k}\big)\\
&+\frac{1}{4}\nabla_{\zeta}^{t}\big(W^{-1}\big)\mathcal R(J){}_{a \eta}{}^{r k j}\big(\nabla^{a}X{}^{i}{}_{k}\big) +\frac{1}{4}W^{-1}\nabla_{\zeta}^{t}\big(\mathcal R(J){}_{a \eta}{}^{r k j}\big)\big(\nabla^{a}X{}^{i}{}_{k}\big)\\
&-\frac{1}{4}W^{-1}\mathcal R(J){}_{a \eta}{}^{r k j}\nabla_{\zeta}^{t}\big(\nabla^{a}X{}^{i}{}_{k}\big) +\frac{1}{2}\nabla_{\zeta}^{t}\big(W^{-1}\big)\big(\nabla^{a}\mathcal R(S){}_{a \eta}{}^{r \alpha i}\big)\lambda{}_{\alpha}{}^{j}\\
&+\frac{1}{2}W^{-1}\nabla_{\zeta}^{t}\big(\nabla^{a}\mathcal R(S){}_{a \eta}{}^{r \alpha i}\big)\lambda{}_{\alpha}{}^{j} +\frac{1}{2}W^{-1}\big(\nabla^{a}\mathcal R(S){}_{a \eta}{}^{r \alpha i}\big)\nabla_{\zeta}^{t}\big(\lambda{}_{\alpha}{}^{j}\big)\\
&+\frac{1}{2}\nabla_{\zeta}^{t}\big(W^{-1}\big)\mathcal R(S){}_{a \eta}{}^{r \alpha i}\big(\nabla^{a}\lambda{}_{\alpha}{}^{j}\big) +\frac{1}{2}W^{-1}\nabla_{\zeta}^{t}\big(\mathcal R(S){}_{a \eta}{}^{r \alpha i}\big)\big(\nabla^{a}\lambda{}_{\alpha}{}^{j}\big)\\
&+\frac{1}{2}W^{-1}\mathcal R(S){}_{a \eta}{}^{r \alpha i}\nabla_{\zeta}^{t}\big(\nabla^{a}\lambda{}_{\alpha}{}^{j}\big) +\frac{1}{2}\nabla_{\zeta}^{t}\big(W^{-1}\big)\big(\nabla^{a}\mathcal R(S){}_{a \eta}{}^{r \alpha j}\big)\lambda{}_{\alpha}{}^{i}\\
&+\frac{1}{2}W^{-1}\nabla_{\zeta}^{t}\big(\nabla^{a}\mathcal R(S){}_{a \eta}{}^{r \alpha j}\big)\lambda{}_{\alpha}{}^{i} +\frac{1}{2}W^{-1}\big(\nabla^{a}\mathcal R(S){}_{a \eta}{}^{r \alpha j}\big)\nabla_{\zeta}^{t}\big(\lambda{}_{\alpha}{}^{i}\big)\\
&+\frac{1}{2}\nabla_{\zeta}^{t}\big(W^{-1}\big)\mathcal R(S){}_{a \eta}{}^{r \alpha j}\big(\nabla^{a}\lambda{}_{\alpha}{}^{i}\big) +\frac{1}{2}W^{-1}\nabla_{\zeta}^{t}\big(\mathcal R(S){}_{a \eta}{}^{r \alpha j}\big)\big(\nabla^{a}\lambda{}_{\alpha}{}^{i}\big)\\
&+\frac{1}{2}W^{-1}\mathcal R(S){}_{a \eta}{}^{r \alpha j}\nabla_{\zeta}^{t}\big(\nabla^{a}\lambda{}_{\alpha}{}^{i}\big) -\frac{i}{2}\nabla_{\zeta}^{t}\big(W^{-1}\big)\mathcal T{}^{a}{}_{\eta}{}^{\alpha}\varepsilon{}^{r i}(\Gamma{}^{b}){}_{\alpha}{}^{\beta}\big(\nabla_{a}\nabla_{b}\lambda{}_{\beta}{}^{j}\big)\\
&-\frac{i}{2}W^{-1}\nabla_{\zeta}^{t}\big(\mathcal T{}^{a}{}_{\eta}{}^{\alpha}\big)\varepsilon{}^{r i}(\Gamma{}^{b}){}_{\alpha}{}^{\beta}\big(\nabla_{a}\nabla_{b}\lambda{}_{\beta}{}^{j}\big) -\frac{i}{2}W^{-1}\mathcal T{}^{a}{}_{\eta}{}^{\alpha}\varepsilon{}^{r i}(\Gamma{}^{b}){}_{\alpha}{}^{\beta}\nabla_{\zeta}^{t}\big(\nabla_{a}\nabla_{b}\lambda{}_{\beta}{}^{j}\big)\\
&+\frac{i}{4}\nabla_{\zeta}^{t}\big(W^{-1}\big)\mathcal T{}^{a}{}_{\eta}{}^{\alpha}\varepsilon{}^{r i}\big(\nabla_{a}W{}_{\alpha \beta}\big)\lambda{}^{\beta j} +\frac{i}{4}W^{-1}\nabla_{\zeta}^{t}\big(\mathcal T{}^{a}{}_{\eta}{}^{\alpha}\big)\varepsilon{}^{r i}\big(\nabla_{a}W{}_{\alpha \beta}\big)\lambda{}^{\beta j}\\
&+\frac{i}{4}W^{-1}\mathcal T{}^{a}{}_{\eta}{}^{\alpha}\varepsilon{}^{r i}\nabla_{\zeta}^{t}\big(\nabla_{a}W{}_{\alpha \beta}\big)\lambda{}^{\beta j} +\frac{i}{4}W^{-1}\mathcal T{}^{a}{}_{\eta}{}^{\alpha}\varepsilon{}^{r i}\big(\nabla_{a}W{}_{\alpha \beta}\big)\nabla_{\zeta}^{t}\big(\lambda{}^{\beta j}\big)\\
&+\frac{i}{4}\nabla_{\zeta}^{t}\big(W^{-1}\big)\mathcal T{}^{a}{}_{\eta}{}^{\alpha}\varepsilon{}^{r i}W{}_{\alpha \beta}\big(\nabla_{a}\lambda{}^{\beta j}\big) +\frac{i}{4}W^{-1}\nabla_{\zeta}^{t}\big(\mathcal T{}^{a}{}_{\eta}{}^{\alpha}\big)\varepsilon{}^{r i}W{}_{\alpha \beta}\big(\nabla_{a}\lambda{}^{\beta j}\big)\\
&+\frac{i}{4}W^{-1}\mathcal T{}^{a}{}_{\eta}{}^{\alpha}\varepsilon{}^{r i}\nabla_{\zeta}^{t}\big(W{}_{\alpha \beta}\big)\big(\nabla_{a}\lambda{}^{\beta j}\big) +\frac{i}{4}W^{-1}\mathcal T{}^{a}{}_{\eta}{}^{\alpha}\varepsilon{}^{r i}W{}_{\alpha \beta}\nabla_{\zeta}^{t}\big(\nabla_{a}\lambda{}^{\beta j}\big)\\
&+\frac{3}{8}W\nabla_{\zeta}^{t}\big(W^{-1}\big)\mathcal T{}^{a}{}_{\eta}{}^{\alpha}\varepsilon{}^{r i}\big(\nabla_{a}X{}_{\alpha}{}^{j}\big) +\frac{3}{8}\nabla_{\zeta}^{t}\big(\mathcal T{}^{a}{}_{\eta}{}^{\alpha}\big)\varepsilon{}^{r i}\big(\nabla_{a}X{}_{\alpha}{}^{j}\big)\\
&+\frac{3}{8}\mathcal T{}^{a}{}_{\eta}{}^{\alpha}\varepsilon{}^{r i}\nabla_{\zeta}^{t}\big(\nabla_{a}X{}_{\alpha}{}^{j}\big) -\frac{3}{8}W^{-1}\mathcal T{}^{a}{}_{\eta}{}^{\alpha}\varepsilon{}^{r i}\big(\nabla_{a}X{}_{\alpha}{}^{j}\big)\nabla_{\zeta}^{t}\big(W\big)\\
&+\frac{3}{8}\nabla_{\zeta}^{t}\big(W^{-1}\big)\mathcal T{}^{a}{}_{\eta}{}^{\alpha}\varepsilon{}^{r i}X{}_{\alpha}{}^{j}\big(\nabla_{a}W\big) +\frac{3}{8}W^{-1}\nabla_{\zeta}^{t}\big(\mathcal T{}^{a}{}_{\eta}{}^{\alpha}\big)\varepsilon{}^{r i}X{}_{\alpha}{}^{j}\big(\nabla_{a}W\big)\\
&+\frac{3}{8}W^{-1}\mathcal T{}^{a}{}_{\eta}{}^{\alpha}\varepsilon{}^{r i}\nabla_{\zeta}^{t}\big(X{}_{\alpha}{}^{j}\big)\big(\nabla_{a}W\big) -\frac{3}{8}W^{-1}\mathcal T{}^{a}{}_{\eta}{}^{\alpha}\varepsilon{}^{r i}X{}_{\alpha}{}^{j}\nabla_{\zeta}^{t}\big(\nabla_{a}W\big)\\
&-\frac{i}{2}\nabla_{\zeta}^{t}\big(W^{-1}\big)\mathcal T{}^{a}{}_{\eta}{}^{\alpha}\varepsilon{}^{r j}(\Gamma{}^{b}){}_{\alpha}{}^{\beta}\big(\nabla_{a}\nabla_{b}\lambda{}_{\beta}{}^{i}\big) -\frac{i}{2}W^{-1}\nabla_{\zeta}^{t}\big(\mathcal T{}^{a}{}_{\eta}{}^{\alpha}\big)\varepsilon{}^{r j}(\Gamma{}^{b}){}_{\alpha}{}^{\beta}\big(\nabla_{a}\nabla_{b}\lambda{}_{\beta}{}^{i}\big)\\
&-\frac{i}{2}W^{-1}\mathcal T{}^{a}{}_{\eta}{}^{\alpha}\varepsilon{}^{r j}(\Gamma{}^{b}){}_{\alpha}{}^{\beta}\nabla_{\zeta}^{t}\big(\nabla_{a}\nabla_{b}\lambda{}_{\beta}{}^{i}\big) +\frac{i}{4}\nabla_{\zeta}^{t}\big(W^{-1}\big)\mathcal T{}^{a}{}_{\eta}{}^{\alpha}\varepsilon{}^{r j}\big(\nabla_{a}W{}_{\alpha \beta}\big)\lambda{}^{\beta i}\\
&+\frac{i}{4}W^{-1}\nabla_{\zeta}^{t}\big(\mathcal T{}^{a}{}_{\eta}{}^{\alpha}\big)\varepsilon{}^{r j}\big(\nabla_{a}W{}_{\alpha \beta}\big)\lambda{}^{\beta i} +\frac{i}{4}W^{-1}\mathcal T{}^{a}{}_{\eta}{}^{\alpha}\varepsilon{}^{r j}\nabla_{\zeta}^{t}\big(\nabla_{a}W{}_{\alpha \beta}\big)\lambda{}^{\beta i}\\
&+\frac{i}{4}W^{-1}\mathcal T{}^{a}{}_{\eta}{}^{\alpha}\varepsilon{}^{r j}\big(\nabla_{a}W{}_{\alpha \beta}\big)\nabla_{\zeta}^{t}\big(\lambda{}^{\beta i}\big) +\frac{i}{4}\nabla_{\zeta}^{t}\big(W^{-1}\big)\mathcal T{}^{a}{}_{\eta}{}^{\alpha}\varepsilon{}^{r j}W{}_{\alpha \beta}\big(\nabla_{a}\lambda{}^{\beta i}\big)\\
&+\frac{i}{4}W^{-1}\nabla_{\zeta}^{t}\big(\mathcal T{}^{a}{}_{\eta}{}^{\alpha}\big)\varepsilon{}^{r j}W{}_{\alpha \beta}\big(\nabla_{a}\lambda{}^{\beta i}\big) +\frac{i}{4}W^{-1}\mathcal T{}^{a}{}_{\eta}{}^{\alpha}\varepsilon{}^{r j}\nabla_{\zeta}^{t}\big(W{}_{\alpha \beta}\big)\big(\nabla_{a}\lambda{}^{\beta i}\big)\\
&+\frac{i}{4}W^{-1}\mathcal T{}^{a}{}_{\eta}{}^{\alpha}\varepsilon{}^{r j}W{}_{\alpha \beta}\nabla_{\zeta}^{t}\big(\nabla_{a}\lambda{}^{\beta i}\big) +\frac{3}{8}W\nabla_{\zeta}^{t}\big(W^{-1}\big)\mathcal T{}^{a}{}_{\eta}{}^{\alpha}\varepsilon{}^{r j}\big(\nabla_{a}X{}_{\alpha}{}^{i}\big)\\
&+\frac{3}{8}\nabla_{\zeta}^{t}\big(\mathcal T{}^{a}{}_{\eta}{}^{\alpha}\big)\varepsilon{}^{r j}\big(\nabla_{a}X{}_{\alpha}{}^{i}\big) +\frac{3}{8}\mathcal T{}^{a}{}_{\eta}{}^{\alpha}\varepsilon{}^{r j}\nabla_{\zeta}^{t}\big(\nabla_{a}X{}_{\alpha}{}^{i}\big)\\
&-\frac{3}{8}W^{-1}\mathcal T{}^{a}{}_{\eta}{}^{\alpha}\varepsilon{}^{r j}\big(\nabla_{a}X{}_{\alpha}{}^{i}\big)\nabla_{\zeta}^{t}\big(W\big) +\frac{3}{8}\nabla_{\zeta}^{t}\big(W^{-1}\big)\mathcal T{}^{a}{}_{\eta}{}^{\alpha}\varepsilon{}^{r j}X{}_{\alpha}{}^{i}\big(\nabla_{a}W\big)\\
&+\frac{3}{8}W^{-1}\nabla_{\zeta}^{t}\big(\mathcal T{}^{a}{}_{\eta}{}^{\alpha}\big)\varepsilon{}^{r j}X{}_{\alpha}{}^{i}\big(\nabla_{a}W\big) +\frac{3}{8}W^{-1}\mathcal T{}^{a}{}_{\eta}{}^{\alpha}\varepsilon{}^{r j}\nabla_{\zeta}^{t}\big(X{}_{\alpha}{}^{i}\big)\big(\nabla_{a}W\big)\\
&-\frac{3}{8}W^{-1}\mathcal T{}^{a}{}_{\eta}{}^{\alpha}\varepsilon{}^{r j}X{}_{\alpha}{}^{i}\nabla_{\zeta}^{t}\big(\nabla_{a}W\big) -\frac{i}{2}\nabla_{\zeta}^{t}\big(W^{-1}\big)\mathcal T{}^{a}{}_{\eta}{}^{\alpha}\mathcal T{}_{a \alpha}{}^{\beta}\varepsilon{}^{r i}(\Gamma{}^{b}){}_{\beta}{}^{\gamma}\big(\nabla_{b}\lambda{}_{\gamma}{}^{j}\big)\\
&-\frac{i}{2}W^{-1}\nabla_{\zeta}^{t}\big(\mathcal T{}^{a}{}_{\eta}{}^{\alpha}\big)\mathcal T{}_{a \alpha}{}^{\beta}\varepsilon{}^{r i}(\Gamma{}^{b}){}_{\beta}{}^{\gamma}\big(\nabla_{b}\lambda{}_{\gamma}{}^{j}\big) -\frac{i}{2}W^{-1}\mathcal T{}^{a}{}_{\eta}{}^{\alpha}\nabla_{\zeta}^{t}\big(\mathcal T{}_{a \alpha}{}^{\beta}\big)\varepsilon{}^{r i}(\Gamma{}^{b}){}_{\beta}{}^{\gamma}\big(\nabla_{b}\lambda{}_{\gamma}{}^{j}\big)\\
&-\frac{i}{2}W^{-1}\mathcal T{}^{a}{}_{\eta}{}^{\alpha}\mathcal T{}_{a \alpha}{}^{\beta}\varepsilon{}^{r i}(\Gamma{}^{b}){}_{\beta}{}^{\gamma}\nabla_{\zeta}^{t}\big(\nabla_{b}\lambda{}_{\gamma}{}^{j}\big) +\frac{i}{4}\nabla_{\zeta}^{t}\big(W^{-1}\big)\mathcal T{}^{a}{}_{\eta}{}^{\alpha}\mathcal T{}_{a \alpha}{}^{\beta}\varepsilon{}^{r i}W{}_{\beta \gamma}\lambda{}^{\gamma j}
\end{aligned}
\tag{S5-H1.3-product-2}
```

```math
\begin{aligned}
&+\frac{i}{4}W^{-1}\nabla_{\zeta}^{t}\big(\mathcal T{}^{a}{}_{\eta}{}^{\alpha}\big)\mathcal T{}_{a \alpha}{}^{\beta}\varepsilon{}^{r i}W{}_{\beta \gamma}\lambda{}^{\gamma j} +\frac{i}{4}W^{-1}\mathcal T{}^{a}{}_{\eta}{}^{\alpha}\nabla_{\zeta}^{t}\big(\mathcal T{}_{a \alpha}{}^{\beta}\big)\varepsilon{}^{r i}W{}_{\beta \gamma}\lambda{}^{\gamma j}\\
&+\frac{i}{4}W^{-1}\mathcal T{}^{a}{}_{\eta}{}^{\alpha}\mathcal T{}_{a \alpha}{}^{\beta}\varepsilon{}^{r i}\nabla_{\zeta}^{t}\big(W{}_{\beta \gamma}\big)\lambda{}^{\gamma j} +\frac{i}{4}W^{-1}\mathcal T{}^{a}{}_{\eta}{}^{\alpha}\mathcal T{}_{a \alpha}{}^{\beta}\varepsilon{}^{r i}W{}_{\beta \gamma}\nabla_{\zeta}^{t}\big(\lambda{}^{\gamma j}\big)\\
&+\frac{3}{8}W\nabla_{\zeta}^{t}\big(W^{-1}\big)\mathcal T{}^{a}{}_{\eta}{}^{\alpha}\mathcal T{}_{a \alpha}{}^{\beta}\varepsilon{}^{r i}X{}_{\beta}{}^{j} +\frac{3}{8}\nabla_{\zeta}^{t}\big(\mathcal T{}^{a}{}_{\eta}{}^{\alpha}\big)\mathcal T{}_{a \alpha}{}^{\beta}\varepsilon{}^{r i}X{}_{\beta}{}^{j}\\
&+\frac{3}{8}\mathcal T{}^{a}{}_{\eta}{}^{\alpha}\nabla_{\zeta}^{t}\big(\mathcal T{}_{a \alpha}{}^{\beta}\big)\varepsilon{}^{r i}X{}_{\beta}{}^{j} +\frac{3}{8}\mathcal T{}^{a}{}_{\eta}{}^{\alpha}\mathcal T{}_{a \alpha}{}^{\beta}\varepsilon{}^{r i}\nabla_{\zeta}^{t}\big(X{}_{\beta}{}^{j}\big)\\
&-\frac{3}{8}W^{-1}\mathcal T{}^{a}{}_{\eta}{}^{\alpha}\mathcal T{}_{a \alpha}{}^{\beta}\varepsilon{}^{r i}X{}_{\beta}{}^{j}\nabla_{\zeta}^{t}\big(W\big) -\frac{i}{2}\nabla_{\zeta}^{t}\big(W^{-1}\big)\mathcal T{}^{a}{}_{\eta}{}^{\alpha}\mathcal T{}_{a \alpha}{}^{\beta}\varepsilon{}^{r j}(\Gamma{}^{b}){}_{\beta}{}^{\gamma}\big(\nabla_{b}\lambda{}_{\gamma}{}^{i}\big)\\
&-\frac{i}{2}W^{-1}\nabla_{\zeta}^{t}\big(\mathcal T{}^{a}{}_{\eta}{}^{\alpha}\big)\mathcal T{}_{a \alpha}{}^{\beta}\varepsilon{}^{r j}(\Gamma{}^{b}){}_{\beta}{}^{\gamma}\big(\nabla_{b}\lambda{}_{\gamma}{}^{i}\big) -\frac{i}{2}W^{-1}\mathcal T{}^{a}{}_{\eta}{}^{\alpha}\nabla_{\zeta}^{t}\big(\mathcal T{}_{a \alpha}{}^{\beta}\big)\varepsilon{}^{r j}(\Gamma{}^{b}){}_{\beta}{}^{\gamma}\big(\nabla_{b}\lambda{}_{\gamma}{}^{i}\big)\\
&-\frac{i}{2}W^{-1}\mathcal T{}^{a}{}_{\eta}{}^{\alpha}\mathcal T{}_{a \alpha}{}^{\beta}\varepsilon{}^{r j}(\Gamma{}^{b}){}_{\beta}{}^{\gamma}\nabla_{\zeta}^{t}\big(\nabla_{b}\lambda{}_{\gamma}{}^{i}\big) +\frac{i}{4}\nabla_{\zeta}^{t}\big(W^{-1}\big)\mathcal T{}^{a}{}_{\eta}{}^{\alpha}\mathcal T{}_{a \alpha}{}^{\beta}\varepsilon{}^{r j}W{}_{\beta \gamma}\lambda{}^{\gamma i}\\
&+\frac{i}{4}W^{-1}\nabla_{\zeta}^{t}\big(\mathcal T{}^{a}{}_{\eta}{}^{\alpha}\big)\mathcal T{}_{a \alpha}{}^{\beta}\varepsilon{}^{r j}W{}_{\beta \gamma}\lambda{}^{\gamma i} +\frac{i}{4}W^{-1}\mathcal T{}^{a}{}_{\eta}{}^{\alpha}\nabla_{\zeta}^{t}\big(\mathcal T{}_{a \alpha}{}^{\beta}\big)\varepsilon{}^{r j}W{}_{\beta \gamma}\lambda{}^{\gamma i}\\
&+\frac{i}{4}W^{-1}\mathcal T{}^{a}{}_{\eta}{}^{\alpha}\mathcal T{}_{a \alpha}{}^{\beta}\varepsilon{}^{r j}\nabla_{\zeta}^{t}\big(W{}_{\beta \gamma}\big)\lambda{}^{\gamma i} +\frac{i}{4}W^{-1}\mathcal T{}^{a}{}_{\eta}{}^{\alpha}\mathcal T{}_{a \alpha}{}^{\beta}\varepsilon{}^{r j}W{}_{\beta \gamma}\nabla_{\zeta}^{t}\big(\lambda{}^{\gamma i}\big)\\
&+\frac{3}{8}W\nabla_{\zeta}^{t}\big(W^{-1}\big)\mathcal T{}^{a}{}_{\eta}{}^{\alpha}\mathcal T{}_{a \alpha}{}^{\beta}\varepsilon{}^{r j}X{}_{\beta}{}^{i} +\frac{3}{8}\nabla_{\zeta}^{t}\big(\mathcal T{}^{a}{}_{\eta}{}^{\alpha}\big)\mathcal T{}_{a \alpha}{}^{\beta}\varepsilon{}^{r j}X{}_{\beta}{}^{i}\\
&+\frac{3}{8}\mathcal T{}^{a}{}_{\eta}{}^{\alpha}\nabla_{\zeta}^{t}\big(\mathcal T{}_{a \alpha}{}^{\beta}\big)\varepsilon{}^{r j}X{}_{\beta}{}^{i} +\frac{3}{8}\mathcal T{}^{a}{}_{\eta}{}^{\alpha}\mathcal T{}_{a \alpha}{}^{\beta}\varepsilon{}^{r j}\nabla_{\zeta}^{t}\big(X{}_{\beta}{}^{i}\big)\\
&-\frac{3}{8}W^{-1}\mathcal T{}^{a}{}_{\eta}{}^{\alpha}\mathcal T{}_{a \alpha}{}^{\beta}\varepsilon{}^{r j}X{}_{\beta}{}^{i}\nabla_{\zeta}^{t}\big(W\big) -\nabla_{\zeta}^{t}\big(W^{-1}\big)\mathcal T{}^{a}{}_{\eta}{}^{\alpha}\mathcal R(\mathbb D){}_{a \alpha}{}^{r}X{}^{i j}\\
&-W^{-1}\nabla_{\zeta}^{t}\big(\mathcal T{}^{a}{}_{\eta}{}^{\alpha}\big)\mathcal R(\mathbb D){}_{a \alpha}{}^{r}X{}^{i j} -W^{-1}\mathcal T{}^{a}{}_{\eta}{}^{\alpha}\nabla_{\zeta}^{t}\big(\mathcal R(\mathbb D){}_{a \alpha}{}^{r}\big)X{}^{i j}\\
&+W^{-1}\mathcal T{}^{a}{}_{\eta}{}^{\alpha}\mathcal R(\mathbb D){}_{a \alpha}{}^{r}\nabla_{\zeta}^{t}\big(X{}^{i j}\big) +\frac{1}{4}\nabla_{\zeta}^{t}\big(W^{-1}\big)\mathcal T{}^{a}{}_{\eta}{}^{\alpha}\mathcal R(J){}_{a \alpha}{}^{r i k}X{}_{k}{}^{j}\\
&+\frac{1}{4}W^{-1}\nabla_{\zeta}^{t}\big(\mathcal T{}^{a}{}_{\eta}{}^{\alpha}\big)\mathcal R(J){}_{a \alpha}{}^{r i k}X{}_{k}{}^{j} +\frac{1}{4}W^{-1}\mathcal T{}^{a}{}_{\eta}{}^{\alpha}\nabla_{\zeta}^{t}\big(\mathcal R(J){}_{a \alpha}{}^{r i k}\big)X{}_{k}{}^{j}\\
&-\frac{1}{4}W^{-1}\mathcal T{}^{a}{}_{\eta}{}^{\alpha}\mathcal R(J){}_{a \alpha}{}^{r i k}\nabla_{\zeta}^{t}\big(X{}_{k}{}^{j}\big) +\frac{1}{4}\nabla_{\zeta}^{t}\big(W^{-1}\big)\mathcal T{}^{a}{}_{\eta}{}^{\alpha}\mathcal R(J){}_{a \alpha}{}^{r k i}X{}_{k}{}^{j}\\
&+\frac{1}{4}W^{-1}\nabla_{\zeta}^{t}\big(\mathcal T{}^{a}{}_{\eta}{}^{\alpha}\big)\mathcal R(J){}_{a \alpha}{}^{r k i}X{}_{k}{}^{j} +\frac{1}{4}W^{-1}\mathcal T{}^{a}{}_{\eta}{}^{\alpha}\nabla_{\zeta}^{t}\big(\mathcal R(J){}_{a \alpha}{}^{r k i}\big)X{}_{k}{}^{j}\\
&-\frac{1}{4}W^{-1}\mathcal T{}^{a}{}_{\eta}{}^{\alpha}\mathcal R(J){}_{a \alpha}{}^{r k i}\nabla_{\zeta}^{t}\big(X{}_{k}{}^{j}\big) +\frac{1}{4}\nabla_{\zeta}^{t}\big(W^{-1}\big)\mathcal T{}^{a}{}_{\eta}{}^{\alpha}\mathcal R(J){}_{a \alpha}{}^{r j k}X{}^{i}{}_{k}\\
&+\frac{1}{4}W^{-1}\nabla_{\zeta}^{t}\big(\mathcal T{}^{a}{}_{\eta}{}^{\alpha}\big)\mathcal R(J){}_{a \alpha}{}^{r j k}X{}^{i}{}_{k} +\frac{1}{4}W^{-1}\mathcal T{}^{a}{}_{\eta}{}^{\alpha}\nabla_{\zeta}^{t}\big(\mathcal R(J){}_{a \alpha}{}^{r j k}\big)X{}^{i}{}_{k}\\
&-\frac{1}{4}W^{-1}\mathcal T{}^{a}{}_{\eta}{}^{\alpha}\mathcal R(J){}_{a \alpha}{}^{r j k}\nabla_{\zeta}^{t}\big(X{}^{i}{}_{k}\big) +\frac{1}{4}\nabla_{\zeta}^{t}\big(W^{-1}\big)\mathcal T{}^{a}{}_{\eta}{}^{\alpha}\mathcal R(J){}_{a \alpha}{}^{r k j}X{}^{i}{}_{k}\\
&+\frac{1}{4}W^{-1}\nabla_{\zeta}^{t}\big(\mathcal T{}^{a}{}_{\eta}{}^{\alpha}\big)\mathcal R(J){}_{a \alpha}{}^{r k j}X{}^{i}{}_{k} +\frac{1}{4}W^{-1}\mathcal T{}^{a}{}_{\eta}{}^{\alpha}\nabla_{\zeta}^{t}\big(\mathcal R(J){}_{a \alpha}{}^{r k j}\big)X{}^{i}{}_{k}\\
&-\frac{1}{4}W^{-1}\mathcal T{}^{a}{}_{\eta}{}^{\alpha}\mathcal R(J){}_{a \alpha}{}^{r k j}\nabla_{\zeta}^{t}\big(X{}^{i}{}_{k}\big) +\frac{1}{2}\nabla_{\zeta}^{t}\big(W^{-1}\big)\mathcal T{}^{a}{}_{\eta}{}^{\alpha}\mathcal R(S){}_{a \alpha}{}^{r \beta i}\lambda{}_{\beta}{}^{j}\\
&+\frac{1}{2}W^{-1}\nabla_{\zeta}^{t}\big(\mathcal T{}^{a}{}_{\eta}{}^{\alpha}\big)\mathcal R(S){}_{a \alpha}{}^{r \beta i}\lambda{}_{\beta}{}^{j} +\frac{1}{2}W^{-1}\mathcal T{}^{a}{}_{\eta}{}^{\alpha}\nabla_{\zeta}^{t}\big(\mathcal R(S){}_{a \alpha}{}^{r \beta i}\big)\lambda{}_{\beta}{}^{j}\\
&+\frac{1}{2}W^{-1}\mathcal T{}^{a}{}_{\eta}{}^{\alpha}\mathcal R(S){}_{a \alpha}{}^{r \beta i}\nabla_{\zeta}^{t}\big(\lambda{}_{\beta}{}^{j}\big) +\frac{1}{2}\nabla_{\zeta}^{t}\big(W^{-1}\big)\mathcal T{}^{a}{}_{\eta}{}^{\alpha}\mathcal R(S){}_{a \alpha}{}^{r \beta j}\lambda{}_{\beta}{}^{i}\\
&+\frac{1}{2}W^{-1}\nabla_{\zeta}^{t}\big(\mathcal T{}^{a}{}_{\eta}{}^{\alpha}\big)\mathcal R(S){}_{a \alpha}{}^{r \beta j}\lambda{}_{\beta}{}^{i} +\frac{1}{2}W^{-1}\mathcal T{}^{a}{}_{\eta}{}^{\alpha}\nabla_{\zeta}^{t}\big(\mathcal R(S){}_{a \alpha}{}^{r \beta j}\big)\lambda{}_{\beta}{}^{i}\\
&+\frac{1}{2}W^{-1}\mathcal T{}^{a}{}_{\eta}{}^{\alpha}\mathcal R(S){}_{a \alpha}{}^{r \beta j}\nabla_{\zeta}^{t}\big(\lambda{}_{\beta}{}^{i}\big) -\frac{1}{4}\nabla_{\zeta}^{t}\big(W^{-1}\big)\mathcal R(M){}^{a}{}_{\eta}{}^{r}{}_{a}{}^{b}\big(\nabla_{b}X{}^{i j}\big)\\
&-\frac{1}{4}W^{-1}\nabla_{\zeta}^{t}\big(\mathcal R(M){}^{a}{}_{\eta}{}^{r}{}_{a}{}^{b}\big)\big(\nabla_{b}X{}^{i j}\big) +\frac{1}{4}W^{-1}\mathcal R(M){}^{a}{}_{\eta}{}^{r}{}_{a}{}^{b}\nabla_{\zeta}^{t}\big(\nabla_{b}X{}^{i j}\big)\\
&+\frac{1}{4}\nabla_{\zeta}^{t}\big(W^{-1}\big)\mathcal R(M){}^{a}{}_{\eta}{}^{r b}{}_{a}\big(\nabla_{b}X{}^{i j}\big) +\frac{1}{4}W^{-1}\nabla_{\zeta}^{t}\big(\mathcal R(M){}^{a}{}_{\eta}{}^{r b}{}_{a}\big)\big(\nabla_{b}X{}^{i j}\big)\\
&-\frac{1}{4}W^{-1}\mathcal R(M){}^{a}{}_{\eta}{}^{r b}{}_{a}\nabla_{\zeta}^{t}\big(\nabla_{b}X{}^{i j}\big) -\frac{3}{2}\nabla_{\zeta}^{t}\big(W^{-1}\big)\mathcal R(\mathbb D){}^{a}{}_{\eta}{}^{r}\big(\nabla_{a}X{}^{i j}\big)\\
&-\frac{3}{2}W^{-1}\nabla_{\zeta}^{t}\big(\mathcal R(\mathbb D){}^{a}{}_{\eta}{}^{r}\big)\big(\nabla_{a}X{}^{i j}\big) +\frac{3}{2}W^{-1}\mathcal R(\mathbb D){}^{a}{}_{\eta}{}^{r}\nabla_{\zeta}^{t}\big(\nabla_{a}X{}^{i j}\big)\\
&+\frac{1}{4}\nabla_{\zeta}^{t}\big(W^{-1}\big)\mathcal R(J){}^{a}{}_{\eta}{}^{r i k}\big(\nabla_{a}X{}_{k}{}^{j}\big) +\frac{1}{4}W^{-1}\nabla_{\zeta}^{t}\big(\mathcal R(J){}^{a}{}_{\eta}{}^{r i k}\big)\big(\nabla_{a}X{}_{k}{}^{j}\big)\\
&-\frac{1}{4}W^{-1}\mathcal R(J){}^{a}{}_{\eta}{}^{r i k}\nabla_{\zeta}^{t}\big(\nabla_{a}X{}_{k}{}^{j}\big) +\frac{1}{4}\nabla_{\zeta}^{t}\big(W^{-1}\big)\mathcal R(J){}^{a}{}_{\eta}{}^{r k i}\big(\nabla_{a}X{}_{k}{}^{j}\big)\\
&+\frac{1}{4}W^{-1}\nabla_{\zeta}^{t}\big(\mathcal R(J){}^{a}{}_{\eta}{}^{r k i}\big)\big(\nabla_{a}X{}_{k}{}^{j}\big) -\frac{1}{4}W^{-1}\mathcal R(J){}^{a}{}_{\eta}{}^{r k i}\nabla_{\zeta}^{t}\big(\nabla_{a}X{}_{k}{}^{j}\big)\\
&+\frac{1}{4}\nabla_{\zeta}^{t}\big(W^{-1}\big)\mathcal R(J){}^{a}{}_{\eta}{}^{r j k}\big(\nabla_{a}X{}^{i}{}_{k}\big) +\frac{1}{4}W^{-1}\nabla_{\zeta}^{t}\big(\mathcal R(J){}^{a}{}_{\eta}{}^{r j k}\big)\big(\nabla_{a}X{}^{i}{}_{k}\big)\\
&-\frac{1}{4}W^{-1}\mathcal R(J){}^{a}{}_{\eta}{}^{r j k}\nabla_{\zeta}^{t}\big(\nabla_{a}X{}^{i}{}_{k}\big) +\frac{1}{4}\nabla_{\zeta}^{t}\big(W^{-1}\big)\mathcal R(J){}^{a}{}_{\eta}{}^{r k j}\big(\nabla_{a}X{}^{i}{}_{k}\big)\\
&+\frac{1}{4}W^{-1}\nabla_{\zeta}^{t}\big(\mathcal R(J){}^{a}{}_{\eta}{}^{r k j}\big)\big(\nabla_{a}X{}^{i}{}_{k}\big) -\frac{1}{4}W^{-1}\mathcal R(J){}^{a}{}_{\eta}{}^{r k j}\nabla_{\zeta}^{t}\big(\nabla_{a}X{}^{i}{}_{k}\big)\\
&+\frac{1}{2}\nabla_{\zeta}^{t}\big(W^{-1}\big)\mathcal R(S){}^{a}{}_{\eta}{}^{r \alpha i}\big(\nabla_{a}\lambda{}_{\alpha}{}^{j}\big) +\frac{1}{2}W^{-1}\nabla_{\zeta}^{t}\big(\mathcal R(S){}^{a}{}_{\eta}{}^{r \alpha i}\big)\big(\nabla_{a}\lambda{}_{\alpha}{}^{j}\big)\\
&+\frac{1}{2}W^{-1}\mathcal R(S){}^{a}{}_{\eta}{}^{r \alpha i}\nabla_{\zeta}^{t}\big(\nabla_{a}\lambda{}_{\alpha}{}^{j}\big) +\frac{1}{2}\nabla_{\zeta}^{t}\big(W^{-1}\big)\mathcal R(S){}^{a}{}_{\eta}{}^{r \alpha j}\big(\nabla_{a}\lambda{}_{\alpha}{}^{i}\big)\\
&+\frac{1}{2}W^{-1}\nabla_{\zeta}^{t}\big(\mathcal R(S){}^{a}{}_{\eta}{}^{r \alpha j}\big)\big(\nabla_{a}\lambda{}_{\alpha}{}^{i}\big) +\frac{1}{2}W^{-1}\mathcal R(S){}^{a}{}_{\eta}{}^{r \alpha j}\nabla_{\zeta}^{t}\big(\nabla_{a}\lambda{}_{\alpha}{}^{i}\big)\\
&+\frac{1}{2}\nabla_{\zeta}^{t}\big(W^{-1}\big)\mathcal R(S){}^{a}{}_{\eta}{}^{r \alpha i}(\Gamma{}_{a}){}_{\alpha}{}^{\beta}(\Gamma{}^{b}){}_{\beta}{}^{\gamma}\big(\nabla_{b}\lambda{}_{\gamma}{}^{j}\big) +\frac{1}{2}W^{-1}\nabla_{\zeta}^{t}\big(\mathcal R(S){}^{a}{}_{\eta}{}^{r \alpha i}\big)(\Gamma{}_{a}){}_{\alpha}{}^{\beta}(\Gamma{}^{b}){}_{\beta}{}^{\gamma}\big(\nabla_{b}\lambda{}_{\gamma}{}^{j}\big)\\
&+\frac{1}{2}W^{-1}\mathcal R(S){}^{a}{}_{\eta}{}^{r \alpha i}(\Gamma{}_{a}){}_{\alpha}{}^{\beta}(\Gamma{}^{b}){}_{\beta}{}^{\gamma}\nabla_{\zeta}^{t}\big(\nabla_{b}\lambda{}_{\gamma}{}^{j}\big) -\frac{1}{4}\nabla_{\zeta}^{t}\big(W^{-1}\big)\mathcal R(S){}^{a}{}_{\eta}{}^{r \alpha i}(\Gamma{}_{a}){}_{\alpha}{}^{\beta}W{}_{\beta \gamma}\lambda{}^{\gamma j}\\
&-\frac{1}{4}W^{-1}\nabla_{\zeta}^{t}\big(\mathcal R(S){}^{a}{}_{\eta}{}^{r \alpha i}\big)(\Gamma{}_{a}){}_{\alpha}{}^{\beta}W{}_{\beta \gamma}\lambda{}^{\gamma j} -\frac{1}{4}W^{-1}\mathcal R(S){}^{a}{}_{\eta}{}^{r \alpha i}(\Gamma{}_{a}){}_{\alpha}{}^{\beta}\nabla_{\zeta}^{t}\big(W{}_{\beta \gamma}\big)\lambda{}^{\gamma j}\\
&-\frac{1}{4}W^{-1}\mathcal R(S){}^{a}{}_{\eta}{}^{r \alpha i}(\Gamma{}_{a}){}_{\alpha}{}^{\beta}W{}_{\beta \gamma}\nabla_{\zeta}^{t}\big(\lambda{}^{\gamma j}\big) +\frac{3i}{8}W\nabla_{\zeta}^{t}\big(W^{-1}\big)\mathcal R(S){}^{a}{}_{\eta}{}^{r \alpha i}(\Gamma{}_{a}){}_{\alpha}{}^{\beta}X{}_{\beta}{}^{j}\\
&+\frac{3i}{8}\nabla_{\zeta}^{t}\big(\mathcal R(S){}^{a}{}_{\eta}{}^{r \alpha i}\big)(\Gamma{}_{a}){}_{\alpha}{}^{\beta}X{}_{\beta}{}^{j} +\frac{3i}{8}\mathcal R(S){}^{a}{}_{\eta}{}^{r \alpha i}(\Gamma{}_{a}){}_{\alpha}{}^{\beta}\nabla_{\zeta}^{t}\big(X{}_{\beta}{}^{j}\big)\\
&-\frac{3i}{8}W^{-1}\mathcal R(S){}^{a}{}_{\eta}{}^{r \alpha i}(\Gamma{}_{a}){}_{\alpha}{}^{\beta}X{}_{\beta}{}^{j}\nabla_{\zeta}^{t}\big(W\big) +\frac{1}{2}\nabla_{\zeta}^{t}\big(W^{-1}\big)\mathcal R(S){}^{a}{}_{\eta}{}^{r \alpha j}(\Gamma{}_{a}){}_{\alpha}{}^{\beta}(\Gamma{}^{b}){}_{\beta}{}^{\gamma}\big(\nabla_{b}\lambda{}_{\gamma}{}^{i}\big)\\
&+\frac{1}{2}W^{-1}\nabla_{\zeta}^{t}\big(\mathcal R(S){}^{a}{}_{\eta}{}^{r \alpha j}\big)(\Gamma{}_{a}){}_{\alpha}{}^{\beta}(\Gamma{}^{b}){}_{\beta}{}^{\gamma}\big(\nabla_{b}\lambda{}_{\gamma}{}^{i}\big) +\frac{1}{2}W^{-1}\mathcal R(S){}^{a}{}_{\eta}{}^{r \alpha j}(\Gamma{}_{a}){}_{\alpha}{}^{\beta}(\Gamma{}^{b}){}_{\beta}{}^{\gamma}\nabla_{\zeta}^{t}\big(\nabla_{b}\lambda{}_{\gamma}{}^{i}\big)\\
&-\frac{1}{4}\nabla_{\zeta}^{t}\big(W^{-1}\big)\mathcal R(S){}^{a}{}_{\eta}{}^{r \alpha j}(\Gamma{}_{a}){}_{\alpha}{}^{\beta}W{}_{\beta \gamma}\lambda{}^{\gamma i} -\frac{1}{4}W^{-1}\nabla_{\zeta}^{t}\big(\mathcal R(S){}^{a}{}_{\eta}{}^{r \alpha j}\big)(\Gamma{}_{a}){}_{\alpha}{}^{\beta}W{}_{\beta \gamma}\lambda{}^{\gamma i}\\
&-\frac{1}{4}W^{-1}\mathcal R(S){}^{a}{}_{\eta}{}^{r \alpha j}(\Gamma{}_{a}){}_{\alpha}{}^{\beta}\nabla_{\zeta}^{t}\big(W{}_{\beta \gamma}\big)\lambda{}^{\gamma i} -\frac{1}{4}W^{-1}\mathcal R(S){}^{a}{}_{\eta}{}^{r \alpha j}(\Gamma{}_{a}){}_{\alpha}{}^{\beta}W{}_{\beta \gamma}\nabla_{\zeta}^{t}\big(\lambda{}^{\gamma i}\big)\\
&+\frac{3i}{8}W\nabla_{\zeta}^{t}\big(W^{-1}\big)\mathcal R(S){}^{a}{}_{\eta}{}^{r \alpha j}(\Gamma{}_{a}){}_{\alpha}{}^{\beta}X{}_{\beta}{}^{i} +\frac{3i}{8}\nabla_{\zeta}^{t}\big(\mathcal R(S){}^{a}{}_{\eta}{}^{r \alpha j}\big)(\Gamma{}_{a}){}_{\alpha}{}^{\beta}X{}_{\beta}{}^{i}\\
&+\frac{3i}{8}\mathcal R(S){}^{a}{}_{\eta}{}^{r \alpha j}(\Gamma{}_{a}){}_{\alpha}{}^{\beta}\nabla_{\zeta}^{t}\big(X{}_{\beta}{}^{i}\big) -\frac{3i}{8}W^{-1}\mathcal R(S){}^{a}{}_{\eta}{}^{r \alpha j}(\Gamma{}_{a}){}_{\alpha}{}^{\beta}X{}_{\beta}{}^{i}\nabla_{\zeta}^{t}\big(W\big)
\end{aligned}
\tag{S5-H1.3-product-3}
```

```math
\begin{aligned}
&-\frac{1}{8}\nabla_{\zeta}^{t}\big(W^{-1}\big)\mathcal R(S){}^{a}{}_{\eta}{}^{r \alpha i}W{}_{a}{}^{b}(\Gamma{}_{b}){}_{\alpha}{}^{\beta}\lambda{}_{\beta}{}^{j} -\frac{1}{8}W^{-1}\nabla_{\zeta}^{t}\big(\mathcal R(S){}^{a}{}_{\eta}{}^{r \alpha i}\big)W{}_{a}{}^{b}(\Gamma{}_{b}){}_{\alpha}{}^{\beta}\lambda{}_{\beta}{}^{j}\\
&-\frac{1}{8}W^{-1}\mathcal R(S){}^{a}{}_{\eta}{}^{r \alpha i}\nabla_{\zeta}^{t}\big(W{}_{a}{}^{b}\big)(\Gamma{}_{b}){}_{\alpha}{}^{\beta}\lambda{}_{\beta}{}^{j} -\frac{1}{8}W^{-1}\mathcal R(S){}^{a}{}_{\eta}{}^{r \alpha i}W{}_{a}{}^{b}(\Gamma{}_{b}){}_{\alpha}{}^{\beta}\nabla_{\zeta}^{t}\big(\lambda{}_{\beta}{}^{j}\big)\\
&-\frac{1}{8}\nabla_{\zeta}^{t}\big(W^{-1}\big)\mathcal R(S){}^{a}{}_{\eta}{}^{r \alpha j}W{}_{a}{}^{b}(\Gamma{}_{b}){}_{\alpha}{}^{\beta}\lambda{}_{\beta}{}^{i} -\frac{1}{8}W^{-1}\nabla_{\zeta}^{t}\big(\mathcal R(S){}^{a}{}_{\eta}{}^{r \alpha j}\big)W{}_{a}{}^{b}(\Gamma{}_{b}){}_{\alpha}{}^{\beta}\lambda{}_{\beta}{}^{i}\\
&-\frac{1}{8}W^{-1}\mathcal R(S){}^{a}{}_{\eta}{}^{r \alpha j}\nabla_{\zeta}^{t}\big(W{}_{a}{}^{b}\big)(\Gamma{}_{b}){}_{\alpha}{}^{\beta}\lambda{}_{\beta}{}^{i} -\frac{1}{8}W^{-1}\mathcal R(S){}^{a}{}_{\eta}{}^{r \alpha j}W{}_{a}{}^{b}(\Gamma{}_{b}){}_{\alpha}{}^{\beta}\nabla_{\zeta}^{t}\big(\lambda{}_{\beta}{}^{i}\big)\\
&-2\nabla_{\zeta}^{t}\big(W^{-1}\big)\mathcal R(K){}_{a \eta}{}^{r a}X{}^{i j} -2W^{-1}\nabla_{\zeta}^{t}\big(\mathcal R(K){}_{a \eta}{}^{r a}\big)X{}^{i j}\\
&+2W^{-1}\mathcal R(K){}_{a \eta}{}^{r a}\nabla_{\zeta}^{t}\big(X{}^{i j}\big)
\end{aligned}
\tag{S5-H1.3-product-4}
```

Substitution of §3 and the gamma contraction (S5-V02) produce 6665 retained covariant contributions from this input. Their exact coefficients and contractions are included in §7; their locations are recorded in [the input-to-result ledger](../../../../../../../references/source_evidence/log/results/gauged_full_fermionic_log/sources/step5/endpoint_term_locations.json).


[Previous component](convention_001.md) · [Component index](../STEP_05_LOG_VECTOR.md) · [Next component](derivation_003.md)
