# JFA Amendment Proposal — Transport Fee as a Third Sovereign Spend

**Status:** Draft for discussion
**Author:** Jodson, NTARI
**Affects:** Substrate layer (orchestrator tier), Record layer (settlement citation), E&I layer (cross-community trade)
**Invariants touched:** Lines 3–5 (value stays home; cross-community exchange as paired sovereign spends), Line 7 (no identities in the shared record), Line 11 (no single point of failure), Line 12 (records survive any operator)

---

## 1. Problem

The standard defines cross-community trade as two atomic sovereign spends cited into the Record. It is silent on how the orchestrator that carries those spends is compensated. Without a defined mechanism, transport is either unpaid (and therefore unsustainable on prosumer hardware), paid out-of-band (and therefore invisible to the Record and exempt from covenant discipline), or absorbed by operators (recreating the platform-as-intermediary model JFA exists to replace).

## 2. Proposal

Every cross-community settlement carries a **third sovereign spend**: the orchestrator's transport fee. It is escrowed with the trade, released by the same citation that settles the trade, and denominated in the credit of the prosumers whose capacity was transported.

## 3. Normative text (proposed)

### 3.1 Transport is a priced service
An orchestrator SHALL publish transport offers into the substrate market. An offer names a fee, a delivery commitment, and the orchestrator's public key. Offers are not mandatory to accept; any E&I platform MAY select any reachable orchestrator.

### 3.2 The fee is a sovereign spend
The transport fee SHALL be recorded as a sovereign spend in the same manner as the two trade spends. It is drawn against the prosumers party to the trade, since transport is a cost of delivering their value. Per Lines 3–5 it does not cross community boundaries: it settles in the prosumers' home ledger.

### 3.3 Escrow and joint release
All three spends SHALL be escrowed together at trade initiation. The Record SHALL release them under a single citation. No partial release is permitted: if delivery is not attested within the offer's commitment window, all three spends revert.

### 3.4 The orchestrator cannot release its own fee
Release requires delivery attestation from witnesses independent of the orchestrator. The orchestrator's own attestation SHALL NOT count toward the release threshold.

### 3.5 Six-fold witnessing of the earned credit
The orchestrator's earned credit is a record stating, in effect, *"a covenant-compliant value was generated on this network,"* cited by hash. It SHALL carry six witnesses:

1. Public chain
2. Paid witness A (independent operator, network path, and geography)
3. Paid witness B (independent of A and of the orchestrator)
4. Prosumer party A
5. Prosumer party B
6. The operator whose application initiated the trade

Per Line 7, all six SHALL be cited by key. No identity enters the shared record.

### 3.6 Transport is delivery, not execution
The orchestrator's obligation is to deliver signed spends to the witness set and return attestations. It SHALL NOT be relied upon to determine whether a trade occurred. Atomicity is a property of the Record's citation rule, not of transport; orchestrators MAY be lossy and retry-based.

## 4. Rationale

- **Correct incentive.** Fee follows delivery. A failed carry earns nothing.
- **Market discipline.** Because transport is an offer, a dominant orchestrator is undercut rather than regulated. This satisfies Line 11 economically as well as topologically.
- **No hidden intermediary.** The fee is visible in the Record and subject to covenant review like any other spend.
- **Fits prosumer hardware.** Because atomicity lives in the Record, transport tolerates churn, sleep, and CGNAT relay without special handling.
- **Small proof burden.** Proving delivery of a signed payload to independent witnesses is far cheaper than proving compute ran, which keeps the protocol tier within the lean-code principle.

## 5. Consequences for other layers

- **Record:** the settlement citation grows from two spends to three, with a six-witness attestation set on the fee. Citation rule must name all ledgers involved.
- **E&I:** niche platforms need no orchestrator of their own. They publish offers and pay transport out of the trade.
- **Substrate:** orchestrators become the role that multi-homes on transit and holds topology truth (which nodes share a failure domain), since they must prove witness independence.

## 6. Open questions

1. Is the fee a fixed offer, or may it be metered (per byte, per hop, per witness)?
2. If a trade involves prosumers from two communities, is the fee split across both home ledgers or borne by the initiating side?
3. Do paid witnesses A and B earn their own credit under this same six-fold rule, and if so, who witnesses the witnesses without recursion?
4. Should the operator's witness slot (item 6) be mandatory, given operators are insulated from the substrate by design?
5. What is the default commitment window before escrow reverts?

## 7. Failure modes considered

| Case | Outcome |
|---|---|
| One spend delivered, other lost | Citation never fires; all three revert at window expiry |
| Orchestrator forges delivery | Its attestation does not count; threshold unmet; no fee |
| Witness A and B collude with orchestrator | Requires compromising three independent failure domains; mitigated by independence requirement in 3.5 |
| Orchestrator goes offline mid-carry | Retry by same or different orchestrator; original fee reverts |
| Prosumer disputes the fee | Covenant review against the cited record; fee is visible and contestable |
