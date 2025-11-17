
#!/usr/bin/env python3
import http.server
import socketserver
import os
import webbrowser

PORT = 8080

def start_frontend():
    os.chdir("frontend")

    handler = http.server.SimpleHTTPRequestHandler
    with socketserver.TCPServer(("", PORT), handler) as httpd:
        print(f"🌐 Frontend server running at http://localhost:{PORT}")
        print("📁 Serving files from frontend directory")
        print("🛑 Press Ctrl+C to stop the server")

        # Open browser automatically
        webbrowser.open(f'http://localhost:{PORT}')

        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n⏹️  Frontend server stopped")

if __name__ == "__main__":
    start_frontend()
