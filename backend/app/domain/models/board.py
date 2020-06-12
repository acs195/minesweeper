"""This is the domain model module for board"""

from pydantic import BaseModel


class Board(BaseModel):
    """This class represents a board in the domain"""

    id: str
