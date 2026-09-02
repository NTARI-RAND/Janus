# Janus-Facing Architecture

**The Janus-Facing Architecture is an architectural theory for building software for the prosumption of digitally coordinated goods and services with no other intermediary than the publicly maintained software itself.** This is its official document, stewarded by Network Theory Applied Research Institute, Inc. Prior instruments, amendments, and companion essays are preserved in [Historical Docs](Historical%20Docs/).

**Licensing.** The JFA software stack is licensed under the GNU Affero General Public License (AGPL-3.0). This specification is licensed under Creative Commons Attribution–ShareAlike 4.0 (CC BY-SA 4.0). Both are copyleft: anyone may build new frontends, federations, protocols and architectures from them, and what they build stays open.

## 1. Why a community would build one

**1.1** The point of the stack is its top layer: members sharing economy and information — real goods, services, compute, and knowledge, traded on trust. If no one is sharing economy and information, there is no point; the four layers beneath exist to make that sharing safe.

**1.2** A community that builds a JFA stack gets:

1. **Money without a bank.** Mutual credit: money created at the moment of exchange — one balance down, one up, always summing to zero — issued only for value provided. No reserves, no issuer, no interest.
2. **A market without a landlord.** The software is copyleft and runs on hardware members own; no platform can raise the rent or close the market.
3. **A record no one can rewrite.** Every rated exchange is journaled append-only and witnessed by independent parties; harm can be forgiven, never hidden.
4. **Trust without surveillance.** Reputation is a covenant built from witnessed outcomes, not a score built from collected personal data.
5. **The right to leave.** A member's positions and history survive any frontend; a community's records survive any operator. Everything is leaveable except the truth of what happened.

**1.3** Between communities: value stays home; only truth crosses. No community's money enters another. Witnessed history lets communities trust each other's members without a shared bank or a shared currency — and therefore without transmitting money at all.

## 2. The shape of the stack

**2.1** The stack is five layers, built bottom-up: Substrate, Record, Covenant, Governance, Economy & Information. Each layer depends only on the layers beneath it.

**2.2** Every layer contains three tiers: the **protocol** — encoding the layer's most important socioeconomic data; the **orchestrator** — a backend providing federation service across diverse frontends; and the **frontend** — where members produce and consume simultaneously.

**2.3** One rule governs the whole: each layer is disciplined by the cost of leaving it. Where leaving is cheap, competition disciplines; where leaving is dear, members get a vote; where leaving is impossible, every decision stays permanently contestable.

**2.4** The stack is Janus-facing: the same community both coordinates and checks the coordination, and the two functions are exchanged continuously — never split into rulers and ruled.

## 3. Substrate Layer

The hardware where everything happens, owned by prosumers — members who produce and consume with the same single account — of CPUs, GPUs, printers, storage and sensors.

**3.1 Protocol.** Encodes instructions and orders across a distributed compute/storage market operated on consumer-grade computers hosted in homes, offices and storage.

**3.2 Orchestrator.** Federates frontend operator communities competing on accessory features and regional/cultural optimization but otherwise sharing work across the same global market.

**3.3 Frontend.** Market operated on the substrate protocol, translating supply and demand across the prosumer market.

## 4. Record Layer

The distributed, immutable record of the dialogs that resulted in rated exchanges.

**4.1 Protocol.** Encodes pre-to-post transaction dialog between prosumers. The dialog itself stays local to the parties' own interfaces; only structural facts — hashes, types, timestamps, exchange references — enter the shared record, which never carries narratives or identities. Each exchange is a dialog, sealed only when complete and quiescent; disputes follow the claim lifecycle — file, adjudicate, resolve, seal. This tier is the append-only journal of the stack's economy: all Economy & Information ledger state must be replayable from sealed records.

**4.2 Orchestrator.** The backend of the record network. Each operator keeps its own append-only log and regularly publishes a signed checkpoint of it to independent witnesses, who countersign it. There is no central chain: an operator showing two different histories becomes provable, not prevented. Every step of a dispute — filing, adjudication, resolution, seal — is committed to the record as it happens, and a claim's filing is committed at a witness independent of the operator who will adjudicate it.

**4.3 Frontend.** A program available for substrate compute providers that audits records published by frontends and the JFA stack against those in the Record.

## 5. Covenant Layer

The social contract enforced in code, guaranteeing expectations in prosumer interactions.

**5.1 Protocol.** A short, coded assessment that runs at each transaction, built from the member's previous interactions. Two rules keep it honest. First, reputation is never squashed into one number: what others see is the count of exchanges at each rating level, so one bad outcome cannot hide inside a good average. Second, reputation answers only one question — may this member trade on trust? How much credit they may draw is a separate cap set by the community's limit rules. Kept apart, one secures honesty while the other sizes risk; merged, they recreate the credit score.

**5.2 Orchestrator.** An API issuing compliant assessments and recording prosumer ratings across the markets of the stack.

**5.3 Frontend.** The prosumer/operator communities of the stack change the covenant using the governance layer.

## 6. Governance Layer

Where and how humans assemble to collaboratively act on the stack.

**6.1 Protocol.** An appropriate legal entity to govern members, plan and document work, oversee currency compliance and submit to national authority.

**6.2 Orchestrator.** Platform for synchronous and asynchronous coordination of the activities of members.

**6.3 Frontend.** Open circles any member may join, electing recallable delegates. Decisions stay contestable — any member can reopen a decided matter with an observation — and the venue itself runs on substrate members can leave, so no host's goodwill is a condition of self-government.

## 7. Economy & Information Layer

This layer is the point of the stack: the four beneath it exist so that this one can happen. It is where members actually trade and actually learn from each other — and where the stack pays for itself in met needs.

**7.1 Protocol.** Where protocols are developed for specific products, services and information categories. All category protocols share the stack's accounting grammar: mutual credit. Money is created at the moment of exchange — one balance down, one up, always summing to zero — issued only for value provided, gated by the covenant, and capped by a separate limit. Credit is earned, never bought, and never redeemable for fiat. Ledger state must at all times equal a replay of the sealed Record — the mirror requirement, enforced by the Record layer's auditors.

**7.2 Orchestrator.** Lets operators provision substrate for records and processing, adjudicate covenant breaches, and interact with their governance federation. Adjudicating operators are rated on their adjudication conduct by both prosumers involved. Each frontend operator community runs its own mutual credit ledger in its own sovereign unit; because ledger state mirrors the Record, orchestrators hold no hostage-able state — a failed or defecting operator is replaced by replaying sealed records, preserving prosumer credit positions. Cross-community exchange is two sovereign spends bound atomically by a witnessed proof — no shared unit, no central clearer, no exchange rate. A community may, by its own governance act, read a newcomer's witnessed history from another network and extend them local credit — recorded truth travels; money never does.

**7.3 Frontend.** Wallets and marketplaces where prosumers hold balances, publish offers against category protocols and initiate transactions. Frontends compete on accessory features atop the same ledger API; per the stack's exit commitment, a prosumer's positions and history are carried by the Record and survive any frontend.

## 8. What it takes to build one

**8.1** Hardware members own — ordinary consumer machines in homes and offices. No single host, account, or vendor whose removal could stop the network.

**8.2** The protocol software: small, dependent on nothing but its language's standard library, auditable whole, licensed AGPL-3.0.

**8.3** At least two independent witnesses countersigning your records. With fewer, the deployment must label itself a stand-in and not present itself as federated.

**8.4** A covenant your members write — and can change through governance.

**8.5** A legal entity to hold governance, oversee currency compliance, and answer to national authority.

**8.6** Category protocols for whatever the community trades.

**8.7** A staged start for money: begin in escrow — collateralized, no negative balances, no trust extended — and switch to mutual credit only after governance approval, membership notice, and a completed regulatory review.

**8.8** A living open-questions document naming what remains unresolved; a stale one means the project is no longer describing itself honestly.

## 9. The lines that cannot be crossed

A build that crosses any of these is not a smaller JFA stack; it is different software wearing the name.

**9.1** The record is append-only. Forgive harm by annotating; never by erasing.

**9.2** No narratives, no identities in the shared record — structural facts and references only.

**9.3** No central chain. Per-operator logs, countersigned by independent witnesses.

**9.4** Reputation is never one number.

**9.5** Reputation decides whether a member trades on trust; a separate limit decides how much.

**9.6** Credit is earned, never bought, and never redeemable for fiat.

**9.7** Each community's currency is sovereign — no shared unit, no conversion between communities.

**9.8** Value stays home; only truth crosses.

**9.9** Everything is leaveable except the record of what happened — and the record belongs to everyone.

---

*Network Theory Applied Research Institute, Inc. — 501(c)(3) — EIN 92-3047136 — info@ntari.org*

*Software: AGPL-3.0 · Specification: CC BY-SA 4.0*
