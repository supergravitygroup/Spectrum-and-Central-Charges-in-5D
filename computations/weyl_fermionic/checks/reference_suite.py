"""Run the retained Weyl component checks against the current source documents.

The restored checkers expect their original relative input layout. This adapter
stages the current documents and ledgers in a temporary directory; generated
check records never overwrite the repository's scientific outputs.
"""
from pathlib import Path
import argparse
import os
import re
import shutil
import subprocess
import sys
import tempfile
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
PHASE_2 = Path('.gpd/phases/02-ozkan-map-and-variation-completion')
PHASE_3 = Path('.gpd/phases/03-full-ungauged-fermionic-invariant')
CHECKS = (
    'verify_conventions',
    'verify_weyl_map_s_invariance',
    'verify_weyl_map_q_variation',
    'verify_weyl_spinor_q_variation',
    'verify_weyl_human_notation',
    'verify_weyl_h50_completion',
    'verify_weyl_clifford_collection',
    'verify_weyl_bivector_cancellation',
    'verify_weyl_scalar_canonicalization',
    'verify_weyl_vector_canonicalization',
    'verify_full_fermionic_map_anchor',
    'verify_weyl_action_substitution',
    'verify_gauged_weyl_action',
)


def stage_document(source, destination):
    """Adapt Markdown wrappers and links for the legacy temporary check layout."""
    def rebase(match):
        target = match.group(1).strip('<>')
        parsed = urlsplit(target)
        if parsed.scheme or parsed.netloc or not parsed.path:
            return match.group(0)
        return '](' + str((source.parent / unquote(parsed.path)).resolve()) + ')'
    destination.parent.mkdir(parents=True, exist_ok=True)
    text = re.sub(
        r'^ {0,3}```math[ \t]*\n(.*?)^ {0,3}```[ \t]*$',
        lambda m: '$$\n' + m[1] + '$$', source.read_text(), flags=re.M | re.S,
    )
    text = re.sub(r'\$`(.*?)`\$', lambda m: '$' + m[1] + '$', text, flags=re.S)
    destination.write_text(re.sub(r'\]\(([^)\n]+)\)', rebase, text))


def stage(workspace):
    for phase in (PHASE_2, PHASE_3):
        (workspace / phase).mkdir(parents=True)
    shutil.copytree(ROOT / 'src/reference_checks', workspace / 'scripts')
    for source in (ROOT / 'inputs/reference/notes').glob('*.md'):
        stage_document(source, workspace / 'notes' / source.name)
    stage_document(
        ROOT.parents[1] / 'weyl2/action/details/construction.md',
        workspace / 'notes/05_gauged_full_fermionic_weyl2_calculation.md',
    )
    documents = {
        '.gpd/CONVENTIONS.md': 'component_conventions.md',
        str(PHASE_2 / 'DERIVATION-fermionic-map.md'): 'fermionic-map.md',
        str(PHASE_3 / 'DERIVATION-full-fermionic-weyl2-action.md'): 'full-fermionic-weyl2-action.md',
    }
    for destination, source in documents.items():
        stage_document(ROOT / 'derivations' / source, workspace / destination)
    for source in (ROOT / 'inputs/component_ledgers').glob('*.json'):
        phase = PHASE_3 if source.name in {
            'ACTION-SUBSTITUTION-LEDGER.json', 'GAUGED-ACTION-LEDGER.json'
        } else PHASE_2
        shutil.copy2(source, workspace / phase / source.name)


def run(selected=CHECKS):
    if sys.flags.optimize:
        raise RuntimeError('Run without -O: the restored scientific checks use assertions.')
    environment = dict(os.environ, PYTHONDONTWRITEBYTECODE='1')
    with tempfile.TemporaryDirectory(prefix='weyl-component-checks-') as temporary:
        workspace = Path(temporary)
        stage(workspace)
        for name in selected:
            print(f'Checking {name}', flush=True)
            subprocess.run(
                [sys.executable, '-B', str(workspace / 'scripts' / (name + '.py'))],
                cwd=workspace, env=environment, check=True,
            )
    print(f'PASS {len(selected)} Weyl component check programs; current inputs preserved.')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='append', choices=CHECKS,
                        help='Run only this checker (repeatable).')
    args = parser.parse_args()
    run(tuple(args.check) if args.check else CHECKS)
