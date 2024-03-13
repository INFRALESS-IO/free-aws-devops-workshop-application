# app.py
import http.server
import socketserver

class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b"Hello, World!")

PORT = 8000

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("HELLO WORLD is being served at port", PORT)
    httpd.serve_forever()
