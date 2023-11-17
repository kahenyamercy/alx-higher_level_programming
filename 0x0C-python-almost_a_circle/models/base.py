#!/usr/bin/python3
"""Base module."""
import json  # Import the json module
import csv   # Import the csv module


class Base:
    """Base class for managing id attribute."""

    __nb_objects = 0  # Priv class attr to keep track of objects created

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

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string representation of list_dictionaries.

        Args:
            list_dictionaries (list): A list of dictionaries.

        Returns:
            str: A JSON string representation of list_dictionaries.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON string representation of list_objs to a file.

        Args:
            list_objs (list): A list of instances that inherit from Base.
        """
        if list_objs is None:
            list_objs = []
        filename = cls.__name__ + ".json"  # Construct the JSON filename
        with open(filename, mode="w", encoding="utf-8") as file:
            obj_dicts = [obj.to_dictionary() for obj in list_objs]
            json_str = cls.to_json_string(obj_dicts)
            file.write(json_str)

    @staticmethod
    def from_json_string(json_string):
        """Return the list of dictionaries from a JSON string representation.

        Args:
            json_string (str): JSON string representing  list of dictionaries.

        Returns:
            list: A list of dictionaries.
        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Create an instance with attributes already set from a dictionary.

        Args:
            **dictionary: A dictionary containing attribute values.

        Returns:
            Base: instance of class with attributes set based on dictionary.
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)  # Create a dummy Rectangle instance
        elif cls.__name__ == "Square":
            dummy = cls(1)  # Create a dummy Square instance
        dummy.update(**dictionary)  # Update attributes with dictionary values
        return dummy

    @classmethod
    def load_from_file(cls):
        """Return a list of instances loaded from a JSON file.

        Returns:
            list: A list of instances.
        """
        filename = cls.__name__ + ".json"  # Construct the JSON filename
        try:
            with open(filename, mode="r", encoding="utf-8") as file:
                json_str = file.read()
                obj_dicts = cls.from_json_string(json_str)
                return [cls.create(**d) for d in obj_dicts]
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serialize instances to a CSV file.

        Args:
            list_objs (list): A list of instances that inherit from Base.
        """
        if list_objs is None:
            list_objs = []
        filename = cls.__name__ + ".csv"  # Construct the CSV filename
        with open(filename, mode="w", encoding="utf-8") as file:
            writer = csv.writer(file)
            for obj in list_objs:
                if cls.__name__ == "Rectangle":
                    writer.writerow([obj.id, obj.width, obj.height, obj.x, obj.y])
                elif cls.__name__ == "Square":
                    writer.writerow([obj.id, obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        """Deserialize instances from a CSV file.

        Returns:
            list: A list of instances.
        """
        filename = cls.__name__ + ".csv"  # Construct the CSV filename
        try:
            with open(filename, mode="r", encoding="utf-8") as file:
                reader = csv.reader(file)
                instances = []
                for row in reader:
                    if cls.__name__ == "Rectangle" and len(row) == 5:
                        id, width, height, x, y = map(int, row)
                        obj_dict = {"id": id, "width": width, "height": height, "x": x, "y": y}
                        instances.append(cls.create(**obj_dict))
                    elif cls.__name__ == "Square" and len(row) == 4:
                        id, size, x, y = map(int, row)
                        obj_dict = {"id": id, "size": size, "x": x, "y": y}
                        instances.append(cls.create(**obj_dict))
                return instances
        except FileNotFoundError:
            return []
