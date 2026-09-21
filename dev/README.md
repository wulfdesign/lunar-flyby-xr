# **Artemis: The Free Return — KremFest XR 2026 Update (v2.1.19-dev)**

**A real-time, browser-native Newtonian cislunar flight simulator and WebXR exhibition experience.**

> Step into the commander's seat of Artemis II. Calculate your Trans-Lunar Injection, coast across the cislunar void, gravitationally slingshot around the Moon, and thread the needle on a fiery 12.3G atmospheric reentry—all powered by dynamic Newtonian N-body physics.

### 🚀 **[Launch Active Dev Sandbox](http://localhost:3550/dev/index.html)** *(Served locally via `server.py --dev` on port 3550)*

---

## 🎪 **The KremFest XR 2026 Experience: Cinematic Autopilot & Pacing**

For the **KremFest XR 2026** festival showcase, this major update transforms *Artemis: The Free Return* into an awe-inspiring, passive-first cinematic journey. 

In a fast-paced festival environment, guests need to be able to don the Meta Quest 3 headset, settle in, and experience the majesty of deep space without getting lost in complicated telemetry menus or stalled in a 10-day orbital wait. 

With an **Autopilot Captain** and **Smart Auto-Warp** at the helm, the entire ~800,000 km voyage is dynamically time-compressed into a tight, breathtaking **~16–17 minute flight**:
1. **Low Earth Orbit & TLI Ignition:** Startup sequence with visual engagement pulses, aligning prograde and firing the 111-second Trans-Lunar Injection burn.
2. **Accelerated Outbound Climb:** Rapidly steps up through intermediate orbital gears (300x -> 600x -> 1800x -> 3600x) as Earth's gravity well recedes.
3. **Deep Space 7.2kx Cruise:** Cruises the vast cislunar abyss at **7,200x** (1 second = 2 hours) in a protected deep-space corridor.
4. **Tighter Lunar Approach:** Holds high cruising speeds closer to the Moon before safely stepping down.
5. **Perilune "Sizzle Shot" Flyby:** Automatically downshifts to **60x** within 5,500 km of the lunar farside, giving festival spectators a breathtaking, cinematic view of the craters and celestial limb.
6. **Accelerated Lunar Departure:** Quickly accelerates out of lunar gravity well back into deep space.
7. **Graduated Earth Approach & Entry Interface:** Drops progressively through safety tiers into Earth's gravity well, locking to 1x at 122 km to endure a brutal 12.3G atmospheric deceleration and plasma blackout.
8. **10x Parachute Descent Auto-Ramp:** Glides swiftly at **10x** through the long subsonic coast, under drogue chutes, and under main parachutes—while smoothly easing down to 1x for 10–15 second observation windows during deployments and the final ocean touchdown.

---

## 🧑‍✈️ **Taking the Helm: Disengaging Autopilot & Auto-Warp**

While optimized for hands-free festival enjoyment, the underlying engine remains an unscripted, 100% dynamic physics sandbox. At any point during flight, pilots can take manual command of their time slip, orientation, and flight maneuvers!

### 1. How to Turn Off Auto-Warp
- **Desktop:** Click the **`AUTO WARP`** toggle button in the top-right HUD header (or press `W`).
- **WebXR (VR):** Point your controller raycast laser at the floating HUD and trigger-click the **`AUTO WARP`** button.
- **Manual Gear Shift:** Once Auto-Warp is **OFF**, the flight computer stops automatic speed adjustments. You have complete manual authority over all 9 gear levels (1x, 10x, 30x, 60x, 300x, 600x, 1800x, 3600x, 7200x).
- **WebXR Motion Comfort:** All speed changes use our continuous **Cubic Hermite Smoothstep Gliding Protocol** (1.0s ease-in/ease-out per tier) to eliminate sudden visual tearing and prevent motion sickness.

### 2. Pushing the Sim Flight Time (Speedrunning the Moon)
Pilots who want to shave time off the 16–17 minute mission can attempt to push their flight time:
- **Running Hot with Auto-Warp ON:** You can manually click a **Yellow Advisory** speed (such as 300x or 600x during lunar approach). The flight computer registers your command intent (`userSelectedWarp`) and maintains the faster speed until the safety envelope drops!
- **Running Wild with Auto-Warp OFF:** Disengage Auto-Warp and push a notch into the **Red** speed regime around the Moon or fire your own manual transverse thrusters for Mid-Course Corrections (MCC).

### 3. Skip to Checkpoint (Experimental)
- The HUD features **`Skip to Next Checkpoint`** actions (TLI, Moon, Earth Return, Re-entry).
- When triggered, this accelerates time-warp directly toward the target flight milestone. 
- *Note: This feature is currently in active testing and calibration.*

---

## 🗺️ **Roadmap to v3.0: Physical Pilot Command**

Currently in v2.1.18, Mid-Course Correction (MCC) burns and TLI alignments are calculated and oriented automatically by the digital flight computer.

On the roadmap for **v3.0**:
- **Computer-Targeted, Pilot-Executed Burns:** The flight avionics will compute the exact transverse Delta-V and entry corridor keyhole, but the human commander will be responsible for:
  1. Manually decoupling from the prograde vector and using Reaction Control System (RCS) thrusters to orient the spacecraft onto the burn vector.
  2. Throttle management: Timing and firing the orbital maneuvering engine to execute the precise delta-V cut.
  3. Real-time reentry lift-vector banking: Steering the capsule through the 2-degree reentry corridor to keep peak Gs below lethal thresholds.

---

## 🥽 **Hardware Setup & Exhibition Guidelines**

### 🎪 At KremFest XR 2026 (Exhibition Floor)
- **Turnkey Immersion:** The Meta Quest 3 headset is pre-calibrated, tethered/streamed, and running on dedicated hardware.
- **Guest Instructions:** Put on the headset, adjust the headstrap for clear focus, and relax. The virtual captain will fly the full mission from Earth orbit to splashdown. Feel free to glance around the cabin and out the viewports!

### 🏠 For Home Users & Remote Pilots
1. Launch the local dev server using `start_dev_server.bat` or `python server.py --dev`.
2. Connect your Quest headset via Quest Link, AirLink, or native Quest Browser to `http://<your-lan-ip>:3550/dev/index.html`.
3. Click **`ENTER VR FLYBY`** to step inside the spacecraft.
4. **Default Mode:** Boots automatically into full Autopilot and Auto-Warp.
5. **Manual Mode:** Look at the HUD controls and trigger-click `AUTO WARP` or `AUTOPILOT` to take over the controls.

---

## 🔬 **v2.1.18 Technical Changelog**

* **Continuous Hermite Time-Warp Easing:** Engineered continuous 1.0s cubic smoothstep rate interpolation (`ease = 3p² - 2p³`), eliminating all instantaneous speed chops for pristine 6DoF WebXR comfort.
* **Tighter Lunar Approach:** Retains 3.6kx down to 42,000 km, 1.8kx down to 22,000 km, and 600x down to 12,000 km, stepping down to 60x at <= 5,500 km for the perilune sizzle shot.
* **Earlier Outbound & Departure Ramps:** Promoted post-TLI climb (1.8kx at 10,000 km, 3.6kx at 22,000 km, 7.2kx at 45,000 km) and lunar departure (300x at 5,000 km, 600x at 10,000 km, 1.8kx at 22,000 km).
* **10x Parachute Descent Schedule:** Auto-Warp maintains 10x Green during settled post-plasma glide and parachute descent, smoothly downshifting to 1x for drogue deployment (8.5 -> 7.3 km), main deployment (3.4 -> 3.0 km), and touchdown (<= 350 m).
* **Sim Flight Time Telemetry:** Live HUD mission timer and structured JSON flight logs (`Artemis_FlightLog_*.json`).
* **Offline Asset Suite:** 100% self-contained offline Three.js r128 and local high-resolution 4K textures in `dev/vendor/` and `dev/textures/`.

---

## 👨‍🚀 **Attribution & Creative Team**

* **Creator & Technical Lead:** Larry James (Wulf Design Studios / UpLiftVR Studios / VRMakerDome)
* **Festival Selection:** KremFest XR 2026 (FilmFreeway Official Submission)
* **License:** MIT License — Open-source space democratization.
