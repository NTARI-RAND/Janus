# Amendment to the Official Document of the Janus Facing Architecture

**Draft · 2026-09-22 · proceeds under P1-001 §9.2**

Prepared for the delegates. The official document is amended only by a majority vote of the delegates, each federation having decided under §6.5, and the amendment is not adopted until the conformance suite passes against the amended text (§9.2). During bootstrap (§16.1) the founder board exercises the powers of the membership; an adoption so made is recorded in the governance registry (§9.5) as a bootstrap act and stands open to the membership under §2.3.

**Sequence.** This amendment precedes the P1-001 v1.1 draft. The v1.1 amendment dated the same day was superseded on 2026-09-30 by the consistency-pass v1.1 (bylaws PR #4), which carries the prosumer member's federation election in §3.9; that election rests on the membership path Section 1 names. Adopted in the other order, the bylaws would exceed the official document in the sense of §15.2 for the interval between the two acts. Where both are adopted in a single bootstrap act, this amendment is recorded first.

**Base.** This amendment is written against the document as it reads with the six editorial revisions of 2026-09-17 applied — pull requests #9 through #14, open at the time of drafting. Section 1 is unaffected by them. Section 2 is: see its own note.

---

## What this amendment does

1. Names prosumer standing as a path into membership of the stewardship organization, on the terms its bylaws provide. *(Governance layer, orchestrator tier.)* **Revised 2026-10-01:** by decision of the principal, the placement of the prosumer member's vote in the Covenant or Governance federation, and the weight of a federation's vote, are bylaw matters and are no longer carried in the amended text; P1-001 v1.1 §3.4, §3.8 and §3.9 (bylaws PR #4) carry them.
2. Names who adjudicates a dispute between a prosumer and the operator of its own platform: the witness layer, never the operator. *(Covenant layer.)* Severable from Section 1.
3. Instructs the conformance suite and the invariant registry.

It touches none of the twelve lines.

---

## Section 1 — Governance layer, orchestrator tier

**Current text.**

> Membership in the Network Theory Applied Research Institute, obtained by operating a federated instance of JFA software.

**Amended text.**

> Membership in the Network Theory Applied Research Institute, obtained by operating a federated instance of JFA software, or by participating as a prosumer on a federated platform as the organization's bylaws provide.

**Rationale.**

Institutional Discipline says that where leaving is dear, members get a vote. A prosumer's exit is dear once its credit is sovereign and non-convertible (Lines 2 and 3). The document gave that prosumer standing to challenge — through the Covenant tier's adjudication — but no vote; the only membership it named was the operator's, whose exit is the cheap one (fork the code, keep the record). The bylaws (P1-001 v1.0 §3.8) supplied the vote, but the document did not recognize the membership they created, §15.2 subordinates the bylaws to the document, and the bylaws' own preamble still describes Governance orchestration as the relationships among operator-members. A vote resting on an instrument the architecture can be read to forbid is a paper check. This section moves the vote into the architecture.

*Revised 2026-10-01: the two paragraphs that follow record reasoning that now lives in the bylaws (P1-001 v1.1 §3.4, §3.8, §3.9, §5.3). The amended text above no longer places the vote or fixes its weight; the architecture names the membership and the bylaws say where it sits.*

Two federations rather than one, because the two things a prosumer has an interest in are held in two places: the covenant — the social contract that governs how it is treated in trade — and governance — the audit of the stack against the standard. Each prosumer places its vote where its interest lies. The bylaws carry the mechanics (recognition, election, the annual change) and the document carries only the structure.

One vote per federation however large its roll is Shared Responsibility applied to weight: headcount decides within a federation and never beyond it, so no federation can be bought by recruitment. This last sentence of the amended text is severable; if the membership prefers to keep weight a bylaw matter, strike it and the rest stands.

**Registry.**

No registered invariant was anchored to the current sentence — the `GOV-*` identifiers were retired to the bylaws level on 2026-08-27 — so no anchor update under §9.16 is carried and no descendant identifier is issued. Proposed new invariants, bound to *instrument* (P1-001):

- `GOV-prosumer-membership` — a prosumer of a federated platform may take up membership of the stewardship organization on the terms its bylaws provide.

*Withdrawn 2026-10-01, before issue:* `GOV-federation-election` and `GOV-one-vote-per-federation`, proposed in the 2026-09-22 draft. The rules they would have bound are bylaw matters (P1-001 v1.1 §3.9, §3.8). Neither identifier was ever issued, so §9.16 does not reserve them.

---

## Section 2 — Covenant layer *(severable)*

**Current text.**

> Exit here is dear. Being cast out of the covenant costs a prosumer the one thing that cannot be rebuilt quickly — the count of exchanges at each rating level, earned one witnessed exchange at a time. That price is why expulsion is adjudicated rather than assumed. When apparent breaches of the covenant occur, platform operators adjudicate between their prosumers; disputes that cross platforms are adjudicated at the witness layer. Adjudicators are rated on their conduct by both prosumers/operators involved — the referees stand inside the reputation system they enforce.

**Amended text.**

> Exit here is dear. Being cast out of the covenant costs a prosumer the one thing that cannot be rebuilt quickly — the count of exchanges at each rating level, earned one witnessed exchange at a time. That price is why expulsion is adjudicated rather than assumed. When apparent breaches of the covenant occur, platform operators adjudicate between their prosumers; disputes that cross platforms, and disputes between a prosumer and the operator of its own platform, are adjudicated at the witness layer — no operator adjudicates a dispute to which it is a party. Adjudicators are rated on their conduct by both prosumers/operators involved — the referees stand inside the reputation system they enforce.

**Note on the target.** These sentences stood in the Covenant layer's orchestrator tier until the editorial revision of 2026-09-17, which moved them into the layer's own paragraph, where the exit cost that explains them is stated (PR #9), and wrote out "Economy & Information" in the tier they left (PR #13). The amendment is applied where the sentences now stand. Nothing of its substance turns on the move: the same two sentences are amended in the same way, and the orchestrator tier is left as the editorial revision leaves it.

**Rationale.**

The document named who adjudicates two of three cases. The third — a prosumer against its own operator — is the case that arises at the credit limit, at custody, and at the stage change, where the prosumer's exit is dearest; and the operator is not neutral in it by the document's own reasoning for cross-platform disputes. Because the document was silent, the bylaws may fill the gap without overriding it; naming the witness layer here nonetheless protects P1-001 §10.9 under §15.2 and lets the rule be registered as an invariant rather than carried as a bylaw alone.

**Registry.**

Proposed `COV-operator-dispute-witnesses` — a dispute between a prosumer and the operator of its own platform is adjudicated at the witness layer, never by that operator. Bound to *instrument* (P1-001 §10.9) and to *implementation* (a platform's dispute routing). Lineage: `COV-operators-adjudicate`, `COV-witness-adjudication`.

---

## Section 3 — Conformance

Run `python jfa-conformance-suite.py` against the amended text before the delegates' vote closes; the amendment is not adopted until it passes (§9.2). The registry changes above are made in the same act (§9.16); an identifier once issued is never reused. A failing run is entered in `OPEN-QUESTIONS.md` and stands as business in the Governance Federation Channel under §9.18 until resolved by repair of the suite or by amendment of the text.

---

## Not amended, noted

**Line 10.** The P1-001 v1.1 amendment adds ratification by the deployment's prosumers as a condition of a switch to *full* mutual credit (§11.1(d)). Line 10 states minimum conditions and is not crossed by an added one, so the Line is left as it stands. If the membership later judges that the ratification should bind every conforming implementation and not only the Institute's members, it belongs in Line 10 and comes back under §9.2.

**Record layer, witness minimum.** Rotation of the standing witnesses, the third witness drawn per dispute, and the definition of independence are instrument-level (P1-001 §3.2(b), §3.10, §10.2, §10.9) and do not change the document's two-witness floor.

**Structure article, "Between Federations."** The bylaws' appendix sources prosumer membership to this article, which is held in NTARI's document store and not published. Publish it, or fold its operative content into the amended Governance tier; a demand sourced to an unpublished paper is self-attested under §9.6.

---

## Provenance of demands

*Informative, not operative.*

| Section | Demand | Source |
| --- | --- | --- |
| §1 | Where leaving is dear, members get a vote; the prosumer's exit is dear under sovereign, non-convertible credit | Official document, Principles (Institutional Discipline); Lines 2, 3 |
| §1 | The community that coordinates is the community that checks | Official document, Principles (Shared Responsibility); P1-001 §2.1 |
| §1 | Bylaws may not override the official document | P1-001 §15.2; §1.5 |
| §1 | Prosumer standing ripens into membership; the vote comes with it | P1-001 §3.8, §4.2; structure article, "Between Federations" (unpublished) |
| §1 | One vote per federation; headcount decides within and never beyond | P1-001 §3.4, §5.3 |
| §2 | No one is neutral in their own case | Official document, Covenant Layer (cross-platform reasoning); P1-001 §10.9 |
| §2 | A power names its check | P1-001 §2.2 |
| §3 | Registry changes are amendments; identifiers never reused; failing suite is business | P1-001 §9.2, §9.16, §9.18 |

---

## Adoption record *(to be completed)*

- Notice published to the Governance Federation Channel under §6.4: ________
- Federation decisions under §6.5 — Substrate: ____ Record: ____ Covenant: ____ Governance: ____ E&I: ____
- Delegates' vote under §9.2: ________
- Conformance suite result against the amended text: ________
- Registry changes recorded under §9.16: ________
- Recorded in the governance registry under §9.5 (bootstrap act, if so): ________

---

*Network Theory Applied Research Institute, Inc. — EIN 92-3047136 — Louisville, Kentucky — <info@ntari.org>*

*Specification: CC BY-SA 4.0*
