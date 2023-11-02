"""
File: homework/h2/src/linear_efficiency.py
Initial contributor: Mihaela
Contributor:
Date:

Implementation requirement:
- Apply the accumulation pattern
- Do not modify the values of the parameters
- Do not return a parameter
- If the use of a built-in data type method eliminates the use of the
    accumulation pattern in the design of a function, do not use it.
    Instead, write a 2nd design for that function to illustrate the use of
    built-in data type method.
"""


def hide(sentence):
    """
    Creates a new string with characters in `sentence` such that:
        - all subsequence occurrences of a character in `sentence` are
        replaced  with '*' in the returned sentence.
    :param sentence: string
    :return: string with the first occurrences of each character in `sentence`
        replaced by '*'
    :return: empty string or 1-charcter string identical with `sentence` if
        `sentence` is empty string or 1-character string
    Example 1: hide('babble') returns 'ba**le'
    Example 2: hide('more is less') returns 'more is*l***'
    """

    data = ''
    seen_chars = []
    for char in sentence:

        if char in seen_chars:
            data += '*'
        else:

            seen_chars.append(char)
            data += char

    return data


    # data = ''
    # seen_chars = {}
    # for char in sentence:

    #     if char in seen_chars:
    #         data += '*'
    #     else:

    #         seen_chars[char] = 0
    #         data += char

    # return data

def reduce_adjacent(num_lst):
    """
    Creates a new list with integers in `num_lst` such that:
        - adjancent integers that are the same in `num_lst` are replaced
        with one integer in the returned list.
    :param num_lst: list of integers
    :return: list of integers with no repeats
    :return: list of integers identical with `num_lst` if `num_lst` has no
        repoeats
    Example: reduce_adjancent([1, 2, 2, 3]) returns [1, 2, 3]
    """
    result = []
    for num in num_lst:
        if num not in result:
            result.append(num)
    return result


def reverse(word):
    """
    Creates and returns a new string that has the characters in `word`
    but in reverse order
    :param word: string
    :return: string with characters from `word` in reverse order
    :return: empty string if `word` is empty
    Example: reverse('python') returns 'nohtyp'
    Implementation requirements: do not use list method reverse
    """