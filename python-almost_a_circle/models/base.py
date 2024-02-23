#!/usr/bin/python3
"""Module for Base class"""
import json
import os


class Base:
    """Base class for managing instances"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a Base instance.

        Args:
            id (int): ID of the instance (default is None).
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string of representation of list dictionaries
        Args:
            list_dictionaries(list) : list of dictionaries

        Returns:
            str: JSON string representation of list_dictionnaries.
        """
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON string representation of list_objs into a file."""
        list_dictionaries = []
        filename = "{}.json".format(cls.__name__)

        if list_objs is not None:
            for obj in list_objs:
                list_dictionaries.append(obj.to_dictionary())

        with open(filename, 'w') as file:
            file.write(cls.to_json_string(list_dictionaries))

    def from_json_string(json_string):
        """Return the list of dictionaries represented by json_string"""
        if not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Return a instance with all attributes set

        Args:
            **dictionary: double pointer to a dictionary.

        Returns:
            Base: Instance with attributes set.
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        else:
            raise Exception("Wrong class")
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Return a list of instances from a file

        Returns:
            list : List of instances.
        """
        filename = "{}.json".format(cls.__name__)
        if not os.path.isfile(filename):
            return []

        with open(filename, "r") as file:
            file_read = file.read()
            list_dics = cls.from_json_string(file_read)

        instances = []
        for x in list_dics:
            instance = cls.create(**x)
            instances.append(instance)

        return instances
