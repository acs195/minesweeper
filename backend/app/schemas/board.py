"""This is the module for API schemas for games"""

from pydantic import BaseModel
from typing import List


class SlotSchema(BaseModel):
    """This is the list schema"""

    available: bool
    mine: bool
    flag: bool


class PickSlotSchema(BaseModel):
    """This is the schema for picking a slot"""

    x: int
    y: int


class BoardSchema(BaseModel):
    """This is the list schema"""

    id: str
    slots: List[List[SlotSchema]]
    mines: int
    rows: int
    cols: int


class BoardCreateSchema(BaseModel):
    """This is the create schema"""

    slots: List[List[dict]]
    mines: int
    rows: int
    cols: int


class BoardUpdateSchema(BaseModel):
    """This is the update schema"""

    slots: List[List[dict]]
    mines: int
    rows: int
    cols: int
