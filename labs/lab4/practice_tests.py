"""
test_parse_season.py
Mihaela
Created March 20, 2019. Updated October 15, 2019
"""

import unittest
from .practice_dictionaries import Practice


class TestParseSeasons(unittest.TestCase):
    """
    Tests for parse_seasons() method
    """
    def setUp(self):
        """
        Define attribute p to hold object of type Problems
        """
        self.p = Practice()

    def test_brief_descriptions(self):
        """
        Test case with short season descriptions
        """
        input1 = {
            'spring': 'warm',
            'summer': 'hot',
            'fall': 'justright',
            'winter': 'cold'
        }
        actual_result = self.p.parse_seasons(input1)
        expected_result = 'springwarmsummerhotfalljustrightwintercold'
        self.assertEqual(actual_result, expected_result)


if __name__ == '__main__':
    unittest.main()