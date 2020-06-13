"""This is the domain model module for game"""

from typing import Optional
from uuid import uuid4

from pydantic import BaseModel, validator

from domain.board import Board
from domain.player import Player

DEFAULT_MINES = 8
DEFAULT_BOARD_ROWS = 8
DEFAULT_BOARD_COLS = 8


class GameFactory:
    """This class is used to instanciate a game"""

    def __init__(self, repo):
        self.repo = repo

    def start(self, player):
        board = Board(rows=DEFAULT_BOARD_ROWS, cols=DEFAULT_BOARD_ROWS)
        board.set_mines(mines=DEFAULT_MINES)
        game = Game(player=player, board=board)
        self.repo.add(game)
        return game


class Game(BaseModel):
    """This class represents a game"""

    id: Optional[str]
    player: Player
    board: Board

    @validator("id", always=True)
    def auto_generate_id(cls, v):
        return v or str(uuid4())
