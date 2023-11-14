#!/usr/bin/python3
"""Module for Base class"""

import csv
import json
import os


class Base:
    """Base Class"""
    __nb_objects = 0

    def __init__(self, id_=None):
        """Initializes a new instance of the Base class"""
        if id_ is not None:
            self.id = id_
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Converts a list of dictionaries to a JSON string representation"""
        if not list_dictionaries:
            return "[]"

        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """Converts a JSON string to a list of dictionaries"""
        if not json_string:
            return []

        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Creates a new instance of the class and initializes it
            with values from a dictionary"""
        if cls.__name__ == 'Rectangle':
            dummy = cls(1, 1)
        elif cls.__name__ == 'Square':
            dummy = cls(1)

        dummy.update(**dictionary)
        return dummy

    @classmethod
    def save_to_file(cls, list_objs):
        """Saves a list of instances to a JSON file"""
        filename = cls.__name__ + '.json'
        with open(filename, 'w', encoding='UTF-8') as json_file:
            if not list_objs:
                json_file.write("[]")
            else:
                list_of_dicts = [obj.to_dictionary() for obj in list_objs]
                json_file.write(Base.to_json_string(list_of_dicts))

    @classmethod
    def load_from_file(cls):
        """Loads a list of instances from a JSON file"""
        filename = cls.__name__ + '.json'
        list_of_instances = []

        if os.path.exists(filename):
            with open(filename, 'r', encoding='UTF-8') as json_file:
                json_str = json_file.read()
                list_of_dicts = cls.from_json_string(json_str)
                for dictionary in list_of_dicts:
                    list_of_instances.append(cls.create(**dictionary))
        return list_of_instances

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Saves a list of instances to a CSV file"""
        filename = cls.__name__ + '.csv'
        name = cls.__name__
        fieldnames = (['id', 'size', 'x', 'y'] if name != 'Rectangle'
                      else ['id', 'width', 'height', 'x', 'y'])
        with open(filename, 'w', newline='', encoding='UTF-8') as csv_file:
            csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            csv_writer.writeheader()

            if not list_objs:
                return

            for obj in list_objs:
                csv_writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Loads a list of instances from a CSV file"""
        filename = cls.__name__ + '.csv'
        name = cls.__name__
        fieldnames = (['id', 'size', 'x', 'y'] if name != 'Rectangle'
                      else ['id', 'width', 'height', 'x', 'y'])
        if os.path.exists(filename):
            with open(filename, 'r', newline='', encoding='UTF-8') as csv_file:
                csv_reader = csv.DictReader(csv_file, fieldnames=fieldnames)
                next(csv_reader)

                list_dicts = []
                for row in csv_reader:
                    new_row = {}
                    for k, val in row.items():
                        new_row[k] = int(val)
                    list_dicts.append(new_row)

                return [cls.create(**dictionary) for dictionary in list_dicts]
        return []
