#!/usr/bin/python3
"""A module of unitest testing City class
"""
import unittest
from models.city import City
import datetime


class TestCity(unittest.TestCase):
    """Unitest testing of city class
    """
    my_city = City()

    def test_class_exists(self):
        self.assertEqual(str(type(self.my_city)), "<class 'models.city.City'>")

    def test_user_inheritance(self):
        self.assertTrue(self.my_city, City)

    def testHasAttributes(self):
        self.assertTrue(hasattr(self.my_city, 'state_id'))
        self.assertTrue(hasattr(self.my_city, 'name'))
        self.assertTrue(hasattr(self.my_city, 'id'))
        self.assertTrue(hasattr(self.my_city, 'created_at'))
        self.assertTrue(hasattr(self.my_city, 'updated_at'))

    def test_types(self):
        self.assertIsInstance(self.my_city.state_id, str)
        self.assertIsInstance(self.my_city.name, str)
        self.assertIsInstance(self.my_city.id, str)
        self.assertIsInstance(self.my_city.created_at, datetime.datetime)
        self.assertIsInstance(self.my_city.updated_at, datetime.datetime)


if __name__ == '__main__':
    unittest.main()
