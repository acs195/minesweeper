"""This is the repository module for boards"""

from typing import Optional, Union

from repos.db.base import BaseRepo
from repos.db.models.board import BoardDB
from schemas.board import BoardCreateSchema, BoardUpdateSchema


class BoardRepo(BaseRepo):
    """This handles boards repository operations"""

    def get(self, id: str) -> Optional[BoardDB]:
        """Get board by id from DB"""
        return super().get(BoardDB, id)

    def add(self, board: Union[dict, BoardCreateSchema]) -> BoardDB:
        """Store board into the DB"""
        return super().add(BoardDB, board)

    def update(
        self, board: BoardDB, board_in: Union[dict, BoardUpdateSchema]
    ) -> BoardDB:
        """Update an board into the DB"""
        return super().update(board, board_in)
