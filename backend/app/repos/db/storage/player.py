"""This is the repository module for players"""

from typing import Optional, Union

from repos.db.base import BaseRepo
from repos.db.models.player import PlayerDB
from schemas.player import PlayerCreateSchema, PlayerUpdateSchema


class PlayerRepo(BaseRepo):
    """This handles players repository operations"""

    def get(self, id: str) -> Optional[PlayerDB]:
        """Get player by id from DB"""
        return super().get(PlayerDB, id)

    def add(self, player: Union[dict, PlayerCreateSchema]) -> PlayerDB:
        """Store player into the DB"""
        return super().add(PlayerDB, player)

    def update(
        self, player: PlayerDB, player_in: Union[dict, PlayerUpdateSchema]
    ) -> PlayerDB:
        """Update an player into the DB"""
        return super().update(player, player_in)
