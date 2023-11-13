"""
Create a Python function that calculates the factorial of a given non-negative
 integer using recursion. The function should take an integer as input and 
 return its factorial. For example, factorial(5) should return 120.

- Use appropriate function docstrings. 
- Include the time complexity of your function in your docstring.
- No need for design documents, unit tests, etc. Just the function and a call
to the function.
"""

def factorial_recursive(num):
    """
    Take in an integer and return its factorial. 
    :param num_: integer
    :return: integer
    time complexity: O(n)
    """
    if num == 1:
        return num
    else:
        return num * factorial_recursive(num - 1)
    
result = factorial_recursive(5)
print (result)