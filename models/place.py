#!/usr/bin/pyrthon3
"""A module of class place
"""
from models.base_model import BaseModel
from models.city import City
from models.user import User


class Place(BaseModel):
    """a class place that enhirts from BaseModel

    Args:
        BaseModel (class): the super class that class place inherits from.
    """

    def __init__(self, city_id="", user_id="", name="", description="",
                 number_rooms=0, number_bathrooms=0, max_guest=0,
                 price_by_night=0, latitude=0.0, longitude=0.0,
                 amenity_ids=[""]):
        """initialize new place

        Args:
            user_id (str, optional): user id. Defaults to "".
            name (str, optional): place's name. Defaults to "".
            city_id (str, optional): city id. Defaults to "".
            description (str, optional): place's description. Defaults to "".
            number_rooms (int, optional): place's no. of rooms. Defaults to 0.
            number_bathrooms (int, optional): place's no. of bathrooms. Defaults to 0.
            max_guest (int, optional): place's max guest no.. Defaults to 0.
            price_by_night (int, optional): place's price by night. Defaults to 0.
            latitude (float, optional): place's latitude. Defaults to 0.0.
            longitude (float, optional): place's longitude. Defaults to 0.0.
            amenity_ids (list, optional): amenity ids. Defaults to [""].
        """
        self.city_id = City.__init__.id
        self.user_id = BaseModel.__init__.id
        self.name = name
        self.description = description
        self.number_rooms = number_rooms
        self.number_bathrooms = number_bathrooms
        self.max_guest = max_guest
        self.price_by_night = price_by_night
        self.latitude = latitude
        self.longitude = longitude
        self.amenity_ids = amenity_ids
