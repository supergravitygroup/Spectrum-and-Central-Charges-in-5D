"""Exact full-body comparisons and the gauged-to-ungauged limit."""
import json
from calculations.linear_multiplet import ROOT
from src.expressions import clean


def compare_expected(result, name):
    expected = json.loads((ROOT / "expected" / f"{name}_action.json").read_text())
    if result["order"] != expected["order"]:
        raise AssertionError("BF contribution order changed")
    for block in result["order"]:
        wanted = [[coefficient, clean(body)] for coefficient, body in expected["blocks"][block]]
        if result["blocks"][block] != wanted:
            raise AssertionError(f"{name}/{block}: coefficient or tensor-body mismatch")


def check_gauged_limit(ungauged, gauged):
    for block in ungauged["order"]:
        terms = gauged["blocks"][block]
        if block == "Y":
            terms = [term for term in terms if not term[1].startswith(r"g\sigma^{-1}L_c")]
        if terms != ungauged["blocks"][block]:
            raise AssertionError(f"g -> 0 failed in {block}")
