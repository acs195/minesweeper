"""This is the module for API schemas for games"""


from pydantic import BaseModel
from schemas.board import BoardSchema
from schemas.player import PlayerSchema


class GameSchema(BaseModel):
    """This is the list schema"""

    id: str
    board: BoardSchema
    player: PlayerSchema
