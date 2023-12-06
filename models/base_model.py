#!/usr/bin/python3
"""it's the base model module
"""
from datetime import datetime
from uuid import uuid
import json

class BaseModel:
    """it's a class BaseModel that's the super class for all
    the classes in this project.
    it defines all common attributes/methods for other classes
    """
    def __init__(self, id, created_at, updated_at):
        """initialize a new id

        Args:
            id (string): id of the new instance created
            created_at (datetime): the current datetime when an instance is created
            updated_at (datetime): the current datetime when an instance is created,
            and it will be updated every time you change the object
        """
        self.id = str(uuid.uuid4())
        """uuid.uuid4: is a function used to generate a unique id of the
        new instance.
        """
        self.created_at = created_at
        self.updated_at = updated_at

    def __str__(self):
        print("[<class name>] (<self.id>) <self.__dict__>")

    def save(self):
        """it's a function that updates the public instance
        attribute updated_at with the current datetime
        """
        self.updated_at = datetime.datetime.now().isoformat("%Y-%m-%dT%H:%M:%S.%f")

    def to_dict(self):
        """it's a function that returns a dictionary
        containing all keys/values of __dict__ of the instance
        """
        