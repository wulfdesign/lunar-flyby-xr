# 📋 Tasks & Upgrades

> **Legend:**
> 🔥🔥🔥 (Critical) | 🔥🔥 (High) | 🔥 (Medium) | 🧊 (Cold/Icebox)
> ❄️ (Frozen) | ❄️❄️ (Deep Freeze) | ❄️❄️❄️ (Cryogenic)
> 🛠️ (In Progress) | 🧪 (Ready for QA) | 🩹 (Tech Debt/Good Enough) | 🏆 (Verified/Done)

---

## 🛠️ Current Work
- [ ] 🔥🔥🔥 **Physics: True TLI Targeting Engine**: Replace artificial `MISSION_LEAD_ANGLE` moon-moving cheat with realistic TLI parameters (ejection angle, transit time) to calculate leading-edge interception of a naturally orbiting Moon.
- [ ] 🔥🔥🔥 **Artemis II Telemetry**: Implement data-mapping from NASA AROW/OEM files into the simulation mission profile.
- [ ] 🔥🔥🔥 **HUD: Visual Trajectory Indicator**: Show "On Target" / "Off Course" status based on real-time physics projection.

## 🐛 UX & Polish (Debrief Feedback)
- [ ] 🐛 **UX: Smooth Warp Deceleration**: Transition warp down to 1x incrementally with visual feedback instead of a hard snap.
- [ ] 🐛 **UX: MCC Countdown & Execution UI**: Display required delta-V, time remaining to burn (2 mins), and allow <10x warp during countdown, enforcing 1x for execution.
- [ ] 🐛 **UI/UX: Warp Text Overflow**: Fix bug where text pushes the UI off-screen. Need responsive layout or CSS constraint.
- [ ] 🐛 **UX: Explicit Log Entry Feedback**: Add visual confirmation/HUD toast when a user manually clicks the 1x button to trigger a flight log save.

## 🔥🔥 End-of-Mission Flow (Re-Entry & Splashdown)
- [ ] 🔥🔥 **UI/HUD: Phase Checklist Updates**: Add "Loss of Signal (LOS) Warning", "Cislunar Return", "Re-entry Prep". 
- [ ] 🔥🔥 **UX: Comms Radio UI**: Add a dedicated scrolling log box for CAPCOM radio instructions and ground-control readouts, logging them to the json output.
- [ ] 🔥🔥 **Simulation: Re-Entry Heating & Plasma Blackout**: Implement visual indicators and a comms blackout period as altitude drops below 120km.
- [ ] 🔥🔥 **Mechanics: Splashdown Sequence**: Add retro-fire targeting, heat shield orientation requirement, drogue chute deployment, and main chute splashdown.
- [ ] 🔥🔥 **Simulation: Splashdown Geolocation Tracking**: Calculate geographic latitude/longitude impact coordinates by syncing the final Cartesian position vector with a rotating Earth texture base based on Mission Elapsed Time.

## 🧪 Ready for QA (Waiting for User Confirmation)
- [ ] 🧪 **UX: Configurable Warp Limits**: Extracted `WARP_LIMITS` for user-adjustable flyby slowdown testing.
- [ ] 🧪 **UI: Revert Sim Start Time**: Reset initial mission window using `MISSION_LEAD_ANGLE`.
- [ ] 🧪 **Physics: Object Pooling Refactor**: Zero-allocation math using global vectors to fix high-warp lag.
- [ ] 🧪 **UX: Gearbox Responsiveness**: Reduced shift delay to 0.5s and added "Current -> Target" HUD feedback (🏆).
- [ ] 🧪 **Physics: Refine Lead Angle (V3)**: Adjusted targetPhaseAngle to 0.74 rad to fix Moon impacts (🏆).
- [ ] 🧪 **Versioning: Alignment**: Reverted/aligned SIM_VERSION to v1.9.6 for baseline consistency.

## 🔥🔥🔥 High Priority (Ready to Forge)
- [ ] 🔥🔥🔥 **Controls: Manual Thrust Vectoring**: Allow user to adjust burn direction (currently locked to prograde) for mid-course corrections.
- [ ] 🔥🔥🔥 **VR: Controller Troubleshooting**: Investigate why controllers might not be appearing in WebXR; add check for `select` events.
- [ ] 🔥🔥🔥 **Artemis II: State Vector Interpolation**: Create the linear/cubic spline interpolation engine for 10-minute samples.

## 🔥🔥 V2.0 Mission Goals & Architecture
- [ ] 🔥🔥 **UI: Mission Control Radio Feed**: Add a "CAPCOM" text box to display authentic radio readouts and telemetry instructions (e.g. "Houston, we are go for TMI").
- [ ] 🔥🔥 **Physics: Lunar Orbit Insertion (LOI)**: Transition beyond Free-Return trajectories to calculate decel burns for stable lunar captures.
- [ ] 🔥🔥 **Avionics: Flight Computer UI**: Build a targeting console to read current state vectors and calculate maneuver nodes (intercepts, rendezvous, MCCs).
- [ ] 🔥🔥 **Physics: Sun Gravity Integration**: Add solar mass to N-body calculation for v2.1 "Gold Master" accuracy.
- [ ] 🔥🔥 **Architecture: Modular Source Files**: Prepare project for split into `styles.css`, `physics.js`, and `ui.js` while maintaining single-file build.
- [ ] 🔥🔥 **Artemis II Real-Time Replay**: Load and play back the actual mission state-vectors from NASA data.


## 🧊 Icebox (Cold)
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
