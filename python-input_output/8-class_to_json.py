#!/usr/bin/python3
"""
This module contains a function that returns the dictionary description
with simple data structures for JSON serialization of an object.
"""


def class_to_json(obj):
    """
    Returns the dictionary description of an object for JSON serialization.
    Args:
        obj: An instance of a class.
    Returns:
        dict: Dictionary containing all serializable attributes of the object.
    """
    return obj.__dict__
