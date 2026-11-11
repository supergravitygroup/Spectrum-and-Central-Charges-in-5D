"""Read the accepted FM01–04 map and expose every exact component term."""
from pathlib import Path
from src.expressions import equation_terms

ROOT = Path(__file__).resolve().parents[1]
MAP = ROOT / "inputs/reference/notes/04_full_fermionic_weyl_linear_map.md"
TAGS = {"L": "FM01", "phi": "FM02", "E": "FM03", "N": "FM04"}


def load_multiplet():
    document = MAP.read_text()
    return {slot: equation_terms(document, tag) for slot, tag in TAGS.items()}
