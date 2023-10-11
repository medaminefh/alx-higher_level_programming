#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    out = {}
    keys = list(a_dictionary.keys())
    for key in keys:
        out[key] = a_dictionary.get(key) * 2
    return out
