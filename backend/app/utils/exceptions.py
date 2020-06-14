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


class GameIsOver(Exception):
    """Exception when game is over"""

    def __init__(self):
        message = "Game is over"
        super().__init__(message)
