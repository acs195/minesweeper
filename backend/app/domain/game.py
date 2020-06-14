"""This is the domain model module for game"""

from typing import Optional
from uuid import uuid4

from pydantic import BaseModel, validator

from domain.board import Board
from domain.player import Player

DEFAULT_MINES = 8
DEFAULT_BOARD_ROWS = 8
DEFAULT_BOARD_COLS = 8


class Game(BaseModel):
    """This class represents a game"""

    id: Optional[str]
    player: Player
    board: Board

    @validator("id", always=True)
    def auto_generate_id(cls, v):
        return v or str(uuid4())

    def pick_slot(self, pick):
        """Pick a slot in the board"""
        self.board.pick_slot(pick)

    @property
    def visual_board(self):
        """Return a visual representation of the board
        Symbols:
            ~ indicates the slot is available and there is a mine behind it
            · indicates the slot is available and clear
            X indicates a picked mine (game over)
              (empty) indicates the slot was already picked (no mine)
        """
        visual_repr = "   " + " ".join([str(i) for i in range(self.board.cols)])
        for i, row in enumerate(self.board.slots):
            line = f'{i} '
            for slot in row:
                if slot.available and slot.mine:
                    line += ' ~'
                elif slot.available and not slot.mine:
                    line += ' ·'
                elif not slot.available and slot.mine:
                    line += ' X'
                elif not slot.available and not slot.mine:
                    line += '  '
            visual_repr += f"\n{line}"
        return visual_repr


class GameFactory:
    """This class is used to instanciate a game"""

    def __init__(self, repo):
        self.repo = repo

    def start(self, player: Player) -> Game:
        """Prepare the board and start the game"""
        board = Board(rows=DEFAULT_BOARD_ROWS, cols=DEFAULT_BOARD_ROWS)
        board.set_mines(mines=DEFAULT_MINES)
        game = Game(player=player, board=board)
        self.repo.add(game)
        return game
