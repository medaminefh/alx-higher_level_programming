#!/usr/bin/python3
def no_c(my_string):
    my_str = ""
    for char in my_string:
        if char in ["c", "C"]:
            continue
        my_str += char
    return my_str
