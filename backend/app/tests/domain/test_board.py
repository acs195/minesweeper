from domain.board import Board, Slot


def test_new_slot():
    mine = False
    available = True
    slot = Slot(mine=mine, available=available)
    assert slot.mine == mine
    assert slot.available == available


def test_new_board():
    rows = cols = 8
    board = Board(rows=rows, cols=cols)
    for row in board.slots:
        for slot in row:
            assert slot.available is True
            assert slot.mine is False


def test_board_set_mines():
    rows = cols = mines = 8
    board = Board(rows=rows, cols=cols)
    board.set_mines(mines)
    count_mines = 0
    for row in board.slots:
        for slot in row:
            if slot.mine:
                count_mines += 1
    assert count_mines == mines
