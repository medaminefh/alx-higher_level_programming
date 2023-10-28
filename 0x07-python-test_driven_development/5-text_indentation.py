#!/usr/bin/python3
"""
text_indentation  module
text_indentation func
"""


def text_indentation(text):
    """text_indentation function"""
    if type(text) is not str:
        raise TypeError("text must be a string")
    for i in range(len(text)):
        if text[i] in ['.', '?', ':']:
            print("{}\n\n".format(text[i]), end="")
            continue
        if text[i-1] in ['.', '?', ':'] and text[i] == ' ':
            continue
        print(text[i], end="")
