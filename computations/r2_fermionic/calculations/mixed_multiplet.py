"""01. Apply C^{1BC} once to each ordered vector pair."""
import sympy as sp
from src.runtime import ROOT, OUTPUT, read_json, write_json


def specialize(rows, coefficients):
    contributions = []
    for row in rows:
        source_coefficient = sp.sympify(row["coefficient"])
        if sum(map(sp.sympify, row["weights"])) != sp.sympify(row["output_weight"]):
            raise ValueError(f"Wrong Weyl weight in {row['id']}")
        for pair, weight in coefficients.items():
            coefficient = sp.expand(sp.sympify(weight) * source_coefficient)
            if coefficient:
                contributions.append({
                    "source_row": row["id"], "vector_pair": list(map(int, pair)),
                    "coefficient": str(coefficient), "slots": row["slots"],
                    "symmetric": row["symmetric"],
                })
    return contributions


def run():
    model = read_json(ROOT / "inputs/model.json")
    rows = read_json(ROOT / "inputs/mixed_map.json")
    # Later source parsers implement precisely this model. Refuse a different
    # recipe rather than silently running unchanged downstream kernels.
    if model["C1BC"] != {"11": "0", "12": "1/2", "21": "1/2", "22": "0"}:
        raise ValueError("Changing C requires a new downstream BF derivation.")
    if model["paired_vector"] != 1 or model["retained_physical_fermion_degrees"] != [0, 2]:
        raise ValueError("This package implements primed BF pairing through degree two.")
    if model["dimension"] != 5 or model["labels"] != {
        "1": "primed composite vector", "2": "unprimed defining vector"
    } or model["gradient_repair"] != "R2-VL-GRADIENT-PHASE-v1":
        raise ValueError("The dimension, vector roles and gradient repair are fixed inputs.")
    result = specialize(rows, model["C1BC"])
    gradient = [r for r in result if r["source_row"] == "P-05"]
    if len(result) != 44 or any(sp.sympify(r["coefficient"]) != sp.I / 4 for r in gradient):
        raise ValueError("The 22-row map must retain the documented i/4 mixed gradient.")
    write_json(OUTPUT / "mixed_multiplet.json", result)
    return {"source_rows": len(rows), "ordered_contributions": len(result)}
