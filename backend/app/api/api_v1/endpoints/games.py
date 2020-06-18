"""This is the api module for games"""

from typing import Optional

from fastapi import APIRouter, Depends, HTTPException

from domain.game import GameFactory, PickSlot, ToggleFlagSlot
from domain.player import PlayerManager
from repos.db import AppRepo
from schemas.board import PickSlotSchema
from schemas.game import GameParamsSchema, GameSchema
from utils.exceptions import GameIsOver, PickOutOrBoard, SlotAlreadyPicked, InvalidGameParameters

router = APIRouter()


@router.post("/start", response_model=GameSchema)
def start_game(
    game_params: GameParamsSchema = None, repo: AppRepo = Depends()
) -> GameSchema:
    """Start game"""
    try:
        player_manager = PlayerManager(repo)
        player = player_manager.get_or_create()
        game_factory = GameFactory(repo, game_params)
        new_game = game_factory.start(player)
        return new_game
    except InvalidGameParameters as e:
        raise HTTPException(status_code=400, detail=e.args[0])


@router.post("/{game_id}/pick-slot", response_model=GameSchema)
def pick_slot(
    game_id: str, pick: PickSlotSchema, repo: AppRepo = Depends(),
) -> GameSchema:
    """Pick a slot"""
    try:
        pick_slot = PickSlot(repo, game_id, pick)
        game = pick_slot.execute()
        return game
    except (SlotAlreadyPicked, GameIsOver, PickOutOrBoard) as e:
        raise HTTPException(status_code=400, detail=e.args[0])


@router.post("/{game_id}/toggle-flag-slot", response_model=GameSchema)
def toggle_flag_slot(
    game_id: str, pick: PickSlotSchema, repo: AppRepo = Depends()
) -> GameSchema:
    """Flag a slot"""
    try:
        pick_toggle_flag_slotslot = ToggleFlagSlot(repo, game_id, pick)
        game = pick_toggle_flag_slotslot.execute()
        return game
    except (SlotAlreadyPicked, GameIsOver, PickOutOrBoard) as e:
        raise HTTPException(status_code=400, detail=e.args[0])
