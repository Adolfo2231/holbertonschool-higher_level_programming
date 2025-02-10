#!/usr/bin/python3

import json

"""
This module contains a function to return the JSON representation of
an object (string).
"""


def to_json_string(my_obj):
    """
    Returns the JSON representation of an object (string).

    Args:
        my_obj: The object to convert into a JSON string.

    Returns:
        str: The JSON representation of the object.
    """
    return json.dumps(my_obj)
