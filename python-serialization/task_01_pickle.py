#!/usr/bin/env python3

"""
Task 01 Pickle Serialization Module

This module defines a custom Python class that can be serialized and
deserialized using the pickle module.

Classes:
    - CustomObject: A class with attributes name, age, and is_student, and
      methods to serialize and deserialize instances.
"""


import pickle


class CustomObject:
    """
    A custom Python class representing an object with name, age, and
    is_student attributes.
    """

    def __init__(self, name, age, is_student):
        """
        Initializes a CustomObject instance.

        :param name: Name of the person
        :type name: str
        :param age: Age of the person
        :type age: int
        :param is_student: Whether the person is a student
        :type is_student: bool
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        Displays the attributes of the CustomObject instance.
        """
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serializes the current instance and saves it to a file using pickle.

        :param filename: The filename to save the serialized object
        :type filename: str
        """
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
        except Exception as e:
            print(f"Serialization error: {e}")

    @classmethod
    def deserialize(cls, filename):
        """
        Deserializes an instance of CustomObject from a file using pickle.

        :param filename: The filename to load the serialized object from
        :type filename: str
        :return: An instance of CustomObject or None if an error occurs
        :rtype: CustomObject or None
        """
        try:
            with open(filename, 'rb') as file:
                return pickle.load(file)
        except (FileNotFoundError, pickle.UnpicklingError, EOFError) as e:
            print(f"Deserialization error: {e}")
            return None
