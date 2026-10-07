# Five Layers, Twelve Lines: The Shape of the Janus Facing Architecture

*Network Theory Applied Research Institute — August 2026*

The Janus Facing Architecture (JFA) is named for the Roman god who embodied the concept of looking in two directions at once — just as every economic participant faces both production and consumption. Every member of an economy is not just a consumer but a *prosumer* (Toffler, 1980), simultaneously producing economic value even if all they have to offer is time. Software built on this observation cannot split a person into a producer and a consumer identity. That is the name's first face. The second face is political, and it is the reason the architecture looks the way it does.

## The corridor and the Red Queen

In *The Narrow Corridor* (2019), Daron Acemoglu and James Robinson argue that liberty is not a natural condition but a narrow corridor a society has to fight its way into and fight to stay inside. Their Leviathan — Hobbes's name for the state — comes in forms. The Absent Leviathan cannot coordinate or protect anyone. The Despotic Leviathan coordinates by dominating. The Paper Leviathan has the org charts of a state and none of the capacity. Liberty exists only under the fourth form, the Shackled Leviathan: strong enough to coordinate, shackled by a society strong enough to check it. And staying there is never settled. The Red Queen effect — named for the queen who tells Alice she must keep running just to stay in place — demands that state and society grow together, each expanding its capacity because the other does. When one side outruns the other, the corridor is lost.

Why does a software architecture open with political theory? Because every platform is a Leviathan in miniature: it coordinates supply and demand, enforces rules, and keeps the record. The dominant platforms of the present economy are despotic by construction — the operator holds the market, the money rail, and the record, while members hold nothing but an account. And the institutions meant to shackle them are failing the Red Queen's race. NTARI's whitepaper on democratic information velocity documents the mismatch: platforms evolve at internet speeds while democratic institutions evolve at meeting schedules, a velocity gap that lets concentrated power accumulate faster than society's capacity to check it. NTARI's study of the material culture of democratic deliberation traces that failure into the tools themselves: deliberative infrastructure is material culture — the way a spear encodes assumptions about hunting, a governance platform encodes assumptions about who may know and who may decide — and the prevailing architectures encode broadcast: information flowing one way, citizens as passive recipients, synthesis locked to electoral cycles at postal speed.

The answer is to stop trying to shackle the Leviathan from outside. If the check must run as fast as the coordination, the check has to live in the same being. With the internet and telecommunications, a community that coordinates the economy can be the same community that checks the coordination, the two roles exchanged continuously between individual members. A shackled Leviathan, in code — built to run the Red Queen's race at the Red Queen's speed.

## An Internal Currency System

Most money is exogenous and chartal — issued by a central authority and imported into communities through banks to facilitate local transactions (Knapp, 1924). Credit is distributed in the same fashion: even the credit union, the most local and member-owned form of capital disbursement, is exogenous at bottom — it lends out the chartal currency concentrated by particular communities, and it prices its trust with credit scores, judgments produced by monitoring individuals and cast from afar. Cryptocurrency, for all its innovation, did not address this issue, only relocating it from central banks to the owners of mining hardware. JFA lets a community transform the issuance model to endogenous mutual credit: money issued by members to one another as they transact (Moore, 1988; Greco, 2009). At the moment of exchange, one balance goes down and one goes up, and the two always sum to zero. Credit is issued only for value provided; it is earned, never bought, and never redeemable for fiat. There is no external issuer and no interest at any stage. Nothing is held in reserve once a deployment reaches full mutual credit — the escrowed cold start described below is the deliberate exception.

The money rules come with a deliberate cold start: a new deployment begins in escrow — collateralized, no negative balances, no trust extended — and switches to a hybrid system or full mutual credit only after the operator builds capacity, the prosumer network is notified, and the local authorizations to provide mutual credit services are published to the governance layer — or, where the jurisdiction requires none, a finding to that effect is published there instead. The hybrid stage is exactly what it sounds like: escrow and mutual credit run across the same system, and each prosumer decides which they accept.

## Nine decades of evidence

Mutual credit is not a thought experiment. It has one of the longest, best-documented track records of any alternative monetary design — and the recurring finding is not merely that these systems survive, but that they stabilize.

An analysis in *Nature Human Behaviour* of 1,477 member firms and 48,170 transactions form Sardinia's Sardex mutual credit network found that trade in the network is organized around geodesic cycles — credit flowing in loops and returning to where it began — which is precisely the circulation geometry a zero-sum currency needs to remain liquid without an issuer (Iosifidis et al., 2018). Sardinia's entire island territory is ~9,300 sq. miles, representing not just a typical urban city, but the suburban, rural and industrial assets of a functional economic region.   

The Swiss WIR, founded in 1934 by businesses frozen out of Depression-era bank credit, has operated continuously for more than ninety years and grew into a network of tens of thousands of small and mid-sized firms. WIR turnover is strongly countercyclical, rising when the Swiss economy contracts, because cash-short firms economize by trading on mutual credit instead — a spontaneous stabilizer credited with helping secure Swiss employment through downturns (Stodder, 2009). The follow-up study found the stabilization operates through both balances and velocity: the money moves fastest exactly when the wider economy needs it most (Stodder & Lietaer, 2016). This is the mirror image of fiat credit, which is procyclical — banks lend freely in booms and withdraw in busts. Mutual credit runs the other way. The benefit of having these opposing monetary algorithms is obvious — fiat and mutual credit systems can exist independent of one another, but together provide liquidity options in shifting trust environments. 

The Republic of Ireland ran an accidental national-scale experiment. Industrial disputes closed the Irish banks three times between 1966 and 1976 — for six months in 1970 — cutting the economy off from most of its money supply. It kept growing. Firms and households traded on uncleared cheques underwritten by personal knowledge of the drawer, with publicans and shopkeepers acting as informal credit assessors (Murphy, 1978). A community issued its own credit, peer to peer, on local reputation — the covenant's premise, run at national scale by accident.

The evidence extends to where money is scarcest. Kenya's Sarafu community inclusion currency scaled to roughly 55,000 accounts and some 300 million Sarafu in recorded transactions through the COVID-19 shock of 2020–2021, with the complete anonymized transaction record published as open research data (Mattsson, Criscione & Ruddick, 2022) — mutual credit functioning as economic infrastructure precisely when national currency stopped circulating in its communities.

Swiss business, a Sardinian exchange, an accidental Irish experiment, a Kenyan aid network: the common finding is that endogenous credit holds up exactly when exogenous money fails. What every one of these systems also shares is a central operator its members simply had to trust — WIR became a bank, Sardex is a company, Sarafu runs on a foundation's platform. JFA keeps the economics the evidence supports — zero-sum issuance, credit limits, managed defaults — and removes the leap of faith: the record outlives every operator, reputation travels without permission, and the operator itself is rated, published, and cheap to leave.

## The grid: five layers, three tiers

The stack is five functional layers — Substrate, Record, Covenant, Governance, and Economy & Information (E&I) — each implemented in three tiers: the **frontend**, for prosumer collaboration; the **orchestrator**, a backend providing overlapping coordination across geographic communities; and the underlying **protocol**, the pattern for securely handling data across tiers.

**Substrate** is the hardware where everything happens — CPUs, GPUs, printers, storage and sensors owned by prosumers, running on consumer-grade computers in homes, offices and storage as well as repurposed industrial equipment. Its protocol exchanges instructions and orders across a distributed compute/storage market; its orchestrator federates prosumer compute power, creating more options across geography; its frontend is the E&I interface for prosuming compute and storage. Nodes join the market over encrypted overlays and outbound polling — no open inbound port, no static address — so a home connection as the provider ships it is a full participant. One constraint governs the layer: it must have no single host, account, or vendor whose removal could stop the network, and the outbound posture is what keeps that true across residential providers.

**Record** is a series of distributed, compensated functions of the substrate, conserving hashes of the dialog between the E&I and Covenant layers for public record. The record of what happened is held six ways: Each party to a transaction keeps a record of their own; the operator keeps its own; two witnesses keep their own; and hashes are committed to one public chain, distributed across the substrate. Six holders, one truth. The chain is append-only: harm is forgiven by annotating, never by erasing. 

The protocol tier captures, categorizes and hashes each transmission in the stack — establishing reputation through the Covenant layer and the basis of truth as an exchange medium in E&I. Only hashes reach the chain; the content stays with the parties — no narratives, no identities in the shared record. The orchestrator federates records across geography, enabling shared reputation and exchange — and what federation shares is recorded truth, reputation and exchange history, never a currency unit.

**Covenant** is the social contract enforced by the governance in code, informing expectations for prosumer interactions. Prosumers rate their interactions as they generate hashable transmissions through interaction; the orchestrator is an API serving compliant assessments across the stack's markets; the frontend is any E&I interface where the API is served. Two rules keep reputation honest. First, reputation is never one number: what others see is the count of exchanges at each rating level, so one bad outcome cannot hide inside a good average. Second, reputation answers exactly one question — how does this prosumer perform within the social covenant of the network? How much credit they may draw is a community-wide limit set by the platform operator, one number for everyone, never derived from reputation. Merged, the two would recreate the credit score, which is the thing the covenant exists to replace. When apparent breaches in covenant occur, platform operators adjudicate between their prosumers; disputes that cross platforms go to the exchange's witnesses. Adjudicators are rated on their conduct by both prosumers involved — the referees are inside the reputation system too.

**Governance** is how humans collaborate on building and maintaining the stack. The protocol is a nonprofit steward of copyleft software; the orchestrator is membership obtained by operating a federated instance of JFA software; the frontend is the synchronous/asynchronous coordination of members governed by the organization's bylaws.

**Economy & Information** is hosted on record layer substrate, and facilitates covenant compliance. Each economic or information platform has a protocol designed for its specific kind of exchange — agriculture, games, research citation — and its own frontend, customizable by the user; membership in the governance layer is what orchestrates them, and every platform runs on revokable hardware obtained and recorded by the substrate layer. Each platform's operator manages the economy it hosts — setting its credit limit, one number for everyone, which prosumers can weigh when choosing where to trade; the operator's remaining economic duties live in the bylaws.

## Between Federations

Members operate software speaking the same protocol, recorded on substrate rented from the community, with different frontend features to support prosumers. Together they troubleshoot bugs, navigate security, innovate on the shared protocol, and find ways to expand the market. Members are organized by the layer(s) they operate addressing any issues within their layer's stack and adhering to the GNU Affero General Public Licensing requirement to publicly publish changes to the source code. This is steamlined by good governance.      

Each federation's currency is sovereign — no shared unit, no conversion. When two communities trade, the exchange is two sovereign spends bound atomically by the public chain. Because nothing redeemable ever crosses federations, there is nothing to transmit and nothing to clear.

Exit is protected the same way. A member's positions and history survive any frontend; a community's records survive any operator. The mechanism is the record topology itself: the public chain plus the per-party records mean no operator holds anything hostage. Underneath it all runs one disciplining rule: each layer is governed by the cost of leaving it. Where leaving is cheap, competition disciplines; where leaving is dear, members get a vote; where leaving is impossible, decisions stay open to challenge.

## The twelve lines

These twelve properties are required of the JFA stack. 
1. Money created only at the moment of exchange, summing to zero. 
2. Credit earned, never bought, never redeemable for fiat. 
3. Sovereign currencies, no shared unit, no conversion. 
4. Value stays home; only truth crosses. 
5. Cross-community exchange bound atomically by the public chain. 
6. The record append-only — forgive by annotating, never by erasing. 
7. No narratives, no identities in the shared record. 
8. Reputation never expressed in one number. 
9. Reputation decides *whether*; a community-wide limit set by the operator decides how much. 
10. Deployments begin in escrow and earn their way to mutual credit through operator capacity and a regulatory review published to the governance layer.
11. No single point whose removal stops the network. 
12. Every member's positions and history survive any frontend, every community's records survive any operator.

A build that violates any of these is not a different JFA stack. It is different software.

## Legibility, mechanized

The architecture's openness is not left as a promise. The official document ships beside an executable conformance suite that verifies the document itself — its nine sections, the three tiers in every layer, the twelve lines, and the presence of every registered invariant in the exact section that carries it. The suite maintains a registry of twenty-six invariants; twenty-three can only be enforced by tests living beside running code or a governance instrument, and the suite confirms this, labeling them unbound rather than pretending to check them. It also checks that retired concepts stay retired. A claim of conformance without tests citing the registry IDs is named what it is: self-attested.

The software stack is licensed under the GNU Affero General Public License; the specification under Creative Commons Attribution–ShareAlike. Both are copyleft: anyone may build new frontends, federations, protocols and architectures from them, and what they build stays open. 

## Sources

Acemoglu, D., & Robinson, J. A. (2019). *The Narrow Corridor: States, Societies, and the Fate of Liberty*. Penguin Press.

Greco, T. H. (2009). *The End of Money and the Future of Civilization*. Chelsea Green Publishing.

Iosifidis, G., Charette, Y., Airoldi, E. M., Littera, G., Tassiulas, L., & Christakis, N. A. (2018). Cyclic motifs in the Sardex monetary network. *Nature Human Behaviour*, 2(11), 822–829.

Knapp, G. F. (1924). *The State Theory of Money*. Macmillan. (Original work published 1905)

Mattsson, C. E. S., Criscione, T., & Ruddick, W. O. (2022). Sarafu Community Inclusion Currency 2020–2021. *Scientific Data*, 9, 426.

Moore, B. J. (1988). *Horizontalists and Verticalists: The Macroeconomics of Credit Money*. Cambridge University Press.

Murphy, A. E. (1978). Money in an economy without banks: The case of Ireland. *The Manchester School*, 46(1), 41–50.

Network Theory Applied Research Institute. (2025a, October). *Addressing democratic information velocity* (P1-002). https://www.ntari.org/post/ntari-whitepaper-addressing-democratic-information-velocity

Network Theory Applied Research Institute. (2025b, June). *The material culture of democratic deliberation*. https://www.ntari.org/post/the-material-culture-of-democratic-deliberation

Stodder, J. (2009). Complementary credit networks and macroeconomic stability: Switzerland's Wirtschaftsring. *Journal of Economic Behavior & Organization*, 72(1), 79–95.

Stodder, J., & Lietaer, B. (2016). The macro-stability of Swiss WIR-Bank credits: Balance, velocity, and leverage. *Comparative Economic Studies*, 58(4), 570–605.

Toffler, A. (1980). *The Third Wave*. William Morrow.

---

*The official document and conformance suite are stewarded by the Network Theory Applied Research Institute, Inc., a 501(c)(3) — info@ntari.org. This article describes the architecture; it never governs it.*
