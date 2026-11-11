"""Run the exact symbolic checks in a disposable directory; no project mutation."""
from pathlib import Path
from tempfile import TemporaryDirectory
from contextlib import redirect_stdout
import hashlib, io, json, runpy
import sympy

ROOT=Path(__file__).resolve().parent
ORDER=[
 'results_vl_check.py','results_p_current_check.py','results_check_scalar_map.py',
 'results_rq_full_check.py','results_rs_bianchi_check.py','results_weyl_gamma_ids.py',
 'results_weyl_l_check.py','results_weyl_spinor_s_check.py',
 'results_weyl_scalar_q_check.py','results_weyl_vector_q_check.py',
 'results_weyl_dc_reduction.py','results_weyl_spinor_q_full_check.py',
 'results_weyl_dr_bianchi.py','results_linear_vector_spinor_check.py']

def main():
    if not __debug__:
        raise SystemExit(
            "Symbolic checks require Python assertions; remove -O/-OO and "
            "unset PYTHONOPTIMIZE before running this script."
        )
    results=[]
    with TemporaryDirectory(prefix='results-symbolic-') as directory:
        work=Path(directory)
        for name in ORDER:
            source=(ROOT/name).read_text()
            (work/name).write_text(source.replace('__RESULTS_CHECK_WORKDIR__',str(work)))
        for name in ORDER:
            output=io.StringIO()
            with redirect_stdout(output):
                runpy.run_path(str(work/name),run_name='__main__')
            results.append({'calculation':name,'sha256':hashlib.sha256((ROOT/name).read_bytes()).hexdigest(),'execution':'passed'})
    print(json.dumps({'method':'exact symbolic, no physical parameter samples','sympy_version':sympy.__version__,'checks':results},ensure_ascii=False,indent=2))

if __name__=='__main__':
    main()
