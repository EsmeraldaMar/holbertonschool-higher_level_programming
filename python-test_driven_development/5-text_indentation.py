#!/usr/bin/python3
"""
Module Name: 5-text_indentation.py
des: prints a text with two new lines after each character (.,? and :)
"""


def text_indentation(text):
    """
    Text Indenation Function

    Args:
    text (str): string of text to be indented

    Return: Indented Text
    """

    if type(text) is not str:
        raise TypeError("text must be a string")
 
    text = text.strip()
    for i in text:
        if i is "." or i is "?" or i is ":":
            print(i, end = "\n\n")
        else:
            print(i, end = "")
        
    # for i in text:

    #     elif i is "." or i is "?" or i is ":":
    #         new_text += i + "\n\n"
    #         no_space = True
    #     else:
    #         new_text += i
    #         no_space = False
    #print(new_text, end='')
