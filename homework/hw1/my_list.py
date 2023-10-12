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
    Find how many times `num` is in `num_list`.
    :param num_list: list of integers
    :param num: integer
    :return: integer, representing how many times `num` is in `num_list`
    """
    counter = 0
    for x in num_list:
        if x == num:
            counter += 1
    return counter


def extend(num_list, another_num_list):
    """
    Build and return a new list that has the items in `num_list` followed by
    the itmes in `another_num_list` preserving the order.
    :param num_list: list of integers
    :param another_num_list: list of integers
    :return: list of integers
    """
    new_list = num_list + another_num_list
    return new_list


def remove(num_list, num):
    """
    Build and return a new list that has the items in `num_list` in their
    original order, except for `num` item, which gets removed.
    :param num_list: list of integers
    :param num: integer
    :return: list of integers
    """
    new_list = []
    for item in num_list:
        if item != num:
            new_list.append(item)
    return new_list

def index(num_list, num):
    """
    Find index of `num` in `num_list`.
    :param num_list: list of integers
    :param num: integer
    :return: non-negative integer of the index of the first occurrent of
    `num`
    :return: None, if `num` not found
    """
    for i in range(len(num_list)):
        if num_list[i] == num:
            return i