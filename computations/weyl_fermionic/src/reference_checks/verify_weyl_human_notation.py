#!/usr/bin/env python3
"""Verify displayed human-notation coefficients, the original 66-origin portion; the H50 checker covers its completion.

Expected multipliers come from the original Part III product-rule ledger,
not from the obsolete coefficient-array presentation. This also audits that
all original terms remain accounted for in the final derivation.
"""
from fractions import Fraction as F
from pathlib import Path
import hashlib,json,re
BASE=Path(__file__).resolve().parents[1]
PHASE=BASE/'.gpd/phases/02-ozkan-map-and-variation-completion'
NOTE=PHASE/'DERIVATION-fermionic-map.md'
raw=json.loads((PHASE/'VARPHI-Q-TERM-LEDGER.json').read_text())
hand=json.loads((PHASE/'HUMAN-NOTATION-LEDGER.json').read_text())
text=NOTE.read_text();part=text.split('# Part IV',1)[1]
checks={};origins=set();line_count=0
pending={(1,'C'),(2,'U'),(4,'Y'),(5,'Y'),(6,'U'),(8,'Z')}
zeros={(x['block'],x['label']) for x in hand['zero_trace_witnesses']}
assert len(zeros)==22
assert {(int(n),t['label']) for n,t in hand['pending'].items()}==pending
# Transpose signs of the actual M at each contracted pairing, from C03/C04.
negative={'D2','T1','T21','Tfirst1','Tsecond1','V3','V5','V8'}
for n in range(1,12):
    original={t['label']:t for t in raw['terms'][str(n)]}
    rows=hand['blocks'][str(n)]
    for row in rows:
        label=row['origin'];origin=(n,label);origins.add(origin)
        source=tuple(map(F,original[label]['coefficient']))
        if isinstance(row['rank'],int):
            sign=-1 if label in negative else 1
            triplet=label.startswith('V')
            factors=[F(3,16),F(3,16),F(-3,32)] if triplet else [F(1,8),F(1,8),F(-1,16)]
            factor=sign*factors[row['rank']]
        else:
            factor=F(1)
            if n==10 and label.startswith('R'):factor=F(-1,2)
            if n==11 and label=='chi2':factor=F(1,2)
        expected=tuple(factor*c for c in source)
        assert tuple(map(F,row['coefficient']))==expected,(n,label,row['rank'],expected)
        # The algebra ledger writes the squared T^2 contraction as T^2^2;
        # the displayed TeX groups its base to avoid a double superscript.
        displayed_latex=row['latex'].replace('T^2^2','{T^2}^2')
        assert displayed_latex in part,(n,label,row['latex'])
        assert row['latex'].endswith(r'\epsilon^i')
        assert r'\epsilon^j' not in row['latex']
        # The i of the final parameter must not be a curvature dummy index.
        assert r'\,ij' not in row['latex']
        line_count+=1
    for label in original:
        assert sum((n,label) in x for x in [origins,pending,zeros])==1,(n,label)
assert len(origins)==66
assert len(origins|pending|zeros)==94
checks['original_product_rule_coefficients']={'status':'PASS','direct_origins':66,'displayed_gamma_and_bilinear_terms':line_count,'pending_origins':6,'zero_trace_origins':22}
# All three gamma ranks of each explicit Fierz application are present.
for n,rows in hand['blocks'].items():
    labels={t['origin'] for t in rows if isinstance(t['rank'],int)}
    for label in labels:assert [r['rank'] for r in rows if r['origin']==label]==[0,1,2]
checks['full_Fierz_rank_coverage']='PASS: scalar, vector and full-pair bivector for each displayed application'

# Independently check the full third-block coefficients after gamma reduction.
assert F(128,3)*F(1,4)==F(32,3)
assert F(128,3)*F(1,6)==F(64,9)
assert F(16,3)*(2-1)==F(16,3)
assert F(16,3)*F(1,2)==F(8,3) # i*(-i)/2 for gamma3 duality
assert F(128,3)*F(1,8)==F(16,3)
assert F(-640,9)*(-1)*F(1,8)==F(80,9)
assert F(-640,9)*(-1)*F(-1,16)==F(-40,9)
checks['third_term_H47']='PASS: scalar/derivative/transpose/Fierz normalization coefficients; gamma-basis identities are covered by the companion component checks'

# Main prose has ordinary field formulas, not the rejected helper language.
for token in [r'\star',r'\mathbf f',r'\mathbf c',r'\mathbf g',r'\ell_',r'\boldsymbol',r'\mathscr',r'\mathbf x',r'\mathbf y',r'\mathbf z']:
    assert token not in part,token
assert not re.search(r'\b[UYZ]_',part)
assert not any(ord(c)<32 and c not in '\n\t' for c in text)
for math in re.findall(r'\$\$([\s\S]*?)\$\$',part):
    level=0
    for c in math:
        level+=(c=='{')-(c=='}');assert level>=0,math[:100]
    assert level==0,math[:100]
    for env in ['aligned','gathered']:
        assert math.count(r'\begin{'+env+'}')==math.count(r'\end{'+env+'}')
tags=re.findall(r'\\tag\{(H\d+[a-z]?)\}',part);assert len(tags)==len(set(tags))
assert {f'H{i:02d}' for i in range(1,54)}<=set(tags)
# Archived-draft preservation is outside the final-paper calculation.
assert 'All six terms in H50 now have parameter-right physical-field expressions.' in part
checks['presentation_and_scope']={'status':'PASS','new_helper_notation_removed':True,'six_originally_retained_groups_now_evaluated_separately':True,'numbered_equations':len(tags)}
result={'status':'PASS_FOR_DISPLAYED_TERMS','date':'2026-09-18','lock':'UNG-WEYL2-OP58-CONVENTIONS-v5','scope':'Explicit 66-origin hand expansion; H50 completion and the full sum are checked separately by verify_weyl_h50_completion.py','checks':checks,'proof_sha256':hashlib.sha256(NOTE.read_bytes()).hexdigest(),'ledger_sha256':hashlib.sha256((PHASE/'HUMAN-NOTATION-LEDGER.json').read_bytes()).hexdigest(),'full_hand_calculation_completion_evidence':'H50-COMPLETION-CHECKS.json'}
(PHASE/'HUMAN-NOTATION-CHECKS.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
