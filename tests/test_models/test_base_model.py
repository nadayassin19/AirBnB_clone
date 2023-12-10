#!/usr/bin/python3
"""A module of unitest testing BaseModel class
"""
import unittest
from models.base_model import BaseModel
from datetime import datetime


class BaseModelTests(unittest.TestCase):
    """For console
    """
    my_model = BaseModel()

    def testBaseModel1(self):
        """ Test attributes value of a BaseModel instance """

        self.my_model.name = "Nada"
        self.my_model.my_number = 27
        self.my_model.save()
        my_model_json = self.my_model.to_dict()

        self.assertEqual(self.my_model.name, my_model_json['name'])
        self.assertEqual(self.my_model.my_number, my_model_json['my_number'])
        self.assertEqual('BaseModel', my_model_json['__class__'])
        self.assertEqual(self.my_model.id, my_model_json['id'])

    def testSave(self):
        """Checks if save method updates the public instance instance
        attribute updated_at
        """
        self.my_model.first_name = "Nada"
        self.my_model.save()

        self.assertIsInstance(self.my_model.id, str)
        self.assertIsInstance(self.my_model.created_at, datetime.datetime)
        self.assertIsInstance(self.my_model.updated_at, datetime.datetime)

        first_dict = self.my_model.to_dict()

        self.my_model.first_name = "Yassin"
        self.my_model.save()
        sec_dict = self.my_model.to_dict()

        self.assertEqual(first_dict['created_at'], sec_dict['created_at'])
        self.assertNotEqual(first_dict['updated_at'], sec_dict['updated_at'])


if __name__ == '__main__':
    unittest.main()
