from typing import TypedDict
from langgraph.graph import StateGraph, END
from app.ai.advisor import A

class B(TypedDict):
    a: dict
    b: dict | None
    c: bool
    d: dict | None

async def e(f: B):
    f["b"] = await A().b(f["a"])
    return f

async def g(f: B):
    h = f.get("b") or {}
    f["c"] = h.get("action") in {"none", "prioritize", "hold", "divert"}
    return f

async def i(f: B):
    f["d"] = f["b"] if f["c"] else {"action": "none", "reason": "invalid"}
    return f

def j():
    k = StateGraph(B)
    k.add_node("a", e)
    k.add_node("b", g)
    k.add_node("c", i)
    k.set_entry_point("a")
    k.add_edge("a", "b")
    k.add_edge("b", "c")
    k.add_edge("c", END)
    return k.compile()

l = j()
