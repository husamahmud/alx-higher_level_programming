#!/usr/bin/python3
"""Student class."""


class Student:
    """A class that represents a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a Student instance."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieve a dictionary representation of the Student instance."""
        return self.__dict__
