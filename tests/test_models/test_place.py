#!/usr/bin/python3
"""A module of unitest testing Place class
"""
import unittest
from models.place import Place
import datetime


class TestPlace(unittest.TestCase):
    """Unitest testing of place class
    """
    my_place = Place()

    def test_class_exists(self):
        self.assertEqual(str(type(self.my_place)), "<class 'models.place.Place'>")

    def test_user_inheritance(self):
        self.assertIsInstance(self.my_place, Place)

    def testHasAttributes(self):
        self.assertTrue(hasattr(self.my_place, 'city_id'))
        self.assertTrue(hasattr(self.my_place, 'user_id'))
        self.assertTrue(hasattr(self.my_place, 'name'))
        self.assertTrue(hasattr(self.my_place, 'description'))
        self.assertTrue(hasattr(self.my_place, 'number_rooms'))
        self.assertTrue(hasattr(self.my_place, 'number_bathrooms'))
        self.assertTrue(hasattr(self.my_place, 'max_guest'))
        self.assertTrue(hasattr(self.my_place, 'price_by_night'))
        self.assertTrue(hasattr(self.my_place, 'latitude'))
        self.assertTrue(hasattr(self.my_place, 'longitude'))
        self.assertTrue(hasattr(self.my_place, 'amenity_ids'))
        self.assertTrue(hasattr(self.my_place, 'id'))
        self.assertTrue(hasattr(self.my_place, 'created_at'))
        self.assertTrue(hasattr(self.my_place, 'updated_at'))

    def test_types(self):
        self.assertIsInstance(self.my_place.city_id, str)
        self.assertIsInstance(self.my_place.user_id, str)
        self.assertIsInstance(self.my_place.name, str)
        self.assertIsInstance(self.my_place.description, str)
        self.assertIsInstance(self.my_place.number_rooms, int)
        self.assertIsInstance(self.my_place.number_bathrooms, int)
        self.assertIsInstance(self.my_place.max_guest, int)
        self.assertIsInstance(self.my_place.price_by_night, int)
        self.assertIsInstance(self.my_place.latitude, float)
        self.assertIsInstance(self.my_place.longitude, float)
        self.assertIsInstance(self.my_place.amenity_ids, list)
        self.assertIsInstance(self.my_place.id, str)
        self.assertIsInstance(self.my_place.created_at, datetime.datetime)
        self.assertIsInstance(self.my_place.updated_at, datetime.datetime)


if __name__ == '__main__':
    unittest.main()
