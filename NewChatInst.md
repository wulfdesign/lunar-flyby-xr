# 🚀 New Chat Instructions: Lunar Flyby XR

## **Context**
This is a high-fidelity WebXR orbital mechanics sandbox titled **"Artemis: The Free Return."** It is timed for the **Artemis II** launch on April 1, 2026. The project has been reconstructed from rescued logs and is now stable at **v1.9.1**.

## **Current State (2026-04-01 01:00)**
- **STABLE BASELINE:** Both local and public GitHub repos have been rolled back to **Commit 3e4074a**. 
- **Rollback Reason:** Failed attempt to implement Phase 5 cinematic refinements (7.2kx warp, gear shifting) resulted in physics instability and blank screens.
- **index.html:** Now contains the clean v1.9.1 source code (No "CINEMATIC CAPTURE" button or automation logic).

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
2.  **Cinematic Capture Re-Implementation:** Start fresh using the parameters in `docs/videoShotScript.md` but ensure physics stability and proper function scoping.
3.  **Consolidated HUD:** Merge Environment and Telemetry panels.

## **Instructions for Gemini**
- Follow the "Research -> Strategy -> Execution" workflow.
- Always update `Tasks.md` and `devlog.md` after changes.
- Append new devlog entries to the top, below header instructions.
- Mark completed tasks with 🧪 for QA first, then 🏆 once verified.
- **STRICT MANDATE:** Do not reference the `/private` folder or its contents in public-facing files or commits.
- **STRICT MANDATE:** NEVER push to public GitHub until the user has verified changes locally.
