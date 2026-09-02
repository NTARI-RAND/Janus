# JFA Open Questions

The living open-questions document for the Janus Facing Architecture, per the practice carried forward in the [2026-08-24 concept triage](jfa-concept-triage-2026-08-24.md). A stale document here means the project has stopped describing itself honestly. Each entry carries a status and names the constraints it inherits.

Two questions are currently open: readmission after trust suspension (entry 7, resolved in draft pending adoption of the bylaws amendment) and sybil resistance in the governance franchise (entry 8). The rest were resolved as raised; their record follows.

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

**Inherits:** whether-vs-how-much (lines 8-9); trust suspension outcome (jfa-dispute-mechanics.md §4); appeals to governance venue.

## 8. Sybil resistance in the governance franchise

**Status:** open (2026-08-31)

Raised by the bylaws draft's extension of the vote in the Governance Federation Channel to prosumers (§4.2, §4.4). Eligibility is at least one sealed exchange committed to the public chain, which prices a manufactured voter at a real witnessed exchange rather than at nothing. It does not price one high enough: an operator can transact with itself at scale and mint eligible prosumers. The weight of that gap is unusual here because the channel's member roll is expected to stay very small — governance hosting has little reason to replicate beyond redundancy and geography — so the prosumer body is where the weight inside that channel sits, including the election and recall of the Vice President and the disposition of expulsion referrals. How far that weight travels beyond the channel is bounded by the delegate channel, below.

The corpus does not price identity anywhere. Entry 3 settled that one account carries both producer and consumer roles; it did not ask what makes an account a person. The privacy floor cuts against the cheap answers: line 7 forbids the identity data that conventional sybil resistance would want in the shared record, so any solution has to work from structure — counterparties, witnesses, timing — rather than from identity.

Candidate directions, none adopted: witness-attested distinctness at the record layer; a per-platform ceiling on the prosumer votes counted in one ballot; eligibility earned across two or more distinct counterparties rather than one; or an explicit decision that headcount is legitimate weight in this channel and that the immediate recall of §6.8 is the whole answer.

**Bounded by the delegate channel (2026-08-31).** A federation's vote is channeled into its one delegate, so a manufactured prosumer body does not scale into Institute-wide weight: a billion prosumer members behind a single governance host still produce one Governance delegate, against the four seated by the operator and orchestrator federations. Headcount inside a federation buys influence over that federation's delegate and nothing beyond it, which is why the operating roll stays the more influential body even as the prosumer roll grows without bound.

What the gap can still reach is the Governance delegate itself, and with it the office of the Vice President and the disposition of expulsion referrals — the powers of Article XII rather than the powers of the membership. The bylaws draft also puts the amendment of the bylaws themselves within prosumer-member reach (bylaws §15.1), which is the one place the gap touches the structure rather than an office; whether that vote is cast directly or channeled through delegates is unsettled in the draft and is the open half of this question. The immediate recall of §6.8 is the standing check, and it is exercised by the same roll a sybil attack would have captured — which is the part that does not resolve itself.

**Inherits:** privacy floor (line 7, entry 2); platform-scoped non-portable identifiers (bylaws §9.10(f)); one member, one vote (bylaws §3.4); recallable delegates, one per federation (bylaws §5.3); witness minimum (entry 4).

