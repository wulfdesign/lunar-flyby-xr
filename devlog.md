# 🚀 Lunar Flyby XR - Devlog

## [2026-03-31 00:30] - Version 18: Session Conclusion & Final Polish
### 📝 Summary
Finalized the initial prototype session. The simulation is now a fully functional, educational WebXR experience.

### 🛠️ Work Done
- **Final CSS Cleanup**: Standardized crosshair styling and UI positioning.
- **Verification**: Confirmed all systems (physics, targeting, logging, warp) are operating within design parameters.
- **Repository Prepared**: This version serves as the base for the local git repository.

---

## [2026-03-31 00:15] - Version 17: "Final Regeneration" Recovery
### 📝 Summary
Duplicate of V1.9.1 generated during the "canvas glitch" recovery phase.
### 🛠️ Work Done
- Attempted to recover code after Gemini WebUI replaced the HTML canvas with a Markdown file.
- Verified that the "Final" version (V1.9.1) was successfully re-generated.

---

## [2026-03-31 00:00] - Version 16: Final Prototype (V1.9.1)
### 📝 Summary
Completed the final stable version of the Artemis Lunar Flyby prototype, consolidating all features and addressing the browser canvas glitch.

### 🛠️ Work Done
- **SOI State Latch**: Fixed the "warp reset" loop. The simulation now uses a state latch (`hasEnteredLunarSOI`) to ensure the automatic drop to 1x speed only happens once upon entering the Moon's gravity well.
- **HUD Consolidation**: Merged the Environment and Telemetry panels into a single, unified list on the left side of the screen.
- **Raycast Targeting Fix**: Specifically excluded the cockpit geometry from the raycaster to prevent the "Targeting: Cockpit" bug.
- **Physics Verification**: Confirmed fuel mass flow rates and Specific Impulse ($I_{sp}$) calculations for physical accuracy.
- **V2.0 Roadmap**: Embedded the future feature list into the code comments.

---

## [2026-03-30 23:45] - Version 15: Project Naming & Roadmap Integration
### 📝 Summary
Finalized project branding and integrated the development roadmap into the source.

### 🛠️ Work Done
- **Official Branding**: Renamed the project to "Artemis: Lunar Flyby VR - Educational Edition".
- **MECO Precision**: Refined the Main Engine Cutoff (MECO) calculations using orbital energy.
- **UI Tweaks**: Small adjustments to panel widths and font sizes.

---

## [2026-03-30 23:30] - Version 14: Internal Cleanup & Safety Checks
### 📝 Summary
Refined the codebase for better maintainability and error handling.

### 🛠️ Work Done
- Added null checks for all DOM elements (e.g., `warp-text`) to prevent crashes during rapid state resets.
- Validated physics constants against NASA reference data (muEarth, muMoon).

---

## [2026-03-30 23:15] - Version 13: Milestone Tracking & Environment Logic
### 📝 Summary
Added tracking for different orbital regions and mission milestones.

### 🛠️ Work Done
- **Space Environment Panel**: Created a HUD panel to track current region (LEO, MEO, GEO, Deep Space, Lunar SOI).
- **Phase Recalibration**: Adjusted the TMI lead angle to 47.5 degrees (0.83 rads) for a perfect 87-hour lunar intercept.
- **Moon Heading Indicator**: Added a visual degree-offset tracker to help users find the Moon.

---

## [2026-03-30 23:00] - Version 12: Advanced Warp & SOI Triggers
### 📝 Summary
Implemented high-speed time warping and automatic encounter handling.

### 🛠️ Work Done
- **3600x Warp**: Added 1-hour-per-second time compression.
- **Automatic Warp Cutoff**: The simulation now drops to 1x speed automatically when entering the "Lunar Encounter" phase.

---

## [2026-03-30 22:45] - Version 11: G-Force & Educational Tooltips
### 📝 Summary
Enhanced the "Educational Sandbox" aspects of the simulation.

### 🛠️ Work Done
- **G-Force Meter**: Implemented real-time G-calculation ($F/m/9.81$).
- **Comprehensive Tooltips**: Added `title` attributes to all HUD elements explaining the underlying physics (Vis-viva, Kepler's Laws).
- **Visual FOV Indicator**: Added a centered zoom-level readout.

---

## [2026-03-30 22:30] - Version 10: Targeting & Raycasting
### 📝 Summary
Implemented interactive scanning of celestial objects.

### 🛠️ Work Done
- **Raycast HUD**: Hovering the crosshair over Earth, Moon, or Sun displays a dynamic info popup.
- **Scroll Zoom**: Added mouse-wheel FOV adjustment (10° to 100°).
- **Prograde Marker**: Added a 3D ring in the scene representing the velocity vector.

---

## [2026-03-30 22:15] - Version 9: Autopilot Latch & Burn Diagnostics
### 📝 Summary
Improved autopilot reliability and burn feedback.

### 🛠️ Work Done
- **Autopilot "Latch"**: Once a burn starts, it stays on until energy requirements are met, ignoring minor timing drifts.
- **Burn Diagnostics**: Added "Target Burn" vs "Actual Burn" counters with color-coded flashing (Red/Yellow/Green).
- **Flight Data Logging**: Created a JSON exporter for mission telemetry.

---

## [2026-03-30 22:00] - Version 8: Initialization & Stability Fixes
### 📝 Summary
Fixed critical startup bugs.

### 🛠️ Work Done
- **TypeError Fix**: Resolved `reading 'isTliCoast'` crash by ensuring at least one physics step runs before UI rendering.

---

## [2026-03-30 21:45] - Version 7: Precision Launch Conditions
### 📝 Summary
Optimized the starting state for the "Free Return" trajectory.

### 🛠️ Work Done
- **T-2:00 Start**: The simulation now starts exactly 2 minutes before the optimal TMI window.
- **Full Moon Lighting**: Positioned the Sun to create a dramatic, illuminated Moon view at launch.
- **Autopilot Prompt**: Added a flashing yellow button when the window is close.

---

## [2026-03-30 21:30] - Version 6: Interactive Camera & Lighting
### 📝 Summary
Added mouse-look controls and improved scene lighting.

### 🛠️ Work Done
- **Mouse/Touch Pan**: Enabled looking around the cockpit while the ship maintains prograde orientation.
- **Ambient Light**: Increased ambient intensity to make "dark" sides of planets visible.
- **Sun Mesh**: Added a visual glowing sphere to represent the light source.

---

## [2026-03-30 21:00] - Version 5: Reset View & HUD Polish
### 📝 Summary
Refined user interaction and HUD transparency.

### 🛠️ Work Done
- **Reset View**: Added a button to re-center the camera.
- **Backdrop Blur**: Added CSS blur effects to HUD panels for a modern "glass" aesthetic.
- **Transparency Fix**: Lowered panel opacity to act as a true heads-up overlay.

---

## [2026-03-30 20:30] - Version 4: Educational HUD & LEO Stability
### 📝 Summary
Expanded UI information and fixed orbital decay.

### 🛠️ Work Done
- **Educational Resources**: Added a panel (initially visible, later hidden in comments) with NASA/Wikipedia links.
- **Phase Angle Math**: Implemented precise phase angle detection for TMI windowing.

---

## [2026-03-30 19:30] - Version 3: Velocity Verlet & Real Units
### 📝 Summary
A major physics engine rewrite for stability and accuracy.

### 🛠️ Work Done
- **Velocity Verlet**: Replaced Euler integration with a symplectic integrator to prevent orbital drift.
- **Real-world Units**: Switched from arbitrary scale to Kilometers, Kilograms, and Seconds.
- **Vis-viva Burn Cutoff**: Engines now cut off based on specific orbital energy rather than target velocity.

---

## [2026-03-30 18:30] - Version 2: WebGL Error Fix
### 📝 Summary
Fixed a critical loading error.

### 🛠️ Work Done
- **CDN Fix**: Removed dependency on an external `WebGL.js` script that was failing to load.

---

## [2026-03-30 18:00] - Version 1: Initial Prototype
### 📝 Summary
First functional Three.js scene.

### 🛠️ Work Done
- Basic Earth/Moon system with simple Euler physics.
- Crude HUD with altitude and velocity.
- Functional (though unstable) manual thrust.
