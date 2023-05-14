#!/usr/bin/python3
"""Defines a function that writes a string to a text file"""


def read_file(filename=""):
    """reads from a file and prints its contents to stdout."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
