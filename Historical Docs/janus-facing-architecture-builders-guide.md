# Janus-Facing Architecture

*A builder's guide: how to build a sovereign economy that no one owns and everyone can leave.*

**Network Theory Applied Research Institute** · Version 2.0 · June 2026

*Distilled from the design intent of the applications argument, the Agrinet protocol, Mycelium, and SoHoLINK, surfaced under adversarial critique. Those systems are held to this guide going forward; it is the standard they answer to, not a description of them.*

> *"When the work is done and their aim fulfilled, the people will say, 'We did it ourselves.'"* — Tao Te Ching, 17

---

## How to use this guide

Janus-Facing Architecture is one rule: govern every layer by the cost of leaving it. What you build under that rule is one kind of thing — a mutual credit network: an economy in which members extend value to one another against a covenant not to harm, on a record no one can quietly rewrite, on hardware no one can revoke, with no central issuer of money and no central judge of trust.

This guide turns the rule into build instructions. Each section states a principle as something to build, works it through a system NTARI has already built or specified — including where that system falls short — and ends with a conformance check. Gathered at the end, the checks are the standard: a system is NTARI software only if it passes all of them.

Treat the shortfalls as the method, not as apology. The architecture forbids performing the absence of gaps; a worked example that concealed where it fell short would only teach you to conceal your own. Every example here names its limit, and the limit is half the lesson.

## What you are building

The form is mutual credit: money created at the moment of exchange. One balance goes negative, one positive, the sum always zero. The value is backed not by a reserve but by members' covenant and their capacity to deliver real goods and work — no central bank mints it, no shareholder owns the float. This is not a theory awaiting trial. The WIR Bank has cleared a complementary franc among Swiss firms since 1934; Sardex has cleared business-to-business trade across Sardinia for over a decade. You are not inventing mutual credit. You are instantiating it digitally under a discipline that keeps it from curdling into its opposite.

The rule is the discipline: govern a layer by the cost of leaving it. Where leaving is cheap, exit governs and you need almost no machinery. Where leaving is dear, voice must do the work exit cannot. Where leaving is impossible, keep the layer minimal, keep it legible, and hold it under permanent contest.

The two are inseparable, and seeing why is the whole point. A mutual credit network contains a scorer (who is trustworthy?), an issuer (whose credit is good?), and a ledger (what happened?). Concentrate any one of them and you have rebuilt the bank — an authority that decides who is creditworthy and answers to no one. The architecture is the only thing standing between mutual credit and that outcome: it keeps the scorer contestable, the ledger legible, and exit cheap, so the power to extend or deny credit never settles where it cannot be checked or left. Run it the other way and the rule alone is abstract — the economy is what gives every layer a concrete job. The form supplies the work; the rule keeps the work free.

**Build it:** build one thing — member-issued mutual credit, governed by the cost of leaving. A system that neither issues nor governs such an economy may be useful, but it is not this.

**Conformance.** The system is, or governs, a member-issued mutual credit economy — not a banking, scoring, or escrow product wearing its vocabulary.

## Build from the floor up

Sovereignty is built from the bottom. You cannot decentralize governance onto infrastructure you do not own, and you cannot run an honest economy on a record someone can rewrite. So the architecture is a stack, and the order is the argument: each layer is sovereign only because the one beneath it is. Build it bottom-up, and hand it to your readers to be read the same way — substrate, then record, then covenant, then economy. Invert the order and every layer above the inversion is decoration.

One thing to hold before the layers: platform power lives in *architecture, not ownership*. Cooperative ownership of an extractive design reproduces extraction, because an interface that shows each party only enough to perform its role — and never enough to see the exchange whole — metacommunicates subordination beneath whatever its content says. Hierarchy is enforced at the level of the screen, below the cap table. That is why the work is architectural, and why none of it is fixed by who holds the equity.

## Layer one — sovereign compute (the substrate)

Start with the dependency most designs never name: software has to run on someone's hardware. An open, forkable protocol is worth little if the only place it can practically run is a hyperscaler or one operator's servers, because then whoever owns the iron owns the network and the openness is decoration. The turtles stop at the cloud invoice.

**Build it:** give every community somewhere to run the protocol, or a fork of it, that no one can revoke — and build that place-to-run *before* the things that run on it.

NTARI's instance is SoHoLINK: a federated compute marketplace that turns participant-owned hardware — desktops, NAS boxes, mini-PCs, phones — into a substrate the rest of the network runs on. It is the most-built layer in this guide: it exists, it runs, it is AGPL. That the place-to-run was built before the things that run on it is the correct order, not an accident.

Where it falls short — and this is permanent — is that sovereign compute buys *mechanical exit, not social or economic exit*. The installers are zero-dependency and the mesh self-discovers, so anyone *can* host. But the chokepoint is relocated, not removed: to the federation's coordinator, who sets fees and mediates the marketplace, and to reputation, since a fresh node with no standing draws no work and earns nothing. That is exactly the deliverability problem that recentralized email despite its open, self-hostable protocol — the mechanical right to participate never delivered the economic capacity to, and email concentrated anyway. So the substrate *caps* how concentrated hosting can become; it does not *guarantee* hosting stays distributed. That guarantee comes from legibility and cheap exit, never from the mechanism alone. And because compute is forkable, the substrate is emphatically *not* the layer no one can leave — that layer is the spec, far above it.

**Conformance.** It runs, or can run, on infrastructure its participants can own — no unremovable hosting chokepoint.

## Layer two — the witnessed ledger (the record)

On the substrate sits the record. An honest economy needs an account of what happened that no one can quietly rewrite, and the design philosophy is *detection, not prevention*: you do not make tampering impossible, you make it evident.

**Build it:** keep per-operator append-only logs and make them non-equivocable by witnessing — not one global chain, not consensus. Make the dialog the atomic unit. Seal it only when the exchange is both complete and quiescent. Annotate, never erase. Keep PII out of the commons.

NTARI's instance is Mycelium. The atomic unit is the dialog — one append-only file per exchange, accumulating the whole story in order: messages, the money lifecycle, ratings, any dispute. It seals only when the exchange is *complete* (every party owed a rating has one; a party that does not rate in its window is assigned a marked default, so silence reads as an exchange that ended without complaint and is never mistaken for praise) and *quiescent* (no dispute open; a harm claim holds the seal open in both directions until it is answered, so the record is never frozen mid-dispute and a harm is never sealed away before adjudication). Two commitments are absolute. *Annotate, never erase:* a front end may forgive a harm but can never hide one, so a dismissal is a new visible record, not a deletion. *No PII in the commons:* the ledger anchors structural facts and references only, never the free-text narrative or anything identifying — which is exactly what lets an immutable record coexist with a right to be forgotten, the personal data living in the erasable, front-end-local layer.

The load-bearing design choice: the ledger is *not one global chain*. There is no global order over unrelated exchanges and none is needed. Each operator keeps its own append-only log and publishes signed, monotonic checkpoints to independent witnesses; an operator that shows two different histories thereby produces two validly-signed, mutually-inconsistent checkpoints — a self-evident, attributable, portable proof that it lied. This is the Certificate Transparency model, not consensus. The *form* of the ledger is shared across platforms because the construction is domain-independent; each platform runs its own *separate* log over it.

Where it falls short: witnessing makes equivocation detectable, not prevented — preventing it outright would require a larger authority at the core, which the architecture refuses — and detection is only as strong as a verifier's reach to independent witnesses, with eclipse a standing residual. And be honest about today: the witness layer that makes the record non-equivocable across *multiple* operators is intended, not yet built; until it exists, non-equivocation rests on there being a single backend.

**Conformance.** Its record is immutable, tamper-evident, witnessed against equivocation, and PII-free in the commons; harm can be forgiven but never hidden.

## Layer three — reputation as covenant

On the record sits trust. Build reputation as a covenant — a standing promise not to harm — *not* a score. It is binary where it counts: you are in good standing or in breach, and the lowest rating on the scale, a harm, *is* the breach, not a debit against a running total.

**Build it:** never average. Carry the full distribution — the count at each level beside the total — so a harm is always visible next to the volume and never cancelled by it. Make the covenant run both ways, so the system never encodes that one class is trustworthy and the other is the risk. Make every claim answerable, with dismissals recorded as annotations rather than erasures. And gate *whether* a member transacts on trust at all — never *how much*.

NTARI's instance is LBTAS, the Leveson-Based Trade Assessment Scale. The logic is the safety engineer's: two crashes in seventy-three flights grounds the fleet. Volume is signal, but it does not absolve harm, and no quantity of good ratings dissolves a harm into a comfortable average. A producer's harm claim against a consumer is as contestable as the reverse.

The way this layer fails is subtle, so engineer against it: what the covenant secures is *honesty, not capacity*. "I will not harm you" is not "I can deliver what I promised," and an honest party can simply over-extend and fail. Non-delivery is itself a harm and belongs in the covenant. But *bounding how large a commitment an honest actor may take on* is a different instrument — a limit, which belongs to the economy, not the covenant. The covenant gates the door; the limit sizes the room. Let the two merge — let good standing buy a higher ceiling — and the harm distribution quietly becomes a credit score, and the bank returns through the back door.

**Conformance.** Its reputation is a covenant, not a score: a full distribution that never averages, contestable in both directions, gating whether-not-how-much.

## Layer four — the economy (member-issued credit)

At the top sits the economy, and it is mutual credit *derived from the record, not bolted onto it*. A member's balance is a deterministic function of the ledger — each sealed exchange moves two balances that net to zero — so the "currency" is simply the running position computed over facts already stored immutably.

Three commitments govern it once it is on.

*Gate by covenant, cap by a separate limit.* The covenant decides whether a member transacts on trust at all. A limit — derived from clean volume, declared capacity, a flat starting line, anything *but* the harm distribution — caps how much exposure the network extends before standing must be re-earned. Conflate them and you rebuild the credit bureau.

*Keep currencies sovereign and separate, not unified.* Each platform runs its own ledger and its own currency. This is safer on every axis: no cross-ledger double-spend, no shared monetary core anyone must govern, and — most of all — it is the anti-colonial monetary move, because each community issues and clears in a unit no outside party can inflate or devalue it into dependence. A unified currency would force the ledgers to stop being independent and rebuild precisely the shared, no-exit core the architecture works to keep small. Separate currencies do *not* force separate identities, though: one portable, witnessed reputation across platforms remains available, and is a far lighter lift than unifying money.

*Make the peg a yardstick, not a tether.* Denominate one-to-one against fiat — one unit, one dollar — for one reason only: legibility. The peg is *not* a defense against rich-poor divergence, and the intuition runs backward here. A fixed rate between economies of unequal productivity does not equalize them; it removes the valve that lets the weaker one adjust and forces the divergence out as something crueler — unemployment, wage cuts. The Eurozone periphery and the interwar gold standard are the warning, not the model. The defense against domination is *sovereignty* — issuing your own unit and never owing in someone else's — which the network has the moment each community issues its own credit. So the dollar is the unit of *account*, never the *backing*. Two lines are absolute: the peg stays a yardstick, never a bridge (the moment one platform's unit converts to another's at a fixed rate, the currencies are merged and double-spend returns); and denomination is not redeemability (a unit counted in dollars but not cashable for them is internal credit; a unit redeemable for actual dollars against reserves is a stablecoin and a regulated money-transmitter). Denominate at par; never redeem at par.

Where it falls short is the most honest line in the guide: this layer is *not yet switched on*. Today's settlement is pre-funded escrow, which is the *opposite* of credit — collateralized in advance, no balance ever negative, no trust ever extended. The architecture is mutual-credit-ready; turning credit on is a deliberate, still-unmade decision with real walls attached.

### How to switch credit on

You cannot cold-start mutual credit. A credit network with few members is worthless — no one to trade with, no one whose credit is worth extending — so you bootstrap in three phases, and the order matters as much as it did in the stack.

**Phase one — fiat on-ramp and integrity display.** Members transact in fiat through the escrow marketplace. Real fiat earnings for real work attract the volume you need, and the witnessed ledger runs underneath, building and *displaying* an auditable record of honest dealing. The escrow lives here, and you say plainly that it is the opposite of credit. This phase has two goals only: critical mass, and visible integrity.

**Phase two — earned, non-redeemable credit enters.** Once there is volume and visible trust, introduce the mutual-credit unit — but only as *earned* (issued for value provided to the network, never bought with dollars) and *non-redeemable* (spend-only, in-network, never cashed out; denominated in dollars but not convertible to them). Its value proposition is the one thing fiat cannot do in-network: counter-cyclical, interest-free credit — liquidity precisely when outside money is scarce. That, not a screen, is what moves people. Migration is *pulled by the value-prop, never pushed by a button*: nobody trades liquid fiat for a non-redeemable token because an interface asks them to; they do it when the token does something fiat cannot. Security earns trust-to-*hold*; only the value-prop earns want-to-hold.

Non-redeemability does double duty, which is why it is non-negotiable. It is the regulatory firewall — a unit that is earned and never cashable is barter-credit, not the money-transmission or securities activity a redeemable, purchasable token would be — and it is the adverse-selection filter: with no fiat yield to extract, pure extractors self-select out as the fiat phase recedes, and the members who remain are exactly the ones who value in-network credit. The migration is therefore also a population sort.

**Phase three — the internal economy thickens; fiat retreats to the perimeter.** As the credit proves more useful in-network than fiat — especially in a crunch — internal volume grows and fiat falls back to the boundary: taxes, outside suppliers, the genuinely external. The end state is mutual credit governed by the architecture, with fiat as the interface to the outside rather than the medium within.

The non-negotiables, in one line each: the unit is earned, never purchased; it is non-redeemable (firewall and filter both); denomination is not redemption; migration is pulled by a value-prop, never pushed by a UI; the covenant and the limit gate issuance throughout; and you get a real regulatory read *before* phase two — a nonprofit issuing a quasi-currency sits on a money-transmitter and securities knife-edge, and earned-not-bought plus non-redeemable is the line you do not cross by accident.

The one decision that is yours, not the architecture's: decide *who* your first users are before *how* you recruit them. A broad fiat lure buys fast volume and a money-motivated founding population, and bets that the filter sorts them out later. A targeted value-prop draw — Sardex's path, recruiting members who already feel the credit pain the network solves — buys alignment and culture at the cost of speed. Both are legitimate. If you take the lure, the filter is what you are betting on; make sure it holds.

**Conformance.** Its economy, if it has one, is member-issued mutual credit gated by covenant and capped by a separate limit; its currency is sovereign, separate, denominated-not-backed, non-convertible across platforms, and never redeemable for fiat; and credit is earned, never bought, entering only behind a value-prop strong enough to pull migration.

## Governing what you have built — the three regimes and the one actor

The rule now does its work. Govern each layer by the cost of leaving it, and each layer gets the only discipline that can hold it.

*Voice* governs the peer layer, where a harm claim can be raised, answered, and adjudicated. The contest is cheap there, so it runs as argument.

*Exit* governs the front ends and the substrate, where leaving is cheap by construction. The market, the record, and the compute all live below any single front end, so leaving one costs only that one. A community reads a front end's trajectory and leaves on the trend rather than waiting for collapse; a failing front end migrates its users without destroying the market. Exit is the discipline because exit is available.

*Contestation* governs the core — the protocol specification — the one layer no one can cheaply leave, because forking it splits the liquidity. It cannot be disciplined by exit, so you keep it minimal (it guarantees only the portabilities that keep every layer above it leaveable, so capturing it pays little), keep it legible (so the one expensive exit, reimplementation, stays possible), and hold it under permanent, standing contestation.

This is **Figure 1, the gravity well**: the deeper the layer, the higher the cost of leaving — shallow at the surface, where users drift off freely, and bottomless at the core, the spec you contest but cannot exit. Its companion is the dependency stack, read floor-up; the two are the same architecture seen as a force and as a sequence.

And the point that makes "the community governs itself" a description rather than a slogan: the two forces of a free order — the power that coordinates and the power that checks — are not two populations but two *functions*, which the same members hold and exchange continuously. The software does not end the contest between them; it internalizes and accelerates it, so the balance is held by motion, the way a living body holds its temperature, not by arrival at a resting symmetry. Do not build for a symmetric end-state and expect it to hold — transparency is not a destination, and the balance decays the instant the running stops. Symmetry is the stage; the contest is the play, and the play has to go on being performed.

What keeps this self-government rather than despotism is legibility: the coordinated can become the coordinators only if they can read and fork the logic that governs them. Legibility is therefore not a feature; it is the condition under which every other claim in this guide is true, and the one commitment whose loss collapses all the rest. It is the single entrenched non-negotiable — and the reason the AGPL's guarantee of the right to fork means nothing unless the artifact ships legible enough to exercise it.

**Conformance.** Voice where contest is cheap, exit where it is dear, standing contestation at a minimal, legible, permanently-contestable core — and legible above all, documented and interpretively accessible enough that the people it governs can read it, fork it, and leave.

## The steward

A network governed by "the community" in the abstract is governed by whoever shows up — the tyranny of structurelessness, capture in open-source clothing. So the one layer with no exit is stewarded by a named body.

**Build it:** name a steward; fill its board from the bottom with recallable delegates of open, sociocratic circles, one member one vote; entrench its deepest commitments behind a double supermajority; and discipline it by the only three things that can discipline a no-exit layer — the entrenchment of those commitments, the expensive-but-real fork of its implementation, and an obligation to keep internal opposition standing rather than to average dissent into consensus.

NTARI's instance is the institute itself: a 501(c)(3) whose deepest commitments — open source, privacy-first, no monetized surveillance, and the non-equivocable witnessed record — are entrenched as above.

Where it falls short, named not performed: at this one layer the governed and the governing are not yet the same set. The protocols are free to all, but the membership that governs the steward is, for now, purchased — and that gap binds hardest on exactly the participants a harm-surfacing system exists to protect, those who come to the network from crisis with the least to spare. Closing it — universal membership — depends on coordination infrastructure (NTARI/OS) that is, as yet, present in intent rather than in fact. The honest posture is to keep the contested prize small, keep exit real, keep the opposition standing, and name the gap as interim work — not to perform a unity the floor does not yet have.

**Conformance.** The core is stewarded by a named, internally-accountable body; its commitments are entrenched only where legibility and portability demand it; and any gap between the governed and the governing is named as interim work, not concealed.

## The honest ledger — what is built, and what is not

The method forbids performing the absence of gaps, so the guide ends by naming them. This is itself an instruction: ship your own status this plainly.

**Built.** The sovereign compute substrate (SoHoLINK); and the single-operator record, reputation, and escrow settlement (Agrinet).

**Intended, not yet built.** The witness layer that makes the record non-equivocable across multiple operators — the single most important step toward real federation; until it exists, non-equivocation rests on there being one backend. And NTARI/OS, the coordination-and-membership substrate that would close the governed/governing gap at the core.

**Not yet switched on.** Mutual credit itself. Today's settlement is escrow; turning credit on is the deliberate, phased decision set out above, with the Sybil, denomination, and regulatory walls attached.

**Open.** Reputation portability across platforms — available, lighter than currency unification, and undecided. And the residuals the architecture does not pretend to close: equivocation is detectable but not prevented, and only as strong as a verifier's reach to independent witnesses; computation honesty — whether an operator's match or price was fair — is out of scope, checked only by legibility and exit.

## The standard

Gathered, the section checks are the cornerstone. A system is conformant to Janus-Facing Architecture — and is NTARI software — only if all of them hold.

1. **Mutual credit, not banking.** It is, or governs, a member-issued mutual credit economy, gated by covenant and capped by a separate limit; its currency is sovereign, separate, denominated-not-backed, non-convertible across platforms, never redeemable for fiat; and credit is earned, never bought, entering only behind a value-prop strong enough to pull migration.
2. **Sovereign substrate.** It runs, or can run, on infrastructure its participants can own — no unremovable hosting chokepoint.
3. **Witnessed, legible record.** Its record is immutable, tamper-evident, witnessed against equivocation, and PII-free in the commons; harm can be forgiven but never hidden.
4. **Reputation as covenant.** Its reputation is a covenant, not a score — a full distribution that never averages, contestable in both directions, gating whether-not-how-much.
5. **Governed by the cost of leaving.** Voice where contest is cheap, exit where it is dear, standing contestation at the core.
6. **A minimal, contested, stewarded core.** The specification is kept minimal, entrenched only where legibility and portability demand it, permanently contestable, and held by a named, internally-accountable steward.
7. **Legible above all.** It is documented and interpretively accessible enough that the people it governs can read it, fork it, and leave. A commons no one can read is a freedom no one can use.

Every NTARI product — SoHoLINK, Agrinet, and what follows — is an instance of this, or it is not NTARI software.

## Closing

What you are building is a sovereign economy: members issue their own trust to one another, in their own currency, on a record no one can rewrite, hosted on hardware no one can revoke, governed by a contest that never ends. Mutual credit is the form, because it puts the power to extend value in the hands of the people who exchange it. The architecture is the discipline, because it keeps that power from settling anywhere it cannot be checked or left. Money becomes a covenant between two people instead of an instrument handed to them; governance becomes a race the community runs instead of a throne it builds.

Liberty here is not a state the architecture reaches and holds. It is the running. Your only job is to keep the running cheap, legible, and impossible to stop.

## References

- Acemoglu, D., & Robinson, J. A. (2019). *The Narrow Corridor: States, Societies, and the Fate of Liberty*. Penguin Press.
- Graeber, D. (2011). *Debt: The First 5,000 Years*. Melville House.
- Greco, T. H. (2009). *The End of Money and the Future of Civilization*. Chelsea Green.
- Laurie, B., Langley, A., & Kasper, E. (2013). *Certificate Transparency*. RFC 6962, IETF.
- Leveson, N. G. (2011). *Engineering a Safer World: Systems Thinking Applied to Safety*. MIT Press.
- Mead, G. H. (1934). *Mind, Self, and Society*. University of Chicago Press.
- Ostrom, E. (1990). *Governing the Commons: The Evolution of Institutions for Collective Action*. Cambridge University Press.
- Stodder, J. (2009). "Complementary Credit Networks and Macroeconomic Stability: Switzerland's Wirtschaftsring." *Journal of Economic Behavior & Organization*.
- Watzlawick, P., Bavelas, J. B., & Jackson, D. D. (1967). *Pragmatics of Human Communication*. W. W. Norton.

---

*Network Theory Applied Research Institute, Inc. — 501(c)(3) — EIN 92-3047136 — info@ntari.org*
*This guide is free documentation under the project's AGPL-3.0 commons; it is meant to be read, reimplemented, and contested.*
