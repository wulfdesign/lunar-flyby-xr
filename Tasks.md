# 📋 Tasks & Upgrades

> **Legend:**
> 🔥🔥🔥 (Critical) | 🔥🔥 (High) | 🔥 (Medium) | 🧊 (Cold/Icebox)
> ❄️ (Frozen) | ❄️❄️ (Deep Freeze) | ❄️❄️❄️ (Cryogenic)
> 🛠️ (In Progress) | 🧪 (Ready for QA) | 🩹 (Tech Debt/Good Enough) | 🏆 (Verified/Done)

---

## 🏆 Completed
- [x] 🏆 **Private Workspace Infrastructure**: Established `privTasks.md`, `privDevLog.md`, and `privCompleted.md` for confidential planning. (Verified 2026-03-31)
- [x] 🏆 **Artemis II & dearMoon Research**: Created `ArtemisII.md` and `dearMoon.md` with mission history and context. (Verified 2026-03-31)
- [x] 🏆 **Cinematic Video Scripting**: Created `docs/videoShotScript.md` with "Shot 01: The Cislunar Crossing" sequence parameters. (Verified 2026-03-31)
- [x] 🏆 **LinkedIn & Facebook Soft Launch**: Published official launch posts and cross-posted to NASA/Space groups. (Verified 2026-03-31)
- [x] 🏆 **Social Media Strategy**: Created `docs/socialMedia.md` with goals and content guidelines. (Verified 2026-03-31)
- [x] 🏆 **Historical Artifact Archiving**: Preserved the 2018 dearMoon proposal email in `/archive` and updated project history. (Verified 2026-03-31)
- [x] 🏆 **Repository Organization**: Moved documentation files into `/docs` and kept archives in `/archive` for a clean root structure. (Verified 2026-03-31)
- [x] 🏆 **Project Licensing**: Added MIT License (LICENSE.md) credited to Wulf Design Studios / UpLiftVR Studios. (Verified 2026-03-31)
- [x] 🏆 **Live Deployment**: Enabled GitHub Pages and added the [Launch Live Experience](https://wulfdesign.github.io/lunar-flyby-xr/) link to README. (Verified 2026-03-31)
- [x] 🏆 **Project Cleanup**: Organized debug screenshots and flight logs into `/debug` directory. (Verified 2026-03-31)
- [x] 🏆 **GitHub Publication**: Repository live at `https://github.com/wulfdesign/lunar-flyby-xr` with GitHub Pages enabled. (Chalice 🏆 2026-03-31)
- [x] 🏆 **Project Screenshots**: Integrated in-sim screenshots into repository and README. (Verified 2026-03-31)
- [x] 🏆 **Standalone Compatibility**: Fix `index.html` to work with single double click (no server required). (Chalice 🏆 2026-03-31)
- [x] 🏆 **Modernize Startup Script**: Update `start_lunar_flyby.bat` to use `npx serve` on port 3550. (Chalice 🏆 2026-03-31)
*(Archive items moved to COMPLETED.md)*

## 🧪 Waiting for QA
- [ ] 🧪 **Cinematic Capture System**: Implemented "Shot 01" automation engine with dynamic warp and smooth camera pans. (Ready for QA 🧪 2026-03-31)
- [ ] 🧪 **Project Credits & Resources**: Created `docs/credits.md` and updated `README.md` with full attribution (NASA, Three.js, Wikipedia, etc.). (Chalice 🏆 2026-03-31)
- [ ] 🧪 **SOI Entrance Latch (Initial Version)**: Attempted fix for warp-reset when entering Moon's gravity. (Needs testing, User reports it still "stops" the sim).
- [ ] 🧪 **Mission Itinerary Checklist**: Checklist UI that tracks TLI, Coast, and Flyby phases.
- [ ] 🧪 **Consolidated HUD**: Merging Environment and Telemetry panels into one list.

## 🛠️ Current Work
- [ ] 🔥🔥🔥 **Fix Lunar SOI Warp Stop**: Simulation "stops" or resets warp repeatedly upon entering Lunar Orbit. (Top Release Priority)
- [ ] 🔥🔥🔥 **Troubleshoot Phase 5 Refinements**: Fix physics instability at 7.2kx, gear-shifting logic, and logging bugs encountered in the latest session.
- [ ] 🔥🔥🔥 **Social: Cinematic Video Execution**: Record TLI burn, coast, and flyby using the stable automation system (Commit 2779de5).

## 🔥🔥🔥 High Priority (Ready to Forge)
- [ ] 🔥🔥🔥 **Bug Investigation: Time Warp Latch**: Refine the SOI trigger between Earth/Moon.

## 🔥🔥 Medium Priority
- [ ] 🔥🔥 **V2.0 Roadmap Integration**: Move roadmap items from `index.html` comments into `tasks.md`.
- [ ] 🔥🔥 **Mission: CubeSat Crowdfund**: Develop technical proof-of-concept for lunar flyby using consumer electronics (COTS).
- [ ] 🔥🔥 **Prograde Marker Refinement**: Ensure 3D marker and crosshair don't confuse the user about ship heading.

## 🧊 Icebox (Cold)
- [ ] 🧊 **Post-Flight Mission Report**: Generate a UI report showing Max Gs, flight time, and fuel remaining.
- [ ] 🧊 **Trajectory Trails**: Visual path rendering (White = Flown, Blue Dotted = Projected).
- [ ] 🧊 **Overview Map**: 3/4 top-down orthographic minimap.
- [ ] 🧊 **Mid-Course Correction (MCC)**: Off-course detection and correction burns.

## ❄️ Frozen (Do much later)
- [ ] ❄️ **Asset Testing**: Test server with custom elements and high-res models (.glb) required for download. (Deep Freeze ❄️❄️❄️)
- [ ] ❄️ **Find True Timestamps**: Search Gemini history for exact message times.
- [ ] ❄️ **Lagrangian Points (L1-L4)**: Add markers for Earth-Moon Lagrange points.
- [ ] ❄️ **Lunar Orbit Insertion (LOI)**: Retrograde burn capability at perilune.
- [ ] ❄️ **Asset Upgrades**: High-res NASA .glb models for Orion and SLS.

## 🏆 Completed Ready to Archive
