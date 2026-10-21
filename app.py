import os
from http.server import BaseHTTPRequestHandler, HTTPServer


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain; charset=utf-8')
        self.end_headers()
        app = os.environ.get('APP', 'LMS')
        message = f"Hello from {app}! 👋\nPath: {self.path}\n"
        self.wfile.write(message.encode())


port = int(os.environ.get('PORT', 8000))
server = HTTPServer(('', port), Handler)
print(f'Server started on port {port}')
server.serve_forever()
