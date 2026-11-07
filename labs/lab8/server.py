import time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

text = "<html><body><h1>ADRENALINE</h1>"
text = text + "<p>каталог спортивной одежды</p>" * 200
text = text + "</body></html>"
page = text.encode("utf8")


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        time.sleep(0.02)
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(page)))
        self.end_headers()
        self.wfile.write(page)

    def log_message(self, *args):
        pass


server = ThreadingHTTPServer(("127.0.0.1", 8088), Handler)
print("Сервер запущен: http://127.0.0.1:8088/")
server.serve_forever()
