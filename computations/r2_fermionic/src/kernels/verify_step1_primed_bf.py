#!/usr/bin/env python3
"""Audit Step 1 distribution/order, weights, limits and epsilon identities.

This is not a supersymmetry proof, composite-map check, or R2-action verifier.
Spinor strings are ordered formal factors; no commuting-spinor substitution
or Fierz identity is used.
"""
from collections import defaultdict
from itertools import permutations
from pathlib import Path
import hashlib
import json
import re
import sympy as s

ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / 'notes/03_step1_full_primed_BF_density.md'


def main():
    checks = []

    def check(value, label):
        checks.append({'check': label, 'pass': bool(value)})

    # Formal noncommuting words retain the published factor ordering.
    Y, L, lb, v, pb, ga, lam, eps, A, dE, rho, N, gab, psi = s.symbols(
        'Yprime Lprime lambdabarprime varphiprime psibar gamma_a '
        'lambdaprime epsilon Aprime partial_E3prime rhoprime Nprime '
        'gamma_ab psi', commutative=False)
    grouped_source = (Y*L + s.I*lb*v - pb*ga*lam*L/2 - eps*A*dE/12
                      + rho*(N + pb*ga*v/2 + s.I*pb*gab*psi*L/4))
    # Independently transcribed in source order from note Eq. (16).
    words = [Y*L, lb*v, pb*ga*lam*L, eps*A*dE, rho*N,
             rho*pb*ga*v, rho*pb*gab*psi*L]
    coefficients = [s.S.One, s.I, -s.Rational(1, 2), -s.Rational(1, 12),
                    s.S.One, s.Rational(1, 2), s.I/4]
    assembled = sum(c*w for c, w in zip(coefficients, words))
    check(s.expand(grouped_source-assembled) == 0,
          'grouped source expands to all seven ordered words')
    for i, (c, w) in enumerate(zip(coefficients, words), 1):
        check(s.expand(grouped_source).coeff(w) == c,
              f'BF-{i:02d} exact coefficient with fermion order retained')

    weights = [[2, 3], [s.Rational(3, 2), s.Rational(7, 2)],
               [s.Rational(1, 2), s.Rational(3, 2), 3], [5, 0, 0], [1, 4],
               [1, s.Rational(1, 2), s.Rational(7, 2)],
               [1, s.Rational(1, 2), s.Rational(1, 2), 3]]
    for i, ww in enumerate(weights, 1):
        check(sum(ww) == 5, f'BF-{i:02d} Weyl weight five')
    check(all(n % 2 == 0 for n in [0, 2, 2, 0, 0, 2, 2]),
          'all terms Grassmann even')
    bosonic = assembled.subs({lb: 0, lam: 0, v: 0, pb: 0, psi: 0})
    check(s.expand(bosonic-(Y*L+rho*N-eps*A*dE/12)) == 0, 'bosonic limit')
    no_gravitino = assembled.subs({pb: 0, psi: 0})
    check(s.expand(no_gravitino-(Y*L+s.I*lb*v+rho*N-eps*A*dE/12)) == 0,
          'zero-gravitino limit retains matter fermions')
    check(assembled.subs({Y: 0, lb: 0, lam: 0, A: 0, rho: 0}) == 0,
          'identically zero vector argument')
    check(assembled.subs({L: 0, v: 0, dE: 0, N: 0}) == 0,
          'identically zero linear argument in zero-potential representative')

    # Independent exact contraction test: aggregate all 5! epsilon components
    # into formal monomials with a symmetric partial-derivative index pair.
    # No random field values and no gamma representation are needed.
    for pair in [(0, 1), (1, 2), (1, 3), (1, 4)]:
        residual = defaultdict(int)
        for p in permutations(range(5)):
            inversions = sum(p[i] > p[j] for i in range(5) for j in range(i+1, 5))
            key = (tuple(sorted((p[pair[0]], p[pair[1]]))),
                   tuple(p[i] for i in range(5) if i not in pair))
            residual[key] += (-1)**inversions
        check(all(c == 0 for c in residual.values()),
              f'120-term epsilon contraction vanishes for symmetric pair {pair}')

    text = DOC.read_text()
    final = text.split('## 6. Final Result', 1)[1].split('## 7.', 1)[0]
    formula = re.search(r'\$\$\s*(.*?)\s*\$\$', final, re.S).group(1)
    normalized = re.sub(r'\s+', '', formula)
    expected_terms = [r"L'_{ij}Y'^{ij}", r"\rho'N'", r"i\bar\lambda'\varphi'",
        r"-\frac12\bar\psi_a{}^i\gamma^a\lambda'^jL'_{ij}",
        r"-\frac1{12}\varepsilon^{\mu\nu\rho\sigma\tau}A'_\mu\partial_\nuE'_{\rho\sigma\tau}",
        r"\frac12\rho'\bar\psi_a\gamma^a\varphi'",
        r"\fraci4\rho'\bar\psi_a{}^i\gamma^{ab}\psi_b{}^jL'_{ij}"]
    for i, term in enumerate(expected_terms, 1):
        check(normalized.count(term) == 1, f'final Markdown term {i} occurs exactly once')
    check(r"\psi'" not in formula and r"\bar\psi'" not in formula,
          'gravitino remains unprimed')
    check(not any(x in text for x in [r'\[', r'\]', r'\(', r'\)']),
          'dollar math delimiters only')
    for title in ['Problem and Target', 'Convention Ledger',
                  'Definitions and Required Identities', 'Detailed Derivation',
                  'Consistency Checks', 'Final Result',
                  'Convention Dependence and Remaining Uncertainties']:
        check(bool(re.search(r'^## \d\. '+re.escape(title)+r'$', text, re.M)),
              'required section: '+title)
    tags = re.findall(r'\\tag\{(\d+)\}', text)
    check(tags == [str(i) for i in range(1, 26)], '25 consecutive equation numbers')
    failures = [c['check'] for c in checks if not c['pass']]
    report = {
        'status': 'FAIL' if failures else 'PASS',
        'scope': 'Step 1 BF transcription, distribution, ordering, weights and stated form identities only',
        'not_checked': ['full local supersymmetry', 'Hermitian conjugation of source density',
                        'mixed vector-to-linear map', 'vector composite maps',
                        'full gauged R2 action or spectrum'],
        'result_lock': 'R2-PRIMED-BF-DENSITY-v1',
        'document': str(DOC.relative_to(ROOT)),
        'document_sha256': hashlib.sha256(DOC.read_bytes()).hexdigest(),
        'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'sympy_version': s.__version__, 'checks': len(checks),
        'failures': failures, 'details': checks}
    (ROOT/'build/step1_primed_bf_verification.json').write_text(json.dumps(report, indent=2)+'\n')
    print(f"{report['status']}: {len(checks)} Step 1 checks; no composite maps evaluated.")
    for f in failures:
        print('FAIL:', f)
    return bool(failures)


if __name__ == '__main__':
    raise SystemExit(main())
