"""Exercise the fixture report with real Go test output."""

import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parent
TEST = "TestInvariant_REC_public_chain_SharedRecord"
GO_TEST = """package fixture

import (
    "os"
    "strings"
    "testing"
)

func TestInvariant_REC_public_chain_SharedRecord(t *testing.T) {
    data, err := os.ReadFile(os.Getenv("FIXTURE"))
    if err != nil {
        t.Fatal(err)
    }
    if string(data) == "skip" {
        t.Skip("no fixture")
    }
    if strings.Count(string(data), "head") != 1 {
        t.Fatal("expected a single shared head")
    }
}

func TestOther(t *testing.T) {}
"""


class BindingFixtureTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        temp = tempfile.TemporaryDirectory()
        cls.addClassCleanup(temp.cleanup)
        cls.repo = Path(temp.name)
        (cls.repo / "go.mod").write_text("module example.com/fixture\n\ngo 1.20\n")
        (cls.repo / "record_test.go").write_text(GO_TEST)
        cls.record_reports(cls.repo, cls.repo)

    @staticmethod
    def record_reports(package_dir, report_dir):
        for name, fixture, selector, expected in (
            ("valid", "head", f"^{TEST}$", 0),
            ("violating", "head head", f"^{TEST}$", 1),
            ("skip", "skip", f"^{TEST}$", 0),
            ("other", "head", "^TestOther$", 0),
        ):
            path = report_dir / (name + ".fixture")
            path.write_text(fixture)
            env = dict(os.environ, FIXTURE=str(path))
            run = subprocess.run(
                ["go", "test", "-json", "-count=1", "-run", selector, "."],
                cwd=package_dir, env=env, capture_output=True, text=True, timeout=120,
            )
            if run.returncode != expected:
                raise RuntimeError(run.stdout + run.stderr)
            (report_dir / (name + ".json")).write_text(run.stdout)

    def check_report(self, valid="valid", violating="violating", test=TEST, repo=None, reports=None):
        repo = self.repo if repo is None else repo
        reports = self.repo if reports is None else reports
        return subprocess.run(
            [sys.executable, str(ROOT / "check-binding-fixtures.py"),
             "--repo", str(repo), "--test", test,
             str(reports / (valid + ".json")), str(reports / (violating + ".json"))],
            capture_output=True, text=True, timeout=10,
        )

    def test_reports_citation_and_distinguishes_fixtures(self):
        result = self.check_report()
        self.assertEqual(result.returncode, 0, result.stderr)
        for label in ("Citation: REC-public-chain", "Valid fixture: PASS",
                      "Violating fixture: FAIL", "Fixture comparison: DISTINGUISHED"):
            self.assertIn(label, result.stdout)

    def test_rejects_comparisons_with_wrong_observed_outcomes(self):
        for valid, violating in (("valid", "valid"), ("violating", "violating"),
                                 ("violating", "valid")):
            with self.subTest(valid=valid, violating=violating):
                result = self.check_report(valid, violating)
                self.assertEqual(result.returncode, 1, result.stderr)
                self.assertIn("DID NOT DISTINGUISH", result.stdout)

    def test_skipped_and_unrelated_runs_are_inconclusive(self):
        for name in ("skip", "other"):
            with self.subTest(name=name):
                result = self.check_report(violating=name)
                self.assertEqual(result.returncode, 2, result.stderr)
                self.assertIn("INCONCLUSIVE", result.stderr)

    def test_runs_from_different_packages_are_inconclusive(self):
        events = (self.repo / "violating.json").read_text().splitlines()
        renamed = [dict(json.loads(line), Package="example.com/other") for line in events]
        (self.repo / "mismatch.json").write_text("\n".join(map(json.dumps, renamed)))
        result = self.check_report(violating="mismatch")
        self.assertEqual(result.returncode, 2, result.stdout)
        self.assertIn("different packages", result.stderr)

    def test_matching_reports_from_wrong_package_are_inconclusive(self):
        for name in ("valid", "violating"):
            events = (self.repo / (name + ".json")).read_text().splitlines()
            renamed = [dict(json.loads(line), Package="example.com/other") for line in events]
            (self.repo / ("wrong-" + name + ".json")).write_text("\n".join(map(json.dumps, renamed)))
        result = self.check_report(valid="wrong-valid", violating="wrong-violating")
        self.assertEqual(result.returncode, 2, result.stdout)
        self.assertIn("example.com/fixture", result.stderr)
        self.assertIn("example.com/other", result.stderr)

    def test_resolves_package_within_nested_module(self):
        with tempfile.TemporaryDirectory() as temp:
            repo = Path(temp)
            (repo / "go.mod").write_text("module example.com/outer\n\ngo 1.20\n")
            nested = repo / "nested"
            package = nested / "record"
            package.mkdir(parents=True)
            (nested / "go.mod").write_text('module "example.com/inner" // nested module\n\ngo 1.20\n')
            (package / "record_test.go").write_text(GO_TEST)
            self.record_reports(package, repo)
            result = self.check_report(repo=repo, reports=repo)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("example.com/inner/record", result.stdout)

    def test_missing_module_is_inconclusive(self):
        with tempfile.TemporaryDirectory() as temp:
            repo = Path(temp)
            (repo / "record_test.go").write_text(GO_TEST)
            result = self.check_report(repo=repo)
        self.assertEqual(result.returncode, 2, result.stdout)
        self.assertIn("go.mod", result.stderr)

    def test_missing_citation_is_inconclusive(self):
        result = self.check_report(test=TEST + "_Missing")
        self.assertEqual(result.returncode, 2)
        self.assertIn("citation", result.stderr.lower())

    def test_missing_package_result_and_malformed_report_are_inconclusive(self):
        events = (self.repo / "violating.json").read_text().splitlines()
        incomplete = [line for line in events if json.loads(line).get("Test")
                      or json.loads(line)["Action"] != "fail"]
        (self.repo / "incomplete.json").write_text("\n".join(incomplete))
        (self.repo / "malformed.json").write_text("invalid")
        for name in ("incomplete", "malformed"):
            with self.subTest(name=name):
                result = self.check_report(violating=name)
                self.assertEqual(result.returncode, 2)
                self.assertIn("INCONCLUSIVE", result.stderr)

    def test_package_lifecycle_must_surround_the_test_run(self):
        events = (self.repo / "violating.json").read_text().splitlines()
        start = next(i for i, line in enumerate(events)
                     if json.loads(line)["Action"] == "start")
        finish = next(i for i, line in enumerate(events)
                      if json.loads(line)["Action"] == "fail" and not json.loads(line).get("Test"))
        for name, report in (
            ("missing-start", events[:start] + events[start + 1:]),
            ("early-finish", events[:start + 1] + [events[finish]]
             + events[start + 1:finish] + events[finish + 1:]),
        ):
            with self.subTest(name=name):
                (self.repo / (name + ".json")).write_text("\n".join(report))
                result = self.check_report(violating=name)
                self.assertEqual(result.returncode, 2, result.stdout)
                self.assertIn("INCONCLUSIVE", result.stderr)


if __name__ == "__main__":
    unittest.main()
