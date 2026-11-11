"""Read the current component density; never load executable pickle data."""
from functools import lru_cache
from pathlib import Path
from parse_density import parse, showterm

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
ACTION = ROOT/'gauss_bonnet/action/gb_splus_action.md'


@lru_cache(maxsize=1)
def terms():
    result = parse(ACTION)
    if len(result) != 1184:
        raise ValueError('Source census changed: review the source manifest')
    return result


def source_id(index):
    return f'GB-FINAL-DENSITY:{index:04d}'


def census():
    from eval2 import leibniz
    from evalbg import expand_terms, has_odd
    records = []
    for index, term in enumerate(terms()):
        children = leibniz(expand_terms([term]))
        classes = [sum(has_odd(f) for f in t['factors']) for t in children]
        if any(c not in (0, 1, 2) for c in classes):
            raise ValueError(('Unexpected fermion classification', index, classes))
        records.append(dict(id=source_id(index), index=index,
                            summand='-2 W' if index < 52 else '-4 LOG',
                            expression=showterm(term), expanded_terms=len(children),
                            explicit_bilinears=classes.count(2),
                            differentiated_bilinears=classes.count(1),
                            implicit_bilinears=classes.count(0)))
    return records
