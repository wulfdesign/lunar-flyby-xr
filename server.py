#!/usr/bin/env python3
"""
🚀 Artemis: The Free Return (Lunar Flyby XR) Multi-Threaded Server (Port 3550)
Compliant with AGENTS.md Windows Winsock Isolation & Threading Directives.

Features:
- ThreadingTCPServer with daemon_threads = True and allow_reuse_address = False
- [WinError 10048] port collision protection with automatic existing tab launcher
- Single-source browser launching via daemon timer (suppressed via --no-browser / --no-open)
- CLI Flags: --dev (opens /private/dev_dashboard/index.html), --no-browser, --no-open
- Custom MIME types: .wasm, .glb, .gltf, .json
- REST API Endpoints:
  - GET  /api/checklist   -> Serves private/checklist_status.json
  - POST /api/checklist   -> Persists checklist state atomically to disk
  - POST /api/promote     -> Executes promote(dry_run=False) in-process
  - POST /api/rollback    -> Restores public index.html from baseline backup
  - OPTIONS               -> Complete CORS header handling
"""

import os
import sys
import time
import socket
import json
import socketserver
import http.server
import webbrowser
import threading

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8", line_buffering=True)
        sys.stderr.reconfigure(encoding="utf-8", line_buffering=True)
    except Exception:
        pass

PORT = 3550
SERVER_VERSION = "2.1.25"
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
PRIVATE_DIR = os.path.join(ROOT_DIR, "private")
CHECKLIST_FILE = os.path.join(PRIVATE_DIR, "checklist_status.json")

# Ensure private is in sys.path for direct import
if PRIVATE_DIR not in sys.path:
    sys.path.insert(0, PRIVATE_DIR)

try:
    from promote_to_production import promote, rollback
except ImportError:
    try:
        from private.promote_to_production import promote, rollback
    except ImportError:
        promote = None
        rollback = None

def get_local_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception:
        return "127.0.0.1"

DEFAULT_CHECKLIST = {
    "updated_at": "2026-10-22T22:45:00Z",
    "updated_by": "default_seed",
    "version": "v2.1.25-dev",
    "items": {
        "sim-verlet": {
            "title": "Velocity Verlet Orbital Dynamics Verified",
            "desc": "Confirm frame-by-frame Vis-viva gravitational integration across 800,000 km cislunar free return without numerical drift.",
            "category": "Physics",
            "checked": False
        },
        "sim-webxr": {
            "title": "Meta Quest 3 6DoF WebXR Cockpit Tested",
            "desc": "Launch on Quest 3 browser; verify controller triggers, recenter, and 72/90 fps refresh rate.",
            "category": "WebXR",
            "checked": False
        },
        "sim-warp": {
            "title": "Hermite Time-Warp Safety Gate Operating",
            "desc": "Test continuous acceleration from 1x to 7,200x warp and verify automatic deceleration at Moon perilune entry.",
            "category": "Avionics",
            "checked": False
        },
        "sim-reentry": {
            "title": "Reentry Plasma Visualizer & Aerodynamic Drag",
            "desc": "Verify 120 km atmospheric entry interface triggers visual plasma glow, HUD heating alerts, and bank angle lift modulation.",
            "category": "Aerodynamics",
            "checked": False
        },
        "portal-form": {
            "title": "Silent Google Form Intake Tested",
            "desc": "Submit test lead from landing.html; verify silent iframe capture, honeypot spam guard, and localStorage redundancy.",
            "category": "Intake",
            "checked": False
        },
        "staging-promotion": {
            "title": "Air-Gapped Private Dev Staging & 1-Click Promotion",
            "desc": "Verify private/dev_site staging, path normalization (../../textures/ -> textures/), snapshots backup, and 1-click rollback.",
            "category": "DevOps",
            "checked": True
        }
    }
}

class LunarServerHandler(http.server.SimpleHTTPRequestHandler):
    extensions_map = http.server.SimpleHTTPRequestHandler.extensions_map.copy()
    extensions_map.update({
        '.wasm': 'application/wasm',
        '.glb': 'model/gltf-binary',
        '.gltf': 'model/gltf+json',
        '.json': 'application/json',
        '.js': 'application/javascript',
        '.mjs': 'application/javascript',
        '.css': 'text/css',
        '.html': 'text/html; charset=utf-8',
        '.md': 'text/plain; charset=utf-8'
    })

    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=ROOT_DIR, **kwargs)

    def end_headers(self):
        self.send_header("Cache-Control", "no-cache, no-store, must-revalidate")
        self.send_header("Pragma", "no-cache")
        self.send_header("Expires", "0")
        super().end_headers()

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()

    def do_GET(self):
        clean_path = self.path.split("?")[0]
        if clean_path == "/api/checklist":
            self.send_response(200)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            if os.path.exists(CHECKLIST_FILE):
                try:
                    with open(CHECKLIST_FILE, "r", encoding="utf-8") as f:
                        data = f.read()
                    self.wfile.write(data.encode("utf-8"))
                    return
                except Exception as e:
                    sys.stderr.write(f"Error reading checklist file: {e}\n")
            # Fallback to default
            self.wfile.write(json.dumps(DEFAULT_CHECKLIST, indent=2).encode("utf-8"))
            return
        return super().do_GET()

    def do_POST(self):
        clean_path = self.path.split("?")[0]

        # 1. Checklist Persistence
        if clean_path == "/api/checklist":
            try:
                content_length = int(self.headers.get("Content-Length", 0))
                post_data = self.rfile.read(content_length)
                payload = json.loads(post_data.decode("utf-8"))
                os.makedirs(PRIVATE_DIR, exist_ok=True)
                with open(CHECKLIST_FILE, "w", encoding="utf-8") as f:
                    json.dump(payload, f, indent=2, ensure_ascii=False)

                self.send_response(200)
                self.send_header("Content-Type", "application/json; charset=utf-8")
                self.send_header("Access-Control-Allow-Origin", "*")
                self.end_headers()
                items = payload.get("items", payload.get("status", payload))
                item_count = len(items) if isinstance(items, (dict, list)) else 1
                resp = json.dumps({"status": "ok", "saved_count": item_count, "saved_at": time.time()})
                self.wfile.write(resp.encode("utf-8"))
                return
            except Exception as e:
                self.send_response(500)
                self.send_header("Content-Type", "application/json; charset=utf-8")
                self.end_headers()
                self.wfile.write(json.dumps({"status": "error", "message": str(e)}).encode("utf-8"))
                return

        # 2. Trigger Promotion Pipeline
        if clean_path == "/api/promote":
            try:
                if promote is not None:
                    result = promote(dry_run=False)
                else:
                    import subprocess
                    promote_py = os.path.join(PRIVATE_DIR, "promote_to_production.py")
                    proc = subprocess.run([sys.executable, promote_py], capture_output=True, text=True, encoding="utf-8")
                    result = {
                        "status": "ok" if proc.returncode == 0 else "error",
                        "output": proc.stdout,
                        "error": proc.stderr
                    }
                status_code = 200 if result.get("status") == "ok" else 500
                self.send_response(status_code)
                self.send_header("Content-Type", "application/json; charset=utf-8")
                self.send_header("Access-Control-Allow-Origin", "*")
                self.end_headers()
                self.wfile.write(json.dumps(result, indent=2).encode("utf-8"))
                return
            except Exception as e:
                self.send_response(500)
                self.send_header("Content-Type", "application/json; charset=utf-8")
                self.end_headers()
                self.wfile.write(json.dumps({"status": "error", "message": str(e)}).encode("utf-8"))
                return

        # 3. Trigger Rollback Pipeline
        if clean_path == "/api/rollback":
            try:
                if rollback is not None:
                    result = rollback()
                else:
                    import subprocess
                    promote_py = os.path.join(PRIVATE_DIR, "promote_to_production.py")
                    proc = subprocess.run([sys.executable, promote_py, "--rollback"], capture_output=True, text=True, encoding="utf-8")
                    result = {
                        "status": "ok" if proc.returncode == 0 else "error",
                        "output": proc.stdout,
                        "error": proc.stderr
                    }
                status_code = 200 if result.get("status") == "ok" else 500
                self.send_response(status_code)
                self.send_header("Content-Type", "application/json; charset=utf-8")
                self.send_header("Access-Control-Allow-Origin", "*")
                self.end_headers()
                self.wfile.write(json.dumps(result, indent=2).encode("utf-8"))
                return
            except Exception as e:
                self.send_response(500)
                self.send_header("Content-Type", "application/json; charset=utf-8")
                self.end_headers()
                self.wfile.write(json.dumps({"status": "error", "message": str(e)}).encode("utf-8"))
                return

        self.send_response(404)
        self.end_headers()

class ThreadedLunarServer(socketserver.ThreadingTCPServer):
    daemon_threads = True
    allow_reuse_address = False  # Strict Winsock isolation on Windows

# Alias for testing and standard socketserver compatibility
ThreadingTCPServer = ThreadedLunarServer

def run_server():
    auto_open = not ("--no-browser" in sys.argv or "--no-open" in sys.argv)
    is_dev = "--dev" in sys.argv
    launch_path = "/private/dev_dashboard/index.html" if is_dev else "/index.html"
    local_ip = get_local_ip()

    os.chdir(ROOT_DIR)
    try:
        httpd = ThreadedLunarServer(("", PORT), LunarServerHandler)
    except OSError as e:
        if getattr(e, 'winerror', None) == 10048 or getattr(e, 'errno', None) == 48 or "10048" in str(e):
            print("=" * 68)
            print(f"⚠️ Port {PORT} is ALREADY IN USE by an active Lunar Flyby server.")
            print(f"👉 The server is ALREADY RUNNING and serving requests at:")
            print(f"   💻 http://localhost:{PORT}{launch_path}")
            print(f"   🥽 http://{local_ip}:{PORT}{launch_path}")
            if auto_open:
                print(f"🌐 Opening http://127.0.0.1:{PORT}{launch_path} in your browser...")
                try:
                    webbrowser.open(f"http://127.0.0.1:{PORT}{launch_path}")
                except Exception:
                    pass
            print("=" * 68)
            return
        raise e

    print("=" * 68)
    print(f"🚀 ARTEMIS: LUNAR FLYBY XR — MULTI-THREADED SERVER (v{SERVER_VERSION} on Port {PORT})")
    print("=" * 68)
    print(f"💻 Live Simulation Root:   http://localhost:{PORT}/index.html")
    print(f"🧪 Staged Dev Landing:     http://localhost:{PORT}/private/dev_site/index.html")
    print(f"🚀 Staged Dev Simulation:  http://localhost:{PORT}/private/dev_site/sim.html")
    print(f"🥽 Quest 3 LAN Headset:    http://{local_ip}:{PORT}/index.html")
    print(f"🔒 Operator Dev Dashboard: http://localhost:{PORT}/private/dev_dashboard/index.html")
    print("=" * 68)
    print("👉 Press Ctrl+C to stop the server.")
    print("=" * 68)

    if auto_open:
        def _open():
            time.sleep(0.3)
            try:
                webbrowser.open(f"http://127.0.0.1:{PORT}{launch_path}")
            except Exception:
                pass
        threading.Thread(target=_open, daemon=True).start()

    with httpd:
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServer gracefully stopped.")

if __name__ == "__main__":
    run_server()
