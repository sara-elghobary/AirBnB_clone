#!/usr/bin/python3
"""Unittest for base model module.

This unittest is a collection of possible test cases
on which this module should not be expected to fail,
and cases on which it is expected to fail.

"""

from datetime import datetime
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.state import State
from models.review import Review
import os
#import pep8
import unittest
import uuid


class TestBaseModel(unittest.TestCase):
    """this will test the base model class
    """

    def setUp(self):
        self.model = BaseModel()


    def tearDown(self):
        """teardown"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_init(self):
        """Test that the BaseModel instance is initialized correctly.
        """
        self.assertIsNotNone(self.model.id)
        self.assertIsInstance(self.model.id, str)
        self.assertIsInstance(self.model.id, str)
        self.assertIsInstance(self.model.created_at, datetime)
        self.assertIsInstance(self.model.updated_at, datetime)
        self.assertEqual(str(type(self.model)),
                         "<class 'models.base_model.BaseModel'>")

    def test_save(self):
        """Test that the save method updates the updated_at attribute."""
        old_updated_at = self.model.updated_at
        self.model.save()
        self.assertGreater(self.model.updated_at, old_updated_at)

    def test_to_dict(self):
        """Test that the to_dict method returns a dictionary representation."""
        model_dict = self.model.to_dict()
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertIsInstance(model_dict['created_at'], str)
        self.assertIsInstance(model_dict['updated_at'], str)

if __name__ == '__main__':
    unittest.main()
