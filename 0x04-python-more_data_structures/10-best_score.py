#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    keys = list(a_dictionary.keys())
    best_score = ""
    for key in keys:
        if a_dictionary[key] > a_dictionary.get(best_score, 0):
            best_score = key
    return best_score
