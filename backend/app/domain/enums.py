"""This module contains Enums"""

from enum import Enum


class GameStatusEnum(Enum):
    """Game status"""

    ongoing = 1
    won = 2
    lost = 3
