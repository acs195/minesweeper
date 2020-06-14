"""This is the api module for games"""

from fastapi import APIRouter, Depends, HTTPException

from domain.game import GameFactory
from domain.player import AnonymousPlayer
from repos.in_memory.game import GameRepo
from schemas.board import PickSlotSchema
from schemas.game import GameSchema
from utils.exceptions import SlotAlreadyPicked, GameIsOver

router = APIRouter()


@router.post("/start", response_model=GameSchema)
def start_game(repo: GameRepo = Depends()) -> GameSchema:
    """Start game"""
    player = AnonymousPlayer()
    game_factory = GameFactory(repo)
    new_game = game_factory.start(player)
    return new_game


@router.post("/{game_id}/pick-slot", response_model=GameSchema)
def pick_slot(
    game_id: str, pick: PickSlotSchema, repo: GameRepo = Depends()
) -> GameSchema:
    """Pick a slot"""
    game = repo.get(id=game_id)
    try:
        game.pick_slot(pick)
        return game
    except (SlotAlreadyPicked, GameIsOver) as e:
        raise HTTPException(status_code=400, detail=e.args[0])


@router.post("/{game_id}/toggle-flag-slot", response_model=GameSchema)
def toggle_flag_slot(
    game_id: str, pick: PickSlotSchema, repo: GameRepo = Depends()
) -> GameSchema:
    """Flag a slot"""
    game = repo.get(id=game_id)
    try:
        game.toggle_flag_slot(pick)
        return game
    except (SlotAlreadyPicked, GameIsOver) as e:
        raise HTTPException(status_code=400, detail=e.args[0])
