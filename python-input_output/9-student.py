#!/usr/bin/python3
"""
This module defines a Student class with attributes and a method
to retrieve a dictionary representation of a Student instance.
"""


class Student:
    """
    Defines a Student with first_name, last_name, and age attributes.
    """
    def __init__(self, first_name, last_name, age):
        """
        Initializes a Student instance.
        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Retrieves a dictionary representation of a Student instance.
        Returns:
            dict: The dictionary representation of the Student instance.
        """
        return self.__dict__
