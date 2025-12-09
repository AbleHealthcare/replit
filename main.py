import http.server
import socketserver

PORT = 8000

_handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), _handler) as httpd:
    print("Serving at port", PORT)
    httpd.serve_forever()
