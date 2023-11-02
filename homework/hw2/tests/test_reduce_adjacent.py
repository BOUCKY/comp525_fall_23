"""
File: homework/h2/tests/test_hide.py
Initial contributor: Mihaela
Contributor:
Date:
"""

import unittest
import sys
import os
sys.path.insert(0, os.path.abspath('..'))
from src import linear_efficiency

class ReduceTestCases(unittest.TestCase):

    def test_reduce_1(self):
        '''
        Example 1: reduce_adjacent([1, 2, 2, 3]) returns [1, 2, 3]
        '''
        list = [1, 2, 2, 3]
        expected_reult = [1, 2, 3]
        actual_result = linear_efficiency.reduce_adjacent(list)
        self.assertEqual(expected_reult, actual_result)


    def test_reduce_2(self):
        '''
        Example 2: reduce_adjacent([1, 2, 3, 4, 4]) returns [1, 2, 3, 4]
        '''
        list = [1, 2, 3, 4, 4]
        expected_reult = [1, 2, 3, 4]
        actual_result = linear_efficiency.reduce_adjacent(list)
        self.assertEqual(expected_reult, actual_result)


if __name__ == '__main__':
    unittest.main()