"""This is the module for API schemas for players"""

from pydantic import BaseModel


class PlayerSchema(BaseModel):
    """This is the list schema"""

    id: str
