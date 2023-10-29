#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest

max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test suite for max_integer function"""

    def test_empty_list(self):
        """"Test with an empty list"""
        nums = []
        max_int = max_integer(nums)
        self.assertIs(max_int, None)

    def test_individual_list(self):
        """"Test with a list containing a single element"""
        nums = [1]
        max_int = max_integer(nums)
        self.assertEqual(max_int, 1)

    def test_one_int(self):
        """"Test with a single integer instead of a list"""
        nums = 1
        with self.assertRaises(TypeError):
            max_integer(nums)

    def test_float_overflow(self):
        """"Test with a list containing float('inf')"""
        nums = [-1, 1, float('inf')]
        max_int = max_integer(nums)
        self.assertEqual(max_int, float('inf'))

    def test_negative_float_overflow(self):
        """"Test with a list containing float('-inf')"""
        nums = [-1, 1, float('-inf')]
        max_int = max_integer(nums)
        self.assertEqual(max_int, 1)

    def test_duplicated_max(self):
        """Test with a list containing duplicate maximum values"""
        nums = [1, 2, 3, 4, 4]
        max_int = max_integer(nums)
        self.assertEqual(max_int, 4)

    def test_max_char(self):
        """"Test with a list of a characters"""
        chars = ['a', 'g', 'z']
        max_char = max_integer(chars)
        self.assertEqual(max_char, 'z')
