#!/usr/bin/env python3

"""
Task 03 XML Serialization Module

This module provides functionality to serialize a Python dictionary
into an XML file and deserialize an XML file back into a Python dictionary.

Functions:
    - serialize_to_xml(dictionary, filename): Serializes a dictionary to XML
      and saves it as a file.
    - deserialize_from_xml(filename): Loads XML data from a file and converts
      it back into a dictionary.
"""


import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serializes a Python dictionary into an XML file.

    :param dictionary: The dictionary to be serialized.
    :type dictionary: dict
    :param filename: The filename to save the XML data.
    :type filename: str
    """
    root = ET.Element("data")

    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    tree = ET.ElementTree(root)
    try:
        tree.write(filename, encoding='utf-8', xml_declaration=True)
    except Exception as e:
        print(f"Error writing XML file: {e}")


def deserialize_from_xml(filename):
    """
    Deserializes an XML file back into a Python dictionary.

    :param filename: The filename of the XML file to read.
    :type filename: str
    :return: A dictionary with deserialized XML data.
    :rtype: dict
    """
    try:
        tree = ET.parse(filename)
        root = tree.getroot()

        return {child.tag: child.text for child in root}
    except (FileNotFoundError, ET.ParseError) as e:
        print(f"Error reading XML file: {e}")
        return None
