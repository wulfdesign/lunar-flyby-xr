# 📋 Tasks & Upgrades

> **Legend:**
> 🔥🔥🔥 (Critical) | 🔥🔥 (High) | 🔥 (Medium) | 🧊 (Cold/Icebox)
> ❄️ (Frozen) | ❄️❄️ (Deep Freeze) | ❄️❄️❄️ (Cryogenic)
> 🛠️ (In Progress) | 🧪 (Ready for QA) | 🩹 (Tech Debt/Good Enough) | 🏆 (Verified/Done)

---

## 🛠️ Current Work
- [ ] 🔥🔥🔥 **Quest 3: Fix VR Entry**: Resolve "three blinking dots" and Link cord errors. Investigate WebXR session initiation.
- [ ] 🔥🔥🔥 **Mobile: Responsive HUD**: Fix HUD panel scaling and positioning for mobile screens.
- [ ] 🔥🔥🔥 **Mobile: Touch Navigation**: Map touch drag events to camera rotation (replace mouse-look).
- [ ] 🔥🔥🔥 **Artemis II Telemetry**: Implement data-mapping from NASA AROW/OEM files into the simulation mission profile.

## 🔥🔥🔥 High Priority (Ready to Forge)
- [ ] 🔥🔥🔥 **Physics: Lunar Keyhole Investigation**: Verify perilune maths for reliable free-return.
- [ ] 🔥🔥🔥 **Quest 3: Controller Input**: Map controller triggers/sticks to view dragging and HUD interaction.
- [ ] 🔥🔥🔥 **VR: HUD Out-of-Bounds**: Fix HUD clipping issues within the WebXR view.

## 🔥🔥 V2.0 Mission Goals & Architecture
- [ ] 🔥🔥 **Mission: Elliptical Earth Loop**: Artemis II initial high-eccentricity orbit option.
- [ ] 🔥🔥 **UI: Mission Selection Panel**: Choose between Direct TMI and Artemis II profile.
- [ ] 🔥🔥 **Artemis II Real-Time Replay**: Load and play back the actual mission state-vectors from NASA data.

## 🧊 Icebox (Cold)
- [ ] 🧊 **Restore Load Flight Log**: Re-enable log playback once stability issues are resolved.
- [ ] 🧊 **Refine Auto Camera Tracking**: Automated pans currently disabled.

## 🏆 Completed Ready to Archive
- [x] 🏆 **Burn Precision Logging**: Added `target_burn_s` and `actual_burn_s` to logs. (Verified 2026-04-01)
- [x] 🏆 **Log Folder Organization**: Established `/logs` directory. (Verified 2026-04-01)
- [x] 🏆 **Track Target Working**: Verified manual and auto tracking. (Verified 2026-04-01)
- [x] 🏆 **Detailed Log Naming**: Log files now save with full ISO timestamp. (Verified 2026-04-01)
- [x] 🏆 **Warp Button Upgrades**: Added **30x** and **7.2kx** buttons. (Verified 2026-04-01)
