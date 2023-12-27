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
    ul_obj = UnorderedList()
    ul_obj.prepend(7)
    ul_obj.prepend(3)
    ul_obj.prepend(6)
    
    print(ul_obj.search(7))  # This should print: True
    print(ul_obj.search(10))  # This should print: False


def test_print():
    """
    Use code in test_prepend() to create the list 6, 3, 7.
    Call print() to test __str__() method.
    """
    ul_obj = UnorderedList()
    ul_obj.prepend(7)
    ul_obj.prepend(3)
    ul_obj.prepend(6)
    
    print(ul_obj)  # This should print: 6,3,7


def test_append():
    """
    Create an empty unordered list object.
    Call append(7) and append(3) to test the method.
    """
    ul_obj = UnorderedList()
    ul_obj.append(7)
    ul_obj.append(3)
    print(ul_obj)  # This should print: 7,3


def test_pop():
    """
    Use code in test_append() to create the list 7, 3
    Call pop(7) and pop(10) to test the full behavior of the method.
    """
    ul_obj = UnorderedList()
    ul_obj.append(7)
    ul_obj.append(3)
    print(ul_obj.pop())  # This should print: 7
    print(ul_obj.pop())  # This should print: 3
    print(ul_obj.pop())  # This should print: None


def test_remove():
    """
    Use code in test_append() to create the list 7, 3
    Call remove(7) and remove(10) to test the full behavior of the method.
    """
    ul_obj = UnorderedList()
    ul_obj.append(7)
    ul_obj.append(3)
    print(ul_obj.remove(7))  # This should print: 7
    print(ul_obj)  # This should print: 3
    print(ul_obj.remove(10))  # This should print: None


def main():
    """
    Test UnorderedList methods with simple test cases.
    """
    test_prepend()
    test_size()
    test_search()
    test_print()
    test_append()
    test_pop()
    test_remove()


if __name__ == '__main__':
    main()