"""This is a fake repository for testing"""
from uuid import uuid4

from domain.board import Board
from domain.game import Game
from domain.player import Player
from repos.db.models.board import BoardDB
from repos.db.models.game import GameDB
from repos.db.models.player import PlayerDB


class FakeAppRepo:
    datastore = dict()

    def __init__(self):
        self.boards = FakeBoardRepo(Board, BoardDB)
        self.games = FakeGameRepo(Game, GameDB)
        self.players = FakePlayerRepo(Player, PlayerDB)

    def get(self, id):
        return self.datastore.get(self.orm.__tablename__).get(id)

    def add(self, item):
        if isinstance(item, dict):
            if 'id' not in item:
                item['id'] = str(uuid4())
                item = self.model(**item)

        new = {self.orm.__tablename__: {item.id: item}}
        self.datastore.update(new)
        return item

    def remove(self, item):
        del self.datastore[self.orm.__tablename__][item.id]


class FakeGameRepo(FakeAppRepo):
    def __init__(self, model, orm):
        self.model = model
        self.orm = orm

    def get(self, id):
        return super().get(id)

    def add(self, item):
        if item["player_id"]:
            item["player"] = self.datastore["players"][item["player_id"]]
        if item["board_id"]:
            item["board"] = self.datastore["boards"][item["board_id"]]
        return super().add(item)

    def update(self, obj_db, item):
        if isinstance(item, dict):
            item = self.model(**item)
        return super().add(item)

    def remove(self, item):
        super().remove(item)


class FakeBoardRepo(FakeAppRepo):
    def __init__(self, model, orm):
        self.model = model
        self.orm = orm

    def get(self, id):
        return super().get(id)

    def add(self, item):
        return super().add(item)

    def update(self, obj_db, item):
        if isinstance(item, dict):
            item = self.model(**item)
        return super().add(item)

    def remove(self, item):
        super().remove(item)


class FakePlayerRepo(FakeAppRepo):
    def __init__(self, model, orm):
        self.model = model
        self.orm = orm

    def get(self, id):
        return super().get(id)

    def add(self, item):
        return super().add(item)

    def update(self, obj_db, item):
        if isinstance(item, dict):
            item = self.model(**item)
        return super().add(item)

    def remove(self, item):
        super().remove(item)
