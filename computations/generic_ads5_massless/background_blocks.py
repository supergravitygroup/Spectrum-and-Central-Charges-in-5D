"""Shared exact constant-curvature projections of the four bosonic blocks."""
import sympy as s

L, N, k, g, c2, alpha, beta, lam = s.symbols(
    "L0 N0 k g c2 alpha beta lambda", real=True)
Dbar = -s.Rational(5, 8)*k+g*N/4+g**2*L**2/16
blocks = [
    20*k*L-2*N**2/L-2*g*L*N-4*g*N-g**2*L**3/2+2*g**2*L**2,
    s.Rational(64, 3)*Dbar**2,
    s.Rational(10, 3)*k**2+s.Rational(10, 3)*g*k*N
    -s.Rational(5, 3)*g**2*k*L**2-g**2*N**2/6
    +s.Rational(2, 3)*g**3*N*L**2+s.Rational(5, 24)*g**4*L**4,
    (10*k+N**2/L**2)**2-5*g**2*k*L**2
    -s.Rational(5, 2)*g**2*N**2-4*g*N**3/L**2+g**4*L**4/16,
]
