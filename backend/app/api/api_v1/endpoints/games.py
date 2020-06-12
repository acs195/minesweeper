"""This is the api module for games"""

from fastapi import APIRouter, Depends

from repos.in_memory.game import GameRepo
from schemas.game import GameCreateSchema

router = APIRouter()


@router.post("/start")
def start_game(game: GameCreateSchema, repo: GameRepo = Depends()):
    """Start game"""
    return {"game": "started"}
