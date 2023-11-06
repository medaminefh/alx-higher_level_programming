#!/usr/bin/python3
"""lockedclass module"""


def inherits_from(obj, a_class):
    """LockedClass"""

    return issubclass(type(obj), a_class) and type(obj) is not a_class
