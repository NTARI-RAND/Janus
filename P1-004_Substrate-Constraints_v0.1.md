# Routed, Not Negotiated: Residential Substrate Under Carrier Constraints

**Network Theory Applied Research Institute**
Document ID: P1-004 · Version: 0.1 (Draft) · September 2026

*Companion to the official document of the Janus Facing Architecture. This paper analyzes; it never governs. Where it recommends a rule, the rule takes effect only by amendment of the official document under bylaws §9.2 and its registry under §9.16.*

## Abstract

The Janus Facing Architecture places its substrate layer on consumer hardware in homes, offices and storage. Three physical facts of consumer broadband stand against that: connections carry dynamic addresses behind carrier-grade network address translation, their acceptable-use policies bar inbound servers, and their upstream bandwidth is a fraction of their downstream. A fourth fact stands against the trust model: a host with physical possession of a machine can read its memory, and the confidential-execution features that would prevent this are absent from consumer processors by vendor decision.

This paper argues that the carrier constraints are best treated as an adversarial physical environment to be routed around in code, not a policy condition to be negotiated legally, and it gives the empirical case for that choice. It then states what routing around them actually requires, separates the parts that technique solves from the parts it does not, and records one legal question that no protocol design can answer.

## 1. The choice of venue

There are two ways to answer a constraint imposed by a network carrier. Change the carrier's obligations through law and regulation, or build software that does not need the carrier to change. The architecture's own research says which one to expect results from.

NTARI's work on democratic information velocity describes a structural mismatch: information and infrastructure move at network speed while democratic synthesis stays locked to electoral cycles (NTARI, 2025a). Acemoglu and Robinson's Red Queen effect names the consequence — when one runner outpaces the other, the corridor is lost (Acemoglu & Robinson, 2019). United States broadband regulation is a clean instance. Two decades of contested rulemaking on network neutrality ended on 2 January 2025, when the Sixth Circuit set aside the Federal Communications Commission's 2024 order in full, holding that the Commission lacked statutory authority to classify broadband as a telecommunications service (Ohio Telecom Association v. FCC, 2025). Relying on Loper Bright, the court removed the deference that had let the rule survive earlier challenges. What remains federally is a disclosure regime: the Commission can require a provider to publish its traffic-management practices and cannot prohibit them. Eight states legislate in the gap, which means a nationally uniform legal answer does not currently exist and a deployment's permissions depend on where its nodes sit.

That record is not an argument against civic engagement. It is an argument against dependency. A protocol whose viability waits on a favorable rule is a protocol that does not run for years at a time, and the counterparties in that venue are incumbents whose lobbying capacity exceeds this institute's by orders of magnitude. Software written to work under the terms carriers already impose runs today and keeps running whichever way the rule turns.

**The position.** Carrier constraints are an immutable physical constraint for design purposes. Lobbying may proceed as a civic matter, and this paper takes no position against it, but it is never a dependency of the architecture and no deployment plan may assume its success.

One caveat belongs here rather than in a footnote. This choice is available for the three constraints below because each has a technical answer. It is not available for every constraint, and the paper's final section names one where it is not.

## 2. Reachability without a server

**The constraint.** A residential connection is not a hosting environment. Its address changes, it commonly sits behind carrier-grade network address translation that gives no inbound path at all, and its acceptable-use policy generally bars running servers. Comcast's residential policy is representative: it prohibits equipment that provides "network content or any other services to anyone outside of your Premises LAN, except for your personal and non-commercial residential use," and names web hosting, file sharing and proxy servers as examples (Comcast, 2021).

**What technique answers.** Everything about reachability. A node that never accepts an inbound connection is unaffected by dynamic addressing, by carrier-grade translation, and by the inbound-server prohibition, because none of those constrain outbound connections. The node opens the connection to the coordinator, holds it or reopens it on a schedule, and asks for work.

The reference protocol already has this shape and did not need changing. Its node-side operations are `SubmitListing`, `Heartbeat`, `PollJobs`, `Decline`, `ReportJob` and `Fees` — every one of them a request the node initiates. The coordinator implements a pluggable interface and answers; it never dials the node. What was missing was not the mechanism but the commitment. A property that holds by accident of the current implementation can be lost in the next refactor, so the official document now states it and the registry binds it:

> Nodes join that market over encrypted overlays and outbound polling, without requiring open inbound ports or a static address; the connection as a residential provider ships it is enough. Line 11 depends on this: a substrate that ran only where a provider permits inbound service would carry a chokepoint at every provider.

Registered as `SUB-no-inbound-requirement`, implementation-bound. A repository binds it by shipping tests that cite the identifier and prove a node completes the full employment loop — register, heartbeat, poll, run, report — with no listening socket, no static address, and a translated, changing address in front of it. Until such tests exist the invariant is reported unbound under bylaws §9.15, and this paper's claim about the reference implementation is exactly the self-attestation §9.6 refuses to recognize.

The line-11 reasoning is the substantive part, and it is why this belongs in the document rather than in a deployment guide. Line 11 forbids any single host, account or vendor whose removal could stop the network. A substrate that required inbound service would run only where a carrier permits it, making every carrier a veto — a chokepoint per provider, distributed in appearance and centralized in fact.

**Three notes on mechanism.** First, on transport: ordinary HTTPS and WebSocket connections on port 443 are the right carrier because that is what the network path reliably permits and what every web client already emits. This paper deliberately does not describe that traffic as disguised. It is not camouflage; it is the standard protocol for the job, and the honesty matters because the framing of camouflage invites the belief that a technical measure has answered a permission question, which section 5 shows it has not.

Second, on internet protocol version six: it removes carrier-grade translation where both ends have it, and adoption crossed half of Google's traffic globally on 28 March 2026, with the United States near 57 per cent (Google, 2026). It is worth using and worth requiring nothing from. Universal addressability is not the same as universal reachability — a globally routable address still sits behind a firewall that drops unsolicited inbound packets, and a node that assumes otherwise fails on the remaining half of connections. Version six is an optimization to the outbound posture, never a replacement for it.

Third, on encrypted overlay networks. Mesh overlays are a real answer to node-to-node paths that the coordinator should not mediate, and named implementations exist. They cannot enter the protocol module. The lean-code principle holds protocol software to its language's standard library so it stays auditable whole, and the reference protocol currently satisfies this strictly — its module declares no dependencies at all, which is the property that keeps any single coordinator from becoming a hub. A large overlay library inside that module would end it. An overlay therefore belongs below the protocol as deployment-level transport, chosen per deployment and replaceable, or is implemented minimally within the leaf. The document's wording is deliberately generic for the same reason the document carries no product names.

There is a related tension the institute should not paper over. The reference coordinator deployment currently sits behind a single commercial content-delivery network, and the agricultural stack's transport design assumes that vendor's tunnel. That is convenient, it is not conformant with line 11 in spirit, and it is a chokepoint of exactly the kind this section removes at the carrier layer while leaving in place one layer up. It is out of scope here and belongs on the substrate's open-problem list.

## 3. Bandwidth asymmetry

**The constraint.** Consumer connections are asymmetric by design, often ten to one or worse, and increasingly metered. A node cannot serve as a general content origin, and a workload that ships large images to every host will spend its time in transfer rather than compute.

**What technique answers.** Most of it, by keeping payloads small rather than by moving them faster. Three design choices do the work, and they compound.

**Coordination traffic is small by construction.** Line 7 keeps narratives and identities out of the shared record — hashes, types, timestamps and references only. A privacy floor adopted for privacy reasons has a bandwidth consequence: the record layer's traffic is bounded by the size of hashes and headers rather than by the size of what was exchanged. Content stays with the parties. The coordination messages that carry the market are a handful of signed structures over a canonical byte encoding. Nothing here strains a home uplink, and this is the sense in which the packages are light: the architecture's own transmissions are light because a line that cannot be crossed forces them to be.

**Work ships as sandboxed modules, not as machine images.** This is the one recommendation in this paper that asks the reference implementation to change rather than to hold its shape. The current node agent runs jobs through a container executor, which means a first job on a fresh node pulls layers measured in hundreds of megabytes before any work begins. A WebAssembly module for the same task is measured in megabytes or less, starts in milliseconds, carries a deny-by-default capability model rather than an opt-out one, and is portable across the mixed consumer hardware the substrate expects instead of requiring a matching architecture. A runtime with no native dependencies keeps the node agent auditable in the same spirit the protocol module is. Containers should remain available for workloads that genuinely need a full operating environment, on nodes whose connections and operators can carry them, and should stop being the default. The trade is real and should be stated: WebAssembly costs some throughput against native execution and cannot host arbitrary existing software unmodified. For irregular, light, sensor-and-coordination work — the agricultural pattern this architecture serves first — that trade is favorable.

**Jobs spool locally.** A node holds its queue and its pending reports in a local embedded store and drains them when the connection allows. The consequence is that a poor uplink delays work instead of losing it, and an intermittent connection stops being a disqualification. This matters beyond bandwidth: the agricultural pilot already plans for rural connectivity gaps with offline entry and later synchronization, and the same property makes a node in that setting a participant rather than a liability.

None of these three is a novel invention and none is registered as an invariant. They are design posture, recorded here so that a deployment can be assessed against them and so the reasoning survives the people who had it. The board may wish to consider whether the module-over-image default should become a registered invariant; this paper does not recommend it yet, because the reference implementation does not satisfy it today and a registry that outruns the code teaches the wrong lesson about what registration means.

## 4. Execution on hardware the host controls

**The constraint.** A prosumer hosting a node has physical possession of the machine. They can read its memory, inspect its disk, and observe what it computes. The conventional answer is hardware confidential execution, and it is unavailable at this layer as a matter of vendor product strategy rather than of cost. Intel deprecated Software Guard Extensions on client processors from the eleventh generation of its Core line and retains it on server and cloud parts (Intel, 2021). AMD's Secure Encrypted Virtualization, including the nested-paging generation, is an EPYC server feature and is not present on Ryzen or Threadripper (AMD, 2021). A requirement for either would exclude essentially all consumer hardware and re-admit precisely the data-center gatekeeping the substrate layer exists to displace. Requiring enclaves would not secure the commons substrate; it would abolish it.

**What technique answers, and how far.** Not confidentiality against a determined host. This section is where the paper's method changes, and saying so plainly is more useful than a workaround presented with more confidence than it earns.

The architecture's available answer is not to trust the host but to make dishonesty visible and expensive, using machinery the stack already owes itself. Three parts:

**Redundant execution with rated disagreement.** A job of consequence is dispatched to two or more independent hosts and their results compared. Agreement is evidence; disagreement is an event that enters the covenant, where the scale's lowest rating already means a party was harmed, exploited, or served with malicious intent. The enforcement hook exists: witnessing is compensated substrate work, and the substrate owes a work-type in which witnesses are randomly assigned so that neither party to an exchange can choose its witness. Redundant execution is that same market pattern applied to compute rather than to record-keeping, and random assignment is what makes collusion between a job's executors a matter of chance rather than of choice. The cost is a multiple of the compute, paid deliberately for the class of work that warrants it, and it buys detection rather than prevention — the same posture the record layer already takes toward tampering.

**Data minimization as the primary control.** A host cannot scrape what never arrives. Line 7 already keeps identities and narratives out of the shared record; the corresponding discipline at the substrate layer is that a job carries the least data that will let it complete, that sensitive inputs are partitioned across hosts where the work allows it, and that a workload requiring a large coherent body of sensitive data about identifiable people is a workload for hardware whose operator is accountable for it. That last clause is a real limit on the substrate's reach and should be stated as one rather than engineered around.

**Attestation as an optional, priced, rated capability.** Where a buyer genuinely needs hardware-backed confidentiality, the answer is a market, not a mandate. A host with such hardware advertises the capability as part of its listing, buyers who need it pay for it, and the claim is subject to the same covenant rating as any other representation a host makes. This keeps the floor open to consumer hardware while letting the ceiling rise wherever a host has invested, and it locates the decision with the party bearing the risk.

**Status.** This is the part of the September 2026 review that is not resolved. The position above is argued, not adopted: no invariant is registered, and a candidate identifier for redundant execution is noted in the open-questions record as a decision for the board under §9.16. Registering it would oblige the substrate to build a work-type it has not built. The honest state is that the architecture has a coherent answer to host-operator observation and has not yet committed to it.

## 5. What technique does not answer

Outbound polling removes the inbound-server problem completely. It does not remove the acceptable-use problem, and this paper would mislead its readers if it implied otherwise.

Read the representative policy again. It bars equipment serving anyone outside the premises network "except for your personal and non-commercial residential use." The inbound-server prohibition is a statement about ports and is answered by not using any. The non-commercial prong is a statement about compensation, and compensation is the point: a prosumer hosting substrate is paid, in fiat in the current implementation and in community credit later. No transport choice, port number, or encryption changes that fact, and a design that claims to have routed around it has confused a mechanism with a permission. The question is whether compensated participation on a residential line engages that prong, and the answer is a reading of contract terms in a jurisdiction, not a property of software.

The institute should have counsel review it, and the natural occasion is at hand: the combined heat-and-compute pilot already has two open questions before counsel about whether a revenue-earning node in a home changes the household's position with its insurer under business-use exclusions. The carrier-terms question is the same question addressed to a different contract, and it should go in the same package rather than wait for its own. Its practical shapes are worth naming now — whether a business-tier connection is required, whether a de-minimis or cost-sharing framing holds, whether the answer varies by carrier enough that node-operator guidance must be regional, and what a deployment tells prospective hosts before they enroll.

The last of those is a covenant matter as much as a legal one. A prosumer is entitled to know what participation may mean for their own service agreement before they take it up, and the architecture's own commitment to a rated, disclosed relationship between operator and prosumer makes silence on the point the wrong default.

## 6. Where this landed

| Level | What changed | Enforcement |
|---|---|---|
| Official document | Substrate protocol tier states the outbound, no-inbound-requirement posture and ties it to line 11 | Suite checks the text; passes at 26 invariants |
| Conformance registry | `SUB-no-inbound-requirement` added, implementation-bound | Unbound until node tests cite the identifier (§9.15) |
| Open-questions record | Entry 9 records the constraint, the resolutions, the open part, and the legal question | §9.3 |
| This paper | The bandwidth and confidential-execution posture, argued and unbound | None; it analyzes and does not govern |

Two procedural obligations attach to the document change and are not discharged by this paper. An amendment of the official document and its registry runs under bylaws §9.2 and §9.16, and during bootstrap the founder board exercises that power with each act recorded in the governance registry as a bootstrap act under §16.1, open to the membership like any other decision. The suite passes against the amended text, which §9.2 requires before adoption, and the seven-language renderings under P2-002 were updated with the English original.

## Sources

Acemoglu, D., & Robinson, J. A. (2019). *The Narrow Corridor: States, Societies, and the Fate of Liberty*. Penguin Press.

AMD. (2021, March 15). *AMD EPYC 7003 series processors set new standard*. https://www.amd.com/en/newsroom/press-releases/2021-3-15-amd-epyc-7003-series-cpus-set-new-standard-as-hig.html

Comcast. (2021, February 1). *Acceptable use policy for Xfinity Internet (residential)*. https://www.xfinity.com/corporate/customers/policies/highspeedinternetaup

Google. (2026). *IPv6 adoption statistics*. https://www.google.com/intl/en/ipv6/statistics.html

Intel. (2021). *Intel SGX deprecation on client processors* [Intel Community discussion]. https://community.intel.com/t5/Intel-Software-Guard-Extensions/Intel-SGX-deprecated-in-11th-Gen-processors/m-p/1351848

Internet Society. (2026, April). *18 years later, IPv6 reaches majority*. https://pulse.internetsociety.org/en/blog/2026/04/18-years-later-ipv6-reaches-majority/

Network Theory Applied Research Institute. (2025a, October). *Addressing democratic information velocity* (P1-002). https://www.ntari.org/post/ntari-whitepaper-addressing-democratic-information-velocity

Network Theory Applied Research Institute. (2025b, June). *The material culture of democratic deliberation*. https://www.ntari.org/post/the-material-culture-of-democratic-deliberation

*Ohio Telecom Association v. FCC*, Nos. 24-7000 et al. (6th Cir. Jan. 2, 2025). Congressional Research Service analysis: https://www.congress.gov/crs-product/LSB11264

---

*Network Theory Applied Research Institute, Inc. — 501(c)(3) — EIN 92-3047136 — info@ntari.org*

*Specification: CC BY-SA 4.0*
