import json
from redis.asyncio import Redis
from app.core.config import a

class A:
    def __init__(self):
        self.a = Redis.from_url(a.redis_url, decode_responses=True)

    async def b(self, c: str, d: dict):
        return await self.a.xadd(f"sim:{c}:events", {"x": json.dumps(d)})

    async def c(self, d: str, e: str = "0-0", f: int = 100):
        return await self.a.xrange(f"sim:{d}:events", min=e, max="+", count=f)

    async def d(self, e: str, f: dict):
        await self.a.set(f"sim:{e}:state", json.dumps(f), ex=86400)

    async def e(self, f: str):
        g = await self.a.get(f"sim:{f}:state")
        return json.loads(g) if g else None
