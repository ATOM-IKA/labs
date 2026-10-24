"""Локальный тестовый сервер для нагрузочного теста (лаба 8). Имитирует страницу с задержкой ~20 мс."""
import time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

PAGE = ("<html><body><h1>ADRENALINE</h1>" + "<p>каталог спортивной одежды</p>" * 200 + "</body></html>").encode("utf8")


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        time.sleep(0.02)
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(PAGE)))
        self.end_headers()
        self.wfile.write(PAGE)

    def log_message(self, *a):
        pass


if __name__ == "__main__":
    ThreadingHTTPServer(("127.0.0.1", 8088), Handler).serve_forever()
