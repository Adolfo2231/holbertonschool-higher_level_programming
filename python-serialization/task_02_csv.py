#!/usr/bin/env python3
"""
Task 02 CSV to JSON Conversion Module

This module provides functionality to convert data from a CSV file
into a JSON file using serialization techniques.

Functions:
    - convert_csv_to_json(csv_filename): Converts a CSV file to JSON and
      saves it as data.json.
"""

import csv
import json


def convert_csv_to_json(csv_filename):
    """
    Converts a CSV file to JSON format and saves it as data.json.

    :param csv_filename: The filename of the CSV file to be converted.
    :type csv_filename: str
    :return: True if conversion is successful, False otherwise.
    :rtype: bool
    """
    try:
        with open(csv_filename, mode='r', encoding='utf-8') as csv_file:
            reader = csv.DictReader(csv_file)
            data = list(reader)

        with open('data.json', mode='w', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=4)

        return True
    except FileNotFoundError:
        print(f"Error: The file {csv_filename} was not found.")
        return False
    except Exception as e:
        print(f"Unexpected error: {e}")
        return False
