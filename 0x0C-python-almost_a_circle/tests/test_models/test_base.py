#!/usr/bin/python3
"""testing Base module"""
import unittest
from models.base import Base


class TestBaseClass(unittest.TestCase):
    """test base class"""

    def test_creating(self):
        """creating instances"""
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)
        b3 = Base(12)
        self.assertEqual(b3.id, 12)
