# JFA Open Questions

The living open-questions document for the Janus Facing Architecture, per the practice carried forward in the [2026-08-24 concept triage](jfa-concept-triage-2026-08-24.md). A stale document here means the project has stopped describing itself honestly. Each entry carries a status and names the constraints it inherits.

Ten entries carry open business: readmission after trust suspension (entry 7, resolved in draft pending adoption of the bylaws amendment, with procedural points open), sybil resistance in the governance franchise (entry 8, priced in draft, its identity half open), residential substrate constraints (entry 9, resolved in draft, its confidential-execution part resolved 2026-10-07), the pricing of the transport fee (entry 10, its split and the operator's attestation resolved in draft), record permanence under paid storage (entry 11, resolved in draft), the public chain's construction and funding (entry 12, funding resolved in draft, construction open), witness adjudication against the operator (entry 13, rule and bench resolved in draft, procedure open), covenant exit and members' records (entry 14), line 9 and capacity (entry 15, pending Act 2), and information-reporting duties before counsel (entry 16, C-9). The rest were resolved as raised; their record follows.

## 1. Contestability

**Status:** resolved (2026-08-24)

The prior spec let any member reopen a decided matter with an observation; that language was judged likely to cause ambiguities. The underlying idea was wanted in different language, and lived for a time in the Governance layer's frontend tier as GOV-reopen. **Superseded (2026-08-27):** assembly, delegation and reopening mechanics were judged bylaws-level detail; the language was removed from the document and GOV-reopen retired from the registry. The idea survives at the bylaws level.

**Inherits:** cost-of-leaving rule; recallable delegates (carried).

## 2. Privacy floor

**Status:** resolved (2026-08-24)

The explicit rule returns as an uncrossable line — line 7: "No narratives, no identities in the shared record — hashes, types, timestamps and references only." Registered as L7.

**Inherits:** public-chain record topology; append-only (line 6).

## 3. Single-account prosumership

**Status:** resolved (2026-08-24)

Not made explicit. One account carrying both producer and consumer roles remains implied by the document's framing — every participant faces both production and consumption — and is not stated as a separate rule.

**Inherits:** the document's Janus/prosumer framing.

## 4. Witness minimum

**Status:** resolved (2026-08-24)

Two independent witnesses minimum. A deployment with fewer must label itself a stand-in and not present itself as federated. Stated in the Record layer; registered as REC-witness-minimum.

**Inherits:** public-chain record topology; no-chokepoint (line 11).

## 5. The hybrid system

**Status:** resolved (2026-08-25)

Line 10 names a hybrid stage between escrow and full mutual credit without defining it. Raised by the dispute-mechanics design; resolved: in a hybrid deployment, escrow and mutual credit operate across the same system, and each prosumer decides which they accept. **Revised (2026-08-27):** the definition now lives in the companion article rather than the document; EI-hybrid retired from the registry.

**Inherits:** escrow start (line 10); zero-sum issuance (line 1).

## 6. Witness assignment

**Status:** resolved (2026-08-25)

Witnesses hold two jobs — record integrity and the neutral bench for cross-platform disputes — but how they attach to an exchange was undesigned. Resolved: witnessing is a function of the substrate, assigned as compute work that prosumers perform and are paid for. Stated in the Record layer; registered as REC-witness-work.

**Inherits:** public-chain record topology; witness minimum (entry 4); cross-platform witness adjudication (COV-witness-adjudication).

## 7. Readmission after trust suspension

**Status:** resolved in draft (2026-08-27)

The dispute-mechanics design lets an adjudicator suspend a member's trust gate — they trade prepaid or collateralized "until the covenant readmits them." Resolved at the instrument level: readmission runs through the governance venue's appeal procedure, drafted as bylaws §2.9 (P1-001 v7.1 draft) — submission to the office of the Vice President with no PII, a one-week rating period in the appropriate Federation Channel where each member of the Vice President's circle may cast one rating on the offense, no readmission on a mode of −1, the Vice President's delegate deciding when no ratings are cast, and resubmission after a one-week cooldown. Banned operators re-enter by the same path. Final resolution follows adoption of the bylaws amendment by the membership.

**Superseded in draft (2026-10-02).** The procedure now stands in bylaws v1.1 §12.5 (draft): submission to the office of the Vice President; a one-week rating period in the concerned federation channel, administered by the office of the President; one rating each, a −1 carrying its comment; ratings, where cast, decide the petition — denied on a mode of −1, granted otherwise — and the federation's delegate decides only where no ratings are cast (principal's decision of 2026-10-02); resubmission after a ten-week cooldown; an appeal of expulsion decided within seven days. Open: (a) a tie for the mode that includes −1; (b) a challenge under §11.4, where the rated offense is the operator's, so that a −1 mode would deny the challenger rather than uphold the challenge; (c) a single rating, even the petitioner's own, now decides; (d) the seven-day limit cannot hold when the decision waits on a one-week rating period; (e) at the end of an expulsion term, no body sets the length of a further term, and the member's vote while the docket is pending is unstated; (f) "the concerned federation channel" is undefined; (g) whether a rating is a vote for §4.5 and §6.5.

**Inherits:** whether-vs-how-much (lines 8-9); trust suspension outcome (jfa-dispute-mechanics.md §4); appeals to governance venue.

## 8. Sybil resistance in the governance franchise

**Status:** open (2026-08-31); priced in draft (2026-10-07), its identity half open

Raised by the bylaws draft's extension of the vote in the Governance Federation Channel to prosumers (§4.2, §4.4). Eligibility is at least one sealed exchange committed to the public chain, which prices a manufactured voter at a real witnessed exchange rather than at nothing. It does not price one high enough: an operator can transact with itself at scale and mint eligible prosumers. The weight of that gap is unusual here because the channel's member roll is expected to stay very small — governance hosting has little reason to replicate beyond redundancy and geography — so the prosumer body is where the weight inside that channel sits, including the election and recall of the Vice President and the disposition of expulsion referrals. How far that weight travels beyond the channel is bounded by the delegate channel, below.

The corpus does not price identity anywhere. Entry 3 settled that one account carries both producer and consumer roles; it did not ask what makes an account a person. The privacy floor cuts against the cheap answers: line 7 forbids the identity data that conventional sybil resistance would want in the shared record, so any solution has to work from structure — counterparties, witnesses, timing — rather than from identity.

Candidate directions, none adopted: witness-attested distinctness at the record layer; a per-platform ceiling on the prosumer votes counted in one ballot; eligibility earned across two or more distinct counterparties rather than one; or an explicit decision that headcount is legitimate weight in this channel and that the immediate recall of §6.8 is the whole answer.

**Bounded by the delegate channel (2026-08-31).** A federation's vote is channeled into its one delegate, so a manufactured prosumer body does not scale into Institute-wide weight: a billion prosumer members behind a single governance host still produce one Governance delegate, against the four seated by the operator and orchestrator federations. Headcount inside a federation buys influence over that federation's delegate and nothing beyond it, which is why the operating roll stays the more influential body even as the prosumer roll grows without bound.

What the gap can still reach is the Governance delegate itself, and with it the office of the Vice President and the disposition of expulsion referrals — the powers of Article XII rather than the powers of the membership. The bylaws draft also puts the amendment of the bylaws themselves within prosumer-member reach (bylaws §15.1), which is the one place the gap touches the structure rather than an office; whether that vote is cast directly or channeled through delegates is unsettled in the draft and is the open half of this question. The immediate recall of §6.8 is the standing check, and it is exercised by the same roll a sybil attack would have captured — which is the part that does not resolve itself.

**Priced in draft (2026-10-07).** The Act 1 amendment prices the franchise where the bylaws widen it. Recognition under §3.8 requires sealed exchanges with at least two distinct counterparties, which only doubles the price of a manufactured voter but stops the simplest pairs. §6.5 strikes the Governance federation's operating-member floor and puts a concurrent platform majority in its place for any federation with prosumer members: a matter carries only with a majority of the votes cast and a majority of the platforms whose prosumer members cast votes, each platform's position being the majority of its own prosumer members' votes — one member keeps one vote, operators lose a veto by abstention, and the price of capture moves from accounts to federated instances, each with independent witnesses of its own. §16.3 counts a Covenant or Governance federation toward the end of bootstrap only when its prosumer members come from at least two federated platforms run by different operators. §3.9 holds a member recognized again within a year of its lapse to the federation it held, closing the switch-by-lapse path. Under the federation election the prosumer-elected delegates reach two of five — the Covenant and Governance seats — which is what the platform majority now disciplines; the delegate paragraph above counted one of five before the election was seated. The §15.1 half is settled by its own text: every member of each federation votes within the federation, and the delegates carry the federations' decisions. What stays open is identity itself: the corpus still prices an account, not a person, and witness-attested distinctness remains undecided.

**Inherits:** privacy floor (line 7, entry 2); platform-scoped non-portable identifiers (bylaws §9.10(f)); one member, one vote (bylaws §3.4); recallable delegates, one per federation (bylaws §5.3); witness minimum (entry 4).

## 9. Residential substrate constraints

**Status:** resolved in draft (2026-09-08); part (c) resolved in draft (2026-10-07)

Raised by the Vice President in the board's September 2026 review of the official document: as a governance and system-specification instrument, the document does not address three physical risks of running substrate on consumer broadband — (a) residential connections carry dynamic addresses, sit behind carrier-grade NAT, and come with terms of service that bar inbound servers; (b) home bandwidth is asymmetric and capped, so heavy container layers and large datasets do not move well; (c) a host operator has physical possession of the machine and can read its memory, and consumer hardware carries no confidential-execution feature to prevent it.

Decided: carrier constraints are treated as a physical, adversarial environment to be routed around in code, not a legal condition to be negotiated away. Lobbying may proceed as a civic matter but is never a dependency of the architecture. Routed at three levels. (a) Resolved in the document — the Substrate protocol tier now states that nodes join the market over encrypted overlays and outbound polling, without requiring open inbound ports or a static address, as the residential case of line 11; registered as SUB-no-inbound-requirement, implementation-bound. The reference protocol already has this shape: its node-side operations poll for work rather than listen. (b) Resolved by design posture in the substrate whitepaper ([P1-004](P1-004_Substrate-Constraints_v0.1.md)): protocol traffic is small by construction under line 7, work ships as sandboxed WebAssembly modules rather than container images, and jobs are spooled locally so a poor uplink delays work rather than losing it. (c) Open: the whitepaper argues for redundant execution across independent hosts with covenant-rated disagreement, plus data minimization, in place of any hardware-enclave requirement, and for attestation as an optional, rated, market-priced capability. Whether that position becomes a registered invariant (a candidate SUB-redundant-execution) is for the board under bylaws §9.16; until then it is argued, not bound. A residual legal question stands with it: whether compensated participation on a residential line engages the non-commercial prong of typical acceptable-use policies, which counsel should review beside the CHC pilot's business-use insurance question.

**Part (c) resolved in draft (2026-10-07).** The whitepaper's position is now the document's. The Substrate protocol tier states that substrate work is integrity-assured, not confidentiality-assured — a host can read what its node computes — and that work whose result settles a spend or enters the record runs on at least two independent hosts, their disagreement rated, never trusted; registered as SUB-redundant-execution, implementation-bound. The Economy & Information protocol tier now assumes the same of every host. Whoever enrolls a prosumer as a substrate host discloses both facts before enrollment (bylaws v1.1 §10.3, per P1-004 §5). The residual legal question moves to the counsel items of entry 16.

**Inherits:** no-chokepoint (line 11); privacy floor (line 7, entry 2); lean, auditable code (P-lean-code); witnessing as compensated substrate work (REC-witness-work, entry 6); document-amendment procedure (bylaws §9.2, §9.16); bootstrap recording (bylaws §16.1).

## 10. Pricing the transport fee

**Status:** open (2026-09-11); the split resolved in draft (2026-10-01); the operator's attestation resolved in draft (2026-10-07)

The Record layer now cites a third sovereign spend — the orchestrator's transport fee — escrowed with the trade and released by the same citation. That much is settled: the fee follows delivery, the orchestrator cannot release its own, and it settles in the home ledger so no value crosses a community boundary. What the fee *is* remains open.

Whether it is a fixed offer or may be metered per byte, per hop or per witness. A fixed offer is legible and cheap to verify; metering prices a long carry honestly but gives the orchestrator a quantity it reports about itself, which is the shape the six-fold witnessing exists to avoid.

Whether a trade between prosumers of two communities splits the fee across both home ledgers or charges the initiating side. Splitting spreads the cost the way the benefit falls; charging the initiator keeps one settlement in one ledger and avoids a second escrow that can fail independently. **Resolved in draft (2026-10-01):** both home ledgers split the fee, each prosumer paying their share in their own unit; the official document's Record layer now says so, and stops counting spends: if delivery is not attested, every spend reverts.

Whether the paid witnesses earn credit under this same six-fold rule, and if so who witnesses them. Applied naively the rule recurses without bottom. Either witnessing is compensated substrate work already covered by the existing record-layer provision, or it needs a terminating case that has not been written.

Whether the operator's witness slot is mandatory, given operators are insulated from the substrate by design. An operator that must attest to a carry it cannot observe is either rubber-stamping or reaching into a layer the architecture keeps it out of. **Resolved in draft (2026-10-07):** the operator holds no attestation slot — the Record layer now says delivery is attested by the witnesses alone, and the operator keeps its record of a carry and never attests to one.

What the default commitment window is before escrow reverts. Too short and prosumer hardware with churn, sleep and relay fails honest carries; too long and capacity sits escrowed against a carry nobody will complete.

**Inherits:** value stays home and cross-community exchange as paired sovereign spends (lines 3–5); privacy floor (line 7, entry 2); no chokepoint (line 11); witness minimum (entry 4); witnessing as compensated substrate work (entry 6).

## 11. Record permanence under paid storage

**Status:** resolved in draft (2026-10-01)

Record permanence is bounded by paid storage. The record layer is compensated for its storage, so each holder's copy — prosumer, operator, witness, orchestrator — lasts as long as its bill is paid and ends with that holder's death or insolvency. Automation may extend some copies, but plausibly none lasts more than a few hundred years. The official document says what was committed "stays committed" (Record layer), and the dispute-mechanics design says defaults are "Recorded forever" (§5). Raised by the principal on 2026-09-30 as not necessarily a defect; the wording should match the mechanism.

**Resolved in draft (2026-10-01):** the official document's Record layer now says that nothing is erased but no single copy is the record, names each copy's lifetime — the orchestrator's with the last paid carry, the witnesses' while the operator pays them, the parties' own until they stop keeping them, the chain's while its storage is funded — and claims for the chain only what its funding supports; the dispute-mechanics design's "Recorded forever" is reworded to match. Who funds the chain, and for how long, is settled under entry 12.

**Inherits:** append-only record (line 6); positions and history survive any frontend (line 12); six holders (REC-six-holders); record-keeping as compensated substrate work (REC-witness-work, entry 6); defaults annotated, never erased (dispute-mechanics design §5).

## 12. The public chain: construction, funding and lifetime

**Status:** funding resolved in draft (2026-10-01); construction open

The corpus fixes the chain's topology — one append-only sequence of salted hashes, types, timestamps and references, distributed across the substrate, serving everyone who holds no record of their own, and binding cross-community spends (line 5) — but not its construction: how entries are ordered, who may append, how append rights are rationed, and what happens under partition are in none of the official document, the registry, the dispute-mechanics design or this record. The Record curriculum article names the gap and makes the construction decision the Record group's first deliverable. Nor did the corpus say who pays for the chain's storage or how long it lasts: the Record frontend tier makes storage a market, "compensating the prosumers who keep the record", without naming the buyer.

Decided by the principal on 2026-10-01: the commitments of every exchange carried by an orchestrator are copied to the chain and stored on substrate that the stewardship organization of the Governance layer funds — in NTARI's instance, the Institute, under bylaws §9.19 — so that the record which binds communities to one another is paid for by none of them. The official document's Record layer now says so, and claims for the chain only the lifetime its funding supports.

Open: (a) construction, within line 11 (no chokepoint), line 7 (no identities) and P-lean-code — the Byzantine-agreement setting the curriculum article lays out; (b) how the Institute buys substrate storage without holding credit (bylaws §9.7) — whether the storage market takes exogenous money for this service, or the Institute funds the buyers; (c) what the funding must look like to satisfy bylaws §13.1 and §13.3 — the entries are also held by the six parties and any other party may fund storage of the same chain, so the Institute's withdrawal must cost the record nothing; (d) resolved (2026-10-02): commitments of exchanges no orchestrator carries are stored by no one, because a frontend that is not federated is not a member; the bylaws draft no longer assigns them.

**Inherits:** cross-community exchange bound by the chain (line 5); append-only (line 6); privacy floor (line 7, entry 2); no chokepoint (line 11); public-chain record topology (REC-public-chain); lean, auditable code (P-lean-code); the Institute's money is not the federation's (bylaws §9.7); self-binding and succession (bylaws §13.1, §13.3); sybil resistance (entry 8); record permanence (entry 11).

## 13. Witness adjudication against the operator

**Status:** rule resolved in draft (2026-10-02); the bench resolved in draft (2026-10-07); procedure open

Decided by the principal on 2026-10-02: a dispute between a prosumer and the operator of its own platform is ruled on by witnesses, never by the operator. The official document's Covenant layer and bylaws §10.9 now say so, and the dispute-mechanics design's §3 carries the case. An earlier draft's third witness, drawn at random for each dispute so the bench would be odd and partly unknown to the operator in advance, was not carried; it rests on undecided rules for witness independence and the witness draw.

Raised by the verification of that decision and open: (a) neutrality — the witnesses are paid by the operator they now judge, their copies of the record last while it pays them, and it rates them as a party, so the bench's pay, evidence and part of its reputation sit with the respondent; "independent" is nowhere defined; (b) a split bench — the minimum bench is two and nothing says what a one-to-one split yields; (c) filing — the design gives standing to record holders of an exchange and its filing commitment references an exchange, but custody, the credit limit and Article X duties need not involve one; (d) the dispute window — under bylaws §10.5 the operator's own rules set it for disputes against itself; (e) execution — the operator runs the ledger and executes every remedy, including one against itself, with no stated consequence if it does not; (f) forum — a prosumer contesting its own operator's switch to mutual credit is sent both to the witnesses (§10.9) and to the federation's ratings (§11.4, §12.5); (g) recusal — nothing stops a party from rating or voting on its own referral or petition in a federation; (h) discipline — witnesses are rated, but no text gives those ratings any effect on assignment.

**The bench resolved in draft (2026-10-07).** The rules the dropped third witness waited on are decided in the Act 1 amendment. Independence is defined (bylaws v1.1 §3.10): not the operator, not under common ownership or control with it, holding no interest in it, and not a prosumer of the platform; a party is ineligible for any draw while the mode of its adjudication-conduct ratings is −1, which also gives the conduct ratings their first effect on assignment — answering (h). The draw is seeded from a public-chain block hash so anyone can verify it, and the operator pays the substrate market, which assigns and pays the witnesses, so the bench's pay no longer sits with the respondent — answering (a); registered as REC-witness-draw (lineage REC-witness-work). Standing seats are staggered two-year terms, one redrawn each March equinox, so a platform always keeps one witness who saw its history. The drawn third seat returns as the only neutral tie-break: a split bench is answered by a witness drawn for the dispute alone, paid only when a dispute arises — a bench of three for a dispute with one's own operator, five across platforms — answering (b). Still open: (c) filing without an exchange, (d) the dispute window where the respondent's own rules set it, (e) execution of a remedy against the operator, (f) the forum overlap between §10.9 and §11.4, and (g) recusal.

**Inherits:** cross-platform witness adjudication (COV-witness-adjudication, entry 6); witness minimum (REC-witness-minimum, entry 4); witnessing as compensated substrate work (REC-witness-work); witness assignment by verifiable draw (REC-witness-draw); adjudicators rated (COV-adjudicators); escrow custody disclosed (bylaws §10.2 Custody); line 10.

## 14. Covenant exit and members' records

**Status:** open (2026-10-07)

The August correction gave each layer its exit cost, and the document now prices leaving the covenant for a member. What it does not reach: whether a community that leaves the covenant may federate with its members' records. The records survive any operator (line 12) and what crosses communities is recorded truth (line 4), but no text says whether a departed community's instance — no longer conformant, no longer recognized — can carry its members' histories into a new federation, or what a member's standing in that history is when the community that held it has left the covenant behind.

**Inherits:** exit costs by layer (Principles); value stays home, only truth crosses (line 4); positions and history survive (line 12); conformance and the name (bylaws §9.6).

## 15. Line 9 and capacity

**Status:** open (2026-10-07), pending Act 2 of the amendment plan; contested

Line 9 sizes credit with one community-wide limit, set by the operator and never derived from reputation. The durable mutual credit systems the follow-up research examined size credit by capacity, which a single number cannot: it holds the members who supply the most to the same ceiling as those who supply the least. Act 2 of the amendment plan proposes a community-wide rule in place of the single number — one published formula applied to everyone, reading only record structure on the same platform, capped at a published multiple of a base limit, the extension at the operator's election. Contested: colluding members can trade in a ring to inflate volume, where a single number cannot be gamed at all; the proposal answers with the cap, the trailing window, the fees on every exchange, and the published default rate. Nothing moves until Act 2's deliberation.

**Inherits:** whether-vs-how-much (lines 8–9, L9); community-wide limit (bylaws §10.2 Credit Setting, §9.10(e)); defaults annotated and the rate published (bylaws §10.2).

## 16. Information-reporting duties (counsel item C-9)

**Status:** open (2026-10-07), with counsel

Line 2 keeps credit unredeemable; it does not put an operator outside information-reporting law. In the United States, a platform on which members trade with one another may be a barter exchange, and barter exchanges report members' transactions on identified forms. Line 7 bars identity from the shared record, not from an operator's own erasable records, so the two can coexist: any such duty is met from the operator's own records, never by placing identity in the shared record. Sent to counsel as C-9, beside C-4 on custody and money transmission, together with the residential acceptable-use question of entry 9 and the heat-and-compute pilot's insurance questions. This is a question for counsel, not a legal finding; the duty is adopted with counsel's reading (amendment plan, Act 2 item 2.3).

**Inherits:** credit never redeemable (line 2); privacy floor (line 7, entry 2); operator duties (bylaws §10.2); the Institute's money is not the federation's (bylaws §9.7).
