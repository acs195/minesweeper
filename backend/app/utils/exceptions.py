"""This module is for custom exceptions"""


class InvalidAmountOfMines(Exception):
    """Exception for invalid amount of mines"""

    def __init__(self, mines):
        message = f"Cannot place {mines} mines in the board"
        super().__init__(message)


class SlotAlreadyPicked(Exception):
    """Exception for picking an previously picked slot"""

    def __init__(self, pick):
        message = f"Cannot pick slot {pick.x}x{pick.y}"
        super().__init__(message)
