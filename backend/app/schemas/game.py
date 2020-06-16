"""This is the module for API schemas for games"""


from pydantic import BaseModel
from schemas.board import BoardSchema
from schemas.player import PlayerSchema
from domain.enums import GameStatusEnum


class GameSchema(BaseModel):
    """This is the list schema"""

    id: str
    board: BoardSchema
    player: PlayerSchema
    status: GameStatusEnum


class GameCreateSchema(BaseModel):
    """This is the create schema"""

    board: BoardSchema
    player: PlayerSchema
    status: GameStatusEnum


class GameUpdateSchema(BaseModel):
    """This is the update schema"""

    board: BoardSchema
    player: PlayerSchema
    status: GameStatusEnum
