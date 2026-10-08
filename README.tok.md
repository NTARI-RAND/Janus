# nasin JFA (Janus Facing Architecture)

> **toki pona:** lipu ni li lipu pi kulupu, tan nasin NTARI "P2-002". lipu
> ale li lipu "README.md" pi toki Inli (tenpo pi sitelen: 2026-10-05). ilo sona
> li pali e lipu ni, la kulupu o lukin o pona e ona, tan nasin "P2-002" kipisi
> nanpa 3.1.
>
> **English:** This is a community rendering under NTARI policy
> P2-002. The complete document is the English original README.md (snapshot
> 2026-10-05). Machine-assisted draft pending community review per P2-002
> section 3.1.
>
> sina lukin e pakala lon toki ni la o pona e ona: o pali e "fork" lon
> https://github.com/NTARI-RAND/Janus, o pana e "pull request". pana sina li
> pona tawa mi mute.

lipu ni li lipu suli pi nasin Janus Facing Architecture (JFA). kulupu
Network Theory Applied Research Institute, Inc. (NTARI) li awen e ona, lon nasin
pi [lipu lawa ona](https://github.com/NTARI-RAND/bylaws) kipisi §1.4(a).

nasin JFA li pana e ken tawa kulupu: kulupu li ken pali tawa lon pi esun ni: jan
ale li jan pali jo (prosumership). nasin JFA li pana kin e nasin tawa: tan mani
pi kulupu lawa tan selo kulupu (exogenous, chartal money) tawa mani pi pana sama
tan insa kulupu (endogenous mutual credit). nasin JFA li jo e kipisi pali luka
(5) — kipisi ilo (Substrate), kipisi sona (Record), kipisi pi toki awen
(Covenant), kipisi lawa (Governance), en kipisi esun en sona (Economy &
Information). kipisi ale li pali lon nasin tu wan (3): lupa lukin (frontend),
ilo insa (orchestrator), en nasin insa (protocol).

## lipu

| | |
|---|---|
| **lipu suli** | [janus-facing-architecture.md](janus-facing-architecture.md) |
| **wile sona pi pini ala** | [OPEN-QUESTIONS.md](OPEN-QUESTIONS.md) |
| **sona tan lipu lawa pi tenpo pini** | [jfa-concept-triage-2026-08-24.md](jfa-concept-triage-2026-08-24.md) |
| **ilo pi lukin sama (ilo li ken pali e ona)** | [jfa-conformance-suite.py](jfa-conformance-suite.py) |
| **kipisi ilo lon anpa pi lawa pi kulupu linja (P1-004, lipu poka)** | [P1-004_Substrate-Constraints_v0.1.md](P1-004_Substrate-Constraints_v0.1.md) |
| **lipu lawa pi tenpo pini** | [Historical Docs/](Historical%20Docs/) |

lipu pi toki Inli li lawa. lipu pi toki ante li lon tawa ni: jan mute li ken
lukin. ona li lon ala tawa ni: jan li sona e kon lawa tan ona.

| toki | lipu |
|---|---|
| العربية (toki Arabu) | [janus-facing-architecture.ar.md](janus-facing-architecture.ar.md) |
| Español (toki Epanja) | [janus-facing-architecture.es.md](janus-facing-architecture.es.md) |
| Français (toki Kanse) | [janus-facing-architecture.fr.md](janus-facing-architecture.fr.md) |
| हिन्दी (toki Insi) | [janus-facing-architecture.hi.md](janus-facing-architecture.hi.md) |
| Português (toki Potuke) | [janus-facing-architecture.pt.md](janus-facing-architecture.pt.md) |
| toki pona | [janus-facing-architecture.tok.md](janus-facing-architecture.tok.md) |
| 中文 (toki Sonko) | [janus-facing-architecture.zh.md](janus-facing-architecture.zh.md) |

## nasin pi ken ala

lipu suli li jo e kipisi pi nimi *The Lines That Cannot Be Crossed* (*nasin 12
pi ken ala*). kipisi ni li jo e nasin luka luka tu (12): ilo ale pi nasin sama
li ken ala pakala e ona. o lukin e ona. ni la o open pali e ilo.

## ilo pi nasin ni

ilo pi sitelen sama (reference implementations) en ilo kepeken (instances) li
lon poki lipu ona:

- [Tell](https://github.com/NTARI-RAND/Tell) — kipisi sona (Record): lipu pi jan
  pi ilo suli wan wan; jan lukin li lukin e ona; toki sin taso li ken kama lon ona
- [Agrinet](https://github.com/NTARI-RAND/Agrinet) — nasin insa pi linja ilo;
  kulupu mute pi pali kasi li wan lon ona (federated)
- [SoHoLINK](https://github.com/NTARI-RAND/SoHoLINK) ·
  [Cloudy](https://github.com/NTARI-RAND/Cloudy) ·
  [sohocloud-protocol](https://github.com/NTARI-RAND/sohocloud-protocol) —
  kipisi ilo (Substrate)
- [lighthouse](https://github.com/NTARI-RAND/lighthouse) ·
  [shelter](https://github.com/NTARI-RAND/shelter) ·
  [childcare-trust-network](https://github.com/NTARI-RAND/childcare-trust-network) ·
  [shanina](https://github.com/NTARI-RAND/shanina) ·
  [COER](https://github.com/NTARI-RAND/COER) ·
  [world-chase-tag](https://github.com/NTARI-RAND/world-chase-tag) — ilo open
  (seeds) en ilo kepeken (instances) pi kipisi esun en sona (Economy &
  Information)

ilo open li awen lon nasin; selo li ken ante, anpa li lawa.

## lukin pi lipu suli

ilo lukin li kipisi ni: ona li jo e wawa pi ijo ale lon sewi ona (load-bearing
rung). ona li wan e toki pi lipu suli e lipu nimi pi nasin awen (invariants).
nasin awen ale li jo e nimi nanpa (ID) pi ante ala. lipu suli en lipu nimi li
kama sama ala la, lukin li pakala lon tenpo ale. ona li kepeken poki ilo lawa
taso (standard library), li wile ala e ilo ante (dependencies).

```
python jfa-conformance-suite.py                 # check the document
python jfa-conformance-suite.py --list          # print the invariant registry
python jfa-conformance-suite.py --doc PATH      # check another copy
python jfa-conformance-suite.py --project PATH  # check a repo's open-questions deliverable
```

lukin ale pi ilo li pona la nanpa pini (exit code) li 0. ante la ona li 1. sina
ante e lipu suli lon tenpo ale la, o kepeken ilo lukin lon tenpo kama.

lipu nimi li jo e nasin awen 26. nasin awen 3 li lawa lon ni, lon kipisi pi lipu
suli. nasin awen 23 li **tawa ante** (delegated): ona li lawa e ilo nanpa pi
tenpo pali, anu lipu lawa pi kulupu lawa. ilo lukin (tests) taso li ken awen e
ona; ilo lukin ni o lon poka pi ilo ni anu lipu lawa ni. nasin awen ni li lon
lipu nimi, li jo e nimi nanpa (ID) pi ante ala. poki lipu li pana ala e ilo
lukin pi toki e nimi nanpa ni la, lukin li toki e ni: nasin awen li tawa ante,
li lawa ala lon tenpo ni. poki lipu pi nasin sama li toki e nimi nanpa ni. ona
li toki ala e ona la, nasin sama ona li toki pi ona taso (self-attested). sina
toki tan lipu ni e ni: nasin awen pi tawa ante li "checked", la ni li toki pi
ona taso lon len pi ilo lukin. tan ni la, ijo pi tenpo lili (stand-in) li jo e
sitelen nimi ona, li jo ala e "checked".

## lipu ni li lon ala poki ni lon tenpo ni

lipu pi nasin pi toki utala (dispute-mechanics design) — "the dispute-mechanics
design" sama [lipu lawa](https://github.com/NTARI-RAND/bylaws) kipisi §1.5 li
toki e ona — en lipu pi nasin kulupu (structure) en lipu pi jan ilo (robotics)
li lon poki lipu pi kulupu NTARI. ona li lon ala poki ni lon tenpo ni.

## nasin pi ken kepeken

nasin tu pi ken kepeken li lon. anpa pi lipu suli li toki e ni:

| ijo | nasin pi ken kepeken |
|---|---|
| lipu nasin (specification) — lipu suli, lipu ona pi toki ante, en lipu lawa pi tenpo pini | [CC BY-SA 4.0](LICENSE-SPEC) |
| ilo (software) — ilo pi lukin sama | [AGPL-3.0](LICENSE) |
