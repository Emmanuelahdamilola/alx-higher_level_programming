#!/usr/bin/python3
"""Defines a derived class"""


class MyList(list):
    """
    A custom list class that inherits from the built-in list class.
    Attributes:
        Inherits all attributes from the list class.
    """

    def print_sorted(self):
        """
        Prints the list in ascending sorted order.

        This method sorts the elements of the list in ascending order and then
        prints them.

        Args:
            None

        Returns:
            None
        """
        print(sorted(self))
