"""This module contains the game repository"""

from repos.in_memory.base import BaseRepo


class GameRepo(BaseRepo):
    """This is the Game Repository class"""

    MODEL = "games"

    def get(self, id):
        """Get a game by id"""
        return super().get(self.MODEL, id)

    def add(self, item):
        """Create and return a game"""
        return super().add(self.MODEL, item)

    def delete(self, id):
        """Delete a game by id"""
        super().get(self.MODEL, id)
