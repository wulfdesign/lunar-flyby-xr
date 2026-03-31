# 📋 Tasks & Upgrades

> **Legend:**
> 🔥🔥🔥 (Critical) | 🔥🔥 (High) | 🔥 (Medium) | 🧊 (Cold/Icebox)
> ❄️ (Frozen) | ❄️❄️ (Deep Freeze) | ❄️❄️❄️ (Cryogenic)
> 🛠️ (In Progress) | 🧪 (Ready for QA) | 🩹 (Tech Debt/Good Enough) | 🏆 (Verified/Done)

---

## 🏆 Completed
- [x] 🏆 **Modernize Startup Script**: Update `start_lunar_flyby.bat` to use `npx serve` on port 3550. (Chalice 🏆 2026-03-31)
*(Archive items moved to COMPLETED.md)*

## 🧪 Waiting for QA
- [ ] 🧪 **Standalone Compatibility**: Fix `index.html` to work with single double click (no server required). (Ready for QA 🧪 2026-03-31)
- [ ] 🧪 **SOI Entrance Latch (Initial Version)**: Attempted fix for warp-reset when entering Moon's gravity. (Needs testing, User reports it still "stops" the sim).
- [ ] 🧪 **Mission Itinerary Checklist**: Checklist UI that tracks TLI, Coast, and Flyby phases.
- [ ] 🧪 **Consolidated HUD**: Merging Environment and Telemetry panels into one list.

## 🛠️ Current Work
- [ ] 🔥🔥🔥 **Fix Lunar SOI Warp Stop**: Simulation "stops" or resets warp repeatedly upon entering Lunar Orbit.

## 🔥🔥🔥 High Priority (Ready to Forge)
- [ ] 🔥🔥🔥 **Bug Investigation: Time Warp Latch**: Refine the SOI trigger to prevent multiple warp drops.

## 🔥🔥 Medium Priority
- [ ] 🔥🔥 **V2.0 Roadmap Integration**: Move roadmap items from `index.html` comments into `tasks.md`.
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
