# Welcome, Reviewers: An Introduction to Janus Facing Architecture

*You found us through a short ad that promised something unusual: a nonprofit inviting the public — and students of political science, economics, sociology, psychology, finance, computer science, and information technology — to refine a written standard before the software that implements it is finished. This article is your orientation. It explains what Janus Facing Architecture is, why it is written the way it is, and what your review is actually for.*

---

## The framing

In conversation with Daron Acemoglu and James A. Robinson's book *The Narrow Corridor: States, Societies, and the Fate of Liberty*, Janus Facing Architecture is a model for operating a network state (Balaji Srinivasan, [thenetworkstate.com](https://thenetworkstate.com)) with liberty and community both intact.

That sentence carries the whole course, so it is worth unpacking slowly.

**The Narrow Corridor.** Acemoglu and Robinson describe the state as *Janus-faced* — after the Roman god with two faces. In one moment it shows the people a favorable face: it keeps order, enforces contracts, provides for the common good. In the next it can turn and show a monstrous one: surveillance, extraction, domination. Their answer to this danger is not to abolish the state or to unleash it, but a permanent footrace they call the Red Queen effect — society running hard to check the state while the state runs hard to stay capable — with liberty surviving only inside the narrow corridor where neither side pulls decisively ahead. Crucially, they keep the hierarchy: there is a state, there is a society, and liberty is the contest between them.

**The network state.** Balaji Srinivasan asks a different question: what if a community formed online first — organized around shared commitments, coordinating through the internet — and only later acquired the trappings of a state? The idea takes seriously that the internet changes what a founding can be. But it leaves the hard problem open: any community that coordinates at scale develops coordinating power, and coordinating power left unchecked becomes the monstrous face all over again — just hosted on someone's servers instead of seated in a capital.

**Janus Facing Architecture** is a written standard for holding both at once. It accepts the network-state premise that a community can be constituted on the internet, and it accepts the Narrow Corridor's warning that coordinating power must be permanently checked — then it collapses the state-over-society hierarchy entirely. There are not two populations, a platform and its users. There is one community carrying two *functions* at the same time: one face coordinates, the other checks the coordination, and members exchange the two continuously. Liberty is preserved not by a constitution alone but by keeping that exchange fast, cheap, and legible. Community is preserved because the coordinating function is real: the network actually moves goods, services, credit, and knowledge among its members. Neither is sacrificed to the other. That is what "liberty and community both intact" means.

## The one rule

The entire architecture compresses to a single principle: **govern every layer by the cost of leaving it.**

Where leaving is cheap — switching the app you use to reach the network — *exit* does the governing, and almost no machinery is needed. Where leaving is expensive — your reputation and trading history live there — *voice* must do the work exit cannot: contestable claims, answerable ratings, adjudication in the open. And at the one layer no one can leave — the shared specification that defines the network itself — the rule demands *standing contestation*: keep that core minimal so capturing it yields little, keep it legible so anyone can reimplement it, and never let ratification be final. (The exit-and-voice vocabulary comes from the economist Albert Hirschman; the standard tells you so, because it cites its sources like the scholarly document it is.)

## What is actually being built

The standard is not abstract political theory. It specifies one concrete kind of thing: a **mutual credit network** — an economy where members extend value to one another against a covenant not to harm, on a record no one can quietly rewrite, on infrastructure no one can revoke, with no central issuer of money and no central judge of trust. Mutual credit is a proven form, not speculation: Switzerland's WIR Bank has cleared complementary credit since 1934, and Sardex has done the same across Sardinia for over a decade. The work is instantiating it digitally without letting it curdle into the thing it opposes — a bank with extra steps.

The standard builds this as five layers, each sovereign only because the one beneath it is:

1. **Substrate** — coordination on infrastructure participants can own, so no host or vendor can shut the network off.
2. **Record** — a witnessed, append-only memory of what happened; corrections are new entries, never erasures, so tampering is evident rather than impossible.
3. **Covenant** — trust as a standing promise not to harm, carried as a full distribution of ratings that is never averaged into a score. One documented harm stays visible beside a thousand good trades, permanently.
4. **Governance** — a named, accountable steward for the one layer with no exit; open circles with recallable delegates; ratification that is never final.
5. **Economy & Information** — member-issued credit created at the moment of exchange (earned, never bought; never redeemable for dollars — that firewall is what keeps it credit rather than a security), plus a knowledge commons where claims are anchored and citable but never certified true by any central authority.

And all of it enters a copyleft commons under the AGPL-3.0 license — the legal instrument the ad mentioned. Anyone may take from the commons; no one may take from it without the binding obligation to give their improvements back. The commons cannot be enclosed.

## What the course covers, and what your review is for

The course walks the full standard: the argument, the five layers, the invariants each layer must satisfy (every one carries a stable identifier a test suite can check), how signals move through the system, two clearly-labeled explorations, and — deliberately — the open problems the architecture has *not* solved, stated as a numbered list with the constraints any future fix must inherit.

That last part is why you were invited. The standard holds itself to a rule it calls the tension protocol: never perform the absence of gaps. A document that hid its unsolved problems would be advertising; this one is meant to be contested, and contest requires readers from outside. Each discipline named in the ad maps to a place the standard needs pressure:

- **Political science** — the governance layer: entrenchment, recallable delegates, the operator-federation proposal for who gets a vote and why.
- **Economics and finance** — the mutual credit design: sovereign non-convertible units, the fiat-to-credit migration path, the money-transmitter and securities line the standard claims never to cross.
- **Sociology** — the covenant: whether reputation-as-distribution actually resists collapsing back into a score, and who a "false positive" excludes.
- **Psychology** — the standard's claims about what interfaces communicate: it argues that a screen showing each party only what its role requires quietly teaches subordination. Is that argument sound?
- **Computer science and IT** — the record and substrate: append-only logs, witnessed checkpoints, the certificate-transparency model, and the conformance suite that binds prose to code.

You do not need to write software to do this work. The standard's own thesis is that the prose *is* load-bearing — its legibility rules require that every normative sentence be checkable, which means an ambiguity you find in the text is a defect exactly as real as a bug in code.

**[→ Read the full Introduction to Janus Facing Architecture course here — LINK TO COURSE]**

Then tell us where we are wrong. That is not a courtesy invitation; the architecture does not work without it.

*Visit [ntari.org/volunteer](https://ntari.org/volunteer) to join the review.*

---

*Network Theory Applied Research Institute, Inc. — 501(c)(3) — [info@ntari.org](mailto:info@ntari.org)*
