import json
import math
import sys

REL_TOL = 1e-2

def compare(actual_path, expected_path):
    with open(actual_path) as f:
        actual = json.load(f)
    with open(expected_path) as f:
        expected = json.load(f)

    if actual.keys() != expected.keys():
        print(f"Key mismatch: only in {actual_path}: {actual.keys() - expected.keys()}, "
              f"only in {expected_path}: {expected.keys() - actual.keys()}")
        return False

    mismatches = []
    for key in actual:
        a, e = actual[key], expected[key]
        if isinstance(a, (int, float)) and isinstance(e, (int, float)):
            if not math.isclose(a, e, rel_tol=REL_TOL):
                mismatches.append((key, a, e))
        elif a != e:
            mismatches.append((key, a, e))

    if mismatches:
        for key, a, e in mismatches:
            print(f"{key}: {a} != {e} (outside rel_tol={REL_TOL})")
        return False

    return True

if __name__ == "__main__":
    actual_path, expected_path = sys.argv[1], sys.argv[2]
    if not compare(actual_path, expected_path):
        sys.exit(1)
    print(f"{actual_path} matches {expected_path} within rel_tol={REL_TOL}")
