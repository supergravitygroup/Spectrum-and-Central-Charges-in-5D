"""Regenerate only this package's item-25 data; no spectrum roots are computed."""
import argparse
import json
import time
import numpy as np
import sympy as sp
from action import evaluate, gauge_columns, pack, basis_record, SECTORS
from sources import HERE, census, source_id

OUT = HERE/'outputs'
SAMPLES = [
    ('H2_3_2_s13', '3', '2', '1/3'),
    ('H2_3_2_s14', '3', '2', '1/4'),
    ('H2_5_1_algebraic', '5', '1', '3'),
    ('H2_7o2_1o2', '7/2', '1/2', '1/2'),
    ('H2_3_1o10', '3', '1/10', '1/3'),
    ('H2_3_1o100', '3', '1/100', '1/3'),
    ('H2_3_1o1000', '3', '1/1000', '1/3'),
    ('H2_3_1o10_principal', '3', '1/10', '1/2+13*I/10'),
    ('H2_7o2_1_principal', '7/2', '1', '1/2+13*I/10'),
    ('H2_7o4_12o5_principal', '7/4', '12/5', '1/2+13*I/10'),
    ('S2_10_1o10', '10', '1/10', '3'),
    ('S2_5_minus1', '5', '-1', '3'),
]
DPOINT = complex(.37, .11)


def sector_record(result):
    rec = dict(n=str(result['n']), q_R=result['q_R'],
               a=basis_record(result['a']), b=basis_record(result['b']),
               lambda_GB=result['lambda_GB'],
               matrices={key: pack(result[key]) for key in ('LR', 'W', 'LOG', 'K')})
    if abs(result['n']) == sp.Rational(1, 2):
        G, projection = gauge_columns(result)
        scale = np.linalg.norm(result['K'])*np.linalg.norm(G)
        rec['gauge_columns'] = pack(G)
        rec['gauge_basis_residual'] = max(projection)
        rec['gauge_residual'] = float(np.linalg.norm(result['K']@G)/scale)
    return rec


def trace_record(result):
    records = []
    for index, K in enumerate(result['engine'].source_terms):
        entries = [[int(i), int(j), float(K[i, j].real), float(K[i, j].imag)]
                   for i, j in zip(*np.nonzero(K))]
        records.append(dict(id=source_id(index), entries=entries))
    return dict(sample=SAMPLES[0][0], g='1', D=[DPOINT.real, DPOINT.imag],
                n='1/2', q_R=1, shape=list(result['K'].shape),
                normalization='raw lambda_GB coefficient, before multiplication by -k/(2g^2)',
                sparse_entry_format=['row_b', 'column_a', 'real', 'imag'], terms=records)


def write(name, record):
    (OUT/name).write_text(json.dumps(record, indent=2, allow_nan=False)+'\n')


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--sample', choices=[s[0] for s in SAMPLES])
    args = ap.parse_args()
    selected = [s for s in SAMPLES if args.sample in (None, s[0])]
    OUT.mkdir(exist_ok=True)
    write('source_terms.json', census())
    for label, L, k, S in selected:
        start = time.monotonic()
        sectors = []
        for n, charge in SECTORS:
            trace = label == SAMPLES[0][0] and n == sp.Rational(1, 2) and charge == 1
            result = evaluate(L, k, '1', n, charge, DPOINT, S, trace=trace)
            sectors.append(sector_record(result))
            if trace:
                write('term_contributions.json', trace_record(result))
        bg = result['background']
        write(label+'.json', dict(method='direct complex128 evaluation; no interpolation',
                                  precision='IEEE complex128',
                                  parameters=dict(L=L, k=k, g='1', S=S,
                                                  D=[DPOINT.real, DPOINT.imag]),
                                  background={key: str(value) for key, value in bg.items()},
                                  physical_level=label != 'H2_5_1_algebraic', sectors=sectors))
        print(f'WROTE {label}: all 8 sectors, {time.monotonic()-start:.1f}s', flush=True)


if __name__ == '__main__':
    main()
