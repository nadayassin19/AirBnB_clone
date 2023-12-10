#!/usr/bin/python3
"""A module of unitest testing Amenity class
"""
import unittest
from models.amenity import Amenity
import datetime


class TestAmenity(unittest.TestCase):
    """Unitest testing of class Amenity
    """
    my_amenity = Amenity()

    def test_class_exists(self):
        res = "<class 'models.amenity.Amenity'>"
        self.assertEqual(str(type(self.my_amenity)), res)

    def test_user_inheritance(self):
        self.assertIsInstance(self.my_amenity, Amenity)

    def testHasAttributes(self):
        self.assertTrue(hasattr(self.my_amenity, 'name'))
        self.assertTrue(hasattr(self.my_amenity, 'id'))
        self.assertTrue(hasattr(self.my_amenity, 'created_at'))
        self.assertTrue(hasattr(self.my_amenity, 'updated_at'))

    def test_types(self):
        self.assertIsInstance(self.my_amenity.name, str)
        self.assertIsInstance(self.my_amenity.id, str)
        self.assertIsInstance(self.my_amenity.created_at, datetime.datetime)
        self.assertIsInstance(self.my_amenity.updated_at, datetime.datetime)


if __name__ == '__main__':
    unittest.main()
