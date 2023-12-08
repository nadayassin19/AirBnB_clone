#!/usr/bin/pyrthon3
"""A module of class user
"""
from models.base_model import BaseModel


class User(BaseModel):
    """a class user that inherits from class BaseModel

    Args:
        BaseModel (class): the super class that class user inherits from.
    """
    def __init__(self, email="", password="", first_name="", last_name=""):
        """initialize a new user

        Args:
            email (str, optional): user's email Defaults to "".
            password (str, optional): user's password Defaults to "".
            first_name (str, optional): user's first_name Defaults to "".
            last_name (str, optional): user's last_name Defaults to "".
        """
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
