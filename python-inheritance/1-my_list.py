#!/usr/bin/python3
"""
Module 1-my_list
Defines a subclass of list with a method to print the list in sorted order.
"""


class MyList(list):
    """
    A subclass of list that includes a method to print the list sorted.
    """

    def print_sorted(self):
        """
        Prints the list in ascending order without modifying the original list.
        """
        print(sorted(self))
