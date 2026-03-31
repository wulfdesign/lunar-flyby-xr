# 🚀 Lunar Flyby XR - Devlog

## [2026-03-30 22:30] - Version 9: Autopilot Latch & Burn Diagnostics
### 📝 Summary
Improved autopilot reliability and added detailed burn performance metrics.

### 🛠️ Work Done
- **Autopilot Latch**: Implemented a state latch that keeps the engines firing until the target orbital energy is reached, even if the optimal window timing drifts during the burn.
- **Burn Diagnostics HUD**: Added real-time tracking of "Target Burn" (frozen at ignition) vs "Actual Burn" time.
- **Visual Feedback**: Added color-coded flashing for the burn duration counter (Red < 80% complete, Yellow > 80%, Green flashing on MECO).
- **Physics Polish**: Refined the transition between LEO and Trans-Lunar Coast states.

---

## [2026-03-30 22:15] - Version 8: Stability & Bug Fix (TypeError)
### 📝 Summary
Fixed a critical initialization bug and improved simulation stability during startup.

### 🛠️ Work Done
...
