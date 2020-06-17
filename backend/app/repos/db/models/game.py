"""This is the DB models module for games"""

from uuid import uuid4

from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy_utils import ChoiceType

from domain.enums import GameStatusEnum
from repos.db.database import Base


class GameDB(Base):
    """This class represents the DB model for Games"""

    __tablename__ = "games"

    id = Column(String, primary_key=True)
    player_id = Column(String, ForeignKey("players.id"), nullable=False)
    board_id = Column(String, ForeignKey("boards.id"), nullable=False)
    status = Column(ChoiceType(GameStatusEnum, impl=Integer()))
    start_time = Column(DateTime, nullable=False)
    end_time = Column(DateTime, nullable=True)

    def __init__(self, *args, **kwargs):
        if not self.id:
            self.id = str(uuid4())
        super().__init__(*args, **kwargs)
