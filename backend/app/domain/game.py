"""This is the domain model module for game"""

from datetime import datetime
from typing import Optional

from pydantic import BaseModel

from domain.board import Board, Slot
from domain.enums import GameStatusEnum
from domain.player import Player
from utils.exceptions import GameIsOver, GameNotFound, PickOutOrBoard

DEFAULT_MINES = 8
DEFAULT_BOARD_ROWS = 8
DEFAULT_BOARD_COLS = 8


class Game(BaseModel):
    """This class represents a game"""

    id: str
    player: Player
    board: Board
    status: GameStatusEnum
    start_time: datetime
    end_time: Optional[datetime]

    class Config:
        orm_mode = True

    def pick_slot(self, pick):
        """Pick a slot in the board"""
        self._check_game_over()
        self._validate_pick(pick)

        slot = self.board.pick_slot(pick)
        if slot.mine:
            self.status = GameStatusEnum.lost
            self.end_time = datetime.utcnow()
        else:
            self._check_for_win()

    def toggle_flag_slot(self, pick):
        """Flag a slot in the board"""
        self._check_game_over()
        self._validate_pick(pick)

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

    def _validate_pick(self, pick):
        if pick.x < 0 or pick.x >= self.board.rows:
            raise PickOutOrBoard(pick)
        if pick.y < 0 or pick.y >= self.board.cols:
            raise PickOutOrBoard(pick)

    def _check_game_over(self):
        if self.game_over:
            raise GameIsOver()

    def _check_for_win(self):
        """Check if won the game"""
        slots_available = any(
            [slot.available for slot in self.board.iter_slots() if not slot.mine]
        )
        if not slots_available:
            self.status = GameStatusEnum.won
            self.end_time = datetime.utcnow()


class GameFactory:
    """This class is used to instanciate a game"""

    def __init__(self, repo):
        self.repo = repo

    def start(self, player: Player) -> Game:
        """Prepare the board and start the game"""
        board_payload = dict(rows=DEFAULT_BOARD_ROWS, cols=DEFAULT_BOARD_ROWS)
        initial_slots = self._get_initial_slots(**board_payload)
        board_db = self.repo.boards.add(
            {**board_payload, "slots": initial_slots, "mines": 0}
        )
        board = Board.from_orm(board_db)

        board.set_mines(mines=DEFAULT_MINES)
        board_db = self.repo.boards.update(board_db, board)

        game_payload = dict(
            player_id=player.id,
            board_id=board.id,
            status=GameStatusEnum.ongoing,
            start_time=datetime.utcnow(),
        )
        game_db = self.repo.games.add(game_payload)
        game = Game.from_orm(game_db)
        return game

    def _get_initial_slots(self, rows, cols) -> list:
        """Create an empty 2D array of slots (rows x cols)"""
        slots = []
        for x in range(rows):
            row = []
            for y in range(cols):
                slot = Slot(x=x, y=y, mine=False, available=True, flag=False)
                row.append(slot)
            slots.append(row)
        return slots


class PickSlot:
    """This class is for pick slot use case"""

    def __init__(self, repo, game_id: str, pick: dict):
        self.repo = repo
        self.game_id = game_id
        self.pick = pick

    def execute(self):
        game_db = self.repo.games.get(id=self.game_id)
        if not game_db:
            raise GameNotFound(self.game_id)

        game = Game.from_orm(game_db)
        game.pick_slot(self.pick)
        game_db = self.repo.games.update(game_db, game)
        self.repo.boards.update(game_db.board, game.board)
        return game


class ToggleFlagSlot:
    """This class is for toggle flag slot use case"""

    def __init__(self, repo, game_id: str, pick: dict):
        self.repo = repo
        self.game_id = game_id
        self.pick = pick

    def execute(self):
        game_db = self.repo.games.get(id=self.game_id)
        if not game_db:
            raise GameNotFound(self.game_id)

        game = Game.from_orm(game_db)
        game.toggle_flag_slot(self.pick)
        self.repo.boards.update(game_db.board, game.board)
        return game
