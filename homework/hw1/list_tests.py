from my_list import count

example_list = [1,2,3,4,4,5,6,4,7,8,9,4]
def test_one(example_list):
    """
    @param example_list - list
        - the list to search
    @return bool
    """
    test_output = count(example_list, 4)
    if test_output == 3:
        return True
    return False
print(f"Result of test_one: {test_one(example_list)}")


from my_list import extend

extend_list = [1,2,3,4,5]
another_extend_list = [6,7,8,9,10]
def test_two(extend_list, another_extend_list):
    """
    @param extend_list - list
        - the list to search
    @param another_extend_list - list
        - the list to search
    @return - list
    """
    test_output = extend(extend_list, another_extend_list)
    return test_output
print(f"Result of test_two: {test_two(extend_list, another_extend_list)}")


from my_list import remove

example_remove_list = [1,2,3,4,4,5,6,4,7,8,9,4]
def test_three(example_remove_list):
    """
    @param example_remove_list - list
        - the list to search
    @return list
    """
    test_output = remove(example_remove_list, 4)
    return test_output
print(f"Result of test_three: {test_three(example_remove_list)}")


from my_list import index

example_index_list = [1,2,3,4,5,6]
def test_four(example_index_list):
    """
    @param example_index_list - list
        - the list to search
    @return bool
    """
    test_output = index(example_index_list, 4)
    if test_output == 3:
        return True
    return False
print(f"Result of test_four: {test_four(example_index_list)}")