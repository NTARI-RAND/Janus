# JFA Amendment 003 — Version Control by Layer; the Anarchy of Production; Where Engineering Standards Live

*Amends the standing description ([janus-facing-architecture.md](janus-facing-architecture.md), unversioned) — drafted against its text as of 2026-07-29. Standing amendment until merged in the open, then retained as record. Amendments One and Three document practice and propose conformance deltas; Amendment Two is an exploration in the manner of Parts V–VI and mandates nothing, but it promotes one question to Part VII.*

**Network Theory Applied Research Institute** · Version 1.0 · 2026-07-31

---

## Why this amendment exists

Amendments 001 and 002 each brought a piece of steward practice into the architecture: presentation sovereignty, then broadcast, preservation, and multilingual legibility. Both entered as *observations about what the steward was already doing*. That is the honest way to amend, and it has a cost: mechanisms arrive one at a time, attached to whichever layer noticed them, without anyone asking what kind of thing they are.

Two such mechanisms are now load-bearing and unplaced. **Version control** runs the canon of every project and enforces provenance at the merge, yet appears in the architecture only as three words in the Governance row — *provenance discipline* — and as steward practice in Amendment 001. **Custom UI per user, non-broadcast** entered as five Substrate invariants, `SUB-5` through `SUB-9`, in a subsection that opens by warning against exactly that: *lest the minimal core grow a contested product feature*. More engineering specifications are in preparation. Before they arrive, the architecture should say where such things go.

The organizing claim of this amendment, stated plainly: **version control is not one mechanism. It is two, at two different layers, and conflating them is what has kept it unplaced.**

---

## Amendment One — version control belongs to two layers, not one

**The claim.** The steward's version control and the network's version control are different mechanisms that happen to use the same tool. Distinguish them by what they hold:

- **Governance version control** holds decisions — bylaws, policies, the architecture itself, the operational record. It is **downstream of the Governance layer**: the decision is made in the governance venue, and version control is how the decision becomes legible, diffable, and un-rewritable afterward. It records; it does not decide. NTARI is the 501(c)(3) governance layer, and its repositories are that layer's memory.
- **Production version control** holds the work — protocol, coordinator, front ends, seeds, specifications-in-progress. It is **not** governance at all. It is the **anarchy of production**: many hands building in parallel, no planner assigning the work, ordered — insofar as it is ordered — from below rather than above.

The same `git` binary serves both. The postures are opposite. Governance version control wants *finality with an audit trail*: what was decided, when, by whom, and what the text said at the moment it bound. Production version control wants *fork-freedom and cheap divergence*: many branches, many implementations, and no requirement that anyone agree.

**Why this is a conformance matter and not a filing convention.** The architecture already assigns these two things to different layers, and assigning them to different layers means they inherit different disciplines. Governance version control inherits the Record layer's posture through the legibility ladder — rung 3, *policy versions commit to the witnessed record*, and rung 2, *rules live as data, diffable by anyone*. Production version control inherits the Substrate and Governance postures — `SUB-1`'s no-hosting-chokepoint, `GOV-10`'s inbound = outbound provenance, and Amendment 001's fork-capacity duty. Collapse the two and you get the failure in both directions: production repositories governed as though every merge were a constitutional act, and governance documents held as though a diff were a decision.

**What happened, as record — and the finding it produces.** In July 2026 the steward built out production version control to a high standard: fourteen repositories mirrored to five platforms across four continents with verified head parity, Developer Certificate of Origin enforced as a merge-blocking check on every default branch, Software Heritage and Internet Archive holding both a source snapshot and a restorable full-history bundle, quarterly releases scheduled, and — on 2026-07-31 — a heartbeat that walks the English root to its seven contextual renderings to the mirror cast state and records each beat in one ledger. The licence-compliance fix of 2026-07-30 was itself forced through the pull-request path by the rulesets, which is the first live proof that the provenance floor holds against the steward.

Set beside that, the finding: **the steward's governance canon is not under version control at all.** `Bylaws/`, `Governance/`, `Operations/`, `JFA/`, and `Curriculum/` are plain files on one machine — no history, no diff, no signed authorship, no mirror, no archive. The layer whose entire product is decisions keeps no record of how its decisions changed; the layer whose product is code keeps five copies in four jurisdictions and three archival systems.

This is precisely inverted, and the architecture's own text says why it matters. Rung 3 requires that policy versions commit to the witnessed record so that *"what rule was in force when my dialog sealed?"* has an answer. Right now the steward cannot answer the governance equivalent — *what did the policy say on the day the directive was issued?* — from anything but memory and file timestamps. Amendment 002 recorded two Presidential directives standing as named interims pending Board ratification; a named interim is only conformant while it is *visible and progressing*, and visibility over time is exactly what an unversioned document tree cannot supply.

The gap is not that the governance tree lacks a fashionable tool. It is that `GOV-4`'s entrenchment, `GOV-5`'s recall, and `GOV-6`'s standing contestation all presuppose that the text being entrenched, recalled against, or contested is a **fixed, citable thing**. Without version control there is no such object — only the current file.

**Conformance delta (proposed).** The legibility ladder's rung 3 gains a sentence making its scope explicit: *this rung binds the steward's own governance canon as well as the network's runtime policy — bylaws, policies, and this architecture are policy versions in the sense meant here, and an unversioned governance corpus fails rung 3 however carefully it is written.*

And `GOV-8` (*legibility is an output, not a comment*) gains a clause: *…including the governance canon's own change history; a decision that cannot be cited as it stood on a given date is not legible, whatever its prose.*

**What this does not require.** Not that governance documents move to a public forge, not that a mirror network be replicated for them, not any particular tool. The duty is a citable history under the steward's control. How it is discharged is policy — diffable, per Amendment 001's own reasoning, and deliberately left to the steward.

---

## Amendment Two — the anarchy of production, and what actually orders it (an exploration)

*Held to every invariant; mandates nothing. It promotes one question to Part VII.*

**The proposition under examination.** The repositories are the anarchy of production, and what orders them is the invisible hand of the Covenant layer.

Both halves are borrowed, and both borrowings are load-bearing, so take them literally before accepting them. *Anarchy of production* is Marx and Engels' term for production distributed across many independent producers with no plan coordinating them — used as a diagnosis, of a system that periodically wrecks itself for want of coordination. *Invisible hand* is Smith's: the claim that self-interested producers, without intending it, are led to serve the general interest — and in Smith the leading is done by **prices**. The producer sees a price, infers where demand is unmet, and moves. The signal is scalar, public, and comparative.

**The first half holds exactly.** The canon is produced the way the term describes: many repositories, no assignment of work, no planner, contributions arriving from whoever shows up. And here the anarchy is a *feature*, not the pathology Engels described, because the architecture has deliberately removed the thing that made it pathological — the coordination failure is priced in the market case by unsold goods and unemployment, whereas a commons that produces the wrong thing wastes only the effort of the people who chose to spend it. Nobody is starved by a fork that goes nowhere. Production anarchy is the correct posture for this layer and needs no defence.

**The second half does not hold as stated, and the reason is a conformance rule.** For the covenant to function as an invisible hand it would have to be a price: a scalar, comparative signal a producer can read to decide where to direct effort. The architecture forbids the covenant from being that, twice over and on purpose. `COV-1` forbids averaging reputation into a score — the distribution is carried whole precisely so it cannot be compared as one figure. `COV-4` restricts reputation to gating **whether** a member transacts on trust, never **how much**. A signal that may not be scalarized and may not size anything cannot allocate. That is not an oversight to be patched; it is the barrier between the covenant and a credit score, and Part III says so directly — *let the two merge and the harm distribution quietly becomes a credit score, and the bank returns through the back door.*

So the honest formulation is narrower and, I think, more interesting than the metaphor:

> **The covenant is a negative coordinator.** It orders the anarchy of production by *exclusion*, not by *allocation*. It makes harm expensive and dishonesty unprofitable, and it does so without anyone deciding who may build what. What it cannot do — by design, not by omission — is make useful work attractive, or tell a producer where effort is most needed.

This is the invisible hand's *filter* without its *pump*. Smith's hand does two jobs: it weeds out the bad and it directs the good. The covenant does the first job well and does not attempt the second.

**Then what is directing the good?** Naming the answer honestly is the point of the exploration. Four mechanisms currently do allocation work in the canon, and only the first two are architectural:

1. **Exit** — a front end nobody uses is abandoned; a protocol nobody implements dies. This is real, and it is the architecture's own answer wherever leaving is cheap. It is also slow and posterior: it tells you what was wrong, not what to do.
2. **The open-questions document** (`GOV-9`) — the closest thing the architecture has to a demand signal. Each project is required to publish what remains unresolved about its future. That is a public list of where effort would be well spent, produced without a planner and citable across projects. `GOV-9` was written as an anti-drift mechanism, but it doubles as the commons' want-ads, and that second function has never been named.
3. **The conformance suite** — orders production by constraint rather than direction: it says which work is admissible, not which is wanted.
4. **The steward's attention** — which today does most of the real allocating, and is the one mechanism the architecture would not endorse if it were stated out loud. A named steward deciding what gets built is a planner, and the fact that it is currently the honest description of how the canon gets written is exactly the kind of thing the tension protocol exists to surface rather than absorb.

**The tension, named.** Per the tension protocol: the proposition as stated reframes a constraint — treating the covenant as an allocative signal when `COV-1` and `COV-4` forbid it — in a way that would make a hard problem look solved. The minimal conformant move is to keep the negative coordinator (which is true, useful, and already built) and to name the allocation gap as an open problem rather than let the metaphor cover it.

**Promoted to Part VII, as `GOV-9`'s own promotion rule requires** — *a question discovered locally that binds architecturally is promoted to Part VII, not kept local*:

> **Open problem — production allocation without a planner.** The covenant excludes but does not allocate; exit is posterior; the steward's attention is a planner in all but name. What signal tells a contributor where effort is most needed, without becoming a price (forbidden at the covenant, `COV-1`/`COV-4`), a reputation multiplier (forbidden, `GOV-7`), or an office that assigns work (forbidden, `GOV-2`/`GOV-3` — stewardship is answerability, not authority)? Candidate direction, unproven: the open-questions corpus read across the whole canon as an aggregated, un-ranked demand surface — visible to all, ordered by no one, carrying no reward. Whether an un-ranked signal can allocate at all is the open part.

This problem belongs on the list beside the others; it is not a reason to change anything now.

**One thing the exploration settles.** Governance version control being downstream and production version control being covenant-disciplined are *the same claim seen from two sides*: the steward records what it decided, and does not decide what gets built. The gap named above is the price of that restraint, and it is the right price. An architecture that solved allocation by appointing an allocator would have rebuilt the planner it removed.

---

## Amendment Three — where engineering standards live

**The problem, concretely.** Presentation sovereignty is right, and the way it entered is a warning. Its subsection opens by saying the pattern is *recommended, not mandated, lest the minimal core grow a contested product feature* — and then adds five invariants, `SUB-5` through `SUB-9`, specifying import-time behaviour for pasted CSS. Those five rules are correct. They are also, in kind, an implementation specification for one class of front-end feature, sitting in the same register as *the coordination protocol is a dependency leaf*.

That is core growth, and `GOV-1` is explicit about the cost: *keep the core minimal — it guarantees only the portabilities that keep every layer above it leaveable, so capturing it pays little.* Every invariant added enlarges the prize. With further engineering specifications in preparation, the question is no longer hypothetical: an architecture with no tier between *invariant* and *nothing* will keep absorbing engineering detail into its constitution, one well-argued subsection at a time.

**The proposal: a named tier.** Introduce **engineering standards** as a class of binding requirement that is explicitly *not* part of the minimal core.

| | Invariant | Engineering standard | Policy |
|---|---|---|---|
| **Answers** | what a role *is* | how a role is *built* | what a steward *does* |
| **Lives in** | this document, Part III | a standard bound to a named invariant | steward policy documents |
| **Changing it** | amendment in the open | the layer's officer, recorded, contestable | ordinary policy process |
| **Entrenched?** | the deepest few, by double lock | never | never |
| **Failing it** | not this architecture | nonconformant implementation | a policy breach |
| **Must cite** | — | the invariant it serves | — |

Three rules keep the tier from becoming a loophole. **An engineering standard MUST cite the invariant it serves**; one that serves no invariant is a product opinion and belongs nowhere in the canon. **It binds implementations in the canon and is checkable by the conformance suite** — this is not a softer word for "suggestion"; failing one is nonconformance, it simply is not a failure of *the architecture*. And **it is never entrenched** — the double lock of `GOV-4` covers open source, privacy, and no-surveillance-economics, and adding engineering detail behind that lock is over-entrenchment, which `GOV-4` already names as making the core less contestable rather than safer.

The distinguishing test, for use in review: *if a conformant implementation could reasonably do this differently and still satisfy the invariant, it is an engineering standard.* Two independent front ends can sanitize pasted themes by different means and both honour the right to restyle. No two implementations can disagree about whether the protocol is a dependency leaf.

**Applying it to what is already here.** Three reclassifications follow immediately, and each shrinks the contested prize without weakening anything:

- **`SUB-5` through `SUB-9` become engineering standards bound to standard #5's presentation clause.** The *right* to restyle one's own render is invariant and stays exactly where it is. Script-blocking, remote-fetch stripping, an un-occludable reset, plain exportable artifacts, and the shipped-theme carve-out are how a conformant front end delivers that right safely — they remain binding and suite-checked, and Substrate drops from nine invariants to four.
- **Provenance enforcement mechanics become an engineering standard bound to `GOV-10`.** That inbound = outbound and that the covenant never suspends are invariant. That the check is a Developer Certificate of Origin sign-off enforced by a merge-blocking ruleset is how this steward discharges it — correct, but not constitutional, and a downstream community using a different mechanism has not left the architecture.
- **Translation provenance becomes an engineering standard bound to Amendment 002's legibility clause.** That a translation is a render bound to the normative text and never a second source of truth is the architectural claim. That each generated file carries a header naming its English source, that source's commit, and its review status — the P2-002 §2.3 community tier made mechanical — is the standard that makes the claim checkable rather than asserted.

**The version-control postures follow the same route.** Amendment 001 already reached this conclusion for mirror topology without having a name for it: *what binds is the duty; how it is discharged stays diffable policy.* Amendment One above adds a governance-canon duty; the mechanics — which forge, which cadence, what the heartbeat measures — are engineering standards and policy beneath it, never invariants. This amendment supplies the vocabulary that Amendment 001 was reaching for.

**Conformance delta (proposed).** No change to the seven-point standard. Two additions:

1. A short subsection after Part III introducing the tier, its three rules, and the distinguishing test.
2. A change to the conformance suite's registry, which is small and already almost shaped for it. `Invariant` is currently `namedtuple("Invariant", "id layer anchor binding note")`, where `binding` says *where* enforcement lives (`document` / `implementation` / `instrument`). It gains a `kind` field — `invariant` or `standard` — and a `serves` field naming the invariant a standard is bound to. **A standard with an empty `serves` fails registration**, which is the mechanism that keeps the tier honest without anyone policing it.

   Two consequences to settle when this is implemented. The suite's D5 check — *every uppercase MUST in the document maps to the registry* — must be taught that a standard's MUST maps to a standard rather than an orphan. And each registry entry carries an `anchor` phrase that MUST appear in the architecture document; reclassifying `SUB-5`–`SUB-9` therefore forces a decision about where standards' normative text lives.

   **Decided 2026-07-31: a companion register**, not a marked subsection of this document. The text moves to [jfa-engineering-standards.md](jfa-engineering-standards.md), and the suite's anchor check resolves each entry against the document named by its `kind` — invariants against the architecture, standards against the register. This is the larger of the two options and the right one: it keeps Part III readable as a constitution rather than a constitution with an appendix of import-time CSS rules, and it gives the engineering specifications now in preparation a destination that exists before they arrive. The register is drafted and takes effect on this amendment's merge; until then the `SUB-5`–`SUB-9` text stays in Part III where the suite currently anchors it, so nothing breaks in the interim.

   **Identifiers do not change.** Eleven `CONFORMANCE.md` and `OPEN-QUESTIONS.md` files across the canon already cite these IDs — `SUB-5` stays `SUB-5` wherever its text lives. A stable identifier whose whole purpose is to let a downstream repository describe itself must survive the canon being reorganized; reclassification changes the `kind` and the location, never the citation.

**Why this is worth doing before the next specification arrives, not after.** The tier costs nothing to add now and is awkward to add later: once a dozen engineering rules sit in Part III as invariants, reclassifying them looks like weakening the architecture rather than restoring it. The three reclassifications above are the moment to establish the pattern, while the count is small and the reasoning is fresh.

---

## Governance observations and open questions

- **The steward's canon needs a version-control decision, and it is a governance decision.** Amendment One establishes a duty and deliberately leaves the discharge open. The choice is genuinely open — a private repository under steward control, a public one, or a signed append-only export into the witnessed record once lifecycle witnessing exists. Each trades legibility against the fact that governance drafts contain positions before they are decisions. Worth a Board decision rather than an operator's default.
- **Bylaws are a special case within that.** `P1-001_Bylaws_v7.0_DRAFT.docx` is a binary Word file, so even under version control its history would not diff. Rung 2 wants rules as data; the bylaws are the most rules-shaped document the steward has and the least diffable. A plain-text or Markdown canonical form with the Word file as a render is the obvious move, and it is not free — the legal instrument's authoritative format is a governance question, not a formatting preference.
- **Does the production/governance split have a third case?** The architecture document itself is produced like code (drafted, amended, forked into amendments) and governs like policy. It currently lives in the governance tree. Amendment 001's reasoning about mirror-network exit capacity applies to it more strongly than to most repositories — this is the canon a downstream community would most need to fork. Whether the architecture should be broadcast on the mirror network alongside the code is open, and cheap.
- **`GOV-9`'s second function is undocumented.** Amendment Two observes that the open-questions requirement doubles as the commons' only forward-looking demand signal. If that function is real, `GOV-9` should say so — the requirement is currently written purely as anti-drift, and a project could satisfy the letter while writing questions useless to anyone deciding where to contribute.
- **The heartbeat is a rung-1 mechanism that nobody classified.** The broadcast preservation heartbeat emits, per repository per day, which link of the chain is intact and which failed. That is a decision receipt for the broadcast duty, in exactly rung 1's sense — *which rule fired, on which inputs*. If the steward's duties get receipts, the receipt format is an engineering standard bound to `LEG-1`, and it should be named as one rather than left as a script.
- **The allocation problem is now on the list.** Amendment Two's promotion should be entered in Part VII with the others and given a number in sequence. It is the first open problem in the stack that concerns the *production of the architecture* rather than the operation of a network built to it, and it may deserve a note saying so.
