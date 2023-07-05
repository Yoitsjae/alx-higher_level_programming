#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
from max_integer import max_integer


class TestMaxInteger(unittest.TestCase):
    """Test class for max_integer function
    """

    def test_regular_list(self):
        """Test max_integer with a regular list
        """
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_empty_list(self):
        """Test max_integer with an empty list
        """
        self.assertEqual(max_integer([]), None)

    def test_negative_numbers(self):
        """Test max_integer with a list of negative numbers
        """
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([-4, -3, -2, -1]), -1)

    def test_duplicate_numbers(self):
        """Test max_integer with a list containing duplicate numbers
        """
        self.assertEqual(max_integer([1, 2, 3, 3, 2, 1]), 3)
        self.assertEqual(max_integer([4, 4, 4, 4]), 4)

    def test_single_element_list(self):
        """Test max_integer with a list containing a single element
        """
        self.assertEqual(max_integer([100]), 100)

    def test_float_numbers(self):
        """Test max_integer with a list of float numbers
        """
        self.assertEqual(max_integer([1.5, 2.5, 3.5, 4.5]), 4.5)
        self.assertEqual(max_integer([4.5, 3.5, 2.5, 1.5]), 4.5)


if __name__ == '__main__':
    unittest.main()
