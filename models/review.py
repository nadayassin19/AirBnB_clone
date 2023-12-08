#!/usr/bin/pyrthon3
"""A module of class review
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """a class review that enhirts from BaseModel

    Args:
        BaseModel (class): the super class that class review inherits from.

    Attributes:
        place_id (str): place id.
        user_id (str): user id.
        text (str): review's text.
    """

    place_id = ""
    user_id = ""
    text = ""
