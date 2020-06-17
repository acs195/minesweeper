"""This module is for testing purpose"""

from fastapi.testclient import TestClient
from pytest import fixture

from domain.game import GameFactory
from domain.player import PlayerManager
from main import app
from tests.fake_repo import FakeAppRepo


@fixture
def fake_repo():
    repo = FakeAppRepo()
    return repo


@fixture
def test_client():
    client = TestClient(app)
    return client


@fixture
def player(fake_repo):
    player_manager = PlayerManager(fake_repo)
    return player_manager.get_or_create()


@fixture
def game(fake_repo, player):
    game_factory = GameFactory(fake_repo)
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
