"""This module registers all the routes for api_v1"""

from fastapi import APIRouter

from api.api_v1.endpoints import games

api_router = APIRouter()

api_router.include_router(games.router, prefix="/games", tags=["games"])
