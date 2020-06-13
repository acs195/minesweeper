"""This module is for custom exceptions"""


class InvalidAmountOfMines(Exception):
    """Exception for invalid amount of mines"""

    def __init__(self, mines):
        message = f"Cannot place {mines} mines in the board"
        super().__init__(message)
