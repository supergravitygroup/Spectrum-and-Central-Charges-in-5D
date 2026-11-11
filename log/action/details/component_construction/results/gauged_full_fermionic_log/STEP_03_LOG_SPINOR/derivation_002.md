# LOG spinor descent — S3-H3.1-input – S3-H3.18-b

<a id="step-3--deriving-the-log-spinor--47-differentiate-every-input-in-the-w-3-sector"></a>

[Component index](../STEP_03_LOG_SPINOR.md). Definitions and source conventions are in [the opening section](convention_001.md).

### 4.7 Differentiate every input in the $`W^{-3}`$ sector

<!-- ASSERT_CONVENTION: source_frame=Gold traceless Standard-Weyl superspace, derivative_parity=odd left, fermions=all degrees retained -->

#### Input H3.1

The calculated input is

```math
\left.H^{ij}\right|_{\mathrm{H3.1}}=W^{-3}\big(\frac18X^{ij}F^{ab}F_{ab}\big).
\tag{S3-H3.1-input}
```

Apply the product rule (S3-09), in the displayed factor order:

```math
\begin{aligned}
\left.\nabla_\eta^rH^{ij}\right|_{\mathrm{H3.1}}=&\frac{1}{8}\nabla_{\eta}^{r}\big(W^{-3}\big)X{}^{i j}F{}^{a b}F{}_{a b} +\frac{1}{8}W^{-3}\nabla_{\eta}^{r}\big(X{}^{i j}\big)F{}^{a b}F{}_{a b}\\
&+\frac{1}{8}W^{-3}X{}^{i j}\nabla_{\eta}^{r}\big(F{}^{a b}\big)F{}_{a b} +\frac{1}{8}W^{-3}X{}^{i j}F{}^{a b}\nabla_{\eta}^{r}\big(F{}_{a b}\big)
\end{aligned}
\tag{S3-H3.1-a}
```

Insert the elementary source identities and the applicable commutators (S3-11)–(S3-14), distribute the vector product rules, and contract only index-raising metrics. The resulting contribution is

```math
\begin{aligned}
\left.\nabla_\eta^rH^{ij}\right|_{\mathrm{H3.1}}=&-\frac{3i}{8}W^{-4}\lambda{}_{\eta}{}^{r}X{}^{i j}F{}^{a b}F{}_{a b} +\frac{i}{8}W^{-3}\varepsilon{}^{r i}(\Gamma{}^{a}){}_{\eta}{}^{\beta}\big(\nabla_{a}\lambda{}_{\beta}{}^{j}\big)F{}^{b c}F{}_{b c}\\
&-\frac{i}{16}W^{-3}\varepsilon{}^{r i}W{}_{\eta \beta}\lambda{}^{\beta j}F{}^{a b}F{}_{a b} -\frac{3}{32}W^{-2}\varepsilon{}^{r i}X{}_{\eta}{}^{j}F{}^{a b}F{}_{a b}\\
&+\frac{i}{8}W^{-3}\varepsilon{}^{r j}(\Gamma{}^{a}){}_{\eta}{}^{\beta}\big(\nabla_{a}\lambda{}_{\beta}{}^{i}\big)F{}^{b c}F{}_{b c} -\frac{i}{16}W^{-3}\varepsilon{}^{r j}W{}_{\eta \beta}\lambda{}^{\beta i}F{}^{a b}F{}_{a b}\\
&-\frac{3}{32}W^{-2}\varepsilon{}^{r j}X{}_{\eta}{}^{i}F{}^{a b}F{}_{a b} -\frac{i}{16}W^{-3}X{}^{i j}(\Sigma{}^{a b}){}^{\beta \gamma}(\Gamma{}^{c}){}_{\eta \beta}\big(\nabla_{c}\lambda{}_{\gamma}{}^{r}\big)F{}_{a b}\\
&-\frac{i}{16}W^{-3}X{}^{i j}(\Sigma{}^{a b}){}_{\eta}{}^{\beta}(\Gamma{}^{c}){}_{\beta}{}^{\gamma}\big(\nabla_{c}\lambda{}_{\gamma}{}^{r}\big)F{}_{a b} +\frac{i}{32}W^{-3}X{}^{i j}(\Sigma{}^{a b}){}^{\beta \gamma}W{}_{\eta \beta}\lambda{}_{\gamma}{}^{r}F{}_{a b}\\
&-\frac{3i}{32}W^{-3}X{}^{i j}(\Sigma{}^{a b}){}_{\eta}{}^{\beta}W{}_{\beta}{}^{\gamma}\lambda{}_{\gamma}{}^{r}F{}_{a b} -\frac{i}{16}W^{-3}X{}^{i j}(\Sigma{}^{a b}){}^{\beta \gamma}(\Gamma{}^{c}){}_{\eta \gamma}\big(\nabla_{c}\lambda{}_{\beta}{}^{r}\big)F{}_{a b}\\
&-\frac{i}{16}W^{-3}X{}^{i j}(\Sigma{}^{a b}){}^{\beta}{}_{\eta}(\Gamma{}^{c}){}_{\beta}{}^{\gamma}\big(\nabla_{c}\lambda{}_{\gamma}{}^{r}\big)F{}_{a b} +\frac{i}{32}W^{-3}X{}^{i j}(\Sigma{}^{a b}){}^{\beta \gamma}W{}_{\eta \gamma}\lambda{}_{\beta}{}^{r}F{}_{a b}\\
&-\frac{3i}{32}W^{-3}X{}^{i j}(\Sigma{}^{a b}){}^{\beta}{}_{\eta}W{}_{\beta}{}^{\gamma}\lambda{}_{\gamma}{}^{r}F{}_{a b} -\frac{3i}{16}W^{-3}X{}^{i j}(\Sigma{}^{a b}){}^{\beta \gamma}W{}_{\beta \gamma}\lambda{}_{\eta}{}^{r}F{}_{a b}\\
&-\frac{1}{8}W^{-2}X{}^{i j}(\Sigma{}^{a b}){}^{\beta \gamma}W{}_{\eta \beta \gamma}{}^{r}F{}_{a b} -\frac{i}{16}W^{-3}X{}^{i j}F{}^{a b}(\Sigma{}_{a b}){}^{\beta \gamma}(\Gamma{}^{c}){}_{\eta \beta}\big(\nabla_{c}\lambda{}_{\gamma}{}^{r}\big)\\
&-\frac{i}{16}W^{-3}X{}^{i j}F{}^{a b}(\Sigma{}_{a b}){}_{\eta}{}^{\beta}(\Gamma{}^{c}){}_{\beta}{}^{\gamma}\big(\nabla_{c}\lambda{}_{\gamma}{}^{r}\big) +\frac{i}{32}W^{-3}X{}^{i j}F{}^{a b}(\Sigma{}_{a b}){}^{\beta \gamma}W{}_{\eta \beta}\lambda{}_{\gamma}{}^{r}\\
&-\frac{3i}{32}W^{-3}X{}^{i j}F{}^{a b}(\Sigma{}_{a b}){}_{\eta}{}^{\beta}W{}_{\beta}{}^{\gamma}\lambda{}_{\gamma}{}^{r} -\frac{i}{16}W^{-3}X{}^{i j}F{}^{a b}(\Sigma{}_{a b}){}^{\beta \gamma}(\Gamma{}^{c}){}_{\eta \gamma}\big(\nabla_{c}\lambda{}_{\beta}{}^{r}\big)\\
&-\frac{i}{16}W^{-3}X{}^{i j}F{}^{a b}(\Sigma{}_{a b}){}^{\beta}{}_{\eta}(\Gamma{}^{c}){}_{\beta}{}^{\gamma}\big(\nabla_{c}\lambda{}_{\gamma}{}^{r}\big) +\frac{i}{32}W^{-3}X{}^{i j}F{}^{a b}(\Sigma{}_{a b}){}^{\beta \gamma}W{}_{\eta \gamma}\lambda{}_{\beta}{}^{r}\\
&-\frac{3i}{32}W^{-3}X{}^{i j}F{}^{a b}(\Sigma{}_{a b}){}^{\beta}{}_{\eta}W{}_{\beta}{}^{\gamma}\lambda{}_{\gamma}{}^{r} -\frac{3i}{16}W^{-3}X{}^{i j}F{}^{a b}(\Sigma{}_{a b}){}^{\beta \gamma}W{}_{\beta \gamma}\lambda{}_{\eta}{}^{r}\\
&-\frac{1}{8}W^{-2}X{}^{i j}F{}^{a b}(\Sigma{}_{a b}){}^{\beta \gamma}W{}_{\eta \beta \gamma}{}^{r}
\end{aligned}
\tag{S3-H3.1-b}
```

**Check for H3.1:** all 27 written summands have weight $`7/2`$, odd parity and the same free indices $`\eta;r,i,j`$. Dummy labels are paired. The coefficient $`1/3`$ and the two external epsilons are applied once, when collecting the spinor.

#### Input H3.2

The calculated input is

```math
\left.H^{ij}\right|_{\mathrm{H3.2}}=W^{-3}\big(-\frac18X^{ij}X^{kl}X_{kl}\big).
\tag{S3-H3.2-input}
```

Apply the product rule (S3-09), in the displayed factor order:

```math
\begin{aligned}
\left.\nabla_\eta^rH^{ij}\right|_{\mathrm{H3.2}}=&-\frac{1}{8}\nabla_{\eta}^{r}\big(W^{-3}\big)X{}^{i j}X{}^{k l}X{}_{k l} -\frac{1}{8}W^{-3}\nabla_{\eta}^{r}\big(X{}^{i j}\big)X{}^{k l}X{}_{k l}\\
&-\frac{1}{8}W^{-3}X{}^{i j}\nabla_{\eta}^{r}\big(X{}^{k l}\big)X{}_{k l} -\frac{1}{8}W^{-3}X{}^{i j}X{}^{k l}\nabla_{\eta}^{r}\big(X{}_{k l}\big)
\end{aligned}
\tag{S3-H3.2-a}
```

Insert the elementary source identities and the applicable commutators (S3-11)–(S3-14), distribute the vector product rules, and contract only index-raising metrics. The resulting contribution is

```math
\begin{aligned}
\left.\nabla_\eta^rH^{ij}\right|_{\mathrm{H3.2}}=&\frac{3i}{8}W^{-4}\lambda{}_{\eta}{}^{r}X{}^{i j}X{}^{k l}X{}_{k l} -\frac{i}{8}W^{-3}\varepsilon{}^{r i}(\Gamma{}^{a}){}_{\eta}{}^{\beta}\big(\nabla_{a}\lambda{}_{\beta}{}^{j}\big)X{}^{k l}X{}_{k l}\\
&+\frac{i}{16}W^{-3}\varepsilon{}^{r i}W{}_{\eta \beta}\lambda{}^{\beta j}X{}^{k l}X{}_{k l} +\frac{3}{32}W^{-2}\varepsilon{}^{r i}X{}_{\eta}{}^{j}X{}^{k l}X{}_{k l}\\
&-\frac{i}{8}W^{-3}\varepsilon{}^{r j}(\Gamma{}^{a}){}_{\eta}{}^{\beta}\big(\nabla_{a}\lambda{}_{\beta}{}^{i}\big)X{}^{k l}X{}_{k l} +\frac{i}{16}W^{-3}\varepsilon{}^{r j}W{}_{\eta \beta}\lambda{}^{\beta i}X{}^{k l}X{}_{k l}\\
&+\frac{3}{32}W^{-2}\varepsilon{}^{r j}X{}_{\eta}{}^{i}X{}^{k l}X{}_{k l} -\frac{i}{8}W^{-3}X{}^{i j}(\Gamma{}^{a}){}_{\eta}{}^{\beta}\big(\nabla_{a}\lambda{}_{\beta}{}^{k}\big)X{}^{r}{}_{k}\\
&+\frac{i}{16}W^{-3}X{}^{i j}W{}_{\eta \beta}\lambda{}^{\beta k}X{}^{r}{}_{k} +\frac{3}{32}W^{-2}X{}^{i j}X{}_{\eta}{}^{k}X{}^{r}{}_{k}\\
&-\frac{i}{8}W^{-3}X{}^{i j}(\Gamma{}^{a}){}_{\eta}{}^{\beta}\big(\nabla_{a}\lambda{}_{\beta}{}^{k}\big)X{}_{k}{}^{r} +\frac{i}{16}W^{-3}X{}^{i j}W{}_{\eta \beta}\lambda{}^{\beta k}X{}_{k}{}^{r}\\
&+\frac{3}{32}W^{-2}X{}^{i j}X{}_{\eta}{}^{k}X{}_{k}{}^{r} +\frac{i}{8}W^{-3}X{}^{i j}X{}^{r k}(\Gamma{}^{a}){}_{\eta}{}^{\beta}\big(\nabla_{a}\lambda{}_{\beta k}\big)\\
&-\frac{i}{16}W^{-3}X{}^{i j}X{}^{r k}W{}_{\eta \beta}\lambda{}^{\beta}{}_{k} -\frac{3}{32}W^{-2}X{}^{i j}X{}^{r k}X{}_{\eta k}\\
&+\frac{i}{8}W^{-3}X{}^{i j}X{}^{k r}(\Gamma{}^{a}){}_{\eta}{}^{\beta}\big(\nabla_{a}\lambda{}_{\beta k}\big) -\frac{i}{16}W^{-3}X{}^{i j}X{}^{k r}W{}_{\eta \beta}\lambda{}^{\beta}{}_{k}\\
&-\frac{3}{32}W^{-2}X{}^{i j}X{}^{k r}X{}_{\eta k}
\end{aligned}
\tag{S3-H3.2-b}
```

**Check for H3.2:** all 19 written summands have weight $`7/2`$, odd parity and the same free indices $`\eta;r,i,j`$. Dummy labels are paired. The coefficient $`1/3`$ and the two external epsilons are applied once, when collecting the spinor.

#### Input H3.3

The calculated input is

```math
\left.H^{ij}\right|_{\mathrm{H3.3}}=W^{-3}\big(-\frac14X^{ij}(\nabla^aW)\nabla_aW\big).
\tag{S3-H3.3-input}
```

Expand each written SU(2) average with weight $`1/2`$ before applying the left derivative.

Apply the product rule (S3-09), in the displayed factor order:

```math
\begin{aligned}
\left.\nabla_\eta^rH^{ij}\right|_{\mathrm{H3.3}}=&-\frac{1}{4}\nabla_{\eta}^{r}\big(W^{-3}\big)X{}^{i j}\big(\nabla^{a}W\big)\big(\nabla_{a}W\big) -\frac{1}{4}W^{-3}\nabla_{\eta}^{r}\big(X{}^{i j}\big)\big(\nabla^{a}W\big)\big(\nabla_{a}W\big)\\
&-\frac{1}{4}W^{-3}X{}^{i j}\nabla_{\eta}^{r}\big(\nabla^{a}W\big)\big(\nabla_{a}W\big) -\frac{1}{4}W^{-3}X{}^{i j}\big(\nabla^{a}W\big)\nabla_{\eta}^{r}\big(\nabla_{a}W\big)
\end{aligned}
\tag{S3-H3.3-a}
```

Insert the elementary source identities and the applicable commutators (S3-11)–(S3-14), distribute the vector product rules, and contract only index-raising metrics. The resulting contribution is

```math
\begin{aligned}
\left.\nabla_\eta^rH^{ij}\right|_{\mathrm{H3.3}}=&\frac{3i}{4}W^{-4}\lambda{}_{\eta}{}^{r}X{}^{i j}\big(\nabla^{a}W\big)\big(\nabla_{a}W\big) -\frac{i}{4}W^{-3}\varepsilon{}^{r i}(\Gamma{}^{a}){}_{\eta}{}^{\beta}\big(\nabla_{a}\lambda{}_{\beta}{}^{j}\big)\big(\nabla^{b}W\big)\big(\nabla_{b}W\big)\\
&+\frac{i}{8}W^{-3}\varepsilon{}^{r i}W{}_{\eta \beta}\lambda{}^{\beta j}\big(\nabla^{a}W\big)\big(\nabla_{a}W\big) +\frac{3}{16}W^{-2}\varepsilon{}^{r i}X{}_{\eta}{}^{j}\big(\nabla^{a}W\big)\big(\nabla_{a}W\big)\\
&-\frac{i}{4}W^{-3}\varepsilon{}^{r j}(\Gamma{}^{a}){}_{\eta}{}^{\beta}\big(\nabla_{a}\lambda{}_{\beta}{}^{i}\big)\big(\nabla^{b}W\big)\big(\nabla_{b}W\big) +\frac{i}{8}W^{-3}\varepsilon{}^{r j}W{}_{\eta \beta}\lambda{}^{\beta i}\big(\nabla^{a}W\big)\big(\nabla_{a}W\big)\\
&+\frac{3}{16}W^{-2}\varepsilon{}^{r j}X{}_{\eta}{}^{i}\big(\nabla^{a}W\big)\big(\nabla_{a}W\big) -\frac{i}{4}W^{-3}X{}^{i j}\big(\nabla^{a}\lambda{}_{\eta}{}^{r}\big)\big(\nabla_{a}W\big)\\
&-\frac{i}{4}W^{-3}X{}^{i j}\mathcal T{}^{a}{}_{\eta}{}^{\beta}\lambda{}_{\beta}{}^{r}\big(\nabla_{a}W\big) -\frac{1}{4}W^{-2}X{}^{i j}\mathcal R(\mathbb D){}^{a}{}_{\eta}{}^{r}\big(\nabla_{a}W\big)\\
&-\frac{i}{4}W^{-3}X{}^{i j}\big(\nabla^{a}W\big)\big(\nabla_{a}\lambda{}_{\eta}{}^{r}\big) -\frac{i}{4}W^{-3}X{}^{i j}\big(\nabla^{a}W\big)\mathcal T{}_{a \eta}{}^{\beta}\lambda{}_{\beta}{}^{r}\\
&-\frac{1}{4}W^{-2}X{}^{i j}\big(\nabla^{a}W\big)\mathcal R(\mathbb D){}_{a \eta}{}^{r}
\end{aligned}
\tag{S3-H3.3-b}
```

**Check for H3.3:** all 13 written summands have weight $`7/2`$, odd parity and the same free indices $`\eta;r,i,j`$. Dummy labels are paired. The coefficient $`1/3`$ and the two external epsilons are applied once, when collecting the spinor.

#### Input H3.4

The calculated input is

```math
\left.H^{ij}\right|_{\mathrm{H3.4}}=W^{-3}\big(-\frac i8\varepsilon^{abcde}(\Sigma_{ab})^{\alpha\beta}F_{de}\lambda_\alpha^{(i}\nabla_c\lambda_\beta^{j)}\big).
\tag{S3-H3.4-input}
```

Expand each written SU(2) average with weight $`1/2`$ before applying the left derivative.

Apply the product rule (S3-09), in the displayed factor order:

```math
\begin{aligned}
\left.\nabla_\eta^rH^{ij}\right|_{\mathrm{H3.4}}=&-\frac{i}{16}\nabla_{\eta}^{r}\big(W^{-3}\big)\varepsilon{}^{a b c d e}(\Sigma{}_{a b}){}^{\beta \gamma}F{}_{d e}\lambda{}_{\beta}{}^{i}\big(\nabla_{c}\lambda{}_{\gamma}{}^{j}\big) -\frac{i}{16}W^{-3}\varepsilon{}^{a b c d e}(\Sigma{}_{a b}){}^{\beta \gamma}\nabla_{\eta}^{r}\big(F{}_{d e}\big)\lambda{}_{\beta}{}^{i}\big(\nabla_{c}\lambda{}_{\gamma}{}^{j}\big)\\
&-\frac{i}{16}W^{-3}\varepsilon{}^{a b c d e}(\Sigma{}_{a b}){}^{\beta \gamma}F{}_{d e}\nabla_{\eta}^{r}\big(\lambda{}_{\beta}{}^{i}\big)\big(\nabla_{c}\lambda{}_{\gamma}{}^{j}\big) +\frac{i}{16}W^{-3}\varepsilon{}^{a b c d e}(\Sigma{}_{a b}){}^{\beta \gamma}F{}_{d e}\lambda{}_{\beta}{}^{i}\nabla_{\eta}^{r}\big(\nabla_{c}\lambda{}_{\gamma}{}^{j}\big)\\
&-\frac{i}{16}\nabla_{\eta}^{r}\big(W^{-3}\big)\varepsilon{}^{a b c d e}(\Sigma{}_{a b}){}^{\beta \gamma}F{}_{d e}\lambda{}_{\beta}{}^{j}\big(\nabla_{c}\lambda{}_{\gamma}{}^{i}\big) -\frac{i}{16}W^{-3}\varepsilon{}^{a b c d e}(\Sigma{}_{a b}){}^{\beta \gamma}\nabla_{\eta}^{r}\big(F{}_{d e}\big)\lambda{}_{\beta}{}^{j}\big(\nabla_{c}\lambda{}_{\gamma}{}^{i}\big)\\
&-\frac{i}{16}W^{-3}\varepsilon{}^{a b c d e}(\Sigma{}_{a b}){}^{\beta \gamma}F{}_{d e}\nabla_{\eta}^{r}\big(\lambda{}_{\beta}{}^{j}\big)\big(\nabla_{c}\lambda{}_{\gamma}{}^{i}\big) +\frac{i}{16}W^{-3}\varepsilon{}^{a b c d e}(\Sigma{}_{a b}){}^{\beta \gamma}F{}_{d e}\lambda{}_{\beta}{}^{j}\nabla_{\eta}^{r}\big(\nabla_{c}\lambda{}_{\gamma}{}^{i}\big)
\end{aligned}
\tag{S3-H3.4-a}
```

Insert the elementary source identities and the applicable commutators (S3-11)–(S3-14), distribute the vector product rules, and contract only index-raising metrics. The resulting contribution is

```math
\begin{aligned}
\left.\nabla_\eta^rH^{ij}\right|_{\mathrm{H3.4}}=&-\frac{3}{16}W^{-4}\lambda{}_{\eta}{}^{r}\varepsilon{}^{a b c d e}(\Sigma{}_{a b}){}^{\beta \gamma}F{}_{d e}\lambda{}_{\beta}{}^{i}\big(\nabla_{c}\lambda{}_{\gamma}{}^{j}\big) -\frac{1}{32}W^{-3}\varepsilon{}^{a b c d e}(\Sigma{}_{a b}){}^{\beta \gamma}(\Sigma{}_{d e}){}^{\delta \rho}(\Gamma{}^{f}){}_{\eta \delta}\big(\nabla_{f}\lambda{}_{\rho}{}^{r}\big)\lambda{}_{\beta}{}^{i}\big(\nabla_{c}\lambda{}_{\gamma}{}^{j}\big)\\
&-\frac{1}{32}W^{-3}\varepsilon{}^{a b c d e}(\Sigma{}_{a b}){}^{\beta \gamma}(\Sigma{}_{d e}){}_{\eta}{}^{\delta}(\Gamma{}^{f}){}_{\delta}{}^{\rho}\big(\nabla_{f}\lambda{}_{\rho}{}^{r}\big)\lambda{}_{\beta}{}^{i}\big(\nabla_{c}\lambda{}_{\gamma}{}^{j}\big) +\frac{1}{64}W^{-3}\varepsilon{}^{a b c d e}(\Sigma{}_{a b}){}^{\beta \gamma}(\Sigma{}_{d e}){}^{\delta \rho}W{}_{\eta \delta}\lambda{}_{\rho}{}^{r}\lambda{}_{\beta}{}^{i}\big(\nabla_{c}\lambda{}_{\gamma}{}^{j}\big)\\
&-\frac{3}{64}W^{-3}\varepsilon{}^{a b c d e}(\Sigma{}_{a b}){}^{\beta \gamma}(\Sigma{}_{d e}){}_{\eta}{}^{\delta}W{}_{\delta}{}^{\rho}\lambda{}_{\rho}{}^{r}\lambda{}_{\beta}{}^{i}\big(\nabla_{c}\lambda{}_{\gamma}{}^{j}\big) -\frac{1}{32}W^{-3}\varepsilon{}^{a b c d e}(\Sigma{}_{a b}){}^{\beta \gamma}(\Sigma{}_{d e}){}^{\delta \rho}(\Gamma{}^{f}){}_{\eta \rho}\big(\nabla_{f}\lambda{}_{\delta}{}^{r}\big)\lambda{}_{\beta}{}^{i}\big(\nabla_{c}\lambda{}_{\gamma}{}^{j}\big)\\
&-\frac{1}{32}W^{-3}\varepsilon{}^{a b c d e}(\Sigma{}_{a b}){}^{\beta \gamma}(\Sigma{}_{d e}){}^{\delta}{}_{\eta}(\Gamma{}^{f}){}_{\delta}{}^{\rho}\big(\nabla_{f}\lambda{}_{\rho}{}^{r}\big)\lambda{}_{\beta}{}^{i}\big(\nabla_{c}\lambda{}_{\gamma}{}^{j}\big) +\frac{1}{64}W^{-3}\varepsilon{}^{a b c d e}(\Sigma{}_{a b}){}^{\beta \gamma}(\Sigma{}_{d e}){}^{\delta \rho}W{}_{\eta \rho}\lambda{}_{\delta}{}^{r}\lambda{}_{\beta}{}^{i}\big(\nabla_{c}\lambda{}_{\gamma}{}^{j}\big)\\
&-\frac{3}{64}W^{-3}\varepsilon{}^{a b c d e}(\Sigma{}_{a b}){}^{\beta \gamma}(\Sigma{}_{d e}){}^{\delta}{}_{\eta}W{}_{\delta}{}^{\rho}\lambda{}_{\rho}{}^{r}\lambda{}_{\beta}{}^{i}\big(\nabla_{c}\lambda{}_{\gamma}{}^{j}\big) -\frac{3}{32}W^{-3}\varepsilon{}^{a b c d e}(\Sigma{}_{a b}){}^{\beta \gamma}(\Sigma{}_{d e}){}^{\delta \rho}W{}_{\delta \rho}\lambda{}_{\eta}{}^{r}\lambda{}_{\beta}{}^{i}\big(\nabla_{c}\lambda{}_{\gamma}{}^{j}\big)\\
&+\frac{i}{16}W^{-2}\varepsilon{}^{a b c d e}(\Sigma{}_{a b}){}^{\beta \gamma}(\Sigma{}_{d e}){}^{\delta \rho}W{}_{\eta \delta \rho}{}^{r}\lambda{}_{\beta}{}^{i}\big(\nabla_{c}\lambda{}_{\gamma}{}^{j}\big) +\frac{i}{8}W^{-3}\varepsilon{}^{a b c d e}(\Sigma{}_{a b}){}^{\beta \gamma}F{}_{d e}\varepsilon{}^{r i}F{}_{\eta \beta}\big(\nabla_{c}\lambda{}_{\gamma}{}^{j}\big)\\
&+\frac{i}{8}W^{-2}\varepsilon{}^{a b c d e}(\Sigma{}_{a b}){}^{\beta \gamma}F{}_{d e}\varepsilon{}^{r i}W{}_{\eta \beta}\big(\nabla_{c}\lambda{}_{\gamma}{}^{j}\big) +\frac{i}{16}W^{-3}\varepsilon{}^{a b c d e}(\Sigma{}_{a b}){}_{\eta}{}^{\beta}F{}_{d e}X{}^{r i}\big(\nabla_{c}\lambda{}_{\beta}{}^{j}\big)\\
&+\frac{i}{16}W^{-3}\varepsilon{}^{a b c d e}(\Sigma{}_{a b}){}^{\beta \gamma}F{}_{d e}\varepsilon{}^{r i}(\Gamma{}^{f}){}_{\eta \beta}\big(\nabla_{f}W\big)\big(\nabla_{c}\lambda{}_{\gamma}{}^{j}\big) -\frac{i}{8}W^{-3}\varepsilon{}^{a b c d e}(\Sigma{}_{a b}){}^{\beta \gamma}F{}_{d e}\lambda{}_{\beta}{}^{i}\varepsilon{}^{r j}\big(\nabla_{c}F{}_{\eta \gamma}\big)\\
&-\frac{i}{8}W^{-2}\varepsilon{}^{a b c d e}(\Sigma{}_{a b}){}^{\beta \gamma}F{}_{d e}\lambda{}_{\beta}{}^{i}\varepsilon{}^{r j}\big(\nabla_{c}W{}_{\eta \gamma}\big) -\frac{i}{8}W^{-3}\varepsilon{}^{a b c d e}(\Sigma{}_{a b}){}^{\beta \gamma}F{}_{d e}\lambda{}_{\beta}{}^{i}\varepsilon{}^{r j}W{}_{\eta \gamma}\big(\nabla_{c}W\big)\\
&-\frac{i}{16}W^{-3}\varepsilon{}^{a b c d e}(\Sigma{}_{a b}){}^{\beta}{}_{\eta}F{}_{d e}\lambda{}_{\beta}{}^{i}\big(\nabla_{c}X{}^{r j}\big) -\frac{i}{16}W^{-3}\varepsilon{}^{a b c d e}(\Sigma{}_{a b}){}^{\beta \gamma}F{}_{d e}\lambda{}_{\beta}{}^{i}\varepsilon{}^{r j}(\Gamma{}^{f}){}_{\eta \gamma}\big(\nabla_{c}\nabla_{f}W\big)\\
&-\frac{i}{8}W^{-3}\varepsilon{}^{a b c d e}(\Sigma{}_{a b}){}^{\beta \gamma}F{}_{d e}\lambda{}_{\beta}{}^{i}\mathcal T{}_{c \eta}{}^{\delta}\varepsilon{}^{r j}F{}_{\delta \gamma} -\frac{i}{8}W^{-2}\varepsilon{}^{a b c d e}(\Sigma{}_{a b}){}^{\beta \gamma}F{}_{d e}\lambda{}_{\beta}{}^{i}\mathcal T{}_{c \eta}{}^{\delta}\varepsilon{}^{r j}W{}_{\delta \gamma}\\
&-\frac{i}{16}W^{-3}\varepsilon{}^{a b c d e}(\Sigma{}_{a b}){}^{\beta}{}_{\gamma}F{}_{d e}\lambda{}_{\beta}{}^{i}\mathcal T{}_{c \eta}{}^{\gamma}X{}^{r j} -\frac{i}{16}W^{-3}\varepsilon{}^{a b c d e}(\Sigma{}_{a b}){}^{\beta \gamma}F{}_{d e}\lambda{}_{\beta}{}^{i}\mathcal T{}_{c \eta}{}^{\delta}\varepsilon{}^{r j}(\Gamma{}^{f}){}_{\delta \gamma}\big(\nabla_{f}W\big)\\
&+\frac{i}{32}W^{-3}\varepsilon{}^{a b c d e}(\Sigma{}_{a b}){}^{\beta \gamma}F{}_{d e}\lambda{}_{\beta}{}^{i}\mathcal R(M){}_{c \eta}{}^{r f g}(\Sigma{}_{f g}){}_{\gamma}{}^{\delta}\lambda{}_{\delta}{}^{j} +\frac{3i}{32}W^{-3}\varepsilon{}^{a b c d e}(\Sigma{}_{a b}){}^{\beta \gamma}F{}_{d e}\lambda{}_{\beta}{}^{i}\mathcal R(\mathbb D){}_{c \eta}{}^{r}\lambda{}_{\gamma}{}^{j}\\
&-\frac{i}{32}W^{-3}\varepsilon{}^{a b c d e}(\Sigma{}_{a b}){}^{\beta \gamma}F{}_{d e}\lambda{}_{\beta}{}^{i}\mathcal R(J){}_{c \eta}{}^{r j k}\lambda{}_{\gamma k} -\frac{i}{32}W^{-3}\varepsilon{}^{a b c d e}(\Sigma{}_{a b}){}^{\beta \gamma}F{}_{d e}\lambda{}_{\beta}{}^{i}\mathcal R(J){}_{c \eta}{}^{r k j}\lambda{}_{\gamma k}\\
&+\frac{1}{8}W^{-2}\varepsilon{}^{a b c d e}(\Sigma{}_{a b}){}^{\beta}{}_{\gamma}F{}_{d e}\lambda{}_{\beta}{}^{i}\mathcal R(S){}_{c \eta}{}^{r \gamma j} -\frac{3}{16}W^{-4}\lambda{}_{\eta}{}^{r}\varepsilon{}^{a b c d e}(\Sigma{}_{a b}){}^{\beta \gamma}F{}_{d e}\lambda{}_{\beta}{}^{j}\big(\nabla_{c}\lambda{}_{\gamma}{}^{i}\big)\\
&-\frac{1}{32}W^{-3}\varepsilon{}^{a b c d e}(\Sigma{}_{a b}){}^{\beta \gamma}(\Sigma{}_{d e}){}^{\delta \rho}(\Gamma{}^{f}){}_{\eta \delta}\big(\nabla_{f}\lambda{}_{\rho}{}^{r}\big)\lambda{}_{\beta}{}^{j}\big(\nabla_{c}\lambda{}_{\gamma}{}^{i}\big) -\frac{1}{32}W^{-3}\varepsilon{}^{a b c d e}(\Sigma{}_{a b}){}^{\beta \gamma}(\Sigma{}_{d e}){}_{\eta}{}^{\delta}(\Gamma{}^{f}){}_{\delta}{}^{\rho}\big(\nabla_{f}\lambda{}_{\rho}{}^{r}\big)\lambda{}_{\beta}{}^{j}\big(\nabla_{c}\lambda{}_{\gamma}{}^{i}\big)\\
&+\frac{1}{64}W^{-3}\varepsilon{}^{a b c d e}(\Sigma{}_{a b}){}^{\beta \gamma}(\Sigma{}_{d e}){}^{\delta \rho}W{}_{\eta \delta}\lambda{}_{\rho}{}^{r}\lambda{}_{\beta}{}^{j}\big(\nabla_{c}\lambda{}_{\gamma}{}^{i}\big) -\frac{3}{64}W^{-3}\varepsilon{}^{a b c d e}(\Sigma{}_{a b}){}^{\beta \gamma}(\Sigma{}_{d e}){}_{\eta}{}^{\delta}W{}_{\delta}{}^{\rho}\lambda{}_{\rho}{}^{r}\lambda{}_{\beta}{}^{j}\big(\nabla_{c}\lambda{}_{\gamma}{}^{i}\big)\\
&-\frac{1}{32}W^{-3}\varepsilon{}^{a b c d e}(\Sigma{}_{a b}){}^{\beta \gamma}(\Sigma{}_{d e}){}^{\delta \rho}(\Gamma{}^{f}){}_{\eta \rho}\big(\nabla_{f}\lambda{}_{\delta}{}^{r}\big)\lambda{}_{\beta}{}^{j}\big(\nabla_{c}\lambda{}_{\gamma}{}^{i}\big) -\frac{1}{32}W^{-3}\varepsilon{}^{a b c d e}(\Sigma{}_{a b}){}^{\beta \gamma}(\Sigma{}_{d e}){}^{\delta}{}_{\eta}(\Gamma{}^{f}){}_{\delta}{}^{\rho}\big(\nabla_{f}\lambda{}_{\rho}{}^{r}\big)\lambda{}_{\beta}{}^{j}\big(\nabla_{c}\lambda{}_{\gamma}{}^{i}\big)\\
&+\frac{1}{64}W^{-3}\varepsilon{}^{a b c d e}(\Sigma{}_{a b}){}^{\beta \gamma}(\Sigma{}_{d e}){}^{\delta \rho}W{}_{\eta \rho}\lambda{}_{\delta}{}^{r}\lambda{}_{\beta}{}^{j}\big(\nabla_{c}\lambda{}_{\gamma}{}^{i}\big) -\frac{3}{64}W^{-3}\varepsilon{}^{a b c d e}(\Sigma{}_{a b}){}^{\beta \gamma}(\Sigma{}_{d e}){}^{\delta}{}_{\eta}W{}_{\delta}{}^{\rho}\lambda{}_{\rho}{}^{r}\lambda{}_{\beta}{}^{j}\big(\nabla_{c}\lambda{}_{\gamma}{}^{i}\big)\\
&-\frac{3}{32}W^{-3}\varepsilon{}^{a b c d e}(\Sigma{}_{a b}){}^{\beta \gamma}(\Sigma{}_{d e}){}^{\delta \rho}W{}_{\delta \rho}\lambda{}_{\eta}{}^{r}\lambda{}_{\beta}{}^{j}\big(\nabla_{c}\lambda{}_{\gamma}{}^{i}\big) +\frac{i}{16}W^{-2}\varepsilon{}^{a b c d e}(\Sigma{}_{a b}){}^{\beta \gamma}(\Sigma{}_{d e}){}^{\delta \rho}W{}_{\eta \delta \rho}{}^{r}\lambda{}_{\beta}{}^{j}\big(\nabla_{c}\lambda{}_{\gamma}{}^{i}\big)\\
&+\frac{i}{8}W^{-3}\varepsilon{}^{a b c d e}(\Sigma{}_{a b}){}^{\beta \gamma}F{}_{d e}\varepsilon{}^{r j}F{}_{\eta \beta}\big(\nabla_{c}\lambda{}_{\gamma}{}^{i}\big) +\frac{i}{8}W^{-2}\varepsilon{}^{a b c d e}(\Sigma{}_{a b}){}^{\beta \gamma}F{}_{d e}\varepsilon{}^{r j}W{}_{\eta \beta}\big(\nabla_{c}\lambda{}_{\gamma}{}^{i}\big)\\
&+\frac{i}{16}W^{-3}\varepsilon{}^{a b c d e}(\Sigma{}_{a b}){}_{\eta}{}^{\beta}F{}_{d e}X{}^{r j}\big(\nabla_{c}\lambda{}_{\beta}{}^{i}\big) +\frac{i}{16}W^{-3}\varepsilon{}^{a b c d e}(\Sigma{}_{a b}){}^{\beta \gamma}F{}_{d e}\varepsilon{}^{r j}(\Gamma{}^{f}){}_{\eta \beta}\big(\nabla_{f}W\big)\big(\nabla_{c}\lambda{}_{\gamma}{}^{i}\big)\\
&-\frac{i}{8}W^{-3}\varepsilon{}^{a b c d e}(\Sigma{}_{a b}){}^{\beta \gamma}F{}_{d e}\lambda{}_{\beta}{}^{j}\varepsilon{}^{r i}\big(\nabla_{c}F{}_{\eta \gamma}\big) -\frac{i}{8}W^{-2}\varepsilon{}^{a b c d e}(\Sigma{}_{a b}){}^{\beta \gamma}F{}_{d e}\lambda{}_{\beta}{}^{j}\varepsilon{}^{r i}\big(\nabla_{c}W{}_{\eta \gamma}\big)\\
&-\frac{i}{8}W^{-3}\varepsilon{}^{a b c d e}(\Sigma{}_{a b}){}^{\beta \gamma}F{}_{d e}\lambda{}_{\beta}{}^{j}\varepsilon{}^{r i}W{}_{\eta \gamma}\big(\nabla_{c}W\big) -\frac{i}{16}W^{-3}\varepsilon{}^{a b c d e}(\Sigma{}_{a b}){}^{\beta}{}_{\eta}F{}_{d e}\lambda{}_{\beta}{}^{j}\big(\nabla_{c}X{}^{r i}\big)\\
&-\frac{i}{16}W^{-3}\varepsilon{}^{a b c d e}(\Sigma{}_{a b}){}^{\beta \gamma}F{}_{d e}\lambda{}_{\beta}{}^{j}\varepsilon{}^{r i}(\Gamma{}^{f}){}_{\eta \gamma}\big(\nabla_{c}\nabla_{f}W\big) -\frac{i}{8}W^{-3}\varepsilon{}^{a b c d e}(\Sigma{}_{a b}){}^{\beta \gamma}F{}_{d e}\lambda{}_{\beta}{}^{j}\mathcal T{}_{c \eta}{}^{\delta}\varepsilon{}^{r i}F{}_{\delta \gamma}\\
&-\frac{i}{8}W^{-2}\varepsilon{}^{a b c d e}(\Sigma{}_{a b}){}^{\beta \gamma}F{}_{d e}\lambda{}_{\beta}{}^{j}\mathcal T{}_{c \eta}{}^{\delta}\varepsilon{}^{r i}W{}_{\delta \gamma} -\frac{i}{16}W^{-3}\varepsilon{}^{a b c d e}(\Sigma{}_{a b}){}^{\beta}{}_{\gamma}F{}_{d e}\lambda{}_{\beta}{}^{j}\mathcal T{}_{c \eta}{}^{\gamma}X{}^{r i}\\
&-\frac{i}{16}W^{-3}\varepsilon{}^{a b c d e}(\Sigma{}_{a b}){}^{\beta \gamma}F{}_{d e}\lambda{}_{\beta}{}^{j}\mathcal T{}_{c \eta}{}^{\delta}\varepsilon{}^{r i}(\Gamma{}^{f}){}_{\delta \gamma}\big(\nabla_{f}W\big) +\frac{i}{32}W^{-3}\varepsilon{}^{a b c d e}(\Sigma{}_{a b}){}^{\beta \gamma}F{}_{d e}\lambda{}_{\beta}{}^{j}\mathcal R(M){}_{c \eta}{}^{r f g}(\Sigma{}_{f g}){}_{\gamma}{}^{\delta}\lambda{}_{\delta}{}^{i}\\
&+\frac{3i}{32}W^{-3}\varepsilon{}^{a b c d e}(\Sigma{}_{a b}){}^{\beta \gamma}F{}_{d e}\lambda{}_{\beta}{}^{j}\mathcal R(\mathbb D){}_{c \eta}{}^{r}\lambda{}_{\gamma}{}^{i} -\frac{i}{32}W^{-3}\varepsilon{}^{a b c d e}(\Sigma{}_{a b}){}^{\beta \gamma}F{}_{d e}\lambda{}_{\beta}{}^{j}\mathcal R(J){}_{c \eta}{}^{r i k}\lambda{}_{\gamma k}\\
&-\frac{i}{32}W^{-3}\varepsilon{}^{a b c d e}(\Sigma{}_{a b}){}^{\beta \gamma}F{}_{d e}\lambda{}_{\beta}{}^{j}\mathcal R(J){}_{c \eta}{}^{r k i}\lambda{}_{\gamma k} +\frac{1}{8}W^{-2}\varepsilon{}^{a b c d e}(\Sigma{}_{a b}){}^{\beta}{}_{\gamma}F{}_{d e}\lambda{}_{\beta}{}^{j}\mathcal R(S){}_{c \eta}{}^{r \gamma i}
\end{aligned}
\tag{S3-H3.4-b}
```

**Check for H3.4:** all 58 written summands have weight $`7/2`$, odd parity and the same free indices $`\eta;r,i,j`$. Dummy labels are paired. The coefficient $`1/3`$ and the two external epsilons are applied once, when collecting the spinor.

#### Input H3.5

The calculated input is

```math
\left.H^{ij}\right|_{\mathrm{H3.5}}=W^{-3}\big(-\frac i4(\Gamma^a)^{\alpha\beta}F_{ab}\lambda_\alpha^{(i}\nabla^b\lambda_\beta^{j)}\big).
\tag{S3-H3.5-input}
```

Expand each written SU(2) average with weight $`1/2`$ before applying the left derivative.

Apply the product rule (S3-09), in the displayed factor order:

```math
\begin{aligned}
\left.\nabla_\eta^rH^{ij}\right|_{\mathrm{H3.5}}=&-\frac{i}{8}\nabla_{\eta}^{r}\big(W^{-3}\big)(\Gamma{}^{a}){}^{\beta \gamma}F{}_{a b}\lambda{}_{\beta}{}^{i}\big(\nabla^{b}\lambda{}_{\gamma}{}^{j}\big) -\frac{i}{8}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}\nabla_{\eta}^{r}\big(F{}_{a b}\big)\lambda{}_{\beta}{}^{i}\big(\nabla^{b}\lambda{}_{\gamma}{}^{j}\big)\\
&-\frac{i}{8}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}F{}_{a b}\nabla_{\eta}^{r}\big(\lambda{}_{\beta}{}^{i}\big)\big(\nabla^{b}\lambda{}_{\gamma}{}^{j}\big) +\frac{i}{8}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}F{}_{a b}\lambda{}_{\beta}{}^{i}\nabla_{\eta}^{r}\big(\nabla^{b}\lambda{}_{\gamma}{}^{j}\big)\\
&-\frac{i}{8}\nabla_{\eta}^{r}\big(W^{-3}\big)(\Gamma{}^{a}){}^{\beta \gamma}F{}_{a b}\lambda{}_{\beta}{}^{j}\big(\nabla^{b}\lambda{}_{\gamma}{}^{i}\big) -\frac{i}{8}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}\nabla_{\eta}^{r}\big(F{}_{a b}\big)\lambda{}_{\beta}{}^{j}\big(\nabla^{b}\lambda{}_{\gamma}{}^{i}\big)\\
&-\frac{i}{8}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}F{}_{a b}\nabla_{\eta}^{r}\big(\lambda{}_{\beta}{}^{j}\big)\big(\nabla^{b}\lambda{}_{\gamma}{}^{i}\big) +\frac{i}{8}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}F{}_{a b}\lambda{}_{\beta}{}^{j}\nabla_{\eta}^{r}\big(\nabla^{b}\lambda{}_{\gamma}{}^{i}\big)
\end{aligned}
\tag{S3-H3.5-a}
```

Insert the elementary source identities and the applicable commutators (S3-11)–(S3-14), distribute the vector product rules, and contract only index-raising metrics. The resulting contribution is

```math
\begin{aligned}
\left.\nabla_\eta^rH^{ij}\right|_{\mathrm{H3.5}}=&-\frac{3}{8}W^{-4}\lambda{}_{\eta}{}^{r}(\Gamma{}^{a}){}^{\beta \gamma}F{}_{a b}\lambda{}_{\beta}{}^{i}\big(\nabla^{b}\lambda{}_{\gamma}{}^{j}\big) -\frac{1}{16}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}(\Sigma{}_{a b}){}^{\delta \rho}(\Gamma{}^{c}){}_{\eta \delta}\big(\nabla_{c}\lambda{}_{\rho}{}^{r}\big)\lambda{}_{\beta}{}^{i}\big(\nabla^{b}\lambda{}_{\gamma}{}^{j}\big)\\
&-\frac{1}{16}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}(\Sigma{}_{a b}){}_{\eta}{}^{\delta}(\Gamma{}^{c}){}_{\delta}{}^{\rho}\big(\nabla_{c}\lambda{}_{\rho}{}^{r}\big)\lambda{}_{\beta}{}^{i}\big(\nabla^{b}\lambda{}_{\gamma}{}^{j}\big) +\frac{1}{32}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}(\Sigma{}_{a b}){}^{\delta \rho}W{}_{\eta \delta}\lambda{}_{\rho}{}^{r}\lambda{}_{\beta}{}^{i}\big(\nabla^{b}\lambda{}_{\gamma}{}^{j}\big)\\
&-\frac{3}{32}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}(\Sigma{}_{a b}){}_{\eta}{}^{\delta}W{}_{\delta}{}^{\rho}\lambda{}_{\rho}{}^{r}\lambda{}_{\beta}{}^{i}\big(\nabla^{b}\lambda{}_{\gamma}{}^{j}\big) -\frac{1}{16}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}(\Sigma{}_{a b}){}^{\delta \rho}(\Gamma{}^{c}){}_{\eta \rho}\big(\nabla_{c}\lambda{}_{\delta}{}^{r}\big)\lambda{}_{\beta}{}^{i}\big(\nabla^{b}\lambda{}_{\gamma}{}^{j}\big)\\
&-\frac{1}{16}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}(\Sigma{}_{a b}){}^{\delta}{}_{\eta}(\Gamma{}^{c}){}_{\delta}{}^{\rho}\big(\nabla_{c}\lambda{}_{\rho}{}^{r}\big)\lambda{}_{\beta}{}^{i}\big(\nabla^{b}\lambda{}_{\gamma}{}^{j}\big) +\frac{1}{32}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}(\Sigma{}_{a b}){}^{\delta \rho}W{}_{\eta \rho}\lambda{}_{\delta}{}^{r}\lambda{}_{\beta}{}^{i}\big(\nabla^{b}\lambda{}_{\gamma}{}^{j}\big)\\
&-\frac{3}{32}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}(\Sigma{}_{a b}){}^{\delta}{}_{\eta}W{}_{\delta}{}^{\rho}\lambda{}_{\rho}{}^{r}\lambda{}_{\beta}{}^{i}\big(\nabla^{b}\lambda{}_{\gamma}{}^{j}\big) -\frac{3}{16}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}(\Sigma{}_{a b}){}^{\delta \rho}W{}_{\delta \rho}\lambda{}_{\eta}{}^{r}\lambda{}_{\beta}{}^{i}\big(\nabla^{b}\lambda{}_{\gamma}{}^{j}\big)\\
&+\frac{i}{8}W^{-2}(\Gamma{}^{a}){}^{\beta \gamma}(\Sigma{}_{a b}){}^{\delta \rho}W{}_{\eta \delta \rho}{}^{r}\lambda{}_{\beta}{}^{i}\big(\nabla^{b}\lambda{}_{\gamma}{}^{j}\big) +\frac{i}{4}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}F{}_{a b}\varepsilon{}^{r i}F{}_{\eta \beta}\big(\nabla^{b}\lambda{}_{\gamma}{}^{j}\big)\\
&+\frac{i}{4}W^{-2}(\Gamma{}^{a}){}^{\beta \gamma}F{}_{a b}\varepsilon{}^{r i}W{}_{\eta \beta}\big(\nabla^{b}\lambda{}_{\gamma}{}^{j}\big) +\frac{i}{8}W^{-3}(\Gamma{}^{a}){}_{\eta}{}^{\beta}F{}_{a b}X{}^{r i}\big(\nabla^{b}\lambda{}_{\beta}{}^{j}\big)\\
&+\frac{i}{8}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}F{}_{a b}\varepsilon{}^{r i}(\Gamma{}^{c}){}_{\eta \beta}\big(\nabla_{c}W\big)\big(\nabla^{b}\lambda{}_{\gamma}{}^{j}\big) -\frac{i}{4}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}F{}_{a b}\lambda{}_{\beta}{}^{i}\varepsilon{}^{r j}\big(\nabla^{b}F{}_{\eta \gamma}\big)\\
&-\frac{i}{4}W^{-2}(\Gamma{}^{a}){}^{\beta \gamma}F{}_{a b}\lambda{}_{\beta}{}^{i}\varepsilon{}^{r j}\big(\nabla^{b}W{}_{\eta \gamma}\big) -\frac{i}{4}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}F{}_{a b}\lambda{}_{\beta}{}^{i}\varepsilon{}^{r j}W{}_{\eta \gamma}\big(\nabla^{b}W\big)\\
&-\frac{i}{8}W^{-3}(\Gamma{}^{a}){}^{\beta}{}_{\eta}F{}_{a b}\lambda{}_{\beta}{}^{i}\big(\nabla^{b}X{}^{r j}\big) -\frac{i}{8}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}F{}_{a b}\lambda{}_{\beta}{}^{i}\varepsilon{}^{r j}(\Gamma{}^{c}){}_{\eta \gamma}\big(\nabla^{b}\nabla_{c}W\big)\\
&-\frac{i}{4}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}F{}_{a b}\lambda{}_{\beta}{}^{i}\mathcal T{}^{b}{}_{\eta}{}^{\delta}\varepsilon{}^{r j}F{}_{\delta \gamma} -\frac{i}{4}W^{-2}(\Gamma{}^{a}){}^{\beta \gamma}F{}_{a b}\lambda{}_{\beta}{}^{i}\mathcal T{}^{b}{}_{\eta}{}^{\delta}\varepsilon{}^{r j}W{}_{\delta \gamma}\\
&-\frac{i}{8}W^{-3}(\Gamma{}^{a}){}^{\beta}{}_{\gamma}F{}_{a b}\lambda{}_{\beta}{}^{i}\mathcal T{}^{b}{}_{\eta}{}^{\gamma}X{}^{r j} -\frac{i}{8}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}F{}_{a b}\lambda{}_{\beta}{}^{i}\mathcal T{}^{b}{}_{\eta}{}^{\delta}\varepsilon{}^{r j}(\Gamma{}^{c}){}_{\delta \gamma}\big(\nabla_{c}W\big)\\
&+\frac{i}{16}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}F{}_{a b}\lambda{}_{\beta}{}^{i}\mathcal R(M){}^{b}{}_{\eta}{}^{r c d}(\Sigma{}_{c d}){}_{\gamma}{}^{\delta}\lambda{}_{\delta}{}^{j} +\frac{3i}{16}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}F{}_{a b}\lambda{}_{\beta}{}^{i}\mathcal R(\mathbb D){}^{b}{}_{\eta}{}^{r}\lambda{}_{\gamma}{}^{j}\\
&-\frac{i}{16}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}F{}_{a b}\lambda{}_{\beta}{}^{i}\mathcal R(J){}^{b}{}_{\eta}{}^{r j k}\lambda{}_{\gamma k} -\frac{i}{16}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}F{}_{a b}\lambda{}_{\beta}{}^{i}\mathcal R(J){}^{b}{}_{\eta}{}^{r k j}\lambda{}_{\gamma k}\\
&+\frac{1}{4}W^{-2}(\Gamma{}^{a}){}^{\beta}{}_{\gamma}F{}_{a b}\lambda{}_{\beta}{}^{i}\mathcal R(S){}^{b}{}_{\eta}{}^{r \gamma j} -\frac{3}{8}W^{-4}\lambda{}_{\eta}{}^{r}(\Gamma{}^{a}){}^{\beta \gamma}F{}_{a b}\lambda{}_{\beta}{}^{j}\big(\nabla^{b}\lambda{}_{\gamma}{}^{i}\big)\\
&-\frac{1}{16}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}(\Sigma{}_{a b}){}^{\delta \rho}(\Gamma{}^{c}){}_{\eta \delta}\big(\nabla_{c}\lambda{}_{\rho}{}^{r}\big)\lambda{}_{\beta}{}^{j}\big(\nabla^{b}\lambda{}_{\gamma}{}^{i}\big) -\frac{1}{16}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}(\Sigma{}_{a b}){}_{\eta}{}^{\delta}(\Gamma{}^{c}){}_{\delta}{}^{\rho}\big(\nabla_{c}\lambda{}_{\rho}{}^{r}\big)\lambda{}_{\beta}{}^{j}\big(\nabla^{b}\lambda{}_{\gamma}{}^{i}\big)\\
&+\frac{1}{32}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}(\Sigma{}_{a b}){}^{\delta \rho}W{}_{\eta \delta}\lambda{}_{\rho}{}^{r}\lambda{}_{\beta}{}^{j}\big(\nabla^{b}\lambda{}_{\gamma}{}^{i}\big) -\frac{3}{32}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}(\Sigma{}_{a b}){}_{\eta}{}^{\delta}W{}_{\delta}{}^{\rho}\lambda{}_{\rho}{}^{r}\lambda{}_{\beta}{}^{j}\big(\nabla^{b}\lambda{}_{\gamma}{}^{i}\big)\\
&-\frac{1}{16}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}(\Sigma{}_{a b}){}^{\delta \rho}(\Gamma{}^{c}){}_{\eta \rho}\big(\nabla_{c}\lambda{}_{\delta}{}^{r}\big)\lambda{}_{\beta}{}^{j}\big(\nabla^{b}\lambda{}_{\gamma}{}^{i}\big) -\frac{1}{16}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}(\Sigma{}_{a b}){}^{\delta}{}_{\eta}(\Gamma{}^{c}){}_{\delta}{}^{\rho}\big(\nabla_{c}\lambda{}_{\rho}{}^{r}\big)\lambda{}_{\beta}{}^{j}\big(\nabla^{b}\lambda{}_{\gamma}{}^{i}\big)\\
&+\frac{1}{32}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}(\Sigma{}_{a b}){}^{\delta \rho}W{}_{\eta \rho}\lambda{}_{\delta}{}^{r}\lambda{}_{\beta}{}^{j}\big(\nabla^{b}\lambda{}_{\gamma}{}^{i}\big) -\frac{3}{32}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}(\Sigma{}_{a b}){}^{\delta}{}_{\eta}W{}_{\delta}{}^{\rho}\lambda{}_{\rho}{}^{r}\lambda{}_{\beta}{}^{j}\big(\nabla^{b}\lambda{}_{\gamma}{}^{i}\big)\\
&-\frac{3}{16}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}(\Sigma{}_{a b}){}^{\delta \rho}W{}_{\delta \rho}\lambda{}_{\eta}{}^{r}\lambda{}_{\beta}{}^{j}\big(\nabla^{b}\lambda{}_{\gamma}{}^{i}\big) +\frac{i}{8}W^{-2}(\Gamma{}^{a}){}^{\beta \gamma}(\Sigma{}_{a b}){}^{\delta \rho}W{}_{\eta \delta \rho}{}^{r}\lambda{}_{\beta}{}^{j}\big(\nabla^{b}\lambda{}_{\gamma}{}^{i}\big)\\
&+\frac{i}{4}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}F{}_{a b}\varepsilon{}^{r j}F{}_{\eta \beta}\big(\nabla^{b}\lambda{}_{\gamma}{}^{i}\big) +\frac{i}{4}W^{-2}(\Gamma{}^{a}){}^{\beta \gamma}F{}_{a b}\varepsilon{}^{r j}W{}_{\eta \beta}\big(\nabla^{b}\lambda{}_{\gamma}{}^{i}\big)\\
&+\frac{i}{8}W^{-3}(\Gamma{}^{a}){}_{\eta}{}^{\beta}F{}_{a b}X{}^{r j}\big(\nabla^{b}\lambda{}_{\beta}{}^{i}\big) +\frac{i}{8}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}F{}_{a b}\varepsilon{}^{r j}(\Gamma{}^{c}){}_{\eta \beta}\big(\nabla_{c}W\big)\big(\nabla^{b}\lambda{}_{\gamma}{}^{i}\big)\\
&-\frac{i}{4}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}F{}_{a b}\lambda{}_{\beta}{}^{j}\varepsilon{}^{r i}\big(\nabla^{b}F{}_{\eta \gamma}\big) -\frac{i}{4}W^{-2}(\Gamma{}^{a}){}^{\beta \gamma}F{}_{a b}\lambda{}_{\beta}{}^{j}\varepsilon{}^{r i}\big(\nabla^{b}W{}_{\eta \gamma}\big)\\
&-\frac{i}{4}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}F{}_{a b}\lambda{}_{\beta}{}^{j}\varepsilon{}^{r i}W{}_{\eta \gamma}\big(\nabla^{b}W\big) -\frac{i}{8}W^{-3}(\Gamma{}^{a}){}^{\beta}{}_{\eta}F{}_{a b}\lambda{}_{\beta}{}^{j}\big(\nabla^{b}X{}^{r i}\big)\\
&-\frac{i}{8}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}F{}_{a b}\lambda{}_{\beta}{}^{j}\varepsilon{}^{r i}(\Gamma{}^{c}){}_{\eta \gamma}\big(\nabla^{b}\nabla_{c}W\big) -\frac{i}{4}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}F{}_{a b}\lambda{}_{\beta}{}^{j}\mathcal T{}^{b}{}_{\eta}{}^{\delta}\varepsilon{}^{r i}F{}_{\delta \gamma}\\
&-\frac{i}{4}W^{-2}(\Gamma{}^{a}){}^{\beta \gamma}F{}_{a b}\lambda{}_{\beta}{}^{j}\mathcal T{}^{b}{}_{\eta}{}^{\delta}\varepsilon{}^{r i}W{}_{\delta \gamma} -\frac{i}{8}W^{-3}(\Gamma{}^{a}){}^{\beta}{}_{\gamma}F{}_{a b}\lambda{}_{\beta}{}^{j}\mathcal T{}^{b}{}_{\eta}{}^{\gamma}X{}^{r i}\\
&-\frac{i}{8}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}F{}_{a b}\lambda{}_{\beta}{}^{j}\mathcal T{}^{b}{}_{\eta}{}^{\delta}\varepsilon{}^{r i}(\Gamma{}^{c}){}_{\delta \gamma}\big(\nabla_{c}W\big) +\frac{i}{16}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}F{}_{a b}\lambda{}_{\beta}{}^{j}\mathcal R(M){}^{b}{}_{\eta}{}^{r c d}(\Sigma{}_{c d}){}_{\gamma}{}^{\delta}\lambda{}_{\delta}{}^{i}\\
&+\frac{3i}{16}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}F{}_{a b}\lambda{}_{\beta}{}^{j}\mathcal R(\mathbb D){}^{b}{}_{\eta}{}^{r}\lambda{}_{\gamma}{}^{i} -\frac{i}{16}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}F{}_{a b}\lambda{}_{\beta}{}^{j}\mathcal R(J){}^{b}{}_{\eta}{}^{r i k}\lambda{}_{\gamma k}\\
&-\frac{i}{16}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}F{}_{a b}\lambda{}_{\beta}{}^{j}\mathcal R(J){}^{b}{}_{\eta}{}^{r k i}\lambda{}_{\gamma k} +\frac{1}{4}W^{-2}(\Gamma{}^{a}){}^{\beta}{}_{\gamma}F{}_{a b}\lambda{}_{\beta}{}^{j}\mathcal R(S){}^{b}{}_{\eta}{}^{r \gamma i}
\end{aligned}
\tag{S3-H3.5-b}
```

**Check for H3.5:** all 58 written summands have weight $`7/2`$, odd parity and the same free indices $`\eta;r,i,j`$. Dummy labels are paired. The coefficient $`1/3`$ and the two external epsilons are applied once, when collecting the spinor.

#### Input H3.6

The calculated input is

```math
\left.H^{ij}\right|_{\mathrm{H3.6}}=W^{-3}\big(-\frac i4(\Gamma^a)^{\alpha\beta}\lambda_\alpha^i\lambda_\beta^j\nabla^cF_{ac}\big).
\tag{S3-H3.6-input}
```

Expand each written SU(2) average with weight $`1/2`$ before applying the left derivative.

Apply the product rule (S3-09), in the displayed factor order:

```math
\begin{aligned}
\left.\nabla_\eta^rH^{ij}\right|_{\mathrm{H3.6}}=&-\frac{i}{4}\nabla_{\eta}^{r}\big(W^{-3}\big)(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{i}\lambda{}_{\gamma}{}^{j}\big(\nabla^{b}F{}_{a b}\big) -\frac{i}{4}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}\nabla_{\eta}^{r}\big(\lambda{}_{\beta}{}^{i}\big)\lambda{}_{\gamma}{}^{j}\big(\nabla^{b}F{}_{a b}\big)\\
&+\frac{i}{4}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{i}\nabla_{\eta}^{r}\big(\lambda{}_{\gamma}{}^{j}\big)\big(\nabla^{b}F{}_{a b}\big) -\frac{i}{4}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{i}\lambda{}_{\gamma}{}^{j}\nabla_{\eta}^{r}\big(\nabla^{b}F{}_{a b}\big)
\end{aligned}
\tag{S3-H3.6-a}
```

Insert the elementary source identities and the applicable commutators (S3-11)–(S3-14), distribute the vector product rules, and contract only index-raising metrics. The resulting contribution is

```math
\begin{aligned}
\left.\nabla_\eta^rH^{ij}\right|_{\mathrm{H3.6}}=&-\frac{3}{4}W^{-4}\lambda{}_{\eta}{}^{r}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{i}\lambda{}_{\gamma}{}^{j}\big(\nabla^{b}F{}_{a b}\big) +\frac{i}{2}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}\varepsilon{}^{r i}F{}_{\eta \beta}\lambda{}_{\gamma}{}^{j}\big(\nabla^{b}F{}_{a b}\big)\\
&+\frac{i}{2}W^{-2}(\Gamma{}^{a}){}^{\beta \gamma}\varepsilon{}^{r i}W{}_{\eta \beta}\lambda{}_{\gamma}{}^{j}\big(\nabla^{b}F{}_{a b}\big) +\frac{i}{4}W^{-3}(\Gamma{}^{a}){}_{\eta}{}^{\beta}X{}^{r i}\lambda{}_{\beta}{}^{j}\big(\nabla^{b}F{}_{a b}\big)\\
&+\frac{i}{4}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}\varepsilon{}^{r i}(\Gamma{}^{b}){}_{\eta \beta}\big(\nabla_{b}W\big)\lambda{}_{\gamma}{}^{j}\big(\nabla^{c}F{}_{a c}\big) -\frac{i}{2}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{i}\varepsilon{}^{r j}F{}_{\eta \gamma}\big(\nabla^{b}F{}_{a b}\big)\\
&-\frac{i}{2}W^{-2}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{i}\varepsilon{}^{r j}W{}_{\eta \gamma}\big(\nabla^{b}F{}_{a b}\big) -\frac{i}{4}W^{-3}(\Gamma{}^{a}){}^{\beta}{}_{\eta}\lambda{}_{\beta}{}^{i}X{}^{r j}\big(\nabla^{b}F{}_{a b}\big)\\
&-\frac{i}{4}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{i}\varepsilon{}^{r j}(\Gamma{}^{b}){}_{\eta \gamma}\big(\nabla_{b}W\big)\big(\nabla^{c}F{}_{a c}\big) -\frac{1}{8}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{i}\lambda{}_{\gamma}{}^{j}(\Sigma{}_{a b}){}^{\delta \rho}(\Gamma{}^{c}){}_{\eta \delta}\big(\nabla^{b}\nabla_{c}\lambda{}_{\rho}{}^{r}\big)\\
&-\frac{1}{8}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{i}\lambda{}_{\gamma}{}^{j}(\Sigma{}_{a b}){}_{\eta}{}^{\delta}(\Gamma{}^{c}){}_{\delta}{}^{\rho}\big(\nabla^{b}\nabla_{c}\lambda{}_{\rho}{}^{r}\big) +\frac{1}{16}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{i}\lambda{}_{\gamma}{}^{j}(\Sigma{}_{a b}){}^{\delta \rho}\big(\nabla^{b}W{}_{\eta \delta}\big)\lambda{}_{\rho}{}^{r}\\
&+\frac{1}{16}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{i}\lambda{}_{\gamma}{}^{j}(\Sigma{}_{a b}){}^{\delta \rho}W{}_{\eta \delta}\big(\nabla^{b}\lambda{}_{\rho}{}^{r}\big) -\frac{3}{16}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{i}\lambda{}_{\gamma}{}^{j}(\Sigma{}_{a b}){}_{\eta}{}^{\delta}\big(\nabla^{b}W{}_{\delta}{}^{\rho}\big)\lambda{}_{\rho}{}^{r}\\
&-\frac{3}{16}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{i}\lambda{}_{\gamma}{}^{j}(\Sigma{}_{a b}){}_{\eta}{}^{\delta}W{}_{\delta}{}^{\rho}\big(\nabla^{b}\lambda{}_{\rho}{}^{r}\big) -\frac{1}{8}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{i}\lambda{}_{\gamma}{}^{j}(\Sigma{}_{a b}){}^{\delta \rho}(\Gamma{}^{c}){}_{\eta \rho}\big(\nabla^{b}\nabla_{c}\lambda{}_{\delta}{}^{r}\big)\\
&-\frac{1}{8}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{i}\lambda{}_{\gamma}{}^{j}(\Sigma{}_{a b}){}^{\delta}{}_{\eta}(\Gamma{}^{c}){}_{\delta}{}^{\rho}\big(\nabla^{b}\nabla_{c}\lambda{}_{\rho}{}^{r}\big) +\frac{1}{16}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{i}\lambda{}_{\gamma}{}^{j}(\Sigma{}_{a b}){}^{\delta \rho}\big(\nabla^{b}W{}_{\eta \rho}\big)\lambda{}_{\delta}{}^{r}\\
&+\frac{1}{16}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{i}\lambda{}_{\gamma}{}^{j}(\Sigma{}_{a b}){}^{\delta \rho}W{}_{\eta \rho}\big(\nabla^{b}\lambda{}_{\delta}{}^{r}\big) -\frac{3}{16}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{i}\lambda{}_{\gamma}{}^{j}(\Sigma{}_{a b}){}^{\delta}{}_{\eta}\big(\nabla^{b}W{}_{\delta}{}^{\rho}\big)\lambda{}_{\rho}{}^{r}\\
&-\frac{3}{16}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{i}\lambda{}_{\gamma}{}^{j}(\Sigma{}_{a b}){}^{\delta}{}_{\eta}W{}_{\delta}{}^{\rho}\big(\nabla^{b}\lambda{}_{\rho}{}^{r}\big) -\frac{3}{8}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{i}\lambda{}_{\gamma}{}^{j}(\Sigma{}_{a b}){}^{\delta \rho}\big(\nabla^{b}W{}_{\delta \rho}\big)\lambda{}_{\eta}{}^{r}\\
&-\frac{3}{8}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{i}\lambda{}_{\gamma}{}^{j}(\Sigma{}_{a b}){}^{\delta \rho}W{}_{\delta \rho}\big(\nabla^{b}\lambda{}_{\eta}{}^{r}\big) +\frac{i}{4}W^{-2}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{i}\lambda{}_{\gamma}{}^{j}(\Sigma{}_{a b}){}^{\delta \rho}\big(\nabla^{b}W{}_{\eta \delta \rho}{}^{r}\big)\\
&+\frac{i}{4}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{i}\lambda{}_{\gamma}{}^{j}(\Sigma{}_{a b}){}^{\delta \rho}W{}_{\eta \delta \rho}{}^{r}\big(\nabla^{b}W\big) -\frac{1}{8}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{i}\lambda{}_{\gamma}{}^{j}\mathcal T{}^{b}{}_{\eta}{}^{\delta}(\Sigma{}_{a b}){}^{\rho \sigma}(\Gamma{}^{c}){}_{\delta \rho}\big(\nabla_{c}\lambda{}_{\sigma}{}^{r}\big)\\
&-\frac{1}{8}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{i}\lambda{}_{\gamma}{}^{j}\mathcal T{}^{b}{}_{\eta}{}^{\delta}(\Sigma{}_{a b}){}_{\delta}{}^{\rho}(\Gamma{}^{c}){}_{\rho}{}^{\sigma}\big(\nabla_{c}\lambda{}_{\sigma}{}^{r}\big) +\frac{1}{16}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{i}\lambda{}_{\gamma}{}^{j}\mathcal T{}^{b}{}_{\eta}{}^{\delta}(\Sigma{}_{a b}){}^{\rho \sigma}W{}_{\delta \rho}\lambda{}_{\sigma}{}^{r}\\
&-\frac{3}{16}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{i}\lambda{}_{\gamma}{}^{j}\mathcal T{}^{b}{}_{\eta}{}^{\delta}(\Sigma{}_{a b}){}_{\delta}{}^{\rho}W{}_{\rho}{}^{\sigma}\lambda{}_{\sigma}{}^{r} -\frac{1}{8}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{i}\lambda{}_{\gamma}{}^{j}\mathcal T{}^{b}{}_{\eta}{}^{\delta}(\Sigma{}_{a b}){}^{\rho \sigma}(\Gamma{}^{c}){}_{\delta \sigma}\big(\nabla_{c}\lambda{}_{\rho}{}^{r}\big)\\
&-\frac{1}{8}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{i}\lambda{}_{\gamma}{}^{j}\mathcal T{}^{b}{}_{\eta}{}^{\delta}(\Sigma{}_{a b}){}^{\rho}{}_{\delta}(\Gamma{}^{c}){}_{\rho}{}^{\sigma}\big(\nabla_{c}\lambda{}_{\sigma}{}^{r}\big) +\frac{1}{16}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{i}\lambda{}_{\gamma}{}^{j}\mathcal T{}^{b}{}_{\eta}{}^{\delta}(\Sigma{}_{a b}){}^{\rho \sigma}W{}_{\delta \sigma}\lambda{}_{\rho}{}^{r}\\
&-\frac{3}{16}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{i}\lambda{}_{\gamma}{}^{j}\mathcal T{}^{b}{}_{\eta}{}^{\delta}(\Sigma{}_{a b}){}^{\rho}{}_{\delta}W{}_{\rho}{}^{\sigma}\lambda{}_{\sigma}{}^{r} -\frac{3}{8}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{i}\lambda{}_{\gamma}{}^{j}\mathcal T{}^{b}{}_{\eta}{}^{\delta}(\Sigma{}_{a b}){}^{\rho \sigma}W{}_{\rho \sigma}\lambda{}_{\delta}{}^{r}\\
&+\frac{i}{4}W^{-2}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{i}\lambda{}_{\gamma}{}^{j}\mathcal T{}^{b}{}_{\eta}{}^{\delta}(\Sigma{}_{a b}){}^{\rho \sigma}W{}_{\delta \rho \sigma}{}^{r} -\frac{i}{8}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{i}\lambda{}_{\gamma}{}^{j}\mathcal R(M){}^{b}{}_{\eta}{}^{r}{}_{a}{}^{c}F{}_{c b}\\
&+\frac{i}{8}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{i}\lambda{}_{\gamma}{}^{j}\mathcal R(M){}^{b}{}_{\eta}{}^{r c}{}_{a}F{}_{c b} -\frac{i}{8}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{i}\lambda{}_{\gamma}{}^{j}\mathcal R(M){}^{b}{}_{\eta}{}^{r}{}_{b}{}^{c}F{}_{a c}\\
&+\frac{i}{8}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{i}\lambda{}_{\gamma}{}^{j}\mathcal R(M){}^{b}{}_{\eta}{}^{r c}{}_{b}F{}_{a c} -\frac{i}{2}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{i}\lambda{}_{\gamma}{}^{j}\mathcal R(\mathbb D){}^{b}{}_{\eta}{}^{r}F{}_{a b}\\
&-\frac{i}{2}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{i}\lambda{}_{\gamma}{}^{j}\mathcal R(S){}^{b}{}_{\eta}{}^{r \delta k}(\Sigma{}_{a b}){}_{\delta}{}^{\rho}\lambda{}_{\rho k} -\frac{i}{2}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{i}\lambda{}_{\gamma}{}^{j}\mathcal R(S){}^{b}{}_{\eta}{}^{r \delta k}(\Sigma{}_{a b}){}^{\rho}{}_{\delta}\lambda{}_{\rho k}
\end{aligned}
\tag{S3-H3.6-b}
```

**Check for H3.6:** all 42 written summands have weight $`7/2`$, odd parity and the same free indices $`\eta;r,i,j`$. Dummy labels are paired. The coefficient $`1/3`$ and the two external epsilons are applied once, when collecting the spinor.

#### Input H3.7

The calculated input is

```math
\left.H^{ij}\right|_{\mathrm{H3.7}}=W^{-3}\big(\frac i4(\Gamma^a)^{\alpha\beta}X^{ij}\lambda_\alpha^k\nabla_a\lambda_{\beta k}\big).
\tag{S3-H3.7-input}
```

Expand each written SU(2) average with weight $`1/2`$ before applying the left derivative.

Apply the product rule (S3-09), in the displayed factor order:

```math
\begin{aligned}
\left.\nabla_\eta^rH^{ij}\right|_{\mathrm{H3.7}}=&\frac{i}{4}\nabla_{\eta}^{r}\big(W^{-3}\big)(\Gamma{}^{a}){}^{\beta \gamma}X{}^{i j}\lambda{}_{\beta}{}^{k}\big(\nabla_{a}\lambda{}_{\gamma k}\big) +\frac{i}{4}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}\nabla_{\eta}^{r}\big(X{}^{i j}\big)\lambda{}_{\beta}{}^{k}\big(\nabla_{a}\lambda{}_{\gamma k}\big)\\
&+\frac{i}{4}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}X{}^{i j}\nabla_{\eta}^{r}\big(\lambda{}_{\beta}{}^{k}\big)\big(\nabla_{a}\lambda{}_{\gamma k}\big) -\frac{i}{4}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}X{}^{i j}\lambda{}_{\beta}{}^{k}\nabla_{\eta}^{r}\big(\nabla_{a}\lambda{}_{\gamma k}\big)
\end{aligned}
\tag{S3-H3.7-a}
```

Insert the elementary source identities and the applicable commutators (S3-11)–(S3-14), distribute the vector product rules, and contract only index-raising metrics. The resulting contribution is

```math
\begin{aligned}
\left.\nabla_\eta^rH^{ij}\right|_{\mathrm{H3.7}}=&\frac{3}{4}W^{-4}\lambda{}_{\eta}{}^{r}(\Gamma{}^{a}){}^{\beta \gamma}X{}^{i j}\lambda{}_{\beta}{}^{k}\big(\nabla_{a}\lambda{}_{\gamma k}\big) -\frac{1}{4}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}\varepsilon{}^{r i}(\Gamma{}^{b}){}_{\eta}{}^{\delta}\big(\nabla_{b}\lambda{}_{\delta}{}^{j}\big)\lambda{}_{\beta}{}^{k}\big(\nabla_{a}\lambda{}_{\gamma k}\big)\\
&+\frac{1}{8}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}\varepsilon{}^{r i}W{}_{\eta \delta}\lambda{}^{\delta j}\lambda{}_{\beta}{}^{k}\big(\nabla_{a}\lambda{}_{\gamma k}\big) -\frac{3i}{16}W^{-2}(\Gamma{}^{a}){}^{\beta \gamma}\varepsilon{}^{r i}X{}_{\eta}{}^{j}\lambda{}_{\beta}{}^{k}\big(\nabla_{a}\lambda{}_{\gamma k}\big)\\
&-\frac{1}{4}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}\varepsilon{}^{r j}(\Gamma{}^{b}){}_{\eta}{}^{\delta}\big(\nabla_{b}\lambda{}_{\delta}{}^{i}\big)\lambda{}_{\beta}{}^{k}\big(\nabla_{a}\lambda{}_{\gamma k}\big) +\frac{1}{8}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}\varepsilon{}^{r j}W{}_{\eta \delta}\lambda{}^{\delta i}\lambda{}_{\beta}{}^{k}\big(\nabla_{a}\lambda{}_{\gamma k}\big)\\
&-\frac{3i}{16}W^{-2}(\Gamma{}^{a}){}^{\beta \gamma}\varepsilon{}^{r j}X{}_{\eta}{}^{i}\lambda{}_{\beta}{}^{k}\big(\nabla_{a}\lambda{}_{\gamma k}\big) -\frac{i}{2}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}X{}^{i j}F{}_{\eta \beta}\big(\nabla_{a}\lambda{}_{\gamma}{}^{r}\big)\\
&-\frac{i}{2}W^{-2}(\Gamma{}^{a}){}^{\beta \gamma}X{}^{i j}W{}_{\eta \beta}\big(\nabla_{a}\lambda{}_{\gamma}{}^{r}\big) -\frac{i}{4}W^{-3}(\Gamma{}^{a}){}_{\eta}{}^{\beta}X{}^{i j}X{}^{r k}\big(\nabla_{a}\lambda{}_{\beta k}\big)\\
&-\frac{i}{4}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}X{}^{i j}(\Gamma{}^{b}){}_{\eta \beta}\big(\nabla_{b}W\big)\big(\nabla_{a}\lambda{}_{\gamma}{}^{r}\big) -\frac{i}{2}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}X{}^{i j}\lambda{}_{\beta}{}^{r}\big(\nabla_{a}F{}_{\eta \gamma}\big)\\
&-\frac{i}{2}W^{-2}(\Gamma{}^{a}){}^{\beta \gamma}X{}^{i j}\lambda{}_{\beta}{}^{r}\big(\nabla_{a}W{}_{\eta \gamma}\big) -\frac{i}{2}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}X{}^{i j}\lambda{}_{\beta}{}^{r}W{}_{\eta \gamma}\big(\nabla_{a}W\big)\\
&+\frac{i}{4}W^{-3}(\Gamma{}^{a}){}^{\beta}{}_{\eta}X{}^{i j}\lambda{}_{\beta}{}^{k}\big(\nabla_{a}X{}^{r}{}_{k}\big) -\frac{i}{4}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}X{}^{i j}\lambda{}_{\beta}{}^{r}(\Gamma{}^{b}){}_{\eta \gamma}\big(\nabla_{a}\nabla_{b}W\big)\\
&-\frac{i}{2}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}X{}^{i j}\lambda{}_{\beta}{}^{r}\mathcal T{}_{a \eta}{}^{\delta}F{}_{\delta \gamma} -\frac{i}{2}W^{-2}(\Gamma{}^{a}){}^{\beta \gamma}X{}^{i j}\lambda{}_{\beta}{}^{r}\mathcal T{}_{a \eta}{}^{\delta}W{}_{\delta \gamma}\\
&+\frac{i}{4}W^{-3}(\Gamma{}^{a}){}^{\beta}{}_{\gamma}X{}^{i j}\lambda{}_{\beta}{}^{k}\mathcal T{}_{a \eta}{}^{\gamma}X{}^{r}{}_{k} -\frac{i}{4}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}X{}^{i j}\lambda{}_{\beta}{}^{r}\mathcal T{}_{a \eta}{}^{\delta}(\Gamma{}^{b}){}_{\delta \gamma}\big(\nabla_{b}W\big)\\
&-\frac{i}{8}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}X{}^{i j}\lambda{}_{\beta}{}^{k}\mathcal R(M){}_{a \eta}{}^{r b c}(\Sigma{}_{b c}){}_{\gamma}{}^{\delta}\lambda{}_{\delta k} -\frac{3i}{8}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}X{}^{i j}\lambda{}_{\beta}{}^{k}\mathcal R(\mathbb D){}_{a \eta}{}^{r}\lambda{}_{\gamma k}\\
&-\frac{i}{8}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}X{}^{i j}\lambda{}_{\beta k}\mathcal R(J){}_{a \eta}{}^{r k l}\lambda{}_{\gamma l} -\frac{i}{8}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}X{}^{i j}\lambda{}_{\beta k}\mathcal R(J){}_{a \eta}{}^{r l k}\lambda{}_{\gamma l}\\
&+\frac{1}{2}W^{-2}(\Gamma{}^{a}){}^{\beta}{}_{\gamma}X{}^{i j}\lambda{}_{\beta k}\mathcal R(S){}_{a \eta}{}^{r \gamma k}
\end{aligned}
\tag{S3-H3.7-b}
```

**Check for H3.7:** all 25 written summands have weight $`7/2`$, odd parity and the same free indices $`\eta;r,i,j`$. Dummy labels are paired. The coefficient $`1/3`$ and the two external epsilons are applied once, when collecting the spinor.

#### Input H3.8

The calculated input is

```math
\left.H^{ij}\right|_{\mathrm{H3.8}}=W^{-3}\big(\frac i4(\Gamma^a)^{\alpha\beta}X^{k(i}\lambda_\alpha^{j)}\nabla_a\lambda_{\beta k}\big).
\tag{S3-H3.8-input}
```

Expand each written SU(2) average with weight $`1/2`$ before applying the left derivative.

Apply the product rule (S3-09), in the displayed factor order:

```math
\begin{aligned}
\left.\nabla_\eta^rH^{ij}\right|_{\mathrm{H3.8}}=&\frac{i}{8}\nabla_{\eta}^{r}\big(W^{-3}\big)(\Gamma{}^{a}){}^{\beta \gamma}X{}^{k i}\lambda{}_{\beta}{}^{j}\big(\nabla_{a}\lambda{}_{\gamma k}\big) +\frac{i}{8}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}\nabla_{\eta}^{r}\big(X{}^{k i}\big)\lambda{}_{\beta}{}^{j}\big(\nabla_{a}\lambda{}_{\gamma k}\big)\\
&+\frac{i}{8}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}X{}^{k i}\nabla_{\eta}^{r}\big(\lambda{}_{\beta}{}^{j}\big)\big(\nabla_{a}\lambda{}_{\gamma k}\big) -\frac{i}{8}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}X{}^{k i}\lambda{}_{\beta}{}^{j}\nabla_{\eta}^{r}\big(\nabla_{a}\lambda{}_{\gamma k}\big)\\
&+\frac{i}{8}\nabla_{\eta}^{r}\big(W^{-3}\big)(\Gamma{}^{a}){}^{\beta \gamma}X{}^{k j}\lambda{}_{\beta}{}^{i}\big(\nabla_{a}\lambda{}_{\gamma k}\big) +\frac{i}{8}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}\nabla_{\eta}^{r}\big(X{}^{k j}\big)\lambda{}_{\beta}{}^{i}\big(\nabla_{a}\lambda{}_{\gamma k}\big)\\
&+\frac{i}{8}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}X{}^{k j}\nabla_{\eta}^{r}\big(\lambda{}_{\beta}{}^{i}\big)\big(\nabla_{a}\lambda{}_{\gamma k}\big) -\frac{i}{8}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}X{}^{k j}\lambda{}_{\beta}{}^{i}\nabla_{\eta}^{r}\big(\nabla_{a}\lambda{}_{\gamma k}\big)
\end{aligned}
\tag{S3-H3.8-a}
```

Insert the elementary source identities and the applicable commutators (S3-11)–(S3-14), distribute the vector product rules, and contract only index-raising metrics. The resulting contribution is

```math
\begin{aligned}
\left.\nabla_\eta^rH^{ij}\right|_{\mathrm{H3.8}}=&\frac{3}{8}W^{-4}\lambda{}_{\eta}{}^{r}(\Gamma{}^{a}){}^{\beta \gamma}X{}^{k i}\lambda{}_{\beta}{}^{j}\big(\nabla_{a}\lambda{}_{\gamma k}\big) -\frac{1}{8}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}(\Gamma{}^{b}){}_{\eta}{}^{\delta}\big(\nabla_{b}\lambda{}_{\delta}{}^{i}\big)\lambda{}_{\beta}{}^{j}\big(\nabla_{a}\lambda{}_{\gamma}{}^{r}\big)\\
&+\frac{1}{16}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}W{}_{\eta \delta}\lambda{}^{\delta i}\lambda{}_{\beta}{}^{j}\big(\nabla_{a}\lambda{}_{\gamma}{}^{r}\big) -\frac{3i}{32}W^{-2}(\Gamma{}^{a}){}^{\beta \gamma}X{}_{\eta}{}^{i}\lambda{}_{\beta}{}^{j}\big(\nabla_{a}\lambda{}_{\gamma}{}^{r}\big)\\
&-\frac{1}{8}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}\varepsilon{}^{r i}(\Gamma{}^{b}){}_{\eta}{}^{\delta}\big(\nabla_{b}\lambda{}_{\delta}{}^{k}\big)\lambda{}_{\beta}{}^{j}\big(\nabla_{a}\lambda{}_{\gamma k}\big) +\frac{1}{16}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}\varepsilon{}^{r i}W{}_{\eta \delta}\lambda{}^{\delta k}\lambda{}_{\beta}{}^{j}\big(\nabla_{a}\lambda{}_{\gamma k}\big)\\
&-\frac{3i}{32}W^{-2}(\Gamma{}^{a}){}^{\beta \gamma}\varepsilon{}^{r i}X{}_{\eta}{}^{k}\lambda{}_{\beta}{}^{j}\big(\nabla_{a}\lambda{}_{\gamma k}\big) -\frac{i}{4}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}X{}^{k i}\varepsilon{}^{r j}F{}_{\eta \beta}\big(\nabla_{a}\lambda{}_{\gamma k}\big)\\
&-\frac{i}{4}W^{-2}(\Gamma{}^{a}){}^{\beta \gamma}X{}^{k i}\varepsilon{}^{r j}W{}_{\eta \beta}\big(\nabla_{a}\lambda{}_{\gamma k}\big) -\frac{i}{8}W^{-3}(\Gamma{}^{a}){}_{\eta}{}^{\beta}X{}^{k i}X{}^{r j}\big(\nabla_{a}\lambda{}_{\beta k}\big)\\
&-\frac{i}{8}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}X{}^{k i}\varepsilon{}^{r j}(\Gamma{}^{b}){}_{\eta \beta}\big(\nabla_{b}W\big)\big(\nabla_{a}\lambda{}_{\gamma k}\big) -\frac{i}{4}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}X{}^{r i}\lambda{}_{\beta}{}^{j}\big(\nabla_{a}F{}_{\eta \gamma}\big)\\
&-\frac{i}{4}W^{-2}(\Gamma{}^{a}){}^{\beta \gamma}X{}^{r i}\lambda{}_{\beta}{}^{j}\big(\nabla_{a}W{}_{\eta \gamma}\big) -\frac{i}{4}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}X{}^{r i}\lambda{}_{\beta}{}^{j}W{}_{\eta \gamma}\big(\nabla_{a}W\big)\\
&+\frac{i}{8}W^{-3}(\Gamma{}^{a}){}^{\beta}{}_{\eta}X{}^{k i}\lambda{}_{\beta}{}^{j}\big(\nabla_{a}X{}^{r}{}_{k}\big) -\frac{i}{8}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}X{}^{r i}\lambda{}_{\beta}{}^{j}(\Gamma{}^{b}){}_{\eta \gamma}\big(\nabla_{a}\nabla_{b}W\big)\\
&-\frac{i}{4}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}X{}^{r i}\lambda{}_{\beta}{}^{j}\mathcal T{}_{a \eta}{}^{\delta}F{}_{\delta \gamma} -\frac{i}{4}W^{-2}(\Gamma{}^{a}){}^{\beta \gamma}X{}^{r i}\lambda{}_{\beta}{}^{j}\mathcal T{}_{a \eta}{}^{\delta}W{}_{\delta \gamma}\\
&+\frac{i}{8}W^{-3}(\Gamma{}^{a}){}^{\beta}{}_{\gamma}X{}^{k i}\lambda{}_{\beta}{}^{j}\mathcal T{}_{a \eta}{}^{\gamma}X{}^{r}{}_{k} -\frac{i}{8}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}X{}^{r i}\lambda{}_{\beta}{}^{j}\mathcal T{}_{a \eta}{}^{\delta}(\Gamma{}^{b}){}_{\delta \gamma}\big(\nabla_{b}W\big)\\
&-\frac{i}{16}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}X{}^{k i}\lambda{}_{\beta}{}^{j}\mathcal R(M){}_{a \eta}{}^{r b c}(\Sigma{}_{b c}){}_{\gamma}{}^{\delta}\lambda{}_{\delta k} -\frac{3i}{16}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}X{}^{k i}\lambda{}_{\beta}{}^{j}\mathcal R(\mathbb D){}_{a \eta}{}^{r}\lambda{}_{\gamma k}\\
&-\frac{i}{16}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}X{}_{k}{}^{i}\lambda{}_{\beta}{}^{j}\mathcal R(J){}_{a \eta}{}^{r k l}\lambda{}_{\gamma l} -\frac{i}{16}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}X{}_{k}{}^{i}\lambda{}_{\beta}{}^{j}\mathcal R(J){}_{a \eta}{}^{r l k}\lambda{}_{\gamma l}\\
&+\frac{1}{4}W^{-2}(\Gamma{}^{a}){}^{\beta}{}_{\gamma}X{}_{k}{}^{i}\lambda{}_{\beta}{}^{j}\mathcal R(S){}_{a \eta}{}^{r \gamma k} +\frac{3}{8}W^{-4}\lambda{}_{\eta}{}^{r}(\Gamma{}^{a}){}^{\beta \gamma}X{}^{k j}\lambda{}_{\beta}{}^{i}\big(\nabla_{a}\lambda{}_{\gamma k}\big)\\
&-\frac{1}{8}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}(\Gamma{}^{b}){}_{\eta}{}^{\delta}\big(\nabla_{b}\lambda{}_{\delta}{}^{j}\big)\lambda{}_{\beta}{}^{i}\big(\nabla_{a}\lambda{}_{\gamma}{}^{r}\big) +\frac{1}{16}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}W{}_{\eta \delta}\lambda{}^{\delta j}\lambda{}_{\beta}{}^{i}\big(\nabla_{a}\lambda{}_{\gamma}{}^{r}\big)\\
&-\frac{3i}{32}W^{-2}(\Gamma{}^{a}){}^{\beta \gamma}X{}_{\eta}{}^{j}\lambda{}_{\beta}{}^{i}\big(\nabla_{a}\lambda{}_{\gamma}{}^{r}\big) -\frac{1}{8}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}\varepsilon{}^{r j}(\Gamma{}^{b}){}_{\eta}{}^{\delta}\big(\nabla_{b}\lambda{}_{\delta}{}^{k}\big)\lambda{}_{\beta}{}^{i}\big(\nabla_{a}\lambda{}_{\gamma k}\big)\\
&+\frac{1}{16}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}\varepsilon{}^{r j}W{}_{\eta \delta}\lambda{}^{\delta k}\lambda{}_{\beta}{}^{i}\big(\nabla_{a}\lambda{}_{\gamma k}\big) -\frac{3i}{32}W^{-2}(\Gamma{}^{a}){}^{\beta \gamma}\varepsilon{}^{r j}X{}_{\eta}{}^{k}\lambda{}_{\beta}{}^{i}\big(\nabla_{a}\lambda{}_{\gamma k}\big)\\
&-\frac{i}{4}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}X{}^{k j}\varepsilon{}^{r i}F{}_{\eta \beta}\big(\nabla_{a}\lambda{}_{\gamma k}\big) -\frac{i}{4}W^{-2}(\Gamma{}^{a}){}^{\beta \gamma}X{}^{k j}\varepsilon{}^{r i}W{}_{\eta \beta}\big(\nabla_{a}\lambda{}_{\gamma k}\big)\\
&-\frac{i}{8}W^{-3}(\Gamma{}^{a}){}_{\eta}{}^{\beta}X{}^{k j}X{}^{r i}\big(\nabla_{a}\lambda{}_{\beta k}\big) -\frac{i}{8}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}X{}^{k j}\varepsilon{}^{r i}(\Gamma{}^{b}){}_{\eta \beta}\big(\nabla_{b}W\big)\big(\nabla_{a}\lambda{}_{\gamma k}\big)\\
&-\frac{i}{4}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}X{}^{r j}\lambda{}_{\beta}{}^{i}\big(\nabla_{a}F{}_{\eta \gamma}\big) -\frac{i}{4}W^{-2}(\Gamma{}^{a}){}^{\beta \gamma}X{}^{r j}\lambda{}_{\beta}{}^{i}\big(\nabla_{a}W{}_{\eta \gamma}\big)\\
&-\frac{i}{4}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}X{}^{r j}\lambda{}_{\beta}{}^{i}W{}_{\eta \gamma}\big(\nabla_{a}W\big) +\frac{i}{8}W^{-3}(\Gamma{}^{a}){}^{\beta}{}_{\eta}X{}^{k j}\lambda{}_{\beta}{}^{i}\big(\nabla_{a}X{}^{r}{}_{k}\big)\\
&-\frac{i}{8}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}X{}^{r j}\lambda{}_{\beta}{}^{i}(\Gamma{}^{b}){}_{\eta \gamma}\big(\nabla_{a}\nabla_{b}W\big) -\frac{i}{4}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}X{}^{r j}\lambda{}_{\beta}{}^{i}\mathcal T{}_{a \eta}{}^{\delta}F{}_{\delta \gamma}\\
&-\frac{i}{4}W^{-2}(\Gamma{}^{a}){}^{\beta \gamma}X{}^{r j}\lambda{}_{\beta}{}^{i}\mathcal T{}_{a \eta}{}^{\delta}W{}_{\delta \gamma} +\frac{i}{8}W^{-3}(\Gamma{}^{a}){}^{\beta}{}_{\gamma}X{}^{k j}\lambda{}_{\beta}{}^{i}\mathcal T{}_{a \eta}{}^{\gamma}X{}^{r}{}_{k}\\
&-\frac{i}{8}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}X{}^{r j}\lambda{}_{\beta}{}^{i}\mathcal T{}_{a \eta}{}^{\delta}(\Gamma{}^{b}){}_{\delta \gamma}\big(\nabla_{b}W\big) -\frac{i}{16}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}X{}^{k j}\lambda{}_{\beta}{}^{i}\mathcal R(M){}_{a \eta}{}^{r b c}(\Sigma{}_{b c}){}_{\gamma}{}^{\delta}\lambda{}_{\delta k}\\
&-\frac{3i}{16}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}X{}^{k j}\lambda{}_{\beta}{}^{i}\mathcal R(\mathbb D){}_{a \eta}{}^{r}\lambda{}_{\gamma k} -\frac{i}{16}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}X{}_{k}{}^{j}\lambda{}_{\beta}{}^{i}\mathcal R(J){}_{a \eta}{}^{r k l}\lambda{}_{\gamma l}\\
&-\frac{i}{16}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}X{}_{k}{}^{j}\lambda{}_{\beta}{}^{i}\mathcal R(J){}_{a \eta}{}^{r l k}\lambda{}_{\gamma l} +\frac{1}{4}W^{-2}(\Gamma{}^{a}){}^{\beta}{}_{\gamma}X{}_{k}{}^{j}\lambda{}_{\beta}{}^{i}\mathcal R(S){}_{a \eta}{}^{r \gamma k}
\end{aligned}
\tag{S3-H3.8-b}
```

**Check for H3.8:** all 50 written summands have weight $`7/2`$, odd parity and the same free indices $`\eta;r,i,j`$. Dummy labels are paired. The coefficient $`1/3`$ and the two external epsilons are applied once, when collecting the spinor.

#### Input H3.9

The calculated input is

```math
\left.H^{ij}\right|_{\mathrm{H3.9}}=W^{-3}\big(\frac i4(\Gamma^a)^{\alpha\beta}\lambda_\alpha^{(i}(\nabla_aX^{j)l})\lambda_{\beta l}\big).
\tag{S3-H3.9-input}
```

Expand each written SU(2) average with weight $`1/2`$ before applying the left derivative.

Apply the product rule (S3-09), in the displayed factor order:

```math
\begin{aligned}
\left.\nabla_\eta^rH^{ij}\right|_{\mathrm{H3.9}}=&\frac{i}{8}\nabla_{\eta}^{r}\big(W^{-3}\big)(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{i}\big(\nabla_{a}X{}^{j k}\big)\lambda{}_{\gamma k} +\frac{i}{8}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}\nabla_{\eta}^{r}\big(\lambda{}_{\beta}{}^{i}\big)\big(\nabla_{a}X{}^{j k}\big)\lambda{}_{\gamma k}\\
&-\frac{i}{8}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{i}\nabla_{\eta}^{r}\big(\nabla_{a}X{}^{j k}\big)\lambda{}_{\gamma k} -\frac{i}{8}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{i}\big(\nabla_{a}X{}^{j k}\big)\nabla_{\eta}^{r}\big(\lambda{}_{\gamma k}\big)\\
&+\frac{i}{8}\nabla_{\eta}^{r}\big(W^{-3}\big)(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{j}\big(\nabla_{a}X{}^{i k}\big)\lambda{}_{\gamma k} +\frac{i}{8}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}\nabla_{\eta}^{r}\big(\lambda{}_{\beta}{}^{j}\big)\big(\nabla_{a}X{}^{i k}\big)\lambda{}_{\gamma k}\\
&-\frac{i}{8}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{j}\nabla_{\eta}^{r}\big(\nabla_{a}X{}^{i k}\big)\lambda{}_{\gamma k} -\frac{i}{8}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{j}\big(\nabla_{a}X{}^{i k}\big)\nabla_{\eta}^{r}\big(\lambda{}_{\gamma k}\big)
\end{aligned}
\tag{S3-H3.9-a}
```

Insert the elementary source identities and the applicable commutators (S3-11)–(S3-14), distribute the vector product rules, and contract only index-raising metrics. The resulting contribution is

```math
\begin{aligned}
\left.\nabla_\eta^rH^{ij}\right|_{\mathrm{H3.9}}=&\frac{3}{8}W^{-4}\lambda{}_{\eta}{}^{r}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{i}\big(\nabla_{a}X{}^{j k}\big)\lambda{}_{\gamma k} -\frac{i}{4}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}\varepsilon{}^{r i}F{}_{\eta \beta}\big(\nabla_{a}X{}^{j k}\big)\lambda{}_{\gamma k}\\
&-\frac{i}{4}W^{-2}(\Gamma{}^{a}){}^{\beta \gamma}\varepsilon{}^{r i}W{}_{\eta \beta}\big(\nabla_{a}X{}^{j k}\big)\lambda{}_{\gamma k} -\frac{i}{8}W^{-3}(\Gamma{}^{a}){}_{\eta}{}^{\beta}X{}^{r i}\big(\nabla_{a}X{}^{j k}\big)\lambda{}_{\beta k}\\
&-\frac{i}{8}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}\varepsilon{}^{r i}(\Gamma{}^{b}){}_{\eta \beta}\big(\nabla_{b}W\big)\big(\nabla_{a}X{}^{j k}\big)\lambda{}_{\gamma k} +\frac{1}{8}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{i}\varepsilon{}^{r j}(\Gamma{}^{b}){}_{\eta}{}^{\delta}\big(\nabla_{a}\nabla_{b}\lambda{}_{\delta}{}^{k}\big)\lambda{}_{\gamma k}\\
&-\frac{1}{16}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{i}\varepsilon{}^{r j}\big(\nabla_{a}W{}_{\eta \delta}\big)\lambda{}^{\delta k}\lambda{}_{\gamma k} -\frac{1}{16}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{i}\varepsilon{}^{r j}W{}_{\eta \delta}\big(\nabla_{a}\lambda{}^{\delta k}\big)\lambda{}_{\gamma k}\\
&+\frac{3i}{32}W^{-2}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{i}\varepsilon{}^{r j}\big(\nabla_{a}X{}_{\eta}{}^{k}\big)\lambda{}_{\gamma k} +\frac{3i}{32}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{i}\varepsilon{}^{r j}X{}_{\eta}{}^{k}\big(\nabla_{a}W\big)\lambda{}_{\gamma k}\\
&+\frac{1}{8}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{i}(\Gamma{}^{b}){}_{\eta}{}^{\delta}\big(\nabla_{a}\nabla_{b}\lambda{}_{\delta}{}^{j}\big)\lambda{}_{\gamma}{}^{r} -\frac{1}{16}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{i}\big(\nabla_{a}W{}_{\eta \delta}\big)\lambda{}^{\delta j}\lambda{}_{\gamma}{}^{r}\\
&-\frac{1}{16}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{i}W{}_{\eta \delta}\big(\nabla_{a}\lambda{}^{\delta j}\big)\lambda{}_{\gamma}{}^{r} +\frac{3i}{32}W^{-2}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{i}\big(\nabla_{a}X{}_{\eta}{}^{j}\big)\lambda{}_{\gamma}{}^{r}\\
&+\frac{3i}{32}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{i}X{}_{\eta}{}^{j}\big(\nabla_{a}W\big)\lambda{}_{\gamma}{}^{r} +\frac{1}{8}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{i}\mathcal T{}_{a \eta}{}^{\delta}\varepsilon{}^{r j}(\Gamma{}^{b}){}_{\delta}{}^{\rho}\big(\nabla_{b}\lambda{}_{\rho}{}^{k}\big)\lambda{}_{\gamma k}\\
&-\frac{1}{16}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{i}\mathcal T{}_{a \eta}{}^{\delta}\varepsilon{}^{r j}W{}_{\delta \rho}\lambda{}^{\rho k}\lambda{}_{\gamma k} +\frac{3i}{32}W^{-2}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{i}\mathcal T{}_{a \eta}{}^{\delta}\varepsilon{}^{r j}X{}_{\delta}{}^{k}\lambda{}_{\gamma k}\\
&+\frac{1}{8}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{i}\mathcal T{}_{a \eta}{}^{\delta}(\Gamma{}^{b}){}_{\delta}{}^{\rho}\big(\nabla_{b}\lambda{}_{\rho}{}^{j}\big)\lambda{}_{\gamma}{}^{r} -\frac{1}{16}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{i}\mathcal T{}_{a \eta}{}^{\delta}W{}_{\delta \rho}\lambda{}^{\rho j}\lambda{}_{\gamma}{}^{r}\\
&+\frac{3i}{32}W^{-2}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{i}\mathcal T{}_{a \eta}{}^{\delta}X{}_{\delta}{}^{j}\lambda{}_{\gamma}{}^{r} -\frac{i}{4}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{i}\mathcal R(\mathbb D){}_{a \eta}{}^{r}X{}^{j k}\lambda{}_{\gamma k}\\
&+\frac{i}{16}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{i}\mathcal R(J){}_{a \eta}{}^{r j k}X{}_{k}{}^{l}\lambda{}_{\gamma l} +\frac{i}{16}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{i}\mathcal R(J){}_{a \eta}{}^{r k j}X{}_{k}{}^{l}\lambda{}_{\gamma l}\\
&+\frac{i}{16}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{i}\mathcal R(J){}_{a \eta}{}^{r k l}X{}^{j}{}_{l}\lambda{}_{\gamma k} +\frac{i}{16}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{i}\mathcal R(J){}_{a \eta}{}^{r k l}X{}^{j}{}_{k}\lambda{}_{\gamma l}\\
&+\frac{i}{8}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{i}\mathcal R(S){}_{a \eta}{}^{r \delta j}\lambda{}_{\delta}{}^{k}\lambda{}_{\gamma k} +\frac{i}{8}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{i}\mathcal R(S){}_{a \eta}{}^{r \delta k}\lambda{}_{\delta}{}^{j}\lambda{}_{\gamma k}\\
&-\frac{i}{4}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{i}\big(\nabla_{a}X{}^{j r}\big)F{}_{\eta \gamma} -\frac{i}{4}W^{-2}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{i}\big(\nabla_{a}X{}^{j r}\big)W{}_{\eta \gamma}\\
&+\frac{i}{8}W^{-3}(\Gamma{}^{a}){}^{\beta}{}_{\eta}\lambda{}_{\beta}{}^{i}\big(\nabla_{a}X{}^{j k}\big)X{}^{r}{}_{k} -\frac{i}{8}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{i}\big(\nabla_{a}X{}^{j r}\big)(\Gamma{}^{b}){}_{\eta \gamma}\big(\nabla_{b}W\big)\\
&+\frac{3}{8}W^{-4}\lambda{}_{\eta}{}^{r}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{j}\big(\nabla_{a}X{}^{i k}\big)\lambda{}_{\gamma k} -\frac{i}{4}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}\varepsilon{}^{r j}F{}_{\eta \beta}\big(\nabla_{a}X{}^{i k}\big)\lambda{}_{\gamma k}\\
&-\frac{i}{4}W^{-2}(\Gamma{}^{a}){}^{\beta \gamma}\varepsilon{}^{r j}W{}_{\eta \beta}\big(\nabla_{a}X{}^{i k}\big)\lambda{}_{\gamma k} -\frac{i}{8}W^{-3}(\Gamma{}^{a}){}_{\eta}{}^{\beta}X{}^{r j}\big(\nabla_{a}X{}^{i k}\big)\lambda{}_{\beta k}\\
&-\frac{i}{8}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}\varepsilon{}^{r j}(\Gamma{}^{b}){}_{\eta \beta}\big(\nabla_{b}W\big)\big(\nabla_{a}X{}^{i k}\big)\lambda{}_{\gamma k} +\frac{1}{8}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{j}\varepsilon{}^{r i}(\Gamma{}^{b}){}_{\eta}{}^{\delta}\big(\nabla_{a}\nabla_{b}\lambda{}_{\delta}{}^{k}\big)\lambda{}_{\gamma k}\\
&-\frac{1}{16}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{j}\varepsilon{}^{r i}\big(\nabla_{a}W{}_{\eta \delta}\big)\lambda{}^{\delta k}\lambda{}_{\gamma k} -\frac{1}{16}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{j}\varepsilon{}^{r i}W{}_{\eta \delta}\big(\nabla_{a}\lambda{}^{\delta k}\big)\lambda{}_{\gamma k}\\
&+\frac{3i}{32}W^{-2}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{j}\varepsilon{}^{r i}\big(\nabla_{a}X{}_{\eta}{}^{k}\big)\lambda{}_{\gamma k} +\frac{3i}{32}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{j}\varepsilon{}^{r i}X{}_{\eta}{}^{k}\big(\nabla_{a}W\big)\lambda{}_{\gamma k}\\
&+\frac{1}{8}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{j}(\Gamma{}^{b}){}_{\eta}{}^{\delta}\big(\nabla_{a}\nabla_{b}\lambda{}_{\delta}{}^{i}\big)\lambda{}_{\gamma}{}^{r} -\frac{1}{16}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{j}\big(\nabla_{a}W{}_{\eta \delta}\big)\lambda{}^{\delta i}\lambda{}_{\gamma}{}^{r}\\
&-\frac{1}{16}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{j}W{}_{\eta \delta}\big(\nabla_{a}\lambda{}^{\delta i}\big)\lambda{}_{\gamma}{}^{r} +\frac{3i}{32}W^{-2}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{j}\big(\nabla_{a}X{}_{\eta}{}^{i}\big)\lambda{}_{\gamma}{}^{r}\\
&+\frac{3i}{32}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{j}X{}_{\eta}{}^{i}\big(\nabla_{a}W\big)\lambda{}_{\gamma}{}^{r} +\frac{1}{8}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{j}\mathcal T{}_{a \eta}{}^{\delta}\varepsilon{}^{r i}(\Gamma{}^{b}){}_{\delta}{}^{\rho}\big(\nabla_{b}\lambda{}_{\rho}{}^{k}\big)\lambda{}_{\gamma k}\\
&-\frac{1}{16}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{j}\mathcal T{}_{a \eta}{}^{\delta}\varepsilon{}^{r i}W{}_{\delta \rho}\lambda{}^{\rho k}\lambda{}_{\gamma k} +\frac{3i}{32}W^{-2}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{j}\mathcal T{}_{a \eta}{}^{\delta}\varepsilon{}^{r i}X{}_{\delta}{}^{k}\lambda{}_{\gamma k}\\
&+\frac{1}{8}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{j}\mathcal T{}_{a \eta}{}^{\delta}(\Gamma{}^{b}){}_{\delta}{}^{\rho}\big(\nabla_{b}\lambda{}_{\rho}{}^{i}\big)\lambda{}_{\gamma}{}^{r} -\frac{1}{16}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{j}\mathcal T{}_{a \eta}{}^{\delta}W{}_{\delta \rho}\lambda{}^{\rho i}\lambda{}_{\gamma}{}^{r}\\
&+\frac{3i}{32}W^{-2}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{j}\mathcal T{}_{a \eta}{}^{\delta}X{}_{\delta}{}^{i}\lambda{}_{\gamma}{}^{r} -\frac{i}{4}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{j}\mathcal R(\mathbb D){}_{a \eta}{}^{r}X{}^{i k}\lambda{}_{\gamma k}\\
&+\frac{i}{16}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{j}\mathcal R(J){}_{a \eta}{}^{r i k}X{}_{k}{}^{l}\lambda{}_{\gamma l} +\frac{i}{16}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{j}\mathcal R(J){}_{a \eta}{}^{r k i}X{}_{k}{}^{l}\lambda{}_{\gamma l}\\
&+\frac{i}{16}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{j}\mathcal R(J){}_{a \eta}{}^{r k l}X{}^{i}{}_{l}\lambda{}_{\gamma k} +\frac{i}{16}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{j}\mathcal R(J){}_{a \eta}{}^{r k l}X{}^{i}{}_{k}\lambda{}_{\gamma l}\\
&+\frac{i}{8}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{j}\mathcal R(S){}_{a \eta}{}^{r \delta i}\lambda{}_{\delta}{}^{k}\lambda{}_{\gamma k} +\frac{i}{8}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{j}\mathcal R(S){}_{a \eta}{}^{r \delta k}\lambda{}_{\delta}{}^{i}\lambda{}_{\gamma k}\\
&-\frac{i}{4}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{j}\big(\nabla_{a}X{}^{i r}\big)F{}_{\eta \gamma} -\frac{i}{4}W^{-2}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{j}\big(\nabla_{a}X{}^{i r}\big)W{}_{\eta \gamma}\\
&+\frac{i}{8}W^{-3}(\Gamma{}^{a}){}^{\beta}{}_{\eta}\lambda{}_{\beta}{}^{j}\big(\nabla_{a}X{}^{i k}\big)X{}^{r}{}_{k} -\frac{i}{8}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{j}\big(\nabla_{a}X{}^{i r}\big)(\Gamma{}^{b}){}_{\eta \gamma}\big(\nabla_{b}W\big)
\end{aligned}
\tag{S3-H3.9-b}
```

**Check for H3.9:** all 64 written summands have weight $`7/2`$, odd parity and the same free indices $`\eta;r,i,j`$. Dummy labels are paired. The coefficient $`1/3`$ and the two external epsilons are applied once, when collecting the spinor.

#### Input H3.10

The calculated input is

```math
\left.H^{ij}\right|_{\mathrm{H3.10}}=W^{-3}\big(\frac i4\lambda^{\alpha i}\lambda_\alpha^j\Box W\big).
\tag{S3-H3.10-input}
```

Apply the product rule (S3-09), in the displayed factor order:

```math
\begin{aligned}
\left.\nabla_\eta^rH^{ij}\right|_{\mathrm{H3.10}}=&\frac{i}{4}\nabla_{\eta}^{r}\big(W^{-3}\big)\lambda{}^{\beta i}\lambda{}_{\beta}{}^{j}\big(\nabla^{a}\nabla_{a}W\big) +\frac{i}{4}W^{-3}\nabla_{\eta}^{r}\big(\lambda{}^{\beta i}\big)\lambda{}_{\beta}{}^{j}\big(\nabla^{a}\nabla_{a}W\big)\\
&-\frac{i}{4}W^{-3}\lambda{}^{\beta i}\nabla_{\eta}^{r}\big(\lambda{}_{\beta}{}^{j}\big)\big(\nabla^{a}\nabla_{a}W\big) +\frac{i}{4}W^{-3}\lambda{}^{\beta i}\lambda{}_{\beta}{}^{j}\nabla_{\eta}^{r}\big(\nabla^{a}\nabla_{a}W\big)
\end{aligned}
\tag{S3-H3.10-a}
```

Insert the elementary source identities and the applicable commutators (S3-11)–(S3-14), distribute the vector product rules, and contract only index-raising metrics. The resulting contribution is

```math
\begin{aligned}
\left.\nabla_\eta^rH^{ij}\right|_{\mathrm{H3.10}}=&\frac{3}{4}W^{-4}\lambda{}_{\eta}{}^{r}\lambda{}^{\beta i}\lambda{}_{\beta}{}^{j}\big(\nabla^{a}\nabla_{a}W\big) -\frac{i}{2}W^{-3}\varepsilon{}^{r i}F{}_{\eta}{}^{\beta}\lambda{}_{\beta}{}^{j}\big(\nabla^{a}\nabla_{a}W\big)\\
&-\frac{i}{2}W^{-2}\varepsilon{}^{r i}W{}_{\eta}{}^{\beta}\lambda{}_{\beta}{}^{j}\big(\nabla^{a}\nabla_{a}W\big) +\frac{i}{4}W^{-3}X{}^{r i}\lambda{}_{\eta}{}^{j}\big(\nabla^{a}\nabla_{a}W\big)\\
&-\frac{i}{4}W^{-3}\varepsilon{}^{r i}(\Gamma{}^{a}){}_{\eta}{}^{\beta}\big(\nabla_{a}W\big)\lambda{}_{\beta}{}^{j}\big(\nabla^{b}\nabla_{b}W\big) +\frac{i}{2}W^{-3}\lambda{}^{\beta i}\varepsilon{}^{r j}F{}_{\eta \beta}\big(\nabla^{a}\nabla_{a}W\big)\\
&+\frac{i}{2}W^{-2}\lambda{}^{\beta i}\varepsilon{}^{r j}W{}_{\eta \beta}\big(\nabla^{a}\nabla_{a}W\big) +\frac{i}{4}W^{-3}\lambda{}_{\eta}{}^{i}X{}^{r j}\big(\nabla^{a}\nabla_{a}W\big)\\
&+\frac{i}{4}W^{-3}\lambda{}^{\beta i}\varepsilon{}^{r j}(\Gamma{}^{a}){}_{\eta \beta}\big(\nabla_{a}W\big)\big(\nabla^{b}\nabla_{b}W\big) -\frac{1}{4}W^{-3}\lambda{}^{\beta i}\lambda{}_{\beta}{}^{j}\big(\nabla^{a}\nabla_{a}\lambda{}_{\eta}{}^{r}\big)\\
&-\frac{1}{4}W^{-3}\lambda{}^{\beta i}\lambda{}_{\beta}{}^{j}\big(\nabla^{a}\mathcal T{}_{a \eta}{}^{\gamma}\big)\lambda{}_{\gamma}{}^{r} -\frac{1}{4}W^{-3}\lambda{}^{\beta i}\lambda{}_{\beta}{}^{j}\mathcal T{}_{a \eta}{}^{\gamma}\big(\nabla^{a}\lambda{}_{\gamma}{}^{r}\big)\\
&+\frac{i}{4}W^{-2}\lambda{}^{\beta i}\lambda{}_{\beta}{}^{j}\big(\nabla^{a}\mathcal R(\mathbb D){}_{a \eta}{}^{r}\big) +\frac{i}{4}W^{-3}\lambda{}^{\beta i}\lambda{}_{\beta}{}^{j}\mathcal R(\mathbb D){}_{a \eta}{}^{r}\big(\nabla^{a}W\big)\\
&-\frac{1}{4}W^{-3}\lambda{}^{\beta i}\lambda{}_{\beta}{}^{j}\mathcal T{}^{a}{}_{\eta}{}^{\gamma}\big(\nabla_{a}\lambda{}_{\gamma}{}^{r}\big) -\frac{1}{4}W^{-3}\lambda{}^{\beta i}\lambda{}_{\beta}{}^{j}\mathcal T{}^{a}{}_{\eta}{}^{\gamma}\mathcal T{}_{a \gamma}{}^{\delta}\lambda{}_{\delta}{}^{r}\\
&+\frac{i}{4}W^{-2}\lambda{}^{\beta i}\lambda{}_{\beta}{}^{j}\mathcal T{}^{a}{}_{\eta}{}^{\gamma}\mathcal R(\mathbb D){}_{a \gamma}{}^{r} +\frac{i}{8}W^{-3}\lambda{}^{\beta i}\lambda{}_{\beta}{}^{j}\mathcal R(M){}^{a}{}_{\eta}{}^{r}{}_{a}{}^{b}\big(\nabla_{b}W\big)\\
&-\frac{i}{8}W^{-3}\lambda{}^{\beta i}\lambda{}_{\beta}{}^{j}\mathcal R(M){}^{a}{}_{\eta}{}^{r b}{}_{a}\big(\nabla_{b}W\big) +\frac{i}{2}W^{-3}\lambda{}^{\beta i}\lambda{}_{\beta}{}^{j}\mathcal R(\mathbb D){}^{a}{}_{\eta}{}^{r}\big(\nabla_{a}W\big)\\
&-\frac{i}{4}W^{-3}\lambda{}^{\beta i}\lambda{}_{\beta}{}^{j}\mathcal R(S){}^{a}{}_{\eta}{}^{r \gamma k}(\Gamma{}_{a}){}_{\gamma}{}^{\delta}\lambda{}_{\delta k} +\frac{i}{2}W^{-2}\lambda{}^{\beta i}\lambda{}_{\beta}{}^{j}\mathcal R(K){}_{a \eta}{}^{r a}
\end{aligned}
\tag{S3-H3.10-b}
```

**Check for H3.10:** all 22 written summands have weight $`7/2`$, odd parity and the same free indices $`\eta;r,i,j`$. Dummy labels are paired. The coefficient $`1/3`$ and the two external epsilons are applied once, when collecting the spinor.

#### Input H3.11

The calculated input is

```math
\left.H^{ij}\right|_{\mathrm{H3.11}}=W^{-3}\big(\frac{3i}{4}(\nabla^aW)\lambda^{\alpha(i}\nabla_a\lambda_\alpha^{j)}\big).
\tag{S3-H3.11-input}
```

Expand each written SU(2) average with weight $`1/2`$ before applying the left derivative.

Apply the product rule (S3-09), in the displayed factor order:

```math
\begin{aligned}
\left.\nabla_\eta^rH^{ij}\right|_{\mathrm{H3.11}}=&\frac{3i}{8}\nabla_{\eta}^{r}\big(W^{-3}\big)\big(\nabla^{a}W\big)\lambda{}^{\beta i}\big(\nabla_{a}\lambda{}_{\beta}{}^{j}\big) +\frac{3i}{8}W^{-3}\nabla_{\eta}^{r}\big(\nabla^{a}W\big)\lambda{}^{\beta i}\big(\nabla_{a}\lambda{}_{\beta}{}^{j}\big)\\
&+\frac{3i}{8}W^{-3}\big(\nabla^{a}W\big)\nabla_{\eta}^{r}\big(\lambda{}^{\beta i}\big)\big(\nabla_{a}\lambda{}_{\beta}{}^{j}\big) -\frac{3i}{8}W^{-3}\big(\nabla^{a}W\big)\lambda{}^{\beta i}\nabla_{\eta}^{r}\big(\nabla_{a}\lambda{}_{\beta}{}^{j}\big)\\
&+\frac{3i}{8}\nabla_{\eta}^{r}\big(W^{-3}\big)\big(\nabla^{a}W\big)\lambda{}^{\beta j}\big(\nabla_{a}\lambda{}_{\beta}{}^{i}\big) +\frac{3i}{8}W^{-3}\nabla_{\eta}^{r}\big(\nabla^{a}W\big)\lambda{}^{\beta j}\big(\nabla_{a}\lambda{}_{\beta}{}^{i}\big)\\
&+\frac{3i}{8}W^{-3}\big(\nabla^{a}W\big)\nabla_{\eta}^{r}\big(\lambda{}^{\beta j}\big)\big(\nabla_{a}\lambda{}_{\beta}{}^{i}\big) -\frac{3i}{8}W^{-3}\big(\nabla^{a}W\big)\lambda{}^{\beta j}\nabla_{\eta}^{r}\big(\nabla_{a}\lambda{}_{\beta}{}^{i}\big)
\end{aligned}
\tag{S3-H3.11-a}
```

Insert the elementary source identities and the applicable commutators (S3-11)–(S3-14), distribute the vector product rules, and contract only index-raising metrics. The resulting contribution is

```math
\begin{aligned}
\left.\nabla_\eta^rH^{ij}\right|_{\mathrm{H3.11}}=&\frac{9}{8}W^{-4}\lambda{}_{\eta}{}^{r}\big(\nabla^{a}W\big)\lambda{}^{\beta i}\big(\nabla_{a}\lambda{}_{\beta}{}^{j}\big) -\frac{3}{8}W^{-3}\big(\nabla^{a}\lambda{}_{\eta}{}^{r}\big)\lambda{}^{\beta i}\big(\nabla_{a}\lambda{}_{\beta}{}^{j}\big)\\
&-\frac{3}{8}W^{-3}\mathcal T{}^{a}{}_{\eta}{}^{\beta}\lambda{}_{\beta}{}^{r}\lambda{}^{\gamma i}\big(\nabla_{a}\lambda{}_{\gamma}{}^{j}\big) +\frac{3i}{8}W^{-2}\mathcal R(\mathbb D){}^{a}{}_{\eta}{}^{r}\lambda{}^{\beta i}\big(\nabla_{a}\lambda{}_{\beta}{}^{j}\big)\\
&-\frac{3i}{4}W^{-3}\big(\nabla^{a}W\big)\varepsilon{}^{r i}F{}_{\eta}{}^{\beta}\big(\nabla_{a}\lambda{}_{\beta}{}^{j}\big) -\frac{3i}{4}W^{-2}\big(\nabla^{a}W\big)\varepsilon{}^{r i}W{}_{\eta}{}^{\beta}\big(\nabla_{a}\lambda{}_{\beta}{}^{j}\big)\\
&+\frac{3i}{8}W^{-3}\big(\nabla^{a}W\big)X{}^{r i}\big(\nabla_{a}\lambda{}_{\eta}{}^{j}\big) -\frac{3i}{8}W^{-3}\big(\nabla^{a}W\big)\varepsilon{}^{r i}(\Gamma{}^{b}){}_{\eta}{}^{\beta}\big(\nabla_{b}W\big)\big(\nabla_{a}\lambda{}_{\beta}{}^{j}\big)\\
&+\frac{3i}{4}W^{-3}\big(\nabla^{a}W\big)\lambda{}^{\beta i}\varepsilon{}^{r j}\big(\nabla_{a}F{}_{\eta \beta}\big) +\frac{3i}{4}W^{-2}\big(\nabla^{a}W\big)\lambda{}^{\beta i}\varepsilon{}^{r j}\big(\nabla_{a}W{}_{\eta \beta}\big)\\
&+\frac{3i}{4}W^{-3}\big(\nabla^{a}W\big)\lambda{}^{\beta i}\varepsilon{}^{r j}W{}_{\eta \beta}\big(\nabla_{a}W\big) +\frac{3i}{8}W^{-3}\big(\nabla^{a}W\big)\lambda{}_{\eta}{}^{i}\big(\nabla_{a}X{}^{r j}\big)\\
&+\frac{3i}{8}W^{-3}\big(\nabla^{a}W\big)\lambda{}^{\beta i}\varepsilon{}^{r j}(\Gamma{}^{b}){}_{\eta \beta}\big(\nabla_{a}\nabla_{b}W\big) +\frac{3i}{4}W^{-3}\big(\nabla^{a}W\big)\lambda{}^{\beta i}\mathcal T{}_{a \eta}{}^{\gamma}\varepsilon{}^{r j}F{}_{\gamma \beta}\\
&+\frac{3i}{4}W^{-2}\big(\nabla^{a}W\big)\lambda{}^{\beta i}\mathcal T{}_{a \eta}{}^{\gamma}\varepsilon{}^{r j}W{}_{\gamma \beta} +\frac{3i}{8}W^{-3}\big(\nabla^{a}W\big)\lambda{}_{\beta}{}^{i}\mathcal T{}_{a \eta}{}^{\beta}X{}^{r j}\\
&+\frac{3i}{8}W^{-3}\big(\nabla^{a}W\big)\lambda{}^{\beta i}\mathcal T{}_{a \eta}{}^{\gamma}\varepsilon{}^{r j}(\Gamma{}^{b}){}_{\gamma \beta}\big(\nabla_{b}W\big) -\frac{3i}{16}W^{-3}\big(\nabla^{a}W\big)\lambda{}^{\beta i}\mathcal R(M){}_{a \eta}{}^{r b c}(\Sigma{}_{b c}){}_{\beta}{}^{\gamma}\lambda{}_{\gamma}{}^{j}\\
&-\frac{9i}{16}W^{-3}\big(\nabla^{a}W\big)\lambda{}^{\beta i}\mathcal R(\mathbb D){}_{a \eta}{}^{r}\lambda{}_{\beta}{}^{j} +\frac{3i}{16}W^{-3}\big(\nabla^{a}W\big)\lambda{}^{\beta i}\mathcal R(J){}_{a \eta}{}^{r j k}\lambda{}_{\beta k}\\
&+\frac{3i}{16}W^{-3}\big(\nabla^{a}W\big)\lambda{}^{\beta i}\mathcal R(J){}_{a \eta}{}^{r k j}\lambda{}_{\beta k} -\frac{3}{4}W^{-2}\big(\nabla^{a}W\big)\lambda{}_{\beta}{}^{i}\mathcal R(S){}_{a \eta}{}^{r \beta j}\\
&+\frac{9}{8}W^{-4}\lambda{}_{\eta}{}^{r}\big(\nabla^{a}W\big)\lambda{}^{\beta j}\big(\nabla_{a}\lambda{}_{\beta}{}^{i}\big) -\frac{3}{8}W^{-3}\big(\nabla^{a}\lambda{}_{\eta}{}^{r}\big)\lambda{}^{\beta j}\big(\nabla_{a}\lambda{}_{\beta}{}^{i}\big)\\
&-\frac{3}{8}W^{-3}\mathcal T{}^{a}{}_{\eta}{}^{\beta}\lambda{}_{\beta}{}^{r}\lambda{}^{\gamma j}\big(\nabla_{a}\lambda{}_{\gamma}{}^{i}\big) +\frac{3i}{8}W^{-2}\mathcal R(\mathbb D){}^{a}{}_{\eta}{}^{r}\lambda{}^{\beta j}\big(\nabla_{a}\lambda{}_{\beta}{}^{i}\big)\\
&-\frac{3i}{4}W^{-3}\big(\nabla^{a}W\big)\varepsilon{}^{r j}F{}_{\eta}{}^{\beta}\big(\nabla_{a}\lambda{}_{\beta}{}^{i}\big) -\frac{3i}{4}W^{-2}\big(\nabla^{a}W\big)\varepsilon{}^{r j}W{}_{\eta}{}^{\beta}\big(\nabla_{a}\lambda{}_{\beta}{}^{i}\big)\\
&+\frac{3i}{8}W^{-3}\big(\nabla^{a}W\big)X{}^{r j}\big(\nabla_{a}\lambda{}_{\eta}{}^{i}\big) -\frac{3i}{8}W^{-3}\big(\nabla^{a}W\big)\varepsilon{}^{r j}(\Gamma{}^{b}){}_{\eta}{}^{\beta}\big(\nabla_{b}W\big)\big(\nabla_{a}\lambda{}_{\beta}{}^{i}\big)\\
&+\frac{3i}{4}W^{-3}\big(\nabla^{a}W\big)\lambda{}^{\beta j}\varepsilon{}^{r i}\big(\nabla_{a}F{}_{\eta \beta}\big) +\frac{3i}{4}W^{-2}\big(\nabla^{a}W\big)\lambda{}^{\beta j}\varepsilon{}^{r i}\big(\nabla_{a}W{}_{\eta \beta}\big)\\
&+\frac{3i}{4}W^{-3}\big(\nabla^{a}W\big)\lambda{}^{\beta j}\varepsilon{}^{r i}W{}_{\eta \beta}\big(\nabla_{a}W\big) +\frac{3i}{8}W^{-3}\big(\nabla^{a}W\big)\lambda{}_{\eta}{}^{j}\big(\nabla_{a}X{}^{r i}\big)\\
&+\frac{3i}{8}W^{-3}\big(\nabla^{a}W\big)\lambda{}^{\beta j}\varepsilon{}^{r i}(\Gamma{}^{b}){}_{\eta \beta}\big(\nabla_{a}\nabla_{b}W\big) +\frac{3i}{4}W^{-3}\big(\nabla^{a}W\big)\lambda{}^{\beta j}\mathcal T{}_{a \eta}{}^{\gamma}\varepsilon{}^{r i}F{}_{\gamma \beta}\\
&+\frac{3i}{4}W^{-2}\big(\nabla^{a}W\big)\lambda{}^{\beta j}\mathcal T{}_{a \eta}{}^{\gamma}\varepsilon{}^{r i}W{}_{\gamma \beta} +\frac{3i}{8}W^{-3}\big(\nabla^{a}W\big)\lambda{}_{\beta}{}^{j}\mathcal T{}_{a \eta}{}^{\beta}X{}^{r i}\\
&+\frac{3i}{8}W^{-3}\big(\nabla^{a}W\big)\lambda{}^{\beta j}\mathcal T{}_{a \eta}{}^{\gamma}\varepsilon{}^{r i}(\Gamma{}^{b}){}_{\gamma \beta}\big(\nabla_{b}W\big) -\frac{3i}{16}W^{-3}\big(\nabla^{a}W\big)\lambda{}^{\beta j}\mathcal R(M){}_{a \eta}{}^{r b c}(\Sigma{}_{b c}){}_{\beta}{}^{\gamma}\lambda{}_{\gamma}{}^{i}\\
&-\frac{9i}{16}W^{-3}\big(\nabla^{a}W\big)\lambda{}^{\beta j}\mathcal R(\mathbb D){}_{a \eta}{}^{r}\lambda{}_{\beta}{}^{i} +\frac{3i}{16}W^{-3}\big(\nabla^{a}W\big)\lambda{}^{\beta j}\mathcal R(J){}_{a \eta}{}^{r i k}\lambda{}_{\beta k}\\
&+\frac{3i}{16}W^{-3}\big(\nabla^{a}W\big)\lambda{}^{\beta j}\mathcal R(J){}_{a \eta}{}^{r k i}\lambda{}_{\beta k} -\frac{3}{4}W^{-2}\big(\nabla^{a}W\big)\lambda{}_{\beta}{}^{j}\mathcal R(S){}_{a \eta}{}^{r \beta i}
\end{aligned}
\tag{S3-H3.11-b}
```

**Check for H3.11:** all 44 written summands have weight $`7/2`$, odd parity and the same free indices $`\eta;r,i,j`$. Dummy labels are paired. The coefficient $`1/3`$ and the two external epsilons are applied once, when collecting the spinor.

#### Input H3.12

The calculated input is

```math
\left.H^{ij}\right|_{\mathrm{H3.12}}=W^{-3}\big(-\frac i2(\Sigma_{ab})^{\alpha\beta}(\nabla^aW)\lambda_\alpha^{(i}\nabla^b\lambda_\beta^{j)}\big).
\tag{S3-H3.12-input}
```

Expand each written SU(2) average with weight $`1/2`$ before applying the left derivative.

Apply the product rule (S3-09), in the displayed factor order:

```math
\begin{aligned}
\left.\nabla_\eta^rH^{ij}\right|_{\mathrm{H3.12}}=&-\frac{i}{4}\nabla_{\eta}^{r}\big(W^{-3}\big)(\Sigma{}_{a b}){}^{\beta \gamma}\big(\nabla^{a}W\big)\lambda{}_{\beta}{}^{i}\big(\nabla^{b}\lambda{}_{\gamma}{}^{j}\big) -\frac{i}{4}W^{-3}(\Sigma{}_{a b}){}^{\beta \gamma}\nabla_{\eta}^{r}\big(\nabla^{a}W\big)\lambda{}_{\beta}{}^{i}\big(\nabla^{b}\lambda{}_{\gamma}{}^{j}\big)\\
&-\frac{i}{4}W^{-3}(\Sigma{}_{a b}){}^{\beta \gamma}\big(\nabla^{a}W\big)\nabla_{\eta}^{r}\big(\lambda{}_{\beta}{}^{i}\big)\big(\nabla^{b}\lambda{}_{\gamma}{}^{j}\big) +\frac{i}{4}W^{-3}(\Sigma{}_{a b}){}^{\beta \gamma}\big(\nabla^{a}W\big)\lambda{}_{\beta}{}^{i}\nabla_{\eta}^{r}\big(\nabla^{b}\lambda{}_{\gamma}{}^{j}\big)\\
&-\frac{i}{4}\nabla_{\eta}^{r}\big(W^{-3}\big)(\Sigma{}_{a b}){}^{\beta \gamma}\big(\nabla^{a}W\big)\lambda{}_{\beta}{}^{j}\big(\nabla^{b}\lambda{}_{\gamma}{}^{i}\big) -\frac{i}{4}W^{-3}(\Sigma{}_{a b}){}^{\beta \gamma}\nabla_{\eta}^{r}\big(\nabla^{a}W\big)\lambda{}_{\beta}{}^{j}\big(\nabla^{b}\lambda{}_{\gamma}{}^{i}\big)\\
&-\frac{i}{4}W^{-3}(\Sigma{}_{a b}){}^{\beta \gamma}\big(\nabla^{a}W\big)\nabla_{\eta}^{r}\big(\lambda{}_{\beta}{}^{j}\big)\big(\nabla^{b}\lambda{}_{\gamma}{}^{i}\big) +\frac{i}{4}W^{-3}(\Sigma{}_{a b}){}^{\beta \gamma}\big(\nabla^{a}W\big)\lambda{}_{\beta}{}^{j}\nabla_{\eta}^{r}\big(\nabla^{b}\lambda{}_{\gamma}{}^{i}\big)
\end{aligned}
\tag{S3-H3.12-a}
```

Insert the elementary source identities and the applicable commutators (S3-11)–(S3-14), distribute the vector product rules, and contract only index-raising metrics. The resulting contribution is

```math
\begin{aligned}
\left.\nabla_\eta^rH^{ij}\right|_{\mathrm{H3.12}}=&-\frac{3}{4}W^{-4}\lambda{}_{\eta}{}^{r}(\Sigma{}_{a b}){}^{\beta \gamma}\big(\nabla^{a}W\big)\lambda{}_{\beta}{}^{i}\big(\nabla^{b}\lambda{}_{\gamma}{}^{j}\big) +\frac{1}{4}W^{-3}(\Sigma{}_{a b}){}^{\beta \gamma}\big(\nabla^{a}\lambda{}_{\eta}{}^{r}\big)\lambda{}_{\beta}{}^{i}\big(\nabla^{b}\lambda{}_{\gamma}{}^{j}\big)\\
&+\frac{1}{4}W^{-3}(\Sigma{}_{a b}){}^{\beta \gamma}\mathcal T{}^{a}{}_{\eta}{}^{\delta}\lambda{}_{\delta}{}^{r}\lambda{}_{\beta}{}^{i}\big(\nabla^{b}\lambda{}_{\gamma}{}^{j}\big) -\frac{i}{4}W^{-2}(\Sigma{}_{a b}){}^{\beta \gamma}\mathcal R(\mathbb D){}^{a}{}_{\eta}{}^{r}\lambda{}_{\beta}{}^{i}\big(\nabla^{b}\lambda{}_{\gamma}{}^{j}\big)\\
&+\frac{i}{2}W^{-3}(\Sigma{}_{a b}){}^{\beta \gamma}\big(\nabla^{a}W\big)\varepsilon{}^{r i}F{}_{\eta \beta}\big(\nabla^{b}\lambda{}_{\gamma}{}^{j}\big) +\frac{i}{2}W^{-2}(\Sigma{}_{a b}){}^{\beta \gamma}\big(\nabla^{a}W\big)\varepsilon{}^{r i}W{}_{\eta \beta}\big(\nabla^{b}\lambda{}_{\gamma}{}^{j}\big)\\
&+\frac{i}{4}W^{-3}(\Sigma{}_{a b}){}_{\eta}{}^{\beta}\big(\nabla^{a}W\big)X{}^{r i}\big(\nabla^{b}\lambda{}_{\beta}{}^{j}\big) +\frac{i}{4}W^{-3}(\Sigma{}_{a b}){}^{\beta \gamma}\big(\nabla^{a}W\big)\varepsilon{}^{r i}(\Gamma{}^{c}){}_{\eta \beta}\big(\nabla_{c}W\big)\big(\nabla^{b}\lambda{}_{\gamma}{}^{j}\big)\\
&-\frac{i}{2}W^{-3}(\Sigma{}_{a b}){}^{\beta \gamma}\big(\nabla^{a}W\big)\lambda{}_{\beta}{}^{i}\varepsilon{}^{r j}\big(\nabla^{b}F{}_{\eta \gamma}\big) -\frac{i}{2}W^{-2}(\Sigma{}_{a b}){}^{\beta \gamma}\big(\nabla^{a}W\big)\lambda{}_{\beta}{}^{i}\varepsilon{}^{r j}\big(\nabla^{b}W{}_{\eta \gamma}\big)\\
&-\frac{i}{2}W^{-3}(\Sigma{}_{a b}){}^{\beta \gamma}\big(\nabla^{a}W\big)\lambda{}_{\beta}{}^{i}\varepsilon{}^{r j}W{}_{\eta \gamma}\big(\nabla^{b}W\big) -\frac{i}{4}W^{-3}(\Sigma{}_{a b}){}^{\beta}{}_{\eta}\big(\nabla^{a}W\big)\lambda{}_{\beta}{}^{i}\big(\nabla^{b}X{}^{r j}\big)\\
&-\frac{i}{4}W^{-3}(\Sigma{}_{a b}){}^{\beta \gamma}\big(\nabla^{a}W\big)\lambda{}_{\beta}{}^{i}\varepsilon{}^{r j}(\Gamma{}^{c}){}_{\eta \gamma}\big(\nabla^{b}\nabla_{c}W\big) -\frac{i}{2}W^{-3}(\Sigma{}_{a b}){}^{\beta \gamma}\big(\nabla^{a}W\big)\lambda{}_{\beta}{}^{i}\mathcal T{}^{b}{}_{\eta}{}^{\delta}\varepsilon{}^{r j}F{}_{\delta \gamma}\\
&-\frac{i}{2}W^{-2}(\Sigma{}_{a b}){}^{\beta \gamma}\big(\nabla^{a}W\big)\lambda{}_{\beta}{}^{i}\mathcal T{}^{b}{}_{\eta}{}^{\delta}\varepsilon{}^{r j}W{}_{\delta \gamma} -\frac{i}{4}W^{-3}(\Sigma{}_{a b}){}^{\beta}{}_{\gamma}\big(\nabla^{a}W\big)\lambda{}_{\beta}{}^{i}\mathcal T{}^{b}{}_{\eta}{}^{\gamma}X{}^{r j}\\
&-\frac{i}{4}W^{-3}(\Sigma{}_{a b}){}^{\beta \gamma}\big(\nabla^{a}W\big)\lambda{}_{\beta}{}^{i}\mathcal T{}^{b}{}_{\eta}{}^{\delta}\varepsilon{}^{r j}(\Gamma{}^{c}){}_{\delta \gamma}\big(\nabla_{c}W\big) +\frac{i}{8}W^{-3}(\Sigma{}_{a b}){}^{\beta \gamma}\big(\nabla^{a}W\big)\lambda{}_{\beta}{}^{i}\mathcal R(M){}^{b}{}_{\eta}{}^{r c d}(\Sigma{}_{c d}){}_{\gamma}{}^{\delta}\lambda{}_{\delta}{}^{j}\\
&+\frac{3i}{8}W^{-3}(\Sigma{}_{a b}){}^{\beta \gamma}\big(\nabla^{a}W\big)\lambda{}_{\beta}{}^{i}\mathcal R(\mathbb D){}^{b}{}_{\eta}{}^{r}\lambda{}_{\gamma}{}^{j} -\frac{i}{8}W^{-3}(\Sigma{}_{a b}){}^{\beta \gamma}\big(\nabla^{a}W\big)\lambda{}_{\beta}{}^{i}\mathcal R(J){}^{b}{}_{\eta}{}^{r j k}\lambda{}_{\gamma k}\\
&-\frac{i}{8}W^{-3}(\Sigma{}_{a b}){}^{\beta \gamma}\big(\nabla^{a}W\big)\lambda{}_{\beta}{}^{i}\mathcal R(J){}^{b}{}_{\eta}{}^{r k j}\lambda{}_{\gamma k} +\frac{1}{2}W^{-2}(\Sigma{}_{a b}){}^{\beta}{}_{\gamma}\big(\nabla^{a}W\big)\lambda{}_{\beta}{}^{i}\mathcal R(S){}^{b}{}_{\eta}{}^{r \gamma j}\\
&-\frac{3}{4}W^{-4}\lambda{}_{\eta}{}^{r}(\Sigma{}_{a b}){}^{\beta \gamma}\big(\nabla^{a}W\big)\lambda{}_{\beta}{}^{j}\big(\nabla^{b}\lambda{}_{\gamma}{}^{i}\big) +\frac{1}{4}W^{-3}(\Sigma{}_{a b}){}^{\beta \gamma}\big(\nabla^{a}\lambda{}_{\eta}{}^{r}\big)\lambda{}_{\beta}{}^{j}\big(\nabla^{b}\lambda{}_{\gamma}{}^{i}\big)\\
&+\frac{1}{4}W^{-3}(\Sigma{}_{a b}){}^{\beta \gamma}\mathcal T{}^{a}{}_{\eta}{}^{\delta}\lambda{}_{\delta}{}^{r}\lambda{}_{\beta}{}^{j}\big(\nabla^{b}\lambda{}_{\gamma}{}^{i}\big) -\frac{i}{4}W^{-2}(\Sigma{}_{a b}){}^{\beta \gamma}\mathcal R(\mathbb D){}^{a}{}_{\eta}{}^{r}\lambda{}_{\beta}{}^{j}\big(\nabla^{b}\lambda{}_{\gamma}{}^{i}\big)\\
&+\frac{i}{2}W^{-3}(\Sigma{}_{a b}){}^{\beta \gamma}\big(\nabla^{a}W\big)\varepsilon{}^{r j}F{}_{\eta \beta}\big(\nabla^{b}\lambda{}_{\gamma}{}^{i}\big) +\frac{i}{2}W^{-2}(\Sigma{}_{a b}){}^{\beta \gamma}\big(\nabla^{a}W\big)\varepsilon{}^{r j}W{}_{\eta \beta}\big(\nabla^{b}\lambda{}_{\gamma}{}^{i}\big)\\
&+\frac{i}{4}W^{-3}(\Sigma{}_{a b}){}_{\eta}{}^{\beta}\big(\nabla^{a}W\big)X{}^{r j}\big(\nabla^{b}\lambda{}_{\beta}{}^{i}\big) +\frac{i}{4}W^{-3}(\Sigma{}_{a b}){}^{\beta \gamma}\big(\nabla^{a}W\big)\varepsilon{}^{r j}(\Gamma{}^{c}){}_{\eta \beta}\big(\nabla_{c}W\big)\big(\nabla^{b}\lambda{}_{\gamma}{}^{i}\big)\\
&-\frac{i}{2}W^{-3}(\Sigma{}_{a b}){}^{\beta \gamma}\big(\nabla^{a}W\big)\lambda{}_{\beta}{}^{j}\varepsilon{}^{r i}\big(\nabla^{b}F{}_{\eta \gamma}\big) -\frac{i}{2}W^{-2}(\Sigma{}_{a b}){}^{\beta \gamma}\big(\nabla^{a}W\big)\lambda{}_{\beta}{}^{j}\varepsilon{}^{r i}\big(\nabla^{b}W{}_{\eta \gamma}\big)\\
&-\frac{i}{2}W^{-3}(\Sigma{}_{a b}){}^{\beta \gamma}\big(\nabla^{a}W\big)\lambda{}_{\beta}{}^{j}\varepsilon{}^{r i}W{}_{\eta \gamma}\big(\nabla^{b}W\big) -\frac{i}{4}W^{-3}(\Sigma{}_{a b}){}^{\beta}{}_{\eta}\big(\nabla^{a}W\big)\lambda{}_{\beta}{}^{j}\big(\nabla^{b}X{}^{r i}\big)\\
&-\frac{i}{4}W^{-3}(\Sigma{}_{a b}){}^{\beta \gamma}\big(\nabla^{a}W\big)\lambda{}_{\beta}{}^{j}\varepsilon{}^{r i}(\Gamma{}^{c}){}_{\eta \gamma}\big(\nabla^{b}\nabla_{c}W\big) -\frac{i}{2}W^{-3}(\Sigma{}_{a b}){}^{\beta \gamma}\big(\nabla^{a}W\big)\lambda{}_{\beta}{}^{j}\mathcal T{}^{b}{}_{\eta}{}^{\delta}\varepsilon{}^{r i}F{}_{\delta \gamma}\\
&-\frac{i}{2}W^{-2}(\Sigma{}_{a b}){}^{\beta \gamma}\big(\nabla^{a}W\big)\lambda{}_{\beta}{}^{j}\mathcal T{}^{b}{}_{\eta}{}^{\delta}\varepsilon{}^{r i}W{}_{\delta \gamma} -\frac{i}{4}W^{-3}(\Sigma{}_{a b}){}^{\beta}{}_{\gamma}\big(\nabla^{a}W\big)\lambda{}_{\beta}{}^{j}\mathcal T{}^{b}{}_{\eta}{}^{\gamma}X{}^{r i}\\
&-\frac{i}{4}W^{-3}(\Sigma{}_{a b}){}^{\beta \gamma}\big(\nabla^{a}W\big)\lambda{}_{\beta}{}^{j}\mathcal T{}^{b}{}_{\eta}{}^{\delta}\varepsilon{}^{r i}(\Gamma{}^{c}){}_{\delta \gamma}\big(\nabla_{c}W\big) +\frac{i}{8}W^{-3}(\Sigma{}_{a b}){}^{\beta \gamma}\big(\nabla^{a}W\big)\lambda{}_{\beta}{}^{j}\mathcal R(M){}^{b}{}_{\eta}{}^{r c d}(\Sigma{}_{c d}){}_{\gamma}{}^{\delta}\lambda{}_{\delta}{}^{i}\\
&+\frac{3i}{8}W^{-3}(\Sigma{}_{a b}){}^{\beta \gamma}\big(\nabla^{a}W\big)\lambda{}_{\beta}{}^{j}\mathcal R(\mathbb D){}^{b}{}_{\eta}{}^{r}\lambda{}_{\gamma}{}^{i} -\frac{i}{8}W^{-3}(\Sigma{}_{a b}){}^{\beta \gamma}\big(\nabla^{a}W\big)\lambda{}_{\beta}{}^{j}\mathcal R(J){}^{b}{}_{\eta}{}^{r i k}\lambda{}_{\gamma k}\\
&-\frac{i}{8}W^{-3}(\Sigma{}_{a b}){}^{\beta \gamma}\big(\nabla^{a}W\big)\lambda{}_{\beta}{}^{j}\mathcal R(J){}^{b}{}_{\eta}{}^{r k i}\lambda{}_{\gamma k} +\frac{1}{2}W^{-2}(\Sigma{}_{a b}){}^{\beta}{}_{\gamma}\big(\nabla^{a}W\big)\lambda{}_{\beta}{}^{j}\mathcal R(S){}^{b}{}_{\eta}{}^{r \gamma i}
\end{aligned}
\tag{S3-H3.12-b}
```

**Check for H3.12:** all 44 written summands have weight $`7/2`$, odd parity and the same free indices $`\eta;r,i,j`$. Dummy labels are paired. The coefficient $`1/3`$ and the two external epsilons are applied once, when collecting the spinor.

#### Input H3.13

The calculated input is

```math
\left.H^{ij}\right|_{\mathrm{H3.13}}=W^{-3}\big(-\frac{3i}{16}(\Gamma^a)^{\alpha\beta}W_{ab}\lambda_\alpha^i\lambda_\beta^j\nabla^bW\big).
\tag{S3-H3.13-input}
```

Expand each written SU(2) average with weight $`1/2`$ before applying the left derivative.

Apply the product rule (S3-09), in the displayed factor order:

```math
\begin{aligned}
\left.\nabla_\eta^rH^{ij}\right|_{\mathrm{H3.13}}=&-\frac{3i}{16}\nabla_{\eta}^{r}\big(W^{-3}\big)(\Gamma{}^{a}){}^{\beta \gamma}W{}_{a b}\lambda{}_{\beta}{}^{i}\lambda{}_{\gamma}{}^{j}\big(\nabla^{b}W\big) -\frac{3i}{16}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}\nabla_{\eta}^{r}\big(W{}_{a b}\big)\lambda{}_{\beta}{}^{i}\lambda{}_{\gamma}{}^{j}\big(\nabla^{b}W\big)\\
&-\frac{3i}{16}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}W{}_{a b}\nabla_{\eta}^{r}\big(\lambda{}_{\beta}{}^{i}\big)\lambda{}_{\gamma}{}^{j}\big(\nabla^{b}W\big) +\frac{3i}{16}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}W{}_{a b}\lambda{}_{\beta}{}^{i}\nabla_{\eta}^{r}\big(\lambda{}_{\gamma}{}^{j}\big)\big(\nabla^{b}W\big)\\
&-\frac{3i}{16}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}W{}_{a b}\lambda{}_{\beta}{}^{i}\lambda{}_{\gamma}{}^{j}\nabla_{\eta}^{r}\big(\nabla^{b}W\big)
\end{aligned}
\tag{S3-H3.13-a}
```

Insert the elementary source identities and the applicable commutators (S3-11)–(S3-14), distribute the vector product rules, and contract only index-raising metrics. The resulting contribution is

```math
\begin{aligned}
\left.\nabla_\eta^rH^{ij}\right|_{\mathrm{H3.13}}=&-\frac{9}{16}W^{-4}\lambda{}_{\eta}{}^{r}(\Gamma{}^{a}){}^{\beta \gamma}W{}_{a b}\lambda{}_{\beta}{}^{i}\lambda{}_{\gamma}{}^{j}\big(\nabla^{b}W\big) -\frac{3i}{16}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}(\Sigma{}_{a b}){}^{\delta \rho}W{}_{\eta \delta \rho}{}^{r}\lambda{}_{\beta}{}^{i}\lambda{}_{\gamma}{}^{j}\big(\nabla^{b}W\big)\\
&-\frac{3i}{32}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}(\Sigma{}_{a b}){}_{\eta}{}^{\delta}X{}_{\delta}{}^{r}\lambda{}_{\beta}{}^{i}\lambda{}_{\gamma}{}^{j}\big(\nabla^{b}W\big) -\frac{3i}{32}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}(\Sigma{}_{a b}){}^{\delta}{}_{\eta}X{}_{\delta}{}^{r}\lambda{}_{\beta}{}^{i}\lambda{}_{\gamma}{}^{j}\big(\nabla^{b}W\big)\\
&+\frac{3i}{8}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}W{}_{a b}\varepsilon{}^{r i}F{}_{\eta \beta}\lambda{}_{\gamma}{}^{j}\big(\nabla^{b}W\big) +\frac{3i}{8}W^{-2}(\Gamma{}^{a}){}^{\beta \gamma}W{}_{a b}\varepsilon{}^{r i}W{}_{\eta \beta}\lambda{}_{\gamma}{}^{j}\big(\nabla^{b}W\big)\\
&+\frac{3i}{16}W^{-3}(\Gamma{}^{a}){}_{\eta}{}^{\beta}W{}_{a b}X{}^{r i}\lambda{}_{\beta}{}^{j}\big(\nabla^{b}W\big) +\frac{3i}{16}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}W{}_{a b}\varepsilon{}^{r i}(\Gamma{}^{c}){}_{\eta \beta}\big(\nabla_{c}W\big)\lambda{}_{\gamma}{}^{j}\big(\nabla^{b}W\big)\\
&-\frac{3i}{8}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}W{}_{a b}\lambda{}_{\beta}{}^{i}\varepsilon{}^{r j}F{}_{\eta \gamma}\big(\nabla^{b}W\big) -\frac{3i}{8}W^{-2}(\Gamma{}^{a}){}^{\beta \gamma}W{}_{a b}\lambda{}_{\beta}{}^{i}\varepsilon{}^{r j}W{}_{\eta \gamma}\big(\nabla^{b}W\big)\\
&-\frac{3i}{16}W^{-3}(\Gamma{}^{a}){}^{\beta}{}_{\eta}W{}_{a b}\lambda{}_{\beta}{}^{i}X{}^{r j}\big(\nabla^{b}W\big) -\frac{3i}{16}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}W{}_{a b}\lambda{}_{\beta}{}^{i}\varepsilon{}^{r j}(\Gamma{}^{c}){}_{\eta \gamma}\big(\nabla_{c}W\big)\big(\nabla^{b}W\big)\\
&+\frac{3}{16}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}W{}_{a b}\lambda{}_{\beta}{}^{i}\lambda{}_{\gamma}{}^{j}\big(\nabla^{b}\lambda{}_{\eta}{}^{r}\big) +\frac{3}{16}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}W{}_{a b}\lambda{}_{\beta}{}^{i}\lambda{}_{\gamma}{}^{j}\mathcal T{}^{b}{}_{\eta}{}^{\delta}\lambda{}_{\delta}{}^{r}\\
&-\frac{3i}{16}W^{-2}(\Gamma{}^{a}){}^{\beta \gamma}W{}_{a b}\lambda{}_{\beta}{}^{i}\lambda{}_{\gamma}{}^{j}\mathcal R(\mathbb D){}^{b}{}_{\eta}{}^{r}
\end{aligned}
\tag{S3-H3.13-b}
```

**Check for H3.13:** all 15 written summands have weight $`7/2`$, odd parity and the same free indices $`\eta;r,i,j`$. Dummy labels are paired. The coefficient $`1/3`$ and the two external epsilons are applied once, when collecting the spinor.

#### Input H3.14

The calculated input is

```math
\left.H^{ij}\right|_{\mathrm{H3.14}}=W^{-3}\big(\frac{3i}{32}W_{ab}F^{ab}\lambda^{\alpha i}\lambda_\alpha^j\big).
\tag{S3-H3.14-input}
```

Apply the product rule (S3-09), in the displayed factor order:

```math
\begin{aligned}
\left.\nabla_\eta^rH^{ij}\right|_{\mathrm{H3.14}}=&\frac{3i}{32}\nabla_{\eta}^{r}\big(W^{-3}\big)W{}_{a b}F{}^{a b}\lambda{}^{\beta i}\lambda{}_{\beta}{}^{j} +\frac{3i}{32}W^{-3}\nabla_{\eta}^{r}\big(W{}_{a b}\big)F{}^{a b}\lambda{}^{\beta i}\lambda{}_{\beta}{}^{j}\\
&+\frac{3i}{32}W^{-3}W{}_{a b}\nabla_{\eta}^{r}\big(F{}^{a b}\big)\lambda{}^{\beta i}\lambda{}_{\beta}{}^{j} +\frac{3i}{32}W^{-3}W{}_{a b}F{}^{a b}\nabla_{\eta}^{r}\big(\lambda{}^{\beta i}\big)\lambda{}_{\beta}{}^{j}\\
&-\frac{3i}{32}W^{-3}W{}_{a b}F{}^{a b}\lambda{}^{\beta i}\nabla_{\eta}^{r}\big(\lambda{}_{\beta}{}^{j}\big)
\end{aligned}
\tag{S3-H3.14-a}
```

Insert the elementary source identities and the applicable commutators (S3-11)–(S3-14), distribute the vector product rules, and contract only index-raising metrics. The resulting contribution is

```math
\begin{aligned}
\left.\nabla_\eta^rH^{ij}\right|_{\mathrm{H3.14}}=&\frac{9}{32}W^{-4}\lambda{}_{\eta}{}^{r}W{}_{a b}F{}^{a b}\lambda{}^{\beta i}\lambda{}_{\beta}{}^{j} +\frac{3i}{32}W^{-3}(\Sigma{}_{a b}){}^{\beta \gamma}W{}_{\eta \beta \gamma}{}^{r}F{}^{a b}\lambda{}^{\delta i}\lambda{}_{\delta}{}^{j}\\
&+\frac{3i}{64}W^{-3}(\Sigma{}_{a b}){}_{\eta}{}^{\beta}X{}_{\beta}{}^{r}F{}^{a b}\lambda{}^{\gamma i}\lambda{}_{\gamma}{}^{j} +\frac{3i}{64}W^{-3}(\Sigma{}_{a b}){}^{\beta}{}_{\eta}X{}_{\beta}{}^{r}F{}^{a b}\lambda{}^{\gamma i}\lambda{}_{\gamma}{}^{j}\\
&+\frac{3}{64}W^{-3}W{}_{a b}(\Sigma{}^{a b}){}^{\beta \gamma}(\Gamma{}^{c}){}_{\eta \beta}\big(\nabla_{c}\lambda{}_{\gamma}{}^{r}\big)\lambda{}^{\delta i}\lambda{}_{\delta}{}^{j} +\frac{3}{64}W^{-3}W{}_{a b}(\Sigma{}^{a b}){}_{\eta}{}^{\beta}(\Gamma{}^{c}){}_{\beta}{}^{\gamma}\big(\nabla_{c}\lambda{}_{\gamma}{}^{r}\big)\lambda{}^{\delta i}\lambda{}_{\delta}{}^{j}\\
&-\frac{3}{128}W^{-3}W{}_{a b}(\Sigma{}^{a b}){}^{\beta \gamma}W{}_{\eta \beta}\lambda{}_{\gamma}{}^{r}\lambda{}^{\delta i}\lambda{}_{\delta}{}^{j} +\frac{9}{128}W^{-3}W{}_{a b}(\Sigma{}^{a b}){}_{\eta}{}^{\beta}W{}_{\beta}{}^{\gamma}\lambda{}_{\gamma}{}^{r}\lambda{}^{\delta i}\lambda{}_{\delta}{}^{j}\\
&+\frac{3}{64}W^{-3}W{}_{a b}(\Sigma{}^{a b}){}^{\beta \gamma}(\Gamma{}^{c}){}_{\eta \gamma}\big(\nabla_{c}\lambda{}_{\beta}{}^{r}\big)\lambda{}^{\delta i}\lambda{}_{\delta}{}^{j} +\frac{3}{64}W^{-3}W{}_{a b}(\Sigma{}^{a b}){}^{\beta}{}_{\eta}(\Gamma{}^{c}){}_{\beta}{}^{\gamma}\big(\nabla_{c}\lambda{}_{\gamma}{}^{r}\big)\lambda{}^{\delta i}\lambda{}_{\delta}{}^{j}\\
&-\frac{3}{128}W^{-3}W{}_{a b}(\Sigma{}^{a b}){}^{\beta \gamma}W{}_{\eta \gamma}\lambda{}_{\beta}{}^{r}\lambda{}^{\delta i}\lambda{}_{\delta}{}^{j} +\frac{9}{128}W^{-3}W{}_{a b}(\Sigma{}^{a b}){}^{\beta}{}_{\eta}W{}_{\beta}{}^{\gamma}\lambda{}_{\gamma}{}^{r}\lambda{}^{\delta i}\lambda{}_{\delta}{}^{j}\\
&+\frac{9}{64}W^{-3}W{}_{a b}(\Sigma{}^{a b}){}^{\beta \gamma}W{}_{\beta \gamma}\lambda{}_{\eta}{}^{r}\lambda{}^{\delta i}\lambda{}_{\delta}{}^{j} -\frac{3i}{32}W^{-2}W{}_{a b}(\Sigma{}^{a b}){}^{\beta \gamma}W{}_{\eta \beta \gamma}{}^{r}\lambda{}^{\delta i}\lambda{}_{\delta}{}^{j}\\
&-\frac{3i}{16}W^{-3}W{}_{a b}F{}^{a b}\varepsilon{}^{r i}F{}_{\eta}{}^{\beta}\lambda{}_{\beta}{}^{j} -\frac{3i}{16}W^{-2}W{}_{a b}F{}^{a b}\varepsilon{}^{r i}W{}_{\eta}{}^{\beta}\lambda{}_{\beta}{}^{j}\\
&+\frac{3i}{32}W^{-3}W{}_{a b}F{}^{a b}X{}^{r i}\lambda{}_{\eta}{}^{j} -\frac{3i}{32}W^{-3}W{}_{a b}F{}^{a b}\varepsilon{}^{r i}(\Gamma{}^{c}){}_{\eta}{}^{\beta}\big(\nabla_{c}W\big)\lambda{}_{\beta}{}^{j}\\
&+\frac{3i}{16}W^{-3}W{}_{a b}F{}^{a b}\lambda{}^{\beta i}\varepsilon{}^{r j}F{}_{\eta \beta} +\frac{3i}{16}W^{-2}W{}_{a b}F{}^{a b}\lambda{}^{\beta i}\varepsilon{}^{r j}W{}_{\eta \beta}\\
&+\frac{3i}{32}W^{-3}W{}_{a b}F{}^{a b}\lambda{}_{\eta}{}^{i}X{}^{r j} +\frac{3i}{32}W^{-3}W{}_{a b}F{}^{a b}\lambda{}^{\beta i}\varepsilon{}^{r j}(\Gamma{}^{c}){}_{\eta \beta}\big(\nabla_{c}W\big)
\end{aligned}
\tag{S3-H3.14-b}
```

**Check for H3.14:** all 22 written summands have weight $`7/2`$, odd parity and the same free indices $`\eta;r,i,j`$. Dummy labels are paired. The coefficient $`1/3`$ and the two external epsilons are applied once, when collecting the spinor.

#### Input H3.15

The calculated input is

```math
\left.H^{ij}\right|_{\mathrm{H3.15}}=W^{-3}\big(\frac{9i}{64}\varepsilon^{abcde}(\Gamma_a)^{\alpha\beta}W_{bc}F_{de}\lambda_\alpha^i\lambda_\beta^j\big).
\tag{S3-H3.15-input}
```

Expand each written SU(2) average with weight $`1/2`$ before applying the left derivative.

Apply the product rule (S3-09), in the displayed factor order:

```math
\begin{aligned}
\left.\nabla_\eta^rH^{ij}\right|_{\mathrm{H3.15}}=&\frac{9i}{64}\nabla_{\eta}^{r}\big(W^{-3}\big)\varepsilon{}^{a b c d e}(\Gamma{}_{a}){}^{\beta \gamma}W{}_{b c}F{}_{d e}\lambda{}_{\beta}{}^{i}\lambda{}_{\gamma}{}^{j} +\frac{9i}{64}W^{-3}\varepsilon{}^{a b c d e}(\Gamma{}_{a}){}^{\beta \gamma}\nabla_{\eta}^{r}\big(W{}_{b c}\big)F{}_{d e}\lambda{}_{\beta}{}^{i}\lambda{}_{\gamma}{}^{j}\\
&+\frac{9i}{64}W^{-3}\varepsilon{}^{a b c d e}(\Gamma{}_{a}){}^{\beta \gamma}W{}_{b c}\nabla_{\eta}^{r}\big(F{}_{d e}\big)\lambda{}_{\beta}{}^{i}\lambda{}_{\gamma}{}^{j} +\frac{9i}{64}W^{-3}\varepsilon{}^{a b c d e}(\Gamma{}_{a}){}^{\beta \gamma}W{}_{b c}F{}_{d e}\nabla_{\eta}^{r}\big(\lambda{}_{\beta}{}^{i}\big)\lambda{}_{\gamma}{}^{j}\\
&-\frac{9i}{64}W^{-3}\varepsilon{}^{a b c d e}(\Gamma{}_{a}){}^{\beta \gamma}W{}_{b c}F{}_{d e}\lambda{}_{\beta}{}^{i}\nabla_{\eta}^{r}\big(\lambda{}_{\gamma}{}^{j}\big)
\end{aligned}
\tag{S3-H3.15-a}
```

Insert the elementary source identities and the applicable commutators (S3-11)–(S3-14), distribute the vector product rules, and contract only index-raising metrics. The resulting contribution is

```math
\begin{aligned}
\left.\nabla_\eta^rH^{ij}\right|_{\mathrm{H3.15}}=&\frac{27}{64}W^{-4}\lambda{}_{\eta}{}^{r}\varepsilon{}^{a b c d e}(\Gamma{}_{a}){}^{\beta \gamma}W{}_{b c}F{}_{d e}\lambda{}_{\beta}{}^{i}\lambda{}_{\gamma}{}^{j} +\frac{9i}{64}W^{-3}\varepsilon{}^{a b c d e}(\Gamma{}_{a}){}^{\beta \gamma}(\Sigma{}_{b c}){}^{\delta \rho}W{}_{\eta \delta \rho}{}^{r}F{}_{d e}\lambda{}_{\beta}{}^{i}\lambda{}_{\gamma}{}^{j}\\
&+\frac{9i}{128}W^{-3}\varepsilon{}^{a b c d e}(\Gamma{}_{a}){}^{\beta \gamma}(\Sigma{}_{b c}){}_{\eta}{}^{\delta}X{}_{\delta}{}^{r}F{}_{d e}\lambda{}_{\beta}{}^{i}\lambda{}_{\gamma}{}^{j} +\frac{9i}{128}W^{-3}\varepsilon{}^{a b c d e}(\Gamma{}_{a}){}^{\beta \gamma}(\Sigma{}_{b c}){}^{\delta}{}_{\eta}X{}_{\delta}{}^{r}F{}_{d e}\lambda{}_{\beta}{}^{i}\lambda{}_{\gamma}{}^{j}\\
&+\frac{9}{128}W^{-3}\varepsilon{}^{a b c d e}(\Gamma{}_{a}){}^{\beta \gamma}W{}_{b c}(\Sigma{}_{d e}){}^{\delta \rho}(\Gamma{}^{f}){}_{\eta \delta}\big(\nabla_{f}\lambda{}_{\rho}{}^{r}\big)\lambda{}_{\beta}{}^{i}\lambda{}_{\gamma}{}^{j} +\frac{9}{128}W^{-3}\varepsilon{}^{a b c d e}(\Gamma{}_{a}){}^{\beta \gamma}W{}_{b c}(\Sigma{}_{d e}){}_{\eta}{}^{\delta}(\Gamma{}^{f}){}_{\delta}{}^{\rho}\big(\nabla_{f}\lambda{}_{\rho}{}^{r}\big)\lambda{}_{\beta}{}^{i}\lambda{}_{\gamma}{}^{j}\\
&-\frac{9}{256}W^{-3}\varepsilon{}^{a b c d e}(\Gamma{}_{a}){}^{\beta \gamma}W{}_{b c}(\Sigma{}_{d e}){}^{\delta \rho}W{}_{\eta \delta}\lambda{}_{\rho}{}^{r}\lambda{}_{\beta}{}^{i}\lambda{}_{\gamma}{}^{j} +\frac{27}{256}W^{-3}\varepsilon{}^{a b c d e}(\Gamma{}_{a}){}^{\beta \gamma}W{}_{b c}(\Sigma{}_{d e}){}_{\eta}{}^{\delta}W{}_{\delta}{}^{\rho}\lambda{}_{\rho}{}^{r}\lambda{}_{\beta}{}^{i}\lambda{}_{\gamma}{}^{j}\\
&+\frac{9}{128}W^{-3}\varepsilon{}^{a b c d e}(\Gamma{}_{a}){}^{\beta \gamma}W{}_{b c}(\Sigma{}_{d e}){}^{\delta \rho}(\Gamma{}^{f}){}_{\eta \rho}\big(\nabla_{f}\lambda{}_{\delta}{}^{r}\big)\lambda{}_{\beta}{}^{i}\lambda{}_{\gamma}{}^{j} +\frac{9}{128}W^{-3}\varepsilon{}^{a b c d e}(\Gamma{}_{a}){}^{\beta \gamma}W{}_{b c}(\Sigma{}_{d e}){}^{\delta}{}_{\eta}(\Gamma{}^{f}){}_{\delta}{}^{\rho}\big(\nabla_{f}\lambda{}_{\rho}{}^{r}\big)\lambda{}_{\beta}{}^{i}\lambda{}_{\gamma}{}^{j}\\
&-\frac{9}{256}W^{-3}\varepsilon{}^{a b c d e}(\Gamma{}_{a}){}^{\beta \gamma}W{}_{b c}(\Sigma{}_{d e}){}^{\delta \rho}W{}_{\eta \rho}\lambda{}_{\delta}{}^{r}\lambda{}_{\beta}{}^{i}\lambda{}_{\gamma}{}^{j} +\frac{27}{256}W^{-3}\varepsilon{}^{a b c d e}(\Gamma{}_{a}){}^{\beta \gamma}W{}_{b c}(\Sigma{}_{d e}){}^{\delta}{}_{\eta}W{}_{\delta}{}^{\rho}\lambda{}_{\rho}{}^{r}\lambda{}_{\beta}{}^{i}\lambda{}_{\gamma}{}^{j}\\
&+\frac{27}{128}W^{-3}\varepsilon{}^{a b c d e}(\Gamma{}_{a}){}^{\beta \gamma}W{}_{b c}(\Sigma{}_{d e}){}^{\delta \rho}W{}_{\delta \rho}\lambda{}_{\eta}{}^{r}\lambda{}_{\beta}{}^{i}\lambda{}_{\gamma}{}^{j} -\frac{9i}{64}W^{-2}\varepsilon{}^{a b c d e}(\Gamma{}_{a}){}^{\beta \gamma}W{}_{b c}(\Sigma{}_{d e}){}^{\delta \rho}W{}_{\eta \delta \rho}{}^{r}\lambda{}_{\beta}{}^{i}\lambda{}_{\gamma}{}^{j}\\
&-\frac{9i}{32}W^{-3}\varepsilon{}^{a b c d e}(\Gamma{}_{a}){}^{\beta \gamma}W{}_{b c}F{}_{d e}\varepsilon{}^{r i}F{}_{\eta \beta}\lambda{}_{\gamma}{}^{j} -\frac{9i}{32}W^{-2}\varepsilon{}^{a b c d e}(\Gamma{}_{a}){}^{\beta \gamma}W{}_{b c}F{}_{d e}\varepsilon{}^{r i}W{}_{\eta \beta}\lambda{}_{\gamma}{}^{j}\\
&-\frac{9i}{64}W^{-3}\varepsilon{}^{a b c d e}(\Gamma{}_{a}){}_{\eta}{}^{\beta}W{}_{b c}F{}_{d e}X{}^{r i}\lambda{}_{\beta}{}^{j} -\frac{9i}{64}W^{-3}\varepsilon{}^{a b c d e}(\Gamma{}_{a}){}^{\beta \gamma}W{}_{b c}F{}_{d e}\varepsilon{}^{r i}(\Gamma{}^{f}){}_{\eta \beta}\big(\nabla_{f}W\big)\lambda{}_{\gamma}{}^{j}\\
&+\frac{9i}{32}W^{-3}\varepsilon{}^{a b c d e}(\Gamma{}_{a}){}^{\beta \gamma}W{}_{b c}F{}_{d e}\lambda{}_{\beta}{}^{i}\varepsilon{}^{r j}F{}_{\eta \gamma} +\frac{9i}{32}W^{-2}\varepsilon{}^{a b c d e}(\Gamma{}_{a}){}^{\beta \gamma}W{}_{b c}F{}_{d e}\lambda{}_{\beta}{}^{i}\varepsilon{}^{r j}W{}_{\eta \gamma}\\
&+\frac{9i}{64}W^{-3}\varepsilon{}^{a b c d e}(\Gamma{}_{a}){}^{\beta}{}_{\eta}W{}_{b c}F{}_{d e}\lambda{}_{\beta}{}^{i}X{}^{r j} +\frac{9i}{64}W^{-3}\varepsilon{}^{a b c d e}(\Gamma{}_{a}){}^{\beta \gamma}W{}_{b c}F{}_{d e}\lambda{}_{\beta}{}^{i}\varepsilon{}^{r j}(\Gamma{}^{f}){}_{\eta \gamma}\big(\nabla_{f}W\big)
\end{aligned}
\tag{S3-H3.15-b}
```

**Check for H3.15:** all 22 written summands have weight $`7/2`$, odd parity and the same free indices $`\eta;r,i,j`$. Dummy labels are paired. The coefficient $`1/3`$ and the two external epsilons are applied once, when collecting the spinor.

#### Input H3.16

The calculated input is

```math
\left.H^{ij}\right|_{\mathrm{H3.16}}=W^{-3}\big(-\frac{3i}{32}(\Sigma_{ab})^{\alpha\beta}X^{ij}W^{ab}\lambda_\alpha^k\lambda_{\beta k}\big).
\tag{S3-H3.16-input}
```

Expand each written SU(2) average with weight $`1/2`$ before applying the left derivative.

Apply the product rule (S3-09), in the displayed factor order:

```math
\begin{aligned}
\left.\nabla_\eta^rH^{ij}\right|_{\mathrm{H3.16}}=&-\frac{3i}{32}\nabla_{\eta}^{r}\big(W^{-3}\big)(\Sigma{}_{a b}){}^{\beta \gamma}X{}^{i j}W{}^{a b}\lambda{}_{\beta}{}^{k}\lambda{}_{\gamma k} -\frac{3i}{32}W^{-3}(\Sigma{}_{a b}){}^{\beta \gamma}\nabla_{\eta}^{r}\big(X{}^{i j}\big)W{}^{a b}\lambda{}_{\beta}{}^{k}\lambda{}_{\gamma k}\\
&-\frac{3i}{32}W^{-3}(\Sigma{}_{a b}){}^{\beta \gamma}X{}^{i j}\nabla_{\eta}^{r}\big(W{}^{a b}\big)\lambda{}_{\beta}{}^{k}\lambda{}_{\gamma k} -\frac{3i}{32}W^{-3}(\Sigma{}_{a b}){}^{\beta \gamma}X{}^{i j}W{}^{a b}\nabla_{\eta}^{r}\big(\lambda{}_{\beta}{}^{k}\big)\lambda{}_{\gamma k}\\
&+\frac{3i}{32}W^{-3}(\Sigma{}_{a b}){}^{\beta \gamma}X{}^{i j}W{}^{a b}\lambda{}_{\beta}{}^{k}\nabla_{\eta}^{r}\big(\lambda{}_{\gamma k}\big)
\end{aligned}
\tag{S3-H3.16-a}
```

Insert the elementary source identities and the applicable commutators (S3-11)–(S3-14), distribute the vector product rules, and contract only index-raising metrics. The resulting contribution is

```math
\begin{aligned}
\left.\nabla_\eta^rH^{ij}\right|_{\mathrm{H3.16}}=&-\frac{9}{32}W^{-4}\lambda{}_{\eta}{}^{r}(\Sigma{}_{a b}){}^{\beta \gamma}X{}^{i j}W{}^{a b}\lambda{}_{\beta}{}^{k}\lambda{}_{\gamma k} +\frac{3}{32}W^{-3}(\Sigma{}_{a b}){}^{\beta \gamma}\varepsilon{}^{r i}(\Gamma{}^{c}){}_{\eta}{}^{\delta}\big(\nabla_{c}\lambda{}_{\delta}{}^{j}\big)W{}^{a b}\lambda{}_{\beta}{}^{k}\lambda{}_{\gamma k}\\
&-\frac{3}{64}W^{-3}(\Sigma{}_{a b}){}^{\beta \gamma}\varepsilon{}^{r i}W{}_{\eta \delta}\lambda{}^{\delta j}W{}^{a b}\lambda{}_{\beta}{}^{k}\lambda{}_{\gamma k} +\frac{9i}{128}W^{-2}(\Sigma{}_{a b}){}^{\beta \gamma}\varepsilon{}^{r i}X{}_{\eta}{}^{j}W{}^{a b}\lambda{}_{\beta}{}^{k}\lambda{}_{\gamma k}\\
&+\frac{3}{32}W^{-3}(\Sigma{}_{a b}){}^{\beta \gamma}\varepsilon{}^{r j}(\Gamma{}^{c}){}_{\eta}{}^{\delta}\big(\nabla_{c}\lambda{}_{\delta}{}^{i}\big)W{}^{a b}\lambda{}_{\beta}{}^{k}\lambda{}_{\gamma k} -\frac{3}{64}W^{-3}(\Sigma{}_{a b}){}^{\beta \gamma}\varepsilon{}^{r j}W{}_{\eta \delta}\lambda{}^{\delta i}W{}^{a b}\lambda{}_{\beta}{}^{k}\lambda{}_{\gamma k}\\
&+\frac{9i}{128}W^{-2}(\Sigma{}_{a b}){}^{\beta \gamma}\varepsilon{}^{r j}X{}_{\eta}{}^{i}W{}^{a b}\lambda{}_{\beta}{}^{k}\lambda{}_{\gamma k} -\frac{3i}{32}W^{-3}(\Sigma{}_{a b}){}^{\beta \gamma}X{}^{i j}(\Sigma{}^{a b}){}^{\delta \rho}W{}_{\eta \delta \rho}{}^{r}\lambda{}_{\beta}{}^{k}\lambda{}_{\gamma k}\\
&-\frac{3i}{64}W^{-3}(\Sigma{}_{a b}){}^{\beta \gamma}X{}^{i j}(\Sigma{}^{a b}){}_{\eta}{}^{\delta}X{}_{\delta}{}^{r}\lambda{}_{\beta}{}^{k}\lambda{}_{\gamma k} -\frac{3i}{64}W^{-3}(\Sigma{}_{a b}){}^{\beta \gamma}X{}^{i j}(\Sigma{}^{a b}){}^{\delta}{}_{\eta}X{}_{\delta}{}^{r}\lambda{}_{\beta}{}^{k}\lambda{}_{\gamma k}\\
&+\frac{3i}{16}W^{-3}(\Sigma{}_{a b}){}^{\beta \gamma}X{}^{i j}W{}^{a b}F{}_{\eta \beta}\lambda{}_{\gamma}{}^{r} +\frac{3i}{16}W^{-2}(\Sigma{}_{a b}){}^{\beta \gamma}X{}^{i j}W{}^{a b}W{}_{\eta \beta}\lambda{}_{\gamma}{}^{r}\\
&+\frac{3i}{32}W^{-3}(\Sigma{}_{a b}){}_{\eta}{}^{\beta}X{}^{i j}W{}^{a b}X{}^{r k}\lambda{}_{\beta k} +\frac{3i}{32}W^{-3}(\Sigma{}_{a b}){}^{\beta \gamma}X{}^{i j}W{}^{a b}(\Gamma{}^{c}){}_{\eta \beta}\big(\nabla_{c}W\big)\lambda{}_{\gamma}{}^{r}\\
&+\frac{3i}{16}W^{-3}(\Sigma{}_{a b}){}^{\beta \gamma}X{}^{i j}W{}^{a b}\lambda{}_{\beta}{}^{r}F{}_{\eta \gamma} +\frac{3i}{16}W^{-2}(\Sigma{}_{a b}){}^{\beta \gamma}X{}^{i j}W{}^{a b}\lambda{}_{\beta}{}^{r}W{}_{\eta \gamma}\\
&-\frac{3i}{32}W^{-3}(\Sigma{}_{a b}){}^{\beta}{}_{\eta}X{}^{i j}W{}^{a b}\lambda{}_{\beta}{}^{k}X{}^{r}{}_{k} +\frac{3i}{32}W^{-3}(\Sigma{}_{a b}){}^{\beta \gamma}X{}^{i j}W{}^{a b}\lambda{}_{\beta}{}^{r}(\Gamma{}^{c}){}_{\eta \gamma}\big(\nabla_{c}W\big)
\end{aligned}
\tag{S3-H3.16-b}
```

**Check for H3.16:** all 18 written summands have weight $`7/2`$, odd parity and the same free indices $`\eta;r,i,j`$. Dummy labels are paired. The coefficient $`1/3`$ and the two external epsilons are applied once, when collecting the spinor.

#### Input H3.17

The calculated input is

```math
\left.H^{ij}\right|_{\mathrm{H3.17}}=W^{-3}\big(-\frac{3i}{8}X^{\alpha k}\lambda_\alpha^{(i}\lambda^{\beta j)}\lambda_{\beta k}\big).
\tag{S3-H3.17-input}
```

Expand each written SU(2) average with weight $`1/2`$ before applying the left derivative.

Apply the product rule (S3-09), in the displayed factor order:

```math
\begin{aligned}
\left.\nabla_\eta^rH^{ij}\right|_{\mathrm{H3.17}}=&-\frac{3i}{16}\nabla_{\eta}^{r}\big(W^{-3}\big)X{}^{\beta k}\lambda{}_{\beta}{}^{i}\lambda{}^{\gamma j}\lambda{}_{\gamma k} -\frac{3i}{16}W^{-3}\nabla_{\eta}^{r}\big(X{}^{\beta k}\big)\lambda{}_{\beta}{}^{i}\lambda{}^{\gamma j}\lambda{}_{\gamma k}\\
&+\frac{3i}{16}W^{-3}X{}^{\beta k}\nabla_{\eta}^{r}\big(\lambda{}_{\beta}{}^{i}\big)\lambda{}^{\gamma j}\lambda{}_{\gamma k} -\frac{3i}{16}W^{-3}X{}^{\beta k}\lambda{}_{\beta}{}^{i}\nabla_{\eta}^{r}\big(\lambda{}^{\gamma j}\big)\lambda{}_{\gamma k}\\
&+\frac{3i}{16}W^{-3}X{}^{\beta k}\lambda{}_{\beta}{}^{i}\lambda{}^{\gamma j}\nabla_{\eta}^{r}\big(\lambda{}_{\gamma k}\big) -\frac{3i}{16}\nabla_{\eta}^{r}\big(W^{-3}\big)X{}^{\beta k}\lambda{}_{\beta}{}^{j}\lambda{}^{\gamma i}\lambda{}_{\gamma k}\\
&-\frac{3i}{16}W^{-3}\nabla_{\eta}^{r}\big(X{}^{\beta k}\big)\lambda{}_{\beta}{}^{j}\lambda{}^{\gamma i}\lambda{}_{\gamma k} +\frac{3i}{16}W^{-3}X{}^{\beta k}\nabla_{\eta}^{r}\big(\lambda{}_{\beta}{}^{j}\big)\lambda{}^{\gamma i}\lambda{}_{\gamma k}\\
&-\frac{3i}{16}W^{-3}X{}^{\beta k}\lambda{}_{\beta}{}^{j}\nabla_{\eta}^{r}\big(\lambda{}^{\gamma i}\big)\lambda{}_{\gamma k} +\frac{3i}{16}W^{-3}X{}^{\beta k}\lambda{}_{\beta}{}^{j}\lambda{}^{\gamma i}\nabla_{\eta}^{r}\big(\lambda{}_{\gamma k}\big)
\end{aligned}
\tag{S3-H3.17-a}
```

Insert the elementary source identities and the applicable commutators (S3-11)–(S3-14), distribute the vector product rules, and contract only index-raising metrics. The resulting contribution is

```math
\begin{aligned}
\left.\nabla_\eta^rH^{ij}\right|_{\mathrm{H3.17}}=&-\frac{9}{16}W^{-4}\lambda{}_{\eta}{}^{r}X{}^{\beta k}\lambda{}_{\beta}{}^{i}\lambda{}^{\gamma j}\lambda{}_{\gamma k} -\frac{3i}{16}W^{-3}X{}_{\eta}{}^{\beta r k}\lambda{}_{\beta}{}^{i}\lambda{}^{\gamma j}\lambda{}_{\gamma k}\\
&-\frac{3}{128}W^{-3}Y\lambda{}_{\eta}{}^{i}\lambda{}^{\beta j}\lambda{}_{\beta}{}^{r} -\frac{9}{32}W^{-3}(\Gamma{}^{a}){}_{\eta}{}^{\beta}\big(\nabla_{a}W{}^{\gamma}{}_{\beta}\big)\lambda{}_{\gamma}{}^{i}\lambda{}^{\delta j}\lambda{}_{\delta}{}^{r}\\
&-\frac{3}{8}W^{-3}W{}_{\eta}{}^{\beta}W{}^{\gamma}{}_{\beta}\lambda{}_{\gamma}{}^{i}\lambda{}^{\delta j}\lambda{}_{\delta}{}^{r} -\frac{3}{32}W^{-3}W{}^{\beta \gamma}W{}_{\beta \gamma}\lambda{}_{\eta}{}^{i}\lambda{}^{\delta j}\lambda{}_{\delta}{}^{r}\\
&-\frac{3}{32}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}\big(\nabla_{a}W{}_{\eta \gamma}\big)\lambda{}_{\beta}{}^{i}\lambda{}^{\delta j}\lambda{}_{\delta}{}^{r} -\frac{3i}{8}W^{-3}X{}^{\beta k}\varepsilon{}^{r i}F{}_{\eta \beta}\lambda{}^{\gamma j}\lambda{}_{\gamma k}\\
&-\frac{3i}{8}W^{-2}X{}^{\beta k}\varepsilon{}^{r i}W{}_{\eta \beta}\lambda{}^{\gamma j}\lambda{}_{\gamma k} -\frac{3i}{16}W^{-3}X{}_{\eta}{}^{k}X{}^{r i}\lambda{}^{\beta j}\lambda{}_{\beta k}\\
&-\frac{3i}{16}W^{-3}X{}^{\beta k}\varepsilon{}^{r i}(\Gamma{}^{a}){}_{\eta \beta}\big(\nabla_{a}W\big)\lambda{}^{\gamma j}\lambda{}_{\gamma k} +\frac{3i}{8}W^{-3}X{}^{\beta k}\lambda{}_{\beta}{}^{i}\varepsilon{}^{r j}F{}_{\eta}{}^{\gamma}\lambda{}_{\gamma k}\\
&+\frac{3i}{8}W^{-2}X{}^{\beta k}\lambda{}_{\beta}{}^{i}\varepsilon{}^{r j}W{}_{\eta}{}^{\gamma}\lambda{}_{\gamma k} -\frac{3i}{16}W^{-3}X{}^{\beta k}\lambda{}_{\beta}{}^{i}X{}^{r j}\lambda{}_{\eta k}\\
&+\frac{3i}{16}W^{-3}X{}^{\beta k}\lambda{}_{\beta}{}^{i}\varepsilon{}^{r j}(\Gamma{}^{a}){}_{\eta}{}^{\gamma}\big(\nabla_{a}W\big)\lambda{}_{\gamma k} +\frac{3i}{8}W^{-3}X{}^{\beta r}\lambda{}_{\beta}{}^{i}\lambda{}^{\gamma j}F{}_{\eta \gamma}\\
&+\frac{3i}{8}W^{-2}X{}^{\beta r}\lambda{}_{\beta}{}^{i}\lambda{}^{\gamma j}W{}_{\eta \gamma} -\frac{3i}{16}W^{-3}X{}^{\beta k}\lambda{}_{\beta}{}^{i}\lambda{}_{\eta}{}^{j}X{}^{r}{}_{k}\\
&+\frac{3i}{16}W^{-3}X{}^{\beta r}\lambda{}_{\beta}{}^{i}\lambda{}^{\gamma j}(\Gamma{}^{a}){}_{\eta \gamma}\big(\nabla_{a}W\big) -\frac{9}{16}W^{-4}\lambda{}_{\eta}{}^{r}X{}^{\beta k}\lambda{}_{\beta}{}^{j}\lambda{}^{\gamma i}\lambda{}_{\gamma k}\\
&-\frac{3i}{16}W^{-3}X{}_{\eta}{}^{\beta r k}\lambda{}_{\beta}{}^{j}\lambda{}^{\gamma i}\lambda{}_{\gamma k} -\frac{3}{128}W^{-3}Y\lambda{}_{\eta}{}^{j}\lambda{}^{\beta i}\lambda{}_{\beta}{}^{r}\\
&-\frac{9}{32}W^{-3}(\Gamma{}^{a}){}_{\eta}{}^{\beta}\big(\nabla_{a}W{}^{\gamma}{}_{\beta}\big)\lambda{}_{\gamma}{}^{j}\lambda{}^{\delta i}\lambda{}_{\delta}{}^{r} -\frac{3}{8}W^{-3}W{}_{\eta}{}^{\beta}W{}^{\gamma}{}_{\beta}\lambda{}_{\gamma}{}^{j}\lambda{}^{\delta i}\lambda{}_{\delta}{}^{r}\\
&-\frac{3}{32}W^{-3}W{}^{\beta \gamma}W{}_{\beta \gamma}\lambda{}_{\eta}{}^{j}\lambda{}^{\delta i}\lambda{}_{\delta}{}^{r} -\frac{3}{32}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}\big(\nabla_{a}W{}_{\eta \gamma}\big)\lambda{}_{\beta}{}^{j}\lambda{}^{\delta i}\lambda{}_{\delta}{}^{r}\\
&-\frac{3i}{8}W^{-3}X{}^{\beta k}\varepsilon{}^{r j}F{}_{\eta \beta}\lambda{}^{\gamma i}\lambda{}_{\gamma k} -\frac{3i}{8}W^{-2}X{}^{\beta k}\varepsilon{}^{r j}W{}_{\eta \beta}\lambda{}^{\gamma i}\lambda{}_{\gamma k}\\
&-\frac{3i}{16}W^{-3}X{}_{\eta}{}^{k}X{}^{r j}\lambda{}^{\beta i}\lambda{}_{\beta k} -\frac{3i}{16}W^{-3}X{}^{\beta k}\varepsilon{}^{r j}(\Gamma{}^{a}){}_{\eta \beta}\big(\nabla_{a}W\big)\lambda{}^{\gamma i}\lambda{}_{\gamma k}\\
&+\frac{3i}{8}W^{-3}X{}^{\beta k}\lambda{}_{\beta}{}^{j}\varepsilon{}^{r i}F{}_{\eta}{}^{\gamma}\lambda{}_{\gamma k} +\frac{3i}{8}W^{-2}X{}^{\beta k}\lambda{}_{\beta}{}^{j}\varepsilon{}^{r i}W{}_{\eta}{}^{\gamma}\lambda{}_{\gamma k}\\
&-\frac{3i}{16}W^{-3}X{}^{\beta k}\lambda{}_{\beta}{}^{j}X{}^{r i}\lambda{}_{\eta k} +\frac{3i}{16}W^{-3}X{}^{\beta k}\lambda{}_{\beta}{}^{j}\varepsilon{}^{r i}(\Gamma{}^{a}){}_{\eta}{}^{\gamma}\big(\nabla_{a}W\big)\lambda{}_{\gamma k}\\
&+\frac{3i}{8}W^{-3}X{}^{\beta r}\lambda{}_{\beta}{}^{j}\lambda{}^{\gamma i}F{}_{\eta \gamma} +\frac{3i}{8}W^{-2}X{}^{\beta r}\lambda{}_{\beta}{}^{j}\lambda{}^{\gamma i}W{}_{\eta \gamma}\\
&-\frac{3i}{16}W^{-3}X{}^{\beta k}\lambda{}_{\beta}{}^{j}\lambda{}_{\eta}{}^{i}X{}^{r}{}_{k} +\frac{3i}{16}W^{-3}X{}^{\beta r}\lambda{}_{\beta}{}^{j}\lambda{}^{\gamma i}(\Gamma{}^{a}){}_{\eta \gamma}\big(\nabla_{a}W\big)
\end{aligned}
\tag{S3-H3.17-b}
```

**Check for H3.17:** all 38 written summands have weight $`7/2`$, odd parity and the same free indices $`\eta;r,i,j`$. Dummy labels are paired. The coefficient $`1/3`$ and the two external epsilons are applied once, when collecting the spinor.

#### Input H3.18

The calculated input is

```math
\left.H^{ij}\right|_{\mathrm{H3.18}}=W^{-3}\big(-\frac{3i}{8}X^{\alpha k}\lambda^{\beta i}\lambda_\beta^j\lambda_{\alpha k}\big).
\tag{S3-H3.18-input}
```

Apply the product rule (S3-09), in the displayed factor order:

```math
\begin{aligned}
\left.\nabla_\eta^rH^{ij}\right|_{\mathrm{H3.18}}=&-\frac{3i}{8}\nabla_{\eta}^{r}\big(W^{-3}\big)X{}^{\beta k}\lambda{}^{\gamma i}\lambda{}_{\gamma}{}^{j}\lambda{}_{\beta k} -\frac{3i}{8}W^{-3}\nabla_{\eta}^{r}\big(X{}^{\beta k}\big)\lambda{}^{\gamma i}\lambda{}_{\gamma}{}^{j}\lambda{}_{\beta k}\\
&+\frac{3i}{8}W^{-3}X{}^{\beta k}\nabla_{\eta}^{r}\big(\lambda{}^{\gamma i}\big)\lambda{}_{\gamma}{}^{j}\lambda{}_{\beta k} -\frac{3i}{8}W^{-3}X{}^{\beta k}\lambda{}^{\gamma i}\nabla_{\eta}^{r}\big(\lambda{}_{\gamma}{}^{j}\big)\lambda{}_{\beta k}\\
&+\frac{3i}{8}W^{-3}X{}^{\beta k}\lambda{}^{\gamma i}\lambda{}_{\gamma}{}^{j}\nabla_{\eta}^{r}\big(\lambda{}_{\beta k}\big)
\end{aligned}
\tag{S3-H3.18-a}
```

Insert the elementary source identities and the applicable commutators (S3-11)–(S3-14), distribute the vector product rules, and contract only index-raising metrics. The resulting contribution is

```math
\begin{aligned}
\left.\nabla_\eta^rH^{ij}\right|_{\mathrm{H3.18}}=&-\frac{9}{8}W^{-4}\lambda{}_{\eta}{}^{r}X{}^{\beta k}\lambda{}^{\gamma i}\lambda{}_{\gamma}{}^{j}\lambda{}_{\beta k} -\frac{3i}{8}W^{-3}X{}_{\eta}{}^{\beta r k}\lambda{}^{\gamma i}\lambda{}_{\gamma}{}^{j}\lambda{}_{\beta k}\\
&-\frac{3}{64}W^{-3}Y\lambda{}^{\beta i}\lambda{}_{\beta}{}^{j}\lambda{}_{\eta}{}^{r} -\frac{9}{16}W^{-3}(\Gamma{}^{a}){}_{\eta}{}^{\beta}\big(\nabla_{a}W{}^{\gamma}{}_{\beta}\big)\lambda{}^{\delta i}\lambda{}_{\delta}{}^{j}\lambda{}_{\gamma}{}^{r}\\
&-\frac{3}{4}W^{-3}W{}_{\eta}{}^{\beta}W{}^{\gamma}{}_{\beta}\lambda{}^{\delta i}\lambda{}_{\delta}{}^{j}\lambda{}_{\gamma}{}^{r} -\frac{3}{16}W^{-3}W{}^{\beta \gamma}W{}_{\beta \gamma}\lambda{}^{\delta i}\lambda{}_{\delta}{}^{j}\lambda{}_{\eta}{}^{r}\\
&-\frac{3}{16}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}\big(\nabla_{a}W{}_{\eta \gamma}\big)\lambda{}^{\delta i}\lambda{}_{\delta}{}^{j}\lambda{}_{\beta}{}^{r} -\frac{3i}{4}W^{-3}X{}^{\beta k}\varepsilon{}^{r i}F{}_{\eta}{}^{\gamma}\lambda{}_{\gamma}{}^{j}\lambda{}_{\beta k}\\
&-\frac{3i}{4}W^{-2}X{}^{\beta k}\varepsilon{}^{r i}W{}_{\eta}{}^{\gamma}\lambda{}_{\gamma}{}^{j}\lambda{}_{\beta k} +\frac{3i}{8}W^{-3}X{}^{\beta k}X{}^{r i}\lambda{}_{\eta}{}^{j}\lambda{}_{\beta k}\\
&-\frac{3i}{8}W^{-3}X{}^{\beta k}\varepsilon{}^{r i}(\Gamma{}^{a}){}_{\eta}{}^{\gamma}\big(\nabla_{a}W\big)\lambda{}_{\gamma}{}^{j}\lambda{}_{\beta k} +\frac{3i}{4}W^{-3}X{}^{\beta k}\lambda{}^{\gamma i}\varepsilon{}^{r j}F{}_{\eta \gamma}\lambda{}_{\beta k}\\
&+\frac{3i}{4}W^{-2}X{}^{\beta k}\lambda{}^{\gamma i}\varepsilon{}^{r j}W{}_{\eta \gamma}\lambda{}_{\beta k} +\frac{3i}{8}W^{-3}X{}^{\beta k}\lambda{}_{\eta}{}^{i}X{}^{r j}\lambda{}_{\beta k}\\
&+\frac{3i}{8}W^{-3}X{}^{\beta k}\lambda{}^{\gamma i}\varepsilon{}^{r j}(\Gamma{}^{a}){}_{\eta \gamma}\big(\nabla_{a}W\big)\lambda{}_{\beta k} +\frac{3i}{4}W^{-3}X{}^{\beta r}\lambda{}^{\gamma i}\lambda{}_{\gamma}{}^{j}F{}_{\eta \beta}\\
&+\frac{3i}{4}W^{-2}X{}^{\beta r}\lambda{}^{\gamma i}\lambda{}_{\gamma}{}^{j}W{}_{\eta \beta} -\frac{3i}{8}W^{-3}X{}_{\eta}{}^{k}\lambda{}^{\beta i}\lambda{}_{\beta}{}^{j}X{}^{r}{}_{k}\\
&+\frac{3i}{8}W^{-3}X{}^{\beta r}\lambda{}^{\gamma i}\lambda{}_{\gamma}{}^{j}(\Gamma{}^{a}){}_{\eta \beta}\big(\nabla_{a}W\big)
\end{aligned}
\tag{S3-H3.18-b}
```

**Check for H3.18:** all 19 written summands have weight $`7/2`$, odd parity and the same free indices $`\eta;r,i,j`$. Dummy labels are paired. The coefficient $`1/3`$ and the two external epsilons are applied once, when collecting the spinor.


[Previous component](convention_001.md) · [Component index](../STEP_03_LOG_SPINOR.md) · [Next component](derivation_003.md)
