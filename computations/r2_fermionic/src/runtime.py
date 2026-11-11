"""Paths and serialization for the current R² component data."""
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "outputs"
WORK = ROOT / "inputs/reference/r2"

def read_json(path):
    return json.loads(path.read_text())

def write_json(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n")
