"""Small ordered-polynomial engine for the seven outer BF contractions.

It expands products and projects explicit fermion degree. It does not commute
tensor words, integrate by parts, expand supercovariant connections or do Fierz
algebra. Complete component definitions remain in the accompanying source note.
"""
from dataclasses import dataclass
from collections import defaultdict
import sympy as sp

DEGREE = {
    "trace_Y_linear": 0, "F_linear": 0, "G": 0, "E2": 0,
    "bar_lambda_varphi": 2, "psi_gamma_lambda": 2,
    "varphi_bilinear": 2, "psi_gamma_varphi": 2, "psi_gamma2_psi": 2,
}


@dataclass(frozen=True)
class Term:
    coefficient: object
    word: tuple = ()

    @property
    def degree(self):
        return sum(DEGREE[name] for name in self.word)


def multiply(left, right, maximum_degree=2):
    return [
        Term(sp.expand(a.coefficient * b.coefficient), a.word + b.word)
        for a in left for b in right
        if a.degree + b.degree <= maximum_degree
    ]


def collect(terms):
    coefficients = defaultdict(lambda: sp.S.Zero)
    for term in terms:
        coefficients[term.word] += term.coefficient
    return [Term(sp.factor(coefficient), word) for word, coefficient in coefficients.items()
            if sp.simplify(coefficient) != 0]
