---
title: Interactions
parent: Gameplay Mechanics
nav_order: 3
permalink: /GDD/game-design-direction/gameplay-mechanics/interactions/
last_modified_date: Dec 14 2024 at 11:52 PM
---

## Table of Contents
- [Interactions](#interactions)
  - [Interaction Systems](#interaction-systems)
    - [Combat or Interaction Systems (if main part of your game)](#combat-or-interaction-systems-if-main-part-of-your-game)
    - [Player Actions and Controls](#player-actions-and-controls)
      - [Movements](#movements)
      - [Jumping](#jumping)
      - [Attacking](#attacking)
      - [Interacting](#interacting)
      - [Special Abilities or Powers](#special-abilities-or-powers)
      - [Camera Controls](#camera-controls)
      - [Additional Actions](#additional-actions)
      - [Cheats and Easter Egg](#cheats-and-easter-egg)
  - [Interaction Structure](#interaction-structure)
    - [Dialogue Structure](#dialogue-structure)
    - [Choice and Consequence](#choice-and-consequence)
    - [Artificial Intelligence (AI)](#artificial-intelligence-ai)
    - [Resource Management](#resource-management)

---

# Interactions

## Interaction Systems

### Combat or Interaction Systems (if main part of your game)
Short description of player-enemy interactions, or non-combat engagement like puzzles or diplomacy.

### Player Actions and Controls

#### Movements
- Describe how players move their character within the game world (e.g., walking, running, crouching).
- Specify input methods (e.g., WASD or arrow keys for keyboard, joystick for gamepad).
- Include any special movement mechanics (e.g., climbing, sliding, swimming, dashing).

#### Jumping
- Outline how players make the character jump, including any additional control inputs for height or distance (e.g., holding the jump button for a higher jump).
- Specify any unique mechanics (e.g., double jump, wall jumping).

#### Attacking
- Detail how players perform attacks, whether melee (e.g., sword slashing) or ranged (e.g., shooting).
- Describe the controls for initiating attacks, including any combos or special attack mechanics.
- Include input variations based on different weapons or abilities (e.g., pressing a different button for a ranged weapon versus a melee weapon).

#### Interacting
- Define the actions for interacting with objects or NPCs (e.g., pressing a button to open doors, talk to NPCs, pick up items).
- Specify any contextual interaction (e.g., pressing a button when near a specific object to trigger a unique action).

#### Special Abilities or Powers
- List any special abilities the character has (e.g., magic spells, stealth mode, shields).
- Describe how these abilities are activated (e.g., holding a button or selecting from a menu).
- Detail any cooldowns, resource management, or energy systems associated with these abilities.

#### Camera Controls
- If applicable, explain how players control the camera (e.g., using the mouse or right joystick).
- Outline whether the camera is fixed, first-person, or third-person, and how it responds to player movement or actions.

#### Additional Actions
- Include any other unique actions that the player can perform, such as crafting, solving puzzles, using gadgets, or interacting with the environment in specific ways.
- Specify the control inputs for these actions and how they contribute to gameplay.
  
#### Cheats and Easter Egg
- Mention any cheat codes or Easter eggs that players can discover, enhancing replayability or adding fun, non-essential content.

---

## Interaction Structure

### Dialogue Structure
Specify how dialogue branching structures are designed and implemented (e.g., as dialogue trees, state machines, or scriptable objects). Include details on input methods for interacting with dialogue (e.g., selection wheels or text-based menus). Mention how the system accounts for context, such as dynamic responses based on player choices or world states.

### Choice and Consequence
Detail how player decisions impact gameplay elements like objectives, allies, or resource availability. Explain the framework for mapping narrative decisions to gameplay outcomes (e.g., decision trees, flag-based systems, or event-driven triggers). Describe how player choices persist across levels or save files, and how branching paths affect variables like quest progression, ally availability, or environmental changes.

### Artificial Intelligence (AI)
Describe if NPCs will move based on pathfinding, avoid obstacles, or make combat decisions like targeting and positioning. Explain if they will react to player actions or environmental changes, such as responding to noise or being ambushed. Indicate if their behavior adapts to the game’s difficulty. Specify if level designers can control these behaviors through configuration files, scripts, or other methods. Also, mention if roles like quest-givers, merchants, or enemies are programmed to support the game’s story and gameplay.


### Resource Management
Detail systems involving collection and utilization of resources (e.g., inventory, crafting).