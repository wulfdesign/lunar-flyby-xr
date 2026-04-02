# 📋 Tasks & Upgrades

> **Legend:**
> 🔥🔥🔥 (Critical) | 🔥🔥 (High) | 🔥 (Medium) | 🧊 (Cold/Icebox)
> ❄️ (Frozen) | ❄️❄️ (Deep Freeze) | ❄️❄️❄️ (Cryogenic)
> 🛠️ (In Progress) | 🧪 (Ready for QA) | 🩹 (Tech Debt/Good Enough) | 🏆 (Verified/Done)

---

## 🏆 Completed
- [x] 🏆 **Optimized Flight Logging**: Removed periodic 5s snapshots to drastically reduce log size. Logging now triggers only on meaningful state changes. (Verified 2026-04-01)
- [x] 🏆 **Trajectory Data**: Added ship X, Y, Z coordinates to every log entry for trajectory validation and debugging. (Verified 2026-04-01)
- [x] 🏆 **Detailed Log Naming**: Log files now save with full ISO timestamp (YYYY-MM-DD-HH-MM-SS) for better organization. (Verified 2026-04-01)
- [x] 🏆 **Non-Forced Warp Transitions**: Removed forced 1x warp resets at Lunar SOI/Encounter. Warp is now purely user or playback driven. (Verified 2026-04-01)
- [x] 🏆 **Streamlined Logging**: Stripped unstable camera/FOV data from Flight Logs to focus on stable Warp/MET synchronization. (Verified 2026-04-01)
- [x] 🏆 **Data-Driven Flight Log Playback**: Implemented LOAD FLIGHT LOG functionality to play back recorded missions. (Verified 2026-04-01)
*(Archive items moved to COMPLETED.md)*

## 🧪 Waiting for QA
- [ ] 🧪 **Log Size Verification**: Test a full flight and confirm the resulting JSON is a manageable size (kilobytes vs megabytes). (Ready for QA 🧪 2026-04-01)

## 🛠️ Current Work
- [ ] 🔥🔥🔥 **Physics: Free Return Verification**: Investigate reported "fly past" issue. Verify if the TLI burn energy and Lunar SOI gravity are correctly resulting in a free-return trajectory.
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
