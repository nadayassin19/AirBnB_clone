#!/usr/bin/python3
"""A module of testing unitest State class
"""
import unittest
from models.state import State
import datetime


class TestState(unittest.TestCase):
    """Unitest testing of state class
    """
    my_state = State()

    def test_class_exists(self):
        res = "<class 'models.state.State'>"
        self.assertEqual(str(type(self.my_state)), res)

    def test_user_inheritance(self):
        self.assertIsInstance(self.my_state, State)

    def testHasAttributes(self):
        self.assertTrue(hasattr(self.my_state, 'name'))
        self.assertTrue(hasattr(self.my_state, 'id'))
        self.assertTrue(hasattr(self.my_state, 'created_at'))
        self.assertTrue(hasattr(self.my_state, 'updated_at'))

    def test_types(self):
        self.assertIsInstance(self.my_state.name, str)
        self.assertIsInstance(self.my_state.id, str)
        self.assertIsInstance(self.my_state.created_at, datetime.datetime)
        self.assertIsInstance(self.my_state.updated_at, datetime.datetime)


if __name__ == '__main__':
    unittest.main()
