"""Exact coefficients and a deliberately small parser for the located FM equations.

This parser handles the documented aligned expressions. It is not a generic
LaTeX parser or a tensor-identity engine. Tensor contractions are explicit input
templates whose derivation is preserved with the package.
"""
from dataclasses import dataclass
from fractions import Fraction
import re


@dataclass(frozen=True)
class Coefficient:
    value: Fraction
    imaginary: bool = False

    def __mul__(self, other):
        sign = -1 if self.imaginary and other.imaginary else 1
        return Coefficient(sign * self.value * other.value,
                           self.imaginary != other.imaginary)

    def record(self):
        return [str(self.value), int(self.imaginary)]

    def latex(self):
        sign = "-" if self.value < 0 else "+"
        value = abs(self.value)
        numerator = str(value.numerator) if value.numerator != 1 or not self.imaginary else ""
        numerator += "i" if self.imaginary else ""
        number = numerator if value.denominator == 1 else rf"\frac{{{numerator}}}{{{value.denominator}}}"
        return sign + number


def clean(text):
    text = re.sub(r"\\hspace\{[^}]*\}", "", text)
    for token in ("\\\\", "&", r"\,", r"\!"):
        text = text.replace(token, "")
    return re.sub(r"\s+", "", text)


def equation_body(document, tag):
    preceding = document.split(r"\tag{" + tag + "}", 1)[0]
    aligned = preceding.rsplit(r"\begin{aligned}", 1)[1]
    aligned = aligned.split(r"\end{aligned}", 1)[0]
    return clean(aligned).split("=", 1)[1].removeprefix("{}").rstrip(".")


def split_sum(expression):
    terms, depth, start = [], 0, 0
    for position, character in enumerate(expression):
        depth += (character in "{[(") - (character in "}])")
        if depth < 0:
            raise ValueError("Unbalanced source expression")
        if character in "+-" and depth == 0 and position > start:
            terms.append(expression[start:position])
            start = position
    if depth != 0:
        raise ValueError("Unbalanced source expression")
    return terms + [expression[start:]]


def take_atom(text):
    if text.startswith("{"):
        end = text.index("}")
        return text[1:end], text[end + 1:]
    return text[0], text[1:]


def parse_term(text):
    sign = -1 if text.startswith("-") else 1
    body = text.lstrip("+-")
    phase = 0
    if body.startswith(r"\frac"):
        numerator, body = take_atom(body[5:])
        denominator, body = take_atom(body)
        if "i" in numerator:
            phase += 1
            numerator = numerator.replace("i", "") or "1"
        value = Fraction(numerator) / Fraction(denominator)
    else:
        match = re.match(r"\d+", body)
        value = Fraction(match[0]) if match else Fraction(1)
        if match:
            body = body[len(match[0]):]
    if body.startswith("i"):
        phase += 1
        body = body[1:]
    return Coefficient(sign * value * (-1)**(phase // 2), bool(phase % 2)), body


def equation_terms(document, tag):
    return [parse_term(term) for term in split_sum(equation_body(document, tag))]
