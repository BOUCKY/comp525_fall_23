"""
Write a Python function that takes a list of integers as input and returns a 
new list with only the even numbers. For example, if the input is 
[1, 2, 3, 4, 5, 6], the function should return [2, 4, 6].

- Use appropriate function docstrings. 
- Include the time complexity of your function in your docstring.
- No need for design documents, unit tests, etc. Just the function and a call
to the function.
"""

def even_numbers(num_list):
    """
    Build and return a new list that has only the even numbers from the num_list
    :param num_list: list of integers
    :return: list of integers
    time complexity: O(n)
    """
    event_list = []
    for number in num_list:
        if number % 2 == 0:
            event_list.append(number)

    return(event_list)

result = even_numbers([1,2,3,4,5,6])
print(result)