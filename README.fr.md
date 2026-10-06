> Traduction communautaire (brouillon) — politique NTARI P2-002, Diffusion
> multilingue mondiale. Source : README.md (original anglais, instantané du
> 2026-10-05). Brouillon communautaire assisté par machine, en attente de
> relecture par le mainteneur régional conformément au P2-002 §3.1. Les
> spécifications techniques de base restent en anglais conformément au §2.2.
>
> Vous avez remarqué une erreur de traduction ? N'hésitez pas à la corriger
> vous-même : forkez le dépôt https://github.com/NTARI-RAND/Janus et ouvrez
> une pull request. Les corrections de traduction sont des contributions
> précieuses, tout autant que le code.

# L'architecture bifrons (Janus Facing Architecture)

Le document officiel de l'architecture bifrons (JFA), dont Network Theory
Applied Research Institute, Inc. (NTARI) assure l'intendance en vertu du §1.4(a)
de [ses statuts](https://github.com/NTARI-RAND/bylaws).

JFA permet aux communautés de traiter la réalité économique de la prosommation et
offre une voie pour passer d'une monnaie chartale exogène à un crédit mutuel
endogène. Elle s'organise en cinq couches fonctionnelles — Substrat, Registre,
Pacte, Gouvernance, et Économie et Information — chacune mise en œuvre sur trois
niveaux : frontend, orchestrateur et protocole.

## Le document

| | |
|---|---|
| **Document officiel** | [janus-facing-architecture.md](janus-facing-architecture.md) |
| **Questions non résolues** | [OPEN-QUESTIONS.md](OPEN-QUESTIONS.md) |
| **Concepts repris des instruments antérieurs** | [jfa-concept-triage-2026-08-24.md](jfa-concept-triage-2026-08-24.md) |
| **Suite de conformité exécutable** | [jfa-conformance-suite.py](jfa-conformance-suite.py) |
| **Le substrat sous les contraintes des fournisseurs d'accès (P1-004, article d'accompagnement)** | [P1-004_Substrate-Constraints_v0.1.md](P1-004_Substrate-Constraints_v0.1.md) |
| **Instruments antérieurs** | [Historical Docs/](Historical%20Docs/) |

Le document anglais fait foi. Les traductions sont fournies pour élargir la
diffusion, non pour l'interprétation.

| Langue | Fichier |
|---|---|
| العربية (arabe) | [janus-facing-architecture.ar.md](janus-facing-architecture.ar.md) |
| Español (espagnol) | [janus-facing-architecture.es.md](janus-facing-architecture.es.md) |
| Français | [janus-facing-architecture.fr.md](janus-facing-architecture.fr.md) |
| हिन्दी (hindi) | [janus-facing-architecture.hi.md](janus-facing-architecture.hi.md) |
| Português (portugais) | [janus-facing-architecture.pt.md](janus-facing-architecture.pt.md) |
| toki pona | [janus-facing-architecture.tok.md](janus-facing-architecture.tok.md) |
| 中文 (chinois) | [janus-facing-architecture.zh.md](janus-facing-architecture.zh.md) |

## Les lignes qui ne peuvent être franchies

La section du document officiel intitulée *Les lignes qui ne peuvent être
franchies* contient les douze dispositions qu'aucune implémentation conforme ne
peut enfreindre. Lisez-la avant de construire.

## Implémentations

Les implémentations de référence et les instances résident dans leurs propres
dépôts :

- [Tell](https://github.com/NTARI-RAND/Tell) — la couche Registre : registre par
  opérateur, attesté par des témoins, en ajout seul
- [Agrinet](https://github.com/NTARI-RAND/Agrinet) — protocole de réseau
  agricole fédéré
- [SoHoLINK](https://github.com/NTARI-RAND/SoHoLINK) ·
  [Cloudy](https://github.com/NTARI-RAND/Cloudy) ·
  [sohocloud-protocol](https://github.com/NTARI-RAND/sohocloud-protocol) —
  couche Substrat
- [lighthouse](https://github.com/NTARI-RAND/lighthouse) ·
  [shelter](https://github.com/NTARI-RAND/shelter) ·
  [childcare-trust-network](https://github.com/NTARI-RAND/childcare-trust-network) ·
  [shanina](https://github.com/NTARI-RAND/shanina) ·
  [COER](https://github.com/NTARI-RAND/COER) ·
  [world-chase-tag](https://github.com/NTARI-RAND/world-chase-tag) — amorces et
  instances de la couche Économie et Information

Les amorces se conforment à la norme ; la forme s'adapte, les planchers
s'imposent.

## Vérifier le document

La suite est l'échelon porteur : elle rattache le texte à un registre
d'invariants dotés d'identifiants stables, de sorte que le document et le
registre ne peuvent diverger sans que la vérification échoue. Bibliothèque
standard uniquement, aucune dépendance.

```
python jfa-conformance-suite.py                 # check the document
python jfa-conformance-suite.py --list          # print the invariant registry
python jfa-conformance-suite.py --doc PATH      # check another copy
python jfa-conformance-suite.py --project PATH  # check a repo's open-questions deliverable
```

Code de sortie 0 lorsque chaque vérification exécutée réussit, 1 sinon.
Exécutez-la après toute modification du document officiel.

Sur les 26 invariants enregistrés, 3 sont rattachés ici, à la couche du
document, et 23 sont **délégués** — ils engagent un logiciel en fonctionnement
ou un instrument de gouvernance, et ne peuvent être appliqués que par des tests
placés à côté de ce code ou de cet instrument. Ils figurent dans le registre avec
des identifiants stables et sont rapportés comme délégués et non rattachés
jusqu'à ce qu'un dépôt livre des tests citant ces identifiants. Un dépôt conforme
cite les identifiants ; tant qu'il ne le fait pas, sa conformité est
auto-attestée. Rapporter ici un invariant délégué comme « vérifié » serait de
l'auto-attestation déguisée en lanceur de tests ; c'est pourquoi le substitut est
plutôt étiqueté comme tel.

## Pas encore publié ici

La conception des mécanismes de litige — « la conception des mécanismes de
litige » telle que la définit le §1.5 des
[statuts](https://github.com/NTARI-RAND/bylaws) — ainsi que les articles sur la
structure et la robotique sont conservés dans le dépôt documentaire de NTARI et
ne figurent pas encore dans ce dépôt.

## Licence

Deux licences, comme l'indique le pied de page du document lui-même :

| Quoi | Licence |
|---|---|
| La spécification — le document officiel, ses traductions et les instruments antérieurs | [CC BY-SA 4.0](LICENSE-SPEC) |
| Le logiciel — la suite de conformité | [AGPL-3.0](LICENSE) |
