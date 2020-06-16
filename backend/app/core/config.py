"""Thi is the config module"""

from enum import Enum
from functools import lru_cache
from os import getenv, path, getcwd

from pydantic import BaseSettings


class AppEnvironmentEnum(Enum):
    development = "development"
    testing = "testing"
    staging = "staging"
    production = "production"


class Settings(BaseSettings):
    """The app settings"""

    # Main
    PROJECT_NAME: str = "minesweeper"
    API_V1_STR: str = "/api/v1"
    APP_ENVIRONMENT: AppEnvironmentEnum = getattr(
        AppEnvironmentEnum, getenv("APP_ENVIRONMENT", "production")
    )
    HOST: str = getenv("HOST", "localhost")
    PORT: int = int(getenv("PORT", 5000))
    TESTING: bool = False

    # Logging
    LOG_LEVEL: str = getenv("LOG_LEVEL", "ERROR")

    # DB
    file_path = path.abspath(getcwd()) + "/minesweeper.db"
    SQLALCHEMY_DATABASE_URI: str = f"sqlite:///{file_path}"

    class Config:
        case_sensitive = True


@lru_cache()
def get_settings(**override: dict) -> Settings:
    return Settings(**override)
