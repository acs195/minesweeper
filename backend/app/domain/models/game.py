"""This is the domain model module for game"""

from pydantic import BaseModel


class Game(BaseModel):
    """This class represents a game in the domain"""

    id: str
