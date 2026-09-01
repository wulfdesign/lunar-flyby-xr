"""
Zero-Dependency Local Server for Artemis: The Free Return (Lunar Flyby XR)
Hosts on port 3550 and displays local LAN IP for Meta Quest headset connection.
"""

import http.server
import socketserver
import socket
import webbrowser
import os

PORT = 3550

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
    
    print("=" * 65)
    print("🚀 ARTEMIS: THE FREE RETURN — LOCAL WEBXR DEMO SERVER")
    print("=" * 65)
    print(f"💻 Laptop Localhost URL:    http://localhost:{PORT}")
    print(f"🥽 Meta Quest Headset URL:  http://{local_ip}:{PORT}")
    print(f"🌐 Cloud Production URL:    https://wulfdesign.github.io/lunar-flyby-xr/")
    print("=" * 65)
    print("👉 Open the Headset URL in the Meta Quest Browser to launch WebXR!")
    print("Press Ctrl+C to stop the server.")
    print("=" * 65)
    
    # Auto launch laptop browser
    try:
        webbrowser.open(f"http://localhost:{PORT}/index.html")
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
