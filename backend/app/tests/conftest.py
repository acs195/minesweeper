"""This module is for testing purpose"""

from fastapi.testclient import TestClient
from pytest import fixture

from domain.game import GameFactory
from domain.player import AnonymousPlayer
from main import app


class FakeRepo:
    datastore = dict()

    def get(self, model, id):
        return self.datastore.get(model).get(id)

    def add(self, model, item):
        new = {model: {item.id: item}}
        self.datastore.update(new)

    def remove(self, model, item):
        del self.datastore[model][item.id]


class FakeGameRepo(FakeRepo):
    def get(self, id):
        return super().get("games", id)

    def add(self, item):
        super().add("games", item)

    def remove(self, item):
        super().remove("games", item)


@fixture
def fake_game_repo():
    repo = FakeGameRepo()
    return repo


@fixture
def test_client():
    client = TestClient(app)
    return client


@fixture
def game(fake_game_repo):
    player = AnonymousPlayer()
    game_factory = GameFactory(fake_game_repo)
    game = game_factory.start(player)

    mines = [
        (1, 2),
        (1, 4),
        (3, 4),
        (3, 6),
        (5, 6),
        (5, 7),
        (7, 2),
        (7, 4),
    ]
    for row_idx, row in enumerate(game.board.slots):
        for col_idx, slot in enumerate(row):
            if (row_idx, col_idx) in mines:
                slot.mine = True
            else:
                slot.mine = False
    return game
