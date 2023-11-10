#!/usr/bin/python3
"""testing Base module"""
import unittest
from models.rectangle import Rectangle


class TestRectangleClass(unittest.TestCase):
    """test rectangle class"""

    def test_creating(self):
        """creating instances"""
        r1 = Rectangle(10, 2, 0, 0, 1)
        self.assertEqual(r1.id, 1)
        r2 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r2.id, 12)

    def test_validation(self):
        """test the validation of the creation"""
        self.assertRaises(TypeError, Rectangle, 10, "2")
        with self.assertRaises(TypeError):
            Rectangle(10,"2")
        self.assertRaises(ValueError, Rectangle, 10, -1)

    def test_area(self):
        """test the area of the rectangle"""
        r1 = Rectangle(10, 5)
        self.assertEqual(r1.area(), 50)

    def test_display(self):
        """test display function"""
        r1 = Rectangle(4, 6)
        d = "####\n####\n####\n####\n####\n####\n"
        self.assertEqual(r1.display(), d)

    def test_str(self):
        """this is to test the __str__ function"""
        r1 = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r1), "[Rectangle] (12) 2/1 - 4/6")
