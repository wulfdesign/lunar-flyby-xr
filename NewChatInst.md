# 🚀 Lunar Flyby XR - Session Handoff Instructions
**Current Version:** `v1.9.7`
**Target Goal:** `v2.0` (Re-entry & Landing UI)

## Context for New AI Assistant
You are working on an interactive 3D WebXR simulation of a Translunar orbit in `Three.js` (mimicking Artemis II / Apollo trajectories). The simulation consists of a single `index.html` file right now that houses all the Physics math, the CSS HUD overlay, and the 3D rendering.

## What was completed in the Last Session:
*   **The Physics Engine is stable!** The simulation correctly models a Deep Space Coast, a trailing edge Lunar Flyby gravity assist, and a return trajectory to Earth using Velocity Verlet integration and `_tempVec` object pooling to prevent memory leaks.
*   **Major Bug Fixed:** We found an issue where the camera was watching the simulation backwards! Three.js `lookAt` maps the positive-Z axis to the forward thrust vector, but cameras face negative-Z. We fixed this by subtracting the velocity vector from the object position when calculating the `lookTarget`.

## Tasks queued for YOU (This upcoming Session):
Do NOT jump to architecture upgrades yet. You need to focus on these queued fixes first:
1.  **UX Polish:** Make the warning buttons flash prominently when slowing down at checkpoints.
2.  **3D Geometry Clipping:** The `progradeMesh` vector ring is mounted at `Z: -15`. Because `renderScale` is `0.02` (every 1 unit = 50km), when the capsule is 100km above Earth, the crosshair ring physically clips 600km DEEP into the crust of the Earth mesh, causing it to visually disappear. This needs to be scaled and pulled closer to the camera to solve the clipping.
3.  **Core Mechanic Request:** The simulation currently triggers a warning at altitude `100km` but there is *no aerodynamic drag*. Plunging into Earth at 10.5 km/s results in no deceleration. You must build an atmospheric drag function that bleeds the velocity, translating it into G-Force calculations for warnings, eventually deploying parachutes.

*Check `Tasks.md` and `devlog.md` immediately upon starting for the most up-to-date tracking.*
