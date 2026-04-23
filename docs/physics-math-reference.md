# Artemis Orbital Physics & Math Reference

This document serves as the "Live Documentation" for the mathematical constants and physics engines driving the `index.html` simulation. To ensure maximum performance and maintain a minimal file footprint, many of these educational comments were stripped from the production source code.

This reference provides the context behind the math.

## 1. Velocity Verlet Integration
Unlike games that place ships on rails using splines, we calculate raw, real-time gravity frame-by-frame. We use **Velocity Verlet** instead of Euler integration because it handles multi-day orbital paths with significantly less "energy drift" (preventing the orbit from artificially spiraling outward).

## 2. N-Body Gravity Constants
All units in the simulation strictly follow standard real-world dimensions: **kilometers (km)** for distance, **kilograms (kg)** for mass, and **seconds (s)** for time.

*   `radEarth = 6371` -- Earth's equatorial radius (km).
*   `radMoon = 1737` -- Lunar equatorial radius (km).
*   `distMoon = 384400` -- Average distance between Earth and Moon (km).
*   `muEarth = 398600.4418` -- Earth's Standard Gravitational Parameter ($G \times M_{earth} $) in $km^3 / s^2$.
*   `muMoon = 4902.8000` -- Moon's Standard Gravitational Parameter in $km^3 / s^2$.

> **Equation:** Gravity Acceleration Vector $\vec{a} = - \frac{\mu}{|\vec{r}|^3} \vec{r}$

## 3. Atmospheric Re-Entry & Aerodynamic Drag
The simulation accurately enforces a **2-degree reentry keyhole**. If you enter too steep, lethal G-forces (calculated via drag acceleration) will destroy the craft. If you enter too shallow, the aerodynamic drag will be insufficient to scrub your velocity, and you will skip into solar orbit.

**The Barometric Formula (Exponential Density):**
*   `RHO_0 = 1.225` -- Sea level atmospheric density ($kg/m^3$).
*   `SCALE_HEIGHT = 8.5` -- Earth's atmospheric scale height (km).
*   `DRAG_AREA = 0.011` -- Exposed cross-sectional area of the capsule base ($km^2$).

> **Equation:** Atmospheric Density $\rho = \rho_0 \times e^{-(\text{altitude} / H_{scale})}$  
> **Equation:** Drag Force $F_d = \frac{1}{2} \rho v^2 C_d A$

**Parachute Stages (Cd adjustments):**
The capsule relies on a multi-stage `dragCd` deployment to survive the final descent.
*   **Atmospheric Coast:** `Cd = 1.5`
*   **Drogue Chutes (< 7.3km):** `Cd = 50.0`
*   **Main Chutes (< 3.0km):** `Cd = 150.0`

## 4. Performance: Zero-Allocation Object Tracking
To cross the cislunar gap in a reasonable time, the simulation relies on a time warp of up to **7,200x** (2 hours per second). 

If we executed `new THREE.Vector3()` during every physics calculation at 60 FPS, the JavaScript engine would accumulate millions of abandoned vectors per second, triggering massive Garbage Collection (GC) pauses and locking up the browser. 
Instead, we globally declare temporary vectors (`_tempVec`) and continually `.copy()` and `.add()` values into them, resulting in zero new memory allocations during flight.
