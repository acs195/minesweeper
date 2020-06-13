from domain.game import GameFactory
from domain.player import AnonymousPlayer
from domain.board import Board


def test_new_slot(fake_game_repo):
    player = AnonymousPlayer()
    game_factory = GameFactory(fake_game_repo)
    new_game = game_factory.start(player)
    assert new_game.player == player
    assert isinstance(new_game.board, Board)
