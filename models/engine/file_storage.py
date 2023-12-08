#!/usr/bin/python3
"""A module of file storage class
"""
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """The storage engine class.

    Attributes:
        __file_path (str): The file's name that's the objects are saved to.
        __objects (dict): A dictionary of objects to be saved.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """A method that returns the dictionary __objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """A method that sets in __objects the obj with key <obj class name>.id
        """
        ocname = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(ocname, obj.id)] = obj

    def save(self):
        """A method that serializes __objects to the JSON file (path: __file_path)
        """
        dict = {}
        for key, value in FileStorage.__objects.items():
            dict[key] = value.to_dict()

        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            json.dump(dict, f)

    def reload(self):
        """A method that deserializes the JSON file to __objects
        """
        dict = {'BaseModel': BaseModel, 'User': User, 'State': State,
                'Place': Place, 'City': City,
                'Amenity': Amenity,'Review': Review}

        if os.path.exists(FileStorage.__file_path) is True:
            with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
                for key, value in json.load(f).items():
                    self.new(dict[value['__class__']](**value))
