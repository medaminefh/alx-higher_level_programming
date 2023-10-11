#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sorted_arr = list(a_dictionary.keys())
    # sort the list
    sorted_arr.sort()

    for key in sorted_arr:
        print("{}: {}".format(key, a_dictionary.get(key)))
