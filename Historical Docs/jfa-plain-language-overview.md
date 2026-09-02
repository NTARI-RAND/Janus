# Janus-Facing Architecture: A Plain-Language Overview

*This document explains the architecture; it never governs it. The normative instrument is [janus-facing-architecture.md](janus-facing-architecture.md); where the two differ, the instrument wins.*

## Introduction

Each layer of the Janus-Facing Architecture contains three tiers: the protocol — encoding the layer's most important socioeconomic data; the orchestrator — a backend providing federation service across diverse frontends; and the frontend — where members produce and consume simultaneously.

The entire JFA software stack is licensed under the GNU Affero General Public License, and the specification is free documentation in the same copyleft commons, allowing new frontends, federations, protocols and architectures to evolve in the global market.

## Substrate Layer

This is the hardware where everything happens, owned by prosumers of CPUs, GPUs, printers, storage and sensors.

**Protocol Tier.** Encodes instructions and orders across a distributed compute/storage market operated on consumer-grade computers hosted in homes, offices and storage.

**Orchestrator Tier.** Federates frontend operator communities competing on accessory features and regional/cultural optimization but otherwise sharing work across the same global market.

**Frontend Tier.** Market operated on the substrate protocol, translating supply and demand across the prosumer market.

## Record Layer

This is the distributed, immutable record of the dialogs that resulted in rated exchanges.

**Protocol Tier.** Encodes pre-to-post transaction dialog between prosumers. The dialog itself stays local to the parties' own interfaces; only structural facts — hashes, types, timestamps, exchange references — enter the shared record. The commons never carries narratives or identities. Each exchange is a dialog, sealed only when complete and quiescent; disputes follow the claim lifecycle — file, adjudicate, resolve, seal. This tier is the append-only journal of the stack's economy: all Economy & Information ledger state must be replayable from sealed records.

**Orchestrator Tier.** The backend of the record network. Each operator keeps its own append-only log and regularly publishes a signed checkpoint of it to independent witnesses, who countersign it. There is no central chain: an operator showing two different histories becomes provable, not prevented. Every step of a dispute — filing, adjudication, resolution, seal — is committed to the record as it happens, and a claim's filing is committed at a witness independent of the operator who will adjudicate it.

**Frontend Tier.** A program available for substrate compute providers that audits records published by frontends and the JFA stack against those in the Record.

## Covenant Layer

The social contract enforced in code, guaranteeing expectations in prosumer interactions.

**Protocol Tier.** A quick assessment written into code, gated by transaction, governing prosumer behavior by encoding reputation from previous interactions. Reputation is carried as the full distribution — the count at each rating level — never averaged into a single score, and it gates whether a member transacts on trust, never how much.

**Orchestrator Tier.** An API issuing compliant assessments and recording prosumer ratings across the markets of the stack.

**Frontend Tier.** The prosumer/operator communities of the stack can change the covenant using the governance layer.

## Governance Layer

This is where and how humans assemble to collaboratively act on the stack.

**Protocol Tier.** An appropriate legal entity to govern members, plan and document work, oversee currency compliance and submit to national authority.

**Orchestrator Tier.** Platform for synchronous and asynchronous coordination of the activities of members.

**Frontend Tier.** Open circles any member may join, electing recallable delegates. Decisions stay contestable — any member can reopen a decided matter with an observation — and the venue itself runs on substrate members can leave, so no host's goodwill is a condition of self-government.

## Economy & Information Layer

**Protocol Tier.** Programs in the E&I layer keep the same tier structure as the others, but this is also where protocols are developed for specific products, services and information categories. All category protocols share the stack's accounting grammar: mutual credit. Money is created at the moment of exchange — one balance down, one up, always summing to zero — issued only for value provided, gated by the covenant, and capped by a separate limit. Credit is earned, never bought, and never redeemable for fiat. Ledger state must at all times equal a replay of the sealed Record — the mirror requirement, enforced by the Record layer's frontend auditors.

**Orchestrator Tier.** The E&I orchestrator lets operators provision substrate for records and processing, adjudicate covenant breaches, and interact with their governance federation. Adjudicating operators are rated on their adjudication conduct by both prosumers involved. Each frontend operator community runs its own mutual credit ledger in its own sovereign unit; because ledger state mirrors the Record, orchestrators hold no hostage-able state — a failed or defecting operator is replaced by replaying sealed records, preserving prosumer credit positions. Value stays home; only truth crosses: cross-community exchange is two sovereign spends bound atomically by a witnessed proof — no shared unit, no central clearer, no exchange rate. A community may, by its own governance act, read a newcomer's witnessed history from another network and extend them local credit — recorded truth travels; money never does.

**Frontend Tier.** Wallets and marketplaces where prosumers hold balances, publish offers against category protocols and initiate transactions. Frontends compete on accessory features atop the same ledger API; per the stack's exit commitment, a prosumer's positions and history are carried by the Record and survive any frontend.
