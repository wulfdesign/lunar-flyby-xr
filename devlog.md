# 🚀 Lunar Flyby XR - Devlog

## [2026-03-30 22:15] - Version 8: Stability & Bug Fix (TypeError)
### 📝 Summary
Fixed a critical initialization bug and improved simulation stability during startup.

### 🛠️ Work Done
- **TypeError Fix**: Resolved a crash where the `telemetry` object was null on the first frame if `simSecondsToProcess` was zero. Added a safety check to ensure at least one physics step is processed (`Math.max(1, ...)`).
- **Physics Latch**: Improved the `isTliCoast` detection logic to prevent accidental engine re-ignition during state transitions.

---

## [2026-03-30 22:00] - Version 7: Targeting & Itinerary HUD
### 📝 Summary
Added advanced navigation tools, flight logging, and interactive targeting features.

### 🛠️ Work Done
...
