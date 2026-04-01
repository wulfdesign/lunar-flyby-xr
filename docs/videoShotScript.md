# 🎬 Cinematic Video Shot Script

> **Status:** [⚠️ WORK IN PROGRESS]
> **Objective:** Automate simulation controls (TMI autopilot, time warp, camera rotation) to produce a cinematic, high-impact 4K screen recording.

---

## 🚀 Shot 01: "The Cislunar Crossing" (Sequence Parameters)

**Goal:** A continuous shot from LEO to the first close-up of the Moon.

### **Phase 1: Pre-Launch & TMI Ignition**
1.  **State:** Ship is in stable 400km LEO.
2.  **Action:** Enable **TMI Autopilot** (Commander Latch).
3.  **Warp:** Speed up (e.g., 10x) for the final 2-minute countdown.
4.  **Transition:** Slow down to **1x real-time** for the initial 15-30 seconds of the TMI burn (engine glow and G-force peak).
5.  **Thrust:** Maintain burn, slowly increase warp to **10x** as the ship moves away from Earth.

### **Phase 2: Earth Departure & Coasting**
6.  **State:** Burn complete, ship entering high-elliptical trajectory.
7.  **Warp:** Incrementally increase to **100x** then **1000x**.
8.  **Transition:** As we approach **Geostationary Orbit (GEO)** altitude (approx. 35,786 km), slow warp to **10x** to see the Earth recede.
9.  **Action:** Slowly rotate viewport 180° to point toward the Moon.
10. **Warp:** Re-engage **1000x** or **3600x** (max warp) for the long cislunar coast.

### **Phase 3: Lunar Arrival**
11. **State:** Approaching the Moon's Sphere of Influence (SOI).
12. **Warp:** Incrementally slow down (**100x -> 10x -> 1x**).
13. **Action:** Focus on the Moon's details (craters, lunar seas) as they fill the frame.
14. **Final:** Stop at the exact moment of entering the **Lunar Flyby** phase.

---

## 🎞️ Alternate: "Blink" Method
If the continuous sequence exceeds 1-2 minutes:
*   Use fade-to-black ("Blinks") to skip large chunks of the 3-day coasting phase.
*   **Scene A:** TMI Burn ignition.
*   **Scene B:** Earth-receding view from GEO.
*   **Scene C:** Lunar SOI entrance.

---

## 📝 Automation Parameters (For Future Scripting)
*   `autopilot_tmi_enable = true`
*   `warp_schedule = [(0s, 10x), (120s, 1x), (150s, 10x), (500s, 1000x)]`
*   `camera_rotation_rate = 0.5 deg/sec` (Smooth transition to Moon-facing view)
