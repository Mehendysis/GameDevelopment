---
title: DCA
parent: Documentez Votre Jeu
nav_order: 3
permalink: /DCA/
last_modified_date: Dec 14 2024 at 11:52 PM
---

## Table of Contents
- [Document de Conception Artistique (DCA)](#document-de-conception-artistique-dca)
  - [Organisation des Ressources Artistiques](#organisation-des-ressources-artistiques)
  - [Style Visuel](#style-visuel)
    - [Conception de l'UI](#conception-de-lui)
  - [Conception Audio](#conception-audio)
    - [Intégration du Doublage Vocal:](#intégration-du-doublage-vocal)
    - [Répartition de l'Utilisation de la Musique](#répartition-de-lutilisation-de-la-musique)
    - [Audio Adaptatif](#audio-adaptatif)
    - [Audio Cinématographique et de Niveau](#audio-cinématographique-et-de-niveau)
    - [Stratégie de Test Audio](#stratégie-de-test-audio)
    - [Effets Sonores](#effets-sonores)
  - [Conception Audiovisuelle des Niveaux](#conception-audiovisuelle-des-niveaux)
  - [Conception Narrative](#conception-narrative)
    - [Guide du Jeu](#guide-du-jeu)

---

# Document de Conception Artistique (DCA)

Le Document de Conception Artistique, également connu sous le nom de Bible de l'Art, Guide de Style Visuel ou Guide de Style Artistique, sert de référence complète pour la direction artistique de notre jeu.

---

## Organisation des Ressources Artistiques
- **Gestion des Ressources Artistiques** : Établir un système clair et structuré pour organiser toutes les ressources artistiques et les partager avec les parties prenantes du projet. Utiliser une plateforme centrale pour le stockage des ressources et le contrôle de version, comme Git, Perforce ou un système basé sur le cloud tel que Google Drive ou Dropbox pour un accès facile et une collaboration.
  
- **Contrôle de Version** : Implémenter un système de contrôle de version (par exemple, Git, Perforce, Google Drive, One Drive, etc.) pour suivre les modifications des ressources artistiques et prévenir les conflits. Assurez-vous que tous les fichiers artistiques sont correctement versionnés et évitez d'écraser les fichiers à moins que cela ne soit nécessaire. Utilisez des branches pour les changements importants et fusionnez-les lorsqu'elles sont prêtes.
  
- **Stockage Centralisé & Contrôle de Version** : Utiliser des plateformes telles que Git, Perforce ou le stockage cloud (Google Drive, Dropbox) pour un accès facile, la collaboration et le contrôle de version.
- **Organisation des Fichiers** : Organiser les ressources en catégories claires pour les éléments 2D, 3D et cinématiques :
  - **Art 2D** : Art marketing, éléments de gameplay (par exemple, icônes, boutons, sprites de joueur/ennemi).
  - **Art 3D** : Modèles, textures, animations, effets spéciaux (par exemple, modèles de personnages, accessoires d'environnement).
  - **Cinématiques & Vidéo** : Scènes cinématiques, FMV, séquences scriptées, et ressources vidéo (par exemple, intro, transitions, scènes de fin).
  - **GUI** : Clics de boutons, ouverture de fenêtres, confirmations de commandes.
  - **Effets Spéciaux** : Tir de fusils, explosions, bip de radar.
  - **Unités/Personnages** : Enregistrements vocaux, bavardage radio, bruits de pas, collisions.
  - **Éléments de Gameplay** : Jingle de ramassage, alertes, sons ambiants.
  - **Terrain (Environnement)** : Oiseaux, sons de jungle, grillons, craquements.
  - **Mouvement** : Vent, bruits de pas, planchers qui craquent, marche dans l'eau, bruit de pas dans les flaques.

- **Nomination des Fichiers & Structure des Dossiers** : Maintenir une convention de nommage cohérente et une structure de dossiers organisée pour un accès facile aux fichiers et un suivi efficace.

---

## Style Visuel
- **Direction Artistique et Esthétique** : Décrire l'apparence générale et l'ambiance (par exemple, stylisé, réaliste).
- **Style Graphique** : Décrire le style général et le mode graphique, avec des références à d'autres jeux ou médias pour comparaison. Inclure des croquis de personnages, d'environnements et de l'UI.
- **Objectifs Artistiques** : Définir les motifs, caractéristiques, le style, l'ambiance et les couleurs pour l'art du jeu. Assurez-vous de l'alignement avec les artistes principaux et le directeur de projet.
- **Caractéristiques Graphiques** : Mettre en évidence les techniques uniques (par exemple, cel-shading, photoréalisme).
- **Philosophie de Conception des Personnages et Environnements** : Définir les principes de conception pour les personnages et les décors.
- **Maquettes Préliminaires** : Si des œuvres d'art détaillées sont indisponibles au début du développement, se concentrer sur la description de la vision ; l'art détaillé peut être créé plus tard par des artistes qualifiés.
- **Art Conceptuel et Aides Visuelles** : Inclure des croquis, des maquettes ou des visuels sources pour communiquer clairement les idées.
- **Ressources Artistiques et Droits d'Auteur** : Spécifier toute œuvre d'art externe utilisée, créditer correctement les sources, et confirmer la conformité aux lois sur les droits d'auteur pour éviter tout problème juridique.

### Conception de l'UI
- **Style de l'UI et Langage Visuel** : Définir le style global et les principes de conception de l'interface utilisateur (UI). Cela inclut les styles de boutons, la typographie, les palettes de couleurs et l'iconographie.
- **Structure des Menus et Navigation** : Décrire la structure des menus principaux, des éléments de l'UI en jeu (par exemple, HUD, écrans d'inventaire), et comment le joueur interagit avec eux.
- **Éléments Interactifs** : Définir la façon dont les éléments de l'UI réagissent aux actions du joueur (par exemple, pressions sur les boutons, effets au survol, animations).
- **HUD et Affichage en Jeu** : Détaillez la conception des informations à l'écran que les joueurs verront pendant qu'ils jouent (par exemple, barres de santé, objectifs de quêtes, mini-cartes).
- **Accessibilité et Lisibilité** : Veiller à ce que la conception de l'UI soit accessible à tous les joueurs, y compris ceux ayant des déficiences visuelles ou d'autres handicaps.
- **Ressources et Actifs de l'UI** : Spécifier toute ressource externe utilisée pour les éléments de l'UI, tels que des icônes, des polices ou des kits d'UI préfabriqués. Assurez-vous de donner les crédits appropriés et que toutes les ressources soient conformes légalement.

---

## Conception Audio

- **Style Musical** : Définir clairement le genre de musique pour le jeu, en faisant référence à des styles ou compositeurs bien connus pour plus de clarté.  
- **Utilisation de la Musique** : Lister toutes les pistes musicales et où elles sont utilisées. Décrire l'humeur et les thèmes, en notant quand les thèmes doivent se répéter. Collaborer avec le compositeur pour une bonne intégration.
- **Audio Adaptatif** : Expliquer comment la musique s'adapte dynamiquement au gameplay, comme augmenter l'intensité pendant les combats ou changer de thème pendant l'exploration.  
- **Immersion** : Décrire l'approche pour créer des effets sonores immersifs qui améliorent le gameplay et l'atmosphère.  
- **Priorisation** : Chaque action devrait avoir un son. Prioriser les sons importants pour éviter les chevauchements. Spécifier si les sons seront enregistrés, synthétisés ou provenant de sources. Le style musical doit être clair, avec des exemples pour référence. Décrire comment la musique s'adaptera au gameplay.
- **Processus de Création** : Spécifier si les effets sonores seront enregistrés, synthétisés ou issus de bibliothèques.

### Intégration du Doublage Vocal:
- **Doublages** : Détaillez comment les doublages vocaux seront intégrés dans la narration et le gameplay.
- **Casting** : Définissez le ton, la langue et les accents des personnages, par exemple, une voix rugueuse pour un guerrier, un ton calme pour un narrateur.
- **Intégration du Script** : Expliquez comment les doublages s'intégreront dans le gameplay, par exemple, des répliques déclenchées par les actions du joueur, des arbres de dialogue ramifiés.

### Répartition de l'Utilisation de la Musique
- **Scénarios Musicaux** : Décrivez où des thèmes musicaux spécifiques seront utilisés.
- **Écran d'Accueil** : Mise en ambiance pour les écrans de titre et de crédits, par exemple, de la musique orchestrale calme.
- **Génériques d'Événements** : Succès/échec/mort/victoire/découverte, par exemple, une musique joyeuse pour la victoire.
- **Thèmes de Niveaux** : Musique spécifique à chaque niveau, par exemple, une musique tendue pendant les zones de combat.
- **Musique Situationnelle** : Musique pour des situations spécifiques comme un danger imminent ou de l'exploration, par exemple, des tonalités ambiantes et inquiétantes pour la furtivité.
- **Bandes Sonores Cinématiques** : Musique sur mesure pour les séquences cinématiques.

### Audio Adaptatif
- **Changements Dynamiques de Musique** : Décrivez comment la musique s'adaptera aux dynamiques du gameplay.
- **Combat** : La musique devient intense et rapide lorsque des ennemis sont proches.
- **Exploration** : La musique passe à des tonalités calmes et atmosphériques pendant l'exploration.
- **Audio Ambiant** : Faites boucler sans interruption les sons environnementaux comme le vent ou les bruits de forêt en fonction de la localisation.

### Audio Cinématographique et de Niveau
- **Synchronisation Audiovisuelle** : Assurez-vous que l'audio soutient l'expérience visuelle en associant le son aux éléments visuels.
- **Explosions** : L'audio se synchronise avec les explosions et destructions à l'écran.
- **Coupures Cinématiques** : Les dialogues et effets sonores renforcent les séquences cinématiques, comme les pas pendant une scène tendue.

### Stratégie de Test Audio
- **Contrôle de Qualité** : Listez les étapes de test pour garantir une bonne implémentation de l'audio.
- **Équilibrage du Volume** : Assurez-vous que la musique et les effets sonores sont équilibrés en termes de volume.
- **Placement des Sons** : Testez les sons 3D pour garantir qu'ils correspondent à la position du joueur.
- **Audio Dynamique** : Vérifiez que les transitions musicales adaptatives fonctionnent de manière fluide.

### Effets Sonores
- **Effets Sonores Requis** : Listez tous les effets sonores et leur emplacement. Incluez les noms de fichiers et respectez la convention de nommage convenue avec l'équipe sonore. Prenez en compte tous les éléments du jeu nécessitant un son, comme l'interface utilisateur, les armes, les personnages, l'environnement et les mouvements.

---

## Conception Audiovisuelle des Niveaux
**Style Visuel et Audio**
Décrivez l’aspect et l’ambiance du jeu pour chaque niveau individuellement, et comment cela soutient l’expérience du joueur. Référez-vous aux concepts artistiques ou aux guides visuels pour transmettre l’ambiance souhaitée.

- **Thèmes Spécifiques aux Niveaux** : Décrivez le ton visuel et audio de chaque niveau, soutenu par des références comme des concepts artistiques ou des mood boards.
- **Intégration de l'Audio** : Décrivez comment la musique de fond, les effets sonores et l'audio ambiant contribuent à l'atmosphère du niveau.

**Liste de Contrôle de la Conception des Niveaux**
  - **Conception Visuelle** : Assurez-vous que l'art de chaque niveau correspond à l'esthétique voulue, y compris le terrain, l'éclairage et les éléments de l'environnement.
  - **Conception Audio** : Vérifiez que la musique de fond, les effets sonores et le doublage de chaque niveau correspondent au ton et à l'atmosphère.
  - **Interactivité** : Confirmez que les éléments de gameplay tels que les obstacles, ennemis et objets à collectionner sont visuellement distincts et clairs.
  - **Cinématiques** : Vérifiez que les cinématiques de chaque niveau améliorent le flux narratif et se fondent harmonieusement dans le gameplay.
  - **Intégration de l'UI** : Assurez-vous que les éléments de l'interface utilisateur sont clairs, fonctionnels et bien intégrés à l'environnement sans obstruer le gameplay.
  - **Performance** : Vérifiez que les éléments visuels et audio de chaque niveau fonctionnent de manière optimale sans compromettre l'expérience du joueur.

---

## Conception Narrative
La section **Conception Narrative** dans un GDD se concentre sur l’histoire du jeu, les personnages et la construction du monde. Elle définit comment les éléments narratifs sont intégrés au gameplay pour créer une expérience cohérente et immersive.

**Histoire**
- **Origines du Monde** : Esquissez brièvement l'histoire du monde du jeu. Quels événements ont façonné le monde avant que le jeu ne commence ? Y a-t-il des contes mythologiques, des guerres ou des percées scientifiques qui définissent le cadre ?
- **Factions et Pouvoirs** : Détaillez les factions clés, leurs motivations et leurs rôles dans la narration.
- **Modèle de Structure de l’Intrigue** : Définissez le modèle narratif qui structure l’histoire du jeu. Spécifiez si l’intrigue suit un format traditionnel comme la structure en 3 actes, le Voyage du Héros, la narration épique, ou un autre modèle. Cela aide à établir le flux des événements et garantit que l’histoire se déroule de manière cohérente au fil du temps.
- **Perspective et Livraison Narrative** : Décrivez la perspective à partir de laquelle l’histoire est racontée (par exemple, à la première personne, à la troisième personne, omnisciente). De plus, décrivez les méthodes de livraison narrative (par exemple, dialogues, cinématiques, narration environnementale) et comment ces méthodes sont intégrées tout au long du gameplay.
- **Conflit Central** : Décrivez la lutte principale qui pousse le jeu. Le conflit est-il personnel (par exemple, vengeance, survie) ou de plus grande envergure (par exemple, une bataille entre factions, une rébellion, une catastrophe) ?
- **Progression et Séquencement de l’Histoire** : Expliquez comment l’intrigue du jeu progresse du début à la fin. Esquissez les moments clés de l’histoire, les principaux tournants, et comment le joueur vit ces événements. Indiquez si l’histoire est linéaire ou non linéaire, et les développements majeurs de l’intrigue qui sont débloqués selon les actions ou décisions du joueur.
- **Rôle du Joueur dans le Monde** : Mettez en évidence l’importance du joueur dans l’histoire. Comment le protagoniste s’intègre-t-il dans le conflit ? Est-il un sauveur, un rebelle, un élu ou un spectateur entraîné dans les événements ?
- **Incident Déclencheur** : Définissez l'événement qui lance le jeu. Que se passe-t-il au début du jeu pour pousser le protagoniste à l’action ?
- **État Actuel du Monde** : Déterminez l'état actuel du monde lorsque le jeu commence. Le monde est-il en chaos, en train de se remettre d'une catastrophe, ou prospère avec des menaces cachées ?
- **Thèmes et Tonalité** : Définissez les thèmes sous-jacents et le ton émotionnel de la narration. L’histoire du jeu parle-t-elle d’espoir, de désespoir, de découverte ou de pouvoir ? Quelle ambiance le joueur doit-il ressentir (par exemple, sombre, fantasque, mystérieuse) ?
- **Relations et Dynamiques entre les Personnages** : Détaillez les interactions entre les personnages et leurs relations avec le joueur et entre eux. Décrivez comment ces relations évoluent tout au long du jeu, telles que les alliances, rivalités et conflits. Mettez en évidence les personnages dont les relations avec le joueur influencent l’intrigue ou le gameplay.

**Conception des Personnages**  
- **Personnages Principaux** : Définir les personnages principaux, leur personnalité et leur signification narrative.  
- **Personnages Secondaires** : Décrire les personnages secondaires et leur rôle dans l'enrichissement de l'histoire.  
- **Arcs des Personnages** : Résumer comment les personnages évoluent au fil de l'histoire.  

**Construction du Monde**  
- **Lieux** : Détaillez les principaux lieux, leur signification et les thèmes visuels/sonores associés.  
- **Lore et Mythologie** : Expliquer la lore sous-jacente ou les mythes qui enrichissent le monde.  

**Monde du Jeu**  
- **Cadre et Atmosphère** : Décrire le monde du jeu, la période, le lieu et l'ambiance.  
- **Disposition de la Carte Dirigée par la Narration** : Décrire comment le terrain et la conception des niveaux reflètent la progression de l'histoire (par exemple, une ville en ruines révélant des secrets à mesure que le joueur avance).  
- **Chemins du Joueur** : Mettre en évidence les parcours possibles que les joueurs peuvent emprunter dans chaque niveau ou section de la carte, y compris les chemins optionnels ou secrets qui enrichissent la narration.  
- **Changements Dynamiques du Monde** : Expliquer comment les actions ou décisions du joueur influencent l'environnement (par exemple, déverrouiller des zones, modifier le terrain ou déclencher des événements).  
- **Thèmes des Niveaux et Intégration de l'Histoire** : Relier chaque section de la carte ou thème de niveau aux moments clés de l'histoire, garantissant une expérience narrative cohérente.  
- **Incitations à l'Exploration** : Définir les récompenses ou découvertes narratives liées à l'exploration de zones hors des sentiers battus, comme des éléments de lore, des objets à collectionner ou des histoires secondaires.  

**Système de Personnage**  
- **Conception du Personnage Joueur et Compétences** : Définir l'apparence, les compétences et l'histoire du protagoniste.  
- **Histoires des Personnages (PNJ)** : Fournir des histoires détaillées et des motivations pour les personnages non-joueurs.  
- **Modes d'Expression** : Mettre en évidence la manière dont les personnages s'expriment, y compris des phrases caractéristiques, des manières ou des bizarreries.  

**Éléments Narratifs**  
- **Structure de l'Histoire et Méthode de Livraison** : Expliquer comment l'intrigue se déroule (par exemple, cinématiques, narration environnementale).  
- **Arbre de Dialogue** : Définir les conversations entre le joueur et les personnages (par exemple, choix ramifiés, dialogues doublés).  
- **Arbre des Choix et Conséquences** : Cartographier comment les décisions narratives influencent l'histoire et les fins.  
- **Événements Dirigés par la Narration** : Décrire comment les événements narratifs impactent le gameplay, tels que les quêtes, les cinématiques ou la narration environnementale.  

### Guide du Jeu  
Fournir un guide étape par étape de la séquence d'événements clés du jeu, des objectifs majeurs et des moments pivots. Cela aide à visualiser la progression de l'histoire ou du gameplay.
