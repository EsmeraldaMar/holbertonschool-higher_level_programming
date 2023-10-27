#!/usr/bin/python3
""" Module for test Rectangle class """
import unittest
import os
import sys
from io import StringIO
from unittest.mock import patch
from models.rectangle import Rectangle
from models.base import Base


class TestRectangleMethods(unittest.TestCase):
    """ Test methods for rectangle """

    def setUp(self):
        """ Runs for each test"""
        Base._Base__nb_objects = 0

    def tearDown(self):
        """ Cleans up after each test """
        pass

    def test_is_Base_instance(self):
        """ Test Rectangle is a Base instance """
        new = Rectangle(1, 1)
        self.assertEqual(True, isinstance(new, Base))

    def test_rectangle_expect(self):
        """Test - width/height/x/y/id is an int"""
        r = Rectangle(5, 10)
        self.assertEqual(r.width, 5)
        self.assertEqual(r.height, 10)
        r2 = Rectangle(1, 2, 3)
        self.assertEqual(r2.width, 1)
        self.assertEqual(r2.height, 2)
        self.assertEqual(r2.x, 3)
        r3 = Rectangle(1, 2, 3, 4)
        self.assertEqual(r3.width, 1)
        self.assertEqual(r3.height, 2)
        self.assertEqual(r3.x, 3)
        self.assertEqual(r3.y, 4)
        r4 = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(r4.width, 1)
        self.assertEqual(r4.height, 2)
        self.assertEqual(r4.x, 3)
        self.assertEqual(r4.y, 4)
        self.assertEqual(r4.id, 5)

    def test_new_rectangles(self):
        """ Test new rectangles """
        new = Rectangle(1, 1)
        new2 = Rectangle(1, 1)
        self.assertEqual(False, new is new2)
        self.assertEqual(False, new.id == new2.id)

    def test_incorrect_attrs(self):
        """ Test error raise with 1 arg passed """
        with self.assertRaises(TypeError):
            new = Rectangle(1)

    def test_incorrect_attrs_1(self):
        """ Test error raised with no args passed """
        with self.assertRaises(TypeError):
            new = Rectangle()

    def test_str_representation(self):
        """ Test for correct string representation"""
        rectangle = Rectangle(5, 1, 2, 3)
        res = "[Rectangle] (1) 2/3 - 5/1"
        self.assertEqual(str(rectangle), res)

    def test_check_value(self):
        """ Test args passed """
        with self.assertRaises(ValueError):
            r1 = Rectangle(-1, 2)

    def test_check_value_2(self):
        """ Test args passed """
        with self.assertRaises(ValueError):
            r1 = Rectangle(1, -2)

    def test_access_private_attrs(self):
        """ Trying to access to a private attribute """
        new = Rectangle(1, 1)
        with self.assertRaises(AttributeError):
            new.__width

    def test_access_private_attrs_2(self):
        """ Trying to access to a private attribute """
        new = Rectangle(1, 1)
        with self.assertRaises(AttributeError):
            new.__height

    def test_access_private_attrs_3(self):
        """ Trying to access to a private attribute """
        new = Rectangle(1, 1)
        with self.assertRaises(AttributeError):
            new.__x

    def test_access_private_attrs_4(self):
        """ Trying to access to a private attribute """
        new = Rectangle(1, 1)
        with self.assertRaises(AttributeError):
            new.__y

    def test_valid_attrs(self):
        """ Trying to pass a string value """
        with self.assertRaises(TypeError):
            new = Rectangle("5", 5, 5, 5, 5)

    def test_valid_attrs_2(self):
        """ Trying to pass a string value """
        with self.assertRaises(TypeError):
            new = Rectangle(5, "5", 5, 5, 5)

    def test_valid_attrs_3(self):
        """ Trying to pass a string value """
        with self.assertRaises(TypeError):
            new = Rectangle(5, 5, "5", 5, 5)

    def test_valid_attrs_4(self):
        """ Trying to pass a string value """
        with self.assertRaises(TypeError):
            new = Rectangle(5, 5, 5, "5", 5)

    def test_rectangle_string(self):
        """Test - an arg is a string"""
        with self.assertRaises(TypeError):
            r = Rectangle("1", 2)
        with self.assertRaises(TypeError):
            r = Rectangle(1, "2")
        with self.assertRaises(TypeError):
            r = Rectangle(1, 2, "3")
        with self.assertRaises(TypeError):
            r = Rectangle(1, 2, 3, "4")

    def test_rectangle_neg(self):
        """Test - an arg is neg"""
        with self.assertRaises(ValueError):
            r = Rectangle(-1, 2)
        with self.assertRaises(ValueError):
            r = Rectangle(1, -2)
        with self.assertRaises(ValueError):
            r = Rectangle(1, 2, -3)
        with self.assertRaises(ValueError):
            r = Rectangle(1, 2, 3, -4)

    def test_rectangle_zero(self):
        """Test - an arg is zero"""
        with self.assertRaises(ValueError):
            r = Rectangle(1, 0)
        with self.assertRaises(ValueError):
            r = Rectangle(0, 2)

    def test_value_attrs(self):
        """ Trying to pass invalid values """
        with self.assertRaises(ValueError):
            new = Rectangle(0, 2)

    def test_value_attrs_1(self):
        """ Trying to pass invalid values """
        with self.assertRaises(ValueError):
            new = Rectangle(2, 0)

    def test_value_attrs_2(self):
        """ Trying to pass invalid values """
        with self.assertRaises(ValueError):
            new = Rectangle(1, 1, -1)

    def test_value_attrs_3(self):
        """ Trying to pass invalid values """
        with self.assertRaises(ValueError):
            new = Rectangle(1, 1, 1, -1)

    def test_create_1(self):
        """ Test Create method"""
        dictionary = {'id': 50}
        s1 = Rectangle.create(**dictionary)
        self.assertEqual(s1.id, 50)

    def test_create_2(self):
        """ Test Create method """
        dictionary = {'id': 50, 'width': 1}
        s1 = Rectangle.create(**dictionary)
        self.assertEqual(s1.id, 50)
        self.assertEqual(s1.width, 1)

    def test_create_3(self):
        """ Test create method """
        dictionary = {'id': 50, 'width': 1, 'x': 2}
        s1 = Rectangle.create(**dictionary)
        self.assertEqual(s1.id, 50)
        self.assertEqual(s1.width, 1)
        self.assertEqual(s1.x, 2)

    def test_create_4(self):
        """ Test create method """
        dictionary = {'id': 50, 'width': 1, 'height': 2, 'x': 2, 'y': 3}
        s1 = Rectangle.create(**dictionary)
        self.assertEqual(s1.id, 50)
        self.assertEqual(s1.width, 1)
        self.assertEqual(s1.x, 2)
        self.assertEqual(s1.y, 3)
        self.assertEqual(s1.height, 2)

    def test_new_rect(self):
        """ Test new squares """
        new = Rectangle(1, 1)
        new2 = Rectangle(1, 1)
        self.assertEqual(False, new is new2)
        self.assertEqual(False, new.id == new2.id)

    def set_width(self):
        """ Test in setting width"""
        new = Rectangle(2)
        self.assertEqual(new.width, 2)
        new.width = 3
        self.assertEqual(new.width, 3)

    def set_height(self):
        """ Test in setting height"""
        new = Rectangle(2)
        self.assertEqual(new.height, 2)
        new.height = 3
        self.assertEqual(new.height, 3)

    def test_update_kwargs(self):
        rectangle = Rectangle(4, 4)
        rectangle.update(id=2, width=4, height=4)
        self.assertEqual(rectangle.id, 2)
        self.assertEqual(rectangle.width, 4)
        self.assertEqual(rectangle.height, 4)

    def test_display_no_args(self):
        """ Test display method with no arguments """
        r = Rectangle(6, 3)
        with self.assertRaises(TypeError) as e:
            Rectangle.display()
        s = "display() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), s)

    def test_basic_display(self):
        """ Test display without x and y """
        s1 = Rectangle(2, 6)
        result = "##\n##\n##\n##\n##\n##\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            s1.display()
            self.assertEqual(str_out.getvalue(), result)

    def test_str_out(self):
        s = Rectangle(4, 5, 9, 7)
        result = "[Rectangle] (1) 9/7 - 4/5\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(s)
            self.assertEqual(str_out.getvalue(), result)

    def test_rectangle_display_missing(self):
        """Test - display as expected without x or y"""
        output = StringIO()
        sys.stdout = output
        r = Rectangle(1, 1)
        r.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(output.getvalue(), "#\n")

    def test_rectangle_display_x_y(self):
        """Test - display as expected with x and y"""
        output = StringIO()
        sys.stdout = output
        r = Rectangle(1, 1, 1, 1)
        r.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(output.getvalue(), "\n #\n")

    def test_rectangle_display_x(self):
        """Test - display as expected with x and no y"""
        output = StringIO()
        sys.stdout = output
        r = Rectangle(1, 1, 1)
        r.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(output.getvalue(), " #\n")

    def test_str_no_args(self):
        """ Tests __str__ method with no arguments """
        r = Rectangle(7, 9)
        with self.assertRaises(TypeError) as e:
            Rectangle.__str__()
        s = "__str__() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), s)

    def test_rectangle_update(self):
        """Test - update as expected"""
        r = Rectangle(1, 2, 3, 4, 5)
        r.update(89)
        self.assertEqual(r.id, 89)
        r2 = Rectangle(1, 2, 3, 4, 5)
        r2.update(89, 1)
        self.assertEqual(r2.id, 89, 1)
        r3 = Rectangle(1, 2, 3, 4, 5)
        r3.update(89, 1, 2)
        self.assertEqual(r3.id, 89, 1)
        r4 = Rectangle(1, 2, 3, 4, 5)
        r4.update(89, 1, 2, 3)
        self.assertEqual(r4.id, 89, 1)
        r5 = Rectangle(1, 2, 3, 4, 5)
        r5.update(**{'id': 89})
        self.assertEqual(r5.id, 89)
        r6 = Rectangle(1, 2, 3, 4, 5)
        r6.update(**{'id': 89, 'width': 1})
        self.assertEqual(r6.width, 1)

    def test_rectangle_create(self):
        """Test - creates new instance of rectangle"""
        r = Rectangle.create(**{'id': 89})
        self.assertEqual(r.id, 89)
        r2 = Rectangle.create(**{'id': 89, 'width': 1})
        self.assertEqual(r2.id, 89)
        r3 = Rectangle.create(**{'id': 89, 'width': 1, 'height': 2})
        self.assertEqual(r3.id, 89)
        r4 = Rectangle.create(**{'id': 89, 'width': 1, 'height': 2, 'x': 3})
        self.assertEqual(r4.id, 89)
        r5 = Rectangle.create(**{
            'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4
        })
        self.assertEqual(r5.id, 89)

    def test_load_from_file(self):
        """ Test load JSON file """
        load_file = Rectangle.load_from_file()
        self.assertEqual(load_file, load_file)

    def test_rectangle_area(self):
        """Test - area of the rectangle"""
        r = Rectangle(1, 2)
        expect = 2
        self.assertEqual(r.area(), expect)

    def test_area(self):
        """ Test area method """
        s1 = Rectangle(5, 5)
        self.assertEqual(s1.area(), 25)

    def test_area_2(self):
        """ Test area method after modifying size """
        r1 = Rectangle(4, 4)
        self.assertEqual(r1.area(), 16)
        r1.height = 9
        r1.width = 9
        self.assertEqual(r1.area(), 81)

    def test_area_3(self):
        """ Checking the return value of area method """
        new = Rectangle(2, 2)
        self.assertEqual(new.area(), 4)
        new.width = 5
        self.assertEqual(new.area(), 10)
        new.height = 5
        self.assertEqual(new.area(), 25)

    def test_area_4(self):
        """ Checking the return value of area method """
        new = Rectangle(3, 8)
        self.assertEqual(new.area(), 24)
        new2 = Rectangle(10, 10)
        self.assertEqual(new2.area(), 100)

    def test_dict_to_json(self):
        """ Test Dictionary to JSON string """
        r1 = Rectangle(2, 2)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        res = "[{}]\n".format(dictionary.__str__())

        with patch('sys.stdout', new=StringIO()) as str_out:
            print(json_dictionary)
            self.assertEqual(str_out.getvalue(), res.replace("'", "\""))

    def test_dictionary(self):
        """ Test dictionary output"""
        new = Rectangle(2, 6, 3, 5, 5)
        result = new.to_dictionary()
        self.assertEqual(result,
                         {'id': 5, 'width': 2, 'height': 6, 'x': 3, 'y': 5})

    def test_rectangle_save_to_file(self):
        """Test - saves rectangle to file"""
        Rectangle.save_to_file([Rectangle(1, 2)])
        with open("Rectangle.json", 'r', encoding="utf-8") as file:
            r = file.read()
        self.assertEqual(
            r, '[{"id": 1, "width": 1, "height": 2, "x": 0, "y": 0}]')
        os.remove("Rectangle.json")

    def test_rectangle_save_to_file_empty(self):
        """Test - saves empty rectangle to file"""
        Rectangle.save_to_file([])
        with open("Rectangle.json", 'r', encoding="utf-8") as file:
            r = file.read()
        self.assertEqual(r, '[]')
        os.remove("Rectangle.json")

    def test_rectangle_save_to_file_none(self):
        """Test - saves None rectangle to file"""
        Rectangle.save_to_file(None)
        with open("Rectangle.json", 'r', encoding="utf-8") as file:
            r = file.read()
        self.assertEqual(r, '[]')
        os.remove("Rectangle.json")

    def test_rectangle_to_dictionary(self):
        """Test - rectangle becomes dictionary"""
        r = Rectangle(1, 2, 3, 4, 5)
        r_dictionary = r.to_dictionary()
        self.assertEqual(r_dictionary,
                         {'id': 5, 'width': 1, 'height': 2, 'x': 3, 'y': 4})

    def test_rectangle_load_from_file(self):
        """Test - rectangle loads file"""
        r = Rectangle(1, 2, 3, 4, 5)
        input = [r]
        Rectangle.save_to_file(input)
        output = Rectangle.load_from_file()
        self.assertEqual(str(output[0]), '[Rectangle] (5) 3/4 - 1/2')
        os.remove("Rectangle.json")
if __name__ == '__main__':
    unittest.main()
