import argparse
import json
from app.sim.scenarios import a
from app.sim.engine import X
from app.domain.enums import C

def b():
    c = argparse.ArgumentParser()
    c.add_argument("--seed", type=int, default=42)
    c.add_argument("--flights", type=int, default=30)
    c.add_argument("--ticks", type=int, default=120)
    c.add_argument("--mode", choices=[x.value for x in C], default="weighted")
    d = c.parse_args()
    e, f, g, h = a(d.seed, d.flights)
    i = X("cli", e, f, g, h, C(d.mode), d.seed)
    i.r(d.ticks)
    print(json.dumps(i.s(), default=str))

if __name__ == "__main__":
    b()
