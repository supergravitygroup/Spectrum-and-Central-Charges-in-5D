"""Small exterior algebra and even variation jets for Appendix-B checks.

Eight phi generators and eight epsilon generators stay formal. Only the
bosonic triplet and its derivatives are sampled. No coefficient threshold
is applied inside the algebra.
"""
from dataclasses import dataclass
import numpy as np


class Exterior:
    def __init__(self, coefficients=None):
        self.terms = {m: complex(c) for m, c in (coefficients or {}).items() if c != 0}

    @staticmethod
    def scalar(value):
        return value if isinstance(value, Exterior) else Exterior({0: value})

    @staticmethod
    def generator(index):
        return Exterior({1 << index: 1})

    def __add__(self, other):
        result = dict(self.terms)
        for mask, value in self.scalar(other).terms.items():
            result[mask] = result.get(mask, 0) + value
        return Exterior(result)

    __radd__ = __add__

    def __neg__(self):
        return self * -1

    def __sub__(self, other):
        return self + -self.scalar(other)

    def __mul__(self, other):
        result = {}
        for left, x in self.terms.items():
            for right, y in self.scalar(other).terms.items():
                if left & right:
                    continue
                inversions = sum((left >> (j + 1)).bit_count()
                                 for j in range(right.bit_length()) if right & (1 << j))
                mask = left | right
                result[mask] = result.get(mask, 0) + (-1 if inversions % 2 else 1) * x * y
        return Exterior(result)

    __rmul__ = __mul__

    def size(self):
        return max((abs(x) for x in self.terms.values()), default=0.)


@dataclass
class Jet:
    """Value and variation; delta with its odd parameter included is even."""
    value: Exterior
    variation: Exterior

    @staticmethod
    def constant(value):
        return value if isinstance(value, Jet) else Jet(Exterior.scalar(value), Exterior())

    def __add__(self, other):
        other = self.constant(other)
        return Jet(self.value + other.value, self.variation + other.variation)

    __radd__ = __add__

    def __mul__(self, other):
        other = self.constant(other)
        return Jet(self.value * other.value,
                   self.variation * other.value + self.value * other.variation)

    __rmul__ = __mul__

    def __neg__(self):
        return self * -1

    def __sub__(self, other):
        return self + -self.constant(other)

    def __pow__(self, exponent):
        if set(self.value.terms) != {0}:
            raise ValueError('Only ordinary bosonic scalar powers are needed here')
        value = self.value.terms[0]
        return Jet(Exterior.scalar(value ** exponent),
                   exponent * value ** (exponent - 1) * self.variation)


def clifford():
    pauli = [np.array([[0, 1], [1, 0]], complex),
             np.array([[0, -1j], [1j, 0]], complex),
             np.diag([1., -1.])]
    unit = np.eye(2)
    # Fixed representation of gamma^a, with gamma^01234=i and eta=(-++++).
    gamma = [-1j * np.kron(pauli[2], unit)]
    gamma += [np.kron(pauli[0], sigma) for sigma in pauli]
    gamma += [np.kron(pauli[1], unit)]
    charge = gamma[2] @ gamma[4]
    return gamma, charge


EPS = np.array([[0., 1.], [-1., 0.]])
GAMMA, CHARGE = clifford()
IDENTITY = np.eye(4)


def contract(left, matrix, right):
    cm = CHARGE @ matrix
    return sum((left[a] * cm[a, b] * right[b]
                for a in range(4) for b in range(4) if cm[a, b] != 0), 0)


def transform(matrix, spinor):
    return [sum((matrix[a, b] * spinor[b] for b in range(4)), 0)
            for a in range(4)]


def lower(doublet):
    return [[sum((EPS[j, i] * doublet[j][a] for j in range(2)), 0)
             for a in range(4)] for i in range(2)]


def triplet(seed):
    """Positive triplet with L=2, using determinant-one integer shears."""
    rng = np.random.default_rng(seed)
    x, y = rng.integers(-2, 3, size=2)
    shear = np.array([[1, x], [y, 1 + x*y]], float)
    return shear @ np.diag([2., 1.]) @ shear.T


def extract_scalar(variation):
    result = [[Exterior() for _ in range(2)] for _ in range(2)]
    for i in range(2):
        for alpha in range(4):
            for mask, coefficient in variation[i][alpha].terms.items():
                physical, parameter = mask & 255, mask >> 8
                if physical.bit_count() != 2 or parameter.bit_count() != 1:
                    continue
                j, beta = divmod(parameter.bit_length() - 1, 4)
                if beta == alpha:
                    result[i][j] += Exterior({physical: coefficient / 4})
    return result


def compare_arrays(left, right):
    error = max((left[i][j] - right[i][j]).size() for i in range(2) for j in range(2))
    scale = max(1., *(x.size() for row in left + right for x in row))
    return error, scale


def evaluate_block(seed, kind, direction=0, derivative_component=0):
    """Derive the N/E/DL scalar Clifford block of delta lambda at psi_mu=0.

Other independent bosonic structures and Dphi, chi, T are zero in this
coefficient extraction. No gravitino-dependent or full nonlinear identity
is claimed. Cubic lambda terms are varied before selecting epsilon*phi^2.
"""
    upper = triplet(seed)
    down = EPS.T @ upper @ EPS
    norm = float(np.sqrt(2 * np.linalg.det(upper)))
    ph = [[Exterior.generator(4*i+a) for a in range(4)] for i in range(2)]
    ep = [[Exterior.generator(8+4*i+a) for a in range(4)] for i in range(2)]
    ph_down, ep_down = lower(ph), lower(ep)
    nvalue = 1. if kind == 'N' else 0.
    eslash = GAMMA[direction] if kind == 'E' else np.zeros((4, 4))
    dupper = np.zeros((2, 2))
    if kind == 'DL':
        i, j = ((0, 0), (0, 1), (1, 1))[derivative_component]
        dupper[i, j] = dupper[j, i] = 1.
    ddown = EPS.T @ dupper @ EPS
    dphi = []
    for i in range(2):
        dphi.append([nvalue/2*ep[i][a]
                     - .5j*transform(eslash, ep[i])[a]
                     - .5j*sum((dupper[i, j]*transform(GAMMA[direction], ep_down[j])[a]
                                for j in range(2)), 0)
                     for a in range(4)])
    phi = [[Jet(ph[i][a], dphi[i][a]) for a in range(4)] for i in range(2)]
    phi_down = lower(phi)
    du = [[.5j*(contract(ep[i], IDENTITY, ph[j]) + contract(ep[j], IDENTITY, ph[i]))
           for j in range(2)] for i in range(2)]
    ul = [[Jet(Exterior.scalar(upper[i,j]), du[i][j]) for j in range(2)] for i in range(2)]
    dl = [[sum((EPS[k,i]*EPS[l,j]*ul[k][l] for k in range(2) for l in range(2)), 0)
           for j in range(2)] for i in range(2)]
    dnorm = sum((down[i,j]*du[i][j] for i in range(2) for j in range(2)), 0) * (1/norm)
    ell = Jet(Exterior.scalar(norm), dnorm)
    gphi = [transform(GAMMA[direction], p) for p in phi_down]
    ephi = [transform(eslash, p) for p in phi]
    lam = [[Jet.constant(0) for _ in range(4)] for _ in range(2)]
    for i in range(2):
        for a in range(4):
            for j in range(2):
                lam[i][a] += -2*nvalue*ell**-3*dl[i][j]*phi[j][a]
                lam[i][a] += -2j*ell**-3*dl[i][j]*ephi[j][a]
                lam[i][a] += 2j*ell**-3*contract(phi_down[i], IDENTITY, phi_down[j])*phi[j][a]
                for k in range(2):
                    lam[i][a] += 2j*ell**-3*ul[j][k]*ddown[i,j]*gphi[k][a]
                    for l in range(2):
                        lam[i][a] += -6j*ell**-5*dl[i][j]*ul[k][l]*contract(phi_down[k], IDENTITY, phi_down[l])*phi[j][a]
    derived = extract_scalar([[x.variation for x in row] for row in lam])
    matrix = eslash if kind == 'E' else (GAMMA[direction] if kind == 'DL' else IDENTITY)
    bu = [[contract(ph[i], matrix, ph[j]) for j in range(2)] for i in range(2)]
    bd = [[contract(ph_down[i], matrix, ph_down[j]) for j in range(2)] for i in range(2)]
    br = [[contract(ph[i], matrix, ph_down[j]) for j in range(2)] for i in range(2)]
    bl = [[contract(ph_down[i], matrix, ph[j]) for j in range(2)] for i in range(2)]
    q = sum((upper[i,j]*bd[i][j] for i in range(2) for j in range(2)), 0)
    kbil = [[sum((down[k,i]*down[j,l]*bu[k][l] for k in range(2) for l in range(2)), 0)
             for j in range(2)] for i in range(2)]
    if kind in ('N', 'E'):
        factor = 1j if kind == 'N' else -1.
        expected = [[factor*(norm**-3*bd[i][j]-3*norm**-5*down[i,j]*q)
                     for j in range(2)] for i in range(2)]
        old_coefficients = (-.5j, -4/3) if kind == 'N' else (-2/3, -1/3)
        old = [[old_coefficients[0]*norm**-3*bd[i][j]+old_coefficients[1]*norm**-5*kbil[i][j]
                for j in range(2)] for i in range(2)]
    else:
        def sym(fn, i, j):
            return .5*(fn(i,j)+fn(j,i))
        def first(i,j):
            return sum((ddown[j,k]*bl[i][k] for k in range(2)), 0)*norm**-3
        mix = upper @ EPS
        def second(i,j):
            return sum((down[m,n]*mix[k,i]*ddown[j,k]*bu[m][n]
                        for m in range(2) for n in range(2) for k in range(2)), 0)*norm**-5
        expected = [[sym(lambda i,j: -first(i,j)+3*second(i,j),i,j) for j in range(2)] for i in range(2)]
        old = [[sym(lambda i,j: -2/3*first(i,j)-second(i,j),i,j) for j in range(2)] for i in range(2)]
    return derived, expected, old
