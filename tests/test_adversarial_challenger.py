#!/usr/bin/env python3
"""
⚔️ Artemis: The Free Return (Lunar Flyby XR) - Adversarial Challenger Stress Suite
==================================================================================
Adversarial tests for promotion pipeline and server routing protocol robustness.
Empirically stress-tests assumptions, edge cases, boundaries, and failure modes.
"""

import os
import sys
import io
import json
import time
import shutil
import hashlib
import tempfile
import unittest
import subprocess
from unittest.mock import MagicMock, patch

# Force UTF-8 on Windows
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8", line_buffering=True)
        sys.stderr.reconfigure(encoding="utf-8", line_buffering=True)
    except Exception:
        pass

TESTS_DIR = os.path.dirname(os.path.abspath(__file__))
LUNAR_ROOT = os.path.abspath(os.path.join(TESTS_DIR, ".."))
PRIVATE_DIR = os.path.join(LUNAR_ROOT, "private")
SNAPSHOTS_DIR = os.path.join(LUNAR_ROOT, "snapshots")
ROOT_INDEX = os.path.join(LUNAR_ROOT, "index.html")
BASELINE_BACKUP = os.path.join(SNAPSHOTS_DIR, "index_v2.1.19_sim_backup.html")
CHECKLIST_FILE = os.path.join(PRIVATE_DIR, "checklist_status.json")

if LUNAR_ROOT not in sys.path:
    sys.path.insert(0, LUNAR_ROOT)
if PRIVATE_DIR not in sys.path:
    sys.path.insert(0, PRIVATE_DIR)

import server
from promote_to_production import normalize_asset_paths, promote, rollback


class MockSocket:
    """Mock socket for SimpleHTTPRequestHandler testing."""
    def __init__(self, request_bytes):
        self.rfile = io.BytesIO(request_bytes)
        self.wfile = io.BytesIO()

    def makefile(self, mode, *args, **kwargs):
        if "r" in mode:
            return self.rfile
        elif "w" in mode:
            return self.wfile
        raise ValueError(f"Unknown mode: {mode}")

    def sendall(self, data):
        self.wfile.write(data)


def simulate_http_request(handler_class, method, path, headers=None, body=b""):
    """
    Simulates an HTTP request through LunarServerHandler using mock I/O.
    Returns (status_code, response_headers, response_body_bytes).
    """
    headers = headers or {}
    req_lines = [f"{method} {path} HTTP/1.1"]
    if "Host" not in headers:
        headers["Host"] = "localhost:3550"
    if body and "Content-Length" not in headers:
        headers["Content-Length"] = str(len(body))
    for k, v in headers.items():
        req_lines.append(f"{k}: {v}")
    req_lines.append("")
    req_lines.append("")
    raw_request = "\r\n".join(req_lines).encode("utf-8") + body

    sock = MockSocket(raw_request)
    # Instantiate handler with dummy client address and mock server
    mock_server = MagicMock()
    mock_server.server_name = "localhost"
    mock_server.server_port = 3550

    try:
        handler = handler_class(sock, ("127.0.0.1", 12345), mock_server)
    except Exception:
        pass

    sock.wfile.seek(0)
    response_bytes = sock.wfile.read()

    # Parse response
    parts = response_bytes.split(b"\r\n\r\n", 1)
    header_block = parts[0].decode("utf-8", errors="replace")
    body_bytes = parts[1] if len(parts) > 1 else b""

    header_lines = header_block.split("\r\n")
    status_line = header_lines[0]
    status_code = int(status_line.split(" ")[1]) if " " in status_line else 0

    resp_headers = {}
    for hline in header_lines[1:]:
        if ":" in hline:
            hk, hv = hline.split(":", 1)
            resp_headers[hk.strip().lower()] = hv.strip()

    return status_code, resp_headers, body_bytes


# ===========================================================================
# 1. Promotion Pipeline Stress-Tests
# ===========================================================================
class TestPromotionPipelineStress(unittest.TestCase):
    """Adversarial stress-testing of promotion pipeline and dry-run guarantees."""

    def test_dry_run_modifies_zero_files_on_disk(self):
        """
        Adversarial Test: Run promote_to_production.py --dry-run and verify
        that NOT A SINGLE FILE or DIRECTORY is modified, created, or deleted.
        """
        # Step 1: Scan entire lunar-flyby-xr directory tree
        before_state = {}
        for root, dirs, files in os.walk(LUNAR_ROOT):
            for fname in files:
                fpath = os.path.join(root, fname)
                try:
                    stat = os.stat(fpath)
                    with open(fpath, "rb") as f:
                        fhash = hashlib.sha256(f.read()).hexdigest()
                    before_state[fpath] = (stat.st_size, stat.st_mtime, fhash)
                except Exception:
                    pass

        # Step 2: Execute promote_to_production.py --dry-run
        proc = subprocess.run(
            [sys.executable, os.path.join(PRIVATE_DIR, "promote_to_production.py"), "--dry-run"],
            capture_output=True,
            text=True,
            encoding="utf-8",
            cwd=LUNAR_ROOT
        )

        self.assertEqual(proc.returncode, 0, f"Dry-run failed with code {proc.returncode}: {proc.stderr}")
        self.assertIn("[DRY-RUN] PROMOTING DEV/STAGING TO PUBLIC PRODUCTION", proc.stdout)
        self.assertIn("[DRY-RUN] Promotion Completed", proc.stdout)

        # Step 3: Scan tree after dry run
        after_state = {}
        for root, dirs, files in os.walk(LUNAR_ROOT):
            for fname in files:
                fpath = os.path.join(root, fname)
                try:
                    stat = os.stat(fpath)
                    with open(fpath, "rb") as f:
                        fhash = hashlib.sha256(f.read()).hexdigest()
                    after_state[fpath] = (stat.st_size, stat.st_mtime, fhash)
                except Exception:
                    pass

        # Step 4: Verify zero new files
        new_files = set(after_state.keys()) - set(before_state.keys())
        self.assertEqual(len(new_files), 0, f"VIOLATION: Dry-run created new files on disk: {new_files}")

        # Step 5: Verify zero deleted files
        deleted_files = set(before_state.keys()) - set(after_state.keys())
        self.assertEqual(len(deleted_files), 0, f"VIOLATION: Dry-run deleted files on disk: {deleted_files}")

        # Step 6: Verify zero content/hash changes
        modified_files = []
        for fpath, (b_size, b_mtime, b_hash) in before_state.items():
            a_size, a_mtime, a_hash = after_state[fpath]
            if b_hash != a_hash:
                modified_files.append((fpath, b_hash, a_hash))

        self.assertEqual(len(modified_files), 0, f"VIOLATION: Dry-run modified file contents: {modified_files}")

    def test_root_index_byte_for_byte_identical_to_snapshot(self):
        """
        Verify root index.html is byte-for-byte identical to
        snapshots/index_v2.1.19_sim_backup.html.
        """
        self.assertTrue(os.path.isfile(ROOT_INDEX), "Missing root index.html")
        self.assertTrue(os.path.isfile(BASELINE_BACKUP), "Missing baseline snapshot")

        with open(ROOT_INDEX, "rb") as f1, open(BASELINE_BACKUP, "rb") as f2:
            root_bytes = f1.read()
            backup_bytes = f2.read()

        self.assertEqual(len(root_bytes), len(backup_bytes), "File size mismatch between root and snapshot")
        self.assertEqual(root_bytes, backup_bytes, "Byte-for-byte content mismatch between root and snapshot")

        root_hash = hashlib.sha256(root_bytes).hexdigest()
        expected_hash = "5ecfaa504e093f6025159a6a88037154598eb26545f2a34a98b44843f0d74861"
        self.assertEqual(root_hash, expected_hash, f"Hash mismatch: expected {expected_hash}, got {root_hash}")

    def test_dry_run_cli_output_accuracy(self):
        """Verify dry-run reports accurate planned operations without execution."""
        proc = subprocess.run(
            [sys.executable, os.path.join(PRIVATE_DIR, "promote_to_production.py"), "--dry-run"],
            capture_output=True,
            text=True,
            encoding="utf-8",
            cwd=LUNAR_ROOT
        )
        self.assertEqual(proc.returncode, 0)
        self.assertIn("Would backup current index.html", proc.stdout)
        self.assertIn("Would write normalized content to index.html", proc.stdout)
        self.assertIn("Would write normalized content to sim.html", proc.stdout)


# ===========================================================================
# 2. Path Normalization Regex Edge Case Mining
# ===========================================================================
class TestPathNormalizationEdgeCases(unittest.TestCase):
    """Adversarial boundary testing for normalize_asset_paths regex logic."""

    def test_standard_double_and_single_quotes(self):
        html = (
            '<script src="../../vendor/three.min.js"></script>\n'
            "<link rel='stylesheet' href='../../vendor/styles.css'>\n"
            '<img src="../../textures/earth.jpg">\n'
            "<img src='../../images/hero.webp'>\n"
            '<div data-src="../../assets/model.glb"></div>\n'
        )
        norm, count = normalize_asset_paths(html)
        self.assertIn('src="vendor/three.min.js"', norm)
        self.assertIn("href='vendor/styles.css'", norm)
        self.assertIn('src="textures/earth.jpg"', norm)
        self.assertIn("src='images/hero.webp'", norm)
        self.assertIn('data-src="assets/model.glb"', norm)

    def test_css_url_patterns(self):
        css = (
            "body { background: url('../../textures/stars.jpg'); }\n"
            'div { background-image: url("../../textures/moon.jpg"); }\n'
            "header { background: url(../../images/banner.png); }\n"
            "footer { background: url(  '../../textures/footer.jpg'  ); }\n"
            "section { background: url(  \"../../textures/section.jpg\"  ); }\n"
        )
        norm, count = normalize_asset_paths(css)
        self.assertIn("url('textures/stars.jpg')", norm)
        self.assertIn('url("textures/moon.jpg")', norm)
        self.assertIn("url(images/banner.png)", norm)
        self.assertIn("url(  'textures/footer.jpg'  )", norm)
        self.assertIn('url(  "textures/section.jpg"  )', norm)

    def test_javascript_string_literals(self):
        js = (
            "textureLoader.load('../../textures/earth-blue-marble.jpg', cb);\n"
            'textureLoader.load("../../textures/moon_1024.jpg", cb);\n'
            "var v = '../../vendor/cannon.min.js';\n"
            'let a = "../../assets/audio/thruster.mp3";\n'
        )
        norm, count = normalize_asset_paths(js)
        self.assertIn("'textures/earth-blue-marble.jpg'", norm)
        self.assertIn('"textures/moon_1024.jpg"', norm)
        self.assertIn("'vendor/cannon.min.js'", norm)
        self.assertIn('"assets/audio/thruster.mp3"', norm)

    def test_single_dotdot_normalization(self):
        html = '<img src="../textures/moon.jpg"><script src="../vendor/lib.js"></script>'
        norm, count = normalize_asset_paths(html)
        self.assertIn('src="textures/moon.jpg"', norm)
        self.assertIn('src="vendor/lib.js"', norm)

    def test_external_cdn_urls_protected(self):
        """External CDN URLs must never be corrupted by asset normalization."""
        cdn = (
            '<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>\n'
            '<script src="https://unpkg.com/three-globe/dist/three-globe.min.js"></script>\n'
            '<script src="https://raw.githubusercontent.com/mrdoob/three.js/master/build/three.min.js"></script>\n'
        )
        norm, count = normalize_asset_paths(cdn)
        self.assertEqual(norm, cdn, "External CDN URLs were modified!")
        self.assertEqual(count, 0)

    def test_query_params_and_hash_anchors(self):
        html = (
            '<script src="../../vendor/three.min.js?v=2.1.25"></script>\n'
            '<link href="../../assets/theme.css#main" rel="stylesheet">\n'
        )
        norm, count = normalize_asset_paths(html)
        self.assertIn('src="vendor/three.min.js?v=2.1.25"', norm)
        self.assertIn('href="assets/theme.css#main"', norm)

    def test_unsupported_pattern_mining_backticks(self):
        """
        Adversarial Boundary Check: ES6 template literals (backticks).
        Notice regex patterns in promote_to_production.py use (['\"]) which does NOT match backticks.
        We verify whether backtick relative paths are normalized or left intact.
        """
        js = "loader.load(`../../textures/moon.jpg`);"
        norm, count = normalize_asset_paths(js)
        # Empirical finding: backticks are NOT replaced by current regex
        is_normalized = "textures/moon.jpg" in norm and "`../../" not in norm
        # We record whether it replaced or not
        self.assertFalse(is_normalized, "Expected backticks not to be normalized by current regex")

    def test_unsupported_pattern_mining_screenshots(self):
        """
        Adversarial Boundary Check: 'screenshots' in ASSET_DIRS vs normalize_asset_paths regex.
        Line 40 defines ASSET_DIRS with 'screenshots', but the regex in normalize_asset_paths
        only includes (textures|vendor|images|assets).
        """
        html = '<img src="../../screenshots/cockpit.png">'
        norm, count = normalize_asset_paths(html)
        # Empirical finding: screenshots is omitted from regex
        self.assertIn('../../screenshots/cockpit.png', norm)


# ===========================================================================
# 3. Server Routing & Protocol Robustness Stress-Tests
# ===========================================================================
class TestServerRoutingAndProtocol(unittest.TestCase):
    """Adversarial stress-testing of server.py request handling and protocol boundaries."""

    def test_get_api_checklist_returns_200_valid_json(self):
        """GET /api/checklist returns 200 OK and valid JSON with items."""
        status, headers, body = simulate_http_request(
            server.LunarServerHandler, "GET", "/api/checklist"
        )
        self.assertEqual(status, 200)
        self.assertIn("application/json", headers.get("content-type", ""))
        self.assertEqual(headers.get("access-control-allow-origin"), "*")

        data = json.loads(body.decode("utf-8"))
        self.assertIsInstance(data, dict)
        self.assertTrue("items" in data or "status" in data)

    def test_get_api_checklist_with_query_params(self):
        """GET /api/checklist?foo=bar returns 200 OK and valid JSON."""
        status, headers, body = simulate_http_request(
            server.LunarServerHandler, "GET", "/api/checklist?cache_bust=12345"
        )
        self.assertEqual(status, 200)
        data = json.loads(body.decode("utf-8"))
        self.assertTrue("items" in data or "status" in data)

    def test_post_api_checklist_valid_payload(self):
        """POST /api/checklist with valid JSON payload updates state and returns 200 OK."""
        # Backup existing checklist file if present
        checklist_backup = None
        if os.path.exists(CHECKLIST_FILE):
            with open(CHECKLIST_FILE, "r", encoding="utf-8") as f:
                checklist_backup = f.read()

        try:
            test_payload = {
                "updated_at": "2026-10-22T23:00:00Z",
                "updated_by": "adversarial_tester",
                "version": "v2.1.25-test",
                "items": {
                    "test-item-1": {"title": "Test 1", "checked": True}
                }
            }
            body = json.dumps(test_payload).encode("utf-8")
            status, headers, resp_body = simulate_http_request(
                server.LunarServerHandler, "POST", "/api/checklist",
                headers={"Content-Type": "application/json"},
                body=body
            )
            self.assertEqual(status, 200)
            resp = json.loads(resp_body.decode("utf-8"))
            self.assertEqual(resp.get("status"), "ok")
            self.assertEqual(resp.get("saved_count"), 1)

            # Verify written to disk
            with open(CHECKLIST_FILE, "r", encoding="utf-8") as f:
                on_disk = json.load(f)
            self.assertEqual(on_disk["updated_by"], "adversarial_tester")
        finally:
            # Restore original checklist file
            if checklist_backup is not None:
                with open(CHECKLIST_FILE, "w", encoding="utf-8") as f:
                    f.write(checklist_backup)

    def test_post_api_checklist_malformed_json(self):
        """
        Adversarial Test: POST /api/checklist with malformed JSON syntax.
        Expects 500 status (handled gracefully without crashing server) with error message.
        """
        bad_body = b"NOT_VALID_JSON{foo:bar"
        status, headers, resp_body = simulate_http_request(
            server.LunarServerHandler, "POST", "/api/checklist",
            headers={"Content-Type": "application/json"},
            body=bad_body
        )
        self.assertEqual(status, 500)
        resp = json.loads(resp_body.decode("utf-8"))
        self.assertEqual(resp.get("status"), "error")
        self.assertIn("message", resp)

    def test_post_api_checklist_empty_body(self):
        """Adversarial Test: POST /api/checklist with 0 content length / empty body."""
        status, headers, resp_body = simulate_http_request(
            server.LunarServerHandler, "POST", "/api/checklist",
            headers={"Content-Length": "0"},
            body=b""
        )
        self.assertEqual(status, 500)
        resp = json.loads(resp_body.decode("utf-8"))
        self.assertEqual(resp.get("status"), "error")

    def test_post_unknown_route_returns_404(self):
        """Adversarial Test: POST to unknown route returns 404 Not Found."""
        status, headers, resp_body = simulate_http_request(
            server.LunarServerHandler, "POST", "/api/nonexistent_route",
            body=b"{}"
        )
        self.assertEqual(status, 404)

    def test_get_on_promote_and_rollback_blocked(self):
        """
        Adversarial Security Test: GET /api/promote and GET /api/rollback
        must NOT trigger actions and must return 404.
        """
        status_promote, _, _ = simulate_http_request(
            server.LunarServerHandler, "GET", "/api/promote"
        )
        self.assertEqual(status_promote, 404, "GET /api/promote should return 404")

        status_rollback, _, _ = simulate_http_request(
            server.LunarServerHandler, "GET", "/api/rollback"
        )
        self.assertEqual(status_rollback, 404, "GET /api/rollback should return 404")

    def test_options_cors_preflight(self):
        """OPTIONS /api/checklist handles CORS preflight cleanly."""
        status, headers, _ = simulate_http_request(
            server.LunarServerHandler, "OPTIONS", "/api/checklist"
        )
        self.assertEqual(status, 200)
        self.assertEqual(headers.get("access-control-allow-origin"), "*")
        self.assertIn("POST", headers.get("access-control-allow-methods", ""))

    def test_winsock_isolation_configuration(self):
        """
        Check AGENTS.md Winsock isolation:
        allow_reuse_address must be False on ThreadedLunarServer.
        daemon_threads must be True.
        """
        self.assertFalse(
            server.ThreadedLunarServer.allow_reuse_address,
            "VIOLATION: allow_reuse_address must be False for Windows Winsock isolation!"
        )
        self.assertTrue(
            server.ThreadedLunarServer.daemon_threads,
            "VIOLATION: daemon_threads must be True to prevent server hangs!"
        )


# ===========================================================================
# 4. Rollback and Promotion In-Process Logic Stress-Tests
# ===========================================================================
class TestPromotionAndRollbackInProcess(unittest.TestCase):
    """Stress tests for promote() and rollback() functions."""

    def test_rollback_restores_from_baseline(self):
        """
        Adversarial Test: Verify rollback() restores index.html from baseline snapshot.
        We simulate by creating a temporary target or checking function behavior.
        """
        self.assertTrue(os.path.exists(BASELINE_BACKUP))
        # Call rollback directly
        res = rollback()
        self.assertEqual(res.get("status"), "ok")
        self.assertEqual(res.get("restored_from"), BASELINE_BACKUP)
        self.assertEqual(res.get("restored_to"), ROOT_INDEX)

        # Re-verify hash equality
        with open(ROOT_INDEX, "rb") as f1, open(BASELINE_BACKUP, "rb") as f2:
            self.assertEqual(f1.read(), f2.read())

    def test_promote_dry_run_flag(self):
        """Verify promote(dry_run=True) returns dict with dry_run=True and status=ok."""
        res = promote(dry_run=True)
        self.assertEqual(res.get("status"), "ok")
        self.assertTrue(res.get("dry_run"))
        self.assertIn("index.html", res.get("promoted_files", []))
        self.assertIn("sim.html", res.get("promoted_files", []))


if __name__ == "__main__":
    unittest.main(verbosity=2)
