"""Independent nonconstant-sigma check of GC08/GC09/GC12 through two fermions.

The expected side uses ordinary matrix contractions of the source equations;
it does not call the symbolic templates or their inverse identities.
"""
import itertools
import json
import numpy as np
import log_step7_supercovariant as a
import verify_log_two_fermi_canonical as v

b, p = a.b, a.p
eta, gamma, g2, C, E = v.eta, v.gamma, v.g2, v.C, v.E
old_arr = v.arr
sigma, coupling = 1., 0.


def arr(f):
    if f.name == 'pow':
        return np.array(sigma ** f.power)
    if f.name == 'gc':
        return np.array(coupling)
    return old_arr(f)


v.arr = arr


def fixed_bilinear(left, right, matrix=None):
    matrix = np.eye(4) if matrix is None else matrix
    return left[:, 0] @ C @ matrix @ right[:, 1] - left[:, 1] @ C @ matrix @ right[:, 0]


def lower(u):
    return np.einsum('ij,sjg->sig', -E, u)


def bilinear(left, right, matrix=None):
    right = lower(right)
    return sum(fixed_bilinear(left[:, i], right[:, i], matrix) for i in range(2))


def act(matrix, u):
    return np.einsum('st,tig->sig', matrix, u)


def evaluate(poly, slot, degree):
    return sum((v.evaluate(c, fs, slot) for c, fs in poly.ts if sum(f.parity for f in fs) == degree), 0)


def trial(seed, rho, g):
    global sigma, coupling
    sigma, coupling = rho, g
    rng = np.random.default_rng(seed)
    v.cache.clear()
    for name, nd in [('rho', 0), ('rho', 1), ('rho', 2), ('lam', 0), ('lam', 1), ('hatF', 0), ('Hdual', 0), ('Lc', 0), ('compPhi', 0), ('compN', 0)]:
        shape = (5,) * nd + tuple({'l': 5, 's': 4, 'u': 2}[x] for x in b.spec[name][0]) + ((2,) if b.spec[name][2] else ())
        z = rng.integers(-2, 3, shape).astype(complex)
        if name in ('hatF', 'Hdual'):
            z -= z.T
        if name == 'Lc':
            z += z.T
        v.cache[name, nd] = z
    v.cache['rho', 0] = np.array(sigma)
    G, H, L = [v.cache[x, 0] for x in ('hatF', 'Hdual', 'Lc')]
    psi, phic, Nc = [v.cache[x, 0] for x in ('lam', 'compPhi', 'compN')]
    ds, dds, dpsi = v.cache['rho', 1], v.cache['rho', 2], v.cache['lam', 1]
    slash = lambda x: np.einsum('ab,abst->st', x, g2)
    dot = lambda x, y: np.einsum('ab,ab,a,b->', x, y, eta, eta)
    triplet_dot = lambda x, y: np.sum(x * ((-E) @ y @ (-E).T))
    dslash = sum(act(gamma[k], dpsi[k]) for k in range(5))
    sds = sum(gamma[k] * ds[k] for k in range(5))
    # GC03/GC08/GC12, entered without the symbolic contraction helpers.
    Y0 = -g * L / (2 * sigma)
    Y2 = np.array([[1j / (4 * sigma) * fixed_bilinear(psi[:, i], psi[:, j]) for j in range(2)] for i in range(2)])
    T0 = G / (8 * sigma) - H / (4 * sigma ** 2)
    T2 = np.array([[1j / (32 * sigma ** 2) * bilinear(psi, psi, eta[k] * eta[l] * g2[k, l]) for l in range(5)] for k in range(5)])
    chi1 = 1j * dslash / (8 * sigma) + 1j * act(sds, psi) / (16 * sigma ** 2) - act(slash(G), psi) / (32 * sigma ** 2)
    chi1 += act(slash(T0), psi) / (4 * sigma) - g * np.einsum('ij,sjg->sig', L, lower(psi)) / (16 * sigma ** 3) + g * phic / (8 * sigma ** 2)
    # GC09 evaluated by degree, retaining the two cross terms of each square.
    D0 = np.einsum('aa,a->', dds, eta) / (4 * sigma) + np.einsum('a,a,a->', ds, ds, eta) / (8 * sigma ** 2) - dot(G, G) / (16 * sigma ** 2)
    D0 += triplet_dot(Y0, Y0) / (4 * sigma ** 2) - 26 * dot(T0, T0) / 3 + 2 * dot(G, T0) / sigma + g * Nc / (4 * sigma ** 2)
    D2 = -bilinear(psi, dslash) / (8 * sigma ** 2) + (triplet_dot(Y0, Y2) + triplet_dot(Y2, Y0)) / (4 * sigma ** 2)
    D2 += 1j * bilinear(psi, psi, slash(T0)) / (4 * sigma ** 2) - 4j * bilinear(psi, chi1) / sigma
    D2 += -26 * (dot(T0, T2) + dot(T2, T0)) / 3 + 2 * dot(G, T2) / sigma
    expected = {'aux': {0: Y0, 2: Y2}, 'ten': {0: T0, 2: T2}, 'chi': {1: chi1}, 'auxD': {0: D0, 2: D2}}
    report = {}
    for name, degrees in expected.items():
        free = a.TEMPLATES[name][1]
        slot = 'source-independent-' + name
        p.FREE[slot] = {x[1:]: x[0] for x in free}
        poly = a.substitute(a.P(a.A(name, free)), 1 if name == 'chi' else 2)
        for degree, target in degrees.items():
            actual = evaluate(poly, slot, degree)
            residual = float(np.max(np.abs(actual - target)))
            relative = residual / max(1., float(np.max(np.abs(target))))
            assert relative < 1e-12, (name, degree, sigma, g, residual, relative)
            report[f'{name}:{degree}'] = {'absolute_residual': residual, 'relative_residual': relative}
    return {'seed': seed, 'sigma': sigma, 'g': g, 'checks': report}


if __name__ == '__main__':
    runs = [trial(9200 + i, rho, g) for i, (rho, g) in enumerate([(0.7, 0.), (1.3, 0.41), (2.4, -0.8)])]
    result = {'status': 'PASS', 'source_anchors': ['GA03', 'GC08', 'GC09', 'GC12'], 'independent_expected_side': 'matrix/Grassmann evaluation before gauge with nonzero dilatino and nonzero first and second scalar derivatives', 'runs': runs, 'scope': 'all explicit-degree terms of four forward pre-gauge composite templates; implicit fermions remain subject to the common outer truncation'}
    (a.OUT / 'ungauged_composite_debug.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2))
