"""This is the module with the DB repositories"""
from repos.db.storage.board import BoardRepo
from repos.db.storage.game import GameRepo
from repos.db.storage.player import PlayerRepo
from repos.db.database import get_db


class AppRepo:
    """This class gathers all repos"""

    def __init__(self):
        db = next(get_db())
        self.boards = BoardRepo(db)
        self.games = GameRepo(db)
        self.players = PlayerRepo(db)


repo = AppRepo()
