#!/usr/bin/python3
"""a function that writes a string to a file and returns written text"""


def write_file(filename="", text=""):
    """ Function that writes to a text file
    Args:
        filename: name of the file
        text: string to be written

        Returns: characters written in a file.
    """

    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
