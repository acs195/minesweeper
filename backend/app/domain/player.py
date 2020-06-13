"""This is the domain model module for player"""

from uuid import uuid4
from pydantic import BaseModel, validator
from typing import Optional


class Player(BaseModel):
    """This class represents a player"""

    id: Optional[str]

    @validator("id", always=True)
    def auto_generate_id(cls, v):
        return v or str(uuid4())


class AnonymousPlayer(Player):
    """This class represents an anonymous player"""

    pass
