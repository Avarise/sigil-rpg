## Dossier: Fission-Pumped Spinal Laser — "Aegis Spine" Series

**Class:** Spinal Heavy Weapon (Capital-grade)  
**Model Family:** Aegis-FSL (Fission-Pumped Spinal Laser) — multiple vendors license the open standard.  
**Mounting:** Spinal (longitudinal) — must be aligned with ship vector to fire.  
**Fuel:** Fission Pellets (sealed subcritical pellets, single-use “pucks”)  
**Role:** Ultimate hard-tackle weapon — designed to annihilate fortified plating, overload shields, and rupture internal systems at extreme range.

---

### Executive Summary / Lore
The **Aegis** family uses compact fission charges to *pump* a high-gain laser medium for a single, earth-shattering discharge. Unlike conventional chemical or electrical lasers, the Aegis uses the intense neutron/gamma flux of an engineered, controlled fission pulse to invert population in the lasing medium (optical → soft X / hard X bands depending on variant). That allows a single shot to concentrate **tens to thousands of GJ** of coherent energy onto a target — enough to punch through multiple meters of plated hull and evaporate whole decks.

Because of cost, size, and danger, Aegis units are only found on capital ships, fortified installations, and very expensive private warships. Their spinal mounting forces tactical positioning and makes the weapon the focal point of fleet maneuver.

---

### Basic Physics / How it Works (brief)
- **Pump source:** A sealed fission pellet is driven into a near-supercritical transient by an external initiation pulse (not a nuclear explosion — controlled neutron flux with heavy tamper & reflectors). The pellet produces an intense burst of neutrons/gammas for milliseconds.
- **Lasing medium:** Surrounding the pellet is a high-gain lasing cavity (often X-ray capable, or optical with doped crystal/gas cells). The fission burst excites the medium; rapid stimulated emission is routed into the beamline.
- **Beam shaping & optics:** Special hardened mirrors or grazing-incidence optics collimate the pulse into a highly coherent beam with extremely small divergence. Final optics are heavily shielded and cooled.
- **Shot:** Discharge duration is short (milliseconds to seconds) — energy delivered in a focused pulse that couples deep into materials and drives massive secondary effects (shock, spallation, x-ray cascades).

---

### Weapon Effects & Interaction with Defenses

#### 1) Shields
- **High-Frequency (HF) Shields:**  
  - HF shields excel at handling coherent EM but are optimized for lower-energy photon bands and charged particle streams. The Aegis beam is an **extremely high flux, broad-spectrum photonic / soft-xray pulse**.  
  - HF shields will attempt to reflect/deflect portions, but **local cell saturation** occurs: when incident energy density exceeds a shield cell’s instantaneous absorption capacity, the cell **collapses**.  
  - **Game effect:** Treat Aegis pulses as *area-saturating* — apply shield HP damage to several adjacent cells at once; if any cell is driven to 0, a **breach column** opens through to hull with enhanced penetration.
- **Low-Frequency (LF) Shields:**  
  - LF shields are heat-sinks. Aegis pulses deposit huge heat in a very small area; LF cannot dump it fast enough → **localized melt/ablation** and likely permanent local collapse.  
  - **Game effect:** Double effective damage to shield HP and reduce recharge time drastically.

#### 2) Plating & Hull
- The beam couples volumetrically: not only does surface melt occur but **deep channels form**, internal structures vaporize, wiring bundles detonate, and ammo/volatile stores often auto-ignite or detonate.  
- **Reactive plating** may detonate, amplifying damage but causing secondary explosions (dangerous to both attacker & defender).  
- **Crystalline / tungsten plating** resists coupling a bit (higher melting/vaporization thresholds), but once breached, brittle fracture and spallation cause catastrophic internal damage.

#### 3) Internal Systems & Cascading Failures
- High-energy photons and secondary neutrons can induce:
  - **Electronics kill:** avionics, fire-control, and sensor nodes fried (electromagnetic pulse & ionizing damage).  
  - **Reactor trip / core damage:** seeds for reactor meltdowns or automatic scrams.  
  - **Ammo/propellant cookoff:** internal explosions if ordnance or fuel is present.  
- **Game effect:** Aegis pulses have a high chance to score **system hits** after penetrating shields & plating (see Game Rules below).

---

### Design Considerations & Safety

#### Structural & Ship Integration
- **Spinal mounting** requires massive structural reinforcement along the keel. Firing exerts thermal & radiation stress along the barrel and into the ship; recoil is negligible (photonic), but mechanical shock and EM loading are substantial.
- **Shielding shells** and **recovery bulkheads** must be placed between weapon bay and crew spaces.  
- **Pellet handling:** remote pellet carousel, robotic manipulators, leaded glove boxes, and dump ports for spent pellets.

#### Heat & Waste
- The pump event produces prompt radiation and heat. **Radiators** and **pulse capacitors** are required to capture and control the energy. Post-shot, the lasing cavity and optics are hot and require cooldown and reconditioning.
- **Radiation hazard:** Pellets get activated; spent pellets are highly radioactive waste and must be stored or reprocessed.

#### Logistics & Supply
- **Pellet cost** is high (manufacture, shielding, legal control). They are strategic resources—targets for theft and piracy.
- **Reload time** is non-trivial: pellet handling + optics reset + cap recharge → ranges from **minutes to hours** depending on shot class and ship systems.

---

### Energy & Cost Framework (in Sparks)

> **Notation:** 1 Spark = 10 MJ

| Shot Class | Beam Energy | Spark Cost | Typical Charge Time | Use Case |
|---:|---:|---:|---:|---|
| **Disruptor** | 100 GJ | **10,000 Sparks** | 30–90 s | System crippling shot vs frigate/large corvette |
| **Obliterator** | 1,000 GJ | **100,000 Sparks** | 2–10 min | Capital strike — punch through heavy shields & decks |
| **Cataclysm** | 10,000 GJ | **1,000,000 Sparks** | 10–60 min | Strategic annihilation; can gut a station or capital ship |

**Capacitor sizing:** Cap banks should be ~**1.2–2×** the shot energy to cover inefficiencies and pumping overhead.

**Pellet consumption:** Each shot requires **1 pellet** of matching yield. Pellets are consumables; pellet cost ≈ **shot Spark cost × (manufacturing premium)**. Sample pricing:
- **Disruptor pellet:** 12,000 Sparks (factory sale)  
- **Obliterator pellet:** 120,000 Sparks  
- **Cataclysm pellet:** 1,200,000 Sparks

(Players & GMs: vendor markup, scarcity, and legal restrictions alter market price.)

---

### Mount & Module Stats (GM-ready)

**Aegis-FSL-Spine (Basic mount)**  
- **Install Slot:** Spine I/II/III (varies by variant)  
- **Mass:** 2,500–40,000 tonnes (scale with variant)  
- **Optics Vulnerability:** -2 to ship stealth (high signature) while charging; fire adds +6 RSR for duration.  
- **Rate:** See shot classes above (cooldowns & charge times).  
- **Accuracy:** Very high at long ranges; however, firing requires **line alignment** (ship must point the spine at the target). Use **Vehicle Usage** + **Navigation** checks for fine aim; substantial penalties if forced to yaw under fire.  
- **Recoil/Effect:** Photonic — no recoil, but **ship systems suffer EM stress** (minor chance of temporary system outages after each shot on poor maintenance).

---

### Game Mechanics — Resolution Rules (suggested)

1. **Charge Phase:** Firing requires a charge phase. During this phase (30s–60min depending on shot) enemy forces can attempt to interrupt:
   - **Hacking / ECM vs. Engineering:** Opposed Programming (attacker) vs. Engineering/Programming (defender) checks to jam, misalign, or detonate pellet prematurely.
   - **Tactical:** Boarding teams or missile strikes during charge can cause misfire with catastrophic results.
2. **Fire Roll:** When shot fires, make an **Accuracy Throw** (Vehicle Usage or dedicated Fire Control) modified by range and aim conditions.
3. **Shield Resolution:** 
   - Apply shot energy as concentrated energy to shield grid → **divide energy across N adjacent shield cells** (GM chooses N based on shot focus; spinal beams can be focused to affect 1–3 cells or defocus to 5–15 cells).  
   - Cells that receive energy > cell capacity are **overloaded** → their HP is reduced by overload amount; if any cell collapses, beam funnels more energy into hull.
4. **Plating Resolution:** After shield depletion or cell collapse, convert remaining energy to **plating penetration**:
   - Use a conversion table: e.g., **1 GJ** → 100–1,000 plating HP equivalent depending on plating type & local coupling (GM to calibrate).  
   - On penetration, roll for **system hits** (reactor, weapons, magazines). A successful penetration usually guarantees at least one internal subsystem critical hit for Obliterator+ shots.
5. **Collateral / Secondary:** On a hit, roll for secondary effects (ammo cookoff, reactor instability, chain reactive plating detonation). High chance for Cataclysm shots.
6. **Aftermath:** Spent pellet and optics require cooldown/repair. If a pellet is detonated (interrupted), treat as an internal explosion with high damage to the firing ship — severe risk to unsafe operators.

---

### Counters & Tactics
- **Intercept before charge completes:** missile salvos, boarding sabotage, or long-range ECM can abort firing sequences.  
- **Sacrificial shielding cells:** distributed energy cells or ablative tiles to soak an Aegis pulse.  
- **Hard killpoint:** target the beam optics or pellet carousel to disable weapon.  
- **Operational law:** many systems control deployment of Aegis weapons by treaty; their use triggers political/hard consequences.

---

### Upgrades & Mods
- **Rapid Conditioning:** reduces charge time by 20–50% at the cost of optics wear.  
- **Yield Tuning:** allow lower-yield shots (save Sparks & pellets) but maintain long-range punch.  
- **Pellet Reprocessor:** shipboard module to salvage and partially reconstitute spent pellets (low efficiency).  
- **Optic Armor:** sacrificial armoring for the beam array (adds HP to optics but increases heat load).

---

### Example Tactical Use Cases (GM Hints)
- **Ship vs Ship:** An Obliterator shot aimed at the enemy’s bridge column after shield collapse will likely disable command and possibly induce reactor failure.  
- **Station Buster:** Multiple Cataclysm pellets fired in sequence can break a station’s backbone. Require allied ships to defend during long charge.  
- **Strategic Deterrent:** Even a single Aegis mount deters most pirates; its presence shapes campaign politics.

---

### Quick Reference (box)

- **Weapon:** Aegis-FSL (Fission-Pumped Spinal Laser)  
- **Mount:** Spinal (must point ship)  
- **Shot Tiers:** Disruptor (100 GJ / 10k Sparks), Obliterator (1,000 GJ / 100k Sparks), Cataclysm (10,000 GJ / 1M Sparks)  
- **Pellet:** Single-use, required per shot (costs ~1.2×Spark cost)  
- **Charge:** 30 s → 60 min depending on class  
- **Effects:** Shields overloaded (multi-cell), deep plating penetration, internal system hits, massive collateral risk  
- **Counterplay:** Interrupt charge, target optics/pellet carousel, use ablative cells and distributed shielding

---

### Closing Note
The **Aegis** is a campaign-level tool: dramatic, terrifying, and consequential. Its use should be rare and narrative – the political and logistical costs of firing a Cataclysm round should be as meaningful as the damage it inflicts. For players and GMs: treat Fission-Pumped Spinal Lasers as game-defining assets, not routine armaments.

---
## Particle Lance — Design Dossier (SigilRPG)

A **Particle Lance** fires a tightly collimated beam of **relativistic helium nuclei** (α-particles, He²⁺) for **~0.5 s** per shot. It couples a compact heavy-ion accelerator to a magnetic beamline and final-focus vector optics. The shot deposits energy *volumetrically* inside targets (not just on the surface), drilling plasma channels through plating and dumping heat into shields.

---

### 1) Physics at a glance

- **Projectile:** fully-stripped **He²⁺** (mass ≈ 4 amu; charge = +2e).  
- **Shot window:** ~**0.5 s** continuous beam.  
- **Typical kinetic energy (per α):** **1–5 GeV** (γ ≈ 1.27–2.34; β ≈ 0.65–0.90).  
- **Beam power:**  
  - 100 MJ shot (10 Sparks) → **200 MW** over 0.5 s  
  - 1 GJ shot (100 Sparks) → **2 GW** over 0.5 s  
  - 10 GJ shot (1,000 Sparks) → **20 GW** over 0.5 s  
  *(1 Spark = 10 MJ)*

- **Number of ions (example):** at **5 GeV/α** (≈8.0×10⁻¹⁰ J), a **1 GJ** shot uses ~**1.25×10¹⁸** α (total beam mass ~**8×10⁻⁹ kg**).  
- **Momentum (ultra-relativistic):** p ≈ E/c → **1 GJ** shot ≈ **3.3 N·s**.  
  - *Damage is heat/ablation (energy deposition), not “push.”*

#### Beam transport & scale
- **Magnetic rigidity:** \( p[\mathrm{GeV}/c] = 0.2998\,B[\mathrm{T}]\,\rho[\mathrm{m}]\,q \).  
  - At **5 GeV/α** → p ≈ **7.9 GeV/c** → **Bρ ≈ 13 T·m** (q = 2).  
  - 5 T bends ⇒ radius ~**2.6 m** (compact rings/achromats are feasible).
- **Acceleration gradient (ship-grade RF):** ~**20–80 MV/m**.  
  - **1–5 GeV** needs **~15–250 m** effective path (linac + recirculation).  
  - Practical on **frigate/capital** hulls; “light lance” fits corvettes via lower energy or modular folded beamlines.
- **Divergence:** set by emittance & space-charge; with neutralization (see below) sub-mrad beams are plausible → **meter-class footprints at hundreds of km**, tens of meters at thousands of km.

---

### 2) Interaction with defenses

#### A) **Energy Shields**
- **High-Frequency (HF)** — EM-driven, fast-recharge.  
  - Pure He²⁺ beams are **strongly deflected** by HF fields (Lorentz force).  
  - **Counter:** *charge-neutralized beam* (co-moving e⁻ stream → quasi-neutral plasma) greatly reduces deflection; HF shields then mostly **absorb/reflect via plasma pressure**, shifting to **heat load**.
- **Low-Frequency (LF)** — heat-sink style (slow recharge from engine waste heat).  
  - Treats the lance as **thermal input**. The beam **punches through locally** (narrow, intense channel) and **overwhelms local cooling**, forcing **localized shield collapse** if power density exceeds the local max.  
  - Repeated pulses **ratchet heat**; LF shields **lag** between pulses.

#### B) **Plating**
- **Hardened/Tungsten:** high Z & density → **short stops & strong heating**, **secondary radiation**, **spallation**; good *surface* survivability but prone to **channel drilling** and **edge melt**.  
- **Reactive:** multiple layers **trigger easily**; lance **pre-heats** and detonates layers → **large local overburden removal** but expensive to repair.  
- **Superconductive plating (shield-hugging)**: reduces shield standoff → **keeps shielding pinned**; lance still **burns a filament**; shield-plate coupling **spreads heat** (helps vs single pulses, worse vs sustained fire).  
- **Bio-plating:** high hydrogen content → good against x-rays/2º radiation; **ablates** into steam/plasma; **self-heal** mitigates shallow gouges but **deep channels** remain.

> **Rule-of-thumb energy deposition:** To *melt/vaporize* steel you need ~**7–10 MJ/kg**.  
> **1 GJ** (100 Sparks) can **vaporize ~100–140 kg** of steel (if perfectly coupled) → a **deep, narrow bore** through plating + shock-heated inner layers.

---

### 3) Design considerations

1. **Charge Neutralization:**  
   - Add an **e⁻ injector** at the final focus to create a **quasi-neutral plasma beam** (He + electrons). This **defeats HF deflection** and **reduces space-charge blow-up**, cutting divergence.
2. **Final Focus & Vectoring:**  
   - Superconducting quadrupoles + fast steering coils; **milliradian slews** in **<10 ms** let you “dither” the beam to **scribe** shapes or **saw** through edges.
3. **Windowless Barrel:**  
   - No physical window (it would flash). Use **differential pumping** and **magnetic cusp** to keep accelerator under vacuum while the muzzle sees space.
4. **Thermal Management:**  
   - Accelerator & magnets dump **tens of MW** (idle) to **GW-class** (firing) waste heat → **dedicated radiators & phase-change heat sinks**.  
   - Expect **signature spikes** (RSR +4 while firing).
5. **Power Conditioning:**  
   - **Capacitor banks** buffer the **GW pulses**.  
   - Example: **1 GJ** shot over **0.5 s** = **2 GW** beam + ~**1–2 GW** overhead → **caps sized** for **~1–2 GJ** with **<1 s** recharge from a **multi-GW** bus or staged over longer with **HF shields throttled**.
6. **Radiation & EMI:**  
   - **Prompt gammas/neutrons** from target spallation; **hard x-rays** from beamline losses. Shield crew spaces; isolate avionics; enforce **interlock arcs**.
7. **Logistics:**  
   - **He fuel** is tiny mass per shot; the **true cost is energy**. A **10 GJ** volley is **1,000 Sparks** from the ship grid, not the helium tank.

---

### 4) Energy requirements (Spark economics)

| Shot Class | Beam Energy | Spark Cost | Beam Power (0.5 s) | Typical Use |
|---|---:|---:|---:|---|
| **Skirmish** | **100 MJ** | **10 Sparks** | **200 MW** | light corvette, carving sensors/radiators |
| **Tactical** | **1 GJ** | **100 Sparks** | **2 GW** | main battery strike vs plating/shields |
| **Siege** | **10 GJ** | **1,000 Sparks** | **20 GW** | capital volley / emplacement kill |

> **Cap banks:** dimension at **1.2–2×** the beam energy to cover accelerator overhead and maintain muzzle quality.

---

### 5) Game implementation (quick rules)

**Weapon:** *Particle Lance (He²⁺)*  
- **Attack Type:** Ranged (Beam) — uses **Navigation (Wis)** or **Engineering (Int)** for tracking/pointing (GM’s call).  
- **Range:** **Line-of-sight**; impose **divergence penalties** beyond **5,000 km** if unfocused/uncharged; charge-neutralized beams ignore up to **50,000 km** for capital mounts.  
- **On HF Shields:** If **not neutralized**, **HF shields gain advantage** on mitigation/deflection. If **neutralized**, treat as **Energy (Force/Fire)**: apply **Damage Threshold**, then HP.  
- **On LF Shields:** Apply **full energy** as **heat**; if **instantaneous flux** exceeds LF local limit, **create a breach** (treat as shield HP damage with ×2 vs localized cell).  
- **On Plating:** Convert **Sparks → HP** by your vehicle damage scale; on crit, apply **Overwhelmed** and **Blinded** (sensor bloom), and **ignite** exposed volatiles.  
- **Firing cycle:** **0.5 s** beam; **cooldown** **3–30 s** (mount class) to re-shape caps and magnets; **sustained fire** imposes **heat penalties** (−Accuracy, +Signature).

**Upgrades & Mods**
- **Neutralizer Stage:** Removes HF deflection.  
- **Edge-Scribe Mode:** Micro-slew to **saw** armor seams (bonus vs joints).  
- **Pulse-Train Gate:** Splits the 0.5 s into **N micro-pulses** (helps vs reactive plating triggers).  
- **Spectral Spoofing:** Modulates beam to **confuse shield discriminators** (contested Programming vs target ECM).

---

### 6) Back-of-the-envelope: armor drilling

- To **open a 10 cm diameter hole** through **1 m** of steel: volume ≈ 0.00785 m³ → mass ≈ **~62 kg** → **~500 MJ** to melt/vaporize (optimistic; real ≈ 0.5–1.0 GJ including losses).  
  - ⇒ A **1 GJ** shot can plausibly **bore** such a hole (with spall cone & internal damage).  
  - Tungsten (denser, higher melt/vap): add **×1.5–×2** energy.

---

### 7) Mount classes (suggested)

| Mount | Ship Size | Shot Class | Cap Bank | Re-charge | Notes |
|---|---|---:|---:|---:|---|
| **L-Light** | Corvette | 10–100 MJ | 50–200 MJ | 3–5 s | Skirmish, radiator killers |
| **M-Medium** | Destroyer/Frigate | 0.5–2 GJ | 1–4 GJ | 5–15 s | Primary battery |
| **H-Heavy** | Cruiser/Capital | 5–20 GJ | 10–40 GJ | 10–60 s | Siege, shield-breach volleys |

---

#### Designer’s Notes
- **Helium** is chosen for **manageable rigidity** (compact magnets) and **high linear energy transfer** (dense ionization → brutal local heating).  
- **Why not photons?** Lances trade perfect line-of-sight and mirror defenses for **volumetric coupling**—they *plow* through and **cook** things that lasers must dwell on.  
- **Counter-play:** HF shield tuning (phase-shifting to kick charged beams), **plasma shutters**, sacrificial **ablator tiles**, **magnet curtains**, and **pitch/yaw jitter** to smear the drill point.
