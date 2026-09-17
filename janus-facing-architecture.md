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

**Institutional Discipline.** Each layer is disciplined by the cost of leaving it — what a member forfeits by walking out, and what a community forfeits by casting someone out. Where leaving is cheap, competition disciplines: the Substrate and Economy & Information layers. Where leaving is dear, members get a vote: the Covenant and Governance layers. Where leaving is impossible, decisions stay open to challenge: the Record layer. Each layer names its own cost below, because that cost is what decides how a fight there gets settled.

**Lean, auditable code.** Protocol software stays small, depends on nothing but its language's standard library, and is auditable whole.

## Substrate Layer

This is the hardware where everything happens, owned by prosumers of CPUs, GPUs, printers, storage and sensors.

Exit here is cheap, and expulsion costs a prosumer nothing but a connection. An orchestrator that refuses to carry your capacity has not taken your hardware, your balances or your history, and another orchestrator is one published offer away. Quarrels at this layer are therefore not adjudicated: a carry that goes unattested inside its commitment window simply reverts, nobody rules on it, and a carrier that expels or fails too freely is undercut rather than appealed to.

### Protocol Tier

Exchanges instructions and orders across a distributed compute/storage market operated on consumer grade computers hosted in homes, offices and storage, as well as repurposed industrial equipment.

Nodes join that market over encrypted overlays and outbound polling, without requiring open inbound ports or a static address; the connection as a residential provider ships it is enough. Line 11 depends on this: a substrate that ran only where a provider permits inbound service would carry a chokepoint at every provider.

### Orchestrator Tier

Federated prosumer compute power creating more options across geography. Orchestrators publish transport offers into the substrate market, each naming a fee, a delivery commitment and a public key; any platform may select any reachable orchestrator, so a dominant carrier is undercut rather than regulated. Transport is delivery, not execution: an orchestrator carries signed spends to the witness set and returns attestations, is never relied upon to determine whether an exchange occurred, and may be lossy and retry-based.

### Frontend Tier

E&I interface for prosuming compute/storage.

## Record Layer

A compensated function of the substrate, recording and serving dialog between E&I and Covenant layers for the public.

The record of what happened is held six ways. Each party to a transaction keeps a record of their own; the operator keeps its own; two witnesses keep their own; and the hashes are committed to one public chain, distributed across the substrate — the record for everyone who was neither transactor, witness, nor operator. The chain is append-only: harm is forgiven by annotation, never by erasing. A platform must have at least two independent witnesses; with fewer, a deployment must label itself unfederated.

Nobody can be expelled from the record, and nobody can leave it. What was committed stays committed, and the hash on the public chain outlives the operator, the frontend and the quarrel. Because there is no exit to hold over anyone, no finding here is ever final: a disputed entry is answered by annotation, and the annotation is as permanent as the entry it answers.

A cross-community exchange remains two sovereign spends. The citation that settles it carries a third: the orchestrator's transport fee, escrowed with the trade at initiation and released by that same citation. Release is joint and all-or-nothing — if delivery is not attested within the offer's commitment window, all three spends revert — and the orchestrator's own attestation does not count toward the threshold that releases its own fee. The fee settles in the home ledger of the prosumers whose capacity was carried; it does not cross a community boundary. The credit it earns is held the same six ways, cited by key.

### Protocol Tier

Captures, categorizes and hashes each transmission within the stack in order to establish reputation through the covenant layer and establishing the basis of an exchange medium through E&I.

### Orchestrator Tier

Federates records across geography enabling shared reputation and exchange. What federation shares is recorded truth — reputation and exchange history — never a currency unit.

### Frontend Tier

Compensated compute/record service provided by prosumers on the substrate layer E&I.

## Covenant Layer

A social contract enforced in code, informing flexible expectations for prosumer interactions.

Exit here is dear. Being cast out of the covenant costs a prosumer the one thing that cannot be rebuilt quickly — the count of exchanges at each rating level, earned one witnessed exchange at a time. That price is why expulsion is adjudicated rather than assumed. When apparent breaches of the covenant occur, platform operators adjudicate between their prosumers; disputes that cross platforms are adjudicated at the witness layer. Adjudicators are rated on their conduct by both prosumers/operators involved — the referees stand inside the reputation system they enforce.

### Protocol Tier

A simple assessment, written in executable code for prosumers to rate interactions with one another across the stack.

### Orchestrator Tier

An API serving compliant assessments across the E&I markets of the stack from substrate prosumers.

### Frontend Tier

The E&I interface where the API is served.

## Governance Layer

This is where and how humans assemble to collaboratively act on the stack.

Exit here is dear, and this is the only layer where expulsion reaches the software itself: a member cast out of the Institute loses the vote that shapes what everyone else runs. So expulsion is never an operator's decision — it is referred and decided by vote under the bylaws, on the record, and the delegates who carry that vote are recallable by the members who seated them.

### Protocol Tier

Nonprofit, copyleft software stewardship organization.

### Orchestrator Tier

Membership in the Network Theory Applied Research Institute, obtained by operating a federated instance of JFA software.   

### Frontend Tier

The synchronous/asynchronous coordination of members governed by the organization's bylaws.

## Economy & Information Layer

The E&I layer is hosted on substrate, syndicated with the record layer, and facilitates covenant compliance.

Exit here is cheap by construction. An operator may bar a prosumer from its platform but not from what they built there: positions and history survive any frontend, so the expelled leave with their record intact and their balances still owed. Expulsion is a loss of market, not a loss of standing — and an operator whose terms or credit limit drive prosumers out loses the trade rather than winning the argument.

### Protocol Tier

Each economic or information platform has a protocol designed for the exchange taking place (i.e. agriculture, a game or research citations). 

### Orchestrator Tier

E&I must run on revokable hardware obtained and recorded by the substrate layer. A platform needs no orchestrator of its own: it selects one from the substrate market and pays transport out of the trade

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
