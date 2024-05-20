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
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class TestHBNBCommand(unittest.TestCase):
    """Unit tests for HBNBCommand class."""

    def setUp(self):
        """Setup method to create initial conditions."""
        self.cli = HBNBCommand()

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_EOF(self, mock_stdout):
        """Test EOF command."""
        self.assertTrue(self.cli.onecmd("EOF"))

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_quit(self, mock_stdout):
        """Test quit command."""
        self.assertTrue(self.cli.onecmd("quit"))

    @patch('sys.stdout', new_callable=StringIO)
    def test_emptyline(self, mock_stdout):
        """Test empty line input."""
        self.cli.onecmd("")
        self.assertEqual(mock_stdout.getvalue(), "")

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_create_missing_class(self, mock_stdout):
        """Test create command with missing class name."""
        self.cli.onecmd("create")
        self.assertEqual(
            mock_stdout.getvalue().strip(), "** class name missing **"
        )

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_create_invalid_class(self, mock_stdout):
        """Test create command with invalid class name."""
        self.cli.onecmd("create InvalidClass")
        self.assertEqual(
            mock_stdout.getvalue().strip(), "** class doesn't exist **"
        )

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_create_valid_class(self, mock_stdout):
        """Test create command with valid class name."""
        with patch('models.storage.new') as mock_new:
            self.cli.onecmd("create BaseModel")
            self.assertTrue(mock_new.called)
            self.assertTrue(mock_stdout.getvalue().strip())

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_show_missing_class(self, mock_stdout):
        """Test show command with missing class name."""
        self.cli.onecmd("show")
        self.assertEqual(
            mock_stdout.getvalue().strip(), "** class name missing **"
        )

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_show_invalid_class(self, mock_stdout):
        """Test show command with invalid class name."""
        self.cli.onecmd("show InvalidClass")
        self.assertEqual(
            mock_stdout.getvalue().strip(), "** class doesn't exist **"
        )

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_show_missing_id(self, mock_stdout):
        """Test show command with missing id."""
        self.cli.onecmd("show BaseModel")
        self.assertEqual(
            mock_stdout.getvalue().strip(), "** instance id missing **"
        )

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_show_no_instance_found(self, mock_stdout):
        """Test show command with no instance found."""
        self.cli.onecmd("show BaseModel 1234")
        self.assertEqual(
            mock_stdout.getvalue().strip(), "** no instance found **"
        )

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_show_valid_instance(self, mock_stdout):
        """Test show command with valid instance."""
        obj = BaseModel()
        storage.new(obj)
        storage.save()
        self.cli.onecmd(f"show BaseModel {obj.id}")
        self.assertIn(obj.id, mock_stdout.getvalue().strip())

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_destroy_missing_class(self, mock_stdout):
        """Test destroy command with missing class name."""
        self.cli.onecmd("destroy")
        self.assertEqual(
            mock_stdout.getvalue().strip(), "** class name missing **"
        )

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_destroy_invalid_class(self, mock_stdout):
        """Test destroy command with invalid class name."""
        self.cli.onecmd("destroy InvalidClass")
        self.assertEqual(
            mock_stdout.getvalue().strip(), "** class doesn't exist **"
        )

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_destroy_missing_id(self, mock_stdout):
        """Test destroy command with missing id."""
        self.cli.onecmd("destroy BaseModel")
        self.assertEqual(
            mock_stdout.getvalue().strip(), "** instance id missing **"
        )

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_destroy_no_instance_found(self, mock_stdout):
        """Test destroy command with no instance found."""
        self.cli.onecmd("destroy BaseModel 1234")
        self.assertEqual(
            mock_stdout.getvalue().strip(), "** no instance found **"
        )

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_destroy_valid_instance(self, mock_stdout):
        """Test destroy command with valid instance."""
        obj = BaseModel()
        storage.new(obj)
        storage.save()
        self.cli.onecmd(f"destroy BaseModel {obj.id}")
        self.assertEqual(mock_stdout.getvalue().strip(), "")
        self.assertNotIn(f"BaseModel.{obj.id}", storage.all())

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_all_invalid_class(self, mock_stdout):
        """Test all command with invalid class name."""
        self.cli.onecmd("all InvalidClass")
        self.assertEqual(
            mock_stdout.getvalue().strip(), "** class doesn't exist **"
        )

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_all_valid_class(self, mock_stdout):
        """Test all command with valid class name."""
        obj = BaseModel()
        storage.new(obj)
        storage.save()
        self.cli.onecmd("all BaseModel")
        self.assertIn(str(obj), mock_stdout.getvalue().strip())

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_all_all_instances(self, mock_stdout):
        """Test all command with all instances."""
        obj1 = BaseModel()
        obj2 = User()
        storage.new(obj1)
        storage.new(obj2)
        storage.save()
        self.cli.onecmd("all")
        output = mock_stdout.getvalue().strip()
        self.assertIn(str(obj1), output)
        self.assertIn(str(obj2), output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_update_missing_class(self, mock_stdout):
        """Test update command with missing class name."""
        self.cli.onecmd("update")
        self.assertEqual(
            mock_stdout.getvalue().strip(), "** class name missing **"
        )

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_update_invalid_class(self, mock_stdout):
        """Test update command with invalid class name."""
        self.cli.onecmd("update InvalidClass")
        self.assertEqual(
            mock_stdout.getvalue().strip(), "** class doesn't exist **"
        )

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_update_missing_id(self, mock_stdout):
        """Test update command with missing id."""
        self.cli.onecmd("update BaseModel")
        self.assertEqual(
            mock_stdout.getvalue().strip(), "** instance id missing **"
        )

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_update_no_instance_found(self, mock_stdout):
        """Test update command with no instance found."""
        self.cli.onecmd("update BaseModel 1234")
        self.assertEqual(
            mock_stdout.getvalue().strip(), "** no instance found **"
        )

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_update_missing_attribute(self, mock_stdout):
        """Test update command with missing attribute name."""
        obj = BaseModel()
        storage.new(obj)
        storage.save()
        self.cli.onecmd(f"update BaseModel {obj.id}")
        self.assertEqual(
            mock_stdout.getvalue().strip(), "** attribute name missing **"
        )

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_update_missing_value(self, mock_stdout):
        """Test update command with missing value."""
        obj = BaseModel()
        storage.new(obj)
        storage.save()
        self.cli.onecmd(f"update BaseModel {obj.id} name")
        self.assertEqual(
            mock_stdout.getvalue().strip(), "** value missing **"
        )

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_update_valid_instance(self, mock_stdout):
        """Test update command with valid instance."""
        obj = BaseModel()
        storage.new(obj)
        storage.save()
        self.cli.onecmd(f'update BaseModel {obj.id} name "TestName"')
        self.assertEqual(mock_stdout.getvalue().strip(), "")
        self.assertEqual(
            getattr(storage.all()[f"BaseModel.{obj.id}"], "name"),
            "TestName"
        )

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_count(self, mock_stdout):
        """Test count command."""
        self.cli.onecmd("count BaseModel")
        self.assertEqual(mock_stdout.getvalue().strip(), "0")
        obj = BaseModel()
        storage.new(obj)
        storage.save()
        self.cli.onecmd("count BaseModel")
        self.assertEqual(mock_stdout.getvalue().strip(), "1")

    @patch('sys.stdout', new_callable=StringIO)
    def test_default_method(self, mock_stdout):
        """Test default method for unknown commands."""
        self.cli.onecmd("InvalidCommand")
        self.assertEqual(
            mock_stdout.getvalue().strip(),
            "*** Unknown syntax: InvalidCommand")


if __name__ == "__main__":
    unittest.main()
