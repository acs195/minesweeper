"""This is the base module for repository"""

from typing import Optional, TypeVar, Union

from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel

from repos.db.database import Base

ModelType = TypeVar("ModelType", bound=Base)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


class BaseRepo:
    """This handles base repository operations"""

    def __init__(self, db) -> None:
        self.db = db

    def get(self, model: ModelType, id: str) -> Optional[ModelType]:
        """Get object by id from DB"""
        return self.db.query(model).filter(model.id == id).first()

    def add(self, model: ModelType, obj_in: Union[dict, CreateSchemaType]) -> ModelType:
        """Create an object into the DB"""
        db_obj = model(**obj_in)
        self.db.add(db_obj)
        self.db.commit()
        return db_obj

    def update(
        self, db_obj: ModelType, obj_in: Union[dict, UpdateSchemaType]
    ) -> ModelType:
        """Update an object into the DB"""
        obj_data = jsonable_encoder(db_obj)
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)

        for field in obj_data:
            if field in update_data and not isinstance(getattr(db_obj, field), Base):
                setattr(db_obj, field, update_data[field])

        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj
