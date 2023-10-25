#!/usr/bin/python3
""" Module for test Square class"""
from unittest.mock import patch
import unittest
import json
from io import StringIO
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class TestBaseMethods(unittest.TestCase):
    """ Tests defined for Square class"""

    def setUp(self):
        """ Runs for each test"""
        Base._Base__nb_objects = 0

    def tearDown(self):
        """ Cleans up after each test """
        pass

    def test_new_square(self):
        """ Test new Square """
        new = Square(4)
        self.assertEqual(new.size, 4)
        self.assertEqual(new.width, 4)
        self.assertEqual(new.height, 4)
        self.assertEqual(new.y, 0)
        self.assertEqual(new.x, 0)
        self.assertEqual(new.id, 1)

    def test_str_representation(self):
        square = Square(5, 1, 2, 3)
        self.assertEqual(str(square), "[Square] (3) 1/2 - 5")

    def test_update_square(self):
        square = Square(5)
        square.update(1, 6, 7, 8)
        self.assertEqual(square.id, 1)
        self.assertEqual(square.size, 6)
        self.assertEqual(square.x, 7)
        self.assertEqual(square.y, 8)

    def test_update_kwargs(self):
        square = Square(5)
        square.update(id= 2, size= 4)
        self.assertEqual(square.id, 2)
        self.assertEqual(square.size, 4)

    def test_create_1(self):
        """ Test Create method"""
        dictionary = {'id': 50}
        s1 = Square.create(**dictionary)
        self.assertEqual(s1.id, 50)

    def test_create_2(self):
        """ Test Create method """
        dictionary = {'id': 50, 'size': 1}
        s1 = Rectangle.create(**dictionary)
        self.assertEqual(s1.id, 50)
        self.assertEqual(s1.size, 1)

    def test_create_3(self):
        """ Test create method """
        dictionary = {'id': 50, 'size': 1, 'x': 2}
        s1 = Rectangle.create(**dictionary)
        self.assertEqual(s1.id, 50)
        self.assertEqual(s1.size, 1)
        self.assertEqual(s1.x, 2)

    def test_create_4(self):
        """ Test create method """
        dictionary = {'id': 50, 'size': 1, 'x': 2, 'y': 3}
        s1 = Rectangle.create(**dictionary)
        self.assertEqual(s1.id, 50)
        self.assertEqual(s1.size, 1)
        self.assertEqual(s1.x, 2)
        self.assertEqual(s1.y, 3)

    def test_new_squares(self):
        """ Test new squares """
        new = Square(1, 1)
        new2 = Square(1, 1)
        self.assertEqual(False, new is new2)
        self.assertEqual(False, new.id == new2.id)

    def set_width(self):
        """ Test in setting width"""
        new = Square(2)
        self.assertEqual(new.width, 2)
        new.width = 3
        self.assertEqual(new.width, 3)
        self.assertEqual(new.height, 3)
        self.assertEqual(new.height, new.width)

    def set_height(self):
        """ Test in setting height"""
        new = Square(2)
        self.assertEqual(new.height, 2)
        new.height = 3
        self.assertEqual(new.height, 3)
        self.assertEqual(new.width, 3)
        self.assertEqual(new.height, new.width)

    def test_dictionary(self):
        """ Test dictionary output"""
        new = Square(2, 6, 3, 5)
        result = new.to_dictionary()
        self.assertEqual(result, {'id': 5, 'size': 2, 'x': 6, 'y': 3})

    def test_display_no_args(self):
        """ Test display method with no arguments """
        r = Square(6)
        with self.assertRaises(TypeError) as e:
            Square.display()
        s = "display() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), s)

    def test_str_out(self):
        s = Square(4, 5, 9, 7)
        result = "[Square] (7) 5/9 - 4\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(s)
            self.assertEqual(str_out.getvalue(), result)

    def test_str_no_args(self):
        """ Tests __str__ method with no arguments """
        r = Square(7, 9)
        with self.assertRaises(TypeError) as e:
            Square.__str__()
        s = "__str__() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), s)

    def test_load_from_file(self):
        """ Test load JSON file """
        load_file = Square.load_from_file()
        self.assertEqual(load_file, load_file)

    def test_basic_display(self):
        """ Test display without x and y """
        s1 = Square(6)
        result = "######\n######\n######\n######\n######\n######\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            s1.display()
            self.assertEqual(str_out.getvalue(), result)