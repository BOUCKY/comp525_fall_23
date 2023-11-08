"""
unorderedlist.py
Jon Shallow
20231102
"""

from node import Node

class UnorderedList:
    """
    Class representation of an UnorderedList
    """

    def __init__(self):
        """
        Constructor
        """
        self.head = None

    def prepend(self, item):
        """
        Create node that has item and make it the first element in the
        unordered list.
        :param item: integer
        """
        new_node = Node(item)
        new_node.next = self.head
        self.head = new_node

    def size(self):
        """
        Count the number of elements in the unordered list.
        :return: integer
        """
        count = 0
        curr_node = self.head
        while curr_node:
            count += 1
            curr_node = curr_node.next
        return count

    def is_empty(self):
        """
        Check whether the unordered list has no nodes.
        :return: True if the unordered list object doesn't have any eleemnt.
        """
        return self.head is None

    def search(self, item):
        """
        Search for item in the unordered list.
        :param item: integer
        :return: True if item found. False otherwise.
        """
        curr_node = self.head
        while curr_node:
            if curr_node.get_data() == item:
                return True
            curr_node = curr_node.get_next()
        return False


    def __str__(self):
        """
        Create string representation of the unordered list object. The string
        shows the data items, separated by ','. If the list is empty, the
        string is empty string.
        :return: string
        """
        pass

    def append(self, item):
        # Appending happens at the end of the unsorted list.
        # Replace these comments with a well-formed docstring.
        pass

    def pop(self):
        # Popping happens at the front of the unsorted list.
        # If popping is successful, the method removes the 1st node and
        # returns the data item in the node. Otherwise, the method returns
        # None.
        # Replace these comments with a well-written docstring.
        pass

    def remove(self, item):
        # If the item is removed successfully, return the item.
        # Otherwise, return the `self._head`.
        # Replace these comments with a well-formed docstring.
        pass
