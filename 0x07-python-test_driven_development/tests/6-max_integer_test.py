#!/usr/bin/python3

import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInt(unittest.TestCase):
    def test_max(self):
        array = [
                [5, 6 ,20],
                [100, 6, 10],
                []
                ]
        result = [max_integer(i) for i in array]
        self.assertEqual(result, [20, 100, None])

    def test_None(self):
        result = max_integer([])
        self.assertEqual(result, None)

if __name__ == "__main__":
    unittest.main()
