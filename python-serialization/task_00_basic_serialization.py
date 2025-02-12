#!/usr/bin/env python3

import json

"""
Task 00 Basic Serialization Module

This module provides functions to serialize a Python dictionary into a JSON
file and deserialize a JSON file back into a Python dictionary.

Functions:
    - serialize_and_save_to_file(data, filename): Serializes a dictionary and
      saves it as a JSON file.
    - load_and_deserialize(filename): Loads a JSON file and returns it as a
      dictionary.
"""


def serialize_and_save_to_file(data, filename):
    """
    Serializes a Python dictionary and saves it to a JSON file.
    If the file exists, it will be replaced.

    :param data: Dictionary to serialize
    :type data: dict
    :param filename: Name of the file to save JSON data
    :type filename: str
    """
    with open(filename, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, indent=4)


def load_and_deserialize(filename):
    """
    Loads JSON data from a file and deserializes it into a Python dictionary.

    :param filename: Name of the JSON file to read
    :type filename: str
    :return: Dictionary with deserialized data
    :rtype: dict
    """
    with open(filename, 'r', encoding='utf-8') as json_file:
        return json.load(json_file)
