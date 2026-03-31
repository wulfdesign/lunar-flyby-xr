# 🚀 Lunar Flyby XR - Devlog

## [2026-03-30 23:30] - Version 13: SOI Latch & HUD Consolidation
### 📝 Summary
Bug fixes for the time warp system and streamlined HUD for better visibility.

### 🛠️ Work Done
- **SOI State Latch**: Fixed the "warp reset" loop. The simulation now uses a state latch (`hasEnteredLunarSOI`) to ensure the automatic drop to 1x speed only happens once upon entering the Moon's gravity well.
- **HUD Consolidation**: Merged the Environment and Telemetry panels into a single, unified list on the left side of the screen. This clears the right side for an unobstructed view of the lunar encounter.
- **Raycast Targeting Fix**: Specifically excluded the cockpit geometry from the raycaster to prevent the "Targeting: Cockpit" bug and ensure planets are selectable.
- **Physics Verification**: Confirmed fuel mass flow rates and Specific Impulse ($I_{sp}$) calculations for physical accuracy.

---

## [2026-03-30 23:15] - Version 12: Milestones & Phase Recalibration
### 📝 Summary
Refined trajectory math and added environment tracking for long-duration transit.

### 🛠️ Work Done
...
