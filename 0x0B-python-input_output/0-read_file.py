#!/usr/bin/python3
"""lockedclass module"""


def read_file(filename=""):
    """LockedClass"""

    with open(filename, encoding="UTF-8") as f:
        print(f.read(), end="")
