import http.server
import socketserver
import os

# Retrieve environment variable or use a default value if it's not set
HELLO_WORLD_TEXT = os.getenv('HELLO_WORLD_TEXT', 'This is a default message')

class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Prepare the HTML content
        html_content = f"<html><body><h1>Hello World! {HELLO_WORLD_TEXT}</h1></body></html>".encode('utf-8')
        
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(html_content)

PORT = 8000

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"HELLO WORLD is being served at port {PORT}")
    httpd.serve_forever()
