"""Independent read-back audit; does not import or execute the assembler."""
from collections import Counter
from fractions import Fraction as Fraction
import hashlib
import json
from pathlib import Path
import re

def check(name, condition):
    if not condition:
        failures.append(name)

def latex_tokens(s):
    s = re.sub('\\\\hspace\\{[^}]*\\}', '', s)
    s = re.sub('\\\\\\\\(?:\\[[^\\]]*\\])?', '', s)
    s = s.replace('&', '')
    return [t for t in re.findall('\\\\[A-Za-z]+|\\\\.|[^\\s]', s) if t not in ('\\,', '\\!', '\\quad', '\\qquad')]

def normalize_field_names(s):
    return s.replace('\\varphi_c', '\\varphi').replace('L_c', 'L').replace('N_c', 'N').replace('\\epsilon{}', '\\varepsilon{}')

def split_additive_terms(s):
    result, start, depth = ([], 0, 0)
    for pos, char in enumerate(s):
        if char in '{[(':
            depth += 1
        elif char in '}])':
            depth -= 1
        if char in '+-' and depth == 0 and (pos > start):
            result.append(s[start:pos])
            start = pos
    result.append(s[start:])
    assert depth == 0
    return result

def read_coefficient_and_body(s):
    s = s.strip()
    sign = -1 if s.startswith('-') else 1
    s = s.lstrip('+-')
    if s.startswith('\\frac'):
        match = re.match('\\\\frac(?:\\{(\\d*i?)\\}|(\\d))(?:\\{(\\d+)\\}|(\\d))', s)
        assert match, s[:70]
        num, den = (match[1] or match[2], match[3] or match[4])
        phase = int('i' in num)
        coef = Fraction(int(num.replace('i', '') or '1'), int(den))
        s = s[match.end():]
    else:
        match = re.match('(\\d*)(i?)', s)
        coef, phase = (Fraction(int(match[1] or '1')), int(bool(match[2])))
        s = s[match.end():]
    if s.startswith('i'):
        phase += 1
        s = s[1:]
    return (sign * coef * (-1) ** (phase // 2), phase % 2, tuple(latex_tokens(normalize_field_names(s))))

def read_log_source(text):
    output = []
    for block in display_blocks(text):
        body = block.split('\\begin{aligned}')[1].split('\\end{aligned}')[0]
        body = re.sub('\\\\\\\\(?:\\[[^\\]]*\\])?', '', body).replace('&', '')
        body = re.sub('\\\\hspace\\{[^}]*\\}', '', body)
        body = re.sub('(\\\\[A-Za-z]+)\\s+(?=[A-Za-z])', '\\1@@S@@', body)
        body = re.sub('\\s+', '', body).replace('@@S@@', ' ')
        body = body.replace('\\,', '').replace('\\!', '').replace('\\quad', '').replace('\\qquad', '')
        if '=' in body:
            body = body.split('=', 1)[1].removeprefix('{}')
        output.extend((read_coefficient_and_body(t) for t in split_additive_terms(body)))
    return output

def display_blocks(text):
    return [a or b for a, b in re.findall(
        r'\$\$(.*?)\$\$|^ {0,3}```math[ \t]*\n(.*?)^ {0,3}```[ \t]*$',
        text, re.M | re.S,
    )]

def find_equation(text, name):
    return next(x for x in display_blocks(text) if '\\tag{' + name + '}' in x)
BASE = Path(__file__).resolve().parents[1]
failures = []

def main():
    failures.clear()
    manifest = json.loads((BASE / 'inputs/action_sources.json').read_text())
    sources = {}
    for item in manifest:
        snapshot = (BASE / item['path']).read_bytes()
        check('snapshot ' + item['original'], hashlib.sha256(snapshot).hexdigest() == item['sha256'])
        sources[item['original']] = snapshot.decode()
    weyl = json.loads(sources['results/ungauged_full_fermionic_weyl2/.gpd/phases/03-full-ungauged-fermionic-invariant/GAUGED-ACTION-LEDGER.json'])
    expected = []
    for block in weyl['order']:
        for index, (coefficient, body) in enumerate(weyl['blocks'][block], 1):
            if block in ('dilatino', 'gravitino_dilatino'):
                continue
            if block == 'Y' and index <= 3:
                continue
            if block in ('two_gravitinos', 'C_two_gravitinos') and index <= 2:
                continue
            co, phase = coefficient
            body = body.replace('\\sigma^{-1}', '').replace('\\sigma', '')
            expected.append((-2 * Fraction(co), phase, tuple(latex_tokens(normalize_field_names(body)))))
    check('52 retained Weyl', len(expected) == 52)
    for name, number in [('covariant_seed', 297), ('explicit_sum', 835)]:
        rows = read_log_source(sources['results/twoder_plus_log_spectrum/fermionic_workings/' + name + '.md'])
        check(name + ' count', len(rows) == number)
        expected.extend(((-4 * co, phase, body) for co, phase, body in rows))
    doc = (BASE / 'outputs/action.md').read_text()
    endpoint = find_equation(doc, 'GB-FINAL-DENSITY')
    prefix, higher = endpoint.split('+\\lambda_{\\mathrm{GB}}\\Bigg(', 1)
    higher = higher.split('\\Bigg)\\Bigg]_{\\le2}', 1)[0]
    higher = re.sub('\\\\\\\\(?:\\[[^\\]]*\\])?', '', higher).replace('&', '')
    actual = [read_coefficient_and_body(t) for t in split_additive_terms(higher)]
    check('1184 output terms', len(actual) == 1184)
    check('every output coefficient, phase and tensor body matches source', actual == expected)
    two = sources['results/gauged_two_derivative_fermionic_action/05_gauged_two_derivative_full_fermionic_action_from_1608_map.md']
    seed = find_equation(two, '5.10').split('\\doteq', 1)[1].split('+O(\\text{four fermions})')[0]
    spinor = find_equation(two, '5.5').split('\\begin{aligned}', 1)[1].split('\\end{aligned}')[0]
    seed_tokens, spinor_tokens = (latex_tokens(seed), latex_tokens(spinor))
    if spinor_tokens[-1] == '.':
        spinor_tokens.pop()
    needle = latex_tokens('\\varepsilon^{ir}\\lambda_{\\mathrm{linear}\\,r}\\big|_{\\mathrm P}')
    hits = [i for i in range(len(seed_tokens) - len(needle) + 1) if seed_tokens[i:i + len(needle)] == needle]
    check('exactly one composite bar slot', len(hits) == 1)
    if hits:
        i = hits[0]
        seed_tokens[i:i + len(needle)] = spinor_tokens
    emitted_two = prefix.split('\\doteq\\Bigg[&', 1)[1]
    check('all two-derivative TeX tokens and bar scope preserved', latex_tokens(emitted_two) == seed_tokens)
    check('no unexpanded linear spinor slot', '\\lambda_{\\mathrm{linear}' not in endpoint)
    check('physical-order projection at endpoint', '\\Bigg)\\Bigg]_{\\le2}' in endpoint)
    curv_w = (Fraction(1, 8), -Fraction(1, 6), Fraction(1, 24))
    curv_log = (Fraction(0), -Fraction(1, 6), Fraction(1, 24))
    curv = tuple((-2 * a - 4 * b for a, b in zip(curv_w, curv_log)))
    check('GB curvature normalization', curv == (-Fraction(1, 4), Fraction(1), -Fraction(1, 4)))
    check('conformal spinor primary coefficient', -Fraction(1, 2) * -Fraction(1, 2) == Fraction(1, 4))
    check('bosonic derivative reordering', Fraction(160, 3) - Fraction(256, 3) / 2 == Fraction(32, 3))
    check('T^4 trace', -Fraction(81, 32) * Fraction(16, 3) ** 4 == -2048)
    check('(T^2)^2', Fraction(33, 128) * Fraction(16, 3) ** 4 == Fraction(5632, 27))
    check('R(V)^2 cancellation', -2 * -Fraction(1, 3) - 4 * Fraction(1, 6) == 0)
    check('gravitational CS', -2 * Fraction(1, 16) == -Fraction(1, 8))
    check('SU2 CS', -2 * -Fraction(1, 12) - 4 * -Fraction(1, 12) == Fraction(1, 2))
    check('action dimension', 3 - 5 + 2 == 0 and 4 - 2 == 2)
    fingerprints = []
    for probe in (7, 17, 31):

        def evaluate(rows):
            result = [Fraction(0), Fraction(0)]
            for co, phase, body in rows:
                digest = hashlib.sha256((' '.join(body) + str(probe)).encode()).digest()
                value = Fraction(int.from_bytes(digest[:4], 'big') % 1009 - 504, probe)
                result[phase] += co * value
            return result
        left, right = (evaluate(expected), evaluate(actual))
        check('coefficient polynomial probe ' + str(probe), left == right)
        fingerprints.append({'probe': probe, 'real': str(right[0]), 'i_part': str(right[1]), 'match': left == right})
    assembly = json.loads((BASE / 'outputs/action_assembly.json').read_text())
    check('assembly action hash', assembly['action_sha256'] == hashlib.sha256(doc.encode()).hexdigest())
    report = {'status': 'PASS_INHERITED_ACTION_ASSEMBLY' if not failures else 'FAIL', 'scope': 'Independent source-to-rendered-action read-back, normalization arithmetic and polynomial coefficient transport; not full SUSY closure or a spectrum', 'included_frozen_inputs': len(manifest), 'four_derivative_terms_read_back': len(actual), 'two_derivative_tokens_compared': len(seed_tokens), 'all_coefficient_phase_and_tensor_bodies_preserved': actual == expected, 'curvature_coefficients': [str(x) for x in curv], 'coefficient_polynomial_probes': fingerprints, 'failures': failures, 'action_sha256': hashlib.sha256(doc.encode()).hexdigest()}
    (BASE / 'outputs/action_readback.json').write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps(report, indent=2))
    raise SystemExit(bool(failures))
if __name__ == '__main__':
    main()
