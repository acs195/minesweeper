"""This module is for testing purpose"""

from pytest import fixture
from fastapi.testclient import TestClient
from main import app


class FakeRepo:
    datastore = dict()

    def add(self, model, item):
        new = {model: {item.id: item}}
        self.datastore.update(new)

    def remove(self, model, item):
        del self.datastore[model][item.id]


class FakeGameRepo(FakeRepo):
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
