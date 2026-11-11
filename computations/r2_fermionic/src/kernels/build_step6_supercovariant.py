#!/usr/bin/env python3
"""Substitute only the primed definitions and collect their outer products."""
import json,hashlib,time
from pathlib import Path
import build_step5a_partial_insertion as source
from step6_supercovariant_maps import *
ROOT=Path(__file__).resolve().parents[1]

def build():
    start=time.time();total=Poly();groups=[]
    for number,raw,terms in source.source_rows():
        p=Poly();source_records=[]
        for number_in_group,row in enumerate(terms,1):
            expanded=poly(row.c);factor_sizes=[]
            for f in row.fs:
                replacement=token(f.tex);factor_sizes.append(len(replacement));expanded*=replacement
            err=index_errors(expanded)
            if err:raise ValueError((number,number_in_group,err[:2]))
            p+=expanded
            source_records.append({'row':number_in_group,'coefficient':str(row.c),
               'factors':[f.tex for f in row.fs],'replacement_sizes':factor_sizes,'retained_products':len(expanded)})
        collected=canonical(p)
        assert not index_errors(collected)
        groups.append({'group':number,'source_tex':raw,'source_rows':source_records,
                       'raw_count':len(p),'rows':records(collected)})
        total+=collected
        print(f'Group {number}: {len(p)} -> {len(collected)}',flush=True)
    total=canonical(total)
    result={'lock':'R2-PRIMED-SUPERCOVARIANT-EXPLICIT2-v1',
       'scope':'Only primed definitions inserted; explicit degree <=2; supercovariant operators and gauged background composites retained.',
       'source_sha256':hashlib.sha256(source.old.DOC.read_bytes()).hexdigest(),
       'map_sha256':hashlib.sha256((ROOT/'notes/08_step5_primed_composite_vector_insertion.md').read_bytes()).hexdigest(),
       'prior_step6_sha256':hashlib.sha256((ROOT/'notes/10_step6_gauged_action_through_two_fermions.md').read_bytes()).hexdigest(),
       'groups':groups,'rows':records(total),'operators':op_records()}
    result['terms']=len(result['rows']);result['degrees']=dict(Counter(r['degree'] for r in result['rows']))
    (ROOT/'build/step6_supercovariant_ledger.json').write_text(json.dumps(result,indent=2)+'\n')
    print('FINAL',result['terms'],result['degrees'],'seconds',round(time.time()-start,2),flush=True)
    return result

if __name__=='__main__':build()
