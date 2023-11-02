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

class HideTestCases(unittest.TestCase):

    def test_hide_1(self):
        '''
        Example 1: hide('babble') returns 'ba**le'
        '''
        sentence = 'babble'
        expected_reult = "ba**le"
        actual_result = linear_efficiency.hide(sentence)
        self.assertEqual(expected_reult, actual_result)


    def test_hide_2(self):
        '''
        Example 2: hide('more is less') returns 'more is*l***'
        '''
        sentence = 'more is less'
        expected_reult = "more is*l***"
        actual_result = linear_efficiency.hide(sentence)
        self.assertEqual(expected_reult, actual_result)


if __name__ == '__main__':
    unittest.main()