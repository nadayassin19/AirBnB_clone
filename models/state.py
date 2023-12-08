#!/usr/bin/pyrthon3
"""A module of class state
"""
from models.base_model import BaseModel


class State(BaseModel):
    """a state class that inherits from BaseModel class

    Args:
        BaseModel (class): the super class that class state inherits from.
    """

    def __init__(self, name=""):
        """initialize new state

        Args:
            name (str, optional): state name Defaults to "".
        """
        self.name = name
