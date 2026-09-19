# 🛡️ Last Known Good (LKG) Hardware Snapshots Archive

This directory maintains immutable, hardware-verified baseline snapshots of *Artemis: The Free Return* (Lunar Flyby XR).

If any experimental build or showcase feature regression introduces rendering anomalies, WebXR session dropouts, or mobile viewport clipping, operators can instantly restore an empirically verified baseline build.

---

## 📦 Snapshot Catalog (v2.1.4 Baseline)

### 1. 2.1.4_baseline_public.html
- **Role:** Exact byte-for-byte duplicate of the public production root index.html as of commit 811215e / 823073e.
- **Status:** Verified baseline with Newtonian N-body Velocity Verlet physics, 9 warp gears, automated decelerator, and mobile 0.73 grid layout.

### 2. hardware_profiles/quest3_webxr_lkg_v2.1.4.html
- **Target Hardware:** Meta Quest 3 / Quest Pro / Quest 2 (Meta Quest Browser v65+).
- **Display Mode:** WebXR Immersive-VR with local-floor and DOM Overlay.
- **Port:** Local demo server on port 3550 (http://<LAN_IP>:3550).
- **Verified Behaviors:**
  - Zero InvalidStateError on session launch.
  - Clean session.addEventListener('end') teardown preventing cancelAnimationFrame crash.
  - Primary controller trigger binds to manual burn; secondary controller trigger binds to target lock.
  - VR entrance buttons forced behind DOM overlay dialogs to prevent accidental input stealing.

### 3. hardware_profiles/desktop_chrome_edge_lkg_v2.1.4.html
- **Target Hardware:** Desktop PC / Mac / Laptop running Chrome, Edge, Brave, or Firefox.
- **Display Mode:** Standard WebGL Canvas with high-performance antialiasing and logarithmic depth buffer.
- **Verified Behaviors:**
  - 60+ FPS at 1080p / 1440p / 4K.
  - Mouse look, mouse-wheel FOV zoom (10° to 100°), prograde raycasting, and HUD telemetry panels.

### 4. hardware_profiles/mobile_touch_ios_android_lkg_v2.1.4.html
- **Target Hardware:** Apple iPhone (Safari iOS 17+) and Android devices (Chrome / Samsung Internet).
- **Display Mode:** Responsive CSS Grid with 	ransform: scale(0.73) top-left anchor.
- **Verified Behaviors:**
  - All 3 telemetry and control quadrants fit on small viewports without overlapping or cut-off buttons.
  - Multi-touch drag navigation with passive event handlers.

---

## 🔄 Emergency Rollback Procedure

To roll back the production or development build to any snapshot:
\\powershell
# To roll back active development copy:
Copy-Item snapshots\hardware_profiles\quest3_webxr_lkg_v2.1.4.html dev\index.html

# To roll back public production copy:
Copy-Item snapshots2.1.4_baseline_public.html index.html
\
