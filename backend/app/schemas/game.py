"""This is the module for API schemas for games"""


from pydantic import BaseModel


class GameSchema(BaseModel):
    """This is the list schema"""

    id: str


class GameCreateSchema(BaseModel):
    """This is the create schema"""

    pass
