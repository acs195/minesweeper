"""This module contains the base repository"""


class BaseRepo:
    """This is the Base Repository class"""

    @classmethod
    def create(cls, storage, model_class, values):
        """Create and return an object of model_class"""
        resource = model_class(**values)
        storage.add(resource)
        return resource
