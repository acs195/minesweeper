"""This is the DB models module for players"""

from uuid import uuid4

from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from repos.db.database import Base
from repos.db.models.game import GameDB


class PlayerDB(Base):
    """This class represents the DB model for Players"""

    __tablename__ = "players"

    id = Column(String, primary_key=True)
    name = Column(String, nullable=True)

    games = relationship(GameDB, backref="player")

    def __init__(self, *args, **kwargs):
        if not self.id:
            self.id = str(uuid4())
        super().__init__(*args, **kwargs)
