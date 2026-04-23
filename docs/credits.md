# 🎖️ Project Credits & Resources

This project leverages open-source technology, NASA scientific data, and historical mission research to provide an accurate and educational orbital simulation.

## 🛠️ Tech Stack & Engine
*   **Engine:** [Three.js (r128)](https://threejs.org/) - A cross-browser JavaScript library and application programming interface used to create and display animated 3D computer graphics in a web browser using WebGL.
*   **Platform:** [WebXR Device API](https://www.w3.org/TR/webxr/) - Providing the foundation for immersive VR experiences directly in the browser.
*   **Development:** AI-assisted rapid prototyping using Google Gemini 1.5 Pro and Gemini CLI.

## 🌍 Textures & Visual Assets
*   **Earth Texture:** [Three-Globe / Earth Blue Marble](https://unpkg.com/three-globe/example/img/earth-blue-marble.jpg)
*   **Moon Texture:** [Three.js official planet textures](https://raw.githubusercontent.com/mrdoob/three.js/master/examples/textures/planets/moon_1024.jpg)
*   **Starfield:** Procedurally generated using `THREE.BufferGeometry` and `THREE.Points` for maximum performance in VR.
*   **Sun & Cockpit:** Procedurally generated geometry.

## 🚀 Scientific Research & Data
*   **NASA Artemis Program:** Official mission profiles and telemetry targets sourced from [NASA Artemis](https://www.nasa.gov/specials/artemis/).
*   **NASA Scientific Visualization Studio (SVS):** Reference for the [CGI Moon Kit](https://svs.gsfc.nasa.gov/4720) and high-resolution lunar mapping.
*   **Orbital Mechanics:** Physics calculations (Vis-viva equation, Delta-V) cross-referenced with:
    *   [Wikipedia: Orbital Mechanics](https://en.wikipedia.org/wiki/Orbital_mechanics)
    *   [Wikipedia: Trans-Lunar Injection](https://en.wikipedia.org/wiki/Trans-lunar_injection)
*   **Physics Engine:** [Velocity Verlet Integration](https://en.wikipedia.org/wiki/Verlet_integration) used for energy-stable multi-day orbital rendering.
*   **Reentry Dynamics:** Atmospheric drag modeled directly using the [Barometric Formula (Exponential Density)](https://en.wikipedia.org/wiki/Barometric_formula) and the [Drag Equation](https://en.wikipedia.org/wiki/Drag_equation) for realistic 2-degree keyhole calculations.

## 🎞️ Historical & Creator Credits
*   **Creator:** Larry James (Wulf Design Studios / UpLiftVR Studios)
*   **Inspiration:** 
    *   [dearMoon Project](https://dearmoon.earth/): The private lunar mission proposal that served as the original impetus for this simulation.
    *   [High Desert Eclipse](https://youtu.be/fzcFw_33iC8): Larry James' 360-degree VR documentary of the 2017 total solar eclipse.
    *   [UpLiftVR 'Maiden Flight'](https://www.king5.com/video/entertainment/television/programs/evening/dive-deep-into-virtual-reality-at-the-siff-vr-zone-king-5-evening/281-8137420): Experimental VR balloon ride showcased at SIFF 2018.

## 🔊 Audio (Planned/Future)
*   *Note: Audio implementation is currently in the V2.0 roadmap. Future credits will include NASA's public domain mission control audio and ambient space soundscapes.*
