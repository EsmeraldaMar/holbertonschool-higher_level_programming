#!/usr/bin/python3
""" Student to disk and reload """


class Student:
    """ New class Student"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Retrieves a dictionary representation of a Student instance """
        if attrs is None:
            return (self.__dict__)
        else:
            if isinstance(attrs, list) and all(isinstance(item, str)
                                               for item in attrs):
                result = {}
                for attr in attrs:
                    if hasattr(self, attr):
                        result[attr] = getattr(self, attr)
                return result

    def reload_from_json(self, json):
        """ Replaces all attributes of the Student instance"""
        if not isinstance(json, dict):
            return
        if "first_name" in json:
            self.first_name = json["first_name"]
        if "last_name" in json:
            self.last_name = json["last_name"]
        if "age" in json:
            self.age = json["age"]
