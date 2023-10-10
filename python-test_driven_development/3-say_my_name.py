#!/usr/bin/python3
"""
Module Name: 3-say_my_name.py
des: prints My Name is <first name> <last name>
"""


def say_my_name(first_name, last_name=""):
    """
    say_my_name - prints first name and last name
    first_name - first name entered
    last_name - last name entered

    Result:
    Prints: My name is <first name> <last name>
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {:s} {:s}".format(first_name, last_name))
