"""This is the DB module"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from core.config import get_settings
from typing import Dict

settings = get_settings()

db_args: Dict = dict()
db_args.update(connect_args={"check_same_thread": False})

engine = create_engine(settings.SQLALCHEMY_DATABASE_URI, **db_args)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db() -> sessionmaker:
    """Get a DB session"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
