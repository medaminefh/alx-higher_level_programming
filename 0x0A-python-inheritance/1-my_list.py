#!/usr/bin/python3
"""lockedclass module"""


class MyList(list):
    """LockedClass"""

    def print_sorted(self):
        """print sorted"""
        out = self[:]
        out.sort()
        print(out)
