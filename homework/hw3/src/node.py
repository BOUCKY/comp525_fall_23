"""
node.py
Jon Shallow
20231102
"""

class Node:
    """
    Class representation of Node
    """

    def __init__(self, data):
        """
        Constructor

        :param data: the data for the node
        :type data: any
        """
        self.data = data
        self.next = None

    def get_data(self):
        """
        Gets the data from the node

        :return: the data in the node
        :rtype: any
        """
        return self.data

    def set_data(self, new_data):
        """
        Set the new_data in the node

        :param new_data: the new data to set
        :type new_data: any
        """
        self.data = new_data

    def get_next(self):
        """
        gets the Next property

        :return: the next property
        :rtype: Node | None
        """
        return self.next

    def set_next(self, new_next):
        """
        Sets a new node the be the next property

        :param new_next: The next Node
        :type new_next: Node | None
        """
        self.next = new_next
