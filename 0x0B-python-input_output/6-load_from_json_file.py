#!/usr/bin/python3
"""lockedclass module"""
import json


def load_from_json_file(filename):
    """LockedClass"""
    with open(filename, 'r') as f:
        return json.load(f)
