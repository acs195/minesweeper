from pytest import raises

from domain.board import Board
from domain.game import GameFactory, GameStatusEnum
from domain.player import AnonymousPlayer
from schemas.board import PickSlotSchema
from utils.exceptions import SlotAlreadyPicked, GameIsOver


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


def test_loss_game(game):
    """Test to loss a game"""
    x, y = 5, 6
    pick = PickSlotSchema(x=x, y=y)
    picked_slot = game.board.slots[x][y]

    assert picked_slot.mine is True
    game.pick_slot(pick)
    assert game.status == GameStatusEnum.lost


def test_win_game(game):
    """Test to win a game"""
    # Set all slots as picked
    for slot in game.board.iter_slots():
        slot.available = True if slot.mine else False

    # Set only one slot to be available
    x, y = 2, 3
    game.board.slots[x][y].available = True

    pick = PickSlotSchema(x=x, y=y)
    game.pick_slot(pick)
    assert game.status == GameStatusEnum.won


def test_cannot_pick_slot_in_game_lost(game):
    """Test to forbid a slot pick when game is lost"""
    x, y = 5, 6
    pick = PickSlotSchema(x=x, y=y)
    game.pick_slot(pick)

    x, y = 2, 3
    pick = PickSlotSchema(x=x, y=y)
    with raises(GameIsOver):
        game.pick_slot(pick)


def test_cannot_pick_slot_in_game_won(game):
    """Test to forbid a slot pick when game is won"""
    # Set all slots as picked
    for slot in game.board.iter_slots():
        slot.available = True if slot.mine else False

    # Set only one slot to be available
    x, y = 2, 3
    game.board.slots[x][y].available = True
    pick = PickSlotSchema(x=x, y=y)
    game.pick_slot(pick)

    x, y = 4, 4
    pick = PickSlotSchema(x=x, y=y)
    with raises(GameIsOver):
        game.pick_slot(pick)
