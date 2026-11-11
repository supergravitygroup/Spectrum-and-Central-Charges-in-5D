"""Check the current component-action inputs."""

import hashlib
import json

from src.reporting import PACKAGE


def validate_entries(entries, path_key):
    for entry in entries:
        path = (PACKAGE / entry[path_key]).resolve()
        if not path.is_relative_to(PACKAGE.parents[2]):
            raise AssertionError(f"Input outside repository: {entry[path_key]}")
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
        if digest != entry["sha256"]:
            raise AssertionError(f"Changed accepted input: {entry[path_key]}")


def main():
    inputs = json.loads((PACKAGE / "inputs/action_sources.json").read_text())
    validate_entries(inputs, "path")
    print(f"Input integrity: {len(inputs)} component-action inputs match.")


if __name__ == "__main__":
    main()
