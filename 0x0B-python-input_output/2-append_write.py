#!/usr/bin/python3
"""lockedclass module"""


def append_write(filename="", text=""):
    """LockedClass"""

    with open(filename, 'a', encoding="UTF-8") as f:
        return f.write(text)
