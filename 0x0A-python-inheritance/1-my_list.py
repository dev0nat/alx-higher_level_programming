#!/usr/bin/python3
"""Defines MyList"""

class MyList(list):
    """A class that inherits from list"""

    def print_sorted(self):
        """Prints sorted list"""
        print(sorted(self))
