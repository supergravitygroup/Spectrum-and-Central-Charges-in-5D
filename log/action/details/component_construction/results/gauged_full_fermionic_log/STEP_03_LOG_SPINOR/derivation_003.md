# LOG spinor descent — S3-H4.1-input – S3-H5.3-b

<a id="step-3--deriving-the-log-spinor--48-differentiate-every-input-in-the-w-4-sector"></a>

[Component index](../STEP_03_LOG_SPINOR.md). Definitions and source conventions are in [the opening section](convention_001.md).

### 4.8 Differentiate every input in the $`W^{-4}`$ sector

<!-- ASSERT_CONVENTION: source_frame=Gold traceless Standard-Weyl superspace, derivative_parity=odd left, fermions=all degrees retained -->

#### Input H4.1

The calculated input is

```math
\left.H^{ij}\right|_{\mathrm{H4.1}}=W^{-4}\big(-\frac{3i}{16}\lambda^{\alpha i}\lambda_\alpha^j(\nabla^aW)\nabla_aW\big).
\tag{S3-H4.1-input}
```

Expand each written SU(2) average with weight $`1/2`$ before applying the left derivative.

Apply the product rule (S3-09), in the displayed factor order:

```math
\begin{aligned}
\left.\nabla_\eta^rH^{ij}\right|_{\mathrm{H4.1}}=&-\frac{3i}{16}\nabla_{\eta}^{r}\big(W^{-4}\big)\lambda{}^{\beta i}\lambda{}_{\beta}{}^{j}\big(\nabla^{a}W\big)\big(\nabla_{a}W\big) -\frac{3i}{16}W^{-4}\nabla_{\eta}^{r}\big(\lambda{}^{\beta i}\big)\lambda{}_{\beta}{}^{j}\big(\nabla^{a}W\big)\big(\nabla_{a}W\big)\\
&+\frac{3i}{16}W^{-4}\lambda{}^{\beta i}\nabla_{\eta}^{r}\big(\lambda{}_{\beta}{}^{j}\big)\big(\nabla^{a}W\big)\big(\nabla_{a}W\big) -\frac{3i}{16}W^{-4}\lambda{}^{\beta i}\lambda{}_{\beta}{}^{j}\nabla_{\eta}^{r}\big(\nabla^{a}W\big)\big(\nabla_{a}W\big)\\
&-\frac{3i}{16}W^{-4}\lambda{}^{\beta i}\lambda{}_{\beta}{}^{j}\big(\nabla^{a}W\big)\nabla_{\eta}^{r}\big(\nabla_{a}W\big)
\end{aligned}
\tag{S3-H4.1-a}
```

Insert the elementary source identities and the applicable commutators (S3-11)–(S3-14), distribute the vector product rules, and contract only index-raising metrics. The resulting contribution is

```math
\begin{aligned}
\left.\nabla_\eta^rH^{ij}\right|_{\mathrm{H4.1}}=&-\frac{3}{4}W^{-5}\lambda{}_{\eta}{}^{r}\lambda{}^{\beta i}\lambda{}_{\beta}{}^{j}\big(\nabla^{a}W\big)\big(\nabla_{a}W\big) +\frac{3i}{8}W^{-4}\varepsilon{}^{r i}F{}_{\eta}{}^{\beta}\lambda{}_{\beta}{}^{j}\big(\nabla^{a}W\big)\big(\nabla_{a}W\big)\\
&+\frac{3i}{8}W^{-3}\varepsilon{}^{r i}W{}_{\eta}{}^{\beta}\lambda{}_{\beta}{}^{j}\big(\nabla^{a}W\big)\big(\nabla_{a}W\big) -\frac{3i}{16}W^{-4}X{}^{r i}\lambda{}_{\eta}{}^{j}\big(\nabla^{a}W\big)\big(\nabla_{a}W\big)\\
&+\frac{3i}{16}W^{-4}\varepsilon{}^{r i}(\Gamma{}^{a}){}_{\eta}{}^{\beta}\big(\nabla_{a}W\big)\lambda{}_{\beta}{}^{j}\big(\nabla^{b}W\big)\big(\nabla_{b}W\big) -\frac{3i}{8}W^{-4}\lambda{}^{\beta i}\varepsilon{}^{r j}F{}_{\eta \beta}\big(\nabla^{a}W\big)\big(\nabla_{a}W\big)\\
&-\frac{3i}{8}W^{-3}\lambda{}^{\beta i}\varepsilon{}^{r j}W{}_{\eta \beta}\big(\nabla^{a}W\big)\big(\nabla_{a}W\big) -\frac{3i}{16}W^{-4}\lambda{}_{\eta}{}^{i}X{}^{r j}\big(\nabla^{a}W\big)\big(\nabla_{a}W\big)\\
&-\frac{3i}{16}W^{-4}\lambda{}^{\beta i}\varepsilon{}^{r j}(\Gamma{}^{a}){}_{\eta \beta}\big(\nabla_{a}W\big)\big(\nabla^{b}W\big)\big(\nabla_{b}W\big) +\frac{3}{16}W^{-4}\lambda{}^{\beta i}\lambda{}_{\beta}{}^{j}\big(\nabla^{a}\lambda{}_{\eta}{}^{r}\big)\big(\nabla_{a}W\big)\\
&+\frac{3}{16}W^{-4}\lambda{}^{\beta i}\lambda{}_{\beta}{}^{j}\mathcal T{}^{a}{}_{\eta}{}^{\gamma}\lambda{}_{\gamma}{}^{r}\big(\nabla_{a}W\big) -\frac{3i}{16}W^{-3}\lambda{}^{\beta i}\lambda{}_{\beta}{}^{j}\mathcal R(\mathbb D){}^{a}{}_{\eta}{}^{r}\big(\nabla_{a}W\big)\\
&+\frac{3}{16}W^{-4}\lambda{}^{\beta i}\lambda{}_{\beta}{}^{j}\big(\nabla^{a}W\big)\big(\nabla_{a}\lambda{}_{\eta}{}^{r}\big) +\frac{3}{16}W^{-4}\lambda{}^{\beta i}\lambda{}_{\beta}{}^{j}\big(\nabla^{a}W\big)\mathcal T{}_{a \eta}{}^{\gamma}\lambda{}_{\gamma}{}^{r}\\
&-\frac{3i}{16}W^{-3}\lambda{}^{\beta i}\lambda{}_{\beta}{}^{j}\big(\nabla^{a}W\big)\mathcal R(\mathbb D){}_{a \eta}{}^{r}
\end{aligned}
\tag{S3-H4.1-b}
```

**Check for H4.1:** all 15 written summands have weight $`7/2`$, odd parity and the same free indices $`\eta;r,i,j`$. Dummy labels are paired. The coefficient $`1/3`$ and the two external epsilons are applied once, when collecting the spinor.

#### Input H4.2

The calculated input is

```math
\left.H^{ij}\right|_{\mathrm{H4.2}}=W^{-4}\big(-\frac{3i}{8}(\Gamma^a)^{\alpha\beta}X^{k(i}\lambda_\alpha^{j)}\lambda_{\beta k}\nabla_aW\big).
\tag{S3-H4.2-input}
```

Expand each written SU(2) average with weight $`1/2`$ before applying the left derivative.

Apply the product rule (S3-09), in the displayed factor order:

```math
\begin{aligned}
\left.\nabla_\eta^rH^{ij}\right|_{\mathrm{H4.2}}=&-\frac{3i}{16}\nabla_{\eta}^{r}\big(W^{-4}\big)(\Gamma{}^{a}){}^{\beta \gamma}X{}^{k i}\lambda{}_{\beta}{}^{j}\lambda{}_{\gamma k}\big(\nabla_{a}W\big) -\frac{3i}{16}W^{-4}(\Gamma{}^{a}){}^{\beta \gamma}\nabla_{\eta}^{r}\big(X{}^{k i}\big)\lambda{}_{\beta}{}^{j}\lambda{}_{\gamma k}\big(\nabla_{a}W\big)\\
&-\frac{3i}{16}W^{-4}(\Gamma{}^{a}){}^{\beta \gamma}X{}^{k i}\nabla_{\eta}^{r}\big(\lambda{}_{\beta}{}^{j}\big)\lambda{}_{\gamma k}\big(\nabla_{a}W\big) +\frac{3i}{16}W^{-4}(\Gamma{}^{a}){}^{\beta \gamma}X{}^{k i}\lambda{}_{\beta}{}^{j}\nabla_{\eta}^{r}\big(\lambda{}_{\gamma k}\big)\big(\nabla_{a}W\big)\\
&-\frac{3i}{16}W^{-4}(\Gamma{}^{a}){}^{\beta \gamma}X{}^{k i}\lambda{}_{\beta}{}^{j}\lambda{}_{\gamma k}\nabla_{\eta}^{r}\big(\nabla_{a}W\big) -\frac{3i}{16}\nabla_{\eta}^{r}\big(W^{-4}\big)(\Gamma{}^{a}){}^{\beta \gamma}X{}^{k j}\lambda{}_{\beta}{}^{i}\lambda{}_{\gamma k}\big(\nabla_{a}W\big)\\
&-\frac{3i}{16}W^{-4}(\Gamma{}^{a}){}^{\beta \gamma}\nabla_{\eta}^{r}\big(X{}^{k j}\big)\lambda{}_{\beta}{}^{i}\lambda{}_{\gamma k}\big(\nabla_{a}W\big) -\frac{3i}{16}W^{-4}(\Gamma{}^{a}){}^{\beta \gamma}X{}^{k j}\nabla_{\eta}^{r}\big(\lambda{}_{\beta}{}^{i}\big)\lambda{}_{\gamma k}\big(\nabla_{a}W\big)\\
&+\frac{3i}{16}W^{-4}(\Gamma{}^{a}){}^{\beta \gamma}X{}^{k j}\lambda{}_{\beta}{}^{i}\nabla_{\eta}^{r}\big(\lambda{}_{\gamma k}\big)\big(\nabla_{a}W\big) -\frac{3i}{16}W^{-4}(\Gamma{}^{a}){}^{\beta \gamma}X{}^{k j}\lambda{}_{\beta}{}^{i}\lambda{}_{\gamma k}\nabla_{\eta}^{r}\big(\nabla_{a}W\big)
\end{aligned}
\tag{S3-H4.2-a}
```

Insert the elementary source identities and the applicable commutators (S3-11)–(S3-14), distribute the vector product rules, and contract only index-raising metrics. The resulting contribution is

```math
\begin{aligned}
\left.\nabla_\eta^rH^{ij}\right|_{\mathrm{H4.2}}=&-\frac{3}{4}W^{-5}\lambda{}_{\eta}{}^{r}(\Gamma{}^{a}){}^{\beta \gamma}X{}^{k i}\lambda{}_{\beta}{}^{j}\lambda{}_{\gamma k}\big(\nabla_{a}W\big) +\frac{3}{16}W^{-4}(\Gamma{}^{a}){}^{\beta \gamma}(\Gamma{}^{b}){}_{\eta}{}^{\delta}\big(\nabla_{b}\lambda{}_{\delta}{}^{i}\big)\lambda{}_{\beta}{}^{j}\lambda{}_{\gamma}{}^{r}\big(\nabla_{a}W\big)\\
&-\frac{3}{32}W^{-4}(\Gamma{}^{a}){}^{\beta \gamma}W{}_{\eta \delta}\lambda{}^{\delta i}\lambda{}_{\beta}{}^{j}\lambda{}_{\gamma}{}^{r}\big(\nabla_{a}W\big) +\frac{9i}{64}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}X{}_{\eta}{}^{i}\lambda{}_{\beta}{}^{j}\lambda{}_{\gamma}{}^{r}\big(\nabla_{a}W\big)\\
&+\frac{3}{16}W^{-4}(\Gamma{}^{a}){}^{\beta \gamma}\varepsilon{}^{r i}(\Gamma{}^{b}){}_{\eta}{}^{\delta}\big(\nabla_{b}\lambda{}_{\delta}{}^{k}\big)\lambda{}_{\beta}{}^{j}\lambda{}_{\gamma k}\big(\nabla_{a}W\big) -\frac{3}{32}W^{-4}(\Gamma{}^{a}){}^{\beta \gamma}\varepsilon{}^{r i}W{}_{\eta \delta}\lambda{}^{\delta k}\lambda{}_{\beta}{}^{j}\lambda{}_{\gamma k}\big(\nabla_{a}W\big)\\
&+\frac{9i}{64}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}\varepsilon{}^{r i}X{}_{\eta}{}^{k}\lambda{}_{\beta}{}^{j}\lambda{}_{\gamma k}\big(\nabla_{a}W\big) +\frac{3i}{8}W^{-4}(\Gamma{}^{a}){}^{\beta \gamma}X{}^{k i}\varepsilon{}^{r j}F{}_{\eta \beta}\lambda{}_{\gamma k}\big(\nabla_{a}W\big)\\
&+\frac{3i}{8}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}X{}^{k i}\varepsilon{}^{r j}W{}_{\eta \beta}\lambda{}_{\gamma k}\big(\nabla_{a}W\big) +\frac{3i}{16}W^{-4}(\Gamma{}^{a}){}_{\eta}{}^{\beta}X{}^{k i}X{}^{r j}\lambda{}_{\beta k}\big(\nabla_{a}W\big)\\
&+\frac{3i}{16}W^{-4}(\Gamma{}^{a}){}^{\beta \gamma}X{}^{k i}\varepsilon{}^{r j}(\Gamma{}^{b}){}_{\eta \beta}\big(\nabla_{b}W\big)\lambda{}_{\gamma k}\big(\nabla_{a}W\big) +\frac{3i}{8}W^{-4}(\Gamma{}^{a}){}^{\beta \gamma}X{}^{r i}\lambda{}_{\beta}{}^{j}F{}_{\eta \gamma}\big(\nabla_{a}W\big)\\
&+\frac{3i}{8}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}X{}^{r i}\lambda{}_{\beta}{}^{j}W{}_{\eta \gamma}\big(\nabla_{a}W\big) -\frac{3i}{16}W^{-4}(\Gamma{}^{a}){}^{\beta}{}_{\eta}X{}^{k i}\lambda{}_{\beta}{}^{j}X{}^{r}{}_{k}\big(\nabla_{a}W\big)\\
&+\frac{3i}{16}W^{-4}(\Gamma{}^{a}){}^{\beta \gamma}X{}^{r i}\lambda{}_{\beta}{}^{j}(\Gamma{}^{b}){}_{\eta \gamma}\big(\nabla_{b}W\big)\big(\nabla_{a}W\big) +\frac{3}{16}W^{-4}(\Gamma{}^{a}){}^{\beta \gamma}X{}^{k i}\lambda{}_{\beta}{}^{j}\lambda{}_{\gamma k}\big(\nabla_{a}\lambda{}_{\eta}{}^{r}\big)\\
&+\frac{3}{16}W^{-4}(\Gamma{}^{a}){}^{\beta \gamma}X{}^{k i}\lambda{}_{\beta}{}^{j}\lambda{}_{\gamma k}\mathcal T{}_{a \eta}{}^{\delta}\lambda{}_{\delta}{}^{r} -\frac{3i}{16}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}X{}^{k i}\lambda{}_{\beta}{}^{j}\lambda{}_{\gamma k}\mathcal R(\mathbb D){}_{a \eta}{}^{r}\\
&-\frac{3}{4}W^{-5}\lambda{}_{\eta}{}^{r}(\Gamma{}^{a}){}^{\beta \gamma}X{}^{k j}\lambda{}_{\beta}{}^{i}\lambda{}_{\gamma k}\big(\nabla_{a}W\big) +\frac{3}{16}W^{-4}(\Gamma{}^{a}){}^{\beta \gamma}(\Gamma{}^{b}){}_{\eta}{}^{\delta}\big(\nabla_{b}\lambda{}_{\delta}{}^{j}\big)\lambda{}_{\beta}{}^{i}\lambda{}_{\gamma}{}^{r}\big(\nabla_{a}W\big)\\
&-\frac{3}{32}W^{-4}(\Gamma{}^{a}){}^{\beta \gamma}W{}_{\eta \delta}\lambda{}^{\delta j}\lambda{}_{\beta}{}^{i}\lambda{}_{\gamma}{}^{r}\big(\nabla_{a}W\big) +\frac{9i}{64}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}X{}_{\eta}{}^{j}\lambda{}_{\beta}{}^{i}\lambda{}_{\gamma}{}^{r}\big(\nabla_{a}W\big)\\
&+\frac{3}{16}W^{-4}(\Gamma{}^{a}){}^{\beta \gamma}\varepsilon{}^{r j}(\Gamma{}^{b}){}_{\eta}{}^{\delta}\big(\nabla_{b}\lambda{}_{\delta}{}^{k}\big)\lambda{}_{\beta}{}^{i}\lambda{}_{\gamma k}\big(\nabla_{a}W\big) -\frac{3}{32}W^{-4}(\Gamma{}^{a}){}^{\beta \gamma}\varepsilon{}^{r j}W{}_{\eta \delta}\lambda{}^{\delta k}\lambda{}_{\beta}{}^{i}\lambda{}_{\gamma k}\big(\nabla_{a}W\big)\\
&+\frac{9i}{64}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}\varepsilon{}^{r j}X{}_{\eta}{}^{k}\lambda{}_{\beta}{}^{i}\lambda{}_{\gamma k}\big(\nabla_{a}W\big) +\frac{3i}{8}W^{-4}(\Gamma{}^{a}){}^{\beta \gamma}X{}^{k j}\varepsilon{}^{r i}F{}_{\eta \beta}\lambda{}_{\gamma k}\big(\nabla_{a}W\big)\\
&+\frac{3i}{8}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}X{}^{k j}\varepsilon{}^{r i}W{}_{\eta \beta}\lambda{}_{\gamma k}\big(\nabla_{a}W\big) +\frac{3i}{16}W^{-4}(\Gamma{}^{a}){}_{\eta}{}^{\beta}X{}^{k j}X{}^{r i}\lambda{}_{\beta k}\big(\nabla_{a}W\big)\\
&+\frac{3i}{16}W^{-4}(\Gamma{}^{a}){}^{\beta \gamma}X{}^{k j}\varepsilon{}^{r i}(\Gamma{}^{b}){}_{\eta \beta}\big(\nabla_{b}W\big)\lambda{}_{\gamma k}\big(\nabla_{a}W\big) +\frac{3i}{8}W^{-4}(\Gamma{}^{a}){}^{\beta \gamma}X{}^{r j}\lambda{}_{\beta}{}^{i}F{}_{\eta \gamma}\big(\nabla_{a}W\big)\\
&+\frac{3i}{8}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}X{}^{r j}\lambda{}_{\beta}{}^{i}W{}_{\eta \gamma}\big(\nabla_{a}W\big) -\frac{3i}{16}W^{-4}(\Gamma{}^{a}){}^{\beta}{}_{\eta}X{}^{k j}\lambda{}_{\beta}{}^{i}X{}^{r}{}_{k}\big(\nabla_{a}W\big)\\
&+\frac{3i}{16}W^{-4}(\Gamma{}^{a}){}^{\beta \gamma}X{}^{r j}\lambda{}_{\beta}{}^{i}(\Gamma{}^{b}){}_{\eta \gamma}\big(\nabla_{b}W\big)\big(\nabla_{a}W\big) +\frac{3}{16}W^{-4}(\Gamma{}^{a}){}^{\beta \gamma}X{}^{k j}\lambda{}_{\beta}{}^{i}\lambda{}_{\gamma k}\big(\nabla_{a}\lambda{}_{\eta}{}^{r}\big)\\
&+\frac{3}{16}W^{-4}(\Gamma{}^{a}){}^{\beta \gamma}X{}^{k j}\lambda{}_{\beta}{}^{i}\lambda{}_{\gamma k}\mathcal T{}_{a \eta}{}^{\delta}\lambda{}_{\delta}{}^{r} -\frac{3i}{16}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}X{}^{k j}\lambda{}_{\beta}{}^{i}\lambda{}_{\gamma k}\mathcal R(\mathbb D){}_{a \eta}{}^{r}
\end{aligned}
\tag{S3-H4.2-b}
```

**Check for H4.2:** all 36 written summands have weight $`7/2`$, odd parity and the same free indices $`\eta;r,i,j`$. Dummy labels are paired. The coefficient $`1/3`$ and the two external epsilons are applied once, when collecting the spinor.

#### Input H4.3

The calculated input is

```math
\left.H^{ij}\right|_{\mathrm{H4.3}}=W^{-4}\big(\frac{3i}{8}(\Gamma^a)^{\alpha\beta}F_{ab}\lambda_\alpha^i\lambda_\beta^j\nabla^bW\big).
\tag{S3-H4.3-input}
```

Expand each written SU(2) average with weight $`1/2`$ before applying the left derivative.

Apply the product rule (S3-09), in the displayed factor order:

```math
\begin{aligned}
\left.\nabla_\eta^rH^{ij}\right|_{\mathrm{H4.3}}=&\frac{3i}{8}\nabla_{\eta}^{r}\big(W^{-4}\big)(\Gamma{}^{a}){}^{\beta \gamma}F{}_{a b}\lambda{}_{\beta}{}^{i}\lambda{}_{\gamma}{}^{j}\big(\nabla^{b}W\big) +\frac{3i}{8}W^{-4}(\Gamma{}^{a}){}^{\beta \gamma}\nabla_{\eta}^{r}\big(F{}_{a b}\big)\lambda{}_{\beta}{}^{i}\lambda{}_{\gamma}{}^{j}\big(\nabla^{b}W\big)\\
&+\frac{3i}{8}W^{-4}(\Gamma{}^{a}){}^{\beta \gamma}F{}_{a b}\nabla_{\eta}^{r}\big(\lambda{}_{\beta}{}^{i}\big)\lambda{}_{\gamma}{}^{j}\big(\nabla^{b}W\big) -\frac{3i}{8}W^{-4}(\Gamma{}^{a}){}^{\beta \gamma}F{}_{a b}\lambda{}_{\beta}{}^{i}\nabla_{\eta}^{r}\big(\lambda{}_{\gamma}{}^{j}\big)\big(\nabla^{b}W\big)\\
&+\frac{3i}{8}W^{-4}(\Gamma{}^{a}){}^{\beta \gamma}F{}_{a b}\lambda{}_{\beta}{}^{i}\lambda{}_{\gamma}{}^{j}\nabla_{\eta}^{r}\big(\nabla^{b}W\big)
\end{aligned}
\tag{S3-H4.3-a}
```

Insert the elementary source identities and the applicable commutators (S3-11)–(S3-14), distribute the vector product rules, and contract only index-raising metrics. The resulting contribution is

```math
\begin{aligned}
\left.\nabla_\eta^rH^{ij}\right|_{\mathrm{H4.3}}=&\frac{3}{2}W^{-5}\lambda{}_{\eta}{}^{r}(\Gamma{}^{a}){}^{\beta \gamma}F{}_{a b}\lambda{}_{\beta}{}^{i}\lambda{}_{\gamma}{}^{j}\big(\nabla^{b}W\big) +\frac{3}{16}W^{-4}(\Gamma{}^{a}){}^{\beta \gamma}(\Sigma{}_{a b}){}^{\delta \rho}(\Gamma{}^{c}){}_{\eta \delta}\big(\nabla_{c}\lambda{}_{\rho}{}^{r}\big)\lambda{}_{\beta}{}^{i}\lambda{}_{\gamma}{}^{j}\big(\nabla^{b}W\big)\\
&+\frac{3}{16}W^{-4}(\Gamma{}^{a}){}^{\beta \gamma}(\Sigma{}_{a b}){}_{\eta}{}^{\delta}(\Gamma{}^{c}){}_{\delta}{}^{\rho}\big(\nabla_{c}\lambda{}_{\rho}{}^{r}\big)\lambda{}_{\beta}{}^{i}\lambda{}_{\gamma}{}^{j}\big(\nabla^{b}W\big) -\frac{3}{32}W^{-4}(\Gamma{}^{a}){}^{\beta \gamma}(\Sigma{}_{a b}){}^{\delta \rho}W{}_{\eta \delta}\lambda{}_{\rho}{}^{r}\lambda{}_{\beta}{}^{i}\lambda{}_{\gamma}{}^{j}\big(\nabla^{b}W\big)\\
&+\frac{9}{32}W^{-4}(\Gamma{}^{a}){}^{\beta \gamma}(\Sigma{}_{a b}){}_{\eta}{}^{\delta}W{}_{\delta}{}^{\rho}\lambda{}_{\rho}{}^{r}\lambda{}_{\beta}{}^{i}\lambda{}_{\gamma}{}^{j}\big(\nabla^{b}W\big) +\frac{3}{16}W^{-4}(\Gamma{}^{a}){}^{\beta \gamma}(\Sigma{}_{a b}){}^{\delta \rho}(\Gamma{}^{c}){}_{\eta \rho}\big(\nabla_{c}\lambda{}_{\delta}{}^{r}\big)\lambda{}_{\beta}{}^{i}\lambda{}_{\gamma}{}^{j}\big(\nabla^{b}W\big)\\
&+\frac{3}{16}W^{-4}(\Gamma{}^{a}){}^{\beta \gamma}(\Sigma{}_{a b}){}^{\delta}{}_{\eta}(\Gamma{}^{c}){}_{\delta}{}^{\rho}\big(\nabla_{c}\lambda{}_{\rho}{}^{r}\big)\lambda{}_{\beta}{}^{i}\lambda{}_{\gamma}{}^{j}\big(\nabla^{b}W\big) -\frac{3}{32}W^{-4}(\Gamma{}^{a}){}^{\beta \gamma}(\Sigma{}_{a b}){}^{\delta \rho}W{}_{\eta \rho}\lambda{}_{\delta}{}^{r}\lambda{}_{\beta}{}^{i}\lambda{}_{\gamma}{}^{j}\big(\nabla^{b}W\big)\\
&+\frac{9}{32}W^{-4}(\Gamma{}^{a}){}^{\beta \gamma}(\Sigma{}_{a b}){}^{\delta}{}_{\eta}W{}_{\delta}{}^{\rho}\lambda{}_{\rho}{}^{r}\lambda{}_{\beta}{}^{i}\lambda{}_{\gamma}{}^{j}\big(\nabla^{b}W\big) +\frac{9}{16}W^{-4}(\Gamma{}^{a}){}^{\beta \gamma}(\Sigma{}_{a b}){}^{\delta \rho}W{}_{\delta \rho}\lambda{}_{\eta}{}^{r}\lambda{}_{\beta}{}^{i}\lambda{}_{\gamma}{}^{j}\big(\nabla^{b}W\big)\\
&-\frac{3i}{8}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}(\Sigma{}_{a b}){}^{\delta \rho}W{}_{\eta \delta \rho}{}^{r}\lambda{}_{\beta}{}^{i}\lambda{}_{\gamma}{}^{j}\big(\nabla^{b}W\big) -\frac{3i}{4}W^{-4}(\Gamma{}^{a}){}^{\beta \gamma}F{}_{a b}\varepsilon{}^{r i}F{}_{\eta \beta}\lambda{}_{\gamma}{}^{j}\big(\nabla^{b}W\big)\\
&-\frac{3i}{4}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}F{}_{a b}\varepsilon{}^{r i}W{}_{\eta \beta}\lambda{}_{\gamma}{}^{j}\big(\nabla^{b}W\big) -\frac{3i}{8}W^{-4}(\Gamma{}^{a}){}_{\eta}{}^{\beta}F{}_{a b}X{}^{r i}\lambda{}_{\beta}{}^{j}\big(\nabla^{b}W\big)\\
&-\frac{3i}{8}W^{-4}(\Gamma{}^{a}){}^{\beta \gamma}F{}_{a b}\varepsilon{}^{r i}(\Gamma{}^{c}){}_{\eta \beta}\big(\nabla_{c}W\big)\lambda{}_{\gamma}{}^{j}\big(\nabla^{b}W\big) +\frac{3i}{4}W^{-4}(\Gamma{}^{a}){}^{\beta \gamma}F{}_{a b}\lambda{}_{\beta}{}^{i}\varepsilon{}^{r j}F{}_{\eta \gamma}\big(\nabla^{b}W\big)\\
&+\frac{3i}{4}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}F{}_{a b}\lambda{}_{\beta}{}^{i}\varepsilon{}^{r j}W{}_{\eta \gamma}\big(\nabla^{b}W\big) +\frac{3i}{8}W^{-4}(\Gamma{}^{a}){}^{\beta}{}_{\eta}F{}_{a b}\lambda{}_{\beta}{}^{i}X{}^{r j}\big(\nabla^{b}W\big)\\
&+\frac{3i}{8}W^{-4}(\Gamma{}^{a}){}^{\beta \gamma}F{}_{a b}\lambda{}_{\beta}{}^{i}\varepsilon{}^{r j}(\Gamma{}^{c}){}_{\eta \gamma}\big(\nabla_{c}W\big)\big(\nabla^{b}W\big) -\frac{3}{8}W^{-4}(\Gamma{}^{a}){}^{\beta \gamma}F{}_{a b}\lambda{}_{\beta}{}^{i}\lambda{}_{\gamma}{}^{j}\big(\nabla^{b}\lambda{}_{\eta}{}^{r}\big)\\
&-\frac{3}{8}W^{-4}(\Gamma{}^{a}){}^{\beta \gamma}F{}_{a b}\lambda{}_{\beta}{}^{i}\lambda{}_{\gamma}{}^{j}\mathcal T{}^{b}{}_{\eta}{}^{\delta}\lambda{}_{\delta}{}^{r} +\frac{3i}{8}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}F{}_{a b}\lambda{}_{\beta}{}^{i}\lambda{}_{\gamma}{}^{j}\mathcal R(\mathbb D){}^{b}{}_{\eta}{}^{r}
\end{aligned}
\tag{S3-H4.3-b}
```

**Check for H4.3:** all 22 written summands have weight $`7/2`$, odd parity and the same free indices $`\eta;r,i,j`$. Dummy labels are paired. The coefficient $`1/3`$ and the two external epsilons are applied once, when collecting the spinor.

#### Input H4.4

The calculated input is

```math
\left.H^{ij}\right|_{\mathrm{H4.4}}=W^{-4}\big(\frac{3i}{32}F^{ab}F_{ab}\lambda^{\alpha i}\lambda_\alpha^j\big).
\tag{S3-H4.4-input}
```

Apply the product rule (S3-09), in the displayed factor order:

```math
\begin{aligned}
\left.\nabla_\eta^rH^{ij}\right|_{\mathrm{H4.4}}=&\frac{3i}{32}\nabla_{\eta}^{r}\big(W^{-4}\big)F{}^{a b}F{}_{a b}\lambda{}^{\beta i}\lambda{}_{\beta}{}^{j} +\frac{3i}{32}W^{-4}\nabla_{\eta}^{r}\big(F{}^{a b}\big)F{}_{a b}\lambda{}^{\beta i}\lambda{}_{\beta}{}^{j}\\
&+\frac{3i}{32}W^{-4}F{}^{a b}\nabla_{\eta}^{r}\big(F{}_{a b}\big)\lambda{}^{\beta i}\lambda{}_{\beta}{}^{j} +\frac{3i}{32}W^{-4}F{}^{a b}F{}_{a b}\nabla_{\eta}^{r}\big(\lambda{}^{\beta i}\big)\lambda{}_{\beta}{}^{j}\\
&-\frac{3i}{32}W^{-4}F{}^{a b}F{}_{a b}\lambda{}^{\beta i}\nabla_{\eta}^{r}\big(\lambda{}_{\beta}{}^{j}\big)
\end{aligned}
\tag{S3-H4.4-a}
```

Insert the elementary source identities and the applicable commutators (S3-11)–(S3-14), distribute the vector product rules, and contract only index-raising metrics. The resulting contribution is

```math
\begin{aligned}
\left.\nabla_\eta^rH^{ij}\right|_{\mathrm{H4.4}}=&\frac{3}{8}W^{-5}\lambda{}_{\eta}{}^{r}F{}^{a b}F{}_{a b}\lambda{}^{\beta i}\lambda{}_{\beta}{}^{j} +\frac{3}{64}W^{-4}(\Sigma{}^{a b}){}^{\beta \gamma}(\Gamma{}^{c}){}_{\eta \beta}\big(\nabla_{c}\lambda{}_{\gamma}{}^{r}\big)F{}_{a b}\lambda{}^{\delta i}\lambda{}_{\delta}{}^{j}\\
&+\frac{3}{64}W^{-4}(\Sigma{}^{a b}){}_{\eta}{}^{\beta}(\Gamma{}^{c}){}_{\beta}{}^{\gamma}\big(\nabla_{c}\lambda{}_{\gamma}{}^{r}\big)F{}_{a b}\lambda{}^{\delta i}\lambda{}_{\delta}{}^{j} -\frac{3}{128}W^{-4}(\Sigma{}^{a b}){}^{\beta \gamma}W{}_{\eta \beta}\lambda{}_{\gamma}{}^{r}F{}_{a b}\lambda{}^{\delta i}\lambda{}_{\delta}{}^{j}\\
&+\frac{9}{128}W^{-4}(\Sigma{}^{a b}){}_{\eta}{}^{\beta}W{}_{\beta}{}^{\gamma}\lambda{}_{\gamma}{}^{r}F{}_{a b}\lambda{}^{\delta i}\lambda{}_{\delta}{}^{j} +\frac{3}{64}W^{-4}(\Sigma{}^{a b}){}^{\beta \gamma}(\Gamma{}^{c}){}_{\eta \gamma}\big(\nabla_{c}\lambda{}_{\beta}{}^{r}\big)F{}_{a b}\lambda{}^{\delta i}\lambda{}_{\delta}{}^{j}\\
&+\frac{3}{64}W^{-4}(\Sigma{}^{a b}){}^{\beta}{}_{\eta}(\Gamma{}^{c}){}_{\beta}{}^{\gamma}\big(\nabla_{c}\lambda{}_{\gamma}{}^{r}\big)F{}_{a b}\lambda{}^{\delta i}\lambda{}_{\delta}{}^{j} -\frac{3}{128}W^{-4}(\Sigma{}^{a b}){}^{\beta \gamma}W{}_{\eta \gamma}\lambda{}_{\beta}{}^{r}F{}_{a b}\lambda{}^{\delta i}\lambda{}_{\delta}{}^{j}\\
&+\frac{9}{128}W^{-4}(\Sigma{}^{a b}){}^{\beta}{}_{\eta}W{}_{\beta}{}^{\gamma}\lambda{}_{\gamma}{}^{r}F{}_{a b}\lambda{}^{\delta i}\lambda{}_{\delta}{}^{j} +\frac{9}{64}W^{-4}(\Sigma{}^{a b}){}^{\beta \gamma}W{}_{\beta \gamma}\lambda{}_{\eta}{}^{r}F{}_{a b}\lambda{}^{\delta i}\lambda{}_{\delta}{}^{j}\\
&-\frac{3i}{32}W^{-3}(\Sigma{}^{a b}){}^{\beta \gamma}W{}_{\eta \beta \gamma}{}^{r}F{}_{a b}\lambda{}^{\delta i}\lambda{}_{\delta}{}^{j} +\frac{3}{64}W^{-4}F{}^{a b}(\Sigma{}_{a b}){}^{\beta \gamma}(\Gamma{}^{c}){}_{\eta \beta}\big(\nabla_{c}\lambda{}_{\gamma}{}^{r}\big)\lambda{}^{\delta i}\lambda{}_{\delta}{}^{j}\\
&+\frac{3}{64}W^{-4}F{}^{a b}(\Sigma{}_{a b}){}_{\eta}{}^{\beta}(\Gamma{}^{c}){}_{\beta}{}^{\gamma}\big(\nabla_{c}\lambda{}_{\gamma}{}^{r}\big)\lambda{}^{\delta i}\lambda{}_{\delta}{}^{j} -\frac{3}{128}W^{-4}F{}^{a b}(\Sigma{}_{a b}){}^{\beta \gamma}W{}_{\eta \beta}\lambda{}_{\gamma}{}^{r}\lambda{}^{\delta i}\lambda{}_{\delta}{}^{j}\\
&+\frac{9}{128}W^{-4}F{}^{a b}(\Sigma{}_{a b}){}_{\eta}{}^{\beta}W{}_{\beta}{}^{\gamma}\lambda{}_{\gamma}{}^{r}\lambda{}^{\delta i}\lambda{}_{\delta}{}^{j} +\frac{3}{64}W^{-4}F{}^{a b}(\Sigma{}_{a b}){}^{\beta \gamma}(\Gamma{}^{c}){}_{\eta \gamma}\big(\nabla_{c}\lambda{}_{\beta}{}^{r}\big)\lambda{}^{\delta i}\lambda{}_{\delta}{}^{j}\\
&+\frac{3}{64}W^{-4}F{}^{a b}(\Sigma{}_{a b}){}^{\beta}{}_{\eta}(\Gamma{}^{c}){}_{\beta}{}^{\gamma}\big(\nabla_{c}\lambda{}_{\gamma}{}^{r}\big)\lambda{}^{\delta i}\lambda{}_{\delta}{}^{j} -\frac{3}{128}W^{-4}F{}^{a b}(\Sigma{}_{a b}){}^{\beta \gamma}W{}_{\eta \gamma}\lambda{}_{\beta}{}^{r}\lambda{}^{\delta i}\lambda{}_{\delta}{}^{j}\\
&+\frac{9}{128}W^{-4}F{}^{a b}(\Sigma{}_{a b}){}^{\beta}{}_{\eta}W{}_{\beta}{}^{\gamma}\lambda{}_{\gamma}{}^{r}\lambda{}^{\delta i}\lambda{}_{\delta}{}^{j} +\frac{9}{64}W^{-4}F{}^{a b}(\Sigma{}_{a b}){}^{\beta \gamma}W{}_{\beta \gamma}\lambda{}_{\eta}{}^{r}\lambda{}^{\delta i}\lambda{}_{\delta}{}^{j}\\
&-\frac{3i}{32}W^{-3}F{}^{a b}(\Sigma{}_{a b}){}^{\beta \gamma}W{}_{\eta \beta \gamma}{}^{r}\lambda{}^{\delta i}\lambda{}_{\delta}{}^{j} -\frac{3i}{16}W^{-4}F{}^{a b}F{}_{a b}\varepsilon{}^{r i}F{}_{\eta}{}^{\beta}\lambda{}_{\beta}{}^{j}\\
&-\frac{3i}{16}W^{-3}F{}^{a b}F{}_{a b}\varepsilon{}^{r i}W{}_{\eta}{}^{\beta}\lambda{}_{\beta}{}^{j} +\frac{3i}{32}W^{-4}F{}^{a b}F{}_{a b}X{}^{r i}\lambda{}_{\eta}{}^{j}\\
&-\frac{3i}{32}W^{-4}F{}^{a b}F{}_{a b}\varepsilon{}^{r i}(\Gamma{}^{c}){}_{\eta}{}^{\beta}\big(\nabla_{c}W\big)\lambda{}_{\beta}{}^{j} +\frac{3i}{16}W^{-4}F{}^{a b}F{}_{a b}\lambda{}^{\beta i}\varepsilon{}^{r j}F{}_{\eta \beta}\\
&+\frac{3i}{16}W^{-3}F{}^{a b}F{}_{a b}\lambda{}^{\beta i}\varepsilon{}^{r j}W{}_{\eta \beta} +\frac{3i}{32}W^{-4}F{}^{a b}F{}_{a b}\lambda{}_{\eta}{}^{i}X{}^{r j}\\
&+\frac{3i}{32}W^{-4}F{}^{a b}F{}_{a b}\lambda{}^{\beta i}\varepsilon{}^{r j}(\Gamma{}^{c}){}_{\eta \beta}\big(\nabla_{c}W\big)
\end{aligned}
\tag{S3-H4.4-b}
```

**Check for H4.4:** all 29 written summands have weight $`7/2`$, odd parity and the same free indices $`\eta;r,i,j`$. Dummy labels are paired. The coefficient $`1/3`$ and the two external epsilons are applied once, when collecting the spinor.

#### Input H4.5

The calculated input is

```math
\left.H^{ij}\right|_{\mathrm{H4.5}}=W^{-4}\big(\frac{3i}{64}\varepsilon^{abcde}(\Gamma_a)^{\alpha\beta}F_{bc}F_{de}\lambda_\alpha^i\lambda_\beta^j\big).
\tag{S3-H4.5-input}
```

Expand each written SU(2) average with weight $`1/2`$ before applying the left derivative.

Apply the product rule (S3-09), in the displayed factor order:

```math
\begin{aligned}
\left.\nabla_\eta^rH^{ij}\right|_{\mathrm{H4.5}}=&\frac{3i}{64}\nabla_{\eta}^{r}\big(W^{-4}\big)\varepsilon{}^{a b c d e}(\Gamma{}_{a}){}^{\beta \gamma}F{}_{b c}F{}_{d e}\lambda{}_{\beta}{}^{i}\lambda{}_{\gamma}{}^{j} +\frac{3i}{64}W^{-4}\varepsilon{}^{a b c d e}(\Gamma{}_{a}){}^{\beta \gamma}\nabla_{\eta}^{r}\big(F{}_{b c}\big)F{}_{d e}\lambda{}_{\beta}{}^{i}\lambda{}_{\gamma}{}^{j}\\
&+\frac{3i}{64}W^{-4}\varepsilon{}^{a b c d e}(\Gamma{}_{a}){}^{\beta \gamma}F{}_{b c}\nabla_{\eta}^{r}\big(F{}_{d e}\big)\lambda{}_{\beta}{}^{i}\lambda{}_{\gamma}{}^{j} +\frac{3i}{64}W^{-4}\varepsilon{}^{a b c d e}(\Gamma{}_{a}){}^{\beta \gamma}F{}_{b c}F{}_{d e}\nabla_{\eta}^{r}\big(\lambda{}_{\beta}{}^{i}\big)\lambda{}_{\gamma}{}^{j}\\
&-\frac{3i}{64}W^{-4}\varepsilon{}^{a b c d e}(\Gamma{}_{a}){}^{\beta \gamma}F{}_{b c}F{}_{d e}\lambda{}_{\beta}{}^{i}\nabla_{\eta}^{r}\big(\lambda{}_{\gamma}{}^{j}\big)
\end{aligned}
\tag{S3-H4.5-a}
```

Insert the elementary source identities and the applicable commutators (S3-11)–(S3-14), distribute the vector product rules, and contract only index-raising metrics. The resulting contribution is

```math
\begin{aligned}
\left.\nabla_\eta^rH^{ij}\right|_{\mathrm{H4.5}}=&\frac{3}{16}W^{-5}\lambda{}_{\eta}{}^{r}\varepsilon{}^{a b c d e}(\Gamma{}_{a}){}^{\beta \gamma}F{}_{b c}F{}_{d e}\lambda{}_{\beta}{}^{i}\lambda{}_{\gamma}{}^{j} +\frac{3}{128}W^{-4}\varepsilon{}^{a b c d e}(\Gamma{}_{a}){}^{\beta \gamma}(\Sigma{}_{b c}){}^{\delta \rho}(\Gamma{}^{f}){}_{\eta \delta}\big(\nabla_{f}\lambda{}_{\rho}{}^{r}\big)F{}_{d e}\lambda{}_{\beta}{}^{i}\lambda{}_{\gamma}{}^{j}\\
&+\frac{3}{128}W^{-4}\varepsilon{}^{a b c d e}(\Gamma{}_{a}){}^{\beta \gamma}(\Sigma{}_{b c}){}_{\eta}{}^{\delta}(\Gamma{}^{f}){}_{\delta}{}^{\rho}\big(\nabla_{f}\lambda{}_{\rho}{}^{r}\big)F{}_{d e}\lambda{}_{\beta}{}^{i}\lambda{}_{\gamma}{}^{j} -\frac{3}{256}W^{-4}\varepsilon{}^{a b c d e}(\Gamma{}_{a}){}^{\beta \gamma}(\Sigma{}_{b c}){}^{\delta \rho}W{}_{\eta \delta}\lambda{}_{\rho}{}^{r}F{}_{d e}\lambda{}_{\beta}{}^{i}\lambda{}_{\gamma}{}^{j}\\
&+\frac{9}{256}W^{-4}\varepsilon{}^{a b c d e}(\Gamma{}_{a}){}^{\beta \gamma}(\Sigma{}_{b c}){}_{\eta}{}^{\delta}W{}_{\delta}{}^{\rho}\lambda{}_{\rho}{}^{r}F{}_{d e}\lambda{}_{\beta}{}^{i}\lambda{}_{\gamma}{}^{j} +\frac{3}{128}W^{-4}\varepsilon{}^{a b c d e}(\Gamma{}_{a}){}^{\beta \gamma}(\Sigma{}_{b c}){}^{\delta \rho}(\Gamma{}^{f}){}_{\eta \rho}\big(\nabla_{f}\lambda{}_{\delta}{}^{r}\big)F{}_{d e}\lambda{}_{\beta}{}^{i}\lambda{}_{\gamma}{}^{j}\\
&+\frac{3}{128}W^{-4}\varepsilon{}^{a b c d e}(\Gamma{}_{a}){}^{\beta \gamma}(\Sigma{}_{b c}){}^{\delta}{}_{\eta}(\Gamma{}^{f}){}_{\delta}{}^{\rho}\big(\nabla_{f}\lambda{}_{\rho}{}^{r}\big)F{}_{d e}\lambda{}_{\beta}{}^{i}\lambda{}_{\gamma}{}^{j} -\frac{3}{256}W^{-4}\varepsilon{}^{a b c d e}(\Gamma{}_{a}){}^{\beta \gamma}(\Sigma{}_{b c}){}^{\delta \rho}W{}_{\eta \rho}\lambda{}_{\delta}{}^{r}F{}_{d e}\lambda{}_{\beta}{}^{i}\lambda{}_{\gamma}{}^{j}\\
&+\frac{9}{256}W^{-4}\varepsilon{}^{a b c d e}(\Gamma{}_{a}){}^{\beta \gamma}(\Sigma{}_{b c}){}^{\delta}{}_{\eta}W{}_{\delta}{}^{\rho}\lambda{}_{\rho}{}^{r}F{}_{d e}\lambda{}_{\beta}{}^{i}\lambda{}_{\gamma}{}^{j} +\frac{9}{128}W^{-4}\varepsilon{}^{a b c d e}(\Gamma{}_{a}){}^{\beta \gamma}(\Sigma{}_{b c}){}^{\delta \rho}W{}_{\delta \rho}\lambda{}_{\eta}{}^{r}F{}_{d e}\lambda{}_{\beta}{}^{i}\lambda{}_{\gamma}{}^{j}\\
&-\frac{3i}{64}W^{-3}\varepsilon{}^{a b c d e}(\Gamma{}_{a}){}^{\beta \gamma}(\Sigma{}_{b c}){}^{\delta \rho}W{}_{\eta \delta \rho}{}^{r}F{}_{d e}\lambda{}_{\beta}{}^{i}\lambda{}_{\gamma}{}^{j} +\frac{3}{128}W^{-4}\varepsilon{}^{a b c d e}(\Gamma{}_{a}){}^{\beta \gamma}F{}_{b c}(\Sigma{}_{d e}){}^{\delta \rho}(\Gamma{}^{f}){}_{\eta \delta}\big(\nabla_{f}\lambda{}_{\rho}{}^{r}\big)\lambda{}_{\beta}{}^{i}\lambda{}_{\gamma}{}^{j}\\
&+\frac{3}{128}W^{-4}\varepsilon{}^{a b c d e}(\Gamma{}_{a}){}^{\beta \gamma}F{}_{b c}(\Sigma{}_{d e}){}_{\eta}{}^{\delta}(\Gamma{}^{f}){}_{\delta}{}^{\rho}\big(\nabla_{f}\lambda{}_{\rho}{}^{r}\big)\lambda{}_{\beta}{}^{i}\lambda{}_{\gamma}{}^{j} -\frac{3}{256}W^{-4}\varepsilon{}^{a b c d e}(\Gamma{}_{a}){}^{\beta \gamma}F{}_{b c}(\Sigma{}_{d e}){}^{\delta \rho}W{}_{\eta \delta}\lambda{}_{\rho}{}^{r}\lambda{}_{\beta}{}^{i}\lambda{}_{\gamma}{}^{j}\\
&+\frac{9}{256}W^{-4}\varepsilon{}^{a b c d e}(\Gamma{}_{a}){}^{\beta \gamma}F{}_{b c}(\Sigma{}_{d e}){}_{\eta}{}^{\delta}W{}_{\delta}{}^{\rho}\lambda{}_{\rho}{}^{r}\lambda{}_{\beta}{}^{i}\lambda{}_{\gamma}{}^{j} +\frac{3}{128}W^{-4}\varepsilon{}^{a b c d e}(\Gamma{}_{a}){}^{\beta \gamma}F{}_{b c}(\Sigma{}_{d e}){}^{\delta \rho}(\Gamma{}^{f}){}_{\eta \rho}\big(\nabla_{f}\lambda{}_{\delta}{}^{r}\big)\lambda{}_{\beta}{}^{i}\lambda{}_{\gamma}{}^{j}\\
&+\frac{3}{128}W^{-4}\varepsilon{}^{a b c d e}(\Gamma{}_{a}){}^{\beta \gamma}F{}_{b c}(\Sigma{}_{d e}){}^{\delta}{}_{\eta}(\Gamma{}^{f}){}_{\delta}{}^{\rho}\big(\nabla_{f}\lambda{}_{\rho}{}^{r}\big)\lambda{}_{\beta}{}^{i}\lambda{}_{\gamma}{}^{j} -\frac{3}{256}W^{-4}\varepsilon{}^{a b c d e}(\Gamma{}_{a}){}^{\beta \gamma}F{}_{b c}(\Sigma{}_{d e}){}^{\delta \rho}W{}_{\eta \rho}\lambda{}_{\delta}{}^{r}\lambda{}_{\beta}{}^{i}\lambda{}_{\gamma}{}^{j}\\
&+\frac{9}{256}W^{-4}\varepsilon{}^{a b c d e}(\Gamma{}_{a}){}^{\beta \gamma}F{}_{b c}(\Sigma{}_{d e}){}^{\delta}{}_{\eta}W{}_{\delta}{}^{\rho}\lambda{}_{\rho}{}^{r}\lambda{}_{\beta}{}^{i}\lambda{}_{\gamma}{}^{j} +\frac{9}{128}W^{-4}\varepsilon{}^{a b c d e}(\Gamma{}_{a}){}^{\beta \gamma}F{}_{b c}(\Sigma{}_{d e}){}^{\delta \rho}W{}_{\delta \rho}\lambda{}_{\eta}{}^{r}\lambda{}_{\beta}{}^{i}\lambda{}_{\gamma}{}^{j}\\
&-\frac{3i}{64}W^{-3}\varepsilon{}^{a b c d e}(\Gamma{}_{a}){}^{\beta \gamma}F{}_{b c}(\Sigma{}_{d e}){}^{\delta \rho}W{}_{\eta \delta \rho}{}^{r}\lambda{}_{\beta}{}^{i}\lambda{}_{\gamma}{}^{j} -\frac{3i}{32}W^{-4}\varepsilon{}^{a b c d e}(\Gamma{}_{a}){}^{\beta \gamma}F{}_{b c}F{}_{d e}\varepsilon{}^{r i}F{}_{\eta \beta}\lambda{}_{\gamma}{}^{j}\\
&-\frac{3i}{32}W^{-3}\varepsilon{}^{a b c d e}(\Gamma{}_{a}){}^{\beta \gamma}F{}_{b c}F{}_{d e}\varepsilon{}^{r i}W{}_{\eta \beta}\lambda{}_{\gamma}{}^{j} -\frac{3i}{64}W^{-4}\varepsilon{}^{a b c d e}(\Gamma{}_{a}){}_{\eta}{}^{\beta}F{}_{b c}F{}_{d e}X{}^{r i}\lambda{}_{\beta}{}^{j}\\
&-\frac{3i}{64}W^{-4}\varepsilon{}^{a b c d e}(\Gamma{}_{a}){}^{\beta \gamma}F{}_{b c}F{}_{d e}\varepsilon{}^{r i}(\Gamma{}^{f}){}_{\eta \beta}\big(\nabla_{f}W\big)\lambda{}_{\gamma}{}^{j} +\frac{3i}{32}W^{-4}\varepsilon{}^{a b c d e}(\Gamma{}_{a}){}^{\beta \gamma}F{}_{b c}F{}_{d e}\lambda{}_{\beta}{}^{i}\varepsilon{}^{r j}F{}_{\eta \gamma}\\
&+\frac{3i}{32}W^{-3}\varepsilon{}^{a b c d e}(\Gamma{}_{a}){}^{\beta \gamma}F{}_{b c}F{}_{d e}\lambda{}_{\beta}{}^{i}\varepsilon{}^{r j}W{}_{\eta \gamma} +\frac{3i}{64}W^{-4}\varepsilon{}^{a b c d e}(\Gamma{}_{a}){}^{\beta}{}_{\eta}F{}_{b c}F{}_{d e}\lambda{}_{\beta}{}^{i}X{}^{r j}\\
&+\frac{3i}{64}W^{-4}\varepsilon{}^{a b c d e}(\Gamma{}_{a}){}^{\beta \gamma}F{}_{b c}F{}_{d e}\lambda{}_{\beta}{}^{i}\varepsilon{}^{r j}(\Gamma{}^{f}){}_{\eta \gamma}\big(\nabla_{f}W\big)
\end{aligned}
\tag{S3-H4.5-b}
```

**Check for H4.5:** all 29 written summands have weight $`7/2`$, odd parity and the same free indices $`\eta;r,i,j`$. Dummy labels are paired. The coefficient $`1/3`$ and the two external epsilons are applied once, when collecting the spinor.

#### Input H4.6

The calculated input is

```math
\left.H^{ij}\right|_{\mathrm{H4.6}}=W^{-4}\big(-\frac{3i}{16}(\Sigma_{ab})^{\alpha\beta}X^{ij}F^{ab}\lambda_\alpha^k\lambda_{\beta k}\big).
\tag{S3-H4.6-input}
```

Expand each written SU(2) average with weight $`1/2`$ before applying the left derivative.

Apply the product rule (S3-09), in the displayed factor order:

```math
\begin{aligned}
\left.\nabla_\eta^rH^{ij}\right|_{\mathrm{H4.6}}=&-\frac{3i}{16}\nabla_{\eta}^{r}\big(W^{-4}\big)(\Sigma{}_{a b}){}^{\beta \gamma}X{}^{i j}F{}^{a b}\lambda{}_{\beta}{}^{k}\lambda{}_{\gamma k} -\frac{3i}{16}W^{-4}(\Sigma{}_{a b}){}^{\beta \gamma}\nabla_{\eta}^{r}\big(X{}^{i j}\big)F{}^{a b}\lambda{}_{\beta}{}^{k}\lambda{}_{\gamma k}\\
&-\frac{3i}{16}W^{-4}(\Sigma{}_{a b}){}^{\beta \gamma}X{}^{i j}\nabla_{\eta}^{r}\big(F{}^{a b}\big)\lambda{}_{\beta}{}^{k}\lambda{}_{\gamma k} -\frac{3i}{16}W^{-4}(\Sigma{}_{a b}){}^{\beta \gamma}X{}^{i j}F{}^{a b}\nabla_{\eta}^{r}\big(\lambda{}_{\beta}{}^{k}\big)\lambda{}_{\gamma k}\\
&+\frac{3i}{16}W^{-4}(\Sigma{}_{a b}){}^{\beta \gamma}X{}^{i j}F{}^{a b}\lambda{}_{\beta}{}^{k}\nabla_{\eta}^{r}\big(\lambda{}_{\gamma k}\big)
\end{aligned}
\tag{S3-H4.6-a}
```

Insert the elementary source identities and the applicable commutators (S3-11)–(S3-14), distribute the vector product rules, and contract only index-raising metrics. The resulting contribution is

```math
\begin{aligned}
\left.\nabla_\eta^rH^{ij}\right|_{\mathrm{H4.6}}=&-\frac{3}{4}W^{-5}\lambda{}_{\eta}{}^{r}(\Sigma{}_{a b}){}^{\beta \gamma}X{}^{i j}F{}^{a b}\lambda{}_{\beta}{}^{k}\lambda{}_{\gamma k} +\frac{3}{16}W^{-4}(\Sigma{}_{a b}){}^{\beta \gamma}\varepsilon{}^{r i}(\Gamma{}^{c}){}_{\eta}{}^{\delta}\big(\nabla_{c}\lambda{}_{\delta}{}^{j}\big)F{}^{a b}\lambda{}_{\beta}{}^{k}\lambda{}_{\gamma k}\\
&-\frac{3}{32}W^{-4}(\Sigma{}_{a b}){}^{\beta \gamma}\varepsilon{}^{r i}W{}_{\eta \delta}\lambda{}^{\delta j}F{}^{a b}\lambda{}_{\beta}{}^{k}\lambda{}_{\gamma k} +\frac{9i}{64}W^{-3}(\Sigma{}_{a b}){}^{\beta \gamma}\varepsilon{}^{r i}X{}_{\eta}{}^{j}F{}^{a b}\lambda{}_{\beta}{}^{k}\lambda{}_{\gamma k}\\
&+\frac{3}{16}W^{-4}(\Sigma{}_{a b}){}^{\beta \gamma}\varepsilon{}^{r j}(\Gamma{}^{c}){}_{\eta}{}^{\delta}\big(\nabla_{c}\lambda{}_{\delta}{}^{i}\big)F{}^{a b}\lambda{}_{\beta}{}^{k}\lambda{}_{\gamma k} -\frac{3}{32}W^{-4}(\Sigma{}_{a b}){}^{\beta \gamma}\varepsilon{}^{r j}W{}_{\eta \delta}\lambda{}^{\delta i}F{}^{a b}\lambda{}_{\beta}{}^{k}\lambda{}_{\gamma k}\\
&+\frac{9i}{64}W^{-3}(\Sigma{}_{a b}){}^{\beta \gamma}\varepsilon{}^{r j}X{}_{\eta}{}^{i}F{}^{a b}\lambda{}_{\beta}{}^{k}\lambda{}_{\gamma k} -\frac{3}{32}W^{-4}(\Sigma{}_{a b}){}^{\beta \gamma}X{}^{i j}(\Sigma{}^{a b}){}^{\delta \rho}(\Gamma{}^{c}){}_{\eta \delta}\big(\nabla_{c}\lambda{}_{\rho}{}^{r}\big)\lambda{}_{\beta}{}^{k}\lambda{}_{\gamma k}\\
&-\frac{3}{32}W^{-4}(\Sigma{}_{a b}){}^{\beta \gamma}X{}^{i j}(\Sigma{}^{a b}){}_{\eta}{}^{\delta}(\Gamma{}^{c}){}_{\delta}{}^{\rho}\big(\nabla_{c}\lambda{}_{\rho}{}^{r}\big)\lambda{}_{\beta}{}^{k}\lambda{}_{\gamma k} +\frac{3}{64}W^{-4}(\Sigma{}_{a b}){}^{\beta \gamma}X{}^{i j}(\Sigma{}^{a b}){}^{\delta \rho}W{}_{\eta \delta}\lambda{}_{\rho}{}^{r}\lambda{}_{\beta}{}^{k}\lambda{}_{\gamma k}\\
&-\frac{9}{64}W^{-4}(\Sigma{}_{a b}){}^{\beta \gamma}X{}^{i j}(\Sigma{}^{a b}){}_{\eta}{}^{\delta}W{}_{\delta}{}^{\rho}\lambda{}_{\rho}{}^{r}\lambda{}_{\beta}{}^{k}\lambda{}_{\gamma k} -\frac{3}{32}W^{-4}(\Sigma{}_{a b}){}^{\beta \gamma}X{}^{i j}(\Sigma{}^{a b}){}^{\delta \rho}(\Gamma{}^{c}){}_{\eta \rho}\big(\nabla_{c}\lambda{}_{\delta}{}^{r}\big)\lambda{}_{\beta}{}^{k}\lambda{}_{\gamma k}\\
&-\frac{3}{32}W^{-4}(\Sigma{}_{a b}){}^{\beta \gamma}X{}^{i j}(\Sigma{}^{a b}){}^{\delta}{}_{\eta}(\Gamma{}^{c}){}_{\delta}{}^{\rho}\big(\nabla_{c}\lambda{}_{\rho}{}^{r}\big)\lambda{}_{\beta}{}^{k}\lambda{}_{\gamma k} +\frac{3}{64}W^{-4}(\Sigma{}_{a b}){}^{\beta \gamma}X{}^{i j}(\Sigma{}^{a b}){}^{\delta \rho}W{}_{\eta \rho}\lambda{}_{\delta}{}^{r}\lambda{}_{\beta}{}^{k}\lambda{}_{\gamma k}\\
&-\frac{9}{64}W^{-4}(\Sigma{}_{a b}){}^{\beta \gamma}X{}^{i j}(\Sigma{}^{a b}){}^{\delta}{}_{\eta}W{}_{\delta}{}^{\rho}\lambda{}_{\rho}{}^{r}\lambda{}_{\beta}{}^{k}\lambda{}_{\gamma k} -\frac{9}{32}W^{-4}(\Sigma{}_{a b}){}^{\beta \gamma}X{}^{i j}(\Sigma{}^{a b}){}^{\delta \rho}W{}_{\delta \rho}\lambda{}_{\eta}{}^{r}\lambda{}_{\beta}{}^{k}\lambda{}_{\gamma k}\\
&+\frac{3i}{16}W^{-3}(\Sigma{}_{a b}){}^{\beta \gamma}X{}^{i j}(\Sigma{}^{a b}){}^{\delta \rho}W{}_{\eta \delta \rho}{}^{r}\lambda{}_{\beta}{}^{k}\lambda{}_{\gamma k} +\frac{3i}{8}W^{-4}(\Sigma{}_{a b}){}^{\beta \gamma}X{}^{i j}F{}^{a b}F{}_{\eta \beta}\lambda{}_{\gamma}{}^{r}\\
&+\frac{3i}{8}W^{-3}(\Sigma{}_{a b}){}^{\beta \gamma}X{}^{i j}F{}^{a b}W{}_{\eta \beta}\lambda{}_{\gamma}{}^{r} +\frac{3i}{16}W^{-4}(\Sigma{}_{a b}){}_{\eta}{}^{\beta}X{}^{i j}F{}^{a b}X{}^{r k}\lambda{}_{\beta k}\\
&+\frac{3i}{16}W^{-4}(\Sigma{}_{a b}){}^{\beta \gamma}X{}^{i j}F{}^{a b}(\Gamma{}^{c}){}_{\eta \beta}\big(\nabla_{c}W\big)\lambda{}_{\gamma}{}^{r} +\frac{3i}{8}W^{-4}(\Sigma{}_{a b}){}^{\beta \gamma}X{}^{i j}F{}^{a b}\lambda{}_{\beta}{}^{r}F{}_{\eta \gamma}\\
&+\frac{3i}{8}W^{-3}(\Sigma{}_{a b}){}^{\beta \gamma}X{}^{i j}F{}^{a b}\lambda{}_{\beta}{}^{r}W{}_{\eta \gamma} -\frac{3i}{16}W^{-4}(\Sigma{}_{a b}){}^{\beta}{}_{\eta}X{}^{i j}F{}^{a b}\lambda{}_{\beta}{}^{k}X{}^{r}{}_{k}\\
&+\frac{3i}{16}W^{-4}(\Sigma{}_{a b}){}^{\beta \gamma}X{}^{i j}F{}^{a b}\lambda{}_{\beta}{}^{r}(\Gamma{}^{c}){}_{\eta \gamma}\big(\nabla_{c}W\big)
\end{aligned}
\tag{S3-H4.6-b}
```

**Check for H4.6:** all 25 written summands have weight $`7/2`$, odd parity and the same free indices $`\eta;r,i,j`$. Dummy labels are paired. The coefficient $`1/3`$ and the two external epsilons are applied once, when collecting the spinor.

#### Input H4.7

The calculated input is

```math
\left.H^{ij}\right|_{\mathrm{H4.7}}=W^{-4}\big(-\frac{3i}{16}X^{ij}X^{kl}\lambda_k^\alpha\lambda_{\alpha l}\big).
\tag{S3-H4.7-input}
```

Apply the product rule (S3-09), in the displayed factor order:

```math
\begin{aligned}
\left.\nabla_\eta^rH^{ij}\right|_{\mathrm{H4.7}}=&-\frac{3i}{16}\nabla_{\eta}^{r}\big(W^{-4}\big)X{}^{i j}X{}^{k l}\lambda{}^{\beta}{}_{k}\lambda{}_{\beta l} -\frac{3i}{16}W^{-4}\nabla_{\eta}^{r}\big(X{}^{i j}\big)X{}^{k l}\lambda{}^{\beta}{}_{k}\lambda{}_{\beta l}\\
&-\frac{3i}{16}W^{-4}X{}^{i j}\nabla_{\eta}^{r}\big(X{}^{k l}\big)\lambda{}^{\beta}{}_{k}\lambda{}_{\beta l} -\frac{3i}{16}W^{-4}X{}^{i j}X{}^{k l}\nabla_{\eta}^{r}\big(\lambda{}^{\beta}{}_{k}\big)\lambda{}_{\beta l}\\
&+\frac{3i}{16}W^{-4}X{}^{i j}X{}^{k l}\lambda{}^{\beta}{}_{k}\nabla_{\eta}^{r}\big(\lambda{}_{\beta l}\big)
\end{aligned}
\tag{S3-H4.7-a}
```

Insert the elementary source identities and the applicable commutators (S3-11)–(S3-14), distribute the vector product rules, and contract only index-raising metrics. The resulting contribution is

```math
\begin{aligned}
\left.\nabla_\eta^rH^{ij}\right|_{\mathrm{H4.7}}=&-\frac{3}{4}W^{-5}\lambda{}_{\eta}{}^{r}X{}^{i j}X{}^{k l}\lambda{}^{\beta}{}_{k}\lambda{}_{\beta l} +\frac{3}{16}W^{-4}\varepsilon{}^{r i}(\Gamma{}^{a}){}_{\eta}{}^{\beta}\big(\nabla_{a}\lambda{}_{\beta}{}^{j}\big)X{}^{k l}\lambda{}^{\gamma}{}_{k}\lambda{}_{\gamma l}\\
&-\frac{3}{32}W^{-4}\varepsilon{}^{r i}W{}_{\eta \beta}\lambda{}^{\beta j}X{}^{k l}\lambda{}^{\gamma}{}_{k}\lambda{}_{\gamma l} +\frac{9i}{64}W^{-3}\varepsilon{}^{r i}X{}_{\eta}{}^{j}X{}^{k l}\lambda{}^{\beta}{}_{k}\lambda{}_{\beta l}\\
&+\frac{3}{16}W^{-4}\varepsilon{}^{r j}(\Gamma{}^{a}){}_{\eta}{}^{\beta}\big(\nabla_{a}\lambda{}_{\beta}{}^{i}\big)X{}^{k l}\lambda{}^{\gamma}{}_{k}\lambda{}_{\gamma l} -\frac{3}{32}W^{-4}\varepsilon{}^{r j}W{}_{\eta \beta}\lambda{}^{\beta i}X{}^{k l}\lambda{}^{\gamma}{}_{k}\lambda{}_{\gamma l}\\
&+\frac{9i}{64}W^{-3}\varepsilon{}^{r j}X{}_{\eta}{}^{i}X{}^{k l}\lambda{}^{\beta}{}_{k}\lambda{}_{\beta l} +\frac{3}{16}W^{-4}X{}^{i j}(\Gamma{}^{a}){}_{\eta}{}^{\beta}\big(\nabla_{a}\lambda{}_{\beta}{}^{k}\big)\lambda{}^{\gamma r}\lambda{}_{\gamma k}\\
&-\frac{3}{32}W^{-4}X{}^{i j}W{}_{\eta \beta}\lambda{}^{\beta k}\lambda{}^{\gamma r}\lambda{}_{\gamma k} +\frac{9i}{64}W^{-3}X{}^{i j}X{}_{\eta}{}^{k}\lambda{}^{\beta r}\lambda{}_{\beta k}\\
&+\frac{3}{16}W^{-4}X{}^{i j}(\Gamma{}^{a}){}_{\eta}{}^{\beta}\big(\nabla_{a}\lambda{}_{\beta}{}^{k}\big)\lambda{}^{\gamma}{}_{k}\lambda{}_{\gamma}{}^{r} -\frac{3}{32}W^{-4}X{}^{i j}W{}_{\eta \beta}\lambda{}^{\beta k}\lambda{}^{\gamma}{}_{k}\lambda{}_{\gamma}{}^{r}\\
&+\frac{9i}{64}W^{-3}X{}^{i j}X{}_{\eta}{}^{k}\lambda{}^{\beta}{}_{k}\lambda{}_{\beta}{}^{r} -\frac{3i}{8}W^{-4}X{}^{i j}X{}^{r k}F{}_{\eta}{}^{\beta}\lambda{}_{\beta k}\\
&-\frac{3i}{8}W^{-3}X{}^{i j}X{}^{r k}W{}_{\eta}{}^{\beta}\lambda{}_{\beta k} -\frac{3i}{16}W^{-4}X{}^{i j}X{}^{k l}X{}^{r}{}_{k}\lambda{}_{\eta l}\\
&-\frac{3i}{16}W^{-4}X{}^{i j}X{}^{r k}(\Gamma{}^{a}){}_{\eta}{}^{\beta}\big(\nabla_{a}W\big)\lambda{}_{\beta k} +\frac{3i}{8}W^{-4}X{}^{i j}X{}^{k r}\lambda{}^{\beta}{}_{k}F{}_{\eta \beta}\\
&+\frac{3i}{8}W^{-3}X{}^{i j}X{}^{k r}\lambda{}^{\beta}{}_{k}W{}_{\eta \beta} -\frac{3i}{16}W^{-4}X{}^{i j}X{}^{k l}\lambda{}_{\eta k}X{}^{r}{}_{l}\\
&+\frac{3i}{16}W^{-4}X{}^{i j}X{}^{k r}\lambda{}^{\beta}{}_{k}(\Gamma{}^{a}){}_{\eta \beta}\big(\nabla_{a}W\big)
\end{aligned}
\tag{S3-H4.7-b}
```

**Check for H4.7:** all 21 written summands have weight $`7/2`$, odd parity and the same free indices $`\eta;r,i,j`$. Dummy labels are paired. The coefficient $`1/3`$ and the two external epsilons are applied once, when collecting the spinor.

#### Input H4.8

The calculated input is

```math
\left.H^{ij}\right|_{\mathrm{H4.8}}=W^{-4}\big(-\frac{3i}{32}X^{kl}X_{kl}\lambda^{\alpha i}\lambda_\alpha^j\big).
\tag{S3-H4.8-input}
```

Apply the product rule (S3-09), in the displayed factor order:

```math
\begin{aligned}
\left.\nabla_\eta^rH^{ij}\right|_{\mathrm{H4.8}}=&-\frac{3i}{32}\nabla_{\eta}^{r}\big(W^{-4}\big)X{}^{k l}X{}_{k l}\lambda{}^{\beta i}\lambda{}_{\beta}{}^{j} -\frac{3i}{32}W^{-4}\nabla_{\eta}^{r}\big(X{}^{k l}\big)X{}_{k l}\lambda{}^{\beta i}\lambda{}_{\beta}{}^{j}\\
&-\frac{3i}{32}W^{-4}X{}^{k l}\nabla_{\eta}^{r}\big(X{}_{k l}\big)\lambda{}^{\beta i}\lambda{}_{\beta}{}^{j} -\frac{3i}{32}W^{-4}X{}^{k l}X{}_{k l}\nabla_{\eta}^{r}\big(\lambda{}^{\beta i}\big)\lambda{}_{\beta}{}^{j}\\
&+\frac{3i}{32}W^{-4}X{}^{k l}X{}_{k l}\lambda{}^{\beta i}\nabla_{\eta}^{r}\big(\lambda{}_{\beta}{}^{j}\big)
\end{aligned}
\tag{S3-H4.8-a}
```

Insert the elementary source identities and the applicable commutators (S3-11)–(S3-14), distribute the vector product rules, and contract only index-raising metrics. The resulting contribution is

```math
\begin{aligned}
\left.\nabla_\eta^rH^{ij}\right|_{\mathrm{H4.8}}=&-\frac{3}{8}W^{-5}\lambda{}_{\eta}{}^{r}X{}^{k l}X{}_{k l}\lambda{}^{\beta i}\lambda{}_{\beta}{}^{j} +\frac{3}{32}W^{-4}(\Gamma{}^{a}){}_{\eta}{}^{\beta}\big(\nabla_{a}\lambda{}_{\beta}{}^{k}\big)X{}^{r}{}_{k}\lambda{}^{\gamma i}\lambda{}_{\gamma}{}^{j}\\
&-\frac{3}{64}W^{-4}W{}_{\eta \beta}\lambda{}^{\beta k}X{}^{r}{}_{k}\lambda{}^{\gamma i}\lambda{}_{\gamma}{}^{j} +\frac{9i}{128}W^{-3}X{}_{\eta}{}^{k}X{}^{r}{}_{k}\lambda{}^{\beta i}\lambda{}_{\beta}{}^{j}\\
&+\frac{3}{32}W^{-4}(\Gamma{}^{a}){}_{\eta}{}^{\beta}\big(\nabla_{a}\lambda{}_{\beta}{}^{k}\big)X{}_{k}{}^{r}\lambda{}^{\gamma i}\lambda{}_{\gamma}{}^{j} -\frac{3}{64}W^{-4}W{}_{\eta \beta}\lambda{}^{\beta k}X{}_{k}{}^{r}\lambda{}^{\gamma i}\lambda{}_{\gamma}{}^{j}\\
&+\frac{9i}{128}W^{-3}X{}_{\eta}{}^{k}X{}_{k}{}^{r}\lambda{}^{\beta i}\lambda{}_{\beta}{}^{j} -\frac{3}{32}W^{-4}X{}^{r k}(\Gamma{}^{a}){}_{\eta}{}^{\beta}\big(\nabla_{a}\lambda{}_{\beta k}\big)\lambda{}^{\gamma i}\lambda{}_{\gamma}{}^{j}\\
&+\frac{3}{64}W^{-4}X{}^{r k}W{}_{\eta \beta}\lambda{}^{\beta}{}_{k}\lambda{}^{\gamma i}\lambda{}_{\gamma}{}^{j} -\frac{9i}{128}W^{-3}X{}^{r k}X{}_{\eta k}\lambda{}^{\beta i}\lambda{}_{\beta}{}^{j}\\
&-\frac{3}{32}W^{-4}X{}^{k r}(\Gamma{}^{a}){}_{\eta}{}^{\beta}\big(\nabla_{a}\lambda{}_{\beta k}\big)\lambda{}^{\gamma i}\lambda{}_{\gamma}{}^{j} +\frac{3}{64}W^{-4}X{}^{k r}W{}_{\eta \beta}\lambda{}^{\beta}{}_{k}\lambda{}^{\gamma i}\lambda{}_{\gamma}{}^{j}\\
&-\frac{9i}{128}W^{-3}X{}^{k r}X{}_{\eta k}\lambda{}^{\beta i}\lambda{}_{\beta}{}^{j} +\frac{3i}{16}W^{-4}X{}^{k l}X{}_{k l}\varepsilon{}^{r i}F{}_{\eta}{}^{\beta}\lambda{}_{\beta}{}^{j}\\
&+\frac{3i}{16}W^{-3}X{}^{k l}X{}_{k l}\varepsilon{}^{r i}W{}_{\eta}{}^{\beta}\lambda{}_{\beta}{}^{j} -\frac{3i}{32}W^{-4}X{}^{k l}X{}_{k l}X{}^{r i}\lambda{}_{\eta}{}^{j}\\
&+\frac{3i}{32}W^{-4}X{}^{k l}X{}_{k l}\varepsilon{}^{r i}(\Gamma{}^{a}){}_{\eta}{}^{\beta}\big(\nabla_{a}W\big)\lambda{}_{\beta}{}^{j} -\frac{3i}{16}W^{-4}X{}^{k l}X{}_{k l}\lambda{}^{\beta i}\varepsilon{}^{r j}F{}_{\eta \beta}\\
&-\frac{3i}{16}W^{-3}X{}^{k l}X{}_{k l}\lambda{}^{\beta i}\varepsilon{}^{r j}W{}_{\eta \beta} -\frac{3i}{32}W^{-4}X{}^{k l}X{}_{k l}\lambda{}_{\eta}{}^{i}X{}^{r j}\\
&-\frac{3i}{32}W^{-4}X{}^{k l}X{}_{k l}\lambda{}^{\beta i}\varepsilon{}^{r j}(\Gamma{}^{a}){}_{\eta \beta}\big(\nabla_{a}W\big)
\end{aligned}
\tag{S3-H4.8-b}
```

**Check for H4.8:** all 21 written summands have weight $`7/2`$, odd parity and the same free indices $`\eta;r,i,j`$. Dummy labels are paired. The coefficient $`1/3`$ and the two external epsilons are applied once, when collecting the spinor.

#### Input H4.9

The calculated input is

```math
\left.H^{ij}\right|_{\mathrm{H4.9}}=W^{-4}\big(-\frac{15}{64}(\Gamma^a)^{\alpha\beta}\lambda_\alpha^i\lambda_\beta^j\lambda^{\gamma k}\nabla_a\lambda_{\gamma k}\big).
\tag{S3-H4.9-input}
```

Expand each written SU(2) average with weight $`1/2`$ before applying the left derivative.

Apply the product rule (S3-09), in the displayed factor order:

```math
\begin{aligned}
\left.\nabla_\eta^rH^{ij}\right|_{\mathrm{H4.9}}=&-\frac{15}{64}\nabla_{\eta}^{r}\big(W^{-4}\big)(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{i}\lambda{}_{\gamma}{}^{j}\lambda{}^{\delta k}\big(\nabla_{a}\lambda{}_{\delta k}\big) -\frac{15}{64}W^{-4}(\Gamma{}^{a}){}^{\beta \gamma}\nabla_{\eta}^{r}\big(\lambda{}_{\beta}{}^{i}\big)\lambda{}_{\gamma}{}^{j}\lambda{}^{\delta k}\big(\nabla_{a}\lambda{}_{\delta k}\big)\\
&+\frac{15}{64}W^{-4}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{i}\nabla_{\eta}^{r}\big(\lambda{}_{\gamma}{}^{j}\big)\lambda{}^{\delta k}\big(\nabla_{a}\lambda{}_{\delta k}\big) -\frac{15}{64}W^{-4}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{i}\lambda{}_{\gamma}{}^{j}\nabla_{\eta}^{r}\big(\lambda{}^{\delta k}\big)\big(\nabla_{a}\lambda{}_{\delta k}\big)\\
&+\frac{15}{64}W^{-4}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{i}\lambda{}_{\gamma}{}^{j}\lambda{}^{\delta k}\nabla_{\eta}^{r}\big(\nabla_{a}\lambda{}_{\delta k}\big)
\end{aligned}
\tag{S3-H4.9-a}
```

Insert the elementary source identities and the applicable commutators (S3-11)–(S3-14), distribute the vector product rules, and contract only index-raising metrics. The resulting contribution is

```math
\begin{aligned}
\left.\nabla_\eta^rH^{ij}\right|_{\mathrm{H4.9}}=&\frac{15i}{16}W^{-5}\lambda{}_{\eta}{}^{r}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{i}\lambda{}_{\gamma}{}^{j}\lambda{}^{\delta k}\big(\nabla_{a}\lambda{}_{\delta k}\big) +\frac{15}{32}W^{-4}(\Gamma{}^{a}){}^{\beta \gamma}\varepsilon{}^{r i}F{}_{\eta \beta}\lambda{}_{\gamma}{}^{j}\lambda{}^{\delta k}\big(\nabla_{a}\lambda{}_{\delta k}\big)\\
&+\frac{15}{32}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}\varepsilon{}^{r i}W{}_{\eta \beta}\lambda{}_{\gamma}{}^{j}\lambda{}^{\delta k}\big(\nabla_{a}\lambda{}_{\delta k}\big) +\frac{15}{64}W^{-4}(\Gamma{}^{a}){}_{\eta}{}^{\beta}X{}^{r i}\lambda{}_{\beta}{}^{j}\lambda{}^{\gamma k}\big(\nabla_{a}\lambda{}_{\gamma k}\big)\\
&+\frac{15}{64}W^{-4}(\Gamma{}^{a}){}^{\beta \gamma}\varepsilon{}^{r i}(\Gamma{}^{b}){}_{\eta \beta}\big(\nabla_{b}W\big)\lambda{}_{\gamma}{}^{j}\lambda{}^{\delta k}\big(\nabla_{a}\lambda{}_{\delta k}\big) -\frac{15}{32}W^{-4}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{i}\varepsilon{}^{r j}F{}_{\eta \gamma}\lambda{}^{\delta k}\big(\nabla_{a}\lambda{}_{\delta k}\big)\\
&-\frac{15}{32}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{i}\varepsilon{}^{r j}W{}_{\eta \gamma}\lambda{}^{\delta k}\big(\nabla_{a}\lambda{}_{\delta k}\big) -\frac{15}{64}W^{-4}(\Gamma{}^{a}){}^{\beta}{}_{\eta}\lambda{}_{\beta}{}^{i}X{}^{r j}\lambda{}^{\gamma k}\big(\nabla_{a}\lambda{}_{\gamma k}\big)\\
&-\frac{15}{64}W^{-4}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{i}\varepsilon{}^{r j}(\Gamma{}^{b}){}_{\eta \gamma}\big(\nabla_{b}W\big)\lambda{}^{\delta k}\big(\nabla_{a}\lambda{}_{\delta k}\big) +\frac{15}{32}W^{-4}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{i}\lambda{}_{\gamma}{}^{j}F{}_{\eta}{}^{\delta}\big(\nabla_{a}\lambda{}_{\delta}{}^{r}\big)\\
&+\frac{15}{32}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{i}\lambda{}_{\gamma}{}^{j}W{}_{\eta}{}^{\delta}\big(\nabla_{a}\lambda{}_{\delta}{}^{r}\big) -\frac{15}{64}W^{-4}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{i}\lambda{}_{\gamma}{}^{j}X{}^{r k}\big(\nabla_{a}\lambda{}_{\eta k}\big)\\
&+\frac{15}{64}W^{-4}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{i}\lambda{}_{\gamma}{}^{j}(\Gamma{}^{b}){}_{\eta}{}^{\delta}\big(\nabla_{b}W\big)\big(\nabla_{a}\lambda{}_{\delta}{}^{r}\big) +\frac{15}{32}W^{-4}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{i}\lambda{}_{\gamma}{}^{j}\lambda{}^{\delta r}\big(\nabla_{a}F{}_{\eta \delta}\big)\\
&+\frac{15}{32}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{i}\lambda{}_{\gamma}{}^{j}\lambda{}^{\delta r}\big(\nabla_{a}W{}_{\eta \delta}\big) +\frac{15}{32}W^{-4}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{i}\lambda{}_{\gamma}{}^{j}\lambda{}^{\delta r}W{}_{\eta \delta}\big(\nabla_{a}W\big)\\
&-\frac{15}{64}W^{-4}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{i}\lambda{}_{\gamma}{}^{j}\lambda{}_{\eta}{}^{k}\big(\nabla_{a}X{}^{r}{}_{k}\big) +\frac{15}{64}W^{-4}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{i}\lambda{}_{\gamma}{}^{j}\lambda{}^{\delta r}(\Gamma{}^{b}){}_{\eta \delta}\big(\nabla_{a}\nabla_{b}W\big)\\
&+\frac{15}{32}W^{-4}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{i}\lambda{}_{\gamma}{}^{j}\lambda{}^{\delta r}\mathcal T{}_{a \eta}{}^{\rho}F{}_{\rho \delta} +\frac{15}{32}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{i}\lambda{}_{\gamma}{}^{j}\lambda{}^{\delta r}\mathcal T{}_{a \eta}{}^{\rho}W{}_{\rho \delta}\\
&-\frac{15}{64}W^{-4}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{i}\lambda{}_{\gamma}{}^{j}\lambda{}_{\delta}{}^{k}\mathcal T{}_{a \eta}{}^{\delta}X{}^{r}{}_{k} +\frac{15}{64}W^{-4}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{i}\lambda{}_{\gamma}{}^{j}\lambda{}^{\delta r}\mathcal T{}_{a \eta}{}^{\rho}(\Gamma{}^{b}){}_{\rho \delta}\big(\nabla_{b}W\big)\\
&+\frac{15}{128}W^{-4}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{i}\lambda{}_{\gamma}{}^{j}\lambda{}^{\delta k}\mathcal R(M){}_{a \eta}{}^{r b c}(\Sigma{}_{b c}){}_{\delta}{}^{\rho}\lambda{}_{\rho k} +\frac{45}{128}W^{-4}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{i}\lambda{}_{\gamma}{}^{j}\lambda{}^{\delta k}\mathcal R(\mathbb D){}_{a \eta}{}^{r}\lambda{}_{\delta k}\\
&+\frac{15}{128}W^{-4}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{i}\lambda{}_{\gamma}{}^{j}\lambda{}^{\delta}{}_{k}\mathcal R(J){}_{a \eta}{}^{r k l}\lambda{}_{\delta l} +\frac{15}{128}W^{-4}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{i}\lambda{}_{\gamma}{}^{j}\lambda{}^{\delta}{}_{k}\mathcal R(J){}_{a \eta}{}^{r l k}\lambda{}_{\delta l}\\
&+\frac{15i}{32}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{i}\lambda{}_{\gamma}{}^{j}\lambda{}_{\delta k}\mathcal R(S){}_{a \eta}{}^{r \delta k}
\end{aligned}
\tag{S3-H4.9-b}
```

**Check for H4.9:** all 27 written summands have weight $`7/2`$, odd parity and the same free indices $`\eta;r,i,j`$. Dummy labels are paired. The coefficient $`1/3`$ and the two external epsilons are applied once, when collecting the spinor.

#### Input H4.10

The calculated input is

```math
\left.H^{ij}\right|_{\mathrm{H4.10}}=W^{-4}\big(-\frac9{32}(\Gamma^a)^{\alpha\beta}\lambda_\alpha^{(i}\lambda^{\rho j)}\lambda_\beta^k\nabla_a\lambda_{\rho k}\big).
\tag{S3-H4.10-input}
```

Expand each written SU(2) average with weight $`1/2`$ before applying the left derivative.

Apply the product rule (S3-09), in the displayed factor order:

```math
\begin{aligned}
\left.\nabla_\eta^rH^{ij}\right|_{\mathrm{H4.10}}=&-\frac{9}{64}\nabla_{\eta}^{r}\big(W^{-4}\big)(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{i}\lambda{}^{\delta j}\lambda{}_{\gamma}{}^{k}\big(\nabla_{a}\lambda{}_{\delta k}\big) -\frac{9}{64}W^{-4}(\Gamma{}^{a}){}^{\beta \gamma}\nabla_{\eta}^{r}\big(\lambda{}_{\beta}{}^{i}\big)\lambda{}^{\delta j}\lambda{}_{\gamma}{}^{k}\big(\nabla_{a}\lambda{}_{\delta k}\big)\\
&+\frac{9}{64}W^{-4}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{i}\nabla_{\eta}^{r}\big(\lambda{}^{\delta j}\big)\lambda{}_{\gamma}{}^{k}\big(\nabla_{a}\lambda{}_{\delta k}\big) -\frac{9}{64}W^{-4}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{i}\lambda{}^{\delta j}\nabla_{\eta}^{r}\big(\lambda{}_{\gamma}{}^{k}\big)\big(\nabla_{a}\lambda{}_{\delta k}\big)\\
&+\frac{9}{64}W^{-4}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{i}\lambda{}^{\delta j}\lambda{}_{\gamma}{}^{k}\nabla_{\eta}^{r}\big(\nabla_{a}\lambda{}_{\delta k}\big) -\frac{9}{64}\nabla_{\eta}^{r}\big(W^{-4}\big)(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{j}\lambda{}^{\delta i}\lambda{}_{\gamma}{}^{k}\big(\nabla_{a}\lambda{}_{\delta k}\big)\\
&-\frac{9}{64}W^{-4}(\Gamma{}^{a}){}^{\beta \gamma}\nabla_{\eta}^{r}\big(\lambda{}_{\beta}{}^{j}\big)\lambda{}^{\delta i}\lambda{}_{\gamma}{}^{k}\big(\nabla_{a}\lambda{}_{\delta k}\big) +\frac{9}{64}W^{-4}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{j}\nabla_{\eta}^{r}\big(\lambda{}^{\delta i}\big)\lambda{}_{\gamma}{}^{k}\big(\nabla_{a}\lambda{}_{\delta k}\big)\\
&-\frac{9}{64}W^{-4}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{j}\lambda{}^{\delta i}\nabla_{\eta}^{r}\big(\lambda{}_{\gamma}{}^{k}\big)\big(\nabla_{a}\lambda{}_{\delta k}\big) +\frac{9}{64}W^{-4}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{j}\lambda{}^{\delta i}\lambda{}_{\gamma}{}^{k}\nabla_{\eta}^{r}\big(\nabla_{a}\lambda{}_{\delta k}\big)
\end{aligned}
\tag{S3-H4.10-a}
```

Insert the elementary source identities and the applicable commutators (S3-11)–(S3-14), distribute the vector product rules, and contract only index-raising metrics. The resulting contribution is

```math
\begin{aligned}
\left.\nabla_\eta^rH^{ij}\right|_{\mathrm{H4.10}}=&\frac{9i}{16}W^{-5}\lambda{}_{\eta}{}^{r}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{i}\lambda{}^{\delta j}\lambda{}_{\gamma}{}^{k}\big(\nabla_{a}\lambda{}_{\delta k}\big) +\frac{9}{32}W^{-4}(\Gamma{}^{a}){}^{\beta \gamma}\varepsilon{}^{r i}F{}_{\eta \beta}\lambda{}^{\delta j}\lambda{}_{\gamma}{}^{k}\big(\nabla_{a}\lambda{}_{\delta k}\big)\\
&+\frac{9}{32}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}\varepsilon{}^{r i}W{}_{\eta \beta}\lambda{}^{\delta j}\lambda{}_{\gamma}{}^{k}\big(\nabla_{a}\lambda{}_{\delta k}\big) +\frac{9}{64}W^{-4}(\Gamma{}^{a}){}_{\eta}{}^{\beta}X{}^{r i}\lambda{}^{\gamma j}\lambda{}_{\beta}{}^{k}\big(\nabla_{a}\lambda{}_{\gamma k}\big)\\
&+\frac{9}{64}W^{-4}(\Gamma{}^{a}){}^{\beta \gamma}\varepsilon{}^{r i}(\Gamma{}^{b}){}_{\eta \beta}\big(\nabla_{b}W\big)\lambda{}^{\delta j}\lambda{}_{\gamma}{}^{k}\big(\nabla_{a}\lambda{}_{\delta k}\big) -\frac{9}{32}W^{-4}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{i}\varepsilon{}^{r j}F{}_{\eta}{}^{\delta}\lambda{}_{\gamma}{}^{k}\big(\nabla_{a}\lambda{}_{\delta k}\big)\\
&-\frac{9}{32}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{i}\varepsilon{}^{r j}W{}_{\eta}{}^{\delta}\lambda{}_{\gamma}{}^{k}\big(\nabla_{a}\lambda{}_{\delta k}\big) +\frac{9}{64}W^{-4}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{i}X{}^{r j}\lambda{}_{\gamma}{}^{k}\big(\nabla_{a}\lambda{}_{\eta k}\big)\\
&-\frac{9}{64}W^{-4}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{i}\varepsilon{}^{r j}(\Gamma{}^{b}){}_{\eta}{}^{\delta}\big(\nabla_{b}W\big)\lambda{}_{\gamma}{}^{k}\big(\nabla_{a}\lambda{}_{\delta k}\big) +\frac{9}{32}W^{-4}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{i}\lambda{}^{\delta j}F{}_{\eta \gamma}\big(\nabla_{a}\lambda{}_{\delta}{}^{r}\big)\\
&+\frac{9}{32}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{i}\lambda{}^{\delta j}W{}_{\eta \gamma}\big(\nabla_{a}\lambda{}_{\delta}{}^{r}\big) +\frac{9}{64}W^{-4}(\Gamma{}^{a}){}^{\beta}{}_{\eta}\lambda{}_{\beta}{}^{i}\lambda{}^{\gamma j}X{}^{r k}\big(\nabla_{a}\lambda{}_{\gamma k}\big)\\
&+\frac{9}{64}W^{-4}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{i}\lambda{}^{\delta j}(\Gamma{}^{b}){}_{\eta \gamma}\big(\nabla_{b}W\big)\big(\nabla_{a}\lambda{}_{\delta}{}^{r}\big) +\frac{9}{32}W^{-4}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{i}\lambda{}^{\delta j}\lambda{}_{\gamma}{}^{r}\big(\nabla_{a}F{}_{\eta \delta}\big)\\
&+\frac{9}{32}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{i}\lambda{}^{\delta j}\lambda{}_{\gamma}{}^{r}\big(\nabla_{a}W{}_{\eta \delta}\big) +\frac{9}{32}W^{-4}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{i}\lambda{}^{\delta j}\lambda{}_{\gamma}{}^{r}W{}_{\eta \delta}\big(\nabla_{a}W\big)\\
&-\frac{9}{64}W^{-4}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{i}\lambda{}_{\eta}{}^{j}\lambda{}_{\gamma}{}^{k}\big(\nabla_{a}X{}^{r}{}_{k}\big) +\frac{9}{64}W^{-4}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{i}\lambda{}^{\delta j}\lambda{}_{\gamma}{}^{r}(\Gamma{}^{b}){}_{\eta \delta}\big(\nabla_{a}\nabla_{b}W\big)\\
&+\frac{9}{32}W^{-4}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{i}\lambda{}^{\delta j}\lambda{}_{\gamma}{}^{r}\mathcal T{}_{a \eta}{}^{\rho}F{}_{\rho \delta} +\frac{9}{32}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{i}\lambda{}^{\delta j}\lambda{}_{\gamma}{}^{r}\mathcal T{}_{a \eta}{}^{\rho}W{}_{\rho \delta}\\
&-\frac{9}{64}W^{-4}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{i}\lambda{}_{\delta}{}^{j}\lambda{}_{\gamma}{}^{k}\mathcal T{}_{a \eta}{}^{\delta}X{}^{r}{}_{k} +\frac{9}{64}W^{-4}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{i}\lambda{}^{\delta j}\lambda{}_{\gamma}{}^{r}\mathcal T{}_{a \eta}{}^{\rho}(\Gamma{}^{b}){}_{\rho \delta}\big(\nabla_{b}W\big)\\
&+\frac{9}{128}W^{-4}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{i}\lambda{}^{\delta j}\lambda{}_{\gamma}{}^{k}\mathcal R(M){}_{a \eta}{}^{r b c}(\Sigma{}_{b c}){}_{\delta}{}^{\rho}\lambda{}_{\rho k} +\frac{27}{128}W^{-4}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{i}\lambda{}^{\delta j}\lambda{}_{\gamma}{}^{k}\mathcal R(\mathbb D){}_{a \eta}{}^{r}\lambda{}_{\delta k}\\
&+\frac{9}{128}W^{-4}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{i}\lambda{}^{\delta j}\lambda{}_{\gamma k}\mathcal R(J){}_{a \eta}{}^{r k l}\lambda{}_{\delta l} +\frac{9}{128}W^{-4}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{i}\lambda{}^{\delta j}\lambda{}_{\gamma k}\mathcal R(J){}_{a \eta}{}^{r l k}\lambda{}_{\delta l}\\
&+\frac{9i}{32}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{i}\lambda{}_{\delta}{}^{j}\lambda{}_{\gamma k}\mathcal R(S){}_{a \eta}{}^{r \delta k} +\frac{9i}{16}W^{-5}\lambda{}_{\eta}{}^{r}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{j}\lambda{}^{\delta i}\lambda{}_{\gamma}{}^{k}\big(\nabla_{a}\lambda{}_{\delta k}\big)\\
&+\frac{9}{32}W^{-4}(\Gamma{}^{a}){}^{\beta \gamma}\varepsilon{}^{r j}F{}_{\eta \beta}\lambda{}^{\delta i}\lambda{}_{\gamma}{}^{k}\big(\nabla_{a}\lambda{}_{\delta k}\big) +\frac{9}{32}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}\varepsilon{}^{r j}W{}_{\eta \beta}\lambda{}^{\delta i}\lambda{}_{\gamma}{}^{k}\big(\nabla_{a}\lambda{}_{\delta k}\big)\\
&+\frac{9}{64}W^{-4}(\Gamma{}^{a}){}_{\eta}{}^{\beta}X{}^{r j}\lambda{}^{\gamma i}\lambda{}_{\beta}{}^{k}\big(\nabla_{a}\lambda{}_{\gamma k}\big) +\frac{9}{64}W^{-4}(\Gamma{}^{a}){}^{\beta \gamma}\varepsilon{}^{r j}(\Gamma{}^{b}){}_{\eta \beta}\big(\nabla_{b}W\big)\lambda{}^{\delta i}\lambda{}_{\gamma}{}^{k}\big(\nabla_{a}\lambda{}_{\delta k}\big)\\
&-\frac{9}{32}W^{-4}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{j}\varepsilon{}^{r i}F{}_{\eta}{}^{\delta}\lambda{}_{\gamma}{}^{k}\big(\nabla_{a}\lambda{}_{\delta k}\big) -\frac{9}{32}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{j}\varepsilon{}^{r i}W{}_{\eta}{}^{\delta}\lambda{}_{\gamma}{}^{k}\big(\nabla_{a}\lambda{}_{\delta k}\big)\\
&+\frac{9}{64}W^{-4}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{j}X{}^{r i}\lambda{}_{\gamma}{}^{k}\big(\nabla_{a}\lambda{}_{\eta k}\big) -\frac{9}{64}W^{-4}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{j}\varepsilon{}^{r i}(\Gamma{}^{b}){}_{\eta}{}^{\delta}\big(\nabla_{b}W\big)\lambda{}_{\gamma}{}^{k}\big(\nabla_{a}\lambda{}_{\delta k}\big)\\
&+\frac{9}{32}W^{-4}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{j}\lambda{}^{\delta i}F{}_{\eta \gamma}\big(\nabla_{a}\lambda{}_{\delta}{}^{r}\big) +\frac{9}{32}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{j}\lambda{}^{\delta i}W{}_{\eta \gamma}\big(\nabla_{a}\lambda{}_{\delta}{}^{r}\big)\\
&+\frac{9}{64}W^{-4}(\Gamma{}^{a}){}^{\beta}{}_{\eta}\lambda{}_{\beta}{}^{j}\lambda{}^{\gamma i}X{}^{r k}\big(\nabla_{a}\lambda{}_{\gamma k}\big) +\frac{9}{64}W^{-4}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{j}\lambda{}^{\delta i}(\Gamma{}^{b}){}_{\eta \gamma}\big(\nabla_{b}W\big)\big(\nabla_{a}\lambda{}_{\delta}{}^{r}\big)\\
&+\frac{9}{32}W^{-4}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{j}\lambda{}^{\delta i}\lambda{}_{\gamma}{}^{r}\big(\nabla_{a}F{}_{\eta \delta}\big) +\frac{9}{32}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{j}\lambda{}^{\delta i}\lambda{}_{\gamma}{}^{r}\big(\nabla_{a}W{}_{\eta \delta}\big)\\
&+\frac{9}{32}W^{-4}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{j}\lambda{}^{\delta i}\lambda{}_{\gamma}{}^{r}W{}_{\eta \delta}\big(\nabla_{a}W\big) -\frac{9}{64}W^{-4}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{j}\lambda{}_{\eta}{}^{i}\lambda{}_{\gamma}{}^{k}\big(\nabla_{a}X{}^{r}{}_{k}\big)\\
&+\frac{9}{64}W^{-4}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{j}\lambda{}^{\delta i}\lambda{}_{\gamma}{}^{r}(\Gamma{}^{b}){}_{\eta \delta}\big(\nabla_{a}\nabla_{b}W\big) +\frac{9}{32}W^{-4}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{j}\lambda{}^{\delta i}\lambda{}_{\gamma}{}^{r}\mathcal T{}_{a \eta}{}^{\rho}F{}_{\rho \delta}\\
&+\frac{9}{32}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{j}\lambda{}^{\delta i}\lambda{}_{\gamma}{}^{r}\mathcal T{}_{a \eta}{}^{\rho}W{}_{\rho \delta} -\frac{9}{64}W^{-4}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{j}\lambda{}_{\delta}{}^{i}\lambda{}_{\gamma}{}^{k}\mathcal T{}_{a \eta}{}^{\delta}X{}^{r}{}_{k}\\
&+\frac{9}{64}W^{-4}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{j}\lambda{}^{\delta i}\lambda{}_{\gamma}{}^{r}\mathcal T{}_{a \eta}{}^{\rho}(\Gamma{}^{b}){}_{\rho \delta}\big(\nabla_{b}W\big) +\frac{9}{128}W^{-4}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{j}\lambda{}^{\delta i}\lambda{}_{\gamma}{}^{k}\mathcal R(M){}_{a \eta}{}^{r b c}(\Sigma{}_{b c}){}_{\delta}{}^{\rho}\lambda{}_{\rho k}\\
&+\frac{27}{128}W^{-4}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{j}\lambda{}^{\delta i}\lambda{}_{\gamma}{}^{k}\mathcal R(\mathbb D){}_{a \eta}{}^{r}\lambda{}_{\delta k} +\frac{9}{128}W^{-4}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{j}\lambda{}^{\delta i}\lambda{}_{\gamma k}\mathcal R(J){}_{a \eta}{}^{r k l}\lambda{}_{\delta l}\\
&+\frac{9}{128}W^{-4}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{j}\lambda{}^{\delta i}\lambda{}_{\gamma k}\mathcal R(J){}_{a \eta}{}^{r l k}\lambda{}_{\delta l} +\frac{9i}{32}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{j}\lambda{}_{\delta}{}^{i}\lambda{}_{\gamma k}\mathcal R(S){}_{a \eta}{}^{r \delta k}
\end{aligned}
\tag{S3-H4.10-b}
```

**Check for H4.10:** all 54 written summands have weight $`7/2`$, odd parity and the same free indices $`\eta;r,i,j`$. Dummy labels are paired. The coefficient $`1/3`$ and the two external epsilons are applied once, when collecting the spinor.

#### Input H4.11

The calculated input is

```math
\left.H^{ij}\right|_{\mathrm{H4.11}}=W^{-4}\big(-\frac{15}{32}(\Gamma^a)^{\alpha\beta}\lambda_\alpha^{(i}\lambda^{\rho j)}\lambda_\rho^k\nabla_a\lambda_{\beta k}\big).
\tag{S3-H4.11-input}
```

Expand each written SU(2) average with weight $`1/2`$ before applying the left derivative.

Apply the product rule (S3-09), in the displayed factor order:

```math
\begin{aligned}
\left.\nabla_\eta^rH^{ij}\right|_{\mathrm{H4.11}}=&-\frac{15}{64}\nabla_{\eta}^{r}\big(W^{-4}\big)(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{i}\lambda{}^{\delta j}\lambda{}_{\delta}{}^{k}\big(\nabla_{a}\lambda{}_{\gamma k}\big) -\frac{15}{64}W^{-4}(\Gamma{}^{a}){}^{\beta \gamma}\nabla_{\eta}^{r}\big(\lambda{}_{\beta}{}^{i}\big)\lambda{}^{\delta j}\lambda{}_{\delta}{}^{k}\big(\nabla_{a}\lambda{}_{\gamma k}\big)\\
&+\frac{15}{64}W^{-4}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{i}\nabla_{\eta}^{r}\big(\lambda{}^{\delta j}\big)\lambda{}_{\delta}{}^{k}\big(\nabla_{a}\lambda{}_{\gamma k}\big) -\frac{15}{64}W^{-4}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{i}\lambda{}^{\delta j}\nabla_{\eta}^{r}\big(\lambda{}_{\delta}{}^{k}\big)\big(\nabla_{a}\lambda{}_{\gamma k}\big)\\
&+\frac{15}{64}W^{-4}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{i}\lambda{}^{\delta j}\lambda{}_{\delta}{}^{k}\nabla_{\eta}^{r}\big(\nabla_{a}\lambda{}_{\gamma k}\big) -\frac{15}{64}\nabla_{\eta}^{r}\big(W^{-4}\big)(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{j}\lambda{}^{\delta i}\lambda{}_{\delta}{}^{k}\big(\nabla_{a}\lambda{}_{\gamma k}\big)\\
&-\frac{15}{64}W^{-4}(\Gamma{}^{a}){}^{\beta \gamma}\nabla_{\eta}^{r}\big(\lambda{}_{\beta}{}^{j}\big)\lambda{}^{\delta i}\lambda{}_{\delta}{}^{k}\big(\nabla_{a}\lambda{}_{\gamma k}\big) +\frac{15}{64}W^{-4}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{j}\nabla_{\eta}^{r}\big(\lambda{}^{\delta i}\big)\lambda{}_{\delta}{}^{k}\big(\nabla_{a}\lambda{}_{\gamma k}\big)\\
&-\frac{15}{64}W^{-4}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{j}\lambda{}^{\delta i}\nabla_{\eta}^{r}\big(\lambda{}_{\delta}{}^{k}\big)\big(\nabla_{a}\lambda{}_{\gamma k}\big) +\frac{15}{64}W^{-4}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{j}\lambda{}^{\delta i}\lambda{}_{\delta}{}^{k}\nabla_{\eta}^{r}\big(\nabla_{a}\lambda{}_{\gamma k}\big)
\end{aligned}
\tag{S3-H4.11-a}
```

Insert the elementary source identities and the applicable commutators (S3-11)–(S3-14), distribute the vector product rules, and contract only index-raising metrics. The resulting contribution is

```math
\begin{aligned}
\left.\nabla_\eta^rH^{ij}\right|_{\mathrm{H4.11}}=&\frac{15i}{16}W^{-5}\lambda{}_{\eta}{}^{r}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{i}\lambda{}^{\delta j}\lambda{}_{\delta}{}^{k}\big(\nabla_{a}\lambda{}_{\gamma k}\big) +\frac{15}{32}W^{-4}(\Gamma{}^{a}){}^{\beta \gamma}\varepsilon{}^{r i}F{}_{\eta \beta}\lambda{}^{\delta j}\lambda{}_{\delta}{}^{k}\big(\nabla_{a}\lambda{}_{\gamma k}\big)\\
&+\frac{15}{32}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}\varepsilon{}^{r i}W{}_{\eta \beta}\lambda{}^{\delta j}\lambda{}_{\delta}{}^{k}\big(\nabla_{a}\lambda{}_{\gamma k}\big) +\frac{15}{64}W^{-4}(\Gamma{}^{a}){}_{\eta}{}^{\beta}X{}^{r i}\lambda{}^{\gamma j}\lambda{}_{\gamma}{}^{k}\big(\nabla_{a}\lambda{}_{\beta k}\big)\\
&+\frac{15}{64}W^{-4}(\Gamma{}^{a}){}^{\beta \gamma}\varepsilon{}^{r i}(\Gamma{}^{b}){}_{\eta \beta}\big(\nabla_{b}W\big)\lambda{}^{\delta j}\lambda{}_{\delta}{}^{k}\big(\nabla_{a}\lambda{}_{\gamma k}\big) -\frac{15}{32}W^{-4}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{i}\varepsilon{}^{r j}F{}_{\eta}{}^{\delta}\lambda{}_{\delta}{}^{k}\big(\nabla_{a}\lambda{}_{\gamma k}\big)\\
&-\frac{15}{32}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{i}\varepsilon{}^{r j}W{}_{\eta}{}^{\delta}\lambda{}_{\delta}{}^{k}\big(\nabla_{a}\lambda{}_{\gamma k}\big) +\frac{15}{64}W^{-4}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{i}X{}^{r j}\lambda{}_{\eta}{}^{k}\big(\nabla_{a}\lambda{}_{\gamma k}\big)\\
&-\frac{15}{64}W^{-4}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{i}\varepsilon{}^{r j}(\Gamma{}^{b}){}_{\eta}{}^{\delta}\big(\nabla_{b}W\big)\lambda{}_{\delta}{}^{k}\big(\nabla_{a}\lambda{}_{\gamma k}\big) +\frac{15}{32}W^{-4}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{i}\lambda{}^{\delta j}F{}_{\eta \delta}\big(\nabla_{a}\lambda{}_{\gamma}{}^{r}\big)\\
&+\frac{15}{32}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{i}\lambda{}^{\delta j}W{}_{\eta \delta}\big(\nabla_{a}\lambda{}_{\gamma}{}^{r}\big) +\frac{15}{64}W^{-4}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{i}\lambda{}_{\eta}{}^{j}X{}^{r k}\big(\nabla_{a}\lambda{}_{\gamma k}\big)\\
&+\frac{15}{64}W^{-4}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{i}\lambda{}^{\delta j}(\Gamma{}^{b}){}_{\eta \delta}\big(\nabla_{b}W\big)\big(\nabla_{a}\lambda{}_{\gamma}{}^{r}\big) +\frac{15}{32}W^{-4}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{i}\lambda{}^{\delta j}\lambda{}_{\delta}{}^{r}\big(\nabla_{a}F{}_{\eta \gamma}\big)\\
&+\frac{15}{32}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{i}\lambda{}^{\delta j}\lambda{}_{\delta}{}^{r}\big(\nabla_{a}W{}_{\eta \gamma}\big) +\frac{15}{32}W^{-4}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{i}\lambda{}^{\delta j}\lambda{}_{\delta}{}^{r}W{}_{\eta \gamma}\big(\nabla_{a}W\big)\\
&-\frac{15}{64}W^{-4}(\Gamma{}^{a}){}^{\beta}{}_{\eta}\lambda{}_{\beta}{}^{i}\lambda{}^{\gamma j}\lambda{}_{\gamma}{}^{k}\big(\nabla_{a}X{}^{r}{}_{k}\big) +\frac{15}{64}W^{-4}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{i}\lambda{}^{\delta j}\lambda{}_{\delta}{}^{r}(\Gamma{}^{b}){}_{\eta \gamma}\big(\nabla_{a}\nabla_{b}W\big)\\
&+\frac{15}{32}W^{-4}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{i}\lambda{}^{\delta j}\lambda{}_{\delta}{}^{r}\mathcal T{}_{a \eta}{}^{\rho}F{}_{\rho \gamma} +\frac{15}{32}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{i}\lambda{}^{\delta j}\lambda{}_{\delta}{}^{r}\mathcal T{}_{a \eta}{}^{\rho}W{}_{\rho \gamma}\\
&-\frac{15}{64}W^{-4}(\Gamma{}^{a}){}^{\beta}{}_{\gamma}\lambda{}_{\beta}{}^{i}\lambda{}^{\delta j}\lambda{}_{\delta}{}^{k}\mathcal T{}_{a \eta}{}^{\gamma}X{}^{r}{}_{k} +\frac{15}{64}W^{-4}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{i}\lambda{}^{\delta j}\lambda{}_{\delta}{}^{r}\mathcal T{}_{a \eta}{}^{\rho}(\Gamma{}^{b}){}_{\rho \gamma}\big(\nabla_{b}W\big)\\
&+\frac{15}{128}W^{-4}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{i}\lambda{}^{\delta j}\lambda{}_{\delta}{}^{k}\mathcal R(M){}_{a \eta}{}^{r b c}(\Sigma{}_{b c}){}_{\gamma}{}^{\rho}\lambda{}_{\rho k} +\frac{45}{128}W^{-4}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{i}\lambda{}^{\delta j}\lambda{}_{\delta}{}^{k}\mathcal R(\mathbb D){}_{a \eta}{}^{r}\lambda{}_{\gamma k}\\
&+\frac{15}{128}W^{-4}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{i}\lambda{}^{\delta j}\lambda{}_{\delta k}\mathcal R(J){}_{a \eta}{}^{r k l}\lambda{}_{\gamma l} +\frac{15}{128}W^{-4}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{i}\lambda{}^{\delta j}\lambda{}_{\delta k}\mathcal R(J){}_{a \eta}{}^{r l k}\lambda{}_{\gamma l}\\
&+\frac{15i}{32}W^{-3}(\Gamma{}^{a}){}^{\beta}{}_{\gamma}\lambda{}_{\beta}{}^{i}\lambda{}^{\delta j}\lambda{}_{\delta k}\mathcal R(S){}_{a \eta}{}^{r \gamma k} +\frac{15i}{16}W^{-5}\lambda{}_{\eta}{}^{r}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{j}\lambda{}^{\delta i}\lambda{}_{\delta}{}^{k}\big(\nabla_{a}\lambda{}_{\gamma k}\big)\\
&+\frac{15}{32}W^{-4}(\Gamma{}^{a}){}^{\beta \gamma}\varepsilon{}^{r j}F{}_{\eta \beta}\lambda{}^{\delta i}\lambda{}_{\delta}{}^{k}\big(\nabla_{a}\lambda{}_{\gamma k}\big) +\frac{15}{32}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}\varepsilon{}^{r j}W{}_{\eta \beta}\lambda{}^{\delta i}\lambda{}_{\delta}{}^{k}\big(\nabla_{a}\lambda{}_{\gamma k}\big)\\
&+\frac{15}{64}W^{-4}(\Gamma{}^{a}){}_{\eta}{}^{\beta}X{}^{r j}\lambda{}^{\gamma i}\lambda{}_{\gamma}{}^{k}\big(\nabla_{a}\lambda{}_{\beta k}\big) +\frac{15}{64}W^{-4}(\Gamma{}^{a}){}^{\beta \gamma}\varepsilon{}^{r j}(\Gamma{}^{b}){}_{\eta \beta}\big(\nabla_{b}W\big)\lambda{}^{\delta i}\lambda{}_{\delta}{}^{k}\big(\nabla_{a}\lambda{}_{\gamma k}\big)\\
&-\frac{15}{32}W^{-4}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{j}\varepsilon{}^{r i}F{}_{\eta}{}^{\delta}\lambda{}_{\delta}{}^{k}\big(\nabla_{a}\lambda{}_{\gamma k}\big) -\frac{15}{32}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{j}\varepsilon{}^{r i}W{}_{\eta}{}^{\delta}\lambda{}_{\delta}{}^{k}\big(\nabla_{a}\lambda{}_{\gamma k}\big)\\
&+\frac{15}{64}W^{-4}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{j}X{}^{r i}\lambda{}_{\eta}{}^{k}\big(\nabla_{a}\lambda{}_{\gamma k}\big) -\frac{15}{64}W^{-4}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{j}\varepsilon{}^{r i}(\Gamma{}^{b}){}_{\eta}{}^{\delta}\big(\nabla_{b}W\big)\lambda{}_{\delta}{}^{k}\big(\nabla_{a}\lambda{}_{\gamma k}\big)\\
&+\frac{15}{32}W^{-4}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{j}\lambda{}^{\delta i}F{}_{\eta \delta}\big(\nabla_{a}\lambda{}_{\gamma}{}^{r}\big) +\frac{15}{32}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{j}\lambda{}^{\delta i}W{}_{\eta \delta}\big(\nabla_{a}\lambda{}_{\gamma}{}^{r}\big)\\
&+\frac{15}{64}W^{-4}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{j}\lambda{}_{\eta}{}^{i}X{}^{r k}\big(\nabla_{a}\lambda{}_{\gamma k}\big) +\frac{15}{64}W^{-4}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{j}\lambda{}^{\delta i}(\Gamma{}^{b}){}_{\eta \delta}\big(\nabla_{b}W\big)\big(\nabla_{a}\lambda{}_{\gamma}{}^{r}\big)\\
&+\frac{15}{32}W^{-4}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{j}\lambda{}^{\delta i}\lambda{}_{\delta}{}^{r}\big(\nabla_{a}F{}_{\eta \gamma}\big) +\frac{15}{32}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{j}\lambda{}^{\delta i}\lambda{}_{\delta}{}^{r}\big(\nabla_{a}W{}_{\eta \gamma}\big)\\
&+\frac{15}{32}W^{-4}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{j}\lambda{}^{\delta i}\lambda{}_{\delta}{}^{r}W{}_{\eta \gamma}\big(\nabla_{a}W\big) -\frac{15}{64}W^{-4}(\Gamma{}^{a}){}^{\beta}{}_{\eta}\lambda{}_{\beta}{}^{j}\lambda{}^{\gamma i}\lambda{}_{\gamma}{}^{k}\big(\nabla_{a}X{}^{r}{}_{k}\big)\\
&+\frac{15}{64}W^{-4}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{j}\lambda{}^{\delta i}\lambda{}_{\delta}{}^{r}(\Gamma{}^{b}){}_{\eta \gamma}\big(\nabla_{a}\nabla_{b}W\big) +\frac{15}{32}W^{-4}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{j}\lambda{}^{\delta i}\lambda{}_{\delta}{}^{r}\mathcal T{}_{a \eta}{}^{\rho}F{}_{\rho \gamma}\\
&+\frac{15}{32}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{j}\lambda{}^{\delta i}\lambda{}_{\delta}{}^{r}\mathcal T{}_{a \eta}{}^{\rho}W{}_{\rho \gamma} -\frac{15}{64}W^{-4}(\Gamma{}^{a}){}^{\beta}{}_{\gamma}\lambda{}_{\beta}{}^{j}\lambda{}^{\delta i}\lambda{}_{\delta}{}^{k}\mathcal T{}_{a \eta}{}^{\gamma}X{}^{r}{}_{k}\\
&+\frac{15}{64}W^{-4}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{j}\lambda{}^{\delta i}\lambda{}_{\delta}{}^{r}\mathcal T{}_{a \eta}{}^{\rho}(\Gamma{}^{b}){}_{\rho \gamma}\big(\nabla_{b}W\big) +\frac{15}{128}W^{-4}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{j}\lambda{}^{\delta i}\lambda{}_{\delta}{}^{k}\mathcal R(M){}_{a \eta}{}^{r b c}(\Sigma{}_{b c}){}_{\gamma}{}^{\rho}\lambda{}_{\rho k}\\
&+\frac{45}{128}W^{-4}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{j}\lambda{}^{\delta i}\lambda{}_{\delta}{}^{k}\mathcal R(\mathbb D){}_{a \eta}{}^{r}\lambda{}_{\gamma k} +\frac{15}{128}W^{-4}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{j}\lambda{}^{\delta i}\lambda{}_{\delta k}\mathcal R(J){}_{a \eta}{}^{r k l}\lambda{}_{\gamma l}\\
&+\frac{15}{128}W^{-4}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{j}\lambda{}^{\delta i}\lambda{}_{\delta k}\mathcal R(J){}_{a \eta}{}^{r l k}\lambda{}_{\gamma l} +\frac{15i}{32}W^{-3}(\Gamma{}^{a}){}^{\beta}{}_{\gamma}\lambda{}_{\beta}{}^{j}\lambda{}^{\delta i}\lambda{}_{\delta k}\mathcal R(S){}_{a \eta}{}^{r \gamma k}
\end{aligned}
\tag{S3-H4.11-b}
```

**Check for H4.11:** all 54 written summands have weight $`7/2`$, odd parity and the same free indices $`\eta;r,i,j`$. Dummy labels are paired. The coefficient $`1/3`$ and the two external epsilons are applied once, when collecting the spinor.

#### Input H4.12

The calculated input is

```math
\left.H^{ij}\right|_{\mathrm{H4.12}}=W^{-4}\big(-\frac{15}{64}(\Gamma^a)^{\alpha\beta}\lambda^{\rho i}\lambda_\rho^j\lambda_\alpha^k\nabla_a\lambda_{\beta k}\big).
\tag{S3-H4.12-input}
```

Expand each written SU(2) average with weight $`1/2`$ before applying the left derivative.

Apply the product rule (S3-09), in the displayed factor order:

```math
\begin{aligned}
\left.\nabla_\eta^rH^{ij}\right|_{\mathrm{H4.12}}=&-\frac{15}{64}\nabla_{\eta}^{r}\big(W^{-4}\big)(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}^{\delta i}\lambda{}_{\delta}{}^{j}\lambda{}_{\beta}{}^{k}\big(\nabla_{a}\lambda{}_{\gamma k}\big) -\frac{15}{64}W^{-4}(\Gamma{}^{a}){}^{\beta \gamma}\nabla_{\eta}^{r}\big(\lambda{}^{\delta i}\big)\lambda{}_{\delta}{}^{j}\lambda{}_{\beta}{}^{k}\big(\nabla_{a}\lambda{}_{\gamma k}\big)\\
&+\frac{15}{64}W^{-4}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}^{\delta i}\nabla_{\eta}^{r}\big(\lambda{}_{\delta}{}^{j}\big)\lambda{}_{\beta}{}^{k}\big(\nabla_{a}\lambda{}_{\gamma k}\big) -\frac{15}{64}W^{-4}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}^{\delta i}\lambda{}_{\delta}{}^{j}\nabla_{\eta}^{r}\big(\lambda{}_{\beta}{}^{k}\big)\big(\nabla_{a}\lambda{}_{\gamma k}\big)\\
&+\frac{15}{64}W^{-4}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}^{\delta i}\lambda{}_{\delta}{}^{j}\lambda{}_{\beta}{}^{k}\nabla_{\eta}^{r}\big(\nabla_{a}\lambda{}_{\gamma k}\big)
\end{aligned}
\tag{S3-H4.12-a}
```

Insert the elementary source identities and the applicable commutators (S3-11)–(S3-14), distribute the vector product rules, and contract only index-raising metrics. The resulting contribution is

```math
\begin{aligned}
\left.\nabla_\eta^rH^{ij}\right|_{\mathrm{H4.12}}=&\frac{15i}{16}W^{-5}\lambda{}_{\eta}{}^{r}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}^{\delta i}\lambda{}_{\delta}{}^{j}\lambda{}_{\beta}{}^{k}\big(\nabla_{a}\lambda{}_{\gamma k}\big) +\frac{15}{32}W^{-4}(\Gamma{}^{a}){}^{\beta \gamma}\varepsilon{}^{r i}F{}_{\eta}{}^{\delta}\lambda{}_{\delta}{}^{j}\lambda{}_{\beta}{}^{k}\big(\nabla_{a}\lambda{}_{\gamma k}\big)\\
&+\frac{15}{32}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}\varepsilon{}^{r i}W{}_{\eta}{}^{\delta}\lambda{}_{\delta}{}^{j}\lambda{}_{\beta}{}^{k}\big(\nabla_{a}\lambda{}_{\gamma k}\big) -\frac{15}{64}W^{-4}(\Gamma{}^{a}){}^{\beta \gamma}X{}^{r i}\lambda{}_{\eta}{}^{j}\lambda{}_{\beta}{}^{k}\big(\nabla_{a}\lambda{}_{\gamma k}\big)\\
&+\frac{15}{64}W^{-4}(\Gamma{}^{a}){}^{\beta \gamma}\varepsilon{}^{r i}(\Gamma{}^{b}){}_{\eta}{}^{\delta}\big(\nabla_{b}W\big)\lambda{}_{\delta}{}^{j}\lambda{}_{\beta}{}^{k}\big(\nabla_{a}\lambda{}_{\gamma k}\big) -\frac{15}{32}W^{-4}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}^{\delta i}\varepsilon{}^{r j}F{}_{\eta \delta}\lambda{}_{\beta}{}^{k}\big(\nabla_{a}\lambda{}_{\gamma k}\big)\\
&-\frac{15}{32}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}^{\delta i}\varepsilon{}^{r j}W{}_{\eta \delta}\lambda{}_{\beta}{}^{k}\big(\nabla_{a}\lambda{}_{\gamma k}\big) -\frac{15}{64}W^{-4}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\eta}{}^{i}X{}^{r j}\lambda{}_{\beta}{}^{k}\big(\nabla_{a}\lambda{}_{\gamma k}\big)\\
&-\frac{15}{64}W^{-4}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}^{\delta i}\varepsilon{}^{r j}(\Gamma{}^{b}){}_{\eta \delta}\big(\nabla_{b}W\big)\lambda{}_{\beta}{}^{k}\big(\nabla_{a}\lambda{}_{\gamma k}\big) +\frac{15}{32}W^{-4}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}^{\delta i}\lambda{}_{\delta}{}^{j}F{}_{\eta \beta}\big(\nabla_{a}\lambda{}_{\gamma}{}^{r}\big)\\
&+\frac{15}{32}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}^{\delta i}\lambda{}_{\delta}{}^{j}W{}_{\eta \beta}\big(\nabla_{a}\lambda{}_{\gamma}{}^{r}\big) +\frac{15}{64}W^{-4}(\Gamma{}^{a}){}_{\eta}{}^{\beta}\lambda{}^{\gamma i}\lambda{}_{\gamma}{}^{j}X{}^{r k}\big(\nabla_{a}\lambda{}_{\beta k}\big)\\
&+\frac{15}{64}W^{-4}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}^{\delta i}\lambda{}_{\delta}{}^{j}(\Gamma{}^{b}){}_{\eta \beta}\big(\nabla_{b}W\big)\big(\nabla_{a}\lambda{}_{\gamma}{}^{r}\big) +\frac{15}{32}W^{-4}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}^{\delta i}\lambda{}_{\delta}{}^{j}\lambda{}_{\beta}{}^{r}\big(\nabla_{a}F{}_{\eta \gamma}\big)\\
&+\frac{15}{32}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}^{\delta i}\lambda{}_{\delta}{}^{j}\lambda{}_{\beta}{}^{r}\big(\nabla_{a}W{}_{\eta \gamma}\big) +\frac{15}{32}W^{-4}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}^{\delta i}\lambda{}_{\delta}{}^{j}\lambda{}_{\beta}{}^{r}W{}_{\eta \gamma}\big(\nabla_{a}W\big)\\
&-\frac{15}{64}W^{-4}(\Gamma{}^{a}){}^{\beta}{}_{\eta}\lambda{}^{\gamma i}\lambda{}_{\gamma}{}^{j}\lambda{}_{\beta}{}^{k}\big(\nabla_{a}X{}^{r}{}_{k}\big) +\frac{15}{64}W^{-4}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}^{\delta i}\lambda{}_{\delta}{}^{j}\lambda{}_{\beta}{}^{r}(\Gamma{}^{b}){}_{\eta \gamma}\big(\nabla_{a}\nabla_{b}W\big)\\
&+\frac{15}{32}W^{-4}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}^{\delta i}\lambda{}_{\delta}{}^{j}\lambda{}_{\beta}{}^{r}\mathcal T{}_{a \eta}{}^{\rho}F{}_{\rho \gamma} +\frac{15}{32}W^{-3}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}^{\delta i}\lambda{}_{\delta}{}^{j}\lambda{}_{\beta}{}^{r}\mathcal T{}_{a \eta}{}^{\rho}W{}_{\rho \gamma}\\
&-\frac{15}{64}W^{-4}(\Gamma{}^{a}){}^{\beta}{}_{\gamma}\lambda{}^{\delta i}\lambda{}_{\delta}{}^{j}\lambda{}_{\beta}{}^{k}\mathcal T{}_{a \eta}{}^{\gamma}X{}^{r}{}_{k} +\frac{15}{64}W^{-4}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}^{\delta i}\lambda{}_{\delta}{}^{j}\lambda{}_{\beta}{}^{r}\mathcal T{}_{a \eta}{}^{\rho}(\Gamma{}^{b}){}_{\rho \gamma}\big(\nabla_{b}W\big)\\
&+\frac{15}{128}W^{-4}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}^{\delta i}\lambda{}_{\delta}{}^{j}\lambda{}_{\beta}{}^{k}\mathcal R(M){}_{a \eta}{}^{r b c}(\Sigma{}_{b c}){}_{\gamma}{}^{\rho}\lambda{}_{\rho k} +\frac{45}{128}W^{-4}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}^{\delta i}\lambda{}_{\delta}{}^{j}\lambda{}_{\beta}{}^{k}\mathcal R(\mathbb D){}_{a \eta}{}^{r}\lambda{}_{\gamma k}\\
&+\frac{15}{128}W^{-4}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}^{\delta i}\lambda{}_{\delta}{}^{j}\lambda{}_{\beta k}\mathcal R(J){}_{a \eta}{}^{r k l}\lambda{}_{\gamma l} +\frac{15}{128}W^{-4}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}^{\delta i}\lambda{}_{\delta}{}^{j}\lambda{}_{\beta k}\mathcal R(J){}_{a \eta}{}^{r l k}\lambda{}_{\gamma l}\\
&+\frac{15i}{32}W^{-3}(\Gamma{}^{a}){}^{\beta}{}_{\gamma}\lambda{}^{\delta i}\lambda{}_{\delta}{}^{j}\lambda{}_{\beta k}\mathcal R(S){}_{a \eta}{}^{r \gamma k}
\end{aligned}
\tag{S3-H4.12-b}
```

**Check for H4.12:** all 27 written summands have weight $`7/2`$, odd parity and the same free indices $`\eta;r,i,j`$. Dummy labels are paired. The coefficient $`1/3`$ and the two external epsilons are applied once, when collecting the spinor.

#### Input H4.13

The calculated input is

```math
\left.H^{ij}\right|_{\mathrm{H4.13}}=W^{-4}\big(\frac9{32}(\Sigma_{ab})^{\alpha\beta}W^{ab}\lambda_\alpha^{(i}\lambda^{\rho j)}\lambda_\beta^k\lambda_{\rho k}\big).
\tag{S3-H4.13-input}
```

Expand each written SU(2) average with weight $`1/2`$ before applying the left derivative.

Apply the product rule (S3-09), in the displayed factor order:

```math
\begin{aligned}
\left.\nabla_\eta^rH^{ij}\right|_{\mathrm{H4.13}}=&\frac{9}{64}\nabla_{\eta}^{r}\big(W^{-4}\big)(\Sigma{}_{a b}){}^{\beta \gamma}W{}^{a b}\lambda{}_{\beta}{}^{i}\lambda{}^{\delta j}\lambda{}_{\gamma}{}^{k}\lambda{}_{\delta k} +\frac{9}{64}W^{-4}(\Sigma{}_{a b}){}^{\beta \gamma}\nabla_{\eta}^{r}\big(W{}^{a b}\big)\lambda{}_{\beta}{}^{i}\lambda{}^{\delta j}\lambda{}_{\gamma}{}^{k}\lambda{}_{\delta k}\\
&+\frac{9}{64}W^{-4}(\Sigma{}_{a b}){}^{\beta \gamma}W{}^{a b}\nabla_{\eta}^{r}\big(\lambda{}_{\beta}{}^{i}\big)\lambda{}^{\delta j}\lambda{}_{\gamma}{}^{k}\lambda{}_{\delta k} -\frac{9}{64}W^{-4}(\Sigma{}_{a b}){}^{\beta \gamma}W{}^{a b}\lambda{}_{\beta}{}^{i}\nabla_{\eta}^{r}\big(\lambda{}^{\delta j}\big)\lambda{}_{\gamma}{}^{k}\lambda{}_{\delta k}\\
&+\frac{9}{64}W^{-4}(\Sigma{}_{a b}){}^{\beta \gamma}W{}^{a b}\lambda{}_{\beta}{}^{i}\lambda{}^{\delta j}\nabla_{\eta}^{r}\big(\lambda{}_{\gamma}{}^{k}\big)\lambda{}_{\delta k} -\frac{9}{64}W^{-4}(\Sigma{}_{a b}){}^{\beta \gamma}W{}^{a b}\lambda{}_{\beta}{}^{i}\lambda{}^{\delta j}\lambda{}_{\gamma}{}^{k}\nabla_{\eta}^{r}\big(\lambda{}_{\delta k}\big)\\
&+\frac{9}{64}\nabla_{\eta}^{r}\big(W^{-4}\big)(\Sigma{}_{a b}){}^{\beta \gamma}W{}^{a b}\lambda{}_{\beta}{}^{j}\lambda{}^{\delta i}\lambda{}_{\gamma}{}^{k}\lambda{}_{\delta k} +\frac{9}{64}W^{-4}(\Sigma{}_{a b}){}^{\beta \gamma}\nabla_{\eta}^{r}\big(W{}^{a b}\big)\lambda{}_{\beta}{}^{j}\lambda{}^{\delta i}\lambda{}_{\gamma}{}^{k}\lambda{}_{\delta k}\\
&+\frac{9}{64}W^{-4}(\Sigma{}_{a b}){}^{\beta \gamma}W{}^{a b}\nabla_{\eta}^{r}\big(\lambda{}_{\beta}{}^{j}\big)\lambda{}^{\delta i}\lambda{}_{\gamma}{}^{k}\lambda{}_{\delta k} -\frac{9}{64}W^{-4}(\Sigma{}_{a b}){}^{\beta \gamma}W{}^{a b}\lambda{}_{\beta}{}^{j}\nabla_{\eta}^{r}\big(\lambda{}^{\delta i}\big)\lambda{}_{\gamma}{}^{k}\lambda{}_{\delta k}\\
&+\frac{9}{64}W^{-4}(\Sigma{}_{a b}){}^{\beta \gamma}W{}^{a b}\lambda{}_{\beta}{}^{j}\lambda{}^{\delta i}\nabla_{\eta}^{r}\big(\lambda{}_{\gamma}{}^{k}\big)\lambda{}_{\delta k} -\frac{9}{64}W^{-4}(\Sigma{}_{a b}){}^{\beta \gamma}W{}^{a b}\lambda{}_{\beta}{}^{j}\lambda{}^{\delta i}\lambda{}_{\gamma}{}^{k}\nabla_{\eta}^{r}\big(\lambda{}_{\delta k}\big)
\end{aligned}
\tag{S3-H4.13-a}
```

Insert the elementary source identities and the applicable commutators (S3-11)–(S3-14), distribute the vector product rules, and contract only index-raising metrics. The resulting contribution is

```math
\begin{aligned}
\left.\nabla_\eta^rH^{ij}\right|_{\mathrm{H4.13}}=&-\frac{9i}{16}W^{-5}\lambda{}_{\eta}{}^{r}(\Sigma{}_{a b}){}^{\beta \gamma}W{}^{a b}\lambda{}_{\beta}{}^{i}\lambda{}^{\delta j}\lambda{}_{\gamma}{}^{k}\lambda{}_{\delta k} +\frac{9}{64}W^{-4}(\Sigma{}_{a b}){}^{\beta \gamma}(\Sigma{}^{a b}){}^{\delta \rho}W{}_{\eta \delta \rho}{}^{r}\lambda{}_{\beta}{}^{i}\lambda{}^{\sigma j}\lambda{}_{\gamma}{}^{k}\lambda{}_{\sigma k}\\
&+\frac{9}{128}W^{-4}(\Sigma{}_{a b}){}^{\beta \gamma}(\Sigma{}^{a b}){}_{\eta}{}^{\delta}X{}_{\delta}{}^{r}\lambda{}_{\beta}{}^{i}\lambda{}^{\rho j}\lambda{}_{\gamma}{}^{k}\lambda{}_{\rho k} +\frac{9}{128}W^{-4}(\Sigma{}_{a b}){}^{\beta \gamma}(\Sigma{}^{a b}){}^{\delta}{}_{\eta}X{}_{\delta}{}^{r}\lambda{}_{\beta}{}^{i}\lambda{}^{\rho j}\lambda{}_{\gamma}{}^{k}\lambda{}_{\rho k}\\
&-\frac{9}{32}W^{-4}(\Sigma{}_{a b}){}^{\beta \gamma}W{}^{a b}\varepsilon{}^{r i}F{}_{\eta \beta}\lambda{}^{\delta j}\lambda{}_{\gamma}{}^{k}\lambda{}_{\delta k} -\frac{9}{32}W^{-3}(\Sigma{}_{a b}){}^{\beta \gamma}W{}^{a b}\varepsilon{}^{r i}W{}_{\eta \beta}\lambda{}^{\delta j}\lambda{}_{\gamma}{}^{k}\lambda{}_{\delta k}\\
&-\frac{9}{64}W^{-4}(\Sigma{}_{a b}){}_{\eta}{}^{\beta}W{}^{a b}X{}^{r i}\lambda{}^{\gamma j}\lambda{}_{\beta}{}^{k}\lambda{}_{\gamma k} -\frac{9}{64}W^{-4}(\Sigma{}_{a b}){}^{\beta \gamma}W{}^{a b}\varepsilon{}^{r i}(\Gamma{}^{c}){}_{\eta \beta}\big(\nabla_{c}W\big)\lambda{}^{\delta j}\lambda{}_{\gamma}{}^{k}\lambda{}_{\delta k}\\
&+\frac{9}{32}W^{-4}(\Sigma{}_{a b}){}^{\beta \gamma}W{}^{a b}\lambda{}_{\beta}{}^{i}\varepsilon{}^{r j}F{}_{\eta}{}^{\delta}\lambda{}_{\gamma}{}^{k}\lambda{}_{\delta k} +\frac{9}{32}W^{-3}(\Sigma{}_{a b}){}^{\beta \gamma}W{}^{a b}\lambda{}_{\beta}{}^{i}\varepsilon{}^{r j}W{}_{\eta}{}^{\delta}\lambda{}_{\gamma}{}^{k}\lambda{}_{\delta k}\\
&-\frac{9}{64}W^{-4}(\Sigma{}_{a b}){}^{\beta \gamma}W{}^{a b}\lambda{}_{\beta}{}^{i}X{}^{r j}\lambda{}_{\gamma}{}^{k}\lambda{}_{\eta k} +\frac{9}{64}W^{-4}(\Sigma{}_{a b}){}^{\beta \gamma}W{}^{a b}\lambda{}_{\beta}{}^{i}\varepsilon{}^{r j}(\Gamma{}^{c}){}_{\eta}{}^{\delta}\big(\nabla_{c}W\big)\lambda{}_{\gamma}{}^{k}\lambda{}_{\delta k}\\
&-\frac{9}{32}W^{-4}(\Sigma{}_{a b}){}^{\beta \gamma}W{}^{a b}\lambda{}_{\beta}{}^{i}\lambda{}^{\delta j}F{}_{\eta \gamma}\lambda{}_{\delta}{}^{r} -\frac{9}{32}W^{-3}(\Sigma{}_{a b}){}^{\beta \gamma}W{}^{a b}\lambda{}_{\beta}{}^{i}\lambda{}^{\delta j}W{}_{\eta \gamma}\lambda{}_{\delta}{}^{r}\\
&-\frac{9}{64}W^{-4}(\Sigma{}_{a b}){}^{\beta}{}_{\eta}W{}^{a b}\lambda{}_{\beta}{}^{i}\lambda{}^{\gamma j}X{}^{r k}\lambda{}_{\gamma k} -\frac{9}{64}W^{-4}(\Sigma{}_{a b}){}^{\beta \gamma}W{}^{a b}\lambda{}_{\beta}{}^{i}\lambda{}^{\delta j}(\Gamma{}^{c}){}_{\eta \gamma}\big(\nabla_{c}W\big)\lambda{}_{\delta}{}^{r}\\
&-\frac{9}{32}W^{-4}(\Sigma{}_{a b}){}^{\beta \gamma}W{}^{a b}\lambda{}_{\beta}{}^{i}\lambda{}^{\delta j}\lambda{}_{\gamma}{}^{r}F{}_{\eta \delta} -\frac{9}{32}W^{-3}(\Sigma{}_{a b}){}^{\beta \gamma}W{}^{a b}\lambda{}_{\beta}{}^{i}\lambda{}^{\delta j}\lambda{}_{\gamma}{}^{r}W{}_{\eta \delta}\\
&+\frac{9}{64}W^{-4}(\Sigma{}_{a b}){}^{\beta \gamma}W{}^{a b}\lambda{}_{\beta}{}^{i}\lambda{}_{\eta}{}^{j}\lambda{}_{\gamma}{}^{k}X{}^{r}{}_{k} -\frac{9}{64}W^{-4}(\Sigma{}_{a b}){}^{\beta \gamma}W{}^{a b}\lambda{}_{\beta}{}^{i}\lambda{}^{\delta j}\lambda{}_{\gamma}{}^{r}(\Gamma{}^{c}){}_{\eta \delta}\big(\nabla_{c}W\big)\\
&-\frac{9i}{16}W^{-5}\lambda{}_{\eta}{}^{r}(\Sigma{}_{a b}){}^{\beta \gamma}W{}^{a b}\lambda{}_{\beta}{}^{j}\lambda{}^{\delta i}\lambda{}_{\gamma}{}^{k}\lambda{}_{\delta k} +\frac{9}{64}W^{-4}(\Sigma{}_{a b}){}^{\beta \gamma}(\Sigma{}^{a b}){}^{\delta \rho}W{}_{\eta \delta \rho}{}^{r}\lambda{}_{\beta}{}^{j}\lambda{}^{\sigma i}\lambda{}_{\gamma}{}^{k}\lambda{}_{\sigma k}\\
&+\frac{9}{128}W^{-4}(\Sigma{}_{a b}){}^{\beta \gamma}(\Sigma{}^{a b}){}_{\eta}{}^{\delta}X{}_{\delta}{}^{r}\lambda{}_{\beta}{}^{j}\lambda{}^{\rho i}\lambda{}_{\gamma}{}^{k}\lambda{}_{\rho k} +\frac{9}{128}W^{-4}(\Sigma{}_{a b}){}^{\beta \gamma}(\Sigma{}^{a b}){}^{\delta}{}_{\eta}X{}_{\delta}{}^{r}\lambda{}_{\beta}{}^{j}\lambda{}^{\rho i}\lambda{}_{\gamma}{}^{k}\lambda{}_{\rho k}\\
&-\frac{9}{32}W^{-4}(\Sigma{}_{a b}){}^{\beta \gamma}W{}^{a b}\varepsilon{}^{r j}F{}_{\eta \beta}\lambda{}^{\delta i}\lambda{}_{\gamma}{}^{k}\lambda{}_{\delta k} -\frac{9}{32}W^{-3}(\Sigma{}_{a b}){}^{\beta \gamma}W{}^{a b}\varepsilon{}^{r j}W{}_{\eta \beta}\lambda{}^{\delta i}\lambda{}_{\gamma}{}^{k}\lambda{}_{\delta k}\\
&-\frac{9}{64}W^{-4}(\Sigma{}_{a b}){}_{\eta}{}^{\beta}W{}^{a b}X{}^{r j}\lambda{}^{\gamma i}\lambda{}_{\beta}{}^{k}\lambda{}_{\gamma k} -\frac{9}{64}W^{-4}(\Sigma{}_{a b}){}^{\beta \gamma}W{}^{a b}\varepsilon{}^{r j}(\Gamma{}^{c}){}_{\eta \beta}\big(\nabla_{c}W\big)\lambda{}^{\delta i}\lambda{}_{\gamma}{}^{k}\lambda{}_{\delta k}\\
&+\frac{9}{32}W^{-4}(\Sigma{}_{a b}){}^{\beta \gamma}W{}^{a b}\lambda{}_{\beta}{}^{j}\varepsilon{}^{r i}F{}_{\eta}{}^{\delta}\lambda{}_{\gamma}{}^{k}\lambda{}_{\delta k} +\frac{9}{32}W^{-3}(\Sigma{}_{a b}){}^{\beta \gamma}W{}^{a b}\lambda{}_{\beta}{}^{j}\varepsilon{}^{r i}W{}_{\eta}{}^{\delta}\lambda{}_{\gamma}{}^{k}\lambda{}_{\delta k}\\
&-\frac{9}{64}W^{-4}(\Sigma{}_{a b}){}^{\beta \gamma}W{}^{a b}\lambda{}_{\beta}{}^{j}X{}^{r i}\lambda{}_{\gamma}{}^{k}\lambda{}_{\eta k} +\frac{9}{64}W^{-4}(\Sigma{}_{a b}){}^{\beta \gamma}W{}^{a b}\lambda{}_{\beta}{}^{j}\varepsilon{}^{r i}(\Gamma{}^{c}){}_{\eta}{}^{\delta}\big(\nabla_{c}W\big)\lambda{}_{\gamma}{}^{k}\lambda{}_{\delta k}\\
&-\frac{9}{32}W^{-4}(\Sigma{}_{a b}){}^{\beta \gamma}W{}^{a b}\lambda{}_{\beta}{}^{j}\lambda{}^{\delta i}F{}_{\eta \gamma}\lambda{}_{\delta}{}^{r} -\frac{9}{32}W^{-3}(\Sigma{}_{a b}){}^{\beta \gamma}W{}^{a b}\lambda{}_{\beta}{}^{j}\lambda{}^{\delta i}W{}_{\eta \gamma}\lambda{}_{\delta}{}^{r}\\
&-\frac{9}{64}W^{-4}(\Sigma{}_{a b}){}^{\beta}{}_{\eta}W{}^{a b}\lambda{}_{\beta}{}^{j}\lambda{}^{\gamma i}X{}^{r k}\lambda{}_{\gamma k} -\frac{9}{64}W^{-4}(\Sigma{}_{a b}){}^{\beta \gamma}W{}^{a b}\lambda{}_{\beta}{}^{j}\lambda{}^{\delta i}(\Gamma{}^{c}){}_{\eta \gamma}\big(\nabla_{c}W\big)\lambda{}_{\delta}{}^{r}\\
&-\frac{9}{32}W^{-4}(\Sigma{}_{a b}){}^{\beta \gamma}W{}^{a b}\lambda{}_{\beta}{}^{j}\lambda{}^{\delta i}\lambda{}_{\gamma}{}^{r}F{}_{\eta \delta} -\frac{9}{32}W^{-3}(\Sigma{}_{a b}){}^{\beta \gamma}W{}^{a b}\lambda{}_{\beta}{}^{j}\lambda{}^{\delta i}\lambda{}_{\gamma}{}^{r}W{}_{\eta \delta}\\
&+\frac{9}{64}W^{-4}(\Sigma{}_{a b}){}^{\beta \gamma}W{}^{a b}\lambda{}_{\beta}{}^{j}\lambda{}_{\eta}{}^{i}\lambda{}_{\gamma}{}^{k}X{}^{r}{}_{k} -\frac{9}{64}W^{-4}(\Sigma{}_{a b}){}^{\beta \gamma}W{}^{a b}\lambda{}_{\beta}{}^{j}\lambda{}^{\delta i}\lambda{}_{\gamma}{}^{r}(\Gamma{}^{c}){}_{\eta \delta}\big(\nabla_{c}W\big)
\end{aligned}
\tag{S3-H4.13-b}
```

**Check for H4.13:** all 40 written summands have weight $`7/2`$, odd parity and the same free indices $`\eta;r,i,j`$. Dummy labels are paired. The coefficient $`1/3`$ and the two external epsilons are applied once, when collecting the spinor.

#### Input H4.14

The calculated input is

```math
\left.H^{ij}\right|_{\mathrm{H4.14}}=W^{-4}\big(\frac9{64}(\Sigma_{ab})^{\alpha\beta}W^{ab}\lambda^{\rho i}\lambda_\rho^j\lambda_\alpha^k\lambda_{\beta k}\big).
\tag{S3-H4.14-input}
```

Expand each written SU(2) average with weight $`1/2`$ before applying the left derivative.

Apply the product rule (S3-09), in the displayed factor order:

```math
\begin{aligned}
\left.\nabla_\eta^rH^{ij}\right|_{\mathrm{H4.14}}=&\frac{9}{64}\nabla_{\eta}^{r}\big(W^{-4}\big)(\Sigma{}_{a b}){}^{\beta \gamma}W{}^{a b}\lambda{}^{\delta i}\lambda{}_{\delta}{}^{j}\lambda{}_{\beta}{}^{k}\lambda{}_{\gamma k} +\frac{9}{64}W^{-4}(\Sigma{}_{a b}){}^{\beta \gamma}\nabla_{\eta}^{r}\big(W{}^{a b}\big)\lambda{}^{\delta i}\lambda{}_{\delta}{}^{j}\lambda{}_{\beta}{}^{k}\lambda{}_{\gamma k}\\
&+\frac{9}{64}W^{-4}(\Sigma{}_{a b}){}^{\beta \gamma}W{}^{a b}\nabla_{\eta}^{r}\big(\lambda{}^{\delta i}\big)\lambda{}_{\delta}{}^{j}\lambda{}_{\beta}{}^{k}\lambda{}_{\gamma k} -\frac{9}{64}W^{-4}(\Sigma{}_{a b}){}^{\beta \gamma}W{}^{a b}\lambda{}^{\delta i}\nabla_{\eta}^{r}\big(\lambda{}_{\delta}{}^{j}\big)\lambda{}_{\beta}{}^{k}\lambda{}_{\gamma k}\\
&+\frac{9}{64}W^{-4}(\Sigma{}_{a b}){}^{\beta \gamma}W{}^{a b}\lambda{}^{\delta i}\lambda{}_{\delta}{}^{j}\nabla_{\eta}^{r}\big(\lambda{}_{\beta}{}^{k}\big)\lambda{}_{\gamma k} -\frac{9}{64}W^{-4}(\Sigma{}_{a b}){}^{\beta \gamma}W{}^{a b}\lambda{}^{\delta i}\lambda{}_{\delta}{}^{j}\lambda{}_{\beta}{}^{k}\nabla_{\eta}^{r}\big(\lambda{}_{\gamma k}\big)
\end{aligned}
\tag{S3-H4.14-a}
```

Insert the elementary source identities and the applicable commutators (S3-11)–(S3-14), distribute the vector product rules, and contract only index-raising metrics. The resulting contribution is

```math
\begin{aligned}
\left.\nabla_\eta^rH^{ij}\right|_{\mathrm{H4.14}}=&-\frac{9i}{16}W^{-5}\lambda{}_{\eta}{}^{r}(\Sigma{}_{a b}){}^{\beta \gamma}W{}^{a b}\lambda{}^{\delta i}\lambda{}_{\delta}{}^{j}\lambda{}_{\beta}{}^{k}\lambda{}_{\gamma k} +\frac{9}{64}W^{-4}(\Sigma{}_{a b}){}^{\beta \gamma}(\Sigma{}^{a b}){}^{\delta \rho}W{}_{\eta \delta \rho}{}^{r}\lambda{}^{\sigma i}\lambda{}_{\sigma}{}^{j}\lambda{}_{\beta}{}^{k}\lambda{}_{\gamma k}\\
&+\frac{9}{128}W^{-4}(\Sigma{}_{a b}){}^{\beta \gamma}(\Sigma{}^{a b}){}_{\eta}{}^{\delta}X{}_{\delta}{}^{r}\lambda{}^{\rho i}\lambda{}_{\rho}{}^{j}\lambda{}_{\beta}{}^{k}\lambda{}_{\gamma k} +\frac{9}{128}W^{-4}(\Sigma{}_{a b}){}^{\beta \gamma}(\Sigma{}^{a b}){}^{\delta}{}_{\eta}X{}_{\delta}{}^{r}\lambda{}^{\rho i}\lambda{}_{\rho}{}^{j}\lambda{}_{\beta}{}^{k}\lambda{}_{\gamma k}\\
&-\frac{9}{32}W^{-4}(\Sigma{}_{a b}){}^{\beta \gamma}W{}^{a b}\varepsilon{}^{r i}F{}_{\eta}{}^{\delta}\lambda{}_{\delta}{}^{j}\lambda{}_{\beta}{}^{k}\lambda{}_{\gamma k} -\frac{9}{32}W^{-3}(\Sigma{}_{a b}){}^{\beta \gamma}W{}^{a b}\varepsilon{}^{r i}W{}_{\eta}{}^{\delta}\lambda{}_{\delta}{}^{j}\lambda{}_{\beta}{}^{k}\lambda{}_{\gamma k}\\
&+\frac{9}{64}W^{-4}(\Sigma{}_{a b}){}^{\beta \gamma}W{}^{a b}X{}^{r i}\lambda{}_{\eta}{}^{j}\lambda{}_{\beta}{}^{k}\lambda{}_{\gamma k} -\frac{9}{64}W^{-4}(\Sigma{}_{a b}){}^{\beta \gamma}W{}^{a b}\varepsilon{}^{r i}(\Gamma{}^{c}){}_{\eta}{}^{\delta}\big(\nabla_{c}W\big)\lambda{}_{\delta}{}^{j}\lambda{}_{\beta}{}^{k}\lambda{}_{\gamma k}\\
&+\frac{9}{32}W^{-4}(\Sigma{}_{a b}){}^{\beta \gamma}W{}^{a b}\lambda{}^{\delta i}\varepsilon{}^{r j}F{}_{\eta \delta}\lambda{}_{\beta}{}^{k}\lambda{}_{\gamma k} +\frac{9}{32}W^{-3}(\Sigma{}_{a b}){}^{\beta \gamma}W{}^{a b}\lambda{}^{\delta i}\varepsilon{}^{r j}W{}_{\eta \delta}\lambda{}_{\beta}{}^{k}\lambda{}_{\gamma k}\\
&+\frac{9}{64}W^{-4}(\Sigma{}_{a b}){}^{\beta \gamma}W{}^{a b}\lambda{}_{\eta}{}^{i}X{}^{r j}\lambda{}_{\beta}{}^{k}\lambda{}_{\gamma k} +\frac{9}{64}W^{-4}(\Sigma{}_{a b}){}^{\beta \gamma}W{}^{a b}\lambda{}^{\delta i}\varepsilon{}^{r j}(\Gamma{}^{c}){}_{\eta \delta}\big(\nabla_{c}W\big)\lambda{}_{\beta}{}^{k}\lambda{}_{\gamma k}\\
&-\frac{9}{32}W^{-4}(\Sigma{}_{a b}){}^{\beta \gamma}W{}^{a b}\lambda{}^{\delta i}\lambda{}_{\delta}{}^{j}F{}_{\eta \beta}\lambda{}_{\gamma}{}^{r} -\frac{9}{32}W^{-3}(\Sigma{}_{a b}){}^{\beta \gamma}W{}^{a b}\lambda{}^{\delta i}\lambda{}_{\delta}{}^{j}W{}_{\eta \beta}\lambda{}_{\gamma}{}^{r}\\
&-\frac{9}{64}W^{-4}(\Sigma{}_{a b}){}_{\eta}{}^{\beta}W{}^{a b}\lambda{}^{\gamma i}\lambda{}_{\gamma}{}^{j}X{}^{r k}\lambda{}_{\beta k} -\frac{9}{64}W^{-4}(\Sigma{}_{a b}){}^{\beta \gamma}W{}^{a b}\lambda{}^{\delta i}\lambda{}_{\delta}{}^{j}(\Gamma{}^{c}){}_{\eta \beta}\big(\nabla_{c}W\big)\lambda{}_{\gamma}{}^{r}\\
&-\frac{9}{32}W^{-4}(\Sigma{}_{a b}){}^{\beta \gamma}W{}^{a b}\lambda{}^{\delta i}\lambda{}_{\delta}{}^{j}\lambda{}_{\beta}{}^{r}F{}_{\eta \gamma} -\frac{9}{32}W^{-3}(\Sigma{}_{a b}){}^{\beta \gamma}W{}^{a b}\lambda{}^{\delta i}\lambda{}_{\delta}{}^{j}\lambda{}_{\beta}{}^{r}W{}_{\eta \gamma}\\
&+\frac{9}{64}W^{-4}(\Sigma{}_{a b}){}^{\beta}{}_{\eta}W{}^{a b}\lambda{}^{\gamma i}\lambda{}_{\gamma}{}^{j}\lambda{}_{\beta}{}^{k}X{}^{r}{}_{k} -\frac{9}{64}W^{-4}(\Sigma{}_{a b}){}^{\beta \gamma}W{}^{a b}\lambda{}^{\delta i}\lambda{}_{\delta}{}^{j}\lambda{}_{\beta}{}^{r}(\Gamma{}^{c}){}_{\eta \gamma}\big(\nabla_{c}W\big)
\end{aligned}
\tag{S3-H4.14-b}
```

**Check for H4.14:** all 20 written summands have weight $`7/2`$, odd parity and the same free indices $`\eta;r,i,j`$. Dummy labels are paired. The coefficient $`1/3`$ and the two external epsilons are applied once, when collecting the spinor.

### 4.9 Differentiate every input in the $`W^{-5}`$ sector

<!-- ASSERT_CONVENTION: source_frame=Gold traceless Standard-Weyl superspace, derivative_parity=odd left, fermions=all degrees retained -->

#### Input H5.1

The calculated input is

```math
\left.H^{ij}\right|_{\mathrm{H5.1}}=W^{-5}\big(\frac38(\Gamma^a)^{\alpha\beta}\lambda_\alpha^{(i}\lambda^{\rho j)}\lambda_\beta^k\lambda_{\rho k}\nabla_aW\big).
\tag{S3-H5.1-input}
```

Expand each written SU(2) average with weight $`1/2`$ before applying the left derivative.

Apply the product rule (S3-09), in the displayed factor order:

```math
\begin{aligned}
\left.\nabla_\eta^rH^{ij}\right|_{\mathrm{H5.1}}=&\frac{3}{16}\nabla_{\eta}^{r}\big(W^{-5}\big)(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{i}\lambda{}^{\delta j}\lambda{}_{\gamma}{}^{k}\lambda{}_{\delta k}\big(\nabla_{a}W\big) +\frac{3}{16}W^{-5}(\Gamma{}^{a}){}^{\beta \gamma}\nabla_{\eta}^{r}\big(\lambda{}_{\beta}{}^{i}\big)\lambda{}^{\delta j}\lambda{}_{\gamma}{}^{k}\lambda{}_{\delta k}\big(\nabla_{a}W\big)\\
&-\frac{3}{16}W^{-5}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{i}\nabla_{\eta}^{r}\big(\lambda{}^{\delta j}\big)\lambda{}_{\gamma}{}^{k}\lambda{}_{\delta k}\big(\nabla_{a}W\big) +\frac{3}{16}W^{-5}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{i}\lambda{}^{\delta j}\nabla_{\eta}^{r}\big(\lambda{}_{\gamma}{}^{k}\big)\lambda{}_{\delta k}\big(\nabla_{a}W\big)\\
&-\frac{3}{16}W^{-5}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{i}\lambda{}^{\delta j}\lambda{}_{\gamma}{}^{k}\nabla_{\eta}^{r}\big(\lambda{}_{\delta k}\big)\big(\nabla_{a}W\big) +\frac{3}{16}W^{-5}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{i}\lambda{}^{\delta j}\lambda{}_{\gamma}{}^{k}\lambda{}_{\delta k}\nabla_{\eta}^{r}\big(\nabla_{a}W\big)\\
&+\frac{3}{16}\nabla_{\eta}^{r}\big(W^{-5}\big)(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{j}\lambda{}^{\delta i}\lambda{}_{\gamma}{}^{k}\lambda{}_{\delta k}\big(\nabla_{a}W\big) +\frac{3}{16}W^{-5}(\Gamma{}^{a}){}^{\beta \gamma}\nabla_{\eta}^{r}\big(\lambda{}_{\beta}{}^{j}\big)\lambda{}^{\delta i}\lambda{}_{\gamma}{}^{k}\lambda{}_{\delta k}\big(\nabla_{a}W\big)\\
&-\frac{3}{16}W^{-5}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{j}\nabla_{\eta}^{r}\big(\lambda{}^{\delta i}\big)\lambda{}_{\gamma}{}^{k}\lambda{}_{\delta k}\big(\nabla_{a}W\big) +\frac{3}{16}W^{-5}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{j}\lambda{}^{\delta i}\nabla_{\eta}^{r}\big(\lambda{}_{\gamma}{}^{k}\big)\lambda{}_{\delta k}\big(\nabla_{a}W\big)\\
&-\frac{3}{16}W^{-5}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{j}\lambda{}^{\delta i}\lambda{}_{\gamma}{}^{k}\nabla_{\eta}^{r}\big(\lambda{}_{\delta k}\big)\big(\nabla_{a}W\big) +\frac{3}{16}W^{-5}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{j}\lambda{}^{\delta i}\lambda{}_{\gamma}{}^{k}\lambda{}_{\delta k}\nabla_{\eta}^{r}\big(\nabla_{a}W\big)
\end{aligned}
\tag{S3-H5.1-a}
```

Insert the elementary source identities and the applicable commutators (S3-11)–(S3-14), distribute the vector product rules, and contract only index-raising metrics. The resulting contribution is

```math
\begin{aligned}
\left.\nabla_\eta^rH^{ij}\right|_{\mathrm{H5.1}}=&-\frac{15i}{16}W^{-6}\lambda{}_{\eta}{}^{r}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{i}\lambda{}^{\delta j}\lambda{}_{\gamma}{}^{k}\lambda{}_{\delta k}\big(\nabla_{a}W\big) -\frac{3}{8}W^{-5}(\Gamma{}^{a}){}^{\beta \gamma}\varepsilon{}^{r i}F{}_{\eta \beta}\lambda{}^{\delta j}\lambda{}_{\gamma}{}^{k}\lambda{}_{\delta k}\big(\nabla_{a}W\big)\\
&-\frac{3}{8}W^{-4}(\Gamma{}^{a}){}^{\beta \gamma}\varepsilon{}^{r i}W{}_{\eta \beta}\lambda{}^{\delta j}\lambda{}_{\gamma}{}^{k}\lambda{}_{\delta k}\big(\nabla_{a}W\big) -\frac{3}{16}W^{-5}(\Gamma{}^{a}){}_{\eta}{}^{\beta}X{}^{r i}\lambda{}^{\gamma j}\lambda{}_{\beta}{}^{k}\lambda{}_{\gamma k}\big(\nabla_{a}W\big)\\
&-\frac{3}{16}W^{-5}(\Gamma{}^{a}){}^{\beta \gamma}\varepsilon{}^{r i}(\Gamma{}^{b}){}_{\eta \beta}\big(\nabla_{b}W\big)\lambda{}^{\delta j}\lambda{}_{\gamma}{}^{k}\lambda{}_{\delta k}\big(\nabla_{a}W\big) +\frac{3}{8}W^{-5}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{i}\varepsilon{}^{r j}F{}_{\eta}{}^{\delta}\lambda{}_{\gamma}{}^{k}\lambda{}_{\delta k}\big(\nabla_{a}W\big)\\
&+\frac{3}{8}W^{-4}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{i}\varepsilon{}^{r j}W{}_{\eta}{}^{\delta}\lambda{}_{\gamma}{}^{k}\lambda{}_{\delta k}\big(\nabla_{a}W\big) -\frac{3}{16}W^{-5}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{i}X{}^{r j}\lambda{}_{\gamma}{}^{k}\lambda{}_{\eta k}\big(\nabla_{a}W\big)\\
&+\frac{3}{16}W^{-5}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{i}\varepsilon{}^{r j}(\Gamma{}^{b}){}_{\eta}{}^{\delta}\big(\nabla_{b}W\big)\lambda{}_{\gamma}{}^{k}\lambda{}_{\delta k}\big(\nabla_{a}W\big) -\frac{3}{8}W^{-5}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{i}\lambda{}^{\delta j}F{}_{\eta \gamma}\lambda{}_{\delta}{}^{r}\big(\nabla_{a}W\big)\\
&-\frac{3}{8}W^{-4}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{i}\lambda{}^{\delta j}W{}_{\eta \gamma}\lambda{}_{\delta}{}^{r}\big(\nabla_{a}W\big) -\frac{3}{16}W^{-5}(\Gamma{}^{a}){}^{\beta}{}_{\eta}\lambda{}_{\beta}{}^{i}\lambda{}^{\gamma j}X{}^{r k}\lambda{}_{\gamma k}\big(\nabla_{a}W\big)\\
&-\frac{3}{16}W^{-5}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{i}\lambda{}^{\delta j}(\Gamma{}^{b}){}_{\eta \gamma}\big(\nabla_{b}W\big)\lambda{}_{\delta}{}^{r}\big(\nabla_{a}W\big) -\frac{3}{8}W^{-5}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{i}\lambda{}^{\delta j}\lambda{}_{\gamma}{}^{r}F{}_{\eta \delta}\big(\nabla_{a}W\big)\\
&-\frac{3}{8}W^{-4}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{i}\lambda{}^{\delta j}\lambda{}_{\gamma}{}^{r}W{}_{\eta \delta}\big(\nabla_{a}W\big) +\frac{3}{16}W^{-5}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{i}\lambda{}_{\eta}{}^{j}\lambda{}_{\gamma}{}^{k}X{}^{r}{}_{k}\big(\nabla_{a}W\big)\\
&-\frac{3}{16}W^{-5}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{i}\lambda{}^{\delta j}\lambda{}_{\gamma}{}^{r}(\Gamma{}^{b}){}_{\eta \delta}\big(\nabla_{b}W\big)\big(\nabla_{a}W\big) +\frac{3i}{16}W^{-5}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{i}\lambda{}^{\delta j}\lambda{}_{\gamma}{}^{k}\lambda{}_{\delta k}\big(\nabla_{a}\lambda{}_{\eta}{}^{r}\big)\\
&+\frac{3i}{16}W^{-5}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{i}\lambda{}^{\delta j}\lambda{}_{\gamma}{}^{k}\lambda{}_{\delta k}\mathcal T{}_{a \eta}{}^{\rho}\lambda{}_{\rho}{}^{r} +\frac{3}{16}W^{-4}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{i}\lambda{}^{\delta j}\lambda{}_{\gamma}{}^{k}\lambda{}_{\delta k}\mathcal R(\mathbb D){}_{a \eta}{}^{r}\\
&-\frac{15i}{16}W^{-6}\lambda{}_{\eta}{}^{r}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{j}\lambda{}^{\delta i}\lambda{}_{\gamma}{}^{k}\lambda{}_{\delta k}\big(\nabla_{a}W\big) -\frac{3}{8}W^{-5}(\Gamma{}^{a}){}^{\beta \gamma}\varepsilon{}^{r j}F{}_{\eta \beta}\lambda{}^{\delta i}\lambda{}_{\gamma}{}^{k}\lambda{}_{\delta k}\big(\nabla_{a}W\big)\\
&-\frac{3}{8}W^{-4}(\Gamma{}^{a}){}^{\beta \gamma}\varepsilon{}^{r j}W{}_{\eta \beta}\lambda{}^{\delta i}\lambda{}_{\gamma}{}^{k}\lambda{}_{\delta k}\big(\nabla_{a}W\big) -\frac{3}{16}W^{-5}(\Gamma{}^{a}){}_{\eta}{}^{\beta}X{}^{r j}\lambda{}^{\gamma i}\lambda{}_{\beta}{}^{k}\lambda{}_{\gamma k}\big(\nabla_{a}W\big)\\
&-\frac{3}{16}W^{-5}(\Gamma{}^{a}){}^{\beta \gamma}\varepsilon{}^{r j}(\Gamma{}^{b}){}_{\eta \beta}\big(\nabla_{b}W\big)\lambda{}^{\delta i}\lambda{}_{\gamma}{}^{k}\lambda{}_{\delta k}\big(\nabla_{a}W\big) +\frac{3}{8}W^{-5}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{j}\varepsilon{}^{r i}F{}_{\eta}{}^{\delta}\lambda{}_{\gamma}{}^{k}\lambda{}_{\delta k}\big(\nabla_{a}W\big)\\
&+\frac{3}{8}W^{-4}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{j}\varepsilon{}^{r i}W{}_{\eta}{}^{\delta}\lambda{}_{\gamma}{}^{k}\lambda{}_{\delta k}\big(\nabla_{a}W\big) -\frac{3}{16}W^{-5}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{j}X{}^{r i}\lambda{}_{\gamma}{}^{k}\lambda{}_{\eta k}\big(\nabla_{a}W\big)\\
&+\frac{3}{16}W^{-5}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{j}\varepsilon{}^{r i}(\Gamma{}^{b}){}_{\eta}{}^{\delta}\big(\nabla_{b}W\big)\lambda{}_{\gamma}{}^{k}\lambda{}_{\delta k}\big(\nabla_{a}W\big) -\frac{3}{8}W^{-5}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{j}\lambda{}^{\delta i}F{}_{\eta \gamma}\lambda{}_{\delta}{}^{r}\big(\nabla_{a}W\big)\\
&-\frac{3}{8}W^{-4}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{j}\lambda{}^{\delta i}W{}_{\eta \gamma}\lambda{}_{\delta}{}^{r}\big(\nabla_{a}W\big) -\frac{3}{16}W^{-5}(\Gamma{}^{a}){}^{\beta}{}_{\eta}\lambda{}_{\beta}{}^{j}\lambda{}^{\gamma i}X{}^{r k}\lambda{}_{\gamma k}\big(\nabla_{a}W\big)\\
&-\frac{3}{16}W^{-5}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{j}\lambda{}^{\delta i}(\Gamma{}^{b}){}_{\eta \gamma}\big(\nabla_{b}W\big)\lambda{}_{\delta}{}^{r}\big(\nabla_{a}W\big) -\frac{3}{8}W^{-5}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{j}\lambda{}^{\delta i}\lambda{}_{\gamma}{}^{r}F{}_{\eta \delta}\big(\nabla_{a}W\big)\\
&-\frac{3}{8}W^{-4}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{j}\lambda{}^{\delta i}\lambda{}_{\gamma}{}^{r}W{}_{\eta \delta}\big(\nabla_{a}W\big) +\frac{3}{16}W^{-5}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{j}\lambda{}_{\eta}{}^{i}\lambda{}_{\gamma}{}^{k}X{}^{r}{}_{k}\big(\nabla_{a}W\big)\\
&-\frac{3}{16}W^{-5}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{j}\lambda{}^{\delta i}\lambda{}_{\gamma}{}^{r}(\Gamma{}^{b}){}_{\eta \delta}\big(\nabla_{b}W\big)\big(\nabla_{a}W\big) +\frac{3i}{16}W^{-5}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{j}\lambda{}^{\delta i}\lambda{}_{\gamma}{}^{k}\lambda{}_{\delta k}\big(\nabla_{a}\lambda{}_{\eta}{}^{r}\big)\\
&+\frac{3i}{16}W^{-5}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{j}\lambda{}^{\delta i}\lambda{}_{\gamma}{}^{k}\lambda{}_{\delta k}\mathcal T{}_{a \eta}{}^{\rho}\lambda{}_{\rho}{}^{r} +\frac{3}{16}W^{-4}(\Gamma{}^{a}){}^{\beta \gamma}\lambda{}_{\beta}{}^{j}\lambda{}^{\delta i}\lambda{}_{\gamma}{}^{k}\lambda{}_{\delta k}\mathcal R(\mathbb D){}_{a \eta}{}^{r}
\end{aligned}
\tag{S3-H5.1-b}
```

**Check for H5.1:** all 40 written summands have weight $`7/2`$, odd parity and the same free indices $`\eta;r,i,j`$. Dummy labels are paired. The coefficient $`1/3`$ and the two external epsilons are applied once, when collecting the spinor.

#### Input H5.2

The calculated input is

```math
\left.H^{ij}\right|_{\mathrm{H5.2}}=W^{-5}\big(\frac38(\Sigma_{ab})^{\alpha\beta}F^{ab}\lambda^{\rho i}\lambda_\rho^j\lambda_\alpha^k\lambda_{\beta k}\big).
\tag{S3-H5.2-input}
```

Expand each written SU(2) average with weight $`1/2`$ before applying the left derivative.

Apply the product rule (S3-09), in the displayed factor order:

```math
\begin{aligned}
\left.\nabla_\eta^rH^{ij}\right|_{\mathrm{H5.2}}=&\frac{3}{8}\nabla_{\eta}^{r}\big(W^{-5}\big)(\Sigma{}_{a b}){}^{\beta \gamma}F{}^{a b}\lambda{}^{\delta i}\lambda{}_{\delta}{}^{j}\lambda{}_{\beta}{}^{k}\lambda{}_{\gamma k} +\frac{3}{8}W^{-5}(\Sigma{}_{a b}){}^{\beta \gamma}\nabla_{\eta}^{r}\big(F{}^{a b}\big)\lambda{}^{\delta i}\lambda{}_{\delta}{}^{j}\lambda{}_{\beta}{}^{k}\lambda{}_{\gamma k}\\
&+\frac{3}{8}W^{-5}(\Sigma{}_{a b}){}^{\beta \gamma}F{}^{a b}\nabla_{\eta}^{r}\big(\lambda{}^{\delta i}\big)\lambda{}_{\delta}{}^{j}\lambda{}_{\beta}{}^{k}\lambda{}_{\gamma k} -\frac{3}{8}W^{-5}(\Sigma{}_{a b}){}^{\beta \gamma}F{}^{a b}\lambda{}^{\delta i}\nabla_{\eta}^{r}\big(\lambda{}_{\delta}{}^{j}\big)\lambda{}_{\beta}{}^{k}\lambda{}_{\gamma k}\\
&+\frac{3}{8}W^{-5}(\Sigma{}_{a b}){}^{\beta \gamma}F{}^{a b}\lambda{}^{\delta i}\lambda{}_{\delta}{}^{j}\nabla_{\eta}^{r}\big(\lambda{}_{\beta}{}^{k}\big)\lambda{}_{\gamma k} -\frac{3}{8}W^{-5}(\Sigma{}_{a b}){}^{\beta \gamma}F{}^{a b}\lambda{}^{\delta i}\lambda{}_{\delta}{}^{j}\lambda{}_{\beta}{}^{k}\nabla_{\eta}^{r}\big(\lambda{}_{\gamma k}\big)
\end{aligned}
\tag{S3-H5.2-a}
```

Insert the elementary source identities and the applicable commutators (S3-11)–(S3-14), distribute the vector product rules, and contract only index-raising metrics. The resulting contribution is

```math
\begin{aligned}
\left.\nabla_\eta^rH^{ij}\right|_{\mathrm{H5.2}}=&-\frac{15i}{8}W^{-6}\lambda{}_{\eta}{}^{r}(\Sigma{}_{a b}){}^{\beta \gamma}F{}^{a b}\lambda{}^{\delta i}\lambda{}_{\delta}{}^{j}\lambda{}_{\beta}{}^{k}\lambda{}_{\gamma k} -\frac{3i}{16}W^{-5}(\Sigma{}_{a b}){}^{\beta \gamma}(\Sigma{}^{a b}){}^{\delta \rho}(\Gamma{}^{c}){}_{\eta \delta}\big(\nabla_{c}\lambda{}_{\rho}{}^{r}\big)\lambda{}^{\sigma i}\lambda{}_{\sigma}{}^{j}\lambda{}_{\beta}{}^{k}\lambda{}_{\gamma k}\\
&-\frac{3i}{16}W^{-5}(\Sigma{}_{a b}){}^{\beta \gamma}(\Sigma{}^{a b}){}_{\eta}{}^{\delta}(\Gamma{}^{c}){}_{\delta}{}^{\rho}\big(\nabla_{c}\lambda{}_{\rho}{}^{r}\big)\lambda{}^{\sigma i}\lambda{}_{\sigma}{}^{j}\lambda{}_{\beta}{}^{k}\lambda{}_{\gamma k} +\frac{3i}{32}W^{-5}(\Sigma{}_{a b}){}^{\beta \gamma}(\Sigma{}^{a b}){}^{\delta \rho}W{}_{\eta \delta}\lambda{}_{\rho}{}^{r}\lambda{}^{\sigma i}\lambda{}_{\sigma}{}^{j}\lambda{}_{\beta}{}^{k}\lambda{}_{\gamma k}\\
&-\frac{9i}{32}W^{-5}(\Sigma{}_{a b}){}^{\beta \gamma}(\Sigma{}^{a b}){}_{\eta}{}^{\delta}W{}_{\delta}{}^{\rho}\lambda{}_{\rho}{}^{r}\lambda{}^{\sigma i}\lambda{}_{\sigma}{}^{j}\lambda{}_{\beta}{}^{k}\lambda{}_{\gamma k} -\frac{3i}{16}W^{-5}(\Sigma{}_{a b}){}^{\beta \gamma}(\Sigma{}^{a b}){}^{\delta \rho}(\Gamma{}^{c}){}_{\eta \rho}\big(\nabla_{c}\lambda{}_{\delta}{}^{r}\big)\lambda{}^{\sigma i}\lambda{}_{\sigma}{}^{j}\lambda{}_{\beta}{}^{k}\lambda{}_{\gamma k}\\
&-\frac{3i}{16}W^{-5}(\Sigma{}_{a b}){}^{\beta \gamma}(\Sigma{}^{a b}){}^{\delta}{}_{\eta}(\Gamma{}^{c}){}_{\delta}{}^{\rho}\big(\nabla_{c}\lambda{}_{\rho}{}^{r}\big)\lambda{}^{\sigma i}\lambda{}_{\sigma}{}^{j}\lambda{}_{\beta}{}^{k}\lambda{}_{\gamma k} +\frac{3i}{32}W^{-5}(\Sigma{}_{a b}){}^{\beta \gamma}(\Sigma{}^{a b}){}^{\delta \rho}W{}_{\eta \rho}\lambda{}_{\delta}{}^{r}\lambda{}^{\sigma i}\lambda{}_{\sigma}{}^{j}\lambda{}_{\beta}{}^{k}\lambda{}_{\gamma k}\\
&-\frac{9i}{32}W^{-5}(\Sigma{}_{a b}){}^{\beta \gamma}(\Sigma{}^{a b}){}^{\delta}{}_{\eta}W{}_{\delta}{}^{\rho}\lambda{}_{\rho}{}^{r}\lambda{}^{\sigma i}\lambda{}_{\sigma}{}^{j}\lambda{}_{\beta}{}^{k}\lambda{}_{\gamma k} -\frac{9i}{16}W^{-5}(\Sigma{}_{a b}){}^{\beta \gamma}(\Sigma{}^{a b}){}^{\delta \rho}W{}_{\delta \rho}\lambda{}_{\eta}{}^{r}\lambda{}^{\sigma i}\lambda{}_{\sigma}{}^{j}\lambda{}_{\beta}{}^{k}\lambda{}_{\gamma k}\\
&-\frac{3}{8}W^{-4}(\Sigma{}_{a b}){}^{\beta \gamma}(\Sigma{}^{a b}){}^{\delta \rho}W{}_{\eta \delta \rho}{}^{r}\lambda{}^{\sigma i}\lambda{}_{\sigma}{}^{j}\lambda{}_{\beta}{}^{k}\lambda{}_{\gamma k} -\frac{3}{4}W^{-5}(\Sigma{}_{a b}){}^{\beta \gamma}F{}^{a b}\varepsilon{}^{r i}F{}_{\eta}{}^{\delta}\lambda{}_{\delta}{}^{j}\lambda{}_{\beta}{}^{k}\lambda{}_{\gamma k}\\
&-\frac{3}{4}W^{-4}(\Sigma{}_{a b}){}^{\beta \gamma}F{}^{a b}\varepsilon{}^{r i}W{}_{\eta}{}^{\delta}\lambda{}_{\delta}{}^{j}\lambda{}_{\beta}{}^{k}\lambda{}_{\gamma k} +\frac{3}{8}W^{-5}(\Sigma{}_{a b}){}^{\beta \gamma}F{}^{a b}X{}^{r i}\lambda{}_{\eta}{}^{j}\lambda{}_{\beta}{}^{k}\lambda{}_{\gamma k}\\
&-\frac{3}{8}W^{-5}(\Sigma{}_{a b}){}^{\beta \gamma}F{}^{a b}\varepsilon{}^{r i}(\Gamma{}^{c}){}_{\eta}{}^{\delta}\big(\nabla_{c}W\big)\lambda{}_{\delta}{}^{j}\lambda{}_{\beta}{}^{k}\lambda{}_{\gamma k} +\frac{3}{4}W^{-5}(\Sigma{}_{a b}){}^{\beta \gamma}F{}^{a b}\lambda{}^{\delta i}\varepsilon{}^{r j}F{}_{\eta \delta}\lambda{}_{\beta}{}^{k}\lambda{}_{\gamma k}\\
&+\frac{3}{4}W^{-4}(\Sigma{}_{a b}){}^{\beta \gamma}F{}^{a b}\lambda{}^{\delta i}\varepsilon{}^{r j}W{}_{\eta \delta}\lambda{}_{\beta}{}^{k}\lambda{}_{\gamma k} +\frac{3}{8}W^{-5}(\Sigma{}_{a b}){}^{\beta \gamma}F{}^{a b}\lambda{}_{\eta}{}^{i}X{}^{r j}\lambda{}_{\beta}{}^{k}\lambda{}_{\gamma k}\\
&+\frac{3}{8}W^{-5}(\Sigma{}_{a b}){}^{\beta \gamma}F{}^{a b}\lambda{}^{\delta i}\varepsilon{}^{r j}(\Gamma{}^{c}){}_{\eta \delta}\big(\nabla_{c}W\big)\lambda{}_{\beta}{}^{k}\lambda{}_{\gamma k} -\frac{3}{4}W^{-5}(\Sigma{}_{a b}){}^{\beta \gamma}F{}^{a b}\lambda{}^{\delta i}\lambda{}_{\delta}{}^{j}F{}_{\eta \beta}\lambda{}_{\gamma}{}^{r}\\
&-\frac{3}{4}W^{-4}(\Sigma{}_{a b}){}^{\beta \gamma}F{}^{a b}\lambda{}^{\delta i}\lambda{}_{\delta}{}^{j}W{}_{\eta \beta}\lambda{}_{\gamma}{}^{r} -\frac{3}{8}W^{-5}(\Sigma{}_{a b}){}_{\eta}{}^{\beta}F{}^{a b}\lambda{}^{\gamma i}\lambda{}_{\gamma}{}^{j}X{}^{r k}\lambda{}_{\beta k}\\
&-\frac{3}{8}W^{-5}(\Sigma{}_{a b}){}^{\beta \gamma}F{}^{a b}\lambda{}^{\delta i}\lambda{}_{\delta}{}^{j}(\Gamma{}^{c}){}_{\eta \beta}\big(\nabla_{c}W\big)\lambda{}_{\gamma}{}^{r} -\frac{3}{4}W^{-5}(\Sigma{}_{a b}){}^{\beta \gamma}F{}^{a b}\lambda{}^{\delta i}\lambda{}_{\delta}{}^{j}\lambda{}_{\beta}{}^{r}F{}_{\eta \gamma}\\
&-\frac{3}{4}W^{-4}(\Sigma{}_{a b}){}^{\beta \gamma}F{}^{a b}\lambda{}^{\delta i}\lambda{}_{\delta}{}^{j}\lambda{}_{\beta}{}^{r}W{}_{\eta \gamma} +\frac{3}{8}W^{-5}(\Sigma{}_{a b}){}^{\beta}{}_{\eta}F{}^{a b}\lambda{}^{\gamma i}\lambda{}_{\gamma}{}^{j}\lambda{}_{\beta}{}^{k}X{}^{r}{}_{k}\\
&-\frac{3}{8}W^{-5}(\Sigma{}_{a b}){}^{\beta \gamma}F{}^{a b}\lambda{}^{\delta i}\lambda{}_{\delta}{}^{j}\lambda{}_{\beta}{}^{r}(\Gamma{}^{c}){}_{\eta \gamma}\big(\nabla_{c}W\big)
\end{aligned}
\tag{S3-H5.2-b}
```

**Check for H5.2:** all 27 written summands have weight $`7/2`$, odd parity and the same free indices $`\eta;r,i,j`$. Dummy labels are paired. The coefficient $`1/3`$ and the two external epsilons are applied once, when collecting the spinor.

#### Input H5.3

The calculated input is

```math
\left.H^{ij}\right|_{\mathrm{H5.3}}=W^{-5}\big(\frac38X^{kl}\lambda^{\alpha i}\lambda_\alpha^j\lambda_k^\beta\lambda_{\beta l}\big).
\tag{S3-H5.3-input}
```

Apply the product rule (S3-09), in the displayed factor order:

```math
\begin{aligned}
\left.\nabla_\eta^rH^{ij}\right|_{\mathrm{H5.3}}=&\frac{3}{8}\nabla_{\eta}^{r}\big(W^{-5}\big)X{}^{k l}\lambda{}^{\beta i}\lambda{}_{\beta}{}^{j}\lambda{}^{\gamma}{}_{k}\lambda{}_{\gamma l} +\frac{3}{8}W^{-5}\nabla_{\eta}^{r}\big(X{}^{k l}\big)\lambda{}^{\beta i}\lambda{}_{\beta}{}^{j}\lambda{}^{\gamma}{}_{k}\lambda{}_{\gamma l}\\
&+\frac{3}{8}W^{-5}X{}^{k l}\nabla_{\eta}^{r}\big(\lambda{}^{\beta i}\big)\lambda{}_{\beta}{}^{j}\lambda{}^{\gamma}{}_{k}\lambda{}_{\gamma l} -\frac{3}{8}W^{-5}X{}^{k l}\lambda{}^{\beta i}\nabla_{\eta}^{r}\big(\lambda{}_{\beta}{}^{j}\big)\lambda{}^{\gamma}{}_{k}\lambda{}_{\gamma l}\\
&+\frac{3}{8}W^{-5}X{}^{k l}\lambda{}^{\beta i}\lambda{}_{\beta}{}^{j}\nabla_{\eta}^{r}\big(\lambda{}^{\gamma}{}_{k}\big)\lambda{}_{\gamma l} -\frac{3}{8}W^{-5}X{}^{k l}\lambda{}^{\beta i}\lambda{}_{\beta}{}^{j}\lambda{}^{\gamma}{}_{k}\nabla_{\eta}^{r}\big(\lambda{}_{\gamma l}\big)
\end{aligned}
\tag{S3-H5.3-a}
```

Insert the elementary source identities and the applicable commutators (S3-11)–(S3-14), distribute the vector product rules, and contract only index-raising metrics. The resulting contribution is

```math
\begin{aligned}
\left.\nabla_\eta^rH^{ij}\right|_{\mathrm{H5.3}}=&-\frac{15i}{8}W^{-6}\lambda{}_{\eta}{}^{r}X{}^{k l}\lambda{}^{\beta i}\lambda{}_{\beta}{}^{j}\lambda{}^{\gamma}{}_{k}\lambda{}_{\gamma l} +\frac{3i}{8}W^{-5}(\Gamma{}^{a}){}_{\eta}{}^{\beta}\big(\nabla_{a}\lambda{}_{\beta}{}^{k}\big)\lambda{}^{\gamma i}\lambda{}_{\gamma}{}^{j}\lambda{}^{\delta r}\lambda{}_{\delta k}\\
&-\frac{3i}{16}W^{-5}W{}_{\eta \beta}\lambda{}^{\beta k}\lambda{}^{\gamma i}\lambda{}_{\gamma}{}^{j}\lambda{}^{\delta r}\lambda{}_{\delta k} -\frac{9}{32}W^{-4}X{}_{\eta}{}^{k}\lambda{}^{\beta i}\lambda{}_{\beta}{}^{j}\lambda{}^{\gamma r}\lambda{}_{\gamma k}\\
&+\frac{3i}{8}W^{-5}(\Gamma{}^{a}){}_{\eta}{}^{\beta}\big(\nabla_{a}\lambda{}_{\beta}{}^{k}\big)\lambda{}^{\gamma i}\lambda{}_{\gamma}{}^{j}\lambda{}^{\delta}{}_{k}\lambda{}_{\delta}{}^{r} -\frac{3i}{16}W^{-5}W{}_{\eta \beta}\lambda{}^{\beta k}\lambda{}^{\gamma i}\lambda{}_{\gamma}{}^{j}\lambda{}^{\delta}{}_{k}\lambda{}_{\delta}{}^{r}\\
&-\frac{9}{32}W^{-4}X{}_{\eta}{}^{k}\lambda{}^{\beta i}\lambda{}_{\beta}{}^{j}\lambda{}^{\gamma}{}_{k}\lambda{}_{\gamma}{}^{r} -\frac{3}{4}W^{-5}X{}^{k l}\varepsilon{}^{r i}F{}_{\eta}{}^{\beta}\lambda{}_{\beta}{}^{j}\lambda{}^{\gamma}{}_{k}\lambda{}_{\gamma l}\\
&-\frac{3}{4}W^{-4}X{}^{k l}\varepsilon{}^{r i}W{}_{\eta}{}^{\beta}\lambda{}_{\beta}{}^{j}\lambda{}^{\gamma}{}_{k}\lambda{}_{\gamma l} +\frac{3}{8}W^{-5}X{}^{k l}X{}^{r i}\lambda{}_{\eta}{}^{j}\lambda{}^{\beta}{}_{k}\lambda{}_{\beta l}\\
&-\frac{3}{8}W^{-5}X{}^{k l}\varepsilon{}^{r i}(\Gamma{}^{a}){}_{\eta}{}^{\beta}\big(\nabla_{a}W\big)\lambda{}_{\beta}{}^{j}\lambda{}^{\gamma}{}_{k}\lambda{}_{\gamma l} +\frac{3}{4}W^{-5}X{}^{k l}\lambda{}^{\beta i}\varepsilon{}^{r j}F{}_{\eta \beta}\lambda{}^{\gamma}{}_{k}\lambda{}_{\gamma l}\\
&+\frac{3}{4}W^{-4}X{}^{k l}\lambda{}^{\beta i}\varepsilon{}^{r j}W{}_{\eta \beta}\lambda{}^{\gamma}{}_{k}\lambda{}_{\gamma l} +\frac{3}{8}W^{-5}X{}^{k l}\lambda{}_{\eta}{}^{i}X{}^{r j}\lambda{}^{\beta}{}_{k}\lambda{}_{\beta l}\\
&+\frac{3}{8}W^{-5}X{}^{k l}\lambda{}^{\beta i}\varepsilon{}^{r j}(\Gamma{}^{a}){}_{\eta \beta}\big(\nabla_{a}W\big)\lambda{}^{\gamma}{}_{k}\lambda{}_{\gamma l} +\frac{3}{4}W^{-5}X{}^{r k}\lambda{}^{\beta i}\lambda{}_{\beta}{}^{j}F{}_{\eta}{}^{\gamma}\lambda{}_{\gamma k}\\
&+\frac{3}{4}W^{-4}X{}^{r k}\lambda{}^{\beta i}\lambda{}_{\beta}{}^{j}W{}_{\eta}{}^{\gamma}\lambda{}_{\gamma k} +\frac{3}{8}W^{-5}X{}^{k l}\lambda{}^{\beta i}\lambda{}_{\beta}{}^{j}X{}^{r}{}_{k}\lambda{}_{\eta l}\\
&+\frac{3}{8}W^{-5}X{}^{r k}\lambda{}^{\beta i}\lambda{}_{\beta}{}^{j}(\Gamma{}^{a}){}_{\eta}{}^{\gamma}\big(\nabla_{a}W\big)\lambda{}_{\gamma k} -\frac{3}{4}W^{-5}X{}^{k r}\lambda{}^{\beta i}\lambda{}_{\beta}{}^{j}\lambda{}^{\gamma}{}_{k}F{}_{\eta \gamma}\\
&-\frac{3}{4}W^{-4}X{}^{k r}\lambda{}^{\beta i}\lambda{}_{\beta}{}^{j}\lambda{}^{\gamma}{}_{k}W{}_{\eta \gamma} +\frac{3}{8}W^{-5}X{}^{k l}\lambda{}^{\beta i}\lambda{}_{\beta}{}^{j}\lambda{}_{\eta k}X{}^{r}{}_{l}\\
&-\frac{3}{8}W^{-5}X{}^{k r}\lambda{}^{\beta i}\lambda{}_{\beta}{}^{j}\lambda{}^{\gamma}{}_{k}(\Gamma{}^{a}){}_{\eta \gamma}\big(\nabla_{a}W\big)
\end{aligned}
\tag{S3-H5.3-b}
```

**Check for H5.3:** all 23 written summands have weight $`7/2`$, odd parity and the same free indices $`\eta;r,i,j`$. Dummy labels are paired. The coefficient $`1/3`$ and the two external epsilons are applied once, when collecting the spinor.


[Previous component](derivation_002.md) · [Component index](../STEP_03_LOG_SPINOR.md) · [Next component](derivation_004.md)
