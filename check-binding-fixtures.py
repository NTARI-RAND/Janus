#!/usr/bin/env python3
"""Compare two recorded Go test runs for one delegated binding."""

import argparse
import ast
import json
from pathlib import Path
import re
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


def package_for(repo, citation):
    """Derive the cited package's import path without running Go."""
    package_dir = (repo / citation.path).parent
    module_dir = package_dir
    while True:
        go_mod = module_dir / "go.mod"
        try:
            module_text = go_mod.read_text(encoding="utf-8")
            break
        except FileNotFoundError:
            if module_dir == repo:
                raise ValueError(f"no go.mod for cited test in {citation.path}") from None
            module_dir = module_dir.parent

    for line in module_text.splitlines():
        fields = line.partition("//")[0].split()
        if fields[:1] != ["module"]:
            continue
        if len(fields) != 2:
            break
        module_path = fields[1]
        if module_path.startswith('"'):
            try:
                module_path = ast.literal_eval(module_path)
            except (SyntaxError, ValueError):
                break
        if re.fullmatch(r"[A-Za-z0-9._~/-]+", module_path):
            return "/".join((module_path, *package_dir.relative_to(module_dir).parts))
        break
    raise ValueError(f"cannot read module path from {go_mod}")


def read_outcome(path, test):
    """Require an isolated, completed run of the selected test and package."""
    packages = set()
    lifecycle = []
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
                lifecycle.append(("test", action))
            if not name and action in ("start", "pass", "fail", "skip"):
                lifecycle.append(("package", action))

    if len(packages) != 1:
        raise ValueError("expected exactly one package")
    for outcome in ("pass", "fail"):
        if lifecycle == [
            ("package", "start"), ("test", "run"),
            ("test", outcome), ("package", outcome),
        ]:
            return packages.pop(), outcome
    raise ValueError(f"expected one completed run of {test} between package start and matching result")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", required=True, type=Path, help="implementation checkout")
    parser.add_argument("--test", required=True, help="exact Go TestInvariant_ function name")
    parser.add_argument("valid_report", type=Path, help="go test -json output for the valid fixture")
    parser.add_argument("violating_report", type=Path, help="output for the violating fixture")
    args = parser.parse_args()

    try:
        repo = args.repo.resolve()
        citation = citation_for(repo, args.test)
        expected_package = package_for(repo, citation)
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
    if runs[0][0] != expected_package:
        print(f"INCONCLUSIVE: reports name {runs[0][0]}, expected {expected_package}",
              file=sys.stderr)
        return 2

    distinguished = runs[0][1] == "pass" and runs[1][1] == "fail"
    print("Fixture comparison: " + ("DISTINGUISHED" if distinguished else "DID NOT DISTINGUISH"))
    print("Scope: one test and two supplied runs. Review the failure output for the intended assertion.")
    return 0 if distinguished else 1


if __name__ == "__main__":
    sys.exit(main())
