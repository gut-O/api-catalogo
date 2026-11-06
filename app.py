"""API de catálogo demonstrativa, usando apenas a biblioteca padrão."""
from http.server import BaseHTTPRequestHandler, HTTPServer
import json

PRODUCTS = [
    {"id": 1, "nome": "Caderno pontilhado", "categoria": "papelaria", "preco": 29.9, "estoque": 18},
    {"id": 2, "nome": "Caneca térmica", "categoria": "casa", "preco": 79.9, "estoque": 7},
    {"id": 3, "nome": "Luminária de mesa", "categoria": "casa", "preco": 119.0, "estoque": 4},
]


class CatalogHandler(BaseHTTPRequestHandler):
    def send_json(self, payload, status=200):
        body = json.dumps(payload, ensure_ascii=False).encode()
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):  # noqa: N802
        if self.path == "/saude":
            return self.send_json({"status": "ok"})
        if self.path == "/produtos":
            return self.send_json({"itens": PRODUCTS, "total": len(PRODUCTS)})
        self.send_json({"erro": "rota não encontrada"}, 404)


if __name__ == "__main__":
    print("API em http://127.0.0.1:8090")
    HTTPServer(("127.0.0.1", 8090), CatalogHandler).serve_forever()
