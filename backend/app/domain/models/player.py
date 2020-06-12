"""This is the domain model module for player"""

from pydantic import BaseModel


class Player(BaseModel):
    """This class represents a player in the domain"""

    id: str
