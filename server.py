"""
Zero-Dependency Local Server for Artemis: The Free Return (Lunar Flyby XR)
Hosts on port 3550 and displays local LAN IP for Meta Quest headset connection.
"""

import http.server
import socketserver
import socket
import webbrowser
import os
import sys

PORT = 3550
SERVER_VERSION = "2.1.8"

def get_local_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception:
        return "127.0.0.1"

def run_server():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    local_ip = get_local_ip()
    is_dev = "--dev" in sys.argv
    launch_path = "/dev/index.html" if is_dev else "/index.html"
    
    print("=" * 68)
    print(f"🚀 ARTEMIS: THE FREE RETURN — {'DEV SANDBOX' if is_dev else 'LOCAL DEMO'} (v{SERVER_VERSION})")
    print("=" * 68)
    print(f"💻 Dev Sandbox (Laptop):   http://localhost:{PORT}/dev/index.html")
    print(f"🥽 Dev Sandbox (Quest 3):  http://{local_ip}:{PORT}/dev/index.html")
    print(f"🏛️ Public Baseline:        http://localhost:{PORT}/index.html")
    print(f"🌐 Cloud Production:       https://wulfdesign.github.io/lunar-flyby-xr/")
    print("=" * 68)
    print("👉 Open the Headset URL in the Meta Quest Browser to launch WebXR!")
    print("Press Ctrl+C to stop the server.")
    print("=" * 68)
    
    # Auto launch browser
    try:
        webbrowser.open(f"http://localhost:{PORT}{launch_path}")
    except Exception:
        pass
    
    handler = http.server.SimpleHTTPRequestHandler
    handler.extensions_map.update({
        '.wasm': 'application/wasm',
        '.glb': 'model/gltf-binary',
        '.gltf': 'model/gltf+json'
    })
    
    with socketserver.TCPServer(("", PORT), handler) as httpd:
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nShutting down demo server.")

if __name__ == '__main__':
    run_server()
