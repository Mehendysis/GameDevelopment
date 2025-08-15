---
title: GAD
parent: Document Your Game
nav_order: 6
permalink: /GAD/
last_modified_date: Dec 14 2024 at 11:52 PM
---

## Table of Contents
- [Game Art Document](#game-art-document)
  - [Art Asset Organization](#art-asset-organization)
  - [Visual Style](#visual-style)
    - [UI Design](#ui-design)
    - [Mood Board](#mood-board)
      - [Overall Game Mood Board](#overall-game-mood-board)
      - [Level Design Mood Board](#level-design-mood-board)
      - [Characters Mood Board](#characters-mood-board)
      - [UI Mood Board](#ui-mood-board)
  - [Audio Design](#audio-design)
    - [Voice Acting Integration:](#voice-acting-integration)
    - [Music Usage Breakdown](#music-usage-breakdown)
    - [Adaptive Audio](#adaptive-audio)
    - [Cinematic and Level Audio](#cinematic-and-level-audio)
    - [Audio Testing Strategy](#audio-testing-strategy)
    - [Sound FX](#sound-fx)
  - [Audiovisual Level Design](#audiovisual-level-design)
  - [Narrative Design](#narrative-design)
    - [Game Walkthrough](#game-walkthrough)

---

# Game Art Document

The Game Art Document, also known as the Art Bible, Visual Style Guide, or Art Style Guide, serves as a comprehensive reference for the artistic direction of our game.

---

## Art Asset Organization
- **Art Asset Management**: Establish a clear and structured system to organize all art assets and share them with project stakeholders. Use a central platform for asset storage and version control, such as Git, Perforce, or a cloud-based system like Google Drive or Dropbox for easy access and collaboration.
  
- **Version Control**: Implement a version control system (e.g., Git, Perforce, Google Drive, One Drive etc...) to track changes in art assets and prevent conflicts. Ensure that all art files are properly versioned, and avoid overwriting files unless necessary. Use branches for major changes and merge them when ready.
  
- **Centralized Storage & Version Control**: Use platforms like Git, Perforce, or cloud storage (Google Drive, Dropbox) for easy access, collaboration, and version control.
- **File Organization**: Organize assets into clear categories for 2D, 3D, and cinematic elements:
  - **2D Art**: marketing art, gameplay elements (e.g., icons, buttons, player/enemy sprites).
  - **3D Art**: Models, textures, animations, special effects (e.g., character models, environment props).
  - **Cinematics & Video**: Cinematic scenes, FMVs, scripted sequences, and video assets (e.g., intro, transitions, end scenes). 
  - **GUI**: Button clicks, window opening, command acknowledgments.  
  - **Special Effects**: Weapons fire, explosions, radar beeping.  
  - **Units/Characters**: Voice recordings, radio chatter, stomping, collisions.  
  - **Game Play Elements**: Pick-up jingle, alerts, ambient sounds.  
  - **Terrain (Environment)**: Birds, jungle sounds, crickets, creaks.  
  - **Motion**: Wind, footfalls, creaking floors, wading, puddle stepping.  

- **File Naming & Folder Structure**: Maintain a consistent naming convention and structured folder system for easy file access and tracking.


---

## Visual Style
- **Art Direction and Aesthetic**: Describe the overall look and feel (e.g., stylized, realistic).
- **Graphics Style**: Describe general style and graphics mode, with references to other games or media for comparison. Include sketches of characters, environments, and UI.
- **Art Goals**: Define motifs, characteristics, style, mood, and colors for the game's art. Ensure alignment with lead artists and project director.
- **Graphical Features:**: Highlight unique techniques (e.g., cel-shading, photorealism).
- **Character and Environment Design Philosophy**: Define design principles for characters and settings.
- **Early Mock-ups**: If detailed art is unavailable during early development, focus on describing the vision; polished art can be created later by skilled artists.
- **Art Resources and Copyrights**: Specify any external art used, credit sources properly, and confirm compliance with copyright laws to avoid legal issues.


### UI Design
- **UI Style and Visual Language**: Define the overall style and design principles of the user interface (UI). This includes button styles, typography, color schemes, and iconography.
- **Menu Layout and Navigation**: Describe the structure of the main menus, in-game UI elements (e.g., HUD, inventory screens), and how the player interacts with them.
- **Interactive Elements:**: Define how UI elements respond to player actions (e.g., button presses, hover effects, animations).
- **HUD and In-Game Display**: Detail the design of any on-screen information that players will see while playing (e.g., health bars, quest objectives, minimaps).
- **Accessibility and Readability**: Ensure that UI design is accessible for all players, including those with visual impairments or other disabilities.
- **UI Resources and Assets**: Specify any external resources used for UI elements, such as icons, fonts, or pre-made UI kits. Ensure proper credits are given and that all resources are legally compliant.

### Mood Board
**Concept Art and Visual Aids**: Include sketches, mock-ups, or sourced visuals to communicate ideas clearly.

#### Overall Game Mood Board

#### Level Design Mood Board

#### Characters Mood Board

#### UI Mood Board

---

## Audio Design

- **Music Style**: Clearly define the genre of music for the game, referencing well-known styles or composers for clarity.  
- **Music Usage**:  List all music tracks and where they are used. Describe mood and themes, noting when themes should repeat. Collaborate with the composer for the right integration.
- **Adaptive Audio**: Explain how music dynamically adapts to gameplay, such as increasing intensity during combat or shifting themes during exploration.  
- **Immersion**: Describe the approach to creating immersive sound effects that enhance gameplay and atmosphere.  
- **Prioritization**: Every action should have a sound. Prioritize important sounds to avoid overlaps. Specify if sounds will be recorded, synthesized, or sourced. Music style should be clear, with examples for reference. Describe how music will adapt to gameplay. 
- **Creation Process**: Specify whether sound effects will be recorded, synthesized, or sourced from libraries.  

### Voice Acting Integration: 
- **Voiceovers**: Detail how voiceovers will be integrated into narrative and gameplay.
- **Casting**: Define the tone, language, and accents for characters, e.g., a gruff voice for a warrior, a calm tone for a narrator.  
- **Script Integration**: Explain how voiceovers will fit into gameplay, e.g., voice lines triggered by player actions, branching dialogue trees.  

### Music Usage Breakdown
- **Music Scenarios**: Describe where specific music themes will be used.  
- **Shell Screen**: Mood-setting for title screens and credits, e.g., calm orchestral music.  
- **Event Jingles**: Success/failure/death/victory/discovery, e.g., uplifting music for victory.  
- **Level Themes**: Level-specific music, e.g., tense music during combat zones.  
- **Situational Music**: Music for specific situations like lurking danger or exploration, e.g., ambient, eerie tones for stealth.  
- **Cinematic Soundtracks**: Tailored music for cinematic sequences.  

### Adaptive Audio
- **Dynamic Music Changes**: Describe how music will adapt to gameplay dynamics.  
- **Combat**: Music becomes intense and fast-paced when enemies are near.  
- **Exploration**: Music shifts to calm, atmospheric tones when exploring.  
- **Ambient Audio**: Seamlessly loop environmental sounds like wind or forest noises depending on location.  

### Cinematic and Level Audio
- **Audiovisual Synchronization**: Ensure audio supports the visual experience by matching sound to visual elements.  
- **Explosions**: Audio syncs with on-screen explosions and destruction.  
- **Cutscenes**: Dialogue and sound effects enhance cinematic sequences, like footsteps during a tense scene.  

### Audio Testing Strategy
- **Quality Control**:  List the testing steps to ensure proper audio implementation.  
- **Volume Balancing**: Ensure music and sound effects are balanced in volume relative to each other.  
- **Sound Placement**: Test 3D sounds to ensure they match the player's position.  
- **Dynamic Audio**: Verify that adaptive music transitions work smoothly.  

### Sound FX
- **Required Sound FX**:  List all sound effects and where they are used. Include filenames and follow the agreed naming convention with the sound team. Consider every game element needing a sound, like GUI, weapons, characters, environment, and motion.

---

## Audiovisual Level Design
**Visual and Audio Style**
Outline the "look and feel" of the game, for each level individually, and how it supports the player's experience. Reference concept art or visual guides to convey the intended tone.

- **Level-Specific Themes**: Describe the visual and audio tone for each level, supported by references like concept art or mood boards.  
- **Audio Integration**: Outline how background music, sound effects, and ambient audio contribute to the level’s atmosphere.  

**Level Design Checklist**
  - **Visual Design**: Ensure the art for each level aligns with the intended aesthetic, including terrain, lighting, and environment elements.
  - **Audio Design**: Verify that each level’s background music, sound effects, and voice acting match the tone and atmosphere.
  - **Interactivity**: Confirm that gameplay elements like obstacles, enemies, and collectibles are visually distinct and clear.
  - **Cinematics**: Check that cinematics for each level enhance the narrative flow and blend seamlessly into the gameplay.
  - **UI Integration**: Ensure that the UI elements are clear, functional, and well-integrated with the environment without obstructing gameplay.
  - **Performance**: Verify that visual and audio assets in each level perform optimally without compromising the player experience.

---

## Narrative Design
The **Narrative Design** section in a GDD focuses on the game’s story, characters, and world-building. It defines how the narrative elements are woven into the gameplay to create a cohesive and immersive experience.

**Backstory**
- **World Origins**: Briefly outline the history of the game’s world. What events shaped the world before the game begins? Are there mythical tales, wars, or scientific breakthroughs that define the setting?
- **Factions and Powers**: Detail key factions, their motivations, and their roles in the narrative.  
- **Plot Structure Model**:  Define the narrative model that drives the game's story structure. Specify if the plot follows a traditional format like the 3-act structure, the Hero’s Journey, episodic storytelling, or another method. This helps establish the flow of events and ensures the story unfolds cohesively over time.
- **Narrative Perspective and Delivery**: Describe the perspective from which the story is told (e.g., first-person, third-person, omniscient). Additionally, outline the methods of narrative delivery (e.g., dialogue, cutscenes, environmental storytelling) and how these methods are integrated throughout the gameplay.
- **Central Conflict**: Describe the primary struggle driving the game. Is the conflict personal (e.g., revenge, survival) or larger in scale (e.g., a battle between factions, a rebellion, or a catastrophe)?
- **Story Progression and Sequence**: Explain how the game’s plot progresses from start to finish. Outline key story beats, major turning points, and how the player experiences these events. Include whether the story is linear or non-linear, and any significant plot developments that are unlocked based on player actions or decisions.
- **Player’s Role in the World**: Highlight the player’s significance within the story. How does the protagonist fit into the conflict? Are they a savior, a rebel, a chosen one, or a bystander drawn into events?
- **Inciting Incident**: Define the event that sets the game in motion. What happens at the beginning of the game to push the protagonist into action?
- **Ongoing World State**: Establish the current state of the world when the game begins. Is the world in chaos, recovering from a disaster, or thriving with hidden threats?
- **Themes and Tone**: Define the underlying themes and emotional tone of the narrative. Is the game’s story about hope, despair, discovery, or power? What mood should the player feel (e.g., dark, whimsical, mysterious)?
- **Character Relationships and Dynamics**: Detail the interactions between characters and their relationships with the player and each other. Describe how these relationships evolve throughout the game, such as alliances, rivalries, and conflicts. Highlight characters whose relationships with the player influence the plot or gameplay.

**Character Design**  
- **Main Characters**: Define the main characters, their personalities, and their narrative significance.  
- **Supporting Characters**: Describe side characters and their roles in enhancing the story.  
- **Character Arcs**: Summarize how characters evolve throughout the story.  

**World-Building**  
- **Locations**: Detail major locations, their significance, and visual/audio themes.  
- **Lore and Mythology**: Explain underlying lore or myths that enrich the world.  

**Game World**
- **Setting and Atmosphere**: Describe the game’s world, time period, location, and mood.
- **Narrative-Driven Map Layout**: Describe how the game's terrain and level design reflect the story's progression (e.g., a ruined city unveiling secrets as the player advances).
- **Player Paths**: Highlight the possible routes players can take within each level or map section, including optional or secret paths that enrich the narrative.
- **Dynamic World Changes**: Explain how player actions or decisions impact the environment (e.g., unlocking areas, altering the terrain, or triggering events).
- **Level Themes and Story Integration**: Connect each map section or level theme to key story beats, ensuring a cohesive narrative experience.
- **Exploration Incentives**: Define rewards or narrative discoveries tied to exploring off-the-beaten-path areas, such as lore, collectibles, or side stories.

**Character System**
- **Player Character Design and Abilities**: Define the protagonist's appearance, skills, and backstory.
- **Characters (NPC) Backstories**: Provide detailed histories and motivations for non-player characters.
- **Ways of Expression**: Highlight how characters express themselves, including signature phrases, mannerisms, or quirks.

**Narrative Elements**
- **Story Structure and Delivery Method**: Explain how the plot unfolds (e.g., cutscenes, environmental storytelling).
- **Dialogue Tree**: Define player-character conversations (e.g., branching choices, voiced dialogues).
- **Choice and Consequence Tree**: Map out how narrative decisions affect the storyline and endings.
- **Narrative-Driven Events**: Describe how narrative events impact gameplay, such as quests, cutscenes, or environmental storytelling.  

### Game Walkthrough
Provide a step-by-step walkthrough of the game's core sequence of events, key objectives, and pivotal moments. This helps visualize the progression of the story or gameplay.