from pytest import raises

from domain.board import Board
from domain.game import GameFactory
from domain.player import AnonymousPlayer
from schemas.board import PickSlotSchema
from utils.exceptions import SlotAlreadyPicked


def test_new_game(fake_game_repo):
    """Test to create a new game"""
    player = AnonymousPlayer()
    game_factory = GameFactory(fake_game_repo)
    new_game = game_factory.start(player)
    assert new_game.player == player
    assert isinstance(new_game.board, Board)


def test_game_pick_slot(game):
    """Test to pick a slot during the game"""
    x, y = 2, 3
    pick = PickSlotSchema(x=x, y=y)
    picked_slot = game.board.slots[x][y]

    assert picked_slot.available is True
    game.pick_slot(pick)
    assert picked_slot.available is False


def test_pick_slot_already_picked(game):
    """Test to pick a slot already picked during the game"""
    x, y = 2, 3
    pick = PickSlotSchema(x=x, y=y)
    picked_slot = game.board.slots[x][y]

    assert picked_slot.available is True
    game.pick_slot(pick)
    assert picked_slot.available is False

    with raises(SlotAlreadyPicked):
        game.pick_slot(pick)
