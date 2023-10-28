#!/usr/bin/python3
"""
say_my_name  module
say_my_name func
"""


def say_my_name(first_name, last_name=""):
    """say_my_name function"""
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("first_name must be a string")

    print("{} {}".format(first_name, last_name))
