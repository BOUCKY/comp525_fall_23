# https://docs.python.org/3/library/unittest.html
import unittest
import my_list

class ExampleTests(unittest.TestCase):

    def test_count(self):
        sample_list = [4,5,6,1,2,3,2,4]
        # check how many times 4 exists, should be twice
        expected = 2
        actual_result = my_list.count(sample_list, 4)
        self.assertEqual(expected, actual_result)

    def test_index(self):
        sample_list = [4,5,6]
        # check how many times 4 exists, should be twice
        expected = 1
        actual_result = my_list.index(sample_list, 5)
        self.assertEqual(expected, actual_result)

if __name__ == "__main__":
    unittest.main()