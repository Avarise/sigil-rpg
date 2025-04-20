# Reactor & Thruster Manual — Monarch Advanced Dynamics
**Model:** MAD-FV-Mk I “Ventline” Fusion Reactor & FV-Vector Thruster Package  
**Role:** Compact, modular fusion powerplant and matched vent-thruster system for small-to-medium spacecraft.  
**Manufacturer:** Monarch Advanced Dynamics — open-standard designs, widely licensed.

---

## Overview / Lore
Monarch’s **Ventline** family is the industry standard for small fusion-powered craft. The design strips propulsion down to essentials: a compact fusion core, a guided magnetic *plasma channel* and a vectoring thruster “bell.” Because the system vents spent fusion fuel as reaction mass (high-velocity hydrogen/deuterium plasma), it eliminates complex turbomachinery — low moving part count, rapid throttle response, and very high effective specific impulse.

Ventline reactors are sold in a single **module** that is intentionally modular: 1 MAD-FV-Mk I module is sized/powered for ~30 m-class craft; stacking 2–4 modules scales linearly for larger hulls (4 modules comfortably serve ~100 m class). All Monarch cores use open access ports and standard fuel cartridges (Deuterium Cartridges) and include a built-in breeding loop and fuel access bay for industry standard rods/cartridges.

---

## Key Specs (Real-world flavored + Game stats)

### Fuel & Energy
- **Fuel type:** Deuterium Cartridges (standard Monarch cartridge)  
- **Cartridge capacity:** **50,000,000 Sparks** (each) → **50,000,000 × 10 MJ = 5.0×10¹⁴ J**  
- **Cartridge slots/module:** **5** (unless modified) — total on-board stored energy per module = **250,000,000 Sparks**  
- **Breeding Loop:** integrated breeding loop (closed-cycle breeder) — passive production: **~1 partial cartridge equivalent every 60–120 days** with continuous operation and access to breeding feedstock. (GM may require infrastructure & catalysts to reach upper efficiency.)

### Electrical / Thermal
- **Continuous electrical output (nominal, per module):** **1.0 GW** (1×10⁹ W) → equals **100 Sparks/sec** (≈6,000 Sparks/min; ≈360,000 Sparks/hr).  
  - **Game shorthand:** **Module Output:** **1 GW (≈360k Sparks / hour)** at baseline load.
- **Peak divertible power:** up to **3.0 GW** for short bursts (10–60 s) before thermal limits; sustained higher output requires extra cooling or multiple modules.
- **Thermal waste:** ~**70%** of fusion power rejected as heat under normal operation; radiator arrays/heat sinks required.

### Thrust (Fusion Vent Thruster)
- **Exhaust velocity (ve):** **0.1 c** (10% speed of light) nominal for optimized venting pulses (game abstraction; very high Isp).  
- **Impulse per cartridge (physics conversion):** ~**3.3×10⁷ N·s** of total impulse per cartridge (approx; physics derivation — used to create simple game numbers below).  
- **Game Thrust Figures (simplified):**
  - **Impulse (per cartridge):** **+3,300 m/s Δv** for a **10,000 t** frame (use scaling rules below) — *abstracted as a per-cartridge delta-v pool for the ship.*  
  - **Sustained thrust (continuous venting):** with mass flow adjustments and divertible power: **enough for effective cruise burns and quick orbital maneuvers**; actual Δv depends on hull mass and number of cartridges consumed.

> **Game rule (recommended):** Treat each cartridge as a discrete “propellant packet.” For a ship of mass `M` (in tonnes), one cartridge yields `Δv_cartridge ≈ 3,300,000 / (M in tonnes)` m/s. E.g. a 10-ton scout ≈ 330,000 m/s (huge), a 10,000-ton corvette ≈ 330 m/s. GM may cap delta-v vs realism.

---

## Module Scaling & Fitment
- **1× MAD-FV-Mk I** — designed for **~30 m** class craft (scout / courier). Powers ship systems (life support, basic shields, sensors) and provides modest propulsion and reserve for short bursts.
- **2× Modules (twin banks)** — suitable for **40–60 m** ships (light corvette, river freighter). Redundant reactors increase safety and burn capability.
- **3–4× Modules** — **~100 m** class ships (freighter / large corvette) depending on hull efficiency; 4 modules provide comfortable operating margin for continuous shield use and heavy burns.
- **Modularity:** connect modules through standard bus. Modules can be ganged for parallel power, or zoned for redundancy.

---

## Game Mechanic Summary (GM-ready)
> These are plug-and-play stats for use at the table. Adjust to campaign tone.

**MAD-FV-Mk I (single module)**  
- **Module Size:** Small reactor module (install slot: Reactor I)  
- **Mass:** 12 tonnes (module)  
- **Stored Fuel Capacity:** 5 cartridges (on-module magazine)  
- **Nominal Output:** 1 GW (continuous) = **360,000 Sparks/hr**  
- **Peak Burst Output:** 3 GW for up to 60 seconds (cooldown required)  
- **Exhaust Impulse (per cartridge):** Provides a ship-level Delta-V pool of `Δv_cartridge` (see formula) — for GM ease, define discrete Δv per ship by tonnage.  
- **Heat / Signature:** High. Operating at cruise raises ship heat signature: **+2 RSR penalty** (makes ship easier to detect), venting/boost burns add **+4 for duration**.  
- **Startup Time:** 5–30 seconds depending on cold/hot start and crew skill. (Instant warm restart when kept warm.)  
- **Cooldown / Maintenance:** Radiation & neutron flux damage accumulates to module integrity. **Routine maintenance every 100 operating hours**. Critical overhaul every 1,000 hours.  
- **Malfunction Table (on catastrophic hit or poor maintenance):** chance to breach, pressure spike, or forced emergency vent. (GM table suggested: 1% per 100 hours + modifier.)

**Fuel Consumption (game rules):**  
- **Normal power draw (cruise/idle ship systems):** ~**25–100 Sparks / minute** depending on ship size and shield usage. (MAD module rated to supply.)  
- **Thruster burn:** Using thruster for propulsion consumes **cartridge propellant** in two ways:
  - **Pulse mode (high impulse):** consume `1 cartridge` per major burn (suitable for interplanetary impulse) — yields Δv pool as above.  
  - **Sustained vent (fine burns):** draw power from reactor; fuel mass flow scales with thrust; GM can convert Sparks/sec diverted into fraction of a cartridge used per minute. (Simplify by letting repeated sustained burns consume `0.01–0.1 cartridge` per minute depending on thrust level.)

---

## Integration with Ship Systems
- **Shield recharge:** High-frequency shields may draw electrical power. A single module can recharge low-duty high-freq shields at baseline; multiple modules allow continuous defensive recharge while thrusting.  
- **Life Support & Systems:** 1 module supports life support for a small crewed ship (~up to 20 crew) in normal conditions; for larger vessels, combine modules.  
- **Power Redundancy:** Recommend at least 2 modules for mission critical warships or passenger craft — reduces single-point failure risk.

---

## Installation & Ports
- **Fuel Ports:** Standardized Monarch cartridge interface (hot-swap capable). Each module has an **access bay** for insertion/removal of cartridges and an external port for breeder feedstock.  
- **Breeding Port:** dedicated plumbing/fuel-processing port for catalytic breeding & salvage intake. Requires maintenance clamp for catalyst refills.  
- **Magnet & Channel Interface:** secure, shielded conduits that route plasma from reactor to thruster. Conduits must be maintained; damage reduces thrust efficiency.

---

## Safety & Emergency Procedures
- **Emergency Vent:** If core instability occurs, reactor can dump core plasma through emergency vent — very loud and reveals precise location (RSR spike), but prevents meltdown. Often destroys any trailing drones/smaller appendages.  
- **Containment Protocol:** Maintain breeding loop coolant at 95% nominal. If coolant drops below 60%: automatic power reduction to 25% and forced shutdown in 30s.  
- **Radiation & Decon:** Cartridge handling requires radiation suits; spent cartridges store activated materials and must be disposed or processed into breeder bays.

---

## Game Narrative Hooks & Tech Flavor
- **Monarch cartridges** are tradeable commodities — high value at frontier outposts. A single cartridge (~50M Sparks) is valuable enough to fund months of a small ship’s operations.  
- **Breeding loop** plots create long-term campaign hooks: colonies focusing on independent fuel production, sabotage of breeder catalysts, or heists of fresh cartridges.  
- **Open standard** nature means you’ll find many vendors and rebranded variants — “Ventline-compatible” is a common sticker.

---

## Example Usage Scenarios (GM Examples)

1. **Scout (30 m craft)** with 1 MAD-FV-Mk I module:  
   - Start with 3 cartridges. Idle ops & comms: ~360k Sparks/hr. One cartridge used for a long interplanetary burn → ship gains ~Δv pool appropriate to its mass (GM uses table).

2. **Corvette (100 m craft)** with 4 modules:  
   - Total continuous power ~4 GW. High-frequency shields remain active during tactical burns. Cartridges consumed faster for major burns but breeder loop across 4 modules produces spare fuel slower.

3. **Heist Hook:** pirates steal a cartridge (50M Sparks) from a depot; security AI triggers reactor safety which marks vault with a heavy RSR spike — rapid pursuit becomes traceable.

---

## Crafting / Market
- **Base Price (new, factory module):** **~1,250,000 Sparks** per MAD-FV-Mk I module (reflects system, casing, magnetics, open-license fees).  
- **Installed cost (shipyards/fitment + conduit rigging):** +50% of module price.  
- **Cartridge price (fresh Deuterium Cartridge):** **50,000,000 Sparks** (stock market value; can vary).  
- **Repair / Overhaul:** Standard maintenance kit: **10,000 Sparks/day** for active crew servicing; catastrophic overhaul ~**5,000,000 Sparks**.

---

## Recommended GM Conversions & Abstractions
- To simplify Δv and thrust in play, precompute **Δv per cartridge** for common hull classes (light scout, courier, corvette, frigate, cruiser). Use the formula above for realism or pick easy round numbers:
  - Scout (10 t): 33,000 m/s per cartridge  
  - Courier (100 t): 3,300 m/s per cartridge  
  - Corvette (10,000 t): 330 m/s per cartridge  
  - Frigate (100,000 t): 33 m/s per cartridge

- For campaign pacing, treat cartridges like high-value consumables: players choose when to burn them for propulsion vs reserve for emergencies.

---

### Quick Reference (box)

- **Module:** MAD-FV-Mk I  
- **Fuel slots:** 5 cartridges (50M Sparks each)  
- **Continuous Power:** 1 GW (360k Sparks/hr)  
- **Peak Burst:** 3 GW (short)  
- **Thrust mode:** Fusion vent → very high Isp; Δv per cartridge scales with ship mass (see example table)  
- **Price (module):** ~1,250,000 Sparks | **Cartridge:** 50,000,000 Sparks

---

If you want, I can:
- Produce a **GM cheat-sheet** table mapping hull tonnages → Δv/cartridge → suggested cartridge burn times, or  
- Create a **shop entry** (full item card) formatted exactly like other gear in your manual, with install recipes, repair DCs, and vendor notes.
