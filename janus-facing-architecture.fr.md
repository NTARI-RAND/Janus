> Traduction communautaire (version préliminaire) — Politique P2-002 de NTARI, Diffusion mondiale multilingue. Source : janus-facing-architecture.md (original en anglais, instantané du 2026-08-31). Version préliminaire communautaire assistée par machine, en attente de révision par le mainteneur régional conformément à P2-002 §3.1. Les spécifications techniques centrales demeurent en anglais conformément au §2.2.
>
> Vous avez repéré une erreur dans cette traduction ? Votre correction est une
> contribution bienvenue et appréciée : créez un fork du dépôt du projet NTARI
> et ouvrez une pull request, ou écrivez-nous à info@ntari.org.

# JFA : l'architecture bifrons (Janus Facing Architecture)

## Introduction

L'architecture bifrons — nommée d'après le dieu romain qui regarde dans deux directions à la fois, tout comme chaque participant économique fait face à des exigences de production et de consommation — permet aux communautés de traiter la réalité économique du prosumérisme. Chaque membre d'une économie n'est pas seulement un consommateur, mais un prosommateur (Toffler, 1980), produisant simultanément quelque chose de valeur même s'il n'a que son temps à offrir. Elle offre également la possibilité de transformer le modèle d'émission : passer d'une monnaie chartale exogène (émise par une autorité extérieure à la communauté) à un crédit mutuel endogène (émis par les membres les uns envers les autres au fil de leurs transactions).

Le second visage du nom est politique. Acemoglu et Robinson (2019) montrent que la liberté ne survit qu'à l'intérieur d'un corridor étroit, où un État capable — le Léviathan — est égalé par une société tout aussi capable de le contrôler. Hors du corridor, le Léviathan prend ses autres formes : absent, et la coordination échoue ; despotique, et le coordinateur domine les coordonnés ; de papier, et les contrepouvoirs existent sur le papier mais non en effet. Rester dans le corridor exige ce qu'ils appellent l'effet Reine Rouge : l'État et la société courant ensemble, chacun développant sa capacité parce que l'autre le fait. Toute plateforme économique est un Léviathan en miniature — elle coordonne, fait appliquer et enregistre — et les plateformes dominantes d'aujourd'hui sont despotiques par construction : elles évoluent à la vitesse du réseau tandis que les institutions censées les contrôler avancent à la vitesse des réunions.

Les travaux de NTARI situent cet échec dans l'infrastructure elle-même. Les systèmes délibératifs sont une culture matérielle : l'architecture d'une plateforme matérialise une théorie de qui peut savoir et de qui peut décider, et les architectures de diffusion dominantes traitent les participants comme des destinataires passifs (NTARI, 2025b). L'écart de vitesse qui en résulte est structurel : l'information circule à la vitesse des réseaux tandis que la synthèse démocratique reste arrimée à des cycles électoraux cadencés par une horloge postale (NTARI, 2025a). JFA est conçue pour combler cet écart depuis l'intérieur : la communauté qui coordonne est la communauté qui contrôle, les deux capacités s'échangeant continuellement dans le même logiciel à la même vitesse, disciplinées couche par couche par le coût du départ. C'est un Léviathan enchaîné, en code.

L'architecture bifrons (JFA) s'organise en cinq couches fonctionnelles — Substrat, Registre, Pacte, Gouvernance, et Économie et Information (E&I) — chacune mise en œuvre sur trois niveaux : le frontend, pour la collaboration entre prosommateurs ; l'orchestrateur, un backend assurant une coordination chevauchante entre communautés géographiques ; et le protocole sous-jacent, le modèle de traitement sécurisé des données entre les niveaux.

Le logiciel JFA est conçu pour être publié et géré dans un environnement copyleft, généralement la Licence publique générale Affero de GNU, ce qui permet à de nouveaux frontends, fédérations, protocoles et architectures d'évoluer sur le marché mondial, formant un commun du logiciel libre.

Ceci est le document officiel, dont Network Theory Applied Research Institute, Inc. assure l'intendance. Les instruments antérieurs sont conservés dans [Historical Docs](Historical%20Docs/) ; les concepts qui en sont issus sont consignés dans le [triage des concepts](jfa-concept-triage-2026-08-24.md) ; ce qui demeure non résolu est nommé dans [OPEN-QUESTIONS.md](OPEN-QUESTIONS.md).

## Principes

**Responsabilité partagée.** La communauté qui coordonne l'économie est la même communauté qui contrôle cette coordination. Les deux fonctions s'échangent continuellement — jamais séparées en gouvernants et gouvernés.

**Discipline institutionnelle.** Chaque couche est disciplinée par le coût du départ : là où partir est peu coûteux, la concurrence discipline ; là où partir est coûteux, les membres votent ; là où partir est impossible, les décisions restent ouvertes à la contestation.

**Code sobre et auditable.** Le logiciel de protocole reste réduit, ne dépend de rien d'autre que de la bibliothèque standard de son langage, et est auditable dans son intégralité.

## Couche Substrat

C'est le matériel où tout se produit, détenu par des prosommateurs de processeurs, de cartes graphiques, d'imprimantes, de stockage et de capteurs.

### Niveau protocole

Échange instructions et ordres sur un marché distribué de calcul et de stockage, exploité sur des ordinateurs grand public hébergés dans des domiciles, des bureaux et des entrepôts, ainsi que sur du matériel industriel reconverti.

### Niveau orchestrateur

Puissance de calcul fédérée de prosommateurs, créant davantage d'options à travers la géographie.

### Niveau frontend

Interface E&I pour prosommer du calcul et du stockage.

## Couche Registre

Une fonction rémunérée du substrat, qui enregistre et sert le dialogue entre les couches E&I et Pacte à destination du public.

Le registre de ce qui s'est produit est conservé de six façons. Chaque partie à une transaction conserve son propre registre ; l'opérateur conserve le sien ; deux témoins conservent les leurs ; et les empreintes sont engagées sur une chaîne publique unique, distribuée sur le substrat — le registre pour tous ceux qui n'étaient ni transacteurs, ni témoins, ni opérateur. La chaîne est en ajout seul : le préjudice est pardonné par annotation, jamais par effacement. Une plateforme doit compter au moins deux témoins indépendants ; en deçà, un déploiement doit s'étiqueter lui-même comme non fédéré.

### Niveau protocole

Capture, catégorise et hache chaque transmission au sein de la pile, afin d'établir la réputation via la couche Pacte et de fonder un moyen d'échange via E&I.

### Niveau orchestrateur

Fédère les registres à travers la géographie, permettant réputation et échange partagés. Ce que la fédération partage, c'est de la vérité enregistrée — réputation et historique des échanges — jamais une unité monétaire.

### Niveau frontend

Service rémunéré de calcul et d'enregistrement fourni par des prosommateurs sur la couche substrat d'E&I.

## Couche Pacte

Un contrat social appliqué par le code, qui informe des attentes souples pour les interactions entre prosommateurs.

### Niveau protocole

Une évaluation simple, écrite en code exécutable, permettant aux prosommateurs de noter leurs interactions mutuelles à travers la pile.

### Niveau orchestrateur

Une API servant des évaluations conformes à travers les marchés E&I de la pile, depuis les prosommateurs du substrat. Lorsque des manquements apparents au pacte se produisent, les opérateurs de plateforme arbitrent entre leurs prosommateurs ; les litiges qui traversent les plateformes sont arbitrés à la couche des témoins. Les arbitres sont notés sur leur conduite par les deux prosommateurs ou opérateurs concernés.

### Niveau frontend

L'interface E&I où l'API est servie.

## Couche Gouvernance

C'est là, et c'est ainsi, que les êtres humains s'assemblent pour agir collectivement sur la pile.

### Niveau protocole

Organisation à but non lucratif d'intendance de logiciels copyleft.

### Niveau orchestrateur

L'adhésion au Network Theory Applied Research Institute, obtenue en exploitant une instance fédérée de logiciel JFA.

### Niveau frontend

La coordination synchrone et asynchrone des membres, régie par les statuts de l'organisation.

## Couche Économie et Information

La couche E&I est hébergée sur le substrat, syndiquée avec la couche Registre, et facilite le respect du pacte.

### Niveau protocole

Chaque plateforme économique ou informationnelle dispose d'un protocole conçu pour l'échange qui s'y déroule (par exemple l'agriculture, un jeu, ou des citations de recherche).

### Niveau orchestrateur

E&I doit fonctionner sur du matériel révocable, obtenu et enregistré par la couche substrat.

### Niveau frontend

Les conceptions de frontend des plateformes E&I doivent être personnalisables par l'utilisateur.

## Les lignes qui ne peuvent être franchies

Une implémentation qui franchit l'une de ces lignes n'est pas un JFA réduit ; c'est un autre logiciel portant le nom.

1. La monnaie est créée au moment de l'échange — un solde baisse, un autre monte, la somme étant toujours nulle.
2. Le crédit se gagne, ne s'achète jamais, et n'est jamais convertible en monnaie fiduciaire.
3. La monnaie de chaque communauté est souveraine — pas d'unité commune, pas de conversion entre communautés.
4. La valeur reste chez elle ; seule la vérité circule.
5. L'échange intercommunautaire consiste en deux dépenses souveraines liées atomiquement par la chaîne publique — pas de chambre de compensation, pas de taux de change.
6. Le registre est en ajout seul — le préjudice se pardonne par annotation, jamais par effacement.
7. Aucun récit, aucune identité dans le registre partagé — empreintes, types, horodatages et références uniquement.
8. La réputation n'est jamais un chiffre unique — ce que les autres voient, c'est le décompte des échanges à chaque niveau de notation.
9. La réputation décide si un membre échange sur la confiance ; une limite commune à toute la communauté, fixée par l'opérateur et jamais dérivée de la réputation, décide de combien.
10. Un déploiement commence sous séquestre — collatéralisé, sans soldes négatifs, sans crédit accordé entre contreparties — et passe à un système de crédit mutuel hybride ou complet seulement après que l'opérateur a développé sa capacité, que le réseau de prosommateurs a été notifié, et que les autorisations locales de fournir des services de crédit mutuel ont été publiées à la couche de gouvernance — ou, lorsque la juridiction n'en exige aucune, qu'un constat en ce sens y a été publié à la place.
11. Aucun hôte, compte ou fournisseur unique dont le retrait pourrait arrêter le réseau.
12. Les positions et l'historique d'un membre survivent à tout frontend ; les registres d'une communauté survivent à tout opérateur.

## Références

Acemoglu, D., & Robinson, J. A. (2019). *The Narrow Corridor: States, Societies, and the Fate of Liberty*. Penguin Press.

Network Theory Applied Research Institute. (2025a, octobre). *Addressing democratic information velocity* (P1-002). https://www.ntari.org/post/ntari-whitepaper-addressing-democratic-information-velocity

Network Theory Applied Research Institute. (2025b, juin). *The material culture of democratic deliberation*. https://www.ntari.org/post/the-material-culture-of-democratic-deliberation

Toffler, A. (1980). *The Third Wave*. William Morrow.

---

*Network Theory Applied Research Institute, Inc. — 501(c)(3) — EIN 92-3047136 — info@ntari.org*
