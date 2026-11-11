# Preservation of gauge conditions under SUSY

The working conditions are fixed as

```math
\sigma=1,\qquad \psi^i=0,\qquad b_\mu=0,\qquad
L^{ij}=\frac L{\sqrt2}\delta^{ij},\qquad L>0
```

Here $`\psi^i`$ is the dilatino; the gravitino $`\psi_\mu^i`$ and independent fermion $`\varphi^i`$ are retained. This file solves the compensating $`S`$, $`K`$, and broken $`SU(2)`$ transformation parameters by varying these conditions. The residual $`U(1)`$ parameter remains free.

The input definitions are the [convention record](../conventions.md), [§4.3 of the two-derivative construction](../two_derivative_action/details/construction.md), and [sections W01, V01, and L01 of the covariant rules](../../log/action/details/covariant_rules.md).

<a id="1-s-parameter"></a>

## S parameter

The gaugino transformation of the defining vector and the triplet definition are

```math
\begin{aligned}
\delta\psi^i={}&-\frac14\gamma^{ab}\widehat G_{ab}\epsilon^i
-\frac i2\gamma^a\mathcal D_a\sigma\,\epsilon^i
+\sigma\gamma^{ab}T_{ab}\epsilon^i-Y^{ij}\epsilon_j
+\sigma\eta^i,\\
Y^{ij}\big|_{\mathrm P}&=-\frac g2 L^{ij},\qquad
\mathcal D_a\sigma\big|_{\mathrm P}=0
\end{aligned}
```

so preservation of the gauge condition requires

```math
\begin{aligned}
0=\delta\psi^i\big|_{\mathrm P}
&=\left(-\frac14\gamma^{ab}\widehat G_{ab}
+\gamma^{ab}T_{ab}\right)\epsilon^i
+\frac g2 L^{ij}\epsilon_j+\eta^i,\\
\eta^i
&=\left(\frac14\widehat G_{ab}-T_{ab}\right)
\gamma^{ab}\epsilon^i-\frac g2 L^{ij}\epsilon_j.
\end{aligned}
```

Substituting $`T_{ab}=\widehat G_{ab}/8+ \varepsilon_{abcde}\widehat H^{cde}/48`$ gives

```math
\boxed{
\eta^i=
\left(\frac18\widehat G_{ab}
-\frac1{48}\varepsilon_{abcde}\widehat H^{cde}\right)
\gamma^{ab}\epsilon^i
-\frac{gL}{2\sqrt2}\delta^{ij}\epsilon_j.}
```

Back-substituting into the first variation makes the curvature, $`T`$, and $`gL`$ coefficients vanish separately. No numerical values are chosen for $`g`$ or $`L`$.

<a id="2-k-parameter"></a>

## K parameter

The transformation of $`b_\mu`$ is

```math
\delta b_\mu=\frac i2\bar\epsilon\phi_\mu
-2\bar\epsilon\gamma_\mu\chi
+\frac i2\bar\eta\psi_\mu+2\Lambda_{K\mu}
```

so the equation $`\delta b_\mu=0`$ gives

```math
\boxed{
\Lambda_{K\mu}=-\frac i4\bar\epsilon\phi_\mu
+\bar\epsilon\gamma_\mu\chi
-\frac i4\bar\eta\psi_\mu}
```

Back-substitution yields $`i/2-i/2=0`$, $`-2+2=0`$, and $`i/2-i/2=0`$ for the three structures, respectively.

<a id="3-converting-the-su2-parameter-to-the-working-convention"></a>

## Converting the SU(2) parameter to the working convention

The generator sign is fixed by the covariant derivative:

```math
\begin{aligned}
\mathcal D_\mu L^{ij}
&=\partial_\mu L^{ij}-3b_\mu L^{ij}
+2V_\mu{}^{(i}{}_kL^{j)k}-i\bar\psi_\mu^{(i}\varphi^{j)},\\
\left.\mathcal D_\mu\right|_U&=-\delta_U(V_\mu),\\
\delta_U(\lambda)L^{ij}&=-2\lambda^{(i}{}_kL^{j)k}.
\end{aligned}
```

Temporarily define the symmetric bilinear and its traceless part by

```math
B^{ij}:=\bar\epsilon^{(i}\varphi^{j)},\qquad
S^{ij}:=B^{ij}-\frac12\delta^{ij}\delta_{k\ell}B^{k\ell}
```

Using $`\delta_Q L^{ij}=iB^{ij}`$ and $`\delta_SL^{ij}=0`$,

```math
\begin{aligned}
\delta L^{ij}
&=iB^{ij}-\sqrt2L\lambda^{(i}{}_k\delta^{j)k},\\
0=\left(\delta L^{ij}\right)_{\mathrm{traceless}}
&=iS^{ij}-\sqrt2L\lambda^{(i}{}_k\delta^{j)k}.
\end{aligned}
```

The NW–SE rules give $`\lambda^i{}_k=\lambda^{ij}\epsilon_{jk}`$. To solve the last equation without assigning numbers to any components, write

```math
S=\begin{pmatrix}s&t\\t&-s\end{pmatrix},\quad
\lambda=\begin{pmatrix}a&b\\b&c\end{pmatrix},\quad
\epsilon=\begin{pmatrix}0&1\\-1&0\end{pmatrix}
```

The components $`s,t`$ are independent and symbolic. Then

```math
\begin{aligned}
\mathop{\mathrm{sym}}\nolimits(\lambda\epsilon)
&=\begin{pmatrix}-b&(a-c)/2\$a-c)/2&b\end{pmatrix},\\
is+\sqrt2Lb&=0,\qquad
it-\frac{L}{\sqrt2}(a-c)=0.
\end{aligned}
```

These two equations impose no condition on the trace $`\vartheta:=a+c`$. The quantity $`\vartheta`$ is the residual $`U(1)`$ parameter. The solution is

```math
\begin{aligned}
b&=-\frac{is}{\sqrt2L},\\
a&=\frac\vartheta2+\frac{it}{\sqrt2L},\qquad
c=\frac\vartheta2-\frac{it}{\sqrt2L},\\
\lambda&=-\frac{i}{\sqrt2L}S\epsilon
+\frac\vartheta2\mathbf1
\end{aligned}
```

This division is defined on the branch $`L>0`$. Directly in matrix form,

```math
\mathop{\mathrm{sym}}\nolimits\left[
\left(-\frac{i}{\sqrt2L}S\epsilon
+\frac\vartheta2\mathbf1\right)\epsilon\right]
=\frac{i}{\sqrt2L}S
```

because $`\epsilon^2=-\mathbf1`$ and $`\mathop{\mathrm{sym}}\nolimits(\epsilon)=0`$. Thus the traceless part of the variation is $`iS-\sqrt2L(iS/\sqrt2L)=0`$.

In the original spinors, the result is:

```math
\boxed{
\lambda^{ij}=-\frac{i}{4\sqrt2L}
\left[
(\bar\epsilon^k\varphi^i+\bar\epsilon^i\varphi^k)\delta^{j\ell}
+(\bar\epsilon^k\varphi^j+\bar\epsilon^j\varphi^k)\delta^{i\ell}
\right]\epsilon_{k\ell}
+\frac\vartheta2\delta^{ij}.}
```

The trace-subtraction term $`\delta^{k(i}\delta^{j)\ell}\epsilon_{k\ell} =(\epsilon_{ij}+\epsilon_{ji})/2=0`$ drops out in the last line. An equivalent compact expression is $`-iS^{k(i}\delta^{j)\ell}\epsilon_{k\ell}/(\sqrt2L) +\vartheta\delta^{ij}/2`$, where $`S^{ij}`$ is the traceless part of the bilinear above. The free parameter $`\vartheta`$ is not fixed.

Directly using the parameter with coefficient $`-1/(\sqrt2L)`$ in construction equation (4.14) with this generator definition leaves

```math
\left(\delta L^{ij}\right)_{\mathrm{traceless}}
=(i-1)S^{ij}
```

Thus the required factor in the working parameter is $`-i/(\sqrt2L)`$. The checked transformation depends on the explicitly defined $`\delta_U`$ sign above.

Taking the trace in the same calculation gives

```math
\boxed{\delta L=\frac i{\sqrt2}\delta_{ij}
\bar\epsilon^i\varphi^j}
```

Both the traceless gauge condition and the transformation of the independent field $`L`$ are thereby obtained.

<a id="4-susy-check-order-for-the-two-fermion-action"></a>

## SUSY-check order for the two-fermion action

Let $`n`$ denote physical fermion number; $`\epsilon`$ is not counted. The quantity $`S^{(n)}`$ is the degree-$`n`$ part of the action. The contribution $`\delta_{-1}`$ lowers fermion degree by one, while $`\delta_{+1}`$ raises it by one.

Degree counting directly gives

```math
\begin{aligned}
\left[\delta S\right]_{1}
&=\delta_{+1}S^{(0)}+\delta_{-1}S^{(2)},\\
\left[\delta S\right]_{3}
&=\delta_{+3}S^{(0)}+\delta_{+1}S^{(2)}
+\delta_{-1}S^{(4)}
\end{aligned}
```

Hence the local two-fermion action-invariance condition, including its boundary current, is

```math
\delta_{+1}\bigl(e\ell^{(0)}\bigr)
+\delta_{-1}\bigl(e\ell^{(2)}\bigr)
=\partial_\mu J_{(1)}^\mu
```

Here $`J_{(1)}^\mu`$ is a local density current of fermion degree one. This line defines the target identity; it is not an invariance result replacing the gauge-preservation identities proved in the preceding sections.
