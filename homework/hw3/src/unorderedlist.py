"""
unorderedlist.py
Alexis Boucouvalas
12/23/2023
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
        items = []
        curr_node = self.head
        while curr_node:
            items.append(str(curr_node.get_data()))
            curr_node = curr_node.get_next()
        return ','.join(items)


    def append(self, item):
        """
        Append an item at the end of the unordered list.
        :param item: integer
        """
        new_node = Node(item)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.get_next():
            last_node = last_node.get_next()
        last_node.set_next(new_node)


    def pop(self):
        """
        Remove and return the first item in the unordered list.
        :return: integer if the list is not empty, otherwise None
        """
        if not self.head:
            return None
        popped_item = self.head.get_data()
        self.head = self.head.get_next()
        return popped_item

    def remove(self, item):
        """
        Remove the first occurrence of the item from the unordered list.
        :param item: integer
        :return: item if found and removed, otherwise self._head
        """
        prev_node = None
        curr_node = self.head
        while curr_node:
            if curr_node.get_data() == item:
                if prev_node:
                    prev_node.set_next(curr_node.get_next())
                else:
                    self.head = curr_node.get_next()
                return item
            prev_node = curr_node
            curr_node = curr_node.get_next()
        return self.head
