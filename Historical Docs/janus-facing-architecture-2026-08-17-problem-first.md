# Janus-Facing Architecture

**The standard: the coordination problems, the five layers that answer them, the substack within each layer, the invariants a conformant system must satisfy, and the questions that remain open.**

Network Theory Applied Research Institute

This document names *roles and mechanisms* — coordination protocol, coordinator, front end, ledger, orchestrator, countersigner, assessment scale, governance venue — and holds every implementation to them. Each layer's section closes by naming the substack the steward operates in those roles; that subsection describes the instance, never the norm. Any implementation, present or future, binds to a role defined here; where an implementation and this document disagree, either the implementation is fixed or this document is amended in the open.

**How to read this.** Sections 1 through 6 each open with the specific coordination problem the layer answers — problems named by Daron Acemoglu and James A. Robinson, James C. Scott, and Elinor Ostrom — and with the reasons the rejected alternatives would weaken the architecture; each closes with what the layer settles and what it leaves to section 1.4. Where a rule says MUST, MUST NOT, or MAY, the keyword carries the force RFC 2119 gives it. Every invariant carries a stable identifier, `SUB-1` through `LEG-2`, printed beside its statement; the executable conformance suite that ships beside this document holds the registry and verifies the pairing, and a conformant repository cites those identifiers in its own test suite — until it does, its conformance is self-attested. This document is the constitution, not the wire specification: it names roles and the requirements they satisfy; schemas, formats, and state machines live with the protocol artifacts that bind to these roles.

**One rule, one form, one pattern.** The whole architecture compresses to one rule: **govern every layer by the cost of leaving it** — exit where leaving is cheap, voice where it is dear, standing contestation where it is impossible. What is built under the rule is one kind of thing: a **mutual credit network** — an economy in which members extend value to one another against a covenant not to harm, on a record no one can quietly rewrite, on hardware no one can revoke, with no central issuer of money and no central judge of trust. And every layer carries the same **substack**: a *protocol* (the layer's wire language and rules), an *orchestrator* (the running service that executes them), and a *user interface* (the surface members touch). Picture the stack as a **gravity well**: shallow at the surface, where users drift freely between interfaces; bottomless at the core, the specification you contest but cannot exit.

---

## Glossary — the terms of art

*Definitions orient; the normative text below governs. Every term names a role or a mechanism, never a product.*

**The whole stack**

- **Janus-facing** — the permanent two-way posture: one face coordinates, the other checks the coordination — two functions carried and exchanged by one community, never two populations.
- **The one rule** — govern every layer by the cost of leaving it: exit where leaving is cheap, voice where it is dear, standing contestation where it is impossible.
- **Layer** — one of the five strata of the stack: Substrate, Record, Covenant, Governance, Education & Information. Each is sovereign only because the one beneath it is.
- **Substack** — the three roles every layer carries: a protocol, an orchestrator, and a user interface.
- **Orchestrator** — the running service that executes a layer's protocol; it federates automatically with its peers and reports to its federation's board in the governance frontend.
- **Federation** — the standing open circle of the members operating a given layer, electing recallable executives answerable for that layer.
- **Gravity well** — the stack pictured as a well: shallow at the surface, where users drift freely between interfaces; bottomless at the core, the spec you contest but cannot exit.
- **Mutual credit network** — the one thing built here: an economy in which members extend value to one another against a covenant not to harm, on a record no one can rewrite, on hardware no one can revoke, with no central issuer of money and no central judge of trust.
- **Maximum Observational Diversity (MOD)** — the root of the witnessed record: maintaining a false pattern grows expensive as independent, diverse observers multiply.
- **Minimum Sustainable Projection (MSP)** — the root of the minimal core: build on the fewest assumptions, so truth-aligned behavior is the path of least resistance and dishonesty costs more than it pays.
- **Sybil** — one actor posing as many — accounts, identities, or operators — to multiply an influence the system meant to hand out once.
- **Named interim** — a non-conformant arrangement (a proprietary venue, a purchase-gated vote) tolerated only while its exit stays committed and progressing; a stalled interim is a standing violation.
- **Tension protocol** — the builder's stop-rule: when a constraint is being reframed, a stand-in is unlabeled, or an open problem is being routed around, name the tension, attach it to the invariant or problem, and propose the minimal conformant move.
- **Open-questions document** — the living per-project deliverable naming what remains unresolved about the project's future; equal in standing to the code, and nonconformant the moment it goes stale.

**Substrate**

- **Substrate** — the bottom layer: coordination on infrastructure participants can own.
- **Coordination protocol** — the shared wire language of the network, and the specification no one can cheaply leave — kept minimal, legible, and permanently contested for exactly that reason. As software, a dependency leaf.
- **Dependency leaf** — software that depends on nothing but its language's standard library, so it can be reimplemented and audited whole.
- **Coordinator** — the node-side orchestration role that runs the protocol on a community's infrastructure and declares its fees legibly.
- **Front end** — the member-facing application; it speaks the node-side surface on behalf of member machines, and it is leaveable by design.
- **Hosting chokepoint** — any single host, account, or vendor whose revocation could stop the network; forbidden as an end-state.
- **Presentation sovereignty** — styling ships as user-editable data separate from application logic, and every participant holds the right to restyle their own render, self-view only.

**Record**

- **Record** — the second layer: a witnessed, append-only memory of what happened, including the full claim lifecycle.
- **Dialog** — the atomic unit of the record; it seals only when complete (every rating owed exists) and quiescent (no open dispute).
- **Seal** — the closing of a dialog into the permanent record; never forced by a clock.
- **Append-only** — corrections are new entries; there is no update-in-place and no delete.
- **Anchor commitment** — a structural fact or reference committed to the commons; never a narrative, never PII.
- **Checkpoint** — an operator-signed, monotonic commitment to the current state of its log.
- **Countersigner** — an independent party that countersigns checkpoints so that showing two histories becomes provable; a countersigner confers no authority.
- **Equivocation** — an operator showing different histories to different audiences; two validly-signed, mutually-inconsistent checkpoints are the portable proof.
- **Claim lifecycle** — file → adjudicate → resolve → seal, each transition witnessed as it happens; filing lands at a countersigning point independent of the adjudicating operator.
- **Dwell** — how long a claim has sat open past a movable threshold; a readable fact, never a verdict.
- **Stand-in label** — the mandatory marker on any deployment running with fewer than two independent countersigners; a single-countersigner system may not present itself as federated.

**Covenant**

- **Covenant** — the third layer: trust as a standing promise not to harm, not a score; a member is in good standing or in breach.
- **Assessment scale** — the harm-surfacing rating scale (Leveson-derived); the lowest rating is the breach itself.
- **Full distribution** — reputation carried as the count at each rating level beside the total; never averaged into one figure.
- **Relation type** — the typing of ratings and claims (trade, adjudication-conduct, verdict-satisfaction); collapsing them rebuilds the forbidden average across relations.
- **Symmetry** — every claim is answerable and every dismissal is an annotation; a rated party with no recourse is a breach of the covenant's own rules.
- **Limit** — the separate instrument that caps how large a commitment an honest member may take on; never derived from the harm distribution.

**Education & Information**

- **Mutual credit** — money created at the moment of exchange: one balance down, one up, the sum always zero, backed by covenant and capacity rather than reserves.
- **Escrow phase** — the pre-credit settlement mode: collateralized in advance, no balance ever negative, no trust extended. The escrow-to-credit switch is a governed configuration change, not a rebuild.
- **Earned, never bought; non-redeemable** — the credit unit is issued only for value provided and can never be purchased or cashed out; at once the regulatory firewall and the adverse-selection filter.
- **Denominated, not backed** — the fiat peg is a unit of account for legibility, never a promise of redemption.
- **Sovereign currency** — each platform issues and clears in its own unit, with no cross-platform convertibility. Value stays home; only truth crosses.
- **Knowledge-claim anchoring** — the record extended to empirical and commercial claims, which become citable without any center certifying them true.

**Governance**

- **Minimal entrenched core** — the few commitments locked behind a double lock (a supermajority of members plus board unanimity): open source, privacy-first and data sovereignty, no surveillance economics. Entrench there and nowhere more.
- **Steward** — the named, internally-accountable body that holds the one layer with no exit; disciplined by entrenchment, the real possibility of a fork, and standing opposition.
- **Layer-aligned stewardship** — five standing offices, one per layer, each a recallable delegate answerable for that layer's conformance and legibility; answerability, never authority.
- **Open circles; recallable delegates** — deliberative channels any member may join, electing representatives whom their channel, or a supermajority of the membership, can recall.
- **Standing contestation** — ratification is never final: any member may reopen a decided matter with an observation, and a single documented harm reopens a synthesis rather than being averaged into it.
- **One-person-one-vote qualifier** — where a status gates the electorate, it qualifies a person's single vote and never multiplies it.
- **Operator-federation** — the governing electorate: corroborated-active operators, one vote per person.
- **Cross-operator corroboration** — operator recognition by other, independent operators; operators under common control corroborate nothing.
- **Genesis operator set** — the founding steward's standing representatives, serving as the bootstrap trust root before corroboration binds.
- **Governance venue** — where deliberation and voting happen; it must itself be leaveable substrate, and any proprietary venue is a named interim.
- **Legibility ladder** — the seven mechanized rungs that bind plain language to running code, from decision receipts at the point of use to reproducible, witnessed builds.

---

## 1. The problems demanding this architecture

### 1.1 The present day

The failure this architecture answers is not scarcity. The world wasted just over a billion tonnes of food in 2022 — a fifth of everything available to consumers, with another 13 percent lost upstream of retail ([UNEP, *Food Waste Index Report 2024*](https://www.unep.org/resources/publication/food-waste-index-report-2024)) — in the same years that more than 730 million people went hungry (FAO, *The State of Food Security and Nutrition in the World*, 2024). The United States holds roughly fifteen million vacant housing units while counting some 770,000 people homeless on a single January night (HUD, *2024 Annual Homeless Assessment Report*). Amartya Sen showed four decades ago that modern famines arrive without any decline in food availability: people starve not because the goods are missing but because their entitlement to them fails. The surplus exists; what fails is coordination. Markets move goods toward money rather than toward need, and the administered alternative rebuilds the unanswerable center that decides for everyone.

The second failure is one of speed. Platforms adjust their algorithms hundreds of times a year; the regulation meant to check them takes years to enact (NTARI, [*Addressing Democratic Information Velocity*](https://www.ntari.org/post/ntari-whitepaper-addressing-democratic-information-velocity)). This is the Red Queen race of Acemoglu and Robinson run at mismatched speeds: when power evolves faster than accountability, the corridor between them closes from the powerful side. Citizens accumulate certainty at network speed with no legitimate pathway to act on it; executives hold the capacity to act without the democratic warrant to; the deliberative middle collapses from both directions at once.

The third failure is material. The infrastructure democracies deliberate on was built as broadcast plumbing: NTARI's survey of twenty-five parliamentary digital systems found the overwhelming majority failing every one of Surowiecki's four conditions for collective intelligence — diversity, independence, decentralization, effective aggregation (NTARI, [*The Material Culture of Democratic Deliberation*](https://www.ntari.org/post/the-material-culture-of-democratic-deliberation)). Centola's network research shows that clustered, "inefficient" topologies outperform centralized ones on exactly the complex problems governance consists of — and parliamentary platforms ship the maximally efficient broadcast topology instead, precisely the wrong architecture for the job.

What the present demands, then, is coordination infrastructure that moves real goods and services against real needs, at the speed the network age runs, without concentrating the power to decide who may have what. That is the work this document specifies.

### 1.2 The history

**Acemoglu and Robinson name the balance problem.** In *The Narrow Corridor* (2019), the state is Janus-faced: it shows the people a favorable face in one moment, then turns to show a monstrous one, and liberty survives only in the corridor where society's capacity to check the state grows as fast as the state's capacity to act — the Red Queen race, both sides running to stay in place. Their earlier work names the stakes: institutions are inclusive or extractive, and extractive ones concentrate the power to decide who prospers. Acemoglu and Robinson kept the state–society hierarchy and asked how to hold it in balance. This architecture collapses that hierarchy back into the mass of the people: with the internet as infrastructure, the communication patterns of a whole population can be made fast and rich enough that the state-over-people hierarchy is no longer needed. The architecture is therefore **Janus-facing** — one face coordinates, the other checks the coordination, two *functions* carried and exchanged continuously by one community, never two populations. The balance is held by motion, a thermostat rather than a throne.

**Scott names the legibility problem.** In *Seeing Like a State* (1998), the high-modernist center simplifies society to administer it — cadastral maps, standardized names, planned cities — and the simplification runs one way: the governed become legible to the center while the center stays opaque to the governed, and the local, practical knowledge Scott calls *mētis* is destroyed in the flattening. Every catastrophic scheme in his catalog paired that one-way legibility with a state strong enough to act on it. This architecture inverts the direction: here it is the *infrastructure* that is made legible to the governed — the rules readable, the record inspectable, the builds reproducible — while persons stay off the wire and narratives stay out of the commons. Legibility of the system to the people, never of the people to a center.

**Ostrom names the commons problem.** *Governing the Commons* (1990) refuted the claim that shared resources must be handed to Leviathan or carved into private property: communities govern commons durably when the institution satisfies her design principles — boundaries defined by the community, rules made by those they affect, monitors accountable to the monitored, graduated sanctions, cheap and accessible conflict resolution, the recognized right to organize, and nested layers of governance. Her cases were irrigation districts and fisheries, small enough for faces to be known; the open question she left is scale. Each layer of this stack is one of her principles made digital — and the numbered sections below say which.

**The monetary history supplies the form.** Mutual credit is proven, not speculative: Switzerland's WIR Bank has cleared complementary credit among businesses since 1934, and Sardex has done the same across Sardinia for over a decade, both counter-cyclically — liquidity appearing exactly when outside money is scarce (Stodder 2009). Graeber's *Debt* locates the ledger before the coin: money begins as recorded mutual obligation, and the bank is a later concentration of three functions — the scorer (who is trustworthy?), the issuer (whose credit is good?), and the ledger (what happened?). Concentrate any one of them and the bank returns. The whole architecture exists to keep all three distributed: the scorer contestable (Covenant), the ledger legible (Record), the issuance member-held (E&I), and exit cheap (Substrate) — with Governance holding the balance. The platform-cooperative literature (Scholz and Schneider 2016) supplies the final warning: cooperative ownership of an extractive architecture reproduces extraction, because ownership is downstream of architecture. An interface that shows each class of participant only what its role requires is enforcing hierarchy beneath whatever the equity says.

**The architecture's own roots.** Three commitments run beneath every layer. **Maximum Observational Diversity (MOD)**: maintaining a false pattern grows computationally expensive as independent, diverse observers multiply — the root of countersigning, and of why observer diversity is a requirement rather than a nicety. **Minimum Sustainable Projection (MSP)**: build on the fewest assumptions, so truth-aligned behavior is the path of least resistance and dishonesty costs more than it pays — the root of the minimal, contestable core. And the scientific method as necessary ritual — sacred doubt, distributed validation, falsifiability — the root of contestation: anchor a claim, never certify it.

### 1.3 The proposed solutions

Four contemporary projects answer parts of the same demand. Each solves one coordination function and leaves the others to the existing institutions — and the unsolved function is where the center grows back. Naming what each gets right is as load-bearing as naming what each concedes.

**The Network State ([thenetworkstate.com](https://thenetworkstate.com)).** Srinivasan's startup societies take exit seriously — cloud-first communities that accumulate capital and negotiate recognition. But exit is the *only* mechanism: membership is purchased, the founder is the unanswerable center, and there is no voice or standing contestation anywhere in the design. In Acemoglu and Robinson's terms it builds a despotic Leviathan in miniature and calls the exit door liberty; in Ostrom's terms it violates the principle that rules are made by those they bind — here they are bought. What survives into this architecture: exit is real and must be provisioned, not merely permitted. What this architecture refuses: making exit do the work of voice and contestation, which prices the poor out of governance entirely.

**The Collective Intelligence Project ([cip.org](https://cip.org)).** Alignment Assemblies demonstrate that structured deliberation at scale produces synthesis broadcast cannot. But the outputs are advisory, the scope is technology governance, and the participants own none of the infrastructure they deliberate on — voice without a record, a franchise, or an economy. What survives: deliberative synthesis as a first-class mechanism. What this architecture adds: a witnessed record that makes the deliberation's history unrewritable, and a governance layer in which the deliberators hold the actual franchise.

**Consul Democracy ([consuldemocracy.org](https://consuldemocracy.org)).** The most widely deployed open-source participation platform — proposals, debates, participatory budgeting, adopted by cities worldwide, copyleft-licensed. But it is hosted by the very institutions it addresses, its proposals flow upward to a center that disposes at its own discretion, and it carries no economic layer: participation rides on the host's continued goodwill. What survives: municipal-scale participation is achievable with free software. What this architecture adds: the venue itself as leaveable substrate, so the deliberation does not live at the pleasure of its subject.

**Pol.is ([pol.is](https://pol.is)).** Real-time opinion clustering — the vTaiwan process showed it surfacing consensus statements across thousands of participants that no poll or forum could find. But it is a listening instrument: aggregation without deliberative synthesis, participation without membership or permanence, and its output informs a center rather than binding one. What survives: aggregation across diverse, independent participants is MOD in practice. What this architecture adds: anchoring, so that what the listening finds becomes a citable, contestable part of a permanent commons rather than a report on a desk.

The common shape of the concession: each project trusts an existing institution — a founder, a lab, a city hall — to carry the functions it does not build. This architecture's claim is that the functions must ship as one stack, because whichever one is left out becomes the seat of the returning center.

### 1.4 The open questions

The architecture keeps its unsolved problems numbered, public, and load-bearing; several have been solved or substantially narrowed since first posed, and each entry below says so plainly. For each: the problem, the constraints any fix inherits, and where it stands. A question discovered locally in any project is promoted here rather than kept local, and every project ships its own living open-questions document (`GOV-9`, section 2).

**1. Equivocation is detectable, not prevented.** Countersigning proves a lying operator showed two histories; it does not stop the lie, and detection is only as strong as a verifier's reach to independent countersigners. *A fix must not* introduce a larger authority at the core. *Status:* a permanent property, managed, never "solved" — the detection machinery (operator-signed monotonic checkpoints, consistency proofs, the checkpoint pair as portable fork evidence) is specified and built; the property itself is unchanged.

**2. The countersigner layer — solved in design, open in deployment.** The witnessed-record core is specified and implemented: per-operator hash-chained logs, signed monotonic checkpoints, retrospective countersignatures with structural independence verification, inclusion and consistency proofs, and a structural stand-in label whenever fewer than two independent countersigners have signed. Federation is structurally cheap: an independent countersigner joins by appending a signature, no protocol change. What remains open is deployment in fact — two or more independent, long-lived countersigners, durable countersigner state, and lifecycle witnessing of the claim pipeline end to end. *Status:* this remains the single highest-leverage build; problem 4's governance read runs on labeled stand-ins until federation is real.

**3. Mutual credit — the switch is governed; the read is not done.** The escrow-now / credit-later switch is a single governed configuration change, and the walls (earned-never-bought, covenant-gate/limit separation, board approval and membership notice before issuance) are codified in the steward's instrument. What is not settled: the regulatory read itself, and Sybil-resistance first. *Status:* narrowed; the read and Sybil-first still gate the switch.

**4. The governed are not the governing at the core.** Free joining under one-member-one-vote is the maximal Sybil hole if joining conveys a vote; purchased membership closes the hole by selling the franchise. The resolution: decouple membership from governance weight, and qualify the vote by **operator-federation** — the electorate is corroborated-active operators, one person one vote, operator status a qualifier never a multiplier; recognition matures from a genesis operator set to cross-operator corroboration, excluding operators under common control; a purchase-based qualifier survives only as a named interim with a committed sunset. *Status:* politically solved — the mechanism is designed and adopted in the steward's governance instrument; evidentially open — honest conduct evidence depends on problem 2, and multi-account Sybil, the cold-start window for new operators, and the false-positive tax on unusual communities remain.

**5. Reputation portability across platforms is undecided.** An operator's conduct read *up* to the governance that governs it is vertical and settled; horizontal portability — the same human's standing reused across platforms as a following score — remains deliberately undecided, and the covenant ships non-portable by default. *A fix must* need only a portable identity and the ability to read another platform's witnessed log — never a shared money supply or a bridge. *Status:* deliberately undecided.

**6. Computation and claim honesty is out of scope.** Whether an operator's match, price, yield, or finding was fair or true is unverified, checked only by legibility and exit. *A fix must not* require trusting a central verifier. *Status:* open in general; the discipline holds — anchor inputs and outputs where no PII leaks, so claims are auditable even if never certified.

**7. Sovereign compute buys mechanical, not social or economic, exit.** The mechanical right to host does not deliver the economic capacity to; coordinator fees and reputation cold-start recentralize, the way deliverability recentralized email despite its open protocol. *A fix must not* concentrate the coordinator further. *Status:* the mechanical half is demonstrated — the coordination protocol is published, versioned, and consumed by independent implementations; the economic half is open and couples to problem 8.

**8. The countersigner layer has a cost floor, and the floor excludes.** Two-or-more independent countersigners, multiplied by per-transition lifecycle witnessing and the filing-liveness requirement, raises the resource floor to participate as an honestly-witnessed operator — and prices out the low-resource operator serving the crisis-entrant, who is asked to carry the heaviest overhead in the stack. A harmed user on a node with no reachable countersigning point cannot lodge a harm: the same exclusion wearing a second hat. *A fix must not* concentrate countersigning in the steward or a few large operators. *Watch for:* separating countersigning from operating — a broad, independent membership countersigning a poor operator's lifecycle, so a node can be governed-honest without being resource-rich. *Status:* open; federation-by-appending-a-signature is exactly the seam membership-as-countersigning needs, and the volunteer federation (section 2) is where the lever sits.

**The convergence.** Problems 2, 4, 7, and 8 meet at one surface: the countersigner layer. Record-integrity (2), governance-legitimacy (4), and substrate-economics (7, 8) are jointly decided there — whatever is built at that surface settles more than it looks like it settles. This is a statement about how the problems relate, not a claim that any is closed.

---

## 2. Governance

**The problem this layer answers.** Michels' iron law: every organization drifts toward oligarchy as its administrators entrench. Freeman's corollary: abolishing structure does not abolish power — a network governed by "the community" in the abstract is governed by whoever shows up, capture in open-source clothing. Acemoglu and Robinson state what must be true instead: liberty holds only while the governed can become the governing as fast as the governing act — the Red Queen run inside one community. And Ostrom's third principle names the test any rule must pass: the people a rule binds participate in making and changing it. The alternatives all fail one of these named problems: a self-perpetuating board is Michels' drift by design; share- or token-weighted voting multiplies votes by wealth and hands the core to whoever buys it; an unnamed steward is Freeman's structurelessness; a global identity authority rebuilds the Leviathan the stack exists to retire. So this layer is built the only remaining way — a named steward, filled from the bottom, recallable throughout, entrenched only where entrenchment protects contestability itself. The one rule does the assigning — govern every layer by the cost of leaving it — and the gravity well pictures the result: exit at the shallow surface where interfaces are freely leaveable, voice where leaving is dear, standing contestation at the bottomless core no one can exit.

### 2.1 Membership by operation

Membership in the steward is earned one way: **operating any part of the stack** — a coordinator on owned hardware, an orchestrator at any layer, a front end, an economy. Operation is Ostrom's boundary principle made digital: the community's edge is defined by contribution to the commons, not by purchase — a franchise that is bought selects for money rather than stake, and a franchise that is free to any account is the maximal Sybil hole. Operation threads between them: it is free of charge and expensive to fake.

- The governing electorate is the **operator-federation**: corroborated-active operators, one vote per person. Operator status **qualifies** a person's single vote and never multiplies it — a person operating ten platforms holds exactly one vote (`GOV-7` below).
- Recognition is by **cross-operator corroboration** — operators recognized by other, independent operators; operators under common control corroborate nothing. Corroboration replaces both the toll and the identity oracle: at the operator layer the population is small and expensive to make real, so corroboration bites where it never could over cheap-to-create accounts.
- The franchise is held under a conduct standard — no gaming (manufactured or manipulated exchange, reputation, or corroboration signals), no tampering (rewriting, equivocating, obstructing the witnessed record), no harmful environments (adjudicated harm to a platform's own users, including obstruction of claim filing, abusive delay, patterned dismissal). One adjudicated harm from a genuine counterparty can cost the franchise; no volume of good conduct absolves it, and no finding is ever derived from an average. Evidence is conduct read as **structure** from the witnessed lifecycle — dwell distributions, dismissal patterns, collusion signatures — never a rating count; an analytic flag is an input to contestation, never a finding.
- Users who operate nothing are **non-mute**: they cannot cast a core vote, but a real adjudicated harm can cost an operator its eligibility, and they govern their own operator by exit and recall. Voice reaches them through the one channel Sybil cannot corrupt — accountability — not the ballot.
- Bootstrap: the founding steward's standing representatives constitute the **genesis operator set**, the trust root that precedes corroboration; the governing body becomes the operator-federation rather than being replaced by it. Any purchase-based qualifier retained during the bootstrap is a named interim with a committed sunset — never an end-state.

### 2.2 The board: formation, operation, and the division of responsibility

The steward's structure is nested circles — Ostrom's eighth principle, nested enterprises, applied to its own governance. Two kinds of circle carry it:

**Office circles.** Each office of the steward is an open deliberative channel any member may join. Each elects a **standing representative** who serves simultaneously as the corresponding officer, as a director of the stewarding body, and as the steward of one layer — and who acts on channel votes, executes what the office requires, and is recallable by the channel or by a supermajority of the membership at any time. Recall is the Red Queen made procedure: the governed replace the governing at the speed of an election, not a crisis.

**Layer federations.** Each layer of the stack has a standing **federation** — the open circle of the members operating that layer — plus a volunteer federation for training, countersigning service, and education across the commons. Federation deliberation is open to members of every class; binding federation votes require the operator qualification in good standing; each federation elects individual, recallable executives to represent it in meeting its responsibilities. Losing the operator franchise ends federation membership without expelling the person from the commons — Ostrom's graduated sanctions, applied to governance itself.

The invariants of the layer, enforceable in any instrument that claims conformance:

- Govern each layer **by the cost of leaving it:** voice at the peer layer, exit at the interfaces and substrate, contestation at the core. Keep the core minimal — it guarantees only the portabilities that keep every layer above it leaveable, so capturing it pays little. `GOV-1`
- **Name the steward.** The one layer with no exit is stewarded by a named, internally-accountable body, its board filled from the bottom with recallable delegates of open circles, disciplined by the three things that can discipline a no-exit layer: the entrenchment of its deepest commitments, the expensive-but-real fork of its implementation, and the obligation to keep internal opposition standing. `GOV-2`
- **Stewardship mirrors the stack** — layer-aligned stewardship. `GOV-3` Five standing offices align one-to-one with the five layers, so every layer has exactly one named, recallable officer answerable for its conformance and legibility: the **workspace administration** stewards the Substrate; the **secretariat** stewards the Record; the **presidency** stewards the Covenant; the **vice-presidency** stewards Governance, including the investigative-but-never-dispositive audit authority; the **treasury** stewards Education & Information. One-to-one is the point: an unassigned layer decays with no one answerable, and a doubled office concentrates exactly what the stack distributes. Stewardship is answerability, not authority — the secretariat no more decides which checkpoint is official than a countersigner does, the presidency never holds a verdict on a claim, and the treasury tends issuance policy as governed, witnessed policy changes, never per-member discretion.
- **The core's deepest commitments are entrenched only where legibility and portability demand it** — open source; privacy-first and data sovereignty; no surveillance economics — behind a double lock (a supermajority of all voting members *plus* unanimity of the stewarding board). This is the minimal entrenched core: entrench there and **nowhere more** — over-entrenchment makes the core less contestable, not safer. `GOV-4`
- **Delegates are recallable; circles are open.** Standing representatives are elected by open deliberative channels and recallable by their channel or by a supermajority of the membership — the governed can always become the governors of the role that governs them. `GOV-5`
- **Contestation keeps opposition standing; it never averages dissent away.** Any member, including one who did not vote, may reopen a decided matter with an observation; and in deliberative synthesis, a single documented harm reopens the synthesis rather than being averaged into it — the covenant's no-averaging posture applied to deliberation. Standing contestation is what keeps ratification from ever being final. `GOV-6`
- **One person, one vote** — no proxy, no delegation. Where a status gates the electorate, it is a **qualifier on this vote, never a multiplier** — a person is one vote whether they hold the qualifying status once or ten times over. `GOV-7`
- **Legibility is an output, not a comment.** Documentation and interpretive accessibility are a build deliverable equal to the code; the mechanisms are the legibility ladder, below. `GOV-8`
- **Every project ships a living open-questions document** — a build deliverable equal to its code, naming what is unresolved about the project's future: questions, constraints, and status, never commitments dressed as questions. Living means reviewed and re-shipped with each release — a stale open-questions document is conformance drift, and a project performing the absence of its gaps has failed the method, whatever its code does. An entry leaves only by resolution or by an explicit values call made by the people who live with the outcome; a question that binds architecturally is promoted to section 1.4, and the two cite each other in both directions. `GOV-9`
- **Provenance is inbound = outbound: every contribution enters the copyleft commons** and cannot be reclaimed; no contributor license agreement, no assignment to a center; PII is not a contribution. The covenant never suspends; its enforcement mechanism may — but only as a named interim with a committed reinstatement, recorded visibly, and the enforcement gap is permanent for the commits made inside it. `GOV-10`
- **The governance venue must itself be leaveable substrate.** A proprietary, revocable hosted venue is a hosting chokepoint at the core; it is conformant *only* as a named interim with a committed exit to sovereign coordination substrate — and a stalled interim is a standing violation, reported as such. `GOV-11`
- Do not build for a static, symmetric end-state. The balance between coordinating and checking is held by **motion.** `GOV-12`
- **Every orchestrator federates automatically.** A layer's orchestrator MUST discover its peers and communicate with the applicable federation's message board in the governance frontend without manual attachment, so the operating state of every layer is continuously legible to the federation answerable for it. An orchestrator that must be hand-wired into governance is a legibility gap wearing a default. `GOV-13`

#### The legibility ladder

The legibility invariant says *must*; this subsection says *how*. "The governed can read the logic that governs them" decomposes into two capacities: every member can directly read the rules that govern them, and anyone independent can cheaply verify that the running code embodies those rules. The mechanisms are a ladder, and the binding principle is that each rung MUST be mechanically bound to the rung below it — a plain-language layer that merely mirrors the code is a second source of truth, born drifting, and unverified explanation is not legibility. `LEG-1`

1. **Decisions explain themselves at the point of use.** Every governance-relevant output — a match, a fee, a rating display, a sealed dialog, a flag — ships with a receipt: which rule fired, on which inputs, linked to the rule's plain statement.
2. **Rules live as data, not code.** The engine — rarely changing, expert-audited — executes policy expressed declaratively: fee schedules, rating scales, seal conditions, dwell thresholds, credit limits. Policy renders as plain tables and sentences, diffable by anyone; this rung is where most lay inspectability actually lives.
3. **Policy versions commit to the witnessed record.** Rule changes are treated exactly like exchanges: append-only, witnessed, each with a plain-language changelog entry — so "what rule was in force when my dialog sealed?" has a witnessed answer.
4. **The spec is the constitution, written in prose.** Normative plain language first, wire format second — literate enough that a motivated lay reader can follow the argument of the protocol, not only its bytes.
5. **Conformance tests bind the prose to the code.** The load-bearing rung: every normative sentence maps to an executable check, so that prose which can fail the build is trustworthy prose.
6. **The trusted core stays small and boring.** A dependency-leaf protocol of a few thousand literate lines is inspectable by a motivated lay person with an afternoon; nothing of half a million lines is inspectable by anyone.
7. **Builds are reproducible; release hashes are witnessed.** The code someone reads must provably be the code that runs: reproducible builds, signed releases, interfaces displaying the hash of what they run, release hashes committed to the witnessed record.

The guarantee never comes from every member personally auditing the code — it comes from making verification cheap and distributed enough that many independent observers can, which makes maintaining a false pattern expensive: MOD applied to legibility. Machine reading aids — a member interrogating the repository through a model — are worth designing for, but an aid MUST remain a reading aid, never an oracle; a "verified true" explanation from any model is the truth authority the architecture forbids, and the aid's claims stay checkable against the spec and the conformance suite. `LEG-2`

### 2.3 The NTARI substack

- **Protocol — the 501(c)(3) instrument.** The governance layer's wire format is the stewarding nonprofit's governing instrument itself: bylaws amended in the open by the membership, one person one vote, the three fundamental commitments double-locked, operator membership adopted as the committed basis of the franchise, and the architecture document explicitly denied authority over any vote — the instrument, not this standard, is where political choices bind. It is the protocol in the exact sense the other layers use the word: the minimal, legible, permanently contestable rule-set every other component binds to.
- **Orchestrator — the steward's self-hosted JFA stack.** The steward runs the full stack on its own sovereign substrate as the governance venue: continuous asynchronous deliberation, channel votes, the append-only register of governing documents, and the capture and auditing reads across every layer. The venue is thereby held to the same substrate invariants it governs (`GOV-11`).
- **Interface — NTARI/OS.** The member-facing governance surface: each federation's message board lives here, every layer's orchestrator reports into it automatically (`GOV-13`), and the auditing toolset renders the witnessed record readable for the governance read. The reader confers no authority — a flag raised here feeds contestation before the federations, and disposition stays with the contested, cross-corroborated vote, never with the tool.

**Settled by this layer:** the steward is named, recallable from the bottom, and entrenched only at the three commitments; the governed become the governing by operating the stack. **Still open:** problem 4's evidentiary half — until the countersigner layer runs federated (problem 2), operator-conduct evidence is self-attested and must say so — and multi-account Sybil in the interim (section 1.4).

---

## 3. The Education & Information layer (E&I)

**The problem this layer answers.** Democratic information velocity: deliberation that moves slower than the power it checks is decoration, and the present gap is measured in orders of magnitude (section 1.1). Scott adds the deeper diagnosis: the knowledge coordination actually needs — what a cultivar yields in this soil, what a course teaches, which tool fails and how — is *mētis*, local and practical, and every system that centralizes information destroys precisely what it collects. And the standing temptation is the one Acemoglu and Robinson warn about: install a center that certifies what is true, and you have built the extractive institution of knowledge — a rating agency for reality. The weakening alternatives are all live in the wild: discovery sold to advertisers prices truth by the bidder; credential monopolies gate knowing behind purchase; a platform-owned marketplace is a company town. This layer answers all three at once: an economy that moves value at exchange speed, and a knowledge commons that anchors claims without ever certifying them.

### 3.1 The economy: mutual credit

A mutual credit network creates money at the moment of exchange — one balance down, one up, the sum always zero — backed not by reserves but by members' covenant and their capacity to deliver real goods and work. Mutual credit is derived from the record, not bolted onto it:

- Balances MUST be a **deterministic function of the sealed record;** each sealed exchange moves two balances that net to zero. `ECO-1`
- Issuance MUST be **gated by the covenant and capped by a separate limit.** The limit MUST NOT be derived from the harm distribution: the covenant gates the door; the limit sizes the room. Let the two merge — let good standing buy a higher ceiling — and the harm distribution quietly becomes a credit score, and the bank returns through the back door. `ECO-2`
- Each platform's currency is **sovereign and separate.** No cross-platform currency, no fixed convertibility between two platforms' units. A fixed rate between economies of unequal productivity does not equalize them; it removes the valve that lets the weaker one adjust — the Eurozone periphery and the interwar gold standard are the warning, not the model. `ECO-3`
- The unit is denominated against fiat one-to-one for legibility only. **Denomination is NOT redemption:** not redeemable for fiat against reserves, not purchasable with fiat — earned for value provided, and spend-only. This single wall is at once the regulatory firewall (a unit that is earned, never bought, and never cashable is barter-credit, not money transmission) and the adverse-selection filter (with no fiat yield to extract, extractors self-select out). `ECO-4`
- Settlement begins as escrow — collateralized in advance, no balance ever negative, no trust extended — and the escrow-to-credit switch is a **governed configuration change**, never a rebuild: board approval, membership notice, and a completed regulatory review before any issuance. `ECO-5`
- **Value stays home; only truth crosses.** Two members in different economies may exchange as two sovereign spends bound atomically by a witnessed proof — no shared or convertible unit, no central clearer, no administered cross-economy rate. `ECO-6`

Credit switches on in phases because a credit network with few members is worthless: first the escrow marketplace builds volume and displays integrity; then the earned, non-redeemable unit enters on the one value proposition fiat cannot match in-network — counter-cyclical, interest-free liquidity, exactly when outside money is scarce; then the internal economy thickens and fiat retreats to the perimeter. Migration is pulled by the value proposition, never pushed by an interface; and who the first members are is each instance's own values call.

### 3.2 The knowledge commons

The same rails that make trade trustworthy make knowledge trustworthy. A witnessed record can anchor not only an exchange claim but any empirical or commercial claim — *this cultivar yielded this under this method; this course teaches this; this tool failed this way.* Anchored, a claim becomes **citable**, its author ratable under the covenant like any counterparty, its lifecycle witnessed like any adjudication — knowledge-claim anchoring, with no center certifying anything true.

The disciplines this extension inherits and adds: **no truth authority** — the commons anchors and weighs claims, never adjudicates fact, and a "verified true" flag from any center is off-architecture; **citation is legible and forkable** — a claim, its references, and their weight ship legible enough to re-derive; **reputation is earned, never sold** — no paid placement, no bought rating; and **Sybil-resistance precedes citation-weight** — problem 4 is settled before citation count or reputation sizes any real reward, exactly as it must be before credit turns on. What this layer must not become: a rating agency for truth, an ad market where visibility is bought, a credentialing monopoly. Keep discovery federated, cited, and contestable.

### 3.3 The NTARI substack

- **The operating entity.** The steward's E&I layer is operated by **Fruitful Management LLC**, wholly owned by and operated for the 501(c)(3): the commercial, member-facing surface that presents the JFA stack to the world at market speed while the nonprofit holds the covenant, the record, and the franchise. The division is deliberate — the layer that must move at the market's pace is exactly the layer that must never hold the no-exit core.
- **The standards registers.** The layer's protocol role is filled by the steward's published standards — protocol standards, orchestrator standards, and frontend standards for every layer of the stack — which are what make market entry cheap: the LLC collaborates with whoever enters the market using the same software, because interoperability is specified in the open rather than negotiated bilaterally.
- **The interface.** The E&I frontend is the stack's public face: the marketplace, the educational surfaces, and the origination point for adjudication — a member's harm claim is raised here and routed to the record layer's orchestrator (section 5.3). The treasury stewards the layer's conformance: mutual-credit compliance and nonprofit compliance, reported in the open.

**Settled by this layer:** coordination at network speed without a truth authority — counter-cyclical credit and a citable commons on the same rails. **Still open:** the regulatory read and Sybil-first gate the credit switch (problem 3), and citation-weight waits on problem 4 (section 1.4).

---

## 4. The Covenant layer

**The problem this layer answers.** Every mutual credit network contains a scorer — the answer to *who is trustworthy?* — and the scorer is where the bank rebuilds first. Concentrate it and you have recreated the extractive institution Acemoglu and Robinson describe: an authority that decides who may participate in the economy and answers to no one. Ostrom's fifth and sixth principles name what works instead: graduated sanctions assessed by the community, and conflict-resolution mechanisms that are cheap, fast, and local. The weakening alternatives are the industry defaults: the averaged star-rating dissolves a harm into a comfortable 4.7 the way no safety engineer would tolerate — two crashes in seventy-three flights grounds the fleet, and no quantity of good landings dissolves them; the credit score merges *is this person honest* with *how much can they carry* until reputation becomes collateral and the bank returns; the central moderator is an unanswerable judge. So trust here is a **covenant** — a standing promise not to harm — binary where it counts: a member is in good standing or in breach, and the lowest rating *is* the breach.

### 4.1 The covenant, not a score

- Reputation MUST NOT be averaged into a score. Carry the **full distribution** — the count at each level beside the total — so a harm stays visible beside the volume permanently. `COV-1`
- The **lowest rating is the breach itself**, not a debit against a total. `COV-2`
- The covenant MUST be **symmetric:** every claim is answerable; dismissals are annotations. A rated party with no answer is a symmetry breach — an adjudicator rated without recourse is the one known place this invariant is broken, and it must be fixed, not shipped. `COV-3`
- Reputation gates **whether** a member transacts on trust, never **how much.** The limit — how large a commitment an honest member may take on — is a separate instrument belonging to the economy, because the covenant secures honesty, not capacity: "I will not harm you" is not "I can deliver what I promised." `COV-4`
- Reputation is **per-platform and non-portable by default.** Carrying standing across platforms is a governance decision (problem 5), never an implementation default. `COV-5`
- When reputation informs anything beyond whether-a-member-transacts — credit, citation weight, or governance standing — Sybil-resistance MUST be settled first (problem 4), and governance standing read from conduct is **structure, never a score.** `COV-6`

Ratings and claims carry a **relation type** — trade, adjudication-conduct, verdict-satisfaction — because the three are different relations with different base rates, and collapsing them rebuilds the forbidden average across relations (the record enforces the typing; section 5).

### 4.2 The NTARI substack

- **Protocol — LBTAS.** The covenant definition: the Leveson-derived assessment scale, shipped as versioned, diffable policy data (legibility rung 2), so the scale that judges conduct is itself readable, contestable, and witnessed on every change.
- **Orchestrator — the LBTAS API.** Serves assessments and receives ratings and claims, typing each by relation and routing the claim lifecycle to the record layer as it happens; it computes distributions, never averages.
- **Interface — Covenant Broadcast.** Publishes standings as full distributions beside their totals — the covenant's public face, and the surface other layers' interfaces embed when they render trust.

The **presidency** stewards this layer: the presidential cabinet carries the covenant's research and development and the broadcast's research and development — evolving the assessment scale and its public dissemination as governed, witnessed policy changes — while the president never personally holds a verdict on any claim. The steward of the trust system is answerable for its integrity and structurally barred from wielding it: that separation is the layer's own medicine applied to its keeper.

**Settled by this layer:** trust without a central scorer — harm permanently visible, every claim answerable, capacity walled off from character. **Still open:** adjudicator symmetry until the recourse path ships (`COV-3`), and horizontal portability, deliberately undecided (problem 5, section 1.4).

---

## 5. The Record layer

**The problem this layer answers.** Scott's cadastral map, pointed the other way: the state's ledger made the governed legible to the center while remaining opaque to them — the record was the instrument of the very power it described. Any coordination system needs a memory of what happened; the question is who can rewrite it. A record the operator can quietly edit is Acemoglu and Robinson's unanswerable center in its most compact form — and MOD states the countermeasure as physics: maintaining a false history grows computationally expensive as independent, diverse observers multiply. The weakening alternatives each fail a named test: one global chain rebuilds the shared authority and couples every community's exchanges to a consensus none of them needs; operator self-attestation is the fox counting the hens; storing narratives in a shared ledger makes the commons a PII archive no one can ever erase; clock-forced closure lets an operator wait out its accusers. The design philosophy here is *detection, not prevention*: tampering is not made impossible; it is made self-evident, attributable, and portable.

### 5.1 The witnessed record

The construction is the certificate-transparency model, not consensus: each operator keeps its own append-only log and publishes signed, monotonic checkpoints to independent countersigners. An operator that shows two different histories thereby produces two validly-signed, mutually-inconsistent checkpoints — a self-evident, attributable, portable proof that it lied. A deployment running with fewer than two independent countersigners carries a **stand-in label**; it may not present itself as federated.

- The ledger MUST be **append-only.** Corrections are new entries; there is no update-in-place and no delete. `REC-1`
- An interface MAY forgive a harm; it MUST NOT hide one. A dismissal is a new visible annotation, never an erasure. `REC-2`
- The commons MUST NOT contain PII. Anchor commitments carry **structural facts and references only**; the free-text narrative and anything identifying lives in the erasable, interface-local layer. `REC-3`
- The atomic unit is the **dialog.** It seals only when complete (every party owed a rating has one; a non-rater is assigned a marked default, so silence is never read as praise) and quiescent (no open dispute; a harm claim holds the seal open in both directions until adjudicated). `REC-4`
- Each operator keeps its **own log.** There MUST NOT be one global chain or a consensus layer over unrelated exchanges. Non-equivocation comes from **witnessing** — signed, monotonic checkpoints to independent countersigners — not from a shared authority. `REC-5`
- **A countersigner confers no authority.** The record orchestrator may schedule, relay, cache, and serve inclusion proofs; it MUST NOT decide which countersigners count, which checkpoint is official, or gate settlement on its blessing. Everything it does must remain possible without it. `REC-6`
- **The witnessed unit is the claim lifecycle, not only the sealed verdict.** A harm claim's *filing*, its *adjudication*, its *resolution*, and its *seal* each commit to the witnessed record **as they happen** — a sequence of monotonic, independently-witnessed transitions, never one terminal block delivered whole. Witnessing only the final sealed adjudication lets an operator present a clean artifact whose process it captured unseen. `REC-7`
- **A harm claim's filing commitment is made at an independent countersigner,** upstream of the operator that will adjudicate it — a deliberate, bounded exception to the countersigner-as-observer role: the countersigning point accepts exactly one write — claim-creation — and nothing else, and MUST NOT become a second log for any other event. The operator is absent from its own claim's birth, so it cannot add filing friction, shape a claim, or shed it before the claim exists in the record. (This creates a liveness dependency; see problem 8.) `REC-8`
- **Ratings and claims carry a relation type.** Trade, adjudication-conduct, and verdict-satisfaction are different relations with different base rates; the record MUST distinguish them, and no reader may collapse them into one figure. `REC-9`
- **PII discipline binds hardest at filing:** the filing commitment witnesses a hash, a type, a timestamp, and an exchange reference — never the narrative or the identities — and **a clock never force-seals a dialog:** an unanswered claim stays open, and only its *dwell* is a readable fact. `REC-10`

### 5.2 The signals a reader may trust

The lifecycle emits three typed streams, and the typing is load-bearing. *Trade harm* is economic, incident-level, low base rate. *Adjudication conduct* is the operator doing or failing its adjudicator job — dwell, dismissal patterns, non-response — the governance-relevant stream, because it is where an operator can abuse the very users it also serves. *Verdict-satisfaction* is a party rating a judgment — unsuppressable, and therefore honest, but a lowest rating here is a losing party's displeasure, not operator misconduct. A scan reads *structure* off the witnessed lifecycle: dwell distributions (the shape, never a count or an open/closed ratio — both invert, punishing the busy honest operator); dismissal and fast-close patterns (visible because the record annotates and never erases); and the too-clean signature (a closed, all-good, low-external-value subgraph is the wash-trade tell). The output is a **contestable flag, never an automatic exclusion** — false positives land on unusual-but-honest communities, so a flag is an input to human contestation, not a verdict. And every one of these signals reads true only over two or more independent countersigners; on a single backend the operator attests its own lifecycle, and the read must be labeled self-attested.

### 5.3 The NTARI substack

- **Protocol — Anchor.** The record's wire language: anchor commitments, checkpoints, inclusion and consistency proofs, and the lifecycle transition format — a dependency leaf, reimplementable whole.
- **Orchestrator — Witness.** Runs the adjudication lifecycle and nothing more: it receives adjudication calls originating from the E&I layer's frontend, commits each transition to the witnessed record as it happens, relays checkpoints to independent countersigners, and serves proofs. Its bounds are `REC-6` and `REC-8` exactly — it decides nothing, gates nothing, and a claim's filing commitment lands at an instance independent of the adjudicating operator, a routing the automatic federation duty (`GOV-13`) makes routine rather than heroic.
- **Interface — none of its own.** The record layer is headless by design: its member-facing surface is the E&I frontend where adjudication calls originate. A second, record-owned surface would be a second place to shape intake — the exact capture `REC-8` exists to prevent.

**Settled by this layer:** equivocation is detectable, attributable, and portable; adjudication is born witnessed, not reported after the fact. **Still open:** live countersigner federation (problem 2) and the cost floor it carries (problem 8, section 1.4).

---

## 6. The Substrate

**The problem this layer answers.** Software has to run on someone's hardware, and whoever owns the iron owns the network: an open, forkable protocol whose only practical home is a hyperscaler or one operator's servers is openness as decoration. This is Scott's problem at the physical layer — infrastructure as the instrument of whoever holds the center — and Ostrom's seventh principle names the cure: the right of a community to organize its own institutions without external permission, which for digital coordination means compute no outside party can revoke. Acemoglu and Robinson supply the warning about the alternative: hosting that can be revoked is the despotic face held in reserve, however favorable the face currently showing. The weakening alternatives are the convenient ones — deploy on one cloud account (a chokepoint wearing a contract), build on a heavy dependency tree (a core no one can audit whole), model persons on the wire (surveillance by schema). Be honest about what the substrate buys: sovereign compute buys *mechanical* exit, not social or economic exit — the chokepoint relocates to coordinator fees and reputation cold-start (problem 7) — and because compute is forkable, this is emphatically *not* the layer no one can leave; that layer is the spec, far above it.

### 6.1 Sovereign coordination

- The platform MUST run, or be able to run, on infrastructure its participants can own; **no unremovable hosting chokepoint.** `SUB-1`
- The coordination protocol is a **dependency leaf.** It depends on nothing but its language's standard library; the coordinator and the interfaces depend on the protocol and never on each other. `SUB-2`
- **Single participant identity.** One account carries the simultaneous roles of contributor and consumer; never split a person into a producer identity and a consumer identity. `SUB-3`
- **Persons never appear on the coordination wire.** Interfaces speak the node-side surface on behalf of member machines; long-term the coordinator models no persons at all. `SUB-4`

The coordinator declares its fees legibly — contestable, coordinator-authored, never hidden in the match.

### 6.2 Presentation sovereignty

The cheapest exit in the stack is the render itself, and it gets the discipline of pure exit: styling ships as user-editable data separate from application logic, and every participant holds the right to restyle their own render — self-view only, nothing entering the commons or any other participant's view. If hierarchy is enforced at the level of the screen (the metacommunication problem: an interface that shows each role only what it needs is telling participants who they are), the counter is that the governed can rewrite their own screen. Five requirements, invariant-grade, enforced at import and paste:

- **Scripts never; markup sandboxed.** Pasted themes carrying executable content are the standing self-XSS attack; no theme executes. `SUB-5`
- **No remote fetches from user styles.** CSS alone phones home — `url()`, `@import`, `@font-face` — and a circulated theme becomes a beacon; strip or block remote references at import. `SUB-6`
- **Reset-to-default lives outside the styleable surface.** The undo cannot be occludable by the thing it undoes. `SUB-7`
- **Styles are plain, exportable artifacts** — a CSS or HTML file the user can read, carry, and reapply, never an opaque blob. `SUB-8`
- **Shipped or hosted themes inherit the carve-out.** A user hiding covenant surfaces from themselves is sovereignty; an interface shipping or hosting a theme that does so is the system hiding harm with extra steps. `SUB-9`

The default theme carries the WCAG 2.2 AA floor and the editor itself meets it; a participant's own overrides are their own.

### 6.3 The NTARI substack

- **Protocol — Sohocloud.** The coordination wire language: a dependency leaf, published and versioned, already consumed by independent implementations — which is what makes the mechanical exit of problem 7 demonstrated rather than promised.
- **Orchestrator — SoHoLINK.** Node-side coordination on member-owned hardware — small-office, home-office scale by design, because the substrate's promise is only as real as the smallest machine that can keep it. It declares its fees legibly and reports to the substrate federation's board automatically (`GOV-13`).
- **Interface — Cloudy Market.** The member-facing front end: leaveable by design, restyleable per presentation sovereignty, and speaking the node-side surface so that persons never touch the wire.

**Settled by this layer:** mechanical exit is real — the protocol runs on hardware no one can revoke, and independent reimplementation is demonstrated. **Still open:** the economic half of exit (problem 7) and the countersigner cost floor it couples to (problem 8, section 1.4).

---

## 7. The standard

Gathered, the layer disciplines are the cornerstone. A system is conformant to Janus-Facing Architecture only if all seven hold; a system that fails one is not a smaller version of this architecture — it is different software wearing its vocabulary.

1. **Mutual credit, not banking.** It is, or governs, a member-issued mutual credit economy, gated by covenant and capped by a separate limit; its currency is sovereign, separate, denominated-not-backed, non-convertible across platforms, never redeemable for fiat; and credit is earned, never bought, entering only behind a value-prop strong enough to pull migration.
2. **Sovereign substrate.** It runs, or can run, on infrastructure its participants can own — no unremovable hosting chokepoint.
3. **Witnessed, legible record.** Its record is immutable, tamper-evident, witnessed against equivocation — including the claim lifecycle, from filing — and PII-free in the commons; harm can be forgiven but never hidden.
4. **Reputation as covenant.** Its reputation is a covenant, not a score — a full distribution that never averages, contestable in both directions, typed by relation, gating whether-not-how-much.
5. **Governed by the cost of leaving.** Voice where contest is cheap, exit where it is dear, standing contestation at the core — and presentation is separable, with every participant holding the right to restyle their own render.
6. **A minimal, contested, stewarded core.** The specification is kept minimal, entrenched only where legibility and portability demand it, permanently contestable, and held by a named, internally-accountable steward.
7. **Legible above all.** It is documented and interpretively accessible enough that the people it governs can read it, fork it, and leave — its legibility is mechanized, not promised (decision receipts, policy as data with witnessed versions, prose bound to code by conformance checks, reproducible builds); its canon is preserved and broadcast redundantly enough that forking it does not depend on any single host's continued goodwill; and it ships a living open-questions document naming what remains unresolved about its future — staleness is nonconformance. A commons no one can read is a freedom no one can use.

### 7.1 Requests to refuse or flag

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
- *"Let the front end mint the filing record."* → Intake capture; the operator is present at its own claim's birth. File at an independent countersigner.
- *"Gate voting on an operator's average rating / show a single operator score."* → Rebuilds the average, and reads verdict-dissatisfaction as misconduct. Read conduct *structure* — dwell, dismissal patterns — not a rating count.
- *"Auto-remove an operator when the scan flags it."* → Makes the scanner the authority the record model forbids. The scan flags; adjudication decides; the operator contests.
- *"Just run it all on our one server or cloud account for now."* → Hosting chokepoint.
- *"Let a vendor pay to rank higher / have the network certify which claim is true."* → Buys reputation / installs a truth authority.
- *"Write the plain-English explainer as a separate doc / document it after launch."* → A second source of truth, born drifting. Legibility is generated from, or conformance-bound to, the artifact it explains — or it is marketing.
- *"Let themes run scripts / load remote assets."* → Self-XSS and beaconing. Presentation-sovereignty requirements one and two; refuse.
- *"Ship a starter theme that tidies away the harm distribution."* → System-authored occlusion. Presentation-sovereignty requirement five; refuse.

A quick test: if a change makes a layer harder to leave, makes the record easier to rewrite, makes credit convertible to or purchasable with fiat, makes some center the arbiter of value or truth, or lets an operator's own attestation stand in for an independent countersigner — it is almost certainly off-architecture. Flag it.

---

## 8. The tension protocol

While implementing, if you notice yourself doing any of the following, stop:

- reframing a constraint of this architecture so a feature becomes convenient,
- implementing a stand-in without labeling it,
- routing around one of the open problems instead of noting it.

These are the signals that the architecture is being quietly eroded. When you hit one: name the tension, attach it to the relevant invariant or open problem, and propose the minimal conformant move — the smallest change that meets the goal without breaking the standard, or the smallest experiment that bears on the open problem. Surface it; do not absorb it.

This document is held to the same discipline as everything else. It is unversioned because it is the standing description of the architecture, not a release: it is amended in the open when the architecture is. Build to the invariants, keep the open decisions cheaply reversible, surface what you find, and leave the values calls to the people who have to live with them.

> *"When the work is done and their aim fulfilled, the people will say, 'We did it ourselves.'"* — Tao Te Ching, 17

---

## References

- Acemoglu, D., & Robinson, J. A. (2012). *Why Nations Fail: The Origins of Power, Prosperity, and Poverty*. Crown.
- Acemoglu, D., & Robinson, J. A. (2019). *The Narrow Corridor: States, Societies, and the Fate of Liberty*. Penguin Press.
- Centola, D. (2018). *How Behavior Spreads: The Science of Complex Contagions*. Princeton University Press.
- FAO, IFAD, UNICEF, WFP, & WHO. (2024). *The State of Food Security and Nutrition in the World 2024*. FAO.
- Freeman, J. (1972–73). "The Tyranny of Structurelessness." *Berkeley Journal of Sociology*.
- Graeber, D. (2011). *Debt: The First 5,000 Years*. Melville House.
- Greco, T. H. (2009). *The End of Money and the Future of Civilization*. Chelsea Green.
- Hirschman, A. O. (1970). *Exit, Voice, and Loyalty: Responses to Decline in Firms, Organizations, and States*. Harvard University Press.
- Laurie, B., Langley, A., & Kasper, E. (2013). *Certificate Transparency*. RFC 6962, IETF.
- Leveson, N. G. (2011). *Engineering a Safer World: Systems Thinking Applied to Safety*. MIT Press.
- Michels, R. (1911). *Political Parties: A Sociological Study of the Oligarchical Tendencies of Modern Democracy*.
- Network Theory Applied Research Institute. *Addressing Democratic Information Velocity*. [ntari.org](https://www.ntari.org/post/ntari-whitepaper-addressing-democratic-information-velocity).
- Network Theory Applied Research Institute. *The Material Culture of Democratic Deliberation*. [ntari.org](https://www.ntari.org/post/the-material-culture-of-democratic-deliberation).
- Ostrom, E. (1990). *Governing the Commons: The Evolution of Institutions for Collective Action*. Cambridge University Press.
- Scholz, T., & Schneider, N. (Eds.). (2016). *Ours to Hack and to Own*. OR Books.
- Scott, J. C. (1998). *Seeing Like a State: How Certain Schemes to Improve the Human Condition Have Failed*. Yale University Press.
- Sen, A. (1981). *Poverty and Famines: An Essay on Entitlement and Deprivation*. Oxford University Press.
- Srinivasan, B. (2022). *The Network State*. thenetworkstate.com.
- Stodder, J. (2009). "Complementary Credit Networks and Macroeconomic Stability: Switzerland's Wirtschaftsring." *Journal of Economic Behavior & Organization*.
- Surowiecki, J. (2004). *The Wisdom of Crowds*. Doubleday.
- UNEP. (2024). *Food Waste Index Report 2024: Think, Eat, Save*. United Nations Environment Programme.
- U.S. Department of Housing and Urban Development. (2024). *The 2024 Annual Homeless Assessment Report (AHAR) to Congress, Part 1*.
- Watzlawick, P., Bavelas, J. B., & Jackson, D. D. (1967). *Pragmatics of Human Communication*. W. W. Norton & Company.

---

*Network Theory Applied Research Institute, Inc. — 501(c)(3) — EIN 92-3047136 — info@ntari.org*

*This document is free documentation under the project's AGPL-3.0 commons; it is meant to be read, reimplemented, and contested.*
