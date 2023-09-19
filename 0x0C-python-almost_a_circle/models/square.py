#!/usr/bin/python3
"""Square module."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class inherits from Rectangle."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a Square instance.

        Args:
            size (int): Size of the square.
            x (int): x-coordinate of the square's position.
            y (int): y-coordinate of the square's position.
            id (int): Unique identifier for the square.

        Attributes:
            id (int): Unique identifier for the square.
            width (int): Width of the square (inherited from Rectangle).
            height (int): Height of the square (inherited from Rectangle).
            x (int): x-coordinate of square's
            position (inherited from Rectangle).
            y (int): y-coordinate of square's
            position (inherited from Rectangle).
        """
        super().__init__(size, size, x, y, id)  # Call super class constructor
        self.size = size

    @property
    def size(self):
        """Getter for size attribute."""
        return self.__width

    @size.setter
    def size(self, value):
        """Setter for size attribute."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value
        self.__height = value

    def __str__(self):
        """Return a string representation of the Square instance."""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.size)

    def update(self, *args, **kwargs):
        """Update attributes of Square instance using provided arguments.

        Args:
            *args: Arguments in the following order - id, size, x, y.
            **kwargs: Key-value arguments where each key represents attribute.
        """
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Return a dictionary representation of the Square instance.

        Returns:
            dict: A dictionary containing id, size, x, and y attributes.
        """
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }
