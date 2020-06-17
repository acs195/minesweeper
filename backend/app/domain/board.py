"""This is the domain model module for board"""

from random import randrange
from typing import List, Union

from pydantic import BaseModel

from schemas.board import PickSlotSchema
from utils.exceptions import InvalidAmountOfMines, SlotAlreadyPicked


class Slot(BaseModel):
    """This class represents a slot in the board"""

    x: int
    y: int
    mine: bool = False
    available: bool = True
    flag: bool = False

    def place_mine(self) -> None:
        self.mine = True

    def pick(self):
        self.available = False
        if self.flag:
            self.flag = False

    def toggle_flag(self):
        self.flag = not self.flag


class Board(BaseModel):
    """This class represents a board"""

    id: str
    rows: int
    cols: int
    slots: List[List[Union[Slot]]] = [[]]
    mines: int = 0

    class Config:
        orm_mode = True

    def _max_mines(self) -> int:
        """Return the max number of mines to be placed in the board"""
        return self.rows * self.cols - 1

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

    def pick_slot(self, pick: PickSlotSchema) -> Slot:
        """Pick a slot in the board"""
        slot = self.slots[pick.x][pick.y]
        if not slot.available:
            raise SlotAlreadyPicked(pick)

        slot.pick()
        if not slot.mine:
            self._clear_adjacent_slots(pick)

        return slot

    def _clear_adjacent_slots(self, pick):
        """Clear adjacent slots when there is no mine around"""
        available_adjacent_slots = self._get_available_adjacent_slots(pick)
        are_mines = any([slot.mine for slot in available_adjacent_slots])

        while len(available_adjacent_slots) > 0 and not are_mines:
            for slot in available_adjacent_slots:
                slot.pick()
                new_pick = PickSlotSchema(x=slot.x, y=slot.y)
                self._clear_adjacent_slots(new_pick)

            available_adjacent_slots = self._get_available_adjacent_slots(pick)
            are_mines = any([slot.mine for slot in available_adjacent_slots])

    def _get_available_adjacent_slots(self, pick):
        """Get a list of all available adjacent slot of a pick"""
        adjacent_slots = []
        # West
        if pick.x - 1 >= 0:
            slot = self.slots[pick.x - 1][pick.y]
            if slot.available:
                adjacent_slots.append(slot)
        # North-West
        if pick.x - 1 >= 0 and pick.y - 1 >= 0:
            slot = self.slots[pick.x - 1][pick.y - 1]
            if slot.available:
                adjacent_slots.append(slot)
        # North
        if pick.y - 1 >= 0:
            slot = self.slots[pick.x][pick.y - 1]
            if slot.available:
                adjacent_slots.append(slot)
        # North-East
        if pick.x + 1 < self.cols and pick.y - 1 >= 0:
            slot = self.slots[pick.x + 1][pick.y - 1]
            if slot.available:
                adjacent_slots.append(slot)
        # East
        if pick.x + 1 < self.cols:
            slot = self.slots[pick.x + 1][pick.y]
            if slot.available:
                adjacent_slots.append(slot)
        # South-East
        if pick.x + 1 < self.cols and pick.y + 1 < self.rows:
            slot = self.slots[pick.x + 1][pick.y + 1]
            if slot.available:
                adjacent_slots.append(slot)
        # South
        if pick.y + 1 < self.rows:
            slot = self.slots[pick.x][pick.y + 1]
            if slot.available:
                adjacent_slots.append(slot)
        # South-West
        if pick.x - 1 >= 0 and pick.y + 1 < self.rows:
            slot = self.slots[pick.x - 1][pick.y + 1]
            if slot.available:
                adjacent_slots.append(slot)

        return adjacent_slots

    def toggle_flag_slot(self, pick: PickSlotSchema) -> None:
        """Flag a slot in the board"""
        slot = self.slots[pick.x][pick.y]
        if not slot.available:
            raise SlotAlreadyPicked(pick)

        slot.toggle_flag()

    def iter_slots(self):
        """Iterate over the slots as it was a 1D list"""
        for row in self.slots:
            for slot in row:
                yield slot
