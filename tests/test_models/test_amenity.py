#!/usr/bin/python3
""" Unittest for Amenity class """

#!/usr/bin/python3
""" Unittest for Amenity class """

import unittest
import pycodestyle
from models.base_model import BaseModel
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):

    def setUp(self):
        """SetUp method"""
        self.amenity1 = Amenity()
        self.amenity1.name = "juan"

    def test_base_pep8(self):
        """Test for PEP8 compliance"""
        pep8style = pycodestyle.StyleGuide(quiet=True)
        result = pep8style.check_files(['./models/amenity.py'])
        self.assertEqual(result.total_errors, 0, "PEP8 errors found in ./models/amenity.py")

    def test_docstring(self):
        """Test that Amenity class has a docstring"""
        self.assertIsNotNone(Amenity.__doc__, "Amenity class needs a docstring")

    def test_is_instance(self):
        """Test instantiation"""
        self.assertIsInstance(self.amenity1, Amenity, "amenity1 is not an instance of Amenity")

    def test_attributes(self):
        """Test attributes"""
        self.amenity1.save()
        amenity1_json = self.amenity1.to_dict()
        my_new_amenity = Amenity(**amenity1_json)
        self.assertEqual(my_new_amenity.id, self.amenity1.id, "IDs do not match")
        self.assertEqual(my_new_amenity.created_at, self.amenity1.created_at, "created_at does not match")
        self.assertEqual(my_new_amenity.updated_at, self.amenity1.updated_at, "updated_at does not match")
        self.assertIsNot(self.amenity1, my_new_amenity, "my_new_amenity is the same object as amenity1")

    def test_subclass(self):
        """Test inheritance"""
        self.assertTrue(issubclass(Amenity, BaseModel), "Amenity is not a subclass of BaseModel")

    def test_save(self):
        """Test save method"""
        initial_updated_at = self.amenity1.updated_at
        self.amenity1.save()
        self.assertNotEqual(initial_updated_at, self.amenity1.updated_at, "updated_at was not updated on save")
