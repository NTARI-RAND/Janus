# JFA Amendment 001 — Open Questions as Deliverable; Presentation Sovereignty

*Amends the unified architecture document — the standing description that absorbed the builder's guide and the operating brief this amendment was originally drafted against (guide v2.0, brief v1.0). The contradiction check against the current text (brief v4.0 and the unified document) has run; its findings are applied in this draft and recorded at the end. Standing amendment until merged into the unified document, which is unversioned and amended in the open; on merge, retained in Historical Docs as record.*

**Network Theory Applied Research Institute** · July 2026 · *Reconciled draft — merged into the unified architecture document July 22, 2026, and locked; retained here as record per the amendment's own merge mechanics*

---

## Amendment One — every project ships a living open-questions document

**The rule.** Every project ships, as a build deliverable equal to its code, a living open-questions document naming what is unresolved about the project's future. This generalizes what the architecture already does at the top — the honest ledger, the network-level open problem stack (the unified document's Part VII), the tension protocol — down to every project in the canon.

**Genre discipline.** It is not a roadmap. A roadmap pre-decides; this names. Pre-codifying the future commits the error the architecture diagnoses — substituting a fixed artifact for a live decision. The document carries questions, constraints, and status; never commitments dressed as questions.

**Structure.** Each entry states three things: the problem; the constraints any resolution inherits from the architecture, such that a resolution violating them is not a resolution; and current status. This is the open-problems pattern applied per-project.

**Living, defined.** Reviewed and re-shipped with each release. A stale open-questions document is conformance drift, not housekeeping — a project performing the absence of its gaps has failed the method, whatever its code does.

**Removal discipline.** An entry leaves the document only by resolution or by an explicit values call made by the people who live with the outcome. Silent absorption — the question quietly disappearing between versions — is the erosion the tension protocol exists to catch.

**Roll-up.** Project documents feed the network-level open problem stack. A question discovered locally that binds architecturally is promoted to the unified document's Part VII, not kept local; the network stack and the project documents cite each other in both directions.

**Conformance delta.** The standard's check 7 (*Legible above all*) gains a clause: *…and it ships a living open-questions document naming what remains unresolved about its future; staleness is nonconformance.*

---

## Amendment Two — presentation sovereignty

**The guarantee (spec-level).** Presentation separability: styling ships as user-editable data separate from application logic, and every participant holds the right to restyle their own render. This is exit at the presentation layer — the cheapest exit in the stack. The gravity well extends one layer up: leaving a rendering costs nothing, so the layer is governed by pure exit and needs no machinery beyond the right itself. And it answers the metacommunication problem on its own ground: if hierarchy is enforced at the level of the screen, the counter is that the governed can rewrite their own screen.

**The pattern (frontend-level, recommended, not mandated).** In-app editing of the frontend's CSS and HTML, saved and rendered locally — an immediate customization layer requiring no fork, no toolchain, no permission. The spec guarantees the separability; the live editor is the recommended way a frontend honors it. Mandating the editor itself in the core would grow the contested prize for a product feature, which the minimal-core discipline refuses.

**Scope.** Self-view only, by decision rather than omission. A participant's styling affects their own render exclusively; nothing about it enters the commons or any other participant's view. Published styling — customization as expression to others — is out of scope, and remains a cheaply reversible later option behind one recorded condition: any view shown to others renders covenant-mandated surfaces (harm distributions, adjudication status) platform-controlled and non-occludable.

**Build requirements.** Five, invariant-grade:

1. **Scripts never; markup sandboxed.** Pasted themes carrying executable content are the standing self-XSS attack. HTML customization is structural and presentational only; no theme executes.
2. **No remote fetches from user styles.** CSS alone phones home — `url()`, `@import`, `@font-face` — and a circulated theme becomes a beacon. Strip or block remote references at import. Privacy-first entails this even with no publish path.
3. **Reset-to-default lives outside the styleable surface.** The undo cannot be occludable by the thing it undoes.
4. **Styles are plain, exportable artifacts.** A CSS or HTML file the user can read, carry, and reapply — never an opaque blob. Legibility applies to the customization itself; it stays entirely out of the commons.
5. **Shipped or hosted themes inherit the carve-out.** A user hiding covenant surfaces from themselves is sovereignty; a frontend shipping or hosting a theme that does so is the system hiding harm with extra steps.

**Enforcement point.** Import, not distribution. Themes will circulate out of band regardless of any local-only intent; requirements 1 and 2 therefore apply at paste and import, where the frontend actually holds the content.

**Accessibility.** The default theme carries the WCAG 2.2 AA floor and the editor itself meets it; a participant's own overrides are their own. Self-view restyling is the user-stylesheet tradition the accessibility standards exist to protect — this amendment extends that tradition rather than trading against it.

**Refuse or flag (extends the unified document's list):**

- *"Let themes run scripts / load remote assets."* → Self-XSS and beaconing. Requirements 1–2; refuse.
- *"Ship a starter theme that tidies away the harm distribution."* → System-authored occlusion. Requirement 5; refuse.

**Conformance delta.** The standard's check 5 (*Governed by the cost of leaving*) gains a clause: *…and presentation is separable, with every participant holding the right to restyle their own render.*

---

## What this amendment leaves open

- **Published styling.** Door located, not opened: the covenant-surface carve-out above is the condition of any future opening.
- **Theme-gallery governance.** If a frontend ever hosts a gallery, requirement 5 is the floor; what curation beyond it looks like is undecided.
- **Adoption.** The reconciliation check has cleared and its findings are applied above; the amendment locks when merged into the unified document.

---

## Reconciliation record

The as-filed amendment named its contradiction check against v3/v4 text as outstanding and did not lock until it cleared. The check ran in July 2026 against brief v4.0 and the unified architecture document. Three findings; each is applied in this draft and recorded here so that no entry leaves the amendment by silent absorption.

**1. The covenant clock — resolved against the assumption, entry closed.** The as-filed draft assumed the consequence machinery converts non-response to a harm claim into an adjudicated outcome on recorded time, never indefinite pendency, and asked reconciliation to verify whether the covenant spec pins this for harm response. It does — in the opposite direction. The current record invariant states: *a clock never force-seals a dialog; an unanswered claim stays open, and only its dwell is a readable fact.* The architecture chose dwell-as-readable-structure — feeding the adjudication-conduct read, which can cost an operator its governance eligibility — over clock-conversion-to-verdict, refusing the clock as an authority. Non-response therefore carries consequence through structure, not through a converted verdict. This is pinned for rating windows (a non-rater is assigned a marked default) and pinned for harm response as above. No covenant-layer item is needed; nothing relocates. The entry leaves the open list by resolution, on this record.

**2. Stale pointer retargeted.** The as-filed draft cited "the brief's Part II" as the network-level open problem stack — its location in brief v1.0, against which the amendment was drafted. The open problems now live in Part VI of brief v4.0 and Part VII of the unified document. All references in this draft point to the unified document's Part VII, and the pattern is named by role (the open-problems pattern) rather than by a number that can go stale again.

**3. Merge mechanics retargeted to the unified document.** The as-filed draft amended two versioned documents and merged "at the next version bump of each." The corpus has since converged on the unified architecture document — unversioned, amended in the open, having absorbed both the guide and the brief. This draft therefore amends the unified document directly: the conformance deltas land in its standard (checks 5 and 7, which retained their numbering), the refuse-or-flag items extend its list, and the amendment merges on adoption rather than at a version bump, after which it is retained in Historical Docs as record. The as-filed version 1.0 text is likewise retained in Historical Docs as record; this reconciled draft carries no version marker, matching the convention of the document it amends.

---

*Network Theory Applied Research Institute, Inc. — 501(c)(3) — EIN 92-3047136 — info@ntari.org*

*This amendment is free documentation under the project's AGPL-3.0 commons; it is meant to be read, reimplemented, and contested.*
