#!/usr/bin/python3
""" Append to a file """


def append_write(filename="", text=""):
    """ A function that adds a string to
a UTF8 text file's end and returns the character count added."""
    with open(filename, 'a', encoding='utf-8') as f:
        return (f.write(text))
