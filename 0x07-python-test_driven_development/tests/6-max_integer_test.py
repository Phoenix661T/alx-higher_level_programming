#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    '''Tests if the max_integer function works'''
    def test_result(self):
        '''Checks for results'''
        self.assertAlmostEqual(max_integer([]), None)
        self.assertAlmostEqual(max_integer([0, 0, 0]), 0)
        self.assertAlmostEqual(max_integer([-1, 0, 1, 1000]), 1000)
        self.assertAlmostEqual(max_integer([-100, -10, -1, 0]), 0)

    def test_types(self):
        '''Checks for wrong types'''
        self.assertRaises(TypeError, max_integer, 12)
        self.assertRaises(TypeError, max_integer, 1.2)
