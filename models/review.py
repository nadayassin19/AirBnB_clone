#!/usr/bin/pyrthon3
"""A module of class review
"""
from models.base_model import BaseModel
from models.place import Place
from models.user import User


class Review(BaseModel):
    """a class review that enhirts from BaseModel

    Args:
        BaseModel (class): the super class that class review inherits from.
    """

    def __init__(self, place_id="", user_id="", text=""):
        """initialize new review

        Args:
            place_id (str, optional): place id. Defaults to "".
            user_id (str, optional): user id. Defaults to "".
            text (str, optional): review's text. Defaults to "".
        """
        self.place_id = Place.__init__.id
        self.user_id = User.__init__.id
        self.text = text
