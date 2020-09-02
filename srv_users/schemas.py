from typing import List, Optional

from pydantic import BaseModel


class Role(BaseModel):
    id: int
    name: str


class State(BaseModel):
    id: int
    name: str
    tax_rate: float
    abbreviation: str
