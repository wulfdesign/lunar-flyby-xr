# 📋 Tasks & Upgrades - Lunar Flyby XR

**⚠️ CRITICAL INSTRUCTION FOR AI AGENTS ⚠️**
DO NOT mark any task as done (🏆 or [x]) until the Human-in-the-Loop (Magus Wulf) has explicitly verified the output. Move finished tasks to 🧪 (Ready for QA) first. Use your Attribution Mark (🐈/🦞).

## 📖 Legend
* **Priority:** 🔥🔥🔥 (Critical) | 🔥🔥 (High) | 🔥 (Medium) | 🧊 (Cold/Icebox)
* **Model Routing:** 🏗️ (Architect) | ⚡ (Runner) | 🎭 (Local)
* **Status:** 🛠️ (In Progress) | 🧪 (Ready for QA) | 🧠 (HITL Action Needed) | 🩹 (Tech Debt) | 🏆 (Verified/Done)
* **Attribution:** 🐈 (Hermes) | 🦞 (MugWort)

**Version:** v2.1.11 (Universal Smooth Time Warp Stepping Protocol & WebXR Kinetosis Prevention 🚀🌕⏱️🥽✨)

---

## 🧪 Waiting for QA (Ready for QA 🧪)
* [ ] 🧪 🔥🔥🔥 **Universal Smooth Time Warp Stepping Protocol & WebXR Kinetosis Prevention (v2.1.11):** Diagnosed and eliminated abrupt 1-frame time warp jumps down to 1x following engine burn cutoff (MECO) and post-burn observation holds. Removed direct `updateWarpUI()` invocations across all runtime flight events (`MECO`, `isPostBurnHold`, `evaluateMCC`, TLI approach slowdown, and entry interface clamps), establishing `updateWarpStepping()` as the sole runtime gear-shifter with an enforced 1.0s dwell per intermediate gear tier (30x -> 10x -> 1x). Implemented `.target-warp` dashed visual outline indicator and progression HUD readout (`30x [>> 1x]`). Guarded Auto-Warp engine to prevent fighting active downshifts (`timeWarp <= targetWarp`). Crystallized the universal hard rule into Symbiot Memory as `smooth_timewarp_transitions_and_vr_kinetosis_prevention.md` linked to `newtonian_velocity_verlet_orbital_engine.md`. 🧪 ⚡ ⏱️ 🥽 🐈
* [ ] 🧪 🔥🔥🔥 **30x Burn Warp Fix, 8s Countdown Hang Resolution, Outbound Progressive Acceleration & Finite Continuous MCC Burns (v2.1.10):** Fixed 30x warp in parking orbit and during burns by setting Tier 1 Green safety in LEO and relaxing the burn click guard to `w > 30`, allowing full switching between 1x, 10x, and 30x during burns. Resolved the auto-align countdown freezing at 8s by synchronizing MES state transitions to immediately clear `tliAutoCountdown` and dismiss `#btn-autopilot-mcc`. Healed outbound acceleration so the craft accelerates progressively out of Earth orbit (60x -> 300x -> 600x -> 1800x -> 3600x) rather than staying clamped to 10x. Replaced impulsive single-frame Mid-Course Correction (MCC) velocity jumps with continuous 3-4 second finite-duration burns integrating acceleration and fuel consumption smoothly via Velocity Verlet equations. 🧪 ⚡ ⏱️ 🐈
* [ ] 🧪 🔥🔥🔥 **Startup Blink Signals, Non-Restricted Burn Cruise, 10s Auto-Align, 1s Button Indicators & Stepped Lunar/Earth Warp Schedules (v2.1.9):** Added distinct 5-second startup blink animations for Autopilot (`blink-blue`) and Auto-Warp (`blink-green`) to visibly signal initialization. Spacecraft cruises smoothly into and through TLI burn at selected speeds up to 30x without being forced down to 1x (warp locked during active firing). Increased trajectory auto-alignment delay from 4s to 10s. Time warp buttons display active `.active` state for the full 1.0s interval during gear shifts. Integrated progressive 3-tier warp safety and Auto-Warp stepping schedules for both Lunar approach (3.6kx -> 1.8kx -> 600x -> 300x -> 10x-30x) and Earth return approach (3600x -> 1800x -> 600x -> 60x -> 30x -> 10x -> 1x) with failsafe clamps locking to 1x before Entry Interface (122 km). 🧪 ⚡ ⏱️ 🐈
* [ ] 🧪 🔥🔥🔥 **Zero Spatial Teleportation, 10x-30x Burn Warps, 3.6kx Deep Space Green Safe Speed, 50/50 Button Symmetry & Persistent Guidance Indicator (v2.1.8):** Eliminated unnatural spatial coordinate jump during TLI auto-alignment by stripping coordinate teleportation (`shipPos.set`/`shipVel.set`), allowing the craft to orbit and burn along its natural Newtonian velocity vector. Permitted time warps up to 30x during engine firings so burns complete smoothly in ~3.7s-11s without sitting through 111s real-time. Expanded Tier 1 Green safe warp speed to 3.6kx (`3600x`) beyond Geosync altitude (`altE > 36,300 km`) for rapid cislunar divide traversal while keeping 7.2kx disabled. Autopilot starts armed with a 5-second blue pulse (`pulse-blue-glow`) and Auto-Warp starts active with a 5-second green pulse (`flash-green`). Formatted top navigation buttons into a symmetric 2x2 grid (50/50 width per row). Restored persistent `#burn-guidance-indicator` above the manual burn override displaying live real-time flight computer countdowns, burn times, post-burn hold timers, checkpoint alerts, and re-entry guidance. 🧪 ⚡ ⏱️ 🐈
* [ ] 🧪 🔥🔥🔥 **Flight Timers & Gated Auto-Warp / Checkpoint Alignment (v2.1.7):** Centralized all operational timers into `FLIGHT_TIMERS` on `window.FLIGHT_TIMERS` (TLI slowdown, ignition window, manual vs auto alignment delays, post-burn hold, and gear shift intervals). Resolved speed fight during TLI approach and waypoint encounters by inhibiting Auto-Warp when approaching burns, during active alignment, and during the 10-second post-burn observation hold. Added fast-track auto-align countdown (4s vs 60s manual) with blinking `#btn-autopilot-mcc` button and automated trajectory alignment execution. 🧪 ⚡ ⏱️ 🐈
* [ ] 🧪 🔥🔥🔥 **Dev Viewport Fix & 100% Offline Asset Suite (v2.1.6):** Resolved `isReentry` global scoping reference error restoring WebGL render loop in `dev/index.html`. Ingested local offline copies of `three.min.js`, `earth-blue-marble.jpg`, and `moon_1024.jpg` with automatic CDN fallback. Created `start_dev_server.bat` and updated `server.py --dev` for dedicated zero-friction local sandbox launching. 🧪 🥽 ⚡ 🐈
* [ ] 🧪 🔥🔥🔥 **Dev/Public Sandbox Segregation & LKG Hardware Snapshots (v2.1.5):** Kept public root `index.html` pristine, initialized `snapshots/` archive with Last Known Good hardware profiles (Quest 3 WebXR, Desktop, Mobile), and isolated festival transmutations in `dev/index.html`. 🧪 🥽 📦 🐈
* [ ] 🧪 🔥🔥🔥 **Auto Warp Engine & 3-Tier Safety Gradient (v2.1.5):** Added Auto Warp toggle (default ON) beside Track Target. Implemented dynamic 3-tier safety coloring (Green Safe, Solid Yellow Advisory, Red Extreme Confirm). Auto Warp and Skip to Action clamp strictly to maximum Green safe speed for active gravity well. 🧪 ⚡ 🟢 🟡 🔴 🐈
* [ ] 🧪 🔥🔥🔥 **Automated Atmospheric Re-Entry Guidance (v2.1.5):** When in re-entry (<122km), autopilot commands attitude vectoring via offset CoG gimbal / roll trim. Autopilot pulses blue glow and Bank Up/Down buttons illuminate dynamically when actuated. 🧪 🌊 🛰️ 🐈
* [ ] 🧪 🔥🔥🔥 **Press-and-Hold Bank Controls & Visual Attitude Gauge (v2.1.5):** Replaced rapid clicking with continuous pointer-hold attitude adjustment. Added tri-color visual gauge above bank buttons showing live attitude, optimal corridor, and autopilot targets. 🧪 🎯 🎮 🥽 🐈
* [ ] 🧪 🔥🔥🔥 **FilmFreeway Public Project Link & KremFest XR 2026 Submission (v2.1.3):** Linked public FilmFreeway project portal, Larry James creator profile, KremFest XR festival page, Director's Cut overview, Director Biography and Statement in README.md, verified 100% waiver code for KremFest XR 2026 submission, and synchronized devlogs without codebase modifications. 🧪 🌕 🎬 🥽 🐈
* [ ] 🧪 🔥🔥🔥 **Retrospective Federated Memory Ingestion:** Crystallized 4 foundational concepts (`newtonian_velocity_verlet_orbital_engine`, `aerodynamic_reentry_corridor_and_lift_vectoring`, `openspace_microlauncher_citizen_science_architecture`, `indiedev_educational_space_outreach_framework`) into `C:/AI/memory/concepts/*.md` and verified D3 memory graph linking. 🧪 🐈
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
