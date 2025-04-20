### Vehicle Classification

    Vehicle Sizes: 
    Based on size of a vehicle, weapons it carry gain a damage multiplier. 
    1. Small   - up to 150 meters, 2x dice multiplier
        Jet fighters, threaded tanks, ground artillery,
        space corvettes and bombers

    2. Medium  - up to 750 meters, 4x dice multiplier
        Freigthers, Frigates, Destroyers

    3. Large   - up to 3750 meters, 8x dice multiplier
        Carriers, Cruisers

    4. Capital - above 3750 meters, 16x dice multiplier
        Dreadnoughts, Flagships, Massive space stations


    Spinal mount weapons count as one size bigger, up to 32x multiplier

### Spaceship Actions and Reactor

    Reactor Unit:
    Every working ship requires source of instantly available energy.
    This is achieved via reactor with an attached capacitor to store and release
    generated energy quickly, on demand. 

    Spaceship rounds happen every 5 character rounds, thus
    energy of a reactor is expressed in arbitrary amount available every 30 seconds.
    Energy per 30 seconds = 6 + (Ship Size)^2 - Reactor Class 
    
    Reactor Classes (quality): 
    0: Ideal energy source, based on given technology 
    1: Next generation prototype, highly upgraded unit 
    2: Overdriven or slightly upgraded basic variant 
    3: Stable basic unit or miniaturized high efficiency variant 
    4: Artificially limited / Older unit with higher safety limit 
    5: Scrapped version, or early prototype 

    Worst reactor capacity:     6 + 1² - 5 = 2 
    Best reactor capacity:      6 + 4² - 0 = 22 
 
    Reactor Energy Capacity: 

### Weapons:
    Machine Guns:
    Small sized guns that require a dedicated gunner. They use negligible amounts of energy, by virtue of using gunpowder filled ammo. 
    Damage: 3d6 (not increased by ship's size dice multiplier) 

    Mass Drivers:  
    One of the oldest, and most reliable weapon types, that works by accelerating chunks of metal to high speed via electromagnetic forces. 
    Mass drivers in theory offer unlimited range, however accuracy at great distances is poor. 
    Ignores energy shields on critical strike. 
    Base damage: 4d6 (avg 14.0) 
    Energy usage: 2/3/4/5 
    
    Lasers: 
    Specialized anti-plating weapon. Lasers deal constant damage with almost 
    immaculate accuracy, however, their damage is reduced heavily with distance. 
    Base Damage: 1d12 (avg 6.5) of Radiant damage 
    Deal 50% more damage against hull. 
    Deal 100% more damage against plating. 
    Deal 200% more against reactive plating. 
    Deal 50% less damage against shields 
    Energy usage: 2/4/6/8     

    Nuclear Pulse Laser: 
    This kind of laser sources majority of energy from contained nuclear explosion. 
    Due to complexity they require spinal mount of at least medium size. 
    Ammo: Fuel Rod x1 (5 Shots) 
    Cooldown: 2d6 rounds 
    Base Damage: 4d20 (avg 42.0) 
    Reactor Energy usage: 6 at all size categories 

    Particle Lances: 
    Hybrid between particle accelerator and specialized form mass driver, 
    this ordinance strikes enemies with dust of mixture of heavy metal salts, 
    accelerated to near relativistic speeds. 
    Strikes at perfect angle cause small localized fusion events, 
    dealing massive fire damage. 
    Base Damage: 2d10 (avg 11.0) Piercing damage 
    +1 bonus to lethality. Critical strikes, deal 50% of the damage dealt as extra fire damage. 
    Energy usage: 1/2/3/4 
    
    
    Plasma Drivers: 
    Evolution of mass drivers, that uses energized gas instead of metal slugs. 
    Their range is heavily limited due to bolt instability.  

    
    Base Damage: 3d6 (avg 10.5) energy damage 
    (split equally into lightning and fire), 
    50% more damage against armor plating and hull 
    Energy usage: 2/3/4/5 
    

    Arc Emitters: 
    Low range weapon, that strikes target using electric tendrils. 
    They are super effective against energy shields. 
    
    Base Damage: 2d6 (avg 7.0) lightning. 
    Deals triple damage against shields. 
    Energy usage: 2/4/6/8 
    
    
    Missile Launchers: 
    Each launcher may lock onto a singular target. Doing so reserves 1 Energy. 
    Properties of attack depend mostly on the used Missile.

### Signature Radius
    
    Ease of accurate targeting depends on spaceship's signature radius.
    The bigger the area visible from a distance, the easier it is to hit.
    Exact RSR can be calculated based on ship's size with following formula:
        42 - 10 * log10(size_meters)


    Durability: Hull 
    Primary pool of Hit Points for a vessel. 
    Damage to hull may result in loss of onboard systems, such as weapons, engines, storage bays etc. 

    Durability: Plating 
    External hull attachments, that protect it from damage. It has own HP pool, independent from hull.
    Each plating has additional damage threshold rating, which dictates minimal damage needed to affect the HP of plating. 

    Durability: Energy Shielding 
    Cloud of charged particles around a ship. 
    Buzzing with oscillating electrons, these clouds dissipate energy weapons really well,
    but may be punched through with kinetic weapons.
    
### Plating Types
    Hardened Steel plating: 
        Most basic type of spaceship plating.
        Easy to repair using basic technology and tools. 
        Repair: 250 Sparks per HP 
    
        Hit Point Formula:          100 + 120 x Size^2 
        Hit Points:                 220 / 580 / 1180 / 2020  
            
        Damage Threshold Formula:   10 + 6 x Size 
        Damage Threshold:           16 / 22 / 28 / 34 


    Tungsten Alloy plating: 
        Spaceship plating that uses densest known alloys to achieve high durability at cost of great weight increase. 

        Hit Points:                 240 / 660 / 1360 / 2340   
        Damage threshold:           15 / 20 / 25 / 30   

        Hit Point formula:          (100 + 140 * size ^ 2)
        Damage threshold formula:   (10 + size * 5)

        Repair: 
        450 Sparks per HP 

    Reactive plating: 
        More intricate plating that consists of many layers, of which some are explosive. 
        This greatly increases damage absorption potential, however almost any damage can trigger plating.
        Those features make this armor very expensive to repair.
        Repair:                     700 Sparks per HP 

        Hit Points:                 260 / 740 / 1540 / 2660
        Damage Threshold:           8 / 11 / 14 / 17

        Hit Point formula:          (100 + 160 * size ^ 2) 
        Damage Threshold formula:   5 + 3 x Size 


    

    Superconductive plating: 
        Weaved in strands of superconductive material keep energy shields attracted to ships outline, instead of a bubble shape.
        This boost effectiveness of shields and negates RSR penalty.
        Repair: 1000 Sparks per HP 

        Hit Points:                 200 / 500 / 1000 / 1700  
        Damage Threshold:           10 / 15 / 20 / 25 

        Hit Point formula:          100 + 100 * size ^ 2
        Damage Threshold formula:   5 + 5 per size 
    
        Shielding HP bonus:         10% 

    Bio-plating: 
        Similar to natural exoskeleton. Capable of regrowing and regenerating. 

        Hit Points:                 300 / 600 / 1100 / 1800 
        Damage threshold:           10 / 15 / 20 / 25 

        Hit Point formula:          50 + 150 x Size^2 
        Damage Threshold formula:   10 + 5 per size 
    
### Energy Shield Types
    Low Frequency Shield: 
        Cloud of energetic particles, that pulses periodically.
        Each pulse blends these particles, filling gaps in zones that absorbed a hit.

        Durability: 50 + 110 * size ^ 2 

        160 / 490 / 1040 / 1810 

    

    High Frequency Shield: 
        Particles of this shielding type constantly travel around the hull, wih 
        Durability: 50 + 90 * size ^ 2 
        140 / 410 / 860 / 1490 
        Using 1 unit of energy recharges 2 ^ size HP. 
        2 / 4 / 8 / 16 



# 🚀 Vehicle Defenses

## 📏 Size Classes

| Class     | Size Index |
|-----------|------------|
| Small     | 1          |
| Medium    | 2          |
| Large     | 3          |
| Capital   | 4          |

---

## 🧱 Plating Types

Each vehicle can be equipped with **one plating system**, which provides **Hit Points (HP)** and **Damage Threshold (DT)**.  
Damage below the DT is ignored. Damage above it is subtracted from HP normally.

> 💡 **HP Formula**: `100 + (Base Multiplier × Size²)`  
> 💡 **DT Formula**: `Base DT + (Modifier × Size)`  

---

### 🔩 Hardened Steel

> "Basic, reliable, and easy to fix."

| Stat                | Formula                     | Values (S/M/L/C)         |
|---------------------|-----------------------------|---------------------------|
| HP                  | 100 + 120 × Size²           | 220 / 580 / 1180 / 2020   |
| Damage Threshold    | 10 + 6 × Size               | 16 / 22 / 28 / 34         |
| Repair Cost         | 250 Sparks per HP           |                           |

---

### 🪨 Tungsten Alloy

> "Dense and durable, at the cost of immense weight."

| Stat                | Formula                     | Values (S/M/L/C)         |
|---------------------|-----------------------------|---------------------------|
| HP                  | 100 + 140 × Size²           | 240 / 660 / 1360 / 2340   |
| Damage Threshold    | 10 + 5 × Size               | 15 / 20 / 25 / 30         |
| Repair Cost         | 450 Sparks per HP           |                           |

---

### 💣 Reactive Plating

> "Explosive layers that dissipate force — costly but effective."

| Stat                | Formula                     | Values (S/M/L/C)         |
|---------------------|-----------------------------|---------------------------|
| HP                  | 100 + 160 × Size²           | 260 / 740 / 1540 / 2660   |
| Damage Threshold    | 5 + 3 × Size                | 8 / 11 / 14 / 17          |
| Repair Cost         | 700 Sparks per HP           |                           |

---

### ⚡ Superconductive Plating

> "Designed to anchor shields along the hull instead of forming a bubble."

| Stat                | Formula                     | Values (S/M/L/C)         |
|---------------------|-----------------------------|---------------------------|
| HP                  | 100 + 100 × Size²           | 200 / 500 / 1000 / 1700   |
| Damage Threshold    | 5 + 5 × Size                | 10 / 15 / 20 / 25         |
| Repair Cost         | 1000 Sparks per HP          |                           |
| Special             | +10% Shield HP              | No penalty for RSR Shields |

---

### 🧬 Bio-Plating

> "Grown like bone — it lives, it heals."

| Stat                | Formula                     | Values (S/M/L/C)         |
|---------------------|-----------------------------|---------------------------|
| HP                  | 100 + 110 × Size²           | 210 / 540 / 1180 / 1860   |
| Damage Threshold    | 10 + 4 × Size               | 14 / 18 / 22 / 26         |
| Repair Cost         | Regrows slowly for free, or 300 Sparks per HP via biotech |
| Special             | Regenerates 5% HP per long rest, if plating is not destroyed |

---


## 🛡️ Shielding Systems

Shields protect the ship before hull plating is affected. They recharge between turns or rounds, depending on frequency type.

| Frequency Type     | Formula (HP)     | Small (1) | Medium (2) | Large (3) | Capital (4) | Notes                              |
|--------------------|------------------|-----------|-------------|------------|--------------|-------------------------------------|
| **Low Frequency**  | 80 × Size²       | 80        | 320         | 720        | 1280         | Slow recharge from engine heat 🔥    |
| **High Frequency** | 60 × Size²       | 60        | 240         | 540        | 960          | Fast recharge from electric systems ⚡ |
| Type              | Recharge Method         | Notes                                              |

| **High|-------------------|-------------------------|----------------------------------------------------|
| **Low Frequency** | Heat from engines       | ⚠️ Slower recharge, but bulkier and more robust    | Frequency**| Electrical systems       | ⚡ Fast recharge; can be modulated on demand       |

---
## 🛡️ Shielding Types

Shields absorb damage before it reaches plating. Shield HP is based on ship size and shield type, and is capped at **~80% of average plating HP per size**. Shields fully regenerate between encounters or recharge gradually during combat depending on frequency type.

> 💡 Shield HP Formula:  
> `Shield HP = Base × Size²` (Base varies per frequency type)

### 📊 Shield Capacity by Type & Size


> 🔧 RSR = "Rapid Spatial Rebound" shielding, typically used in dogfighting

---

🧮 **Reference**:  
Average plating HP per size ≈  
Small: 242, Medium: 604, Large: 1264, Capital: 2116 → 80% = ~194 / 483 / 1011 / 1693  
Low Freq shields fall just below that cap to allow energy margin.

```






Ship defenses provide pool of additional hit points, before ship's hull is damaged. Plating, provides bigger pool, that might be repaired for cheaper than hull. Shielding is a magnetic field bubble that keeps energized particles around the hull. This provides a weaker pool of HP, but one that can be regenerated easily. 

 

Hardened Steel plating: 

Most basic type of spaceship plating. Easy to repair using basic technology and tools. 

Hit Points: 
100 + 120 x Size^2 

Damage Threshold: 
10 + 6 x Size 


Repair: 

250 Sparks per HP 

  

Tungsten Alloy plating: 

Spaceship plating that uses densest known alloys to achieve high durability at cost of great weight increase. 

Hit Points: 

240 / 660 / 1360 / 2340 (100 + 140 * size ^ 2) 

Damage threshold: 

15 / 20 / 25 / 30 (10 + size * 5) 

Repair: 

450 Sparks per HP 

     

Reactive plating: 

More intricate plating that consists of many layers, of which some are explosive. 

This greatly increases damage absorption potential, however almost any damage can trigger plating. Those features make this armor very expensive to repair. 

Hit Points: 

260 / 740 / 1540 / 2660 (100 + 160 * size ^ 2) 

Damage Threshold: 

8 / 11 / 14 / 17 (5 + 3 * size) 


Repair: 

700 Sparks per HP 

  

Superconductive plating: 

Weaved in strands of superconductive material keep energy shields attracted to ships outline, instead of a bubble shape. 

Hit Points: 

200 / 500 / 1000 / 1700  [ 100 + 100 * size ^ 2 ] 

Damage Threshold: 

10 / 15 / 20 / 25 [ 5 + 5 per size ] 

5 + 5 x Size 

Shielding Bonuses: 

HP:+10% 

RSR Shield penalty removed 

Repair: 1000 Sparks per HP 

  

Bio-plating: 

Similar to natural exoskeleton. Capable of regrowing and regenerating. 

*Chatgpt command: fill missing data*







# 🛡️ Vehicle Defenses

Spaceships in **SigilRPG** use two main forms of defense:

- **Plating** — acts as armor with **Hit Points (HP)** and **Damage Threshold**
- **Shielding** — a regenerable barrier that absorbs incoming damage before HP is affected

---

## ⚙️ Size Classes

| Size     | Index | Example Types          |
|----------|-------|------------------------|
| Small    | 1     | Fighters, Scouts       |
| Medium   | 2     | Freighters, Corvettes  |
| Large    | 3     | Frigates, Cruisers     |
| Capital  | 4     | Battleships, Carriers  |

---

## 🔰 Shielding Types

| Type               | Recharge Source | Traits                                                                 |
|--------------------|------------------|------------------------------------------------------------------------|
| **High Frequency** | Electric power   | 🟢 Fast recharge, 🔴 Lightweight, 🟠 Vulnerable to EMP                   |
| **Low Frequency**  | Engine heat      | 🟢 More HP, 🔴 Slower recharge, 🟠 More stable under signal interference |

---

## 🧱 Armor Plating Types

All plating types provide HP and a **Damage Threshold** — minimum damage required to reduce HP.

| Type                   | HP Formula                        | Damage Threshold Formula       | Repair Cost      | Traits                                                   |
|------------------------|-----------------------------------|-------------------------------|------------------|-----------------------------------------------------------|
| **Hardened Steel**     | `100 + 120 × Size²`               | `10 + 6 × Size`               | 250 Sparks/HP     | Basic, easy to repair                                     |
| **Tungsten Alloy**     | `100 + 140 × Size²`               | `10 + 5 × Size`               | 450 Sparks/HP     | Dense, heavy, very durable                                |
| **Reactive**           | `100 + 160 × Size²`               | `5 + 3 × Size`                | 700 Sparks/HP     | Layered, explosive reactive armor                         |
| **Superconductive**    | `100 + 100 × Size²`               | `5 + 5 × Size`                | 1000 Sparks/HP    | Shield-enhancing, no RSR penalty                         |
| **Bio-plating**        | `100 + 130 × Size²` (regenerative)| `8 + 4 × Size`                | 600 Sparks/HP     | Regenerates slowly over time; organic, grown not built    |

---

## 🧮 Reference Table

| Type               | Small (1) | Medium (2) | Large (3) | Capital (4) | Damage Threshold (S/M/L/C) |
|--------------------|-----------|------------|-----------|-------------|-----------------------------|
| Hardened Steel     | 220       | 580        | 1180      | 2020        | 16 / 22 / 28 / 34           |
| Tungsten Alloy     | 240       | 660        | 1360      | 2340        | 15 / 20 / 25 / 30           |
| Reactive           | 260       | 740        | 1540      | 2660        | 8 / 11 / 14 / 17            |
| Superconductive    | 200       | 500        | 1000      | 1700        | 10 / 15 / 20 / 25           |
| Bio-plating        | 230       | 620        | 1270      | 2180        | 12 / 16 / 20 / 24           |

> 🩹 **Repair Mechanics**:  
> Each HP of damage requires Sparks based on plating type.  
> Some plating (e.g. Bio) may **regenerate 1 HP per round** when out of combat.

---

## 🎯 RSR — Reverse Signature Radius

- Equivalent of **Armor Class** for ships.
- Most shields form a **visible energy bubble**, making targeting easier.
- **Superconductive plating** keeps shield tight to hull shape → **No RSR penalty**.
- Smaller ships benefit from **higher RSR**, making them harder to hit.

---

## ⚡ Shield + Plating Interaction

1. **Shields** absorb damage first.
2. When shields drop, **Damage Threshold** on plating applies.
3. If attack deals **less than threshold**, no HP lost.
4. Once HP reaches 0 → ship becomes **disabled or destroyed**, based on situation.

---

## 🔧 Future Expansions

- Shield HP by size class
- Heat vs Energy resistance modules
- Synergistic interactions with **Zen-tech** enhancements

