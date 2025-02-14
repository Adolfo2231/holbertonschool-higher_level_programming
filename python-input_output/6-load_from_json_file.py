#!/usr/bin/python3


"""
This module contains functions to write an object to a text file
using its JSON representation and to create an object from a JSON file.
"""


import json


def load_from_json_file(filename):
    """
    Creates an object from a JSON file.
    Args:
        filename (str): The name of the file to read from.
    Returns:
        object: The Python object represented by the JSON file.
    """
    with open(filename, "r", encoding="utf-8") as f:
        # Ordena el diccionario por claves si es un diccionario
        return json.load(f)
