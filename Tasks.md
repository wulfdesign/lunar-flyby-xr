# 📋 Tasks & Upgrades

> **Legend:**
> 🔥🔥🔥 (Critical) | 🔥🔥 (High) | 🔥 (Medium) | 🧊 (Cold/Icebox)
> ❄️ (Frozen) | ❄️❄️ (Deep Freeze) | ❄️❄️❄️ (Cryogenic)
> 🛠️ (In Progress) | 🧪 (Ready for QA) | 🩹 (Tech Debt/Good Enough) | 🏆 (Verified/Done)

---

## 🛠️ Current Work
- [ ] 🔥🔥🔥 **Physics: Lunar Keyhole Investigation**: Verify the perilune target maths to ensure a reliable free-return trajectory. Investigate why recent flights overshot into deep space.
- [ ] 🔥🔥🔥 **Physics: Burn Precision**: Investigate discrepancy between `initialTargetBurnTime` and `actualBurnTime`. Ensure the engine cuts off exactly when the target energy is reached.
- [ ] 🔥🔥🔥 **Final Release Check**: Perform one last manual flight to confirm all HUD milestones and flight log saves are working perfectly.

## 🔥🔥🔥 High Priority (Ready to Forge)
- [ ] 🔥🔥🔥 **Physics: Sub-stepping Refinement**: Ensure gravity integration remains precise during SOI entry at high warp. (In Progress)

## 🔥🔥 V2.0 Mission Goals & Architecture
- [ ] 🔥🔥 **Mission: Elliptical Earth Loop**: Add option for an initial high-eccentricity Earth orbit before the Moon transfer (Artemis II profile).
- [ ] 🔥🔥 **UI: Mission Selection Panel**: Implement a splash screen or settings panel to choose between Direct TMI and Elliptical Earth Loop.
- [ ] 🔥🔥 **Resource Integration**: Collate reference transcripts and video links into the simulation's educational docs.
- [ ] 🔥🔥 **V2.0 Roadmap Integration**: Move roadmap items from `index.html` comments into this list.

## 🧊 Icebox (Cold)
- [ ] 🧊 **Refine Auto Camera Tracking**: Automated pans and tracking for "Cinematic hero shots" currently disabled.
- [ ] 🧊 **Camera Log/Playback**: Re-enable camera orientation logging once the sync logic is more robust.
- [ ] 🧊 **Restore Cinematic Capture**: Re-enable and polish the hardcoded Shot 01 sequence once the playback engine is fully stable.
- [ ] 🧊 **Restore Load Flight Log**: Re-enable log playback once the "wonkyness" and state reset issues are resolved.

## 🏆 Completed Ready to Archive
- [x] 🏆 **Burn Precision Logging**: Added `target_burn_s` and `actual_burn_s` to logs for TMI troubleshooting. (Verified 2026-04-01)
- [x] 🏆 **Log Folder Organization**: Established `/logs` directory for flight record management. (Verified 2026-04-01)
- [x] 🏆 **Track Target Working**: Verified that manual and auto tracking (when enabled) correctly follows targets. (Verified 2026-04-01)
- [x] 🏆 **Comprehensive Milestone Logging**: Tracked "Approaching", "At", and "Beyond" states for Geosync, Midpoint, and SOI. (Verified 2026-04-01)
- [x] 🏆 **Bugfix: Duplicate Declarations**: Resolved `distM` and `lastLogTime` SyntaxErrors. (Verified 2026-04-01)
- [x] 🏆 **Trajectory Data**: Added ship X, Y, Z coordinates to every log entry for trajectory validation. (Verified 2026-04-01)
- [x] 🏆 **Optimized Flight Logging**: Reduced periodic snapshot frequency to lower file size. (Verified 2026-04-01)
- [x] 🏆 **Detailed Log Naming**: Log files now save with full ISO timestamp. (Verified 2026-04-01)
- [x] 🏆 **Non-Forced Warp Transitions**: Removed forced 1x warp resets at Lunar SOI/Encounter. (Verified 2026-04-01)
- [x] 🏆 **Data-Driven Flight Log Playback**: Implemented basic LOAD FLIGHT LOG (Currently disabled for stability). (Verified 2026-04-01)
- [x] 🏆 **Warp Button Upgrades**: Added **30x** and **7.2kx** buttons. (Verified 2026-04-01)
