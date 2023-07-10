#!/usr/bin/python3

class MyList(list):
    """A class that inherits from the list class."""

    def print_sorted(self):
        """Print the list in ascending order."""
        sorted_list = sorted(self)
        print(sorted_list)
