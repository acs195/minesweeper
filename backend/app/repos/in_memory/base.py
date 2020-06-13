"""This module contains the base repository"""

datastore = dict()


class BaseRepo:
    """This is the Base Repository class"""

    def get(self, model, id):
        """Get an object by id"""
        resource = datastore.get(model).get(id)
        return resource

    def add(self, model, item):
        """Create and return an object of model"""
        resource = model(**item)
        new = {model: {resource.id: resource}}
        datastore.update(new)
        return resource

    def delete(self, model, id):
        """Delete an object by id"""
        del datastore[model][id]
