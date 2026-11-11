"""Exact Clifford and covariant-derivative calculation of the GB fermion operator.

Fixed component frame: k=-1, g=1, x=sqrt(2), m=1/2, u=3.
The rescaling back to general g,x is proved in FERMIONIC_CALCULATIONS FC10-FC13.
All matrices use object entries (exact SymPy numbers), never floating tolerance.
The linear Majorana bar uses transpose, not conjugate transpose.
"""
import itertools
import numpy as np
import sympy as sp
I = sp.I
metric_signs = np.array([-1, 1, 1, 1, 1])
identity_spinor = np.eye(4, dtype=object)
identity_doublet = np.eye(2, dtype=object)
pauli_one = np.array([[0, 1], [1, 0]], object)
pauli_two = np.array([[0, -I], [I, 0]])
pauli_three = np.diag([1, -1])
spinor_gamma = [-I * np.kron(pauli_three, identity_doublet), np.kron(pauli_one, pauli_one), np.kron(pauli_one, pauli_two), np.kron(pauli_one, pauli_three), np.kron(pauli_two, identity_doublet)]
gamma_up = [np.kron(identity_doublet, gamma_matrix) for gamma_matrix in spinor_gamma]
gamma_down = [metric_signs[a] * gamma_up[a] for a in range(5)]
charge_conjugation = spinor_gamma[2] @ spinor_gamma[4]
doublet_generator = np.kron(np.array([[0, -1], [1, 0]]), identity_spinor)
delta_pairing = np.kron(identity_doublet, charge_conjugation)
contracted_pairing = np.kron(np.array([[0, -1], [1, 0]]), charge_conjugation)

def gamma_two(a, b):
    """Antisymmetrized gamma^{ab}, with weight 1/2."""
    return sp.Integer(1) * (gamma_up[a] @ gamma_up[b] - gamma_up[b] @ gamma_up[a]) / 2

def gamma_three(a, b, c):
    """Antisymmetrized gamma^{abc}; distinct Clifford generators anticommute."""
    if len({a, b, c}) < 3:
        return np.zeros((8, 8), object)
    return gamma_up[a] @ gamma_up[b] @ gamma_up[c]
FIELD_COMPONENTS = 48
field_selectors = []
for a in range(6):
    v = np.zeros((8, FIELD_COMPONENTS), object)
    v[:, 8 * a:8 * a + 8] = np.eye(8, dtype=object)
    field_selectors.append(v)
m = sp.Rational(1, 2)
u = 3
tangent_connection = np.zeros((5, 5, 5), dtype=object)
spin_connection = []
for a in range(5):
    spin_connection.append(np.zeros((8, 8), object))
    if a < 4:
        tangent_connection[a, a, 4] = -metric_signs[a]
        tangent_connection[a, 4, a] = 1
        spin_connection[a] = -sp.Rational(1, 2) * metric_signs[a] * gamma_up[a] @ gamma_up[4]

def spinor_derivative(exponent, a, spinor):
    """FC10: covariant derivative on a homogeneous radial spinor jet z^s."""
    return exponent * spinor if a == 4 else spin_connection[a] @ spinor

def vector_spinor_derivative(exponent, a, b, spinor):
    """FC10: also differentiate the lower tangent index b."""
    connection_term = sum(
        tangent_connection[a, b, d] * spinor[d] for d in range(5)
    )
    return spinor_derivative(exponent, a, spinor[b]) + connection_term


def twoform_spinor_derivative(exponent, a, b, c, spinor):
    """Differentiate both lower tangent indices of the Q curvature."""
    connection_terms = sum(
        tangent_connection[a, b, d] * spinor[d, c]
        + tangent_connection[a, c, d] * spinor[b, d]
        for d in range(5)
    )
    return spinor_derivative(exponent, a, spinor[b, c]) + connection_terms


def linear_descendants(exponent):
    """FC1-FC2 and SF1-SF5, with all 48 fermion components arbitrary.

    Gravitino and spinor are rectangular selectors, not gauge-fixed modes.
    The gauge-fixed dilatino vanishes, but its covariant derivatives survive.
    """
    gravitino = field_selectors[:5]
    spinor = field_selectors[5]
    index_pairs = list(itertools.product(range(5), repeat=2))

    raw_Q_curvature = {
        (a, b): vector_spinor_derivative(exponent, a, b, gravitino)
        - vector_spinor_derivative(exponent, b, a, gravitino)
        for a, b in index_pairs
    }
    curvature_gamma_trace = sum(
        gamma_two(a, b) @ raw_Q_curvature[a, b] for a, b in index_pairs
    )
    S_connection = [
        I / 3 * sum(gamma_up[b] @ raw_Q_curvature[a, b] for b in range(5))
        - I / 24 * gamma_down[a] @ curvature_gamma_trace
        for a in range(5)
    ]
    dilatino_gradient = [
        -m * doublet_generator @ gravitino[a] - S_connection[a]
        for a in range(5)
    ]
    Q_curvature = {
        (a, b): raw_Q_curvature[a, b]
        - I * (gamma_down[a] @ S_connection[b] - gamma_down[b] @ S_connection[a])
        for a, b in index_pairs
    }
    Weyl_spinor = (
        I / 8 * sum(gamma_up[a] @ dilatino_gradient[a] for a in range(5))
        + sp.Rational(1, 8) * spinor
    )
    compensator_gradient = [
        spinor_derivative(exponent, a, spinor)
        + u * doublet_generator @ dilatino_gradient[a]
        for a in range(5)
    ]
    dilatino_hessian = {
        (a, b): vector_spinor_derivative(exponent, a, b, dilatino_gradient)
        + I * m * gamma_down[b] @ doublet_generator @ dilatino_gradient[a]
        for a, b in index_pairs
    }
    compensator_hessian = {
        (a, b): vector_spinor_derivative(exponent, a, b, compensator_gradient)
        - I * u * m * gamma_down[b] @ dilatino_gradient[a]
        + (sp.Rational(7, 4) * metric_signs[a] * spinor if a == b else 0)
        - sp.Rational(1, 4) * metric_signs[b] * metric_signs[a]
        * gamma_two(b, a) @ spinor
        for a, b in index_pairs
    }
    return {
        "gravitino": gravitino,
        "spinor": spinor,
        "S_connection": S_connection,
        "dilatino_gradient": dilatino_gradient,
        "Q_curvature": Q_curvature,
        "Weyl_spinor": Weyl_spinor,
        "compensator_gradient": compensator_gradient,
        "dilatino_hessian": dilatino_hessian,
        "compensator_hessian": compensator_hessian,
    }


def bilinear_matrices(exponent):
    """Assemble FC3, FC8, FC9 and the two implicit FC6 groups separately.
The candidate is the independent FC13 representative. No expected matrix is read.
Left derivatives use 4-s because the AdS measure adjoint is fixed by FC11."""
    left = linear_descendants(4 - exponent)
    right = linear_descendants(exponent)
    matrix = np.zeros((FIELD_COMPONENTS, FIELD_COMPONENTS), object)
    groups = {}

    def add_bilinear(left_field, right_field, coefficient=1, gamma=None, delta=False):
        """Add an ordered bilinear; the Majorana bar is linear in its slot."""
        nonlocal matrix
        pairing = delta_pairing if delta else contracted_pairing
        insertion = np.eye(8, dtype=object) if gamma is None else gamma
        matrix += coefficient * (left_field.T @ pairing @ insertion @ right_field)

    def finish_group(name):
        nonlocal matrix
        groups[name] = matrix.copy()
        matrix[:] = 0
    # FC3: Weyl curvature and composite-spinor bilinears.
    for a, b, c in itertools.product(range(5), repeat=3):
        add_bilinear(
            left['Q_curvature'][a, b],
            twoform_spinor_derivative(exponent, c, a, b, right['Q_curvature']),
            -sp.Rational(3, 2) * metric_signs[a] * metric_signs[b],
            gamma_up[c],
        )
    for a in range(5):
        add_bilinear(
            left['Weyl_spinor'],
            spinor_derivative(exponent, a, right['Weyl_spinor']),
            sp.Integer(1) * 512 / 3,
            gamma_up[a],
        )
    for a, b in itertools.product(range(5), repeat=2):
        add_bilinear(
            left['Q_curvature'][a, b],
            right['Q_curvature'][a, b],
            sp.Integer(1) * I / 4 * metric_signs[a] * metric_signs[b],
            delta=True,
        )
    add_bilinear(
        left['Weyl_spinor'],
        right['Weyl_spinor'],
        sp.Integer(1) * (256 * I) / 3,
        delta=True,
    )
    finish_group('Weyl')

    # FC8: LOG covariant seed, terms 29-62.
    for a, b in itertools.product(range(5), repeat=2):
        add_bilinear(
            twoform_spinor_derivative(4 - exponent, a, a, b, left['Q_curvature']),
            right['dilatino_gradient'][b],
            3 * I * metric_signs[a] * metric_signs[b],
        )
    for c, a, b in itertools.product(range(5), repeat=3):
        add_bilinear(
            left['dilatino_gradient'][c],
            right['dilatino_hessian'][a, b],
            sp.Integer(1) * -2 / 3,
            gamma_three(c, a, b),
        )
    dilatino_box = sum((metric_signs[a] * right['dilatino_hessian'][a, a] for a in range(5)))
    for a in range(5):
        add_bilinear(
            left['dilatino_gradient'][a],
            dilatino_box,
            sp.Integer(1) * -10 / 3,
            gamma_up[a],
        )
    for a, b in itertools.product(range(5), repeat=2):
        add_bilinear(
            left['dilatino_gradient'][b],
            right['dilatino_hessian'][a, b],
            sp.Integer(1) * 2 / 3 * metric_signs[b],
            gamma_up[a],
        )
        add_bilinear(
            left['dilatino_gradient'][b],
            right['dilatino_hessian'][b, a],
            sp.Integer(1) * 16 / 3 * metric_signs[b],
            gamma_up[a],
        )
        add_bilinear(
            left['dilatino_gradient'][a],
            right['dilatino_gradient'][b],
            -3 * I,
            gamma_two(a, b),
            True,
        )
    for a in range(5):
        add_bilinear(
            left['dilatino_gradient'][a],
            right['dilatino_gradient'][a],
            -12 * I * metric_signs[a],
            delta=True,
        )
    for a, b in itertools.product(range(5), repeat=2):
        add_bilinear(
            left['compensator_gradient'][a],
            right['dilatino_gradient'][b],
            sp.Integer(1) * (-10 * I) / 3,
            gamma_two(a, b),
        )
        add_bilinear(
            left['spinor'],
            right['dilatino_hessian'][a, b],
            sp.Integer(1) * (-10 * I) / 3,
            gamma_two(a, b),
        )
    for a in range(5):
        add_bilinear(
            left['compensator_gradient'][a],
            right['dilatino_gradient'][a],
            sp.Integer(1) * (26 * I) / 3 * metric_signs[a],
        )
    add_bilinear(left['spinor'], dilatino_box, sp.Integer(1) * (10 * I) / 3)
    for a in range(5):
        add_bilinear(
            left['spinor'],
            right['dilatino_gradient'][a],
            sp.Integer(1) * -35 / 3,
            gamma_up[a],
            True,
        )
        add_bilinear(
            left['spinor'],
            right['compensator_gradient'][a],
            sp.Integer(1) * -2 / 3,
            gamma_up[a],
        )
    add_bilinear(left['spinor'], right['spinor'], sp.Integer(1) * (17 * I) / 3, delta=True)
    finish_group('LOG29to62')

    # FC9: explicit LOG bilinears, surviving terms 315-827.
    for a, b in itertools.product(range(5), repeat=2):
        add_bilinear(
            left['gravitino'][a],
            right['dilatino_gradient'][b],
            4 * I,
            gamma_up[a] @ gamma_up[b],
        )
    for a in range(5):
        add_bilinear(left['spinor'], right['gravitino'][a], 4, gamma_up[a])
    for a, b in itertools.product(range(5), repeat=2):
        add_bilinear(
            left['compensator_gradient'][a],
            right['gravitino'][b],
            4 * I,
            gamma_up[a] @ gamma_up[b],
            True,
        )
    for c, a, b in itertools.product(range(5), repeat=3):
        add_bilinear(
            left['gravitino'][c],
            right['dilatino_hessian'][a, b],
            -4,
            gamma_three(c, a, b),
            True,
        )
    for a, b in itertools.product(range(5), repeat=2):
        add_bilinear(
            left['gravitino'][b],
            right['dilatino_hessian'][a, b] - right['dilatino_hessian'][b, a],
            4 * metric_signs[b],
            gamma_up[a],
            True,
        )
    for a in range(5):
        add_bilinear(left['gravitino'][a], dilatino_box, -2, gamma_up[a], True)
    compensator_box_left = sum((metric_signs[a] * left['compensator_hessian'][a, a] for a in range(5)))
    for a in range(5):
        add_bilinear(compensator_box_left, right['gravitino'][a], -2, gamma_up[a])
    for a, b in itertools.product(range(5), repeat=2):
        add_bilinear(left['gravitino'][a], right['gravitino'][b], 3 * I, gamma_two(a, b), True)
    finish_group('LOG315plus')

    # FC6: implicit fermions in the sigma/L descendants.
    for a, b in itertools.product(range(5), repeat=2):
        add_bilinear(left['S_connection'][a], right['gravitino'][b], -2 * I, gamma_two(a, b))
    for a in range(5):
        add_bilinear(left['gravitino'][a], right['dilatino_gradient'][a], -2 * I * metric_signs[a])
        add_bilinear(
            left['gravitino'][a],
            right['compensator_gradient'][a],
            -2 * I * metric_signs[a],
            delta=True,
        )
        add_bilinear(left['spinor'], right['S_connection'][a], 2, gamma_up[a], True)
    finish_group('implicitSigmaL')

    # FC6: implicit fermions in the N descendant.
    for a, b in itertools.product(range(5), repeat=2):
        add_bilinear(left['S_connection'][a], right['gravitino'][b], 6 * I, gamma_two(a, b))
        add_bilinear(
            left['gravitino'][a],
            right['compensator_hessian'][a, b],
            -2 * metric_signs[a],
            gamma_up[b],
        )
    for a in range(5):
        add_bilinear(
            left['gravitino'][a],
            spinor_derivative(exponent, a, right['Weyl_spinor']),
            -16 * I * metric_signs[a],
            delta=True,
        )
        add_bilinear(
            left['S_connection'][a],
            right['compensator_gradient'][a],
            -6 * I * metric_signs[a],
        )
        add_bilinear(left['S_connection'][a], right['Weyl_spinor'], 16, gamma_up[a], True)
    for a, b in itertools.product(range(5), repeat=2):
        add_bilinear(
            left['S_connection'][a],
            right['compensator_gradient'][b],
            -2 * I,
            gamma_up[a] @ gamma_up[b],
        )
    finish_group('implicitN')
    total = sum(groups.values())

    # FC13: independently assembled collected representative.
    for a, b, c in itertools.product(range(5), repeat=3):
        add_bilinear(
            left['gravitino'][a],
            vector_spinor_derivative(exponent, b, c, right['gravitino']),
            -2,
            gamma_three(a, b, c),
        )
    for a in range(5):
        add_bilinear(
            left['spinor'],
            spinor_derivative(exponent, a, right['spinor']),
            2,
            gamma_up[a],
        )
        add_bilinear(left['gravitino'][a], right['spinor'], -6, gamma_up[a])
    for a, b in itertools.product(range(5), repeat=2):
        add_bilinear(
            left['gravitino'][a],
            spinor_derivative(exponent, b, right['spinor']),
            -4 * I,
            gamma_two(a, b),
            True,
        )
        add_bilinear(left['gravitino'][a], right['gravitino'][b], -2 * I, gamma_two(a, b), True)
    add_bilinear(left['spinor'], right['spinor'], 7 * I, delta=True)
    groups['candidate'] = matrix.copy()
    groups['total'] = total
    return groups
