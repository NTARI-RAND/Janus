# JFA Engineering Standards

**The companion register: binding requirements that say how a role is built, each bound to the invariant it serves — and deliberately outside the minimal core.**

Network Theory Applied Research Institute

*Companion to [janus-facing-architecture.md](janus-facing-architecture.md) (unversioned). Established by [Amendment 003](jfa-amendment-003-version-control-by-layer-and-engineering-standards.md), Amendment Three. **Status: draft, effective on that amendment's merge.** Until then the normative text of `SUB-5`–`SUB-9` remains in the architecture document where the conformance suite currently anchors it; this register is the destination, not yet the source.*

---

## What this document is

The architecture names *roles and mechanisms*. It does not say how to build them, and mostly should not: `GOV-1` keeps the core minimal so that capturing it pays little, and every requirement added to Part III enlarges the prize.

But some requirements are genuinely binding and genuinely about construction. A front end that accepts a pasted theme carrying a `<script>` tag has not merely made a poor product choice — it has handed an attacker the member's session while claiming to honour presentation sovereignty. That rule has to bind. It is also not constitutional: two conformant front ends can sanitize by different means and both deliver the right.

This register holds that class of requirement. **An engineering standard is binding on implementations in the canon and checkable by the conformance suite; failing one is a nonconformant implementation. It is not part of the minimal core, and failing one is not a failure of the architecture.**

### The distinguishing test

> *If a conformant implementation could reasonably do this differently and still satisfy the invariant, it is an engineering standard.*

Two independent front ends can block executable content in pasted themes by different means and both honour the right to restyle — engineering standard. No two implementations can disagree about whether the coordination protocol is a dependency leaf — invariant.

### The three rules

1. **Every standard cites the invariant it serves.** A standard serving no invariant is a product opinion and belongs nowhere in the canon. In the conformance registry this is the `serves` field, and **an entry with an empty `serves` fails registration** — the mechanism that keeps this tier honest without anyone policing it.
2. **A standard is never entrenched.** `GOV-4`'s double lock covers open source, privacy-first and data sovereignty, and no surveillance economics. Adding construction detail behind that lock is over-entrenchment, which `GOV-4` itself names as making the core less contestable rather than safer.
3. **A standard is amended by its layer's officer, recorded and contestable** — not by the amendment-in-the-open process that governs invariants, and not silently. `GOV-3` already makes each officer answerable for their layer's conformance and legibility; this is that answerability given something concrete to hold. Standing contestation (`GOV-6`) applies unchanged: any member may reopen a standard.

### Identifiers do not change on reclassification

A standard reclassified out of Part III **keeps its identifier**. `SUB-5` remains `SUB-5`. Eleven downstream `CONFORMANCE.md` and `OPEN-QUESTIONS.md` files across the canon already cite these identifiers, and the whole point of a stable ID is that a downstream repository's self-description survives the canon being reorganized. What changes is the `kind` field in the registry and the location of the normative text — never the citation.

The identifiers therefore remain layer-prefixed and share one numbering space with the invariants of that layer. `SUB-5` is a Substrate requirement whether it is an invariant or a standard; the register says which.

---

## The register

| ID | Serves | Layer | Requirement |
|---|---|---|---|
| `SUB-5` | standard #5 (presentation) | Substrate | Scripts never; markup sandboxed |
| `SUB-6` | standard #5 (presentation) | Substrate | No remote fetches from user styles |
| `SUB-7` | standard #5 (presentation) | Substrate | Reset-to-default lives outside the styleable surface |
| `SUB-8` | standard #5 (presentation) | Substrate | Styles are plain, exportable artifacts |
| `SUB-9` | standard #5 (presentation) | Substrate | Shipped or hosted themes inherit the carve-out |
| `GOV-10-E` | `GOV-10` | Governance | Provenance enforcement is a merge-blocking check |
| `LEG-2-T` | Amendment 002 legibility clause | Governance | A translation declares its source, commit, and review tier |

Two identifiers are new. `GOV-10-E` and `LEG-2-T` are the *enforcement mechanics* of requirements whose principle stays invariant; the suffixed form marks a standard derived from an invariant that itself remains in Part III, so the citation makes the relationship visible. Standards with no invariant counterpart of their own take a plain layer-prefixed number in the layer's sequence.

---

## Substrate — presentation sovereignty

*Serving standard #5: `…and presentation is separable, with every participant holding the right to restyle their own render.`*

The right to restyle one's own render is invariant and stays in the architecture. These five are how a conformant front end delivers that right without handing the member a weapon pointed at themselves. They are enforced **at import and paste** — where the front end actually holds the content — because themes circulate out of band regardless of any local-only intent.

Scope is self-view only, by decision rather than omission: a participant's styling affects their own render exclusively, and nothing about it enters the commons or any other participant's view.

**`SUB-5` — Scripts never; markup sandboxed.**
Pasted themes carrying executable content are the standing self-XSS attack. HTML customization is structural and presentational only; no theme executes.
*Suite binding:* implementation — front-end theme-import tests: executable content rejected.

**`SUB-6` — No remote fetches from user styles.**
CSS alone phones home — `url()`, `@import`, `@font-face` — and a circulated theme becomes a beacon. Strip or block remote references at import. Privacy-first entails this even with no publish path.
*Suite binding:* implementation — front-end theme-import tests: `url()`/`@import`/`@font-face` stripped.

**`SUB-7` — Reset-to-default lives outside the styleable surface.**
The undo cannot be occludable by the thing it undoes.
*Suite binding:* implementation — front-end UI tests: reset control unstyleable.

**`SUB-8` — Styles are plain, exportable artifacts.**
A CSS or HTML file the user can read, carry, and reapply — never an opaque blob; and the customization stays entirely out of the commons.
*Suite binding:* implementation — front-end tests: theme export round-trips as plain CSS/HTML.

**`SUB-9` — Shipped or hosted themes inherit the carve-out.**
A user hiding covenant surfaces from themselves is sovereignty; a front end shipping or hosting a theme that does so is the system hiding harm with extra steps.
*Suite binding:* implementation — front-end release tests: bundled themes render covenant surfaces.

**Accessibility floor, unchanged.** The default theme carries WCAG 2.2 AA and the editor itself meets it; a participant's own overrides are their own — self-view restyling is the user-stylesheet tradition the accessibility standards exist to protect.

**Left open, by decision.** *Published styling* — customization as expression to others — remains a cheaply reversible later option behind one recorded condition: any view shown to others renders covenant-mandated surfaces, harm distributions and adjudication status, platform-controlled and non-occludable. *Theme-gallery governance* is undecided; `SUB-9` is the floor and curation beyond it is open. Both belong here rather than in the architecture, and moving them here is part of what this register is for: an open product question sitting inside Part III reads as an unresolved constitutional matter, which it is not.

---

## Governance — provenance enforcement

*Serving `GOV-10`: `Provenance is inbound = outbound… The covenant never suspends; its enforcement mechanism may.`*

**`GOV-10-E` — Provenance enforcement is a merge-blocking check.**

That every contribution enters the copyleft commons, that there is no contributor license agreement and no assignment to a center, and that the covenant itself never suspends — all invariant, all unchanged in Part III.

*How* that is discharged is this standard: a certificate-of-origin sign-off or equivalent, enforced by a check that can **fail a merge to a default branch**. Per the legibility ladder's own logic — rung 5, prose bound to code by checks that can fail — a provenance rule that cannot fail a merge is marketing.

Three requirements:

1. The check runs on every proposed change to a default branch and blocks the merge on failure. An honour-system rule does not satisfy this standard.
2. The sign-off trailer matches the commit author. A trailer that names someone other than the author certifies nothing.
3. Suspension follows `GOV-10`'s interim rules exactly — named, with a committed reinstatement, recorded in the repository's conformance self-description and reported until reinstated; and the enforcement gap stays **permanent for the commits made inside it**, because reinstatement cannot retroactively certify them.

*Suite binding:* implementation — repo checks: licence present, no CLA, sign-off enforced at the branch protection layer.

**Steward practice, not standard.** That this steward uses the GitHub DCO app with a "Require DCO" ruleset per default branch is policy. A downstream community using a different mechanism that blocks merges has not left the architecture. Mirror topology, platform choice, and archival cadence remain policy for the same reason (Amendment 001).

---

## Governance — translation provenance

*Serving Amendment 002's legibility clause: `a translation is a render bound to the normative text, never a second source of truth`, and `LEG-2`'s reading-aid-never-oracle discipline.*

**`LEG-2-T` — A translation declares its source, commit, and review tier.**

The architectural claim is that there is one source of truth and many renders. This standard is what makes the claim checkable rather than asserted: an unmarked translation *is* a second source of truth, because a reader has no way to tell it from one.

Every translated artifact in the canon carries a header declaring:

1. **The English source file** it renders, by path.
2. **The commit** of that source it was generated from — this is what makes drift detectable rather than merely regrettable.
3. **Its review tier** — machine-assisted community draft, or reviewed by a named regional maintainer (P2-002 §2.3).
4. **That the English original governs** in case of conflict.

A translation whose source has moved past the declared commit is **stale**, and stale is a reportable state, not a cosmetic one. Regeneration is wholesale: if the English source changed, every language regenerates, so no translation silently describes an older version.

*Suite binding:* implementation — repo checks: every translated artifact has a header; declared source exists; declared commit is an ancestor of the source's current commit.

**Why this is a standard and not policy.** The seven-language portfolio, the `.lang.md` suffix convention, and the review cadence are P2-002 policy and will change. That a render declares what it renders is the thing that must not change, because the no-second-source-of-truth claim depends on it entirely.

---

## Adding a standard

1. Name the invariant it serves. If you cannot, stop — it is a product opinion.
2. Apply the distinguishing test. If no conformant implementation could reasonably do it differently, it is an invariant and belongs in Part III through amendment in the open, not here.
3. Give it an identifier in its layer's sequence — suffixed (`GOV-10-E`) if it is the enforcement mechanics of an invariant that remains in Part III, plain-numbered otherwise.
4. Write the requirement, the reason, and the suite binding — what test, in which repository, would fail.
5. Register it with `kind = standard` and a non-empty `serves`.
6. Record the addition where the layer's officer is answerable for it.

A standard that cannot describe the test that would fail is not ready. That is rung 5 applied to this register itself: prose that can fail a build is trustworthy prose, and this document is not exempt.
