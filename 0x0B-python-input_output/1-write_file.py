#!/usr/bin/python3
"""lockedclass module"""


def write_file(filename="", text=""):
    """LockedClass"""

    with open(filename, 'w', encoding="UTF-8") as f:
        return f.write(text)
