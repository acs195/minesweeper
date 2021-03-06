"""This is the module for API schemas for games"""


from datetime import datetime
from typing import Optional

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
    end_time: Optional[datetime]


class GameParamsSchema(BaseModel):
    """This is the start game schema"""

    rows: int
    cols: int
    mines: int


class GameCreateSchema(BaseModel):
    """This is the create schema"""

    board: BoardSchema
    player: PlayerSchema
    status: GameStatusEnum
    start_time: datetime
    end_time: Optional[datetime]


class GameUpdateSchema(BaseModel):
    """This is the update schema"""

    board: BoardSchema
    player: PlayerSchema
    status: GameStatusEnum
    start_time: datetime
    end_time: Optional[datetime]
