from domain.board import Board, Slot
from schemas.board import PickSlotSchema
from domain.game import GameFactory

from uuid import uuid4


def test_new_slot():
    """Test to create a new slot"""
    mine = False
    available = True
    slot = Slot(mine=mine, available=available, x=1, y=1)
    assert slot.mine == mine
    assert slot.available == available


def test_new_board():
    """Test to create a new board with slots initialized"""
    rows = cols = 8
    board = Board(id=str(uuid4()), rows=rows, cols=cols)
    for row in board.slots:
        for slot in row:
            assert slot.available is True
            assert slot.mine is False


def test_board_set_mines(fake_repo):
    """Test to set mines in a board"""
    rows = cols = mines = 8
    game_factory = GameFactory(fake_repo)
    board_payload = dict(rows=rows, cols=cols)
    initial_slots = game_factory._get_initial_slots(**board_payload)
    board = Board(id=str(uuid4()), slots=initial_slots, **board_payload)
    board.set_mines(mines)
    count_mines = 0
    for row in board.slots:
        for slot in row:
            if slot.mine:
                count_mines += 1
    assert count_mines == mines


def test_board_pick_slot_clear_adjacent(game):
    """Test to pick a slot in a board"""
    x, y = 4, 1
    pick = PickSlotSchema(x=x, y=y)
    picked_slot = game.board.slots[x][y]

    assert picked_slot.available is True
    game.pick_slot(pick)

    expected_result_after_clear = [
        [False, False, True, True, True, True, True, True],
        [False, False, True, True, True, True, True, True],
        [False, False, False, False, True, True, True, True],
        [False, False, False, False, True, True, True, True],
        [False, False, False, False, False, False, True, True],
        [False, False, False, False, False, False, True, True],
        [False, False, False, False, False, False, True, True],
        [False, False, True, True, True, True, True, True],
    ]
    for x, row in enumerate(game.board.slots):
        for y, slot in enumerate(row):
            assert slot.available is expected_result_after_clear[x][y]


def test_board_toggle_flag_slot(game):
    """Test to toggle a flag in the board"""
    x, y = 7, 7
    flag_slot = PickSlotSchema(x=x, y=y)
    assert game.board.slots[x][y].flag is False
    game.board.toggle_flag_slot(flag_slot)
    assert game.board.slots[x][y].flag is True
    game.board.toggle_flag_slot(flag_slot)
    assert game.board.slots[x][y].flag is False


def test_board_iter_slots(game):
    """Test to iterate over the slots as it was a 1D list"""
    count = 0
    for _ in game.board.iter_slots():
        count += 1

    assert game.board.rows * game.board.cols == count
