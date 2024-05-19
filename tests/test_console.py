#!/usr/bin/python3
"""Defines unittests for console.py.
Unittest classes:
    TestHBNBCommand_prompting
    TestHBNBCommand_help
    TestHBNBCommand_exit
    TestHBNBCommand_create
    TestHBNBCommand_show
    TestHBNBCommand_all
    TestHBNBCommand_destroy
    TestHBNBCommand_update
"""

import unittest
from io import StringIO
from unittest.mock import patch
from console import HBNBCommand
from models import storage
from models.base_model import BaseModel
from models.user import User
import os

class TestHBNBCommand(unittest.TestCase):

    def setUp(self):
        """Set up test environment"""
        self.cli = HBNBCommand()

    def tearDown(self):
        """Clean up storage after each test"""
        storage._FileStorage__objects.clear()
        if os.path.exists("file.json"):
            os.remove("file.json")

    @patch('sys.stdout', new_callable=StringIO)
    def test_EOF(self, mock_stdout):
        """Test EOF command"""
        self.cli.onecmd("EOF")
        self.assertEqual(mock_stdout.getvalue(), "")

    @patch('sys.stdout', new_callable=StringIO)
    def test_quit(self, mock_stdout):
        """Test quit command"""
        self.cli.onecmd("quit")
        self.assertEqual(mock_stdout.getvalue(), "")

    @patch('sys.stdout', new_callable=StringIO)
    def test_emptyline(self, mock_stdout):
        """Test empty line input"""
        self.cli.onecmd("")
        self.assertEqual(mock_stdout.getvalue(), "")

    @patch('sys.stdout', new_callable=StringIO)
    def test_create_missing_class(self, mock_stdout):
        """Test create command with missing class name"""
        self.cli.onecmd("create")
        self.assertEqual(mock_stdout.getvalue().strip(), "** class name missing **")

    @patch('sys.stdout', new_callable=StringIO)
    def test_create_invalid_class(self, mock_stdout):
        """Test create command with invalid class name"""
        self.cli.onecmd("create MyModel")
        self.assertEqual(mock_stdout.getvalue().strip(), "** class doesn't exist **")

    @patch('sys.stdout', new_callable=StringIO)
    def test_create_valid_class(self, mock_stdout):
        """Test create command with valid class name"""
        self.cli.onecmd("create BaseModel")
        self.assertTrue(len(mock_stdout.getvalue().strip()) > 0)

    @patch('sys.stdout', new_callable=StringIO)
    def test_show_missing_class(self, mock_stdout):
        """Test show command with missing class name"""
        self.cli.onecmd("show")
        self.assertEqual(mock_stdout.getvalue().strip(), "** class name missing **")

    @patch('sys.stdout', new_callable=StringIO)
    def test_show_invalid_class(self, mock_stdout):
        """Test show command with invalid class name"""
        self.cli.onecmd("show MyModel")
        self.assertEqual(mock_stdout.getvalue().strip(), "** class doesn't exist **")

    @patch('sys.stdout', new_callable=StringIO)
    def test_show_missing_id(self, mock_stdout):
        """Test show command with missing instance id"""
        self.cli.onecmd("show BaseModel")
        self.assertEqual(mock_stdout.getvalue().strip(), "** instance id missing **")

    @patch('sys.stdout', new_callable=StringIO)
    def test_show_invalid_id(self, mock_stdout):
        """Test show command with invalid instance id"""
        self.cli.onecmd("show BaseModel 1234")
        self.assertEqual(mock_stdout.getvalue().strip(), "** no instance found **")

    @patch('sys.stdout', new_callable=StringIO)
    def test_show_valid_id(self, mock_stdout):
        """Test show command with valid class name and instance id"""
        obj = BaseModel()
        obj.save()
        self.cli.onecmd(f"show BaseModel {obj.id}")
        self.assertIn(obj.id, mock_stdout.getvalue().strip())

    @patch('sys.stdout', new_callable=StringIO)
    def test_destroy_missing_class(self, mock_stdout):
        """Test destroy command with missing class name"""
        self.cli.onecmd("destroy")
        self.assertEqual(mock_stdout.getvalue().strip(), "** class name missing **")

    @patch('sys.stdout', new_callable=StringIO)
    def test_destroy_invalid_class(self, mock_stdout):
        """Test destroy command with invalid class name"""
        self.cli.onecmd("destroy MyModel")
        self.assertEqual(mock_stdout.getvalue().strip(), "** class doesn't exist **")

    @patch('sys.stdout', new_callable=StringIO)
    def test_destroy_missing_id(self, mock_stdout):
        """Test destroy command with missing instance id"""
        self.cli.onecmd("destroy BaseModel")
        self.assertEqual(mock_stdout.getvalue().strip(), "** instance id missing **")

    @patch('sys.stdout', new_callable=StringIO)
    def test_destroy_invalid_id(self, mock_stdout):
        """Test destroy command with invalid instance id"""
        self.cli.onecmd("destroy BaseModel 1234")
        self.assertEqual(mock_stdout.getvalue().strip(), "** no instance found **")

    @patch('sys.stdout', new_callable=StringIO)
    def test_destroy_valid_id(self, mock_stdout):
        """Test destroy command with valid class name and instance id"""
        obj = BaseModel()
        obj.save()
        self.cli.onecmd(f"destroy BaseModel {obj.id}")
        self.assertEqual(mock_stdout.getvalue().strip(), "")
        self.assertNotIn(f"BaseModel.{obj.id}", storage.all())

    @patch('sys.stdout', new_callable=StringIO)
    def test_all_no_class(self, mock_stdout):
        """Test all command without a class name"""
        self.cli.onecmd("all")
        self.assertEqual(mock_stdout.getvalue().strip(), "[]")

    @patch('sys.stdout', new_callable=StringIO)
    def test_all_invalid_class(self, mock_stdout):
        """Test all command with invalid class name"""
        self.cli.onecmd("all MyModel")
        self.assertEqual(mock_stdout.getvalue().strip(), "** class doesn't exist **")

    @patch('sys.stdout', new_callable=StringIO)
    def test_all_valid_class(self, mock_stdout):
        """Test all command with valid class name"""
        obj = BaseModel()
        obj.save()
        self.cli.onecmd("all BaseModel")
        self.assertIn(obj.id, mock_stdout.getvalue().strip())

    @patch('sys.stdout', new_callable=StringIO)
    def test_update_missing_class(self, mock_stdout):
        """Test update command with missing class name"""
        self.cli.onecmd("update")
        self.assertEqual(mock_stdout.getvalue().strip(), "** class name missing **")

    @patch('sys.stdout', new_callable=StringIO)
    def test_update_invalid_class(self, mock_stdout):
        """Test update command with invalid class name"""
        self.cli.onecmd("update MyModel")
        self.assertEqual(mock_stdout.getvalue().strip(), "** class doesn't exist **")

    @patch('sys.stdout', new_callable=StringIO)
    def test_update_missing_id(self, mock_stdout):
        """Test update command with missing instance id"""
        self.cli.onecmd("update BaseModel")
        self.assertEqual(mock_stdout.getvalue().strip(), "** instance id missing **")

    @patch('sys.stdout', new_callable=StringIO)
    def test_update_invalid_id(self, mock_stdout):
        """Test update command with invalid instance id"""
        self.cli.onecmd("update BaseModel 1234")
        self.assertEqual(mock_stdout.getvalue().strip(), "** no instance found **")

    @patch('sys.stdout', new_callable=StringIO)
    def test_update_missing_attr_name(self, mock_stdout):
        """Test update command with missing attribute name"""
        obj = BaseModel()
        obj.save()
        self.cli.onecmd(f"update BaseModel {obj.id}")
        self.assertEqual(mock_stdout.getvalue().strip(), "** attribute name missing **")

    @patch('sys.stdout', new_callable=StringIO)
    def test_update_missing_value(self, mock_stdout):
        """Test update command with missing value"""
        obj = BaseModel()
        obj.save()
        self.cli.onecmd(f"update BaseModel {obj.id} name")
        self.assertEqual(mock_stdout.getvalue().strip(), "** value missing **")

    @patch('sys.stdout', new_callable=StringIO)
    def test_update_valid(self, mock_stdout):
        """Test update command with valid inputs"""
        obj = BaseModel()
        obj.save()
        self.cli.onecmd(f'update BaseModel {obj.id} name "My Model"')
        self.assertEqual(storage.all()[f"BaseModel.{obj.id}"].name, "My Model")

    @patch('sys.stdout', new_callable=StringIO)
    def test_update_dict(self, mock_stdout):
        """Test update command with a dictionary"""
        obj = BaseModel()
        obj.save()
        self.cli.onecmd(f'update BaseModel {obj.id} {{"name": "My Model", "age": 25}}')
        updated_obj = storage.all()[f"BaseModel.{obj.id}"]
        self.assertEqual(updated_obj.name, "My Model")
        self.assertEqual(updated_obj.age, 25)

    @patch('sys.stdout', new_callable=StringIO)
    def test_count(self, mock_stdout):
        """Test count command"""
        self.cli.onecmd("create BaseModel")
        self.cli.onecmd("create BaseModel")
        self.cli.onecmd("count BaseModel")
        self.assertEqual(mock_stdout.getvalue().strip(), "2")

if __name__ == "__main__":
    unittest.main()
