"""Exercise invariant lookup through the conformance suite CLI."""

from pathlib import Path
import subprocess
import sys
from tempfile import TemporaryDirectory
import unittest


SUITE = Path(__file__).with_name("jfa-conformance-suite.py")


class InvariantLookupTests(unittest.TestCase):
    def run_suite(self, *args):
        return subprocess.run(
            [sys.executable, str(SUITE), *args], capture_output=True, text=True
        )

    def test_delegated_lookup_reports_registry_fields(self):
        result = self.run_suite("--explain", "REC-public-chain")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stderr, "")
        lines = result.stdout.splitlines()
        self.assertIn("Invariant: REC-public-chain", lines)
        self.assertIn("Section: Record Layer", lines)
        self.assertIn("Enforcement: implementation", lines)
        self.assertRegex(result.stdout, r"(?m)^Anchor: \S")
        self.assertRegex(result.stdout, r"(?m)^Expected evidence: \S")

    def test_accepts_underscore_ids_as_written_in_go_test_names(self):
        canonical = self.run_suite("--explain", "REC-witness-minimum")
        self.assertEqual(canonical.returncode, 0, canonical.stderr)
        for invariant in ("REC_witness_minimum", "REC_witness-minimum"):
            with self.subTest(invariant=invariant):
                result = self.run_suite("--explain", invariant)
                self.assertEqual(result.returncode, 0, result.stderr)
                self.assertEqual(result.stdout, canonical.stdout)

    def test_list_and_lookup_label_the_same_registry_note(self):
        lookup = self.run_suite("--explain", "REC-public-chain")
        listing = self.run_suite("--list")
        self.assertEqual(lookup.returncode, 0, lookup.stderr)
        self.assertEqual(listing.returncode, 0, listing.stderr)
        note = next(
            line for line in lookup.stdout.splitlines() if line.startswith("Expected evidence: ")
        )
        lines = listing.stdout.splitlines()
        entry = next(i for i, line in enumerate(lines) if line.startswith("REC-public-chain "))
        self.assertEqual(lines[entry + 1].strip(), note)

    def test_lookup_reports_document_and_instrument_categories(self):
        for invariant, section, enforcement in (
            ("INTRO-janus", "Introduction", "document"),
            ("GOV-prosumer-membership", "Governance Layer", "instrument"),
        ):
            with self.subTest(invariant=invariant):
                result = self.run_suite("--explain", invariant)
                self.assertEqual(result.returncode, 0, result.stderr)
                self.assertIn(f"Section: {section}", result.stdout.splitlines())
                self.assertIn(f"Enforcement: {enforcement}", result.stdout.splitlines())

    def test_unknown_id_reports_error_without_listing_registry(self):
        for invariant in ("NOT-REGISTERED", "rec-public-chain", "REC-public",
                          "REC_witness_minimum_UnfederatedLabel"):
            with self.subTest(invariant=invariant):
                result = self.run_suite("--explain", invariant)
                self.assertEqual(result.returncode, 1, result.stderr)
                self.assertEqual(result.stdout, "")
                self.assertIn(invariant, result.stderr)
                self.assertIn("--list", result.stderr)

    def test_lookup_skips_document_checks(self):
        with TemporaryDirectory() as directory:
            missing_document = Path(directory) / "missing.md"
            result = self.run_suite("--explain", "L1", "--doc", str(missing_document))
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("Invariant: L1", result.stdout.splitlines())
        self.assertIn("Section: The Lines That Cannot Be Crossed", result.stdout.splitlines())

    def test_lookup_requires_an_id(self):
        result = self.run_suite("--explain")
        self.assertEqual(result.returncode, 2)
        self.assertIn("--explain: expected one argument", result.stderr)

    def test_lookup_and_list_are_mutually_exclusive(self):
        result = self.run_suite("--list", "--explain", "L1")
        self.assertEqual(result.returncode, 2)
        self.assertEqual(result.stdout, "")
        self.assertIn("not allowed with argument --list", result.stderr)


if __name__ == "__main__":
    unittest.main()
