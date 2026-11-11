"""Portable exact polynomial records: rational numbers, ordered fields and jets."""
import json
from .algebra import rules


def encode(polynomial):
    return [
        {
            "coefficient": [str(coefficient.r), str(coefficient.i)],
            "factors": [
                {
                    "field": atom.name,
                    "indices": list(atom.ix),
                    "derivatives": list(atom.ds),
                    "power": atom.power,
                    "odd_derivatives": list(atom.oddD),
                }
                for atom in factors
            ],
        }
        for coefficient, factors in polynomial.ts
    ]


def decode(records):
    terms = []
    for row in records:
        real, imaginary = map(rules.Q, row["coefficient"])
        factors = tuple(
            rules.A(
                atom["field"],
                tuple(atom["indices"]),
                tuple(atom["derivatives"]),
                atom["power"],
                tuple(atom["odd_derivatives"]),
            )
            for atom in row["factors"]
        )
        terms.append((rules.C(real, imaginary), factors))
    return rules.P.terms(terms)


def save(path, polynomial):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(encode(polynomial), ensure_ascii=False) + "\n")


def load(path):
    return decode(json.loads(path.read_text()))
