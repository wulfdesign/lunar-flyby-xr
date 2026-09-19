---
name: cislunar-flight-engine
description: >-
  Comprehensive guide, equations, and operational workflows for real-time Newtonian cislunar WebXR simulations,
  including 3-tier warp safety gating, continuous Hermite time-warp transitions, atmospheric guidance,
  and empirical telemetry verification.
---

# 🚀 Cislunar Flight Engine & WebXR Simulation Skill

This skill provides architectural patterns, physical equations, time-warp stepping algorithms, and verification procedures for high-fidelity, real-time celestial simulations across the Symbiot AI Ecology (e.g. *Artemis: The Free Return*, *NearStarXR*, *UpLiftVR*).

---

## 🎯 When to Use This Skill

Activate this skill when:
1. **Calibrating Time Warp Schedules:** Designing or tuning simulation speed regimes ($1\times$ to $7,200\times$) to balance real-time pacing with numerical integration stability.
2. **Preventing WebXR Cybersickness:** Enforcing smooth, continuous ease-in/ease-out transitions between time warps without instantaneous visual tearing or angular velocity shocks.
3. **Implementing Gravity & Orbital Mechanics:** Configuring Newtonian $N$-body gravity, Velocity Verlet integration, ephemeris propagation, or patched conic approximations.
4. **Engineering Atmospheric Guidance:** Modeling lifting-body re-entry, bank-angle lift vectoring, trim damping, and multistage parachute descent.
5. **Analyzing Flight Telemetry:** Validating empirical flight logs (`Artemis_FlightLog_*.json`), verifying energy conservation, minimum perilune clearance, and mission duration speedruns.

---

## 🔬 Core Physics & Mathematical Specifications

### 1. Newtonian $N$-Body Velocity Verlet Integration
For a spacecraft of mass $m$ experiencing simultaneous gravitational pull from Earth ($M_e$) and Moon ($M_m$):
$$\mathbf{a}_{\text{net}} = -G M_e \frac{\mathbf{r}_e}{\|\mathbf{r}_e\|^3} - G M_m \frac{\mathbf{r}_m}{\|\mathbf{r}_m\|^3} + \frac{\mathbf{F}_{\text{thrust}} + \mathbf{F}_{\text{aero}}}{m}$$

Numerical integration evaluates in dual half-steps:
$$\mathbf{r}(t + \Delta t) = \mathbf{r}(t) + \mathbf{v}(t)\Delta t + \frac{1}{2}\mathbf{a}(t)\Delta t^2$$
$$\mathbf{v}(t + \Delta t) = \mathbf{v}(t) + \frac{1}{2}\left[\mathbf{a}(t) + \mathbf{a}(t + \Delta t)\right]\Delta t$$

**Adaptive Step Sizing:**
To prevent artificial energy injection during high-speed flybys:
- High proximity ($\|\mathbf{r}_m - R_m\| < 12,000\text{ km}$ or $\|\mathbf{r}_e - R_e\| < 1,000\text{ km}$): $\Delta t_{\text{base}} = 0.01\text{ s}$.
- Deep space cruise: $\Delta t_{\text{base}} = 0.05\text{ s}$.

---

### 2. Continuous Cubic Hermite Smoothstep Gliding
Instantaneous speed changes trigger severe kinetosis in 6DoF WebXR headsets. All speed changes must glide continuously across a 1.0-second window:
$$p = \min\left(1.0, \frac{\Delta t_{\text{transition}}}{\tau_{\text{interval}}}\right)$$
$$\text{ease}(p) = 3p^2 - 2p^3$$
$$\text{smoothWarp} = W_{\text{start}} + (W_{\text{target}} - W_{\text{start}}) \cdot \text{ease}(p)$$
$$\Delta t_{\text{sim}} = \Delta t_{\text{real}} \cdot \text{smoothWarp}$$

---

## 🛡️ The 3-Tier Warp Safety Framework

| Tier | Visual Indicator | Condition | Operational Rule |
| :--- | :--- | :--- | :--- |
| **Tier 1 (Safe)** | 🟢 **Green** | $\text{speed} \le \text{maxSafeWarp}$ | Fully safe for physical integration. Auto-Warp automatically engages this tier. |
| **Tier 2 (Advisory)** | 🟡 **Yellow** | $\text{maxSafeWarp} < \text{speed} \le \text{maxAdvisoryWarp}$ | Permitted under pilot manual command. Auto-Warp honors human intent (`userSelectedWarp`). |
| **Tier 3 (Locked)** | 🔴 **Red** | $\text{speed} > \text{maxAdvisoryWarp}$ | Strictly disabled in UI and physics loop to prevent integrator divergence. |

---

## 🗺️ Calibrated Artemis II Free-Return Flight Envelope

Targeting **~16–17 minutes** total simulation duration from launch to ocean splashdown:

```text
1. LEO PARKING ORBIT (400 km) ──► Safe: 30x Green (Burns locked <= 30x)
2. POST-BURN OBSERVATION       ──► 1x Hold for 6 seconds post-MECO
3. OUTBOUND CLIMB             ──► 1.2k km: 300x | 4k km: 600x | 10k km: 1.8kx | 22k km: 3.6kx
4. DEEP SPACE OUTBOUND        ──► altE > 45k km, distM > 70k km: 7200x (7.2kx) Green Cruise
5. LUNAR APPROACH             ──► 70k km: 3.6kx | 42k km: 1.8kx | 22k km: 600x | 12k km: 300x
6. PERILUNE SIZZLE SHOT       ──► distM <= 5,500 km: 60x Green (Cinematic Flyby)
7. LUNAR DEPARTURE            ──► 5k km: 300x | 10k km: 600x | 22k km: 1.8kx | 42k km: 3.6kx
8. DEEP SPACE INBOUND         ──► distM > 70k km, altE > 150k km: 7200x (7.2kx) Green Cruise
9. EARTH RETURN WELL          ──► 150k km: 1.8kx | 100k km: 600x | 50k km: 300x | 25k km: 60x | 1.5k km: 30x | 200 km: 10x
10. ENTRY INTERFACE (122 km)  ──► 1x Locked (12.3G plasma deceleration)
11. SUBSONIC DESCENT (35-8.5km)──► 10x Auto-Ramped Green
12. DROGUE DEPLOY (8.5-7.3km) ──► 1x Locked (~10s observation window)
13. UNDER DROGUES (7.3-3.4km) ──► 10x Auto-Ramped Green
14. MAIN DEPLOY (3.4-3.0km)   ──► 1x Locked (~15s observation window)
15. UNDER MAINS (3.0-0.35km)  ──► 10x Auto-Ramped Green
16. TOUCHDOWN (<= 0.35km)     ──► 1x Locked (~18s touchdown window)
```

---

## 🔍 Telemetry & Flight Log Verification Workflow

1. Telemetry logs are stored as JSON under `projects/lunar-flyby-xr/logs/Artemis_FlightLog_YYYY-MM-DDTHH-mm-ss.json`.
2. Inspect flight duration:
   `node -e "const log = require('./logs/...json'); console.log('Flight Time:', log.sim_flight_time);"`
3. Verify orbital energy conservation across lunar flyby:
   $$\epsilon = \frac{1}{2}v^2 - \frac{G M_m}{r_m}$$
   Ensure $\Delta \epsilon / \epsilon_0 < 10^{-4}$ throughout closest perilune pass.
