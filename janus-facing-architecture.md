# JFA: Janus Facing Architecture

## Introduction

Janus Facing Architecture — named for the Roman god who looks in two directions at once, just as every economic participant faces demands for both production and consumption — allows communities to address the economic reality of prosumership. Every member of an economy is not just a consumer, but a prosumer (Toffler, 1980), simultaneously producing something of value even if all they have to offer is time. It also provides an option to transform the issuance model from exogenous, chartal money (issued by an authority outside the community) to endogenous mutual credit (issued by members to one another as they transact).

The name's second face is political. Acemoglu and Robinson (2019) show that liberty survives only inside a narrow corridor where a capable state — the Leviathan — is matched by a society equally capable of checking it. Outside the corridor the Leviathan takes its other forms: absent, and coordination fails; despotic, and the coordinator dominates the coordinated; paper, and the checks exist in writing but not in effect. Staying inside the corridor demands what they call the Red Queen effect: state and society running together, each growing capacity because the other does. Every economic platform is a Leviathan in miniature — it coordinates, enforces and records — and today's dominant platforms are despotic by construction, evolving at network speed while the institutions meant to check them move at the speed of meetings.

NTARI's research locates this failure in infrastructure itself. Deliberative systems are material culture: a platform's architecture materializes a theory of who may know and who may decide, and the prevailing broadcast architectures treat participants as passive recipients (NTARI, 2025b). The resulting velocity gap is structural — information moves at network speeds while democratic synthesis stays locked to electoral cycles synched by a postal clock (NTARI, 2025a). JFA is built to close that gap from inside: the community that coordinates is the community that checks, the two capacities exchanged continuously in the same software at the same speed, disciplined layer by layer by the cost of leaving. It is a shackled Leviathan in code.

The Janus Facing Architecture (JFA) is organized into five functional layers — Substrate, Record, Covenant, Governance, and Economy & Information (E&I) — each implemented in three tiers: the frontend — for prosumer collaboration; the orchestrator — a backend providing overlapping coordination across geographic communities; and the underlying protocol — the pattern for securely handling data across tiers.

JFA software is designed for release and management in a copyleft environment, generally the GNU Affero General Public License, allowing new frontends, federations, protocols and architectures to evolve in the global market, forming a free software commons. 

This is the official document, stewarded by Network Theory Applied Research Institute, Inc. Prior instruments are preserved in [Historical Docs](Historical%20Docs/); concepts carried from them are recorded in the [concept triage](jfa-concept-triage-2026-08-24.md); what remains unresolved is named in [OPEN-QUESTIONS.md](OPEN-QUESTIONS.md).

## Principles

**Shared Responsibility.** The community that coordinates the economy is the same community that checks the coordination. The two functions are exchanged continuously — never split into rulers and ruled.

**Institutional Discipline.** Each layer is disciplined by the cost of leaving it: where leaving is cheap, competition disciplines; where leaving is dear, members get a vote; where leaving is impossible, decisions stay open to challenge.

**Lean, auditable code.** Protocol software stays small, depends on nothing but its language's standard library, and is auditable whole.

## Substrate Layer

This is the hardware where everything happens, owned by prosumers of CPUs, GPUs, printers, storage and sensors.

### Protocol Tier

Exchanges instructions and orders across a distributed compute/storage market operated on consumer grade computers hosted in homes, offices and storage, as well as repurposed industrial equipment.

### Orchestrator Tier

Federated prosumer compute power creating more options across geography.

### Frontend Tier

E&I interface for prosuming compute/storage.

## Record Layer

A compensated function of the substrate, recording and serving dialog between E&I and Covenant layers for the public.

The record of what happened is held six ways. Each party to a transaction keeps a record of their own; the operator keeps its own; two witnesses keep their own; and the hashes are committed to one public chain, distributed across the substrate — the record for everyone who was neither transactor, witness, nor operator. The chain is append-only: harm is forgiven by annotation, never by erasing. A platform must have at least two independent witnesses; with fewer, a deployment must label itself unfederated. 

### Protocol Tier

Captures, categorizes and hashes each transmission within the stack in order to establish reputation through the covenant layer and establishing the basis of an exchange medium through E&I.

### Orchestrator Tier

Federates records across geography enabling shared reputation and exchange. What federation shares is recorded truth — reputation and exchange history — never a currency unit.

### Frontend Tier

Compensated compute/record service provided by prosumers on the substrate layer E&I.

## Covenant Layer

A social contract enforced in code, informing flexible expectations for prosumer interactions.

### Protocol Tier

A simple assessment, written in executable code for prosumers to rate interactions with one another across the stack.

### Orchestrator Tier

An API serving compliant assessments across the E&I markets of the stack from substrate prosumers. When apparent breaches of the covenant occur, platform operators adjudicate between their prosumers; disputes that cross platforms are adjudicated at the witness layer. Adjudicators are rated on their conduct by both prosumers/operators involved.

### Frontend Tier

The E&I interface where the API is served.

## Governance Layer

This is where and how humans assemble to collaboratively act on the stack.

### Protocol Tier

Nonprofit, copyleft software stewardship organization.

### Orchestrator Tier

Membership in the Network Theory Applied Research Institute, obtained by operating a federated instance of JFA software.   

### Frontend Tier

The synchronous/asynchronous coordination of members governed by the organization's bylaws.

## Economy & Information Layer

The E&I layer is hosted on substrate, syndicated with the record layer, and facilitates covenant compliance.

### Protocol Tier

Each economic or information platform has a protocol designed for the exchange taking place (i.e. agriculture, a game or research citations). 

### Orchestrator Tier

E&I must run on revokable hardware obtained and recorded by the substrate layer

### Frontend Tier

Frontend designs for E&I platforms must be customizeable by the user. 

## The Lines That Cannot Be Crossed

A build that crosses any of these is not a smaller JFA; it is different software wearing the name.

1. Money is created at the moment of exchange — one balance down, one up, always summing to zero.
2. Credit is earned, never bought, and never redeemable for fiat.
3. Each community's currency is sovereign — no shared unit, no conversion between communities.
4. Value stays home; only truth crosses.
5. Cross-community exchange is two sovereign spends bound atomically by the public chain — no clearer, no exchange rate.
6. The record is append-only — forgive harm by annotating, never by erasing.
7. No narratives, no identities in the shared record — hashes, types, timestamps and references only.
8. Reputation is never one number — what others see is the count of exchanges at each rating level.
9. Reputation decides whether a member trades on trust; a community-wide limit, set by the operator and never derived from reputation, decides how much.
10. A deployment begins in escrow — collateralized, no negative balances, no counterparty credit extended — and switches to a hybrid or full mutual credit system only after the operator builds capacity, the prosumer network is notified, and the local authorizations to provide mutual credit services are published to the governance layer — or, where the jurisdiction requires none, a finding to that effect is published there instead.
11. No single host, account, or vendor whose removal could stop the network.
12. A member's positions and history survive any frontend; a community's records survive any operator.

## References

Acemoglu, D., & Robinson, J. A. (2019). *The Narrow Corridor: States, Societies, and the Fate of Liberty*. Penguin Press.

Network Theory Applied Research Institute. (2025a, October). *Addressing democratic information velocity* (P1-002). https://www.ntari.org/post/ntari-whitepaper-addressing-democratic-information-velocity

Network Theory Applied Research Institute. (2025b, June). *The material culture of democratic deliberation*. https://www.ntari.org/post/the-material-culture-of-democratic-deliberation

Toffler, A. (1980). *The Third Wave*. William Morrow.

---

*Network Theory Applied Research Institute, Inc. — 501(c)(3) — EIN 92-3047136 — info@ntari.org*

*Software: AGPL-3.0 · Specification: CC BY-SA 4.0*
