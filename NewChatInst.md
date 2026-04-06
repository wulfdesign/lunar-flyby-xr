# 🧠 New Chat Instructions (Memory Boot)

> **Context:** This file is read by the AI at the start of a new session to restore project state and mission intent without relying on chat history.

## 🛰️ Current Mission Status (v1.9.5)
- **Baseline:** Stable baseline for public release. Manual TLI and flyby are functional.
- **Architecture:** Single-file `index.html` using Three.js (r128) and custom Velocity Verlet integration.
- **Logging:** High-fidelity JSON logging in `/logs` capturing raw MET, Warp, and X,Y,Z coordinates.
- **Controls:** 9-speed gear-shifting warp system (1x to 7.2kx).

## 🛠️ Active Work Tracks (Priority)
1. **Quest 3 Optimization:** Resolve WebXR session entry errors and map controller inputs.
2. **Mobile Readiness:** Responsive HUD design and touch-drag navigation.
3. **Artemis II Telemetry:** Reverse-engineer NASA AROW data for real-world mission replay.
4. **Physics Check:** Verify the "Lunar Keyhole" maths for 100% reliable free-return capture.

## 🛡️ Foundational Mandates (CRITICAL)
- **NEVER** push to GitHub without explicit user confirmation.
- **NEVER** overwrite stable v1.9.5 logic without a verified test run.
- **Surgical Edits:** Use `replace` or `read_file` with line numbers to avoid context blowup.
- **Safety Suppression:** The 1x warp reset at Lunar SOI is suppressed in professional modes (Playback/Cine).

## 📂 Directory Structure
- `/logs`: Mission telemetry JSON records.
- `/debug`: Recovery HTML artifacts and rescue chat logs.
- `/docs`: Artemis mission research and video scripts.
- `/private`: Confidential roadmap, NorWesCon notes, and social media post drafts.

## 📡 Social Strategy
- Reddit outreach plan is ready in `private/SocialMedia/` with 18+ target communities identified.
- Cross-promotion with *High Desert Eclipse 360* is integrated into outreach.
