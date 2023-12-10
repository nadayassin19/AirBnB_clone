#!/usr/bin/python3
"""A module of unitest testing Review class
"""
import unittest
from models.review import Review
import datetime


class TestReview(unittest.TestCase):
    """Unitest testing of review class
    """
    my_review = Review()

    def test_class_exists(self):
        res = "<class 'models.review.Review'>"
        self.assertEqual(str(type(self.my_review)), res)

    def test_user_inheritance(self):
        self.assertIsInstance(self.my_review, Review)

    def testHasAttributes(self):
        self.assertTrue(hasattr(self.my_review, 'place_id'))
        self.assertTrue(hasattr(self.my_review, 'user_id'))
        self.assertTrue(hasattr(self.my_review, 'text'))
        self.assertTrue(hasattr(self.my_review, 'id'))
        self.assertTrue(hasattr(self.my_review, 'created_at'))
        self.assertTrue(hasattr(self.my_review, 'updated_at'))

    def test_types(self):
        self.assertIsInstance(self.my_review.place_id, str)
        self.assertIsInstance(self.my_review.user_id, str)
        self.assertIsInstance(self.my_review.text, str)
        self.assertIsInstance(self.my_review.id, str)
        self.assertIsInstance(self.my_review.created_at, datetime.datetime)
        self.assertIsInstance(self.my_review.updated_at, datetime.datetime)


if __name__ == '__main__':
    unittest.main()
