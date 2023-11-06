#!/usr/bin/python3
"""lockedclass module"""


class MyInt(int):
    """LockedClass"""

    def __eq__(self, value):
        """area instance me"""
        return self.real != value

    def __ne__(self, value):
        """not equal"""
        return self.real == value
