#!/usr/bin/python3
"""
This module contains MyList class.
"""


class MyList(list):
    """MyList extends list."""

    def print_sorted(self):
        """Prints sorted list in asc order."""

        print(sorted(self))
