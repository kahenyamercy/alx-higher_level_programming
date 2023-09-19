#!/usr/bin/python3
"""Base module."""


class Base:
    """Base class for managing id attribute."""

    __nb_objects = 0  # Private class attribute keeps track of objects created

    def __init__(self, id=None):
        """Initialize the Base instance.

        Args:
            id (int): An optional integer id.
        """
        if id is not None:
            self.id = id
        else:
            # Increment the private class attribute and assign it to id
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
