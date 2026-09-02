# JFA Amendment 001 — Open Questions as Deliverable; Presentation Sovereignty

*Amends the builder's guide and the operating brief at their current versions. Drafted against guide v2.0 and brief v1.0 plus decisions locked since; the contradiction check against v3/v4 text is outstanding — reconcile before this amendment locks. Standing amendment until merged at the next version bump of each document, then retained as record.*

**Network Theory Applied Research Institute** · Version 1.0 · July 2026

---

## Amendment One — every project ships a living open-questions document

**The rule.** Every project ships, as a build deliverable equal to its code, a living open-questions document naming what is unresolved about the project's future. This generalizes what the architecture already does at the top — the honest ledger, the brief's Part II, the tension protocol — down to every project in the canon.

**Genre discipline.** It is not a roadmap. A roadmap pre-decides; this names. Pre-codifying the future commits the error the architecture diagnoses — substituting a fixed artifact for a live decision. The document carries questions, constraints, and status; never commitments dressed as questions.

**Structure.** Each entry states three things: the problem; the constraints any resolution inherits from the architecture, such that a resolution violating them is not a resolution; and current status. This is the Part II pattern applied per-project.

**Living, defined.** Reviewed and re-shipped with each release. A stale open-questions document is conformance drift, not housekeeping — a project performing the absence of its gaps has failed the method, whatever its code does.

**Removal discipline.** An entry leaves the document only by resolution or by an explicit values call made by the people who live with the outcome. Silent absorption — the question quietly disappearing between versions — is the erosion the tension protocol exists to catch.

**Roll-up.** Project documents feed the network-level open problem stack. A question discovered locally that binds architecturally is promoted to the brief's Part II, not kept local; the network stack and the project documents cite each other in both directions.

**Conformance delta.** The legibility check (check 7) gains a clause: *…and it ships a living open-questions document naming what remains unresolved about its future; staleness is nonconformance.*

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

**Refuse or flag (extends the brief's list):**

- *"Let themes run scripts / load remote assets."* → Self-XSS and beaconing. Requirements 1–2; refuse.
- *"Ship a starter theme that tidies away the harm distribution."* → System-authored occlusion. Requirement 5; refuse.

**Conformance delta.** The governance check (check 5) gains a clause: *…and presentation is separable, with every participant holding the right to restyle their own render.*

---

## What this amendment leaves open

- **Published styling.** Door located, not opened: the covenant-surface carve-out above is the condition of any future opening.
- **Theme-gallery governance.** If a frontend ever hosts a gallery, requirement 5 is the floor; what curation beyond it looks like is undecided.
- **The covenant clock (relocated, not regulated).** Self-blindness carries no rule here; the consequence machinery assumes non-response to a harm claim converts to an adjudicated outcome on recorded time, never to indefinite pendency. Explicit for rating windows; verify at reconciliation whether the covenant spec pins it for harm response. If unpinned, it is a one-line covenant-layer item, not a presentation-layer one.
- **Reconciliation.** The contradiction check against guide v3 and brief v4 is outstanding; this amendment does not lock until it clears.

---

*Network Theory Applied Research Institute, Inc. — 501(c)(3) — EIN 92-3047136 — info@ntari.org*

*This amendment is free documentation under the project's AGPL-3.0 commons; it is meant to be read, reimplemented, and contested.*
