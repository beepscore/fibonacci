#!/usr/bin/env python3

import unittest
import fibonacci


class TestSparseBinaryNumber(unittest.TestCase):

    def setUp(self):
        self.fibonacci_numbers = [
            0,
            1,
            1,
            2,
            3,
            5,
            8,
            13,
            21,
            34,
            55,
            89,
            144
        ]

    def test_fibonacci(self):
        for index in range(0, len(self.fibonacci_numbers)):
            actual = fibonacci.fibonacci(index)
            expected = self.fibonacci_numbers[index]
            self.assertEqual(expected, actual,
                             "expected fibonacci({}) == {} but got {}"
                             .format(index, expected, actual))

    def test_fibonacci_n_large(self):
        """ Current implementation is slow for large n.
        On Macbook Pro, fibonacci(36) takes ~ 10 seconds
        python3 -m unittest discover test
        ..
        ----------------------------------------------------------------------
        Ran 2 tests in 10.982s
        OK
        """
        n = 36
        actual = fibonacci.fibonacci(n)
        expected = 14930352
        self.assertEqual(expected, actual,
                         "expected fibonacci({}) == {} but got {}"
                         .format(n, expected, actual))


if __name__ == "__main__":
    unittest.main()
