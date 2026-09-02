# Five Layers, Nine Lines: The Shape of the Janus-Facing Architecture

*Network Theory Applied Research Institute — August 2026*

The Janus-Facing Architecture (JFA) states its purpose in a single sentence: it is *an architectural theory for building software for the prosumption of digitally coordinated goods and services with no other intermediary than the publicly maintained software itself.* Unpacked: **prosumption** means the same people who produce also consume — real goods, services, compute, and knowledge, traded on trust; **digitally coordinated** means software does the matching of supply to demand; and **no other intermediary** means no bank issuing the money, no platform owning the market, no landlord owning the record — only software anyone can read, run, and fork. In August 2026 the architecture was rebuilt around a single streamlined document of nine numbered sections, paired with an executable conformance suite, with every prior instrument preserved in the open. This article walks the current structure.

## Why anyone builds one

Start where the official document starts: with the point. The stack exists so that its top layer can happen — members sharing economy and information. If no one is sharing economy and information, there is no point; everything beneath exists to make that sharing safe.

A community that builds a JFA stack gets five things that are hard to get anywhere else together:

**Money without a bank.** The stack runs on mutual credit: money created at the moment of exchange — one balance goes down, one goes up, and the two always sum to zero. Credit is issued only for value provided. There are no reserves, no issuer, and no interest.

**A market without a landlord.** The software is copyleft and runs on hardware members own. No platform can raise the rent or close the market.

**A record no one can rewrite.** Every rated exchange is journaled append-only and witnessed by independent parties. Harm can be forgiven — but never hidden.

**Trust without surveillance.** Reputation is a covenant built from witnessed outcomes, not a score built from collected personal data.

**The right to leave.** A member's positions and history survive any frontend; a community's records survive any operator. Everything is leaveable except the truth of what happened.

## Two faces, one community

The name comes from Janus, the Roman god who looks both ways at once. The stack carries two functions permanently: coordinating the economy, and checking the coordination. The design's central refusal is to split those functions into two populations — rulers and ruled, platform and users, regulator and regulated. The same community does both, and the two roles are exchanged continuously.

One rule disciplines the whole structure: **each layer is governed by the cost of leaving it.** Where leaving is cheap, competition does the work. Where leaving is expensive, members get a vote. Where leaving is impossible, every decision stays permanently contestable.

## The grid: five layers, three tiers

The stack is five layers, built bottom-up — Substrate, Record, Covenant, Governance, Economy & Information — and each layer depends only on the layers beneath it. Every layer carries the same three tiers: a **protocol**, encoding the layer's most important socioeconomic data; an **orchestrator**, the backend federating diverse frontends; and a **frontend**, where members produce and consume simultaneously. The document calls these members *prosumers*, and the word is doing real work: one account carries both roles, and the architecture never splits a person into a producer identity and a consumer identity.

**Substrate** is the hardware where everything happens — CPUs, GPUs, printers, storage and sensors owned by members, running in homes and offices on consumer-grade machines. The orchestrator federates operator communities that compete on accessory features and regional optimization but share work across the same global market. The design constraint that matters: no single host, account, or vendor whose removal could stop the network.

**Record** is the layer most likely to surprise a technical reader, because it is not a blockchain. There is no central chain and no consensus layer. Instead, each operator keeps its own append-only log and regularly publishes a signed checkpoint of it to independent witnesses, who countersign it. The consequence is subtle and powerful: an operator showing two different histories to two different audiences becomes *provable*, not prevented. Lying stays possible; getting away with it does not.

Privacy is structural, not policy. The dialog around a transaction stays local to the parties' own interfaces; only structural facts — hashes, types, timestamps, exchange references — enter the shared record, which never carries narratives or identities. When a dispute arises it follows a witnessed lifecycle — file, adjudicate, resolve, seal — with every step committed to the record as it happens, and the filing itself lands at a witness independent of the operator who will adjudicate it. No one can quietly bury a complaint at intake.

**Covenant** is the social contract enforced in code: a short assessment that runs at each transaction, built from a member's previous interactions. Two rules keep it honest. First, reputation is never squashed into one number — what others see is the count of exchanges at each rating level, so one bad outcome cannot hide inside a good average. Second, reputation answers exactly one question: *may this member trade on trust?* How much credit they can draw is a separate cap set by the community's limit rules. Kept apart, one secures honesty while the other sizes risk. Merged, they recreate the credit score — the thing the covenant exists to replace.

**Governance** is where humans assemble to act on the stack: a legal entity to govern members and answer to national authority, a coordination platform, and — at the frontend — open circles any member may join, electing recallable delegates. Decisions stay contestable; any member can reopen a decided matter with an observation. And the venue itself runs on substrate members can leave, so no host's goodwill is ever a condition of self-government.

**Economy & Information** is the point of the stack — the four layers beneath exist so this one can happen. It is where category protocols are written for specific products, services and information; where wallets and marketplaces live; and where the money moves. All category protocols share one accounting grammar: mutual credit, gated by the covenant and capped by a separate limit. Credit is earned, never bought, and never redeemable for fiat.

Two mechanisms here deserve a closer look. The first is the **mirror requirement**: ledger state must at all times equal a replay of the sealed Record. Because balances are just a replay, orchestrators hold no hostage-able state — a failed or defecting operator is replaced by replaying sealed records, and every member's credit position survives. The second is how communities relate to each other: **value stays home; only truth crosses.** No community's money ever enters another. Cross-community exchange is two sovereign spends bound atomically by a witnessed proof — no shared unit, no central clearer, no exchange rate. And when a newcomer arrives with a clean history elsewhere, a community may — by its own explicit governance act, never by default — read that witnessed history and extend them local credit. Recorded truth travels; money never does. That single sentence is also the architecture's regulatory posture: nothing redeemable crosses any boundary, so there is nothing to transmit and nothing to clear.

## What it takes to build one

The document closes its constructive half with a checklist, and it is refreshingly concrete: hardware members own; a small protocol codebase that depends on nothing but its language's standard library, auditable whole; at least two independent witnesses — with fewer, a deployment must label itself a stand-in and not present itself as federated; a covenant the members themselves write and can change; a legal entity; category protocols for whatever the community actually trades; and a staged start for the money — beginning in escrow, with no negative balances and no trust extended, switching to mutual credit only after governance approval, membership notice, and a completed regulatory review. Finally, every project ships a living open-questions document naming what remains unresolved. A stale one means the project has stopped describing itself honestly.

## The nine lines

Section 9 of the document draws the boundary of the name: nine lines that cannot be crossed. The record is append-only — forgive by annotating, never by erasing. No narratives or identities in the shared record. No central chain. Reputation is never one number. Reputation decides *whether*; a separate limit decides *how much*. Credit is earned, never bought, never redeemable. Each community's currency is sovereign — no shared unit, no conversion. Value stays home; only truth crosses. And everything is leaveable except the record of what happened — which belongs to everyone.

The framing matters as much as the list: a build that crosses any of these is not a smaller JFA stack. It is different software wearing the name.

## Legibility, mechanized

The architecture's promise of openness is not left as a promise. The official document ships beside an executable conformance suite that verifies the document itself — its nine sections, its clause numbering, the presence of every registered invariant in the exact clause that carries it — and maintains a registry of thirty-seven invariants cited by clause number. Thirty-five of them can only be enforced by tests living beside running code or a governance instrument, and the suite says so, labeling them delegated and unbound rather than pretending to check them. A claim of conformance without tests citing those clause IDs is named what it is: self-attested.

The software stack is licensed under the GNU Affero General Public License; the specification under Creative Commons Attribution–ShareAlike 4.0. Both are copyleft: anyone may build new frontends, federations, protocols and architectures from them, and what they build stays open. Every prior instrument, amendment, and companion essay — including the far longer constitutional document this structure replaced — is preserved unedited in the project's historical archive. The architecture is meant to be read, reimplemented, and contested, and it keeps the receipts of its own evolution.

---

*The official document and conformance suite are stewarded by the Network Theory Applied Research Institute, Inc., a 501(c)(3) — info@ntari.org. This article describes the architecture; it never governs it.*
