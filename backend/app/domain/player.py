"""This is the domain model module for player"""

from pydantic import BaseModel
from typing import Optional


class Player(BaseModel):
    """This class represents a player"""

    id: str
    name: Optional[str]

    class Config:
        orm_mode = True


class AnonymousPlayer(Player):
    """This class represents an anonymous player"""

    pass


class PlayerManager:
    """This class manages player state"""

    def __init__(self, repo):
        self.repo = repo

    def get_or_create(self, id: str = "", name: str = "") -> Player:
        """Get player or create a new one"""
        if id:
            player_db = self.repo.players.get(id=id)
            player = Player.from_orm(player_db)
            return player
        else:
            name = name if name else "anon"
            player_db = self.repo.players.add(dict(name=name))
            player = Player.from_orm(player_db)
            return player
