#!/usr/bin/pyrthon3
"""A module of class place
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """a class place that enhirts from BaseModel

    Args:
        BaseModel (class): the super class that class place inherits from.

    Attributes:
        user_id (str): user id.
        name (str): place's name.
        city_id (str): city id.
        description (str): place's description.
        number_rooms (int): place's no. of rooms.
        number_bathrooms (int): place's no. of bathrooms.
        max_guest (int): place's max guest no..
        price_by_night (int): place's price by night.
        latitude (float): place's latitude.
        longitude (float): place's longitude.
        amenity_ids (list): amenity ids.
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
