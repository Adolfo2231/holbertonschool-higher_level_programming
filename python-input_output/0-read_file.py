#!/usr/bin/python3

"""
This module contains a function to read and print the contents of a
text file in UTF-8 encoding.
"""


def read_file(filename=""):
    """
    Reads a text file (UTF8) and prints its content to stdout.

    Args:
        filename (str): The name of the file to read. Defaults to an
        empty string.
    """
    # Open the file in read mode with UTF-8 encoding
    with open(filename, 'r', encoding='utf-8') as file:
        # Read and print the file content without adding extra newlines
        print(file.read(), end="")
