#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """ Testing max_integer"""
    def test_max_end(self):
        """ Test function on a normal list with max at the end """
        self.assertEqual(max_integer([1, 2, 3]), 3)
    
    def test_max_mid(self):
        """ Test function on a normal list with max at the middle """
        self.assertEqual(max_integer([1, 3, 2]), 3)

    def test_max_beg(self):
        """ Test function on a normal list with max at the beginning """
        self.assertEqual(max_integer([3, 1, 2]), 3)

    def test_string(self):
        """ Test function on a string """
        self.assertEqual(max_integer("Hamburger"), 'u')

    def test_normal(self):
        """ Test function on a tuple """
        self.assertEqual(max_integer((1, 2, 3)), 3)

    def test_empty_list(self):
        """ Test function on empty list """
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer(), None)

    def test_single_element(self):
        """ Test function on list with 1 element """
        self.assertEqual(max_integer([5]), 5)

    def test_negative_elements_mix(self):
        """ Test function on mixed integers"""
        self.assertEqual(max_integer([-12, 4, -3]), 4)

    def test_negative_elements(self):
        """ Test Function on negative integers in list"""
        self.assertEqual(max_integer([-2, -10, -23]), -2)

    def test_multiple_args(self):
         """ Test function by passing more than one argument """
         with self.assertRaises(TypeError):
             max_integer([3], [8])

    def test_mixed_elements(self):
        """ Test function on list with mixed type elements """
        with self.assertRaises(TypeError):
            max_integer([3, 5.1, "Haha"])
    
    def test_not_list(self):
        """ Test function on non iterable """
        with self.assertRaises(TypeError):
            max_integer(3)

if __name__ == '__main__':
    unittest.main()
