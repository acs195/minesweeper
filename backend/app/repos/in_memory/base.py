"""This module contains the base repository"""

datastore = dict()


class BaseRepo:
    """This is the Base Repository class"""

    def get(self, model, id: str):
        """Get an object by id"""
        resource = datastore.get(model).get(id)
        return resource

    def add(self, model, item):
        """Create and return an object of model"""
        new = {model: {item.id: item}}
        datastore.update(new)

    def delete(self, model, id: str):
        """Delete an object by id"""
        del datastore[model][id]
