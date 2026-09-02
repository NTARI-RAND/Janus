#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""JFA conformance suite — bound to the streamlined official document
(janus-facing-architecture.md, 2026-08-19 rebuild).

The prior instrument and its suite are preserved in Historical Docs as
*-pre-streamline-2026-08-19.*; their semantic IDs (SUB-*, REC-*, COV-*,
ECO-*, GOV-*, LEG-*) are retired. This suite's registry cites the new
document's clause numbers directly (e.g. "9.3", "4.2-filing"), because in
the streamlined document the numbering IS the identity.

What it checks, executably, right now (the DOCUMENT checks):
  * All nine sections are present, in order, with their expected titles.
  * Every layer section (3-7) carries the three tiers in order:
    Protocol, Orchestrator, Frontend.
  * Clause numbering is contiguous inside every section.
  * Every registered invariant's anchor phrase appears inside the clause
    that carries it, so the text and this registry cannot drift apart.
  * The nine lines that cannot be crossed (9.1-9.9) are all present.
  * Licensing is stated: AGPL-3.0 for software, CC BY-SA 4.0 for the
    specification.
  * The Economy & Information layer's primacy is stated in section 1 and
    again in section 7 ("the point of the stack").
  * The document is product-agnostic (no product names anywhere — the new
    document has no Schedule A exception zone) and carries no terms ruled
    off-architecture during the 2026-08-19 rebuild ("blockchain",
    "Credit Commons").
  * The document is PII-free beyond the organizational footer.
  * History is preserved: the document points at Historical Docs, and when
    the folder sits beside the document, the pre-streamline instrument is
    actually in it.

What it does NOT check, and says so (the DELEGATED registry):
  Invariants that bind running software (append-only logs, witnessing,
  zero-sum issuance, exit survival, ...) or a governance instrument
  (recallable delegates, the escrow-to-credit switch, ...) can only be
  enforced by tests living beside that code or that instrument. They are
  carried here as a registry with stable clause IDs and reported as
  delegated and unbound until a repo ships tests citing those IDs.
  Reporting them as "checked" from here would be self-attestation wearing
  a test runner — the stand-in is labeled instead.

Usage:
  python jfa-conformance-suite.py                 # check the document
  python jfa-conformance-suite.py --doc PATH      # check another copy
  python jfa-conformance-suite.py --list          # print the registry
  python jfa-conformance-suite.py --project PATH  # check a project repo's
                                                  # open-questions deliverable (8.8)

Exit code 0 when every executed check passes; 1 otherwise.

Software: AGPL-3.0 · Specification it verifies: CC BY-SA 4.0.
"""

import argparse
import glob
import io
import os
import re
import sys
from collections import namedtuple

# --------------------------------------------------------------------------
# The invariant registry.
#
# id       stable identifier a repo's test suite cites (e.g. "9.3",
#          "4.2-filing"); the leading number is the clause that carries it
# clause   the clause (or section) whose text must contain the anchor
# anchor   normalized phrase that MUST appear inside that clause (see
#          normalize)
# binding  where executable enforcement must live:
#            "document"       -- enforced fully by this suite (presence)
#            "implementation" -- enforced by tests beside the code
#            "instrument"     -- enforced by a governance instrument and
#                                its venue tooling
# note     where the delegated enforcement is expected to land
# --------------------------------------------------------------------------

Invariant = namedtuple("Invariant", "id clause anchor binding note")

REGISTRY = [
    # Section 1-2 — posture
    Invariant("1.3", "1.3", "without transmitting money at all",
              "document", "posture statement; carried by presence"),
    Invariant("2.3", "2.3", "disciplined by the cost of leaving it",
              "instrument", "governance instrument assigns each layer's discipline by exit cost"),
    Invariant("2.4", "2.4", "never split into rulers and ruled",
              "document", "posture statement; carried by presence"),
    # Section 3 — Substrate
    Invariant("3-single-account", "3", "produce and consume with the same single account",
              "implementation", "coordinator + frontend tests: one account carries both roles"),
    # Section 4 — Record
    Invariant("4.1-local-dialog", "4.1", "stays local to the parties own interfaces",
              "implementation", "commons schema tests: no narrative or identity fields"),
    Invariant("4.1-seal", "4.1", "sealed only when complete and quiescent",
              "implementation", "record tests: seal requires complete and quiescent; no clock-forced seal"),
    Invariant("4.1-replay", "4.1", "replayable from sealed records",
              "implementation", "economy tests: ledger state re-derivable from sealed records"),
    Invariant("4.2-own-log", "4.2", "keeps its own append only log",
              "implementation", "record tests: per-operator log; no update-in-place, no delete"),
    Invariant("4.2-countersigned", "4.2", "independent witnesses who countersign it",
              "implementation", "record tests: signed checkpoints countersigned by independent witnesses"),
    Invariant("4.2-no-central-chain", "4.2", "there is no central chain",
              "implementation", "record tests: no global chain or consensus layer over unrelated exchanges"),
    Invariant("4.2-lifecycle", "4.2", "committed to the record as it happens",
              "implementation", "lifecycle tests: filing/adjudication/resolution/seal each witnessed live"),
    Invariant("4.2-filing", "4.2", "independent of the operator who will adjudicate",
              "implementation", "filing tests: claim creation lands at an independent witness"),
    Invariant("4.3-auditor", "4.3", "audits records published by frontends",
              "implementation", "auditor program ships and verifies published records against the Record"),
    # Section 5 — Covenant
    Invariant("5.1-distribution", "5.1", "count of exchanges at each rating level",
              "implementation", "covenant tests: full distribution carried; no scalar score anywhere"),
    Invariant("5.1-whether", "5.1", "may this member trade on trust",
              "implementation", "covenant/economy boundary tests: reputation gates whether only"),
    # Section 6 — Governance
    Invariant("6.3-open-circles", "6.3", "open circles any member may join electing recallable delegates",
              "instrument", "recall, open-circle, and reopen-by-observation provisions present and usable"),
    # Section 7 — Economy & Information
    Invariant("7.1-zero-sum", "7.1", "always summing to zero",
              "implementation", "economy tests: each exchange moves two balances netting to zero"),
    Invariant("7.1-mirror", "7.1", "equal a replay of the sealed record",
              "implementation", "economy tests: balances equal replay of the sealed Record at all times"),
    Invariant("7.2-adjudicator-rated", "7.2", "rated on their adjudication conduct by both prosumers",
              "implementation", "covenant tests: adjudication conduct ratable by both parties"),
    Invariant("7.2-replay-recovery", "7.2", "replaced by replaying sealed records",
              "implementation", "failover tests: operator replaced by replay; credit positions preserved"),
    Invariant("7.2-atomic-cross", "7.2", "two sovereign spends bound atomically by a witnessed proof",
              "implementation", "cross-community tests: paired sovereign spends; no shared unit, no clearer"),
    Invariant("7.2-portability", "7.2", "by its own governance act",
              "instrument", "newcomer recognition only by recorded governance act, never by default"),
    Invariant("7.3-exit", "7.3", "survive any frontend",
              "implementation", "exit tests: positions and history survive frontend loss"),
    # Section 8 — the build checklist
    Invariant("8.1-chokepoint", "8.1", "no single host account or vendor whose removal could stop the network",
              "implementation", "deployment tests: participant-owned hardware; no hosting chokepoint"),
    Invariant("8.2-leaf", "8.2", "auditable whole",
              "implementation", "protocol repo: dependency audit in CI - standard library only; AGPL check"),
    Invariant("8.3-witnesses", "8.3", "label itself a stand in and not present itself as federated",
              "implementation", "deployment tests: fewer than two independent witnesses forces the label"),
    Invariant("8.7-escrow-switch", "8.7", "completed regulatory review",
              "instrument", "escrow-to-credit switch gated by approval, member notice, regulatory review"),
    Invariant("8.8-open-questions", "8.8", "living open questions document",
              "implementation", "per-project: open-questions file present and fresh (see --project)"),
    # Section 9 — the lines that cannot be crossed
    Invariant("9.1", "9.1", "forgive harm by annotating never by erasing",
              "implementation", "record tests: dismissal is annotation, never erasure"),
    Invariant("9.2", "9.2", "structural facts and references only",
              "implementation", "commons schema tests: no narratives, no identities"),
    Invariant("9.3", "9.3", "per operator logs countersigned by independent witnesses",
              "implementation", "record tests: no central chain"),
    Invariant("9.4", "9.4", "reputation is never one number",
              "implementation", "covenant tests: no averaging anywhere a rating is read"),
    Invariant("9.5", "9.5", "a separate limit decides how much",
              "implementation", "boundary tests: limit never derived from reputation"),
    Invariant("9.6", "9.6", "earned never bought and never redeemable for fiat",
              "implementation", "economy tests: no purchase path, no redemption path"),
    Invariant("9.7", "9.7", "no shared unit no conversion between communities",
              "implementation", "economy tests: sovereign units; no convertibility"),
    Invariant("9.8", "9.8", "value stays home only truth crosses",
              "implementation", "cross-community tests: only witnessed history crosses"),
    Invariant("9.9", "9.9", "everything is leaveable except the record of what happened",
              "implementation", "exit tests at every layer; the record outlives its operators"),
]

EXPECTED_TITLES = {
    1: "Why a community would build one",
    2: "The shape of the stack",
    3: "Substrate Layer",
    4: "Record Layer",
    5: "Covenant Layer",
    6: "Governance Layer",
    7: "Economy & Information Layer",
    8: "What it takes to build one",
    9: "The lines that cannot be crossed",
}

LAYER_SECTIONS = [3, 4, 5, 6, 7]
TIER_WORDS = ["protocol", "orchestrator", "frontend"]

# Product names must not appear anywhere: the streamlined document has no
# Schedule A exception zone. Off-architecture terms were ruled out during
# the 2026-08-19 rebuild (central chains; a named external protocol where
# the document now states the generic mechanism).
PRODUCT_NAMES = ["Sohocloud", "SoHoLINK", "Cloudy", "Slack", "Discord", "Mycelium",
                 "LBTAS", "Agrinet", "NTARI/OS", "GitHub", "Wix", "Fruitful"]
OFF_ARCHITECTURE_TERMS = ["blockchain", "credit commons"]


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


def parse_document(doc):
    """Split the document into numbered sections, each with an intro (text
    before the first clause) and an ordered mapping of clause id -> text."""
    sections = {}
    cur_sec, cur_clause = None, None
    for line in doc.splitlines():
        m = re.match(r"^## (\d+)\.\s+(.+?)\s*$", line)
        if m:
            cur_sec, cur_clause = int(m.group(1)), None
            sections[cur_sec] = {"title": m.group(2), "intro": "", "clauses": {}}
            continue
        if cur_sec is None:
            continue
        m = re.match(r"^\*\*(\d+\.\d+)\b", line)
        if m and int(m.group(1).split(".")[0]) == cur_sec:
            cur_clause = m.group(1)
            sections[cur_sec]["clauses"][cur_clause] = line[m.end():]
            continue
        if cur_clause is not None:
            sections[cur_sec]["clauses"][cur_clause] += "\n" + line
        else:
            sections[cur_sec]["intro"] += "\n" + line
    return sections


def clause_text(sections, clause):
    """Text of a clause id like '4.2', or a section intro for an id like '3'."""
    if "." in clause:
        sec = int(clause.split(".")[0])
        return sections.get(sec, {}).get("clauses", {}).get(clause)
    sec = int(clause)
    if sec not in sections:
        return None
    return sections[sec]["intro"]


# --------------------------------------------------------------------------
# Document checks
# --------------------------------------------------------------------------

def check_sections(sections):
    problems = []
    if sorted(sections) != list(range(1, 10)):
        problems.append("expected sections 1-9, found %s" % sorted(sections))
    for n, title in EXPECTED_TITLES.items():
        got = sections.get(n, {}).get("title")
        if got is not None and normalize(got) != normalize(title):
            problems.append("section %d titled '%s', expected '%s'" % (n, got, title))
    return Result("D1 nine sections present, ordered, titled", not problems,
                  "; ".join(problems))


def check_tiers(sections):
    problems = []
    for n in LAYER_SECTIONS:
        clauses = sections.get(n, {}).get("clauses", {})
        ids = list(clauses)
        expected = ["%d.%d" % (n, i) for i in (1, 2, 3)]
        if ids != expected:
            problems.append("section %d clauses %s, expected %s" % (n, ids, expected))
            continue
        for cid, word in zip(expected, TIER_WORDS):
            if not normalize(clauses[cid]).startswith(word):
                problems.append("clause %s does not open with '%s'" % (cid, word.title()))
    return Result("D2 layers 3-7 carry Protocol/Orchestrator/Frontend in order",
                  not problems, "; ".join(problems))


def check_numbering(sections):
    problems = []
    for n, sec in sorted(sections.items()):
        minors = [int(c.split(".")[1]) for c in sec["clauses"]]
        if minors != list(range(1, len(minors) + 1)):
            problems.append("section %d clause numbers not contiguous: %s" % (n, minors))
    return Result("D3 clause numbering contiguous in every section", not problems,
                  "; ".join(problems))


def check_registry_anchors(sections):
    problems = []
    for inv in REGISTRY:
        text = clause_text(sections, inv.clause)
        if text is None:
            problems.append("%s: clause %s not found" % (inv.id, inv.clause))
        elif inv.anchor not in normalize(text):
            problems.append("%s: anchor absent from clause %s" % (inv.id, inv.clause))
    return Result("D4 registered anchors present in their clauses", not problems,
                  "; ".join(problems) if problems
                  else "%d registered invariants anchored to their clauses" % len(REGISTRY))


def check_nine_lines(sections):
    clauses = sections.get(9, {}).get("clauses", {})
    expected = ["9.%d" % i for i in range(1, 10)]
    ok = list(clauses) == expected
    return Result("D5 the nine lines (9.1-9.9) intact", ok,
                  "" if ok else "found %s" % list(clauses))


def check_licensing(doc):
    norm = normalize(doc)
    problems = []
    if "affero general public license" not in norm and "agpl" not in norm:
        problems.append("AGPL not stated for the software")
    if "cc by sa 4 0" not in norm and "sharealike 4 0" not in norm:
        problems.append("CC BY-SA 4.0 not stated for the specification")
    return Result("D6 licensing stated (AGPL software, CC BY-SA 4.0 spec)",
                  not problems, "; ".join(problems))


def check_ei_primacy(sections):
    problems = []
    s1 = normalize(sections.get(1, {}).get("intro", "") +
                   " ".join(sections.get(1, {}).get("clauses", {}).values()))
    if "if no one is sharing economy and information there is no point" not in s1:
        problems.append("section 1 missing the no-point statement")
    s7 = normalize(sections.get(7, {}).get("intro", ""))
    if "the point of the stack" not in s7:
        problems.append("section 7 missing 'the point of the stack'")
    return Result("D7 E&I primacy stated in sections 1 and 7", not problems,
                  "; ".join(problems))


def check_product_agnosticism(doc):
    hits = [name for name in PRODUCT_NAMES
            if re.search(r"(?<![A-Za-z])" + re.escape(name) + r"(?![A-Za-z])", doc)]
    norm = normalize(doc)
    hits += [term for term in OFF_ARCHITECTURE_TERMS if term in norm]
    return Result("D8 no product names, no off-architecture terms", not hits,
                  ("found: " + ", ".join(hits)) if hits else "")


def check_no_pii(doc):
    emails = set(re.findall(r"[\w.+-]+@[\w-]+\.[\w.]+", doc))
    emails.discard("info@ntari.org")
    return Result("D9 no PII beyond the organizational footer", not emails,
                  ("unexpected addresses: " + ", ".join(sorted(emails))) if emails else "")


def check_history(doc, doc_path):
    problems = []
    if "historical docs" not in normalize(doc):
        problems.append("document does not point at Historical Docs")
    hist = os.path.join(os.path.dirname(os.path.abspath(doc_path)), "Historical Docs")
    detail = ""
    if os.path.isdir(hist):
        if not glob.glob(os.path.join(hist, "janus-facing-architecture-pre-*")):
            problems.append("Historical Docs holds no pre-* instrument")
        else:
            detail = "prior instrument preserved in Historical Docs"
    else:
        detail = "folder not beside this copy; text reference verified only"
    return Result("D10 history preserved and referenced", not problems,
                  "; ".join(problems) if problems else detail)


# --------------------------------------------------------------------------
# Per-project check: the living open-questions deliverable (8.8)
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
        results.append(Result("P1 open-questions document exists (8.8)", False,
                              "none of: " + ", ".join(candidates)))
        return results
    text = io.open(found, encoding="utf-8", errors="replace").read()
    results.append(Result("P1 open-questions document exists (8.8)", True, found))
    norm = normalize(text)
    entries = len(re.findall(r"^(?:#{2,4} |\- |\d+\. )", text, re.M))
    results.append(Result("P2 document has entries", entries > 0,
                          "%d candidate entries" % entries))
    has_status = "status" in norm
    results.append(Result("P3 entries carry status", has_status,
                          "" if has_status else "no 'status' language found"))
    has_constraints = ("constraint" in norm or "invariant" in norm
                       or "inherits" in norm or "clause" in norm)
    results.append(Result("P4 entries name inherited constraints", has_constraints,
                          "" if has_constraints else
                          "no constraints/clauses language found"))
    conf = os.path.join(path, "CONFORMANCE.md")
    results.append(Result("P5 conformance self-description present", os.path.isfile(conf),
                          conf if os.path.isfile(conf) else
                          "CONFORMANCE.md absent (warning-level: required once the repo "
                          "claims conformance)"))
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
        print("[DELEGATED:%s] %-22s %s" % (inv.binding, inv.id, inv.note))
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
            print("%-22s clause %-5s [%s] anchor='%s'"
                  % (inv.id, inv.clause, inv.binding, inv.anchor))
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
        sections = parse_document(doc)
        results = [
            check_sections(sections),
            check_tiers(sections),
            check_numbering(sections),
            check_registry_anchors(sections),
            check_nine_lines(sections),
            check_licensing(doc),
            check_ei_primacy(sections),
            check_product_agnosticism(doc),
            check_no_pii(doc),
            check_history(doc, args.doc),
        ]
        print_results("DOCUMENT CHECKS: %s" % os.path.basename(args.doc), results)
        print_delegation()
        all_ok = all(r.ok for r in results)

    print("RESULT: %s" % ("all executed checks PASS" if all_ok else "FAILURES present"))
    return 0 if all_ok else 1


if __name__ == "__main__":
    sys.exit(main())
