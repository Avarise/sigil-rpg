## Initiative & Rounds

**Initiative** determines the order in which characters act in combat.

- At the start of combat, each character makes an **Initiative Throw**.
- After order is established, all characters receive a **pool of actions** that **refreshes at the start of each new round**.

---

## Combat Structure

### Round
- Represents **6 seconds** of in-game time.
- During a round:
  - Every character takes a **Turn** (based on initiative order).
  - Characters may use **Reactions**..

### Turn
- A character’s **individual segment** within the round.
- On their turn, characters may consume focus to take Actions, such as
  - **Move**
  - **Attack**
  - **Use powers**
  - **Interact**
  - **Prepare** actions to be triggered with Reaction, later in the round.

### Reaction
- **Triggered actions** taken **outside your turn**.
- Rules:
  - Each character has **1 free reaction** per round.
  - Additional reactions cost **1 Focus each**.
  - Maximum reactions per round = **Dexterity modifier (minimum 1)**.

---

## Movement

### Movement Basics
- Each character has a **Movement Speed**, based on their **Movement Mode** (e.g. running, swimming).
- This speed defines the distance in **meters**, a character can travel **using 1 Focus**.

### Multiple Modes
- Some creatures have multiple movement modes. Each Focus point can only be used for singular movement mode
- To run 10 meters, and then fly 15 meters, character has to use 2 Focus.

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




    


# 📕 Damage Types, Prevention, and Status Effects




## ❤️ Hit Points & Regeneration

| Mechanic            | Description                                                                                             |
|---------------------|---------------------------------------------------------------------------------------------------------|
| HP                  | When reduced to 0: go unconscious. If damage exceeds max HP below 0, death is instant.                  |
| Short Rest          | Recovers 25% + 5% × CON modifier of Max HP.                                                              |
| Long Rest           | Fully restores HP and resets regeneration pool.                                                          |
| Regeneration Pool   | Accumulates healing effects. Restored at start of turn (max 10% + 5% × CON mod of max HP per turn).      |

