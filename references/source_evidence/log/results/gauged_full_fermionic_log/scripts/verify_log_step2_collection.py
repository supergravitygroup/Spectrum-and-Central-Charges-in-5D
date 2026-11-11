#!/usr/bin/env python3
"""Verify final transcription/provenance, never substitute for physics checks."""
from pathlib import Path
import json,hashlib,re
BASE=Path(__file__).resolve().parents[1]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def main():
 source=json.loads((BASE/'sources/step2/primary_term_ledger.json').read_text())
 derived=json.loads((BASE/'sources/step2/primary_derived_term_ledger.json').read_text())
 text=(BASE/'STEP_02_LOG_PRIMARY.md').read_text()
 benchmark=text.split('<!-- FULL_PRIMARY_BENCHMARK_BEGIN -->')[1].split('<!-- FULL_PRIMARY_BENCHMARK_END -->')[0]
 result=text.split('<!-- FULL_PRIMARY_DERIVED_BEGIN -->')[1].split('<!-- FULL_PRIMARY_DERIVED_END -->')[0]
 assert [len(g['terms']) for g in derived['groups']]==[2,7,12,18,14,3,2]
 changes=[];count=0
 for sg,dg in zip(source['groups'],derived['groups']):
  assert sg['inverse_W_power']==dg['inverse_W_power']
  for st,dt in zip(sg['terms'],dg['terms']):
   assert st['id']==dt['id']
   assert st['latex'].removesuffix('.') in benchmark,st['id']
   assert dt['latex'].removesuffix('.') in result,dt['id']
   assert dt['hand_derivation']
   if st['latex']!=dt['latex']:changes.append(dt['id']);assert dt['latex']=='+'+st['latex'][1:]
   count+=1
 assert count==58 and changes==['H3.9']
 allowed=source['groups'][3]['terms'][8]['latex']
 normalized=result.replace('\\boxed{\\begin{aligned}','\\begin{aligned}').replace('\\end{aligned}}','\\end{aligned}').replace('\\tag{S2-193}','\\tag{S2-BENCHMARK}')
 assert normalized==benchmark.replace(allowed,'+'+allowed[1:])
 coverage=json.loads((BASE/'sources/step2/derivation_coverage.json').read_text())
 assert coverage['derived_total_summands']==58 and coverage['remaining_source_summands']==0 and coverage['remaining_poles']==[]
 assert len(re.findall(r'\\tag\{S2-193\}',text))==1
 report={'date':'2026-09-23','status':'PASS','scope':'Final 58-term transcription, sector coverage and explicit source difference; no S/K/reality or action certification','terms_per_pole':[2,7,12,18,14,3,2],'derived_terms':count,'source_agreeing_terms':57,'source_differences':changes,'derivation_sha256':sha(BASE/'STEP_02_LOG_PRIMARY.md'),'derived_ledger_sha256':sha(BASE/'sources/step2/primary_derived_term_ledger.json'),'source_ledger_sha256':sha(BASE/'sources/step2/primary_term_ledger.json'),'script_sha256':sha(Path(__file__))}
 (BASE/'sources/step2/collection_checks.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))
if __name__=='__main__':main()
