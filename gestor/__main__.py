"""python3 -m gestor [--data DIR] [--port 8765] — local single-user server."""
import argparse
from pathlib import Path
from wsgiref.simple_server import make_server

from .web import make_app

p = argparse.ArgumentParser(prog="gestor")
p.add_argument("--data", type=Path, default=Path.home() / ".gestor")
p.add_argument("--port", type=int, default=8765)
a = p.parse_args()
print(f"gestor: http://127.0.0.1:{a.port}  data: {a.data}")
make_server("127.0.0.1", a.port, make_app(a.data)).serve_forever()
