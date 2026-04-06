# 📋 Tasks & Upgrades

> **Legend:**
> 🔥🔥🔥 (Critical) | 🔥🔥 (High) | 🔥 (Medium) | 🧊 (Cold/Icebox)
> ❄️ (Frozen) | ❄️❄️ (Deep Freeze) | ❄️❄️❄️ (Cryogenic)
> 🛠️ (In Progress) | 🧪 (Ready for QA) | 🩹 (Tech Debt/Good Enough) | 🏆 (Verified/Done)

---

## 🛠️ Current Work
- [ ] 🔥🔥🔥 **Artemis II Telemetry**: Implement data-mapping from NASA AROW/OEM files into the simulation mission profile.
- [ ] 🔥🔥 **Mission: Elliptical Earth Loop**: Artemis II initial high-eccentricity orbit option.

## 🧪 Ready for QA (Waiting for User Confirmation)
- [ ] 🧪 **Physics: Velocity Verlet Integration**: Standardized integration for better energy conservation and lunar capture.
- [ ] 🧪 **Physics: Ultra-fine Sub-stepping**: Implemented 0.01s steps for close lunar flybys to prevent "drifting past".
- [ ] 🧪 **Warp: Smooth Gearbox**: Automated gradual ramp-up/down implemented globally for all warp changes.
- [ ] 🧪 **Telemetry: Enhanced Vectors & Gravity**: Added Vx, Vy, Vz and Gravity Field magnitudes (Earth/Moon) to logs and HUD.
- [ ] 🧪 **Mobile: UI Layout (Landscape/Portrait)**: Responsive scaling, scrolling, and orientation-specific layouts (🏆).
- [ ] 🧪 **Quest 3: VR HUD Visibility**: Updated z-index and panel background for `dom-overlay` visibility.
- [ ] 🧪 **Quest 3: VR Session Restoration**: User confirmed VR works via Link (🏆).

## 🔥🔥🔥 High Priority (Ready to Forge)
- [ ] 🔥🔥🔥 **VR: Controller Troubleshooting**: Investigate why controllers might not be appearing in WebXR; add check for `select` events.
- [ ] 🔥🔥🔥 **Artemis II: State Vector Interpolation**: Create the linear/cubic spline interpolation engine for 10-minute samples.

## 🔥🔥 V2.0 Mission Goals & Architecture
- [ ] 🔥🔥 **Physics: Sun Gravity Integration**: Add solar mass to N-body calculation for v2.1 "Gold Master" accuracy.
- [ ] 🔥🔥 **Architecture: Modular Source Files**: Prepare project for split into `styles.css`, `physics.js`, and `ui.js` while maintaining single-file build.
- [ ] 🔥🔥 **Artemis II Real-Time Replay**: Load and play back the actual mission state-vectors from NASA data.


## 🧊 Icebox (Cold)
- [ ] 🧊 **Restore Load Flight Log**: Re-enable log playback once stability issues are resolved.
- [ ] 🧊 **Refine Auto Camera Tracking**: Automated pans currently disabled.

## 🏆 Completed Ready to Archive
- [x] 🏆 **Burn Precision Logging**: Added `target_burn_s` and `actual_burn_s` to logs. (Verified 2026-04-01)
- [x] 🏆 **UI Stability & Crash Prevention**: Implemented `safeSetText` and `try...catch` in the main loop to resolve "Cannot set properties of null" errors. (Verified 2026-04-06)
- [x] 🏆 **Log Folder Organization**: Established `/logs` directory. (Verified 2026-04-01)
- [x] 🏆 **Track Target Working**: Verified manual and auto tracking. (Verified 2026-04-01)
- [x] 🏆 **Detailed Log Naming**: Log files now save with full ISO timestamp. (Verified 2026-04-01)
- [x] 🏆 **Warp Button Upgrades**: Added **30x** and **7.2kx** buttons. (Verified 2026-04-01)
