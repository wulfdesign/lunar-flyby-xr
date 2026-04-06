# 🛰️ Artemis II Telemetry: NASA AROW & OEM Data Research

> **Objective:** Map real-world Artemis II flight data into the simulation mission profile for historical replay.

## 📡 Data Source: NASA AROW (Artemis Real-time Orbit Website)
*   **Website:** [https://www.nasa.gov/specials/trackartemis/](https://www.nasa.gov/specials/trackartemis/)
*   **Format:** Often provides real-time state vectors (X, Y, Z coordinates) via a JSON endpoint.
*   **Coordinate System:** Earth-Centered Inertial (ECI) or J2000.
*   **Units:** Positions usually in **km**, velocities in **km/s**.

## 📑 Data Source: OEM (Orbit Ephemeris Message)
*   **Format:** Standardized CCSDS ASCII or XML format.
*   **Mapping:** Requires parsing a header and then a series of state vector blocks.
*   **Key Fields:**
    - `EPOCH`: Time of state (ISO 8601).
    - `X, Y, Z`: Position coordinates.
    - `X_DOT, Y_DOT, Z_DOT`: Velocity components.

## 🛠️ Implementation Strategy
1.  **JSON Parser:** Create a `loadArtemisTelemetry(data)` function in `index.html`.
2.  **Coordinate Mapping:** 
    - NASA ECI coordinates must be rotated to match the simulation's orbital plane (X-Z plane for Earth-Moon).
    - Time-stamps must be converted to **Mission Elapsed Time (MET)** relative to the Artemis II launch epoch.
3.  **Interpolation:** Use linear or cubic spline interpolation to fill gaps between 10-minute state vector samples.
4.  **Playback Hook:** Connect the telemetry data to the `playbackActive` engine, overriding the physics solver with the NASA state-vectors.

## 📝 Next Steps
- [ ] Locate official Artemis II launch epoch (T=0).
- [ ] Find a sample OEM/AROW JSON file for Artemis I (to use as a baseline).
- [ ] Map J2000 (NASA) to simulation coordinates (likely a Y-axis up or Z-axis up adjustment).
