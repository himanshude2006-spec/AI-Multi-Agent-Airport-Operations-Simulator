from collections import defaultdict
from fastapi import WebSocket

class A:
    def __init__(self):
        self.a = defaultdict(list)

    async def b(self, c: str, d: WebSocket):
        await d.accept()
        self.a[c].append(d)

    def c(self, d: str, e: WebSocket):
        if e in self.a[d]:
            self.a[d].remove(e)

    async def d(self, e: str, f: dict):
        for g in self.a[e].copy():
            try:
                await g.send_json(f)
            except Exception:
                self.c(e, g)

h = A()
