#!/usr/bin/python3
""" Module for test class base"""
import unittest
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
from io import StringIO
from unittest import TestCase
from unittest.mock import patch


class TestBaseMethods(unittest.TestCase):
    """ Defines test for Base class"""

    def setUp(self):
        """Runs for each test reset private attribute"""
        Base._Base__nb_objects = 0

    def tearDown(self):
        """ Cleans up JSON files created by tests """
        try:
            os.remove("Base.json")
        except (FileNotFoundError, PermissionError):
            pass

    def test_id(self):
        """Test - generated id"""
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)
        a = Base()
        x = a.id > 0
        self.assertEqual(x, True)
        b = Base()
        self.assertEqual(b.id, a.id + 1)

    def test_missing_args(self):
        """ Test for missing arguments"""
        base1 = Base()
        self.assertEqual(base1.id, 1)
        base1_c = base1.id > 0
        self.assertEqual(base1_c, True)
        base2 = Base()
        self.assertEqual(base1.id + 1, base2.id)
        base3 = Base(2)
        self.assertEqual(base3.id, 2)

    def test_id_input(self):
        """Test - id inputted as arg"""
        b3 = Base(12)
        self.assertEqual(b3.id, 12)

    def test_id_default(self):
        """ Test Default ID """
        new = Base()
        self.assertEqual(new.id, 1)

    def test_id_inc(self):
        """Checks id increments"""
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)

    def test_dif_id(self):
        """ Test different nb object attributes and assigned id"""
        new = Base()
        new2 = Base(1234)
        new3 = Base()
        self.assertEqual(new.id, 1)
        self.assertEqual(new2.id, 1234)
        self.assertEqual(new3.id, 2)

    def test_id_nb_objects(self):
        """ Test object attribute """
        new = Base()
        new2 = Base()
        new3 = Base()
        self.assertEqual(new.id, 1)
        self.assertEqual(new2.id, 2)
        self.assertEqual(new3.id, 3)

    def test_0_id(self):
        """ Test id to see if it duplicates """
        Base._Base__nb_objects = 0
        b1 = Base()
        b2 = Base()
        b3 = Base()
        b4 = Base(12)
        b5 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)
        self.assertEqual(b4.id, 12)
        self.assertEqual(b5.id, 4)

    def test_consecutive_ids(self):
        """ Tests consecutive ids """
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id + 1, b2.id)

    def test_string_id(self):
        """ Test string Id"""
        new = Base('2')
        self.assertEqual(new.id, '2')

    def test_mul_args(self):
        """ Test for multiple args to init method"""
        with self.assertRaises(TypeError):
            new = Base(1, 1)

    def test_class_const(self):
        """ Tests constructor signature """
        with self.assertRaises(TypeError) as e:
            Base.__init__()
        msg = "__init__() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), msg)

    def test_constructor_args_2(self):
        """ Tests constructor signature with 2 notself args """
        with self.assertRaises(TypeError) as e:
            Base.__init__(self, 1, 2)
        msg = "__init__() takes from 1 to 2 positional arguments but 3 \
were given"
        self.assertEqual(str(e.exception), msg)

    def test_attr_priv(self):
        """ Testing accessing private attributes"""
        new = Base()
        with self.assertRaises(AttributeError):
            new.__nb_objects

    def test_to_json_string(self):
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")
        self.assertIsInstance(Base.to_json_string([{'id': 1}]), str)

    def test_save_to_file_1(self):
        """ Test JSON file """
        Square.save_to_file(None)
        result = "[]\n"
        with open("Square.json", "r") as file:
            with patch('sys.stdout', new=StringIO()) as str_out:
                print(file.read())
                self.assertEqual(str_out.getvalue(), result)

        try:
            os.remove("Square.json")
        except (FileNotFoundError, PermissionError):
            pass

        Square.save_to_file([])
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), "[]")

    def test_save_to_file_2(self):
        """ Test JSON file """
        Rectangle.save_to_file(None)
        result = "[]\n"
        with open("Rectangle.json", "r") as file:
            with patch('sys.stdout', new=StringIO()) as str_out:
                print(file.read())
                self.assertEqual(str_out.getvalue(), result)
        try:
            os.remove("Rectangle.json")
        except (FileNotFoundError, PermissionError):
            pass

        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), "[]")

    def test_load_from_file_empty_file(self):
        """ Test use of load_from_file with empty file """
        try:
            os.remove("Rectangle.json")
        except Exception:
            pass
        open("Rectangle.json", 'a').close()
        self.assertEqual(Rectangle.load_from_file(), [])

    def test_create(self):
        """ Test create method """
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual(str(r1), str(r2))
        self.assertFalse(r1 is r2)
        self.assertFalse(r1 == r2)

    def test_base_to_json_string(self):
        """Test - to_json_string list_dictionaries is not empty"""
        json_dictionary = Base.to_json_string([{'id': 10}])
        self.assertEqual(json_dictionary, "[{\"id\": 10}]")

    def test_base_to_json_string_none(self):
        """Test - to_json_string list_dictionaries is None"""
        json_dictionary = Base.to_json_string(None)
        self.assertEqual(json_dictionary, "[]")

    def test_base_to_json_string_empty(self):
        """Test - to_json_string list_dictionaries is empty"""
        input = []
        self.assertEqual(Base.to_json_string(input), "[]")

    def test_base_to_json_string_type(self):
        """Test - to_json_string makes the correct type"""
        input = Base.to_json_string([{'id': 10}])
        self.assertEqual(type(input).__name__, "str")

    def test_from_json_string(self):
        """Test - from_json_string converts correctly"""
        input = "[{\"id\": 89}]"
        expected = [{"id": 89}]
        self.assertEqual(Base.from_json_string(input), expected)

    def test_from_json_string_none(self):
        """Test - from_json_string is None"""
        input = None
        expected = []
        self.assertEqual(Base.from_json_string(input), expected)

    def test_from_json_string_empty(self):
        """Test - from_json_string is empty"""
        input = "[]"
        self.assertEqual(Base.from_json_string(input), [])

    def test_from_json_string_type(self):
        """Test - from_json_string creates correct type"""
        input = Base.from_json_string("[{\"id\": 89}]")
        self.assertEqual(type(input).__name__, "list")

    if __name__ == '__main__':
        unittest.main()
