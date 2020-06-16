"""This module is for custom exceptions"""


class InvalidAmountOfMines(ValueError):
    """Exception for invalid amount of mines"""

    def __init__(self, mines):
        message = f"Cannot place {mines} mines in the board"
        super().__init__(message)


class InvalidPick(ValueError):
    """This is a base exception for invalid picking"""

    pass


class PickOutOrBoard(InvalidPick):
    """Exception for picking a slot out of the board"""

    def __init__(self, pick):
        message = f"Slot {pick.x}x{pick.y} is not in the board"
        super().__init__(message)


class SlotAlreadyPicked(InvalidPick):
    """Exception for picking an previously picked slot"""

    def __init__(self, pick):
        message = f"Slot {pick.x}x{pick.y} is not available"
        super().__init__(message)


class GameIsOver(Exception):
    """Exception when game is over"""

    def __init__(self):
        message = "Game is over"
        super().__init__(message)


class ResourceNotFound(ValueError):
    """Bae exception for resource not found"""


class GameNotFound(ResourceNotFound):
    """Exception when game is not found"""

    def __init__(self, id):
        message = f"Game {id} is not found"
        super().__init__(message)


class PlayerNotFound(ResourceNotFound):
    """Exception when game is not found"""

    def __init__(self, id):
        message = f"Player {id} is not found"
        super().__init__(message)
