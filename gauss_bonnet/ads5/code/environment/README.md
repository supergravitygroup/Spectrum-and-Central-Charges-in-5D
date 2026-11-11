# Runtime

The tested environment is recorded in [the last full run](../CLAIMS.md).
Use Python 3.12 and the exact versions in [requirements.txt](requirements.txt).
NumPy arrays in the fermionic component calculation have `dtype=object`; entries
are exact SymPy expressions. No floating-point tolerance determines a PASS.

The development verification used an already available local Python 3.12 runtime
and these libraries, including pure-Python SymPy/mpmath from a local installation.
A network installation from PyPI was not tested here. The package itself contains
no machine-specific interpreter or dependency fallback. The relocation test uses
the same interpreter with a separate calculation directory and freshly generated
outputs; it establishes path independence, not cross-platform installation.

No network access is used by the calculation stages. BLAS/MKL behavior does not
supply the symbolic arithmetic. Other Python or library versions may work but are
not claimed as tested by the recorded run.
