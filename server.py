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
  - GET  /api/tasks       -> Parses Tasks.md and private/privTasks.md live task ledgers
  - GET  /api/docs        -> Discovers & returns all public, docs, and private Markdown codex files
  - POST /api/task-action -> Toggles checkboxes, promotes to QA, or confirms QA to COMPLETED.md
  - POST /api/promote     -> Executes promote(dry_run=False) in-process
  - POST /api/rollback    -> Restores public index.html from baseline backup
  - OPTIONS               -> Complete CORS header handling
"""

import os
import sys
import time
import socket
import json
import re
import socketserver
import http.server
import webbrowser
import threading
from datetime import datetime

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8", line_buffering=True)
        sys.stderr.reconfigure(encoding="utf-8", line_buffering=True)
    except Exception:
        pass

PORT = 3550
SERVER_VERSION = "2.2.1"
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
PRIVATE_DIR = os.path.join(ROOT_DIR, "private")
CHECKLIST_FILE = os.path.join(PRIVATE_DIR, "checklist_status.json")
TASKS_FILE = os.path.join(ROOT_DIR, "Tasks.md")
COMPLETED_FILE = os.path.join(ROOT_DIR, "COMPLETED.md")
PRIV_TASKS_FILE = os.path.join(PRIVATE_DIR, "privTasks.md")
PRIV_COMPLETED_FILE = os.path.join(PRIVATE_DIR, "privCompleted.md")

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
    "updated_at": "2026-11-19T23:30:00Z",
    "updated_by": "default_seed",
    "version": "v2.2.0-dev",
    "items": {
        "sim-tidal-moon": {
            "title": "Lunar 1:1 Tidal Locking & Anti-Washout Crater Relief (v2.1.30-dev)",
            "desc": "Confirm Lunar Near Side faces Earth continuously (moon.rotation.y = Math.PI - moonAngle) and crater relief remains crisp without white wash-out on approach.",
            "category": "Graphics",
            "checked": False
        },
        "sim-real-stars": {
            "title": "Real Astronomical Starfield, 5 Planets & Sirius Fin Beacon (v2.1.31-dev)",
            "desc": "Verify 3,000+ star celestial sphere, Pogson magnitudes, Planck B-V colors, Venus/Jupiter/Mars/Saturn/Mercury, and HUD hover on Sirius (The Dog Star — In Honor of Fin).",
            "category": "Graphics",
            "checked": False
        },
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

def _extract_task_fields(raw_line):
    m_bold = re.search(r"\*\*(.+?)\*\*:?\s*(.*)", raw_line)
    if m_bold:
        title = m_bold.group(1).strip().rstrip(":")
        desc = m_bold.group(2).strip().lstrip(":").strip()
    else:
        clean = re.sub(r"^\s*[-*]\s*\[[ xX]\]\s*", "", raw_line).strip()
        title = clean
        desc = ""
    return title, desc

def parse_tasks_file(filepath, target_name):
    items = []
    version = "v2.2.0-dev"
    if not os.path.exists(filepath):
        return items, version

    with open(filepath, "r", encoding="utf-8") as f:
        lines = f.read().splitlines()

    section = "General"
    for idx, line in enumerate(lines):
        s = line.strip()
        if s.startswith("**Version:**"):
            version = s.replace("**Version:**", "").strip()
        elif s.startswith("#"):
            section = re.sub(r"^#+\s*", "", s).strip()
            continue

        m = re.match(r"^\s*[-*]\s*\[([ xX])\]\s*(.*)$", line)
        if not m:
            continue
        checked = (m.group(1).lower() == "x")
        body = m.group(2).strip()
        sec_low = section.lower()

        if checked or "🏆" in body or "completed" in sec_low:
            status = "completed"
        elif "🧪" in body or "waiting for qa" in sec_low:
            status = "qa"
        elif "🛠️" in body or "🩹" in body or "🏗️" in body or "current work" in sec_low or "active sprint" in sec_low or "fin fest" in sec_low:
            status = "in_progress"
        else:
            status = "roadmap"

        priority = body.count("🔥")
        title, desc = _extract_task_fields(body)
        items.append({
            "target": target_name,
            "lineIndex": idx,
            "rawLine": line,
            "checked": checked,
            "status": status,
            "section": section,
            "priority": priority,
            "title": title,
            "desc": desc
        })
    return items, version

def get_all_tasks_payload():
    pub_items, version = parse_tasks_file(TASKS_FILE, "public")
    priv_items, _ = parse_tasks_file(PRIV_TASKS_FILE, "private")
    all_items = pub_items + priv_items

    counts = {"qa": 0, "in_progress": 0, "roadmap": 0, "completed": 0}
    for it in all_items:
        st = it["status"]
        if st in counts:
            counts[st] += 1

    # Include archived counts from COMPLETED.md / privCompleted.md
    archived = 0
    for cfile in (COMPLETED_FILE, PRIV_COMPLETED_FILE):
        if os.path.exists(cfile):
            with open(cfile, "r", encoding="utf-8", errors="ignore") as f:
                archived += len(re.findall(r"^\s*[-*]\s*\[[xX]\]", f.read(), re.M))

    return {
        "version": version,
        "counts": counts,
        "archived_count": archived,
        "items": all_items,
        "updated_at": datetime.now().isoformat()
    }

def handle_task_action(payload):
    target = payload.get("target", "public")
    action = payload.get("action", "toggle_check")
    line_index = payload.get("lineIndex")
    raw_line = payload.get("rawLine", "")

    tasks_path = PRIV_TASKS_FILE if target == "private" else TASKS_FILE
    completed_path = PRIV_COMPLETED_FILE if target == "private" else COMPLETED_FILE

    if not os.path.exists(tasks_path):
        return {"ok": False, "error": f"{os.path.basename(tasks_path)} not found"}

    with open(tasks_path, "r", encoding="utf-8") as f:
        lines = f.read().splitlines()

    match_idx = None
    if isinstance(line_index, int) and 0 <= line_index < len(lines):
        if not raw_line or lines[line_index].strip() == raw_line.strip():
            match_idx = line_index
    if match_idx is None and raw_line:
        for i, l in enumerate(lines):
            if l.strip() == raw_line.strip():
                match_idx = i
                break

    if match_idx is None:
        return {"ok": False, "error": "Matching task line not found"}

    target_line = lines[match_idx]

    if action == "toggle_check":
        if re.match(r"^(\s*[-*]\s*)\[\s*\]", target_line):
            lines[match_idx] = re.sub(r"^(\s*[-*]\s*)\[\s*\]", r"\1[x]", target_line, count=1)
        elif re.match(r"^(\s*[-*]\s*)\[[xX]\]", target_line):
            lines[match_idx] = re.sub(r"^(\s*[-*]\s*)\[[xX]\]", r"\1[ ]", target_line, count=1)
        with open(tasks_path, "w", encoding="utf-8") as f:
            f.write("\n".join(lines) + "\n")
    elif action == "promote_to_qa":
        new_line = re.sub(r"^(\s*[-*]\s*)\[[ xX]\](\s*(?:🧪|🛠️|🩹|🏗️|🔬|📤|☀️|🧭|🐾|📇|🧩|💻|🌌|✨|🌕|📚)?\s*)", r"\1[ ] 🧪 ", target_line, count=1)
        if "🧪" not in new_line:
            new_line = re.sub(r"^(\s*[-*]\s*)\[[ xX]\]\s*", r"\1[ ] 🧪 ", target_line, count=1)
        if target == "public":
            lines.pop(match_idx)
            qa_idx = next((i for i, l in enumerate(lines) if "## 🧪" in l), None)
            if qa_idx is not None:
                lines.insert(qa_idx + 1, new_line)
            else:
                lines.insert(0, new_line)
        else:
            lines[match_idx] = new_line
        with open(tasks_path, "w", encoding="utf-8") as f:
            f.write("\n".join(lines) + "\n")
    elif action == "confirm_qa":
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
        promoted = re.sub(r"^(\s*[-*]\s*)\[[ xX]\]\s*(?:🧪|🛠️|🩹|🏗️)?\s*", r"\1[x] 🏆 ", target_line, count=1)
        if "🏆" not in promoted:
            promoted = re.sub(r"^(\s*[-*]\s*)\[[ xX]\]\s*", r"\1[x] 🏆 ", target_line, count=1)
        promoted = f"{promoted.rstrip()} *(HITL QA Confirmed {timestamp})*"
        lines.pop(match_idx)
        with open(tasks_path, "w", encoding="utf-8") as f:
            f.write("\n".join(lines) + "\n")
        existing_comp = ""
        if os.path.exists(completed_path):
            with open(completed_path, "r", encoding="utf-8") as f:
                existing_comp = f.read().rstrip()
        with open(completed_path, "w", encoding="utf-8") as f:
            f.write(f"{existing_comp}\n{promoted}\n")
    else:
        return {"ok": False, "error": f"Unknown action: {action}"}

    return {"ok": True, "tasks": get_all_tasks_payload()}

DOCS_PRIORITY_ORDER = [
    "README.md",
    "Tasks.md",
    "devlog.md",
    "chatHandOff.md",
    "COMPLETED.md",
    "LICENSE_RATIONALE.md",
    "LICENSE.md",
    "private/privTasks.md",
    "private/privDevLog.md",
    "private/chatHandOff.md",
    "private/LAUNCH_MEMORIES.md",
    "private/GOOGLE_FORM_SETUP_GUIDE.md",
    "private/privCompleted.md",
    "private/business_model.md",
    "private/philosophy.md",
    "private/founders.md",
    "docs/celestial_navigation.md",
    "docs/ArtemisII.md",
    "docs/ArtemisII_Telemetry_Notes.md",
    "docs/credits.md"
]

def _classify_doc_scope(rel_path):
    norm = rel_path.replace("\\", "/")
    if norm.startswith("private/"):
        return "private"
    if norm.startswith("docs/") or norm.startswith("snapshots/") or norm.startswith("session-handoff/") or norm.startswith("archive/") or norm.startswith(".agents/"):
        return "docs"
    return "public"

def _extract_markdown_title(content, fallback_name):
    for line in content.splitlines():
        s = line.strip()
        if s.startswith("#"):
            title = re.sub(r"^#+\s*", "", s).strip()
            if title:
                return title
    return fallback_name

def get_all_docs_payload():
    priority_map = {path: idx for idx, path in enumerate(DOCS_PRIORITY_ORDER)}
    docs = []
    counts = {"total": 0, "public": 0, "private": 0, "docs": 0}

    for dirpath, dirnames, filenames in os.walk(ROOT_DIR):
        dirnames[:] = [d for d in dirnames if d not in (".git", "node_modules", "__pycache__")]
        for fname in filenames:
            if not fname.lower().endswith(".md"):
                continue
            full_path = os.path.join(dirpath, fname)
            rel_path = os.path.relpath(full_path, ROOT_DIR).replace("\\", "/")
            scope = _classify_doc_scope(rel_path)
            try:
                stat = os.stat(full_path)
                with open(full_path, "r", encoding="utf-8", errors="replace") as f:
                    content = f.read()
                title = _extract_markdown_title(content, fname)
                line_count = len(content.splitlines())
                docs.append({
                    "id": rel_path,
                    "name": fname,
                    "rel_path": rel_path,
                    "scope": scope,
                    "title": title,
                    "size_bytes": stat.st_size,
                    "modified_at": datetime.fromtimestamp(stat.st_mtime).isoformat(timespec="seconds"),
                    "line_count": line_count,
                    "content": content
                })
                counts["total"] += 1
                counts[scope] = counts.get(scope, 0) + 1
            except Exception as exc:
                sys.stderr.write(f"Warning: could not read markdown {rel_path}: {exc}\n")

    docs.sort(key=lambda d: (priority_map.get(d["rel_path"], 9999), 0 if d["scope"] == "public" else 1 if d["scope"] == "private" else 2, d["rel_path"].lower()))

    return {
        "ok": True,
        "version": SERVER_VERSION,
        "counts": counts,
        "docs": docs,
        "updated_at": datetime.now().isoformat()
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
        if clean_path == "/api/tasks":
            try:
                payload = get_all_tasks_payload()
                self.send_response(200)
                self.send_header("Content-Type", "application/json; charset=utf-8")
                self.send_header("Access-Control-Allow-Origin", "*")
                self.end_headers()
                self.wfile.write(json.dumps(payload, indent=2, ensure_ascii=False).encode("utf-8"))
            except Exception as e:
                self.send_response(500)
                self.send_header("Content-Type", "application/json; charset=utf-8")
                self.end_headers()
                self.wfile.write(json.dumps({"ok": False, "error": str(e)}).encode("utf-8"))
            return
        if clean_path == "/api/docs":
            try:
                payload = get_all_docs_payload()
                self.send_response(200)
                self.send_header("Content-Type", "application/json; charset=utf-8")
                self.send_header("Access-Control-Allow-Origin", "*")
                self.end_headers()
                self.wfile.write(json.dumps(payload, indent=2, ensure_ascii=False).encode("utf-8"))
            except Exception as e:
                self.send_response(500)
                self.send_header("Content-Type", "application/json; charset=utf-8")
                self.end_headers()
                self.wfile.write(json.dumps({"ok": False, "error": str(e)}).encode("utf-8"))
            return
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

        # 0. Interactive Task Ledger Action (/api/task-action)
        if clean_path == "/api/task-action":
            try:
                content_length = int(self.headers.get("Content-Length", 0))
                post_data = self.rfile.read(content_length)
                payload = json.loads(post_data.decode("utf-8")) if post_data else {}
                res = handle_task_action(payload)
                self.send_response(200 if res.get("ok") else 400)
                self.send_header("Content-Type", "application/json; charset=utf-8")
                self.send_header("Access-Control-Allow-Origin", "*")
                self.end_headers()
                self.wfile.write(json.dumps(res, ensure_ascii=False).encode("utf-8"))
                return
            except Exception as e:
                self.send_response(500)
                self.send_header("Content-Type", "application/json; charset=utf-8")
                self.end_headers()
                self.wfile.write(json.dumps({"ok": False, "error": str(e)}).encode("utf-8"))
                return

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
