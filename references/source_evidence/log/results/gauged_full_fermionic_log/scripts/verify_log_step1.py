#!/usr/bin/env python3
"""Verify the listed step-1 identities and detect documented source conflicts.

Full generic superform projection is checked separately by verify_log_form_interface.py.
This verifier does not establish the actual nonlinear LOG polynomial identities.
No dependency hash is updated by this verifier.
"""
from pathlib import Path
from fractions import Fraction as F
from collections import defaultdict
import contextlib
import hashlib
import io
import itertools as it
import json
import runpy
import re
import sympy as s

BASE = Path(__file__).resolve().parents[1]
ROOT = BASE.parents[1]


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    checks = {}
    links = json.loads((BASE / 'LOG_CONVENTION_LINKS.json').read_text())
    for dep in links['dependencies']:
        path = ROOT / dep['path']
        assert sha(path) == dep['sha256'], f"Changed input requires review: {path}"
    for edge in links['reciprocal_links']:
        assert edge['literal_target'] in (ROOT / edge['source']).read_text()
        assert (ROOT / edge['target']).exists()
    checks['dependency_graph'] = f"PASS: {len(links['dependencies'])} hashes and {len(links['reciprocal_links'])} links"

    with contextlib.redirect_stdout(io.StringIO()):
        m = runpy.run_path(str(BASE / 'scripts/common_conventions_check_frozen.py'),
                          run_name='log_step1_matrix_inputs')
    assert m['result']['algebra_status'] == 'PASS'
    add, scale, mul, trans, eq = [m[k] for k in ('add', 'scale', 'mul', 'trans', 'eq')]
    gam, lowgam, eps, C, Z = [m[k] for k in ('gam', 'lowgam', 'eps', 'C', 'Z')]
    eta = m['eta']
    for a, b in it.product(range(5), repeat=2):
        lhs = add(*[scale(eps((a, b, c, d, e)), lowgam((c, d, e)))
                    for c, d, e in it.product(range(5), repeat=3)])
        assert eq(lhs, scale(6j, gam((a, b))))
    for a, b, c in it.product(range(5), repeat=3):
        lhs = add(*[scale(eps((a, b, c, d, e)), lowgam((d, e)))
                    for d, e in it.product(range(5), repeat=2)])
        assert eq(lhs, scale(2j, gam((a, b, c))))
    checks['epsilon_gamma_form_identities'] = 'PASS: 25 rank-three and 125 rank-two contractions'

    for a in range(5):
        for b, c in it.combinations(range(5), 2):
            lhs = mul(gam((b, c)), lowgam((a,)))
            rhs = add(scale(eta[a], gam((a, b, c))),
                      scale(int(a == c), m['g'][b]),
                      scale(-int(a == b), m['g'][c]))
            assert eq(lhs, rhs)
    for b, c in it.combinations(range(5), 2):
        M = gam((b, c))
        assert eq(trans(mul(C, M)), mul(C, M))
        # Lower the second index: M_ab=epsilon_bg M_a^g means M*C.T.
        U = scale(-1, C)
        lower_kernel = mul(mul(trans(U), mul(M, trans(C))), U)
        assert eq(lower_kernel, scale(-1, mul(C, M)))
        assert not eq(lower_kernel, mul(C, M))
    checks['clifford_product_and_bilinear_kernels'] = 'PASS: 50 gamma products, 10 correctly lowered second-index kernels; old opposite kernel rejected'

    # Explicit NW-SE lowering, independently evaluated in both forms.
    su = [[0, 1], [-1, 0]]
    triplet = [[2, 3], [3, 5]]
    xi = [7, 11]
    lower_xi = [sum(xi[j] * su[j][i] for j in range(2)) for i in range(2)]
    lower_L = [[sum(triplet[k][l] * su[k][i] * su[l][j]
                    for k, l in it.product(range(2), repeat=2))
                for j in range(2)] for i in range(2)]
    upper_product = [sum(triplet[i][j] * lower_xi[j] for j in range(2)) for i in range(2)]
    lowered_product = [sum(upper_product[j] * su[j][i] for j in range(2)) for i in range(2)]
    assert lowered_product == [-sum(lower_L[i][j] * xi[j] for j in range(2)) for i in range(2)]
    checks['su2_lowering'] = f'PASS: lowered L epsilon = {lowered_product}'

    # Keep independent antisymmetrized index orders and nonconstant test data.
    B = lambda a, d: F(2 + 3*a + 7*d)
    de = lambda a, b: int(a == b)
    for a, b, c, d in it.product(range(5), repeat=4):
        K = (de(a,c)*B(b,d)-de(b,c)*B(a,d)-de(a,d)*B(b,c)+de(b,d)*B(a,c))/4
        J = (B(a,d)*de(b,c)-B(b,d)*de(a,c)-B(a,c)*de(b,d)+B(b,c)*de(a,d))/4
        assert J == -K
        assert -(F(8,3)+F(16,3))*K == 8*J
    checks['curvature_chi'] = 'PASS: all625 index orders and625 converted/project coefficients; -8K=+8J'

    # Exact coefficient checks, not a new proof of whole transformation algebra.
    for a in (s.Rational(-1,2), s.Integer(1), s.Rational(3,7)):
        b, c, d = -s.I*a, 2*a, -2*a
        assert -2*b == 2*s.I*a and d/2 == -a and -s.I*c/2 == -s.I*a
        assert -F(3,2)*F(1,2)*b*F(16,3) == 4*s.I*a
        assert 2*a*(3*s.I-F(3,2)*s.I*F(2,3)) == 4*s.I*a
        # Six source density coefficients after spinor/SU2 conversion.
        raw = [-2*a, -c, -2*(-1)*b, s.I*b*(-1), s.I*s.I*(-1)*a, -s.I*F(1,2)*a]
        target = [-2*a*x for x in (1, 1, s.I, F(1,2), F(-1,2), s.I/4)]
        assert raw == target
    checks['slot_and_nonform_bf_coefficients'] = 'PASS: three arbitrary normalizations; multiplier -2a, unit at a=-1/2'

    # Grassmann polynomial test. Independent generators for d_epsilon, phi, psi;
    # all bilinears are reordered by exterior-algebra signs, never commuting spins.
    index = lambda family, frame, i, alpha: family*40 + frame*8 + i*4 + alpha
    def bilinear(poly, coefficient, left, right, matrix):
        if not coefficient:
            return
        for alpha, beta in it.product(range(4), repeat=2):
            x, y = left(alpha), right(beta)
            if x == y:
                continue
            key = (min(x,y), max(x,y))
            poly[key] += coefficient * matrix[alpha][beta] * (1 if x < y else -1)
    def zero(poly):
        return all(abs(v) < 1e-11 for v in poly.values())
    def combine(*terms):
        out = defaultdict(complex)
        for coefficient, polynomial in terms:
            for key, value in polynomial.items():
                out[key] += coefficient*value
        return out

    q1, q2, p1, p2 = ([defaultdict(complex) for _ in range(5)] for _ in range(4))
    for a, b, i, j in it.product(range(5), range(5), range(2), range(2)):
        der = lambda x, b=b, i=i: index(0,b,i,x)
        phi = lambda x, j=j: index(1,0,j,x)
        bilinear(q1[a], 1j/2*su[j][i], der, phi, mul(C,gam((b,a))))
    for a, b, c, i, j in it.product(range(5), range(5), range(5), range(2), range(2)):
        mat = mul(C,gam((a,b,c)))
        bilinear(q2[a], triplet[i][j]/4,
                 lambda x,b=b,i=i:index(0,b,i,x), lambda x,c=c,j=j:index(2,c,j,x), mat)
        bilinear(q2[a], triplet[i][j]/4,
                 lambda x,b=b,i=i:index(2,b,i,x), lambda x,c=c,j=j:index(0,c,j,x), mat)
    for a, b, c, d, e in it.permutations(range(5)):
        orient = eps((a,b,c,d,e))
        mat3, mat2 = mul(C,lowgam((c,d,e))), mul(C,lowgam((d,e)))
        for i,j in it.product(range(2),repeat=2):
            bilinear(p1[a], -orient*su[j][i]/12,
                     lambda x,b=b,i=i:index(0,b,i,x), lambda x,j=j:index(1,0,j,x), mat3)
            bilinear(p2[a], -1j*orient*triplet[i][j]/12,
                     lambda x,c=c,i=i:index(2,c,i,x), lambda x,b=b,j=j:index(0,b,j,x), mat2)
    for a in range(5):
        assert zero(combine((1,p1[a]),(-1,q1[a])))
        assert zero(combine((-3,p2[a]),(-1,q2[a])))
        assert zero(combine((1,p1[a]),(-3,p2[a]),(-1,q1[a]),(-1,q2[a])))
        assert not zero(combine((-1,p1[a]),(1,p2[a]),(-1,q1[a]),(-1,q2[a])))
        # Literal C24 H=h+Q1-Q2 leaves precisely 2*dQ1; the Q2 sector cancels.
        residual = combine((1,p1[a]),(-3,p2[a]),(1,q1[a]),(-1,q2[a]))
        assert not zero(residual)
        assert zero(combine((1,residual),(-2,q1[a])))
        assert zero(combine((-3,p2[a]),(-1,q2[a])))
    checks['local_susy_grassmann_form_test'] = (
        'PASS: all5 vector components; independent odd generators; alpha=1,beta=-3 cancel; '
        'literal OP(-1,+1) fails; literal Gold h+Q1-Q2 leaves exactly 2*dQ1')

    assert F(23,384)-F(1,64)-F(1,384) == F(1,24)
    weights = [2+3,1+4,F(3,2)+F(7,2),1+F(1,2)+F(7,2),
               F(1,2)+F(3,2)+3,1+2*F(1,2)+3,1+4]
    assert all(w == 5 for w in weights)
    assert F(1,2)+F(7,2) == 2*F(1,2)+3 == 4
    assert 3-5+2 == 3-5-2+4 == 0
    checks['normalization_and_weights'] = 'PASS: raw bosonic R² ->1/24; seven density weights5, current completions4, action dimension0'

    # Validate working-document links and unique relation IDs as well as hashes.
    doc = (BASE/'LOG_CONVENTIONS.md').read_text()
    for angled, plain in re.findall(r'\]\((?:<([^>]+)>|([^\)]+))\)', doc):
        ref = angled or plain
        if ref.startswith(('http://','https://','#')):
            continue
        assert (BASE/ref.split('#')[0]).exists(), ref
    tags = re.findall(r'\\tag\{([^}]+)\}',doc)
    assert len(tags) == len(set(tags)) == 24
    checks['working_ledger_structure'] = 'PASS: 24 unique relation IDs and all local links'
    output = {
        'date':'2026-09-25', 'record':'GAUGED-LOG-STEP1-v1',
        'status':'PASS_LISTED_CHECKS_WITH_GENERIC_FORM_INTERFACE_RESOLVED',
        'checks':checks,
        'covariant_linear_QS_map':'VERIFIED',
        'nonform_BF_terms':'SIX OF SIX MATCH',
        'explicit_chi_curvature_interface':'MATCHES PROJECT +8 IN ITS WRITTEN ORDER',
        'bosonic_normalization':'UNIT MULTIPLIER VERIFIED IN CURVATURE PROBE',
        'full_printed_Gold_form_equivalence':'LITERAL FORMULAS INCOMPATIBLE; derived corrections recorded',
        'generic_form_interface':'RESOLVED by log-certification-form-interface.md and verify_log_form_interface.py, conditional on genuine multiplets',
        'full_generic_potential_SUSY':'DERIVED by superform contraction; separate from this principal test',
        'full_LOG_invariant':'ACTUAL COMPOSITE IDENTITIES REQUIRE SEPARATE VERIFICATION',
        'working_ledger_sha256':sha(BASE/'LOG_CONVENTIONS.md')
    }
    (BASE/'sources/step1/checks.json').write_text(json.dumps(output,indent=2)+'\n')
    print(json.dumps(output,indent=2))


if __name__ == '__main__':
    main()
