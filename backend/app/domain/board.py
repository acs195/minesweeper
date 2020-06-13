"""This is the domain model module for board"""

from uuid import uuid4
from random import randrange
from typing import Optional, List
from pydantic import BaseModel, validator

from utils.exceptions import InvalidAmountOfMines, SlotAlreadyPicked


class Slot(BaseModel):
    """This class represents a slot in the board"""

    mine: bool
    available: bool

    def place_mine(self) -> None:
        self.mine = True

    def pick(self):
        self.available = False


class Board(BaseModel):
    """This class represents a board"""

    id: Optional[str]
    rows: int
    cols: int
    slots: List[List[Slot]] = []
    mines: int = 0

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.slots = self._initiate_slots()

    @validator("id", always=True)
    def auto_generate_id(cls, v):
        return v or str(uuid4())

    def _max_mines(self):
        """Return the max number of mines to be placed in the board"""
        return self.rows * self.cols - 1

    def _initiate_slots(self) -> list:
        """Create an empty 2D array of slots (rows x cols)"""
        slots = []
        for x in range(self.rows):
            row = []
            for y in range(self.cols):
                slot = Slot(mine=False, available=True)
                row.append(slot)
            slots.append(row)
        return slots

    def set_mines(self, mines: int) -> None:
        """Place mines in the board to start a new game"""
        if mines > self._max_mines():
            raise InvalidAmountOfMines(mines)

        self.mines = mines
        mines_placed = 0
        while mines_placed < self.mines:
            random_x = randrange(0, self.rows)
            random_y = randrange(0, self.cols)
            slot = self.slots[random_x][random_y]
            if not slot.mine:
                slot.place_mine()
                mines_placed += 1

    def pick_slot(self, pick):
        """Pick a slot in the board"""
        slot = self.slots[pick.x][pick.y]
        if not slot.available:
            raise SlotAlreadyPicked(pick)
        slot.pick()
