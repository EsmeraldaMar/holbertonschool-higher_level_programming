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
    no_space = False
    for i in text:
        if i == "." or i == "?" or i == ":":
            print(i, end = "\n\n")
            no_space = True
        else:
            if no_space and i == " ":
                continue
            elif no_space and i != " ":
                no_space = False
            print(i, end = "")
        
    # for i in text:

    #     elif i is "." or i is "?" or i is ":":
    #         new_text += i + "\n\n"
    #         no_space = True
    #     else:
    #         new_text += i
    #         no_space = False
    #print(new_text, end='')
