# JFA Concept Triage — 2026-08-24

On 2026-08-24 the official document was replaced by a new prosumership-first instrument (see [janus-facing-architecture.md](janus-facing-architecture.md)); the prior 9-section spec, its companion article, and its conformance suite were archived in Historical Docs as `*-pre-rebuild-2026-08-24.*`. This document records which concepts from the prior spec carry into the new JFA, which are modified, and which are retired. Decisions were made by NTARI stewardship against the archived suite's registry of 37 named invariants (old clause IDs cited below).

## Ground rule

**Retire by default.** The new document is the foundation. A concept from the prior spec is part of the new JFA only if this triage carries it forward. Nothing survives by inertia.

## Carried forward as-is

**Money**

- **Zero-sum issuance** (old 7.1) — money is created at the moment of exchange: one balance down, one up, always summing to zero.
- **No fiat bridge** (old 9.6) — credit is earned, never bought, and never redeemable for fiat.
- **Sovereign units** (old 9.7) — each community's currency is sovereign; no shared unit, no conversion between communities.
- **Escrow start** (old 8.7) — new deployments begin in collateralized escrow (no negative balances, no trust extended) and switch to mutual credit only after governance approval, membership notice, and a completed regulatory review.

**Record**

- **Append-only** (old 9.1) — the record is never rewritten; forgive harm by annotating, never by erasing.

**Reputation**

- **Never one number** (old 9.4, 5.1) — reputation is shown as the count of exchanges at each rating level, never averaged into a score.
- **Whether vs. how much** (old 9.5, 5.1) — reputation answers only "may this member trade on trust?"; a separate community-set limit decides how much credit. Merged, they recreate the credit score.
- **Adjudicators rated** (old 7.2) — whoever adjudicates a dispute is rated on their conduct by both parties involved.

**Cross-community**

- **Only truth crosses** (old 9.8, 1.3) — value stays home; no community's money ever enters another. What crosses boundaries is recorded history, not anything redeemable.

**Exit**

- **Cost-of-leaving rule** (old 2.3) — each layer is disciplined by the cost of leaving it: where leaving is cheap, competition disciplines; where dear, members vote; where impossible, decisions stay open to challenge.
- **No chokepoint** (old 8.1) — hardware members own; no single host, account, or vendor whose removal could stop the network.

**Governance**

- **Recallable delegates** (old 6.3, delegates portion) — open circles any member may join, electing delegates who can be recalled.

**Meta**

- **Uncrossable lines** — the new document will carry a boundary section rebuilt from this triage: a build that crosses one is not a smaller JFA, it is different software wearing the name.
- **Conformance suite** — an executable suite verifies the document's structure and keeps a registry of invariants cited by clause, labeling what it cannot check as delegated rather than pretending to check it.
- **Open-questions doc** (old 8.8) — every JFA project ships a living open-questions document; a stale one means the project stopped describing itself honestly. (This project's is [OPEN-QUESTIONS.md](OPEN-QUESTIONS.md).)
- **Lean auditable code** (old 8.2) — protocol code stays small, depends only on its language's standard library, and is auditable whole.

## Carried forward, modified

- **Record topology** (replaces old 9.3, 4.2) — the prior spec forbade a central chain. The new JFA reverses this deliberately: the record of what happened is hashed into **one public chain distributed across the substrate**. Alongside it, operators keep their own records, witnesses keep their own records, and **each party to a transaction keeps a record of their own**. The public chain is the record for those who are neither witness, nor operator, nor transactor. Four holders, one truth.
- **Atomic cross-community exchange** (old 7.2) — cross-community trade remains two sovereign spends bound atomically, with no shared unit, no clearer, and no exchange rate; **the public chain is what binds them**, replacing the old witnessed-proof mechanism.
- **Positions survive** (old 7.3, 9.9) — a member's balances and history survive any frontend; a community's records survive any operator. The mechanism is no longer ledger replay; it is the public chain plus the per-party records.
- **Coordinate + check** (old 2.4) — the same community both coordinates the economy and checks the coordination, never split into rulers and ruled. Kept as a governance principle. The name "Janus" now refers to production and consumption — every participant faces both — not to this principle.

## Retired

- **Replay / mirror** (old 4.1-replay, 7.1-mirror, 7.2-replay-recovery) — ledger state as a replay of sealed records, and operator recovery by replay. Explicitly retired.
- **No central chain** (old 9.3) — reversed by the new record topology above.
- **Countersigned checkpoints** (old 4.2-countersigned) — superseded as the integrity mechanism by the public chain plus per-party records.
- **Dispute lifecycle mechanics** (old 4.1-seal, 4.2-lifecycle, 4.2-filing) — the file → adjudicate → resolve → seal sequence and independent-witness filing were not re-adopted. Adjudication itself survives (adjudicators are rated); its mechanics were redesigned around the new record topology on 2026-08-25 — see [jfa-dispute-mechanics.md](jfa-dispute-mechanics.md).
- **Record auditor program** (old 4.3) — the dedicated auditor frontend was not re-adopted; the new document's Record frontend is record-keeping selected as a compute function by substrate prosumers.
- **History portability** (old 7.2-portability) — extending local credit to a newcomer by reading their recorded history from another network via a governance act. Not re-adopted.
- **Contestability language** (old 6.3, reopen-by-observation portion) — judged likely to cause ambiguities as worded; not carried. See open questions.
- **Standalone regulatory-submission clause** (old 6.1) — not re-adopted as its own clause; regulatory review survives inside the escrow-start rule (old 8.7), and legal structure lives in the new Governance layer's tiers.

## Open questions

Seeded into [OPEN-QUESTIONS.md](OPEN-QUESTIONS.md):

1. **Contestability** — dropped as worded; is the underlying idea (no decision permanently closed) wanted in different language, or dropped entirely?
2. **Privacy floor** (old 9.2, 4.1-local-dialog) — "hashes each transmission" keeps content out of the chain implicitly; should "no narratives, no identities in the shared record" be an explicit line?
3. **Single-account prosumership** (old 3-single-account) — one account carries both producer and consumer roles; implied by the new document's whole framing, not yet stated as a rule.
4. **Dispute mechanics** — adjudicators are rated, so adjudication exists; how disputes enter, resolve, and land on the public chain is undesigned.
5. **Witness minimum** (old 8.3) — witnesses keep their own records in the new topology; is there a minimum count, and is a deployment below it required to label itself a stand-in?

**Revision (2026-08-27):** the document was tightened to architecture only. Recallable delegates / open circles, reopen-decided-matters, and operator economic management beyond the credit limit (including default-rate publication) were judged bylaws-level detail and removed from the document; GOV-delegates, GOV-reopen and EI-operator-economy retired from the registry. The hybrid definition moved to the companion article (EI-hybrid retired). The record is now counted as six holders (REC-six-holders): each transactor, the operator, both witnesses, and the public chain. Governance orchestrator redefined as NTARI membership obtained by operating a federated instance.

**Resolutions (2026-08-24, same day):** 1 — carried in new language: "No decision of the membership is permanently closed; any member may bring a decided matter back before the body" (Governance frontend). 2 — restored as uncrossable line 7. 3 — stays implicit; not made a rule. 4 — withdrawn as a question; dispute mechanics designed 2026-08-25, recorded in [jfa-dispute-mechanics.md](jfa-dispute-mechanics.md). 5 — re-adopted: two independent witnesses minimum, stand-in labeling below it (Record layer).

## Adjustments the new document needs to reflect this triage

- The Record orchestrator's "enabling shared reputation and exchange" should be clarified so that what is shared across geography is truth and reputation, never a currency unit (sovereign units, only truth crosses).
- The public-chain topology (one chain on substrate; operator, witness, and transactor records beside it) belongs in the Record layer's tiers.
- The carried money, reputation, exit, and governance rules need a home — either woven into the layer sections or gathered into a rebuilt uncrossable-lines section.

---

*Network Theory Applied Research Institute, Inc. — info@ntari.org*
