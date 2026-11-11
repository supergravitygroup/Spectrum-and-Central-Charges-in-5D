#!/usr/bin/env python3
"""Definition-led audits for the fully expanded bosonic Weyl/Log report.

No coefficient is imported from Gold et al.'s printed expanded Weyl or Log
actions.  The checks start from the component-descendant map used in the
report and test its algebraic expansion, differential ordering, epsilon
identities, the raw curved-space Log w-sector canonicalization, gauged
three-form Bianchi reduction, dimensions, and the absence of helper-field
notation in the two final displayed densities.
"""

from __future__ import annotations

import itertools
from pathlib import Path
import random

import sympy as sp


RNG_SEED = 20260820
N_DIM = 5


def assert_zero(expr: sp.Expr, label: str) -> None:
    value = sp.expand(expr)
    if value != 0:
        raise AssertionError(f"{label}: {value}")


def check_composite_D() -> None:
    R, GG, GH, HH, gN, g2L2 = sp.symbols("R GG GH HH gN g2L2")
    T2 = GG / 64 - GH / 16 + HH / 16
    GT = GG / 8 - GH / 4
    direct = (
        -R / 32
        - GG / 16
        - sp.Rational(26, 3) * T2
        + 2 * GT
        + gN / 4
        + g2L2 / 16
    )
    expected = (
        -R / 32
        + sp.Rational(5, 96) * GG
        + GH / 24
        - sp.Rational(13, 24) * HH
        + gN / 4
        + g2L2 / 16
    )
    assert_zero(direct - expected, "composite D")


def check_log_descendant_conversion() -> None:
    # Supplement: +(69/1024) w^2 Y.  Projection: D=-3Y/128.
    coefficient_in_D = sp.Rational(69, 1024) * (-sp.Rational(128, 3))
    if coefficient_in_D != -sp.Rational(23, 8):
        raise AssertionError("Log Y-to-D conversion")


def check_log_curvature_canonicalization() -> None:
    # Raw supplement notation:
    # N=(D_a w_bc)^2, Q=(D^b w^a_b)(D^c w_ac),
    # I=(D^c w^a_b)(D^b w_ac),
    # J=R_abcd w^ab w^cd, Jcross=R_acbd w^ab w^cd,
    # K=R_ab w^ac w^b_c, and Rw2=R w_ab w^ab.
    N, Q, I, J, Jcross, K, Rw2 = sp.symbols("N Q I J Jcross K Rw2")
    raw_curvature = (
        J / 3
        + Jcross / 3
        - sp.Rational(2, 3) * K
        - K / 3
        - sp.Rational(27, 256) * Rw2
    )
    after_ibp = (
        sp.Rational(39, 16) * N
        - I / 2
        + 2 * Q
        - sp.Rational(33, 16) * N
        - sp.Rational(9, 4) * Q
        + sp.Rational(3, 4) * I
    )
    # Algebraic Bianchi identity: Jcross=J/2.
    # One derivative commutator: I=Q+K-J/2.
    canonical = sp.expand(
        (raw_curvature + after_ibp)
        .subs(Jcross, J / 2)
        .subs(I, Q + K - J / 2)
    )
    expected = sp.Rational(3, 8) * N + sp.Rational(3, 8) * J
    expected += -sp.Rational(3, 4) * K - sp.Rational(27, 256) * Rw2
    assert_zero(canonical - expected, "raw Log w-sector canonicalization")

    missing_standard_coefficient = canonical.coeff(J) - sp.Rational(1, 4)
    if missing_standard_coefficient != sp.Rational(1, 8):
        raise AssertionError("Log standard-frame Riemann-w-w correction")

    RGG, RGH, RHH = sp.symbols("RGG RGH RHH")
    mapped_delta = (
        -missing_standard_coefficient
        * sp.Rational(4, 9)
        * (RGG - 4 * RGH + 4 * RHH)
    )
    expected_delta = (
        -RGG / 18
        + sp.Rational(2, 9) * RGH
        - sp.Rational(2, 9) * RHH
    )
    assert_zero(mapped_delta - expected_delta, "mapped Log curvature correction")
    former_block = (
        RGG / 18
        - sp.Rational(2, 9) * RGH
        + sp.Rational(2, 9) * RHH
    )
    assert_zero(former_block + mapped_delta, "corrected final Log Riemann block")
    assert_zero(
        mapped_delta.subs({RGG: 4 * RHH, RGH: 2 * RHH}),
        "G=2H correction limit",
    )


def check_weyl_complete_scalar_polynomial() -> None:
    R, sG, q, sH, n, p = sp.symbols("R sG q sH n p")
    two_form_square = sG - 4 * q + 4 * sH
    graviphoton_dot = sG - 2 * q
    D = (
        -R / 32
        + sp.Rational(5, 96) * sG
        + q / 24
        - sp.Rational(13, 24) * sH
        + n / 4
        + p / 16
    )

    # Complete commutative scalar part of the raw descendant-derived density:
    # pure Weyl-tensor R^2 piece, D block, explicit R contractions, and the
    # factorized quartics.  Noncommuting chains are checked independently.
    raw = -R**2 / 24
    raw += -sp.Rational(128, 3) * D**2
    raw += sp.Rational(8, 3) * D * graviphoton_dot
    raw += -sp.Rational(32, 9) * D * two_form_square
    raw += -R * graviphoton_dot / 12 - R * two_form_square / 12
    raw += graviphoton_dot * two_form_square / 36
    raw += sp.Rational(11, 216) * two_form_square**2

    expected = (
        -R**2 / 12
        + R * (q / 3 - sp.Rational(4, 3) * sH + sp.Rational(2, 3) * n + p / 6)
        - sG**2 / 12
        - sG * q / 3
        + sp.Rational(8, 3) * sG * sH
        + sp.Rational(4, 3) * q**2
        - sp.Rational(16, 3) * q * sH
        - 4 * sH**2
        + n * (-sp.Rational(4, 3) * sG + sp.Rational(4, 3) * q + 8 * sH)
        + p * (-sG / 3 + q / 3 + 2 * sH)
        - sp.Rational(8, 3) * n**2
        - sp.Rational(4, 3) * n * p
        - p**2 / 6
    )
    # A full residual equality catches both wrong coefficients and unexpected
    # extra monomials; this replaces the earlier selected-dictionary check.
    assert_zero(raw - expected, "complete Weyl scalar polynomial")


def check_log_complete_scalar_polynomial() -> None:
    R, sG, q, sH, n, p = sp.symbols("R sG q sH n p")
    two_form_square = sG - 4 * q + 4 * sH
    graviphoton_dot = sG - 2 * q
    D = (
        -R / 32
        + sp.Rational(5, 96) * sG
        + q / 24
        - sp.Rational(13, 24) * sH
        + n / 4
        + p / 16
    )

    raw = R * (
        24 * sG
        - sp.Rational(160, 3) * graviphoton_dot
        + 12 * two_form_square
        + 128 * D
        - 8 * p
    ) / 256
    raw += -sp.Rational(8, 3) * D**2
    raw += p * (two_form_square - 2 * sG + p) / 32
    raw += D * (
        -sp.Rational(32, 3) * graviphoton_dot
        - 8 * sG
        + sp.Rational(92, 9) * two_form_square
        + 24 * p
    ) / 8
    raw += sp.Rational(23, 384) * R**2

    # Factorized scalar part of the independent tensor-quartic block.
    raw += -two_form_square * graviphoton_dot / 72
    raw += -sp.Rational(25, 96) * two_form_square * sG
    raw += graviphoton_dot * sG / 4 - sG**2 / 32
    raw += sp.Rational(335, 3456) * two_form_square**2

    expected = (
        R**2 / 24
        + R * (n / 6 - p / 12 + q / 3 - sH / 3)
        - n**2 / 6
        + sp.Rational(2, 3) * n * p
        + n * (-sG / 3 - sp.Rational(2, 3) * q + 2 * sH)
        + sp.Rational(5, 24) * p**2
        + p * (sG / 24 - q / 6 - sH)
        - sG**2 / 48
        - sG * q / 3
        + sp.Rational(2, 3) * sG * sH
        + sp.Rational(4, 3) * q**2
        - sp.Rational(4, 3) * q * sH
        - 2 * sH**2
    )
    assert_zero(raw - expected, "complete Log scalar polynomial")


def antisymmetric_matrix(rng: random.Random, n: int = N_DIM) -> sp.Matrix:
    matrix = sp.zeros(n)
    for a in range(n):
        for b in range(a + 1, n):
            value = rng.randint(-4, 4)
            matrix[a, b] = value
            matrix[b, a] = -value
    return matrix


def two_form_inner_euclidean(first: sp.Matrix, second: sp.Matrix) -> sp.Expr:
    return sum(first[a, b] * second[a, b] for a in range(N_DIM) for b in range(N_DIM))


def check_quartic_chain_expansions() -> None:
    rng = random.Random(RNG_SEED)
    for sample in range(24):
        G = antisymmetric_matrix(rng)
        H = antisymmetric_matrix(rng)
        combination = G - 2 * H
        sG = two_form_inner_euclidean(G, G)
        q = two_form_inner_euclidean(G, H)
        sH = two_form_inner_euclidean(H, H)
        combination_square = two_form_inner_euclidean(combination, combination)
        graviphoton_dot = two_form_inner_euclidean(G, combination)

        # Weyl quartic block before the Bianchi epsilon-square shift.
        raw_weyl = graviphoton_dot * combination_square / 36
        raw_weyl += sp.Rational(11, 216) * combination_square**2
        raw_weyl += sp.trace(combination**3 * G) / 3
        raw_weyl += -sp.trace(combination**4) / 2
        expanded_weyl = (
            sp.Rational(17, 216) * sG**2
            - sp.Rational(31, 54) * sG * q
            + sp.Rational(14, 27) * sG * sH
            + sp.Rational(28, 27) * q**2
            - sp.Rational(50, 27) * q * sH
            + sp.Rational(22, 27) * sH**2
            - sp.trace(G**4) / 6
            + 2 * sp.trace(G**3 * H)
            - sp.Rational(16, 3) * sp.trace(G**2 * H**2)
            - sp.Rational(8, 3) * sp.trace(G * H * G * H)
            + sp.Rational(40, 3) * sp.trace(H**3 * G)
            - 8 * sp.trace(H**4)
        )
        assert_zero(raw_weyl - expanded_weyl, f"Weyl raw quartics sample {sample}")

        # The non-E part of the Bianchi shift is
        # -Q_G^2/48 + Q_G.Q_HH/12.  Epsilon identities turn it into
        # +sG^2/6-Tr(G^4)/3-2q^2/3+4Tr(GHGH)/3.
        bianchi_shift = (
            sG**2 / 6
            - sp.trace(G**4) / 3
            - sp.Rational(2, 3) * q**2
            + sp.Rational(4, 3) * sp.trace(G * H * G * H)
        )
        clean_weyl = expanded_weyl + bianchi_shift
        clean_expected = (
            sp.Rational(53, 216) * sG**2
            - sp.Rational(31, 54) * sG * q
            + sp.Rational(14, 27) * sG * sH
            + sp.Rational(10, 27) * q**2
            - sp.Rational(50, 27) * q * sH
            + sp.Rational(22, 27) * sH**2
            - sp.trace(G**4) / 2
            + 2 * sp.trace(G**3 * H)
            - sp.Rational(16, 3) * sp.trace(G**2 * H**2)
            - sp.Rational(4, 3) * sp.trace(G * H * G * H)
            + sp.Rational(40, 3) * sp.trace(H**3 * G)
            - 8 * sp.trace(H**4)
        )
        assert_zero(clean_weyl - clean_expected, f"Weyl clean quartics sample {sample}")

        # Log algebraic quartic block, compared directly with the five
        # displayed cyclic chains and six scalar products.
        def u4(X: sp.Matrix, Y: sp.Matrix, Z: sp.Matrix, W: sp.Matrix) -> sp.Expr:
            return sum(
                X[a, b] * Y[c, d] * Z[a, c] * W[b, d]
                for a, b, c, d in itertools.product(range(N_DIM), repeat=4)
            )

        raw_log = -sp.Rational(2, 3) * (
            combination_square * graviphoton_dot / 48
            + u4(combination, G, combination, combination)
            + sp.Rational(25, 64) * combination_square * sG
            - sp.Rational(3, 2) * u4(combination, G, combination, G)
            - sp.Rational(3, 8) * graviphoton_dot * sG
            + sp.Rational(3, 4) * u4(combination, G, G, G)
        )
        raw_log += -sp.Rational(1, 32) * (sG**2 - 4 * u4(G, G, G, G))
        raw_log += sp.Rational(335, 3456) * combination_square**2
        expanded_log = (
            sp.Rational(143, 3456) * sG**2
            - sp.Rational(65, 432) * sG * q
            - sp.Rational(139, 432) * sG * sH
            + sp.Rational(311, 216) * q**2
            - sp.Rational(323, 108) * q * sH
            + sp.Rational(335, 216) * sH**2
            - sp.trace(G**4) / 24
            + sp.trace(G**3 * H)
            - sp.Rational(4, 3) * sp.trace(G**2 * H**2)
            - sp.Rational(8, 3) * sp.trace(G * H * G * H)
            + sp.Rational(16, 3) * sp.trace(H**3 * G)
        )
        assert_zero(raw_log - expanded_log, f"Log quartics sample {sample}")


def random_derivative_tensor(rng: random.Random) -> list[list[list[int]]]:
    tensor = [[[0 for _ in range(N_DIM)] for _ in range(N_DIM)] for _ in range(N_DIM)]
    for derivative in range(N_DIM):
        for a in range(N_DIM):
            for b in range(a + 1, N_DIM):
                value = rng.randint(-3, 3)
                tensor[derivative][a][b] = value
                tensor[derivative][b][a] = -value
    return tensor


def random_second_derivative_tensor(
    rng: random.Random,
) -> list[list[list[list[int]]]]:
    tensor = [
        [
            [[0 for _ in range(N_DIM)] for _ in range(N_DIM)]
            for _ in range(N_DIM)
        ]
        for _ in range(N_DIM)
    ]
    for first in range(N_DIM):
        for second in range(N_DIM):
            for a in range(N_DIM):
                for b in range(a + 1, N_DIM):
                    value = rng.randint(-2, 2)
                    tensor[first][second][a][b] = value
                    tensor[first][second][b][a] = -value
    return tensor


def add_derivatives(first, second, factor: int):
    return [
        [
            [first[d][a][b] + factor * second[d][a][b] for b in range(N_DIM)]
            for a in range(N_DIM)
        ]
        for d in range(N_DIM)
    ]


def add_second_derivatives(first, second, factor: int):
    return [
        [
            [
                [
                    first[p][q][a][b] + factor * second[p][q][a][b]
                    for b in range(N_DIM)
                ]
                for a in range(N_DIM)
            ]
            for q in range(N_DIM)
        ]
        for p in range(N_DIM)
    ]


def derivative_norm(first, second) -> sp.Expr:
    return sum(
        first[d][a][b] * second[d][a][b]
        for d, a, b in itertools.product(range(N_DIM), repeat=3)
    )


def derivative_cross(first, second) -> sp.Expr:
    return sum(
        first[a][c][e] * second[c][a][e]
        for a, c, e in itertools.product(range(N_DIM), repeat=3)
    )


def divergence(derivative) -> list[sp.Expr]:
    return [sum(derivative[b][a][b] for b in range(N_DIM)) for a in range(N_DIM)]


def second_derivative_block(form: sp.Matrix, second_derivative) -> sp.Expr:
    return sum(
        form[c, d] * second_derivative[c][b][b][d]
        for c, d, b in itertools.product(range(N_DIM), repeat=3)
    )


def dot(first, second) -> sp.Expr:
    return sum(first[a] * second[a] for a in range(N_DIM))


def check_raw_derivative_expansions() -> None:
    rng = random.Random(RNG_SEED + 1)
    for sample in range(16):
        G = antisymmetric_matrix(rng)
        H = antisymmetric_matrix(rng)
        combination = G - 2 * H
        dG = random_derivative_tensor(rng)
        dH = random_derivative_tensor(rng)
        dC = add_derivatives(dG, dH, -2)
        ddG = random_second_derivative_tensor(rng)
        ddH = random_second_derivative_tensor(rng)
        ddC = add_second_derivatives(ddG, ddH, -2)

        compact_weyl = sp.Rational(2, 3) * derivative_norm(dC, dC)
        compact_weyl += -sp.Rational(2, 3) * derivative_cross(dC, dC)
        compact_weyl += sp.Rational(4, 3) * second_derivative_block(combination, ddC)
        expanded_weyl = sp.Rational(2, 3) * derivative_norm(dG, dG)
        expanded_weyl += -sp.Rational(8, 3) * derivative_norm(dG, dH)
        expanded_weyl += sp.Rational(8, 3) * derivative_norm(dH, dH)
        expanded_weyl += -sp.Rational(2, 3) * derivative_cross(dG, dG)
        expanded_weyl += sp.Rational(8, 3) * derivative_cross(dG, dH)
        expanded_weyl += -sp.Rational(8, 3) * derivative_cross(dH, dH)
        expanded_weyl += sp.Rational(4, 3) * second_derivative_block(G, ddG)
        expanded_weyl += -sp.Rational(8, 3) * second_derivative_block(G, ddH)
        expanded_weyl += -sp.Rational(8, 3) * second_derivative_block(H, ddG)
        expanded_weyl += sp.Rational(16, 3) * second_derivative_block(H, ddH)
        assert_zero(compact_weyl - expanded_weyl, f"Weyl derivatives sample {sample}")

        divG = divergence(dG)
        divH = divergence(dH)
        divC = divergence(dC)
        compact_log = sp.Rational(1, 6) * derivative_norm(dC, dC)
        compact_log += sp.Rational(1, 4) * derivative_norm(dG, dG)
        compact_log += -dot(divG, divC)
        expanded_log = sp.Rational(5, 12) * derivative_norm(dG, dG)
        expanded_log += -sp.Rational(2, 3) * derivative_norm(dG, dH)
        expanded_log += sp.Rational(2, 3) * derivative_norm(dH, dH)
        expanded_log += -dot(divG, divG) + 2 * dot(divG, divH)
        assert_zero(compact_log - expanded_log, f"Log derivatives sample {sample}")


def epsilon5(indices: tuple[int, int, int, int, int]) -> int:
    return int(sp.LeviCivita(*indices))


def epsilon_vector(first: sp.Matrix, second: sp.Matrix) -> list[sp.Expr]:
    return [
        sum(
            epsilon5((a, b, c, d, e)) * first[b, c] * second[d, e]
            for b, c, d, e in itertools.product(range(N_DIM), repeat=4)
        )
        for a in range(N_DIM)
    ]


def odd_first(G: sp.Matrix, first: sp.Matrix, derivative_second) -> sp.Expr:
    return sum(
        epsilon5((a, b, c, d, e))
        * G[a, b]
        * first[c, f]
        * derivative_second[d][e][f]
        for a, b, c, d, e, f in itertools.product(range(N_DIM), repeat=6)
    )


def odd_second(G: sp.Matrix, first: sp.Matrix, derivative_second) -> sp.Expr:
    return sum(
        epsilon5((a, b, c, d, e))
        * G[a, b]
        * first[c, f]
        * derivative_second[f][d][e]
        for a, b, c, d, e, f in itertools.product(range(N_DIM), repeat=6)
    )


def odd_third(first: sp.Matrix, second: sp.Matrix, derivative_third) -> sp.Expr:
    return sum(
        epsilon5((a, b, c, d, e))
        * first[a, b]
        * second[c, d]
        * derivative_third[f][e][f]
        for a, b, c, d, e, f in itertools.product(range(N_DIM), repeat=6)
    )


def check_raw_parity_expansions() -> None:
    rng = random.Random(RNG_SEED + 2)
    for sample in range(10):
        G = antisymmetric_matrix(rng)
        H = antisymmetric_matrix(rng)
        combination = G - 2 * H
        dG = random_derivative_tensor(rng)
        dH = random_derivative_tensor(rng)
        dC = add_derivatives(dG, dH, -2)

        compact_weyl = sp.Rational(1, 2) * odd_first(G, combination, dC)
        compact_weyl += sp.Rational(1, 3) * odd_second(G, combination, dC)
        compact_weyl += sp.Rational(1, 6) * odd_third(combination, combination, dC)
        expanded_weyl = (
            sp.Rational(1, 2) * odd_first(G, G, dG)
            - odd_first(G, G, dH)
            - odd_first(G, H, dG)
            + 2 * odd_first(G, H, dH)
            + sp.Rational(1, 3) * odd_second(G, G, dG)
            - sp.Rational(2, 3) * odd_second(G, G, dH)
            - sp.Rational(2, 3) * odd_second(G, H, dG)
            + sp.Rational(4, 3) * odd_second(G, H, dH)
            + sp.Rational(1, 6) * odd_third(G, G, dG)
            - sp.Rational(1, 3) * odd_third(G, G, dH)
            - sp.Rational(2, 3) * odd_third(G, H, dG)
            + sp.Rational(4, 3) * odd_third(G, H, dH)
            + sp.Rational(2, 3) * odd_third(H, H, dG)
            - sp.Rational(4, 3) * odd_third(H, H, dH)
        )
        assert_zero(compact_weyl - expanded_weyl, f"Weyl parity sample {sample}")

        divG = divergence(dG)
        divH = divergence(dH)
        divC = divergence(dC)
        epsGG = epsilon_vector(G, G)
        epsHH = epsilon_vector(H, H)
        epsHG = epsilon_vector(H, G)
        compact_log = -sp.Rational(1, 24) * dot(divC, epsGG)
        compact_log += sp.Rational(2, 3) * dot(divC, epsHH)
        compact_log += sp.Rational(5, 48) * dot(divG, epsGG)
        compact_log += -sp.Rational(1, 6) * dot(divG, epsHG)
        compact_log += -sp.Rational(1, 3) * dot(divG, epsHH)
        expanded_log = sp.Rational(1, 16) * dot(divG, epsGG)
        expanded_log += sp.Rational(1, 12) * dot(divH, epsGG)
        expanded_log += sp.Rational(1, 3) * dot(divG, epsHH)
        expanded_log += -sp.Rational(4, 3) * dot(divH, epsHH)
        expanded_log += -sp.Rational(1, 6) * dot(divG, epsHG)
        assert_zero(compact_log - expanded_log, f"Log parity sample {sample}")


def check_epsilon_square_identities() -> None:
    rng = random.Random(RNG_SEED + 3)
    metric = [-1, 1, 1, 1, 1]

    def raise_two(form: sp.Matrix, a: int, b: int) -> sp.Expr:
        return metric[a] * metric[b] * form[a, b]

    def contraction(first: sp.Matrix, second: sp.Matrix) -> sp.Expr:
        return sum(
            first[a, b] * raise_two(second, a, b)
            for a, b in itertools.product(range(N_DIM), repeat=2)
        )

    def cyclic_chain(form: sp.Matrix) -> sp.Expr:
        return sum(
            form[a, b]
            * raise_two(form, b, c)
            * form[c, d]
            * raise_two(form, d, a)
            for a, b, c, d in itertools.product(range(N_DIM), repeat=4)
        )

    for sample in range(12):
        G = antisymmetric_matrix(rng)
        H = antisymmetric_matrix(rng)
        qgg_up = epsilon_vector(G, G)
        qhh_up = epsilon_vector(H, H)
        qgg_lower = []
        for a in range(N_DIM):
            value = 0
            for f, g, h, i in itertools.product(range(N_DIM), repeat=4):
                eps_lower = -epsilon5((a, f, g, h, i))
                value += eps_lower * raise_two(G, f, g) * raise_two(G, h, i)
            qgg_lower.append(value)

        lhs_gg = dot(qgg_up, qgg_lower)
        rhs_gg = -8 * contraction(G, G) ** 2 + 16 * cyclic_chain(G)
        assert_zero(lhs_gg - rhs_gg, f"epsilon GGGG sample {sample}")

        lhs_hhgg = dot(qhh_up, qgg_lower)
        mixed_chain = sum(
            H[a, b]
            * H[c, d]
            * raise_two(G, a, c)
            * raise_two(G, b, d)
            for a, b, c, d in itertools.product(range(N_DIM), repeat=4)
        )
        rhs_hhgg = -8 * contraction(G, H) ** 2 + 16 * mixed_chain
        assert_zero(lhs_hhgg - rhs_hhgg, f"epsilon HHGG sample {sample}")


def check_gauged_bianchi_sectors() -> None:
    g = sp.symbols("g")
    KH0, E, KG, QG, QHH, QHG = sp.symbols("KH0 E KG QG QHH QHG")
    KH = KH0 + g * E / 2

    weyl = -8 * KH**2 + sp.Rational(8, 3) * KG * KH
    weyl += -sp.Rational(4, 3) * QHH * KH
    weyl += -QG * KH / 6 + QG * KG / 6
    weyl0 = weyl.subs(E, 0)
    expected_weyl_E = -2 * g**2 * E**2 + sp.Rational(4, 3) * g * E * KG
    expected_weyl_E += sp.Rational(5, 12) * g * E * QG
    expected_weyl_E += -sp.Rational(2, 3) * g * E * QHH
    assert_zero(
        (weyl - weyl0).subs(KH0, -QG / 16) - expected_weyl_E,
        "Weyl gauged Bianchi sector",
    )

    log = sp.Rational(2, 3) * KG * KH + sp.Rational(4, 3) * KH**2
    log += KG * QG / 16 + KG * QHH / 3 - KG * QHG / 6
    log += KH * QG / 12 - sp.Rational(4, 3) * KH * QHH
    log0 = log.subs(E, 0)
    expected_log_E = g * E * KG / 3 - g * E * QG / 24
    expected_log_E += -sp.Rational(2, 3) * g * E * QHH + g**2 * E**2 / 3
    assert_zero(
        (log - log0).subs(KH0, -QG / 16) - expected_log_E,
        "Log gauged Bianchi sector",
    )


def check_dimensions_and_limits() -> None:
    dim = {"d": 1, "g": 1, "R": 2, "G": 1, "H": 1, "N": 1, "L": 0, "E": 1, "V": 2}
    checks = {
        "Riemann square": 2 * dim["R"],
        "Riemann times two forms": dim["R"] + 2 * dim["G"],
        "g R N": dim["g"] + dim["R"] + dim["N"],
        "g^2 (dL)^2": 2 * dim["g"] + 2 * (dim["d"] + dim["L"]),
        "g^2 E^2": 2 * dim["g"] + 2 * dim["E"],
        "g E epsilon G G": dim["g"] + dim["E"] + 2 * dim["G"],
        "V^2": 2 * dim["V"],
    }
    for label, value in checks.items():
        if value != 4:
            raise AssertionError((label, value))

    # Pure-geometry endpoints stated in the report.
    Riem2, Ric2, R2 = sp.symbols("Riem2 Ric2 R2")
    pure_weyl = -Riem2 / 4 + Ric2 / 3 - R2 / 12
    pure_log = -Ric2 / 6 + R2 / 24
    if pure_weyl.subs({Riem2: 0, Ric2: 0, R2: 0}) != 0:
        raise AssertionError("Weyl zero-field limit")
    if pure_log.subs({Ric2: 0, R2: 0}) != 0:
        raise AssertionError("Log zero-field limit")


def check_final_formula_has_no_helper_shorthand() -> None:
    project_root = Path(__file__).resolve().parents[1]
    tex_path = project_root / "results/latex/weyl_log_from_definitions/weyl_log_from_definitions.tex"
    source = tex_path.read_text(encoding="utf-8")
    start = source.index(r"\section{Final Result}")
    end = source.index(r"\section{Convention Dependence", start)
    final_source = source[start:end]
    forbidden = [r"\WA", r"\Delta", "K_", "Q_", "s_G", "s_H", r"\operatorname{tr}"]
    present = [token for token in forbidden if token in final_source]
    if present:
        raise AssertionError(f"helper shorthand remains in final result: {present}")

    corrected_standard_term = r"\frac38\cR_{abcd}w^{ab}w^{cd}"
    old_grouped_term = r"\frac14\cR_{abcd}(F^{ab}F^{cd}+w^{ab}w^{cd})"
    if corrected_standard_term not in source:
        raise AssertionError("corrected 3/8 standard-frame Log term is missing")
    if old_grouped_term in source:
        raise AssertionError("stale 1/4-1/4 standard-frame Log term remains")

    log_start = final_source.index(r"\subsection{Fully expanded Log invariant}")
    log_final = final_source[log_start:]
    stale_log_riemann_terms = [
        r"+\frac1{18}R_{abcd}G^{ab}G^{cd}",
        r"-\frac29R_{abcd}G^{ab}H^{cd}",
        r"+\frac29R_{abcd}H^{ab}H^{cd}",
    ]
    stale_present = [term for term in stale_log_riemann_terms if term in log_final]
    if stale_present:
        raise AssertionError(
            f"stale Riemann-two-form terms remain in final Log density: {stale_present}"
        )


def main() -> None:
    checks = [
        check_composite_D,
        check_log_descendant_conversion,
        check_log_curvature_canonicalization,
        check_weyl_complete_scalar_polynomial,
        check_log_complete_scalar_polynomial,
        check_quartic_chain_expansions,
        check_raw_derivative_expansions,
        check_raw_parity_expansions,
        check_epsilon_square_identities,
        check_gauged_bianchi_sectors,
        check_dimensions_and_limits,
        check_final_formula_has_no_helper_shorthand,
    ]
    for check in checks:
        check()
        print(f"PASS  {check.__name__}")
    print(f"PASS  all {len(checks)} fully-expanded definition-map audits")


if __name__ == "__main__":
    main()
