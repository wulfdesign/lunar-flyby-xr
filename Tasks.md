# 📋 Tasks & Upgrades

> **Legend:**
> 🔥🔥🔥 (Critical) | 🔥🔥 (High) | 🔥 (Medium) | 🧊 (Cold/Icebox)
> ❄️ (Frozen) | ❄️❄️ (Deep Freeze) | ❄️❄️❄️ (Cryogenic)
> 🛠️ (In Progress) | 🧪 (Ready for QA) | 🩹 (Tech Debt/Good Enough) | 🏆 (Verified/Done)

---

## 🏆 Completed
- [x] 🏆 **Data-Driven Flight Log Playback**: Implemented LOAD FLIGHT LOG functionality to play back recorded missions (Warp, Cam, FOV). (Verified 2026-04-01)
- [x] 🏆 **Enhanced Mission Recording**: Every warp change and 5s state snapshot (Cam/FOV) is captured in the flight log. (Verified 2026-04-01)
- [x] 🏆 **Recommended Action System**: Suppressed forced 1x warp resets during professional (Cine/Playback) modes. (Verified 2026-04-01)
- [x] 🏆 **Warp Button Upgrades**: Added **30x** and **7.2kx** buttons with professional labels and logic. (Verified 2026-04-01)
- [x] 🏆 **Granular HUD POIs**: Implemented full suite of mission regions (Geosync, Midpoint, SOI, Proximity) with alerts. (Verified 2026-04-01)
- [x] 🏆 **Gradual Lunar Deceleration**: Multi-step warp deceleration (1800x -> 1x) for professional approach. (Verified 2026-04-01)
- [x] 🏆 **Gear-Shifting Warp Logic**: Smooth, stepped time warp transitions (2s hold per level) implemented and verified. (Verified 2026-04-01)
- [x] 🏆 **Manual Camera Freedom**: Manual camera panning and tilting enabled during Cinematic Capture when tracking is off. (Verified 2026-04-01)
- [x] 🏆 **Fix Lunar SOI Warp Stop**: Simulation threshold increased to 60,000km with robust latching logic to prevent repeated resets. (Verified 2026-04-01)
*(Archive items moved to COMPLETED.md)*

## 🧪 Waiting for QA
- [ ] 🧪 **Flight Log Playback Engine**: Test recording a full mission and loading the JSON to verify auto-playback of all camera/warp moves. (Ready for QA 🧪 2026-04-01)

## 🛠️ Current Work
- [ ] 🔥🔥🔥 **Verification: Playback Fidelity**: Ensure the playback engine perfectly reconstructs complex mission profiles.

## 🔥🔥🔥 High Priority (Ready to Forge)
- [ ] 🔥🔥🔥 **UI: Flight Log Browser**: (Future) allow selection from multiple local logs.

## 🔥🔥 Medium Priority
- [ ] 🔥🔥 **V2.0 Roadmap Integration**: Move roadmap items from `index.html` comments into `tasks.md`.
- [ ] 🔥🔥 **Mission: CubeSat Crowdfund**: Develop technical proof-of-concept for lunar flyby using consumer electronics (COTS).

## 🧊 Icebox (Cold)
- [ ] 🧊 **Refine Auto Camera Tracking**: Automated pans and tracking for "Cinematic hero shots" currently disabled in favor of manual control or data-driven playback. (Moved to Icebox 2026-04-01)

## 🏆 Completed Ready to Archive
