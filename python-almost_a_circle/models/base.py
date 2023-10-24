#!/usr/bin/python3
""" Create a new class Base """
from os import path
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
        new = []
        if list_dictionaries is None:
            return new
        else:
            return (json.dumps(list_dictionaries))
