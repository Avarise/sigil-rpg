### Action Order

    Initiative count determines order of character actions.
    At the beginning of combat each character makes Initiative Throw,
    and after order is settled, each character gets pool of resources,
    that refresh at the beginning of each new round. 

    Round:
    Period of 6 seconds, during which all characters take their turns,
    use reactions and other resources. 

    Turn:
    Ordered by rolled initiative, during which, 
    characters may use focus to cast powers and attack,
    or use other resources such as movement. 

    Reaction:
    Limited action used outside of character's turn.
    Each character has one free reaction, with ability to take more
    reactions by consuming Focus. Each character may use up to
    dexterity modifier of reactions (minimum 1) during a Round.  

    Movement:
    Distance a character may travel during a round,
    without using any other resources. 
    This value depends on current Movement Mode of a character,
    such as crouching or sprinting.

### Movement Modes
    Speed of a character is represented as number of meters they can cover during a round (6 second period), without using any Focus. 

    To convert speed into km/h, multiply "per round speed" by 0.6 
    30 meters/round = 18 km/h 

    Some characters may have multiple movement modes each having their own speed, for example Running 30 meters, Flying 60 meters. 
    When a character uses part of a movement as one mode, remaining distance to move on the other modes is proportional:
    Using 10 meters of running, will leave example above with 40 meters of flight left. 

    

    Movement distance can be covered using one of the many available movement actions, like Jumping, Dashing, Sneaking or Sprinting. 

    

    Running is the basic movement mode available to all land creatures, including those traditionally not considered to be running such as snakes. 

    

    Swimming is the movement mode that all creatures perform while in liquids. Creatures with no swimming available, begin to drown. Their movement is half of the running speed, but for each 10 meters moved they need to perform Athletics Check of DC 15. 

    

    Gliding is an aerial movement mode that allows to gain forward movement by redirecting forces of falling down in gravitational field. While most instances of gliding  require dense atmosphere, there are rare devices that allow electromagnetic glide. 

    

    Flying is a mode in which characters has most independence for movement in all directions. It is achieved by using wings, or jet-packs and similar devices. 

    

    Skimming is a hybrid type of movement using feet attachments including but not limited to skiing or skating. Devices called skimming rings expands on concepts introduced in electromagnetic gliders, to allow fully aerial movement. 

    

    Burrowing is movement mode used while moving through ground. 

    

    Phasing is a hybrid movement mode which is based on idea of losing most of the physical form. Used by ghost-like creatures, phasing is the fastest way to move without teleportation. 

    

    Piloting is a mode used by character that uses a vehicle. Independent vehicles, such as rockets or drones are described by using Running Mode. 

    

    

    Movement Actions: 

    Jump: (No focus) 
    Distance of Standing Jump is equal to strength attribute. 
    Distance of Running Jump is equal to twice the strength attribute. 
    Running jump requires running at least 5 meters in direction of the jump. 
    Jump cannot exceed your movement limit.

    Dash: (1 Focus) 
    When you take the Dash action, you gain extra movement for the current turn. 
    You can dash once during your turn. 
    
    Sprint: (Requires full Focus) 
    Use all of your focus to move as far as possible in a chosen direction. 
    Distance you may travel and conditions you suffer during that action  
    depend on your movement mode: 

        Running: 
        Move 3 times your movement distance, +10 meters per each Focus consumed. 
        During sprint, all melee attacks against you have advantage. 

        Swimming: 
        Move 3 times your movement distance, +5 meters per each Focus Consumed. 
        During sprint, all melee attacks against you have advantage. 

        Flight:  
        Move 5 times your movement distance, +15 meters per each Focus consumed. 
        During next turn, you must forgo all of you movement to stop your momentum. 
        Unless you do so, you move 25% of the distance covered in the same direction and you are knocked prone. 
        If you collide with terrain, suffer 1d6 physical damage for 10 meters travelled. 

        Skimming:
        Move 4 times your movement distance, +10 meters per each Focus consumed. 
        Gain bonus to Reflex and AC against ranged attacks equal to consumed Focus while sprinting. 
        Gliding: 


        Phasing: 
        Move 6 times your movement distance, +20 meters per each Focus consumed. 
        During sprint, all melee attacks against you have advantage. 
        Take 1 Force damage for each 1 Focus consumed. 

        Piloting: 
        Move at 150% move speed of current vehicle. Gain additional 5% speed up 
        for each Focus consumed. 
        Ship gains one stack of Overheating. 

    Sneaking: (1 Focus) 
    Halves your movement speed for the rest of a round. 
    Allows you to make a Stealth Skill check. Check automatically fails if 
    Character performing sneak is in line of sight, or is currently in area of detector or sensor. 
    Cloaking effects, such as powers or invisibility devices, may allow user to 
    make checks in the open field.     

    Crouching: (No focus) 
    Halves your movement speed, to stay in prone condition. 
    Cannot be used with Skimming and Flying movement modes. 

    Disengage: (1 Focus) 
    When you disengage, until end of your turn, you cannot be targeted 
    with Attacks of Opportunity. 

    Defend/Dodge: (All remaining Focus, minimum 1) 
    Gain bonus to AC and Reflex equal to ( 1 + consumed Focus ). 
    Your movement speed is halved for the rest of a round. 

    Brace: (1 Focus) 

### Attacks
    Attacks require Focus to perform.  
    They have associated Accuracy, Damage and Lethality ratings. 
    These ratings are based on weapon used to perform attack 
    and may be further modified by character features or external factors. 

    Each attack may critically strike, whenever they roll 20 on the Accuracy Throw. 
    Each point of Lethality extends pool of critical rolls,
    for example, +2 Lethality adds [19/18] to available critical rolls. 

### Basic Attacks: (Available to all characters) 
    Normal Attack: 
    Cost        : 1 Focus  
    Accuracy    : +0  
    Damage      : +0  
    Lethality   : +0  
    Other       : Basic single target attack 

    Expose Attack:  
    Cost        : 1 Focus 
    Accuracy    : +0 
    Damage      : Deals no damage 
    Lethality   : cannot crit 
    Other       : Other attacks against exposed enemy have advantage until 

                        end of targets next turn. 

    Swipe Attack: 
    Cost        : 1 Focus  
    Accuracy    : -1 per each target  
    Damage      : No damage bonus from strength/dexterity/spellcasting modifier 
    Lethality   : Cannot crit
    Other       : On-hit effects like sneak attack apply only half damage to targets 

    Opportunity Attack:  
    Cost        : 1 Reaction 
    Accuracy    : +0 
    Damage      : +0 
    Lethality   : +0 

### Advanced Attacks: (Require unlocking via Prowess Discipline Tree) 
    Heavy Attack I/II: 
    Cost        : 2 Focus  
    Accuracy    : +0
    Damage      : +2/+4, one/two extra weapon dice.  
    Lethality   : +0  
    Other       : Counter and Quick attacks against are made with advantage. Melee only. 

    Precision Attack I/II: 
    Cost        : 2 Focus
    Accuracy    : +2/+4 (Attack gains advantage)
    Damage      : +0
    Lethality   : +1/+2
    Other       : Cannot be counterattacked

    Quick Attack I/II: 
    Cost        : 1 Reaction before attacker attempts to hit you. 
    Accuracy    : +0
    Damage      : Weapon die becomes one tier lower, and d4 becomes 1.
    Lethality   : +0
    Other       : Quick attack may be used when another creature attacks you
                  within melee range. Quick attack will hit before triggering 
                  attack 

    Counter Attack I/II: 
    Cost        : 1 Reaction when you are missed with a melee attack 
    Accuracy    : +0  
    Damage      : Deal extra damage equal to difference between counter attacker's  
                  AC and accuracy throw of the triggering attack. 
    Lethality   : +0/+1 
    Other       : - 