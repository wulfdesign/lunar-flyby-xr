# 📋 Tasks & Upgrades

> **Legend:**
> 🔥🔥🔥 (Critical) | 🔥🔥 (High) | 🔥 (Medium) | 🧊 (Cold/Icebox)
> ❄️ (Frozen) | ❄️❄️ (Deep Freeze) | ❄️❄️❄️ (Cryogenic)
> 🛠️ (In Progress) | 🧪 (Ready for QA) | 🐛 (UX Bugs & Polish) | 🩹 (Tech Debt) | 🏆 (Verified/Done)

---

## 🛠️ Current Work
- [ ] 🔥🔥🔥 **Physics: True TLI Targeting Engine**: Replace artificial `MISSION_LEAD_ANGLE` moon-moving cheat with realistic TLI parameters (ejection angle, transit time) to calculate leading-edge interception of a naturally orbiting Moon.
- [ ] 🔥🔥🔥 **Artemis II Telemetry**: Implement data-mapping from NASA AROW/OEM files into the simulation mission profile.
- [ ] 🔥🔥🔥 **HUD: Visual Trajectory Indicator**: Show "On Target" / "Off Course" status based on real-time physics projection.

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
- [ ] 🔥🔥 **Simulation: Re-Entry Heating & Plasma Blackout**: Implement visual indicators and a comms blackout period as altitude drops below 120km.
- [ ] 🔥🔥 **Mechanics: Atmospheric Drag**: Program velocity bleed-off (`F_drag`) interacting with `updatePhysics` once `altE < 100km`, allowing the ship to aerodynamically slow down before impact.
- [ ] 🔥🔥 **Mechanics: Splashdown Sequence**: Add retro-fire targeting, heat shield orientation requirement, drogue chute deployment, and main chute splashdown restrictions interacting with the aerodynamic load.
- [ ] 🔥🔥 **Mechanics: Earth-Return Waypoints**: Duplicate the Mission Waypoint script to track distance *decreasing* for inbound flights, triggering the same auto-warp slowdowns and MCC checks.
- [ ] 🔥🔥 **Simulation: Splashdown Geolocation Tracking**: Calculate geographic latitude/longitude impact coordinates by syncing the final Cartesian position vector with a rotating Earth texture base based on Mission Elapsed Time.

## 🧪 Ready for QA (Waiting for User Confirmation)
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

## 🏆 Completed Ready to Archive
- [x] 🏆 **Avionics: Waypoint MCC Autopilot**: Implemented Mid-Course Correction distance triggers and prototype Delta-V execution frame. (Verified 2026-04-07)
- [x] 🏆 **Burn Precision Logging**: Added `target_burn_s` and `actual_burn_s` to logs. (Verified 2026-04-01)
- [x] 🏆 **UI Stability & Crash Prevention**: Implemented `safeSetText` and `try...catch` in the main loop to resolve "Cannot set properties of null" errors. (Verified 2026-04-06)
- [x] 🏆 **Log Folder Organization**: Established `/logs` directory. (Verified 2026-04-01)
- [x] 🏆 **Track Target Working**: Verified manual and auto tracking. (Verified 2026-04-01)
- [x] 🏆 **Detailed Log Naming**: Log files now save with full ISO timestamp. (Verified 2026-04-01)
- [x] 🏆 **Warp Button Upgrades**: Added **30x** and **7.2kx** buttons. (Verified 2026-04-01)
- [x] 🏆 **Camera Inversion Bug:** Fixed `shipGroup.lookAt` vector subtraction to properly align the camera facing forward along the velocity path instead of backwards.
