from pydantic import BaseModel, Field
from app.domain.enums import C

class A(BaseModel):
    a: int = 42
    b: int = Field(default=30, ge=1, le=500)
    c: C = C.c
    d: str = "demo"

class B(BaseModel):
    a: int = Field(default=1, ge=1, le=10000)

class C1(BaseModel):
    a: int = 100
    b: int = 120
    c: int = 30

class D(BaseModel):
    a: str
    b: dict = {}
