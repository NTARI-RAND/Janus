# Janus-Facing Architecture

**The unified architecture document: the argument, the five layers, the mechanisms within them, the invariants those mechanisms must satisfy, the standard a conformant system must pass, and the problems that remain open.**

Network Theory Applied Research Institute

This document names *roles and mechanisms* — coordination protocol, coordinator, front end, ledger, anchor, witness, assessment scale, governance venue — never the software that fills them. Any implementation, present or future, binds to a role defined here; where an implementation and this document disagree, either the implementation is fixed or this document is amended in the open.

**The demand.** The failure this architecture answers is not scarcity. The world wasted just over a billion tonnes of food in 2022 — a fifth of everything available to consumers, with another 13 percent lost upstream of retail ([UNEP, *Food Waste Index Report 2024*](https://www.unep.org/resources/publication/food-waste-index-report-2024)) — in the same years that more than 730 million people went hungry (FAO, *The State of Food Security and Nutrition in the World*, 2024). The United States holds roughly fifteen million vacant housing units while counting some 770,000 people homeless on a single January night (HUD, *2024 Annual Homeless Assessment Report*). Amartya Sen showed four decades ago that modern famines arrive without any decline in food availability: people starve not because the goods are missing but because their entitlement to them fails. The pattern is general, and it is not a production problem — the surplus exists; what fails is coordination. Markets move goods toward money rather than toward need, and the administered alternative rebuilds the unanswerable center that decides for everyone. And where the want is real scarcity rather than stranded surplus, the answer is the same infrastructure seen from the other side: mutual credit issues liquidity at the moment of exchange, backed by capacity rather than reserves, so a community poor in money but not in ability can clear its own trade — and the coordination itself is nearly weightless, costing almost nothing to extend wherever the internet can reach. The demand, then, is for coordination infrastructure that moves real goods and services against real needs without concentrating the power to decide who may have what — which is the work this document specifies.

**How to read this if you are implementing.** Parts I and II carry the argument; the operative sections are Part III (the invariants, grouped by the layer they defend), Part IV (how the signals move), the refuse-or-flag list, and the standard; Parts V and VI are labeled explorations, and Part VII is the honest list of what remains unsolved. Where a rule says MUST, MUST NOT, or MAY, the keyword carries the force RFC 2119 gives it. Every invariant carries a stable identifier, `SUB-1` through `LEG-2`, printed beside its statement; the executable conformance suite that ships beside this document holds the registry and verifies the pairing, and a conformant repository cites those identifiers in its own test suite — until it does, its conformance is self-attested. And this document is the constitution, not the wire specification: it names roles and the requirements they satisfy; schemas, formats, and state machines live with the protocol artifacts that bind to these roles.

---

## Glossary — the terms of art

*Definitions orient; the normative text below governs. Every term names a role or a mechanism, never a product.*

**The whole stack**

- **Janus-facing** — the permanent two-way posture: one face coordinates, the other checks the coordination — two functions carried and exchanged by one community, never two populations.
- **The one rule** — govern every layer by the cost of leaving it: exit where leaving is cheap, voice where it is dear, standing contestation where it is impossible.
- **Layer** — one of the five strata of the stack: Substrate, Record, Covenant, Governance, Economy & Information. Each is sovereign only because the one beneath it is.
- **Gravity well** — the stack pictured as a well: shallow at the surface, where users drift freely between front ends; bottomless at the core, the spec you contest but cannot exit.
- **Mutual credit network** — the one thing built here: an economy in which members extend value to one another against a covenant not to harm, on a record no one can rewrite, on hardware no one can revoke, with no central issuer of money and no central judge of trust.
- **Maximum Observational Diversity (MOD)** — the root of witnessing: maintaining a false pattern grows expensive as independent, diverse observers multiply.
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
- **Witness** — an independent party that countersigns checkpoints so that showing two histories becomes provable; a witness confers no authority.
- **Witness relay** — scheduling and caching plumbing for witnessing; it relays and serves proofs, and never decides which witnesses count.
- **Equivocation** — an operator showing different histories to different audiences; two validly-signed, mutually-inconsistent checkpoints are the portable proof.
- **Claim lifecycle** — file → adjudicate → resolve → seal, each transition witnessed as it happens; filing goes to an independent witness, with the operator absent.
- **Dwell** — how long a claim has sat open past a movable threshold; a readable fact, never a verdict.
- **Stand-in label** — the mandatory marker on any deployment running with fewer than two independent witnesses; a single-witness system may not present itself as federated.

**Covenant**

- **Covenant** — the third layer: trust as a standing promise not to harm, not a score; a member is in good standing or in breach.
- **Assessment scale** — the harm-surfacing rating scale (Leveson-derived); the lowest rating is the breach itself.
- **Full distribution** — reputation carried as the count at each rating level beside the total; never averaged into one figure.
- **Relation type** — the typing of ratings and claims (trade, adjudication-conduct, verdict-satisfaction); collapsing them rebuilds the forbidden average across relations.
- **Symmetry** — every claim is answerable and every dismissal is an annotation; a rated party with no recourse is a breach of the covenant's own rules.
- **Limit** — the separate instrument that caps how large a commitment an honest member may take on; never derived from the harm distribution.

**Economy & Information**

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
- **Operator-federation** — the explored answer to open problem 4: the governing electorate is corroborated-active operators, one vote per person.
- **Cross-operator corroboration** — operator recognition by other, independent operators; operators under common control corroborate nothing.
- **Genesis operator set** — the founding steward's standing representatives, serving as the bootstrap trust root before corroboration binds.
- **Governance venue** — where deliberation and voting happen; it must itself be leaveable substrate, and any proprietary venue is a named interim.
- **Legibility ladder** — the seven mechanized rungs that bind plain language to running code, from decision receipts at the point of use to reproducible, witnessed builds.

---

## Part I — the argument

**Why "Janus-facing."** In *The Narrow Corridor* (2019), the economists Daron Acemoglu and James A. Robinson describe the state as Janus-faced: it shows the people a favorable face in one moment, then turns to show a monstrous one. The contest between state and society, in their telling, is a Red Queen race — each side running hard against the other to keep the monstrous face from showing. Acemoglu and Robinson kept the state–society hierarchy and asked how to hold it in balance. This work collapses that hierarchy back into the mass of the people. Ordinarily the collapse would mean anarchy; with the internet as infrastructure, the communication patterns of a whole population can be made fast and rich enough that the state-over-people hierarchy is no longer needed.

The architecture therefore faces two ways at once, permanently: one face coordinates, the other checks the coordination. These are not two populations — a platform and its users, a state and its society — but two *functions* that the same community carries simultaneously and exchanges continuously. Every layer and mechanism below exists to keep that exchange running fast enough, and legibly enough, that the balance between coordinating power and checking power is held by the motion of communication through the wire — and the social and economic needs of the whole are met.

**One rule, one form.** The whole architecture compresses to one rule: **govern every layer by the cost of leaving it.** Where leaving is cheap, exit governs, and almost no machinery is needed. Where leaving is dear, voice must do the work exit cannot. Where leaving is impossible, keep the layer minimal, keep it legible, and hold it under permanent contest.

What is built under the rule is one kind of thing: a **mutual credit network** — an economy in which members extend value to one another against a covenant not to harm, on a record no one can quietly rewrite, on hardware no one can revoke, with no central issuer of money and no central judge of trust. Mutual credit is a proven form, not a theory awaiting trial: complementary credit has cleared real trade for decades — Switzerland's WIR Bank since 1934, Sardex across Sardinia for over a decade. The work here is instantiating it digitally, under a discipline that keeps it from curdling into its opposite.

The rule and the form are inseparable, and seeing why is the whole point. Every mutual credit network contains a **scorer** (who is trustworthy?), an **issuer** (whose credit is good?), and a **ledger** (what happened?). Concentrate any one of them and you have rebuilt the bank: an authority that decides who is creditworthy and answers to no one. The architecture is the only thing standing between mutual credit and that outcome — it keeps the scorer contestable, the ledger legible, and exit cheap, so the power to extend or deny credit never settles where it cannot be checked or left. Run it the other way around and the rule alone is abstract; the economy is what gives every layer a concrete job. The form supplies the work; the rule keeps the work free.

**Architecture over ownership.** A platform's interface communicates on two levels at once: the content level — what a button does — and the relationship level — who the participant is to whom. This is Watzlawick, Bavelas, and Jackson's axiom that every communication carries a content and a relationship aspect, the relationship classifying the content — the term *metacommunication* is Bateson's — applied to the screen. An interface that gives each class of participant only the information its role requires is saying something on that second level: it metacommunicates subordination. It tells participants to trust calculations they cannot inspect, and it prevents each side from taking the other's role and recognizing a common interest. Hierarchy is thereby enforced beneath ownership. This is why cooperative ownership of an extractive architecture reproduces extraction: ownership is downstream of architecture, and an architecture of asymmetry maintains concentrated power no matter who holds the equity.

**The stage is not the play.** Transparency is not the cure, because disclosure is not verification: an operator can publish an algorithm and run modified code, and a "transparent" interface will faithfully render the manipulated result. Symmetry is not the solution either: information equality does not equalize the capacity to act, and transparency no one consumes is decoration. And exit is expensive: the right to fork a live network is hollow when forking abandons the liquidity. A lit, level stage on which everyone sees the same thing is necessary — and insufficient. The play is the *contest*, and the contest has to go on being performed.

**Homeostasis, not harmony.** Liberty at platform scale is the balance between a coordinating capacity strong enough to be useful and a checking capacity strong enough to restrain it — neither permanently ahead, the running itself holding the corridor open. Collapsing the two into "the community is both the power and the check," left unqualified, is the founding sentence of despotism. The collapse is liberating in only one reading: the two forces are two functions held by one population and swapped quickly — a thermostat, not a throne. The balance is maintained only by continuous motion and the expenditure of energy. There is no finish line.

**Mesh, not conductor.** Orchestration in the conductor's sense — a layer that sits between every actor, prevents collisions, and "maintains the music" — smuggles sovereignty into the infrastructure: whatever defines and stops coercion is the Leviathan, hidden and unanswerable. Orchestration in the mesh sense does the opposite. It exposes collisions rather than suppressing them, prices friction rather than forbidding it, routes dissent rather than dissolving it, and makes the reversal of roles cheap and legible — so the coordinated can become the coordinators.

**Voice, exit, and a contested core.** No single coordination layer can sit between every actor without becoming the thing it polices, so the coordinating function is distributed across layers by the cost of leaving each one (the exit-and-voice vocabulary is Albert Hirschman's). Where contest is cheap — between peers — the mechanism is *voice*: contestable reputation. Where a participant cannot litigate design — against a front end or a host — the mechanism is *exit*, made cheap by keeping the market, the matching, and the record in the protocol rather than the front end. And at the one layer no one can leave — the specification that defines exit for everything beneath it — the mechanism is *standing contestation*: keep the core minimal so capturing it yields little, keep it legible so reimplementation stays possible, and keep the opposition standing so ratification is never final.

Picture the stack as a **gravity well**: the deeper the layer, the higher the cost of leaving — shallow at the surface, where users drift off freely, and bottomless at the core, the spec you contest but cannot exit. Its companion image is the dependency stack read floor-up; the two are the same architecture seen as a force and as a sequence.

**Legibility is the hinge.** A license guarantees the right to fork; it cannot supply the capacity. The capacity comes from liquidity and reputation living in the protocol (so the cheap exit is real) and from legibility (so the expensive exit is at least possible). Every artifact ships documented and interpretively accessible enough that a downstream community can actually exercise the freedom the license promises. A commons no one can read is a freedom no one can use — and an opaque coordination layer claiming to be the orchestra is precisely the despot the architecture exists to prevent.

---

## The shared philosophy — three roots

The architecture and the governance that stewards it grow from a scientific philosophy — one that makes every user, every operator, and the architecture itself observers employing the scientific method — and it is load-bearing everywhere below.

**Maximum Observational Diversity (MOD).** Maintaining a false pattern grows computationally expensive as independent, diverse observers multiply. This is the root of the witnessed record: it is *why* two or more independent witnesses make equivocation detectable, and why witness diversity is a requirement rather than a nicety.

**Minimum Sustainable Projection (MSP).** Build so that truth-aligned behavior is the path of least resistance, on the fewest assumptions. This is the root of the minimal, contestable core and of every Sybil posture here: make dishonesty *cost more than it pays* rather than pretend to make it impossible.

**The scientific method as necessary ritual.** Sacred doubt, distributed validation, falsifiability. This is the root of contestation: anchor a claim, never certify it.

Where this document says *detection not prevention*, *minimal core*, *witness diversity*, or *contestable flag*, it is applying MOD and MSP.

---

## Part II — the five layers and the mechanisms within them

Sovereignty is built from the bottom. You cannot decentralize governance onto infrastructure you do not own, and you cannot run an honest economy on a record someone can rewrite. So the architecture is one stack of five layers, each sovereign only because the one beneath it is — and the order is the argument. Build bottom-up: substrate, then record, then covenant, then economy — the place-to-run *before* the things that run on it. Invert the order and every layer above the inversion is decoration. A mechanism named in a higher row depends only on rows beneath it.

| Layer | What it guarantees | Mechanisms within it |
|---|---|---|
| **Substrate** | Coordination on infrastructure participants can own | The **coordination protocol** (a dependency leaf) · the **coordinator** (node-side orchestration) · **front ends** (the member-facing applications) |
| **Record** | A witnessed, append-only memory no operator can rewrite — including the adjudication lifecycle, not only the sealed verdict | The **per-operator dialog ledger** · **anchor commitments** (structural facts and references committed to the commons) · **independent witnesses** and the **witness relay** |
| **Covenant** | Reputation as a full, un-averaged, symmetric distribution, typed by relation | The **assessment scale** (harm-surfacing, Leveson-derived) · the **distribution record** · the **claim/dispute/adjudication mechanism** |
| **Governance** | Every layer stays leaveable; the core stays minimal; the governed can become the governing | The **minimal entrenched core** · **open circles with recallable delegates** · **layer-aligned officer stewardship** · **standing contestation channels** · the **sovereign governance venue** · **provenance discipline** (copyleft commons, developer certificate of origin) |
| **Economy & Information** | Member-issued credit, and a witnessed knowledge commons | **Mutual credit** with the escrow/credit switch · **knowledge-claim anchoring and citation** |

Each row holds a mix of built, designed, and intended mechanisms; the layer is real to the degree its lowest mechanisms are, and Part VII is honest about where each stands.

---

## Part III — invariants to enforce in code

These are the conformance checks turned into implementation rules, grouped by the layer they defend. They are not negotiable by a feature request. Where a rule says MUST NOT, a change that violates it is not a smaller version of this architecture; it is a different architecture.

### Substrate

Start with the dependency most designs never name: software has to run on someone's hardware. An open, forkable protocol is worth little if the only place it can practically run is a hyperscaler or one operator's servers — whoever owns the iron owns the network, and the openness is decoration. The substrate gives every community somewhere to run the protocol, or a fork of it, that no one can revoke.

Be honest about what this buys. Sovereign compute buys *mechanical* exit, not social or economic exit. The chokepoint relocates rather than disappears — to the coordinator's fees, and to reputation cold-start, since a fresh node with no standing draws no work (the deliverability problem that recentralized email despite its open, self-hostable protocol). The substrate *caps* how concentrated hosting can become; it does not *guarantee* hosting stays distributed — that guarantee comes from legibility and cheap exit, never from the mechanism alone (open problem 7). And because compute is forkable, the substrate is emphatically *not* the layer no one can leave; that layer is the spec, far above it.

- The platform MUST run, or be able to run, on infrastructure its participants can own; **no unremovable hosting chokepoint.** `SUB-1`
- The coordination protocol is a **dependency leaf.** It depends on nothing but its language's standard library; the coordinator and the front ends depend on the protocol and never on each other. `SUB-2`
- **Single participant identity.** One account carries the simultaneous roles of contributor and consumer; never split a person into a producer identity and a consumer identity. `SUB-3`
- Persons never appear on the coordination wire. Front ends speak the node-side surface on behalf of member machines; long-term the coordinator models no persons at all. `SUB-4`

#### Presentation sovereignty

The cheapest exit in the stack is the render itself, and it gets the discipline of pure exit: **presentation separability** — styling ships as user-editable data separate from application logic, and every participant holds the right to restyle their own render. The gravity well extends one layer up: leaving a rendering costs nothing, so the layer is governed by exit alone and needs no machinery beyond the right itself. And it answers the metacommunication problem on its own ground: if hierarchy is enforced at the level of the screen, the counter is that the governed can rewrite their own screen. The recommended pattern — recommended, not mandated, lest the minimal core grow a contested product feature — is in-app editing of the front end's CSS and HTML, saved and rendered locally: customization with no fork, no toolchain, no permission. Scope is self-view only, by decision rather than omission: a participant's styling affects their own render exclusively; nothing about it enters the commons or any other participant's view.

Five requirements, invariant-grade, enforced at import and paste — where the front end actually holds the content — because themes will circulate out of band regardless of any local-only intent:

- **Scripts never; markup sandboxed.** Pasted themes carrying executable content are the standing self-XSS attack; HTML customization is structural and presentational only — no theme executes. `SUB-5`
- **No remote fetches from user styles.** CSS alone phones home — `url()`, `@import`, `@font-face` — and a circulated theme becomes a beacon; strip or block remote references at import. Privacy-first entails this even with no publish path. `SUB-6`
- **Reset-to-default lives outside the styleable surface.** The undo cannot be occludable by the thing it undoes. `SUB-7`
- **Styles are plain, exportable artifacts.** A CSS or HTML file the user can read, carry, and reapply — never an opaque blob; and the customization stays entirely out of the commons. `SUB-8`
- **Shipped or hosted themes inherit the carve-out.** A user hiding covenant surfaces from themselves is sovereignty; a front end shipping or hosting a theme that does so is the system hiding harm with extra steps. `SUB-9`

The default theme carries the WCAG 2.2 AA floor and the editor itself meets it; a participant's own overrides are their own — self-view restyling is the user-stylesheet tradition the accessibility standards exist to protect. Left open, by decision: **published styling** — customization as expression to others — remains a cheaply reversible later option behind one recorded condition (any view shown to others renders covenant-mandated surfaces — harm distributions, adjudication status — platform-controlled and non-occludable); and **theme-gallery governance**, for which the fifth requirement is the floor and curation beyond it is undecided.

### Record

On the substrate sits the record: an account of what happened that no one can quietly rewrite. The design philosophy is *detection, not prevention* — you do not make tampering impossible; you make it evident. The construction is the certificate-transparency model, not consensus: each operator keeps its own append-only log and publishes signed, monotonic checkpoints to independent witnesses. An operator that shows two different histories thereby produces two validly-signed, mutually-inconsistent checkpoints — a self-evident, attributable, portable proof that it lied. The *form* of the ledger is shared across platforms because the construction is domain-independent; each platform runs its own *separate* log over it.

- The ledger MUST be **append-only.** Corrections are new entries; there is no update-in-place and no delete. `REC-1`
- A front end MAY forgive a harm; it MUST NOT hide one. A dismissal is a new visible annotation, never an erasure. `REC-2`
- The commons MUST NOT contain PII. Anchor **structural facts and references only**; the free-text narrative and anything identifying lives in the erasable, front-end-local layer. `REC-3`
- The atomic unit is the **dialog.** It seals only when complete (every party owed a rating has one; a non-rater is assigned a marked default, so silence is never read as praise) and quiescent (no open dispute; a harm claim holds the seal open in both directions until adjudicated). `REC-4`
- Each operator keeps its **own log.** There MUST NOT be one global chain or a consensus layer over unrelated exchanges. Non-equivocation comes from **witnessing** — signed, monotonic checkpoints to independent witnesses — not from a shared authority. `REC-5`
- **A witness confers no authority.** The witness relay may schedule, relay, cache, and serve inclusion proofs; it MUST NOT decide which witnesses count, which checkpoint is official, or gate settlement on its blessing. Everything it does must remain possible without it. `REC-6`
- **The witnessed unit is the claim lifecycle, not only the sealed verdict.** A harm claim's *filing*, its *adjudication*, its *resolution*, and its *seal* each commit to the witnessed record **as they happen** — a sequence of monotonic, independently-witnessed transitions, never one terminal block delivered whole. Witnessing only the final sealed adjudication lets an operator present a clean artifact whose process it captured unseen; the integrity comes from the *filing* being witnessed before the operator acts. `REC-7`
- **A harm claim's filing commitment is made at an independent witness,** upstream of the operator that will adjudicate it. This is a deliberate, bounded exception to the witness-as-observer role: the witness accepts exactly one write — claim-creation — and nothing else, and MUST NOT become a second log for any other event. Its purpose is intake integrity — the operator is absent from its own claim's birth, so it cannot add filing friction, shape a claim, or shed it before the claim exists in the record. (This creates a liveness dependency; see open problem 8.) `REC-8`
- **Ratings and claims carry a relation type.** Trade, adjudication-conduct, and verdict-satisfaction are different relations with different base rates; the record MUST distinguish them. No reader may collapse them into one figure — that is the average the covenant forbids, committed across relations instead of across ratings. `REC-9`
- **PII discipline binds hardest at filing.** The filing commitment witnesses a hash, a type, a timestamp, and an exchange reference — the structural fact that a claim of a kind exists — **never** the narrative or the identities, which stay front-end-local and erasable. A clock never force-seals a dialog; an unanswered claim stays open, and only its *dwell* is a readable fact. `REC-10`

### Covenant

On the record sits trust, built as a covenant — a standing promise not to harm — not a score. It is binary where it counts: a member is in good standing or in breach, and the lowest rating *is* the breach. The logic is the safety engineer's: two crashes in seventy-three flights grounds the fleet, and no quantity of good ratings dissolves a harm into a comfortable average.

There is a subtle failure mode to engineer against: the covenant secures *honesty, not capacity*. "I will not harm you" is not "I can deliver what I promised" — an honest party can over-extend and fail. Non-delivery is itself a harm and belongs in the covenant; *bounding how large a commitment an honest actor may take on* is a different instrument — a limit, which belongs to the economy. Let the two merge — let good standing buy a higher ceiling — and the harm distribution quietly becomes a credit score, and the bank returns through the back door.

- Reputation MUST NOT be averaged into a score. Carry the **full distribution** — the count at each level beside the total — so a harm stays visible beside the volume permanently. `COV-1`
- The **lowest rating is the breach itself**, not a debit against a total. `COV-2`
- The covenant MUST be **symmetric:** every claim is answerable; dismissals are annotations. **A rated party with no answer is a symmetry breach** — an adjudicator rated without recourse is the one place this invariant is broken, and it must be fixed, not shipped. `COV-3`
- Reputation gates **whether** a member transacts on trust, never **how much.** `COV-4`
- Reputation is **per-platform and non-portable by default.** Carrying standing across platforms is a governance decision (open problem 5), never an implementation default. `COV-5`
- When reputation informs anything beyond whether-a-member-transacts — credit, citation weight, **or governance standing** — Sybil-resistance MUST be settled first (open problem 4), and governance standing read from conduct is **structure, never a score.** `COV-6`

### Economy

At the top sits the economy: mutual credit *derived from the record, not bolted onto it* — money created at the moment of exchange, one balance negative, one positive, the sum always zero, backed not by a reserve but by members' covenant and their capacity to deliver real goods and work.

Keeping each economy's currency sovereign is the anti-colonial monetary move. Each community issues and clears in a unit no outside party can inflate, or devalue into dependence; a unified currency would force the ledgers to stop being independent and would rebuild precisely the shared, no-exit core the architecture works to keep small. (Separate currencies do *not* force separate identities — portable reputation remains available as a governance decision, open problem 5, a far lighter lift than unifying money.) The peg is a yardstick, never a tether, and the intuition runs backward here: a fixed rate between economies of unequal productivity does not equalize them; it removes the valve that lets the weaker one adjust, and forces the divergence out as something crueler — unemployment, wage cuts. The Eurozone periphery and the interwar gold standard are the warning, not the model.

The defense against domination is *sovereignty*: issuing your own unit and never owing in someone else's. So the fiat unit is the unit of *account*, never the *backing* — denominate at par; never redeem at par. A unit counted in fiat but not cashable for it is internal credit; a unit redeemable for fiat against reserves is a stablecoin, and a regulated money-transmitter.

- Balances MUST be a **deterministic function of the sealed record;** each sealed exchange moves two balances that net to zero. `ECO-1`
- Issuance MUST be **gated by the covenant and capped by a separate limit.** The limit MUST NOT be derived from the harm distribution. The covenant gates the door; the limit sizes the room. `ECO-2`
- Each platform's currency is **sovereign and separate.** No cross-platform currency, no fixed convertibility between two platforms' units. `ECO-3`
- The unit is denominated against fiat one-to-one **for legibility only.** Denomination is NOT redemption: not redeemable for fiat against reserves, not purchasable with fiat. It is earned for value provided, and spend-only. `ECO-4`
- Today's settlement is **escrow.** The escrow-now / credit-later switch is a governed configuration change, not a rebuild. `ECO-5`
- **Value stays home; only truth crosses.** Two members in different economies may exchange as two sovereign spends bound atomically by a witnessed proof — no shared or convertible unit, no central clearer, no administered cross-economy rate. `ECO-6`

#### Switching credit on

You cannot cold-start mutual credit. A credit network with few members is worthless — no one to trade with, no one whose credit is worth extending — so credit switches on in three phases, and the order matters as much as it did in the stack.

**Phase one — fiat on-ramp and integrity display.** Members transact in fiat through the escrow marketplace. Real fiat earnings for real work attract the volume you need, and the witnessed ledger runs underneath, building and *displaying* an auditable record of honest dealing. The escrow lives here, and you say plainly that it is the opposite of credit — collateralized in advance, no balance ever negative, no trust ever extended. This phase has two goals only: critical mass, and visible integrity.

**Phase two — earned, non-redeemable credit enters.** Once there is volume and visible trust, introduce the mutual-credit unit — but only as *earned* (issued for value provided to the network, never bought with fiat) and *non-redeemable* (spend-only, in-network, denominated in fiat but never convertible to it). Its value proposition is the one thing fiat cannot do in-network: counter-cyclical, interest-free credit — liquidity precisely when outside money is scarce. That, not a screen, is what moves people. Migration is *pulled by the value-prop, never pushed by a button*: nobody trades liquid fiat for a non-redeemable unit because an interface asks them to; they do it when the unit does something fiat cannot. Security earns trust-to-*hold*; only the value-prop earns want-to-hold. Non-redeemability does double duty, which is why it is non-negotiable: it is the **regulatory firewall** — a unit that is earned and never cashable is barter-credit, not the money-transmission or securities activity a redeemable, purchasable token would be — and it is the **adverse-selection filter**: with no fiat yield to extract, pure extractors self-select out as the fiat phase recedes, and the members who remain are exactly the ones who value in-network credit. The migration is therefore also a population sort.

**Phase three — the internal economy thickens; fiat retreats to the perimeter.** As the credit proves more useful in-network than fiat — especially in a crunch — internal volume grows and fiat falls back to the boundary: taxes, outside suppliers, the genuinely external. The end state is mutual credit governed by the architecture, with fiat as the interface to the outside rather than the medium within.

The non-negotiables, one line each: the unit is earned, never purchased; it is non-redeemable (firewall and filter both); denomination is not redemption; migration is pulled by a value-prop, never pushed by a UI; the covenant and the limit gate issuance throughout; and get a real regulatory read *before* phase two — a nonprofit issuing a quasi-currency sits on a money-transmitter and securities knife-edge, and earned-not-bought plus non-redeemable is the line you do not cross by accident.

One decision belongs to each instance, not to the architecture: decide *who* the first users are before *how* to recruit them. A broad fiat lure buys fast volume and a money-motivated founding population, and bets that the adverse-selection filter sorts them out later. A targeted value-prop draw — recruiting members who already feel the credit pain the network solves, the path the longest-lived mutual credit networks took — buys alignment and culture at the cost of speed. Both are legitimate. If you take the lure, the filter is what you are betting on; make sure it holds.

### Governance

The rule now does its work: each layer gets the only discipline that can hold it. *Voice* governs the peer layer, where the contest is cheap and runs as argument. *Exit* governs the front ends and the substrate, where the market, the record, and the compute all live below any single front end, so leaving one costs only that one — a community reads a front end's trajectory and leaves on the trend rather than waiting for collapse, and a failing front end migrates its users without destroying the market. *Contestation* governs the core — the protocol specification — the one layer no one can cheaply leave, because forking it splits the liquidity.

- Govern each layer **by the cost of leaving it:** voice at the peer layer, exit at the front ends and substrate, contestation at the core. Keep the core minimal — it guarantees only the portabilities that keep every layer above it leaveable, so capturing it pays little. `GOV-1`
- **Name the steward.** A network governed by "the community" in the abstract is governed by whoever shows up — the tyranny of structurelessness, capture in open-source clothing. The one layer with no exit is stewarded by a named, internally-accountable body, its board filled from the bottom with recallable delegates of open circles, disciplined by the three things that can discipline a no-exit layer: the entrenchment of its deepest commitments, the expensive-but-real fork of its implementation, and the obligation to keep internal opposition standing. `GOV-2`
- **Stewardship mirrors the stack.** `GOV-3` The steward's five standing offices align one-to-one with the five layers, so every layer has exactly one named, recallable officer answerable for its conformance and legibility:
  - the **workspace administration** stewards the Substrate — the venue and infrastructure, including the committed exit from any proprietary interim;
  - the **secretariat** stewards the Record — the office that keeps the minutes is the office that answers for the append-only, witnessed discipline of the ledger;
  - the **presidency** stewards the Covenant — the assessment scale's integrity, its symmetry, and the no-averaging discipline;
  - the **vice-presidency** stewards Governance — the minimal core, the contestation channels, and the venue exit; this is the same office as the investigative-not-dispositive audit authority of Part V;
  - the **treasury** stewards Economy & Information — issuance gating, the escrow/credit switch, the regulatory read, and the knowledge commons' no-truth-authority discipline.

  One-to-one is the point: an unassigned layer decays with no one answerable, and a doubled office concentrates exactly what the stack distributes. Two constraints keep the alignment conformant. *Stewardship is answerability, not authority:* an officer answers for their layer's conformance; they do not become its adjudicator — the secretariat no more decides which checkpoint is official than a witness does, the presidency stewards the covenant's discipline but never holds a verdict on a claim, and the treasury tends issuance policy as governed, witnessed policy changes, never per-member discretion. *The alignment inherits recall:* each office is a recallable delegate of an open circle, so the governed can replace the steward of any layer that is drifting — the stack's leaveability applied to its own stewardship.
- **The core's deepest commitments are entrenched only where legibility and portability demand it** — open source; privacy-first and data sovereignty; no surveillance economics — behind a double lock (a supermajority of all voting members *plus* unanimity of the stewarding board). Entrench there and **nowhere more** — over-entrenchment makes the core less contestable, not safer. `GOV-4`
- **Delegates are recallable; circles are open.** Standing representatives are elected by open deliberative channels and recallable by their channel or by a supermajority of the membership — the governed can always become the governors of the role that governs them. `GOV-5`
- **Contestation keeps opposition standing; it never averages dissent away.** Any member, including one who did not vote, may reopen a decided matter with an observation; and in deliberative synthesis, a single documented harm reopens the synthesis rather than being averaged into it — the covenant's no-averaging posture applied to deliberation. A synthesis that smoothed dissent *without* the harm-reopen would be the averaging the covenant forbids; the reopen is what keeps it conformant. `GOV-6`
- **One person, one vote** — no proxy, no delegation. Where a status gates the electorate (Part V), it is a **qualifier on this vote, never a multiplier** — a person is one vote whether they hold the qualifying status once or ten times over. `GOV-7`
- **Legibility is an output, not a comment.** Treat documentation and interpretive accessibility as a build deliverable equal to the code. The mechanisms are the legibility ladder, below. `GOV-8`
- **Every project ships a living open-questions document** — a build deliverable equal to its code, naming what is unresolved about the project's future. This generalizes the network-level open problem stack (Part VII) down to every project in the canon. It is not a roadmap: a roadmap pre-decides; this names — questions, constraints, and status, never commitments dressed as questions. Each entry states the problem, the constraints any resolution inherits from the architecture (a resolution violating them is not a resolution), and current status. Living means reviewed and re-shipped with each release: a stale open-questions document is conformance drift, not housekeeping — a project performing the absence of its gaps has failed the method, whatever its code does. An entry leaves the document only by resolution or by an explicit values call made by the people who live with the outcome; silent absorption is the erosion the tension protocol exists to catch. A question discovered locally that binds architecturally is promoted to Part VII, not kept local, and the network stack and the project documents cite each other in both directions. `GOV-9`
- **Provenance is inbound = outbound.** Every contribution enters the copyleft commons and cannot be reclaimed; no contributor license agreement, no assignment to a center. PII is not a contribution — the record's no-PII rule restated as a governance commitment. **The covenant never suspends; its enforcement mechanism may.** A provenance check (certificate-of-origin sign-off or equivalent) may be suspended only as a named interim with a committed reinstatement, recorded visibly in the affected repo's conformance self-description and reported until reinstated — the interim-steward pattern applied to a mechanism. Two honesties bind the suspension: contributions made during the window still enter the commons under the covenant, and the enforcement gap is **permanent for the commits made inside it** — reinstatement cannot retroactively certify them, so the window is kept short and its start and end are matters of record. `GOV-10`
- **The governance venue must itself be leaveable substrate.** A proprietary, revocable hosted venue is a hosting chokepoint at the core; it is conformant *only* as a named interim with a committed exit to sovereign coordination substrate. The sovereign venue also makes the witnessed record readable for the governance read (Parts IV–V) — a legibility tool that **confers no authority**; disposition stays with the contested federation, never the reader. `GOV-11`
- Do not build for a static, symmetric end-state. The balance between coordinating and checking is held by **motion.** `GOV-12`

#### The legibility ladder

The legibility invariant says *must*; this subsection says *how*. Lay members will never read source, in any language, under any formatting discipline — that is not the barrier to remove. "The governed can read the logic that governs them" decomposes into two capacities: **every member can directly read the rules that govern them, and anyone independent can cheaply verify that the running code embodies those rules.** The mechanisms are a ladder, and the binding principle is that each rung MUST be mechanically bound to the rung below it. A plain-language layer that merely mirrors the code is a second source of truth, born drifting — and drift converts inspection into marketing. Unverified explanation is not legibility. `LEG-1`

1. **Decisions explain themselves at the point of use.** Every governance-relevant output — a match, a fee, a rating display, a sealed dialog, a flag — ships with a receipt: which rule fired, on which inputs, linked to the rule's plain statement. A member inspects the decision that touched them, immediately, in the interface. This is the fee-declaration pattern generalized.
2. **Rules live as data, not code.** Split mechanism from policy. The engine — rarely changing, expert-audited — executes policy expressed declaratively: fee schedules, rating scales, seal conditions, dwell thresholds, credit limits. Policy renders as plain tables and sentences, and is diffable by anyone. Nearly every change that governs people lands in policy; this rung is where most lay inspectability actually lives.
3. **Policy versions commit to the witnessed record.** Treat rule changes exactly like exchanges: append-only, witnessed, each with a plain-language changelog entry. *The rules cannot be quietly rewritten* becomes the same guarantee, from the same machinery, as *the record cannot be quietly rewritten* — and "what rule was in force when my dialog sealed?" has a witnessed answer.
4. **The spec is the constitution, written in prose.** Normative plain language first, wire format second — literate enough that a motivated lay reader can follow the argument of the protocol, not only its bytes.
5. **Conformance tests bind the prose to the code.** The load-bearing rung. Every normative sentence in the spec, and every rendered policy statement, maps to an executable check, so that prose which can fail the build is trustworthy prose. Without this rung, every layer above the code quietly diverges from the one that runs.
6. **The trusted core stays small and boring.** A dependency-leaf protocol of a few thousand literate lines is inspectable by a motivated lay person with an afternoon and a guided tour; nothing of half a million lines is inspectable by anyone. The minimal honest core is itself a legibility mechanism: shrink what must be trusted until reading it is a feasible act.
7. **Builds are reproducible; release hashes are witnessed.** Disclosure is not verification — the recipe is not the kitchen. The code someone reads must provably be the code that runs: reproducible builds, signed releases, front ends displaying the hash of what they run, release hashes committed to the witnessed record. A lay member never rebuilds; anyone independent can, cheaply.

The guarantee, stated in the architecture's own terms: it never comes from every member personally auditing the code — it comes from making verification cheap and distributed enough that many independent observers *can*, which makes maintaining a false pattern expensive. This is MOD applied to legibility, the same argument as witnessing. A member's direct experience is rungs 1–3: read the rule that touched me, and see that it cannot be silently changed. Rungs 4–7 are what make the delegated check trustworthy without trusting any particular checker.

Machine reading aids — a member interrogating the repository through a model ("explain the seal logic to me") — are worth designing for: structure the code and spec so guided explanation comes out accurate. But an aid MUST remain a reading aid, never an oracle. A "verified true" explanation from any model is the truth authority the architecture forbids; the aid's claims are checkable against the spec and the conformance suite, which is one more reason rung 5 is load-bearing. `LEG-2`

### Requests to refuse or flag

- *"Let users cash out / redeem credits for dollars."* → Redeemability. The unit is spend-only.
- *"Let users buy credits with dollars."* → Purchasable currency / deposit-taking. The unit is earned, never bought.
- *"Convert one economy's currency to another's at a fixed rate."* → Currency merger. Cross-economy trade is atomic barter over the witness, never a shared unit.
- *"Show a single reputation score / average the ratings."* → Rebuilds the score the covenant forbids.
- *"Raise a member's credit limit when their reputation is good."* → Merges covenant with limit. Keep them separate.
- *"Store the conversation or dispute narrative on the shared ledger."* → PII in the commons. Anchor references only.
- *"Edit or delete a record to resolve a dispute."* → Erasure. Annotate; never erase.
- *"Make one global ledger so everything is consistent."* → Reintroduces the global authority. Per-operator logs plus witnessing.
- *"Route all checkpoints / all witnessing through our relay."* → Makes the witness a chokepoint. It relays and serves proofs; it never adjudicates.
- *"Witness only the final sealed adjudication / deliver the lifecycle as one block."* → Self-attestation wearing a hash. Witness each transition as it happens, from filing.
- *"Let the front end mint the filing record."* → Intake capture; the operator is present at its own claim's birth. File to an independent witness.
- *"Gate voting on an operator's average rating / show a single operator score."* → Rebuilds the average, and reads verdict-dissatisfaction as misconduct. Read conduct *structure* — dwell, dismissal patterns — not a rating count.
- *"Auto-remove an operator when the scan flags it."* → Makes the scanner the authority the witness model forbids. The scan flags; adjudication decides; the operator contests.
- *"Just run it all on our one server or cloud account for now."* → Hosting chokepoint.
- *"Let a vendor pay to rank higher / have the network certify which claim is true."* → Buys reputation / installs a truth authority. (See Part VI.)
- *"Write the plain-English explainer as a separate doc / document it after launch."* → A second source of truth, born drifting. Legibility is generated from, or conformance-bound to, the artifact it explains — or it is marketing. (See the legibility ladder.)
- *"Let themes run scripts / load remote assets."* → Self-XSS and beaconing. Presentation-sovereignty requirements one and two; refuse.
- *"Ship a starter theme that tidies away the harm distribution."* → System-authored occlusion. Presentation-sovereignty requirement five; refuse.

A quick test: if a change makes a layer harder to leave, makes the record easier to rewrite, makes credit convertible to or purchasable with fiat, makes some center the arbiter of value or truth, or lets an operator's own attestation stand in for an independent witness — it is almost certainly off-architecture. Flag it.

---

## Part IV — the signal architecture

A builder needs more than the invariants; they need to know how the signals *move* — what is recorded, where it seals, to whom, and what a reader may infer. This part traces that flow, and it is settled demand; Part V is the still-open governance use of it.

**The dialog and its typed signals.** The dialog is the atomic unit and seals on complete-and-quiescent. An exchange emits the covenant's ratings between counterparties; when a dispute arises, it also emits an adjudication lifecycle. These are **typed** — trade, adjudication-conduct, verdict-satisfaction — because they mean different things and occur at different rates, and a reader that blurs them has rebuilt the average across relations.

**The claim lifecycle as a pipeline: file → adjudicate → resolve → seal.** Each transition seals to the witnessed record as it happens, and the *routing differs by transition*. Filing goes to an **independent witness, upstream, with the operator absent** — so intake cannot be shaped or shed before the claim exists. Adjudication and resolution are the **operator's conduct**, sealed and witnessed as the operator performs them. The final seal closes the dialog **only when the harm is actually answered** — a clock never force-seals it. An unanswered claim stays open, visible, and its **dwell** — age past a movable threshold, 90 days as the current default, possibly per-dispute-type — is a readable fact, not a verdict.

**The three streams, and why typing is load-bearing.** *Trade harm* is economic, incident-level, low base rate — the pipes mostly work. *Adjudication conduct* is the operator doing or failing its adjudicator job — dwell, dismissal patterns, non-response — and it is the governance-relevant stream, because it is where an operator can abuse the very users it also gates for voting. *Verdict-satisfaction* is a party rating a judgment: unsuppressable (the operator cannot stop it), and therefore honest — but a lowest-level rating here is a losing party's displeasure, **not** operator misconduct. The governance-relevant signal is adjudication *conduct* read as structure, plus the unsuppressable user-controlled streams; it is never a raw operator rating average.

**What a reader may and may not infer — the scan.** A scan reads *structure* off the witnessed lifecycle, and three signatures matter. Aged-open **dwell distributions**: the shape, not a count and not an open/closed ratio — both of those invert, punishing the busy honest operator and rewarding the fast trivial-close. **Dismissal and fast-close patterns**, visible because the record annotates and never erases: the sweep-it-closed evasion complements the sit-on-it evasion — sit and you trip dwell, sweep and you trip the dismissal pattern; together they bind. And the **too-clean signature**: a closed, all-good, low-external-value subgraph is the wash-trade tell, and the thing to flag, not wave through. The output is a **contestable flag, never an automatic exclusion** — a dial that raises the cost of gaming, not a wall. False positives land on unusual-but-honest communities, so a flag is an input to human contestation, not a verdict.

**Honest only over a witnessed record.** Every signal above reads true only with **two or more independent witnesses.** On a single backend the operator attests its own lifecycle — dwell, dismissals, and all — and the read is self-reported: the fox counting hens. The signal architecture is specified now; it *runs honestly* only once the witness layer (open problem 2) is real for the lifecycle. That dependency is the bridge to Part V and the reason problem 4 now rests on problem 2.

---

## Part V — governing the core (an exploration)

This part is written as exploration and held to every invariant above. It works one answer to the hardest open problem, and it is *not mandated for every implementation* — an aligned instance may govern its core differently. The architecture keeps the *mechanism* reversible even where an instance has committed to it in its own governance instrument. The signal *plumbing* it relies on (Parts III–IV) is settled.

**The problem.** Open problem 4: the governed are not the governing, because membership was purchased. Onboarding is open-signup plus zero-cost verification — email as username, TOTP or passkeys as the factor, never SMS (a purchase wall, a surveillance vector, and a weak root). But free-to-join under one member, one vote is the *maximal* Sybil hole **if joining conveys a vote.** So the first move is to **decouple membership from governance weight:** everyone joins free; a vote is gated separately, by something that is neither a purchase nor a global identity authority — the two things the architecture refuses.

**The candidate: operator-federation.** The electorate is corroborated-active **operators**, not individual users — but the vote stays **one person, one vote:** operator-status *qualifies* a person to vote, it does not multiply anyone's vote. This pushes governance out of the zero-cost quadrant without a toll or an oracle: at the operator layer the population is small and expensive to make real, so **cross-operator corroboration** bites where it never could over cheap-to-bot users. Corroboration is the qualifier; user ratings never are (inflatable), and an operator's own attestation never is.

**The disqualifier, and how it reads.** One **adjudicated harm from a genuine counterparty** can cost an operator its vote — never an average, per the Leveson posture. But the operator-harm signal is *not* "users rated the operator badly" (mostly verdict-dissatisfaction). It is **adjudication conduct** read as structure from the witnessed lifecycle (Part IV). The evidence is clean and structural; the *verdict* on whether it disqualifies is a contested, cross-corroborated federation decision — anchor-the-claim, don't-certify, applied to operators. What counts as operator harm is **culturally interpreted**, not centrally codified: the assessment scale is domain-general, a user interprets it in context, and the federation adjudicates the claim rather than consulting a taxonomy. This is **vertical** review — an operator's conduct on its own platform read *up* to the governance that governs it — and is therefore not horizontal reputation portability (open problem 5).

**Users are non-mute.** A user cannot cast a core vote, but can **cost an operator its eligibility** through a real adjudicated harm, and governs its own operator by exit and recall. Voice reaches users through the one channel Sybil cannot corrupt — accountability — not the ballot. That asymmetry is exactly what lets users stay off the ballot, since every per-user metric is Sybil food, without silencing them.

**The review venue.** An audit authority — the governance layer's steward office, per the layer-aligned stewardship in Part III — may **investigate and convene**: surface anomalies, read structure, raise cases. It is **not dispositive:** the disposition is made by the contested, cross-corroborated federation, with the operator answering. The **open-objection channel is co-equal at the raising stage**, not a supplement — so agenda control is not concentrated in the audit role either.

**The multi-account residual.** One-person-one-vote dissolves the many-operators-one-person Sybil — a single party running ten operators still casts one vote. The residual is **multi-account** Sybil: one human holding several member-accounts, each qualified through an operator. In an interim it is gated by a real recurring cost per account and by application review; in the target it is gated by corroboration that **excludes non-independent operators** — same-controller operators are not independent corroborators, and the operator-collusion scan (structural, contestable) is what catches them. That scan stays load-bearing; one-person-one-vote caps the multiplier but does not by itself stop multi-account minting.

**The interim-steward pattern.** An instance bootstraps under a founding steward with a ratified governance instrument — typically dues-gated membership and a proprietary governance venue. Both are conformant **only as named interims on a committed path:** the steward's founding body becomes the **genesis operator set** as the layers come online (the bootstrap trust root, before corroboration's guarantees bind — the governing body becomes the operator-federation rather than being replaced by it, no flag day), and the proprietary venue is exited for sovereign coordination substrate that makes the witnessed record readable for the operator-conduct read. Conformance here is **conditional, not permanent**: if the transition stalls, each interim reverts to a standing violation. And the end-state requires a deliberate amendment of the governance instrument — the purchase qualifier must be *sunset* by the membership, on its own timing. The two qualifiers can coexist during the transition: operator membership may be adopted immediately, with staged recognition, alongside the interim purchase gate, so adopting the mechanism need not wait for the sunset. Only the sunset is deferred.

**Settled, designed, committed, and open — stated honestly.** *Settled as demands* (Parts III–IV): the signal plumbing — lifecycle witnessing, filing placement, typing, structure-not-average, flag-not-verdict. *Substantially designed:* corroboration-qualifier, conduct-disqualifier, non-dispositive audit with co-equal objection. *Committed per instance, in its own instrument:* adoption of operator-membership as the governing requirement — now drafted in one instance's instrument, with immediate adoption under staged recognition rather than a deferred end-state — which accepts a real **enfranchisement tradeoff**: the crisis-entrant's leverage on the core is real but *mediated and slow*, through their operator's eligibility and through recall, not a ballot. *Still open:* the operator-majority hole in corroboration (the genesis set is now specified per instance — the founding steward's standing representatives — but its concentration before corroboration binds is real); **multi-account** Sybil; the **cold-start window** for new operators; the false-positive tax on unusual communities; and problem 8 below.

**The dependency.** This entire read requires the witnessed lifecycle to be real (two or more independent witnesses). Operator-federation cannot run honestly on a single backend. **Problem 4's resolution now depends on problem 2's build** — they are no longer independent problems.

---

## Part VI — the Economy & Information layer (an exploration)

Held to every invariant above; built as the smallest conformant experiment, cheaply reversible.

**Why economy and information are one layer.** The economy layer applies the four layers below to a specific socioeconomic activity. Building economies surfaced a fact: a front end is already a site of information exchange. Members describe what they produce, teach each other, compare tools, and vouch for what worked, before any credit moves.

**What the structure must support.** This document regulates structure, not economies, so it describes application shapes only to illustrate how the layers below constrain them. Two shapes illustrate the layer's invariants in force:

- **A reintegration-support economy** — connecting caseworkers, people reintegrating into community, and citizen helpers. It adapts the assessment scale **bidirectionally**, is offline-first for entry-level devices, and puts dignity and exit ahead of oversight — the layer's invariants applied to a low-resource population, and the sharpest case for open problem 8.
- **A high-stakes care economy** — a matching-and-trust marketplace on the **full assessment distribution**, with a prevention-first safety layer that *takes precedence over every other rule*: verification and screening before reputation applies, and a harm report runs a safety track independent of the reputation track. It shows that a high-stakes economy may run a track that overrides the covenant — the precedent for treating governance eligibility likewise.

A witnessed record can anchor not only an exchange claim but any **empirical or commercial claim** — *this cultivar yielded this under this method; this course teaches this; this tool failed this way.* Anchored, a claim becomes **citable**, and the covenant can rate the *claimant* the same way it rates a trading partner — and its lifecycle witnesses the same way an adjudication's does (Part IV). The same rails that make trade trustworthy make knowledge trustworthy.

**The invariants this layer inherits — and the new ones it needs.** Everything above binds. Beyond them:

- **No truth authority.** The commons anchors and weighs claims; it never adjudicates fact. A "verified true" flag from any center is off-architecture.
- **Citation is legible and forkable.** A claim, its references, and their weight ship legible enough to re-derive and to fork.
- **Reputation is earned, never sold.** No paid placement, no bought rating.
- **Claims are anchored as claims, not asserted as fact.** Anchor the inputs and outputs, not a verdict.
- **Sybil-resistance precedes citation-weight.** Settle problem 4 before citation count or reputation sizes any real reward — exactly as it must be settled before credit turns on.

**What it must not become.** A rating agency for truth. An ad market where visibility is bought. A credentialing monopoly. Keep discovery **federated, cited, and contestable.**

---

## Part VII — the open problems

For each: the problem, the constraints any fix inherits, what to watch for, and where it stands. This stack is fed from below: every project ships its own living open-questions document (Part III, Governance), a question discovered locally that binds architecturally is promoted here rather than kept local, and the network stack and the project documents cite each other in both directions.

**1. Equivocation is detectable, not prevented.** Witnessing proves a lying operator showed two histories; it does not stop the lie, and detection is only as strong as a verifier's reach to independent witnesses. *A fix must not* introduce a larger authority at the core. *Status:* a permanent property, managed, never "solved." The detection machinery — operator-signed monotonic checkpoints, consistency proofs, and the checkpoint pair as portable fork evidence — is now implemented in the built record instances; the property itself is unchanged.

**2. The witness layer — the core is built; federation is not yet the default.** The witnessed-record core is now implemented in the built record instances: per-operator hash-chained logs, operator-signed monotonic checkpoints, retrospective witness countersignatures with structural independence verification (pairwise-distinct witness keys, none the operator's), inclusion and consistency proofs, and a structural **stand-in label** whenever fewer than two independent witnesses have countersigned — a single-witness deployment cannot present itself as federation. Federation is structurally cheap by design: an independent witness joins by appending a countersignature, with no protocol change.

What remains: the **witness relay** role; **federated deployment in fact** — two or more independent, long-lived witnesses, with witness state durability a named residual (a restarted witness reverts to trust-on-first-checkpoint); **lifecycle witnessing** of the claim pipeline — filing (at an independent witness, upstream of the operator), adjudication, resolution, and seal, each a monotonic independently-witnessed transition; and the anchoring of substrate work claims, reserved as a labeled stub inheriting the record's invariants. *This remains the single highest-leverage build and the prerequisite for honest operator-conduct evidence:* problem 4's governance read runs on labeled stand-ins until federation is real.

The sovereign governance venue is the interface that will make the witnessed record readable for the governance read — a legibility tool that **confers no authority**: it serves the read, it never decides the verdict. That venue now exists in seed form — a founding specification, a first feasibility read, and a portable file-structure seed of the venue's channel structure — while the proprietary interim venue stands; the exit is committed, not yet performed. *Status:* core built, running on labeled single-witness stand-ins; relay, lifecycle witnessing, live federation, and the venue exit open.

**3. Mutual credit — the switch is real; the walls are codified; the read is not done.** The escrow-now / credit-later policy switch is a single governed configuration change, and the walls are now codified as binding governance requirements in an instance's instrument — Board approval, membership notice, and a completed regulatory review before any issuance; earned-never-bought and the covenant-gate/limit separation stated as rules. What is not settled: the regulatory read itself, and Sybil-resistance. *Status:* switch real; walls codified; the read and Sybil-first still pending.

**4. The governed are not the governing at the core; membership was purchased.** Open-signup plus zero-cost verification **narrows but does not close** the gap. The direction (Part V) is **operator-federation**, which relocates Sybil from "distinct human" to "corroborated-active operator" — purchase-free and authority-free — and decouples membership from vote-weight. *A fix must not* make the core a no-exit chokepoint or require a global identity authority.

*Status:* **substantially narrowed — the political half is drafted; the evidentiary half still waits on problem 2.** An instance's draft instrument (pending its membership's adoption) now does what this problem demanded of institutions. Membership is free to all; verification is zero-cost (no purchase, no telephone-number root); and **operator membership is adopted immediately** as a free, franchise-carrying qualification held under a conduct standard — gaming, tampering, harmful environments — with structure-not-average evidence discipline, flag-never-finding, co-equal raising channels, and due process. Recognition is staged: steward-recognized from a genesis operator set (the founding standing representatives, who become the first operator members) until the witnessed record is real, then cross-operator corroboration excluding common-control operators. The federation now has a drafted *body*, not only a drafted franchise: the same instrument constitutes standing, layer-aligned federation circles — one per layer of the stack, mirroring the stewardship alignment — whose membership requires the operator qualification in good standing, whose deliberation stays open to members of every class (circles stay open; users stay non-mute; a countering observation can reopen a decided matter), and whose binding votes inherit one-person-one-vote and the staged recognition of the bootstrap. Loss of the operator franchise ends federation membership without expelling the person from the commons. The purchase qualifier is retained only as the named interim Sybil gate alongside, with a committed sunset by membership amendment and quarterly public reporting of the transition's status. One-person-one-vote is preserved throughout; operator status is a qualifier, never a multiplier.

What remains: the instrument's adoption; honest conduct evidence (**depends on problem 2** — until federation is real, dispositions must name their evidence as self-attested); multi-account Sybil in the interim; the operator-majority hole in corroboration; the cold-start window; the false-positive tax. Narrowed, not closed.

**5. Reputation portability across platforms is undecided.** An operator's conduct read *up* to the governance that governs it is **vertical** and is *not* this problem. **Horizontal** portability — the same human's standing reused across platforms as a following score — remains undecided; the covenant ships non-portable by default. *A fix must* need only a portable identity and the ability to read another platform's witnessed log — never a shared money supply or a bridge. *Status:* deliberately undecided.

**6. Computation and claim honesty is out of scope.** Whether an operator's match, price, yield, or finding was fair or true is unverified, checked only by legibility and exit. *A fix must not* require trusting a central verifier. *Watch for:* maximize legibility; anchor inputs and outputs where no PII leaks, so claims are auditable even if not proven. *Status:* open in general — but the substrate has begun anchoring specific claim families: storage-possession audits are implemented at the protocol layer (with a labeled finite-challenge stand-in), and the anchoring of work claims — job in, result out, meter — is reserved as a labeled stub inheriting the record's invariants, so a coordinator that equivocates about completed work becomes provable rather than merely distrusted. The discipline holds: anchor inputs and outputs; never certify. Still the theoretical home of the information layer's discipline.

**7. Sovereign compute buys mechanical, not social or economic, exit.** The mechanical right to host does not deliver the economic capacity to; coordinator fees and reputation cold-start recentralize. The economic floor on hosting has become an economic floor on **governing** — see problem 8. *A fix must not* concentrate the coordinator further. *Status:* open — but the mechanical exit is now concrete rather than promised: the coordination protocol is published, versioned, and consumed by two independent implementations, so reimplementation is a demonstrated path, and fee declarations are coordinator-authored and legible (contestable). The economic half is unchanged: cold-start remains fragile, and it still couples to governance.

**8. The witness layer has a cost floor, and the floor excludes.** The two-or-more-independent-witness guarantee, multiplied by per-transition lifecycle witnessing and the filing-liveness requirement, raises the resource floor — compute, connectivity, uptime — to participate as an *honestly-witnessed* operator. That floor prices out the low-resource operator, who is disproportionately the one serving the crisis-entrant: the offline-first, entry-level-device economy is asked to carry the heaviest witness overhead in the stack. And filing-at-an-independent-witness means a harmed user on a node with no reachable witness **cannot lodge a harm** — the same exclusion wearing a second hat. *This is not a new Sybil problem; it is problem 7 (mechanical-not-economic exit) surfacing at the witness layer with a governance consequence — problems 7 and 4 coupling.*

*A fix must not* concentrate witness-provision in the steward or a few large operators — that recentralizes the thing federation exists to distribute, and rebuilds the oracle. *Watch for:* separating **witnessing from operating** — let a broad, independent membership witness a poor operator's lifecycle, so a node can be *governed-honest* without being *witness-rich*. Membership-as-witnessing is the most architecture-shaped lever, since it distributes witness capacity across members rather than concentrating it; watch the filing-liveness gap on offline-first nodes specifically. *Status:* open — with one precondition landed: in the built record instances, witness federation is structurally cheap (an independent witness joins by appending a countersignature, no protocol change), which is exactly the seam membership-as-witnessing needs. The cost floor itself — long-lived witness state, connectivity, uptime — and the filing-liveness gap remain unsolved.

**The convergence.** Problems 2, 4, 7, and 8 meet at one surface: the witness layer. Record-integrity (2), governance-legitimacy (4), and substrate-economics (7, 8) are jointly decided there — which is why the same build keeps reappearing from different sides of this design. The witness layer is the load-bearing surface of the architecture; whatever you build there settles more than it looks like it settles. This is a statement about how the problems *relate*, not a claim that any is solved.

---

## The standard

Gathered, the layer disciplines are the cornerstone. A system is conformant to Janus-Facing Architecture only if all seven hold; a system that fails one is not a smaller version of this architecture — it is different software wearing its vocabulary.

1. **Mutual credit, not banking.** It is, or governs, a member-issued mutual credit economy, gated by covenant and capped by a separate limit; its currency is sovereign, separate, denominated-not-backed, non-convertible across platforms, never redeemable for fiat; and credit is earned, never bought, entering only behind a value-prop strong enough to pull migration.
2. **Sovereign substrate.** It runs, or can run, on infrastructure its participants can own — no unremovable hosting chokepoint.
3. **Witnessed, legible record.** Its record is immutable, tamper-evident, witnessed against equivocation — including the claim lifecycle, from filing — and PII-free in the commons; harm can be forgiven but never hidden.
4. **Reputation as covenant.** Its reputation is a covenant, not a score — a full distribution that never averages, contestable in both directions, typed by relation, gating whether-not-how-much.
5. **Governed by the cost of leaving.** Voice where contest is cheap, exit where it is dear, standing contestation at the core — and presentation is separable, with every participant holding the right to restyle their own render.
6. **A minimal, contested, stewarded core.** The specification is kept minimal, entrenched only where legibility and portability demand it, permanently contestable, and held by a named, internally-accountable steward.
7. **Legible above all.** It is documented and interpretively accessible enough that the people it governs can read it, fork it, and leave — and its legibility is mechanized, not promised: decisions carry receipts, policy is data with witnessed versions, prose is bound to code by conformance checks, and builds are reproducible (the legibility ladder); and it ships a living open-questions document naming what remains unresolved about its future — staleness is nonconformance. A commons no one can read is a freedom no one can use.

---

## The tension protocol

While implementing, if you notice yourself doing any of the following, stop:

- reframing a constraint of this architecture so a feature becomes convenient,
- implementing a stand-in without labeling it,
- routing around one of the open problems instead of noting it.

These are the signals that the architecture is being quietly eroded. When you hit one: name the tension, attach it to the relevant invariant or open problem, and propose the minimal conformant move — the smallest change that meets the goal without breaking the standard, or the smallest experiment that bears on the open problem. Surface it; do not absorb it.

---

## The discipline this document is under

This document is held to Janus-Facing Architecture, like everything else. It is unversioned because it is the standing description of the architecture, not a release: it is amended in the open when the architecture is, and it carries no changelog theater. It is product-agnostic because the architecture is the thing that persists while implementations are built, forked, and left — an implementation binds to a role here, and no role here depends on any implementation surviving. And it does **not mandate** the operator-federation *mechanism* for every implementation: an aligned instance may govern its core differently, and the mechanism stays reversible in the architecture even where an instance has committed to it.

Two honesties are load-bearing and must not be smoothed. An instance's purchased membership and proprietary governance venue are conformant **only as named interims on a committed path**, never relaxed into permanence. And the operator-federation **end-state requires a deliberate amendment of the instance's governance instrument**, timed by its membership. The plumbing is a demand on all; the political choice binds per instance, in its own instrument; the interim is conformant only while the exit stays committed.

Build to the invariants, keep the open decisions cheaply reversible, surface what you find, and leave the values calls to the people who have to live with them.

> *"When the work is done and their aim fulfilled, the people will say, 'We did it ourselves.'"* — Tao Te Ching, 17

---

## References

- Acemoglu, D., & Robinson, J. A. (2019). *The Narrow Corridor: States, Societies, and the Fate of Liberty*. Penguin Press.
- Downs, A. (1957). *An Economic Theory of Democracy*. Harper & Row.
- FAO, IFAD, UNICEF, WFP, & WHO. (2024). *The State of Food Security and Nutrition in the World 2024*. FAO.
- Freeman, J. (1972–73). "The Tyranny of Structurelessness." *Berkeley Journal of Sociology*.
- Graeber, D. (2011). *Debt: The First 5,000 Years*. Melville House.
- Greco, T. H. (2009). *The End of Money and the Future of Civilization*. Chelsea Green.
- Hirschman, A. O. (1970). *Exit, Voice, and Loyalty: Responses to Decline in Firms, Organizations, and States*. Harvard University Press.
- Laurie, B., Langley, A., & Kasper, E. (2013). *Certificate Transparency*. RFC 6962, IETF.
- Leveson, N. G. (2011). *Engineering a Safer World: Systems Thinking Applied to Safety*. MIT Press.
- Leveson, N. G. (2020). *CAST Handbook: How to Learn More from Incidents and Accidents*. MIT.
- Mead, G. H. (1934). *Mind, Self, and Society*. University of Chicago Press.
- Michels, R. (1911). *Political Parties: A Sociological Study of the Oligarchical Tendencies of Modern Democracy*.
- Ostrom, E. (1990). *Governing the Commons: The Evolution of Institutions for Collective Action*. Cambridge University Press.
- Ruesch, J., & Bateson, G. (1951). *Communication: The Social Matrix of Psychiatry*. W. W. Norton & Company.
- Scholz, T., & Schneider, N. (Eds.). (2016). *Ours to Hack and to Own*. OR Books.
- Sen, A. (1981). *Poverty and Famines: An Essay on Entitlement and Deprivation*. Oxford University Press.
- Stodder, J. (2009). "Complementary Credit Networks and Macroeconomic Stability: Switzerland's Wirtschaftsring." *Journal of Economic Behavior & Organization*.
- UNEP. (2024). *Food Waste Index Report 2024: Think, Eat, Save*. United Nations Environment Programme.
- U.S. Department of Housing and Urban Development. (2024). *The 2024 Annual Homeless Assessment Report (AHAR) to Congress, Part 1*.
- Watzlawick, P., Bavelas, J. B., & Jackson, D. D. (1967). *Pragmatics of Human Communication*. W. W. Norton & Company.

---

*Network Theory Applied Research Institute, Inc. — 501(c)(3) — EIN 92-3047136 — info@ntari.org*

*This document is free documentation under the project's AGPL-3.0 commons; it is meant to be read, reimplemented, and contested.*
