#!/usr/bin/python3

import json

"""
This module contains functions to write an object to a text file
using its JSON representation and to create an object from a JSON file.
"""


def load_from_json_file(filename):
    """
    Creates an object from a JSON file.
    Args:
        filename (str): The name of the file to read from.
    Returns:
        object: The Python object represented by the JSON file.
    """
    with open(filename, "r", encoding="utf-8") as file:
        data = json.load(file)
        # Ordena el diccionario por claves si es un diccionario
        return dict(sorted(data.items())) if isinstance(data, dict) else data
