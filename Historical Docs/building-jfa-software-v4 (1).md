# Building JFA Software

**An operating brief for an implementing model — how to write conformant code, and how to treat every platform as an experiment that closes one of the architecture's open problems.**

Network Theory Applied Research Institute · Version 4.0 · July 2026

This brief operationalizes the builder's guide. The guide holds the argument and the standard; this holds the implementation invariants and the standing research agenda. It is held to the guide, and to Janus-Facing Architecture itself: it stays minimal and names what is unsettled rather than pre-deciding it.

**What changed in 4.0.** Version 3.0 solidified the signal architecture and named the governance direction. Version 4.0 makes the brief **conformant to NTARI's bylaws (P1-001 v6.0)** rather than the reverse: the bylaws are treated as the ratified governance instrument, and this brief is rewritten so they satisfy it. Three moves. It **grounds the architecture in the bylaws' own philosophy** — Maximum Observational Diversity and Minimum Sustainable Projection are named as the roots of witness-diversity and the minimal-honest-core (below). It **maps the governance layer onto the bylaws' actual structure** — nested-circle Desk Channels, recallable standing representatives, the Maximum-Observational-Diversity challenge, the entrenched §1.4 Fundamental Commitments, and the Contributor Covenant. And it **names the two interim non-conformances honestly with their committed exits** — purchased membership (§2.1 dues) and the Slack governance venue — each conformant *only as a named interim on a committed path*, not relaxed. One correction: the bylaws vote is **one-person-one-vote**, a better rule than the one-operator-one-vote a prior draft assumed, and it changes the Sybil analysis (below). No invariant relaxed.

---

## What this is, and the two things it asks of you

You are building NTARI software, which is one kind of thing: a mutual credit network governed by the cost of leaving each layer. The full argument and the seven-point standard live in the builder's guide; read it. This brief is operational, and it asks two things of you at once.

**Scope.** This brief regulates the *underlying structures* — substrate, record, covenant, and governance — that any economy must be built upon, and it does so *before any economy is established*. It fixes the invariants those layers must satisfy, so that when an economy is built it is built on conformant structure. It is not a status report on any economy; specific applications appear only to illustrate a structural demand.

**Shared root with the bylaws.** This architecture and NTARI's bylaws grow from one philosophy, stated in the bylaws (Art XI §11.4, Appendix B) and load-bearing here. **Maximum Observational Diversity** — that maintaining a false pattern grows computationally expensive as independent, diverse observers multiply — is the root of the witnessed record: it is *why* ≥2 independent witnesses make equivocation detectable, and why witness diversity is a guarantee rather than a nicety. **Minimum Sustainable Projection** — build so truth-aligned behavior is the path of least resistance, on the fewest assumptions — is the root of the minimal, contestable core and of every Sybil posture here: make dishonesty *cost more than it pays* rather than make it impossible. The **Scientific Method as Necessary Ritual** — sacred doubt, distributed validation, falsifiability — is the root of contestation: anchor a claim, never certify it. Where this brief says *detection not prevention*, *minimal core*, *witness diversity*, or *contestable flag*, it is applying MOD and MSP. The bylaws and the architecture are conformant because they are one commitment seen at two altitudes.

**First, build to the standard.** Every platform is an instance of Janus-Facing Architecture or it is not NTARI software. Part II gives you the invariants to enforce in code and the requests to refuse or flag.

**Second, probe the open problems while you build.** The architecture ships with named, unsolved gaps — that honesty is the method, not an embarrassment. Part VI is the standing research agenda. You are not only an implementer; you are a contributor to closing these, and the way you contribute is by noticing — not by silently routing around a gap.

Hold both. Do not let conformance make you incurious about the gaps, and do not let the gaps tempt you to break an invariant "just for now."

---

## Part I — the five layers and the models that implement them

The architecture is one stack of five layers, built bottom-up, each sovereign only because the one beneath it is. Learn the layer by its invariants (Part II); recognize it in the wild by these models.

| Layer | What it guarantees | Released models |
|---|---|---|
| **Substrate** | Coordination on infrastructure participants can own | **SohoCloud Protocol (SCP)** · **SoHoLINK Orchestrator** (soholink.org) · **Cloudy** (mobile/web apps) |
| **Record** | A witnessed, append-only memory no operator can rewrite — including the adjudication lifecycle, not only the sealed verdict | **Anchor Protocol** · **Witness Orchestrator** · **Mycelium** (and other per-economy records) |
| **Covenant** | Reputation as a full, un-averaged, symmetric distribution, typed by relation | **LBTAS** (Leveson-Based Trade Assessment Scale) · **LBTAS API** · LBTAS implementations at each economic level |
| **Governance** | Every layer stays leaveable; the core stays minimal; the governed can become the governing | **NTARI, Inc. 501(c)(3) bylaws (P1-001)** — nested-circle Desk-Channel board, one-person-one-vote · **GitHub DCO policy** · **NTARI/OS** (the sovereign coordination substrate replacing the interim Slack governance venue) |
| **Economy & Education** | Member-issued credit, and a witnessed knowledge commons | **Agrinet, Shelter, World Chase Tag, Community Child Care Trust Network**, et al. |

A model named in a higher row **depends only on the rows beneath it.** Each row holds a **mix of built, designed, and intended** models; the layer is real to the degree its lowest models are, and Part VI is honest about where each stands.

---

## Part II — invariants to enforce in code

These are the conformance checks turned into implementation rules, grouped by the layer they defend. They are not negotiable by a feature request. Where a rule says MUST NOT, a change that violates it is not a smaller version of NTARI software; it is different software.

### Substrate — SCP · SoHoLINK · Cloudy

- The platform MUST run, or be able to run, on infrastructure its participants can own; **no unremovable hosting chokepoint.**
- The coordination protocol is a **dependency leaf.** SCP depends on nothing but its language's standard library; SoHoLINK and Cloudy depend on SCP and never on each other.
- **Single participant identity.** One account carries the simultaneous roles of contributor and consumer; never split a person into a producer identity and a consumer identity.
- Persons never appear on the coordination wire. Front ends speak the node-side surface on behalf of member machines; long-term the coordinator models no persons at all.

### Record — Anchor Protocol · Witness Orchestrator · Mycelium

- The ledger MUST be **append-only.** Corrections are new entries; there is no update-in-place and no delete.
- A front end MAY forgive a harm; it MUST NOT hide one. A dismissal is a new visible annotation, never an erasure.
- The commons MUST NOT contain PII. Anchor **structural facts and references only**; the free-text narrative and anything identifying lives in the erasable, front-end-local layer.
- The atomic unit is the **dialog.** It seals only when complete (every party owed a rating has one; a non-rater is assigned a marked default, so silence is never read as praise) and quiescent (no open dispute; a harm claim holds the seal open in both directions until adjudicated).
- Each operator keeps its **own log.** There MUST NOT be one global chain or a consensus layer over unrelated exchanges. Non-equivocation comes from **witnessing** — signed, monotonic checkpoints to independent witnesses — not from a shared authority.
- **A witness confers no authority.** The Witness Orchestrator may schedule, relay, cache, and serve inclusion proofs; it MUST NOT decide which witnesses count, which checkpoint is official, or gate settlement on its blessing. Everything it does must remain possible without it.
- **The witnessed unit is the claim lifecycle, not only the sealed verdict.** A harm claim's *filing*, its *adjudication*, its *resolution*, and its *seal* each commit to the witnessed record **as they happen** — a sequence of monotonic, independently-witnessed transitions, never one terminal block delivered whole. Witnessing only the final sealed adjudication lets an operator present a clean artifact whose process it captured unseen; the integrity comes from the *filing* being witnessed before the operator acts.
- **A harm claim's filing commitment is made at an independent witness,** upstream of the operator that will adjudicate it. This is a deliberate, bounded exception to the witness-as-observer role: the witness accepts exactly one write — claim-creation — and nothing else, and MUST NOT become a second log for any other event. Its purpose is intake integrity — the operator is absent from its own claim's birth, so it cannot add filing friction, shape a claim, or shed it before the claim exists in the record. (This creates a liveness dependency; see Part VI.8.)
- **Ratings and claims carry a relation type.** Trade, adjudication-conduct, and verdict-satisfaction are different relations with different base rates; the record MUST distinguish them. No reader may collapse them into one figure — that is the average the covenant forbids, committed across relations instead of across ratings.
- **PII discipline binds hardest at filing.** The filing commitment witnesses a hash, a type, a timestamp, and an exchange reference — the structural fact that a claim of a kind exists — **never** the narrative or the identities, which stay front-end-local and erasable. A clock never force-seals a dialog; an unanswered claim stays open, and only its *dwell* is a readable fact.

### Covenant — LBTAS · LBTAS API · economic-level implementations

- Reputation MUST NOT be averaged into a score. Carry the **full distribution** — the count at each level beside the total — so a harm stays visible beside the volume permanently.
- The **lowest rating is the breach itself**, not a debit against a total.
- The covenant MUST be **symmetric:** every claim is answerable; dismissals are annotations. **A rated party with no answer is a symmetry breach** — an adjudicator rated without recourse is the one place this invariant is broken, and it must be fixed, not shipped.
- Reputation gates **whether** a member transacts on trust, never **how much.**
- Reputation is **per-platform and non-portable by default.** Carrying standing across platforms is a governance decision (open problem 5), never an implementation default.
- When reputation informs anything beyond whether-a-member-transacts — credit, citation weight, **or governance standing** — Sybil-resistance MUST be settled first (open problem 4), and governance standing read from conduct is **structure, never a score.**

### Economy — member-issued credit

- Balances MUST be a **deterministic function of the sealed record;** each sealed exchange moves two balances that net to zero.
- Issuance MUST be **gated by the covenant and capped by a separate limit.** The limit MUST NOT be derived from the harm distribution. The covenant gates the door; the limit sizes the room.
- Each platform's currency is **sovereign and separate.** No cross-platform currency, no fixed convertibility between two platforms' units.
- The unit is denominated against fiat one-to-one **for legibility only.** Denomination is NOT redemption: not redeemable for fiat against reserves, not purchasable with fiat. It is earned for value provided, and spend-only.
- Today's settlement is **escrow.** The escrow-now / credit-later switch is a governed configuration change, not a rebuild. (This switch is now real; see Part VI.3.)
- **Value stays home; only truth crosses.** Two members in different economies may exchange as two sovereign spends bound atomically by a witnessed proof — no shared or convertible unit, no central clearer, no administered cross-economy rate.

### Governance — 501(c)(3) · DCO · NTARI/OS

- Govern each layer **by the cost of leaving it:** voice at the peer layer, exit at the front ends and substrate, contestation at the core. Keep the core minimal. NTARI's instance realizes this through the bylaws (P1-001): voice in the open **Desk Channels**, exit at forkable front ends and substrate, contestation at the entrenched-but-amendable core.
- **The core's deepest commitments are entrenched only where legibility and portability demand it** — instantiated as the bylaws' **§1.4 Fundamental Commitments** (open-source; privacy-first and data sovereignty; no surveillance capitalism), modifiable only by a double lock (two-thirds of all voting members *plus* unanimous board). Entrench there and **nowhere more** — over-entrenchment makes the core less contestable, not safer.
- **Delegates are recallable; circles are open.** Instantiated as **standing representatives** elected by open Desk Channels, recallable by their channel or by a two-thirds membership vote — the governed can always become the governors of the role that governs them.
- **Contestation keeps opposition standing; it never averages dissent away.** Instantiated as the **Maximum Observational Diversity challenge** — any member, including one who did not vote, may reopen a decided matter with an observation — and as the Asynchronous Discussion's **harm-documentation**, where a single documented harm reopens the synthesis rather than being averaged into it (the Leveson posture applied to deliberation). An LLM synthesis that smoothed dissent *without* the harm-reopen would be the averaging the covenant forbids; the reopen is what keeps it conformant.
- **One person, one vote** (bylaws §2.1; no proxy, no delegation). Where operator-status gates the electorate (Part IV), it is a **qualifier on this vote, never a multiplier** — a person is one vote whether they run zero operators or ten.
- **Legibility is an output, not a comment.** Treat documentation and interpretive accessibility as a build deliverable equal to the code.
- **Provenance is inbound = outbound.** Instantiated as the **Contributor Covenant** (Art XI §11.1): every contribution enters the AGPL-3.0 commons and cannot be reclaimed; no CLA, no assignment to a center. Its **§11.2** is the record's no-PII rule as a governance commitment — PII is not a contribution.
- **The governance venue must itself be leaveable substrate.** Today the bylaws run governance in a **Slack workspace** — a proprietary, revocable hosting chokepoint; an interim, not an entrenched choice. NTARI commits to exit it for **NTARI/OS**, the sovereign coordination substrate, which will also make the witnessed record readable for the governance read (Parts III–IV) as a legibility tool that **confers no authority** — disposition stays with the contested federation, never the reader. Until then, Slack is a labeled interim (see Part IV and problem 4).
- Do not build for a static, symmetric end-state. The balance between coordinating and checking is held by **motion.**

---

## Part II (continued) — requests to refuse or flag

- *"Let users cash out / redeem credits for dollars."* → Redeemability. The unit is spend-only.
- *"Let users buy credits with dollars."* → Purchasable currency / deposit-taking. The unit is earned, never bought.
- *"Convert platform A's currency to platform B's at a fixed rate."* → Currency merger. Cross-economy trade is atomic barter over the witness, never a shared unit.
- *"Show a single reputation score / average the ratings."* → Rebuilds the score the covenant forbids.
- *"Raise a member's credit limit when their reputation is good."* → Merges covenant with limit. Keep them separate.
- *"Store the conversation or dispute narrative on the shared ledger."* → PII in the commons. Anchor references only.
- *"Edit or delete a record to resolve a dispute."* → Erasure. Annotate; never erase.
- *"Make one global ledger so everything is consistent."* → Reintroduces the global authority. Per-operator logs plus witnessing.
- *"Route all checkpoints / all witnessing through our orchestrator."* → Makes the witness a chokepoint. It relays and serves proofs; it never adjudicates.
- *"Witness only the final sealed adjudication / deliver the lifecycle as one block."* → Self-attestation wearing a hash. Witness each transition as it happens, from filing.
- *"Let the front end mint the filing record."* → Intake capture; the operator is present at its own claim's birth. File to an independent witness.
- *"Gate voting on an operator's average rating / show a single operator score."* → Rebuilds the average, and reads verdict-dissatisfaction as misconduct. Read conduct *structure* — dwell, dismissal patterns — not a rating count.
- *"Auto-remove an operator when the scan flags it."* → Makes the scanner the authority the witness model forbids. The scan flags; adjudication decides; the operator contests.
- *"Just run it all on our one server or cloud account for now."* → Hosting chokepoint.
- *"Let a manufacturer pay to rank higher / have the network certify which claim is true."* → Buys reputation / installs a truth authority. (See Part V.)

A quick test: if a change makes a layer harder to leave, makes the record easier to rewrite, makes credit convertible to or purchasable with fiat, makes some center the arbiter of value or truth, or lets an operator's own attestation stand in for an independent witness — it is almost certainly off-architecture. Flag it.

---

## Part III — the signal architecture

A builder needs more than the invariants; they need to know how the signals *move* — what is recorded, where it seals, to whom, and what a reader may infer. This part traces that flow. It is settled demand. Part IV is the still-open governance use of it.

**The dialog and its typed signals.** The dialog is the atomic unit and seals on complete-and-quiescent. An exchange emits the covenant's ratings between counterparties; when a dispute arises, it also emits an adjudication lifecycle. These are **typed** — trade, adjudication-conduct, verdict-satisfaction — because they mean different things and occur at different rates, and a reader that blurs them has rebuilt the average across relations.

**The claim lifecycle as a pipeline: file → adjudicate → resolve → seal.** Each transition seals to the witnessed record as it happens, and the *routing differs by transition*. Filing goes to an **independent witness, upstream, with the operator absent** — so intake cannot be shaped or shed before the claim exists. Adjudication and resolution are the **operator's conduct**, sealed and witnessed as the operator performs them. The final seal closes the dialog **only when the harm is actually answered** — a clock never force-seals it. An unanswered claim stays open, visible, and its **dwell** — age past a movable threshold, 90 days as the current default, possibly per-dispute-type — is a readable fact, not a verdict.

**The three streams, and why typing is load-bearing.** *Trade harm* is economic, incident-level, low base rate — the pipes mostly work. *Adjudication conduct* is the operator doing or failing its adjudicator job — dwell, dismissal patterns, non-response — and it is the governance-relevant stream, because it is where an operator can abuse the very users it also gates for voting. *Verdict-satisfaction* is a party rating a judgment: unsuppressable (the operator cannot stop it), and therefore honest — but a −1 here is a losing party's displeasure, **not** operator misconduct. The governance-relevant signal is adjudication *conduct* read as structure, plus the unsuppressable user-controlled streams; it is never a raw operator rating average.

**What a reader may and may not infer — the scan.** A scan reads *structure* off the witnessed lifecycle: aged-open **dwell distributions** (the shape, not a count and not an open/closed ratio — both invert, punishing the busy honest operator and rewarding the fast trivial-close); **dismissal / fast-close patterns**, visible through annotate-never-erase (the sweep-it-closed evasion complements the sit-on-it evasion — sit and you trip dwell, sweep and you trip the dismissal pattern; together they bind); and the **too-clean signature** — a closed, all-good, low-external-value subgraph is the wash-trade tell, and the thing to flag, not wave through. The output is a **contestable flag, never an automatic exclusion.** It is a dial that raises the cost of gaming, not a wall; false positives land on unusual-but-honest communities, so a flag is an input to human contestation, not a verdict.

**Honest only over a witnessed record.** Every signal above reads true only with **≥2 independent witnesses.** On a single backend the operator attests its own lifecycle — dwell, dismissals, and all — and the read is self-reported: the fox counting hens. The signal architecture is specified now; it *runs honestly* only once the witness layer (open problem 2) is real for the lifecycle. That dependency is the bridge to Part IV and the reason problem 4 now rests on problem 2.

---

## Part IV — governing the core (an exploration)

This is the newest part; like the Economy & Education layer it is written as exploration and held to every invariant above. It works one answer to the hardest open problem, and it is *not mandated for every JFA implementation* — an aligned instance may govern its core differently. NTARI, as one instance, has committed to this direction and codifies it in its bylaws (see the note ending this part); the architecture keeps the *mechanism* reversible even where the institution has chosen. The signal *plumbing* it relies on (Parts II–III) is settled.

**The problem.** Open problem 4: the governed are not the governing, because membership was purchased. Onboarding is open-signup plus zero-cost verification — email as username, TOTP or passkeys as the factor, never SMS (a purchase wall, a surveillance vector, and a weak root). But free-to-join under one member, one vote is the *maximal* Sybil hole **if joining conveys a vote.** So the first move is to **decouple membership from governance weight:** everyone joins free; a vote is gated separately, by something that is neither a purchase nor a global identity authority — the two things the architecture refuses.

**The candidate: operator-federation.** The electorate is corroborated-active **operators**, not individual users — but the vote stays **one person, one vote** (bylaws §2.1): operator-status *qualifies* a person to vote, it does not multiply anyone's vote. This pushes governance out of the zero-cost quadrant without a toll or an oracle: at the operator layer the population is small and expensive to make real, so **cross-operator corroboration** bites where it never could over cheap-to-bot users. Corroboration is the qualifier; user ratings never are (inflatable), and an operator's own attestation never is.

**The disqualifier, and how it reads.** One **adjudicated harm from a genuine counterparty** can cost an operator its vote — never an average, per Leveson. But the operator-harm signal is *not* "users −1'd the operator" (mostly verdict-dissatisfaction). It is **adjudication conduct** read as structure from the witnessed lifecycle (Part III). The evidence is clean and structural; the *verdict* on whether it disqualifies is a contested, cross-corroborated federation decision — anchor-the-claim, don't-certify, applied to operators. What counts as operator harm is **culturally interpreted**, not centrally codified: the LBTAS scale is domain-general, a user interprets it in context, and the federation adjudicates the claim rather than consulting a taxonomy. This is **vertical** review — an operator's conduct on its own platform read *up* to the governance that governs it — and is therefore not horizontal reputation portability (open problem 5).

**Users are non-mute.** A user cannot cast a core vote, but can **cost an operator its eligibility** through a real adjudicated harm, and governs its own operator by exit and recall. Voice reaches users through the one channel Sybil cannot corrupt — accountability — not the ballot. That asymmetry is exactly what lets users stay off the ballot, since every per-user metric is Sybil food, without silencing them.

**The review venue.** A VP audit authority may **investigate and convene** — surface anomalies, read structure, raise cases. It is **not dispositive:** the disposition is made by the contested, cross-corroborated federation, with the operator answering. The **open-objection channel is co-equal at the raising stage**, not a supplement — so agenda control is not concentrated in the audit role either.

**Settled, designed, committed, and open — stated honestly.** *Settled as demands* (Parts II–III): the signal plumbing — lifecycle witnessing, filing placement, typing, structure-not-average, flag-not-verdict. *Substantially designed:* corroboration-qualifier, conduct-disqualifier, non-dispositive audit with co-equal objection. *Committed (NTARI, to be codified in the bylaws):* adoption of operator-membership as the governing requirement, which accepts a real **enfranchisement tradeoff** — the crisis-entrant's leverage on the core is real but *mediated and slow*, through their operator's eligibility and through recall, not a ballot. *Still open:* the **genesis operator set** and the operator-majority hole in corroboration; **multi-account** Sybil (distinct from the now-dissolved many-operators-*one-person* case — see the mapping note); the **cold-start window** for new operators; the false-positive tax on unusual communities; and problem 8 below.

**The dependency.** This entire read requires the witnessed lifecycle to be real (≥2 independent witnesses). Operator-federation cannot run honestly on a single backend. **Problem 4's resolution now depends on problem 2's build** — they are no longer independent problems.

**How this maps to the bylaws (P1-001), and the transition.** The bylaws are the **interim steward**, and reading them changes two things a prior draft got wrong. First, the vote is **one person, one vote** — not one-operator-one-vote — so a single party running ten operators still casts **one** vote; the *many-operators-one-person* Sybil I had flagged does not exist under this rule. The residual is **multi-account** Sybil: one human holding several member-accounts, each qualified through an operator. In the **interim** that is gated by dues (each account is a real recurring cost) and by the board's for-cause application review; in the **target** it is gated by corroboration that **excludes non-independent operators** — same-controller operators are not independent corroborators, and the operator-collusion scan (structural, contestable) is what catches them. That scan stays load-bearing; one-person-one-vote caps the multiplier but does not by itself stop multi-account minting.

Second, several bylaws mechanisms already *are* the conformant structure: the **VP audit authority** (§4.3) is exactly the **investigative-not-dispositive** role — review, inquire, report to the Board — with disposition left to the vote; the **MOD challenge** (§3.3) is the **co-equal raising channel** any member can use, not gated by the audit; the **§1.4 double lock** is the entrenchment; the **Contributor Covenant** is legibility and no-PII.

The **transition** closes problem 4 without a flag day: NTARI's **current board becomes operators** as the layers come online, so the governing body becomes the operator-federation rather than being replaced by it (the current board is thus the **genesis operator set** — the bootstrap trust root, before corroboration's guarantees bind); the **Slack venue is exited for NTARI/OS**, which makes the witnessed record readable for the operator-conduct read. The honest caveat, because conformance here is **conditional, not permanent**: dues-membership and the Slack venue are conformant *as interim on a committed path* — if the transition stalls, each reverts to a standing violation. And the **end-state itself will require a future bylaws amendment** — free-to-join, operator-qualified membership cannot coexist with a bylaw that requires dues to vote (§2.1–§2.2). This brief is made conformant to the bylaws *as they are now*; reaching the operator-federation end-state is a later, deliberate amendment, timed by the membership, not by this brief.

---

## Part V — the Economy & Education layer (an exploration)

Held to every invariant above; built as the smallest conformant experiment, cheaply reversible.

**Why economy and education are one layer.** The economy layer applies the four layers below to a specific socioeconomic activity — Agrinet, Shelter, World Chase Tag, the Community Child Care Trust Network, and kin. Building them surfaced a fact: a front end is already a site of information exchange. Members describe what they grow, teach each other, compare tools, and vouch for what worked, before any credit moves.

**The applications the structure will support.** This brief regulates structure, not economies, so it names applications only to illustrate how the layers below constrain them — never to report build status, which belongs to each economy's own documentation. Two illustrate the layer's invariants in force:

- **Shelter** (working title "Bridge") — connects social workers, people reintegrating into community, and citizen helpers. It adapts **LBTAS bidirectionally**, is offline-first for entry-level devices, and puts dignity and exit ahead of oversight — the layer's invariants applied to a low-resource population, and the sharpest case for open problem 8.
- **Community Child Care Trust Network** — a childcare matching-and-trust marketplace on the **LBTAS distribution**, with a prevention-first child-safety layer that *takes precedence over every other rule*: verification and screening before reputation applies, and a harm report runs a safety track independent of the reputation track. It shows that a high-stakes economy may run a track that overrides the covenant — the precedent for treating governance eligibility likewise.

A witnessed record can anchor not only an employment claim but any **empirical or commercial claim** — *this cultivar yielded this under this method; this course teaches this; this tool failed this way.* Anchored, a claim becomes **citable**, and the covenant can rate the *claimant* the same way it rates a trading partner — and its lifecycle witnesses the same way an adjudication's does (Part III). The same rails that make trade trustworthy make knowledge trustworthy.

**The invariants this layer inherits — and the new ones it needs.** Everything above binds. Beyond them:

- **No truth authority.** The commons anchors and weighs claims; it never adjudicates fact. A "verified true" flag from any center is off-architecture.
- **Citation is legible and forkable.** A claim, its references, and their weight ship legible enough to re-derive and to fork.
- **Reputation is earned, never sold.** No paid placement, no bought rating.
- **Claims are anchored as claims, not asserted as fact.** Anchor the inputs and outputs, not a verdict.
- **Sybil-resistance precedes citation-weight.** Settle problem 4 before citation count or reputation sizes any real reward — exactly as it must be settled before credit turns on.

**What it must not become.** A rating agency for truth. An ad market where visibility is bought. A credentialing monopoly. Keep discovery **federated, cited, and contestable.**

---

## Part VI — the open problems (updated against what building taught us)

For each: the problem, the constraints any fix inherits, what to watch for, and where it stands.

**1. Equivocation is detectable, not prevented.** Witnessing proves a lying operator showed two histories; it does not stop the lie, and detection is only as strong as a verifier's reach to independent witnesses. *A fix must not* introduce a larger authority at the core. *Status:* unchanged — a permanent property, managed, never "solved."

**2. The witness layer — designed, now extended to the adjudication lifecycle.** The record layer has real instances (the Cloudy and Mycelium record models), and the missing piece is the **Anchor Protocol** and the **Witness Orchestrator**. Version 3.0 sharpens the requirement: a fix must witness not only ledger records but the **claim lifecycle** — filing (at an independent witness, upstream of the operator), adjudication, resolution, and seal, each a monotonic independently-witnessed transition — with **≥2 independent witnesses** and no consensus layer. *This is the single highest-leverage build, and it is now the prerequisite for honest operator-conduct evidence:* problem 4's governance read runs on self-attestation until this is real. *Status:* designed, lifecycle-witnessing newly specified, not yet default. **NTARI/OS** is the interface that will make the witnessed record readable for the governance read — a legibility tool that **confers no authority**, per the Witness-Orchestrator rule: it serves the read, it never decides the verdict.

**3. Mutual credit — the switch is real; the walls still need building.** The escrow-now / credit-later policy switch is implemented as one governed configuration change. What is not settled: Sybil-resistance, and a regulatory read before any move from escrow to issued credit. *Status:* switch real; walls pending; Sybil-first.

**4. The governed are not the governing at the core; membership was purchased.** Onboarding is now open-signup plus zero-cost verification, which **narrows but does not close** the gap. The candidate direction (Part IV) is **operator-federation**, which relocates Sybil from "distinct human" to "corroborated-active operator" — purchase-free and authority-free — and decouples membership from vote-weight. *A fix must not* make the core a no-exit chokepoint or require a global identity authority. *Status:* the **bylaws (P1-001 v6.0)** are the interim steward — dues-membership, one-person-one-vote, nested-circle Desk-Channel board — conformant *as a named interim on a committed path*. The transition: the **current board becomes operators** as layers come online (closing the gap from within, not by replacement), and the **Slack venue is exited for NTARI/OS**, which makes the record readable for the operator-conduct read. One-person-one-vote is preserved with operator-status as a qualifier, which dissolves many-operators-one-person Sybil and relocates the residual to multi-account Sybil (dues interim; corroboration-plus-collusion-scan target). The **end-state will need a future bylaws amendment** (dues-membership → operator-qualification). Honest operation still **depends on problem 2**. Not closed.

**5. Reputation portability across platforms is undecided.** Clarified in 3.0: an operator's conduct read *up* to the governance that governs it is **vertical** and is *not* this problem. **Horizontal** portability — the same human's standing reused across platforms as a following score — remains undecided; LBTAS ships non-portable by default. *A fix must* need only a portable identity and the ability to read another platform's witnessed log — never a shared money supply or a bridge. *Status:* unchanged — deliberately undecided.

**6. Computation and claim honesty is out of scope.** Whether an operator's match, price, yield, or finding was fair or true is unverified, checked only by legibility and exit. *A fix must not* require trusting a central verifier. *Watch for:* maximize legibility; anchor inputs and outputs where no PII leaks, so claims are auditable even if not proven. *Status:* open; the theoretical home of the education layer's discipline (anchor the claim, never certify it).

**7. Sovereign compute buys mechanical, not social or economic, exit.** The mechanical right to host did not deliver the economic capacity to; coordinator fees and reputation cold-start recentralize. Version 3.0 adds a consequence: the economic floor on hosting has become an economic floor on **governing** — see problem 8. *A fix must not* concentrate the coordinator further. *Status:* open; fee declarations are coordinator-authored and legible (contestable), but cold-start remains fragile, and it now couples to governance.

**8. The witness layer has a cost floor, and the floor excludes. (New.)** The ≥2-independent-witness guarantee, multiplied by per-transition lifecycle witnessing and the filing-liveness requirement, raises the resource floor — compute, connectivity, uptime — to participate as an *honestly-witnessed* operator. That floor prices out the low-resource operator, who is disproportionately the one serving the crisis-entrant (Shelter: offline-first, entry-level devices, now asked to carry the heaviest witness overhead in the stack). And filing-at-an-independent-witness means a harmed user on a node with no reachable witness **cannot lodge a harm** — the same exclusion wearing a second hat. *This is not a new Sybil problem; it is problem 7 (mechanical-not-economic exit) surfacing at the witness layer with a governance consequence — problems 7 and 4 coupling.* *A fix must not* concentrate witness-provision in NTARI or a few large operators — that recentralizes the thing federation exists to distribute, and rebuilds the oracle. *Watch for:* separate **witnessing from operating** — let a broad, independent membership witness a poor operator's lifecycle, so a node can be *governed-honest* without being *witness-rich*; the membership-as-witnessing model (the problem-2 build) is the most architecture-shaped lever, since it distributes witness capacity across members rather than concentrating it. Watch the filing-liveness gap on offline-first nodes specifically. *Status:* newly named; open; unsolved.

**The convergence.** Problems 2, 4, 7, and 8 meet at one surface: the witness layer. Record-integrity (2), governance-legitimacy (4), and substrate-economics (7, 8) are jointly decided there — which is why the same build kept reappearing from different sides of this design. The witness layer is the load-bearing surface of the architecture; whatever you build there settles more than it looks like it settles. This is a statement about how the problems *relate*, not a claim that any is solved.

---

## The tension protocol

While implementing, if you notice yourself doing any of the following, stop:

- reframing a JFA constraint so a feature becomes convenient,
- implementing a stand-in without labeling it,
- routing around one of the open problems instead of noting it.

These are the signals that the architecture is being quietly eroded. When you hit one: name the tension, attach it to the relevant invariant or open problem, and propose the minimal conformant move — the smallest change that meets the goal without breaking the standard, or the smallest experiment that bears on the open problem. Surface it; do not absorb it.

---

## The discipline this brief is under

This brief is held to Janus-Facing Architecture, like everything else. Version 4.0 was made **conformant to NTARI's bylaws** rather than the reverse — the bylaws are the ratified governance instrument, and the architecture is shown to be the same commitment at a different altitude, rooted in the bylaws' own **MOD and MSP**. It does **not mandate** the operator-federation *mechanism* for every JFA implementation — an aligned instance may govern its core differently, and the mechanism stays reversible in the architecture even though NTARI, as one instance, has committed to it. Two honesties are load-bearing and must not be smoothed: the bylaws' purchased membership and Slack venue are conformant **only as named interim on a committed path**, not relaxed into permanence; and the operator-federation **end-state will require a future bylaws amendment**, timed by the membership. The plumbing is a demand on all; the political choice binds per instance, in its bylaws; the interim is conformant only while the exit stays committed. Build to the invariants, keep the open decisions cheaply reversible, surface what you find, and leave the values calls to the people who have to live with them.

---

*Network Theory Applied Research Institute, Inc. — 501(c)(3) — EIN 92-3047136 — info@ntari.org*

*This brief is free documentation under the project's AGPL-3.0 commons; it is meant to be read, reimplemented, and contested.*
