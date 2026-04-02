# 📋 Tasks & Upgrades

> **Legend:**
> 🔥🔥🔥 (Critical) | 🔥🔥 (High) | 🔥 (Medium) | 🧊 (Cold/Icebox)
> ❄️ (Frozen) | ❄️❄️ (Deep Freeze) | ❄️❄️❄️ (Cryogenic)
> 🛠️ (In Progress) | 🧪 (Ready for QA) | 🩹 (Tech Debt/Good Enough) | 🏆 (Verified/Done)

---

## 🏆 Completed
- [x] 🏆 **Non-Forced Warp Transitions**: Removed forced 1x warp resets at Lunar SOI/Encounter. Warp is now purely user or playback driven. (Verified 2026-04-01)
- [x] 🏆 **Streamlined Logging**: Stripped unstable camera/FOV data from Flight Logs to focus on stable Warp/MET synchronization. (Verified 2026-04-01)
- [x] 🏆 **Data-Driven Flight Log Playback**: Implemented LOAD FLIGHT LOG functionality to play back recorded missions (Warp/MET only for now). (Verified 2026-04-01)
- [x] 🏆 **Warp Button Upgrades**: Added **30x** and **7.2kx** buttons with professional labels and logic. (Verified 2026-04-01)
- [x] 🏆 **Granular HUD POIs**: Implemented full suite of mission regions (Geosync, Midpoint, SOI, Proximity) with alerts. (Verified 2026-04-01)
- [x] 🏆 **Gradual Lunar Deceleration**: Multi-step warp deceleration (1800x -> 1x) for professional approach. (Verified 2026-04-01)
- [x] 🏆 **Gear-Shifting Warp Logic**: Smooth, stepped time warp transitions (2s hold per level) implemented and verified. (Verified 2026-04-01)
*(Archive items moved to COMPLETED.md)*

## 🧪 Waiting for QA
- [ ] 🧪 **Warp-Only Playback**: Test recording a mission with various warp changes and loading it back to verify the sim follows the speed profile correctly. (Ready for QA 🧪 2026-04-01)

## 🛠️ Current Work
- [ ] 🔥🔥🔥 **Verification: Final Cislunar Flight**: Verify all 12+ mission phases and warp transitions without any "forced" resets.

## 🔥🔥🔥 High Priority (Ready to Forge)
- [ ] 🔥🔥🔥 **Refinement: Playback Interpolation**: (Future) Smoothen transitions between log entries if needed.

## 🔥🔥 Medium Priority
- [ ] 🔥🔥 **V2.0 Roadmap Integration**: Move roadmap items from `index.html` comments into `tasks.md`.
- [ ] 🔥🔥 **Mission: CubeSat Crowdfund**: Develop technical proof-of-concept for lunar flyby using consumer electronics (COTS).

## 🧊 Icebox (Cold)
- [ ] 🧊 **Refine Auto Camera Tracking**: Automated pans and tracking for "Cinematic hero shots" currently disabled in favor of manual control or data-driven playback. (Moved to Icebox 2026-04-01)
- [ ] 🧊 **Camera Log/Playback**: Re-enable camera orientation logging once the sync logic is more robust. (Moved to Icebox 2026-04-01)

## 🏆 Completed Ready to Archive
