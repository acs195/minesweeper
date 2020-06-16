"""This is the module for API schemas for players"""

from pydantic import BaseModel
from typing import Optional


class PlayerSchema(BaseModel):
    """This is the list schema"""

    id: str
    name: Optional[str]


class PlayerCreateSchema(BaseModel):
    """This is the create schema"""

    name: Optional[str]


class PlayerUpdateSchema(BaseModel):
    """This is the update schema"""

    name: Optional[str]
