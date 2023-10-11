#!/usr/bin/python3
"""
Module Name: 5-text_indentation.py
des: prints a text with two new lines after each character (.,? and :)
"""


def text_indentation(text):
    """
    Text Indenation Function

    Args:
    text (str): string of text
    """

    if type(text) is not str:
        raise TypeError("text must be a string")
    
    no_space = True
    size = 0
    text = text.strip()
    new_text = ""
    for i in text:
        if i is " " and no_space:
            pass
        elif i is "." or i is "?" or i is ":":
            new_text += i + "\n\n"
            no_space = True
        else:
            new_text += i
            no_space = False
        print(new_text,end='')
