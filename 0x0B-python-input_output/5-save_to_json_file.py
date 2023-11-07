#!/usr/bin/python3
"""lockedclass module"""
import json


def save_to_json_file(my_obj, filename):
    """LockedClass"""
    with open(filename, 'w') as f:
        f.write(json.dumps(my_obj))
