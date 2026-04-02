# 📋 Tasks & Upgrades

> **Legend:**
> 🔥🔥🔥 (Critical) | 🔥🔥 (High) | 🔥 (Medium) | 🧊 (Cold/Icebox)
> ❄️ (Frozen) | ❄️❄️ (Deep Freeze) | ❄️❄️❄️ (Cryogenic)
> 🛠️ (In Progress) | 🧪 (Ready for QA) | 🩹 (Tech Debt/Good Enough) | 🏆 (Verified/Done)

---

## 🏆 Completed
- [x] 🏆 **Trajectory Data**: Added ship X, Y, Z coordinates to every log entry for trajectory validation. (Verified 2026-04-01)
- [x] 🏆 **Optimized Flight Logging**: Reduced periodic snapshot frequency to lower file size. (Verified 2026-04-01)
- [x] 🏆 **Detailed Log Naming**: Log files now save with full ISO timestamp. (Verified 2026-04-01)
- [x] 🏆 **Non-Forced Warp Transitions**: Removed forced 1x warp resets at Lunar SOI/Encounter. (Verified 2026-04-01)
- [x] 🏆 **Streamlined Logging**: Stripped unstable camera/FOV data from Flight Logs. (Verified 2026-04-01)
- [x] 🏆 **Data-Driven Flight Log Playback**: Implemented LOAD FLIGHT LOG functionality. (Verified 2026-04-01)
- [x] 🏆 **Warp Button Upgrades**: Added **30x** and **7.2kx** buttons. (Verified 2026-04-01)
*(Archive items moved to COMPLETED.md)*

## 🧪 Waiting for QA
- [ ] 🧪 **Comprehensive Milestone Logging**: Logging "Approaching", "At", and "Beyond" for all major POIs (Geosync, Midpoint, SOI). (Ready for QA 🧪 2026-04-01)
- [ ] 🧪 **Log Throttling**: Hourly "Nominal" updates removed or extended to prevent 7200x spam. (Ready for QA 🧪 2026-04-01)

## 🛠️ Current Work
- [ ] 🔥🔥🔥 **Physics: Free Return Verification**: Investigate reported "fly past" issue. Check if 7200x warp causes physics drift or if TMI energy is too high for free return.
- [ ] 🔥🔥🔥 **Verification: Final Cislunar Flight**: Verify all milestones are correctly latched and logged once.

## 🔥🔥🔥 High Priority (Ready to Forge)
- [ ] 🔥🔥🔥 **Physics: Sub-stepping Refinement**: Ensure gravity integration remains precise during SOI entry at high warp.

## 🔥🔥 Medium Priority
- [ ] 🔥🔥 **V2.0 Roadmap Integration**: Move roadmap items from `index.html` comments into `tasks.md`.

## 🧊 Icebox (Cold)
- [ ] 🧊 **Refine Auto Camera Tracking**: Automated pans and tracking for "Cinematic hero shots" currently disabled.
- [ ] 🧊 **Camera Log/Playback**: Re-enable camera orientation logging once the sync logic is more robust.

## 🏆 Completed Ready to Archive
