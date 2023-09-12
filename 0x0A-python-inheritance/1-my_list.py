#!/usr/bin/python3
"""Prints a sorted list in ascending order"""


class MyList(list):
    """MyList is a subclass of the built-in list class."""

    def print_sorted(self):
        """
        Print the elements of the list in ascending sorted order.
        Example:
        >>> my_list = MyList([3, 1, 2])
        >>> my_list.print_sorted()
        [1, 2, 3]
        """
        sorted_list = sorted(self)
        print(sorted_list)
