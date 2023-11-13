"""
Write a Python function that takes a list of strings and sorts them based on 
the length of the strings, with the shortest strings coming first. 
For example, if the input is ["apple", "banana", "cherry", "date"], the 
function should return ["date", "apple", "cherry", "banana"].

- Use appropriate function docstrings. 
- Include the time complexity of your function in your docstring.
- No need for design documents, unit tests, etc. Just the function and a call
to the function.
"""

def sort_string_list(input_list):
    """
    Make a new list based on the length of each value in the input_list. The new list will be in order of shortest value to longest.
    :param imput_list: list of strings
    :return: list of strings
    time complexity: O(n * log(n))
    """
    return sorted(input_list, key=len)

input_strings = ["apple", "banana", "cherry", "date"]
result = sort_string_list(input_strings)
print(result)


