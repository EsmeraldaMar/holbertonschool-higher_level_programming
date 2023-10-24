#!/usr/bin/python3
""" Create a new class Base """
import json


class Base:
    """ New Class Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries."""
        if list_dictionaries is None:
            return "[]"
        else:
            return (json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        """ Writes the JSON string representation of list_objs to a file"""
        file = "{}.json".format(cls.__name__)
        new = []
        if list_objs is None:
            pass
        else:
            for obj in list_objs:
                new.append(obj.to_dictionary())
        with open(file, "w", encoding="utf-8") as f:
            f.write(cls.to_json_string(new))

    @staticmethod
    def from_json_string(json_string):
        """ Returns the list of the JSON string representation json_string"""
        list = []
        if json_string is None:
            return (list)
        return (json.loads(json_string))

    @classmethod
    def create(cls, **dictionary):
        """ Returns an instance with all attributes already set """
        if cls.__name__ == "Rectangle":
            new_c = cls(1, 1)
        if cls.__name__ == "Square":
            new_c = cls(1)
        new_c.update(**dictionary)
        return (new_c)
