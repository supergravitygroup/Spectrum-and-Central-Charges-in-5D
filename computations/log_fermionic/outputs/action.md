# Recomputed LOG multiplet and BF density

The full-primary descent supplies these component polynomials; the [component stages](../README.md) describe their construction and the supported checks. Ordered derivatives are full supercovariant operators. Even slots retain degrees 0 and 2; the spinor retains degree 1.

## L: 0 explicit fermions

```math
\begin{aligned}
L_{\log}^{ij}[0]={}&-\frac{1}{3}\widehat R(V){}^{a}{}^{b}{}^{i}{}^{j}\widehat G{}_{a}{}_{b}\\
&-\frac{4}{3}\widehat H{}^{a}{}^{b}\widehat R(V){}_{a}{}_{b}{}^{i}{}^{j}\\
&-gL_c{}^{i}{}^{j}\big(\Box^c \sigma\big)\\
&-\frac{1}{2}gL_c{}^{i}{}^{j}\widehat G^2\\
&-g^{3}L_c{}^{i}{}^{j}L_c{}^{k}{}^{l}L_c{}_{k}{}_{l}\\
&+6g\widehat H{}^{a}{}^{b}\widehat H{}_{a}{}_{b}L_c{}^{i}{}^{j}\\
&-3N_cg^{2}L_c{}^{i}{}^{j}\\
&-g\big(\Box^c L_c{}^{i}{}^{j}\big)
\end{aligned}
```

## L: 2 explicit fermions

```math
\begin{aligned}
L_{\log}^{ij}[2]={}&-\frac{5i}{6}\overline{\big(\mathcal D_{a}\psi{}^{i}\big)}\gamma{}^{a}{}^{b}\big(\mathcal D_{b}\psi{}^{j}\big)\\
&+\frac{2i}{3}\overline{\big(\mathcal D^{a}\psi{}^{i}\big)}\big(\mathcal D_{a}\psi{}^{j}\big)\\
&-\frac{11}{6}g\overline{\varphi_c{}^{j}}\gamma{}^{a}\big(\mathcal D_{a}\psi{}^{i}\big)\\
&-\frac{11}{6}g\overline{\varphi_c{}^{i}}\gamma{}^{a}\big(\mathcal D_{a}\psi{}^{j}\big)\\
&+\frac{17i}{6}g^{2}\overline{\varphi_c{}^{i}}\varphi_c{}^{j}
\end{aligned}
```

## phi: 1 explicit fermions

```math
\begin{aligned}
\varphi_{\log}^{i}[1]={}&+\frac{1}{6}\widehat R(V){}^{a}{}^{b}{}^{i}{}^{j}\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\gamma{}^{c}{}^{d}\big(\mathcal D^{e}\psi{}_{j}\big)\\
&-\frac{i}{3}\widehat R(V){}^{a}{}^{b}{}^{i}{}^{j}\gamma{}_{a}\big(\mathcal D_{b}\psi{}_{j}\big)\\
&+\frac{1}{3}g\widehat R(V){}^{a}{}^{b}{}^{i}{}^{j}\gamma{}_{a}{}_{b}\varphi_c{}_{j}\\
&+\frac{1}{144}\widehat G{}_{a}{}_{b}\widehat G{}_{c}{}_{d}\gamma{}^{c}{}^{d}\widehat R(Q){}^{a}{}^{b}{}^{i}\\
&+\frac{1}{36}\widehat H{}^{a}{}^{b}\widehat G{}_{c}{}_{d}\gamma{}_{a}{}_{b}\widehat R(Q){}^{c}{}^{d}{}^{i}\\
&-\frac{7}{72}\widehat H{}^{a}{}^{b}\widehat G{}_{c}{}_{d}\gamma{}^{c}{}^{d}\widehat R(Q){}_{a}{}_{b}{}^{i}\\
&-\frac{7}{18}\widehat H{}^{a}{}^{b}\widehat H{}^{c}{}^{d}\gamma{}_{c}{}_{d}\widehat R(Q){}_{a}{}_{b}{}^{i}\\
&-\frac{2i}{3}\widehat H{}^{a}{}^{b}\widehat G{}_{a}{}_{b}\gamma{}^{c}\big(\mathcal D_{c}\psi{}^{i}\big)\\
&-\frac{1}{4}g\widehat G^2\varphi_c{}^{i}\\
&-\frac{2}{3}g\widehat H{}^{a}{}^{b}\widehat G{}_{a}{}_{b}\varphi_c{}^{i}\\
&+\frac{5}{2}g\widehat H{}^{a}{}^{b}\widehat H{}_{a}{}_{b}\varphi_c{}^{i}\\
&-\frac{5i}{16}\widehat G{}_{b}{}_{c}\gamma{}_{a}\big(\mathcal D^{a}\widehat R(Q){}^{b}{}^{c}{}^{i}\big)\\
&-\frac{5i}{4}\widehat H{}^{a}{}^{b}\gamma{}_{c}\big(\mathcal D^{c}\widehat R(Q){}_{a}{}_{b}{}^{i}\big)\\
&+\widehat H{}^{a}{}^{b}\widehat G{}_{b}{}_{c}\widehat R(Q){}_{a}{}^{c}{}^{i}\\
&-\frac{1}{24}\widehat G{}_{a}{}_{c}\widehat G{}_{b}{}_{d}\gamma{}^{c}{}^{d}\widehat R(Q){}^{a}{}^{b}{}^{i}\\
&-\frac{1}{12}\widehat H{}^{a}{}^{b}\widehat G{}_{c}{}_{d}\gamma{}_{b}{}^{d}\widehat R(Q){}_{a}{}^{c}{}^{i}\\
&+\frac{1}{3}\widehat H{}^{a}{}^{b}\widehat H{}^{c}{}^{d}\gamma{}_{b}{}_{d}\widehat R(Q){}_{a}{}_{c}{}^{i}\\
&-\frac{3}{16}\widehat G{}^{c}{}^{d}\widehat G{}^{e}{}^{f}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\gamma{}^{a}{}^{b}\big(\mathcal D_{a}\psi{}^{i}\big)\\
&+\frac{1}{16}\widehat G{}^{a}{}^{b}\widehat G{}^{c}{}^{d}\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\big(\mathcal D^{e}\psi{}^{i}\big)\\
&+\frac{1}{2}\widehat H{}^{a}{}^{b}\widehat G{}^{e}{}^{f}\epsilon{}_{a}{}_{b}{}_{d}{}_{e}{}_{f}\gamma{}^{c}{}^{d}\big(\mathcal D_{c}\psi{}^{i}\big)\\
&+\frac{2}{3}\widehat H{}^{a}{}^{b}\widehat H{}^{c}{}^{d}\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{f}\gamma{}^{e}{}^{f}\big(\mathcal D_{e}\psi{}^{i}\big)\\
&-\frac{3i}{16}g\widehat G{}^{b}{}^{c}\widehat G{}^{d}{}^{e}\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\gamma{}^{a}\varphi_c{}^{i}\\
&+\frac{i}{2}g\widehat H{}^{a}{}^{b}\widehat G{}^{d}{}^{e}\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\gamma{}^{c}\varphi_c{}^{i}\\
&+\frac{i}{4}g\widehat H{}^{a}{}^{b}\widehat H{}^{c}{}^{d}\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\gamma{}^{e}\varphi_c{}^{i}
\end{aligned}
```

```math
\begin{aligned}
&-\frac{1}{32}\widehat G{}^{d}{}^{e}\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\big(\mathcal D^{a}\widehat R(Q){}^{b}{}^{c}{}^{i}\big)\\
&-\frac{1}{8}\widehat H{}^{a}{}^{b}\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\big(\mathcal D^{c}\widehat R(Q){}^{d}{}^{e}{}^{i}\big)\\
&-\frac{1}{32}\widehat G{}^{e}{}^{f}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\gamma{}^{c}{}^{d}\big(\mathcal D^{a}\widehat R(Q){}_{a}{}^{b}{}^{i}\big)\\
&-\frac{1}{8}\widehat H{}^{a}{}^{b}\epsilon{}_{a}{}_{b}{}_{d}{}_{e}{}_{f}\gamma{}^{e}{}^{f}\big(\mathcal D^{c}\widehat R(Q){}_{c}{}^{d}{}^{i}\big)\\
&-\frac{1}{32}\widehat G{}_{a}{}^{f}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\gamma{}^{d}{}^{e}\big(\mathcal D^{a}\widehat R(Q){}^{b}{}^{c}{}^{i}\big)\\
&-\frac{1}{8}\widehat H{}^{a}{}^{b}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\gamma{}^{e}{}^{f}\big(\mathcal D_{a}\widehat R(Q){}^{c}{}^{d}{}^{i}\big)\\
&-\frac{1}{16}\widehat G{}_{b}{}^{f}\epsilon{}_{a}{}_{c}{}_{d}{}_{e}{}_{f}\gamma{}^{d}{}^{e}\big(\mathcal D^{a}\widehat R(Q){}^{b}{}^{c}{}^{i}\big)\\
&-\frac{1}{4}\widehat H{}^{a}{}^{b}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\gamma{}^{e}{}^{f}\big(\mathcal D^{c}\widehat R(Q){}_{a}{}^{d}{}^{i}\big)\\
&-\frac{i}{8}\widehat G{}_{b}{}_{c}\gamma{}^{c}\big(\mathcal D^{a}\widehat R(Q){}_{a}{}^{b}{}^{i}\big)\\
&+\frac{i}{2}\widehat H{}^{a}{}^{b}\gamma{}_{b}\big(\mathcal D^{c}\widehat R(Q){}_{a}{}_{c}{}^{i}\big)\\
&+\frac{4}{3}\widehat H{}^{a}{}^{b}\gamma{}_{a}{}^{c}\big(\mathcal D_{c}\mathcal D_{b}\psi{}^{i}\big)\\
&-\frac{2i}{3}\widehat H{}^{a}{}^{b}\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\gamma{}^{c}\big(\mathcal D^{d}\mathcal D^{e}\psi{}^{i}\big)\\
&-\frac{8i}{3}\widehat H{}^{a}{}^{b}\widehat H{}_{a}{}^{c}\gamma{}_{b}\big(\mathcal D_{c}\psi{}^{i}\big)\\
&-g\widehat H{}^{a}{}^{b}L_c{}^{i}{}^{j}\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\gamma{}^{c}{}^{d}\big(\mathcal D^{e}\psi{}_{j}\big)\\
&+\frac{1}{2}g\widehat H{}^{a}{}^{b}\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\gamma{}^{d}{}^{e}\big(\mathcal D^{c}\varphi_c{}^{i}\big)\\
&+\frac{1}{24}\widehat H{}^{a}{}^{b}\widehat G{}^{e}{}^{f}\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{f}\gamma{}^{c}{}^{d}\big(\mathcal D_{e}\psi{}^{i}\big)\\
&+\frac{2i}{3}\widehat H{}^{a}{}^{b}\widehat G{}_{b}{}^{c}\gamma{}_{a}\big(\mathcal D_{c}\psi{}^{i}\big)\\
&+\frac{i}{6}gL_c{}^{i}{}^{j}\widehat G{}_{a}{}^{b}\gamma{}^{a}\big(\mathcal D_{b}\psi{}_{j}\big)\\
&+\frac{8i}{3}g\widehat H{}^{a}{}^{b}L_c{}^{i}{}^{j}\gamma{}_{a}\big(\mathcal D_{b}\psi{}_{j}\big)\\
&-\frac{2i}{3}g\widehat G{}_{a}{}_{b}\gamma{}^{b}\big(\mathcal D^{a}\varphi_c{}^{i}\big)\\
&+\frac{4i}{3}g\widehat H{}^{a}{}^{b}\gamma{}_{b}\big(\mathcal D_{a}\varphi_c{}^{i}\big)\\
&+\frac{5i}{6}\big(\Box^c \sigma\big)\gamma{}^{a}\big(\mathcal D_{a}\psi{}^{i}\big)\\
&+\frac{5}{6}g\big(\Box^c \sigma\big)\varphi_c{}^{i}\\
&+\frac{11i}{24}g^{2}L_c{}^{j}{}^{k}L_c{}_{j}{}_{k}\gamma{}^{a}\big(\mathcal D_{a}\psi{}^{i}\big)
\end{aligned}
```

```math
\begin{aligned}
&-\frac{7}{24}g^{3}L_c{}^{j}{}^{k}L_c{}_{j}{}_{k}\varphi_c{}^{i}\\
&+\frac{11i}{6}N_cg\gamma{}^{a}\big(\mathcal D_{a}\psi{}^{i}\big)\\
&-\frac{1}{6}N_cg^{2}\varphi_c{}^{i}\\
&+\frac{13}{12}\big(\mathcal D^{c}\widehat G{}_{a}{}_{b}\big)\gamma{}^{a}{}^{b}\big(\mathcal D_{c}\psi{}^{i}\big)\\
&+\frac{5}{3}\big(\mathcal D_{a}\widehat G{}_{b}{}^{c}\big)\gamma{}^{a}{}^{b}\big(\mathcal D_{c}\psi{}^{i}\big)\\
&+\frac{7i}{12}\big(\mathcal D^{b}\widehat G{}^{c}{}^{d}\big)\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\gamma{}^{a}\big(\mathcal D^{e}\psi{}^{i}\big)\\
&+\frac{1}{3}\big(\mathcal D^{a}\widehat H{}^{b}{}^{c}\big)\gamma{}_{b}{}_{c}\big(\mathcal D_{a}\psi{}^{i}\big)\\
&-\frac{4}{3}\big(\mathcal D^{a}\widehat H{}^{b}{}^{c}\big)\gamma{}_{a}{}_{b}\big(\mathcal D_{c}\psi{}^{i}\big)\\
&+\frac{i}{6}\big(\mathcal D^{a}\widehat H{}^{b}{}^{c}\big)\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\gamma{}^{d}\big(\mathcal D^{e}\psi{}^{i}\big)\\
&-\frac{13}{24}g\big(\mathcal D^{c}\widehat G{}^{d}{}^{e}\big)\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\gamma{}^{a}{}^{b}\varphi_c{}^{i}\\
&+\frac{7}{12}g\big(\mathcal D^{a}\widehat H{}^{b}{}^{c}\big)\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\gamma{}^{d}{}^{e}\varphi_c{}^{i}\\
&-\frac{1}{3}\big(\mathcal D^{c}\widehat G{}_{a}{}_{c}\big)\gamma{}^{a}{}^{b}\big(\mathcal D_{b}\psi{}^{i}\big)\\
&-\frac{1}{6}\big(\mathcal D^{a}\widehat G{}_{a}{}^{b}\big)\big(\mathcal D_{b}\psi{}^{i}\big)\\
&-\frac{8}{3}\big(\mathcal D^{a}\widehat H{}_{a}{}^{b}\big)\gamma{}_{b}{}^{c}\big(\mathcal D_{c}\psi{}^{i}\big)\\
&-\frac{5}{3}\big(\mathcal D^{a}\widehat H{}_{a}{}^{b}\big)\big(\mathcal D_{b}\psi{}^{i}\big)\\
&+\frac{5i}{6}g\big(\mathcal D^{b}\widehat G{}_{a}{}_{b}\big)\gamma{}^{a}\varphi_c{}^{i}\\
&+\frac{11i}{3}g\big(\mathcal D^{a}\widehat H{}_{a}{}^{b}\big)\gamma{}_{b}\varphi_c{}^{i}\\
&-2gL_c{}^{i}{}^{j}\gamma{}^{a}{}^{b}\big(\mathcal D_{a}\mathcal D_{b}\psi{}_{j}\big)\\
&-gL_c{}^{i}{}^{j}\big(\Box^c \psi{}_{j}\big)\\
&-\frac{5i}{4}g^{2}L_c{}^{i}{}^{j}L_c{}_{j}{}^{k}\gamma{}^{a}\big(\mathcal D_{a}\psi{}_{k}\big)\\
&+2ig^{2}L_c{}^{i}{}^{j}\gamma{}_{a}\big(\mathcal D^{a}\varphi_c{}_{j}\big)\\
&+\frac{i}{4}\widehat H{}^{a}{}^{b}\widehat G{}^{e}{}^{f}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\gamma{}^{d}\widehat R(Q){}_{a}{}^{c}{}^{i}\\
&-\frac{i}{4}\widehat H{}^{a}{}^{b}\widehat G{}_{a}{}^{f}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\gamma{}^{e}\widehat R(Q){}^{c}{}^{d}{}^{i}\\
&+\frac{i}{8}\widehat H{}^{a}{}^{b}\widehat G{}_{c}{}^{f}\epsilon{}_{a}{}_{b}{}_{d}{}_{e}{}_{f}\gamma{}^{e}\widehat R(Q){}^{c}{}^{d}{}^{i}
\end{aligned}
```

```math
\begin{aligned}
&-\frac{5i}{2}\big(\mathcal D_{b}\mathcal D_{a}\sigma\big)\gamma{}^{a}\big(\mathcal D^{b}\psi{}^{i}\big)\\
&+\frac{1}{2}g\big(\mathcal D^{a}L_c{}^{i}{}^{j}\big)\big(\mathcal D_{a}\psi{}_{j}\big)\\
&-g\big(\Box^c \varphi_c{}^{i}\big)\\
&-\frac{i}{6}\widehat G{}^{b}{}^{c}\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\gamma{}^{a}\big(\mathcal D^{d}\mathcal D^{e}\psi{}^{i}\big)\\
&+\frac{1}{3}\widehat G{}_{a}{}^{c}\gamma{}^{a}{}^{b}\big(\mathcal D_{b}\mathcal D_{c}\psi{}^{i}\big)\\
&-g\big(\mathcal D^{a}L_c{}^{i}{}^{j}\big)\gamma{}_{a}{}^{b}\big(\mathcal D_{b}\psi{}_{j}\big)\\
&+ig^{2}\big(\mathcal D^{a}L_c{}^{i}{}^{j}\big)\gamma{}_{a}\varphi_c{}_{j}\\
&+\frac{i}{2}\widehat G{}_{a}{}^{b}\widehat G{}_{b}{}^{c}\gamma{}^{a}\big(\mathcal D_{c}\psi{}^{i}\big)\\
&+i\widehat H{}^{a}{}^{b}\widehat G{}_{a}{}_{c}\gamma{}^{c}\big(\mathcal D_{b}\psi{}^{i}\big)\\
&+\frac{23i}{576}gL_c{}^{i}{}^{j}\widehat G{}^{d}{}^{e}\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\gamma{}^{c}\widehat R(Q){}^{a}{}^{b}{}_{j}\\
&-\frac{11i}{288}g\widehat H{}^{a}{}^{b}L_c{}^{i}{}^{j}\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\gamma{}^{e}\widehat R(Q){}^{c}{}^{d}{}_{j}\\
&-\frac{1}{288}gL_c{}^{i}{}^{j}\widehat G{}_{a}{}_{b}\widehat R(Q){}^{a}{}^{b}{}_{j}\\
&-\frac{59}{144}g\widehat H{}^{a}{}^{b}L_c{}^{i}{}^{j}\widehat R(Q){}_{a}{}_{b}{}_{j}\\
&+\frac{1}{2}\big(\mathcal D^{d}\mathcal D^{e}\sigma\big)\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\gamma{}^{a}{}^{b}\big(\mathcal D^{c}\psi{}^{i}\big)\\
&+i\big(\mathcal D_{a}\mathcal D_{b}\sigma\big)\gamma{}^{a}\big(\mathcal D^{b}\psi{}^{i}\big)\\
&+g\big(\mathcal D_{a}\mathcal D_{b}\sigma\big)\gamma{}^{a}{}^{b}\varphi_c{}^{i}\\
&+\frac{1}{12}\widehat H{}^{a}{}^{b}\widehat G{}_{a}{}^{e}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\gamma{}^{c}{}^{d}\big(\mathcal D^{f}\psi{}^{i}\big)\\
&-\frac{1}{12}\widehat H{}^{a}{}^{b}\widehat G{}^{e}{}^{f}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\gamma{}^{c}{}^{d}\big(\mathcal D_{a}\psi{}^{i}\big)\\
&+\frac{1}{4}\widehat H{}^{a}{}^{b}\widehat G{}_{c}{}^{e}\epsilon{}_{a}{}_{b}{}_{d}{}_{e}{}_{f}\gamma{}^{c}{}^{d}\big(\mathcal D^{f}\psi{}^{i}\big)\\
&+\frac{1}{8}gL_c{}^{i}{}^{j}\widehat G{}^{c}{}^{d}\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\gamma{}^{a}{}^{b}\big(\mathcal D^{e}\psi{}_{j}\big)\\
&+\frac{1}{4}g^{2}L_c{}^{i}{}^{j}\widehat G{}_{a}{}_{b}\gamma{}^{a}{}^{b}\varphi_c{}_{j}\\
&-\frac{1}{6}\widehat H{}^{a}{}^{b}\widehat G{}^{d}{}^{e}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\gamma{}_{a}{}^{c}\big(\mathcal D^{f}\psi{}^{i}\big)
\end{aligned}
```

## N: 0 explicit fermions

```math
\begin{aligned}
N_{\log}[0]={}&+\frac{1}{6}\widehat R(V){}^{a}{}^{b}{}^{i}{}^{j}\widehat R(V){}_{a}{}_{b}{}_{i}{}_{j}\\
&+\frac{17}{144}\widehat C{}^{a}{}^{b}{}^{c}{}^{d}\widehat G{}_{a}{}_{b}\widehat G{}_{c}{}_{d}\\
&+\frac{23}{72}\widehat H{}^{a}{}^{b}\widehat C{}_{a}{}_{b}{}^{c}{}^{d}\widehat G{}_{c}{}_{d}\\
&-\frac{11}{18}\widehat H{}^{a}{}^{b}\widehat H{}^{c}{}^{d}\widehat C{}_{a}{}_{b}{}_{c}{}_{d}\\
&+\frac{11}{72}\widehat C{}^{a}{}^{b}{}^{c}{}^{d}\widehat G{}_{a}{}_{c}\widehat G{}_{b}{}_{d}\\
&+\frac{17}{36}\widehat H{}^{a}{}^{b}\widehat C{}_{a}{}^{c}{}_{b}{}^{d}\widehat G{}_{c}{}_{d}\\
&-\frac{5}{9}\widehat H{}^{a}{}^{b}\widehat H{}^{c}{}^{d}\widehat C{}_{a}{}_{c}{}_{b}{}_{d}\\
&+\frac{1}{16}(\widehat G^2)^{2}\\
&-\widehat H{}^{a}{}^{b}\widehat G{}_{a}{}_{b}\widehat G^2\\
&+\widehat H{}^{a}{}^{b}\widehat H{}_{a}{}_{b}\widehat G^2\\
&+\frac{4}{3}\widehat H{}^{a}{}^{b}\widehat H{}^{c}{}^{d}\widehat G{}_{a}{}_{b}\widehat G{}_{c}{}_{d}\\
&-2\widehat H{}^{a}{}^{b}\widehat H{}_{a}{}_{b}\widehat H{}^{c}{}^{d}\widehat H{}_{c}{}_{d}\\
&+\frac{1}{12}\widehat G{}^{a}{}^{b}\widehat G{}^{c}{}^{d}\big(\mathcal D^{e}\widehat G{}_{e}{}^{f}\big)\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{f}\\
&+\frac{1}{3}\big(\mathcal D^{a}\widehat H{}_{a}{}^{b}\big)\widehat G{}^{c}{}^{d}\widehat G{}^{e}{}^{f}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\\
&-\frac{863}{1152}\widehat H{}^{a}{}^{b}\widehat G{}^{c}{}^{d}\big(\mathcal D^{e}\widehat G{}_{e}{}^{f}\big)\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{f}\\
&-\frac{1129}{576}\widehat H{}^{a}{}^{b}\big(\mathcal D^{c}\widehat H{}_{c}{}^{d}\big)\widehat G{}^{e}{}^{f}\epsilon{}_{a}{}_{b}{}_{d}{}_{e}{}_{f}\\
&+\frac{1}{3}\widehat H{}^{a}{}^{b}\widehat H{}^{c}{}^{d}\big(\mathcal D^{e}\widehat G{}_{e}{}^{f}\big)\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{f}\\
&+\frac{4}{3}\widehat H{}^{a}{}^{b}\widehat H{}^{c}{}^{d}\big(\mathcal D^{e}\widehat H{}_{e}{}^{f}\big)\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{f}\\
&-\frac{4}{3}\widehat H{}^{a}{}^{b}\widehat G{}_{a}{}_{b}\big(\Box^c \sigma\big)\\
&+\frac{1}{8}g^{2}L_c{}^{i}{}^{j}L_c{}_{i}{}_{j}\widehat G^2\\
&-\frac{1}{3}g^{2}\widehat H{}^{a}{}^{b}L_c{}^{i}{}^{j}L_c{}_{i}{}_{j}\widehat G{}_{a}{}_{b}\\
&+2g^{2}\widehat H{}^{a}{}^{b}\widehat H{}_{a}{}_{b}L_c{}^{i}{}^{j}L_c{}_{i}{}_{j}\\
&+\frac{1}{2}N_cg\widehat G^2\\
&-\frac{4}{3}N_cg\widehat H{}^{a}{}^{b}\widehat G{}_{a}{}_{b}
\end{aligned}
```

```math
\begin{aligned}
&+2N_cg\widehat H{}^{a}{}^{b}\widehat H{}_{a}{}_{b}\\
&-\frac{3}{32}\big(\mathcal D^{a}\widehat C{}_{a}{}^{b}{}^{c}{}^{d}\big)\widehat G{}^{e}{}^{f}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\\
&-\frac{3}{8}\widehat H{}^{a}{}^{b}\big(\mathcal D^{c}\widehat C{}_{c}{}^{d}{}^{e}{}^{f}\big)\epsilon{}_{a}{}_{b}{}_{d}{}_{e}{}_{f}\\
&-\frac{1}{16}\big(\mathcal D^{a}\widehat C{}^{b}{}^{c}{}^{d}{}^{e}\big)\widehat G{}_{b}{}^{f}\epsilon{}_{a}{}_{c}{}_{d}{}_{e}{}_{f}\\
&-\frac{1}{4}\widehat H{}^{a}{}^{b}\big(\mathcal D^{c}\widehat C{}_{a}{}^{d}{}^{e}{}^{f}\big)\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\\
&-\frac{1}{16}\big(\mathcal D^{a}\widehat C{}^{b}{}^{c}{}^{d}{}^{e}\big)\widehat G{}_{a}{}^{f}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\\
&-\frac{1}{4}\widehat H{}^{a}{}^{b}\big(\mathcal D_{a}\widehat C{}^{c}{}^{d}{}^{e}{}^{f}\big)\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\\
&-\frac{4}{3}\widehat G{}^{a}{}^{b}\widehat G{}_{a}{}^{c}\big(\mathcal D_{b}\mathcal D_{c}\sigma\big)\\
&+\frac{2}{9}\widehat G{}^{a}{}^{b}\big(\mathcal D_{a}\mathcal D^{c}\widehat G{}_{b}{}_{c}\big)\\
&-\frac{28}{9}\widehat H{}^{a}{}^{b}\widehat G{}_{a}{}^{c}\big(\mathcal D_{c}\mathcal D_{b}\sigma\big)\\
&+\frac{28}{9}\big(\mathcal D^{a}\mathcal D^{b}\widehat H{}_{b}{}^{c}\big)\widehat G{}_{a}{}_{c}\\
&+\frac{28}{9}\widehat H{}^{a}{}^{b}\widehat G{}_{a}{}^{c}\big(\mathcal D_{b}\mathcal D_{c}\sigma\big)\\
&+\frac{8}{9}\widehat H{}^{a}{}^{b}\big(\mathcal D_{a}\mathcal D^{c}\widehat G{}_{b}{}_{c}\big)\\
&-\frac{8}{3}\widehat H{}^{a}{}^{b}\widehat H{}_{a}{}^{c}\big(\mathcal D_{b}\mathcal D_{c}\sigma\big)\\
&+\frac{32}{9}\widehat H{}^{a}{}^{b}\big(\mathcal D_{a}\mathcal D^{c}\widehat H{}_{b}{}_{c}\big)\\
&+\frac{1}{3}\widehat G{}^{a}{}^{b}\big(\Box^c \widehat G{}_{a}{}_{b}\big)\\
&+\frac{4}{3}\widehat H{}^{a}{}^{b}\big(\Box^c \widehat G{}_{a}{}_{b}\big)\\
&+\frac{1}{9}\widehat G{}^{a}{}^{b}\big(\mathcal D^{c}\mathcal D_{a}\widehat G{}_{b}{}_{c}\big)\\
&+\frac{2}{9}\big(\mathcal D^{a}\mathcal D^{b}\widehat H{}_{a}{}^{c}\big)\widehat G{}_{b}{}_{c}\\
&+\frac{4}{9}\widehat H{}^{a}{}^{b}\big(\mathcal D^{c}\mathcal D_{a}\widehat G{}_{b}{}_{c}\big)\\
&-\frac{8}{9}\widehat H{}^{a}{}^{b}\big(\mathcal D^{c}\mathcal D_{a}\widehat H{}_{b}{}_{c}\big)\\
&+\frac{5}{6}\big(\Box^c \sigma\big)\big(\Box^c \sigma\big)\\
&+\frac{5}{3}g^{2}L_c{}^{i}{}^{j}L_c{}_{i}{}_{j}\big(\Box^c \sigma\big)\\
&+\frac{8}{3}N_cg\big(\Box^c \sigma\big)
\end{aligned}
```

```math
\begin{aligned}
&-\frac{17}{48}g^{4}L_c{}^{i}{}^{j}L_c{}_{i}{}_{j}L_c{}^{k}{}^{l}L_c{}_{k}{}_{l}\\
&-\frac{5}{6}N_cg^{3}L_c{}^{i}{}^{j}L_c{}_{i}{}_{j}\\
&-\frac{1}{6}N_cN_cg^{2}\\
&+\frac{5}{6}\big(\mathcal D^{a}\widehat G{}^{b}{}^{c}\big)\big(\mathcal D_{b}\widehat G{}_{a}{}_{c}\big)\\
&-\frac{7}{3}\big(\mathcal D^{a}\widehat H{}^{b}{}^{c}\big)\big(\mathcal D_{b}\widehat G{}_{a}{}_{c}\big)\\
&+\frac{4}{3}\big(\mathcal D^{a}\widehat H{}^{b}{}^{c}\big)\big(\mathcal D_{b}\widehat H{}_{a}{}_{c}\big)\\
&-\frac{1}{3}\big(\mathcal D^{a}\widehat G{}^{b}{}^{c}\big)\big(\mathcal D_{a}\widehat G{}_{b}{}_{c}\big)\\
&+\frac{11}{6}\big(\mathcal D^{a}\widehat H{}^{b}{}^{c}\big)\big(\mathcal D_{a}\widehat G{}_{b}{}_{c}\big)\\
&+\frac{2}{3}\big(\mathcal D^{a}\widehat H{}^{b}{}^{c}\big)\big(\mathcal D_{a}\widehat H{}_{b}{}_{c}\big)\\
&-2\big(\mathcal D^{a}\widehat H{}_{a}{}^{b}\big)\big(\mathcal D^{c}\widehat G{}_{b}{}_{c}\big)\\
&+4\big(\mathcal D^{a}\widehat H{}_{a}{}^{b}\big)\big(\mathcal D^{c}\widehat H{}_{b}{}_{c}\big)\\
&-\frac{1}{2}gL_c{}^{i}{}^{j}\widehat R(V){}^{a}{}^{b}{}_{i}{}_{j}\widehat G{}_{a}{}_{b}\\
&-\frac{1163}{1152}\widehat H{}^{a}{}^{b}\widehat G{}^{c}{}^{d}\big(\mathcal D_{c}\widehat G{}^{e}{}^{f}\big)\epsilon{}_{a}{}_{b}{}_{d}{}_{e}{}_{f}\\
&+\frac{563}{576}\widehat H{}^{a}{}^{b}\big(\mathcal D^{c}\widehat H{}^{d}{}^{e}\big)\widehat G{}_{c}{}^{f}\epsilon{}_{a}{}_{b}{}_{d}{}_{e}{}_{f}\\
&+\frac{269}{576}\widehat H{}^{a}{}^{b}\widehat G{}_{a}{}^{c}\big(\mathcal D^{d}\widehat G{}^{e}{}^{f}\big)\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\\
&-\frac{139}{288}\widehat H{}^{a}{}^{b}\big(\mathcal D^{c}\widehat H{}^{d}{}^{e}\big)\widehat G{}_{a}{}^{f}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\\
&+\frac{3}{16}\widehat H{}^{a}{}^{b}\widehat G{}^{c}{}^{d}\big(\mathcal D^{e}\widehat G{}_{c}{}^{f}\big)\epsilon{}_{a}{}_{b}{}_{d}{}_{e}{}_{f}\\
&+\frac{19}{24}\widehat H{}^{a}{}^{b}\big(\mathcal D^{c}\widehat H{}^{d}{}^{e}\big)\widehat G{}_{d}{}^{f}\epsilon{}_{a}{}_{b}{}_{c}{}_{e}{}_{f}\\
&-\frac{353}{576}\widehat H{}^{a}{}^{b}\widehat G{}^{c}{}^{d}\big(\mathcal D^{e}\widehat G{}_{a}{}^{f}\big)\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\\
&+\frac{89}{288}\widehat H{}^{a}{}^{b}\big(\mathcal D^{c}\widehat H{}_{a}{}^{d}\big)\widehat G{}^{e}{}^{f}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\\
&-\frac{7}{64}\widehat H{}^{a}{}^{b}\widehat G{}^{c}{}^{d}\big(\mathcal D_{a}\widehat G{}^{e}{}^{f}\big)\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\\
&-\frac{25}{32}\widehat H{}^{a}{}^{b}\big(\mathcal D_{a}\widehat H{}^{c}{}^{d}\big)\widehat G{}^{e}{}^{f}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\\
&-g^{2}L_c{}^{i}{}^{j}\big(\Box^c L_c{}_{i}{}_{j}\big)\\
&-\frac{3}{4}\big(\mathcal D^{a}\widehat G{}^{b}{}^{c}\big)\big(\mathcal D^{d}\mathcal D^{e}\sigma\big)\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}
\end{aligned}
```

```math
\begin{aligned}
&+\frac{3}{2}\big(\mathcal D^{a}\widehat H{}^{b}{}^{c}\big)\big(\mathcal D^{d}\mathcal D^{e}\sigma\big)\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\\
&-\frac{3}{2}\big(\mathcal D^{a}\mathcal D^{b}\sigma\big)\big(\mathcal D_{a}\mathcal D_{b}\sigma\big)\\
&-\frac{3}{4}g^{2}\big(\mathcal D^{a}L_c{}^{i}{}^{j}\big)\big(\mathcal D_{a}L_c{}_{i}{}_{j}\big)\\
&-g\big(\Box^c N_c\big)\\
&-\frac{3}{8}\widehat G{}^{a}{}^{b}\widehat G{}_{a}{}^{c}\widehat G{}_{b}{}^{d}\widehat G{}_{c}{}_{d}\\
&+2\widehat H{}^{a}{}^{b}\widehat G{}_{a}{}^{c}\widehat G{}_{b}{}^{d}\widehat G{}_{c}{}_{d}\\
&-4\widehat H{}^{a}{}^{b}\widehat H{}_{a}{}^{c}\widehat G{}_{b}{}^{d}\widehat G{}_{c}{}_{d}\\
&+\frac{1}{8}g^{4}L_c{}^{i}{}^{j}L_c{}_{i}{}^{k}L_c{}_{j}{}^{l}L_c{}_{k}{}_{l}
\end{aligned}
```

## N: 2 explicit fermions

```math
\begin{aligned}
N_{\log}[2]={}&+\frac{685i}{6144}\widehat G{}^{e}{}^{f}\epsilon{}_{a}{}_{b}{}_{d}{}_{e}{}_{f}\overline{\widehat R(Q){}^{a}{}^{b}{}^{i}}\gamma{}^{c}{}^{d}\big(\mathcal D_{c}\psi{}_{i}\big)\\
&-\frac{2125i}{18432}\widehat G{}^{c}{}^{d}\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\widehat R(Q){}^{a}{}^{b}{}^{i}}\big(\mathcal D^{e}\psi{}_{i}\big)\\
&+\frac{379i}{3072}\widehat H{}^{a}{}^{b}\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{f}\overline{\widehat R(Q){}^{c}{}^{d}{}^{i}}\gamma{}^{e}{}^{f}\big(\mathcal D_{e}\psi{}_{i}\big)\\
&-\frac{1211i}{9216}\widehat H{}^{a}{}^{b}\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\widehat R(Q){}^{c}{}^{d}{}^{i}}\big(\mathcal D^{e}\psi{}_{i}\big)\\
&-\frac{2651}{18432}g\widehat G{}^{d}{}^{e}\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\widehat R(Q){}^{a}{}^{b}{}^{i}}\gamma{}^{c}\varphi_c{}_{i}\\
&-\frac{541}{9216}g\widehat H{}^{a}{}^{b}\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\widehat R(Q){}^{c}{}^{d}{}^{i}}\gamma{}^{e}\varphi_c{}_{i}\\
&-\frac{607i}{18432}\widehat G{}_{a}{}^{e}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\widehat R(Q){}^{a}{}^{b}{}^{i}}\gamma{}^{c}{}^{d}\big(\mathcal D^{f}\psi{}_{i}\big)\\
&-\frac{289}{576}\widehat G{}_{a}{}_{c}\overline{\widehat R(Q){}^{a}{}^{b}{}^{i}}\gamma{}^{c}\big(\mathcal D_{b}\psi{}_{i}\big)\\
&+\frac{65i}{9216}\widehat H{}^{a}{}^{b}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\widehat R(Q){}_{a}{}^{c}{}^{i}}\gamma{}^{d}{}^{e}\big(\mathcal D^{f}\psi{}_{i}\big)\\
&+\frac{11}{144}\widehat H{}^{a}{}^{b}\overline{\widehat R(Q){}_{a}{}^{c}{}^{i}}\gamma{}_{b}\big(\mathcal D_{c}\psi{}_{i}\big)\\
&+\frac{859i}{9216}g\widehat G{}_{a}{}_{b}\overline{\widehat R(Q){}^{a}{}^{b}{}^{i}}\varphi_c{}_{i}\\
&+\frac{6173i}{4608}g\widehat H{}^{a}{}^{b}\overline{\widehat R(Q){}_{a}{}_{b}{}^{i}}\varphi_c{}_{i}\\
&-\frac{209}{9216}\widehat G{}_{a}{}_{b}\overline{\widehat R(Q){}^{a}{}^{b}{}^{i}}\gamma{}^{c}\big(\mathcal D_{c}\psi{}_{i}\big)\\
&-\frac{8167}{4608}\widehat H{}^{a}{}^{b}\overline{\widehat R(Q){}_{a}{}_{b}{}^{i}}\gamma{}^{c}\big(\mathcal D_{c}\psi{}_{i}\big)\\
&-\frac{1}{8}\widehat G{}^{b}{}^{c}\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\big(\mathcal D^{d}\psi{}^{i}\big)}\gamma{}^{a}\big(\mathcal D^{e}\psi{}_{i}\big)\\
&-\frac{i}{4}\widehat G{}_{a}{}_{b}\overline{\big(\mathcal D^{c}\psi{}^{i}\big)}\gamma{}^{a}{}^{b}\big(\mathcal D_{c}\psi{}_{i}\big)\\
&-\frac{i}{12}\widehat G{}_{a}{}^{c}\overline{\big(\mathcal D_{b}\psi{}^{i}\big)}\gamma{}^{a}{}^{b}\big(\mathcal D_{c}\psi{}_{i}\big)\\
&-\frac{3i}{2}\widehat G{}^{a}{}^{b}\overline{\big(\mathcal D_{a}\psi{}^{i}\big)}\big(\mathcal D_{b}\psi{}_{i}\big)\\
&+\frac{1}{12}\widehat H{}^{a}{}^{b}\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\big(\mathcal D^{d}\psi{}^{i}\big)}\gamma{}^{c}\big(\mathcal D^{e}\psi{}_{i}\big)\\
&+\frac{i}{6}\widehat H{}^{a}{}^{b}\overline{\big(\mathcal D_{b}\psi{}^{i}\big)}\gamma{}_{a}{}^{c}\big(\mathcal D_{c}\psi{}_{i}\big)\\
&-\frac{5i}{6}\widehat H{}^{a}{}^{b}\overline{\big(\mathcal D^{c}\psi{}^{i}\big)}\gamma{}_{a}{}_{b}\big(\mathcal D_{c}\psi{}_{i}\big)\\
&+\frac{2i}{3}\widehat H{}^{a}{}^{b}\overline{\big(\mathcal D_{a}\psi{}^{i}\big)}\big(\mathcal D_{b}\psi{}_{i}\big)\\
&-\frac{i}{4}g\widehat G{}^{c}{}^{d}\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\varphi_c{}^{i}}\gamma{}^{a}{}^{b}\big(\mathcal D^{e}\psi{}_{i}\big)\\
&-\frac{1}{2}g\widehat G{}_{a}{}^{b}\overline{\varphi_c{}^{i}}\gamma{}^{a}\big(\mathcal D_{b}\psi{}_{i}\big)
\end{aligned}
```

```math
\begin{aligned}
&+\frac{19i}{24}g\widehat H{}^{a}{}^{b}\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\varphi_c{}^{i}}\gamma{}^{c}{}^{d}\big(\mathcal D^{e}\psi{}_{i}\big)\\
&+\frac{1}{6}g\widehat H{}^{a}{}^{b}\overline{\varphi_c{}^{i}}\gamma{}_{a}\big(\mathcal D_{b}\psi{}_{i}\big)\\
&-\frac{3i}{8}g^{2}\widehat G{}_{a}{}_{b}\overline{\varphi_c{}^{i}}\gamma{}^{a}{}^{b}\varphi_c{}_{i}\\
&+\frac{3i}{4}g^{2}\widehat H{}^{a}{}^{b}\overline{\varphi_c{}^{i}}\gamma{}_{a}{}_{b}\varphi_c{}_{i}\\
&-\frac{81i}{256}\overline{\big(\mathcal D^{a}\widehat R(Q){}_{a}{}^{b}{}^{i}\big)}\big(\mathcal D_{b}\psi{}_{i}\big)\\
&+\frac{111}{512}\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\big(\mathcal D^{a}\widehat R(Q){}^{b}{}^{c}{}^{i}\big)}\gamma{}^{d}\big(\mathcal D^{e}\psi{}_{i}\big)\\
&-\frac{153i}{1024}g\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\big(\mathcal D^{a}\widehat R(Q){}^{b}{}^{c}{}^{i}\big)}\gamma{}^{d}{}^{e}\varphi_c{}_{i}\\
&-\frac{i}{12}\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\big(\mathcal D^{c}\psi{}^{i}\big)}\gamma{}^{a}{}^{b}\big(\mathcal D^{d}\mathcal D^{e}\psi{}_{i}\big)\\
&+\frac{5}{6}\overline{\big(\mathcal D_{a}\psi{}^{i}\big)}\gamma{}^{a}\big(\Box^c \psi{}_{i}\big)\\
&-\frac{1}{6}\overline{\big(\mathcal D^{b}\psi{}^{i}\big)}\gamma{}^{a}\big(\mathcal D_{a}\mathcal D_{b}\psi{}_{i}\big)\\
&-\frac{4}{3}\overline{\big(\mathcal D^{b}\psi{}^{i}\big)}\gamma{}^{a}\big(\mathcal D_{b}\mathcal D_{a}\psi{}_{i}\big)\\
&+\frac{i}{3}gL_c{}^{i}{}^{j}\overline{\big(\mathcal D_{a}\psi{}_{i}\big)}\gamma{}^{a}{}^{b}\big(\mathcal D_{b}\psi{}_{j}\big)\\
&+\frac{10i}{3}gL_c{}^{i}{}^{j}\overline{\big(\mathcal D^{a}\psi{}_{i}\big)}\big(\mathcal D_{a}\psi{}_{j}\big)\\
&+\frac{5i}{6}g\overline{\big(\mathcal D^{a}\varphi_c{}^{i}\big)}\gamma{}_{a}{}^{b}\big(\mathcal D_{b}\psi{}_{i}\big)\\
&-\frac{13i}{6}g\overline{\big(\mathcal D^{a}\varphi_c{}^{i}\big)}\big(\mathcal D_{a}\psi{}_{i}\big)\\
&+\frac{5i}{6}g\overline{\varphi_c{}^{i}}\gamma{}^{a}{}^{b}\big(\mathcal D_{a}\mathcal D_{b}\psi{}_{i}\big)\\
&-\frac{5i}{6}g\overline{\varphi_c{}^{i}}\big(\Box^c \psi{}_{i}\big)\\
&+\frac{13}{12}g^{2}L_c{}^{i}{}^{j}\overline{\varphi_c{}_{i}}\gamma{}^{a}\big(\mathcal D_{a}\psi{}_{j}\big)\\
&+\frac{1}{6}g^{2}\overline{\varphi_c{}^{i}}\gamma{}_{a}\big(\mathcal D^{a}\varphi_c{}_{i}\big)\\
&-\frac{19i}{64}\widehat G{}_{b}{}_{c}\overline{\widehat R(Q){}^{a}{}^{b}{}^{i}}\widehat R(Q){}_{a}{}^{c}{}_{i}\\
&-\frac{19i}{16}\widehat H{}^{a}{}^{b}\overline{\widehat R(Q){}_{a}{}^{c}{}^{i}}\widehat R(Q){}_{b}{}_{c}{}_{i}\\
&+\frac{15}{512}\widehat G{}_{a}{}^{f}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\widehat R(Q){}^{a}{}^{b}{}^{i}}\gamma{}^{e}\widehat R(Q){}^{c}{}^{d}{}_{i}\\
&+\frac{15}{128}\widehat H{}^{a}{}^{b}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\widehat R(Q){}_{a}{}^{c}{}^{i}}\gamma{}^{f}\widehat R(Q){}^{d}{}^{e}{}_{i}\\
&+\frac{3}{256}\widehat G{}^{e}{}^{f}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\widehat R(Q){}^{a}{}^{b}{}^{i}}\gamma{}^{d}\widehat R(Q){}_{a}{}^{c}{}_{i}
\end{aligned}
```

```math
\begin{aligned}
&+\frac{3}{64}\widehat H{}^{a}{}^{b}\epsilon{}_{a}{}_{b}{}_{d}{}_{e}{}_{f}\overline{\widehat R(Q){}^{c}{}^{d}{}^{i}}\gamma{}^{f}\widehat R(Q){}_{c}{}^{e}{}_{i}\\
&-\frac{9i}{1024}\widehat G{}_{c}{}_{d}\overline{\widehat R(Q){}^{a}{}^{b}{}^{i}}\gamma{}^{c}{}^{d}\widehat R(Q){}_{a}{}_{b}{}_{i}\\
&-\frac{9i}{256}\widehat H{}^{a}{}^{b}\overline{\widehat R(Q){}^{c}{}^{d}{}^{i}}\gamma{}_{a}{}_{b}\widehat R(Q){}_{c}{}_{d}{}_{i}\\
&+\frac{355i}{2304}gL_c{}^{i}{}^{j}\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\widehat R(Q){}^{a}{}^{b}{}_{i}}\gamma{}^{c}{}^{d}\big(\mathcal D^{e}\psi{}_{j}\big)\\
&+\frac{131i}{1152}\widehat G{}^{e}{}^{f}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\widehat R(Q){}^{a}{}^{b}{}^{i}}\gamma{}^{c}{}^{d}\big(\mathcal D_{a}\psi{}_{i}\big)\\
&-\frac{95i}{576}\widehat H{}^{a}{}^{b}\epsilon{}_{a}{}_{b}{}_{d}{}_{e}{}_{f}\overline{\widehat R(Q){}^{c}{}^{d}{}^{i}}\gamma{}^{e}{}^{f}\big(\mathcal D_{c}\psi{}_{i}\big)\\
&+\frac{4999i}{36864}\widehat G{}^{e}{}^{f}\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{f}\overline{\widehat R(Q){}^{a}{}^{b}{}^{i}}\gamma{}^{c}{}^{d}\big(\mathcal D_{e}\psi{}_{i}\big)\\
&-\frac{3271i}{18432}\widehat H{}^{a}{}^{b}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\widehat R(Q){}^{c}{}^{d}{}^{i}}\gamma{}^{e}{}^{f}\big(\mathcal D_{a}\psi{}_{i}\big)\\
&+\frac{117i}{2048}\widehat G{}_{c}{}^{e}\epsilon{}_{a}{}_{b}{}_{d}{}_{e}{}_{f}\overline{\widehat R(Q){}^{a}{}^{b}{}^{i}}\gamma{}^{c}{}^{d}\big(\mathcal D^{f}\psi{}_{i}\big)\\
&+\frac{69i}{1024}\widehat H{}^{a}{}^{b}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\widehat R(Q){}^{c}{}^{d}{}^{i}}\gamma{}_{a}{}^{e}\big(\mathcal D^{f}\psi{}_{i}\big)\\
&-\frac{i}{64}g\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\widehat R(Q){}^{a}{}^{b}{}^{i}}\gamma{}^{d}{}^{e}\big(\mathcal D^{c}\varphi_c{}_{i}\big)\\
&-\frac{i}{1024}gL_c{}^{i}{}^{j}\overline{\widehat R(Q){}^{a}{}^{b}{}_{i}}\widehat R(Q){}_{a}{}_{b}{}_{j}\\
&+\frac{1}{2048}gL_c{}^{i}{}^{j}\epsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\widehat R(Q){}^{a}{}^{b}{}_{i}}\gamma{}^{e}\widehat R(Q){}^{c}{}^{d}{}_{j}
\end{aligned}
```

## E: 0 explicit fermions

```math
\begin{aligned}
E_{\log}^{a}[0]={}&-\frac{1}{12}\widehat R(V){}^{b}{}^{c}{}^{i}{}^{j}\widehat R(V){}^{d}{}^{e}{}_{i}{}_{j}\epsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{e}\\
&-\frac{1}{128}\widehat C{}^{b}{}^{c}{}^{d}{}^{e}\widehat G{}^{a}{}^{f}\widehat G{}_{b}{}^{g}\epsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g}\\
&+\frac{3}{8}\widehat H{}^{b}{}^{c}\widehat C{}_{b}{}^{d}{}^{e}{}^{f}\widehat G{}^{a}{}^{g}\epsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g}\\
&+\frac{21}{64}\widehat H{}^{a}{}^{b}\widehat C{}^{c}{}^{d}{}^{e}{}^{f}\widehat G{}_{c}{}^{g}\epsilon{}_{b}{}_{d}{}_{e}{}_{f}{}_{g}\\
&+\frac{5}{16}\widehat H{}^{a}{}^{b}\widehat H{}^{c}{}^{d}\widehat C{}_{c}{}^{e}{}^{f}{}^{g}\epsilon{}_{b}{}_{d}{}_{e}{}_{f}{}_{g}\\
&+\frac{25}{768}\widehat C{}^{b}{}^{c}{}^{d}{}^{e}\widehat G{}^{a}{}_{b}\widehat G{}^{f}{}^{g}\epsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g}\\
&+\frac{11}{96}\widehat H{}^{b}{}^{c}\widehat C{}^{d}{}^{e}{}^{f}{}^{g}\widehat G{}^{a}{}_{d}\epsilon{}_{b}{}_{c}{}_{e}{}_{f}{}_{g}\\
&-\frac{31}{384}\widehat H{}^{a}{}^{b}\widehat C{}_{b}{}^{c}{}^{d}{}^{e}\widehat G{}^{f}{}^{g}\epsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g}\\
&-\frac{37}{96}\widehat H{}^{a}{}^{b}\widehat H{}^{c}{}^{d}\widehat C{}_{b}{}^{e}{}^{f}{}^{g}\epsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g}\\
&+\frac{1}{192}\widehat C{}^{b}{}^{c}{}^{d}{}^{e}\widehat G{}^{a}{}^{f}\widehat G{}_{f}{}^{g}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{g}\\
&-\frac{5}{192}\widehat H{}^{b}{}^{c}\widehat C{}^{d}{}^{e}{}^{f}{}^{g}\widehat G{}^{a}{}_{b}\epsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g}\\
&+\frac{7}{192}\widehat H{}^{a}{}^{b}\widehat C{}^{c}{}^{d}{}^{e}{}^{f}\widehat G{}_{b}{}^{g}\epsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g}\\
&-\frac{1}{24}\widehat H{}^{a}{}^{b}\widehat H{}_{b}{}^{c}\widehat C{}^{d}{}^{e}{}^{f}{}^{g}\epsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g}\\
&-\frac{41}{576}\widehat C{}^{b}{}^{c}{}^{d}{}^{e}\widehat G{}_{b}{}^{f}\widehat G{}_{d}{}^{g}\epsilon{}^{a}{}_{c}{}_{e}{}_{f}{}_{g}\\
&-\frac{29}{288}\widehat H{}^{b}{}^{c}\widehat C{}_{b}{}^{d}{}^{e}{}^{f}\widehat G{}_{e}{}^{g}\epsilon{}^{a}{}_{c}{}_{d}{}_{f}{}_{g}\\
&+\frac{53}{72}\widehat H{}^{b}{}^{c}\widehat H{}^{d}{}^{e}\widehat C{}_{b}{}^{f}{}_{d}{}^{g}\epsilon{}^{a}{}_{c}{}_{e}{}_{f}{}_{g}\\
&-\frac{31}{1152}\widehat C{}^{b}{}^{c}{}^{d}{}^{e}\widehat G{}_{b}{}_{d}\widehat G{}^{f}{}^{g}\epsilon{}^{a}{}_{c}{}_{e}{}_{f}{}_{g}\\
&+\frac{59}{288}\widehat H{}^{b}{}^{c}\widehat C{}^{d}{}^{e}{}^{f}{}^{g}\widehat G{}_{d}{}_{f}\epsilon{}^{a}{}_{b}{}_{c}{}_{e}{}_{g}\\
&-\frac{161}{576}\widehat H{}^{b}{}^{c}\widehat C{}_{b}{}^{d}{}_{c}{}^{e}\widehat G{}^{f}{}^{g}\epsilon{}^{a}{}_{d}{}_{e}{}_{f}{}_{g}\\
&+\frac{19}{144}\widehat H{}^{b}{}^{c}\widehat H{}^{d}{}^{e}\widehat C{}_{b}{}^{f}{}_{c}{}^{g}\epsilon{}^{a}{}_{d}{}_{e}{}_{f}{}_{g}\\
&-\frac{1}{1152}\widehat C{}^{b}{}^{c}{}^{d}{}^{e}\widehat G{}_{b}{}_{c}\widehat G{}^{f}{}^{g}\epsilon{}^{a}{}_{d}{}_{e}{}_{f}{}_{g}\\
&+\frac{23}{1152}\widehat H{}^{b}{}^{c}\widehat C{}^{d}{}^{e}{}^{f}{}^{g}\widehat G{}_{d}{}_{e}\epsilon{}^{a}{}_{b}{}_{c}{}_{f}{}_{g}\\
&+\frac{23}{1152}\widehat H{}^{b}{}^{c}\widehat C{}_{b}{}_{c}{}^{d}{}^{e}\widehat G{}^{f}{}^{g}\epsilon{}^{a}{}_{d}{}_{e}{}_{f}{}_{g}\\
&+\frac{25}{144}\widehat H{}^{b}{}^{c}\widehat H{}^{d}{}^{e}\widehat C{}_{b}{}_{c}{}^{f}{}^{g}\epsilon{}^{a}{}_{d}{}_{e}{}_{f}{}_{g}
\end{aligned}
```

```math
\begin{aligned}
&-\frac{43}{576}\widehat C{}^{b}{}^{c}{}^{d}{}^{e}\widehat G{}_{b}{}^{f}\widehat G{}_{f}{}^{g}\epsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{g}\\
&+\frac{29}{144}\widehat H{}^{b}{}^{c}\widehat C{}^{d}{}^{e}{}^{f}{}^{g}\widehat G{}_{b}{}_{d}\epsilon{}^{a}{}_{c}{}_{e}{}_{f}{}_{g}\\
&-\frac{149}{288}\widehat H{}^{b}{}^{c}\widehat C{}_{b}{}^{d}{}^{e}{}^{f}\widehat G{}_{c}{}^{g}\epsilon{}^{a}{}_{d}{}_{e}{}_{f}{}_{g}\\
&-\frac{5}{72}\widehat H{}^{b}{}^{c}\widehat H{}_{b}{}^{d}\widehat C{}_{c}{}^{e}{}^{f}{}^{g}\epsilon{}^{a}{}_{d}{}_{e}{}_{f}{}_{g}\\
&+\frac{35}{2304}\widehat C{}^{b}{}^{c}{}^{d}{}^{e}\epsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{e}\widehat G^2\\
&+\frac{59}{1152}\widehat H{}^{b}{}^{c}\widehat C{}^{d}{}^{e}{}^{f}{}^{g}\widehat G{}_{b}{}_{c}\epsilon{}^{a}{}_{d}{}_{e}{}_{f}{}_{g}\\
&-\frac{11}{288}\widehat H{}^{b}{}^{c}\widehat H{}_{b}{}_{c}\widehat C{}^{d}{}^{e}{}^{f}{}^{g}\epsilon{}^{a}{}_{d}{}_{e}{}_{f}{}_{g}\\
&+\frac{5}{576}\widehat C{}^{b}{}^{c}{}^{d}{}^{e}\widehat G{}_{b}{}^{f}\widehat G{}_{c}{}^{g}\epsilon{}^{a}{}_{d}{}_{e}{}_{f}{}_{g}\\
&+\frac{29}{288}\widehat H{}^{b}{}^{c}\widehat C{}_{b}{}^{d}{}^{e}{}^{f}\widehat G{}_{d}{}^{g}\epsilon{}^{a}{}_{c}{}_{e}{}_{f}{}_{g}\\
&+\frac{19}{72}\widehat H{}^{b}{}^{c}\widehat H{}^{d}{}^{e}\widehat C{}_{b}{}_{d}{}^{f}{}^{g}\epsilon{}^{a}{}_{c}{}_{e}{}_{f}{}_{g}\\
&-\frac{86015}{82944}\widehat G{}^{a}{}^{b}\widehat G{}_{b}{}^{c}\widehat G{}^{d}{}^{e}\widehat G{}^{f}{}^{g}\epsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g}\\
&+\frac{98689}{41472}\widehat H{}^{b}{}^{c}\widehat G{}^{a}{}^{d}\widehat G{}_{d}{}^{e}\widehat G{}^{f}{}^{g}\epsilon{}_{b}{}_{c}{}_{e}{}_{f}{}_{g}\\
&-\frac{23027}{20736}\widehat H{}^{b}{}^{c}\widehat H{}^{d}{}^{e}\widehat G{}^{a}{}^{f}\widehat G{}_{f}{}^{g}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{g}\\
&+\frac{2243}{41472}\widehat H{}^{b}{}^{c}\widehat G{}^{a}{}_{b}\widehat G{}^{d}{}^{e}\widehat G{}^{f}{}^{g}\epsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g}\\
&-\frac{6947}{5184}\widehat H{}^{b}{}^{c}\widehat H{}^{d}{}^{e}\widehat H{}^{f}{}^{g}\widehat G{}^{a}{}_{b}\epsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g}\\
&+\frac{34427}{41472}\widehat H{}^{a}{}^{b}\widehat G{}_{b}{}^{c}\widehat G{}^{d}{}^{e}\widehat G{}^{f}{}^{g}\epsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g}\\
&-\frac{4385}{20736}\widehat H{}^{a}{}^{b}\widehat H{}_{b}{}^{c}\widehat G{}^{d}{}^{e}\widehat G{}^{f}{}^{g}\epsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g}\\
&+\frac{1801}{5184}\widehat H{}^{a}{}^{b}\widehat H{}^{c}{}^{d}\widehat H{}^{e}{}^{f}\widehat G{}_{b}{}^{g}\epsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g}\\
&-\frac{44159}{10368}\widehat H{}^{a}{}^{b}\widehat H{}_{b}{}^{c}\widehat H{}^{d}{}^{e}\widehat G{}^{f}{}^{g}\epsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g}\\
&+\frac{13625}{2592}\widehat H{}^{a}{}^{b}\widehat H{}_{b}{}^{c}\widehat H{}^{d}{}^{e}\widehat H{}^{f}{}^{g}\epsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g}\\
&-\frac{551}{10368}\widehat G{}^{b}{}^{c}\widehat G{}_{b}{}^{d}\widehat G{}_{c}{}^{e}\widehat G{}^{f}{}^{g}\epsilon{}^{a}{}_{d}{}_{e}{}_{f}{}_{g}\\
&+\frac{889}{2592}\widehat H{}^{b}{}^{c}\widehat G{}^{d}{}^{e}\widehat G{}_{d}{}^{f}\widehat G{}_{e}{}^{g}\epsilon{}^{a}{}_{b}{}_{c}{}_{f}{}_{g}\\
&+\frac{26779}{20736}\widehat H{}^{b}{}^{c}\widehat G{}_{b}{}^{d}\widehat G{}_{d}{}^{e}\widehat G{}^{f}{}^{g}\epsilon{}^{a}{}_{c}{}_{e}{}_{f}{}_{g}\\
&-\frac{23027}{41472}\widehat H{}^{b}{}^{c}\widehat H{}^{d}{}^{e}\epsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{e}\widehat G^2
\end{aligned}
```

```math
\begin{aligned}
&-\frac{19823}{10368}\widehat H{}^{b}{}^{c}\widehat H{}^{d}{}^{e}\widehat G{}_{b}{}_{d}\widehat G{}^{f}{}^{g}\epsilon{}^{a}{}_{c}{}_{e}{}_{f}{}_{g}\\
&+\frac{21275}{5184}\widehat H{}^{b}{}^{c}\widehat H{}^{d}{}^{e}\widehat H{}^{f}{}^{g}\widehat G{}_{b}{}_{d}\epsilon{}^{a}{}_{c}{}_{e}{}_{f}{}_{g}\\
&+\frac{125}{20736}\widehat H{}^{b}{}^{c}\widehat G{}_{b}{}^{d}\widehat G{}_{c}{}^{e}\widehat G{}^{f}{}^{g}\epsilon{}^{a}{}_{d}{}_{e}{}_{f}{}_{g}\\
&-\frac{1181}{10368}\widehat H{}^{b}{}^{c}\widehat H{}^{d}{}^{e}\widehat G{}_{b}{}^{f}\widehat G{}_{c}{}^{g}\epsilon{}^{a}{}_{d}{}_{e}{}_{f}{}_{g}\\
&-\frac{4385}{41472}\widehat H{}^{b}{}^{c}\widehat H{}_{b}{}_{c}\widehat G{}^{d}{}^{e}\widehat G{}^{f}{}^{g}\epsilon{}^{a}{}_{d}{}_{e}{}_{f}{}_{g}\\
&+\frac{12205}{5184}\widehat H{}^{b}{}^{c}\widehat H{}_{b}{}^{d}\widehat H{}^{e}{}^{f}\widehat G{}_{c}{}^{g}\epsilon{}^{a}{}_{d}{}_{e}{}_{f}{}_{g}\\
&+\frac{122}{81}\widehat H{}^{b}{}^{c}\widehat H{}_{b}{}^{d}\widehat H{}_{c}{}^{e}\widehat G{}^{f}{}^{g}\epsilon{}^{a}{}_{d}{}_{e}{}_{f}{}_{g}\\
&-\frac{635}{162}\widehat H{}^{b}{}^{c}\widehat H{}_{b}{}^{d}\widehat H{}_{c}{}^{e}\widehat H{}^{f}{}^{g}\epsilon{}^{a}{}_{d}{}_{e}{}_{f}{}_{g}\\
&+\frac{551}{41472}\widehat G{}^{b}{}^{c}\widehat G{}^{d}{}^{e}\epsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{e}\widehat G^2\\
&-\frac{889}{5184}\widehat H{}^{b}{}^{c}\widehat G{}^{d}{}^{e}\epsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{e}\widehat G^2\\
&-\frac{1237}{5184}\widehat H{}^{b}{}^{c}\widehat G{}_{b}{}_{c}\widehat G{}^{d}{}^{e}\widehat G{}^{f}{}^{g}\epsilon{}^{a}{}_{d}{}_{e}{}_{f}{}_{g}\\
&+\frac{1513}{1296}\widehat H{}^{b}{}^{c}\widehat H{}^{d}{}^{e}\widehat G{}_{b}{}_{c}\widehat G{}^{f}{}^{g}\epsilon{}^{a}{}_{d}{}_{e}{}_{f}{}_{g}\\
&-\frac{3209}{2592}\widehat H{}^{b}{}^{c}\widehat H{}^{d}{}^{e}\widehat H{}^{f}{}^{g}\widehat G{}_{b}{}_{c}\epsilon{}^{a}{}_{d}{}_{e}{}_{f}{}_{g}\\
&-\frac{61}{81}\widehat H{}^{b}{}^{c}\widehat H{}_{b}{}_{c}\widehat H{}^{d}{}^{e}\widehat G{}^{f}{}^{g}\epsilon{}^{a}{}_{d}{}_{e}{}_{f}{}_{g}\\
&+\frac{635}{648}\widehat H{}^{b}{}^{c}\widehat H{}_{b}{}_{c}\widehat H{}^{d}{}^{e}\widehat H{}^{f}{}^{g}\epsilon{}^{a}{}_{d}{}_{e}{}_{f}{}_{g}\\
&-\frac{1}{6}\big(\mathcal D^{b}\widehat G{}^{a}{}_{b}\big)\widehat G^2\\
&-\frac{2}{3}\big(\mathcal D^{b}\widehat H{}^{a}{}_{b}\big)\widehat G^2\\
&+2\widehat H{}^{b}{}^{c}\widehat G{}_{b}{}_{c}\big(\mathcal D^{d}\widehat G{}^{a}{}_{d}\big)\\
&-\frac{2}{3}\widehat H{}^{b}{}^{c}\widehat H{}_{b}{}_{c}\big(\mathcal D^{d}\widehat G{}^{a}{}_{d}\big)\\
&-\frac{8}{3}\widehat H{}^{b}{}^{c}\widehat H{}_{b}{}_{c}\big(\mathcal D^{d}\widehat H{}^{a}{}_{d}\big)\\
&+\frac{2}{3}\widehat G{}^{b}{}^{c}\widehat G{}_{b}{}^{d}\big(\mathcal D_{c}\widehat G{}^{a}{}_{d}\big)\\
&+\frac{2}{3}\big(\mathcal D^{b}\widehat H{}^{a}{}^{c}\big)\widehat G{}_{b}{}^{d}\widehat G{}_{c}{}_{d}\\
&-\frac{8}{3}\widehat H{}^{b}{}^{c}\widehat G{}_{b}{}^{d}\big(\mathcal D_{d}\widehat G{}^{a}{}_{c}\big)\\
&-\frac{8}{3}\widehat H{}^{b}{}^{c}\big(\mathcal D^{d}\widehat H{}^{a}{}_{b}\big)\widehat G{}_{c}{}_{d}
\end{aligned}
```

```math
\begin{aligned}
&+\frac{16}{3}\widehat H{}^{b}{}^{c}\big(\mathcal D_{b}\widehat H{}^{a}{}^{d}\big)\widehat G{}_{c}{}_{d}\\
&+\frac{8}{3}\widehat H{}^{b}{}^{c}\widehat H{}_{b}{}^{d}\big(\mathcal D_{c}\widehat G{}^{a}{}_{d}\big)\\
&+\frac{32}{3}\widehat H{}^{b}{}^{c}\widehat H{}_{b}{}^{d}\big(\mathcal D_{c}\widehat H{}^{a}{}_{d}\big)\\
&-\frac{2}{3}\widehat G{}^{a}{}^{b}\widehat G{}_{b}{}^{c}\big(\mathcal D^{d}\widehat G{}_{c}{}_{d}\big)\\
&-\frac{2}{3}\big(\mathcal D^{b}\widehat H{}_{b}{}^{c}\big)\widehat G{}^{a}{}^{d}\widehat G{}_{c}{}_{d}\\
&+\frac{10}{3}\widehat H{}^{b}{}^{c}\widehat G{}^{a}{}_{b}\big(\mathcal D^{d}\widehat G{}_{c}{}_{d}\big)\\
&+\frac{8}{3}\widehat H{}^{b}{}^{c}\big(\mathcal D^{d}\widehat H{}_{b}{}_{d}\big)\widehat G{}^{a}{}_{c}\\
&-\frac{2}{3}\widehat H{}^{a}{}^{b}\widehat G{}_{b}{}^{c}\big(\mathcal D^{d}\widehat G{}_{c}{}_{d}\big)\\
&-\frac{16}{3}\widehat H{}^{a}{}^{b}\big(\mathcal D^{c}\widehat H{}_{c}{}^{d}\big)\widehat G{}_{b}{}_{d}\\
&-\frac{8}{3}\widehat H{}^{a}{}^{b}\widehat H{}_{b}{}^{c}\big(\mathcal D^{d}\widehat G{}_{c}{}_{d}\big)\\
&-\frac{32}{3}\widehat H{}^{a}{}^{b}\widehat H{}_{b}{}^{c}\big(\mathcal D^{d}\widehat H{}_{c}{}_{d}\big)\\
&+\frac{7}{3}\widehat G{}^{a}{}^{b}\widehat G{}^{c}{}^{d}\big(\mathcal D_{c}\widehat G{}_{b}{}_{d}\big)\\
&-\frac{10}{3}\big(\mathcal D^{b}\widehat H{}^{c}{}^{d}\big)\widehat G{}^{a}{}_{c}\widehat G{}_{b}{}_{d}\\
&+2\widehat H{}^{b}{}^{c}\widehat G{}^{a}{}^{d}\big(\mathcal D_{b}\widehat G{}_{c}{}_{d}\big)\\
&-\frac{8}{3}\widehat H{}^{b}{}^{c}\big(\mathcal D_{b}\widehat H{}_{c}{}^{d}\big)\widehat G{}^{a}{}_{d}\\
&-\frac{4}{3}\widehat H{}^{a}{}^{b}\widehat G{}^{c}{}^{d}\big(\mathcal D_{c}\widehat G{}_{b}{}_{d}\big)\\
&+\frac{8}{3}\widehat H{}^{a}{}^{b}\big(\mathcal D^{c}\widehat H{}_{b}{}^{d}\big)\widehat G{}_{c}{}_{d}\\
&-\frac{20}{3}\widehat H{}^{a}{}^{b}\widehat H{}^{c}{}^{d}\big(\mathcal D_{c}\widehat G{}_{b}{}_{d}\big)\\
&+\frac{32}{3}\widehat H{}^{a}{}^{b}\widehat H{}^{c}{}^{d}\big(\mathcal D_{c}\widehat H{}_{b}{}_{d}\big)\\
&-\frac{7}{6}\widehat G{}^{a}{}^{b}\widehat G{}^{c}{}^{d}\big(\mathcal D_{b}\widehat G{}_{c}{}_{d}\big)\\
&+2\big(\mathcal D^{b}\widehat H{}^{c}{}^{d}\big)\widehat G{}^{a}{}_{b}\widehat G{}_{c}{}_{d}\\
&+\frac{10}{3}\widehat H{}^{b}{}^{c}\widehat G{}^{a}{}^{d}\big(\mathcal D_{d}\widehat G{}_{b}{}_{c}\big)\\
&-\frac{4}{3}\widehat H{}^{b}{}^{c}\big(\mathcal D^{d}\widehat H{}_{b}{}_{c}\big)\widehat G{}^{a}{}_{d}\\
&-\frac{1}{3}\widehat H{}^{a}{}^{b}\widehat G{}^{c}{}^{d}\big(\mathcal D_{b}\widehat G{}_{c}{}_{d}\big)
\end{aligned}
```

```math
\begin{aligned}
&+\frac{2}{3}\widehat H{}^{a}{}^{b}\widehat H{}^{c}{}^{d}\big(\mathcal D_{b}\widehat G{}_{c}{}_{d}\big)\\
&-\frac{16}{3}\widehat H{}^{a}{}^{b}\widehat H{}^{c}{}^{d}\big(\mathcal D_{b}\widehat H{}_{c}{}_{d}\big)\\
&-\frac{1}{4}\big(\mathcal D^{b}\widehat C{}^{a}{}^{c}{}_{b}{}^{d}\big)\widehat G{}_{c}{}_{d}\\
&+\widehat H{}^{b}{}^{c}\big(\mathcal D^{d}\widehat C{}^{a}{}_{b}{}_{c}{}_{d}\big)\\
&-\frac{1}{8}\big(\mathcal D^{b}\widehat C{}^{a}{}_{b}{}^{c}{}^{d}\big)\widehat G{}_{c}{}_{d}\\
&-\frac{1}{2}\widehat H{}^{b}{}^{c}\big(\mathcal D^{d}\widehat C{}^{a}{}_{d}{}_{b}{}_{c}\big)\\
&-\frac{7}{18}\widehat G{}^{b}{}^{c}\widehat G{}^{d}{}^{e}\big(\mathcal D^{f}\mathcal D^{a}\sigma\big)\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\\
&+\frac{7}{72}\widehat G{}^{b}{}^{c}\widehat G{}^{d}{}^{e}\big(\mathcal D^{a}\mathcal D^{f}\sigma\big)\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\\
&+\frac{7}{144}\widehat G{}^{a}{}^{b}\big(\mathcal D^{c}\mathcal D^{d}\widehat G{}^{e}{}^{f}\big)\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\\
&+\frac{13}{9}\widehat H{}^{b}{}^{c}\widehat G{}^{a}{}^{d}\big(\mathcal D^{e}\mathcal D^{f}\sigma\big)\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\\
&-\frac{25}{72}\big(\mathcal D^{b}\mathcal D^{c}\widehat H{}^{d}{}^{e}\big)\widehat G{}^{a}{}^{f}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\\
&+\frac{257}{144}\widehat H{}^{a}{}^{b}\widehat G{}^{c}{}^{d}\big(\mathcal D^{e}\mathcal D^{f}\sigma\big)\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\\
&+\frac{91}{144}\widehat H{}^{a}{}^{b}\big(\mathcal D^{c}\mathcal D^{d}\widehat G{}^{e}{}^{f}\big)\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\\
&+\frac{37}{18}\widehat H{}^{b}{}^{c}\widehat H{}^{d}{}^{e}\big(\mathcal D^{f}\mathcal D^{a}\sigma\big)\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\\
&-\frac{7}{18}\widehat H{}^{b}{}^{c}\widehat H{}^{d}{}^{e}\big(\mathcal D^{a}\mathcal D^{f}\sigma\big)\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\\
&-\frac{55}{72}\widehat H{}^{a}{}^{b}\big(\mathcal D^{c}\mathcal D^{d}\widehat H{}^{e}{}^{f}\big)\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\\
&+\frac{7}{24}\widehat G{}^{b}{}^{c}\widehat G{}^{d}{}^{e}\big(\Box^c \sigma\big)\epsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{e}\\
&-\frac{1}{36}\widehat G{}^{b}{}^{c}\big(\mathcal D_{b}\mathcal D^{d}\widehat G{}^{e}{}^{f}\big)\epsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f}\\
&-\frac{11}{36}\widehat H{}^{b}{}^{c}\widehat G{}^{d}{}^{e}\big(\mathcal D_{d}\mathcal D^{f}\sigma\big)\epsilon{}^{a}{}_{b}{}_{c}{}_{e}{}_{f}\\
&-\frac{5}{36}\big(\mathcal D^{b}\mathcal D^{c}\widehat H{}^{d}{}^{e}\big)\widehat G{}_{b}{}^{f}\epsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f}\\
&+\frac{149}{144}\widehat H{}^{b}{}^{c}\widehat G{}^{d}{}^{e}\big(\mathcal D_{b}\mathcal D^{f}\sigma\big)\epsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f}\\
&-\frac{37}{144}\widehat H{}^{b}{}^{c}\big(\mathcal D_{b}\mathcal D^{d}\widehat G{}^{e}{}^{f}\big)\epsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f}\\
&-\frac{5}{3}\widehat H{}^{b}{}^{c}\widehat H{}^{d}{}^{e}\big(\Box^c \sigma\big)\epsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{e}\\
&+\frac{25}{72}\widehat H{}^{b}{}^{c}\big(\mathcal D_{b}\mathcal D^{d}\widehat H{}^{e}{}^{f}\big)\epsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f}
\end{aligned}
```

```math
\begin{aligned}
&-\frac{1}{8}\widehat G{}^{b}{}^{c}\big(\mathcal D^{d}\mathcal D^{e}\widehat G{}_{b}{}^{f}\big)\epsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f}\\
&+\frac{43}{24}\widehat H{}^{b}{}^{c}\widehat G{}_{b}{}^{d}\big(\mathcal D^{e}\mathcal D^{f}\sigma\big)\epsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f}\\
&-\frac{5}{12}\big(\mathcal D^{b}\mathcal D^{c}\widehat H{}^{d}{}^{e}\big)\widehat G{}_{d}{}^{f}\epsilon{}^{a}{}_{b}{}_{c}{}_{e}{}_{f}\\
&-\frac{5}{8}\widehat H{}^{b}{}^{c}\big(\mathcal D^{d}\mathcal D^{e}\widehat G{}_{b}{}^{f}\big)\epsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f}\\
&+\frac{11}{12}\widehat H{}^{b}{}^{c}\big(\mathcal D^{d}\mathcal D^{e}\widehat H{}_{b}{}^{f}\big)\epsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f}\\
&+\frac{1}{12}\widehat G{}^{b}{}^{c}\big(\mathcal D^{d}\mathcal D^{e}\widehat G{}^{a}{}^{f}\big)\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\\
&-\frac{1}{2}\big(\mathcal D^{b}\mathcal D^{c}\widehat H{}^{a}{}^{d}\big)\widehat G{}^{e}{}^{f}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\\
&+\frac{5}{6}\widehat H{}^{b}{}^{c}\big(\mathcal D^{d}\mathcal D^{e}\widehat G{}^{a}{}^{f}\big)\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\\
&-\widehat H{}^{b}{}^{c}\big(\mathcal D^{d}\mathcal D^{e}\widehat H{}^{a}{}^{f}\big)\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\\
&-\frac{25}{144}\widehat G{}^{b}{}^{c}\big(\mathcal D^{d}\mathcal D^{e}\widehat G{}_{d}{}^{f}\big)\epsilon{}^{a}{}_{b}{}_{c}{}_{e}{}_{f}\\
&+\frac{25}{72}\big(\mathcal D^{b}\mathcal D^{c}\widehat H{}_{b}{}^{d}\big)\widehat G{}^{e}{}^{f}\epsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f}\\
&-\frac{11}{18}\widehat H{}^{b}{}^{c}\big(\mathcal D^{d}\mathcal D^{e}\widehat G{}_{d}{}^{f}\big)\epsilon{}^{a}{}_{b}{}_{c}{}_{e}{}_{f}\\
&+\frac{11}{9}\widehat H{}^{b}{}^{c}\big(\mathcal D^{d}\mathcal D^{e}\widehat H{}_{d}{}^{f}\big)\epsilon{}^{a}{}_{b}{}_{c}{}_{e}{}_{f}\\
&-\frac{5}{288}\widehat G{}^{b}{}^{c}\big(\mathcal D^{a}\mathcal D^{d}\widehat G{}^{e}{}^{f}\big)\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\\
&+\frac{13}{24}\widehat H{}^{b}{}^{c}\widehat G{}^{d}{}^{e}\big(\mathcal D^{a}\mathcal D^{f}\sigma\big)\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\\
&-\frac{19}{144}\big(\mathcal D^{a}\mathcal D^{b}\widehat H{}^{c}{}^{d}\big)\widehat G{}^{e}{}^{f}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\\
&+\frac{2}{9}\widehat H{}^{b}{}^{c}\big(\mathcal D^{a}\mathcal D^{d}\widehat G{}^{e}{}^{f}\big)\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\\
&-\frac{1}{9}\widehat H{}^{b}{}^{c}\big(\mathcal D^{a}\mathcal D^{d}\widehat H{}^{e}{}^{f}\big)\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\\
&-\frac{5}{144}\widehat G{}^{b}{}^{c}\big(\mathcal D^{d}\mathcal D^{e}\widehat G{}_{e}{}^{f}\big)\epsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{f}\\
&-\frac{371}{144}\widehat H{}^{b}{}^{c}\widehat G{}^{d}{}^{e}\big(\mathcal D^{f}\mathcal D_{b}\sigma\big)\epsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f}\\
&-\frac{55}{72}\big(\mathcal D^{b}\mathcal D^{c}\widehat H{}_{c}{}^{d}\big)\widehat G{}^{e}{}^{f}\epsilon{}^{a}{}_{b}{}_{d}{}_{e}{}_{f}\\
&-\frac{65}{72}\widehat H{}^{b}{}^{c}\widehat G{}^{d}{}^{e}\big(\mathcal D^{f}\mathcal D_{d}\sigma\big)\epsilon{}^{a}{}_{b}{}_{c}{}_{e}{}_{f}\\
&-\frac{7}{72}\widehat H{}^{b}{}^{c}\big(\mathcal D^{d}\mathcal D^{e}\widehat G{}_{e}{}^{f}\big)\epsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{f}\\
&+\frac{67}{36}\widehat H{}^{b}{}^{c}\big(\mathcal D^{d}\mathcal D^{e}\widehat H{}_{e}{}^{f}\big)\epsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{f}
\end{aligned}
```

```math
\begin{aligned}
&+\frac{23}{288}\widehat G{}^{b}{}^{c}\big(\mathcal D^{d}\mathcal D^{a}\widehat G{}^{e}{}^{f}\big)\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\\
&+\frac{43}{48}\widehat H{}^{b}{}^{c}\widehat G{}^{d}{}^{e}\big(\mathcal D^{f}\mathcal D^{a}\sigma\big)\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\\
&-\frac{11}{144}\big(\mathcal D^{b}\mathcal D^{a}\widehat H{}^{c}{}^{d}\big)\widehat G{}^{e}{}^{f}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\\
&+\frac{13}{144}\widehat H{}^{b}{}^{c}\big(\mathcal D^{d}\mathcal D^{a}\widehat G{}^{e}{}^{f}\big)\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\\
&-\frac{25}{72}\widehat H{}^{b}{}^{c}\big(\mathcal D^{d}\mathcal D^{a}\widehat H{}^{e}{}^{f}\big)\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\\
&+\frac{5}{72}\widehat G{}^{b}{}^{c}\big(\mathcal D^{d}\mathcal D_{b}\widehat G{}^{e}{}^{f}\big)\epsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f}\\
&+\frac{1}{18}\big(\mathcal D^{b}\mathcal D^{c}\widehat H{}^{d}{}^{e}\big)\widehat G{}_{c}{}^{f}\epsilon{}^{a}{}_{b}{}_{d}{}_{e}{}_{f}\\
&+\frac{43}{144}\widehat H{}^{b}{}^{c}\big(\mathcal D^{d}\mathcal D_{b}\widehat G{}^{e}{}^{f}\big)\epsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f}\\
&-\frac{55}{72}\widehat H{}^{b}{}^{c}\big(\mathcal D^{d}\mathcal D_{b}\widehat H{}^{e}{}^{f}\big)\epsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f}\\
&-\frac{7}{48}\widehat G{}^{b}{}^{c}\big(\Box^c \widehat G{}^{e}{}^{f}\big)\epsilon{}^{a}{}_{b}{}_{c}{}_{e}{}_{f}\\
&-\frac{23}{16}\widehat H{}^{b}{}^{c}\widehat G{}^{d}{}^{e}\big(\Box^c \sigma\big)\epsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{e}\\
&+\frac{5}{24}\big(\Box^c \widehat H{}^{c}{}^{d}\big)\widehat G{}^{e}{}^{f}\epsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f}\\
&+\frac{17}{48}\widehat H{}^{b}{}^{c}\big(\Box^c \widehat G{}^{e}{}^{f}\big)\epsilon{}^{a}{}_{b}{}_{c}{}_{e}{}_{f}\\
&+\frac{11}{24}\widehat H{}^{b}{}^{c}\big(\Box^c \widehat H{}^{e}{}^{f}\big)\epsilon{}^{a}{}_{b}{}_{c}{}_{e}{}_{f}\\
&-\frac{1}{3}\widehat G{}^{a}{}^{b}\big(\mathcal D_{b}\Box^c \sigma\big)\\
&-\frac{4}{3}\widehat H{}^{a}{}^{b}\big(\mathcal D_{b}\Box^c \sigma\big)\\
&-\frac{4}{3}g^{2}L_c{}^{i}{}^{j}\big(\mathcal D^{b}L_c{}_{i}{}_{j}\big)\widehat G{}^{a}{}_{b}\\
&+\frac{2}{3}g^{2}\widehat H{}^{a}{}^{b}L_c{}^{i}{}^{j}\big(\mathcal D_{b}L_c{}_{i}{}_{j}\big)\\
&-\frac{5}{3}g\big(\mathcal D^{b}N_c\big)\widehat G{}^{a}{}_{b}\\
&+\frac{4}{3}g\widehat H{}^{a}{}^{b}\big(\mathcal D_{b}N_c\big)\\
&-\frac{2}{3}\big(\mathcal D^{b}\widehat G{}^{a}{}_{b}\big)\big(\Box^c \sigma\big)\\
&+\frac{10}{3}\big(\mathcal D^{b}\widehat H{}^{a}{}_{b}\big)\big(\Box^c \sigma\big)\\
&-\frac{2}{3}g^{2}L_c{}^{i}{}^{j}L_c{}_{i}{}_{j}\big(\mathcal D^{b}\widehat G{}^{a}{}_{b}\big)\\
&+\frac{1}{3}g^{2}\big(\mathcal D^{b}\widehat H{}^{a}{}_{b}\big)L_c{}^{i}{}^{j}L_c{}_{i}{}_{j}
\end{aligned}
```

```math
\begin{aligned}
&-\frac{5}{3}N_cg\big(\mathcal D^{b}\widehat G{}^{a}{}_{b}\big)\\
&+\frac{4}{3}N_cg\big(\mathcal D^{b}\widehat H{}^{a}{}_{b}\big)\\
&+\frac{113}{1536}\big(\mathcal D^{b}\widehat G{}^{a}{}^{c}\big)\big(\mathcal D^{d}\widehat G{}^{e}{}^{f}\big)\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\\
&-\frac{881}{768}\big(\mathcal D^{b}\widehat H{}^{c}{}^{d}\big)\big(\mathcal D^{e}\widehat G{}^{a}{}^{f}\big)\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\\
&+\frac{1199}{768}\big(\mathcal D^{b}\widehat H{}^{a}{}^{c}\big)\big(\mathcal D^{d}\widehat G{}^{e}{}^{f}\big)\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\\
&-\frac{431}{384}\big(\mathcal D^{b}\widehat H{}^{a}{}^{c}\big)\big(\mathcal D^{d}\widehat H{}^{e}{}^{f}\big)\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\\
&+\frac{1105}{1536}\big(\mathcal D^{b}\widehat G{}^{c}{}^{d}\big)\big(\mathcal D_{c}\widehat G{}^{e}{}^{f}\big)\epsilon{}^{a}{}_{b}{}_{d}{}_{e}{}_{f}\\
&-\frac{401}{768}\big(\mathcal D^{b}\widehat H{}^{c}{}^{d}\big)\big(\mathcal D^{e}\widehat G{}_{b}{}^{f}\big)\epsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f}\\
&-\frac{1265}{768}\big(\mathcal D^{b}\widehat H{}^{c}{}^{d}\big)\big(\mathcal D_{c}\widehat G{}^{e}{}^{f}\big)\epsilon{}^{a}{}_{b}{}_{d}{}_{e}{}_{f}\\
&+\frac{187}{128}\big(\mathcal D^{b}\widehat H{}^{c}{}^{d}\big)\big(\mathcal D_{c}\widehat H{}^{e}{}^{f}\big)\epsilon{}^{a}{}_{b}{}_{d}{}_{e}{}_{f}\\
&-\frac{1039}{768}\big(\mathcal D^{b}\widehat G{}^{c}{}^{d}\big)\big(\mathcal D^{e}\widehat G{}_{c}{}^{f}\big)\epsilon{}^{a}{}_{b}{}_{d}{}_{e}{}_{f}\\
&+\frac{245}{64}\big(\mathcal D^{b}\widehat H{}^{c}{}^{d}\big)\big(\mathcal D^{e}\widehat G{}_{c}{}^{f}\big)\epsilon{}^{a}{}_{b}{}_{d}{}_{e}{}_{f}\\
&-\frac{431}{192}\big(\mathcal D^{b}\widehat H{}^{c}{}^{d}\big)\big(\mathcal D^{e}\widehat H{}_{c}{}^{f}\big)\epsilon{}^{a}{}_{b}{}_{d}{}_{e}{}_{f}\\
&+\frac{175}{512}\big(\mathcal D^{b}\widehat G{}_{b}{}^{c}\big)\big(\mathcal D^{d}\widehat G{}^{e}{}^{f}\big)\epsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f}\\
&-\frac{17}{256}\big(\mathcal D^{b}\widehat H{}^{c}{}^{d}\big)\big(\mathcal D^{e}\widehat G{}_{e}{}^{f}\big)\epsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{f}\\
&+\frac{49}{256}\big(\mathcal D^{b}\widehat H{}_{b}{}^{c}\big)\big(\mathcal D^{d}\widehat G{}^{e}{}^{f}\big)\epsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f}\\
&-\frac{241}{128}\big(\mathcal D^{b}\widehat H{}_{b}{}^{c}\big)\big(\mathcal D^{d}\widehat H{}^{e}{}^{f}\big)\epsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f}\\
&-\frac{415}{1536}\big(\mathcal D^{a}\widehat G{}^{b}{}^{c}\big)\big(\mathcal D^{d}\widehat G{}^{e}{}^{f}\big)\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\\
&+\frac{415}{768}\big(\mathcal D^{b}\widehat H{}^{c}{}^{d}\big)\big(\mathcal D^{a}\widehat G{}^{e}{}^{f}\big)\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\\
&+\frac{191}{768}\big(\mathcal D^{a}\widehat H{}^{b}{}^{c}\big)\big(\mathcal D^{d}\widehat G{}^{e}{}^{f}\big)\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\\
&-\frac{191}{384}\big(\mathcal D^{a}\widehat H{}^{b}{}^{c}\big)\big(\mathcal D^{d}\widehat H{}^{e}{}^{f}\big)\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\\
&-\frac{353}{1536}\big(\mathcal D^{b}\widehat G{}^{c}{}^{d}\big)\big(\mathcal D_{b}\widehat G{}^{e}{}^{f}\big)\epsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f}\\
&+\frac{59}{128}\big(\mathcal D^{b}\widehat H{}^{c}{}^{d}\big)\big(\mathcal D_{b}\widehat G{}^{e}{}^{f}\big)\epsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f}\\
&+\frac{191}{384}\big(\mathcal D^{b}\widehat H{}^{c}{}^{d}\big)\big(\mathcal D_{b}\widehat H{}^{e}{}^{f}\big)\epsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f}
\end{aligned}
```

```math
\begin{aligned}
&+gL_c{}^{i}{}^{j}\big(\mathcal D^{b}\widehat R(V){}^{a}{}_{b}{}_{i}{}_{j}\big)\\
&+g\big(\mathcal D^{b}L_c{}^{i}{}^{j}\big)\widehat R(V){}^{a}{}_{b}{}_{i}{}_{j}\\
&-\frac{31}{192}\widehat H{}^{b}{}^{c}\widehat C{}^{a}{}^{d}{}^{e}{}^{f}\widehat G{}_{e}{}^{g}\epsilon{}_{b}{}_{c}{}_{d}{}_{f}{}_{g}\\
&-\frac{1}{8}\widehat H{}^{b}{}^{c}\widehat C{}^{a}{}^{d}{}^{e}{}^{f}\widehat G{}_{b}{}^{g}\epsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g}\\
&-\frac{11}{24}\widehat H{}^{b}{}^{c}\widehat C{}^{a}{}^{d}{}_{b}{}^{e}\widehat G{}^{f}{}^{g}\epsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g}\\
&-\frac{25}{64}\widehat H{}^{b}{}^{c}\widehat C{}^{a}{}^{d}{}^{e}{}^{f}\widehat G{}_{d}{}^{g}\epsilon{}_{b}{}_{c}{}_{e}{}_{f}{}_{g}\\
&+\frac{1}{64}\widehat H{}^{b}{}^{c}\widehat C{}^{a}{}_{b}{}^{d}{}^{e}\widehat G{}^{f}{}^{g}\epsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g}\\
&+\frac{63}{16}\widehat H{}^{b}{}^{c}\widehat G{}^{a}{}^{d}\widehat G{}_{b}{}^{e}\widehat G{}^{f}{}^{g}\epsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g}\\
&-\frac{37}{4}\widehat H{}^{a}{}^{b}\widehat H{}^{c}{}^{d}\widehat H{}^{e}{}^{f}\widehat G{}_{c}{}^{g}\epsilon{}_{b}{}_{d}{}_{e}{}_{f}{}_{g}\\
&+\frac{2}{3}\widehat G{}^{a}{}^{b}\big(\Box^c \mathcal D_{b}\sigma\big)\\
&+\frac{1}{2}\big(\mathcal D^{b}\widehat G{}^{a}{}^{c}\big)\big(\mathcal D_{b}\mathcal D_{c}\sigma\big)\\
&+\frac{8}{3}\widehat H{}^{a}{}^{b}\big(\Box^c \mathcal D_{b}\sigma\big)\\
&+5\big(\mathcal D^{b}\widehat H{}^{a}{}^{c}\big)\big(\mathcal D_{b}\mathcal D_{c}\sigma\big)\\
&-2\big(\Box^c \mathcal D^{c}\widehat H{}^{a}{}_{c}\big)\\
&+\frac{1}{2}\big(\mathcal D^{b}\widehat G{}^{a}{}^{c}\big)\big(\mathcal D_{c}\mathcal D_{b}\sigma\big)\\
&-\big(\mathcal D^{b}\widehat H{}^{a}{}^{c}\big)\big(\mathcal D_{c}\mathcal D_{b}\sigma\big)\\
&-\frac{5}{4}\big(\mathcal D^{b}\widehat G{}_{b}{}^{c}\big)\big(\mathcal D_{c}\mathcal D^{a}\sigma\big)\\
&+\frac{5}{2}\big(\mathcal D^{b}\widehat H{}_{b}{}^{c}\big)\big(\mathcal D_{c}\mathcal D^{a}\sigma\big)\\
&+\frac{1}{4}\big(\mathcal D^{b}\widehat G{}_{b}{}^{c}\big)\big(\mathcal D^{a}\mathcal D_{c}\sigma\big)\\
&-\frac{1}{2}\big(\mathcal D^{b}\widehat H{}_{b}{}^{c}\big)\big(\mathcal D^{a}\mathcal D_{c}\sigma\big)\\
&+\frac{1}{2}\big(\mathcal D^{a}\widehat G{}^{b}{}^{c}\big)\big(\mathcal D_{b}\mathcal D_{c}\sigma\big)\\
&-\big(\mathcal D^{a}\widehat H{}^{b}{}^{c}\big)\big(\mathcal D_{b}\mathcal D_{c}\sigma\big)\\
&-\frac{89}{144}\widehat H{}^{b}{}^{c}\widehat H{}^{d}{}^{e}\widehat G{}_{b}{}^{f}\widehat G{}_{d}{}^{g}\epsilon{}^{a}{}_{c}{}_{e}{}_{f}{}_{g}\\
&+\frac{2}{3}\widehat H{}^{b}{}^{c}\widehat G{}_{b}{}^{d}\big(\mathcal D^{a}\widehat G{}_{c}{}_{d}\big)
\end{aligned}
```

## E: 2 explicit fermions

```math
\begin{aligned}
E_{\log}^{a}[2]={}&-\frac{505i}{1152}\widehat G{}^{a}{}_{b}\overline{\widehat R(Q){}^{b}{}^{c}{}^{i}}\big(\mathcal D_{c}\psi{}_{i}\big)\\
&+\frac{313}{1536}\widehat G{}^{a}{}^{e}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\widehat R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{d}\big(\mathcal D^{f}\psi{}_{i}\big)\\
&-\frac{839i}{576}\widehat H{}^{a}{}^{b}\overline{\widehat R(Q){}_{b}{}^{c}{}^{i}}\big(\mathcal D_{c}\psi{}_{i}\big)\\
&-\frac{319}{768}\widehat H{}^{a}{}^{b}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\widehat R(Q){}^{c}{}^{d}{}^{i}}\gamma{}^{e}\big(\mathcal D^{f}\psi{}_{i}\big)\\
&+\frac{2645i}{36864}g\widehat G{}^{a}{}^{f}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\widehat R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{d}{}^{e}\varphi_c{}_{i}\\
&+\frac{5083i}{18432}g\widehat H{}^{a}{}^{b}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\widehat R(Q){}^{c}{}^{d}{}^{i}}\gamma{}^{e}{}^{f}\varphi_c{}_{i}\\
&+\frac{4685i}{9216}\widehat G{}_{b}{}_{c}\overline{\widehat R(Q){}^{b}{}^{c}{}^{i}}\big(\mathcal D^{a}\psi{}_{i}\big)\\
&+\frac{425i}{2304}\widehat G{}_{b}{}_{d}\overline{\widehat R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{a}{}^{d}\big(\mathcal D_{c}\psi{}_{i}\big)\\
&+\frac{2047i}{1536}\widehat G{}_{b}{}^{c}\overline{\widehat R(Q){}^{a}{}^{b}{}^{i}}\big(\mathcal D_{c}\psi{}_{i}\big)\\
&+\frac{401}{2304}\widehat G{}_{b}{}^{e}\epsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\widehat R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{d}\big(\mathcal D^{f}\psi{}_{i}\big)\\
&+\frac{3691i}{4608}\widehat H{}^{b}{}^{c}\overline{\widehat R(Q){}_{b}{}_{c}{}^{i}}\big(\mathcal D^{a}\psi{}_{i}\big)\\
&+\frac{473i}{768}\widehat H{}^{b}{}^{c}\overline{\widehat R(Q){}^{a}{}_{b}{}^{i}}\big(\mathcal D_{c}\psi{}_{i}\big)\\
&-\frac{305i}{1152}\widehat H{}^{b}{}^{c}\overline{\widehat R(Q){}_{b}{}^{d}{}^{i}}\gamma{}^{a}{}_{c}\big(\mathcal D_{d}\psi{}_{i}\big)\\
&-\frac{1469}{1152}\widehat H{}^{b}{}^{c}\epsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\widehat R(Q){}_{b}{}^{d}{}^{i}}\gamma{}^{e}\big(\mathcal D^{f}\psi{}_{i}\big)\\
&+\frac{2071i}{18432}g\widehat G{}_{b}{}^{f}\epsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\widehat R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{d}{}^{e}\varphi_c{}_{i}\\
&+\frac{5191i}{9216}g\widehat H{}^{b}{}^{c}\epsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\widehat R(Q){}_{b}{}^{d}{}^{i}}\gamma{}^{e}{}^{f}\varphi_c{}_{i}\\
&+\frac{719i}{3072}\widehat G{}_{b}{}_{c}\overline{\widehat R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{a}{}^{d}\big(\mathcal D_{d}\psi{}_{i}\big)\\
&+\frac{929i}{1536}\widehat H{}^{b}{}^{c}\overline{\widehat R(Q){}_{b}{}_{c}{}^{i}}\gamma{}^{a}{}^{d}\big(\mathcal D_{d}\psi{}_{i}\big)\\
&+\frac{1099}{9216}g\widehat G{}_{b}{}_{c}\overline{\widehat R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{a}\varphi_c{}_{i}\\
&+\frac{6509}{4608}g\widehat H{}^{b}{}^{c}\overline{\widehat R(Q){}_{b}{}_{c}{}^{i}}\gamma{}^{a}\varphi_c{}_{i}\\
&-\frac{803}{18432}\widehat G{}^{e}{}^{f}\epsilon{}^{a}{}_{b}{}_{c}{}_{e}{}_{f}\overline{\widehat R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{d}\big(\mathcal D_{d}\psi{}_{i}\big)\\
&+\frac{539}{9216}\widehat H{}^{b}{}^{c}\epsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\widehat R(Q){}^{d}{}^{e}{}^{i}}\gamma{}^{f}\big(\mathcal D_{f}\psi{}_{i}\big)\\
&+\frac{919i}{18432}g\widehat G{}^{d}{}^{e}\epsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\widehat R(Q){}^{b}{}^{c}{}^{i}}\varphi_c{}_{i}\\
&-\frac{655i}{9216}g\widehat H{}^{b}{}^{c}\epsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\widehat R(Q){}^{d}{}^{e}{}^{i}}\varphi_c{}_{i}
\end{aligned}
```

```math
\begin{aligned}
&-\frac{2269i}{9216}\widehat G{}_{c}{}_{d}\overline{\widehat R(Q){}^{a}{}^{b}{}^{i}}\gamma{}^{c}{}^{d}\big(\mathcal D_{b}\psi{}_{i}\big)\\
&-\frac{181}{3072}\widehat G{}^{d}{}^{e}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\widehat R(Q){}^{a}{}^{b}{}^{i}}\gamma{}^{c}\big(\mathcal D^{f}\psi{}_{i}\big)\\
&-\frac{3731i}{4608}\widehat H{}^{b}{}^{c}\overline{\widehat R(Q){}^{a}{}^{d}{}^{i}}\gamma{}_{b}{}_{c}\big(\mathcal D_{d}\psi{}_{i}\big)\\
&-\frac{115}{1536}\widehat H{}^{b}{}^{c}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\widehat R(Q){}^{a}{}^{d}{}^{i}}\gamma{}^{e}\big(\mathcal D^{f}\psi{}_{i}\big)\\
&+\frac{719i}{18432}g\widehat G{}^{e}{}^{f}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\widehat R(Q){}^{a}{}^{b}{}^{i}}\gamma{}^{c}{}^{d}\varphi_c{}_{i}\\
&+\frac{889i}{9216}g\widehat H{}^{b}{}^{c}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\widehat R(Q){}^{a}{}^{d}{}^{i}}\gamma{}^{e}{}^{f}\varphi_c{}_{i}\\
&+\frac{2129i}{2304}\widehat G{}_{b}{}_{c}\overline{\widehat R(Q){}^{a}{}^{b}{}^{i}}\gamma{}^{c}{}^{d}\big(\mathcal D_{d}\psi{}_{i}\big)\\
&+\frac{151i}{1152}\widehat H{}^{b}{}^{c}\overline{\widehat R(Q){}^{a}{}_{b}{}^{i}}\gamma{}_{c}{}^{d}\big(\mathcal D_{d}\psi{}_{i}\big)\\
&+\frac{2341}{2304}g\widehat G{}_{b}{}_{c}\overline{\widehat R(Q){}^{a}{}^{b}{}^{i}}\gamma{}^{c}\varphi_c{}_{i}\\
&-\frac{241}{1152}g\widehat H{}^{b}{}^{c}\overline{\widehat R(Q){}^{a}{}_{b}{}^{i}}\gamma{}_{c}\varphi_c{}_{i}\\
&-\frac{197i}{768}\epsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{f}\overline{\big(\mathcal D^{b}\widehat R(Q){}^{c}{}^{d}{}^{i}\big)}\gamma{}^{e}{}^{f}\big(\mathcal D_{e}\psi{}_{i}\big)\\
&+\frac{49i}{192}\epsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\big(\mathcal D^{b}\widehat R(Q){}^{c}{}^{d}{}^{i}\big)}\big(\mathcal D^{e}\psi{}_{i}\big)\\
&+\frac{67}{256}g\epsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\big(\mathcal D^{b}\widehat R(Q){}^{c}{}^{d}{}^{i}\big)}\gamma{}^{e}\varphi_c{}_{i}\\
&+\frac{209i}{768}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\big(\mathcal D^{b}\widehat R(Q){}^{a}{}^{c}{}^{i}\big)}\gamma{}^{d}{}^{e}\big(\mathcal D^{f}\psi{}_{i}\big)\\
&+\frac{167}{384}\overline{\big(\mathcal D^{b}\widehat R(Q){}^{a}{}^{c}{}^{i}\big)}\gamma{}_{b}\big(\mathcal D_{c}\psi{}_{i}\big)\\
&+\frac{221i}{128}g\overline{\big(\mathcal D^{b}\widehat R(Q){}^{a}{}_{b}{}^{i}\big)}\varphi_c{}_{i}\\
&-\frac{217i}{768}\epsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\big(\mathcal D^{b}\widehat R(Q){}_{b}{}^{c}{}^{i}\big)}\gamma{}^{d}{}^{e}\big(\mathcal D^{f}\psi{}_{i}\big)\\
&-\frac{283}{768}\overline{\big(\mathcal D^{b}\widehat R(Q){}_{b}{}^{c}{}^{i}\big)}\gamma{}^{a}\big(\mathcal D_{c}\psi{}_{i}\big)\\
&-\frac{173}{256}\overline{\big(\mathcal D^{b}\widehat R(Q){}^{a}{}_{b}{}^{i}\big)}\gamma{}^{c}\big(\mathcal D_{c}\psi{}_{i}\big)\\
&+\frac{257i}{1536}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\big(\mathcal D^{a}\widehat R(Q){}^{b}{}^{c}{}^{i}\big)}\gamma{}^{d}{}^{e}\big(\mathcal D^{f}\psi{}_{i}\big)\\
&-\frac{1}{2}\epsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\big(\mathcal D^{c}\psi{}^{i}\big)}\gamma{}^{b}\big(\mathcal D^{d}\mathcal D^{e}\psi{}_{i}\big)\\
&-\frac{3i}{2}\overline{\big(\mathcal D_{b}\psi{}^{i}\big)}\gamma{}^{b}{}^{c}\big(\mathcal D_{c}\mathcal D^{a}\psi{}_{i}\big)\\
&+\frac{i}{2}\overline{\big(\mathcal D^{c}\psi{}^{i}\big)}\gamma{}^{a}{}^{b}\big(\mathcal D_{b}\mathcal D_{c}\psi{}_{i}\big)\\
&-\frac{i}{6}\overline{\big(\mathcal D_{b}\psi{}^{i}\big)}\gamma{}^{a}{}^{b}\big(\Box^c \psi{}_{i}\big)
\end{aligned}
```

```math
\begin{aligned}
&-\frac{5i}{2}\overline{\big(\mathcal D^{b}\psi{}^{i}\big)}\big(\mathcal D_{b}\mathcal D^{a}\psi{}_{i}\big)\\
&+\frac{i}{2}\overline{\big(\mathcal D^{a}\psi{}^{i}\big)}\gamma{}^{b}{}^{c}\big(\mathcal D_{b}\mathcal D_{c}\psi{}_{i}\big)\\
&+\frac{7i}{6}\overline{\big(\mathcal D^{a}\psi{}^{i}\big)}\big(\Box^c \psi{}_{i}\big)\\
&-\frac{7i}{6}\widehat H{}^{b}{}^{c}\epsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\big(\mathcal D^{d}\psi{}^{i}\big)}\big(\mathcal D^{e}\psi{}_{i}\big)\\
&-\frac{25i}{48}\widehat H{}^{b}{}^{c}\epsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\big(\mathcal D_{b}\psi{}^{i}\big)}\gamma{}^{d}{}^{e}\big(\mathcal D^{f}\psi{}_{i}\big)\\
&-\frac{11}{6}\widehat H{}^{a}{}^{b}\overline{\big(\mathcal D_{b}\psi{}^{i}\big)}\gamma{}^{c}\big(\mathcal D_{c}\psi{}_{i}\big)\\
&-\frac{1}{6}\widehat H{}^{b}{}^{c}\overline{\big(\mathcal D_{b}\psi{}^{i}\big)}\gamma{}^{a}\big(\mathcal D_{c}\psi{}_{i}\big)\\
&-\frac{23i}{32}\widehat H{}^{b}{}^{c}\epsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\big(\mathcal D^{f}\psi{}^{i}\big)}\gamma{}^{d}{}^{e}\big(\mathcal D_{f}\psi{}_{i}\big)\\
&+\frac{23i}{32}\widehat H{}^{b}{}^{c}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\big(\mathcal D^{a}\psi{}^{i}\big)}\gamma{}^{d}{}^{e}\big(\mathcal D^{f}\psi{}_{i}\big)\\
&-\frac{4}{3}\widehat H{}^{b}{}^{c}\overline{\big(\mathcal D^{a}\psi{}^{i}\big)}\gamma{}_{b}\big(\mathcal D_{c}\psi{}_{i}\big)\\
&-\frac{i}{12}gL_c{}^{i}{}^{j}\epsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\big(\mathcal D^{d}\psi{}_{i}\big)}\gamma{}^{b}{}^{c}\big(\mathcal D^{e}\psi{}_{j}\big)\\
&-\frac{1}{3}gL_c{}^{i}{}^{j}\overline{\big(\mathcal D^{b}\psi{}_{i}\big)}\gamma{}^{a}\big(\mathcal D_{b}\psi{}_{j}\big)\\
&+\frac{1}{3}gL_c{}^{i}{}^{j}\overline{\big(\mathcal D^{a}\psi{}_{i}\big)}\gamma{}^{b}\big(\mathcal D_{b}\psi{}_{j}\big)\\
&-\frac{i}{12}g\epsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\big(\mathcal D^{b}\varphi_c{}^{i}\big)}\gamma{}^{c}{}^{d}\big(\mathcal D^{e}\psi{}_{i}\big)\\
&-\frac{1}{6}g\overline{\big(\mathcal D^{b}\varphi_c{}^{i}\big)}\gamma{}_{b}\big(\mathcal D^{a}\psi{}_{i}\big)\\
&+\frac{7}{6}g\overline{\big(\mathcal D^{b}\varphi_c{}^{i}\big)}\gamma{}^{a}\big(\mathcal D_{b}\psi{}_{i}\big)\\
&+\frac{i}{4}g\epsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\varphi_c{}^{i}}\gamma{}^{b}{}^{c}\big(\mathcal D^{d}\mathcal D^{e}\psi{}_{i}\big)\\
&-\frac{1}{2}g\overline{\varphi_c{}^{i}}\gamma{}^{b}\big(\mathcal D_{b}\mathcal D^{a}\psi{}_{i}\big)\\
&+\frac{1}{6}g\overline{\varphi_c{}^{i}}\gamma{}^{a}\big(\Box^c \psi{}_{i}\big)\\
&-\frac{23}{12}g\widehat H{}^{b}{}^{c}\epsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\varphi_c{}^{i}}\gamma{}^{d}\big(\mathcal D^{e}\psi{}_{i}\big)\\
&-\frac{5i}{6}g\widehat H{}^{a}{}^{b}\overline{\varphi_c{}^{i}}\gamma{}_{b}{}^{c}\big(\mathcal D_{c}\psi{}_{i}\big)\\
&+\frac{5i}{6}g\widehat H{}^{b}{}^{c}\overline{\varphi_c{}^{i}}\gamma{}^{a}{}_{b}\big(\mathcal D_{c}\psi{}_{i}\big)\\
&+\frac{i}{2}g\widehat H{}^{a}{}^{b}\overline{\varphi_c{}^{i}}\big(\mathcal D_{b}\psi{}_{i}\big)\\
&+\frac{11i}{12}g^{2}L_c{}^{i}{}^{j}\overline{\varphi_c{}_{i}}\gamma{}^{a}{}^{b}\big(\mathcal D_{b}\psi{}_{j}\big)
\end{aligned}
```

```math
\begin{aligned}
&+\frac{5i}{6}g^{2}\overline{\varphi_c{}^{i}}\gamma{}^{a}{}_{b}\big(\mathcal D^{b}\varphi_c{}_{i}\big)\\
&+\frac{5i}{48}\widehat G{}^{d}{}^{e}\epsilon{}^{a}{}_{b}{}_{c}{}_{e}{}_{f}\overline{\big(\mathcal D_{d}\psi{}^{i}\big)}\gamma{}^{b}{}^{c}\big(\mathcal D^{f}\psi{}_{i}\big)\\
&+\frac{7i}{48}\widehat G{}^{d}{}^{e}\epsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\big(\mathcal D_{b}\psi{}^{i}\big)}\gamma{}^{b}{}^{c}\big(\mathcal D^{f}\psi{}_{i}\big)\\
&-\frac{29i}{48}\widehat H{}^{b}{}^{c}\epsilon{}^{a}{}_{b}{}_{c}{}_{e}{}_{f}\overline{\big(\mathcal D_{d}\psi{}^{i}\big)}\gamma{}^{d}{}^{e}\big(\mathcal D^{f}\psi{}_{i}\big)\\
&+\frac{5i}{96}\widehat G{}^{d}{}^{e}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\big(\mathcal D^{a}\psi{}^{i}\big)}\gamma{}^{b}{}^{c}\big(\mathcal D^{f}\psi{}_{i}\big)\\
&-\frac{65}{256}\widehat G{}_{c}{}_{d}\overline{\widehat R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{a}\widehat R(Q){}_{b}{}^{d}{}_{i}\\
&-\frac{65}{64}\widehat H{}^{b}{}^{c}\overline{\widehat R(Q){}_{b}{}^{d}{}^{i}}\gamma{}^{a}\widehat R(Q){}_{c}{}_{d}{}_{i}\\
&-\frac{11i}{512}\widehat G{}_{b}{}^{g}\epsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g}\overline{\widehat R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{a}{}^{f}\widehat R(Q){}^{d}{}^{e}{}_{i}\\
&-\frac{11i}{128}\widehat H{}^{b}{}^{c}\epsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g}\overline{\widehat R(Q){}_{b}{}^{d}{}^{i}}\gamma{}^{a}{}^{g}\widehat R(Q){}^{e}{}^{f}{}_{i}\\
&-\frac{13i}{256}\widehat G{}_{b}{}^{f}\epsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\widehat R(Q){}^{b}{}^{c}{}^{i}}\widehat R(Q){}^{d}{}^{e}{}_{i}\\
&+\frac{13i}{64}\widehat H{}^{b}{}^{c}\epsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\widehat R(Q){}_{b}{}^{d}{}^{i}}\widehat R(Q){}^{e}{}^{f}{}_{i}\\
&-\frac{35i}{2048}\widehat G{}_{b}{}_{c}\epsilon{}^{a}{}_{d}{}_{e}{}_{f}{}_{g}\overline{\widehat R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{f}{}^{g}\widehat R(Q){}^{d}{}^{e}{}_{i}\\
&-\frac{35i}{512}\widehat H{}^{b}{}^{c}\epsilon{}^{a}{}_{d}{}_{e}{}_{f}{}_{g}\overline{\widehat R(Q){}_{b}{}_{c}{}^{i}}\gamma{}^{f}{}^{g}\widehat R(Q){}^{d}{}^{e}{}_{i}\\
&+\frac{7i}{512}\widehat G{}^{e}{}^{f}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\widehat R(Q){}^{a}{}^{b}{}^{i}}\widehat R(Q){}^{c}{}^{d}{}_{i}\\
&+\frac{7i}{128}\widehat H{}^{b}{}^{c}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\widehat R(Q){}^{a}{}^{d}{}^{i}}\widehat R(Q){}^{e}{}^{f}{}_{i}\\
&-\frac{23i}{512}\widehat G{}^{e}{}^{f}\epsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\widehat R(Q){}^{b}{}^{c}{}^{i}}\widehat R(Q){}_{b}{}^{d}{}_{i}\\
&-\frac{23i}{128}\widehat H{}^{b}{}^{c}\epsilon{}^{a}{}_{b}{}_{c}{}_{e}{}_{f}\overline{\widehat R(Q){}^{d}{}^{e}{}^{i}}\widehat R(Q){}_{d}{}^{f}{}_{i}\\
&-\frac{5i}{96}\widehat G{}^{d}{}^{e}\epsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\big(\mathcal D^{f}\psi{}^{i}\big)}\gamma{}^{b}{}^{c}\big(\mathcal D_{f}\psi{}_{i}\big)\\
&+\frac{19i}{1024}\widehat G{}_{b}{}^{g}\epsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g}\overline{\widehat R(Q){}^{a}{}^{b}{}^{i}}\gamma{}^{e}{}^{f}\widehat R(Q){}^{c}{}^{d}{}_{i}\\
&+\frac{19i}{256}\widehat H{}^{b}{}^{c}\epsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g}\overline{\widehat R(Q){}^{a}{}_{b}{}^{i}}\gamma{}^{f}{}^{g}\widehat R(Q){}^{d}{}^{e}{}_{i}\\
&-\frac{3i}{128}\widehat G{}_{c}{}^{g}\epsilon{}^{a}{}_{d}{}_{e}{}_{f}{}_{g}\overline{\widehat R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{e}{}^{f}\widehat R(Q){}_{b}{}^{d}{}_{i}\\
&-\frac{3i}{32}\widehat H{}^{b}{}^{c}\epsilon{}^{a}{}_{c}{}_{e}{}_{f}{}_{g}\overline{\widehat R(Q){}_{b}{}^{d}{}^{i}}\gamma{}^{f}{}^{g}\widehat R(Q){}_{d}{}^{e}{}_{i}\\
&-\frac{7i}{1024}\widehat G{}^{a}{}_{b}\epsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g}\overline{\widehat R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{f}{}^{g}\widehat R(Q){}^{d}{}^{e}{}_{i}\\
&-\frac{7i}{256}\widehat H{}^{a}{}^{b}\epsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g}\overline{\widehat R(Q){}_{b}{}^{c}{}^{i}}\gamma{}^{f}{}^{g}\widehat R(Q){}^{d}{}^{e}{}_{i}
\end{aligned}
```

```math
\begin{aligned}
&+\frac{i}{256}\widehat G{}_{b}{}_{d}\epsilon{}^{a}{}_{c}{}_{e}{}_{f}{}_{g}\overline{\widehat R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{f}{}^{g}\widehat R(Q){}^{d}{}^{e}{}_{i}\\
&+\frac{i}{64}\widehat H{}^{b}{}^{c}\epsilon{}^{a}{}_{d}{}_{e}{}_{f}{}_{g}\overline{\widehat R(Q){}_{b}{}^{d}{}^{i}}\gamma{}^{f}{}^{g}\widehat R(Q){}_{c}{}^{e}{}_{i}\\
&+\frac{i}{128}\widehat G{}^{f}{}^{g}\epsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g}\overline{\widehat R(Q){}^{a}{}^{b}{}^{i}}\gamma{}^{d}{}^{e}\widehat R(Q){}_{b}{}^{c}{}_{i}\\
&+\frac{i}{32}\widehat H{}^{b}{}^{c}\epsilon{}_{b}{}_{c}{}_{e}{}_{f}{}_{g}\overline{\widehat R(Q){}^{a}{}^{d}{}^{i}}\gamma{}^{f}{}^{g}\widehat R(Q){}_{d}{}^{e}{}_{i}\\
&-\frac{3}{32}\widehat G{}_{c}{}_{d}\overline{\widehat R(Q){}^{a}{}^{b}{}^{i}}\gamma{}^{d}\widehat R(Q){}_{b}{}^{c}{}_{i}\\
&+\frac{3}{8}\widehat H{}^{b}{}^{c}\overline{\widehat R(Q){}^{a}{}^{d}{}^{i}}\gamma{}_{c}\widehat R(Q){}_{b}{}_{d}{}_{i}\\
&+\frac{5i}{1024}\widehat G{}^{f}{}^{g}\epsilon{}^{a}{}_{d}{}_{e}{}_{f}{}_{g}\overline{\widehat R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{d}{}^{e}\widehat R(Q){}_{b}{}_{c}{}_{i}\\
&+\frac{5i}{256}\widehat H{}^{b}{}^{c}\epsilon{}^{a}{}_{b}{}_{c}{}_{f}{}_{g}\overline{\widehat R(Q){}^{d}{}^{e}{}^{i}}\gamma{}^{f}{}^{g}\widehat R(Q){}_{d}{}_{e}{}_{i}\\
&-\frac{i}{512}\widehat G{}_{b}{}_{f}\epsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{g}\overline{\widehat R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{f}{}^{g}\widehat R(Q){}^{d}{}^{e}{}_{i}\\
&-\frac{i}{128}\widehat H{}^{b}{}^{c}\epsilon{}^{a}{}_{d}{}_{e}{}_{f}{}_{g}\overline{\widehat R(Q){}_{b}{}^{d}{}^{i}}\gamma{}_{c}{}^{g}\widehat R(Q){}^{e}{}^{f}{}_{i}\\
&+\frac{i}{1024}\widehat G{}^{a}{}_{f}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{g}\overline{\widehat R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{f}{}^{g}\widehat R(Q){}^{d}{}^{e}{}_{i}\\
&+\frac{i}{256}\widehat H{}^{a}{}^{b}\epsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g}\overline{\widehat R(Q){}^{c}{}^{d}{}^{i}}\gamma{}_{b}{}^{g}\widehat R(Q){}^{e}{}^{f}{}_{i}\\
&-\frac{7i}{1024}\widehat G{}_{f}{}^{g}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{g}\overline{\widehat R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{a}{}^{f}\widehat R(Q){}^{d}{}^{e}{}_{i}\\
&-\frac{7i}{256}\widehat H{}^{b}{}^{c}\epsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g}\overline{\widehat R(Q){}^{d}{}^{e}{}^{i}}\gamma{}^{a}{}_{b}\widehat R(Q){}^{f}{}^{g}{}_{i}\\
&+\frac{i}{2048}\widehat G{}_{f}{}_{g}\epsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\widehat R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{f}{}^{g}\widehat R(Q){}^{d}{}^{e}{}_{i}\\
&+\frac{i}{512}\widehat H{}^{b}{}^{c}\epsilon{}^{a}{}_{d}{}_{e}{}_{f}{}_{g}\overline{\widehat R(Q){}^{d}{}^{e}{}^{i}}\gamma{}_{b}{}_{c}\widehat R(Q){}^{f}{}^{g}{}_{i}\\
&-\frac{3i}{512}\widehat G{}_{e}{}^{g}\epsilon{}_{b}{}_{c}{}_{d}{}_{f}{}_{g}\overline{\widehat R(Q){}^{a}{}^{b}{}^{i}}\gamma{}^{e}{}^{f}\widehat R(Q){}^{c}{}^{d}{}_{i}\\
&-\frac{3i}{128}\widehat H{}^{b}{}^{c}\epsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g}\overline{\widehat R(Q){}^{a}{}^{d}{}^{i}}\gamma{}_{b}{}^{g}\widehat R(Q){}^{e}{}^{f}{}_{i}\\
&+\frac{3}{4}\widehat G{}^{a}{}^{c}\overline{\big(\mathcal D_{b}\psi{}^{i}\big)}\gamma{}^{b}\big(\mathcal D_{c}\psi{}_{i}\big)\\
&-\frac{11i}{6}g\widehat G{}^{a}{}^{b}\overline{\varphi_c{}^{i}}\big(\mathcal D_{b}\psi{}_{i}\big)\\
&-\frac{433}{4608}\widehat G{}^{e}{}^{f}\epsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{f}\overline{\widehat R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{d}\big(\mathcal D_{e}\psi{}_{i}\big)\\
&-\frac{83}{384}\widehat G{}_{d}{}^{e}\epsilon{}^{a}{}_{b}{}_{c}{}_{e}{}_{f}\overline{\widehat R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{d}\big(\mathcal D^{f}\psi{}_{i}\big)\\
&+\frac{503}{2304}\widehat H{}^{b}{}^{c}\epsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\widehat R(Q){}^{d}{}^{e}{}^{i}}\gamma{}^{f}\big(\mathcal D_{b}\psi{}_{i}\big)\\
&+\frac{5}{192}\widehat H{}^{b}{}^{c}\epsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\widehat R(Q){}^{d}{}^{e}{}^{i}}\gamma{}_{b}\big(\mathcal D^{f}\psi{}_{i}\big)
\end{aligned}
```

```math
\begin{aligned}
&-\frac{461i}{2048}g\widehat G{}_{d}{}^{f}\epsilon{}^{a}{}_{b}{}_{c}{}_{e}{}_{f}\overline{\widehat R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{d}{}^{e}\varphi_c{}_{i}\\
&-\frac{77i}{1024}g\widehat H{}^{b}{}^{c}\epsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\widehat R(Q){}^{d}{}^{e}{}^{i}}\gamma{}_{b}{}^{f}\varphi_c{}_{i}\\
&+\frac{1}{24}\widehat G{}^{e}{}^{f}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\widehat R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{d}\big(\mathcal D^{a}\psi{}_{i}\big)\\
&+\frac{107}{9216}\widehat G{}^{d}{}^{e}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\widehat R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{a}\big(\mathcal D^{f}\psi{}_{i}\big)\\
&-\frac{49}{192}\widehat H{}^{b}{}^{c}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\widehat R(Q){}^{d}{}^{e}{}^{i}}\gamma{}^{f}\big(\mathcal D^{a}\psi{}_{i}\big)\\
&+\frac{469}{4608}\widehat H{}^{b}{}^{c}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\widehat R(Q){}^{d}{}^{e}{}^{i}}\gamma{}^{a}\big(\mathcal D^{f}\psi{}_{i}\big)\\
&+\frac{5i}{256}g\widehat G{}^{e}{}^{f}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\widehat R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{a}{}^{d}\varphi_c{}_{i}\\
&-\frac{27i}{128}g\widehat H{}^{b}{}^{c}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\widehat R(Q){}^{d}{}^{e}{}^{i}}\gamma{}^{a}{}^{f}\varphi_c{}_{i}\\
&+\frac{4i}{3}\overline{\big(\mathcal D_{b}\psi{}^{i}\big)}\gamma{}^{b}{}^{c}\big(\mathcal D^{a}\mathcal D_{c}\psi{}_{i}\big)\\
&+\frac{4i}{3}\overline{\big(\mathcal D^{b}\psi{}^{i}\big)}\big(\mathcal D^{a}\mathcal D_{b}\psi{}_{i}\big)\\
&-g\overline{\big(\mathcal D^{a}\varphi_c{}^{i}\big)}\gamma{}^{b}\big(\mathcal D_{b}\psi{}_{i}\big)\\
&+\frac{i}{4}\widehat G{}^{b}{}^{c}\epsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\big(\mathcal D^{d}\psi{}^{i}\big)}\big(\mathcal D^{e}\psi{}_{i}\big)\\
&+\frac{1}{4}g\widehat G{}^{c}{}^{d}\epsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\varphi_c{}^{i}}\gamma{}^{b}\big(\mathcal D^{e}\psi{}_{i}\big)\\
&+\frac{211i}{144}gL_c{}^{i}{}^{j}\overline{\widehat R(Q){}^{a}{}^{b}{}_{i}}\big(\mathcal D_{b}\psi{}_{j}\big)\\
&+\frac{103}{288}gL_c{}^{i}{}^{j}\epsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\widehat R(Q){}^{b}{}^{c}{}_{i}}\gamma{}^{d}\big(\mathcal D^{e}\psi{}_{j}\big)\\
&-\frac{499i}{2304}g^{2}L_c{}^{i}{}^{j}\epsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\widehat R(Q){}^{b}{}^{c}{}_{i}}\gamma{}^{d}{}^{e}\varphi_c{}_{j}\\
&+\frac{259}{4608}\widehat G{}^{e}{}^{f}\epsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\widehat R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{d}\big(\mathcal D_{b}\psi{}_{i}\big)\\
&+\frac{533}{2304}\widehat H{}^{b}{}^{c}\epsilon{}^{a}{}_{b}{}_{c}{}_{e}{}_{f}\overline{\widehat R(Q){}^{d}{}^{e}{}^{i}}\gamma{}^{f}\big(\mathcal D_{d}\psi{}_{i}\big)\\
&-\frac{437i}{1536}\epsilon{}^{a}{}_{b}{}_{d}{}_{e}{}_{f}\overline{\big(\mathcal D^{b}\widehat R(Q){}^{c}{}^{d}{}^{i}\big)}\gamma{}^{e}{}^{f}\big(\mathcal D_{c}\psi{}_{i}\big)\\
&-\frac{39i}{1024}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\big(\mathcal D^{b}\widehat R(Q){}^{c}{}^{d}{}^{i}\big)}\gamma{}^{e}{}^{f}\big(\mathcal D^{a}\psi{}_{i}\big)\\
&+\frac{95i}{768}\epsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\big(\mathcal D^{b}\widehat R(Q){}^{c}{}^{d}{}^{i}\big)}\gamma{}^{e}{}^{f}\big(\mathcal D_{b}\psi{}_{i}\big)\\
&+\frac{13i}{128}\epsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\widehat R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{d}{}^{e}\big(\Box^c \psi{}_{i}\big)\\
&+\frac{35i}{1536}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\big(\mathcal D^{b}\widehat R(Q){}^{c}{}^{d}{}^{i}\big)}\gamma{}^{a}{}^{e}\big(\mathcal D^{f}\psi{}_{i}\big)\\
&+\frac{i}{16}\epsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\widehat R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{d}{}^{e}\big(\mathcal D^{f}\mathcal D_{b}\psi{}_{i}\big)
\end{aligned}
```

```math
\begin{aligned}
&-\frac{i}{32}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\widehat R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{a}{}^{d}\big(\mathcal D^{e}\mathcal D^{f}\psi{}_{i}\big)\\
&+\frac{1}{3}g\overline{\varphi_c{}^{i}}\gamma{}^{b}\big(\mathcal D^{a}\mathcal D_{b}\psi{}_{i}\big)\\
&-\frac{i}{32}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\widehat R(Q){}^{a}{}^{b}{}^{i}}\gamma{}^{c}{}^{d}\big(\mathcal D^{e}\mathcal D^{f}\psi{}_{i}\big)\\
&-\frac{i}{64}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\widehat R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{d}{}^{e}\big(\mathcal D^{f}\mathcal D^{a}\psi{}_{i}\big)\\
&-\frac{i}{64}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\widehat R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{d}{}^{e}\big(\mathcal D^{a}\mathcal D^{f}\psi{}_{i}\big)\\
&+\frac{i}{16}\epsilon{}^{a}{}_{b}{}_{c}{}_{e}{}_{f}\overline{\widehat R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{d}{}^{e}\big(\mathcal D^{f}\mathcal D_{d}\psi{}_{i}\big)\\
&+\frac{3}{32}g\epsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\widehat R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{e}\big(\mathcal D^{d}\varphi_c{}_{i}\big)\\
&+\frac{13i}{16}g\overline{\widehat R(Q){}^{a}{}^{b}{}^{i}}\big(\mathcal D_{b}\varphi_c{}_{i}\big)\\
&+\frac{23i}{3072}gL_c{}^{i}{}^{j}\epsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\widehat R(Q){}^{b}{}^{c}{}_{i}}\gamma{}^{e}{}^{f}\widehat R(Q){}_{b}{}^{d}{}_{j}\\
&-\frac{17}{1024}gL_c{}^{i}{}^{j}\overline{\widehat R(Q){}^{b}{}^{c}{}_{i}}\gamma{}^{a}\widehat R(Q){}_{b}{}_{c}{}_{j}\\
&-\frac{5i}{6144}gL_c{}^{i}{}^{j}\epsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\widehat R(Q){}^{b}{}^{c}{}_{i}}\widehat R(Q){}^{d}{}^{e}{}_{j}\\
&-\frac{i}{192}gL_c{}^{i}{}^{j}\epsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\widehat R(Q){}^{a}{}^{b}{}_{i}}\gamma{}^{e}{}^{f}\widehat R(Q){}^{c}{}^{d}{}_{j}\\
&-\frac{1}{4}\widehat G{}^{b}{}^{c}\overline{\big(\mathcal D_{b}\psi{}^{i}\big)}\gamma{}^{a}\big(\mathcal D_{c}\psi{}_{i}\big)
\end{aligned}
```


## Density insertion

The JSON output applies these seven operators term by term, including each
coefficient and the external-fermion degree. It keeps the contractions explicit;
it does not claim a further primitive-field expansion of the supercovariants.

```math
\begin{aligned}
e^{-1}\mathcal L_{\log}=\big[&
N_{\log}-\frac g2L_c^{ij}L_{\log ij}+C_aE_{\log}^a
+\frac12\bar\psi_a\gamma^a\varphi_{\log}
+\frac i2C_a\bar\psi_b\gamma^{ba}\varphi_{\log}\\
&+\frac i4\bar\psi_a^i\gamma^{ab}\psi_b^jL_{\log ij}
+\frac14C_a\bar\psi_b^i\gamma^{abc}\psi_c^jL_{\log ij}
\big]_{\le2}.
\end{aligned}
```

Source: S23 (3.2), (3.27), project SC7-50–52. Implicit fermions in covariants
are retained with the same degree prescription as the accepted source.
