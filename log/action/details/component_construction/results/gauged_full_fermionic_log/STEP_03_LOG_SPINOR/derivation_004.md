# LOG spinor descent — S3-H6.1-input – S3-155

<a id="step-3--deriving-the-log-spinor--410-differentiate-every-input-in-the-w-6-sector"></a>

[Component index](../STEP_03_LOG_SPINOR.md). Definitions and source conventions are in [the opening section](convention_001.md).

### 4.10 Differentiate every input in the $`W^{-6}`$ sector

<!-- ASSERT_CONVENTION: source_frame=Gold traceless Standard-Weyl superspace, derivative_parity=odd left, fermions=all degrees retained -->

#### Input H6.1

The calculated input is

```math
\left.H^{ij}\right|_{\mathrm{H6.1}}=W^{-6}\big(\frac{3i}{32}\lambda^{\alpha i}\lambda_\alpha^j\lambda^{\beta k}\lambda_\beta^l\lambda_k^\gamma\lambda_{\gamma l}\big).
\tag{S3-H6.1-input}
```

Apply the product rule (S3-09), in the displayed factor order:

```math
\begin{aligned}
\left.\nabla_\eta^rH^{ij}\right|_{\mathrm{H6.1}}=&\frac{3i}{32}\nabla_{\eta}^{r}\big(W^{-6}\big)\lambda{}^{\beta i}\lambda{}_{\beta}{}^{j}\lambda{}^{\gamma k}\lambda{}_{\gamma}{}^{l}\lambda{}^{\delta}{}_{k}\lambda{}_{\delta l} +\frac{3i}{32}W^{-6}\nabla_{\eta}^{r}\big(\lambda{}^{\beta i}\big)\lambda{}_{\beta}{}^{j}\lambda{}^{\gamma k}\lambda{}_{\gamma}{}^{l}\lambda{}^{\delta}{}_{k}\lambda{}_{\delta l}\\
&-\frac{3i}{32}W^{-6}\lambda{}^{\beta i}\nabla_{\eta}^{r}\big(\lambda{}_{\beta}{}^{j}\big)\lambda{}^{\gamma k}\lambda{}_{\gamma}{}^{l}\lambda{}^{\delta}{}_{k}\lambda{}_{\delta l} +\frac{3i}{32}W^{-6}\lambda{}^{\beta i}\lambda{}_{\beta}{}^{j}\nabla_{\eta}^{r}\big(\lambda{}^{\gamma k}\big)\lambda{}_{\gamma}{}^{l}\lambda{}^{\delta}{}_{k}\lambda{}_{\delta l}\\
&-\frac{3i}{32}W^{-6}\lambda{}^{\beta i}\lambda{}_{\beta}{}^{j}\lambda{}^{\gamma k}\nabla_{\eta}^{r}\big(\lambda{}_{\gamma}{}^{l}\big)\lambda{}^{\delta}{}_{k}\lambda{}_{\delta l} +\frac{3i}{32}W^{-6}\lambda{}^{\beta i}\lambda{}_{\beta}{}^{j}\lambda{}^{\gamma k}\lambda{}_{\gamma}{}^{l}\nabla_{\eta}^{r}\big(\lambda{}^{\delta}{}_{k}\big)\lambda{}_{\delta l}\\
&-\frac{3i}{32}W^{-6}\lambda{}^{\beta i}\lambda{}_{\beta}{}^{j}\lambda{}^{\gamma k}\lambda{}_{\gamma}{}^{l}\lambda{}^{\delta}{}_{k}\nabla_{\eta}^{r}\big(\lambda{}_{\delta l}\big)
\end{aligned}
\tag{S3-H6.1-a}
```

Insert the elementary source identities and the applicable commutators (S3-11)–(S3-14), distribute the vector product rules, and contract only index-raising metrics. The resulting contribution is

```math
\begin{aligned}
\left.\nabla_\eta^rH^{ij}\right|_{\mathrm{H6.1}}=&\frac{9}{16}W^{-7}\lambda{}_{\eta}{}^{r}\lambda{}^{\beta i}\lambda{}_{\beta}{}^{j}\lambda{}^{\gamma k}\lambda{}_{\gamma}{}^{l}\lambda{}^{\delta}{}_{k}\lambda{}_{\delta l} -\frac{3i}{16}W^{-6}\varepsilon{}^{r i}F{}_{\eta}{}^{\beta}\lambda{}_{\beta}{}^{j}\lambda{}^{\gamma k}\lambda{}_{\gamma}{}^{l}\lambda{}^{\delta}{}_{k}\lambda{}_{\delta l}\\
&-\frac{3i}{16}W^{-5}\varepsilon{}^{r i}W{}_{\eta}{}^{\beta}\lambda{}_{\beta}{}^{j}\lambda{}^{\gamma k}\lambda{}_{\gamma}{}^{l}\lambda{}^{\delta}{}_{k}\lambda{}_{\delta l} +\frac{3i}{32}W^{-6}X{}^{r i}\lambda{}_{\eta}{}^{j}\lambda{}^{\beta k}\lambda{}_{\beta}{}^{l}\lambda{}^{\gamma}{}_{k}\lambda{}_{\gamma l}\\
&-\frac{3i}{32}W^{-6}\varepsilon{}^{r i}(\Gamma{}^{a}){}_{\eta}{}^{\beta}\big(\nabla_{a}W\big)\lambda{}_{\beta}{}^{j}\lambda{}^{\gamma k}\lambda{}_{\gamma}{}^{l}\lambda{}^{\delta}{}_{k}\lambda{}_{\delta l} +\frac{3i}{16}W^{-6}\lambda{}^{\beta i}\varepsilon{}^{r j}F{}_{\eta \beta}\lambda{}^{\gamma k}\lambda{}_{\gamma}{}^{l}\lambda{}^{\delta}{}_{k}\lambda{}_{\delta l}\\
&+\frac{3i}{16}W^{-5}\lambda{}^{\beta i}\varepsilon{}^{r j}W{}_{\eta \beta}\lambda{}^{\gamma k}\lambda{}_{\gamma}{}^{l}\lambda{}^{\delta}{}_{k}\lambda{}_{\delta l} +\frac{3i}{32}W^{-6}\lambda{}_{\eta}{}^{i}X{}^{r j}\lambda{}^{\beta k}\lambda{}_{\beta}{}^{l}\lambda{}^{\gamma}{}_{k}\lambda{}_{\gamma l}\\
&+\frac{3i}{32}W^{-6}\lambda{}^{\beta i}\varepsilon{}^{r j}(\Gamma{}^{a}){}_{\eta \beta}\big(\nabla_{a}W\big)\lambda{}^{\gamma k}\lambda{}_{\gamma}{}^{l}\lambda{}^{\delta}{}_{k}\lambda{}_{\delta l} -\frac{3i}{16}W^{-6}\lambda{}^{\beta i}\lambda{}_{\beta}{}^{j}F{}_{\eta}{}^{\gamma}\lambda{}_{\gamma}{}^{k}\lambda{}^{\delta r}\lambda{}_{\delta k}\\
&-\frac{3i}{16}W^{-5}\lambda{}^{\beta i}\lambda{}_{\beta}{}^{j}W{}_{\eta}{}^{\gamma}\lambda{}_{\gamma}{}^{k}\lambda{}^{\delta r}\lambda{}_{\delta k} +\frac{3i}{32}W^{-6}\lambda{}^{\beta i}\lambda{}_{\beta}{}^{j}X{}^{r k}\lambda{}_{\eta}{}^{l}\lambda{}^{\gamma}{}_{k}\lambda{}_{\gamma l}\\
&-\frac{3i}{32}W^{-6}\lambda{}^{\beta i}\lambda{}_{\beta}{}^{j}(\Gamma{}^{a}){}_{\eta}{}^{\gamma}\big(\nabla_{a}W\big)\lambda{}_{\gamma}{}^{k}\lambda{}^{\delta r}\lambda{}_{\delta k} +\frac{3i}{16}W^{-6}\lambda{}^{\beta i}\lambda{}_{\beta}{}^{j}\lambda{}^{\gamma k}F{}_{\eta \gamma}\lambda{}^{\delta}{}_{k}\lambda{}_{\delta}{}^{r}\\
&+\frac{3i}{16}W^{-5}\lambda{}^{\beta i}\lambda{}_{\beta}{}^{j}\lambda{}^{\gamma k}W{}_{\eta \gamma}\lambda{}^{\delta}{}_{k}\lambda{}_{\delta}{}^{r} +\frac{3i}{32}W^{-6}\lambda{}^{\beta i}\lambda{}_{\beta}{}^{j}\lambda{}_{\eta}{}^{k}X{}^{r l}\lambda{}^{\gamma}{}_{k}\lambda{}_{\gamma l}\\
&+\frac{3i}{32}W^{-6}\lambda{}^{\beta i}\lambda{}_{\beta}{}^{j}\lambda{}^{\gamma k}(\Gamma{}^{a}){}_{\eta \gamma}\big(\nabla_{a}W\big)\lambda{}^{\delta}{}_{k}\lambda{}_{\delta}{}^{r} +\frac{3i}{16}W^{-6}\lambda{}^{\beta i}\lambda{}_{\beta}{}^{j}\lambda{}^{\gamma r}\lambda{}_{\gamma}{}^{k}F{}_{\eta}{}^{\delta}\lambda{}_{\delta k}\\
&+\frac{3i}{16}W^{-5}\lambda{}^{\beta i}\lambda{}_{\beta}{}^{j}\lambda{}^{\gamma r}\lambda{}_{\gamma}{}^{k}W{}_{\eta}{}^{\delta}\lambda{}_{\delta k} +\frac{3i}{32}W^{-6}\lambda{}^{\beta i}\lambda{}_{\beta}{}^{j}\lambda{}^{\gamma k}\lambda{}_{\gamma}{}^{l}X{}^{r}{}_{k}\lambda{}_{\eta l}\\
&+\frac{3i}{32}W^{-6}\lambda{}^{\beta i}\lambda{}_{\beta}{}^{j}\lambda{}^{\gamma r}\lambda{}_{\gamma}{}^{k}(\Gamma{}^{a}){}_{\eta}{}^{\delta}\big(\nabla_{a}W\big)\lambda{}_{\delta k} -\frac{3i}{16}W^{-6}\lambda{}^{\beta i}\lambda{}_{\beta}{}^{j}\lambda{}^{\gamma k}\lambda{}_{\gamma}{}^{r}\lambda{}^{\delta}{}_{k}F{}_{\eta \delta}\\
&-\frac{3i}{16}W^{-5}\lambda{}^{\beta i}\lambda{}_{\beta}{}^{j}\lambda{}^{\gamma k}\lambda{}_{\gamma}{}^{r}\lambda{}^{\delta}{}_{k}W{}_{\eta \delta} +\frac{3i}{32}W^{-6}\lambda{}^{\beta i}\lambda{}_{\beta}{}^{j}\lambda{}^{\gamma k}\lambda{}_{\gamma}{}^{l}\lambda{}_{\eta k}X{}^{r}{}_{l}\\
&-\frac{3i}{32}W^{-6}\lambda{}^{\beta i}\lambda{}_{\beta}{}^{j}\lambda{}^{\gamma k}\lambda{}_{\gamma}{}^{r}\lambda{}^{\delta}{}_{k}(\Gamma{}^{a}){}_{\eta \delta}\big(\nabla_{a}W\big)
\end{aligned}
\tag{S3-H6.1-b}
```

**Check for H6.1:** all 25 written summands have weight $`7/2`$, odd parity and the same free indices $`\eta;r,i,j`$. Dummy labels are paired. The coefficient $`1/3`$ and the two external epsilons are applied once, when collecting the spinor.

#### Input H6.2

The calculated input is

```math
\left.H^{ij}\right|_{\mathrm{H6.2}}=W^{-6}\big(\frac{3i}{16}\lambda^{\alpha i}\lambda_\alpha^k\lambda^{\beta j}\lambda_\beta^l\lambda_k^\gamma\lambda_{\gamma l}\big).
\tag{S3-H6.2-input}
```

Apply the product rule (S3-09), in the displayed factor order:

```math
\begin{aligned}
\left.\nabla_\eta^rH^{ij}\right|_{\mathrm{H6.2}}=&\frac{3i}{16}\nabla_{\eta}^{r}\big(W^{-6}\big)\lambda{}^{\beta i}\lambda{}_{\beta}{}^{k}\lambda{}^{\gamma j}\lambda{}_{\gamma}{}^{l}\lambda{}^{\delta}{}_{k}\lambda{}_{\delta l} +\frac{3i}{16}W^{-6}\nabla_{\eta}^{r}\big(\lambda{}^{\beta i}\big)\lambda{}_{\beta}{}^{k}\lambda{}^{\gamma j}\lambda{}_{\gamma}{}^{l}\lambda{}^{\delta}{}_{k}\lambda{}_{\delta l}\\
&-\frac{3i}{16}W^{-6}\lambda{}^{\beta i}\nabla_{\eta}^{r}\big(\lambda{}_{\beta}{}^{k}\big)\lambda{}^{\gamma j}\lambda{}_{\gamma}{}^{l}\lambda{}^{\delta}{}_{k}\lambda{}_{\delta l} +\frac{3i}{16}W^{-6}\lambda{}^{\beta i}\lambda{}_{\beta}{}^{k}\nabla_{\eta}^{r}\big(\lambda{}^{\gamma j}\big)\lambda{}_{\gamma}{}^{l}\lambda{}^{\delta}{}_{k}\lambda{}_{\delta l}\\
&-\frac{3i}{16}W^{-6}\lambda{}^{\beta i}\lambda{}_{\beta}{}^{k}\lambda{}^{\gamma j}\nabla_{\eta}^{r}\big(\lambda{}_{\gamma}{}^{l}\big)\lambda{}^{\delta}{}_{k}\lambda{}_{\delta l} +\frac{3i}{16}W^{-6}\lambda{}^{\beta i}\lambda{}_{\beta}{}^{k}\lambda{}^{\gamma j}\lambda{}_{\gamma}{}^{l}\nabla_{\eta}^{r}\big(\lambda{}^{\delta}{}_{k}\big)\lambda{}_{\delta l}\\
&-\frac{3i}{16}W^{-6}\lambda{}^{\beta i}\lambda{}_{\beta}{}^{k}\lambda{}^{\gamma j}\lambda{}_{\gamma}{}^{l}\lambda{}^{\delta}{}_{k}\nabla_{\eta}^{r}\big(\lambda{}_{\delta l}\big)
\end{aligned}
\tag{S3-H6.2-a}
```

Insert the elementary source identities and the applicable commutators (S3-11)–(S3-14), distribute the vector product rules, and contract only index-raising metrics. The resulting contribution is

```math
\begin{aligned}
\left.\nabla_\eta^rH^{ij}\right|_{\mathrm{H6.2}}=&\frac{9}{8}W^{-7}\lambda{}_{\eta}{}^{r}\lambda{}^{\beta i}\lambda{}_{\beta}{}^{k}\lambda{}^{\gamma j}\lambda{}_{\gamma}{}^{l}\lambda{}^{\delta}{}_{k}\lambda{}_{\delta l} -\frac{3i}{8}W^{-6}\varepsilon{}^{r i}F{}_{\eta}{}^{\beta}\lambda{}_{\beta}{}^{k}\lambda{}^{\gamma j}\lambda{}_{\gamma}{}^{l}\lambda{}^{\delta}{}_{k}\lambda{}_{\delta l}\\
&-\frac{3i}{8}W^{-5}\varepsilon{}^{r i}W{}_{\eta}{}^{\beta}\lambda{}_{\beta}{}^{k}\lambda{}^{\gamma j}\lambda{}_{\gamma}{}^{l}\lambda{}^{\delta}{}_{k}\lambda{}_{\delta l} +\frac{3i}{16}W^{-6}X{}^{r i}\lambda{}_{\eta}{}^{k}\lambda{}^{\beta j}\lambda{}_{\beta}{}^{l}\lambda{}^{\gamma}{}_{k}\lambda{}_{\gamma l}\\
&-\frac{3i}{16}W^{-6}\varepsilon{}^{r i}(\Gamma{}^{a}){}_{\eta}{}^{\beta}\big(\nabla_{a}W\big)\lambda{}_{\beta}{}^{k}\lambda{}^{\gamma j}\lambda{}_{\gamma}{}^{l}\lambda{}^{\delta}{}_{k}\lambda{}_{\delta l} +\frac{3i}{8}W^{-6}\lambda{}^{\beta i}F{}_{\eta \beta}\lambda{}^{\gamma j}\lambda{}_{\gamma}{}^{k}\lambda{}^{\delta r}\lambda{}_{\delta k}\\
&+\frac{3i}{8}W^{-5}\lambda{}^{\beta i}W{}_{\eta \beta}\lambda{}^{\gamma j}\lambda{}_{\gamma}{}^{k}\lambda{}^{\delta r}\lambda{}_{\delta k} +\frac{3i}{16}W^{-6}\lambda{}_{\eta}{}^{i}X{}^{r k}\lambda{}^{\beta j}\lambda{}_{\beta}{}^{l}\lambda{}^{\gamma}{}_{k}\lambda{}_{\gamma l}\\
&+\frac{3i}{16}W^{-6}\lambda{}^{\beta i}(\Gamma{}^{a}){}_{\eta \beta}\big(\nabla_{a}W\big)\lambda{}^{\gamma j}\lambda{}_{\gamma}{}^{k}\lambda{}^{\delta r}\lambda{}_{\delta k} -\frac{3i}{8}W^{-6}\lambda{}^{\beta i}\lambda{}_{\beta}{}^{k}\varepsilon{}^{r j}F{}_{\eta}{}^{\gamma}\lambda{}_{\gamma}{}^{l}\lambda{}^{\delta}{}_{k}\lambda{}_{\delta l}\\
&-\frac{3i}{8}W^{-5}\lambda{}^{\beta i}\lambda{}_{\beta}{}^{k}\varepsilon{}^{r j}W{}_{\eta}{}^{\gamma}\lambda{}_{\gamma}{}^{l}\lambda{}^{\delta}{}_{k}\lambda{}_{\delta l} +\frac{3i}{16}W^{-6}\lambda{}^{\beta i}\lambda{}_{\beta}{}^{k}X{}^{r j}\lambda{}_{\eta}{}^{l}\lambda{}^{\gamma}{}_{k}\lambda{}_{\gamma l}\\
&-\frac{3i}{16}W^{-6}\lambda{}^{\beta i}\lambda{}_{\beta}{}^{k}\varepsilon{}^{r j}(\Gamma{}^{a}){}_{\eta}{}^{\gamma}\big(\nabla_{a}W\big)\lambda{}_{\gamma}{}^{l}\lambda{}^{\delta}{}_{k}\lambda{}_{\delta l} +\frac{3i}{8}W^{-6}\lambda{}^{\beta i}\lambda{}_{\beta}{}^{k}\lambda{}^{\gamma j}F{}_{\eta \gamma}\lambda{}^{\delta}{}_{k}\lambda{}_{\delta}{}^{r}\\
&+\frac{3i}{8}W^{-5}\lambda{}^{\beta i}\lambda{}_{\beta}{}^{k}\lambda{}^{\gamma j}W{}_{\eta \gamma}\lambda{}^{\delta}{}_{k}\lambda{}_{\delta}{}^{r} +\frac{3i}{16}W^{-6}\lambda{}^{\beta i}\lambda{}_{\beta}{}^{k}\lambda{}_{\eta}{}^{j}X{}^{r l}\lambda{}^{\gamma}{}_{k}\lambda{}_{\gamma l}\\
&+\frac{3i}{16}W^{-6}\lambda{}^{\beta i}\lambda{}_{\beta}{}^{k}\lambda{}^{\gamma j}(\Gamma{}^{a}){}_{\eta \gamma}\big(\nabla_{a}W\big)\lambda{}^{\delta}{}_{k}\lambda{}_{\delta}{}^{r} +\frac{3i}{8}W^{-6}\lambda{}^{\beta i}\lambda{}_{\beta}{}^{r}\lambda{}^{\gamma j}\lambda{}_{\gamma}{}^{k}F{}_{\eta}{}^{\delta}\lambda{}_{\delta k}\\
&+\frac{3i}{8}W^{-5}\lambda{}^{\beta i}\lambda{}_{\beta}{}^{r}\lambda{}^{\gamma j}\lambda{}_{\gamma}{}^{k}W{}_{\eta}{}^{\delta}\lambda{}_{\delta k} +\frac{3i}{16}W^{-6}\lambda{}^{\beta i}\lambda{}_{\beta}{}^{k}\lambda{}^{\gamma j}\lambda{}_{\gamma}{}^{l}X{}^{r}{}_{k}\lambda{}_{\eta l}\\
&+\frac{3i}{16}W^{-6}\lambda{}^{\beta i}\lambda{}_{\beta}{}^{r}\lambda{}^{\gamma j}\lambda{}_{\gamma}{}^{k}(\Gamma{}^{a}){}_{\eta}{}^{\delta}\big(\nabla_{a}W\big)\lambda{}_{\delta k} -\frac{3i}{8}W^{-6}\lambda{}^{\beta i}\lambda{}_{\beta}{}^{k}\lambda{}^{\gamma j}\lambda{}_{\gamma}{}^{r}\lambda{}^{\delta}{}_{k}F{}_{\eta \delta}\\
&-\frac{3i}{8}W^{-5}\lambda{}^{\beta i}\lambda{}_{\beta}{}^{k}\lambda{}^{\gamma j}\lambda{}_{\gamma}{}^{r}\lambda{}^{\delta}{}_{k}W{}_{\eta \delta} +\frac{3i}{16}W^{-6}\lambda{}^{\beta i}\lambda{}_{\beta}{}^{k}\lambda{}^{\gamma j}\lambda{}_{\gamma}{}^{l}\lambda{}_{\eta k}X{}^{r}{}_{l}\\
&-\frac{3i}{16}W^{-6}\lambda{}^{\beta i}\lambda{}_{\beta}{}^{k}\lambda{}^{\gamma j}\lambda{}_{\gamma}{}^{r}\lambda{}^{\delta}{}_{k}(\Gamma{}^{a}){}_{\eta \delta}\big(\nabla_{a}W\big)
\end{aligned}
\tag{S3-H6.2-b}
```

**Check for H6.2:** all 25 written summands have weight $`7/2`$, odd parity and the same free indices $`\eta;r,i,j`$. Dummy labels are paired. The coefficient $`1/3`$ and the two external epsilons are applied once, when collecting the spinor.

## 5. Consistency Checks

### 5.1 Index structure, weight and parity

<!-- ASSERT_CONVENTION: source_frame=Gold traceless Standard-Weyl superspace, derivative_parity=odd left, fermions=all degrees retained -->

Every displayed contribution is checked for one lower spinor index $`\eta`$, three upper SU(2) indices $`r,i,j`$, and one upper/lower occurrence of each dummy label. Contracting with $`\varepsilon^{\alpha\eta}\varepsilon_{jr}/3`$ leaves precisely $`\alpha,i`$. No gamma-matrix transpose or fermion exchange is used in collecting the answer. The weight is

```math
\mathbb D\varphi^{\alpha i}
=\tfrac13[\mathbb D,\nabla_j^\alpha]H^{ij}+\tfrac13\nabla_j^\alpha(\mathbb DH^{ij})
=\big(\tfrac12+3\big)\varphi^{\alpha i}=\tfrac72\varphi^{\alpha i}.
\tag{S3-150}
```

The even primary differentiated once is odd. Directly, $`w(\mathcal T)=1`$, $`w(\mathcal R(M,J,\mathbb D))=3/2`$, $`w(\mathcal R(S))=2`$ and $`w(\mathcal R(K))=5/2`$ make each commutator contribution have the weight of the derivative it replaces. Concrete exact rational weight/index checks and the independent seven-derivative test are recorded in [the step-3 report](../../../../../../../references/source_evidence/log/results/gauged_full_fermionic_log/sources/step3/checks.json); their scopes are not interchangeable.

### 5.2 Bosonic limit and the seven-gaugino endpoint

Set every odd superfield and its vector derivatives to zero only for this test. Then the spinor–vector curvatures $`\mathcal R(M,J,\mathbb D,K)`$ vanish by (S3-05)–(S3-06); $`\mathcal T`$ and $`\mathcal R(S)`$ may remain. Each surviving-looking product still contains an odd original field or derivative. Hence the complete spinor becomes zero. This follows term by term from the odd parity and the displayed geometric definitions, without a bosonic equation of motion.

The last denominator is $`W^{-7}`$. It can arise only by differentiating the denominator of the two sextic inputs, because the elementary derivative rules introduce no inverse scalar. Including $`1/3`$ gives

```math
\begin{aligned}
\left.\varphi_{\log W}^{\alpha i}\right|_{W^{-7}}={}&\varepsilon^{\alpha\eta}\varepsilon_{jr}W^{-7}\Big\{
\tfrac3{16}\lambda_\eta^r\lambda^{\beta i}\lambda_\beta^j\lambda^{\gamma k}\lambda_\gamma^l\lambda_k^\delta\lambda_{\delta l}
+\tfrac38\lambda_\eta^r\lambda^{\beta i}\lambda_\beta^k\lambda^{\gamma j}\lambda_\gamma^l\lambda_k^\delta\lambda_{\delta l}\Big\}.
\end{aligned}
\tag{S3-151}
```

The coefficients are $`(1/3)(-6i)(3i/32)=3/16`$ and $`(1/3)(-6i)(3i/16)=3/8`$. Its weight is $`-7+7(3/2)=7/2`$. The new leftmost gaugino has not been moved through the existing six. This independently checks the largest denominator and highest explicit fermion degree.

### 5.3 Curved-commutator check against the primary calculation

Take the SU(2) component $`+=1`$, $`-=2`$. The source curvature (S3-05) and generator action (S3-07) give

```math
\begin{aligned}
\tfrac32\mathcal R(\mathbb D)_{a\eta}{}^+\lambda_\beta^+
&=-\tfrac38(\Gamma_a)_\eta{}^\gamma X_\gamma^+\lambda_\beta^+,\\
\mathcal R(J)_{a\eta}{}^{+kl}J_{kl}\lambda_\beta^+
&=2\mathcal R(J)_{a\eta}{}^{++-}J_{+-}\lambda_\beta^+
=2\big[-\tfrac38(\Gamma_a)_\eta{}^\gamma X_\gamma^+\big]\big[-\tfrac12\lambda_\beta^+\big]\\
&=+\tfrac38(\Gamma_a)_\eta{}^\gamma X_\gamma^+\lambda_\beta^+.
\end{aligned}
\tag{S3-156}
```

Here $`\mathcal R(J)_{a\eta}{}^{+++}=0`$ because $`\varepsilon^{++}=0`$, and $`J_{--}\lambda_\beta^+=0`$ by (S3-07), so only the two equal mixed-index terms contribute. The dilatation and SU(2) terms cancel locally, without commuting their odd factors. Since $`\varepsilon^{++}=0`$, $`\nabla_\eta^+\lambda_\beta^+=-\varepsilon_{\eta\beta}X^{++}`$. The complete remaining commutator is

```math
[\nabla_\eta^+,\nabla_a]\lambda_\beta^+
=-\mathcal T_{a\eta}{}^\gamma\varepsilon_{\gamma\beta}X^{++}
+\tfrac12\mathcal R(M)_{a\eta}{}^{+,bc}(\Sigma_{bc})_\beta{}^\gamma\lambda_\gamma^+
-2i\mathcal R(S)_{a\eta}{}^{+,\gamma+}\varepsilon_{\gamma\beta}W.
\tag{S3-157}
```

This reproduces both the scalar-degree-zero and scalar-degree-one commutators independently derived in (S2-158). The comparison checks the SU(2) lowering sign, dilatation weight, Lorentz coefficient and S-curvature contribution. It does not remove the K curvature from the subsequent commutator on $`\nabla_a\lambda`$.

### 5.4 Independent check against seven spinor derivatives

The source definition implies

```math
\varphi_{\log W}^{\alpha i}
=\frac{i}{1280}\nabla_j^\alpha\nabla^{(ij}\nabla^{kl)}\nabla_{kl}\log W.
\tag{S3-152}
```

The independent test evaluates these ordered derivatives in flat superspace with constant $`F_{ab}`$, $`X^{ij}`$ and $`\partial_aW`$, retaining all eight independent gaugino Grassmann generators. In this restricted test $`\partial_a\lambda=0`$ and the Weyl multiplet vanishes. The expanded candidate is evaluated by finite tensor contractions, while the right-hand side is evaluated as ordered derivative words on exterior polynomials. The latter does not use the new curved commutator expansion. The comparison denominator is $`1280\times24\times3=92160`$ when using the earlier six-derivative numerator. The report lists each case and its coefficient comparisons.

All **13 probes pass**, with **12,544 coefficient comparisons**, including vanishing coefficients, and a separate comparison of the index-raised printed expression. The independent [gradient check](../../../../../../../references/source_evidence/log/results/gauged_full_fermionic_log/sources/step3/gradient_x_checks.json) additionally tests all **15 components of $`\partial_aX^{ij}`$** in the $`W^{-4}\lambda^3\partial X`$ sector. It evaluates the original seven-derivative operator through $`\varphi_\eta^+=-\nabla_\eta^-H^{++}/2`$ and compares it with the direct trace (S3-01). It therefore tests propagation of the corrected H3.9 coefficient beyond the constant-$`X`$ probes.

These checks verify nontrivial all-fermion limits. They do **not** establish the full curved comparison with C24 supplement §2.2.1 or the full S/K Ward identities. Curvature contributions were derived using the displayed operator and representation identities; no flat probe is described as checking them.

Reproduction scripts: [verify_log_step3_spinor.py](../../../../../../../references/source_evidence/log/results/gauged_full_fermionic_log/scripts/verify_log_step3_spinor.py) and [verify_log_step3_gradient_x.py](../../../../../../../references/source_evidence/log/results/gauged_full_fermionic_log/scripts/verify_log_step3_gradient_x.py), with Python and NumPy; the [component evidence guide](../../../../../../../references/source_evidence/README.md) states their source-relative input dependencies. The [source-rule transcription and contraction checks](../../../../../../../references/source_evidence/log/results/gauged_full_fermionic_log/scripts/log_step3_covariant_rules.py) contain the exact coefficients used to audit the written algebra; all derivation steps are displayed above.

### 5.5 What the transformation checks establish

The input's linear constraint establishes (S3-10), preserving the primary-to-spinor Q relation. Weight and tensor type were checked above. The S action exposes the inherited primary gate. C24 (A.1k), $`M_{ab}H^{ij}=0`$ and $`\mathbb DH^{ij}=3H^{ij}`$ give

```math
\begin{aligned}
S_\kappa^k\varphi_\beta^i
&=\tfrac13\varepsilon_{jl}\{S_\kappa^k,\nabla_\beta^l\}H^{ij}-\tfrac13\nabla_{\beta j}(S_\kappa^kH^{ij}),\\
\varepsilon_{jl}J^{kl}H^{ij}
&=\tfrac12\varepsilon_{jl}\big(\varepsilon^{ik}H^{lj}+\varepsilon^{il}H^{kj}+\varepsilon^{jk}H^{il}+\varepsilon^{jl}H^{ki}\big)\\
&=\tfrac12(0-H^{ki}-H^{ki}-2H^{ki})=-2H^{ki},\\
S_\kappa^k\varphi_\beta^i
&=\underbrace{(-2-4)}_{-6}\varepsilon_{\kappa\beta}H^{ki}-\tfrac13\nabla_{\beta j}(S_\kappa^kH^{ij}).
\end{aligned}
\tag{S3-153}
```

The zero contracts antisymmetric $`\varepsilon_{jl}`$ with symmetric $`H^{lj}`$. The $`-2`$ in the last line is the dilatation contribution; $`-4`$ is the SU(2) contribution. The minus before the final derivative comes from moving odd S through the odd spinor derivative. Thus the source S law follows when the primary S gate is established; quoting the law does not certify the full-primary S gate, now independently verified in the current certificate.

Likewise, using $`[K_a,\nabla_\beta^l]=i(\Gamma_a)_\beta{}^\gamma S_\gamma^l`$,

```math
K_a\varphi_\beta^i
=\tfrac i3(\Gamma_a)_\beta{}^\gamma S_{\gamma j}H^{ij}+\tfrac13\nabla_{\beta j}(K_aH^{ij}).
\tag{S3-154}
```

This becomes zero when both primary gates vanish. These exact residual equations now vanish by the independently certified full-primary S/K identities.

The spinor Q law, C24 (2.41b), uses the scalar and vector descendants constructed in Steps 4–5 and certified at the retained order:

```math
\nabla_\beta^j\varphi_\gamma^i=-\tfrac i2\varepsilon^{ji}\varepsilon_{\beta\gamma}F_{\log W}
+\tfrac i2\varepsilon^{ji}\mathcal H_{\beta\gamma,\log W}+i\nabla_{\beta\gamma}H_{\log W}^{ji}.
\tag{S3-155}
```

This is a **source target identity**, not a performed full-component verification. Its component form is C24 (2.52b), inspected on [Components of curvature-squared invariants of minimal supergravity in five dimensions — PDF22](https://arxiv.org/abs/2311.00679). Projection must also retain (2.53b)'s gravitino and S-connection terms. Retained-order reality and the multiplet transformation identities are now certified through the full-primary and projection certificates; no chirality condition is imposed in five dimensions. An all-fermion expanded variation is outside the certified display scope.

## 6. Convention Dependence and Remaining Uncertainties

The input is our primary with the corrected H3.9 sign. Descending it instead of literal S23 (3.25) adds twice the contribution displayed for H3.9, including the denominator derivative and all three numerator-factor derivatives. Its subsection makes each term inspectable. This change uses neither integration by parts nor a gauge restriction.

The endpoint is a complete **covariant derivative expansion in the declared geometric basis**. It has not been reduced to the Weyl-field basis of the seven-page C24 supplement, nor has every displayed geometric curvature been replaced by (S3-05)–(S3-06). These standard tensors are fully defined, with no missing-fermion placeholder. The output is not the final gauge-fixed component spinor or the gauged LOG action.

Full-primary defining-projector equality and curved S/K/linearity now pass. Project-frame projection, canonicalization, reality, current conservation and BF construction are certified through the retained order in [the current certificate](../CERTIFICATION_LOG_TWO_FERMI_2026-09-25.md). The conservation and supersymmetry conclusions use verified multiplet premises and the complete superform proof; a separate brute-force variation of all expanded terms is not claimed. The all-fermion descendant comparison to every literal C24 term is outside that certificate. There is no approximation or discarded fermion order, so no perturbative error estimate applies. No source PDF, primary coefficient, bridge, compensator gauge or action normalization is changed.

References used: S23 (2.6), (2.8), (2.12)–(2.15), (2.20)–(2.24), (3.24)–(3.26a); C24 (2.41)–(2.44), (2.52)–(2.53), (A.1), (A.3). The component comparison is C24 supplement §2.2.1, cached [Components of curvature-squared invariants of minimal supergravity in five dimensions — PDF106](https://arxiv.org/abs/2311.00679) through [Components of curvature-squared invariants of minimal supergravity in five dimensions — PDF112](https://arxiv.org/abs/2311.00679). Its first page was inspected to identify its different basis; its coefficients are not derivation inputs here.

## 7. Final Result

Under A1–A4, all 58 differentiated inputs give the following single expression. The common factor implements S23 (3.26a). Every summand is displayed, grouped by the explicit scalar power, with several summands per row. Torsions/curvatures mean (S3-05)–(S3-06), and every remaining derivative is a **vector** covariant derivative. No intermediate coefficient polynomial occurs. Redundant contractions are retained to preserve provenance; the written summand count is not a count of independent tensor structures.


[Previous component](derivation_003.md) · [Component index](../STEP_03_LOG_SPINOR.md) · [Next component](derivation_005.md)
