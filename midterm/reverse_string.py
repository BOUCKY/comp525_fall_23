"""
Create a Python function that reverses a string using a Stack. For example, 
string_reverse("I really love data structures") should return 
"serutcurts atad evol yllaer I".

- Use appropriate function docstrings. 
- Include the time complexity of your function in your docstring.
- No need for design documents, unit tests, etc. Just the function and a call
to the function.
"""

def reverse_string(input_string):
    """
    Create a new string that is reverse order of the input string
    :param input_string: string
    :return: string
    time complexity: O(n)
    """
    input_list = []
    reversed_string = ""
    for char in input_string:
        input_list.append(char)
    while input_list:
        reversed_string += input_list.pop()

    return reversed_string


original_string = "I really love data structures"
result = reverse_string(original_string)
print(result)
