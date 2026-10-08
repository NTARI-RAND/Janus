# JFA Dispute Mechanics — Design

*Adopted 2026-08-25; revised 2026-10-07 to carry the September–October amendments: six record holders with the orchestrator, witness adjudication against one's own operator, and the witness draw. Subordinate to the official document ([janus-facing-architecture.md](janus-facing-architecture.md)); where the two disagree, the official document governs. Decisions recorded here were made by NTARI stewardship; the constraints each part inherits are cited by suite registry ID.*

## 1. The frame: operator responsibility, market discipline

Responsibility for managing each platform's economy and information exchange rests on its **operator**. The operator runs the ledger, adjudicates covenant breaches between its prosumers, executes remedies, annotates defaults, sets its community-wide credit limit (L9), and publishes its economy's trailing default rate. Apart from the limit, which the official document binds in line 9, these economic-management duties are bylaws-level obligations: the 2026-08-27 revision moved them out of the official document and into the governing bylaws.

The checks on the operator are not institutional routing but the architecture's own market machinery:

- Every filing lands on the public chain the moment it is made, so a complaint can never be quietly buried at intake.
- Every adjudication is rated by the parties to it (COV-adjudicators), and those ratings accumulate into a **publicly displayed adjudication reputation** — shown as the count of outcomes at each rating level, never one number (L8 applies to operators too).
- Leaving an operator is cheap, so competition disciplines (the cost-of-leaving principle): prosumers weigh an operator's adjudication reputation, credit limit, and default rate when choosing where to trade.

## 2. Filing

**Who may file.** Any record holder of the exchange: either transactor, the operator, the orchestrator, or a witness. (A witness who spots tampering can file; a stranger to the exchange cannot.)

**What lands on the chain.** Two commitments, and only two: the **filing** (at the moment it is made) and the **resolution** (when decided). Each is structural facts and hashes only — exchange reference, dispute type, timestamps, party references, and the salted hash of the underlying material (L7: no narratives, no identities). The story — evidence, statements, the dialog itself — stays in the six holders' own records: the two prosumers, the operator, the orchestrator, and the two witnesses.

**When.** Each E&I category protocol sets its own dispute window — produce disputes close in days; research-citation disputes may stay open for years. Where a category protocol is silent, the operator's platform rules set the default window, consistent with the operator-responsibility frame.

## 3. Adjudication

**Same platform.** The platform operator adjudicates between its prosumers (COV-operators-adjudicate).

**Cross-platform.** When the transactors are on different platforms, the dispute is adjudicated at the **witness layer**: the independent witnesses who hold records of the exchange decide it (COV-witness-adjudication). This is one reason the two-witness minimum (REC-witness-minimum) is load-bearing — witnesses are not only integrity checks but the neutral bench for disputes no single operator should judge.

**Against one's own operator.** A dispute between a prosumer and the operator of its own platform is adjudicated by that platform's witnesses; no operator adjudicates a dispute to which it is a party (in NTARI's instance, bylaws §10.9).

**Witness assignment.** Witnessing is a function of the substrate: it is assigned as compute work through the substrate market, and the prosumers who perform it are paid for it (REC-witness-work). Standing witnesses are assigned by a draw seeded from a public-chain block hash, so anyone can verify the assignment, and are paid by the substrate market, never by the operator they observe: the operator pays the market for witnessing as a service, and the market assigns and pays the witnesses (REC-witness-draw). Each standing seat is held for two years; the two seats are staggered so that one is redrawn each March equinox, and a platform always keeps one witness who saw its history. A witness must be independent of the platform it observes — not the operator, not under common ownership or control with it, holding no interest in it, and not a prosumer of the platform — and is ineligible for any draw while the mode of its adjudication-conduct ratings is −1 (in NTARI's instance, bylaws §3.10). A witness's neutrality comes from the assignment being verifiable substrate work rather than a party's choice.

**The bench.** A dispute between a prosumer and the operator of its own platform is heard by three: the platform's two standing witnesses and a third witness drawn for the dispute alone, by the same verifiable draw, paid through the market only when a dispute arises. A dispute that crosses platforms is heard by five: the two standing witnesses of each platform and one drawn seat. The drawn seat is the only neutral tie-break a split bench has — every default except a fresh draw favors one side, since the operator is the respondent and holds the funds — and rotation changes who witnesses, never how many.

**Rating the adjudicator.** Wherever adjudication occurs, the parties to it rate the adjudicator: between its own prosumers, the operator; across platforms or against the operator, the witnesses. The rating enters the adjudicator's public distribution like any other covenant assessment.

## 4. Outcomes

All outcomes land as **annotation, never erasure** (L6). Four remedies are available:

1. **Rating annotation** — the disputed exchange's rating is corrected or contextualized on the record. The baseline remedy. Final.
2. **Restitution** — a compensating mutual-credit transfer from the party at fault, within the community-wide limit; in escrow, restitution is made from the held escrow (below). Final.
3. **Trust suspension** — the trust gate closes for the party at fault; they trade prepaid or collateralized until the covenant readmits them. Appealable.
4. **Expulsion referral** — for grave breaches, the adjudicator refers expulsion to the governance layer. Expulsion suspends a member's vote for a bounded term; operators and witnesses never expel, only governance does. Appealable.

An operator's **bar** — ending a prosumer's activity on its own platform — is not a remedy of adjudication. It rests on at least three adjudicated −1 ratings, attached as evidence (in NTARI's instance, bylaws §12.3(b)).

**In escrow.** Where a deployment operates in escrow, a −1 rating on an exchange holds that exchange's escrow for adjudication. The adjudication may return all or part of the amount to the consumer, deliver all or part of the payment to the producer, or divide it between them. Whoever adjudicates is rated on the adjudication, and an operator adjudicating between its own prosumers receives its payment regardless of outcome. Where the operator is itself a party, the platform's witnesses adjudicate (§3).

**Appeals.** Annotation and restitution are final — the adjudicator's public rating is the check. Trust suspension and expulsion referral may be appealed to the governance venue, under the procedure the governing instrument provides. (In NTARI's instance, bylaws §12.5 governs, including its ten-week cooldown before resubmission.)

## 5. Defaults and the hole

In mutual credit, a member who leaves with a negative balance leaves a hole: live claims in the community now exceed live promises. The design handles it by containment and visibility, not pretense:

- **Recorded, never erased.** The defaulted balance stands on the chain, annotated, never erased, for as long as the chain's storage is funded and any holder keeps a copy. Its truth follows the member wherever recorded truth travels.
- **Annotated by kind.** *Deceased*, *departed*, *adjudicated*, or *unknown* — a death carries no reputational meaning; a walk-away is signal. Same permanence, different meaning.
- **Capped.** The community-wide limit (L9) — one number for everyone, set by the operator, never derived from reputation — is precisely the most any single member's disappearance can cost the community.
- **Measured as a flow, not a stock.** The operator publishes the **trailing default rate**: dead credit created over a recent rolling window, as a share of trade volume. A cumulative tally grows scarier every decade while meaning less; the rate stays comparable forever and is the dial-reading an operator uses to tune the limit. It is the community's inflation gauge, and — published — part of how operators compete.
- **No architectural levy.** No reserve or insurance is required at the architecture level. A community that wants to mutualize default losses may build a reserve in its own covenant; currencies are sovereign, so the choice stays home.

## 6. Record protocol requirements

Two schema requirements fall out of this design:

- **Dispute commitments.** The Record protocol carries two dispute commitment types — filing and resolution — each holding structural facts and hashes only, referencing the disputed exchange.
- **Salted hashes.** Every transmission is hashed with a random salt held in the parties' own records. Hashes are one-way, but a short, predictable transmission (a rating, a price) could otherwise be guess-matched against the public chain by hashing likely candidates; the salt makes every public hash unguessable. Verification is unchanged: a holder produces content plus salt, and anyone can check the pair against the chain.

## 7. Registry hooks

Suite IDs binding this design: COV-operators-adjudicate, COV-witness-adjudication, COV-adjudicators, L6 (annotation), L7 (structural facts only), L8 (distribution display), L9 (operator-set limit), REC-witness-minimum, REC-six-holders, REC-public-chain, REC-witness-work (assignment as compensated substrate work), REC-witness-draw (the verifiable draw; the market pays, never the operator observed). (Operator economic management beyond the limit is a bylaws-level obligation as of 2026-08-27 and no longer carries a registry ID.) Implementation test suites for a record, covenant, or economy repo should cite these IDs; until they do, conformance with this design is self-attested.

---

*Network Theory Applied Research Institute, Inc. — info@ntari.org*
