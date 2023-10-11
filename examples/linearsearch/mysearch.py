"""
Name: Jon
date: today
linear search functions
"""

def linear_search(a_list, search_value):
    """
    @param a_list - a_list 
        the list to search
    @param search_value - many
        the value to search in a_list fore
    @return int
        if search_value is found, the index of search_value
        else -1
    """
    for idx, item in enumerate(a_list):
        if item == search_value:
            return idx
    return -1
