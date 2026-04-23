# 📋 Tasks & Upgrades

> **Legend:**
> 🔥🔥🔥 (Critical) | 🔥🔥 (High) | 🔥 (Medium) | 🧊 (Cold/Icebox)
> ❄️ (Frozen) | ❄️❄️ (Deep Freeze) | ❄️❄️❄️ (Cryogenic)
> 🛠️ (In Progress) | 🧪 (Ready for QA) | 🐛 (UX Bugs & Polish) | 🩹 (Tech Debt) | 🏆 (Verified/Done)

---

## 🩹 Tech Debt & Documentation
- [x] 🏆 **Repo: Directory Cleanup**: Moved redundant `index_v*.html` versions from root to `/archive` or `/debug`.
- [ ] 🩹 **Repo: Version Audit**: Double-check version numbers in `index.html` commits and the initial commit metadata (time/date) to ensure accuracy; resolve the accidental "v2.0" jump in the commit history for chronological clarity.
- [ ] 🩹 **Docs: Search for Missing Sprint**: Investigate suspected Gemini WebUI save failure to recover the original chat logs for the final "Landing Sprint" (v1.9.8.10 / v1.9.9.1).
- [ ] 🩹 **Docs: Link Validation**: Fix broken links in `README.md` and `docs/` after directory reorganization.
- [ ] 🩹 **Docs: Recover Stripped Comments**: Extract educational documentation from `index_Rescue_V04.html` and move to `index_html.md` or re-weave into code using context-efficient markers.
- [ ] 🐛 **UI: Mobile View (Portrait & Landscape)**: Fix native responsive mobile layout sizing and CSS Grid limits. Wait for UI overhaul or apply proportional scaling. Current workaround requires "Desktop Site" enabled on mobile.
- [ ] 🛠️ **UI: Mission Settings Panel**: Build a panel to toggle "Auto-MCC", "Auto-Warp Deceleration", and "Auto-Warp to Recommended" speed settings.

## 🛠️ Current Work
- [ ] 🔥🔥🔥 **Media: Quest 3s Offload**: Offload 4K screenshots and flight video from the Quest 3s validation flight.
- [ ] 🔥🔥🔥 **Media: Stitch & Edit**: Edit and stitch the final mission video for promotional use.
- [ ] 🛠️ **Media: Update README Visuals**: Insert the Quest 3s screenshots and stitched video into the README XR section once offloaded.
- [ ] 🛠️ **Docs: Mobile XR Instructions**: Write detailed step-by-step setup instructions for the Mobile XR / Quest 3s section in the README (explaining how to set up the floating browser window workaround).
- [ ] 🛠️ **UI: Mobile XR UX Overhaul**: Rebuild the XR HUD to be fully interactive within the headset natively, removing the need for a separate floating browser window to operate the flyby (V2.0 priority).
- [ ] 🔥🔥🔥 **Physics: True TLI Targeting Engine**: Replace artificial `MISSION_LEAD_ANGLE` moon-moving cheat with realistic TLI parameters (ejection angle, transit time) to calculate leading-edge interception of a naturally orbiting Moon.
- [ ] 🔥🔥🔥 **Artemis II Telemetry**: Implement data-mapping from NASA AROW/OEM files into the simulation mission profile.
- [ ] 🔥🔥🔥 **HUD: Visual Trajectory Indicator**: Show "On Target" / "Off Course" status based on real-time physics projection.
- [ ] 🛠️ **UI: Mission Settings Panel**: Build a panel to toggle "Auto-MCC", "Auto-Warp Deceleration", and sensitivity settings.

## 🐛 UX & Polish (Debrief Feedback)
- [ ] 🐛 **UX: Smooth Warp Deceleration**: Transition warp down to 1x incrementally with visual feedback instead of a hard snap.
- [ ] 🐛 **UX: MCC Countdown & Execution UI**: Approach waypoints should auto-trigger sequential warp gear-downs to 1x before flashing the Execute calculate prompt.
- [ ] 🐛 **UI/UX: Warp Text Overflow**: Fix bug where text pushes the UI off-screen. Need responsive layout or CSS constraint.
- [ ] 🐛 **UX: Explicit Log Entry Feedback**: Add visual confirmation/HUD toast when a user manually clicks the 1x button to trigger a flight log save.
- [ ] 🐛 **UX: Dynamic Safe-Warp Button Colors**: Illuminate Warp buttons Green (safe) or Red (unsafe bounds) dynamically based on distance limits. Fix Red-Active button text contrast.
- [ ] 🐛 **UX: Flashing Buttons on Slowdown**: The notification buttons during forced deceleration or checkpoint arrivals should visually flash to grab user attention.
- [ ] 🐛 **UX: Mobile Landscape/Portrait Scaling**: Overhaul CSS to dynamically scale `zoom` or Transform percentages to keep HUD proportional on orientation flips. Move VR buttons back to bottom but with a negative z-index offset.
- [ ] 🐛 **UX/3D: Disappearing Crosshairs**: Fix the bug where the 3D Prograde vector ring disappears/clips into the Earth when altitude drops below 100km due to its -15 Z-depth rendering scale.
- [ ] 🐛 **UX: Early Checkpoint Warnings (Pre-Arrival)**: Trigger checkpoint warnings *earlier* in the approach trajectory to give the user time to execute MCC maneuvers safely.
- [ ] 🐛 **UX: Warp-Adjusted ETA Countdown**: Implement a HUD countdown timer that displays the ETA to the next node in real-time seconds dynamically adjusted by the current warp gear.
- [ ] 🐛 **UI: Help Popup Toggle**: Add a hotkey/button to toggle the visibility of the informational help popups on screen.
- [ ] 🐛 **Documentation: Flesh out Credits Links**: Hyperlink the remaining organizations, individuals, and inspirations across the README and legacy credits (e.g., MicroLaunchers, Armadillo Aerospace, etc.).
- [x] 🏆 **UI: WebXR Button Z-Index & Centering**: Fixed the default WebXR "Enter VR" and "Reset View" buttons rendering order and restored them to the bottom center, properly adjusting their widths safely behind panels on mobile.
- [x] 🏆 **UI: FOV Indicator Size**: Increased the FOV tracking text size by 120% per A/B playtest feedback.

## 🔥🔥 End-of-Mission Flow (Re-Entry & Splashdown)
- [ ] 🔥🔥 **UI/HUD: Phase Checklist Updates**: Add "Loss of Signal (LOS) Warning", "Cislunar Return", "Re-entry Prep". 
- [ ] 🔥🔥 **UX: Comms Radio UI**: Add a dedicated scrolling log box for CAPCOM radio instructions and ground-control readouts, logging them to the json output.
- [x] 🏆 **Simulation: Re-Entry Heating & Plasma Blackout**: Implemented visual indicators and a comms blackout period as altitude drops below 120km.
- [x] 🏆 **Mechanics: Atmospheric Drag**: Programmed velocity bleed-off (`F_drag`) interacting with `updatePhysics` once `altE < 122km`, allowing the ship to aerodynamically slow down.
- [x] 🏆 **Mechanics: Splashdown Sequence**: Added lifting-entry bank controls, interpolated drogue/main chutes, and structural survivability checks.
- [ ] 🔥🔥 **Mechanics: Earth-Return Waypoints**: Duplicate the Mission Waypoint script to track distance *decreasing* for inbound flights, triggering the same auto-warp slowdowns and MCC checks.
- [ ] 🔥🔥 **Simulation: Splashdown Geolocation Tracking**: Calculate geographic latitude/longitude impact coordinates by syncing the final Cartesian position vector with a rotating Earth texture base based on Mission Elapsed Time.

## 🧪 Ready for QA (Waiting for User Confirmation)
- [ ] 🧪 **Physics: Vector Corruption Hotfix (v1.9.8.5)**: Fixed integration bug where `_totalAccel` was overwriting base gravity instead of copying it, causing the "crazy numbers" and black screen failures.
- [ ] 🧪 **Physics: Trajectory Keyhole Restoration**: Reverted `MISSION_LEAD_ANGLE` to 0.74 to restore the proven Free-Return slingshot timing.
- [ ] 🧪 **Physics: NaN Crash Hotfix (v1.9.8.4)**: Clamped dot-product inputs for `Math.asin` to prevent physics explosions and "black screen" rendering failures.
- [ ] 🧪 **Avionics: Advanced MCC Logging**: Course corrections now log specific heading, velocity, altitude, and fuel-mass-lost data to the flight log.
- [ ] 🧪 **Avionics: Auto-MCC self-correction**: Ship now displays a 45s countdown and automatically executes alignment if at 1x speed; button text dynamically updates with timer.
- [ ] 🧪 **UX: Enhanced Button States**: Implemented specific hover states for Safe (Green) and Danger (Red) buttons with black text contrast.
- [ ] 🧪 **Avionics: Radial MCC Calibration (v1.9.8.3)**: Replaced overpowering tangential boost with a 0.02 km/s radial impulse to accurately target 40km perigee.
- [ ] 🧪 **Mechanics: Fuel-Consuming MCC**: Integrated rocket equation math into mid-course corrections; MCC burns now physically deplete the fuel tank.
- [ ] 🧪 **UX: Dangerous Warp Pulse**: Added aggressive red-flashing animation for `.active.danger-btn` states to warn users of high-speed risks.
- [ ] 🧪 **UI: HUD Stability Hotfix**: Fixed Navigation button jitter by wrapping MCC controls in a fixed-height container with `visibility` toggling.
- [ ] 🧪 **UX/3D: Prograde Crosshair Clipping**: Optimized `renderScale` to 0.1 and pulled `progradeMesh` to Z: -3, ensuring it stays 9.2 units above the Earth's surface even at 122km re-entry interface.
- [ ] 🧪 **UI/3D: Fix Black Screen Bug**: Scaled down the ship's interior `cockpit` mesh to 0.005 units (inside the camera near-plane) to restore the "invisible frame" behavior and fix the blank screen issue reported during V1.9.8 integration.

## 🔥🔥🔥 High Priority (Ready to Forge)
- [ ] 🔥🔥🔥 **Controls: Manual Thrust Vectoring**: Allow user to adjust burn direction (currently locked to prograde) for mid-course corrections.
- [ ] 🔥🔥🔥 **VR: Controller Troubleshooting**: Investigate why controllers might not be appearing in WebXR; add check for `select` events.
- [ ] 🔥🔥🔥 **Artemis II: State Vector Interpolation**: Create the linear/cubic spline interpolation engine for 10-minute samples.

## 🔥🔥 V2.0 Mission Goals & Architecture
- [ ] 🔥🔥 **Education: In-Game Glossary & Dictionary**: Build an interactive terminology dictionary (e.g., Perilune, Prograde, Vis-viva) with local tooltips and links out to Wikipedia for deeper learning.
- [ ] 🔥🔥 **Environment: Orbital Traffic Checkpoints**: Add altitude markers/indicators for passing real-world orbital bands (ISS/LEO, Starlink, GPS, Geostationary Satellites). Include visual "telescope/starboard window" flybys as ambient flavor.
- [ ] 🔥🔥 **Mechanics: Emergency Flight Computer Override (Auto-Fly)**: If trajectory deviation is critical or checkpoints are missed, flash red, drop warp to 1x, and announce an emergency computer take-over. The system automatically calculates a safe return trajectory unless explicitly cancelled by the user.
- [ ] 🔥🔥 **UI: Mission Control CAPCOM Feed**: Add a "CAPCOM" side panel to display scrolling text messages for progress, warnings, and checkpoint approaches sequentially as radio comms.
- [ ] 🔥🔥 **Physics: Lunar Orbit Insertion (LOI)**: Transition beyond Free-Return trajectories to calculate decel burns for stable lunar captures.
- [ ] 🔥🔥 **Avionics: Flight Computer UI**: Build a targeting console to read current state vectors and calculate maneuver nodes (intercepts, rendezvous, MCCs).
- [ ] 🔥🔥 **Physics: Sun Gravity Integration**: Add solar mass to N-body calculation for v2.1 "Gold Master" accuracy.
- [ ] 🔥🔥 **Architecture: Modular Source Files**: Prepare project for split into `styles.css`, `physics.js`, and `ui.js` while maintaining single-file build.
- [ ] 🔥🔥 **Artemis II Real-Time Replay**: Load and play back the actual mission state-vectors from NASA data.
- [ ] 🔥🔥 **Mechanic**: Service Module Jettison (Release ESM mass at 2000km to stabilize heatshield before Entry Interface).


## 🧊 Icebox (Cold)
- [ ] 🧊 **Mechanic**: Dragon-style Powered Landing (Fire retros, discard chutes, zero-velocity touchdown).
- [ ] 🧊 **Restore Load Flight Log**: Re-enable log playback once stability issues are resolved.
- [ ] 🧊 **Refine Auto Camera Tracking**: Automated pans currently disabled.
## 🧪 Waiting for QA
- [/] 🧪 **UI/UX Layout: Quadrant Expansion Bugfix**: Completely decoupled CSS rigid flex rows and rebuilt HUD wrapper to absolute Quadrants. Bottom-Right Navigation panel now correctly consumes empty Top-Right space dynamically on squashed non-maximized viewports instead of cutting off behind taskbars. Awaiting tests on Tablet, Mobile, and Quest.

## 🏆 Completed Ready to Archive
- [x] 🪂 **Docs: Restore Educational Wiki Mechanics**: Transitioned the raw physics constraints (Orbital Velocity, Gimbaling, Reefing) into a dedicated `docs/physics.html` live wiki, mapping explicit anchor URLs down into the `index.html` integration loop.
- [x] 🏆 **UI/Simulation: AI Syntax Corruption Hotfix**: Sliced off duplicated HTML closing tags and restored the `mccAutoCountdown` global variable to prevent a fatal ReferenceError from killing the animation loop.
- [x] 🏆 **XR: Standalone Headset Verification**: Successfully hand-patched WebXR bindings and completed a flawless end-to-end flight test in the native Meta Quest 3s browser before the Art Show.
- [x] 🏆 **Mechanics: Atmospheric Drag & Parachutes**: Implemented exponential density drag math and multi-stage chute deployment (Drogues @ 7.3km, Mains @ 3km).
- [x] 🏆 **Mechanics: Splashdown State Machine**: Added mission success/failure logic based on 15m/s impact velocity threshold and 15G structural limit.
- [x] 🏆 **Mechanics: Lifting Entry Physics**: Integrated capsule roll/lift (L/D ~0.25) allowing for manual trajectory steering during reentry.
- [x] 🏆 **Physics: Vector Corruption Hotfix (v1.9.8.5)**: Fixed integration bug where `_totalAccel` was overwriting base gravity instead of copying it, causing the "crazy numbers" and black screen failures.
- [x] 🏆 **Physics: Trajectory Keyhole Restoration**: Reverted `MISSION_LEAD_ANGLE` to 0.74 to restore the proven Free-Return slingshot timing.
- [x] 🏆 **Avionics: Waypoint MCC Autopilot**: Implemented Mid-Course Correction distance triggers and prototype Delta-V execution frame. (Verified 2026-04-07)
...
- [x] 🏆 **Burn Precision Logging**: Added `target_burn_s` and `actual_burn_s` to logs. (Verified 2026-04-01)
- [x] 🏆 **UI Stability & Crash Prevention**: Implemented `safeSetText` and `try...catch` in the main loop to resolve "Cannot set properties of null" errors. (Verified 2026-04-06)
- [x] 🏆 **Log Folder Organization**: Established `/logs` directory. (Verified 2026-04-01)
- [x] 🏆 **Track Target Working**: Verified manual and auto tracking. (Verified 2026-04-01)
- [x] 🏆 **Detailed Log Naming**: Log files now save with full ISO timestamp. (Verified 2026-04-01)
- [x] 🏆 **Warp Button Upgrades**: Added **30x** and **7.2kx** buttons. (Verified 2026-04-01)
- [x] 🏆 **Camera Inversion Bug:** Fixed `shipGroup.lookAt` vector subtraction to properly align the camera facing forward along the velocity path instead of backwards.
