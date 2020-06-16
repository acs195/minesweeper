"""This is the repository module for games"""

from typing import Optional, Union

from repos.db.base import BaseRepo
from repos.db.models.game import GameDB
from schemas.game import GameCreateSchema, GameUpdateSchema


class GameRepo(BaseRepo):
    """This handles games repository operations"""

    def get(self, id: str) -> Optional[GameDB]:
        """Get game by id from DB"""
        return super().get(GameDB, id)

    def add(self, game: Union[dict, GameCreateSchema]) -> GameDB:
        """Store game into the DB"""
        return super().add(GameDB, game)

    def update(self, game: GameDB, game_in: Union[dict, GameUpdateSchema]) -> GameDB:
        """Update an game into the DB"""
        return super().update(game, game_in)
