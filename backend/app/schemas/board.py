"""This is the module for API schemas for games"""

from pydantic import BaseModel
from typing import List


class SlotSchema(BaseModel):
    """This is the list schema"""

    available: bool
    mine: bool


class BoardSchema(BaseModel):
    """This is the list schema"""

    id: str
    slots: List[List[SlotSchema]]
    mines: int
    rows: int
    cols: int
