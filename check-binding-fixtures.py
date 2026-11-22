#!/usr/bin/env python3
"""Compare two recorded Go test runs for one delegated binding."""

import argparse
import json
from pathlib import Path
import runpy
import sys


def citation_for(repo, test):
    """Find a single Go citation for an implementation-bound invariant."""
    if not repo.is_dir():
        raise ValueError(f"repository is not a directory: {repo}")
    suite = runpy.run_path(str(Path(__file__).with_name("jfa-conformance-suite.py")))
    citations, _ = suite["scan_bindings"](repo)
    matches = [c for c in citations if c.test == test and c.path.endswith("_test.go")]
    if len(matches) != 1:
        raise ValueError(f"expected one Go citation for {test}, found {len(matches)}")
    citation = matches[0]
    if not any(inv.id == citation.inv_id and inv.binding == "implementation"
               for inv in suite["REGISTRY"]):
        raise ValueError(f"{citation.inv_id} is not implementation-bound")
    return citation


def read_outcome(path, test):
    """Require an isolated, completed run of the selected test and package."""
    packages = set()
    test_actions = []
    package_outcomes = []
    with path.open(encoding="utf-8") as report:
        for line in report:
            event = json.loads(line)
            if not isinstance(event, dict) or not isinstance(event.get("Action"), str):
                raise ValueError("expected a Go test event")
            action = event["Action"]
            if action == "build-fail" or event.get("FailedBuild"):
                raise ValueError("build failed")
            if action == "build-output":
                continue
            package = event.get("Package")
            name = event.get("Test", "")
            if not isinstance(package, str) or not package or not isinstance(name, str):
                raise ValueError("expected a Go package and optional test name")
            packages.add(package)
            if name and name.split("/", 1)[0] != test:
                raise ValueError(f"unexpected test: {name}")
            if name == test and action in ("run", "pass", "fail", "skip"):
                test_actions.append(action)
            if not name and action in ("pass", "fail", "skip"):
                package_outcomes.append(action)

    if len(packages) != 1:
        raise ValueError("expected exactly one package")
    if test_actions not in (["run", "pass"], ["run", "fail"]):
        raise ValueError(f"expected one completed, non-skipped run of {test}")
    outcome = test_actions[-1]
    if package_outcomes != [outcome]:
        raise ValueError("package result is missing or differs from the test result")
    return packages.pop(), outcome


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", required=True, type=Path, help="implementation checkout")
    parser.add_argument("--test", required=True, help="exact Go TestInvariant_ function name")
    parser.add_argument("valid_report", type=Path, help="go test -json output for the valid fixture")
    parser.add_argument("violating_report", type=Path, help="output for the violating fixture")
    args = parser.parse_args()

    try:
        citation = citation_for(args.repo, args.test)
    except (OSError, ValueError) as error:
        print(f"INCONCLUSIVE: {error}", file=sys.stderr)
        return 2
    print(f"Citation: {citation.inv_id} in {citation.path} ({citation.test})")

    runs = []
    for label, path in (("Valid", args.valid_report), ("Violating", args.violating_report)):
        try:
            package, outcome = read_outcome(path, args.test)
        except (OSError, ValueError) as error:
            print(f"{label} fixture: INCONCLUSIVE ({error})", file=sys.stderr)
            continue
        print(f"{label} fixture: {outcome.upper()} ({package})")
        runs.append((package, outcome))

    if len(runs) != 2:
        return 2
    if runs[0][0] != runs[1][0]:
        print("INCONCLUSIVE: reports come from different packages", file=sys.stderr)
        return 2

    distinguished = runs[0][1] == "pass" and runs[1][1] == "fail"
    print("Fixture comparison: " + ("DISTINGUISHED" if distinguished else "DID NOT DISTINGUISH"))
    print("Scope: one test and two supplied runs. Review the failure output for the intended assertion.")
    return 0 if distinguished else 1


if __name__ == "__main__":
    sys.exit(main())
