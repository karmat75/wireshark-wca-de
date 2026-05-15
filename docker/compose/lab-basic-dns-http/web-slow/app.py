from http.server import BaseHTTPRequestHandler, HTTPServer
import time

class Handler(BaseHTTPRequestHandler):
    protocol_version = "HTTP/1.1"

    def do_HEAD(self):
        time.sleep(2)
        self.send_response(200)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.send_header("Content-Length", "0")
        self.send_header("X-WWCA-Lab", "slow-response")
        self.end_headers()

    def do_GET(self):
        time.sleep(2)
        body = b"Slow response from Wireshark WCA DE lab.\n"
        self.send_response(200)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("X-WWCA-Lab", "slow-response")
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, fmt, *args):
        print("%s - - [%s] %s" % (self.client_address[0], self.log_date_time_string(), fmt % args), flush=True)

if __name__ == "__main__":
    server = HTTPServer(("0.0.0.0", 80), Handler)
    print("Starting slow lab web server on port 80", flush=True)
    server.serve_forever()
