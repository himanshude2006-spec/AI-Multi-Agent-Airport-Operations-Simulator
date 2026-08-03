from dataclasses import dataclass, field
from typing import Any
from app.domain.enums import A, B

@dataclass
class C:
    a: str
    b: int
    c: int
    d: int
    e: int
    f: list[str]
    g: bool = False
    h: A = A.a
    i: str | None = None
    j: str | None = None
    k: int = 0
    l: int = 0
    m: int = 0
    n: int = 0

@dataclass
class D:
    a: str
    b: int
    c: int = 0
    d: bool = False
    e: int = 0
    f: int = 0

@dataclass
class E:
    a: str
    b: str
    c: int = 0
    d: bool = True
    e: int = 0

@dataclass
class F:
    a: B = B.a
    b: float = 10.0
    c: float = 5.0
    d: set[str] = field(default_factory=set)
    e: float = 1.0

@dataclass
class G:
    a: str
    b: int
    c: str
    d: dict[str, Any]

@dataclass
class H:
    a: str
    b: int
    c: int
    d: int
    e: int
    f: str
    g: str
    h: int

@dataclass
class I:
    a: float = 0.0
    b: int = 0
    c: int = 0
    d: float = 0.0
    e: float = 0.0
    f: int = 0
    g: int = 0
    h: float = 0.0
