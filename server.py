import http.server
import socketserver
import webbrowser
import threading
import time

PORT = 8000
Handler = http.server.SimpleHTTPRequestHandler

def open_browser():
    time.sleep(1) # Wait for server to start
    webbrowser.open(f"http://localhost:{PORT}")

if __name__ == "__main__":
    print(f"Starting server at http://localhost:{PORT}")
    
    # Run browser opening in a separate thread
    threading.Thread(target=open_browser).start()
    
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServer stopped.")
            httpd.shutdown()
