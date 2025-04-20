## 🗡️ MELEE WEAPONS

Bonus to **Accuracy** of melee weapons is equal to **Strength** modifier + **Proficiency Bonus** if proficient with given weapon.

| Weapon         | Price (Sparks) | Damage              | Accuracy Mod | Traits                                           |
|----------------|----------------|---------------------|--------------|--------------------------------------------------|
| **Spear**      | 50        | `1d8 + STR/DEX`         | STR or DEX   | Brace: AoO against enemies entering melee.       |
| **Staff**      | 250       | `1d6 / 1d8 + STR/DEX`   | STR or DEX   | Versatile. Bash: Expose knockdown.                    |
| **Wire**       | 500       | `1d4 + STR/DEX`         | STR or DEX   | 10m range. Can pull/move objects via terrain.    |
| **Dagger**     | 500       | `1d4 + STR/DEX`         | STR or DEX   | Ignores plating damage threshold.                |
| **Short Blade**| 2,500     | `1d6 + STR/DEX`         | STR or DEX   | +1 AC if held in offhand.                        |
| **Shield**     | 2,500     | `1d4 + STR/DEX`         | STR or DEX   | +2 AC if offhand. Thrown (30m). Bash: Prone on expose.|
| **Long Blade** | 15,000    | `1d8 / 1d10 + STR`      | STR          | Versatile: 1d10 if wielded two-handed.           |
| **Ripper**     | 25,000    | `1d12 + STR`            | STR          | STR 15+ (2h) or STR 19+ (1h) required.            |

### Weapon Properties
Weapons with *Light* property can use **Dexterity** instead of **Strength**.

---

## 🎯 RANGED WEAPONS

Bonus to **Accuracy** of ranged weapons is equal to **Dexterity** modifier + **Proficiency Bonus** if proficient with given weapon.
Ranged weapons have defined **effective** and **maximum** range brackets, with disadvantage on Accuracy Throws past the first.

| Weapon       | Price (Sparks) | Damage                    | Range (Eff./Max)   | Traits                                                                 |
|--------------|----------------|----------------------------|--------------------|------------------------------------------------------------------------|
| **Bow**       | 5,000          | `1d8 + STR` (Piercing)     | 60m / 120m         | Rare. Requires high skill to match firearms. Uses STR for damage.     |
| **Hand Gun**  | 5,000          | `1d6 + DEX` (Piercing)     | 60m / 120m         | 10 rounds/mag. Reload costs 1 Focus. Quick and concealable.           |
| **Rifle**     | 25,000         | `1d10 + DEX`               | 120m / 240m *(Sniper: 240m / 480m)* | 6 rounds. Can swap to Sniper (double range, no sweep). Burst = 1 shot. |
| **Emiter**    | 75,000         | `2d6 + DEX` (Energy)       | 30m (hard limit)   | Short-range energy weapon. Damage based on energy cartridge quality.  |
| **Multitool Laser**       | 25,000          | `1d4 + dex` (Radiant)     | 30m / 150m         | Rare. Requires high skill to match firearms. Uses STR for damage.     |

---

### 🔋 AMMO & RELOADING

- **Hand Guns**: 10 shells per magazine, **1 Focus** to reload.
- **Rifles**: 6 shots total per magazine; **burst** counts as one attack regardless of number of targets hit.
- **Emiters**: Use **cartridges**, not traditional ammo. Quality of cartridge may boost damage or add status effects.
- **Bows**: No reload cost, but requires free hand for arrows unless using integrated mod.
- **Multitool Laser**: Has to cooldown for one whole round after dealing 10 - 40 damage (Based on device tier)

---

### 🧾 NOTES

- *Sniper Mode* disables **sweep** or **multi-target** abilities, but allows attacks from afar with greater precision.
- All ranged attacks beyond effective range suffer **disadvantage** unless target is stationary or otherwise exposed.
- **Energy weapons** (like Emiter) may be affected by environmental conditions (e.g., water, magnetic interference).

---

## 🧨 EXPLOSIVES, TRAPS & EXOTICS

| Weapon / Device        | Price (Sparks)     | Effect                                                                                     | Save / Accuracy                        | Damage / Outcome                                      |
|------------------------|--------------------|---------------------------------------------------------------------------------------------|----------------------------------------|--------------------------------------------------------|
| **Kinetic Orb**         | 25,000,000         | Self-propelled drone; acts in a 30m radius; telekinetic/remote interface.                  | `INT + proficiency`                    | `1d6 + INT` (Bludgeoning); can apply knockback         |
| **Ordinance Platform**  | 500,000            | Mount 3 weapons or utilities on armor (medium/heavy only). Uses **Vehicle** skill.         | N/A                                    | Mounted weapons deal **+1 size die** damage            |
| **Beartrap**            | 25                 | Pressure trap. Causes bleeding. One-time use.                                               | DC 10 Reflex                           | `3d4` Piercing; **always causes bleeding**             |
| **Stun Cloud Trap**     | 2,500              | Deploys poison gas. 10m radius cloud. One-time use.                                         | DC 14 Constitution                     | `4d6` Poison; may **stagger** or **weaken** target     |
| **Cryo Grenade**        | 1,500              | Explodes in cold mist. Reduces movement. 5m radius.                                         | DC 13 Constitution                     | `3d6` Cold; targets are **slowed** for 1 turn          |
| **Incendiary Grenade**  | 1,750              | Ignites area. 5m radius. Flammable objects catch fire.                                      | DC 14 Reflex                           | `3d8` Fire; target may **burn** for 1d4 turns          |
| **EMP Mine**            | 3,000              | Explodes on contact. Disables machines for 1 turn.                                          | DC 12 Intellect (for AI), Reflex (for drones) | `2d10` Lightning; disables unshielded tech             |
| **Shrapnel Mine**       | 2,000              | Wide-area blast; cone effect (15m forward).                                                 | DC 13 Reflex                           | `4d6` Piercing; may cause **bleeding**                 |
| **Zen Disruptor Charge**| 100,000            | Rare anti-Zen device. Collapses local Zen field (10m).                                     | DC 15 Willpower                        | `2d12` Pure (vs Zen-powered); suppresses Zen effects    |
| **Teleportation Spike** | 75,000             | Places return beacon. Can recall user from up to 5km. Single-use.                          | N/A                                    | N/A — teleports user to spike location                 |
| **Gravity Well Mine**   | 8,000              | Pulls targets toward center. 10m radius.                                                    | DC 14 Strength or Reflex               | `2d6` Force; **immobilizes** if failed by 5+            |

---

### 🔧 DEPLOYMENT RULES

- **Traps & Mines**: Take 1–2 actions to set. Stealth determines concealment success.
- **Grenades**: Thrown within STR × 2 meters. Detonate on impact or via trigger.
- **Ordinance Platform**: Treated as vehicle extension. Use vehicle skill for targeting.
- **Kinetic Orb**: Acts on command; movement speed 10m/turn; can be blocked or destroyed.

---