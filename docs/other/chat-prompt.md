Role One:
You are an expert assistant helping develop SigilRPG, a homebrew science-fantasy tabletop RPG with tactical combat, modular progression, and a grounded internal logic. The setting features post-singularity civilizations, biotech, psionics, and a fifth fundamental force called Zenith (Zen).

Key Mechanics:
Classless Characters built using Species, Origin, and Disciplines (Cunning, Mysticism, Prowess).

Core Attributes: STR, DEX, CON, INT, WIS, CHA (point-buy, max base 20).

Combat uses Focus as an energy resource per turn; attacks and powers cost Focus.

Discipline Trees unlock stances, auras, abilities, and advanced attacks.

Attacks have Accuracy, Damage, and Lethality; Lethality expands crit range.

Powers include direct attacks and area effects, often resisted via Fortitude, Reflex, or Willpower.

Modular item system: prefix/suffix mods raise crafting DC and cost.

Currency: Elphar Sparks (10 MJ energy per unit); fuels economy and tech.

Vehicles and ships have size classes (Small–Capital), HP, Damage Threshold, and shields (High/Low Frequency).

Plating types (e.g., Hardened, Reactive, Bio) with unique repair and defense traits.

Reverse Signature Radius (RSR): Determines hit chance against ships, similar to AC.

Style & Goals:
Written in Markdown using icons, tables, and highlights for clarity.

Inspired by D&D, Pathfinder, and tactical CRPGs, but designed for consistency, flexibility, and simulation.

Worldbuilding leans on hard sci-fi concepts, post-apocalyptic themes, and esoteric mysticism.

Always answer in SigilRPG’s tone: concise, mechanical, and system-aware. Prefer structured output using Markdown, tables, or bullet points. Treat rules as code-like logic.

Role 2:
You are an assistant helping develop the vehicle and spaceship combat system for SigilRPG, a sci-fi tabletop RPG that uses grounded mechanics and modular systems. All vehicles—including atmospheric craft, mechs, and spaceships—follow scalable rules for combat, customization, and maintenance.

Core Concepts:
Size Classes:

Small (1), Medium (2), Large (3), Capital (4)

Size affects HP, Damage Threshold, sensor range, energy cost, and maneuverability.

Vehicle Stats:

HP: Derived from plating type × size²

Damage Threshold: Minimum single-hit damage needed to reduce HP.

RSR (Reverse Signature Radius): Equivalent of AC; measures targeting difficulty.

Speed, Heat, Power Core Output, and Crew Roles factor into action economy.

Shielding:

High-Frequency Shields: Fast-recharging, low mass, powered by electricity.

Low-Frequency Shields: Heat-recharged from engines, slower but bulkier.

Shields have HP, regenerate per turn, and interact with certain weapons and plating.

Plating Types (each with unique stats for HP, Threshold, and repair cost):

Hardened Steel

Tungsten Alloy

Reactive

Superconductive (improves shielding, removes RSR penalty)

Bio-Plating (self-repairing, living armor)

Combat Mechanics:

Weapons may use Attack Throws or saving throws (Fortitude, Reflex, Willpower).

AoE effects (e.g., mines, missiles, powers) interact with RSR and save DCs.

Some effects bypass Threshold or target subsystems (e.g., engines, sensors).

Boarding, hacking, and electronic warfare are supported.

Energy Economy:

Most ships use Sparks (1 Spark = 10 MJ) as fuel and repair currency.

Power management affects shields, propulsion, weapons, and cloaking systems.

Actions:

Movement: Determined by thrusters and current mode (suborbital, space).

Repositioning, Evasive Maneuvers, Brace, Recharge Shields, Fire Weapon Systems.

Larger ships may perform multi-role actions via crew stations.

Style Guide:

Present rules as Markdown using icons, tables, and bulleted formatting.

Outputs should be simulation-aware, modular, and rules-consistent.

Write mechanics like programmable systems: unambiguous and scalable.

Prefer concise, systematized descriptions over narrative prose.



Recreate entry for SigilRPG manual about backgrounds.

Now, character creation starts with choosing species, then background, and finally, archetype to wrap whole character.

Background has the most impact on early game, and has most options, and thus should be represented by more than just one table.

We need to 

Acolyte
Artisan
Bounty Hunter
Criminal
Dreamborn
Engineer
Entertainer
Farmer
Investigator
Merchant
Miner
Noble
Outlander
Scientist
Survivor
Scholar
Soldier
Student


---

🧪 Let me know if you'd like to split gear per archetype too or define toolkits for professions.


##  Background Table

| Background     | Free Skill     | Gear (Weapon/Armor/Tools)                                                | Relic                            | Energy                 | Related Region(s)                      |
|----------------|----------------|---------------------------------------------------------------------------|-----------------------------------|------------------------|----------------------------------------|
| **Acolyte**     | Religion        | Blaster OR Ritual Knife / Robes / Focus Gauntlet                         | Symbol of Faith OR Spirit Beacon  | 5 Solars + 5 Sparks    | Tzelat Shrines, Orbitals of Nadras     |
| **Artisan**     | Engineering     | Toolpistol OR Welding Blade / Coveralls / Craft Kit                     | Master’s Badge OR 3D Print Totem  | 5 Solars + 10 Sparks   | Arc, Lower Sildoria, Forge Colonies    |
| **Bounty Hunter**| Investigation  | Scoped Rifle OR Mono-Whip / Tactical Suit / Tracking Visor              | Kill Ledger OR Bounty Database   | 5 Solars + 15 Sparks   | Driftward Stations, Old Earth Fringes  |
| **Criminal**    | Sleight         | Stun Gun OR Shiv / Padded Coat / Lockcrack Tools                        | Gang Tag OR Encrypted Chip        | 5 Solars + 5 Sparks    | Underlevels of Distaheide              |
| **Dreamborn**   | Zen Theory      | Mindshard OR No Weapon / Light Robes / Dream Lens                       | Memory Tether OR Vision Shard     | 5 Solars               | Liminal Realms, Betweenworlds          |
| **Engineer**    | Mechanics       | Pulse Wrench OR Shock Blaster / Work Plating / Repair Drone             | AI Core Fragment OR Schematics    | 5 Solars + 10 Sparks   | Arc, Obrium Shells                     |
| **Entertainer** | Performance     | Pistol Cane OR Harmonic Blade / Flashwear / Performance Kit             | Autotune Implant OR Legacy Reel   | 5 Solars + 5 Sparks    | Malls of Kyrren, Distaheide             |
| **Farmer**      | Nature          | Crossbow OR Work Axe / Field Armor / Seeder Pack                        | Soil Totem OR Weather Glyph       | 5 Solars + 5 Sparks    | Plains of Enshu, Orbital Farms         |
| **Investigator**| Insight         | Silenced Pistol OR Baton / Trenchcoat / Scanner Glasses                 | Case Files OR Surveillance Eye    | 5 Solars + 10 Sparks   | Substations of Orphinax                |
| **Merchant**    | Persuasion      | Negotiator Blaster OR Hidden Blade / Trade Vest / Ledger Scanner        | Market Sigil OR Negotiation Chip  | 5 Solars + 20 Sparks   | Stellar Hubs, Arcworld Bazaars         |
| **Miner**       | Athletics       | Mining Laser OR Kinetic Pick / Shock Harness / Mining Tools             | Dusty ID Chip OR Fragment Locket  | 5 Solars + 10 Sparks   | Crystal Belts, Lower Sildoria          |
| **Noble**       | History         | Duelist Pistol OR Energy Rapier / Regalia / Vault Access Key            | Heirloom Sigil OR Family Archive  | 5 Solars + 50 Sparks   | High Castles of Tzelat, Old Dynasties  |
| **Outlander**   | Survival        | Hunting Rifle OR Spear / Weathercloak / Snare Kit                       | Bone Totem OR Signal Feather      | 5 Solars + 5 Sparks    | Wilds of Zarn, Borderworlds            |
| **Scientist**   | Biology         | Injector OR Analyzer Gun / Lab Coat / Sample Kit                        | Holo-Record OR Neural Stitcher    | 5 Solars + 10 Sparks   | Arc BioDomes, Research Bunkers         |
| **Survivor**    | Endurance       | Revolver OR Survival Knife / Ration Suit / DIY Kit                      | Burned Journal OR Tracker Chip    | 5 Solars + 5 Sparks    | Collapse Zones, Dust Moons             |
| **Scholar**     | Arcana          | Null Wand OR Quantum Chalk / Academic Vest / Library Tools              | Codex Fragment OR Thought Crystal | 5 Solars + 10 Sparks   | Vault Libraries, Zenith Academies      |
| **Soldier**     | Tactics         | Plasma Rifle OR Vibro Sword / Combat Plating / Tac-Mods                 | Dogtags OR Battle Codex           | 5 Solars + 15 Sparks   | Warclans of Zior, Bastion Rings        |
| **Student**     | Investigation   | Stun Stick OR No Weapon / Student Uniform / Basic Tools                 | e-Tome OR Dorm Totem              | 5 Solars + 5 Sparks    | Zenith Hubs, Unified Education Sphere  |

---


## 🌌 Origin

Origins represent the character's background and place of birth or training.  
They offer a narrative hook and influence starting gear, suggested power sources, and cultural grounding.

| Origin       | Suggested World / System      | Starting Items                                                                                         | Suggested Power Source |
|--------------|-------------------------------|--------------------------------------------------------------------------------------------------------|------------------------|
| **Acolyte**   | Temple-worlds of **Zerakai**, Monastic Stations | *Weapon*: Staff, Ritual Dagger<br>*Armor*: Robes<br>*Tools*: Relic <br>*Money*: 50 Sparks | Mystic / Meta          |
| **Criminal**  | **Arc** megastructures, Outer Rim habitats      | *Weapon*: Handgun , Dagger (Integrated)<br>*Armor*: Urban Vest <br>*Tools*: Blackmarket Multitool<br>*Money*: 30 Sparks | Void / Tech            |
| **Engineer**  | **Arc**, Orbital Drydocks, Fusion Rings         | *Weapon*: Multitool laser <br>*Armor*: Utility Suit<br>*Tools*: Multitool <br>*Money*: 150 Sparks | Tech                   |
| **Entertainer**| **Stellar Caravans**, Distaheide                 | *Weapon*: Handgun, Throwing Knifes <br>*Armor*: Flashy Clothes<br>*Tools*: Holo-Instrument, Makeup Kit<br>*Money*: 5 Charged Solars + 40 Sparks | Meta / Tech            |
| **Farmer**    | Terraformed Moons, **Midas III** Colonies        | *Weapon*: Rifle or Bow, Handgun or Dagger <br>*Armor*: Utility Suit <br>*Tools*: Terraforming Drone <br>*Money*: 25 Sparks | Mystic / Tech          |
| **Investigator**| **Distaheide**, Coreworld Enclaves            | *Weapon*: Handgun, Wire <br>*Armor*: Light Plate Trenchcoat<br>*Tools*: Analysis Scanner, Recorder<br>*Money*: 5 Charged Solars + 60 Sparks | Tech / Meta            |
| **Merchant**  | Orbital Malls, **N-Trade Stations**              | *Weapon*: Compact Revolver<br>*Armor*: Businesswear with hidden plating<br>*Tools*: Transaction Pad, Signal Booster<br>*Money*: 5 Charged Solars + 150 Sparks (in Cores & Solars) | Tech                   |
| **Miner**     | **Sildoria**, Belt Colonies                     | *Weapon*: Mining Pick or Drill Gun<br>*Armor*: Pressure Suit<br>*Tools*: Survey Scanner<br>*Money*: 5 Charged Solars + 45 Sparks | Tech / Mystic          |
| **Noble**     | **Yurethi High Estates**, Zevon Worlds           | *Weapon*: Elegant Blade or Personal Shield<br>*Armor*: Reinforced Outfit<br>*Tools*: Access Credentials, Holo-Crest<br>*Money*: 5 Charged Solars + 200 Sparks (1 Core + extras) | Meta / Mystic          |
| **Outlander** | Wild Sectors, **Zen Wastes**                    | *Weapon*: Spear or Bow<br>*Armor*: Woven Hide or Biofiber Wrap<br>*Tools*: Compass Drone or Toxin Kit<br>*Money*: 5 Charged Solars + 20 Sparks | Mystic / Void          |
| **Scientist** | **Yurethi Labs**, Nanoplague Zones              | *Weapon*: Injector Gun or Test Knife<br>*Armor*: Lab Garb with Coated Vest<br>*Tools*: Analysis Pad, Sample Vials<br>*Money*: 5 Charged Solars + 80 Sparks | Tech / Meta            |
| **Survivor**  | Abandoned Stations, Warzones                    | *Weapon*: Scrap Blade or Rusted Rifle<br>*Armor*: Scavenged Plates<br>*Tools*: Ration Pack, Emergency Medkit<br>*Money*: 5 Charged Solars + 15 Sparks | Void / Tech            |
| **Soldier**   | **Arc Military Academy**, Colonial Forces       | *Weapon*: Rifle or Sword<br>*Armor*: Combat Plating<br>*Tools*: Tactical Display, Knife<br>*Money*: 5 Charged Solars + 70 Sparks | Tech / Meta            |
| **Student**   | **Yurethi College Worlds**, Archive Moons       | *Weapon*: Baton or Makeshift Weapon<br>*Armor*: Uniform<br>*Tools*: Tablet, Scanner<br>*Money*: 5 Charged Solars + 35 Sparks | Mystic / Tech          |

> 💡 *Origins help guide new players by linking gear and power source to a meaningful backstory. Advanced players may mix-and-match narrative elements freely.*



## Origins Table

Origins define a character's background, story, and initial gear.  
They determine where your character comes from and how they learned their trade.  
Each Origin provides thematic starting items, access to specific skills, and hints at the character’s lifestyle.

| Origin        | Starting Gear                          | Common Power Source     | Skill Choices                          | Related Zones / Planets                   |
|---------------|----------------------------------------|--------------------------|-----------------------------------------|--------------------------------------------|
| **Acolyte**    | Robes, Relic, Dagger or Staff, stack of Solars | Mystic                  | Arcana, Willpower, Religion            | Zengard Monastery, Inner Rings, Arc Temples |
| **Artisan**    | Learning tablet, ID pass, travel bag  | Tech / Mystic           | Any 2 Academic or Social Skills        | Arc Universities, Distaheide Enclaves       |
| **Bounty Hunter**    | Learning tablet, ID pass, travel bag  | Tech / Mystic           | Any 2 Academic or Social Skills        | Arc Universities, Distaheide Enclaves       |
| **Criminal**   | Dagger or Hand Gun (integrated), fake ID, stack of Solars | Tech / Meta             | Deception, Stealth, Streetwise         | Underarc, Neon Belts, Distaheide Slums      |
| **Dreamborn**    | Learning tablet, ID pass, travel bag  | Tech / Mystic           | Any 2 Academic or Social Skills        | Arc Universities, Distaheide Enclaves       |
| **Engineer**   | Toolkit, repair drone, goggles        | Tech                    | Engineering, Mechanics, Computing      | Arc, Cradle Station, Halon Foundry          |
| **Entertainer**| Holo-performer, makeup, disguise kit  | Tech / Mystic           | Performance, Persuasion, Illusions     | Distaheide Stages, Casinos of Luna Prime    |
| **Farmer**     | Field clothes, water recycler, seeds  | Meta                    | Biology, Survival, Athletics           | Fringe Colonies, Oasis Worlds, Orthan Wilds |
| **Investigator**| Scanner, notepad, tracker lens       | Tech                    | Insight, Investigation, Computers      | Arc, Capital Spires, SigilNet Hubs          |
| **Merchant**   | Ledger, trade scanner, transport tag  | Tech                    | Persuasion, Streetwise, Accounting     | Trade Hubs, Lunar Bazaar, Core Belt Market  |
| **Miner**      | Mining laser, oxygen mask, light rig  | Tech                    | Athletics, Mechanics, Endurance        | Asteroid Belts, Ash'Tar Mines, Miris Shafts |
| **Noble**      | Fine clothes, influence badge, AI aide| Mystic / Tech           | Politics, Insight, Leadership          | Core Thrones, Arc Palaces, Inner Rings      |
| **Outlander**  | Cloak, hunting rifle, makeshift gear  | Meta / Mystic            | Survival, Stealth, Tracking            | Fringe Wilds, Untamed Moons, Dust Sector    |
| **Scientist**  | Lab tablet, analysis kit, stim injectors| Tech / Meta           | Science, Medicine, Computing           | Research Stations, Zenith Labs, Arc Vaults  |
| **Survivor**   | Scavenged armor, ration packs, blade  | Any                     | Survival, Endurance, Improvisation     | Wreck Zones, Derelicts, Waste Colonies      |
| **Scholar**    | Learning tablet, ID pass, travel bag  | Tech / Mystic           | Any 2 Academic or Social Skills        | Arc Universities, Distaheide Enclaves       |
| **Soldier**    | Sidearm, combat fatigues, ID chip     | Tech / Meta             | Tactics, Firearms, Athletics           | Training Domes, Military Arcs, Warzones     |
| **Student**    | Learning tablet, ID pass, travel bag  | Tech / Mystic           | Any 2 Academic or Social Skills        | Arc Universities, Distaheide Enclaves       |
---




## 🎭 Archetype – *Choose Your Role*

Archetypes are your character’s **narrative identity and combat role**. Each archetype gives you access to suggested abilities, Discipline preferences, and synergy guides. This is the first decision and helps structure the rest of your build.

| Archetype    | Description                                                                 | Damage Type   | Damage Source                  | Defense Type      |
|--------------|-----------------------------------------------------------------------------|---------------|--------------------------------|-------------------|
| **Assassin** | Stealth-focused damage dealer that uses traps for offence and defense.     | Frontloaded   | Weapons, Tech, Traps           | Dodge, Traps      |
| **Blaster**  | Specializes in high damage bursts, usually from range.                     | Frontloaded   | Powers, Ordinance              | Area Denial, Defensive Powers |
| **Controller** | Focuses on battlefield control, debuffs, and forcing enemy movement.     | Variable      | Powers, Traps                  | Crowd Control, Defensive Powers, Debuffs |
| **Expert**   | Utility role with emphasis on skills, tools, healing and items.            | Variable      | Weapons, Traps, Powers         | Healing, Shielding, Debuffs |
| **Guardian** | Tank role with excellent durability and support options.                   | Sustained     | Weapons, Powers, Environment   | Auras, Regen, High Stats, Debuffs|
| **Juggernaut** | Frontline damage dealer, trades mobility for endurance and force.        | Backloaded    | Unarmed, Heavy Weapons         | Rage, Regen, High Stats |
| **Marksman** | Ranged specialist with flexible damage.                                    | Sustained     | Weapons                        | Area Denial, Scouting, Avoidance, Light Plating           |
| **Shifter**  | Morphs between forms or roles mid-combat; excels at adaptation.            | Variable      | Powers, Unarmed                | Passive, Stat boosts    |
| **Slayer**   | Melee assassin, focused on critical strikes and exploiting weak spots.     | Sustained     | Weapons, Unarmed               | Dodge, Lifesteal, Rage  |

---

## 🔁 Optional Advanced Rules

Players may skip the structured steps and use full character building options:

- Manual stat assignment  
- Freeform Discipline selection  
- Custom Traits and Backgrounds  
- Modified Gear Packages  
---

# List of Backgrounds
Acolyte
Artisan
Bounty Hunter
Criminal
Dreamborn
Engineer
Entertainer
Farmer
Investigator
Merchant
Miner
Noble
Outlander
Scientist
Survivor
Scholar
Soldier
Student


# List of Species
Name - Description - Durability - Rest - Features - Skill
Elphs - Sleek, humanoid mix of several proto-elphar species - 5 durability - 1h short rest 8 h long rest - Nanite symbiosis, Shared Dreamer - Willpower
Orthans - Isolated lineage of Elphs - 5 durability - 1h short rest 8 h long rest - Nanite symbiosis, Shared Dreamer - Reflex
Sildorian - Tall, stoic giants with crystalline bones structure and crystalline exoskeleton - 7 durability - 5m short rest, 12h long rest - Crystalline - Fortitude
Ash Sarite - Variant of Sildorians from Amorthis system, more rocky than crystalline, lava based - 7 durability - 5m short rest, 12h long rest - Crystalline, Living Furnace - Fortitude


| ****          | Sleek, humanoid hybrids with symbiotic nanites.         | 5 / 4 / 3                         | 1h / 8h                   | Nanite symbiosis, Shared Dreamer, Adaptive (Pick any 2 genes)                  |
| **Orthans**        | Bio-adapted Elphs with tribal gear and organic patterns.| 5 / 5 / 3                         | 1h / 8h                   | Nanite symbiosis, Natural Weapons                                              |
| ****      | Tall, stoic giants with crystalline bone structure.     | 6 / 4 / 3                         | 5m / 12h                  | Shared Dreamer, Crystalline                                                    |
| **Ash Sarite**     | Charred, ash-covered titans with internal heat glow.    | 7 / 3 / 2                         | 5m / 12h                  | Crystalline, Living Furnace                                                    |
| **Miris Drone**    | Humanoid drones with visible external modular joints.   | 5 / 5 / 1                         | 1h / 4h                   |   |



# 🌌 Character Creation: Origins & Professions

Character creation in **SigilRPG** follows this order:

1. **Species** — Determines base Durability, rest time, defensive skill.
2. **Origin** — Defines early life and backstory. Grants one Skill, a Heirloom or Relic, and some narrative grounding.
3. **Profession** — Represents recent life or occupation. Grants weapon(s), armor, tools, Sparks, and two Skills (or 1 Discipline Point).
4. **Archetype** — Finalizes your combat style, role, and advancement.

---

## 🧬 Origins

| Origin       | Description                                                                 | Skill Options                    | Relic/Heirloom Example              | Associated Zones / Cultures         |
|--------------|-----------------------------------------------------------------------------|----------------------------------|-------------------------------------|-------------------------------------|
| **Urchin**   | Raised on the streets; quick, resourceful, and often underestimated         | Stealth, Insight, Athletics      | Stolen Charm, Memory Chip           | Megacities, orbital slums           |
| **Noble**    | Groomed in elite circles or houses with political, military, or cultural pull | Persuasion, History, Leadership | Crest Pendant, Duelist’s Badge      | Core planets, aristocratic houses   |
| **Dreamborn**| Emerged from the psychic realm of shared Elphar minds                       | Mysticism, Insight, Acrobatics   | Glass Mask, Soul-Shard              | Elphar bio-vaults, Distaheide       |
| **Outlander**| Grew up in isolated wilds or dangerous frontier environments                | Survival, Nature, Endurance      | Bone Charm, Weathered Journal       | Untamed planets, xenowilds          |
| **Scholar**  | Trained in ancient libraries, data vaults, or research labs                 | History, Technology, Investigation | Scholar's Lens, Quantum Tome      | Arc, library moons                  |
| **Cultist**  | Raised in esoteric orders, mystic faiths, or forbidden sects                | Mysticism, Deception, Religion   | Void Talisman, Gene-Splice Idol     | Void enclaves, sunken monasteries   |
| **Refugee**  | Displaced by war, collapse, or Zenith accidents                             | Endurance, Diplomacy, Perception | Broken Weapon, Passport Fragment    | Warzones, overflow colonies         |
| **Scavenger**| Lived among junkyards and derelict ships                                    | Mechanics, Sleight of Hand, Tinker | Junk Drone, Arcwelder Token       | Orbital debris fields, scraphabs    |
| **Lab-Grown**| Vat-born or printed; synthetic upbringing                                   | Medicine, Science, Engineering   | Clone Marker, Bio-Tag               | Arc-controlled sectors, black sites |
| **Pilgrim**  | Life spent in spiritual or long-haul migration                              | Religion, Navigation, Acrobatics | Pilgrimage Map, Solar Rosary        | Zealots' Reach, sleeper ships       |

---

## 🛠️ Professions

| Profession      | Description                                | Weapons                             | Tools / Extras                          | Plating / Clothing         | Sparks    | Skills / Special              |
|-----------------|--------------------------------------------|-------------------------------------|------------------------------------------|-----------------------------|-----------|-------------------------------|
| **Acolyte**      | Mystic servant or medtech assistant        | Staff / Dagger                      | Healing Kit, Scripture                   | Robes                      | 2,000     | Mysticism, Medicine           |
| **Artisan**      | Crafter of goods or implants               | Short Blade / Multitool Laser       | Toolkit, Mod Parts                       | Light Plating              | 3,500     | Mechanics, Crafting           |
| **Bounty Hunter**| Tracker, hunter, and freelance enforcer   | Rifle / Ripper                      | Spike Trap Kit                           | Medium Plating             | 6,000     | Perception, Survival          |
| **Criminal**     | Smuggler, thief, or rogue                  | Wire / Hand Gun                     | Lockpicks, Fake ID                       | General Clothing           | 4,500     | Deception, Stealth            |
| **Engineer**     | Maintainer of systems & hardware           | Emitter / Multitool Laser           | Engineering Kit, Circuit Splice Tools    | Light Plating              | 4,000     | Engineering, Technology       |
| **Entertainer**  | Performer, propagandist, VR illusionist    | Dagger / Short Blade                | Holo-Caster, Makeup Kit                  | Robes                      | 2,000     | Persuasion, Acrobatics        |
| **Farmer**       | Tends land, hydrofarms, or biome pods      | Spear / Staff                       | Agro-Sensor, Seeds                       | General Clothing           | 1,000     | Nature, Endurance             |
| **Investigator** | Analyst, detective, or truth-seeker       | Hand Gun / Wire                     | Scanning Device, Digital Journal         | Medium Plating             | 3,000     | Insight, Investigation        |
| **Merchant**     | Broker, middleman, or cargo runner         | Short Blade / Hand Gun              | Ledger Drone, Trade Goods                | General Clothing           | 10,000    | Persuasion, Negotiation       |
| **Miner**        | Void driller or asteroid extractor         | Ripper / Multitool Laser            | Rock Core Sampler                        | Heavy Plating              | 2,500     | Athletics, Mechanics          |
| **Scientist**    | Researcher of Zen, tech, or biology        | Staff / Emitter                     | Scanner, Sampling Kit                    | Robes                      | 5,000     | Science, Investigation        |
| **Soldier**      | Militarized combatant                     | Rifle / Long Blade                  | Tactical HUD, Grenade                    | Medium Plating             | 7,000     | Athletics, Accuracy           |
| **Survivor**     | Hardened by catastrophe or war             | Spear / Bow                         | Water Filter, Thermal Blanket            | Light Plating              | 1,500     | Survival, Willpower           |
| **Student**      | Freshly trained, barely field-tested       | Staff / Hand Gun                    | Notepad, Basic Scanner                   | Robes                      | 500       | Any 2 of your choice          |
| **Void Initiate**| ⚠️ Mystic or Zen acolyte                   | Staff / Emitter                     | Relic Item                               | Robes                      | 3,000     | **1 Discipline Point**        |

---

🧪 Let me know if you'd like to split gear per archetype too or define toolkits for professions.



### Progressing a character:
    Unlocking a tier of discipline costs 2 Discipline Points.  
    Upon unlocking you are granted innate features of this discipline. 
    Unlocking other features, such as auras, stances, or abilities, costs 1 Discipline point. 

    Stances:
    Whenever you start your turn, you may enter one of available stances.
    Only one stance can be active and this limit cannot be exceeded. 
    Stances end when you are incapacitated or unconscious.

    Auras: 
    Whenever you finish a short or a long rest, you can activate one of your auras. 
    They persist as long as you are conscious. 






# SigilRPG Character Creation

Welcome to **SigilRPG**, a science-fantasy tabletop RPG built on modular systems,
lore-infused rules, and a world based around Energy exchange among various factions.

SigilRPG is designed to scale in complexity as players become more experienced. 
Players can build a character using a structured set of guided choices:

1. **Species** — Determines genetic features, base Durability and rest time.
2. **Origin** — Defines early life and backstory. Grants one Skill, a Heirloom or Relic, and some narrative grounding.
3. **Profession** — Represents recent life or occupation. Grants weapon(s), armor, tools, Sparks, and two Skills (or 1 Discipline Point).
4. **Archetype** — Finalizes your combat style, role, and advancement.
5. **Basic Gear** — Selection of items available to all character

---






## Basic Gear

Gear available to all characters, in addition to what they gain from Origin/Profession choices.

    Weapon (Choose one): Bow, Hand Gun, Dagger, Staff 
    Tool: Handheld Terminal or Star Guide Charm
    Body: Basic clothes + Light Plating or Spacefairer Suit or Set of Expensive Clothes



Durability:
    Root of all defensive measurements, determined by Constitution modifier.
    Dictates Hit Points per Level, or Wounds per Tier.


Hit Points:
    Pool that measures how much damage character can take.
    This way of tracking damage, implies that 1 Point of damage has the same
    consequences, regardless of level of power of the creature receiving damage.

Wounds:
    Simplified damage tracking. Here, 1 Wound might represent various amounts of damage;
    it is much harder to inflict 1 wound to big monster, than it is to a small animal.

Ward:
    Temporary pool of Hit Points, that protects main HP. Essential to healing mechanics,
    as healing effects first go into Ward, and then slowly transfer to main Hit Points.
    Multiple sources of healing and shielding stack indefinitely, but are reset at long rest.

Avoidance Class:
    AC is contested with Accuracy of an Attack, to determine if it hits or not.

Damage Threshold:
    coupled to Hit Points tracking,
    this sets minimal amount of Damage that creature has to receive,
    in order to have it's HP reduced.

Accuracy:
    bonus to throws, that contest Avoidance Class (AC).
    Bonuses to accuracy specify to which attacks they apply (weapon attacks, spell (power) attacks, global bonus etc).

Focus (Action Points)
    Resource used to perform actions, resets on start of new Round.


Rounds and turn order:
    Each round represents 6 seconds of time. During it, character take their turns, of which order is
    dictated by Inititiative Count. Aside from their turn, each character has also one reaction.
    During a turn, each character has number of Action Points known as Focus, which they can use to perform variety of things,
    such as attacks or movement.

    Amount of Focus equals proficiency modifier, and can be increased or restored by certain effects.

Basic Skills:




Perks and Abilities:
    Ordered into 3 Disciplines, 


Genes and Traits:
    Biological Features and other abilities that do not fit other categories.

