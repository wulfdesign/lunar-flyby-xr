# 🚀 Lunar Flyby XR - Devlog

## [2026-03-30 19:30] - Version 3: Stable Orbits & Velocity Verlet
### 📝 Summary
Complete physics engine rewrite to support stable orbits and educational documentation.

### 🛠️ Work Done
- Switched from Euler integration to **Velocity Verlet** for energy-conserving orbital mechanics.
- Implemented real-world units (kilometers, kilograms, seconds, muEarth, muMoon).
- Added **Vis-viva equation** based TLI (Trans-Lunar Injection) targeting.
- Implemented **Mission Elapsed Time (MET)** counter.
- Enhanced UI with educational tooltips and dynamic color-coded HUD (Nominal, Caution, Danger).
- Added "Skip to Window" autopilot feature with 10,000x warp.
- Implemented stable 400km initial LEO (Low Earth Orbit).

### 📖 Educational Notes (Comments added to code)
- Explained Standard Gravitational Parameter (μ).
- Documented Kepler's Circular Orbital Velocity formula ($v = \sqrt{\mu / r}$).
- Documented Vis-viva equation for calculating transfer $\Delta V$.

---

## [2026-03-30 18:30] - Version 2: WebGL Error Fix
### 📝 Summary
Fixed ReferenceError caused by failing CDN link and simplified WebGL initialization.

### 🛠️ Work Done
...
