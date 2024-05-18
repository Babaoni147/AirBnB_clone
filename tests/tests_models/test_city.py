#!/usr/bin/python3
""" Unittest for City class """
import unittest
import json
import pep8
import os
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.state import State
from models.review import Review
from models.user import User
from models.engine.file_storage import FileStorage


class TestCity(unittest.TestCase):

    def setUp(self):
        """SetUp method"""
        self.city1 = City()
        self.city1.state_id = "ad45ad61as6d1"
        self.city1.name = "juan"

    def test_base_pep8(self):
        """Test for pep8"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['./models/city.py'])
        self.assertEqual(result.total_errors, 0)

    def test_docstring(self):
        """test docstring in the file"""
        self.assertIsNotNone(City.__doc__)

    def test_is_instance(self):
        """Test for instantiation"""
        self.assertIsInstance(self.city1, City)

    def test_attributes(self):
        """Test to check attributes"""
        self.city1.save()
        city1_json = self.city1.to_dict()
        my_new_city = City(**city1_json)
        self.assertEqual(my_new_city.id, self.city1.id)
        self.assertEqual(my_new_city.created_at, self.city1.created_at)
        self.assertEqual(my_new_city.updated_at, self.city1.updated_at)
        self.assertIsNot(self.city1, my_new_city)

    def test_subclass(self):
        """Test to check the inheritance"""
        self.assertTrue(issubclass(self.city1.__class__, BaseModel), True)

    def test_save(self):
        """Test to check save method"""
        variable_update = self.city1.updated_at
        self.city1.save()
        self.assertNotEqual(variable_update, self.city1.updated_at)

