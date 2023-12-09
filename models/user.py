#!/usr/bin/pyrthon3
"""A module of class user
"""
from models.base_model import BaseModel


class User(BaseModel):
    """a class user that inherits from class BaseModel

    Args:
        BaseModel (class): the super class that class user inherits from.

    Attributes:
        email (str): user's email.
        password (str): user's password.
        first_name (str): user's first_name.
        last_name (str): user's last_name.
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
