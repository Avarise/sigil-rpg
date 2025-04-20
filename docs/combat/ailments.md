## Status Effects

| Name          | Description                                                                            | Breakout-Cleansable |
|---------------|----------------------------------------------------------------------------------------|---------------------|
| Dead          | HP & Ward at 0.                                                                        | ❌                  |
| Disrupted     | Enemies gain Accuracy Advantage. Becoming Disrupted triggers opportunity attacks.      | ✅                  |
| Prone         | Melee attacks against target gain Advantage, ranged gain Disadvantage.                 | ✅                  |
| Stunned       | Cannot have more than 1 Focus. Cannot have reactions                                   | ✅                  |
| Restrained    | Exposed. Speed = 0. Auto-fails Reflex. Disadv. on STR/DEX checks.                      | ✅                  |
| Frightened    | Disadvantage on skill/accuracy throws. Cannot approach source of fear.                 | ✅                  |
| Grappled      | Requires Athletics to escape. Shared with grappler. Ends on displacement.              | ✅                  |
| Incapacitated | No Focus, Reactions, or Turn.                                                          | ❌                  |
| Incorporeal   | Immune to Physical. Vulnerable to Force. Passes through matter.                        | ❌                  |
| Petrified     | Unconscious. Immune to Bio, vulnerable to Chemical. Poison/disease still active.       | ❌                  |
| Shocked       | Cannot use Reactions.                                                                  | ✅                  |
| Surprised     | Can’t act during first round. Attacks gain advantage. Ends after 1st round.            | ❌                  |
| Unconscious   | Drops items, prone, fails Reflex. Revives at 10% HP.                                   | ❌                  |
| Overwhelmed   | Exposed and Slowed.                                                                    | ✅                  |
| Sense Impaired| Auto-fails checks using the impaired sense. (e.g. Blinded, Deafened)                   | ✅                  |
| Slowed        | Half movement. Disadvantage on Reflex Checks.                                          | ✅                  |
| Weakness      | -1 to Accuracy, Weapon Damage, and Skill throws per stack.                             | ✅ (1 stack)        |

## Damaging Ailments

| Name     | Description                                                                                    | Damage            | Breakout-Cleansable |
|----------|------------------------------------------------------------------------------------------------|-------------------|----------------------|
| Bleeding | 1d4 internal damage/round per stack. One stack removed when regenerating any HP.               | 1d4 per stack     | ❌                   |
| Burning  | Fire damage each round. Must be extinguished using Breakout Action. Damage scales with size.   | 1d4 - 1d12        | ✅                   |
| Poisoned | Damage dealt when accumulated dmg > current HP. 1 Weakness persists while poisoned.            | Accumulates       | ❌                   |

## Breakout

Basic Action available to all characters. It consumes all available focus

**Cost:** 2 Focus

**Effect:** Attempt to end status effects on you.

**Check:** Fortitude vs DC = 10 + 5 per effect  

---
## Legacy docs 
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