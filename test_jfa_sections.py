"""Regression tests for required headings in the JFA conformance CLI."""

from pathlib import Path
from shutil import copyfile
import subprocess
import sys
from tempfile import TemporaryDirectory
import unittest


ROOT = Path(__file__).resolve().parent
DOCUMENT = (ROOT / "janus-facing-architecture.md").read_text(encoding="utf-8")


class RequiredSectionTests(unittest.TestCase):
    def run_suite(self, document):
        with TemporaryDirectory() as directory:
            fixture = Path(directory) / "instrument.md"
            fixture.write_text(document, encoding="utf-8")
            copyfile(ROOT / "OPEN-QUESTIONS.md", fixture.with_name("OPEN-QUESTIONS.md"))
            return subprocess.run(
                [sys.executable, str(ROOT / "jfa-conformance-suite.py"),
                 "--doc", str(fixture)],
                capture_output=True, text=True, timeout=5,
            )

    def test_duplicate_required_headings_fail_conformance(self):
        for heading, expected_title in (
            ("Introduction", "introduction"),
            ("**REFERENCES**", "references"),
        ):
            with self.subTest(heading=heading):
                result = self.run_suite(f"{DOCUMENT}\n## {heading}\n")
                self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
                self.assertRegex(
                    result.stdout,
                    rf"(?m)^\[FAIL\] D1 .*duplicate required sections: {expected_title}$",
                )

    def test_supplementary_headings_are_allowed(self):
        result = self.run_suite(f"{DOCUMENT}\n## Why This Matters\n\n### Introduction\n")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("[PASS] D1 ", result.stdout)

    def test_duplicate_headings_in_indented_and_setext_forms_fail(self):
        for heading, expected in (
            ("   ## Record Layer", "record layer"),
            ("**REFERENCES**\n----------", "references"),
            ("The Lines That\nCannot Be Crossed\n---", "the lines that cannot be crossed"),
        ):
            with self.subTest(heading=heading):
                result = self.run_suite(f"{DOCUMENT}\n\n{heading}\n")
                self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
                self.assertRegex(
                    result.stdout,
                    rf"(?m)^\[FAIL\] D1 .*duplicate required sections: {expected}$",
                )

    def test_required_sections_can_use_indented_or_setext_headings(self):
        document = DOCUMENT.replace("## Introduction\n", "  ## Introduction\n", 1)
        document = document.replace("## Record Layer\n", "Record Layer\n----\n", 1)
        result = self.run_suite(document)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_fenced_examples_do_not_count_as_sections_or_tiers(self):
        for opener, shorter, closer in (
            ("````markdown", "```", "````"),
            ("~~~markdown", "~~", "~~~"),
        ):
            with self.subTest(opener=opener):
                example = (
                    f"\n{opener}\n## References\n### Example Tier\n"
                    f"{shorter}\nIntroduction\n---\n## Record Layer\n{closer}\n"
                )
                document = DOCUMENT.replace("## Record Layer\n",
                                            "## Record Layer\n" + example, 1)
                result = self.run_suite(document)
                self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
                self.assertIn("[PASS] D1 ", result.stdout)
                self.assertIn("[PASS] D2 ", result.stdout)

    def test_missing_and_reordered_required_headings_still_fail(self):
        without_intro = DOCUMENT.replace("## Introduction\n", "## Supplement\n", 1)
        for document, diagnostic in (
            (without_intro, "missing sections: introduction"),
            (without_intro + "\n## Introduction\n", "sections out of order:"),
        ):
            with self.subTest(diagnostic=diagnostic):
                result = self.run_suite(document)
                self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
                self.assertRegex(result.stdout, rf"(?m)^\[FAIL\] D1 .*{diagnostic}")


if __name__ == "__main__":
    unittest.main()
