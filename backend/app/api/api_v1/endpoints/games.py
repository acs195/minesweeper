"""This is the api module for games"""

from fastapi import APIRouter, Depends

from domain.game import GameFactory
from domain.player import AnonymousPlayer
from repos.in_memory.game import GameRepo
from schemas.game import GameSchema

router = APIRouter()


@router.post("/start", response_model=GameSchema)
def start_game(repo: GameRepo = Depends()) -> GameSchema:
    """Start game"""
    player = AnonymousPlayer()
    game_factory = GameFactory(repo)
    new_game = game_factory.start(player)
    return new_game
