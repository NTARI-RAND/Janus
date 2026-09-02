#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""JFA conformance suite.

This suite implements rung 5 of the legibility ladder ("conformance tests
bind the prose to the code") at the layer it can honestly reach from a
documents folder: the unified architecture document itself.

What it checks, executably, right now (the DOCUMENT checks):
  * The glossary is bound to the body: every defined term still appears in
    the normative text, so the glossary cannot drift into a second source
    of truth.
  * Every registered invariant's anchor phrase is present in the document,
    and its stable ID is printed on the same line as that anchor, so the
    text and this registry cannot drift apart.
  * Every sentence containing an uppercase MUST maps to a registered
    invariant, so a new normative demand cannot enter the document without
    entering this registry (and a registered one cannot silently leave).
  * The standard has exactly seven checks, including the two clauses merged
    from Amendment 001 (presentation separability on check 5; the living
    open-questions deliverable on check 7).
  * Part VII's open problems are numbered contiguously, each carries a
    Status, and every "open problem N" cross-reference resolves.
  * The tension protocol and the refuse-or-flag list are present and intact.
  * The document stays product-agnostic (no product names) and PII-free
    (no email addresses beyond the organizational footer).
  * Named interims are stated alongside committed exits.

What it does NOT check, and says so (the DELEGATED registry):
  Invariants that bind running software (append-only ledgers, witnessing,
  issuance caps, presentation sandboxing, ...) or a governance instrument
  (recall, one-person-one-vote, entrenchment locks, ...) can only be
  enforced by tests living beside that code or that instrument. They are
  carried here as a registry with stable IDs and reported as delegated and
  unbound until a repo ships tests citing those IDs. Reporting them as
  "checked" from here would be self-attestation wearing a test runner --
  the stand-in is labeled instead, per the tension protocol.

Usage:
  python jfa-conformance-suite.py                 # check the document
  python jfa-conformance-suite.py --doc PATH      # check another copy
  python jfa-conformance-suite.py --list          # print the registry
  python jfa-conformance-suite.py --project PATH  # check a project repo's
                                                  # open-questions deliverable

Exit code 0 when every executed check passes; 1 otherwise.

Free documentation and tooling under the project's AGPL-3.0 commons.
"""

import argparse
import io
import os
import re
import sys
from collections import namedtuple

# --------------------------------------------------------------------------
# The invariant registry.
#
# id       stable identifier a repo's test suite cites (e.g. "REC-1")
# layer    the layer the invariant defends
# anchor   normalized phrase that MUST appear in the document (see normalize)
# binding  where executable enforcement must live:
#            "document"       -- enforced fully by this suite
#            "implementation" -- enforced by tests beside the code
#            "instrument"     -- enforced by a governance instrument and its
#                                venue tooling
# note     where the delegated enforcement is expected to land
# --------------------------------------------------------------------------

Invariant = namedtuple("Invariant", "id layer anchor binding note")

REGISTRY = [
    # Substrate
    Invariant("SUB-1", "Substrate", "no unremovable hosting chokepoint",
              "implementation", "deployment/packaging tests: runs on participant-owned infrastructure"),
    Invariant("SUB-2", "Substrate", "dependency leaf",
              "implementation", "protocol repo: import/dependency audit in CI"),
    Invariant("SUB-3", "Substrate", "single participant identity",
              "implementation", "coordinator + front-end tests: one account, both roles"),
    Invariant("SUB-4", "Substrate", "persons never appear on the coordination wire",
              "implementation", "protocol schema tests: no person-modeling fields"),
    Invariant("SUB-5", "Substrate", "scripts never markup sandboxed",
              "implementation", "front-end theme-import tests: executable content rejected"),
    Invariant("SUB-6", "Substrate", "no remote fetches from user styles",
              "implementation", "front-end theme-import tests: url()/@import/@font-face stripped"),
    Invariant("SUB-7", "Substrate", "reset to default lives outside the styleable surface",
              "implementation", "front-end UI tests: reset control unstyleable"),
    Invariant("SUB-8", "Substrate", "styles are plain exportable artifacts",
              "implementation", "front-end tests: theme export round-trips as plain CSS/HTML"),
    Invariant("SUB-9", "Substrate", "shipped or hosted themes inherit the carve out",
              "implementation", "front-end release tests: bundled themes render covenant surfaces"),
    # Record
    Invariant("REC-1", "Record", "append only",
              "implementation", "record-instance tests: no update-in-place, no delete"),
    Invariant("REC-2", "Record", "may forgive a harm",
              "implementation", "record-instance tests: dismissal is annotation, never erasure"),
    Invariant("REC-3", "Record", "the commons must not contain pii",
              "implementation", "anchor-commitment tests: structural facts and references only"),
    Invariant("REC-4", "Record", "the atomic unit is the dialog",
              "implementation", "record-instance tests: seal requires complete and quiescent"),
    Invariant("REC-5", "Record", "own log",
              "implementation", "record-instance tests: per-operator logs, no global chain"),
    Invariant("REC-6", "Record", "a witness confers no authority",
              "implementation", "witness-relay tests: relay cannot gate or adjudicate"),
    Invariant("REC-7", "Record", "the witnessed unit is the claim lifecycle",
              "implementation", "lifecycle tests: file/adjudicate/resolve/seal each witnessed"),
    Invariant("REC-8", "Record", "filing commitment is made at an independent witness",
              "implementation", "filing tests: operator absent at claim creation; single-write witness"),
    Invariant("REC-9", "Record", "carry a relation type",
              "implementation", "schema tests: trade / adjudication-conduct / verdict-satisfaction typed"),
    Invariant("REC-10", "Record", "a clock never force seals a dialog",
              "implementation", "seal tests: unanswered claim stays open; dwell is readable"),
    # Covenant
    Invariant("COV-1", "Covenant", "must not be averaged",
              "implementation", "covenant tests: full distribution carried, no scalar score"),
    Invariant("COV-2", "Covenant", "lowest rating is the breach itself",
              "implementation", "covenant tests: breach semantics, not a debit"),
    Invariant("COV-3", "Covenant", "must be symmetric",
              "implementation", "covenant tests: every claim answerable; dismissals annotate"),
    Invariant("COV-4", "Covenant", "never how much",
              "implementation", "covenant/economy boundary tests: reputation gates whether only"),
    Invariant("COV-5", "Covenant", "non portable by default",
              "implementation", "covenant tests: no cross-platform standing without governance act"),
    Invariant("COV-6", "Covenant", "sybil resistance must be settled first",
              "instrument", "governance gate before reputation feeds credit, citation, or votes"),
    # Economy
    Invariant("ECO-1", "Economy", "deterministic function of the sealed record",
              "implementation", "economy tests: balances re-derivable from sealed dialogs"),
    Invariant("ECO-2", "Economy", "capped by a separate limit",
              "implementation", "issuance tests: covenant gate and limit independent; limit never from harms"),
    Invariant("ECO-3", "Economy", "sovereign and separate",
              "implementation", "economy tests: no cross-platform unit or fixed convertibility"),
    Invariant("ECO-4", "Economy", "denomination is not redemption",
              "implementation", "economy tests: no redemption path, no purchase path"),
    Invariant("ECO-5", "Economy", "governed configuration change",
              "instrument", "escrow-to-credit switch gated by recorded governance action"),
    Invariant("ECO-6", "Economy", "value stays home only truth crosses",
              "implementation", "cross-economy tests: atomic paired spends over witnessed proof"),
    # Governance
    Invariant("GOV-1", "Governance", "by the cost of leaving it",
              "instrument", "instrument review: discipline assigned per layer"),
    Invariant("GOV-2", "Governance", "name the steward",
              "instrument", "instrument names the accountable stewarding body"),
    Invariant("GOV-3", "Governance", "stewardship mirrors the stack",
              "instrument", "five offices map one-to-one to five layers; no doubling"),
    Invariant("GOV-4", "Governance", "behind a double lock",
              "instrument", "entrenchment limited to the three commitments; supermajority + unanimity"),
    Invariant("GOV-5", "Governance", "delegates are recallable circles are open",
              "instrument", "recall and open-circle provisions present and usable"),
    Invariant("GOV-6", "Governance", "never averages dissent away",
              "instrument", "observation-reopen and harm-reopen provisions present"),
    Invariant("GOV-7", "Governance", "one person one vote no proxy no delegation",
              "instrument", "voting provisions: status qualifies, never multiplies"),
    Invariant("GOV-8", "Governance", "legibility is an output not a comment",
              "implementation", "each repo ships documentation as a build deliverable"),
    Invariant("GOV-9", "Governance", "ships a living open questions document",
              "implementation", "per-repo: open-questions file present and fresh (see --project)"),
    Invariant("GOV-10", "Governance", "every contribution enters the copyleft commons",
              "implementation", "repo checks: license, no CLA, sign-off discipline"),
    Invariant("GOV-11", "Governance", "must itself be leaveable substrate",
              "instrument", "venue designation: proprietary venue only as named interim"),
    Invariant("GOV-12", "Governance", "held by motion",
              "document", "posture statement; carried by the document checks as presence"),
    # Legibility ladder
    Invariant("LEG-1", "Governance", "mechanically bound to the rung below",
              "implementation", "docs pipeline: each legibility rung generated from or tested against the rung below"),
    Invariant("LEG-2", "Governance", "remain a reading aid never an oracle",
              "implementation", "any model-assisted explainer checked against spec + conformance suite"),
]

# The seven checks of the standard, with the two merged amendment clauses.
STANDARD_ANCHORS = [
    ("S1", "mutual credit not banking"),
    ("S2", "sovereign substrate"),
    ("S3", "witnessed legible record"),
    ("S4", "reputation as covenant"),
    ("S5", "governed by the cost of leaving"),
    ("S6", "a minimal contested stewarded core"),
    ("S7", "legible above all"),
]
STANDARD_CLAUSES = [
    ("S5 clause (Amendment 001)", "presentation is separable"),
    ("S7 clause (Amendment 001)", "living open questions document naming what remains unresolved"),
]

# Product names that must never appear in the product-agnostic document.
PRODUCT_NAMES = ["SoHoLINK", "Cloudy", "Slack", "Discord", "Mycelium",
                 "LBTAS", "Agrinet", "NTARI/OS", "GitHub", "Wix"]

# Glossary terms whose body wording differs enough to need explicit aliases.
GLOSSARY_ALIASES = {
    "the one rule": ["one rule"],
    "escrow phase": ["escrow"],
    "sovereign currency": ["currency is sovereign", "sovereign and separate"],
    "one person one vote qualifier": ["one person one vote"],
}

# Lines allowed to contain an uppercase MUST without mapping to the registry
# (they explain the convention rather than stating a demand).
MUST_EXEMPT_MARKERS = ["where a rule says"]


def normalize(text):
    """Lowercase; strip markdown emphasis; fold dashes and punctuation to
    spaces; collapse whitespace. Anchors are written in this normal form."""
    text = text.lower()
    text = re.sub(r"[*_`>#|]", "", text)
    text = re.sub(u"[–—-]", " ", text)
    text = re.sub(u"[(),;:.\"'“”‘’?!→·\\[\\]]", " ", text)
    return re.sub(r"\s+", " ", text).strip()


class Result:
    def __init__(self, name, ok, detail=""):
        self.name, self.ok, self.detail = name, ok, detail


def section(doc, start_marker, end_markers):
    i = doc.find(start_marker)
    if i < 0:
        return None
    end = len(doc)
    for m in end_markers:
        j = doc.find(m, i + len(start_marker))
        if 0 <= j < end:
            end = j
    return doc[i:end]


# --------------------------------------------------------------------------
# Document checks
# --------------------------------------------------------------------------

def check_glossary_binding(doc):
    gloss = section(doc, "## Glossary", ["\n## Part I"])
    if gloss is None:
        return Result("D1 glossary bound to body", False, "no '## Glossary' section found")
    body = doc[doc.find("## Part I"):]
    norm_body = normalize(body)
    terms = re.findall(r"^- \*\*(.+?)\*\*", gloss, re.M)
    if not terms:
        return Result("D1 glossary bound to body", False, "glossary defines no terms")
    missing = []
    for term in terms:
        key = normalize(term)
        segments = [normalize(s) for s in term.split(";") if normalize(s)]
        candidates = GLOSSARY_ALIASES.get(key)
        if candidates is None:
            # every ';'-separated segment of the term must appear in the body
            candidates = None
            if all(seg in norm_body for seg in segments):
                continue
            missing.append(term)
        else:
            if not any(alias in norm_body for alias in candidates):
                missing.append(term)
    if missing:
        return Result("D1 glossary bound to body", False,
                      "terms absent from body: " + "; ".join(missing))
    return Result("D1 glossary bound to body", True,
                  "%d terms all present in the normative text" % len(terms))


def check_glossary_disclaimer(doc):
    ok = "definitions orient the normative text below governs" in normalize(doc)
    return Result("D2 glossary disclaims authority", ok,
                  "" if ok else "missing 'Definitions orient; the normative text below governs.'")


def check_standard(doc):
    std = section(doc, "## The standard", ["\n## The tension protocol"])
    if std is None:
        return Result("D3 the standard (7 checks + merged clauses)", False,
                      "no '## The standard' section")
    count = len(re.findall(r"^\d+\.\s+\*\*", std, re.M))
    problems = []
    if count != 7:
        problems.append("expected 7 numbered checks, found %d" % count)
    norm = normalize(std)
    for label, anchor in STANDARD_ANCHORS + STANDARD_CLAUSES:
        if anchor not in norm:
            problems.append("missing %s ('%s')" % (label, anchor))
    return Result("D3 the standard (7 checks + merged clauses)",
                  not problems, "; ".join(problems))


def check_invariant_anchors(doc):
    norm = normalize(doc)
    norm_lines = [normalize(line) for line in doc.splitlines()]
    missing = [inv.id for inv in REGISTRY if inv.anchor not in norm]
    untagged = [inv.id for inv in REGISTRY
                if inv.id not in missing and not any(
                    inv.anchor in nl and normalize(inv.id) in nl
                    for nl in norm_lines)]
    problems = []
    if missing:
        problems.append("anchors missing: " + ", ".join(missing))
    if untagged:
        problems.append("anchor present but ID not printed beside it: "
                        + ", ".join(untagged))
    return Result("D4 invariant anchors present and ID-tagged", not problems,
                  "; ".join(problems) if problems
                  else "%d registered invariants anchored and ID-tagged in the text" % len(REGISTRY))


def check_must_coverage(doc):
    """Every uppercase-MUST line maps to at least one registered anchor."""
    orphans = []
    for line in doc.splitlines():
        if "MUST" not in line:
            continue
        norm_line = normalize(line)
        if any(marker in norm_line for marker in MUST_EXEMPT_MARKERS):
            continue
        if not any(inv.anchor in norm_line for inv in REGISTRY):
            orphans.append(line.strip()[:90])
    return Result("D5 every MUST maps to the registry", not orphans,
                  ("unregistered MUST lines: " + " || ".join(orphans)) if orphans else "")


def check_open_problems(doc):
    part = section(doc, "## Part VII", ["\n## The standard"])
    if part is None:
        return Result("D6 open problems intact", False, "no Part VII section")
    numbers = [int(n) for n in re.findall(r"^\*\*(\d+)\.", part, re.M)]
    problems = []
    if numbers != list(range(1, len(numbers) + 1)):
        problems.append("problems not numbered contiguously from 1: %s" % numbers)
    blocks = re.split(r"^\*\*\d+\.", part, flags=re.M)[1:]
    for n, block in zip(numbers, blocks):
        if "Status:" not in block:
            problems.append("problem %d has no Status" % n)
    valid = set(numbers)
    for ref in re.findall(r"problem\s+(\d+)", doc, re.I):
        if int(ref) not in valid:
            problems.append("reference to nonexistent problem %s" % ref)
    return Result("D6 open problems intact", not problems,
                  "; ".join(problems) if problems
                  else "%d problems, contiguous, each with Status; all references resolve" % len(numbers))


def check_tension_protocol(doc):
    tp = section(doc, "## The tension protocol", ["\n## The discipline"])
    if tp is None:
        return Result("D7 tension protocol present", False, "section missing")
    norm = normalize(tp)
    signals = ["reframing a constraint", "without labeling it", "routing around"]
    missing = [s for s in signals if s not in norm]
    return Result("D7 tension protocol present", not missing,
                  ("missing signals: " + "; ".join(missing)) if missing else "")


def check_refuse_flag(doc):
    sec = section(doc, "### Requests to refuse or flag", ["\n---"])
    if sec is None:
        return Result("D8 refuse-or-flag list intact", False, "section missing")
    items = re.findall(r'^- \*"', sec, re.M)
    norm = normalize(sec)
    problems = []
    if len(items) < 18:
        problems.append("expected at least 18 items, found %d" % len(items))
    for needle in ["themes run scripts", "starter theme"]:
        if needle not in norm:
            problems.append("missing merged theme item ('%s')" % needle)
    return Result("D8 refuse-or-flag list intact", not problems,
                  "; ".join(problems) if problems else "%d items" % len(items))


def check_product_agnosticism(doc):
    hits = [name for name in PRODUCT_NAMES
            if re.search(r"(?<![A-Za-z])" + re.escape(name) + r"(?![A-Za-z])", doc)]
    return Result("D9 product-agnostic", not hits,
                  ("product names found: " + ", ".join(hits)) if hits else "")


def check_no_pii(doc):
    emails = set(re.findall(r"[\w.+-]+@[\w-]+\.[\w.]+", doc))
    emails.discard("info@ntari.org")
    return Result("D10 no PII beyond the organizational footer", not emails,
                  ("unexpected addresses: " + ", ".join(sorted(emails))) if emails else "")


def check_interim_honesty(doc):
    norm = normalize(doc)
    problems = []
    if "named interim" not in norm:
        problems.append("'named interim' absent")
    if "committed exit" not in norm and "committed path" not in norm:
        problems.append("no committed exit/path language")
    if "standing violation" not in norm:
        problems.append("stalled-interim consequence absent")
    return Result("D11 named interims carry committed exits", not problems,
                  "; ".join(problems))


DOC_CHECKS = [
    check_glossary_binding,
    check_glossary_disclaimer,
    check_standard,
    check_invariant_anchors,
    check_must_coverage,
    check_open_problems,
    check_tension_protocol,
    check_refuse_flag,
    check_product_agnosticism,
    check_no_pii,
    check_interim_honesty,
]


# --------------------------------------------------------------------------
# Per-project check: the living open-questions deliverable (GOV-9)
# --------------------------------------------------------------------------

def check_project(path):
    results = []
    candidates = ["OPEN-QUESTIONS.md", "OPEN_QUESTIONS.md", "open-questions.md",
                  os.path.join("docs", "open-questions.md")]
    found = None
    for c in candidates:
        p = os.path.join(path, c)
        if os.path.isfile(p):
            found = p
            break
    if not found:
        results.append(Result("P1 open-questions document exists (GOV-9)", False,
                              "none of: " + ", ".join(candidates)))
        return results
    text = io.open(found, encoding="utf-8", errors="replace").read()
    results.append(Result("P1 open-questions document exists (GOV-9)", True, found))
    norm = normalize(text)
    entries = len(re.findall(r"^(?:#{2,4} |\- |\d+\. )", text, re.M))
    results.append(Result("P2 document has entries", entries > 0,
                          "%d candidate entries" % entries))
    has_status = "status" in norm
    results.append(Result("P3 entries carry status", has_status,
                          "" if has_status else "no 'status' language found"))
    has_constraints = "constraint" in norm or "invariant" in norm or "inherits" in norm
    results.append(Result("P4 entries name inherited constraints", has_constraints,
                          "" if has_constraints else
                          "no constraints/invariants language found"))
    conf = os.path.join(path, "CONFORMANCE.md")
    results.append(Result("P5 conformance self-description present", os.path.isfile(conf),
                          conf if os.path.isfile(conf) else
                          "CONFORMANCE.md absent (warning-level: required once the repo "
                          "claims conformance or suspends an enforcement mechanism)"))
    return results


# --------------------------------------------------------------------------
# Reporting
# --------------------------------------------------------------------------

def print_results(title, results):
    print(title)
    print("-" * len(title))
    for r in results:
        mark = "[PASS]" if r.ok else "[FAIL]"
        line = "%s %s" % (mark, r.name)
        if r.detail:
            line += " -- " + r.detail
        print(line)
    print()


def print_delegation():
    delegated = [inv for inv in REGISTRY if inv.binding != "document"]
    print("Delegated invariants (labeled stand-ins; unbound until a repo or")
    print("instrument ships checks citing these IDs)")
    print("-" * 60)
    for inv in delegated:
        print("[DELEGATED:%s] %-7s %-10s %s" % (inv.binding, inv.id, inv.layer, inv.note))
    print()
    print("%d of %d registered invariants are delegated; this suite binds the"
          % (len(delegated), len(REGISTRY)))
    print("document layer only. A conformant repo cites the IDs above in its")
    print("own test suite; until then, its conformance is self-attested.")
    print()


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    ap = argparse.ArgumentParser(description="JFA conformance suite")
    ap.add_argument("--doc", default=os.path.join(here, "janus-facing-architecture.md"))
    ap.add_argument("--project", help="path to a project repo to check for the "
                                      "open-questions deliverable")
    ap.add_argument("--list", action="store_true", help="print the invariant registry")
    args = ap.parse_args()

    if args.list:
        for inv in REGISTRY:
            print("%-7s %-10s [%s] anchor='%s'" % (inv.id, inv.layer, inv.binding, inv.anchor))
            print("        enforcement: %s" % inv.note)
        return 0

    all_ok = True

    if args.project:
        results = check_project(args.project)
        print_results("PROJECT CHECKS: %s" % args.project, results)
        # P5 is warning-level; it reports but does not fail the run.
        all_ok = all(r.ok for r in results if not r.name.startswith("P5"))
    else:
        if not os.path.isfile(args.doc):
            print("document not found: %s" % args.doc)
            return 1
        doc = io.open(args.doc, encoding="utf-8").read()
        results = [check(doc) for check in DOC_CHECKS]
        print_results("DOCUMENT CHECKS: %s" % os.path.basename(args.doc), results)
        print_delegation()
        all_ok = all(r.ok for r in results)

    print("RESULT: %s" % ("all executed checks PASS" if all_ok else "FAILURES present"))
    return 0 if all_ok else 1


if __name__ == "__main__":
    sys.exit(main())
