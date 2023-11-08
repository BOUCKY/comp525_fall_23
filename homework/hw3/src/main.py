"""
File: src/main.py
Author: Mihaela
Date: 3/21/2023
Developer:
Date:
"""

from unorderedlist import UnorderedList


def test_prepend():
    """
    Call prepend() to create the list with items 6, 3, 7
    """
    # Start by creating UnorderedList object, `ul_obj`
    ul_obj = UnorderedList()

    # Use `prepend()` three times with arguments 7, 3, 6
    ul_obj.prepend(7)
    ul_obj.prepend(3)
    ul_obj.prepend(6)

    print(f'\n{ul_obj.head.data}')
    print(f'{ul_obj.head.next.data}')
    print(f'{ul_obj.head.next.next.data}')


def test_size():
    """
    Use code in test_prepend() to create the list 6, 3, 7.
    Call size() to test the method.
    """
    ul_obj = UnorderedList()

    # Use `prepend()` three times with arguments 7, 3, 6
    ul_obj.prepend(7)
    ul_obj.prepend(3)
    ul_obj.prepend(6)
    size = ul_obj.size()
    print(size)

def test_search():
    """
    Use code in test_prepend() to create the list 6, 3, 7.
    Call search(7) and search(10) to test the full behavior of the method.
    """


def test_print():
    """
    Use code in test_prepend() to create the list 6, 3, 7.
    Call print() to test __str__() method.
    """


def test_append():
    """
    Create an empty unordered list object.
    Call append(7) and append(3) to test the method.
    """


def test_pop():
    """
    Use code in test_append() to create the list 7, 3
    Call pop(7) and pop(10) to test the full behavior of the method.
    """


def test_remove():
    """
    Use code in test_append() to create the list 7, 3
    Call remove(7) and remove(10) to test the full behavior of the method.
    """


def main():
    """
    Test UnorderedList methods with simple test cases.
    """
    test_prepend()
    # Call the testing functions here.
    # As you add a call to a new testing function, comment out the ones
    # that have been called already. Do NOT delete any of the calls.


if __name__ == '__main__':
    main()