# $`\mathcal F_{AB}`$: initial expressions and first three derivatives

Source: multiplets.pdf,
(2.14) and (2.6). SU(2) index conventions:
[CONVENTIONS.md](CONVENTIONS.md).

<a id="1-multiplet-names-and-initial-expressions"></a>

## Multiplet names and initial expressions

Bold symbols name multiplets; component fields are not bold:

```math
\begin{aligned}
\mathbf L_A&=\bigl(L_A^{ij},\varphi_A^i,E_A^a,N_A\bigr),\\
\mathbf V_A&=\bigl(\rho_A,A_{\mu A},\lambda_A^i,Y_A^{ij}\bigr),
\qquad A=1,2.
\end{aligned}
```

For each linear multiplet, the scalar norm is defined as

```math
L_A\equiv\sqrt{L_{A\,ij}L_A^{ij}}
\qquad(A\text{ is not summed})
```

Here $`L_A`$ is the norm of the triplet component,
not the name of the multiplet $`\mathbf L_A`$.

The choice in the paper's (2.14) is:

```math
\boxed{
\mathcal F_{11}=L_2^{-1},\qquad
\mathcal F_{12}=-L_2^{-3}L_{2\,pq}L_1^{pq},\qquad
\mathcal F_{21}=\mathcal F_{22}=0.
}
```

All expressions are defined in the region $`L_2\neq0`$. Derivative definitions
in (2.6) and their extension to third order are:

```math
\begin{aligned}
\mathcal F_{ABC}{}^{ij}
&\equiv\frac{\partial\mathcal F_{AB}}{\partial L_{C\,ij}},\\
\mathcal F_{ABCD}{}^{ij\,km}
&\equiv\frac{\partial^2\mathcal F_{AB}}
{\partial L_{C\,ij}\,\partial L_{D\,km}},\\
\mathcal F_{ABCDE}{}^{ij\,km\,rs}
&\equiv\frac{\partial^3\mathcal F_{AB}}
{\partial L_{C\,ij}\,\partial L_{D\,km}\,\partial L_{E\,rs}},
\qquad A,B,C,D,E\in\{1,2\}.
\end{aligned}
```

<a id="2-derivative-identities"></a>

## Derivative identities

```math
L_{A\,ij}=L_{A\,ji},\qquad
L_A^{ij}=\epsilon^{ip}\epsilon^{jq}L_{A\,pq},
\qquad
\epsilon_{12}=\epsilon^{12}=1.
```

With unit-weight symmetrization,

```math
\begin{aligned}
\frac{\partial L_{A\,pq}}{\partial L_{B\,ij}}
&=\delta_{AB}\delta_p^{(i}\delta_q^{j)},\\
\frac{\partial L_A^{pq}}{\partial L_{B\,ij}}
&=\delta_{AB}\epsilon^{p(i}\epsilon^{|q|j)},\\
\epsilon^{i(k}\epsilon^{|j|m)}
&=\frac12\left(\epsilon^{ik}\epsilon^{jm}
+\epsilon^{im}\epsilon^{jk}\right).
\end{aligned}
```

Derivatives of the norm:

```math
\begin{aligned}
\frac{\partial(L_{2\,pq}L_2^{pq})}{\partial L_{2\,ij}}
&=L_2^{ij}
+L_{2\,pq}\epsilon^{p(i}\epsilon^{|q|j)}
=2L_2^{ij},\\
\frac{\partial L_2}{\partial L_{2\,ij}}
&=\frac{1}{2L_2}\,2L_2^{ij}
=\frac{L_2^{ij}}{L_2},\\
\frac{\partial L_2^{-n}}{\partial L_{2\,ij}}
&=-\frac n2(L_{2\,pq}L_2^{pq})^{-\frac n2-1}
\,2L_2^{ij}
=-nL_2^{-n-2}L_2^{ij}.
\end{aligned}
```

Derivatives of the mixed contraction:

```math
\begin{aligned}
\frac{\partial(L_{2\,pq}L_1^{pq})}{\partial L_{1\,ij}}
&=L_{2\,pq}\epsilon^{p(i}\epsilon^{|q|j)}
=L_2^{ij},\\
\frac{\partial(L_{2\,pq}L_1^{pq})}{\partial L_{2\,ij}}
&=\delta_p^{(i}\delta_q^{j)}L_1^{pq}
=L_1^{ij}.
\end{aligned}
```

<a id="3-first-derivatives"></a>

## First derivatives

```math
\begin{aligned}
\mathcal F_{111}{}^{ij}
&=\frac{\partial L_2^{-1}}{\partial L_{1\,ij}}
=0,\\
\mathcal F_{112}{}^{ij}
&=\frac{\partial L_2^{-1}}{\partial L_{2\,ij}}
=-L_2^{-3}L_2^{ij},\\
\mathcal F_{121}{}^{ij}
&=-L_2^{-3}
\frac{\partial(L_{2\,pq}L_1^{pq})}{\partial L_{1\,ij}}
=-L_2^{-3}L_2^{ij},\\
\mathcal F_{122}{}^{ij}
&=-\frac{\partial L_2^{-3}}{\partial L_{2\,ij}}
(L_{2\,pq}L_1^{pq})
-L_2^{-3}
\frac{\partial(L_{2\,pq}L_1^{pq})}{\partial L_{2\,ij}}\\
&=3L_2^{-5}(L_{2\,pq}L_1^{pq})L_2^{ij}
-L_2^{-3}L_1^{ij}.
\end{aligned}
```

All first derivatives:

```math
\boxed{
\begin{aligned}
\mathcal F_{111}{}^{ij}&=0,\\
\mathcal F_{112}{}^{ij}
=\mathcal F_{121}{}^{ij}
&=-\frac{L_2^{ij}}{L_2^3},\\
\mathcal F_{122}{}^{ij}
&=-\frac{L_1^{ij}}{L_2^3}
+\frac{3(L_{2\,pq}L_1^{pq})L_2^{ij}}{L_2^5},\\
\mathcal F_{2BC}{}^{ij}&=0
\qquad(B,C=1,2).
\end{aligned}
}
```

<a id="4-second-derivatives"></a>

## Second derivatives

```math
\begin{aligned}
\mathcal F_{1122}{}^{ij\,km}
=\mathcal F_{1212}{}^{ij\,km}
&=\frac{\partial(-L_2^{-3}L_2^{ij})}
{\partial L_{2\,km}}\\
&=-(-3L_2^{-5}L_2^{km})L_2^{ij}
-L_2^{-3}\epsilon^{i(k}\epsilon^{|j|m)}\\
&=-\frac{\epsilon^{i(k}\epsilon^{|j|m)}}{L_2^3}
+\frac{3L_2^{ij}L_2^{km}}{L_2^5},\\[4pt]
\mathcal F_{1221}{}^{ij\,km}
&=\frac{\partial}{\partial L_{1\,km}}
\left[-L_2^{-3}L_1^{ij}
+3L_2^{-5}(L_{2\,pq}L_1^{pq})L_2^{ij}\right]\\
&=-L_2^{-3}\epsilon^{i(k}\epsilon^{|j|m)}
+3L_2^{-5}L_2^{km}L_2^{ij}.
\end{aligned}
```

```math
\begin{aligned}
\mathcal F_{1222}{}^{ij\,km}
&=\frac{\partial}{\partial L_{2\,km}}
\left[-L_2^{-3}L_1^{ij}
+3L_2^{-5}(L_{2\,pq}L_1^{pq})L_2^{ij}\right]\\
&=3L_2^{-5}L_2^{km}L_1^{ij}\\
&\quad+3\Big[
-5L_2^{-7}L_2^{km}(L_{2\,pq}L_1^{pq})L_2^{ij}
+L_2^{-5}L_1^{km}L_2^{ij}\\
&\hspace{64pt}
+L_2^{-5}(L_{2\,pq}L_1^{pq})
\epsilon^{i(k}\epsilon^{|j|m)}
\Big]\\
&=\frac{3}{L_2^5}
\left[
L_1^{ij}L_2^{km}+L_2^{ij}L_1^{km}
+(L_{2\,pq}L_1^{pq})\epsilon^{i(k}\epsilon^{|j|m)}
\right]\\
&\quad-\frac{15}{L_2^7}
(L_{2\,pq}L_1^{pq})L_2^{ij}L_2^{km}.
\end{aligned}
```

All second derivatives:

```math
\boxed{
\begin{aligned}
\mathcal F_{1111}{}^{ij\,km}
=\mathcal F_{1112}{}^{ij\,km}
=\mathcal F_{1121}{}^{ij\,km}
=\mathcal F_{1211}{}^{ij\,km}
&=0,\\[2pt]
\mathcal F_{1122}{}^{ij\,km}
=\mathcal F_{1212}{}^{ij\,km}
=\mathcal F_{1221}{}^{ij\,km}
&=-\frac{\epsilon^{i(k}\epsilon^{|j|m)}}{L_2^3}
+\frac{3L_2^{ij}L_2^{km}}{L_2^5},\\[2pt]
\mathcal F_{1222}{}^{ij\,km}
&=\frac{3}{L_2^5}
\Big[
L_1^{ij}L_2^{km}+L_2^{ij}L_1^{km}\\
&\qquad
+(L_{2\,pq}L_1^{pq})\epsilon^{i(k}\epsilon^{|j|m)}
\Big]\\
&\quad-\frac{15(L_{2\,pq}L_1^{pq})}{L_2^7}
L_2^{ij}L_2^{km},\\[2pt]
\mathcal F_{2BCD}{}^{ij\,km}&=0
\qquad(B,C,D=1,2).
\end{aligned}
}
```

<a id="5-third-derivatives"></a>

## Third derivatives

Temporary symbols used in the intermediate steps of this section:

```math
S\equiv L_{2\,pq}L_1^{pq},
\qquad
\Delta^{ij,km}\equiv\epsilon^{i(k}\epsilon^{|j|m)}.
```

```math
\begin{aligned}
\mathcal F_{11222}{}^{ij\,km\,rs}
&=\frac{\partial}{\partial L_{2\,rs}}
\left[-L_2^{-3}\Delta^{ij,km}
+3L_2^{-5}L_2^{ij}L_2^{km}\right]\\
&=3L_2^{-5}L_2^{rs}\Delta^{ij,km}
-15L_2^{-7}L_2^{rs}L_2^{ij}L_2^{km}\\
&\quad+3L_2^{-5}
\left(\Delta^{ij,rs}L_2^{km}
+L_2^{ij}\Delta^{km,rs}\right).
\end{aligned}
```

Using the second-derivative equalities gives

```math
\begin{aligned}
\mathcal F_{12122}{}^{ij\,km\,rs}
&=\frac{\partial\mathcal F_{1212}{}^{ij\,km}}
{\partial L_{2\,rs}}
=\frac{\partial\mathcal F_{1122}{}^{ij\,km}}
{\partial L_{2\,rs}}
=\mathcal F_{11222}{}^{ij\,km\,rs},\\
\mathcal F_{12212}{}^{ij\,km\,rs}
&=\frac{\partial\mathcal F_{1221}{}^{ij\,km}}
{\partial L_{2\,rs}}
=\frac{\partial\mathcal F_{1122}{}^{ij\,km}}
{\partial L_{2\,rs}}
=\mathcal F_{11222}{}^{ij\,km\,rs}.
\end{aligned}
```

The other mixed derivative:

```math
\begin{aligned}
\mathcal F_{12221}{}^{ij\,km\,rs}
&=\frac{\partial}{\partial L_{1\,rs}}
\left[
3L_2^{-5}
\left(L_1^{ij}L_2^{km}+L_2^{ij}L_1^{km}
+S\Delta^{ij,km}\right)
-15SL_2^{-7}L_2^{ij}L_2^{km}
\right]\\
&=3L_2^{-5}
\left(\Delta^{ij,rs}L_2^{km}
+L_2^{ij}\Delta^{km,rs}
+L_2^{rs}\Delta^{ij,km}\right)\\
&\quad-15L_2^{-7}L_2^{rs}L_2^{ij}L_2^{km}\\
&=\mathcal F_{11222}{}^{ij\,km\,rs}.
\end{aligned}
```

In the original variables:

```math
\boxed{
\begin{aligned}
\mathcal F_{11222}{}^{ij\,km\,rs}
&=\mathcal F_{12122}{}^{ij\,km\,rs}
=\mathcal F_{12212}{}^{ij\,km\,rs}
=\mathcal F_{12221}{}^{ij\,km\,rs}\\
&=\frac{3}{L_2^5}
\Big[
\epsilon^{i(k}\epsilon^{|j|m)}L_2^{rs}
+\epsilon^{i(r}\epsilon^{|j|s)}L_2^{km}
+\epsilon^{k(r}\epsilon^{|m|s)}L_2^{ij}
\Big]\\
&\quad-\frac{15}{L_2^7}L_2^{ij}L_2^{km}L_2^{rs}.
\end{aligned}
}
```

Third derivative with respect to $`L_{2\,ij}`$ components only:

```math
\begin{aligned}
\mathcal F_{12222}{}^{ij\,km\,rs}
&=\frac{\partial}{\partial L_{2\,rs}}
\left[
3L_2^{-5}
\left(L_1^{ij}L_2^{km}+L_2^{ij}L_1^{km}
+S\Delta^{ij,km}\right)
-15SL_2^{-7}L_2^{ij}L_2^{km}
\right]\\
&=-15L_2^{-7}L_2^{rs}
\left(L_1^{ij}L_2^{km}+L_2^{ij}L_1^{km}
+S\Delta^{ij,km}\right)\\
&\quad+3L_2^{-5}
\left(L_1^{ij}\Delta^{km,rs}
+\Delta^{ij,rs}L_1^{km}
+L_1^{rs}\Delta^{ij,km}\right)\\
&\quad-15L_2^{-7}L_1^{rs}L_2^{ij}L_2^{km}
+105SL_2^{-9}L_2^{rs}L_2^{ij}L_2^{km}\\
&\quad-15SL_2^{-7}
\left(\Delta^{ij,rs}L_2^{km}
+L_2^{ij}\Delta^{km,rs}\right).
\end{aligned}
```

In the original variables:

```math
\boxed{
\begin{aligned}
\mathcal F_{12222}{}^{ij\,km\,rs}
&=\frac{3}{L_2^5}
\Big[
\epsilon^{i(k}\epsilon^{|j|m)}L_1^{rs}
+\epsilon^{i(r}\epsilon^{|j|s)}L_1^{km}
+\epsilon^{k(r}\epsilon^{|m|s)}L_1^{ij}
\Big]\\
&\quad-\frac{15}{L_2^7}
\Big[
L_1^{ij}L_2^{km}L_2^{rs}
+L_2^{ij}L_1^{km}L_2^{rs}
+L_2^{ij}L_2^{km}L_1^{rs}
\Big]\\
&\quad-\frac{15(L_{2\,pq}L_1^{pq})}{L_2^7}
\Big[
\epsilon^{i(k}\epsilon^{|j|m)}L_2^{rs}
+\epsilon^{i(r}\epsilon^{|j|s)}L_2^{km}
+\epsilon^{k(r}\epsilon^{|m|s)}L_2^{ij}
\Big]\\
&\quad+\frac{105(L_{2\,pq}L_1^{pq})}{L_2^9}
L_2^{ij}L_2^{km}L_2^{rs}.
\end{aligned}
}
```

For vanishing components,

```math
\frac{\partial\mathcal F_{11}}{\partial L_{1\,ij}}=0,
\qquad
\frac{\partial^2\mathcal F_{12}}
{\partial L_{1\,ij}\,\partial L_{1\,km}}=0,
\qquad
\mathcal F_{2B}=0,
```

and therefore

```math
\boxed{
\begin{aligned}
\mathcal F_{1BCDE}{}^{ij\,km\,rs}&=0
&&\text{if }\delta_{B1}+\delta_{C1}+\delta_{D1}+\delta_{E1}\geq2,\\
\mathcal F_{2BCDE}{}^{ij\,km\,rs}&=0
&&\text{for all }B,C,D,E\in\{1,2\}\text{}.
\end{aligned}
}
```

The first condition requires at least two of the $`B,C,D,E`$ indices to be $`1`$.
