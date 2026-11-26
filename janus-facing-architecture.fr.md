> Traduction communautaire (version préliminaire) — Politique P2-002 de NTARI, Diffusion mondiale multilingue. Source : janus-facing-architecture.md (original en anglais, instantané du 2026-10-08). Version préliminaire communautaire assistée par machine, en attente de révision par le mainteneur régional conformément à P2-002 §3.1. Les spécifications techniques centrales demeurent en anglais conformément au §2.2.
>
> Vous avez repéré une erreur dans cette traduction ? Votre correction est une
> contribution bienvenue et appréciée : créez un fork du dépôt du projet NTARI
> et ouvrez une pull request, ou écrivez-nous à info@ntari.org.

# JFA : l'architecture bifrons (Janus Facing Architecture)

## Introduction

Chaque membre d'une économie est un **prosommateur** — non seulement un consommateur, mais en même temps un producteur de quelque chose de valeur, même s'il n'a que son temps à offrir (Toffler, 1980). Personne ne se tient d'un seul côté d'un échange ; les deux visages sont la même personne.

L'architecture bifrons (Janus Facing Architecture) est nommée d'après le dieu romain qui regarde dans deux directions à la fois, parce que c'est ce que fait chaque prosommateur : chacun fait face à des exigences de production et de consommation, en même temps. Elle permet aux communautés de traiter la réalité économique du prosumérisme, et offre la possibilité de transformer le modèle d'émission : passer d'une monnaie chartale exogène — émise par une autorité extérieure à la communauté (Knapp, 1924) — à un crédit mutuel endogène, émis par les membres les uns envers les autres au fil de leurs transactions (Moore, 1988 ; Greco, 2009).

Le second visage du nom est politique. Acemoglu et Robinson (2019) montrent que la liberté ne survit qu'à l'intérieur d'un corridor étroit, où un État capable — le Léviathan — est égalé par une société tout aussi capable de le contrôler. Hors du corridor, le Léviathan prend ses autres formes : absent, et la coordination échoue ; despotique, et le coordinateur domine les coordonnés ; de papier, et les contrepouvoirs existent sur le papier mais non en effet. Rester dans le corridor exige ce qu'ils appellent l'effet Reine Rouge : l'État et la société courant ensemble, chacun développant sa capacité parce que l'autre le fait. Toute plateforme économique est un Léviathan en miniature — elle coordonne, fait appliquer et enregistre — et les plateformes dominantes d'aujourd'hui sont despotiques par construction : elles évoluent à la vitesse du réseau tandis que les institutions censées les contrôler avancent à la vitesse des réunions.

Les travaux de NTARI situent cet échec dans l'infrastructure elle-même. Les systèmes délibératifs sont une culture matérielle : l'architecture d'une plateforme matérialise une théorie de qui peut savoir et de qui peut décider, et les architectures de diffusion dominantes traitent les participants comme des destinataires passifs (NTARI, 2025b). L'écart de vitesse qui en résulte est structurel : l'information circule à la vitesse des réseaux tandis que la synthèse démocratique reste arrimée à des cycles électoraux cadencés par une horloge postale (NTARI, 2025a). JFA est conçue pour combler cet écart depuis l'intérieur, disciplinée couche par couche par le coût du départ. C'est un Léviathan enchaîné, en code.

L'architecture bifrons (JFA) s'organise en cinq couches fonctionnelles — Substrat, Registre, Pacte, Gouvernance, et Économie et Information (E&I) — chacune mise en œuvre sur trois niveaux : le frontend, pour la collaboration entre prosommateurs ; l'orchestrateur, un backend assurant une coordination chevauchante entre communautés géographiques ; et le protocole sous-jacent, le modèle de traitement sécurisé des données entre les niveaux.

Le logiciel JFA est conçu pour être publié et géré dans un environnement copyleft, généralement la Licence publique générale Affero de GNU, version 3 ou ultérieure (AGPL-3.0-or-later), ce qui permet à de nouveaux frontends, fédérations, protocoles et architectures d'évoluer sur le marché mondial, formant un commun du logiciel libre.

Ceci est le document officiel, dont Network Theory Applied Research Institute, Inc. assure l'intendance. Les instruments antérieurs sont conservés dans [Historical Docs](Historical%20Docs/) ; les concepts qui en sont issus sont consignés dans le [triage des concepts](jfa-concept-triage-2026-08-24.md) ; ce qui demeure non résolu est nommé dans [OPEN-QUESTIONS.md](OPEN-QUESTIONS.md).

## Pourquoi c'est important

Tout système qui coordonne des personnes exerce un pouvoir sur elles, qu'il le veuille ou non. Ce n'est pas un défaut ; la coordination l'exige. Mais le pouvoir ne reste sain que lorsque quelque chose le contrôle — non un contrepouvoir de papier, mais des personnes réelles, avec un intérêt réel, assez proches pour agir. La plupart des plateformes avancent désormais à la vitesse du réseau tandis que tout ce qui est censé leur demander des comptes avance à la vitesse des réunions, et un contrepouvoir qui arrive en retard n'en est pas un. La réponse de JFA est de cesser de traiter la coordination et la redevabilité comme deux systèmes : même logiciel, mêmes personnes, même vitesse.

## Principes

**Responsabilité partagée.** La communauté qui coordonne l'économie est la même communauté qui contrôle cette coordination. Les deux fonctions s'échangent continuellement — jamais séparées en gouvernants et gouvernés.

**Discipline institutionnelle.** Chaque couche est disciplinée par le coût du départ — ce qu'un membre perd en s'en allant, et ce qu'une communauté perd en excluant quelqu'un. Là où partir est peu coûteux, la concurrence discipline : les couches Substrat et Économie et Information. Là où partir est coûteux, les membres votent : les couches Pacte et Gouvernance. Là où partir est catastrophique, les décisions restent ouvertes à la contestation : la couche Registre. Chaque couche nomme ci-dessous son propre coût, parce que c'est ce coût qui décide de la manière dont un différend s'y règle.

**Code sobre et auditable.** Le logiciel de protocole reste réduit, ne dépend de rien d'autre que de la bibliothèque standard de son langage, et est auditable dans son intégralité.

## Couche Substrat

C'est le matériel où tout se produit, détenu par des prosommateurs de processeurs, de cartes graphiques, d'imprimantes, de stockage et de capteurs.

Partir d'ici est peu coûteux, et le refus d'un transporteur ne coûte à un prosommateur rien d'autre qu'une connexion. Un orchestrateur qui refuse d'acheminer votre capacité n'a pris ni votre matériel, ni vos soldes, ni votre historique, et un autre orchestrateur n'est qu'à une offre publiée de distance. Les querelles à cette couche ne sont donc pas arbitrées : un acheminement qui reste sans attestation dans sa fenêtre d'engagement est simplement annulé, personne ne statue dessus, et un transporteur qui refuse ou échoue trop librement est évincé par la concurrence plutôt que saisi en appel.

### Niveau protocole

Échange instructions et ordres sur un marché distribué de calcul et de stockage, exploité sur des ordinateurs grand public hébergés dans des domiciles, des bureaux et des entrepôts, ainsi que sur du matériel industriel reconverti.

Les nœuds rejoignent ce marché par des réseaux superposés chiffrés (overlays) et une interrogation sortante (polling), sans exiger de ports entrants ouverts ni d'adresse statique ; la connexion telle qu'un fournisseur résidentiel la livre suffit. La ligne 11 en dépend : un substrat qui ne fonctionnerait que là où un fournisseur autorise le service entrant porterait un point d'étranglement chez chaque fournisseur.

Le travail du substrat est garanti en intégrité, non en confidentialité : un hôte peut lire ce que son nœud calcule. Le travail dont le résultat règle une dépense ou entre au registre s'exécute sur au moins deux hôtes indépendants, et leur désaccord est noté, jamais tenu pour fiable.

### Niveau orchestrateur

Puissance de calcul fédérée de prosommateurs, créant davantage d'options à travers la géographie. Les orchestrateurs publient des offres de transport sur le marché du substrat, chacune nommant un tarif, un engagement de livraison et une clé publique ; toute plateforme peut sélectionner tout orchestrateur joignable, de sorte qu'un transporteur dominant est évincé par la concurrence plutôt que régulé. Le transport est de la livraison, non de l'exécution : un orchestrateur achemine des dépenses signées jusqu'à l'ensemble des témoins et rapporte des attestations, n'est jamais chargé de déterminer si un échange a eu lieu, et peut être à pertes et fondé sur les réessais.

### Niveau frontend

Interface Économie et Information pour prosommer du calcul et du stockage.

## Couche Registre

Une fonction rémunérée du substrat, qui enregistre et sert le dialogue entre les couches Économie et Information et Pacte à destination du public.

Le registre de ce qui s'est produit est conservé par six parties : les deux prosommateurs de l'échange, l'opérateur, l'orchestrateur et deux témoins conservent chacun leur propre registre. Les empreintes sont en outre engagées sur une chaîne publique unique, distribuée sur le substrat — le registre pour tous ceux qui n'en conservent aucun en propre. Les engagements de chaque échange acheminé par un orchestrateur sont copiés sur la chaîne et stockés sur du substrat financé par l'organisation d'intendance de la couche Gouvernance, de sorte que le registre qui lie les communautés entre elles n'est payé par aucune d'elles. La chaîne est en ajout seul : le préjudice est pardonné par annotation, jamais par effacement. Une plateforme doit compter au moins deux témoins indépendants ; en deçà, un déploiement doit s'étiqueter lui-même comme non fédéré. Les témoins sont désignés par un tirage au sort amorcé depuis la chaîne publique, que quiconque peut vérifier, et sont payés par le marché du substrat, jamais par l'opérateur qu'ils observent.

Personne ne peut être effacé du registre, et le quitter est catastrophique. Ce qui a été engagé n'est jamais effacé, mais aucune copie unique n'est le registre, et chaque copie ne dure qu'aussi longtemps qu'elle est conservée : celle de l'orchestrateur, avec le dernier acheminement payé ; celles des témoins, tant que leur stockage est payé ; celles des prosommateurs et de l'opérateur, jusqu'à ce qu'ils cessent de les conserver ; et celle de la chaîne, tant que son stockage est financé. Le registre survit dans les copies qui demeurent ; la chaîne est stockée par le substrat plutôt que par l'opérateur, de sorte qu'elle peut survivre à l'opérateur, au frontend et à la querelle, et ce qu'elle porte au-delà de chaque détenteur est le fait de l'engagement, non le contenu. Parce que rien ne peut être effacé du registre, aucun constat n'y est jamais définitif : une entrée contestée reçoit une réponse par annotation, et l'annotation est aussi permanente que l'entrée à laquelle elle répond.

Un échange intercommunautaire demeure deux dépenses souveraines. La citation qui le règle porte aussi le tarif de transport de l'orchestrateur, placé sous séquestre avec l'échange à l'initiation et libéré par cette même citation. La libération est conjointe et tout ou rien — si la livraison n'est pas attestée dans la fenêtre d'engagement de l'offre, toutes les dépenses sont annulées — et l'attestation propre de l'orchestrateur ne compte pas pour le seuil qui libère son propre tarif. Le tarif est réparti entre les grands livres d'origine des deux prosommateurs dont l'échange a été acheminé, chacun payant sa part dans sa propre unité ; rien ne franchit une frontière communautaire. Le crédit qu'il rapporte est conservé par les six mêmes parties, cité par clé. La livraison est attestée par les seuls témoins ; l'opérateur conserve son registre d'un acheminement et n'en atteste jamais.

### Niveau protocole

Capture, catégorise et hache chaque transmission au sein de la pile, afin d'établir la réputation via la couche Pacte et de fonder un moyen d'échange via Économie et Information.

### Niveau orchestrateur

Fédère les registres à travers la géographie, permettant réputation et échange partagés. Ce que la fédération partage, c'est de la vérité enregistrée — réputation et historique des échanges — jamais une unité monétaire.

### Niveau frontend

L'achat et la vente de stockage de registre à travers le substrat, rémunérant les prosommateurs qui conservent le registre.

## Couche Pacte

Un contrat social appliqué par le code, qui informe des attentes souples pour les interactions entre prosommateurs.

Partir d'ici est coûteux. Un prosommateur banni d'une plateforme conserve le registre de chaque notation qu'il y a gagnée — six parties le détiennent — mais la position que ce registre porte ne le suit pas par défaut : sur la plateforme suivante, le décompte des échanges à chaque niveau de notation se reconstruit un échange attesté à la fois. Ce prix est la raison pour laquelle un bannissement repose sur des preuves arbitrées plutôt que sur la parole d'un opérateur. Lorsque des manquements apparents au pacte se produisent, les opérateurs de plateforme arbitrent entre leurs prosommateurs ; les litiges qui traversent les plateformes, et les litiges entre un prosommateur et l'opérateur de sa propre plateforme, sont arbitrés à la couche des témoins — aucun opérateur n'arbitre un litige auquel il est partie. Où que l'arbitrage ait lieu, les parties à celui-ci notent l'arbitre — l'opérateur entre ses propres prosommateurs, les témoins autrement — de sorte que les arbitres se tiennent à l'intérieur du système de réputation qu'ils font appliquer.

Parce que partir est coûteux, les membres votent ici : la fédération du Pacte vote les changements conceptuels et programmatiques du pacte (l'échelle d'évaluation des échanges fondée sur Leveson, Leveson-Based Trade Assessment Scale, LBTAS), de son API et de son orchestration, et commande des études formelles des effets du pacte choisi sur ses utilisateurs.

### Niveau protocole

Une évaluation simple, écrite en code exécutable, permettant aux prosommateurs de noter leurs interactions mutuelles à travers la pile.

### Niveau orchestrateur

Une API servant des évaluations conformes à travers les marchés Économie et Information de la pile, depuis les prosommateurs du substrat.

### Niveau frontend

L'interface Économie et Information où l'API est servie.

## Couche Gouvernance

C'est là, et c'est ainsi, que les êtres humains s'assemblent pour agir collectivement sur la pile.

Partir d'ici est coûteux, et c'est la seule couche où l'exclusion atteint le logiciel lui-même : un membre exclu de l'Institut perd, pour une durée bornée, le vote qui façonne ce que tous les autres exécutent. L'exclusion n'est donc jamais la décision d'un opérateur — elle est renvoyée à la fédération de Gouvernance et décidée par le vote de ses membres conformément aux statuts, et consignée au registre.

### Niveau protocole

Organisation à but non lucratif d'intendance de logiciels copyleft.

### Niveau orchestrateur

L'adhésion au Network Theory Applied Research Institute, obtenue en exploitant une instance fédérée de logiciel JFA ou en participant comme prosommateur sur une plateforme fédérée.

### Niveau frontend

La coordination synchrone et asynchrone des membres, régie par les statuts de l'organisation.

## Couche Économie et Information

La couche Économie et Information est hébergée sur le substrat, syndiquée avec la couche Registre, et facilite le respect du pacte.

Partir d'ici est peu coûteux par construction. Un opérateur peut bannir un prosommateur de sa plateforme, mais non de ce qu'il y a bâti : les positions et l'historique survivent à tout frontend, de sorte que les bannis partent avec leur registre intact et leurs soldes toujours dus. Un bannissement est une perte de marché, non une perte de position — et un opérateur dont les conditions ou la limite de crédit font fuir les prosommateurs perd le commerce plutôt que de gagner la dispute.

### Niveau protocole

Chaque plateforme économique ou informationnelle dispose d'un protocole conçu pour l'échange qui s'y déroule (par exemple l'agriculture, un jeu, ou des citations de recherche). Chacun suppose que tout hôte du substrat peut lire ce qu'il calcule.

### Niveau orchestrateur

L'Économie et Information doit fonctionner sur du matériel révocable, obtenu et enregistré par la couche substrat. Une plateforme n'a pas besoin d'orchestrateur en propre : elle en sélectionne un sur le marché du substrat et paie le transport à même l'échange.

### Niveau frontend

Les conceptions de frontend des plateformes Économie et Information doivent être personnalisables par l'utilisateur.

## Les lignes qui ne peuvent être franchies

Une implémentation qui franchit l'une de ces lignes n'est pas un JFA réduit ; c'est un autre logiciel portant le nom.

1. Tout crédit est une reconnaissance de dette (IOU), créée au moment où deux membres échangent — un solde baisse, un autre monte, la somme étant toujours nulle. C'est la seule manière dont la monnaie vient à exister : rien n'est frappé, rien n'est émis de l'extérieur, et rien ne s'accumule en intérêts.
2. Le crédit se gagne, ne s'achète jamais, et n'est jamais convertible en monnaie fiduciaire.
3. La monnaie de chaque communauté est souveraine — pas d'unité commune, pas de conversion entre communautés.
4. La valeur reste chez elle ; seule la vérité circule.
5. L'échange intercommunautaire consiste en deux dépenses souveraines liées atomiquement par la chaîne publique — pas de chambre de compensation, pas de taux de change.
6. Le registre est en ajout seul — le préjudice se pardonne par annotation, jamais par effacement.
7. Aucun récit, aucune identité dans le registre partagé — empreintes, types, horodatages et références uniquement.
8. La réputation n'est jamais un chiffre unique — ce que les autres voient, c'est le décompte des échanges à chaque niveau de notation.
9. La réputation décide si un membre échange sur la confiance ; une limite commune à toute la communauté, fixée par l'opérateur et jamais dérivée de la réputation, décide de combien.
10. Un déploiement commence sous séquestre — collatéralisé, sans soldes négatifs, sans crédit accordé entre contreparties — et passe à un système de crédit mutuel hybride ou complet seulement après que l'opérateur a développé sa capacité, que le réseau de prosommateurs a été notifié, et que les autorisations locales de fournir des services de crédit mutuel ont été publiées à la couche de gouvernance — ou, lorsque la juridiction n'en exige aucune, qu'un constat en ce sens y a été publié à la place — et qu'un passage au crédit mutuel complet a été ratifié par les prosommateurs du déploiement.
11. Aucun hôte, compte ou fournisseur unique dont le retrait pourrait arrêter le réseau.
12. Les positions et l'historique d'un membre survivent à tout frontend ; les registres d'une communauté survivent à tout opérateur.

## Références

Acemoglu, D., & Robinson, J. A. (2019). *The Narrow Corridor: States, Societies, and the Fate of Liberty*. Penguin Press.

Greco, T. H. (2009). *The End of Money and the Future of Civilization*. Chelsea Green Publishing.

Knapp, G. F. (1924). *The State Theory of Money*. Macmillan. (Œuvre originale publiée en 1905)

Moore, B. J. (1988). *Horizontalists and Verticalists: The Macroeconomics of Credit Money*. Cambridge University Press.

Network Theory Applied Research Institute. (2025a, octobre). *Addressing democratic information velocity* (P1-002). https://www.ntari.org/post/ntari-whitepaper-addressing-democratic-information-velocity

Network Theory Applied Research Institute. (2025b, juin). *The material culture of democratic deliberation*. https://www.ntari.org/post/the-material-culture-of-democratic-deliberation

Toffler, A. (1980). *The Third Wave*. William Morrow.

---

*Network Theory Applied Research Institute, Inc. — 501(c)(3) — EIN 92-3047136 — info@ntari.org*

*Logiciel : AGPL-3.0-or-later · Spécification : CC BY-SA 4.0*
