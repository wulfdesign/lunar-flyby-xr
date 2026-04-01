# **Artemis: The Free Return (WebXR Orbital Sandbox)**

**A browser-based, educational gravity and orbital dynamics simulator built with Three.js and WebXR.**

### **🚀 [Launch Live Experience](https://wulfdesign.github.io/lunar-flyby-xr/)**
*(No installation required. Works in modern browsers and WebXR-compatible VR headsets.)*

![LEO Orbit TMI Burn Start](Lunar-Flyby-XR_Screenshot_LEO-Orbit-TMI-BurnStart_2026-03-31.png)
*Initial Burn toward the Moon from Low Earth Orbit.*

![At the Moon](LunarFlybyXR_Screenshot_AtMoon_2026-03-31.png)
*Arriving at the Moon after a 3-day cislunar coast.*

> **🚀 Current Status (v1.9.1):** The simulation successfully achieves Trans-Lunar Injection and coast. Currently, the physics engine "stops" or resets warp upon entering the Lunar Sphere of Influence (SOI). This is the top priority for the V2.0 roadmap to allow for full flybys and Earth returns.

## **🚀 The Vision**

*Artemis: The Free Return* was conceived to make orbital mechanics accessible, intuitive, and awe-inspiring without intimidating the user with complex mathematics.

Originally inspired by a proposal for the now-canceled *dearMoon* project and timed to celebrate NASA's historic Artemis missions, this project places everyday people in the commander's seat of a spacecraft in Low Earth Orbit (LEO). It proves that you don't need a multi-billion dollar budget to reach the stars—you just need curiosity and a browser.

## **🛠️ Features**

This isn't a pre-rendered animation; it's a living physics sandbox.

* **Real Newtonian Physics:** Powered by a custom Velocity Verlet integration engine using real-world units (kilometers, kilograms, seconds) and true N-body gravity (Earth and Moon).  
* **Orbital Energy Targeting:** The flight computer calculates Trans-Lunar Injection (TLI) burns using the Vis-viva equation and orbital energy, not just preset timers.  
* **Dynamic Telemetry HUD:** Real-time G-Force, relative velocity, altitude, and fuel mass-flow calculations.  
* **Time Warp System:** Accelerate time up to 3,600x to cross the 3-day cislunar gap.  
* **WebXR Support:** Instantly jump into an immersive VR headset view directly from the browser.  
* **Flight Data Logging:** Export your mission telemetry to a .json file for post-flight analysis.

## **🛠️ Tech Stack**
- **Engine:** Three.js (r128)
- **Physics:** Custom Velocity Verlet Integration
- **Frontend:** Vanilla HTML5/CSS3 (No Tailwind/Bootstrap)
- **Immersion:** WebXR API (VR Support)

## **📜 History**
This project began as an AI-assisted rapid prototype session on March 30-31, 2026. After a successful iteration process, the source code was rescued from a browser canvas glitch and reconstructed into this repository to serve as a foundation for further development of educational space simulations.

## **💻 How to Run**

This project is currently completely self-contained in a single file for maximum accessibility.

1. Clone or download this repository.  
2. Double-click index.html to open it in any modern web browser.  
3. (Optional) Put on a WebXR-compatible headset (like the Meta Quest) and click "ENTER VR FLYBY".

## **⭐ Attribution & Giving Credit**

If you use this project for your own research, education, or as a base for your own work, we'd love to see it! 

*   **Credit:** Please credit **Larry James (Wulf Design Studios / UpLiftVR Studios)** in any public-facing descriptions or presentations.
*   **Tag Us:** Tag us on social media so we can share your progress with the community!
    *   **LinkedIn:** [WulfDesignStudios](https://linkedin.com/in/WulfDesignStudios)
    *   **YouTube:** [UpLiftVR Studios](https://www.youtube.com/@UpLiftVR)
*   **Clone & Fork:** If you fork or clone this repository, please keep the attribution and license files intact.

## **🗺️ V2.0 Roadmap**

* \[ \] **Bug Investigation:** Time warp seems to halt/reset repeatedly when deep inside the Lunar Sphere of Influence. Need to refine the SOI trigger latch.  
* \[ \] **Mid-Course Correction (MCC):** Add an "Off Course Detected" warning and a "Recalculate Destination" button to execute a burn midway to the Moon if alignment drifts.  
* \[ \] **Trajectory Trails:** Render the actual path flown (white line) vs projected path (blue dotted line).  
* \[ \] **Overview Map:** A 3/4 top-down orthographic minimap overlay showing Earth, Moon, and ship position.  
* \[ \] **Post-Flight Report:** After flyby/crash, generate a UI report showing Max Gs, flight time, and fuel remaining.  
* \[ \] **Lagrangian Points (L1-L4):** Add invisible targets/markers to the raycaster for L1 (between Earth/Moon), L2 (behind Moon), etc.  
* \[ \] **Lunar Orbit Insertion (LOI):** Add capability to do a retrograde burn at perilune to establish Lunar Orbit instead of a Free Return.  
* \[ \] **Asset Upgrades:** Replace procedural geometry with high-res NASA .glb models for the Orion capsule and SLS.

## **🏆 Completed Ready to Archive**

## **👨‍🚀 About the Creator**

**Larry James (WulfDesignStudios / UpLiftVR Studios)** is an indie VR developer, filmmaker, and space enthusiast with a passion for using immersive technology to make complex science accessible and awe-inspiring.

### **🌑 Featured Project: High Desert Eclipse**
One of Larry's most impactful works is **"High Desert Eclipse,"** a 360-degree VR documentary capturing the majestic 2017 total solar eclipse from a remote hilltop in the Oregon high desert. 

*   **For Educators & Schools:** This experience is a powerful tool for Earth and Space science. It captures the eerie transition from day to twilight, the 360-degree "sunrise" on the horizon, and the breathtaking solar corona.
*   **Watch for Free:** The 4K 360-degree timelapse is available on YouTube. **Tip:** For the best quality, especially in a VR headset, set the playback speed to **0.25x**. This allows the 4K stream to buffer smoothly and lets you soak in the subtle environmental changes.
    *   [📺 Watch: High Desert Eclipse (YouTube)](https://youtu.be/fzcFw_33iC8)
*   **Immersive Edition:** A full-length version is available for the **Meta Quest** (via App Lab) and on [upliftvr.itch.io](https://upliftvr.itch.io/). It's a perfect addition to classroom VR kits to bring a "once-in-a-lifetime" celestial event to students anywhere.

### **🚀 The Vision Behind Artemis: The Free Return**
This project represents a "lifetime vision finally fulfilled." Inspired by a proposal for the (now canceled) *dearMoon* project, it leverages the latest in WebXR and AI-assisted development to create a prototype that is "quicker and more accessible than ever before in history." 

Larry's goal is to inspire the next generation of space explorers and to remind those who have seen a total eclipse of the magic—and for those who haven't, to provide the impetus to get into the path of the next one.

*   [🎥 Evening Magazine Feature (UpLiftVR)](https://www.youtube.com/watch?v=Xh0l8hA9y0c)
*   [🎬 FilmFreeway: Larry James](https://filmfreeway.com/LarryJames)
*   [🔗 LinkedIn: WulfDesignStudios](https://linkedin.com/in/WulfDesignStudios)