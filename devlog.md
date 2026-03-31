# 🚀 Lunar Flyby XR - Devlog

## [2026-03-30 22:00] - Version 7: Targeting & Itinerary HUD
### 📝 Summary
Added advanced navigation tools, flight logging, and interactive targeting features.

### 🛠️ Work Done
- **Raycast-powered Targeting**: Looking at Earth, Moon, or Sun now triggers a dynamic info popup showing distance and contextual mission hints.
- **Scroll Zooming**: Added ability to adjust FOV (10° to 100°) using the mouse scroll wheel, with a HUD indicator for zoom level.
- **Mission Itinerary HUD**: A new checklist panel tracks major mission milestones (TLI Burn, Coast, Flyby) with real-time ETA calculations.
- **3D Prograde Marker**: Added a green ring marker in the 3D scene that represents the ship's forward velocity vector.
- **Orbital Energy Targeting**: Switched the TMI cutoff logic to use **Specific Orbital Energy**. This is more accurate than simple velocity as it accounts for altitude changes during long burns.
- **Flight Data Logging**: Implemented a "SAVE FLIGHT LOG" feature that exports mission telemetry (Altitude, Velocity, Events) to a JSON file for analysis.
- **Physics Polish**: Implemented realistic mass flow rates based on thrust and $I_{sp}$ (exhaust velocity).

---

## [2026-03-30 21:30] - Version 6: Precision Launch & Autopilot Cues
### 📝 Summary
Refined the starting conditions for better "gameplay" flow and added visual cues for the burn window.

### 🛠️ Work Done
...
