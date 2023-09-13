#!/usr/bin/python3
"""Defines student class"""


class Student:
    """
    Represents a student.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes this student with the given first name,
        last name, and age.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary of this student's attributes.

        Args:
            attrs (list): A list of attributes that can be retrieved.

        Returns:
            dict: A dictionary of this student's attributes.
        """
        if attrs is None:
            return self.__dict__
        else:
            return {key: value for key, value in
                    self.__dict__.items() if key in attrs}

    def reload_from_json(self, json):
        """
        Replaces all attributes of Student instance based on JSON dictionary.

        Args:
            json (dict): A dictionary containing attribute names and values.
        """
        for key, value in json.items():
            setattr(self, key, value)
