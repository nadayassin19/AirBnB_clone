#!/usr/bin/pyrthon3
"""A module of class city
"""
from models.base_model import BaseModel
from models.state import State


class City(BaseModel):
    """a class city that enhirts from BaseModel

    Args:
        BaseModel (class): the super class that class city inherits from.

    Attributes:
        state_id (str): the state id
        name (str): the city name
    """

    state_id = ""
    name = ""
