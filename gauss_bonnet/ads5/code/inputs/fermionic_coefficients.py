"""Editable FC13/FC14 coefficients in the fixed, ordered six-bilinear basis.

FC13 follows the full source and descendant expansion, checked independently
by calculations.fermion_operator. These inputs are not a nonlinear CAS action.
The complete monomials and their delta/NW-SE pairings are in FC13-FC15.
"""

import sympy as sp
from inputs.symbols import g, x


def two_derivative_terms():
    return {
        "gravitino_kinetic": -x,
        "spinor_kinetic": 2 / x,
        "derivative_mixing_delta": -2 * sp.sqrt(2) * sp.I,
        "gravitino_mass_delta": -sp.I * g * x * (x + 2) / (2 * sp.sqrt(2)),
        "algebraic_mixing": -2 * g * (x + 1),
        "spinor_mass_delta": 7 * sp.I * g / sp.sqrt(2),
    }


def gauss_bonnet_terms():
    return {
        "gravitino_kinetic": -g**2 * x**2,
        "spinor_kinetic": 2 * g**2,
        "derivative_mixing_delta": -2 * sp.sqrt(2) * sp.I * g**2 * x,
        "gravitino_mass_delta": -sp.I * g**3 * x**3 / sp.sqrt(2),
        "algebraic_mixing": -3 * g**3 * x**2,
        "spinor_mass_delta": 7 * sp.I * g**3 * x / sp.sqrt(2),
    }
