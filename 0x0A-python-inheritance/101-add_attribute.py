#!/usr/bin/python3
"""lockedclass module"""


def add_attribute(obj, attr, value):
    """set attr"""
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attr, value)
