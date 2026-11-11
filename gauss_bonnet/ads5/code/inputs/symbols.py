"""Common symbols; see CONVENTIONS.md for dimensions and index conventions."""

import sympy as sp

# L,N,k are free background parameters until the branch substitution is made.
L, N, k = sp.symbols("L N k", real=True)
g = sp.Symbol("g", real=True, nonzero=True)
lam = sp.Symbol("lambda_GB", real=True)
x = sp.Symbol("x", positive=True)
a = sp.Symbol("a", real=True)
c = 2 - x
m = g * x / (2 * sp.sqrt(2))


def branch_values():
    """GB-S+: 0<x<=2, g!=0; no division by c=2-x."""
    return {
        L: x,
        N: -sp.Rational(3, 2) * g * x**2,
        k: -g**2 * x**2 / 2,
        lam: 2 * (1 - x) / (g**2 * x**2),
    }


def on_branch(expression):
    return sp.factor(expression.subs(branch_values(), simultaneous=True))
