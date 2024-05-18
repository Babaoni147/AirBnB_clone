#!/usr/bin/python3
""" Unittest for Place class """
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


class TestPlace(unittest.TestCase):

    def setUp(self):
        """SetUp method"""
        self.place1 = Place()
        self.place1.city_id = "Toronto"
        self.place1.user_id = "3r45t9s323d9"
        self.place1.name = "juan"
        self.place1.description = "Warehouse"
        self.place1.number_rooms = 9
        self.place1.number_bathrooms = 5
        self.place1.max_guest = 36
        self.place1.price_by_night = 300
        self.place1.latitude = 43.6
        self.place1.longitude = 79.3
        self.place1.amenity_ids = ["d15s64sd", "4asdad"]

    def test_base_pep8(self):
        """Test for pep8"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['./models/place.py'])
        self.assertEqual(result.total_errors, 0)

    def test_docstring(self):
        """test docstring in the file"""
        self.assertIsNotNone(Place.__doc__)

    def test_is_instance(self):
        """Test for instantiation"""
        self.assertIsInstance(self.place1, Place)

    def test_attributes(self):
        """Test to check attributes"""
        self.place1.save()
        place1_json = self.place1.to_dict()
        my_new_place = Place(**place1_json)
        self.assertEqual(my_new_place.id, self.place1.id)
        self.assertEqual(my_new_place.created_at, self.place1.created_at)
        self.assertEqual(my_new_place.updated_at, self.place1.updated_at)
        self.assertIsNot(self.place1, my_new_place)

    def test_subclass(self):
        """Test to check the inheritance"""
        self.assertTrue(issubclass(self.place1.__class__, BaseModel), True)

    def test_save(self):
        """Test to check save method"""
        variable_update = self.place1.updated_at
        self.place1.save()
        self.assertNotEqual(variable_update, self.place1.updated_at)

