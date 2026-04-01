# 🚀 New Chat Instructions: Lunar Flyby XR

## **Context**
This is a high-fidelity WebXR orbital mechanics sandbox titled **"Artemis: The Free Return."** It is timed for the **Artemis II** launch on April 1, 2026. The project has been reconstructed from rescued logs and is now stable at **v1.9.1**.

## **Current State (2026-03-31 23:55)**
- **Stable Commit:** `2779de5` (includes refined cinematic capture v1.0, auto-tracking, and milestone alerts).
- **Broken Attempt:** An attempt to add Phase 5 refinements (7.2kx warp, gear shifting, ETAs) resulted in physics instability and was rolled back. **Do not re-implement Phase 5 without solving the physics step jitter at high warp.**

## **Project Structure**
- `index.html`: The primary simulation file. Self-contained and supports standalone execution (double-click).
- `Tasks.md`: Main roadmap and priority list.
- `devlog.md`: Chronological history of development.
- `COMPLETED.md`: Archive of finished tasks.
- `docs/`: Supplemental documentation (Social Media, Video Scripts, Credits, Artemis/dearMoon research).
- `start_lunar_flyby.bat`: Dev server script (npx serve) on **Port 3550**.

## **Technical Stack**
- **Engine:** Three.js (r128).
- **Physics:** Custom Velocity Verlet integration (km/kg/s units).
- **UI:** Vanilla HTML5/CSS3 HUD.
- **VR:** WebXR Device API.

## **Immediate Objectives (Roadmap)**
1.  **🔥 FIX LUNAR SOI WARP STOP (Critical):** The simulation resets warp or "stops" when entering the Moon's Sphere of Influence.
2.  **Troubleshoot Phase 5 Refinements:**
    - Fix the `formatTime` ReferenceError (ensure it is defined at the top of the script).
    - Solve "Ship flying off" bug: Likely caused by high warp (7.2kx) and large `dt_step` in the physics loop.
    - Fix "One item flight log": The log array was clearing or failing to push correctly during Phase 5.
3.  **Consolidated HUD:** Merge Environment and Telemetry panels.

## **Instructions for Gemini**
- Follow the "Research -> Strategy -> Execution" workflow.
- Always update `Tasks.md` and `devlog.md` after changes.
- Append new devlog entries to the top, below header instructions.
- Mark completed tasks with 🧪 for QA first, then 🏆 once verified.
- **STRICT MANDATE:** Do not reference the `/private` folder or its contents in public-facing files or commits.
- **STRICT MANDATE:** NEVER push to public GitHub until the user has verified changes locally.
