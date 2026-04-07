# 📋 Tasks & Upgrades

> **Legend:**
> 🔥🔥🔥 (Critical) | 🔥🔥 (High) | 🔥 (Medium) | 🧊 (Cold/Icebox)
> ❄️ (Frozen) | ❄️❄️ (Deep Freeze) | ❄️❄️❄️ (Cryogenic)
> 🛠️ (In Progress) | 🧪 (Ready for QA) | 🩹 (Tech Debt/Good Enough) | 🏆 (Verified/Done)

---

## 🛠️ Current Work
- [ ] 🔥🔥🔥 **Physics: Refine Mission Lead Angle**: Investigate why ship arrives at orbital path but misses Moon phase; update 0.83 rad offset.
- [ ] 🔥🔥🔥 **UX: Suggested Warp Alerts**: Replace forced resets at milestones with flashing UI buttons and `nav-msg` prompts.
- [ ] 🔥🔥🔥 **HUD: Gravity Units (m/s²)**: Convert gravity display from km/s² to m/s² for human-scale readability.

## 🧪 Ready for QA (Waiting for User Confirmation)
- [ ] 🧪 **Physics: Rocket Equation Burn Estimation**: Uses Tsiolkovsky math for mass-aware target time calculation (🏆).
- [ ] 🧪 **Physics: Optimized Sub-stepping**: Lifted budget to 10k steps and refined SOI thresholds for high-warp stability (🏆).
- [ ] 🧪 **Controls: Warp Reset at MES**: Engines now automatically force 1x warp at ignition for maximum physics precision.
- [ ] 🧪 **Bug: Logging TypeError**: Fixed "Cannot read properties of undefined" crash when logging events with partial telemetry.

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
