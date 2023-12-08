#!/usr/bin/pyrthon3
"""A module of class city
"""
from models.base_model import BaseModel
from models.state import State


class City(BaseModel):
    """a class city that enhirts from BaseModel

    Args:
        BaseModel (class): the super class that class city inherits from.
    """

    def __init__(self, state_id="", name=""):
        """initialize new city

        Args:
            state_id (str, optional): state id. Defaults to "".
            name (str, optional): city's name. Defaults to "".
        """
        self.state_id = State.__init__.id
        self.name = name
        