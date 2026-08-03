import logging
import sys

def a():
    b = logging.getLogger()
    b.setLevel(logging.INFO)
    c = logging.StreamHandler(sys.stdout)
    c.setFormatter(logging.Formatter("%(asctime)s %(levelname)s %(name)s %(message)s"))
    b.handlers = [c]
