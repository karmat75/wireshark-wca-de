from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
import base64
import json
import time


class Handler(BaseHTTPRequestHandler):
    protocol_version = "HTTP/1.1"

    def _send_text(self, status, body, extra_headers=None):
        data = body.encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.send_header("Content-Length", str(len(data)))
        self.send_header("X-WWCA-Lab", "security-basics")
        if extra_headers:
            for key, value in extra_headers.items():
                self.send_header(key, value)
        self.end_headers()
        self.wfile.write(data)

    def do_GET(self):
        parsed = urlparse(self.path)

        if parsed.path == "/":
            self._send_text(200, "Wireshark WCA DE Security Basics Lab\n")
            return

        if parsed.path == "/basic":
            auth = self.headers.get("Authorization", "")
            expected = "Basic " + base64.b64encode(b"labuser:LabPassword123").decode("ascii")
            if auth == expected:
                self._send_text(200, "Basic auth accepted for synthetic lab user.\n")
            else:
                self._send_text(
                    401,
                    "Basic auth required for lab.\n",
                    {"WWW-Authenticate": 'Basic realm="WWCA Lab"'},
                )
            return

        if parsed.path == "/beacon":
            query = parse_qs(parsed.query)
            response = {
                "status": "ok",
                "lab": "security-basics",
                "received": query,
                "timestamp": int(time.time()),
            }
            self._send_text(200, json.dumps(response, sort_keys=True) + "\n")
            return

        self._send_text(404, "Not found.\n")

    def do_POST(self):
        parsed = urlparse(self.path)
        length = int(self.headers.get("Content-Length", "0") or "0")
        body = self.rfile.read(length).decode("utf-8", errors="replace")

        if parsed.path == "/login":
            self._send_text(200, "Synthetic login data received: " + body + "\n")
            return

        self._send_text(404, "Not found.\n")

    def log_message(self, fmt, *args):
        print("%s - - [%s] %s" % (self.client_address[0], self.log_date_time_string(), fmt % args), flush=True)


if __name__ == "__main__":
    server = HTTPServer(("0.0.0.0", 80), Handler)
    print("Starting WWCA security basics lab server on port 80", flush=True)
    server.serve_forever()
