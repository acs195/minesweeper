"""This is the module for API schemas for games"""


from pydantic import BaseModel


class BoardSchema(BaseModel):
    """This is the list schema"""

    id: str


class BoardCreateSchema(BaseModel):
    """This is the create schema"""

    pass
