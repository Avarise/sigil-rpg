## 🎲 Initiative & Rounds

**Initiative** determines the order in which characters act in combat.

- At the start of combat, each character makes an **Initiative Throw**.
- After order is established, all characters receive a **pool of actions** that **refreshes at the start of each new round**.

---

## 🔁 Combat Structure

### 🔄 Round
- Represents **6 seconds** of in-game time.
- During a round:
  - Every character takes a **Turn** (based on initiative order).
  - Characters may use **Reactions** and other **resource-based abilities**.

### ⏱️ Turn
- A character’s **individual segment** within the round.
- On their turn, characters may:
  - **Move**
  - **Attack**
  - **Use powers** (via Focus)
  - **Interact** or **Prepare** actions

### ⚡ Reaction
- **Triggered actions** taken **outside your turn**.
- Rules:
  - Each character has **1 free reaction** per round.
  - Additional reactions cost **1 Focus each**.
  - Maximum reactions per round = **Dexterity modifier (minimum 1)**.

---

## 🏃 Movement

### Movement Basics
- Each character has a **Movement Speed**, based on their **Movement Mode** (e.g. running, swimming).
- This speed defines the **meters per round** (6 seconds) a character can travel **without spending Focus**.

> 🧮 **Conversion**:  
> `Speed in meters/round × 0.6 = km/h`  
> _Example: 30 meters/round = 18 km/h_

### Multiple Modes
Some creatures have multiple movement modes. When switching mid-move, **remaining distance is proportional**.

> _Example: A character with 30m Run and 60m Fly uses 10m Run — they have 40m Fly remaining._

---

## 🛤️ Movement Modes

| Mode         | Description |
|--------------|-------------|
| **Running**  | Default ground movement for all creatures. |
| **Swimming** | Movement through liquid. If untrained: Half speed, DC 15 Athletics per 15 meters, or begin drowning. |
| **Flying**   | Full 3D movement. Requires wings, jetpacks, or other aerial tech. |
| **Burrowing**| Movement through ground (e.g., tunnels, soil). |
| **Piloting** | Movement using a **controlled vehicle**. |

---

## 🚶 Movement Actions

| 🧷 Name     | ⚡ Cost              | 📜 Description |
|------------|----------------------|----------------|
| **Jump**   | 0 Focus               | Jump distance = `Strength` (Standing) or `2 × Strength` (Running) — limited by move speed |
| **Dash**   | 1 Focus               | Move additional distance equal to your base speed; usable **once per turn** |
| **Sprint** | All Focus             | Run in a **straight line**, gaining bonus distance; enemies gain **advantage** on attacks |
|            |                      | - **Running**: `3×Speed + 10m` per Focus<br> - **Swimming**: `3×Speed + 5m` per Focus<br> - **Flying**: `5×Speed + 15m` per Focus |
| **Sneak**  | 1 Focus               | Move at half speed and attempt a **Stealth Check**. Fails if visible or detected. Cloaking may override |
| **Crouch** | 0 Focus               | Halves speed to enter **prone** condition. Not usable with **Flying** or **Skimming** |

---

## 🛡️ Defensive Actions

| 🧷 Name     | ⚡ Cost                     | 📜 Description |
|------------|-----------------------------|----------------|
| **Brace**  | All remaining Focus (min 1)  | Gain **+AC** and **+Damage Threshold** equal to Focus spent |
| **Breakout** | All remaining Focus (min 1) | Attempt to end status effects — requires **Fortitude Check**:<br>`DC = 10 + 5 per status effect`<br>|
| **Disengage** | 1 Focus           | Avoid **Opportunity Attacks** for the rest of the turn |
| **Dodge**  | All remaining Focus (min 1)  | Gain bonus to **+AC** and **Dexterity Skill Throws** equal to Focus spent |


## 🗡️ Attack Actions

Attacks in **SigilRPG** require **⚡ Focus** to perform and are characterized by:

- 🎯 **Accuracy** — chance to hit
- 💥 **Damage** — amount of harm dealt
- ☠️ **Lethality** — critical hit threat range

By default, a natural **20** on an Accuracy Throw is a critical hit.  
Each point of **Lethality** extends this range by 1 (e.g. Lethality +2 allows crits on 20, 19, and 18).

---

## ⚔️ Basic Attacks  
*Available to all characters.*

| 🧷 Name             | ⚡ Cost   | 🎯 Acc. | 💥 Dmg  | ☠️ Lethality | 📝 Notes |
|--------------------|----------|--------|--------|--------------|---------|
| **Normal Attack**  | 1 Focus  | +0     | +0     | +0           | Basic single-target attack |
| **Expose Attack**  | 1 Focus  | +0     | –      | –            | Target becomes **Exposed**: all attacks vs it have **advantage** until end of its next turn |
| **Swipe Attack**   | 1 Focus  | –1 per target | No attribute bonus | – | Hits **multiple targets** in range. On-hit effects deal **half damage** |
| **Opportunity Attack** | 1 Reaction | +0 | +0 | +0 | Triggered when target leaves melee range |

---

## 💪 Advanced Attacks  
*Unlocked through the **Prowess Discipline** tree.*

| 🧷 Name                | ⚡ Cost | 🎯 Acc.   | 💥 Dmg         | ☠️ Lethality | 📝 Notes |
|-----------------------|--------|----------|----------------|--------------|----------|
| **Heavy Attack I**    | 2 Focus | +0       | +2, +1 die     | +0           | Melee only. Opponent's **Counter**/**Quick Attacks** gain **advantage** |
| **Heavy Attack II**   | 2 Focus | +0       | +4, +2 dice    | +0           | As above, stronger version |
| **Precision Attack I**| 2 Focus | +2 / Adv | +0             | +1           | Cannot be **counterattacked** |
| **Precision Attack II**| 2 Focus | +4 / Adv | +0            | +2           | Stronger variant |
| **Quick Attack I**    | 1 Reaction | +0   | –1 weapon die tier   | +0           | Used **before** a melee attacker hits you. Strikes first |
| **Quick Attack II**   | 1 Reaction | +0   | no penalty   | +0           | Stronger version |
| **Counter Attack I**  | 1 Reaction | +0   | Diff. between AC and enemy accuracy | +0 | Triggered on a **missed melee attack** |
| **Counter Attack II** | 1 Reaction | +0   | Same as above | +1           | Stronger version |

---

🧩 *See Prowess discipline tree for unlocking advanced techniques.*

## ❤️ Hit Points & Regeneration

Hitpoint Formula: Durability x Level

Hit points dictate damage required to kill or destroy character, item or structure.
When character reaches 0 HP, it goes unconscious, and regains consciousness upon regenerating 20% of max HP.

Temporary Hit points from multiple sources stack. They cover main pool of Hit Points.
At the start of each round, damaged creatures can convert Temporary Hit Points into regular hit points.

> Temp HP into HP conversion limit: 10% + 5% per constitution of max Hit Points.
 

## 🛡️ Damage Prevention

| Mechanic           | Description                                                                 |
|--------------------|-----------------------------------------------------------------------------|
| Armor Class (AC)   | Avoids damage if Accuracy Check < AC.                                       |
| Damage Threshold   | Ignores damage below threshold.                                             |
| Resistance         | Halves damage from a specific type. Grants Advantage vs related effects.    |
| Immunity           | Negates all damage/status from a type. Auto-success vs related checks.      |
| Damage Reduction   | Subtracts flat value from incoming damage.                                  |
| Temporary Hit Points | Shields Hit Points from damage.                                           |


## ☣️ Status Effects



### Damaging Ailments

    Bleeding: (Stacking)
        Target takes 1d4 internal damage at the beginning of the round,
        for each bleeding wound. When target heals or regenerates during a round,
        one wound closes.

    Burning: 
        Target takes fire damage at the beginning of the round/
        Damage is based on target's size: 
        Small 1d4 / Medium 1d6 / Large 1d8 / Huge 1d10 / Gargantuan 1d12

    Poisoned:
        While poisoned, critical failure happens on 1 and 2 on d20 throws.
        Damage from poisons adds up over time, instead of dealing damage immediately.
        When target suffers any damage that would reduce thier current HP below the
        accumulated poison damage, the target takes all stacked the damage.
        This effect cannot reduce HP of the target below 1.
        Different sources of poisons may have extra effects, for example,
        neurotoxin might incapacitate, and different poison might petrify.

### Status Effects

    Disrupted:
        Attackers gain advantage on accuracy throws.
        Whenever target becomes disrupted, enemies in range can perform opportunity attack.

    Prone:
        Melee accuracy throws against prone target gain advantage, ranged throws gain disadvantage. 

    Stunned:
        Target is disrupted, cannot move, use reactions, and can use their turn only to Breakout.

    Restrained:
        Target is disrupted, and has speed of 0.
        Target automatically fails Reflex Checks. 
        
    Frightened:
        Target has disadvantage on skill checks and accuracy checks while the source of its fear is within line of sight. 
        Target can’t willingly move closer to the source of its fear.
    
    Grappled:
        Target is held down by an opponent, and both have their movement locked.
        If one of the creatures want to move, it has to win Athletics contest again the other.
        Displacements end grappling.

    Incapacitated: 
        Target cannot use focus, reactions and turns. 

    Incorporeal: 
        Target becomes immune to all physical damage, can pass through objects, 
        and has flying speed equal to their normal walking speed.
        Incorporeal targets are always vulnerable to Force damage. 

    Petrified: 
        Target is turned into stone-like matter.
        It becomes unconscious vulnerable to chemical damage,
        immune to biological damage, and resistant to all other forms of damage. 
        Poison or disease affecting target is not neutralized.

    Shocked: 
        Target cannot use reactions. 

    Surprised: 
        Target cannot act on their turn while surprised.
        Attacks against surprised targets gain advantage.
        Condition ends at the end of the first round of the encounter. 

    Unconscious:
        When reaching 0 HP with non-zero regeneration pool, target becomes incapacitated.
        It cannot communicate, and is unaware of its surroundings.
        The target drops whatever it is holding and falls prone.
        The target automatically fails Reflex Checks.
        Targets regain consciousness after reachng 10% or more of HP. 

    Overwhelmed:
        Target is exposed and slowed.

    Sense Impaired:
        Automatically fail all checks using the impaired sense.
        Hearing / Vision

    Slowed/Staggered:
        Lose half of the movement speed.
        Reflex Checks gain disadvantage. 

    Weakness (Stacking): 
        Suffer -1 penalty to accuracy, weapon damage and all skill throws per stack.

### Breakout Action
    Basic Action available to all characters
    Cost: All remaining Focus (Minimum 1)
    Attempt to end status effects — requires Fortitude Check:
    DC = 10 + 5 per status effect
    


# 📕 Damage Types, Prevention, and Status Effects




## ❤️ Hit Points & Regeneration

| Mechanic            | Description                                                                                             |
|---------------------|---------------------------------------------------------------------------------------------------------|
| HP                  | When reduced to 0: go unconscious. If damage exceeds max HP below 0, death is instant.                  |
| Short Rest          | Recovers 25% + 5% × CON modifier of Max HP.                                                              |
| Long Rest           | Fully restores HP and resets regeneration pool.                                                          |
| Regeneration Pool   | Accumulates healing effects. Restored at start of turn (max 10% + 5% × CON mod of max HP per turn).      |

