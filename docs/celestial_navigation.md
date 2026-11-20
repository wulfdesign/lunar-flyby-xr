# 🧭 Celestial Optical Navigation (OpNav) & Space Sextant Triangulation

> **How Do Spacecraft Know Where They Are in Deep Space?**  
> *From Apollo's Command Module Optical Unit to Modern Autonomous Star Trackers & CubeSat OpNav — and the Upcoming Artemis: Lunar Flyby XR Space Sextant Minigame.*

---

## 1. Why Stars Alone Tell You *Orientation*, Not *Position*

During *Artemis: Lunar Flyby XR*, the stars in the sky dome (`J2000 Equatorial Coordinates` for the 59 brightest Apollo Navigational Stars including Sirius, Canopus, Vega, Rigel, and Polaris) are locked at optical infinity (`celestialGroup.position.copy(shipGroup.position)`).

Even the closest star system to Earth, **Alpha Centauri**, sits **4.24 light-years** ($4.01 \times 10^{13}\text{ km}$) away. Moving all the way from Earth to the Moon ($384,400\text{ km}$) produces a stellar parallax shift of only:

$$\Delta \theta_{\text{parallax}} \approx \frac{384{,}400\text{ km}}{4.01 \times 10^{13}\text{ km}} \approx 9.6 \times 10^{-9}\text{ rad} \approx 0.002\text{ arcseconds}$$

Because fixed stars show practically **zero parallax** inside the Earth–Moon system:
1. **Stars cannot directly measure your distance $(x, y, z)$ from Earth.**
2. **Instead, stars provide a rock-solid 3-axis Inertial Attitude Reference Frame ($\mathbf{q}_{\text{inertial}}$).** By matching two or more cataloged stars (for instance, **Apollo Nav Star #18 Sirius** and **Canopus**), the spacecraft knows the exact orientation of its optical camera/sextant in J2000 heliocentric/geocentric coordinates to within arcseconds.

---

## 2. How Spacecraft Determine 3D Position $\mathbf{r}(t)$ in Cislunar Space

To triangulate **where** you are without GPS (which stops working cleanly above Medium Earth Orbit) or Earth-based Deep Space Network (DSN) Doppler ranging during radio blackout, spacecraft combine star attitudes with **nearby solar system bodies** (Earth, the Moon, the Sun, and the bright naked-eye planets):

### A. Star-to-Landmark / Star-to-Horizon Sextant Angles ($\theta_1, \theta_2$)
This was the core job of the **Apollo Command Module Optical Unit** (1x Scanning Telescope + 28x Space Sextant):
1. The Navigator sights a **foreground body limb or lunar crater** in one eyepiece and superimposes a **known Apollo Nav Star** (with fixed J2000 unit vector $\hat{\mathbf{s}}_1$) in the second eyepiece.
2. Measuring the angular separation $\theta_1$ between $\hat{\mathbf{s}}_1$ and the foreground body's direction $\hat{\mathbf{u}}_{\text{body}}$ places the spacecraft on a 3D cone around $\hat{\mathbf{s}}_1$.
3. Repeating the sight against a second non-collinear star $\hat{\mathbf{s}}_2$ yields angle $\theta_2$, defining a second cone. The intersection of those two cones + coarse range resolves the exact 3D line-of-sight unit vector $\hat{\mathbf{u}}_{\text{body}}$ relative to Earth or the Moon!

### B. Apparent Angular Diameter Rangefinding ($\alpha$)
Once you know the unit direction $\hat{\mathbf{u}}_M$ toward the Moon (radius $R_M = 1{,}737\text{ km}$) or $\hat{\mathbf{u}}_E$ toward Earth (radius $R_E = 6{,}371\text{ km}$), measuring its apparent angular diameter $\alpha$ in the telescope reticle directly solves the radial distance $d$:

$$d_{\text{center}} = \frac{R_{\text{body}}}{\sin(\alpha / 2)}$$

Multiplying distance by the negative line-of-sight vector yields a direct 3D Cartesian position fix relative to that body:

$$\mathbf{r}_{\text{craft}} = -d_E \cdot \hat{\mathbf{u}}_E$$

### C. Multi-Body Cross-Fix + Ephemeris Clock (`MET`)
Because the Moon (`moonAngle(t)`) and planets (`Venus, Mars, Jupiter, Saturn, Mercury`) move along precisely known Keplerian/ephemeris tables indexed by **Mission Elapsed Time (`MET`)**:
- Sighting the **direction vector to Earth ($\hat{\mathbf{u}}_E$)** and the **direction vector to the Moon ($\hat{\mathbf{u}}_M$)** at known `MET` triangulates the triangle $(\text{Earth}, \text{Moon}, \text{Spacecraft})$ without even needing Earth-based radar!
- **NASA's Artemis I & Orion Optical Navigation (OpNav)** and modern autonomous deep-space CubeSats automate this exact technique by thresholding lunar limb pixels against background stars to maintain independent trajectory verification all the way to splashdown.

---

## 3. Future Interactive Roadmap: Space Sextant & OpNav Minigame Mission

Coming to a future Expansion Pack & Training Module of *Artemis: Lunar Flyby XR*:
1. **Manual Blackout Navigation Challenge ("Telemetry Jammed"):** Mid-way through Trans-Lunar Coast, telemetry readouts (`Alt (Earth)`, `Dist (Moon)`, `Vx/Vy/Vz`) go offline.
2. **Space Sextant Sighting Loop:**
   - Pan your reticle and click **Lock Reference Star #1** (e.g. `Sirius α CMa` or `Rigel β Ori`).
   - Lock **Reference Star #2** (e.g. `Canopus` or `Polaris`).
   - Sight the **Lunar Limb** or **Earth Horizon** and pinch the optical rangefinder ring to measure apparent angular diameter $\alpha$.
3. **Solve Your Own State Vector:** Watch the onboard Apollo Guidance Computer overlay compute your 3D position $\mathbf{r}(t)$, cross-check your Mid-Course Correction (MCC) corridor error, and award the **Master Celestial Navigator** achievement!
