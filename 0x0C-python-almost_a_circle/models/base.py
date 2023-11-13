#!/usr/bin/python3
"""Base Class"""
import json
import csv
import os


class Base:
    """Base class that serves as the base for all other classes."""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes an instance of the Base class."""
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string representation of list_dictionaries."""
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(list_dictionaries):
        """Return the list of the JSON string representation json_string."""
        if list_dictionaries is None:
            return []
        return json.loads(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON string representation of list_objs to a file."""
        file_name = cls.__name__ + '.json'
        with open(file_name, "w", encoding='UTF-8') as f:
            if list_objs is None:
                json.dump([], f)
                return
            json.dump([json.loads(cls.to_json_string(obj.to_dictionary()))
                       for obj in list_objs], f)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all the attributes already set"""
        from .rectangle import Rectangle
        from .square import Square

        if cls.__name__ == "Rectangle":
            obj = Rectangle(1, 1)
        elif cls.__name__ == "Square":
            obj = Square(1)
        obj.update(**dictionary)
        return obj

    @classmethod
    def load_from_file_csv(cls):
        """Load from file csv."""
        data = []
        with open(cls.__name__ + ".csv", encoding="utf-8", mode="r") as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                # Convert values to integers
                for key in row:
                    row[key] = int(row[key])
                data.append(row)
        return list(map(lambda obj: cls.create(**obj), data))
