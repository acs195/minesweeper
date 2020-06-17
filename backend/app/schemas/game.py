"""This is the module for API schemas for games"""


from datetime import datetime

from pydantic import BaseModel

from domain.enums import GameStatusEnum
from schemas.board import BoardSchema
from schemas.player import PlayerSchema


class GameSchema(BaseModel):
    """This is the list schema"""

    id: str
    board: BoardSchema
    player: PlayerSchema
    status: GameStatusEnum
    start_time: datetime
    end_time: datetime


class GameCreateSchema(BaseModel):
    """This is the create schema"""

    board: BoardSchema
    player: PlayerSchema
    status: GameStatusEnum
    start_time: datetime
    end_time: datetime


class GameUpdateSchema(BaseModel):
    """This is the update schema"""

    board: BoardSchema
    player: PlayerSchema
    status: GameStatusEnum
    start_time: datetime
    end_time: datetime
