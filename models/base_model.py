#!/usr/bin/python3
"""it's the base model module
"""
from datetime import datetime
from uuid import uuid
import models


class BaseModel:
    """it's a class BaseModel that's the super class for all
    the classes in this project.
    it defines all common attributes/methods for other classes
    """
    def __init__(self, *args, **kwargs):
        """initialize a new id
        """
        form = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid.uuid4())
        """uuid.uuid4: is a function used to generate a unique id of the
        new instance.
        """
        self.created_at = datetime.now()
        self.updated_at = self.created_at

        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(value, form)
                else:
                    self.__dict__[key] = value
        else:
            models.storage.new(self)

    def __str__(self):
        """A method that returns the str representation of BaseModel instance
        """
        class_name = self.__class__.__name__
        return ("[{}] ({}) {}".format(class_name, self.id, self.__dict__))

    def save(self):
        """it's a function that updates the public instance
        attribute updated_at with the current datetime
        """
        self.updated_at = datetime.datetime.now()
        models.storage.save()

    def to_dict(self):
        """it's a function that returns a dictionary
        containing all keys/values of __dict__ of the instance
        """
        dict = self.__dict__.copy()
        dict["created_at"] = self.created_at.isoformat()
        dict["updated_at"] = self.updated_at.isoformat()
        dict["__class__"] = self.__class__.__name__
        return dict
