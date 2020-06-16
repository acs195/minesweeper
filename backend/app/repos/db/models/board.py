"""This is the DB models module for boards"""

from uuid import uuid4

from sqlalchemy import Column, Integer, String, TypeDecorator
from sqlalchemy.orm import relationship
from sqlalchemy.types import JSON

from domain.board import Slot
from repos.db.database import Base
from repos.db.models.game import GameDB


class JSONSlots(TypeDecorator):
    impl = JSON

    def process_result_value(self, slots_from, dialect):
        """Conver the 2D list of Slots to a 2D list of dicts"""
        slots_to = []
        for row in slots_from:
            rows = []
            for slot in row:
                if isinstance(slot, dict):
                    slot_converted = Slot(**slot)
                else:
                    slot_converted = slot
                rows.append(slot_converted)
            slots_to.append(rows)
        return slots_to

    def process_bind_param(self, slots_from, dialect):
        """Conver the 2D list of dicts to a 2D list of Slots"""
        slots_to = []
        for row in slots_from:
            rows = []
            for slot in row:
                if isinstance(slot, Slot):
                    slot_converted = dict(slot)
                else:
                    slot_converted = slot
                rows.append(slot_converted)
            slots_to.append(rows)
        return slots_to


class BoardDB(Base):
    """This class represents the DB model for Boards"""

    __tablename__ = "boards"

    id = Column(String, primary_key=True)
    rows = Column(Integer, nullable=False)
    cols = Column(Integer, nullable=False)
    mines = Column(Integer, nullable=False, default=0)
    slots = Column(JSONSlots, nullable=False, default=[[]])

    game = relationship(GameDB, backref="board", uselist=False)

    def __init__(self, *args, **kwargs):
        if not self.id:
            self.id = str(uuid4())
        super().__init__(*args, **kwargs)
