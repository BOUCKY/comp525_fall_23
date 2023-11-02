"""
File: homework/h1/src/my_list.py
Initial contributor: Mihaela
Contributor:
Date:

Implementation requirement:
- Do not call built-in list methods, except for append()
"""


def count(num_list, num):
    """
    Find how many ti `num` is in `num_list`.
    :param num_list: list of integmesers
    :param num: integer
    :return: integer, representing how many times `num` is in `num_list`
    """
    counter = 0
    for i in num_list:
        if i == num:
            counter += 1
    return counter

def index(num_list, num):
    """
    Find index of `num` in `num_list`.
    :param num_list: list of integers
    :param num: integer
    :return: non-negative integer of the index of the first occurrent of
    `num`
    :return: None, if `num` not found
    """
    for idx, el in enumerate(num_list):
        if el == num:
            return idx
    return None