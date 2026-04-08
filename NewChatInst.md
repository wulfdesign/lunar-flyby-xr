# 🚀 Lunar Flyby XR - Session Handoff Instructions
**Current Version:** `v1.9.7`
**Target Goal:** `v2.0` (Mobile UX & Re-entry)

## Context for New AI Assistant
You are working on an interactive 3D WebXR simulation of a Translunar orbit in `Three.js` (mimicking Artemis II / Apollo trajectories). The simulation consists of a single `index.html` file right now that houses all the Physics math, the CSS HUD overlay, and the 3D rendering.

## What was completed in the Last Session:
*   **The Physics Engine is stable!** The simulation correctly models a Deep Space Coast, a trailing edge Lunar Flyby gravity assist, and a return trajectory to Earth using Velocity Verlet integration and `_tempVec` object pooling to prevent memory leaks. We successfully executed a speedrun test surviving a 1.4km perilune slingshot and landing in the Pacific.
*   **UI/UX Polish:** We centered the WebXR and Reset View buttons, bumped up the FOV tracking scale by 120%, and significantly updated the `README.md` to showcase the project's historical legacy and a complete mobile portrait-mode lunar flyby. 

## Tasks queued for YOU (This upcoming Session):
Do NOT jump to architecture upgrades yet. You need to focus on these queued tasks first:
1.  **Mobile UX Overhaul:** The current layout places critical 7.2kx warp buttons too close to other touchscreen inputs, resulting in fatal misclicks on mobile. We need a targeted, touch-friendly UI strategy for mobile devices to prevent this.
2.  **UX Polish:** Make the notification warning and checkpoint buttons flash prominently when the system forces a warp deceleration. Check tasks to integrate the new "Orbital Traffic Checkpoints" (ISS, Starlink, GPS altitude markers).
3.  **Core Mechanic Request:** The simulation currently triggers a warning at altitude `100km` but there is *no aerodynamic drag*. Plunging into Earth at 10.5 km/s results in no deceleration. You must build an atmospheric drag function that bleeds the velocity, translating it into G-Force calculations for warnings, eventually deploying parachutes.
4.  **3D Geometry Clipping:** The `progradeMesh` vector ring is mounted at `Z: -15`. Because `renderScale` is `0.02` (every 1 unit = 50km), when the capsule is 100km above Earth, the crosshair ring physically clips 600km DEEP into the crust of the Earth mesh, causing it to visually disappear. This needs to be scaled and pulled closer to the camera.

*Check `Tasks.md` and `devlog.md` immediately upon starting for the most up-to-date tracking.*
