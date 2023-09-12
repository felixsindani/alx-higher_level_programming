#!/usr/bin/python3
"""Defines class MyList that inherits from list"""

class MyList(list):
    """prints the list, and sorts them(ascending sort)"""

    def print_sorted(self):
        """Print the list and sort in ascending order."""
        print(sorted(self))