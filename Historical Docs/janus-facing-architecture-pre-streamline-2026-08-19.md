# Janus-Facing Architecture

**A technical constitution.** Network Theory Applied Research Institute.

**Recitals.** The surplus exists; coordination fails: goods move toward money rather than need, and the administered alternative rebuilds the unanswerable center. Deliberation moves slower than the power it is meant to check. This instrument therefore constitutes coordination infrastructure that moves real goods and services against real needs without concentrating the power to decide who may have what. The argument for these articles — the grounding in Acemoglu and Robinson, Scott, and Ostrom; the history; the assessment of adjacent designs — is carried by the companion commentary ([jfa-commentary.md](jfa-commentary.md)), which explains this instrument and never governs it.

**Rules of construction.** Where a rule says MUST, MUST NOT, or MAY, the keyword carries the force RFC 2119 gives it. Every invariant carries a stable identifier, `SUB-1` through `LEG-2`, printed beside its clause; the executable conformance suite shipped beside this instrument holds the registry and verifies the pairing, and a conformant repository cites those identifiers in its own test suite — until it does, its conformance is self-attested. This instrument names roles and mechanisms, never products; implementations bind to roles, and the steward's own bindings are recorded in Schedule A, which describes and never governs. This is the constitution, not the wire specification: schemas, formats, and state machines live with the protocol artifacts that bind to these roles. Where an implementation and this instrument disagree, either the implementation is fixed or this instrument is amended in the open.

---

## Article I — Definitions

*Definitions orient; the normative text below governs. Every term names a role or a mechanism, never a product.*

- **Anchor commitment** — a structural fact or reference committed to the commons; never a narrative, never PII.
- **Append-only** — corrections are new entries; there is no update-in-place and no delete.
- **Assessment scale** — the harm-surfacing rating scale (Leveson-derived); the lowest rating is the breach itself.
- **Checkpoint** — an operator-signed, monotonic commitment to the current state of its log.
- **Claim lifecycle** — file → adjudicate → resolve → seal, each transition witnessed as it happens.
- **Coordination protocol** — the shared wire language of the network, and the specification no one can cheaply leave; kept minimal, legible, and permanently contested for exactly that reason.
- **Coordinator** — the node-side role that runs the coordination protocol on a community's infrastructure and declares its fees legibly.
- **Countersigner** — an independent party that countersigns checkpoints so that showing two histories becomes provable; a countersigner confers no authority.
- **Covenant** — trust as a standing promise not to harm, not a score; a member is in good standing or in breach.
- **Cross-operator corroboration** — operator recognition by other, independent operators; operators under common control corroborate nothing.
- **Denominated, not backed** — the fiat peg is a unit of account for legibility, never a promise of redemption.
- **Dependency leaf** — software that depends on nothing but its language's standard library, so it can be reimplemented and audited whole.
- **Dialog** — the atomic unit of the record; it seals only when complete and quiescent.
- **Dwell** — how long a claim has sat open past a movable threshold; a readable fact, never a verdict.
- **Earned, never bought; non-redeemable** — the credit unit is issued only for value provided and can never be purchased or cashed out.
- **Equivocation** — an operator showing different histories to different audiences; two validly-signed, mutually-inconsistent checkpoints are the portable proof.
- **Escrow phase** — the pre-credit settlement mode: collateralized in advance, no balance ever negative, no trust extended.
- **Federation** — the standing open circle of the members operating a given layer, electing recallable executives answerable for that layer.
- **Front end** — the member-facing application; it speaks the node-side surface on behalf of member machines, and it is leaveable by design.
- **Full distribution** — reputation carried as the count at each rating level beside the total; never averaged into one figure.
- **Genesis operator set** — the founding steward's standing representatives, serving as the bootstrap trust root before corroboration binds.
- **Governance venue** — where deliberation and voting happen; it must itself be leaveable substrate.
- **Hosting chokepoint** — any single host, account, or vendor whose revocation could stop the network; forbidden as an end-state.
- **Janus-facing** — the permanent two-way posture: one face coordinates, the other checks the coordination — two functions carried and exchanged by one community, never two populations.
- **Knowledge-claim anchoring** — the record extended to empirical and commercial claims, which become citable without any center certifying them true.
- **Layer** — one of the five strata of the stack: Substrate, Record, Covenant, Governance, Education & Information.
- **Legibility ladder** — the seven mechanized rungs that bind plain language to running code.
- **Limit** — the separate instrument that caps how large a commitment an honest member may take on; never derived from the harm distribution.
- **Maximum Observational Diversity (MOD)** — maintaining a false pattern grows expensive as independent, diverse observers multiply.
- **Minimal entrenched core** — the few commitments locked behind a double lock: open source; privacy-first and data sovereignty; no surveillance economics.
- **Minimum Sustainable Projection (MSP)** — build on the fewest assumptions, so truth-aligned behavior is the path of least resistance and dishonesty costs more than it pays.
- **Mutual credit** — money created at the moment of exchange: one balance down, one up, the sum always zero, backed by covenant and capacity rather than reserves.
- **Mutual credit network** — an economy in which members extend value to one another against a covenant not to harm, on a record no one can rewrite, on hardware no one can revoke, with no central issuer of money and no central judge of trust.
- **Named interim** — a non-conformant arrangement tolerated only while its exit stays committed and progressing; a stalled interim is a standing violation.
- **One-person-one-vote qualifier** — where a status gates the electorate, it qualifies a person's single vote and never multiplies it.
- **Open circles; recallable delegates** — deliberative channels any member may join, electing representatives whom their channel, or a supermajority of the membership, can recall.
- **Open-questions document** — the living per-project deliverable naming what remains unresolved about the project's future.
- **Operator-federation** — the governing electorate: corroborated-active operators, one vote per person.
- **Orchestrator** — the running service that executes a layer's protocol.
- **Presentation sovereignty** — styling ships as user-editable data separate from application logic, and every participant holds the right to restyle their own render, self-view only.
- **Record** — a witnessed, append-only memory of what happened, including the full claim lifecycle.
- **Relation type** — the typing of ratings and claims: trade, adjudication-conduct, verdict-satisfaction.
- **Seal** — the closing of a dialog into the permanent record; never forced by a clock.
- **Sovereign currency** — each platform issues and clears in its own unit, with no cross-platform convertibility.
- **Stand-in label** — the mandatory marker on any deployment running with fewer than two independent countersigners.
- **Standing contestation** — ratification is never final: any member may reopen a decided matter with an observation.
- **Steward** — the named, internally-accountable body that holds the one layer with no exit.
- **Substack** — the three roles every layer carries: a protocol, an orchestrator, and a user interface.
- **Sybil** — one actor posing as many, to multiply an influence the system meant to hand out once.
- **Symmetry** — every claim is answerable and every dismissal is an annotation.
- **Tension protocol** — the builder's stop-rule of Article VIII.
- **The one rule** — govern every layer by the cost of leaving it.

---

## Article II — The Stack

**II.1** The stack is five layers: Substrate, Record, Covenant, Governance, Education & Information. Each layer is sovereign only because the one beneath it is; a mechanism in a higher layer depends only on layers beneath it. Build bottom-up; an inverted order leaves every layer above the inversion decorative.

**II.2** Every layer carries the same substack: a protocol, an orchestrator, and a user interface.

**II.3** The one rule governs the whole: each layer is disciplined by the cost of leaving it — exit where leaving is cheap, voice where it is dear, standing contestation where it is impossible.

**II.4** The stack is Janus-facing: coordinating and checking are two functions carried and exchanged continuously by one community, never two populations. The balance between them is held by motion, not by any end-state.

**II.5** What the stack constitutes is a mutual credit network. Its three concentrable functions — the scorer, the issuer, the ledger — are held apart by Articles V, VII, and IV respectively; concentrating any one of them rebuilds the bank.

**II.6** The requirements of this instrument implement Maximum Observational Diversity (MOD) and Minimum Sustainable Projection (MSP): independence multiplies observers until a false pattern grows too expensive to maintain, and minimal assumption makes truth-aligned behavior the path of least resistance. Claims are anchored, never certified.

---

## Article III — Substrate

**III.1** The platform MUST run, or be able to run, on infrastructure its participants can own; **no unremovable hosting chokepoint.** `SUB-1`

**III.2** The coordination protocol is a **dependency leaf.** It depends on nothing but its language's standard library; the coordinator and the front ends depend on the protocol and never on each other. `SUB-2`

**III.3** **Single participant identity.** One account carries the simultaneous roles of contributor and consumer; never split a person into a producer identity and a consumer identity. `SUB-3`

**III.4** **Persons never appear on the coordination wire.** Front ends speak the node-side surface on behalf of member machines; long-term the coordinator models no persons at all. `SUB-4`

**III.5** The coordinator declares its fees legibly: coordinator-authored, member-readable, contestable.

**III.6** Presentation sovereignty is a right of every participant: styling ships as user-editable data separate from application logic, restyling is self-view only, and nothing about a participant's styling enters the commons or any other participant's view. Its five requirements, enforced at import and paste:

- (a) **Scripts never; markup sandboxed.** No theme executes. `SUB-5`
- (b) **No remote fetches from user styles** — `url()`, `@import`, `@font-face` stripped or blocked at import. `SUB-6`
- (c) **Reset-to-default lives outside the styleable surface.** `SUB-7`
- (d) **Styles are plain, exportable artifacts** — never an opaque blob. `SUB-8`
- (e) **Shipped or hosted themes inherit the carve-out:** no shipped theme occludes covenant surfaces. `SUB-9`

**III.7** The default theme carries the WCAG 2.2 AA floor, and the style editor itself meets it.

---

## Article IV — Record

**IV.1** The ledger MUST be **append-only.** `REC-1`

**IV.2** A front end MAY forgive a harm; it MUST NOT hide one. A dismissal is a new visible annotation, never an erasure. `REC-2`

**IV.3** The commons MUST NOT contain PII. Anchor commitments carry structural facts and references only; narratives and identities live in the erasable, interface-local layer. `REC-3`

**IV.4** **The atomic unit is the dialog.** It seals only when complete (every rating owed exists; a non-rater is assigned a marked default) and quiescent (no open dispute). `REC-4`

**IV.5** Each operator keeps its **own log.** There MUST NOT be one global chain or a consensus layer over unrelated exchanges; non-equivocation comes from **witnessing** — signed, monotonic checkpoints to independent countersigners. Equivocation is thereby detectable, attributable, and portable, never prevented. `REC-5`

**IV.6** **A countersigner confers no authority.** The record orchestrator may schedule, relay, cache, and serve inclusion proofs; it MUST NOT decide which countersigners count, which checkpoint is official, or gate settlement on its blessing. `REC-6`

**IV.7** **The witnessed unit is the claim lifecycle, not only the sealed verdict.** Filing, adjudication, resolution, and seal each commit to the witnessed record as they happen. `REC-7`

**IV.8** **A harm claim's filing commitment is made at an independent countersigner,** upstream of the adjudicating operator — a bounded exception accepting exactly one write, claim-creation, and nothing else; it MUST NOT become a second log. (Liveness dependency: problem 8.) `REC-8`

**IV.9** **Ratings and claims carry a relation type.** The record MUST distinguish trade, adjudication-conduct, and verdict-satisfaction; no reader may collapse them into one figure. `REC-9`

**IV.10** PII discipline binds hardest at filing — the filing commitment witnesses a hash, a type, a timestamp, and an exchange reference, never a narrative or an identity — and **a clock never force-seals a dialog:** an unanswered claim stays open, and only its dwell is a readable fact. `REC-10`

**IV.11** A deployment with fewer than two independent countersigners carries the stand-in label and does not present itself as federated.

**IV.12** A reader of the lifecycle reads structure — dwell distributions, dismissal patterns, collusion signatures — never a rating average. Any analytic output is a contestable flag, never an automatic exclusion, and a read taken over fewer than two independent countersigners is named self-attested.

---

## Article V — Covenant

**V.1** Reputation MUST NOT be averaged into a score. Carry the **full distribution** — the count at each level beside the total. `COV-1`

**V.2** On the assessment scale, the **lowest rating is the breach itself,** not a debit against a total. `COV-2`

**V.3** The covenant MUST be **symmetric:** every claim is answerable; dismissals are annotations. A rated party with no answer is a symmetry breach — an adjudicator rated without recourse is the one known instance, and it is fixed, not shipped. `COV-3`

**V.4** Reputation gates **whether** a member transacts on trust, never **how much.** The limit is a separate instrument of Article VII: the covenant secures honesty, the limit sizes capacity, and merging them rebuilds the credit score. `COV-4`

**V.5** Reputation is **per-platform and non-portable by default.** Portability is a governance decision (problem 5), never an implementation default. `COV-5`

**V.6** When reputation informs anything beyond whether-a-member-transacts — credit, citation weight, or governance standing — Sybil-resistance MUST be settled first (problem 4), and governance standing read from conduct is **structure, never a score.** `COV-6`

---

## Article VI — Governance

**VI.1** Govern each layer **by the cost of leaving it:** voice at the peer layer, exit at the front ends and substrate, standing contestation at the core. Keep the core minimal, so capturing it pays little. `GOV-1`

**VI.2** **Name the steward.** The one layer with no exit is held by a named, internally-accountable body, its board filled from the bottom with recallable delegates of open circles, disciplined by entrenchment, the expensive-but-real fork, and standing internal opposition. `GOV-2`

**VI.3** **Stewardship mirrors the stack** — layer-aligned stewardship. `GOV-3` Five standing offices align one-to-one with the five layers: the workspace administration stewards the Substrate; the secretariat stewards the Record; the presidency stewards the Covenant; the vice-presidency stewards Governance, holding an audit authority that is investigative and never dispositive; the treasury stewards Education & Information. Stewardship is answerability, not authority: no steward adjudicates its layer's content, and no office holds two layers.

**VI.4** The minimal entrenched core is entrenched **behind a double lock** — a supermajority of all voting members plus unanimity of the stewarding board — and **nowhere more.** `GOV-4`

**VI.5** **Delegates are recallable; circles are open.** `GOV-5`

**VI.6** Standing contestation is preserved: any member may reopen a decided matter with an observation, a single documented harm reopens a synthesis, and deliberation **never averages dissent away.** `GOV-6`

**VI.7** **One person, one vote** — no proxy, no delegation; a gating status is a qualifier, never a multiplier. `GOV-7`

**VI.8** Membership in the steward is qualified by operation of any part of the stack, never by purchase. The governing electorate is the operator-federation; recognition matures from the genesis operator set to cross-operator corroboration, which excludes operators under common control. The franchise is held under a conduct standard — no gaming, no tampering, no harmful environments — and one adjudicated harm from a genuine counterparty can end it; no volume of good conduct absolves it. Non-operating members are non-mute: a real adjudicated harm can cost an operator its eligibility, and exit and recall remain theirs. A purchase-qualified franchise is conformant only as a named interim with a committed sunset.

**VI.9** **Legibility is an output, not a comment.** `GOV-8` Every project **ships a living open-questions document** — equal in standing to its code; staleness is nonconformance; a question that binds architecturally is promoted to Article IX. `GOV-9`

**VI.10** Provenance is inbound = outbound: **every contribution enters the copyleft commons** and cannot be reclaimed; no contributor license agreement, no assignment to a center; PII is not a contribution. An enforcement mechanism may suspend only as a named interim with committed reinstatement, and the gap is permanent for the commits made inside it. `GOV-10`

**VI.11** The governance venue **must itself be leaveable substrate.** A proprietary hosted venue is conformant only as a named interim with a committed exit, and a stalled interim is a standing violation. `GOV-11`

**VI.12** The balance between coordinating and checking is **held by motion**; do not build for a static end-state. `GOV-12`

**VI.13** **Every orchestrator federates automatically.** A layer's orchestrator MUST discover its peers and communicate with the applicable federation's message board in the governance frontend without manual attachment. `GOV-13`

**VI.14** The legibility ladder binds plain language to running code, and each rung MUST be **mechanically bound to the rung below** it — an unbound explanation is a second source of truth, born drifting. `LEG-1`

1. Decisions explain themselves at the point of use: every governance-relevant output ships a receipt — which rule fired, on which inputs, linked to the rule's plain statement.
2. Rules live as data, not code: policy is declarative, rendered as plain tables and sentences, diffable by anyone.
3. Policy versions commit to the witnessed record, each with a plain-language changelog entry.
4. The spec is the constitution, written in prose — normative plain language first, wire format second.
5. Conformance tests bind the prose to the code: every normative sentence maps to an executable check.
6. The trusted core stays small and boring: a dependency-leaf protocol of a few thousand literate lines.
7. Builds are reproducible; release hashes are witnessed.

**VI.15** A machine reading aid MUST **remain a reading aid, never an oracle;** a "verified true" explanation from any model is a forbidden truth authority, and an aid's claims stay checkable against the spec and the conformance suite. `LEG-2`

---

## Article VII — Education & Information

**VII.1** Balances MUST be a **deterministic function of the sealed record;** each sealed exchange moves two balances that net to zero. `ECO-1`

**VII.2** Issuance MUST be gated by the covenant and **capped by a separate limit;** the limit MUST NOT be derived from the harm distribution. `ECO-2`

**VII.3** Each platform's currency is **sovereign and separate:** no cross-platform currency, no fixed convertibility. `ECO-3`

**VII.4** The unit is denominated, not backed: fiat denomination is a unit of account only, and **denomination is NOT redemption** — the unit is earned, never bought, non-redeemable, spend-only. `ECO-4`

**VII.5** Settlement begins as the escrow phase, and the escrow-to-credit switch is a **governed configuration change:** board approval, membership notice, and a completed regulatory review before any issuance. Credit is earned, never bought, and enters only behind a value proposition strong enough to pull migration — never pushed by an interface. `ECO-5`

**VII.6** **Value stays home; only truth crosses.** Cross-economy exchange is two sovereign spends bound atomically by a witnessed proof — no shared unit, no central clearer, no administered rate. `ECO-6`

**VII.7** Knowledge-claim anchoring extends the record to empirical and commercial claims: anchored, a claim is citable, and its claimant is ratable under the covenant like any counterparty.

**VII.8** No truth authority: the commons anchors and weighs claims and never adjudicates fact. Citation is legible and forkable. Reputation is earned, never sold — no paid placement, no bought rating. Sybil-resistance precedes citation-weight (problem 4).

**VII.9** This layer does not become a rating agency for truth, an ad market for visibility, or a credentialing monopoly. Discovery stays federated, cited, and contestable.

---

## Article VIII — Conformance

A system is conformant to Janus-Facing Architecture only if all seven checks hold; a system that fails one is not a smaller version of this architecture — it is different software wearing its vocabulary.

1. **Mutual credit, not banking.** It is, or governs, a member-issued mutual credit economy, gated by covenant and capped by a separate limit; its currency is sovereign, separate, denominated-not-backed, non-convertible across platforms, never redeemable for fiat; and credit is earned, never bought.
2. **Sovereign substrate.** It runs, or can run, on infrastructure its participants can own — no unremovable hosting chokepoint.
3. **Witnessed, legible record.** Its record is immutable, tamper-evident, witnessed against equivocation — including the claim lifecycle, from filing — and PII-free in the commons; harm can be forgiven but never hidden.
4. **Reputation as covenant.** Its reputation is a covenant, not a score — a full distribution that never averages, contestable in both directions, typed by relation, gating whether-not-how-much.
5. **Governed by the cost of leaving.** Voice where contest is cheap, exit where it is dear, standing contestation at the core — and presentation is separable, with every participant holding the right to restyle their own render.
6. **A minimal, contested, stewarded core.** The specification is kept minimal, entrenched only where legibility and portability demand it, permanently contestable, and held by a named, internally-accountable steward.
7. **Legible above all.** Its legibility is mechanized, not promised — decision receipts, policy as data with witnessed versions, prose bound to code by conformance checks, reproducible builds; its canon is preserved and broadcast redundantly enough that forking it does not depend on any single host's goodwill; and it ships a living open-questions document naming what remains unresolved — staleness is nonconformance.

### Requests to refuse or flag

- *"Let users cash out / redeem credits for dollars."* → Redeemability. The unit is spend-only.
- *"Let users buy credits with dollars."* → Purchasable currency / deposit-taking. The unit is earned, never bought.
- *"Convert one economy's currency to another's at a fixed rate."* → Currency merger. Cross-economy trade is atomic barter over a witnessed proof, never a shared unit.
- *"Show a single reputation score / average the ratings."* → Rebuilds the score the covenant forbids.
- *"Raise a member's credit limit when their reputation is good."* → Merges covenant with limit. Keep them separate.
- *"Store the conversation or dispute narrative on the shared ledger."* → PII in the commons. Anchor references only.
- *"Edit or delete a record to resolve a dispute."* → Erasure. Annotate; never erase.
- *"Make one global ledger so everything is consistent."* → Reintroduces the global authority. Per-operator logs plus countersigning.
- *"Route all checkpoints / all countersigning through one orchestrator."* → Makes the orchestrator a chokepoint. It relays and serves proofs; it never adjudicates.
- *"Witness only the final sealed adjudication / deliver the lifecycle as one block."* → Self-attestation wearing a hash. Witness each transition as it happens, from filing.
- *"Let the front end mint the filing record."* → Intake capture. File at an independent countersigner.
- *"Gate voting on an operator's average rating / show a single operator score."* → Rebuilds the average. Read conduct structure — dwell, dismissal patterns — not a rating count.
- *"Auto-remove an operator when the scan flags it."* → Makes the scanner an authority. The scan flags; adjudication decides; the operator contests.
- *"Just run it all on our one server or cloud account for now."* → Hosting chokepoint.
- *"Let a vendor pay to rank higher / have the network certify which claim is true."* → Buys reputation / installs a truth authority.
- *"Write the plain-English explainer as a separate doc / document it after launch."* → A second source of truth, born drifting. Explanation is generated from, or conformance-bound to, the artifact it explains.
- *"Let themes run scripts / load remote assets."* → Self-XSS and beaconing. Article III.6(a)–(b); refuse.
- *"Ship a starter theme that tidies away the harm distribution."* → System-authored occlusion. Article III.6(e); refuse.

A quick test: if a change makes a layer harder to leave, makes the record easier to rewrite, makes credit convertible to or purchasable with fiat, makes some center the arbiter of value or truth, or lets an operator's own attestation stand in for an independent countersigner — it is almost certainly off-architecture. Flag it.

### The tension protocol

While implementing, if you notice yourself doing any of the following, stop:

- reframing a constraint of this architecture so a feature becomes convenient,
- implementing a stand-in without labeling it,
- routing around one of the open matters of Article IX instead of noting it.

When you hit one: name the tension, attach it to the relevant clause or open matter, and propose the minimal conformant move. Surface it; do not absorb it.

### Amendment

This instrument is unversioned: it is the standing description of the architecture, amended in the open when the architecture is. Every normative clause pairs with a registry identifier in the conformance suite, and an amendment that adds, removes, or rewords a clause amends the registry in the same change. Schedule A is descriptive and is updated by the steward without amendment of the articles. The values calls named in Article IX belong to the people who live with the outcomes, not to this instrument.

---

## Article IX — Open matters

Unresolved questions are constitutional matter: they are numbered, public, and load-bearing, and every project's open-questions document feeds this article. For each — the problem, the constraints any resolution inherits, and where it stands.

**1. Equivocation is detectable, not prevented.** Detection is only as strong as a verifier's reach to independent countersigners. A fix must not introduce a larger authority at the core. *Status:* permanent, managed; the detection machinery is built.

**2. The countersigner layer.** Core specified and built; an independent countersigner joins by appending a signature. Open: federation in fact — two or more independent, long-lived countersigners, durable countersigner state, lifecycle witnessing end to end. *Status:* the single highest-leverage build; problem 4's read runs on labeled stand-ins until it lands.

**3. Mutual credit.** The governed switch and its walls are codified. Open: the regulatory read, and Sybil-first. *Status:* narrowed; both gates still closed.

**4. The governed and the governing.** Resolved in design by the operator-federation of Article VI.8; adopted in the steward's instrument. Open: honest conduct evidence (depends on problem 2), multi-account Sybil in the interim, the cold-start window, the false-positive tax. *Status:* politically solved; evidentially open.

**5. Reputation portability.** Vertical conduct reads are settled; horizontal portability is deliberately undecided, and the covenant ships non-portable. A fix must need only a portable identity and a readable witnessed log — never a shared money supply. *Status:* deliberately undecided.

**6. Computation and claim honesty.** Whether a match, price, yield, or finding was fair is unverified, checked only by legibility and exit. A fix must not require a central verifier. *Status:* open; anchor inputs and outputs, never certify.

**7. Mechanical versus economic exit.** Sovereign compute buys the right to leave, not the capacity; fees and reputation cold-start recentralize. A fix must not concentrate the coordinator. *Status:* mechanical exit demonstrated by independent reimplementation; economic exit open.

**8. The countersigner cost floor.** Independence requirements price out the low-resource operator, and filing-liveness can silence exactly the users most exposed. A fix must not concentrate countersigning in the steward or a few large operators. *Status:* open; separating countersigning from operating — membership-as-countersigning — is the watched lever.

Problems 2, 4, 7, and 8 meet at the countersigner layer; record-integrity, governance-legitimacy, and substrate-economics are jointly decided there.

---

## Schedule A — The NTARI substack

*Descriptive, never normative: the steward's current bindings of products to the roles of this instrument. Updated by the steward without amendment of the articles.*

| Layer | Protocol | Orchestrator | User interface |
|---|---|---|---|
| Substrate | Sohocloud | SoHoLINK | Cloudy Market |
| Record | Anchor | Witness | — (served by the E&I front end) |
| Covenant | LBTAS | LBTAS API | Covenant Broadcast |
| Governance | the 501(c)(3) instrument | the steward's self-hosted JFA stack | NTARI/OS |
| Education & Information | the standards registers (protocol, orchestrator, front-end standards) | Fruitful Management LLC operations | the public marketplace and education surfaces |

Notes of record:

- **Witness** runs the adjudication lifecycle and nothing more: it receives adjudication calls originating from the E&I front end, commits each transition, relays checkpoints to countersigners, and serves proofs, within the bounds of IV.6 and IV.8; a claim's filing lands at an instance independent of the adjudicating operator, a routing VI.13 makes routine. The Record layer is headless by design: a second, record-owned surface would be a second place to shape intake.
- **Fruitful Management LLC** is wholly owned by and operated for the 501(c)(3); it presents the stack publicly at market speed and interoperates with any market entrant using the same software, on the published standards registers.
- **NTARI/OS** carries each federation's message board; every layer's orchestrator reports into it under VI.13. Its auditing toolset confers no authority: a flag feeds contestation before the federations.
- Office stewardship per VI.3, in the steward's terms: Workspace Administrator → Substrate; Secretary → Record; President → Covenant; Vice President → Governance; Treasurer → Education & Information. The presidential cabinet carries the covenant's research and development and the broadcast's research and development; the president never holds a verdict on any claim.
- Federations: one per layer, plus a volunteer federation for training, countersigning service, and education. Each elects individual, recallable executives.

---

## Schedule B — References

- Acemoglu, D., & Robinson, J. A. (2019). *The Narrow Corridor*. Penguin Press.
- Hirschman, A. O. (1970). *Exit, Voice, and Loyalty*. Harvard University Press.
- Laurie, B., Langley, A., & Kasper, E. (2013). *Certificate Transparency*. RFC 6962, IETF.
- Leveson, N. G. (2011). *Engineering a Safer World*. MIT Press.
- Ostrom, E. (1990). *Governing the Commons*. Cambridge University Press.
- Scott, J. C. (1998). *Seeing Like a State*. Yale University Press.
- Sen, A. (1981). *Poverty and Famines*. Oxford University Press.
- Stodder, J. (2009). "Complementary Credit Networks and Macroeconomic Stability." *Journal of Economic Behavior & Organization*.
- The full bibliography, the theoretical grounding, and the assessment of adjacent designs are carried by the companion commentary, [jfa-commentary.md](jfa-commentary.md).

---

*Network Theory Applied Research Institute, Inc. — 501(c)(3) — EIN 92-3047136 — info@ntari.org*

*This instrument is free documentation under the project's AGPL-3.0 commons; it is meant to be read, reimplemented, and contested.*
