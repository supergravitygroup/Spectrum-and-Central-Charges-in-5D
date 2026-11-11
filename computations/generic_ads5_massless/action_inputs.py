"""Item 23: source-grouped bosonic inputs, with exact symbolic coefficients.

The component projection and integration-by-parts identities are derived in
SOURCE_MAP.md.  No parameter sampling or small-coupling expansion is used.
"""
import sympy as s

Q = s.Rational
g = s.Symbol("g", real=True, nonzero=True)
L = s.Symbol("L0", positive=True)
N, k, x = s.symbols("N k x", real=True)
alpha, beta, zeta = s.symbols("alpha beta zeta", real=True)
c, v, h, E, multiplier = s.symbols("c v h E multiplier", real=True)
R, Ricci2, Riemann2 = s.symbols("R Ricci2 Riemann2", real=True)
couplings = (s.S.One, alpha, beta, zeta)
block_names = ("two_derivative", "weyl", "log", "r2")
r = g**2 * L**2 / 2  # ell^{-2}; g itself is not assigned a value.
N0 = -Q(3, 2) * g * L**2
vacuum_polynomial = (beta + 6*zeta)*g**2*L**2 - 8*L + 8
beta_on_vacuum = 8*(L - 1)/(g**2*L**2) - 6*zeta


def factor(value):
    return s.factor(s.cancel(value))


def on_vacuum(value):
    """Use Q=0 on g!=0, L>0; alpha, zeta, g and L remain symbolic."""
    return factor(value.subs(beta, beta_on_vacuum))


def pair(a, b):
    """Integrated (da)_{ab}(db)^{ab} for div_first d = x: -2*x*a*b."""
    return -2*x*a*b


def derivative_pair(a, b):
    """Integrated nabla(da).nabla(db) on AdS5; see SOURCE_MAP.md."""
    return 2*x**2*a*b + 6*r*pair(a, b)


def curvature_blocks():
    """Zero-form, constant-scalar curvature polynomials, before any AdS EOM.

    generic_combination/action.md: G-2D, G-W + G-D7/D8, G-LOG, G-R2.
    Ricci2 and Riemann2 are independent curvature monomials here.
    """
    D = -R/32 + g*N/4 + g**2*L**2/16
    return dict(zip(block_names, (
        L*R - 2*N**2/L - 2*g*L*N - 4*g*N - g**2*L**3/2 + 2*g**2*L**2,
        (Riemann2 - Q(4, 3)*Ricci2 + R**2/6)/8 + Q(64, 3)*D**2,
        -Ricci2/6 + R**2/24 + R*(g*N/6 - g**2*L**2/12)
        - g**2*N**2/6 + Q(2, 3)*g**3*N*L**2 + Q(5, 24)*g**4*L**4,
        (-R/2 - N**2/L**2)**2 - g**2*L**2*R/4
        - Q(5, 2)*g**2*N**2 - 4*g*N**3/L**2 + g**4*L**4/16,
    )))


def vector_groups():
    """Quadratic singlet vector/exact-two-form projection of the current action.

    H=dh, G=dc, V=dv. E is retained until the linearized Bianchi constraint.
    The labels identify the source groups explained in SOURCE_MAP.md.
    """
    T = (c - 2*h)/8
    F = 2*E/L + s.sqrt(2)*v
    Y0 = 10*r - N0**2/L**2
    return {
        "two_derivative": {
            "2D-strengths": -L*pair(c, c)/2 + 4*L*pair(h, h),
            "2D-constrained-current": -2*E**2/L - 2*s.sqrt(2)*E*v - 4*g*E*c,
        },
        "weyl": {
            "W-internal-strength": -pair(v, v)/6,
            "W-T-derivatives": -Q(64, 3)*derivative_pair(T, T) + 64*x**2*T**2,
            "W-T-curvature": Q(320, 3)*r*pair(T, T),
            "W-gauging": -g*L*pair(v, c - 2*h)/(3*s.sqrt(2)),
        },
        "log": {
            "LOG-internal-strength": pair(v, v)/12,
            "LOG-strength-mixing": g*L*pair(v, c)/(6*s.sqrt(2))
            + 2*g*L*pair(v, h)/(3*s.sqrt(2)),
            "LOG-curvature": -4*r*pair(c, c)/6 + Q(16, 3)*r*pair(c, h)
            - 20*r*(pair(c, h)/3 - pair(h, h)/3),
            "LOG-N": g*N0*(-pair(c, c)/3 - Q(2, 3)*pair(c, h) + 2*pair(h, h)),
            "LOG-L": g**2*L**2*(pair(c, c)/24 - pair(c, h)/6 - pair(h, h)),
            "LOG-G-derivative": -x**2*c**2/6,
            # The cyclic H derivative in G-LOG vanishes for the exact part H=dh.
            "LOG-current": -g*E*x*c/3 + g**2*E**2/3,
        },
        "r2": {
            "R2-Y-square": 2*Y0*(pair(c, c)/4 - 2*pair(h, h) - E**2/L**2),
            "R2-composite-strength": -pair(F, F)/4,
            "R2-mixed-strength": N0/L*(pair(F, c) - 4*pair(F, h)),
            "R2-N-square": -N0**2/L**2*(pair(c, c) - 4*pair(c, h)),
            "R2-gauging": g**2*L**2*(pair(c, c)/8 - pair(h, h)) - g**2*E**2/2,
        },
    }


def vector_blocks():
    return {name: s.expand(sum(groups.values())) for name, groups in vector_groups().items()}


def expanded_vector_blocks():
    """Independent rewritten representatives, retaining the current Bianchi terms.

    Adapted from the historical general_c_CF.py transcription, then checked
    against the compact current-action projection above, block by block.
    This path uses the non-cyclic H derivative and explicit gE terms.
    """
    G2, GH, H2 = pair(c, c), pair(c, h), pair(h, h)
    divG = -x*c
    nH2 = derivative_pair(h, h)
    F = 2*E/L + s.sqrt(2)*v
    Y0 = 10*r - N0**2/L**2
    return dict(zip(block_names, (
        -L*G2/2 + 4*L*H2 - 2*E**2/L - 2*s.sqrt(2)*E*v - 4*g*E*c,
        -pair(v, v)/6 + r*(Q(4, 3)*G2 - GH/3 - Q(10, 3)*H2)
        + divG**2/3 - Q(4, 3)*nH2
        + g*N0*(Q(2, 3)*G2 - Q(2, 3)*GH - 4*H2)
        - g*L*(pair(v, c) - 2*pair(v, h))/(3*s.sqrt(2))
        - Q(2, 3)*g*E*divG + g**2*L**2*(G2/6 - GH/6 - H2) + g**2*E**2,
        pair(v, v)/12 + r*(-Q(2, 3)*G2 - Q(4, 3)*GH + Q(8, 3)*H2)
        - divG**2/6 + Q(2, 3)*nH2
        + g*N0*(-G2/3 - Q(2, 3)*GH + 2*H2)
        + g*L*(pair(v, c) + 4*pair(v, h))/(6*s.sqrt(2))
        + g*E*divG/3 + g**2*L**2*(G2/24 - GH/6 - H2),
        2*Y0*(G2/4 - 2*H2 - E**2/L**2) - pair(F, F)/4
        + N0/L*(pair(F, c) - 4*pair(F, h))
        - N0**2/L**2*(G2 - 4*GH) + g**2*L**2*(G2/8 - H2) - g**2*E**2/2,
    )))
