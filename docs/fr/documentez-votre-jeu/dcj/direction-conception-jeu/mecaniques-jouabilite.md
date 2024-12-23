---
title: Mécaniques de Jouabilité
parent: Direction de Conception du Jeu
nav_order: 2
permalink: /DCJ/direction-conception-jeu/mecaniques-jouabilite/
last_modified_date: Dec 14 2024 at 11:52 PM
---

## Table of Contents
- [Mécaniques de Jouabilité](#mécaniques-de-jouabilité)
  - [Mécanismes de Jouabilité de Base](#mécanismes-de-jouabilité-de-base)
  - [Défis et Progression du Joueur](#défis-et-progression-du-joueur)
    - [Facteurs de Rejouabilité](#facteurs-de-rejouabilité)
  - [Systèmes d'Interaction](#systèmes-dinteraction)
    - [Structure des Interactions](#structure-des-interactions)
    - [UI/Contrôles du Jeu](#uicontrôles-du-jeu)

---
# Mécaniques de Jouabilité

---

## Mécanismes de Jouabilité de Base

**Boucle de Jouabilité de Base**  
Définissez la séquence principale des actions que les joueurs répètent tout au long du jeu (par exemple, explorer, collecter, améliorer).

**Éléments de Jouabilité de Base**  
Identifiez les mécanismes de jouabilité clés qui définissent l'expérience de base, tels que la vitesse, l'action, les mécaniques au tour par tour ou les éléments stratégiques.

**Flux de Jouabilité**  
Le Flux de Jouabilité doit fournir une description détaillée, étape par étape, des actions du joueur, y compris comment il interagit avec le monde du jeu, progresse à travers les défis et influence la narration. Il doit décrire l'évolution de la difficulté, les extensions de la jouabilité de base, et l'intégration des éléments de l'UI, comme les menus et le HUD, qui améliorent l'expérience. Expliquez également comment les résultats immédiats et les conséquences à long terme des décisions du joueur façonnent la progression du jeu et l'engagement du joueur.

---

## Défis et Progression du Joueur

**Difficulté et Accessibilité**

- **Options de Difficulté (optionnel)** :  
Décrivez comment votre jeu offre des défis évolutifs pour s'adapter aux joueurs de différents niveaux de compétence. Par exemple, vous pourriez inclure des options comme des modes facile, normal et difficile, ou des fonctionnalités telles que l'assistance à la visée, des aides visuelles ou d'autres outils pour améliorer l'accessibilité selon les besoins des joueurs.

- **Échelle de Difficulté** :  
Décrivez comment la difficulté dans votre jeu évolue au fil du temps. Cela pourrait inclure des aspects comme la difficulté des ennemis, la complexité des énigmes ou des défis de niveau. Vous pouvez aussi décrire comment les joueurs progressent, comme en montant en niveau, en débloquant des capacités ou en atteignant des étapes clés de l’histoire. Considérez comment ces systèmes interagissent avec les options de difficulté ou les fonctionnalités d'accessibilité incluses.

- **Options d'Assistance Visuelle et Audio** :  
Incluez des outils comme les sous-titres ou les modes pour daltoniens.

**Systèmes de Progression**  
Expliquez comment les joueurs avancent dans le jeu (par exemple, monter en niveau, débloquer des compétences).

**Objectif et/ou Objectifs**

- **Objectif Principal** :  
Décrivez le principal objectif global du jeu qui motive la narration et la jouabilité.  
- **Objectifs (optionnels)** :  
Fournissez un plan pour tout objectif supplémentaire que les joueurs peuvent poursuivre, comme des missions secondaires ou des tâches supplémentaires.

**Motivation du Joueur**  
Expliquez pourquoi atteindre ces objectifs est engageant et significatif pour le joueur.

Exemple :  
*"Sauver le royaume procure un sentiment d'héroïsme, tandis que compléter les objectifs secondaires récompensera les joueurs avec des capacités uniques et une immersion plus profonde dans le monde."*

### Facteurs de Rejouabilité

**Génération Procédurale** :  
Inclure du contenu aléatoire ou dynamique pour garder le jeu frais.

**Multiples Fins ou Chemins** :  
Offrir des récits ramifiés ou des résultats pilotés par le joueur.

**Fonctionnalités New Game+** :  
Améliorer la rejouabilité avec des défis supplémentaires ou des déblocages après la première partie.

**Système de Sauvegarde** :  
Décrivez comment les joueurs peuvent sauvegarder leur progression, charger des jeux sauvegardés et rejouer au jeu, y compris les options de sauvegarde automatique et manuelle.

---

## Systèmes d'Interaction

**Systèmes de Combat ou d'Interaction (si partie principale de votre jeu)**  
Brève description des interactions joueur-ennemi, ou d'engagements non-combattants comme des énigmes ou de la diplomatie.

**Actions et Contrôles du Joueur**

**Mouvements** :  
- Décrivez comment les joueurs déplacent leur personnage dans le monde du jeu (par exemple, marcher, courir, s'accroupir).
- Spécifiez les méthodes d'entrée (par exemple, WASD ou les flèches pour le clavier, joystick pour la manette).
- Incluez les mécaniques de mouvement spéciales (par exemple, grimper, glisser, nager, foncer).

**Saut** :  
- Décrivez comment les joueurs font sauter leur personnage, y compris toute entrée de contrôle supplémentaire pour la hauteur ou la distance (par exemple, maintenir le bouton de saut pour un saut plus haut).
- Spécifiez les mécaniques uniques (par exemple, double saut, saut mural).

**Attaquer** :  
- Détaillez comment les joueurs effectuent des attaques, qu'elles soient au corps à corps (par exemple, trancher avec une épée) ou à distance (par exemple, tirer).
- Décrivez les contrôles pour initier les attaques, y compris toute mécanique de combo ou d'attaque spéciale.
- Incluez des variations d'entrée en fonction des armes ou des capacités (par exemple, appuyer sur un bouton différent pour une arme à distance par rapport à une arme de mêlée).

**Interagir** :  
- Définissez les actions pour interagir avec les objets ou les PNJ (par exemple, appuyer sur un bouton pour ouvrir des portes, parler aux PNJ, ramasser des objets).
- Spécifiez toute interaction contextuelle (par exemple, appuyer sur un bouton près d'un objet spécifique pour déclencher une action unique).

**Capacités ou Pouvoirs Spéciaux** :  
- Listez toutes les capacités spéciales du personnage (par exemple, sorts magiques, mode furtif, boucliers).
- Décrivez comment ces capacités sont activées (par exemple, maintenir un bouton ou sélectionner depuis un menu).
- Détaillez les temps de recharge, la gestion des ressources ou les systèmes d'énergie associés à ces capacités.

**Contrôles de la Caméra** :  
- Si applicable, expliquez comment les joueurs contrôlent la caméra (par exemple, en utilisant la souris ou le joystick droit).
- Décrivez si la caméra est fixe, à la première personne ou à la troisième personne, et comment elle réagit aux mouvements ou actions du joueur.

**Actions Supplémentaires** :  
- Incluez toute autre action unique que le joueur peut effectuer, comme la fabrication, la résolution d'énigmes, l'utilisation de gadgets ou l'interaction avec l'environnement de manière spécifique.
- Spécifiez les entrées de contrôle pour ces actions et comment elles contribuent à la jouabilité.

**Trucs et Easter Eggs**  
- Mentionnez les codes de triche ou les easter eggs que les joueurs peuvent découvrir, améliorant la rejouabilité ou ajoutant du contenu fun, non essentiel.

---

### Structure des Interactions

**Structure du Dialogue** :  
Précisez comment les structures de dialogue sont conçues et mises en œuvre (par exemple, sous forme d'arbres de dialogue, de machines d'état ou d'objets scriptables). Incluez des détails sur les méthodes d'entrée pour interagir avec les dialogues (par exemple, des roues de sélection ou des menus basés sur du texte). Mentionnez comment le système prend en compte le contexte, comme les réponses dynamiques en fonction des choix du joueur ou des états du monde.

**Choix et Conséquences** :  
Détaillez comment les décisions du joueur impactent des éléments de gameplay tels que les objectifs, les alliés ou la disponibilité des ressources. Expliquez le cadre pour associer les décisions narratives aux résultats du gameplay (par exemple, des arbres de décision, des systèmes basés sur des indicateurs ou des déclencheurs d'événements). Décrivez comment les choix du joueur persistent à travers les niveaux ou les fichiers de sauvegarde, et comment les chemins divergents affectent des variables comme la progression des quêtes, la disponibilité des alliés ou les changements environnementaux.

**Intelligence Artificielle (IA)** :  
Décrivez si les PNJ se déplaceront en fonction de la recherche de chemin, éviteront les obstacles ou prendront des décisions en combat comme le ciblage et le positionnement. Expliquez s'ils réagiront aux actions du joueur ou aux changements environnementaux, tels que répondre au bruit ou être attaqués en embuscade. Indiquez si leur comportement s'adapte à la difficulté du jeu. Précisez si les concepteurs de niveaux peuvent contrôler ces comportements via des fichiers de configuration, des scripts ou d'autres méthodes. Mentionnez également si des rôles comme les donneurs de quêtes, les marchands ou les ennemis sont programmés pour soutenir l'histoire et le gameplay du jeu.

**Gestion des Ressources** :  
Détaillez les systèmes impliquant la collecte et l'utilisation des ressources (par exemple, l'inventaire, l'artisanat).

---

### UI/Contrôles du Jeu

**Conception de l'Interface Utilisateur (UI)** :  
Fournissez une description détaillée de l'UI du jeu, y compris l'HUD, les menus, le système d'inventaire et la façon dont les joueurs interagissent avec ces éléments.

**Schéma de Contrôle** :  
Définissez comment les joueurs contrôlent le jeu, y compris les dispositions des boutons pour les différentes plateformes (clavier/souris, manette). Mettez en évidence les actions clés et les mappages des entrées.

**Fonctionnalités d'Accessibilité dans les Contrôles** :  
Spécifiez les contrôles personnalisables ou les fonctionnalités d'assistance telles que le remappage des boutons, les schémas de contrôle alternatifs pour les joueurs handicapés ou les dispositifs adaptatifs.

**Exigences Fonctionnelles** :  
Définissez une ventilation de chaque écran, fenêtre et menu, détaillant les actions des utilisateurs et les résultats souhaités. Incluez des actions comme les clics de boutons, les curseurs et les interactions, et envisagez de fournir des diagrammes et des maquettes. Décrivez comment les interactions évolueront pendant l'implémentation et comment elles se rapportent aux spécifications techniques.

**Diagramme de Flux de Navigation de l'UI** :  
Créez un diagramme de flux illustrant la navigation à travers les différents écrans, fenêtres et menus. Utilisez un outil comme Visio ou similaire pour connecter des boîtes étiquetées et numérotées représentant les différents éléments de l'interface. Cela aide à visualiser le parcours du joueur et le flux des tâches.

**Objets GUI** :  
Listez tous les objets GUI qui doivent être programmés, y compris les boutons, les icônes, les curseurs, les composants de l'HUD et autres éléments interactifs. Fournissez une description de leur comportement et de la façon dont le joueur interagit avec eux. Incluez des détails concernant leur fonction dans le jeu et leur comportement lorsqu'ils sont cliqués ou activés.

**Paramètres et Options de Personnalisation** :  
Listez les paramètres que les joueurs peuvent personnaliser, y compris les options graphiques, les préférences sonores, les méthodes d'entrée et toutes autres préférences. Décrivez comment ces paramètres sont accessibles via l'UI et comment ils affectent le gameplay.

**Maquettes** :  
Incluez des maquettes simples/schémas pour tous les écrans, menus et fenêtres, même si la conception finale n'est pas encore disponible. Il peut s'agir de dessins au trait ou de wireframes de base qui aident à communiquer la vision de l'UI. Évitez de créer des œuvres d'art polies à ce stade ; concentrez-vous sur la clarté et la fonctionnalité. Cela sera donné au directeur artistique pour utilisation et perfection dans le Document d'Art du Jeu par les artistes.

**Textes et Messages à l'Écran** :  
Définissez tous les messages textuels à l'écran, y compris les indices du tutoriel, les messages d'erreur et les notifications. Décrivez leur format général, leur style et leur comportement. Expliquez comment ces messages interagissent avec le joueur, y compris le timing, les déclencheurs et la visibilité.
