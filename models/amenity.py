#!/usr/bin/pyrthon3
"""A module of class amenity
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """a class amenity that enhirts from BaseModel

    Args:
        BaseModel (class): the super class that class amenity inherits from.

    Attributes"
        name (str): the amenity name
    """

    name = ""
