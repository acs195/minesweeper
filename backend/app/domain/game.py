"""This is the domain model module for game"""

from typing import Optional
from uuid import uuid4
from enum import Enum

from pydantic import BaseModel, validator

from utils.exceptions import GameIsOver
from domain.board import Board
from domain.player import Player

DEFAULT_MINES = 8
DEFAULT_BOARD_ROWS = 8
DEFAULT_BOARD_COLS = 8


class GameStatusEnum(Enum):
    """Game status"""

    ongoing = 1
    won = 2
    lost = 3


class Game(BaseModel):
    """This class represents a game"""

    id: Optional[str]
    player: Player
    board: Board
    status: GameStatusEnum = GameStatusEnum.ongoing

    @validator("id", always=True)
    def auto_generate_id(cls, v):
        return v or str(uuid4())

    def pick_slot(self, pick):
        """Pick a slot in the board"""
        if self.game_over:
            raise GameIsOver()

        slot = self.board.pick_slot(pick)
        if slot.mine:
            self.status = GameStatusEnum.lost
        else:
            self._check_for_win()

    def toggle_flag_slot(self, pick):
        """Flag a slot in the board"""
        if self.game_over:
            raise GameIsOver()

        self.board.toggle_flag_slot(pick)

    @property
    def game_over(self):
        return self.status in (GameStatusEnum.won, GameStatusEnum.lost)

    @property
    def visual_board(self):
        """Return a visual representation of the board
        Symbols:
            ! indicates the slot is flagged
            ~ indicates the slot is available and there is a mine behind it
            · indicates the slot is available and clear
            X indicates a picked mine (game over)
              (empty) indicates the slot was already picked (no mine)
        """
        visual_repr = "   " + " ".join([str(i) for i in range(self.board.cols)])
        for i, row in enumerate(self.board.slots):
            line = f"{i} "
            for slot in row:
                if slot.flag:
                    line += " !"
                elif slot.available and slot.mine:
                    line += " ~"
                elif slot.available and not slot.mine:
                    line += " ·"
                elif not slot.available and slot.mine:
                    line += " X"
                elif not slot.available and not slot.mine:
                    line += "  "
            visual_repr += f"\n{line}"
        return visual_repr

    def _check_for_win(self):
        """Check if won the game"""
        slots_available = any(
            [slot.available for slot in self.board.iter_slots() if not slot.mine]
        )
        if not slots_available:
            self.status = GameStatusEnum.won


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
