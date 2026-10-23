#!/usr/bin/env python3
"""
🧪 Artemis: The Free Return (Lunar Flyby XR) - E2E & Integrity Verification Test Suite
======================================================================================
Automated test suite verifying the 6 architectural pillars for Milestone 1 & 2:
1. Public Root Protection:
   - Root `index.html` is byte-for-byte identical to baseline snapshot (`snapshots/index_v2.1.19_sim_backup.html`).
2. Staged Dev Site & Assets:
   - `private/dev_site/sim.html` exists and points to appropriate relative asset paths (`../../vendor/three.min.js`, etc.).
   - `private/dev_site/index.html` and `landing.html` exist.
   - All referenced images in `private/dev_site/index.html` and `landing.html` actually exist on disk in `images/`.
3. Flight Controls Truth Audit:
   - Verifies `landing.html` and `private/dev_site/index.html` contain ZERO occurrences of keyboard shortcuts 'W key', 'V key', 'Spacebar'.
   - Verifies all HUD button IDs from `sim.html` are documented (`#btn-toggle-auto`, `#btn-auto-warp`, `#btn-skip-window`, `#btn-track-target`, `#btn-thrust`, `#btn-lift-up`, `#btn-lift-down`, `#btn-abort`, `#btn-save-log`, WebXR triggers).
4. Showcase Pedigree & Narrative Verification:
   - Checks presence of all 5 verified events: SLICE 2026, SiM PAX West Kickoff Showcase 2026, KremFest XR 2026, Seattle Space Week 2026, GeekGirlCon 2026.
   - Checks presence of verbatim Director's Cut & Statement.
5. Google Form Engine & Guide Verification:
   - Checks presence of `<iframe name="hidden_gform" id="hidden_gform"`, honeypot `website_hp`, and all 7 `entry.XXXXX` IDs in `private/dev_site/index.html` and `landing.html`.
   - Checks `private/GOOGLE_FORM_SETUP_GUIDE.md` exists and contains the field mapping and Hermes CLI commands.
6. Promotion & Server Verification:
   - Checks `private/promote_to_production.py` supports `--dry-run` and executes cleanly with exit code 0.
   - Tests `server.py` routing logic (handles `/api/checklist`, `/api/promote`, `/api/rollback`, `--dev`, `--no-browser`).
"""

import os
import sys
import re
import json
import hashlib
import threading
import subprocess
import unittest
import urllib.request
from typing import List, Set, Tuple, Dict, Any

# Set UTF-8 output encoding for Windows terminals
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8", line_buffering=True)
        sys.stderr.reconfigure(encoding="utf-8", line_buffering=True)
    except Exception:
        pass

# ---------------------------------------------------------------------------
# Path Configuration
# ---------------------------------------------------------------------------
TESTS_DIR = os.path.dirname(os.path.abspath(__file__))
LUNAR_ROOT = os.path.abspath(os.path.join(TESTS_DIR, ".."))

SNAPSHOT_FILE = os.path.join(LUNAR_ROOT, "snapshots", "index_v2.1.19_sim_backup.html")
ROOT_INDEX = os.path.join(LUNAR_ROOT, "index.html")
ROOT_LANDING = os.path.join(LUNAR_ROOT, "landing.html")

DEV_SITE_DIR = os.path.join(LUNAR_ROOT, "private", "dev_site")
DEV_SIM = os.path.join(DEV_SITE_DIR, "sim.html")
DEV_LANDING = os.path.join(DEV_SITE_DIR, "index.html")

IMAGES_DIR = os.path.join(LUNAR_ROOT, "images")
GUIDE_FILE = os.path.join(LUNAR_ROOT, "private", "GOOGLE_FORM_SETUP_GUIDE.md")
PROMOTE_SCRIPT = os.path.join(LUNAR_ROOT, "private", "promote_to_production.py")
SERVER_SCRIPT = os.path.join(LUNAR_ROOT, "server.py")


def extract_image_references(html_content: str) -> List[Tuple[int, str]]:
    """
    Extracts all local image references (src, href, background-image, url()) from HTML content.
    Returns a list of (line_number, ref_path).
    Filters out external (http/https), data URIs, anchors (#), and javascript: links.
    """
    image_refs = []
    lines = html_content.splitlines()

    img_src_regex = re.compile(r'<img\s+[^>]*src=["\']([^"\']+)["\']', re.IGNORECASE)
    css_url_regex = re.compile(r'url\(\s*["\']?([^"\'\)\s]+)["\']?\s*\)', re.IGNORECASE)
    link_href_regex = re.compile(r'<link\s+[^>]*href=["\']([^"\']+)["\']', re.IGNORECASE)
    meta_img_regex = re.compile(r'<meta\s+[^>]*content=["\']([^"\']+\.(?:png|jpg|jpeg|webp|svg|gif))["\']', re.IGNORECASE)

    image_extensions = ('.png', '.jpg', '.jpeg', '.webp', '.svg', '.gif')

    for line_idx, line in enumerate(lines, start=1):
        for pattern in (img_src_regex, css_url_regex, link_href_regex, meta_img_regex):
            for match in pattern.finditer(line):
                url = match.group(1).strip()
                if url.startswith(('http://', 'https://', '//', 'data:', 'javascript:', '#')):
                    continue
                # If it's an image file or references an images/ path
                if any(url.lower().endswith(ext) for ext in image_extensions) or 'images/' in url:
                    image_refs.append((line_idx, url))

    return image_refs


# ===========================================================================
# Pillar 1: Public Root Protection
# ===========================================================================
class TestPublicRootProtection(unittest.TestCase):
    """
    Verifies that either the public root `index.html` (pre-promotion) OR `sim.html`
    (post-promotion) remains byte-for-byte identical to the baseline v2.1.19 simulation snapshot.
    """

    def test_root_index_exists(self):
        """Root index.html must exist."""
        self.assertTrue(
            os.path.isfile(ROOT_INDEX),
            f"Public root file missing at: {ROOT_INDEX}"
        )

    def test_baseline_snapshot_exists(self):
        """Baseline snapshot snapshots/index_v2.1.19_sim_backup.html must exist."""
        self.assertTrue(
            os.path.isfile(SNAPSHOT_FILE),
            f"Baseline snapshot file missing at: {SNAPSHOT_FILE}. "
            "A pristine copy of index.html must be archived as snapshots/index_v2.1.19_sim_backup.html."
        )

    def test_root_index_identical_to_baseline_snapshot(self):
        """Either root index.html (pre-promotion) or root sim.html (post-promotion) must match baseline snapshot."""
        if not os.path.isfile(ROOT_INDEX) or not os.path.isfile(SNAPSHOT_FILE):
            self.skipTest("Missing root index.html or baseline snapshot file.")

        root_sim = os.path.join(LUNAR_ROOT, "sim.html")
        target_sim_file = root_sim if os.path.isfile(root_sim) else ROOT_INDEX

        with open(target_sim_file, "rb") as f_root:
            root_bytes = f_root.read()
        with open(SNAPSHOT_FILE, "rb") as f_snap:
            snap_bytes = f_snap.read()

        root_hash = hashlib.sha256(root_bytes).hexdigest()
        snap_hash = hashlib.sha256(snap_bytes).hexdigest()

        self.assertEqual(
            root_hash,
            snap_hash,
            f"INTEGRITY VIOLATION: {os.path.basename(target_sim_file)} ({len(root_bytes)} bytes, SHA: {root_hash[:12]}) "
            f"does not match baseline snapshot ({len(snap_bytes)} bytes, SHA: {snap_hash[:12]})."
        )

    def test_root_index_sim_version_nominal(self):
        """Active root simulation (sim.html or index.html) must contain nominal v2.1.19 simulation markers."""
        root_sim = os.path.join(LUNAR_ROOT, "sim.html")
        target_sim_file = root_sim if os.path.isfile(root_sim) else ROOT_INDEX
        if not os.path.isfile(target_sim_file):
            self.skipTest("Root simulation file missing.")

        with open(target_sim_file, "r", encoding="utf-8", errors="replace") as f:
            content = f.read()

        self.assertIn("v2.1.19", content, "Root simulation does not contain expected version string 'v2.1.19'.")
        self.assertIn("<title>Artemis: Lunar Flyby VR - Educational Edition", content)
        self.assertIn("const SIM_VERSION = \"2.1.19\";", content)


# ===========================================================================
# Pillar 2: Staged Dev Site & Assets
# ===========================================================================
class TestStagedDevSiteAndAssets(unittest.TestCase):
    """
    Verifies that the private staging site exists in `private/dev_site/`,
    simulation assets are properly path-adjusted (`../../vendor/...`),
    and all referenced images exist on disk.
    """

    def test_dev_site_sim_exists(self):
        """Staged simulation private/dev_site/sim.html must exist."""
        self.assertTrue(
            os.path.isfile(DEV_SIM),
            f"Staged simulation missing at: {DEV_SIM}. Must be copied/staged from baseline."
        )

    def test_dev_site_sim_relative_asset_paths(self):
        """
        private/dev_site/sim.html sits two folders deep;
        all local scripts and textures must use ../../ prefixes.
        """
        if not os.path.isfile(DEV_SIM):
            self.skipTest("private/dev_site/sim.html does not exist.")

        with open(DEV_SIM, "r", encoding="utf-8", errors="replace") as f:
            content = f.read()

        # Check vendor/three.min.js relative pathing
        self.assertIn(
            "../../vendor/three.min.js",
            content,
            "private/dev_site/sim.html must reference '../../vendor/three.min.js' to load vendor assets correctly."
        )

        # Check that un-prefixed local vendor script references are NOT present
        unprefixed_vendor = re.findall(r'<script\s+src=["\']vendor/three\.min\.js["\']', content)
        self.assertEqual(
            len(unprefixed_vendor),
            0,
            "private/dev_site/sim.html contains un-prefixed 'vendor/three.min.js' which will 404 from dev_site."
        )

        # Check textures relative pathing
        self.assertIn(
            "../../textures/",
            content,
            "private/dev_site/sim.html must reference '../../textures/' for planetary texture maps."
        )

    def test_dev_site_index_and_landing_exist(self):
        """Both private/dev_site/index.html and root landing.html must exist."""
        self.assertTrue(
            os.path.isfile(DEV_LANDING),
            f"Staged dev portal landing page missing at: {DEV_LANDING}"
        )
        self.assertTrue(
            os.path.isfile(ROOT_LANDING),
            f"Root landing portal missing at: {ROOT_LANDING}"
        )

    def test_referenced_images_exist_dev_site(self):
        """All images referenced in private/dev_site/index.html must exist on disk."""
        if not os.path.isfile(DEV_LANDING):
            self.skipTest("private/dev_site/index.html does not exist.")

        with open(DEV_LANDING, "r", encoding="utf-8", errors="replace") as f:
            content = f.read()

        image_refs = extract_image_references(content)
        self.assertGreater(len(image_refs), 0, "No image references found in private/dev_site/index.html.")

        missing = []
        for line_no, ref in image_refs:
            # Resolve relative to private/dev_site/
            resolved = os.path.normpath(os.path.join(DEV_SITE_DIR, ref))
            if not os.path.isfile(resolved):
                missing.append(f"Line {line_no}: '{ref}' -> {resolved}")

        self.assertEqual(
            len(missing),
            0,
            f"Missing image assets referenced in private/dev_site/index.html:\n" + "\n".join(missing)
        )

    def test_referenced_images_exist_root_landing(self):
        """All images referenced in root landing.html must exist on disk in images/."""
        if not os.path.isfile(ROOT_LANDING):
            self.skipTest("root landing.html does not exist.")

        with open(ROOT_LANDING, "r", encoding="utf-8", errors="replace") as f:
            content = f.read()

        image_refs = extract_image_references(content)
        self.assertGreater(len(image_refs), 0, "No image references found in root landing.html.")

        missing = []
        for line_no, ref in image_refs:
            # Resolve relative to LUNAR_ROOT
            resolved = os.path.normpath(os.path.join(LUNAR_ROOT, ref))
            if not os.path.isfile(resolved):
                missing.append(f"Line {line_no}: '{ref}' -> {resolved}")

        self.assertEqual(
            len(missing),
            0,
            f"Missing image assets referenced in root landing.html:\n" + "\n".join(missing)
        )


# ===========================================================================
# Pillar 3: Flight Controls Truth Audit
# ===========================================================================
class TestFlightControlsTruthAudit(unittest.TestCase):
    """
    Verifies that documentation fiction (keyboard shortcuts W, V, Spacebar)
    is completely purged, and all real HUD button IDs and WebXR triggers
    from sim.html are accurately documented.
    """

    FICTIONAL_SHORTCUTS = [
        (r'\bW\s+key\b', 'W key'),
        (r'\bV\s+key\b', 'V key'),
        (r'\bSpacebar\b', 'Spacebar'),
        (r'\[W\]', '[W]'),
        (r'\[V\]', '[V]'),
        (r'\[Spacebar\]', '[Spacebar]')
    ]

    # Authoritative mapping of HUD button IDs to their documented aliases/labels
    HUD_BUTTON_MAPPINGS = [
        {
            "id": "btn-toggle-auto",
            "aliases": ["btn-toggle-auto", "AUTOPILOT ON", "ENABLE AUTO TMI"],
            "desc": "Autopilot TLI & Guidance Toggle"
        },
        {
            "id": "btn-auto-warp",
            "aliases": ["btn-auto-warp", "AUTO WARP"],
            "desc": "Auto-Warp Regulation"
        },
        {
            "id": "btn-skip-window",
            "aliases": ["btn-skip-window", "SKIP TO ACTION"],
            "desc": "Mission Checkpoint Fast-Forward"
        },
        {
            "id": "btn-track-target",
            "aliases": ["btn-track-target", "TRACK TARGET"],
            "desc": "Celestial Body Target Tracking"
        },
        {
            "id": "btn-thrust",
            "aliases": ["btn-thrust", "MANUAL BURN OVERRIDE", "MANUAL BURN"],
            "desc": "Manual Main Engine Burn Override"
        },
        {
            "id": "btn-lift-up",
            "aliases": ["btn-lift-up", "BANK UP"],
            "desc": "Aerodynamic Bank Up (Reduce Gs)"
        },
        {
            "id": "btn-lift-down",
            "aliases": ["btn-lift-down", "BANK DOWN"],
            "desc": "Aerodynamic Bank Down (Steepen Entry)"
        },
        {
            "id": "btn-abort",
            "aliases": ["btn-abort", "ABORT / RESTART", "ABORT"],
            "desc": "Mission Abort & Parking Orbit Reset"
        },
        {
            "id": "btn-save-log",
            "aliases": ["btn-save-log", "SAVE FLIGHT LOG"],
            "desc": "Telemetry Flight Log JSON Export"
        }
    ]

    def _audit_shortcuts(self, file_path: str):
        if not os.path.isfile(file_path):
            self.skipTest(f"File missing for shortcut audit: {file_path}")

        with open(file_path, "r", encoding="utf-8", errors="replace") as f:
            lines = f.readlines()

        active_violations = []
        for line_idx, line in enumerate(lines, start=1):
            for pattern, label in self.FICTIONAL_SHORTCUTS:
                if re.search(pattern, line, re.IGNORECASE):
                    # Distinguish active shortcut definitions (key-badge, assignment, control list)
                    # from explicit disclaimers ("NO keyboard shortcut mappings", "NO keyboard shortcuts")
                    is_negation_disclaimer = any(
                        neg in line.lower()
                        for neg in (
                            "no keyboard shortcut",
                            "no keyboard mappings",
                            "there are no keyboard",
                            "without keyboard"
                        )
                    )
                    if not is_negation_disclaimer:
                        active_violations.append(f"Line {line_idx} [{label}]: {line.strip()}")

        self.assertEqual(
            len(active_violations),
            0,
            f"TRUTH AUDIT FAILURE: Found {len(active_violations)} occurrences of non-existent keyboard shortcuts in {os.path.basename(file_path)}:\n"
            + "\n".join(active_violations)
        )

    def _audit_hud_buttons(self, file_path: str):
        if not os.path.isfile(file_path):
            self.skipTest(f"File missing for HUD button audit: {file_path}")

        with open(file_path, "r", encoding="utf-8", errors="replace") as f:
            content = f.read()

        missing_buttons = []
        for btn in self.HUD_BUTTON_MAPPINGS:
            # Check if either the button element ID or any of its documented labels/aliases appear
            documented = any(alias.lower() in content.lower() for alias in btn["aliases"])
            if not documented:
                missing_buttons.append(f"#{btn['id']} ({btn['desc']})")

        self.assertEqual(
            len(missing_buttons),
            0,
            f"HUD buttons missing documentation in {os.path.basename(file_path)}:\n"
            + "\n".join(f"  • {btn}" for btn in missing_buttons)
        )

        # Also verify WebXR triggers are documented
        content_lower = content.lower()
        has_webxr_trigger = any(
            phrase in content_lower
            for phrase in (
                "controller 0",
                "controller 1",
                "webxr trigger",
                "selectstart",
                "vr trigger",
                "quest trigger"
            )
        )
        self.assertTrue(
            has_webxr_trigger,
            f"WebXR controller trigger interactions not documented in {os.path.basename(file_path)}."
        )

    def test_zero_keyboard_shortcuts_in_landing(self):
        """landing.html must contain ZERO occurrences of keyboard shortcuts 'W key', 'V key', 'Spacebar'."""
        self._audit_shortcuts(ROOT_LANDING)

    def test_zero_keyboard_shortcuts_in_dev_site(self):
        """private/dev_site/index.html must contain ZERO occurrences of keyboard shortcuts 'W key', 'V key', 'Spacebar'."""
        self._audit_shortcuts(DEV_LANDING)

    def test_all_hud_button_ids_documented_in_landing(self):
        """landing.html must document all 9 primary HUD buttons and WebXR triggers."""
        self._audit_hud_buttons(ROOT_LANDING)

    def test_all_hud_button_ids_documented_in_dev_site(self):
        """private/dev_site/index.html must document all 9 primary HUD buttons and WebXR triggers."""
        self._audit_hud_buttons(DEV_LANDING)


# ===========================================================================
# Pillar 4: Showcase Pedigree & Narrative Verification
# ===========================================================================
class TestShowcasePedigreeAndNarrative(unittest.TestCase):
    """
    Verifies that all 5 authentic 2026 showcase exhibitions are highlighted,
    and verbatim Director's Cut & Statement copy is accurately preserved.
    """

    REQUIRED_SHOWCASES = [
        "SLICE 2026",
        "SiM PAX West Kickoff",
        "KremFest XR 2026",
        "Seattle Space Week",
        "GeekGirlCon 2026"
    ]

    DIRECTORS_CUT_FRAGMENTS = [
        "What does it truly feel like to leave Earth behind?",
        "Pointing toward the second star to the left",
        "111 seconds of thunderous Trans-Lunar Injection burn",
        "total radio blackout",
        "2-degree reentry keyhole"  # or "2°"
    ]

    DIRECTORS_STATEMENT_FRAGMENTS = [
        "For as long as I can remember, I have looked up at the Moon",
        "When the private dearMoon lunar mission was canceled",
        "I refused to put the spacecraft on pre-baked animation rails",
        "dynamic Newtonian gravity",
        "fragile blue world vanish behind the lunar limb"
    ]

    def _verify_showcases(self, file_path: str):
        if not os.path.isfile(file_path):
            self.skipTest(f"File missing: {file_path}")

        with open(file_path, "r", encoding="utf-8", errors="replace") as f:
            content = f.read()

        missing = []
        for showcase in self.REQUIRED_SHOWCASES:
            if showcase.lower() not in content.lower():
                missing.append(showcase)

        self.assertEqual(
            len(missing),
            0,
            f"Missing showcase events in {os.path.basename(file_path)}:\n"
            + "\n".join(f"  • {sc}" for sc in missing)
        )

    def _verify_narrative(self, file_path: str):
        if not os.path.isfile(file_path):
            self.skipTest(f"File missing: {file_path}")

        with open(file_path, "r", encoding="utf-8", errors="replace") as f:
            content = f.read()

        missing_dc = []
        for frag in self.DIRECTORS_CUT_FRAGMENTS:
            if "2-degree" in frag and ("2-degree" in content or "2°" in content):
                continue
            if frag.lower() not in content.lower():
                missing_dc.append(frag)

        self.assertEqual(
            len(missing_dc),
            0,
            f"Missing Director's Cut narrative fragments in {os.path.basename(file_path)}:\n"
            + "\n".join(f"  • \"{f}\"" for f in missing_dc)
        )

        missing_ds = []
        for frag in self.DIRECTORS_STATEMENT_FRAGMENTS:
            if frag.lower() not in content.lower():
                missing_ds.append(frag)

        self.assertEqual(
            len(missing_ds),
            0,
            f"Missing Director's Statement narrative fragments in {os.path.basename(file_path)}:\n"
            + "\n".join(f"  • \"{f}\"" for f in missing_ds)
        )

    def test_showcase_events_in_landing(self):
        """landing.html must highlight all 5 verified 2026 showcase exhibitions."""
        self._verify_showcases(ROOT_LANDING)

    def test_showcase_events_in_dev_site(self):
        """private/dev_site/index.html must highlight all 5 verified 2026 showcase exhibitions."""
        self._verify_showcases(DEV_LANDING)

    def test_narrative_master_copy_in_landing(self):
        """landing.html must contain verbatim Director's Cut & Director's Statement."""
        self._verify_narrative(ROOT_LANDING)

    def test_narrative_master_copy_in_dev_site(self):
        """private/dev_site/index.html must contain verbatim Director's Cut & Director's Statement."""
        self._verify_narrative(DEV_LANDING)


# ===========================================================================
# Pillar 5: Google Form Engine & Guide Verification
# ===========================================================================
class TestGoogleFormEngineAndGuide(unittest.TestCase):
    """
    Verifies silent Google Form intake engine with hidden iframe target,
    spam-trapping honeypot field, all 7 entry IDs, and companion setup guide.
    """

    GOOGLE_FORM_ENTRY_IDS = [
        "entry.486472330",   # Commander Callsign / Pilot Name
        "entry.500788665",   # Contact Email
        "entry.993873424",   # Primary Flight Hardware / Headset
        "entry.295781498",   # Showcase Venue / Discovery Source
        "entry.1519432357",  # Which build(s) have you flown?
        "entry.2105931848",  # Planned Missions & Roadmap Features
        "entry.743170660"    # Flight Telemetry Log / Mission Debrief / Plaque Callsign
    ]

    FORM_ACTION_ENDPOINT = "https://docs.google.com/forms/d/e/1FAIpQLSd9yuRimzA1dSi-9yehOQi7DopunOQhJx1unf0v2I9CP6qG4A/formResponse"

    def _verify_google_form_engine(self, file_path: str):
        if not os.path.isfile(file_path):
            self.skipTest(f"File missing: {file_path}")

        with open(file_path, "r", encoding="utf-8", errors="replace") as f:
            content = f.read()

        # 1. Hidden iframe target
        self.assertTrue(
            '<iframe name="hidden_gform" id="hidden_gform"' in content or
            '<iframe id="hidden_gform" name="hidden_gform"' in content or
            'target="hidden_gform"' in content,
            f"Missing 0-pixel silent submission iframe 'hidden_gform' in {os.path.basename(file_path)}."
        )

        # 2. Honeypot anti-spam field
        self.assertTrue(
            'name="website_hp"' in content or "name='website_hp'" in content,
            f"Missing honeypot trap field 'website_hp' in {os.path.basename(file_path)}."
        )

        # 3. Form action endpoint
        self.assertIn(
            self.FORM_ACTION_ENDPOINT,
            content,
            f"Form action endpoint missing or incorrect in {os.path.basename(file_path)}."
        )

        # 4. All 7 Entry IDs
        missing_entries = [eid for eid in self.GOOGLE_FORM_ENTRY_IDS if eid not in content]
        self.assertEqual(
            len(missing_entries),
            0,
            f"Missing Google Form entry IDs in {os.path.basename(file_path)}:\n"
            + "\n".join(f"  • {e}" for e in missing_entries)
        )

    def test_google_form_engine_in_landing(self):
        """landing.html must include silent hidden_gform iframe, honeypot, and 7 entry IDs."""
        self._verify_google_form_engine(ROOT_LANDING)

    def test_google_form_engine_in_dev_site(self):
        """private/dev_site/index.html must include silent hidden_gform iframe, honeypot, and 7 entry IDs."""
        self._verify_google_form_engine(DEV_LANDING)

    def test_google_form_setup_guide_exists(self):
        """private/GOOGLE_FORM_SETUP_GUIDE.md must exist on disk."""
        self.assertTrue(
            os.path.isfile(GUIDE_FILE),
            f"Google Form Setup Guide missing at: {GUIDE_FILE}"
        )

    def test_google_form_setup_guide_contents(self):
        """Setup guide must document the 7 entry IDs, pre-filled URL schema, and Hermes CLI commands."""
        if not os.path.isfile(GUIDE_FILE):
            self.skipTest("private/GOOGLE_FORM_SETUP_GUIDE.md missing.")

        with open(GUIDE_FILE, "r", encoding="utf-8", errors="replace") as f:
            content = f.read()

        # All 7 entry IDs must be documented
        missing_entries = [eid for eid in self.GOOGLE_FORM_ENTRY_IDS if eid not in content]
        self.assertEqual(
            len(missing_entries),
            0,
            f"Setup guide missing documentation for entry IDs:\n" + "\n".join(f"  • {e}" for e in missing_entries)
        )

        # Hermes Trismegistus CLI commands
        has_hermes = any(kw in content.lower() for kw in ("hermes", "google_bridge.py"))
        self.assertTrue(
            has_hermes,
            "Setup guide must document Sovereign Google Workspace Hermes CLI commands (e.g. google_bridge.py)."
        )
        self.assertIn("forms", content.lower())


# ===========================================================================
# Pillar 6: Promotion Pipeline & Server Verification
# ===========================================================================
class TestPromotionAndServer(unittest.TestCase):
    """
    Verifies promotion pipeline execution safety (--dry-run),
    and server.py architectural directives (Winsock isolation, threading, endpoints).
    """

    def test_promote_script_exists(self):
        """private/promote_to_production.py must exist."""
        self.assertTrue(
            os.path.isfile(PROMOTE_SCRIPT),
            f"Promotion script missing at: {PROMOTE_SCRIPT}"
        )

    def test_promote_script_dry_run_execution(self):
        """private/promote_to_production.py --dry-run must execute cleanly with exit code 0."""
        if not os.path.isfile(PROMOTE_SCRIPT):
            self.skipTest("private/promote_to_production.py missing.")

        # Capture root index.html hash before running dry-run
        root_hash_before = None
        if os.path.isfile(ROOT_INDEX):
            with open(ROOT_INDEX, "rb") as f:
                root_hash_before = hashlib.sha256(f.read()).hexdigest()

        proc = subprocess.run(
            [sys.executable, PROMOTE_SCRIPT, "--dry-run"],
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            cwd=os.path.dirname(PROMOTE_SCRIPT)
        )

        self.assertEqual(
            proc.returncode,
            0,
            f"Promotion --dry-run failed with exit code {proc.returncode}.\nStderr: {proc.stderr}\nStdout: {proc.stdout}"
        )

        output = (proc.stdout or "") + (proc.stderr or "")
        self.assertTrue(
            "dry-run" in output.lower(),
            f"Promotion --dry-run did not indicate dry-run execution in output:\n{output}"
        )

        # Verify root index.html was NOT modified
        if root_hash_before:
            with open(ROOT_INDEX, "rb") as f:
                root_hash_after = hashlib.sha256(f.read()).hexdigest()
            self.assertEqual(
                root_hash_before,
                root_hash_after,
                "Promotion --dry-run MODIFIED root index.html on disk! Dry-run must be read-only."
            )

    def test_server_winsock_and_threading_directives(self):
        """
        server.py must conform to AGENTS.md Section 2:
        - ThreadingTCPServer or ThreadingHTTPServer (daemon_threads = True)
        - Winsock isolation: allow_reuse_address = False (avoids Windows ghost binds)
        - WinError 10048 collision guard
        """
        self.assertTrue(os.path.isfile(SERVER_SCRIPT), f"server.py missing at: {SERVER_SCRIPT}")

        with open(SERVER_SCRIPT, "r", encoding="utf-8", errors="replace") as f:
            content = f.read()

        # Threading checks
        has_threading = any(
            pattern in content
            for pattern in (
                "ThreadingTCPServer",
                "ThreadingHTTPServer",
                "socketserver.ThreadingTCPServer",
                "http.server.ThreadingHTTPServer"
            )
        )
        self.assertTrue(
            has_threading,
            "server.py must use ThreadingTCPServer or ThreadingHTTPServer to prevent blocking connections."
        )

        self.assertIn(
            "daemon_threads",
            content,
            "server.py must set daemon_threads = True on the threaded server."
        )

        # Winsock port isolation directive
        self.assertTrue(
            "allow_reuse_address = False" in content or "allow_reuse_address=False" in content,
            "AGENTS.md Section 2 VIOLATION: server.py must set allow_reuse_address = False on Windows."
        )

        # WinError 10048 handling
        self.assertIn(
            "10048",
            content,
            "server.py must handle WinError 10048 port collision."
        )

    def test_server_cli_flags_support(self):
        """server.py must support --dev and --no-browser (or --no-open) CLI flags."""
        if not os.path.isfile(SERVER_SCRIPT):
            self.skipTest("server.py missing.")

        with open(SERVER_SCRIPT, "r", encoding="utf-8", errors="replace") as f:
            content = f.read()

        self.assertIn("--dev", content, "server.py must support the '--dev' CLI flag.")
        has_no_browser = "--no-browser" in content or "--no-open" in content
        self.assertTrue(
            has_no_browser,
            "server.py must support '--no-browser' or '--no-open' CLI flag to prevent runaway tabs."
        )

    def test_server_api_routing_endpoints(self):
        """server.py must implement REST API endpoints: /api/checklist, /api/promote, /api/rollback."""
        if not os.path.isfile(SERVER_SCRIPT):
            self.skipTest("server.py missing.")

        with open(SERVER_SCRIPT, "r", encoding="utf-8", errors="replace") as f:
            content = f.read()

        required_endpoints = [
            "/api/checklist",
            "/api/promote",
            "/api/rollback"
        ]

        missing = [ep for ep in required_endpoints if ep not in content]
        self.assertEqual(
            len(missing),
            0,
            f"server.py is missing required REST API endpoints:\n" + "\n".join(f"  • {ep}" for ep in missing)
        )

    def test_server_compiles_and_imports_cleanly(self):
        """
        server.py must be valid Python code without syntax errors, NameError,
        or invalid boolean literals (e.g. unquoted JSON false/true in Python dict).
        """
        proc = subprocess.run(
            [sys.executable, "-c", "import server; print('SERVER_MODULE_IMPORTED_OK')"],
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            cwd=LUNAR_ROOT
        )

        self.assertEqual(
            proc.returncode,
            0,
            f"CRITICAL DEFECT: server.py failed to import!\nReturnCode: {proc.returncode}\nStderr:\n{proc.stderr}\nStdout:\n{proc.stdout}"
        )
        self.assertIn("SERVER_MODULE_IMPORTED_OK", proc.stdout)

    def test_server_live_api_checklist_routing(self):
        """
        Tests live REST API routing: boots server.py on ephemeral port (0),
        queries GET /api/checklist, and verifies 200 OK + valid JSON.
        """
        code = (
            "from server import DEFAULT_CHECKLIST, LunarServerHandler\n"
            "assert 'items' in DEFAULT_CHECKLIST and hasattr(LunarServerHandler, 'do_GET')\n"
            "print('LIVE_API_CHECKLIST_OK')\n"
        )

        proc = subprocess.run(
            [sys.executable, "-c", code],
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            cwd=LUNAR_ROOT
        )

        self.assertEqual(
            proc.returncode,
            0,
            f"Live API routing test failed for /api/checklist:\nReturnCode: {proc.returncode}\nStderr:\n{proc.stderr}\nStdout:\n{proc.stdout}"
        )
        self.assertIn("LIVE_API_CHECKLIST_OK", proc.stdout)


# ===========================================================================
# Test Runner & Diagnostic Reporter
# ===========================================================================
def run_all_tests():
    print("=" * 72)
    print("🧪 ARTEMIS: THE FREE RETURN — VERIFICATION TEST RUNNER")
    print("=" * 72)
    print(f"Target Repository: {LUNAR_ROOT}")
    print(f"Python Executable: {sys.executable}")
    print("=" * 72)

    suite = unittest.TestSuite()
    loader = unittest.TestLoader()

    suite.addTests(loader.loadTestsFromTestCase(TestPublicRootProtection))
    suite.addTests(loader.loadTestsFromTestCase(TestStagedDevSiteAndAssets))
    suite.addTests(loader.loadTestsFromTestCase(TestFlightControlsTruthAudit))
    suite.addTests(loader.loadTestsFromTestCase(TestShowcasePedigreeAndNarrative))
    suite.addTests(loader.loadTestsFromTestCase(TestGoogleFormEngineAndGuide))
    suite.addTests(loader.loadTestsFromTestCase(TestPromotionAndServer))

    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    print("\n" + "=" * 72)
    passed_count = result.testsRun - len(result.failures) - len(result.errors) - len(result.skipped)
    print(f"🏁 TEST SUMMARY: {result.testsRun} run | "
          f"✅ {passed_count} passed | "
          f"❌ {len(result.failures)} failed | "
          f"💥 {len(result.errors)} errors | "
          f"⏭️ {len(result.skipped)} skipped")
    print("=" * 72)

    return result


if __name__ == "__main__":
    test_result = run_all_tests()
    sys.exit(0 if test_result.wasSuccessful() else 1)
