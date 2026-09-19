# 📋 Tasks & Upgrades - Lunar Flyby XR

**⚠️ CRITICAL INSTRUCTION FOR AI AGENTS ⚠️**
DO NOT mark any task as done (🏆 or [x]) until the Human-in-the-Loop (Magus Wulf) has explicitly verified the output. Move finished tasks to 🧪 (Ready for QA) first. Use your Attribution Mark (🐈/🦞).

## 📖 Legend
* **Priority:** 🔥🔥🔥 (Critical) | 🔥🔥 (High) | 🔥 (Medium) | 🧊 (Cold/Icebox)
* **Model Routing:** 🏗️ (Architect) | ⚡ (Runner) | 🎭 (Local)
* **Status:** 🛠️ (In Progress) | 🧪 (Ready for QA) | 🧠 (HITL Action Needed) | 🩹 (Tech Debt) | 🏆 (Verified/Done)
* **Attribution:** 🐈 (Hermes) | 🦞 (MugWort)

**Version:** v2.1.7 (Flight Timers & Gated Auto-Warp / Checkpoint Alignment 🚀🌕⏱️🥽✨)

---

## 🧪 Waiting for QA (Ready for QA 🧪)
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
