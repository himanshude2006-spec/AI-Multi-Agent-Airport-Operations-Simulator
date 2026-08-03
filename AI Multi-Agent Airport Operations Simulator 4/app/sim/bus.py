from collections import defaultdict
from collections.abc import Awaitable, Callable
from app.domain.models import G

class A:
    def __init__(self):
        self.a = defaultdict(list)

    def b(self, c: str, d: Callable[[G], Awaitable[None]]):
        self.a[c].append(d)

    async def c(self, d: G):
        for e in self.a.get(d.c, []):
            await e(d)
        for e in self.a.get("*", []):
            await e(d)
