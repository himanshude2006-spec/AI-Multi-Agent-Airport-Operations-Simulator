import json
import time
from app.core.config import a

class A:
    async def b(self, c: dict):
        if not a.openai_api_key:
            return {"action": "none", "reason": "no_key"}
        from openai import AsyncOpenAI
        d = AsyncOpenAI(api_key=a.openai_api_key)
        e = time.perf_counter()
        f = await d.responses.create(
            model="gpt-4.1-mini",
            input="Return JSON with action and reason for this airport state: " + json.dumps(c),
            text={"format": {"type": "json_object"}}
        )
        g = (time.perf_counter() - e) * 1000
        try:
            h = json.loads(f.output_text)
        except Exception:
            h = {"action": "none", "reason": f.output_text}
        h["latency_ms"] = g
        return h
