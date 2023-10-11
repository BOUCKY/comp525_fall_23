"""
Name: Jon
date: today
tests for linear search functions
"""

from mysearch import linear_search

example_list = ["hello", 18, [5,6], 1.2]
def test_one(example_list):
    """
    @param example_list - list
        - the list to search
    @return bool
    """
    test_output = linear_search(example_list, 18)
    if test_output == 1:
        return True
    return False
print(f"Result of test_one: {test_one(example_list)}")

def test_two(example_list):
    """
    @param example_list - list
        - the list to search
    @return bool
    """
    test_output = linear_search(example_list, 1.2)
    if test_output == 3:
        return True
    return False
print(f"Result of test_two: {test_two(example_list)}")

def test_three(example_list):
    """
    @param example_list - list
        - the list to search
    @return bool
    """
    test_output = linear_search(example_list, "turtle")
    if test_output == -1:
        return True
    return False
print(f"Result of test_three: {test_three(example_list)}")
