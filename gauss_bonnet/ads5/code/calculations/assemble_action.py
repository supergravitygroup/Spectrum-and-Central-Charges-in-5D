#!/usr/bin/env python3
"""Exact rational assembly of the component action.

Reading guide: derivations/action/full_action.md, GB01 and GB16–GB20.
Inputs are included in inputs/action_sources/; outputs go only to outputs/. This script
only distributes constant coefficients, applies the explicitly listed source
gauge/fermion projection, and typesets the complete collected endpoint.
"""
import argparse
from collections import Counter
from fractions import Fraction as Fraction
import hashlib
import json
from pathlib import Path
import re

BASE = Path(__file__).resolve().parents[1]
WORK = BASE / 'inputs'


def sha(data):
    return hashlib.sha256(data).hexdigest()


def read_action_inputs():
    manifest = json.loads((WORK / 'action_sources.json').read_text())
    texts = {}
    for entry in manifest:
        data = (BASE / entry['path']).read_bytes()
        assert sha(data) == entry['sha256'], entry['path']
        texts[entry['original']] = data.decode()
    return texts


def normalize_latex(s):
    s = re.sub(r'\\hspace\{[^}]*\}', '', s)
    s = re.sub(r'\\\\(?:\[[^]]*\])?', '', s)
    s = s.replace('&', '').replace(r'\,', '').replace(r'\!', '')
    s = s.replace(r'\quad', '').replace(r'\qquad', '')
    # A space terminating a TeX control word is semantic: removing the space
    # in \mathcal D, \widehat G, or \mu k creates a different command.
    s = re.sub(r'(\\[A-Za-z]+)\s+(?=[A-Za-z])', r'\1@@SPACE@@', s)
    return re.sub(r'\s+', '', s).replace('@@SPACE@@', ' ')


def split_sum(s):
    depth = 0
    start = 0
    result = []
    for i, char in enumerate(s):
        if char in '{[(':
            depth += 1
        elif char in '}])':
            depth -= 1
        assert depth >= 0, s[max(0, i-50):i+50]
        if char in '+-' and depth == 0 and i > start:
            result.append(s[start:i])
            start = i
    result.append(s[start:])
    assert depth == 0
    return result


def read_tex_atom(s):
    if s[0] == '{':
        end = s.index('}')
        return s[1:end], s[end+1:]
    return s[:1], s[1:]


def parse_coefficient(s):
    sign = -1 if s.startswith('-') else 1
    s = s.lstrip('+-')
    phase = 0
    if s.startswith(r'\frac'):
        numerator, s = read_tex_atom(s[5:])
        denominator, s = read_tex_atom(s)
        if 'i' in numerator:
            phase = 1
            numerator = numerator.replace('i', '') or '1'
        value = Fraction(numerator) / Fraction(denominator)
    else:
        match = re.match(r'\d+', s)
        value = Fraction(match[0]) if match else Fraction(1)
        if match:
            s = s[len(match[0]):]
    if s.startswith('i'):
        phase += 1
        s = s[1:]
    return sign * value * (-1)**(phase//2), phase % 2, s


def format_coefficient(co, phase=0):
    sign = '-' if co < 0 else '+'
    co = abs(co)
    if co.denominator == 1:
        number = '' if co == 1 else str(co.numerator)
        return sign + number + ('i' if phase else '')
    numerator = ('' if co.numerator == 1 and phase else str(co.numerator)) + ('i' if phase else '')
    return sign + r'\frac{' + numerator + '}{' + str(co.denominator) + '}'


def read_log_terms(text, group):
    rows = []
    for block in display_blocks(text):
        equation = block.split(r'\begin{aligned}', 1)[1].split(r'\end{aligned}', 1)[0]
        equation = normalize_latex(equation)
        if '=' in equation:
            equation = equation.split('=', 1)[1].removeprefix('{}')
        for term in split_sum(equation):
            co, phase, body = parse_coefficient(term)
            rows.append({'source': group, 'index': len(rows)+1,
                         'input_coefficient': str(co), 'phase_i': phase,
                         'factor': '-4', 'coefficient': str(-4*co), 'body': body})
    return rows


def standardize_display_names(body):
    # Explicit notational identifications: independent compensator suffix c
    # is suppressed in the entire displayed action; no field rescaling.
    body = body.replace(r'\varphi_c', r'\varphi').replace('L_c', 'L').replace('N_c', 'N')
    body = body.replace(r'\epsilon{}', r'\varepsilon{}')
    # Empty index carriers are required when upper/lower slots alternate;
    # preserve them so mixed tensors do not acquire double-script errors.
    for _ in range(5):
        body = re.sub(r'\^\{([a-z]+)\}\^\{([a-z]+)\}', r'^{\1\2}', body)
        body = re.sub(r'_\{([a-z]+)\}_\{([a-z]+)\}', r'_{\1\2}', body)
    return body


def display_blocks(text):
    """Read both archived dollar wrappers and GitHub-protected math fences."""
    return [a or b for a, b in re.findall(
        r'\$\$(.*?)\$\$|^ {0,3}```math[ \t]*\n(.*?)^ {0,3}```[ \t]*$',
        text, re.M | re.S,
    )]


def find_tagged_equation(text, tag):
    for block in display_blocks(text):
        if r'\tag{' + tag + '}' in block:
            return block
    raise ValueError(tag)


def expand_two_derivative_spinor(text):
    block = find_tagged_equation(text, '5.10')
    block = block.split(r'\begin{aligned}', 1)[1].split(r'\end{aligned}', 1)[0]
    block = block.split(r'\doteq', 1)[1]
    block = block[:block.rindex(r'+O(\text{four fermions})')]
    # Expand the one remaining composite-spinor symbol using the complete
    # raised spinor explicitly displayed in the donor's (5.5).
    spinor = find_tagged_equation(text, '5.5').split(r'\begin{aligned}', 1)[1].split(r'\end{aligned}', 1)[0]
    spinor = normalize_latex(spinor).removesuffix('.')
    block = normalize_latex(block)
    old = r'\varepsilon^{ir}\lambda_{\mathrm{linear}\,r}\big|_{\mathrm P}'
    old = normalize_latex(old)
    assert block.count(old) == 1, 'Expected one factored Majorana-bar slot'
    block = block.replace(old, spinor)
    assert r'\lambda_{\mathrm{linear}' not in block
    assert r'\mathcal L' not in block
    # Reflow in short runs using original source line boundaries, preserving
    # all grouping. For this single nested expression use term-sign breaks
    # only outside TeX index braces, with a soft width target.
    out = []
    start = 0
    depth = 0
    for i, char in enumerate(block):
        if char == '{' and (i == 0 or block[i-1] != '\\'):
            depth += 1
        elif char == '}' and (i == 0 or block[i-1] != '\\'):
            depth -= 1
        if char in '+-' and depth == 0 and i-start > 250:
            out.append(block[start:i])
            start = i
    out.append(block[start:])
    return '\\\\\n&'.join(out)


def assemble_action():
    texts = read_action_inputs()
    weyl_path = 'results/ungauged_full_fermionic_weyl2/.gpd/phases/03-full-ungauged-fermionic-invariant/GAUGED-ACTION-LEDGER.json'
    ledger = json.loads(texts[weyl_path])
    rows = []
    removed = []
    for name in ledger['order']:
        for i, ((co, phase), body) in enumerate(ledger['blocks'][name], 1):
            reason = None
            if name in ('dilatino', 'gravitino_dilatino') or (name == 'Y' and i <= 3):
                reason = 'undifferentiated gauge-fixed dilatino'
            if name in ('two_gravitinos', 'C_two_gravitinos') and i <= 2:
                reason = 'four explicit physical fermions'
            if reason:
                removed.append({'source': name, 'index': i, 'reason': reason,
                                'input_coefficient': co, 'phase_i': phase,
                                'body': body})
                continue
            body = body.replace(r'\sigma^{-1}', '').replace(r'\sigma', '').strip()
            rows.append({'source': 'Weyl_'+name, 'index': i,
                         'input_coefficient': co, 'phase_i': phase, 'factor': '-2',
                         'coefficient': str(-2*Fraction(co)), 'body': body})
    assert len(rows) == 52 and len(removed) == 21
    weyl = list(rows)
    log_seed = read_log_terms(texts['results/twoder_plus_log_spectrum/fermionic_workings/covariant_seed.md'], 'LOG_seed')
    log_explicit = read_log_terms(texts['results/twoder_plus_log_spectrum/fermionic_workings/explicit_sum.md'], 'LOG_explicit')
    assert len(log_seed) == 297 and len(log_explicit) == 835
    rows += log_seed + log_explicit
    rendered = [format_coefficient(Fraction(r['coefficient']), r['phase_i']) + standardize_display_names(r['body']) for r in rows]
    higher = '\\\\\n&'.join(' '.join(rendered[i:i+2]) for i in range(0, len(rendered), 2))
    two = expand_two_derivative_spinor(texts['results/gauged_two_derivative_fermionic_action/05_gauged_two_derivative_full_fermionic_action_from_1608_map.md'])
    final = ('```math\n\\fbox{$\\displaystyle{\\begin{aligned}\n'
             r'\ell_{\mathrm{tot}}^{(0+2)}\doteq\Bigg[&' + two + '\\\\[3pt]\n&'
             r'+\lambda_{\mathrm{GB}}\Bigg(' + higher + '\n'
             r'\Bigg)\Bigg]_{\le2}.' + '\n'
             r'\end{aligned}}$}\tag{GB-FINAL-DENSITY}' + '\n```\n')
    template = (BASE.parents[1] / 'action/details/gb_splus_construction.md').read_text()
    assert template.count('<!-- COLLECTED_ACTION -->') == 1
    document = template.replace('<!-- COLLECTED_ACTION -->', final)
    # A complete source coefficient ledger supplies every multiplication,
    # including the covariant seed that carries implicit two-fermion terms.
    audit = '# Every four-derivative coefficient multiplication\n\n'
    audit += 'The physical derivation and complete endpoint are in [the action](action.md). '
    audit += 'Each row preserves the source tensor body and spinor order; only the written rational factor is multiplied. '
    audit += 'An i in the source coefficient is retained by the linear Majorana convention.\n\n'
    audit += '| Input and term | Coefficient calculation | Unchanged field expression |\n|---|---|---|\n'
    for r in rows:
        input_co = format_coefficient(Fraction(r['input_coefficient']), r['phase_i']).removeprefix('+')
        output_co = format_coefficient(Fraction(r['coefficient']), r['phase_i']).removeprefix('+')
        if not input_co:
            input_co = '1'
        if not output_co:
            output_co = '1'
        if input_co == '-':
            input_co = '-1'
        if output_co == '-':
            output_co = '-1'
        audit += ('| ' + r['source'] + ' ' + str(r['index']) + ' | $`('
                  + r['factor'] + ')(' + input_co + ')=' + output_co + '`$ | $`'
                  + standardize_display_names(r['body']) + '`$ |\n')
    audit += '\n## Every discarded Weyl term\n\n'
    audit += ('The following are all 21 omitted source entries. In the first 17, '
              'the displayed undifferentiated dilatino is zero in the source gauge. '
              'The last four contain two gravitinos and two additional odd '
              'covariants, so their projection to physical degree at most two '
              'vanishes. No equation of motion is used.\n\n')
    audit += '| Source entry | Explicit vanishing expression | Reason |\n|---|---|---|\n'
    for r in removed:
        expression = format_coefficient(-2*Fraction(r['input_coefficient']), r['phase_i']) + standardize_display_names(r['body'])
        audit += ('| Weyl ' + r['source'] + ' ' + str(r['index']) + r' | $`\left['
                  + expression + r'\right]_{\mathrm P,\le2}=0`$ | ' + r['reason'] + ' |\n')
    report = {'status': 'PASS_INHERITED_ACTION_ASSEMBLY',
              'scope': 'Exact linear combination of adopted input densities through two physical fermions; not independent Weyl multiplet certification',
              'counts': {'weyl_input': 73, 'weyl_retained': 52, 'weyl_gauge_zero': 17,
                         'weyl_explicit_four_fermi': 4, 'log_covariant_seed': 297,
                         'log_explicit_bilinears': 835, 'four_derivative_outer_terms': len(rows)},
              'normalizations': {'Weyl_OP': '-2', 'LOG': '-4', 'two_derivative': 'unchanged existing Gold-frame action'},
              'fermion_order': '0 and 2, with the physical-degree projection outside every full covariant',
              'source_gauge': 'sigma=1,b=0,dilatino=0,Lij=deltaij L/sqrt2 after ordered differentiation',
              'removed_weyl_terms': removed, 'source_blocks': dict(Counter(r['source'] for r in rows)),
              'action_sha256': sha(final.encode()),
              'coefficients_sha256': sha(json.dumps(rows, sort_keys=True).encode()),
              'higher_fermions_certified': False, 'spectrum_certified': False}
    return {'action.md': final,
            'action_coefficient_ledger.md': audit,
            'action_coefficients.json': json.dumps(rows, indent=2) + '\n',
            'action_assembly.json': json.dumps(report, indent=2) + '\n'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    for name, content in assemble_action().items():
        target = BASE / 'outputs' / name
        if args.check:
            assert target.read_text() == content, name
        else:
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(content)
    print('PASS_INHERITED_ACTION_ASSEMBLY: 52 Weyl + 297 LOG covariant + 835 LOG explicit terms; full two-derivative input retained.')


if __name__ == '__main__':
    main()
