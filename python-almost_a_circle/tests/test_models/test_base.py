#!/usr/bin/python3
""" Module for test class base"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
from io import StringIO
from unittest import TestCase
from unittest.mock import patch


class TestBaseMethods(unittest.TestCase):
    """ Defines test for Base class"""

    def setUp(self):
        """Runs for each test """
        Base._Base__nb_objects = 0

    def test_id(self):
        """ Test Assigned ID"""
        new = Base(1)
        self.assertEqual(new.id, 1)

    def test_id_default(self):
        """ Test Default ID """
        new = Base()
        self.assertEqual(new.id, 1)

    def tearDown(self):
        """ Cleans up after each test """
        pass

    def test_docstring_pre(self):
        """ Tests if Doc string is present"""
        self.assertIsNotNone(Base.__doc__)

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

    def test_attr_priv(self):
        """ Testing accessing private attributes"""
        new = Base()
        with self.assertRaises(AttributeError):
            new.__nb_objects

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
        except:
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
        except:
            pass

        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), "[]")
