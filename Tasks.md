# 📋 Tasks & Upgrades - Lunar Flyby XR

**⚠️ CRITICAL INSTRUCTION FOR AI AGENTS ⚠️**
DO NOT mark any task as done (🏆 or [x]) until the Human-in-the-Loop (Magus Wulf) has explicitly verified the output. Move finished tasks to 🧪 (Ready for QA) first. Use your Attribution Mark (🐈/🦞).

## 📖 Legend
* **Priority:** 🔥🔥🔥 (Critical) | 🔥🔥 (High) | 🔥 (Medium) | 🧊 (Cold/Icebox)
* **Model Routing:** 🏗️ (Architect) | ⚡ (Runner) | 🎭 (Local)
* **Status:** 🛠️ (In Progress) | 🧪 (Ready for QA) | 🧠 (HITL Action Needed) | 🩹 (Tech Debt) | 🏆 (Verified/Done)
* **Attribution:** 🐈 (Hermes) | 🦞 (MugWort)

**Version:** v2.1.21 (Modular Mission Pack Plugin Architecture & Seattle Space Week Roadmap 🚀🧩📇🪙✨)

---

## 🧪 Waiting for QA (Ready for QA 🧪)
* [ ] 🧪 🔥🔥🔥 **Direct Browser Play Portal, Early Access Funnel & Dev Feedback Pipeline (v2.1.20):** Architect and stage dedicated public mission landing page / launcher allowing visitors to launch the full WebXR simulation directly in-browser with 1 click, capture Early Access Flight Crew email sign-ups for launch notifications and mission updates, collect community feedback, and deliver access to the gated bleeding-edge dev sandbox (`/dev/`) with a dedicated co-creation feature request form ("Request for stuff"). 🧪 🚀 🌐 📬 🥽 🐈 ✨
* [ ] 🧪 🔥🔥🔥 **KremFest XR 2026 Production Release & Live UI Version Indicators (v2.1.19):** Promoted empirically verified dev sandbox (16:45.2 flight time in `Artemis_FlightLog_2026-09-21T22-34-08.json`, 2,452 km perilune flyby, 12.7G entry peak, 9.0 m/s splashdown) to root production `index.html`. Integrated live Early Access Alpha version and release channel indicator (`v2.1.19-dev` in dev sandbox, `v2.1.19 (Production)` in root release). Ingested 100% offline Three.js r128 and high-res texture assets into root repository. Merged KremFest XR 2026 update announcement and comprehensive festival particulars into public-facing `README.md` while preserving all original deep-dive documentation. Bumped `server.py` to v2.1.19. 🧪 ⚡ ⏱️ 🎪 🥽 🐈

---

## 🏆 Completed / Verified (Past Sprints 🏆)
* [x] 🏆 🔥🔥🔥 **Tighter Lunar Approach & Earlier Outbound/Departure Warp Acceleration (v2.1.18):** Calibrated faster speed ramps across outbound climb and lunar transit while leaving pristine Earth approach and re-entry/touchdown untouched. Empirically verified in `Artemis_FlightLog_2026-09-21T22-34-08.json` with 16:45.2 total flight time, 2,452 km perilune pass, 12.7G max G, 9.0 m/s touchdown. 🏆 ⚡ ⏱️ 🌕 🐈
* [x] 🏆 🔥🔥🔥 **Deep Space 7.2kx Cruise, 300x Lunar Approach, 60x Perilune Sizzle Shot & Auto Descent 10x Ramp (v2.1.17):** Squeezed overall flight simulation duration down to 15-20 minutes by optimizing safe warp envelopes across all flight phases. Re-enabled 7.2kx (`7200x`) Tier 1 Green cruise in deep space corridors. Promoted lunar approach and departure (between 6,000 km and 25,000 km) to 300x Green, preserving the 60x sizzle shot envelope. Removed obsolete render loop `shiftWarp(1)` override under mains ($altE < 3.0\text{ km}$), enabling 10x down to 350 meters. Unlocked Auto-Warp throughout atmospheric descent. 🏆 ⚡ ⏱️ 🌕 🪂 🌊 🐈
* [x] 🏆 🔥🔥🔥 **Continuous 1s Ease-In/Out Warp Transitions & 10x Green Atmospheric Descent Schedule (v2.1.16):** Engineered continuous cubic ease-in/ease-out time warp transitions (`smoothWarp = warpTransitionStart + (warpTransitionTarget - warpTransitionStart) * ease`), eliminating all instantaneous speed jumps by smoothly gliding simulation rate across 1.0 full second per tier. Promoted 10x to Tier 1 Green across all settled atmospheric descent zones, with calibrated 1x observation windows before drogue deployment, main deployment, and final touchdown. 🏆 ⚡ ⏱️ 🪂 🌊 🐈
* [x] 🏆 🔥🔥🔥 **Lunar Flyby 30x/60x Green Cruise, 300x/600x Yellow Advisory & High Precision Flyby Integration (v2.1.15):** Recalibrated lunar flyby speed tiers (distM <= 12,000 km) to set maxSafeWarp = 60 (making 30x and 60x Green) and maxAdvisoryWarp = 600 (making 300x and 600x Yellow), while locking out speeds above 600x. Auto-Warp now comfortably cruises through lunar flyby at 60x. Expanded high-precision numerical integration (stepSize = 0.01) to cover the entire lunar encounter envelope (distM < 12,000 km). 🏆 ⚡ ⏱️ 🌕 🥽 🐈
* [x] 🏆 🔥🔥🔥 **Sim Flight Time Telemetry, Inbound Auto-Warp Downshift, 10x Descent Warp & 30s Chute Observation Windows (v2.1.14):** Integrated live wall-clock mission simulation timer on the HUD and inside all telemetry logs / splashdown reports. Calibrated inbound Earth return Auto-Warp downshift. Damped re-entry bank angle oscillations with velocity and deceleration guards. Enabled 10x Yellow advisory warp during atmospheric descent below 35 km with 1x observation windows. 🏆 ⚡ ⏱️ 🪂 🌊 🐈
* [x] 🏆 🔥🔥🔥 **Re-entry Sweet Spot Latch, Post-Flyby Auto Ramp-Up, 6s Operational Timers & Earlier GEO Deceleration (v2.1.13):** Latched atmospheric guidance to neutral trim upon terminal descent. Enabled auto ramp-up when safe envelope expands. Recalibrated lunar proximity for Yellow advisory cruise up to 300x. Tuned Earth return schedule to drop from 600x to 300x earlier at 50,000 km. Reduced auto-alignment and post-burn holds to 6.0s. Fortified `server.py` with `ReusableTCPServer`. 🏆 ⚡ ⏱️ 🥽 🐈
* [x] 🏆 🔥🔥🔥 **Earth Return Pilot Speed Selection, Advisory Warp Honors & Graduated Safe Tiers (v2.1.12):** Implemented `userSelectedWarp` manual command intent so Auto-Warp honors pilot-selected speeds up to `maxAdvisoryWarp`. Recalibrated Earth return graduated safety tiers (10x Green down to 200 km, 30x Green down to 1,500 km, 300x Green down to 15,000 km). Stripped conflicting hardcoded clamps from `updatePhysics`. 🏆 ⚡ ⏱️ 🥽 🐈
* [x] 🏆 🔥🔥🔥 **Universal Smooth Time Warp Stepping Protocol & WebXR Kinetosis Prevention (v2.1.11):** Diagnosed and eliminated abrupt 1-frame time warp jumps down to 1x following MECO and post-burn observation holds. `updateWarpStepping()` enforced as sole runtime gear-shifter with 1.0s dwell per intermediate gear tier (30x -> 10x -> 1x). Implemented `.target-warp` dashed visual outline indicator and progression HUD readout (`30x [>> 1x]`). Ingested into Symbiot Memory substrate. 🏆 ⚡ ⏱️ 🥽 🐈
* [x] 🏆 🔥🔥🔥 **30x Burn Warp Fix, 8s Countdown Hang Resolution, Outbound Progressive Acceleration & Finite Continuous MCC Burns (v2.1.10):** Fixed 30x warp in parking orbit and burns. Resolved auto-align countdown freezing at 8s. Outbound progressive acceleration up to 3.6kx. Continuous 3-4 second finite-duration MCC burns. 🏆 ⚡ ⏱️ 🐈
* [x] 🏆 🔥🔥🔥 **Startup Blink Signals, Non-Restricted Burn Cruise, 10s Auto-Align, 1s Button Indicators & Stepped Lunar/Earth Warp Schedules (v2.1.9):** 5-second startup blink animations for Autopilot (`blink-blue`) and Auto-Warp (`blink-green`). Non-restricted burn entry up to 30x. 10s auto-align timer. 1s button indicators. Progressive 3-tier warp safety and Auto-Warp stepping schedules. 🏆 ⚡ ⏱️ 🐈
* [x] 🏆 🔥🔥🔥 **Zero Spatial Teleportation, 10x-30x Burn Warps, 3.6kx Deep Space Green Safe Speed, 50/50 Button Symmetry & Persistent Guidance Indicator (v2.1.8):** Eliminated coordinate jump during TLI auto-alignment. Permitted time warps up to 30x during burns. Expanded Tier 1 Green safe warp speed to 3.6kx beyond Geosync. Formatted top navigation buttons into symmetric 2x2 grid. Persistent `#burn-guidance-indicator`. 🏆 ⚡ ⏱️ 🐈
* [x] 🏆 🔥🔥🔥 **Flight Timers & Gated Auto-Warp / Checkpoint Alignment (v2.1.7):** Centralized operational timers into `FLIGHT_TIMERS` on `window.FLIGHT_TIMERS`. Inhibited Auto-Warp when approaching burns, during active alignment, and during 10-second post-burn hold. Fast-track auto-align countdown (10s) with blinking button. 🏆 ⚡ ⏱️ 🐈
* [x] 🏆 🔥🔥🔥 **Dev Viewport Fix & 100% Offline Asset Suite (v2.1.6):** Resolved `isReentry` reference error. Ingested local offline copies of `three.min.js`, `earth-blue-marble.jpg`, and `moon_1024.jpg` with CDN fallback. Built `start_dev_server.bat` and updated `server.py --dev`. 🏆 🥽 ⚡ 🐈
* [x] 🏆 🔥🔥🔥 **Dev/Public Sandbox Segregation & LKG Hardware Snapshots (v2.1.5):** Kept public root `index.html` pristine, initialized `snapshots/` archive with Last Known Good hardware profiles (Quest 3 WebXR, Desktop, Mobile), and isolated festival transmutations in `dev/index.html`. 🏆 🥽 📦 🐈
* [x] 🏆 🔥🔥🔥 **Auto Warp Engine & 3-Tier Safety Gradient (v2.1.5):** Added Auto Warp toggle (default ON) beside Track Target. Implemented dynamic 3-tier safety coloring (Green Safe, Solid Yellow Advisory, Red Extreme Confirm). Auto Warp and Skip to Action clamp strictly to maximum Green safe speed for active gravity well. 🏆 ⚡ 🟢 🟡 🔴 🐈
* [x] 🏆 🔥🔥🔥 **Automated Atmospheric Re-Entry Guidance (v2.1.5):** When in re-entry (<122km), autopilot commands attitude vectoring via offset CoG gimbal / roll trim. Autopilot pulses blue glow and Bank Up/Down buttons illuminate dynamically when actuated. 🏆 🌊 🛰️ 🐈
* [x] 🏆 🔥🔥🔥 **Press-and-Hold Bank Controls & Visual Attitude Gauge (v2.1.5):** Replaced rapid clicking with continuous pointer-hold attitude adjustment. Added tri-color visual gauge above bank buttons showing live attitude, optimal corridor, and autopilot targets. 🏆 🎯 🎮 🥽 🐈
* [x] 🏆 🔥🔥🔥 **FilmFreeway Public Project Link & KremFest XR 2026 Submission (v2.1.3):** Linked public FilmFreeway project portal, Larry James creator profile, KremFest XR festival page, Director's Cut overview, Director Biography and Statement in README.md, verified 100% waiver code for KremFest XR 2026 submission, and synchronized devlogs without codebase modifications. 🏆 🌕 🎬 🥽 🐈
* [x] 🏆 🔥🔥🔥 **Retrospective Federated Memory Ingestion:** Crystallized 4 foundational concepts (`newtonian_velocity_verlet_orbital_engine`, `aerodynamic_reentry_corridor_and_lift_vectoring`, `openspace_microlauncher_citizen_science_architecture`, `indiedev_educational_space_outreach_framework`) into `C:/AI/memory/concepts/*.md` and verified D3 memory graph linking. 🏆 🐈
* [x] 🛠️ 🔥🔥🔥 **Alignment Ritual:** Standardize documentation and substrate to official Symbiot Alchemical standards. 🏆 🐈
* [ ] 🏗️ 🔥 **Documentation:** Update root README.md to reflect Symbiot integration. 🐈

## 🧠 Human-in-the-Loop (HITL)
* [ ] 🧠 🔥 **QA: Quadrant Layout**: Refactored the core HUD UI layout architecture into geometric corner Quadrants. 🧪
* [ ] 🧠 🔥 **QA: Mobile View**: Fixed native CSS Grid proportions. 🧪

## 🛠️ Current Work
* [ ] 🏗️ 🔥🔥🔥 **Physics: True TLI Targeting Engine**: Replace artificial MISSION_LEAD_ANGLE with realistic TLI parameters. 🛠️
* [ ] 🏗️ 🔥🔥🔥 **Artemis II Telemetry**: Implement data-mapping from NASA AROW/OEM files. 🛠️
* [ ] 🏗️ 🔥🔥 **UI: Mobile XR UX Overhaul**: Rebuild the XR HUD to be fully interactive within the headset natively. 🛠️

## 🚀 Mission Roadmap
* [ ] 📇 🌐 🔥🔥🔥 **Seattle Space Week Showcase Portal & Digital Contact Link**: Deploy lightweight public landing page (`wulfdesign.github.io/lunar-flyby-xr/`) with 1-click `[ 🚀 Launch Mission in Browser ]` button and digital business card / vCard download (`wulfdesign.github.io/card/`) with scannable QR code for live demonstration and networking during Seattle Space Week social mixers, presenting the simulation as an unassailable proof of real-time WebXR orbital mechanics.
* [ ] 🧩 🎮 🔥🔥🔥 **Modular Plugin Format & Mission Pack Architecture (Dev Roadmap)**: Decouple the core Three.js / WebXR physics engine from mission scenario data via a lightweight Plugin API (`registerMissionPack()`). Keep *Artemis: The Free Return* circum-lunar trajectory 100% free on GitHub Pages as the flagship experience. Enable modular loading of expandable mission scenarios:
  - **Pack 01 (Apollo 11 Historical Descent & Touchdown):** Low lunar orbit descent, landing radar, and manual RCS hover over boulder fields.
  - **Pack 02 (Mars Transit & Aerobraking Corridor):** High-velocity interplanetary cruise and atmospheric skip capture.
  - **Pack 03 (Lunar Gateway Rendezvous & NRHO Docking):** Near-Rectilinear Halo Orbit approach, station-keeping, relative velocity matching, and docking physics.
  - **Pack 04 (Cislunar Orbit Sandbox & Mission Planner):** Custom delta-v burn planner and orbital vector plotter.
* [ ] 💻 📦 🔥🔥 **Lightweight Standalone Desktop Application Wrapper (Tauri)**: Package the WebXR simulation into an ultra-compact (<15MB) standalone Windows `.exe` using Tauri (Rust + OS WebView2), avoiding heavy 150MB+ Electron overhead, featuring uncompressed 8K textures, offline 120fps PCVR mode, and built-in mission editor.
* [ ] 🌌 🎪 🔥🔥🔥 **Seattle Space Week (SEA) Preparation**: Festival & exhibition curation for upcoming Space Week in Seattle. Finalize kiosk/booth turnkey hardware configuration, Meta Quest 3 standalone & tethered profiles, visitor QR flow, and presentation collateral.
* [ ] ✨ 🗺️ 🔥🔥🔥 **Celestial Starfield Integration (PolyZone Real Stars)**: Ingest the real astronomical star catalog from `projects/poly-zone` (Hipparcos/Yale Bright Star coordinates and magnitudes) to replace procedural/random star points with scientifically accurate constellations and Milky Way celestial alignment.
* [ ] 🌕 📐 🔥🔥🔥 **Lunar Tidal Locking & Surface Orientation**: Correct the Moon's axial rotation and initial orientation to accurately model 1:1 tidal locking with Earth. Ensure the lunar nearside (Mare Tranquillitatis, Oceanus Procellarum) permanently faces Earth, while the heavily cratered farside correctly greets the spacecraft during the circum-lunar free-return perilune pass.
* [ ] 📚 🌊 **Educational Physics FAQ & Splashdown Hydrodynamics Guide**: Add deep-dive educational FAQ on ocean water impact (20.1 mph / 9 m/s), 12–15G couch attenuation struts, and circum-lunar free-return orbital loops.
* [ ] 🏗️ 🔥🔥 **Simulation: Re-Entry Heating**: Implement plasma blackout and drag interaction.
* [ ] 🏗️ 🔥 **Simulation: Splashdown Sequence**: Add lifting-entry bank controls and chutes.

## 🧹 Ecosystem Maintenance
* [ ] ⚡ 🔥 **Session Wrap-up**: Update docs/chatHandOff.md and devlog.md. 🐈
* [ ] 🏺 🔥 **Versioning Protocol**: Perform minor version increments on every session. 🐈

---

## 🏆 COMPLETED
* [x] 🏆 **Baseline v2.0**: Core simulation, warp gears, and cinematic capture system.
* [x] 🏆 **Infrastructure**: Folder reorganization, LFS initialization, and GitHub publication.
* [x] 🏆 **Telemetry**: Research into NASA AROW/OEM formats documented.
